// v356-G — runs tools/inventory_probe.js once in a fresh built page: node tools/inventory_prove.js <out.json>
// (prototype/reader.html, or SMOKE_READER). tools/inventory.py calls it; the smoke suite evaluates the probe on its own page instead.
const { chromium } = require('playwright-core'); const fs = require('fs'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH }); const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.setItem('qissa-welcomed', '1'); } catch (e) {} });
  await p.goto('file://' + path.resolve(process.env.SMOKE_READER || path.join(__dirname, '../prototype/reader.html')), { waitUntil: 'load', timeout: 600000 });
  await p.waitForFunction(() => typeof STORIES !== 'undefined' && STORIES.length > 10, null, { timeout: 600000, polling: 1000 });
  const src = fs.readFileSync(path.join(__dirname, 'inventory_probe.js'), 'utf8');
  const out = await p.evaluate(s => (0, eval)(s)(), src);
  fs.writeFileSync(process.argv[2], JSON.stringify(out)); await b.close();
})().catch(e => { console.error(e); process.exit(1); });
