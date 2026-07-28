/**
 * Checks the installable / offline side of the app, which the main smoke suite
 * cannot: it runs on file://, where a service worker may not register at all.
 *
 *   NODE_PATH=<node_modules> CHROMIUM_PATH=<chrome> node tools/pwa_test.js
 *
 * Serves prototype/ from an ephemeral port, so there is nothing to start or
 * clean up by hand.
 */
const { chromium } = require('playwright-core');
const http = require('http');
const fs = require('fs');
const path = require('path');

const ROOT = path.resolve(__dirname, '..', 'prototype');
const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.webmanifest': 'application/manifest+json; charset=utf-8',
  '.png': 'image/png',
};

let failed = 0;
function ok(name, cond, detail) {
  console.log((cond ? 'PASS ' : 'FAIL ') + name + (cond ? '' : ' — ' + detail));
  if (!cond) failed++;
}

const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '') || 'reader.html';
  const file = path.join(ROOT, rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    res.writeHead(404); return res.end('not found');
  }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file)] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const base = 'http://127.0.0.1:' + server.address().port + '/';
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const ctx = await browser.newContext();
  const page = await ctx.newPage();
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));

  try {
    await page.goto(base + 'reader.html', { waitUntil: 'load' });

    // The charset must be declared. Served standalone nothing else supplies it,
    // and a document that is mostly Arabic decoded as latin-1 is unreadable —
    // this is exactly how that bug showed up.
    const charset = await page.evaluate(() => document.characterSet);
    ok('document is UTF-8', charset === 'UTF-8', charset);

    const man = await page.evaluate(async () => {
      const link = document.querySelector('link[rel=manifest]');
      if (!link) return null;
      const r = await fetch(link.href);
      return r.ok ? await r.json() : null;
    });
    ok('manifest resolves and parses', !!man, 'no manifest');
    if (man) {
      ok('manifest is installable', man.name && man.icons.length >= 2 &&
        man.icons.some(i => i.purpose === 'maskable') && man.display === 'standalone',
        JSON.stringify({ icons: man.icons.length, display: man.display }));
      const bad = [];
      for (const i of man.icons) {
        const st = await page.evaluate(async u => (await fetch(u)).status, new URL(i.src, base).href);
        if (st !== 200) bad.push(i.src + '->' + st);
      }
      ok('every icon resolves', !bad.length, bad.join(', '));
    }

    await page.evaluate(async () => {
      const r = await navigator.serviceWorker.register('sw.js');
      if (!r.active) await new Promise(res => (r.installing || r.waiting)
        .addEventListener('statechange', e => e.target.state === 'activated' && res()));
    });
    const entries = await page.evaluate(async () => {
      const keys = await caches.keys();
      const c = await caches.open(keys[0]);
      return (await c.keys()).map(q => new URL(q.url).pathname);
    });
    ok('service worker precaches the shell', entries.includes('/reader.html') &&
      entries.some(e => e.endsWith('.webmanifest')) && entries.some(e => e.endsWith('.png')),
      entries.join(', '));

    await page.reload({ waitUntil: 'load' });
    ok('service worker controls the page', await page.evaluate(() => !!navigator.serviceWorker.controller));

    // The real test: pull the network and reload.
    await ctx.setOffline(true);
    await page.reload({ waitUntil: 'load' });
    const off = await page.evaluate(() => ({
      stories: typeof STORIES !== 'undefined' ? STORIES.length : 0,
      notes: typeof GRAMMAR !== 'undefined' ? Object.keys(GRAMMAR).length : 0,
      cards: document.querySelectorAll('.lib-card').length,
    }));
    ok('app loads with the network off', off.stories > 0 && off.notes > 0 && off.cards > 0,
      JSON.stringify(off));
    await page.locator('.lib-card').first().click();
    const words = await page.locator('.sentence .word').count();
    ok('a story opens with the network off', words > 0, 'words=' + words);
    await ctx.setOffline(false);

    ok('no JS errors', errs.length === 0, errs.join(' | '));
  } catch (e) {
    ok('pwa run completed', false, String(e));
  } finally {
    await browser.close();
    server.close();
  }
  console.log(failed ? `\n${failed} failure(s)` : '\nall PWA checks passed');
  process.exit(failed ? 1 : 0);
})();
