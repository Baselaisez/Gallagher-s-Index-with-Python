/**
 * Render the app icons from one HTML source, so the letter, the colours and the
 * proportions live in a single place and every size is the same drawing.
 *
 *   NODE_PATH=<node_modules> CHROMIUM_PATH=<chrome> node tools/make_icons.js
 *
 * Writes prototype/icons/. Re-run only when the design changes; the PNGs are
 * committed, because a build that needs a browser to produce an icon is a build
 * that breaks on someone else's machine.
 */
const { chromium } = require('playwright-core');
const fs = require('fs');
const path = require('path');

const OUT = path.resolve(__dirname, '..', 'prototype', 'icons');
const CREAM = '#faf6ef', GREEN = '#0f5c4a';

// `safe` is the maskable padding: Android may crop to a circle, so the letter
// has to sit inside the middle 80% or it loses its tail.
function html({ bg, fg, safe }) {
  const pad = safe ? 12 : 0;
  return `<!doctype html><meta charset="utf-8">
  <style>
    html,body{margin:0;height:100%;}
    body{background:${bg};display:grid;place-items:center;}
    .g{width:${100 - pad * 2}%;height:${100 - pad * 2}%;display:grid;place-items:center;
       border-radius:${safe ? 0 : 22}%;background:${bg};}
    .q{font-family:"Amiri","Scheherazade New","Noto Naskh Arabic",serif;
       color:${fg};font-size:62vmin;line-height:1;transform:translateY(-4%);}
  </style>
  <div class="g"><div class="q" lang="ar" dir="rtl">ق</div></div>`;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const jobs = [
    { file: 'icon-192.png', size: 192, bg: CREAM, fg: GREEN, safe: false },
    { file: 'icon-512.png', size: 512, bg: CREAM, fg: GREEN, safe: false },
    // Maskable wants full bleed and the subject inside the safe zone.
    { file: 'icon-maskable-512.png', size: 512, bg: GREEN, fg: CREAM, safe: true },
    { file: 'apple-touch-icon.png', size: 180, bg: CREAM, fg: GREEN, safe: false },
  ];
  for (const j of jobs) {
    const page = await browser.newPage({ viewport: { width: j.size, height: j.size } });
    await page.setContent(html(j));
    await page.waitForTimeout(120);           // let the webfont fall back and settle
    await page.screenshot({ path: path.join(OUT, j.file) });
    await page.close();
    console.log('wrote icons/' + j.file);
  }
  await browser.close();
})();
