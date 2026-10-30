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

// Android (wave 69): `--android android/app/src/main/res` writes the launcher mipmaps the Capacitor project
// needs — ic_launcher / ic_launcher_round at 48·72·96·144·192 and the adaptive FOREGROUND at 108·162·216·324·432,
// whose glyph must sit inside the middle 66 % (the system masks the outer ring). The background colour of the
// adaptive icon is a resource (values/ic_launcher_background.xml), so the foreground is drawn on TRANSPARENT.
const ANDROID = (() => { const i = process.argv.indexOf('--android'); return i > 0 ? path.resolve(process.argv[i + 1]) : null; })();
const DENS = [['mdpi', 48, 108], ['hdpi', 72, 162], ['xhdpi', 96, 216], ['xxhdpi', 144, 324], ['xxxhdpi', 192, 432]];
function fgHtml() {
  return `<!doctype html><meta charset="utf-8">
  <style>html,body{margin:0;height:100%;background:transparent;}body{display:grid;place-items:center;}
    .q{font-family:"Amiri","Scheherazade New","Noto Naskh Arabic",serif;color:${GREEN};font-size:40vmin;line-height:1;transform:translateY(-4%);}</style>
  <div class="q" lang="ar" dir="rtl">ق</div>`;
}

(async () => {
  fs.mkdirSync(OUT, { recursive: true });
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  if (ANDROID) {
    for (const [d, launcher, fg] of DENS) {
      const dir = path.join(ANDROID, 'mipmap-' + d); fs.mkdirSync(dir, { recursive: true });
      for (const f of ['ic_launcher.png', 'ic_launcher_round.png']) {
        const page = await browser.newPage({ viewport: { width: launcher, height: launcher } });
        await page.setContent(html({ bg: CREAM, fg: GREEN, safe: true })); await page.waitForTimeout(120);
        await page.screenshot({ path: path.join(dir, f) }); await page.close();
      }
      const page = await browser.newPage({ viewport: { width: fg, height: fg } });
      await page.setContent(fgHtml()); await page.waitForTimeout(120);
      await page.screenshot({ path: path.join(dir, 'ic_launcher_foreground.png'), omitBackground: true }); await page.close();
      console.log('wrote mipmap-' + d + ' (' + launcher + ' / ' + fg + ')');
    }
    await browser.close(); return;
  }
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
