# Qissa — working notes

An Arabic graded-reader app (DuChinese-shaped) built on classical Islamic texts,
with madrasah grammar attached to every word. Target: iOS + Android launch.
Everything here is the *why*; the code is the *what*.

## Where things live

```
content/
  grammar/          78 global grammar notes — one JSON per topic, shared by every story
  i18n/irab-tr.json Turkish translation memory for i'rab strings, keyed by the English
  samples/<story>/  manifest.json · chapters/N.json · glossary.json · morphology.json
  user-uploads/     same shape; deeds-are-by-intentions ships its own standalone reader.html
  catalog.json      generated — index of every package (level, access, chapter count)
prototype/reader.html   the whole app: shell + generated data block
tools/
  validate_content.py   the quality gate — run it before anything else
  build_prototype.py    splices JS constants between // __DATA_START__ / // __DATA_END__
  smoke_test.js         49 browser checks over file:// (Playwright)
  pwa_test.js           9 checks over http:// — manifest, icons, SW,actually-offline
  make_icons.js         regenerates prototype/icons from one HTML source
  check_canon.py        audits the registry against the madrasah's own lists
                        (20 harf-i cer, 8 inna sisters, 15 jawazim, 13 mansubat…)
                        — coverage report, not a gate; --strict only checks that
                        every mapped note id really exists
  check_irab_tr.py      finds i'rab strings with no Turkish yet
  check_i18n.py         fails on ANY user-visible string that has en but no tr
research/sources/       transcribed madrasah texts + README on provenance
```

Eleven stories, Levels 1–6. Aqaid runs to four chapters, the Abu Yusuf wasiyya to five; Kitab al-Buyu and Kitab al-Kaffarat are the fiqh texts. Grammar notes are **global**: a note authored once shows
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
- **Sentence i'rab sheet**: the إعراب button on each sentence opens the whole sentence
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

**The registry is audited against the canon, not just against itself.**
`check_canon.py` holds the madrasah's own lists (from the Turkish table
transcriptions in `research/sources/`) and maps each item to the note that
teaches it. 79/81 covered. The tail of Birgivi's twenty harf-i cer is taught
as ONE note (`huruf-jarr-nawadir`) because each rare letter is defined by its
restriction, not by a story appearance; ism fa'il and ism maf'ul as GOVERNORS
are `ism-fail` / `ism-maful`, anchored to real tokens (مُوَدِّعًا، عَامِلًا،
الْمُخْرَجُ، مَشْرُوطٌ). The two remaining TODOs are honest: the الا of the inna
table (identity unclear in the transcription) and Manayı Fiil. Two mapping
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
example sentences.

## Process

- Branch: `claude/arabic-app-research-ozd58s`. Never push elsewhere.
- No PR unless explicitly asked.
- `git push -u origin <branch>`; retry only on network errors (2s/4s/8s/16s).
- Every story manifest carries `reviewStatus: pending-scholarly-review`. Keep it there
  until a human scholar signs off.
