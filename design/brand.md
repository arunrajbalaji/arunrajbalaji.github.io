The personal site of Raj Balaji-Wright, a computational scientist. The look is an engineering document: flat, ruled and precise, with one teal accent. Restraint carries the tone. Nothing shouts.

## Voice

- Write in the first person, in plain words. Technical terms belong inside work cards, not in the header or the Now section.
- Use sentence case. Monospace labels are capitalised by CSS, not typed in capitals.
- No exclamation marks, no emoji, and no availability or "hire me" language.
- At most one emphasised sentence per section. Set it as `callout`, not in bold.

## Colour

- The page sits on `ground`. Cards sit on `panel`. Figure areas, the mesh strip and proof cells sit on `inset`.
- Text is `ink` for headings and paragraphs, `ink-body` inside cards, `ink-soft` for the lede and figure labels, and `ink-muted` for monospace labels and metadata.
- `accent` is a petrol teal and the only brand colour. Use it for the accent bar, the monogram, the mesh interface line, the callout marker, and one highlighted series per figure. Use it once per region of the page. The resume uses the same light value.
- Link text is `link`, which is `accent`, changing to `link-hover` on hover. Do not set any other text in `accent`: headings, paragraphs and labels stay in the ink colours.
- Text on an `accent` fill is `on-accent`. Do not place link text on `accent-tint`.
- `accent` is dark enough to carry meaning in both themes, so a highlighted series needs no second cue. It has a different value in each theme; always use the token, never a fixed hex.

## Type

- Two families carry the page. `sans` (Barlow) is for everything read as prose. `mono` (IBM Plex Mono) is for labels, navigation, metadata and the monogram.
- `serif` (Source Serif 4, italic) appears only inside figures, as `figure-label`. Never use it for headings or body text.
- The headline is `display` at regular weight, never semibold or bold. Size it with `display-size` and cap its width at `measure-display`.
- Section paragraphs are `body-lg` within `measure`. Card paragraphs are `card-body`.
- `label`, `meta` and `figure-title` are uppercase. `nav` is lowercase. Apply both with `text-transform`.
- Self-host all three families as WOFF2 files. Load no font or script from a third party.

## Layout

- Content sits in a column of `container` width with `gutter` side padding.
- Each section starts `section-gap` below the last. A text section puts its `label` in a `rail` to the left of the body, `space-40` apart. On a narrow screen the label stacks above the body.
- Work cards leave the rail and span the full column: three across on desktop, one per row on a phone, never narrower than `card-min`.
- Every link and control is at least `tap` tall.
- `gutter`, `section-gap`, `hero-top`, `hero-bottom`, `display-size`, `lede-size`, `callout-size` and `nav-gap` are `clamp()` values. Use them as written.

## Lines, corners and depth

- Rules give the page its structure. Use `border-strong` in `rule-strong` under the header and above the proof row, and `border-hairline` in `rule-strong` on the edges of the mesh strip. Use `border-hairline` in `rule` around cards, cells and figures. Use `rule-soft` inside a card.
- Never draw a rule in `ink`. `rule-strong` equals `ink` on light and is deliberately softer on dark.
- Corners are square: `radius-none` everywhere.
- No shadows, no gradients and no motion. The one exception is the `grid` line pattern behind figures.
- Keyboard focus is a solid outline of `border-strong` width in `focus`, offset by the same width.

## Figures

- A figure drawn for the site, such as a schematic, sits on `inset` with `grid` lines at a `space-16` pitch and takes its colours from the tokens.
- A real published figure is an image made for white paper. Place it on `plate` in both themes, with no grid behind it. Do not invert or recolour it.
- Draw axes and primary data in `ink`. Draw earlier or secondary series in `mesh` and `rule`. Draw the one highlighted series in `accent`.
- Set axis labels and legends in `figure-label`. Set box titles in schematics in `figure-title`.
- Give every figure alt text. On case-study pages, give it a caption too.
- Cite a paper exactly: journal, volume, article number and year, linked to its DOI.

## The mark

- The monogram is the letters "rbw" in `monogram` type and `on-accent`, on an `accent` square of `mark` size. It sits to the left of the name in the header.
- There is no logo file. Export the monogram as SVG and PNG icons when the site is built.

## Dark theme

- The site follows the visitor's system setting through `prefers-color-scheme`. There is no theme toggle and no stored preference.
- Only colour tokens change between themes. Layout, type and spacing stay the same.
- The `dark` values were reviewed on the desktop homepage. The heavy rules were softened to `rule-strong` after that review.
- `accent` is brighter on dark. Keep to the same few uses; do not add more because it reads well.
