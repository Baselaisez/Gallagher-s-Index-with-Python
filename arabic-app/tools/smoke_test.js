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
  // Pin to the L2 package by id — the L4 sibling shares the same Arabic title,
  // so a title substring would match two library cards.
  const wasiyyaStats = await page.evaluate(() => {
    const i = STORIES.findIndex(s => s.id === 'wasiyyat-abi-hanifa-L2');
    if (i === -1) return null;
    const s = STORIES[i];
    return {
      index: i,
      chapters: s.chapters.length,
      sentences: s.chapters.reduce((n, c) => n + c.sentences.length, 0),
    };
  });
  if (!wasiyyaStats) throw new Error('could not find wasiyyat-abi-hanifa-L2 in STORIES to derive expectations');

  await check('library lists ' + storyCount + ' stories, reader controls hidden', async () => {
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const cardCount = await page.locator('.lib-card').count();
    if (cardCount !== storyCount) throw new Error('cards=' + cardCount + ' expected=' + storyCount);
    if (await page.locator('#gamesOpen').isVisible()) throw new Error('reader controls visible in library');
  });

  await check('open story renders ' + wasiyyaStats.chapters + ' chapters', async () => {
    await page.locator('.lib-card').nth(wasiyyaStats.index).click();
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
    // fire onend/onerror almost immediately, very slowly, or never. On CI's
    // Chrome-for-Testing the instant-error path let the play-all queue race
    // through the whole story and auto-stop BEFORE our second click, which
    // then restarted playback and failed the "stops cleanly" assertion.
    // Freeze TTS entirely: with speak() stubbed out no utterance event ever
    // fires, so the queue deterministically stays on its first sentence and
    // both clicks exercise exactly the start/stop state machine.
    await page.keyboard.press('Escape');
    await page.evaluate(() => {
      speechSynthesis.speak = () => {};
      speechSynthesis.cancel = () => {};
    });
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

  await check('grammar reference: search box and level filter narrow the list', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#refOpen').click();
    await page.waitForSelector('.ref-list', { timeout: 3000 });

    const unfilteredCount = await page.locator('.ref-list li').count();
    const totalNotes = await page.evaluate(() => Object.keys(GRAMMAR).length);
    if (unfilteredCount !== totalNotes) {
      throw new Error('unfiltered ref list=' + unfilteredCount + ' expected=' + totalNotes);
    }

    // Pick a query guaranteed to hit at least one note (its own English title),
    // but not necessarily all of them — derived from page data, not hardcoded.
    const sampleTitle = await page.evaluate(() => Object.values(GRAMMAR)[0].title.en);
    const queryWord = sampleTitle.split(/\s+/)[0];
    await page.locator('#refSearch').fill(queryWord);
    const searchedCount = await page.locator('.ref-list li').count();
    if (searchedCount < 1) throw new Error('search for "' + queryWord + '" matched nothing');
    if (searchedCount >= unfilteredCount) {
      throw new Error('search did not narrow the list: ' + searchedCount + ' >= ' + unfilteredCount);
    }

    // Clear the search, then apply a level filter and confirm the list changes
    // to exactly the notes at that level (derived from GRAMMAR, not hardcoded).
    await page.locator('#refSearch').fill('');
    const clearedCount = await page.locator('.ref-list li').count();
    if (clearedCount !== unfilteredCount) throw new Error('clearing search did not restore full list: ' + clearedCount);

    const level = await page.evaluate(() => {
      const levels = [...new Set(Object.values(GRAMMAR).map(g => g.level).filter(Boolean))];
      return levels.sort((a, b) => a - b)[0];
    });
    const expectedForLevel = await page.evaluate(lvl =>
      Object.values(GRAMMAR).filter(g => g.level === lvl).length, level);
    await page.locator('#refLevels [data-level="' + level + '"]').click();
    const leveledCount = await page.locator('.ref-list li').count();
    if (leveledCount !== expectedForLevel) {
      throw new Error('level ' + level + ' filter=' + leveledCount + ' expected=' + expectedForLevel);
    }
    if (leveledCount === unfilteredCount) throw new Error('level filter did not change the list');

    // A query with no plausible match should show the localized empty state.
    await page.locator('#refLevels [data-level="all"]').click();
    await page.locator('#refSearch').fill('zzzzznonexistentzzzzz');
    await page.waitForSelector('.ref-empty', { timeout: 3000 });
    if (await page.locator('.ref-list li').count() !== 0) throw new Error('expected zero results for nonsense query');
  });

  await check('back to library shows reading progress', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const w = await page.locator('.lib-card').nth(wasiyyaStats.index)
      .locator('.progress > div').getAttribute('style');
    if (!w || /width:\s*0%/.test(w)) throw new Error('no progress: ' + w);
  });

  await check('premium L4: paywall preview then unlock', async () => {
    // The TR-UI check left the app in Turkish; this check asserts English tab labels.
    await page.locator('#uiLangSeg [data-ui="en"]').click();
    const l4 = await page.evaluate(() => {
      const i = STORIES.findIndex(s => s.id === 'wasiyyat-abi-hanifa-L4');
      if (i === -1) return null;
      const s = STORIES[i];
      return { index: i, access: s.access,
               sentences: s.chapters.reduce((n, c) => n + c.sentences.length, 0) };
    });
    if (!l4) throw new Error('wasiyyat-abi-hanifa-L4 missing from STORIES');
    if (l4.access !== 'premium') throw new Error('access=' + l4.access);
    const card = page.locator('.lib-card').nth(l4.index);
    const chips = await card.locator('.chip').allTextContents();
    if (!chips.some(c => c.includes('Premium'))) throw new Error('no Premium chip: ' + chips.join(','));
    await card.click();
    // Locked: only the preview renders, then the upsell card. The Play-all
    // queue is built from the rendered sentences, so audio is gated too.
    const previewCount = await page.locator('.sentence').count();
    if (previewCount >= l4.sentences) throw new Error('paywall did not limit render: ' + previewCount);
    await page.waitForSelector('.upsell', { timeout: 3000 });
    await page.locator('#unlockPremium').click();
    await page.waitForSelector('.upsell', { state: 'detached', timeout: 3000 });
    const fullCount = await page.locator('.sentence').count();
    if (fullCount !== l4.sentences) throw new Error('unlock rendered ' + fullCount + '/' + l4.sentences);
  });

  await check('premium L4 sibling: hal note, sarf table, level switcher', async () => {
    // مُوَدِّعًا carries the hal note — a Level-4 structure shared via the registry.
    await page.locator('.word', { hasText: 'مُوَدِّعًا' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Grammar' }).click();
    const notes = await page.locator('.gnote h3').allTextContents();
    if (!notes.some(t => t.includes('الْحَال'))) throw new Error('hal note not shown: ' + notes.join(','));
    // Form III conjugation table for جَادَلَ must render from the new morphology.
    await page.keyboard.press('Escape');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('.word', { hasText: 'تُجَادِلْ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    // sarfTense persists from the earlier amr check — select mazi explicitly.
    await page.waitForSelector('table.conj', { timeout: 3000 });
    await page.locator('.tense-seg button', { hasText: 'الماضي' }).click();
    await page.waitForSelector('table.conj', { timeout: 3000 });
    const cells = await page.locator('table.conj td').allTextContents();
    if (!cells.some(c => c.includes('جَادَلْتُمَا'))) throw new Error('Form III paradigm missing');
    await page.evaluate(() => document.getElementById('scrim').click());
    // Level switcher: the L4 story links to its Level-2 sibling in the same storyGroup.
    await page.locator('#metaRow .sib').first().click();
    const levelChip = await page.locator('#metaRow .chip.level').first().textContent();
    if (!levelChip.includes('Level 2')) throw new Error('sibling switch landed on: ' + levelChip);
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    // Reset the demo-premium flag so the library check state stays clean.
    await page.locator('#premiumReset').click();
    if (await page.locator('#premiumReset').count()) throw new Error('premium reset chip still shown');
  });

  await check('ashab-al-fil story: mithal amr + word pronounce button', async () => {
    const fil = await page.evaluate(() => {
      const i = STORIES.findIndex(s => s.id === 'ashab-al-fil');
      return i === -1 ? null : { index: i, level: STORIES[i].level };
    });
    if (!fil) throw new Error('ashab-al-fil missing from STORIES');
    if (fil.level !== 1) throw new Error('level=' + fil.level);
    await page.locator('.lib-card').nth(fil.index).click();
    // وَقَفَ is a mithal verb — its amr paradigm must show the waw-dropping قِفْ.
    await page.locator('.word', { hasText: 'وَقَفَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    await page.waitForSelector('table.conj', { timeout: 3000 });
    await page.locator('.tense-seg button', { hasText: 'الأمر' }).click();
    await page.waitForSelector('table.conj', { timeout: 3000 });
    const cells = await page.locator('table.conj td').allTextContents();
    if (!cells.some(c => c.trim() === 'قِفْ')) throw new Error('mithal amr قِفْ missing');
    // The Word tab has the 🔊 pronounce button; clicking must not throw.
    await page.locator('.sheet .tabs button', { hasText: 'Word' }).click();
    await page.waitForSelector('#sayWord', { timeout: 3000 });
    await page.evaluate(() => { speechSynthesis.speak = () => {}; speechSynthesis.cancel = () => {}; });
    await page.locator('#sayWord').click();
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('classical L5 (Abu Yusuf): premium, tahdhir note in preview', async () => {
    const l5 = await page.evaluate(() => {
      const i = STORIES.findIndex(s => s.id === 'wasiyyat-abi-yusuf-L5');
      if (i === -1) return null;
      return { index: i, level: STORIES[i].level, access: STORIES[i].access,
               hasTahdhir: !!GRAMMAR['at-tahdhir'], hasVI: !!GRAMMAR['form-vi-verbs'] };
    });
    if (!l5) throw new Error('wasiyyat-abi-yusuf-L5 missing from STORIES');
    if (l5.level !== 5) throw new Error('level=' + l5.level);
    if (l5.access !== 'premium') throw new Error('access=' + l5.access);
    if (!l5.hasTahdhir || !l5.hasVI) throw new Error('new grammar notes missing from registry');
    await page.locator('.lib-card').nth(l5.index).click();
    // s2 «وَإِيَّاكَ وَالْكَذِبَ» sits inside the free preview — no unlock needed.
    // Tapping إِيَّاكَ opens the shared at-tahdhir note.
    await page.locator('.word', { hasText: 'إِيَّاك' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Grammar' }).click();
    const notes = await page.locator('.gnote h3').allTextContents();
    if (!notes.some(t => t.includes('التَّحْذِير'))) throw new Error('tahdhir note not shown: ' + notes.join(','));
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
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
