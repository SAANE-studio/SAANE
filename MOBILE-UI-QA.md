# SAANE mobile UI implementation and QA

Date: 13 November 2026
Repository: D:/SHANZ/SNN/MISC/Github/HUGO/saane-hugo

## Problems found
- Profile sections retained max-width:min(46vw,700px) on mobile.
- More-specific Experience and Competence selectors overrode the existing generic mobile grid.
- Education inherited narrow section widths and 10–13px text.
- Research used small category buttons and a thumbnail/text grid that squeezed text.
- Global floating navigation and desktop rails remained present on mobile.

## Implementation
All new CSS rules are inside max-width:760px, the existing primary breakpoint.
Existing styles.css, research/research.css, profile-layout.js, research-layout.js and portfolio-layout.js were not edited.

Experience: date above role/company; one full-width content column; readable descriptions and lists.
Education: full available width, natural wrapping, larger metadata/descriptions and consistent workshop spacing.
Competence: 28px number column, minmax(0,1fr) text column, thin separators.
Intro, portrait and Tools: responsive single-column layout and 22px page margins.
Navigation: shared SAANE header, existing homepage and destination URLs, native modal dialog, explicit Tab/Shift+Tab loop, Escape, focus restoration, close on navigation and scroll lock. Desktop rails and floating links are hidden only on mobile.
Research: dropdown generated from existing category data delegates to existing filter buttons; editorial stacked thumbnails/text; empty state preserved.
Articles: mobile back link, responsive headings/metadata, constrained images/media and scrollable code/table containers.

## Files changed
- layouts/index.html
- layouts/page/profile.html
- layouts/page/portfolio.html
- layouts/partials/head.html
- layouts/partials/mobile-nav.html (new)
- layouts/research/list.html
- layouts/research/single.html
- static/mobile.css (new)
- static/mobile.js (new)
- MOBILE-UI-QA.md (this report)

## Validation
- Hugo production build: PASS, hugo --renderToMemory --noBuildLock, 14 pages.
- Existing warning: missing HTML taxonomy template; also present in baseline build.
- JavaScript syntax: PASS, node --check static/mobile.js.
- Changed-template whitespace check: PASS.
- Repository-wide whitespace check reports pre-existing article-content whitespace; those files were not edited by this task.
- Browser checks: widths 320,360,375,390,430 across Home, Portfolio, Profile, Research and all five published research articles (45 combinations): no document horizontal overflow, mobile header displayed, floating navigation hidden.
- Profile measurements confirmed full-width Experience/Education and a 28px Competence number column.
- Menu opening, initial focus, Shift+Tab containment, Escape, focus restoration and scroll lock checked.
- AEC Software filtering returned one card; Design showed the empty state; All restored five cards.
- Experience and Education visually inspected; article images inspected.
- Mobile screenshot artifacts: C:/Users/user/AppData/Local/Temp/saane-mobile-qa/

## Desktop comparison
Native before/after viewport screenshots were identical for:
- Profile: 768px, 1024px, 1440px.
- Home, Portfolio, Research listing: 1440px.
Full-page Building Energy Modelling screenshots were identical at 768,1024,1280,1440px.

Initial automated captures included incomplete entrance animations (confirmed by computed opacity 0.489553). Repeated 1280px Profile captures also changed image dimensions. Therefore a pixel-identical 1280px Profile comparison is NOT conclusively verified. Other Home/Portfolio/listing widths were inspected but not established pixel-identical. No desktop CSS rules or existing desktop scripts were changed.

## Remaining verification
- Full desktop visual acceptance remains pending the inconclusive comparisons above.
- No physical iOS/Android device or Safari test.
- No dedicated interactive test of every code block, table, PDF or embedded-media type.
- No exhaustive desktop interaction test.
- No commit, push, deployment, content/taxonomy/URL changes or generated public/ edits.
- Existing and concurrently added content/image changes were preserved.