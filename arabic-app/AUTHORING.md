# Growing the story pool — the developer's loop

This is the workflow for enriching Qissa week after week: new stories, new
chapters, new grammar notes. Everything routes through scripts that live in
the repo, so a story can always be regenerated, audited, and extended.

## Add a chapter to an existing story

1. Open the story's regenerator in `tools/authoring/` (e.g. `author_sulh.py`).
2. Append an `S<N>` block of sentences — every token gets trilingual i'rab
   (`ar`/`en`/`tr`), grammar-note ids that exist in `content/grammar/`, and
   the sentence gets its `jumal` clause rows.
3. Add new vocabulary to the GLOSS dict (per-story; `{en, tr}` glosses).
4. New verbs: build the paradigm with `sarf_gen` engines, or copy from a
   package that already owns the verb (lemma-identity rule). The browser
   audit will regenerate every classifiable paradigm cell-for-cell.
5. Wire: chapters list + TITLE, version bump, attribution range, `ALL`, and
   the `chapters/<N>.json` write.
6. Run the script, then `python3 tools/release.py`.

## Add a whole new story

```sh
python3 tools/authoring/new_story.py kitab-al-hajj "كِتَابُ الْحَجِّ" \
    "The Book of Hajj" "Hac Bahsi" --level 4 --source "hajj-turkce.txt"
```

The scaffolder writes `author_kitab_al_hajj.py` with the proven skeleton.
Author the sentences, transcribe the source into `research/sources/` with a
provenance header, run the script, run `release.py`. The library, catalog,
search, games, Root Finder and the audits all pick the story up by
discovery — nothing else needs registering.

## One command to ship

```sh
NODE_PATH=<node_modules-with-playwright-core> \
CHROMIUM_PATH=<chromium-binary> \
DART_BIN=<dart> \
python3 tools/release.py          # gates, builds, smoke, sw bump
python3 tools/release.py --check  # gates only (CI style)
QISSA_SKIP=smoke,pwa,dart python3 tools/release.py   # machines without a browser
```

It stops at the first failure and names it. When it prints ALL GATES GREEN,
`git add` from the repo root, commit, push.

## The honesty rules (non-negotiable)

- **Never publish Arabic we aren't sure of.** Omit an uncertain form; the
  UI hides the row. Divergences from a source are recorded in the
  manifest attribution.
- Original compositions say ORIGINAL in the attribution, in both
  languages, and stay `pending-scholarly-review` until a human scholar
  signs off.
- Sema'i facts (Form I babs, irregular nisbas, shadh imperatives) are
  STORED, never computed. When an engine cannot re-derive a stored form
  (ibdal, hamza drops), store the surface wazn so the audit skips it —
  the أَخَذَ / اِتَّقَى precedent.
- A user correction becomes doctrine: fix the data, add or extend the
  grammar note that teaches the distinction, anchor it where the mistake
  lived, and pin it with a smoke check (the vav-ı hâliye and Rize-nisba
  precedents).

## Where knowledge goes

| Kind | Home |
|------|------|
| Uploaded source texts | `research/sources/` + provenance header |
| Grammar topics | `content/grammar/<id>.json` (global, bilingual) |
| Rules with no data (orthography, wazn, tasgir…) | engine classes in the reader (HarakeAuditor, WaznEngine, IsmEngine, SentenceAnalyzer…) + a smoke check per rule |
| Sema'i exceptions | the engines' stored tables (SEMAI_NISBA, corpus paradigms) |
| Process lessons | CLAUDE.md "Rules learned the hard way" |

## The balagha frames — an assertion the engines will test

A sentence may carry `tashbih`, `majaz`, `kinaya` and `badi` frames (lists of
objects, token indexes zero-based within the sentence). Each frame is a CLAIM:
the validator range-checks every index, the matching engine reads the sentence
and `agree()` grades itself against the frame, and the wave's smoke gate
refuses a chapter whose frames the engine cannot read back. Author the frame
from the book's own analysis, never from what the engine happens to say.

The badiʿ frames (`tools/validate_content.py`: `BADI_KINDS`, `BADI_FIELDS`,
`BADI_SUBS`) take the shape of the figure:

| kind | fields | subs |
|---|---|---|
| tibaq | `pair` | ijab, salb |
| muqabala | `first`, `second` (ordered, equal length) | — |
| muraat-al-nazir | `set` | haqiqi, mulhaq |
| tashabuh-al-atraf | `pairs` (`[[end, head], …]`) | — |
| iham-al-tanasub | `set`, `word`, `murad`, `other` | — |
| irsad, ruju | `pair` | — |
| mushakala | `word`, `companion` (taḥqīq) or none (taqdīr), `asl` | tahqiq, taqdir |
| muzawaja | `first`, `second` | — |
| aks | `first`, `second` | mudaf, mutaalliq, tarafayn |
| tawriya | `word`, `near`, `far`, `companion` | mujarrada, murashshaha |
| istikhdam | `word`, `refs`, `murad`, `other` | lafz-damir, damirayn |
| laff-nashr | `first`, `second` (ijmālī: one first, two or more seconds) | murattab, ghayr-murattab, ijmali |
| jam | `set` (the gathered things), `word` (the one ruling) | atf, fail, inna, amm, ishara |
| tafriq | `first`, `second` (the two things of one kind, each as its word or its head + annex) | nafy-tashbih, bayan, partition |
| taqsim | `first`, `second` (equal length: the things and their rulings, or the rulings and the things) | tayin, ahwal, istifa, amma |
| jam-tafriq | `set`, `word` (the shared mushabbah bihi), `pairs` (`[[thing, its side], …]`) | — |
| jam-taqsim, jam-tafriq-taqsim | `with` (the partner sentence's id — the compound is read across sentences by `BadiEngine.compoundsOf`) | jam-first, taqsim-first |
| tajrid | `word` (the drawn-out figure), `companion` (the mark it is drawn from) | min, bi, bi-musahaba, fi, bila-harf, kinaya, nafs |
| mubalagha | `sub` (the degree — the author's judgement), `receipt` (kada, law, hatta, khayyal, hazl, none), `word` | tabligh, ighraq, ghuluww |
| kalami | `word` (the premise), `companion` (the consequence) | law, qasam, lain, qiyas |
| husn-talil | `word` (the claimed cause), `companion` (the quality), `sub` (the kind — the author's judgement), `receipt` (innama, lakin, jumla, law, kaanna) | la-illa, ghayr-madhkura, mumkina, ghayr-mumkina, shakk |
| tafri | `word` (the كَمَا hinge), `first`, `second` (each `[subject, predicate]`) | — |
| takid-madh, takid-dhamm | `word` (the adat), `sub` (the kind), `receipt` (illa, illa-anna, ghayr, bayda, siwa, lakinna), `first`, `second` (the clause on each side) | istithna-min-dhamm, madh-thumma-istithna, nafy-illa / istithna-min-madh, dhamm-thumma-istithna |
| istitba | `word` (the spoken praise), `companion` (the entailed one) — a doc frame | — |
| idmaj, tawjih, hazl-jidd | `word` — doc frames, shown and not read | — |
| tajahul | `word` (the question's word), `sub` (the aim — the author's), `receipt` (hamza-am, am, layta, ma-adri, kaanna), `companion` | tawbikh, mubalagha-madh, mubalagha-dhamm, hayra |
| qawl-mujib | `word` (the turned word), `companion` (the other's), `sub` | sifa-kinaya, lafz-mushtarak |
| ittirad | `set` (the names in their order) | — |
| jinas (wave 22) | `sub` as before, plus `kind2` (the seat / the kind within the kind — the engine's reading, checked by `agree()`): tamm → mumathil, mustawfa; murakkab → mutashabih, mafruq; naqis → awwal, wasat, akhir, mudhayyal; mudari, lahiq → awwal, wasat, akhir (+ muzdawij); qalb → kull, bad, mujannah; ishtiqaq → shibh-ishtiqaq; `pair` or `first`/`second` | see kind2 |
| radd-ajuz | `kind2` (tikrar, jinas, mulhaq), `pair` (the head, the close), `at` in verse (sadr-awwal, hashw-awwal, arud, sadr-thani, ajuz) — a hemistich mark `punct="*"` on the bayt tells the grader the rhyme seats | tikrar, jinas, mulhaq |
| saj (wave 23) | `sub` (mutarraf, mutawazi, murassa) and `kind2` for the finest kinds (equal, second-longer, third-longer) — the engine reads the clauses off the author's pauses: a `punct: "،"` / `"؛"` after the token that closes a clause, `"*"` at the hemistich; a one-word clause is read only where marked | `pair` (the two fāṣilas) |
| tashtir | `pair` optional — the frame names the figure; the engine reads both halves off the `"*"` and requires two different rawīs | the bayt carries `"*"` |
| muwazana | `sub` mumathala when half the words or more answer in wazn | `pair` (the two fāṣilas) |
| qalb-kull | `pair` = [first token, last token] of the palindromic span (a whole line or one hemistich) | `set` optional |
| tashri | `pair` (the first rhyme word — a stop the sense allows — and the line's true close); the engine confirms two different rawīs | hinted: the frame names the words |
| luzum | `pair` for one line (the two rhyme words) OR `word` + `letter` for a bayt whose peers are the chapter's other luzum bayts — every rhyme word must keep the same letter before the same rawī | a `word` frame is graded across the chapter |
| sariqa (wave 24) | `sub` zahir / ghayr-zahir; `kind2` the book's kind (naskh, ighara, ilmam; tashabuh, naql, ashmal, qalb, ziyada); `grade` mamduh / madhmum / mithl; `with` the sentence taken from (same chapter) | `set` the taker's words |
| iqtibas / tadmin | `sub` quran / hadith (iqtibas) or istiana / idaa (tadmin); `kind2` ghayr-manqul / manqul (the words kept their meaning or were moved); `source` the sura:aya, the hadith, the poet; `with` for a tadmin whose other hemistich sits in another sentence — the IqtibasEngine finds the received span by its own table | `set` the received words |
| aqd / hall / talmih | `source` the prose or verse the frame answers to (the engine confirms by the source it names); `with` the sentence holding the other side of an ʿaqd / ḥall | `set` |
| husn-ibtida / baraat-istihlal / takhallus / husn-intiha | `sub` husn / tatayyur (the opening); takhallus / iqtidab / fasl-khitab (the transition); `source` the poet or the aya — the received bayts of ch76 live in the IqtibasEngine's table and the frame is confirmed by the finder | `set` the bayt (or the hinge word هَذَا) |

Three of them are HINTED figures (mushakala, tawriya, istikhdam): the frame
names the word, and the engine reads the rest off the surface — the companion
that shares a stem, the pronouns that return, the furnishing that makes a
tawriya murashshaḥa. A probe that calls `BadiEngine.read(rows)` without the
sentence cannot read those; pass `{ sen }`.

## A second text from an Ottoman notebook (wave 25)

`tools/authoring/kafiya_common.py` is the whole adapter: it imports
`talkhis_common`, re-points its `PKG` at `content/samples/al-kafiya` (or at
`DRY_PKG` / `DRY_GR` for a dry run), and adds the commentary markers. Chapter
scripts (`author_kafiya_ch1.py`, `author_kafiya_ch2.py`) use the Talkhīṣ API
unchanged — `tok`, `seg`, `G`/`need`, `put_morph`, `write_out`, `report`. Three
rules carried over and one new: a key is a global claim (check every package's
glossary AND morphology before minting one — `alam` means عَالَم in Aqaid and
عَلَم in the Talkhīṣ, so the Kāfiya's sign is `alam-sign`); a restored ruling is
marked in both translations and in the attribution; a worked example that is
the teacher's, not the matn's, is marked COMMENTARY (`C_EN` / `C_TR`); and
**probe the chapter through the engines before landing it** (`STORY=al-kafiya
… probe24_sen.js <ch>` against a dry reader) — every miss is either an authoring
slip or a rule the text is owed, and the Kāfiya is owed many, because it is a
book about exactly what the engine claims to know.
