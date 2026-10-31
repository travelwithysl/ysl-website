# YSL Travel & Tours website

| Folder | What it is | Served by |
|---|---|---|
| `feedback-site/` | Tour feedback form and link maker, live at feedback.ysltravel.com | Cloudflare Pages project `ysl-feedback` (build output: `feedback-site`, no build command) |
| `source/` | Source for the main website (in progress). `python3 source/build.py` builds it; `python3 source/standalone.py` rebuilds `feedback-site/` | Not yet deployed |

Feedback responses go to the Google Sheet "YSL Tour Feedback" in YSL's Google account, via the Apps Script web app set in `feedback-site/config.js`.

Built by Twain Productions.
