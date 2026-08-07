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
        afterQawl: at('قال زيد ان الله قادر', 2),
        afterVerb: at('علم زيد ان الله قادر', 2),
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
    const pool = await page.evaluate(() => hamzaItems().length);
    if (pool < 8) throw new Error('hamza pool too small: ' + pool);
    await page.locator('.lib-card').first().click();
    await page.locator('#gamesOpen').click();
    await page.locator('.game-pick #gHamza').click();
    await page.waitForSelector('.sheet.show .game-q', { timeout: 3000 });
    const opts = await page.locator('.opts [data-o]').allTextContents();
    const bare = opts.map(o => o.replace(/[ً-ٰ]/g, ''));
    if (!(bare.some(o => o.includes('إن')) && bare.some(o => o.includes('أن'))))
      throw new Error('options must be inna vs anna, got: ' + opts.join(' | '));
    await page.locator('.opts [data-o]').first().click();
    if (!(await page.locator('.game-why').count())) throw new Error("no i'rab shown after answering");
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
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
    if (r.worked < 12) throw new Error('worked relations: ' + r.worked);
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
    if (r.sentences !== 4) throw new Error('ch10 sentences: ' + r.sentences);
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
    if (rows !== 12) throw new Error('the panel should show all twelve worked relations, got ' + rows);
    if (!(await page.locator('#alaqaPlay').count())) throw new Error('the panel should offer its game');
    await page.evaluate(() => document.getElementById('scrim').click());
    await page.locator('#backLib').click();
    await page.waitForSelector('.lib-card', { timeout: 3000 });
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
    if (!en(r.idafa[0].notes).includes('mudaf (idafa)')) throw new Error('kitab al-talib must read as idafa: ' + en(r.idafa[0].notes));
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
  // 42.7/62.9 to 49.3/71.0 when it was added; the floor sits just under that.
  await check('the model scores on the corpus, and the score is pinned', async () => {
    const a = await page.evaluate(() => {
      const x = IrabModel.accuracy();
      return { n: x.n, top1: Math.round(x.top1 * 1000) / 10, top2: Math.round(x.top2 * 1000) / 10,
               shown: (document.body.innerHTML.match(/ml-score/g) || []).length };
    });
    if (a.n < 2000) throw new Error('the labeled set shrank: ' + a.n);
    if (a.top1 < 47) throw new Error('first-guess accuracy regressed to ' + a.top1 + '%');
    if (a.top2 < 68) throw new Error('two-guess accuracy regressed to ' + a.top2 + '%');
    await page.evaluate(() => { conjState.lab = 'jumla'; });
    await page.locator('#conjOpen').click();
    await page.waitForSelector('.ml-score', { timeout: 3000 });
    const line = await page.locator('.ml-score').textContent();
    if (!line.includes(String(a.n))) throw new Error('the panel must state the real size: ' + line);
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
               ml: html.includes('ml-vote') };
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
    if (r.heads.length !== 4) throw new Error('four disciplines expected, got ' + r.heads.length);
    if (r.firstHead !== 0) throw new Error('a card sits above the first heading');
    if (r.orphanHead) throw new Error('a heading has no card under it');
    if (r.cards.length !== 12) throw new Error('twelve games expected, got ' + r.cards.length);
    for (const id of r.cards) {
      const wired = await page.evaluate(i => !!document.getElementById(i), id);
      if (!wired) throw new Error('card ' + id + ' vanished');
    }
    await page.evaluate(() => closeSheet());
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
