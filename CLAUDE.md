# YSL Travel & Tours website: notes for Claude

Client: YSL Travel & Tours Sdn Bhd (877803-T), Klang, Malaysia. Licence KPL 6107 (MOTAC).
Built and maintained by Twain Productions (Michelle Liu). The 2020 YSL brand identity is Twain's work: keep continuity with it.

## Layout

| Path | What | Deployed |
|---|---|---|
| `source/` | Static-site generator (Python, no dependencies) and all CSS/JS | no |
| `dist/` | Built main website, including all images in `dist/assets/` | not yet (prototype only) |
| `dist/zh/` | Simplified Chinese site, same pages and templates (shares `dist/assets/`) | with `dist/` |
| `feedback-site/` | Tour feedback form + link maker, live at feedback.ysltravel.com | Cloudflare Pages project `ysl-feedback`, output dir `feedback-site`, no build command |

Build: `cd source && python3 build.py` writes the HTML into `../dist` (images in `dist/assets` are hand-placed: never delete them).
`python3 standalone.py` rebuilds `../feedback-site` from the same form code (`feedback.py`).
Commit the built output with the source change: Cloudflare serves the committed files, it does not build.

## Source map

- `build.py`: page templates (`build_home`, `build_corporate`, `build_about`, `build_services`, `build_tours`, tour pages, journal, contact).
- `data.py`: tours, services, contact details, Golden Destinations itineraries. `articles.py`: journal articles.
- Golden Destinations dates: `GD_DATES` in `data.py` (GD tour code + ISO dates, from `https://www.gd.my/b2c2b/api/v1/series/<CODE>?business_type=b2c2b&type=series`, the JSON behind `gd.my/web/itinerary/<CODE>`). Card months (`departs`) and the tour-page date list are built from it, in both languages. GD photos: `dist/assets/gd-<tour>-card.jpg` (5:4) and `-hero.jpg`.
- GD tour SEO: each GD tour has `seo` (the page `<title>`, keyword first: "Korea Tour Package from Malaysia: ..."; Chinese "韩国旅游配套：..." in `tours_zh.py`). The meta description adds the departure months; the share image is the tour hero.
- `feedback.py`: the feedback form (also used by `standalone.py`, which also holds the Google Apps Script for the response sheet).
- CSS is concatenated in this order: `site.css`, `pages.css`, `home.css`, `premium.css`, `type.css`, `red.css`, `zh.css`. Later files override earlier ones. `zh.css` only applies under `html:lang(zh)`.
- Home hero: `globe.js` + `globe.css` (d3-geo orthographic globe), landmark line art in `art/*.svg`, imported by `import_art.py` into `landmark-art.js`.

## Chinese site

`build.py` builds every page twice: English into `dist/`, then Chinese into `dist/zh/` (the feedback form is already bilingual and has no twin).
- Content: `zh.py` (services, tour cards, members, hours), `tours_zh.py` (itineraries), `articles_zh.py` (journal). Overlays keyed by slug; images, codes and links stay in `data.py` / `articles.py`.
- Template wording: the `UI` dict in `zh.py` maps exact English fragments of the rendered HTML to Chinese. When you change English copy in `build.py`, update the matching key. The build stops if a key no longer matches anything, or if a run of English words is left on a Chinese page (allowed names are in `KEEP`).
- Brand names stay in English on the Chinese site: YSL Travel & Tours (or YSL), tour brands and Golden Destinations tour names, airlines, Ctrip, shops and venues. Exception: YSL's own tour 大美青甘. Add any new brand to `KEEP` in `zh.py`.
- Malaysian Chinese usage: 配套, 纽西兰, 巴生, 冷气. Chinese has no italics: red accent words stay upright.

## Output gotcha

`build.py` writes HTML through `encode('ascii', 'xmlcharrefreplace')`. Non-ASCII text inside `<script>` must be written as `\uXXXX` escapes, or it turns into `&#...;` entities and breaks.

## Design rules (agreed with the client)

- Fonts: Instrument Serif (headings, upright), Inter Tight (text), IBM Plex Mono (codes, labels). Only red accent words in headings are italic.
- Colour: ivory body, dark maroon bands (#4a0a19 family), bright logo red #e72629 for the closing band, primary buttons, figures and accent words. 5px red rule under the header.
- Buttons: subtle, all caps, no arrows. No dash before eyebrows.
- Airport codes (KUL etc.) stay: they tie to the YSL name card.

## Content rules

- No prices anywhere on the site; fares are "on request" to drive enquiries.
- Do not copy Golden Destinations itinerary text verbatim; rewrite in YSL's voice.
- Do not feature YSL's own coaches.
- British spelling. Plain, confident copy; no filler.
- Placeholders YSL still has to supply are marked with the `tbc` class (yellow highlight).
- Golden Destinations stays low-key (client request): no GD headings or sections. Partner-tour cards say "Partner tour"; GD is named only in the partner list (`BRANDS`), the "Tour by" line and the small print on its tour pages.
- Holidays & Tours is one grid filtered by region (`cat` in `TOURS`: asia, europe, africa, oceania), YSL's own tours first. No airline logos or lists: YSL sells all airlines.
- Credentials (all confirmed by YSL): MOTAC KPL 6107, IATA accredited, MATTA, MITA, MICA, MCTA. Shown as text until YSL supplies the logo files; for IATA only the "IATA Accredited Agent" mark from IATA's agent portal may be used.
- Partners (confirmed): Apple Vacations, Lovely Vacation, UbinGO Vacations, FS Holidays, Parlo Tours (less active, still listed), Golden Destinations.
- The "Planning a company incentive trip" journal story is held back until YSL's client approves it (it was in `articles.py` / `articles_zh.py`; restore from git history).

## Feedback form

- Responses go to the Google Sheet "YSL Tour Feedback" (travelwithysl@gmail.com) via the Apps Script web app URL in `feedback-site/config.js`.
- All questions required except email and testimonial consent (marketing consent must stay optional under PDPA). Privacy Notice consent is required.
- Trip details from a pre-filled link (`?code=&leader=&dep=&ret=`) are locked on the form.
- Sheet tabs: Responses (master), Summary (per tour code), Tour view (dropdown filter on B2). Changing the script means pasting it into the sheet's Apps Script and deploying a New version (same URL).
