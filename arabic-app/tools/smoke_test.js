// Qissa reader smoke test — drives both built readers in headless Chromium.
// Usage: npm i playwright-core && node tools/smoke_test.js
// Override the browser binary with CHROMIUM_PATH if needed.
const fs = require('node:fs');
const path = require('node:path');
const { pathToFileURL } = require('node:url');
const { chromium } = require('playwright-core');

// Resolve a real Chrome/Chromium binary. playwright-core ships no bundled
// browser, so we must point executablePath at a system install. Checked in
// order: CHROMIUM_PATH override, then common per-OS install locations.
function findChrome() {
  const candidates = [];
  if (process.env.CHROMIUM_PATH) candidates.push(process.env.CHROMIUM_PATH);

  if (process.platform === 'win32') {
    candidates.push('C:/Program Files/Google/Chrome/Application/chrome.exe');
    candidates.push('C:/Program Files (x86)/Google/Chrome/Application/chrome.exe');
    if (process.env.LOCALAPPDATA) {
      candidates.push(path.join(process.env.LOCALAPPDATA, 'Google/Chrome/Application/chrome.exe'));
    }
  } else if (process.platform === 'darwin') {
    candidates.push('/Applications/Google Chrome.app/Contents/MacOS/Google Chrome');
  } else {
    candidates.push('/opt/pw-browsers/chromium-1194/chrome-linux/chrome');
    candidates.push('/usr/bin/google-chrome');
    candidates.push('/usr/bin/chromium');
  }

  return candidates.find(c => c && fs.existsSync(c)) || null;
}

const CHROME = findChrome();
if (!CHROME) {
  console.error(
    'ERROR: no Chrome/Chromium binary found. Set CHROMIUM_PATH to a Chrome ' +
    'executable (e.g. CHROMIUM_PATH="C:/Program Files/Google/Chrome/Application/chrome.exe").'
  );
  process.exit(1);
}

(async () => {
  const browser = await chromium.launch({ executablePath: CHROME });
  const page = await browser.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push('pageerror: ' + e.message));
  page.on('console', m => { if (m.type() === 'error') errors.push('console: ' + m.text()); });

  const url = pathToFileURL(path.resolve(__dirname, '..', 'prototype/reader.html')).href;
  await page.goto(url);
  const check = async (name, fn) => {
    try { await fn(); console.log('PASS', name); }
    catch (e) { console.log('FAIL', name, '—', e.message.split('\n')[0]); process.exitCode = 1; }
  };

  // Data-driven expectations, derived from the page's own STORIES global
  // (see tools/build_prototype.py) instead of hardcoded magic numbers, so
  // the test survives content additions.
  const storyCount = await page.evaluate(() => STORIES.length);
  const wasiyyaStats = await page.evaluate(() => {
    const s = STORIES.find(s => s.title.ar.includes('وَصِيَّةُ'));
    if (!s) return null;
    return {
      chapters: s.chapters.length,
      sentences: s.chapters.reduce((n, c) => n + c.sentences.length, 0),
    };
  });
  if (!wasiyyaStats) throw new Error('could not find the وَصِيَّةُ story in STORIES to derive expectations');

  await check('library lists ' + storyCount + ' stories, reader controls hidden', async () => {
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const cardCount = await page.locator('.lib-card').count();
    if (cardCount !== storyCount) throw new Error('cards=' + cardCount + ' expected=' + storyCount);
    if (await page.locator('#gamesOpen').isVisible()) throw new Error('reader controls visible in library');
  });

  await check('open story renders ' + wasiyyaStats.chapters + ' chapters', async () => {
    await page.locator('.lib-card', { hasText: 'وَصِيَّةُ' }).click();
    const chapterCount = await page.locator('.chapter-head').count();
    if (chapterCount !== wasiyyaStats.chapters) throw new Error('chapter count=' + chapterCount + ' expected=' + wasiyyaStats.chapters);
    const sentenceCount = await page.locator('.sentence').count();
    if (sentenceCount !== wasiyyaStats.sentences) throw new Error('sentence count=' + sentenceCount + ' expected=' + wasiyyaStats.sentences);
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

  await check('deck gloss follows TR UI language (bilingual deck cards)', async () => {
    // The card saved earlier (test 6) was saved while the UI was English —
    // toggleSave() must have snapshotted BOTH glosses on the card, not just
    // English, or a language switch afterwards can't recover the Turkish one.
    await page.keyboard.press('Escape');
    await page.locator('#deckOpen').click();
    await page.waitForSelector('.deck-list .g', { timeout: 3000 });
    const result = await page.evaluate(() => {
      const card = state.deck[0];
      return {
        shown: document.querySelector('.deck-list .g').textContent,
        tr: card && card.gloss && card.gloss.tr,
        en: card && card.gloss && card.gloss.en,
      };
    });
    if (!result.tr) throw new Error('saved card has no gloss.tr: ' + JSON.stringify(result));
    if (result.shown !== result.tr) throw new Error('deck gloss shown="' + result.shown + '" expected tr="' + result.tr + '"');
    if (result.tr === result.en) throw new Error('tr gloss equals en gloss — test cannot prove localization: ' + result.tr);
    await page.keyboard.press('Escape');
  });

  await check('audiobook: Play all highlights a sentence and stops cleanly', async () => {
    // Headless Chromium ships no TTS voices, so speechSynthesis.speak() may
    // fire onend/onerror almost immediately, very slowly, or never produce
    // audible sound. The app applies the .playing highlight and the
    // aria-pressed state SYNCHRONOUSLY inside the click handler, before the
    // (inherently async) speechSynthesis.speak() call — so asserting right
    // after click(), with no polling/timeout, is race-free regardless of TTS
    // behavior in this environment.
    await page.keyboard.press('Escape');
    await page.locator('#playAll').click();
    const playingCount = await page.locator('.sentence.playing').count();
    if (playingCount !== 1) throw new Error('expected exactly one playing sentence right after click, got ' + playingCount);
    const pressed = await page.locator('#playAll').getAttribute('aria-pressed');
    if (pressed !== 'true') throw new Error('playAll aria-pressed=' + pressed);

    await page.locator('#playAll').click(); // stop
    const playingAfter = await page.locator('.sentence.playing').count();
    if (playingAfter !== 0) throw new Error('expected no playing sentence after stop, got ' + playingAfter);
    const pressedAfter = await page.locator('#playAll').getAttribute('aria-pressed');
    if (pressedAfter !== 'false') throw new Error('playAll aria-pressed after stop=' + pressedAfter);
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
  const url2 = pathToFileURL(path.resolve(__dirname, '..', 'content/user-uploads/deeds-are-by-intentions/reader.html')).href;
  await page2.goto(url2);
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
