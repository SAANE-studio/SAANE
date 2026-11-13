# SAANE Research authoring

The single article layout uses static/research/research.css and the sr-* namespace. It does not attach legacy research-study / research-detail / article-body classes, so obsolete selectors in styles.css cannot compete with the new system. Shared CSS, Home/Profile/Portfolio/Research archive, and global navigation remain unchanged.

## Local style guide
Run: hugo server --buildDrafts --bind 127.0.0.1 --port 1314
Open /_local/research-style-guide/. It is a draft with build.list: never, noindex and sitemap disabled; a normal hugo build omits it. Never use --buildDrafts for publication.
The guide includes synthetic media fixtures and labels them as such.

## Markdown
Use front matter title for H1; body normally starts with ##. H1–H6 retain their source levels. Standard emphasis, lists, nested lists, task lists (read-only checkboxes), blockquotes, tables and footnotes work. Align numbers with | --: |. Wide tables and code blocks scroll in their own keyboard-focusable regions.
Use $...$ or \( ... \) for inline mathematics, $$...$$ or \[ ... \] for blocks. Escape literal dollar signs with \$; mathematics uses Hugo's KaTeX renderer and locally bundled CSS/fonts.
Use a mermaid code fence for diagrams. Mermaid is local, strict-security mode, neutral theme; a source disclosure remains available. Scripts and unsafe HTML in diagrams are not supported.

## Callouts (native Research render hook)
> [!note]- Optional **title**
> Markdown body.
>
> > [!tip]+ Nested title
> > Body.

+ starts open; - starts closed; no sign is non-foldable. Native details/summary supports keyboard and screen readers. Types: note/info/tip/warning/method/finding/limitation/summary/statement/lead. Other types use a neutral treatment and their original label. Markdown is rendered in titles and bodies.

## Custom shortcodes
Use {{< ... >}} for custom shortcodes. Text wrappers render their inner Markdown; gallery and steps containers compose child shortcodes.

{{< research-image src="/images/example.png" alt="Description" size="wide" caption="Visible caption" number="1" source="Source label" source_url="https://example.com/" >}}

Sizes: small 360, medium 560, large 720, wide 1040 px maximum. Legacy full maps to wide. Image links open the original, uncropped file. The alt is never copied into the caption.

{{< research-gallery title="Two diagrams" >}}
{{< research-image src="/images/a.png" alt="First diagram" caption="A." >}}
{{< research-image src="/images/b.png" alt="Second diagram" caption="B." >}}
{{< /research-gallery >}}

{{< research-comparison title="ON / OFF" on_src="/images/on.png" on_alt="ON chart" on_caption="Ventilation ON" off_src="/images/off.png" off_alt="OFF chart" off_caption="Ventilation OFF" >}}

{{< research-media type="video" src="/media/example.mp4" title="Video" caption="Context" captions="/media/example.vtt" lang="en" >}}
{{< research-media type="audio" src="/media/example.mp3" title="Recording" caption="Context / transcript link" >}}
{{< research-media type="pdf" src="/media/example.pdf" title="Document" caption="Context" >}}
{{< research-media type="youtube" id="VIDEO_ID" title="Accessible title" >}}
{{< research-media type="embed" src="https://approved-provider.example/embed" title="Accessible title" >}}

Local media uses native controls, no autoplay, and a permanent fallback link. Supply captions/transcripts for meaningful audio/video. Generic iframes require HTTPS and use a sandbox. External providers may refuse framing, require network access, or set cookies; local fallback links remain visible. PDF inline viewing depends on browser support.

{{< research-lead >}}Lead paragraph.{{< /research-lead >}}
{{< research-statement >}}Light type with **strong contrast**.{{< /research-statement >}}
{{< research-small >}}Supporting text.{{< /research-small >}}
{{< research-mark >}}Highlight.{{< /research-mark >}}

{{< research-steps >}}
{{< research-step >}}**Prepare.** Detail.{{< /research-step >}}
{{< research-step >}}**Evaluate.** Detail.{{< /research-step >}}
{{< research-step >}}**Review.** Detail.{{< /research-step >}}
{{< /research-steps >}}

Method steps are optional, not a replacement for numbered lists.

## Targeted Obsidian import
No existing permanent importer was present. scripts/import_obsidian.py uses only Python's standard library. scripts/obsidian-publication.json explicitly approves only Natural Ventilation and its four PNG attachments. Existing article files were not reimported during the style change.

Dry run:
python scripts/import_obsidian.py --manifest scripts/obsidian-publication.json --note "BIM 6D/5_Natural Ventilation.md"

Write only after reviewing the manifest:
python scripts/import_obsidian.py --manifest scripts/obsidian-publication.json --note "BIM 6D/5_Natural Ventilation.md" --write

Each allowed note needs output (inside content/), slug, and optionally a canonical url. New outputs require a reviewed frontmatter object. Existing YAML front matter is preserved. An approved embedded note can omit url, but cannot then be a link target. A different linked note must already have an imported output, avoiding invented public destinations. Approve every referenced asset with an exact vault-relative path. Basename collisions fail; resolve them using explicit paths. Asset files get stable content-hash names. Only referenced assets are copied. Originals are never modified; no automatic asset deletion occurs.

Supports:
- ==highlight== outside code; native callouts including nested/foldable forms.
- [[note|alias]], [[note#Heading]], [[note#^block-id]] and approved attachment links.
- ![[image|360]], local video/audio/PDF; approved note/heading/block embeds.
- URL-encoded SVG data URIs; standard local Markdown images.
- Math and Mermaid are preserved for Hugo render hooks.
- Private %% comments are stripped before publication, including comments inside code examples.
- Missing/ambiguous references, unclosed comments, unsafe paths and cyclic note embeds abort before writing.

Boundaries: no Dataview, Canvas, arbitrary plugins, Excalidraw source rendering, queries, or base64 data URIs. Note embeds preserve source heading levels, so authors must review hierarchy. Explicit anchors are namespaced in note embeds. Embedded notes should not contain custom scripts/HTML; Hugo unsafe HTML remains disabled. The converter is for trusted, explicitly selected author content, not untrusted third-party documents. Do not insert private vault syntax directly into Hugo: run the importer first.

## Optional Obsidian snippet
extras/obsidian/saane-research.css is supplied only as a file. Manually copy it to your vault's .obsidian/snippets and enable it if desired. Add cssclasses: [saane-research] to selected notes. Font availability in Obsidian is independent; install Jost/Poppins there if needed. This project never activates the snippet or edits the vault.

## Validation
python -m unittest discover -s scripts -p "test_import_obsidian.py"
hugo
hugo --buildDrafts --destination public-preview
Check Natural Ventilation, Clash Detection and the local guide at desktop/mobile widths. Font assets are local (Poppins 300/500/600/700, Jost normal+italic 400/600). The existing global navigation markup, links and desktop appearance remain shared. Within Research only, mobile navigation follows the article in normal flow to avoid covering text.

Reference APIs: https://gohugo.io/render-hooks/blockquotes/ , https://gohugo.io/render-hooks/passthrough/ , https://gohugo.io/render-hooks/tables/
