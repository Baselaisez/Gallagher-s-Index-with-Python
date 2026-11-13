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
    rules/            law tables (axioms as JSON)           <- pillar 3a
    samples/          story and treatise packages           <- pillar 3b, calibration corpus
    grammar/          lesson notes linked from tokens
    catechism/        question-and-answer banks
    models/           fitted weights of the small models    <- pillar 2
  qissa_core/
    core_grammar/
      sarf/           Root, Wazn, PhonologicalRule, Deriver, Analyzer, SemanticDeducer
      nahw/           reserved (Step 3)
    ml_engine/        reserved (Step 3): trainers, ML-to-rule promotion
    ingestion_pipeline/  reserved (Step 3): treatise -> law table, story -> package
    memory_store/     Lexicon (read-only today); the growing store is Step 3
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

ML-to-rule promotion (a mined pattern proposed as a rule, accepted only after it passes
the fixtures and the corpus sweep) is designed but not built; it is Step 3.

### Pillar 3 — ingestion and memory

Two kinds of source, two destinations:

* Treatises (the axiom base) → a law table under `content/rules/` plus, where the text is
  also good reading, a package under `content/samples/`.
* Stories → packages under `content/samples/` (reading material and calibration data).

The working story pipeline is `tools/authoring/pkg_from_engine.py`. Only the classical
matn of a printed book is ever transcribed; a modern editor's introduction, footnotes and
apparatus are not.

Memory today is the content tree itself, read through `memory_store.Lexicon`. A store
that grows on its own (a SQLite file or graph of roots, patterns, attestations and
promoted rules) is Step 3.

## The five sources uploaded on 2026-11-13

| Source | Pages | Text layer | What it will feed |
|---|---|---|---|
| Marāḥ al-Arwāḥ (two files) | 185 | yes (matn above a modern footnote apparatus) | the iʿlāl and derived-noun chapters of the ṣarf law tables |
| Taṣrīf al-ʿIzzī (two files) | 114 | no (scan; the opening pages are a modern introduction) | bāb functions and verb classes |
| Sharḥ Shudhūr al-Dhahab, pp. 1–99 | 99 | no (scan; the opening pages are a modern editor's front matter) | the naḥw law tables |

Status: inventoried and sampled. Marāḥ's matn has been pulled out of its text layer by type size
(174 pages, about 9,200 words) into `research/sources/marah-al-arwah-matn.txt` — raw and lossy
(private-use ligature glyphs drop letters), so it is working material, not yet text for the reader.
The two scanned books have not been transcribed. The rules in
`ishtiqaq.json` are the standard rules the reader already taught plus eight noun rules;
each will be tied to its place in Marāḥ and al-ʿIzzī when their matn is ingested.

## What waits for approval

* Step 3 — the ingestion and analysis schema: JSON schema for law tables, the treatise
  pipeline (page image or text layer → matn only → rule records → tests), the growing
  memory store, the ML-to-rule promotion gate.
* Step 4 — ingest the five sources through that schema.

## How to run

```
cd arabic-app
python3 -m unittest discover -s qissa_core/tests -t .     # the Python interpreter
python3 tools/build_prototype.py                           # embeds the law table in the reader
node tools/smoke_test.js                                   # the reader, fixtures included
```

```python
from qissa_core.core_grammar.sarf import Sarf
s = Sarf()
s.build("ق و ل", "fail-1").rule_ids        # ['hamz-fail']   قَاوِلٌ -> قَائِلٌ
s.meaning("قَائِلٌ").tr                      # 'diyen / kavl eden'
```
