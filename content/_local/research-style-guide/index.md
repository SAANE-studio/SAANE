---
title: "SAANE Research Style System"
date: 2026-11-12
type: research
category: "Local design reference"
article_type: "Style guide · local only"
summary: "An editorial system for long-form research: geometric type, measured contrast, and room to read."
draft: true
local_styleguide: true
url: /_local/research-style-guide/
build:
  list: never
sitemap:
  disable: true
---

> [!note] Local preview only
> This draft is excluded from ordinary builds and the Research listing. Examples are illustrative design fixtures, not research findings. Run Hugo with **--buildDrafts** to view it.

## Typography and hierarchy

The page title above is the single primary H1. Body copy uses Jost 400 at 18px on desktop and 17px on mobile, with a 1.75 line height. Headings use Poppins. The text measure is 720px, while wide media can reach 1040px when the viewport permits.

### H3 · A clear reading sequence

#### H4 · Supporting detail

##### H5 · Small section label

###### H6 · Fine-grained structure

Regular text, **bold 600**, *true italic*, ***bold italic***, ~~thin strikethrough~~, {{< research-mark >}}neutral highlight{{< /research-mark >}}, [an underlined link to Natural Ventilation](/research/natural-ventilation/), and inline code: `airflow_rate`.

{{< research-small >}}Small text is 14px. Use it for supporting notes, not primary arguments.{{< /research-small >}}

> [!lead]
> A lead introduces the argument with a larger, relaxed paragraph. It remains part of the reading flow.

> [!statement]
> Let the evidence breathe. **Make the important distinction clear.**

---

## Lists and method steps

- Ordinary bullet list.
- A second item with a nested list:
  - One supporting detail.
  - Another detail.

1. First ordinary numbered item.
2. Second item.
   1. A nested numbered item.
3. Third item.

- [x] Image references resolved.
- [ ] Review assumptions before publication.

The custom steps component is opt-in. Ordinary lists remain ordinary lists.

{{< research-steps >}}
{{< research-step >}}
**Prepare.** Define the scope and approved inputs.
{{< /research-step >}}
{{< research-step >}}
**Evaluate.** Record the method and compare results.
{{< /research-step >}}
{{< research-step >}}
**Review.** Document uncertainty and limitations.
{{< /research-step >}}
{{< /research-steps >}}

> A blockquote uses a thin left rule, a 24px indent, and 21px text on desktop.

## Callouts

> [!note] Note with a title
> Markdown **emphasis**, lists, and [links](/research/) remain available.

> [!info]
> Context that supports the main argument.

> [!tip] Authoring tip
> Prefer a short label and a specific explanation.

> [!warning] Warning: review the inputs
> The label explicitly identifies the warning; the thicker rule does not rely on color.

> [!method] Evaluation procedure
> 1. Define the input.
> 2. Record the output.

> [!finding] Illustrative finding
> A larger text treatment distinguishes a finding from supporting detail.

> [!limitation]
> These fixtures demonstrate presentation, not the validity of a simulation.

> [!summary] Summary
> A quiet neutral field groups the key points.

> [!custom] Unknown type fallback
> Unrecognized types retain their label and use the neutral callout treatment.

> [!note]- Foldable note
> This starts collapsed. Focus the summary and press **Enter** or **Space**.
>
> > [!tip]+ Nested foldable tip
> > This nested callout starts open.
> >
> > - Nested Markdown is preserved.
> > - Each disclosure is independently operable.

> [!method]+ Expanded method
> This starts open, and can be collapsed without a mouse.

## Images and captions

Small ≤360px; medium ≤560px; large ≤720px; wide ≤1040px. Every image keeps its intrinsic aspect ratio. Click an image to inspect its original resolution. Alt text describes the image; a caption provides visible context.

{{< research-image src="/images/research/natural-ventilation/air-movement.png" alt="Blue arrows entering and leaving a room through opposite openings" size="small" number="1" caption="Small image, uncropped." source="Natural Ventilation article" source_url="/research/natural-ventilation/" >}}

{{< research-image src="/images/research/natural-ventilation/heat-transfer.svg" alt="25 degree air enters a room and 30 degree air leaves" size="medium" caption="Medium SVG, preserved as a vector." >}}

{{< research-image src="/images/research/natural-ventilation/heat-balance.png" alt="Diagram of the room heat balance" size="large" caption="Large image at the text measure." >}}

{{< research-image src="/images/research/natural-ventilation/natural-ventilation-analysis.png" alt="Natural ventilation simulation comparison charts" size="wide" caption="Wide image. Original chart colors remain unchanged." >}}

### Gallery · custom shortcode

{{< research-gallery title="Two explanatory diagrams" >}}
{{< research-image src="/images/research/natural-ventilation/air-movement.png" alt="Air movement through a room" caption="Air movement." >}}
{{< research-image src="/images/research/natural-ventilation/heat-transfer.svg" alt="Cool and warm air exchange" caption="Heat transfer." >}}
{{< /research-gallery >}}

### ON / OFF · custom shortcode

The same source image is deliberately repeated below to demonstrate layout only; it is **not** a new ON/OFF result.

{{< research-comparison title="Illustrative comparison layout" on_src="/images/research/natural-ventilation/air-movement.png" on_alt="Repeated air movement fixture, ON panel" on_caption="Layout fixture — ON." off_src="/images/research/natural-ventilation/air-movement.png" off_alt="Repeated air movement fixture, OFF panel" off_caption="Layout fixture — OFF." >}}

## Media

Local video and audio have controls and never autoplay. The video fixture is a silent two-second neutral field. Its caption track identifies the fixture.

{{< research-media type="video" src="/research/examples/sample.mp4" title="Local video fixture" caption="Silent visual fixture; native aspect ratio." captions="/research/examples/sample.vtt" >}}

{{< research-media type="audio" src="/research/examples/sample.wav" title="Local audio fixture" caption="Two-second quiet test tone." >}}

{{< research-media type="pdf" src="/research/examples/sample.pdf" title="PDF fixture" caption="One-page authoring reference." >}}

### YouTube and generic embeds

The external example below uses YouTube's privacy-enhanced player. Network access and provider permissions are required; the open-video link remains available if embedding is blocked.

{{< research-media type="youtube" id="aqz-KE-bpKQ" title="External player example — Big Buck Bunny" caption="External illustrative video, Blender Foundation." >}}

A generic HTTPS embed uses the same responsive frame, an accessible title, and a fallback link. Providers may refuse embedding; never bypass that restriction.

{{< research-media type="embed" src="https://www.youtube-nocookie.com/embed/aqz-KE-bpKQ" title="Generic HTTPS embed fixture" caption="Same external video, generic embed component." >}}

## Tables, code, mathematics, and diagrams

| Scenario | Airflow (m³/s) | Hours | Comment |
|:--|--:|--:|:--|
| Example A | 0.25 | 120 | Illustrative value |
| Example B | 0.10 | 80 | Illustrative value |

Right-aligned columns use tabular numerals. The table region accepts keyboard focus and scrolls locally when necessary.

| Long input identifier | Design case | Measurement convention | Reference period | Analysis status |
|:--|:--|:--|:--|:--|
| example_identifier_with_a_long_name | Demonstration only | A deliberately wide table | Illustrative evaluation period | Pending review |

~~~python
def airflow(velocity, area):
    # Example code, not a simulation implementation.
    return velocity * area
~~~

Inline mathematics: $Q = v A$. Block mathematics:

$$
ACH = \frac{3600 Q}{V}
$$

~~~mermaid
flowchart LR
    A["Approved inputs"] --> B["Evaluate"]
    B --> C["Review limitations"]
~~~

A footnote keeps a supporting source close to the argument.[^source]

[^source]: Local illustrative source note, 14px, with a return link. [Research index](/research/).

## Obsidian import · tested fixtures

The following examples were generated by the allowlist importer from synthetic notes in docs/fixtures/obsidian. Private fixture comments were removed.

### Converted source examples

{{< research-mark >}}Neutral highlight from Obsidian{{< /research-mark >}} and [an approved heading link](/_local/approved-fixture/#example-heading).

#### Whole-note embed


### Approved excerpt {#embed-9413d636-approved-excerpt}

This is a **public fixture** for note transclusion.

#### Example heading {#embed-9413d636-example-heading}

{{< research-anchor "embed-9413d636-block-sample" >}}

A paragraph with a stable block identifier.


#### Heading embed


#### Example heading {#embed-7c5119aa-example-heading}

{{< research-anchor "embed-7c5119aa-block-sample" >}}

A paragraph with a stable block identifier.


#### Block embed


{{< research-anchor "embed-d304e9fe-block-sample" >}}

A paragraph with a stable block identifier.


> [!note]- Imported foldable callout
> Imported **Markdown**, with a nested callout.
>
> > [!tip] Nested import
> > Only approved content is included.

## Authoring syntax and boundaries

Markdown is the primary format. Heading levels come directly from Markdown; use front matter for the article's main H1. Do not add a second H1 in the body.

~~~markdown
## Section
### Subsection
**bold** *italic* ***bold italic*** ~~deleted~~
[link](/research/natural-ventilation/)
- [x] Completed item

> [!warning]- Optional title
> Foldable Markdown content.
>
> > [!tip] Nested title
> > Nested content.

$$
Q = v A
$$
~~~

Obsidian source syntax is converted by the explicit-allowlist importer:

~~~text
==highlight==
[[Approved note|label]]
[[Approved note#Heading]]
![[approved-image.png|360]]
![[approved-video.mp4]]
![[Approved note]]
![[Approved note#Heading]]
![[Approved note#^block-id]]
~~~

Private Obsidian comments are removed during import. Do not paste private material directly into Hugo content: the vault importer is the publication boundary.

Custom shortcodes are documented in **docs/research-authoring.md**. They provide lead/statement, optional numbered steps, image/gallery/comparison, media, highlighting, small text, and stable block anchors. Callouts, tables, footnotes, code, mathematics, and Mermaid use Markdown plus Research render hooks.

**Limits:** this is a targeted converter, not an Obsidian plugin runtime. Dataview, Canvas, Excalidraw source, arbitrary plugin syntax, block queries, base64 data URIs, and arbitrary HTML are not supported. Export approved visual assets first. Missing, ambiguous, unpublished link targets, and cyclic note embeds block the import before any file is written. Images and attachments must also be explicitly approved in the manifest.
