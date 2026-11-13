# Qissa — architecture of the neuro-symbolic engine

This is Step 1 of the engine brief: how the four pillars map onto the repository as it
stands, what was added for Step 2, and what waits for approval (Steps 3–4).

## The principle: one law table, two interpreters

A grammar rule lives once, as data, under `content/rules/`. Two programs read it:

| Interpreter | Where | Role |
|---|---|---|
| Reader engines (JavaScript classes) | `prototype/reader.html` | what the learner uses, offline, on a phone |
| `qissa_core` (typed Python) | `qissa_core/` | the testable reference: unit tests, tooling, ingestion |

Both must agree on one shared, hand-verified fixture file. The smoke test checks the
reader against it; `python3 -m unittest discover -s qissa_core/tests -t .` checks the
Python side. A rule that is in one interpreter and not the other fails a gate.

First table: `content/rules/ishtiqaq.json` (derivation). Fixtures:
`content/rules/ishtiqaq_fixtures.json` (70 derivations).

## The four pillars and where they live

```
arabic-app/
  content/
    rules/            law tables, schemas, citations, induced tendencies   <- pillar 3a
    sources/          source manifests (how a printing's matn is read)
    samples/          story and treatise packages           <- pillar 3b, calibration corpus
    grammar/          lesson notes linked from tokens
    catechism/        question-and-answer banks
    models/           fitted weights of the small models    <- pillar 2
  qissa_core/
    core_grammar/
      sarf/           Root, Wazn, PhonologicalRule, Deriver, Analyzer, SemanticDeducer
      nahw/           reserved (Step 3)
    ml_engine/        induction: proposals, a promotion gate, tendencies written as data
    ingestion_pipeline/  pdf_layer, treatise (matn, sections, records, citations), schema
    memory_store/     Lexicon and the growing SQLite store
    tests/            unit tests on the shared fixtures
  prototype/reader.html   the app: every engine as a class
  tools/              builder, validators, authoring pipeline, model fitters, smoke test
```

### Pillar 1 — the deterministic rule engine

The reader already holds the ṣarf and naḥw engines as classes (iʿlāl, conjugation,
governors, iʿrāb, taʿalluq, ellipsis, waqf, the bayān and badīʿ figures). Step 2 added the
piece the brief asked for by name:

* `Root` — three radicals and their class (sound, hollow, defective, doubled, mithāl, mahmūz, lafīf).
* `Wazn` — a template over ف ع ل with its role and its per-class overrides.
* `PhonologicalRule` — one class per rule; two ordered groups (the shared iʿlāl rules, then the noun rules).
* `Deriver` — BUILD: root + wazn → origin form → each rule that fires → surface.
* `Analyzer` — READ: peel clitics, lay the stem on inverse templates, rebuild each candidate
  root, keep only a rebuild that lands on the written word vowel for vowel (analysis by synthesis).
  The inverse templates are not written by hand: they are what the builder makes of each
  root class with unknown radicals.
* `SemanticDeducer` — DEDUCE: the meaning from the root's verb and the wazn's role, in
  English and Turkish (قَتَلَ + فَاعِل → «one who kills / öldüren — katl eden»).

In the reader the same engine is `IshtiqaqEngine`; it feeds the word sheet, the Muḥallil
(typed-sentence reading) and the Türetim lab.

Honesty rules built into the engine:

* A Form I maṣdar and bāb are recited knowledge. The engine names such a shape only where
  the verb's own lexicon entry recites that very maṣdar.
* Where only the bare verb is known, the gloss states the bāb's function and says it is structural.
* Where the root is unknown, only the structure is stated, and only for a fully vowelled word.
* The root family shown to a learner contains only regular (qiyāsī) forms and forms the lexicon recites.

### Pillar 2 — the learning layer

Decision: the runtime models stay small, transparent and on the device. They are the
iʿrāb perceptron (`content/models/irab_model.json`, fitted by `tools/gen_irab_model.js`),
the bāb and figure models, the taggers and the rule miner inside the reader. No external
language model or transformer runs in the app: it must work offline, start fast on a
modest phone, and every verdict must be explainable by a rule or a named feature.

The stories are the calibration corpus. For derivation this is already live: every verb
package recites its active participle, passive participle and maṣdar, and the engine
rebuilds them from the root.

| Calibration (v257) | Rebuilt | Total |
|---|---|---|
| Recited participles and regular maṣdars | 2,990 | 3,025 |

Every miss is a recited exception (a ṣifa standing where the participle would, أَرَى,
اتَّخَذَ, أَحْوَجَ). The floor is gated at 98.5 % in both interpreters.

ML-to-rule promotion is built for its first case (the Form I maṣdar): see Step 3 below.

### Pillar 3 — ingestion and memory

Two kinds of source, two destinations:

* Treatises (the axiom base) → a law table under `content/rules/` plus, where the text is
  also good reading, a package under `content/samples/`.
* Stories → packages under `content/samples/` (reading material and calibration data).

The working story pipeline is `tools/authoring/pkg_from_engine.py`. Only the classical
matn of a printed book is ever transcribed; a modern editor's introduction, footnotes and
apparatus are not.

Memory is the content tree read through `memory_store.Lexicon`, plus the growing SQLite
store described under Step 3.

## Step 3 — ingestion, memory and the learning layer (built)

### Schemas (`content/rules/schema/`)

| Schema | Describes |
|---|---|
| `law_table.schema.json` | a law table: roles, bābs, patterns with overrides, rule sentences |
| `source.schema.json` | a source manifest: a printing, how its matn is told apart, its glyph map, its sections |
| `records.schema.json` | the records mined from a treatise |

`qissa_core.ingestion_pipeline.schema` checks them with no third-party dependency.

### The treatise pipeline (`qissa_core/ingestion_pipeline/`)

```
PDF text layer --pdf_layer--> runs with size and position
   --MatnExtractor--> the matn only (by type size), glyphs folded by the manifest's map
   --Treatise--> sections (by the page each manifest entry names)
   --RecordMiner--> records: objection and answer, definition, statement with its examples
   --cites()--> which law rule is treated in which section, on which pages
```

Run: `python -m qissa_core.ingestion_pipeline content/sources/<id>.json --pdf-dir <dir>`.
It writes the matn and the records under `research/sources/` and the citations under
`content/rules/<id>.cites.json`. A citation is kept only where the rule's own vocabulary
occurs on a page of the section the manifest names: evidence, not a guess.

### The memory store (`qissa_core/memory_store/store.py`)

One SQLite file that only grows: patterns and rules (the law), verbs (what the lexicon
recites), sources with their citations and records, attestations (a derived noun met in a
story, with its root and wazn), and promoted tendencies. Every write is an upsert.

Run: `python -m qissa_core.memory_store` (the file is a build product, not committed; its
summary is `research/memory-summary.json`).

| Memory after the first build | Count |
|---|---|
| Attested derived nouns (tokens) | 5,960 |
| Distinct attested forms | 2,587 |
| Roots with an attested derivation | 495 |
| Verbs recited | 1,334 |
| Citations into Marāḥ | 22 |
| Records from Marāḥ | 114 |

### Rule induction with a promotion gate (`qissa_core/ml_engine/induction.py`)

A Form I maṣdar is recited, yet the books state tendencies. `MasdarInducer` proposes
"if these features, then this shape" over every small set of features (the two recited
vowels, transitivity, root class) and promotes a proposal only through `PromotionGate`:
enough verbs, enough of them agreeing, and a real gain over the rule it refines. A
plurality rule passes only with a strong lift over the shape's base rate, and is labelled.

What it found on 538 verbs matches the classical statements:

| If | Then | Share | Verbs |
|---|---|---|---|
| فَعَلَ, transitive, sound | فَعْل | 75 % | 184 |
| فَعِلَ, intransitive, sound | فَعَل | 50 % | 38 |
| فَعَلَ, intransitive, sound | فُعُول | 47 % | 53 |

Held-out accuracy is 50.4 % against a 46.1 % baseline. That modest number is the point:
the tendency is real but weak, which is why the builder never applies it. The reader shows
it beside a recited maṣdar ("follows the tendency" or "recited against it").

Run: `python -m qissa_core.ml_engine` (writes `content/rules/masdar_tendencies.json`).

## Step 4 — the five sources

| Source | Pages | State |
|---|---|---|
| Marāḥ al-Arwāḥ (two files) | 185 | ingested through the pipeline: 174 matn pages, about 9,200 words, 15 sections, 114 records, 18 law rules cited by section and page |
| Taṣrīf al-ʿIzzī (two files) | 114 | scan, not transcribed; at least the first 27 pages are the modern editor's introduction |
| Sharḥ Shudhūr al-Dhahab, pp. 1–99 | 99 | scan, not transcribed; the opening is the modern editor's front matter |

Marāḥ's printing sets vowel marks and some ligatures as private glyphs. The manifest
(`content/sources/marah-al-arwah.json`) names each one, checked against the page images,
so no letter is lost. Its headings are in a display face that cannot be read as text, so
the manifest states each section's first page and title, checked against the matn's own
opening words. The matn is still marked raw: word spacing and the printing's vowels have
not been collated line by line, so it is cited by section in the app and not shown as text.

The two scans have no text layer. They need page-by-page transcription from the images,
matn only, which is the next piece of Step 4.

## In the app

* The derivation card names where the classical primer treats each rule that fired.
* The root family shows whether a recited maṣdar follows or breaks the induced tendency.
* A new game, "Build the word", is generated by the engine from the verbs the shelf
  recites: build the form, find the root, or say what it means. Wrong answers are the
  origin form, the half-ruled form, the neighbouring wazn or the neighbouring root, and
  the feedback names the rule left undone.

## How to run

```
cd arabic-app
python3 -m unittest discover -s qissa_core/tests -t .     # the Python side (30 tests)
python3 -m qissa_core.ml_engine                            # induce and write the tendencies
python3 -m qissa_core.memory_store                         # build or grow the memory
python3 tools/build_prototype.py                           # embeds the law table in the reader
node tools/smoke_test.js                                   # the reader, fixtures included
```

```python
from qissa_core.core_grammar.sarf import Sarf
s = Sarf()
s.build("ق و ل", "fail-1").rule_ids        # ['hamz-fail']   قَاوِلٌ -> قَائِلٌ
s.meaning("قَائِلٌ").tr                      # 'diyen / kavl eden'
```
