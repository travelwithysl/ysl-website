/**
 * YSL tour feedback -> Google Sheet
 * 1. Open the "YSL Tour Feedback" sheet > Extensions > Apps Script.
 * 2. Replace everything in Code.gs with this file, Save.
 * 3. First time: Deploy > New deployment > Web app (Execute as: Me, Who has access: Anyone),
 *    then paste the /exec URL into config.js.
 *    Updating: Deploy > Manage deployments > pencil > Version: New version > Deploy (URL stays the same).
 * Ratings are stored as numbers: 4 Excellent, 3 Good, 2 Average, 1 Poor.
 * Any new question added to the form later gets its own column automatically.
 */
var COLUMNS = [
  'submitted_at', 'tour_code', 'tour_leader', 'departure', 'return',
  'leader_lead', 'leader_attitude', 'leader_knowledge',
  'guide_lead', 'guide_attitude', 'guide_knowledge',
  'tour_itinerary', 'tour_hotel', 'tour_meals', 'tour_transport', 'tour_driver',
  'overall', 'comments', 'times', 'reasons', 'reasons_other', 'source', 'source_other',
  'name', 'phone', 'email', 'testimonial_consent', 'testimonial_credit', 'privacy_consent'
];

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    var d = JSON.parse(e.postData.contents);
    var header = sheet.getLastRow() === 0 ? [] : sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    // make sure every known column, and any new field, has a heading
    COLUMNS.concat(Object.keys(d)).forEach(function (k) {
      if (k !== 'page' && header.indexOf(k) < 0) header.push(k);
    });
    sheet.getRange(1, 1, 1, header.length).setValues([header]).setFontWeight('bold');
    sheet.setFrozenRows(1);
    var row = header.map(function (k) {
      var v = d[k];
      if (v === undefined || v === null) return '';
      if (Array.isArray(v)) return v.join(', ');
      if (k === 'submitted_at') return new Date(v);
      return v;
    });
    sheet.appendRow(row);
    return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}
