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

## 2026-11-26 19:55 UTC

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

## 2026-11-26 20:23 UTC

Nothing merged since the last entry; CI passed on `6baad21` and `2bd12f2`.

Owner, 2026-11-26 evening: three more books — al-Suyūṭī's al-Iqtirāḥ (Shamela 14246), Ibn Jinnī's al-Khaṣāʾiṣ (9986; «must be both feeder and text»), Ibn ʿAqīl on the Alfiyya (9904; «so important a naḥw resource, automatable»); «Iẓhār is so important and you have sufficient resource for it»; design improvements; an onboarding guide; speed.

Running (scratch folder = wave tag):
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v348-A | qissa-feed2 · tmp/amthal348 | amthal348 | the proverbs' shelf | audit judged (33 records), full suite running |
| v349-V | qissa-audit · tmp/voicein349 | voicein349 | the app's own voice | delivery path, deploy-time rendering, two samples for the owner's ear; full suite running |
| v350-S | qissa-speed · tmp/speed350 | speed350 | speed VI | fixes in; final A/B and full suite running |
| v351-O | qissa-why · tmp/guide351 | guide351 | the guide (tour on the real screens, one-time hints, «Kılavuz» page) and a design pass | tour built; design audit started |
| v351-I | qissa-sarf · tmp/izhar351 | izhar351 | Iẓhār as a course (`izhar_map.json`, the course page, «söylenir mi?» round, the Iẓhār story's audit) | ledger's two open rows applied; course built; checks next |

Queued (briefs in the scratchpad's V352_BRIEFS.md; start as worktrees free, at most five agents at once): v352-A Ibn ʿAqīl as feeder (qissa-feed1), v352-U al-Khaṣāʾiṣ + al-Iqtirāḥ as uṣūl feeders, v352-K readings from al-Khaṣāʾiṣ as a shelf. Sources: al-Iqtirāḥ 405 pp. and al-Khaṣāʾiṣ 1,357 pp. fetched; Ibn ʿAqīl fetching (scratchpad newsrc/dl/b9904).

## 2026-11-26 22:23 UTC

The container restarted at about 22:00 UTC and killed every process; the worktrees and the scratchpad survived. Three agents (guide + design, the uṣūl feeder, Iẓhār round 2) had written everything and were inside their final full-suite runs: their work is committed on their branches (`tmp/guide351` a049e2f, `tmp/usul352` d71107e, `tmp/izhar353` 25be5eb) and is merged by the orchestrator from their CLAUDE.md sections, with CI's whole-suite run on each push as the gate.

Landed since the last entry (dev branch; CI's whole suite green on each up to `baada46`):
- `02cd67d` — the suite's temporary site copies never outlive a run (180 leftovers, 13 GB, had filled the disk and crashed two full runs).
- v350-S `92cca6c` — speed VI: door usable 1.46 → 0.95 s local and 8.9 → 7.0 s at 4 Mbit/s (4× CPU); the sentence iʿrāb sheet's first paint 3.98 → 0.32 s cold; the core slice 1.62 → 0.69 MB gzip (the grammar tables' bodies in their own slice after the door); settled heap −21 %; the ten `#story:has(.lib-card)` rules a class.
- v349-V `b2c8dfd` — the app's own voice: the delivery path, deploy-time rendering, the endings test (30 of 30 with the app's own phoneme reading). The voice is a formant synthesiser (robotic; ظ said as ذ): **off by default** until the owner has heard the two samples sent to him. APK run 23 and Pages run 18 built from this commit.
- v351-I `5709b65` — Iẓhār as a course: `izhar_map.json` (60 ʿāmil, 30 maʿmūl, 10 signs), the ledger's open rows 2 → 0, «İzhâr dersi» (100 units, 417 exercise items), «يقال / لا يقال».
- v352-A `baada46` — Ibn ʿAqīl: a ledger of 806 rule statements (51 joined, 199 new-applied, 188 ⚠, 156 open, 212 not automatable), the Alfiyya's verses on 108 notes, 35 reasons (15 of the 44 unanswered topics), one rule row (tawkidPron).
- v348-A `6e334da` — the proverbs' shelf «الأمثال»: 11 proverbs with their tales from Faṣl al-Maqāl (1,252 tokens), an index of 651 entries.
- sources `63bc2a8` — Ibn ʿAqīl, al-Khaṣāʾiṣ, al-Iqtirāḥ.

Being merged now, in this order: v351-O (the guide: a seven-step tour on the real screens, one-time hints, the «Kılavuz» page; the design pass — `--muted` defined, 44 px targets, the tarkib sheet's Arabic), v352-U (al-Khaṣāʾiṣ + al-Iqtirāḥ as feeders: the proofs, the 24 kinds of ʿilla, «İki yöntem», 31 reasons — among them why the fāʿil is rafʿ), v353-I (Iẓhār round 2: the owner's Turkish translation leads 75 of 100 units; missing cells 23 → 9; taʿalluq 228 → 224).

Running:
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v352-K | qissa-feed2 · tmp/khasais352 | khasais352 | readings from al-Khaṣāʾiṣ as a shelf (about eight passages, L5–6) | started 22:17 |

Next, in order: speed VII (owner: after all these tasks the optimisation job is done again — alone on the machine, against v350's numbers; carries the shelf-scroll question and v350's «still slow» list); the engine round from Ibn ʿAqīl's 188 ⚠ rows and the hand-over list of the 19:55 entry; renderings for the hoca.

Waiting on people:
- the owner: his ear on the two voice samples (then `app_voice` on, and main's copy of the Pages workflow updated); whether the Iẓhār course feeds Today's lesson; the archive.org item; a phone test of «Dinle»;
- the hoca: packet o08 and the earlier packets; the proverbs' vowels and the listed doubts; the renderings (now also 35 + 31 reasons, 23 verses, the uṣūl cards, the course's English questions).

## 2026-11-27 00:22 UTC

Landed since the last entry (dev branch; CI's whole suite green on every commit up to `9137d90`):
- v351-O `f48d481` — the guide (a seven-step tour on the real screens, six one-time hints, «Kılavuz») and the design pass.
- v352-U `4cb86a9` — al-Khaṣāʾiṣ and al-Iqtirāḥ as feeders: the proofs' plan, the 24 kinds of ʿilla, «İki yöntem» in the khilāf lab, 31 reasons (why the fāʿil is rafʿ among them). `ilal.json` is the union with Ibn ʿAqīl's: 156 reasons.
- v353-I `9137d90` — Iẓhār round 2: the owner's Turkish translation leads 75 of 100 units; missing cells 23 → 9; sifaFail / wasf rows; taʿalluq on the merged shelf 228 / 200 / 735.
- APK and Pages rebuilt from `9137d90` (queued 23:37 UTC). The generated voice stays off.

Running:
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v352-K | qissa-feed2 · tmp/khasais352 | khasais352 | readings from al-Khaṣāʾiṣ as the shelf «مِنْ كُتُبِ الْعَرَبِيَّةِ» | passages authored and guarded; 13 audit records judged; first full suite 618 passed, the threshold checks re-measured the v333 way; second full suite running |

Next, in order: merge v352-K; then speed VII alone on the machine (owner's order); the engine round (task list: Ibn ʿAqīl's 189 ⚠ rows, the hand-overs) waits for the owner's word on budget.

Waiting on people: unchanged from the 22:23 entry.

## 2026-11-27 01:05 UTC

- v352-K merged `(this commit's parent)` — readings from al-Khaṣāʾiṣ: eight passages (1,077 tokens) on the shelf «مِنْ كُتُبِ الْعَرَبِيَّةِ». Every wave of the round has landed; the shelf holds 102 stories.
- Running next, ALONE on the machine: v354-S speed VII (qissa-speed · tmp/speed354 · scratch folder speed354; brief V354_BRIEF.md in the scratchpad).
- Queued for the owner's word on budget: the engine round (Ibn ʿAqīl's 189 ⚠ rows, the hand-overs).

## 2026-11-27 03:25 UTC

Landed: v354-S `fe83622` — speed VII, measured alone on the machine (A/B alternated, 4× CPU): the core slice 0.83 → 0.49 MB gzip (a story's about text with its body; ALFIYYA_JSON and AMTHAL in the last body slice — each proved equal to the repository reader's); door at 4 Mbit/s 6.22 → 5.49 s, at 20 Mbit/s 2.00 → 1.78 s; on a 6× CPU phone with slow 4G 6.49 → 5.84 s; the 0.4–0.9 s freeze after the games hub was a background drip meeting the vowelling engine cold — it now waits for the warm-up. The shelf-scroll dip of v350 was machine load (0 long tasks alone on both builds). Whole suite 643 of 643 on this tree; entrance test passes. CI green on every earlier commit of the round (`c50adf7`).

Nothing is running. Still slow (named in CLAUDE.md «v354-S»): the sentence sheet's heaviest deferred task (~250 ms at 4×), the Jumla lab's first analysis (`DabtEngine.decide` ×5, no cache proved safe), the first word tap at 6× (~280 ms).

Queued for the owner's word on budget: the engine round (Ibn ʿAqīl's 189 ⚠ rows, the hand-overs of the 2026-11-26 19:55 entry, moving ارْتَدَعَ from L to C).

Waiting on people:
- the owner: his ear on the two voice samples (the generated voice is off); whether the Iẓhār course feeds Today's lesson; the archive.org item; a phone test of «Dinle» and of the guide in the new APK;
- the hoca: packet o08 and the earlier packets on the precheck branch; the vowels and listed doubts of the two new shelves (19 packages); the renderings (reasons 156, verses 23, the uṣūl cards, the course's English lines).
