# What the app holds — 2026-11-27 (v356-G)

Generated from `content/inventory.json` (`python3 tools/inventory.py --write`; guarded by `--check` in the smoke suite and,
for the tree half, in `tools/release.py`). Every number below is a count the guard refuses to see fall.

## Stories — 102 packages, 899 chapters, 7,320 sentences, 90,147 tokens

| Shelf (`LIB_SOURCES`) | stories | chapters | sentences | tokens |
|---|---:|---:|---:|---:|
| qisas (prophets' stories) | 30 | 211 | 2,127 | 21,055 |
| tarikh (history) | 16 | 76 | 441 | 4,544 |
| mutun (the texts) | 11 | 403 | 3,293 | 49,989 |
| amthal (proverbs) | 11 | 12 | 136 | 1,252 |
| kutub (books) | 8 | 8 | 76 | 1,077 |
| shiʿr (poetry) | 7 | 96 | 648 | 6,091 |
| akhbār (reports and lives) | 4 | 21 | 135 | 1,702 |
| fiqh | 4 | 14 | 67 | 564 |
| ḥikāya | 4 | 16 | 58 | 561 |
| waṣāyā (counsels) | 4 | 21 | 133 | 1,104 |
| practice | 2 | 8 | 57 | 223 |
| maqāmāt | 1 | 13 | 149 | 1,985 |

Each package also carries three hashes: its Arabic text (every token's `surface.full`, in order), its iʿrāb lines (ar/en/tr),
its translations + glossary + morphology. The built page's `STORIES` and the hosted split copy (26 body slices) hold the same
102 stories with the same text hash.

## Grammar

- **Notes**: 335 (`content/grammar`), **2,087 examples**.
- **Catechism**: 15 books, **591 questions**.
- **Rule tables** (`content/rules/`, 77 files): the Alfiyya **1,006 verses**; **156 reasons** (`ilal.json`, 6 books; 24 kinds);
  Inṣāf **121 masāʾil** in 14 bābs; amthāl index 744 records; commentary links 2,709; ishtiqāq law 51 patterns / 24 rules
  (+70 fixtures); Iẓhār map 100 items, 100 Turkish units; sarf ledger 4,260 probes; tables of contents (Ibn Mālik 143,
  Ibn ʿAqīl 76 bābs, Khaṣāʾiṣ 160, Raḍī 101, Shaykhzāde 69, Iqtirāḥ 116); uṣūl 8 proofs.
- **Coverage ledgers**: 54 books, **6,586 entries** — applied 2,463 · noted 1,048 · shelved 1,827 · not-automatable 453 ·
  open 434 · banked 299 · other 62 (a status moving is progress, not loss: only an entry that disappears fails).

## Engines (read from the built page)

119 classes; 95 of them carry rules as data in **368 static tables, 5,300 rows** in all. Largest: BadiEngine 393 rows,
DabtEngine 392, SentenceAnalyzer 270, IsmKindsEngine 241, FahmEngine 210, WujuhEngine 200 (CLOSED 83, FACE 53), HadhfEngine 151,
MajazEngine 148, TaqdirEngine 139, TashbihEngine 117, MamnuEngine 110, IsmEngine 108, MaqsudEngine 92, TartibEngine 86
(RULES 19), TaalluqEngine 84 (JARR 22), SignEngine 83, IshtiqaqEngine 83, IlalEngine 80 (RULES 26, GATES 15), QawaidEngine 80
(RULES 20), Bab35Engine 62 (DOORS 35), InnaEngine 33 (SEAT 33), JumlaMahallEngine 31 (RULES 20), Nahw342Engine 21 (RULES 21),
Roles345 66 (RULES 10), WaqfEngine 24 (RULES 9). Every row id is listed in the inventory.

## Features (read from the built page)

- **51 games** (`GameFactory.CATALOGUE`), **39 labs** (`LAB_TOOLS`), **12 shelves** (`LIB_SOURCES`).
- Word sheet: 4 tabs (word, sarf, irab, grammar). Today card: 6 step kinds (read, collect, recall, check, strong, izhar).
  Settings: 7 sections (language, theme, level, teacher's review, listening, the voice studio, the guide).
- **1,616 interface strings** in each of English and Turkish (the same keys). **49 `qissa-*` storage keys** named by the code
  (Backup carries every one).
- Data tables in the page: STORIES, GRAMMAR, CATECHISM, ILAL, ALFIYYA_JSON, AMTHAL, INSAF, ISHTIQAQ_LAW, USUL, REF_GROUPS and
  three models (BAB, FIGURE, IRAB) — all reachable in the hosted copy too (app.js + 30 files, ≈ 79 MB before compression).
