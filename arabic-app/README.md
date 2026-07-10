# Qissa (working title) — Arabic Graded-Reader & Audiobook App

A DuChinese-style app for learning Arabic through graded Islamic stories and audiobooks:
tap-word dictionary, grammar deep-dives with common-mistake warnings, SRS flashcard games,
and a lite/premium subscription model with continuously updated content.

## Repository layout

| Path | Contents |
|---|---|
| `research/` | Competitive research (DuChinese, Arabic market gap) |
| `docs/` | Product spec, MVP scope, data model, analyzer/app-store architecture |
| `content/grammar/` | **Global grammar registry** — one bilingual (EN/TR) note per topic, shared by every story and every analyzed upload |
| `content/samples/` | Editorial story packages (pilot: وصية أبي حنيفة) |
| `content/user-uploads/` | Packages produced by the LLM analyzer from user-uploaded classical texts (demo: hadith إنما الأعمال بالنيات) |
| `prototype/` | Self-contained interactive reader prototype (open `reader.html` in a browser) |
| `tools/` | Pipeline tooling: `validate_content.py` (quality gate), `build_prototype.py` (package → reader), `analyze_text.py` (upload-your-own-text LLM analyzer) |

## Status

- [x] Competitive research (DuChinese + Arabic landscape) — `research/01-duchinese-competitive-research.md`
- [x] Product spec v0.1 — `docs/02-product-spec.md`
- [x] Content data model + pilot sample — `docs/03-content-data-model.md`, `content/samples/wasiyyat-abi-hanifa/`
- [x] Interactive reader prototype v0.3 (tashkeel toggle, tap-word, sarf tables, i'rab, awamil, flashcards) — `prototype/reader.html`
- [x] Grammar note library (14 notes: sarf / nahw / awamil, each with common-mistakes; classical sources cited: Emsile, Bina, Awamil, Izhar, al-Kafiya, Qatr al-Nada) — `content/samples/grammar/`
- [x] Content validator — `tools/validate_content.py` (tashkeel-layer consistency, lex/grammar refs, audio spans, paradigm shapes)
- [x] Wasiyya chapter 2 (the first counsels: إنّ وأخواتها، لا الناهية، إذا الشرطية) — 48 tokens, 100% i'rab coverage, 14 verb paradigms
- [x] Prototype build pipeline — `tools/build_prototype.py` regenerates the prototype from content packages (packages are the single source of truth)
- [x] Bilingual EN/TR: UI language toggle in the reader; all grammar notes carry English and Turkish explanations and mistake notes
- [x] Global grammar registry (`content/grammar/`) — same note everywhere a topic appears, in stories and uploads alike
- [x] LLM analyzer ability — `tools/analyze_text.py`: upload classical Arabic → full package (tashkeel layers, EN/TR/AR i'rab, glossary, registry-linked grammar) → validated → standalone reader; demo package committed
- [ ] Deepen grammar notes from uploaded studies of al-Kafiya / Izhar / Qatr al-Nada (pending user uploads)
- [ ] Wasiyya chapters 3+ and the level-4 sibling package
- [ ] Flutter scaffold + backend v1 (see docs/04-analyzer-service.md for the store roadmap)
- [ ] Content pipeline: morphological analysis + forced audio alignment; server TTS for uploads
