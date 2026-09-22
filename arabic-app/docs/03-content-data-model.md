# Content Data Model v0.1

Stories ship as **content packages**: a folder of static JSON + audio, versioned and served from a
CDN. The app downloads a catalog index, then packages on demand. Nothing here requires an
app-store release to change — this implements the "self-updating content" requirement.

```
catalog.json                     # index of all packages: id, level, version, free/premium flag, rotation window
<story-id>/
  manifest.json                  # story metadata
  chapters/<n>.json              # text: sentences → tokens (3 tashkeel layers), audio alignment
  glossary.json                  # story-scoped lexicon: lemma, root, gloss(es), level, audio ref
  morphology.json                # Emsile/Bina-style verb data: bab, wazn, masdar, ism fail/maful,
                                 #   full mazi/mudari (14 cells) and amr (6 cells) paradigms
  grammar-links.json             # token/phrase → grammar-note id
  audio/chapter-<n>.mp3          # human narration
  audio/words/<lemma-id>.mp3     # word audio (TTS ok at launch)
grammar/<note-id>.json           # GLOBAL, reusable grammar notes incl. common-mistakes blocks
```

## Key design rules

1. **Three text layers per token** — `full` (كَتَبَ), `smart` (only disambiguating harakat), `bare`
   (كتب) — generated in the editorial pipeline, never on-device. The reader's tashkeel toggle just
   switches layers.
2. **Tokens carry segmentation** — clitics split (`وَالْكِتَابُ` → `وَ` + `الْكِتَابُ`) so tap-word
   resolves the *lexical* word; the `surface` string preserves display form.
3. **Every token links a glossary entry (`lex`)**; glossary entries link roots and level tags →
   colored-underline rendering and flashcard creation are lookups, not NLP at runtime.
4. **Grammar notes are global objects** referenced from many stories; each has ≥1
   `commonMistakes[]` entry. The "spot the error" game later generates directly from these.
   Notes are grouped after the madrasah primers — **sarf** (الأمثلة / بناء الأفعال: paradigms,
   verb classes/abwab) and **nahw/awamil** (Birgivi's العوامل: each governing particle carries an
   `amil` field stating what it governs). Every token may also carry an `irab` field — the full
   classical parsing of that word in its sentence (Arabic + learner-English) — cheap to author
   per story and the backbone of the Master-level treatment.
5. **Audio alignment** is per-sentence `[startMs, endMs]` against the chapter MP3 (forced alignment
   in the pipeline) → karaoke highlight + tap-to-hear.
6. **Same story, multiple levels** = separate packages sharing `storyGroup` so the app can offer
   "read this again at your level."

See `../content/samples/wasiyyat-abi-hanifa/` for a worked example (level-2 retelling, chapter 1
excerpt, one grammar note with common mistakes). The level-6 original-text package will quote the
classical text and **must be checked against a printed edition before publishing** — the sample
marks this.
