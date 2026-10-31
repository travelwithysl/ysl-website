YSL TOUR FEEDBACK SITE  (feedback.ysltravel.com)
================================================

WHAT IS IN THIS FOLDER
  index.html        the feedback form (opens at feedback.ysltravel.com)
  links.html        link and QR maker for tour leaders (feedback.ysltravel.com/links)
  config.js         where the Google Sheet address goes (step B)
  assets/           styles and scripts
  _headers          keeps search engines away from the form
  google-apps-script.gs   paste into the response sheet (step B); not served

A. PUT IT ONLINE (Cloudflare Pages)
  1. dash.cloudflare.com > Workers & Pages > Create > Pages > Upload assets.
  2. Project name: ysl-feedback. Drag in THIS FOLDER (or the zip). Deploy.
     It is now live at ysl-feedback.pages.dev
  3. In the project: Custom domains > Set up a custom domain > feedback.ysltravel.com
     Cloudflare shows a CNAME record to add. Keep that tab open.
  4. Squarespace > Domains > ysltravel.com > DNS > Custom records > Add record:
        Host:  feedback
        Type:  CNAME
        Data:  ysl-feedback.pages.dev
     Do not change any other record (email and the current website keep working).
  5. Back in Cloudflare, wait for the domain to show Active (minutes to a few hours).
     HTTPS is set up automatically.

B. CONNECT THE GOOGLE SHEET (where responses go)
  1. Follow the steps at the top of google-apps-script.gs.
  2. Open config.js and paste the Web app URL between the quotes.
  3. Upload again: Cloudflare project > Create new deployment > drag the folder in.
  4. Test: fill in the form once, check the new row in the sheet.
  Until this is done, the form works but does not store answers (it says so on screen).

C. USING IT
  Open feedback.ysltravel.com/links, fill in the tour code, leader and dates,
  then copy the link for WhatsApp or download the QR code for the coach.
