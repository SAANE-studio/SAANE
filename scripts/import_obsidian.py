"""Explicit-allowlist Obsidian import. Dry-run by default; no vault writes.
Python 3.10+, standard library only. See docs/research-authoring.md.
"""
from pathlib import Path
import argparse, hashlib, html, json, re, shutil, sys, urllib.parse
import xml.etree.ElementTree as ET

class ImportFailure(ValueError): pass

def slug(s):
    return re.sub(r'[^\w\- ]','',s.lower()).strip().replace(' ','-')

class Importer:
    def __init__(self, manifest, root):
        self.m=manifest
        self.root=Path(root).resolve()
        self.vault=Path(manifest['vault']).resolve()
        self.notes=manifest.get('notes',{})
        self.assets=manifest.get('assets',[])
        self.pending={}
        self.report=[]
    def path(self, name):
        p=(self.vault/name).resolve()
        if not p.is_relative_to(self.vault):raise ImportFailure('Path escapes vault: '+name)
        if not p.is_file():raise ImportFailure('Missing allowed file: '+name)
        return p
    def resolve(self, name, current, note=False):
        name=urllib.parse.unquote(name).replace('\\','/')
        options=list(self.notes) if note else self.assets
        names={name,str(Path(current).parent/name).replace('\\','/')}
        if note:names.update({n+'.md' for n in list(names) if not n.endswith('.md')})
        candidates=[n for n in options if n in names]
        if not candidates:
            candidates=[n for n in options if Path(n).name==name or (note and Path(n).stem==name)]
        candidates=list(dict.fromkeys(candidates))
        if len(candidates)!=1:
            raise ImportFailure(('Ambiguous' if candidates else 'Missing or not publication-approved')+': '+name+' '+str(candidates))
        self.path(candidates[0])
        return candidates[0]
    def asset(self, key, article):
        data=self.path(key).read_bytes()
        ext=Path(key).suffix.lower()
        safe=slug(Path(key).stem) or 'asset'
        filename=safe+'-'+hashlib.sha256(data).hexdigest()[:10]+ext
        target=Path('static/images/research')/article/filename
        self.pending[target]=data
        self.report.append('asset: '+key+' -> '+str(target))
        return '/'+str(target.relative_to('static')).replace('\\','/')
    def fragment(self,text,fragment):
        if not fragment:return text
        if fragment.startswith('^'):
            marker=fragment[1:]
            blocks=re.split(r'\n\s*\n',text)
            matches=[]
            for i,b in enumerate(blocks):
                if re.search(r'\^'+re.escape(marker)+r'\s*$',b):
                    matches.append((blocks[i-1]+'\n\n'+b) if b.strip()=='^'+marker and i else b)
            if len(matches)!=1:raise ImportFailure('Missing or ambiguous block: '+fragment)
            return matches[0]
        lines=text.splitlines()
        searchable=[];fence=None
        for i,line in enumerate(lines):
            m=re.match(r'^\s*(' + chr(96) + r'{3,}|~{3,})',line)
            if m:
                if fence is None:fence=m[1][0]
                elif m[1][0]==fence:fence=None
                continue
            if fence is None:searchable.append(i)
        matches=[i for i,l in enumerate(lines) if i in searchable and re.match(r'^#{1,6}\s+',l) and re.sub(r'^#+\s+','',l).strip()==fragment]
        if len(matches)!=1:raise ImportFailure('Missing or ambiguous heading: '+fragment)
        start=matches[0];level=len(re.match(r'^#+',lines[start])[0]);end=len(lines)
        for i in range(start+1,len(lines)):
            if i not in searchable:continue
            m=re.match(r'^(#{1,6})\s+',lines[i])
            if m and len(m[1])<=level:end=i;break
        return '\n'.join(lines[start:end])
    def convert(self,key,article,stack=(),fragment='',prefix=''):
        if key in stack:raise ImportFailure('Embed cycle: '+' -> '.join((*stack,key)))
        text=self.path(key).read_text(encoding='utf-8-sig')
        text=re.sub(r'\A\s*---\r?\n.*?\r?\n---\r?\n','',text,flags=re.S)
        # Comments are never emitted, even inside code examples.
        if text.count('%%')%2:raise ImportFailure('Unclosed private comment: '+key)
        text=re.sub(r'%%.*?%%','',text,flags=re.S)
        text=self.fragment(text,fragment)
        held=[]
        def hold(m):
            held.append(m[0]);return '\x00CODE'+str(len(held)-1)+'\x00'
        text=re.sub(r'(?ms)^([ \t]*)(~~~+|'+chr(96)+r'{3,})[^\n]*\n.*?^\1\2[ \t]*$|'+chr(96)+r'+[^'+chr(96)+r'\n]*'+chr(96)+r'+',hold,text)
        def image(src,label='',width=''):
            ext=Path(src).suffix.lower()
            if ext in ('.png','.jpg','.jpeg','.gif','.webp','.svg','.avif'):
                size='large'
                if width:
                    w=int(width.split('x')[0]);size='small' if w<=360 else 'medium' if w<=560 else 'large' if w<=740 else 'wide'
                return '{{< research-image src="'+src+'" alt="'+html.escape(label,quote=True)+'" size="'+size+'" >}}'
            kind={'.mp4':'video','.webm':'video','.ogv':'video','.mp3':'audio','.wav':'audio','.ogg':'audio','.m4a':'audio','.pdf':'pdf'}.get(ext)
            if not kind:raise ImportFailure('Unsupported embed format: '+src)
            return '{{< research-media type="'+kind+'" src="'+src+'" title="'+html.escape(label,quote=True)+'" >}}'
        def wiki(m):
            embed=bool(m[1]);raw=m[2]
            dest,*alias=raw.split('|',1)
            target,sep,frag=dest.partition('#')
            label=alias[0] if alias else (frag or Path(target).stem)
            is_note=not Path(target).suffix or Path(target).suffix.lower()=='.md'
            if is_note:
                resolved=self.resolve(target,key,True) if target else key
                clean=self.path(resolved).read_text(encoding='utf-8-sig')
                if frag:self.fragment(clean,frag)
                if embed:
                    token='embed-'+hashlib.sha256((key+raw+str(m.start())).encode()).hexdigest()[:8]+'-'
                    converted=self.convert(resolved,article,(*stack,key),frag,token)
                    held.append(converted)
                    return '\n\x00CODE'+str(len(held)-1)+'\x00\n'
                url=self.notes[resolved].get('url')
                if not url:raise ImportFailure('Wikilink has no approved published URL: '+resolved)
                output=self.notes[resolved].get('output')
                if resolved!=self.selected and (not output or not (self.root/output).is_file()):
                    raise ImportFailure('Wikilink target has not been imported: '+resolved)
                if frag:url+='#'+('block-'+frag[1:] if frag.startswith('^') else slug(frag))
                return '['+label.replace(']','\\]')+']('+url+')'
            resolved=self.resolve(target,key)
            url=self.asset(resolved,article)
            if embed:return image(url,Path(target).stem,label if alias and re.fullmatch(r'\d+(?:x\d+)?',label) else '')
            return '['+label.replace(']','\\]')+']('+url+')'
        text=re.sub(r'(!?)\[\[([^\]]+)\]\]',wiki,text)
        def data_svg(m):
            data=urllib.parse.unquote(m[2].replace(r'\(','(').replace(r'\)',')')).encode()
            try: node=ET.fromstring(data)
            except ET.ParseError as e:raise ImportFailure('Invalid SVG data URI: '+str(e))
            if not node.tag.endswith('svg'):raise ImportFailure('Data URI is not SVG')
            if re.search(rb'<script|onload=|javascript:',data,re.I):raise ImportFailure('Active SVG is not accepted')
            name='diagram-'+hashlib.sha256(data).hexdigest()[:10]+'.svg'
            target=Path('static/images/research')/article/name;self.pending[target]=data
            return image('/'+str(target.relative_to('static')).replace('\\','/'),'Diagram',m[1] if m[1].isdigit() else '')
        text=re.sub(r'!\[([^\]]*)\]\(data:image/svg\+xml(?:;charset=[^,]+)?,(.*?%3E)\)',data_svg,text)
        def markdown_asset(m):
            label,dest=m[1],m[2]
            if re.match(r'https?://',dest):
                self.report.append('external image retained: '+dest);return m[0]
            if dest.startswith('/'):raise ImportFailure('Unvalidated absolute image URL: '+dest)
            resolved=self.resolve(dest.strip('<>'),key)
            return image(self.asset(resolved,article),label)
        text=re.sub(r'!\[([^\]]*)\]\(([^()\n]+)\)',markdown_asset,text)
        text=re.sub(r'==(.+?)==',lambda m:'{{< research-mark >}}'+m[1]+'{{< /research-mark >}}',text)
        # Explicit anchors preserve source block references.
        text=re.sub(r'(?m)^(.+?)\s+\^([\w-]+)\s*$',lambda m:'{{< research-anchor "'+prefix+'block-'+m[2]+'" >}}\n\n'+m[1],text)
        text=re.sub(r'(?m)^\^([\w-]+)\s*$',lambda m:'{{< research-anchor "'+prefix+'block-'+m[1]+'" >}}',text)
        if 'data:image' in text:
            raise ImportFailure('Unsupported data URI; export an approved local asset')
        if prefix:
            text=re.sub(r'(?m)^(#{1,6}\s+)(.+)$',lambda m:m[1]+m[2]+' {#'+prefix+slug(m[2])+'}',text)
        for i,code in enumerate(held):text=text.replace('\x00CODE'+str(i)+'\x00',code)
        return text
    def run(self,selected,write=False):
        if selected not in self.notes:raise ImportFailure('Selected note not in publication manifest')
        self.selected=selected;meta=self.notes[selected]
        output=Path(meta['output'])
        if output.is_absolute() or '..' in output.parts or not str(output).replace('\\','/').startswith('content/'):
            raise ImportFailure('Output must stay inside content/')
        article=meta.get('slug',Path(output).stem)
        if not re.fullmatch(r'[a-z0-9-]+',article):raise ImportFailure('Invalid article slug')
        body=self.convert(selected,article)
        target=self.root/output
        if target.exists():
            old=target.read_text(encoding='utf-8')
            match=re.match(r'\A---\n.*?\n---\n',old,re.S)
            if not match:raise ImportFailure('Existing output needs YAML front matter')
            front=match[0]
        else:
            fields=meta.get('frontmatter',{})
            if not fields:raise ImportFailure('New article needs reviewed frontmatter')
            front='---\n'+'\n'.join(k+': '+json.dumps(v,ensure_ascii=False) for k,v in fields.items())+'\n---\n'
        self.pending[output]=(front+'\n'+body.strip()+'\n').encode('utf-8')
        for rel in self.pending:
            if not (self.root/rel).resolve().is_relative_to(self.root):raise ImportFailure('Output escapes project')
        if write:
            # All resolution / privacy validation finishes before the first write.
            for rel,data in self.pending.items():
                dest=self.root/rel;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
        return {'mode':'write' if write else 'dry-run','selected':selected,'files':[str(p) for p in self.pending],'references':self.report}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--manifest',required=True);p.add_argument('--note',required=True)
    p.add_argument('--project',default=str(Path(__file__).resolve().parents[1]));p.add_argument('--write',action='store_true')
    args=p.parse_args()
    try:
        manifest=json.loads(Path(args.manifest).read_text(encoding='utf-8-sig'))
        print(json.dumps(Importer(manifest,args.project).run(args.note,args.write),indent=2,ensure_ascii=False))
    except (ImportFailure,OSError,KeyError) as e:
        print('IMPORT BLOCKED: '+str(e),file=sys.stderr);sys.exit(1)
if __name__=='__main__':main()

