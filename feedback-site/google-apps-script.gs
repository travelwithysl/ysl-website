/**
 * YSL tour feedback -> Google Sheet
 * 1. Create a Google Sheet named "YSL Tour Feedback".
 * 2. Extensions > Apps Script. Delete what is there, paste this whole file, Save.
 * 3. Deploy > New deployment > type: Web app.
 *      Execute as: Me      Who has access: Anyone
 *    Deploy, authorise, then copy the Web app URL (ends in /exec).
 * 4. Paste that URL into config.js on the feedback site and re-upload.
 * Ratings are stored as numbers: 4 Excellent, 3 Good, 2 Average, 1 Poor.
 */
var COLUMNS = [
  'submitted_at', 'tour_code', 'tour_leader', 'departure', 'return',
  'leader_lead', 'leader_attitude', 'leader_knowledge',
  'guide_lead', 'guide_attitude', 'guide_knowledge',
  'tour_itinerary', 'tour_hotel', 'tour_meals', 'tour_transport', 'tour_driver',
  'overall', 'comments', 'times', 'reasons', 'reasons_other', 'source', 'source_other',
  'name', 'phone', 'email'
];

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getSheets()[0];
    if (sheet.getLastRow() === 0) {
      sheet.appendRow(COLUMNS);
      sheet.setFrozenRows(1);
      sheet.getRange(1, 1, 1, COLUMNS.length).setFontWeight('bold');
    }
    var d = JSON.parse(e.postData.contents);
    var row = COLUMNS.map(function (k) {
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
