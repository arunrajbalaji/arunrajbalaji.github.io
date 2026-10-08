# rajbalajiwright.com

The personal site of Raj Balaji-Wright, a computational scientist. This repository is the site: GitHub Pages serves the committed files as they are, from `main`, at the repository root. It replaces a WordPress.com site at the same domain.

Read `docs/build-plan.md` for what to build and in what order. Read `design/brand.md` and `design/tokens.json` before writing any CSS or markup.

## Sources of truth

- `content/*.md` holds the final copy for every new or rewritten page. Use it word for word. Do not rewrite, extend, or "improve" copy. If something reads wrong, flag it to Raj instead.
- `design/tokens.json` holds every colour, size, space and font value. `design/brand.md` holds the rules for using them. `design/components/*/preview.html` shows each component as working HTML and CSS, and `README.md` beside it gives its rules. Port these components; do not invent new ones without asking.
- Publications, Teaching and CV pages have no new copy. Port them from the current site, applying the voice and design rules.
- Once a page is built, the HTML is the source of truth for that page's copy. Edit it there, not in `content/`.

## Hard rules

- **No build step.** Hand-written HTML and CSS, committed as served. No framework, no bundler, no static-site generator, no npm dependency at runtime. Small helper scripts you run by hand (a header/footer check, image resizing) are fine.
- **No third-party requests.** No CDNs, no Google Fonts, no analytics, no embeds. Fonts are self-hosted WOFF2 files. KaTeX is copied into the repository and loaded only on pages with equations.
- **The repository is public, and its history is permanent.** Never commit drafts, notes, or anything about Raj's employer beyond the exact text in `content/`. This applies to commit messages too.
- **Employer content stays as written.** The Ark Biotech text in `content/` has been reviewed for what can be said publicly. Do not add detail, names of tools, methods, products, customers or results about Ark work, in copy, alt text, comments or commit messages.
- **Raj reviews everything before it goes live.** Nothing moves to the custom domain without his sign-off.
- **No job-seeking language.** No availability lines and no "hire me" calls to action. Contact is an email address.

## Structure

- One folder per page, each holding `index.html`, so URLs end in a slash: `/work/`, `/about/`.
- Pages: `/`, `/work/`, `/work/capacitive-deionization/`, `/work/electrodialysis/`, `/work/co2-electro-reduction/`, `/work/multi-layered-cell-simulation/`, `/publications/`, `/teaching/`, `/about/`, `/cv/`. A `/writing/` section is planned later; build nothing for it unless asked.
- `.nojekyll` at the root keeps GitHub Pages from running Jekyll.
- One stylesheet, `assets/css/site.css`, built on CSS custom properties generated from `design/tokens.json`. Light values in `:root`, dark values under `@media (prefers-color-scheme: dark)`. No theme toggle.
- Fonts in `assets/fonts/`, images in `assets/img/`, KaTeX in `assets/katex/`.
- All internal links are root-relative (`/work/`), so they work the same on `arunrajbalaji.github.io` and on the custom domain.

## Shared header and footer

The header (monogram, name, nav: Work, Publications, Teaching, About, CV) and the footer links are duplicated in every page file so the nav works without JavaScript. `aria-current="page"` marks the current section. A script (`scripts/check-chrome.py`) verifies that every page's header and footer match the canonical copy apart from `aria-current`. Run it before every commit that touches a page.

## Old addresses

GitHub Pages has no server-side redirects. Each old WordPress address gets a stub `index.html` with an instant meta refresh and a canonical link to its new address:

| Old | New |
| --- | --- |
| `/research/` | `/work/` |
| `/research/<slug>/` (four case studies) | `/work/<slug>/` |
| Biography page | `/about/` |
| Download links page | `/cv/` |

Confirm the exact old paths for the Biography and Download links pages from the live site before writing those two stubs.

The two PDFs linked from the old site must keep resolving. Recreate these paths and serve the current documents from them:

- `/wp-content/uploads/2024/11/balajiwright_cv-3.pdf` → the current CV
- `/wp-content/uploads/2025/02/balajiwright_resume.pdf` → the current resume

## Images

- Pre-size every raster image to two widths and serve with `srcset` and `sizes`. Never commit a multi-megapixel original to a page.
- Every image has alt text. Figures on case-study pages also have a one-line caption.
- Published paper figures sit on the `plate` token in both themes. Never invert or recolour them.
- Schematics drawn for the site are inline SVG using the tokens (see `design/brand.md`, Figures).

## Quality bar

- Valid, semantic HTML: one `h1` per page, landmarks, a skip link.
- Every page has a unique `<title>` and meta description (given in `content/` for new pages), plus Open Graph tags.
- Works at 320 px wide with no horizontal scroll. Tap targets at least the `tap` token.
- Text contrast meets WCAG AA in both themes.
- Preview locally with `python3 -m http.server` from the repository root.

## Contacts and links

- Email: contact@rajbalajiwright.com
- GitHub: https://github.com/arunrajbalaji
- LinkedIn, Google Scholar and ORCID URLs: ask Raj, or take them from the current site.
