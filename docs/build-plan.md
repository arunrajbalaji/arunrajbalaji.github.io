# Build plan

Work through the phases in order. Stop at the end of each phase so Raj can review on `https://arunrajbalaji.github.io/` before the next one starts.

## Phase 1: Foundations

1. Generate `assets/css/site.css` from `design/tokens.json`: custom properties for light and dark, a reset, base typography, and the layout primitives in `design/brand.md` (container, gutter, rail, section gap).
2. Self-host Barlow (400, 500, 600), IBM Plex Mono (400, 500) and Source Serif 4 italic (400) as WOFF2, subset to Latin, with `font-display: swap`.
3. Build the shared header and footer from `design/components/SiteHeader` and `FooterLinks`, and write `scripts/check-chrome.py`.
4. Export the "rbw" monogram as SVG and PNG favicons and an Apple touch icon.
5. Write a minimal `404.html` in the site style.

Review: header, footer and type in both themes, at desktop and phone widths.

## Phase 2: Homepage

Build `/` from `content/home.md` using the Hero, MeshStrip, Section, WorkCard, Callout, ProofRow and FooterLinks components. Draw the card-one schematic as inline SVG; it must stay generic (a physics model and a machine-learning model coupled in one simulation), with nothing specific to any company. Cards two and three use simplified plots redrawn in the site style, as in `design/components/WorkCard/preview.html`.

Review: the whole page in both themes at 1440, 1024, 768, 390 and 320 px.

## Phase 3: Work and case studies

1. Build `/work/` from `content/work.md`. Card two needs a new generic schematic of a simulation running beside a live experiment.
2. Port the four case studies from the live site into `/work/<slug>/`, adding the titles and leads from `content/case-studies.md` and applying its edits. Set equations with KaTeX. Recover the figures at the best resolution available and pre-size them.

Review: each case study against its live original, checking that no section, equation or figure was lost.

## Phase 4: Remaining pages

1. `/about/` from `content/about.md`, with the headshot (Raj supplies the file).
2. `/publications/`: port from the live site. Drop the "2024" stamps on papers in preparation. Each entry has one DOI or PDF link. State the earlier author name (Arunraj Balaji) once.
3. `/teaching/`: port from the live site, adding the three students Raj mentored (ask him for the details).
4. `/cv/`: one current resume and CV at file names that never change, plus the two legacy `/wp-content/uploads/...` paths listed in `CLAUDE.md`.
5. The seven redirect stubs listed in `CLAUDE.md`.

Review: every page, then a read-through by one non-technical reader.

## Phase 5: Cutover (with Raj)

1. Test every old URL against the stubs, including both PDF paths.
2. Verify the domain in Raj's GitHub account settings, then add it under the repository's Pages settings. This writes a `CNAME` file.
3. At the registrar (Squarespace Domains), point DNS at GitHub. Leave the MX and TXT records for email forwarding untouched.
   - A records for `@`: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
   - AAAA records for `@` (optional): 2606:50c0:8000::153 through 2606:50c0:8003::153
   - CNAME `www` → `arunrajbalaji.github.io`
4. Once DNS and the certificate are live (up to 24 hours each), turn on Enforce HTTPS.
5. Check the site on the domain, then cancel or downgrade the WordPress.com plan. Keep the domain registration.

## Later

- Numbers for the CO2 and multi-layer leads, once those papers are published.
- Vector originals of the paper figures, swapped in when found.
- The `/writing/` section.
