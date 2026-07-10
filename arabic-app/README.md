# Qissa (working title) — Arabic Graded-Reader & Audiobook App

A DuChinese-style app for learning Arabic through graded Islamic stories and audiobooks:
tap-word dictionary, grammar deep-dives with common-mistake warnings, SRS flashcard games,
and a lite/premium subscription model with continuously updated content.

## Repository layout

| Path | Contents |
|---|---|
| `research/` | Competitive research (DuChinese, Arabic market gap) |
| `docs/` | Product spec, MVP scope, data model, architecture |
| `content/samples/` | Sample story packages in the canonical content format (pilot: وصية أبي حنيفة) |
| `prototype/` | Self-contained interactive reader prototype (open `reader.html` in a browser) |
| `tools/` | Content pipeline tooling (`validate_content.py` — run on every package before publish) |

## Status

- [x] Competitive research (DuChinese + Arabic landscape) — `research/01-duchinese-competitive-research.md`
- [x] Product spec v0.1 — `docs/02-product-spec.md`
- [x] Content data model + pilot sample — `docs/03-content-data-model.md`, `content/samples/wasiyyat-abi-hanifa/`
- [x] Interactive reader prototype v0.2 (tashkeel toggle, tap-word, sarf tables, i'rab, awamil, flashcards) — `prototype/reader.html`
- [x] Grammar note library seeded (10 notes: sarf / nahw / awamil, each with common-mistakes) — `content/samples/grammar/`
- [x] Content validator — `tools/validate_content.py` (tashkeel-layer consistency, lex/grammar refs, audio spans, paradigm shapes)
- [ ] Tech-stack decision & Flutter scaffold
- [ ] Wasiyya chapters 2+ (the counsels) and the level-4 sibling package
- [ ] Content pipeline: morphological analysis + forced audio alignment
