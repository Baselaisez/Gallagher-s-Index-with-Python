// v342-A — prove every probe of the aux ledgers against a built page.
// usage: node tools/ledger/aux_prove.js <probes.json: [{key, probe}]> [reader.html] > results.json  ({key: {ok, got}})
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
(async () => {
  const list = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const html = path.resolve(process.argv[3] || path.join(__dirname, '..', '..', 'prototype', 'reader.html'));
  const fn = fs.readFileSync(path.join(__dirname, 'aux_probe.js'), 'utf8').replace(/^\s*\/\/.*$/mg, '').trim();
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + html, { waitUntil: 'load', timeout: 300000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10, null, { timeout: 300000 });
  const res = await p.evaluate(([src, probes]) => (0, eval)('(' + src + ')')(probes), [fn, list.map(x => x.probe)]);
  const out = {}; list.forEach((x, i) => { out[x.key] = res[i]; });
  process.stdout.write(JSON.stringify(out));
  await b.close();
})();
