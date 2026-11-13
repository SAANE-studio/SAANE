# Research validation — 12 November 2026

- Hugo 0.169.0: standard build and draft preview build succeed. Existing missing taxonomy template warning remains.
- 15 importer unit tests pass: privacy comments, code protection, approved assets, missing/ambiguous references, unpublished links, heading/block embeds, standalone block IDs, cycles, path traversal and unsupported data URIs.
- Real Natural Ventilation import dry-run succeeds; no vault files or existing article content are rewritten.
- Baseline SHA-256 checks pass for Natural Ventilation, Clash Detection, shared styles.css, head.html and nav.html.
- Browser QA: Natural Ventilation, Clash Detection and guide at 1440px and 390px. Desktop/mobile heading and body sizes match the specification. Text measure reaches 720px. No page-level horizontal overflow.
- Native Enter/Space toggles outer and nested disclosures. Wide table keyboard scroll confirmed (scrollLeft 78px at 390px viewport).
- KaTeX (2 formulas) and local Mermaid render. Local audio/video reach readyState 4 with controls and without autoplay. PDF has inline viewer and direct fallback.
- 32 distinct local resources return HTTP 200; all local fragment links resolve. Original diagram colors are retained.
- Default build excludes local guide and fixture pages; guide is absent from Research archive, feed and sitemap. Research stylesheet is absent from Home, Profile, Portfolio and Research archive.
- External YouTube/generic embed playback is provider/network dependent; responsive frames, titles and permanent fallback links are present. Playback is not certified by this local test.
- Four referenced image attachments were not available in the chat; implementation follows the supplied written design specification.

Preview: http://127.0.0.1:1314/_local/research-style-guide/
No deployment performed.
