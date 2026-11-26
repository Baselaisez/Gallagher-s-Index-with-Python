# Development trace — November 2026

A dated log of what is running, what landed, and what is waiting. Newest entry last. Times are UTC.

## 2026-11-26 14:30 — round «v342/v343» started

Landed today on the dev branch (all gates green at each push):
- v338 `aeb0b0e` — Today's lesson, chapter-end questions, verification marks (558/558).
- v340 `550f14c` — a calmer door, better sheets, generated covers (563/563).
- v339 `8efa6e5` — al-Inṣāf lab «الخلاف» and game; the clause-maḥall engine; the shelf's grammar audit (568/568).
- v341-S `dea5d51` — speed IV: library before the story text, no stall on first analysis, faster search (572/572).
- `8e0ed4d` — Android build script follows the hashed data file names. APK run 45833758654 and Pages run 45833564338 green.

Running (each agent in its own worktree; nothing merged yet):
| wave | worktree / branch | job |
|---|---|---|
| v342-N | qissa-feed1 · tmp/nahw342 | Shudhūr, Qawāʿid al-Iʿrāb, Iẓhār, Kāfiya: ledger of every rule, then the open rules into engines and notes |
| v342-S | qissa-feed2 · tmp/sarf342 | Marāḥ, Maqṣūd, ʿIzzī: ledger, then the open rules into the ṣarf engines, notes and a catechism bank |
| v342-A | qissa-sarf · tmp/aux342 | every other resource file: ledger, data-side consumption, a ranked engine-gaps work order |
| v342-T | qissa-audit · tmp/triage342 | the story audit's ~1,100 contradictions triaged: line wrong / engine wrong / both right |
| v343-S | qissa-speed · tmp/speed343 | speed V: Android shell proved offline, first-use freezes, two-letter search, heap, core slice, cover scroll |

Waiting on people:
- the hoca's answers (to be uploaded this weekend);
- for the hoca: four authored clause-seat slips (v339-M), the al-Inṣāf renderings, masāʾil 44 and 65 against another edition.

## 2026-11-26 16:25 — round 1 (v342, v344) landed; round 2 (v345) started

Landed since the last entry (dev branch):
- v342-T `cef0400` — the stories' audit triaged: 1,869 engine-versus-story contradictions judged (line wrong 650, engine wrong 1,112 in 30 clusters, both right 102, undecided 5); proposals and an engine work order in `research/`.
- v342-S `2174b6c` — ṣarf ledgers (Marāḥ open 0, ʿIzzī open 0, Maqṣūd open 204), five iʿlāl rules, 381 book lines in the notes; the owner's ruling «اِيتَسَرَ is from ي س ر» applied.
- v342-A `0ef8a54` and v342-N `1888330` — the other resources' ledger (45 ledgers, 66 files, open 74) with an engine-gaps work order; the naḥw ledgers (Shudhūr open 1, Qawāʿid 30, Iẓhār 10, Kāfiya 9; 79 rows a note carries while the engine still misreads the book's example) and `Nahw342Engine`. Full gate 586/586.
- v344 `f2bfa87` — the teacher's review in the app with export, khilāf links, the rule of the day, the level from reading (agent suite 577/577; shared checks re-run green on the merge; the full suite on this exact tree runs with the next merge).

Running:
| wave | worktree / branch | job |
|---|---|---|
| v343-S | qissa-speed · tmp/speed343 | speed V (Android shell offline proof, first-use freezes, two-letter search, heap, core slice, cover scroll) |
| v345-D | qissa-feed1 · tmp/dabt345 | the vowelling engine's 649 case-ending faults |
| v345-T | qissa-feed2 · tmp/taalluq345 | taʿalluq (272), framed clauses (72), إِنَّ / أَنَّ (25), order (2) |
| v345-R | qissa-sarf · tmp/roles345 | role gaps (nāʾib al-fāʿil 145 …), the sign engine, the naḥw ledgers' ⚠ and open rows |
| v345-Q | qissa-audit · tmp/maqsud345 | al-Maqṣūd's 204 open units, the typed iʿlāl road, the missing ʿalāqas |

Waiting on people:
- the hoca's answers (this weekend); the 64 certain story-correction proposals; the al-Inṣāf and Marāḥ pp. 145–182 renderings; six typos in the uploaded sheets.
