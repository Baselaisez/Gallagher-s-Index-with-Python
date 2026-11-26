// v342-N — runs every ledger probe in the built page once: node tools/ledger/prove.js <in.json> <out.json>
// in: [{s,w,re,not}|{js}], out: [{ok, got}] (tools/ledger/probe.js evaluated inside prototype/reader.html, or SMOKE_READER).
const { chromium } = require('playwright'); const fs = require('fs'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + path.resolve(process.env.SMOKE_READER || path.join(__dirname, '../../prototype/reader.html')), { waitUntil: 'load', timeout: 600000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10, null, { timeout: 600000, polling: 2000 });
  const src = fs.readFileSync(path.join(__dirname, 'probe.js'), 'utf8'); const fn = src.slice(src.indexOf('(probes)'));
  const probes = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const out = await p.evaluate(([f, ps]) => (0, eval)('(' + f + ')')(ps), [fn, probes]);
  fs.writeFileSync(process.argv[3], JSON.stringify(out)); await b.close();
})();
