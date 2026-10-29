/**
 * Play-listing assets from the live reader (wave 73): six phone screenshots per language at 1080×1920 (a 360×640
 * viewport at 3×, the 9:16 Play wants) and the 1024×500 feature graphic drawn from the same colours and glyph as the
 * icon. Nothing is mocked — every screenshot is the app as it runs, on the first story of the shelf.
 *
 *   NODE_PATH=<node_modules> CHROMIUM_PATH=<chrome> node tools/store_shots.js [outdir=research/store] [reader]
 */
const { chromium } = require('playwright-core'); const fs = require('fs'); const path = require('path'); const { pathToFileURL } = require('url');
const OUT = path.resolve(process.argv[2] || path.join(__dirname, '..', 'research', 'store'));
const READER = path.resolve(process.argv[3] || path.join(__dirname, '..', 'prototype', 'reader.html'));
const CREAM = '#faf6ef', GREEN = '#0f5c4a';
const TAG = { en: ['Classical Arabic, one story at a time', 'madrasah grammar on every word · offline'],
              tr: ['Klasik Arapça, her seferinde bir hikâye', 'her kelimede medrese grameri · çevrimdışı'] };
function feature(lang) {
  return `<!doctype html><meta charset="utf-8"><style>
    html,body{margin:0;width:1024px;height:500px;background:${CREAM};font-family:Georgia,"Noto Serif",serif;color:#1d1a14;overflow:hidden}
    .g{position:absolute;right:70px;top:40px;font-family:"Amiri","Scheherazade New","Noto Naskh Arabic",serif;font-size:300px;line-height:1;color:${GREEN}}
    .t{position:absolute;left:70px;top:150px;font-size:64px;font-weight:700;color:${GREEN};letter-spacing:.01em}
    .s{position:absolute;left:72px;top:240px;font-size:30px;color:#3b362c}.s2{position:absolute;left:72px;top:290px;font-size:22px;color:#5d574b;letter-spacing:.06em;text-transform:uppercase;font-family:system-ui,sans-serif}
    .bar{position:absolute;left:0;right:0;bottom:0;height:14px;background:${GREEN}}</style>
    <div class="g" lang="ar" dir="rtl">ق</div><div class="t">Qissa</div><div class="s">${TAG[lang][0]}</div><div class="s2">${TAG[lang][1]}</div><div class="bar"></div>`;
}
(async () => {
  const browser = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const url = pathToFileURL(READER).href;
  for (const lang of ['en', 'tr']) {
    const dir = path.join(OUT, lang); fs.mkdirSync(dir, { recursive: true });
    const ctx = await browser.newContext({ viewport: { width: 360, height: 640 }, deviceScaleFactor: 3 });
    await ctx.addInitScript(l => { localStorage.setItem('qissa-welcomed', '1'); localStorage.setItem('qissa-lang', l); }, lang);
    const p = await ctx.newPage(); await p.goto(url); await p.waitForSelector('.lib-card'); await p.waitForTimeout(600);
    let n = 0; const shot = async name => { n++; await p.waitForTimeout(350); const f = path.join(dir, `${String(n).padStart(2, '0')}-${name}.png`); await p.screenshot({ path: f }); console.log(lang, path.basename(f)); };
    await shot('library');
    await p.locator('.lib-card').first().click(); await p.waitForSelector('.word'); await shot('story');
    await p.locator('.word').nth(3).click(); await p.waitForSelector('.sheet.show'); await shot('word');
    await p.evaluate(() => document.getElementById('scrim').click()); await p.waitForTimeout(300);
    const tark = p.locator('button:has-text("تركيب")').first();
    if (await tark.count()) { await tark.click(); await p.waitForSelector('.sheet.show'); await shot('tarkib'); await p.evaluate(() => document.getElementById('scrim').click()); await p.waitForTimeout(300); }
    await p.evaluate(() => openGames()); await p.waitForSelector('.sheet.show .game-pick'); await shot('games');
    await p.evaluate(() => document.getElementById('scrim').click()); await p.waitForTimeout(300);
    await p.evaluate(() => openConjugator()); await p.waitForSelector('.sheet.show'); await shot('workshop');
    await ctx.close();
    const fp = await browser.newPage({ viewport: { width: 1024, height: 500 } });
    await fp.setContent(feature(lang)); await fp.waitForTimeout(150);
    await fp.screenshot({ path: path.join(OUT, `feature-graphic-${lang}.png`) }); await fp.close(); console.log(lang, 'feature-graphic');
  }
  await browser.close();
})().catch(e => { console.error('ERR', e.message); process.exit(1); });
