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

## 2026-11-26 19:15 — round 2 landed with speed V and the reasons; voices merging; two agents on the new books

Landed since the last entry (dev branch):
- `ad32ec4` — four books received from the owner, verbatim and page-marked in `research/sources/`: Shaykhzāde's Sharḥ Qawāʿid al-Iʿrāb, al-Bakrī's Faṣl al-Maqāl, al-Raḍī's Sharḥ al-Shāfiya, Ibn Mālik's Sharḥ al-Kāfiya al-Shāfiya. (The archive.org item could not be reached.)
- v346 `78bb934` — «Neden? / Why?»: the reason chain (role → family and state → governor → kind and sign → what the sign tells) in the word sheet, the games' feedback, the role notes, the sentence sheet and the lab; 0 contradictions with the authored lines over 87,818 tokens.
- v345-Q `44a8cc6` — al-Maqṣūd open 204 → 0; the typed iʿlāl road agrees with the derivation on 671 of 673 forms of the eighteen models.
- v345-R, v345-T, v345-D and v343-S together `1d15db3` — full gate 609/609:
  - roles: nāʾib al-fāʿil 514 → 569 of 623 agreeing, أَمْ / لَا / حَتَّى as ʿāṭifa, the khabar of lā 4 → 51 of 82; sign contradictions 141 → 58; naḥw ledgers — Shudhūr open 0, Qawāʿid 21, Iẓhār 2, Kāfiya 2; ⚠ rows 79 → 24;
  - taʿalluq contradictions 307 → 228; إِنَّ / أَنَّ 27 → 15; order 2 → 0;
  - the vowelling engine on authored text: contradictions 663 → 303 (the page's own marks choose between the readings it sees; blind vowelling of typed text unchanged);
  - speed V: first-use tasks over 200 ms about 100 → 10–19 at 4× CPU; the shell copy proved offline by a check; covers as bitmaps.

Merging:
- v347 «Dinle» (`tmp/voice347`, 40f3b72): the listening bar, the Arabic voice sheet and no-voice message, the Android speech plugin (untested on a phone), the narration studio and packs. On the merge a page-wide `:has()` rule cost 1.7 s at the door; replaced by a class set in showSheet / closeSheet (door 2.86 s → 1.08 s at 4× CPU).

Running:
| wave | worktree / branch | job |
|---|---|---|
| v348-F | qissa-feed1 · tmp/ilal348 | the commentaries' reasons (Shaykhzāde whole first) into the notes, the reason chain and a game round |
| v348-A | qissa-feed2 · tmp/amthal348 | the proverbs' index and a first shelf «الأمثال» from Faṣl al-Maqāl |

Waiting on people:
- the hoca's answers (this weekend); the story-correction proposals (64 certain + 4 + 3 new); the renderings (al-Inṣāf, Marāḥ pp. 145–182, al-Maqṣūd's 78 units, the 28 role definitions of v346); 304 lines whose role and stated case disagree;
- the owner: the archive.org item's title or file; who records the narration; whether to price a generated voice (778,063 characters for the shelf); whether the «Neden?» ladder should always open in full.

## 2026-11-26 20:00 UTC

Landed since the last entry (dev branch):
- v347 `f9d202f` — «Dinle»: the listening bar, the voice sheet and the no-voice message, the Android speech plugin, the narration studio and packs; the page-wide `:has()` rule that cost 1.7 s at the door replaced by a class.
- `2cf1075` — owner, 2026-11-26: «Neden?» opens on touch only (word sheet and game feedback start as the one-line summary); a check forbids `body:has(…)` / `html:has(…)` / `:root:has(…)`.
- v348-F `6baad21` — the commentaries' reasons: 90 reasons from Shaykhzāde, Ibn Mālik and al-Raḍī, verbatim and anchored, in the notes' «Neden böyle?», the reason chain's family → state and kind → sign steps, the rule of the day on alternate days, and the game round «لِمَاذَا؟». APK run 22 built from this commit; CI (the whole suite) passed on `2cf1075`, running on `6baad21`.

On the hoca's branch (`claude/ai-precheck-2026-11-17`, never merged by us):
- o08 `6fe9802` — the triage's 67 «certain» story corrections compared with that branch: 55 were already corrected there, 1 is on a package the branch does not hold, 10 applied with book citations, 1 judged right as authored (Talkhīṣ 4:s3 ارْتَدَعَ: the seat of jazm on the VERB is the commentary's own ruling, Shaykhzāde l.398).
  Follow-up for the next engine round on dev: move that record from L to C (pins: L 650 → 649, C 102 → 103, certain 64 → 63), and re-word the two T-J01 proposals (قَتَلْتُكُمْ, جَاءَكُمْ) to keep «الفعل وحده في محل جزم».

Running:
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v348-A | qissa-feed2 · tmp/amthal348 | amthal348 | the proverbs' index (746 records) and a first shelf «الأمثال» from Faṣl al-Maqāl | 11 packages (12 chapters, ≈1,250 tokens) authored and valid; audit judged; full suite running |
| v349-V | qissa-audit · tmp/voicein349 | voicein349 | the app's own Arabic voice (owner: «a voice within the app») | the one neural Arabic voice reachable is non-commercial → unfit; a formant voice reading by the app's own phonemes scores 30/30 on the endings test; delivery path built; steered: audio is rendered at deploy time, never committed; two sample files for the owner's ear |
| v350-S | qissa-speed · tmp/speed350 | speed350 | speed VI on the whole of today's app | sentence sheet first paint 3.98 s → 0.32 s cold; word iʿrāb tab cold 0.58 s → ≈0; labs stepped; budgets and suite pending |

Hand-overs still open for the next engine round: DabtEngine (a noun after a passive → nāʾib; the five verbs after أَنْ), JumlaMahallEngine `claimed()` for an open مَنْ / مَا mubtadaʾ, SentenceAnalyzer (أُكْرِمَكَ after إِذَنْ), InnaEngine R83 (kasr after حَيْثُ), أَحْوَجَ kept sound, 20 WujuhEngine face probes, Qawāʿid's 21 open rows; contradictions left — case 303, taʿalluq 228, clause 114, sign 58, inna 15; 44 topics without a book reason (why the fāʿil is rafʿ needs Asrār al-ʿArabiyya or the unscanned parts of Ibn Mālik and al-Raḍī).

Waiting on people:
- the hoca: his answers (this weekend); packet o08 with the earlier packets; the 586 «likely» proposals (not applied); the renderings (al-Inṣāf, Marāḥ pp. 145–182, al-Maqṣūd's 78 units, 28 role definitions, 84 commentary reasons); 304 lines whose role and stated case disagree;
- the owner: the archive.org item's title or file; a phone test of «Dinle» in the APK; his ear on the app's own voice once the samples are ready; who records the narration.
