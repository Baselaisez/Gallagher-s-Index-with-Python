// entrance_test.js <siteDir> (v334): serve the hosted copy (pubsplit output + welcome.html as index.html), open the entrance at 4× CPU,
// wait until it reports the app ready (every file in the offline cache), then open the app from the cache. Prints the timings.
const { chromium } = require('playwright'); const http = require('http'), fs = require('fs'), path = require('path');
const dir = process.argv[2];
const types = { '.html': 'text/html', '.js': 'text/javascript', '.json': 'application/json', '.webmanifest': 'application/manifest+json', '.png': 'image/png' };
const srv = http.createServer((q, r) => { let p = decodeURIComponent(q.url.split('?')[0]); if (p.endsWith('/')) p += 'index.html'; const f = path.join(dir, p);
  if (!f.startsWith(dir) || !fs.existsSync(f)) { r.writeHead(404); return r.end(); } const st = fs.statSync(f);
  r.writeHead(200, { 'content-type': types[path.extname(f)] || 'application/octet-stream', 'content-length': st.size }); if (q.method === 'HEAD') return r.end(); fs.createReadStream(f).pipe(r); }).listen(0);
(async () => { const base = 'http://127.0.0.1:' + srv.address().port + '/'; const b = await chromium.launch(); const ctx = await b.newContext({ viewport: { width: 390, height: 844 } });
  const p = await ctx.newPage(); const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
  const c = await ctx.newCDPSession(p); await c.send('Emulation.setCPUThrottlingRate', { rate: 4 });
  const t0 = Date.now(); await p.goto(base); const fcp = await p.evaluate(() => new Promise(r => new PerformanceObserver(l => r(l.getEntries()[0].startTime)).observe({ type: 'paint', buffered: true })));
  await p.waitForFunction(() => /✓/.test(document.getElementById('prepText').textContent) || /tamamlanamadı|Could not/.test(document.getElementById('prepText').textContent), null, { timeout: 300000 });
  const prep = await p.evaluate(() => document.getElementById('prepText').textContent); const tReady = Date.now() - t0;
  const cached = await p.evaluate(async () => { const ks = await caches.keys(); const c = await caches.open(ks[0]); return (await c.keys()).map(r => new URL(r.url).pathname); });
  await p.screenshot({ path: path.join(require('os').tmpdir(), 'qissa-entrance.png') });
  const t1 = Date.now(); await p.click('#open'); await p.waitForFunction(() => document.querySelector('.lib-card'), null, { timeout: 120000 }); const tOpen = Date.now() - t1;
  console.log(JSON.stringify({ fcp: Math.round(fcp), prep, tReadyMs: tReady, cached, tOpenAppMs: tOpen, errs: errs.slice(0, 5) }, null, 1));
  await b.close(); srv.close(); })();
