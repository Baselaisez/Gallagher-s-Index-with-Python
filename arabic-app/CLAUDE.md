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

**An imperative on a sukun is MABNI, never majzum.** The app read `أُكْتُبْ` as
"jazm by sukun" — a reader caught it. There is no jazm without a jazim, and no
jazim is present; the sukun is the *bina* of the amr. `IrabSign` discriminates
on the OPENING vowel, not on the ending: `[اٱأإ][ُِ]` with a bare stem of three
or more is an amr, so `لَمْ أَكْتُبْ` (fatha on the prefix) stays majzum. Its
hamza is written as a WASL: `اُكْتُبْ`, not `أُكْتُبْ`, and the app says so.

**A mizan is not the name of a bab.** It is the word with its root letters
stood in ف ع ل and everything else left exactly where it is — augments,
sukuns, harakat, the ta marbuta. That is mechanical, so `WaznEngine.mizan()`
computes it rather than looking it up: قَادِرٌ → فَاعِلٌ, مُسْتَغْفِرٌ →
مُسْتَفْعِلٌ, مَكْتُوبَة → مَفْعُولَة. Before this a noun borrowed a verb's bab
and قَادِرٌ came out as فَاعَلَ. It declines where it cannot be sure: a weak
root whose letter has been turned no longer stands in the word (قَالَ shows no
و — that is the IlalEngine's business), and any surviving letter outside
سَأَلْتُمُونِيهَا plus the ta kills the scan. **A word wearing ال, tanwin or the
ta cannot be a verb, so if the scale declines, drop the wazn rather than leave
a verb pattern standing over a noun.**

**`GameFactory` is the one declaration of what a game needs.** The supply map
used to be a local `const` inside `openGames()`, so the question "what can THIS
story actually play?" could not be asked from anywhere else — least of all from
a test. It is now a class: one entry per game carrying its id, discipline,
emblem, `supply()` and `min`. The hub renders from it (and shows the real item
count on each card), and `GameFactory.audit()` scores **every story against
every game**. The suite gates on it: a story must reach **9 of the 13
content-gated games on its own content**, so a new upload cannot arrive
underplayable without failing the build. `gCloze` is marked `needsProgress` and
excluded from that floor — it quizzes only sentences the learner has READ, so
zero on a fresh profile is correct, not broken.

`forStory()` saves and restores `CUR` and `GAME_SCOPE_FALLBACK` in a `finally`:
it must be able to score a story without opening it and without disturbing what
the reader is looking at. Writing it found a real gap — `gameGlossary()`
returned the render-time global `GLOSSARY`, which is empty until a story is
*drawn*, so anything reasoning about a story it had not opened saw no lexicon
at all. It falls back to `CUR.glossary` now.

**A multiple-choice round is only as hard as its wrong answers.** İbare drew
three RANDOM sentences, and a random sentence gives itself away with no Arabic
read at all: different length, no shared words, plainly about something else.
`DistractorEngine.near()` scores the pool for CLOSENESS — shared vocabulary
(Jaccard, weight 3), length (2), number of amil pairs (1), same kind of clause
(1) — and draws from the top of it. Measured on 338 items: the answer is
uniquely the longest or shortest option **41.1% → 4.1%** of the time, and the
mean length gap falls from 2.7 words to 0.39. Both are gated.
**Never call `SentenceAnalyzer.analyze()` inside a scorer.** The first draft did,
for both sides of every comparison — O(pool) analyses per question, seconds to
draw one round, and it hung the measurement outright. The sentence type is
already on the corpus tokens' own `pos`; read it there, once, when the pool is
built.

**A fixed element cannot be cleared by body padding.** The thumb bar is
`position: fixed; bottom: 0` and so is `.sheet` — so the sheet's last row sat
UNDER the bar, unreachable by any amount of scrolling. «Save to flashcards» was
rendered, in the DOM, and invisible. `body { padding-bottom }` does nothing for
it, because a fixed element is not in the body's flow; the clearance has to go
on `.sheet-inner`, inside the same media query that shows the bar. One rule
fixes every sheet in the app. **The smoke suite now walks all four sheets at
390×844 and fails if any button, link or input ends below the bar** — the
reported bug was one instance of a whole class, and the class is what is
guarded. When writing that check: **wait for the sheet's transform to finish**
before measuring, or every child reads as below the bar because the sheet is
still translated off-screen.

**Derive on the card, never store on it.** A word card's answer side shows its
root, its computed scale and the offices that scale can hold — all computed at
RENDER from the card's lex, so nothing was added to the schema and every card
already in a learner's deck gained it without a migration. Two guards, both
earned by getting it wrong first:
- **The root comes from the card's own glossary entry, never from the peeling
  rules.** `RootFinder.find("مَكْتُوب")` returns ك و ب, and feeding that to the
  scale produced **مَفْتُعل — a shape that does not exist**. A wrong wazn on a
  flashcard is worse than none.
- **The offices are shown only when the learned tagger AGREES with the computed
  scale.** Two independent answers matching is the bar for putting a third
  claim on top of them.

**Feed the model the ENGINES' verdicts, but ablate every family.** `IrabModel`
learned from letters and neighbours only. Four rule-derived feature families
were built and measured leave-one-story-out on 2,801 labelled tokens, and
**three of the four were noise or worse**:

| family | held-out top-1 without it | verdict |
|---|---|---|
| the noun tagger's wazn | 49.6 vs 48.9 with | **HURT** — dropped |
| the idafa test (`idafa-head`, `next-al`) | 49.3 / 68.3 vs 48.9 / 67.9 | **HURT** — dropped |
| «preceded by a bare noun» | 48.6 vs 48.9 | noise — dropped |
| **the GOVERNOR** (`gov-jarr`, `gov-verbal`) | 47.8 vs 48.9 | **+1.1 / +1.0** — kept |

Final: **48.7 / 67.1 → 49.8 / 68.1** on the ablation harness, 50.7 / 68.7 in
the app's own 16-fold crossVal, and both floors were raised to hold it.

That the governor is the one to survive is not luck — it is the **Awamil
doctrine itself**: what a word IS depends on what governs it. The model could
already see `after-verb` but was blind to a masdar or a participle doing the
same work, which is exactly what `TaalluqEngine.VERBAL_WAZN` knows. **More
rule-derived features is not better; the right ones are.** Re-run
`scratchpad/irab_ab.js`-style leave-one-story-out ablation before adding any.

**Two classes of engine, and never blur them.** Some questions the surface
settles completely and the engine's answer is EXACT — `IdafaEngine.build()`,
`WaznEngine.mizan()`, `IlalEngine.derive()`, `AdadEngine`. Others the surface
cannot settle even in principle, and the honest deliverable is a ranked
SHORTLIST with the signal that raised each — `MaEngine`, `WawEngine`,
`TaalluqEngine`, both taggers. Claiming a single verdict for the second class
is the failure mode to guard against; the app's promise there is that the right
answer is *in the list* and that the reason is stated.

**`TaalluqEngine` — Qawa'id al-I'rab bab 2.** Every jarr-majrur and every zarf
attaches to a verb or to something carrying a verb's meaning; nothing hangs in
the air, and an i'rab that names a jarr-majrur and stops has not finished. The
rule the corpus confirms is **الأقرب أولى بالتعلق** — the nearest governor wins,
which is why عَنْ حَوْزَةِ in Aqaid 23 hangs on the masdar الذَّبِّ beside it and does
not reach back past it to قَادِرًا. Measured against the corpus's 111 answerable
hand-written attachments: **33.1% → 48.0%**, and a five-way ablation confirmed
nearest-wins beats verb-first (37.8%) and beats dropping the model (37.8%).
Every point came from a correctness fix; none from tuning. Four things it must
get right and now does:
- **A majrur is not the letter that governs it.** The note test used to match
  «AFTER a jarr letter — likely majrur», so every majrur noun was read as a
  jarr letter and answered for a question it never asked.
- **Ask the glossary which nouns carry a verb's meaning.** ذَبّ is a masdar on
  فَعْل, a shape ten thousand ordinary nouns wear; no pattern test can find it,
  but the glossary's own gloss says «(masdar)» and `nounIndex()` now carries
  that as a `verbal` flag.
- **لِلْخَلْقِ is لِ + الْخَلْق** with the article's alif swallowed — the letter is
  there, it is simply not separable by eye.
- **A jarr letter fused to an INDEFINITE noun** (بِقَائِمٍ, بِعِلْمِكَ) is never
  peeled by the proclitic pass, so it has to be recognised here — guarded like
  the waw, since a lemma opening with the same letter means it is RADICAL
  (بَيْت, بَاب, لَيْل, كِتَاب). Worth 8 points on its own.

The remaining 60% is not noise to be tuned away: the corpus often attaches a
phrase across a clause boundary the analyzer is not holding, exactly as the
opening waw's antecedent lies in the sentence above. **Do not chase that number
by weakening the rule** — the ablation already shows every looser variant is
worse.

**Rank a many-faced word on MEASURED evidence, not on the books' order.**
Ibn Hisham gives the waw eight faces (Qawa'id al-I'rab, bab 3): isti'naf, hal,
atf, maf'ul ma'ah, jam', qasam, rubba, zaid. The first `WawEngine` reasoned
them out from the books and scored **36.9%** against the corpus's own rulings —
*worse than always answering "atf"* (68%). Grading it against the 211 waws a
human has already judged in the library taught three things reasoning had not:
- **A hal waw never opens a sentence.** Not once in 211. Offering it at the
  head is simply wrong, so the hal branch is gated on `i > 0`.
- **Mid-sentence the waw is atf five times in six.**
- **At the head the question is genuinely OPEN**, because what a ma'tuf joins
  to lies in the sentence BEFORE, which the analyzer is not holding. Reading
  "nothing precedes it" as evidence of isti'naf is what cost 31 points; it is
  evidence of nothing but that the antecedent is out of frame. The engine now
  offers atf and isti'naf together there, says exactly that, and the kernel
  pushes it into `undecided`. **70.6% → 71.6% top-1, 98.1% top-2.**

The lesson generalises: for a word with many faces the app's promise is a
correct SHORTLIST, not a correct verdict, and the shortlist is what to measure.

**A separable letter and a radical one are different words.** `WawEngine.separable()`
asks the analyzer what it already knows: if the row carries a lemma that itself
begins with waw (وَلَد, وِلَايَة, وَجَبَ, وَاجِب) the letter belongs to the word.
**The analyzer, the kernel and the evaluation all call it**, so the number the
suite reports is the number the reader sees — before that they disagreed, and
the eval was scoring a wider set than the app ever annotated.

**The glossary is a LEXICON, and open text may consult it.** `fromCorpus` walks
the verb paradigms and nothing else, so for several hundred nouns the analyzer
had no lookup at all — الْإِمَامُ came back with no gloss, and اللهَ got one only
because a lexical branch handled it by name. `RootFinder.nounIndex()` indexes
every non-verb glossary entry under its bare **lemma and its stored plural**,
and `nounFromCorpus()` tries the written word, then without the article, then
without one clitic letter (and the لِلْ that swallows the article). A gloss the
glossary owns is not a guess, so the row becomes `sure`. Verbs still answer
from their paradigm first — the noun index is only asked when nothing did.

**«an» wears two faces and telling them apart is not a guess.** أَنَّ is followed
by a NOUN, أَنْ by a VERB — the same discriminator the i'rab uses. `ReadingEngine`
routes on it: `readAnna` bails the moment a verb follows, `readMasdar` requires
one. أَنْ turns its clause into a **masdar** that then fills a slot like a single
noun, and the reading is **labelled rather than dressed as fluent prose**: the
app can be certain what the structure is and cannot be certain how a reader
would idiomatically say it, so it states the first and stops.

**A lex key is GLOBAL, not per-package.** `corpusIndex()` spans every story, so
two packages using the same key for different verbs silently replace one
another. Adding جَازَ to Aqaid as `jaza` wiped bad-al-amali's جَزَى and the
smoke suite caught it as a *root-finder* failure two engines away from the
cause. Check the key across `content/samples/*/morphology.json` before adding a
verb; جَازَ is keyed `jaaza`. And note that these authoring scripts only ever
ADD — renaming a key leaves the old one behind, so a rename must `pop()` the
stale key explicitly or the collision survives the fix.

**`amr_attach` appends the sukun itself.** Pass the stem WITHOUT one or the
paradigm ships جِبْْ. For a hollow verb pass both stems — the long one before a
vowel-initial ending (جُوزُوا), the short one before a sukun (جُزْ). And a
**doubled verb needs both stems too**: the merge holds only while the second
identical letter stays vowelled and breaks apart the moment a sukun-initial
ending arrives — اِخْتَصَصْتُمَا, never *اِخْتَصّْتُمَا. Build those with `entry()`
and explicit split stems, not with `derived()`.

**An engine whose rules are exact should BUILD, not describe.** `IdafaEngine`
does not comment on an idafa it is shown — it constructs one from two nouns and
a case, and prints every rule that fired: the tanwin dropped, the nun of the
dual and the sound plural dropped, the five nouns declining by a LETTER, the
mudaf ilayh's kasra (or its **fatha**, when it is mamnu' min al-sarf), the
taqdiri ending on a maqsur at either end. Where the rules forbid the thing it
**refuses and names the rule** — لا يجتمع الألف واللام والإضافة — because a
refusal with a reason teaches more than a wrong answer offered politely. A
describer can be vague; a builder cannot, which is the whole argument for
writing it this way.

Two traps inside it, both cost a wrong word before they were found:
- **Test the nun BEFORE stripping the ending.** `strip()` takes the final vowel
  off, so `ـُونَ` no longer matches and مُسْلِمُونَ walks out as *مُسْلِمُونُ.
- **A maqsur head shows nothing.** فَتَى الْقَوْمِ, not *فَتَىُ.

**Which nouns are barred from tanwin is asked of the LEARNED tagger.** That is
what training it was for: a rule that used to need a lexicon now has a model to
consult, so غَنَائِمُ takes its fatha in jarr without anyone listing the
sighat muntaha al-jumu'. Below 50% confidence the answer is "don't know", and
"don't know" falls back to the ordinary munsarif reading.

**The closed-class table holds classes, not one class — continued.** The
demonstratives and the relatives are ASMA too (mabni asma, but asma), and مَا is
six nouns and six letters: `MA_ISM` names the six, and the class follows
`MaEngine`'s own ranking instead of a blanket assumption. That last change was
measured NEUTRAL on top-1 accuracy (it fixed six tokens and broke five) and was
kept anyway, because it replaces a categorically wrong label with an
engine-grounded one and marks the genuinely undecidable `sure: false`. Recorded
as neutral — do not claim it as a gain.

**Grade the analyzer against HUMAN labels, not against itself.** Every token in
the library carries a hand-written `pos`. Scoring the analyzer's `kind` against
those 3,331 labels on the three classes it decides is the only number here
nobody can argue with, and it is a smoke gate (floor 90). It went **82.0% →
91.5%** in one turn, and every point of that is traceable:
- the **arbiter** (+3.2): the surface left 747 tokens marked `noun?`/`verb?` and
  was right about only 61.4% of them. Asking BOTH distilled taggers and taking
  whichever is more confident is right 75.5%, measured leave-one-story-out. A
  sweep over a scale factor and a dead-band margin was run first — the raw
  comparison (scale 1, margin 0) won outright, and held-out 75.5% matched
  resubstitution 75.9%, so **there is no fitted constant** and none appears.
- **the closed-class table is a table of closed classes, not of harf** (+2.9):
  كَانَ وَأَخَوَاتُهَا live in it because they govern, but they are verbs; لَيْسَ is a
  jamid verb; the detached pronouns are asma. Calling all three "particle" cost
  ~50 tokens.
- **مِنْ vs مَنْ** (part of the same +2.9): one spelling, two words, and the
  surface *does* decide — kasra on the mim is the letter, fatha is the ism (and
  مَنْ is an ism in every reading, never a harf). Undiacritised, neither wins:
  the jarr reading is shown, `sure` is false, and the note says why.
- **a jarr letter fused to a pronoun** (+3.4): بِهِ، لَهُ، عَلَيْهِ، مِنْهُمْ is one
  word and two i'rabs. Peeled by RULE via `JARR_HEAD`, not by listing the two
  dozen spellings; عَلَيْهِ and إِلَيْهِ turn their alif maqsura to ya before the
  pronoun, so the head is looked up both ways.

**The taggers are NOT memoised.** A word cache keyed on the model was built and
measured: it saved two percent of a corpus sweep — noise — and carries a real
hazard, since `evalUnseen` swaps a fold's model in behind the caller's back and
a cache outliving that swap would grade the folds against one another. Measured,
rejected, recorded; do not re-add it without a number.

**The learned layer has two halves, and each is asked only its own question.**
`SarfTagger` reads a conjugated VERB back to its (form, tense, person);
`IsmTagger` reads a derived NOUN back to its **wazn**. The analyzer routes on
`row.kind` — asking the verb tagger about مُؤْمِنُونَ wastes a guess and asking
the noun tagger about كَتَبَ invents one. Both are generated from the rules
(38 patterns × 40 sound roots × the endings real text shows = 15,760 examples)
and both are graded five-fold **by root**.

**IsmTagger predicts the SCALE and stops there — deliberately.** The surface
settles which wazn a noun stands in; the wazn does **not** settle what the noun
is *for*. مَفْعَل is a place, a time and a masdar mimi at once; أَفْعَل is an
elative and a colour; فَعِيل is a sifa mushabbaha, an intensive, and sometimes
passive in sense; فِعَال is the Form III masdar **and** one of the busiest
broken plurals. `ROLES` is a deterministic lookup returning a **list**, the UI
shows the list whole, and the kernel pushes the leftover choice into
`undecided`. Showing the ambiguity *is* the teaching.

**Sound triliteral roots only in the noun generator.** A weak root's letter is
turned or dropped before it reaches the surface; training on those surfaces
without running the i'lal teaches wrong ones. That derivation is IlalEngine's
work, and the two engines meet in the kernel, not in the generator.

**Inflection is not scale — peel it before you featurise.** Adding sound-plural
forms to the training set dropped held-out singular accuracy 92.5% → 86.1%,
because ون/ين/ات walked into the suffix features *and their harakat walked into
the mark features*. Peeling the tail from the bare string alone bought 0.2
points; peeling it from the **diacritised** string too took plurals 67.5% →
97.1%. The ta marbuta is deliberately NOT peeled — it belongs to مُفَاعَلَة's own
scale, and مُفَاعَلَةٌ really is both that masdar and the feminine of مُفَاعَل.
Final: **90.6% top-1, 98.7% top-2 on unseen roots.** A uniform class prior was
measured and is worse (−1.5); α beyond 0.5 buys nothing.

**Peel a proclitic only when the article stands behind it.** `PROCLITIC` is
`/^[وفبكل][ً-ْ]*(?=[اٱ][ً-ْ]*ل)/`. The و of وَالْمُؤْمِنُونَ is a conjunction; the و
of وَاصِل is a RADICAL, and without a lexicon only the following ال tells them
apart. **Featurise the vowelled word, never a bare segment** — handing the
tagger an undiacritised «المؤمنون» cost it every haraka it reasons from and
dropped its confidence from 56% to 17%.

**اللَّه is an ALAM and is answered lexically.** Left to the general machinery
the commonest word in a creed text came apart as «ال + له + ه» — the article
peeled, the radical ha called an attached pronoun and a mudaf ilayh, a root
ل ل ه invented from the wreckage, and أَفْعَلَ hung on it. `SentenceAnalyzer.JALALA`
short-circuits all of it. **إِلَه is NOT in that set**: it is the common noun,
with a real root (أ ل ه) and a real wazn, and must keep going through the rules.
`JALALA_PRE` covers the name behind a clitic — لِلَّهِ is ل + الله with the
article's alif swallowed, so its bare form is ل ل ه, which the root finder was
matching to a corpus **imperative**. The prefix is named (jarr lam, oath ba,
oath waw, the ta that enters on no other word) and the rest is the alam.
A row marked `alam` is offered no root, no wazn and no learned scale.

**لَا يَجْتَمِعُ الْأَلِفُ وَاللَّامُ وَالْإِضَافَةُ.** A noun already made definite by ال
cannot also be a mudaf, so a pronoun-shaped tail on an ال-word is a root
letter. The enclitic peel is blocked there — and the block is *stated* in the
notes, because the rule is the reason the reading is refused.

**The reading is the last thing said, and it is assembled, never invented.**
`ReadingEngine` fills every slot with a gloss the glossary owns or the Arabic
word itself; only the joining tissue (-dığını, «that …») is supplied, and that
comes from the syntax. It answers for structures it can name and is otherwise
**silent** — a half-guessed translation teaches worse than none. Turkish
genitive is by vowel harmony off the last vowel; an Arabic word standing in for
a missing gloss falls back on -ın.

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

**A game round survives a detour.** `runQuiz` keeps the whole round in G and
repaints through one `draw()`; `QUIZ_RESUME = {redraw}` lets a grammar note
or an i'rab sheet offer «back to the game» (`quizReturnHtml()` +
`bindQuizReturn()` — call BOTH in any sheet a game can reach). Options are
drawn once per question (`G.optsFor`), so a resume never reshuffles them and
never re-scores: the Elo update fires only on the first answer. Closing the
sheet or reopening the hub clears the resume.

**A wrong answer must teach, not just mark.** `runQuiz` always prints the
correct option; a game may add `whyNot(it, picked)` to refute the specific
pick. The refutations are DERIVED, never canned: `caseSignOf` reads the
actual ending sign off the word (damma/fatha/kasra/sukun + the waw/ya/alif
of the plurals and duals) and says which cases it can carry; `roleWhyNot`
names the picked role's own interrogative and the true one's (ROLE_KEYS
carry a `q` field); the sarf drill names WHICH cell of the same paradigm the
learner picked; the Hamza game refutes each of إِنَّ/أَنَّ/أَنْ on its own
grounds.

**The quadriliteral babs are the other seventeen doors.** `rubaiDerive`
(RUBAI_BABS R1-R4) conjugates any four-letter root by rule alone —
فَعْلَلَ يُفَعْلِلُ (the only bare verb whose mudari' prefix takes DAMMA),
تَفَعْلَلَ, افْعَنْلَلَ, and افْعَلَلَّ, whose last radical contracts before a
vowel and BREAKS before a consonant (اِقْشَعَرَّ / اِقْشَعْرَرْتُ — the sukun
falls on the third radical). RUBAI_MULHAQ names the six attached shapes
(حَوْقَلَ، بَيْطَرَ، جَهْوَرَ، عَثْيَرَ، جَلْبَبَ، سَلْقَى). A fourth letter in the
Sarf Lab hands the controls over: the triliteral forms hide, the four
quadriliteral babs appear, and `conjAutoPick` returns early because
`conjKey` reads `cls.rs`, which the ruba'i shape has not got. Every derived
form is proofread by HarakeAuditor in the smoke suite — that is how the
broken-stem sukun was caught.

**`hidden` loses to a later `display` rule.** The bab row had been failing
to hide under a mazid form for as long as it existed; `[hidden] { display:
none !important }` fixes it globally. Attribute-hiding needs the guard rule.

**research/COVERAGE.md is the shelf audit.** Every file in research/sources/
judged FULL/PARTIAL/UNTOUCHED against what the app consumes, with a
prioritized backlog. Regenerate with the `sources-coverage-audit` workflow
after each content wave. Current tally: 9 FULL, 19 PARTIAL, 6 UNTOUCHED.

**مَا wears twelve faces, and the engine names the SIGNAL.** `class MaEngine`
(WAJH table + `read(words, i, fulls, isVerb)`) applies Qawa'id al-I'rab's
bab on مَا as pure surface rules: kaffa when it rides a fused governor
(إِنَّمَا، رُبَّمَا، قَلَّمَا), zarfiyya before the دَامَ family (match the ROOT —
دُمْتُ wears no dal-alif-mim), taajjub on أَفْعَلَ + a mansub noun, masdariyya
/mawsula after a jarr letter, shartiyya on two verbs, hijaziyya when a noun
follows and a later word is MANSUB — that accusative is the khabar this ma
governs. (The Hijazi signal is the mansub khabar, NOT a ba: the ba of
بَشَرًا is a radical. An early draft got this wrong.) Every reading prints
with the neighbour that proposed it and the runners-up follow when the
signal is weak — the app never says «it is X», it says «X, because Y».
The fused spellings (مِمَّا، بِمَا، إِنَّمَا…) are registered in
SentenceAnalyzer.PARTICLES so the branch is reached at all.

**A bare mazi wears no prefix — pass the corpus in as an ORACLE.** MaEngine
takes an optional `isVerb(k)`; the Analyzer supplies one backed by
RootFinder.fromCorpus, so كَتَبَ is known to be a verb and مَا before it
reads nafiya rather than hijaziyya. Standalone callers get the prefix test
and the engine degrades honestly. Vowelling sharpens every reading: the
taajjub and hijaziyya signals live in the tanwin, so unvowelled input
legitimately returns a weaker shortlist.

**Every reading in a table must be REACHABLE.** The ma review found three
entries no signal could ever propose — dead data pretending to be coverage —
and two spellings that reached no branch at all because they were absent
from PARTICLES. The smoke suite now walks a sentence per wajh and fails if
any defined reading is unreachable. Apply the same test to any future table:
if `say(k)` is never called with a key, either give it a signal or delete it.

**A duplicate key in PARTICLES silently deletes doctrine.** «لما» was
registered twice — the later `{k:"ma"}` shadowed `{k:"jazm"}`, killing the
jazim reading AND the v72 after-jazim mizan correction downstream. There is
now a regression check; when adding to PARTICLES, grep for the key first.
لَمَّا is told from لِمَا by its SHADDA, which is right there in the surface.

**Some roots refuse i'lal, and the engine must know which.** SOUND_HOLLOW
holds أَفْعَالُ الْعُيُوبِ وَالْأَلْوَانِ — a hollow verb of bab سَمِعَ meaning a
defect or a colour keeps its weak letter SOUND (عَوِرَ يَعْوَرُ, never عَارَ),
because its masdar فَعَل is sound and its ism fa'il rides أَفْعَل not فَاعِل.
The engine had been over-applying qalb and producing wrong forms. WHICH
roots carry that meaning is lexical and cannot be derived, so the table
holds ONLY the roots; everything after that is rule. This is the project's
line in one place: automate the derivable, store only what cannot be. The
i'lal walkthrough returns a single step that says why NO step runs.

**Aqaid runs to ch7** (khalq al-af'al, the servants' chosen acts, and
al-istita'a ma'a al-fi'l — with three passive deputies and كُلِّهَا as
ma'nawi tawkid). **The drill garden is six chapters / 48 sentences**: the
newest contrasts كَانَ against إِنَّ on the SAME sentence (the mirror the
books teach), the tamyiz of the decades (singular mansub), istithna tamm
against mufarragh — where the noun takes the case its POSITION demands —
and ism tafdil both as a diptote and in idafa. The model trains on 1100+
labeled tokens.

**A span may STOP EARLY; it may never skip from the middle.** The ch7 review
caught me splicing two non-contiguous matn fragments with a comma — and the
i'rab lied to cover it, calling a waw عاطفة that in the matn follows a full
stop. The fix is always the same: split into two sentences, and let the
second one's waw be استئنافية. There is now a smoke guard on exactly that
sentence pair. And when the received wording beats the supplied
transcription (7:s2 قَضَائِهِ against the file's قضيته), the received text
wins AND the divergence goes into the manifest attribution — every story
does this, and the smoke suite reads it OFF DISK, because the attribution
text never ships to the browser (only reviewStatus does).

**Aqaid reaches ch8, the sam'iyyat — and the story closes its own ring.**
Chapter 1 opened this book with the hawd hadith; chapter 8's roll of eight
realities names الْحَوْضُ حَقٌّ. That roll is also the cleanest possible
mubtada/khabar drill: eight pairs, one pattern. Chapter 8 also forced a
real gap into the open — the DUAL was taught nowhere. `al-muthanna` now
covers it: alif in raf', ya in nasb and jarr, i'rab BY LETTERS (so it sits
with the five nouns and the sound plural), the nun dropping in idafa, the
five verbs taking raf' by the RETAINED nun, and the alif inside such a verb
being the FA'IL rather than a sign of i'rab. Anchored to the chapter's own
مَخْلُوقَتَانِ مَوْجُودَتَانِ بَاقِيَتَانِ لَا تَفْنَيَانِ, and contrasted with
زَوَايَا from chapter 1, which merely looks dual.

**The bayan file is no longer untouched.** `alaka-ilm-bayan.txt` is Ottoman
script, but its ARABIC definitions are vowelled and perfectly readable —
that is the lesson for the rest of the Ottoman shelf: DO NOT write a file
off because its prose is in Ottoman. `anwa-al-majaz` takes from it the
lughawi/aqli division, the mursal ʿalaqa roll, and three kinds the app had
never taught: مَجَازٌ عَقْلِيٌّ (أَنْبَتَ الرَّبِيعُ الْبَقْلَ — every word literal,
the ATTRIBUTION moved), مَجَازٌ بِالزِّيَادَةِ (لَيْسَ كَمِثْلِهِ شَيْءٌ) and
مَجَازٌ بِالنُّقْصَانِ (وَاسْأَلِ الْقَرْيَةَ) — where the i'rab itself is the
evidence that a word was added or dropped. Still unconsumed there: the
isti'ara subdivisions and the Sakkaki/Khatib disagreement. Update
research/COVERAGE.md whenever a file's verdict changes — it has a Log now.

**Aqaid reaches ch9** — the grave sin that does not unmake faith,
intercession, the non-eternity of sinning believers (لَا يَخْلُدُونَ, the five
verbs again), and the definition of iman as التَّصْدِيقُ وَالْإِقْرَار with a
damir fasl and a relative مَا carrying its sila.

**The eleventh game is «Which relation?»** `ALAQAT` holds the twelve
relations the bayan file works right through — definition, example, literal
meaning, intended meaning, the QARINA that forbids the literal reading, and
the madrasah's own formula (ذِكْرُ السَّبَبِ إِرَادَةُ الْمُسَبَّبِ). Sixteen more
it merely names; those are listed, never quizzed, because the app quizzes
only what it can teach. The book's tally is 28 and a smoke check holds the
registry to it. Only مُشَابَهَة makes an isti'ara — that single fact is the
whole mursal/isti'ara line, and it is pinned. BALAGHA is a real Elo area
now, with its own bar, sparkline and coach label; old saved ratings are
BACKFILLED at 1200 rather than reset.

**IrabSign is the i'rab-realization engine — pure rule, no data.** It
answers the Kafiya's two crossing questions off the surface alone: BY WHAT
is the case shown (haraka / letters / removal) and IN WHAT MANNER (lafzi /
taqdiri / mahalli). Five nouns, dual, sound plurals, maqsur, definite
manqus, mabni and jazm all fall out of it, and every Analyzer row now wears
the badge. Two traps it taught: stripAr keeps the HAMZA SEAT, so أَبُوهُ
never matches a plain-alif pattern — fold seats for MATCHING only, never
for display; and indefinite قَاضٍ is spelled exactly like any other
indefinite majrur, so the engine reads it as the plain vowel rather than
pretending to know. Decide only what the surface can decide.

**The deck has a browser.** Past eight cards, a search box and a filter row
(due / fresh / learning / mature / leech / verb / note) sit above the list.
The filter predicates use EXACTLY deckStats' rules — isLeech and the 21-day
line — so the counts beside the buttons can never disagree with the stats
row above them, and leech is non-exclusive in both. Filter state is a view,
not a preference: it lives outside `state` and dies with the sheet.

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

**The vocative is computed, not stored.** `NidaEngine` (reader.html) takes a
call as typed and derives everything: `read(text)` returns the particle, the
kind, the ruling (`mabni` / `mansub` / `majrur`), the SIGN and the reason;
`tarkhim(name)` lops the last letter off in both dialects; `nadb(name)` hangs
the alif of grief and the ha of pause on the end. Four things to keep:

1. **The engine reads the ENDING, never the meaning.** يَا زَيْدُ and يَا رَجُلُ
   are one shape and one ruling, so the kind is named «مُفْرَدٌ عَلَمٌ أَوْ نَكِرَةٌ
   مَقْصُودَةٌ» and it stops there. An unvowelled call returns
   `{ok:false, reason:"unvowelled"}` — this whole chapter is decided by the
   last vowel and by nothing else.
2. **`nakiraOrShibh` exists because the surface cannot tell them apart.**
   يَا رَجُلًا اِسْمَعْ and يَا طَالِعًا جَبَلًا look identical to any rule that
   does not know whether the next word is GOVERNED by the munada. Both are
   mansub, so the engine rules once and names both kinds. Do not "fix" this
   into a definite `shibh`.
3. **Tarkhim must NOT re-strip the stem after dropping the last letter.**
   The vowel left standing IS the difference between لُغَةُ مَنْ يَنْتَظِرُ
   (حَارِ) and لُغَةُ مَنْ لَا يَنْتَظِرُ (حَارُ). Taking the damma off for the
   second dialect keeps the SHADDA (مُحَمَّ → مُحَمُّ, not مُحَمَُّ), and a
   madda ending takes no damma at all, so both dialects fall together
   (سُعَا، مَنْصُ).
4. **The smoke suite runs the engine against every munada in the corpus** and
   fails if a stored i'rab says مَبْنِيٌّ where the engine says mansub, or the
   reverse. It also demands that all six signs — damma, alif, waw, fatha,
   fathatan, fathaTaqdiri — appear in real text; that is why the drill garden
   has a vocative chapter.

**I'lal is an ALGORITHM, not a table.** `IlalEngine` holds ten ordered rules
and a `derive(asl)` that applies the first matching one until nothing fires,
recording every firing. `build(root, shape)` assembles the underlying form
from a wazn and hands it over, so قَائِلٌ، مَقُولٌ، مَبِيعٌ، مَكِيلٌ، مَغْزُوٌّ،
مَرْمِيٌّ، غَازٍ، دَاعٍ، مَدْعُوٌّ and قُلْ all come out of the same rules with
nothing stored. Five things the rules taught us the hard way:

0. **The mithal waw-drop is licensed by the KASRA after it,** not by the waw
   itself: يَوْعِدُ → يَعِدُ, but يَوْجَلُ keeps its waw because a fatha follows,
   and يَوْمَ is not a verb at all. The rule tests the prefix, the sakin waw
   and the following kasra together, and all three matter.
1. **Order is doctrine.** naql before qalb; qalb before the meeting of two
   sakins; the vowel-harmony that PROVES what was dropped comes after the
   drop. Reorder the array and قُلْتُ becomes قَلْتُ.
2. **The alif must remember what it came from.** After qalb, قَالْتُ and
   بَاعْتُ look identical, but one ends in a damma and the other in a kasra.
   `qalb-alif` stamps `from` on the unit, and `hadhf` reads it.
3. **Idgham requires the SECOND letter to bear a vowel.** Where both are
   quiescent it is a meeting of sakins, and that chapter drops a letter
   instead of fusing them — this is the whole difference between مَغْزُوٌّ and
   مَقُولٌ.
4. **When two weak letters meet, the WAZN's letter goes** — it is the second.
   Then the surviving weak letter, not the fallen one, decides the vowel:
   مَكْيُولٌ loses its waw but harmonizes to the ya, giving مَكِيلٌ.
5. **A doubled ya is no manqus.** `hadhf-manqus` must refuse a ya wearing a
   shadda, or مَرْمِيٌّ collapses to مَرْمٍ.

The smoke suite pins 23 worked derivations plus 12 root+wazn builds, and
includes sound roots and مُيَسَّرٌ — a real word that LOOKS like an i'lal site
— to prove the rules also know when to do nothing.

**And the rules have to be told where to stand down.** `IlalEngine.blocked
(root, shape)` runs before `build()` and returns a refusal with its reason.
There are exactly two kinds, and the panel names which one fired, because the
distinction IS the project's method: (1) a WAZN rule, derivable and therefore
coded — the elative and the wonder-verb on أَفْعَل are never i'lal'd, since the
shape is the meaning and i'lal would destroy it (أَقْوَلُ مِنْهُ); (2) a LEXICAL
set, not derivable and therefore stored — whether a root means a defect or a
colour is something you know, not something you compute (عَوِرَ، حَوِلَ، صَيِدَ،
غَيِدَ، هَيِفَ، حَوِرَ). A blocked derivation still shows its ORIGIN, so the
learner sees the form the rules would have eaten. Do not "simplify" the
مِفْعَال case into a rule: مِيزَان comes from مِوْزَان and IS i'lal'd, while
مِقْوَل is not — that split is sema'i and any rule you write for it will be
wrong.

**The design system is one page and four gates.** `DESIGN.md` documents the
tokens, the components and what was borrowed from the reading apps people
actually keep. The smoke suite enforces every claim a browser can check:
tokens resolve, a live primary action measures ≥ 44px, the front door's stat
strip matches `deckStats()` exactly, and the phone layout is exercised at
390×844. A literal `padding: .9rem` in a new rule is a bug even when it
looks right.

**`SarfTagger` is DISTILLED from the conjugator — the rules write their own
training set.** Every other model here learns from what humans wrote down,
which caps it at the corpus. This one runs `sarfDerive` over thirty roots
through every form and bab and turns each cell into a labelled example:
~12,750 of them, generated in about 40ms, from nothing but the algorithm the
app already trusts. What it buys is not speed — the conjugator maps
(root, form, bab) → forms, and the tagger maps a FORM BACK to its slot, for a
root the app has never met, which the rules can only do by exhaustive search.

Three things keep it honest:

1. **Character shape only.** First letters, last letters, the sequence of
   harakat, length, shadda. No root list, no lexicon — so the model must learn
   the PATTERN rather than memorise a root.
2. **Graded on UNSEEN ROOTS.** `evalUnseen()` folds five ways *by root*:
   70.8% exact (form + tense + person), 87.8% within two, 86.9% on the form
   alone. A fit-on-itself number here would be meaningless, because the whole
   question is whether it generalises to a root it was never given.
3. **Its confidence IS its part-of-speech filter.** Real verb forms come back
   at 40–48% and قَالَ at 11%, while مَدِينَة manages 5.6% and الْكِتَابُ 1.9% for
   labels that are nonsense. The kernel shows it above 10%, which is where
   verbs stop and furniture begins — and it is always badged a GUESS.

**More generated data is free, so the question is where it stops paying.**
`tools/tagger_curve.js` scores the whole learning curve, every point held out
by root: 10 roots 73.9%, 20 → 69.6%, 30 → 70.8%, **45 → 75.0%**, 60 → 75.5%,
70 → 75.7%. Forty-five is where the jump happens and sixty is where it
saturates, so the shipped list is forty-five. Two traps in reading that curve:
the 10-root point looks great and is **deceptive** — two roots per fold is too
small a test set to mean anything — and the curve is NOT monotonic between 10
and 30, so a single extra point proves nothing on its own. Re-run the whole
curve before changing the root list.

`evalUnseen()` is expensive (five folds over the whole generated set, ~6s at
forty-five roots) and is deliberately **never on a user path** — only
`train()` is, and that is one pass. The smoke suite pays the cost; the app
does not.

Note that ALPHA here is 0.5 while `IrabModel.ALPHA` is 0.35. Different feature
sets damp differently; both were chosen on held-out evidence, and neither
number should be copied to the other model.

**`GrammarKernel` is one door for ten engines.** `ask(text)` routes a word to
the form engines (lexicon, `IrabSign`, `WaznEngine`/`RootFinder`, `IsmEngine`,
`IlalEngine`, and the learned `SarfTagger`) and a phrase to the sentence engines (`NidaEngine`, `MaEngine`,
the corpus's own i'rab plus `AmilEngine`, else `SentenceAnalyzer`). Three
rules make it worth having, and they are what a grammar kernel IS:

1. **Every finding declares HOW it is known** — `rule` (an engine derived it),
   `corpus` (a human wrote it down) or `model` (a statistical guess, badged).
   A guess that renders like a rule is the one failure mode that matters.
2. **A silent engine says nothing.** No "could not determine" rows; if an
   engine did not decide, it is simply absent.
3. **What nothing settled is stated OUT LOUD**, last and visibly. The boundary
   of the automatable is itself a thing worth teaching — meaning is never
   derivable, an unvowelled ending cannot be read, and no rule settles every
   word of open text.

**It is not a language model and must not be sold as one.** It is the
deterministic core such a model would need underneath it: everything in Arabic
that is genuinely derivable, derived, with the honest edges marked.

**`AmilEngine` reads the government out of the i'rab, it does not store it.**
Every stored i'rab line already says what a word IS; nothing says which word
GOVERNS which, and nothing needs to. `AmilEngine.pairs(sen)` walks the
sentence keeping a stack of governors and pairs each governed word with the
nearest governor that can give the case it wears — which is what the `from`
list on each MA'MUL entry is for: **a majrur must never be handed to a verb**.
The smoke suite asserts that constraint over the whole pool, and that no word
governs itself. This is what the İbare game's reveal is built from, so the
explanation can never drift from the analysis.

**Games are scoped to where you are.** `gameStories()` is the ONE place the
decision is made: at the front door a round is drawn from the whole library,
inside a story it is drawn from that story alone. Every item builder goes
through it — a builder reaching for `STORIES` or `CHAPTERS` directly has
escaped the scope. Two things learned wiring it: (1) **scope is a preference,
not a cage** — a story that cannot feed a drill hands the round back to the
library via `scopeFallback()`, because a dead button teaches nothing; (2) the
smoke suite must MEASURE and PLAY in the same scope, or it will size a pool
from the library and then open a story that holds none of it.

**A known engine inconsistency, deliberately not papered over:** for a
nun-final root, `sarf_gen.derived()` writes the feminine-plural boundary
un-assimilated (بَيَّنْنَ) while the in-app Form II branch assimilates it
(بَيَّنَّ); `sound1()` and the Form I branch agree on the un-assimilated
أَمِنْنَ. `bayyana`'s four boundary cells are stored in the engine's spelling
so the audit gate is honest. Settle the engine before harmonising the data.

**Navigation exists twice and is implemented once.** Below 860px `.tabbar` is
the app's navigation; above it the toolbar is, and the bar is hidden. Every
tab DELEGATES to the toolbar handler that already owns that destination
(`TAB_NAV`), and `syncTabbar()` derives the active item from what is on
screen — there is no stored "current tab". The bar repaints by wrapping
`renderLibrary`, `openStory` and `grade`, the three functions that define
which view is open and what is due; do not add a fourth wrapper without
checking whether one of those three already covers it. **Test the phone
layout at a phone viewport** — everything else in the suite runs at 1280px,
where the bar is correctly absent.

**The model is graded HELD OUT.** `IrabModel.crossVal()` trains on every
story but one and tests on the one held out, sixteen folds over ~2600 labelled
tokens. That is the number the Jumla Lab leads with and the number the smoke
suite floors, because it is the only one that says anything about a sentence
the app has never seen; `accuracy()` (resubstitution) is shown beside it as
the upper bound it is, and the suite asserts resubstitution BEATS held-out —
if it ever does not, something is leaking. `ALPHA` (the feature-damping
exponent) was chosen this way: on the training score 0.35 looked like a spike
between two equal neighbours, which is what an overfitted hyperparameter looks
like; cross-validation confirmed it as a real +1.2. Run `tools/cv_eval.js`
before changing it.

**Four ML ideas were tried and REJECTED on measurement.** Write them down so
nobody spends the afternoon again: (1) a **Viterbi sequence layer** over role
transitions — catastrophic, 52.9% → 40.6%; the role sequence in this corpus is
not helpfully Markovian, and the transition counts just drag every token
toward the frequent classes. (2) **Richer `prev` states** (nasikh, particle) —
53.0% vs 52.9%, noise. (3) **The previous token's PREDICTED role as a feature**
— 51.1%, worse; errors compound left to right. (4) **Complement and Bernoulli
naive Bayes** — 42.8% and 52.1%, both worse than the shipped multinomial. The
signal in this corpus lives in the word's own surface, not in its neighbours.

**The rule engines feed the statistical one.** `IrabModel.features()` now
pushes `sign-<caseSignOf>` and `by-<IrabSign.of().by>` alongside the cheap
surface flags. A bucketed word length was added the
same way, and the likelihoods now carry a **1/sqrt(k) weight** where k is how
many features the word fired — naive Bayes assumes independence and ours are
plainly correlated (`al`, `sign-kasra` and `by-haraka` move together on one
word), so an unweighted product counts one piece of evidence three times. Measured, not asserted, over the labeled corpus tokens: first-guess
accuracy went 42.7% → 49.3% (sign + manner) → 51.4% (length) → 53.2% (weighted likelihoods); two-guess 62.9% → 71.2%.
**`tools/ablate_features.js` earns a FEATURE its place and
`tools/ablate_estimator.js` earns an ESTIMATOR its place** — it monkeypatches `features()` in a live page and scores each
candidate against the shipped set. A mim-initial flag and a shadda flag were
tried in the same run and dropped as noise, and complement naive Bayes was
tried as an estimator and was far WORSE (42.8%). An unmeasured change is a
superstition. **In `ablate_features.js`, `base` is the SHIPPED set** — every
variant ADDS to it, so re-adding a shipped feature scores a double count and
reads as a regression.
`IrabModel.accuracy()` computes that score lazily and caches it, the Jumla
Lab prints it (`.ml-score`), and the smoke suite pins the floor just under the last measured run so
a feature change has to be measured instead of believed. The score is
RESUBSTITUTION — an upper bound — and the panel says so.

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

## Traps found while setting Mukhtasar al-Manar chapters 2–3

**When a correct word breaks a test, the test was wrong.** The corpus-search
check asserted that searching a root closed up (`قول`) returns exactly as many
hits as searching it spaced (`ق و ل`). It had passed for sixteen stories by
coincidence. `الْمَنْقُولُ` broke it — and `م-ن-ق-و-ل` really does contain
`ق-و-ل`, so the extra hit was not a bug. The assertion is now **superset**: the
closed-up search must find every spaced hit and may find more. The right answer
to an unwanted-but-legitimate hit is never to filter it out; it is to **rank**
it. `searchRank()` scores root-identity 4, word-identity 3, prefix or gloss 2,
incidental substring 1, and `openSearch` orders groups by rank before count.
Same doctrine as everywhere else: the app owes a correct shortlist, and
dropping a hit because a rule dislikes it is how a shortlist stops being
correct.

**A head that declines by a LETTER takes the case it was ASKED for, not the
case it was TYPED in.** `IdafaEngine` dropped the nun of the dual and the sound
masculine plural correctly, then kept whichever letter the input happened to
carry — so `مُجْتَهِدُونَ` asked for in jarr came out `مُجْتَهِدُو`. The ending
is now chosen from `kase`: plural waw/ya/ya, dual alif/ya/ya, and a second step
is emitted whenever the letter actually changed, because that change is the
lesson. The smoke check had *enshrined* the bug — it asked for `كِتَابَانِ` in
nasb and expected `كِتَابَا وَلَدٍ`. A test that asserts the current output is
not a test.

**Two sukuns will not stand.** `دَفَّتَيْ` + `الْمُصْحَفِ` puts the sukun of the
dual's ya against the silent alif of ال, so the ya is broken with a kasra:
`دَفَّتَيِ الْمُصْحَفِ` — which is exactly what the matn writes. The engine now
does this at the end of `build`, and the step says why. Any future
letter-ending head followed by ال needs the same treatment.

**Attribution is content, so it is bilingual too.** The chapter-2 script
appended its English provenance note to `attribution.tr`, which had been empty
— an English sentence sitting in the Turkish field of an app whose whole promise
is EN–TR parity. Provenance is the one field a reader is most entitled to read
in their own language. Write the note once per language; never let one language
inherit another's.

**Peel SHAPE-FIRST, never trailing-mark-first.** `AlamaEngine` was written with
the IdafaEngine lesson in hand and made the same mistake twice more in one
function. A blind `replace(/[ًٌٍَُِ]$/, "")` eats the vowel that belongs to the
dual's own nun, so `كِتَابَانِ` becomes `كِتَابَان`, the `(َانِ)$` test no longer
matches, and the word walks out as *`كِتَابَانَانِ`. And a maqsur keeps its tanwin
BEFORE the alif, where a trailing peel never looks at all, so `فَتًى` came out
`فَتًًى` with two. Decide the shape on the ORIGINAL string, then peel what that
shape says is peelable.

**`مَعَانٍ` is the row that separates a rule table from an engine.** It is a
صِيغَةُ مُنْتَهَى الْجُمُوعِ, so it is barred from tanwin — and it is written *with*
one. Both are true at once: as a منقوص it drops its ya in raf' and jarr, and
the tanwin standing in that gap is a tanwin of ʿiwaḍ, compensation for the
dropped letter, not the tanwin of the indefinite. Put it in nasb and the two
facts separate: `رَأَيْتُ مَعَانِيَ`, ya restored, fatha bare. Anything that stores
only "mamnuʿ → fatha in jarr" gets this word wrong in all three cases. The
smoke suite gates every row of the table, not a sample of it.

**Mark what is ours.** No transcription was supplied for this package past page
1, so chapters 2–3 are set from the received matn of the Hanafi usul tradition
and say so. The closing sentence of chapter 3 is not matn at all — it is an
ORIGINAL bridge, and the manifest names it as one in all three languages. An
unmarked original inside a quoted text is the single thing this content pipeline
must never ship.

## Process

- Branch: `claude/arabic-app-research-ozd58s`. Never push elsewhere.
- No PR unless explicitly asked.
- `git push -u origin <branch>`; retry only on network errors (2s/4s/8s/16s).
- Every story manifest carries `reviewStatus: pending-scholarly-review`. Keep it there
  until a human scholar signs off.

## The Form IV mithal — substituting into the scale is not the last step

Chapter 4's أَنْ يُوجِبَ broke the paradigm-regeneration gate, and it was the
ENGINE that was wrong, not the stored form. `sarfDerive` builds a derived form
by standing the root letters in the scale — أَفْعَلَ يُفْعِلُ with ف = و gives
`يُوْجِبُ` and `إِوْجَاب`. Both are wrong on the page. A weak first radical
carrying a sukun takes the shape of the vowel in front of it: after a DAMMA it
is already a madd letter and no sukun is written (يُوجِبُ), and after a KASRA it
turns into a ya outright (إِيجَاب). The mazi keeps its waw untouched, because a
FATHA precedes it there — أَوْجَبَ. One rule, two vowels, and it applies to every
cell at once, so `sjMithalWeakHead` is run over the whole derived object rather
than spelled into each branch.

The general lesson, and it will come round again: **the wazn is a template, not
a derivation.** Substituting the root into the scale is the first step of a
derivation whose remaining steps are i'lal. Wherever a weak letter lands next
to a vowel that does not match it, expect one more rule after the substitution.

## The ta of iftiʿāl happens in two steps, and the second one was missing

Chapter 5's اِزْدَادَ sent me back through `nakilT`, and the table it encodes was
half a rule. The ibdal is **two steps**:

1. The ta takes the colour of the first radical — ط after the four emphatics
   (ص ض ط ظ), د after ز ذ د.
2. **Only where the two letters have come out identical** do they run together.

So ص and ض keep their ط standing apart — اِصْطَبَرَ، اِضْطَرَبَ — because ص is not
ط. ز keeps its د apart — اِزْدَادَ, never *اِزَّادَ — because ز is not د. But ط+ط،
ظ+ط، د+د، ذ+د do meet, and idgham follows: اِطَّلَعَ، اِظَّلَمَ، اِدَّعَى، اِذَّكَرَ.
The engine had step 1 and applied step 2 to د/ذ only, so `اِطَّلَعَ` came out
right in the past tense while its own masdar came out `*اِطْطِلَاع` and ظ never
assimilated at all.

Two more defects fell out of the same visit:

- **The masdar's kasra was skipped wherever the ibdal had already fired.**
  `tp.replace(/َ$/, "ِ")` looks for a bare fatha at the end of the chunk, but an
  assimilated chunk ends in a SHADDA — so the rule quietly did nothing and
  اِدِّعَاء had been shipping as اِدَّعَاء since the engine was written. When a
  string transformation is conditional on the last character, check what the
  *other* branches leave there.
- **Form VII had no geminate branch** and fell through to the sound path, so
  اِنْسَدَّ came out `*اِنْسَدَدَ`. Forms IV and VIII both had one; VII was simply
  never given it. The vowel that surfaces on the shadda is the mudari's own
  (يَنْسَدُّ), because the letter before the ʿayn is already vowelled and has
  nowhere to take a transferred haraka — unlike يَمْدُدُ → يَمُدُّ and
  يُحْلِلُ → يُحِلُّ, where the fāʾ is sakin and does take it.

All three are now gated by name in the smoke suite over a ten-root table, and
250 stored paradigms regenerate from the engine.

## ـَاء is two endings wearing the same three letters

Chapter 6's خَفَاءً forced a rule the engine did not have. A مَمْدُود noun ends
in an alif and a hamza, and four different things can put that hamza there:

1. the root's own hamza — قُرَّاء from ق ر أ;
2. a radical waw or ya turned into one — خَفَاء (خ ف ي)، رَجَاء (ر ج و)، دُعَاء (د ع و);
3. the **alif of femininity** — صَحْرَاء، حَمْرَاء، عُلَمَاء;
4. an added letter for lengthening — عِلْبَاء، حِرْبَاء.

**Only the third is barred from tanwin.** صَحْرَاءُ and خَفَاءً end in the same
three letters, decline differently in every case, and nothing on the page
separates them — only the ROOT does. So `AlamaEngine.mamdudVerdict` answers from
the root and returns `null` without one, and `renderAlamaOut` asks the corpus
lexicon for the root before it asks anything else. Same doctrine as the manqūṣ:
where the surface cannot decide, ask, and where nothing can be asked, say so.

**Fold the hamza SEATS when reading a root.** Roots are written with the carrier
the dictionary uses — ق ر أ, not ق ر ء — so a test for a bare `ء` as third
radical read قُرَّاء as feminine and barred it from a tanwin it is entitled to.
Any rule that inspects a root letter-by-letter has this bug waiting in it.

The registry gained note 94, `ism-mamdud`, which is the same rule written for
the reader — and it is the note the engine's behaviour is now gated against.

**A near-miss note is worse than a general one.** خَفَاءً was first tagged
`mamnu-min-sarf`, the note whose rule decides it — but the word is NOT barred
from tanwin, and a learner tapping through would have read the opposite of what
the word on the page does. Same call as ch5's لَا, which was nearly tagged
`la-nafiya-lil-jins` when it is neither that lā nor governing anything. Tag what
the word IS.

**There are TWO naqis mazi patterns and `naqis1` builds only one.** رَمَى and
دَعَا end their third person in an alif; بَقِيَ، رَضِيَ، خَفِيَ keep the ya, vowel
it with a kasra, and contract only in the third-person plural (خَفُوا).
`sarf_gen` has `mazi_naqis` for the first and `mazi_naqis_kasra` for the second,
and `naqis1` wires up the first only — so a samiʿa-bab naqis authored through
`naqis1` ships *خَفِى / *خَفِتْ. The regeneration gate caught it, which is what
that gate is for: **when the generator and the engine disagree, one of them is
wrong and the corpus is the thing that finds out.**

## The nakil drill is walkable now, and the bank is a golden file

**The transfer table was a poster.** It showed رَاجَعَ standing in the فَاعَلَ row
and gave the reader nowhere to go with it. Every row the conjugator can build
is now a button: tap it and that bab opens in full — its own three tenses and
its own muhtelife — derived by `sarfDerive` and dressed in the same shape a
stored paradigm has, so `muhtelife`, `conjTable` and `ziyadeExt` all read it
without being taught a second format. Rows the conjugator cannot build (IX, XI,
XII, XIII) stay plain text: a button that leads nowhere is worse than no button.
The derived view SAYS it was derived — the corpus does not carry those babs, and
the learner is entitled to know which of the two they are looking at.

**`content/drills/generated.json` is a golden file, not content.** 536 derived
rows — every ending class × three cases, thirty-six idafas including the refusals,
forty-seven paradigms sampled at the cells where rules fire, and the scales.
`tools/gen_drills.js` builds it by driving the app's own exact engines; nothing
in it is authored, and `--check` in the release gate fails on a one-cell drift.
Two rules govern it:

- **Nothing invented.** Every root and lemma is one the corpus already carries
  and a human has already checked; the explanation attached to each row is the
  engine's own step list, not a paraphrase.
- **No silent caps.** A scale is admitted only if it round-trips AND none of the
  pattern's augment letters is also one of the root's. اِنْفَعَلَ on ن ص ر puts two
  nuns side by side and nothing in the surface says which is the augment — both
  orderings rebuild the same word, so the round-trip cannot catch it and the test
  has to be on the LETTERS. The six dropped scales are written into the file with
  the reason, so the gap is visible instead of quiet.

**Chained `.replace()` cascades.** The round-trip check first read `فَاعِل` for
ع ل م as broken, because ف→ع then ع→ل then ل→م turns it into مَامِم. One pass
with a callback, always, when the replacements can feed each other.

**Stems go into `sarf_gen` WITHOUT their sukun** — every maker appends its own,
and `"سُقْ"` ships سُقْْتَ with two. And the hollow amr needs BOTH stems: the long
one for the vowel-initial persons (سُوقُوا) and the short one for the bare and
the نَ (سُقْ، سُقْنَ). Passing the short stem for both cost four cells.

**A lam that matches the suffix contracts.** ثَبَتَ + تَ is ثَبَتَّ, not *ثَبَتْتَ;
`sarf_gen.idgham` exists for exactly this and a verb whose last radical is
ت ن or د must be put through it.

## The bank now analyses as well as builds

`content/drills/generated.json` grew from 536 to **1,386 derived rows**, and
gained a fourth section that is different in kind from the other three.

Sections 1–3 (endings, idafa, paradigms) are EXACT: the engine decides and the
row is the answer. Section 4, the **worked sentences**, is not. For every
sentence of a named story it writes down the HUMAN parse the corpus carries and
the ENGINES' reading of the same words side by side, marks each token agree or
disagree, and counts. Manar's eight chapters come out at **91.7% part-of-speech
agreement over 301 tokens**, with 25 named disagreements left in the file —
`مَا` read as a particle where the books call it an ism, `أَمَّا` read as a noun,
`سِيقَ` read as a noun. Those rows are the point. A dataset that only contains
what the engine already gets right teaches nothing.

**Score a model only on the question it answers.** Two normalisations were
needed before the number meant anything, and both are doctrine, not fudging:

- prep, conj and part are ONE class to the analyzer — it returns «particle» for
  all three and has never claimed to separate them. Scoring them apart reported
  75%, which was a measurement of the scoring code, not of the engine.
- **a pronoun is an ism.** That is the tradition's own ruling and it is already
  written into this file. The corpus tags هُوَ and مَا as `pron` for the reader's
  sake; marking the analyzer wrong for calling them nouns would be marking it
  wrong for agreeing with the books.

With both applied the figure lands at 91.7%, next to the 91.5% the smoke gate
measures over the whole hand-labelled set — which is the check that the number
is real.

## The `مَا` rule, and how the bank paid for itself immediately

The worked-sentence section had barely shipped before it earned its keep. Ten
of its 25 named disagreements were one word: `مَا` read as a HARF where the
books call it an ism. `MaEngine` was returning a single face — `nafiya` — so
the shortlist did not contain the true reading at all.

The signal it was missing is syntactic and statable: **a definite noun stands
immediately before the مَا, no verb has occurred yet, and a verb follows.**
`الْخَاصُّ مَا وُضِعَ`, `وَالْمُشْكِلُ مَا ازْدَادَ`, `وَدَلَالَتُهُ مَا ثَبَتَ` — the mubtada
is still waiting for a khabar, and a relative clause supplies one where a bare
negation would leave it standing empty. The face is ranked above the negation
in **that configuration and nowhere else**, because `زَيْدٌ مَا قَامَ` is a real
sentence too and the negation stays on the list underneath it.

Two measurements, both taken on the bank:

- stating the rule for `i === 1` only: 92% → 92%, 25 → 24 disagreements. Nearly
  nothing, because the frame's noun almost always wears a clitic.
- testing the preceding word as `/^[وفبلك]?ال/` instead of `/^ال/`: **92% → 93.7%,
  24 → 19**. `فَالْخَاصُّ`, `وَالنَّصُّ`, `وَالْمُقَيَّدُ` — the fa and the waw were
  hiding the article from a rule that only knew how to look for it bare.

**A clitic can hide the very feature a rule tests for.** Any rule that inspects
the word BEFORE the one it is deciding must peel first, and this is the second
time that has cost real accuracy in this codebase.

And the general lesson: a dataset that records where the engine is WRONG is
worth more than one that records where it is right. Five disagreements went
away because they were written down where they could be counted.

## أَمَّا was not in the particle table at all

The drill bank's second finding, and cheaper than the first: four of the named
disagreements were `أَمَّا` read as an open-class NOUN. It was simply missing
from `SentenceAnalyzer.PARTICLES` — a word the library uses in four chapters
and has its own registry note, and the analyzer had never been told it is a
harf. Adding one row moved the bank from **93.8% to 95%**.

Two things follow from that, and they are worth stating separately:

- **A closed-class table is only as good as its coverage, and nothing warns you
  about what is missing from it.** The analyzer never errored; it confidently
  read `أَمَّا` as an ordinary noun and moved on. Only a dataset that compares
  the engine against a human label makes an omission visible at all.
- Every entry in `PARTICLES` needs a `KIND_LBL` row beside it, or the note the
  analyzer pushes is `undefined`. The table and the labels are two halves of
  one thing and must be edited together.

Running total on the worked-sentence section since it shipped: **92% → 95%**,
25 named disagreements → 17, from two rules and one table row. The section has
now paid for itself twice.

## The participle stem is not the conjugating stem

Forms V and VI run their mudari on a FATHA — يَتَفَعَّلُ، يَتَفَاعَلُ — but their ism
fa'il takes a KASRA: مُتَعَلِّم، مُتَشَابِه. `sarfDerive` handed the conjugating
stem straight to the participle maker, so for those two forms the ism fa'il and
the ism maf'ul came out IDENTICAL — `مُتَنَصَّر` for both. Forms II and III were
fine only because their conjugating stem already carries the kasra.

It had been wrong since the engine was written and nothing caught it, because
**`sarfAudit` compares the tenses and not the participles.** A gate that checks
mazi, mudari, amr and the two governed cells is a good gate and it was silent
here for eleven versions. The corpus's own `مُتَشَابِه` — authored by hand in
chapter 6 — disagreed with the engine the whole time and no test compared them.

Two things now guard it: an explicit table of six root×form participles, and a
structural check that **the ism fa'il may never equal the ism maf'ul**. One
kasra apart is the entire distinction; equality means the distinction was lost,
whatever the letters happen to be.

The general form of the lesson: **a gate defines what "correct" means, and
anything outside it is unverified by construction.** When an engine grows a new
output, the gate has to grow with it or that output is folklore.

## The last letter's vowel is i'rab; every vowel before it is sarf

`findFormInParadigm` matched a stored cell two ways: exactly, and — failing
that — on the bare letters with the harakat stripped off both sides. The loose
pass is there for undiacritised input, which is real and has to work.

But the corpus is fully vowelled on both sides, and comparing it letter-only
meant `حُكْمُ` (a masdar on فُعْل) matched a cell of `حَكَمَ`, `عِلْمَ` matched
`عَلِمَ`, `قَصْرُ` matched `قَصَرَ`, `رَفْعُهُ` matched `رَفَعَ`. **Fourteen of the drill
bank's twenty-six named disagreements were this one missing comparison** — the
analyzer was calling masdars verbs all over the library.

The rule that fixes it is one sentence and it is the whole of the matter:

> **The last letter's vowel is i'rab and may move. Every vowel before it is
> sarf and may not.**

A governor moves the ending and nothing else, so `يَعْلَمُ` → `يَعْلَمَ` is the same
cell, while `حُكْم` and `حَكَمَ` are two different words that happen to share three
letters. Two corollaries fall out of it:

- **Compare per LETTER, not per string.** A stray mark in a string comparison
  belongs to nothing; the test has to know which letter each mark sits on.
- **Missing evidence is not contrary evidence.** Where either side has no mark
  on a letter, the letter proves nothing and the pair passes. That is what
  keeps undiacritised input working.

### …and the caller must not throw the vowels away first

Fixing the comparison exposed the second half. `RootFinder.candidates()` strips
the harakat to run its skeleton regexes, and `_find` was feeding those stripped
skeletons back to the corpus — so the sarf test arrived with nothing to judge
and `وَحُكْمُ` matched anyway. Same shape one layer up: `SentenceAnalyzer` passes
`MaEngine` an oracle for "is word *k* a verb?", and was calling it with `bares`.

**A test can only refuse what it is shown.** When you tighten a comparison, walk
every caller and check what it is handing over — a caller that pre-strips its
input silently restores the old behaviour and the new gate reports success.

## An agreement can be wrong

`رَوَاهُ` was scoring as a match: the human said verb, the engine said verb. It
was matching **رَأَى's imperative plural** — right class, wrong root, wrong verb,
wrong everything but the one field the score looked at.

The real reading needed an orthographic rule the candidate builder did not have:
**the alif maqsura is written as a full alif the moment a pronoun clings to it**
(رَوَى + هُ = رَوَاهُ). Until that spelling was offered, the paradigm never saw its
own word, and the accident stood in for it.

Two things follow. First, **a metric that counts CLASS agreement cannot see a
lemma error**, so a rising number is evidence about the metric before it is
evidence about the engine. Second — the useful half — **the fixes that raise the
score and the fixes that only correct the reasoning are the same work**: this one
was found by chasing a genuine regression in a neighbouring row, not by chasing
the number.

## No verb wears tanwin, the article, or the ta marbuta

The code already knew this: it was using the rule to retire a wrong *wazn*
twelve lines below the place where it was writing a wrong *class*. `خَفِيٌّ` —
the sifa mushabbaha on فَعِيل — was being read as a cell of `خَفِيَ` because the
letters lined up and a stored paradigm outranked the morphology.

**When a rule is decisive enough to overturn one output, ask what else it should
be overturning.** A fact used in one place and ignored in another is not a
subtle bug; it is the same bug written down twice.

## The passive is derivable, so derive it

Once the sarf test started reading harakat, `يُنَالُ` stopped matching `يَنَالُ` —
correctly, they are different words — and the verb vanished, because that
package never stored a majhul cell. Storing more cells is the fix that does not
scale. The majhul is a RULE:

- الماضي: ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ — نَصَرَ → نُصِرَ، عَلَّقَ → عُلِّقَ
- المضارع: ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ — يَنْصُرُ → يُنْصَرُ، يَنَالُ → يُنَالُ

Two details decide whether it works. A **shadda is not a vowel** and stays where
it is while the vowel under it changes. And when «ما قبل الآخر» is a madd alif,
the vowel it wants already sits on the letter before it — so the rule steps back
one letter rather than trying to vowel an alif.

Where a hollow root changes its LETTER as well (يَقُولُ → يُقَالُ) the build
**refuses to match rather than guess**. A stored cell answers those, and the
tightened test is what makes refusing safe: a miss costs a shortlist entry, a
wrong match costs the reading.

## Widening a frame is not the same as loosening it

Every `مَا` in Mukhtasar al-Manar is mawsula, and nine were still being read as
particles. The fixes were four separate rules, each naming the SHAPE it reads:

- **Definiteness has three routes, not one.** The definitional frame tested for
  `ال` and so missed `وَدَلَالَتُهُ مَا ثَبَتَ` (definite by idafa) and `وَهُوَ مَا
  يُبْتَنَى` (definite by being a pronoun). Same sentence shape, three spellings.
- **الْمُضَافُ إِلَيْهِ لَا يَكُونُ إِلَّا اسْمًا.** After a word that is mudaf by its very
  meaning — كُلّ، بَعْض، جَمِيع، غَيْر، مِثْل — the class is settled by POSITION, and
  no context can put a harf in that seat.
- **A sila may be a shibh jumla.** `مَا لَهَا وَمَا عَلَيْهَا`: a jarr phrase follows
  and no verb does. A negation would need a subject and a predicate to work on;
  a relative needs only something to hang on.
- **الْعَائِد.** A relative's clause must contain a pronoun pointing back at it; a
  masdariyya's clause has nothing to point back at, because it has become a
  masdar. That is the whole difference between `فِيمَا وُضِعَ لَهُ` and `بِمَا صَبَرُوا`,
  and it is the classical test, not a heuristic.

The discipline that keeps this honest: **promote, never remove.** Each rule
unshifts its reading to the head of the shortlist and every other face stays
underneath. `زَيْدٌ مَا قَامَ` is still a negation and is gated as one; `بِمَا
صَبَرُوا` is still masdariyya and is gated as one. A rule that can only ever add
a ranking cannot destroy a reading — which is why four of them could go in at
once without arguing about interactions.

## 100% means exactly what it measures

The bank reached 533 of 533 tokens in part-of-speech agreement. Written out, so
nobody reads it as more than it is: **the engines agree with the corpus's own
part-of-speech tag, on the sixty-five worked sentences they were measured
against.** It is not a claim that the analyzer's i'rab is right — i'rab is not
what is being compared. It is not a claim about unseen text.

What it does mean is operational: the named-disagreement list is empty, so this
set has stopped generating work. **The next round of engine fixes has to come
from NEW sentences.** A saturated benchmark is a retired benchmark, and keeping
it as a regression gate — which is what it now is — is a different job from
using it to find bugs.

## A saturated benchmark saturates against its CORPUS, not against the language

The previous entry closed by saying the drill bank had stopped generating work
and that the next fixes would have to come from new sentences. Chapter 15 was
written the same day; its five sentences produced **one** disagreement on
arrival, and that disagreement was a real hole in a rule shipped hours earlier.

So the prediction was right in form and wrong in tone. **Five sentences were
enough.** The bank does not need a new dataset to keep finding things — it
needs the next chapter, which the project writes anyway. That makes the worked-
sentence section cheap to keep useful, and it is worth saying because the
opposite conclusion (retire it, build something bigger) would have been the
expensive one.

## The ʿaid may be MUSTATIR — so test for the SEAT, not for the pronoun

The v116 ʿaid rule looks for a pronoun in the sila that points back at the mā.
`اسْمٌ لِمَا لَزِمَ الْعِبَادَ` has no such pronoun anywhere on the page, and the mā
is still mawṣūla — the ʿaid is the hidden fāʿil inside لَزِمَ.

What the page does show is the **vacancy**. A sila must leave a seat for the
returning pronoun; a maṣdariyya's clause is complete, because it has become a
maṣdar and has nothing to return to. And the vacancy is visible: **a verb that
names an object in naṣb and no doer has an empty fāʿil position.** الْعِبَادَ
wears a fatḥa, so it is not the doer, so something unwritten is — and after a
relative, that something is the mā.

The general shape, which has now come round three times in this codebase:
**when the thing a rule looks for can be concealed, look for the hole it left.**
The ʿaid can be hidden; the seat cannot. Same move as reading the case off the
sign rather than off the meaning, and as reading a governor's expectation
rather than the governed word's intent.

`بِمَا صَبَرُوا` is the control and is gated: its verb carries its own fāʿil (the
wāw), there is no seat, and it stays maṣdariyya.

## Choose the two examples so they sit on either side of the boundary

Chapter 15 uses تُدْرَكُ and يُقَاسُ within four sentences of each other, and that
is not decoration. تُدْرَكُ is the feminine of a passive the package stores only
in the masculine, so the majhūl **builder** has to make it — and can. يُقَاسُ is
the passive of a hollow verb, where the middle radical changes letter as well
as vowel (يَقِيسُ → يُقَاسُ), so no vowel rule reaches it and the paradigm must
store it.

The smoke check asserts both directions, including that the builder's output
for يَقِيسُ does **not** equal the stored يُقَاسُ. That negative assertion is the
valuable one: it fails the moment somebody "improves" the majhūl rule into
guessing at hollow roots, which would be a plausible-looking change that
silently starts inventing Arabic.

**A content chapter can be a test fixture.** When an engine has a documented
boundary, write a chapter that stands on both sides of it — the corpus then
holds the counter-example permanently, in real text, instead of in a fixture
somebody may prune.

## `stripAr` lives in the PAGE, not in the test runner

Twice in two turns a new smoke check called `stripAr` in Node scope and failed
the whole release with `stripAr is not defined`. Everything the reader defines
is available inside `page.evaluate` and nowhere else. Do the normalising **in
the evaluate block** and return a boolean; the assertions outside it should be
comparing already-computed values, not doing Arabic string work.

## Mukhtasar al-Manar is complete — sixteen chapters, 607 tokens

The last chapter, الِاجْتِهَادُ وَالتَّقْلِيد, is the only one in the book about a
PERSON rather than a text, and it closes a ring the smoke suite now asserts:
chapter 2 lists the four sources in RAFʿ as what the Law is known BY, chapter 16
lists the same four, same order, in JARR as what the mujtahid must know. The
gate compares the two token lists letter for letter after stripping clitics.
**When a text has structure, gate the structure** — a claim in a comment that
"the book is a ring" is worth nothing; a check that fails if someone reorders
either list is worth something.

## A final kasra is a jarr sign, and no verb is majrur

فَعَل the masdar and فَعَلَ the māḍī are spelled alike down to the last vowel, and
that is exactly the vowel the ṣarf test permits to move — so `طَلَبِ` matched a
cell of `طَلَبَ` and nothing on the word could have stopped it. The CASE stops it:
a kasra there is a case-ending, and cases belong to nouns.

This is the **fourth** member of a guard that started with one: tanwīn, the
article, the tāʾ marbūṭa, and now the jarr kasra all outrank a corpus cell
match. Each was added after a real word was misread. The pattern worth naming:
**when a comparison is deliberately blind to something, that blindness is where
the next bug will be.** The ṣarf test ignores the last vowel by design; the
misreadings it lets through are all decided by the last vowel, and they have to
be caught by a rule that looks exactly there.

The imperative keeps its reading — اِضْرِبِ الْوَلَدَ takes a kasra for the meeting
of two sākins, not for a case — so the guard is restricted to the māḍī and the
muḍāriʿ.

## Name a shape once, or two call sites will disagree about it

`فَعَلَيْهِ` — the last two words of the whole book — was read as a noun with the
root ع ل ه. The wāw/fāʾ peel only fired when what remained was in the
closed-class TABLE, and عَلَيْهِ is not a table entry: it is two words written as
one, recognised twenty lines later by a *different* piece of code walking
`ENCLITICS` against `JARR_HEAD`.

Two call sites, one concept, one of them ignorant of it. The fix was to give the
concept a name — `SentenceAnalyzer.fusedJarr(core)` — and have both the peel
test and the reading call it. **A shape that is recognised by inline logic in
one place will eventually be needed in another, and the second place will not
know.** Extract it the first time it is used, not the second.

## Leaving a disagreement in is sometimes the finding

Chapter 16 produced three drill-bank disagreements. Two were bugs and are fixed.
The third, `بِمَا لَا يَعْلَمُ`, is **kept**: the ʿaid would be a dropped MAFʿŪL, and
a maṣdariyya clause with an unstated object looks exactly the same on the page —
عَجِبْتُ مِمَّا صَنَعْتَ is the books' own example of the maṣdariyya and is read the
other way round. Any rule that moved the Manar token would have moved the
control too.

The engine does the right thing already: `sure: false`, both readings on the
shortlist, maṣdariyya first and mawṣūla second. That IS the promise this class
of engine makes — a correct shortlist, not a correct verdict — and a token that
exercises it is worth more in the file than a rule tuned to one sentence.

**Do not spend a rule to close the last point of a metric.** Check first whether
the remaining gap is the engine being wrong or the engine being honest.

## The Talkhīṣ is a story now, and an Ottoman source is not an unreadable one

`content/samples/talkhis-al-miftah` (L6, premium, 2 chapters, 10 sentences,
86 tokens; regenerator `tools/authoring/author_talkhis.py`) carries al-Qazwīnī's
own matn — the faṣāḥa definitions, balāgha in the utterance and in the speaker,
the ḥadd of ʿilm al-maʿānī, and the khabar/inshāʾ split.

The source is `research/sources/talkhis-al-miftah-balagha.txt`, an Ottoman-Turkish
sharḥ — and its ARABIC is vowelled and exact, which is the second time that has
been true on this shelf. **Do not write a file off because its prose is Ottoman.**
Chapter 1 s2–s4 are verbatim from it; everything else is the received matn,
restored where the page carries only the Turkish, and the manifest says which is
which line by line.

**Pick the passage for what it lets a reader do.** The Talkhīṣ defines its
science with the same frame Mukhtaṣar al-Manār uses for its own — عِلْمٌ يُعْرَفُ
بِهِ أَحْوَالُ… — so a reader who has finished the Manār can read that line
unaided. The smoke suite asserts the two token sequences match letter for letter,
because a cross-book parallel that lives only in a comment will rot.

## The app now shows its own working — تَحْقِيقُ الْآلَة

Every stored sentence carries two analyses, and the iʿrāb sheet now shows both:
the HUMAN parse the package was authored with, and the reading the engines derive
live from the letters — token by token, ✓/✗, with a `sure`/`guess` badge on every
engine row and a foot-note naming what is compared (part of speech, not iʿrāb),
that a disagreement may be the engine reporting an undecidable surface, and where
the rows are kept.

The part worth keeping is not the panel, it is **`posClass()`**. Agreement is now
defined ONCE in the reader — pronoun-is-an-ism; prep, conj and part are one class
— and `tools/gen_drills.js` calls it through the page instead of holding its own
copy. Those were two separate statements of the same doctrine, both correct, with
nothing to stop one being edited. **The number in the golden file and the number
on the screen are now the same number by construction.**

Same rule as `fusedJarr`, one turn later: a definition that two call sites need
gets a name.

## Confidently wrong is worse than undecided

The Talkhīṣ arrived at 99.6% with two disagreements, both `إِمَّا`, both marked
`sure: true`. Two causes, and each has been recorded here before:

- **`stripAr` keeps the hamza SEAT.** «إما» never matched the table's «اما» and
  «أما», so the word reached no closed-class branch at all. This file has warned
  about the seat since `IrabSign` was written; it caught the analyzer anyway.
- **أَمَّا and إِمَّا are two words sharing four letters.** أَمَّا detaches a topic and
  demands a fāʾ in its answer; إِمَّا offers a choice and is never used once — a
  second إِمَّا always answers it. The hamza's vowel decides, which is precisely
  the مِنْ / مَنْ shape the analyzer already implements, so the fix is the same
  three lines: read the vowel, pick the entry, and where there is no vowel keep
  the commoner reading with **`sure: false`** and a note naming both.

The general form, and it is why a `sure` flag exists at all: **a wrong answer
delivered with confidence costs more than a shortlist.** When a table lookup
misses, the fall-through path should be the one that says "I don't know" — here
it was the open-class path, which says "noun" and means it.

## Two gates, and the quiet one is not the useless one

Talkhīṣ chapter 3 produced **zero** new part-of-speech disagreements on arrival —
the worked-sentence bank, which has found something in every chapter since it
shipped, found nothing. The finding came from the **paradigm audit** instead:
`حَسُنَ`'s lām is a nūn, so it meets the feminine plural's own nūn and contracts
(حَسُنَّ), and `sarf_gen` wrote the fakk.

Two gates that measure different things will take turns being the one that
earns its keep. **Do not retire the quiet one** — on this turn the bank was the
quiet one, and on the previous three it was the only thing finding anything.

## The generator was missing the fifth bāb of the mujarrad

`sarf_gen.BABS` held naṣara, ḍaraba, fataḥa and samiʿa. The reader's
`SJ_BAB1_OF_MODEL` has known حَسُنَ (فَعُلَ يَفْعُلُ) by its model word since the
audit was written — so the app could *recognise* a verb of that bāb and the
authoring tool could not *build* one. Nobody noticed for a hundred versions
because no chapter had needed one.

**Two halves of one system can disagree about what exists, and the disagreement
is silent until content demands the missing half.** When adding to either table,
check the other.

Its ism fāʿil is regularly the ṣifa mushabbaha (حَسَن، كَرِيم), not فَاعِل — the
paradigm stores the mechanical حَاسِن because that is what the conjugator derives
and the audit compares, and the entry's own note says which is which.

## Choose the examples so the question completes

Three verbs, three chapters, two books, one question — which vowel, on which
letter, written or estimated:

| | verb | vowel | letter | manner |
|---|---|---|---|---|
| Manār 15 | يَجْرِي | damma | yāʾ | **estimated** (too heavy) |
| Manār 16 | يُفْتِيَ | fatḥa | yāʾ | **written** (light enough) |
| Talkhīṣ 3 | يُلْقَى | fatḥa | alif | **estimated** (carries nothing) |

None of these was chosen for its meaning. The smoke suite asserts all three in
one check, reaching across two packages — which is the point: **a teaching
sequence that spans stories has to be gated across stories, or the next author
breaks it without seeing it.**

## Never assert a RUNNING TOTAL — assert a floor

Written up one turn ago after chapter 16 broke chapter 15's gate, and then
repeated in the same session: the Talkhīṣ ch1/ch2 check asserted
`chapters !== 2`, so chapter 3 broke it on arrival.

A chapter check is about **the chapter it names**, never about how many exist.
`if (r.chapters < N)` is right in every case; `!== N` is a claim that the book
has stopped growing, which is false for every book in this library. Twelve
chapter assertions in the suite are floors and that is now uniform.

The reason this keeps happening is worth naming: **when you write a gate for
new content, the current total is sitting right there in front of you and is the
easiest number to type.** It is also the only number that is guaranteed to be
wrong later.

## The same doctrine, seen from the other side, is a SECOND rule

The `MaEngine` already had a "seat" rule: after a مَا, a verb that names a
manṣūb object and no doer has left the fāʿil position empty, and after a
relative an empty fāʿil position is where the concealed ʿāid stands. That rule
looks FORWARD from the mā.

Chapter 4 of the Talkhīṣ handed over the mirror image — إِذَا تَقَدَّمَ فِي
الْكَلَامِ مَا يُشِيرُ — where the verb is BEHIND the mā, three words back, and the
only noun between them is majrūr and so cannot be its doer. Same doctrine
(الْفِعْلُ لَا بُدَّ لَهُ مِنْ فَاعِلٍ), same conclusion (a word in the fāʿil seat is an
ism), and **the existing rule did not fire on it at all** — it was not looking
in that direction.

The lesson is not "add rule 6f". It is that when a rule is written from one
sentence, it silently inherits that sentence's WORD ORDER. Before calling a
qāʿida implemented, write the same doctrine backwards and check whether the code
still recognises it. Half the time it is a different rule wearing the same name.

## A peel is not a classification

`fusedJarr` peels مِنْهُ, عَلَيْهِ, مَعَهُ into head + pronoun. It was also
deciding, by the fact that it fired, that the head is a **ḥarf jarr** — and so
مَعَهُ came out as a jarr letter with its majrūr. مَعَ is a ẓarf: an ism, manṣūb,
and a muḍāf. The pronoun is its muḍāf ilayh, not a majrūr by a letter.

The operation was right and the label was wrong, which is the failure mode to
watch for whenever one function does both. The fix keeps the shared machinery
(one table, one loop, so the two can never disagree about what a fused shape
looks like) and returns a flag the caller branches on. **Share the mechanism,
split the verdict** — the opposite mistake, giving the ẓurūf their own peel loop,
would have been the "two call sites disagreeing about one shape" bug again.

## Ask the question the ORACLE can answer, not the one you want answered

The rule was right: مَا الْمَصْدَرِيَّة needs a VERBAL ṣila, so with no verb after it
the reading is impossible. The first implementation asked «does a verb follow?»
and broke عَجِبْتُ مِمَّا صَنَعْتَ — not because the rule is wrong but because the
verb oracle is a corpus lookup, and the corpus has never seen صَنَعَ. A bare māḍī
wears no prefix, so «not a verb» and «I have never heard of this word» are the
same answer.

Rewritten as **«is what follows something that CANNOT open a verbal clause?»** —
a pronoun, a demonstrative, a relative, a word wearing the article — the test
answers from the surface every time, and it stays silent exactly where it should:
a negation is not on the list, so بِمَا لَا يَعْلَمُ keeps its ambiguity.

Before writing a test, ask which of its two answers the engine is entitled to
give. If «no» can mean «I don't know», invert the test until the confident answer
is the one that fires.

## Name the two states you are already computing

`TaalluqEngine` had branched for months on «is the ʿāmil written or omitted?» and
returned two differently-shaped answers. Those two branches ARE ظَرْفٌ لَغْوٌ and
ظَرْفٌ مُسْتَقَرٌّ — the distinction every nahw book draws, and the reason a bare
jarr phrase can be a khabar. Nothing had to be derived; a label had to be
attached to a fact already in hand.

When a classical term turns out to be a name for a branch the code already takes,
that is the cheapest teaching the app can buy. Go looking for those before
building a new engine.

## A wall in the grammar is a wall in the walk

الصِّلَةُ سُورٌ: nothing inside a relative's clause attaches to anything outside it.
The taʿalluq walk had no such wall and hung the لَهُ of a ṣila on the masdar that
opened the sentence — a perfectly reasonable nearest-governor answer that no
grammarian would accept. The same shape had already appeared once, in the أَنَّ
search («a particle wall ends the search»), and was not generalised.

Any search that walks backwards through a sentence needs to know which words are
walls. Write them down as you meet them.

## New corpus data can make an old sentence genuinely ambiguous

Chapter 6 shipped the paradigm for زَادَ, and a smoke check that had passed for a
hundred versions began to fail: `قال زيد ان الله قادر` no longer found its qawl
verb, because **زيد is now a real passive cell** (زِيدَ) as well as a name, and
the sentence is unvowelled. The walk back to the verb stopped at what it took for
one.

Nothing was broken. The corpus got bigger and an accident stopped holding. The
fix is to vowel the fixture — زَيْدٌ with its tanwīn, which no verb wears — not to
weaken the lookup. **A test written on undiacritised Arabic is betting that no
future verb will ever share those letters**, and this library adds verbs every
chapter.

## The guard that reads a final vowel needs two more guards

«A mabnī cell's ending cannot move» is right, and it took three tries to state:

1. **Compare the CELL, not the written word.** A clitic pronoun brings its own
   vowel — رَوَاهُ ends in a ḍamma and رَوَى in nothing — and the match was made on
   the peeled candidate. Compare skeletons first and stand down where they differ,
   or every verb wearing an object pronoun is read as a noun.
2. **Missing evidence is not contrary evidence.** Undiacritised «قال» carries no
   final vowel at all, and the loose pass exists precisely for that input. Both
   sides must actually bear a vowel before their difference means anything.

Both are already written in this file, one for the ṣarf test and one for the
candidate builder. **A new rule in an old neighbourhood inherits the old
neighbourhood's traps** — read the entries around the code you are editing before
adding a comparison of your own.

## Rank on the evidence the DOCTRINE names, and emit in the old place

مَا الشَّرْطِيَّة was outranking the negation whenever any verb stood later in the
line. The doctrinal separator is JAZM — it is one of the jawāzim — so the fix was
to demand a muḍāriʿ showing jazm or a fāʾ on the jawāb.

The second half is a ranking discipline worth stating on its own: the weak reading
is emitted AFTER the negation, and the strong one is emitted **where the rule
always stood**, not unshifted to the head. Unshifting looked equivalent and was
not: rules that had already promoted a reading — the ʿāid, the seat, the
definitional frame — lost the head of their own shortlist to a shape that is
merely common. **Promote by position in the rule order, not by a flag**, unless
the rule really is the strongest evidence available.

## The peel table had no row for the commonest shape in the language

`RootFinder.peel` handled the maṣdars of the derived forms and the verb
skeletons, and had **nothing at all** for their PARTICIPLES: مُقَرِّر, مُوضِح,
مُسْتَفَاد, مُوَسْوِس, الْمُفْلِحُونَ all returned null. A table that has been extended
a dozen times can still be missing an entire family, and nothing complains —
`peel` returns null and the caller quietly shows no root.

Three fixes went in with the row, and each is a lesson this file has already
recorded in another neighbourhood:

- **Give the discriminator to the code that needs it.** مَفْعُول and مُفْتَعِل are
  the same five letters and the mīm's vowel decides — so `peel` takes the vowel
  as an argument now. This is the documented **مَكْتُوب → ك و ب** bug, live since
  the flashcard work, and it was never a missing pattern: it was a pattern
  matching on evidence that had been thrown away before it arrived.
- **A clitic can hide the feature a rule tests for** (the ما entry, again): the
  ARTICLE hid every pattern from its own table.
- **Inflection is not scale** (the IsmTagger entry, again): the tāʾ marbūṭa was
  counted as a fourth radical by the brand-new rubāʿī row.

**When you add a row to a mature table, re-run the words the table already
handled.** Two of the three fixes above were regressions introduced by the first.

## A rule you just wrote as a NOTE is a test you can run

Note 103 says a verb reaching the speaker's yāʾ must put a nūn in between —
عَصَانِي, never عَصَايَ. One chapter later عَصَايَ matched the māḍī of عَصَى, and the
refutation was already written down: **a bare speaker's yāʾ whose matched cell
does not contain it cannot be a verb cell.** No new doctrine, no heuristic — the
note turned round and became a guard.

The registry is now large enough that this is worth doing deliberately: when a
new disagreement appears, check whether a note already states the rule that
kills it. The notes were written to teach a reader; several of them are also
decision procedures, and those are the cheapest engine improvements available.

## Lower a floor only with the measurement in hand

The held-out two-guess score slipped to 67.9% against a floor of 68 and blocked
the release. Two ways to respond, and only one of them is honest: lower the
number, or find out why it moved.

It moved because the CORPUS moved — chapters 7 and 8 added ~90 labelled tokens
and reshaped the seventeen folds. That was established by **A/B on the same
page**: a copy of reader.html with the turn's engine change (eight demonstratives
added to PARTICLES) removed scores 51.0 / 67.9 too, identical to a tenth. So the
change was neutral and the data was the whole of the difference.

The floor is re-pinned at 67 **and the A/B is written into the check**, next to
the number, where the next person to hit it will read it. A floor lowered without
a measurement is not a floor; it is a note saying the gate has been turned off.

## The hamza SEAT, for the fourth time

`stripAr` keeps the seat, so «أَهَذَا» bares to أهذا and never matches a key
written with a plain alif. This file has warned about it since `IrabSign`; it has
now cost a smoke check, an analyzer branch and two probe scripts. **Fold the
seats for MATCHING and never for display** — and when writing a test that looks
a word up by its bare form, fold them there too, because the test is doing the
same matching the engine does.

## Probe the chapter's own words BEFORE authoring it

Chapter 9's two engine defects were both found by running its sentences through
`SentenceAnalyzer` and `RootFinder` in a throwaway script, before a single token
was written. Neither would have shown up in the drill bank afterwards: the bank
compares PART OF SPEECH, and both bugs got the part of speech right —
«لَفِي» was correctly a particle and «الصَّاغَة» was correctly a noun. What was
wrong was the label under it (a jarr clitic governing another jarr letter) and
the root beside it (ل ص غ, the article's own lām standing in as a radical).

**A metric that scores one field is blind to every other field**, and this file
has said so once already about lemma errors hiding behind class agreement. The
cheap countermeasure is not a better metric: it is to read the engine's whole
output for five sentences by eye, once per chapter, while the sentences are
still cheap to change.

## A peel is not a classification — the same lesson, one layer down

Chapter 4 split `fusedJarr`'s operation from its verdict because مَعَ is an ism.
The ب/ل/ك proclitic pass had the identical shape and was not looked at: it
peeled correctly and then asserted «this very word is the majrur» whatever
remained. **لَا يَدْخُلُ حَرْفُ جَرٍّ عَلَى حَرْفٍ** — a jarr letter never governs
another particle — so a lām before في is لَامُ الِابْتِدَاءِ الْمُزَحْلَقَة, not a jarr
clitic, and «إِنَّ الْإِنْسَانَ لَفِي خُسْرٍ» is the textbook case.

The general form: **when one function both transforms and labels, the label is
where the bug is.** The transform is usually driven by the surface and is right;
the label is driven by an assumption about why the transform fired. When you fix
one such pair, grep for the others in the same file the same day — this one sat
four chapters after its twin was fixed.

## ال is never a radical

Every ا-initial row of `RootFinder.peel` reads its first letter as a radical or
as the augment of إِفْعَال / اِفْتِعَال / اِنْفِعَال. Hand it a word still wearing the
article and it will happily read the article's own lām as a root letter:
الصَّاغَة → إِفْعَال on الصاغ → **ل ص غ**.

The fix is a sort, not a filter: candidates that still carry ال are tried LAST.
Dropping them would have robbed a genuine ا ل root (إِلَه) of its letters — and a
three-letter word is never article-peeled in the first place, so the sort costs
nothing and cannot lose a reading. **Reorder before you remove**, wherever a
candidate list is involved; this is the same discipline as «promote, never
remove» in the مَا rules.

Two more defects fell out of the same table on the same visit, and both are
entries this file already contains, in another neighbourhood:

- **The tāʾ marbūṭa is an ending, not a radical** — but its recursion guard was
  `length > 4`, and a four-letter word ending in the tāʾ leaves exactly a
  three-letter root. صَاغَة fell through to فَاعَلَ and answered «ص غ ة».
- **فَاعِل and فَاعَلَ are one skeleton** once the ʿayn's vowel is stripped, and
  the row picked the rarer of the two, so every ism fāʿil in the language came
  back as a Form III verb. Same shape as مَفْعُول / مُفْتَعِل, which was fixed by
  passing the mīm's vowel in — here the honest fix is cheaper: **name both.**

## Three chapters, three notes, one letter

The registry gained `anwa-al-lam-al-tarif`, `tarif-bil-idafa` and
`tankir-al-musnad-ilayh` rather than one note on «definiteness». The temptation
was to extend chapter 8's `tarif-al-musnad-ilayh`, whose title names the
relative and the demonstrative — and a note whose title no longer covers its
contents is how a registry stops being navigable. **Extend a note when the new
material is the same question; write a new one when it is the next question.**

## The probe found seven defects, and none of them was in the metric

Chapter 9 introduced the practice of running a chapter's own sentences through
the engines before authoring them. Chapter 10 did it again and the yield was
seven, where the drill bank — run on the same words afterwards — reported ONE.

That gap is the entry. **The bank compares part of speech and nothing else.**
Every one of these got the part of speech right and was wrong underneath it:

| word | the bank saw | what was actually wrong |
|---|---|---|
| جَاءَنِي | verb ✓ | the speaker's yāʾ called a **muḍāf ilayh on a verb** |
| نَفْسُهُ | noun ✓ | reached no lexicon entry; read as «probably a verb» |
| الْحَقُّ | noun ✓ | root **ل ح ق** — the article's lām as a radical |
| التَّاجِرُ | noun ✓ | root **ا ج ر** on تَفَعَّلَ |
| أَخُوكَ | noun ✓ | root **خ و ك** — a case-letter and a pronoun |
| كُلُّهُمْ | noun ✓ | **«jazm by the sukun»**, on a noun |
| عَمْرٌو | noun ✓ | flagged by both harakat auditors as a bad tanwīn |

A benchmark is a floor, not a mirror. Reading five sentences of engine output by
eye, once per chapter, costs ten minutes and sees the other fields.

## نُونُ الْوِقَايَةِ — the note was right, the peel had never been told

Note 103 has said since it was written that a verb reaching the speaker's yāʾ
puts a nūn between them. The enclitic peel listed «ي» and not «ني», so جَاءَنِي
came apart as «جاءن + ي» and the yāʾ was named a **muḍāf ilayh — on a verb**,
which is impossible twice over.

This is the second time a registry note has turned round and become a guard
(عَصَايَ was the first, one chapter earlier). The registry is now large enough
that this is worth doing on purpose: **when a note states a rule about a SHAPE,
grep the code for the place that reads that shape.**

The peel asks the oracle the answerable question — «is what remains a verb the
corpus knows?» — and where the corpus is silent the old peel runs. مَبَانِي must
not lose two letters because it happens to end in a nūn and a yāʾ.

## A geminate's third radical is the SHADDA, and `stripAr` eats it

`RootFinder.find("الْحَقُّ")` answered **ل ح ق** — and had done since the peel
table existed, for every definite geminate noun in the library: الرَّبُّ، اللِّصُّ،
الْجِنُّ، كُلّ. Two separate facts have to be in hand before the word can be read
at all, and neither was:

1. **Is it definite?** The vowel says so and nothing else does: the article's
   alif is a hamzat al-waṣl and carries nothing, while أَلْزَمَ opens on a hamza
   SEAT with a fatḥa. Read off the bare letters the two are the same word.
2. **Is it doubled?** Strip the harakat and حَقّ is two letters. Every other noun
   leaves three, so a two-letter remainder is itself the signal — but only when
   the shadda is really there, which is why الْيَد is refused rather than doubled
   into «ي د د».

The rule that follows is the project's own line again: the shadda is read off
the VOWELLED word, and the doubling is then a fact rather than a guess.

**And the `stem` chain that reads the mīm's vowel is not a general stripper.**
It takes a bare lām and a bare kāf off unconditionally, which is harmless when
all you want is one character of evidence and fatal when you want the letters:
it ate the assimilated radical lām of اللِّصّ and the kāf of كُلّ, and both words
then had no geminate left to find. **A helper written for one question will be
wrong for the next one — read what it actually does before reusing it.**

## The vowel that decides may be at the SEAM

`أَكْثَرُهُمْ` matched the Form IV verb أَكْثَرَ and the mabnī-ending guard could not
see why not: the word ends in a sukun on the mīm, because it ends in a pronoun.
The vowel that settles it is on the letter the pronoun was hung on — a ḍamma,
where a māḍī is mabnī on the fatḥa and cannot move.

Three separate mistakes were made getting this right, and all three are variants
of entries already in this file:

- **the pronoun's own vowel is not the host's** — using it made every verb
  wearing an object read as a noun;
- **compare skeletons with the pronoun off on BOTH sides**, or the guard never
  fires at all;
- **a literal «هم» never matches a vowelled word**, because it is ه + damma + م +
  sukun. The pattern has to allow a mark between the pronoun's own letters —
  the fatha-before-shadda trap, one layer along.

## A silent letter is an exception, not an error

`عَمْرٌو` was flagged by both harakat auditors as a tanwīn before the end of the
word. It is: the wāw of عَمْرو is silent and is written for exactly one reason —
to tell the name from عُمَر in an unpointed text — and it appears in rafʿ and
jarr only, because in naṣb the alif of the fatḥa already distinguishes them
(عَمْرًا). This is the books' own spelling, like the بْنُ the auditor already
knew, and the exception went into the reader AND into `validate_content.py` in
the same edit. **KEEP THE TWO IMPLEMENTATIONS IN STEP** is written above; this
is the second time it has been paid.

## Retire a warning by writing the content that answers it

`tawkid`, `atf-bayan` and `sifa-mushabbaha` had carried «no example is sourced
from a story» since they were written, because no chapter had used them in real
text. Chapter 10 uses all three, so the warnings were retired by ANCHORING —
not by silencing the check.

One of the three needed more than an anchor. `atf-bayan`'s «جَاءَ أَخُوكَ زَيْدٌ» is
the classical khilāf case, and the Talkhīṣ files those very words under BADAL —
which is how this chapter tags them. Two notes quietly claiming the same words
is the tibāq/muqābala failure mode; the note now names the disagreement and says
what turns on it. **Where the books disagree, say they disagree.**

## The closed-class key rides the row now — flattening it was costing doctrine

Three of chapter 11's defects were one omission wearing three masks. The
analyzer marked هُوَ, أَنَا and هٰذَا all `kind: "noun"` — correctly, they are
asmāʾ — and threw away WHICH closed class put them there. Downstream, every
pass that needed the distinction improvised or failed:

- the idafa chain annexed هُوَ (الضَّمِيرُ الْمُنْفَصِلُ لَا يُضَافُ — a detached
  pronoun takes neither seat; the demonstrative legitimately takes the second:
  مِثْلُ هٰذَا is real);
- the MaEngine's verb ORACLE passed أَنَا, because its bare letters match a
  stored paradigm cell, and مَا أَنَا قُلْتُ هَذَا became a conditional whose
  first "verb" was a pronoun;
- nothing could ask «is this row a pronoun?» without re-deriving it.

The fix is one line at the particle branch — `row.pk = p.k` — and then every
consumer branches on knowledge instead of resemblance. **When a classifier
collapses classes for one consumer's convenience, every OTHER consumer pays.**
Same lesson as posClass, from the other side: there the collapse was the right
definition of agreement; here it silently deleted the table's whole point.

## The seam is a doctrine now, not a patch

Chapter 10 read the seam vowel in ONE guard (أَكْثَرُهُمْ). Chapter 11 found the
same blindness in IrabSign — إِلَهُنَا read as a MAQSUR because the نا's alif was
taken for the word's last letter — and the fix was promoted from a guard to a
rule: peel the enclitic pronoun, read the HOST, and say in the note that the
sign sits at the seam. Three guards keep it honest, each bought by a word that
would have broken it: the host must end in a WRITTEN vowel (مُلُوكَ's waw
carries none), must keep three bare letters (وَجْهُ's ha is a radical), and the
kaf tails are refused after a fatha (مُبَارَكَ) — refusal beats a wrong peel.

The payoff was immediate and unplanned: the model feature `irc-` (below) is
only informative BECAUSE the sign engine now answers correctly on
pronoun-bearing words. **Fix the rule engine first and the statistical layer
inherits the fix** — the reverse order would have taught the model the bug.

## Ablate in pairs when the second feature depends on the first

The v129 ML wave shipped two features measured together: `irc-` (IrabSign's
settled case) and `pk-` (the closed-class key). Base 52.9/70.5 → both 55.0/72.9
resubstitution — and held-out CONFIRMED it, 50.9/67.8 → 52.8/70.2 over 17
folds, the largest single gain since the governor features. Floors raised to
51.5/69 with the measurement written into the check.

Two disciplines held: the held-out number is the one that moves floors
(resubstitution alone flattered a Viterbi layer once, and it was catastrophic
held-out); and the ablation ran on the SHIPPED base so neither feature was
double-counted. Worth naming: `pk-` is the same closed-class key the analyzer
fix landed this turn — **a fact taught to the rule layer for correctness
reasons turned out to be worth two points to the statistical layer for free.**

## The sixth guard reads the context, and only the context can read it

دَارِ the majrur house and دَارِ the amr of دَارَى («humour him!») are the same
letters and the SAME VOWELS. Five guards read the word — tanwin, article, ta
marbuta, jarr-kasra, mabni-ending — and all five pass this pair, because
nothing on the word separates them. The sentence does: لَا يَدْخُلُ حَرْفُ جَرٍّ
عَلَى فِعْلٍ, and the İzhar layer had already computed «a jarr letter stands
before this word» — the fact just wasn't written on the row where the
corpus-cell branch could see it (`row.afterJarr`).

**When every word-level guard passes and the reading is still wrong, the next
guard is a context guard** — and the context is usually already computed
somewhere upstream, waiting to be stamped on the row.

## iOS Safari is a target, not a variant

The reader ran "fine" in desktop Chrome and Playwright for 130 versions while
carrying four defects every iPhone user would meet in the first minute: sheets
sized in vh (which iOS measures with the toolbar RETRACTED, so the sheet's
head hides under it — dvh fixes it and the vh line stays as fallback), inputs
under 16px (iOS zooms the whole page on focus), no touch-action on buttons
(the 350ms double-tap wait makes every quiz feel broken), and sheet overscroll
chaining to the page behind. None of these is visible in any desktop test.

The smoke suite now has an iOS-shell gate: viewport-fit, the apple metas, the
touch icon, safe-area padding, dvh, text-size-adjust, overscroll containment,
and a LIVE input measured at ≥16px. The rules are all in one commented block
at the top of the stylesheet, each line naming the iOS behaviour it answers —
because a safe-area inset with no explanation is the first thing a cleanup
deletes.

## A note's rule, read backwards, is a guard — third time, so it is a method

Note 103 says a verb reaching the speaker's yāʾ puts نُونُ الْوِقَايَةِ between
them. Chapter 10 used it forwards (peel «ني» whole); chapter 11 used it as a
refutation (عَصَايَ cannot be a verb cell); chapter 12 used it BACKWARDS: a bare
final yāʾ that completes a stored verb cell must be a RADICAL, because if it
were the object pronoun the nun would be standing in front of it. That closed
the يُعْطِي defect — the peel was taking a naqis verb's third radical for «its
maf'ul bihi».

Three uses, one sentence of doctrine. When a registry note states a rule about
a SHAPE, it is worth actively asking all three questions: what does the rule
peel, what does it refuse, and what does its absence prove.

## The first persons never take the group's waw

أَسَرُّوا was read as «one of the five verbs with its nun dropped» — the وا
branch tested for a person prefix with /^[يتنأ]/, and the hamza of Form IV
passed it. But the class is يت ONLY: أَفْعَلُ (1s) and نَفْعَلُ (1p) have no
plural-waw forms at all, so an opening hamza before وا is always the verb's
own. A person-prefix class copied from another rule brought along two members
that are impossible in THIS position. **A closed class is closed per POSITION,
not per concept** — the five-verbs prefix set and the group's-waw prefix set
overlap without being equal.

## Refuse the row when the skeleton cannot split the readings

مِثْلُكَ answered «ث ل ك»: the م(...) row read the radical mīm of مِثْل as the
participle prefix. The kasra on the mīm disqualifies the whole participle
family (they open مَ/مُ, never مِ) — but what remains is TWO readings, the
instrument (مِبْرَد) and the radical mīm (مِثْل، مِلْك), and nothing in the
skeleton separates them. The row now returns null there, and the enclitic
candidate (bare ك, newly added) lets مِثْلُكَ find م ث ل on the next try.

The discipline: **a rule that cannot name the right answer should step aside
rather than name a wrong one** — refusal costs a shortlist entry; a wrong
answer costs the reading. Same call as the hollow-passive builder refusing
يَقُولُ, now applied to a peel row.

## The provenance of a candidate is evidence about the candidate

حَاجَتِي lost its possessive yāʾ in the candidate builder and the remainder
حاجت matched the ch11 hollow-māḍī row (قَالَت-shaped). But that candidate was
PRODUCED BY STRIPPING a possessive pronoun — and a verb's feminine-tāʾ never
stands before a possessive yāʾ (the verb would take نِي). So the tāʾ in a
stripped candidate is always the unrolled marbūṭa, and the row must refuse it.
`peel` now receives a `sub` flag: candidate-was-stripped. **A candidate list
flattens away how each candidate was made, and sometimes the making is the
discriminator.** Fourth parameter, same lesson as the mīm's vowel — evidence
was being thrown away before the rule that needed it ran.

## Teach the khilaf as a khilaf

Chapter 12 carries a real disagreement: the nahw scholars read شَرٌّ أَهَرَّ
ذَا نَابٍ as an outright qasr (taʾwīl: مَا أَهَرَّ ذَا نَابٍ إِلَّا شَرٌّ) and Sakkākī
saves his two-condition rule by reading the tanwīn as taʿẓīm. The Talkhīṣ
records three objections and keeps both schools on the page — so the token,
the note and the anchors all STATE the divergence instead of picking a winner.
This is the second khilaf the registry teaches by name (the atf-bayan/badal
reading of جَاءَ أَخُوكَ زَيْدٌ was the first). A teaching that hides a khilaf
teaches less than the books do — and a data model that can only store one
verdict per token would have forced the hiding. The i'rab prose is where the
both-schools answer lives; keep it prose.

## Count the isnads — a gradation that is pure syntax

The chapter's centerpiece teaches something rare: a BALAGHA gradation that
falls out of NAHW arithmetic. أَنْتَ لَا تَكْذِبُ (two isnads: khabar→mubtada,
verb→fāʿil) beats لَا تَكْذِبُ (one) beats nothing, and لَا تَكْذِبُ أَنْتَ is NOT
a second ascription — the sentence was complete before the pronoun arrived, so
the trailing anta is a tawkid of the hidden fāʿil, one isnad plus an emphasis.
The jumal rows carry the count explicitly. When a rhetorical claim can be
grounded in a countable syntactic fact, ground it — the learner can check
arithmetic; they can only believe an assertion.

## The clitic-peel ate the rule's own triggers — for two hundred versions

`MaEngine.naked()` strips a leading و/ف/ب/ل/ك before the table lookup, and كل
begins with a kaf, بعض with a ba. So rule 6c — «the mudaf-ilayh seat after
كل/بعض is closed to particles», written in v116 and credited in this file with
real accuracy — had NEVER FIRED for its two commonest triggers: the lookup saw
ل and عض. It kept passing every gate because the gated sentences used غير and
مثل, whose first letters are not proclitics.

The fix asks before peeling: if the word as written is already a table word,
it IS the word. The general form has been in this file since the ما entry («a
clitic can hide the very feature a rule tests for») — this is its sharpest
instance yet, because the hidden feature was the rule's own trigger list, and
because the gate's example sentences happened to dodge it. **When a rule is
keyed on a closed set, test the rule against EVERY member of the set once** —
a five-line loop in the suite would have caught this the day it shipped.

## An accident can hold a reading up — fixing the bug underneath exposes it

Tightening the jazm-shape test (a naqis ى is not «showing jazm») broke a bank
row that had agreed for twenty versions: وَمَا نَابَ عَنْهَا. On investigation the
agreement was STANDING ON the bug — the spurious shartiyya (an ism reading)
happened to share the human label's class, so the metric said ✓ while the
doctrine underneath was wrong. The fix took the accident away and the TRUE
reading (the matns' list-frame mawsula) turned out to have no rule at all;
rule 6f now states it: a joining waw carries the ma, a noun before it to hang
on, and the verb's fa'il seat concealed.

This is «an agreement can be wrong» meeting «when every word-level guard
passes, the next guard is a context guard». The practical rule: **when a fix
breaks an old agreement, do not restore the old behaviour — find out what the
agreement was standing on.** Twice now the answer was: an accident.

## The naqis stem goes in bare — the generator trap has a naqis edition

تَشْتَهِِي shipped with a doubled kasra: `derived_naqis` takes the mudari stem
WITHOUT its final vowel (جْز, not جْزِ — the maker appends the ending), exactly
as `amr_attach` appends its own sukun. The mazi stem DOES carry its vowel
(جَزَ). One signature, two conventions, and the ch8 precedent (غَشِيَ built
through `entry` by hand) had hidden the asymmetry. The bank caught it within
the hour — تَشْتَهِي failed its own corpus lookup because the stored cell was
one codepoint wrong and visually identical. **NFC-invisible corruption is what
the exact-match layers exist to catch; trust the failed lookup, not your eyes.**

## The madda is two hamzas, and the corpus spells it the engine's way

آخُذُ is what the books print; أَأْخُذُ is what the conjugator assembles; and the
first person of every hamza-initial verb was unreachable from its written form
— لَمْ آخُذْ parsed as a jarr-less MUDAF. The fix is a matching-only unfold
(آ → أَأْ in formCandidates), the same doctrine as folding hamza seats: **spelling
equivalences live at the matching layer, never in the data and never in the
display.** The stored paradigm stays in the engine's mechanical spelling
because the audit regenerates it; the reader's eye never sees it.

## The NFC order of a shadda and its vowel is not fixed — test both, every time

The إِنَّا branch tested `/نّ/` and never fired: NFC sorts the fatha (ccc 30)
BEFORE the shadda (ccc 33), so the written نَّ is nun+fatha+shadda and the
letter is never adjacent to its doubling. The lammaJazim test three lines down
had known this for two hundred versions (`/مَّ|مّ/`); the new branch had to
relearn it. **Any regex that reads a shadda next to a letter must allow marks
between them** — and when a branch you just wrote doesn't fire, diff it against
the nearest working sibling before theorizing.

## The closed-class table is also a refusal list — and the branch must be reachable

Two halves of one ch14 lesson. (1) إِيَّاكَ answered فَعَّال — «an intensive or a
trade» — because RootFinder had never been told that closed-class words are
jamid: the fix is corpus-first, then REFUSE for any PARTICLES word, the same
shape as the five-nouns table (a rule written from the surface cannot recover
what the surface does not carry — here there is nothing to recover at all).
(2) The إِنَّا fix lived INSIDE the particle branch, and the bare «إنا» (hamza
seat kept by stripAr) was not a PARTICLES key — so the branch that decides was
unreachable for exactly the spelling it was written for. **A fix inside a
guarded branch is only as good as the guard's key set**: when a new sub-branch
doesn't fire, check whether its parent branch is entered at all.

## The blanket unfold failed where the narrow row succeeded — the bank drew the line

مُقِرًّا answered ق ر و/ي: a guessed weak third radical where the surface
carries the letter, in the shadda. The obvious fix — unfold every shadda into
a doubled letter among the candidates — doubled the SUN LETTER of الدَّرَاهِمِ
(article assimilation) and the AUGMENT of مُحَمَّد (form doubling), and the
drill bank refused both within the minute. A shadda attests a geminate root
only in a known shape; everywhere else it is assimilation or morphology. The
shipped rule is the narrow one: mim prefix + two remaining letters + shadda
attested on the second. **When a general principle and a narrow row disagree,
the bank is the arbiter — and the narrow row that survives it teaches more
than the principle that didn't.** (The failed attempt is recorded in the row's
own comment, so nobody re-derives it.)

## «What stands before the last» means the STEM's last — suffixes are not the word

sjMajhul voweled يَرْجِعُونَ's wāw as «ما قبل الآخر» and the derived passive of
every suffixed cell was garbage; تُرْجَعُونَ matched nothing and read as Form
IV. The classical rule is stated on the singular base and the person suffixes
ride outside it — the code now steps back over ونَ/انِ/ينَ before applying the
vowel. Same family as the iṭlāq alif (أَتَاكَا = أَتَى + كَ + a metre-alif the
grammar does not count) and the tanwīn's seat (مُقِرًّا's final alif is
orthography for the fatḥatan, not a maqṣūr ending): **Arabic writes three
kinds of tail the rules must not read as stem — person suffixes, the tanwīn's
seat, and verse padding — and each one now has its explicit step-over.** The
derived cell also keeps the PERSON of the active it was built from; a derived
majhūl that reports «he» for a you-pl cell is a correct derivation wearing the
wrong name.

## The next word's class is a diagnostic — إِذَا reads forward

The table gave إِذَا one label («conditional») and the fuja'iyya did not
exist: خَرَجْتُ فَإِذَا زَيْدٌ read its زَيْدٌ under a conditional's expectations.
The two readings differ by exactly one observable — what follows: the shart
idha demands its verb, the surprise idha opens a nominal sentence. Same
method as the مَنْ fatha/kasra split and the إِنَّا shadda: **when a closed-class
word wears two faces, find the single surface observable that splits them and
write the branch on it** — and teach the essence-khilaf (harf for al-Akhfash,
zarf for al-Mubarrad) instead of flattening it.

## The vowel left behind names the letter that fell — the heavy nun edition

يَقُولُونَ + نَّ loses its raf' nun, then its group's waw against the two sakins
— and the damma stranded on the lam is the waw's headstone. formCandidates
reads it: damma → restore ونَ, kasra → restore ينَ, fatha → the singular.
Same family as the maqsura returning before a pronoun and the madda unfolding:
**the surface never destroys information without leaving a receipt, and the
matching layer's job is to read receipts.** The restoration is matching-only;
the stored cell stays canonical.

## A table the engines READ is a table that must be COMPLETE

نَحْنُ was in three other pronoun lists but not in PARTICLES — and MaEngine's
rule 6d reads pronounhood off PARTICLES alone, so the bayt's first بِمَا
silently lost its mawsula. The lesson is not «add نحن»; it is that a
closed-class table consulted by other engines is an INTERFACE, and a missing
row is not a cosmetic gap but a wrong answer somewhere else. When adding a
closed-class behavior, grep for every OTHER list that claims to enumerate the
same class and reconcile them (هُمَا and أَنْتُمْ rode along; the zarf-sila
list was missing عندك the same way).

## Two words can share every letter AND every vowel — then only knowledge splits them

Chapter 15 hit the limit twice. سَأَلْتَهُمْ vs سَيَقُولُ: the sin peel cannot
know a radical from the future prefix, but the corpus can — a paradigm whose
lemma begins with sin keeps its sin. رَاضٍ vs بَابٍ: the manqus and the hollow
are surface-identical (three letters, middle alif, kasratan), and the
glossary decides; where it is silent, keep the commoner class as the honest
default rather than refuse both. **The escalation order is fixed: surface
observable → corpus/glossary knowledge → honest default with the khilaf
stated.** Never invert it — a rule that guesses where knowledge exists is a
bug, and a refusal where an honest default exists is a worse teacher.

## The model's missing shape is the model's confident error

IsmTagger had no فَعْل/فِعْل/فُعْل — so صَبْر, the commonest noun shape in the
corpus, was answered أَفْعَل at 0.30: a model without the right class does not
abstain, it picks the nearest wrong one with conviction. After adding the
shapes, held-out top1 ROSE (91.2 over 43 shapes vs the 86 floor) — coverage
gaps hurt twice, on the missing class and on everything it steals from.
Check the shape inventory against the corpus's commonest patterns, not
against the derivational textbook order the inventory was first written in.

## The sukun is the shadda's other half — one observable, four splits now

مِنْ/مَنْ split on the mim's vowel, إِنَّا on its shadda, إِذَا on the next word's
class — and now إِنْ/إِنَّ and لَكِنْ/لَكِنَّ split on the nun: sukun is the
conditional (or the light istidrak, governing NOTHING), shadda the inna
family. Two disciplines rode along. First, the table's generic label was
POPPED, not left standing: «inna family — nasb on its noun» followed by
«governs nothing» is not a refinement, it is a contradiction, and a reader
keeps whichever they read first. When a branch OVERRIDES the table rather than
narrowing it, remove the table's note. Second, the promised expectation moved
with the reading — the next word had been awaiting a mansub ism that never
comes; it now awaits the shart verb.

## A peel that rides over another peel must re-check the second peel's guard

The interrogative hamza peel was extended to ride over a joining waw
(أَوَكُلَّمَا = أ + و + كلما) — and the bank refused it within the hour: أَفْعَمَ
read as أ + فَ + عَمَّ, because the extension tested only the LETTERS. The
original wa/fa peel never fires without its own guards; a compound peel
re-implements the inner peel and silently drops them. The missing one was the
vowel: **a joining letter always wears the joiner's fatha**, and أَفْعَمَ's fa
carries a sukun — a radical's dress. When peel A learns to ride over peel B,
copy B's guard list into A's condition, or the bank will do it for you.

## The refusal list grows by DRESSES, not by words

RootFinder's closed-class refusal began as one check (the bare word in
PARTICLES) and chapter 16 added three more dresses the same closed class
hides in: a joining wa/fa over a particle (وَهْوَ), a fused jarr/zarf head with
its pronoun (مَعَهُ), and the merged speaker's-ya (إِلَيَّ, told from the name
عَلِيّ by the lam's fatha). Each dress needed its own guard against a REAL
word wearing the same letters — وَفِيٌّ is saved by its tanwin and shadda.
The pattern: **a jamid word has as many spellings as the orthography has
fusions, and every fusion the analyzer learns to READ, the root finder must
learn to REFUSE.** The two engines walk the same list in opposite directions.

## A hedge is evidence-shaped, not position-shaped

The glossary-override for rules-roots first fired only on the GUESSED
positions (the weak-note flags) — and أَمِير answered م ي ر with no flag at
all, because the peel's error was reading the hamza as أَفْعَل's augment, not
guessing a weak seat. The shipped trigger is any rules-root carrying a weak
letter ANYWHERE: that is where the peel's confusions live (augment-vs-radical,
turned letters, seats), and it is exactly where a lexicographer's entry
outranks a table. The bank held at 99.8% through the widening — the arbiter
again — and the corpus/verb path is untouched, so a sound rules answer is
never displaced. **Write the trigger from where the errors come from, not
from where the flags happen to be.**

## A gate that pins the honest hedge will block the exact answer

Three old gates failed the v133 release: مُسْتَفَاد expected «ف و/ي د», قَائِم
expected «ق و/ي م», الصَّاغَة expected the same hedge shape — and the engine now
answers ف ي د, ق و م, ص و غ exactly, from the glossary. The hedge was the
honest BEST at the time it was pinned, and the checks enshrined it as the
truth. When an escalation layer is added (surface → lexicon), every gate that
pinned the lower layer's honest uncertainty must be widened to accept the
higher layer's certainty — exact first, hedge still allowed. And the reverse
guard matters equally: the override compares against the DISPLAYED root (the
raw peel root still carries the hamza seat), fires only where the lexicon
actually disagrees, and keeps the rules' wazn where both name the same
radicals — the override corrects roots; it must not strip the scale off
answers that were already right.

## The ShartEngine reads the FRAME, and the adat's asl is what makes nukta legible

The conditional bab was scattered: the analyzer knew the adats as table rows,
the notes taught the doctrine, and nothing connected an adat to ITS shart and
ITS jawab. `ShartEngine.read(rows)` builds the frame as an exact engine — and
the design decision worth recording is that the TENSE-CHECK emits a NUKTA,
never an error: لَوْ + muḍāriʿ is not a violation to flag but the istimrar
reading to name, because the asl is precisely what makes the shift legible as
rhetoric. An exact engine over a rule system should encode the rule AND the
licensed departures, each with its classical name — the departures are where
the balagha lives, and an engine that only validates would erase them. (Also:
the adat may hide behind its own peels — read it off the analyzer's LAST
segment, which is already undressed; أَوَكُلَّمَا taught that within the hour.)

## The governor's key is worth two points held-out — the İzhar doctrine, again

The v129 pk- feature gave the model the word's OWN closed-class key; v134's
ppk- hands it the PREVIOUS word's. Resubstitution 56.1/72.5 → 58.2/74.6,
held-out A/B on the same corpus 52.6/70.5 → 54.7/72.1 over 17 folds — the
largest gain since pk- itself, and the same lesson from one seat over: what a
word IS depends on what GOVERNS it, and the governor's identity is cheap
surface knowledge the closed-class table already holds. Note the harness trap:
the shipped ablate_features.js predict-loop predates ctx and never passes
prevFull, so any ctx-based feature reads as noise there — the scratchpad
protocol passes ctx in BOTH train and predict, and cv_eval/crossVal confirm
held-out. When a feature needs context, check the measurement rig hands the
context over on both sides, or the rig will veto a real gain.

## A game that teaches a rule must read the rule's OWN table

gShart's refutations are ShartEngine.DOC lines — the same object the Jumla
lab renders — so the game can never drift from the engine. This is posClass
and fusedJarr again, at the game layer: the moment a drill paraphrases a
doctrine that lives in an engine, the paraphrase and the engine begin to
diverge, and the learner meets two versions of one rule. Wire the game to the
table; write the table once.

## Pattern behind chrome, never behind tashkeel

The arabesque tile is one inline SVG at 13% neutral alpha, laid behind the
surfaces that FRAME content (header, continue card, stat strip, frame cards)
and deliberately never behind running Arabic — pattern under harakat is
noise, and the reader column stays plain. One neutral half-grey tile serves
both themes; a colored tile would need two and could drift. The combo chip
follows the same restraint: feedback, not score — it renders only from ×2 up,
resets on a miss, and its animation sits behind prefers-reduced-motion.

## A global lex key must agree with itself across packages

`nounFromCorpus` reads every package's glossary as one corpus, so a key that
lives in two packages with two different claims is a bug the engines will
surface in whichever order the packages load: `zayd` was propn in the Talkhīṣ
glossary and plain noun in jumal-al-tadrib, and the propn guard on the
learned scale silently stopped firing after a rebuild. When a lex key already
exists elsewhere, the new entry must MATCH it — and when a guard keys on a
pos, check every package that owns the key, not the one you are authoring.

## The article strip owns the sun-letter shadda

Stripping ال must take the assimilated lām's shadda with it: الشُّجَاعُ minus
the article is شُجَاع, not شُّجَاع, and the leftover mark walked straight into
IsmTagger's sh:/m1: features and sold فَعَّال over فُعَال. The license is
absolute — no Arabic word begins with a doubled consonant, so a word-initial
shadda after an article strip is always the article's. Remember NFC puts the
vowel BEFORE the shadda: the strip regex must let the mark group ride between
the letter and the shadda (`/^([ء-ي])([ً-ٰ]*)ّ/`).

## The wajh is the content, so it ships as data

«Put detailed explanations in the chapter» does not mean longer prose: the
Belâgat vecihleri went in as NAMED jumal rows — two per sentence, each
carrying its wajh (no-ḥaṣr, tafkhīm, taḥqīr, takhsis, qaṣr in both
strengths, the Rāzī khilaf) — plus one catalogue note the rows point into.
A layer the user asked for gets a floor in the smoke gate (every ch18
sentence ≥2 jumal rows), so a later regeneration cannot quietly flatten it
back to prose.

## An exact engine claims the ORDER; intent stays a shortlist

TaqdimEngine reads two frames the surface settles completely — a fronted
jarr/zarf before its indefinite marfūʿ noun is a khabar muqaddam (and WAJIB
when the mubtada is a nakira), and lā + a bare fatḥa-final noun directly
after is the genus-lā with its ism — but WHY the speaker fronted (qaṣr,
tanbīh, tafāʾul, tashwīq) is semantic, so the four wujuh ship as a DOC
shortlist, never a verdict. Same split as ShartEngine's nukta: the engine
encodes the rule and NAMES the licensed departures; it does not adjudicate
motive. And the frame pair teaches by CONTRAST: the same lā is voided in
لَا فِيهَا غَوْلٌ and working in لَا رَيْبَ فِيهِ, and the visible endings
(damma/fatḥ) are the receipts — gate both directions, never one.

## Jazm belongs to the muḍāriʿ — the ending alone cannot say so

IrabSign read سَعِدَتْ as «jazm by the sukun»: the final ـَتْ is the tāʾ
al-taʾnīth and the word is a mabni māḍī, but no rule that looks only at the
last letter can know that. The discriminator lives at the OTHER end — a
muḍāriʿ shows its person prefix ([يتنأ] + a sākin letter, the damma prefix
of the derived forms, the V/VI prefix pair) — so the bina branch fires only
where no prefix shape stands. This is the seam doctrine's sibling: when the
ending underdetermines, the evidence is elsewhere ON THE SAME WORD, and the
gate must pin both directions (سَعِدَتْ mabni AND يَكْتُبْ still majzum).

## The candidate's dress is part of the evidence — the override reads it now

The glossary override fired only on weak-letter roots, and وَجْهِكَ answered
ج ه ك — a sound-LOOKING root built on a waw-peeled candidate. The trigger now
includes provenance: a rules answer matched on a peeled candidate (c !==
cands[0]) or on one still wearing a peelable letter (/^[وفبلك]/) is hedged,
and the lexicon outranks it exactly where they disagree. Pair this with the
noun lexicon running its pronoun strip over EVERY try (clitic + plural +
pronoun stack on one word: لِكِبَارِهَا), and with the propn-first guard —
the lexicon is asked about proper names BEFORE the rules, because a rule
CANNOT refuse what it was never told is jamid (إِسْحَاقَ as «grinding»).
Agreement always keeps the rules answer whole, wazn included.

## The iyya family's case is its spelling — three engines had to be told

إِيَّا exists for one purpose: the detached NASB pronoun. Three consequences
landed in one chapter, each in a different engine: a clause opening إِيَّاكَ
is a VERBAL clause with its object fronted, so WawEngine's hal branch (which
had listed اياك among its nominal-clause openers since it was written) was
offering an impossible reading; TaqdimEngine reads the fronted object off
the spelling alone — no case sign needed, the word IS its case; and the
detection regex must admit the hamza SEAT (إياك, fifth occurrence of the
trap). When a closed-class word encodes its i'rab in its very letters,
every engine that reasons about order or case around it inherits a fact —
walk them all the day the word enters the corpus.

## A promoted rule needs its ANCHOR named, or a twin frame will steal it

MaEngine's list-frame (6f: wa+ma, noun before, seat concealed) fired on
مَا وَدَّعَكَ رَبُّكَ وَمَا قَلَى and sold mawsula where the aya is negation
joined on negation. Both frames share every surface test; they differ only
in what the waw HANGS ON — a noun list, or an earlier negation clause. The
fix names the anchor: an earlier bare مَا directly before its own verb hands
the wa+ma exactly the clause the list-frame's refutation says a negation
lacks, and where that anchor stands the negation wins. When two readings
share a trigger shape, the discriminator is the antecedent, not the shape —
and the control sentence (وَمَا نَابَ عَنْهَا, anchored on a noun) must be
gated through the same change.

## Demotion is not omission — and the difference is whether taqdir EXISTS

The mutaallaqat bab divides on one question: can the missing object be
named back? يَعْلَمُونَ (Zumar 9) predicates knowing AS SUCH — reconstruct
an object and the aya's point dies; لَهَدَاكُمْ names its dropped هِدَايَتَكُمْ
in its own jawab. The authoring rule that follows: a demoted verb's i'rab
must SAY no taqdir exists (لَا حَذْفَ وَلَا تَقْدِيرَ), an omitted object's
i'rab must NAME the taqdir — the two are different claims, and flattening
them into «object omitted» teaches the bab's own commonMistake.

## The illa pairs with the NEAREST negation — the bank drew the line in minutes

Rule 6h's first draft promoted the negation for ANY ما with an إِلَّا later
in the line, and four Manar definitional mawsulas broke on arrival: in
وَالْمُشْكِلُ مَا ازْدَادَ … لَا يُنَالُ إِلَّا بِالطَّلَبِ the إِلَّا answers the inner
لَا, not the mawsula four words back. The discriminator is the pairing rule
the grammar itself uses: an exception attaches to the nearest preceding
negation, so a second lā/mā between the ma and the illa hands the illa away
— and BOTH engines that read the frame (MaEngine 6h, QasrEngine) must carry
the same guard, or they will pair differently on one sentence. Same family
as «a promoted rule needs its anchor named»: when a frame rule reaches over
intervening words, name what may NOT intervene.

## One preference, one storage key — unify before you duplicate

The Aa sheet's four size steps were first built as a parallel scale
(state.arScale + body attribute + new CSS variable) — and the probe showed
the size not moving, because renderStory was already stamping an inline
--ar-size from a state.arSize the header's A−/A+ buttons had owned for a
hundred versions. The shipped fix drives the EXISTING state from the new
control (AR_SIZE_STEPS → setArSizeStep → the same qissa-arsize key), so two
controls move one preference and neither can drift. Before adding any
user-visible setting, grep for the state it would duplicate — the app is
old enough now that most preferences already exist somewhere.

## The reading surface is a preference, not a theme

The sepia/night tint scopes to the story COLUMN (body[data-rt] +
:not(:has(.lib-card)) + CSS variables redefined on the column), never to
the app chrome — the Kindle convention: a reader chooses a page color the
way they choose a type size, independently of the app's light/dark. The
mechanism is variables-only, so a tap repaints with no re-render; the
sepia palette deliberately commits to one look in both app themes, which
is what choosing sepia means. Everything that reads --ink/--line inside
the column inherits the tint for free.
