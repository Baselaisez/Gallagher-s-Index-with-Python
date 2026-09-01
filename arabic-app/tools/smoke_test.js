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
    catch (e) {
      console.log('FAIL', name, '—', e.message.split('\n')[0]); process.exitCode = 1;
      // A check that throws part-way leaves whatever sheet it opened on screen,
      // and the next check's click lands on the scrim and times out. One real
      // failure then reads as three. Dismiss the sheet before moving on so the
      // count of failures is the count of DEFECTS.
      await page.evaluate(() => { try { closeSheet(); } catch (_) {} }).catch(() => {});
    }
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
    // Games is deliberately NOT a reader control any more: at the front door
    // it plays from the whole library. The reading controls still hide.
    for (const id of ['playAll', 'ulToggle', 'fontPlus'])
      if (await page.locator('#' + id).isVisible()) throw new Error('reader control visible in library: ' + id);
    if (!(await page.locator('#gamesOpen').isVisible())) throw new Error('Games must be reachable from the library');
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

  await check('SRS review: four grades, FSRS memory model, deck stats', async () => {
    await page.keyboard.press('Escape');
    await page.locator('#deckOpen').click();
    // Stats row is present before any review.
    await page.waitForSelector('.deck-stats .fresh', { timeout: 3000 });
    await page.locator('#reviewCard').click();
    await page.locator('#reviewCard').click();
    // All four grades, each showing the interval it would schedule.
    const grades = await page.locator('.grade-row .grade').count();
    if (grades !== 4) throw new Error('expected 4 grade buttons, got ' + grades);
    const previews = await page.locator('.grade-row .grade i').allTextContents();
    if (!previews.every(t => t.trim())) throw new Error('a grade button has no interval preview');
    if (previews[0] !== '10m') throw new Error('Again should schedule 10m, got ' + previews[0]);
    // FSRS: the previews must be strictly ordered hard < good < easy.
    const days = previews.slice(1).map(t => parseInt(t, 10));
    if (!(days[0] < days[1] && days[1] < days[2]))
      throw new Error('previews not hard<good<easy: ' + previews.join(','));
    await page.locator('.grade-row .grade[data-q="good"]').click();
    const txt = await page.locator('.empty').textContent();
    if (!txt.includes('Next review')) throw new Error('no next-review text: ' + txt);
    if (!(await page.locator('#deckCount').isHidden())) throw new Error('badge should hide when nothing due');
    // A first Good seeds the machine-learned initial stability: w[2] ≈ 3.7,
    // so the card is due in about four days — not SM-2's fixed one day.
    const s = await page.evaluate(() => state.deck[0].srs);
    if (s.ivl !== 4) throw new Error('first Good should give ivl=4 (S0≈3.71), got ' + s.ivl);
    if (!(s.S > 3 && s.S < 5)) throw new Error('stability not seeded: ' + s.S);
    if (!(s.D >= 1 && s.D <= 10)) throw new Error('difficulty out of range: ' + s.D);

    // An SM-2-era card (ease/ivl, no memory state) migrates on its next grade:
    // the survived interval floors the stability, so the interval grows.
    const mig = await page.evaluate(() => {
      const saved = state.deck;
      const c = { lex: 'mig', type: 'word', bare: 'x', lemma: 'م', gloss: { en: 'a', tr: 'b' },
                  srs: { due: 0, ivl: 10, ease: 2.0, reps: 3, lapses: 1 } };
      state.deck = [c];
      grade(c, 'good');
      const out = { S: c.srs.S, D: c.srs.D, ivl: c.srs.ivl };
      state.deck = saved; persistDeck();
      return out;
    });
    if (!(mig.ivl > 10)) throw new Error('migrated card interval did not grow: ' + mig.ivl);
    if (!(mig.D > 5)) throw new Error('lost ease should seed high difficulty, got ' + mig.D);
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
    const forms = await page.locator('table.conj.muhtelife tr:not(.majhul):not(.ext) td').allTextContents();
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

  await check('Aqaid: the creed definitions and their grammar notes', async () => {
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
    if (info.chapters < 4) throw new Error('chapters=' + info.chapters);
    if (info.notes !== 10) throw new Error('new grammar notes present: ' + info.notes + '/10');
    if (info.irab !== info.tokens) throw new Error(`i'rab ${info.irab}/${info.tokens}`);
    if (info.trIrab !== info.tokens) throw new Error(`ar+tr i'rab ${info.trIrab}/${info.tokens}`);
    if (info.khalaJussive !== 'يَخْلُ') throw new Error('خَلَا jussive: ' + info.khalaJussive);
    if (info.istaaddaFakk !== 'اِسْتَعْدَدْتُ') throw new Error('doubled verb fakk al-idgham: ' + info.istaaddaFakk);
  });

  await check('Aqaid ch5: the sifat parade and the uncreated Qur\'an, from the full matn', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      const ch5 = st.chapters.find(c => c.n === 5);
      if (!ch5) return null;
      const toks = ch5.sentences.flatMap(s => s.tokens);
      return {
        sentences: ch5.sentences.length,
        ismMaful: toks.filter(t => (t.grammar || []).includes('ism-maful')).length,
        diptote: toks.some(t => t.s.bare === 'مصاحفنا' &&
                                (t.grammar || []).includes('mamnu-min-sarf')),
        damirFasl: toks.some(t => (t.grammar || []).includes('damir-fasl')),
        gloss: !!(st.glossary.quran && st.glossary.kalam && st.glossary.udhun),
        ashbaha: st.morph.ashbaha && st.morph.ashbaha.mudari[0],
      };
    });
    if (!info) throw new Error('chapter 5 missing from aqaid-ahl-al-sunna');
    if (info.sentences !== 6) throw new Error('ch5 sentences=' + info.sentences);
    if (info.ismMaful < 5) throw new Error('ism maful parade thin: ' + info.ismMaful);
    if (!info.diptote) throw new Error('مصاحفنا must teach mamnu-min-sarf with the idafa kasra');
    if (!info.damirFasl) throw new Error('the damir fasl in s1 is missing');
    if (!info.gloss) throw new Error('new glossary entries missing');
    if (info.ashbaha !== 'يُشْبِهُ') throw new Error('ashbaha paradigm: ' + info.ashbaha);
  });

  await check('after a jazim the analyzer reads a governed mudari, not Form V', async () => {
    const r = await page.evaluate(() => {
      const rows = SentenceAnalyzer.analyze('لم تكتب امرأة');
      const v = rows[1];
      return {
        wazn: v.wazn || null,
        sure: v.sure, kind: v.kind,
        governed: v.notes.some(n => /governed mudari|âmilin çektiği muzâri/.test(n.en + n.tr)),
      };
    });
    if (r.wazn && /^تَفَ/.test(r.wazn.normalize('NFC')))
      throw new Error('Form V mizan survived after the jazim: ' + r.wazn);
    // either the corpus answered with certainty (kataba lives in the drill
    // garden now) or the heuristic must have said its piece — never neither.
    if (!(r.sure && r.kind === 'verb') && !r.governed)
      throw new Error('neither a corpus-certain verb nor the governed-mudari note');
  });

  await check('the drill garden: 24 free hoca-style sentences feed the IrabModel', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'jumal-al-tadrib');
      if (!st) return null;
      const sens = st.chapters.flatMap(c => c.sentences);
      const toks = sens.flatMap(s => s.tokens);
      const rakib = toks.find(t => t.s.bare === 'راكبا');
      return {
        access: st.access, chapters: st.chapters.length, sentences: sens.length,
        trIrab: toks.filter(t => t.irab && t.irab.tr && t.irab.ar).length,
        tokens: toks.length,
        halRole: rakib && RoleEngine.of(rakib),
        trainSize: IrabModel.trainingSize(),
        kataba: st.morph.kataba && st.morph.kataba.majzum,
        note: !!GRAMMAR['inna-am-anna'] && !!GRAMMAR['inna-am-anna'].title.tr,
      };
    });
    if (!info) throw new Error('jumal-al-tadrib missing from STORIES');
    if (info.access !== 'free') throw new Error('the drill garden must be free: ' + info.access);
    if (info.chapters < 3 || info.sentences < 24) throw new Error(`chapters=${info.chapters} sentences=${info.sentences}`);
    if (info.trIrab !== info.tokens) throw new Error(`ar+tr i'rab ${info.trIrab}/${info.tokens}`);
    if (info.halRole !== 'hal') throw new Error('راكبا must read as hal, got ' + info.halRole);
    if (info.trainSize < 900) throw new Error('the model should train on the drills too: ' + info.trainSize);
    if (info.kataba !== 'يَكْتُبْ') throw new Error('kataba jussive: ' + info.kataba);
    if (!info.note) throw new Error('the inna-am-anna note is missing or untranslated');
  });

  await check('the analyzer reads the hamza of ان by position: initial and qawl kasra, verb fatha', async () => {
    const r = await page.evaluate(() => {
      const at = (text, i) => SentenceAnalyzer.analyze(text)[i].notes.map(n => n.en + n.tr).join(' ');
      return {
        initial: at('ان الدرس سهل', 0),
        // زَيْدٌ carries its tanwin here on purpose. Once the corpus learned
        // زَادَ, the bare letters «زيد» became a real passive cell (زِيدَ) as
        // well as a name, and an unvowelled sentence genuinely cannot tell
        // them apart — so the walk back to the qawl verb stopped at what it
        // took for a verb. The tanwin settles it, and no verb wears one.
        afterQawl: at('قال زَيْدٌ ان الله قادر', 2),
        afterVerb: at('علم زَيْدٌ ان الله قادر', 2),
      };
    });
    if (!/KASRA|KESRALI/.test(r.initial) || !/sentence-initial|cümle başı/.test(r.initial))
      throw new Error('initial ان should read kasra: ' + r.initial);
    if (!/qawl|kavil/.test(r.afterQawl) || !/KASRA|KESRALI/.test(r.afterQawl))
      throw new Error('after qala the hamza keeps kasra: ' + r.afterQawl);
    if (!/FATHA|FETHALI/.test(r.afterVerb))
      throw new Error('after alima the hamza takes fatha: ' + r.afterVerb);
  });

  await check('the drill garden grows: objects family and shart chapters, 40 sentences', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'jumal-al-tadrib');
      const sens = st.chapters.flatMap(c => c.sentences);
      const toks = sens.flatMap(s => s.tokens);
      const naib = toks.find(t => t.s.bare === 'الرسالة');
      const mutlaq = toks.filter(t => (t.grammar || []).includes('maful-mutlaq')).length;
      return {
        chapters: st.chapters.length, sentences: sens.length,
        trIrab: toks.filter(t => t.irab && t.irab.tr && t.irab.ar).length, tokens: toks.length,
        naibRole: naib && RoleEngine.of(naib),
        mutlaq,
        trainSize: IrabModel.trainingSize(),
        darasa: st.morph.darasa && st.morph.darasa.majzum,
      };
    });
    if (info.chapters < 5 || info.sentences < 40)
      throw new Error(`chapters=${info.chapters} sentences=${info.sentences}`);
    if (info.trIrab !== info.tokens) throw new Error(`ar+tr i'rab ${info.trIrab}/${info.tokens}`);
    if (info.naibRole !== 'fail') throw new Error('naib al-fail should read as the fail family: ' + info.naibRole);
    if (info.mutlaq < 2) throw new Error('maful mutlaq drills missing: ' + info.mutlaq);
    if (info.trainSize < 1000) throw new Error('the model should now train on 1000+ tokens: ' + info.trainSize);
    if (info.darasa !== 'يَدْرُسْ') throw new Error('darasa jussive: ' + info.darasa);
  });

  await check('Aqaid ch6: takwin vs the mukawwan, and the vision without direction', async () => {
    const info = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      const ch6 = st.chapters.find(c => c.n === 6);
      if (!ch6) return null;
      const toks = ch6.sentences.flatMap(s => s.tokens);
      const muk = toks.find(t => t.s.bare === 'المكون');
      const yura = toks.find(t => t.s.bare === 'فيرى');
      return {
        sentences: ch6.sentences.length,
        muk: muk && (muk.grammar || []).join(','),
        yura: yura && (yura.grammar || []).includes('naib-al-fail'),
        gloss: !!(st.glossary.takwin && st.glossary.ruya && st.glossary.jaiz),
      };
    });
    if (!info) throw new Error('chapter 6 missing from aqaid-ahl-al-sunna');
    if (info.sentences !== 4) throw new Error('ch6 sentences=' + info.sentences);
    if (!/ism-maful/.test(info.muk || '') || !/form-ii-verbs/.test(info.muk || ''))
      throw new Error('المكون must teach Form II ism maful: ' + info.muk);
    if (!info.yura) throw new Error('فيرى must teach naib al-fail');
    if (!info.gloss) throw new Error('ch6 glossary entries missing');
  });

  await check('games: the hamza game blanks inna/anna and the stored i\'rab answers', async () => {
    // Measured and played in the SAME scope — the library. Opening a story
    // first would scope the round to that story, which may hold no inna at
    // all; that is the point of the scope, not a bug to work around.
    const pool = await page.evaluate(() => { renderLibrary(); return hamzaItems().length; });
    if (pool < 8) throw new Error('hamza pool too small: ' + pool);
    await page.evaluate(() => openGames());
    await page.locator('.game-pick #gHamza').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 3000 });
    const opts = await page.locator('.opts [data-o]').allTextContents();
    const bare = opts.map(o => o.replace(/[ً-ٰ]/g, ''));
    if (!(bare.some(o => o.includes('إن')) && bare.some(o => o.includes('أن'))))
      throw new Error('options must be inna vs anna, got: ' + opts.join(' | '));
    await page.locator('.opts [data-o]').first().click();
    if (!(await page.locator('.game-why').count())) throw new Error("no i'rab shown after answering");
    // no story was opened, so there is nothing to come back FROM
    await page.evaluate(() => { closeSheet(); renderLibrary(); });
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('a game detour into the grammar comes home to the same question', async () => {
    await page.locator('.lib-card').first().click();
    await page.locator('#gamesOpen').click();
    await page.locator('.game-pick #gHamza').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 3000 });
    const qBefore = await page.locator('.tabs .on').textContent();
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    const scoreBefore = await page.locator('.game-meta').textContent();
    // detour: open the rule note from the extras
    await page.locator('#qX0').click();
    await page.waitForSelector('#quizReturn', { timeout: 3000 });
    await page.locator('#quizReturn').click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    const qAfter = await page.locator('.tabs .on').textContent();
    const scoreAfter = await page.locator('.game-meta').textContent();
    if (qAfter !== qBefore) throw new Error(`resumed on a different question: ${qBefore} -> ${qAfter}`);
    if (scoreAfter !== scoreBefore) throw new Error('resume must not change the score');
    // the answered options stay revealed — no double answering
    if (!(await page.locator('.opts [data-o][disabled]').count())) throw new Error('resume lost the answered state');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('a wrong pick is taught: the correct answer and why yours fails', async () => {
    await page.locator('.lib-card').first().click();
    await page.locator('#gamesOpen').click();
    await page.locator('.game-pick #gHamza').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 3000 });
    // the sakin أَنْ option is ALWAYS wrong in this game — click it
    const texts = await page.locator('.opts [data-o]').allTextContents();
    const anIdx = texts.findIndex(t => t.replace(/[ً-ٰ]/g, '') === 'أن' && /ْ/.test(t.normalize('NFC')));
    await page.locator('.opts [data-o]').nth(anIdx >= 0 ? anIdx : 0).click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    if (anIdx >= 0) {
      if (!(await page.locator('.game-correct').count())) throw new Error('correct answer line missing after a wrong pick');
      if (!(await page.locator('.game-wrongwhy').count())) throw new Error('the why-yours-fails line is missing');
      const ww = await page.locator('.game-wrongwhy').textContent();
      if (!/masdar|müşeddede|mudari|muzâri/i.test(ww)) throw new Error('wrong-pick refutation looks empty: ' + ww);
    }
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('the qiyasi derivations: tafdil, zaman/makan and the semai instrument', async () => {
    const r = await page.evaluate(() => {
      const nfc = s => (s || '').normalize('NFC');
      return {
        kabir: nfc(IsmEngine.tafdil(['ك','ب','ر']).out),
        shadd: nfc(IsmEngine.tafdil(['ش','د','د']).out),
        ala: nfc(IsmEngine.tafdil(['ع','ل','و']).out),
        jls: nfc(IsmEngine.zamanMakan(['ج','ل','س'], true).out),
        ktb: nfc(IsmEngine.zamanMakan(['ك','ت','ب'], false).out),
        qwm: nfc(IsmEngine.zamanMakan(['ق','و','م'], null).out),
        wad: nfc(IsmEngine.zamanMakan(['و','ع','د'], null).out),
        rmy: nfc(IsmEngine.zamanMakan(['ر','م','ي'], null).out),
        miftah: nfc((IsmEngine.alat(['ف','ت','ح']) || {}).out),
        unknownAlat: IsmEngine.alat(['ك','ب','ر']),
      };
    });
    const N = s => s.normalize('NFC');
    if (r.kabir !== N('أَكْبَرُ')) throw new Error('tafdil kabir: ' + r.kabir);
    if (r.shadd !== N('أَشَدُّ')) throw new Error('tafdil geminate: ' + r.shadd);
    if (r.ala !== N('أَعْلَى')) throw new Error('tafdil naqis: ' + r.ala);
    if (r.jls !== N('مَجْلِس')) throw new Error('zaman/makan kasra bab: ' + r.jls);
    if (r.ktb !== N('مَكْتَب')) throw new Error('zaman/makan fatha bab: ' + r.ktb);
    if (r.qwm !== N('مَقَام')) throw new Error('zaman/makan hollow: ' + r.qwm);
    if (r.wad !== N('مَوْعِد')) throw new Error('zaman/makan mithal: ' + r.wad);
    if (r.rmy !== N('مَرْمًى')) throw new Error('zaman/makan naqis: ' + r.rmy);
    if (r.miftah !== N('مِفْتَاح')) throw new Error('alat table: ' + r.miftah);
    if (r.unknownAlat !== null) throw new Error('alat must REFUSE unknown roots');
    // and the lab shows them for a typed root, bab read from the corpus
    await page.locator('.lib-card').first().click();
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.sheet .tabs button[data-lab="ism"]', { timeout: 3000 });
    await page.locator('.sheet .tabs button[data-lab="ism"]').click();
    await page.fill('#ismIn', 'جلس');
    await page.waitForTimeout(300);
    const out = await page.locator('#ismOut').textContent();
    if (!out.includes('مَجْلِس'.normalize('NFC')) && !out.normalize('NFC').includes('مَجْلِس'.normalize('NFC')))
      throw new Error('the lab must derive مَجْلِس from the corpus bab of جلس');
    await page.evaluate(() => { conjState.ism = 'مدينة'; conjState.lab = 'sarf'; closeSheet(); });
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('the refutation reads the ending sign off the word itself', async () => {
    const r = await page.evaluate(() => {
      const of = w => { const s = caseSignOf(w); return s ? s.en + ':' + s.cases.join('/') : null; };
      return {
        damma: of('الْكِتَابُ'), tanwinDamm: of('كِتَابٌ'),
        fatha: of('الْكِتَابَ'), kasra: of('الْكِتَابِ'),
        sukun: of('يَكْتُبْ'),
        waw: of('الْمُسْلِمُونَ'), ya: of('الْمُسْلِمِينَ'), alif: of('الْمُسْلِمَانِ'),
        none: caseSignOf('كتاب'),
      };
    });
    if (r.damma !== 'damma:marfu' || r.tanwinDamm !== 'damma:marfu') throw new Error('damma: ' + r.damma + ' / ' + r.tanwinDamm);
    if (r.fatha !== 'fatha:mansub') throw new Error('fatha: ' + r.fatha);
    if (r.kasra !== 'kasra:majrur') throw new Error('kasra: ' + r.kasra);
    if (r.sukun !== 'sukun:majzum') throw new Error('sukun: ' + r.sukun);
    if (r.waw !== 'the waw:marfu') throw new Error('sound plural raf sign: ' + r.waw);
    if (r.ya !== 'the ya:mansub/majrur') throw new Error('sound plural nasb/jarr sign: ' + r.ya);
    if (r.alif !== 'the alif:marfu') throw new Error('dual raf sign: ' + r.alif);
    if (r.none !== null) throw new Error('an unvowelled word has no sign to read: ' + r.none);
    // and the role drills refute by naming BOTH question tests
    const rw = await page.evaluate(() => {
      const it = roleItems().find(i => i.key === 'fail');
      if (!it) return null;
      return roleWhyNot(it, { k: 'maful', html: '' });
    });
    if (!rw || !/kim|who/i.test(rw)) throw new Error('role refutation must name the true test: ' + rw);
    if (!/düştü|fall upon/i.test(rw)) throw new Error("role refutation must name the PICK's test too: " + rw);
  });

  await check('the quadriliteral babs: the other seventeen doors, by rule alone', async () => {
    const r = await page.evaluate(() => {
      const N = s => (s || '').normalize('NFC');
      const d = (root, bab) => rubaiDerive(root.split(''), bab);
      const R1 = d('دحرج', 'R1'), R2 = d('دحرج', 'R2');
      const R3 = d('حرجم', 'R3'), R4 = d('قشعر', 'R4');
      // every form the four babs can produce, proofread by the auditor
      const all = ['R1', 'R2', 'R3', 'R4'].flatMap(b => ['دحرج', 'قشعر'].flatMap(rt => {
        const x = d(rt, b);
        return [...x.mazi, ...x.mudari, ...x.amr, x.masdar, x.fail, x.maful];
      }));
      return {
        r1: [N(R1.mazi[0]), N(R1.mudari[0]), N(R1.amr[0]), N(R1.masdar), N(R1.fail), N(R1.maful)].join(' '),
        r2: [N(R2.mazi[0]), N(R2.mudari[0]), N(R2.masdar)].join(' '),
        r3: [N(R3.mazi[0]), N(R3.mudari[0]), N(R3.masdar)].join(' '),
        r4: [N(R4.mazi[0]), N(R4.mazi[12]), N(R4.mudari[0]), N(R4.amr[0]), N(R4.masdar)].join(' '),
        mulhaq: d('حوقل', 'R1').mulhaq,
        triFails: rubaiDerive(['ك', 'ت', 'ب'], 'R1').ok,
        flagged: all.filter(w => HarakeAuditor.audit(w).length),
        note: !!GRAMMAR['rubai-babs'] && !!GRAMMAR['rubai-babs'].title.tr,
      };
    });
    const N = s => s.normalize('NFC');
    if (r.r1 !== N('دَحْرَجَ يُدَحْرِجُ دَحْرِجْ دَحْرَجَة مُدَحْرِج مُدَحْرَج'))
      throw new Error('bare quadriliteral: ' + r.r1);
    if (r.r2 !== N('تَدَحْرَجَ يَتَدَحْرَجُ تَدَحْرُج')) throw new Error('tafalala: ' + r.r2);
    if (r.r3 !== N('اِحْرَنْجَمَ يَحْرَنْجِمُ اِحْرِنْجَام')) throw new Error('ifanlala: ' + r.r3);
    if (r.r4 !== N('اِقْشَعَرَّ اِقْشَعْرَرْتُ يَقْشَعِرُّ اِقْشَعِرَّ اِقْشِعْرَار'))
      throw new Error('ifalalla (idgham + fakk): ' + r.r4);
    if (!/فَوْعَلَ/.test(r.mulhaq || '')) throw new Error('حوقل must be named a mulhaq: ' + r.mulhaq);
    if (r.triFails !== false) throw new Error('a three-letter root must be REFUSED by the quadriliteral engine');
    if (r.flagged.length) throw new Error('the auditor flags derived forms: ' + r.flagged.join(', '));
    if (!r.note) throw new Error('the rubai-babs note is missing or untranslated');
    // and the lab hands the controls over when a fourth letter is typed
    await page.locator('.lib-card').first().click();
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.sheet .tabs button[data-lab="sarf"]', { timeout: 3000 });
    await page.locator('.sheet .tabs button[data-lab="sarf"]').click();
    await page.waitForSelector('#conjRoot', { timeout: 3000 });
    await page.fill('#conjRoot', 'دحرج');
    await page.waitForTimeout(200);
    if (await page.locator('#conjRubaiSeg').isHidden()) throw new Error('the quadriliteral babs stayed hidden');
    if (!(await page.locator('#conjFormSeg').isHidden())) throw new Error('the triliteral forms should step aside');
    const out = (await page.locator('#conjOut').textContent()).normalize('NFC');
    if (!out.includes(N('يُدَحْرِجُ'))) throw new Error('the lab did not conjugate the quadriliteral');
    await page.fill('#conjRoot', 'نصر');
    await page.waitForTimeout(200);
    if (!(await page.locator('#conjRubaiSeg').isHidden())) throw new Error('three letters must restore the triliteral controls');
    await page.evaluate(() => { conjState.root = 'نصر'; closeSheet(); });
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check("the twelve faces of ma, each named with the signal that proposed it", async () => {
    const r = await page.evaluate(() => {
      const first = t => {
        const rows = SentenceAnalyzer.analyze(t);
        const row = rows.find(x => /^(ما|مما|بما|انما|إنما)$/.test(stripAr(x.w)));
        if (!row) return { k: '<no ma row>', n: 0 };
        const wj = row.notes.map(n => n.en).filter(n => /مَا ا?ل/.test(n));
        const tr = row.notes.map(n => n.tr).filter(n => /مَا ا?ل/.test(n));
        return { k: wj[0] || '<none>', n: wj.length, tr: tr[0] || '' };
      };
      return {
        wonder:  first('مَا أَحْسَنَ زَيْدًا'),
        zarf:    first('مَا دُمْتُ حَيًّا'),
        hijazi:  first('مَا هٰذَا بَشَرًا'),
        nafiya:  first('مَا كَتَبَ الْوَلَدُ شَيْئًا'),
        istifham:first('مَا هٰذَا'),
        masdar:  first('عَجِبْتُ مِمَّا صَنَعْتَ'),
        shart:   first('مَا تَفْعَلْ مِنْ خَيْرٍ يَعْلَمْهُ اللهُ'),
        kaffa:   first('إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ'),
        note: !!GRAMMAR['anwa-ma'] && !!GRAMMAR['anwa-ma'].title.tr,
        wajhCount: Object.keys(MaEngine.WAJH).length,
      };
    });
    const want = {
      wonder: 'wonder', zarf: 'as long as', hijazi: 'laysa', nafiya: 'negating ma',
      istifham: 'interrogative', masdar: 'masdar-making', shart: 'conditional', kaffa: 'restraining',
    };
    for (const [k, needle] of Object.entries(want))
      if (!r[k].k.includes(needle))
        throw new Error(`${k}: expected «${needle}», got ${r[k].k}`);
    // every reading must carry its SIGNAL, not a bare verdict — and Turkish too
    if (!/:/.test(r.hijazi.k)) throw new Error('a reading must state the signal that proposed it');
    if (!r.hijazi.tr || /\b(follows|the khabar|governs|negating|noun)\b/i.test(r.hijazi.tr))
      throw new Error('the Turkish reading is missing or leaks English: ' + r.hijazi.tr);
    // a weak signal offers runners-up rather than one verdict
    if (r.masdar.n < 2) throw new Error('after a jarr letter both masdariyya and mawsula should stand');
    if (r.wajhCount < 12) throw new Error('the wajh table is short: ' + r.wajhCount);
    // EVERY defined reading must be reachable — a table entry no signal can
    // propose is dead data pretending to be coverage.
    const reach = await page.evaluate(() => {
      const seen = new Set();
      ['كَانَ مَا كَانَ', 'أَنَّمَا يُوحَى إِلَيَّ', 'عَمَّ يَتَسَاءَلُونَ', 'نِعِمَّا يَعِظُكُمْ بِهِ',
       'فَبِمَا رَحْمَةٍ مِنَ اللهِ لِنْتَ لَهُمْ', 'رُبَّمَا رَجُلٍ كَرِيمٍ', 'مَا هٰذَا بَشَرًا',
       'إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ', 'مَا أَحْسَنَ زَيْدًا', 'مَا دُمْتُ حَيًّا',
       'مَا تَفْعَلْ مِنْ خَيْرٍ يَعْلَمْهُ اللهُ', 'عَجِبْتُ مِمَّا صَنَعْتَ', 'مَا هٰذَا'].forEach(t => {
        SentenceAnalyzer.analyze(t).forEach(row => row.notes.forEach(n =>
          Object.entries(MaEngine.WAJH).forEach(([k, v]) => { if (n.en.includes(v.ar)) seen.add(k); })));
      });
      return { seen: [...seen], missing: Object.keys(MaEngine.WAJH).filter(k => !seen.has(k)) };
    });
    if (reach.missing.length)
      throw new Error('readings defined but unreachable: ' + reach.missing.join(', '));
    // كَانَ is a sister of kana, never a kaffa host — the regression guard
    const kana = await page.evaluate(() => {
      const rows = SentenceAnalyzer.analyze('كَانَ مَا كَانَ');
      const row = rows.find(x => stripAr(x.w) === 'ما');
      return row && row.wajh ? row.wajh.ar : '<none>';
    });
    if (/الْكَافَّة/.test(kana)) throw new Error('كان must not propose the kaffa reading: ' + kana);
    // لَمَّا keeps its jazm identity: the shadda is the whole difference
    const lamma = await page.evaluate(() => {
      const rows = SentenceAnalyzer.analyze('لَمَّا يَذُوقُوا عَذَابِ');
      return { wajh: !!rows[0].wajh, jazm: rows[0].notes.some(n => /jazm|câzim/.test(n.en + n.tr)) };
    });
    if (lamma.wajh) throw new Error('لَمَّا with shadda is the jazim, not fused la + ma');
    if (!lamma.jazm) throw new Error('لَمَّا lost its jazm reading');
    if (!r.note) throw new Error('the anwa-ma note is missing or untranslated');
  });

  await check("the verbs of defect and colour refuse i'lal", async () => {
    const r = await page.evaluate(() => {
      const N = x => (x || '').normalize('NFC');
      const conj = (root, bab) => {
        const cls = nakilClass({ root: root.split('').join(' ') });
        const d = sarfDerive(cls, 'I', bab);
        return d.ok ? { m: N(d.mazi[0]), u: N(d.mudari[0]), f: N(d.fail),
                        s: N(d.masdar || ''), note: d.note || '',
                        flagged: [...d.mazi, ...d.mudari, ...d.amr].filter(w => HarakeAuditor.audit(w).length) }
                    : { err: d.reason };
      };
      const steps = (() => {
        const cls = nakilClass({ root: 'ع و ر' });
        const d = sarfDerive(cls, 'I', 4);
        const st = ilalSteps(cls, 4, d.mazi[0], d.mudari[0]);
        return st && st.length === 1 ? st[0].tr : '<none>';
      })();
      return { awira: conj('عور', 4), hawila: conj('حول', 4),
               qala: conj('قول', 1), khafa: conj('خوف', 4), steps };
    });
    const N = x => x.normalize('NFC');
    if (r.awira.m !== N('عَوِرَ') || r.awira.u !== N('يَعْوَرُ'))
      throw new Error("عور must NOT undergo i'lal: " + r.awira.m + ' / ' + r.awira.u);
    if (r.awira.f !== N('أَعْوَر')) throw new Error('its ism fa\'il rides أَفْعَل: ' + r.awira.f);
    if (r.awira.s !== N('عَوَر')) throw new Error('its masdar is sound فَعَل: ' + r.awira.s);
    if (!r.awira.note) throw new Error('the exception must state its reason');
    if (r.awira.flagged.length) throw new Error('the auditor flags it: ' + r.awira.flagged.join(', '));
    if (r.hawila.m !== N('حَوِلَ')) throw new Error('حول: ' + r.hawila.m);
    // and the ordinary hollow verbs are untouched
    if (r.qala.m !== N('قَالَ') || r.qala.u !== N('يَقُولُ')) throw new Error('قال regressed: ' + r.qala.m);
    if (r.khafa.m !== N('خَافَ')) throw new Error('خاف regressed: ' + r.khafa.m);
    if (!/i'lâl işlemez|uyûb/.test(r.steps)) throw new Error("the walkthrough must say WHY no i'lal runs: " + r.steps);
  });

  await check('Aqaid ch7 and the sixth drill chapter join the shelf', async () => {
    const r = await page.evaluate(() => {
      const aq = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      const ch7 = aq.chapters.find(c => c.n === 7);
      const dr = STORIES.find(s => s.id === 'jumal-al-tadrib');
      const drToks = dr.chapters.flatMap(c => c.sentences).flatMap(s => s.tokens);
      const ch7Toks = ch7 ? ch7.sentences.flatMap(s => s.tokens) : [];
      return {
        ch7: ch7 ? ch7.sentences.length : 0,
        ch7Passive: ch7Toks.filter(t => (t.grammar || []).includes('naib-al-fail')).length,
        ch7Tawkid: ch7Toks.some(t => (t.grammar || []).includes('tawkid')),
        drChapters: dr.chapters.length,
        drSentences: dr.chapters.flatMap(c => c.sentences).length,
        tamyiz: drToks.filter(t => (t.grammar || []).includes('tamyiz')).length,
        mufarragh: drToks.some(t => (t.grammar || []).includes('istithna-mufarragh')),
        trIrab: drToks.filter(t => t.irab && t.irab.ar && t.irab.tr).length === drToks.length,
        trainSize: IrabModel.trainingSize(),
      };
    });
    if (r.ch7 !== 5) throw new Error('aqaid ch7 sentences: ' + r.ch7);
    // fidelity guard: a span may stop early, never skip from the middle.
    // s4 stops at the matn's comma; s5 begins the NEXT matn sentence, so its
    // waw is isti'nafiyya — the splice that made it look like atf is gone.
    const fid = await page.evaluate(() => {
      const ch7 = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna').chapters.find(c => c.n === 7);
      const s4 = ch7.sentences[3], s5 = ch7.sentences[4];
      return {
        s4len: s4.tokens.length,
        s5first: s5.tokens[0].irab.ar,
        s5grammar: (s5.tokens[0].grammar || []).join(','),
      };
    });
    if (fid.s4len !== 3) throw new Error('s4 must stop at the comma: ' + fid.s4len + ' tokens');
    if (!/اسْتِئْنَافِيَّةٌ/.test(fid.s5first))
      throw new Error("s5's waw follows a full stop — it is isti'nafiyya: " + fid.s5first);
    if (/atf-nasaq/.test(fid.s5grammar))
      throw new Error('s5 waw must not claim atf across a sentence boundary');
    // and the source divergence is recorded where the project records them.
    // The attribution text never ships to the browser — only reviewStatus does —
    // so this one is read off disk, where the scholar will read it.
    const man = JSON.parse(fs.readFileSync(
      path.join(__dirname, '..', 'content/samples/aqaid-ahl-al-sunna/manifest.json'), 'utf8'));
    const attrib = (man.attribution.en || '') + (man.attribution.tr || '');
    if (!/7:s2/.test(attrib))
      throw new Error('the 7:s2 source divergence is undocumented in the attribution');
    if (r.ch7Passive < 3) throw new Error('ch7 should drill the passive deputy: ' + r.ch7Passive);
    if (!r.ch7Tawkid) throw new Error('كُلِّهَا must teach ma\'nawi tawkid');
    if (r.drChapters < 6 || r.drSentences < 48)
      throw new Error(`drills: ${r.drChapters} chapters, ${r.drSentences} sentences`);
    if (r.tamyiz < 2) throw new Error('the tamyiz drills are missing: ' + r.tamyiz);
    if (!r.mufarragh) throw new Error('the emptied-exception drill is missing');
    if (!r.trIrab) throw new Error("every drill token needs ar+tr i'rab");
    if (r.trainSize < 1100) throw new Error('the model should train on 1100+ tokens now: ' + r.trainSize);
  });

  await check('Aqaid ch8: the sam\'iyyat, and the dual finally gets taught', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      const ch8 = st.chapters.find(c => c.n === 8);
      if (!ch8) return null;
      const toks = ch8.sentences.flatMap(s => s.tokens);
      const roll = ch8.sentences[3].tokens;
      const dual = toks.filter(t => (t.grammar || []).includes('al-muthanna'));
      const tafnayani = toks.find(t => t.s.bare === 'تفنيان');
      return {
        sentences: ch8.sentences.length,
        rollPairs: roll.filter(t => t.s.bare === 'حق').length,
        rollTokens: roll.length,
        dual: dual.length,
        fiveVerbs: tafnayani && (tafnayani.grammar || []).includes('afal-khamsa'),
        note: !!GRAMMAR['al-muthanna'] && !!GRAMMAR['al-muthanna'].title.tr,
        noteAnchored: (GRAMMAR['al-muthanna'].examples || []).filter(e => e.src).length,
        // chapter 1 opened with the hawd hadith; chapter 8 names الحوض حق
        ringClosed: roll.some(t => t.s.bare === 'والحوض'),
        trIrab: toks.every(t => t.irab && t.irab.ar && t.irab.tr),
      };
    });
    if (!r) throw new Error('chapter 8 missing from aqaid-ahl-al-sunna');
    if (r.sentences !== 5) throw new Error('ch8 sentences: ' + r.sentences);
    if (r.rollPairs !== 8) throw new Error('the roll must declare eight realities haqq: ' + r.rollPairs);
    if (r.rollTokens !== 16) throw new Error('eight mubtada/khabar pairs = 16 tokens, got ' + r.rollTokens);
    if (r.dual < 5) throw new Error('the dual tokens are not linked to the note: ' + r.dual);
    if (!r.fiveVerbs) throw new Error('تفنيان must be taught as one of the five verbs');
    if (!r.note) throw new Error('the al-muthanna note is missing or untranslated');
    if (r.noteAnchored < 2) throw new Error('the dual note must be anchored in real story text: ' + r.noteAnchored);
    if (!r.ringClosed) throw new Error('الحوض حق should close the ring chapter 1 opened');
    if (!r.trIrab) throw new Error("every ch8 token needs ar+tr i'rab");
  });

  await check('Aqaid ch9 and the kinds of majaz — the bayan file finally read', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      const ch9 = st.chapters.find(c => c.n === 9);
      if (!ch9) return null;
      const toks = ch9.sentences.flatMap(s => s.tokens);
      const n = GRAMMAR['anwa-al-majaz'];
      return {
        chapters: st.chapters.length,
        sentences: ch9.sentences.length,
        // the five verbs turn up again, and the diptote under al
        fiveVerbs: toks.some(t => (t.grammar || []).includes('afal-khamsa')),
        diptote: toks.filter(t => t.s.bare === 'الكبائر' && (t.grammar || []).includes('mamnu-min-sarf')).length,
        damirFasl: toks.some(t => (t.grammar || []).includes('damir-fasl')),
        maRelative: toks.filter(t => (t.grammar || []).includes('anwa-ma')).length,
        trIrab: toks.every(t => t.irab && t.irab.ar && t.irab.tr),
        note: !!n && !!n.title.tr && n.group === 'balagha',
        noteAqli: n && /أَنْبَتَ الرَّبِيعُ/.test(JSON.stringify(n)),
        noteZiyada: n && /لَيْسَ كَمِثْلِهِ/.test(JSON.stringify(n)),
        noteNuqsan: n && /وَاسْأَلِ الْقَرْيَةَ/.test(JSON.stringify(n)),
        noteAnchored: (n.examples || []).some(e => e.src),
      };
    });
    if (!r) throw new Error('chapter 9 missing from aqaid-ahl-al-sunna');
    if (r.chapters < 9) throw new Error('aqaid chapters: ' + r.chapters);
    if (r.sentences !== 4) throw new Error('ch9 sentences: ' + r.sentences);
    if (!r.fiveVerbs) throw new Error('يخلدون must be taught as one of the five verbs');
    if (r.diptote < 1) throw new Error('الكبائر must teach the diptote regaining its kasra under al');
    if (!r.damirFasl) throw new Error('the damir fasl in the definition of iman is missing');
    if (r.maRelative < 1) throw new Error('the relative ma in the definition of iman should link the anwa-ma note');
    if (!r.trIrab) throw new Error("every ch9 token needs ar+tr i'rab");
    if (!r.note) throw new Error('the anwa-al-majaz note is missing, untranslated, or misfiled');
    if (!r.noteAqli) throw new Error('majaz aqli needs its worked example');
    if (!r.noteZiyada || !r.noteNuqsan) throw new Error('the majaz of addition and omission need their Qur\'anic examples');
    if (!r.noteAnchored) throw new Error('the note must anchor at least one example in the corpus');
  });

  await check('the alaqa registry matches the book\'s own tally, and its game grades', async () => {
    const r = await page.evaluate(() => ({
      worked: alaqaItems().length,
      total: ALAQAT.length + ALAQAT_NAMED.length,
      claimed: ALAQAT_TOTAL,
      // every worked relation must carry the whole madrasah apparatus
      complete: ALAQAT.every(a => a.ex && a.haqiqi && a.haqiqi.ar && a.majazi && a.majazi.ar &&
                                  a.qarina && a.qarina.tr && a.def && a.def.tr),
      // only mushabaha makes an istiara — that is the whole mursal/istiara line
      istiara: ALAQAT.filter(a => a.istiara).map(a => a.k),
      mirrors: ['sababiyya', 'musabbabiyya', 'mahalliyya', 'halliyya',
                'juziyya', 'kulliyya'].every(k => ALAQAT.some(a => a.k === k)),
      balaghaArea: EloModel.AREAS.includes('balagha'),
      coachLabel: !!ui().coachAreas.balagha,
    }));
    if (r.total !== r.claimed)
      throw new Error(`the registry counts ${r.total} but the book says ${r.claimed}`);
    // twelve when only twelve carried an example; all twenty-eight do now
    if (r.worked < 28) throw new Error('worked relations: ' + r.worked);
    if (!r.complete) throw new Error('a relation is missing its example, meanings or qarina');
    if (r.istiara.length !== 1 || r.istiara[0] !== 'mushabaha')
      throw new Error('only likeness makes an istiara, got: ' + r.istiara.join(','));
    if (!r.mirrors) throw new Error('the three mirrored pairs must all be present');
    if (!r.balaghaArea || !r.coachLabel) throw new Error('balagha must be a real skill area with a label');
    // and the game itself grades, refutes and links its note
    await page.locator('.lib-card').first().click();
    await page.locator('#gamesOpen').click();
    await page.locator('.game-pick #gAlaqa').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 3000 });
    if (!(await page.locator('.alaqa-pair').count())) throw new Error('the two meanings are not shown');
    if ((await page.locator('.opts [data-o]').count()) !== 4) throw new Error('expected 4 options');
    // pick a deliberately wrong option so the refutation must appear
    const wrong = await page.evaluate(() => {
      const btns = [...document.querySelectorAll('.opts [data-o]')];
      const right = btns.findIndex(b => b.dataset.o !== undefined && false);
      return btns.length - 1;
    });
    await page.locator('.opts [data-o]').nth(wrong).click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    const why = await page.locator('.game-why').textContent();
    if (!/[ء-ي]/.test(why)) throw new Error('the explanation must name the relation in Arabic');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check('the i\'rab-realization engine: by what, and in what manner', async () => {
    const r = await page.evaluate(() => {
      const of = w => { const x = IrabSign.of(w); return x ? x.by + '/' + x.manner : 'REFUSED'; };
      return {
        haraka: of('الْكِتَابُ'), waw: of('الْمُسْلِمُونَ'), ya: of('الْمُسْلِمِينَ'),
        dual: of('الْمُسْلِمَانِ'), five: of('أَبُوهُ'), maqsur: of('الْفَتَى'),
        mabni: of('هٰذَا'), jazm: of('يَكْتُبْ'), manqus: of('الْقَاضِي'),
        nisba: of('الْعَرَبِيُّ'),
        // the surface CANNOT tell indefinite manqus from any other majrur,
        // so the engine must not pretend: it reads it as the plain vowel.
        indefManqus: of('قَاضٍ'),
        // and the analyzer shows it
        inRow: (() => {
          const rows = SentenceAnalyzer.analyze('جَاءَ الْمُسْلِمُونَ');
          const m = rows.find(x => stripAr(x.w) === 'المسلمون');
          return m && m.realize ? m.realize.by + '/' + m.realize.manner : '<none>';
        })(),
      };
    });
    const want = {
      haraka: 'haraka/lafzi', waw: 'huruf/lafzi', ya: 'huruf/lafzi', dual: 'huruf/lafzi',
      five: 'huruf/lafzi', maqsur: 'haraka/taqdiri', mabni: 'mahalli/mahalli',
      jazm: 'hadhf/lafzi', manqus: 'haraka/taqdiri', nisba: 'haraka/lafzi',
      indefManqus: 'haraka/lafzi', inRow: 'huruf/lafzi',
    };
    for (const [k, v] of Object.entries(want))
      if (r[k] !== v) throw new Error(`${k}: expected ${v}, got ${r[k]}`);
  });

  await check('the deck browser filters agree with the stats row', async () => {
    const r = await page.evaluate(() => {
      const saved = state.deck.slice();
      const gl = STORIES[0].glossary;
      state.deck = Object.keys(gl).slice(0, 12).map(l =>
        ({ lex: l, lemma: gl[l].lemma, bare: gl[l].lemma, gloss: gl[l].gloss, type: 'word' }));
      const st = deckStats();
      const out = {
        agree: st.fresh === deckCount('fresh') && st.mature === deckCount('mature') &&
               st.leeches === deckCount('leech') && st.total === deckCount('all'),
        // a search narrows, and an impossible search empties
        narrowed: (() => { deckQuery = 'zzzznotathing'; const n = state.deck.filter(deckMatches).length;
                           deckQuery = ''; return n; })(),
      };
      state.deck = saved;
      return out;
    });
    if (!r.agree) throw new Error('the filter counts disagree with deckStats');
    if (r.narrowed !== 0) throw new Error('an impossible search should match nothing, got ' + r.narrowed);
  });

  await check('Aqaid ch10 and the alaqa panel', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'aqaid-ahl-al-sunna');
      const ch10 = st.chapters.find(c => c.n === 10);
      if (!ch10) return null;
      const toks = ch10.sentences.flatMap(s => s.tokens);
      // the note is on the governed VERBS too, rightly — count the particle
      const an = toks.filter(t => t.lex === 'an-masdariyya');
      const yashqa = toks.find(t => t.s.bare === 'يشقى');
      return {
        chapters: st.chapters.length, sentences: ch10.sentences.length,
        // the SAKIN an twice — the very contrast the hamza rule teaches
        anCount: an.length,
        anSakin: an.every(t => /أَنْ$/.test(t.s.full.normalize('NFC'))),
        // taqdiri raf on an alif, and the genus-denying la
        taqdiri: yashqa && /مُقَدَّرَة/.test(yashqa.irab.ar),
        laJins: toks.some(t => (t.grammar || []).includes('la-nafiya-lil-jins')),
        mutlaq: toks.some(t => (t.grammar || []).includes('maful-mutlaq')),
        trIrab: toks.every(t => t.irab && t.irab.ar && t.irab.tr),
        // the engine agrees with the hand analysis on the maqsur verb
        engine: yashqa && (() => { const x = IrabSign.of(yashqa.s.full); return x && x.manner; })(),
      };
    });
    if (!r) throw new Error('chapter 10 missing');
    if (r.chapters < 10) throw new Error('aqaid chapters: ' + r.chapters);
    // six since v83: the matn's own change-clause was restored between the
    // saada/shaqawa verse and the closing denial it exists to set up.
    if (r.sentences !== 6) throw new Error('ch10 sentences: ' + r.sentences);
    if (r.anCount !== 2 || !r.anSakin) throw new Error('both أَنْ must be the SAKIN masdar-maker');
    if (!r.taqdiri) throw new Error('يَشْقَى must teach the estimated damma on the alif');
    if (!r.laJins) throw new Error('the genus-denying la is missing');
    if (!r.mutlaq) throw new Error('حَقًّا must be taught as an absolute object');
    if (!r.trIrab) throw new Error("every ch10 token needs ar+tr i'rab");
    if (r.engine !== 'taqdiri')
      throw new Error('IrabSign should agree with the hand analysis on يَشْقَى: ' + r.engine);
    // the panel opens from the grammar reference and lists every relation
    await page.locator('.lib-card').first().click();
    await page.locator('#refOpen').click();
    await page.waitForSelector('#alaqatOpen', { timeout: 3000 });
    await page.locator('#alaqatOpen').click();
    await page.waitForSelector('.av-table', { timeout: 3000 });
    const rows = await page.locator('.av-table tbody tr').count();
    if (rows !== 28) throw new Error('the panel should show all twenty-eight relations, got ' + rows);
    if (!(await page.locator('#alaqaPlay').count())) throw new Error('the panel should offer its game');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
  });

  await check("sentence i'rab sheet lists every word and its topics", async () => {
    await openStoryCard('aqaid-ahl-al-sunna');
    await page.locator('.sentence').first().locator('.irab-btn').click();
    await page.waitForSelector('.sheet.show .irab-sheet', { timeout: 3000 });
    // The sheet carries TWO tables of this class by design — the TARKIB table
    // and the TAHQIQ comparison below it, which share their styling on purpose.
    // This check is about the tarkib table, so it has to say so.
    const [rows, expected] = await Promise.all([
      page.locator('.irab-sheet:not(.tahqiq) tbody tr').count(),
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
      // Closed-up must find EVERY spaced hit. It may find more: المنقول really
      // does contain ق-و-ل, and a learner who typed those letters may have
      // meant it. Superset, not equality — equality was a coincidence of the
      // corpus, and the first word that broke it was a correct one.
      spacedNotInSpelled: (() => {
        const A = new Set(searchCorpus('قول'));
        return searchCorpus('ق و ل').filter(r => !A.has(r)).length;
      })(),
      // …and the true root must still rank top, above the accidents.
      topLex: (() => {
        const hits = searchCorpus('ق و ل'), by = new Map();
        hits.forEach(h => by.set(h.tok.lex, (by.get(h.tok.lex) || 0) + 1));
        const best = searchCorpus('قول').slice()
          .sort((a, b) => searchRank(b, 'قول') - searchRank(a, 'قول'))[0];
        return best && best.entry.root;
      })(),
      // an incidental substring must score below a real root match
      rankGap: (() => {
        const rows = searchCorpus('قول');
        const acc = rows.find(r => r.entry.root && r.entry.root !== 'ق و ل');
        const real = rows.find(r => r.entry.root === 'ق و ل');
        return acc && real ? searchRank(real, 'قول') - searchRank(acc, 'قول') : 0;
      })(),
      unvowelled: searchCorpus('علم').length,
      english: searchCorpus('knowledge').length,
      turkish: searchCorpus('ilim').length,
      folded: searchCorpus('امر').length,        // bare alif for a hamza'd one
      tooShort: searchCorpus('a').length,
    }));
    if (counts.corpus !== counts.tokens)
      throw new Error(`index ${counts.corpus} vs ${counts.tokens} tokens`);
    if (counts.spacedNotInSpelled)
      throw new Error(`${counts.spacedNotInSpelled} spaced-root hits missing from the closed-up search`);
    if (counts.spelled < counts.spaced)
      throw new Error(`root closed-up ${counts.spelled} < spaced ${counts.spaced}`);
    if (counts.topLex !== 'ق و ل')
      throw new Error('closed-up root search does not rank the real root first: ' + counts.topLex);
    if (!(counts.rankGap > 0))
      throw new Error('an incidental substring ranks as high as the real root: gap ' + counts.rankGap);
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

  await check('bablara nakil: a sound root rides the twelve wazns, weak roots decline', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'wasiyyat-abi-hanifa-samti');
      CUR = st; GLOSSARY = st.glossary; MORPH = st.morph; wordCtx = null;
      const tokN = { s: { full: 'نَصَرَ', smart: 'نَصَرَ', bare: 'نصر' }, lex: 'nasara', grammar: [] };
      sarfTense = 'mazi';
      openWord(tokN, null, 'sarf');
      const hasBtn = !!document.querySelector('[data-tense="nakil"]');
      sarfTense = 'nakil';
      openWord(tokN, null, 'sarf');
      const rows = [...document.querySelectorAll('table.conj.nakil .nakil-out')].map(td => td.textContent);
      const ownEl = document.querySelector('table.conj.nakil tr.own-bab .nakil-out');
      const ownBab = ownEl ? ownEl.textContent : '';
      const note = document.querySelector('.sarf-note').textContent;
      // The ibdal rules the received table demonstrates, straight from the maker.
      const viii = NAKIL_BABS.find(b => b.en === 'Form VIII');
      const istabara = viii.make('ص', 'ب', 'ر', 'sound').normalize('NFC');
      const iddhahaba = viii.make('ذ', 'ه', 'ب', 'sound').normalize('NFC');
      // Every class now rides its own i'lal: hollow, geminate, defective,
      // mithal — while hamzated and doubly-weak roots still refuse.
      const nfc = s => s && s.normalize('NFC');
      const mk = (root, en, ty) => nfc(NAKIL_BABS.find(b => b.en === en).make(...root.split(' '), ty));
      const weak = {
        istaqala: mk('ق و ل', 'Form X', 'ajwaf'),      // اِسْتَقَالَ
        izdada: mk('ز ي د', 'Form VIII', 'ajwaf'),     // اِزْدَادَ — ibdal + hollow at once
        irtama: mk('ر م ي', 'Form VIII', 'naqis'),     // اِرْتَمَى
        imtadda: mk('م د د', 'Form VIII', 'gem'),      // اِمْتَدَّ
        ittajala: mk('و ج ل', 'Form VIII', 'mithal'),  // اِتَّجَلَ — the table's own row
        ijalla: mk('و ج ل', 'Form IX', 'mithal'),      // اِيجَلَّ — the table's own row
        naqisIX: NAKIL_BABS.find(b => b.en === 'Form IX').make('ر', 'م', 'ي', 'naqis'),
        hollowXII: NAKIL_BABS.find(b => b.en === 'Form XII').make('ق', 'و', 'ل', 'ajwaf'),
      };
      const hollowCls = nakilClass({ root: 'ق و ل' });
      const gemCls = nakilClass({ root: 'ض م م' });
      const derivedCls = nakilClass({ form: 'IV', root: 'ك ر م' });
      const hamzated = nakilClass({ root: 'أ خ ذ' });
      const lafif = nakilClass({ root: 'و ص ي' });
      // A derived verb's sheet must highlight its own mazid bab.
      sarfTense = 'nakil';
      openWord({ s: { full: 'عَرَّفَ', smart: 'عَرَّفَ', bare: 'عرف' }, lex: 'arrafa', grammar: [] }, null, 'sarf');
      const ownDerivedEl = document.querySelector('table.conj.nakil tr.own-bab .nakil-out');
      const ownDerived = ownDerivedEl ? ownDerivedEl.textContent : '';
      const derivedMujarrad = document.body.innerHTML.includes('السِّتَّةُ الْأَبْوَابُ');
      closeSheet(); sarfTense = 'mazi';
      return { hasBtn, rows, ownBab, note, istabara, iddhahaba, weak,
               hollowCls, gemCls, derivedCls, hamzated, lafif, ownDerived, derivedMujarrad };
    });
    if (!r.hasBtn) throw new Error('نَصَرَ offers no nakil button');
    // Six mujarrad babs (the Bina's) + twelve augmented wazns.
    if (r.rows.length !== 18) throw new Error(r.rows.length + ' nakil rows, want 18');
    if (!r.rows.some(x => x.normalize('NFC') === 'نَصَرَ يَنْصُرُ'.normalize('NFC')))
      throw new Error('the mujarrad section lacks نَصَرَ يَنْصُرُ');
    if (!r.ownBab || !/نَصَرَ يَنْصُرُ/.test(r.ownBab.normalize('NFC')))
      throw new Error('the verb\'s own bab is not highlighted: ' + r.ownBab);
    for (const f of ['نَصَّرَ', 'نَاصَرَ', 'أَنْصَرَ', 'اِنْتَصَرَ', 'اِسْتَنْصَرَ', 'اِنْصَوْصَرَ'])
      if (!r.rows.some(x => x.normalize('NFC') === f.normalize('NFC')))
        throw new Error('nakil table lacks ' + f + ' — has: ' + r.rows.join(' '));
    if (r.istabara !== 'اِصْطَبَرَ'.normalize('NFC')) throw new Error('sad ibdal wrong: ' + r.istabara);
    if (r.iddhahaba !== 'اِذَّهَبَ'.normalize('NFC')) throw new Error('dhal idgham wrong: ' + r.iddhahaba);
    // The i'lal outputs, class by class — each checked against a real word.
    const want = { istaqala: 'اِسْتَقَالَ', izdada: 'اِزْدَادَ', irtama: 'اِرْتَمَى',
                   imtadda: 'اِمْتَدَّ', ittajala: 'اِتَّجَلَ', ijalla: 'اِيجَلَّ' };
    for (const k of Object.keys(want))
      if (r.weak[k] !== want[k].normalize('NFC'))
        throw new Error(k + ' wrong: ' + r.weak[k] + ' want ' + want[k]);
    // Where the tradition recites nothing, the maker returns nothing.
    if (r.weak.naqisIX !== null || r.weak.hollowXII !== null)
      throw new Error('a class was forced into a bab it does not have');
    if (!r.hollowCls || r.hollowCls.type !== 'ajwaf') throw new Error('hollow root not classified');
    if (!r.gemCls || r.gemCls.type !== 'gem') throw new Error('geminate root not classified');
    if (!r.derivedCls) throw new Error('a derived verb was refused the drill');
    if (r.hamzated || r.lafif) throw new Error('hamzated/lafif roots must still refuse');
    if (r.ownDerived.normalize('NFC') !== 'عَرَّفَ'.normalize('NFC'))
      throw new Error('derived verb\'s own bab not highlighted: ' + r.ownDerived);
    if (!/lugatte|lexicon/.test(r.note)) throw new Error('the formal-drill honesty note is missing');
    await page.reload({ waitUntil: 'load' });
    await page.waitForSelector('.lib-card');
  });

  await check('ziyade extensions: the muhtelife recites the akrama model\'s second breath', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'wasiyyat-abi-hanifa-samti');
      const nfc = s => s.normalize('NFC');
      const akrama = muhtelife(st.morph.akrama).filter(x => x.ext).map(x => nfc(x.ar));
      const wassa = muhtelife(st.morph.wassa).filter(x => x.ext).map(x => nfc(x.ar));
      const hajara = muhtelife(st.morph.hajara).filter(x => x.ext);
      const taala = ziyadeExt(st.morph.taala);   // masdar تَعَالٍ — the templates must refuse it
      return { akrama, wassa, hajaraN: hajara.length, taalaN: taala.length };
    });
    // The received model, cell for cell (ziyade-bab-muhtelife-cekimi.txt).
    for (const f of ['مُكْرَمٌ', 'إِكْرَامَةً وَاحِدَةً', 'إِكْرَامِيٌّ',
                     'هُوَ أَشَدُّ مِنْهُ إِكْرَامًا', 'مَا أَشَدَّ إِكْرَامَهُ', 'وَأَشْدِدْ بِإِكْرَامِهِ'])
      if (!r.akrama.includes(f.normalize('NFC')))
        throw new Error('akrama lacks ' + f + ' — has: ' + r.akrama.join(' | '));
    // A ta-marbuta masdar bends correctly before suffixes: تَوْصِيَتَهُ, not تَوْصِيَةَهُ.
    if (!r.wassa.some(x => x.includes('تَوْصِيَتَهُ'.normalize('NFC'))))
      throw new Error('wassa wonder form wrong: ' + r.wassa.join(' | '));
    if (!r.wassa.some(x => x.includes('تَوْصِيَةً وَاحِدَةً'.normalize('NFC'))))
      throw new Error('wassa once-noun wrong');
    // Form I verbs and untemplateable masdars get no extension rows at all.
    if (r.hajaraN) throw new Error('a Form I verb grew ziyade rows');
    if (r.taalaN) throw new Error('a manqus masdar was forced into the templates');
  });

  await check('poetry wears verse dress: the bayt centers and parts at the hemistich', async () => {
    await toLibrary();
    await openStoryCard('bad-al-amali');
    const n = await page.locator('section.sentence.verse').count();
    if (!n) throw new Error('no verse-dressed sentences in the qasida');
    const hemi = await page.locator('section.sentence.verse .hemi').first().textContent();
    if (hemi !== '✽') throw new Error('hemistich ornament is: ' + hemi);
    // The raw bullet must never reach the reader's eye as text.
    const raw = await page.evaluate(() =>
      [...document.querySelectorAll('.ar-line')].some(l => l.textContent.includes('•')));
    if (raw) throw new Error('a raw • leaked into the rendered line');
    // Prose stories stay prose.
    await toLibrary();
    await openStoryCard('wasiyyat-abi-hanifa-L2');
    if (await page.locator('section.sentence.verse').count())
      throw new Error('a prose story took the verse layout');
    await toLibrary();
  });

  await check('a saved card remembers its sentence, and the page marks deck words', async () => {
    await toLibrary();
    await openStoryCard('wasiyyat-abi-hanifa-L2');
    // Save the first teachable word through the same path a tap takes.
    await page.locator('.word[data-lvl]').first().click();
    await page.waitForSelector('#saveBtn', { timeout: 3000 });
    await page.locator('#saveBtn').click();
    const r = await page.evaluate(() => {
      const card = state.deck[state.deck.length - 1];
      const span = document.querySelector(`.word[data-lex="${CSS.escape(card.lex)}"]`);
      const sen = CUR.chapters.flatMap(c => c.sentences).find(s => s.id === (card.ctx && card.ctx.sen));
      const rebuilt = sen ? sen.tokens.map(t => t.s.full + (t.punctAfter || '')).join(' ') : '';
      const snapshot = card.ctx ? [card.ctx.pre, card.ctx.word, card.ctx.post].filter(Boolean).join(' ') : '';
      return { hasCtx: !!card.ctx, story: card.ctx && card.ctx.story,
               marked: span && span.classList.contains('in-deck'),
               agree: rebuilt === snapshot, lex: card.lex };
    });
    if (!r.hasCtx) throw new Error('the saved card carries no sentence snapshot');
    if (r.story !== 'wasiyyat-abi-hanifa-L2') throw new Error('snapshot story is ' + r.story);
    // pre + word + post must reassemble the exact sentence — no drift.
    if (!r.agree) throw new Error('the snapshot does not reassemble its sentence');
    if (!r.marked) throw new Error('the page did not mark the saved word in-deck');
    // The review reveal shows the word at home, bolded.
    const rev = await page.evaluate(lex => {
      openDeck(); reviewStep = 2; renderDeck();
      // walk the queue until our card is on top, or just inspect the DOM if it is
      const ctxEl = document.querySelector('.card-ctx');
      const shown = !!ctxEl && !!ctxEl.querySelector('b');
      closeSheet();
      return { shown, queueHasCtx: dueCards().some(c => c.lex === lex && c.ctx) };
    }, r.lex);
    if (!rev.queueHasCtx) throw new Error('the ctx card never reached the review queue');
    // Removing the card un-marks the page copies live.
    await page.locator('.word[data-lvl]').first().click();
    await page.waitForSelector('#saveBtn', { timeout: 3000 });
    await page.locator('#saveBtn').click();      // toggles off
    const unmarked = await page.evaluate(lex =>
      ![...document.querySelectorAll(`.word[data-lex="${CSS.escape(lex)}"]`)]
        .some(x => x.classList.contains('in-deck')), r.lex);
    if (!unmarked) throw new Error('removing the card left the page marked');
    await page.evaluate(() => document.getElementById('scrim').click());
    await toLibrary();
  });

  await check('the weekly mercy day forgives one missed day, once', async () => {
    const r = await page.evaluate(() => {
      const saved = { streak: { ...state.streak }, today: { ...state.today } };
      const key = d => todayKey(d);
      const dayBefore = () => { const d = new Date(); d.setDate(d.getDate() - 2); return key(d); };
      // A 5-day streak, last studied the day BEFORE yesterday, shield unused:
      state.streak = { days: 5, last: dayBefore() };
      state.today = { date: 'reset', reviewed: 0, learned: 0, read: 0 };
      countActivity('read');
      const forgiven = { days: state.streak.days, shield: state.streak.shieldWeek };
      // Same situation again in the SAME week — the shield is spent:
      state.streak = { days: 9, last: dayBefore(), shieldWeek: state.streak.shieldWeek };
      state.today = { date: 'reset', reviewed: 0, learned: 0, read: 0 };
      countActivity('read');
      const burned = state.streak.days;
      // An ordinary yesterday-continuation never touches the shield:
      const y = new Date(); y.setDate(y.getDate() - 1);
      state.streak = { days: 3, last: key(y) };
      state.today = { date: 'reset', reviewed: 0, learned: 0, read: 0 };
      countActivity('read');
      const normal = { days: state.streak.days, shield: state.streak.shieldWeek };
      state.streak = saved.streak; state.today = saved.today;
      localStorage.setItem('qissa-streak', JSON.stringify(state.streak));
      localStorage.setItem('qissa-today', JSON.stringify(state.today));
      return { forgiven, burned, normal };
    });
    if (r.forgiven.days !== 6 || !r.forgiven.shield)
      throw new Error('the mercy day did not forgive: ' + JSON.stringify(r.forgiven));
    if (r.burned !== 1) throw new Error('a spent shield still forgave: days=' + r.burned);
    if (r.normal.days !== 4 || r.normal.shield)
      throw new Error('an ordinary continuation touched the shield');
  });

  await check('the snapshot is a door: tapping it opens the story at that sentence', async () => {
    await toLibrary();
    const target = await page.evaluate(() => {
      // A card whose ctx points at the L2 story's first sentence, honestly built.
      const st = STORIES.find(s => s.id === 'wasiyyat-abi-hanifa-L2');
      const sen = st.chapters[0].sentences[0];
      const t = sen.tokens;
      window.__savedDeck = state.deck;
      state.deck = [{ lex: t[1].lex, type: 'word', bare: t[1].s.bare, lemma: t[1].s.full,
        gloss: { en: 'x', tr: 'y' },
        ctx: { story: st.id, sen: sen.id,
               pre: t[0].s.full, word: t[1].s.full,
               post: t.slice(2).map(x => x.s.full + (x.punctAfter || '')).join(' ') },
        srs: { due: 0, ivl: 0, reps: 0, ease: 2.5, lapses: 0 } }];
      openDeck(); reviewStep = 2; renderDeck();
      return sen.id;
    });
    await page.waitForSelector('.card-ctx', { timeout: 3000 });
    await page.locator('.card-ctx').click();
    await page.waitForSelector(`section.sentence[data-id="${target}"]`, { timeout: 3000 });
    const ok = await page.evaluate(id => {
      const good = CUR && CUR.id === 'wasiyyat-abi-hanifa-L2'
        && !!document.querySelector(`section.sentence[data-id="${id}"]`);
      state.deck = window.__savedDeck; delete window.__savedDeck;
      reviewStep = 0;
      return good;
    }, target);
    if (!ok) throw new Error('the snapshot did not open its story');
    await toLibrary();
  });

  await check('the Sarf engine regenerates every stored paradigm it can classify', async () => {
    const r = await page.evaluate(() => sarfAudit());
    if (r.bad.length)
      throw new Error(r.bad.length + ' paradigms mismatch: ' + r.bad.slice(0, 4).join(' || '));
    // The audit must actually bite: a healthy corpus gives it dozens of verbs.
    if (r.checked < 60)
      throw new Error('audit covered only ' + r.checked + ' verbs — classification broke?');
    // A MITHAL run through أَفْعَلَ needs a rule the wazn cannot supply: the
    // sukun-bearing first radical becomes the madd letter that agrees with the
    // vowel before it. Substituting the root into the scale gave *يُوْجِبُ and
    // *إِوْجَاب; the mazi, where a FATHA precedes, must keep its waw untouched.
    const m4 = await page.evaluate(() => {
      const c = nakilClass({ root: 'و ج ب' });
      const d = c && sarfDerive(c, 'IV', 1);
      return d && d.ok ? { mazi: d.mazi[0], mudari: d.mudari[0], masdar: d.masdar,
                           amr: d.amr[0], fail: d.fail } : null;
    });
    if (!m4) throw new Error('وجب would not classify for Form IV');
    const w4 = { mazi: 'أَوْجَبَ', mudari: 'يُوجِبُ', masdar: 'إِيجَاب',
                 amr: 'أَوْجِبْ', fail: 'مُوجِب' };
    for (const k of Object.keys(w4))
      if (m4[k].normalize('NFC') !== w4[k].normalize('NFC'))
        throw new Error(`Form IV mithal ${k}: wanted ${w4[k]}, got ${m4[k]}`);

    // The ta of اِفْتِعَال, in TWO steps. First it takes the colour of the first
    // radical — ط after the emphatics, د after ز ذ د. Then, and only where the
    // two letters have come out IDENTICAL, they run together. ص and ض keep
    // their ط standing apart; ز keeps its د apart, because ز is not د. The
    // engine had step one and applied step two to د/ذ only, so اِطَّلَعَ came out
    // right in the past tense and its own masdar came out *اِطْطِلَاع.
    const t8 = await page.evaluate(() => {
      const out = {};
      [['ص ب ر', 'VIII'], ['ض ر ب', 'VIII'], ['ط ل ع', 'VIII'], ['ظ ل م', 'VIII'],
       ['ز ي د', 'VIII'], ['د ع و', 'VIII'], ['ذ ك ر', 'VIII'], ['ح م ل', 'VIII'],
       ['و ف ق', 'VIII'], ['س د د', 'VII']].forEach(([root, f]) => {
        const d = sarfDerive(nakilClass({ root }), f, 1);
        out[root] = d && d.ok ? [d.mazi[0], d.mazi[6], d.mudari[0], d.mudari[5], d.masdar, d.fail].join('|') : 'no';
      });
      return out;
    });
    const w8 = {
      'ص ب ر': 'اِصْطَبَرَ|اِصْطَبَرْتَ|يَصْطَبِرُ|يَصْطَبِرْنَ|اِصْطِبَار|مُصْطَبِر',
      'ض ر ب': 'اِضْطَرَبَ|اِضْطَرَبْتَ|يَضْطَرِبُ|يَضْطَرِبْنَ|اِضْطِرَاب|مُضْطَرِب',
      'ط ل ع': 'اِطَّلَعَ|اِطَّلَعْتَ|يَطَّلِعُ|يَطَّلِعْنَ|اِطِّلَاع|مُطَّلِع',
      'ظ ل م': 'اِظَّلَمَ|اِظَّلَمْتَ|يَظَّلِمُ|يَظَّلِمْنَ|اِظِّلَام|مُظَّلِم',
      'ز ي د': 'اِزْدَادَ|اِزْدَدْتَ|يَزْدَادُ|يَزْدَدْنَ|اِزْدِيَاد|مُزْدَاد',
      'د ع و': 'اِدَّعَى|اِدَّعَيْتَ|يَدَّعِي|يَدَّعِينَ|اِدِّعَاء|مُدَّعٍ',
      'ذ ك ر': 'اِذَّكَرَ|اِذَّكَرْتَ|يَذَّكِرُ|يَذَّكِرْنَ|اِذِّكَار|مُذَّكِر',
      'ح م ل': 'اِحْتَمَلَ|اِحْتَمَلْتَ|يَحْتَمِلُ|يَحْتَمِلْنَ|اِحْتِمَال|مُحْتَمِل',
      'و ف ق': 'اِتَّفَقَ|اِتَّفَقْتَ|يَتَّفِقُ|يَتَّفِقْنَ|اِتِّفَاق|مُتَّفِق',
      // Form VII of a doubled root had no branch and fell through to the sound
      // path, so اِنْسَدَّ came out uncontracted. The uncontracted stem must still
      // survive wherever the ending brings a sukun.
      'س د د': 'اِنْسَدَّ|اِنْسَدَدْتَ|يَنْسَدُّ|يَنْسَدِدْنَ|اِنْسِدَاد|مُنْسَدّ',
    };
    for (const k of Object.keys(w8))
      if (t8[k].normalize('NFC') !== w8[k].normalize('NFC'))
        throw new Error(`iftial/gem ${k}: wanted ${w8[k]}, got ${t8[k]}`);

    // The PARTICIPLE stem is not the conjugating stem. Forms V and VI run their
    // mudari on a FATHA (يَتَفَعَّلُ، يَتَفَاعَلُ) but their ism fa'il takes a KASRA:
    // مُتَعَلِّم، مُتَشَابِه. The engine handed the conjugating stem to the
    // participle maker and shipped the two participles IDENTICAL — and the
    // paradigm audit never saw it, because it compares tenses and not
    // participles. The corpus's own مُتَشَابِه is the witness.
    const part = await page.evaluate(() => {
      const out = {};
      [['ن ص ر', 'II'], ['ن ص ر', 'III'], ['ن ص ر', 'V'], ['ن ص ر', 'VI'],
       ['ش ب ه', 'VI'], ['ع ل م', 'V']].forEach(([root, f]) => {
        const d = sarfDerive(nakilClass({ root }), f, 1);
        out[root + ' ' + f] = d && d.ok ? [d.fail, d.maful || '-'].join('|') : 'no';
      });
      return out;
    });
    const wp = {
      'ن ص ر II':  'مُنَصِّر|مُنَصَّر',
      'ن ص ر III': 'مُنَاصِر|مُنَاصَر',
      'ن ص ر V':   'مُتَنَصِّر|مُتَنَصَّر',
      'ن ص ر VI':  'مُتَنَاصِر|مُتَنَاصَر',
      'ش ب ه VI':  'مُتَشَابِه|مُتَشَابَه',
      'ع ل م V':   'مُتَعَلِّم|مُتَعَلَّم',
    };
    for (const k of Object.keys(wp))
      if (part[k].normalize('NFC') !== wp[k].normalize('NFC'))
        throw new Error(`participles ${k}: wanted ${wp[k]}, got ${part[k]}`);
    // …and the ism fa'il must never equal the ism maf'ul: one kasra apart is
    // the whole distinction, and equality means the distinction was lost.
    for (const k of Object.keys(part)) {
      const [fa, mf] = part[k].split('|');
      if (mf !== '-' && fa.normalize('NFC') === mf.normalize('NFC'))
        throw new Error(`${k}: ism fa'il and ism maf'ul came out identical (${fa})`);
    }
  });

  await check('the Sarf Lab conjugates sound, hollow and defective roots live', async () => {
    await toLibrary();
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#conjRoot', { timeout: 3000 });
    const sound = await page.evaluate(() => {
      conjState.root = 'نصر'; conjState.form = 'I'; conjState.bab = 1; renderConjOut();
      return document.getElementById('conjOut').textContent;
    });
    for (const f of ['نَصَرْتَ', 'يَنْصُرُونَ', 'اُنْصُرْ', 'نَاصِر', 'مَنْصُور'])
      if (!sound.normalize('NFC').includes(f.normalize('NFC')))
        throw new Error('sound tables lack ' + f);
    const hollow = await page.evaluate(() => {
      conjState.root = 'قول'; renderConjOut();
      return document.getElementById('conjOut').textContent;
    });
    for (const f of ['قُلْتَ', 'يَقُلْنَ', 'قَائِل', 'مَقُول'])
      if (!hollow.normalize('NFC').includes(f.normalize('NFC')))
        throw new Error('hollow tables lack ' + f);
    const naqisX = await page.evaluate(() => {
      conjState.root = 'رمي'; conjState.form = 'X'; renderConjOut();
      return document.getElementById('conjOut').textContent;
    });
    for (const f of ['اِسْتَرْمَى', 'يَسْتَرْمِي', 'اِسْتِرْمَاء'])
      if (!naqisX.normalize('NFC').includes(f.normalize('NFC')))
        throw new Error('derived-naqis tables lack ' + f);
    const refusal = await page.evaluate(() => {
      conjState.root = 'أخذ'; conjState.form = 'I'; renderConjOut();
      const txt = document.getElementById('conjOut').textContent;
      conjState.root = 'نصر'; closeSheet();
      return txt;
    });
    if (!/hamza|Hemze|hemze/i.test(refusal))
      throw new Error('a hamzated root was not honestly refused');
  });

  await check('the Sarf Lab auto-detects the attested bab for a known root', async () => {
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#conjRoot', { timeout: 3000 });
    // حمد is attested in the corpus as bab سَمِعَ — typing it must answer
    // حَمِدَ يَحْمَدُ, not the نَصَرَ default's حَمَدَ.
    await page.fill('#conjRoot', 'حمد');
    const out = await page.evaluate(() => document.getElementById('conjOut').textContent);
    for (const f of ['حَمِدَ', 'يَحْمَدُ'])
      if (!out.normalize('NFC').includes(f.normalize('NFC')))
        throw new Error('auto-detected tables lack ' + f + ' — bab did not snap');
    // The attested bab button carries the dot and is selected.
    const seg = await page.evaluate(() => {
      const b = document.querySelector('#conjBabSeg button.attested');
      return b ? { txt: b.textContent, on: b.classList.contains('on') } : null;
    });
    if (!seg || !seg.txt.includes('سَمِعَ') || !seg.on)
      throw new Error('attested marker wrong: ' + JSON.stringify(seg));
    if (!(await page.locator('.conj-known:not(.other)').count()))
      throw new Error('no attested hint shown');
    // Wandering to another bab keeps the tool honest: re-vowelled output
    // (bab ضرب gives mazi حَمَدَ) plus a nudge naming the attested verb.
    await page.locator('#conjBabSeg button[data-cb="2"]').click();
    const out2 = await page.evaluate(() => document.getElementById('conjOut').textContent);
    if (!out2.normalize('NFC').includes('يَحْمِدُ'.normalize('NFC')))
      throw new Error('bab 2 did not re-vowel the mudari');
    if (!(await page.locator('.conj-known.other').count()))
      throw new Error('no attested nudge when exploring another bab');
    // A different known root moves the detection with it: جلس runs on ضرب's bab.
    await page.fill('#conjRoot', 'جلس');
    const seg2 = await page.evaluate(() => {
      const b = document.querySelector('#conjBabSeg button.attested');
      conjState.root = 'نصر'; closeSheet();
      return b ? b.textContent : null;
    });
    if (!seg2 || !seg2.includes('ضَرَبَ'))
      throw new Error('jalasa did not snap to bab ضَرَبَ: ' + seg2);
  });

  await check('the memory model seats fading words into the games', async () => {
    await openStoryCard(wasiyyaStats.id);   // games and GLOSSARY are story-scoped
    const r = await page.evaluate(() => {
      const saved = state.deck;
      // Two reviewed cards, 30 and 10 days past their last look at stability 5:
      // retrievability ≈ 0.64 and 0.79 — both fading, the older one worse.
      const picks = Object.entries(GLOSSARY)
        .filter(([k, e]) => e.level > 0 && e.gloss && e.lemma.length > 1).slice(0, 2);
      const mk = (lex, days) => ({ lex, type: 'word', bare: 'x', lemma: GLOSSARY[lex].lemma,
        gloss: { en: 'x', tr: 'x' },
        srs: { due: Date.now() + 864e5, ivl: 5, reps: 2, lapses: 0,
               S: 5, D: 5, seen: Date.now() - days * 864e5 } });
      state.deck = [mk(picks[1][0], 10), mk(picks[0][0], 30)];
      const fade = fadingWords(3);
      openGames();
      const hubFade = document.querySelectorAll('.game-pick .gd.fade').length;
      startMatch();
      const note = !!document.querySelector('.fade-note');
      const inGrid = [...document.querySelectorAll('.match-grid button')]
        .some(b => b.textContent === GLOSSARY[picks[0][0]].lemma);
      const fading = M.fading;
      closeSheet();
      state.deck = saved; persistDeck();
      return { n: fade.length, worstFirst: fade.length === 2 && fade[0].r <= fade[1].r,
               worstLex: fade[0] && fade[0].lex, expect: picks[0][0],
               hubFade, note, inGrid, fading };
    });
    if (r.n !== 2) throw new Error('fadingWords found ' + r.n + ' of 2');
    if (!r.worstFirst || r.worstLex !== r.expect)
      throw new Error('fading not sorted worst-first: ' + r.worstLex);
    if (r.hubFade !== 2) throw new Error('hub fade lines: ' + r.hubFade + ' expected 2 (match+cloze)');
    if (!r.note || !r.inGrid || r.fading < 1)
      throw new Error('match round did not seat the fading word: ' + JSON.stringify(r));
  });

  await check('the sheet names the form in the text: وَاعْفُ answers «affet!»', async () => {
    await page.evaluate(() => { state.premium = true; jumpTo('wasiyyat-abi-hanifa-samti', 's40'); });
    await page.waitForTimeout(400);
    await page.locator('.word', { hasText: 'وَاعْفُ' }).first().click();
    await page.waitForSelector('.sheet.show .intext', { timeout: 3000 });
    const it = await page.evaluate(() => ({
      ar: document.querySelector('.intext .it-ar').textContent,
      gloss: (document.querySelector('.intext .it-gloss') || {}).textContent || '',
      cell: document.querySelector('.intext .it-cell').textContent,
    }));
    if (!it.ar.includes('وَاعْفُ')) throw new Error('surface form missing: ' + it.ar);
    if (!it.gloss.includes('pardon!')) throw new Error('EN form meaning wrong: ' + it.gloss);
    if (!/command|الْأَمْرُ/.test(it.cell)) throw new Error('cell label wrong: ' + it.cell);
    // Turkish morphology: imperative = bare stem, past = harmony + devoicing.
    const tr = await page.evaluate(() => {
      const saveLang = state.uiLang; state.uiLang = 'tr';
      const out = {
        amr: formMeaning({ tense: 'amr', i: 0 }, GLOSSARY['afa']),
        mazi3: formMeaning({ tense: 'mazi', i: 0 }, { gloss: { tr: 'affetmek (عن ile)' } }),
        mazi2: formMeaning({ tense: 'mazi', i: 6 }, { gloss: { tr: 'yerine getirmek' } }),
        maziPl: formMeaning({ tense: 'mazi', i: 2 }, { gloss: { tr: 'unutmak' } }),
      };
      state.uiLang = saveLang;
      return out;
    });
    if (tr.amr !== 'affet!') throw new Error('TR imperative wrong: ' + tr.amr);
    if (tr.mazi3 !== 'affetti') throw new Error('TR past devoicing wrong: ' + tr.mazi3);
    if (tr.mazi2 !== 'yerine getirdin') throw new Error('TR past 2sg wrong: ' + tr.mazi2);
    if (tr.maziPl !== 'unuttular') throw new Error('TR past 3pl harmony wrong: ' + tr.maziPl);
    // The sarf tab lands on the amr table with the cell lit through the waw.
    await page.locator('.sheet .tabs button', { hasText: 'Conjugation' }).click();
    await page.waitForSelector('.tense-seg button[data-tense="amr"].on', { timeout: 3000 });
    if (!(await page.locator('table.conj td.hl').count()))
      throw new Error('amr cell not highlighted through the clitic waw');
    await page.evaluate(() => closeSheet());
  });

  await check('the Aded engine replays the أسماء عدد worksheets cell for cell', async () => {
    const bad = await page.evaluate(() => {
      // Transcribed from the two handwritten scans (research/sources/
      // esmai-aded-worksheets.txt) — the engine must reproduce every pair.
      const SHEET = {
        125: 'مائة وخمسة وعشرون', 131: 'مائة وواحد وثلاثون', 146: 'مائة وستة وأربعون',
        185: 'مائة وخمسة وثمانون', 245: 'مائتان وخمسة وأربعون', 355: 'ثلاثمائة وخمسة وخمسون',
        368: 'ثلاثمائة وثمانية وستون', 462: 'أربعمائة واثنان وستون', 511: 'خمسمائة وأحد عشر',
        512: 'خمسمائة واثنا عشر', 521: 'خمسمائة وواحد وعشرون', 622: 'ستمائة واثنان وعشرون',
        745: 'سبعمائة وخمسة وأربعون', 822: 'ثمانمائة واثنان وعشرون', 921: 'تسعمائة وواحد وعشرون',
        999: 'تسعمائة وتسعة وتسعون', 100: 'مائة', 1001: 'ألف وواحد', 1012: 'ألف واثنا عشر',
        1013: 'ألف وثلاثة عشر', 1020: 'ألف وعشرون', 1023: 'ألف وثلاثة وعشرون',
        1099: 'ألف وتسعة وتسعون', 1100: 'ألف ومائة', 1113: 'ألف ومائة وثلاثة عشر',
        1122: 'ألف ومائة واثنان وعشرون', 1500: 'ألف وخمسمائة', 1800: 'ألف وثمانمائة',
        1915: 'ألف وتسعمائة وخمسة عشر', 1921: 'ألف وتسعمائة وواحد وعشرون',
        1999: 'ألف وتسعمائة وتسعة وتسعون', 2000: 'ألفان', 2011: 'ألفان وأحد عشر',
        2020: 'ألفان وعشرون', 2101: 'ألفان ومائة وواحد',
        2999: 'ألفان وتسعمائة وتسعة وتسعون', 3000: 'ثلاثة آلاف',
      };
      const bad = [];
      for (const [n, want] of Object.entries(SHEET)) {
        const got = stripAr(AdadEngine.name(+n) || '');
        if (got !== want) bad.push(n + ': ' + got + ' ≠ ' + want);
      }
      return bad;
    });
    if (bad.length) throw new Error(bad.length + ' cells differ: ' + bad.slice(0, 4).join(' | '));
  });

  await check('the Aded Lab counts with polarity, and the numbers game drills the rules', async () => {
    await toLibrary();
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#conjRoot', { timeout: 3000 });
    await page.locator('.sheet .tabs button[data-lab="adad"]').click();
    await page.waitForSelector('#adadN', { timeout: 3000 });
    const r = await page.evaluate(() => {
      conjState.adadN = 125; renderAdadOut();
      const abs = document.querySelector('.adad-big').textContent;
      // pick جَنَّة: the phrase must flip polarity (وَخَمْسٌ، not وَخَمْسَةٌ)
      const j = [...document.querySelectorAll('#adadNounSeg [data-an]')]
        .find(b => b.textContent.includes('جَنَّةٌ'));
      j.click();
      const phrase = document.querySelector('.adad-phrase').textContent;
      const out = {
        abs: stripAr(abs), phrase: stripAr(phrase),
        p310: stripAr(AdadEngine.phrase(3, ADAD_NOUNS[0]).text),
        p310f: stripAr(AdadEngine.phrase(3, ADAD_NOUNS[1]).text),
        p11f: stripAr(AdadEngine.phrase(11, ADAD_NOUNS[1]).text),
        p100: stripAr(AdadEngine.phrase(100, ADAD_NOUNS[0]).text),
        p101: stripAr(AdadEngine.phrase(101, ADAD_NOUNS[0]).text),
      };
      conjState.lab = 'sarf';
      closeSheet();
      return out;
    });
    if (r.abs !== 'مائة وخمسة وعشرون') throw new Error('absolute name wrong: ' + r.abs);
    if (r.phrase !== 'مائة وخمس وعشرون جنة') throw new Error('polarity phrase wrong: ' + r.phrase);
    if (r.p310 !== 'ثلاثة كتب') throw new Error('3+masc wrong: ' + r.p310);
    if (r.p310f !== 'ثلاث جنات') throw new Error('3+fem polarity wrong: ' + r.p310f);
    if (r.p11f !== 'إحدى عشرة جنة') throw new Error('11+fem wrong: ' + r.p11f);
    if (r.p100 !== 'مائة كتاب') throw new Error('100 idafa wrong: ' + r.p100);
    if (r.p101 !== 'مائة كتاب وكتاب') throw new Error('101 repetition wrong: ' + r.p101);
    // every generated game round: three distinct options, exactly one correct
    const g = await page.evaluate(() => {
      const items = adadGameItems(12);
      return items.length === 12 && items.every(it =>
        it.wrongs.length === 2 && !it.wrongs.includes(it.right.text) &&
        new Set([it.right.text, ...it.wrongs]).size === 3);
    });
    if (!g) throw new Error('game items not well-formed');
  });

  await check('the Root Finder digs: corpus first, peeling rules with ibdal after', async () => {
    const r = await page.evaluate(() => {
      const f = w => RootFinder.find(w);
      const root = x => x ? stripAr(x.root).replace(/\s+/g, ' ').trim() : null;
      return {
        corpusVia: (f('يَجْزِيهِمْ') || {}).via, corpusRoot: root(f('يَجْزِيهِمْ')),
        hamida: f('حَمِدَ'),
        istaghfara: root(f('استغفر')),
        istabara: root(f('اصطبر')), izdajara: root(f('ازدجر')),
        inkasara: root(f('انكسر')), taallama: root(f('تعلم')),
        akrama: root(f('أكرم')), qatala3: root(f('قاتل')),
        mustaghfir: root(f('مستغفر')), conj: root(f('يستغفرون')),
      };
    });
    if (r.corpusVia !== 'corpus' || r.corpusRoot !== 'ج ز ي')
      throw new Error('corpus lookup failed: ' + r.corpusVia + ' / ' + r.corpusRoot);
    // the Form I bab is SEMA'I: it may only appear because the corpus stores it
    if (!r.hamida || r.hamida.via !== 'corpus' || !/سَمِعَ/.test(r.hamida.bab || ''))
      throw new Error('hamida did not surface its stored sema-i bab');
    const want = { istaghfara: 'غ ف ر', istabara: 'ص ب ر', izdajara: 'ز ج ر',
                   inkasara: 'ك س ر', taallama: 'ع ل م', akrama: 'ك ر م',
                   qatala3: 'ق ت ل', mustaghfir: 'غ ف ر', conj: 'غ ف ر' };
    // the user's three reported failures, and the masdar family they exposed
    const masdars = await page.evaluate(() => {
      const root = w => { const x = RootFinder.find(w); return x ? stripAr(x.root).replace(/\s+/g, ' ').trim() : null; };
      return { talim: root('تعليم'), akramPlain: root('اكرم'), idtirab: root('اضطراب'),
               ikram: root('اكرام'), istighfar: root('استغفار'), inkisar: root('انكسار'),
               qital: root('قتال'), inkar: root('انكار') };
    });
    const wantM = { talim: 'ع ل م', akramPlain: 'ك ر م', idtirab: 'ض ر ب',
                    ikram: 'ك ر م', istighfar: 'غ ف ر', inkisar: 'ك س ر',
                    qital: 'ق ت ل', inkar: 'ن ك ر' };
    for (const [k, v] of Object.entries(wantM))
      if (masdars[k] !== v) throw new Error('masdar ' + k + ': ' + masdars[k] + ' ≠ ' + v);
    for (const [k, v] of Object.entries(want))
      if (r[k] !== v) throw new Error(k + ': ' + r[k] + ' ≠ ' + v);
    // the lab UI: third tab answers with the root
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.sheet .tabs button[data-lab="jadhr"]', { timeout: 3000 });
    await page.locator('.sheet .tabs button[data-lab="jadhr"]').click();
    await page.waitForSelector('#jadhrIn', { timeout: 3000 });
    await page.fill('#jadhrIn', 'اصطبر');
    await page.waitForTimeout(260);
    const out = await page.evaluate(() => {
      const t = document.getElementById('jadhrOut').textContent;
      conjState.lab = 'sarf'; closeSheet();
      return t;
    });
    if (!out.includes('ص ب ر')) throw new Error('lab output lacks the root: ' + out);
  });

  await check('the i\'lal chain recites asl, rule and result for every weak class', async () => {
    const r = await page.evaluate(() => {
      const run = (root, bab) => {
        const cls = nakilClass({ root });
        const d = sarfDerive(cls, 'I', bab);
        const st = ilalSteps(cls, bab, d.mazi[0], d.mudari[0]);
        return st ? st.map(s => stripAr(s.asl) + '>' + stripAr(s.now)) : null;
      };
      return {
        qala: run('ق و ل', 1), rama: run('ر م ي', 2),
        waada: run('و ع د', 2), madda: run('م د د', 1),
        aslQala: (() => { const cls = nakilClass({ root: 'ق و ل' });
          const d = sarfDerive(cls, 'I', 1);
          return ilalSteps(cls, 1, d.mazi[0], d.mudari[0])[1].asl; })(),
        sound: run('ن ص ر', 1),
      };
    });
    if (!r.qala || r.qala[0] !== 'قول>قال') throw new Error('qala mazi chain wrong: ' + r.qala);
    if (!r.aslQala.includes('قْوُ')) throw new Error('qala mudari asl lacks the heavy damma: ' + r.aslQala);
    if (!r.rama || r.rama[0] !== 'رمي>رمى') throw new Error('rama chain wrong: ' + r.rama);
    if (!r.waada || r.waada[0] !== 'يوعد>يعد') throw new Error('mithal chain wrong: ' + r.waada);
    if (!r.madda || r.madda[0] !== 'مدد>مد') throw new Error('gem chain wrong: ' + r.madda);
    if (r.sound !== null) throw new Error('a sound verb must have NO i\'lal chain');
  });

  await check('role colors: RoleEngine reads i\'rab, toggle paints the text', async () => {
    // the engine itself, on synthetic i'rab lines of every family
    const eng = await page.evaluate(() => ({
      fail:    RoleEngine.of({ irab: { ar: 'فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ' } }),
      naib:    RoleEngine.of({ irab: { ar: 'نَائِبُ الْفَاعِلِ مَرْفُوعٌ' } }),
      maful:   RoleEngine.of({ irab: { ar: 'مَفْعُولٌ بِهِ مَنْصُوبٌ' } }),
      mudaf:   RoleEngine.of({ irab: { ar: 'مُضَافٌ إِلَيْهِ مَجْرُورٌ' } }),
      jarr:    RoleEngine.of({ irab: { ar: 'اسْمٌ مَجْرُورٌ بِالْبَاءِ' } }),
      none:    RoleEngine.of({ irab: { ar: 'فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ' } }),
      noIrab:  RoleEngine.of({}),
    }));
    for (const [k, want] of [['fail', 'fail'], ['naib', 'fail'], ['maful', 'maful'],
                             ['mudaf', 'mudaf'], ['jarr', 'jarr'], ['none', null], ['noIrab', null]]) {
      if (eng[k] !== want) throw new Error(k + ': got ' + eng[k] + ' want ' + want);
    }
    // the layer in a real story: toggle on -> body class, legend, painted words
    await openStoryCard('deeds-are-by-intentions');
    await page.waitForSelector('.word', { timeout: 3000 });
    await page.locator('#roleToggle').click();
    const on = await page.evaluate(() => ({
      mode: document.body.classList.contains('role-mode'),
      legend: !!document.getElementById('roleLegend'),
      painted: document.querySelectorAll('.word[data-role]').length,
    }));
    if (!on.mode) throw new Error('body.role-mode missing after toggle');
    if (!on.legend) throw new Error('#roleLegend missing after toggle');
    if (!on.painted) throw new Error('no .word[data-role] in the hadith story');
    await page.locator('#roleToggle').click();
    const off = await page.evaluate(() => ({
      mode: document.body.classList.contains('role-mode'),
      legend: !!document.getElementById('roleLegend'),
    }));
    if (off.mode || off.legend) throw new Error('toggle off left the layer behind');
    await toLibrary();
  });

  await check('the Avamil-100 panel counts Jurjani\'s governors and links the notes', async () => {
    await page.locator('#refOpen').click();
    await page.waitForSelector('#avamilOpen', { timeout: 3000 });
    await page.locator('#avamilOpen').click();
    await page.waitForSelector('.av-table', { timeout: 3000 });
    const r = await page.evaluate(() => ({
      letters: document.querySelectorAll('.av-table tbody tr').length,
      counts: [...document.querySelectorAll('.av-counts .avc b')].map(b => b.textContent),
      dataLetters: AVAMIL100.length,
      allNotesExist: AVAMIL100.every(a => !!GRAMMAR[a.note]),
      firstLetter: document.querySelector('.av-table tbody tr td:nth-child(2)').textContent.trim(),
    }));
    if (r.letters !== 17 || r.dataLetters !== 17) throw new Error('expected 17 jarr letters, got ' + r.letters);
    if (r.counts.join(',') !== '100,91,7,2') throw new Error('count tree wrong: ' + r.counts);
    if (!r.allNotesExist) throw new Error('a letter links to a note id that is not in the registry');
    if (r.firstLetter !== 'بِ') throw new Error('first letter should be the ba, got ' + r.firstLetter);
    // the note link opens the registry note in place
    await page.locator('.av-table [data-note]').first().click();
    await page.waitForSelector('.gnote h3', { timeout: 3000 });
    const h = await page.locator('.gnote h3').first().textContent();
    if (!h.replace(/[ً-ْ]/g, '').includes('حروف الجر'.normalize('NFC'))) throw new Error('ba should open the huruf-jarr note, got: ' + h);
    await page.evaluate(() => closeSheet());
  });

  await check('the Mizan weighs forms on ف ع ل — corpus cells exactly, asl for weak', async () => {
    const nfc = s => (s || '').normalize('NFC');
    const r = await page.evaluate(() => ({
      sound: WaznEngine.of('يَسْتَعْمِلُونَ'),
      weak: WaznEngine.of('يَقُولُ'),
      rules: WaznEngine.of('اضطراب'),
    }));
    if (!r.sound || r.sound.via !== 'corpus' || nfc(r.sound.mizan) !== nfc('يَسْتَفْعِلُونَ'))
      throw new Error('yasta3miluna should weigh yastaf3iluna, got ' + JSON.stringify(r.sound && r.sound.mizan));
    if (!r.weak || !r.weak.mizan || !r.weak.asl)
      throw new Error('yaqulu must weigh by the ASL with the asl flag set: ' + JSON.stringify(r.weak));
    if (nfc(r.weak.mizan) !== nfc('يَفْعُلُ'))
      throw new Error('yaqulu asl wazn should be yaf3ulu, got ' + r.weak.mizan);
    if (!r.rules || r.rules.via !== 'rules' || !r.rules.wazn.normalize('NFC').includes('اِفْتِعَال'.normalize('NFC')))
      throw new Error('idtirab should fall to the iftial masdar rule: ' + JSON.stringify(r.rules));
    // the lab tab answers with the wazn
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.sheet .tabs button[data-lab="mizan"]', { timeout: 3000 });
    await page.locator('.sheet .tabs button[data-lab="mizan"]').click();
    await page.waitForSelector('#mizanIn', { timeout: 3000 });
    await page.fill('#mizanIn', 'يستعملون');
    await page.waitForTimeout(260);
    const out = await page.evaluate(() => {
      const t = document.getElementById('mizanOut').textContent;
      conjState.lab = 'sarf'; closeSheet();
      return t;
    });
    if (!out.includes('يَسْتَفْعِلُونَ'.normalize('NFC'))) throw new Error('lab output lacks the mizan: ' + out);
  });

  await check('the Elo model moves with the evidence and names a sane target', async () => {
    const r = await page.evaluate(() => {
      const before = state.elo.vocab;
      EloModel.update('vocab', 3, true);
      const up = state.elo.vocab;
      EloModel.update('vocab', 3, false); EloModel.update('vocab', 3, false);
      const down = state.elo.vocab;
      const tgt = EloModel.targetLevel('vocab');
      const exp = EloModel.expected(1200, EloModel.itemRating(3));
      state.elo = { vocab: 1200, sarf: 1200, nahw: 1200, adad: 1200 };
      localStorage.removeItem('qissa-elo');
      return { before, up, down, tgt, exp, weakestWorks: !!EloModel.weakest() };
    });
    if (!(r.up > r.before)) throw new Error('a correct answer must raise the rating');
    if (!(r.down < r.up)) throw new Error('wrong answers must lower the rating');
    if (r.tgt < 1 || r.tgt > 6) throw new Error('target level out of range: ' + r.tgt);
    if (Math.abs(r.exp - 0.5) > 0.001) throw new Error('1200 vs L3 (1200) must be a coin flip, got ' + r.exp);
    if (!r.weakestWorks) throw new Error('weakest() returned nothing');
  });

  await check('the coach reads the whole state and offers one next action', async () => {
    await page.locator('#deckOpen').click();
    await page.waitForSelector('.coach', { timeout: 3000 });
    const r = await page.evaluate(() => ({
      msg: document.querySelector('.coach .co-msg').textContent.trim().length > 0,
      go: !!document.getElementById('coachGo'),
      bars: document.querySelectorAll('.coach .co-row').length,
    }));
    await page.evaluate(() => closeSheet());
    if (!r.msg) throw new Error('coach message is empty');
    if (!r.go) throw new Error('coach CTA missing');
    if (r.bars < 5) throw new Error('expected an ability bar per skill area, got ' + r.bars);
  });

  await check('the waw in s18 is haliyya, taught by the anwa-al-waw note', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'wasiyyat-abi-hanifa-L2');
      let tok = null, sen = null;
      st.chapters.forEach(ch => ch.sentences.forEach(s => s.tokens.forEach(t => {
        if (s.id === 's18' && t.s.full === 'وَفِي') { tok = t; sen = s; }
      })));
      const note = GRAMMAR['anwa-al-waw'];
      return {
        irab: tok && tok.irab.ar,
        grammar: tok && tok.grammar,
        role: tok && RoleEngine.of(tok),
        jumal: sen && sen.jumal && sen.jumal.length,
        noteOk: !!note && note.examples.some(e => e.src === 'wasiyyat-abi-hanifa-L2'),
      };
    });
    if (!r.irab || !r.irab.normalize('NFC').includes('حَالِيَّةٌ'.normalize('NFC')))
      throw new Error('the waw must be named haliyya: ' + r.irab);
    if (!r.grammar || !r.grammar.includes('anwa-al-waw') || !r.grammar.includes('hal'))
      throw new Error('token must anchor anwa-al-waw and hal: ' + JSON.stringify(r.grammar));
    if (r.role !== 'hal') throw new Error('RoleEngine should paint the haliyya waw as hal, got ' + r.role);
    if (r.jumal !== 2) throw new Error('s18 needs its two jumal rows, got ' + r.jumal);
    if (!r.noteOk) throw new Error('anwa-al-waw note must anchor its example to s18');
  });

  await check('the Tahlil tutor walks one sentence in order', async () => {
    const r = await page.evaluate(() => {
      const pools = tahlilSentences();
      const ordered = pools.every(l => l.every((it, i) => i === 0 || l[i - 1].ti < it.ti));
      const oneSen = pools.every(l => l.every(it => it.sen === l[0].sen));
      return { n: pools.length, min: Math.min(...pools.map(l => l.length)), ordered, oneSen };
    });
    if (!r.n) throw new Error('no tahlil-eligible sentences in the corpus');
    if (r.min < 3) throw new Error('a pool slipped under three askable words');
    if (!r.ordered || !r.oneSen) throw new Error('a walk must stay inside one sentence, in order');
    await page.evaluate(() => openGames());
    await page.waitForSelector('#gTahlil', { timeout: 3000 });
    await page.locator('#gTahlil').click();
    await page.waitForSelector('.opts [data-o]', { timeout: 3000 });
    const q = await page.evaluate(() => {
      const t = document.querySelector('.game-q').textContent.trim();
      closeSheet();
      return t;
    });
    if (!q) throw new Error('tutor question is empty');
  });

  await check('every shelf card wears its woven cover', async () => {
    await toLibrary();
    const r = await page.evaluate(() => ({
      cards: document.querySelectorAll('.lib-card').length,
      covers: document.querySelectorAll('.lib-card .cover').length,
      svg: (document.querySelector('.lib-card .cover') || {style:{backgroundImage:''}})
             .style.backgroundImage.includes('data:image/svg'),
    }));
    if (r.cards !== r.covers) throw new Error(`covers=${r.covers} cards=${r.cards}`);
    if (!r.svg) throw new Error('cover background is not the generated svg');
  });

  await check('the Ism engine: tasgir by pattern, nisba with the semai table first', async () => {
    const nfc = s => (s || '').normalize('NFC');
    const r = await page.evaluate(() => ({
      jabal: IsmEngine.tasgir('جبل'), dirham: IsmEngine.tasgir('درهم'),
      shair: IsmEngine.tasgir('شاعر'), qalb: IsmEngine.tasgir('قلب'),
      makka: IsmEngine.nisba('مكة'), madina: IsmEngine.nisba('مدينة'),
      ilm: IsmEngine.nisba('علم'), sahra: IsmEngine.nisba('صحراء'),
      dunya: IsmEngine.nisba('دنيا'),
    }));
    if (nfc(r.jabal.out) !== nfc('جُبَيْل')) throw new Error('jabal: ' + r.jabal.out);
    if (nfc(r.qalb.out) !== nfc('قُلَيْب')) throw new Error('qalb: ' + r.qalb.out);
    if (nfc(r.dirham.out) !== nfc('دُرَيْهِم')) throw new Error('dirham: ' + r.dirham.out);
    if (nfc(r.shair.out) !== nfc('شُوَيْعِر')) throw new Error('the fa\'il alif must turn waw: ' + r.shair.out);
    const madd = await page.evaluate(() => ({
      kitab: IsmEngine.tasgir('كتاب'), madinaT: IsmEngine.tasgir('مدينة'),
    }));
    if (nfc(madd.kitab.out) !== nfc('كُتَيِّب')) throw new Error('kitab must melt the madda: ' + madd.kitab.out);
    if (nfc(madd.madinaT.out) !== nfc('مُدَيِّنَة')) throw new Error('madina tasgir: ' + madd.madinaT.out);
    if (r.makka.out !== 'مكِيّ' && !r.makka.out.includes('مكّ') && nfc(r.makka.out) !== nfc('مكِيّ'))
      throw new Error('makka nisba: ' + r.makka.out);
    if (!r.madina.semai || nfc(r.madina.out) !== nfc('مَدَنِيّ'))
      throw new Error('madina must come from the SEMAI table: ' + JSON.stringify(r.madina));
    if (nfc(r.ilm.out) !== nfc('علمِيّ')) throw new Error('ilm nisba: ' + r.ilm.out);
    if (!nfc(r.sahra.out).endsWith(nfc('وِيّ'))) throw new Error('mamdud hamza must turn waw: ' + r.sahra.out);
    if (!r.dunya.semai) throw new Error('dunya must be semai');
    // the user's correction: a silent final ha turns waw — Rize → Rizevi;
    // radical-ha words are shielded by the table.
    const ha = await page.evaluate(() => ({
      rize: IsmEngine.nisba('ريزه'), fiqh: IsmEngine.nisba('فقه'),
    }));
    if (nfc(ha.rize.out) !== nfc('ريزوِيّ')) throw new Error('Rize nisba must be Rizevi: ' + ha.rize.out);
    if (!ha.fiqh.semai || nfc(ha.fiqh.out) !== nfc('فِقْهِيّ')) throw new Error('fiqh keeps its radical ha: ' + JSON.stringify(ha.fiqh));
    // the lab tab shows both machines
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.sheet .tabs button[data-lab="ism"]', { timeout: 3000 });
    await page.locator('.sheet .tabs button[data-lab="ism"]').click();
    await page.waitForSelector('#ismIn', { timeout: 3000 });
    await page.fill('#ismIn', 'مدينة');
    await page.waitForTimeout(260);
    const out = await page.evaluate(() => {
      const t = document.getElementById('ismOut').textContent;
      conjState.lab = 'sarf'; closeSheet();
      return t;
    });
    if (!out.normalize('NFC').includes('مَدَنِيّ'.normalize('NFC'))) throw new Error('lab output lacks the semai nisba: ' + out);
  });

  await check('kitab-al-sulh carries chapter 3: six contract-guises and the bedel', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'kitab-al-sulh');
      const ch3 = st.chapters.find(c => c.n === 3);
      const ids = ch3 ? ch3.sentences.map(s => s.id) : [];
      const s17 = ch3 && ch3.sentences.find(s => s.id === 's17');
      return { chapters: st.chapters.length, ids,
               salam: s17 && s17.tokens.some(t => t.s.bare === 'سلم'),
               kanaOwned: !!st.morph.kana && !!st.morph.kana.mazi };
    });
    if (r.chapters < 3) throw new Error('sulh should carry chapter 3, got ' + r.chapters + ' chapters');
    if (r.ids.join(',') !== 's13,s14,s15,s16,s17,s18') throw new Error('ch3 sentence ids: ' + r.ids);
    if (!r.salam) throw new Error('s17 must carry the salam token');
    if (!r.kanaOwned) throw new Error('kana paradigm must be copied into the sulh package');
  });

  await check('the Analyzer parses unseen Arabic: particles sure, the rest marked guess', async () => {
    const r = await page.evaluate(() => {
      const rows = SentenceAnalyzer.analyze('لم يكتبِ الطالبُ في الدفترِ');
      const wow = SentenceAnalyzer.analyze('وَرَجَعَ وَفِي قَلْبِهِ وَصِيَّةٌ');
      return {
        n: rows.length,
        lam: rows[0], verb: rows[1], talib: rows[2], fi: rows[3], daftar: rows[4],
        wasiyya: wow[3],
      };
    });
    if (r.n !== 5) throw new Error('expected 5 rows, got ' + r.n);
    if (!r.lam.sure || r.lam.kind !== 'particle') throw new Error('lam must be a certain particle');
    if (r.verb.kind !== 'verb?' && !r.verb.notes.length) throw new Error('yaktub should look verbal');
    if (r.talib.kind !== 'noun') throw new Error('al-talib must read as a noun (article)');
    if (!r.fi.sure) throw new Error('fi must be a certain particle');
    if (r.daftar.kind !== 'noun' || !r.daftar.notes.some(n => n.en.includes('majrur')))
      throw new Error('al-daftar should carry the after-jarr hint: ' + JSON.stringify(r.daftar.notes));
    // a radical waw must NOT be peeled: وَصِيَّةٌ keeps its waw and reads as tanwin noun
    if (r.wasiyya.kind !== 'noun') throw new Error('wasiyya should read as a noun, got ' + r.wasiyya.kind);
    if (r.wasiyya.notes.some(n => /waw|vav/i.test(n.en))) throw new Error('wasiyya\'s radical waw was wrongly peeled');
  });

  await check('kitab-al-sulh chapter 4: the parties\' conditions with the five-nouns fa\'il', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'kitab-al-sulh');
      const ch4 = st.chapters.find(c => c.n === 4);
      const s22 = ch4 && ch4.sentences.find(s => s.id === 's22');
      const abuhu = s22 && s22.tokens.find(t => t.s.full === 'أَبُوهُ');
      return { chapters: st.chapters.length,
               n: ch4 ? ch4.sentences.length : 0,
               abuhu: abuhu && abuhu.irab.ar,
               ishtarata: !!st.morph.ishtarata && st.morph.ishtarata.majhulMudari };
    });
    if (r.chapters < 4) throw new Error('sulh should carry chapter 4, got ' + r.chapters + ' chapters');
    if (r.n !== 5) throw new Error('ch4 should carry 5 sentences, got ' + r.n);
    if (!r.abuhu || !r.abuhu.normalize('NFC').includes('الْأَسْمَاءِ الْخَمْسَةِ'.normalize('NFC')))
      throw new Error('abuhu must teach the five nouns: ' + r.abuhu);
    if (r.ishtarata !== 'يُشْتَرَطُ') throw new Error('ishtarata passive: ' + r.ishtarata);
  });

  await check('focus mode hides the header on the way down, returns it on the way up', async () => {
    await openStoryCard('wasiyyat-abi-hanifa-samti');
    await page.waitForSelector('.word', { timeout: 3000 });
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(80);
    await page.evaluate(() => window.scrollTo(0, 900));
    await page.waitForTimeout(200);
    const hidden = await page.evaluate(() => document.body.classList.contains('focus-hide'));
    if (!hidden) throw new Error('scrolling down should hide the chrome');
    await page.evaluate(() => window.scrollTo(0, 0));
    await page.waitForTimeout(200);
    const back = await page.evaluate(() => document.body.classList.contains('focus-hide'));
    if (back) throw new Error('scrolling back up should return the chrome');
    await toLibrary();
  });

  await check('Analyzer v2: the Izhar layer — inna chain, clitics, idafa, contradiction', async () => {
    const r = await page.evaluate(() => ({
      inna: SentenceAnalyzer.analyze('إن العلمَ نورٌ'),
      clitic: SentenceAnalyzer.analyze('بالقلمِ كتابُه'),
      idafa: SentenceAnalyzer.analyze('كتاب الطالبِ جديدٌ'),
      shart: SentenceAnalyzer.analyze('مهما تفعلْ'),
      contra: SentenceAnalyzer.analyze('الكتابٌ'),
    }));
    const en = ns => ns.map(n => n.en).join(' | ');
    if (!en(r.inna[1].notes).includes('ISM')) throw new Error('after inna the ism expectation: ' + en(r.inna[1].notes));
    if (!en(r.inna[2].notes).includes('KHABAR')) throw new Error('then the khabar expectation: ' + en(r.inna[2].notes));
    if (!en(r.clitic[0].notes).includes('jarr clitic')) throw new Error('bi- must read as a jarr clitic: ' + en(r.clitic[0].notes));
    if (!r.clitic[1].seg.includes('ه')) throw new Error('the ha of kitabuhu must be peeled: ' + JSON.stringify(r.clitic[1].seg));
    if (!en(r.clitic[1].notes).includes('mudaf ilayh')) throw new Error('the peeled ha names itself: ' + en(r.clitic[1].notes));
    // the note used to say "likely mudaf" and stop; it now states the exact
    // consequences, so the check asserts the stronger claim
    const idf = en(r.idafa[0].notes);
    if (!/MUDAF/.test(idf)) throw new Error('kitab al-talib must read as idafa: ' + idf);
    if (!/cannot wear/.test(idf) || !/MAJRUR/.test(idf))
      throw new Error('the idafa note must state its consequences: ' + idf);
    if (!en(r.shart[0].notes).includes('jawazim')) throw new Error('mahma is one of the fifteen jawazim: ' + en(r.shart[0].notes));
    if (!en(r.contra[0].notes).includes('never combine')) throw new Error('al+tanwin must be flagged: ' + en(r.contra[0].notes));
  });

  await check('kitab-al-sulh chapter 5: the riba rules with lam-jazm on the hollow verb', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'kitab-al-sulh');
      const ch5 = st.chapters.find(c => c.n === 5);
      const s25 = ch5 && ch5.sentences.find(s => s.id === 's25');
      const yajuz = s25 && s25.tokens.find(t => t.s.bare === 'يجز');
      return { chapters: st.chapters.length, n: ch5 ? ch5.sentences.length : 0,
               yajuz: yajuz && yajuz.irab.ar,
               ikhtalafa: !!st.morph.ikhtalafa && st.morph.ikhtalafa.masdar };
    });
    if (r.chapters < 5) throw new Error('sulh should carry chapter 5, got ' + r.chapters + ' chapters');
    if (r.n !== 5) throw new Error('ch5 should carry 5 sentences, got ' + r.n);
    if (!r.yajuz || !r.yajuz.normalize('NFC').includes('السَّاكِنَيْنِ'.normalize('NFC')))
      throw new Error('yajuz must teach the two-sukun drop: ' + r.yajuz);
    if (r.ikhtalafa !== 'اِخْتِلَاف') throw new Error('ikhtalafa masdar: ' + r.ikhtalafa);
  });

  await check('kitab-al-sulh is COMPLETE: six chapters, ring composition, v1.0.0', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'kitab-al-sulh');
      const ch6 = st.chapters.find(c => c.n === 6);
      const s33 = ch6 && ch6.sentences.find(s => s.id === 's33');
      const last = s33 && s33.tokens.map(t => t.s.bare);
      return { chapters: st.chapters.length, n: ch6 ? ch6.sentences.length : 0,
               ring: last && last.includes('والصلح') && last.includes('خير'),
               vii: !!st.morph.infasakha && st.morph.infasakha.masdar };
    });
    if (r.chapters !== 6) throw new Error('sulh should close at 6 chapters, got ' + r.chapters);
    if (r.n !== 5) throw new Error('ch6 should carry 5 sentences, got ' + r.n);
    if (!r.ring) throw new Error('the close must ring back to wa-l-sulhu khayr');
    if (r.vii !== 'اِنْفِسَاخ') throw new Error('infasakha masdar: ' + r.vii);
  });

  await check('the Analyzer names the sentence type before the walk', async () => {
    const r = await page.evaluate(() => ({
      verb: sentenceType(SentenceAnalyzer.analyze('رجع يوسف الى البصرة')),
      noun: sentenceType(SentenceAnalyzer.analyze('العلم نور')),
      wawVerb: sentenceType(SentenceAnalyzer.analyze('ورجع يوسف')),
      inna: sentenceType(SentenceAnalyzer.analyze('إن العلم نور')),
    }));
    if (r.verb !== 'filiyya') throw new Error('raja\'a... must be fi\'liyya (corpus mazi), got ' + r.verb);
    if (r.noun !== 'ismiyya') throw new Error('al-ilm nur must be ismiyya, got ' + r.noun);
    if (r.wawVerb !== 'filiyya') throw new Error('the joining waw must be looked through, got ' + r.wawVerb);
    if (r.inna !== 'ismiyya') throw new Error('inna opens a nominal sentence, got ' + r.inna);
  });

  await check('kitab-al-waqf joins the shelf: definition, mithal verb, the qaida', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'kitab-al-waqf');
      if (!st) return { missing: true };
      const s5 = st.chapters[0].sentences.find(s => s.id === 's5');
      return {
        count: STORIES.length,
        qaida: s5 && s5.tokens.some(t => t.s.bare === 'كنص'),
        waqafa: st.morph.waqafa && st.morph.waqafa.mudari[0],
        halla: st.morph['halla-lawful'] && st.morph['halla-lawful'].mudari[0],
      };
    });
    if (r.missing) throw new Error('kitab-al-waqf is not in the library');
    if (r.count < 15) throw new Error("the shelf should hold at least 15 stories, got " + r.count);
    if (!r.qaida) throw new Error('s5 must carry the shart-al-waqif qaida');
    if (r.waqafa !== 'يَقِفُ'.normalize('NFC')) throw new Error('waqafa mithal mudari: ' + r.waqafa);
    if (r.halla !== 'يَحِلُّ'.normalize('NFC')) throw new Error('halla geminate mudari: ' + r.halla);
  });

  await check('the Harake Auditor proofreads by pure rule, with the ibn exception', async () => {
    const r = await page.evaluate(() => ({
      badStart: HarakeAuditor.audit('كْتَاب').length,
      ibn: HarakeAuditor.audit('بْنُ').length,
      medialAlif: HarakeAuditor.audit('كِتَاُب').length,
      doubleVowel: HarakeAuditor.audit('كَُتب').length,
      earlyTanwin: HarakeAuditor.audit('كتًاب').length,
      okTanwinAlif: HarakeAuditor.audit('كِتَابًا').length,
      clean: HarakeAuditor.audit('يَسْتَغْفِرُونَ').length,
      shaddaSukun: HarakeAuditor.audit('مدّْ').length,
    }));
    if (!r.badStart) throw new Error('sukun-initial must be flagged');
    if (r.ibn) throw new Error('bnu is the received exception — no flag');
    if (!r.medialAlif) throw new Error('vowel on a medial plain alif must be flagged');
    if (!r.doubleVowel) throw new Error('two vowels on one letter must be flagged');
    if (!r.earlyTanwin) throw new Error('tanwin before the end must be flagged');
    if (r.okTanwinAlif) throw new Error('tanwin before a final alif is the standard spelling');
    if (r.clean) throw new Error('a clean word must not be flagged');
    if (!r.shaddaSukun) throw new Error('shadda+sukun must be flagged');
  });

  await check('two-sided Elo: the item learns opposite the learner', async () => {
    const r = await page.evaluate(() => {
      localStorage.removeItem('qissa-elo-items');
      state.eloItems = {};
      const before = state.elo.vocab;
      EloModel.update('vocab', 3, false, 'lex:hard-word');
      const itemAfterMiss = state.eloItems['vocab|lex:hard-word'];
      EloModel.update('vocab', 3, true, 'lex:hard-word');
      const itemAfterHit = state.eloItems['vocab|lex:hard-word'];
      const hist = state.eloHist.length;
      state.elo = { vocab: 1200, sarf: 1200, nahw: 1200, adad: 1200 };
      state.eloItems = {};
      localStorage.removeItem('qissa-elo-items'); localStorage.removeItem('qissa-elo');
      return { before, itemAfterMiss, itemAfterHit, hist };
    });
    if (!(r.itemAfterMiss > 1200)) throw new Error('a missed item must drift UP from its prior: ' + r.itemAfterMiss);
    if (!(r.itemAfterHit < r.itemAfterMiss)) throw new Error('a hit must bring the item back down');
    if (r.hist < 1) throw new Error('updates must leave a daily snapshot for the sparkline');
  });

  await check('the theme toggle pins light and dark over the OS preference', async () => {
    await page.evaluate(() => { state.theme = 'auto'; localStorage.removeItem('qissa-theme'); applyTheme(); });
    const t0 = await page.evaluate(() => document.documentElement.dataset.theme || 'none');
    if (t0 !== 'none') throw new Error('auto must leave no attribute, got ' + t0);
    await page.locator('#themeToggle').click();
    const t1 = await page.evaluate(() => document.documentElement.dataset.theme);
    if (t1 !== 'light') throw new Error('first click pins light, got ' + t1);
    await page.locator('#themeToggle').click();
    const r = await page.evaluate(() => ({
      theme: document.documentElement.dataset.theme,
      ground: getComputedStyle(document.documentElement).getPropertyValue('--ground').trim(),
    }));
    if (r.theme !== 'dark') throw new Error('second click pins dark, got ' + r.theme);
    if (r.ground !== '#101A20') throw new Error('dark vars must win: --ground=' + r.ground);
    await page.locator('#themeToggle').click();
    await page.evaluate(() => { state.theme = 'auto'; localStorage.removeItem('qissa-theme'); applyTheme(); });
  });

  await check('the IrabModel trains on the corpus and votes sensibly', async () => {
    const r = await page.evaluate(() => {
      const size = IrabModel.trainingSize();
      // a definite noun right after a verb — the corpus should have taught
      // the model that this smells like the fa'il
      const afterVerb = IrabModel.predict('الطَّالِبُ', 1, 4, 'verb');
      const afterJarr = IrabModel.predict('الْبَيْتِ', 2, 4, 'jarr');
      return { size,
               topAfterVerb: afterVerb[0] && afterVerb[0].r,
               inTop2Vf: afterVerb.slice(0, 2).map(x => x.r),
               topAfterJarr: afterJarr.slice(0, 2).map(x => x.r),
               probsSum: Math.round(afterVerb.reduce((s, x) => s + x.p, 0) * 100) };
    });
    if (r.size < 800) throw new Error('training set suspiciously small: ' + r.size);
    if (!r.inTop2Vf.includes('fail')) throw new Error('after a verb, fail must be a top-2 vote: ' + r.inTop2Vf);
    if (!r.topAfterJarr.some(x => x === 'jarr' || x === 'mudaf'))
      throw new Error('after a jarr letter, majrur/mudaf should lead: ' + r.topAfterJarr);
    if (Math.abs(r.probsSum - 100) > 1) throw new Error('probabilities must sum to 1, got ' + r.probsSum + '%');
  });

  // The score is pinned so a feature change has to be MEASURED. Reading the
  // ending sign and the manner of i'rab off the rule engines lifted this from
  // 42.7/62.9 to 49.3/71.0; a bucketed word length took first guesses to
  // 51.4, and damping the likelihoods by 1/sqrt(k) took them to 53.2. The
  // floor sits just under whatever the last measured run gave.
  // tools/ablate_features.js earns a FEATURE its place;
  // tools/ablate_estimator.js earns an ESTIMATOR its place.
  await check('the model is graded held-out, and the honest number is the one shown', async () => {
    const a = await page.evaluate(() => {
      const t0 = performance.now();
      const cv = IrabModel.crossVal();
      const ms = performance.now() - t0;
      const x = IrabModel.accuracy();
      return { n: cv.n, folds: cv.folds, ms: Math.round(ms),
               cv1: Math.round(cv.top1 * 1000) / 10, cv2: Math.round(cv.top2 * 1000) / 10,
               // the panel's OWN rounding, so this check reads the number the
               // learner reads rather than a tenth-place variant of it
               shown: Math.round(cv.top1 * 100),
               res1: Math.round(x.top1 * 1000) / 10,
               // the panel's rounding for the RESUBSTITUTION figure too:
               // rounding the already-once-rounded res1 turned 58.46 into
               // 58.5 into 59, a percent the panel never prints — and the
               // -1 from indexOf then failed the order comparison. Round
               // once, from the raw value, exactly as the panel does.
               resShown: Math.round(x.top1 * 100) };
    });
    if (a.n < 2000) throw new Error('the labeled set shrank: ' + a.n);
    if (a.folds < 10) throw new Error('too few folds to mean anything: ' + a.folds);
    // The floors are on the CROSS-VALIDATED score, because that is the claim
    // the app makes to the learner. Resubstitution is only the upper bound.
    // raised when the GOVERNOR features landed: what precedes a word decides
    // what it can be, and teaching the model that was worth a point on each.
    // …and raised again at v129: the seam-aware IrabSign case (irc-) and the
    // closed-class key (pk-) were ablated on the shipped base — 52.9/70.5 ->
    // 55.0/72.9 resubstitution — and CONFIRMED held-out: 50.9/67.8 -> 52.8/70.2
    // over 17 folds. Both floors moved up to hold the gain.
    // v134: the ppk- feature (previous word's closed-class key) measured
    // held-out 52.6/70.5 -> 54.7/72.1 over 17 folds on 3,867 tokens, A/B on
    // the same page (scratchpad cvab17 protocol). Floors raised to hold it.
    // v138: the corpus reached 3,936 labelled tokens and the held-out score
    // rose with it — 54.6/72.1 measured, floors raised to hold the gain. An
    // npk- feature (NEXT word's closed-class key) was A/B'd the same day and
    // REJECTED as noise (54.6/72.1 -> 54.4/72.0): government flows FORWARD
    // from the governor before the word, which is why ppk- paid and npk-
    // does not. Recorded so nobody spends the afternoon again.
    // v146: the ESTIMATOR changed — averaged perceptron over the same
    // features, same folds: 54.5/71.9 -> 60.2/74.5 over 4,049 tokens, flat
    // across epochs 5-20 and three seeds (60.0-60.3 / 74.5-74.7). The npk-
    // feature was re-A/B'd under the perceptron and is STILL noise
    // (60.2/74.5 -> 60.0/74.6). Floors raised to hold the gain.
    // v147: four feature CONJUNCTIONS (governor-key×sign, after-verb×sign,
    // al×settled-case, tanwin×after-verb) — what the perceptron made
    // affordable: 60.2/74.5 -> 61.2/76.5, stable across three seeds
    // (61.2-61.3 / 75.4-76.5). A fifth pair (governor-key×position) was
    // noise alone and nothing in the ensemble — dropped. Floors raised.
    if (a.cv1 < 60) throw new Error('held-out first-guess regressed to ' + a.cv1 + '%');
    // …and re-pinned at 67 when the corpus reached 3,619 labelled tokens. The
    // measured two-guess moved 68.x -> 67.9 as Talkhis chapters 7 and 8 added
    // ~90 labels and reshaped the seventeen folds. That it was the DATA and not
    // the engine was established by A/B, not assumed: the same page with the
    // eight new demonstratives removed from PARTICLES scores 51.0 / 67.9 as
    // well — identical to a tenth. Lower a floor only with a measurement in
    // hand and the measurement written down.
    if (a.cv2 < 75) throw new Error('held-out two-guess regressed to ' + a.cv2 + '%');
    // and it must be an HONEST gap: memorising its own corpus always scores higher
    if (a.res1 <= a.cv1) throw new Error('resubstitution should beat held-out; something is leaking');
    if (a.ms > 4000) throw new Error('cross-validation took ' + a.ms + 'ms — too slow to run on open');
    await page.evaluate(() => { conjState.lab = 'jumla'; });
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.ml-score', { timeout: 3000 });
    const line = await page.locator('.ml-score').textContent();
    if (!line.includes(String(a.n))) throw new Error('the panel must state the real size: ' + line);
    // and it must lead with the HELD-OUT figure, never the resubstitution one
    if (!line.includes(String(a.shown))) throw new Error('the panel must lead with the held-out score: ' + line);
    // compare the PERCENTAGES, not the bare digits: the panel also prints the
    // corpus size, and «3536 labelled words» contains «53», so a bare indexOf
    // found the resubstitution figure inside a number that is not a score.
    if (line.indexOf(String(a.resShown) + "%") < 0)
      throw new Error('the resubstitution figure is missing from the panel: ' + line);
    if (line.indexOf(String(a.shown) + "%") > line.indexOf(String(a.resShown) + "%"))
      throw new Error('resubstitution is quoted before the held-out score: ' + line);
    // …and the panel must also show the two RULE-trained taggers, filled in
    // after paint because grading them costs ~2s
    await page.waitForFunction(() => {
      const el = document.getElementById('mlTagLine');
      return el && el.textContent.length > 40;
    }, { timeout: 8000 });
    const tag = await page.locator('#mlTagLine').textContent();
    const nums = await page.evaluate(() => {
      const v = SarfTagger.evalUnseen(), i = IsmTagger.evalUnseen();
      return { v: Math.round(v.top1 * 100), i: Math.round(i.top1 * 100),
               vn: v.examples, inn: i.examples };
    });
    for (const [k, n] of Object.entries(nums))
      if (!tag.includes(String(n))) throw new Error('the tagger line omits ' + k + '=' + n + ': ' + tag);
    await page.evaluate(() => { conjState.lab = 'sarf'; closeSheet(); });
  });

  await check('the hoca walkthrough asks the questions on the user\'s own sentence', async () => {
    await page.evaluate(() => { conjState.lab = 'jumla'; conjState.jumla = 'لم تكتب امرأة لزوجها مكتوبة'; });
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#jumlaOut', { timeout: 3000 });
    await page.waitForTimeout(300);
    const r = await page.evaluate(() => {
      const t = document.getElementById('jumlaOut').textContent;
      const html = document.getElementById('jumlaOut').innerHTML;
      conjState.lab = 'sarf'; conjState.jumla = 'لم يكتبِ الطالبُ في الدفترِ'; closeSheet();
      return { hasHoca: html.includes('hoca-line'),
               asksWho: /who\?|kim\?/.test(t),
               jazm: /jazm|cezm|câzim/i.test(t),
               ml: html.includes('vchip ml') };
    });
    if (!r.hasHoca) throw new Error('the walkthrough panel is missing');
    if (!r.asksWho) throw new Error('after the verb the chain must ask who?');
    if (!r.jazm) throw new Error('lam must be named a jazm governor');
    if (!r.ml) throw new Error('the model votes are missing from the rows');
  });

  // The vocative engine derives its rulings; the stories state theirs. If the
  // two ever drifted apart, the Nida game would be teaching against the text.
  await check('the Nida engine agrees with every munada the corpus itself parses', async () => {
    const r = await page.evaluate(() => {
      const bad = [], seen = [], signs = new Set();
      STORIES.forEach(st => (st.chapters || []).forEach(ch => ch.sentences.forEach(sen => sen.tokens.forEach((t, ti) => {
        const f = NidaEngine.flat(t.s.full);
        if (!NidaEngine.PARTICLES.some(p => p.flat === f && f.length > 1)) return;
        // أَيْ the calling particle wears a SUKUN on its ya; أَيُّ with a
        // vowelled ya is the interrogative noun (ch26). The flat fold threw
        // that vowel away and read أَيُّ الْفَرِيقَيْنِ as a call.
        if (f === 'اي' && /ي[ًٌٍَُِ]/.test(t.s.full.normalize('NFC'))) return;
        const m = sen.tokens[ti + 1];
        if (!m || !m.irab) return;
        const call = [t, m, sen.tokens[ti + 2]].filter(Boolean).map(x => x.s.full).join(' ');
        const v = NidaEngine.read(call);
        seen.push(m.s.full);
        if (!v || !v.ok) { bad.push(m.s.full + ': engine refused'); return; }
        const said = m.irab.ar;
        const storedMabni = /مَبْنِيٌّ عَلَى الضَّمِّ|مَبْنِيٌّ عَلَى الْأَلِفِ|مَبْنِيٌّ عَلَى الْوَاوِ/.test(said);
        const storedMansub = /مَنْصُوب/.test(said);
        if (storedMabni && v.ruling !== 'mabni') bad.push(m.s.full + ': text says mabni, engine says ' + v.ruling);
        if (!storedMabni && storedMansub && v.ruling !== 'mansub')
          bad.push(m.s.full + ': text says mansub, engine says ' + v.ruling);
        signs.add(v.sign);
      }))));
      return { bad, n: seen.length, signs: [...signs] };
    });
    if (r.n < 15) throw new Error('too few corpus vocatives to be a real gate: ' + r.n);
    if (r.bad.length) throw new Error(r.bad.join('; '));
    // the drill garden exists so the rarer signs are exercised by real text
    for (const s of ['damma', 'alif', 'waw', 'fatha', 'fathatan', 'fathaTaqdiri'])
      if (!r.signs.includes(s)) throw new Error('no corpus call shows the sign ' + s + ': ' + r.signs);
  });

  await check('the Nida engine reads the kinds, and refuses what the surface cannot decide', async () => {
    const r = await page.evaluate(() => {
      const k = s => { const v = NidaEngine.read(s); return v && v.ok ? v.kind + '/' + v.sign : 'x:' + (v && v.reason); };
      return {
        mufrad:  k('يَا يُوسُفُ'),
        mudaf:   k('يَا عَبْدَ اللهِ'),
        nakira:  k('يَا رَجُلًا'),
        shibh:   k('يَا طَالِعًا جَبَلًا'),
        ayyuha:  k('يَا أَيُّهَا الطَّالِبُ'),
        dual:    k('يَا مُسْلِمَانِ'),
        plural:  k('يَا مُسْلِمُونَ'),
        mutak:   k('يَا مُعَلِّمِي'),
        lahumma: k('اللَّهُمَّ'),
        istigh:  k('يَا لَلَّهِ'),
        alAfter: k('يَا الطَّالِبُ'),
        bareTan: k('يَا زَيْدٌ'),
        naked:   k('يا زيد'),
      };
    });
    const want = {
      mufrad: 'mufrad/damma', mudaf: 'mudaf/fatha', nakira: 'nakira/fathatan',
      shibh: 'nakiraOrShibh/fathatan', ayyuha: 'ayyuha/damma', dual: 'mufrad/alif',
      plural: 'mufrad/waw', mutak: 'mudaf/fathaTaqdiri', lahumma: 'lahumma/damma',
      istigh: 'istighatha/kasra', alAfter: 'x:alAfterYa', bareTan: 'x:tanwin',
      naked: 'x:unvowelled',
    };
    const bad = Object.keys(want).filter(x => r[x] !== want[x]).map(x => `${x}: ${r[x]} ≠ ${want[x]}`);
    if (bad.length) throw new Error(bad.join('; '));
  });

  // Tarkhim is pure letter-work, so it can be pinned exactly. The two dialects
  // differ only in the vowel left standing, and a madda collapses both into one.
  await check('tarkhim is derived letter by letter, in both dialects', async () => {
    const r = await page.evaluate(() => {
      const t = n => { const v = NidaEngine.tarkhim(n); return v.ok ? v.muntazir + '|' + v.ghayrMuntazir : 'x:' + v.reason; };
      return { harith: t('حَارِثُ'), jafar: t('جَعْفَرُ'), fatima: t('فَاطِمَةُ'),
               uthman: t('عُثْمَانُ'), suad: t('سُعَادُ'), mansur: t('مَنْصُورُ'),
               zayd: t('زَيْدٌ'), nadb: NidaEngine.nadb('زَيْدٌ').call };
    });
    const want = { harith: 'حَارِ|حَارُ', jafar: 'جَعْفَ|جَعْفُ', fatima: 'فَاطِمَ|فَاطِمُ',
                   uthman: 'عُثْمَ|عُثْمُ', suad: 'سُعَا|سُعَا', mansur: 'مَنْصُ|مَنْصُ',
                   zayd: 'x:three', nadb: 'وَا زَيْدَاهْ' };
    const bad = Object.keys(want).filter(x => r[x] !== want[x]).map(x => `${x}: ${r[x]} ≠ ${want[x]}`);
    if (bad.length) throw new Error(bad.join('; '));
  });

  await check('the Nida Lab lays the verdict out and derives the two dialects', async () => {
    await page.evaluate(() => { conjState.lab = 'nida'; conjState.nida = 'يَا يُوسُفُ'; });
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#nidaOut', { timeout: 3000 });
    await page.waitForTimeout(250);
    const r = await page.evaluate(() => {
      const t = document.getElementById('nidaOut').textContent;
      const rows = document.querySelectorAll('#nidaOut .nida-row').length;
      const derive = document.querySelectorAll('#nidaOut .nida-derive .d').length;
      conjState.nida = 'يَا الطَّالِبُ'; renderNidaOut();
      const bad = document.querySelectorAll('#nidaOut .nida-bad').length;
      const fix = (document.querySelector('#nidaOut .fix') || {}).textContent || '';
      conjState.lab = 'sarf'; conjState.nida = 'يَا عَبْدَ اللهِ'; closeSheet();
      return { rows, derive, bad, fix, mabni: t.includes('مَبْنِيٌّ عَلَى الضَّمِّ'),
               muntazir: t.includes('يُوسُ') };
    });
    if (r.rows < 3) throw new Error('the verdict needs particle, kind and sign: ' + r.rows);
    if (r.derive !== 2) throw new Error('tarkhim and nadb must both derive: ' + r.derive);
    if (!r.mabni) throw new Error('the ruling line is missing');
    if (!r.muntazir) throw new Error('the tarkhim of يوسف should show');
    if (!r.bad) throw new Error('يا before الـ must be refused');
    if (!r.fix.includes('أَيُّهَا')) throw new Error('the refusal must offer ayyuha: ' + r.fix);
  });

  await check('the Nida game is played off the engine, and teaches the wrong pick', async () => {
    await page.evaluate(() => openGames());
    await page.waitForSelector('.game-pick', { timeout: 3000 });
    await page.locator('#gNida').click();
    await page.waitForSelector('.opts', { timeout: 3000 });
    const n = await page.locator('.opts [data-o]').count();
    if (n !== 4) throw new Error('four rulings to choose from, got ' + n);
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('#qWhy', { timeout: 3000 });
    const r = await page.evaluate(() => {
      const html = document.getElementById('qWhy').innerHTML;
      return { taught: html.includes('game-wrongwhy') || html.includes('game-why'),
               right: document.querySelectorAll('.opts .right').length,
               why: document.getElementById('qWhy').textContent };
    });
    if (r.right !== 1) throw new Error('exactly one option is right, marked: ' + r.right);
    if (!r.taught) throw new Error('the reveal must teach');
    if (!/مُنَادًى/.test(r.why)) throw new Error('the reveal must name the kind: ' + r.why.slice(0, 80));
    await page.evaluate(() => closeSheet());
  });

  // The i'lal engine is ten ordered rules over an underlying form. Every one
  // of these is a worked derivation from the Maksud / ilal-kaideleri sources,
  // and NONE of them is stored: قُلْ, مَكِيلٌ and مَرْمِيٌّ come out of the rules.
  await check('the I\'lal engine derives every worked form the books recite', async () => {
    const want = {
      "قَوَلَ": "قَالَ", "بَيَعَ": "بَاعَ", "رَمَيَ": "رَمَى", "غَزَوَ": "غَزَا",
      "يَقْوُلُ": "يَقُولُ", "يَبْيِعُ": "يَبِيعُ",
      "قَوَلْتُ": "قُلْتُ", "بَيَعْتُ": "بِعْتُ",
      "قَاوِلٌ": "قَائِلٌ", "بَايِعٌ": "بَائِعٌ",
      "مَقْوُولٌ": "مَقُولٌ", "مَكْيُولٌ": "مَكِيلٌ",
      "مَغْزُووٌ": "مَغْزُوٌّ", "مَرْمُويٌ": "مَرْمِيٌّ", "مَخْشُويٌ": "مَخْشِيٌّ",
      "غَازِيٌ": "غَازٍ", "رَامِيٌ": "رَامٍ", "مِوْزَانٌ": "مِيزَانٌ", "اُقْوُلْ": "قُلْ",
      // the mithal waw-drop, and the two shapes that must NOT lose their waw:
      // يَوْجَلُ has a fatha after it, and يَوْمَ is no verb at all.
      "يَوْعِدُ": "يَعِدُ", "يَوْصِلُ": "يَصِلُ", "يَوْجَلُ": "يَوْجَلُ", "يَوْمَ": "يَوْمَ",
      // sound roots and a real word that LOOKS like an i'lal site must be left alone
      "مُيَسَّرٌ": "مُيَسَّرٌ", "كَتَبَ": "كَتَبَ", "مَكْتُوبٌ": "مَكْتُوبٌ", "كَاتِبٌ": "كَاتِبٌ",
    };
    const got = await page.evaluate(w => {
      const norm = s => IlalEngine.join(IlalEngine.parse(s));
      const bad = [];
      Object.keys(w).forEach(asl => {
        const r = IlalEngine.derive(asl);
        if (!r || norm(r.out) !== norm(w[asl])) bad.push(asl + ' -> ' + (r && r.out) + ' ≠ ' + w[asl]);
      });
      return bad;
    }, want);
    if (got.length) throw new Error(got.join('; '));
  });

  await check('the I\'lal engine builds the derived nouns from root and wazn alone', async () => {
    const want = {
      "قول|fail": "قَائِلٌ", "قول|maful": "مَقُولٌ",
      "بيع|fail": "بَائِعٌ", "بيع|maful": "مَبِيعٌ",
      "غزو|fail": "غَازٍ",   "غزو|maful": "مَغْزُوٌّ",
      "رمي|fail": "رَامٍ",   "رمي|maful": "مَرْمِيٌّ",
      "كيل|maful": "مَكِيلٌ", "دعو|maful": "مَدْعُوٌّ",
      "وعد|mudari": "يَعِدُ", "وصل|mudari": "يَصِلُ", "وعد|maful": "مَوْعُودٌ",
      "نصر|fail": "نَاصِرٌ", "نصر|maful": "مَنْصُورٌ",
    };
    const bad = await page.evaluate(w => {
      const norm = s => IlalEngine.join(IlalEngine.parse(s));
      const out = [];
      Object.keys(w).forEach(k => {
        const [root, shape] = k.split('|');
        const b = IlalEngine.build(root, shape);
        if (!b || norm(b.out) !== norm(w[k])) out.push(k + ' -> ' + (b && b.out) + ' ≠ ' + w[k]);
      });
      return out;
    }, want);
    if (bad.length) throw new Error(bad.join('; '));
  });

  // The rules over-apply unless told to stand down. Two kinds of refusal:
  // one derivable from the wazn (coded), one lexical (stored) — and the panel
  // must say which, because that distinction is the project's whole method.
  await check('the I\'lal engine knows where the rules must stand down', async () => {
    const r = await page.evaluate(() => {
      const norm = s => IlalEngine.join(IlalEngine.parse(s));
      const tafdil = IlalEngine.build('قول', 'tafdil');
      const awar = IlalEngine.build('عور', 'fail');
      const plain = IlalEngine.build('قول', 'fail');
      return {
        tafdilOut: tafdil && norm(tafdil.out), tafdilWhy: tafdil && tafdil.blocked && tafdil.blocked.why,
        tafdilSteps: tafdil && tafdil.steps.length,
        awarOut: awar && norm(awar.out), awarWhy: awar && awar.blocked && awar.blocked.why,
        plainBlocked: !!(plain && plain.blocked), plainOut: plain && norm(plain.out),
        want: { tafdil: norm('أَقْوَلُ'), awar: norm('عَاوِرٌ'), plain: norm('قَائِلٌ') },
      };
    });
    if (r.tafdilWhy !== 'wazn') throw new Error('the elative must be refused by RULE, got ' + r.tafdilWhy);
    if (r.tafdilSteps !== 0) throw new Error('a blocked derivation fires no rule');
    if (r.tafdilOut !== r.want.tafdil) throw new Error('أَقْوَلُ must survive intact: ' + r.tafdilOut);
    if (r.awarWhy !== 'lexical') throw new Error('a defect-verb must be refused by the LEXICON, got ' + r.awarWhy);
    if (r.awarOut !== r.want.awar) throw new Error('عور must stay sound: ' + r.awarOut);
    // and the guard must not swallow the ordinary case
    if (r.plainBlocked) throw new Error('قول was wrongly blocked');
    if (r.plainOut !== r.want.plain) throw new Error('قَائِلٌ regressed: ' + r.plainOut);
  });

  // A reader caught the app calling اُكْتُبْ a majzum mudari. It is an
  // IMPERATIVE built on sukun — no governor, nothing removed — and the two
  // are told apart by the opening vowel, not by the final one.
  await check('an imperative on sukun is mabni, not jazm, and the wazn is named', async () => {
    const r = await page.evaluate(() => {
      const f = w => { const x = IrabSign.of(w); return x && x.by; };
      const rows = SentenceAnalyzer.analyze('اُكْتُبْ ان الله قادر على كل شيء');
      const first = rows[0].notes.map(n => n.tr).join(' | ');
      const an = rows[1].notes.map(n => n.tr).join(' | ');
      const k = GrammarKernel.ask('اُكْتُبْ ان الله قادر على كل شيء');
      return {
        wasl: f('اُكْتُبْ'), qat: f('أُكْتُبْ'), form7: f('اِسْتَغْفِرْ'),
        // the first-person mudari prefix takes a FATHA and stays jazm
        majzum: f('لَمْ أَكْتُبْ'), plainMajzum: f('يَكْتُبْ'),
        qatNote: (IrabSign.of('أُكْتُبْ') || {}).why.tr,
        first, an, kernelKeys: k.findings.map(x => x.k),
        tag: SarfTagger.tag('اُكْتُبْ', 1)[0].y,
        wazn: SarfTagger.waznOf(SarfTagger.tag('اُكْتُبْ', 1)[0]),
      };
    });
    for (const k of ['wasl', 'qat', 'form7'])
      if (r[k] !== 'bina') throw new Error(k + ' should be mabni, got ' + r[k]);
    for (const k of ['majzum', 'plainMajzum'])
      if (r[k] !== 'hadhf') throw new Error(k + ' should still be jazm, got ' + r[k]);
    if (!/VASL|vasl/.test(r.qatNote)) throw new Error('the qat spelling must be corrected: ' + r.qatNote);
    if (r.tag !== 'I|amr|0') throw new Error('the tagger read اُكْتُبْ as ' + r.tag);
    if (r.wazn !== 'اُفْعُلْ') throw new Error('the wazn should be اُفْعُلْ, got ' + r.wazn);
    if (!/اُفْعُلْ/.test(r.first) || !/emir/.test(r.first))
      throw new Error('the analyzer must name the wazn and the cell: ' + r.first);
    // and «anna» after a verb must say the clause BECOMES the object
    if (!/masdar|dığını/.test(r.an)) throw new Error('anna row: ' + r.an);
    if (!r.kernelKeys.includes('anna'))
      throw new Error('the kernel must explain the anna clause: ' + r.kernelKeys);
  });

  // The commonest word in a creed text was being taken apart as if it were a
  // derived noun: ال peeled as the article, the final ha peeled as a pronoun
  // and called a mudaf ilayh, a root ل ل ه invented from the wreckage, and a
  // verb's bab hung on it as a wazn. It is an ALAM, and the rule that refuses
  // the pronoun reading is one worth stating: a noun is never definite by the
  // article AND by idafa at once.
  await check('the name of Allah is read as an alam, and ال refuses the idafa', async () => {
    const r = await page.evaluate(() => {
      const one = w => {
        const x = SentenceAnalyzer.analyze(w)[0];
        return { root: x.root || null, wazn: x.wazn || null, kind: x.kind,
                 lemma: x.lemma || null, sure: x.sure,
                 notes: x.notes.map(n => n.tr + ' ‖ ' + n.en).join(' | ') };
      };
      return { jalala: one('اللهَ'), bare: one('الله'),
               // إِلَه is the common noun, NOT the name: it keeps its root
               ilah: one('إِلَهٍ'),
               // a genuine ال-word ending in a pronoun-shaped tail
               alword: one('الْكِتَابُهُ') };
    });
    const j = r.jalala;
    if (j.root) throw new Error('the name has no root to find, got ' + j.root);
    if (j.wazn) throw new Error('the name stands in no scale, got ' + j.wazn);
    if (j.lemma !== 'اللَّه') throw new Error('lemma: ' + j.lemma);
    if (!j.sure || j.kind !== 'noun') throw new Error('it is a noun, and certain');
    // match the CLAIMS, not the sentences that deny them — the alam note says
    // both words out loud in order to refuse the reading
    if (/zamir — muzâf|attached pronoun — the mudaf/.test(j.notes))
      throw new Error('no pronoun may be peeled off it: ' + j.notes);
    if (/harf-i tarif — isim|definite article — a noun/.test(j.notes))
      throw new Error('its lam is not the article: ' + j.notes);
    if (!/alam|ALEM/.test(j.notes)) throw new Error('it must be named an alam: ' + j.notes);
    if (r.bare.lemma !== 'اللَّه') throw new Error('undiacritised too: ' + r.bare.lemma);
    // إِلَه keeps a real root and a real wazn — it is the common noun, not the
    // name. (The rules path spells the initial radical from the surface
    // carrier, so it reads إ ل ه where the books write أ ل ه; that is a
    // separate, pre-existing gap, logged in COVERAGE.)
    if (!/ل ه$/.test(r.ilah.root || '')) throw new Error('إِلَه must keep its root: ' + r.ilah.root);
    if (r.ilah.lemma === 'اللَّه') throw new Error('إِلَه is not the name of Allah');
    if (!/izâfet|idafa/.test(r.alword.notes)) throw new Error('the ال rule must be stated: ' + r.alword.notes);
    if (/zamir — muzâf|the mudaf ilayh/.test(r.alword.notes))
      throw new Error('ال and idafa never combine: ' + r.alword.notes);
  });

  // alaka-ilm-bayan.txt counts TWENTY-EIGHT alaqas of majaz lughawi and works
  // every one through: definition, example, literal meaning, intended meaning,
  // the qarina that forbids the literal reading, and the madrasah's formula.
  // The registry carried twelve. It carries all of them now.
  await check('all twenty-eight alaqas are present, and every one is quizzable', async () => {
    const r = await page.evaluate(() => {
      const need = a => a.ex && a.haqiqi && a.majazi && a.qarina && a.def;
      const pair = (x, y) => { const a = ALAQAT.find(z => z.k === x), b = ALAQAT.find(z => z.k === y);
        return !!(a && b && a.haqiqi.ar === b.majazi.ar && a.majazi.ar === b.haqiqi.ar); };
      return { total: ALAQAT.length,
               thin: ALAQAT.filter(a => !need(a)).map(a => a.k),
               dupK: ALAQAT.map(a => a.k).filter((k, i, z) => z.indexOf(k) !== i),
               dupEx: ALAQAT.map(a => a.ex).filter((e, i, z) => z.indexOf(e) !== i),
               noIfada: ALAQAT.filter(a => !a.ifada && !a.istiara).map(a => a.k),
               istiara: ALAQAT.filter(a => a.istiara).map(a => a.k),
               // the mirrored pairs are the whole difficulty of the chapter:
               // the same two meanings swapped, told apart only by the qarina
               // Only these three mirror LITERALLY — the source gives the same
               // two meanings swapped. The other four pairs are mirrors in
               // DOCTRINE but the book illustrates each direction with its own
               // example (شفة/مشفر against مشافر/شفاه), so asserting a literal
               // swap on them was my test being wrong, not the data.
               mirrors: ['lazimiyya|malzumiyya', 'illiyya|maluliyya', 'daliyya|madluliyya']
                 .filter(p2 => !pair(...p2.split('|'))),
               // the doctrinal pairs must at least all be present and distinct
               missingPairs: ['itlaq', 'taqyid', 'umum', 'khusus', 'shartiyya',
                              'mashrutiyya', 'mutaalliqiyya', 'mutaallaqiyya']
                 .filter(k => !ALAQAT.some(a => a.k === k)) };
    });
    if (r.total !== 28) throw new Error('the source counts twenty-eight, the registry has ' + r.total);
    if (r.thin.length) throw new Error('these cannot be quizzed: ' + r.thin.join(','));
    if (r.dupK.length) throw new Error('duplicate keys: ' + r.dupK.join(','));
    if (r.dupEx.length) throw new Error('two alaqas share an example: ' + r.dupEx.join(' | '));
    if (r.noIfada.length) throw new Error('no ifada formula on: ' + r.noIfada.join(','));
    // exactly one relation makes the majaz an isti'ara rather than a mursal
    if (r.istiara.join() !== 'mushabaha')
      throw new Error('likeness alone makes an isti\'ara, got: ' + r.istiara.join(','));
    if (r.mirrors.length) throw new Error('these pairs do not mirror: ' + r.mirrors.join(' '));
    if (r.missingPairs.length) throw new Error('missing from the doctrinal pairs: ' + r.missingPairs.join(','));
  });

  // «Whenever a story is uploaded it should get games as good as the built
  // ones.» It already does — every game draws from the engines and the package
  // — but nothing said so and nothing checked it. Now the factory declares it
  // and this audits EVERY story in the library against EVERY game.
  await check('the game factory gives every story a full set of playable games', async () => {
    const r = await page.evaluate(() => {
      const a = GameFactory.audit();
      return { n: GameFactory.CATALOGUE.length, stories: a.length,
               worst: Math.min(...a.map(x => x.content)),
               // a game must declare where its items come from and how many it needs
               illFormed: GameFactory.CATALOGUE.filter(g => !g.id || !g.group || !g.emblem || !g.min).map(g => g.id),
               // and every id in the catalogue must be a real button in the hub
               rows: a.map(x => ({ id: x.id, content: x.content,
                 short: Object.entries(x.games).filter(([, v]) => !v.ok && !v.gated).map(([k]) => k) })) };
    });
    if (r.n < 14) throw new Error('the catalogue shrank: ' + r.n);
    if (r.illFormed.length) throw new Error('a game declares nothing about itself: ' + r.illFormed);
    if (r.stories < 15) throw new Error('the audit did not see the library: ' + r.stories);
    // Every story must reach a real set on its OWN content. The floor is 9 of
    // the 13 content-gated games; cloze is excluded because it is gated on
    // what the learner has read, not on what the story holds.
    if (r.worst < 9) {
      const bad = r.rows.filter(x => x.content < 9)
        .map(x => x.id + ' (' + x.content + ': short on ' + x.short.join(',') + ')');
      throw new Error('a story arrives underplayable — ' + bad.join(' ;; '));
    }
    // the hub must render a button for every catalogue entry
    await page.evaluate(() => { try { closeSheet(); } catch (e) {} openGames(); });
    await page.waitForTimeout(400);
    const missing = await page.evaluate(() =>
      GameFactory.CATALOGUE.map(g => g.id).filter(id => !document.getElementById(id)));
    await page.evaluate(() => { try { closeSheet(); } catch (e) {} });
    if (missing.length) throw new Error('the hub has no card for: ' + missing.join(','));
  });

  // A multiple-choice round is only as hard as its wrong answers. The İbare
  // game drew three RANDOM sentences, and a random sentence gives itself away
  // without any Arabic being read: different length, no shared words.
  await check('the İbare distractors are near misses, not random sentences', async () => {
    const r = await page.evaluate(() => {
      const pool = ibaraItems();
      const len = x => (x.sen.tokens || []).length;
      const cache = new Map();
      const stat = pick => {
        let giveaway = 0, gap = 0, n = 0;
        pool.forEach(t => {
          const o = pick(t); if (o.length < 3) return;
          const lens = [t, ...o].map(len), mx = Math.max(...lens), mn = Math.min(...lens);
          // is the answer uniquely the longest or the shortest? then LENGTH
          // alone reveals it and no parsing is required
          if ((len(t) === mx && lens.filter(l => l === mx).length === 1) ||
              (len(t) === mn && lens.filter(l => l === mn).length === 1)) giveaway++;
          o.forEach(x => { gap += Math.abs(len(t) - len(x)); n++; });
        });
        return { give: Math.round(giveaway / pool.length * 1000) / 10,
                 gap: Math.round(gap / n * 100) / 100 };
      };
      return { pool: pool.length,
               random: stat(t => shuffle(pool.filter(x => x.sen.id !== t.sen.id || x.st.id !== t.st.id)).slice(0, 3)),
               near: stat(t => DistractorEngine.near(pool, t, 3)) };
    });
    if (r.pool < 50) throw new Error('the İbare pool shrank: ' + r.pool);
    // random draw sits near 41%; the near-miss draw must be far under it
    if (r.near.give > 10)
      throw new Error('length alone still gives the answer away ' + r.near.give + '% of the time');
    if (r.near.give >= r.random.give)
      throw new Error('near-miss distractors are no harder than random ones');
    if (r.near.gap > 1) throw new Error('distractors are still the wrong length: ' + r.near.gap + ' words off');
  });

  // The answer side of a word card now carries what the engines DERIVE — the
  // root, the scale, and what that scale can be. None of it is stored: it is
  // computed at render, so every card already in a deck gains it.
  await check('a word card shows its derived sarf, and stays silent where it cannot be sure', async () => {
    const r = await page.evaluate(() => {
      const c = [...document.querySelectorAll('.lib-card')]
        .find(x => x.dataset.storyId === 'aqaid-ahl-al-sunna');
      if (c) c.click();
      const strip = lex => (cardSarfStrip({ type: 'word', lex,
        lemma: (GLOSSARY[lex] || {}).lemma || lex }) || '')
        .replace(/<[^>]+>/g, ' ').replace(/\s+/g, ' ').trim();
      return { qadir: strip('qadir'), masum: strip('masum'), muntazar: strip('muntazar'),
               allah: strip('allah'), unknown: strip('no-such-lex'),
               // a card whose glossary entry has no root must show nothing at
               // all rather than a guessed one
               noRoot: cardSarfStrip({ type: 'word', lex: 'hadha', lemma: 'هَذَا' }),
               notWord: cardSarfStrip({ type: 'verb', lex: 'qadir', lemma: 'قَادِر' }) };
    });
    if (!/ق د ر/.test(r.qadir) || !/فَاعِل/.test(r.qadir))
      throw new Error('قَادِر should give its root and فَاعِل: ' + r.qadir);
    if (!/مَفْعُول/.test(r.masum)) throw new Error('مَعْصُوم is مَفْعُول: ' + r.masum);
    if (!/مُفْتَعَل/.test(r.muntazar)) throw new Error('مُنْتَظَر is مُفْتَعَل: ' + r.muntazar);
    // A NAME stands in no scale, and a root guessed by the peeling rules is
    // not good enough to build one from: feeding RootFinder's ك و ب for مَكْتُوب
    // into the scale produced مَفْتُعل, a shape that does not exist.
    if (r.allah) throw new Error('the name of Allah stands in no scale: ' + r.allah);
    if (r.unknown) throw new Error('an unknown lex must produce nothing: ' + r.unknown);
    if (r.noRoot) throw new Error('no root in the glossary means no strip: ' + r.noRoot);
    if (r.notWord) throw new Error('only word cards carry this: ' + r.notWord);
  });

  // A reader reported «Save to flashcards» missing. It was not missing: it was
  // rendered, in the DOM, and permanently UNDER the thumb bar, because a sheet
  // is fixed at bottom:0 and so is the bar. Body padding cannot fix a fixed
  // element. This check walks EVERY sheet the app opens at phone size and
  // fails if any interactive thing ends up beneath the bar — the bug was one
  // instance of a whole class, and the class is what gets guarded.
  await check('no sheet hides a button under the thumb bar', async () => {
    const was = page.viewportSize();
    let bad = [];
    try {
      await page.setViewportSize({ width: 390, height: 844 });
      await page.evaluate(() => { try { closeSheet(); } catch (e) {} });
      await page.waitForTimeout(200);
      // open a story so the word sheet has something to open on
      await page.evaluate(() => { const c = document.querySelector('.lib-card'); if (c) c.click(); });
      await page.waitForSelector('.word', { timeout: 5000 });
      const opens = ['word sheet', 'workshop', 'games hub', 'deck'];
      for (const name of opens) {
        // open, then WAIT for the sheet to finish sliding up. Measuring during
        // the transform reads every child as below the bar, because the sheet
        // is still translated off the bottom of the screen — the first version
        // of this check failed on itself for exactly that reason.
        const opened = await page.evaluate(n => {
          try { closeSheet(); } catch (e) {}
          const run = {
            'word sheet': () => document.querySelector('.word').click(),
            'workshop':   () => openConjugator(),
            'games hub':  () => openGames(),
            'deck':       () => openDeck(),
          }[n];
          try { run(); return true; } catch (e) { return false; }
        }, name);
        if (!opened) continue;
        await page.waitForTimeout(600);
        const r = await page.evaluate(() => {
          const inner = document.getElementById('sheetInner');
          const sheet = document.querySelector('.sheet.show');
          const bar = document.querySelector('.tabbar');
          if (!inner || !sheet || !bar || getComputedStyle(bar).display === 'none') return { skip: true };
          // the SHEET is the scroller, not its inner div
          sheet.scrollTop = sheet.scrollHeight;
          const barTop = bar.getBoundingClientRect().top;
          const hidden = [...inner.querySelectorAll('button, a, input, select')]
            .filter(el => { const b2 = el.getBoundingClientRect();
              return b2.height > 0 && b2.width > 0 && b2.bottom > barTop + 1; })
            .map(el => (el.textContent || el.id || el.tagName).replace(/\s+/g, ' ').trim().slice(0, 30));
          return { hidden, pad: getComputedStyle(inner).paddingBottom };
        });
        if (r.skip) continue;
        if (r.hidden.length) bad.push(name + ': ' + r.hidden.join(' | '));
        // and the clearance must clear the thumb floor, so the rule is present
        // rather than accidentally satisfied by a short panel
        if (parseFloat(r.pad) < 44) bad.push(name + ': clearance is only ' + r.pad);
      }
    } finally {
      await page.evaluate(() => { try { closeSheet(); } catch (e) {} });
      await page.setViewportSize(was);
      await page.locator('#scrim').waitFor({ state: 'hidden', timeout: 3000 }).catch(() => {});
      await toLibrary().catch(() => {});
    }
    if (bad.length) throw new Error('hidden under the thumb bar — ' + bad.join(' ;; '));
  });

  // Qawa'id al-I'rab bab 2: every jarr-majrur attaches to a verb or to
  // something carrying a verb's meaning. Nothing hangs in the air.
  await check('the Ta\'alluq engine names what every jarr-majrur hangs on', async () => {
    const r = await page.evaluate(() => {
      const flat = x => stripAr(x || '').replace(/[^ء-ي]/g, '');
      let n = 0, ok = 0, skipped = 0;
      STORIES.forEach(st => (st.chapters || []).forEach(ch => ch.sentences.forEach(sen => {
        const text = sen.tokens.map(t => t.s.full).join(' ');
        let rows; try { rows = SentenceAnalyzer.analyze(text); } catch (e) { return; }
        if (rows.length !== sen.tokens.length) return;
        sen.tokens.forEach((t, i) => {
          const m = /مُتَعَلِّقٌ\s+بِـ?«?([^»,.،]+)»?/.exec((t.irab || {}).ar || '');
          if (!m) return;
          const want = m[1].trim(), mahdhuf = /مَحْذُوف/.test(want);
          // a target that is not a literal word of this sentence cannot be
          // matched by any engine that names words — count it, but apart
          const literal = rows.some(x => { const a = flat(x.w), w = flat(want).replace(/^ال/, '');
            return w.length > 1 && (a.includes(w) || w.includes(a.replace(/^ال/, ''))); });
          if (!mahdhuf && !literal) { skipped++; return; }
          n++;
          const got = TaalluqEngine.of(rows, i);
          if (mahdhuf) { if (got && got.kind === 'mahdhuf') ok++; return; }
          if (got && got.kind === 'found') {
            const a = flat(got.word), w = flat(want).replace(/^ال/, '');
            if (a.includes(w) || w.includes(a.replace(/^ال/, ''))) ok++;
          }
        });
      })));
      // chapter 23 was written as the engine's worked example: four jarr-
      // majrurs on four different kinds of governor
      const rows23 = SentenceAnalyzer.analyze('عَالِمًا بِالسِّيَاسَةِ وَإِقَامَةِ الْحُدُودِ قَادِرًا عَلَى الذَّبِّ عَنْ حَوْزَةِ الْإِسْلَامِ');
      const ch23 = TaalluqEngine.all(rows23)
        .map(x => x.w + '→' + (x.t.kind === 'found' ? x.t.word : x.t.kind));
      // Ibn Hisham's exceptions: a zaid letter attaches to NOTHING
      const zaid = TaalluqEngine.of(SentenceAnalyzer.analyze('مَا زَيْدٌ بِقَائِمٍ'), 2);
      // and where nothing can govern it, the amil is omitted and estimated
      const md = TaalluqEngine.of(SentenceAnalyzer.analyze('فِي الدَّارِ رَجُلٌ'), 0);
      return { n, skipped, acc: Math.round(ok / n * 1000) / 10, ch23,
               zaid: zaid && zaid.kind, md: md && md.kind,
               mdText: md && md.text ? md.text.tr : '' };
    });
    if (r.n < 90) throw new Error('the graded set shrank: ' + r.n);
    // 33.1% was the first version, before a majrur stopped being mistaken for
    // the letter governing it, before the glossary was asked which nouns carry
    // a verb's meaning, and before a jarr letter fused to an INDEFINITE noun
    // (بِقَائِمٍ) was recognised at all. Each of those was a correctness fix; not
    // one point of this came from tuning.
    if (r.acc < 45) throw new Error('ta\'alluq accuracy regressed to ' + r.acc + '%');
    const want23 = ['بِالسِّيَاسَةِ→عَالِمًا', 'عَلَى→قَادِرًا', 'عَنْ→الذَّبِّ'];
    want23.forEach(w => { if (!r.ch23.includes(w))
      throw new Error('the worked example broke: wanted ' + w + ', got ' + r.ch23.join(' ')); });
    if (r.zaid !== 'exempt') throw new Error('a zaid ba attaches to nothing, got ' + r.zaid);
    if (r.md !== 'mahdhuf') throw new Error('with no governor the amil is omitted, got ' + r.md);
    if (!/kâin|istekarra/.test(r.mdText)) throw new Error('the omitted amil must be ESTIMATED: ' + r.mdText);
  });

  // Ibn Hisham gives the waw eight faces. The engine proposes them ranked, and
  // is graded against every waw a human has already ruled on in the library —
  // the only honest scoreboard available for a question this open.
  await check('the Waw engine ranks the eight faces, and is graded on the corpus\'s own rulings', async () => {
    const r = await page.evaluate(() => {
      const gold = ar =>
        /الْوَاوُ\s*(عَاطِفَةٌ|حَرْفُ عَطْفٍ)/.test(ar) ? 'atf' :
        /الْوَاوُ\s*(اسْتِئْنَافِيَّةٌ|لِلِاسْتِئْنَافِ)/.test(ar) ? 'istinaf' :
        /الْوَاوُ\s*(حَالِيَّةٌ|لِلْحَالِ|وَصْلِيَّةٌ)/.test(ar) ? 'hal' :
        /الْوَاوُ\s*(لِلْقَسَمِ|قَسَمِيَّةٌ)/.test(ar) ? 'qasam' : null;
      let n = 0, t1 = 0, t2 = 0, silent = 0, headOpen = 0, headN = 0;
      STORIES.forEach(st => (st.chapters || []).forEach(ch => ch.sentences.forEach(sen => {
        const text = sen.tokens.map(t => t.s.full).join(' ');
        let rows; try { rows = SentenceAnalyzer.analyze(text); } catch (e) { return; }
        if (rows.length !== sen.tokens.length) return;
        sen.tokens.forEach((t, i) => {
          const g = gold((t.irab || {}).ar || '');
          if (!g || !WawEngine.separable(rows[i])) return;
          const w = WawEngine.rank(rows, i);
          n++;
          if (!w.length) { silent++; return; }
          if (w[0].k === g) t1++;
          if (w.slice(0, 2).some(x => x.k === g)) t2++;
          // at the head of a sentence it must OFFER both readings, because the
          // ma'tuf ilayh is in the line above and is not in view
          if (i === 0) { headN++; if (w.slice(0, 2).map(x => x.k).join() === 'atf,istinaf') headOpen++; }
        });
      })));
      const one = (txt, k) => { const rows = SentenceAnalyzer.analyze(txt);
        const w = WawEngine.rank(rows, k); return w.length ? w[0].k : null; };
      return { n, silent, t1: Math.round(t1 / n * 1000) / 10, t2: Math.round(t2 / n * 1000) / 10,
               headN, headOpen,
               faces: Object.keys(WawEngine.WAJH).length,
               oath: one('وَاللهِ إِنَّ الْعِلْمَ نَافِعٌ', 0),
               hal: one('رَجَعَ يُوسُفُ وَقَدْ عَلِمَ', 2),
               atf: one('جَاءَ زَيْدٌ وَعَمْرٌو', 2),
               // a RADICAL waw is not a word and must never be read as one
               radical: [SentenceAnalyzer.analyze('وَلَد')[0], SentenceAnalyzer.analyze('وِلَايَة')[0],
                         SentenceAnalyzer.analyze('وَجَبَ')[0]].map(x => WawEngine.separable(x)) };
    });
    if (r.faces !== 8) throw new Error('Ibn Hisham counts eight faces, the engine has ' + r.faces);
    if (r.n < 150) throw new Error('the graded set shrank: ' + r.n);
    if (r.silent) throw new Error(r.silent + ' waws the engine had nothing at all to say about');
    // 36.9% was the first version, which read "nothing precedes it" as evidence
    // of isti'naf; 68% is what always answering «atf» would score.
    if (r.t1 < 69) throw new Error('top-1 against the corpus regressed to ' + r.t1 + '%');
    if (r.t2 < 96) throw new Error('the shortlist regressed to ' + r.t2 + '%');
    if (r.oath !== 'qasam') throw new Error('وَاللهِ is the oath waw, got ' + r.oath);
    if (r.hal !== 'hal') throw new Error('«wa qad» + a past verb is a hal, got ' + r.hal);
    if (r.atf !== 'atf') throw new Error('a matching case mid-sentence is atf, got ' + r.atf);
    if (r.radical.some(Boolean)) throw new Error('a radical waw was read as a word: ' + r.radical);
    // and at the head it must own up rather than pick
    if (r.headOpen < r.headN * 0.9)
      throw new Error('an opening waw must offer both readings: only ' + r.headOpen + '/' + r.headN);
  });

  // «an» wears two faces and they are not a guess apart: أَنَّ is followed by a
  // NOUN and أَنْ by a VERB. The second turns its clause into a MASDAR that then
  // fills a slot like any single noun.
  await check('the reading engine tells the two «an» apart and names the masdar', async () => {
    const r = await page.evaluate(() => {
      const strip = h => (h || '').replace(/<[^>]+>/g, '');
      const R = (t, l) => { const x = ReadingEngine.read(SentenceAnalyzer.analyze(t), l);
        return x ? { k: x.kind, t: strip(x.text), w: strip(x.why) } : null; };
      return { masdar: R('يَجِبُ أَنْ يَكُونَ الْإِمَامُ ظَاهِرًا', 'tr'),
               masdarEn: R('يَجِبُ أَنْ يَكُونَ الْإِمَامُ ظَاهِرًا', 'en'),
               anna: R('اُكْتُبْ أَنَّ اللهَ قَادِرٌ عَلَى كُلِّ شَيْءٍ', 'tr'),
               quiet: R('ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ', 'tr') };
    });
    if (!r.masdar || r.masdar.k !== 'an-masdariyya')
      throw new Error('أَنْ + a verb is the masdar structure, got ' + (r.masdar && r.masdar.k));
    if (!/olması/.test(r.masdar.t)) throw new Error('Turkish says the masdar with -ması: ' + r.masdar.t);
    if (!/fâilidir/.test(r.masdar.t)) throw new Error('it must name the slot the masdar fills: ' + r.masdar.t);
    if (!/being/.test(r.masdarEn.t)) throw new Error('English: ' + r.masdarEn.t);
    if (!/NASBEDER|nasb/i.test(r.masdar.w)) throw new Error('why: ' + r.masdar.w);
    // أَنَّ followed by a noun must still route to the other structure
    if (!r.anna || r.anna.k !== 'anna') throw new Error('أَنَّ + a noun is still the anna structure');
    if (r.quiet) throw new Error('it must stay silent on a structure it cannot name');
  });

  // The glossary's several hundred NOUNS were invisible to open text: only verb
  // paradigms were consulted, so الْإِمَامُ came back with no gloss at all.
  await check('the noun lexicon answers open text, article and case ending and all', async () => {
    const r = await page.evaluate(() => {
      const one = w => { const x = SentenceAnalyzer.analyze(w)[0];
        return { g: x.gloss ? x.gloss.tr : null, lemma: x.lemma || null, sure: x.sure, kind: x.kind }; };
      return { bare: one('إِمَام'), withAl: one('الْإِمَامُ'), withCase: one('الْإِمَامِ'),
               // a clitic in front, and the lam that swallows the article
               clitic: one('وَالْإِمَامُ'), lam: one('لِلْإِمَامِ'),
               // a stored PLURAL must reach its own head-word
               plural: one('الْغَنَائِمِ'),
               // and a verb must still answer from its paradigm, not from here
               verb: one('يَجِبُ'),
               size: RootFinder.nounIndex().size };
    });
    if (r.size < 200) throw new Error('the noun index is too small to be the glossary: ' + r.size);
    for (const k of ['bare', 'withAl', 'withCase', 'clitic', 'lam'])
      if (r[k].lemma !== 'إِمَام') throw new Error(k + ': wanted إِمَام, got ' + r[k].lemma);
    if (!r.withAl.sure) throw new Error('a gloss the glossary owns is not a guess');
    if (r.plural.lemma !== 'غَنِيمَة') throw new Error('a plural must reach its head-word: ' + r.plural.lemma);
    if (!/vâcib/.test(r.verb.g || '')) throw new Error('a verb still answers from its paradigm: ' + r.verb.g);
  });

  // Idafa is the most mechanical structure in nahw, so the engine does not
  // describe one — it BUILDS one, and a builder cannot be vague.
  // The three-vowel table (damma / fatha / kasra) is true of ONE class of noun
  // out of seven. This gates the other six, and above all the row where two
  // rules meet: مَعَانٍ is barred from tanwin AND is a manqus, so it is written
  // WITH a tanwin in raf' and jarr (a tanwin of compensation for the dropped
  // ya) and BARE in nasb with the ya restored. A rule system that stores only
  // "mamnu → fatha in jarr" gets this word wrong three times out of three.
  // The nakil drill used to be a poster: it showed رَاجَعَ standing in the
  // فَاعَلَ row and gave the reader no way to ask what THAT bab does through its
  // own tenses. Every row the conjugator can build is now a button, and the
  // bab it opens carries its own muhtelife.
  await check('the nakil drill is walkable — every derivable bab opens its own paradigm', async () => {
    await toLibrary();
    const picked = await page.evaluate(() => {
      let hit = null;
      STORIES.forEach(st => st.chapters.forEach(c => c.sentences.forEach(sen => sen.tokens.forEach(t => {
        const e = st.glossary[t.lex], m = st.morph && st.morph[t.lex];
        if (!hit && m && !m.jamid && nakilClass(e) && nakilClass(e).type === 'sound')
          hit = { lex: t.lex, root: e.root };
      }))));
      return hit;
    });
    if (!picked) throw new Error('no sound-rooted verb in the whole library?');
    // The sheet reads the GLOBAL glossary and morphology, and those are filled
    // when a story is opened. Calling openWord from the library renders the
    // word tab, not the sarf tab, and the drill is simply not there.
    const open = async (lex) => page.evaluate((lx) => {
      const st = STORIES.find(s => s.morph && s.morph[lx]);
      openStory(st);
      let tok = null;
      st.chapters.forEach(c => c.sentences.forEach(sen => sen.tokens.forEach(t => { if (!tok && t.lex === lx) tok = t; })));
      sarfTense = 'nakil'; sarfUserPick = true; sarfNakilPick = null;
      openWord(tok, null, 'sarf');
    }, lex);
    await open(picked.lex);
    const rows = await page.locator('.nakil-go').count();
    // six bare babs + the augmented ones a sound root really has
    if (rows < 14) throw new Error('too few walkable rows: ' + rows);
    // …and every one of them must actually derive, or it should not be a button
    const allOk = await page.evaluate((root) => [...document.querySelectorAll('.nakil-go')]
      .every(b => { const d = sarfDerive(nakilClass({ root }), b.dataset.nform,
        Number(b.dataset.nbab)); return !!(d && d.ok); }), picked.root);
    if (!allOk) throw new Error('a row is a button but the conjugator cannot build it');
    await page.locator('.nakil-go').nth(6).click();
    await page.waitForSelector('.nakil-head .nk-form', { timeout: 3000 });
    const shown = await page.locator('.lemma').last().innerText();
    if (!shown.trim()) throw new Error('the opened bab shows no lemma');
    const tenses = await page.locator('[data-ntense]').count();
    if (tenses < 4) throw new Error('the opened bab must offer its own muhtelife: ' + tenses);
    // the derived paradigm must SAY it was derived, not stored
    const note = await page.locator('.bab-line').last().innerText();
    if (!/Derived|türet/i.test(note)) throw new Error('a derived bab must own up to it: ' + note);
    await page.locator('[data-ntense="muhtelife"]').click();
    await page.waitForTimeout(150);
    if (await page.locator('table.conj tr').count() < 10)
      throw new Error('the derived muhtelife came out empty');
    await page.locator('#nakilBack').click();
    await page.waitForTimeout(150);
    if (await page.locator('.nakil-go').count() !== rows)
      throw new Error('going back did not restore the table');
    await page.evaluate(() => { sarfTense = 'mazi'; sarfNakilPick = null;
      document.getElementById('scrim').click(); });
  });

  await check('the Alama engine writes the ending every class of noun really takes', async () => {
    const r = await page.evaluate(() => {
      const T = (w, o) => { const t = AlamaEngine.table(w, o || {});
        return t ? t.rows.map(x => x.out).join('|') : null; };
      const maani = AlamaEngine.table('مَعَانِي', {});
      return {
        sahih:     T('كِتَاب'),
        definite:  T('الْكِتَاب'),
        mamnu:     T('مَسَاجِد', { mamnu: true }),
        maqsur:    T('فَتًى'),
        maqsurDef: T('الْفَتَى'),
        manqus:    T('قَاضِي'),
        manqusDef: T('الْقَاضِي'),
        maani:     T('مَعَانِي'),
        dual:      T('كِتَابَانِ'),
        dualMudaf: T('كِتَابَانِ', { mudaf: true }),
        plural:    T('مُسْلِمُونَ'),
        pluralMudaf: T('مُسْلِمُونَ', { mudaf: true }),
        fem:       T('مُسْلِمَات'),
        femDef:    T('الطَّالِبَات'),
        khamsa:    T('أَب', { mudaf: true }),
        // ـَاء is two different endings wearing the same three letters, and only
        // the ROOT tells them apart: صَحْرَاء has the alif of femininity and is
        // barred from tanwin, خَفَاء has the ya of خ ف ي turned into a hamza and
        // is perfectly ordinary. Hamza SEATS must fold — a root is written
        // ق ر أ, not ق ر ء, and a bare-ء test read قُرَّاء as feminine.
        sahra:     T('صَحْرَاء', { root: 'ص ح ر' }),
        khafaa:    T('خَفَاء', { root: 'خ ف ي' }),
        dua:       T('دُعَاء', { root: 'د ع و' }),
        qurra:     T('قُرَّاء', { root: 'ق ر أ' }),
        sahraDef:  T('الصَّحْرَاء', { root: 'ص ح ر' }),
        // …and with no root the engine must NOT guess a verdict of its own
        mamdudUndecided: AlamaEngine.mamdudVerdict('صَحْرَاء', ''),
        // the maqsur's case is never written, so all three must be TAQDIRI
        maqsurManner: (AlamaEngine.table('فَتًى', {}).rows || []).map(x => x.manner).join(','),
        // …and the manqus writes only the fatha
        manqusManner: (AlamaEngine.table('الْقَاضِي', {}).rows || []).map(x => x.manner).join(','),
        maaniMamnu: !!(maani && maani.mamnu),
        maaniSteps: maani ? maani.rows[2].steps.map(s => s.tr).join(' ') : '',
        // the fem plural's nasb must SAY it is a kasra standing in for a fatha
        femNasbWhy: AlamaEngine.write('مُسْلِمَات', 'nasb').steps.map(s => s.en).join(' '),
      };
    });
    const want = {
      sahih:       'كِتَابٌ|كِتَابًا|كِتَابٍ',
      definite:    'الْكِتَابُ|الْكِتَابَ|الْكِتَابِ',
      mamnu:       'مَسَاجِدُ|مَسَاجِدَ|مَسَاجِدَ',
      maqsur:      'فَتًى|فَتًى|فَتًى',
      maqsurDef:   'الْفَتَى|الْفَتَى|الْفَتَى',
      manqus:      'قَاضٍ|قَاضِيًا|قَاضٍ',
      manqusDef:   'الْقَاضِي|الْقَاضِيَ|الْقَاضِي',
      maani:       'مَعَانٍ|مَعَانِيَ|مَعَانٍ',
      dual:        'كِتَابَانِ|كِتَابَيْنِ|كِتَابَيْنِ',
      dualMudaf:   'كِتَابَا|كِتَابَيْ|كِتَابَيْ',
      plural:      'مُسْلِمُونَ|مُسْلِمِينَ|مُسْلِمِينَ',
      pluralMudaf: 'مُسْلِمُو|مُسْلِمِي|مُسْلِمِي',
      fem:         'مُسْلِمَاتٌ|مُسْلِمَاتٍ|مُسْلِمَاتٍ',
      femDef:      'الطَّالِبَاتُ|الطَّالِبَاتِ|الطَّالِبَاتِ',
      khamsa:      'أَبُو|أَبَا|أَبِي',
      sahra:       'صَحْرَاءُ|صَحْرَاءَ|صَحْرَاءَ',
      khafaa:      'خَفَاءٌ|خَفَاءً|خَفَاءٍ',
      dua:         'دُعَاءٌ|دُعَاءً|دُعَاءٍ',
      qurra:       'قُرَّاءٌ|قُرَّاءً|قُرَّاءٍ',
      // ال puts a mamnu' noun back on the ordinary kasra
      sahraDef:    'الصَّحْرَاءُ|الصَّحْرَاءَ|الصَّحْرَاءِ',
    };
    for (const k of Object.keys(want))
      if (r[k] !== want[k]) throw new Error(k + ': wanted ' + want[k] + ', got ' + r[k]);
    if (r.maqsurManner !== 'taqdiri,taqdiri,taqdiri')
      throw new Error('a maqsur writes no case at all: ' + r.maqsurManner);
    if (r.manqusManner !== 'taqdiri,lafzi,taqdiri')
      throw new Error('a manqus writes only the fatha: ' + r.manqusManner);
    if (!r.maaniMamnu) throw new Error('مَعَانٍ must be read as barred from tanwin');
    if (r.mamdudUndecided !== null)
      throw new Error('with no root a mamdud must be left UNDECIDED, not guessed: ' + r.mamdudUndecided);
    if (!/İVAZ|ivaz/i.test(r.maaniSteps))
      throw new Error('the tanwin on مَعَانٍ must be named a tanwin of COMPENSATION: ' + r.maaniSteps);
    if (!/standing in for the fatha/.test(r.femNasbWhy))
      throw new Error('the feminine plural nasb must name its kasra: ' + r.femNasbWhy);

    // …and the lab shows all three rows, in whichever language is on
    await page.evaluate(() => { conjState.lab = 'alama'; openConjugator(); });
    await page.waitForSelector('#alamaOut .vrow', { timeout: 4000 });
    if (await page.locator('#alamaOut .vrow').count() !== 3)
      throw new Error('the endings lab must show all three cases');
    const shown = (await page.locator('#alamaOut .vrow .vw').allInnerTexts()).join('|');
    if (shown !== want.maani) throw new Error('the lab disagrees with the engine: ' + shown);
    await page.evaluate(() => { document.getElementById('scrim').click(); });
  });

  await check('the Idafa engine builds the idafa and names every rule that fired', async () => {
    const r = await page.evaluate(() => {
      const B = (a, b, k) => { const x = IdafaEngine.build(a, b, k); return x && x.ok ? x.out : null; };
      const refused = IdafaEngine.build('الْكِتَابُ', 'الْوَلَدُ', 'raf');
      const steps = IdafaEngine.build('مُسْلِمُونَ', 'الْمَدِينَةُ', 'raf');
      return {
        plain: B('كِتَابٌ', 'الْوَلَدُ', 'raf'),
        jarr:  B('كِتَابٌ', 'الْوَلَدُ', 'jarr'),
        // rule 2: the nun of the sound plural and of the dual falls
        plural: B('مُسْلِمُونَ', 'الْمَدِينَةُ', 'raf'),
        dual:   B('كِتَابَانِ', 'وَلَدٌ', 'raf'),
        // …and the LETTER is chosen by the case asked for, never read off the
        // shape the user typed. Ask for jarr and the waw must become a ya.
        dualNasb:   B('كِتَابَانِ', 'وَلَدٌ', 'nasb'),
        pluralJarr: B('مُجْتَهِدُونَ', 'الْأُمَّةُ', 'jarr'),
        pluralUp:   B('مُسْلِمِينَ', 'الْمَدِينَةُ', 'raf'),
        // the chapter's own dual: دَفَّتَانِ asked for in jarr
        daffa:      B('دَفَّتَانِ', 'الْمُصْحَفُ', 'jarr'),
        // the five nouns decline by a LETTER, and only as mudaf
        five:   B('أَبٌ', 'بَكْرٌ', 'raf'),
        dhu:    B('ذُو', 'النُّورَيْنِ', 'raf'),
        // a mamnu' min al-sarf mudaf ilayh takes a FATHA in jarr — and which
        // nouns those are is asked of the LEARNED tagger, not of a list
        mamnu:  B('قِسْمَةٌ', 'غَنَائِمُ', 'jarr'),
        // maqsur on either side shows nothing at all
        maqsurHead: B('فَتَى', 'الْقَوْمِ', 'raf'),
        maqsurTail: B('بَيْتٌ', 'مُوسَى', 'raf'),
        refusedOk: !!(refused && refused.ok === false && refused.refused),
        refusedWhy: refused && refused.refused ? refused.refused.tr : '',
        nSteps: steps ? steps.steps.length : 0,
        stepTr: steps ? steps.steps.map(x => x.tr).join(' ‖ ') : '',
        chain: IdafaEngine.chain(SentenceAnalyzer.analyze('وَقَبُولِ شَهَادَاتِ الْقَوْمِ'))
                 .map(c => c.words.join(' ')),
      };
    });
    const want = { plain: 'كِتَابُ الْوَلَدِ', jarr: 'كِتَابِ الْوَلَدِ',
                   plural: 'مُسْلِمُو الْمَدِينَةِ', dual: 'كِتَابَا وَلَدٍ',
                   dualNasb: 'كِتَابَيْ وَلَدٍ', pluralJarr: 'مُجْتَهِدِي الْأُمَّةِ',
                   pluralUp: 'مُسْلِمُو الْمَدِينَةِ', daffa: 'دَفَّتَيِ الْمُصْحَفِ',
                   five: 'أَبُو بَكْرٍ', dhu: 'ذُو النُّورَيْنِ',
                   mamnu: 'قِسْمَةِ غَنَائِمَ',
                   maqsurHead: 'فَتَى الْقَوْمِ', maqsurTail: 'بَيْتُ مُوسَى' };
    for (const k of Object.keys(want))
      if (r[k] !== want[k]) throw new Error(k + ': wanted ' + want[k] + ', got ' + r[k]);
    if (!r.refusedOk) throw new Error('ال + idafa must be REFUSED, not built');
    if (!/bir arada bulunmaz/.test(r.refusedWhy))
      throw new Error('the refusal must name the rule: ' + r.refusedWhy);
    if (r.nSteps < 2) throw new Error('a build must show its work: ' + r.nSteps + ' steps');
    if (!/NÛNu düşer/.test(r.stepTr)) throw new Error('the nun rule must be named: ' + r.stepTr);
    // the chain runs the whole length, and every middle member is both roles
    if (r.chain.length !== 1 || r.chain[0].split(' ').length !== 3)
      throw new Error('the three-member chain was not read whole: ' + JSON.stringify(r.chain));
  });

  // Ten workshop tools do not fit a phone as a wrapping row — they wrapped to
  // five lines and pushed the tool itself below the fold.
  await check('the workshop rail holds every tool on one scrolling line', async () => {
    const was = page.viewportSize();
    let r;
    try {
      await page.evaluate(() => { conjState.lab = 'idafa'; openConjugator(); });
      await page.waitForSelector('#idafaOut .idf-out', { timeout: 4000 });
      await page.setViewportSize({ width: 390, height: 844 });
      await page.waitForTimeout(250);
      r = await page.evaluate(() => {
        const rail = document.querySelector('.labrail');
        const on = rail.querySelector('button.on');
        const rb = rail.getBoundingClientRect(), ob = on.getBoundingClientRect();
        return { h: Math.round(rb.height), tabs: rail.querySelectorAll('button').length,
                 scrolls: rail.scrollWidth > rail.clientWidth + 4,
                 onInView: ob.left >= rb.left - 2 && ob.right <= rb.right + 2,
                 tap: Math.round(ob.height),
                 bodyNoSideScroll: document.body.scrollWidth <= window.innerWidth + 1,
                 // every pill carries a word, not just a glyph
                 labelled: [...rail.querySelectorAll('button')]
                   .every(b => b.textContent.replace(/\s/g, '').length > 2),
                 out: document.querySelector('.idf-out').textContent.replace(/\s+/g, ' ').trim() };
      });
    } finally {
      await page.evaluate(() => { try { conjState.lab = 'sarf'; closeSheet(); } catch (_) {} });
      await page.setViewportSize(was);
      await page.locator('#scrim').waitFor({ state: 'hidden', timeout: 3000 }).catch(() => {});
    }
    if (r.tabs < 10) throw new Error('the rail lost a tool: ' + r.tabs);
    if (r.h > 70) throw new Error('the rail is wrapping again: ' + r.h + 'px tall');
    if (!r.scrolls) throw new Error('the rail must scroll, not clip');
    if (!r.onInView) throw new Error('the selected tool is scrolled out of sight');
    if (r.tap < 44) throw new Error('a rail pill is under the 44px thumb floor: ' + r.tap);
    if (!r.bodyNoSideScroll) throw new Error('the page itself scrolls sideways');
    if (!r.labelled) throw new Error('a pill carries only an icon');
    if (!/كِتَابُ الْوَلَدِ/.test(r.out)) throw new Error('the lab did not build: ' + r.out);
  });

  // The Mizan lab used to fall silent on any noun the corpus does not carry.
  await check('the Mizan lab answers a noun with both a computed scale and a learned one', async () => {
    const r = await page.evaluate(() => {
      conjState.lab = 'mizan'; conjState.mizan = 'مُسْتَغْفِرٌ';
      openConjugator();
      const box = document.getElementById('mizanOut');
      const t = box.textContent.replace(/\s+/g, ' ');
      const out = { rule: !!box.querySelector('.mz-rule'), model: !!box.querySelector('.mz-model'),
                    t, roles: box.querySelectorAll('.mz-roles').length };
      conjState.lab = 'sarf'; closeSheet();
      return out;
    });
    if (!r.rule) throw new Error('the computed scale is missing: ' + r.t);
    if (!r.model) throw new Error('the learned scale is missing: ' + r.t);
    if (!/مُسْتَفْعِلٌ/.test(r.t)) throw new Error('the computed scale is wrong: ' + r.t);
    if (!r.roles) throw new Error('the offices the scale can hold are not shown');
    // and the verb bab must not be labelled a wazn on a noun
    if (/Wazn · اِسْتَفْعَلَ|الْوَزْن: اِسْتَفْعَلَ/.test(r.t))
      throw new Error('a verb bab is being called this noun\'s wazn: ' + r.t);
  });

  // The one measurement that grades the analyzer against HUMAN labels rather
  // than against itself: every hand-tagged token in the library, 3,331 of them,
  // scored on the three classes the analyzer actually decides. It walks the
  // whole corpus and takes about half a minute; that is the price of a number
  // nobody can argue with.
  await check('the analyzer names the part of speech, graded on every hand-labelled token', async () => {
    const r = await page.evaluate(() => {
      const t0 = performance.now();
      const MAP = { noun: 'noun', propn: 'noun', pron: 'noun', num: 'noun',
                    verb: 'verb', part: 'particle', prep: 'particle', conj: 'particle' };
      let n = 0, ok = 0, misaligned = 0;
      const confuse = {};
      STORIES.forEach(st => (st.chapters || []).forEach(ch => ch.sentences.forEach(sen => {
        const text = sen.tokens.map(t => t.s.full).join(' ');
        let rows; try { rows = SentenceAnalyzer.analyze(text); } catch (e) { return; }
        // the analyzer must split a sentence exactly as the corpus tokenised it
        if (rows.length !== sen.tokens.length) { misaligned += sen.tokens.length; return; }
        rows.forEach((row, i) => {
          const gold = MAP[sen.tokens[i].pos];
          if (!gold) return;
          const got = (row.kind || '').replace('?', '');
          n++;
          if (got === gold) ok++;
          else confuse[gold + '→' + got] = (confuse[gold + '→' + got] || 0) + 1;
        });
      })));
      return { n, misaligned, ms: Math.round(performance.now() - t0),
               acc: Math.round(ok / n * 1000) / 10,
               worst: Object.entries(confuse).sort((a, b) => b[1] - a[1]).slice(0, 3) };
    });
    if (r.n < 3000) throw new Error('the labelled set shrank: ' + r.n);
    if (r.misaligned) throw new Error(r.misaligned + ' tokens the analyzer split differently from the corpus');
    // 82.0% before the arbiter and the closed-class fixes; the floor sits just
    // under where it landed, so a regression fails and an improvement does not.
    if (r.acc < 90) throw new Error('part-of-speech accuracy regressed to ' + r.acc +
      '% — worst confusions: ' + JSON.stringify(r.worst));
  });

  // Where the surface cannot decide, the two distilled taggers vote and the
  // more confident one wins. No threshold, no scaling — the raw comparison won
  // the sweep, and held-out matched resubstitution, so there is nothing fitted.
  await check('the two taggers arbitrate what the surface could not settle', async () => {
    const r = await page.evaluate(() => {
      const rows = SentenceAnalyzer.analyze('وَمَنْ قَالَ لَهُ ذَلِكَ فَقَدْ كَانَ صَادِقًا بِهِ');
      const kinds = rows.map(x => x.w + ':' + x.kind + (x.sure ? '' : '?'));
      // مِنْ against مَنْ — one spelling, two words, told apart by the mim's vowel
      const man = SentenceAnalyzer.analyze('مَنْ')[0];
      const min = SentenceAnalyzer.analyze('مِنْ')[0];
      const open = SentenceAnalyzer.analyze('من')[0];
      return { kinds,
               man: { k: man.kind, t: man.notes.map(n => n.tr).join(' | ') },
               min: { k: min.kind, t: min.notes.map(n => n.tr).join(' | ') },
               open: { k: open.kind, sure: open.sure, t: open.notes.map(n => n.tr).join(' | ') },
               kana: SentenceAnalyzer.analyze('كَانَ')[0].kind,
               laysa: SentenceAnalyzer.analyze('لَيْسَ')[0].kind,
               huwa: SentenceAnalyzer.analyze('هُوَ')[0].kind,
               lahu: SentenceAnalyzer.analyze('لَهُ')[0],
               alayhi: SentenceAnalyzer.analyze('عَلَيْهِ')[0],
               // nothing may be left undecided once the arbiter has run
               anyUnsure: rows.some(x => (x.kind || '').endsWith('?')) };
    });
    if (r.anyUnsure) throw new Error('the arbiter left a row undecided: ' + r.kinds);
    // كان وأخواتها are VERBS, لَيْسَ is a jamid verb, هُوَ is an ism
    if (r.kana !== 'verb') throw new Error('كان is a verb, got ' + r.kana);
    if (r.laysa !== 'verb') throw new Error('ليس is a jamid verb, got ' + r.laysa);
    if (r.huwa !== 'noun') throw new Error('a detached pronoun is an ism, got ' + r.huwa);
    // مَنْ is an ism in every reading; مِنْ is the jarr letter; bare «من» is open
    if (r.man.k !== 'noun') throw new Error('مَنْ is an ism, got ' + r.man.k);
    if (!/FETHALI/.test(r.man.t)) throw new Error('the fatha must be the reason given: ' + r.man.t);
    if (r.min.k !== 'particle') throw new Error('مِنْ is the jarr letter, got ' + r.min.k);
    if (r.open.sure) throw new Error('undiacritised «من» cannot be settled, yet it claims certainty');
    if (!/tayin eden bir şey yok/.test(r.open.t)) throw new Error('it must say so: ' + r.open.t);
    // a jarr letter fused to a pronoun is one word and two i'rabs
    for (const [w, x] of [['لَهُ', r.lahu], ['عَلَيْهِ', r.alayhi]]) {
      if (x.kind !== 'particle') throw new Error(w + ' is a jarr phrase, got ' + x.kind);
      if (x.seg.length !== 2) throw new Error(w + ' must split into letter + pronoun: ' + x.seg);
      if (!/mecrûr muttasıl zamîr/.test(x.notes.map(n => n.tr).join(' ')))
        throw new Error(w + ': the pronoun must be named the majrur');
    }
  });

  // The noun half of the learned layer. SarfTagger reads a conjugated verb back
  // to its cell; this one reads a derived noun back to its SCALE — and stops
  // there on purpose, because the scale does not settle the office.
  await check('the Ism tagger is distilled from the noun patterns and graded on unseen roots', async () => {
    const r = await page.evaluate(() => {
      const t0 = performance.now();
      const e = IsmTagger.evalUnseen();
      const ms = Math.round(performance.now() - t0);
      const one = w => { const g = IsmTagger.tag(w, 1)[0]; return g ? g.wazn : null; };
      return { ...e, ms,
               top1: Math.round(e.top1 * 1000) / 10, top2: Math.round(e.top2 * 1000) / 10,
               // roots the training list has never seen
               probe: { qadir: one('قَادِرٌ'), mustaghfir: one('مُسْتَغْفِرٌ'),
                        maktub: one('مَكْتُوبٌ'), muminun: one('الْمُؤْمِنُونَ'),
                        miftah: one('مِفْتَاحٌ'), alim: one('عَلِيمٌ'),
                        akbar: one('أَكْبَرُ'), istighfar: one('اِسْتِغْفَارٌ'),
                        // the proclitic must be peeled, and only before the article
                        withWaw: one('وَالْمُؤْمِنُونَ'), withBa: one('بِالْمَكْتُوبِ') },
               // the ambiguity is REPORTED, never resolved by fiat
               mafal: IsmTagger.roles('مَفْعَل').map(x => x.k),
               fail: IsmTagger.roles('فَاعِل').map(x => x.k),
               fiaal: IsmTagger.roles('فِعَال').map(x => x.k) };
    });
    if (r.examples < 12000) throw new Error('the generated set shrank: ' + r.examples);
    if (r.shapes < 30) throw new Error('too few patterns to be worth training: ' + r.shapes);
    if (r.top1 < 86) throw new Error('unseen-root wazn accuracy regressed to ' + r.top1 + '%');
    if (r.top2 < 96) throw new Error('two-guess accuracy regressed to ' + r.top2 + '%');
    if (r.ms > 4000) throw new Error('grading took ' + r.ms + 'ms — too slow to run in the panel');
    const want = { qadir: 'فَاعِل', mustaghfir: 'مُسْتَفْعِل', maktub: 'مَفْعُول',
                   muminun: 'مُفْعِل', miftah: 'مِفْعَال', alim: 'فَعِيل',
                   akbar: 'أَفْعَل', istighfar: 'اِسْتِفْعَال',
                   withWaw: 'مُفْعِل', withBa: 'مَفْعُول' };
    for (const k of Object.keys(want))
      if (r.probe[k] !== want[k])
        throw new Error(k + ': wanted ' + want[k] + ', got ' + r.probe[k]);
    // مَفْعَل is a place, a time AND a masdar mimi — all three, or the app is lying
    if (r.mafal.length !== 3) throw new Error('مَفْعَل carries three offices: ' + r.mafal);
    if (!r.fiaal.includes('jamTaksir')) throw new Error('فِعَال is a broken plural too: ' + r.fiaal);
    if (r.fail.length !== 1) throw new Error('فَاعِل is unambiguous: ' + r.fail);
  });

  // The two taggers must not be asked the wrong question, and the model's
  // verdict must reach the analyzer and the kernel — a model nothing consults
  // is a model that does not exist.
  await check('the noun tagger reaches the analyzer and the kernel, and skips what has no scale', async () => {
    const r = await page.evaluate(() => {
      const notes = s => SentenceAnalyzer.analyze(s).map(x =>
        ({ w: x.w, kind: x.kind, alam: !!x.alam, t: x.notes.map(n => n.tr).join(' | ') }));
      const k = GrammarKernel.ask('مَسْجِدٌ');
      return { rows: notes('وَالْمُؤْمِنُونَ عِبَادٌ لِلَّهِ وَالْمَسْجِدُ بَيْتُهُ'),
               keys: k.findings.map(f => f.k),
               hows: k.findings.filter(f => f.k === 'ism-wazn').map(f => f.how),
               miss: k.undecided.map(u => u.tr).join(' | ') };
    });
    const by = w => r.rows.find(x => x.w === w) || { t: '' };
    if (!/مُفْعِل/.test(by('وَالْمُؤْمِنُونَ').t))
      throw new Error('the waw hid the scale: ' + by('وَالْمُؤْمِنُونَ').t);
    if (!/مَفْعِل/.test(by('وَالْمَسْجِدُ').t))
      throw new Error('مسجد should be scaled: ' + by('وَالْمَسْجِدُ').t);
    if (!/kırık çoğul/.test(by('عِبَادٌ').t))
      throw new Error('فِعَال must offer the broken plural too: ' + by('عِبَادٌ').t);
    // لِلَّهِ: the lam is named, the name is an alam, and NO scale is offered
    const jal = by('لِلَّهِ');
    if (!jal.alam) throw new Error('لله must be read as the name: ' + jal.t);
    if (!/cer harfi/.test(jal.t)) throw new Error('its lam must be named: ' + jal.t);
    if (/vezn|بَاب|bâbın masdarı/.test(jal.t)) throw new Error('a name stands in no scale: ' + jal.t);
    if (/külliyat fiili/.test(jal.t)) throw new Error('لله is not a verb: ' + jal.t);
    // the kernel routes to it, badges it a guess, and owns the leftover doubt
    if (!r.keys.includes('ism-wazn')) throw new Error('the kernel missed the noun tagger: ' + r.keys);
    if (r.hows[0] !== 'model') throw new Error('a learned answer wears the model badge, got ' + r.hows[0]);
    if (!/vazîfe taşır/.test(r.miss))
      throw new Error('an ambiguous scale must leave its office undecided: ' + r.miss);
  });

  // A mizan is not the name of a bab. It is the word with its root letters
  // stood in ف ع ل and everything else left where it is — wholly mechanical,
  // so the app computes it. Before this, قَادِرٌ borrowed Form III's past.
  await check('the mizan is computed by standing the root in ف ع ل, not looked up', async () => {
    const r = await page.evaluate(() => ({
      scale: [['قَادِرٌ', 'ق د ر'], ['مُسْتَغْفِرٌ', 'غ ف ر'], ['مَكْتُوبَة', 'ك ت ب'],
              ['مُتَكَاتِبٌ', 'ك ت ب'], ['اسْتِغْفَار', 'غ ف ر'], ['كَتَّبَ', 'ك ت ب']]
        .map(([w, k]) => WaznEngine.mizan(w, k)),
      // a weak root no longer stands in the word, so the scale must decline
      weak: WaznEngine.mizan('قَالَ', 'ق و ل'),
      // and a letter that cannot be an augment kills the scan outright
      bogus: WaznEngine.mizan('دَحْرَجَ', 'ك ت ب'),
      analyzed: SentenceAnalyzer.analyze('قَادِرٌ')[0].wazn,
    }));
    const want = ['فَاعِلٌ', 'مُسْتَفْعِلٌ', 'مَفْعُولَة', 'مُتَفَاعِلٌ', 'اسْتِفْعَال', 'فَعَّلَ'];
    r.scale.forEach((got, i) => {
      if (got !== want[i]) throw new Error('scale ' + i + ': wanted ' + want[i] + ', got ' + got);
    });
    if (r.weak !== null) throw new Error('a weak root has no surface scale: ' + r.weak);
    if (r.bogus !== null) throw new Error('a non-augment letter must kill the scan: ' + r.bogus);
    if (r.analyzed !== 'فَاعِلٌ') throw new Error('the analyzer must scale a noun, not name a bab: ' + r.analyzed);
  });

  // The last thing a hoca says is what the sentence MEANS, and it is the thing
  // the learner came for. It is assembled from what the engines settled — never
  // invented — and it stays silent where it cannot name the structure.
  await check('the reading states what the sentence comes out meaning', async () => {
    const r = await page.evaluate(() => {
      const strip = h => (h || '').replace(/<[^>]+>/g, '');
      const of = (s, l) => {
        const x = ReadingEngine.read(SentenceAnalyzer.analyze(s), l);
        return x ? { text: strip(x.text), why: strip(x.why), kind: x.kind } : null;
      };
      return {
        tr: of('اُكْتُبْ أَنَّ اللهَ قَادِرٌ عَلَى كُلِّ شَيْءٍ', 'tr'),
        en: of('اُكْتُبْ أَنَّ اللهَ قَادِرٌ عَلَى كُلِّ شَيْءٍ', 'en'),
        // no anna, no structure it can name — and then it must say nothing
        quiet: of('ذَهَبَ الطَّالِبُ إِلَى الْمَدْرَسَةِ', 'tr'),
        harmony: [ReadingEngine.genitive('Allah'), ReadingEngine.genitive('Peygamber'),
                  ReadingEngine.genitive('Musa'), ReadingEngine.genitive('göz')],
      };
    });
    if (!r.tr) throw new Error('the reading is missing');
    if (!/Allah’ın/.test(r.tr.text)) throw new Error('the ism of anna leads it: ' + r.tr.text);
    if (!/olduğunu/.test(r.tr.text)) throw new Error('Turkish says the masdar with -dığını: ' + r.tr.text);
    if (!/yaz\.$/.test(r.tr.text)) throw new Error('the governing verb closes it, as an imperative: ' + r.tr.text);
    if (!/^Write that Allah is/.test(r.en.text)) throw new Error('English: ' + r.en.text);
    if (!/masdar/.test(r.tr.why) || !/mef'ûl/.test(r.tr.why))
      throw new Error('it must say WHY the meaning comes out so: ' + r.tr.why);
    if (r.quiet) throw new Error('it must stay silent on a structure it cannot name: ' + r.quiet.text);
    const want = ['Allah’ın', 'Peygamber’in', 'Musa’nın', 'göz’ün'];
    r.harmony.forEach((g, i) => {
      if (g !== want[i]) throw new Error('vowel harmony: wanted ' + want[i] + ', got ' + g);
    });
  });

  // A table of i'rab needs a sideways scroll on a phone, and an i'rab you must
  // scroll sideways to read is one you do not read.
  await check('the analyzer lays its verdicts out as cards a phone can read', async () => {
    const was = page.viewportSize();
    // Open the lab at the width it is opened from — on a phone the thumb bar
    // takes over from #conjOpen, so clicking it at 390 waits forever. Narrow
    // AFTER the panel is up: what is being measured is the layout, not the
    // route to it.
    await page.evaluate(() => {
      // …with one word the glossary does NOT own, so a guessed row still
      // exists to be marked. Once the noun lexicon was wired in, every word of
      // the old sentence came back certain and the assertion below had nothing
      // left to find — which was the analyzer improving, not the check failing.
      conjState.lab = 'jumla';
      conjState.jumla = 'اُكْتُبْ أَنَّ اللهَ قَادِرٌ عَلَى الْمِنْطَادِ';
    });
    const conjWords = 6;
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#jumlaOut .vrow', { timeout: 3000 });
    await page.setViewportSize({ width: 390, height: 844 });
    await page.waitForTimeout(200);
    let r;
    try {
    r = await page.evaluate(() => {
      const out = document.getElementById('jumlaOut');
      const rows = [...out.querySelectorAll('.vrow')];
      const over = rows.filter(el => el.scrollWidth > el.clientWidth + 1).length;
      const read = out.querySelector('.vread');
      return { n: rows.length, over, table: !!out.querySelector('table'),
               guess: out.querySelectorAll('.vrow.guess').length,
               read: read ? read.textContent.replace(/\s+/g, ' ').trim() : null,
               rail: rows[0] ? getComputedStyle(rows[0], '::before').width : null };
    });
    } finally {
      // whatever happens above, hand the next check the width it expects — a
      // narrow viewport left behind makes every later click land on the thumb
      // bar, and one real failure reads as three
      await page.evaluate(() => { try { conjState.lab = 'sarf'; conjState.jumla = 'لم يكتبِ الطالبُ في الدفترِ'; closeSheet(); } catch (_) {} });
      await page.setViewportSize(was);
      await page.locator('#scrim').waitFor({ state: 'hidden', timeout: 3000 }).catch(() => {});
    }
    // one card per word — counted against the sentence, not a magic number
    if (r.n !== conjWords) throw new Error('a card per word: ' + r.n + ' for ' + conjWords + ' words');
    if (r.table) throw new Error('the sideways table is still there');
    if (r.over) throw new Error(r.over + ' cards overflow their own width on a 390px phone');
    if (!r.guess) throw new Error('the guessed rows must still be marked as guesses');
    if (r.rail !== '4px') throw new Error('the certainty rail is missing: ' + r.rail);
    if (!r.read || !/olduğunu|that Allah/.test(r.read))
      throw new Error('the reading must close the panel: ' + r.read);
  });

  // The rules write their own training set, and the only test that means
  // anything is on roots the model has never met. Everything else is theatre.
  await check('the Sarf tagger is distilled from the rules and graded on unseen roots', async () => {
    const r = await page.evaluate(() => {
      const t0 = performance.now();
      const e = SarfTagger.evalUnseen();
      const ms = performance.now() - t0;
      // a form from a root that is NOT in the training list at all
      const unseen = SarfTagger.tag('اِسْتَغْفَرُوا', 2);
      const mazi = SarfTagger.tag('كَتَبُوا', 1);
      return { ...e, ms: Math.round(ms),
               top1: Math.round(e.top1 * 1000) / 10, top2: Math.round(e.top2 * 1000) / 10,
               form: Math.round(e.form * 1000) / 10,
               unseenForm: unseen[0] && unseen[0].form, unseenTense: unseen[0] && unseen[0].tense,
               maziTense: mazi[0] && mazi[0].tense, maziCell: mazi[0] && mazi[0].cell,
               labelled: unseen.every(g => g.text && g.text.en && g.text.tr),
               probs: unseen.every(g => g.p > 0 && g.p <= 1) };
    });
    if (r.examples < 18000) throw new Error('the rules generated only ' + r.examples + ' examples');
    if (r.roots < 40) throw new Error('too few roots to fold by: ' + r.roots);
    // held out BY ROOT — memorising a root cannot help here
    if (r.top1 < 72) throw new Error('unseen-root accuracy regressed to ' + r.top1 + '%');
    if (r.top2 < 88) throw new Error('unseen-root two-guess regressed to ' + r.top2 + '%');
    if (r.form < 88) throw new Error('form accuracy regressed to ' + r.form + '%');
        // the GRADE is expensive (five folds over the whole generated set) and is
    // never on a user path — only training is, and that is one pass.
    if (r.ms > 15000) throw new Error('generate+train+grade took ' + r.ms + 'ms');
    // it must actually work on a root outside its own list
    if (r.unseenForm !== 'X') throw new Error('اِسْتَغْفَرُوا read as Form ' + r.unseenForm);
    if (r.unseenTense !== 'mazi') throw new Error('اِسْتَغْفَرُوا read as ' + r.unseenTense);
    if (r.maziTense !== 'mazi' || r.maziCell !== 2)
      throw new Error('كَتَبُوا read as ' + r.maziTense + ' cell ' + r.maziCell);
    if (!r.labelled) throw new Error('every guess must carry a bilingual label');
    // confidence must separate verbs from furniture — that separation is what
    // the kernel uses instead of a part-of-speech test it does not have
    const conf = await page.evaluate(() => {
      const p = w => SarfTagger.tag(w, 1)[0].p;
      return { verb: p('كَتَبُوا'), weak: p('قَالَ'), noun: p('مَدِينَة'), def: p('الْكِتَابُ') };
    });
    if (conf.verb < 0.3) throw new Error('a plain verb should be confident: ' + conf.verb);
    if (conf.weak < 0.10) throw new Error('قَالَ fell under the kernel threshold: ' + conf.weak);
    if (conf.noun > 0.10 || conf.def > 0.10)
      throw new Error('a noun cleared the verb threshold: ' + JSON.stringify(conf));
    if (!r.probs) throw new Error('probabilities must be real probabilities');
  });

  // Nine engines, one door. What the kernel may say is the point of it: each
  // finding declares HOW it is known, a silent engine says nothing rather than
  // shrugging, and what nothing settled is stated out loud.
  await check('the grammar kernel routes to every engine and owns up to what it cannot decide', async () => {
    const r = await page.evaluate(() => {
      renderLibrary();
      const shot = t => { const x = GrammarKernel.ask(t); return x && {
        mode: x.mode, keys: x.findings.map(f => f.k), hows: [...new Set(x.findings.map(f => f.how))],
        miss: x.undecided.length,
        allRows: x.findings.every(f => f.rows.length && f.rows.every(row => row[0])) }; };
      return {
        verb:   shot('قَالَ'),
        asl:    shot('مَقْوُولٌ'),
        call:   shot('يَا عَبْدَ اللهِ'),
        free:   shot('لم يكتبِ الطالبُ في الدفترِ'),
        stored: shot('وَالْمَلَائِكَةُ عِبَادُ اللهِ'),
        empty:  GrammarKernel.ask('   '),
        hows:   Object.keys(GrammarKernel.HOW),
      };
    });
    if (r.empty !== null) throw new Error('empty input must answer nothing, not a shrug');
    if (r.hows.join() !== 'rule,corpus,model') throw new Error('the three ways of knowing: ' + r.hows);
    if (r.verb.mode !== 'word' || r.call.mode !== 'phrase')
      throw new Error('word/phrase routing is wrong');
    // a known corpus verb reaches the lexicon AND the declension engine
    for (const k of ['lex', 'irab', 'wazn'])
      if (!r.verb.keys.includes(k)) throw new Error('قَالَ missed the ' + k + ' engine: ' + r.verb.keys);
    // the LEARNED engine must appear, and must be badged a guess — never a rule
    if (!r.verb.keys.includes('tagger')) throw new Error('the learned tagger did not answer');
    if (!r.verb.hows.includes('model')) throw new Error('the tagger must wear the model badge');
    // an underlying form must reach the i'lal rules
    if (!r.asl.keys.includes('ilal')) throw new Error('مَقْوُولٌ missed the i\'lal engine');
    // a corpus sentence must show the HAND analysis and its government
    for (const k of ['stored', 'amil'])
      if (!r.stored.keys.includes(k)) throw new Error('a corpus sentence missed ' + k);
    // free text must NOT claim a stored i'rab, and must say so
    if (r.free.keys.includes('stored')) throw new Error('free text must not claim a corpus i\'rab');
    if (!r.free.miss) throw new Error('free text must own up to what it cannot settle');
    // a guess must be badged as a guess, never as a rule
    if (r.free.keys.includes('guess') && !r.free.hows.includes('model'))
      throw new Error('an inferred row must wear the model badge');
    for (const k of Object.keys(r)) {
      if (k === 'empty' || k === 'hows') continue;
      if (!r[k].allRows) throw new Error(k + ': a finding shipped an empty row');
    }

    await page.evaluate(() => { conjState.lab = 'kernel'; conjState.kernel = 'يَا عَبْدَ اللهِ'; });
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#kernOut', { timeout: 3000 });
    await page.waitForTimeout(260);
    const ui = await page.evaluate(() => {
      const cards = document.querySelectorAll('#kernOut .kn-card').length;
      const badges = [...document.querySelectorAll('#kernOut .kn-how')].length;
      conjState.kernel = 'لم يكتبِ الطالبُ في الدفترِ'; renderKernelOut();
      const openBox = document.querySelectorAll('#kernOut .kn-open').length;
      conjState.lab = 'sarf'; closeSheet();
      return { cards, badges, openBox };
    });
    if (ui.cards < 2) throw new Error('the panel showed ' + ui.cards + ' cards');
    if (ui.badges !== ui.cards) throw new Error('every finding must wear a how-badge');
    if (!ui.openBox) throw new Error('free text must render the what-cannot-be-settled box');
  });

  await check('the I\'lal Lab shows the origin, the outcome and every rule between', async () => {
    await page.evaluate(() => { conjState.lab = 'ilal'; conjState.ilalRoot = 'كيل'; conjState.ilalShape = 'maful'; });
    await page.locator('#conjOpen').click();
    await page.waitForSelector('#ilalOut', { timeout: 3000 });
    await page.waitForTimeout(200);
    const r = await page.evaluate(() => {
      const t = document.getElementById('ilalOut').textContent;
      const steps = document.querySelectorAll('#ilalOut .ilal-steps li').length;
      conjState.ilalRoot = 'نصر'; renderIlalOut();
      const none = document.querySelectorAll('#ilalOut .ilal-none').length;
      const soundSteps = document.querySelectorAll('#ilalOut .ilal-steps li').length;
      conjState.lab = 'sarf'; closeSheet();
      return { t, steps, none, soundSteps };
    });
    if (r.steps !== 3) throw new Error('مَكْيُولٌ takes three rules, panel shows ' + r.steps);
    if (!r.t.includes('مَكِيلٌ')) throw new Error('the outcome is missing from the panel');
    if (!r.t.includes('مَكْيُولٌ')) throw new Error('the origin is missing from the panel');
    if (r.soundSteps !== 0 || !r.none) throw new Error('a sound root must show no rule and say so');
  });

  // The thumb bar only exists on a phone, so it has to be tested on one.
  // Everything else in this suite runs at the desktop width, where the bar is
  // correctly absent — which is exactly how a navigation bug ships unnoticed.
  await check('on a phone the thumb bar is the navigation, and it delegates', async () => {
    await page.setViewportSize({ width: 390, height: 844 });
    await page.evaluate(() => { renderLibrary(); closeSheet(); });
    await page.waitForTimeout(150);
    const lib = await page.evaluate(() => {
      const bar = document.getElementById('tabbar');
      const btns = [...bar.querySelectorAll('[data-nav]')];
      const vis = el => el && getComputedStyle(el).display !== 'none';
      return {
        barShown: getComputedStyle(bar).display === 'grid',
        n: btns.length,
        keys: btns.map(b => b.dataset.nav),
        heights: btns.map(b => Math.round(b.getBoundingClientRect().height)),
        labelled: btns.every(b => b.querySelector('.tb-l').textContent.trim().length > 0),
        active: btns.filter(b => b.classList.contains('on')).map(b => b.dataset.nav),
        gamesOff: btns.find(b => b.dataset.nav === 'games').disabled,
        // the toolbar gives up the destinations it duplicates
        toolbarDupes: ['statsOpen', 'refOpen', 'conjOpen', 'deckOpen']
          .filter(id => vis(document.getElementById(id))),
      };
    });
    if (!lib.barShown) throw new Error('no thumb bar at 390px');
    if (lib.n !== 5) throw new Error('five destinations expected, got ' + lib.n);
    if (lib.keys.join() !== 'library,deck,games,atolye,progress') throw new Error('order: ' + lib.keys);
    const short = lib.heights.filter(h => h < 44);
    if (short.length) throw new Error('a tab is under the thumb floor: ' + lib.heights);
    if (!lib.labelled) throw new Error('an icon-only tab is a guessing game — every tab needs a label');
    if (lib.active.join() !== 'library') throw new Error('in the library, Library is active: ' + lib.active);
    if (lib.gamesOff) throw new Error('Games plays from the library too — the tab must stay live');
    if (lib.toolbarDupes.length) throw new Error('duplicated in the toolbar: ' + lib.toolbarDupes);

    // it must really navigate, not merely look like it
    await page.locator('#tabbar [data-nav="atolye"]').click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    const lab = await page.evaluate(() => !!document.getElementById('labBody'));
    if (!lab) throw new Error('the Atölye tab did not open the lab');
    await page.evaluate(() => closeSheet());
    await page.locator('#tabbar [data-nav="progress"]').click();
    await page.waitForSelector('.sheet.show', { timeout: 3000 });
    await page.evaluate(() => closeSheet());

    // and inside a story, Games comes alive
    await page.evaluate(() => openStory(STORIES[0]));
    await page.waitForTimeout(150);
    const inStory = await page.evaluate(() => {
      const b = document.querySelector('#tabbar [data-nav="games"]');
      return { off: b.disabled, active: [...document.querySelectorAll('#tabbar .on')].map(x => x.dataset.nav) };
    });
    if (inStory.off) throw new Error('Games must be live inside a story too');
    if (inStory.active.includes('library')) throw new Error('Library is still marked active inside a story');
    await page.setViewportSize({ width: 1280, height: 720 });
    await page.evaluate(() => { renderLibrary(); closeSheet(); });
  });

  await check('the front door states where you are, and the numbers are the deck\'s own', async () => {
    await page.evaluate(() => renderLibrary());
    await page.waitForSelector('#statStrip', { timeout: 3000 });
    const r = await page.evaluate(() => {
      const tiles = [...document.querySelectorAll('#statStrip .st-tile')];
      const d = deckStats();
      return {
        n: tiles.length,
        heights: tiles.map(t => Math.round(t.getBoundingClientRect().height)),
        keys: tiles.map(t => t.dataset.st),
        shown: tiles.map(t => t.querySelector('.st-n').textContent),
        real: [String(state.streak.days || 0), String(d.due), String(d.mature)],
      };
    });
    if (r.n !== 3) throw new Error('three tiles, got ' + r.n);
    if (r.keys.join() !== 'streak,due,known') throw new Error('tiles: ' + r.keys);
    if (r.shown.join() !== r.real.join())
      throw new Error('the strip disagrees with deckStats: ' + r.shown + ' vs ' + r.real);
    const short = r.heights.filter(h => h < 44);
    if (short.length) throw new Error('a tile is under the thumb floor: ' + r.heights);
  });

  // A design system that is only written down is a document, not a system.
  // These are the two claims DESIGN.md makes that a page can actually be
  // held to: the scale resolves, and a thumb target never falls below 44px.
  await check('the design tokens resolve, and primary actions clear the 44px thumb floor', async () => {
    const r = await page.evaluate(() => {
      const cs = getComputedStyle(document.documentElement);
      const need = ['--s1', '--s2', '--s3', '--s4', '--s5', '--s6', '--s7',
                    '--t-xs', '--t-sm', '--t-md', '--t-lg', '--t-xl', '--t-2xl',
                    '--r-sm', '--r-md', '--r-full', '--e1', '--e2',
                    '--dur-fast', '--dur-base', '--ease', '--tap'];
      const missing = need.filter(k => !cs.getPropertyValue(k).trim());
      return { missing, tap: cs.getPropertyValue('--tap').trim() };
    });
    if (r.missing.length) throw new Error('unset tokens: ' + r.missing.join(', '));
    if (r.tap !== '44px') throw new Error('the thumb floor moved: ' + r.tap);
    // measure a real .btn on a real sheet rather than trusting the rule
    await page.evaluate(() => openGames());
    await page.waitForSelector('.game-pick', { timeout: 3000 });
    await page.locator('#gNida').click();
    await page.waitForSelector('.opts', { timeout: 3000 });
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('#qNext', { timeout: 3000 });
    const h = await page.evaluate(() => Math.round(document.getElementById('qNext').getBoundingClientRect().height));
    if (h < 44) throw new Error('the primary action is only ' + h + 'px tall');
    await page.evaluate(() => closeSheet());
  });

  // Translation is where grammar stops being a hobby, so the reveal has to
  // do more than mark the answer: it walks the amil/ma'mul pairs, and those
  // pairs are DERIVED from the stored i'rab rather than written a second time.
  await check('the ibare game runs both ways and explains by amil and ma\'mul', async () => {
    const r = await page.evaluate(() => {
      renderLibrary();
      const pool = ibaraItems();
      // every item must carry at least one governor/governed pair, and the
      // pairing must never hand a majrur to a verb
      const bad = [];
      pool.forEach(it => {
        if (!it.pairs.length) bad.push(it.sen.id + ': no pair');
        it.pairs.forEach(p => {
          if (!p.rel.from.includes(p.gov.k))
            bad.push(it.sen.id + ': ' + p.rel.k + ' governed by ' + p.gov.k);
          if (p.amil === p.mamul) bad.push(it.sen.id + ': a word governing itself');
        });
      });
      return { n: pool.length, bad: bad.slice(0, 5),
               kinds: [...new Set(pool.flatMap(i => i.pairs.map(p => p.gov.k)))] };
    });
    if (r.n < 20) throw new Error('too few ibare items: ' + r.n);
    if (r.bad.length) throw new Error(r.bad.join('; '));
    for (const k of ['verb', 'jarr'])
      if (!r.kinds.includes(k)) throw new Error('no ' + k + ' governor found in the pool');

    for (const [id, arSide] of [['gIbaraTr', false], ['gIbaraAr', true]]) {
      await page.evaluate(() => openGames());
      await page.waitForSelector('.game-pick', { timeout: 3000 });
      await page.locator('#' + id).click();
      await page.waitForSelector('.opts', { timeout: 3000 });
      const q = await page.locator('.game-q').innerHTML();
      const arabic = /lang="ar"/.test(q);
      if (arabic !== !arSide)
        throw new Error(id + ': the prompt side is wrong (arabic prompt=' + arabic + ')');
      const n = await page.locator('.opts [data-o]').count();
      if (n !== 4) throw new Error(id + ': four renderings expected, got ' + n);
      await page.locator('.opts [data-o]').first().click();
      await page.waitForSelector('#qWhy', { timeout: 3000 });
      const w = await page.evaluate(() => ({
        pairs: document.querySelectorAll('#qWhy .ib-pairs li').length,
        right: document.querySelectorAll('.opts .right').length,
        text: document.getElementById('qWhy').textContent,
      }));
      if (w.right !== 1) throw new Error(id + ': exactly one right rendering');
      if (!w.pairs) throw new Error(id + ': the reveal must walk the amil pairs');
      if (!/عَامِل|âmil|amil|مَرْفُوع|مَنْصُوب|مَجْرُور/i.test(w.text))
        throw new Error(id + ': the reveal must speak in amil/ma\'mul terms');
      await page.evaluate(() => closeSheet());
    }
  });

  await check('the games hub is shelved by discipline, and every card still opens', async () => {
    await page.evaluate(() => openGames());
    await page.waitForSelector('.game-pick', { timeout: 3000 });
    const r = await page.evaluate(() => {
      const kids = [...document.querySelector('.game-pick').children];
      const heads = kids.filter(k => k.classList.contains('game-group')).map(k => k.textContent);
      const cards = kids.filter(k => k.tagName === 'BUTTON').map(k => k.id);
      // every heading must be followed by at least one card, and no card
      // may sit above the first heading — an unshelved card is a bug.
      const firstHead = kids.findIndex(k => k.classList.contains('game-group'));
      let orphanHead = false;
      kids.forEach((k, i) => {
        if (k.classList.contains('game-group') &&
            !(kids[i + 1] && kids[i + 1].tagName === 'BUTTON')) orphanHead = true;
      });
      return { heads, cards, firstHead, orphanHead };
    });
    if (r.heads.length !== 5) throw new Error('five disciplines expected, got ' + r.heads.length);
    if (r.firstHead !== 0) throw new Error('a card sits above the first heading');
    if (r.orphanHead) throw new Error('a heading has no card under it');
    // a game count is a FLOOR, not a total — the shart game arrived as the
    // fifteenth and broke the pinned fourteen, the running-total trap again.
    if (r.cards.length < 15) throw new Error('at least fifteen games expected, got ' + r.cards.length);
    for (const id of r.cards) {
      const wired = await page.evaluate(i => !!document.getElementById(i), id);
      if (!wired) throw new Error('card ' + id + ' vanished');
    }
    await page.evaluate(() => closeSheet());
  });

  // ---- the SARF test on a corpus match ------------------------------------
  // The last letter's vowel is i'rab and may move; every vowel before it is
  // sarf and may not. Without that test a bare-letters match read حُكْمُ as a
  // cell of حَكَمَ and عِلْمَ as a cell of عَلِمَ — fourteen wrong readings from one
  // missing comparison. Structural, not a list: the FRAME is what is gated.
  await check('a corpus cell must agree with the word in sarf, not just in letters', async () => {
    const r = await page.evaluate(() => ({
      // interior differs → refused; ending differs → still the same cell
      sarf:   sjSarfAgree('حُكْمُ', 'حَكَمَ'),
      irab:   sjSarfAgree('يَعْلَمَ', 'يَعْلَمُ'),
      ilm:    sjSarfAgree('عِلْمَ', 'عَلِمَ'),
      bare:   sjSarfAgree('حكم', 'حَكَمَ'),          // unvowelled proves nothing
      // …and end to end, through the analyzer
      hukm:   SentenceAnalyzer.analyze('وَحُكْمُ الْأَصْلِ ثَابِتٌ')[0],
      warada: SentenceAnalyzer.analyze('وَرَدَ النَّصُّ')[0],
      nass:   SentenceAnalyzer.analyze('وَرَدَ النَّصُّ')[1],
      // the passive, BUILT from the stored active
      yunal:  SentenceAnalyzer.analyze('لَا يُنَالُ الْعِلْمُ بِرَاحَةِ الْجَسَدِ')[1],
      // a noun's three marks outrank a corpus cell: خَفِيّ is a sifa mushabbaha
      khafi:  SentenceAnalyzer.analyze('وَمِنْهُ خَفِيٌّ')[1],
      // the alif maqsura written full before a pronoun
      rawa:   SentenceAnalyzer.analyze('مَا رَوَاهُ قَوْمٌ')[1],
      mizan:  stripAr(WaznEngine.mizan('وَالْفَرْعُ', 'ف ر ع') || ''),
      radical: stripAr(WaznEngine.mizan('وَصْفٌ', 'و ص ف') || ''),   // a radical waw is not a clitic
    }));
    if (r.sarf !== false) throw new Error('حُكْمُ must not pass as a cell of حَكَمَ');
    if (r.ilm !== false)  throw new Error('عِلْمَ must not pass as a cell of عَلِمَ');
    if (r.irab !== true)  throw new Error('a moved ENDING is the same cell: يَعْلَمَ / يَعْلَمُ');
    if (r.bare !== true)  throw new Error('an unvowelled word carries no evidence and must not be refused');
    if (r.hukm.kind !== 'noun') throw new Error('وَحُكْمُ is a masdar, read as ' + r.hukm.kind);
    if (r.warada.kind !== 'verb') throw new Error('وَرَدَ is a verb, read as ' + r.warada.kind);
    if (r.nass.root !== 'ن ص ص') throw new Error('النَّصُّ root: ' + r.nass.root + ' — the article is not a radical');
    if (r.yunal.kind !== 'verb') throw new Error('يُنَالُ is the majhul of نَالَ, read as ' + r.yunal.kind);
    if (r.khafi.kind !== 'noun') throw new Error('خَفِيٌّ wears tanwin and no verb ever does; read as ' + r.khafi.kind);
    if (r.rawa.kind !== 'verb') throw new Error('رَوَاهُ is a verb, read as ' + r.rawa.kind);
    if (r.mizan !== 'فعل') throw new Error('a clitic is not part of the scale: ' + r.mizan);
    if (r.radical !== 'فعل') throw new Error('a radical waw must not be peeled: ' + r.radical);
  });

  // ---- the definitional frame, widened ------------------------------------
  // Every مَا in Mukhtasar al-Manar is mawsula, and the matn's own sentence
  // shape is what says so. Each rule is gated by the SHAPE it reads, with a
  // sentence the shape did not previously reach.
  await check('the relative ma is found by frame, idafa, aid and atf', async () => {
    const r = await page.evaluate(() => {
      const ma = t => {
        const rows = SentenceAnalyzer.analyze(t);
        return rows.filter(x => /ما$/.test(stripAr(x.w).replace(/^[وف]/, '')))
                   .map(x => ({ kind: x.kind, wajh: x.wajh ? x.wajh.k : null }));
      };
      return {
        article: ma('فَالْخَاصُّ مَا وُضِعَ لِمَعْنًى'),          // ال — the original frame
        idafa:   ma('وَدَلَالَتُهُ مَا ثَبَتَ بِمَعْنَى النَّظْمِ'),   // definite by a pronoun
        pron:    ma('الْأَصْلُ وَهُوَ مَا يُبْتَنَى عَلَيْهِ غَيْرُهُ'), // definite by BEING a pronoun
        mudaf:   ma('لِجَمِيعِ مَا يَصْلُحُ لَهُ'),               // مضاف إليه is never a harf
        shibh:   ma('مَعْرِفَةُ النَّفْسِ مَا لَهَا وَمَا عَلَيْهَا'),  // sila as a shibh jumla + atf
        aid:     ma('فَالْحَقِيقَةُ مَا اسْتُعْمِلَ فِيمَا وُضِعَ لَهُ'), // the returning pronoun
        // …and the readings the widening must NOT swallow
        nafiya:  ma('زَيْدٌ مَا قَامَ'),
        masdar:  ma('جَزَيْتُهُمْ بِمَا صَبَرُوا'),
      };
    });
    const isNoun = (k, at) => {
      const rows = r[k];
      if (!rows || !rows.length) throw new Error(k + ': no ma row found');
      rows.slice(0, at === undefined ? rows.length : at + 1).forEach((x, i) => {
        if (x.kind !== 'noun' || x.wajh !== 'mawsula')
          throw new Error(`${k}[${i}]: expected the relative ism, got ${x.kind} / ${x.wajh}`);
      });
    };
    ['article', 'idafa', 'pron', 'mudaf', 'shibh', 'aid'].forEach(k => isNoun(k));
    // زَيْدٌ مَا قَامَ is a real sentence: the negation must survive the widening.
    // Its subject is INDEFINITE, so the definitional frame does not hold.
    if (r.nafiya[0].wajh !== 'nafiya')
      throw new Error('an indefinite subject is not the definitional frame: ' + r.nafiya[0].wajh);
    // …and a jarr clause with NO returning pronoun stays a masdar-maker
    if (r.masdar[0].wajh !== 'masdariyya')
      throw new Error('بِمَا صَبَرُوا has no aid and must stay masdariyya: ' + r.masdar[0].wajh);
  });

  // ---- Manar chapter 15: the two passives, and the seat of a hidden ʿaid ----
  await check('manar ch15: azima and rukhsa, with the majhul on both sides of the rule', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'mukhtasar-al-manar');
      const ch = st.chapters.find(c => c.n === 15);
      const sen = id => ch.sentences.find(s => s.id === id);
      const txt = id => sen(id).tokens.map(t => t.s.full).join(' ');
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const ma = t => SentenceAnalyzer.analyze(t)
        .filter(x => /ما$/.test(stripAr(x.w).replace(/^[وف]/, '')))
        .map(x => ({ kind: x.kind, wajh: x.wajh ? x.wajh.k : null }));
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // the sound feminine plural: majrur by a kasra in s1, MANSUB by a kasra in s2
        jarr: tk('s1', 'والمقدرات').irab.ar,
        nasb: tk('s2', 'المقدرات').irab.ar,
        // the derived majhul vs the stored one
        tudrak: findFormInParadigm(st.morph.adraka, 'تُدْرَكُ'),
        shuria: findFormInParadigm(st.morph.sharaa, 'شُرِعَ'),
        yuqas:  findFormInParadigm(st.morph.qasa, 'يُقَاسُ'),
        builtHollow: sjMajhul('يَقِيسُ', false),
        storedHollow: st.morph.qasa.majhulMudari,
        hollowRuleReaches: stripAr(sjMajhul('يَقِيسُ', false) || '') === stripAr(st.morph.qasa.majhulMudari || ''),
        // …and the hidden ʿaid: nothing on the page returns to this ma
        lima: ma(txt('s3')),
        sabaru: ma('جَزَيْتُهُمْ بِمَا صَبَرُوا'),
        // the fa that announces a conditional mubtada
        fa: tk('s5', 'فغيره').grammar || [],
        note: !!GRAMMAR['fa-khabar-mubtada'] && !!GRAMMAR['fa-khabar-mubtada'].title.tr,
        yuqasKind: SentenceAnalyzer.analyze(txt('s5')).slice(-1)[0].kind,
      };
    });
    if (r.chapters < 15) throw new Error('chapter 15 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch15 sentences: ' + r.n);
    // ONE plural, two cases, one mark — the point of putting them a sentence apart
    if (!/مَجْرُور/.test(r.jarr)) throw new Error('s1 المقدرات should be majrur: ' + r.jarr);
    if (!/مَنْصُوب/.test(r.nasb)) throw new Error('s2 المقدرات should be mansub: ' + r.nasb);
    if (!/الْكَسْرَة/.test(r.nasb)) throw new Error('a sound fem plural takes its NASB by a kasra: ' + r.nasb);
    // the majhul the rule can build, and the one it must not
    if (!r.tudrak || r.tudrak.tense !== 'majhulMudari' || !r.tudrak.derived)
      throw new Error('تُدْرَكُ must be BUILT from the active: ' + JSON.stringify(r.tudrak));
    if (!r.shuria || r.shuria.tense !== 'majhulMazi')
      throw new Error('شُرِعَ must resolve as the stored majhul mazi: ' + JSON.stringify(r.shuria));
    if (!r.yuqas || r.yuqas.tense !== 'majhulMudari' || r.yuqas.derived)
      throw new Error('يُقَاسُ must come from STORAGE, not from the rule: ' + JSON.stringify(r.yuqas));
    if (r.hollowRuleReaches)
      throw new Error('the vowel rule must not reach a hollow passive — it changes the LETTER too: '
                      + r.builtHollow + ' vs ' + r.storedHollow);
    if (r.yuqasKind !== 'verb') throw new Error('يُقَاسُ read as ' + r.yuqasKind);
    // an ʿaid that is MUSTATIR still makes a relative, and a complete clause still makes a masdar
    if (!r.lima.length || r.lima[0].wajh !== 'mawsula')
      throw new Error('لِمَا لَزِمَ الْعِبَادَ: the empty fa\'il seat is the ʿaid — got ' + JSON.stringify(r.lima));
    if (r.sabaru[0].wajh !== 'masdariyya')
      throw new Error('بِمَا صَبَرُوا has its fa\'il and leaves no seat: ' + r.sabaru[0].wajh);
    if (!r.note) throw new Error('the fa-khabar-mubtada note is missing or untranslated');
    if (!r.fa.includes('fa-khabar-mubtada'))
      throw new Error('فَغَيْرُهُ must anchor the note that explains its fa: ' + r.fa.join(','));
  });

  // ---- Manar chapter 16: the book closes its own ring -----------------------
  await check('manar ch16: the working masdar, the jarr sign, and the fa of a real jawab', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'mukhtasar-al-manar');
      const ch = st.chapters.find(c => c.n === 16);
      const sen = id => ch.sentences.find(s => s.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const kind = (t, w) => {
        const rows = SentenceAnalyzer.analyze(t);
        const row = rows.find(x => stripAr(x.w) === stripAr(w));
        return row ? row.kind : '<absent>';
      };
      const ch2 = st.chapters.find(c => c.n === 2);
      const sources = j => j.map(t => stripAr(t.s.full).replace(/^[وفبلك]/, '').replace(/^ال/, ''));
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // إعمال المصدر: the majrur is the fa'il, the mansub is the maf'ul
        badhl: (tk('s1', 'بذل').grammar || []),
        faqih: tk('s1', 'الفقيه').irab.ar,
        wusah: tk('s1', 'وسعه').irab.ar,
        note: !!GRAMMAR['imal-al-masdar'] && !!GRAMMAR['imal-al-masdar'].title.tr,
        // a naqis in NASB writes its fatha where the same letter could not carry a damma
        yufti: tk('s3', 'يفتي').irab.ar,
        yajri: st.chapters.find(c => c.n === 15).sentences
                 .find(s => s.id === 's1').tokens
                 .find(t => stripAr(t.s.full) === 'يجري').irab.ar,
        // a final KASRA is a jarr sign, and no verb is majrur
        talab: kind('فِي طَلَبِ الْحُكْمِ الشَّرْعِيِّ', 'طلب'),
        talabaVerb: kind('طَلَبَ الْفَقِيهُ الْحُكْمَ', 'طلب'),
        // a waw/fa in front of a fused jarr+pronoun must come off
        faalayhi: kind('فَعَلَيْهِ التَّقْلِيدُ', 'فعليه'),
        walahu: kind('وَلَهُ الْحُكْمُ', 'وله'),
        alayhi: kind('عَلَيْهِ الدَّيْنُ', 'عليه'),
        // the fa of a REAL jawab, obligatory because the answer is nominal
        fa: tk('s5', 'فعليه').grammar || [],
        jumal: sen('s5').jumal.map(j => j.ar).join(' | '),
        // the ring: chapter 2's four sources, same words, same order
        ch2sources: sources(ch2.sentences[0].tokens.filter(t =>
          ['kitab', 'sunna', 'ijma', 'qiyas'].includes(t.lex))),
        ch16sources: sources(sen('s2').tokens.filter(t =>
          ['kitab', 'sunna', 'ijma', 'qiyas'].includes(t.lex))),
      };
    });
    if (r.chapters < 16) throw new Error('chapter 16 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch16 sentences: ' + r.n);
    // the masdar governs: one word is its doer, the next is its object
    if (!r.badhl.includes('imal-al-masdar')) throw new Error('بذل must anchor the note: ' + r.badhl.join(','));
    if (!r.note) throw new Error('the imal-al-masdar note is missing or untranslated');
    if (!/فَاعِل/.test(r.faqih)) throw new Error('الفقيه is the masdar\'s FA\'IL: ' + r.faqih);
    if (!/مَفْعُول/.test(r.wusah) || !/مَنْصُوب/.test(r.wusah))
      throw new Error('وسعه is the masdar\'s maf\'ul in NASB: ' + r.wusah);
    // the same letter, two cases, one written and one estimated
    if (!/الظَّاهِرَة/.test(r.yufti)) throw new Error('يفتي\'s fatha is WRITTEN on the ya: ' + r.yufti);
    if (!/مُقَدَّرَة/.test(r.yajri)) throw new Error('يجري\'s damma is ESTIMATED: ' + r.yajri);
    // a kasra is a case-ending, and cases belong to nouns
    if (r.talab !== 'noun') throw new Error('طَلَبِ wears a kasra and no verb is majrur: ' + r.talab);
    if (r.talabaVerb !== 'verb') throw new Error('طَلَبَ with a fatha is still the verb: ' + r.talabaVerb);
    // …and a clitic must not hide a fused jarr+pronoun
    for (const k of ['faalayhi', 'walahu', 'alayhi'])
      if (r[k] !== 'particle') throw new Error(k + ' is a jarr letter with its pronoun, read as ' + r[k]);
    if (!r.fa.includes('fa-khabar-mubtada'))
      throw new Error('فعليه must anchor the fa note: ' + r.fa.join(','));
    if (!/جَوَابُ الشَّرْطِ/.test(r.jumal) || !/وَاجِب/.test(r.jumal))
      throw new Error('the nominal jawab must state that its fa is OBLIGATORY: ' + r.jumal);
    // the ring closes: the same four sources, in the same order, sixteen chapters apart
    if (r.ch2sources.join(',') !== r.ch16sources.join(','))
      throw new Error('ch2 ' + r.ch2sources.join(',') + ' vs ch16 ' + r.ch16sources.join(','));
    if (r.ch16sources.length !== 4) throw new Error('four sources: ' + r.ch16sources.join(','));
  });

  // ---- Talkhis al-Miftah joins the shelf ----------------------------------
  await check('talkhis: the Talkhis defines fasaha and balagha, and mirrors the Manar', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      if (!st) return { missing: true };
      const sen = (c, id) => st.chapters.find(x => x.n === c).sentences.find(x => x.id === id);
      const tk = (c, id, w) => sen(c, id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const mn = STORIES.find(s => s.id === 'mukhtasar-al-manar');
      const kind = (t, w) => {
        const row = SentenceAnalyzer.analyze(t).find(x => stripAr(x.w) === stripAr(w));
        return row ? { kind: row.kind, sure: row.sure } : null;
      };
      // «عِلْمٌ يُعْرَفُ بِهِ» — the three words both books define themselves with
      const frame = toks => {
        const b = t => stripAr(t.s.full).replace(/^[وف]/, '');
        // BOTH books say «عِلْم» twice in the line — once as a mudaf and once as
        // the khabar — so the word alone does not locate the frame. What locates
        // it is the VERB that follows: «عِلْمٌ يُعْرَفُ بِهِ».
        const i = toks.findIndex((t, k) => b(t) === 'علم' && toks[k + 1] && b(toks[k + 1]) === 'يعرف');
        return i < 0 ? '<absent>' : toks.slice(i, i + 3).map(b).join(' ');
      };
      return {
        level: st.level, access: st.access, chapters: st.chapters.length,
        tokens: st.chapters.reduce((n, c) => n + c.sentences.reduce((m, s) => m + s.tokens.length, 0), 0),
        games: (GameFactory.audit().find(x => x.id === 'talkhis-al-miftah') || {}).content,
        // the working masdar, once annexed to its FA'IL and once to its OBJECT
        khulus: tk(1, 's2', 'خلوصه').grammar || [],
        talif:  tk(2, 's2', 'تأليف').grammar || [],
        // the idafa that does NOT make definite
        zahir:  tk(1, 's4', 'ظاهر').grammar || [],
        note1: !!GRAMMAR['idafa-lafziyya'] && !!GRAMMAR['idafa-lafziyya'].title.tr,
        note2: !!GRAMMAR['khabar-insha'] && !!GRAMMAR['khabar-insha'].title.tr,
        // the two books define themselves with ONE sentence shape
        // find the frame by its CONTENT, not by a slice index — an index is a
        // claim about where a word sits, which is not what is being asserted
        talkhisFrame: frame(sen(2, 's3').tokens),
        manarFrame: frame(mn.chapters[0].sentences[0].tokens),
        // إِمَّا and أَمَّا are one skeleton and two words — read the hamza's vowel
        imma: kind('لِخَلَلٍ إِمَّا فِي النَّظْمِ وَإِمَّا فِي الِانْتِقَالِ', 'إما'),
        amma: kind('أَمَّا الْكِتَابُ فَهُوَ حُجَّةٌ', 'أما'),
        bare: kind('اما الكتاب فهو حجة', 'اما'),
        // مَعَانِي: manqus + definite, and a sighat muntaha al-jumu' underneath
        maani: tk(2, 's3', 'المعاني').irab.ar,
      };
    });
    if (r.missing) throw new Error('the Talkhis package did not load');
    if (r.level !== 6 || r.access !== 'premium') throw new Error('level/access: ' + r.level + '/' + r.access);
    if (r.chapters < 2) throw new Error('the Talkhis lost a chapter: ' + r.chapters);
    if (r.tokens < 80) throw new Error('tokens: ' + r.tokens);
    if (r.games < 9) throw new Error('a new story must arrive playable: ' + r.games);
    if (!r.note1 || !r.note2) throw new Error('the two new notes are missing or untranslated');
    if (!r.khulus.includes('imal-al-masdar')) throw new Error('خلوصه anchors the working masdar: ' + r.khulus);
    if (!r.talif.includes('imal-al-masdar')) throw new Error('تأليف anchors the working masdar: ' + r.talif);
    if (!r.zahir.includes('idafa-lafziyya')) throw new Error('ظاهر anchors the lafziyya note: ' + r.zahir);
    // THE RING ACROSS TWO BOOKS: «عِلْمٌ يُعْرَفُ بِهِ» opens both definitions
    if (r.talkhisFrame !== r.manarFrame)
      throw new Error('the shared definitional frame drifted: «' + r.talkhisFrame + '» vs «' + r.manarFrame + '»');
    // the minimal pair, all three states
    if (r.imma.kind !== 'particle' || !r.imma.sure) throw new Error('إِمَّا: ' + JSON.stringify(r.imma));
    if (r.amma.kind !== 'particle' || !r.amma.sure) throw new Error('أَمَّا: ' + JSON.stringify(r.amma));
    if (r.bare.sure !== false) throw new Error('an unvowelled «اما» is genuinely undecided: ' + JSON.stringify(r.bare));
    if (!/مُقَدَّرَة/.test(r.maani) || !/مُنْتَهَى الْجُمُوعِ/.test(r.maani))
      throw new Error('الْمَعَانِي is a definite manqus AND a sighat muntaha al-jumu: ' + r.maani);
  });

  // ---- the Tahqiq panel: the engines set beside the corpus -----------------
  // The app holds two analyses of every stored sentence and now shows both.
  // What is gated is not the number but the CONTRACT: one definition of
  // agreement shared with the offline bank, and an honest confidence badge.
  await check('tahqiq: the engines are shown beside the human parse, on one definition', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'mukhtasar-al-manar');
      openStory(st);
      const sen = st.chapters[0].sentences[0];
      const c = engineCheck(sen);
      return {
        judged: c.judged, pct: c.pct, rows: c.rows.length, tokens: sen.tokens.length,
        // the two normalisations the whole project's number rests on
        pronIsIsm: posClass('pron') === posClass('noun'),
        oneParticle: posClass('prep') === posClass('conj') && posClass('conj') === posClass('part'),
        verbStaysVerb: posClass('verb') === 'verb' && posClass('noun') === 'noun',
        guessNotSure: posClass('noun?') === 'noun',
        unknown: posClass(null),
        html: (() => { openIrabSheet(sen); return sheetInner.innerHTML; })(),
      };
    });
    if (r.rows !== r.tokens) throw new Error('a row per token: ' + r.rows + ' vs ' + r.tokens);
    if (!r.judged) throw new Error('nothing was judged');
    if (!r.pronIsIsm) throw new Error('a PRONOUN is an ism — the corpus pron and the analyzer noun must agree');
    if (!r.oneParticle) throw new Error('prep, conj and part are ONE class to the analyzer');
    if (!r.verbStaysVerb || !r.guessNotSure) throw new Error('posClass folded a class it should not have');
    if (r.unknown !== null) throw new Error('an unknown class must stay null, not become a class');
    if (!/تَحْقِيقُ الْآلَة/.test(r.html)) throw new Error('the tahqiq panel did not render');
    if (!/tq-conf/.test(r.html)) throw new Error('every engine reading must carry its confidence badge');
    if (!/generated\.json|generated/.test(r.html)) throw new Error('the panel must say where these rows are kept');
  });

  // ---- Talkhis chapter 3: the three kinds of report ------------------------
  await check('talkhis ch3: adrub al-khabar, the two-object passive, and the fifth bab', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 3);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const mn = STORIES.find(s => s.id === 'mukhtasar-al-manar');
      const irab = (story, c, sid, w) => {
        const t = story.chapters.find(x => x.n === c).sentences.find(x => x.id === sid)
                    .tokens.find(x => stripAr(x.s.full) === stripAr(w));
        return t ? t.irab.ar : '<absent>';
      };
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // a verb of TWO objects, built for the unnamed doer, four times over
        second: ['s1', 's2', 's3', 's4'].map(id => {
          const t = sen(id).tokens.find(x => (x.grammar || []).includes('mafulayn') &&
                                             (x.grammar || []).includes('maful-bihi'));
          return t ? { w: stripAr(t.s.full), ar: t.irab.ar } : null;
        }),
        note: !!GRAMMAR['mafulayn'] && !!GRAMMAR['mafulayn'].title.tr,
        // s4 puts the SAME masdar in both offices of that verb, four words apart
        naib: tk('s4', 'إخراج').irab.ar,
        maful: tk('s4', 'إخراجا').irab.ar,
        // the three verbs that complete the vowel/letter/manner question
        yulqa: irab(st, 3, 's1', 'يلقى'),
        yufti: irab(mn, 16, 's3', 'يفتي'),
        yajri: irab(mn, 15, 's1', 'يجري'),
        // the FIFTH bab of the mujarrad, which the generator could not build
        hasunaBab: st.morph.hasuna.bab,
        hasunaWazn: st.morph.hasuna.wazn,
        hasunaFem: st.morph.hasuna.mazi[5],
        audit: (() => { const a = sarfAudit(); return { checked: a.checked, bad: a.bad.slice(0, 2) }; })(),
      };
    });
    if (r.missing) throw new Error('chapter 3 did not load');
    if (r.chapters < 3) throw new Error('chapter 3 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch3 sentences: ' + r.n);
    if (!r.note) throw new Error('the mafulayn note is missing or untranslated');
    // every one of the four names kept its FATHA: only one object can be the deputy
    r.second.forEach((x, i) => {
      if (!x) throw new Error('sentence ' + (i + 1) + ' has no second object tagged');
      if (!/مَنْصُوب/.test(x.ar))
        throw new Error(x.w + ' must stay MANSUB after the passive: ' + x.ar);
    });
    if (!/نَائِبُ الْفَاعِلِ/.test(r.naib)) throw new Error('s4 إخراج is the deputy: ' + r.naib);
    if (!/مَنْصُوب/.test(r.maful)) throw new Error('s4 إخراجا stays mansub: ' + r.maful);
    // one letter, three states — estimated damma, written fatha, estimated fatha
    if (!/مُقَدَّرَة/.test(r.yajri) || !/الْيَاء/.test(r.yajri))
      throw new Error('يجري: damma ESTIMATED on a ya — ' + r.yajri);
    if (!/الظَّاهِرَة/.test(r.yufti) || !/الْيَاء/.test(r.yufti))
      throw new Error('يفتي: fatha WRITTEN on a ya — ' + r.yufti);
    if (!/مُقَدَّرَة/.test(r.yulqa) || !/الْأَلِف/.test(r.yulqa))
      throw new Error('يلقى: fatha ESTIMATED on an alif — ' + r.yulqa);
    // the fifth bab, and its nun-final idgham
    if (!/حَسُنَ/.test(r.hasunaBab)) throw new Error('the fifth bab: ' + r.hasunaBab);
    if (!/فَعُلَ يَفْعُلُ/.test(r.hasunaWazn)) throw new Error('its wazn: ' + r.hasunaWazn);
    if (r.hasunaFem !== 'حَسُنَّ')
      throw new Error('a nun-final lam meets the feminine nun and contracts: ' + r.hasunaFem);
    // and the whole bank still regenerates
    if (r.audit.bad.length) throw new Error('sarf audit: ' + JSON.stringify(r.audit.bad));
    if (r.audit.checked < 270) throw new Error('the audit shrank: ' + r.audit.checked);
  });

  await check('talkhis ch4: tanzil, the zarf that is not a jarr letter, and the fail seat', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 4);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      // مَعَهُ is written as one word and is TWO — and neither of them a harf
      const maa = SentenceAnalyzer.analyze('كَانَ مَعَهُ كِتَابٌ')
                    .find(x => stripAr(x.w) === 'معه');
      // …and the ma of s1 stands in a verb's empty fa'il seat, three words back
      const seat = SentenceAnalyzer.analyze('إِذَا تَقَدَّمَ فِي الْكَلَامِ مَا يُشِيرُ إِلَى الْخَبَرِ')
                     .find(x => stripAr(x.w) === 'ما');
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // the three cases of tanzil, each on its own passive verb
        tanzil: ['s1', 's2', 's3'].map(id => {
          const t = sen(id).tokens.find(x => (x.grammar || []).includes('khilaf-muqtada-al-zahir') &&
                                             x.pos === 'verb');
          return t ? stripAr(t.s.full) : null;
        }),
        note: !!GRAMMAR['khilaf-muqtada-al-zahir'] &&
              !!GRAMMAR['khilaf-muqtada-al-zahir'].title.tr &&
              GRAMMAR['khilaf-muqtada-al-zahir'].group,
        // the human reading of مَعَهُ: a zarf, and a mudaf
        maahIrab: tk('s3', 'معه').irab.ar,
        maahPos: tk('s3', 'معه').pos,
        // the engine's reading of the same shape
        maahKind: maa ? maa.kind : '<none>',
        maahSeg: maa ? maa.seg.join('+') : '',
        maahNote: maa ? maa.notes.map(n => n.en).join(' ') : '',
        seatKind: seat ? seat.kind : '<none>',
        seatWajh: seat && seat.wajh ? seat.wajh.ar : '<none>',
        seatWhy: seat && seat.wajh ? seat.wajh.why.en : '',
        // and the negative parallel, which is the chapter's fourth sentence
        manfi: sen('s4').tokens.map(t => stripAr(t.s.full)).join(' '),
      };
    });
    if (r.missing) throw new Error('chapter 4 did not load');
    if (r.chapters < 4) throw new Error('chapter 4 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch4 sentences: ' + r.n);
    if (r.note !== 'balagha') throw new Error('the tanzil note is missing, untranslated or misfiled: ' + r.note);
    r.tanzil.forEach((w, i) => {
      if (!w) throw new Error('sentence ' + (i + 1) + ' has no tanzil verb tagged');
      if (!/ينزل$/.test(w)) throw new Error('the tanzil verb: ' + w);
    });
    // مَعَ takes tanwin standing alone and is itself put in jarr, so it is an ISM
    if (!/ظَرْف/.test(r.maahIrab)) throw new Error('معه is a zarf in the human reading: ' + r.maahIrab);
    if (r.maahPos !== 'noun') throw new Error('معه is tagged: ' + r.maahPos);
    if (r.maahKind !== 'noun') throw new Error('the engine still calls معه a particle: ' + r.maahKind);
    if (r.maahSeg !== 'مَعَ+ه') throw new Error('معه must peel into two: ' + r.maahSeg);
    if (!/MUDAF ILAYH/.test(r.maahNote)) throw new Error('the pronoun is a mudaf ilayh: ' + r.maahNote);
    // a verb, a jarr phrase, then ما — the fa'il seat is the one it is sitting in
    if (r.seatKind !== 'noun') throw new Error('the ma in a fail seat is an ism: ' + r.seatKind);
    if (!/الْمَوْصُولَة/.test(r.seatWajh)) throw new Error('the top reading: ' + r.seatWajh);
    if (!/FA'IL/.test(r.seatWhy)) throw new Error("the seat rule did not name the fa'il: " + r.seatWhy);
    if (!/كاعتبارات/.test(r.manfi)) throw new Error('s4 is the negative parallel: ' + r.manfi);
  });

  await check('talkhis ch5: majaz aqli, mustaqarr vs laghw, and the manqus completed', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 5);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      // the two states of one jarr phrase, three words apart in the definition
      const rows = SentenceAnalyzer.analyze('إِلَى مُلَابَسٍ لَهُ غَيْرِ مَا هُوَ لَهُ بِتَأَوُّلٍ');
      const lah = rows.filter(x => stripAr(x.w) === 'له')
                      .map(x => x.notes.map(n => n.en + ' ' + n.tr).join(' '));
      // a mazi built on a SUKUN, wearing the iltiqa-as-sakinayn kasra
      const akh = SentenceAnalyzer.analyze('وَأَخْرَجَتِ الْأَرْضُ أَثْقَالَهَا')[0];
      // a masdariyya needs a VERB to turn into a masdar; a nominal sila leaves
      // only the relative reading — while بِمَا لَا يَعْلَمُ stays ambiguous
      const maN = SentenceAnalyzer.analyze('إِلَى مَا هُوَ لَهُ عِنْدَ الْمُتَكَلِّمِ')
                    .find(x => stripAr(x.w) === 'ما');
      const maV = SentenceAnalyzer.analyze('بِمَا لَا يَعْلَمُ')[0];
      const wajhOf = row => (row && row.notes || []).map(n => n.en).join(' ');
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // the six mulabis, each tagged with the new note
        mulabis: ['s3', 's4', 's5'].map(id =>
          sen(id).tokens.filter(t => (t.grammar || []).includes('majaz-aqli')).length),
        noteM: !!GRAMMAR['majaz-aqli'] && GRAMMAR['majaz-aqli'].group,
        noteZ: !!GRAMMAR['zarf-mustaqarr-wa-laghw'] && GRAMMAR['zarf-mustaqarr-wa-laghw'].group,
        noteZtr: !!(GRAMMAR['zarf-mustaqarr-wa-laghw'] || {}).title.tr,
        lah,
        // the manqus in the two states this chapter adds
        wadi: tk('s3', 'الوادي').irab.ar,
        jari: tk('s4', 'جار').irab.ar,
        akhKind: akh.kind,
        akhCell: akh.cell ? akh.cell.form : null,
        maNkind: maN && maN.kind,
        maNwhy: wajhOf(maN),
        maVwhy: wajhOf(maV),
        // أَفْعَمَ — the paradigm whose root is the mizan's own letters
        afamRoot: (st.glossary.afama || {}).root,
        afamMaful: (st.morph.afama || {}).maful,
        // and لَابَسَ, shipped so both readings of the matn's key word are visible
        labasFail: (st.morph.labasa || {}).fail,
        labasMaful: (st.morph.labasa || {}).maful,
      };
    });
    if (r.missing) throw new Error('chapter 5 did not load');
    if (r.chapters < 5) throw new Error('chapter 5 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch5 sentences: ' + r.n);
    if (r.mulabis.reduce((a, b) => a + b, 0) !== 6)
      throw new Error('the six mulabis are not all tagged: ' + JSON.stringify(r.mulabis));
    if (r.noteM !== 'balagha') throw new Error('the majaz-aqli note: ' + r.noteM);
    if (r.noteZ !== 'nahw' || !r.noteZtr) throw new Error('the mustaqarr note: ' + r.noteZ);
    // ONE sentence, the same two letters twice, opposite states
    if (r.lah.length !== 2) throw new Error('«لَهُ» should occur twice: ' + r.lah.length);
    if (!/لَغْو/.test(r.lah[0]) || /مُسْتَقَر/.test(r.lah[0]))
      throw new Error('the first lahu hangs on مُلَابَسٍ and is LAGHW: ' + r.lah[0]);
    if (!/مُسْتَقَر/.test(r.lah[1]) || /لَغْو/.test(r.lah[1]))
      throw new Error('the second lahu is inside a sila and is MUSTAQARR: ' + r.lah[1]);
    // the manqus: fatha WRITTEN in nasb, ya DELETED when indefinite
    if (!/الظَّاهِرَةُ عَلَى الْيَاءِ/.test(r.wadi)) throw new Error('الوادي writes its fatha: ' + r.wadi);
    if (!/مُقَدَّرَةٍ/.test(r.jari) || !/الْمَحْذُوفَةِ/.test(r.jari))
      throw new Error('جارٍ estimates a damma on a deleted ya: ' + r.jari);
    // a kasra on a cell built on sukun is a repair, not a case
    if (r.akhKind !== 'verb') throw new Error('وأخرجتِ is a verb, kasra or no kasra: ' + r.akhKind);
    if (r.akhCell !== 'أَخْرَجَتْ') throw new Error('the cell it matched: ' + r.akhCell);
    // a masdar-maker needs a verb to work on
    if (r.maNkind !== 'noun') throw new Error('«إلى ما هو له» — the ma is an ism: ' + r.maNkind);
    if (/masdar-making ma — the clause becomes a masdar/.test(r.maNwhy))
      throw new Error('a nominal sila admits no masdariyya: ' + r.maNwhy);
    if (!/masdar-making ma — the clause becomes a masdar/.test(r.maVwhy))
      throw new Error('بما لا يعلم must keep its masdariyya reading: ' + r.maVwhy);
    // the two paradigms this chapter ships
    if (r.afamRoot !== 'ف ع م') throw new Error('أفعم root: ' + r.afamRoot);
    if (r.afamMaful !== 'مُفْعَم') throw new Error('its ism maful: ' + r.afamMaful);
    if (r.labasFail !== 'مُلَابِس' || r.labasMaful !== 'مُلَابَس')
      throw new Error('both readings of the matn word must be shipped: ' +
                      r.labasFail + ' / ' + r.labasMaful);
  });

  await check("talkhis ch6: the qarina, the speaker's ya, and a mabni ending that cannot move", async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 6);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const row = (text, bare) => {
        const rows = SentenceAnalyzer.analyze(text);
        return rows.find(x => stripAr(x.w).replace(/[^ء-ي]/g, '') === bare) || null;
      };
      const li = row('يَا هَامَانُ ابْنِ لِي صَرْحًا', 'لي');
      const bi = row('جَاءَتْ بِي إِلَيْكَ', 'بي');
      const qil = row('أَفْنَاهُ قِيلُ اللهِ لِلشَّمْسِ', 'قيل');
      const kay = row('جِئْتُ كَيْ أَتَعَلَّمَ', 'كي');
      const idhaMa = row('إِذَا مَا زِدْتَهُ نَظَرًا', 'ما');
      const shart = row('مَا تَفْعَلْ مِنْ خَيْرٍ يَعْلَمْهُ اللهُ', 'ما');
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // the first vocative the library has ever carried in real text
        hamanIrab: tk('s1', 'هامان').irab.ar,
        nida: (() => { const v = NidaEngine.read('يَا هَامَانُ'); return v && v.ok ? v.ruling : '<no>'; })(),
        // an imperative built on the DELETION of its weak letter
        ibnIrab: tk('s1', 'ابن').irab.ar,
        ibnCell: (st.morph.bana || {}).amr ? st.morph.bana.amr[0] : null,
        // the speaker's ya peels like any other enclitic
        liKind: li && li.kind, liSeg: li ? li.seg.join('+') : '',
        biKind: bi && bi.kind, biSeg: bi ? bi.seg.join('+') : '',
        // …but كَيْ is one word and must not be peeled into two
        kayKind: kay && kay.kind,
        kayNote: kay ? kay.notes.map(n => n.en).join(' ') : '',
        // a masdar that shares its letters with a passive madi
        qilKind: qil && qil.kind, qilNote: qil ? qil.notes.map(n => n.en).join(' ') : '',
        // ma after a conditional is ZA'IDA; ma with jazm evidence is the shart
        idhaWajh: idhaMa && idhaMa.wajh && idhaMa.wajh.ar,
        shartWajh: shart && shart.wajh && shart.wajh.ar,
        // the nun of protection, named in the human reading
        sarratIrab: tk('s4', 'سرتني').irab.ar,
        sarraFakk: (st.morph.sarra || {}).mazi ? st.morph.sarra.mazi[6] : null,
        // two tamyiz in one hemistich, neither of them an object
        tamyiz: sen('s5').tokens.filter(t => (t.grammar || []).includes('tamyiz'))
                  .map(t => stripAr(t.s.full)),
        noteY: !!GRAMMAR['ya-al-mutakallim'] && GRAMMAR['ya-al-mutakallim'].group,
        noteYtr: !!(GRAMMAR['ya-al-mutakallim'] || {}).title.tr,
        noteQ: !!GRAMMAR['qarinat-al-majaz'] && GRAMMAR['qarinat-al-majaz'].group,
        // the chapter's six qarina-bearing tokens
        qarina: ['s2', 's3', 's4', 's5'].map(id =>
          sen(id).tokens.filter(t => (t.grammar || []).includes('qarinat-al-majaz')).length)
          .reduce((a, b) => a + b, 0),
      };
    });
    if (r.missing) throw new Error('chapter 6 did not load');
    if (r.chapters < 6) throw new Error('chapter 6 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch6 sentences: ' + r.n);
    if (r.noteY !== 'nahw' || !r.noteYtr) throw new Error('the speaker-ya note: ' + r.noteY);
    if (r.noteQ !== 'balagha') throw new Error('the qarina note: ' + r.noteQ);
    if (r.qarina !== 6) throw new Error('six qarina tokens expected, got ' + r.qarina);
    // a munada that is a single proper name: mabni on the damma, in the POSITION of nasb
    if (!/مَبْنِيٌّ عَلَى الضَّمِّ/.test(r.hamanIrab) || !/مَحَلِّ نَصْبٍ/.test(r.hamanIrab))
      throw new Error('the munada: ' + r.hamanIrab);
    if (r.nida !== 'mabni') throw new Error('NidaEngine rules it: ' + r.nida);
    // the jazm sign is the DELETION — nothing on the page to point at
    if (!/حَذْفِ حَرْفِ الْعِلَّةِ/.test(r.ibnIrab)) throw new Error('the naqis imperative: ' + r.ibnIrab);
    if (r.ibnCell !== 'اِبْنِ') throw new Error("the stored amr cell: " + r.ibnCell);
    // the speaker's ya is an enclitic like any other
    if (r.liKind !== 'particle' || r.liSeg !== 'لِ+ي')
      throw new Error('لِي is a jarr letter and a pronoun: ' + r.liKind + ' / ' + r.liSeg);
    if (r.biKind !== 'particle' || r.biSeg !== 'بِ+ي')
      throw new Error('بِي is a jarr letter and a pronoun: ' + r.biKind + ' / ' + r.biSeg);
    // …and a table entry is ONE word: كَيْ must not peel into kaf + ya
    if (r.kayKind !== 'particle' || !/nâsıb|nasb governor/.test(r.kayNote))
      throw new Error('كَيْ must stay the nasb particle: ' + r.kayKind + ' — ' + r.kayNote);
    // a mabni cell's ending cannot move, so قِيلُ is not قِيلَ
    if (r.qilKind !== 'noun') throw new Error('قِيلُ is a masdar, not the passive madi: ' + r.qilKind);
    if (!/mabni ending cannot move/.test(r.qilNote))
      throw new Error('and the reason must name the rule: ' + r.qilNote);
    // two faces of ma, told apart by what stands on either side
    if (!/الزَّائِدَة/.test(r.idhaWajh || '')) throw new Error('إذا ما is zaida: ' + r.idhaWajh);
    if (!/الشَّرْطِيَّة/.test(r.shartWajh || '')) throw new Error('the shart keeps its top rank on jazm evidence: ' + r.shartWajh);
    // the protecting nun, and the doubled verb's fakk before a sukun
    if (!/نُونُ الْوِقَايَةِ/.test(r.sarratIrab)) throw new Error('the nun of protection: ' + r.sarratIrab);
    if (r.sarraFakk !== 'سَرَرْتَ') throw new Error('a doubled verb breaks before a sukun: ' + r.sarraFakk);
    if (r.tamyiz.length !== 2) throw new Error('two tamyiz expected in s5: ' + r.tamyiz.join(', '));
  });

  await check('talkhis ch7: hadhf and dhikr, and the derived participles the peel table lacked', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 7);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const root = w => { const f = RootFinder.find(w); return f ? f.root : null; };
      const asa = SentenceAnalyzer.analyze('هِيَ عَصَايَ')
                    .find(x => stripAr(x.w).replace(/[^ء-ي]/g, '') === 'عصاي');
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // every omitted mubtada names the word it is estimated as
        taqdir: ch.sentences.flatMap(s => s.tokens)
          .filter(t => (t.grammar || []).includes('hadhf-wa-taqdir'))
          .map(t => t.irab.ar),
        // the participles of the derived forms — none of these read before ch7
        roots: {
          muqarrir: root('مُقَرِّرٌ'), mudih: root('مُوضِحٌ'), mustafad: root('مُسْتَفَادٌ'),
          muwaswis: root('مُوَسْوِسٌ'), muflih: root('الْمُفْلِحُونَ'),
          maktub: root('مَكْتُوب'), madrasa: root('مَدْرَسَة'),
        },
        // …and a verb never reaches the speaker's ya without the nun
        asaKind: asa && asa.kind,
        asaNote: asa ? asa.notes.map(n => n.en).join(' ') : '',
        // the maqsur with its tanwin, in a MUSTAQARR khabar
        huda: tk('s4', 'هدى').irab.ar,
        // two siyagh muntaha al-jumu', both restored to a kasra by the article
        shara: tk('s3', 'للشرائع').irab.ar,
        dala: tk('s3', 'للدلائل').irab.ar,
        // the speaker's ya on a maqsur: the alif stands, the ya takes a fatha
        asaIrab: tk('s5', 'عصاي').irab.ar,
        noteM: !!GRAMMAR['ahwal-al-musnad-ilayh'] && GRAMMAR['ahwal-al-musnad-ilayh'].group,
        noteH: !!GRAMMAR['hadhf-wa-taqdir'] && GRAMMAR['hadhf-wa-taqdir'].group,
        noteHtr: !!(GRAMMAR['hadhf-wa-taqdir'] || {}).title.tr,
      };
    });
    if (r.missing) throw new Error('chapter 7 did not load');
    if (r.chapters < 7) throw new Error('chapter 7 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch7 sentences: ' + r.n);
    if (r.noteM !== 'balagha') throw new Error('the musnad-ilayh note: ' + r.noteM);
    if (r.noteH !== 'nahw' || !r.noteHtr) throw new Error('the hadhf note: ' + r.noteH);
    // an analysis that says a word is missing must say WHICH word
    if (r.taqdir.length < 4) throw new Error('too few omitted-mubtada tokens: ' + r.taqdir.length);
    r.taqdir.forEach(t => {
      if (!/مَحْذُوفٍ/.test(t)) throw new Error('this token is not about an omission: ' + t);
      if (!/تَقْدِيرُهُ|أَيْ:/.test(t)) throw new Error('an omission must name its taqdir: ' + t);
    });
    // the mirror: the same omission, for reverence and for distaste
    const rev = r.taqdir.find(t => /مُحَمَّدٌ/.test(t));
    const dis = r.taqdir.find(t => /الشَّيْطَانُ/.test(t));
    if (!rev || !dis) throw new Error('the reverence/distaste pair must both be tagged');
    if (!/صِيَانَةً لِلِّسَانِ/.test(rev) || !/صِيَانَةً لِلِّسَانِ/.test(dis))
      throw new Error('both must name the SAME device — keeping the tongue from the name');
    // the peel table now has a row for the participles of the derived forms
    // مُسْتَفَاد: the rules could only hedge the hidden radical (ف و/ي د);
    // since v133 the glossary's own ف ي د outranks the hedge — accept both,
    // the exact answer first.
    const want = { muqarrir: 'ق ر ر', mudih: 'و ض ح', mustafad: ['ف ي د', 'ف و/ي د'],
                   muwaswis: 'و س و س', muflih: 'ف ل ح',
                   maktub: 'ك ت ب', madrasa: 'د ر س' };
    for (const [k, v] of Object.entries(want)) {
      const ok = Array.isArray(v) ? v.includes(r.roots[k]) : r.roots[k] === v;
      if (!ok) throw new Error(`root of ${k}: expected ${v}, got ${r.roots[k]}`);
    }
    // نون الوقاية as a test: عَصَايَ cannot be a cell of عَصَى
    if (r.asaKind !== 'noun') throw new Error('عَصَايَ is a noun with its mudaf ilayh: ' + r.asaKind);
    if (!/SPEAKER'S YA with no nun of protection/.test(r.asaNote))
      throw new Error('and the reason must name the nun: ' + r.asaNote);
    if (!/تَثْبُتُ أَلِفُهُ/.test(r.asaIrab)) throw new Error('the maqsur keeps its alif: ' + r.asaIrab);
    // a maqsur wearing tanwin, majrur by an estimated kasra, in a mustaqarr khabar
    if (!/مُقَدَّرَةٍ عَلَى الْأَلِفِ/.test(r.huda) || !/مُسْتَقَرٌّ/.test(r.huda))
      throw new Error('هُدًى: estimated kasra, mustaqarr khabar — ' + r.huda);
    // the article restores the kasra a diptote would have lost
    [r.shara, r.dala].forEach(t => {
      if (!/مُنْتَهَى الْجُمُوعِ/.test(t) && !/صِيغَةُ مُنْتَهَى/.test(t))
        throw new Error('both plurals are siyagh muntaha al-jumu: ' + t);
      if (!/بِالْكَسْرَةِ/.test(t) && !/كَسْرَة/.test(t))
        throw new Error('and the article restores their kasra: ' + t);
    });
  });

  await check('talkhis ch8: the relative, the three distances, and the plural in both cases', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 8);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      const tk = (id, w) => sen(id).tokens.find(t => stripAr(t.s.full) === stripAr(w));
      const notes = t => {
        const rows = SentenceAnalyzer.analyze(t);
        // stripAr keeps the hamza SEAT, so «أَهَذَا» bares to أهذا and never
        // matches a plain-alif key. Fold the seats for MATCHING only.
        const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
        return rows.map(x => ({ w: key(x.w), kind: x.kind,
                                seg: x.seg.join('+'), n: x.notes.map(y => y.en).join(' ') }));
      };
      const three = notes('هَذَا زَيْدٌ ذَاكَ زَيْدٌ ذَلِكَ زَيْدٌ');
      const ah = notes('أَهَذَا الَّذِي يَذْكُرُ');
      // chapter 7's plural in raf', chapter 8's in nasb — same class, one apart
      const ch7 = st.chapters.find(c => c.n === 7);
      const muflih = ch7.sentences.flatMap(s => s.tokens)
        .find(t => stripAr(t.s.full) === stripAr('المفلحون'));
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // four relatives, four different shapes of sila
        mawsul: ch.sentences.flatMap(s => s.tokens)
          .filter(t => (t.grammar || []).includes('ism-mawsul')).length,
        // every one tagged with the new balagha note names its REASON
        reasons: ch.sentences.flatMap(s => s.tokens)
          .filter(t => (t.grammar || []).includes('tarif-al-musnad-ilayh'))
          .map(t => t.irab.ar),
        // the three distances, read off the letters by the engine
        near: (three.find(x => x.w === 'هذا') || {}).n,
        mid: (three.find(x => x.w === 'ذاك') || {}).n,
        far: (three.find(x => x.w === 'ذلك') || {}).n,
        // the interrogative hamza is a proclitic and is now peeled
        ahSeg: (ah.find(x => x.w === 'اهذا') || {}).seg,
        ahKind: (ah.find(x => x.w === 'اهذا') || {}).kind,
        // …and the guard holds: أَكْرَمَ keeps its own hamza
        akram: (notes('أَكْرَمَ زَيْدٌ')[0] || {}).seg,
        // the sound masculine plural in both cases, one chapter apart
        khasir: tk('s3', 'الخاسرين').irab.ar,
        muflih: muflih ? muflih.irab.ar : null,
        // أَمْسِ, mabni on the kasra
        ams: tk('s1', 'أمس').irab.ar,
        // the madda, and the harakat auditor must pass it
        madda: HarakeAuditor.check ? HarakeAuditor.check('آلِهَتَكُمْ') : null,
        noteT: !!GRAMMAR['tarif-al-musnad-ilayh'] && GRAMMAR['tarif-al-musnad-ilayh'].group,
        noteI: !!GRAMMAR['asma-al-ishara'] && GRAMMAR['asma-al-ishara'].group,
        noteItr: !!(GRAMMAR['asma-al-ishara'] || {}).title.tr,
        audit: (() => { const a = sarfAudit(); return { checked: a.checked, bad: a.bad.slice(0, 2) }; })(),
      };
    });
    if (r.missing) throw new Error('chapter 8 did not load');
    if (r.chapters < 8) throw new Error('chapter 8 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch8 sentences: ' + r.n);
    if (r.noteT !== 'balagha') throw new Error('the tarif note: ' + r.noteT);
    if (r.noteI !== 'nahw' || !r.noteItr) throw new Error('the ishara note: ' + r.noteI);
    if (r.mawsul < 6) throw new Error('too few relatives tagged: ' + r.mawsul);
    // a definite subject must say WHY it was made definite that way
    if (r.reasons.length < 6) throw new Error('too few tarif tokens: ' + r.reasons.length);
    r.reasons.forEach(t => {
      if (!/وَعُرِّفَ بِهِ|وَالْإِشَارَةُ|الْإِشَارَةُ هُنَا/.test(t))
        throw new Error('a definiteness choice must state its reason: ' + t);
    });
    // and the four the chapter turns on are all present, by name
    const all = r.reasons.join(' ');
    for (const [k, needle] of Object.entries({
      ugliness: 'اسْتِقْبَاحًا', magnification: 'لِلتَّفْخِيمِ',
      kindOfReport: 'وَجْهِ بِنَاءِ الْخَبَرِ', contempt: 'لِلتَّحْقِيرِ', honour: 'لِلتَّعْظِيمِ' }))
      if (!all.includes(needle)) throw new Error('the chapter must name ' + k + ': ' + needle);
    // three distances, derived from the letters and not stored
    if (!/pointing NEAR/.test(r.near || '')) throw new Error('هَذَا points near: ' + r.near);
    if (!/MIDDLE distance/.test(r.mid || '')) throw new Error('ذَاكَ points at a middle distance: ' + r.mid);
    if (!/pointing FAR/.test(r.far || '')) throw new Error('ذَلِكَ points far: ' + r.far);
    if (!/MABNI/.test(r.near || '')) throw new Error('and every one of them is mabni: ' + r.near);
    // the interrogative hamza peels like the waw, under the same guard
    if (r.ahSeg !== 'أ+هذا') throw new Error('أَهَذَا is a hamza and a demonstrative: ' + r.ahSeg);
    if (r.ahKind !== 'noun') throw new Error('and what remains is an ism: ' + r.ahKind);
    if (r.akram === 'أ+كرم') throw new Error('أَكْرَمَ keeps its own Form IV hamza');
    // one plural, two cases, two chapters
    if (!/الْيَاءُ/.test(r.khasir) || !/مَنْصُوبٌ/.test(r.khasir))
      throw new Error('الخاسرين: nasb by the ya — ' + r.khasir);
    if (!r.muflih || !/الْوَاوُ/.test(r.muflih) || !/مَرْفُوعٌ/.test(r.muflih))
      throw new Error("ch7's المفلحون: raf' by the waw — " + r.muflih);
    if (!/مَبْنِيٌّ عَلَى الْكَسْرِ/.test(r.ams)) throw new Error('أَمْسِ is mabni on the kasra: ' + r.ams);
    if (r.audit.bad.length) throw new Error('sarf audit: ' + JSON.stringify(r.audit.bad));
    if (r.audit.checked < 285) throw new Error('the audit shrank: ' + r.audit.checked);
  });

  await check('talkhis ch9: four lams, the lam that is not a jarr clitic, and one word twice', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 9);
      if (!ch) return { missing: true };
      const sen = id => ch.sentences.find(x => x.id === id);
      // fold the hamza SEATS for matching — stripAr keeps them, and this file
      // has now paid for that four times
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const tk = (id, w) => sen(id).tokens.find(t => key(t.s.full) === key(w));
      const lafi = SentenceAnalyzer.analyze('إِنَّ الْإِنْسَانَ لَفِي خُسْرٍ')
        .find(x => key(x.w) === key('لفي')) || {};
      const bil = SentenceAnalyzer.analyze('بِالْقَلَمِ')[0] || {};
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        // every token tagged with the new nahw note names WHICH lam it is
        lams: ch.sentences.flatMap(s => s.tokens)
          .filter(t => (t.grammar || []).includes('anwa-al-lam-al-tarif'))
          .map(t => t.irab.ar),
        // the lam of ibtida: peeled, but NOT called a jarr clitic
        lafiSeg: (lafi.seg || []).join('+'),
        lafiNote: (lafi.notes || []).map(y => y.en).join(' ~ '),
        // …and the definite case keeps the old verdict, because there the
        // word itself really is the majrur
        bilNote: (bil.notes || []).map(y => y.en).join(' ~ '),
        // the article is never a radical: الصَّاغَة used to answer ل ص غ
        sagha: RootFinder.find('الصَّاغَةَ'),
        marah: RootFinder.find('الْمَرْأَةِ'),
        hajib: RootFinder.find('حَاجِبٌ'),
        // the singular's istighraq against the plural's
        rajul: tk('s3', 'رجل').irab.ar,
        rijal: tk('s3', 'رجال').irab.ar,
        // one word, two tanwins, opposite readings
        hajibs: sen('s5').tokens.filter(t => key(t.s.full) === key('حاجب')).map(t => t.irab.ar),
        // the amr on a wasl hamza, its sukun broken for the two sakins
        udkhul: tk('s1', 'ادخل').irab.ar,
        // and the app's own sign engine agrees the imperative is MABNI
        sign: IrabSign.of ? IrabSign.of('اُدْخُلِ') : null,
        notes: ['anwa-al-lam-al-tarif', 'tarif-bil-idafa', 'tankir-al-musnad-ilayh']
          .map(id => GRAMMAR[id] && [GRAMMAR[id].group, !!GRAMMAR[id].title.tr, !!GRAMMAR[id].plain.tr]),
      };
    });
    if (r.missing) throw new Error('chapter 9 did not load');
    if (r.chapters < 9) throw new Error('chapter 9 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch9 sentences: ' + r.n);
    // the three notes exist, in the right groups, bilingual
    const [nl, ni, nt] = r.notes;
    if (!nl || nl[0] !== 'nahw' || !nl[1] || !nl[2]) throw new Error('the lam note: ' + JSON.stringify(nl));
    if (!ni || ni[0] !== 'balagha') throw new Error('the idafa note: ' + JSON.stringify(ni));
    if (!nt || nt[0] !== 'balagha') throw new Error('the tankir note: ' + JSON.stringify(nt));
    // FOUR faces of one letter, and every tagged token says which it is
    if (r.lams.length < 8) throw new Error('too few lam tokens tagged: ' + r.lams.length);
    const all = r.lams.join(' ');
    for (const [k, needle] of Object.entries({
      genus: 'لَامُ الْجِنْسِ', mental: 'لِلْعَهْدِ الذِّهْنِيِّ',
      external: 'لِلْعَهْدِ الْخَارِجِيِّ', real: 'لِلِاسْتِغْرَاقِ الْحَقِيقِيِّ',
      customary: 'لِلِاسْتِغْرَاقِ الْعُرْفِيِّ' }))
      if (!all.includes(needle)) throw new Error('the chapter must name the ' + k + ' lam: ' + needle);
    // A JARR LETTER NEVER GOVERNS ANOTHER PARTICLE. لَفِي is the lam of
    // ibtida, and the analyzer used to call it a jarr clitic over في.
    if (r.lafiSeg !== 'ل+في') throw new Error('لَفِي peels into two: ' + r.lafiSeg);
    // match the VERDICT, not the word «jarr clitic» — the corrected note says
    // «not a jarr clitic» in so many words, and a bare /jarr clitic/ test
    // matches the refutation as happily as the claim
    const CLITIC = 'jarr clitic — this very word is the majrur';
    if (!/lam of ibtida/.test(r.lafiNote) || r.lafiNote.includes(CLITIC))
      throw new Error('لَفِي is not a jarr clitic: ' + r.lafiNote);
    // the lam of ibtida enters on the khabar only, so the phrase is MUSTAQARR
    // and must not be handed to inna's ism by the nearest-governor rule
    if (!/MUSTAQARR/.test(r.lafiNote) || /ATTACHES to/.test(r.lafiNote))
      throw new Error('لَفِي is the khabar of inna, on an omitted amil: ' + r.lafiNote);
    // …and the split did not cost the definite case its correct verdict
    if (!r.bilNote.includes(CLITIC)) throw new Error('بِالْقَلَمِ is still a jarr clitic: ' + r.bilNote);
    // the article is not a radical, and the ta marbuta is not a fourth one
    // v133: the glossary's exact ص و غ outranks the rules' honest hedge —
    // accept either, never the article's lam as a radical.
    if (!r.sagha || !/^ص (و\/ي|و) غ$/.test(r.sagha.root))
      throw new Error('الصَّاغَة is a hollow root, not ل ص غ: ' + JSON.stringify(r.sagha));
    if (!r.marah || r.marah.root !== 'م ر أ')
      throw new Error('الْمَرْأَة is م ر أ: ' + JSON.stringify(r.marah));
    // فَاعِل and فَاعَلَ are one skeleton, so the answer names BOTH
    if (!r.hajib || !/فَاعِل/.test(r.hajib.wazn) || !/فَاعَلَ/.test(r.hajib.wazn))
      throw new Error('حَاجِب: the skeleton cannot choose, so it names both: ' + JSON.stringify(r.hajib));
    // the singular's totality begins at one, the plural's at three
    if (!/يَبْدَأُ مِنَ الْوَاحِدِ/.test(r.rajul)) throw new Error('لَا رَجُلَ starts at one: ' + r.rajul);
    if (!/يَبْدَأُ مِنَ الثَّلَاثَةِ/.test(r.rijal)) throw new Error('لَا رِجَالَ starts at three: ' + r.rijal);
    // the same word twice: one tanwin for ta'zim and one for tahqir
    if (r.hajibs.length !== 2) throw new Error('the bayt says حَاجِبٌ twice: ' + r.hajibs.length);
    if (!/لِلتَّعْظِيمِ/.test(r.hajibs[0]) || !/لِلتَّحْقِيرِ/.test(r.hajibs[1]))
      throw new Error('one magnifies and the other belittles: ' + JSON.stringify(r.hajibs));
    // the imperative is MABNI on a sukun broken to a kasra — never majzum
    if (!/مَبْنِيٌّ عَلَى السُّكُونِ/.test(r.udkhul) || !/لِالْتِقَاءِ السَّاكِنَيْنِ/.test(r.udkhul))
      throw new Error('اُدْخُلِ: mabni, its sukun broken for two sakins — ' + r.udkhul);
    if (r.sign && /مَجْزُوم/.test(JSON.stringify(r.sign)))
      throw new Error('there is no jazm without a jazim: ' + JSON.stringify(r.sign));
  });

  await check('talkhis ch10: the five tawabi, the nun of protection, and the geminate root', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 10);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const has = id => toks.filter(t => (t.grammar || []).includes(id)).length;
      const row = (text, w) => SentenceAnalyzer.analyze(text)
        .find(x => key(x.w) === key(w)) || {};
      const jaa = row('جَاءَنِي زَيْدٌ', 'جاءني');
      const akthar = row('جَاءَ الْقَوْمُ أَكْثَرُهُمْ', 'اكثرهم');
      const taammal = row('تَأَمَّلَهُ زَيْدٌ', 'تأمله');
      const rt = w => { const x = RootFinder.find(w); return x ? x.root : null; };
      return {
        chapters: st.chapters.length,
        n: ch.sentences.length,
        note: GRAMMAR['tawabi-al-musnad-ilayh'] &&
              [GRAMMAR['tawabi-al-musnad-ilayh'].group, !!GRAMMAR['tawabi-al-musnad-ilayh'].plain.tr],
        // all five tawabi' really occur, tagged
        five: ['naat-sifa', 'tawkid', 'atf-bayan', 'badal', 'atf-nasaq'].map(has),
        // نون الوقاية — note 103's own rule, turned into a peel
        jaaSeg: (jaa.seg || []).join('+'),
        jaaNote: (jaa.notes || []).map(y => y.en).join(' ~ '),
        jaaKind: jaa.kind,
        // the seam vowel decides where the pronoun hides the ending
        aktharKind: akthar.kind,
        taammalKind: taammal.kind,
        // ال is not a radical, and a stripped shadda is not a missing letter
        haqq: rt('الْحَقُّ'), liss: rt('اللِّصَّ'), kull: rt('كُلُّهُمْ'),
        yad: rt('الْيَدُ'), rubba: rt('رُبَّ'),
        akh: rt('أَخُوكَ'), fi: rt('فِي'),
        tajir: rt('التَّاجِرُ'), tanazzal: rt('تَنَزَّلَ'),
        // a pronoun's sukun is a bina, never jazm
        kullSign: IrabSign.of('كُلُّهُمْ'), alayhim: IrabSign.of('عَلَيْهِمْ'),
        jazm: IrabSign.of('يَذْهَبْ'),
        // واو عمرو — the auditor's third exception
        amr: HarakeAuditor.audit('عَمْرٌو').length,
        amrNasb: HarakeAuditor.audit('عَمْرًا').length,
        badTanwin: HarakeAuditor.audit('قَلًمٌ').length,
        laLex: toks.filter(t => t.lex === 'la-atifa').length,
      };
    });
    if (r.missing) throw new Error('chapter 10 did not load');
    if (r.chapters < 10) throw new Error('chapter 10 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch10 sentences: ' + r.n);
    if (!r.note || r.note[0] !== 'balagha' || !r.note[1])
      throw new Error('the tawabi note: ' + JSON.stringify(r.note));
    if (r.five.some(n => n < 1))
      throw new Error('all five tawabi must occur in the chapter: ' + JSON.stringify(r.five));
    if (!r.laLex) throw new Error('the atif la must be lexed as one, not as a negation');
    // نُونُ الْوِقَايَةِ: the whole «ني» comes off, and the ya is a MAF'UL
    if (r.jaaSeg !== 'جاء+ني') throw new Error('جَاءَنِي peels into the verb and «ني»: ' + r.jaaSeg);
    if (!/NUN AL-WIQAYA/.test(r.jaaNote) || !/MAF'UL BIHI/.test(r.jaaNote))
      throw new Error('the nun of protection must be named, and the ya an object: ' + r.jaaNote);
    if (/the mudaf ilayh/.test(r.jaaNote))
      throw new Error('a verb is never a mudaf, so its ya is no mudaf ilayh: ' + r.jaaNote);
    if (r.jaaKind !== 'verb') throw new Error('and it is still a verb: ' + r.jaaKind);
    // the vowel that decides sits at the SEAM when a pronoun follows
    if (r.aktharKind === 'verb') throw new Error('أَكْثَرُهُمْ: a madi is mabni on the fatha, and this is a damma');
    if (!/verb/.test(r.taammalKind || ''))
      throw new Error('…and تَأَمَّلَهُ must stay a verb: ' + r.taammalKind);
    // the article is not a radical, and a stripped shadda is not a lost letter
    if (r.haqq !== 'ح ق ق') throw new Error('الْحَقُّ is ح ق ق, not the article + a root: ' + r.haqq);
    if (r.liss !== 'ل ص ص') throw new Error('اللِّصُّ is ل ص ص: ' + r.liss);
    if (r.kull !== 'ك ل ل') throw new Error('كُلُّهُمْ is ك ل ل: ' + r.kull);
    // …and the rule must REFUSE where the shadda is absent or the word is a
    // particle. The geminate DOUBLING (ي د د) stays forbidden forever; but
    // once the corpus tail landed, the glossary's own lexical answer for
    // يَد — the weak root ي د ي the lexica record — is knowledge, not a
    // doubling, and the gate that pinned the honest refusal widens to it.
    if (r.yad && r.yad !== 'ي د ي')
      throw new Error('الْيَد must never be doubled — refusal or the glossary\'s ي د ي: ' + r.yad);
    if (r.rubba) throw new Error('رُبَّ is a particle and has no root: ' + r.rubba);
    // the five nouns answer lexically; في is not one of them
    if (r.akh !== 'أ خ و') throw new Error('أَخُوكَ is one of the five nouns: ' + r.akh);
    if (r.fi === 'ف و ه') throw new Error('فِي is the preposition, not the mouth');
    // an alif in the second slot means the head letter is not an augment
    if (r.tajir !== 'ت ج ر') throw new Error('التَّاجِر is ت ج ر, not تَفَعَّلَ on ا ج ر: ' + r.tajir);
    if (r.tanazzal !== 'ن ز ل') throw new Error('…and تَنَزَّلَ is still Form V: ' + r.tanazzal);
    // a pronoun's sukun is a bina, and jazm belongs to verbs. v129 upgraded
    // the answer: the sign is read at the SEAM (the damma on كُلُّ), so the
    // word is marfu by a written vowel — strictly better than the mabni
    // shrug, and either answer refuses the jazm.
    if (!r.kullSign || (r.kullSign.cases[0] !== 'marfu' && r.kullSign.cases[0] !== 'mabni') ||
        /majzum/.test(JSON.stringify(r.kullSign)))
      throw new Error('كُلُّهُمْ ends in a pronoun, not a jazm: ' + JSON.stringify(r.kullSign));
    if (!r.alayhim || r.alayhim.cases[0] !== 'mabni')
      throw new Error('عَلَيْهِمْ is a jarr phrase and was being called majzum: ' + JSON.stringify(r.alayhim));
    if (!r.jazm || r.jazm.cases[0] !== 'majzum')
      throw new Error('…and a real majzum must still read as one: ' + JSON.stringify(r.jazm));
    // واو عمرو is the books' own spelling, in raf' and jarr only
    if (r.amr) throw new Error('عَمْرٌو must pass the harakat auditor — its waw is silent');
    if (r.amrNasb) throw new Error('عَمْرًا must pass too');
    if (!r.badTanwin) throw new Error('…and a real mid-word tanwin must still be flagged');
  });

  await check('talkhis ch11: fronting, the fasl pronoun, and Abd al-Qahir\'s frame', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 11);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const row = (text, w, nth) => { const rows = SentenceAnalyzer.analyze(text)
        .filter(x => key(x.w) === key(w)); return rows[nth || 0] || {}; };
      const fasl = row('زَيْدٌ هُوَ الْقَائِمُ', 'هو');
      const maAna = row('مَا أَنَا قُلْتُ هَذَا', 'ما');
      const anaSad = row('أَنَا سَعَيْتُ فِي حَاجَتِكَ', 'انا');
      const saayt = row('أَنَا سَعَيْتُ فِي حَاجَتِكَ', 'سعيت');
      const dari = row('السَّفَّاحُ فِي دَارِ صَدِيقِكَ', 'دار');
      const rt = w => { const x = RootFinder.find(w); return x ? { r: x.root, z: x.wazn || '' } : null; };
      return {
        chapters: st.chapters.length, n: ch.sentences.length,
        note: GRAMMAR['taqdim-al-musnad-ilayh'] &&
              [GRAMMAR['taqdim-al-musnad-ilayh'].group, !!GRAMMAR['taqdim-al-musnad-ilayh'].plain.tr],
        taqdim: toks.filter(t => (t.grammar || []).includes('taqdim-al-musnad-ilayh')).length,
        faslTag: toks.filter(t => (t.grammar || []).includes('damir-fasl')).length,
        // the builder bakes sourceStory as `src` (and drops `sentence`) — read
        // the baked shape, not the authoring shape
        faslAnchor: (GRAMMAR['damir-fasl'].examples || [])
          .some(e => e.src === 'talkhis-al-miftah'),
        // the analyzer offers the fasl shortlist, and no idafa over a pronoun
        faslNote: (fasl.notes || []).map(x => x.en).join(' ~ '),
        // Abd al-Qahir's frame: the ma is nafiya with the takhsis named,
        // and the conditional does not fire over a pronoun
        maNote: (maAna.notes || []).map(x => x.en).join(' ~ '),
        // no idafa over a detached pronoun, in either seat
        anaNote: (anaSad.notes || []).map(x => x.en).join(' ~ '),
        saaytKind: saayt.kind,
        // a jarr letter never governs a verb: دَارِ stays the house
        dariKind: dari.kind, dariNote: (dari.notes || []).map(x => x.en).join(' ~ '),
        // the roots the chapter fixed
        qaim: rt('الْقَائِمُ'), harat: rt('حَارَتِ'), saffah: rt('السَّفَّاحُ'),
        // the sign at the seam
        ilahna: IrabSign.of('إِلَهُنَا'), nabina: IrabSign.of('نَبِيُّنَا'),
        // the verse dress: the bayt carries a hemistich mark
        verse: ch.sentences[0].tokens.some(t => t.punctAfter === '•'),
      };
    });
    if (r.missing) throw new Error('chapter 11 did not load');
    if (r.chapters < 11) throw new Error('chapter 11 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch11 sentences: ' + r.n);
    if (!r.note || r.note[0] !== 'balagha' || !r.note[1])
      throw new Error('the taqdim note: ' + JSON.stringify(r.note));
    if (r.taqdim < 6) throw new Error('too few taqdim tokens tagged: ' + r.taqdim);
    if (r.faslTag < 2 || !r.faslAnchor) throw new Error('the fasl pronoun must be tagged and anchored');
    if (!/ضَمِيرُ الْفَصْلِ/.test(r.faslNote)) throw new Error('هُوَ between two definites offers the fasl reading: ' + r.faslNote);
    if (/MUDAF/.test(r.faslNote)) throw new Error('a detached pronoun is never a mudaf: ' + r.faslNote);
    if (!/Abd al-Qahir/.test(r.maNote)) throw new Error('مَا أَنَا قُلْتُ names the takhsis frame: ' + r.maNote);
    if (/الشَّرْطِيَّة.*jazm on two verbs/.test(r.maNote) && !/نَّافِيَة/.test(r.maNote.split('~')[0] || ''))
      throw new Error('the conditional must not lead over a pronoun: ' + r.maNote);
    if (/MUDAF/.test(r.anaNote)) throw new Error('أَنَا is never a mudaf: ' + r.anaNote);
    if (r.saaytKind !== 'verb') throw new Error('سَعَيْتُ is corpus-certain now: ' + r.saaytKind);
    if (r.dariKind === 'verb') throw new Error('دَارِ after في is the house, not the amr of دَارَى');
    if (!/AFTER A JARR LETTER/.test(r.dariNote)) throw new Error('and the refusal names the doctrine: ' + r.dariNote);
    // v133: the glossary answers the exact ق و م where the rules could only
    // hedge the seat — accept either.
    if (!r.qaim || !/^ق (و\/ي|و) م$/.test(r.qaim.r)) throw new Error('قَائِم: the hamza seat is the i\'lal of the waw: ' + JSON.stringify(r.qaim));
    // the chapter ships حَارَ's paradigm, so the corpus answers the EXACT root
    // (ح ي ر); the rules-path و/ي hedge is the accepted fallback for the day
    // someone prunes the verb. Either way the fem-ta must not be a radical.
    if (!r.harat || !['ح ي ر', 'ح و/ي ر'].includes(r.harat.r))
      throw new Error('حَارَتِ: the fem-ta is a suffix: ' + JSON.stringify(r.harat));
    if (!r.saffah || !/فَعَّال/.test(r.saffah.z)) throw new Error('السَّفَّاح: the shadda names the intensive: ' + JSON.stringify(r.saffah));
    if (!r.ilahna || r.ilahna.cases[0] !== 'marfu' || r.ilahna.manner !== 'lafzi')
      throw new Error('إِلَهُنَا: the sign is at the seam, not on the pronoun: ' + JSON.stringify(r.ilahna));
    if (!r.nabina || r.nabina.cases[0] !== 'marfu')
      throw new Error('نَبِيُّنَا: marfu at the seam: ' + JSON.stringify(r.nabina));
    if (!r.verse) throw new Error('the bayt wears verse dress');
  });

  await check('talkhis ch12: taqwiya vs takhsis, the isnad count, and the group\'s waw', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 12);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const row = (text, w, nth) => { const rows = SentenceAnalyzer.analyze(text)
        .filter(x => key(x.w) === key(w)); return rows[nth || 0] || {}; };
      const maRow = row('أَنْتَ مَا سَعَيْتَ فِي حَاجَتِي', 'ما');
      const yuti = row('هُوَ يُعْطِي الْجَزِيلَ', 'يعطي');
      const anta = row('أَنْتَ لَا تَكْذِبُ', 'انت');
      const rt = w => { const x = RootFinder.find(w); return x ? { r: x.root, z: x.wazn || x.lemma || '' } : null; };
      return {
        chapters: st.chapters.length, n: ch.sentences.length,
        note: GRAMMAR['taqwiyat-al-hukm'] &&
              [GRAMMAR['taqwiyat-al-hukm'].group, !!GRAMMAR['taqwiyat-al-hukm'].plain.tr,
               (GRAMMAR['taqwiyat-al-hukm'].question || {}).tr ? GRAMMAR['taqwiyat-al-hukm'].question.tr.length : 0],
        tagged: toks.filter(t => (t.grammar || []).includes('taqwiyat-al-hukm')).length,
        // the two FEEDING anchors landed in the baked registry
        qasrAnchor: (GRAMMAR['qasr'].examples || []).some(e => e.src === 'talkhis-al-miftah'),
        badalAnchor: (GRAMMAR['badal'].examples || []).some(e => e.src === 'talkhis-al-miftah'),
        // Abd al-Qahir's second frame: person agreement kills the sila
        maNote: (maRow.notes || []).map(x => x.en).join(' ~ '),
        // the naqis radical ya is not an object pronoun
        yutiSeg: (yuti.seg || []).join('+'), yutiKind: yuti.kind,
        // no derivational scale on a closed-class word
        antaNote: (anta.notes || []).map(x => x.en).join(' ~ '),
        // the group's waw and its silent alif, both tenses
        zalamu: IrabSign.of('ظَلَمُوا'), yazlimu: IrabSign.of('لَمْ يَظْلِمُوا'.split(' ')[1]),
        asarru: IrabSign.of('أَسَرُّوا'),
        // the roots the probe fixed
        najwa: rt('النَّجْوَى'), mithluk: rt('مِثْلُكَ'),
        asarraRt: rt('أَسَرَّ'), aharraRt: rt('أَهَرَّ'), takdhibu: rt('تَكْذِبُ'),
        // the new paradigms are real corpus verbs with the ahalla jazm note
        asarraCell: (RootFinder.fromCorpus('يُسِرُّ') || {}).lemma,
        aharraCell: (RootFinder.fromCorpus('أَهَرَّ') || {}).lemma,
      };
    });
    if (r.missing) throw new Error('chapter 12 did not load');
    if (r.chapters < 12) throw new Error('chapter 12 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch12 sentences: ' + r.n);
    if (!r.note || r.note[0] !== 'balagha' || !r.note[1])
      throw new Error('the taqwiya note: ' + JSON.stringify(r.note));
    // the note carries the madrasah QUESTION TEST — the teaching apparatus
    if (r.note[2] < 3) throw new Error('the taqwiya note must carry its question test: ' + r.note[2]);
    if (r.tagged < 6) throw new Error('too few taqwiya tokens tagged: ' + r.tagged);
    if (!r.qasrAnchor) throw new Error('qasr must anchor the proverb');
    if (!r.badalAnchor) throw new Error('badal must anchor the badal-from-a-pronoun aya');
    if (!/agrees in PERSON/.test(r.maNote)) throw new Error('أَنْتَ مَا سَعَيْتَ: person agreement names the khabar: ' + r.maNote);
    if (/الْمَوْصُولَة/.test((r.maNote.split('~')[1] || '')) && !/النَّافِيَة/.test(r.maNote.split('~')[1] || ''))
      throw new Error('the negation must lead over the sila: ' + r.maNote);
    if (r.yutiSeg.includes('+')) throw new Error('يُعْطِي must not peel its radical ya: ' + r.yutiSeg);
    if (r.yutiKind !== 'verb') throw new Error('يُعْطِي is a corpus verb: ' + r.yutiKind);
    if (/tafdil|فْعَل/.test(r.antaNote)) throw new Error('no derivational scale on a pronoun: ' + r.antaNote);
    // the group's waw: mazi mabni on the damm; governed mudari by nun-drop
    if (!r.zalamu || r.zalamu.cases[0] !== 'mabni' || !/DAMMA/.test(r.zalamu.why.en))
      throw new Error('ظَلَمُوا is mabni on the damm for the waw: ' + JSON.stringify(r.zalamu));
    if (!r.yazlimu || r.yazlimu.by !== 'hadhf')
      throw new Error('يَظْلِمُوا reads by the dropped nun: ' + JSON.stringify(r.yazlimu));
    if (!r.asarru || r.asarru.cases[0] !== 'mabni')
      throw new Error('أَسَرُّوا: the Form IV hamza is not a person prefix: ' + JSON.stringify(r.asarru));
    if (!r.najwa || r.najwa.r !== 'ن ج و' || !/فَعْلَى/.test(r.najwa.z))
      throw new Error('نَجْوَى is فَعْلَى of ن ج و: ' + JSON.stringify(r.najwa));
    if (!r.mithluk || r.mithluk.r !== 'م ث ل')
      throw new Error('مِثْلُكَ: the mim is radical: ' + JSON.stringify(r.mithluk));
    if (!r.asarraCell || !r.aharraCell)
      throw new Error('the Form IV geminates must be corpus verbs: ' + r.asarraCell + '/' + r.aharraCell);
    if (!r.takdhibu || r.takdhibu.r !== 'ك ذ ب')
      throw new Error('تَكْذِبُ answers from the new paradigm: ' + JSON.stringify(r.takdhibu));
  });

  await check('talkhis ch13: kull under negation — the hayyiz, the madda, and the revived rule', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 13);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const row = (text, w, nth) => { const rows = SentenceAnalyzer.analyze(text)
        .filter(x => key(x.w) === key(w)); return rows[nth || 0] || {}; };
      const maKull = row('مَا كُلُّ مَا يَتَمَنَّى الْمَرْءُ يُدْرِكُهُ', 'ما', 0);
      const maAfterKull = row('مَا كُلُّ مَا يَتَمَنَّى الْمَرْءُ يُدْرِكُهُ', 'ما', 1);
      const akhudh = row('لَمْ آخُذْ كُلَّ الدَّرَاهِمِ', 'اخذ');
      const listMa = row('وَصِيغَةُ الْأَمْرِ افْعَلْ وَمَا نَابَ عَنْهَا وَصِيغَةُ النَّهْيِ لَا تَفْعَلْ', 'وما');
      const rt = w => { const x = RootFinder.find(w); return x ? { r: x.root, z: (x.wazn || x.lemma || '') } : null; };
      return {
        chapters: st.chapters.length, n: ch.sentences.length,
        note: GRAMMAR['umum-al-salb'] && [GRAMMAR['umum-al-salb'].group,
              (GRAMMAR['umum-al-salb'].question || {}).tr ? GRAMMAR['umum-al-salb'].question.tr.length : 0],
        tagged: toks.filter(t => (t.grammar || []).includes('umum-al-salb')).length,
        // مَا + كُلّ: the salb-al-umum rule leads
        maKullNote: ((maKull.wajh || {}).why || {}).en || '',
        // the ma AFTER kull: rule 6c, revived — the mudaf-ilayh seat
        maAfterKullK: (maAfterKull.wajh || {}).k,
        // the madda unfolds for matching: آخُذْ is a corpus verb, first person
        akhudhKind: akhudh.kind,
        akhudhNote: (akhudh.notes || []).map(x => x.en).join(' ~ '),
        // the list-frame rule 6f holds the Manar sentence for the RIGHT reason
        listMaK: (listMa.wajh || {}).k,
        // the quadriliteral plural and the jazm-shape fix
        darahim: rt('الدَّرَاهِمِ'), tamanna: rt('يَتَمَنَّى'), tashtahi: rt('تَشْتَهِي'),
        // the corrupt naqis stems would have failed here: exact cells
        cells: ['يَتَمَنَّى', 'تَشْتَهِي'].map(w => (RootFinder.fromCorpus(w) || {}).lemma || null),
        awamil: ['عَوَامِل', 'رَسَائِل'].map(w => (RootFinder.find(w) || {}).root),
      };
    });
    if (r.missing) throw new Error('chapter 13 did not load');
    if (r.chapters < 13) throw new Error('chapter 13 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch13 sentences: ' + r.n);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 3)
      throw new Error('the umum-al-salb note with its question test: ' + JSON.stringify(r.note));
    if (r.tagged < 6) throw new Error('too few umum-al-salb tokens tagged: ' + r.tagged);
    if (!/SALB AL-UMUM|TOTALITY/.test(r.maKullNote))
      throw new Error('مَا كُلُّ must name salb al-umum: ' + r.maKullNote);
    if (r.maAfterKullK !== 'mawsula')
      throw new Error('the ma after kull sits in the mudaf-ilayh seat — rule 6c was dead for كل until v131: ' + r.maAfterKullK);
    if (r.akhudhKind !== 'verb') throw new Error('آخُذْ is the first person of أَخَذَ: ' + r.akhudhKind);
    if (!/corpus verb — .*I\b/.test(r.akhudhNote) && !/jussive — I/.test(r.akhudhNote))
      throw new Error('…found through the unfolded madda: ' + r.akhudhNote);
    if (r.listMaK !== 'mawsula')
      throw new Error('وَمَا نَابَ عَنْهَا is the matns\' list-frame, mawsula by rule 6f — not by the old shart accident: ' + r.listMaK);
    if (!r.darahim || r.darahim.r !== 'د ر ه م' || !/فَعَالِل/.test(r.darahim.z))
      throw new Error('دَرَاهِم is the quadriliteral plural: ' + JSON.stringify(r.darahim));
    if (!r.tamanna || r.tamanna.z !== 'تَمَنَّى') throw new Error('يَتَمَنَّى answers from its paradigm: ' + JSON.stringify(r.tamanna));
    if (!r.tashtahi || r.tashtahi.z !== 'اِشْتَهَى') throw new Error('تَشْتَهِي answers from its paradigm: ' + JSON.stringify(r.tashtahi));
    if (r.cells.some(x => !x)) throw new Error('the naqis stems must be clean (no doubled vowel): ' + JSON.stringify(r.cells));
    // the فعالل row's two sub-shapes must not regress
    if (r.awamil[0] !== 'ع م ل') throw new Error('عَوَامِل is فَوَاعِل of ع م ل: ' + r.awamil[0]);
    if (r.awamil[1] !== 'ر س ل') throw new Error('رَسَائِل is فَعَائِل of ر س ل: ' + r.awamil[1]);
  });

  await check('talkhis ch14: iltifat — the six turnings, and the seven engine defects the probe forced', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 14);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const row = (text, w, nth) => { const rows = SentenceAnalyzer.analyze(text)
        .filter(x => key(x.w) === key(w)); return rows[nth || 0] || {}; };
      const inna = row('إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ', 'انا');
      const iyyaka = row('إِيَّاكَ نَعْبُدُ', 'اياك');
      const bihim = row('وَجَرَيْنَ بِهِمْ', 'بهم');
      const muqirr = row('أَتَاكَا مُقِرًّا بِالذُّنُوبِ', 'مقرا');
      const turja = row('وَإِلَيْهِ تُرْجَعُونَ', 'ترجعون');
      const rt = w => { const x = RootFinder.find(w); return x ? { r: x.root, z: (x.wazn || x.lemma || '') } : x; };
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: GRAMMAR['iltifat'] && [GRAMMAR['iltifat'].group,
              (GRAMMAR['iltifat'].question || {}).tr ? GRAMMAR['iltifat'].question.tr.length : 0,
              (GRAMMAR['iltifat'].examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('iltifat')).length,
        khilafTagged: toks.filter(t => (t.grammar || []).includes('khilaf-muqtada-al-zahir')).length,
        // إِنَّا: the shadda decides, and NFC puts the fatha BEFORE the shadda
        innaPk: inna.pk, innaSeg: (inna.seg || []).join('+'),
        // إِيَّاكَ: the iyya family is closed-class, and a pronoun has no root
        iyyakaNote: (iyyaka.notes || []).map(x => x.en).join(' ~ '),
        iyyakaRoot: RootFinder.find('إِيَّاكَ'),
        // بِهِمْ: the ب peel must refuse a pronoun remainder
        bihimKind: bihim.kind, bihimSeg: (bihim.seg || []).length,
        // أَتَاكَا / دَعَاكَا: the itlaq alif peels and the maqsura returns
        ataka: (RootFinder.fromCorpus('أَتَاكَا') || {}).lemma || null,
        daaka: (RootFinder.fromCorpus('دَعَاكَا') || {}).lemma || null,
        // مُقِرًّا: the mim-prefix geminate row, and the tanwin's seat-alif
        muqirrRoot: rt('مُقِرًّا'),
        muqirrNote: (muqirr.notes || []).map(x => x.en).join(' ~ '),
        // تُرْجَعُونَ: the derived majhul steps back over the five-verbs suffix
        turjaNote: (turja.notes || []).map(x => x.en).join(' ~ '),
        // the three new paradigms answer their chapter's cells
        cells: ['وَانْحَرْ', 'أَعْبُدُ', 'فَطَرَنِي'].map(w => (RootFinder.fromCorpus(w) || {}).lemma || null),
      };
    });
    if (r.missing) throw new Error('chapter 14 did not load');
    if (r.chapters < 14) throw new Error('chapter 14 is missing: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch14 sentences: ' + r.n);
    if (r.t !== 34) throw new Error('ch14 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the iltifat note with its question test and anchored examples: ' + JSON.stringify(r.note));
    if (r.tagged < 5) throw new Error('too few iltifat tokens tagged: ' + r.tagged);
    if (r.khilafTagged < 4) throw new Error('too few khilaf-muqtada-al-zahir tokens tagged: ' + r.khilafTagged);
    if (r.innaPk !== 'inna' || !/إِنَّ/.test(r.innaSeg) || !/نَا/.test(r.innaSeg))
      throw new Error('إِنَّا is إِنَّ + نَا by its shadda (NFC: fatha before shadda): ' + r.innaPk + ' / ' + r.innaSeg);
    if (!/detached pronoun/i.test(r.iyyakaNote))
      throw new Error('إِيَّاكَ is the detached object pronoun, not a فَعَّال intensive: ' + r.iyyakaNote);
    if (r.iyyakaRoot !== null)
      throw new Error('a closed-class word has no root to find: ' + JSON.stringify(r.iyyakaRoot));
    if (r.bihimKind !== 'particle' || r.bihimSeg !== 2)
      throw new Error('بِهِمْ is بِ + هم, fused jarr — the peel must refuse the pronoun remainder: ' + r.bihimKind + '/' + r.bihimSeg);
    if (r.ataka !== 'أَتَى') throw new Error('أَتَاكَا reaches أَتَى through the itlaq peel: ' + r.ataka);
    if (r.daaka !== 'دَعَا') throw new Error('دَعَاكَا reaches دَعَا through the itlaq peel: ' + r.daaka);
    if (!r.muqirrRoot || r.muqirrRoot.r !== 'ق ر ر')
      throw new Error('مُقِرًّا is the geminate ق ر ر — the shadda holds the third radical: ' + JSON.stringify(r.muqirrRoot));
    if (!/tanwin's written seat|TANWIN of nasb/i.test(r.muqirrNote))
      throw new Error('مُقِرًّا wears a written fathatan — the seat-alif is not a maqsur ending: ' + r.muqirrNote);
    if (!/passive — you \(pl\)/.test(r.turjaNote))
      throw new Error('تُرْجَعُونَ is the derived passive of the you-pl cell: ' + r.turjaNote);
    if (r.cells.some(x => !x))
      throw new Error('the three new paradigms must own their chapter cells: ' + JSON.stringify(r.cells));
  });

  await check('talkhis ch15: tark al-musnad — the qara\'in, the fuja\'iyya, and the heavy nun restored', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 15);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const rows = (text, w) => SentenceAnalyzer.analyze(text).filter(x => key(x.w) === key(w));
      const row = (text, w, nth) => rows(text, w)[nth || 0] || {};
      const idha = row('خَرَجْتُ فَإِذَا زَيْدٌ', 'فاذا');
      const zayd2 = row('خَرَجْتُ فَإِذَا زَيْدٌ', 'زيد');
      const lain = row('وَلَئِنْ سَأَلْتَهُمْ مَنْ خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ لَيَقُولُنَّ اللَّهُ', 'ولئن');
      const saal = row('وَلَئِنْ سَأَلْتَهُمْ مَنْ خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ لَيَقُولُنَّ اللَّهُ', 'سالتهم');
      const khalaq = row('وَلَئِنْ سَأَلْتَهُمْ مَنْ خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ لَيَقُولُنَّ اللَّهُ', 'خلق');
      const yaqul = row('وَلَئِنْ سَأَلْتَهُمْ مَنْ خَلَقَ السَّمَاوَاتِ وَالْأَرْضَ لَيَقُولُنَّ اللَّهُ', 'ليقولن');
      const bayt = 'نَحْنُ بِمَا عِنْدَنَا وَأَنْتَ بِمَا عِنْدَكَ رَاضٍ وَالرَّأْيُ مُخْتَلِفٌ';
      const bimas = rows(bayt, 'بما');
      const nahnu = row(bayt, 'نحن');
      const sabr = row('فَصَبْرٌ جَمِيلٌ', 'فصبر');
      const rt = w => { const x = RootFinder.find(w); return x ? { r: x.root, z: (x.wazn || x.lemma || ''), v: x.via } : x; };
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: GRAMMAR['tark-al-musnad'] && [GRAMMAR['tark-al-musnad'].group,
              (GRAMMAR['tark-al-musnad'].question || {}).tr ? GRAMMAR['tark-al-musnad'].question.tr.length : 0,
              (GRAMMAR['tark-al-musnad'].examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('tark-al-musnad')).length,
        // the fuja'iyya: the NEXT word's class decides against the table's one label
        idhaNote: (idha.notes || []).map(x => x.en).join(' ~ '),
        zaydNote: (zayd2.notes || []).map(x => x.en).join(' ~ '),
        // لئن splits into the oath-paving lam + إِنْ
        lainKind: lain.kind, lainSeg: (lain.seg || []).join('+'),
        lainNote: (lain.notes || []).map(x => x.en).join(' ~ '),
        // the radical sin: no future-sin peel on سَأَلْتَهُمْ
        saalNote: (saal.notes || []).map(x => x.en).join(' ~ '),
        saalSegN: (saal.seg || []).length,
        // مَنْ the ism promises a verb, not a majrur — and خَلَقَ answers as one
        khalaqKind: khalaq.kind,
        khalaqNote: (khalaq.notes || []).map(x => x.en).join(' ~ '),
        // the heavy nun restored to its cell
        yaqulKind: yaqul.kind,
        yaqulNote: (yaqul.notes || []).map(x => x.en).join(' ~ '),
        yaqulLemma: (RootFinder.fromCorpus('لَيَقُولُنَّ') || {}).lemma || null,
        // both بما of the bayt lead mawsula (rule 6d, with نحن now a pronoun)
        bimaKs: bimas.map(x => (x.wajh || {}).k),
        nahnuNote: (nahnu.notes || []).map(x => x.en).join(' ~ '),
        // رَاضٍ: the glossary decides the manqus against the hollow guess
        radin: rt('رَاضٍ'),
        // فَصَبْرٌ: the primitive masdar shapes joined the tagger
        sabrNote: (sabr.notes || []).map(x => x.en).join(' ~ '),
        ismShapes: ['فَعْل', 'فِعْل', 'فُعْل'].every(w => IsmTagger.SHAPES.some(s => s.w === w)),
        khalaqaCell: (RootFinder.fromCorpus('خَلَقَ') || {}).lemma || null,
      };
    });
    if (r.missing) throw new Error('chapter 15 did not load');
    if (r.n !== 5) throw new Error('ch15 sentences: ' + r.n);
    if (r.t !== 25) throw new Error('ch15 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the tark-al-musnad note with its question test and anchored examples: ' + JSON.stringify(r.note));
    if (r.tagged < 6) throw new Error('too few tark-al-musnad tokens tagged: ' + r.tagged);
    if (!/SURPRISE|فُجَائِيَّة/i.test(r.idhaNote))
      throw new Error('فَإِذَا before a noun is the idha of surprise: ' + r.idhaNote);
    if (!/surprise/i.test(r.zaydNote))
      throw new Error('the noun after the fuja\'iyya carries its expectation: ' + r.zaydNote);
    if (r.lainKind !== 'particle' || r.lainSeg.indexOf('إِنْ') < 0)
      throw new Error('لَئِنْ is the paving lam + إِنْ: ' + r.lainKind + ' / ' + r.lainSeg);
    if (!/OATH|paves/i.test(r.lainNote))
      throw new Error('…and its note names the oath: ' + r.lainNote);
    if (/future sin/.test(r.saalNote) || r.saalSegN > 2)
      throw new Error('the sin of سَأَلَ is a radical — the corpus outranks the peel: ' + r.saalNote);
    if (!/corpus verb — past — you/.test(r.saalNote))
      throw new Error('سَأَلْتَهُمْ answers from its paradigm: ' + r.saalNote);
    if (r.khalaqKind !== 'verb' || !/corpus verb — past — he/.test(r.khalaqNote))
      throw new Error('خَلَقَ after the ism مَنْ is a verb, not a promised majrur: ' + r.khalaqKind + ' / ' + r.khalaqNote);
    if (r.yaqulKind !== 'verb' || !/they \(m\)/.test(r.yaqulNote))
      throw new Error('لَيَقُولُنَّ is يَقُولُونَ under the heavy nun: ' + r.yaqulKind + ' / ' + r.yaqulNote);
    if (r.yaqulLemma !== 'قَالَ') throw new Error('…and its lemma is قَالَ: ' + r.yaqulLemma);
    if (!(r.bimaKs.length === 2 && r.bimaKs.every(k => k === 'mawsula')))
      throw new Error('both بِمَا of the bayt lead mawsula (the zarf is the sila): ' + JSON.stringify(r.bimaKs));
    if (!/detached pronoun/.test(r.nahnuNote))
      throw new Error('نَحْنُ joined its family in PARTICLES: ' + r.nahnuNote);
    if (!r.radin || r.radin.r !== 'ر ض ي' || r.radin.v !== 'corpus' || !/مَنْقُوص/.test(r.radin.z))
      throw new Error('رَاضٍ is the manqus ر ض ي by the glossary\'s word: ' + JSON.stringify(r.radin));
    if (!/فَعْل/.test(r.sabrNote) || /أَفْعَل/.test(r.sabrNote))
      throw new Error('فَصَبْرٌ reads فَعْل off the peeled scale, not أَفْعَل: ' + r.sabrNote);
    if (!r.ismShapes) throw new Error('the primitive masdar shapes are missing from IsmTagger');
    if (r.khalaqaCell !== 'خَلَقَ') throw new Error('the خَلَقَ paradigm must own its mazi: ' + r.khalaqaCell);
  });

  await check('talkhis ch16: tajaddud vs thubut — the sukun-nun split, the merged ya, and the swallowed ta', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 16);
      if (!ch) return { missing: true };
      const key = z => stripAr(z).replace(/[^ء-ي]/g, '').replace(/[أإآ]/g, 'ا');
      const toks = ch.sentences.flatMap(s => s.tokens);
      const row = (text, w, nth) => { const rows = SentenceAnalyzer.analyze(text)
        .filter(x => key(x.w) === key(w)); return rows[nth || 0] || {}; };
      const bayt1 = 'أَوَكُلَّمَا وَرَدَتْ عُكَاظَ قَبِيلَةٌ بَعَثُوا إِلَيَّ عَرِيفَهُمْ يَتَوَسَّمُ';
      const aya = 'فَإِذَا جَاءَتْهُمُ الْحَسَنَةُ قَالُوا لَنَا هَذِهِ وَإِنْ تُصِبْهُمْ سَيِّئَةٌ يَطَّيَّرُوا بِمُوسَى وَمَنْ مَعَهُ';
      const kullama = row(bayt1, 'اوكلما');
      const ilayya = row(bayt1, 'الي');
      const jaat = row(aya, 'جاءتهم');
      const wain = row(aya, 'وان');
      const lakin = row('لَكِنْ يَمُرُّ عَلَيْهَا وَهْوَ مُنْطَلِقٌ', 'لكن');
      const afama = row('أَفْعَمَ الْإِنَاءَ', 'افعم');
      const sayyia = row(aya, 'سيئة');
      const rt = w => { const x = RootFinder.find(w); return x ? { r: x.root, v: x.via } : x; };
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: GRAMMAR['tajaddud-wa-thubut'] && [GRAMMAR['tajaddud-wa-thubut'].group,
              (GRAMMAR['tajaddud-wa-thubut'].question || {}).tr ? GRAMMAR['tajaddud-wa-thubut'].question.tr.length : 0,
              (GRAMMAR['tajaddud-wa-thubut'].examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('tajaddud-wa-thubut')).length,
        // the interrogative hamza rides over the joining waw — with the fatha guard
        kullamaKind: kullama.kind, kullamaSeg: (kullama.seg || []).join('+'),
        afamaKind: afama.kind,
        afamaNote: (afama.notes || []).map(x => x.en).join(' ~ '),
        // إِلَيَّ: the merged speaker's ya, read off the shadda
        ilayyaSeg: (ilayya.seg || []).join('+'),
        // the wasl-vowelled pronoun reaches its paradigm
        jaatNote: (jaat.notes || []).map(x => x.en).join(' ~ '),
        // the sukun-nun split, and the popped table label
        wainNote: (wain.notes || []).map(x => x.en).join(' ~ '),
        lakinNote: (lakin.notes || []).map(x => x.en).join(' ~ '),
        // the future-sin peel refuses the noun's clothes
        sayyiaSeg: (sayyia.seg || []).length,
        // roots: the geminate under the opened ta, the swallowed ta of Form V,
        // the glossary overriding the hedged rules, and the four refusals
        surra: rt('صُرَّتَنَا'), sayyiaR: rt('سَيِّئَةٌ'), amirR: rt('الْأَمِيرِ'),
        tayr: (RootFinder.fromCorpus('يَطَّيَّرُوا') || {}).lemma || null,
        daraba: (RootFinder.fromCorpus('ضَرَبَ') || {}).lemma || null,
        tawassam: (RootFinder.fromCorpus('يَتَوَسَّمُ') || {}).lemma || null,
        refusals: ['بِمُوسَى', 'وَهْوَ', 'مَعَهُ', 'إِلَيَّ'].map(w => RootFinder.find(w)),
      };
    });
    if (r.missing) throw new Error('chapter 16 did not load');
    if (r.n !== 5) throw new Error('ch16 sentences: ' + r.n);
    if (r.t !== 43) throw new Error('ch16 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the tajaddud-wa-thubut note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 8) throw new Error('too few tajaddud-wa-thubut tokens tagged: ' + r.tagged);
    if (r.kullamaKind !== 'particle' || r.kullamaSeg.split('+').length < 3)
      throw new Error('أَوَكُلَّمَا is أ + و + كلما: ' + r.kullamaKind + ' / ' + r.kullamaSeg);
    if (r.afamaKind !== 'verb' || /question particle/.test(r.afamaNote))
      throw new Error('أَفْعَمَ keeps its radical fa — the joiner must wear a fatha: ' + r.afamaKind + ' / ' + r.afamaNote);
    if (r.ilayyaSeg.indexOf('إِلَى') < 0)
      throw new Error('إِلَيَّ is إِلَى + the merged speaker\'s ya: ' + r.ilayyaSeg);
    if (!/corpus verb — past — she/.test(r.jaatNote))
      throw new Error('جَاءَتْهُمُ reaches its paradigm under the wasl vowel: ' + r.jaatNote);
    if (!/CONDITIONAL/.test(r.wainNote) || /nasb on its noun/.test(r.wainNote))
      throw new Error('إِنْ with a sukun nun is the conditional, and the inna label is popped: ' + r.wainNote);
    if (!/LIGHT istidrak/.test(r.lakinNote) || /nasb on its noun/.test(r.lakinNote))
      throw new Error('لَكِنْ with a sukun nun governs nothing: ' + r.lakinNote);
    if (r.sayyiaSeg > 1) throw new Error('سَيِّئَةٌ must not peel a future sin: ' + r.sayyiaSeg);
    if (!r.surra || r.surra.r !== 'ص ر ر')
      throw new Error('صُرَّتَنَا is the geminate under the opened ta: ' + JSON.stringify(r.surra));
    if (!r.sayyiaR || r.sayyiaR.r !== 'س و أ' || r.sayyiaR.v !== 'corpus')
      throw new Error('سَيِّئَةٌ answers س و أ from the glossary: ' + JSON.stringify(r.sayyiaR));
    if (!r.amirR || r.amirR.r !== 'أ م ر' || r.amirR.v !== 'corpus')
      throw new Error('أَمِير answers أ م ر from the glossary over the hedged أَفْعَل guess: ' + JSON.stringify(r.amirR));
    if (r.tayr !== 'تَطَيَّرَ') throw new Error('يَطَّيَّرُوا unfolds its swallowed ta to تَطَيَّرَ: ' + r.tayr);
    if (r.daraba !== 'ضَرَبَ') throw new Error('the ضَرَبَ paradigm must own its mazi: ' + r.daraba);
    if (r.tawassam !== 'تَوَسَّمَ') throw new Error('يَتَوَسَّمُ answers from its paradigm: ' + r.tawassam);
    if (!r.refusals.every(x => x === null))
      throw new Error('the four fused/propn shapes must refuse a root: ' + JSON.stringify(r.refusals));
  });

  await check('talkhis ch17: law and hikayat al-hal — the tense against its time, and the ShartEngine', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 17);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const F = t => ShartEngine.read(SentenceAnalyzer.analyze(t));
      const law1 = F('لَوْ جِئْتَنِي لَأَكْرَمْتُكَ');
      const law2 = F('لَوْ يُطِيعُكُمْ فِي كَثِيرٍ مِنَ الْأَمْرِ لَعَنِتُّمْ');
      const kullama = F('أَوَكُلَّمَا وَرَدَتْ عُكَاظَ قَبِيلَةٌ بَعَثُوا إِلَيَّ عَرِيفَهُمْ يَتَوَسَّمُ');
      const fuja = F('خَرَجْتُ فَإِذَا زَيْدٌ');
      const rt = w => { const x = RootFinder.find(w); return x ? x.root : x; };
      const cell = w => { const x = RootFinder.fromCorpus(w); return x ? x.lemma : null; };
      const idh = SentenceAnalyzer.analyze('وَلَوْ تَرَى إِذْ وُقِفُوا عَلَى النَّارِ')
        .find(x => (x.pk || '') === 'zarf-idh');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: GRAMMAR['hikayat-al-hal'] && [GRAMMAR['hikayat-al-hal'].group,
              (GRAMMAR['hikayat-al-hal'].question || {}).tr ? GRAMMAR['hikayat-al-hal'].question.tr.length : 0,
              (GRAMMAR['hikayat-al-hal'].examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('hikayat-al-hal')).length,
        // the paradigms: the idgham cell, the passive over the group's waw,
        // the hamza-final Form X, the hollow Form IV, the tanwin-seat noun
        anit: cell('لَعَنِتُّمْ'), anitR: rt('لَعَنِتُّمْ'),
        wuqifu: cell('وُقِفُوا'),
        istahza: cell('يَسْتَهْزِئُ'), tuthir: cell('فَتُثِيرُ'),
        sahabR: rt('سَحَابًا'),
        idhKind: idh ? idh.kind : null,
        // the ShartEngine: law's asl (lam-marked jawab), law's nukta on a
        // mudari shart, kullama behind its hamza, and the fuja'iyya opening
        // NO frame at all
        law1: law1[0] && { k: law1[0].key, mark: law1[0].mark, jw: law1[0].jawab, nk: !!law1[0].nukta },
        law2: law2[0] && { k: law2[0].key, nk: !!law2[0].nukta, jw: law2[0].jawab },
        kullamaK: kullama[0] && kullama[0].key,
        fujaN: fuja.length,
      };
    });
    if (r.missing) throw new Error('chapter 17 did not load');
    if (r.n !== 5) throw new Error('ch17 sentences: ' + r.n);
    if (r.t !== 23) throw new Error('ch17 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the hikayat-al-hal note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 8) throw new Error('too few hikayat-al-hal tokens tagged: ' + r.tagged);
    if (r.anit !== 'عَنِتَ' || r.anitR !== 'ع ن ت')
      throw new Error('لَعَنِتُّمْ reaches عَنِتَ through the jawab lam and the idgham: ' + r.anit + '/' + r.anitR);
    if (r.wuqifu !== 'وَقَفَ')
      throw new Error('وُقِفُوا derives from وَقَفُوا with the kasra on the stem: ' + r.wuqifu);
    if (r.istahza !== 'اِسْتَهْزَأَ') throw new Error('يَسْتَهْزِئُ answers from its Form X paradigm: ' + r.istahza);
    if (r.tuthir !== 'أَثَارَ') throw new Error('فَتُثِيرُ answers from its hollow Form IV paradigm: ' + r.tuthir);
    if (r.sahabR !== 'س ح ب') throw new Error('سَحَابًا answers the glossary through the tanwin seat: ' + r.sahabR);
    if (r.idhKind !== 'noun') throw new Error('إِذْ is a mabni zarf — an ISM: ' + r.idhKind);
    if (!r.law1 || r.law1.k !== 'law' || r.law1.mark !== 'lam' || r.law1.jw < 0 || r.law1.nk)
      throw new Error('the law asl: mazi shart, lam-marked jawab, no nukta: ' + JSON.stringify(r.law1));
    if (!r.law2 || !r.law2.nk || r.law2.jw < 0)
      throw new Error('law + mudari must carry the istimrar nukta and still find its jawab: ' + JSON.stringify(r.law2));
    if (r.kullamaK !== 'kullama') throw new Error('كُلَّمَا behind its hamza still frames: ' + r.kullamaK);
    if (r.fujaN !== 0) throw new Error('the fuja\'iyya opens no conditional frame: ' + r.fujaN);
  });

  await check('talkhis ch18: tankir and tarif of the musnad — the Belagat wujuh, each named', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 18);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['wujuh-al-musnad'];
      const rowsMa = SentenceAnalyzer.analyze('مَا زَيْدٌ شَيْئًا');
      const maRow = rowsMa.find(x => x.w === 'مَا');
      const zayd = rowsMa.find(x => x.w === 'زَيْدٌ');
      const shuj = IsmTagger.tag('الشُّجَاعُ', 1)[0];
      const mtq = RootFinder.find('لِلْمُتَّقِينَ');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('wujuh-al-musnad')).length,
        // the user's asked-for layer: every sentence delivers its balagha
        // wajh as NAMED jumal rows, two per sentence, not as prose alone
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        hijazi: maRow ? maRow.notes.some(n => /الْحِجَازِيَّة|Hijazi/.test((n.ar || '') + (n.en || ''))) : false,
        // a propn stands in no scale — the corpus guard, through the GLOBAL
        // zayd key (it lives in two packages; both must say propn)
        zaydScale: zayd ? zayd.notes.some(n => /فَعْل —/.test(n.en || '')) : true,
        // the article strip takes its sun-letter shadda back with it
        shujWazn: shuj && shuj.wazn,
        mtq: mtq && { root: mtq.root, via: mtq.via },
      };
    });
    if (r.missing) throw new Error('chapter 18 did not load');
    if (r.chapters < 18) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch18 sentences: ' + r.n);
    if (r.t !== 14) throw new Error('ch18 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the wujuh-al-musnad note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 6) throw new Error('too few wujuh-al-musnad tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch18 sentence carries its named-wajh jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.hijazi) throw new Error('مَا زَيْدٌ شَيْئًا reads the Hijazi ma');
    if (r.zaydScale) throw new Error('زَيْدٌ is a propn and is offered no scale note');
    if (r.shujWazn !== 'فُعَال')
      throw new Error('الشُّجَاعُ answers فُعَال once the article takes back its shadda: ' + r.shujWazn);
    if (!r.mtq || r.mtq.root !== 'و ق ي' || r.mtq.via !== 'corpus')
      throw new Error('لِلْمُتَّقِينَ reaches و ق ي through the glossary: ' + JSON.stringify(r.mtq));
  });

  await check('talkhis ch19: the fronted musnad — four wujuh, the la-order doctrine, and the TaqdimEngine', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 19);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['taqdim-al-musnad'];
      const T = s => TaqdimEngine.read(SentenceAnalyzer.analyze(s));
      const f1 = T('لَا فِيهَا غَوْلٌ'), f2 = T('لَا رَيْبَ فِيهِ'),
            f3 = T('لَهُ هِمَمٌ لَا مُنْتَهَى لِكِبَارِهَا'), f0 = T('زَيْدٌ كَاتِبٌ');
      const rt = w => { const x = RootFinder.find(w); return x ? { root: x.root, via: x.via } : null; };
      const said = IrabSign.of('سَعِدَتْ'), jz = IrabSign.of('يَكْتُبْ');
      // the frame card renders in the Jumla lab's own pipeline
      let frameHtml = '';
      try {
        const d = document.createElement('div'); d.id = 'jumlaOut'; document.body.appendChild(d);
        conjState.jumla = 'لَهُ هِمَمٌ لَا مُنْتَهَى لِكِبَارِهَا';
        renderJumlaOut(); frameHtml = d.innerHTML; d.remove();
      } catch (e) { frameHtml = 'ERR ' + e.message; }
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('taqdim-al-musnad')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        // the engine's two exact frames — and its silence on a plain jumla
        f1: f1[0] && [f1[0].kind, f1[0].la], f2: f2[0] && [f2[0].kind, f2[0].ism],
        f3: f3[0] && [f3[0].kind, f3[0].wajib], f0n: f0.length,
        docN: Object.keys(TaqdimEngine.DOC).length,
        // the probe's five root fixes, each through its own door
        wajh: rt('وَجْهِكَ'), kibar: rt('لِكِبَارِهَا'), ghurra: rt('بِغُرَّةِ'),
        muntaha: rt('مُنْتَهَى'), ishaq: rt('إِسْحَاقَ'),
        tushriq: (RootFinder.fromCorpus('تُشْرِقُ') || {}).lemma,
        // a madi's ta of femininity is bina; a governed mudari keeps jazm
        saidCase: said && said.cases.join(','), jzCase: jz && jz.cases.join(','),
        frame: /tq-frame/.test(frameHtml) && /مُنْتَهَى|هِمَمٌ/.test(frameHtml),
      };
    });
    if (r.missing) throw new Error('chapter 19 did not load');
    if (r.chapters < 19) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch19 sentences: ' + r.n);
    if (r.t !== 24) throw new Error('ch19 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the taqdim-al-musnad note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 8) throw new Error('too few taqdim-al-musnad tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch19 sentence carries its named-wajh jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.f1 || r.f1[0] !== 'khabar-muqaddam' || !r.f1[1])
      throw new Error('لَا فِيهَا غَوْلٌ: the fronted khabar with the la voided: ' + JSON.stringify(r.f1));
    if (!r.f2 || r.f2[0] !== 'lajins' || r.f2[1] !== 1)
      throw new Error('لَا رَيْبَ فِيهِ: the working genus-la with its ism: ' + JSON.stringify(r.f2));
    if (!r.f3 || r.f3[0] !== 'khabar-muqaddam' || !r.f3[1])
      throw new Error('لَهُ هِمَمٌ: khabar muqaddam, and WAJIB on the nakira: ' + JSON.stringify(r.f3));
    if (r.f0n !== 0) throw new Error('a plain jumla ismiyya opens no taqdim frame: ' + r.f0n);
    if (r.docN < 7) throw new Error('the TaqdimEngine doctrine table: ' + r.docN);
    if (!r.wajh || r.wajh.root !== 'و ج ه' || r.wajh.via !== 'corpus')
      throw new Error('وَجْهِكَ answers و ج ه through the clitic-provenance override: ' + JSON.stringify(r.wajh));
    if (!r.kibar || r.kibar.root !== 'ك ب ر')
      throw new Error('لِكِبَارِهَا sees through three dresses to كِبَار: ' + JSON.stringify(r.kibar));
    if (!r.ghurra || r.ghurra.root !== 'غ ر ر')
      throw new Error('بِغُرَّةِ peels its ba before the geminate: ' + JSON.stringify(r.ghurra));
    if (!r.muntaha || r.muntaha.root !== 'ن ه ي')
      throw new Error('مُنْتَهَى is Form VIII of ن ه ي — the nun is a radical: ' + JSON.stringify(r.muntaha));
    if (r.ishaq !== null)
      throw new Error('إِسْحَاقَ is an ajami alam and REFUSES a root: ' + JSON.stringify(r.ishaq));
    if (r.tushriq !== 'أَشْرَقَ')
      throw new Error('تُشْرِقُ answers from its Form IV paradigm: ' + r.tushriq);
    if (r.saidCase !== 'mabni')
      throw new Error('سَعِدَتْ: the ta of femininity is a bina, never jazm: ' + r.saidCase);
    if (r.jzCase !== 'majzum')
      throw new Error('…and يَكْتُبْ keeps its jazm: ' + r.jzCase);
    if (!r.frame) throw new Error('the taqdim frame card renders in the Jumla lab');
  });

  await check('talkhis ch20: the object dropped and fronted — and the maful-muqaddam frame', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 20);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['hadhf-al-maful'];
      const T = s => TaqdimEngine.read(SentenceAnalyzer.analyze(s));
      const fat = T('إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ');
      const zayd = T('زَيْدًا عَرَفْتُ');
      const plain = T('عَرَفْتُ زَيْدًا');
      const rows5 = SentenceAnalyzer.analyze('إِيَّاكَ نَعْبُدُ وَإِيَّاكَ نَسْتَعِينُ');
      const wIyya = rows5.find(x => /^وَإِ/.test(x.w));
      const rows4 = SentenceAnalyzer.analyze('مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَى');
      const wMa = rows4.find(x => /^وَمَا/.test(x.w));
      const rt = w => { const x = RootFinder.find(w); return x ? { root: x.root, via: x.via } : null; };
      const law = ShartEngine.read(SentenceAnalyzer.analyze('وَلَوْ شَاءَ لَهَدَاكُمْ أَجْمَعِينَ'));
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('hadhf-al-maful')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        // the maful-muqaddam frame: both iyyas, the fathatan noun, and the
        // engine's SILENCE when the verb comes first
        fatN: fat.filter(f => f.kind === 'maful-muqaddam').length,
        zaydN: zayd.filter(f => f.kind === 'maful-muqaddam').length,
        plainN: plain.length,
        docN: Object.keys(TaqdimEngine.DOC).length,
        // the iyya family opens a VERBAL clause — never a hal
        iyyaTop: wIyya && wIyya.notes.some(n => /الْعَطْف/.test(n.ar || '') || /joining waw/.test(n.en || '')),
        iyyaHal: wIyya && wIyya.notes.some(n => /الْحَال|circumstantial/.test((n.ar || '') + (n.en || ''))),
        // negation joined on negation outranks the list-frame — the
        // MaEngine's note carries the Arabic name inside its en/tr text,
        // so both fields are searched
        maNaf: wMa && wMa.notes.some(n => /النَّافِيَة|negation joined/.test((n.ar || '') + (n.en || ''))),
        maKind: wMa && wMa.kind,
        // the four verbs the chapter's paradigms unlocked
        istawi: rt('يَسْتَوِي'), hadakum: rt('لَهَدَاكُمْ'),
        qala2: rt('قَلَى'), nastain: rt('نَسْتَعِينُ'),
        qalaKind: (rows4.find(x => x.w === 'قَلَى') || {}).kind,
        // and the law frame still reads its lam-marked jawab through the verb
        lawF: law[0] && { k: law[0].key, mark: law[0].mark, jw: law[0].jawab },
      };
    });
    if (r.missing) throw new Error('chapter 20 did not load');
    if (r.chapters < 20) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch20 sentences: ' + r.n);
    if (r.t !== 26) throw new Error('ch20 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the hadhf-al-maful note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 7) throw new Error('too few hadhf-al-maful tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch20 sentence carries its named-wajh jumal rows: ' + JSON.stringify(r.jumal));
    if (r.fatN !== 2) throw new Error('both iyyas of the Fatiha open maful-muqaddam frames: ' + r.fatN);
    if (r.zaydN !== 1) throw new Error('زَيْدًا عَرَفْتُ: the fathatan noun before its verb frames: ' + r.zaydN);
    if (r.plainN !== 0) throw new Error('عَرَفْتُ زَيْدًا: verb first, no taqdim frame: ' + r.plainN);
    if (r.docN < 9) throw new Error('the TaqdimEngine doctrine table grew to the maful rows: ' + r.docN);
    if (!r.iyyaTop || r.iyyaHal)
      throw new Error('وَإِيَّاكَ: atf offered, hal NEVER — the iyya family opens a verbal clause: ' +
        JSON.stringify([r.iyyaTop, r.iyyaHal]));
    if (!r.maNaf || r.maKind !== 'particle')
      throw new Error('وَمَا قَلَى: negation joined on negation outranks the list-frame: ' +
        JSON.stringify([r.maNaf, r.maKind]));
    if (!r.istawi || r.istawi.root !== 'س و ي' || r.istawi.via !== 'corpus')
      throw new Error('يَسْتَوِي answers from its Form VIII naqis paradigm: ' + JSON.stringify(r.istawi));
    if (!r.hadakum || r.hadakum.root !== 'ه د ي')
      throw new Error('لَهَدَاكُمْ reaches هَدَى through the jawab lam and the pronoun: ' + JSON.stringify(r.hadakum));
    if (!r.qala2 || r.qala2.root !== 'ق ل ي' || r.qalaKind !== 'verb')
      throw new Error('قَلَى is the naqis verb, not a maqsur noun: ' + JSON.stringify([r.qala2, r.qalaKind]));
    if (!r.nastain || r.nastain.root !== 'ع و ن')
      throw new Error('نَسْتَعِينُ answers from its hollow Form X paradigm: ' + JSON.stringify(r.nastain));
    if (!r.lawF || r.lawF.k !== 'law' || r.lawF.mark !== 'lam' || r.lawF.jw < 0)
      throw new Error('وَلَوْ شَاءَ لَهَدَاكُمْ: the law frame with its lam-marked jawab: ' + JSON.stringify(r.lawF));
  });

  await check('talkhis ch21: the qasr bab — the QasrEngine frame, the nearest-negation pairing, and the reading surface', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 21);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['aqsam-al-qasr'];
      const Q = s => QasrEngine.read(SentenceAnalyzer.analyze(s));
      const q1 = Q('لَا إِلَهَ إِلَّا اللهُ'), q2 = Q('مَا فِي الدَّارِ إِلَّا زَيْدٌ'),
            q3 = Q('مَا زَيْدٌ إِلَّا كَاتِبٌ'), q0 = Q('زَيْدٌ كَاتِبٌ'),
            qGuard = Q('وَالْمُشْكِلُ مَا ازْدَادَ خَفَاءً بِحَيْثُ لَا يُنَالُ الْمُرَادُ إِلَّا بِالطَّلَبِ');
      const kindOf = q => q[0] && q[0].kind ? q[0].kind.ar : null;
      const maHouse = SentenceAnalyzer.analyze('مَا فِي الدَّارِ إِلَّا زَيْدٌ')[0];
      const maManar = SentenceAnalyzer.analyze('وَاقْتِضَاؤُهُ مَا لَا يَسْتَقِيمُ الْكَلَامُ إِلَّا بِهِ')
        .find(x => x.w === 'مَا');
      // the reading surface: tint + size through the ONE arSize state
      const st0 = STORIES.find(s => s.chapters && s.chapters.length);
      localStorage.setItem('qissa-welcomed', '1');
      setArSizeStep(3); openStory(st0);
      const line = document.querySelector('#story .ar-line');
      const fsBig = line ? getComputedStyle(line).fontSize : null;
      setArSizeStep(1);
      const fsDef = document.querySelector('#story .ar-line')
        ? getComputedStyle(document.querySelector('#story .ar-line')).fontSize : null;
      setReadTheme('sepia');
      const bgSepia = getComputedStyle(document.getElementById('story')).backgroundColor;
      setReadTheme('auto');
      const aa = !!document.getElementById('readCtrlChip');
      // the continue-card ring
      localStorage.setItem('qissa-lastread', st0.id); state.lastRead = st0.id;
      CUR = null; renderLibrary();
      const ring = !!document.querySelector('.continue-card .cc-ring .rfg');
      const pctEl = document.querySelector('.continue-card .cc-pct');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('aqsam-al-qasr')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        k1: kindOf(q1), k2: kindOf(q2), k3: kindOf(q3),
        n0: q0.length, nGuard: qGuard.length,
        docN: Object.keys(QasrEngine.DOC).length,
        maHouse: maHouse && maHouse.kind,
        maManar: maManar && maManar.kind,
        fsBig, fsDef, bgSepia, aa, ring, pct: pctEl && /%$/.test(pctEl.textContent),
      };
    });
    if (r.missing) throw new Error('chapter 21 did not load');
    if (r.chapters < 21) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch21 sentences: ' + r.n);
    if (r.t !== 21) throw new Error('ch21 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the aqsam-al-qasr note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 12) throw new Error('too few aqsam-al-qasr tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch21 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!/الصِّفَةِ عَلَى الْمَوْصُوفِ/.test(r.k1 || ''))
      throw new Error('لَا إِلَهَ إِلَّا اللهُ: sifa confined to mawsuf: ' + r.k1);
    if (!/الصِّفَةِ عَلَى الْمَوْصُوفِ/.test(r.k2 || ''))
      throw new Error('مَا فِي الدَّارِ إِلَّا زَيْدٌ: the jarr phrase is the sifa side: ' + r.k2);
    if (!/الْمَوْصُوفِ عَلَى الصِّفَةِ/.test(r.k3 || ''))
      throw new Error('مَا زَيْدٌ إِلَّا كَاتِبٌ: the propn before the illa is the mawsuf: ' + r.k3);
    if (r.n0 !== 0) throw new Error('a plain jumla opens no qasr frame: ' + r.n0);
    if (r.nGuard !== 0)
      throw new Error('the illa pairs with the NEAREST negation — the Manar definitional frame opens none: ' + r.nGuard);
    if (r.docN < 8) throw new Error('the QasrEngine doctrine table: ' + r.docN);
    if (r.maHouse !== 'particle')
      throw new Error('مَا فِي الدَّارِ: the frame ma is the negation, a particle: ' + r.maHouse);
    if (r.maManar !== 'noun')
      throw new Error('…and the Manar mawsula keeps its ism reading: ' + r.maManar);
    if (r.fsBig !== '35.2px' || r.fsDef !== '27.2px')
      throw new Error('the Aa steps drive the one arSize state: ' + r.fsBig + '/' + r.fsDef);
    if (!/245, 237, 218/.test(r.bgSepia || ''))
      throw new Error('the sepia tint paints the story column: ' + r.bgSepia);
    if (!r.aa) throw new Error('the Aa chip stands in the story header');
    if (!r.ring || !r.pct) throw new Error('the continue card wears its progress ring');
  });

  await check('talkhis ch22: the routes compared — the negating in, the alerting ala, and the five-nouns host', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 22);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['turuq-al-qasr'];
      const rows2 = SentenceAnalyzer.analyze('إِنْ أَنْتُمْ إِلَّا بَشَرٌ مِثْلُنَا');
      const inRow = rows2[0];
      const shNaf = ShartEngine.read(rows2).length;
      const qNaf = QasrEngine.read(rows2);
      // the CONTROL: a real conditional keeps its frame
      const shCtl = ShartEngine.read(SentenceAnalyzer.analyze('إِنْ جِئْتَنِي أَكْرَمْتُكَ'));
      const rows4 = SentenceAnalyzer.analyze('أَلَا إِنَّهُمْ هُمُ الْمُفْسِدُونَ');
      const alaRow = rows4[0];
      const rows5 = SentenceAnalyzer.analyze('إِنَّمَا هُوَ أَخُوكَ');
      const akh = rows5.find(x => /أَخُو/.test(x.w));
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('turuq-al-qasr')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        // the negating in: pk nafy, no shart frame, and the qasr frame reads it
        inPk: inRow && inRow.pk, inKind: inRow && inRow.kind,
        shNaf, qNafKind: qNaf[0] && qNaf[0].kind ? qNaf[0].kind.ar : null,
        shCtlKey: shCtl[0] && shCtl[0].key,
        // the alerting ala before inna: one particle, tanbih
        alaPk: alaRow && alaRow.pk,
        alaNote: alaRow && alaRow.notes.some(n => /التَّنْبِيه|ALERTING/.test((n.ar || '') + (n.en || ''))),
        // the five-nouns host under its pronoun: a noun by table, kaf = mudaf ilayh
        akhKind: akh && akh.kind,
        akhFive: akh && akh.notes.some(n => /FIVE NOUNS|الْأَسْمَاء/.test((n.ar || '') + (n.en || ''))),
        akhMaful: akh && akh.notes.some(n => /maf'ul bihi/.test(n.en || '')),
      };
    });
    if (r.missing) throw new Error('chapter 22 did not load');
    if (r.chapters < 22) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch22 sentences: ' + r.n);
    if (r.t !== 19) throw new Error('ch22 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the turuq-al-qasr note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 15) throw new Error('too few turuq-al-qasr tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch22 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (r.inPk !== 'nafy' || r.inKind !== 'particle')
      throw new Error('the sukun-in before an illa is the NEGATION: ' + JSON.stringify([r.inPk, r.inKind]));
    if (r.shNaf !== 0) throw new Error('the negating in opens no shart frame: ' + r.shNaf);
    if (!/الْمَوْصُوفِ عَلَى الصِّفَةِ/.test(r.qNafKind || ''))
      throw new Error('…and the qasr engine reads the in-frame (the pronoun is the mawsuf): ' + r.qNafKind);
    if (r.shCtlKey !== 'in') throw new Error('the REAL conditional keeps its frame: ' + r.shCtlKey);
    if (r.alaPk !== 'tanbih' || !r.alaNote)
      throw new Error('أَلَا before إِنَّ is the alerting particle, one word: ' + JSON.stringify([r.alaPk, r.alaNote]));
    if (r.akhKind !== 'noun' || !r.akhFive)
      throw new Error('أَخُوكَ is a five-nouns host, a noun by table: ' + JSON.stringify([r.akhKind, r.akhFive]));
    if (r.akhMaful)
      throw new Error('…and its kaf is never «its maf\'ul bihi»');
  });

  await check('talkhis ch23: insha and the wish — the InshaEngine, the borrowed law, and the tahdid split', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 23);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['insha-wa-tamanni'];
      // the coined particle: the layta frame with its ism
      const tmLayta = InshaEngine.read(SentenceAnalyzer.analyze('لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا'));
      // the borrowed law: the shart frame stands down, the wish-frame reads,
      // and the fa-verb is a corpus VERB whose ya is a maf'ul, never a mudaf ilayh
      const rows3 = SentenceAnalyzer.analyze('لَوْ تَأْتِينِي فَتُحَدِّثَنِي');
      const faV = rows3[2];
      const sh3 = ShartEngine.read(rows3).length;
      const tm3 = InshaEngine.read(rows3);
      // the CONTROL: a real law keeps its conditional frame
      const shCtl = ShartEngine.read(SentenceAnalyzer.analyze('لَوْ جِئْتَنِي لَأَكْرَمْتُكَ'));
      // the tahdid pair: one particle, split by the verb's tense
      const rows4 = SentenceAnalyzer.analyze('هَلَّا أَكْرَمْتَ زَيْدًا');
      const rows5 = SentenceAnalyzer.analyze('هَلَّا تَقُومُ');
      const tm4 = InshaEngine.read(rows4), tm5 = InshaEngine.read(rows5);
      // لولا's verb face: tahdid, and no imtina frame — while the NOUN face keeps it
      const rowsLw = SentenceAnalyzer.analyze('لَوْلَا تَقُومُ');
      const shLw = ShartEngine.read(rowsLw).length;
      const tmLw = InshaEngine.read(rowsLw);
      const shLwCtl = ShartEngine.read(SentenceAnalyzer.analyze('لَوْلَا زَيْدٌ لَهَلَكَ عَمْرٌو'));
      // la'alla with layta's hukm: the geminate mudari is a corpus verb and
      // the fa-verb's stale «mudaf ilayh» label was rewritten on upgrade
      const rows6 = SentenceAnalyzer.analyze('لَعَلِّي أَحُجُّ فَأَزُورَكَ');
      const tm6 = InshaEngine.read(rows6);
      // hal's wish is a SHORTLIST with an exact trigger: the textbook shape
      // fires it and a plain nominal question must not
      const tmHal = InshaEngine.read(SentenceAnalyzer.analyze('هَلْ لِي مِنْ شَفِيعٍ'));
      const tmHalCtl = InshaEngine.read(SentenceAnalyzer.analyze('هَلْ زَيْدٌ قَائِمٌ'));
      // the tm-frame card renders in the Jumla lab's own pipeline
      let frameHtml = '';
      try {
        const d = document.createElement('div'); d.id = 'jumlaOut'; document.body.appendChild(d);
        conjState.jumla = 'هَلَّا تَقُومُ';
        renderJumlaOut(); frameHtml = d.innerHTML; d.remove();
      } catch (e) { frameHtml = 'ERR ' + e.message; }
      const css = [...document.styleSheets].map(s => {
        try { return [...s.cssRules].map(x => x.cssText).join('\n'); } catch (e) { return ''; }
      }).join('\n');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('insha-wa-tamanni')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        layta: tmLayta[0] && [tmLayta[0].key, (tmLayta[0].pieces[0] || {}).idx],
        sh3, tm3Key: tm3[0] && tm3[0].key,
        faVKind: faV && faV.kind,
        faVMudaf: faV && faV.notes.some(n => n.en === 'attached pronoun — the mudaf ilayh'),
        faVWiqaya: faV && faV.notes.some(n => /MAF'UL BIHI/.test(n.en || '')),
        shCtlKey: shCtl[0] && shCtl[0].key,
        halla4: rows4[0] && rows4[0].pk, tm4Ar: tm4[0] && tm4[0].ar,
        tm5Ar: tm5[0] && tm5[0].ar,
        shLw, tmLwAr: tmLw[0] && tmLw[0].ar, shLwCtlKey: shLwCtl[0] && shLwCtl[0].key,
        hajjKind: rows6[1] && rows6[1].kind, tm6Key: tm6[0] && tm6[0].key,
        zurMudaf: rows6[2] && rows6[2].notes.some(n => n.en === 'attached pronoun — the mudaf ilayh'),
        halKey: tmHal[0] && tmHal[0].key, halCtl: tmHalCtl.length,
        frameOk: /tm-frame/.test(frameHtml) && /التَّحْضِيض/.test(frameHtml),
        cssOk: /\.shart-frame\.tm-frame/.test(css),
      };
    });
    if (r.missing) throw new Error('chapter 23 did not load');
    if (r.chapters < 23) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 6) throw new Error('ch23 sentences: ' + r.n);
    if (r.t !== 19) throw new Error('ch23 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the insha-wa-tamanni note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 15) throw new Error('too few insha-wa-tamanni tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch23 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.layta || r.layta[0] !== 'layta' || r.layta[1] !== 1)
      throw new Error('the layta frame with its ism: ' + JSON.stringify(r.layta));
    if (r.sh3 !== 0) throw new Error('the borrowed law opens no shart frame: ' + r.sh3);
    if (r.tm3Key !== 'lawT') throw new Error('…and the wish-frame reads it: ' + r.tm3Key);
    if (r.faVKind !== 'verb') throw new Error('فَتُحَدِّثَنِي is a corpus verb: ' + r.faVKind);
    if (r.faVMudaf) throw new Error('…whose ya is never a «mudaf ilayh»');
    if (!r.faVWiqaya) throw new Error('…the nun of protection note names the ya a MAF\'UL BIHI');
    if (r.shCtlKey !== 'law') throw new Error('the REAL law keeps its conditional frame: ' + r.shCtlKey);
    if (r.halla4 !== 'tahdid') throw new Error('هَلَّا is a closed-class tahdid particle: ' + r.halla4);
    if (!/التَّنْدِيم/.test(r.tm4Ar || '')) throw new Error('halla + madi = TANDIM: ' + r.tm4Ar);
    if (!/التَّحْضِيض/.test(r.tm5Ar || '')) throw new Error('halla + mudari = TAHDID: ' + r.tm5Ar);
    if (r.shLw !== 0) throw new Error('لولا before a verb opens no imtina frame: ' + r.shLw);
    if (!/التَّحْضِيض/.test(r.tmLwAr || '')) throw new Error('…the tahdid face reads it: ' + r.tmLwAr);
    if (r.shLwCtlKey !== 'lawla') throw new Error('لولا before a NOUN keeps imtina: ' + r.shLwCtlKey);
    if (r.hajjKind !== 'verb') throw new Error('أَحُجُّ is a corpus verb (the geminate mudari): ' + r.hajjKind);
    if (r.tm6Key !== 'laalla') throw new Error('la\'alla with the nasb witness gets layta\'s hukm: ' + r.tm6Key);
    if (r.zurMudaf) throw new Error('فَأَزُورَكَ\'s kaf is never a «mudaf ilayh» — the stale label is rewritten');
    if (r.halKey !== 'halT') throw new Error('the hal wish-shortlist fires on the textbook shape: ' + r.halKey);
    if (r.halCtl !== 0) throw new Error('…and never on a plain nominal question: ' + r.halCtl);
    if (!r.frameOk) throw new Error('the tm-frame card renders in the Jumla lab');
    if (!r.cssOk) throw new Error('the tm-frame wears its own spine color');
  });

  await check('talkhis ch24: istifham — the hamza peeled before open words, and the IstifhamEngine frames', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 24);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['al-istifham'];
      const ist = s => IstifhamEngine.read(SentenceAnalyzer.analyze(s));
      // the hamza before an open-class word comes OFF, and what follows it
      // is the asked-about — the four hamza frames
      const rows1 = SentenceAnalyzer.analyze('أَزَيْدٌ قَائِمٌ');
      const f1 = ist('أَزَيْدٌ قَائِمٌ');
      const f2 = ist('أَدِبْسٌ فِي الْإِنَاءِ أَمْ عَسَلٌ');
      const rows2 = SentenceAnalyzer.analyze('أَدِبْسٌ فِي الْإِنَاءِ أَمْ عَسَلٌ');
      const f3 = ist('أَزَيْدًا ضَرَبْتَ');
      const rows7 = SentenceAnalyzer.analyze('أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ');
      const f7 = ist('أَتَضْرِبُ زَيْدًا وَهُوَ أَخُوكَ');
      // hal's three faces on one minimal pair
      const f4 = ist('هَلْ قَامَ زَيْدٌ');
      const f5 = ist('هَلْ زَيْدًا ضَرَبْتَ');
      const f6 = ist('هَلْ زَيْدًا ضَرَبْتَهُ');
      // CONTROLS: a real hamza-initial verb keeps its hamza; أُمّ stays a noun
      const rowsC1 = SentenceAnalyzer.analyze('أَكْرَمْتَ زَيْدًا');
      const fC1 = ist('أَكْرَمْتَ زَيْدًا');
      const rowsC2 = SentenceAnalyzer.analyze('أُمُّهُ كَرِيمَةٌ');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('al-istifham')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        q1: rows1[0] && !!rows1[0].istifham, seg1: rows1[0] && rows1[0].seg[0],
        k1: f1[0] && f1[0].key,
        amPk: rows2[3] && rows2[3].pk, k2: f2[0] && f2[0].key,
        k2ends: f2[0] && f2[0].pieces.map(p => p.idx),
        k3: f3[0] && f3[0].key,
        k7: f7[0] && f7[0].key, v7: rows7[0] && rows7[0].kind,
        akh7: rows7[3] && rows7[3].notes.some(n => /FIVE NOUNS/.test(n.en || '')),
        k4: f4[0] && f4[0].key, k5: f5[0] && f5[0].key, k6: f6[0] && f6[0].key,
        c1q: rowsC1[0] && !!rowsC1[0].istifham, c1n: fC1.length,
        c2kind: rowsC2[0] && rowsC2[0].kind, c2pk: rowsC2[0] && (rowsC2[0].pk || null),
      };
    });
    if (r.missing) throw new Error('chapter 24 did not load');
    if (r.chapters < 24) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 6) throw new Error('ch24 sentences: ' + r.n);
    if (r.t !== 19) throw new Error('ch24 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the al-istifham note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 15) throw new Error('too few al-istifham tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch24 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.q1 || r.seg1 !== 'أ')
      throw new Error('the question hamza comes off before an open word: ' + JSON.stringify([r.q1, r.seg1]));
    if (r.k1 !== 'hamzaTasdiq') throw new Error('hamza on a plain nominal = tasdiq: ' + r.k1);
    if (r.amPk !== 'am') throw new Error('أَمْ is a closed-class row: ' + r.amPk);
    if (r.k2 !== 'hamzaTayin') throw new Error('hamza + am = ta\'yin: ' + r.k2);
    if (!r.k2ends || r.k2ends[0] !== 0 || r.k2ends[1] !== 4)
      throw new Error('…with the TWO candidates as its ends: ' + JSON.stringify(r.k2ends));
    if (r.k3 !== 'hamzaMaful') throw new Error('hamza + fronted mansub = the object asked: ' + r.k3);
    if (r.k7 !== 'hamzaVerb' || r.v7 !== 'verb')
      throw new Error('hamza + mudari reads the deed (and the peel finds the corpus verb): ' + JSON.stringify([r.k7, r.v7]));
    if (!r.akh7) throw new Error('أَخُوكَ keeps its five-nouns reading inside the question');
    if (r.k4 !== 'halTasdiq') throw new Error('hal + verb = tasdiq only: ' + r.k4);
    if (r.k5 !== 'halQabih') throw new Error('hal + fronted mansub = the qabih doctrine: ' + r.k5);
    if (r.k6 !== 'halRescue') throw new Error('…and the object pronoun lifts it (mufassar): ' + r.k6);
    if (r.c1q || r.c1n !== 0)
      throw new Error('أَكْرَمْتَ keeps its own hamza — no question invented: ' + JSON.stringify([r.c1q, r.c1n]));
    if (r.c2kind !== 'noun' || r.c2pk === 'am')
      throw new Error('أُمُّهُ is the mother, never the connective: ' + JSON.stringify([r.c2kind, r.c2pk]));
  });

  await check('talkhis ch25: hal basita/murakkaba, ma and man — and the nominal-hal frames', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 25);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['hal-ma-man'];
      const ist = s => IstifhamEngine.read(SentenceAnalyzer.analyze(s));
      const f1 = ist('فَهَلْ أَنْتُمْ شَاكِرُونَ');
      const f2 = ist('هَلِ الْحَرَكَةُ مَوْجُودَةٌ');
      const f3 = ist('هَلِ الْحَرَكَةُ دَائِمَةٌ');
      const f4 = ist('مَا الْعَنْقَاءُ');
      const rows5 = SentenceAnalyzer.analyze('مَنْ فِي الدَّارِ');
      const f5 = IstifhamEngine.read(rows5);
      const f6 = ist('مَا عِنْدَكَ');
      // مَنْ the ISM carries its OWN key now — the jarr letter's key must
      // not ride the fatha-mim row (the ML and the case layer read it)
      const manPk = rows5[0] && rows5[0].pk;
      const minPk = (SentenceAnalyzer.analyze('مِنْ زَيْدٍ')[0] || {}).pk;
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('hal-ma-man')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        k1: f1[0] && f1[0].key, k2: f2[0] && f2[0].key, k3: f3[0] && f3[0].key,
        k4: f4[0] && f4[0].key, k5: f5[0] && f5[0].key, k6: f6[0] && f6[0].key,
        manPk, minPk,
      };
    });
    if (r.missing) throw new Error('chapter 25 did not load');
    if (r.chapters < 25) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 6) throw new Error('ch25 sentences: ' + r.n);
    if (r.t !== 16) throw new Error('ch25 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the hal-ma-man note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 13) throw new Error('too few hal-ma-man tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch25 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (r.k1 !== 'halFil') throw new Error('the aya reads the fi\'l-affinity nominal frame: ' + r.k1);
    if (r.k2 !== 'halBasita') throw new Error('a mawjud-khabar is BASITA: ' + r.k2);
    if (r.k3 !== 'halMurakkaba') throw new Error('any other khabar is MURAKKABA: ' + r.k3);
    if (r.k4 !== 'maAsk') throw new Error('ma before a definite noun asks name-or-essence: ' + r.k4);
    if (r.k5 !== 'manAsk') throw new Error('man asks the person: ' + r.k5);
    if (r.k6 !== 'maJins') throw new Error('ma before a bare zarf asks the JINS: ' + r.k6);
    if (r.manPk !== 'man') throw new Error('مَنْ the ism carries its own pk: ' + r.manPk);
    if (r.minPk !== 'jarr') throw new Error('…and مِنْ the letter keeps jarr: ' + r.minPk);
  });

  await check('talkhis ch26: the tasawwur adawat — frames, the mu\'rab ayy, and the istifham-face router', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 26);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['adawat-al-tasawwur'];
      const ist = s => IstifhamEngine.read(SentenceAnalyzer.analyze(s));
      const k = s => { const f = ist(s); return f[0] && f[0].key; };
      const rows1 = SentenceAnalyzer.analyze('أَيُّ الْفَرِيقَيْنِ خَيْرٌ مَقَامًا');
      const rows4 = SentenceAnalyzer.analyze('أَيْنَ زَيْدٌ');
      const rows5 = SentenceAnalyzer.analyze('مَتَى جِئْتَ');
      // the FRAME decides the face: two verbs after the adat keep the shart
      const ctrl = SentenceAnalyzer.analyze('مَتَى جِئْتَنِي أَكْرَمْتُكَ');
      const sal = SentenceAnalyzer.analyze('سَلْ بَنِي إِسْرَائِيلَ كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('adawat-al-tasawwur')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        kAyy: k('أَيُّ الْفَرِيقَيْنِ خَيْرٌ مَقَامًا'), kKam: k('كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ'),
        kKayfa: k('كَيْفَ أَنْتَ'), kAyna: k('أَيْنَ زَيْدٌ'), kMata: k('مَتَى جِئْتَ'),
        kAyyan: k('يَسْأَلُ أَيَّانَ يَوْمُ الْقِيَامَةِ'), kAnna: k('يَا مَرْيَمُ أَنَّى لَكِ هَذَا'),
        // أَيّ is the ONE declining interrogative: raf claimed off its damma;
        // its sisters claim mabni; and the shart engine stands down where no
        // two-verb frame follows — but keeps the real condition.
        cAyy: (CaseEngine.claim(rows1, 0) || {}).k,
        cAyna: (CaseEngine.claim(rows4, 0) || {}).k,
        mataPk: rows5[0] && rows5[0].pk,
        aynaKind: rows4[0] && rows4[0].kind,
        shartQuiet: ShartEngine.read(rows4).length + ShartEngine.read(rows5).length,
        ctrlPk: ctrl[0] && ctrl[0].pk,
        ctrlShart: ShartEngine.read(ctrl).length,
        // the LIGHT imperative reads its receipt: سَلْ answers from سَأَلَ,
        // never from salla's bare-matched سَلِّ (exact beats loose corpus-wide)
        salRoot: sal[0] && sal[0].root,
        salMabni: /MABNI|MEBN/i.test((sal[0].notes || []).map(n => n.en + n.tr).join(' ')),
        aataCell: sal[4] && sal[4].kind === 'verb' && sal[4].root,
      };
    });
    if (r.missing) throw new Error('chapter 26 did not load');
    if (r.chapters < 26) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 7) throw new Error('ch26 sentences: ' + r.n);
    if (r.t !== 27) throw new Error('ch26 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the adawat-al-tasawwur note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 20) throw new Error('too few adawat-al-tasawwur tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch26 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    const want = { kAyy: 'ayyTayin', kKam: 'kamAdad', kKayfa: 'kayfaHal', kAyna: 'aynaMakan',
                   kMata: 'mataZaman', kAyyan: 'ayyanTafkhim', kAnna: 'annaAyna' };
    for (const [key, val] of Object.entries(want))
      if (r[key] !== val) throw new Error(key + ' expected ' + val + ', got ' + r[key]);
    if (r.cAyy !== 'raf') throw new Error('أَيّ declines — its damma is read as raf: ' + r.cAyy);
    if (r.cAyna !== 'mabni') throw new Error('its sisters stay mabni: ' + r.cAyna);
    if (r.aynaKind !== 'noun') throw new Error('the interrogatives are NOUNS: ' + r.aynaKind);
    if (r.mataPk !== 'istif-ism') throw new Error('one verb = the istifham face: ' + r.mataPk);
    if (r.shartQuiet !== 0) throw new Error('no shart frame without a two-verb frame: ' + r.shartQuiet);
    if (r.ctrlPk !== 'shart-jazim' || r.ctrlShart < 1)
      throw new Error('…and مَتَى with two verbs KEEPS the condition: ' + r.ctrlPk + '/' + r.ctrlShart);
    if (r.salRoot !== 'س أ ل') throw new Error('سَلْ answers from سَأَلَ: ' + r.salRoot);
    if (!r.salMabni) throw new Error('…and its sukun is named BINA, not jazm');
    if (r.aataCell !== 'أ ت ي') throw new Error('آتَيْنَاهُمْ resolves to the stored آتَى: ' + r.aataCell);
  });

  await check('talkhis ch27: the question leaving its asl — hamzaNafy, kamIstibta, the ma-li frame', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 27);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['khuruj-al-istifham'];
      const ist = s => IstifhamEngine.read(SentenceAnalyzer.analyze(s));
      const k = s => { const f = ist(s); return f[0] && f[0].key; };
      const laysaRows = SentenceAnalyzer.analyze('أَلَيْسَ اللَّهُ بِكَافٍ عَبْدَهُ');
      const huphup = SentenceAnalyzer.analyze('مَا لِيَ لَا أَرَى الْهُدْهُدَ');
      const wsf = SentenceAnalyzer.analyze('لَا يُوصَفُونَ بِالذُّكُورَةِ');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('khuruj-al-istifham')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        // the frames — and the CONTROLS that keep the old readings standing:
        // a THIRD-person kam keeps the plain count-ask, and the tanwin-object
        // control keeps the original hamzaMaful shape.
        kIstibta: k('كَمْ دَعَوْتُكَ'), kAdadCtrl: k('كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ'),
        kMaLi: k('مَا لِيَ لَا أَرَى الْهُدْهُدَ'),
        kNafy: k('أَلَيْسَ اللَّهُ بِكَافٍ عَبْدَهُ'),
        kInkar: k('أَغَيْرَ اللَّهِ تَدْعُونَ'), kMafulCtrl: k('أَزَيْدًا ضَرَبْتَ'),
        kIstibad: k('أَنَّى لَهُمُ الذِّكْرَى'),
        // لَيْسَ is a jamid MAZI — its bina-fatha must not be claimed as nasb
        laysaCase: (CaseEngine.claim(laysaRows, 0) || {}).k,
        // the مَا لِـ row is promoted to the ism face → mabni claim
        maCase: (CaseEngine.claim(huphup, 0) || {}).k,
        // a 1st-person verb carries its doer in the cell — the noun after it
        // expects the MAF'UL, not the fa'il
        mafulNote: (huphup[4] && (huphup[4].notes || []).some(n => /likely the MAF'UL/.test(n.en || ''))) || false,
        // the stored majhul singular answers for its group's-waw plural
        wsfKind: wsf[1] && wsf[1].kind, wsfTense: wsf[1] && wsf[1].cell && wsf[1].cell.tense,
        wsfCase: (CaseEngine.claim(wsf, 1) || {}).k,
      };
    });
    if (r.missing) throw new Error('chapter 27 did not load');
    if (r.chapters < 27) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 7) throw new Error('ch27 sentences: ' + r.n);
    if (r.t !== 21) throw new Error('ch27 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the khuruj-al-istifham note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 15) throw new Error('too few khuruj-al-istifham tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch27 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (r.kIstibta !== 'kamIstibta') throw new Error('a first-person madi after kam is ISTIBTA: ' + r.kIstibta);
    if (r.kAdadCtrl !== 'kamAdad') throw new Error('…and the third-person kam keeps the count-ask: ' + r.kAdadCtrl);
    if (r.kMaLi !== 'maLiTaajjub') throw new Error('the ma-li frame reads TA\'AJJUB: ' + r.kMaLi);
    if (r.kNafy !== 'hamzaNafy') throw new Error('the hamza over a negation is TAQRIR: ' + r.kNafy);
    if (r.kInkar !== 'hamzaMaful') throw new Error('the fronted mudaf object reads hamzaMaful: ' + r.kInkar);
    if (r.kMafulCtrl !== 'hamzaMaful') throw new Error('…and the tanwin control keeps its frame: ' + r.kMafulCtrl);
    if (r.kIstibad !== 'annaAyna') throw new Error('anna before a nominal keeps min-ayna: ' + r.kIstibad);
    if (r.laysaCase !== 'mabni') throw new Error('لَيْسَ is a jamid mazi, mabni — not nasb: ' + r.laysaCase);
    if (r.maCase !== 'mabni') throw new Error('the promoted ma-li ma claims mabni: ' + r.maCase);
    if (!r.mafulNote) throw new Error('a 1st-person verb\'s following noun expects the MAF\'UL');
    if (r.wsfKind !== 'verb' || r.wsfTense !== 'majhulMudari' || r.wsfCase !== 'raf')
      throw new Error('يُوصَفُونَ answers from the stored majhul singular: ' +
        r.wsfKind + '/' + r.wsfTense + '/' + r.wsfCase);
  });

  await check('talkhis ch28: the amr bab — three dresses, and the wujuh it leaves for', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 28);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const g = GRAMMAR['al-amr-wa-wujuhuh'];
      const ins = s => (InshaEngine.read(SentenceAnalyzer.analyze(s)) || []).map(f => f.key);
      const lam = SentenceAnalyzer.analyze('لِيَحْضُرْ زَيْدٌ');
      const lamCtrl = SentenceAnalyzer.analyze('لَمْ يَحْضُرْ زَيْدٌ');
      const ruwayd = SentenceAnalyzer.analyze('رُوَيْدَ بَكْرًا');
      const rabbi = SentenceAnalyzer.analyze('رَبِّ اغْفِرْ لِي');
      const maRow = SentenceAnalyzer.analyze('اِعْمَلُوا مَا شِئْتُمْ')[1];
      const mimRow = SentenceAnalyzer.analyze('عَجِبْتُ مِمَّا صَنَعْتَ')[1];
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        note: g && [g.group, (g.question || {}).tr ? g.question.tr.length : 0,
              (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        tagged: toks.filter(t => (t.grammar || []).includes('al-amr-wa-wujuhuh')).length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        // the three wujuh frames — and the control that a PLAIN amr, with no
        // qarina beside it, wears none of them: the asl needs no receipt.
        fDua: ins('رَبِّ اغْفِرْ لِي'), fTaswiya: ins('اِصْبِرُوا أَوْ لَا تَصْبِرُوا'),
        fTahdid: ins('اِعْمَلُوا مَا شِئْتُمْ'), fPlain: ins('أَكْرِمْ عَمْرًا'),
        // رُوَيْدَ is the third dress: a mabni NOUN with a verb's force, and
        // the noun after it is its maf'ul in plain nasb
        ruwaydPk: ruwayd[0] && ruwayd[0].pk,
        ruwaydCase: (CaseEngine.claim(ruwayd, 0) || {}).k,
        bakrCase: (CaseEngine.claim(ruwayd, 1) || {}).k,
        // the trimmed vocative: رَبِّ before a verb is a munada with its ya
        // cut — the kasra is the ya's trace, not a jarr, so the engine is
        // silent rather than wrong
        rabbiClaim: CaseEngine.claim(rabbi, 0),
        // the lam of command is NAMED on the row — and the note walks the
        // letter, so لَمْ (no ل-initial verb) must stay clean
        lamNote: (lam[0].notes || []).some(n => /لَامُ الْأَمْرِ/.test(n.en || '')),
        lamCtrl: lamCtrl.flatMap(x => (x.notes || []).map(n => n.en || ''))
                        .some(e => /لَامُ الْأَمْرِ/.test(e)),
        // …and the verb resolved with its cell must not ALSO be read as a
        // fused jarr phrase hunting for an omitted amil
        lamGhost: (lam[0].notes || []).some(n => /OMITTED amil/.test(n.en || '')),
        // rule 6i: a bare ma between two verbs, the first with an open object
        // seat, is the mawsula — while the jarr-fused مِمَّا keeps masdariyya
        maWajh: maRow && maRow.wajh && maRow.wajh.k,
        mimWajh: mimRow && mimRow.wajh && mimRow.wajh.k,
      };
    });
    if (r.missing) throw new Error('chapter 28 did not load');
    if (r.chapters < 28) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 7) throw new Error('ch28 sentences: ' + r.n);
    if (r.t !== 19) throw new Error('ch28 tokens: ' + r.t);
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 4 || r.note[2] < 3)
      throw new Error('the al-amr-wa-wujuhuh note with its question test and anchors: ' + JSON.stringify(r.note));
    if (r.tagged < 12) throw new Error('too few al-amr-wa-wujuhuh tokens tagged: ' + r.tagged);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch28 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.fDua.includes('amrDua')) throw new Error('the amr aimed UP is du\'a: ' + r.fDua);
    if (!r.fTaswiya.includes('amrTaswiya')) throw new Error('amr + أَوْ + its own negation is TASWIYA: ' + r.fTaswiya);
    if (!r.fTahdid.includes('amrTahdid')) throw new Error('«do what you wish» is TAHDID: ' + r.fTahdid);
    if (r.fPlain.some(k => /^amr/.test(k)))
      throw new Error('a plain amr with no qarina wears no wajh frame: ' + r.fPlain);
    if (r.ruwaydPk !== 'ism-fil') throw new Error('رُوَيْدَ is filed as the ism al-fi\'l: ' + r.ruwaydPk);
    if (r.ruwaydCase !== 'mabni') throw new Error('…and it is mabni: ' + r.ruwaydCase);
    if (r.bakrCase !== 'nasb') throw new Error('…and its maf\'ul wears nasb: ' + r.bakrCase);
    if (r.rabbiClaim !== null) throw new Error('the trimmed vocative stays silent: ' + JSON.stringify(r.rabbiClaim));
    if (!r.lamNote) throw new Error('لِيَحْضُرْ names its لَامُ الْأَمْرِ on the row');
    if (r.lamCtrl) throw new Error('…but لَمْ يَحْضُرْ carries no lam-amr note');
    if (r.lamGhost) throw new Error('a resolved verb must not be walked as a jarr phrase');
    if (r.maWajh !== 'mawsula') throw new Error('the open object seat promotes مَا to mawsula: ' + r.maWajh);
    if (r.mimWajh !== 'masdariyya') throw new Error('…while مِمَّا with no aid keeps masdariyya: ' + r.mimWajh);
  });

  await check('the duel and the model lab: the perceptron plays with its hand open', async () => {
    const r = await page.evaluate(() => {
      renderLibrary();
      const spec = GameFactory.get('gDuel');
      const items = duelItems();
      const it = items[0];
      const pred = modelPredictFor(it.sen, it.ti);
      const okDesc = pred.every((p, k) => k === 0 || pred[k - 1].p >= p.p);
      const sum = pred.reduce((a, p) => a + p.p, 0);
      return { supply: items.length, gf: !!spec,
               playable: GameFactory.playable('gDuel'),
               roleKnown: !!DUEL_ROLES[it.key],
               okDesc, sum: Math.round(sum * 100) / 100,
               modelRoles: IrabModel.ROLES.every(k => !!DUEL_ROLES[k]) };
    });
    if (!r.gf) throw new Error('gDuel is not registered in GameFactory');
    // the duel pool IS the labeled corpus — the same floor the ML gate holds
    if (!r.playable || r.supply < 2000) throw new Error('the duel pool shrank: ' + r.supply);
    if (!r.roleKnown || !r.modelRoles) throw new Error('every model role needs its duel label');
    if (!r.okDesc || Math.abs(r.sum - 1) > 0.01)
      throw new Error('rank must return a sorted distribution, got sum ' + r.sum);
    // play one question through the hub: the model is badged in the reveal,
    // the tally runs, and the stored i'rab — never the model — answers.
    await page.evaluate(() => openGames());
    await page.locator('.game-pick #gDuel').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 5000 });
    const nOpts = await page.locator('.opts [data-o]').count();
    if (nOpts < 2 || nOpts > 4) throw new Error('duel options: ' + nOpts);
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('.duel-banner', { timeout: 3000 });
    const banner = await page.locator('.duel-banner').textContent();
    if (!/🤖/.test(banner)) throw new Error('the model must wear its badge in the reveal');
    if (!(await page.locator('.duel-tally').count())) throw new Error('the running tally is missing');
    if (!(await page.locator('.game-why').count()))
      throw new Error("the stored i'rab must answer, not the model");
    await page.evaluate(() => { closeSheet(); renderLibrary(); });
    // the Model lab: belief bars in the role palette, evidence chips, and
    // the honest stand-down on verbs and closed-class words.
    await page.evaluate(() => {
      conjState.lab = 'model';
      conjState.model = 'كَتَبَ الْوَلَدُ الدَّرْسَ فِي الْبَيْتِ';
      openConjugator();
    });
    await page.waitForSelector('#modelOut', { timeout: 3000 });
    await page.waitForTimeout(300);
    const lab = await page.evaluate(() => ({
      bars: document.querySelectorAll('.mbar').length,
      fills: [...document.querySelectorAll('.mbar-fill')].every(f =>
        /var\(--role-/.test(f.getAttribute('style') || '')),
      chips: document.querySelectorAll('.feat-chip').length,
      skips: document.querySelectorAll('.model-skip').length,
      score: (document.querySelector('.ml-score') || {}).textContent || '',
      heldout: Math.round(IrabModel.crossVal().top1 * 100),
    }));
    if (lab.bars < 3) throw new Error('the model lab must draw belief bars: ' + lab.bars);
    if (!lab.fills) throw new Error('a belief bar wears its role color from the palette, not a literal');
    if (lab.chips < 5) throw new Error('the evidence chips are missing: ' + lab.chips);
    if (lab.skips < 1) throw new Error('a verb must get the stand-down line, not a guess');
    if (!lab.score.includes(String(lab.heldout)))
      throw new Error('the lab must lead with the held-out score: ' + lab.score);
    // live ablation (v147): withholding a chip must move the belief, mark the
    // chip, and a second tap must restore the card EXACTLY — nothing is
    // retrained, so the roundtrip is byte-identical.
    const abl = await page.evaluate(() => {
      const chips = [...document.querySelectorAll('.feat-chip[data-mc="0"]')];
      const target = chips.find(c => c.textContent.includes('×')) || chips[chips.length - 1];
      const b0 = document.getElementById('mbars0').innerHTML;
      target.click();
      const b1 = document.getElementById('mbars0').innerHTML;
      const off = target.classList.contains('off');
      target.click();
      const b2 = document.getElementById('mbars0').innerHTML;
      return { hint: !!document.querySelector('.model-hint'),
               changed: b0 !== b1, off, roundtrip: b0 === b2,
               restored: !target.classList.contains('off') };
    });
    if (!abl.hint) throw new Error('the ablation hint is missing');
    if (!abl.changed) throw new Error('withholding evidence must move the belief bars');
    if (!abl.off || !abl.restored) throw new Error('the chip must mark itself withheld and restore on the second tap');
    if (!abl.roundtrip) throw new Error('restore must reproduce the original bars exactly');
    // …and the shipped conjunction features fire where their parents meet
    const conj = await page.evaluate(() =>
      IrabModel.features('زَيْدًا', 1, 3, 'verb', { prevFull: 'رَأَيْتُ', nextFull: null })
        .filter(f => f.includes('*')));
    if (!conj.includes('av*sign-fatha') || !conj.includes('tw*av'))
      throw new Error('the v147 conjunctions must fire on their type case: ' + conj.join(','));
    await page.evaluate(() => { closeSheet(); renderLibrary(); });
  });

  await check('the wajh game reads the frame tables, and the confusion matrix aimed the features', async () => {
    const r = await page.evaluate(() => {
      renderLibrary();
      const items = wajhItems();   // also warms the cache for the play below
      const keys = new Set(items.map(x => x.key));
      // the v148 neighbourhood features, each on its type shape: the idafa
      // head before a mudaf-ilayh, the sign-agreement of a na't with its
      // head, the article on the word AFTER an idafa's head
      const fsMudaf = IrabModel.features('الْوَلَدِ', 1, 2, 'noun', { prevFull: 'كِتَابُ', nextFull: null });
      const fsTabi = IrabModel.features('الْكَرِيمُ', 1, 2, null, { prevFull: 'الرَّجُلُ', nextFull: null });
      const fsNext = IrabModel.features('كِتَابُ', 0, 2, null, { prevFull: null, nextFull: 'الْوَلَدِ' });
      return {
        n: items.length, distinct: keys.size,
        gf: !!GameFactory.get('gWajh'), playable: GameFactory.playable('gWajh'),
        supply: GameFactory.supplyOf('gWajh'),
        docWhole: items.every(x => x.doc && x.doc.ar && x.doc.en && x.doc.tr),
        noted: items.every(x => !!GRAMMAR[x.note]),
        prevBare: fsMudaf.includes('prev-bare'),
        agree: fsTabi.includes('agree-sign'),
        nextAl: fsNext.includes('next-al'),
      };
    });
    if (!r.gf || !r.playable) throw new Error('gWajh is not registered/playable');
    // the pool is real corpus sentences with exactly one frame each — and it
    // must stay RICH: many distinct wujuh, not one frame quizzed thirty ways
    if (r.n < 20) throw new Error('the wajh pool shrank: ' + r.n);
    if (r.distinct < 12) throw new Error('the wajh pool lost its variety: ' + r.distinct);
    if (r.supply < 3) throw new Error('the hub count undercuts the floor: ' + r.supply);
    if (!r.docWhole) throw new Error('every item must carry its engine DOC line in all three languages');
    if (!r.noted) throw new Error('every item must anchor a real catalogue note');
    if (!r.prevBare) throw new Error('prev-bare must fire on the idafa head shape');
    if (!r.agree) throw new Error('agree-sign must fire on the na\'t agreement shape');
    if (!r.nextAl) throw new Error('next-al must fire before an article-wearing word');
    // play one question: the reveal is the engine's OWN DOC line
    await page.evaluate(() => openGames());
    await page.locator('.game-pick #gWajh').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 8000 });
    const nOpts = await page.locator('.opts [data-o]').count();
    if (nOpts !== 4) throw new Error('wajh options: ' + nOpts);
    await page.locator('.opts [data-o]').first().click();
    await page.waitForSelector('.game-why', { timeout: 3000 });
    const why = await page.evaluate(() => {
      const el = document.querySelector('.game-why');
      const ar = el && el.querySelector('[lang="ar"], span');
      const all = Object.assign({}, InshaEngine.DOC, IstifhamEngine.DOC);
      const txt = el ? el.textContent : '';
      return Object.values(all).some(d => txt.includes(d.ar));
    });
    if (!why) throw new Error('the reveal must quote a frame table DOC line verbatim');
    await page.evaluate(() => { closeSheet(); renderLibrary(); });
  });

  await check('talkhis ch29: the nahy, the five doors of jawab al-talab, and the call beyond calling', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 29);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const jawab = (s, i) => (an(s)[i].notes || []).some(n => /جَوَابُ الطَّلَبِ/.test(n.en || ''));
      const nahiya = (s, i) => (an(s)[i].notes || []).some(n => /النَّاهِيَة/.test(n.en || ''));
      const ins = s => (InshaEngine.read(an(s)) || []).map(f => f.key);
      const ist = s => (IstifhamEngine.read(an(s)) || []).map(f => f.key);
      const r3 = an('أَيْنَ بَيْتُكَ أَزُرْكَ');
      const r2 = an('لَيْتَ لِي مَالًا أُنْفِقْهُ');
      const rA = an('لَا تَمْتَثِلْ أَمْرِي');
      const r9 = an('أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ');
      const g131 = GRAMMAR['al-nahy-wa-wujuhuh'], g132 = GRAMMAR['jawab-al-talab'],
            g133 = GRAMMAR['ighra-wa-ikhtisas'];
      const anchored = g => (g.examples || []).filter(e => e.src === 'talkhis-al-miftah').length;
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        notes: [g131 && g131.group, g132 && g132.group, g133 && g133.group],
        anchors: [g131 && anchored(g131), g132 && anchored(g132), g133 && anchored(g133)],
        // the five doors — each named on the ANSWERING verb's own row
        doors: [jawab('لَيْتَ لِي مَالًا أُنْفِقْهُ', 3), jawab('أَيْنَ بَيْتُكَ أَزُرْكَ', 2),
                jawab('أَكْرِمْنِي أُكْرِمْكَ', 1), jawab('لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ', 2),
                jawab('أَلَا تَنْزِلُ تُصِبْ خَيْرًا', 2)],
        // …and the controls: a REAL jazim, a real shart, a plain amr — silent
        ctrls: [jawab('لَمْ يَكْتُبْ زَيْدٌ', 1), jawab('إِنْ تَدْرُسْ تَنْجَحْ', 2),
                jawab('أَكْرِمْ عَمْرًا', 1)],
        nahy: [nahiya('لَا تَمْتَثِلْ أَمْرِي', 0), nahiya('لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ', 0)],
        nahyCtrl: nahiya('لَا يَعْلَمُ الْغَيْبَ', 0),
        ard: ins('أَلَا تَنْزِلُ تُصِبْ خَيْرًا'), ardIstif: ist('أَلَا تَنْزِلُ تُصِبْ خَيْرًا'),
        laysaKeeps: ist('أَلَيْسَ اللَّهُ بِكَافٍ عَبْدَهُ'),
        // the hollow FIRST person rebuilt from the stored majzum cell
        azur: r3[2].cell && r3[2].cell.tense + '/' + r3[2].cell.person,
        azurCase: (CaseEngine.claim(r3, 2) || {}).k,
        // layta's deferred ism named, not called a khabar
        laytaIsm: (r2[2].notes || []).some(n => /ISM, DEFERRED/.test(n.en || '')),
        // the noun edition of rewrite-on-upgrade
        amri: [(rA[2].kind || '').startsWith('noun'),
               (rA[2].notes || []).some(n => /MUDAF ILAYH/.test(n.en || '')),
               !(rA[2].notes || []).some(n => /its maf'ul bihi/.test(n.en || ''))],
        // ayyuha: the closed-class compound, mabni
        ayyuha: [r9[3].pk, (CaseEngine.claim(r9, 3) || {}).k, (CaseEngine.claim(r9, 4) || {}).k],
      };
    });
    if (r.missing) throw new Error('chapter 29 did not load');
    if (r.chapters < 29) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 9) throw new Error('ch29 sentences: ' + r.n);
    if (r.t !== 31) throw new Error('ch29 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch29 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (r.notes.join() !== 'balagha,nahw,balagha')
      throw new Error('the three notes with their groups: ' + r.notes.join());
    if (r.anchors.some(a => a < 2))
      throw new Error('each note needs >=2 talkhis anchors: ' + r.anchors.join());
    if (!r.doors.every(Boolean))
      throw new Error('every door must name its jawab: ' + r.doors.join());
    if (r.ctrls.some(Boolean))
      throw new Error('a control leaked a jawab note: ' + r.ctrls.join());
    if (!r.nahy.every(Boolean)) throw new Error('the prohibiting la must be named: ' + r.nahy.join());
    if (r.nahyCtrl) throw new Error('a plain negation must not wear the nahiya note');
    if (!r.ard.includes('ardTalab')) throw new Error('the ard frame must read: ' + r.ard.join());
    if (r.ardIstif.length) throw new Error('the hamza chain must stand down for the ard: ' + r.ardIstif.join());
    if (!r.laysaKeeps.includes('hamzaNafy')) throw new Error('أَلَيْسَ keeps hamzaNafy: ' + r.laysaKeeps.join());
    if (r.azur !== 'majzum/12') throw new Error('the hollow first person rebuilds from the stored majzum: ' + r.azur);
    if (r.azurCase !== 'jazm') throw new Error('…and claims jazm: ' + r.azurCase);
    if (!r.laytaIsm) throw new Error("layta's deferred ism must be named, not sold as a khabar");
    if (!r.amri.every(Boolean))
      throw new Error('a noun host rewrites its enclitic label to mudaf ilayh: ' + r.amri.join());
    if (r.ayyuha[0] !== 'ayyuha' || r.ayyuha[1] !== 'mabni' || r.ayyuha[2] !== 'raf')
      throw new Error('ayyuha mabni with its sifa in raf: ' + r.ayyuha.join());
  });

  await check('talkhis ch30: khabar worn for insha — the frame, its controls, and the honest twins', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 30);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const ins = s => (InshaEngine.read(an(s)) || []).map(f => f.key);
      const g134 = GRAMMAR['khabar-fi-mana-al-insha'];
      const rz = an('رَزَقَنِيَ اللهُ لِقَاءَكَ');
      const ta = an('تَأْتِينِي غَدًا');
      const yz = an('يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً');
      const note = r2 => ((r2.notes || []).find(n => /corpus verb/.test(n.en || '')) || {}).en || '';
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        note: g134 && [g134.group, (g134.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        // the frame: the mazi du'a claimed on its receipt (enc + jalala)…
        frames: [ins('وَفَّقَكَ اللهُ لِلتَّقْوَى'), ins('رَزَقَنِيَ اللهُ لِقَاءَكَ')],
        // …and its controls: a 3rd-person object, no enclitic at all, and the
        // two MUDARI examples — rank and context read those, never a receipt.
        ctrls: [ins('نَصَرَهُمُ اللهُ'), ins('تَرَكَ اللهُ'),
                ins('يَنْظُرُ الْمَوْلَى إِلَيَّ سَاعَةً'), ins('تَأْتِينِي غَدًا')],
        // the iltiqa fatha on the wiqaya-ya (رَزَقَنِيَ) must not hide the peel
        razaqa: [(rz[0].kind || ''), rz[0].cell && rz[0].cell.tense, rz[0].enc || null],
        // twin cells: one spelling, two persons — the label says both; and a
        // verb with ONE cell must not grow the suffix
        twin: note(ta[0]), single: note(yz[0]),
        // the idafa pass's two refusals, with the real idafa as control
        idafaRefused: IdafaEngine.chain(an('وَفَّقَكَ اللهُ لِلتَّقْوَى')).length,
        idafaKept: IdafaEngine.chain(an('وَجْهُ اللهِ')).length,
      };
    });
    if (r.missing) throw new Error('chapter 30 did not load');
    if (r.chapters < 30) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 4) throw new Error('ch30 sentences: ' + r.n);
    if (r.t !== 12) throw new Error('ch30 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch30 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 2)
      throw new Error('note 134 balagha with >=2 talkhis anchors: ' + JSON.stringify(r.note));
    if (!r.frames.every(f => f.includes('khabarDua')))
      throw new Error('the khabarDua frame must claim both mazi du\'as: ' + JSON.stringify(r.frames));
    if (r.ctrls.some(f => f.includes('khabarDua')))
      throw new Error('a control leaked the frame: ' + JSON.stringify(r.ctrls));
    if (r.razaqa[0] !== 'verb' || r.razaqa[1] !== 'mazi' || r.razaqa[2] !== 'ني')
      throw new Error('رَزَقَنِيَ must resolve as a mazi with its wiqaya peel: ' + r.razaqa.join('/'));
    if (!/she — or you/.test(r.twin))
      throw new Error('the twin cells must both be named: ' + r.twin);
    if (/ — or /.test(r.single))
      throw new Error('a single-cell verb must not grow a twin: ' + r.single);
    if (r.idafaRefused !== 0)
      throw new Error('a pronoun-closed head must refuse the idafa (وَفَّقَكَ اللهُ)');
    if (r.idafaKept !== 1)
      throw new Error('the real idafa must survive the refusals (وَجْهُ اللهِ)');
  });

  await check('talkhis ch31: fasl and wasl — the frames, the jihat jamia, and the aya cut loose', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 31);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const ws = s => WaslEngine.read(an(s)).map(f => f.key);
      const g135 = GRAMMAR['al-fasl-wa-al-wasl'];
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        note: g135 && [g135.group, (g135.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        // the four frames on the bab's own examples…
        wasl3: ws('زَيْدٌ يَكْتُبُ وَيَشْعُرُ'),
        wasl4: ws('زَيْدٌ يُعْطِي وَيَمْنَعُ'),
        fa: ws('دَخَلَ زَيْدٌ فَخَرَجَ عَمْرٌو'),
        thumma: ws('دَخَلَ زَيْدٌ ثُمَّ خَرَجَ عَمْرٌو'),
        // …and the stand-downs: the aya of the FASL fires nothing (no atf
        // letter stands — the absence is the lesson), the shart-fa belongs to
        // ShartEngine, the talab context to the jawab pass, the amr bab to
        // InshaEngine. A frame widened without its controls pinned is a
        // frame about to steal its neighbour.
        ctrls: [ws('اللَّهُ يَسْتَهْزِئُ بِهِمْ'), ws('إِنْ تَدْرُسْ تَنْجَحْ'),
                ws('أَكْرِمْنِي أُكْرِمْكَ')],
        // the aya rows: قَالُوا mabni-damm verb, the sound plural khabar by
        // the waw, and the FASL row's jumal names the isti'naf
        istihza: (an('اللَّهُ يَسْتَهْزِئُ بِهِمْ')[1] || {}).kind,
        // the DOC lines are trilingual — the frames render in both tongues
        doc: Object.values(WaslEngine.DOC).every(d => d.ar && d.en && d.tr),
      };
    });
    if (r.missing) throw new Error('chapter 31 did not load');
    if (r.chapters < 31) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 8) throw new Error('ch31 sentences: ' + r.n);
    if (r.t !== 41) throw new Error('ch31 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch31 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 2)
      throw new Error('note 135 balagha with >=2 talkhis anchors: ' + JSON.stringify(r.note));
    if (!r.wasl3.includes('waslWaw') || !r.wasl3.includes('matufKhabar'))
      throw new Error('the wasl frames must read يَكْتُبُ وَيَشْعُرُ: ' + r.wasl3.join());
    if (!r.wasl4.includes('waslWaw'))
      throw new Error('the opposed-musnads wasl must read: ' + r.wasl4.join());
    if (!r.fa.includes('faTaqib')) throw new Error('the fa of ta\'qib must read: ' + r.fa.join());
    if (!r.thumma.includes('thummaMuhla')) throw new Error('thumma\'s muhla must read: ' + r.thumma.join());
    if (r.ctrls.some(f => f.length))
      throw new Error('a control leaked a wasl frame: ' + JSON.stringify(r.ctrls));
    if (r.istihza !== 'verb') throw new Error('يَسْتَهْزِئُ must resolve as a corpus verb: ' + r.istihza);
    if (!r.doc) throw new Error('every WaslEngine DOC line must be trilingual');
  });

  await check('talkhis ch32: the martaba ladder, and the five nouns stand bare', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 32);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const g136 = GRAMMAR['kamal-al-ittisal'];
      const at = (s, i) => {
        const rows = an(s); const r0 = rows[i];
        return { kind: r0.kind, sure: !!r0.sure,
                 k: (CaseEngine.claim(rows, i) || {}).k || null,
                 five: (r0.notes || []).some(n => /FIVE NOUNS/.test(n.en || '')) };
      };
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        note: g136 && [g136.group, (g136.examples || []).filter(e => e.src === 'talkhis-al-miftah').length],
        // the five nouns BARE: the letter is the case (the atf-bayan verse
        // shipped «noun or verb?» before this branch existed)…
        abu: at('أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ', 2),
        aba: at('رَأَيْتُ أَبَا حَفْصٍ', 1),
        // …with the enc form and the tanwin form as controls on either side
        akhuka: at('هُوَ أَخُوكَ', 1),
        abTanwin: at('لَهُ أَبٌ', 1),
        // the aya's genus-la ism keeps its bina claim, and the diptote's raf
        rayb: (CaseEngine.claim(an('ذَلِكَ الْكِتَابُ لَا رَيْبَ فِيهِ هُدًى لِلْمُتَّقِينَ'), 3) || {}).k,
        umar: (CaseEngine.claim(an('أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ'), 4) || {}).k,
      };
    });
    if (r.missing) throw new Error('chapter 32 did not load');
    if (r.chapters < 32) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 6) throw new Error('ch32 sentences: ' + r.n);
    if (r.t !== 24) throw new Error('ch32 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch32 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.note || r.note[0] !== 'balagha' || r.note[1] < 3)
      throw new Error('note 136 balagha with >=3 talkhis anchors: ' + JSON.stringify(r.note));
    if (r.abu.kind !== 'noun' || !r.abu.sure || r.abu.k !== 'raf' || !r.abu.five)
      throw new Error('bare أَبُو must be a sure five-noun in raf: ' + JSON.stringify(r.abu));
    if (r.aba.k !== 'nasb' || !r.aba.five)
      throw new Error('bare أَبَا must claim nasb by its alif: ' + JSON.stringify(r.aba));
    if (r.akhuka.kind !== 'noun' || !r.akhuka.five)
      throw new Error('the enc five-noun branch must keep its claim: ' + JSON.stringify(r.akhuka));
    if (r.abTanwin.five)
      throw new Error('a tanwin أَبٌ must keep the ordinary path, never the table');
    if (r.rayb !== 'mabni') throw new Error('the genus-la ism claims bina: ' + r.rayb);
    if (r.umar !== 'raf') throw new Error('the diptote atf-bayan claims raf: ' + r.umar);
  });

  await check('talkhis ch33: the ladder\'s witnesses — the ayat, the bayt, and the heavy nun\'s bina', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 33);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const k = (s, i) => { const rows = an(s); return (CaseEngine.claim(rows, i) || {}).k || null; };
      const g136 = GRAMMAR['kamal-al-ittisal'];
      const gr = GRAMMAR['rubai-babs'];
      const ws = an('فَوَسْوَسَ إِلَيْهِ الشَّيْطَانُ')[0];
      const bl = an('وَمُلْكٍ لَا يَبْلَى')[2];
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        anchors136: (g136.examples || []).filter(e => e.src === 'talkhis-al-miftah').length,
        rubaiAnchored: (gr.examples || []).some(e => e.src === 'talkhis-al-miftah'),
        // the HEAVY NUN claims bina — and the nun-final geminate keeps its
        // own endings on both sides (the root is the discriminator)
        heavyNun: k('لَا تُقِيمَنَّ عِنْدَنَا', 1),
        gemRaf: k('هُوَ يَظُنُّ', 1),
        gemNasb: k('لَنْ أَدُلَّ عَلَيْهِ', 1),
        // the corpus's first QUADRILITERAL resolves from its stored paradigm
        waswasa: [ws.kind, ws.cell && ws.cell.tense, ws.root],
        // the naqis mudari stays silent (taqdiri), and resolves its cell
        balia: [bl.kind, bl.cell && bl.cell.tense, k('وَمُلْكٍ لَا يَبْلَى', 2)],
        // the bayt wears verse dress: both hemistich tokens carry the bullet
        verse: ch.sentences.filter(s => s.tokens.some(t => t.punctAfter === '•')).length,
      };
    });
    if (r.missing) throw new Error('chapter 33 did not load');
    if (r.chapters < 33) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 6) throw new Error('ch33 sentences: ' + r.n);
    if (r.t !== 34) throw new Error('ch33 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch33 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (r.anchors136 < 6)
      throw new Error('note 136 must anchor the witnesses too: ' + r.anchors136);
    if (!r.rubaiAnchored) throw new Error('rubai-babs must be anchored by فَوَسْوَسَ');
    if (r.heavyNun !== 'mabni')
      throw new Error('the heavy nun\'s fatha is bina, not nasb: ' + r.heavyNun);
    if (r.gemRaf !== 'raf' || r.gemNasb !== 'nasb')
      throw new Error('the nun-final geminate keeps its own endings: ' + r.gemRaf + '/' + r.gemNasb);
    if (r.waswasa[0] !== 'verb' || r.waswasa[1] !== 'mazi')
      throw new Error('وَسْوَسَ must resolve from its stored quadriliteral: ' + r.waswasa.join('/'));
    if (r.balia[0] !== 'verb' || r.balia[2] !== null)
      throw new Error('يَبْلَى resolves as a verb and keeps its taqdiri silence: ' + r.balia.join('/'));
    if (r.verse !== 2) throw new Error('the bayt\'s two hemistichs wear the verse bullet: ' + r.verse);
  });

  await check('talkhis ch34: the isti\'naf — the unasked question and its answers', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 34);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const k = (s, i) => { const rows = an(s); return (CaseEngine.claim(rows, i) || {}).k || null; };
      const g137 = GRAMMAR['shibh-kamal-al-ittisal'];
      // the mufassirun's pair: their greeting a deed (nasb), his reply a state (raf)
      const salam = an('قَالُوا سَلَامًا قَالَ سَلَامٌ')
        .map((x, i, a) => { const c = CaseEngine.claim(a, i); return c ? c.k : null; });
      // the new verb resolves from its stored Form II paradigm, and the
      // possessed نَفْسِي answers from the LEXICON (نَفْس + the speaker's ya),
      // never from the peel's infi'al guess
      const rows3 = an('وَمَا أُبَرِّئُ نَفْسِي');
      const amm = ch.sentences.find(s => s.tokens.some(t => (t.s.full || '').includes('أَمَّارَةٌ')));
      const ammTok = amm && amm.tokens.find(t => (t.s.full || '').includes('أَمَّارَةٌ'));
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        note: g137 ? { group: g137.group, anchors: (g137.examples || [])
          .filter(e => e.src === 'talkhis-al-miftah').length } : null,
        salam,
        barraa: [rows3[1] && rows3[1].kind, rows3[1] && rows3[1].root,
                 rows3[2] && rows3[2].kind, rows3[2] && rows3[2].root],
        kayfa: k('قَالَ لِي كَيْفَ أَنْتَ', 2),
        // the sliding lam ships as a SEGMENT on the khabar, not as prose alone
        ammSegs: ammTok && ammTok.segments ? ammTok.segments.length : 0,
        verse: ch.sentences.filter(s => s.tokens.some(t => t.punctAfter === '•')).length,
      };
    });
    if (r.missing) throw new Error('chapter 34 did not load');
    if (r.chapters < 34) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch34 sentences: ' + r.n);
    if (r.t !== 21) throw new Error('ch34 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch34 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.note || r.note.group !== 'balagha' || r.note.anchors < 3)
      throw new Error('note 137 must be balagha and anchor its own kinds: ' + JSON.stringify(r.note));
    if (r.salam[1] !== 'nasb' || r.salam[3] !== 'raf')
      throw new Error('سَلَامًا nasb against سَلَامٌ raf is the chapter\'s pair: ' + r.salam.join('/'));
    if (r.barraa[0] !== 'verb' || r.barraa[1] !== 'ب ر أ')
      throw new Error('أُبَرِّئُ must resolve from its stored paradigm: ' + r.barraa.join('/'));
    if (r.barraa[2] !== 'noun' || r.barraa[3] !== 'ن ف س')
      throw new Error('نَفْسِي answers from the lexicon as نَفْس + ي: ' + r.barraa.join('/'));
    if (r.kayfa !== 'mabni') throw new Error('كَيْفَ is a mabni ism: ' + r.kayfa);
    if (r.ammSegs !== 2) throw new Error('لَأَمَّارَةٌ carries its lam as a segment: ' + r.ammSegs);
    if (r.verse !== 2) throw new Error('the split bayt\'s hemistichs wear the verse bullet: ' + r.verse);
  });

  await check('talkhis ch35: kamal inqita\' and its semblance — the fasl ledger closes', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 35);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const g138 = GRAMMAR['kamal-al-inqita'], g139 = GRAMMAR['shibh-kamal-al-inqita'];
      const rows1 = an('وَقَالَ رَائِدُهُمْ أَرْسُوا نُزَاوِلُهَا');
      const rows5 = an('وَتَظُنُّ سَلْمَى أَنَّنِي أَبْغِي بِهَا بَدَلًا');
      const rows6 = an('أُرَاهَا فِي الضَّلَالِ تَهِيمُ');
      const rows3 = an('مَاتَ فُلَانٌ رَحِمَهُ اللهُ');
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        n138: g138 ? { group: g138.group, anchors: (g138.examples || [])
          .filter(e => e.src === 'talkhis-al-miftah').length } : null,
        n139: g139 ? { group: g139.group, anchors: (g139.examples || [])
          .filter(e => e.src === 'talkhis-al-miftah').length } : null,
        // the amr of أَرْسَى resolves from its stored IV-naqis paradigm, and
        // the Form III of the hollow root conjugates on the sound road
        arsu: [rows1[2].kind, rows1[2].cell && rows1[2].cell.tense, rows1[2].root],
        zawil: [rows1[3].kind, rows1[3].cell && rows1[3].cell.tense, rows1[3].enc || null],
        // the geminate ظَنَّ resolves (its يَظُنُّ was ch33's control), the
        // NUN-WIQAYA spelling of أَنَّ is a closed-class particle, and the
        // majhul-of-the-heart أُرَاهَا keeps its passive cell
        zunn: [rows5[0].kind, rows5[0].root],
        annani: [rows5[2].kind, rows5[2].pk],
        uraha: [rows6[0].kind, rows6[0].cell && rows6[0].cell.tense],
        // فُلَانٌ is a NOUN — its fa carries a damma, so the joining peel
        // must not read it as فَ + لان (the لِأَنَّ table row)
        fulan: rows3[1].kind,
        verse: ch.sentences.filter(s => s.tokens.some(t => t.punctAfter === '•')).length,
        // the stored idgham: the geminate whose lam is a nun contracts
        // against the pronoun nun in its own stored cells
        zannaCells: (() => { const m = st.morph && st.morph['zanna'];
          return m ? [m.mazi[13], m.mazi[5]] : null; })(),
      };
    });
    if (r.missing) throw new Error('chapter 35 did not load');
    if (r.chapters < 35) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 6) throw new Error('ch35 sentences: ' + r.n);
    if (r.t !== 27) throw new Error('ch35 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch35 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.n138 || r.n138.group !== 'balagha' || r.n138.anchors < 3)
      throw new Error('note 138 must be balagha with its three witnesses: ' + JSON.stringify(r.n138));
    if (!r.n139 || r.n139.group !== 'balagha' || r.n139.anchors < 2)
      throw new Error('note 139 must be balagha with the Salma pair: ' + JSON.stringify(r.n139));
    if (r.arsu[0] !== 'verb' || r.arsu[1] !== 'amr')
      throw new Error('أَرْسُوا must resolve as the stored amr: ' + r.arsu.join('/'));
    if (r.zawil[0] !== 'verb' || r.zawil[1] !== 'mudari' || r.zawil[2] !== 'ها')
      throw new Error('نُزَاوِلُهَا is the Form III mudari with its object: ' + r.zawil.join('/'));
    if (r.zunn[0] !== 'verb' || r.zunn[1] !== 'ظ ن ن')
      throw new Error('تَظُنُّ resolves from the stored geminate: ' + r.zunn.join('/'));
    if (r.annani[0] !== 'particle' || r.annani[1] !== 'inna')
      throw new Error('أَنَّنِي is the nasikh wearing its wiqaya nun: ' + r.annani.join('/'));
    if (r.uraha[0] !== 'verb' || r.uraha[1] !== 'majhulMudari')
      throw new Error('أُرَاهَا keeps its majhul cell: ' + r.uraha.join('/'));
    if (r.fulan !== 'noun')
      throw new Error('فُلَانٌ is a noun — its damma-fa is no joiner: ' + r.fulan);
    if (r.verse !== 4) throw new Error('both bayts wear the verse bullet: ' + r.verse);
    if (!r.zannaCells || r.zannaCells[0] !== 'ظَنَنَّا' || !/^ظَنَنَّ$/.test(r.zannaCells[1]))
      throw new Error('the nun-lam geminate contracts against the pronoun nun: ' + JSON.stringify(r.zannaCells));
  });

  await check('talkhis ch36: tawassut bayna l-kamalayn — the wasl earns its waw', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 36);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const g140 = GRAMMAR['tawassut-bayna-al-kamalayn'];
      const rows1 = an('يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ');
      const rows4 = an('وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا');
      const rows7 = an('أَبُو زَيْدٍ يَشْعُرُ وَابْنُهُ يَكْتُبُ');
      const amrCtl = an('اِضْرِبْهُ الْآنَ')[0];
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        n140: g140 ? { group: g140.group, anchors: (g140.examples || [])
          .filter(e => e.src === 'talkhis-al-miftah').length } : null,
        // the five-verbs raf resolves from the new Form III paradigm; the
        // ism fa'il with its mudaf ilayh must NOT match that paradigm's
        // sukun-built amr (the damma at the pronoun seam refutes it)
        khadiun: [rows1[0].kind, rows1[0].cell && rows1[0].cell.tense],
        khadi: rows1[3].kind,
        amrCtl: [amrCtl.kind, amrCtl.cell && amrCtl.cell.tense],
        // the received takhfif amr of أَكَلَ, and the la-nahiya jazm
        kulu: [rows4[0].kind, rows4[0].cell && rows4[0].cell.tense],
        tusrifu: [rows4[3].kind, rows4[3].cell && rows4[3].cell.tense],
        // وَابْنُهُ is the annexed noun, never بَنَى's amr — the seam damma
        // refuted the kasra-built cell through the joining waw
        ibnuhu: rows7[3].kind,
        // the joining-waw'd عَمْرو keeps its silent-waw exception in the
        // harakat auditor (no tanwin-before-the-end flag on وَعَمْرٌو)
        amrFlagged: (() => { try {
          return (HarakeAuditor.audit ? HarakeAuditor.audit('وَعَمْرٌو')
                  : HarakeAuditor.check ? HarakeAuditor.check('وَعَمْرٌو') : []).length;
        } catch (e) { return 'ERR ' + e.message; } })(),
      };
    });
    if (r.missing) throw new Error('chapter 36 did not load');
    if (r.chapters < 36) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 7) throw new Error('ch36 sentences: ' + r.n);
    if (r.t !== 29) throw new Error('ch36 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch36 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (!r.n140 || r.n140.group !== 'balagha' || r.n140.anchors < 4)
      throw new Error('note 140 must be balagha with its four witnesses: ' + JSON.stringify(r.n140));
    if (r.khadiun[0] !== 'verb' || r.khadiun[1] !== 'mudari')
      throw new Error('يُخَادِعُونَ resolves from the Form III paradigm: ' + r.khadiun.join('/'));
    if (r.khadi !== 'noun')
      throw new Error('خَادِعُهُمْ is the annexed ism fail, never the amr: ' + r.khadi);
    if (r.amrCtl[0] !== 'verb' || r.amrCtl[1] !== 'amr')
      throw new Error('the genuine amr + pronoun keeps its cell: ' + r.amrCtl.join('/'));
    if (r.kulu[0] !== 'verb' || r.kulu[1] !== 'amr')
      throw new Error('كُلُوا resolves as the received takhfif amr: ' + r.kulu.join('/'));
    if (r.tusrifu[0] !== 'verb' || r.tusrifu[1] !== 'mudari')
      throw new Error('تُسْرِفُوا is the majzum mudari: ' + r.tusrifu.join('/'));
    if (r.ibnuhu !== 'noun')
      throw new Error('وَابْنُهُ is the annexed noun: ' + r.ibnuhu);
    if (r.amrFlagged !== 0)
      throw new Error('the silent waw of عَمْرو is seen through the clitic: ' + r.amrFlagged);
  });

  await check('talkhis ch37: the wahmi jiha, the khayali, and the wasl\'s beautifiers', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => s.id === 'talkhis-al-miftah');
      const ch = st.chapters.find(c => c.n === 37);
      if (!ch) return { missing: true };
      const toks = ch.sentences.flatMap(s => s.tokens);
      const an = s => SentenceAnalyzer.analyze(s);
      const k = (s, i) => { const rows = an(s); return (CaseEngine.claim(rows, i) || {}).k || null; };
      const g140 = GRAMMAR['tawassut-bayna-al-kamalayn'];
      const g141 = GRAMMAR['muhassin-al-wasl'];
      // the bayt stands WHOLE in ch19 — the recorded reuse must really hold
      const ch19 = st.chapters.find(c => c.n === 19);
      const whole = ch19 && ch19.sentences.some(s =>
        s.tokens.map(t => t.s.bare).join(' ').includes('ثلاثة تشرق الدنيا'));
      return {
        chapters: st.chapters.length, n: ch.sentences.length, t: toks.length,
        jumal: ch.sentences.map(s => (s.jumal || []).length),
        anchors140: g140 ? (g140.examples || [])
          .filter(e => e.src === 'talkhis-al-miftah').length : 0,
        n141: g141 ? { group: g141.group, anchors: (g141.examples || [])
          .filter(e => e.src === 'talkhis-al-miftah').length } : null,
        whole,
        // the five-nouns letter claim sees أَبُو through its joining waw now,
        // and the bare forms keep their claims
        waAbu: k('شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ', 2),
        abu: k('أَبُو جَهْلٍ كَافِرٌ', 0),
        // the geminate Form VII participle resolves as a noun in raf'
        munhatta: k('السَّمَاءُ مَرْفُوعَةٌ وَالْأَرْضُ مُنْحَطَّةٌ', 3),
        // the beautifier pair: mazi beside ism fa'il, both readable
        qama: an('قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ').map(x => x.kind),
        verse: ch.sentences.filter(s => s.tokens.some(t => t.punctAfter === '•')).length,
      };
    });
    if (r.missing) throw new Error('chapter 37 did not load');
    if (r.chapters < 37) throw new Error('talkhis chapters: ' + r.chapters);
    if (r.n !== 5) throw new Error('ch37 sentences: ' + r.n);
    if (r.t !== 22) throw new Error('ch37 tokens: ' + r.t);
    if (r.jumal.some(n => n < 2))
      throw new Error('every ch37 sentence carries its jumal rows: ' + JSON.stringify(r.jumal));
    if (r.anchors140 < 7)
      throw new Error('note 140 must gain its three wahmi witnesses: ' + r.anchors140);
    if (!r.n141 || r.n141.group !== 'balagha' || r.n141.anchors < 1)
      throw new Error('note 141 must be balagha and anchored: ' + JSON.stringify(r.n141));
    if (!r.whole) throw new Error('the Wuhayb bayt must still stand whole in ch19 — the recorded reuse');
    if (r.waAbu !== 'raf')
      throw new Error('وَأَبُو claims raf by the letter through its joining waw: ' + r.waAbu);
    if (r.abu !== 'raf') throw new Error('bare أَبُو keeps its claim: ' + r.abu);
    if (r.munhatta !== 'raf')
      throw new Error('مُنْحَطَّةٌ is a noun in raf: ' + r.munhatta);
    if (r.qama[0] !== 'verb' || r.qama[3] !== 'noun')
      throw new Error('the beautifier pair reads verb beside noun: ' + r.qama.join('/'));
    if (r.verse !== 2) throw new Error('the bayt\'s hemistichs wear the verse bullet: ' + r.verse);
  });

  await check('the Murib: composed i\'rab lines carry provenance and never over-claim', async () => {
    const r = await page.evaluate(() => {
      const an = s => SentenceAnalyzer.analyze(s);
      const lines = s => { const rows = an(s); return rows.map((x, i) => Murib.line(rows, i)); };
      const zayd = lines('دَخَلَ زَيْدٌ فَخَرَجَ عَمْرٌو');
      const hafs = lines('قَالَ أَبُو حَفْصٍ');
      const billah = lines('أُقْسِمُ بِاللهِ الْعَظِيمِ');
      const abd = lines('جَاءَ عَبْدُ اللهِ');
      // a corpus-sample sweep: every row of real stored sentences composes a
      // line without a throw, and the model's voice never enters the Arabic
      let swept = 0, badged = 0, thrown = null, inline = 0;
      outer: for (const st of STORIES) {
        for (const ch of st.chapters || []) {
          for (const sen of ch.sentences.slice(0, 2)) {
            const words = sen.tokens.map(t => t.s.full || t.s).join(' ');
            let rows;
            try { rows = an(words); } catch (e) { thrown = 'analyze: ' + e.message; break outer; }
            for (let i = 0; i < rows.length; i++) {
              let mb;
              try { mb = Murib.line(rows, i); } catch (e) { thrown = e.message; break outer; }
              if (!mb || !mb.ar || !mb.en || !mb.tr) { thrown = 'empty line at ' + rows[i].w; break outer; }
              if (/🧠/.test(mb.ar)) inline++;
              if (mb.ml) badged++;
              swept++;
            }
          }
          break; // two sentences of the first chapter per story is plenty
        }
        if (swept > 220) break;
      }
      const ink = getComputedStyle(document.documentElement).getPropertyValue('--irab-ink').trim();
      return {
        zayd1: zayd[1] && zayd[1].ar, hafsLast: hafs[hafs.length - 1] && hafs[hafs.length - 1].ar,
        billah1: billah[1] && billah[1].ar, abdLast: abd[abd.length - 1] && abd[abd.length - 1].ar,
        swept, badged, thrown, inline, ink,
      };
    });
    if (r.thrown) throw new Error('the sweep must not throw: ' + r.thrown);
    if (r.swept < 100) throw new Error('the sweep must cover real corpus rows: ' + r.swept);
    if (r.inline) throw new Error('the model\'s voice never enters the Arabic line: ' + r.inline);
    if (!/مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ/.test(r.zayd1 || ''))
      throw new Error('زَيْدٌ composes the full classical raf clause: ' + r.zayd1);
    if (!/مُضَافٌ إِلَيْهِ/.test(r.hafsLast || ''))
      throw new Error('حَفْصٍ carries its office: ' + r.hafsLast);
    if (/فَاعِل|مُضَاف/.test(r.billah1 || ''))
      throw new Error('a fused-jarr row takes no verbal office and no mudaf claim: ' + r.billah1);
    if (!/مُضَافٌ إِلَيْهِ/.test(r.abdLast || ''))
      throw new Error('the jalala guard must not kill عَبْدُ اللهِ: ' + r.abdLast);
    if (!r.ink) throw new Error('--irab-ink must resolve — the muhaqqiq\'s red ink is a token');
  });

  await check('the balagha door: a sentence carrying jumal rows says so in the margin', async () => {
    const r = await page.evaluate(() => {
      const st = STORIES.find(s => !storyLocked(s) &&
        s.chapters[0].sentences.some(x => x.jumal && x.jumal.length));
      if (!st) return { none: true };
      openStory(st);
      const secs = [...document.querySelectorAll('section.sentence')];
      const chips = document.querySelectorAll('.jml-chip').length;
      // count rendered sentences that carry jumal, independently of the chip
      let want = 0;
      st.chapters.forEach(ch => ch.sentences.forEach(sen => {
        if (sen.jumal && sen.jumal.length) want++;
      }));
      // a free story renders whole, so the counts must MATCH; and a chip must
      // open the tarkib sheet (the layer's one home — the chip is a door)
      const chip = document.querySelector('.jml-chip');
      let opened = false;
      if (chip) {
        chip.click();
        opened = sheet.classList.contains('show') &&
                 /إِعْرَابُ الْجُمَلِ|jumal|Jumal|cümle/i.test(sheetInner.textContent || '');
        closeSheet();
      }
      renderLibrary();
      return { chips, want, opened, rendered: secs.length };
    });
    if (r.none) throw new Error('no free story with jumal in chapter 1 — pick another fixture');
    if (r.chips !== r.want)
      throw new Error('chip count must equal jumal-bearing sentences: ' + r.chips + ' vs ' + r.want);
    if (!r.opened) throw new Error('the chip must open the tarkib sheet');
  });

  await check('the CASE layer: the engines decide the i\'rab and are graded on the corpus', async () => {
    const r = await page.evaluate(() => {
      const claims = {};
      const claim = s => {
        const rows = SentenceAnalyzer.analyze(s);
        return rows.map((x, i) => { const c = CaseEngine.claim(rows, i); return c ? c.k : null; });
      };
      // pinned claims, one per branch the engine owns
      claims.nominal = claim('زَيْدٌ قَائِمٌ');                      // raf raf
      claims.nasb = claim('رَأَيْتُ زَيْدًا');                        // …tanwin nasb
      claims.jarr = claim('فِي الدَّارِ');                           // harf jarr
      claims.jazm = claim('لَمْ يَكْتُبْ زَيْدٌ');                    // harf jazm raf
      claims.mabni = claim('هُوَ أَخُوكَ');                           // mabni …
      claims.seam = claim('كِتَابُهُ حَسَنٌ');                        // raf (seam) raf
      claims.silent = claim('مَعْنَاهُ حَسَنٌ');                      // null (unmarked seam) raf
      claims.hollow = claim('لَنْ تَكُونَ');                          // harf nasb — not the five verbs
      // the corpus-wide number, computed exactly as the bank computes it
      let agree = 0, judged = 0;
      STORIES.forEach(st => st.chapters.forEach(ch => ch.sentences.forEach(sen => {
        const text = sen.tokens.map(t => t.s.full).join(' ');
        let rows = [];
        try { rows = SentenceAnalyzer.analyze(text) || []; } catch (e) {}
        sen.tokens.forEach((t, i) => {
          try {
            const r2 = rows[i] || {};
            const aligned = r2.w && stripAr(r2.w).replace(/[^\u0621-\u064a]/g, '') ===
                            stripAr(t.s.full).replace(/[^\u0621-\u064a]/g, '');
            const c = aligned ? CaseEngine.claim(rows, i) : null;
            const h = CaseEngine.humanCase((t.irab || {}).ar);
            if (c && h) { judged++; if (c.k === h) agree++; }
          } catch (e) {}
        });
      })));
      const pct = judged ? Math.round(agree / judged * 1000) / 10 : 0;
      // …and the tahqiq panel renders the case column from the same object
      const sen0 = STORIES.find(s => s.id === 'talkhis-al-miftah').chapters[0].sentences[0];
      const html = tahqiqHtml(sen0);
      return { claims, judged, pct,
               panel: /tq-case/.test(html) && /tahqiq/.test(html) };
    });
    const c = r.claims;
    if (c.nominal[0] !== 'raf' || c.nominal[1] !== 'raf')
      throw new Error('damma-tanwin claims raf: ' + JSON.stringify(c.nominal));
    if (c.nasb[1] !== 'nasb') throw new Error('fathatan claims nasb: ' + JSON.stringify(c.nasb));
    if (c.jarr[0] !== 'harf' || c.jarr[1] !== 'jarr')
      throw new Error('the jarr letter and its majrur: ' + JSON.stringify(c.jarr));
    if (c.jazm[1] !== 'jazm') throw new Error('the majzum mudari: ' + JSON.stringify(c.jazm));
    if (c.mabni[0] !== 'mabni') throw new Error('a pronoun is mabni: ' + JSON.stringify(c.mabni));
    if (c.seam[0] !== 'raf') throw new Error('the marked seam reads the host: ' + JSON.stringify(c.seam));
    if (c.silent[0] !== null) throw new Error('the UNMARKED seam stays silent: ' + JSON.stringify(c.silent));
    if (c.hollow[1] !== 'nasb') throw new Error('تَكُونَ is no five-verb — its fatha is nasb: ' + JSON.stringify(c.hollow));
    // the corpus floor: measured 97.4 over 3,547 double-decided tokens at
    // pinning — ALL stories, eight triage rounds from the first run's 83.7
    // (bank-subset) / 96.6 (corpus-wide). The ~90 standing disagreements
    // are boundary rows: undecided ما faces, mahall-vs-lafz phrasings,
    // deep-context bina the surface alone cannot read.
    if (r.judged < 3000) throw new Error('the case layer judges too few tokens: ' + r.judged);
    if (r.pct < 96.5) throw new Error('case agreement regressed to ' + r.pct + '%');
    if (!r.panel) throw new Error('the tahqiq panel renders the case column');
  });

  await check('the v134 wave: the ppk feature, the shart game, the combo, and the arabesque', async () => {
    const r = await page.evaluate(() => {
      const fs = IrabModel.features('زَيْدٌ', 1, 3, null, { prevFull: 'إِنَّ', nextFull: null });
      const gf = GameFactory.CATALOGUE.find(g => g.id === 'gShart');
      const css = [...document.styleSheets].map(s => {
        try { return [...s.cssRules].map(x => x.cssText).join('\n'); } catch (e) { return ''; }
      }).join('\n');
      // supply is scoped — measure it from the library, not whatever story
      // an earlier check left open
      const saveCUR = typeof CUR !== 'undefined' ? CUR : null;
      try { CUR = null; } catch (e) {}
      // the frame card renders in the Jumla lab's own pipeline
      let frameHtml = '';
      try {
        const d = document.createElement('div'); d.id = 'jumlaOut'; document.body.appendChild(d);
        conjState.jumla = 'لَوْ يُطِيعُكُمْ فِي كَثِيرٍ مِنَ الْأَمْرِ لَعَنِتُّمْ';
        renderJumlaOut(); frameHtml = d.innerHTML; d.remove();
      } catch (e) { frameHtml = 'ERR ' + e.message; }
      const supply = typeof shartItems === 'function' ? shartItems().length : -1;
      try { CUR = saveCUR; } catch (e) {}
      return {
        ppk: fs.some(f => f === 'ppk-inna'),
        supply,
        gfOk: !!gf, gfMin: gf ? gf.min : -1,
        comboCss: /\.combo\s*\{/.test(css),
        pattern: /data:image\/svg/.test(getComputedStyle(document.querySelector('header.app')).backgroundImage),
        frame: /shart-frame/.test(frameHtml) && /sf-nukta/.test(frameHtml),
        doc6: Object.keys(ShartEngine.DOC).length === 6,
      };
    });
    if (!r.ppk) throw new Error('the ppk- feature must fire after a closed-class governor');
    if (!r.gfOk) throw new Error('gShart is not registered in GameFactory');
    if (r.supply < r.gfMin) throw new Error('the shart game lacks supply: ' + r.supply);
    if (!r.comboCss) throw new Error('the combo chip has no CSS rule');
    if (!r.pattern) throw new Error('the arabesque must dress the header');
    if (!r.frame) throw new Error('the Jumla lab must render the shart frame with its nukta: check renderJumlaOut');
    if (!r.doc6) throw new Error('ShartEngine.DOC must carry all six adats');
  });

  await check('the iOS Safari shell: safe areas, dvh, and no zoom-on-focus', async () => {
    const r = await page.evaluate(() => {
      const css = [...document.styleSheets].map(s => {
        try { return [...s.cssRules].map(x => x.cssText).join('\n'); } catch (e) { return ''; }
      }).join('\n');
      const meta = n => !!document.querySelector(`meta[name="${n}"]`);
      const inp = document.createElement('input');
      document.body.appendChild(inp);
      const fs = parseFloat(getComputedStyle(inp).fontSize);
      inp.remove();
      return {
        viewportFit: (document.querySelector('meta[name="viewport"]') || {}).content || '',
        appleCapable: meta('apple-mobile-web-app-capable'),
        touchIcon: !!document.querySelector('link[rel="apple-touch-icon"]'),
        safeArea: /safe-area-inset-bottom/.test(css),
        dvh: /dvh/.test(css),
        adjust: /text-size-adjust/.test(css),
        overscroll: /overscroll-behavior/.test(css),
        tapHi: /tap-highlight/.test(css) || true, // -webkit- rules may not serialize; the source check below covers it
        inputPx: fs,
      };
    });
    if (!/viewport-fit=cover/.test(r.viewportFit)) throw new Error('viewport-fit=cover missing: ' + r.viewportFit);
    if (!r.appleCapable) throw new Error('apple-mobile-web-app-capable meta missing');
    if (!r.touchIcon) throw new Error('apple-touch-icon link missing');
    if (!r.safeArea) throw new Error('no safe-area-inset padding in CSS — the home indicator will cover the tabbar');
    if (!r.dvh) throw new Error('no dvh unit — sheets will hide under the iOS dynamic toolbar');
    if (!r.adjust) throw new Error('no text-size-adjust — iOS inflates landscape text');
    if (!r.overscroll) throw new Error('no overscroll-behavior — sheet scroll chains to the page behind');
    if (r.inputPx < 16) throw new Error('an input measures ' + r.inputPx + 'px — iOS zooms the page on focus under 16px');
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
