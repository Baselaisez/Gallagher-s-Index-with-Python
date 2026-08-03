# Qissa — working notes

An Arabic graded-reader app (DuChinese-shaped) built on classical Islamic texts,
with madrasah grammar attached to every word. Target: iOS + Android launch.
Everything here is the *why*; the code is the *what*.

## Where things live

```
content/
  grammar/          87 global grammar notes — one JSON per topic, shared by every story
  i18n/irab-tr.json Turkish translation memory for i'rab strings, keyed by the English
  samples/<story>/  manifest.json · chapters/N.json · glossary.json · morphology.json
  user-uploads/     same shape; deeds-are-by-intentions ships its own standalone reader.html
  catalog.json      generated — index of every package (level, access, chapter count)
prototype/reader.html   the whole app: shell + generated data block
tools/
  validate_content.py   the quality gate — run it before anything else
  build_prototype.py    splices JS constants between // __DATA_START__ / // __DATA_END__
  smoke_test.js         96 browser checks over file:// (Playwright)
  pwa_test.js           9 checks over http:// — manifest, icons, SW,actually-offline
  make_icons.js         regenerates prototype/icons from one HTML source
  check_canon.py        audits the registry against the madrasah's own lists
                        (20 harf-i cer, 8 inna sisters, 15 jawazim, 13 mansubat…)
                        — coverage report, not a gate; --strict only checks that
                        every mapped note id really exists
  check_irab_tr.py      finds i'rab strings with no Turkish yet
  check_i18n.py         fails on ANY user-visible string that has en but no tr
  release.py            ONE COMMAND from edited content to a shippable build:
                        validates every package, rebuilds both readers, runs
                        smoke+i18n+canon+dart+pwa, bumps sw.js. --check skips
                        the bump; QISSA_SKIP=smoke,pwa,dart for browserless CI
  authoring/new_story.py scaffolds a new story's regenerator (the stub
                        INTENTIONALLY fails validation until TODOs are filled)
flutter/                the mobile client: lib/models is a VERIFIED data layer
                        (tool/verify_models.dart proves it against content/);
                        main.dart + reader/ are still an unverified design spike
research/sources/       transcribed madrasah texts + README on provenance
```

Fifteen stories, Levels 1–6 (fourteen sample packages plus the deeds-are-by-intentions upload). kitab-al-waqf (L4 Upper Intermediate, premium, TWO chapters, regenerator tools/authoring/author_waqf.py) is ORIGINAL graded Arabic from the user's Turkish waqf sohbet (research/sources/vakif-mali-turkce.txt) — ch1: definition, inviolability, misuse-is-theft, the qaida شرط الواقف كنص الشارع; ch2: the lüzum khilaf with بقولهما يُفتى, the waqif's conditions, ghasb with radd+daman, the amana close. ittaqa's morphology stores the SURFACE wazn اِتَّعَلَ so the audit skips the ibdal it cannot re-derive (the akhadha precedent). Aqaid runs to four chapters, the Abu Yusuf wasiyya to five; Kitab al-Buyu and Kitab al-Kaffarat are the fiqh texts; wasiyyat-abi-hanifa-samti (L5, **eleven chapters — the received text is COMPLETE**, from the narrative frame through the counsel to al-Samti's epilogue at the Euphrates) carries the wasiyya to Yusuf b. Khalid al-Samti; the verbatim text lives in research/sources/wasiyya-samti-arabic.txt (one obscure clause, وانتقضت المجالس, is held back pending scholarly review — the manifest attribution lists every divergence). kitab-al-sulh (L5 Advanced, premium, **COMPLETE — six chapters, v1.0.0**: definition/legitimacy; kinds; the six contract-guises; the parties' conditions; the riba rules; effects and end — closing on وَالصُّلْحُ خَيْرٌ, the aya it opened with) is **ORIGINAL graded Arabic** composed editorially from the user's Turkish sulh article (research/sources/sulh-fiqh-turkce.txt; the aya and hadith are received text, everything else editorial — the attribution says so and must keep saying so); its regenerator is tools/authoring/author_sulh.py. bad-al-amali (L6 Master, premium, version 1.0.0) carries the Ushi qasida **COMPLETE — all 67 verses in fourteen chapters** from research/sources/emali-qasida-ottoman.txt (ch14 is the two-verse khatima) (v22: the upload reads فِعْلٌ أَصْلَحُ as attribute, not the فِعْلُ أَصْلَحَ idafa of some prints — divergence recorded in the manifest attribution). The story-regenerating scripts are IN THE REPO: `tools/authoring/author_amali.py`, `author_samti.py` and the paradigm generator `sarf_gen.py` (selftest reproduces hand-authored corpus paradigms; run any author script from anywhere — paths are __file__-relative). Grammar notes are **global**: a note authored once shows
up in every story that anchors a token to it. Never duplicate a note per story.

## The loop

```sh
python3 tools/validate_content.py content/samples/<pkg>     # every package you touched
python3 tools/build_prototype.py                            # full discovery + catalog.json
cp prototype/reader.html content/user-uploads/deeds-are-by-intentions/reader.html
python3 tools/build_prototype.py --package content/user-uploads/deeds-are-by-intentions \
        --html content/user-uploads/deeds-are-by-intentions/reader.html
NODE_PATH=<scratchpad>/node_modules CHROMIUM_PATH=/opt/pw-browsers/chromium-1194/chrome-linux/chrome \
        node tools/smoke_test.js
python3 tools/check_i18n.py                                 # no English without Turkish
# when the content SCHEMA changes (new manifest/token/note field), also:
#   dart analyze flutter/lib/models flutter/tool && dart flutter/tool/verify_models.dart content
# — the Flutter data layer must not drift from what the packages actually hold
node tools/pwa_test.js                                      # only when the head or sw.js changed
```

Run every command from `arabic-app/`, but `git add` from the repo root — a recurring
foot-gun. The reader is a *renderer*; content packages are the source of truth. Never
hand-edit inside the data block.

## Invariants the validator enforces

- **Tashkeel layers**: `strip_diacritics(full) == bare` and `strip(smart) == bare`.
  Diacritics are `[ً-ٰٕ]`. A mismatch means a typo in the Arabic, every time.
- Every `lex` resolves in `glossary.json`; every `grammar` id resolves in the registry.
- Every glossary entry is reached by at least one token (no dead vocabulary).
- Bilingual everywhere: `{en, tr}` on glosses, notes, explanations, mistakes,
  manifest titles/subtitles/chapter titles, **grammar-note titles and every worked
  example**. Turkish is not optional. `tools/check_i18n.py` is the gate: run it
  with the validator. It applies the same i'rab translation-memory merge the
  builder does, so a token without `tr` is fine if `content/i18n/irab-tr.json`
  covers its English.
- Labels that live in the data as English — `pos`, `levelName` — are translated at
  the point of display (`POS_TR`, `LEVEL_TR` in the reader), not duplicated per
  package. Adding a new level name means adding it to `LEVEL_TR` too; the checker
  enforces that.

## Rules learned the hard way

**Store governed forms, don't derive them.** `mansub` / `majzum` / `majzum2` and
`majhulMazi` / `majhulMudari` are authored per verb in `morphology.json`. The
vowel-swap rule breaks on weak verbs — يَقُولُ → لَمْ يَقُلْ, رَمَى → لَمْ يَرْمِ,
قَالَ → قِيلَ. When a form is genuinely uncertain, omit it: the UI hides the row.
**Never publish Arabic we aren't sure of.**

**Every glossary verb owns a paradigm — a smoke check now sweeps the corpus
for it.** The paradigms were bulk-authored by `sarf_gen.py` (scratchpad): two
assembly engines (suffix-attach for sound/hollow/geminate, a naqis engine for
the three defective endings) plus an explicit per-verb spec for everything
lexical. The engines are trusted only because they reproduce the corpus's
hand-authored paradigms cell-for-cell (qala, daa, baqiya, awsa, istaadda…) —
that selftest is the correctness argument. Two traps the engines cannot see:
NFC-normalize everything (the corpus stores fatha-before-shadda; naive
concatenation produces the other order, visually identical, string-unequal),
and idgham where the root's last radical meets an identical suffix letter
(كَانَ → كُنَّ، مَاتَ → مُتَّ، اِمْتَحَنَ → اِمْتَحَنَّا — never كُنْنَ). Paradigms are
semantics-free, so a verb authored in one package is copied into another after
a lemma identity check. `author_samti.py` merges with the on-disk morphology
instead of overwriting it, so regenerating the story keeps the bank.

**A jamid verb stores exactly the tenses that exist — absence is doctrine,
not omission.** `"jamid": true` on a morphology entry means: 14 mazi cells
always; a mudari (and governed forms) only if the verb really has them; never
an amr, masdar or participles. لَيْسَ is mazi-only; زَالَ (أخت كان الملازمة
للنفي) keeps its mudari and its real لَمْ يَزَلْ but has no imperative.
Validator, builder, reader, Dart harness and the governed-forms smoke sweep
all understand the flag. The sarf tab offers only the tenses present, and
`muhtelife()` additionally requires a non-empty amr (the table has an
imperative row), so no drill, verb card or game ever picks one.

**Passive by wazn, not by letter count.** Form II verbs with three bare letters
(وَدَّعَ, عَلَّمَ) fell through to the Form I branch and produced *وُدِعَ. Match the
`wazn` regex first.

**Old `.doc` files decode as utf-16-le.** Scoring encodings by "most letters" picks
cp1256 and yields garbage; the WordDocument stream is UTF-16. Check the output reads
as words before trusting it.

**PDF Arabic extraction is unreliable** — harakat come out as separately positioned
glyphs. Render to images (`pdftoppm`) and transcribe from the page instead.
`libreoffice` is broken in this container; `python-docx`, `olefile` + utf-16-le,
`xlrd`, and poppler all work.

## Data model notes

- **Clitic segmentation**: `segments: [{form, lex}]` splits وَبِالْكِتَابِ into its parts.
- **i'rab** is per-token `{ar, en, tr}`. Author `{ar, en}`; the builder merges Turkish
  from `content/i18n/irab-tr.json` so a phrase repeated across stories is translated once.
- **Idioms/phrases**: the *first* token of the span carries
  `{"phrase": {"lex": "bayna-yadayh", "span": 2}}` and the phrase gets its own
  glossary entry (`pos: "phrase"`, plus `literal` and `note`). The reader tints the
  span and shows a banner above every tab. **Both layers survive**: بَيْنَ يَدَيْهِ
  means "in his presence" *and* بَيْنَ stays a mansub zarf with يَدَيْهِ its mudaf ilayh.
- **Reading modes** (`state.mode`): `easy` translates the sentence, `medium` drops the
  translation and stacks each word over its gloss (interlinear — `.word.stacked`),
  `hard` shows Arabic only. Translation language follows `state.uiLang`; the old
  `– / EN / TR` segment is gone. A per-sentence "Show meaning" button lets a stuck
  reader peek without leaving the mode.
- **The quiz shell is `runQuiz` — games supply hooks, never markup.** Six of
  the seven games (sarf, case, role, harakat, spot, cloze) run on one machine:
  `runQuiz({title, ask, items, restart, question(it), options(it), why(it),
  after?, extras?})`. `options()` returns `[{html, ok, ar?}]` **pre-shuffled** —
  the shell knows nothing about distractors, which is where each game's domain
  logic lives (the role game's nominal filter, cloze's pos gating; the case game
  deliberately does NOT shuffle, its four options sit in the case-table order).
  Reveal DOM is uniform: `.opts [data-o]`, `#qWhy`, `#qNext`, extras `#qX0…`.
  Match stays OUTSIDE the shell on purpose — a pairing grid with no rounds and
  no reveal is a different game, not a seventh copy. A new quiz game is an items
  function plus ~15 lines of hooks; anything that needs shell changes is a shell
  feature and lands for all six at once.
- **`pos` reaches the reader.** The role game needs it: a verb's i'rab routinely names
  another word's role («فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ» is not a fa'il), so
  anything derived by regex from i'rab text must first filter to nominals.
- **The Lite deck cap** (`LITE_DECK_CAP`, research §7.5) gates ADDING only —
  reviewing, grading and removing always work, because a lapsed subscriber must
  never lose access to their own cards. `toggleCard` returns false on refusal;
  `learnNewHere` counts only words that actually went in, or the daily goal
  would fill with cards that were never created. Save buttons render disabled
  with the reason instead of dying silently.
- **The daily loop**: `state.streak` (days + last date), `state.today` (reviewed /
  learned / read, reset by `rollDay()` when the local date changes) and `state.goal`.
  `countActivity(kind)` is called from `grade()` and `markRead()` — it bumps the
  counter, extends the streak only when the date is new, and always refreshes the
  chip (an early return there once froze the percentage at 0). Dates are LOCAL:
  a streak is about the learner's day. `newWordsHere()` offers the words of the
  chapter being read, level-ascending, that are not already in the deck.
- **Recorded narration is a content drop, not an app change.** A chapter names
  its recording (`audioFile` in the manifest chapter entry, file inside the
  package — the validator 404-checks it) and each sentence carries its
  `audio: [startMs, endMs]` slice. `buildSenAudio()` maps sentence → slice when
  a story opens; `speak()` plays the slice through one shared `Audio` element
  and only falls back to synthesis where either half is missing — half-wired
  narration must fall back, never go silent. The stop is a rate-scaled timer
  plus a `timeupdate` guard (timers drift when the tab is throttled). No
  word-level highlight on recordings: there are no boundary events, and
  interpolating one would be a guess — the sentence highlight is the honest
  cue. To ship narration: record the chapter, time the sentences, add two
  fields, rebuild. Nothing else.
- **A failed narration play() must never advance the queue.** The recorded
  branch mirrors the TTS branch's contract: on refusal or failure, clear the
  highlight and stop play-all — never call onDone, or a 404'd audio file races
  through the story in microtasks marking everything read. The span deadline
  timer re-checks `currentTime` and re-arms rather than truncating (buffering
  makes wall-clock a lie), and same-source detection compares RESOLVED URLs
  (`endsWith` both matched wrong files and missed percent-encoded ones).
  The cloze «see it in the story» gap was closed as a shell feature: a quiz
  extra may declare `show(it)` and is simply not offered for items where the
  action would dead-end — a sentence behind the paywall gets no jump button
  rather than a jump into the preview wall.
- **Corpus search** (`buildCorpus`, `searchCorpus`): one lazily-built index over every
  token in every story, matched against the bare spelling, the lemma, the root (stored
  spaced ق و ل but indexed closed-up too, because that is how it gets typed) and both
  glosses. Alif and ta-marbuta are folded. The root chip in the word sheet is a button
  that runs the same index — that is the root family view, not a separate feature.
  `jumpTo` opens the story if needed; a hit behind a paywall preview is not on the page,
  so it reopens the search rather than failing silently.
- **The Lite tier rotates.** `rotatingFree()` derives the week's free premium
  stories from the date — never from storage, so every device agrees with no
  server and clearing storage does not mint a new set. The window is
  `FREE_ROTATION` wide and slides forward by its own width each week, over the
  premium ids **sorted by id**, so inserting a story mid-catalogue does not
  reshuffle the week and every story comes round in turn. `storyLocked()` is the
  single source of truth — `isFreeThisWeek()` is defined as its complement
  rather than as a second copy of the same clauses. The badge, the paywall and
  the Play-all gate all read
  it, and the test asserts they cannot disagree. Anything hard-coding a
  particular premium story as "locked" will break in the week that story is free
  — pick by `storyLocked()` instead.
- **One civil-date convention, everywhere.** `localMidnight()` renders the
  learner's own day as a UTC instant, and everything that subtracts dates must
  produce its operands the same way. `Date.parse("2026-07-28T00:00:00")` returns
  *local* midnight, and mixing the two made a story published today read as −1
  days old anywhere west of UTC — so the NEW badge never appeared on the day a
  story shipped, for half the world, on a machine where the tests were green.
  The regression test asserts a story published *today* is zero days old, which
  holds in any timezone the suite happens to run in.
- **First-run onboarding asks exactly one question.** `state.myLevel`
  (`qissa-mylevel`, 0 = unset) feeds `LIB_SORTS.foryou`: distance from the
  reader's level with easier breaking the tie — at-level, one easier, one
  harder, two easier… newest first within a shelf. The picker's choices come
  from `levelChoices()` (the levels actually on the shelf), never a hardcoded
  list. `qissa-welcomed` guards the boot-time auto-open separately from the
  answer: dismissing the sheet is an answer too, and must not re-nag on every
  boot — the level chip and the "For you" button reopen the picker on demand,
  and `setLibSort("foryou")` with no stored level opens the question instead
  of sorting by a default. Every fresh-context test (smoke, PWA) pre-seeds
  `qissa-welcomed=1` unless it is testing onboarding itself, or the sheet sits
  over whatever the test clicks first.
- **The library remembers the reader.** `qissa-lastread` stores only the id of
  the last story opened; the continue card offers it back while it is
  unfinished, and `openStory(st, true)` resumes at the first sentence whose id
  is not in `state.progress` (scroll + one flash of `.resume-target`). A
  finished story retires the card — `read === total` swaps the read-count chip
  for ✓ instead. The card is a `.continue-card`, deliberately NOT a
  `.lib-card`: every test and sort walks `.lib-card`, and the hero must never
  count as a second copy of the story.
- **Every story carries its word list.** `openVocab()` — the vocab chip in the
  story header — lists the story's teachable words once, easiest first, each
  saveable to the deck in place. Reads GLOSSARY live, stores nothing. The chip
  is `.chip.vocab`, deliberately NOT `.sib`: the sibling switcher and its test
  click `#metaRow .sib` positionally, and the vocab chip must never be the
  button they land on.
- **The library sells the deck, and the deck calls back.** Every unfinished
  card carries a live "{n} new words" chip (`storyNewWords`: unique token
  lexes with level ≥ 1 not already saved — segments don't count, the reader
  meets the whole token), and a dashed review-nudge banner appears in the
  library whenever `dueCards()` is non-empty. Both are computed at render;
  the smoke check hand-counts one story independently rather than calling
  `storyNewWords`, so agreement is evidence.
- **The progress page computes, never stores.** `openStats()` reads everything
  live through `storyStats`/`deckStats`/`rollDay` — the same primitives the
  library and deck already trust — so the tiles cannot disagree with the shelf.
  The smoke check derives its expectations through those primitives too, which
  proves agreement rather than two copies of the same arithmetic. The streak
  chip is the same numbers seen smaller; tapping either opens the page.
- **A word card born in a sentence carries a snapshot** (`card.ctx`:
  story/sen ids + pre/word/post strings, captured in `toggleSave(tok, ctx)`
  from `wordCtx`). Review's final reveal shows the sentence with the word
  bolded — the Satori Reader pattern. The snapshot is OPTIONAL: vocab-sheet
  and learn-goal saves have no sentence, old cards have none, and the render
  guards on it. The smoke check asserts pre+word+post reassembles the exact
  sentence — the only thing that can silently drift.
- **The deck is visible while reading.** `renderStory` builds a Set of deck
  lexes once and marks matching tokens `.in-deck` (underline turns the ok
  green); every span carries `data-lex`, and the save button flips the
  page's copies live in both directions. LingQ's known-word marking, in
  Qissa's underline language.
- **The streak forgives once a week.** `countActivity` grants a mercy day:
  a last-studied of exactly two days ago continues the chain IF
  `streak.shieldWeek` differs from the current `weekKey()` (approximate
  local week — the shield is a kindness, not accounting). The shield is
  consumed by stamping the week, a toast says so, and an ordinary
  yesterday-continuation never touches it. Absent field = shield available
  (backward compatible).
- **The snapshot is a door.** `.card-ctx` on the review card is clickable —
  `jumpTo(ctx.story, ctx.sen)` with no token index, so it scrolls to the
  sentence without popping a word sheet; jumpTo's paywall fallback applies.
- **`cardKey()` is the only statement of card identity.** Membership tests and
  toggles all route through `findCard`/`cardSaved`/`toggleCard`; a new card type
  declares its key once instead of adding a fourth hand-written `findIndex`
  predicate. Test deck membership *positively* (`type === "word"`), never
  negatively (`type !== "verb"`) — the negative form silently widened to admit
  note cards, which have no `lex` at all.
- **`pruneDeck()` is the single guarantee that a stored deck is renderable.**
  `GRAMMAR` is baked into the file and never changes at runtime, so once it has
  run no card can point at a missing note — which is why nothing downstream
  carries a fallback for that case. Don't add one back; extend the prune.
- **`published` is authored, never derived.** Each manifest carries the day the
  story entered the library (not the day the text was written) — seeded once
  from each package's first git commit, stamped by `analyze_text.py` for
  uploads, and required by the validator. A rebuild must never re-date the
  catalogue, which is why it is content and not something the builder computes.
  The library badges anything under `NEW_FOR_DAYS` and can sort newest-first;
  undated stories sort *last*, not first, which an epoch-0 fallback would do.
  This exists because invisible content cadence is the single sharpest
  complaint about the app this one is modelled on — see `research/01-*.md` §7.2.
- **Every note opens in plain language (`plain`, required).** One jargon-free
  sentence, both languages, capped at 320 characters by the validator — a
  summary as long as what it summarises is not one. It renders as the lede and
  the classical `explanation` folds into a `<details>` whose open state is
  remembered in `state.deepNotes`, so a beginner is not walled off by
  «Badi' is the third of the three sciences of balagha…» and a student opens
  the full text once rather than every time. `<details>`'s `toggle` event does
  **not bubble** and is dispatched **asynchronously**: the listener is on
  `sheetInner` in the capture phase, and anything reading the preference right
  after a click has to wait for it rather than read it in the same tick.
- **The chrome is copy, not build metadata.** The header used to read
  `Qissa · app shell v0.6` and the footer named a repository path. A test now
  fails on any version string, "prototype", or file path in the header or
  footer. Ship-facing text belongs in `L.en`/`L.tr` like everything else.
- **The app follows the device language on first run** (`navigator.language`),
  with a stored choice always winning. Defaulting to English meant a Turkish
  reader met an English app despite the whole content layer being bilingual.
- **The question test (`question` on a note).** The Ottoman madrasah's own
  answer to *how do I know which i'rab this is?*: you ask which question the
  word answers. Fa'il answers «Ne? Kim?», maf'ul fih «Nerede? Ne zaman?», hal
  «Ne olduğu halde?». Eleven nahw notes carry it, from
  `research/sources/edatlar-irab-soru-testi.txt`. It renders above the
  explanation — a reader who has just tapped a word wants to recognise the role
  before reading about it — and the role game shows it on reveal, since it is
  the thing that would have given the answer away.
  **The Turkish is the source and the English is a functional equivalent, not a
  translation.** The device works because Turkish case endings line up with
  Arabic's; English has none, so «Neyi?» and «Neye?» both collapse toward
  "what". Say so rather than implying the mapping is exact. The validator
  requires `tr` and `en` to be non-empty and the *same length*, because they are
  read as corresponding lists.
- **Cloze gates on the glossary's `pos`, not the token's.** They legitimately
  disagree — تَعَالَى is a verb in form but a formulaic particle in the lexicon —
  and since the options are citation forms, the lexical class has to govern both
  which words may be blanked and which words may be distractors. Mixing the two
  offered a verb against three particles, which gives the answer away by shape
  alone. Anything drawing multiple-choice options from the glossary needs the
  same rule. Candidates are bucketed by pos **once per story**
  (`glossaryByPos`) and pools are resolved only for the eight items a round
  uses — filtering the whole glossary per candidate made the walk cost
  tokens-read x glossary-size, so it got slower the more the reader had read.
- **Word-following playback.** `sentenceText(sen)` returns the spoken string
  **and** each token's character range from one walk, so the boundary handler
  and the utterance cannot describe the format differently
  (`full + punctAfter`, spaces between; `quoteBefore`/`quoteAfter` are rendered
  but never spoken). The highlighted element is held in `spokenEl` rather than
  re-queried: boundary events arrive several times a second and `.word.speaking`
  has no fast path, so the document sweep walked hundreds of spans to find the
  one element we had just classed ourselves. Boundary events are best-effort — some engines never fire
  one — so the word highlight is pure enrichment layered over the sentence
  highlight, which still works with no voices at all. The test checks the
  offsets against the real string for every token in the corpus, because that
  agreement is the only thing that can silently drift.
- **Grammar topics are reviewable.** A `note` card stores only `noteId`; the
  title and example are read from `GRAMMAR` at review time, so a corrected or
  retranslated note never leaves a stale copy in someone's deck — and an orphan
  id is pruned at boot rather than rendered blank. The card asks the madrasah
  question: name the term, then give an example.
- **Chapter pills** (`.ch-nav`) render only when MORE THAN ONE `.chapter-head`
  actually rendered — built from the DOM after the paywall cut, never from the
  manifest, so a pill can never point at a chapter the preview dropped.
- **Tarkib vs I'rab — two layers on one sheet.** The sentence button is
  تركيب: the word-by-word table (unchanged). Below it, sentences that carry
  authored `jumal` rows get an إِعْرَابُ الْجُمَلِ section: each CLAUSE named
  and given — or denied — its mahall, per Ibn Hisham's Qawa'id al-I'rab
  (7 with mahall / 7 without; `anwa-al-jumal` teaches the doctrine and is
  auto-offered in the sheet's topics when jumal exist). `jumal` is optional
  per sentence, authored trilingual {text, ar, en, tr}; builder forwards it,
  the validator and the Dart harness reject half-translated rows. Where the
  token layer and the clause layer meet (a bare jawab al-shart), the token
  states the VERB's mahall and the clause row the CLAUSE's — the Qawa'id
  distinction, not a contradiction.
- **Sentence tarkib sheet**: the تركيب button on each sentence opens the whole sentence
  analysed at once — the exercise a madrasah student writes out. It needs nothing beyond
  per-token `irab`, so it comes free with any new chapter.
- **Birgivi's ma'mul taxonomy** organizes the registry — every note carries `mamul`
  (marfu' 8/8, mansub 13/13, majrur 2/2, majzum 1/1, tawabi' 5/5: complete).
- **Emsile-i Muttarida** = one form across 14 persons; **Emsile-i Muhtelife** = 14
  forms from one verb (+2 passive rows). Both render from `morphology.json`.

**Kitab al-Kaffarat repeats the Buyu' pattern and adds a third source class.**
The upload was again a Turkish teaching text; the Arabic is, line by line:
the source's own definition rendered in standard fiqh phrasing, the received
Quduri wording for the Ramadan kaffara — and, where the Turkish itself cites
scripture, the Qur'an quoted exactly (al-Ma'ida 5:89 for the oath; s10 built
on al-Baqara 2:196). Qur'anic wording is the one class that needs no
hedging, and the manifest attribution says which sentences are which. The
story anchors the newest registry notes on arrival: مُتَتَابِعَيْنِ is the Form VI
ism fa'il in na't position, مِسْكِينًا the tamyiz of a number (the canon's
«İsmi Mübhemüt Tam» governor), أَذًى a maqsur noun under the lam of cause.

**A source with no Arabic in it.** The Buyu' upload was a Turkish definition
list. Supplying the Arabic is legitimate when the underlying wording is the
received one (al-Quduri, al-Hidaya, the Mecelle) — but the manifest must say so
line by line, and where the Turkish and the received wording diverge, the
received wording wins and the divergence is recorded.

**The app is installable.** `prototype/` is a deployable directory:
`reader.html` + `manifest.webmanifest` + `sw.js` + `icons/`. The service worker is
network-first with a cache fallback, so a reader who is online gets the current
text and one who is not still gets the app; bump `CACHE` in `sw.js` whenever
reader.html is rebuilt for a deploy. Registration is guarded by an `https?:`
protocol test, so file:// and the published artifact are untouched.

**Declare the charset.** reader.html had no `<meta charset>` for a long time
because the artifact host supplies one. Served standalone the browser guesses,
and a document that is mostly Arabic decoded as latin-1 is unreadable. The PWA
test asserts `document.characterSet === "UTF-8"` for exactly this reason.

**Bablara nakil is a formal drill, and says so.** The النَّقْل phase carries
ANY verb's root through the babs, class by class (`nakilClass`: sound,
mithal, ajwaf, naqis, gem). Each maker takes (f, a, l, type): sound roots
get the full received table (bablara-nakil-12-wazn.txt) including the
mechanical اِنْنَصَرَ and iftial ibdal (ص ض ط ظ → ط، ز → زد، د ذ → idgham,
via `nakilT` — which composes with the weak classes: اِزْدَ + ادَ =
اِزْدَادَ). Weak classes ride the i'lal rules' own outputs: ajwaf melts to
alif exactly in IV/VII/VIII/X (أَقَالَ، اِسْتَقَالَ) and stays a letter
elsewhere (قَوَّلَ، اِقْوَلَّ); naqis ends every derived mazi in ى
(اِرْتَمَى); the geminate contracts where its twins meet (اِمْتَدَّ، مَادَّ)
but not in II/V (مَدَّدَ); mithal keeps its waw except iftial (اِتَّجَلَ)
and the اِفْـ babs where اِوْ → اِي (اِيجَلَّ) — all of these are the
received table's own rows for وجل. A maker returns null where the
tradition recites no form (naqis/gem IX+XI, non-sound XII/XIII) — no row,
never a guess. Hamzated roots (seat orthography) and doubly-weak lafif
still refuse entirely. The six-bab mujarrad section renders for sound
roots only; derived verbs get the drill through their root with their own
mazid bab highlighted. NFC-normalize every generated form.

**Poetry wears verse dress, driven by data.** A sentence whose token carries
`punctAfter: "•"` renders centered with a ✽ hemistich ornament and takes
`.verse` — no manifest flag, no renderer special case per story. The raw
bullet never reaches the DOM as text; the spoken string keeps it (symbols
are TTS-silent), so playback offsets stay honest.

**The ziyade muhtelife breathes twice.** For derived-bab verbs (`ziyadeExt`,
gated on the wazn's head word) the Muhtelife table appends the recitation's
extension rows from the received أَكْرَمَ model: mimi masdar (= the stored
maf'ul form), binâ-i merre/nev', ism-i mensûb, and the paraphrased tafdil and
taaccüb (مَا أَشَدَّ إِكْرَامَهُ) — all exact templates around the STORED masdar.
A masdar the templates cannot carry (manqus, bracketed, ta-marbuta for the
mensub row) opts out row by row rather than being guessed; ta-marbuta bends
to ت before suffixes (تَوْصِيَتَهُ). The rows carry `ext: true` — the smoke
check that counts the fourteen core forms filters them, and the sarf-note
adds the received rule: no instrument-noun, diminutive or mubalagha from the
augmented babs.

**The Sarf Lab (المُصَرِّف) is a live conjugator, and the corpus is its
judge.** `sarfDerive(cls, form, bab)` conjugates any classifiable root —
Form I through its six babs and the derived II/III/IV/V/VI/VII/VIII/X —
across sound/mithal/ajwaf/naqis/geminate, with the i'lal rules applied
(vowel-melt in ajwaf IV/VII/VIII/X, ى-endings in naqis, contraction in the
geminate, waw-drop in mithal b2/3/6, the iftial ibdal via `nakilT`, and a
general seam-idgham `sjIdgham` that contracts a SAKIN twin only — مَرَرْنَ
keeps its fakk). Passives and Form I masdars are NOT generated: stored-only
and sama'i respectively. `sarfAudit()` regenerates every stored paradigm it
can classify (187 verbs at last count) and the smoke suite fails on ONE
mismatched cell — this audit found and fixed three real data
inconsistencies on arrival (صَانَ، أَمْكَنَ، تَهَاوَنَ missing the كُنَّ-style
idgham). Hamzated and lafif roots are refused with the honest reason. The
UI is `openConjugator` (nav: #conjOpen), state in `conjState`.

**The Sarf Lab knows the corpus's own verbs.** `conjKnownMap()` (lazy,
keyed by `conjKey` = radicals with ى→ي) maps every classifiable root to the
form/bab the texts recite it in, via `sjAttested(m)` — the SAME
wazn-head/bab-model tables the audit uses (`SJ_FORM_OF_HEAD`,
`SJ_BAB1_OF_MODEL`), hoisted so lookup and audit can never disagree. A Form
I attestation outranks a derived one. On every root keystroke
`conjAutoPick()` snaps the controls to the attested form/bab (so typing
حمد answers حَمِدَ of bab سَمِعَ, not the نَصَرَ default); `syncConjSeg()`
keeps a green `●` on the attested buttons even while the learner explores
other babs, and `renderConjOut` shows a green attested hint on the home bab
or a nudge naming the real verb elsewhere (keys conjKnown/conjKnownOther).

**Review scheduling is FSRS-4.5, not SM-2 — the one real ML model in the
web build.** `fsrsNext(s, g)` is a pure step function over the card's
memory state (S stability in days, D difficulty 1–10) with the seventeen
published weights machine-learned from hundreds of millions of reviews
(`FSRS_W`). Desired retention is 0.9 and the 19/81 factor makes
R(S, S) = 0.9, so the next interval IS the stability (`s.ivl =
round(s.S)`), which keeps `deckStats`'s mature threshold and `fmtDue`
untouched. Elapsed time comes from `s.seen`; a card without one is assumed
reviewed on time (elapsed = ivl ⇒ R = 0.9 exactly). SM-2-era cards migrate
on their first FSRS grade: the survived interval floors S, lost ease seeds
D (`5 + (2.5 − ease) × 3.5`). "Again" still requeues in ten minutes and the
post-lapse stability sets the next real interval. `struggleScore` prefers D
when present, falls back to ease. The deck shows `fsrsNote` under the
stats. The smoke suite asserts hard<good<easy previews, first-Good ivl=4
(S0 = w[2] ≈ 3.71), and that a migrated SM-2 card's interval grows.

**The memory model reaches into the games.** `fadingWords(n)` returns deck
word-cards sorted by ascending FSRS retrievability (only cards with real
memory state; R ≥ 0.95 is "fine", not fading). The match round seats up to
3 fading words first (`M.fading`, `.fade-note` banner), `clozeRound` walks
items that gap a fading lex first (each carries `fading: true` and the
cloze question shows a rescue banner, key fadingCloze), and the games hub
puts a `.gd.fade` line under Match and Cloze when any exist (fadingHub /
fadingNote keys). Games are STORY-SCOPED — GLOSSARY is empty in the
library, so any test touching them must open a story first.

**The sheet names the form in the text.** `findFormInParadigm(morph,
surface)` finds which paradigm cell a token is: `formCandidates` peels
vocalized proclitics (وَ فَ سَ لَ لِ بِ, up to two) and enclitic object
pronouns (restoring the 3pl alif: رَأَوْهُ → رَأَوْا), then an EXACT-NFC pass
runs before the bare-letters pass so قَضَيْتَ ≠ قَضَيْتُ; governed forms
(mansub/majzum) are checked after the three tenses so يَرْضَى resolves as
mudari. The Word tab shows an `.intext` block — surface form + cell name
(`formCellLabel`, AR/EN/TR via CELL_TENSE/CELL_PERSON[14]/CELL_PERSON_AMR)
+ the meaning of the FORM (`formMeaning`): TR imperative = gloss stem
minus -mek/-mak («affet!»), TR past fully generated by `trPast` (vowel
harmony + devoicing after fstkçşhp; duals get an «o ikisi/ikiniz»
prefix); EN only trusts its imperative — everything else shows the label
and stays silent rather than guess. The sarf tab auto-opens the tense
holding the tapped form with the cell lit by INDEX (conjTable's 4th arg
hlIdx — string matching alone cannot see through a clitic waw), and
`sarfUserPick` stops the auto-jump from overriding an explicit tense
click (reset whenever a non-sarf tab opens).

**The Aded engine is the number chapter as a machine.** `class AdadEngine`
(static tables + `parts/name/idafa/phrase`) composes 1–9999 exactly as the
uploaded أسماء عدد worksheets do (research/sources/esmai-aded-worksheets.txt
— the smoke suite replays the transcribed handwritten table against
`name()`, bare-letters compare): thousands، hundreds، UNITS، tens, joined
by و, hundreds multiples joined (ثَلَاثُمِائَةٍ). `phrase(n, noun)` applies
the ma'dud rules by the LAST part: 1–2 adjective-agree, 3–10 polarity +
jam' majrur, 11–99 mufrad mansub tamyiz, hundreds/thousands mufrad majrur
idafa (duals drop the nun: مِائَتَا كِتَابٍ), and 101-type numbers repeat
the noun (مِائَةُ كِتَابٍ وَكِتَابٌ). `ADAD_NOUNS` is a small hand-verified
set (half feminine; دَرَاهِمَ diptote). UI: the Sarf Atölyesi sheet now has
lab tabs (conjState.lab, `renderLabBody`) — Sarf Lab | Aded Lab
(`renderAdadOut`). The numbers game (`startAdadGame` via runQuiz, hub id
gAdad) generates every round from the engine with the CLASSIC drill
errors as distractors (polarity flip, wrong tamyiz shape); the smoke
suite asserts every generated round is well-formed.

**The i'lal chain recites asl → rule → result.** `ilalSteps(cls, bab,
mazi, mudari)` (Form I, weak classes only; sound verbs return null) builds
the Maksud-style derivation: ajwaf qalb-alif + naql, naqis qalb (bab≠4) +
hadhf-of-damma (bab 4 gets qalb in the mudari instead), mithal
waw-between-ya-and-kasra hadhf, geminate naql+idgham — each step
{asl, now, ar, en, tr}. Rendered by `ilalHtml` in the word sheet's sarf
tab (via `ilalChain(entry, morph)` — needs the sema'i bab from
sjAttested) and in the Sarf Lab output for Form I. Sources:
ilal-kaideleri-turkce.txt + maksut-sarf-ottoman.txt. FSRS gained a
user-facing **target-recall control** (state.retention 0.85/0.9/0.95,
qissa-retention key, `fsrsInterval(S)` = S·(81/19)·(r⁻²−1) — at 0.9 it
degrades to S) shown under the deck stats. RootFinder.peel understands
MASDAR shapes (استفعال، افتعال with ibdal، انفعال، إفعال with plain-alif
hamza، تفعيل، مفعال، مفاعل، فعيل، فعال) tried before verb skeletons.

**The Root Finder digs corpus-first.** `class RootFinder`: `fromCorpus`
scans a lazy index of every stored paradigm with `findFormInParadigm`, so
a typed form answers with the stored root AND the semai facts (Form I bab
shows ONLY because the corpus carries it — never computed). Only when
the corpus is silent do `candidates` (clitic + person-affix peeling) and
`peel` (pattern table, longest-first: است/مست/ست، من/ان، iftial with its
ibdal reversed ط←ت after صضطظ and د←ت after زدذ، مت/ت، أ، فاعل، then
bare ن) run; hidden weak radicals render as و/ي with an honest note. The
nav button is now **Atölye/Workshop** (key conjBtn) with THREE lab tabs:
Sarf | Aded | Kök Bulucu (conjState.lab: sarf/adad/jadhr). The reader's
sarfDerive also gained the **Form IV geminate** branch (أَحَلَّ يُحِلُّ,
jazm bil-fath) — added because the Sulh story's أَحَلَّ made the audit
demand it.

**The role layer paints i'rab, it never re-derives it.** `class RoleEngine`
maps each token's STORED `irab.ar` line to one of eight functional roles
(fail incl. naib, maful incl. mustathna/munada, mubtada incl. ism of the
sisters, khabar, mudaf ilayh, hal/tamyiz/zarf, tabi, jarr) by regex over the
NFC text — the analysis stays editorial, the engine only reads it. The 🎨
header button (#roleToggle, qissa-roles key, state.roles) sets
body.role-mode: words grow 3px colored underlines from `data-role` (stamped
in renderStory) and `updateRoleMode` builds a #roleLegend in the header in
the UI language. A token whose i'rab names no role stays unpainted — no
guessing. The palette is deliberately MUTED (one soft-chroma family in
--role-* CSS vars, 2px underline) — full-strength primaries proved tiring over a
page of text; keep any new role color at the same chroma. Order matters in ROLES: mubtada's `اسْمُ «` must come after fail
so نَائِبُ الْفَاعِلِ wins, and jarr is last because مَجْرُور appears
inside mudaf-ilayh lines too.

**The Avamil-100 panel teaches only what the source has taught it.** The
grammar index opens with a card for Jurjani's count (`AVAMIL100` in the shell,
from research/sources/avamil-curcani-slides.txt): 100 = 91 semai in 13 kinds +
7 kiyasi + 2 manevi, with KIND ONE — the seventeen jarr letters — walked letter
by letter with the meanings each adds and one example. Every letter links to
the registry note that already teaches it (huruf-jarr / huruf-jarr-nawadir),
so the Jurjani count and the Birgivi tables stay one doctrine. Kinds 2-13 are
NOT guessed: the panel says they await the deck's later parts and points to
the Birgivi tables meanwhile. When those parts arrive, extend AVAMIL100 rather
than writing a parallel structure.

**The Mizan weighs on the engine, not on templates.** `class WaznEngine`:
a corpus form's wazn is computed by conjugating the root ف ع ل ITSELF through
the same form, bab and cell with sarfDerive (يَسْتَعْمِلُونَ → يَسْتَفْعِلُونَ), so every
harake is earned; for a weak verb this yields the wazn بِحَسَبِ الْأَصْلِ
(قَالَ → فَعَلَ, flagged `asl:true`) — the madrasah's answer, with the i'lal
chain explaining the surface. Rules path: the RootFinder peel pattern that
found the root already names the wazn. Fourth Atölye tab (conjState.lab
"mizan"). A sema'i-only entry (no sjAttested) answers honestly that its wazn
is stored, not derived.

**The ability model is Elo, and the coach only reads.** `class EloModel`:
one rating per area (vocab/sarf/nahw/adad, qissa-elo key), items rated
900+level·100, update R += K·(result − expected) — logistic IRT fitted one
observation at a time, no model file. Every runQuiz game declares `area` and
`lvl(it)`; the harness posts one observation per answer. `targetLevel` inverts
the expected-score curve at 0.75 (desirable difficulty); clozeRound ranks its
pool by closeness to that band AFTER fading words take their reserved seats
(FSRS outranks Elo). The deck's coach card (`coachPlan`/`coachHtml`) is a
deterministic read of the whole state — dues beat fading beats weakest-area
game — every sentence traces to a number; nothing is generated.

**A user correction becomes doctrine, not just a patch.** The reader caught
s18's waw (wasiyyat-abi-hanifa-L2) glossed as عاطفة when it is حالية — the fix
went into the token AND into a new note (`anwa-al-waw`: atif, haliyya,
isti'nafiyya, qasam, ma'iyya, plus the pronoun waw), anchored to that very
sentence, with the «while/إذ»-substitution test and the جاء الطلاب والمعلمَ
nasb-betrays-ma'iyya mistake. When a correction lands, always ask what NOTE
teaches the distinction — and anchor it where the mistake lived. A smoke check
pins s18's i'rab, its two jumal rows, and the note's anchor.

**The Tahlil tutor walks, the role game samples.** `tahlilSentences()` groups
roleItems by sentence (object identity — sentence ids repeat across stories)
and keeps sentences with 3+ askable tokens, sorted by position; `startTahlil`
then walks ONE sentence in order like a hoca, revealing each stored i'rab after
the learner answers. Elo area nahw; the coach's nahw action now points here.

**Covers are woven, not stored.** `coverArt(st)` hashes the story id into an
eight-point-star SVG lattice in the level's muted colour — data URI, no asset.
Trap: encodeURIComponent leaves apostrophes, and the inline style wraps the URI
in url('…') — replace ' with %27 or the style dies silently.

**The Ism engine keeps the Root Finder's oath: table before rule.** USER
RULE (2026-07-31): a silent final ه turns waw in the nisba — رِيزَه →
رِيزَوِيّ (Rizevî), the Ottoman place-name convention. Radical-ha words
(فقه → فِقْهِيّ، وجه → وَجْهِيّ) are shielded by SEMAI_NISBA, which answers
first. Speed rule: the lab inputs are debounced (140ms) and RootFinder.find /
WaznEngine.of are memoized (400-entry Map) — analysis runs when the typist
pauses, and repeat lookups never re-walk the corpus. Smoke checks that FILL a
lab input must waitForTimeout(260) before reading the output.
`class IsmEngine` (fifth Atölye tab, conjState.lab "ism"): tasgir puts three
sound letters on فُعَيْل (ta re-attached), four on فُعَيْعِل, the فَاعِل alif
turns waw (شَاعِر → شُوَيْعِر), a weak last letter melts into the diminutive ya
— shapes beyond the classical patterns REFUSE rather than guess. Nisba drops
the ta and adds the doubled ya; maqsur alif and mamdud hamza turn waw; and
SEMAI_NISBA (مَدِينَة → مَدَنِيّ، قُرَيْش → قُرَشِيّ، دُنْيَا → دُنْيَوِيّ…)
answers before any rule runs. Extend the table, never special-case the rules.

**The Harake Auditor is the musahhih with no dictionary.** `class
HarakeAuditor` (reader) and `audit_harakat` (validate_content.py) apply only
what orthography itself forbids: no initial sukun/shadda (except بْنُ between
names — alif elided, the received exception), no vowel on a medial plain alif
(word-initial alif+vowel IS hamzat al-wasl's spelling), one vowel per letter,
no shadda+sukun, tanwin only word-final (or before final ا/ى), no two explicit
sukuns meeting. The corpus swept clean on first run except the two legit بْنُ.
KEEP THE TWO IMPLEMENTATIONS IN STEP — the validator warns, the Analyzer flags.

**Elo is two-sided now.** When a game names its item (cfg.itemKey — a lex, a
paradigm cell), the ITEM's rating learns opposite the learner (K_ITEM=16,
qissa-elo-items, level stays the prior). Misses push an item up, hits pull it
down — online IRT on both sides. Daily snapshots (qissa-elo-hist, 90 days)
feed the coach's per-area sparkline.

**AUTHORING.md is the content-ops contract.** Chapter loop, new-story
scaffold, release.py, the honesty rules, and the where-knowledge-goes table.
Content drops for weeks and months route through it — keep it current.

**The Analyzer reads signals, it does not claim i'rab.** v2 is the İZHAR
LAYER: every amil the book lists pushes what it EXPECTS to govern into a
queue that following open-class words consume — inna's six sisters push
[ism-nasb, khabar-raf], kana's push [ism-raf, khabar-nasb], the fifteen
jawazim (incl. the conditional NOUNS مهما متى أين أنى حيثما إذما أي) push a
verb, a verb's own promise is the fa'il. Clitic segmentation shows its work
(بالقلم → ب + القلم؛ كتابه → كتاب + ه with the pronoun naming itself mudaf
ilayh/maf'ul by host kind); ب/ل/ك peel ONLY before ال or a particle — the kaf
of كتاب is a radical (a greedy peel split كتابه; the smoke check pins it).
The idafa pass reads bare-noun + definite-noun as mudaf/mudaf-ilayh; ال+tanwin
on one word raises a ⚠ contradiction flag. Bare أن is labeled ambiguous
(masdariyya before a verb, anna before a noun) — stripping erases the shadda. `class
SentenceAnalyzer` (Atölye tab "jumla") parses ANY pasted Arabic with no
stored data: the closed classes (its PARTICLES table) are identified as
KNOWLEDGE; word kinds are read off morphology (article/tanwin/ta-marbuta →
noun, mudari prefix → verb?) and marked as guesses; sequence expectations
(jarr→majrur, jazim→verb, ya→munada) ride one token forward; RootFinder and
WaznEngine dig root and wazn. A joining و/ف is peeled ONLY when the remainder
is a particle or definite — a radical waw (وَصِيَّة) keeps its letter, and the
smoke check pins that. The output footer points to the stories for real i'rab.

**Corpus-first applies to the peeled skeletons too.** RootFinder.find now
tries fromCorpus on every candidate (clitic-stripped) BEFORE any peel rule —
ورجع must find the stored رَجَعَ, not a pattern guess. And when the corpus
answers, the Analyzer upgrades the word to a CERTAIN verb with its cell named
(a bare mazi wears no prefix; only the corpus can call it). The Analyzer also
opens with Qawa'id al-I'rab's first question — jumla ismiyya or fi'liyya —
looking through joining و/ف and the introducers to the first weight-bearing
word (kana ⇒ fi'liyya, inna ⇒ ismiyya).

**The IrabModel is trained at runtime from the corpus itself.** `class
IrabModel` (naive Bayes, 8 roles, Laplace-smoothed, softmax output) walks
STORIES on first call and labels every token with `RoleEngine.of` — the
~1500 hand-i'rabed tokens ARE the training set, so every authored chapter
makes the model better with zero extra work. Features come from surface
orthography (ال، tanwin, ة, enclitic pronoun, position, prev = verb/jarr/
noun). TRAIN AND PREDICT MUST SHARE ONE FEATURE DEFINITION: `prev` is
non-sticky in both (a non-jarr particle resets it to null) and `features()`
NFC-normalizes before touching the string — an orchestrated review caught
train() keeping a sticky prev while the Analyzer call site computed it fresh,
which silently skewed every after-X count. Its votes render only as the
labeled `.ml-vote` chip (`🧠 model: fâil %62`) — statistics, never claimed
as i'rab.

**The hoca walkthrough asks the madrasah's questions.** `hocaChain` renders
the user's uploaded style — «Tektub = o kadın yazmadı, kim? İmre'etün = bir
kadın, kime?» — as gloss + the question the NEXT word answers: a verb asks
ROLE_Q.fail (kim?), a jarr letter asks its own JARR_Q (ل → kime/ne için?),
and when only the model suggests a role the question wears the model's badge
(`🧠 … (tahmin)`) — an unlabeled statistical question would violate the
honesty contract. `roughGloss` builds the «İmre'e kitabet etmedi bir mektub»
bridge line: corpus gloss first clause, else the verb's REALIZED MASDAR
(`realizeMasdar` — MASDAR_SHAPE covers forms II–X; Form I masdars are semai,
so refuse), else the bare Arabic. Everything user-typed that reaches
innerHTML goes through `escapeAttr` — r.w and the seg join in both hocaChain
and the Analyzer table (the review's third confirmed finding was exactly
these raw interpolations).

**Fable orchestrates; lighter models execute.** Standing user directive: the
crucial passes (adversarial verification, anything shipping) run under a
Fable-driven Workflow; mechanical finder/reader stages delegate to
sonnet/haiku. Precedent: the v71 pre-ship review (3 finder lenses on
sonnet/haiku + Fable verifiers) returned 3 confirmed defects — train/predict
feature skew, unlabeled ML questions, raw-interpolation XSS — all fixed
before commit. Reviews that only confirm are wasted; wire the findings back
in before shipping.

**The full Nasafi matn is on the shelf now.** The project owner supplied the
COMPLETE matn of al-'Aqa'id al-Nasafiyya (research/sources/
aqaid-nasafi-matn-full.txt — its bracketed [أي ...] glosses are the
supplier's notes, not matn). aqaid-ahl-al-sunna continues from it chapter by
chapter via tools/authoring/author_aqaid_ch5.py-style ADD scripts (load
existing package, write the new chapter, merge glossary/morph, bump
version — idempotent). Sentences are VERBATIM CONTIGUOUS SPANS re-vowelled
against the received text; stopping early at a list boundary is allowed,
skipping words inside a span is not. Next in the matn after ch5: takwin,
ru'yat Allah, khalq al-af'al, qada/qadar, sam'iyyat (qabr, mizan, hawd —
ch1 already has the hawd hadith), iman, the prophets, the four caliphs.

**After a governor of verbs, the mazi parse is impossible.** The Analyzer's
jazm/nasb expectations carry verb:true; when the governed word is ta/ya-
initial the İzhar contract outranks WaznEngine's pattern guess: a Form V/VI
mizan is retired (detected on the SKELETON — NFC reorders fatha before
shadda, so a literal تَفَعَّ regex never matches; test stripAr prefix +
shadda instead) and the word is labeled a governed mudari whose ta is the
person prefix. The corpus gets one more try on the stem behind the prefix.
The smoke check pins لم تكتب.

**The drill garden feeds the model.** content/samples/jumal-al-tadrib
(tools/authoring/author_tadrib.py) is a FREE 3-chapter package of ORIGINAL
textbook sentences in the owner's question-chain style («Gâle = dedi, kim?»)
— fi'liyya, ismiyya, and inne-vs-enne. Its second job is stated in its own
attribution: every token is a labeled training example for the runtime
IrabModel, so growing the drill garden IS growing the training set. The
i'rab lines ride shared template helpers (FAIL/MAFUL/MUBT/KHAB…) so the
madrasah wording — and therefore the RoleEngine labels — stay uniform.

**The hamza of ان reads by position (Qatr al-Nada).** Note `inna-am-anna`:
kasra sentence-initially, after the QAWL verbs (قَالَ إِنَّ — speech is
quoted whole; the books except qawl from the after-a-verb fatha) and after
the oath; fatha where the clause construes as a masdar (عَلِمْتُ أَنَّ =
عَلِمْتُ قُدْرَةَ اللهِ; Turkish -dığını). The Analyzer teaches the same
rule live: for bare ان/أن it walks BACK OVER NOUN ROWS to the nearest verb
(the fa'il sits between قَالَ and إِنَّ; a particle wall stops the walk).
Dart gate: gameSeeds is a MAP ({"spotTheError": true}), never a list — the
Flutter model casts it.

**RoleEngine blanks sarf phrases before matching.** «اسْمُ فَاعِلٍ مِنْ
رَكِبَ» inside a hal's i'rab must not label the token fail — the role
regexes run on a string with /اسْم[ُِ]\s*(الْ)?(فَاعِل|مَفْعُول)\S*/
blanked. Keep the syntactic claim BEFORE any sarf commentary in authored
i'rab, and never let a bare role-word (مَفْعُول as a wazn mention) trail
after it. Corpus growth also upgrades old heuristics: once kataba joined
the drill garden, لم تكتب became corpus-certain and the governed-mudari
note rightly stopped firing — the smoke check accepts either outcome.

**The drill garden is five chapters now** (v1.1.0, 40 sentences / 158
tokens): fi'liyya, ismiyya, inne-vs-enne, the OBJECTS FAMILY (maful mutlaq/
fih/lah, naib al-fail, munada+amr) and SHART/ISTIFHAM (in + man with the
iltiqa-sakinayn kasra, idha without jazm, la nahiya, lam of command, hal/
madha/ayna). Aqaid runs to ch6 (takwin vs the mukawwan — the kasra/fatha
minimal pair مُكَوِّن/مُكَوَّن — and ru'ya with فَيُرَى teaching naib
al-fail on a passive naqis). IrabModel now trains on 1000+ labeled tokens.

**The tenth game is the Hamza game** (`hamzaItems`/`startHamza`): sweeps
ALL STORIES for stored إِنَّ/أَنَّ tokens (shadda required — إِنْ/أَنْ are
different particles), blanks them, and lets Qatr al-Nada's rule pick; the
stored i'rab line is the answer key and the extras button opens the
inna-am-anna note via openRef. Games that teach a NOTE's rule should link
the note in extras. Design wave 6: game cards wear .gi emblems and
nth-child spine colors from the role palette; Atölye tabs carry ::before
emblems (the smoke [data-lab] selectors still match); :focus-visible gets
the accent ring globally.

**Focus mode fades, never collapses.** body.focus-hide (scroll down past
260px → hide, scroll up or near top → show) fades the reader header via
opacity+transform. It KEEPS ITS SPACE: the first version collapsed max-height
and the layout shift under a mid-scroll tap made clicks miss (Playwright
caught it as an unstable-element timeout — real users would feel the same).

**The verb card is a drill, not a flashcard.** `verbPrompt` returns
`{qs: [...], lemma}` — `VERB_DRILL_QS` (3) cells per round, stride `len/n`
over the Muhtelife so the picks are spread AND distinct, deterministic per
round (reps + pick). Asks show from step 0, answers at step 2, one grade for
the round. The smoke check asserts 3 distinct answers, each a real cell of
that verb's own paradigm.

**The registry is audited against the canon, not just against itself.**
`check_canon.py` holds the madrasah's own lists (from the Turkish table
transcriptions in `research/sources/`) and maps each item to the note that
teaches it. 81/81 covered — the audit is closed. The tail of Birgivi's twenty harf-i cer is taught
as ONE note (`huruf-jarr-nawadir`) because each rare letter is defined by its
restriction, not by a story appearance; ism fa'il and ism maf'ul as GOVERNORS
are `ism-fail` / `ism-maful`, anchored to real tokens (مُوَدِّعًا، عَامِلًا،
الْمُخْرَجُ، مَشْرُوطٌ). The last two gaps fell to kafiya-internet-digest.txt: the inna-table الا is
أَلَا التنبيه (`huruf-tanbih` — it precedes إِنَّ but governs nothing), and
Manayı Fiil is the hal-governor with verbal force but no verbal form
(`mana-al-fil`, هذا زيد قائما). Two mapping
rules to keep: a particle counts as covered only if a note names it AND its
government, and never stretch a neighbouring note over a gap — write the note
or leave the TODO.

## Grammar sourcing

Emsile, Bina, Maqsud, Birgivi's Awamil, Izhar, al-Kafiya (Ibn al-Hajib), Qatr al-Nada,
and — for the balagha group — al-Qazwini's Talkhis and the ʿAlaqat treatise.

The registry has **four** groups now: sarf, nahw, awamil, balagha. Adding a fifth
means adding it to `NOTE_GROUPS` in the validator and to `REF_GROUPS` in the
builder; nothing else knows about the list.

**Balagha is complete in all three of its divisions**: maani (`qasr`), bayan
(`tashbih`, `istiara`, `kinaya`, `haqiqa-majaz`) and now badiʿ — `tibaq`,
`muqabala`, `muraat-al-nazir` from the maʿnawi embellishments, `jinas` and `saj`
from the lafzi. Two things govern how badiʿ was authored, and both matter if it
grows:

- **Anchor to what the corpus actually has, and say so when it doesn't.** The
  stories are prose definitions and counsel, so they are full of tibaq and of the
  ishtiqaq kind joined to jinas, and thin on jinas tamm and on saj'. The notes
  teach the full taxonomy from the Talkhis but only *anchor* what is really there;
  the book's own Qur'anic citations carry the rest as unsourced examples.
- **The near-miss is the lesson.** «الْعِلْمُ بِلَا عَمَلٍ كَشَجَرٍ بِلَا ثَمَرٍ» sounds like sajʿ
  and is not one — the two fawasil end on different letters. It is filed as a
  `commonMistakes` entry on `saj`, not quietly anchored. Same for the tibaq /
  muqabala boundary, which `smoke_test.js` enforces structurally: no single token
  may carry both notes, because one of them would be wrong.
Transcriptions live in `research/sources/` with provenance in its README. Teach from
the books' own categories and wording — but generalize; do not overfit to one book's
example sentences. The awamil/izhar shelf now holds three layers that must agree:
`avamil-curcani-slides.txt` (Jurjani's count — 100 amils: 91 semai lafzi in 13 kinds
+ 7 kiyasi + 2 manevi, opening with the 17 jarr letters and their MEANINGS),
`izhar-tercume-full.txt` (Birgivi's full İzhar in Turkish — the kıyasi-9/semai/manevi-2
split the registry's awamil group follows) and the Q&A pair — `izhar-sual-cevap.txt`
(Ottoman script, reliable Arabic) with `izhar-sual-cevap-tafsilatli.txt` (modern
Turkish; its Arabic is mojibake from the PDF font — quote ONLY its Turkish, and
take Arabic wording from the tercume or Ottoman files instead).

## Process

- Branch: `claude/arabic-app-research-ozd58s`. Never push elsewhere.
- No PR unless explicitly asked.
- `git push -u origin <branch>`; retry only on network errors (2s/4s/8s/16s).
- Every story manifest carries `reviewStatus: pending-scholarly-review`. Keep it there
  until a human scholar signs off.
