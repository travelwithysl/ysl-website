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

## Domain and SEO

- Domain ysltravel.com is registered at Squarespace. Official address: `SITE = 'https://www.ysltravel.com'` in `build.py` (www works with Squarespace DNS via a CNAME to Cloudflare Pages; the bare domain should forward to it). Change `SITE` if the address changes.
- Before launch, ysltravel.com only forwards to YSL's Facebook page (no old website, so no redirects needed). At launch, replace that forwarding in Squarespace: `www` CNAME to the Cloudflare Pages project, and the bare domain forwarded to https://www.ysltravel.com.
- The domain is linked to Google Workspace in Squarespace: never touch its MX or TXT records (email and Google verification). Today one forwarding rule sends both `www.ysltravel.com` and `ysltravel.com` to facebook.com/ysltravel (temporary, SSL off). At launch: take `www` out of that rule, point the bare domain to https://www.ysltravel.com (permanent, SSL on), then add the `www` CNAME from Cloudflare Pages.
- Every page gets a canonical link, hreflang alternates (en, zh-Hans, x-default), Open Graph and Twitter tags with absolute image URLs, and favicon links. `build.py` also writes `dist/sitemap.xml` (both languages, no 404) and `dist/robots.txt`.
- Favicons: `dist/assets/favicon.svg` (the YSL pin from `entrance.html`), `favicon-32.png`, `apple-touch-icon.png` (pin on maroon), and `dist/favicon.ico`. Hand-placed: do not delete.

## Source map

- `build.py`: page templates (`build_home`, `build_corporate`, `build_about`, `build_services`, `build_tours`, tour pages, journal, contact).
- `data.py`: tours, services, contact details, Golden Destinations itineraries. `articles.py`: journal articles (each has `seo`, the page title; the lead is the meta description; the photo is the share image).
- `legal.py`: Privacy Notice text (English and Bahasa Malaysia on `privacy.html`, as the PDPA requires both; Chinese on `zh/privacy.html`). `build_404()` writes `404.html` and `zh/404.html` with a `<base>` tag, so they work at any URL on Cloudflare Pages.
- Golden Destinations dates: `GD_DATES` in `data.py` (GD tour code + ISO dates, from `https://www.gd.my/b2c2b/api/v1/series/<CODE>?business_type=b2c2b&type=series`, the JSON behind `gd.my/web/itinerary/<CODE>`). Card months (`departs`) and the tour-page date list are built from it, in both languages. GD photos: `dist/assets/gd-<tour>-card.jpg` (5:4) and `-hero.jpg`.
- Apple Vacations tours (`ap-*` slugs) use the same `GD_TOURS` / `GD_DATES` structures with `brand='Apple Vacations'`. Source: `applevacations.my/en/tour.php?pckg_id=<id>` (server-rendered HTML: days, hotels, meals, and a departure table where bookable rows have a `booking.php` link; rows marked Full are left out). Apple's photos sit on `aws.applevacations.my:2030`, which the environment's proxy cannot reach (non-443 port), so Apple tour pages use GD photos of the same places (Greece was swapped for Morocco for lack of photos). Apple pages say "Images are for illustration purposes only." in the small print.
- YSL's own tours: Majestic Qinghai & Gansu (大美青甘, own template `build_tour_qg`) and Golden Peak, Hidden Lake (金山秘湖, `tour-yunnan.html`, from YSL's itinerary PDF, built with the partner template and `brand='YSL Travel &amp; Tours'`). The old "Yunnan & Shangri-La" sample page is gone.
- YSL's own tour dates: `YSL_DATES` in `data.py` (dates from YSL); `QG['date_notes']` tags single dates (School holidays, Fully booked). Seat counts and fares stay off the site.
- GD tour SEO: each GD tour has `seo` (the page `<title>`, keyword first: "Korea Tour Package from Malaysia: ..."; Chinese "韩国旅游配套：..." in `tours_zh.py`). The meta description adds the departure months; the share image is the tour hero.
- `feedback.py`: the feedback form (also used by `standalone.py`, which also holds the Google Apps Script for the response sheet).
- Logo: header and footer use `source/logo-full.svg` (YSL's own full lockup with TRAVEL & TOURS, trimmed, colours inlined); header 84px tall on desktop, logo 60px (50px on mobile). `logo.svg` (mark only) is still used for the favicon source.
- Icons: `source/icons.svg`. The eight service icons (air, ins, hotel, tour, visa, mice, transfer, coach) come from YSL's own `YSL2026 - services.svg`; cruise and the corporate-page icons were redrawn to match (thin 0.85 line on a 24 grid). Keep any new icon in that style.
- CSS is concatenated in this order: `site.css`, `pages.css`, `home.css`, `premium.css`, `type.css`, `red.css`, `zh.css`. Later files override earlier ones. `zh.css` only applies under `html:lang(zh)`.
- Home hero: `globe.js` + `globe.css` (d3-geo orthographic globe), landmark line art in `art/*.svg`, imported by `import_art.py` into `landmark-art.js`.

## Chinese site

`build.py` builds every page twice: English into `dist/`, then Chinese into `dist/zh/` (the feedback form is already bilingual and has no twin).
- Content: `zh.py` (services, tour cards, members, hours), `tours_zh.py` (itineraries), `articles_zh.py` (journal). Overlays keyed by slug; images, codes and links stay in `data.py` / `articles.py`.
- Template wording: the `UI` dict in `zh.py` maps exact English fragments of the rendered HTML to Chinese. When you change English copy in `build.py`, update the matching key. The build stops if a key no longer matches anything, or if a run of English words is left on a Chinese page (allowed names are in `KEEP`).
- Brand names stay in English on the Chinese site: YSL Travel & Tours (or YSL), tour brands and Golden Destinations tour names, airlines, Ctrip, shops and venues. Exception: YSL's own tours 大美青甘 and 金山秘湖. Add any new brand to `KEEP` in `zh.py`.
- Chinese voice: written as original Chinese, not translated: short, poised, a little poetic in headlines (e.g. 千里之行，始于图上一点。), plain and warm in body text. Lines break only after punctuation: `zh.phrase_breaks()` wraps each phrase of h1–h3 and `.lead`/`.sub`/`.line` paragraphs in `.ph` (inline-block), and Chinese `.h-xxl` has no width cap.
- Malaysian Chinese usage: 配套, 纽西兰, 巴生, 冷气, 联络 (not 联系), 讯息 (not 信息, for messages), 雪糕 (not 冰淇淋), 手信, 巴士 (not 大巴), 电动车 (not 电瓶车), 名牌折扣商场 (not 奥特莱斯), 专人负责 (not 对接), 办理登机 (not 值机), 度假会议/度假营 (not 退修), 外州, 华语. Chinese has no italics: red accent words stay upright.

## Output gotcha

`build.py` writes HTML through `encode('ascii', 'xmlcharrefreplace')`. Non-ASCII text inside `<script>` must be written as `\uXXXX` escapes, or it turns into `&#...;` entities and breaks.

## Design rules (agreed with the client)

- Fonts: Instrument Serif (headings, upright), Inter Tight (text), IBM Plex Mono (codes, labels). Only red accent words in headings are italic.
- Colour: ivory body, dark maroon bands (#4a0a19 family), bright logo red #e72629 for the closing band, primary buttons, figures and accent words. 5px red rule under the header.
- Buttons: subtle, all caps, no arrows. No dash before eyebrows.
- Airport codes (KUL etc.) stay: they tie to the YSL name card.
- Tour cards show `From KUL` unless the tour sets `origin` (Golden Peak, Hidden Lake flies Batik Air OD696/OD697 from Subang, `SZB`).

## Content rules

- No prices anywhere on the site; fares are "on request" to drive enquiries.
- Do not copy Golden Destinations itinerary text verbatim; rewrite in YSL's voice.
- Do not feature YSL's own coaches.
- British spelling. Plain, confident copy; no filler.
- Placeholders YSL still has to supply are marked with the `tbc` class (yellow highlight).
- Golden Destinations and Apple Vacations stay low-key (client request): no brand headings or sections. Partner-tour cards say "Partner tour"; the brand is named only in the partner list (`BRANDS`), the "Tour by" line and the small print on its tour pages.
- Holidays & Tours is one grid filtered by region (`cat` in `TOURS`: asia, europe, africa, oceania), YSL's own tours first. No airline logos or lists: YSL sells all airlines.
- Credentials (confirmed by YSL): MOTAC KPL 6107, MATTA, MITA, MICA, MCTA. Their logos, in colour, sit on an ivory strip above the footer on every page (`assoc_strip()` in `build.py`; files `dist/assets/assoc-*.png`, taken from trulytravelmart.com.my, hand-placed). No tourism-board logos (they imply an endorsement YSL doesn't have). The MOTAC crest is left out: the only copy found carries the ministry's old name. IATA is held back for now at YSL's request (if it returns, only the "IATA Accredited Agent" mark from IATA's agent portal may be used).
- Partners (confirmed): Apple Vacations, Lovely Vacation, UbinGO Vacations, FS Holidays, Parlo Tours (less active, still listed), Golden Destinations.
- No case studies or named past projects on the corporate page: corporate work is usually under NDA. No client logos either (`dist/assets/clients.jpg` is kept but unused). Corporate figures: largest single group 300+, MICE projects delivered 100+ (confirm with YSL if they change).
- No home-page testimonial until the feedback form brings in good reviews. The main site has no copy of the feedback form (it lives only at feedback.ysltravel.com).
- Social: Facebook /ysltravel and Instagram @ysltravel (`CONTACT` in `data.py`).
- WhatsApp: +60 16-626 4500, the office line (no one carries it; checked during office hours), so the site says "We reply during office hours." Every enquiry button leads to the contact form, which opens WhatsApp with the message filled in (`CONTACT['wa']`); from a tour page it presets "Tour packages".
- The "Planning a company incentive trip" journal story is held back until YSL's client approves it (it was in `articles.py` / `articles_zh.py`; restore from git history).

## Feedback form

- Responses go to the Google Sheet "YSL Tour Feedback" (travelwithysl@gmail.com) via the Apps Script web app URL in `feedback-site/config.js`.
- All questions required except email and testimonial consent (marketing consent must stay optional under PDPA). Privacy Notice consent is required.
- Trip details from a pre-filled link (`?code=&leader=&dep=&ret=`) are locked on the form.
- Sheet tabs: Responses (master), Summary (per tour code), Tour view (dropdown filter on B2). Changing the script means pasting it into the sheet's Apps Script and deploying a New version (same URL).
