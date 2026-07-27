# Qissa — working notes

An Arabic graded-reader app (DuChinese-shaped) built on classical Islamic texts,
with madrasah grammar attached to every word. Target: iOS + Android launch.
Everything here is the *why*; the code is the *what*.

## Where things live

```
content/
  grammar/          65 global grammar notes — one JSON per topic, shared by every story
  i18n/irab-tr.json Turkish translation memory for i'rab strings, keyed by the English
  samples/<story>/  manifest.json · chapters/N.json · glossary.json · morphology.json
  user-uploads/     same shape; deeds-are-by-intentions ships its own standalone reader.html
  catalog.json      generated — index of every package (level, access, chapter count)
prototype/reader.html   the whole app: shell + generated data block
tools/
  validate_content.py   the quality gate — run it before anything else
  build_prototype.py    splices JS constants between // __DATA_START__ / // __DATA_END__
  smoke_test.js         34 browser checks (Playwright)
  check_irab_tr.py      finds i'rab strings with no Turkish yet
  check_i18n.py         fails on ANY user-visible string that has en but no tr
research/sources/       transcribed madrasah texts + README on provenance
```

Ten stories, Levels 1–6. Aqaid runs to four chapters, the Abu Yusuf wasiyya to five, and Kitab al-Buyu is the first fiqh text. Grammar notes are **global**: a note authored once shows
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
- **`pos` reaches the reader.** The role game needs it: a verb's i'rab routinely names
  another word's role («فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ» is not a fa'il), so
  anything derived by regex from i'rab text must first filter to nominals.
- **Corpus search** (`buildCorpus`, `searchCorpus`): one lazily-built index over every
  token in every story, matched against the bare spelling, the lemma, the root (stored
  spaced ق و ل but indexed closed-up too, because that is how it gets typed) and both
  glosses. Alif and ta-marbuta are folded. The root chip in the word sheet is a button
  that runs the same index — that is the root family view, not a separate feature.
  `jumpTo` opens the story if needed; a hit behind a paywall preview is not on the page,
  so it reopens the search rather than failing silently.
- **Sentence i'rab sheet**: the إعراب button on each sentence opens the whole sentence
  analysed at once — the exercise a madrasah student writes out. It needs nothing beyond
  per-token `irab`, so it comes free with any new chapter.
- **Birgivi's ma'mul taxonomy** organizes the registry — every note carries `mamul`
  (marfu' 8/8, mansub 13/13, majrur 2/2, majzum 1/1, tawabi' 5/5: complete).
- **Emsile-i Muttarida** = one form across 14 persons; **Emsile-i Muhtelife** = 14
  forms from one verb (+2 passive rows). Both render from `morphology.json`.

**A source with no Arabic in it.** The Buyu' upload was a Turkish definition
list. Supplying the Arabic is legitimate when the underlying wording is the
received one (al-Quduri, al-Hidaya, the Mecelle) — but the manifest must say so
line by line, and where the Turkish and the received wording diverge, the
received wording wins and the divergence is recorded.

## Grammar sourcing

Emsile, Bina, Maqsud, Birgivi's Awamil, Izhar, al-Kafiya (Ibn al-Hajib), Qatr al-Nada.
Transcriptions live in `research/sources/` with provenance in its README. Teach from
the books' own categories and wording — but generalize; do not overfit to one book's
example sentences.

## Process

- Branch: `claude/arabic-app-research-ozd58s`. Never push elsewhere.
- No PR unless explicitly asked.
- `git push -u origin <branch>`; retry only on network errors (2s/4s/8s/16s).
- Every story manifest carries `reviewStatus: pending-scholarly-review`. Keep it there
  until a human scholar signs off.
