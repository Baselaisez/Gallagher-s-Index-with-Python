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

### 2026-11-18, night — r24–r26 applied: ALL 26 PACKETS DONE

- r24 (Qaṣaṣ 1) 18, r25 (small) 38 + 2 AI-ŞÜPHELİ, r26 (small) 3 — 57 applied by the tool, 2 by hand (they change letters):
  Qaṣaṣ 1 9:s23 «وَلَا وَتَخَفْ» → «وَلَا تَخَفْ» (the doubled wāw; segment dropped) and 21:s23 «ءَأَنَّكَ» → «ءَإِنَّكَ» (12:90 — the lām
  on لَأَنْتَ follows only the kasra إِنَّ; lex anna→inna, segment, and t3 «خَبَرُ إِنَّ») — the hoca may check the Karachi print.
- Open for the hoca from r25: qisas-2 26:s16 لَيَالٍ (Zajjāj vs Sībawayh/Khalīl on the جَوَارٍ plurals); qisas-2 35:s4 «عَلَى اللهِ رَبِّ
  الْعَالَمِينَ» vs 26:145 «عَلَىٰ رَبِّ الْعَالَمِينَ».
- Totals over r01–r26: about 1,060 corrections applied with a verbatim source each, every one logged by:"ai", confirmed_by_human:false;
  the open questions are in this file; the lines found OUTSIDE the packets are in outside-packet-notes.md — the next pass.

## Outside-packet batch o01 — al-Uṣūl al-munīfa (85 findings, all AI-ONAY, applied, unconfirmed)

Ids are QO-…; the findings are in `findings-outside.json` (tracked) and the verdicts in `verdicts/o01-al-usul-al-munifa.jsonl`.
`precheck_apply.py` now also reads `findings-outside.json`.

**For the hoca**
- 24:s15 t38 أَهَمُّ: only the missing «مُضَافٌ» was added. Mubtadaʾ or khabar is left open.
- The four أُولٰئِكَ lines now say «مَبْنِيٌّ عَلَى الْكَسْرِ» (house wording had «عَلَى الْفَتْحِ»). No repo book states the
  vowel, so please confirm.
- 23:s6 t101 and 30:s4 t87 ذٰلِكَ: the open «يَسْمَعُ ذٰلِكَ الْمَلِكُ» question. Not touched. On 30:s4 t85 only the hidden
  doer was removed.
- 31:s12: the names after t21 mix «مَعْطُوفٌ» with one «مُبْتَدَأٌ» (t37). Both can be defended, so this is consistency only.

**Out of scope (lexicon, POS, tags, letters, translations)**
- Lex keys and POS:
  - 24:s20 t12 إِنَّا (ana→inna); 24:s16 t92 (alima→allama); 24:s21 t121/t127 فَسَّرَهُ (sarra→fassara); 24:s2 t15 وَهْبٍ;
    24:s6:16 and 24:s21:77 (ma-hijaziyya / ma-mawsula).
  - From r07: إِذًا, وَأَوْضَحُ, وَذَا النُّونِ.
  - From r09: لِمَا; يَكُ, keyed ilayka-ism-fil, should be kana; أَكْرَمَكُمْ; عَرَضَ; تُرْجِيَ; 25:s6 t20 أَعْلَمُ.
  - 29:s2 t21 and 30:s3 t36 (→ ma-istifham); 30:s2 t22 لِمَنْ; 27:s7 t3 أَسْلَمَ.
  - رُقَيَّةُ, بَعْدِي, جَارَ, أَجْرُكُمْ, أَنَّا, نُعْمَانَ; 24:s10 t29 تَقُولُ keyed taqawwala.
  - 14:s15 t6 نُصْحِي has pos verb (should be noun). 19:s10 t5 يَجْرِمَنَّكُمْ has pos noun (should be verb).
- Grammar tags: the tags on the 85 corrected tokens still name the old roles, as do the r10 tag list.
- Source-file letters (usul-al-munifa-src.txt): p.48 تَرْجِيَ→تُرْجِيَ; l.367 أَعْتِقْ→أُعْتِقْ; p.58 وَلَنَسْكُتْ→وَلْنَسْكُتْ.
- Translations: the en/tr formula "its doer is a hidden pronoun — one of kāna's sisters" on correct kāna/laysa lines
  (8:s4 t8/t25, 14:s7 t1, 14:s8 t1, 16:s1 t28, 24:s1 t24, 31:s11 t47, 14:s43 t36).

**Same errors on tokens no note names (next batch)**
- 24:s20 t17 and 24:s11 t29 بِكَافِرٍ: laysa's extra bāʾ.
- 25:s19 t24 يُعَذَّبَ: passive called «فاعل».
- 19:s2 t25 كُفْرُهُ: «اسم كان» under لَيْسَ.
- No role: 19:s2 t10 فَهُوَ, 24:s18 t26 هُمُ, 14:s43 t37 هِيَ.
- The r17 note "D04 misses a quoted word as the doer (35:s7, 47:s2)" belongs to Marāḥ, not al-Uṣūl.

## Outside-packet batch o02 — the rest of the shelf (181 findings: 180 AI-ONAY applied, 1 AI-ŞÜPHELİ)

The verdicts are in `verdicts/o02-shelf.jsonl` and the findings in `findings-outside.json`.

Findings per package: ʿIzzī 58, Maqāmāt 42, Iẓhār 17, Marāḥ 15, Kāfiya 14, Qaṣaṣ 4 13, Qaṣaṣ 1 9, Talkhīṣ 3, Juḥā 3, al-Ghurāb 2,
Qaṣaṣ 2 2, ʿAqāʾid 1, Zakariyyā 1, Ayyūb 1.

Surface (vowel-only) corrections:
- Iẓhār 2:s11 t14 مُسْتَقَرًّا and 22:s8 t10 الْمُسْتَقَرِّ («ظرف مستقر أي … مستقر فيه»)
- 3:s6 t14/t24 مَضْرِب (place noun of yaḍribu)
- 66:s3 t3 الْمُتَّصِلُ. This is the surface half of r16's QR-E991F496, which never landed because the applier ignores
  `corrected.surface`.

**For the hoca**
- AI-ŞÜPHELİ QO-C31CBB84, ʿIzzī 6:s7 t16 فَإِنَّ: is the fāʾ taʿlīliyya or ʿāṭifa? No repo book names the causal fāʾ.
- 13 findings fix only the EN/TR of a correct Arabic line, where "doer" stands for kāna's noun (pattern
  `kana-noun-called-doer`; Marāḥ 76:s10, the ten لَيْسَتْ/كَانَتْ tokens, Qaṣaṣ 4 36:s6 t28). o01 listed the same kind as out of
  scope. Keep or revert, so the two batches agree.
- Rewrites that go past the note: Kāfiya 10:s6 t25 يُعْطَفُ now has «عَلَيْهِ» as the nāʾib al-fāʿil (per Iẓhār's «مُرَّ بِزَيْدٍ»).
  Maqāmāt 2:s18 t5 فَأَنْتَ: the fāʾ now opens the answer of إِذَا.
- ʿIzzī 9:s3, s5, s6: the jazm seat was added to the كَانَ condition lines, and قُلِبَتْ is now named as passive.
- Left out because they belong to an open question:
  - Talkhīṣ 70:s10 t6 قَلِيلًا
  - the faṣl/second-mubtadaʾ question: Marāḥ 4:s1 t1 هُوَ and 24:s5 t2/t3; Maqāmāt 2:s15 t9 هُوَ
  - Maqāmāt 12:s2 t12 هُمْ
  - Manār 8:s2 t1 (مُوجَب/مُوجِب)
  - Kāfiya 25:s3 t0
  - ʿIzzī 3:s2 t1 and 6:s1 t1/t2 after أَمَّا

**Out of scope**
- Lexicon keys and POS:
  - Iẓhār: 2:s11 t8 `mutadammin`; the glossary lemmas of `mustaqarr` and `madrab` (→ مَضْرِب); 58:s2 t27 دَعْنِي (وَدَعَ).
  - Kāfiya: 25:s2 t20 ma-nafiya→ma-masdariyya.
  - Manār: split `mujib` / `mujab`.
  - Maqāmāt: 13:s6 t1 أَعْلَمُ; 3:s7 t1 طَلَبَ and 4:s3 t4 لُبْسُ → their maṣdar; 3:s2 t2 بِأَنْ; 5:s3 t13 وَانْهَ.
  - Qaṣaṣ 4: 4:s1 t8 مَعَهُمْ has pos prep.
- Grammar tags:
  - ʿIzzī 14:s32 t11, 14:s26 t15
  - Talkhīṣ 62:s10/s11, 3:s4
  - Iẓhār 42:s6 t13, 64:s1 t8, 25:s5 t0, 54:s6 t2, 44:s6 t13, 3:s16 t2, 6:s4 t15
  - Marāḥ 60:s3 t16/t17, 61:s5, 76:s10, 28:s7, 20:s6, 53:s1 t40
  - Kāfiya: the r18 list
  - Manār 8:s2/s4, 13:s1 t6
  - Maqāmāt 9:s5 t6, 11:s5 t10, 13:s7 t9, 8:s7 t4
  - Juḥā 2:s1 t9; Qaṣaṣ 4 4:s1 t8
- Letters: qisas-1 2:s1 t8/t9 يَفْهَمُ written twice (check the print); talkhis-src l.4197 and l.4719.

**Seen while working, for the next batch**
- ʿIzzī 13:s6 t5 وَاعِدٌ: its wāw is a radical, but the line says «عاطفة».
- ʿIzzī 15:s4 t3/t4 الْمُعْطَى / الْمُشْتَرَى: maqṣūr, but the line says «بالكسرة».
- ʿIzzī 19:s6 t6 يَكُونُ: EN/TR say "doer".
- ʿIzzī 9:s6 t15 أُدْغِمَتْ: the line doesn't say passive.
- ʿIzzī 13:s17 t15 وَهٰذَا: no role.
- ʿIzzī 3:s6 t11/t13 and 3:s8 t4/t6: bare «خَبَرٌ» on مِثْلُ / نَحْوُ.
- Marāḥ 40:s2 t3 يَجِيءُ: no doer.

## Rule M01 — maqṣūr diptote in jarr (32 lines, rule-applied, unconfirmed) + SignEngine fix

o02 corrected six maqṣūr diptotes to «مجرور بفتحة مقدرة … نيابة عن الكسرة». About 30 more lines on the shelf still said
«بكسرة مقدرة» for the same kind of word, so the corpus disagreed with itself and the SignEngine's maqṣūr class fell
below its 97% floor.

**Doctrine** (Shudhūr l.30, «مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ … إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ»): a maqṣūr
diptote free of ال and annexation is majrūr by the fatḥa ESTIMATED on the alif, in place of the kasra.

**Rule M01** (`tools/authoring/irab_rules.py`) rewrote 32 lines on مُوسَى، عِيسَى، يَحْيَى، أَعْلَى، أُنْثَى، أُخْرَى، دُنْيَا، يُمْنَى،
ذِكْرَى، دَعْوَى، بُشْرَى. Lines that say the word itself is «مُضَافٌ» were left alone, because an annexed diptote is
declined fully. Every rewrite is in rule-applied.jsonl.

**SignEngine (precheck reader only):**
- the maqṣūr diptote's jarr is now an estimated fatḥa;
- the alif-of-femininity pattern فُعْلَى / فَعْلَى / فِعْلَى is flagged as a diptote;
- مَفْعَل words (مَعْنًى) are excluded.

The maqṣūr class went from 96.3% to 97.9%. This engine change must travel with the M01 content to main, never before
it: main's corpus still has the kasra lines.

**For the hoca:**
- juha-wa-al-… جُحَا «مجرور بكسرة مقدرة على الألف» was left as it is. Is جحا a diptote at all? It has no clear second cause.
- Marāḥ عَلَامَتَا (s4, s14) is counted as a maqṣūr by the engine, but it is a dual. That is the engine's error and is noted.

## Engine-found corpus slips (v327 engine wave on main: أَنْ, kāna's ism, objects carrying a pronoun)

Token numbers here count from 1. Not yet written as a packet.

- I-1 أَنْ:
  - qisas-al-nabiyyin-4:19:s7:6 «أَنْ لَا تَأْكُلَ». The أَنْ line says tafsīriyya with lā of prohibition, but تَأْكُلَ has a
    fatḥa and its own line says «منصوب بأن», so it is the maṣdariyya.
  - al-usul-al-munifa:14:s30:37 and 14:s34:18 «أَلَّا تَعْبُدُوا», and 19:s10:10 «أَلَّا تَعْدِلُوا». The token أَلَّا carries
    the line of «إِلَّا» («أداة استثناء»).
- I-2: a kāna-family verb whose line says «فاعل» or «والفاعل ضمير مستتر»:
  - al-maqamat-birgivi:3:s7:11 كُونُوا
  - al-usul-al-munifa: 6:s9:30, 13:s4:15, 14:s21:14, 18:s1:18, 21:s5:22, 21:s5:41, 23:s2:66, 23:s7:92, 20:s2:29,
    20:s2:31, 24:s17:27, 25:s12:20, 31:s5:53, 31:s5:57, 31:s7:27
  - luqman-wa-ibnuh:4:s3:9 صَارَ
  - qisas-al-nabiyyin-4:22:s4:10 and 22:s4:17 كَانُوا

### o03-engine327: the engine-found list, verified (12 findings: 10 AI-ONAY applied, 2 AI-ŞÜPHELİ, all unconfirmed)

- **Applied:**
  - row 1, Qaṣaṣ 4 19:s7 أَنْ → maṣdariyya (تَأْكُلَ carries a fatḥa)
  - row 3, al-Uṣūl 14:s34 أَلَّا: the line of the exceptive إِلَّا is replaced
  - rows 6, 8, 16–21: kāna-family verbs, «فاعل» → «اسمها / اسمه», with the EN/TR corrected
- **Gone past the source line:**
  - rows 6 and 8: the lām answering لَوْ was added. 6:s9 is read with ḍamīr al-shaʾn as the ism and the clause «مَنْ شَرِبَهَا
    فَقَدْ شَرِبَ» as the khabar.
  - rows 18 and 19 فَكُونُوا: the fāʾ is now «رابطة لجواب الشرط», not «عاطفة», and the EN/TR plural is fixed.
- **For the hoca:**
  - **ŞÜPHELİ, rows 14 and 15, al-Uṣūl 20:s2 «كَيْفَ أَصْبَحْتَ؟ — أَصْبَحْتُ مُؤْمِنًا حَقًّا».** Is أَصْبَحَ nāqiṣa or tāmma? The
    package disagrees with itself. The line on كَيْفَ says «خبر أصبح مقدم», while the lines on مُؤْمِنًا and the EN/TR read
    tāmma with a ḥāl.
  - **Row 1:** if the Karachi print reads تَأْكُلْ (jussive, matching the «وَلَا تَهْشِمْ» after it), the أَنْ is tafsīriyya and the
    verdict reverses.
  - **al-Uṣūl 31:s7:** the English "except that I did not fight" has a negation that the Arabic «إِلَّا أَنْ أَكُونَ قَاتَلْتُ»
    lacks. Check it against the source.
- **Next batch:**
  - al-Uṣūl 6:s9 t32 فَقَدْ «عاطفة»: it is the fāʾ of the khabar of مَنْ.
  - al-Uṣūl 25:s12 t20 أَنَا and t21 الَّذِي have no role.
  - the three أَلَّا tokens are keyed `illa` (a lexicon issue).

## Engine-found corpus slips (v328 engine wave on main: the implied أَنْ, ẓarf with a pronoun)

Token numbers count from 1. Not yet a packet.

- **حتى named as the nāṣib** (Shudhūr R156: the naṣb is by an implied أَنْ after ḥattā):
  - al-maqamat-birgivi: 2:s37:29, 2:s40:25
  - al-usul-al-munifa: 3:s21:28, 19:s3:16, 21:s7:11, 25:s7:50, 25:s11:28, 25:s12:20, 32:s2:64, 34:s2:40
- **«منصوب بلم» on the verb after lām al-juḥūd** (it is by an implied أَنْ, wujūban): al-usul-al-munifa 3:s14:27, 3:s14:32,
  24:s21:54, 24:s21:112. Also «منصوب بمن» at al-maqamat-birgivi 7:s5:12.
- **«منصوب بلا»:**
  - al-usul-al-munifa 22:s3:21 (after حتى)
  - al-usul-al-munifa 19:s7:37 (the fāʾ of sababiyya after a negation, R159)
- **بين called «مفعول به»** (it is a ẓarf, R104): al-usul-al-munifa 25:s7:53, 25:s11:31, 32:s2:54.

### o04-engine328 (9 AI-ONAY applied, unconfirmed)

- Nine verbs had «منصوب بحتى». They now read «منصوب بأن مضمرة وجوبًا بعد حتى». The source is the Kāfiya Q&A, l.2489 and l.2537.
- The other 11 listed tokens were already correct on this branch.
- The list entry 24:s21:54 لِيُفَرِّقَ follows «وَلَمْ يَبْعَثْ». It is lām al-taʿlīl, not juḥūd, and the line already says so.
- 22:s3:21 reads «بِأَنْ مُضْمَرَةً» with a fatḥa (as a ḥāl). This can be defended, so it was not raised.
- Row 8, al-Uṣūl 25:s12:20, is the same token as o03 row 17. It was given its own id, QO-49A51F6D.

## Engine-found corpus slips (v329 engine wave on main: the feminine plural, the conditional nouns, the built ẓurūf)

Token numbers count from 1. Not yet written as a packet.

- **Singulars called «جمع مؤنث سالم» with the kasra.** The tāʾ wears a fatḥa before the pronoun:
  - al-usul-al-munifa 22:s11:21 وَصَلَاتَهُمْ
  - al-usul-al-munifa 23:s7:34 مَرْضَاتَهُ
  - al-usul-al-munifa 24:s7:36 and 24:s7:59 زَكَاتَهُ
- **يَرَهُ called naṣb by the fatḥa.** It is the answer of مَنْ, majzūm by the dropped alif: al-usul-al-munifa 26:s2:76 and 26:s2:82.
- **مَنْ led as a relative while the jazm of يَتَّقِ shows:** qisas-al-nabiyyin-1 21:s24:11.
- **لِمَا (the jarr lām + a relative مَا) called «ظرف بمعنى حين»:** al-usul-al-munifa 14:s25:8, 14:s28:14, 14:s37:35,
  14:s37:41, 25:s18:27.
- **A line calls the word the ḥīniyya لَمَّا, but the page writes no shadda:** al-usul-al-munifa 8:s5:16 «لَمَا قَدَرَ». Either the page or the
  line is wrong.
- **For the hoca, بَنَات:** the engine treats it as a SOUND feminine plural, taking the kasra in naṣb (R12; «بَنِينَ وَبَنَاتٍ»).
  The triage had called it broken.

### o05-engine329 (3 AI-ONAY applied, unconfirmed)

- **Applied:** al-Uṣūl 14:s28 t13 and 14:s37 t34/t40 «لِمَا» now read as the jarr lām + relative مَا, not the ḥīniyya لَمَّا
  (src l.183/193 has a kasra and no shadda).
- **Already correct on this branch:** the other 10 items. 8:s5 «لَمَا قَدَرَ» is the lām answering لَوْ with nāfiya مَا (src l.115).
- **Next batch:**
  - 14:s28 t11 فَكُلٌّ «عاطفة، فاعل»: should be the fāʾ of taʿlīl, and mubtadaʾ
  - 14:s28 t12 مُيَسَّرٌ «نعت»: should be the khabar
  - 14:s28 t14 خُلِقَ «الفاعل ضمير مستتر»: should be nāʾib al-fāʿil
- **Lex keys:** the five «لِمَا» tokens are keyed `lamma` (→ ma-mawsula), and 8:s5 t15 «لَمَا» is keyed `lamma` (→ ma-nafiya).

## Engine-found corpus slips (v330 engine wave on main: the verbs of approach, istithnāʾ, ism fiʿl, the compound numbers)

Token numbers count from 1. Not yet a packet.

- **«فاعل» on the noun after عسى / تكاد.** It is the ism of a nāsikh:
  - al-usul-al-munifa 23:s5:4 اللهُ
  - al-usul-al-munifa 25:s7:70 اللهُ
  - al-usul-al-munifa 25:s17:68 السَّمَاوَاتُ
- **qisas-al-nabiyyin-4 45:s4:18 النَّصْرَانِيَّةُ «فاعل».** The next line calls تَأْخُذُ «خبر بدأت من أفعال الشروع», so the two lines contradict
  each other.
- **al-usul-al-munifa 2:s25:32 السَّوَادَ «مفعول به».** In «كلهم في النار إلا السواد», a complete affirmative clause, it is the
  manṣūb mustathnā.
- **al-usul-al-munifa 2:s22:1 «عَلَيْكَ بِالْأَثَرِ» is read as a jarr phrase.** It is the ism fiʿl «الزم» with an extra bāʾ, which is how
  wasiyyat-abi-hanifa-samti 4:s26:1 reads the same phrase.
- **For the hoca:**
  - In Uṣūl 2:s16:2, 23:s4:62, 24:s20:19 and 30:s4:42, عسى + أن is given «والفاعل ضمير مستتر». That pronoun is the ism if عسى is
    deficient. If it is complete, the maṣdar from أن + muḍāriʿ is the fāʿil.
  - marah-al-arwah 13:s13:9 has اثْنَا as the khabar of صار. اثْنَيْ is due, and the author's own line says so. This is the edition's
    spelling.

### o06-engine330 (4 AI-ONAY applied, unconfirmed)

**Applied**
- al-Uṣūl 23:s5 t3 and 25:s7 t69 اللهُ now read «اسم عسى». The noun precedes أن, so عسى is nāqiṣ (Iẓhār l.34).
- al-Uṣūl 2:s22 t0–1 «عَلَيْكَ بِالْأَثَرِ» now reads as the ism fiʿl «الزم» with an extra bāʾ (Iẓhār l.49), the same as the wasiyya package.
  - For the hoca: some read this bāʾ as one of transitivity.

**Already correct on this branch:** the other three items. qisas-4 45:s4 was settled by r23.

**For the next batch**
- The verb lines of عَسَى (23:s5 t2, 25:s7 t68), تَكَادُ (25:s17 t66) and بَدَأَتِ (qisas-4 45:s4 t16) do not say the verb is nāqiṣ.
- Lexicon key and tags of عَلَيْكَ: should be `alayka`, ism-fil.
