# Flutter Architecture Spike v0.1

> ## ⚠️ NOT COMPILED — design + skeleton only
> There is no Flutter/Dart SDK on the authoring machine, so **nothing in this
> spike has been compiled, type-checked, or run.** The Dart under `../flutter/`
> is written to be correct and idiomatic and its `fromJson` parsing is
> cross-checked field-by-field against the real content packages, but treat it as
> a *buildable design target*, not working software. No "it runs" claims are made.
> To make it real: `cd flutter && flutter create . && flutter pub get` (see
> `../flutter/README.md`).

This resolves open decision §8.1 of the product spec ("prototype the reader in
Flutter first — RTL + custom text layout is the risk area") and open decision §1
(Flutter vs React Native vs native). It maps the existing web prototype
(`../prototype/reader.html`) and content model (`../docs/03-content-data-model.md`)
onto a Flutter app, and confirms the risky part — per-token tappable vocalized
Arabic — is tractable with the framework's native text stack.

---

## 1. Goal & non-goals

**Goal.** De-risk the Flutter client by (a) proving the reader's RTL/tashkeel/
tap-word/karaoke layout has a concrete, framework-native implementation, (b)
pinning the package→Dart data layer against the real JSON, and (c) choosing the
state, storage, and audio stacks with justification. Output = this document + the
`../flutter/` skeleton.

**Non-goals.** Not a finished app; not compiled. No backend. No visual/theme
polish. Only the Reader screen is skeletoned in code — every other screen is
designed here and left as a `// TODO(spike)`. Does not touch the web app, tools,
content packages, or `reader.html` (purely additive).

---

## 2. The #1 risk: RTL + custom per-token text layout

The spec calls custom Arabic text layout the project's top technical risk. The
reader must, in one line of running Arabic, simultaneously:

1. render **right-to-left** with correct joining/shaping and bidi for embedded
   punctuation and quotation marks (`«…»`, `،`, `:`);
2. show one of **three tashkeel layers** per token (`full` / `smart` / `bare`),
   toggled live without reflowing the page;
3. draw a **level-colored underline** under selected words (levels 1–4);
4. make **each token independently tappable** (opens the word sheet); and
5. paint a **karaoke highlight** on the sentence during audio playback.

### Recommended approach

**Render each sentence as a single `Text.rich` (`RichText`) with one `TextSpan`
per token, inside `Directionality(textDirection: TextDirection.rtl)`.** Attach a
`TapGestureRecognizer` to each token span; carry per-token style (underline
color, size). This is exactly what `../flutter/lib/reader/reader_screen.dart`
demonstrates.

Why this and not the obvious alternative:

- **Do NOT lay tokens out as separate widgets** (`Wrap`/`Row` of `GestureDetector(Text(...))`).
  That hands each word to the shaper in isolation, which breaks Arabic
  cursive joining across the word boundary set by the tokenizer, defeats
  line-level justification/kashida, and makes bidi with punctuation fragile. A
  single `Text.rich` gives the shaping engine the whole continuous run while
  still exposing per-span hit-testing and styling — the best of both.
- **Directionality / `TextDirection.rtl`** on the reading column (plus
  `textAlign: TextAlign.right`) gives correct RTL flow. Punctuation and quote
  marks are emitted as their own plain `TextSpan`s *outside* the tappable token
  span (matching the prototype, which appends them as bare text nodes) so a tap
  resolves the lexical word and the neutral-bidi marks sit correctly.
- **Tashkeel toggle** = re-selecting `SurfaceForms.layer(...)` and rebuilding the
  spans. Because all three layers are pre-rendered in the package (data-model
  rule 1), this is a pure string swap — no on-device diacritization. Consider a
  fixed `strutStyle` so toggling `full`↔`bare` doesn't change line-box height and
  reflow the page.
- **Level underline** = `TextStyle(decoration: underline, decorationColor: …)`
  on the token span, color from the level bucket (`level >= 4 ? 4 : level`),
  mirroring the prototype's `--lvl1..4` and its `data-lvl` rule. Toggleable, like
  the prototype's underline switch.
- **Karaoke highlight** = wrap the sentence in a container whose background lights
  up while `playingSentenceId == sentence.id`. For a per-*word* karaoke later,
  the same span list can swap the active token's `background`/color driven by
  `just_audio`'s `positionStream` against each token's position — but sentence-
  level highlight (what the prototype ships) is the MVP.

### Fonts & TTS/audio packages

- **Bundle Noto Naskh Arabic** (declared in `pubspec.yaml`, shipped under
  `assets/fonts/`). Do not depend on the platform Arabic font — full-tashkeel
  glyph coverage and vertical metrics differ across iOS/Android, and the reader
  lives or dies on consistent diacritic rendering. Give the text run generous
  `height` (~1.9) for tashkeel headroom.
- **`flutter_tts`** for device Arabic TTS. This is the sentence-▶ voice for
  user-uploaded texts (no studio audio) and the word-audio fallback — exactly as
  the analyzer doc specifies, reading the `full` layer so vocalization is
  correct. Set language `ar` / `ar-SA`, rate from the speed control.
- **`just_audio`** (+ `audio_service` for lock-screen/background) for real
  studio narration: one MP3 per chapter, seek by the sentence's
  `[startMs,endMs]` `AudioSpan` (data-model rule 5) for tap-to-hear and the
  "Play all" audiobook queue. Server-side neural TTS (analyzer doc V2) slots in
  behind the same `just_audio` path.

### State management — **riverpod** (over bloc)

Chosen: **`flutter_riverpod`**. The reader is a web of derived read-mostly state —
`ReaderSettings` (layer, underline, font size, ui/trans language, speed), the
loaded package, the SRS deck, per-story progress, playback position — consumed by
many widgets at different depths (the line, the word sheet, the control bar, the
library badges). Riverpod's `Provider`/`NotifierProvider` compose these as a
dependency graph with fine-grained rebuilds, no `BuildContext` for reads, and
trivial testability (override providers in tests) — ideal when there is no SDK to
lean on and correctness must be reasoned about. Bloc's event/stream ceremony buys
little here (there are few genuine "event streams"; playback is the one, and
`just_audio` already exposes streams) and adds boilerplate. Riverpod also makes
the Lite/Premium gate a single `entitlementProvider` the whole tree can watch.

### Local store — split by shape

- **`shared_preferences`** for the handful of scalar reader settings (mirrors the
  prototype's `qissa-layer`, `qissa-arsize`, `qissa-lang`, `qissa-rate` keys).
- **`isar`** for the **SRS deck and per-story progress** — collections with many
  rows, due-date queries (`due <= now`), reactive watches to update the "due"
  badge, and offline durability. This is the right tool over `drift` (no SQL
  schema/migrations needed for a document-shaped deck) and over
  `shared_preferences` (JSON-blob-in-a-string doesn't scale to a capped-at-100→
  unlimited deck with indexed queries). Downloaded content packages are cached as
  files in the app-docs dir (via `path_provider`), with their catalog metadata in
  isar.

> Decision note: isar 3.x is stable and the pragmatic pick today; if the team
> prefers a SQL substrate or isar's maintenance cadence is a concern at build
> time, `drift` is the drop-in alternative behind the same repository interface.
> The repository abstraction keeps this reversible.

---

## 3. Data layer: packages → Dart models

The app fetches `catalog.json` first (the server-driven index, spec §3.5), then
each story package on demand. Each JSON file maps to one Dart model with a
hand-written `fromJson` (no codegen, to keep the spike inspectable). Files under
`../flutter/lib/models/`:

| Package file | Dart model(s) | Notes |
|---|---|---|
| `catalog.json` | `Catalog`, `CatalogEntry` | `chapters` here is an **int count**, not a list |
| `<story>/manifest.json` | `StoryManifest`, `ChapterRef`, `StorySibling`, `Attribution` | `chapters` here is a **list** |
| `<story>/chapters/<n>.json` | `Chapter`, `Sentence`, `AudioSpan`, `Token`, `SurfaceForms`, `Segment` | the reader body |
| `<story>/glossary.json` | `Glossary`, `GlossaryEntry` | `entries` is a **map** keyed by `lex` |
| `<story>/morphology.json` | `Morphology`, `VerbParadigm` | `verbs` map; 14/14/6-cell paradigms |
| `grammar/<id>.json` | `GrammarNote`, `GrammarExample`, `CommonMistake` | **global**, reusable |
| (shared) `{ar,en,tr}` objects | `LocalizedText` | fallback order requested→en→ar (mirrors `T()`) |

The full verified field-by-field mapping is in §8.

**Note on prototype vs package field names.** `reader.html` consumes a *build-time
compacted* form of the data (e.g. `tok.s` for `surface`, `morph.fail`/`morph.maful`
for `ismFail`/`ismMaful`, `g.sources`/`g.mistakes` for `classicalSources`/
`commonMistakes`). The models here target the **canonical package JSON** (the real
files under `content/`), which is the source of truth the shipped app fetches from
the CDN. The build script's renames are not part of the wire format.

---

## 4. Screen / widget map (with reader.html parity)

Each prototype feature → Flutter widget(s) → the `reader.html` function it ports.

| Feature (spec) | Flutter widget(s) | reader.html fn | Approach |
|---|---|---|---|
| **Library shell** | `LibraryScreen` (grid of `StoryCard`) | `renderLibrary`, `storyStats`, `accessLabel` | `ListView`/`GridView` over `Catalog.packages`; per-story % from progress in isar |
| **Reader** | `ReaderScreen` → `SentenceBlock` → `Text.rich` | `renderStory`, `levelBucket` | §2; one `Text.rich`/sentence, RTL, per-token spans (**skeletoned**) |
| **Tashkeel toggle (3 layers)** | `TashkeelToggle` in control bar → `ReaderSettings` | layer control (`data-layer`) | swap `SurfaceForms.layer`; rebuild spans |
| **Level underlines** | per-span `TextStyle.decoration` | `.underlines .word[data-lvl]` | color by level bucket; toggle switch |
| **Font size / speed / trans lang** | control-bar buttons → `ReaderSettings` | `fontPlus/Minus`, `speedSeg`, `transSeg` | scalar settings in `shared_preferences` |
| **Tap-word bottom sheet** | `showModalBottomSheet` → `WordSheet` | `openWord`, `showSheet`/`closeSheet` | tabbed sheet; tabs shown conditionally |
| — Word tab | `WordTab` | `openWord` mode `"word"` | lemma, root, pos, form, plural, level, EN/TR gloss, segments, Save button |
| — Sarf conjugation table | `SarfTab` → `ConjTable` | `conjTable`, `openWord` mode `"sarf"` | `Table` widget; 14-cell (`PERSON_ROWS`) / 6-cell (`AMR_ROWS`); highlight the surface form; مضارع/ماضي/أمر tense switch |
| — I'rab tab | `IrabTab` | `openWord` mode `"irab"` | `Token.irab.ar` (RTL) + `.resolve(uiLang)` |
| — Grammar tab | `GrammarTab` → `NoteCard` | `openWord` mode `"grammar"`, `renderNote` | render each linked `GrammarNote` |
| **Grammar reference (search + level filter)** | `GrammarReferenceScreen` | `openRef`, `refNoteMatches`, `refLevelMatches`, `refListHtml` | list of all `grammar/*.json`; tashkeel-insensitive search + level chips |
| **SRS deck / review** | `DeckScreen` → `ReviewCard` | `openDeck`, `renderDeck`, `grade`, `dueCards` | isar collection; stepwise reveal (bare→lemma→gloss); FSRS (lean per spec §8.3) replacing the prototype's SM-2-ish `grade` |
| **Games — Match** | `MatchGame` | `startMatch`, `renderMatch`, `pickMatch` | word↔gloss pairs from glossary; timed |
| **Games — Harakat** | `HarakatGame` | `startHarakat`, `renderHarakat`, `harakatItems` | place vowels on last letter; items from tokens with `irab` |
| **Games — Spot-the-error** | `SpotError` | `startSpot`, `renderSpot` | from `GrammarNote.commonMistakes` (`gameSeeds.spotTheError`) |
| **Bilingual EN/TR** | app locale + `LocalizedText.resolve` | `ui()`, `T()` | `uiLang` provider; gloss/translation resolve |
| **Dark mode** | `MaterialApp.theme`/`darkTheme` | `data-theme` / `prefers-color-scheme` | system + manual toggle; level colors are theme tokens |
| **Sentence TTS + Play-all audiobook** | `PlaybackController` (riverpod + `audio_service`) | `speak`, `startPlayAll`/`playAllStep`/`stopPlayAll` | `just_audio` (aligned MP3) or `flutter_tts` (uploads); resume from first unread; background controls |

---

## 5. Offline, gating, and the analyzer "My Texts" flow (high level)

- **Offline / caching.** Catalog and package files fetched over `http`, written
  to the app-docs dir; a package is "downloaded" once its JSON + audio are local.
  Reader reads only from the local copy → offline by construction. Deck/progress
  live in isar and sync later. Premium unlocks explicit offline downloads (spec
  §3.1/§3.6).
- **Lite / Premium gating (spec §3.6).** A single `entitlementProvider`
  (RevenueCat via `purchases_flutter`) exposes the tier. Lite = rotating free
  stories (`CatalogEntry.access == "free"` and the server `rotationWindow` flag),
  deck capped at 100, Match game only, no offline. `CatalogEntry.isFreeToOpen`
  is the first gate; the entitlement + rotation window is the real check. Gating
  is UI-enforced client-side and authoritative server-side.
- **Analyzer "My Texts" (docs/04).** Premium users POST a `.txt`/`.pdf` to the
  analyzer endpoint; the app polls the job, then downloads the produced package
  and renders it in the **same `ReaderScreen`** as embedded stories, in a "My
  Texts" library section. Uploaded packages carry
  `access: "user-upload"` and `attribution.reviewStatus:
  "auto-generated-unreviewed"` → the reader shows a "machine-analyzed — may
  contain errors" banner (`Attribution.isMachineGenerated`), and sentence-▶ uses
  `flutter_tts` since there is no studio audio.

---

## 6. Milestone plan (mapped to the app-store roadmap, docs/04 §"App-store roadmap")

- **M1 — Reader parity (this spike → runnable).** `flutter create`, bundle one
  sample package, land Library + Reader + tashkeel toggle + underlines +
  tap-word sheet (all four tabs) + sentence TTS. Proves the risk is dead.
  *(roadmap step 1: "prototype parity in Flutter".)*
- **M2 — Learner loop.** SRS deck (FSRS) + review, grammar reference browser
  (search + level filter), bilingual EN/TR, dark mode, Match game. Persistence
  in isar + shared_preferences.
- **M3 — Content + audio + monetization.** Server-driven catalog over the real
  API, package download/offline cache, `just_audio` aligned narration +
  Play-all/background, RevenueCat Lite/Premium gating. *(roadmap step 2: backend
  v1 catalog/auth/sync; §3.6 subscriptions.)*
- **M4 — Analyzer + store launch.** "My Texts" upload→poll→render flow, Harakat &
  Spot-the-error games, store listings (EN/TR/AR, auto-generated-content
  disclosure). *(roadmap steps 3–4.)*

---

## 7. Open risks & decisions

1. **Per-word karaoke** needs word-level alignment; today only sentence spans
   exist (`AudioSpan`). Sentence highlight ships first; word-level is a pipeline
   +model addition later.
2. **isar longevity** — see §2 decision note; the repository interface keeps
   drift a swap-in.
3. **Tashkeel toggle stability** — verify a `strutStyle` prevents reflow when
   switching layers on a real device (cannot verify without SDK).
4. **FSRS vs the prototype's SM-2-ish `grade`** — spec §8.3 leans FSRS; the deck
   model stores an opaque `srs` blob so the scheduler is swappable.
5. **Font licensing/size** — Noto Naskh Arabic (OFL) bundled; watch app-bundle
   size if additional weights/scripts are added.
6. **`.gitignore` foot-gun** — the root Python `.gitignore`'s `lib/` rule hides
   `flutter/lib/`; must be un-ignored before commit (see `../flutter/README.md`).

---

## 8. Verified JSON → Dart field mappings

Every `fromJson` was cross-checked against the real files. Source file in
parentheses.

**`Catalog` / `CatalogEntry`** (`content/catalog.json`):
`catalogVersion`, `generatedFrom`, `packages[]` → each: `id`, `title{ar,en,tr}`,
`level`, `levelName`, `version`, `access`, `storyGroup`, `reviewStatus`,
`chapters` (**int count** → `chapterCount`), `rotationWindow` (nullable).

**`StoryManifest`** (`content/samples/wasiyyat-abi-hanifa/manifest.json`,
`content/samples/yunus-wa-al-hut/manifest.json`,
`content/user-uploads/deeds-are-by-intentions/manifest.json`):
`id`, `storyGroup`, `title{ar,en,tr}`, `subtitle{ar,en(,tr)}` (optional — absent
in deeds), `level`, `levelName`, `version`, `access`, `chapters[]` (**list** →
`ChapterRef`), `siblings[]` (optional — absent in yunus/deeds → `StorySibling`),
`attribution`.
— `ChapterRef`: `n`, `title{ar,en(,tr)}`, `audio` (optional).
— `StorySibling`: `id`, `level`, `status`, `note` (optional).
— `Attribution`: `ar` (optional), `en`, `reviewStatus` (localized text bag built
from ar/en, `reviewStatus` split out).

**`Chapter` / `Sentence` / `Token`** (`content/samples/wasiyyat-abi-hanifa/chapters/1.json`,
`content/samples/yunus-wa-al-hut/chapters/1.json`):
`chapter` (int), `sentences[]` → each: `id`, `audio` (`[startMs,endMs]` array →
`AudioSpan`, optional), `translation{en,tr}`, `tokens[]`.
— `Token`: `surface{full,smart,bare}` (→ `SurfaceForms`), `lex`, `pos`, `grammar[]`
(optional), `irab{ar,en(,tr)}` (optional → `LocalizedText`), `segments[]`
(optional → `Segment{form,lex,pos}`), `punctAfter` / `quoteBefore` / `quoteAfter`
(all optional).

**`Glossary` / `GlossaryEntry`** (`content/samples/wasiyyat-abi-hanifa/glossary.json`):
`entries` = **map** `lex` → `{ lemma, root?(absent for particles/pronouns/names),
pos, form?(Roman numeral, verbs only), plural?(nouns only), gloss{en,tr}
(no ar), level(int, 0 for names/pronouns), audio?(optional) }`.

**`Morphology` / `VerbParadigm`** (`content/samples/wasiyyat-abi-hanifa/morphology.json`):
`comment` (top-level), `verbs` = **map** `lex` → `{ bab, wazn, masdar, ismFail,
ismMaful?(JSON-null e.g. takallama), irregularity?(hollow/hollow-wawi/
defective-yai), mazi[14], mudari[14], amr[6], note?(optional) }`.
— *Corrects the task brief's shorthand:* keys are **`ismFail`/`ismMaful`** (not
"ismFail/ maful"), and `ismMaful`/`irregularity`/`note` are real optional keys.

**`GrammarNote`** (`content/grammar/inna-wa-akhawatuha.json`,
`content/grammar/badal.json`):
`id`, `title{ar,en(,tr)}`, `level`, `group` (nahw/awamil/sarf), `amil` (optional
string, awamil only), **`classicalSources[]`** (array of strings),
`explanation{en,tr}`, `examples[]` → `{ar, en, sourceStory?, sentence?}`,
**`commonMistakes[]`** → `{wrong, right, why{en,tr}}`, `relatedNotes[]` (strings),
`gameSeeds{spotTheError:bool}` (→ `spotTheErrorSeed`).
— *Corrects the task brief's shorthand:* the canonical keys are
**`classicalSources`** (not "sources") and **`commonMistakes`** (not "mistakes");
`id`, `relatedNotes`, `gameSeeds` also exist and are modeled.

**`LocalizedText`** (shared, all files): any `{ar?,en?,tr?}` object; `resolve()`
falls back requested→en→ar→"" (mirrors `T()` in `reader.html`). Glosses/translations
carry en/tr; titles carry ar/en(/tr); i'rab carries ar/en(/tr).
