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
  // The first-run level picker has its own fresh-context check below; the main
  // page runs as a returning reader so its sheet cannot sit over every other check.
  await page.addInitScript(() => localStorage.setItem('qissa-welcomed', '1'));
  await page.goto(url);
  const check = async (name, fn) => {
    try { await fn(); console.log('PASS', name); }
    catch (e) { console.log('FAIL', name, '—', e.message.split('\n')[0]); process.exitCode = 1; }
  };

  // Select a library card by the story it holds, never by position: the library
  // sorts (by level, or newest-first), so a card's index is not its place in
  // STORIES. reader.html stamps data-story-id for exactly this.
  const storyCard = id => page.locator('.lib-card[data-story-id="' + id + '"]');
  // Get back to the library from wherever the previous check left off, so a
  // check that fails part-way cannot cascade into the next one.
  const toLibrary = async () => {
    await page.evaluate(() => document.getElementById('scrim').click());
    if (await page.locator('#backLib').isVisible().catch(() => false)) {
      await page.locator('#backLib').click();
    }
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  };
  const openStoryCard = async id => {
    if (!(await storyCard(id).count())) await toLibrary();
    const card = storyCard(id);
    if (!(await card.count())) throw new Error(id + ' is not in the library');
    await card.click();
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
      id: s.id,
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
    await openStoryCard(wasiyyaStats.id);
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

  await check('SRS review: four grades, SM-2 intervals, deck stats', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#deckOpen').click();
    // Stats row is present before any review.
    await page.waitForSelector('.deck-stats .fresh', { timeout: 3000 });
    await page.locator('#reviewCard').click();
    await page.locator('#reviewCard').click();
    // All four SM-2 grades, each showing the interval it would schedule.
    const grades = await page.locator('.grade-row .grade').count();
    if (grades !== 4) throw new Error('expected 4 grade buttons, got ' + grades);
    const previews = await page.locator('.grade-row .grade i').allTextContents();
    if (!previews.every(t => t.trim())) throw new Error('a grade button has no interval preview');
    if (previews[0] !== '10m') throw new Error('Again should schedule 10m, got ' + previews[0]);
    await page.locator('.grade-row .grade[data-q="good"]').click();
    const txt = await page.locator('.empty').textContent();
    if (!txt.includes('Next review')) throw new Error('no next-review text: ' + txt);
    if (!(await page.locator('#deckCount').isHidden())) throw new Error('badge should hide when nothing due');
    // A card graded Good from new is due in a day, not ten minutes.
    const ivl = await page.evaluate(() => state.deck[0].srs.ivl);
    if (ivl !== 1) throw new Error('first Good should give ivl=1, got ' + ivl);
  });

  await check('games: spot-the-error round works', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#gamesOpen').click();
    await page.locator('#gSpot').click();
    await page.waitForSelector('.opts button', { timeout: 3000 });
    await page.locator('.opts button').first().click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    await page.waitForSelector('.opts button.right', { timeout: 3000 });
    await page.locator('#qNext').click();
    await page.waitForSelector('.opts button:not([disabled])', { timeout: 3000 });
  });

  await check('games: harakat round shows i\'rab explanation', async () => {
    await page.locator('#gBack').click();
    await page.locator('#gHarakat').click();
    await page.waitForSelector('.game-q', { timeout: 3000 });
    await page.locator('.opts button').first().click();
    await page.waitForSelector('#qWhy .game-why', { timeout: 3000 });
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
    // Skip stopword-length openers ("The five verbs…") — a query of "The"
    // matches every English title and narrows nothing.
    const queryWord = sampleTitle.split(/\s+/).find(w => w.length >= 5) ||
      sampleTitle.split(/\s+/)[0];
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
    const w = await storyCard(wasiyyaStats.id)
      .locator('.progress > div').getAttribute('style');
    if (!w || /width:\s*0%/.test(w)) throw new Error('no progress: ' + w);
  });

  await check('Lite tier: a free set that rotates with the week', async () => {
    await page.locator('#uiLangSeg [data-ui="en"]').click();
    await page.evaluate(() => { setPremium(false); renderLibrary(); });
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const info = await page.evaluate(() => {
      const sorted = s => [...s].sort();
      const setOf = d => sorted(rotatingFree(d));
      const now = new Date();
      const day = DAY_MS;
      const prem = premiumIds();
      // Step a week at a time: the window slides by its own width, so every
      // premium story must come round within one lap of the catalogue.
      const covered = new Set();
      for (let i = 0; i < prem.length; i++)
        setOf(new Date(now.getTime() + i * 7 * day)).forEach(id => covered.add(id));
      const tomorrow = new Date(now.getTime() + day);
      return {
        prem,
        now: setOf(now),
        again: setOf(now),                                   // purity
        tomorrow: setOf(tomorrow),
        rolled: weekIndex(tomorrow) !== weekIndex(now),
        next: setOf(new Date(now.getTime() + 7 * day)),
        covered: [...covered].sort(),
        unlocked: STORIES.filter(s => s.access === 'premium' && !storyLocked(s)).map(s => s.id).sort(),
      };
    });
    const want = Math.min(2, info.prem.length);
    if (info.now.length !== want) throw new Error('free set size ' + info.now.length + ' expected ' + want);
    if (info.now.some(id => !info.prem.includes(id))) throw new Error('non-premium in free set: ' + info.now);
    if (String(info.again) !== String(info.now)) throw new Error('rotation is not a pure function of the date');
    // Within a week it must not move; across the boundary it must.
    if (!info.rolled && String(info.tomorrow) !== String(info.now))
      throw new Error('free set changed inside one week: ' + info.now + ' -> ' + info.tomorrow);
    if (info.next.some(id => info.now.includes(id)))
      throw new Error('next week repeats this week: ' + info.now + ' / ' + info.next);
    if (String(info.covered) !== String(info.prem))
      throw new Error('rotation never reaches: ' + info.prem.filter(i => !info.covered.includes(i)));
    // storyLocked must agree with the rotation — the badge and the paywall
    // cannot disagree about the same story.
    if (String(info.unlocked) !== String(info.now))
      throw new Error('unlocked ' + info.unlocked + ' but free set is ' + info.now);

    // A rotated story opens in full — it is free, not a longer preview.
    const card = storyCard(info.now[0]);
    const chips = await card.locator('.chip').allTextContents();
    if (!chips.some(c => /Free this week/.test(c))) throw new Error('no rotation badge: ' + chips.join(','));
    await card.click();
    const shown = await page.locator('.sentence').count();
    const total = await page.evaluate(id => STORIES.find(s => s.id === id)
      .chapters.reduce((n, c) => n + c.sentences.length, 0), info.now[0]);
    if (shown !== total) throw new Error('rotated story truncated: ' + shown + '/' + total);
    if (await page.locator('.upsell').count()) throw new Error('rotated story showed the upsell');
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('premium: paywall preview then unlock', async () => {
    // Whichever premium stories are free this week, four of the six are not.
    const l4 = await page.evaluate(() => {
      const i = STORIES.findIndex(s => s.access === 'premium' && storyLocked(s));
      if (i === -1) return null;
      const s = STORIES[i];
      return { index: i, id: s.id, access: s.access,
               sentences: s.chapters.reduce((n, c) => n + c.sentences.length, 0) };
    });
    if (!l4) throw new Error('no locked premium story to test the paywall with');
    if (l4.access !== 'premium') throw new Error('access=' + l4.access);
    const card = storyCard(l4.id);
    const chips = await card.locator('.chip').allTextContents();
    if (!chips.some(c => c.includes('Premium'))) throw new Error('no Premium chip: ' + chips.join(','));
    if (chips.some(c => /Free this week/.test(c))) throw new Error('locked story badged free: ' + l4.id);
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
    // Premium is unlocked by the check above, so L4 renders in full whether or
    // not this week's rotation happens to include it.
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const card4 = page.locator('.lib-card[data-story-id="wasiyyat-abi-hanifa-L4"]');
    if (!(await card4.count())) throw new Error('wasiyyat-abi-hanifa-L4 missing from the library');
    await card4.click();
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
    await openStoryCard('ashab-al-fil');
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
    await openStoryCard('wasiyyat-abi-yusuf-L5');
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

  await check('idiom: بَيْنَ يَدَيْهِ reads as one unit without losing each word\'s i\'rab', async () => {
    // The two words keep their own analysis (mansub zarf + mudaf ilayh); the
    // banner adds what they mean *together*. Both layers must survive.
    await openStoryCard('wasiyyat-abi-yusuf-L5');
    const tinted = await page.locator('.sentence .word.in-phrase').count();
    if (tinted < 2) throw new Error('phrase span not tinted in the text: ' + tinted);
    await page.locator('.sentence .word', { hasText: 'بَيْنَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    const gloss = await page.locator('.phrase-banner .pb-gloss').first().textContent();
    if (!/in his presence/i.test(gloss)) throw new Error('idiom gloss missing: ' + gloss);
    const lit = await page.locator('.phrase-banner .pb-lit').first().textContent();
    if (!/between his two hands/i.test(lit)) throw new Error('literal reading missing: ' + lit);
    // ...and the word's own i'rab is still there, unchanged.
    await page.locator('.sheet .tabs button[data-tab="irab"]').click();
    const irab = await page.locator('.irab-en').first().textContent();
    if (!irab.trim()) throw new Error('i\'rab lost under the idiom banner');
    if (!(await page.locator('.phrase-banner').count()))
      throw new Error('idiom banner should persist across tabs');
    // TR UI must show the Turkish idiom, not fall back to English.
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    await page.locator('.sentence .word', { hasText: 'بَيْنَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    const trGloss = await page.locator('.phrase-banner .pb-gloss').first().textContent();
    if (!/huzurunda/.test(trGloss)) throw new Error('idiom not Turkish under TR UI: ' + trGloss);
    // A word outside any idiom must not inherit the previous banner.
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('.sentence .word:not(.in-phrase)').first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    if (await page.locator('.phrase-banner').count())
      throw new Error('stale idiom banner shown on a word outside the span');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="en"]').click();
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check("i'rab tab is Turkish when TR UI is selected", async () => {
    // Regression guard: i'rab notes used to fall back to English under TR UI
    // because the token data only carried {ar, en}. Turkish now comes from the
    // shared translation memory (content/i18n/irab-tr.json) merged in at build.
    const coverage = await page.evaluate(() => {
      let total = 0, withTr = 0;
      for (const st of STORIES)
        for (const c of st.chapters)
          for (const s of c.sentences)
            for (const t of s.tokens)
              if (t.irab && t.irab.en) { total++; if (t.irab.tr) withTr++; }
      return { total, withTr };
    });
    if (coverage.withTr !== coverage.total) {
      throw new Error(`i'rab tr coverage ${coverage.withTr}/${coverage.total}`);
    }
    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const firstId = await page.locator('.lib-card').first().getAttribute('data-story-id');
    await page.locator('.lib-card').first().click();
    await page.locator('.sentence .word').first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: "İ'rab" }).click();
    const shown = await page.locator('.irab-en').first().textContent();
    const expected = await page.evaluate(id => {
      const t = STORIES.find(s => s.id === id).chapters[0].sentences[0].tokens[0];
      return { tr: t.irab.tr, en: t.irab.en };
    }, firstId);
    if (shown.trim() !== expected.tr.trim()) {
      throw new Error(`i'rab under TR UI showed "${shown}" (expected the Turkish "${expected.tr}")`);
    }
    if (shown.trim() === expected.en.trim()) throw new Error('i\'rab still English under TR UI');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="en"]').click();
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('Emsile-i Muhtelife: 14 forms, hollow jussive shortens', async () => {
    // Every verb in the corpus must carry the three governed forms the
    // muhtelife needs — they are stored, not derived, precisely because weak
    // verbs break the sound-verb rule.
    const missing = await page.evaluate(() => {
      const out = [];
      for (const st of STORIES)
        for (const [lex, m] of Object.entries(st.morph || {}))
          // A jamid verb (لَيْسَ) has no mudari at all, hence no governed
          // forms — that is doctrine, not missing data.
          if (!m.jamid && (!m.mansub || !m.majzum || !m.majzum2)) out.push(st.id + ':' + lex);
      return out;
    });
    if (missing.length) throw new Error('verbs without governed forms: ' + missing.join(', '));

    await openStoryCard('wasiyyat-abi-hanifa-L2');
    await page.locator('.word', { hasText: 'أَرَادَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    await page.locator('.tense-seg button', { hasText: 'المُخْتَلِفَة' }).click();
    await page.waitForSelector('table.conj.muhtelife', { timeout: 3000 });
    const forms = await page.locator('table.conj.muhtelife tr:not(.majhul) td').allTextContents();
    if (forms.length !== 14) throw new Error('expected 14 active forms, got ' + forms.length);
    // أَرَادَ is Form IV hollow: the jussive must shorten (لَمْ يُرِدْ), and the
    // naive damma->sukun derivation (لَمْ يُرِيدْ) must never appear.
    if (!forms.some(f => f.includes('لَمْ يُرِدْ'))) throw new Error('hollow jussive wrong: ' + forms.join(' / '));
    if (forms.some(f => f.includes('يُرِيدْ'))) throw new Error('naive derived jussive leaked into the table');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('passive (majhul): rows render, hollow takes kasra, none invented', async () => {
    // Intransitive verbs must carry NO passive rather than a derived guess.
    const bad = await page.evaluate(() => {
      const out = [];
      for (const st of STORIES)
        for (const [lex, m] of Object.entries(st.morph || {})) {
          if ((m.majhulMazi && !m.majhulMudari) || (!m.majhulMazi && m.majhulMudari))
            out.push(st.id + ':' + lex + ' half-passive');
        }
      return out;
    });
    if (bad.length) throw new Error(bad.join(', '));

    await page.evaluate(() => document.getElementById('scrim').click());
    if (!(await page.locator('.lib-card').first().isVisible().catch(() => false))) {
      await page.locator('#backLib').click();
      await page.waitForSelector('.lib-card', { timeout: 3000 });
    }
    await openStoryCard('wasiyyat-abi-hanifa-L2');
    await page.locator('.word', { hasText: 'قَالَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    await page.locator('.tense-seg button', { hasText: 'المُخْتَلِفَة' }).click();
    await page.waitForSelector('table.conj.muhtelife', { timeout: 3000 });
    const maj = await page.locator('table.conj.muhtelife tr.majhul td').allTextContents();
    if (maj.length !== 2) throw new Error('expected 2 passive rows, got ' + maj.length);
    // قَالَ is hollow: the passive takes kasra and a ي (قِيلَ), never *قُولَ.
    if (!maj[0].includes('قِيلَ')) throw new Error('hollow passive wrong: ' + maj.join('/'));
    if (maj.some(f => f.includes('قُولَ'))) throw new Error('derived-but-wrong hollow passive leaked');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('conjugation cards and the two new games', async () => {
    await page.evaluate(() => document.getElementById('scrim').click());
    if (!(await page.locator('.lib-card').first().isVisible().catch(() => false))) {
      await page.locator('#backLib').click();
      await page.waitForSelector('.lib-card', { timeout: 3000 });
    }
    await openStoryCard('wasiyyat-abi-hanifa-L2');

    // Saving a verb creates a conjugation card, distinct from a meaning card.
    await page.locator('.word', { hasText: 'أَرَادَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    await page.locator('#saveConjBtn').click();
    const verbCards = await page.evaluate(() => state.deck.filter(c => c.type === 'verb').length);
    if (verbCards !== 1) throw new Error('expected 1 verb card, got ' + verbCards);
    // It must ask for a sigha, not a gloss.
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#deckOpen').click();
    await page.locator('#reviewCard').click();
    await page.locator('#reviewCard').click();
    if (!(await page.locator('.verb-answer').count())) throw new Error('verb card did not show a conjugated form');
    // The drill asks several cells in one round — three distinct questions,
    // three distinct answers, every answer a real cell of this verb's own
    // paradigm (the müderris asks the sigha in one breath, not one per day).
    const drill = await page.evaluate(() => ({
      asks: [...document.querySelectorAll('#reviewCard .verb-ask')].map(x => x.textContent),
      answers: [...document.querySelectorAll('#reviewCard .verb-answer')].map(x => x.textContent),
    }));
    if (drill.asks.length !== 3 || drill.answers.length !== 3)
      throw new Error('drill shows ' + drill.asks.length + ' asks / ' + drill.answers.length + ' answers, expected 3+3');
    if (new Set(drill.answers).size !== 3) throw new Error('the drill repeated a paradigm cell');
    const legit = await page.evaluate(ans => {
      const card = state.deck.find(c => c.type === 'verb');
      const rows = muhtelife(MORPH[card.lex]);
      return ans.every(a => rows.some(r => r.ar === a));
    }, drill.answers);
    if (!legit) throw new Error('a drill answer is not a cell of the paradigm');

    // Sarf drill: distractors come from the same verb's own paradigm.
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#gamesOpen').click();
    await page.locator('#gSarf').click();
    await page.waitForSelector('.game-q .sigha', { timeout: 3000 });
    if (await page.locator('.opts button').count() < 2) throw new Error('sarf drill has too few options');
    await page.locator('.opts button').first().click();
    await page.waitForSelector('.opts button.right', { timeout: 3000 });

    // Which-case drill, answered from the token's own i'rab.
    await page.locator('#gBack').click();
    await page.locator('#gCase').click();
    await page.waitForSelector('.game-q .target', { timeout: 3000 });
    const caseOpts = await page.locator('.opts [data-o]').count();
    if (caseOpts !== 4) throw new Error('expected 4 case options, got ' + caseOpts);
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('.opts .right', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('reading modes: easy translates, medium glosses each word, hard hides both', async () => {
    await page.locator('.lib-card').first().click();
    const first = page.locator('.sentence').first();

    await page.locator('#modeSeg [data-mode="easy"]').click();
    const easyTr = (await first.locator('.trans').textContent()).trim();
    if (!easyTr) throw new Error('easy mode shows no sentence translation');
    if (await first.locator('.word.stacked').count()) throw new Error('easy mode should not gloss words');
    if (await first.locator('.peek').count()) throw new Error('nothing to peek at in easy mode');

    await page.locator('#modeSeg [data-mode="medium"]').click();
    if ((await first.locator('.trans').textContent()).trim())
      throw new Error('medium mode still shows the sentence translation');
    const glossed = await first.locator('.word.stacked .w-gl:not(:empty)').count();
    if (glossed < 2) throw new Error('medium mode glossed only ' + glossed + ' words');
    // proper nouns are deliberately left bare
    const bare = await page.evaluate(() => {
      const sen = CHAPTERS[0].sentences[0];
      return sen.tokens.filter(t => { const e = GLOSSARY[t.lex]; return e && e.level === 0; }).length;
    });
    const empties = await first.locator('.word.stacked .w-gl:empty').count();
    if (empties !== bare) throw new Error(`${empties} bare glosses, ${bare} level-0 words`);

    await page.locator('#modeSeg [data-mode="hard"]').click();
    if ((await first.locator('.trans').textContent()).trim())
      throw new Error('hard mode still shows the sentence translation');
    if (await first.locator('.word.stacked').count()) throw new Error('hard mode should not gloss words');
    // ...but a word still opens on tap, and one sentence can be peeked at
    await first.locator('.word').first().click();
    await page.waitForSelector('.sheet.show .gloss', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());
    await first.locator('.peek').click();
    if ((await first.locator('.trans').textContent()).trim() !== easyTr)
      throw new Error('peek did not reveal the same translation easy mode shows');
    if (await first.locator('.peek').count()) throw new Error('peek button should go once used');

    // the mode survives a reload and localizes with the UI
    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    const label = await page.locator('#modeSeg [data-mode="hard"] .m-en').textContent();
    if (label !== 'Zor') throw new Error('mode label not Turkish under TR UI: ' + label);
    await page.locator('#uiLangSeg [data-ui="en"]').click();
    await page.locator('#modeSeg [data-mode="easy"]').click();
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('games: role game asks the role, and its pool holds only nominals', async () => {
    // The pool is derived by regex from the Arabic i'rab, so it is exactly the
    // kind of thing that silently goes wrong. Guard the invariant, not the UI:
    // a verb or particle whose i'rab merely NAMES a role must never be an item.
    const pool = await page.evaluate(() => {
      const items = roleItems();
      const nonNominal = items.filter(i => !['noun', 'propn', 'pron', 'adv'].includes(i.tok.pos));
      const keys = {};
      items.forEach(i => keys[i.key] = (keys[i.key] || 0) + 1);
      return { n: items.length, nonNominal: nonNominal.length, kinds: Object.keys(keys).length };
    });
    if (pool.nonNominal) throw new Error(pool.nonNominal + ' non-nominal tokens in the role pool');
    if (pool.n < 50) throw new Error('role pool too small: ' + pool.n);
    if (pool.kinds < 5) throw new Error('role pool covers only ' + pool.kinds + ' roles');
    await page.locator('.lib-card').first().click();   // Games is a reader-only control
    await page.locator('#gamesOpen').click();
    await page.locator('.game-pick #gRole').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 3000 });
    const opts = await page.locator('.opts [data-o]').count();
    if (opts !== 4) throw new Error('expected 4 options, got ' + opts);
    if (!(await page.locator('.game-q .target').count())) throw new Error('no word highlighted');
    await page.locator('.opts [data-o]').first().click();
    if (!(await page.locator('.game-why').count())) throw new Error("no i'rab shown after answering");
    // the explanation offers the full sentence sheet
    await page.locator('#qX0').click();
    await page.waitForSelector('.sheet.show .irab-sheet', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('Aqaid: four chapters, the creed definitions, new grammar notes', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      if (!st) return null;
      const sens = st.chapters.flatMap(c => c.sentences);
      const withIrab = sens.flatMap(s => s.tokens).filter(t => t.irab);
      const trIrab = withIrab.filter(t => t.irab.tr && t.irab.ar);
      return {
        chapters: st.chapters.length,
        sentences: sens.length,
        tokens: sens.reduce((n, s) => n + s.tokens.length, 0),
        irab: withIrab.length, trIrab: trIrab.length,
        notes: ['ism-mawsul', 'jumla-sifa', 'damir-fasl', 'anwa-al-khabar', 'jumla-mutarida',
                'istithna-mufarragh', 'qad-harf', 'jam-muannath-salim', 'ism-maqsur-manqus',
                'doubled-verbs'].filter(id => GRAMMAR[id]).length,
        // Weak-verb paradigms must be stored, not derived.
        khalaJussive: st.morph.khala && st.morph.khala.majzum,
        istaaddaFakk: st.morph.istaadda && st.morph.istaadda.mazi[12],
      };
    });
    if (!info) throw new Error('aqaid-ahl-al-sunna missing from STORIES');
    if (info.chapters !== 4) throw new Error('chapters=' + info.chapters);
    if (info.notes !== 10) throw new Error('new grammar notes present: ' + info.notes + '/10');
    if (info.irab !== info.tokens) throw new Error(`i'rab ${info.irab}/${info.tokens}`);
    if (info.trIrab !== info.tokens) throw new Error(`ar+tr i'rab ${info.trIrab}/${info.tokens}`);
    if (info.khalaJussive !== 'يَخْلُ') throw new Error('خَلَا jussive: ' + info.khalaJussive);
    if (info.istaaddaFakk !== 'اِسْتَعْدَدْتُ') throw new Error('doubled verb fakk al-idgham: ' + info.istaaddaFakk);
  });

  await check("sentence i'rab sheet lists every word and its topics", async () => {
    await openStoryCard('aqaid-ahl-al-sunna');
    await page.locator('.sentence').first().locator('.irab-btn').click();
    await page.waitForSelector('.sheet.show .irab-sheet', { timeout: 3000 });
    const [rows, expected] = await Promise.all([
      page.locator('.irab-sheet tbody tr').count(),
      page.evaluate(() => STORIES.find(s => s.id === 'aqaid-ahl-al-sunna')
        .chapters[0].sentences[0].tokens.length),
    ]);
    if (rows !== expected) throw new Error(`sheet rows ${rows}, sentence has ${expected} tokens`);
    if (!(await page.locator('.irab-sheet .ir-ar').count()))
      throw new Error("Arabic i'rab column empty");
    if (!(await page.locator('.sheet-topics .btn').count()))
      throw new Error('no grammar topics listed for the sentence');
    // A topic chip opens that note; a word cell opens that word.
    await page.locator('.sheet-topics .btn').first().click();
    await page.waitForSelector('.sheet.show .gnote', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('.sentence').first().locator('.irab-btn').click();
    await page.locator('.irab-sheet .jump').first().click();
    await page.waitForSelector('.sheet.show .lemma', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('Kitab al-Buyu: Level 6 fiqh story, masdar-headed definitions', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'kitab-al-buyu');
      if (!st) return null;
      const sens = st.chapters.flatMap(c => c.sentences);
      const toks = sens.flatMap(s => s.tokens);
      const anqas = toks.find(t => t.s.bare === 'بأنقص');
      return {
        level: st.level, access: st.access, chapters: st.chapters.length,
        tokens: toks.length,
        full: toks.filter(t => t.irab && t.irab.ar && t.irab.tr).length,
        notes: ['masdar', 'thulathi-mujarrad-babs', 'form-vii-verbs'].filter(id => GRAMMAR[id]).length,
        // the elative is barred from tanwin, so its jarr is marked by fatha
        anqasIrab: anqas && anqas.irab.ar,
        // Form VII is always intransitive — no passive may have been invented
        vii: st.morph.inaqada && (st.morph.inaqada.majhulMazi || null),
        // and the defective VIII drops its ya in the jussive
        ishtaraJussive: st.morph.ishtara && st.morph.ishtara.majzum,
      };
    });
    if (!info) throw new Error('kitab-al-buyu missing from STORIES');
    if (info.level !== 6) throw new Error('level=' + info.level);
    if (info.access !== 'premium') throw new Error('access=' + info.access);
    if (info.chapters !== 3) throw new Error('chapters=' + info.chapters);
    if (info.notes !== 3) throw new Error('new sarf notes present: ' + info.notes + '/3');
    if (info.full !== info.tokens) throw new Error(`ar+tr i'rab ${info.full}/${info.tokens}`);
    if (!/بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ/.test(info.anqasIrab || ''))
      throw new Error('أَنْقَصَ not analysed as mamnu min al-sarf: ' + info.anqasIrab);
    if (info.vii) throw new Error('Form VII must have no passive, got ' + info.vii);
    if (info.ishtaraJussive !== 'يَشْتَرِ') throw new Error('اشترى jussive: ' + info.ishtaraJussive);
    // and the story opens
    await openStoryCard('kitab-al-buyu');
    await page.waitForSelector('.sentence', { timeout: 3000 });
    await page.locator('.sentence').first().locator('.irab-btn').click();
    await page.waitForSelector('.sheet.show .irab-sheet', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('TR UI leaves no English in the grammar reference or the word sheet', async () => {
    // The gap the checker was written for: explanations were bilingual, but note
    // titles, worked examples, level names and the fact chips were not.
    const gaps = await page.evaluate(() => {
      const out = [];
      for (const [id, g] of Object.entries(GRAMMAR)) {
        if (!g.title.tr) out.push('title:' + id);
        (g.examples || []).forEach((x, i) => {
          if (x.gloss && x.gloss.en && !x.gloss.tr) out.push(`example:${id}[${i}]`);
        });
      }
      REF_GROUPS.forEach(gr => { if (!gr.label || !gr.label.tr) out.push('refgroup:' + gr.id); });
      STORIES.forEach(s => { if (!LEVEL_TR[s.levelName]) out.push('levelName:' + s.levelName); });
      return out;
    });
    if (gaps.length) throw new Error('untranslated: ' + gaps.slice(0, 6).join(', '));

    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-group', { timeout: 3000 });
    const group = await page.locator('.ref-group span:not(.ar)').first().textContent();
    if (!/Sarf|Nahiv|Âmiller/.test(group)) throw new Error('ref group still English: ' + group);
    // the list is grouped, so read the id off the button rather than assuming one
    const noteId = await page.locator('.ref-list button').first().getAttribute('data-note');
    await page.locator('.ref-list button').first().click();
    await page.waitForSelector('.sheet.show .gnote', { timeout: 3000 });
    const heading = await page.locator('.gnote h3').first().textContent();
    const exGloss = await page.locator('.gnote .ex .en').first().textContent();
    const expect = await page.evaluate(id => ({
      tr: GRAMMAR[id].title.tr, en: GRAMMAR[id].title.en,
      exTr: (GRAMMAR[id].examples[0] || {}).gloss?.tr,
    }), noteId);
    if (!heading.includes(expect.tr)) throw new Error('note heading not Turkish: ' + heading);
    if (expect.en && heading.includes(expect.en)) throw new Error('note heading still English');
    if (expect.exTr && !exGloss.includes(expect.exTr.slice(0, 20)))
      throw new Error('example gloss not Turkish: ' + exGloss);
    await page.evaluate(() => document.getElementById('scrim').click());

    // word sheet: pos chip and level chip
    await page.locator('.lib-card').first().click();
    const lvl = await page.locator('.chip.level').first().textContent();
    if (!lvl.includes('Seviye')) throw new Error('level chip still English: ' + lvl);
    await page.locator('.sentence .word').first().click();
    await page.waitForSelector('.sheet.show .facts', { timeout: 3000 });
    const chips = await page.locator('.facts .chip').allTextContents();
    if (chips.some(c => /^(noun|verb|prep|part|pron|propn|adv|conj)$/.test(c.trim())))
      throw new Error('pos chip still English: ' + chips.join('|'));
    if (chips.some(c => /^(root:|pl\.|Form |Level )/.test(c.trim())))
      throw new Error('fact chip still English: ' + chips.join('|'));
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="en"]').click();
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('Abu Yusuf runs to five chapters; the conditional governs two verbs', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'wasiyyat-abi-yusuf-L5');
      const sens = st.chapters.flatMap(c => c.sentences);
      const toks = sens.flatMap(s => s.tokens);
      const walTakun = toks.find(t => t.s.bare === 'ولتكن');
      return {
        chapters: st.chapters.length, sentences: sens.length, tokens: toks.length,
        full: toks.filter(t => t.irab && t.irab.ar && t.irab.tr).length,
        notes: ['in-shartiyya', 'lam-amr'].filter(id => GRAMMAR[id]).length,
        walTakunGrammar: walTakun && (walTakun.grammar || []),
        // hollow verbs shorten in jazm, and the stored forms must say so
        kanaJussive: st.morph.kana && st.morph.kana.majzum,
        ajabaJussive: st.morph.ajaba && st.morph.ajaba.majzum,
        // Form III defective: the passive is what the text actually uses
        nadaPassive: st.morph.nada && st.morph.nada.majhulMudari,
      };
    });
    if (info.chapters !== 5) throw new Error('chapters=' + info.chapters);
    if (info.sentences !== 27) throw new Error('sentences=' + info.sentences);
    if (info.notes !== 2) throw new Error('in-shartiyya / lam-amr missing: ' + info.notes);
    if (info.full !== info.tokens) throw new Error(`ar+tr i'rab ${info.full}/${info.tokens}`);
    if (!(info.walTakunGrammar || []).includes('lam-amr'))
      throw new Error('وَلْتَكُنْ not anchored to lam-amr: ' + info.walTakunGrammar);
    if (info.kanaJussive !== 'يَكُنْ') throw new Error('كان jussive: ' + info.kanaJussive);
    if (info.ajabaJussive !== 'يُجِبْ') throw new Error('أجاب jussive: ' + info.ajabaJussive);
    if (info.nadaPassive !== 'يُنَادَى') throw new Error('نادى passive: ' + info.nadaPassive);
  });

  await check('corpus search finds by spelling, root and meaning, and jumps there', async () => {
    const counts = await page.evaluate(() => ({
      corpus: buildCorpus().length,
      tokens: STORIES.reduce((n, s) => n + s.chapters
        .reduce((m, c) => m + c.sentences.reduce((k, x) => k + x.tokens.length, 0), 0), 0),
      spelled: searchCorpus('قول').length,       // root typed closed up
      spaced: searchCorpus('ق و ل').length,      // root typed as stored
      unvowelled: searchCorpus('علم').length,
      english: searchCorpus('knowledge').length,
      turkish: searchCorpus('ilim').length,
      folded: searchCorpus('امر').length,        // bare alif for a hamza'd one
      tooShort: searchCorpus('a').length,
    }));
    if (counts.corpus !== counts.tokens)
      throw new Error(`index ${counts.corpus} vs ${counts.tokens} tokens`);
    if (counts.spelled !== counts.spaced)
      throw new Error(`root closed-up ${counts.spelled} != spaced ${counts.spaced}`);
    for (const k of ['spelled', 'unvowelled', 'english', 'turkish'])
      if (!counts[k]) throw new Error('no hits for ' + k);
    if (!counts.folded) throw new Error('alif folding does not match');
    if (counts.tooShort) throw new Error('a one-letter query should return nothing');

    await page.locator('#searchOpen').click();
    await page.waitForSelector('#corpusSearch', { timeout: 3000 });
    await page.fill('#corpusSearch', 'علم');
    await page.waitForSelector('.hit', { timeout: 3000 });
    if (!(await page.locator('.hit-lex').count())) throw new Error('results not grouped by word');
    if (!(await page.locator('.hit .h-ar b').count())) throw new Error('hit not highlighted');
    await page.locator('.hit').first().click();
    await page.waitForSelector('.sheet.show .lemma', { timeout: 3000 });
    await page.evaluate(() => document.getElementById('scrim').click());

    // the root chip in the word sheet runs the same index
    await page.locator('.sentence .word').first().click();
    await page.waitForSelector('.sheet.show .facts', { timeout: 3000 });
    if (await page.locator('.root-btn').count()) {
      await page.locator('.root-btn').first().click();
      await page.waitForSelector('#corpusSearch', { timeout: 3000 });
      const q = await page.locator('#corpusSearch').inputValue();
      if (!q.trim()) throw new Error('root chip did not fill the search box');
    }
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('daily loop: streak starts, goal moves, new words come from the story', async () => {
    await page.evaluate(() => {
      ['qissa-streak', 'qissa-today', 'qissa-goal', 'qissa-deck', 'qissa-progress']
        .forEach(k => localStorage.removeItem(k));
    });
    await page.reload();
    if (!(await page.locator('#streakChip').isHidden()))
      throw new Error('streak chip should be hidden before any activity');

    await page.locator('.lib-card').first().click();
    await page.locator('.sentence .word').first().click();      // reading counts
    await page.evaluate(() => document.getElementById('scrim').click());
    const afterRead = await page.evaluate(() => ({ ...state.streak, read: state.today.read }));
    if (afterRead.days !== 1) throw new Error('streak did not start: ' + afterRead.days);
    if (!afterRead.read) throw new Error('reading was not counted');

    await page.locator('#deckOpen').click();
    await page.waitForSelector('.daily', { timeout: 3000 });
    if (!(await page.locator('#learnHere').count()))
      throw new Error('no "learn new words" button with an empty deck');
    await page.locator('#learnHere').click();
    const afterLearn = await page.evaluate(() => ({
      learned: state.today.learned, deck: state.deck.length, goal: state.goal.newWords,
      // every word pulled in must come from the story being read and be new
      allFromHere: state.deck.every(d => !!CUR.glossary[d.lex]),
    }));
    if (afterLearn.learned !== afterLearn.goal)
      throw new Error(`learned ${afterLearn.learned}, goal ${afterLearn.goal}`);
    if (afterLearn.deck !== afterLearn.goal)
      throw new Error('deck size ' + afterLearn.deck + ' should equal the daily new-word goal');
    if (!afterLearn.allFromHere) throw new Error('a saved word is not from this story');
    // the button goes once the day's allowance is spent
    if (await page.locator('#learnHere').count())
      throw new Error('learn button should disappear once the goal is met');

    const chip = await page.locator('#streakChip').textContent();
    if (!/1/.test(chip) || !/%/.test(chip)) throw new Error('chip text: ' + chip);
    // grading a card counts as a review and moves the other bar
    await page.locator('#reviewCard').click();
    await page.locator('#reviewCard').click();
    await page.locator('.grade[data-q="good"]').click();
    const reviewed = await page.evaluate(() => state.today.reviewed);
    if (reviewed !== 1) throw new Error('review not counted: ' + reviewed);
    // a second act on the same day must not bump the streak again
    const days = await page.evaluate(() => state.streak.days);
    if (days !== 1) throw new Error('streak double-counted the same day: ' + days);
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('balagha: a fourth group, anchored to the imagery already in the stories', async () => {
    const info = await page.evaluate(() => {
      const ids = ['haqiqa-majaz', 'tashbih', 'istiara', 'kinaya', 'qasr'];
      const anchored = {};
      STORIES.forEach(s => s.chapters.forEach(c => c.sentences.forEach(x =>
        x.tokens.forEach(t => (t.grammar || []).forEach(g => {
          if (ids.includes(g)) anchored[g] = (anchored[g] || 0) + 1;
        })))));
      return {
        present: ids.filter(id => GRAMMAR[id]).length,
        group: ids.map(id => GRAMMAR[id] && GRAMMAR[id].group),
        inRefGroups: REF_GROUPS.some(g => g.id === 'balagha'),
        anchored,
        // every note must be bilingual like the rest
        untranslated: ids.filter(id => GRAMMAR[id] &&
          (!GRAMMAR[id].title.tr || (GRAMMAR[id].examples || [])
            .some(x => x.gloss && x.gloss.en && !x.gloss.tr))),
      };
    });
    if (info.present !== 5) throw new Error('balagha notes present: ' + info.present + '/5');
    if (info.group.some(g => g !== 'balagha')) throw new Error('wrong group: ' + info.group);
    if (!info.inRefGroups) throw new Error('balagha missing from REF_GROUPS');
    if (info.untranslated.length) throw new Error('no Turkish on: ' + info.untranslated);
    for (const id of ['haqiqa-majaz', 'tashbih', 'istiara', 'kinaya', 'qasr'])
      if (!info.anchored[id]) throw new Error(id + ' is not anchored to any token');

    // it shows up as its own section of the reference, in both languages
    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-group', { timeout: 3000 });
    let heads = await page.locator('.ref-group').allTextContents();
    if (!heads.some(h => /Rhetoric/.test(h))) throw new Error('no rhetoric group: ' + heads.join('|'));
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-group', { timeout: 3000 });
    heads = await page.locator('.ref-group').allTextContents();
    if (!heads.some(h => /Belâgat/.test(h))) throw new Error('rhetoric group not Turkish: ' + heads.join('|'));
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="en"]').click();
  });

  await check('badiʿ: the third division, and tibaq kept apart from muqabala', async () => {
    const info = await page.evaluate(() => {
      const ids = ['tibaq', 'muqabala', 'muraat-al-nazir', 'jinas', 'saj'];
      const anchored = {};
      // tibaq is one word against one word; muqabala is a set answered by a set.
      // A token that claims both would be teaching the reader the distinction is
      // not real, so the two must never land on the same word.
      const bothOnOneToken = [];
      STORIES.forEach(s => s.chapters.forEach(c => c.sentences.forEach(x =>
        x.tokens.forEach(t => {
          const g = t.grammar || [];
          g.forEach(id => { if (ids.includes(id)) anchored[id] = (anchored[id] || 0) + 1; });
          if (g.includes('tibaq') && g.includes('muqabala'))
            bothOnOneToken.push(s.id + ' ' + x.id + ' ' + t.s.bare);
        }))));
      return {
        missing: ids.filter(id => !GRAMMAR[id]),
        wrongGroup: ids.filter(id => GRAMMAR[id] && GRAMMAR[id].group !== 'balagha'),
        unanchored: ids.filter(id => !anchored[id]),
        bothOnOneToken,
      };
    });
    if (info.missing.length) throw new Error('missing notes: ' + info.missing);
    if (info.wrongGroup.length) throw new Error('not in balagha: ' + info.wrongGroup);
    if (info.unanchored.length) throw new Error('not anchored to any token: ' + info.unanchored);
    if (info.bothOnOneToken.length) throw new Error('tibaq and muqabala on one token: ' + info.bothOnOneToken);
    // "every note has mistakes / has Turkish" is enforced for all 75 notes by
    // validate_content.py and check_i18n.py — asserting it here for five would
    // pass loudly while saying nothing about the other seventy.

    // الْكِبَارَ / الصِّغَارَ carry two figures at once — the opposition and the
    // rhyme it falls into — and the word sheet must show both.
    await page.evaluate(() => document.getElementById('scrim').click());
    if (!(await page.locator('.lib-card').first().isVisible().catch(() => false))) {
      await page.locator('#backLib').click();
      await page.waitForSelector('.lib-card', { timeout: 3000 });
    }
    await openStoryCard('wasiyyat-abi-hanifa-L2');
    await page.locator('.word', { hasText: 'الْكِبَارَ' }).first().click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.locator('.sheet .tabs button', { hasText: 'Grammar' }).click();
    const titles = await page.locator('.gnote h3').allTextContents();
    for (const want of ['الطِّبَاق', 'السَّجْع'])
      if (!titles.some(t => t.includes(want)))
        throw new Error(want + ' not on the word: ' + titles.join(' | '));
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('library: New badges and a sort that agrees with the dates', async () => {
    await page.evaluate(() => document.getElementById('scrim').click());
    if (!(await page.locator('.lib-card').first().isVisible().catch(() => false))) {
      await page.locator('#backLib').click();
      await page.waitForSelector('.lib-card', { timeout: 3000 });
    }
    const data = await page.evaluate(() => {
      // A story published TODAY must read as zero days old in every timezone.
      // Mixing Date.UTC against a local-midnight parse made it -1 west of UTC,
      // so the badge never appeared on the day a story shipped.
      const now = new Date();
      const iso = now.getFullYear() + '-' + String(now.getMonth() + 1).padStart(2, '0') +
                  '-' + String(now.getDate()).padStart(2, '0');
      return {
        fresh: STORIES.filter(isNewStory).map(s => s.id),
        todayAge: daysSincePublished({ published: iso }),
        shippedToday: isNewStory({ published: iso }),
      };
    });
    if (data.todayAge !== 0)
      throw new Error('a story published today reads as ' + data.todayAge + ' days old');
    if (!data.shippedToday) throw new Error('a story published today is not badged NEW');

    // "By level" has to actually order by level — it used to be the identity,
    // which silently meant directory-name order.
    const byLevel = await page.evaluate(() =>
      [...document.querySelectorAll('.lib-card')].map(c => c.dataset.storyId));
    const levels = await page.evaluate(ids => ids.map(id =>
      STORIES.find(s => s.id === id).level), byLevel);
    for (let i = 1; i < levels.length; i++)
      if (levels[i] < levels[i - 1]) throw new Error('level sort is out of order: ' + levels);
    const badged = await page.evaluate(() => [...document.querySelectorAll('.lib-card')]
      .filter(c => [...c.querySelectorAll('.chip')].some(x => /NEW/.test(x.textContent)))
      .map(c => c.dataset.storyId));
    if (String(badged.slice().sort()) !== String(data.fresh.slice().sort()))
      throw new Error('badges ' + badged + ' disagree with isNewStory ' + data.fresh);

    await page.locator('.lib-sort [data-sort="new"]').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
    const order = await page.evaluate(() =>
      [...document.querySelectorAll('.lib-card')].map(c => c.dataset.storyId));
    const dates = await page.evaluate(ids => ids.map(id =>
      STORIES.find(s => s.id === id).published), order);
    for (let i = 1; i < dates.length; i++)
      if (dates[i] > dates[i - 1]) throw new Error('newest-first sort is out of order at ' + i + ': ' + dates);
    if (order.length !== byLevel.length) throw new Error('sorting dropped or duplicated cards');
    if (new Set(order).size !== order.length) throw new Error('a story appears twice after sorting');
    await page.locator('.lib-sort [data-sort="level"]').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('cloze: built only from sentences already read', async () => {
    // With nothing read anywhere it must say so rather than offer an empty game.
    const empty = await page.evaluate(() => {
      const saved = state.progress;
      state.progress = {};
      const n = clozeItems().length;
      state.progress = saved;
      return n;
    });
    if (empty !== 0) throw new Error('cloze drew ' + empty + ' items from unread sentences');

    await page.locator('.lib-card[data-story-id="yunus-wa-al-hut"]').click();
    await page.waitForSelector('.sentence .word', { timeout: 3000 });
    // Read the story, then the game has something to draw on.
    await page.evaluate(() => { STORIES[STORIES.findIndex(s => s.id === 'yunus-wa-al-hut')]
      .chapters.forEach(c => c.sentences.forEach(s => markRead(s.id))); });
    const items = await page.evaluate(() => {
      const out = [];
      // clozeRound resolves the distractor pool, which clozeItems defers.
      for (const it of clozeRound(50)) {
        const st = STORIES.find(s => s.id === it.storyId);
        // A distractor must never be a second right answer, so no lemma already
        // standing in the sentence may appear among them.
        const inSentence = new Set(it.sen.tokens
          .map(t => (st.glossary[t.lex] || {}).lemma).filter(Boolean));
        out.push({
          story: it.storyId,
          read: !!(state.progress[it.storyId] || {})[it.sen.id],
          pos: it.entry.pos,
          // No option may be identifiable by its class: the answer and every
          // distractor share one part of speech.
          collides: it.pool.some(g => inSentence.has(g.lemma)),
          samePos: it.pool.every(g => g.pos === it.entry.pos),
          enough: it.pool.length >= 2,
        });
      }
      return out;
    });
    if (!items.length) throw new Error('no cloze items after reading a whole story');
    const bad = items.filter(x => !x.read || !x.samePos || !x.enough || x.collides);
    if (bad.length) throw new Error(bad.length + '/' + items.length + ' bad items, e.g. ' + JSON.stringify(bad[0]));
    const offClass = await page.evaluate(() => clozeItems()
      .filter(it => !CLOZE_POS.includes(it.entry.pos)).length);
    if (offClass) throw new Error(offClass + ' items blank a word outside CLOZE_POS');

    await page.locator('#gamesOpen').click();
    await page.waitForSelector('#gCloze', { timeout: 3000 });
    await page.locator('#gCloze').click();
    await page.waitForSelector('.game-q', { timeout: 3000 });
    const q = await page.locator('.game-q').textContent();
    if (!q.includes('ـــــ')) throw new Error('no gap in the prompt: ' + q);
    const optCount = await page.locator('.opts [data-o]').count();
    if (optCount < 3) throw new Error('only ' + optCount + ' options');
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    const right = await page.locator('.opts .right').count();
    if (right !== 1) throw new Error('expected exactly one correct option, got ' + right);
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('every note opens with a plain summary, and the detail is one tap away', async () => {
    await toLibrary();
    const data = await page.evaluate(() => {
      const all = Object.entries(GRAMMAR);
      return {
        total: all.length,
        noPlain: all.filter(([, g]) => !g.plain || !g.plain.en || !g.plain.tr).map(([id]) => id),
        // A summary as long as the thing it summarises is not a summary.
        tooLong: all.filter(([, g]) => g.plain &&
          (g.plain.en.length > 320 || g.plain.tr.length > 320)).map(([id]) => id),
        // ...and it must actually be shorter than the full explanation.
        notShorter: all.filter(([, g]) => g.plain && g.explanation &&
          g.plain.en.length >= g.explanation.en.length).map(([id]) => id),
      };
    });
    if (data.noPlain.length) throw new Error('no bilingual plain summary on: ' + data.noPlain.slice(0, 5));
    if (data.tooLong.length) throw new Error('plain summary too long on: ' + data.tooLong);
    if (data.notShorter.length) throw new Error('plain is not shorter than explanation on: ' + data.notShorter);

    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-list', { timeout: 3000 });
    await page.locator('.ref-list [data-note="tibaq"]').click();
    await page.waitForSelector('.gnote p.plain', { timeout: 3000 });
    const lede = await page.locator('.gnote p.plain').first().textContent();
    if (!/opposite/.test(lede)) throw new Error('plain lede: ' + lede);
    // The classical account is present but folded away by default.
    const open = await page.locator('.gnote details.deep').first().evaluate(d => d.open);
    if (open) throw new Error('the full explanation should start closed');
    const deepText = await page.locator('.gnote details.deep p').first().textContent();
    if (!/Badi/.test(deepText)) throw new Error('full explanation missing: ' + deepText.slice(0, 60));
    // Opening it is remembered, so a reader who wants depth asks once.
    await page.locator('.gnote details.deep summary').first().click();
    // `toggle` is queued rather than dispatched synchronously, so wait for the
    // preference to settle instead of reading it in the same tick as the click.
    await page.waitForFunction(() => state.deepNotes === true, null, { timeout: 3000 })
      .catch(() => { throw new Error('opening the detail was not remembered'); });
    if (await page.evaluate(() => localStorage.getItem('qissa-deep')) !== '1')
      throw new Error('the preference was not persisted');
    await page.evaluate(() => { state.deepNotes = false; localStorage.setItem('qissa-deep', '0'); });
    await page.evaluate(() => document.getElementById('scrim').click());
  });

  await check('the app opens in the language of the device', async () => {
    // A Turkish device must not be shown an English app on first run; a stored
    // choice must still win over the device.
    const ctx2 = await browser.newContext({ locale: 'tr-TR' });
    try {
      const p2 = await ctx2.newPage();
      await p2.goto(url);
      const lang = await p2.evaluate(() => state.uiLang);
      if (lang !== 'tr') throw new Error('tr-TR device opened in ' + lang);
      const seg = await p2.locator('#uiLangSeg [data-ui="tr"]').getAttribute('class');
      if (!/on/.test(seg || '')) throw new Error('language segment does not show the active language');
      await p2.evaluate(() => localStorage.setItem('qissa-lang', 'en'));
      await p2.reload();
      if (await p2.evaluate(() => state.uiLang) !== 'en')
        throw new Error('a stored choice must override the device language');
    } finally {
      await ctx2.close();   // never leak the context past a failed assertion
    }
  });

  await check('nothing in the chrome reads like build metadata', async () => {
    await toLibrary();
    const txt = await page.evaluate(() => ({
      eyebrow: (document.getElementById('eyebrow') || {}).textContent || '',
      footer: document.querySelector('footer.note').textContent,
    }));
    for (const [where, s] of Object.entries(txt)) {
      if (/v\d+\.\d+|app shell|prototype|content\/samples|\.json/i.test(s))
        throw new Error(where + ' shows build metadata: ' + s.trim().slice(0, 80));
    }
    if (!txt.eyebrow.trim()) throw new Error('the eyebrow is empty');
  });

  await check('the question test identifies the role, in both languages', async () => {
    await toLibrary();
    const data = await page.evaluate(() => {
      const withQ = Object.entries(GRAMMAR).filter(([, g]) => g.question);
      return {
        count: withQ.length,
        // Both languages must be present and the same length — a note that has
        // the test in one language goes silently blank in the other.
        lopsided: withQ.filter(([, g]) => !g.question.tr || !g.question.en ||
          g.question.tr.length !== g.question.en.length).map(([id]) => id),
        // Every role the game can ask about must point at a note, and every
        // note it points at must exist.
        rolesMissingNote: ROLE_KEYS.filter(r => r.note && !GRAMMAR[r.note]).map(r => r.k),
        fail: (GRAMMAR.fail.question || {}).tr,
        mafulFih: (GRAMMAR['maful-fih'].question || {}).tr,
      };
    });
    if (data.count < 10) throw new Error('only ' + data.count + ' notes carry a question test');
    if (data.lopsided.length) throw new Error('question test not bilingual on: ' + data.lopsided);
    if (data.rolesMissingNote.length)
      throw new Error('role game points at missing notes: ' + data.rolesMissingNote);
    // Spot-check the transcription against research/sources/edatlar-irab-soru-testi.txt.
    if (!data.fail.includes('Kim?')) throw new Error("fa'il should answer «Kim?»: " + data.fail);
    if (!data.mafulFih.includes('Ne zaman?'))
      throw new Error("maf'ul fih should answer «Ne zaman?»: " + data.mafulFih);

    // It renders, and it follows the UI language.
    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-list', { timeout: 3000 });
    await page.locator('.ref-list [data-note="hal"]').click();
    await page.waitForSelector('.gnote .qtest', { timeout: 3000 });
    const en = await page.locator('.gnote .qtest .qt').first().textContent();
    if (!/In what state/.test(en)) throw new Error('EN question test: ' + en);
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="tr"]').click();
    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-list', { timeout: 3000 });
    await page.locator('.ref-list [data-note="hal"]').click();
    await page.waitForSelector('.gnote .qtest', { timeout: 3000 });
    const tr = await page.locator('.gnote .qtest .qt').first().textContent();
    if (!/Ne olduğu halde/.test(tr)) throw new Error('TR question test: ' + tr);
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#uiLangSeg [data-ui="en"]').click();
  });

  await check('playback offsets index the exact string that is spoken', async () => {
    // The word-following highlight maps a boundary event's charIndex back to a
    // token. That mapping is only as good as its agreement with the join speak()
    // uses — punctuation and the inter-word space are where it would drift — so
    // check every token of every sentence in the whole corpus.
    const bad = await page.evaluate(() => {
      const out = [];
      for (const st of STORIES)
        for (const ch of st.chapters)
          for (const sen of ch.sentences) {
            // sentenceText builds the string and the ranges together, so this
            // proves they agree for every token rather than trusting that two
            // descriptions of the format stayed in step.
            const { text, offsets } = sentenceText(sen);
            offsets.forEach((o, i) => {
              const got = text.slice(o.start, o.end);
              if (got !== sen.tokens[i].s.full)
                out.push(st.id + ' ' + sen.id + ' [' + i + '] ' + JSON.stringify(got));
            });
          }
      return out.slice(0, 5);
    });
    if (bad.length) throw new Error('offset drift: ' + bad.join(' | '));

    // ...and the DOM has to carry the index the mapping resolves to.
    if (!(await page.locator('.sentence .word').count())) {
      await page.waitForSelector('.lib-card', { timeout: 3000 });
      await page.locator('.lib-card').first().click();
      await page.waitForSelector('.sentence .word', { timeout: 3000 });
    }
    const mismatch = await page.evaluate(() => {
      const words = [...document.querySelectorAll('.sentence')].flatMap(s =>
        [...s.querySelectorAll('.word')].map((w, i) => w.dataset.ti === String(i)));
      return { total: words.length, wrong: words.filter(x => !x).length };
    });
    if (!mismatch.total) throw new Error('no words on the page to check');
    if (mismatch.wrong) throw new Error(mismatch.wrong + ' words carry the wrong data-ti');
  });

  await check('recorded narration plays the sentence\'s slice, and TTS yields to it', async () => {
    await toLibrary();
    await page.locator('.lib-card[data-story-id="yunus-wa-al-hut"]').click();
    await page.waitForSelector('.sentence .word', { timeout: 3000 });
    // Wire one sentence to a synthetic half-second WAV, exactly as a content
    // drop would: chapter names the file, the sentence carries its slice.
    await page.evaluate(() => {
      const rate = 8000, secs = 0.5, n = rate * secs;
      const buf = new ArrayBuffer(44 + n), v = new DataView(buf);
      const w = (o, str) => [...str].forEach((c, i) => v.setUint8(o + i, c.charCodeAt(0)));
      w(0, 'RIFF'); v.setUint32(4, 36 + n, true); w(8, 'WAVE');
      w(12, 'fmt '); v.setUint32(16, 16, true); v.setUint16(20, 1, true);
      v.setUint16(22, 1, true); v.setUint32(24, rate, true); v.setUint32(28, rate, true);
      v.setUint16(32, 1, true); v.setUint16(34, 8, true); w(36, 'data'); v.setUint32(40, n, true);
      for (let i = 0; i < n; i++) v.setUint8(44 + i, 128); // silence
      const b64 = btoa(String.fromCharCode(...new Uint8Array(buf)));
      CHAPTERS[0].audioFile = 'data:audio/wav;base64,' + b64;
      // The story ships with every sentence already timed (forward-prep), so
      // naming the file is genuinely all a narration drop needs. Shorten the
      // first slice so the test does not sit through a full sentence, and
      // strip the second sentence's span to prove the fallback.
      CHAPTERS[0].sentences[0].audio = [0, 250];
      window._savedSpan = CHAPTERS[0].sentences[1].audio;
      delete CHAPTERS[0].sentences[1].audio;
      buildSenAudio();
    });
    const counts = await page.evaluate(() => ({
      mapped: SEN_AUDIO.size,
      timed: CHAPTERS[0].sentences.filter(x => x.audio).length,
    }));
    if (counts.mapped !== counts.timed)
      throw new Error('SEN_AUDIO mapped ' + counts.mapped + ' but ' + counts.timed + ' sentences carry spans');

    try {
    await page.locator('.sentence').first().locator('.play:not(.irab-btn)').click();
    // The real path: the shared narration element takes the chapter file and
    // plays; the sentence highlight behaves exactly as with TTS.
    await page.waitForFunction(() => narration.src.startsWith('data:audio/wav'), null, { timeout: 3000 });
    if (!(await page.locator('.sentence.playing').count())) throw new Error('no sentence highlight during narration');
    // The slice ends on its own — [0,250]ms plus the guard timer — and the
    // highlight must come down with it, with nothing left playing.
    await page.waitForFunction(() => narration.paused, null, { timeout: 4000 });
    await page.waitForFunction(() => !document.querySelector('.sentence.playing'), null, { timeout: 2000 });

    // A sentence WITHOUT a slice must still take the synthesis path even
    // while its chapter has a recording — half-wired narration falls back.
    const second = await page.evaluate(() => !!SEN_AUDIO.get(CHAPTERS[0].sentences[1].id));
    if (second) throw new Error('a sentence with no span was mapped to the recording');
    await page.locator('.sentence').nth(1).locator('.play:not(.irab-btn)').click();
    // (The fallback guarantee is the SEN_AUDIO assert above — the un-spanned
    // sentence never enters the narration path at all.)
    } finally {
      // Undo the injection whether or not the check passed — a failure here
      // must not leave the story rewired for every later check.
      await page.evaluate(() => {
        delete CHAPTERS[0].audioFile;
        CHAPTERS[0].sentences[1].audio = window._savedSpan;
        delete window._savedSpan;
        buildSenAudio();
      });
    }
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('a grammar topic can be reviewed like a word', async () => {
    await page.evaluate(() => { state.deck.length = 0; persistDeck(); });
    await page.locator('#refOpen').click();
    await page.waitForSelector('.sheet.show .ref-list', { timeout: 3000 });
    await page.locator('.ref-list [data-note]').first().click();
    await page.waitForSelector('.gnote [data-note-save]', { timeout: 3000 });
    const noteId = await page.locator('.gnote [data-note-save]').first().getAttribute('data-note-save');
    await page.locator('.gnote [data-note-save]').first().click();
    const after = await page.locator('.gnote [data-note-save]').first().textContent();
    if (!/In your deck/.test(after)) throw new Error('button did not flip: ' + after);
    const card = await page.evaluate(() => state.deck.find(c => c.type === 'note'));
    if (!card || card.noteId !== noteId) throw new Error('note card not stored: ' + JSON.stringify(card));

    // The card asks the madrasah question: name the term, then give an example.
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#deckOpen').click();
    await page.waitForSelector('.sheet.show #reviewCard', { timeout: 3000 });
    const front = await page.locator('#reviewCard .front').textContent();
    const want = await page.evaluate(id => GRAMMAR[id].title.ar, noteId);
    if (front.trim() !== want) throw new Error('front is ' + front + ' expected ' + want);
    if (await page.locator('#reviewCard .verb-ask').count()) throw new Error('the answer was on the front');
    await page.locator('#reviewCard').click();
    if (!(await page.locator('#reviewCard .verb-ask').count())) throw new Error('step 2 revealed nothing');
    await page.locator('#reviewCard').click();
    if (!(await page.locator('#reviewCard .verb-answer').count())) throw new Error('no example at step 3');
    await page.locator('.grade[data-q="good"]').click();
    const due = await page.evaluate(() => state.deck[0].srs.due - Date.now());
    if (!(due > 0)) throw new Error('grading did not schedule the note card: ' + due);

    // A card pointing at a note that no longer exists must never reach a review.
    const pruned = await page.evaluate(() => {
      state.deck.push({ type: 'note', noteId: 'no-such-note-xyz', srs: { due: 0, ivl: 0 } });
      pruneDeck();                       // the real thing, not a copy of its filter
      return state.deck.length;
    });
    if (pruned !== 1) throw new Error('orphan note card survived the prune: ' + pruned);
    await page.evaluate(() => { state.deck.length = 0; persistDeck(); });
    await page.evaluate(() => document.getElementById('scrim').click());
  });

  await check('Lite deck cap: adding stops at the limit, reviewing never does', async () => {
    await toLibrary();
    const r = await page.evaluate(() => {
      const saved = { deck: state.deck, premium: state.premium };
      state.premium = false;
      // Fill to one below the cap with well-formed word cards.
      state.deck = Array.from({ length: LITE_DECK_CAP - 1 }, (_, i) =>
        ({ lex: 'zz' + i, type: 'word', bare: 'x', lemma: 'x',
           gloss: { en: 'x', tr: 'x' }, srs: { due: 0, ivl: 0 } }));
      const out = {};
      out.atCapAfterOne = (toggleCard('word:last', () =>
        ({ lex: 'last', type: 'word', bare: 'x', lemma: 'x', gloss: { en: 'x', tr: 'x' } })),
        state.deck.length);
      // The cap refuses the 101st…
      out.refused = toggleCard('word:overflow', () =>
        ({ lex: 'overflow', type: 'word', bare: 'x', lemma: 'x', gloss: { en: 'x', tr: 'x' } }));
      out.lenAfterRefused = state.deck.length;
      // …removal always works at the cap…
      toggleCard('word:last', () => null);
      out.lenAfterRemove = state.deck.length;
      // …and Premium lifts the limit.
      state.premium = true;
      out.premiumAdd = toggleCard('word:premium-extra', () =>
        ({ lex: 'premium-extra', type: 'word', bare: 'x', lemma: 'x', gloss: { en: 'x', tr: 'x' } }));
      const len = state.deck.length;
      state.deck = saved.deck; state.premium = saved.premium; persistDeck();
      out.premiumLen = len;
      return out;
    });
    if (r.atCapAfterOne !== 100) throw new Error('expected the cap-filling add to land at 100, got ' + r.atCapAfterOne);
    if (r.refused !== false) throw new Error('the 101st card was not refused: ' + r.refused);
    if (r.lenAfterRefused !== 100) throw new Error('deck length moved on a refused add');
    if (r.lenAfterRemove !== 99) throw new Error('removal at the cap failed');
    if (r.premiumAdd !== true || r.premiumLen !== 100)
      throw new Error('premium did not lift the cap: ' + r.premiumAdd + '/' + r.premiumLen);
  });

  await check('cloze hides «see it in the story» when the sentence is behind the paywall', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.access === 'premium');
      const savedPremium = state.premium;
      state.premium = true;
      const openShow = it => !storyLocked(STORIES.find(x => x.id === it.storyId));
      // With premium on, every sentence of every story is reachable.
      const anyLockedWhilePremium = STORIES.some(s => storyLocked(s));
      state.premium = savedPremium;
      return { anyLockedWhilePremium, probe: st.id };
    });
    if (r.anyLockedWhilePremium) throw new Error('a story is locked while premium is on');
    // Structural check of the predicate itself, on a locked story's sentences:
    const probe = await page.evaluate(() => {
      const saved = state.premium;
      state.premium = false;
      const st = STORIES.find(s => s.access === 'premium' && storyLocked(s));
      if (!st) { state.premium = saved; return null; }
      const flat = st.chapters.flatMap(c => c.sentences);
      const inside = flat[0], outside = flat[PREVIEW_SENTENCES];
      const show = it => {
        const s2 = STORIES.find(x => x.id === it.storyId);
        if (!storyLocked(s2)) return true;
        let i = 0;
        for (const ch of s2.chapters) for (const sen of ch.sentences) {
          if (sen.id === it.sen.id) return i < PREVIEW_SENTENCES;
          i++;
        }
        return false;
      };
      const out = {
        preview: show({ storyId: st.id, sen: inside }),
        behind: outside ? show({ storyId: st.id, sen: outside }) : null,
      };
      state.premium = saved;
      return out;
    });
    if (!probe) throw new Error('no locked premium story to probe');
    if (probe.preview !== true) throw new Error('a preview sentence should be jumpable');
    if (probe.behind !== false) throw new Error('a behind-paywall sentence should hide the jump');
  });

  await check('the library remembers the reader: continue card resumes mid-story', async () => {
    await toLibrary();
    const target = await page.evaluate(() => {
      // Start from a clean slate — earlier checks opened stories too.
      state.lastRead = null; localStorage.removeItem('qissa-lastread');
      // A free multi-sentence story, so the resume point really renders.
      const st = STORIES.find(s => s.access === 'free' &&
        s.chapters.reduce((n, c) => n + c.sentences.length, 0) >= 4);
      const sens = st.chapters.flatMap(c => c.sentences).map(x => x.id);
      // The reader stopped after the first two sentences.
      state.progress[st.id] = { [sens[0]]: 1, [sens[1]]: 1 };
      localStorage.setItem('qissa-progress', JSON.stringify(state.progress));
      renderLibrary();
      return { id: st.id, resumeAt: sens[2] };
    });
    // Progress alone earns no card — only a story actually opened does.
    if (await page.locator('.continue-card').count())
      throw new Error('a continue card appeared with no last-read story');
    await openStoryCard(target.id);
    await toLibrary();
    const cc = page.locator('.continue-card');
    if (!(await cc.count())) throw new Error('no continue card after opening a story');
    if ((await cc.getAttribute('data-story-id')) !== target.id)
      throw new Error('continue card shows the wrong story');
    if (!/2\/\d+/.test(await cc.textContent()))
      throw new Error('continue card does not show progress');
    await cc.click();
    await page.waitForSelector('.sentence.resume-target', { timeout: 3000 });
    const at = await page.evaluate(() => document.querySelector('.sentence.resume-target').dataset.id);
    if (at !== target.resumeAt) throw new Error('resumed at ' + at + ', expected ' + target.resumeAt);

    // A finished story retires the card and earns the ✓ chip in its place.
    const done = await page.evaluate(id => {
      const st = STORIES.find(s => s.id === id);
      const all = {};
      st.chapters.forEach(c => c.sentences.forEach(x => { all[x.id] = 1; }));
      state.progress[id] = all;
      localStorage.setItem('qissa-progress', JSON.stringify(state.progress));
      renderLibrary();
      return {
        cards: document.querySelectorAll('.continue-card').length,
        chip: !!document.querySelector('.lib-card[data-story-id="' + id + '"] .chip.done'),
      };
    }, target.id);
    if (done.cards) throw new Error('a finished story still offers "continue"');
    if (!done.chip) throw new Error('a finished story shows no ✓ chip');
    await page.evaluate(id => {
      delete state.progress[id];
      localStorage.setItem('qissa-progress', JSON.stringify(state.progress));
      state.lastRead = null; localStorage.removeItem('qissa-lastread');
      renderLibrary();
    }, target.id);
  });

  await check('library cards count new words, and due cards nudge from the shelf', async () => {
    await toLibrary();
    // Independent hand-count for one story — walked here, not through
    // storyNewWords, so agreement means something.
    const exp = await page.evaluate(() => {
      const st = STORIES[0];
      const have = new Set(state.deck.filter(d => d.type === 'word').map(d => d.lex));
      const seen = new Set();
      st.chapters.forEach(c => c.sentences.forEach(s => s.tokens.forEach(t => {
        const e = st.glossary[t.lex];
        if (e && e.level >= 1 && !have.has(t.lex)) seen.add(t.lex);
      })));
      return { id: st.id, n: seen.size };
    });
    if (!exp.n) throw new Error('fixture story offers no new words — pick another');
    const chip = await storyCard(exp.id).locator('.chip.newwords').textContent();
    if (!chip.includes(String(exp.n)))
      throw new Error('chip says "' + chip + '", hand count is ' + exp.n);
    // Saving one of those words moves the count down — the chip is live.
    const after = await page.evaluate(id => {
      const st = STORIES.find(s => s.id === id);
      const lex = st.chapters.flatMap(c => c.sentences.flatMap(s => s.tokens))
        .filter(t => {
          const e = st.glossary[t.lex];
          // Must be a word the deck does NOT hold, or the toggle removes it.
          return e && e.level >= 1 &&
            !state.deck.some(d => d.type === 'word' && d.lex === t.lex);
        })[0];
      toggleCard('word:' + lex.lex, () => ({ lex: lex.lex, type: 'word', bare: lex.s.bare,
        lemma: st.glossary[lex.lex].lemma, gloss: st.glossary[lex.lex].gloss }));
      renderLibrary();
      const c = document.querySelector('.lib-card[data-story-id="' + id + '"] .chip.newwords');
      const out = c ? c.textContent : '';
      toggleCard('word:' + lex.lex, () => null);   // put the deck back
      return out;
    }, exp.id);
    if (!after.includes(String(exp.n - 1)))
      throw new Error('saving a word did not move the chip: ' + after);

    // The nudge appears exactly when something is due, and opens the review.
    const r = await page.evaluate(() => {
      const saved = state.deck;
      state.deck = [];
      renderLibrary();
      const none = document.querySelectorAll('.review-nudge').length;
      state.deck = [{ lex: 'zz-due', type: 'word', bare: 'x', lemma: 'x',
                      gloss: { en: 'x', tr: 'x' }, srs: { due: 0, ivl: 0 } }];
      renderLibrary();
      const one = document.querySelectorAll('.review-nudge').length;
      const txt = one ? document.querySelector('.review-nudge').textContent : '';
      return { none, one, txt, savedLen: saved.length, _saved: void (window._savedDeck = saved) };
    });
    if (r.none !== 0) throw new Error('a nudge with an empty deck');
    if (r.one !== 1 || !r.txt.includes('1')) throw new Error('no nudge while a card is due: ' + r.txt);
    await page.locator('.review-nudge').click();
    await page.waitForSelector('.sheet.show #reviewCard', { timeout: 3000 });
    await page.evaluate(() => {
      state.deck = window._savedDeck; delete window._savedDeck; persistDeck();
      document.getElementById('scrim').click();
    });
    await toLibrary();
  });

  await check('the vocabulary sheet lists every teachable word of a story once', async () => {
    await toLibrary();
    // The newest story doubles as the fixture — this also proves the Samti
    // package opens and its glossary resolves.
    await openStoryCard('wasiyyat-abi-hanifa-samti');
    const exp = await page.evaluate(() => {
      const s = new Set();
      CUR.chapters.forEach(c => c.sentences.forEach(x => x.tokens.forEach(t => {
        const e = GLOSSARY[t.lex];
        if (e && e.level >= 1) s.add(t.lex);
      })));
      return s.size;
    });
    if (!exp) throw new Error('fixture story has no teachable words');
    await page.locator('#vocabChip').click();
    await page.waitForSelector('.sheet.show .vocab-list', { timeout: 3000 });
    const rows = await page.locator('.vocab-list li').count();
    if (rows !== exp) throw new Error(rows + ' rows for ' + exp + ' unique teachable words');
    const lv = await page.evaluate(() =>
      [...document.querySelectorAll('.vocab-list .chip.level')].map(x => +x.textContent.replace('L', '')));
    if (lv.some((v, i) => i && v < lv[i - 1])) throw new Error('not sorted easiest-first: ' + lv.join(','));
    // Saving from the list lands a real word card, and the button flips.
    const lex = await page.locator('.vocab-list [data-vocab-save]').first().getAttribute('data-vocab-save');
    await page.locator('.vocab-list [data-vocab-save]').first().click();
    const saved = await page.evaluate(l =>
      state.deck.some(c => c.type === 'word' && c.lex === l), lex);
    if (!saved) throw new Error('saving from the vocabulary list added no card');
    if (!/In your deck|Destede/.test(await page.locator('.vocab-list [data-vocab-save]').first().textContent()))
      throw new Error('the save button did not flip');
    await page.evaluate(l => {
      const i = state.deck.findIndex(c => c.type === 'word' && c.lex === l);
      if (i >= 0) { state.deck.splice(i, 1); persistDeck(); }
      document.getElementById('scrim').click();
    }, lex);
    await toLibrary();
  });

  await check('chapter pills jump through a long story, and never point past a paywall', async () => {
    await toLibrary();
    const pick = await page.evaluate(() => {
      const st = STORIES.find(s => !storyLocked(s) && s.chapters.length > 1);
      return st && { id: st.id, n: st.chapters.length };
    });
    if (!pick) throw new Error('no unlocked multi-chapter story on the shelf');
    await openStoryCard(pick.id);
    const pills = await page.locator('.ch-nav .ch-pill').count();
    if (pills !== pick.n) throw new Error(pills + ' pills for ' + pick.n + ' chapters');
    await page.locator('.ch-nav .ch-pill').last().click();
    await page.waitForFunction(n => {
      const el = document.querySelector('.chapter-head[data-ch="' + n + '"]');
      return el && Math.abs(el.getBoundingClientRect().top) < 250;
    }, pick.n, { timeout: 3000 }).catch(() => { throw new Error('the last pill did not land on its chapter'); });
    // A single-chapter story must not grow a nav.
    const single = await page.evaluate(() => {
      const st = STORIES.find(s => s.chapters.length === 1 && !storyLocked(s));
      return st && st.id;
    });
    if (single) {
      await toLibrary();
      await openStoryCard(single);
      if (await page.locator('.ch-nav').count()) throw new Error('a single-chapter story grew a chapter nav');
    }
    // A locked preview renders fewer heads than the manifest has chapters —
    // the pills must match the RENDERED heads, never the manifest.
    const locked = await page.evaluate(() => {
      const st = STORIES.find(s => storyLocked(s) && s.chapters.length > 1);
      return st && st.id;
    });
    if (locked) {
      await toLibrary();
      await openStoryCard(locked);
      const renderedHeads = await page.locator('.chapter-head').count();
      const lockedPills = await page.locator('.ch-nav .ch-pill').count();
      if (renderedHeads > 1 ? lockedPills !== renderedHeads : lockedPills !== 0)
        throw new Error(lockedPills + ' pills for ' + renderedHeads + ' rendered heads behind the paywall');
    }
    await toLibrary();
  });

  await check('tarkib and i\'rab: the sentence sheet reads words AND clauses', async () => {
    await toLibrary();
    await openStoryCard('wasiyyat-abi-hanifa-samti');
    // The button is now تركيب, not إعراب.
    const btn = await page.locator('.sentence .irab-btn').first().textContent();
    if (!btn.includes('تركيب')) throw new Error('sentence button reads: ' + btn);
    await page.locator('.sentence .irab-btn').first().click();
    await page.waitForSelector('.sheet.show .irab-sheet', { timeout: 3000 });
    // Every Samti sentence carries authored clause rows; count must match data.
    const exp = await page.evaluate(() => (CUR.chapters[0].sentences[0].jumal || []).length);
    if (!exp) throw new Error('s1 has no authored jumal');
    const rows = await page.locator('.jumla-row').count();
    if (rows !== exp) throw new Error(rows + ' clause rows for ' + exp + ' authored');
    // The clause layer teaches its doctrine: the jumal note is offered.
    if (!(await page.locator('.sheet-topics [data-note="anwa-al-jumal"]').count()))
      throw new Error('the jumal section does not link anwa-al-jumal');
    // Every authored row is complete in both languages, corpus-wide.
    const bad = await page.evaluate(() => {
      const out = [];
      for (const st of STORIES)
        for (const ch of st.chapters)
          for (const sen of ch.sentences)
            (sen.jumal || []).forEach((j, i) => {
              if (!j.text || !j.ar || !j.en || !j.tr) out.push(st.id + ' ' + sen.id + '[' + i + ']');
            });
      return out.slice(0, 5);
    });
    if (bad.length) throw new Error('incomplete jumal rows: ' + bad.join(', '));
    // A sentence WITHOUT authored jumal shows no clause section.
    await page.evaluate(() => document.getElementById('scrim').click());
    await toLibrary();
    await openStoryCard('wasiyyat-abi-hanifa-L2');
    await page.locator('.sentence .irab-btn').first().click();
    await page.waitForSelector('.sheet.show .irab-sheet', { timeout: 3000 });
    if (await page.locator('.jumla-row').count())
      throw new Error('an unanalysed sentence grew a clause section');
    await page.evaluate(() => document.getElementById('scrim').click());
    await toLibrary();
  });

  await check('the progress page agrees with the shelf, the deck and today', async () => {
    await toLibrary();
    const exp = await page.evaluate(() => {
      // Live expectations through the same primitives the page itself uses —
      // this proves the tiles agree with the library, not that both copied
      // the same arithmetic.
      let done = 0, read = 0;
      STORIES.forEach(st => {
        const s = storyStats(st);
        read += s.read;
        if (s.total && s.read === s.total) done++;
      });
      return { done, read, stories: STORIES.length,
               levels: new Set(STORIES.map(s => s.level)).size };
    });
    await page.locator('#statsOpen').click();
    await page.waitForSelector('.sheet.show .stats-grid', { timeout: 3000 });
    const tiles = (await page.locator('.stat-tile b').allTextContents()).map(x => x.trim());
    if (tiles.length !== 6) throw new Error('expected 6 tiles, got ' + tiles.length);
    if (!tiles.includes(exp.done + '/' + exp.stories))
      throw new Error('stories tile: ' + tiles.join('|') + ' missing ' + exp.done + '/' + exp.stories);
    if (!tiles.includes(String(exp.read)))
      throw new Error('sentences tile: ' + tiles.join('|') + ' missing ' + exp.read);
    if ((await page.locator('.lvl-row').count()) !== exp.levels)
      throw new Error('level rows do not match the levels on the shelf');
    // The reader's own level is the highlighted row — and only that one.
    await page.evaluate(() => { state.myLevel = STORIES[0].level; openStats(); });
    if ((await page.locator('.lvl-row.mine').count()) !== 1)
      throw new Error('own level not highlighted exactly once');
    await page.evaluate(() => { state.myLevel = 0; });
    await page.evaluate(() => document.getElementById('scrim').click());
  });

  await check('first run asks the level once, and "For you" shelves by it', async () => {
    // A brand-new profile: nothing stored, so this is the first visit.
    const ctx3 = await browser.newContext();
    try {
      const p3 = await ctx3.newPage();
      await p3.goto(url);
      await p3.waitForSelector('.sheet.show .level-pick', { timeout: 3000 });
      // The choices come from the shelf itself — every level present, no other.
      const offered = await p3.evaluate(() =>
        [...document.querySelectorAll('[data-pick-level]:not(.unsure)')].map(b => +b.dataset.pickLevel));
      const shelved = await p3.evaluate(() => [...new Set(STORIES.map(s => s.level))].sort((a, b) => a - b));
      if (offered.join() !== shelved.join())
        throw new Error('picker offers ' + offered + ' but the library holds ' + shelved);
      // Answer from the middle of whatever is on offer — the test must not
      // assume any particular level exists in the corpus.
      const mid = String(shelved[Math.floor(shelved.length / 2)]);

      await p3.locator('.level-pick [data-pick-level="' + mid + '"]').click();
      await p3.waitForSelector('.lib-card', { timeout: 3000 });
      if (await p3.locator('.sheet.show').count()) throw new Error('the sheet stayed open after a choice');
      const after = await p3.evaluate(() => ({
        level: localStorage.getItem('qissa-mylevel'),
        sort: state.libSort,
        // The comparator's whole contract: walking the rendered shelf, the
        // distance-rank must never decrease.
        ranks: [...document.querySelectorAll('.lib-card')].map(c =>
          forYouRank(STORIES.find(s => s.id === c.dataset.storyId))),
        chip: (document.getElementById('myLevelChip') || {}).textContent || '',
      }));
      if (after.level !== mid) throw new Error('level not persisted: ' + after.level);
      if (after.sort !== 'foryou') throw new Error('choosing a level did not select "For you"');
      if (after.ranks.some((r, i) => i && r < after.ranks[i - 1]))
        throw new Error('shelf order breaks the distance rank: ' + after.ranks);
      if (!after.chip.includes(mid)) throw new Error('no level chip after choosing: ' + after.chip);

      // Second visit: the question is not asked again, the shelf is remembered,
      // and the chip reopens the picker for a reader who mis-answered.
      await p3.reload();
      await p3.waitForSelector('.lib-card', { timeout: 3000 });
      if (await p3.locator('.sheet.show').count()) throw new Error('the picker came back on the second visit');
      if (await p3.evaluate(() => state.libSort) !== 'foryou') throw new Error('the sort was forgotten');
      await p3.locator('#myLevelChip').click();
      await p3.waitForSelector('.sheet.show .level-pick', { timeout: 3000 });
      const marked = await p3.locator('.level-pick .btn.saved').getAttribute('data-pick-level');
      if (marked !== mid) throw new Error('the reopened picker does not show the stored level');

      // A reader who dismissed the first-run sheet is asked nothing on boot,
      // but "For you" still opens the question instead of sorting by nothing.
      await p3.evaluate(() => { localStorage.removeItem('qissa-mylevel'); });
      await p3.reload();
      await p3.waitForSelector('.lib-card', { timeout: 3000 });
      if (await p3.locator('.sheet.show').count()) throw new Error('a dismissed picker must stay dismissed on boot');
      await p3.locator('[data-sort="foryou"]').click();
      await p3.waitForSelector('.sheet.show .level-pick', { timeout: 3000 });
    } finally {
      await ctx3.close();
    }
  });

  await check('struggling cards come first, the deck exports, the reading bar tracks', async () => {
    // The struggle model: a four-lapse card outranks a young one, whatever due says.
    const r = await page.evaluate(() => {
      const saved = state.deck;
      state.deck = [
        { lex: 'fresh1', type: 'word', bare: 'x', lemma: 'س', gloss: { en: 'a', tr: 'b' },
          srs: { due: 0, ivl: 0, reps: 3, ease: 2.5, lapses: 0 } },
        { lex: 'leechy', type: 'word', bare: 'x', lemma: 'ل', gloss: { en: 'a', tr: 'b' },
          srs: { due: 5, ivl: 0, reps: 1, ease: 1.6, lapses: 4 } },
        { lex: 'middle', type: 'word', bare: 'x', lemma: 'م', gloss: { en: 'a', tr: 'b' },
          srs: { due: 1, ivl: 0, reps: 2, ease: 2.1, lapses: 1 } },
      ];
      const q = dueCards().map(c => c.lex);
      const tsv = buildDeckExport();
      state.deck = saved;
      return { q, tsv };
    });
    if (r.q.join() !== 'leechy,middle,fresh1')
      throw new Error('queue is not struggle-first: ' + r.q.join());
    const lines = r.tsv.trim().split('\n');
    if (lines.length !== 3) throw new Error('export has ' + lines.length + ' rows for 3 cards');
    if (!lines.every(l => l.split('\t').length === 3))
      throw new Error('export is not three-column TSV');
    if (!/qissa vocab/.test(lines[0])) throw new Error('export rows carry no tag');

    // The reading bar: absent from the library, grows with scroll in a story.
    await toLibrary();
    if (await page.locator('#readbar').isVisible())
      throw new Error('the reading bar is visible in the library');
    await openStoryCard('wasiyyat-abi-hanifa-L2');
    await page.evaluate(() => window.scrollTo(0, document.scrollingElement.scrollHeight));
    await page.waitForFunction(() =>
      parseFloat(document.querySelector('#readbar div').style.width) > 50,
      null, { timeout: 3000 })
      .catch(() => { throw new Error('the reading bar did not follow the scroll'); });
    await page.evaluate(() => window.scrollTo(0, 0));
    await toLibrary();
  });

  await check('finishing a story raises the completion toast, exactly once', async () => {
    await toLibrary();
    const pick = await page.evaluate(() =>
      STORIES.find(s => !storyLocked(s)).id);
    await openStoryCard(pick);
    const r = await page.evaluate(() => {
      const flat = CUR.chapters.flatMap(c => c.sentences);
      const prog = {};
      flat.slice(0, -1).forEach(s => { prog[s.id] = 1; });
      state.progress[CUR.id] = prog;
      localStorage.setItem('qissa-progress', JSON.stringify(state.progress));
      markRead(flat[flat.length - 1].id);           // the finishing read
      const shown = !!document.querySelector('#toast.show');
      const text = shown ? document.getElementById('toast').textContent : '';
      markRead(flat[flat.length - 1].id);           // already read: no re-toast path
      return { shown, text };
    });
    if (!r.shown) throw new Error('no toast on the finishing read');
    if (!/finished|bitti/i.test(r.text)) throw new Error('toast says: ' + r.text);
    await page.evaluate(() => {
      delete state.progress[CUR.id];
      localStorage.setItem('qissa-progress', JSON.stringify(state.progress));
    });
    await toLibrary();
  });

  await check('every verb in every glossary owns a paradigm — no verb without tasrif', async () => {
    // The complaint this guards against: a reader taps مَضَى and finds no
    // Çekim tab. Sarf renders only when st.morph[lex] exists, so the sweep is
    // exhaustive: a glossary verb with no paradigm anywhere in the catalogue
    // fails the build.
    const r = await page.evaluate(() => {
      const missing = [];
      let verbs = 0;
      STORIES.forEach(st => Object.entries(st.glossary).forEach(([lex, e]) => {
        if (e.pos !== 'verb') return;
        verbs++;
        if (!st.morph || !st.morph[lex]) missing.push(st.id + ':' + lex);
      }));
      const mada = STORIES.find(s => s.id === 'wasiyyat-abi-hanifa-samti').morph.mada;
      return { verbs, missing, madaMajzum: mada && mada.majzum,
               madaCells: mada ? mada.mazi.length : 0 };
    });
    if (r.missing.length) throw new Error(r.missing.length + ' verbs without paradigms: ' + r.missing.slice(0, 5).join(', '));
    if (r.verbs < 150) throw new Error('sweep saw only ' + r.verbs + ' verbs — did the glossaries shrink?');
    // The verb from the field report: مَضَى, defective — the stored jussive
    // must be the shortened form, not a vowel swap.
    if (r.madaCells !== 14 || r.madaMajzum !== 'يَمْضِ')
      throw new Error('mada paradigm wrong: cells=' + r.madaCells + ' majzum=' + r.madaMajzum);
  });

  await check('لَيْسَ is jamid: a mazi-only sarf table, and no drill ever picks it', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.morph && s.morph.laysa);
      const m = st && st.morph.laysa;
      return { found: !!m, jamid: m && !!m.jamid, cells: m ? m.mazi.length : 0,
               second: m && m.mazi[6],                      // لَسْتَ
               muh: m ? muhtelife(m) : 'n/a',               // must be null — no governed forms
               drilled: sarfItems().some(it => it.lex === 'laysa') };
    });
    if (!r.found) throw new Error('no story carries a laysa paradigm');
    if (!r.jamid || r.cells !== 14) throw new Error('laysa entry malformed');
    if (r.second !== 'لَسْتَ') throw new Error('laysa 2nd person is ' + r.second);
    if (r.muh !== null) throw new Error('muhtelife built rows for a jamid verb');
    if (r.drilled) throw new Error('the sarf game drilled a jamid verb');
    // And the sheet itself: open the aqaid word sheet for a لَيْسَ token via
    // the same path a tap takes, then assert one tense button, no empty table.
    const ui = await page.evaluate(() => {
      const st = STORIES.find(s => s.morph && s.morph.laysa);
      const tok = { s: { full: 'لَيْسَ', smart: 'لَيْسَ', bare: 'ليس' }, lex: 'laysa', grammar: [] };
      CUR = st; GLOSSARY = st.glossary; MORPH = st.morph; wordCtx = null;
      openWord(tok, null, 'sarf');
      const tenses = [...document.querySelectorAll('.tense-seg [data-tense]')].map(b => b.dataset.tense);
      const cells = [...document.querySelectorAll('.conj td')].map(td => td.textContent).filter(Boolean);
      closeSheet();
      return { tenses, cellCount: cells.length, hasLasta: cells.includes('لَسْتَ') };
    });
    if (ui.tenses.join() !== 'mazi') throw new Error('jamid tense buttons: ' + ui.tenses.join());
    if (!ui.hasLasta || ui.cellCount < 14) throw new Error('jamid mazi table incomplete');
    await page.reload({ waitUntil: 'load' });
    await page.waitForSelector('.lib-card');
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
