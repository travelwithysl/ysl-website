# YSL Travel & Tours website: notes for Claude

Client: YSL Travel & Tours Sdn Bhd (877803-T), Klang, Malaysia. Licence KPL 6107 (MOTAC).
Built and maintained by Twain Productions (Michelle Liu). The 2020 YSL brand identity is Twain's work: keep continuity with it.

## Layout

| Path | What | Deployed |
|---|---|---|
| `source/` | Static-site generator (Python, no dependencies) and all CSS/JS | no |
| `dist/` | Built main website, including all images in `dist/assets/` | not yet (prototype only) |
| `feedback-site/` | Tour feedback form + link maker, live at feedback.ysltravel.com | Cloudflare Pages project `ysl-feedback`, output dir `feedback-site`, no build command |

Build: `cd source && python3 build.py` writes the HTML into `../dist` (images in `dist/assets` are hand-placed: never delete them).
`python3 standalone.py` rebuilds `../feedback-site` from the same form code (`feedback.py`).
Commit the built output with the source change: Cloudflare serves the committed files, it does not build.

## Source map

- `build.py`: page templates (`build_home`, `build_corporate`, `build_about`, `build_services`, `build_tours`, tour pages, journal, contact).
- `data.py`: tours, services, contact details, Golden Destinations itineraries. `articles.py`: journal articles.
- `feedback.py`: the feedback form (also used by `standalone.py`, which also holds the Google Apps Script for the response sheet).
- CSS is concatenated in this order: `site.css`, `pages.css`, `home.css`, `premium.css`, `type.css`, `red.css`. Later files override earlier ones.
- Home hero: `globe.js` + `globe.css` (d3-geo orthographic globe), landmark line art in `art/*.svg`, imported by `import_art.py` into `landmark-art.js`.

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

## Feedback form

- Responses go to the Google Sheet "YSL Tour Feedback" (travelwithysl@gmail.com) via the Apps Script web app URL in `feedback-site/config.js`.
- All questions required except email and testimonial consent (marketing consent must stay optional under PDPA). Privacy Notice consent is required.
- Trip details from a pre-filled link (`?code=&leader=&dep=&ret=`) are locked on the form.
- Sheet tabs: Responses (master), Summary (per tour code), Tour view (dropdown filter on B2). Changing the script means pasting it into the sheet's Apps Script and deploying a New version (same URL).
