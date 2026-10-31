# YSL Travel & Tours website

| Folder | What it is | Served by |
|---|---|---|
| `feedback-site/` | Tour feedback form and link maker, live at feedback.ysltravel.com | Cloudflare Pages project `ysl-feedback` (build output: `feedback-site`, no build command) |
| `source/` | Source for the main website. `cd source && python3 build.py` builds it into `dist/`; `python3 standalone.py` rebuilds `feedback-site/` | — |
| `dist/` | The built main website (prototype), with all images | Not yet deployed |

Feedback responses go to the Google Sheet "YSL Tour Feedback" in YSL's Google account, via the Apps Script web app set in `feedback-site/config.js`.

Built by Twain Productions.
