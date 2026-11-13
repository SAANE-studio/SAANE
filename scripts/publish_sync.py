"""Discover publish:true Research notes; never modify the Obsidian vault."""
import hashlib, json, os, re, shutil
from datetime import date
from pathlib import Path
import yaml
from import_obsidian import Importer

ROOT=Path(__file__).resolve().parents[1]
MANIFEST=ROOT/'scripts/obsidian-publication.json'
FM=re.compile(r'\A\s*---\r?\n(.*?)\r?\n---(?:\r?\n|$)',re.S)

def metadata(text):
    match=FM.match(text)
    if not match:return {},text
    value=yaml.safe_load(match[1]) or {}
    if not isinstance(value,dict):raise ValueError('Metadata must be a YAML mapping')
    return value,text[match.end():]

def files(vault):
    for directory, folders, names in os.walk(vault):
        folders[:]=[n for n in folders if not n.startswith('.')]
        for name in sorted(names):
            path=Path(directory)/name
            if not path.resolve().is_relative_to(vault.resolve()):continue
            yield path

def fingerprint(manifest_path=MANIFEST):
    raw=Path(manifest_path).read_bytes(); config=json.loads(raw.decode('utf-8-sig'))
    vault=Path(config['vault']); digest=hashlib.sha256(raw)
    if not vault.is_dir():raise ValueError('Vault unavailable: '+str(vault))
    for path in sorted(files(vault)):
        stat=path.stat()
        digest.update(str(path.relative_to(vault)).encode())
        digest.update(str((stat.st_mtime_ns,stat.st_size)).encode())
    return digest.hexdigest()

def first_image(body):
    # Read the converted article in display order, ignoring code examples.
    body = re.sub(r'(?ms)^\s*(`{3,}|~{3,})[^\n]*\n.*?^\s*\1\s*$', '', body)
    pattern = r'\{\{<\s*research-image\s+[^>]*?src="([^"]+)"|!\[[^\]]*\]\(([^\s)]+)\)'
    match = re.search(pattern, body)
    return (match.group(1) or match.group(2)) if match else 'saane-logo.svg'

def sync(root=ROOT, manifest_path=MANIFEST):
    root=Path(root); before=fingerprint(manifest_path)
    config=json.loads(Path(manifest_path).read_text(encoding='utf-8-sig'))
    vault=Path(config['vault']); state_path=root/'.saane-preview/managed.json'
    previous=json.loads(state_path.read_text()) if state_path.exists() else {}
    discovered={}; assets=[]; slugs={}
    for path in files(vault):
        key=path.relative_to(vault).as_posix()
        if path.suffix.lower()!='.md':
            assets.append(key); continue
        text=path.read_text(encoding='utf-8-sig')
        try: meta,body=metadata(text)
        except yaml.YAMLError as error:
            if re.search(r'(?m)^publish:\s*true\s*$',text):raise ValueError(key+': invalid YAML: '+str(error))
            continue
        if meta.get('publish') is not True or meta.get('website_section')!='research':continue
        slug=meta.get('slug','')
        if not isinstance(slug,str) or not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',slug):raise ValueError(key+': valid slug required')
        if not meta.get('title') or not meta.get('category'):raise ValueError(key+': title/category required')
        if slug in slugs:raise ValueError('Duplicate slug: '+slug)
        slugs[slug]=key
        output='content/research/'+slug+'.md'
        approved=config.get('notes',{}).get(key,{}).get('output')
        if (root/output).exists() and previous.get(key)!=output and approved!=output:
            raise ValueError('Refusing to overwrite an unmanaged article: '+output)
        if key in previous and previous[key]!=output:raise ValueError('Slug changed; migrate existing article explicitly: '+key)
        front={k:meta[k] for k in ('title','category','summary','date','article_type','cover','description','tags') if k in meta}
        front.update(slug=slug,article_type=meta.get('article_type','Research'))
        front.setdefault('date',date.today().isoformat())
        discovered[key]={'output':output,'slug':slug,'url':'/research/'+slug+'/','frontmatter':front}
    # Preserve the originally authorized Natural Ventilation workflow until it gets Properties.
    for key,info in config.get('notes',{}).items():
        path=vault/key
        if key not in discovered and path.is_file():
            meta,_=metadata(path.read_text(encoding='utf-8-sig'))
            if 'publish' not in meta and key not in previous:discovered[key]=info
    manifest={'vault':str(vault),'notes':discovered,'assets':assets}
    pending={}; managed={}
    for key,info in discovered.items():
        importer=Importer(manifest,root); importer.run(key,False)
        output=Path(info['output']); generated=importer.pending[output].decode()
        old,body=metadata(generated)
        new=info.get('frontmatter',old).copy()
        if 'date' not in metadata((vault/key).read_text(encoding='utf-8-sig'))[0]:new['date']=old.get('date',new['date'])
        source_meta,_=metadata((vault/key).read_text(encoding='utf-8-sig'))
        if not source_meta.get('cover'):
            new['cover']=first_image(body)
        elif new['cover'] and not (root/'static'/str(new['cover']).lstrip('/')).is_file():
            resolved=importer.resolve(str(new['cover']),key)
            new['cover']=importer.asset(resolved,info['slug'])
        importer.pending[output]=('---\n'+yaml.safe_dump(new,allow_unicode=True,sort_keys=False)+'---\n\n'+body.lstrip()).encode()
        if info.get('frontmatter'):managed[key]=info['output']
        pending.update(importer.pending)
    # Withdraw only auto-managed pages when publish is removed/false; keep files as drafts.
    for key,output in previous.items():
        if key not in discovered and (root/output).is_file():
            front,body=metadata((root/output).read_text(encoding='utf-8'))
            front['draft']=True
            pending[Path(output)]=('---\n'+yaml.safe_dump(front,allow_unicode=True,sort_keys=False)+'---\n'+body).encode()
            managed[key]=output
    if before!=fingerprint(manifest_path):raise ValueError('Vault changed during import; retrying after save settles')
    count=0
    for rel,data in pending.items():
        target=root/rel
        if target.exists() and target.read_bytes()==data:continue
        if target.exists() and rel.as_posix().startswith('content/'):
            backup=root/'.saane-preview/backups'/rel
            if not backup.exists():backup.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(target,backup)
        target.parent.mkdir(parents=True,exist_ok=True)
        temporary=target.with_name(target.name+'.saane-tmp'); temporary.write_bytes(data);os.replace(temporary,target);count+=1
    state_path.parent.mkdir(parents=True,exist_ok=True)
    state_path.write_text(json.dumps(managed,indent=2))
    return count
