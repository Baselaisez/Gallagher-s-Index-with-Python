// Qissa reader smoke test — drives both built readers in headless Chromium.
// Usage: npm i playwright-core && node tools/smoke_test.js
// Override the browser binary with CHROMIUM_PATH if needed.
const { chromium } = require('playwright-core');
const CHROME = process.env.CHROMIUM_PATH || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome';

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

  const url = 'file://' + require('path').resolve(__dirname, '..') + '/prototype/reader.html';
  await page.goto(url);
  const check = async (name, fn) => {
    try { await fn(); console.log('PASS', name); }
    catch (e) { console.log('FAIL', name, '—', e.message.split('\n')[0]); process.exitCode = 1; }
  };

  await check('library lists 2 stories, reader controls hidden', async () => {
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    if (await page.locator('.lib-card').count() !== 2) throw new Error('cards=' + await page.locator('.lib-card').count());
    if (await page.locator('#gamesOpen').isVisible()) throw new Error('reader controls visible in library');
  });

  await check('open story renders 2 chapters', async () => {
    await page.locator('.lib-card', { hasText: 'وَصِيَّةُ' }).click();
    if (await page.locator('.chapter-head').count() !== 2) throw new Error('chapter count');
    if (await page.locator('.sentence').count() !== 7) throw new Error('sentence count');
  });

  await check('tap-word opens sheet with tabs', async () => {
    await page.locator('.word', { hasText: 'اسْمَعْ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    const tabs = await page.locator('.sheet .tabs button').allTextContents();
    if (tabs.length < 4) throw new Error('tabs: ' + tabs.join('|'));
  });

  await check('sarf tab shows conjugation table', async () => {
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    await page.waitForSelector('table.conj', { timeout: 3000 });
    await page.locator('.tense-seg button', { hasText: 'الأمر' }).click();
    await page.waitForSelector('td.hl', { timeout: 3000 });
  });

  await check('grammar tab shows common mistakes', async () => {
    await page.locator('.sheet .tabs button', { hasText: 'Grammar' }).click();
    await page.waitForSelector('.mistake', { timeout: 3000 });
  });

  await check('save to flashcards updates deck badge', async () => {
    await page.locator('.sheet .tabs button', { hasText: 'Word' }).click();
    await page.locator('#saveBtn').click();
    const badge = await page.locator('#deckCount').textContent();
    if (badge !== '1') throw new Error('badge=' + badge);
  });

  await check('SRS review: reveal + Good schedules card', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#deckOpen').click();
    await page.locator('#reviewCard').click();
    await page.locator('#reviewCard').click();
    await page.locator('#goodBtn').click();
    const txt = await page.locator('.empty').textContent();
    if (!txt.includes('Next review')) throw new Error('no next-review text: ' + txt);
    if (!(await page.locator('#deckCount').isHidden())) throw new Error('badge should hide when nothing due');
  });

  await check('games: spot-the-error round works', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#gamesOpen').click();
    await page.locator('#gSpot').click();
    await page.waitForSelector('.opts button', { timeout: 3000 });
    await page.locator('.opts button').first().click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    await page.waitForSelector('.opts button.right', { timeout: 3000 });
    await page.locator('#sNext').click();
    await page.waitForSelector('.opts button:not([disabled])', { timeout: 3000 });
  });

  await check('games: harakat round shows i\'rab explanation', async () => {
    await page.locator('#gBack').click();
    await page.locator('#gHarakat').click();
    await page.waitForSelector('.game-q', { timeout: 3000 });
    await page.locator('.opts button').first().click();
    await page.waitForSelector('#hWhy .game-why', { timeout: 3000 });
  });

  await check('games: match completes', async () => {
    await page.locator('#gBack').click();
    await page.locator('#gMatch').click();
    await page.waitForSelector('.match-grid', { timeout: 3000 });
    // brute-force: click pairs by data-pair via evaluate
    await page.evaluate(() => {
      const btns = [...document.querySelectorAll('.match-grid [data-i]')];
      const byPair = {};
      btns.forEach(b => {
        const i = +b.dataset.i;
        const c = M.cards[i];
        (byPair[c.pair] = byPair[c.pair] || []).push(i);
      });
      Object.values(byPair).forEach(([a, b]) => { pickMatch(a); pickMatch(b); });
    });
    await page.waitForSelector('#replayM', { timeout: 3000 });
  });

  await check('TR UI switch localizes tabs and notes', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    const btn = await page.locator('#gamesOpen').textContent();
    if (btn !== 'Oyunlar') throw new Error('games btn=' + btn);
    await page.locator('.word', { hasText: 'إِنَّ' }).first().click();
    await page.locator('.sheet .tabs button', { hasText: 'Gramer' }).click();
    await page.waitForSelector('.mistake', { timeout: 3000 });
    const why = await page.locator('.mistake .why').first().textContent();
    if (!/[çğışüö]|mansub|merfu|ötre/i.test(why)) throw new Error('why not Turkish: ' + why.slice(0, 60));
  });

  await check('back to library shows reading progress', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const w = await page.locator('.lib-card .progress > div').first().getAttribute('style');
    if (!w || /width:\s*0%/.test(w)) throw new Error('no progress: ' + w);
  });

  await check('no JS errors on page', async () => {
    if (errors.length) throw new Error(errors.join(' | '));
  });

  // hadith reader quick check
  const page2 = await browser.newPage();
  const errors2 = [];
  page2.on('pageerror', e => errors2.push(e.message));
  await page2.goto('file://' + require('path').resolve(__dirname, '..') + '/content/user-uploads/deeds-are-by-intentions/reader.html');
  await check('hadith reader: innama opens global note', async () => {
    await page2.locator('.word', { hasText: 'إِنَّمَا' }).first().click();
    await page2.waitForSelector('.sheet.show', { timeout: 3000 });
    await page2.locator('.sheet .tabs button', { hasText: 'Grammar' }).click();
    const h = await page2.locator('.gnote h3').first().textContent();
    if (!h.includes('الْكَافَّة')) throw new Error('note title: ' + h);
    if (errors2.length) throw new Error(errors2.join(' | '));
  });

  await browser.close();
})();
