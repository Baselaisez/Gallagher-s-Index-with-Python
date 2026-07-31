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
