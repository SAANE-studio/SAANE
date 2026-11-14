import tempfile,unittest
from pathlib import Path
from import_obsidian import Importer,ImportFailure

class ImportTests(unittest.TestCase):
 def setUp(self):
  self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
  self.root=Path(self.temp.name);self.vault=self.root/'vault';self.vault.mkdir()
  self.project=self.root/'site';self.project.mkdir()
  self.m={'vault':str(self.vault),'notes':{},'assets':[]}
 def note(self,name,text,url=True):
  p=self.vault/name;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(text)
  self.m['notes'][name]={'output':'content/research/'+Path(name).stem+'.md','slug':Path(name).stem.lower(),'frontmatter':{'title':Path(name).stem}}
  if url:self.m['notes'][name]['url']='/research/'+Path(name).stem+'/'
 def run_note(self,name='a.md'):
  obj=Importer(self.m,self.project);result=obj.run(name);return obj,result
 def test_comments_and_code(self):
  self.note('a.md','visible %%SECRET%% ==mark==\n\n~~~text\n[[literal]]\n~~~')
  obj,_=self.run_note();body=obj.pending[Path('content/research/a.md')].decode()
  self.assertNotIn('SECRET',body);self.assertIn('research-mark',body);self.assertIn('[[literal]]',body)
 def test_unapproved_embed_has_no_writes(self):
  self.note('a.md','![[private]]')
  (self.vault/'private.md').write_text('secret')
  with self.assertRaisesRegex(ImportFailure,'not publication-approved'):self.run_note()
  self.assertEqual(list(self.project.iterdir()),[])
 def test_cycles(self):
  self.note('a.md','![[b]]');self.note('b.md','![[a]]')
  with self.assertRaisesRegex(ImportFailure,'cycle'):self.run_note()
 def test_ambiguous(self):
  self.note('a.md','![[b]]');self.note('one/b.md','one');self.note('two/b.md','two')
  with self.assertRaisesRegex(ImportFailure,'Ambiguous'):self.run_note()
 def test_heading_and_block_embeds(self):
  self.note('a.md','![[b#Section]]\n\n![[b#^sample]]')
  self.note('b.md','## Section\nKeep\n## Other\nDrop\n\nBlock text ^sample',False)
  obj,_=self.run_note();body=obj.pending[Path('content/research/a.md')].decode()
  self.assertIn('Keep',body);self.assertNotIn('Drop',body);self.assertIn('Block text',body)
 def test_missing_heading(self):
  self.note('a.md','![[b#Absent]]');self.note('b.md','## Present')
  with self.assertRaisesRegex(ImportFailure,'heading'):self.run_note()
 def test_missing_comment_end(self):
  self.note('a.md','%%secret')
  with self.assertRaisesRegex(ImportFailure,'Unclosed'):self.run_note()
 def test_output_traversal(self):
  self.note('a.md','text');self.m['notes']['a.md']['output']='../escape.md'
  with self.assertRaisesRegex(ImportFailure,'Output'):self.run_note()
 def test_unpublished_link(self):
  self.note('a.md','[[b]]');self.note('b.md','text')
  with self.assertRaisesRegex(ImportFailure,'not been imported'):self.run_note()
 def test_callout_and_math_preserved(self):
  text='> [!note]- Title\n> Body $x+y$\n>\n> > [!tip] Nested'
  self.note('a.md',text);obj,_=self.run_note()
  self.assertIn(text,obj.pending[Path('content/research/a.md')].decode())

 def test_standalone_block(self):
  self.note('a.md','![[b#^list]]')
  self.note('b.md','- One\n- Two\n\n^list',False)
  obj,_=self.run_note();body=obj.pending[Path('content/research/a.md')].decode()
  self.assertIn('- One',body);self.assertIn('research-anchor',body)
 def test_asset_allowlist_and_bytes(self):
  self.note('a.md','![[image.png|360]]')
  (self.vault/'image.png').write_bytes(b'fixture-image')
  self.m['assets']=['image.png']
  obj,_=self.run_note()
  self.assertIn(b'fixture-image',obj.pending.values())
  self.assertIn('size="small"',obj.pending[Path('content/research/a.md')].decode())
 def test_unsupported_data_uri(self):
  self.note('a.md','![x](data:image/png;base64,YQ==)')
  with self.assertRaises(ImportFailure):self.run_note()

 def test_code_inside_note_embed_is_not_reconverted(self):
  self.note('a.md','![[folder/b]]')
  self.note('folder/b.md','~~~text\n==literal==\n![[not-an-embed]]\n~~~',False)
  obj,_=self.run_note();body=obj.pending[Path('content/research/a.md')].decode()
  self.assertIn('==literal==',body);self.assertIn('![[not-an-embed]]',body)
 def test_heading_in_code_is_not_selected(self):
  self.note('a.md','![[b#Real]]')
  self.note('b.md','~~~md\n## Real\nFake\n~~~\n\n## Real\nActual\n',False)
  obj,_=self.run_note();body=obj.pending[Path('content/research/a.md')].decode()
  self.assertIn('Actual',body);self.assertNotIn('Fake',body)

 def test_html_report_embed(self):
  self.note('a.md','![[report.htm]]')
  (self.vault/'report.htm').write_text('<html><head></head><body>Report</body></html>')
  self.m['assets']=['report.htm']
  obj,_=self.run_note()
  self.assertIn('type="html"',obj.pending[Path('content/research/a.md')].decode())
  output=next(data for name,data in obj.pending.items() if name.suffix=='.htm').decode()
  self.assertIn('sandbox allow-scripts',output)
 def test_html_dependency_requires_approval(self):
  self.note('a.md','![[report.htm]]')
  (self.vault/'report.htm').write_text('<head><script src="private.js"></script></head>')
  self.m['assets']=['report.htm']
  with self.assertRaisesRegex(ImportFailure,'not approved'):self.run_note()
 def test_html_approved_dependency_is_inlined(self):
  self.note('a.md','![[report.htm]]')
  library=self.vault/'library.js';library.write_text('var fixture = 1;')
  (self.vault/'report.htm').write_text('<head><script src="'+library.as_posix()+'"></script></head>')
  self.m['assets']=['report.htm'];self.m['html_resource_files']=[str(library)]
  obj,_=self.run_note()
  output=next(data for name,data in obj.pending.items() if name.suffix=='.htm').decode()
  self.assertIn('var fixture = 1;',output);self.assertNotIn(library.as_posix(),output)
if __name__=='__main__':unittest.main()



