# Where the AI pre-check stands (2026-11-17, after wave 2)

**Stopped: the Fable 5.2 usage limit was reached before any verdict was written** («resets Nov 19, 3am UTC»).
Nothing in the content has changed on this branch; the student sheets are on hold.

Ready:
- `review/ai-precheck/findings-critical.json` — the 1,297 critical findings (ids, sheet and row unchanged).
- `tools/precheck.py packets` rebuilds the 43 work packets (17 pattern packets D01–D12, then 26 by package,
  engine sources first); `check` enforces the citation rule; `status` prints the resume point.
- `review/ai-precheck/BRIEF.md` — the verifier's brief (verdicts, citation rule, sources).
- `tools/precheck_apply.py` — writes checked AI-ONAY corrections (dry run by default); AI-RET goes to
  `ai-rejections.jsonl` with `confirmed_by_human: false`, which `--learn-from-rejections` ignores.
- `baseline-before.txt` — the gauges before any change: label gauge 90.31 % (32,470 / 35,953), typed gauge 99.92 %
  (1,214 / 1,215), every package validates, drill bank 9,217 rows.

Resume order (once Fable 5.2 answers again):
1. Wave 1 — p-D02-1, p-D02-2, p-D08 + p-D11 + p-D12, p-D03, p-D01-1, p-D01-2.
2. Wave 2 — p-D04-1, p-D04-2, p-D05-1, p-D05-2, p-D06, p-D07.  Wave 3 — p-D09, p-D10-1, p-D10-2.
3. Confirmed patterns → line-level rule passes (taṣrīf/iʿlāl before iʿrāb) through `pkg_from_engine.py` / `polish_pkg.py`,
   rerun on every package, validators + gauges compared with the baseline.
4. The 26 package packets (r01–r26), al-usul-al-munifa first.
5. Sheets 01–17 regenerated with the AI columns; final report.

## Progress (Opus 5.5 by the owner's decision; weekly cap 85 %)

- Wave 1 (D01, D02, D03, D08, D11, D12) and wave 2 (D04, D05, D06, D07) are done: 428 of 1,297 verified.
  Verdicts: see `python3 tools/precheck.py check` (total line). Cost: about 1.5 M + 1.15 M subagent tokens
  (wave 1 moved the weekly meter 67 % → 74 %).
- Next: wave 3 = p-D09, p-D10-1, p-D10-2; then the package packets r01–r26 (al-usul-al-munifa first).
- Rule fixes (from the verifiers' reports): D03, D11, D12 deterministic; D06 deterministic by the glossary lemma;
  D08 for يـ/أ/نـ only; D07 for a bare بْن between names; D02, D04 partial; D01, D05 flag only.

## 2026-11-18 — rule classes for the confirmed patterns, and a sweep for headless lines (Opus 5.5)

`tools/authoring/irab_rules.py` now carries five rule classes, each with its source quoted verbatim from
`research/sources/` and every change logged to `rule-applied.jsonl` (`by: ai`, `confirmed_by_human: false`):

| rule | what | lines |
|---|---|---|
| D03 `AmmaFaRule` | the fāʾ answering أَمَّا (earlier wave) | 24 |
| H01 `HeadlessLineRule` | a line whose ROLE the authoring pass dropped (« بِالْفَتْحَةِ، مُضَافٌ.») — role read off the context: munādā muḍāf after يَا, muḍāf ilayh after بْنِ, majrūr after a jarr letter, غَيْرَ أَنَّ the exception, kāna's postponed noun | 25 (al-uṣūl 22, Maqāmāt 2, ʿIzzī 1) |
| S01 `AmrTakidRule` | a recited emphatic row right after the imperative row holds IMPERATIVES, built (Marāḥ l. 517; Iẓhār l. 186) — ʿIzzī 17:s32 read all six as muḍāriʿ, four of them in rafʿ or jazm | 6 |
| D07 `IbnNatRule` | «بْنُ» without its alif between two names, and the nisba after them, are naʿt — not doers | 3 |
| D06 `ZarfSingularRule` | حِينَ، دُونَ given the sound plural's yāʾ | 4 |

The pattern SCANS in `review_sheets.py` were tightened at the same time: the old ones counted correct lines (the
mulḥaq عَالَمِينَ and the real duals; «عَنِ ابْنِ مَسْعُودٍ» where ابْنِ opens the name; the question hamza of أَتَظُنُّ;
the yāʾ of the woman addressed). After the rules, D06 / D07 / D08 / D11 scan at 0.

### 2026-11-18, later — r01–r03 applied; D04 and P01 rule classes

- r01–r03 (al-Uṣūl, 118 findings): 109 AI-ONAY applied, 1 AI-RET (2:s11 فَإِمَّا — the line is right, the vowel should be
  فَأَمَّا), 8 AI-ŞÜPHELİ for the hoca, three of them readings of the TEXT (6:s7 عَلِمَ/عَمِلَ, 10:s2 الفعل/المفعول,
  11:s1 the wāw of وَتَفَضُّلًا) and four the one choice «أَمَّا بَعْدُ: الْحَمْدُ …» vs «أَمَّا بَعْدَ الْحَمْدِ …» (1:s2).
- D04 `OvertDoerRule` (8 lines): the hidden-doer clause removed where the doer stands written after the verb; the search
  stops at a conjunction or a relative (Maqāmāt 8:s2 «تَعَالَى وَتَرْكُ مَا سِوَاهُ» is left alone). Open for the hoca:
  «لَمْ يَكْفُرْ هٰذَا الْمُسْتَدِلُّ», «يَسْمَعُ ذٰلِكَ الْمَلِكُ» — is the demonstrative the doer and the noun its badal?
- P01 `PronounBuildRule` (1 line): أَنْتِ is built on kasra. هُمُ / أَنْتُمُ before a sākin stay «on sukūn» — the ḍamma
  only breaks two sākins; the first scan counted them and was wrong.
- Left for the hoca: 2:s16 «مَا الْمَخْرَجُ مِنْهَا» — the line of مَا says khabar muqaddam, the line of الْمَخْرَجُ makes
  مِنْهَا its khabar; one of the two readings must be chosen.
- «One key, one word»: a correction that changes the face of مَا now carries the token's lexicon key with it
  (`precheck_apply.py`, `relex_ma`, run after every apply and by `--relex`) — only on lines a correction touched, since
  the matcher cannot tell «نَافِيَةٌ، وَلَيْسَتِ الْحِجَازِيَّةَ» from a Ḥijāzī mā. 9 keys retargeted in al-Uṣūl.
  For the hoca: ʿIzzī 6:s7 and 7:s3 — authored lines say «نَافِيَةٌ» while the key says the relative; which is right?

### 2026-11-18, night — r04–r06 applied

- r04–r06 (al-Uṣūl ch. 14–22, 119 findings): 116 AI-ONAY applied, 1 skipped by the applier because the correction changes
  the LETTERS (19:s5 token 8: «فَرَضَ عَلَى الصَّلَاةَ» → «عَلَيَّ», both translations say «on me/bana»; the iʿrāb line
  of that token must change with it) — a reading of the text, left for the hoca. 2 AI-ŞÜPHELİ: QR-C8C479EB (nawāṣib,
  the five verbs) and QR-2F4E6B70 («بِخِصَالٍ ثَلَاثٍ وَاحِدَةٌ فَإِنَّهُمْ …» — mubtadaʾ with the fāʾ in its khabar
  without a written أَمَّا?).
- Alternatives the verifier chose between, for the hoca: 16:s2 الْقَيِّمُ made khabar because token 34 الدِّينُ is
  badal (the usual reading: الدِّينُ khabar, الْقَيِّمُ naʿt — two lines change); 17:s1 مِثْلَ ḥāl (or مِثْلِ naʿt/badal,
  a vowel change); 18:s16 رَدًّا mafʿūl lahu (or ḥāl); 19:s12 «لَيَقُولُنَّ اللهُ» mubtadaʾ with khabar dropped (or the
  doer of a dropped verb).
- Lines outside the packets the verifier flagged (next packet or the hoca): 19:s2 token 22 «مَجْرُورٌ بِـ«مَنْ»» → «مِنْ»;
  19:s11 token 18 وَعِبَادَتُهُمْ maʿṭūf, not mubtadaʾ; 18:s13 لَيْسَ — its noun is the maṣdar «أَنْ يَتَكَلَّفُوا», not a
  hidden pronoun.
- After applying r04–r06: `precheck_apply.py --relex --write` retargeted 4 mā keys (14:s11, s12, s16 → nafiya; s23 →
  mawsula); `irab_rules.py --write` (D04) dropped the hidden-doer clause from 3 lines whose doer is written after the verb;
  14:s18 «بَعَثَهُ اللهُ» repaired by hand the same way (the hāʾ an object placed before the doer, the Name the doer).
