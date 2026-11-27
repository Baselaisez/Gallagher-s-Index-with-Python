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

## 2026-11-27 03:20 UTC

Landed: v354-S `fe83622` — speed VII, measured alone on the machine (A/B alternated, 4× CPU): the core slice 0.83 → 0.49 MB gzip (a story's about text with its body; ALFIYYA_JSON and AMTHAL in the last body slice — each proved equal to the repository reader's); door at 4 Mbit/s 6.22 → 5.49 s, at 20 Mbit/s 2.00 → 1.78 s; on a 6× CPU phone with slow 4G 6.49 → 5.84 s; the 0.4–0.9 s freeze after the games hub was a background drip meeting the vowelling engine cold — it now waits for the warm-up. The shelf-scroll dip of v350 was machine load (0 long tasks alone on both builds). Whole suite 643 of 643 on this tree; entrance test passes. CI green on every earlier commit of the round (`c50adf7`).

Nothing is running. Still slow (named in CLAUDE.md «v354-S»): the sentence sheet's heaviest deferred task (~250 ms at 4×), the Jumla lab's first analysis (`DabtEngine.decide` ×5, no cache proved safe), the first word tap at 6× (~280 ms).

Queued for the owner's word on budget: the engine round (Ibn ʿAqīl's 189 ⚠ rows, the hand-overs of the 2026-11-26 19:55 entry, moving ارْتَدَعَ from L to C).

Waiting on people:
- the owner: his ear on the two voice samples (the generated voice is off); whether the Iẓhār course feeds Today's lesson; the archive.org item; a phone test of «Dinle» and of the guide in the new APK;
- the hoca: packet o08 and the earlier packets on the precheck branch; the vowels and listed doubts of the two new shelves (19 packages); the renderings (reasons 156, verses 23, the uṣūl cards, the course's English lines).

## 2026-11-27 06:22 UTC

Owner, 2026-11-27: «For Iẓhār feed: yes. You can go on with Ibn ʿAqīl. And you find a voice package.» A new round started at about 04:35 UTC. APK run 25 and Pages run 20 were built from `62efd0b` (everything up to speed VII); CI green on it.

Running:
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v355-N1 | qissa-feed1 · tmp/aqiln1 | aqiln1 | Ibn ʿAqīl's work order, the pillars (≈ 100 ⚠ rows) + the older hand-overs in the same engines | triage done; found that every nāʾib probe was a false ⚠ (the probe's regex never matched «نائب») |
| v355-N2 | qissa-feed2 · tmp/aqiln2 | aqiln2 | Ibn ʿAqīl's work order, the complements and followers (≈ 89 rows) | triage: 16 artefacts, 30 real gaps, 22 probe faults, 30 not decidable; fixes started |
| v355-T | qissa-sarf · tmp/iztoday | iztoday | the Iẓhār course in Today's lesson | built, two checks green, full suite running |
| v355-V | qissa-audit · tmp/voice2 | voice2 | a voice the app can ship (web survey, licences quoted, the 30-sentence test) | two neural candidates tested and failed so far: one overrides written vowels (8 seen), one cannot keep ص ض ط ظ apart; survey continues |

Merge note for N1 + N2: both rebuild Ibn ʿAqīl's ledger — merge their `<scratch>/ledger_rows.json`, then rebuild once on the merged page.

## 2026-11-27 08:17 UTC

Landed since 06:22: `297cd01` v355-V (voice survey + Azure adapter; CI failed on it — the Azure key check sat after the ffmpeg
check and the CI runner has no ffmpeg), `4a54bf7` v355-N1 (24 rules, three Roles345 hand-over gates, the CI fix), `091186e`
v355-N2 merged (18 rules; one ledger road for both triages — Ibn ʿAqīl's ledger on the merged page: applied 391, ⚠ 4, n-a 249;
N1 alone 333 / 90, N2 alone 304 / 104). CI is running the whole suite on both. v356-G (the inventory guard) is being merged:
`content/inventory.json` refreshed on the merged tree, then pushed.

The owner, 2026-11-27 (three messages): «Neden?» must give the iʿrāb details of EVERY kind of word (هو: a ḍamīr → mabnī → no lafẓī
or taqdīrī iʿrāb → maḥallan marfūʿ); stories at different levels from Shamela 1686 (Ibn Saʿd's Ṭabaqāt); the Alfiyya and its sharḥ
for learning, applying, checks; ONE story with many parts = al-Nadwī's «السيرة النبوية» (Shamela 9914; he states he has
al-Nadwī's permission); Shudhūr's web text = Shamela 6969; more level-one notes — the Amthila in detail and the pronouns through
«مَا أَنْصَرَهُ وَأَنْصِرْ بِهِ»; «where are the hoca checks I can revise» → one workbook made from the precheck branch's
`review/ai-precheck/*.jsonl` and this branch's `story-corrections-proposed-*.jsonl` (1,557 applied + 128 rule passes + 9 AI-RET +
721 proposals; reports/ is git-ignored — sent to the owner; the generator is scratchpad/hoca_book.py).

Running (five agents, briefs in scratchpad `V357_BRIEF.md`, `V358_BRIEFS.md`):
| wave | worktree / branch | scratch folder | job |
|---|---|---|---|
| v357-N | qissa-why · tmp/naw357 | naw357 | `Illa346`: the kind of word → muʿrab / mabnī → lafẓī / taqdīrī / maḥallī for every class; deduced places marked |
| v358-T | qissa-feed1 · tmp/tabaqat358 | tabaqat358 | 8–10 short stories at levels 2–6 from the Ṭabaqāt (its long story dropped — the Sīra is the long one) |
| v358-A | qissa-feed2 · tmp/alf358 | alf358 | the Alfiyya as a course: verses, ruling, book examples, applied in stories, engine-proved checks |
| v359-S | qissa-speed · tmp/sira359 | sira359 | al-Nadwī's Sīra as ONE package, first instalment from الفصل الثاني, chapter ids append-only |
| v359-E | qissa-audit · tmp/emsile359 | emsile359 | level one: the Amthila (24 forms, muṭṭarida) and five pronoun notes, every cell engine-proved |

Downloads (scratchpad/newsrc/dl/): 1686 (≈3,100 pp.), 9914 (767 pp.), then 6969 (602 pp. — Shudhūr, for a check of our
source file against the web text; no agent yet). Waiting on the owner: the Azure Speech resource's region.
After these land: the speed checks on the merged tree, APK (dev ref) and Pages (ref main).

## 2026-11-27 09:32 UTC

Landed since 08:17 (CI green on the whole suite for `4a54bf7`, `091186e`, `5b828bb`, `2d4092c`): `5b828bb` v356-G (the inventory
guard), `2d4092c` v357-N («Neden?» says the kind of iʿrāb of every word: 67,243 tokens, 234 deduced places marked, 0
contradictions), `f22e81a` v358-A (the Alfiyya as a course: 72 units, 1,006 verses, 806 rulings, 1,090 proved questions),
`e83ba83` v359-E (level one: 19 Amthila and pronoun notes, 493 cells engine-proved).

**The owner, 2026-11-27: «After all those current works are done you can stop and do optimisation. Then I'll give the hoca
reviews. Those current developments and traced ones can also be given to the agents. All of 358–360 have to be done.»**
So: no new round. The waves below are the last; then ONE optimisation pass alone on the machine, the APK, the closing entry,
and the scheduled trace is disabled.

Running (five agents; briefs `V358_BRIEFS.md`, `V360_BRIEF.md`, `V361_BRIEFS.md` in the scratchpad):
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v358-T | qissa-feed1 · tmp/tabaqat358 | tabaqat358 | 8–10 short stories at levels 2–6 from the Ṭabaqāt | authored; pins re-measured; second subset running |
| v359-S | qissa-speed · tmp/sira359 | sira359 | al-Nadwī's Sīra, ONE package, first instalment | built, its check green, audit triaged; speed measure and subset left |
| v360-Sh | qissa-why · tmp/shudhur360 | shudhur360 | Sharḥ Shudhūr whole from the web text (source `scratchpad/sharh-shudhur-src.txt`) | on the unread half (web pp. 455–602) |
| v361-D | qissa-feed2 · tmp/determ361 | determ361 | the engines' order-dependence; مَحْسِبٌ; Ibn ʿAqīl's last four ⚠ rows | started |
| v361-N | qissa-audit · tmp/naw361 | naw361 | «Neden?» second pass: the pronoun inside a word, the follower's place, sign-less lines; engine misreads split from the review list | started |

Merge notes: v360-Sh and v361-D both touch the engines' post lists and may both rebuild ledgers — rebuild Ibn ʿAqīl's ledger and
the Alfiyya course once on the merged page; `content/inventory.json` is refreshed (`tools/inventory.py --write`) at every merge.
Load: checks that only read slow with five browser jobs on the machine (v317's reload step, the v341 door, a game detour) are
re-run alone before a push — the door is 1.07–1.10 s alone (budget 1.8).

Waiting on people: the hoca's reviews (the workbook sent on 2026-11-27 from `scratchpad/hoca_book.py`; the review lists named in
CLAUDE.md's last sections); the Azure Speech resource's region for the man's voice. Left for the hoca, not for agents (they
change authored lines): the tāʾ segments, the kit wording.

## 2026-11-27 10:30 UTC

Landed since 09:32: `f239eca` v358-T (eight Ṭabaqāt stories, levels 2–6; 110 stories), and with this entry v360-Sh (Sharḥ Shudhūr
whole) plus the fix of a red CI.

**CI was red from `e83ba83` to `f239eca`; the whole suite run locally on `f239eca` (589 of 595) named it:** (1) «wave 74» — the
search for «إِنَّ» listed the new Amthila notes before the note of إِنَّ (the fold matches «ـان» inside any title and the new group
sorts first): `DoctrineSearch.word362` now ranks a whole-word title match above a substring. (2) Two FALSE «unsaid» readings the
Ṭabaqāt's akhbār showed, fixed in `HadhfEngine` rule 22: «قَالَ رَجُلٌ لِأَبِي بَكْرٍ» (the doer, then the one addressed) and «يَقُولُونَ
رَبُّكَ اللَّاتُ» (a whole sentence). (3) Pins the new stories moved, each re-measured with its reason in the check: wave 184 «مَا»
wrong 56 → 57 («بَعْدَ مَا طُعِنَ», an engine miss), the Tartīb audit 2684/1015/0, the Hadhf rate with the Ṭabaqāt measured apart
(the v333 rule). (4) «v349 voice A/B» read slow under load 5 and passes alone. **Lesson, now the rule for the remaining merges:
a STORY wave's merge subset includes wave 74, wave 184, v316, v334 and v349 — or the whole suite runs in the spare worktree
(qissa-sarf) before the push.**

Reported and waiting to merge (snapshots committed on their branches): v359-S instalment 1 (`95728b1`, chapters 101–106, 520
tokens), v361-N (`3db1de6`, pronoun ladders on 20,687 tokens, 722 followers, 6,379 class-given signs, 26 engine misreads fixed).

Running:
| wave | worktree / branch | scratch folder | job | progress |
|---|---|---|---|---|
| v359-S | qissa-speed · tmp/sira359 | sira359 | the Sīra's second instalment, chapters 107+ | chapter 110 authored; 111–112 next |
| v361-D | qissa-feed2 · tmp/determ361 | determ361 | the engines' order-dependence; مَحْسِبٌ; Ibn ʿAqīl's last four ⚠ rows | built; its subset running |

Then: merge v359-S (1) + v361-N together (re-measure v345 Sign / taʿalluq / v345-D, wave 184, Hadhf, Tartīb on the merged tree —
both story waves pinned from older bases), then v361-D + the Sīra's second instalment, then ONE optimisation pass alone on the
machine (it includes the windowed chapter render the Sīra needs before ~30 chapters), APK + Pages, the closing entry.
For the next engine work order (not this round): «بَعْدَ مَا» + verb read as a built noun; v360's four ⚠ rows (SH445.1, SH517.1,
SH535.1, SH543.1); the search's substring fold on two-letter terms.

## 2026-11-27 12:50 UTC

Landed since 10:3x: `342c868` v360-Sh + the CI fix (CI green), `601d94c` v361-N (CI red: its own 390 px check went home at
phone width, where a story has no «← Library» button — fixed in the next commit), `3e9b9e1` v361-D (CI green), and with this
entry v359-S — al-Nadwī's Sīra, ONE package, chapters 101–112, 1,127 tokens; 111 stories. **Every wave of the round has landed.**

The Sīra merge was gated by the WHOLE suite, twice (657 of 664, then 664 of 664) — the first run found what a subset would not:
- a name hid a word: the glossary's «الْقَيِّم» (Ibn al-Qayyim) had no root and took «الْقَيِّمِ» of ق و م from the engines (the
  Talkhīṣ's ishtiqāq in «فَأَقِمْ وَجْهَكَ لِلدِّينِ الْقَيِّمِ») — the name carries its root now;
- «مَالُكَ» typed was read as the name «مَالِك» the lineage brought: `RootFinder.nounFromCorpus` (v362) rejects a NAME look-alike
  that the word's own inner vowels contradict;
- one false «unsaid» reading (ishtighāl on «نَسَمَةً مُبَارَكَةً وَحَسَدَتْهَا») fixed in HadhfEngine; «الْإِثْنَيْنِ» off the
  class-given-sign rule; the Kāfiya order check knows the one keyed order (109:s4, judged C); v327's kāna ceiling 55 (a complete
  kāna); two «first token of a kind» finders made exact;
- three glossary keys both story waves had made: «بِلَال» and «حَبَشِيّ» are one entry now; «فَيْء» was TWO words (the spoil in
  the Ṭabaqāt, the shade in the Sīra) — the shade is `fay-shade`.
Pins on the merged shelf, measured: v345 Sign miss 65, taʿalluq 244 / 215 (v353-I with it), إِنَّ miss 22, v345-D contra 330,
wave 184 «مَا» wrong 57, Tartīb 2739/1021/1, Hadhf false 1 with the Ṭabaqāt and the Sīra measured apart.

Running next (alone on the machine): **v362-S, the closing optimisation pass** — qissa-why · tmp/speed362 · scratch speed362 ·
brief `V362_BRIEF.md` (re-baseline against v354; the windowed chapter render and «Bölüm 1 … n» for the Sīra; cheap pre-tests
for Murib.line's post rows, proved equal over the corpus; the load-fragile checks made robust). Then APK (dev ref), Pages
(ref main), the closing entry, and the scheduled trace disables itself.

Rule kept from today: a STORY wave is gated by the whole suite (in the spare worktree qissa-sarf if the dev worktree is busy),
never by a subset — three of today's four red CI runs were story waves pushed on a subset.
For the next engine work order (after the hoca's reviews): the items judged E in the delta files of the Ṭabaqāt and the Sīra
(ẓurūf hung on the prayer formula ×14, «بْنِ» after a badal, «حِينَذَاكَ», «بَعْدَ مَا» + verb); v360's four ⚠ rows; a lexicon
index that keeps a name and a common noun of one spelling apart by context, not by one entry.

## 2026-11-27 15:58 UTC — the round is closed; waiting for the hoca's reviews

Landed since 12:50: `9f9a703` v359-S (CI: one run failed and passed on re-run with nothing changed — a timing check; the measures
were made robust in this wave) and, with this entry, **v362-S — speed VIII, the closing optimisation pass** (whole suite on the
merged tree 668 of 668; inventory green, 0 text / iʿrāb / translation hashes changed).
- The windowed chapter render (22 stories: more than one chapter and > 80 sentences or ≥ 10 chapters): the opened chapter
  node-for-node the full render's; the Sīra opens 349 → 241 ms at 4×; a 150-chapter copy jumps to its last sentence in
  0.2 s (was 2.8) and holds 1,733 nodes (was 21,944). One helper `chOrd362` prints «Bölüm 1 … 12» for the Sīra; `ch.n` and
  every stored key unchanged.
- The post rows' letter helpers remembered: −28 % in the rows, Murib.line −4.5 % over the corpus; 95,333 lines identical.
- The load-fragile measures made robust (v341 door, v343 fresh query, v349 voice A/B, toLibrary, a game detour); no ceiling widened.
- Against v354: the door at 4 Mbit/s 5.49 → 5.79 s and all bodies 7.62 → 8.01 s — download size only (app.js +83 KB gzip, the
  bodies 11.95 → 12.50 MB gzip); no function slower. Still slow: the Jumla lab's first analysis (DabtEngine.decide runs
  three times per sentence; a memo was tried and dropped — decide changes the rows it reads), the sentence sheet's heaviest
  background task (~250 ms), «Dinle» on a very long text.

**The round, 2026-11-27, in one list** (all on `claude/arabic-app-research-ozd58s`): v355-N1 / N2 (Ibn ʿAqīl: 42 rules, ledger
395 applied / 0 ⚠), v356-G (inventory guard), v357-N + v361-N («Neden?»: the kind of iʿrāb of every word, pronoun ladders,
followers, class-given signs), v358-A (the Alfiyya course), v359-E (19 level-one notes: the Amthila and the pronouns), v358-T
(eight Ṭabaqāt stories), v359-S (al-Nadwī's Sīra, one story, chapters 101–112), v360-Sh (Sharḥ Shudhūr whole), v361-D (one
sentence, one answer; مَحْسِبٌ), v362-S (speed VIII). 111 stories, 354 grammar notes, 170 reasons, 668 checks.

**Nothing is running. No new round is started** (the owner, 2026-11-27: «After all those current works are done you can stop
and do optimisation. Then I'll give the hoca reviews.»). The scheduled trace is disabled with this entry.

Waiting on people:
- the hoca's reviews — the workbook `03-hoca-kontrol-2026-11-27.xlsx` (generator `scratchpad/hoca_book.py`; 1,557 applied
  corrections on the precheck branch + 128 rule passes + 9 AI-RET + 721 proposals), `research/irab-kind-review-2026-11-27.md`
  (140 author-side lines), the «for the hoca» lists of v358-T, v359-S, v359-E, v360-Sh, v361-D in CLAUDE.md;
- the Azure Speech resource's region (then the key through the secure form) for the man's voice — the app's voice stays off.
Left for the hoca, not for agents (they change authored lines): the tāʾ segments, the kit wording.
When work resumes — the next engine work order is already listed: the E-judged items of the Ṭabaqāt and Sīra delta files
(ẓurūf on the prayer formula, «بْنِ» after a badal, «حِينَذَاكَ», «بَعْدَ مَا» + verb), v360's four ⚠ rows, a lexicon index that
keeps a name and a common noun of one spelling apart, DabtEngine.decide once per sentence; the Sīra continues at chapter 113
(«مثال غريب من التعصّب الدينيّ …», about 2,000 tokens left of Faṣl 2).

## 2026-11-27 17:46 UTC — v363-E: the misses the new stories exposed (one agent, on the owner's word)

The owner, evening: «I'll give you the hoca reviews this weekend. … We can run Engine for new stories with not much usage of
tokens.» Read as the go-ahead for the engine work order the closing entry listed; ONE agent, a brief with a token budget
(`scratchpad/V363_BRIEF.md`), about 280,000 tokens.
- Closed 27 of the 33 «E» records of the Ṭabaqāt and Sīra delta files; the shelf's audit 1,400 → 1,371, FIXED 29, BROKEN 0.
  A the prayer formula is transparent to taʿalluq (12; taʿalluq 244 → 232); B «أَنَّ» after a transmission phrase (4; 22 → 17);
  C signs and segmentation (7; sign 65 → 60); D the case layer — «بْن» past a badal / naʿt, «سَاوَا», «بَنُو» the doer (4; 330 → 323).
- Left: 107:s6:11 and 108:s6:16 (a new clause at «وَذٰلِكَ» / «وَالْفَرْقُ» is not decided by the letters); the optional group
  («بَعْدَ مَا» + verb, «فِيمَا بَعْدُ», the nominal ḥāl «وَعَلَى رَقَبَتِهِ أَثْوَابٌ», talkhis 14:s4:2); v360's four ⚠ rows; the lexicon
  index for name / common-noun homographs; decide once per sentence.
- «وأنّه مِنَ الْغَلَطِ» (Sīra 111:s3:10) no longer shows as a contradiction (the engine now carries the fatḥ over the ʿaṭf) — it
  STAYS on the hoca's list: the print's hamza against the sense is his to decide.
- `LEX_OFF361` lost «ithnayn-monday»: SignEngine reads the word as the dual's now.
- Whole suite on the wave's tree 669 of 669 (the new check «v363 — the misses the new stories exposed»); inventory green,
  0 text / iʿrāb / translation hashes changed.
- The voice: the owner chose the Saudi man's voice (ar-SA-HamedNeural, the adapter's default) and has not opened the Azure
  Speech resource yet (West Europe is fine); the key comes through the secure form when he says it is ready. The app's voice
  stays off.
Still waiting for the hoca's reviews; nothing else is running.
