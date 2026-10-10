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

**The hosted copy is split; the repository reader is not.** From v194 the reader is 20 MB on disk
(Part Four alone adds 45 chapters), above the artifact host's 16 MB page limit. The published copy is therefore
produced by `pubsplit.py <reader> <outdir>` (kept with the release scripts): the `// __DATA_START__ … __DATA_END__`
block is moved into `data/d1.js` (`const STORIES = [...]`, the first packages), `data/d2.js` (`STORIES.push(...)`)
and `data/d3.js` (GRAMMAR, the models, REF_GROUPS), each under 15 MB, loaded by three `<script src>` tags in the
page's place; top-level `const` in classic scripts shares one global lexical scope, so the engines see the
same names. The page shrinks to 2.7 MB. Nothing else changes, and `prototype/reader.html` stays self-contained
for file://, the PWA and the review bundle. Check the split copy headlessly (`STORIES.length`, one analysis)
before publishing, and publish with `root=<outdir>` and the three files mapped.

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

## The sukun-إن wears a THIRD face — the illa is the observable

The sukūn-nūn split (إِنْ shartiyya vs إِنَّ nasiba) gained a third branch
in ch22: sukūn-إن with an إِلَّا later in the sentence and NO other
negation between them is إِنْ النَّافِيَة (equivalent to مَا) — the same
nearest-negation pairing that guards MaEngine 6h and the QasrEngine
decides this face too. The observable stays mechanical (scan forward,
break on لَا/مَا, match الا/إِلَّا), the ShartEngine stands down for it,
and the QasrEngine's negation opener accepts pk==="nafy" on إن so the
frame reads. When a closed-class word grows a new face, every engine that
keyed on the OLD faces must be re-checked — the control sentence
(إِنْ جِئْتَنِي أَكْرَمْتُكَ still opens a shart frame) is what keeps the
new branch from stealing the old ones.

## ألا before إنّ is one particle — a peel must not split what a table lists whole

The hamza-peel read أَلَا as interrogative-hamza + لَا and shipped a wrong
negation. أَلَا التَّنْبِيه (alerting "lo!") is a single particle the
classical tables list whole, and its one reliable observable is إِنَّ
directly after it. The branch fires BEFORE the hamza peel — the same
ordering doctrine as the inna-table: multi-letter closed-class entries
outrank the letter-by-letter decomposition that would consume them.

## The five-nouns table outranks the prefix guess under a pronoun

أَخُوكَ was read as verbish (its alif looked like a muḍāriʿ prefix) and
its kāf labelled a mafʿūl bihi. A five-nouns entry hosting an attached
pronoun is a muḍāf with its muḍāf ilayh — that is WHY it shows the wāw
(its case shows as a LETTER because it is annexed). The guard sits before
the verbish branch: membership in a closed lexical table is a stronger
signal than any affix-shape heuristic, which is the RootFinder doctrine
(the lexicon eats first) applied one row down.

## The borrowing leaves a receipt — read the nasb, not the heart

Chapter 23's doctrine and its engine are one lesson: لَوْ and لَعَلَّ
borrowed for the wish LOOK like the conditional and the hope, and the
discriminator is not the speaker's heart but a fatha — the fa-verb's naṣb
by a hidden أَنْ follows the six talab things and never a shart. The
InshaEngine claims exactly the frames that carry the receipt (reading the
host's last vowel at the seam, past the object pronoun) and leaves هَلْ's
wish a labelled shortlist, because there the converting despair really is
in the heart. When the books say a particle «acquires» another's meaning,
ask what the acquisition does to the GOVERNMENT downstream — that is
where the surface records it.

## A fa-initial verb gets its enclitic label before its class — rewrite on upgrade

The enclitic pass labels a pronoun by the host's kind, and a fa-initial
verb (فَأَزُورَكَ) fails the muḍāriʿ-prefix test — so the label was written
against a noun-guess and said «mudaf ilayh». The corpus dig upgrades the
class twenty lines later; it must also rewrite what the earlier pass said
under the old class. When a later stage OVERTURNS an earlier stage's
classification, grep for every note the earlier stage wrote off that
classification — the row carries its history, and a reader reads all of it.

## The tahdid family is one particle per row, four rows, one observable

هَلَّا، أَلَّا، لَوْلَا، لَوْمَا: Sakkaki derives them (hal/law + a
tamanni-laden zaida), the tables list them whole, and the tense after
them decides tandim (madi — reproach) against tahdid (mudari — urging).
لَوْلَا is the interesting row: it was already in PARTICLES as shart
(imtina'), and the verb face did not need a second key — the NEXT WORD'S
CLASS routes it (noun = imtina' frame, verb = tahdid frame), the same
next-word observable as إِذَا's two faces. A closed-class word's new face
does not always need a new table row; sometimes it needs a router.

## The question hamza rides an invented word until the lexicon splits them

أَزَيْدٌ read as an «indefinite noun أزيد» for two hundred versions: the
interrogative hamza was peeled only before closed-class remainders. The
open-class peel is lexicon-guarded BOTH WAYS — the remainder must answer
(corpus or glossary) and the whole word must not — and both lookups get
the VOWELLED word, because bare أزيد matched زَادَ's أَزِيدُ with nothing
to refuse on («a test can only refuse what it is shown», third payment).
Sentence-head only: that is where the question hamza stands, and the
narrow claim is what keeps أَكْرَمْتَ، أَحُجُّ، أَخُوكَ whole. When a peel's
guard is a lexicon question, ask it with every mark the page carries.

## The refusals are the frame — an engine may teach what a sentence may NOT do

The IstifhamEngine's هَلْ rows are mostly REFUSALS: the mumtani am-pairing,
the qabih fronted mansub, the futurity clash with a hal-clause — and the
mufassar rescue that lifts one of them on a single pronoun. A frame engine
over a bab whose doctrine is restrictions should render the restriction
WITH its reason and its minimal pair (ضَرَبْتَ / ضَرَبْتَهُ), because the
boundary is the teaching — the same doctrine as IdafaEngine's refusals,
lifted from government to word order.

## What follows the hamza is what is asked — adjacency as an exact claim

The istifham bab's core rule is pure word order, so the engine claims it
exactly: verb after the hamza = the deed asked, detached pronoun = the
doer, fronted mansub = the object, am-paired nouns = ta'yin of the two.
The hamza peel stamps row.istifham and the engine branches on the row's
OWN class — no semantics anywhere. When a balagha rule is secretly a
syntax rule, implement it as syntax and let the note carry the rhetoric.

## The engines now decide the i'rab — and are graded on it corpus-wide

The bank's worked sentences compare a SECOND field since v142: CaseEngine
claims each token's case (raf'/nasb/jarr/jazm, harf, mabni — and SILENCE
where taqdir or an un-narrowed shortlist leaves the surface undecided) and
humanCase reads the case the stored line names; only double-decided tokens
count. One definition, three readers — the tahqiq panel's i'rab column,
the Jumla lab's case chip, the bank — the posClass discipline again. Five
triage rounds took it 83.7 → 99.3 over 1,107 tokens, and every round's
lesson was one already in this file wearing a new mask: the claim must be
SHOWN the vowelled word; a fused token holding two i'rabs gets no single
claim; the human line's FIRST keyword may describe the clitic, so an
explicit case word outranks position. The 8 rows left are honest
boundaries, kept on the leaving-a-disagreement-in doctrine.

## An audit layer is an engine-bug detector for OTHER engines

The case audit's first run found five real defects in engines that had
passed every existing gate: IrabSign's seam peel ate the radical ha of
ال-definite words (لا يجتمع ال والإضافة had guarded the analyzer's peel
for a hundred versions and never IrabSign's); the dual letters-shape
claimed raf' on singulars ending ـَانِ; the five-verbs tail matched the
hollow تَكُونَ (LENGTH splits the plural from the singular); the
ات-plural's kasra is nasb and jarr both; the unmarked seam decides
nothing. A new comparison field is worth more than a new engine: it makes
every existing engine's silent errors countable. And the article test
inside it must read the BARE spelling — the article is never آ, and
folding seats turned آلِهَتَكُمْ into a false ال-word.

## مَنْ the ism must not wear the letter's key

The min/man vowel split flipped the KIND for two hundred versions while
the pk stayed «jarr» — and pk rides downstream (the ML pk- feature, the
case layer's mabni table, every consumer that branches on knowledge). When
a split decides a word is a DIFFERENT WORD, give it its own key, not just
its own kind: the fix is one ternary at the stamp, and the probe that
found it was reading the row's whole output, not the metric.

## Widen the audit's corpus and the bug list doubles

The case layer triaged to 99+ on the bank's analyse-subset — and the
smoke gate's ALL-stories sweep immediately fell to 96.6, because the
subset had never held أَهْلِ (peeling as أ + هَلْ since the hamza branch
was written), وَرَبُّ (read as رُبَّ — no vowel guard), دُونَ and
الْيَمَنِ (IrabSign's letters-shapes firing on short bares), or the verse
rows whose ALIGNMENT had silently drifted. A benchmark's blind spot is
its sampling before it is its metric: when an audit layer saturates,
widen its corpus before declaring the engines sound. And grade only
aligned pairs — a comparison across two different words measures the
tokenizer, not the engine.

## Bina hides under every case-shaped ending — the audit made the list

The genus-la's fatha, the munada's damma, the heavy nun's fatha, the
madi's ending, قَطُّ's damma: each wears a case's dress and is BINA. The
case layer now reads the OBSERVABLE beside the word (the لا before it,
the يا before it, the nun's shadda, the cell's tense, the mabni table) —
and where the observable is absent it claims the case, which is exactly
where the residual disagreements live. Bina-vs-i'rab is not a word list;
it is a list of CONTEXTS, and the audit is what forced them to be
enumerated.

## The frame router is one decision, written once — متى asks OR conditions

مَتَى أَيْنَ أَنَّى أَيّ are shart nouns AND interrogative nouns, and the
discriminator is arithmetic: a jazim binds TWO clauses, so fewer than two
verbs after the adat is a question. The router runs as a POST-pass over
the analyzer's rows (swap pk to istif-ism, swap the table note, withdraw
the dangling verb-expectation) — and because ShartEngine and CaseEngine
both branch on pk, ONE swap retargets every consumer. When a face-split
needs context the stamp-time walk hasn't seen yet, do it in a post-pass
on the row's pk rather than teaching each engine the frame test.

## The interrogatives are ASMA — and أَيّ alone declines

The conditional nouns sat in ISM_KINDS' blind spot as kind "particle"
for two hundred versions (the closed-class-table flattening, again), and
IrabSign listed أي among the mabni asma. Every book says the opposite on
both counts: they are nouns, and أَيّ is the ONE that declines — it never
leaves the idafa, so it never lost its ending. CaseEngine now reads
أَيّ's own written vowel and claims mabni for its sisters; the note, the
KIND_LBL and the case layer all state the exception with its reason.

## The light imperative is a receipt, and the receipt is lexical

سَلْ خُذْ كُلْ مُرْ are the received takhfif amrs — a CLOSED set the books
recite. The matching layer offers the regular spelling (سَلْ → اِسْأَلْ)
exactly as the madda unfolds: never stored, never displayed. And the
first attempt surfaced two deeper defects: (1) **an EXACT cell anywhere
in the corpus outranks a LOOSE hit anywhere else** — fromCorpus was
first-hit-wins over package order, so سَلْ bare-matched سَلِّ (salla's
amr, alphabetically earlier) while its own exact cell sat unasked; the
walk is two-pass now. (2) The mabni-ending guard's endVowel read only
the LAST character — a doubled ending (سَلِّ) shows its shadda last and
answered «no evidence», and an explicit sukun wasn't in the vowel class
at all. Both halves of the NFC-shadda trap, in one pair of words.

## A doubled walk needs a memo — measure the stall before shipping the pass

The exact-beats-loose second pass doubled fromCorpus, and the corpus-wide
case audit went from minutes to a timeout — because findFormInParadigm
rebuilds formCandidates once PER VERB for the same surface. The one-entry
memo (callers only read the array) restored the runtime. When a
correctness fix multiplies a walk, profile the walk's inner loop first:
the redundancy was always there, the fix just made it visible.

## The nida أَيْ and the interrogative أَيُّ split on the ya's vowel

The munada sweep read أَيُّ الْفَرِيقَيْنِ as a CALL: NidaEngine.flat folds
the marks away, and the calling particle أَيْ differs from the noun only
by its sukun. The sweep now requires the particle's dress — the fifth
member of the min/man family (one spelling, two words, one vowel), and
the second time a flat fold threw away the very evidence a closed-class
split needed.

## The question that already holds its answer — receipts before rhetoric

Chapter 27's bab is semantic (istibta', tahakkum, tahwil…), yet four of
its wujuh carry MECHANICAL receipts, and only those four became frames:
the hamza OVER a negation (أَلَيْسَ — nafy-of-nafy, claimed before the
class branches eat the verb-row), a FIRST-PERSON madi after كَمْ (a man
cannot ask the count of his own deed), the مَا لِـ frame (a bare
li-pronoun khabar gives the nafiya nothing to deny — structure, not
taste), and the fronted mudaf object (plain fatha, verb past the idafa
chain). The other six wujuh live in the note. The line to hold: a frame
engine claims what the SURFACE settles; rhetoric that needs the context's
knowledge ships as DOC and note, never as a verdict.

## A widened frame ships WITH its control — both directions, same check

hamzaMaful's first draft demanded a tanwin and verb-adjacency, and
أَغَيْرَ اللَّهِ تَدْعُونَ (plain fatha — the idafa took the tanwin; the
verb past the mudaf-ilayh) read as tasdiq. The widening accepts both
dresses and walks over intervening NOUNS only — and the gate pins the
control (أَزَيْدًا ضَرَبْتَ) in the same check that pins the new shape.
Same for kamIstibta: the third-person كَمْ آتَيْنَاهُمْ keeps kamAdad in
the same gate. A frame widened without its control pinned is a frame
about to steal its neighbour.

## لَيْسَ wears the shapes of three wrong readings

The jamid nasikh is a MAZI with no mudari — and every engine that reads
shapes found a wrong one on it: its opening hamza-dress (أَلَيْسَ) passes
the mudari-prefix test, so CaseEngine claimed nasb off its bina-fatha;
its khabar wears the ZAIDA BA (majrur in letter, mansub in place — word
the i'rab with the lafzi case first, and humanCase agrees with the
engine's honest jarr). A closed-class VERB needs its own guards exactly
as the closed-class nouns did — the bare-ليس test now sits in the case
engine's verb branch, before the prefix heuristic.

## The doer may already be in the cell — expectations must read the person

«First noun after the verb — likely the fa'il» was wrong after every أَرَى
and سَلْ in the corpus: a 1st/2nd-person cell (and every amr) carries its
doer as its own pronoun, so the following noun can only be the maf'ul.
The flag is computed at the END of the analyzer's iteration — the corpus
dig stamps the cell AFTER the expectation code runs, and reading row.cell
where it does not yet exist is the in-iteration ordering trap: set state
for the NEXT word where this word is finished.

## The stored majhul is a singular — its plural is rebuilt IN the cell loop

يُوصَفُونَ reached no cell twice over: the mithal's returned waw blocks
the vowel-rule derivation from يَصِفُونَ, and the package stores only
يُوصَفُ. The general fix (offer the singular as a candidate) was WRONG —
every active plural would resolve to its singular cell, person lost,
because the slots loop meets mudari[0] before mudari[2]. The safe home is
inside the majhulMudari branch itself: build stored-singular + ونَ and
test THAT, so the fallback exists only where no plural cell can. Where a
candidate could match many cells, put the derivation next to the one cell
it is FOR — not in the shared candidate list.

## The amr's wujuh are surface-settled — its frames carry exact receipts

Ch28's three amr frames each hold a mechanical qarina: amrDua fires on
the amr aimed at رَبِّ / رَبَّنَا / اللَّهُمَّ before it; amrTaswiya on
amr + أَوْ + a nafy + THE SAME ROOT again (do or don't — the same to me);
amrTahdid on amr + مَا شِئْتَ. The plain amr wears NO frame — the asl
needs no receipt, and the control that أَكْرِمْ عَمْرًا fires nothing is
pinned in the gate beside the frames it guards. Rank-dependent wujuh
(ibaha, ta'jiz, ihana, tamanni, iltimas) live in note 130, not in code:
receipts before rhetoric.

## The hamza seat is a standing tax — أَوْ bares to «أو», never «او»

Sixth payment. stripAr strips harakat but keeps the hamza SEAT, so every
bare() comparison against a hamza-opening particle must write the seat:
the amrTaswiya branch compared against plain-alif «او» and never fired
on its own type sentence. Grep for bare-string literals opening with alif
whenever a branch mysteriously stays silent.

## The ism al-fi'l is a closed-class NOUN with a verb's force

رُوَيْدَ enters PARTICLES with pk "ism-fil", joins ISM_KINDS and
CaseEngine.MABNI_PK: a mabni noun that governs a maf'ul (بَكْرًا in plain
nasb). The row must SAY what it is — the KIND_LBL entry names the class
and the note explains the paradox (a noun that commands), because the
learner's first question on رُوَيْدَ بَكْرًا is why a "noun" takes an
object.

## The open object seat is a definiteness route — MaEngine rule 6i

مَا between two verbs where the FIRST still owes its maf'ul (no object
enclitic on it) is the mawsula filling that seat: اِعْمَلُوا مَا شِئْتُمْ.
The seat itself supplies what the definitional frame usually demands —
a definite before ما — so the rule sits with the definiteness routes,
guarded by the jarr-fused control (مِمَّا with no aid keeps masdariyya).

## The trimmed vocative: silence beats a wrong claim

رَبِّ sentence-initial before a verb is يَا رَبِّي with the ya cut — its
kasra is the trace of the pronoun, not a jarr. CaseEngine returns null
there (bare رب, kasra-final, no tanwin, verb next): the NFC trap again —
the word ends kasra+shadda, so the test is /ِّ?$/, never /ِ$/.

## A resolved verb is never a jarr phrase — TaalluqEngine bails on cells

The fused-jarr heuristic (ل-initial, length > 3, lemma not ل-initial)
swallows لِيَحْضُرْ and walks a VERB toward an "omitted amil" — wrong
grammar published on the very sentence ch28 teaches. Any row that
resolved with a paradigm cell and kind verb exits of() before the
letter tests run: the lam it opens on belongs to the lam-amr pass.

## The estimator is replaceable — the harness is what made it safe to replace

v146 swapped naive Bayes for an AVERAGED PERCEPTRON inside IrabModel and
the whole app followed for free, because every consumer reads predict()'s
{r, p} contract and every grader now routes through the same three
methods: rows() materialises the labelled corpus once, fit() trains,
rank() scores — train(), predict(), accuracy(), crossVal(), cv_eval.js
and ablate_estimator.js all call THOSE. The old crossVal carried a
private naive-Bayes copy; one algorithm change away from grading a model
that no longer shipped. A validator that owns a twin of the estimator is
drift waiting to happen — give the estimator one home and make the
validator call it.

## The perceptron needs no damping apology — mistake-driven kills the double count

Naive Bayes multiplied correlated evidence («al», «sign-kasra»,
«by-haraka» move together) and needed the 1/k^ALPHA hack. The averaged
perceptron updates ONLY on mistakes: once one cue of a cluster carries
the decision, its twins stop accumulating weight — the correlation is
learned away, not damped away. Same features, same folds: 54.5/71.9 →
60.2/74.5 held-out, flat across epochs 5-20 and three seeds. A flat
sweep is what a real gain looks like; a spike on one setting is a
hyperparameter overfitted to its folds. Determinism matters for gates:
fixed LCG seed, fixed epochs, and the averaging is O(1) per touched
weight (back-rent accumulators), so 17-fold crossVal stays under 3s.

## The model is an OPPONENT the learner can beat — and its errors are the drill

gDuel pits the learner against IrabModel on the model's own training
labels: the hand analysis is the answer key, the model's ranked WRONG
readings are the distractors (the confusions a statistical reader
actually makes — near misses by construction), and the reveal shows the
model's pick, its percentage and the running tally. The shell grew ONE
hook for it (onAnswer, fired beside the Elo update, resume-safe) — a
game that needs shell changes is a shell feature and lands for all
sixteen at once. The model's guess wears 🤖 everywhere; the honest
framing (statistics, never i'rab) is in the game's own ask line.

## The Model lab shows the hand, not just the verdict

The atölye's نَمُوذَج tab renders, per open noun, the ranked roles as
bars AND the evidence — every fired feature named in plain language
(modelFeatLbl) — while verbs and closed-class words get a stand-down
line: the rules decide those, the model only votes where rules cannot.
Two disciplines: the lab computes prev/ctx EXACTLY as the analyzer's
predict site does (a lab showing a twin model is the crossVal bug at the
UI layer), and a runner-up below 3% belief draws no bar — a %0 bar is
furniture, not honesty. Design wave 7 (DESIGN.md §7): belief is a bar in
the role palette, evidence is a chip row, the statistical voice keeps
the lvl3 amber.

## Conjunctions are the perceptron's dividend — and each pair is doctrine

v147 shipped four feature conjunctions (ppk×sign, after-verb×sign,
al×irc, tanwin×after-verb): under naive Bayes a conjunction is maximally
correlated with both parents and the damping taxes it twice, so the
family was unaffordable; the mistake-driven perceptron learns exactly
the RESIDUAL the pair carries beyond its parents. Held-out 60.2/74.5 →
61.2/76.5 across three seeds. Each shipped pair states a rule the single
features blur — after إِنَّ the SIGN decides ism-vs-khabar, after a verb
it decides fa'il-vs-maf'ul: the İzhar doctrine needs both halves in one
feature. The fifth candidate (governor-key×position) was noise alone AND
in the ensemble — a conjunction inherits no right to ship from its
parents' pedigree. The Model lab labels a conjunction chip «parent ×
parent» via the labeller calling itself on the halves.

## The ablation harness became a UI — withholding evidence teaches government

The Model lab's chips are buttons: tap to drop that one feature from the
card's vector and re-rank with the SAME shipped weights — no retraining,
so the second tap restores byte-identically, and the gate asserts
exactly that roundtrip. This is ablate_features.js handed to the
learner, and the lesson it animates is the Awamil doctrine: withhold the
governor's key and watch the belief collapse. Per-card state lives in
MODEL_CARDS (rebuilt on input, toggles repaint one card's bars only);
bars and first paint share one modelBarsHtml so they can never disagree.

## A beatable round is a designed round — seat the model's failures

startDuel predicts over a 40-item draw and seats up to three model-WRONG
questions per round of eight. A round the model aces teaches only
respect; the fumbled questions are where the learner can win — and the
revealed misreading (ranked, with its percentage) is the most instructive
distractor the app owns. The seating is shuffle-blind after selection,
so the learner cannot tell which kind they are on until the reveal.

## An estimator change voids old feature verdicts — retry the rejected

The NB-era ablation table in this file rejected «preceded by a bare
noun» as noise and the idafa family as harmful. Under the perceptron the
first is worth +1.8 held-out alone and the second's next-al half is
additive — the old verdicts measured the ESTIMATOR's inability to carry
correlated context, not the features' worth. When the estimator changes,
the rejection table is unproven again: re-run it before trusting any
recorded «dropped as noise». (The reverse holds too — npk- was re-A/B'd
under the perceptron and is STILL noise; a retrial is a measurement, not
an amnesty.)

## Aim features with the confusion matrix, then ship the doctrine pair

v148's features came from reading the held-out confusion table, not from
brainstorming: jarr↔mudaf leads (both wear kasra — the discriminator is
the word BEFORE: a jarr letter vs a bare idafa head), the tabi classes
next (the tawabi' follow their head in i'rab — sign agreement IS the
classical signal). prev-bare, agree-sign, next-al: +2.0 top-1 together,
stable over three seeds. Ship the feature in the EXACT form the probe
measured — the shipped prev-bare guard reuses the probe's own
hamza-folded closed-class lookup, because a feature that drifts from its
measurement is an unmeasured feature.

## A frame quiz draws from analyzed corpus, and its supply must not charge for it

gWajh analyzes only sentences anchored to the wajh-bearing notes and
keeps sentences firing EXACTLY ONE insha/istifham frame — one
unambiguous answer; a sentence firing two would quiz a khilaf. The
sweep costs seconds, so GameFactory's supply() answers with the tagged
POOL count until the cache exists (a cheap honest upper bound — it
counts what the builder will analyze) and the exact count after; a
boot-idle setTimeout warms the library scope so the exact number is the
common case. Options and reveals quote InshaEngine.DOC/IstifhamEngine.DOC
verbatim; distractors are the same bab's other wujuh — what a madrasah
exam would offer.

## The chapter's doctrine became a post-pass — jawab al-talab is engine gold

Ch29's rule IS a detector: a jazm-shaped verb after a TALAB (an amr
cell, a nahy, a question row, a layta, an أَلَا offer) with no written
jazim anywhere before it is the JAWAB of an estimated shart, and the
post-pass names it with the taqdir. Three controls pin the boundary
(لَمْ real jazim, إِنْ real shart, a plain amr with a noun after). The
nahy's OWN verb is part of the talab, not the jawab — talab advances to
i+1 there. The jazm shape must read the SEAM too (أُكْرِمْكَ hides its
sukun before the object pronoun), and the pronoun letters carry marks —
the vowelled-هم trap, again.

## لَا النَّاهِيَة rides a flag, never a new pk

The prohibiting la is split from the negating la by the NEXT word's
dress (jazm shape) — the إِذَا method. But pk "nafy" feeds QasrEngine's
negation openers, MaEngine 6h's nearest-negation pairing and the ML
pk-feature: renaming it would re-key three engines for one note. The
nahy fact rides r.nahy, the note swaps in beside the generic one, and
every downstream consumer keeps reading the pk it always read.

## One engine's frame is another's stand-down — the receipt decides

أَلَا over a RAF' mudari with a bare majzum later is the ARD, and
InshaEngine claims it on the jawab receipt. IstifhamEngine's hamza
chain must stand down for that exact shape — the WHOLE chain (a single
suppressed branch let the row fall through to hamzaMaful within the
minute). أَلَيْسَ keeps hamzaNafy because its core is a nafy VERB, and
أَلَا with NO jawab keeps its question face: both readings are real, and
the receipt is what splits them. Also the SEVENTH hamza-seat payment:
bare(أَلَا) is «ألا».

## The hollow first person rebuilds INSIDE the majzum branch

أَزُرْكَ was unreachable twice over: the stored majzum cells are the
third and second persons (يَزُرْ، تَزُرْ) and the hollow's jazm changed
the letters, so أَزُورُ never bare-matches أَزُرْ. The rebuild swaps the
stored cell's person prefix (أ → person 12, نَ → 13) and lives inside
the majzum branch only — the stored-majhul-plural doctrine again: a
derivation sits next to the ONE cell it is for, never in the shared
candidate list.

## Rewrite-on-upgrade has a noun edition

The enclitic pass labels a clinging pronoun by the host's kind AT THAT
MOMENT; a host the arbiter later settles as a NOUN kept a verb-branch
«maf'ul bihi» on its ya (أَمْرِي). A noun's pronoun is annexed, never
acted on — the post-pass rewrites the label wherever kind ends up noun.
The fa-initial verb taught this rule for verbs (ch23); the nouns needed
their own edition.

## An inconclusive probe is recorded, not shipped

The mubtada↔khabar seam was probed with a definite-opener feature
(HURT, −0.5) and a definite-before/tanwin-here khabar frame (mixed:
+0.4 top1, −0.3 top2 across seeds). Neither shipped. A top1 gain that
pays with top2 across seeds is not a gain — the residual there is
genuine word-order ambiguity (both halves of a nominal sentence are
marfu'), and no surface feature reads intent. Recorded so the afternoon
is not respent.

## A boot warmup must drip, never sweep

The wajh pool's warmup first ran wajhItems() synchronously at boot+2.5s
— an 8-second main-thread freeze exactly when a user takes their first
taps, and a smoke check caught it as a lab that stopped answering. The
drip builds the same pool one sentence per 120ms timeout slice, checks
WAJH_CACHE before every step (a synchronous call that got there first
wins), and the item-builder is ONE named function (wajhItemOf) shared
by both paths — the fusedJarr rule at the scheduling layer: two builders
of one pool will disagree about an item the day one is edited.

## A rebuilt cell must carry its person THROUGH the label

formCellLabel hard-coded «he» for the governed cells — right for the
stored third-person cells, wrong the moment a rebuild carries person 12
(أَزُرْ، آخُذْ): the row's cell said «I» while the printed note said
«he», and the ch13 gate caught the split. The label now honours
cell.person wherever it exists — the derived-majhul rule extended to
every rebuild. When a matching-layer derivation adds a field, walk the
PRINTERS the same day: a field the label ignores is a fact the reader
never hears.

## A drip must also YIELD: stand down while a sheet is up

The drip fixed the sweep's freeze, but each slice still costs one full
analyze() — milliseconds locally, ~a second on a slow runner. CI caught
the residue: the jadhr lab's 140ms-debounced input was filled, the
check read the output 260ms later, and a drip slice sat on the main
thread inside that window — the output still showed the DEFAULT word's
root. The drip now polls without computing while sheet.classList holds
"show" (350ms re-check) and resumes on close. The general rule: a
background loop must yield to the FOREGROUND SURFACE it can starve,
and "open sheet" is that surface here — pacing alone only shrinks the
collision window, it never closes it.

## The frame's receipt is the peel, never the letter-tail

The khabarDua frame (mazi + speaker/addressee object + the jalala as
fa'il — وَفَّقَكَ اللهُ) first tested the word's ENDING for a pronoun
shape, and every mazi that merely ends in a kaf (تَرَكَ اللهُ) would
have prayed. The analyzer had already peeled the enclitic; the fix was
to stamp the peel on the row (row.enc) and read THAT — the closed-class
key lesson one field over. And the peel itself had a hole the chapter
exposed: رَزَقَنِيَ wears an iltiqa fatha ON the wiqaya-ya, and the
$-anchored نِي row never matched — the vowelled-pronoun trap, at the
enclitic table this time. A frame's receipt must be knowledge a pass
already established, and every enclitic row must be tried in the
dresses the orthography actually writes.

## One spelling, two cells — the label says both or it lies

تَأْتِي is «she» AND «you» in every mudari of the language; the
matching layer answered whichever index came first and printed it with
full confidence. findFormInParadigm now scans the tense array for
IDENTICAL twin forms and carries them on the cell (cell.also);
formCellLabel prints «she — or you». The honest-shortlist doctrine at
the cell-matching layer: where the paradigm itself cannot split two
readings, a first-hit answer is a guess dressed as knowledge.

## A dead guard is worse than no guard — it documents an intention nobody checks

IdafaEngine.chain's pronoun-closed test was `tail-regex && !isNoun(next)`
— unreachable, because the line above had already `continue`d on
!isNoun(next). It sat there looking like protection for two hundred
versions while وَفَّقَكَ اللهُ annexed the jalala over a visible damma.
The live rule reads row.enc (knowledge, not letter-tails — a radical
kaf in مَلِك would break real idafas), and the chain gained its sign
guard: it may not CLOSE on a word showing raf'. When a guard's
condition contains the negation of a condition already handled above
it, the guard is dead — read the control flow before trusting a test
that has never failed.

## The atf letters are a TABLE, so the frame engine claims them — the waw is the exception

WaslEngine (ch31) is the receipts-before-rhetoric split applied to the
fasl-wasl bab: fa = ta'qib and thumma = muhla are table facts and the
frames say so outright; the WAW is the one atf letter with no meaning
beyond joining, so its frame names the PRICE (the jihat jamia) rather
than a verdict on whether the price was paid — and whether joining
would have been BETTER (the dawa'i) is semantic and lives in the note.
The engine's stand-down list is longer than its claim list: any
shart/talab/amr/istifham context hands the letter to the bab that owns
it, because the same fa is the jawab's fa after a shart and the
hidden-an fa after a talab. One letter, four owners — the context
decides which engine may speak, and the controls pin each boundary.

## A pre-existing key collision is recorded, not inherited silently

The ch31 glossary needed بَعْض, and «bad» already means بَعْض in three
packages AND بَدْء in bad-al-amali — a standing violation of the
global-key rule that predates this chapter. The new entry copies the
majority reading (بَعْض, samti's entry verbatim), which adds no new
disagreement; the amali collision remains on the books and is noted
here so the eventual rename (amali's بَدْء wants its own key) is done
deliberately, with the stale-key pop the rename rule demands.

## The five-nouns table answered only half its own words

The enc-guarded branch (v-ch22) read أَخُوكَ and stood silent on أَبُو
حَفْصٍ — the five nouns annexed to a NOUN never carry an enclitic, so
the books' own atf-bayan verse shipped «noun or verb?». The table now
answers bare for the declined letter-forms (length ≥3 keeps the
two-letter heads out), and CaseEngine claims the case by the LETTER for
the waw and alif forms only — أَبِي is the jarr form AND «my father» in
any case, so the ya-forms stay silent. A closed lexical table must be
asked in EVERY dress its words wear (the refusal-list lesson, walked in
the claiming direction): keying the branch on one accident of the first
example (the pronoun) hid half the class for two hundred versions.

## The heavy nun hid its bina behind the NFC tail — and the root splits the twins

CaseEngine's heavy-nun branch normalized the shadda forward and then
demanded the word END on it — but NFC writes تُقِيمَنَّ as nun + fatha
+ shadda, and after the swap the string ends on the nun's own fatha:
the branch never fired and the bina shipped as nasb. The widened tail
(/ن[ً-ٰ]*ّ[ً-ٰ]*$/) then met the OTHER twin: a nun-final geminate wears
the same letters as its own ending (يَظُنُّ raf, لَنْ يَظُنَّ nasb), and
only the ROOT tells the tawkid nun from the lam — root known and not
nun-final claims bina; anything else falls through to the marks scan,
which reads the geminate honestly. The NFC-shadda trap's sixth payment,
and the escalation-order doctrine in one branch: surface first, then
knowledge, then the honest fallback.

## Sentence ids restart every chapter — a note-example key must carry the text

The ch33 script appended three witnesses to note 136 with a dedupe
keyed on (sourceStory, sentence) — and ch32's own s2/s6 examples
already held those ids, so two witnesses were silently dropped and the
gate counted 4 where 6 were intended. Sentence ids are PER-CHAPTER
(every chapter restarts s1…), so any cross-chapter registry that keys
on them alone collides; the fix keys on the AR text as well. The same
looseness lives in the example-jump itself (an anchor's sN resolves to
the first chapter that has one) — a standing schema property to keep
in mind, not a bug to fix by renaming three hundred sentence ids.

## The Murib composes; it never decides — and its probe audits the deciders

`class Murib` (after CaseEngine) writes the full classical i'rab line per
analyzer row — class+tasrif, bina/case+sign, office — assembled ENTIRELY
from verdicts other engines already made (formCellLabel, CaseEngine.claim,
IrabSign.realize, the analyzer's own notes read through an OFFICES regex
table). Three rules keep it honest: every clause has a provenance (a null
verdict composes the honest «undecided» clause, never silence dressed as
knowledge); the model's office NEVER enters the Arabic line (it rides after
the translation as the badged 🧠 chip); and a consistency veto drops an
office that contradicts the case claim (a «likely the fa'il» note on a row
CaseEngine reads as jarr is a wrong note, not a wrong composition). The
veto is a smoke detector, not a fix: each time it fires in a probe, chase
the note to its source — that is how three standing analyzer defects fell
in one wave (below).

## A composer's probe reads every field, and the sources get the fixes

The Murib probe re-read whole rows and caught what the POS/CASE metrics
never could: (1) the verbal expectation pass offered fa'il/maf'ul seats to
FUSED-JARR rows — the row is its own majrur; the peel now stamps
`row.fusedJarr` and the after-verb guess skips it (and `row.afterJarr`).
(2) IdafaEngine.chain annexed the jalala over its own na't (بِاللهِ
الْعَظِيمِ): the clitic hid the ال from hasAl — the documented trap, at a
third call site — and the jalala itself never annexes (it stands to be
annexed TO; عَبْدُ اللهِ is the control and is gated). (3) The noun
lexicon's pronoun strip had every attached pronoun EXCEPT the bare
speaker's ya — نَفْسِي answered ف س ي off the infi'al row. A noun takes
the possessive ya directly (the wiqaya nun is a verb's dress — note 103
read backwards, fourth use); the ≥3-letter guard keeps نبي، سعي، رأي
whole, and the ya-final control row is gated.

## The seat-memory feature is noise — the nasikh's expectation is already spent

Tried for v155 and rejected on measurement: remembering the nasikh's OPEN
seat across fulls (seat-inna1/2, seat-kana1/2 from the previous rows'
pk) fires on 230/4159 rows and scores +0.3/+0.4/−0.2 held-out across
three seeds — noise. The İzhar queue already hands the model that fact
where it matters (ppk-, the consumed-expectation notes); a second copy
arriving two words late carries no residual. Same verdict family as the
richer-prev states under naive Bayes — recorded so the afternoon is not
respent.

## The joining letter wears the joiner's fatha — at EVERY peel site

The أَفْعَمَ lesson (a compound peel must re-check the inner peel's
guards) had a sibling hiding in the BASE peel itself: the plain wa/fa
peel tested only the letters, so فُلَانٌ — whose fa carries a DAMMA —
peeled to ف + لان and matched the لِأَنَّ table row: an inna-sister
verdict on an ordinary noun, pushing a phantom ism-nasb expectation
onto the next word. The guard is one test on the VOWELLED word
(`!/^[وف][ًٌٍُِّْ]/`): a joining letter always wears the joiner's
fatha, and any other mark on it proves it radical. When a guard is
added to a derived rule, grep for the base rule it was derived FROM —
the base had the hole first, and for two hundred versions.

## A closed-class fusion has as many table rows as it has spellings

أَنَّنِي is إِنَّ's family wearing the wiqaya nun — and it reached no
branch at all, answering «noun, its ya a mudaf ilayh» (a HARF takes
the speaker's ya through the nun exactly as a verb does: note 103's
family, fourth appearance). The إِنَّا branch could not see it because
that branch keys on its own two spellings. All four nun-wiqaya
spellings (أنني إنني أننا إننا) now sit in PARTICLES and a refinement
branch reads the attached pronoun as the ISM with only the khabar
still owed. Same lesson as إيّاك's row: the table is looked up with
seats intact, so every spelling the orthography writes must be a key.

## The seam-idgham must ride EVERY cell list — the amr was the odd one out

sjMazi14, sjMudari14 and sjAmr all map sjIdgham — but the GEMINATE
branches build their amr lists inline, and those mapped only sjN. So the
engine contracted ظَنَنَّا (mazi seam) and يَظْنُنَّ (mudari seam) and
shipped اُظْنُنْنَ (amr seam) from the same rule system, and nothing
noticed until the corpus stored a nun-lam geminate and the paradigm
audit compared the two spellings. All seven inline amr lists now run the
seam-idgham; it is a no-op except on a sakin twin, which is exactly
where the contraction is mandatory (a vowelled first twin keeps its
fakk: أَمْدِدْنَ). The general form is the fusedJarr rule at the maker
layer: when a transformation is applied by mapping a shared helper,
every INLINE list that bypasses the helper silently opts out of every
rule the helper carries — build cell lists through one road, or audit
the roads against each other.

## A new paradigm is a new PREDATOR — sweep the corpus for its prey

Storing أَكَلَ gave the corpus a two-letter amr (كُلْ), and within one
bank run seven stored rows fell to it: every كُلُّ، كُلَّ، فَكُلُّ in
the library matched the new cell. The mabni-ending guard took three
refinements in one wave, each a doctrine already in this file wearing a
new mask: (1) see through a JOINING CLITIC on the written side
(وَابْنُهُ vs بَنَى's amr — the match was made on the peeled candidate);
(2) a sukun-built cell is refuted by any explicit vowel EXCEPT the
iltiqa kasra (خَادِعُهُمْ's seam damma, كُلُّ's damma — nothing ever
puts a damma on a sukun-mabni amr); (3) the enc-strip must leave a REAL
remainder on the cell side, or كُنْ strips to nothing and empty equals
empty (فَكُنْ went noun — missing evidence is not contrary evidence,
fourth payment). The meta-rule: when a short verb enters the lexicon,
run the bank BEFORE trusting the eye-probe — a two- or three-letter
cell shares its skeleton with half the closed classes, and only the
corpus-wide sweep sees the collisions.

## كم joined the min/man family — one spelling, two words, one vowel

The ب/ل proclitic peel refuses a PRONOUN remainder (the بِهِمْ rule) by
asking the closed-class table — and the table says كم is the
interrogative, so لَكُمْ peeled as the muzahlaqa lam over «how many»
and the fused-jarr path never saw it. The kaf's vowel decides: fatha is
كَمْ the interrogative, damma is كُمْ the plural pronoun — the same
one-observable split as مِنْ/مَنْ, إِنْ/إِنَّ, أَيْ/أَيُّ, now at the
peel guard. The general lesson doubles the closed-class-interface rule:
a table consulted as an ORACLE answers for the spelling, not the word,
and every guard that keys on table membership inherits the table's
homographs — walk the enclitic list against the particle list once and
every shared spelling needs its discriminating vowel written into the
guard (كن beside كُنَّ rode along).

## The restored nun and the seam the two classes share (ch39, v160)

A jazm or nasb drops the five-verbs nun; a clinging pronoun then takes
the alif's place — and the leftover stem (يُكَذِّبُو، تَعْرِفُو) is a
spelling NO cell stores, so the corpus went silent and the analyzer
read nouns. The candidate list now restores ونَ onto a damma'd bare
group-waw, exactly as it already restored the وا spelling — which nun
fell is IrabSign's news, not the paradigm's. But the FIVE NOUNS wear
the same seam from the other class: أَخُوكَ peels to أَخُو, and the
restored أَخُونَ walked straight into خَانَ's first person (three bank
regressions in one line of engine). Their waw-construct is a closed
set (أَبُو أَخُو حَمُو فُو ذُو) and the restore excludes it by name.
Corollary at the CASE layer: a damma'd bare waw at the seam is ALREADY
nasb-or-jazm — raf' would have kept its nun — so the marks scan must
not read the stem's own damma as an ending; a shart/jazim earlier in
the clause names jazm, and anything less is silence.

## The iltiqa kasra must be claimed EXACTLY or the guards eat it

مَتَى أَضَعِ الْعِمَامَةَ writes a kasra where the jussive cell holds a
sukun (iltiqa al-sakinayn). The loose pass matched the RAF' cell first
(أَضَعُ — last vowel may move), whereupon the jarr-sign guard read the
written kasra as a case and the verb became a noun; the majzum rebuild
that knew better sat later in the walk. The fix is ordering, not
tolerance: the majzum branch claims the iltiqa spelling as an EXACT
candidate (stored cells and the first-person rebuild both), so the
exact pass answers before the loose pass can hand the word to a guard
built for nouns. And the claim closes the loop at the case layer: a
kasra-final word whose matched cell is majzum is jazm, not silence —
the paradigm decided, the kasra only repairs the meeting of sakins.
Rider: the متى istifham-router counts FOLLOWING VERBS to pick the
shart face, so a verb the engine misreads as a noun flips متى to the
question face too — one wrong kind can cost the row before it.

## The geminate's twin cells and the governor that names them (ch40, v161)

A geminate writes its jussive as a FATHA (لَمْ يَشِبَّ، لَمْ يَظُنَّ),
so its stored mansub and majzum are one spelling — and the cell walk
answers «mansub» merely because that shelf stands first. No reading of
the word alone can split the twins; the GOVERNOR does: a jazim
immediately before renames the matched cell to majzum (doubled endings
only, so لَنْ يَشِبَّ keeps its true name), and the case layer then
reads the final fatha as jazm ONLY on a renamed cell. Same family as
the iltiqa-kasra rule one wave earlier: when orthography collapses two
cells into one spelling, the paradigm has already decided everything
except which twin — and which twin is the CONTEXT's to say, never the
marks scan's. The first cut trusted `tense === majzum` alone at the
case layer and the ch33 gate caught it within the hour: the
first-person REBUILD also stamps «majzum» (it derives from the
majzum2 shelf) while being twin-agnostic, so لَنْ أَدُلَّ — a true
nasb wearing the rebuilt cell — read as jazm. The rename now carries
an explicit `gov: "jazim"` stamp and the case layer trusts only the
stamp; the same rename applied over a rebuilt cell under لم turned
لَمْ أَدُلَّ from a silent nasb-guess into an honest jazm. Meta-rule:
a tense name on a cell is a SHELF label, not a verdict — two shelves
can hold one spelling, and only a stamp written at the moment context
decided is evidence downstream.

## كَلَّا joined the table — and brought its dual along

The rebuke harf had no entry, so the ب/ك/ل peel read كَلَّا as kaf +
لا and stamped a two-segment i'rab on a one-word harf. Adding the
entry inherits the homograph (the standing table doctrine): كِلَا
«both of» wears the same bare letters, so the KAF'S KASRA sends the
word down the open-class path whole, and an unvowelled كلا keeps the
table's rad' reading UNSURE (no harf claim) instead of walking into a
verb cell — the manOpen pattern, one particle over. Every new table
entry pays this toll: name the homograph, write its discriminating
vowel into the guard, and keep the unvowelled face honest.

## The munada reads its own ending — a flat rule was hiding a wrong one (ch41, v162)

«After يا: mabni» was one line and one lie: the bina-on-damm belongs
to the MUFRAD MA'RIFA alone; a mudaf munada is mu'rab and mansub
(يَا عَبْدَ اللهِ), and the flat rule was claiming bina against the
written fatha. The refined claim reads the munada's ending exactly as
NidaEngine's five kinds teach: damm → mabni, fatha (tanwin included)
→ nasb, bare kasra → the dropped speaker's-ya construct (يَا قَوْمِ،
يَا رَبِّ) whose nasb is estimated before an absent letter — silence,
not a guess; unmarked input keeps the old mabni default. The lesson
generalizes: a case rule keyed on a GOVERNOR ALONE (after يا, after
لا, after a jarr letter) is only as true as its least common
follower — enumerate the follower's own shapes before shipping the
rule, because the corpus will eventually put every shape after every
governor.

## Two gate catches in one wave: the builder that skipped idgham, the reader that refused a wajh

The v162 release run failed twice before green, both engine truths.
(1) sjGov — the one cell-builder among five that never ran sjIdgham —
regenerated اِتَّبَعَ's governed cells as يَتْتَبِعَ against the stored
يَتَّبِعَ; the tense builders had the contraction, the audit compared
all of them, and a ta-initial root under bab iftial was the first
corpus verb to expose the odd one out. When a rule (twin-seam idgham)
belongs to a CLASS of builders, grep every builder in the class the
day the rule lands — one omitted call site is invisible until a root
arrives whose letters need it. (2) NidaEngine.read had the speaker's
ya WITH its letter (يَا مُعَلِّمِي) but not the commoner trimmed wajh
(يَا قَوْمِ, bare kasra, no tanwin) — it answered «unvowelled», and
the corpus-agreement gate rightly called the refusal a failure: the
gate walks every munada the corpus parses, so shipping the chapter
that uses a wajh IS the test of the engine that reads it.

## The corpus index dedupes by LEX — a key name is a global claim (ch43, v164)

RootFinder.corpusIndex walks stories in order and keeps the FIRST
paradigm per lex key. Authoring talkhis's سَقَى («to water») under the
key 'saqa' silently lost it: manar already owns 'saqa' for سَاقَ («to
drive»), so the corpus-wide walk saw only the driver, and فَسَقَى
walked into the فِسْق noun. The in-app popup masks the collision —
per-story morph lookup is keyed locally, so the token LOOKED right —
but every corpus-wide engine (open-text analyze, the bank's engine
side, RootFinder) answered with the other story's verb. Rule: a lex
key is a GLOBAL name; before authoring one, grep every package's
glossary AND morphology for it (the ch39 key-check missed morphology),
and when the word differs, mint a suffixed key (malik-king,
saqa-water) — never share a spelling between two words. The eye-probe
caught it only because the probe reads the BUILT corpus, which is one
more reason the pre-authoring probe is mandatory.

## The key check must cover the package's OWN glossary too (ch44, v165)

The ch43 lesson said: grep every OTHER package before minting a lex
key. Ch44 showed the nearer trap — talkhis itself already owned 'daf'
(ضَعْف, from the fasl chapters) and 'ilm', and `GLOSS_ADD.update()`
overwrote both without a sound: the validator saw a valid entry either
way, and only a diff against HEAD would have shown ضَعْف turning into
دَفْع under every older token that pointed at it. Rule: the author
script's key list is checked against the CURRENT package's glossary
and morphology FIRST (a hit there is either «reuse the existing key»
or «mint a suffixed one», never «overwrite»), then against every other
package; and after the script runs, `git diff` the glossary and read
every CHANGED (not added) entry — an author script may only ADD.

## The seventh demotion guard reads the atf, not the word (ch44)

أَكْثَرَ is one spelling for the diptote tafdil and the Form IV mazi,
and no vowel splits them — the mabniMoved family is helpless. What
splits them is the ATF: بِجُمْلَةٍ أَوْ أَكْثَرَ joins the word onto a
majrur, and الْمَعْطُوفُ يَشْتَرِكُ مَعَ الْمَعْطُوفِ عَلَيْهِ فِي
الْعَامِلِ, so the jarr letter reaches it and «nothing a jarr letter
governs is a verb». The guard is narrow by design: previous row an
atf particle, the row before it a majrur noun, AND the lexicon owning
the noun lemma — because وَقَامَ after بِزَيْدٍ is a real verb (a
hal/isti'naf waw), and قام is nobody's noun. A context guard without
the lexicon test would have demoted every verb after a majrur's waw.

## A stored paradigm is a claim the regenerator will test (ch44, أَحْوَجَ)

Storing أَحْوَجَ يُحْوِجُ sound (the received form — 'Awf's bayt has
أَحْوَجَتْ) tripped the Sarf regeneration gate: the engine's Form IV
hollow branch melts every waw (أَحَاجَ), because no RULE says which
hollows refuse i'lal in a derived bab. The fix is the same shape as
the defects-and-colours class in Form I: a recited closed list
(SOUND_HOLLOW_IV = حوج, with اِسْتَحْوَذَ waiting for bab X) that makes
the i'lal rule stand down and conjugates the root sound. Two lessons:
every sama'i exception the corpus witnesses must be written into the
ENGINE, not only into the stored cells, or the audit will rightly call
the stored cells wrong; and the audit gate is exactly why paradigms may
be authored by hand at all — hand cells that the engine cannot rebuild
are either a bug in the engine or a bug in the hand, and the gate makes
you say which.

## Rules as a ledger; the corpus as the negative set (wave 12, v166)

Every engine decides; none of them had said WHICH RULE its decision
obeys. QawaidEngine names the nahw rules (what follows a jarr letter is
majrur, the ism of inna is mansub, a mudari after a jazim is majzum…),
reads the CaseEngine's claims against them, and writes a ledger. Two
disciplines make it honest. (1) A rule can only be broken by a case the
surface SETTLED — a silent claim is never a violation, because missing
evidence is not contrary evidence; and the analyzer's «likely the
fa'il» is a shortlist, so a lost seat is never a violation either, only
a kept one is written. (2) The corpus is the NEGATIVE test set: every
stored sentence is correct Arabic, so a ✗ on it is a false alarm — an
engine wrong somewhere, and the gate names where — while twelve seeded
errors are the positive set. The first sweep raised 147 alarms on 1,166
checks and every one was an engine truth, not a corpus error: the
fused-jarr flag only stamped on definite hosts; kana's ism may be
hidden (كَانَ مُتَرَدِّدًا is one nasb noun, the error is two); a jawab
may stay raf' after a MAZI shart; the idafa chain links by shape and
must not turn every link into a rule; لِمَا with a kasra is two words
and kept the jazim's key; the jalala under a fused lam read its own ha
as a pronoun; a sentence that OPENS on a joined majrur continues a list
the corpus cut. Meta-rule: a rule checker built on the engines' own
claims is the cheapest audit of those engines there is — run it on the
corpus before trusting any of them, and treat every alarm as a bug
report with the sentence attached.

The second sweep (46 → 0 across all seventeen stories, 2,287 checks) paid
in the same coin, and four of its lessons are general:
- **A bracketed lemma is a dead key.** «خَالٍ (الْخَالِي)» indexed WHOLE
  answered nobody, so the manqus fell to the rules' hollow guess. Index the
  head word — for NOUNS only: the closed classes carry bracketed lemmas too
  («مَا (الْمَوْصُولَة)», «أَلَا (التَّنْبِيه)»), and the first cut let every
  one of them into the noun index, where the lexicon-first paths read them
  as nouns (the bank caught أَلَا within the hour).
- **A ب/ك/ل strip may not land on a PARTICLE.** كُلُّهُمْ found لَهُمْ behind
  its kaf and wore a prep's lemma; no jarr letter enters on a harf, so the
  clitic-stripped tries refuse part/prep/conj hits.
- **The fused letter must wear the JARR vowel.** The lemma test alone read
  لَأَمَّارَةٌ (lam of ibtida', fatha) and بَصْرَةَ (radical ba, fatha) as
  jarr-fused; kasra on ب/ل and fatha on ك are the receipt.
- **حَتَّى before a mudari is the nasib, not the jarr letter.** Stamping
  «after a jarr letter» on تَمْتَحِنَهُ made the demotion guard turn a verb
  into a noun — the İzhar expectation must read the NEXT word's class
  before it is consumed, the إِذَا method one letter over.
And the rule that asks for a governor walks BACK: a na't, a badal or a
ma'tuf takes its governor from a head several words up (over a maqsur that
settles no case, over a hal, over a fused لَهُ), while a sentence that OPENS
on a majrur is governed from the line above and is never an error.

## The sarf ledger narrates; the sarf engine rebuilds; they must agree

SarfLedger takes a written verb — through the analyzer, so the
governor's rename (لَمْ يَشِبَّ) and the clitic peel come with it — and
narrates the root's class, the bab and wazn, the cell with the letters
that mark it, the phonology by class (idgham/fakk, qalb/naql/hadhf, the
mithal's waw, the ta of iftial), the augment of a derived bab, the
passive vowelling, the mood sign, the fallen five-verbs nun and the
riding clitic — in the books' own words, each step citing its note —
and LAST rebuilds the cell from the root with sarfDerive and says
whether the two agree. The narration is not a second engine: it is the
existing engines' facts in the Emsile lesson's order.

## Dabt is the test of nahw automation (wave 13, v167)

A rule engine that only JUDGES can hide behind the surface: it reads the
mark and says the mark is right. The DabtEngine cannot — it strips every
ending, decides each word's case from the governors alone (the verb and
its seats, the jarr letter, inna and kana, the idafa chain, the shart
frame, the tawabi'), and WRITES the ending through AlamaEngine; the stored
text is the answer key. Measured against the corpus in wave 13: drill
sentences 99.5%, the Talkhis 91.4%, al-Samti 93.9%, the Nasafi creed
86.5% of endings rebuilt exactly (coverage 92-99%; the creed's long
definitional chains are the hard case), and 97.7% of the drill sentences
rebuilt from BARE letters — every internal mark too — from the paradigm
cells and the lexicon. Lessons the sweeps forced, each a rule now:

- **Closed classes keep their marks.** إِنَّ / إِنْ / أَنْ share letters,
  and stripping their endings destroyed the analyzer's only evidence; a
  closed-class word is never stripped in endings mode, and in full mode
  its vowels are DECIDED first (a verb after it → إِنْ or أَنْ; a noun →
  إِنَّ; after a verb other than قَالَ → أَنَّ) and handed to the analyzer
  as marks, never spelled afterwards from a lexicon that would pick the
  first lemma.
- **A pronoun tail belongs to the word that owns its host.** Splitting
  هُ/كُمْ off every word ate اللَّهُ and الْفُلْكِ; the split happens only
  when the lexicon or a paradigm owns the host, and a two-letter host
  (رَبّ) needs the lexicon to vouch for it.
- **Ambiguity is resolved by adjacency, not by state.** A subject known
  three words back is not the doer of this verb; the «doer stands right
  before the verb» rule fires only at i-1, and the twin persons of a bare
  mazi (عَلِمَتْ / عَلِمْتَ / عَلِمْتُ) are picked by the noun beside it, the
  addressee in the line, or the speaker — and only when the twin shares
  the LETTERS (قَالَتْ is never قُلْتُ).
- **A shape guess loses to a lemma's own marks.** أَمَركُم read as أَمْر +
  كم by bare letters; the marks on the host contradict that lemma and
  agree with the stored أَمَرَ, so the paradigm wins. The same rescue makes
  شَيَّعُونِي a verb after حَتَّى, where the analyzer's «majrur expected»
  had bent it into a noun.
- **A cut in the chain must be earned twice.** The wave-12 cut «a
  definite member after a khabar head is not annexed» lost five chains
  (مُحَمَّدٌ رَسُولُ اللهِ) for every one it saved; removing it raised every
  story. The cut that stayed is narrower: an INDEFINITE head right after
  a TRANSITIVE verb, before a definite word, is the fa'il (جَوَّزَ قَوْمٌ
  الِاعْتِرَاضَ) — and a head that starts with a peeled jarr letter is
  never that fa'il.
- **The five verbs' jazm is a deletion, not a mark.** The ledger's
  correction for لَمْ يَكْتُبُونَ was writing يَكْتُبُون with nothing on
  the nun; the nun goes.

Meta-rule: measure ḍabṭ per story and per rule before and after every
engine change, and refuse any change that lowers a story it was not
aimed at. The gate holds floors under the measured numbers, never the
numbers themselves.

## The sarf corrector matches on the ASL, not the surface (wave 13)

A learner who writes يَقْوُلُ has not misspelled يَقُولُ by one letter;
they have written the cell on the scale ف ع ل with the root's letters
stood into it and NO i'lal run. Distance from the surface put يَقْوُلُ
nearer to يَقُلْ than to its own cell. The corrector therefore builds,
for every candidate cell, the same cell on the template root and
substitutes the letters — the asl — and a match on the asl is exact
evidence of which cell was meant; the correction is the real cell and the
i'lal chain of THAT tense is its reason. Ten seeded errors (hollow, naqis,
geminate, mithal) are corrected 10/10; the 11,451 stored cells of the
corpus are the negative set and none is «corrected». Two truths the
build forced: sarfDerive counts its babs (1-6), and passing bab NAMES
silently produced ok:false for every geminate and mithal root — the
seeds were 6/10 until the number was passed; and a corrector must narrate
only the corrected cell's own i'lal, not both tenses' (يَقُولُ's card
carries the naql step, not the mazi's qalb).

## A tagged token is a claim the engines will test (ch45, v165→v167)

Chapter 45's first engine run showed seven «noun/part» disagreements —
all mine: I had tagged the fused بِ-words (بِغَيْرِ، بِحَمْدِ، بِاعْتِبَارِ…)
with the particle's lex and pos, against the package's own precedent
(لِلّٰهِ carries the noun's lex with segments). The tahqiq panel is the
authoring gate as much as the reader's: run every new chapter through
engineCheck before committing, and read a disagreement as a question to
the author first. The same run caught real engine gaps — حَيْثُ losing its
bina after مِنْ, عَنَّ read as the jarr letter, the hamzated amr behind a
fa (فَأْتُوهُنَّ) reaching no cell, the sifa after «X بن Y» agreeing with
Y — and each became a rule with a gate.

## A bayan rukn is a nahw seat wearing a new name (wave 14, v168)

The first bayan engine was built in an afternoon because it never
analyses: TashbihEngine reads DabtEngine's own decisions — the fused kaf
(a majrur), كَأَنَّ's ism and khabar, مِثْل and its mudaf ilayh, a verb's
fa'il and maf'ul — and only NAMES them mushabbah, mushabbah bihi, adat,
wajh. The wajh is a tamyiz or a فِي-phrase after the bihi; the kind
(mursal/mu'akkad, mufassal/mujmal, baligh) is what is spoken and what is
not. Three disciplines: (1) a rukn is a cluster, never a word — the na't
and the mudaf ilayh ride with their head (صَوْتُهُ الضَّعِيفُ، كَخُلُقٍ كَرِيمٍ),
so every chain fix in nahw is a tashbih fix for free; (2) a likeness
without an adat is asserted only where the lexicon vouches for the khabar
as a stock likeness — a metaphor the lexicon cannot ground is not the
engine's to claim; (3) the AUTHORED frame is the negative-and-positive set
in one: chapter 46 stores each likening's arkan by token index, the sheet
shows agreement, the gate refuses disagreement. Eleven of eleven agree —
and every one of the disagreements on the way was a NAHW defect the
chapter surfaced: the na't after a pronoun-bearing head (الضَّعِيف's
shadda hid its فَعِيل), the Form III masdar read as a participle by its
mim (مُشَارَكَة), joined() refusing lemmas that begin with waw (وَجْه), an
ال-head annexing, the two-object passive's second object (تُسَمَّى الْأُولَى
مُطَابَقَةً), the women's-nun passive (نُشِرْنَ), the naqis passive behind
a shadda (تُسَمَّى), the radical alif-lam (الْتِزَام is no article: the
article before a sun letter always doubles it), a tanwin word read as
بِكُمْ (بُكْمٌ). Meta-rule: build a balagha engine as a reader of the nahw
engines' verdicts, and use its authored frames to audit the nahw — the
chapter that teaches a figure is the sharpest test of the grammar
underneath it.

## One word, two offices — the annexed letter-nouns (wave 15, v169)

USER RULE (2026-09-04): «سَلْ بَنِي — بَنِي is a mudaf AND a maf'ul; the
engines must understand that kind of detail.» The word carries its CASE
from the verb (nasb) and shows it by a LETTER (the ya, because بَنُونَ is
attached to the sound plural), has DROPPED its nun for the idafa, and is
the mudaf of إِسْرَائِيلَ — three facts on one word, and the app was reading
the ya as the speaker's pronoun («my son»). Nothing on the word decides
it: بَنِي and كِتَابِي («my book») are spelled alike. The discriminator is
the NEXT word — a possessive ya CLOSES its host, so a noun that can only
be a mudaf ilayh standing right after (jarr written on it, a name, an
ال-word not showing raf'/nasb) proves the ya is the plural's letter. The
rule now rides every layer: the analyzer stamps `row.construct` and
refuses the enclitic peel; `CaseEngine` reads the letter and lets the
GOVERNOR split the ya's nasb from its jarr; the Murib line writes both
offices (وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ،
وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالظَّاهِرُ أَنَّهُ مَفْعُولٌ بِهِ، وَهُوَ مُضَافٌ);
DabtEngine WRITES the letter (بَنُو / بَنِي, كِتَابَا / كِتَابَيْ), never a
vowel; the Qawaid ledger names the rule kept. The mulhaqat (بَنُونَ، أُولُو،
ذَوُو، عَالَمُونَ، أَهْلُونَ، سِنُونَ) answer from a table, because their
singular is not the word with the letter taken off. Three traps paid on
the way: a MANQUS the lexicon owns whole (خَالِي الذِّهْنِ) keeps its ya
and must be refused first; a diptote NAME in the mudaf-ilayh seat wears
a FATHA for its jarr (إِسْرَائِيلَ) and that is now a claim, not silence;
and a name closes the chain it is annexed TO (كَمْ was being annexed to
إِسْرَائِيلَ) — but a name may still HEAD one: the first cut refused every
name the head seat and the kunya أَبُو حَفْصٍ lost its idafa (the Murib gate
caught it), so the refusal is lifted for a five-noun letter-form and for a
construct row. Likewise the interrogative nouns are refused the ANNEXED seat
(كَمْ, مَنْ) but أَيّ — the one that declines because it never leaves the
idafa — must keep the HEAD seat, or أَيُّ الْفَرِيقَيْنِ raises a jarr-with-
no-governor alarm in the Qawaid ledger. And a whole word the corpus stores
as a verb cell with agreeing marks is that verb (قَالَا «they two said»),
never a dual construct of the manqus قَالٍ — a manqus singular spells its
bare form without the ya, so its bare letters equal a stem by accident;
its dual takes the ya back (قَالِيَانِ). Also: the Murib used to print ONE
office per word; a word with two (maf'ul + mudaf) now gets both, in that
order.

## A plural key is a WEAK key in the noun index

أُسُود (lions) and أَسْوَد (black) bare to the same letters, and the noun
index — which files every entry under its lemma AND its plural — was
answering «lion» for the colour because the plural walked first. A lemma
anywhere in the corpus now wins the key over any entry's plural. When two
different words share a bare spelling, the one that IS that word (its
lemma) outranks the one that merely inflects to it.

## The bayan's second door: the wajh has a SHAPE the syntax settles

TashbihEngine now claims what the sentence itself decides about the
wajh and the two ends — and offers the rest as a shortlist. CLAIMED: each
end is mufrad (a bare noun cluster), muqayyad (the cluster with a
jarr-phrase or zarf hanging on it: النَّحْوُ فِي الْكَلَامِ), or murakkab
(the noun with the clause that describes it: سُنَنٌ لَاحَ بَيْنَهُنَّ
ابْتِدَاعٌ — the indefinite khabar + a verb clause with a returning
pronoun); a spoken wajh is one meaning or a hay'a (an idafa chain, an
AND-joined list — أَوْ-alternatives stay one). NOT claimed: tahqiqi vs
takhyili, and whether the shared quality is inside the essences, sensed,
of the mind, or relational — those are knowledge of the two THINGS, so
`WAJH_DOC` prints them as a shortlist with the note. Two more adats
entered: the masdar تَشْبِيه itself (تَشْبِيهُ الْحُجَّةِ بِالشَّمْسِ — its mudaf
ilayh the mushabbah, its بِ-phrase the bihi, a فِي-phrase after it the
wajh) and the verb شَبَّهَ active or passive (شُبِّهَتِ السُّنَّةُ بِالنُّورِ). And
the kaf has a face that is NOT a likening: كَافُ التَّمْثِيلِ («for
instance») — كَقَوْلِهِ، كَمَا، and a kaf after a nisba-with-tanwin in an
أَوْ/إِمَّا list (أَوْ إِضَافِيَّةٌ كَإِزَالَةِ الْحِجَابِ) — which the engine
refuses, so the masdar frame beside it can be read. `agree()` compares
the authored frame with the engine frame that shares its adat, so a
sentence holding two likenings is graded on the one the author meant.

## Ch47's disagreements were nine nahw truths, and the chapter paid for all of them

The wajh chapter arrived at 82% ḍabṭ and left at 96.7%, and every point
was a rule: (1) a derived PASSIVE mudari under a governor (أَنْ تُشَبَّهَ)
reaches its cell with the governor's vowel, and with NO final vowel at
all (the endings strip); (2) inna's family with ANY attached pronoun
(فَإِنَّهُ، أَنَّهَا، لَكِنَّهُمْ، كَأَنَّهُ) is one table row, and the wa/fa peel
must see through it and through a jarr clitic on a particle (وَلِهٰذَا);
(3) بَلْ is a particle; (4) the ATF joins by SHAPE PARITY — a mudaf
parallels a mudaf (عَيْشَ السُّعَدَاءِ وَمَوْتَ الشُّهَدَاءِ), a bare indefinite a
bare indefinite (وَاحِدٌ أَوْ بِمَنْزِلَتِهِ أَوْ مُتَعَدِّدٌ), a pronoun-bearing
word a pronoun-bearing word (وُجُودَهُ … وَعَدَمَهُ) — and only where no shape
agrees does the nearest noun win; (5) kana's khabar never rides a waw: a
joined noun after kana's ism is a second ISM; (6) a bare noun right after
a detached pronoun is that pronoun's khabar (مَا هُوَ جَهْلٌ); (7) a subject
named earlier in the clause (kana's ism, inna's ism, a mubtada) owns the
verb after it — the fa'il is the returning pronoun and the next noun is
the OBJECT (يَجْعَلُ صَاحِبَهُ، لَا يَحْتَمِلُ الْقِلَّةَ) — unless a pronoun-
bearing zarf stands right after the verb, for then the pronoun is there
and the seat is open (لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ); (8) a na't reaches over a
shibh jumla only from an INDEFINITE head (مُلَابَسٍ لَهُ غَيْرِ) — a definite
head + jarr phrase + ال-noun is mubtada and khabar (وَجْهُ الشَّبَهِ فِيهِ
الْهَيْئَةُ); (9) a cell reached only by PEELING a joining wa/fa (فَسَادُ ~
فَ + سَادَ) loses to a noun the lexicon owns WHOLE. Rider: the five
verbs' DUAL ends in a kasra of its own (يَشْتَرِكَانِ) — the jarr-sign
guard must exempt a cell written ـانِ, and the ḍabṭ writes the dual's
nun with a kasra, the plural's with a fatha.

## The nisba's doubled ya is written vowel-then-shadda — third payment

sifaShape tested `ِيّ` and the exemplifying-kaf test copied it: in NFC the
nisba ya carries its vowel BEFORE the shadda (حَقِيقِيَّةٌ = ي + fatha +
shadda + ة), so neither ever matched, صِفَةٌ حَقِيقِيَّةٌ was read as an
idafa and a category list as a likening. Any regex that reads a shadda
next to a letter must allow marks between them — this file has said so
twice; the nisba is the third place it cost real rows.

## The Atlas shows the boundary of the automatable — and that is its point

`QawaidAtlas.ENGINE_OF` maps every note-id family to the lab whose exact
engine computes its rule; a ringed star is a note the app COMPUTES, a
plain star one it still only teaches, and the coverage line prints the
count (88 of 154 at v169). The map is honest by construction: badi' has
no engine and wears no ring, and the gate asserts it. A note sheet on a
ringed note grows «open in the lab», hovering a star lights its links
and neighbours while the rest recedes, and a star anchored in a sentence
the reader has actually read glows. The design rule: the sky is a
progress map twice over — the app's (what is automated) and the
reader's (what was read) — and both must be computed from data at
render, never stored.

## The dual and the sound plurals are the qiyasi half of the plural chapter

`IsmEngine.dual` and `jamSalim` build them by rule: the singular stays
whole and only the last letter's fate needs a rule — the ta returns as a
ta (مَدْرَسَتَانِ) and drops before ات; a three-letter maqsur's alif
returns to its origin (عَصَوَانِ، فَتَيَانِ) and a longer one turns ya
(مُصْطَفَيَانِ) or, in the masculine plural, falls with its fatha left as
the receipt (مُصْطَفَوْنَ / مُصْطَفَيْنَ); the manqus keeps its ya in the dual
(قَاضِيَانِ) and loses it in the plural (قَاضُونَ / قَاضِينَ); the alif of
femininity's hamza turns waw (صَحْرَاوَانِ) and a radical hamza stays
(قُرَّاءَانِ); فَعْلَة of a NOUN opens its ayn in the feminine plural
(تَمَرَات) and a sifa does not (ضَخْمَات). The masculine sound plural is
REFUSED where the shape cannot vouch for a rational male, because the
alternative — a broken plural — is heard, not derived (note 153
`jam-taksir` says so). Two traps: the tanwin of a maqsur sits BEFORE its
alif (عَصًا), so «strip the final tanwin» must look one letter in; and the
ending-strip must never eat a SHADDA (عَرَبِيّ → عَرَبِيُّونَ), or the nisba
loses its doubled ya.

## The tashbih's kinds and the majaz — the engines graded on four chapters (wave 16, v170)

Chapters 48–51 of the Talkhīṣ carry 91 sentences, 49 authored **tashbih
frames** (now with `taaddud` and `rank`) and 13 authored **majaz frames**
(`{word, kind, alaqa, haqiqa, murad}`), and the engines are graded on all
of them: every frame read back, no frame where none was authored, ḍabṭ
floors per chapter (endings-mode ḍabṭ at v170: ch48 94.4, ch49 91.9, ch50 97.2, ch51 95.4 — floors 92/88/94/91). The wave's rule, in one line: **the
authored frame is an assertion, and every layer that reads it must be
able to refuse it.** The validator now range-checks every frame index
against the sentence's own token count — ch51 shipped EIGHT majaz frames
pointing one token off (a `word` past the end, or at the فِي before the
word) and nothing complained until the engine was graded against them.
An index the reader cannot resolve is silent on the page and wrong in the
audit; both are worse than an error.

**The pronoun's own vowel is not the host's — the chain's closing test read
the strip's هُ.** In endings mode the ending-strip normalises a clinging
pronoun to هُ, and `IdafaEngine.chain`'s guard «the chain may not close on
a word showing raf'» read that damma as the HOST's — so every «bare noun +
pronoun-bearing member» idafa (بَيَانُ إِمْكَانِهِ، بِاسْمِ سَبَبِهِ، seven of them in
ch51 alone) fell apart in endings mode while holding in full mode. The
test now strips the enclitic first and reads the seam. The seam doctrine
(ch10, ch11) had been paid at the analyzer and at IrabSign; the chain was
its third payment.

**The lam of command is SAKIN after فَ/وَ, and a lam of purpose never is.**
فَلْيَدْعُ read as a nasb-lam (فَلِيَدْعُ) because the lam-amr test only fired at a
clause head. The sukun on the lam is an internal mark — it survives the
endings strip — and it is the receipt: the writer keeps it, the mood is
jazm. And the word after it, نَادِيَهُ, was «the 2fs amr نَادِي with an object»:
a cell that ENDS in a madd letter (ِي، ُو، َا) cannot carry a haraka on that
letter, so a fatha on the ya refutes the cell — the manqūs noun in nasb
with its pronoun. Eighth guard on the corpus-cell match, and the first
that reads the cell's own last LETTER rather than its last vowel.

**The seat-alif of the tanwīn survives an endings strip.** رَطْبًا → رَطْبا:
the fathatan goes, the alif stays, and an indefinite noun whose lemma does
not end in an alif but whose written form does is wearing the tanwīn's
SEAT — nasb, decided by the letter the strip cannot take
(`DabtEngine.alifSeat`). It rides the hal-on-inna's-ism rule, so
كَأَنَّ قُلُوبَ الطَّيْرِ رَطْبًا وَيَابِسًا reads its two hals in both modes, and
the owed khabar then refuses the na't reading: **an ال-noun after a zarf's
mudaf ilayh while inna's khabar is still owed IS the khabar** (لَدَى وَكْرِهَا
الْعُنَّابُ), and inna's family with an attached pronoun (كَأَنَّهَا) opens with
its ism already given — the intransitive-verb guard that names the next
noun innaKhabar now sets the rule itself instead of re-opening the state
for a later branch that never came.

**The jawāb of a shart may open on a NOUN.** إِنْ كَانَتِ الْعَلَاقَةُ غَيْرَ
الْمُشَابَهَةِ فَمُرْسَلٌ — the fa is the jawāb's fa and the noun after it is
marfūʿ: a mubtada when definite (فَالْأَحْسَنُ تَرْكُ التَّشْبِيهِ), the khabar of
an omitted هُوَ when not. The state is two fields (`st.shartAt`,
`st.jawabDone`), armed by the shart particles including the sukūn-إن and
وَإِلَّا (= وَإِنْ لَا, whose jawāb stands right beside it), disarmed by a
fa-verb. Before this every such noun was joined onto the nearest majrūr.

**A joined noun followed by its OWN verb joins the earlier SUBJECT** —
فَالْعَلَاقَةُ تُخْرِجُ الْغَلَطَ وَالْقَرِينَةُ تُخْرِجُ الْكِنَايَةَ is a sentence joined to a
sentence, and the parity walk (which stops at a verb) could only reach
الْغَلَطَ. When the next row is a verb, the walk crosses the earlier verb to
the earlier mubtada/fāʿil of the same shape, and the joined noun becomes the
new subject so its verb's next noun is the OBJECT. Two more parity facts
from the same bayt of ch50: **a pronoun-bearing word and a noun-annexed
head are one shape — both are mudafs** (صُدْغُ الْحَبِيبِ وَحَالِي), and
**كِلَاهُمَا after the pair it follows is the TAWKĪD**, never a khabar — its
`k` is «keep» (it declines by its own letter) and the TashbihEngine's
shape rule already excluded tawkīd from the nominal-clause test, which is
how the bayt's shape came back mufrad and its taʿaddud taswiya.

**Two more nahw rules the chapters paid for:** a na't across a na't's own
mudaf ilayh — لَدَى أَسَدٍ شَاكِي السِّلَاحِ مُقَذَّفٍ qualifies أَسَدٍ, not السِّلَاحِ
(agreement then holds: indefinite with indefinite); and a sifa-SHAPED head
the lexicon owns as a plain noun keeps its chain — قَرِينَةُ عَدَمِ إِرَادَتِهِ was
cut by the «sifa before a bare noun» rule because قَرِينَة wears فَعِيلَة, and
the lexicon (pos noun, gloss «clue») outranks the shape.

**MajazEngine reads receipts and stores the rest.** The received pairs are a
TABLE (رَعَى الْغَيْثَ، أَمْطَرَتِ السَّمَاءُ نَبَاتًا، آتُوا الْيَتَامَى، عَصَرَ خَمْرًا،
فَلْيَدْعُ نَادِيَهُ، لِسَانَ صِدْقٍ، فِي رَحْمَةِ اللهِ) and the istiʿāras the books
recite joined it (اهْدِنَا الصِّرَاطَ، فِي أَيْمَانِنَا نِيرَانَا — keyed on a
NEIGHBOUR, not a verb) — stored, never derived, because the likeness is
knowledge of the two things. Three things the chapter taught: the object
test must read the lemma OR the surface, because the lexicon's lemma is
the SINGULAR (يَتِيم) and the pair names the plural (يَتَامَى); the prev-word
test must peel the joining fa (فَفِي رَحْمَةِ); and the books' own CITATION
frame — «كَالْيَدِ فِي النِّعْمَةِ», a word under the kaf of «for instance», then
فِي and the meaning it is used for — is read as a mursal whose ʿalaqa is the
one the sentence itself just NAMED (بِاسْمِ جُزْئِهِ كَالْعَيْنِ → juzʾiyya,
بِاسْمِ كُلِّهِ كَالْأَصَابِعِ → kulliyya) or, failing that, the received table
(يد/نعمة → sababiyya; راوية/مزادة → mujāwara); with neither it stays a
candidate. The frame is refused wherever the TashbihEngine already read the
kaf as a likening (زَيْدٌ كَالْأَسَدِ فِي الشَّجَاعَةِ is a tashbih with its wajh).

**TashbihEngine, four more shapes:** the masdar with RELATIVE ends
(تَشْبِيهِ مَنْ لَا يَحْصُلُ … بِمَنْ يَرْقُمُ — مَنْ joins the relative set and
بِمَنْ/بِمَا is a بِ-group), a fused particle-with-pronoun inside a nominal
clause (فَحْمٍ فِيهِ جَمْرٌ مُوقَدٌ — فِيهِ is not a wall), the majrūr of a SKIPPED
governing letter is the end itself (كَأَنَّمَا يَبْسِمُ عَنْ لُؤْلُؤٍ: mufrad, not
muqayyad), and **a mushabbah never reaches past its own adat** — the atf
head's cluster is filtered to indices before the kaf, or the second
likening of a bayt swallows the first (كِلَاهُمَا كَاللَّيَالِي وَثَغْرُهُ …).

**The plural in the glossary must be the plural the corpus witnesses.**
وَأَدْمُعِي was read as a NA'T of صَفَاءٍ: `joined()` asks the lexicon whether
the remainder behind the waw is a word, the entry for دَمْع carried دُمُوع,
and أَدْمُع (the paucity plural — exactly the qiyāsī أَفْعُل of a فَعْل noun)
answered nobody. The entry now stores the attested plural. A lexicon field
nobody reads can hold anything; this one is read by the atf rule, so it
must hold what the text actually says.

**The five verbs drop their nun in the DUAL too — and a dropped nun is a receipt the writer must not erase.** تَرَيَا and تُتْعِبَا (the dual muḍāriʿ after a talab and a nahy) reached no cell: the candidate builder restored ونَ onto a bare group-waw since ch39 and never انِ onto a bare fatḥa-alif. It offers the dual's nun now, for matching only. Two things followed. The jawāb-al-talab detector reads the fallen nun as the jazm SHAPE (a muḍāriʿ cell ending انِ/ونَ/ينَ whose written form has no nun), and DabtEngine names the jazm after a talab from the same fact. And the ḍabṭ writer, handed a raf' verdict on such a word, used to append the nun's KASRA to the alif (تَرَيَاِ): where the page has already dropped the nun the letters say nasb-or-jazm and raf' is impossible — the writer keeps the nun-less form and, under a raf' verdict, withdraws as undecided rather than dress the word with a nun the text does not carry (تَرَيَا opening a sentence whose talab stands in the sentence before). A verdict the letters refute is not written; it is withdrawn.

**A context rule needs its own controls before it ships — the arbiter's clause-head rule cost دَارِكَ within the hour.** «A clause-head word on a final fatḥa before an ال-noun on a ḍamma is a māḍī and its fāʿil» is true (أَنْبَتَ الرَّبِيعُ) and the bank refused it at once: سَعْدٌ فِي دَارِكَ السَّفَّاحُ — the fatḥa is the PRONOUN's, and the particle before the word is a JARR letter, and nothing a jarr letter governs is a verb. Both guards were already doctrine elsewhere in this file (the seam; the sixth demotion guard); the new rule had to be told. And the construct dual behind a pronoun (نَظَرَيْكُمَا) was refused by a person-prefix guard written for bare words — a verb host before an object pronoun never ends in a bare يْ, so behind a pronoun that guard stands down and the lexicon-owned stem and the corpus-cell test do the refusing.

**Progress is keyed by CHAPTER and sentence id — a bare id could never finish a book.** Sentence ids restart every chapter (s1, s2… in each), and `markRead` stored the bare id: reading chapter 1's s3 marked every chapter's s3 read, `storyStats` could count at most one chapter's worth of ids, and no multi-chapter story could ever raise its completion toast or retire its continue card. The release gate found it only because this week's Lite rotation put a nine-chapter story first on the shelf — the check had picked a one-chapter story for 130 versions. `progKey(sen, ch)` writes `n:id`, `senRead` reads it (and honours a legacy bare key only in a one-chapter story, where it cannot collide), `SENTENCE_FLAT` carries the chapter, and the Atlas's read-glow matches an anchor's bare id against any chapter's key, because anchors carry no chapter. The tests that seeded progress by bare id were wrong for the same reason and seed by `progKey` now. Two lessons: a rotation-dependent pick is a test that runs a different test each week, and a store keyed on something that repeats is a bug waiting for the first record that repeats.

**The corpus walk is the analyzer's whole cost — memoise the WORD, not the model.** Timed at v170 on twelve creed sentences: 97% of `analyze()` sat in `RootFinder.fromCorpus` — 58–67 ms a call, thirty-odd calls a sentence, each call re-walking ~270 paradigms and every cell of each. The Taʿalluq gate analyses the whole corpus (2,200 sentences) and was reading as a hang at 98% CPU eighteen minutes in; it was not hung, it was slow, and it had been slow since the walk was written (v169: 1.7 s a sentence, v170 before the memo: 2.3 s). The answer for a written word depends on nothing but the corpus, so `fromCorpus` now memoises per word (bounded, dropped whenever the corpus index object changes) — 1.26 s a sentence cold, far less warm. This is NOT the rejected tagger memo: that one was keyed on a model that `evalUnseen` swaps behind the caller's back; nothing swaps the corpus. The lesson underneath: when a gate «hangs», measure before killing it — two release runs were killed inside a check that would have finished — and when a helper is 97% of the cost, the memo goes on the helper.

**What the full release found that the measured gates had not — four regressions, each a wave-16 rule reaching one word too far.** The wave's engines were measured on their own chapters before the release; the release then ran every gate, and four earlier ones FAILed — the record, so the next wave measures the neighbours too. (1) `mudafHuruf` false alarm on أَهْلُوهُمَا (bad-al-amali 4:s19): the new pronoun-annexed construct (`enc`) is a mudaf whose mudaf ilayh is ON the word, so the next word owes it nothing — the Qawaid rule now reads `c.enc` and leaves the neighbour alone. (2) The memo hands out COPIES: a caller may annotate the cell it gets back, and a shared object would carry that annotation into the next sentence — `fromCorpus` copies on the way in and on the way out. (3) كَلَامِ آخَرَ: the chain adoption's «a masdar head keeps a sifa-shaped member» guard (`!masdarHead`) had grown teeth once `masdarShape` learned فَعَال (كَلَام), and swallowed the diptote sifa; the diptote sifas (آخَر، أُخْرَى، كُبْرَى…) now cut the chain whatever the head. (4) زَيْدٌ كَالْبَحْرِ كَرَمًا lost its wajh twice over: the wajh reader's «no fused jarr letter» test was a bare-letter regex that read the kaf OF كَرَمًا as a clitic (it now asks `fused()` first), and the ḍabṭ ladder, having correctly learnt that a fused-kaf phrase after the mubtada IS the khabar, left the fathatan noun after it with no rule at all — a fathatan noun after a finished nominal sentence is now its tamyiz (a masdar) or its hal, never nothing. And the idafa-tashbih frame (4c) read حُمْرِ الْيَوَاقِيتِ as «the donkeys of the rubies»: the colour plural فُعْل annexed to its own noun is a sifa on its mawsuf, and its bare letters spelling a stock word (حُمُر) is no evidence — the rule now refuses the فُعْل shape and any sifa-shaped head. Two more surfaced on the rerun: the qulub frame (عَلِمْتُ زَيْدًا أَسَدًا) took a second object from ANYWHERE after the first — تَرَيَا وُجُوهَ الْأَرْضِ كَيْفَ تَصَوَّرُ handed it the verb behind كَيْفَ; the second object now stands right after the first's cluster and is never a verb cell. And the lab gate counted two chips where the v170 design draws three (the rank chip is a claim, not decoration) — the gate reads the design, not the other way round.

## The istiʿara's kinds — the engine graded on the authored fields (wave 17, v171)

Chapters 52–54 of the Talkhīṣ carry 68 sentences and 37 majaz frames, and every istiʿara frame now carries an **`istiara` object** — lafz (asliyya / tabaʿiyya), the clue's seat, the ends (wifaqiyya / ʿinadiyya), the jamiʿ (ʿammiyya / khassiyya), the sensory triple, and the mulaʾim words by index with their kind (mutlaqa / mujarrada / murashshaha / both). `IstiaraEngine` settles what the surface settles — the lafz off the lent word's class, the seat off DabtEngine's own seats (maful2 > maful > majrur > fail, picked by POSITION, a pronoun never a clue), the mulaʾim off a stored field table and off what hangs on the lent word, the ends off the non-existent noun and the verb with its contrary — and `agree()` grades the engine on the authored fields where it is sure. Endings-mode ḍabṭ: ch52 100, ch53 98.8, ch54 98.6 (floors 97/96/96). The wave's rules, each paid for by a named token:

- **A lemma never wears a joining clitic.** Fifteen seat tests stripped `^[وف]` off the LEMMA before matching it against the author's-voice, two-object, giving and physical verb tables — so فَسَّرَ tested as «سر», وَجَدَ as «جد», وَهَبَ as «هب», and every one of those verbs lost its rule. The clitic strip belongs to the WRITTEN word; the dictionary form is already bare of it. Grep for `.lemma || "").replace(/^[وف]/` before writing another table test.
- **The citation opens a new clause, and it must be decided FIRST.** كَقَوْلِ / كَمَا فِي reset every open seat; placed after the verb's seats, the rule let the citation's first word be claimed as the earlier verb's object (مُقَذَّفٍ as the maful of يَجْتَمِعَانِ). A reset that stands after the rules it is meant to fence is a comment, not a rule. And the analyzer's «nothing a jarr letter governs is a verb» stands down for the فِي of كَمَا فِي — the cited sentence (نَطَقَتِ الْحَالُ) is quoted whole.
- **ال before a sun letter always doubles it — at the analyzer's own article test.** The wave-14 rule lived in `articleOn` and the analyzer's enclitic peel and noun classification still read `/^ال/` on the bare letters, so فَالْتَقَطَهُ آلُ فِرْعَوْنَ was «the article + تقط + a blocked pronoun». `MaEngine.realAl` is the one test now; unvowelled input keeps the article reading, because nothing refutes it.
- **A whole stored cell is never split into host and pronoun.** The endings strip took نَا off أَخَذْنَا and stripped the host's «ending» — the sukun that IS the first-plural cell — so the writer rebuilt «he took us». The strip asks the corpus for the whole word first (mark for mark) and only then peels.
- **The relative's verb carries its ʿāʾid as the concealed doer** (وَمَا يُشْتَقُّ مِنْهُ، بِمَا يُلَائِمُ الْمُسْتَعَارَ) — presumed only where no bare noun stands ready to be the doer (وَالْعِنَادِيَّةُ مَا امْتَنَعَ اجْتِمَاعُ طَرَفَيْهَا keeps its named one), or where the relative is fused (بِمَا) and a definite follows. And a passive verb takes no object at all: its second object comes only through the two-object table, and a ma'tuf on its naib REOPENS that seat (فَيُسَمَّى التَّشْبِيهُ اسْتِعَارَةً … وَإِثْبَاتُ ذَلِكَ الْأَمْرِ اسْتِعَارَةً).
- **The annex-to-relative rule asked for LETTERS and got the jarr letter.** «A bare noun before مَا/مَنْ is annexed» matched مِنْ the preposition by its two letters, so مُسْتَعَارَةٌ مِنْ and مُقْتَبَسٌ مِنْ became mudafs and lost their tanwin. A rule keyed on a spelling shared by two closed classes must ask the row's KIND — the closed-class-interface lesson, once more.
- **The clause-initial shibh jumla is the khabar muqaddam** — a zarf with its mudaf ilayh, a fused pronoun — and the noun after it the mubtada whether definite or not (وَعِنْدَ السَّكَّاكِيِّ الِاسْتِعَارَةُ، لَهُ لِبَدٌ، عِنْدِي أَسَدٌ), unless a bare noun follows to be the khabar itself (الِاسْتِعَارَةُ مُصَرَّحَةٌ). The na't rule stands down for an ال-noun after a zarf's mudaf ilayh when no mubtada has been seen; and a delayed fa'il after a jarr phrase (سَالَتْ بِأَعْنَاقِ الْمَطِيِّ الْأَبَاطِحُ) is not the majrur's na't while the verb still owes its doer.
- **The seat picked by POSITION, the zarf read off the BARE word.** IstiaraEngine's lahu test read `core(لَدَى)` — and `core()` peels a leading lam as a clitic, leaving «دى», so the zarf was counted as a mulaʾim. Every closed-class test that runs on `core()` must also run on `bare()`.
- **The zarf wearing the speaker's ya** (عِنْدِي، لَدَيَّ) is ruled `keep/zarf` (nasb estimated before the ya) and annexes nothing after it — it had been heading a chain onto أَسَدٌ and reading as a mubtada, which hid the book's own istiʿara mutlaqa from the engine.
- **Two words, one letter's vowel, fifth payment:** أَيْ on a sukun is the explaining particle («that is») and أَيّ with a shadda the conditional noun — the ShartEngine was reading يَجْتَمِعَانِ as the jawab of «i.e.». The pk is «tafsir», the kind particle, and the shart-noun frame stands down on it.
- **The manqus with its ya restored in idafa** (شَاكِي السِّلَاحِ): the lexicon owns شَاكٍ, the written form carries the ya back, and the bare ya without a shadda is the noun's own letter, never the speaker's — the wholeNoun test now compares the lemma against the core minus that ya. Likewise the article-swallowing لِلْ hides the lexicon's whole word (لِلتَّهَكُّمِ was peeled as «تَهَ + كُمْ»).
- **Small closed sets the chapters forced:** آلُ before a noun is the family, never the mazi آلَ; عَابِرُ سَبِيلٍ is annexed (a participle head before a member the lexicon owns as a plain noun); a number after a noun is never its mudaf ilayh (إِبِلًا مِائَةً); a nisba after a masdar head is its na't (اسْتِعَارَةً تَخْيِيلِيَّةً); كَذَا behind a fused letter is still mabni; لِئَلَّا governs the verb in nasb; the pair of joined ال-nouns before their dual verb opens a new sentence (وَالْهِدَايَةُ وَالْإِحْيَاءُ يَجْتَمِعَانِ); إِمَّا … أَوْ joins onto the word after إِمَّا; the hal after a verb of the intransitive shapes (تَبَسَّمَ ضَاحِكًا — the shape test folds the vowels first, or the fatha on the ta breaks it); the future sin sits directly on its verb, so nothing peels after it and سَبِيلٍ is no jussive of وَلِيَ; the symbol row (ﷺ) is written as it stands.
- **Two receipts the writer now honours:** the iltiqa kasra on the feminine ta before a wasl alif (نَطَقَتِ الْحَالُ — offered back as the cell's sukun for matching) and the iltiqa damma on the group's waw (اشْتَرَوُا الضَّلَالَةَ — written where the next word opens on a wasl alif).
- **The MajazEngine's doer may stand BEFORE its verb** (إِذَا الْمَنِيَّةُ أَنْشَبَتْ أَظْفَارَهَا — the makniyya's abstract doer is the mubtada, not a fail after the verb), and a stock noun standing as a mubtada muʾakhkhar after a place has its clue in the place (عِنْدِي أَسَدٌ).
- **The seam tail is a pronoun only with the pronoun's OWN vowel.** The seam guard's tail regex matched any ه or ك (or كن، نا…) at a word's end with any marks, so أَمْكَنَ (…كَنَ) and شُبِّهَ (…هَ) were read as host + pronoun, the «seam» vowel then disagreed with the cell, and both verbs went noun — every relative's sila on such a verb was lost. On a vowelled word the tail must wear its vowel (هُ/هِ، كَ/كِ، هُمْ، كُمْ، نَا، هَا…); the loose pattern stays for unvowelled input. And the speaker's-ya refusal compares skeletons with the joining clitic off (وَعُرِّيَ) and stands down where the CELL itself ends in that ya.
- **The bank's first run after the wave named the rest:** the seven تَعَالَى of ch52 tagged «part» against every other chapter's «verb» (retagged — one token, one convention); ﷺ read as a noun by the analyzer (a symbol row is a particle for every reader of the rows, not only the ḍabṭ); كَذَا with a root guess (a closed-class kināya now, mabni); two paradigms the release audit refused — قَرَنَ and أَثْبَتَ, a lām that is ن or ت meeting the same suffix letter, written with the fakk because the author script skipped the `idgham` wrapper this file already prescribes; and two iʿrāb lines whose FIRST case keyword belonged to a neighbour (وَسَالَتْ read as «jarr» off its clue's مَجْرُور, كَاللُّغْزِ as «harf» off its kāf) — the case reader takes the first keyword, so the token's own case is stated first.
- **What the full release found after the measured gates were green — six regressions, each a new rule reaching one word too far.** (1) The strict seam-tail pattern refused the WASL vowel on a pronoun's mim (جَاءَتْهُمُ الْبَيِّنَاتُ، أَمَرَكُمُ اللهُ) — the pronoun wears its own vowel, and the letter after it may wear the meeting-of-sakins damma. (2) The author's-voice rule overrode a WRITTEN damma: شَبَّهَ الشَّاعِرُ الْعِلْمَ names its doer, and a noun wearing raf' is never the author's object. (3) The كَمَا فِي exemption dropped the jarr on a cited NOUN (كَمَا فِي تَشْبِيهِ ثَوْبٍ): the flag now only stands the verb guard down; the word keeps its afterJarr. (4) The إِمَّا … أَوْ pairing stole a pronoun-bearing ma'tuf from the parity walk (فِي نَوْعِهِ أَوْ جِنْسِهِ) — it applies to a bare ma'tuf only. (5) Fixing the speaker's-ya guard took away an accident the annexed-masdar frame had leaned on: يُقْعِي جُلُوسَ الْبَدَوِيِّ had «found» its mushabbah in a phantom pronoun; the frame now names the hidden doer of a third-person verb on its own. (6) Two Qawaid alarms on the new chapters were old holes the content exposed: IrabSign's seam peel and the CASE layer's did not know لِلْ as the article (لِلْمُشَبَّهِ lost its ha and read nasb), and the governor walk broke at a verb before reaching the jarr phrase a joined majrur joins (وَمَا يُشْتَقُّ مِنْهُ وَالْحَرْفِ). Meta-rule, restated with a cost attached: measure the neighbours BEFORE the release — the full run costs two hours per pass and this wave paid three.
- **The git checkout that ate a wave.** `git checkout -- prototype/reader.html` restored the committed v170 shell and discarded every uncommitted wave-17 patch; the shell was rebuilt from the patch scripts in the scratchpad plus two inline edits recovered from the session transcript. Keep every engine edit in a numbered patch script (patch17a…), never inline, so a lost working tree is a replay and not a loss.

## The kinaya's kinds, the tibaq, and the ghost layer — four engines graded on their own chapters (wave 18, v172)

Chapters 55–57 of the Talkhīṣ carry the majāz by omission and addition, the
kināya's three kinds and Sakkākī's four names, and the opening of the badīʿ
with the ṭibāq. Four engines arrived with them, and every one is graded on
something a human wrote down: **KinayaEngine** (10/10 authored frames),
**BadiEngine** (6/6), **TaqdirEngine** (97.8% recall against the corpus's
own «ضَمِيرٌ مُسْتَتِرٌ» lines, every named pronoun right, no false ghost),
**SifaEngine** (98.9% against the glossary's own kinds over 271 entries).
Endings-mode ḍabṭ: ch55 98.0, ch56 96.0, ch57 100 (floors 95/92/97). The
lessons, each paid for by a named token:

- **A helper's name is not its contract — read it before you lean on it.**
  The kināya's article test was `MajazEngine.core(w)` + `/^ال/`, and
  `MajazEngine.core` STRIPS the article (and a leading ب/ل/ك: بَيْنَ came
  back as «ين»). `hasAl` was never true and the nisba rule never saw its
  zarf; nine authored frames failed on one borrowed function. The fix reads
  the bare word. This is the `stem`-chain lesson (v130) again: a helper
  written for one question is wrong for the next.
- **A regex skeleton that deletes the sukūn cannot match a pattern that
  asks for one.** `SifaEngine.classify` stripped `[ًٌٍْ]` and then tested
  `مَفْعُول` with an explicit ْ — 46.9% on the audit, and مَوْجُود «unknown».
  Keep the sukūn in the skeleton and make it optional in the patterns
  (unvowelled input); the NFC shadda rides between a letter and its vowel,
  so the mim-forms test a shadda-less copy. 46.9 → 98.9 in one patch.
- **The cell's form is the paradigm's spelling, never the written word's.**
  The whole-word match learnt to see through a joining wāw (وَأُعْطِيَ) and
  returned `form: "وَقَتَلَ"` — so `joined()` compared the cell against itself
  and every «قَتَلَ الْبُخْلَ وَأَحْيَا السَّمَاحَا» lost its inherited doer. The
  neighbour sweep caught it in ch53; the fix is one line.
- **A rule for one word stands down while a larger frame is open.** «وَاحِد
  after an indefinite is its naʿt» (نَوْعٍ وَاحِدٍ) stole the first item of a
  number's list (سَبْعَةُ أَقْسَامٍ وَاحِدٌ حِسِّيٌّ …) from badal al-tafṣīl and
  dropped ch48 below its floor. `!(st.tafsil && !st.tafsil.used)`.
- **The full-mode readers may read the marks; the rebuilder may not.**
  `DabtEngine.writtenCase` reads a written ending (through a shadda, past
  the tanwīn's seat, not on the dual's kasra-nūn or the plural's fatḥa-nūn)
  and in FULL mode only: a written fatḥa on the first noun after a verb
  says the doer is concealed (يُمِيتُ الْخَلْقَ), after كَانَ that its ism is
  (كَانَ مُتَرَدِّدًا), after a passive it is the ḥāl or the second object
  (لَمْ يُعْرَفْ نَبِيًّا, يُسَمَّى ابْتِدَائِيًّا), a written kasra is never kāna's
  ism (الْكَامِلَةِ is a naʿt) and after وَلَا joins the majrūr (لَيْسَ بِعَرَضٍ
  وَلَا جِسْمٍ). In endings mode nothing is written and nothing changes —
  the ḍabṭ numbers are untouched, the ghost recall went 75 → 98.
- **The mazi's first and second persons WRITE their doer.** `PRON.mazi`
  offered أَنَا for قُلْتُ and the corpus refused it as a false ghost within
  the minute; only the third persons conceal in the māḍī.
- **The named-doer scan stops at the next clause.** A doer found anywhere
  later in the sentence is not this verb's; the scan breaks on a verb, a
  clause particle (inna, shart, istifhām, nidāʾ, ʿaṭf), or a seat that
  comes after the doer's (any khabar, a new mubtada).
- **A negated assertion is not the assertion.** «نَائِبُ الْفَاعِلِ هُنَا مَذْكُورٌ لَا
  مُسْتَتِرٌ» matched `/مُسْتَتِر/` and was graded as a ghost the engine missed.
  Strip «لَا / لَيْسَ / غَيْرُ + مُسْتَتِر» before testing.
- **The ghost layer on the page reads the STORED line; the engine's ghosts
  live in the sheet.** `TaqdirEngine.fromLine` is a regex over the human
  iʿrāb (334 ghosts over the corpus, 0 ms); the engine analyses one sentence
  in the sheet and the lab. A story renders hundreds of words at once — the
  jml-chip lesson, one layer over.
- **Two engines that read the same seats must be graded together.** The
  chapter probe printed `KN:` lines only when the builder forwarded the
  `kinaya` field — it had not — so the first run showed engine reads
  (`KN-UNEXPECTED`) and no agreements at all. When a new authored field
  enters a chapter, the builder's forwarding list is the first thing to
  check, before the engine.
- **A table that «outranks every reading below» must be TESTED before them.** The
  received mursal pairs sat under the omission rule with a comment promising
  precedence; nothing enforced it, and the moment the nahw got نَادِيَهُ right
  (its written fatḥa: the object) the omission rule reached it first and
  فَلْيَدْعُ نَادِيَهُ stopped being the table's mursal. A precedence stated in a
  comment is a precedence that does not exist.
- **A rule tightened with a state the previous line resets is a dead rule.**
  «The clause verb is spent, the noun is inna's khabar» gained `st.innaOpen`
  in wave 18 — and the verb branch closes inna two hundred lines earlier, so
  the rule never fired again and كَأَنَّهَا … ضَعُفْنَ بِهَا أَوَائِلُ lost its
  khabar. When adding a state test to an old rule, grep for where that state
  is written between the two.
- **«The pronoun ism does the khabar's act» only where the cell conceals its
  doer.** أَنَّهَا تُخَالِفُ is a 3fs cell; ضَعُفْنَ writes its own doer in the nūn.
  Guard on cell 0/3 — the same «read the person» lesson as the after-verb
  expectations (v155).
- **الدُّنْيَا writes فُعْلَى with a plain alif.** The gender bar on an ال-naʿt read
  «no tāʾ» as masculine and refused الْحَيَاةِ الدُّنْيَا; a maqṣūr or mamdūd
  ending (ى, يا, اء) cannot tell gender, so it does not bar.
- **`naqis1` builds the alif-type māḍī and nothing warns you** — the ch8
  lesson, paid again on خَشِيَ (*خَشِى، *خَشِوْا shipped to the regeneration
  gate). A samiʿa-bāb nāqiṣ goes through `entry()` with `mazi_naqis_kasra`;
  and `put_morph` only ADDS, so a wrong stored paradigm must be deleted
  before the script can replace it.
- **A new registry GROUP breaks every gate that pinned the old one.** Moving
  ṭibāq/muqābala to `badi` and kināya to `bayan` failed the wave-2 «fourth
  group» gates and the plain-lede check keyed on the word «opposite»; widen
  the gates to the balāgha family, and reword the lede, on the day the group
  is added — before the two-hour run finds them.
- **Measure the neighbours BEFORE the release, in the background.** A
  named-gate sweep (the ḍabṭ floors, the wave-14/16/17 chapter gates) runs
  in ~25 minutes under nohup and found both regressions above while the
  design work went on; the release run costs two hours per pass.

## The badiʿ read whole, the letters aligned, and a learned layer that is graded against the rules (wave 19, v173)

Chapters 58–60 of the Talkhīṣ carry fifteen more figures of the badīʿ — the
muqābala, murāʿāt al-naẓīr, tashābuh al-aṭrāf, īhām al-tanāsub, the irṣād,
mushākala, muzāwaja, ʿaks, rujūʿ, tawriya, istikhdām, laff wa-nashr — and the
two lafẓī figures the notes had only described, the jinās and the sajʿ, now
have engines. Every figure is graded on something a human wrote: 40 authored
badīʿ frames (ch58 19/19, ch59 12/12, ch60 9/9 read back), the notes' own
jinās examples 4/4 and sajʿ examples 3/3, and the corpus's sarf and iʿrāb
labels for the learned layer. Endings-mode ḍabṭ: ch58 98.3, ch59 97.0,
ch60 99.5 (floors 96/95/97). The lessons, each paid for by a named
token or a named afternoon:

- **A figure's frame is a SHAPE, and the validator learns the shape before
  the engine does.** The badīʿ block in `validate_content.py` was one
  `{kind, pair}` test; the fifteen kinds need `first/second`, `set`, `pairs`,
  `word/companion`, `refs`, `near/far`, `murad/other`, `field`, `asl` — so
  the block is now generic (`BADI_KINDS / BADI_FIELDS / BADI_SUBS`), with
  the one structural rule the books state (a laff-nashr ijmālī has ONE first
  and two or more seconds) written in as a check. And the probe harness has
  the same contract: `probe18` crashed on `f.pair.join` the moment a frame
  without `pair` arrived, and — subtler — it grades `BadiEngine.read(rows)`
  WITHOUT the sentence, so the HINTED figures (mushākala, tawriya, istikhdām:
  the frame names the word, the engine reads the rest) report `none` there
  and `ok` in `probe19`. Read a probe's `BAD` against what the probe was
  handed before reading it against the engine.
- **The hinted figure is the honest half of the badīʿ engine.** Whether
  اطْبُخُوا was said for خِيطُوا is knowledge of the two things; the engine
  claims only what the surface settles — the companion word that shares a
  stem (taḥqīq vs taqdīr), the pronouns that return to an istikhdām's word
  (lafẓ-ḍamīr vs ḍamīrayn), the furnishing that makes a tawriya murashshaḥa
  — and the tawriya's FURNISH table lost عرش under استوى because a stored
  furnishing that the books do not recite is a guess dressed as a table.
- **The ʿaks is read by LEMMA KEY, and the pronoun is its own key.** عَادَاتُ
  السَّادَاتِ سَادَاتُ الْعَادَاتِ is (A,B)(B,A) by lemma; لَهَا مَا كَسَبَتْ وَعَلَيْهَا
  is (pronoun, particle)(particle, pronoun) — so a fused jarr+pronoun yields
  the PRONOUN as key and the ṭarafayn shape is two pronouns around two
  particles. And a muqābala whose four words are exactly an ʿaks IS the ʿaks:
  the muqābala reader is run first and its frame withdrawn when the ʿaks
  reader claims the same four indexes.
- **The negation the tashābuh and the rujūʿ need must not be a relative.**
  `negBefore` read every مَا as a negation; after a jarr letter or a mawṣūl
  it is the relative, and the rujūʿ's «negated clause, then بَلَى» fired on
  the wrong clause. Same lesson as MaEngine's whole bab, at a new consumer.
- **`joined()` must open on a hamza.** The lexicon test behind the wāw refused
  every hamza-initial remainder (وَأَقْبَحَ), because the regex that guessed a
  word from its letters started at ب; the segment/lexicon route now runs
  first and the regex only for five-letter-plus remainders.
- **Jinās is read by ROOT first, then by letters.** الْمَالِ / بِمَالٍ is no
  jinās muḥarraf — the clitic is not a letter of the word — so `vowels()`
  strips و/ف and ب/ل/ك before comparing, and the article's shadda with them;
  ishtiqāq is decided by `rootOf` (memoised: the corpus sweep in the jinās
  game walked every pair's lexicon roots and timed out until it was) before
  any letter test; sameKey by lemma + class refuses a word against itself.
  The letter-true oddities the sweep still shows (الْبَشَرِ بَكْرٍ) are what
  the books call jinās too — leave them.
- **Sajʿ is clauses, not words.** The first cut rhymed coordinated single
  words and sound plurals (every ـِينَ rhymes with every ـِينَ). Clauses are
  cut only at wāw joiners that open a clause (a verb, a particle, a fresh
  mubtada, noun+noun), each must be two words or more, the pausal form drops
  ًا and ة before the rhyme is read, and a sound-plural rhyme is refused.
  The near-miss the sajʿ note already teaches (كَشَجَرٍ بِلَا ثَمَرٍ — two
  fawāṣil on different letters) is the control.
- **A model trained on the rules' own labels is graded against the rules.**
  `BabModel` (multinomial LR on `content/models/bab_model.json`, trained by
  `tools/ml/train_bab.py` on the corpus's 265 Form-I verbs) predicts the
  samāʿī bāb of a root the corpus has never met: 57.0% held-out top-1, 76.2%
  top-2 against a 35.5% majority — ablations with class features and bigrams
  were WORSE, so the base features ship. `SeatModel` (naive Bayes over
  `RuleMiner.feats`) is evaluated by story parity against DabtEngine on the
  same tokens: engine 65.0% (19% undecided), model 51.9% — the model loses to
  the rules, which is the finding: on its CONFIDENT subset (204 of 675) it
  reaches 81.4%, and that is the only place the app lets it speak. The miner
  writes 59 rules of the form `p=jarr & e=0 → majrur (111, 100%)` — the
  Awāmil doctrine re-derived from labels — and the Learning lab prints them
  with their support. Two traps: the first name (`IrabModel`) collided with
  the perceptron the app already has — grep for a class name before minting
  it; and a full-corpus evaluation ran past fifteen minutes and closed the
  Playwright target — cap per story (40) and gather in slices.
- **The Sarf lab wears the model's badge only where the paradigm is silent.**
  A root the corpus recites gets its bāb from the corpus; the 🧠 badge with
  a percentage appears only when no stored paradigm answers, and the
  percentage is rendered `dir="ltr"` so the number does not flip.
- **The nahw the badīʿ chapters forced (patch19g–l), each rule named by its
  token:** the mufarragh exception (لَنْ يَدْخُلَ الْجَنَّةَ إِلَّا مَنْ — the noun
  before إِلَّا is the object, the word after it the doer); the verb of wonder
  conceals its doer (مَا أَحْسَنَ الدِّينَ … وَأَقْبَحَ الْكُفْرَ, a TAAJJUB set); a
  transitive verb right after a relative carries the relative as doer and a
  plain definite noun after it is the object (بِمَا يُنَاسِبُ ابْتِدَاءَهُ، مِمَّا
  يُلَائِمُ الْقَرِيبَ) — guarded three ways, each by a regression the baseline
  sweep caught: never an intransitive verb (مَا تَعَدَّدَ طَرَفَاهُ، مَا امْتَنَعَ
  اجْتِمَاعُ), never a construct or a chain head as the "object", and never a
  clause-initial مَا before a verb, which is the negation (فَمَا رَبِحَتْ
  تِجَارَتُهُمْ); the dual after a fronted jarr phrase is the delayed mubtada and
  the two indefinites after it its badal of detail (لَهُ مَعْنَيَانِ قَرِيبٌ وَبَعِيدٌ
  — even after a passive whose naib is already seated); a wāw-joined jarr
  particle after a complete nominal clause opens a new one; a clause-initial
  jarr phrase fronts the khabar and the DEFINITE noun after it is the mubtada,
  a bare indefinite after that its ḥāl (فَفِي الْأَوَّلَيْنِ مُرَاعَاةُ النَّظِيرِ
  حَقِيقَةً — the lexicon's plain masdar outranks the فَعِيلَة / مُفَاعَلَة shapes);
  a noun after ثُمَّ that repeats an earlier noun takes its case and annexes
  even a relative (ثُمَّ ذِكْرُ مَا لِكُلٍّ); after ثُمَّ and a jarr phrase a
  definite noun repeats the earlier clause's raf seat with the verb elided
  (ثُمَّ بِضَمِيرِهِ الْآخَرُ); غَيْر annexes ONE noun and a bare indefinite after its
  member is the ḥāl (مِنْ غَيْرِ تَعْيِينٍ ثِقَةً); the noun after بَلْ takes the last
  head's case and an indefinite sifa after it is the ḥāl (بَلِ الْأَسْهُمِ
  مَبْرِيَّةً); a sentence opening وَقَوْلِ + a name continues the citation list
  (وَقَوْلِ الْبُحْتُرِيِّ), and the citation is a WALL for the atf walk; the five
  nouns the analyzer called particles (أَبِي دُلَامَةَ), ابن between two nouns is
  never the amr of بَنَى and the saying is annexed to the son (قَوْلُ ابْنِ
  حَيُّوسٍ), the dual annexed by its yāʾ (طَرَفَيْ جُمْلَةٍ); a kasra'd ب/ل on a
  word the lexicon owns as a noun is that noun whatever verb cell its letters
  reach (بِأَرْضِ قَوْمٍ ~ لَمْ أَرْضَ); the wāw-joined passive of a two-object
  verb whose clause already named its subject takes its SECOND object
  (وَتُسَمَّى التَّنَاسُبَ وَالتَّوْفِيقَ) while the fa-joined one before a definite
  noun and an indefinite names its own naib (فَسُمِّيَ الْإِيمَانُ صِبْغَةً); a
  two-object verb wearing its first object as a pronoun takes the next noun as
  its second (يُسَمُّونَهُ الْمَعْمُودِيَّةَ); the mood reaches over ثُمَّ and أَوْ onto
  a verb of the SAME VOICE (ثُمَّ يُؤَخَّرَ؛ أَوْ يُرَادَ) and a voice shift opens a
  new clause (وَيَقَعُ عَلَى وُجُوهٍ) — the copula excepted (فَتَكُونَ); a joined
  ال-noun opening a clause before a verb whose object pronoun returns to it is
  the ishtighāl (وَالسَّمَاءَ بَنَيْنَاهَا); the speaker's 1s muḍāriʿ and the
  passive māḍī share their letters, and after a relative the doer is its
  ʿāʾid (وَمَا أُضِيفَ إِلَيْهِ); a lām-clitic verb is not a joined noun's OWN verb
  (اللَّيْلَ وَالنَّهَارَ لِتَسْكُنُوا); the writer writes the annexed dual by its letter
  and the five verbs' nūn behind a shadda (يُسَمُّونَهُ، يَحِلُّونَ — NFC writes
  vowel, shadda, wāw, and the old regex asked for the vowel beside the wāw);
  a diptote name before ابن loses its tanwīn and KEEPS its jarr fatḥa
  (مُعَاوِيَةَ بْنِ مَالِكٍ). Endings-mode ḍabṭ went ch58 93.1 → 98.3, ch59 92.9
  → 97.0, ch60 89.7 → 99.5 across the patches, and the regression sweep of
  ch48–57 came back to its baseline.
- **A twin candidate offered to EVERY word steals every word's person.** The
  hollow's shortened majzūm is stored for the 3ms only (يُجِدْ), so patch19h
  offered the yāʾ-prefixed twin of any نـ/أـ/تـ word as a matching candidate —
  and the exact pass met the 3ms cell FIRST for every ordinary verb: فَتَكُونَ
  read as يَكُونُ, نَقْرِيهِمْ as يَقْرِي, أُرِيدَ as يُرِيدُ, تَجِدُ as «he». Five
  chapters lost a point each and nothing in the new chapters' numbers said so.
  The twin now lives in `findFormInParadigm` as a LAST resort, on the three
  governed cells only, after every stored cell has refused. **A candidate that
  can match a commoner cell than the one it was written for must be tried after
  that cell, not beside it** — and the baseline diff (every chapter, before and
  after, sentence by sentence) is what found it; the per-chapter totals alone
  read as «−1, probably noise».
- **`joined()` must see a verb the analyzer guessed by its prefix.** With no
  cell and no lemma, وَتُسَمَّى was «not joined», so it inherited nothing from its
  clause; no verb opens on wāw + a person letter, so the wāw is a joiner.
- **The vowelled-word rewrite block runs only on UNMARKED input.** Three rules
  written into it (بِأَرْضِ, the amr after a pronoun, the annexed pairs) never
  fired in endings mode, because the block's first line is «if the word carries
  a mark, return». Read a block's guard before adding a rule to it; the rules
  moved to the pre-pass that sees every row.
- **Stems go into the generator WITHOUT their sukūn — fourth payment, five
  verbs at once.** The ch59 script passed «أَجَدْ», «جَاوَزْ», «لَجِجْ» and every cell
  shipped a doubled sukūn (invisible on the page, refused by the audit); the
  amr of a wasl-alif verb stores its VOWEL (اِبْكِ، اُسْلُ، اِسْتَغْنَى — the engine's
  spelling, which the audit compares); a nūn-final lām needs the `idgham`
  wrapper (سَكَنَّ). And the engine had its own hole: a bāb-سَمِعَ geminate breaks
  its stem with the bāb's OWN vowel (لَجِجْتُ، عَضِضْتُ), and the Form-I geminate
  branch had written the fatḥa for every bāb. The audit is what makes any of
  this visible; `sarfAudit()` is now pinned empty in the wave's own gate.
- **A glossary lemma is ONE word.** «مُعَاوِيَةُ بْنُ مَالِكٍ» as the lemma of the
  token مُعَاوِيَةَ hid the name from every lookup that compares the lemma against
  the host, and the diptote's fatḥa went with it; the rest of the name belongs
  in the gloss.
- **The ʿaks is adjacent and never runs through a joiner.** عَقْلِيٌّ وَمُرَكَّبٌ …
  وَمُرَكَّبٌ عَقْلِيٌّ is a list; السَّوَادِ لِبَيَانِ … لِبَيَانِ سَوَادِهِ is a phrase
  repeated four words apart. Both read as ʿaks until the corpus sweep printed
  them; the real ones (عَادَاتُ السَّادَاتِ، هُنَّ لَهُمْ … هُمْ لَهُنَّ) are gated
  beside the refusals.
- **A trace field that reads a `const` declared later kills the whole engine.**
  Widening the debug push with `copyMood` before its declaration threw a
  ReferenceError inside `decide()` for every sentence, and the probe that
  filtered for one line printed nothing at all. When a probe goes silent, run
  it unfiltered first.
- **A `//` comment appended to the FIRST line of a multi-line object literal
  comments out the rest of the object.** The diptote-before-ابن fix put its
  note at the end of `const opt = { definite: …,` and silently dropped
  `mudaf`, `dual`, `pron` and every field after — the writer put a tanwīn on
  every idafa head, dual and ẓarf in the corpus, and the pin that guarded the
  edit tested only the one word the edit was for. Three chapters fell ten
  points in the sweep before it was seen. Put the note on its own line, and
  pin a SENTENCE the change should not touch beside the word it should.
- **What the full release found after the measured gates were green — thirteen
  FAILs, four lessons.** (1) The twin's ونَ restoration (patch19a) made
  أَخُوكَ into أَخُونَ ~ خَانَ through the enclitic peel's alif-restored
  candidate: three old chapter gates, the Wāw engine's corpus score and the
  learned layer's engine accuracy all moved, and NONE of the wave's own
  measurements said so — a candidate rule must name the closed sets it may
  not touch (the five nouns' wāw), and the old gates are the neighbours'
  measurement. (2) **A glossary that grows can flip a rule that asks it.**
  The question-hamza peel accepts أَ + remainder when the lexicon owns the
  remainder; chapter 58 added the noun نَبْت, and the seed أَنْبَتَ الرَّبِيعُ
  became «is the plant…?» — the lookup answered by letters. The oracle is now
  asked with the MARKS (نَبْت is not نَبَتَ). (3) Old gates pin the old shape:
  the wave-18 Atlas gate asserted «jinās has no ring», the phone gate that the
  ṭibāq opens the kināya lab, the wave-18 seeds gate read `f.pair` on every
  frame — each true until this wave; widen the gate the day the engine grows,
  or the two-hour run finds it. (4) Three engines read one rule three ways:
  the citation نَحْوَ was cut in DabtEngine's chain, and QawaidEngine's own
  refused-head rule and the analyzer's dig still annexed it; the jarr clitic
  on a lexicon noun (بِأَرْضِ) and ابن were decided in DabtEngine's pre-pass
  while the ANALYZER still called them verbs, so the Qawāʿid ledger raised
  «majrūr with no governor». A fact about a WORD's class belongs in the
  analyzer, where every engine reads it; a fact about a SEAT belongs in
  DabtEngine. And `SMOKE_ONLY=<regex>` now runs a named subset of the suite
  for triage — the release still runs everything.
- **Self-kill, third AND fourth time.** `pgrep -f '[p]robe19.js sweep'` killed
  the shell that ran it because the SAME command line held a heredoc with the
  literal `probe19.js sweep`; a day later `pgrep -f "[d]abt19f"` killed its
  shell because a `sed … dabt19f.sh` stood three commands further along the
  same line. The bracket trick protects against the pgrep's OWN text and
  nothing else. A kill goes in a command of its own, with nothing after it.
- **An edit that is not written is not an edit.** The SeatModel rename was
  applied to the in-memory string and the file re-read before the write; the
  syntax error survived a whole design probe (`setPremium is not defined` was
  the script block failing to parse). When a probe reports an undefined global
  the reader has always defined, run the parse check first.

## The khātima: the ʿarūḍ engine, the takings, the received text, and the Talkhīṣ complete (wave 24, v178)

Chapters 73–76 close the Talkhīṣ al-Miftāḥ — 76 chapters, from the
definition of eloquence to the openings and closings of the suras. The
khātima: the poets' takings, plain (naskh / ighāra / ilmām) and hidden
(tashābuh / naql / ashmal / qalb / ziyāda) with the grades the book gives
(ch73–74); the iqtibas, the tadmin (istiʿāna / īdāʿ), the ʿaqd, the ḥall
and the talmīḥ (ch75); the three places of care — the fine opening and the
ill omen, barāʿat al-istihlāl, the takhalluṣ and the iqtiḍāb, the fasl
al-khitāb, the fine close — and the book's last sentence (ch76).
42 authored badīʿ frames read back; endings-mode ḍabṭ ch73 98.4 ·
ch74 99.7 · ch75 98.3 · ch76 99.6 (floors 97 / 97 / 96 / 97). The lessons:

- **A bayt is a measurable thing, and the engine measures it before it
  argues.** `ArudEngine.scan` turns the writing into its sukūn/ḥaraka
  string by the rules of the taqṭīʿ (the wasl of the article, the tanwīn's
  nūn, the long vowels, the shadda's doubled letter, the pausal close of
  the rhyme) and fits the sixteen metres with their licensed ziḥāfāt and
  ʿilal by cost; a bayt of prose scans to none. Seventeen bayts of known
  metre are the seeds, and every bayt of the corpus that carries a
  hemistich mark is scanned in the smoke (the mudawwar audit: a hemistich
  mark may not stand where the metre does not close the ṣadr).
  `QafiyaEngine.read` names the rawī, the waṣl and the khurūj, the ridf,
  the taʾsīs with its dakhīl, the majrā and the qāfiya's name.
- **The received text is found, not asserted.** `IqtibasEngine.RECEIVED`
  is a table of the ayas, the hadiths and the bayts the khātima cites;
  `read` finds each one inside the sentence (one word may differ — the
  taghyīr yasīr the book allows), reports the source and whether the
  words were changed, and reads a tadmin's sub off the length found
  (a whole bayt: istiʿāna; less: īdāʿ; two hemistichs of one source in one
  sentence: the whole). The ʿaqd, ḥall and talmīḥ are authored with their
  `source` and confirmed by it. Chapter 76's openings, transitions and
  closes are rows of the same table — the finder lights Imruʾ al-Qays's
  opening, Ibn Muqātil's ill omen, Abū Tammām's turn «كَلَّا وَلَكِنْ
  مَطْلَعَ الْجُودِ», the أَمَّا بَعْدُ of fasl al-khitāb, the Qurʾanic هَذَا of
  Ṣād 55 and 49, the writers' هَذَا بَابٌ, and the close that announces the
  end.
- **A taking is measured on words, roots and metre.** `SariqaEngine`
  compares the taker's line with the sentence the frame names in `with`
  (same chapter): the bare words shared, the roots shared, the baḥr and the
  rawī kept — and from those reads naskh (all the words), ighāra (most),
  ilmām (the meaning), and for the hidden kinds the book's names; the grade
  (mamdūḥ / madhmūm / mithl) is the book's, shown as its judgement.
- **The last two chapters forced twenty-odd nahw rules, each a receipt.**
  The extra مَا inside an idafa (غَيْرِ مَا جُرْمٍ: the member's head two
  back); the frozen verbs of praise and their doer (نِعْمَ الْوَكِيلُ) with the
  canonical form written; the question of wonder (مَا بَالُ: the khabar is
  no بِ + ال); the hamza of question on a noun the lexicon does not own
  whole (أَمَطْلَعَ، أَأَحْلَامُ) with its idafa, and the fronted object before a
  1st/2nd-person verb; the alif of release only on a participle's sound
  plural (رَاجِعُونَا, not عَوَالِينَا); F1's lookback stopping at a pronoun (أَوْ
  هُوَ أَقْرَبُ); the ism fiʿl on kasra (حَذَارِ) and بَعْدُ cut from its noun
  (أَمَّا بَعْدُ), both mabni with their ending written back; the joined
  citation head after the first (كَقَوْلِهِ … وَقَوْلِهِ); كُلَّ يَوْمٍ before a
  verb as a zarf with its annexed time noun keeping its tanwīn; the doer
  after قَدْ whatever noun stood before the فَ (بُشْرَى فَقَدْ أَنْجَزَ الْإِقْبَالُ);
  the she-verb's doer in the plural or feminine noun right after it
  (جَاءَتْ فَوَاتِحُ، سَاءَتْ ظُنُونُهُ، قَبُحَتْ فَعَلَاتُهُ); the joined أَفْعَل between
  two tamyīz nouns as the elative (أَعْذَبَ لَفْظًا وَأَحْسَنَ سَبْكًا); the elative
  before its tamyīz as kāna's khabar with her ism concealed; the list after
  a colon opening a nominal clause; the nisba after a definite noun as its
  naʿt (الْعَرَبِ الْجَاهِلِيَّةِ); the naming passive's second object after its
  deputy (يُسَمَّى تَضْمِينُ الْبَيْتِ … اسْتِعَانَةً); the sifa after a مَا-clause as
  the pronoun's khabar (وَأَنْتَ بِمَا أَمَّلْتُ مِنْكَ جَدِيرُ); the causative's second
  object after its clitic first (يُذْكِرُنِي … مَجَرَّ); the jussive of a naqis
  verb behind its object clitic, the dropped letter restored to find the
  cell (فَإِنْ تُولِنِي); a verb reading after a jarr letter refused (مِنْ قَدِّهَا);
  the joined demonstrative opening the second hemistich's clause (وَهَذَا
  دُعَاءٌ); the closing «or other» following the list's case.
- **The writer learned three things.** The ta'nith alif of the maqṣūr takes
  no tanwīn (ذِكْرَى، بُشْرَى، شَكْوَى، دُنْيَا — never مَعْنًى or فَتًى: four
  letters, the second sakin, no mīm); ʿAmr's silent wāw stands after the
  tanwīn as the page writes it (عَمْرٌو، لَعَمْرٌو، بِعَمْرٍو); and the author's
  qāfiya tag is a rhyme seat — the lone hemistich, the muṣarraʿ maṭlaʿ,
  and the sukūn-close of a muqayyada rhyme (الْوَكِيلْ) kept like the sajʿ's
  pausal close.
- **A lone أَمَّا is a hinge, not yet a division.** The taqsīm-by-أَمَّا reader
  fired on every «وَأَمَّا التَّخَلُّصُ فَهُوَ» definition; it now needs two shares
  in the sentence (or a share before it) to be sure, and offers one share
  as a candidate.
- **The regression sweep that closed the bundle (patches 24m / 24n / 24p).**
  Four waves landed in one release, so every earlier gate re-ran on the
  grown corpus and the sweep fixed what it found rather than moving floors:
  the maqṣūr with a pronoun is no dual in construct (مَعْنَاهُ — the name مَعْن
  had entered the lexicon); the Qawaid audit exempts what the khātima writes
  (a verb wearing a kasra, بْنِ, the fused كَ of a citation head, the dual's
  yāʾ, كَانَ + muḍāriʿ, the relative's verb, أَنْ before سَ, the elative
  khabar with its tamyīz, مَا بَالُ); the sajʿ clause cuts at a joined مَا;
  `decide()` now sees the author's ORIGINAL tokens (`DabtEngine._orig24`,
  set by `vowel()`) beside the stripped rows — the jawāb al-ṭalab
  (اقْتَرِحْ شَيْئًا نُجِدْ) is read off the author's sukūn and the oath particle
  only off its kasra (وَاللهُ أَحَقُّ is a mubtada; مُعْتَصِمٍ بِاللهِ a jarr
  phrase); JinasEngine.rootOf takes a verb row's own root before the
  lexicon's homograph (قَالَ / الْقَالِينَ); a joined she-verb inherits no
  hidden «we»; بَيْنَ X وَY is no pair when بَيْنَ returns; no imperative after
  a relative; the quoted predicate after كِنَايَةً عَنِ X; the joined noun
  before a repeated بِ-phrase; each إِمَّا-share as a khabar; نَحْوُ: after a stop;
  the giving verb's second object kept from the hal; the ات-naʿt onto a
  broken-plural head; the KinayaEngine's mawsuf run opening on a plain nakira
  predicate (24q). The release's own chunks then caught four more (24r): R9's
  doer swap asks for a masdar doer behind a non-agent noun (لَمْ يَكْتُبِ
  الطَّالِبُ دَرْسَهُ keeps its doer), the قَدْ-doer pre-pass leaves a sister of
  kāna her ism, the citation نَحْوَ stays mansub, نِعْمَ carries a jamid
  paradigm, the maqṣūr-construct guard asks for the host's own marks
  (ذُكْرَانًا is no ذِكْرَى), and the ʿarūḍ engine's mudawwar audit moved three
  hemistich marks to where the ṣadr closes (ch64 s3, ch73 s22, ch74 s15).
  Six ch73–76 paradigms were corrected against
  the reader's own `sarfAudit()` (the wawi naqis سَخَا, حَسَّنَّ by idgham, the
  wasl alif's kasra on the افْتَعَلَ verbs, the doubled أَلَمَّ unpacked). The
  JamEngine ceiling follows the corpus (151 heard plurals).

## The sajʿ cut on the author's pauses, four figures read as receipts, and the nahw the last lafẓī chapters forced (wave 23, v177)

Chapters 71–72 of the Talkhīṣ close the lafẓī badīʿ: the sajʿ by its three
kinds and its finest lengths, the sukūn close, the two qīls, the tashṭīr
(ch71); the muwāzana and mumāthala, the qalb of the whole, the tashrīʿ,
luzūm mā lā yalzam, and the closing principle that the words follow the
meanings (ch72). 29 authored badīʿ frames are read back (16 / 13); endings-
mode ḍabṭ ch71 100, ch72 100 (floors 97 / 96). The lessons:

- **The author's pause is data, and the engine reads it before it guesses.**
  The wave-19 sajʿ engine cut clauses at wāw joiners and refused every
  one-word clause; خُذُوهُ، فَغُلُّوهُ، ثُمَّ الْجَحِيمَ صَلُّوهُ has three clauses
  and two of them are one word. `SajEngine.cutsOf` now takes the cuts from
  the sentence's own `punctAfter` (`،` `؛` and the hemistich `*`), and a
  marked one-word clause is a clause; free text is read through
  `marksOf`, which lifts the same marks out of the string. The finest kind
  is then arithmetic on the clauses' content words (nouns and verbs, never
  pronouns — `cw23`): equal, second longer, third longer, shorter.
- **A wazn is counted on the madd letters, not on every mark.** The
  murassaʿ of al-Ḥarīrī (لَفْظِهِ / وَعْظِهِ) failed because the first cut
  weighed every ḥaraka and the joiner's fatḥa on وَعْظِهِ tipped the scale.
  `wazn()` strips a joining و/ف and the article (with the sun letter's
  shadda) and counts only `(?<=َ)ا | (?<=ُ)و | (?<=ِ)ي`, keeping the joiner's
  own fatḥa out of it. This is the ʿarūḍ's own notion of weight, and it is
  what makes the muwāzana (same wazn, different rawī) decidable at all.
- **The four last figures are receipts, and each names what it refuses.**
  Tashṭīr: the hemistich cut, a sajʿ pair in each half, and the two rawīs
  DIFFERENT (a bayt with one rawī is one sajʿ). Muwāzana: same wazn, not
  the same rawī; mumāthala when ≥ ceil(m/2) and ≥ 2 words of both clauses
  answer in wazn. Qalb al-kull: the bare letters of the line (seats folded,
  ة→ه, the first word's joiner tried both ways) are a palindrome of six
  letters or more — exact, or nothing. Tashrīʿ and luzūm are HINTED (the
  frame names the words; the engine confirms the rawīs differ, or that the
  letter before the rawī is the same on every rhyme word of the chapter's
  luzum bayts — `BadiEngine.chapterOf` walks the peers) and free text gets
  them only under `force`, because «two words that rhyme» is every second
  line of prose. And the luzum's kept letter may not be a madd letter (the
  ridf every rhyme may carry) nor an attached pronoun.
- **The sajʿ mark and the atf chain disagree about one comma.** فِي سِدْرٍ
  مَخْضُودٍ وَطَلْحٍ مَنْضُودٍ وَظِلٍّ مَمْدُودٍ was first authored with `،` after
  each clause, and `_punctAt` — the set the ḍabṭ ladder consults to stop a
  naʿt or a chain at a pause — broke the joined majrūrs into fresh clauses.
  The sajʿ there reads without the marks (the wāw joiners cut it), so the
  marks were removed from the content; where a mark IS needed for the cut
  (وَنَمَارِقُ مَصْفُوفَةٌ، وَزَرَابِيُّ مَبْثُوثَةٌ) it stays, and the hemistich `*`
  is no longer a stop for the ladder at all (the naʿt and the genus-lā
  reach across it). A mark has two readers; author it for both.
- **The nahw the two chapters forced, each paid for by a token.** The
  oath's wāw before إِذَا (وَالنَّجْمِ إِذَا هَوَى: a clause-initial joined
  ال-noun or name followed by إِذَا is majrūr by the qasam — `encOf`, not the
  later-declared `enc`, because the rule stands before the oath rule in the
  ladder); the ishtighāl after ثُمَّ (ثُمَّ الْجَحِيمَ صَلُّوهُ, the amr accepted
  as the verb); the fronted object of an amr and of the prohibition
  (وَرَبَّكَ فَكَبِّرْ، فَأَمَّا الْيَتِيمَ فَلَا تَقْهَرْ — `youV`, the object seat
  free, the verb transitive by its ism mafʿūl or majhūl); the elative at the
  head is a noun (وَأَحْسَنُ السَّجْعِ — `b0` folds the seats, so the test reads
  the hamza off the written word); the plural the lexicon owns WHOLE is a
  diptote (بَلْ فَوَاصِلُ — `diptote()` must not peel a radical ف or و the
  lexicon vouches for); the kāna-shaped noun (وَظِلٍّ مَمْدُودٍ — a row the
  shape guess called a verb, with no cell and no lemma, that the lexicon
  owns and whose marks agree with the noun, is that noun; generalized from
  KANA_FORMS to any `pk === "kana"` row); فَكَبِّرْ re-read as a noun by the
  ladder's kind guess because the lexicon owns بَرّ under a jarr clitic —
  `__verbSure` is stamped by the pre-pass and re-asserted before the
  chains; the demonstrative after إِنَّ is its ism; the fa-peeled cell that
  opens on و; the plural index records `viaPlural`; the naʿt over a jarr
  clitic onto a same-wazn annexed participle (بِاللهِ مُنْتَقِمٍ لِلهِ
  مُرْتَغِبٍ); the passive after a relative takes its second object (مَا
  يُسَمَّى التَّشْطِيرَ); a masdar jawāb noun; the sifa-clause verb's object
  as a bare idafa head (عَلَى سَجْعٍ يُخَالِفُ سَجْعَ الْآخَرِ — the verb owned
  transitive by the lexicon); لِلهِ / لِلَّهِ one jalāla in both modes; the
  māḍī feminine rhyme تْ → تِ.
- **Two wave-21 false alarms the release found before this wave landed.**
  The Qawāʿid ledger raised «jarr with no governor» on بِأَنَّكَ (the ب/ل/ك
  peel refused the inna-family remainder wearing a pronoun — now
  `(ان|أن|إن|لكن|كأن|لعل|ليت)(pronoun)` with a shadda on the nūn peels) and
  on ذَا after a jarr letter (the demonstrative is mabnī, whatever governs
  it). Both are in patch21n; the v175 release was rerun on it.
- **The pins are the wave's own regression set, and one pin was wrong.**
  The pin «سَجْعَ الْآخَرِ annexed» was written on the two-word phrase
  يُخَالِفُ سَجْعَ الْآخَرِ, where a 3ms verb with no earlier subject rightly
  takes the first noun as its doer; the chapter's phrase has the nakira
  before the verb. Write a pin on the sentence the rule was written for,
  never on the fragment that looked like it.

## The jinas by its seat, the close brought back, and the nahw the lafẓī chapters forced (wave 22, v176)

Chapters 68–70 of the Talkhīṣ open the lafẓī badīʿ: the jinas by its
kinds and positions (ch68–69) and radd al-ʿajuz ʿalā al-ṣadr in prose and
verse (ch70). 37 authored badīʿ frames are read back (11 / 12 / 14);
endings-mode ḍabṭ ch68 98.7, ch69 99.4, ch70 95.0 (floors 97 / 98 / 93).
The lessons:

- **The jinas's sub-kinds are positions, and positions are computed.**
  `JinasEngine.read` already aligned the two words; wave 22 reads `kind2`
  off the alignment — the seat of the odd letter (awwal / wasat / akhir),
  the count of added letters (mudhayyal at two and more), the whole or the
  part reversed, the winged qalb at the two ends of the line, the two
  parts of speech (mumathil / mustawfa by the authored pos when the corpus
  has it), the jinas of composition (a two-word span against one word,
  mutashabih when the script is one). The letter-kinds outrank a root
  match (السَّاقُ / الْمَسَاقُ is naqis, not ishtiqaq), vowels-first makes the
  muḥarraf (جُبَّةُ الْبُرْدِ جُنَّةُ الْبَرْدِ), the makhraj groups are the
  book's (ب و / ث ذ ظ / ت د ط / س ز ص / ل ر / ج ش ي / ك ق / خ غ / ح ع ه ء ا),
  and `agree()` accepts the author's mutarraf for the engine's naqis/akhir.
- **Radd al-ʿajuz is read unhinted from the content words.** `RaddEngine`
  takes the last content word and looks for its repeat, its jinas partner
  (from `JinasEngine`) or its derivation earlier in the line; the kind is
  tikrar / jinas / mulhaq by what it found, the seat is estimated from the
  content-word midpoint (sadr-awwal, hashw-awwal, arud, sadr-thani) with
  the neighbouring seats as alternates, and `agree()` accepts the alternate.
  Prose gets `nathr`.
- **A verse sentence needs its hemistich mark.** The grader's rhyme rules
  (the iṭlāq: tanwin dropped, the alif of the nasb tanwin) fire only when a
  token carries `punctAfter: "*"`; the wave-22 bayts were authored without
  it and read as prose until the marks were added. At the rhyme the grader
  now accepts the waqf and the waṣl forms alike (مُغْرَمَا / مُغْرَمًا,
  بِسَرِيعِ / بِسَرِيعٍ) — both are readings of the qāfiya, and the content
  keeps whichever the received text prints.
- **The nahw the three chapters forced** (two dry-run rounds, 22b and 22c;
  ch48–67 checked sentence by sentence): the writer's five verbs of the
  naqis keep the nun's fatha (يَنْهَوْنَ); the ال sound plural in raf writes
  ونَ even when the plural index knows it (الْمُجْرِمُونَ — a pre-existing gap);
  the mabni compounds (ذَلِكُمْ، اللَّهُمَّ، يَوْمَئِذٍ) and يَوْمَئِذٍ annexing nothing;
  وَاللهُ + nakira as a mubtada, not an oath; the genus-lā before a
  jarr-pronoun khabar (وَلَا جَامَ لَنَا); the naming passive's second object
  (سُمِّيَ تَجْنِيسَ الْقَلْبِ); a name the analyzer took for a verb before بْنِ
  (يَحْيَى بْنِ) once the corpus calls it propn; the joined pronoun-bearing
  noun opening a nominal clause after a verb, including after a mubtada's
  own verb (وَدَمْعُهُ سَائِلٌ); لَمْ يَكُنْ إِلَّا X — the mufarragh's إِلَّا keeps kana
  open for its delayed ism and the time noun after the ism is annexed
  (مُعَرَّجُ سَاعَةٍ) but takes no sifa-shaped nakira of its own (قَلِيلًا is the
  khabar); the definition's opening masdar (رَدُّ الْعَجُزِ … هُوَ); «one of»
  annexed to its definite (أَحَدُ اللَّفْظَيْنِ) and «the other» joining «one of
  them» across a jarr phrase (وَالْآخَرُ); the pronoun-bearing item joining
  the annexed head of ITS jarr phrase (أَوْ حَشْوِهِ); the verb after مَتَى
  (وَلِيَ is not و + لِ + ي, and the zarf of question or condition is no doer);
  the fronted khabar's mubtada after إِلَى … يَوْمَئِذٍ (الْمَسَاقُ); the ya of
  «my» on a doubled stem or on the analyzer's «verb» (كِنِّي، جَدِّي) found by
  the glossary when the noun index holds a homograph; the ism mafʿūl
  khabar's deputy doer (مَعْقُودٌ بِنَوَاصِيهَا الْخَيْرُ); the addressee's تَ before
  a masculine human noun (وَتَخْشَى النَّاسَ); wāw + hamza as the joiner
  (وَأَعْدَادِهَا); the فَعِيل head of a three-link nakira chain (شَمِيمِ عَرَارِ
  نَجْدٍ); فُعَلَة and فَوَاعِل as sifa shapes (هُمَزَةٍ لُمَزَةٍ، أَيْدٍ عَوَاصٍ); no naʿt
  across a particle (فَإِنِّي نَافِعٌ); the dual command read off its two
  addressees (دَعَانِي مِنْ مَلَامِكُمَا سَفَاهًا: the alif is the doer, the ني
  the object, the nakira after is the ḥāl, and the fa-joined annexed head
  whose verb follows its chain opens a new sentence); the tanwin's seat
  alif before a final ha (سَفَاهًا is no «her»).
- **Accepted misses, named:** عَوَاصِمِ's kasra is the rawi's (the diptote
  would take a fatha — a poetic licence the grader cannot know without a
  second rhyme word), and the ch48–60 numbers moved only where the wave-22
  rules read a sentence differently on purpose (listed in the release
  notes).

## The cause read by its receipt, the exception by its adat, the question by its shape, the names by their chain — and the figures of meaning shown, not claimed (wave 21, v175)

Chapters 65–67 of the Talkhīṣ finish the maʿnawī badīʿ: ḥusn al-taʿlīl and
tafrīʿ (ch65), the praise confirmed by what looks like blame and its mirror,
istitbāʿ and idmāj (ch66), tawjīh, the jest that means earnest, tajāhul
al-ʿārif, al-qawl bil-mūjib and iṭṭirād (ch67). 23 authored badīʿ frames are
read back (6 / 8 / 9); endings-mode ḍabṭ ch65 96.4, ch66 100, ch67 99.5
(floors 95 / 98 / 98). The lessons:

- **Where the figure is a claim about the world, the engine reads the RECEIPT
  and leaves the claim to the author.** A ḥusn al-taʿlīl is a cause the poet
  invents; no surface says the cause is unreal. What the surface does say is
  what the cause RIDES ON: a negation answered by إِنَّمَا (لَمْ يَحْكِ … وَإِنَّمَا حُمَّتْ),
  the light لَكِنْ after a negation, the unreal لَوْ whose لَ-answer is negated,
  the doubting كَأَنَّ, or a fresh mazi sentence after the quality. `TalilEngine`
  reads those five receipts and the cause-word, the frame gives the kind, the
  card says so in one line — the same contract as the mubalagha's degree and
  the istiʿāra's shortlist. Unhinted free text with a receipt returns nothing
  unless `force` is passed (the lab), because «negation + إِنَّمَا» is everyday
  Arabic, not a figure.
- **The exception is nahw first.** Taʾkīd al-madḥ is an adat of exception
  (إِلَّا أَنَّ, غَيْرَ أَنَّ, بَيْدَ أَنَّ, سِوَى أَنَّ, the لَكِنَّ that stands in for it) with a
  quality before it and a quality after it; a negation before the adat makes
  the first kind, none the second, مَا … إِلَّا أَنْ + verb the third.
  `TakidEngine` reads the adat, the negation and the clause on each side from
  `DabtEngine.decide`'s seats (the first khabar after the citation head; the
  predicate of the adat's أَنَّ with its ism skipped) and gives one frame per
  adat — the Hamadhānī bayt has three. The POLARITY (praise or blame) is
  meaning: with a frame the kind is the frame's; without one a plain إِلَّا is
  refused outright and the rarer adats are offered with «polarity unknown».
- **The knower's question has a shape; its point does not.** `TajahulEngine`
  reads the hamza paired with أَمْ, a bare أَمْ after a mubtada, لَيْتَ, مَا أَدْرِي and
  a question word shadowed by كَأَنَّ; the aim (reproach, hyperbole in praise or
  blame, bewilderment in love) is the frame's. Al-qawl bil-mūjib is read by
  the other's word standing in both halves — the consonantal skeleton
  (`TalilEngine.skel`) makes الْأَعَزُّ and الْعِزَّةُ one word. Iṭṭirād is the only
  wave-21 figure read unhinted: a name, بْنِ, a name, بْنِ, a name is rare enough
  to be sure. Istitbāʿ, idmāj, tawjīh and the jest are DOC frames: shown with
  a note that says the engine reads nothing.
- **The istifhām hamza on a noun is found by the lexicon, not the seg.** In
  endings mode the analyzer does not peel أَلَمْعُ; the pre-pass asks the
  lexicon whether the whole is a word and the rest is (`__hamzaQ`), `hasAl`
  ignores the flag, the chain loop stops treating it as a sifa-shape, the
  ladder makes the hamza'd nakira the fronted khabar (أَقَوْمٌ آلُ حِصْنٍ) and the
  veto keeps it from annexing a definite. One flag, four consumers.
- **The wave-20 entries stored the hollow verbs' short amr stem in the long
  cells.** دُومَا, دُومُوا, دُومِي keep the long vowel; دُمَا does not exist. The
  sarf-audit gate caught it on the second v174 run, the four entries were
  rewritten (`fix21_hollow`) and the authoring calls corrected — the audit's
  regeneration was right, the stored paradigm was wrong, and the gate is
  exactly for that.
- **A plain word that takes the noun index's key over a bracketed manqus must
  keep the manqus reachable.** جَار (ch64's neighbour) silently replaced «جَارٍ
  (الْجَارِي)» and نَهْرٌ جَارٍ became a majrur without a governor for the Qawaid
  gate. `nounIndex` now keeps the displaced entry as an alternate and
  `nounFromCorpus` prefers it when the written word carries the kasratan.
- **The nahw the three chapters forced** (twelve dry-run patches, ch48–64
  unchanged): the doubled passive's she-cell built from the stored he-cell
  (the root walk cannot see two mīms under one shadda); the feminine of a
  manqus written whole; the passive's deputy after a لِ-phrase or after the
  nakira it describes; a mim-participle on لِ that annexes; the citation head
  keeping a name before بْنِ; غَيْرُ + definite as a naʿt; a masdar annexing the
  مَا that opens a verb; the light لَكِنْ keeping the subject; the فَعِيل naʿt
  after a nakira jarr head; an annexed masdar never a maf'ul mutlaq; the
  nasikh under a jarr clitic; مِنَّا / عَنَّا; the clause's own وَلَا after a stop;
  غَيْرَ / بَيْدَ before أَنَّ as the exception's seat; the demonstrative's badal after
  a preposition; the sifa-clause verb keeping its doer even without a stored
  cell; the pronoun's definite khabar; مَا لَكَ as a finished nominal; the bare
  word after لَمْ as a verb; the naqis before its pronoun; وَقَعَ over «and
  fall!»; آلُ before a name; إِخَالُ; أَيَا; كَيْفَ fronting its khabar; the command
  after قُلْ; a word never annexed to itself; the two-object verb's doer after
  its pronoun object and the second object still owed; the writer's وَلِلَّهِ.

## The list figures read off the seats, the tajrid by its letter, the mubalagha as a dial and a receipt, the kalami by its shape — and a learned shortlist graded by chapter (wave 20, v174)

Chapters 61–64 of the Talkhīṣ close the maʿnawī badīʿ: the jamʿ, the tafrīq,
the taqsīm and their three compounds (ch61–62), the tajrīd and its seven ways
(ch63), the accepted mubālagha with its three degrees and four accepted
ghuluww kinds, and the madhhab kalāmī (ch64). 38 authored badīʿ frames
are read back (5 / 14 / 7 / 12 by chapter), the three compounds across sentences too
(`BadiEngine.compoundsOf`), and the FigurePredictor — the first learned thing
that guesses a FIGURE — is graded with every chapter held out in turn:
top-3 26.6%. Endings-mode ḍabṭ: ch61 99.1, ch62 96.0, ch63 98.3,
ch64 98.3 (floors 97 / 94 / 96 / 96). The lessons:

- **The jamʿ, the tafrīq and the taqsīm are nahw before they are badīʿ.** «Many
  things under one ruling» is a wāw-list standing in ONE seat — a mubtada with
  its atf members and one khabar, the ism of إِنَّ, a doer-run behind one verb
  — so section 11 of `BadiEngine.read` is a walk over `DabtEngine.decide`'s
  seats, not a word table: `listFrom(i)` gathers the atf run (skipping each
  member's annex), the ruling is the khabar after it or the verb before it.
  The tafrīq is two constructs sharing a HEAD and differing in the annex
  (نَوَالُ الْغَمَامِ … كَنَوَالِ الْأَمِيرِ) under a negation and a kāf, or two
  mubtadas of that shape each with its khabar; the taqsīm is a list and as
  many pointers, or «jarr-noun + مَا + verb» repeated, or «إِذَا + verb … verb»
  repeated, or «indefinite ṣifa + إِذَا + verb» repeated, or one verb-head over
  three objects. Every one of these is a count of seats; none is a guess about
  meaning. What IS meaning — «is the count exhaustive?» (istīfāʾ) — stays the
  author's sub.
- **A compound across sentences is read across sentences, once, and the
  sentences remember.** The jamʿ-then-taqsīm of al-Mutanabbī and the
  taqsīm-then-jamʿ of Ḥassān live in two bayts each, and Hūd 105–108 in three
  āyas; a frame cannot index another sentence's tokens, so the authored claim
  is `{"kind": "jam-taqsim", "sub": "jam-first", "with": "s5"}` and the reading
  is `compoundsOf(chapter)`: it reads every sentence's single figures in order
  (handing each the previous sentence's frames, so سَجِيَّةٌ تِلْكَ is a SURE
  ishāra-jamʿ only after a taqsīm) and composes; `agree()` on a `with`-frame
  asks the chapter, not the sentence. The gate names the three compounds it
  expects in ch62 by their sentence ids.
- **The degree of a mubālagha is not the engine's to claim.** Whether the
  neighbour's honour «following him wherever he goes» is possible by custom is
  a judgement about the world; the engine shows the three stops as a dial and
  lights the author's, and reads only what the surface carries — the RECEIPT
  of acceptance: كَادَ, the unreal لَوْ with its لَ-answer (ShartEngine's frame),
  حَتَّى opening an إِنَّ clause, يُخَيَّلُ, the jest's tibāq of أَمْس and غَد.
  `MubalaghaEngine` returns nothing on free text that carries no receipt — it
  does not name a mubālagha it cannot show.
- **The kalāmī is a shape, and its shapes are the frames of other engines.**
  لَوْ كَانَ … إِلَّا … لَفَسَدَتَا is ShartEngine's `law` frame with an إِلَّا
  inside the premise and a لَ on the answer; the oath is a verb of swearing
  followed by a negation; the لَئِنْ argument is the wave-20 `__lamJawab` noun
  (the لَ on لَمُبْلِغُكَ is the OATH's, not a jarr letter — the pre-pass sees
  لَئِنْ, then a verb, then a fused-lām noun the lexicon owns, and un-jarrs it);
  the analogy is a clause opened by كَ + a masdar of doing with a pronoun
  (كَفِعْلِكَ).
- **The rhyme is a rule, not a miss.** The Ottoman print writes the rhyme word
  by the iṭlāq — أَحَدُ, كَرِيمُ, مَذْهَبُ, سَخَاءِ, مَاءِ without tanwīn; فَيُغْسَلِ
  and تُخْلَقِ with a kasra on the jussive; بَخِلَا, مَالَا, لَأَمْكَنَا with the
  alif after a verb's fatḥa; and وَقَمِيصًا, غِضَابًا, وَرِدْفًا (ch59–60) keep
  their ًا. So `grade()` marks the rhyme positions (the last token of a
  sentence that carries a hemistich `*`, and a token closed by `؛` inside it)
  and `rhymeForm` rewrites the writer's answer there: ٌ→ُ, ٍ→ِ, a jussive's
  ْ→ِ, a verb's َ→َا, a verb misread as a noun (بَخِلَا) told by its corpus cell
  without the alif. Free text with a `*` ends on a rhyme too. Fourteen misses
  in the probe were this one rule.
- **Two writer bugs that were tables being trusted past their meaning.** The
  sound masculine plural declined by its letters was skipped whenever the
  plural INDEX listed the word — the index exists to catch عُيُون/فُنُون (a
  broken plural in ون that takes tanwīn), and it caught بَنُونَ too (وَالْبَنُونُ):
  the sound plurals the index also lists (بنون، سنون، أهلون، عالمون، أرضون)
  are named past it. And the أَفْعَل diptote test excluded every word ending in
  ل/ب/ن (meant for أَرْنَب) — أَكْذَبُ took a tanwīn; the exclusion is now the
  named nouns (أرنب، أفكل، أثمد، أجدل، أخدع، أنمل، أصبع) or a lexicon gloss that
  is a plain noun, and every elative/colour keeps its bar. A -اء noun is judged
  by SHAPE first (فَعْلَاء, فُعَلَاء, أَفْعِلَاء barred; فَعَال + ء free unless the
  root says otherwise), so عَطَاءً and سَخَاءِ no longer wait on a root the
  lexicon may not have; and a plural the lexicon lists (ذُكْرَان under ذَكَر) is
  never read as a dual.
- **The seat rules the texts forced, each one word long.** `لَا تَكَلَّمُ نَفْسٌ`:
  a ت-verb after لَا followed by a bare FEMININE noun is the negation with that
  noun its doer, not a prohibition; `إِنَّهُ لَتَخَافُكَ`: the lām on a verb after
  إِنَّ is the slid lām of ibtidāʾ — raf, and the writer dresses it لَ (`lamFath`);
  `لَأَرْحَلَنَّ … أَوْ يَمُوتَ`: after a verb built on the heavy nūn, أَوْ hides an
  أَنْ (`awAn`); `لِلسَّبْيِ مَا نَكَحُوا وَالْقَتْلِ مَا وَلَدُوا`: a joined ال-noun that
  opens «مَا + verb» again is joined to the noun that opened that shape before
  it — the parallel clause is an atf across a clause; `عَطَاءً غَيْرَ مَجْذُوذٍ`:
  a bare lexicon-masdar closing a verb clause already closed by its doer is
  the mafʿūl muṭlaq of the verb the sense supplies; `يَكَادُ زَيْتُهَا`, `مَا
  دَامَتِ السَّمَاوَاتُ`: كَادَ and دَامَ join the nawāsikh's trigger lists; and the
  delayed mubtada after a fronted shibh-jumla may be a فَعِيل NOUN (زَفِيرٌ,
  صَدِيقٌ) when the lexicon says noun and not adjective — the shape is not the
  last word.
- **The regression round is the method, and it found the engine reading copies.**
  The wave-20 rules were written in twelve numbered patches against a DRY
  reader (the package copied under the scratchpad, `build_prototype --packages`
  with the copy, every patch a script that asserts its anchors), each probed on
  ch61–64 and then swept over ch48–60 and every other story against the
  shipped reader — a per-sentence diff, not a floor. The sweep caught what the
  new chapters could not: the `jarrClit` test that took بِرِّكَ for a clitic on
  رِّك (a pronoun alone proves no clitic — the rest must be a headword); the
  ladder rule that gave a jarr clitic its case BEFORE the citation rule and so
  silenced كَقَوْلِهِ's clause (it now serves بِ and لِ only, after the
  citations); the dual test that stopped at a sun letter's shadda (الطَّرَفَانِ)
  and at the maqṣūr's alif (مَعْنَيَانِ); the masdar-over-mazi rule that took
  قَتَلَ for قَتْل (the lemma's own marks must match); and the seat alif on a
  participle (مُرِيدًا إِنْسَانًا) that is a ḥāl whose object follows. And the
  deepest one: `BadiEngine.read`, `TajridEngine`, `SajEngine` and `RuleMiner`
  decided the seats on COPIES of the rows, so the pre-pass corrections
  (تَكَلَّمُ turned into the she-verb, دَارُ into a noun, أَرَاكَ into a verb)
  never reached the figure rules — the copies are kept now, and the figure
  rules read them. Vetoes on the annexation chain (a chain's members all point
  at its ROOT: undoing one link makes the next word the root of the rest) undo
  what the seats forbid — ذِي as a naʿt, a dual keeping its nūn, آخَرُ, a
  demonstrative after a sentence-initial nakira, a participle plural after a
  nakira, the passive's owed deputy, a stop between two words, a zarf with its
  pronoun, a jarr clitic.
- **A learned figure-guesser is graded the only honest way: by chapter.** The
  FigurePredictor is one-vs-rest logistic regression over 43 features the
  engines already compute (`FigurePredictor.feats` lives in the page; the
  trainer's table is dumped BY the page through Playwright, so there is one
  feature function, never a copy), trained on the 64 framed sentences and
  192 without a figure, and its floor is the leave-one-chapter-out top-3
  rate — a chapter's figures are one author's one afternoon, and a split by
  sentence would leak the afternoon into the test. It is a 🧠 shortlist above
  the engine's frames in the Badiʿ lab and a third card in the Learning lab;
  the frames stay the claim.
- **Key hygiene, again: a key is a global claim, and the check runs before the
  write.** `ahwal` already meant أَحْوَال (the plural as lemma), `inath` إِنَاث,
  `sadiq` صَدِيق in the Talkhīṣ but صَادِق elsewhere, `kaff` the masdar not the
  hand, `khalid` the name not the participle, `amma` الْعَامَّة in one package and
  أَمَّا in ours — so the scripts build `GLOSS_ADD` through `need()` (nothing
  the package already owns is re-asserted) and reuse by `find_gloss` for what
  another package owns with the same word; the collisions were caught by `G()`'s
  assertion at dry-run, in a package COPY under the scratchpad with the
  validator run against it, before a byte of the repo moved. And a verb copied
  in from another package brings its paradigm with it — the release gate wants
  every glossary verb conjugated (`adkhala`, `azama`, `baqiya`, `khafa`,
  `shaqiya`, `takallama` arrived bare).
- **The source has slips of the press, and the manifest says so.** حرشنة for
  خَرْشَنَة, ولارض for وَالْأَرْضُ — printed here in their known form and named in
  the attribution; al-Nābigha's three bayts are given by the source in Turkish
  only, so their Arabic is RESTORED (the received text the Talkhīṣ cites) and
  marked as such, sentence by sentence.
- **The harness's 3-second boot wait is a load gauge.** One check in the v173
  release run failed on `waitForSelector('.lib-card', 3000)` — the page boots
  in under a second on an idle box, but a full-corpus check before it had left
  Chromium at 90 % — and passed alone. With v173 every appearance wait is 10 s, a failed check returns the page to the library, and `SMOKE_READER` points the suite at a dry reader for triage — the second v173 run had lost four checks to the 3-second waits at load average 1.1, two of them cascades from one slow boot.
- **A wave's patches are bisected against the previous release before the
  release runs again.** v174's first release run showed four engine
  regressions that no wave-20 probe had watched (the bare shart seed, ch45,
  a ch47 tashbih frame, a ch51 majaz frame). Rebuilding the v173 reader with
  the repo content and applying the seventeen wave-20 patches one by one
  (`$SCR/bisect20.sh`, then the exact failing smoke bodies replayed on each
  variant) named the four culprits in one pass: the آخر veto (F5) fired on
  آخِرِ «last», the mawsul guard (L1) swallowed مَنْ of the shart, the
  ثُمَّ/أَوْ-joins-the-khabar rule (F9) pulled the third member of a jarr chain
  up to the khabar, and a jarr-clitic test (P1) that took كُلِّهِ for ك + لّ + ه
  vetoed بِاسْمِ كُلِّهِ — which let the TashbihEngine assert a likening on
  كَالْأَصَابِعِ. Each fix keeps the marks in view: the veto asks for آخَر's
  fatha, the clitic test asks the lexicon for the host whole. The hollow amr
  stems (دُومَا, مِيلُوا) and the twin-nun seams (تَضَمَّنَّ) are stored the way the
  SarfEngine regenerates them; `put_morph` never overwrites, so a paradigm
  fix is a fix to the stored file, not a re-run. A `SMOKE_ONLY` subset run
  on the patched reader then caught what the probes had not watched: the
  Qawaid audit alarming on a jarr letter the analyzer left on its noun
  (بِبَاءِ), and the bare-masdar rule taking a chain member (فَسَادُ جَعْلِ) — a
  false likening the ch47 gate had reported only after its first failure
  was fixed. A gate that throws on its first finding hides its second. The full run
  then found the last one: the manqus twin (جَارٍ beside جَار) must be preferred
  only over a key whose own word is no manqus — رَاضٍ keeps the glossary's
  entry with its root.

## Al-Kāfiya opens: an Ottoman notebook becomes the second nahw text, and its definitions become rules (wave 25, v179)

`content/samples/al-kafiya` (L5 Advanced, premium; regenerators
`tools/authoring/author_kafiya_ch1.py`, `author_kafiya_ch2.py` over the shared
`kafiya_common.py`, which re-points `talkhis_common` at the package) carries Ibn
al-Ḥājib's matn from the notebook `research/sources/kafiya-ibn-hajib-sual-cevap.txt`
— Ziya Sungur-oğlu's Ottoman-script lesson book, whose ARABIC is vowelled and
exact under every Turkish معناسى gloss (the third Ottoman file on the shelf to
prove the rule: never write a file off for its script). Chapter 1: the kalima
and its two divisions, lafẓ / waḍʿ / maʿnā, the kalām and the isnād, the
two-word minimum with the quoted كَزَيْدٌ قَائِمٌ, the five non-kalām compounds,
the three definitions, the noun's marks (19 sentences, 199 tokens). Chapter 2:
the muʿrab and the mabnī, the iʿrāb and its three signs, the ʿāmil, and the six
declension classes proved on the notebook's own triplet جَاءَنِي / رَأَيْتُ /
مَرَرْتُ بِـ (21 sentences, 183 tokens). Two notes carry the doctrine with Molla
Jāmī's questions as their question test (`al-kalima-wal-kalam`,
`al-murab-wal-mabni-wal-irab`). Endings-mode ḍabṭ at v179: ch1 100.0 (191),
ch2 100.0 (163) — floors 98 / 96; both bayts of ʿAlī scan (basīṭ, wāfir).

**Mark what is whose, sentence by sentence.** The notebook mixes the matn, the
teacher's worked examples and Molla Jāmī's answers on one page. A sentence the
notebook gives only in Turkish is RESTORED from the received matn and marked in
both translations; a worked example (فَزَيْدٌ فِي ضَرَبَ زَيْدٌ مُعْرَبٌ) or an
etymology (the كَلْم of the wound) is COMMENTARY and marked as such; the manifest
attribution lists which sentences are which. ʿAlī's two bayts are printed as
the notebook prints them (ضَيِّقَةٌ feminine by sense, يَلْتَامُ with its hamza
softened) and the iʿrāb says so rather than correcting the page.

**A text about grammar is a test-bench for the grammar engine.** Every
definitional sentence of the Kāfiya forced a rule the Talkhīṣ had never needed,
and each is a receipt, not a guess (patch25a / 25b, gated by the wave-25 seeds):
- **The author's ending is evidence the tagger threw away.** أُطْلِقَ / أُحِسَّ were
  read as the 1sg muḍāriʿ (cell 12); a fatḥa ending is the passive māḍī. سَمُّ was
  the amr of سَمَّى; an imperative never wears a ḍamma. وَجَرٌّ was the māḍī جَرَّ;
  no verb wears tanwīn. أَحْمَدَ was the 1sg of حَمِدَ; the lexicon owns it as a
  name. Each rule reads `DabtEngine._orig24` — the author's own token — and
  stands down where the ending says nothing.
- **A tanwīn word annexes nothing.** رَفْعٌ وَنَصْبٌ وَجَرٌّ had been chained as an
  idafa by bare letters; the prePairs filter and the ladder drop every head whose
  author's token ends in tanwīn.
- **The quoted sentence after the kaf and after فِي.** كَزَيْدٌ قَائِمٌ keeps its
  ḍamma (the whole sentence sits in the place of jarr), كَقَامَ زَيْدٌ keeps its
  verb, فِي ضَرَبَ زَيْدٌ keeps its verb though the analyzer had demoted it after a
  jarr letter (`__vcell` restores it; the corpus is asked for a bare māḍī), and
  the definite noun after the quotation is the delayed mubtada (فَفِي جَاءَنِي
  زَيْدٌ الْعَامِلُ جَاءَ).
- **The letter-names are nouns.** لَامِ التَّعْرِيفِ was the verb لَامَ; a letter
  name before a definite annex is a noun and annexes to it.
- **The mulḥaq forms are written as the author wrote them.** أَحَدَ عَشَرَ,
  سِيبَوَيْهِ, اثْنَانِ / الِاثْنَيْنِ, أُولُو (read as the amr of آلَ) keep their letter;
  a kept row is now written from the author's token, not from the stripped text
  (the writer's «keep» had been printing الِاثْنَان and كِلَيْهُمَا), and كِلَيْهِمَا
  after a kept mulḥaq is its tawkīd.
- **The passive in a person the package does not store is rebuilt from the
  he-form** (تُرْفَعُ، يُرْفَعَانِ، تُجَرُّ — the she-prefix, the dual and the plural
  offered to the corpus as candidates) — stored-only remains the doctrine for
  the FORM; the person is derivable and derived.
- **The we-doer.** اتَّبَعْنَا / عَمِلْنَا were «he followed us»: a māḍī closing on
  ـْنَا (the sukūn before the نَا) carries the first-plural cell.
- **Seats the definitions forced:** the ordinal resuming after أَوْ لَا
  (وَالثَّانِي الْحَرْفُ) or after its sibling's khabar; the mirrored clause
  (وَالنَّصْبُ عَلَمُ الْمَفْعُولِيَّةِ repeats فَالرَّفْعُ عَلَمُ الْفَاعِلِيَّةِ — a joined
  definite noun before a repeated khabar resumes the frame with its annex);
  الْأَزْمِنَةِ الثَّلَاثَةِ (a definite cardinal is its noun's naʿt); غَيْرِ مُقْتَرِنٍ
  across فِي نَفْسِهِ (غَيْر + participle after a nakira's jarr chain is that
  nakira's naʿt); زَيْدٍ الْعَالِمِ (a proper name is never annexed to the definite
  adjective after it); السَّالِمُ after جَمْعُ الْمُؤَنَّثِ (the naʿt of جَمْع, not of its
  annex); مُضَافَةً إِلَى after the mubtada (a fathatan nakira before a jarr letter
  with the khabar still owed is the ḥāl); وَكَوْنُهُ مُسْنَدًا and وَأَخَوَاتُهَا joined
  to the clause's mubtada; نَحْوُ: at the head as the khabar of a dropped mubtada
  annexed to the quoted sentence; وَلَا يَلْتَامُ (after لَا a lexicon-less word
  with a muḍāriʿ prefix and a final ḍamma is the verb, not the genus-lā's ism).

**The design piece is the Kāfiya's own test-bench drawn** (DESIGN.md §24): a
sentence carrying one noun in three case-forms grows a `.bd-triplet` card in the
iʿrāb sheet — the case off the stored line, the sign off the word's ending
(`caseSignOf`), vowel-class or letter-class off `IrabSign.of`, the letter classes
dashed. `IrabSign.of` names its manner `huruf`, not `letters`; the five nouns show
their letter only once the pronoun is peeled (أَبُوهُ reads a ḍamma otherwise), and
the jarr clitic must come off before the engine is asked (بِأَبِيهِ). Gated on a phone.

**Three things the wave taught about the tooling.**
- **`process.env` does not exist inside `page.evaluate`.** The probes had been
  "generalised" to a `STORY` env in wave 24 by reading `process.env.STORY` inside
  the browser callback — a ReferenceError the moment the default was not taken.
  Inject the value into the page once (`window.__STORY`) and read that.
- **The ladder's early rules exist twice.** Lines 14648–14655 are repeated
  inside the noun branch (~15069–15076); an anchor on any of them matches twice.
  The true ladder top is the `const bw = bareOf(r), cw = coreOf(r);` line, and the
  wave-24 `__zarfKull24` anchor is NOT the top — it sits after the idafa rules,
  which is why the first cut of the propn-naʿt rule never saw its row.
- **The maqṣūr writer ate the shadda.** `writeNoun`'s `[ً-ٰ]+ى$` strip includes
  U+0651, so الْمُثَنَّى was written الْمُثَنَى; the shadda is kept and the fatḥa
  is re-added before it (NFC order), for the definite and the tanwīn case both.
- **Free text carries its own stops.** `grade()` fed the ladder `_colonAt` and
  `_punctAt` from the tokens' `punctAfter`; `vowel()` on typed text had neither,
  so «ثَلَاثَةٌ: رَفْعٌ وَنَصْبٌ وَجَرٌّ» lost its list frame in the lab. `vowel()` now
  reads the colon and the pauses off the typed text when no grade supplied
  them, keeps the sets it made in `_own25`, and retires them at the END of the
  call — never at the next one: the first cut left them standing, and the
  ch47/ch48 tashbih gates (which call `decide()` directly, not through
  `vowel()`) read the seeds gate's colon at index 3 as their own. And the
  author's tokens (`_orig24`) are stored without their trailing stops, or every
  ending test on the last word of a clause fails on the comma.
- **The author's token is evidence only where it is THIS row's.** A rule that
  reads `_orig24[i]` inherits every place the analyzer's rows and the whitespace
  tokens disagree; مَجْذُوذٍ became a ḥāl because the fathatan it "wore" was
  عَطَاءً's, one token back. Every reader of the author's token now checks the
  bare letters first and stands down on a mismatch.
- **A new lexicon entry is a predator — fourth payment.** The needle's eye سَمّ
  (ch1's bayt) let the speaker's-ya rule (22c) re-read سُمِّيَ as «my سَمّ», and
  nine sentences of the jinās chapters lost their naming passive. The rule now
  stands down on a whole stored cell matched mark for mark; the sweep of
  ch48–76 against the v178 baseline is what found it.
- **The amr's iltiqāʾ kasra is no evidence.** «An imperative never ends in a
  kasra» took اُدْخُلِ الْبَيْتَ out of the drill garden within the hour — the kasra
  is the meeting of two sākins before the article. The receipt rule keeps the
  ḍamma and the tanwīn only.
- **The name annexed keeps its head's naʿt.** كِتَابَ زَيْدٍ الْجَدِيدَ describes the
  book; the propn-naʿt rule (زَيْدٍ الْعَالِمِ) stands down when the name is a
  muḍāf ilayh. The seeded full-mode decision caught it.
- **A nūn-final lām needs the `idgham` wrapper — fifth payment.** اقْتَرَنَ
  shipped as اِقْتَرَنْنَ / اِقْتَرَنْنَا and the Sarf regeneration gate blocked the
  first v179 run on it (the audit contracts the sākin twin; the stored cell
  did not). `put_morph` never overwrites, so the script pops the stale key
  before it stores the contracted one.
- **A cell that IS the written word must win across the WHOLE corpus, not
  only inside its own paradigm.** The release's sarf-corrector gate samples
  every ninth stored cell, and al-Kāfiya's paradigms shifted the sample onto
  fifteen Talkhīṣ cells the corrector "corrected" — all latent on v178:
  تَقْرِنَّ (qarana's 2fp) was handed to قَرَى's تَقْرِينَ, because the heavy-nūn
  restoration (kasra → ينَ) offered a candidate that matched قَرَى EXACTLY and
  قَرَى walks first; اِقْرِنِي lost to اِقْرِ through the ني peel, وَعَدَا to دَعَا
  through the joining-clitic strip, سَبَقُوا to بَقُوا through the future sīn,
  شَبَّهَا to شَبَّتَا through the pronoun peel. `findFormInParadigm` already
  ranked the whole surface first — per paradigm; `_fromCorpusWalk` now walks
  the corpus four times (the word whole, the word behind a joining clitic,
  candidate-exact, loose), so no derived candidate anywhere outranks the word
  itself anywhere (patch25d). And the sixteenth was DATA: the Talkhīṣ copy of
  سَاقَ stored the short amr stem in the vowel-initial cells (سُقِي for سُوقِي —
  the hollow-amr rule this file already states), invisible to the paradigm
  audit because the corpus index keeps the FIRST paradigm per key and the
  Manār copy is right. A sampled gate is a gate that moves when the corpus
  grows; `$SCR/sweep_musahhih.js` runs the corrector over every stored cell.
- **A `grep -c` that finds nothing is exit 1, and everything after `&&` is
  skipped — silently.** Two rounds of patch edits never ran because the Python
  that made them stood behind a diagnostic grep; the rebuilt reader then
  measured the OLD rules and the failures looked unexplained. Diagnostics go in
  their own command; an edit script prints what it did, and the rebuild greps
  for the edit's own comment before any probe is trusted.


## Qiṣaṣ al-Nabiyyīn is a story now, and the Level-1 reader's frames are rules (wave 26b–26e, v181)

`content/samples/qisas-al-nabiyyin-1` (L1 Newbie, premium, **five chapters, 171
sentences, 1,090 tokens**; regenerators `tools/authoring/author_qisas_ch1.py` …
`author_qisas_ch5.py` over the shared `qisas_common.py`) carries the opening of
Nadwī's «مَنْ كَسَرَ الْأَصْنَامَ؟» from the user's scans, transcribed page by page
(`$SCR/pdf26/qisas1_matn.txt`, vol. 1 complete): the idol seller, Ibrāhīm breaks
the idols, the cold fire and «my Lord is Allah», the call and the king, the call
to the father, the road to Mecca and the well of Zamzam. **Nadwī died in 1999 and
the text is in copyright**: the manifest attribution carries the RIGHTS/HAKLAR
notice in both languages and the smoke gate reads it off disk; the user directed
the story be authored regardless. Every Qurʾanic line the print sets (26:71–74,
26:78–81, 21:59–63, 21:68–69, 6:78, 2:258, 19:42/44/47) is marked with
`quoteBefore`/`quoteAfter` and the `al-iqtibas-wal-tadmin` tag, and the gate
checks the ids. The note `la-nafiya` (nahw, level 1) with its question test is
anchored in the story. Endings-mode ḍabṭ at v181: **ch1 100.0 (186), ch2 100.0
(206), ch3 100.0 (235), ch4 100.0 (191), ch5 100.0 (240)** — floors 98/97/96/96/93;
47 seed sentences rebuilt ending for ending; the whole volume as free text
(4,480 endings, lexicon-blind) 84.5 → **90.4**.

**A Level-1 text is the hardest test the ḍabṭ engine has met.** The Talkhīṣ
settles most seats by definition frames and lexicon; a children's narrative is
all verbs, names, pronouns and joined clauses, and every ambiguity the books
list is live in it. The two patches (`patch26d`, `patch26e` — eighteen numbered
rounds, each probed on the chapter it was for and re-graded on every earlier
chapter and on the seeds before the next) are the record. The rules, each paid
for by a named token:

- **The inherited doer.** A joined transitive māḍī inherits the doer the clause
  already named (غَضِبَ إِبْرَاهِيمُ وَأَخَذَ الْفَأْسَ) — guarded by person, by the
  lexicon's transitivity (`majhulMazi`/`ismMaful`, compared in NFC: the shadda's
  order had hidden every Form-II verb from the rule for seven rounds), by the
  INTRANS gloss, by a colon or a pause, and by the SAME-LEMMA test that bends
  only where the first verb took an object (وَغَضِبَ قَوْمُهُ وَغَضِبَ الْمَلِكُ names new
  doers; نَصَرَ اللهُ هَاجَرَ وَنَصَرَ إِسْمَاعِيلَ keeps its doer). A NAME is the object
  only where the first verb took an object or its doer stands right before the
  joined verb (فَغَضِبَ الْمَلِكُ وَطَلَبَ إِبْرَاهِيمَ) — never the jalāla, never after
  a saying verb, never past a pause (وَخَرَجَ الْمَاءُ … وَشَرِبَ إِسْمَاعِيلُ).
- **The an-chain.** After أَرَادَ (or any verb whose doer is named or hidden) the
  an-verb's doer is that doer; a verb from the PERSON_OBJ table takes the plain
  noun after it, or the noun behind a returning jarr-pronoun (وَيَعْبُدَ فِيهِ اللهَ
  وَيَدْعُوَ النَّاسَ); the joined an-verbs keep the chain through `st.anHidden30`;
  أَنْ يَفْهَمَ الْمَلِكُ keeps its doer because فَهِمَ is in no table; أَنْ يَبْعُدَ
  مِنْهُ يُوسُفُ keeps its doer because a returning pronoun + a noun is a seat, and
  the one-letter `fused()` test had to be widened to مِنْهُ/فِيهَا/عَلَيْهِ before
  the rule could see it.
- **The speaker and the addressee.** A 1st/2nd-person tāʾ māḍī is written only
  when the line resolves it: أَنَا/نَحْنُ or the speaker's نِي — including the
  TRIMMED wiqāya nūn read off the author's token (وَإِذَا مَرِضْتُ فَهُوَ يَشْفِينِ) —
  against أَنْتَ/the vocative/a question particle opening the line (هَلْ شَرِبْتَ).
  Unresolved stays `none`: a guess here is a wrong person half the time.
- **The five verbs' nūn is not dropped when an object pronoun hides it**
  (هَلْ يَسْمَعُونَكُمْ is no jawāb al-ṭalab): `nunDropped` reads the HOST.
- **The exception follows the object it excepts from** (لَا يَخَافُ أَحَدًا إِلَّا
  اللهَ — badal, nasb), the mirror of R13's mufarragh doer.
- **A frozen adverb is transparent to the atf** (مَلِكٌ كَبِيرٌ جِدًّا، وَظَالِمٌ) and
  never itself a maʿṭūf (وَكَذٰلِكَ); a clause-opening كَذٰلِكَ fronts the khabar
  (وَكَذٰلِكَ كُلُّ مُشْرِكٍ); a wa-joined fused ẓarf opens a nominal clause
  (وَمَعَهُ زَوْجُهُ هَاجَرُ) and the name after a pronoun-bearing noun is its badal.
- **The twins the surface cannot split are split by the context's receipts:**
  the amr-dual cell of another paradigm that spells this verb's 3ms māḍī reads
  as the māḍī with no addressee in the line (وَدَعَا is never «you two, leave!»);
  the token behind ONE joining letter matched mark for mark outranks a cell of
  another lemma (وَوَصَلَ is وَ + وَصَلَ, never وَ + وَ + صَلِّ); a whole stored cell is
  never split into host and pronoun (وَيَتَحَرَّكَ keeps its kāf); no pronoun clings
  to a tanwīn word (مُشْرِكٍ); the analyzer's wāw-peel before a false article is
  undone where the lexicon owns the wāw-initial noun (وَالِدَهُ was وَ + الد + ه —
  and `joined()` believed the segments); a wa-joined «māḍī + pronoun» after a
  pronoun-bearing noun is the noun (زَوْجَهُ هَاجَرَ وَوَلَدَهُ إِسْمَاعِيلَ) and keeps
  its joiner in the segments or `joined()` cannot see it; the fused ب/ل/ك peel
  loses to a whole stored verb cell (كَسَرَ is no كَ + سِرّ) — on the analyzer's
  FLAG, not its segment list, which the heuristic peel leaves at one.
- **فَكَانَ after a clause with its doer** conceals its ism and stamps the next
  noun as its khabar outright (بَقِيَ الْمَاءُ فَكَانَ بِئْرَ زَمْزَمَ) — the kāna state
  was reset by the row's own pre-pass twice and reopened by the analyzer's
  «ism of kāna expected» note once; the stamp is what survived, and the stamped
  khabar annexes the name after it (no tanwīn on a muḍāf).
- **The relative is a wall for the subject** (الصِّلَةُ سُورٌ: الَّتِي يَشْرَبُ مِنْهَا
  النَّاسُ — the mubtada before the relative owns nothing inside the ṣila, and
  «the doer stands right before the verb» excludes every relative, not only مَا);
  a returning jarr-pronoun after the ṣila's verb carries the ʿāʾid, so the
  definite noun after it is the doer whatever the verb's valency.
- **The foreign names are diptotes whatever the lexicon knows** —
  `AJAM_NAMES26` grew إِسْمَاعِيل، مَكَّة، زَمْزَم، إِسْحَاق، يَعْقُوب، يُوسُف … and now
  feeds `propn()` too, so free text with no lexicon entry still reads a name as
  a name; the writer keeps the author's dress where only a dagger alif differs
  (لِلّٰهِ) and the fatḥa the author put on the speaker's yāʾ (رَبِّيَ).
- **Quotation marks are no letters**: the author's tokens lose «» before any
  ending test, or every last word of a quoted line fails on the ».

Three things the wave taught about the tooling. **The ladder's early rules exist
twice** (recorded in wave 25) — a rep that must hit the delayed-ism rule needs
`count=2`, and the one that hits `joined()` needs `count=1`; a wrong count crashes
the patch chain and the next build silently measures the previous round. **A
rule's guard must be instrumented, not reasoned about:** six rounds were spent
on وَوَدَّعَ وَالِدَهُ before a one-line trace (`DabtEngine._trace.push({...every
operand})`) showed `plainObj(nx)` false because the analyzer had segmented the
object as a wāw + a false article; the same trace found the NFC lemma mismatch,
the `fused()` one-letter blindness and the kāna reset in one afternoon. And
**the saying verb's colon belongs to the doer** — `qala()` defaults to a colon
and ch2/ch3 had shipped «قَالَ: إِبْرَاهِيمُ:» for a hundred commits; the regex fix
runs over every author script and the JSON audit is in the chapter-4 run.

**The seam-idghām wrapper, sixth payment — and the release gate is what pays it.** سَكَتَ
(a tāʾ-final lām meeting the doer's تَ) and the hollow أَهَانَ (a nūn-final lām meeting
the women's نَ and the نَا) were authored through `sound1`/`derived_hollow` bare,
shipped سَكَتْتَ and أَهَنْنَ, and the Sarf regeneration gate blocked the first v181 run
on them. Every maker whose lām is ت، ن or د goes through `_sg.idgham(...)`, and
`put_morph` never overwrites, so the stale keys are popped before the script
re-runs. The release is the only reader of the whole corpus's paradigms; the
chapter probes never see a cell the text does not use.

**Key hygiene, again:** `hajar` already meant حَجَر (ch2's stone), `adaa` أَدَاء,
`safa` صَفَاء, `mushriq` «shining» not مَشْرِق — the global check caught all four
at authoring time; the names are `hajar-name`, `adaa-lose`, `safa-q`, `mashriq`.

**What the release found after the measured gates were green — three full-mode
regressions and one seed, each a wave-26 rule reaching one word too far (rounds
19–20).** The chapter probes grade in ENDINGS mode; the release also rebuilds the
drill garden from BARE letters, and there the author's written marks are evidence
the rules may read. (1) The mufarragh exception (لَنْ يَدْخُلَ الْجَنَّةَ إِلَّا مَنْ) had
no negation in its guard — it was unreachable only because the name after إِلَّا
used to read as a verb; the moment the wave's propn rules made زَيْدًا a noun,
جَاءَ الطُّلَّابُ إِلَّا زَيْدًا became «the students were the object». The classical
condition is the guard now (`negBefore33`: a nafy, a nahy, لَيْسَ or a question
before the verb), and in full mode a written ḍamma on the noun refuses the object
reading outright (`writtenRaf33`). (2) Round 15 excluded every relative from «the
doer stands right before the verb» for الَّتِي يَشْرَبُ مِنْهَا النَّاسُ — and took
مَنْ يَطْلُبِ الْعِلْمَ with it, where the ʿāʾid inside يَطْلُبِ IS the doer and الْعِلْمَ
the object. The exclusion is now the SHAPE that needed it: a returning
jarr-pronoun and a plain noun after the verb; مَا keeps the wave-20 reading.
(3) Round 1 turned the vocative annexed to the speaker's yāʾ into a `keep` (يَا
أَبِي — the five-noun host must not take the nasb alif), and the keep writer
composed lemma + bare yāʾ in full mode: مُعَلِّمي. The muḍāf's kasra before the
yāʾ is written on the host now. (4) The sixth idghām payment had a rider: once
أَهَانَ's women's nūn contracted (تُهِنَّ), its bare letters equalled the singular
jussive تُهِنْ, and the cell walk handed وَلَا تُهِنْ the 2fp cell. The يَكُنْ / يَكُنَّ
rule (under a jazim the matching majzum cell is the cell) now covers the 2fp and
reads the string-valued `majzum` / `majzum2` fields the packages actually store —
its first cut assumed an array and silently did nothing. Meta-rule, paid for the
fourth time this wave: a rule's new reach is measured on the NEIGHBOURS before the
release, in full mode as well as endings mode, and a writer fix is probed on the
seed it was written for before the two-hour run.

**Round 21 — a glossary that grows flips a rule that asks it, fifth payment.**
Release run 3 blocked on a Talkhīṣ bayt the wave never touched: كَقَوْلِ
الْمُتَنَبِّي … لَوْ تَبْتَغِي عَنَقًا عَلَيْهِ لَأَمْكَنَا lost its mubālagha frame because
لَأَمْكَنَا stopped being a verb. The bisect over the twenty rounds found NONE
of them guilty — the unpatched v180 shell fails on the current content too. The
Qiṣaṣ brought أُمّ into the lexicon; the marked-text rescue asks the lexicon
whether the host owns the word, and «لَأَمْكَ» now answered أُمّ + كَ («your
mother»). That hit did not match the host, so the rule neither returned nor
tried the whole stored cell — the verb path lived in the `else` of a lookup
that was never meant to be a verdict. A lexicon hit obtained only through a
pronoun strip owns nothing; the whole-word corpus walk now runs before the row
is left a noun. Two lessons on top of the standing one: bisect against the
UNPATCHED shell first (one build answers «is it the engine or the content?»),
and when a chapter's glossary enters the corpus, the sentences that can flip
are everywhere else — the release is the only sweep that sees them.

**Round 22 — the widened fall-through reached one word too far, within the hour.**
Run 4 blocked on ch51's فَلْيَدْعُ نَادِيَهُ: round 21's whole-word walk read the
manqūṣ in nasb with its pronoun as the 2fs amr نَادِي with an object — the exact
reading the wave-16 madd-letter guard exists to refuse. Two guards now: a manqūṣ
lemma (kasratan) equals the host with its restored yāʾ dropped, and that IS
ownership; and the mismatch path takes a māḍī/muḍāriʿ cell only, never over a
host whose last letter is a vowelled madd letter. The pattern is the one this
file keeps recording — a widened frame ships WITH its control — and the cheap
countermeasure is now in the loop: after a round that fixes a release finding,
the failing CHUNK is rerun standalone on the landed reader before the two-hour
run, so the next regression costs ten minutes.

**Round 23 — the standalone chunk found two pins in ten minutes, and each was a
Level-1 rule wearing a wave-22/24 sentence.** The subject's walk back over
لا/ما/قد (round 3) crossed فَقَدْ, and بُشْرَى became the concealed doer of
أَنْجَزَ — the fāʾ opens the jawāb's clause and the walk stops at it. The wa-fused
ẓarf rule (وَمَعَهُ زَوْجُهُ, round 12) matched the VERB وَلِيَ by its bare letters
(وَ + لِي) and seated أَحَدُ as a mubtada — a row with a verb cell is never that
ẓarf; and the first guard written for it («the previous row is a particle»)
took the Qiṣaṣ sentence away within the minute, because مَعَ is a ẓarf and
the analyzer rightly calls it a NOUN (a peel is not a classification — the
v-ch4 lesson, read from the other side). The one-joiner rule (round 10,
وَوَصَلَ) swallowed وَعَدَا — its own cell وَعَدَ's dual already spelt the whole
token, and a cell that spells the whole token outranks the token behind the
joiner. Bisecting by ROUND (truncate the patch file before a marker, rebuild,
probe) named all three in two passes of five builds; the bisect script stays
in the scratchpad as the method.

## Qiṣaṣ chapters 6–7, and the two rounds the dream and the Kaʿba forced (wave 26g–26i, v182)

`qisas-al-nabiyyin-1` runs to **seven chapters, 217 sentences, 1,455 tokens**:
chapter 6 «رُؤْيَا إِبْرَاهِيمَ» (§14, print pp. 21–23 — the return to Mecca, the
dream, al-Ṣāffāt 37:102 as the print sets it in two marked lines, Minā, the ram,
the Feast of Sacrifice; `author_qisas_ch6.py`) and chapter 7 «الْكَعْبَةُ وَبَيْتُ
الْمَقْدِسِ» (§15–16, pp. 23–26 — the building of the Kaʿba with al-Baqara 2:127,
the Muslims' turning and pilgrimage, Sārah and Isḥāq, al-Shām and Bayt
al-Maqdis, Yaʿqūb's twelve sons and the hand-over to Yūsuf's story;
`author_qisas_ch7.py`). Endings-mode ḍabṭ at v182: **ch6 97.3 (150), ch7
100.0 (200)** — floors 95 / 97; ch1–5 held at 100.0, the 47 seeds at 267/267,
the drill garden's full re-vowelling at 96.3. The two chapters cost two
engine rounds (`patch26g`, round 24; `patch26h` + `patch26i`, round 25), and
every rule is a Level-1 frame the Talkhīṣ never needed:

- **A maqṣūr NAME whose lexicon lemma carries the tanwīn is munṣarif.** The
  writer treated every name on an alif as a diptote (مُوسَى، عِيسَى) and wrote
  مِنى; the lexicon's own مِنًى is the receipt of ṣarf, and `diptote()` stands
  down on it.
- **The elative after a verb's DEFINITE object is the elative** (يُحِبُّ اللهَ
  أَكْثَرَ): a bare māḍī there could only be the object's naʿt or its ḥāl, a
  definite takes no naʿt clause and a māḍī ḥāl needs قَدْ — the tenth demotion
  guard, and the first that reads the clause rather than the word or its
  neighbour.
- **ابن wearing a pronoun right after a verb is the son** (يُحِبُّ ابْنَهُ) — an
  imperative is never a verb's object, and «build it!» would need a colon.
- **A verb matched WHOLE with its object pronoun is stamped with the pronoun it
  wears** (بَنَاهُ ~ بَنَى + هُ, found through the maqṣūra-to-alif candidate): the
  doer seat stays open, the name after it is the doer, and the cell writer
  splits the host from the pronoun before writing. Two accidents sat on the
  way: the lexicon's clitic strip read بَنَاهُ as بِ + نَاهٍ («a forbidder») and
  told `guessEnc` the word was owned whole — a stamped pronoun now outranks
  that strip; and the verb branch had already handed the name to the object
  seat, so the doer rule runs BEFORE the object stamp is read.
- **The relative's ʿāʾid may ride the ẓarf AFTER the noun** (الَّذِي بَارَكَ اللهُ
  حَوْلَهُ): the subject-before-the-verb rule stands down for «relative + verb +
  plain noun + returning pronoun» — on a noun or a fused particle, never on a
  verb, or مَنْ يَطْلُبِ الْعِلْمَ يَجِدْهُ loses its doer (the drill garden said so
  within the hour).
- **The ism fiʿl family takes its object** (وَإِلَيْكَ هٰذِهِ الْقِصَّةَ): إِلَيْكَ،
  عَلَيْكَ، دُونَكَ، هَاكَ at the clause head make the next noun manṣūb, and a
  demonstrative's badal follows the demonstrative's maḥall.
- **رَبَّنَا before a plea verb is the vocative with its يَا dropped** (رَبَّنَا
  تَقَبَّلْ مِنَّا) — the amr after it is the receipt; a mubtada has no imperative
  for a khabar.
- **اسْمُهُ / اسْمُهَا after a nakira opens its ṣifa clause** (زَوْجٌ أُخْرَى، اسْمُهَا
  سَارَةُ؛ وَلَدٌ اسْمُهُ يَعْقُوبُ): mubtada, and the name after it the khabar — the
  nakira may stand up to four rows back, across a pause or a jarr phrase.
- **A name takes no plain-noun naʿt** (وَنَقَلَ إِبْرَاهِيمُ وَإِسْمَاعِيلُ الْحِجَارَةَ):
  the ال-noun after a named or joined doer, while the verb owes its object, is
  the object.
- **The foreign names under a jarr clitic** (لِإِسْحٰقَ — the print's dagger alif,
  which no lexicon lemma spells): `propn()` and `diptote()` fold the clitic
  before the names table, so the fatḥa of jarr and kāna's fronted khabar both
  survive a spelling the lexicon has never seen.
- **The compound number** (لَهُ اثْنَا عَشَرَ وَلَدًا): اثْنَا carries no pronoun —
  its نا is the stem's, and `guessEnc` had read «our two» — it is the delayed
  mubtada after the fused pronoun and writes by its LETTER (اثْنَا / اثْنَيْ,
  اثْنَتَا / اثْنَتَيْ); عَشَرَ keeps its bina.
- **A fused pronoun after a pause opens a nominal clause** (…، مِنْهُمْ يُوسُفُ
  بْنُ يَعْقُوبَ) exactly as the wāw-fused one did (وَمَعَهُ زَوْجُهُ).
- **وَكَانَ + a lone nakira closing the sentence** after a clause with its
  subject conceals its ism (اسْمُهُ يَعْقُوبُ وَكَانَ نَبِيًّا) — the فَكَانَ rule's
  wāw sibling, narrowed to the sentence's last word.
- **The tanwīn-word atf rule (P13) stands down on a lexicon-owned wāw-initial
  word** (وَلَدٌ after لِإِبْرَاهِيمَ is kāna's delayed ism, never joined to the
  majrūr) — the «clitic hides the feature» trap read from the other side: a
  wāw the lexicon owns is not a joiner.

**Accepted misses, named.** ch6 s2 (وَلَقِيَ إِسْمَاعِيلَ وَلَقِيَ هَاجَرَ — a
sentence-initial verb whose doer is the previous sentence's) and s15 (وَهَلْ
يُحِبُّ اللهَ أَكْثَرَ — a question joined onto the previous sentence's subject):
both readings need the sentence before, which the grader does not hold. The
chapter floor sits under them rather than on a rule that would guess.

**Two things the wave taught about the loop.** The chapter probe grades in
endings mode and the drill garden in FULL mode — the first cut of the ʿāʾid rule
passed every chapter and took a drill sentence; the neighbour sweep
(`build26t.sh`-style: chapters, seeds, the ch61–64 and ch51–57 gates, the drill,
`sarfAudit`) runs after EVERY round now, in the background, before the next
round is written. And a rule inserted «early in the ladder» is only early
relative to the rules after it: the verb branch's object stamp (`__obj26`) is
read at the top of the ladder, so a doer rule that must beat it goes before
that line, not before the frame it was written beside — bisect by trace, not
by reasoning (`DabtEngine._trace.push({...every operand})` named the stamp in
one run).

## Qiṣaṣ chapter 8 — Yūsuf's dream, and the three rounds the children's narrative forced (wave 26j–26l, v183)

`qisas-al-nabiyyin-1` runs to **eight chapters, 247 sentences, 1,707 tokens**:
chapter 8 «رُؤْيَا عَجِيبَةٌ وَحَسَدُ الْإِخْوَةِ» (§1–2 of «أَحْسَنُ الْقَصَصِ», print
pp. 27–30 — the boy Yūsuf, the dream with Yūsuf 12:4 as the print sets it,
Yaʿqūb's reading and his warning, Binyāmīn, the brothers' envy, their council
and the well; `author_qisas_ch8.py`). Endings-mode ḍabṭ at v183: **ch8 100.0
(256)** — floor 97; ch1–7 held, the 47 seeds at 267/267. Three engine rounds
(`patch26j`, round 26; `patch26k`, round 26 continued; `patch26l`, round 27),
and each rule is a Level-1 frame:

- **A `const` declared inside the ladder is unreachable from the rule above
  it.** `transOf` was declared ~90 lines below its first use; the first
  sentence to reach that use (أَبُونَا يُوسُفَ — a pronoun-bearing five-noun
  before a name) threw `ReferenceError` in the TDZ and the whole sentence
  came back undecided. A helper the ladder's early rules read is hoisted
  beside `encOf`, at the ladder's head (`patch26j`). When a probe prints
  nothing for a sentence, run it unfiltered first — the error was in the
  log the filter dropped.
- **فَهِمَ is not فَ + هِمْ.** The pre-pass read the verb as a fāʾ with the
  plural pronoun; the kasra on the hāʾ is the receipt — no pronoun هِمْ rides
  a fāʾ with a kasra — and the corpus owns the cell.
- **The compound number is the object** (رَأَى أَحَدَ عَشَرَ كَوْكَبًا): both
  halves mabnī on the fatḥa, the verb's doer concealed, the counted noun its
  tamyīz.
- **كُلّ / بَعْض before a muḍāriʿ opens the nominal clause** (كُلٌّ يَسْجُدُ لَهُ)
  — never after inna's family.
- **The elative before مِنْ right after a verb is the absolute object's
  deputy** (يُحِبُّهُ أَكْثَرَ مِنْ جَمِيعِ إِخْوَتِهِ) — and the rule accepts the
  analyzer's Form-IV reading of the word (أَكْثَرَ as the māḍī), because R11's
  clause-head khabar reaches the same word first otherwise.
- **وَكَانَ + [لَا|مَا] + a third-person muḍāriʿ after a clause with its subject
  conceals kāna's ism, and the muḍāriʿ does the ism's act** (وَكَانَ يَعْرِفُ
  طَبَائِعَ النَّاسِ، وَكَانَ لَا يُحِبُّ مِثْلَهُمَا أَحَدًا). Two traps paid: the
  first cut lived in the KANA_FORMS branch, which وَكَانَ never enters (it has
  a cell; the forms the table LACKS go there) — the rule belongs in the verbs
  branch where the word actually arrives; and the analyzer's own «kāna's ism
  expected» note re-opened kāna on the verb row itself, through the notes
  regex at the head of that block — the stamped verb is exempt. The
  «clause with its subject» test reads every seat decided so far
  (fail/kanaIsm/mubtada/innaIsm), not the live state, because a verb clause
  as kāna's khabar has already spent it.
- **The you-frame stands down for an intransitive verb and for a plural the
  corpus knows** (كَيْفَ تَسْجُدُ الْكَوَاكِبُ): a broken plural agrees with the
  she-verb — it is the doer, not the object of «you prostrate». `INTRANS`
  learned prostrate/bow/kneel/laugh/weep/cry/sleep/walk/swim/fly.
- **A joined māḍī inherits a doer only in its own person** (سَمِعُوا الرُّؤْيَا
  وَاشْتَدَّ حَسَدُهُمْ): a 3ms verb cannot share the group's wāw, so the pronoun-
  bearing noun after it is its own doer.
- **The name after a pronoun-bearing doer of a transitive verb that still
  owes its object is the object** (يُحِبُّ أَبُونَا يُوسُفَ) — the LATE badal rule
  («the name after a pronoun-bearing noun is its badal») needed the same
  guard the early one got in 26k; the early rule had already stood down and
  the late one was the one firing. The set()-tracing debug reader
  (`probe26_set.js`: every `set()` records its source line) named the rule in
  one run, where reading the ladder had named the wrong one twice.
- **The engine's geminate amr is the jazm bil-fatḥ** (اِشْتَدَّ, with the fakk
  only before the women's nūn: اِشْتَدِدْنَ) — the audit's message is
  `engine≠stored`, and the first fix read it backwards.

**Accepted misses, named.** None in chapter 8. The two from chapter 6 (s2,
s15 — readings that need the sentence before) stand.

**What the release found: a ceiling that follows the corpus.** The JamEngine
audit counts the stored plurals the qiyāsī builder cannot rebuild, and the
gate holds a ceiling just above the last measurement; chapter 8's heard
plurals (شُبَّان، أَقْوِيَاء، طَبَائِع، أَذْكِيَاء) took it from 151 to 161 and the
first v183 run blocked on it. The ceiling moves with the corpus by design
(v178 said so) — raise it to the measurement, name the chapter, and rerun the
resumable release from the blocked chunk.

## Qiṣaṣ chapter 9 — the delegation and the forest, and the round the quoted speech forced (wave 26m, v184)

`qisas-al-nabiyyin-1` runs to **nine chapters, 280 sentences, 1,964 tokens**:
chapter 9 «وَفْدٌ إِلَى يَعْقُوبَ، وَإِلَى الْغَابَةِ» (§3–4 of «أَحْسَنُ الْقَصَصِ», print
pp. 30–34 — the brothers' plea, Yūsuf 12:12 and 12:13 as the print sets them,
the leave, the forest and the well, the glad tidings in the well, the council,
the ram and the dyed shirt; `author_qisas_ch9.py`). Endings-mode ḍabṭ at v184:
**ch9 100.0 (257)** — floor 97; ch1–8 held; sarfAudit clean. The chapter cost
one round (`patch26m`, round 28), four rules, every one a receipt in the quoted
speech:

- **The jawāb al-ṭalab stamp knew only the word the analyzer took for a
  NOUN.** Round 24m read the author's sukūn after an amr to turn a noun-read
  word into the jussive (اقْتَرِحْ شَيْئًا نُجِدْ); يَرْتَعْ was already a verb to
  the analyzer, so no stamp fell and the writer gave it raf'. The stamp now
  reads the sukūn on a verb the analyzer owns too (third person, within three
  rows of the amr, no jazim or nāṣib between) — أَرْسِلْهُ مَعَنَا غَدًا يَرْتَعْ
  وَيَلْعَبْ, the second verb by the copied mood.
- **The prohibiting لَا may stand after a saying verb's colon** (وَقَالَ لَهُ: لَا
  تَحْزَنْ وَلَا تَخَفْ). The nahy test asked for the sentence head or a joiner;
  the colon IS a clause head. The hollow تَخَفْ had passed on its letters
  alone — the sound تَحْزَنْ needed the rule.
- **The naṣb of أَنْ stops at the an-clause's named doer** before a FIRST-PERSON
  joined verb (أَخَافُ أَنْ يَأْكُلَهُ الذِّئْبُ فَنَقُولُ لَهُ): the copied mood reached
  four rows across the wolf, and «we» cannot be the wolf's co-ordinate.
- **A mubtada needs its khabar** (آيَةُ ذٰلِكَ الدَّمُ): the ال-noun closing the
  sentence after a demonstrative annexed to the clause's mubtada is the
  khabar, not the demonstrative's badal — the rule that reads اسْمُ هٰذَا
  الرَّجُلِ stands down on the sentence's last word.

**Key hygiene:** `sadaqa` already meant صَدَقَة, `ghaba` the verb غَابَ, `wahid`
وَاحِد (and وَحِيد in one upload — a standing collision); the chapter's keys are
`sadaqa-verb`, `ghaba-forest`, `wahid-alone`. A note id that does not exist
(`lam-ibtida`, `hamzated-verbs`) is a validator error, not a silent gap — the
slid lām and the hamzated verbs still have no note of their own.

## Qiṣaṣ chapter 10 — before Yaʿqūb, Yūsuf in the well, and the round the ayas forced (wave 26n, v185)

`qisas-al-nabiyyin-1` runs to **ten chapters, 300 sentences, 2,107 tokens**:
chapter 10 «أَمَامَ يَعْقُوبَ، وَيُوسُفُ فِي الْبِئْرِ» (§5–6 of «أَحْسَنُ الْقَصَصِ», print
pp. 34–36 — the brothers before Yaʿqūb with Yūsuf 12:16, 12:17 and the opening
of 12:18 as the print sets them, the whole shirt, «فَصَبْرٌ جَمِيلٌ», Yūsuf in the
well at night; `author_qisas_ch10.py`). Endings-mode ḍabṭ at v185: **ch10
100.0 (143)** — floor 97; ch1–9 held; sarfAudit clean. One round
(`patch26n`, round 29), six rules, each a receipt:

- **One word, two hamza seats.** The print writes جَاؤُوا and the paradigm
  stores جَاءُوا; the stored cell was unreachable and the analyzer read the
  verb as a noun wearing the group's wāw — every seat of the sentence then
  fell. The candidate builder offers ءُوا for ؤُوا, matching only, exactly as
  the madda unfolds — and the fold must run AGAIN over the candidates the
  later passes build (the joiner-stripped جَاؤُوا), or the joined form stays
  blind. A spelling equivalence added early in a candidate list is only as
  good as its reach over the candidates added after it.
- **The five noun under its pronoun is the noun by table** (أَبَاهُمْ) even
  where a verb cell spells the same letters (أَبَى + هُمْ, found through the
  maqṣūra-to-alif candidate) — the pre-pass decides it before the whole-match
  stamp can call the father an object pronoun of «he refused».
- **The joined «māḍī + pronoun» that reads as the lexicon's noun rides a
  wāw only** (وَوَلَدَهُ), and never before an ال-noun that would be its doer:
  فَأَكَلَهُ الذِّئْبُ is a verb and the wolf its doer, not «and its food».
- **The jawāb of إِذَا carries the shart verb's concealed doer** (إِذَا أَكَلَ
  إِنْسَانًا جَرَحَهُ), and a verb joined onto that jawāb inherits the same
  concealed doer though the jawāb wears its object (وَشَقَّ قَمِيصَهُ) — the
  inherited-hidden rule had refused every verb wearing a pronoun. Two
  blindnesses sat underneath: `joined()` refused every three-letter word
  (وَشَقَّ — the geminate's third radical is the shadda), and the «وَوَصَلَ»
  rule that re-cells a joined verb was dropping the joiner from its segments.
- **بَقِيَ before «noun + muḍāriʿ» is ظَلَّ's sister** (بَقِيَ يَعْقُوبُ يَذْكُرُ
  يُوسُفَ): the ism, the muḍāriʿ as khabar with the ism's act, the name after it
  the object — the full verb بَقِيَ الْمَاءُ keeps its doer.
- **An intransitive verb owes no object**: the bare nakira after a nakira
  majrūr is its naʿt (جَاؤُوا … بِدَمٍ كَذِبٍ) — the lexicon's maṣdar-noun كَذِب
  has no sifa shape to show, so the verb's valency is the receipt.

**Key hygiene:** `isha` already meant عِيشَة and `mata` مَتَى — the chapter's keys
are `isha-evening` and `mata-goods`; the إِذَا note is `idha-shartiyya`.

## Qiṣaṣ chapter 11 — from the well to the palace, and the round the narrative's full stops forced (wave 26o, v186)

`qisas-al-nabiyyin-1` runs to **eleven chapters, 328 sentences, 2,282 tokens**:
chapter 11 «مِنَ الْبِئْرِ إِلَى الْقَصْرِ، وَالْوَفَاءُ وَالْأَمَانَةُ» (§7–8 of «أَحْسَنُ
الْقَصَصِ», print pp. 36–38 — the caravan and the bucket with Yūsuf 12:19 as the
print sets it, the market of Egypt and the ʿAzīz, the wife's attempt and
Yūsuf's refusal, the ʿAzīz's verdict (12:29), the city's wonder (12:31),
«السِّجْنُ أَحَبُّ إِلَيَّ» (12:33) and the prison; `author_qisas_ch11.py`).
Endings-mode ḍabṭ at v186: **ch11 100.0 (175)** — floor 97; ch1–10 held (ch6's
two accepted misses stand); the 47 seeds 267/267; the r21/r22 gates and the
drill garden unchanged; sarfAudit clean. One round in five cuts (`patch26o`
… `patch26o5`, round 30), and the rule that paid for most of it is new in kind:

- **The narrative carries its subject across the full stop.** Every earlier
  chapter accepted a miss where a sentence opened on a verb whose doer stood
  in the sentence before (ch6 s2). The grader now hands `decide()` the subject
  it found one sentence back — in reading order only, keyed on the chapter's
  own sentence objects, cleared the moment the grade returns — and a sentence
  opening on a joined 3rd-person transitive verb with ONE plain noun after it
  reads that noun as the object (وَنَزَعَ الدَّلْوَ). Four neighbour sweeps drew
  the rule's edges, each a receipt: the carried subject is the LAST named doer
  (خَلِيلُهُ, not اللهَ) and only a name or an ال-noun (اسْمُهُ carries nothing);
  it stands down for an intransitive verb (وَرَجَعَ الْإِخْوَةُ — INTRANS learned
  dwell/settle/reside/rest for سَكَنَ), before an object clause (فَعَرَفَ يَعْقُوبُ
  أَنَّهُ) or a colon, where a later verb's person is dual or plural (وَتَرَكُوا),
  where the one noun is the jalāla (فَبَارَكَ اللهُ), and where it is a name
  while the carried subject is not; joined nouns form one unit (وَنَقَلَ
  إِبْرَاهِيمُ وَإِسْمَاعِيلُ الْحِجَارَةَ keeps its two doers); إِذَا after the noun opens
  a clause, not an object. The chain propagates through joined verbs, over
  أَوْ / ثُمَّ and into a muḍāriʿ after a muḍāriʿ — and an intransitive joined
  verb before a plain definite noun names its own doer, whether it would have
  inherited a hidden one or a named one (وَلَقِيَ هَاجَرَ وَفَرِحَ إِبْرَاهِيمُ).
- **The madda is also hamza + alif** (رَآهُ = رَأَى + هُ): a matching-only unfold
  beside the madda's two hamzas, and the whole-match stamp folds it the same
  way — the first cut unfolded the word and left the comparison blind.
- **The endings strip keeps a pronoun's vowel on a verb host the restore
  rules can reach** (وَأَخْفَوْهُ → أَخْفَوْا; رَآهُ → رَأَى): a bare ه after the strip
  reaches no cell, and the whole sentence after it fell. And the writer keeps
  the group's wāw's sukūn before the pronoun that took the alif's place.
- **A stored plural is owned whole** — no pronoun hides in its tail (بِدَرَاهِمَ is
  never دَرَى + هُمْ: the أَبَاهُمْ trap with a lexicon plural); a diptote under its
  jarr clitic is still a diptote; and the naʿt after a nakira majrūr reads the
  jarr clitic by its kasra where the analyzer left it unpeeled, also when the
  verb's object is already taken and the two agree (a broken plural takes the
  feminine singular: بِدَرَاهِمَ مَعْدُودَةٍ).
- **The bare speaker's yāʾ on a noun the lexicon owns without it is the
  pronoun** (سَيِّدِي) — the analyzer had peeled a false future sīn.
- **إِذَنْ in the middle of the speech is cancelled** (مُلْغَاة): it governs only
  at the head of its sentence — the print's إِذَنْ تَذْهَبُ after قَالَتْ لِيُوسُفَ
  keeps its raf', and the rule says why.
- **The elative after a mubtada, before its مِنْ / إِلَى, is the khabar**, never
  the Form-IV māḍī (السِّجْنُ أَحَبُّ إِلَيَّ).
- **The «indefinite head after a transitive verb is the doer» cut stands down
  for the nouns of relation** (امْرَأَةُ الْعَزِيزِ، زَوْجُ الْمَلِكِ) and wherever a third
  plain definite noun follows to be the object (رَاوَدَتِ امْرَأَةُ الْعَزِيزِ يُوسُفَ) —
  the cut was written for جَوَّزَ قَوْمٌ الِاعْتِرَاضَ, where nothing follows.

Two content slips the engine caught: the aya's مِنَ الْخَاطِئِينَ had been typed
with a sukūn, and أَدْلَى had been authored with no passive — so the inherited
doer could not see it was transitive. **Key hygiene:** `idhan` already meant
إِذًا, `baad` بَعْض in the Maqṣūd (the adverb is `bada`), `man-istifham` was
already the package's own; the note ids the first draft guessed (ma-al-hijaziyya,
in-nafiya, idha-fujaiyya, anwa-al-jawab, nun-al-wiqaya, ya-nida) do not
exist — the validator said so, and the tokens anchor anwa-ma, qasr,
idha-shartiyya, an-masdariyya, ya-al-mutakallim and vocative-munada instead.

**What the release found: the plural ceiling again, and a timing gate that
reads the machine.** The JamEngine audit rose to 167 with chapter 11's heard
plurals (أُمَنَاء، بُرَآء، دِلَاء) and blocked the run at the v183 ceiling of 165;
the gate now sits at 175 and names the chapter. And the held-out cross-
validation timing check (4.5 s ceiling) failed once at 6.9 s — not the corpus
but the load: two probe browsers were sweeping chapter 12 beside the release.
Rerun alone it passed. **A timing gate measures the machine as much as the
code; never run a probe beside the release's smoke chunks.**

## Qiṣaṣ chapter 12 — the sermon of the prison, and the round the she-verb forced (wave 26p, v187)

`qisas-al-nabiyyin-1` runs to **twelve chapters, 354 sentences, 2,453 tokens**:
chapter 12 «مَوْعِظَةُ السِّجْنِ» (§9 of «أَحْسَنُ الْقَصَصِ», print pp. 38–41 — Yūsuf in
the prison, loved and honoured; the two men and their dreams with Yūsuf 12:36
in the print's two lines; the people of his time and their invented lords; the
sermon's four questions; the two «but he was» sentences; the prophets proclaim
the truth; `author_qisas_ch12.py`). Endings-mode ḍabṭ at v187: **ch12 100.0
(171)** — floor 97; ch1–11 held; the Talkhīṣ khātima and sajʿ chapters (71–76)
unchanged; the 47 seeds 267/267; sarfAudit clean. One round in four cuts
(`patch26p` … `patch26p4`, round 31):

- **The tanwīn's seat alif is read on a stored PLURAL too.** `alifSeat` compared
  the written word against the lexicon's lemma only, so أَرْبَابًا (رَبّ's plural
  owns it) was not a seat, and the head annexed the sifa after it (أَرْبَابًا
  كَثِيرَةً). The plural field is a lemma for this purpose — hamza seats folded.
- **The question hamza over a sister of kāna** (أَلَيْسَ أَهْلُ السِّجْنِ عِبَادَ اللهِ):
  the kāna block's form test strips the hamza, and the pre-pass hands the row
  لَيْسَ's frozen cell by hand — the jamid verb has no walkable paradigm, so the
  corpus walk returns nothing for it and the writer had no ending to keep.
- **A she-verb with no feminine in its clause takes the ال-noun after it as its
  doer** (إِنِّي أَرَانِي أَحْمِلُ فَوْقَ رَأْسِي خُبْزًا تَأْكُلُ الطَّيْرُ مِنْهُ). Three rules
  had claimed the collective as an object: «the subject named earlier owns the
  verb after it» (the subject is «I»), «no she-verb takes a masculine doer — the
  ta is you» (a first-person speech with no addressee anywhere in the line has
  no «you»), and the sifa-clause presumption. Each now reads the gender of what
  it would have made the doer; the collective's gloss (bird(s)) counts as a
  plural. And the guard reads the PREVIOUS verb's person — by the time it runs
  the row's own person is already «she», which is what the first cut compared.

**Key hygiene:** `jari` already meant جَارٍ (the Talkhīṣ manqūṣ) — the bold man is
`jari-bold`; `alim` in this package is عَلِيم, so the learned man is the standing
`alim-scholar`; the geminate note is `doubled-verbs`, not the guessed
`geminate-verbs`.

## Qiṣaṣ chapters 13–19 — from Yūsuf's wisdom to Binyāmīn at Yūsuf's side, and round 32 (wave 26q, v188)

`qisas-al-nabiyyin-1` runs to **nineteen chapters, 523 sentences, 3,814 tokens**:
seven chapters landed in one wave, §10–20 of «أَحْسَنُ الْقَصَصِ» (print pp. 41–59) —
ch13 «حِكْمَةُ يُوسُفَ، وَمَوْعِظَةُ التَّوْحِيدِ» (§10–11; the two men's dreams interpreted,
the sermon of tawḥīd with Yūsuf 12:37–40, 35:40, 31:11), ch14 «تَأْوِيلُ الرُّؤْيَا،
وَرُؤْيَا الْمَلِكِ» (§12–13; 12:41–42, the king's seven cows and seven ears),
ch15 «الْمَلِكُ يُرْسِلُ إِلَى يُوسُفَ، وَيُوسُفُ عَلَى خَزَائِنِ الْأَرْضِ» (§14–16; 12:54–55),
ch16 «جَاءَ إِخْوَةُ يُوسُفَ» (§17; 12:58), ch17 «بَيْنَ يُوسُفَ وَإِخْوَتِهِ» (§18; 12:59),
ch18 «بَيْنَ يَعْقُوبَ وَأَبْنَائِهِ» (§19; 12:63–67), ch19 «بِنْيَامِينُ عِنْدَ يُوسُفَ» (§20;
12:69, 12:73–75, 12:77 unmarked as the print sets it, 12:78–79) — regenerators
`author_qisas_ch13.py` … `author_qisas_ch19.py`, +160 glossary entries, +53
paradigms. Endings-mode ḍabṭ at v188: **ch13 100.0 (224), ch14 96.6 (177),
ch15 98.3 (294), ch16 100.0 (164), ch17 100.0 (121), ch18 100.0 (114),
ch19 97.8 (267)** — floors 97 where the chapter reaches it, else the named
misses below; ch1–12 held; Talkhīṣ 71–76 unchanged; the 47 seeds 267/267;
sarfAudit clean. One round in seven cuts (`patch26q` … `patch26q7`, round 32),
the probe-first way: 120/169 sentences clean on the v187 engine, then
138, 149, 156 and 158/169 after the cuts. The rules the seven chapters forced:

- **The dual māḍī behind a lām or fā** (لَسَمِعَا، فَفَرِحَا): the ladder's seat-alif
  test took the lexicon's lemma for the word minus its alif; now the WRITTEN
  vowels must agree with that lemma (فَرِحَ ≠ فَرَح), and a fā-joined dual at the
  head before a joined verb is the verb.
- **The zarf before أَنْ/مَا/إِذَا is annexed to its clause** (قَبْلَ أَنْ يَأْتِيَ — no
  tanwīn); the zarf never annexes an ordinal ṣifa (مَرَّةً ثَانِيَةً); كُلَّ يَوْمٍ after a
  verb is a zarf; مَعَاذَ اللهِ is the mafʿūl muṭlaq.
- **Title heads annex the name after them** (مَلِكُ مِصْرَ، رَسُولُ الْمَلِكِ، مَكَانَ
  يُوسُفَ): the «verb + nakira + definite» object cut stands down for them, for a
  chain member (تَأْوِيلِ رُؤْيَا الْمَلِكِ), and the number test stands down after an
  always-muḍāf head (كُلَّ أَحَدٍ).
- **The saying verb never takes a plain object** (وَقَالَ الْمَلِكُ is the doer); the
  joined transitive māḍī's object is the name after it even across a jarr
  phrase when the verb takes persons (وَسَأَلَ يُوسُفَ); a noun that repeats the
  clause's doer, or that أَنَّ follows, is the doer again (وَعَلِمَ الْمَلِكُ وَعَلِمَ
  النَّاسُ أَنَّ); the an-chain's name after a transitive verb is the object (أَنْ
  يَذْكُرَ يُوسُفَ، أَنْ يَحْبِسَ بِنْيَامِينَ) and an intransitive one with a zarf names its
  doer after it (أَنْ يَبْقَى عِنْدَهُ بِنْيَامِينُ); a doer-less muḍāriʿ opens the chain
  too (يُمْكِنُ لِيُوسُفَ أَنْ).
- **The she-verb after a masculine subject** (وَأَمَّا الْآخَرُ فَيُصْلَبُ فَتَأْكُلُ
  الطَّيْرُ) takes the ال-noun after it as its doer when nothing feminine stands
  before it.
- **Kāna:** after إِنَّ's ism كَانَ conceals its ism (إِنَّ يُوسُفَ كَانَ كَبِيرَ النَّفْسِ); a
  wa-joined noun after a jarr phrase is the maʿṭūf, not the ism (وَكَانَ فِي مِصْرَ
  وَالشَّامِ مَجَاعَةٌ); the fronted khabar — kāna, a zarf or jarr phrase, then the
  nakira ism — leaves the ṣifa after the ism as its naʿt (وَيَكُونُ بَعْدَ ذٰلِكَ
  قَحْطٌ عَامٌّ); the subject scan steps over kāna's khabar so the ism owns the
  verb after it (كَانَ يُوسُفُ جَوَادًا كَرِيمًا لَا يَعْرِفُ الْبُخْلَ).
- **Sarf and the writer:** أَسْمَاء and the أَفْعَال plurals with a hamza lām are
  munṣarif (only أَشْيَاء is barred); سِنِينَ declines by its letters at four letters;
  the plural of a diptote colour declines (خُضْرٍ — the gloss's «diptote» belongs
  to the lemma); وَبِنْيَامِينُ is no sound plural behind its wāw; الْأَخَوَانِ is the
  five noun's dual on its wāw; إِخْوَان is not أَخَوَان (the lexicon's plural owns a
  word only when the written vowels agree); أَبًا شَيْخًا annexes nothing; the
  jawāb al-ṭalab in the first person, with a hamza or with its pronoun (نَأْخُذْ،
  أَسْتَخْلِصْهُ); وَتَوَجَّهَ and وَضَعَ at the head are the māḍī (the twin amr needs
  an addressee); لَا تَجِدُونَ keeps its nūn, so لَا is the nafy; وَكَلَّمَهُمْ goes back to
  its cell when a jarr-letter peel left a verb with its pronoun; أَمِينَا in the
  endings mode is no «our mother».
- **Chains and pauses:** no annexation crosses a pause (بِشَيْءٍ، النَّائِمُ); a
  wa-joined name after a pause with a nakira participle opens a ḥāl clause
  (، وَبِنْيَامِينُ رَاجِعٌ غَدًا); the ṣifa-shaped head annexes a demonstrative
  (صَاحِبُ هٰذَا التَّأْوِيلِ); the pair-before-their-verb reading stands down when the
  noun before is a badal of the same shape and the verb is singular
  (هٰذَا التَّأْوِيلَ وَالتَّدْبِيرَ فَرِحَ); مَنْ after the saying verb's colon opens the
  question; the mufarragh (لَا يَنْفَعُ النَّاسَ … إِلَّا مَنْ) takes its object before
  إِلَّا and its doer after; the name-object across a jarr phrase is for the
  verbs of address only (وَسَأَلَ يُوسُفَ — never وَشَرِبَ إِسْمَاعِيلُ, which the
  neighbour sweep caught in ch5); the tafṣīl badal keeps its ṣifa-shaped items after a
  colon and the kāna-ism guard stops at a pause (the release smoke caught
  Talkhīṣ ch48 s3/s4 — cut 7); the carried doer stands down for the name
  after a dative pronoun only — a plain name after the carried verb is its
  object (وَلَقِيَ إِسْمَاعِيلَ, ch6 in the same sweep); the plural ṣifa agrees with its ات-head (بَقَرَاتٍ
  سِمَانٍ، سُنْبُلَاتٍ يَابِسَاتٍ); the counted phrase after a perception verb and a jarr
  phrase is the object (رَأَى فِي الْمَنَامِ سَبْعَ بَقَرَاتٍ); the demonstrative's badal is
  the object when a number doer follows (وَيَأْكُلُ هٰذِهِ الْبَقَرَاتِ سَبْعُ بَقَرَاتٍ);
  a name after «nakira + لَهُ» is that nakira's badal (سَرَقَ أَخٌ لَهُ يُوسُفُ); the
  shart's doer is not inherited by a jawāb whose nakira has its own clause;
  لِأَيِّ شَيْءٍ declines and annexes (a question, no shart); كَيْفَ opens no shart;
  بِاللهِ after a verb is the verb's own jarr phrase (نُشْرِكَ بِاللهِ); زَمَنٍ طَوِيلٍ
  keeps its ṣifa with the majrūr that agrees with it; فَهُوَ جَزَاؤُهُ is the
  pronoun's khabar, not the passive's second object.

**Accepted misses (named, not floors):** ch14 s9 رَأَى فِي الْمَنَامِ سَبْعَ بَقَرَاتٍ (the counted object after a perception verb and a jarr phrase still reads as the doer); ch14 s13 هٰذَا لَيْسَ بِشَيْءٍ، النَّائِمُ يَرَى أَشْيَاءَ كَثِيرَةً (a pre-pass annexation crosses the pause — four tokens); ch14 s15 تَأْوِيلِ رُؤْيَا الْمَلِكِ (the chain stops after رُؤْيَا); ch15 s4 وَاشْتَاقَ الْمَلِكُ (the doer carried from s3 takes the repeated name as the object) and أَسْتَخْلِصْهُ (the jawāb al-ṭalab with its pronoun); ch15 s8 كَانَ أَحَدٌ مَكَانَ يُوسُفَ (the place noun before a name after kāna's ism); ch15 s22 لَا يَنْفَعُ النَّاسَ بِخَزَائِنِ الْأَرْضِ إِلَّا مَنْ (the mufarragh over a clitic-jarr noun); ch15 s31 أَمِينًا (read as «our mother» through the construct); ch19 s8 يُمْكِنُ (the majzūm twin wins the cell); ch19 s12 وَضَعَ هٰذَا الْإِنَاءَ (the demonstrative's badal after the doer-less verb reads as the doer); ch19 s14 صُوَاعَ إِنَاءَ الْمَلِكِ … وَلِمَنْ جَاءَ بِهِ حِمْلُ بَعِيرٍ (the bracketed badal and the delayed mubtada — three tokens); ch19 s21 أَبًا شَيْخًا (the bare five noun annexes the ṣifa-shaped nakira). Eleven sentences, twenty-two tokens of 1,361; ch14's floor is set at 96 for them, the other six chapters hold 97.

**Key hygiene:** `hasada` is حَسَدَ (envy) — the reaping verb is `hasada-harvest`
(حَصَدَ, bāb نَصَرَ); `jaa` is جَاءَ (the hunger is `jaa-hunger`), `dai` is دَاعٍ (the
lost one `dai-lost`), `hafiz` is حَافِظ (`hafiz-keeper` for حَفِيظ), `sab` is صَعْب
(`sab-seven`), `salaba` is سَلَبَ (`salaba-crucify`), `zaman` is زَمَان (`zaman-period`
for زَمَن), `adhana` is آذَنَ (`adhdhana` for أَذَّنَ), `rahim` is the name
(`rahim-merciful`).

## Qiṣaṣ chapters 20–23 — the end of volume 1, and round 33 (wave 26r, v189)

`qisas-al-nabiyyin-1` is **complete for volume 1: twenty-three chapters, 597
sentences, 4,502 tokens** (print pp. 1–68). The four chapters of this wave are
§21–25 of «أَحْسَنُ الْقَصَصِ» (print pp. 59–68): ch20 «إِلَى يَعْقُوبَ» (§21; the
brothers' return with 12:81 and 12:83), ch21 «يَظْهَرُ السِّرُّ» (§22; Yaʿqūb's grief
with 12:84 and 12:86, the third journey, the secret revealed with 12:89–92),
ch22 «يُوسُفُ يُرْسِلُ إِلَى يَعْقُوبَ، وَيَعْقُوبُ عِنْدَ يُوسُفَ» (§23–24; the shirt with
12:93–98, the prostration with 12:100 and 12:4), ch23 «حُسْنُ الْعَاقِبَةِ» (§25; the
kingship that did not distract, the prayer of 12:101, the death) —
regenerators `author_qisas_ch20.py` … `author_qisas_ch23.py`, +100 glossary
entries, +39 paradigms (عَسَى stored jamid, the geminates قَرَّ of bāb سَمِعَ and
اِرْتَدَّ through `entry()` with split stems, عَمِيَ and تَوَفَّى through the
kasra-māḍī nāqiṣ road). Endings-mode ḍabṭ at v189: **ch20 100.0 (151), ch21
100.0 (238), ch22 100.0 (206), ch23 100.0 (93)** — floors 97; ch1–19 held;
Talkhīṣ 48–50 and 71–76 unchanged; the 47 seeds 267/267; sarfAudit clean. One
round in nine cuts (`patch26r` … `patch26r9`, round 33), the probe-first way:
41/73 sentences clean on the v188 engine, then 58, 67, 71 and 73/73 — and the
neighbour sweep's sixth cut, the drill garden's seventh and the release's eighth, below.

**The sentence's end is not where the text ends.** Four of the round's rules
were written and measured inert before they fired, and every one of them was
reading the wrong copy of a fact:

- **The ladder resets the verb's state before the inheritance rules read it.**
  A rule placed beside `inheritSubj` read `st.failRow` and `st.verb` AFTER the
  row had already claimed `st.verb = i` and cleared the doer; the fact it needed
  lives in `prevFailRow` and `pre30.verb`, captured at the ladder's top for
  exactly this reason. وَتَوَفَّاهُ اللهُ مُسْلِمًا وَأَلْحَقَهُ: the second verb wears its
  object and inherits the first's named doer.
- **A rule's guard inherits the earlier rule's blind spot.** The hamza-over-fā
  peel (أَفَيَفْجَعُونَهُ) copied the open-class peel's `out.length === 0` — true
  at the sentence head, false after the comma where the question actually
  stands. The verb shape behind the hamza and the fatḥa'd fā is unambiguous, so
  the peel now fires anywhere. And the endings strip had taken the pronoun's
  vowel off the host (يَفْجَعُونَه), so the corpus walk needed the هُ candidate
  back — the strip and the matcher have to agree about what a stripped pronoun
  looks like.
- **A `keep` that rewrites `row.w` changes what the writer keeps.** The
  standalone question hamza (ءَأَنَّكَ, written on the line in the print) was
  peeled by rewriting the row's word; the writer then wrote the remainder. The
  row keeps the whole word; only the analyzer's `w` and `core` lose the hamza.
- **`sawfa` set the right cell and a later pass overwrote `__cell`.** The
  passive twin rule (the speaker's أُضِيفُ against the passive أُضِيفَ) stamps
  `r.__cell`, which the ladder reads before `r.cell`; سَوْفَ أَسْتَغْفِرُ needed both
  the flag the twin rule now respects and the author's ḍamma as a receipt.

**The strip had a joiner bug for two hundred versions.** `stripEnding` tested
the wiqāya-nūn tail (نِي) by comparing the lexicon's lemma against the host —
without taking the joining wāw off the host — so وَحُزْنِي failed the test, kept
«نِي» as its tail, and `rawStrip` ate the sukūn of the zāy as if it were the
ending (وَحُزنِي). The lemma test folds the joiner now; the same fold already
lived in a dozen other guards (the clitic hides the feature a rule tests for).

**The rules of round 33, each paid for by a token:** the five noun annexed to
the speaker's bare yāʾ is kept (أَبِي، أَخِي — a name after it would make the
yāʾ the letter of jarr: أَبِي زَيْدٍ); سُبْحَانَ اللهِ beside مَعَاذَ اللهِ; هَلْ opens
its clause; the delayed ism of إِنَّ after a fronted jarr khabar (إِنَّ لِلّٰهِ فِي
ذٰلِكَ يَدًا خَفِيَّةً — and the demonstrative under فِي is the majrūr, not the ism
the wave-23 rule took it for); كُلُّهُمْ after a plural verb is the tawkīd of its
wāw; نَفْسَهُ after a transitive verb still owing its object is the object, not
the tawkīd; the name before a demonstrative phrase after a transitive verb is
the fronted object and the phrase the doer (لَمْ يَشْغَلْ يُوسُفَ هٰذَا الْمُلْكُ);
الْيَوْمَ beside its verb is the zarf (أَفَيَفْجَعُونَهُ الْيَوْمَ، وَالْيَوْمَ يُفْجَعُ); the
kin word joined after an intransitive verb's doer joins the doer (وَبَقِيَ يَعْقُوبُ
وَآلُ يَعْقُوبَ); the nakira after a returning jarr phrase after a finished khabar
opens its ṣifa clause with the phrase as fronted khabar (كَانَ بَشَرًا فِي صَدْرِهِ
قَلْبُ بَشَرٍ — and that mubtada carries no subject across the sentence); the
second object of a two-object verb is never a chain member and is not owed past
a jarr letter (مَنَعَهُمْ مِنْ أَنْ يَقْنَطُوا مِنْ رَحْمَةِ اللهِ); R8's delayed doer stands
down for the annex of the noun before it and after a seated subject (مِنْ كَثْرَةِ
الْبُكَاءِ); the nahy reads the author's sukūn (وَلَا تَسْأَلْ after a complete
clause); the intransitive joined verb — by gloss or by a paradigm with no
passive — names its own pronoun-bearing doer under both inheritances (وَتَجَدَّدَ
حُزْنُهُ); يَا أَسَفَى is kept, no mark on an alif; لَمْ يَزَلْ conceals its ism like
وَكَانَ and joins the kāna list; إِلَى مَتَى is the question whatever follows (a jarr
letter never enters on a conditional); أَلَمْ أَقُلْ is the hamza over لَمْ — a
shadda on a cell's last letter is ṣarf and the written sukūn refutes it, and
before a verb the particle remainder wins; ابْنَكَ after إِنَّ is the son; a
jussive cell (أَجْرِ ~ جَرَى) cannot wear the author's fatḥa, and the lexicon's
أَجْر owns the word; a lexicon noun reached by bare letters whose marks
contradict the written word loses to the verb cell the marks spell exactly
(الْقِصَّةَ عَلِمَ أَنَّ — and that cell is SURE, so the feminine-nakira demotion
stands down); kāna is no transitive head for the chain walk (وَكَانَ دُعَاءُ
يُوسُفَ annexes); a tanwīn head annexes nothing in the chain walk too (رَجَاءٌ
كَبِيرٌ، يَدًا خَفِيَّةً — the author's token is the receipt, seat alif included);
لَأَنْتَ is a detached pronoun under a lām and annexes nothing, the strip and the
writer keep it; the print's dagger alif inside a name (إِسْحٰقَ) is an alif for
the names table; a singular joined noun before a PLURAL joined verb is not
that verb's own subject (وَبِنْيَامِينَ وَيَجْتَهِدُوا).

**The neighbour sweep paid for three rules, and one of them was a lesson about
shape.** (1) «A name before a demonstrative phrase after a transitive verb is
the fronted object» (لَمْ يَشْغَلْ يُوسُفَ هٰذَا الْمُلْكُ) took ch19's سَمِعَ يُوسُفُ هٰذَا
الْبُهْتَانَ within the sweep: the two sentences share every surface feature, and
only the VERB splits them — the verbs of distraction and prevention (شَغَلَ،
أَلْهَى، صَرَفَ، مَنَعَ) take the person as their object. The rule is keyed on that
closed set now; a rule that two readings fit equally is a guess, whichever
sentence it was written for. (2) R8's delayed doer (وَفَازَ بِاللَّذَّةِ الْجَسُورُ)
had been given a «seated subject» guard for مِنْ كَثْرَةِ الْبُكَاءِ, and the guard
took ch73's مَنْ رَاقَبَ النَّاسَ … وَفَازَ بِالطَّيِّبَاتِ الْفَاتِكُ — the subject seated
by مَنْ belongs to the first verb, and the delayed doer is the second's own. The
annex guard alone (the ال-noun completing an open idafa head) was the whole fix;
the second guard was reasoning, not measurement. (3) The five-noun keep met the
KUNYA: كَقَوْلِ أَبِي تَمَّامٍ، مِنْ أَبِي سَعِيدٍ — the yāʾ is the letter of jarr and the
name after it the annex, so the kept أَبِي now HEADS the noun after it when that
noun can be annexed (bare, not joined, not under a letter), and «my father»
stays the reading before a verb, a joiner or a pause.

**The drill garden's full-mode re-vowelling caught the seventh cut within the
sweep** — two rules that read letters where they should have read the author's
marks: the munada on a final alif (يَا أَسَفَى) was keeping يَا رَجُلًا, whose alif
is the tanwīn's seat; and «a lām or wāw before the letters of a pronoun» (لَأَنْتَ)
was keeping فَهْمًا, whose هما are the letters of هُمَا by accident — the tanwīn
and the sukūn on the hāʾ refuse the pronoun. Both rules now read the author's
token, in the strip and in the writer alike; in full mode the writer sees only
bare letters, so the author's token is the only receipt it has.

**The eighth cut was the release's — a māḍī is mabnī on its fatḥa.** Chunk 7
failed on the wave-21 pin أَقَوْمٌ آلُ حِصْنٍ and on Talkhīṣ ch67 (s9, the same
bayt): the round's «the author's marks spell the verb cell exactly» rule
compared the word and the cell with `rawStrip`, which takes the LAST vowel off
both — so آلُ read as the māḍī آلَ, mark for mark. The last vowel is iʿrāb on a
muḍāriʿ and may move; on a māḍī it is binaʾ and may not, so the exactness test
asks for the whole form when the cell is a māḍī. Chapters 58–60 and 65–70 were
not in the neighbour sweep — the sweep covered the chapters the previous rounds
had named, and the release found the one outside it within its first chunk.

**And a ninth from the diff of the chapters the sweep had skipped.** Running
ch58–70 against the v188 engine sentence by sentence (the only honest baseline:
a floor hides a one-token change) found وَيَوْمَ تَقُومُ السَّاعَةُ reading its doer as
a zarf: «the time noun beside its verb» had been written as «before or after a
verb» and must be «after a verb that already HAS its doer, or wa-joined before
its verb». The patch landed in the window between chunk 7 and the release.

**Content:** ch21 s20 had lost its عَلَى to a helper that printed the role
without the letter (هُوَ الَّذِي عَلَى خَزَائِنِ الْأَرْضِ) — the probe's
«خَزَائِنِ→خَزَائِنُ (mubtada)» was a content slip, not an engine miss, and the
matn line is the check. **Key hygiene:** `shaghala`, `ghayyara`, `hakama`,
`adda-count`, `mawt`, `salih`, `dua`, `hadith`, `wali`, `dunya`, `alhaqa` and
`aataa` (آتَى) were owned by other packages and copied with `find_gloss`;
`naffadha`, `hashara`, `fatir`, `akhira`, `tawaffa` are new; أَوَامِر rides the
standing `amr` with its plural named in the iʿrāb (the أُمُور plural means
«matters»).

**A deviation, named.** The land chain's ADD-only diff reported `morphology
changed ['tala-long']`: chapter 22 re-specs the paradigm of طَالَ that chapter
13 had copied in with `find_morph` — every cell identical, the bāb string now
naming its model word in brackets and a note added. The chain's assertion
fired and the chain went on, because the Python heredoc that holds it had no
`|| exit 1` after it (the same trap this file records for `grep -c`): chunk 7
and the release were already running on the re-specced file before the log
was read. The release was left to run — the audit regenerates the cells from
the bāb's model word, which did not change — and the deviation is recorded
here instead of costing a second two-hour pass. The chain script has its exit
now; chapter 22's `pop` of an inherited key is the thing to remove next wave.

## Iẓhār al-Asrār opens — Birgivī's matn from the lithograph, and round 34 (wave 27, v190)

`content/samples/izhar-al-asrar` (L5 Advanced, premium; regenerator
`tools/authoring/author_izhar_ch1.py` over the shim `izhar_common.py`, which
re-points `talkhis_common` at the package) carries the matn of Birgivī's Iẓhār
from `research/sources/izhar-al-asrar-matn-lithograph.txt` — the framed text of
the Ottoman lithograph, print pp. 84–89 for this chapter: the ḥamd, the treatise
and the three things every parser needs (the governor, the governed, the
governing = the iʿrāb), the kalima and its three kinds stated through the MARKS
each admits and whether each governs, the ʿāmil's definition (مَا أَوْجَبَ
بِوَاسِطَتِهِ كَوْنَ آخِرِ الْكَلِمَةِ عَلَى وَجْهٍ مَخْصُوصٍ مِنَ الْإِعْرَابِ), its division
lafẓī/maʿnawī, samāʿī/qiyāsī, in-the-noun/in-the-muḍāriʿ, one-noun/two-nouns, and
the TWENTY jarr letters each with its meaning — 21 sentences, 281 tokens, 160
glossary entries (37 new), 13 paradigms (تَوَقَّفَ and عَنَى new). The note
`al-amil-wa-aqsamuh` (awāmil, level 5) carries the opening with an eight-question
test. The print's الصلوة / ثلثة are given standard and the manifest says so;
the Turkish follows the tercüme on the shelf in sense. Endings-mode ḍabṭ at
v190: **ch1 100.0 (281)** — floor 97; 239/281 on the v189 engine, then 263, 273,
277 and 281 across seven cuts (`patch27a` … `patch27g`, round 34), and two more from the neighbour sweep. The chapter
is the engines' own test-bench: every one of the twenty entries is a nominal
sentence whose mubtada is a PARTICLE mentioned as a word.

**A word mentioned as a word keeps its own marks and takes the seat the
sentence gives it.** مِنْ لِلِابْتِدَاءِ: the jarr letter is quoted (لَفْظٌ مَحْكِيٌّ
قُصِدَ لَفْظُهُ) and stands in the place of rafʿ as the mubtada; كَأَنَا وَأَنْتَ and
كَهَلْ وَقَدْ sit in the place of jarr under the kāf. The engines already keep a
closed-class word whole; what the chapter forced was the seat around it: a
masdar annexes the quoted particle (دُخُولُ قَدْ — a قَدْ before no verb is a word
mentioned, so the head writes no tanwīn), a clitic over a quoted pronoun or
particle is kept whole (the lexicon's clitic-stripped hit on أَنَا is no refusal),
and an ال-adjective after a quoted word under a jarr letter is its naʿt (عَلَى مَا
الِاسْتِفْهَامِيَّةِ — the quoted مَا is a NOUN row to the analyzer, pk `ma`, not a
particle row). حَاشَا entered PARTICLES as a jarr letter.

**The rules of round 34, each paid for by a token:** the ḥamdala's رَبِّ is the
annexed naʿt of the Name and the jarr phrase was the khabar (الْحَمْدُ لِلّٰهِ رَبِّ
الْعَالَمِينَ), and the joined noun with its own jarr-phrase khabar joins the
mubtada (وَالصَّلَاةُ عَلَى مُحَمَّدٍ) — never when the next jarr particle is itself
joined (لِلْبُعْدِ وَالْمُجَاوَزَةِ، وَعَلَى); آل wearing a pronoun is the family
(وَآلِهِ — آلَ «to return» takes no object); the sentence-initial وَبَعْدُ before a
fā-clause keeps its ḍamma; the colon list after a counted annex spells out the
NUMBER (ثَلَاثَةُ أَشْيَاءَ: الْعَامِلُ), and the noun after the explaining أَيْ follows
its head (أَيِ الْإِعْرَابُ — the particle wears the iltiqāʾ kasra before the waṣl
alif, which the analyzer's sukūn test had refused); the colon item after a dual
or a number is the khabar of an omitted «one of them» (ضَرْبَيْنِ: سَمَاعِيٌّ
وَقِيَاسِيٌّ) and is never the naʿt of the majrūr before the colon; a joined noun
that REPEATS an earlier seat's word takes that seat (عَامِلٌ فِي اسْمٍ وَاحِدٍ وَعَامِلٌ
فِي اسْمَيْنِ، حُرُوفَ الْجَرِّ وَحُرُوفَ الْإِضَافَةِ); the joined annexing noun after a
masdar's own annex joins the annex (دُخُولُ التَّنْوِينِ وَحَرْفِ الْجَرِّ وَلَامِ
التَّعْرِيفِ — keyed on the head's «(masdar)» gloss, so عَيْشَ السُّعَدَاءِ وَمَوْتَ
الشُّهَدَاءِ keeps its parity); the joined pronoun-bearing كُلّ/بَعْض before a bare
nakira opens a nominal clause (وَكُلُّهُ عَامِلٌ، وَبَعْضُهُ غَيْرُ عَامِلٍ); بَلْ after a
غَيْر-negation opens a new clause whose bare nakira is the khabar of an omitted
mubtada (بَلْ آلَةٌ); inna's khabar survives a parenthetical (أَنَّ الْكَلِمَةَ، وَهِيَ
اللَّفْظُ الْمَوْضُوعُ لِمَعْنًى مُفْرَدٍ، ثَلَاثَةٌ); غَيْر's walk back steps over an
unpeeled بِالْفَهْمِ; the passive continuing a ṣifa clause conceals its deputy and
the annexed noun after it is its second object (حُرُوفٌ تَجُرُّهُ تُسَمَّى حُرُوفَ
الْجَرِّ); kāna after a relative with jarr phrases after it takes the bare nakira
past them as its delayed ism (مَا يَكُونُ لِلِّسَانِ فِيهِ حَظٌّ); the future sīn never
stands on a jussive (عَلَى مَا سَيَجِيءُ), and the analyzer's jawāb-al-ṭalab note is
trusted only after a REAL ṭalab (أَعْنِي after the listed عَامِلٌ, which the
analyzer had read as the amr of عَامَلَ); the relative's verb takes a jarr
clitic on the next word as its majrūr, never its object (بِوَاسِطَتِهِ، بِهَيْئَتِهِ);
the definitional relative X هُوَ مَا VERB keeps its ʿāʾid as the doer when the verb
is transitive — the first plain noun past the jarr phrases is the object (مَا
أَوْجَبَ بِوَاسِطَتِهِ كَوْنَ) — while an INTRANSITIVE verb after a relative names its
doer in the noun after it, even behind a fused pronoun (الَّذِي يَتَوَقَّفُ إِعْمَالُهُ،
مَا يَحْتَاجُ إِلَيْهِ كُلُّ مُعْرِبٍ); the verbs that take their complement through a
letter are intransitive for the object seat (need, depend, hinge, attach, belong
joined INTRANS; Form VIII with no stored passive and no ism mafʿūl joined
`intransParadigm`), and the «verb + fused pronoun + nakira → object» frame is for
the Form II/IV shapes only — a waṣl-alif verb is not one (اتَّصَلَ بِهَا ضَمِيرٌ).

**Four traps, each a doctrine this file already holds wearing a new mask:**
- **The writer's hamza seat.** مُبْتَدَأً: a hamza seated on the alif takes the
  fathatan with no second alif, and so does the mamdūd's hamza after its alif —
  `writeNoun` wraps `writeNoun0` and corrects the two tails.
- **A prefix regex on a core that still wears its article.** The tafṣīl badal is
  armed when a set row's core matches NUMBERS — and «الف» matched الْفَاعِل, so
  كَاسْمِ الْفَاعِلِ وَبَعْضُهُ غَيْرُ made غَيْرُ a badal of the thousand. The article
  before a fāʾ is no أَلْف unless the core IS the number (الف، الفان، الاف).
- **آخِر and آخَر are one spelling to the bare letters.** The diptote-ṣifa cut
  (كَلَامِ آخَرَ) and the sifa-shape test read «اخر» and cut كَوْنَ آخِرِ الْكَلِمَةِ;
  the khāʾ's vowel decides — the min/man family's newest member.
- **The nisba's doubled yāʾ is no plural pattern.** سَمَاعِيّ matched the
  diptote-by-shape test (فَعَالِي) and lost its tanwīn while لَفْظِيّ kept it; the
  guard reads the shadda before any shape is tried.

**A table the engines READ must be complete — fourth payment.** `FUSED_PRON` had
فِيهِ and عَلَيْهِ and not إِلَيْهِ, while the relative presumption's own regex listed
اليه; the one-letter `fused()` test stood blind to فِيهِ in a look-ahead this wave
wrote (and had been widened once already in wave 26). Both reads now go through
the one table, and إِلَيْهِ is in it.

**The neighbour sweep paid for two guards — and bisected one miss away.** (1) The
intransitive-relative doer rule read the clause-initial negating مَا of وَمَا بَقِيَ
عِنْدَهُمْ شَكٌّ as a relative and seated the ẓarf as the doer; a bare مَا/مَنْ at the
head of its clause before a verb is the negation (`patch27h`). (2) The
quoted-particle annex armed on مَلَامَةً إِنَّ and ذِكْرٌ، وَإِنَّ — the particle must
be one that normally precedes a VERB (قَدْ، سَوْفَ، لَمْ، لَنْ) and must be followed by
a joined list, or it is no word mentioned; and the ḥamdala's naʿt rule reached
عَبْدَ اللهِ بْنَ الزُّبَيْرِ — the Name ANNEXED heads no naʿt, and ابن is never one
(`patch27i`, with the nisba guard asking the lexicon so that زَرَابِيُّ, a stored
plural on the same letters, keeps its bar). (3) Kāfiya ch1 s12 (حَقِيقَةً أَوْ حُكْمًا
after a numbered annex) reads as a khabar — on the unpatched v189 reader too:
a pre-existing miss inside its floor, recorded here rather than chased in this
wave. Talkhīṣ 48–50 and 71–76, Qiṣaṣ 6/14/15/19–23, Kāfiya ch2, the 47 seeds
(267/267), the r21/r22 gates, the drill garden (FULL jumal 96.3) and sarfAudit
(n: 0) are at baseline.

**The tooling.** The first probe of a new package needs its OWN dry build
(`build27.sh`: every repo package plus the dry copy, the grammar copy via
`--grammar-dir`), and `probe24_sen.js` takes `STORY=izhar-al-asrar`. A rule
whose anchor is a `const` with a cut comment is found by `rep()`'s count — every
cut script asserts each anchor exactly once, and the instrumented copy
(`patch26_dbgset.py`, plus one-off `_trace.push` lines) is what named the
look-ahead's blindness and the tafṣīl arming in minutes where reading the ladder
had not.

**What the release found after the measured gates were green — two findings in smoke chunk 6, each a
standing doctrine wearing a new mask (`patch27j`).** (1) **A new lexicon entry is a predator, fifth
payment — and this time the prey was a homograph.** The Izhar's glossary brought قَسَم (the oath, among
the jarr letters' meanings) into the noun index, which is keyed by BARE letters, and the oath took the
key from قِسْم (the kind): the writer's dual test compares the written marks against the lemma it was
handed, قِسْمَانِ no longer agreed with قَسَم, and the wave-19 pin wrote قِسْمَانٌ with a tanwīn. The index
now keeps a refused strong homograph as an ALTERNATE of the key's holder (the جَارٍ-beside-جَار mechanism,
generalised), and `nounFromCorpus` prefers the lemma whose marks agree with the written word on the
key's letters, the last letter excepted (iʿrāb), the shadda ignored (sarf the writer may not carry) —
unvowelled input keeps the holder. The rule underneath is the sarf test's: the vowels before the last
letter are the word's identity, and a lookup that throws them away answers for the spelling, not the
word. (2) **A verb the corpus is silent about is UNKNOWN, not intransitive.** The round-34 rule «an
intransitive verb after a relative names its doer in the noun after it» had a fallback — a verb with no
stored passive and no ism mafʿūl counts as intransitive — and شَاءَ owns no passive; so لِمَنْ يَشَاءُ
الذُّكُورَ seated the males as the doer of «wills» and ch62's taqsim frame lost its fourth share. Under a
jarr-fused relative (لِمَنْ، بِمَا، مِمَّا) the relative's clause sits inside an OUTER verb's government
and the noun after it belongs to that verb unless the inner verb is KNOWN intransitive (gloss or
paradigm shape); the fallback stands only for a bare relative at the clause head, where it was written.
Both chapters were outside the neighbour sweep (ch61–64 and the wave-19 pins); the sweep now runs
every Talkhīṣ chapter from 48 and the drill, so a rule's new reach is measured before the two-hour run.
(3) **A clitic-peel regex is a homograph trap, every time — `patch27k`.** The quoted-word keep (كَأَنَا وَأَنْتَ،
كَهَلْ وَقَدْ: a ب/ك/ل over a closed-class word mentioned as a word) matched by bare letters, and كَانَتِ is ك + انت
to the letters: إِنْ كَانَتِ الْعَلَاقَةُ غَيْرَ (ch51) and وَكَانَتِ الْبِيضُ (ch70) lost their kāna. The keep now
stands down on a whole stored verb cell and on a word the lexicon owns whole (كَهْل). Neither chapter was in the
round's sweep; a per-sentence diff of EVERY Talkhīṣ chapter against the v189 engine found both inside their
floors — which is why the floors are floors and the diff is the measurement.
The per-sentence diff of al-Samti (eleven chapters, both readers) showed the cost of the accident: وَكَانَتْ مِنَّةُ أَبِي
حَنِيفَةَ بِوَصِيَّتِهِ إِلَيَّ وَبِرِّهِ أَعْظَمَ had been «clean» on وَبِرِّهِ because وَكَانَتْ was KEPT as كَ + أَنْتَ and
kāna never opened; with kāna read, the ism is right and the joined وَبِرِّهِ — a jarr clitic that should join
بِوَصِيَّتِهِ while kāna's khabar is still owed — opens a nominal clause instead. One token, structurally an
improvement, inside the floor (92.3 against 91), and the rule it names is round 36's.

### v190 addendum — patch27l: the perceptron on interned features

The v190 release blocked at smoke_3 on the crossVal timing gate (9.8 s against the 6.5 s ceiling). Measured A/B on the same host: the v189 reader took 9.7–10.6 s too, so the host was ~1.7× slower than at v189, not the engine. Rather than raise the ceiling, `IrabModel.fit` now interns every feature string to an integer once and keeps weights / accumulators / last-touched clocks in flat `Float64Array`s (`role*F+feature`, slot 0 the bias). Same LCG shuffle, same update order, same floating-point sums: `crossVal`, `accuracy`, the per-role key counts and a hash of every averaged weight were compared old vs new and are identical to the digit (cv 0.61292/0.76370, resubstitution 0.66880/0.81500, 13,762 tokens, 20 folds). Cost: 10.4 s → 2.7 s on the slow host. `rank()` and `tools/ablate_estimator.js` read the same string-keyed `{w, total}` as before. Rule kept: a timing-gate failure is first A/B'd against the previous reader on the same host; if the host is the cause, make the algorithm cheaper, never the gate looser.

## Iẓhār chapter 2 — what the jarr letters hang on, and the round the quoted lists forced (wave 28, v191)

`izhar-al-asrar` runs to **two chapters, 33 sentences, 460 tokens**: chapter 2
(print pp. 89–91; `author_izhar_ch2.py`) carries the taʿalluq of the jarr letters
— every one hangs on a verb, its likeness or its meaning, except the zāʾid — the
seven that hang on nothing (the zāʾid, رُبَّ, حَاشَا, خَلَا, عَدَا, لَوْلَا, لَعَلَّ) with
where their majrūr stands, the five seats of the majrūr (mafʿūl fīh, mafʿūl lah,
mafʿūl bihi ghayr ṣarīḥ, the deputy of the doer, the fronting), and the omitted
mutaʿallaq that makes the ẓarf mustaqarr against the laghw — 12 sentences, 179
tokens, 53 glossary entries, 3 paradigms. The note `mahall-al-majrur` (awāmil,
level 5) carries the doctrine with an eight-question test. Endings-mode ḍabṭ at
v191: **ch2 100.0 (169)** — floor 97; 143/166 on the v190 engine, then 160 and
169 across three cuts (`patch28a`…`28c`, round 35). The chapter is twelve
definitional sentences, each closing on a quoted example after نَحْوُ:, and the
rules it forced are the rules of a text that TALKS ABOUT its own particles:

- **A word listed as a word opens nothing.** مَجْرُورُ لَوْلَا وَلَعَلَّ مُبْتَدَأٌ: the
  analyzer rightly pushed inna's expectation after لَعَلَّ, and the ladder seated
  مُبْتَدَأٌ as its ism. A noun head before a particle that is followed by a JOINED
  particle is annexing a list of words mentioned (`__quoted27` on both); a quoted
  particle is kept as hikāya and pushes nothing, and the inna-note rules stand
  down after one. The exceptive list وَحَاشَا وَخَلَا وَعَدَا is kept the same way —
  the wāw-joined exceptive after a joined particle is a word mentioned, not a
  majrūr of the letter before it (which is what the new خَلَا row had made of
  عَدَا within the minute).
- **The listed لَعَلَّ governs jarr in its own example.** لَعَلَّ زَيْدٍ قَائِمٌ is the
  ʿUqayl dialect the Iẓhār counts among the jarr letters; nothing on the page
  decides it but the text itself, which has just listed لَعَلَّ as a quoted word.
  A later لَعَلَّ in a sentence that carries a quoted لَعَلَّ earlier governs jarr,
  and the noun after its majrūr is the khabar. The receipt is the mention.
- **نَحْوُ: after a pause.** Wave 25 read the citation head only at the sentence
  head; the Iẓhār writes «…، نَحْوُ: كَفَى بِاللهِ» inside every sentence. The rule
  now fires after a pause too, resets the clause and marks the citation wall.
- **The colon list after a nakira majrūr is its badal** (مِنْ مُتَعَلَّقٍ: فِعْلٍ أَوْ
  شِبْهِهِ أَوْ مَعْنَاهُ) — beside the wave-27 rule that makes the list after a dual
  or a number the khabar of «one of them». **The exception after a negated,
  complete nominal clause** is manṣūb (لَا بُدَّ … إِلَّا الزَّائِدَ): the two verbal
  إِلَّا rules needed a verb, and a nominal clause with the genus-lā idiom or a
  seated khabar is complete.
- **A term-noun the lexicon glosses «the …» keeps its chain.** مَجْرُورُ حُرُوفِ
  الِاسْتِثْنَاءِ and مَنْصُوبُ الْمَحَلِّ wear مَفْعُول, and the chain cut «a sifa-shaped
  head before a bare noun» ate them; the wave-16 escape (فَعِيلَة worn by a NOUN)
  now admits any lexicon noun whose gloss opens «the …» — the nahw's own terms.
  The joined term-noun at the clause head annexes مَا عَدَا (the relative under a
  verb of exception), and the annexed participle after that sila, with the
  khabar still owed, is the khabar — not the ḥāl the shape rule offered.
- **The pair under the letter is the dual verb's subject.** فِي الْجَارِّ وَالْمَجْرُورِ
  يُسَمَّيَانِ: the wave-16 rule «a joined noun before its own verb joins the earlier
  subject» crossed to الْمَحْذُوفُ; a joined ال-noun right after an ال-majrūr before
  a DUAL verb joins the majrūr. The dual is read off the WRITTEN word (…ان): in
  the endings-stripped rows the verb may carry no cell at all.
- **The jawāb after a māḍī shart may keep its rafʿ, and the kept nūn is the
  receipt.** فَإِنْ كَانَ الْمَحْذُوفُ … يُسَمَّيَانِ: the ShartEngine's frame hands the
  jawab to jazm; where the shart is a māḍī (a cell, or كَانَ's closed-class row,
  which carries none) and the author's five-verbs nūn stands, the raf is written
  — the books allow both, and the page decides.
- **The masdar after an impersonal verb is its doer** (وَيَجُوزُ تَقْدِيمُ): the
  mafʿūl muṭlaq rule for an annexed masdar stands down for جَازَ، وَجَبَ، صَحَّ، لَزِمَ،
  أَمْكَنَ and the glosses «permissible / obligatory / possible».
- **فَيَكُونُ conceals its ism like فَكَانَ** (فَيَكُونُ مَرْفُوعَ الْمَحَلِّ after the
  passive clause with its deputy) — the muḍāriʿ joins the wave-26 regex.
- **The passive by the author's ḍamma.** مُرَّ بِزَيْدٍ: the package stores no
  passive for مَرَّ, and the loose cell walk matched the active مَرَّ. A māḍī cell
  matched with the author's token opening on a ḍamma where the cell opens on a
  fatḥa is the passive, stamped as a derived majhūl — the wave-25 «the author's
  ending is evidence» read at the FIRST letter.
- **The joiner's fatḥa at the matching layer.** فُلَانًا was reaching فَلَانَا through
  the corpus walk's joined pass; the analyzer's base peel learnt in wave 15 that a
  joining letter wears a fatḥa, and the matching layer had not — the wāw/fāʾ
  wearing any other mark is radical there too (`patch28c`).

**Content and tooling.** خَلَا the exceptive is `khala-except` (the verb «to be
devoid» owns `khala`) and joins PARTICLES as a jarr letter beside حَاشَا; كَيْمَهْ
joins as a question. The dry build of a package the shelf already carries must
EXCLUDE the landed copy (`build27.sh` skips `content/samples/izhar-al-asrar` when
a dry copy is passed), or the landed one wins the id and the new chapter is
silently absent — the first ch2 probe crashed on it. And a ladder guard traced
through `window.__X` globals from inside `decide()` named the three remaining
misses in one run where the SET trace could not (the dual verb's cell missing on
the stripped row; the quoted list firing while a LATER rule re-opened inna; the
mubtada state reset by the sila's verb).

**The neighbour sweep paid for two narrowings (`patch28d`, `28e`).** The colon-badal rule took every colon list
after a nakira majrūr — the Talkhīṣ writes «…: وَاحِدٌ», «…: تَبْلِيغٌ وَإِغْرَاقٌ وَغُلُوٌّ», «…: قَصْرٌ تَحِيَّةٌ وَسَلَامُ»
as new clauses in rafʿ (five chapters moved) — and the Iẓhār's list is a list of ALTERNATIVES: a badal only when
أَوْ follows the first item. The exception rule took لَوْ كَانَ فِيهِمَا آلِهَةٌ إِلَّا اللهُ and the shahāda itself
(لَا إِلٰهَ إِلَّا اللهُ) — manṣūb only behind the genus-lā IDIOM whose ism the لَا row recorded (بُدَّ، شَكَّ، رَيْبَ…).
A rule written on one sentence inherits that sentence's whole frame; the sweep is what says which half of the
frame was the receipt. And فُلَانًا → فَلَانَا (Talkhīṣ ch63 s5) is a standing v189 miss that the hikāya accident
had hidden in wave 27 (ك + انا): the root finder's bare candidate list strips the fāʾ before the vowel is read
(`radJoin28` guards the first strip; the loose passes still reach لَانَ's dual through the bare skeleton) —
recorded, inside its floor, for the next round.

## Iẓhār chapter 3 — the omission of the jarr letter, and round 36 (wave 29, v192)

`izhar-al-asrar` runs to **three chapters, 51 sentences, 814 tokens**: chapter 3
(print pp. 91–94; `author_izhar_ch3.py`) carries the omission of the governing
letter — by rule in three places: the mafʿūl fīh (the time ẓarf, vague or
bounded: سِرْتُ حِينًا، صُمْتُ شَهْرًا; the vague place ẓarf — the six directions,
عِنْدَ، لَدَى، وَسْطَ، بَيْنَ، إِزَاءَ، حِذَاءَ، تِلْقَاءَ, the measured distances فَرْسَخ، مِيل، بَرِيد —
with the exceptions جَانِبًا، وَجْهًا، وَسَطًا، خَارِجَ الدَّارِ، دَاخِلَ الدَّارِ، جَوْفَ الْبَيْتِ and
every place-noun not meaning rest (مَقْتَل، مَضْرَب) or whose governor does not
(مَقَام، مَكَان); the bounded place keeping فِي except after دَخَلَ، نَزَلَ، سَكَنَ), the
mafʿūl lah as the doer's own concurrent act (ضَرَبْتُ زَيْدًا تَأْدِيبًا against
أَكْرَمْتُكَ لِإِكْرَامِكَ), and أَنْ / أَنَّ (80:1–2); by hearing elsewhere; ḥadhf
wa-īṣāl surfacing the iʿrāb of place (7:155, مَالٌ مُشْتَرَكٌ، ظَرْفٌ مُسْتَقِرٌّ); the
shādhdh اللهِ لَأَفْعَلَنَّ; two letters of one meaning never on one verb without
ʿaṭf — 18 sentences, 354 tokens, 113 glossary entries, 4 paradigms (اِنْتَصَبَ،
عَبَسَ، أَوْصَلَ، اِخْتَارَ). The note `hadhf-al-jarr` (awāmil) carries the doctrine with
an eight-question test, five anchored examples and three mistakes. Divergences
recorded in the chapter's notes: لم يثبت restored where the lithograph's line
breaks, كلت جانبا read as كُنْتُ جَانِبَ, the فَ of أَمَّا omitted as printed.
Endings-mode ḍabṭ at v192: **ch3 100.0 (354)** — floor 97; 276/354 on the
v191 engine, then 289, 297, 309, 352 and 354 across the cuts (`patch29a`…`29f`, round 36). The
rules the chapter forced:

- **A quoted letter is annexed by the noun that names its omission.** حَذْفُ فِي
  مِنْهَا، فَإِنَّ حَذْفَ فِي مِنْهُ قِيَاسٌ: the masdar head takes the quoted jarr letter
  as its annex (no tanwīn) when a fused pronoun-particle, a pause or a
  non-jarr particle follows the letter — and فِي begins with a fāʾ, so the
  joiner test asks `joined()` instead of the first letter (`29a` R1, `29c`, `29d`).
- **Kāna's bare annexed head is its khabar only when kāna carries its
  subject** (كُنْتُ جَانِبَ الدَّارِ) **or nothing after the whole annex can be a
  khabar.** كَانَ عَامِلُ الْقِسْمِ الْأَخِيرِ بِمَعْنَى الِاسْتِقْرَارِ: the walk passes the
  annex and its ال-naʿt, finds the jarr phrase, and the head is the ism; the
  ال-noun after the ism's annex is its naʿt when a jarr phrase waits (`29b`, `29c`, `29d`).
- **A waw-joined muḍāriʿ that opens its own condition is a new clause, not the
  jawāb** — وَيُرْفَعُ إِنْ كَانَ نَائِبًا keeps its rafʿ even when the frames had
  paired it with the earlier إِنْ (`29b`, `29c`).
- **نَحْوَ as a citing ẓarf annexes the saying** (نَحْوَ قَوْلِهِ تَعَالَى); **نَحْوُ: with
  a colon is the khabar of a dropped mubtada and never the citing ẓarf**, needs
  no pause before it (…الِاسْتِقْرَارِ نَحْوُ:), **and a LIST after its colon is
  annexed** — فَرْسَخٍ وَمِيلٍ وَبَرِيدٍ, الْمَقْتَلِ وَالْمَضْرَبِ — while a quoted sentence
  (نَحْوُ: زَيْدٌ قَائِمٌ) is not: the next word must be a joiner, a pause, أَوْ or the
  end (`29c`, `29d`, `29e`).
- **The oath with its letter omitted** — اللهِ لَأَفْعَلَنَّ — is jarr by the qasam
  (the rule had refused the jalāla for wearing ال); **وَاللهِ / تَاللهِ / بِاللهِ** as the
  oath particle are written with the kasra (`29c`).
- **A tāʾ-verb carrying كَ is spoken by «I»**: أَكْرَمْتُكَ decides the person of
  every tāʾ-verb in the line (ضَرَبْتُ، جِئْتُكَ) — the object كَ is no addressee
  evidence, and the speaker pick runs before the addressee count (`29c`, `29d`).
- **A sentence opening on أَوْ or إِلَّا continues the last sentence's seat**: أَوْ
  ظَرْفَ مَكَانٍ (the khabar of the kāna before the full stop), إِلَّا جَانِبًا (the
  exception after the previous rule), the latter arming the exception list so
  the joined nouns after the vowelling gloss بِفَتْحِ السِّينِ continue it in naṣb
  rather than joining the gloss's annex (`29d`).
- **The listed direction-ẓarfs after وَهِيَ:** — قُدَّامُ وَأَمَامُ وَخَلْفُ … — are the
  pronoun's khabar and its ʿaṭf, written on a bare ḍamma (the ẓarf cut from its
  annex is mabni on the ḍamma), while the same words quoted under a kāf keep the
  kāf's form (`29d`, `29e`).
- **The nakira after a لَهُ phrase is the doer the verb was still owed** (مَا ثَبَتَ
  لَهُ اسْمٌ), and the relative's hidden-ʿāʾid reading stands down before it (`29d`, `29e`).
- **A verb of saying before a colon closes the frames behind it** (لَا يُقَالُ:
  كُنْتُ جَانِبَ الدَّارِ — the inna of the previous clause no longer owns the saying) (`29e`).
- **The ال-participle after a jarr-clitic noun is its naʿt** (وَكَالْمَقَادِيرِ
  الْمَمْسُوحَةِ) — the joined kāf-noun had slipped past the general naʿt rule (`29e`).
- **A waw-nun singular the lexicon owns is no sound plural, clitic or not**:
  بِسُكُونِ السِّينِ، بِقَانُونِ — the clitic had pushed the bare word over the plural's
  length test, so the ending writer refused it; the tens (عِشْرُونَ) stay plurals (`29d`).
- **The neighbour sweep's seven regressions, and the rules narrowed** (`29f`): the
  لَهُ-doer only after a relative (فَخَلَقَ لَهُمَا مَاءً keeps its object); the own-condition
  verb needs a SHART particle (فَإِنَّ is inna) and never the lām of command
  (فَلْيُسْعِدِ النُّطْقُ إِنْ); kāna's bare annexed head is never the khabar when the
  author wrote its rafʿ, when it is a quantifier head (أَحَدُ اللَّفْظَيْنِ، غَيْرُ) or when a
  colon or the end follows the annex (وَكَانَ دُعَاءُ يُوسُفَ:); the sentence-initial أَوْ
  continues only a kāna-khabar the last sentence actually left (`_carryKana29`,
  carried like the subject, in reading order); the speaker's tāʾ needs a māḍī stem
  before it (تَكُنْ is no tāʾ-verb — Talkhīṣ ch65 رَأَيْتَ); نَحْوَ: with the author's
  FATHA and a colon still cites (the Talkhīṣ's forty-odd نَحْوَ:), only the ḍamma
  makes it the khabar of a dropped mubtada.

Measured across the cuts (endings mode, 354 tokens): 276 on the v191 engine →
289 (`29a`+`29b`) → 297 (`29c`) → 309 (`29d`) → 352 (`29e`) → **354** (the list /
tens refinements of `29d`); ch1 100.0 (281) and ch2 100.0 (169) kept; the neighbour
sweep at baseline. Rules kept: a quoted word's joiner is read off the row, never
the first letter; a source's list and a source's sentence after the same colon
are told apart by what follows the first word; a sentence that opens on a
connective inherits the seat the last sentence left open.

## The İ'rab Mağazası and the nine causes — the Avâmil lesson and the Şerhu'l-Muğnî notes as engines (wave 30, v192)

Two of the v180 sources are now consumed as RULES rather than as reading. The
Avâmil lecture (row 35) teaches Birgivī as a shop — every word a MÜŞTERİ, fitted
with a BEDEN, showing an ENDAM, by an ETKİ EDEN — and `IrabShopEngine`
(`patch30a`) arranges exactly those four columns off verdicts the app already
derives: the seat and the governor from `DabtEngine.vowel()` (`x.k`, `x.rule`,
`x.head`), the class from `AlamaEngine.shape` plus the five-verbs persons
(`FIVE_PERSONS` 1 2 4 7 8 9 10 of the 14-cell order; nūn al-niswa 5 and 11 are
mabni) and the weak-final test on the lemma, the sign from the lesson's
Bedenler table (`CLASSES`: seven noun customers, three muḍāriʿ customers), the
manner from the ending's shape — the maqṣūr's three assumed vowels by
التَّعَذُّر, the manqūṣ's damma and kasra by الِاسْتِثْقَال with the fatha spoken, the
speaker's yāʾ by الْمُنَاسَبَة — and the governor's kind from `GOVERNOR` (Birgivī's
samāʿī / qiyāsī / maʿnawī, and «by following» for the tawābiʿ). The engine
never parses: a word the Dabt engine left undecided gets `manner: "mahalli"`
or `"mabni"` and no sign, a letter gets `"none"`. `IrabShopEngine.audit()`
grades the shop on the corpus's own «وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ» lines
(`readIrab` parses case + sign + مُقَدَّر from the first عَلَامَةُ clause of a
token's iʿrāb): **319/319 claims agree (100.0) over the whole corpus, 92/92 on the gate's 140-sentence budget** — after the five nouns with an enclitic (أَبُوهُ), the mulḥaq plurals (بَنِي، اثْنَا), the tanwīn's alif (زَيْدًا is no maqṣūr) and the written plural wāw (تُغْلَبُوا) were taught to the classifier; the first cut measured 287/322. The lab (`مَغَازَة` on the workshop rail), the
lesson's twelve seeds, the legend of ten customers / ten signs / three
obstacles, Birgivī's 60/30/10 tree on the Awāmil card (`BIRGIVI_TREE`, every
taught leaf linking its note) and the gShop game (only words where the
author's sign and the shop's sign agree are asked) are in DESIGN.md §25.

The Şerhu'l-Muğnî notes (row 36) count the diptote's NINE causes, and
`MamnuEngine` (`patch30b`) walks them with the notes' exits: ʿalamiyya with
taʾnīth (the tāʾ, or a listed feminine name / city), a verb's pattern (أَفْعَل,
يَفْعِل/يَفِيل/يَفُول, فَعَّل, يَحْيَى), ʿadl (فُعَل), a fused compound, ʿujma (a listed
foreign name), the alif-nūn; waṣfiyya with أَفْعَل, فَعْلَان, or the ʿadl numbers
(ثُلَاث… أُخَر) — the adjective read off `SifaEngine.classify` or the gloss; the
ultimate plural (`JamEngine.recognize`) and the alif of femininity, long
(`AlamaEngine.mamdudVerdict` — root-aware) or short (فُعْلَى / فَعْلَى / فُعَالَى by
shape), standing for two. Exits: ال and the idafa give the kasra back without
un-barring (`jarr: "kasra"`), رُبَّ strips ʿalamiyya so ʿujma alone no longer bars,
ـوَيْهِ is mabni, a tāʾ-plural (أَسَاتِذَة) declines in full; the quiet-middle
three-letter name (نُوح، مِصْر) is a PERMISSION in the notes, so the engine says
nothing there and the lexicon keeps its say — the corpus reads مِصْرَ as barred
and that reading is untouched. `AlamaEngine.mamnu` asks the engine first and
only a SURE verdict overrides the tagger; the Mağaza card prints the causes
under the figure. Audited against the authored endings (a bare majrūr noun
written with a fatha and no tanwin is diptote evidence, with ـٍ munsarif
evidence): **113/118 sure verdicts agreed on the first cut** — the five misses were مَاء read as an alif of femininity (a three-letter stem is required now), تَمِيم read as a verb's pattern (the prefix must be extra, the root's first radical tells), and the Talkhīṣ's خَرْشَنَةٍ, which the author reads with tanwīn and the engine leaves to the author; the thirty-five seeds of the notes pass. The `mamnu-min-sarf` note grew the nine causes and the
exits, a seven-question test, seven corpus-anchored examples (أَحْمَدَ، مَكَّةَ،
عُثْمَانَ، أَشْيَاءَ، إِبْرَاهِيمَ، فِرْعَوْنَ، أُخْرَى) and three more mistakes (`note30.py`).

Rules kept: an engine ARRANGES verdicts it did not make and says so; a source's
permission (مِصْر both ways) is never turned into a verdict; a game asks only
what the corpus asserts; every lab opens on a phone without a horizontal
scroll; the audit floors are measured on the day they are set.

**Gate repair at v192's release (29g):** the Nida corpus gate folds every
vocative particle flat and read the EXPLANATORY أَيْ of Iẓhār ch3 (حَرْفُ تَفْسِيرٍ,
«أَيْ: مِنْ قَوْمِهِ») as a call, then failed because the engine rightly refused
مِنْ / لِأَنْ / مُشْتَرَكٌ as munādās. The gate now skips أَيْ when the token's lexicon
key is `ay`, or its iʿrāb line names the tafsīr, or a colon follows it
(`patch29g_smoke`). The engine was right; the gate's reading of the corpus
was not.

## The hamza of إِنَّ decided from the seat — Iẓhār ch4 and the InnaEngine (wave 31, v193)

Iẓhār ch4 (print pp. 94–96, `author_izhar_ch4.py`) is the governor in two
nouns, first division: the eight letters whose manṣūb precedes their marfūʿ, the
six that resemble the verb with their meanings (إِنَّ / أَنَّ taḥqīq, كَأَنَّ tashbīh,
لٰكِنَّ istidrāk, لَيْتَ tamannī, لَعَلَّ tarajjī), the front of speech save أَنَّ, the
restraining مَا (إِنَّمَا ضَرَبَ زَيْدٌ), Birgivī's reason — إِنَّ leaves the sentence a
sentence, أَنَّ turns it into a maṣdar, hence KASR where a sentence stands and FATH
where a word stands — and the ten kasr places with their examples (28:76, 8:5):
12 sentences / 187 tokens, 48 glossary entries, 3 paradigms (the hollow
hamza-final نَاءَ يَنُوءُ written by hand on the أَسَاءَ precedent), the awāmil note
`mawadi-kasr-inna` with an eight-question test, six corpus-anchored examples and
three mistakes. Two readings of the lithograph are declared in the manifest: the
unclear «ومعها» before لَهَا صَدْرُ الْكَلَامِ is left out; «ولحقها ما» is read as the
māḍī وَلَحِقَهَا مَا with the conditional sense of the received wording. Chapter 5 (pp. 96–98, `author_izhar_ch5.py`) is the other half of the
rule: the fatḥa seats (a doer, an object, a mubtada, a muḍāf ilayh; after
لَوْ / لَوْلَا with the restored wording لَوْ ثَبَتَ / مَوْجُودٌ, after the مَا of time, a
jarr letter, the joining حَتَّى, مُذْ / مُنْذُ), the fāʾ of the answer where both
stand, and the LIGHTENED forms — إِنْ with its telling lām and the verbs of the
mubtada (2:143, 26:186), أَنْ with the concealed pronoun of the matter, a verb of
certainty before it and لَا / the sīn / سَوْفَ / قَدْ parting it from a conjugable verb
(73:20), none before a frozen verb, a condition or a prayer (7:185, 34:14, 24:9
in the reading أَنْ غَضِبَ اللهُ the print carries), كَأَنْ and لٰكِنْ — 10 sentences /
281 tokens, 60 entries, 5 paradigms, the note `mawadi-fath-anna` (nine
questions). Chapter 6 (pp. 98–99, `author_izhar_ch6.py`) closes the governors
of two nouns: إِلَّا in the disjoined exception read as لٰكِنَّ with a khabar
estimated, لَا of the genus with its condition, and the second division — مَا and
لَا that resemble لَيْسَ, their three conditions, the three failures (مَا إِنْ زَيْدٌ
قَائِمٌ، مَا قَائِمٌ زَيْدٌ، مَا زَيْدٌ إِلَّا قَائِمٌ) and the bar on a fronted maʿmūl — 5
sentences / 119 tokens, 22 entries, 5 paradigms, the note
`ma-la-laysa-wa-la-al-jins`. Four garbled spots of the lithograph are read
and declared: «كأن ذا ناب حقا» → the received shāhid كَأَنْ ثَدْيَاهُ حُقَّانِ, «الفاء
وهما» → فَيَجِبُ إِلْغَاؤُهَا, «لكونهما» → لِكَوْنِهَا, «إلا الأحمار» → إِلَّا الْحِمَارَ. Package
0.6.0: 6 chapters, 78 sentences, 1401 tokens, 456 entries. Endings-mode ḍabṭ:
ch4 183/183, ch5 269/269, ch6 117/117 — 100% on all three after rounds 37–38 (`patch31b`–`patch31f`).

**Rounds 37–38 (`patch31b`–`patch31f`) — the Iẓhār's own rules taught to the DabtEngine.** The
first probe read ch4 170/187, ch5 ≈225/263, ch6 108/117; thirty-two misses in sixteen families,
every one of them a rule the chapter itself states. (1) The NAMED particle: in وَبَعْدَ حَتَّى الْعَاطِفَةِ,
بِمَعْنَى لٰكِنَّ, لِاخْتِصَاصِ مَا الْمَصْدَرِيَّةِ the particle is MENTIONED, not used — a bare head before it
annexes the name (no tanwīn), the ال-naʿt or nisba after the name is in jarr, and the name opens
nothing (`__named31`, folded into the wave-28 `__quoted27` flag); a particle counts as named when a
pause, a naʿt, نَحْوُ or a joined second name follows it. (2) The LIGHTENED family (`lightened31`: the
letters without the shadda, with marks on the page, on a particle row): كَأَنْ / أَنْ before a noun
carry the ḍamīr al-shaʾn — the noun opens a nominal sentence (كَأَنْ ثَدْيَاهُ حُقَّانِ, عَلِمْتُ أَنْ زَيْدٌ قَائِمٌ);
after a verb of certainty لَا / قَدْ part أَنْ from its verb, which stays in rafʿ (أَنْ لَا تَقُومُ، أَنْ قَدْ
تَقُومُ); إِنْ before a verb with a lām within three words is no shart (وَإِنْ نَظُنُّكَ لَمِنَ الْكَاذِبِينَ),
and the lām-noun after kāna under it is the khabar (وَإِنْ كَانَتْ لَكَبِيرَةً); إِنَّ with its shadda
before لَا + verb nasbs nothing (فَلَا تَقَعُ). (3) إِنَّمَا governs nothing — the bare noun after its
verb is the doer. (4) The maṣdar of kāna governs: كَوْنُ اسْمِهَا نَكِرَةً. (5) The Ḥijāzī مَا loses its
work when its khabar comes first or إِلَّا breaks the negation (وَمَا قَائِمٌ زَيْدٌ، وَمَا زَيْدٌ إِلَّا قَائِمٌ
→ rafʿ), and the shart's jazm stops at a citation (لَمْ تَعْمَلْ، نَحْوُ: … وَلَا يَتَقَدَّمُ) unless a shart
particle with its own verb opens inside it; مَنْ at the head with a fāʾ-answer is the shart (مَنْ
يُكْرِمْنِي فَإِنِّي أُكْرِمُهُ). (6) The letter's NAME is a noun (بَعْدَ وَاوِ الْحَالِ — its wāw no joiner);
ثَمَّةَ joins the wave-30 mabnī ẓarfs; a counted noun, a noun after a jarr letter or a word the
lexicon owns wears no question-hamza (ثَمَانِيَةُ أَحْرُفٍ — the number family's misses were all
this one misreading); the endings page's لَـ + حِقْ is re-read as the māḍī the corpus owns
(وَلَحِقَهَا). (7) Seats: a ẓarf is never the relative clause's doer (وَقَعَتْ بَعْدَ فَاءِ الْجَزَاءِ); the
she-verb's named doer is never a jarr-fused noun (لَتَنُوءُ بِالْعُصْبَةِ) and an intransitive
she-verb's definite noun is its doer whatever its gender (تَبَيَّنَتِ الْجِنُّ); غَيْر right after kāna
before a ṣifa is the khabar (كَانَ غَيْرَ مُتَصَرِّفٍ) and after a definite jarr noun its naʿt (الْفِعْلِ
الْمُتَصَرِّفِ غَيْرِ الشَّرْطِ); the أَوْ-list follows the alif-marked item before it (شَرْطًا أَوْ دُعَاءً);
إِلَّا after a full affirmative sentence takes the mustathnā in naṣb (جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ);
a joined head after a pause before a particle opens a new sentence (، وَشَرْطُ عَمَلِهَا أَنْ); the
participle after the genus-lā's ism before a jarr phrase is the khabar (لَا غُلَامَ رَجُلٍ جَالِسٌ
عِنْدَنَا); the participle after a passive she-verb before نَحْوُ: is the deputy's ḥāl, and the joined
participle after the example rides onto it (وَفُتِحَتْ فَاعِلَةً نَحْوُ: … ، وَمَفْعُولَةً); the second
citation rides the wāw onto the first in its jarr (نَحْوَ قَوْلِهِ تَعَالَى … وَقَوْلِهِ تَعَالَى) and the cited
clause opens anew after the colon (وَالْخَامِسَةُ أَنْ); the addressee's كَ on the clause after a
tāʾ-verb makes the tāʾ the speaker's (عَجِبْتُ مِنْ أَنَّكَ قَائِمٌ). (8) Two engine repairs: the
annexation's `marksSay` now reads the author's own marks from `_orig24` (the endings page had
stripped them, so ضَمِيرِ شَأْنٍ was cut), and the dual of a doubled noun (حُقَّانِ, four bare letters
under a shadda) is recognised in `dualByLex` and in `writeNoun`. The sweep then showed five regressions, repaired in `patch31f`: a particle under a jarr clitic is in use, not named (ثِقَةً بِأَنَّ السَّامِعَ), and a head the author closed with tanwīn names nothing; the addressee's كَ reaches the tāʾ only on a bare إِنَّ-family word within three words (نَهَبْتَ … حَوَيْتَهُ … بِأَنَّكَ keeps the addressee); the she-verb's named doer is never a ẓarf and an intransitive's doer is definite itself (أَقَامَتْ مَعَ الرَّايَاتِ، بَقِيتَ بَقَاءَ الدَّهْرِ); the page's marks settle an annexation only on a head that can be annexed — not a diptote sifa (أَبْيَضَ مِخْذَمٍ), not a muntahā plural (نَمَارِقُ مَصْفُوفَةٌ), and a maqṣūr head counts (إِحْدَى الْكَلِمَتَيْنِ); the dual is read off the row's lemma only when the inner marks agree (حُقَّانِ yes, ذُكْرَانًا no); and the whole word the corpus owns as a noun outranks a clitic-plus-verb reading (بِنَاءُ الْبَيْتِ, which the new verb نَاءَ had captured). The targeted re-sweep after 31f: no regressions; Talkhīṣ ch56 s4, ch62 s6, ch64 s2/s17, ch65 s2/s4/s5/s10, ch76 s4 and the r21 ch64 floor (95.7 → 97.9) improved.

**`patch31g` — the author's marks belong to ONE sentence.** The chunk-6 smoke found Talkhīṣ ch48 s11 (وَكَأَنَّ الْبَرْقَ مُصْحَفُ قَارٍ) losing its كَأَنَّ frame: the pin analyses a sentence right after another sentence's `grade`, and the rules of 31c/31f that read `_orig24[j-1]` / `_orig24[i+1]` without a bare-word match were reading s10's marks under s11's indices. `decide(rows)` now drops `_orig24` when fewer than 60% of the rows match it bare for bare; `vowel()` sets it afresh on every call, so the grader loses nothing. Two more chunk-6 findings of the same run: the regenerated-paradigm audit refuses an uncontracted seam nūn (تَبَيَّنْنَ) — `sarf_gen.entry()` now writes the tables' idghām (تَبَيَّنَّ، تَبَيَّنَّا) and the Iẓhār's `tabayyana` was repaired; the qiyāsī-plural audit floor moved 175 → 178 for the three heard plurals ch4–6 added (ثَدْي → أَثْدَاء، كَارِه → كَارِهُونَ، كَنْز → كُنُوز).

**`patch31h` — a noun the lexicon owns WHOLE keeps its first letter.** The chunk-5 smoke's Qawāʿid gate (every seeded error caught, no alarm on correct Arabic) raised one false alarm on Talkhīṣ 72:s9 بِنَاءُ الْبَيْتِ — «jarr: what follows a jarr letter is majrūr». The cause was a lexicon side-effect of ch4–6: the Iẓhār's نَاءَ (ن و أ) joined the paradigms, and the analyzer's loose corpus walk (`findFormInParadigm` over `formCandidates`, which peels بِ/لِ/كَ too) matched بِنَاءُ to نَاءَ's māḍī cell; the row was published as a noun with the lemma نَاءَ, root ن و أ, and `QawaidEngine.fused()` then took the بِ for a jarr letter and flagged the ḍamma. Three guards, all asking the noun lexicon (`RootFinder.nounFromCorpus`) whether it owns the word WHOLE: `RootFinder._find` drops a whole-word verb hit reached through a peeled بِ/لِ/كَ/سَ candidate; the candidate loop refuses the same peel (it already refused the وَ/فَ one for فَسَادُ); `QawaidEngine.fused()` returns false before its lemma/root paths. Probed: بِنَاءُ → بِنَاء (ب ن ي), no alarm; بِعَرَضٍ، لِفِقْهٍ، كَكُلِّ، بِبَيْتٍ still fused; لِسَانُهُ، كَلَامُ، بِنَاءً keep their lemmas. The Qawāʿid gate run alone passes; the release was restarted from scratch (the reader's sha changed between chunks). Lesson: a glossary entry is a GLOBAL claim on the analyzer too — a new short verb (نَاءَ، آبَ، عَادَ) can be reached through a clitic peel from any longer noun, so a whole-word owner must always outrank a peel.

**`InnaEngine` (`patch31a`) turns the chapter's rule into a decision procedure.**
`verdict(rows, i)` looks at the SEAT of an إِنَّ-shaped word — the previous word,
the nearest governing verb within five words, the punctuation, a لَ on the
khabar within four words — and names one of Birgivī's places: the ten kasr seats
(`ibtida`, `qasam`, `sila`, `khabarAyn`, `lam`, `qawl`, `hattaIbt`, `tasdiq`,
`iftitah`, `wawHal`) plus the fāʾ of causation and the isti'nāf wāw, the fath
seats (`fail`, `maful`, `mubtada`, `khabarMana`, `mudaf`, `law`, `maTime`, `jarr`,
`hattaAtf`, `mudh`, and إِلَّا's `istithna`), the two that allow both (`faJaza`,
`hatta`), and `atf` (a wāw-joined particle inherits the previous clause's hamza,
across a sentence boundary too through `audit()`'s `prevTail`). Where no seat is
recognised the verdict is `both` and the engine says so — it never guesses. Three
things made the audit honest: NFC puts the vowel BEFORE the shadda (إِنَّ is ن َ ّ,
إِنِّي is ن ِ ّ), so the hamza test is `[إأ][َِ]?ن[َُِ]?ّ`; a jarr letter counts only
when it stands BARE (فِيهِ / مِنَّا / لَهُ before إِنَّ close a phrase and open a new
sentence); and a فَ-prefixed إِنَّ after a complete clause is the fāʾ of taʿlīl
(kasr) unless a shart word came first. The verbs of knowing and of saying are
read by STEM (`stem()` strips the conjugation affixes, `ILM_STEM` / `QAWL_STEM`),
so يَعْرِفُونَ أَنَّ and نَادَى إِنَّ are seen without a lexicon; the lām of ibtidāʾ is
trusted from an authored line (لَامُ الِابْتِدَاءِ / الْمُزَحْلَقَة) and from the shape in free
text, never after لَوْ (لَكَانَ is the answer's lām). `audit()` grades every authored
إِنَّ / أَنَّ in the corpus — the hamza LETTER the author wrote is the answer, quoted
particles (لَفْظٌ مَحْكِيٌّ) are skipped, كَأَنَّ / لٰكِنَّ / إِنَّمَا / أَنَّى are not إِنَّ: **271
particles, 246 decided by a seat (90.8%), 246/246 agree with the author (100.0)**;
the first cut measured 162/199 and 77% coverage, the misses were the jarr-phrase
false hits, the fāʾ of taʿlīl, the verb two words back (عَلِمَ النَّاسُ أَنَّ), the
vocative (يَا أَبَانَا إِنَّا) and the joined أَنَّ at a sentence's head. The lab
(`إِنَّ` on the workshop rail), Birgivī's sixteen seeds, the gInna game (only
particles where the seat and the author agree are asked, three options: kasra /
fatha / both) and the gates are in DESIGN.md §26. Smoke: the ch4 floor (97; the
quoted particles' لِ-khabars, the ism in naṣb and the khabar in rafʿ, the slid
lām, 28:76 and 8:5, the mabnī ثَمَّةَ), the nineteen seeds by seat, the audit floors
(n ≥ 200, coverage ≥ 85, accuracy ≥ 97), the lab on a phone + the game supply.

## Qiṣaṣ Part Four and Part Two — the sarf table's transitivity decides the doer (waves 32–33, v194)

Two more of the owner's Nadwī scans became stories. **Part Four** (`qisas-al-nabiyyin-4`,
`qisas4_common.py` + `author_qisas4_ch1–45.py`): Shuʿayb §1–13, Dāwūd and Sulaymān
§1–15, Ayyūb and Yūnus §1–7, Zakariyyā §1–8, ʿĪsā §1–42 — the whole book, print
pp. 1–70 of the Karachi 2008 edition, transcribed page by page with its ḍabṭ:
45 chapters, 401 sentences, 6789 tokens, 1891 glossary entries, 565 paradigms,
Level 3, in copyright and flagged so (the manifest's RIGHTS line, the chapter notes
that name every quoted āya as the print quotes it). **Part Two** (`qisas-al-nabiyyin-2`,
`qisas2_common.py` + `author_qisas2_ch1–4.py`): «سفينة نوح» §1–8, print pp. 8–15 —
after Ādam, the envy of Satan, his idea, his trick, the pictures of the righteous,
from pictures to statues, from statues to idols, the anger of God: 4 chapters, 59
sentences, 519 tokens, Level 1 like Part
One; the transcript of the whole volume (Nūḥ §1–22, الْعَاصِفَة §1–11, نَاقَةُ ثَمُود
§1–13) is in the scratchpad and the rest follows chapter by chapter.

**The segment audit** that the fourth volume forced: `segcheck.py` compares every
token's segments with its surface (consonant skeletons, with the corpus's
underlying-form allowances: لِ+ال, مِنْ+مَا, كُنْ+نَا) and found 41 slips in Part One
and 7 in the Talkhīṣ / Kāfiya — a wāw the i'rab named and the segments lacked, a
pronoun split one letter short; `qisas_common`'s wa-helpers are now conj-aware
(`conj_of / conj_full / conj_segs`: the فَ and the وَ read from the surface, the
segments written from it), `talkhis_common`'s kaq/kawa likewise, and
`validate_content.py` gates it corpus-wide ("segments '…' do not spell the surface").

**Rounds 39–50 (patch32a–32l)** — the engine learned from 6789 new tokens, and the
lesson of this wave is one principle made mechanical: **transitivity from the sarf
table**. A verb whose paradigm carries no ism mafʿūl and no majhūl (or whose gloss
is intransitive, or whose bāb is حَسُنَ / a reflexive form) is LĀZIM and takes no
object — so the definite noun after it, even past a jarr phrase, is its doer
(لَجَّ بِهِ الشَّيْبُ، ضَاقَتْ عَلَيْهِ نَفْسُهُ، اشْتَدَّ إِلْحَاحُ الْيَهُودِ، تَنَصَّرَ قُسْطَنْطِينُ،
شَاعَتْ لَهَا تَمَاثِيلُ); a mutaʿaddī verb already carrying its object pronoun has its
doer next (خَانَهَا عَقْلُهَا، لَا يُزْعِجُهُمْ شَيْءٌ) unless it takes two objects
(آتَانِيَ الْكِتَابَ، فَيُوَفِّيهِمْ أُجُورَهُمْ); the scan stops at a bare majrur head waiting
for its muḍāf ilayh (فِي مُعَامَلَةِ الزُّجَاجِ) and never takes آلَ before a name as the
hollow verb (اعْمَلُوا آلَ دَاوُدَ). Around it: the elative annexes the bare noun after
it (فِي أَقْرَبِ وَقْتٍ، أَكْبَرُ مَظْهَرٍ — a diptote muḍāf declines with kasra); the
pronoun-closed word the lexicon owns as a noun, after a bare head, is the muḍāf
ilayh and no māḍī (قُصُورِ نَظَرِهَا); the annexed sound plural writes its wāw
(صَيَّادُو الْأَسْمَاكِ); the sound plurals the lexicon owns whole (الْعَالَمِينَ) still
write ِينَ; the name behind its jarr letter is still the diptote (لِدَاوُدَ،
وَلِسُلَيْمَانَ); حَتَّى before a corpus māḍī is the ibtidāʾiyya (حَتَّى جَاءَ); سُبْحَانَكَ /
وَحْدَهُ / رَغْمَ fixed in naṣb; رَبَّنَا the dropped-يَا vocative before a plea, and the
plea's تَ as «you»; يَا عِيسَى ابْنَ مَرْيَمَ; the khabar after كُلِّ شَيْءٍ (وَهُوَ عَلَى كُلِّ
شَيْءٍ قَدِيرٌ، وَكُنَّا بِكُلِّ شَيْءٍ عَالِمِينَ); the delayed mubtada after a pronoun-closed
jarr phrase no verb governs (لَهُمْ عَذَابٌ شَدِيدٌ); لَدُنْ built on sukūn. Part Two's
first probes added the Level-1 seats: kāna's fronted jarr khabar and the naʿt of
its delayed ism (فَكَانَ فِيهَا رِجَالٌ كَثِيرٌ); the five nouns' wāw is rafʿ — a mubtada or
a doer, never an object (أَبُوهُمْ آدَمُ وَرَبُّهُمُ اللهُ); the noun annexed to a definite
is definite — no ḥāl — and before a second definite it is the doer (يَدْخُلُ ذُرِّيَّةُ
آدَمَ الْجَنَّةَ، وَيَدْخُلُ إِبْلِيسُ وَذُرِّيَّتُهُ النَّارَ); the fatḥa-lām of لَوْ's answer on
a māḍī (لَتَعَجَّبَ — the lām of command wears a kasra); the question hamza before a
muḍāriʿ the analyzer had read as a noun (أَنُشْرِكُ بِرَبِّنَا); the joined noun whose
pronoun points at the muḍāf ilayh is joined to the muḍāf (رِجَالُ اللهِ وَأَوْلِيَاؤُهُ);
the third person's لَا after a noun negates (حِجَارَةٌ لَا تَنْفَعُهُمْ). **The neighbour
sweep then paid for the wave's own rounds** (patch32k–32l): rounds 39–47 had never
been swept, and Kāfiya / Part One / Talkhīṣ showed eleven new misses — the lāzim
scan taking the verb's cognate-manner masdar (يُقْعِي جُلُوسَ الْبَدَوِيِّ), the
letters-only māḍī match swallowing a noun the lexicon owns with the same vowels (أَوْ
حَالِهِ), the relative's-object rule reaching a doer that closes the sentence (وَلَا
يَلْتَامُ مَا جَرَحَ اللِّسَانُ), the joined muḍāriʿ inheriting a doer that was NAMED
(يَأْتِي النَّصْرُ وَيُخْصِبُ النَّاسُ), a bare lāzim verb naming a new doer from a seat
that keeps the old one (إِنَّهُ خَانَ الْعَزِيزَ، أَنْ يَتْرُكَ الْأُمَرَاءَ), and the
two-definites rule on a poet's fronted object (أَعْدَى الزَّمَانَ سَخَاؤُهُ) — each
narrowed to its seat, and the sweep re-run clean before the gates. A token is one
printed word: the validator now refuses whitespace inside a surface (twelve
two-word tokens of Part Four — وَلَا تَنْقُصُوا، وَمَا قَتَلُوهُ — split into their words).

**Round 51 (patch32m) — the owner's report.** Typed into the workshop, «ان الله
غفور رحيم» drew غفور → رحيم as مُضَافٌ إِلَيْهِ on the İ'rab haritası. The DabtEngine had
read the sentence right (اسم إنّ، خبر إنّ، نعت); the arrow came from `IdafaEngine.chain`,
which on BARE text pairs noun to noun by shape alone (no tanwin to refute it), and
from the Shajara, which drew every chain link without asking the verdict. Three
edits: on an unvocalized head two adjective-shaped indefinites in a row (غفور رحيم،
عزيز حكيم، سميع عليم، رجل كريم) are a khabar and its naʿt, never an annexation
(`sifaPair32`, `DabtEngine.sifaShape` on both words, the member bare — no ال, no
name, no pronoun); a demonstrative never HEADS a chain (هٰذَا رَسُولُ اللهِ — it may
still be annexed to: مِثْلُ هٰذَا); and `Shajara.build` asks `DabtEngine.decide` once,
on a copy of the rows, whenever a chain's head wears no vowel, and draws a link as
idafa only where the verdict on the annexed word is `mudafIlayh` (or none) — the
vocalized corpus never pays for this, so the Shajara's corpus gate costs the same.
Smoke seeds: the four typed sentences, with and without vowels.

**Round 52 (patch32o) — the sweep's debts, bisected.** The neighbour sweep after
rounds 39–50 showed nine sentences worse than the wave-31 baseline; each was
bisected to its round with `bisect32m.sh` (v193 + a, +b, … on the same nine
sentences) and repaired at the source: 32a's relative-object rule read وَلَمَّا as
لِ + مَا (the shadda on the mīm now names لَمَّا: وَلَمَّا رَأَى يُوسُفُ، سَمِعَ الْمَلِكُ،
بَلَغَ إِبْرَاهِيمُ); 32b's two-joined-muḍāriʿ rule measured the gap from the CURRENT
verb, which is always empty — it now finds the previous verb, wants no doer named
between them and no majhūl before (فَيُصْلَبُ فَتَأْكُلُ الطَّيْرُ، يَأْتِي النَّصْرُ
وَيُخْصِبُ النَّاسُ); 32l's clause-opening seat admits the lightened لٰكِنِ before a
verb (وَلٰكِنِ اشْتَدَّ إِلْحَاحُ الْيَهُودِ); 32b's إِنَّمَا rule leaves the doer to a verb
already carrying its object (إِنَّمَا خَانَهَا عَقْلُهَا); the jussive kāna never heads a
chain (وَلَمْ يَكُ أَكْثَرَ الْفِتْيَانِ); 32g's two-definites rule yields to an ال-naʿt
and to an intransitive verb, and the posture glosses count as one manner
(يُقْعِي جُلُوسَ الْبَدَوِيِّ الْمُصْطَلِي); a three-letter «māḍī» between a bare annexing
noun and a definite noun is the construct head the lexicon owns — the fourth
volume's حَالَ had claimed تَشْبِيهُ حَالِ الدُّنْيَا, and the same noun with its pronoun
joined by أَوْ to a pronoun-closed noun (أَوْ حَالِهِ) is the noun. The gate chapters
(r21 / r22) added five more: 32a's naʿt-after-a-bare-jarr-noun rule spares a lexicon
NOUN whose gloss names no quality and the word after a frozen one (لِي مِنْ فُلَانٍ
صَدِيقٌ حَمِيمٌ — the delayed mubtada); 32a's nisba-yāʾ reading never takes a majhūl
(سُمِّيَ فَصْلَ الْخِطَابِ keeps its verb); after يَا no word is a verb (يَا خَاطِبَ
الدُّنْيَا — the fourth volume's خَاطَبَ had claimed it); a host closed by a kasra
before هِ is the noun with its pronoun, never a māḍī with its object; 32h's
two-definites rule yields to an intransitive verb and to a naʿt behind a
pronoun-closed doer (مَا طَالَتْ قَرِينَتُهُ الثَّانِيَةُ). A second bisect pass on the
sweep after those fixes found six more, each traced to its round and closed at
the source: هَدَى takes two objects (اهْدِنَا الصِّرَاطَ الْمُسْتَقِيمَ — 32e's
object-pronoun doer had taken the path as the doer); the quotation after كَقَوْلِ X
opens on its mubtada (كَقَوْلِ الْوَطْوَاطِ فَوَجْهُكَ كَالنَّارِ — a فَ-joined noun with
its pronoun or ال after the cited poet, not his naʿt); a MĀḌĪ right after كَانَ keeps
her seat open for the delayed ism (مَا كَانَ خَاطَ عَلَيْهِمْ كُلُّ زَرَّادِ — 32c's
"a verb after kāna is never kāna" and 32a's "the verb after kāna is her khabar"
both narrowed to the muḍāriʿ, which is the only reading in which كَانَ يَتَكَلَّمُ
was ever meant); the called one after يَا stays a noun at the seat even when the
page's marks had re-sworn it a verb (the fourth volume's خَاطَبَ against the
author's خَاطِبَ — the marks block sets `__nida32`, the case loop's head drops the
verb cell); and the amr's first cell is أَنْتَ, not هُوَ, so an object-pronoun amr
takes no named doer (قُلْتُ: دَعْنِي، وَجْهُكَ الْجَنَّةُ — 32e had read the face as the
doer of «let me» and the garden as its object). The final probes then caught
two of the gate-chapter fixes over-reaching on the fourth volume, and both were
narrowed: "intransitive" had been read off the FIRST sense of a verb's gloss, so
تَحَقَّقَ «to be certain of, to verify» lost its object (يَتَحَقَّقَ الْحُكَّامُ …
حَقِيقَةَ الْأَمْرِ) and دَخَلَ «to enter» lost its doer (يَدْخُلُ ذُرِّيَّةُ آدَمَ الْجَنَّةَ)
— `intransAll32` now wants EVERY «to …» sense intransitive and never counts the
place-object movers; and the lexicon-noun spare in the naʿt rule had believed the
glossary's `pos`, which tags every adjective "noun" (فَاسِد، أَجْنَبِيّ، جَائِر) — `nounGloss32`
reads the English and Turkish glosses for a mark of quality (ism fāʿil, nisba,
ṣifa, ism-i fâil, sıfat…) and a short list of plain adjectives, so مِنْ أَخْلَاقٍ
فَاسِدَةٍ and فِي لُغَةٍ أَجْنَبِيَّةٍ keep their naʿt while لِي مِنْ فُلَانٍ صَدِيقٌ keeps its
delayed mubtada. The lesson is recorded here because it will recur: the glossary
has no adjective class, so an engine rule may never infer "noun" from `pos`
alone. An all-floors gate (`$SCR/gates_all.sh`, every Talkhīṣ chapter 48–76 in
endings mode exactly as the smoke measures it) then showed ch63 at 94.9 against its
floor of 96 — and 95.7 even on the v193 engine once the fourth volume's lexicon was
loaded: the new verb دَارَ had taken دَارُ الْخُلْدِ. The delayed mubtada after the
khabar-muqaddam's jarr phrases is now read in both homograph blocks: a three-letter
«māḍī» the lexicon also owns as a noun, right after a jarr+pronoun word (لَهُمْ،
فِيهَا) and right before an ال-noun, is that noun, annexed (لَهُمْ فِيهَا دَارُ الْخُلْدِ).
One content slip stays documented: the fourth volume's authoring dropped the year's
digits after سَنَةَ (تَنَصَّرَ قُسْطَنْطِينُ الْكَبِيرُ سَنَةَ ٣٠٦), so the ẓarf stands annexed
to nothing and the grader reads it as an object — the digits belong in the token
stream, which is a content task, not an engine rule. The same gate's sentence-by-sentence
diff against the v193 engine found ch63's other debt in round 43: 32e's "the indefinite
after a pronoun-closed jarr phrase that no verb governs is the delayed mubtada" (لَهُمْ
عَذَابٌ شَدِيدٌ) had looked back only four words for a verb, so يُنْتَزَعَ مِنْ أَمْرٍ ذِي صِفَةٍ
أَمْرٌ آخَرُ مِثْلُهُ فِيهَا مُبَالَغَةً opened a nominal clause at مُبَالَغَةً. The rule now
asks the seat's own state: a doer or nāʾib seated between the clause's verb and this
word closes the way (the nāʾib أَمْرٌ), while the mubtada's own verb does not
(وَكُلُّ مُجْرِمٍ يَتَنَصَّلُ مِنْ جَرِيمَتِهِ وَكُلُّ مُجْرِمٍ لَهُ صِيَاحٌ keeps its two
mubtadas). Three tries went into that guard — `st.subject` is not set by the nāʾib rule,
`st.failRow` neither — and the lesson is the same as always: read the trace, not the
field names. The same gate had ch67 one token under its floor of 98 (98.1 on the
v193 engine): round 41's «يَا قَوْمِ even when a chain claimed it» (32c — the kasra of
the dropped yāʾ, the chain undone) had taken يَا ظَبَيَاتِ الْقَاعِ, where the kasra is
the sound feminine plural's naṣb before its annex; the dropped-yāʾ reading now
steps aside when a definite noun (ال, a name) with no jarr letter and no pronoun
stands right after the called one — يَا قَوْمِ أَرَهْطِي keeps its kasra because رَهْطِي is
pronoun-closed and annexes to nothing. Last, the smoke generator's own regress
list (a chapter under its v193-engine figure) named three chapters of the fourth
volume, and the a–l bisect on the base engine put all four sentences on rounds 39
and 40: the relative's-object rule (32a) and the ṣifa-clause rule (32b) read the
Name as the object whenever a definite noun followed a transitive verb — شَرَحَ اللهُ
صَدْرَهُ، أَكْرَمَ اللهُ بِهَا سَيِّدَنَا، وَمَا كَفَرَ سُلَيْمَانُ. Both rules now ask
`laterObject32`: a definite or pronoun-closed noun further on, past the jarr phrases,
is the object, so the noun right after the verb is the doer (the rule's own candidate
may itself stand behind a jarr-pronoun, وَمَا شَرَحَ لَهُ صَدْرَهُ, and that is honoured);
and a sentence-initial مَا before a māḍī is the negation, not the relative. The
fourth — round 40's joined() learning the wāw before a wāw-initial lemma
(وَوِلَادَتُهُ) — was right about the wāw and wrong about the seat: a joined
pronoun-closed noun after a complete nominal clause, followed by a bare ṣifa-shaped
noun agreeing with it (the host's tāʾ before the pronoun counts as the tāʾ marbūṭa),
opens a new nominal clause, وَوِلَادَتُهُ خَارِقَةٌ لِلْعَادَةِ, no ʿaṭf.

**Round 53 (patch32q) — the sarf audit bites the new volumes.** The release's smoke
(chunk 2) failed on «the Sarf engine regenerates every stored paradigm it can
classify»: seventeen of the fourth and second volumes' stored paradigms disagreed
with `sarfDerive`. Read cell by cell, fifteen were the AUTHORING's slips and the
engine was right — the hollow verb's amr before a vowel-initial suffix keeps its
long vowel (تُبْ but تُوبَا، تُوبُوا، تُوبِي; زِيدَا، أَمِيلَا، عِيلَا، أَثِيرَا، مِيلَا،
اِنْهَالَا، صِيحَا، ذُوبَا، شِيعَا، قُودَا), a tāʾ-final root merges with the subject's tāʾ
in the māḍī (أَنْبَتَّ، أَنْبَتُّمْ، كَبَتُّ، نَحَتُّمَا), and the madd wāw after a ḍamma wears
no sukūn (يُودِعُ). Those rows were rewritten from the engine's own derivation
(`$SCR/fix_morph32b.py`, package and dry package alike). Two were the engine's:
the mithāl's wāw in bāb فَعِلَ يَفْعَلُ is kept by rule (وَجِلَ يَوْجَلُ) except the recited
few whose muḍāriʿ opened on a guttural — وَسِعَ يَسَعُ، وَطِئَ يَطَأُ، وَلِغَ يَلَغُ — and
Form VIII on a ذ-initial root has two recited spellings, اِذَّكَرَ and اِدَّكَرَ — the engine
keeps اِذَّ (the smoke's own canon from the İzzî), and the audit now reads the print's
اِدَّخَرَ as its twin instead of a mismatch. The audit is at 0 on 989 verbs. The same chunk's
Root Finder lab check read the output 260 ms after typing; the Relax drips now share
the main thread, so the check waits for the root (`waitForFunction`, 8 s) instead —
and the next rerun failed the SAME way on the Ism lab (مَجْلِس from جلس), so every lab
check that types and sleeps (ism, conjugator, mīzān, the second ism) now waits for its
own render. Rule for future smoke checks: never read a debounced lab after a fixed
sleep; wait for the text. The next chunk found a real one: Relax's shop count
(`shopCandidates`) had dropped the old pool's scope fallback, so a story whose
sentences carry no readable iʿrāb line counted 0 and the figure game closed its door
(patch32r: below three customers the count falls back to the shelf, as the pool
always did). Chunk 5 then found two more that only the new volumes could expose:
the fourth volume's verb رَجَمَ gave the analyzer a dual cell تَرْجُمَانِ, and the
rhyme-sukūn leniency let إِلَى تَرْجُمَانْ (the interpreter, Talkhīṣ ch44) pass as that
verb — a written final sukūn against a cell closed by the dual or plural nūn's
vowel, with the noun in the corpus, now keeps the noun (patch32r_c); and the sarf
corrector's first step asked the corpus index for ONE bare-letter hit, so حَرْنَ
(the amr of حَارَ) was "corrected" to a sound حَرَنَ because another lemma answered
first — it now vouches for any exact stored cell (patch32r_b, an exact-form map built
once). One more authoring slip surfaced on the way, اِسْتَرِحِي for اِسْتَرِيحِي (the
Form X hollow the audit could not classify), rewritten by hand. Chunk 6's plural
audit then counted 200 stored plurals the qiyāsī builder disputes against the pin of
178: the twenty-three new ones are the two volumes' HEARD plurals (قُرُون، دُرُوع،
رُؤَسَاء، أَعْضَاء، صُحُف، شُعُوب، أَطِبَّاء، أَنْصَار، زُعَمَاء، خِرَاف، زُمَلَاء، مَآسٍ …), each
reviewed, so the pin moves to 200 with its reason in the check — and two of the
builder's own guesses are gaps worth a round of their own: أَعْضَاو for أَعْضَاء (the
wāw-final root under أَفْعَال takes the hamza) and مَأَاسِا for مَآسٍ (the hamza-initial
root under مَفَاعِل wants the madda and the manqūṣ close).
The lesson for authoring: a stored paradigm is a claim the engine will contest, so
author scripts should derive the weak classes rather than type them. Two misses the fourth
volume's lexicon introduced stay documented, not fixed: فَدَارِهِ (the amr of دَارَى,
which `verbByBare` cannot see past the new māḍī دَارَ once endings mode has
stripped the kasra) and ذَلِكَ أَنْ تَكُونَ الْأَلْفَاظُ تَوَابِعَ (kāna's ism read as
her khabar only behind the demonstrative) — both inside their chapters' floors.
The lesson for the next wave: a rule that names a neighbour by REGEX must say
which particle it excludes (لَمَّا is not لِمَا), a rule about "the previous verb"
must look for it, and every new verb a volume brings is a new homograph for every
older text — the sweep must include the gate chapters, not only the neighbours.

**The reviewer's notes and the offline bundle (patch32n, `tools/build_review_bundle.py`).**
The owner asked for a build friends can revise offline. The reader needs no
network (no CDN, no fonts, no API), so an offline build is the file itself; what
was missing was a way to SEND NOTES BACK. `ReviewNotes` (before `renderStory`):
a ⚑ on every sentence's tool row opens a form under the sentence — the kind
(✓ correct · harakat · i'rab · translation · word meaning · spelling · other), the
word it concerns (a select over the sentence's tokens), the problem, the
correction; notes live in `localStorage["qissa-review"]` keyed story / chapter /
sentence, with the sentence's text, translation, chapter and the reviewer's name;
the Progress sheet grows a ledger (`statsHtml` / `bind`): the on/off switch, the
name, export (a `qissa-review-<name>-<date>.json` download), copy as text (one
block per note for a chat message), import (a friend's file, merged and listed
with "Imported · name", de-duplicated by sentence + reviewer + time), delete,
and jump-to-sentence (`goto`: opens the story, scrolls the section, opens the
form). `REVIEW_BUILD` is a build-time constant: `build_review_bundle.py` copies
`prototype/reader.html` with it flipped to true (notes on from the first open,
`storyLocked` returns false so every story is open to the reviewers), adds the
manifest, service worker and icons, and a README in English and Turkish, into
`dist/qissa-review-<sw-version>.zip` (`dist/` is git-ignored; the zip is sent to
the owner, not committed). In the ordinary reader the notes switch on from
Progress. Strings in both languages (`rev*`); the smoke check saves a note on a
sentence, exports, re-imports, finds it on Progress, jumps back, and reads the
Turkish labels.

**Relax — paint first, count later, remember per build (patch32p).** The owner's
phone could not open the Games hub or the Atölye. Measured cold on the desktop:
`openGames` 48 s (205 s under 4× CPU throttling) — the İ'rab-shop pool ran
`DabtEngine.vowel` on sentence after sentence before one card painted (38 s), the
jinas pool read every seed (7 s); the model and jumla labs cross-validated on open
(2.9 s + 1.7 s), the perceptron re-trained on every fresh load (2.9 s). One principle
fixed all of it, and it is now the rule for anything that is a FUNCTION OF THE BUILD:
`Relax` (before `GameFactory`) — `get/set` a memo with a localStorage mirror keyed
by the build (story count + sentence count + `document.lastModified`, other builds'
keys swept at start), `later(key, fn, render)` (render the placeholder now, the value
in a later task, cached), `chunked(items, step)` (slices of 10 ms). Then:
`GameFactory.supplyOf` remembers per scope and build (`supplyKnown` answers without
computing; the two vocabulary drills that follow the learner's deck are not stored);
the hub paints every card at once with «…» where the count is still owed and fills
them one game per slice (`.g-wait`), then warms the two slow pools in a drip; the
shop pool counts CANDIDATES (a sentence whose author wrote an i'rab line the shop can
read — milliseconds) and reads the engine's table only for the few sentences a round
needs now, the rest in a 400 ms drip that pauses during a round, the items remembered
as light references (`senRef32`); the jinas pool reads what a round needs and drips
the seeds and the corpus (a frame carries a closure, so it is not stored); the model
and jumla scores, the taggers' line and the Inna tally fill in after the panel paints
and are remembered; the perceptron's 55 KB of weights are stored per build. Measured
after: the hub paints in 11 ms and its counts arrive in under a second; the labs paint
in tens of milliseconds; after a reload every count and score is a lookup. The smoke
checks that read a score or a tally now WAIT for the digits (`patch32p_smoke`). The
rule for the next engine: a count or an audit is never computed on the open path —
it is painted as owed, computed in a slice, and remembered.

Measured in endings mode on every sentence: Part Four 5972/6505 = 91.81% before the wave's
rounds → 6130/6516 = 94.08% after them, no chapter regressing; Part Two 497/501 = 99.20%. The
neighbours (Kāfiya, Part One, Talkhīṣ, the seeds, the r19/r21/r22 drills,
`sarfAudit`) swept clean. Smoke: a Part Four gate (45 chapters, 401 sentences,
Level 3, per-chapter floors from the measurement, the quoted āyas flagged, the
RIGHTS line present) and a Part Two gate (4 chapters, Level 1, floors), the
segment gate in the validator, the Shajara's four typed sentences (no idafa arc
on two adjectives, one on رَسُولُ اللهِ), the reviewer's notes end to end. The engines and the games (gDabt, gGhost, the
İ'rab Mağazası) read the new stories through the same `STORIES` feed — nothing
is special-cased: a Level-1 sentence of Nūḥ and a Level-3 period of ʿĪsā go
through the same decide() and the same rules.

## Qiṣaṣ Part Two chapters 5–8 — the volition verb's hidden doer, and rounds 53–54 (wave 33, v195)

Four more chapters of «سفينة نوح» (`author_qisas2_ch5–8.py`, print pp. 15–23, §9–14):
the messenger — a human or an angel (ch5, 15 sentences), Nūḥ the messenger and what
the people answered (ch6, 16), between Nūḥ and his people (ch7, 9, with 7:59–62
quoted as the print quotes them), «اتَّبَعَكَ الْأَرْذَلُونَ» (ch8, 12, with 26:111,
26:114–115, 11:30). Part Two now carries 8 chapters, 111 sentences, 1139 tokens,
308 glossary entries, 107 paradigms, still Level 1, still in copyright and flagged
so. New lexicon keys of this stretch: `lima`, `limadha`, `shafiq`, `riyasa`,
`sadiq-friend`, `amma-tafsil` (أَمَّا), `ardhal` (أَرْذَل / أَرَاذِل), `tarid-expeller`,
`in-nafiya`; the print's وَلٰكِنْ نُوحًا is kept as printed and the validator
accepted it (the lightened لٰكِنْ before a naṣb noun is the print's reading, not
ours to correct).

**Rounds 53–54 (`patch33a`–`patch33g`) — sixteen rules the Level-1 prose forced,
all probe-first, none on the neighbours' backs.** The four chapters measured
198/199, 163/163, 129/129, 113/113 in endings mode after them (ch5 s5 اللهُ after
إِلَّا مَنْ أَرَادَ is a true ambiguity we leave to the reviewer).

1. **The nahy لَا and the five-verbs.** وَلَا تَذْكُرُونَهُ keeps its nūn: the nahy rule
   jazms only when the verb, with its enclitic and its wāw/fāʾ stripped, does not end
   in ون/ين/ان — a لَا before a five-verb form in a statement is the لَا of negation.
2. **The same-subject verbs and أَنْ.** After يَقْدِرُ / يَسْتَطِيعُ / يُرِيدُ … أَنْ the
   muḍāriʿ's doer is the governing verb's own: `SAME_SUBJ33` marks the row, and a
   joined muḍāriʿ within four rows of it (no doer noun between) wears the hidden doer
   — وَلَا يَقْدِرُ أَحَدٌ أَنْ يَرَاهُمْ وَيَسْمَعَ, no new fāʿil for يَسْمَعَ.
3. **The sayer after قَالَ in a كَانَ frame.** وَإِذَا كَانَ الرَّسُولُ مَلَكًا قَالَ النَّاسُ: a
   definite noun or a name right after قَالَ/يَقُولُ is the sayer, not the earlier
   subject carried over — except the quoted-content nouns (الْحَقَّ، كَلِمَةً، شِعْرًا …),
   which stay objects.
4. **The oath that is a mubtada.** وَاللهُ يَعْلَمُ: a وَاللهُ right before a muḍāriʿ (not
   a lām-verb, not a heavy nūn) is no oath but the subject — in the pre-pass and in the
   noun rule (`patch33e`, the rule of wave 22b yielded).
5. **The volition verb's own doer.** أَرَادَ اللهُ أَنْ يُرْسِلَ: `VOLITION33` (أَرَادَ, أَحَبَّ,
   حَرَصَ …) gives the أَنْ-verb a hidden doer only when the governing verb's own doer
   does not stand after it (`ownDoer33`: a definite/propn/enclitic noun in the next two
   rows) — أَرَادَ اللهُ أَنْ يَعْرِفَ النَّاسُ keeps النَّاسُ as the doer of يَعْرِفَ.
6. **The ism-fiʿl line refuses tanwīn and refuses آمِين after a noun** (أَمِينًا is a
   ḥāl / khabar, never the «amen» interjection).
7. **أَنْ + amr.** أَوْحَى إِلَيْهِ أَنْ أَنْذِرْ قَوْمَكَ: the wave-24p re-typing of an amr to a
   māḍī after أَنْ is refused when the inner marks of the print's form disagree with
   the māḍī cell (`marksDisagree9`) — the أَنْ here is the explanatory أَنْ.
8. **The kin-noun iḍāfa.** قَالَ أَصْدِقَاءُ نُوحٍ: a bare kin/plural noun (أَوْلَاد، أَصْدِقَاء،
   قَوْم، أَهْل، بَنُو …) ruled fāʿil/mafʿūl/ism/khabar takes the name after it as
   muḍāf ilayh (`KIN33`).
9. **The tanwīn word is never enclitic-split.** أَمِينًا was read as أُمّ + نَا by the
   enclitic guess; a word wearing tanwīn carries no pronoun (`__noEnc33`: the
   segments, construct and enclitic reset, the lemma re-read from the corpus).
10. **The jarr clitic on an unsettled verb-shaped host.** بِأَيْدِيهِمْ: a host that
    the analyzer could not settle, with a جَرّ letter and a lexicon noun beneath it,
    is the noun after its letter (`__jarrClitic`), not a verb.
11. **لَيْسَ in the kana family.** إِنَّ بَابِي لَيْسَ بَابَ مَلِكٍ: the wave-26q innaIsm rule
    now lists لَيْسَ / لَيْسَتْ with كَانَ / صَارَ / يَكُونُ, so the ism of إِنَّ is also the
    ism of لَيْسَ and the noun after it its naṣb khabar.
12. **The joined subject before أَنْ.** وَشَغَلَتْهُمْ أَمْوَالُهُمْ وَأَوْلَادُهُمْ أَنْ يُفَكِّرُوا:
    an enclitic noun right after an object-pronoun verb that already has its object,
    followed by أَنْ, is the delayed fāʿil; the same-pronoun noun joined to it is its
    ʿaṭf (the analyzer's unsplit wāw split here).
13. **The joined-wāw fallback.** `joined()` was false for the analyzer's وأولاد+هم; the
    ʿaṭf rule now also accepts a وَ/فَ prefix whose host-minus-wāw is a lexicon noun and
    splits the segment itself.
14. **The demonstrative's object.** أَنْ يَطْرُدَ هٰؤُلَاءِ الْمَسَاكِينَ: a definite noun after
    a demonstrative that follows a transitive, object-less, non-passive, non-qawl 3ms
    verb (nothing but a stop or particle after it) is the badal of the object; the
    verb's doer stays OPEN (not hidden: the badal-doer rule leaves the same state, and
    a joined māḍī after it then keeps the right to its own doer — وَضَعَ هٰذَا الْإِنَاءَ
    … وَأَذَّنَ مُؤَذِّنٌ). The lanes found the refusals the rule needs: a FEMININE verb
    agreeing with هٰذِهِ/تِلْكَ names its doer (لَقِيَتْ هٰذِهِ الْأُمَمُ، رَجَعَتْ هٰذِهِ
    الْبِعْثَةُ), and a مَا/مَنْ before the verb is already its object.
15. **The volition verb's doer named after it (`patch33g`).** أَرَادَ إِبْرَاهِيمُ أَنْ
    يَفْهَمَ الْمَلِكُ، وَيَفْهَمَ قَوْمُهُ: when the volition verb's own doer stands after it
    and the أَنْ-verb is followed by an ال-noun, that noun is the clause's own doer
    (`ownDoer33`'s second arm); with the doer hidden (إِنَّ نُوحًا يُرِيدُ أَنْ يَنَالَ
    الرِّيَاسَةَ) the ال-noun after the أَنْ-verb stays its object.
16. **«to hurry», «to rush» are intransitive senses (`patch33g`).** أَسْرَعَ هٰذَا
    الرَّجُلُ إِلَى بَابِ السِّجْنِ: the sarf table generated a majhūl for أَسْرَعَ, so the
    demonstrative's-object rule read the verb as transitive; `INTRANS` now lists the two
    senses, and the transitivity test reads every gloss sense as before.

Two content repairs outside the story: `nala` (نَالَ) in the Badʾ al-Amālī and
Mukhtaṣar al-Manār morphology carried no ism mafʿūl / majhūl, so the sarf table read it
as lāzim and the doer rule refused its object — مَنِيل، نِيلَ، يُنَالُ added
(`fix_morph33.py`); the rule stands: **a verb's transitivity is read off its own
paradigm, so a paradigm without a majhūl is a claim of intransitivity**.

Smoke: the Part Two gate grows to ch1-8 / 111 sentences with per-chapter floors from
the measurement (ch1 100.0, ch2 99.3, ch3 99.1, ch4 99.2, ch5 99.5, ch6–8 100.0) and
twelve rule assertions on real sentences (the sayer النَّاسُ, the five-verb
تَذْكُرُونَهُ, the oath-mubtada وَاللهُ, أَمِينًا, أَنْذِرْ, نُوحٍ after أَصْدِقَاءُ, ضَلَالَةٌ
after لَيْسَ بِي, بِأَيْدِيهِمْ, وَأَوْلَادُهُمْ, الْمَسَاكِينَ, بَابَ after لَيْسَ) — the gate
reads `DabtEngine.grade().words[i].ok/k`, so a rule that slips is named, not just
counted. The JamEngine corpus-audit ceiling moves 200 → 201: أَصْدِقَاءُ نُوحٍ brought the
heard plural أَصْدِقَاء of صَدِيق into the story's glossary beside the builder's أَصْدِقَة. The neighbours (the Talkhīṣ/Kāfiya/Part One sweep, Part Four's forty-five
chapters and Part One's twenty-four against the unpatched reader, the seeds, r21/r22,
`sarfAudit`) swept WORSE 0.

## Qiṣaṣ Part Two chapters 9–11 — the argument of the rich, the call, the prayer, the ship, and round 55 (wave 34, v196)

Three more chapters of «سفينة نوح» (`author_qisas2_ch9–11.py`, print pp. 23–28, §15–18):
the argument of the rich and the call of Nūḥ (ch9, 20 sentences — «had it been good they
would not have preceded us to it», 46:11; 71:2–4 as one quotation, so the jussive answer
يَغْفِرْ sees its command), the prayer of Nūḥ (ch10, 13 — a thousand years less fifty; 11:36;
11:32; «O God, leave not on the earth anyone of the unbelievers»), the ship (ch11, 14 — the
mockery of the carpenters and the smiths; 11:38). Part Two now carries 11 chapters, 158
sentences, 1584 tokens, 394 glossary entries, still Level 1, still in copyright and flagged
so. New paradigms: `jarraba` (B2), `zala` (hollow wāw; the note keeps it apart from مَا زَالَ
of the kāna family), `aqala`, `aghraqa` (B4), `naja-escape` (nāqiṣ wāw), `amara-command`
(its amr مُرْ), `sanaa`, `sakhira`; the keys `naja`, `amara`, `an`, `tayyib`, `tabi` were
already claimed by other words (نَعْجَة، أَمَارَة، أَنْ، الطَّيِّب، تَابِع) — a key is a global
claim, so the new ones carry a suffix (`naja-escape`, `amara-command`, `an-prep`,
`tayyib-good`, `tabaa-followers`).

**Round 55 (`patch34a`–`patch34d`) — four cuts, all probe-first; the fourth is the lanes' repair.** The three chapters
measure 195/196, 123/123, 111/111 in endings mode after them (ch9 s12 الْأَمْطَارَ after
أَرْسَلَ عَلَيْكُمُ is the one ambiguity left: the sender is the previous sentence's God).

1. **The relative's doer after the ʿāʾid.** الَّذِي يَدْعُو إِلَيْهِ نُوحٌ: inside a relative
   clause, a verb followed by a jarr letter + pronoun (the returning pronoun) takes the next
   definite noun as its DOER — the object seat is the relative's own.
2. **The amr with the nūn of protection.** وَاتَّقُوهُ وَأَطِيعُونِ: a wāw-joined ون-word after
   an amr, whose host + ا is an amr cell of the corpus, is that amr wearing the nūn of
   protection with the speaker's yāʾ elided; it keeps its written form (the wave-26e
   wiqāya trim now accepts …ونِ beside …ينِ).
3. **Inna's bare ism annexes.** إِنَّ أَجَلَ اللهِ إِذَا جَاءَ: an ism of إِنَّ without ال, pronoun,
   tanwīn or a sound-plural ending annexes the definite noun after it — and أَجَل after
   إِنَّ / a jarr letter is the noun «term», never the answer-particle أَجَلْ the
   particle list would make of it.
4. **مَتَى under a jarr letter.** إِلَى مَتَى يَرَى الْحِجَارَةَ تُعْبَدُ: the analyzer already re-read
   مَتَى under إِلَى as the question (wave 26r), but the shart-noun frame of decide() still
   jazm'd the second verb; the frame now yields to `istif-ism`.
5. **The verbs of continuing and beginning.** بَقِيَ right before a muḍāriʿ (as before
   «noun + muḍāriʿ», wave 26n) and بَدَأَ / أَخَذَ / شَرَعَ / طَفِقَ / جَعَلَ before «noun +
   muḍāriʿ» open the kāna frame; the khabar verb carries the 26l mark and does the ism's
   act, so قَوْمَهُ and سَفِينَةً after it are its objects.
6. **The opening number.** أَلْفَ سَنَةٍ إِلَّا خَمْسِينَ عَامًا اللهُ أَكْبَرُ: a sentence-opening
   number annexed to a bare noun and followed by إِلَّا is the ẓarf of an understood verb
   (the exclamation repeats مَكَثَ …); the excepted after إِلَّا takes naṣb, the number's
   list-state is cleared, and the mubtada is still to come.
7. **لَا of prohibition after a vocative and after لَكَ.** اللّٰهُمَّ لَا تَتْرُكْ, رَبِّ /
   رَبَّنَا لَا …, and نَقُولُ لَكَ لَا تَجْلِسْ (لَكَ / لَكُمْ behind a verb of saying).
8. **رَآهُ joined.** وَرَآهُ قَوْمُهُ: the analyzer knows رَآهُ but not وَرَآهُ; the pre-pass reads
   the wāw-joined رَآ + pronoun as the defective رَأَى with its object, kept as written, the
   doer following.
9. **The addressee's tāʾ.** وَلٰكِنَّكَ مَا سَمِعْتَ كَلَامَنَا وَجَلَسْتَ: a tāʾ-verb right after
   إِنَّكَ / لٰكِنَّكَ / لَعَلَّكَ (over مَا / لَا / قَدْ) is the addressee's — سَمِعْتَ, not the
   speaker's سَمِعْتُ that the كَلَامَنَا «we» would otherwise win — and a wāw-joined tāʾ-verb
   after it is the addressee's too.
10. **فَإِنَّ in the answer slot.** إِنْ تَسْخَرُوا مِنَّا فَإِنَّا نَسْخَرُ مِنْكُمْ: the verb after
    فَإِنَّ (heavy nūn) is inna's khabar in rafʿ; the shart frame no longer jazms it.
11. **The joined māḍī before أَنْ.** وَأَجَابَ اللهُ … وَأَرَادَ أَنْ يُغْرِقَ قَوْمَهُ: a wāw-joined
    māḍī right before أَنْ inherits the previous verb's NAMED doer (the 26l inheritance asked
    for an unnamed one), so the volition rule of wave 33 can give the أَنْ-verb its hidden doer.
12. **The subject search steps back over a question.** فَإِلَى مَتَى يَنْتَظِرُ نُوحٌ؟ إِلَى
    مَتَى يَرَى فَسَادَ الْأَرْضِ؟: the «subject named earlier» frame walks back over the
    question word and its jarr letter, and accepts a plain doer (rule `fail`) when the verb
    stands right after a question word — an UNJOINED one: كَيْفَ يَغْلِبُ الشَّيْطَانُ وَكَيْفَ
    يَلْعَبُ الشَّيْطَانُ بِالْإِنْسَانِ (Part One ch8) repeats the question with a wāw and names
    its own doer again (34d).
13. **The carried tāʾ reads the previous verb, not the state.** The 34c carry of the
    addressee's tāʾ first read `st.person`, which the verb block had already set to the
    CURRENT verb's cell (6, the ambiguous ت cell) — so لَقَدْ أَبْلَغْتُكُمْ … وَنَصَحْتُ لَكُمْ,
    ظَلَمْتُ نَفْسِي وَأَسْلَمْتُ and قَتَلْتُ رَجُلًا وَتَرَكْتُ رَجُلًا (Parts Four and One) lost
    their speaker's ḍamma in the lanes. It now reads the previous verb's RESOLVED cell
    (`__cell` or `cell`, person 6, and the verb decided) through `pre30.verb` (34d). The
    lanes are the only place such a slip shows: the new chapters had no speaker's tāʾ
    followed by a joined one.

Smoke: the Part Two gate grows to ch1-11 / 158 sentences with the floors from the
measurement (ch9 99.5, ch10 100, ch11 100) and seventeen more named rule assertions; a
word the grader keeps as written (the nūn of protection, رَآهُ) counts as undecided in the
gate, as it does in the grader. The neighbours (the Talkhīṣ/Kāfiya/Part One sweep, Part
Four's forty-five chapters and Part One's twenty-four against the v195 engine, Part Two
ch1–8, the seeds, r21/r22, `sarfAudit`, the Talkhīṣ gates) swept WORSE 0.
The JamEngine plural-audit floor moves from 201 to 205: ch9–11 added four HEARD plurals
(سُرُج of سِرَاج, رِمَال of رَمْل, and the sound نَجَّارُونَ / حَدَّادُونَ of the فَعَّال trade-names,
which the builder still tries to break — its own gap, owed to a later round); the four were
named by diffing the audit lists of the v195 and v196 readers, not guessed.

## Qiṣaṣ Part Two chapters 12–39 — the flood, the storm, the she-camel: VOLUME 2 COMPLETE, and round 56 (wave 35, v197)

Twenty-eight chapters close the volume (`author_qisas2_ch12–39.py`, print pp. 28–68):
the end of «سفينة نوح» — the flood (ch12), the son of Nūḥ (ch13: 11:42–43), «he is not
of your family» (ch14: 11:45–47), after the flood (ch15: 11:44; 37:79); the whole of
«العاصفة» §1–11 — after Nūḥ, the ingratitude, the aggression and the palaces of ʿĀd, Hūd
the messenger, the call of Hūd (ch21: 7:65), the answer of the people (ch22: 7:66–68), the
wisdom of Hūd (ch23: 7:69), the faith of Hūd (ch24: 11:54–56), the obstinacy of ʿĀd (ch25:
67:26), the punishment (ch26: 11:43; 11:60); and the whole of «ناقة ثمود» §1–13 — after
ʿĀd, the ingratitude of Thamūd, the worship of idols (ch29: 10:44), Ṣāliḥ, the call of
Ṣāliḥ (ch31: 7:73), the propaganda of the rich (ch32: 23:33–38 as one quotation), «our
opinion was wrong», the counsel of Ṣāliḥ, «I ask you no reward» (ch35: 26:145, 26:153–154),
the she-camel of God, the turns (ch37: 11:64), the tyranny of Thamūd, the punishment (ch39:
11:65; 7:79; the ḥadīth of the dwellings of the wrongdoers; 11:68). Part Two now carries
39 chapters, 445 sentences, 4335 tokens, 804 glossary entries — **volume 2 complete** —
still Level 1, still in copyright and flagged so. New paradigms include `khaba` (hollow
yāʾ), `fajara`, `nafara`, `dajira`, `khariba`, `nabata`, `nataja`, `ayqana` (B4),
`tafattara` / `tahaddama` (B5), `hajara-emigrate` (B3; the key `hajara` was هَجَرَ),
`mujib-answerer` (the key `mujib` was مُوجِب), `hum` for the detached هُمْ.

**Round 56 (`patch35a`–`patch35ae`) — thirty-one cuts, all probe-first, on 83 misses of the first
measurement (ch12–39 at 95.1 on the v196 engine).** The chapters measure 99.x after them
(ch12–18 100, ch19 94.0, ch20 100, ch21 99.0, ch22 97.1, ch23 98.2, ch24 98.9, ch25 100, ch26 97.7, ch27 100, ch28 100, ch29 98.7, ch30 98.0, ch31 96.7, ch32 96.8, ch33–34 100, ch35 94.8, ch36 100, ch37 97.5, ch38 100, ch39 98.2 — 2612/2645 = 98.75 overall, 97 of the 83+ first-measurement misses fixed, 31 kept (nominal leftovers under the floors), 0 new). The round's one structural change is the first: the grader hands the
author's part of speech to the decision.

1. **The author's part of speech settles the homograph (35c).** The grader has carried
   the author's `pos` by index since wave 32c, but `vowel()` reset it before `decide()`
   ever read it. It now survives for the one call, and a new first pass uses it only
   where a STORED form is the written word: a verb by the author that the analyzer took
   for a noun, a particle or a wāw-joined pair becomes the corpus cell that IS the word
   (وَعَدَهُ = waʿada's māḍī, not وَ + عَدَّ; وَصَلَ, not وَ + صَلِّ; سَآوِي = the future sīn on
   awā's muḍāriʿ; لَانَ; وَكُنَّا); a noun by the author that the analyzer took for a verb
   becomes the noun lexicon's head that IS the word (مَلَكُ الْمَوْتِ, أَشَدُّ, ظَنُّنَا, وَبِنَاءِ);
   a name by the author (صَالِح, هُود, عَاد, هَاجَر) is a name whatever the lexicon's verb says,
   so `propn()` and the writer's `isPropn` honour it (no hal for صَالِحٌ, no annexed يَا هُودُ,
   the name keeps its tanwīn before a bare ابْنٌ — لِنُوحٍ ابْنٌ). A verb the analyzer and the author
   agree on is stamped and RESTORED if a later lexical pass renames it (وَهَاجَرَ صَالِحٌ was
   becoming the name Hājar). The stored plural that IS the written word wears no
   pronoun (مُلُوكَ, not مُلُو + كَ); the hamza seat is spelling for the comparison
   (سَآوِي ~ أَأْوِي, أُومِنُ ~ أُؤْمِنُ); after the negating لَا the stripped word's passive
   māḍī reading yields to the paradigm's own 1s muḍāriʿ (لَا أُومِنُ).
2. **The analyzer's nahy flag reads the host (35a).** فَلَا تَسْأَلْنِ, لَا أَسْأَلُكُمْ, لَا
   أَخَافُهُمْ: the prohibition was being read off the enclitic's sukūn; it now tests the
   host's last letter, never the speaker's forms, and never the negated khabar after
   إِنَّكَ / a detached pronoun.
3. **The writer (35b).** بَسَاتِينُ: a muntahā-shape plural the lexicon STORES takes the
   diptote's ḍamma (the ين-tail is the pattern's, not a sound plural's — النَّجَّارِينَ stays
   a sound plural); بَاكِينَ: the manqūṣ branch never rewrites a sound plural's ين/ون;
   يَصِحْنَ: the women's nūn keeps its fatḥa; فَلَا تَسْأَلْنِ: the shortened nūn of
   protection keeps its kasra; يَا بُنَيَّ: the muḍāf munādā on the shadda takes its
   fatḥa; إِنْ أَجْرِيَ: the page's fatḥa on the speaker's yāʾ.
4. **The nominal seats (35d).** أَرْضًا جَمِيلَةً خَضْرَاءَ فِيهَا بَسَاتِينُ وَعُيُونٌ: the bare
   noun after a jarr-pronoun behind an indefinite object is the ṣifa clause's delayed
   mubtada, never the object's badal; وَإِنَّ وَعْدَكَ الْحَقُّ وَأَنْتَ…: the definite noun after
   إِنَّ's ism with nothing left to be the khabar IS the khabar; وَإِنْ كَانَ ابْنَهُ: the
   pronoun-closed noun that ends the line after kāna is her khabar; فَالْعِيَاذُ بِاللهِ: a
   new nominal line after a closed iḍāfa; وَاللهُ لَا يَقْبَلُ الشَّفَاعَةَ: no oath when a
   he-verb under لَا follows with no doer of its own — God is the mubtada, the verb his
   khabar, the noun after it the object.
5. **The doer and the frames (35e).** The verb after kāna's NAMED ism (كَانَتْ خَيْلُ عَادٍ
   تَمْلَأُ الْمَيْدَانَ) or إِنَّ's NAMED ism (إِنَّ اللهَ لَا يَرْضَى لِعِبَادِهِ الْكُفْرَ) does the
   ism's act — the noun after it is its object, and a pre-pass walk-back from the verb to
   the kāna / إِنَّ keeps the doer-picks and the «definite noun after a hidden doer» rule
   from naming another doer (35f); a kāna-sister with a pronoun ism under an open إِنَّ is
   إِنَّ's khabar (وَلٰكِنَّهُمْ … صَارُوا عُبَّادَ); the shouting, calling and answering verbs
   quote like قَالَ (وَصَاحُوا هٰذِهِ سَحَابَةُ مَطَرٍ); a ẓarf with its pronoun right after the
   verb is the ẓarf and the definite noun behind it the doer (وَحَالَ بَيْنَهُمَا الْمَوْجُ);
   السَّمَاء joins the feminine list; after a verb of prayer or worship الله is the one
   addressed and the name after Him the doer (فَدَعَا اللهَ صَالِحٌ); the reciprocal
   بَعْضُهُمْ بَعْضًا; kāna tāmma before the ال-time word with its ordinal (وَلَمَّا كَانَ
   الْيَوْمُ الثَّالِثُ); the noun lexicon reads the opened tāʾ before a pronoun (مَاشِيَتُكُمْ
   = مَاشِيَة, كَعَادَتِهِمْ = عَادَة) and the hamza on its seat (مَاؤُهَا = مَاء); a colon before
   a verb closes the clause before it; a name right after a she-verb with no feminine
   subject is its doer even for a verb of perception (لَمْ تَجِدْ عَادٌ جَوَابًا — the tribe is
   feminine); the wāw-joined ال-noun before its own verb after a mubtada–verb line is a
   new mubtada (الْأَطْفَالُ يَبْكُونَ وَالنِّسَاءُ يَصِحْنَ وَالرِّجَالُ يَدْعُونَ); after a pause an
   ال-noun followed by a bare noun opens a nominal line (النَّاسُ أَمْوَاتٌ … وَالْبُيُوتُ خَرَابٌ);
   the pronoun-closed noun after a naʿt before كَأَنَّهَا is the ṣifa clause's mubtada
   (أَجْسَامُهُمْ كَأَنَّهَا مِنْ حَدِيدٍ); كُلّ / بَعْض / جَمِيع annex the bare noun after them
   (كُلَّ وَاحِدٍ).
6. **The moods and the kāna frames (35f).** وَإِلَّا تَغْفِرْ لِي وَتَرْحَمْنِي: إِلَّا before a
   muḍāriʿ at the clause head is إِنْ + لَا, the shart's jazm copied by the wāw; لِيُنْذِرَكُمْ:
   a lām after a jarr-pronoun or a jarr particle is the lām of purpose; وَلَا تَمْلِكُ لِأَحَدٍ,
   وَلَا تَسْقُطُ وَرَقَةٌ: the she-verb under لَا with no addressee is negated — a jarr
   phrase or a feminine noun after it changes nothing; فَيَأْخُذَكُمْ عَذَابٌ: the fāʾ of
   consequence after a prohibition takes naṣb even where the author's note names the
   jawāb of the request; لَيْسَ هٰذَا سَحَابَ رَحْمَةٍ, كَانَ ذٰلِكَ سَبْعَ لَيَالٍ: the demonstrative
   after kāna is her ism (an ال-noun after it her badal); بَلْ closes every frame before
   it (بَلْ هُوَ رِيحٌ); وَلٰكِنَّ النَّاسَ أَنْفُسَهُمْ يَظْلِمُونَ: the pronoun-closed noun between
   إِنَّ's ism and a plural verb is the fronted object; the delayed ism behind a
   jarr-pronoun, with or without its own pronoun (وَكَانَ لِلنَّاسِ فِيهِ رَجَاءٌ كَبِيرٌ, وَلَيْسَ
   عَلَيْكُمْ عَلَفُهَا وَمَاؤُهَا — the frame closes on it, the adjective is a naʿt, the joined
   noun an ʿaṭf); the future sīn on kāna's sister still opens her frame (أَنَّكَ سَتَكُونُ
   مِثْلَ فُلَانٍ, where إِنَّ's pronoun ism is kāna's); kāna before مَا / مَنْ + verb is tāmma
   (وَلَمَّا كَانَ مَا أَرَادَهُ اللهُ), and a wāw-joined verb after a مَا-subject clause starts
   its own clause.
7. **The leftovers (35g–35k).** بِالْفَوَاكِهِ وَالْأَثْمَارِ: the wāw-joined ال-noun right after
   a noun in jarr is joined to it in jarr, and so after a frozen muḍāf ilayh (مِثْلَ فُلَانٍ
   وَفُلَانٍ); وَبَارَكَ اللهُ لَهُمْ: الله right after a verb is its doer even where a subject
   was named earlier in the line; تَشْرَبُ هٰذِهِ النَّاقَةُ: the she-verb's only feminine is the
   demonstrative doer, the ال-noun its badal in rafʿ; inside the shart clause a joined
   intransitive verb before a definite noun takes it as doer and the jawāb's she-verb
   shares no masculine doer (وَغَرِقَ الْكُفَّارُ أَمْسَكَتِ السَّمَاءُ); بِآلِهَتِنَا: a
   pronoun-closed noun whose head the lexicon owns only behind بِ / كَ / لِ is under that
   jarr letter; the second لَا continues the negation past a jarr phrase (لَا تُؤْمِنُ
   بِآلِهَتِنَا وَلَا تَخَافُهُمْ); the fāʾ clitic on a pronoun-closed muḍāriʿ; the relative
   clause inside إِنَّ's ism (إِنَّ هٰذَا الْكَلْبَ الَّذِي تَرْمُونَ إِلَيْهِ … لَا يُفَارِقُ بَيْتَكُمْ)
   keeps her frame open past its verb — the demonstrative after إِنَّ is her ism; after
   مَا / مَنْ the definite noun behind the he-verb is its doer (كَمَا طَلَبَ النَّاسُ, مَا يَصْنَعُ
   الْإِنْسَانُ); an intransitive verb's bare noun behind a jarr phrase is its doer when it
   is no ṣifa-shape and wears no fatḥatān on the page (خَرَجَتْ مِنَ الْجَبَلِ نَاقَةٌ حَامِلٌ).
   After لَا's ism the ال-time word is its ẓarf, not its annex (لَا شَكَّ الْيَوْمَ) (35k).

8. **The neighbours' lanes (35l–35ae) — what the sweep of Parts One and Four found.** The
   first full-lane run of the 35a–k reader against the v196 logs was WORSE 9 / 7 / 8
   on the three lanes; every one was hunted to its rule. The surprise was content, not
   code: عِيدِ الْأَضْحَى (Part One ch6) broke on the UNPATCHED reader because Part Two
   brought the name عَاد (the people of Hūd) into the lexicon, and the analyzer's lemma
   for عِيد is the verb عَادَ — the "name + ṣifa" rule (زَيْدٍ الْعَالِمِ) tested the LEMMA
   against the lexicon and found a name. A head is a name by its own word now, never by
   a lemma that merely spells a name elsewhere (35m). The rest: the relative's hidden
   doer passes only to a verb JOINED to the relative's own verb (وَمَنْ رَآهُمْ وَرَأَى
   قُصُورَهُمْ takes the object; الَّتِي أَكْرَمَ اللهُ بِهَا keeps الله) (35l/35n); a مَا
   governed by a noun or a jarr letter is mawṣūl (غَيْرِ مَا يُرْضِي اللهَ) and the taʿajjub
   أَفْعَلَ takes its noun as object (فَمَا أَشَدَّ الظَّلَامَ وَمَا أَبْعَدَ السَّلَامَ); inside a
   chain of "ال-noun + jarr phrase" members the joined ال-noun before its own jarr phrase
   joins the chain's head, not the jarr noun (الِاسْتِخْفَافُ بِالْأَنْبِيَاءِ … وَالتَّعَامُلُ
   بِالرِّبَا); the walk-back to kāna's ism crosses no fatḥatān khabar and no relative
   pronoun (كَانَ الْوَقْتُ مَسَاءً قَدْ مَدَّ الظَّلَامُ رُوَاقَهُ), and a noun the pre-pass
   already named doer is never the owed object; the she-verb right after a kāna sister is
   its khabar — the ism is its doer (لَا تَزَالُ تَعْبُدُ الشَّمْسَ, صَارَتْ تَفْقِدُ
   أَصَالَتَهَا), and an opened-tāʾ noun under هُمْ after a named doer is the object (لَمْ
   تَقْبَلْ مَقَالَتَهُمْ); once الله is the named doer, every later joined 3ms muḍāriʿ
   continues Him (يُرِيدُهُ اللهُ … وَيُقِيمُ الْحُجَّةَ … وَيَنْصُرُ الْحَقَّ وَيَكْبِتُ أَهْلَ
   الْبَاطِلِ) (35o); the two-object verb whose second object rides بِ owes no further
   object (يُبَشِّرُكِ بِكَلِمَةٍ … اسْمُهُ الْمَسِيحُ عِيسَى ابْنُ مَرْيَمَ); a fatḥatān noun behind
   a tafḍīl is its tamyīz, never the muḍāf ilayh, and the tafḍīl is diptote in the writer
   too (أَدَقَّ مِنْهُ وَأَبْعَدَ مَنَالًا, أَكْثَرُ مَالًا) (35p); the author-noun retype keeps
   the joiner in its own segment (وَكَفٍّ عَنِ الْعَمَلِ); the munādā's fatḥa is already there
   under the shadda in NFC order (يَا بَنِيَّ); the jarr-clitic pass lends the row its lemma
   and its jarr but leaves the analyzer's own segments to the writer (بِأَهْلِكُمْ, لِإِخْوَتِكُمُ,
   بِهَدِيَّتِكُمْ), and a demonstrative joined after a jarr member opens its own clause
   (وَذٰلِكَ سِرُّ تَفْضِيلِهِمْ) (35q); a wāw-joined مَا is the negation, governed by no noun
   (وَمَا سَمِعَ النَّاسُ بِمِثْلِهَا), only an unjoined مَا behind a tanwīn-less muḍāf is the
   governed mawṣūl (غَيْرِ مَا يُرْضِي اللهَ, not لِبَعْضٍ مَا يَقُولُ هُودٌ), and behind a question
   word the name after the verb is its doer, never the object the name-rule would make
   it now that the author's propn flag reaches that rule (مَاذَا يُرِيدُ هُودٌ) (35r); the release's own Talkhīṣ gate caught the last one — the
   wāw/fāʾ-joined māḍī reading (وَهَاجَرَ) is refused where the author wrote a noun or the
   lexicon owns the whole word (ظَهَرَ فَسَادُ جَعْلِ وَجْهِ الشَّبَهِ is no فَ + سَادَ) (35s); the Talkhīṣ gates of ch48–57 caught two
   more — a مَا fused to بِ / لِ is the governed mawṣūl (بِمَا يُلَائِمُ الْمُسْتَعَارَ لَهُ; كَمَا
   طَلَبَ النَّاسُ keeps its doer), and the joined noun after a muḍāf-ilayh member is its atf only
   when both are bare indefinites and the joined one wears no fatḥatān (مِثْلَ فُلَانٍ وَفُلَانٍ;
   وَالْجَامِعُ التَّرَتُّبُ and وَالْكَرَمُ بَيْنَ بُرْدَيْهِ open their own clause, فَانْطِبَاقًا is
   the ḥāl) (35t). A Talkhīṣ lane (ch40–76 against v196) then found eleven more, all
   hunted to their rules (35u–35ab): إِنَّمَا is no مَا and a مَا behind a pronoun-closed noun
   is the governed mawṣūl; the joined ال-noun after a jarr noun is its atf only when no
   pause stands before it, no unjoined verb follows the joined chain, the joiner is no
   jawāb's fāʾ after a shart, and no raf noun with its own jarr phrase precedes
   (فَالْأَحْسَنُ تَرْكُ…, وَالنَّجْمُ وَالشَّجَرُ يَسْجُدَانِ, وَالْفَضْلُ لِلْأَوَّلِ); a passive verb keeps
   the مَا before it as its nāʾib (وَتُسَمَّى التَّنَاسُبَ); the jawāb on the fāʾ is no jazm
   (وَإِلَّا فَيُقَالُ); a head wearing tanwīn annexes nothing — no pre-pair, no كُلّ-pair, no
   asked-nakira pair survives it, and the asked nakira annexes only without tanwīn (أَقَوْمٌ آلُ حِصْنٍ, كُلٌّ مَوَدَّتُهُ); the كُلّ-member rule releases
   the member from any head seat so the writer keeps its tanwīn, and keeps the seat when it annexes on (كُلَّ يَوْمٍ تُبْدِي; كُلِّ أَعْمَالِ الْخَيْرِ); the
   author's noun behind لَا is the genus-lā's ism before any ḥāl reading (وَلَا مَالَ). After these the lanes read WORSE 0 against v196 on
   every sentence the round touched. The release's chunk 6 then found the one lane none of these probes walk — the FREE-TEXT path
   (35ac): the bayān and badīʿ engines call `decide()` on the analyzer's rows with no grader context, and the round's
   tanwīn tests read `_orig24` (the grader's copy of the written words), which that path leaves empty or stale from the
   last graded sentence, as it leaves the grader's part-of-speech list. Now `decide()` takes the row's own written word
   as its marks and drops the stale list when no graded text is aligned (فَانْطِبَاقًا keeps its fatḥatān and its ḥāl, so
   the tashbīh's wajh is read again); the 35j bare-doer hop crosses jarr phrases only, never a negation (لَا تَكَلَّمُ نَفْسٌ:
   the homograph after لَا is its own verb, not يَأْتِ's doer, and the jamʿ ʿāmm comes back); and C4's tanwīn alif needs the
   fatḥatān itself — آمَنَّا wears a fatḥa before its shadda and stays the verb now that Part Two's lexicon owns آمِن (the
   takīd al-madḥ sub reads nafy-illā again). The five chunk-6 checks (ch48–50, ch61–64, ch65–67, the tibāq and list seeds)
   are that lane's gate. Chunk 7 then caught what the lane compare itself had hidden: it counted HITS, so a sentence whose
   graded-word count grew with new misses (12/13 → 12/15) read as unchanged. The compare now counts misses (`cmplog56b`),
   and the three it surfaced are cut in 35ad: the ال-noun right after a NAMED or pronoun-closed object or its badal is that
   object's naʿt, no new mubtada (وَتَنَاوَلُوا أُمَّهُ مَرْيَمَ الْبَتُولَ — and so وَالطَّعْنِ is بِالْقَذْفِ's atf again; Part Four ch29
   back over its floor; a plain ال-object keeps the old reading, because Part Four ch18 s4 showed the wider cut only moves the
   miss: there the print separates a chain of five naʿts with a comma — الْقَاهِرَةِ، الرَّحِيمَةِ — and the 23c "no naʿt across
   a stop" rule turns الرَّحِيمَةِ into an object, after which فَتُخْرِجُ هٰذَا الْإِنْسَانَ needs the joined she-verb to inherit
   يَدُ as its hidden doer; both are round-57 cuts, probe-first, not this release's); the 35h object rule skips a demonstrative, whose kāf is no pronoun (فَعَلَ ذَلِكَ keeps its mabnī surface); a word
   wearing fatḥatān on the page is no delayed mubtada and no khabar (مِثْلُهُ فِيهَا مُبَالَغَةً is left to the reader, as v196
   left it — and the writer (35ae) now leaves an undecided word with the page's own ending instead of a stripped one, so
   the free-text reader shows وَكِلَا مُضَافًا as written, never مُضَافا; the seventh gate run caught that on the Kāfiya
   seeds). Two Part Two floors had been carried over above their own measurement (ch19 94.0, ch35 94.8 against a floor of
   95) and now stand at the measured 93.

What this round is NOT: no engine learned the author's answers. The part of speech is
the only authored fact read, it is read only where a stored form confirms it, and the
grader still writes every ending from the rules; the `pos` has been in every token since
the first package and the live app shows it on the card.

Smoke: the Part Two gate grows to ch1-39 / 445 sentences with per-chapter floors from
the measurement (floors ch1 99, ch2 98, ch3 98, ch4 98, ch5 98, ch6 99, ch7 99, ch8 99, ch9 99, ch10 99, ch11 99, ch12 99, ch13 99, ch14 99, ch15 99, ch16 99, ch17 99, ch18 99, ch19 93, ch20 99, ch21 98, ch22 96, ch23 97, ch24 97, ch25 99, ch26 96, ch27 99, ch28 99, ch29 97, ch30 97, ch31 95, ch32 95, ch33 99, ch34 99, ch35 93, ch36 99, ch37 96, ch38 99, ch39 97) and fifty-four more named rule assertions (one per cut
above, taken from the sentences the round was cut on). The neighbours (the
Talkhīṣ/Kāfiya/Part One sweep, Part Four's forty-five chapters and Part One's
twenty-four against the v196 engine, Part Two ch1–11, the seeds, r21/r22, `sarfAudit`,
the Talkhīṣ gates) swept WORSE 0 on Part Four's lanes A and C, Part One, Part Two ch1–11 and the sweep (BETTER 27 / 6 / 1 / 1); lane B shows two lines whose graded-word count fell by one because وَرَبَّكُمْ moved from a lucky verb reading to the uncounted mabni noun reading — the same vowels.

## The Şerḥu'l-Muġnī as engines — the fifteen kinds of ism, taṣghīr and nisba by rule, and round 57 (wave 36, v198)

**What the wave is.** Row 36 of the coverage table — the 96-page Şerḥu'l-Muġnî lesson
notes (`research/sources/serhul-mugni-ders-notlari-kisa-1.txt`) — had given the app the
nine causes of ghayr munṣarif (v192) and the seventeen lāzim-mabnī ẓarfs (v192); its
other automatable chapters were still lying in the text. This wave takes three of them
cover to cover and makes them engines, labs, cards and games, each graded on the book's
OWN examples: the fifteen kinds of ism (p. 3), the diminutive (pp. 51–53) and the nisba
(pp. 53–55). Round 57 of the DabtEngine rides along with one cut.

**Round 57 (`patch36a`) — one cut, one refused.** v197 had logged two cuts for this round
off Part Four ch18 s4. The first — a chain of ال-adjectives the print separates with a
comma (الْقَاهِرَةِ، الرَّحِيمَةِ) — was REFUSED on inspection: the page vowels
الْقَوِيَّةُ الْقَاهِرَةُ الرَّحِيمَةُ الْحَكِيمَةُ in raf, naʿts of يَدُ and not of
الْقُدْرَةِ, so the comma marks a change of head that no rule can read without the vowel
the grader is forbidden to look at; the sentence keeps its three misses honestly. The
second landed, narrower than logged: a wāw/fāʾ-joined muḍāriʿ of the same person cell as
the muḍāriʿ before it, whose doer was NAMED, inherits that doer as its hidden pronoun when
it is transitive AND a demonstrative follows it — تَبْرُزُ يَدُ الْقُدْرَةِ … فَتُخْرِجُ
هٰذَا الْإِنْسَانَ الضَّعِيفَ (the demonstrative and its badal are the object, nasb). The
wider cut (any transitive joined verb) was tried first and the lanes refused it: an ال-noun
or a pronoun-closed noun after such a verb is as often its NEW doer — وَيَغْشَى الْيَأْسُ
الْقَاتِلُ, وَيَفْهَمَ قَوْمُهُ, وَيُخْصِبُ النَّاسُ, وَيَأْكُلُ الْقَوِيُّ مِنْهُمُ
الضَّعِيفَ — four regressions for five gains, so the engine keeps the old reading there and
takes only the demonstrative, which after a verb with a doer already seated is its object.
An intransitive one still names its own doer after it — يَقُومُ زَيْدٌ وَيَقْعُدُ عَمْرٌو.
On every lane with the misses-based compare: every lane reads WORSE 0, BETTER 0 against v197 (Parts One, Two and Four, the Talkhīṣ, the sweep, the crash scan) — the cut touches nothing the corpus grades in sequence and holds the free-text sentence it was cut on; the Part Four ch18 s4 line keeps its three naʿt misses, which the page's own raf vowels alone could settle.

**The IsmEngine learns the Muġnī (`patch36b`).** The engine already derived فُعَيْل /
فُعَيْعِل and the plain nisba; the notes add the rules it lacked, in this order before
the old ones: أَب / أَخ restore their elided wāw and melt it into the yāʾ of taṣghīr
(أُبَيّ، أُخَيّ); فَعْلَان of a name or an adjective keeps its ان (سُلَيْمَان،
عُثَيْمَان، سُكَيْرَان، كُسَيْلَان); the feminine اء and ى stay (حُمَيْرَاء، سُمَيْرَاء،
بُشَيْرَى); five letters with a long fourth take فُعَيْعِيل with the long vowel turned yāʾ
(مُفَيْتِيح، عُصَيْفِير، قُنَيْدِيل); anything past the fourth letter is dropped
(سُفَيْرِج، عُنَيْدِل); a samāʿī feminine of three letters shows its ة (شُمَيْسَة،
أُرَيْضَة، عُيَيْنَة — and رِجْل the foot does while رَجُل the man does not, the vowels
telling them apart); a doubled letter counts twice (هِرَّة → هُرَيْرَة). For the nisba:
فَعِل opens its kasra (مَلَكِيّ، نَمَرِيّ); فَعِيلَة and فُعَيْلَة drop the ة and the
yāʾ together (قَبَلِيّ، مَدَنِيّ); the feminine hamza turns wāw while the root's hamza
stays on its seat (صَحْرَاوِيّ against اِبْتِدَائِيّ، إِنْشَائِيّ — `femHamza` decides);
a final doubled yāʾ after one letter returns its first yāʾ and turns the second wāw
(حَيَوِيّ), after two letters drops the first (نَبَوِيّ، عَلَوِيّ); مَكَّة and سُنَّة keep
their shadda and their own first vowel (مَكِّيّ، سُنِّيّ). `IsmEngine.MUGHNI_SEEDS` holds
the book's 53 examples and `mughniAudit()` grades the engine on them — 53/53 — by a
comparison that checks every letter and every vowel the engine wrote against the book's,
and forgives only a vowel it left unwritten. The first gate run caught one seam (`patch36e`): on a word typed BARE, with no
vowels at all, the hamza rule cannot see فَعْلَاء, so the old reading holds and the hamza turns wāw
(صحراء → صحراوِيّ); the root hamza is kept only when the written vowels show another shape.

**The surface (`patch36c`).** The Ism lab names the source under a Muġnī rule and offers
the book's examples as seed chips (tap one, the derivation appears); a new sarf game
**gTasgir** asks the diminutive or the nisba of the corpus's own nouns, its distractors
cut from the wrong rule — the fatḥa for the ḍamma, the ة toggled, the other derivation,
a neighbour's form — and its answer card reads the rule aloud.

**IsmKindsEngine — the fifteen kinds (`patch36d`).** The notes open the ism with
fifteen kinds: cins, alem, mu'reb, the tâbi', mebnî, tesniye, cem', ma'rife, nekre,
müzekker, müennes, tasğîr, mensûb, aded, ism-i fiil. `IsmKindsEngine.L` carries all
fifteen with the book's definitions in English and Turkish (the alem's three — ism,
laqab, kunya; the mabnī's lāzim list and its ʿāriḍ list; the three plurals; the
maʿrifa's five; the feminine's three written marks and its samāʿī kinds — women's names,
female beings, the paired organs). `profile(word, ctx)` reads a word's shape and the
lists and returns the kinds that apply with a sub-kind and a why: اسْمُ الْجِنْسِ or
الْعَلَمُ (a kunya by its أَب / أُمّ, a laqab by its الدِّين, else an ism), مُعْرَب or
مَبْنِيّ with the lāzim cause (ضَمِير، اسْمُ إِشَارَةٍ، مَوْصُول، شَرْط، اسْتِفْهَام،
ظَرْف، اسْمُ فِعْل، كِنَايَة) or the ʿāriḍ one (the 11–19 compound, the munādā, لَا's
ism, the ẓarf annexed to a clause — the last three only when the sentence says so), the
dual, the sound and broken plurals (the JamEngine's recognition), the maʿrifa with its
kind or the nakira, the gender with its mark, the taṣghīr shape, the nisba yāʾ, the
number noun, the ism fiʿl. The Ism lab lists the fifteen as a checklist with the applied
ones lit and defined; the word card gets a row «أَقْسَامُ الِاسْمِ» naming the applied
kinds; a second game **gKinds** asks one axis of a corpus noun — gender (by which mark),
number, definiteness (by which cause), or the kind itself — and answers with the book's
definition. `IsmKindsEngine.SEEDS` are the notes' own examples, one per kind, and
`audit()` reads them all back.

**Gates.** Two smoke checks: the IsmEngine on the Muġnī's 53 examples with the two
homographs (رُجَيْل / رُجَيْلَة), the lab's seed chips, the source note and gTasgir's
supply; the IsmKindsEngine on the book's examples (حَمْرَاء feminine by the long alif
and muʿrab, أَبُو بَكْرٍ a kunya, أَحَدَ عَشَرَ a number mabnī by accident, رَجُل /
رِجْل told apart), the fifteen-row checklist and gKinds' supply. Coverage row 36 moves
from PARTIAL to its three new engines; what the notes still hold for a later wave: the
munādā's seven rulings as a lab, the 24-row sarf table as a drill.

## The Qawāʿid al-Iʿrāb's third chapter as an engine — the twenty words and their faces (wave 37, v199)

Ibn Hishām's *Qawāʿid al-Iʿrāb* (COVERAGE row 34, `research/sources/qawaid-al-irab-turkish.txt` lines 49–68) groups twenty words by how
many FACES (wujūh) each wears: one (قَطُّ عَوْضُ أَجَلْ بَلَى نَعَمْ إِي), two (إِذَا), three (إِذْ لَمَّا كَلَّا لَا), four (لَوْلَا إِنْ أَنْ مَنْ), five
(أَيّ لَوْ), seven (قَدْ), eight (الْوَاو) and twelve (مَا). Wave 37 builds that chapter as `WujuhEngine` (`prototype/reader.html`, inserted before
`InnaEngine`; the source of the patch is `patch37a.py`, the lab/game/card `patch37b.py`).

**What the engine does.** `WujuhEngine.table(src)` (a sentence object or a free string) returns one item per word of the table with
`key`, `word`, `face`, `faces` (every face of that word, the chosen one lit, EN/TR/AR labels), `why` (EN/TR reason), `n` (the book's
count), `authored` (the faces the page's own iʿrāb phrase names, or null) and `agree`. `read(rows, i)` decides the face off the page:

- the word's own vowels first (`keyOf`): a shadda turns إِنْ into إِنَّ and لٰكِنْ into لٰكِنَّ, a kasra on مِنْ makes it the jarr letter, a tanwīn
  makes إِذًا, كِلَا / نِعْمَ / نِعَمٍ / أَجَلٍ / لِمَا are homographs — all skipped, never guessed;
- then the row beside it: a majzūm muḍāriʿ after لَا is the nāhiya, a nakira in naṣb without tanwīn the jins, a لَا inside a negated
  chain after a و the zāʾida, a single bare noun after an affirmative the ʿāṭifa; فَإِذَا before a nominal sentence is the mufājaʾa; a
  لَ-answer after لَوْ makes it the imtināʿ, a وَلَوْ with no answer the waṣliyya/taqlīl, وَدَّ before it the maṣdariyya; مَا إِنْ before a noun is
  the extra إِنْ, إِلَّا close after إِنْ the nāfiya, وَإِنْ + كان/muḍāriʿ + a lām fāriqa the mukhaffafa; a separator (سَـ سَوْفَ قَدْ لَنْ لَمْ لَوْ) or a
  noun after أَنْ the lightened أَنَّ, a command after a verb that means «say» without its letters (أَوْحَى نَادَى كَتَبَ) the tafsīriyya, لَمَّا أَنْ the
  zāʾida; بَيْنَمَا … إِذْ the mufājaʾa, a judgment before and a reason after the taʿlīl; قَدْ + māḍī the taḥqīq, + muḍāriʿ the taqlīl (takthīr
  when the doer is God), قَدْ قَامَتِ الصَّلَاةُ the taqrīb, قَدْنِي the ism fiʿl; كَلَّا + إِنَّ / an oath the istiftāḥ; نَعَمْ after a question the iʿlām, after
  a request the waʿd; مَنْ after a question mark, a verb of asking or a vocative the istifhām, after كُلّ / a preposition / a construct / with a
  ẓarf-clause the mawṣūl, with a majzūm or a فَ-answer the shart, after رُبَّ the mawṣūfa; أَيُّهَا the nidāʾ bridge, أَيْ with sukūn the tafsīr,
  أَيّ repeating a nakira the kamāl, أَيُّ + al-noun + khabar the istifhām.
- **The verb's tense and mood are read from the corpus cell first.** `RootFinder.fromCorpus(form).cell.tense` carries `mazi`,
  `majhulMazi`, `mudari`, `majhulMudari`, `mansub`, `majzum`, `majzum2`, `amr`; the engine trusts the cell's mood only when the cell's form
  equals the page word exactly (يُشَمَّ ≠ يُشَمُّ, so the page's fatḥa wins), and the page's vowels otherwise, after stripping object suffixes
  (يَنْهَاهُمْ → يَنْهَا, تُجِبْهُ → تُجِبْ). A weak-final ending (تَهْدِي، يَرْجُو، يُبْنَى) is `weak` — the page cannot show its mood, and no rule
  may call it jazm. The free-text fallback reads the māḍī/muḍāriʿ off the vowel after the first letter (تَجَلَّى / أَكَلَ / نَزَلَ are māḍī;
  تَكْتُبُ / تَنَامُ muḍāriʿ; أَرْسَلَ the māḍī of bāb IV; تُرِكَ the majhūl).
- **مَا** is read by `readMa` (the same neighbour facts, taught by the corpus) with `MaEngine.read` as the fallback shortlist; **الْوَاو**
  stays with `WawEngine` (a prefix, not a row).

**Grading — the page is the examiner.** `authored(key, irabAr)` maps the authored iʿrāb phrase to the faces it names (شَرْط → shart,
مَصْدَرِيّ → masdariyya, تَفْسِير → tafsiriyya, نَافِيَة|نَفْي → nafiya, نَاهِيَة|جَازِمَة → nahiya, لِلْجِنْسِ → jins, زَائِدَة|تَأْكِيد النَّفْي → zaida, تَحْقِيق →
tahqiq, تَقْلِيل → taqlil, تَكْثِير → takthir, فُجَائِيَّة → mufajaa, تَعْلِيل → talil, مَوْصُول → mawsul, اسْتِفْهَام → istifham, امْتِنَاع → imtina,
وَصْلِيَّة → taqlil, مُخَفَّفَة → mukhaffafa, حِجَازِيَّة → hijaziyya, ظَرْفِيَّة → zarfiyya, كَافَّة → kaffa, تَعَجُّب → taajjub …); لَفْظٌ مَحْكِيٌّ and حَرْفُ جَرٍّ
return null (not graded). The leading «الواو عاطفة، و…» clause is cut first so «عاطفة» never leaks into لَا's own face. Four places where
the pages themselves divide are held as EITHER: وَلَا inside a negated chain before a noun (Nadwī's pages say نافية, the ʿAqāʾid زائدة
لتأكيد النفي), لَا before a nakira in naṣb that a page calls plain نافية (it is the jins by form), لَا before a jarr-phrase (نافية as a ṣifa
on some pages, عاطفة on others), and بَلْ before a sentence that the pages call «إضراب وعطف» (the book calls it ibtidāʾ). A standalone
لَا that a page calls نافية is also allowed the answer-face. **These leniencies are listed here so nobody mistakes them for accuracy.**

**Measured (probe reader q3an, the whole corpus):** 1691 authored instances of the twenty + the four corpus extras (لٰكِنْ بَلْ حَتَّى أَمَّا),
coverage 100%, **99.5% agree** (9 misses: Birgivi's «قَدْ الفاصل» after عَلِمْتُ أَنْ, «أَنْ غَضِبَ اللهُ» lightened by context, حَتَّى بِالْقَتْلِ as
ibtidāʾiyya, حَتَّى أَحَاطَ with a māḍī called naṣb, وَلَوْ بَرَزَتْ waṣliyya with a لَ-verb within six rows, لَا بِالتَّضَادِّ called ʿāṭifa, وَمَنْ فِي
كَفِّهِ with a question later, فَلَا يَدْخُلُوا in a naṣb chain across a فَ, وَمَنْ خَلَقَكُمْ a question with no question mark). Seeds: the book's 40
example sentences, 40/40. **مَا: 435 instances, 61.8% under `MaEngine.read` alone → 89.7% with `readMa`** (the relative after a
preposition / construct / إِلَّا / a transitive verb, the negation at the head of a clause, مَا لَكُمْ مِنْ as negation, مَا + pronoun + verb,
مَا أَفْعَلَ + manṣūb as wonder, مَا دَامَ / مَكَثَ مَا as the ẓarfiyya, إِذَا مَا as the zāʾida). Everything together: 2126 instances, 97.5%.

**Atölye — the Wujuh lab** (`conjState.lab === "wujuh"`, `#wujuhIn`, `renderWujuhOut`): a card per word with the book's count badge,
the chosen face in Arabic with its EN/TR definition and the reason, every face of the word as chips (the chosen one lit, the corpus's
added faces dashed), ✓/✗ against the page when the sentence is a corpus one, the 40 seeds, the corpus tally (`Relax.later`
`"wujuh-audit"`), and the legend of the twenty by face count. **Game gWujuh** («Which face?», nahw, 🎭): corpus sentences where the
engine agrees with the page, the options are that word's own faces (max six per word). **Word card**: a «وُجُوهُ الْكَلِمَاتِ» row for the
twenty words in a phrase. Smoke gates: the audit floors (n ≥ 1500, coverage ≥ 99, acc ≥ 98; مَا n ≥ 400, acc ≥ 85; seeds 40/40; five
sample faces; the homographs مِنْ and إِنَّ never enter the table) and the lab on a phone (four cards for the seed sentence with the faces
shart / nafiya / zaida / mufajaa, chips, legend, seeds, tally, gWujuh supply). `DabtEngine` is untouched: the lanes are byte-identical.

**Process notes.** (1) `!this.negationBefore(rows, i)` on an index that returns −1 is always false — three rules were dead until the
seeds caught them; every index test now reads `< 0` / `>= 0`. (2) A prefix regex on a stem list (`ILM_STEM` has حس) made حُسْن a verb of
knowing; the list is excluded by name where it matters. (3) An authored phrase can name a face it then denies («لا تحقيق»): the map
tests the specific faces before the generic one.
