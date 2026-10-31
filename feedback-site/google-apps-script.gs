/**
 * YSL tour feedback -> Google Sheet
 * 1. Open the "YSL Tour Feedback" sheet > Extensions > Apps Script.
 * 2. Replace everything in Code.gs with this file, Save.
 * 3. First time: Deploy > New deployment > Web app (Execute as: Me, Who has access: Anyone),
 *    then paste the /exec URL into config.js.
 *    Updating: Deploy > Manage deployments > pencil > Version: New version > Deploy (URL stays the same).
 * 4. Optional, once: choose setupSheets in the function list at the top and click Run,
 *    to build the Summary and Tour view tabs straight away (otherwise they appear with the next response).
 *
 * Tabs:
 *   Responses  every submission, one row each (the master record)
 *   Summary    one row per tour: responses, average scores, how many agreed to be quoted
 *   Tour view  pick a tour code from the dropdown in B2; only that tour's responses are listed
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
var NUMBERS = ['leader_lead', 'leader_attitude', 'leader_knowledge', 'guide_lead', 'guide_attitude', 'guide_knowledge',
  'tour_itinerary', 'tour_hotel', 'tour_meals', 'tour_transport', 'tour_driver', 'overall'];
var RED = '#bb2030';

function responsesSheet_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sh = ss.getSheetByName('Responses');
  if (!sh) { sh = ss.getSheets()[0]; sh.setName('Responses'); }
  return sh;
}

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.waitLock(10000);
  try {
    var sheet = responsesSheet_();
    var d = JSON.parse(e.postData.contents);
    // tidy the tour code so small slips land in the same tour
    if (d.tour_code) d.tour_code = String(d.tour_code).trim().toUpperCase().replace(/\s+/g, '');
    var header = sheet.getLastRow() === 0 ? [] : sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
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
      if (NUMBERS.indexOf(k) >= 0 && v !== '') return Number(v);
      return String(v);
    });
    sheet.appendRow(row);
    // keep the tour code as text (so codes like 261022 are not turned into numbers)
    sheet.getRange(sheet.getLastRow(), header.indexOf('tour_code') + 1).setNumberFormat('@');
    setupSheets();
    return ContentService.createTextOutput(JSON.stringify({ ok: true })).setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

/** Adds a YSL Feedback menu to the sheet. */
function onOpen() {
  SpreadsheetApp.getUi().createMenu('YSL Feedback')
    .addItem('Refresh summary', 'setupSheets')
    .addToUi();
}

/** Builds or refreshes the Summary and Tour view tabs. Safe to run any time. */
function setupSheets() {
  refreshSummary_();
  buildTourView_();
}

function avg_(rows, idx) {
  var n = 0, t = 0;
  idx.forEach(function (i) { rows.forEach(function (r) { var v = r[i]; if (typeof v === 'number' && !isNaN(v)) { t += v; n++; } }); });
  return n ? Math.round(t / n * 100) / 100 : '';
}

function refreshSummary_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var src = responsesSheet_();
  var sum = ss.getSheetByName('Summary') || ss.insertSheet('Summary', 1);
  sum.clear();
  var head = ['Tour code', 'Tour leader', 'Departure', 'Responses', 'Overall /100', 'Tour leader /4', 'Local guide /4',
              'Itinerary /4', 'Hotel /4', 'Meals /4', 'Transport /4', 'Driver /4', 'OK to quote', 'Last response'];
  sum.getRange(1, 1, 1, head.length).setValues([head]).setFontWeight('bold').setFontColor('#ffffff').setBackground(RED);
  sum.setFrozenRows(1);
  if (src.getLastRow() < 2) return;
  var data = src.getDataRange().getValues(), h = data.shift();
  var c = function (k) { return h.indexOf(k); };
  var groups = {};
  data.forEach(function (r) {
    var code = String(r[c('tour_code')] || '').trim();
    if (!code) return;
    (groups[code] = groups[code] || []).push(r);
  });
  var out = Object.keys(groups).map(function (code) {
    var rows = groups[code], last = rows[rows.length - 1];
    var dep = last[c('departure')];
    return [code, last[c('tour_leader')], dep, rows.length,
      avg_(rows, [c('overall')]),
      avg_(rows, [c('leader_lead'), c('leader_attitude'), c('leader_knowledge')]),
      avg_(rows, [c('guide_lead'), c('guide_attitude'), c('guide_knowledge')]),
      avg_(rows, [c('tour_itinerary')]), avg_(rows, [c('tour_hotel')]), avg_(rows, [c('tour_meals')]),
      avg_(rows, [c('tour_transport')]), avg_(rows, [c('tour_driver')]),
      rows.filter(function (r) { return r[c('testimonial_consent')] === 'yes'; }).length,
      last[c('submitted_at')]];
  });
  // newest departures first
  out.sort(function (a, b) { return new Date(b[2]) - new Date(a[2]); });
  sum.getRange(2, 1, out.length, head.length).setValues(out);
  sum.getRange(2, 1, out.length, 1).setNumberFormat('@');
  sum.getRange(2, 3, out.length, 1).setNumberFormat('d mmm yyyy');
  sum.getRange(2, 14, out.length, 1).setNumberFormat('d mmm yyyy, h:mm am/pm');
  // highlight weak spots: overall below 70, ratings below 3
  var rules = [
    SpreadsheetApp.newConditionalFormatRule().whenNumberLessThan(70).setBackground('#fde8e8').setFontColor('#9b1219')
      .setRanges([sum.getRange(2, 5, out.length, 1)]).build(),
    SpreadsheetApp.newConditionalFormatRule().whenNumberLessThan(3).setBackground('#fde8e8').setFontColor('#9b1219')
      .setRanges([sum.getRange(2, 6, out.length, 7)]).build()
  ];
  sum.setConditionalFormatRules(rules);
  sum.autoResizeColumns(1, head.length);
}

function buildTourView_() {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var v = ss.getSheetByName('Tour view');
  var fresh = !v;
  if (fresh) v = ss.insertSheet('Tour view', 2);
  // dropdown of tour codes, fed from the Summary tab so new tours appear automatically
  var rule = SpreadsheetApp.newDataValidation().requireValueInRange(ss.getSheetByName('Summary').getRange('A2:A'), true)
    .setAllowInvalid(false).setHelpText('Pick a tour code').build();
  v.getRange('B2').setDataValidation(rule);
  if (!fresh) return;
  v.getRange('A1').setValue('Tour view').setFontSize(14).setFontWeight('bold');
  v.getRange('A2').setValue('Tour code').setFontWeight('bold');
  v.getRange('B2').setBackground('#fff4d6').setFontWeight('bold').setNumberFormat('@');
  v.getRange('C2').setValue('← pick a tour code from the dropdown').setFontColor('#888888');
  v.getRange('A3').setValue('Responses').setFontWeight('bold');
  v.getRange('B3').setFormula('=IF(B2="","",COUNTIF(Responses!B:B,B2))');
  v.getRange('A4').setValue('Overall average /100').setFontWeight('bold');
  v.getRange('B4').setFormula('=IF(B2="","",IFERROR(ROUND(AVERAGEIF(Responses!B:B,B2,INDEX(Responses!A:AZ,0,MATCH("overall",Responses!1:1,0))),1),""))');
  v.getRange('A6').setFormula('=Responses!A1:AZ1');
  v.getRange('A6:AZ6').setFontWeight('bold').setFontColor('#ffffff').setBackground(RED);
  v.getRange('A7').setFormula('=IF(B2="","",IFERROR(FILTER(Responses!A2:AZ,Responses!B2:B=B2),"No responses for this tour yet"))');
  v.setFrozenRows(6);
}
