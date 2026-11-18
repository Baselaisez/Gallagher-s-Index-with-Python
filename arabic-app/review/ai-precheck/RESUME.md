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

### 2026-11-18, night — r07–r09 applied

- r07–r09 (al-Uṣūl ch. 22–26, 118 findings): 114 AI-ONAY applied, 4 AI-ŞÜPHELİ for the hoca (23:s6 «لتنازله وجوم» letters and
  vowels ×3; 24:s11 the Turkish of «لَنْ نَقْدِرَ عَلَيْهِ»). The verifiers' alternatives and the lines they flagged OUTSIDE their
  packets are in outside-packet-notes.md, for a packet of their own.
- relex learned «حَرْفُ نَفْيٍ» as the face of the negation (3 keys retargeted); D04 now repairs a line whose EN/TR never named the
  hidden doer (2 lines); 24:s10 «أَنْ تَضِلَّ إِحْدَاهُمَا فَتُذَكِّرَ إِحْدَاهُمَا الْأُخْرَى» (2:282) repaired by hand — the second إِحْدَاهُمَا
  is the doer, الْأُخْرَى the object, no hidden «أَنْتَ».
- The «مَا» measure's ceiling moved 45 → 46 because two LINES moved: 22:s6 «… إِذَا قَاتَلَ مَا أَقْدَمَ» (the answer of لَوْلَا) and
  22:s3 «وَمَا يَرْكَبُ الْمَعْصِيَةَ وَهُوَ يَعْلَمُ» are negations the seat rule reads as objects — named engine misses.

### 2026-11-18, late — r10–r12 applied

- r10–r11 (al-Uṣūl ch. 26–35): 79 AI-ONAY; r12 (Talkhīṣ): 25 AI-ONAY — 104 corrections applied; relex retargeted 2 mā keys;
  D04 one line. 4 AI-ŞÜPHELİ for the hoca (r11 32:s6 «وَإِلَّا قَاتَلْتَهُ»; r12 63:s15 «وَلَا مَالَ/مَالُ» ×2; r12 70:s10 مُعَرَّجُ).
- Talkhīṣ 74:s3 «فَلَلرَّيْثُ فِي بَعْضِ الْمَوَاضِعِ أَنْفَعُ» (the package's source, l.4677): once the surface became the lām of
  inception, its line was rewritten by hand to match (lām al-ibtidāʾ + mubtadaʾ, segment keyed `lam-ibtida`, أَنْفَعُ its khabar);
  the smart layer of the two surface corrections (فَلَلرَّيْثُ، هَوَاكِ) follows the full.

### 2026-11-18, late — r13–r15 applied

- r13–r14 (Taṣrīf al-ʿIzzī): 50 AI-ONAY, 6 AI-RET (17:s32 already repaired by rule S01); r15 (Iẓhār): 19 AI-ONAY, 2 AI-ŞÜPHELİ
  (14:s5 «وَالْمُضَافُ غَيْرَ/غَيْرُ غَيْرٍ»). 69 corrections; relex one mā key.
- Iẓhār 12:s3 QR-D253FE03 holds only with its surface: the verifier read «لَمْ يَضُرَّ عَمَلَهُمَا السَّابِقَ» (the object in naṣb,
  the description the hidden doer — both commentaries, Ottoman l.673 and the Turkish), so the surface was changed with the line:
  عَمَلُهُمَا → عَمَلَهُمَا, السَّابِقُ → السَّابِقَ (its line now naʿt in naṣb). The passive reading يُضَرَّ عَمَلُهُمَا fits the old
  EN/TR — for the hoca to confirm.
- ʿIzzī 3:s11 t9 نَحْوُ: once r13 made مِثْلُ the khabar of an omitted «ذٰلِكَ», the bare «خَبَرٌ مَرْفُوعٌ» of نَحْوُ left it no
  mubtadaʾ (the Hadhf audit's new false alarm) — rewritten as the second khabar of that omitted «ذٰلِكَ». 3:s6 t11/t13 and 3:s8
  t4/t6 carry the same bare «خَبَرٌ» on مِثْلُ / نَحْوُ: for the outside-packet packet.

### 2026-11-18, night — r16–r18 applied

- r16 (Iẓhār ch. 22–66) 21, r17 (Marāḥ) 13, r18 (Kāfiya) 16 — 50 AI-ONAY applied, none skipped; relex one key.
- `precheck_apply.py` now lands a surface correction whole: the smart layer follows the full, every segment takes the new vowels
  (its letters found in order in the word), and an iʿrāb carried in the same verdict (`corrected.irab`) lands with it.
- Hand-carried with them: Iẓhār 50:s1 sentence translation («you struck, you» / «dövdün, sen»); Marāḥ 59:s6 EN/TR quote اِرْمُنَّ.
- **For the hoca — an emendation against the print:** Marāḥ 59:s6 اِرْمِنَّ → اِرْمُنَّ (the sentence is about the plural's wāw
  dropped after a ḍamma; the book's own nāqiṣ paradigm separates the two, matn l.463, but the print reads اِرْمِنَّ at l.346 and the
  source at l.654). If accepted, the manifest attribution must record it; if not, revert the token and its two translations.
- The Iẓhār catechism (izhar-mamul q58) quoted «يَا تَيْمُ تَيْمَ عَدِيٍّ» while its own TR/EN answer wrote «يَا تَيْمَ» — once r16 set the
  chapter to تَيْمَ (QR-25CB89C1 + QR-8E47605A, for the hoca), the verified string follows the chapter and its own answer.

### 2026-11-18, night — r19–r21 applied

- r19 (Manār) 8, r20 (Maqāmāt) 30, r21 (Maqāmāt) 31 — 69 AI-ONAY applied; relex one key. Two surfaces: Manār 8:s2/s4 وَمُوجَبُهُ
  (ism mafʿūl — for the hoca against a printed Manār; the repo holds none) and Maqāmāt سَلْطَنَتِي (فَعْلَلَة).

### 2026-11-18, night — r22–r23 applied; rule K01 applied

- r22–r23 (Qaṣaṣ 4): 48 AI-ONAY applied; QR-681D784B (5:76 TR «gücü yeten» → «gücü yetmeyen», the dropped negation reversed
  the verse) applied by hand; 1 AI-ŞÜPHELİ (21:87 «لَنْ نَقْدِرَ عَلَيْهِ», shared with al-Uṣūl QR-4B58419B).
- K01 KanaIsmTwiceRule: 19 lines (al-Uṣūl 10, Marāḥ 9) named kāna's noun twice; the written noun (or a detached pronoun right
  after the verb) keeps «الْمَرْفُوعُ بَعْدَهَا», otherwise the hidden pronoun stands. Logged by:"ai", confirmed_by_human:false.
