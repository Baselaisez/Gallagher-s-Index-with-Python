# The stories' grammar audit, triaged — 2026-11-27 (v342-T)

Every contradiction `tools/grammar_audit.js` emits today (uncapped: `research/story-grammar-audit-2026-11-27.json`, 1869 records) judged by the books in `research/sources/`, cluster by cluster. **L** = the authored line (or sign, or tag) is wrong → a proposal in `research/story-corrections-proposed-2026-11-27.jsonl` (nothing applied); **E** = the engine is wrong → a work order in `research/engine-faults-2026-11-27.md`; **C** = both right; **undecided** = no book line decides. Per-record verdicts: `research/story-audit-triage-2026-11-27.json`. *listed* = an earlier wave already put the item (or its cluster) before the hoca (CLAUDE.md); those are not new. Everything here awaits scholarly review.

## Totals

| engine | contradictions | L | E | C | undecided | new | listed before |
|---|---:|---:|---:|---:|---:|---:|---:|
| Sign of the case — SignEngine | 141 | 49 | 89 | 0 | 3 | 131 | 10 |
| Case ending and role — DabtEngine | 663 | 9 | 649 | 3 | 2 | 656 | 7 |
| Taʿalluq — TaalluqEngine | 307 | 0 | 272 | 35 | 0 | 307 | 0 |
| The manṣūb offices — MansubEngine (v332) | 18 | 16 | 1 | 1 | 0 | 2 | 16 |
| The Shudhūr rules — Sh336Engine (v336-Sh) | 20 | 2 | 1 | 17 | 0 | 18 | 2 |
| إِنَّ / أَنَّ — InnaEngine | 27 | 2 | 25 | 0 | 0 | 27 | 0 |
| Order — TartibEngine | 2 | 0 | 2 | 0 | 0 | 2 | 0 |
| The muʿrib's etiquette — AdabEngine | 570 | 568 | 1 | 1 | 0 | 2 | 568 |
| Clause maḥall — JumlaMahallEngine | 121 | 4 | 72 | 45 | 0 | 103 | 18 |
| **all** | **1869** | **650** | **1112** | **102** | **5** | **1248** | **621** |

Proposals: 650 lines (64 certain, 586 likely); 77 carry a mechanical `after_ar`, 573 describe the fault. The adab findings (568 L) are incomplete lines, not wrong analyses, and were already listed in the lab (wave 40) — without them the L count is 82.

**Method.** Clustered by script (engine, rule, the shape of the disagreement: the written ending against the engine's, the authored office, keywords of the line — مَحْكِيٌّ، لِلرَّوِيِّ، مَمْنُوعٌ، مُقَدَّرَةٌ…); one member of each cluster read with its sentence, the rest checked by shape (random samples of 7 per large case cluster read as well); outliers judged alone. A case-ending contradiction where the written vowel and the authored line agree and the engine differs is E unless the reading showed the line itself wrong. Scripts: scratchpad `triage342/` (`j/*.py` the judgements, `build.py`, `render.py`, `probe2.js`).

**Not certain by item.** The case clusters (649 E) were judged by shape: of 663 items, every item where the line and the written vowel disagree (~100), the first two of each of ~120 sub-shapes, and 7 random members of five large clusters were read; a later reader may still find a line wrong inside an E cluster (the written vowel and the line agreeing is not proof). All 307 taʿalluq items were read in a one-line form (the word with three words either side, the authored governor, the engine's).

## Clusters, largest first

### T-A01 — The muʿrib's etiquette — AdabEngine · L — the line is wrong (likely) · 409

- **Shape**: a verb line that stops before its doer (no «فَاعِلٌ / مُسْتَتِرٌ / التَّاءُ …» on it or on the next tokens before the next verb)
- **Judgement**: Bāb 4: the doer is named on every verb line — written, attached, or concealed with its estimate. Not a wrong analysis: an incomplete one. The proposal is to add «وَالْفَاعِلُ …» (the person is the author's to state).
- **Book**: `qawaid-al-irab-turkish.txt` l.76 «(bāb 4) «Ayıplananlar: failden bahsetmeden fiili, haberi araştırmadan mübtedayı zikretmek; sıla ve âid zamiri söylemeden ismi mevsûl demek» — the AdabEngine's Arabic: «لَا يُذْكَرُ الْفِعْلُ دُونَ فَاعِلِهِ»، «لَا يُذْكَرُ الْمُبْتَدَأُ دُونَ خَبَرِهِ»، «لَا يُقَالُ «اسْمٌ مَوْصُولٌ» دُونَ ذِكْرِ الصِّلَةِ وَالْعَائِدِ»»
- **listed-before**: CLAUDE.md wave 40 (v202): the AdabEngine findings «listed in the lab for scholarly review»
- **Examples**: al-kafiya:7:s14:13 تَكُنْ; al-kafiya:7:s14:14 أَكُنْ; al-kafiya:7:s15:9 تَخْرُجْ

### T-T02 — Taʿalluq — TaalluqEngine · E — the engine is wrong · 163

- **Shape**: author: an explicit governor (verb, maṣdar, participle, elative, or the sense of a word — «لَفْظُ اللهِ لِمَا فِيهِ مِنْ مَعْنَى الْمَعْبُودِ», «مَا فِي كَأَنَّ مِنْ مَعْنَى التَّشْبِيهِ») / engine: another written word (the nearest noun, تَعَالَى, the verb of a neighbouring clause, a fronted object)
- **Judgement**: The phrase is laghw and belongs to the word whose meaning it completes (I.16); a fronted phrase keeps its governor after it (I.15 «بزيد مررت»); a word with the sense of a verb governs it (I.52, the matn's own «وهو الله في السموات»). «لَا يُحِبُّ اللهُ الْجَهْرَ بِالسُّوءِ» — بِالسُّوءِ completes الْجَهْرَ, not يُحِبُّ.
- **Book**: `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»; `izhar-al-asrar-matn-lithograph.txt` l.15 «ويجوز تقديم ما عدا هذا على متعلقه نحو بزيد مررت.»; `izhar-al-asrar-matn-lithograph.txt` l.52 «ومنه كل اسم فهم منه معنى الصفة نحو لفظة الله في قوله تعالى وهو الله في السموات أي المعبود فيها. ومنه اسم الإشارة وليت ولعل وحرف النداء والتشبيه والتنبيه والنفي وغيرها فإنها تعمل»
- **Examples**: al-kafiya:1:s12:8 إِلَى; al-kafiya:15:s8:11 بِالسُّوءِ; aqaid-ahl-al-sunna:2:s6:6 بِصِحَّةِ

### T-C-tanwin — Case ending and role — DabtEngine · E — the engine is wrong · 106

- **Shape**: same case, wrong tanwīn: the engine adds tanwīn to an annexed noun (شَهَادَةُ أَنْ …، عَذَابُ الْحَرِيقِ، نُورُ الدِّينِ), to a name before «ابْن» (زَيْدِ بْنِ، قَيْسُ بْنُ), or drops it from a fully declined plural (أَسْمَاءٌ)
- **Judgement**: «وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ» (S.274); a name described by ابن between two names loses its tanwīn; أَسْمَاءٌ (plural of اسْم) is not a diptote (S.30 is for what does not decline).
- **Book**: `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ»
- **Examples**: adam-wa-iblis:1:s2:5 كُلِّهَا; al-ghazali-wa-al-uzla:3:s2:1 فَبَيْنَمَا; al-kafiya:19:s12:14 فَاعِلُ

### T-C-mood — Case ending and role — DabtEngine · E — the engine is wrong · 87

- **Shape**: engine: the wrong mood on a muḍāriʿ — naṣb after a coordinated / fresh verb, rafʿ after لَنْ / أَنْ, rafʿ on a jussive answer of a condition or a request, naṣb after لَامُ الْأَمْرِ
- **Judgement**: «الْمُضَارِعُ إِذَا تَجَرَّدَ مِنْ نَاصِبٍ وَجَازِمٍ» is rafʿ (S.185); after لَنْ / أَنْ naṣb (S.256); after لَمْ, لَامُ الْأَمْرِ, the condition's tools jazm (S.284). The written vowel and the authored line already say it.
- **Book**: `shudhur-al-dhahab-src.txt` l.185 «العَاشِرُ المُضَارِعُ إِذَا تَجَرَّدَ مِنْ نَاصِبٍ وَجَازِمٍ.»; `shudhur-al-dhahab-src.txt` l.256 «وَالمضَارِعُ بَعْدَ نَاصِبٍ، وَهُوَ «لَنْ» أَوْ «كَي» المَصْدَرِيَّةُ مُطْلَقًا، و«إِذَنْ» إِنْ صُدِّرَتْ …»; `shudhur-al-dhahab-src.txt` l.284 «بَابٌ– الْمَجْزُومَاتُ الأَفْعَالُ الْمُضَارِعَةُ الدَّاخِلُ عَلَيْهَا جَازِمٌ، وَهُوَ ضَرْبَانِ: جازِمٌ لِفِعْلٍ، وَهُوَ: لَمْ، وَلَمَّا، وَلَامُ الأَمْرِ، وَلَا في النَّهْيِ»
- **Examples**: al-kafiya:16:s6:9 يَأْخُذْ; al-maqamat-birgivi:2:s42:10 نَزِدْ; al-maqamat-birgivi:4:s5:24 تَجِدَ

### T-T01 — Taʿalluq — TaalluqEngine · E — the engine is wrong · 77

- **Shape**: author: «مُتَعَلِّقٌ بِمَحْذُوفٍ» (khabar / naʿt / ḥāl / khabar kāna — a ẓarf mustaqarr) / engine: a written word nearby (the head noun, the subject, or a verb of the next clause)
- **Judgement**: Where the governor is the deleted general verb (كَائِنٌ / حَصَلَ) the phrase is mustaqarr and stands as khabar, ṣifa or ḥāl (I.15–16): «وَكَانَ إِبْلِيسُ مَعَهُمْ» (khabar kāna), «لَا شَكَّ فِيهَا» (khabar lā), «رَجُلٌ مِنَ الْحُجَّاجِ» (naʿt). The engine binds the phrase to the noun it describes or to a neighbouring verb.
- **Book**: `izhar-al-asrar-matn-lithograph.txt` l.15 «ومجرور ما عدا هذه السبعة منصوب المحل على أنه مفعول فيه لمتعلقه … وقد يحذف المتعلق، فإن كان المحذوف فعلا عاما متضمنا في الجار والمجرور يسميان ظرفا مستقرا نحو زيد في الدار أي»; `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»
- **Examples**: adam-wa-iblis:1:s4:3 مَعَهُمْ; al-asad-wa-al-arnab:3:s2:9 فِيهَا; al-bukhari-fi-baghdad:4:s1:12 فِيهَا

### T-A02 — The muʿrib's etiquette — AdabEngine · L — the line is wrong (likely) · 76

- **Shape**: a mubtadaʾ line whose khabar is never pointed at within ten lines (often a clause khabar: «أَمَّا وَاحِدَةٌ فَإِنَّهُ يَرْجُو …»، «رَجُلٌ غُفِرَ لَهُ»)
- **Judgement**: Bāb 4: the khabar is sought and named for every mubtadaʾ.
- **Book**: `qawaid-al-irab-turkish.txt` l.76 «(bāb 4) «Ayıplananlar: failden bahsetmeden fiili, haberi araştırmadan mübtedayı zikretmek; sıla ve âid zamiri söylemeden ismi mevsûl demek» — the AdabEngine's Arabic: «لَا يُذْكَرُ الْفِعْلُ دُونَ فَاعِلِهِ»، «لَا يُذْكَرُ الْمُبْتَدَأُ دُونَ خَبَرِهِ»، «لَا يُقَالُ «اسْمٌ مَوْصُولٌ» دُونَ ذِكْرِ الصِّلَةِ وَالْعَائِدِ»»
- **listed-before**: CLAUDE.md wave 40 (v202): the AdabEngine findings «listed in the lab for scholarly review»
- **Examples**: al-kafiya:1:s14:16 وَالْمَزْجِيُّ; al-kafiya:45:s5:1 وَالنُّونُ; al-maqamat-birgivi:9:s6:19 سَبَبُ

### T-J03 — Clause maḥall — JumlaMahallEngine · E — the engine is wrong · 72

- **Shape**: OFFERED: the engine offers naʿt-or-ḥāl / naʿt-or-khabar / ḥāl-or-istiʾnāf, and neither reading is the seat an open frame gives the clause — the author names that frame: khabar of kāna / inna / a mubtadaʾ, the answer of إِذَا / لَمَّا / a condition, the ṣila of مَنْ / مَا / الَّذِي, the maqūl after قَالَ, the request's answer (قِفِي نَسْأَلْكِ), ʿaṭf on the previous clause
- **Judgement**: m.49 (the khabar in the bābs of the mubtadaʾ, inna, kāna), m.53 (the maqūl), m.59/67 (the answers), m.124 (the ṣila): the frame decides the seat; a describable noun next to the clause does not.
- **Book**: `qawaid-al-irab-ibn-hisham-matn.txt` l.49 «إحداها واقعةٌ خبرًا، وموضعها رفعٌ في بابي المبتدأ، وإن نحو: زيدٌ قام أبوه، وإن زيدًا أبوه قائمٌ، ونصبٌ، وموضعها نصبٌ في بابي كان وكاد، نحو: إنهم كانوا يظلمون، وما كادوا يفعلون.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.53 «والمفعوليةُ تقع في أربعة مواضع، محكيةً بالقول نحو: قال: إني عبد الله …»; `qawaid-al-irab-ibn-hisham-matn.txt` l.59 «وكلُ جملةٍ وقعت بعد إذ، أو إذا، أو حيثُ، أو لما الوجودية، عند من قال باسميتها، أو بينما، أو بين؛ فهي في موضع ظرفٍ بإضافتهن إليها.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.67 «فأما نحو: إن قام أخوك قامَ عمرٌو.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.124 «الثانيةً الواقعةَ صلةً لاسمٍ، نحو: جاء الَّذي قام أبوه …»
- **Examples**: abu-hanifa-wa-al-safina:1:s1:9 نَحْكِيهِ; abu-hanifa-wa-al-safina:4:s5:8 كَانَ; al-kafiya:1:s13:13 كَقَامَ

### T-A03 — The muʿrib's etiquette — AdabEngine · L — the line is wrong (likely) · 67

- **Shape**: «اسْمٌ مَوْصُولٌ» with no ṣila named within eight lines
- **Judgement**: Bāb 4: a relative is never named without its ṣila and the returning pronoun.
- **Book**: `qawaid-al-irab-turkish.txt` l.76 «(bāb 4) «Ayıplananlar: failden bahsetmeden fiili, haberi araştırmadan mübtedayı zikretmek; sıla ve âid zamiri söylemeden ismi mevsûl demek» — the AdabEngine's Arabic: «لَا يُذْكَرُ الْفِعْلُ دُونَ فَاعِلِهِ»، «لَا يُذْكَرُ الْمُبْتَدَأُ دُونَ خَبَرِهِ»، «لَا يُقَالُ «اسْمٌ مَوْصُولٌ» دُونَ ذِكْرِ الصِّلَةِ وَالْعَائِدِ»»
- **listed-before**: CLAUDE.md wave 40 (v202): the AdabEngine findings «listed in the lab for scholarly review»
- **Examples**: al-kafiya:4:s6:15 مَا; al-kafiya:11:s4:2 مَا; al-kafiya:13:s5:14 مَا

### T-C-built — Case ending and role — DabtEngine · E — the engine is wrong · 65

- **Shape**: engine: rewrites a BUILT word's ending — the person of a māḍī (نَزَلْتِ → نَزَلْتُ، عُنِيتُ → عُنِيَتْ), an amr's pronoun vowel (فَأَلْقِهْ), the mīm of a plural pronoun (مِنْكُمُ)
- **Judgement**: A built word keeps its one ending whatever the governor (S.71: the māḍī's endings; S.22: iʿrāb is only on the declinable); the author names the person the text addresses.
- **Book**: `shudhur-al-dhahab-src.txt` l.71 «أو الفَتْحِ، وَهُوَ سَبْعَةٌ: الماضي المجرَّدُ كضَرَبَ وضرَبكَ وضَرَبَا،»; `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»
- **Examples**: al-ghazali-wa-al-uzla:1:s4:5 يَطْمَئِنُّ; al-maqamat-birgivi:6:s16:13 أَقْبَلْ; al-maqamat-birgivi:8:s2:6 وَتَرْكُ

### T-C-maful — Case ending and role — DabtEngine · E — the engine is wrong · 62

- **Shape**: engine: «مَفْعُولٌ بِهِ» (naṣb) on a word the text writes and the author parses in another case — a muḍāf ilayh (عَبْدِ اللهِ، الْأَصْنَافِ), a doer (السُّنَّةُ، رَجُلٌ), a jarr follower
- **Judgement**: The written ending and the authored line agree; the word is not «مَا وَقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ» here (S.188): it is the second term of an iḍāfa (S.274) or the doer (S.131).
- **Book**: `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»; `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.131 «بَابٌ– الْمَرْفُوعَاتُ عَشَرَةٌ: أحَدُهَا الْفَاعِلُ، وَهُوَ: مَا قُدِّمَ الْفِعْلُ أوْ شِبْهُهُ عَلَيْهِ وَأُسْنِدَ إلَيْهِ»
- **Examples**: al-bukhari-fi-baghdad:2:s2:5 رَجُلٌ; al-maqamat-birgivi:2:s2:16 خَيْرِهِ; al-maqamat-birgivi:8:s3:22 أَمْرِهِ

### T-C-follower — Case ending and role — DabtEngine · E — the engine is wrong · 57

- **Shape**: engine: naʿt / ʿaṭf / badal / tawkīd copying the case of a head it chose, against the written case the author explains (an object, a muḍāf ilayh, a fresh mubtadaʾ)
- **Judgement**: The follower takes its head's case only when it follows that head; here the author (and the vowel) make the word a governed word of its own (S.188, S.274).
- **Book**: `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»
- **Examples**: abu-hanifa-wa-al-safina:1:s2:5 أَهْلِ; al-bukhari-fi-baghdad:1:s2:4 أَهْلِ; al-kafiya:10:s7:18 مُفْرَدٌ

### T-C-verse — Case ending and role — DabtEngine · E — the engine is wrong · 56

- **Shape**: engine: overrides a verse licence the author names in the line (the rhyme's kasra on a jussive, a sukūn for the metre, alif al-iṭlāq, a ḍamma kept for the metre)
- **Judgement**: The poem's commentator quoted in the line outranks the engine: the base sign (S.25) is moved by the rhyme or the metre, and the author says so («وَحُرِّكَ بِالْكَسْرِ لِلرَّوِيِّ»، «سُكِّنَتْ ضَرُورَةً»).
- **Book**: `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Examples**: bad-al-amali:3:s13:9 الْأَهَالِ; bad-al-amali:8:s37:9 تُبَالِ; bad-al-amali:10:s50:10 قَالِ

### T-S02 — Sign of the case — SignEngine · E — the engine is wrong · 43

- **Shape**: author: alif / wāw / yāʾ on a dual, its ilḥāq (اثْنَا), a sound masculine plural or a five-noun / engine: the vowel (class «sahih; sound» or «maqṣūr annexed»)
- **Judgement**: The author names the letter-sign correctly: dual (يَدَيْهِ، وَالِدَيْكَ، يَدَايَ، عَلَامَتَا، نُونَا، الشُّعْبَتَانِ، بِعُنَيْزَتَيْنِ، حَرْفَيْهِ), its ilḥāq اثْنَا (l.41), place names in the dual form (الْبَحْرَيْنِ، الْحَيَارَيْنِ، الدَّحْرُضَيْنِ), sound plurals incl. cited ones (الزَّيْدُونَ، الْمُضَرَّبُونَ، يَمَانُونْ، مُسْلِمِيَّ), five nouns (أَبِي وَقَّاصٍ، فِيهَا = فُو). The classifier missed the class.
- **Book**: `shudhur-al-dhahab-src.txt` l.39 «الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَفْتُوحِ مَا قَبْلَهَا الْمَكْسُورِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.41 «وَأُلْحِقَ بِهِ اثْنَانِ، وَاثْنَتَانِ، وَثِنْتَانِ مُطْلَقًا، وَكِلَا وَكِلْتَا مُضَافَيْنِ إِلَى مُضْمَرٍ.»; `shudhur-al-dhahab-src.txt` l.43 «الْخَامِسُ: جَمْعُ الْمُذَكَّرِ السَّالِمُ، كَالزَّيْدُونَ وَالْمُسْلِمُونَ، فَإِنَّهُ يُرْفَعُ بِالْوَاوِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَكْسُورِ مَا قَبْلَهَا الْمَفْتُوحِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.34 «الثَّالِثُ: «ذُو» بِمَعْنَى صَاحِبٍ، وَمَا أُضِيفَ لِغَيْرِ الْيَاءِ مِنْ «أَبٍ» «وَأَخٍ» «وَحَمٍ» «وَهَنٍ» «وَفَمٍ» بِغَيْرِ مِيمٍ، فَإِنَّهَا تُعْرَبُ بِالْوَاوِ وَالْأَلِفِ وَالْيَاءِ.»
- **Examples**: al-kafiya:16:s10:8 وَالزَّيْدُونَ; al-kafiya:18:s5:19 حَسَنَا; al-kafiya:18:s5:23 وَالزَّيْدُونَ

### T-C-letters — Case ending and role — DabtEngine · E — the engine is wrong · 37

- **Shape**: engine: a vowel (or tanwīn) on a dual, a sound plural, a five-noun or a five-verb whose sign the author names as a letter (ضَالَّتَانٌ، حَيَّيْنَ، بَنُونٌ، يَغُرُّوكُمْ)
- **Judgement**: S.39 (the dual by the alif / yāʾ), S.48 (the five verbs by the nūn).
- **Book**: `shudhur-al-dhahab-src.txt` l.39 «الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ …»; `shudhur-al-dhahab-src.txt` l.48 «السَّادِسُ: يَفْعَلَانِ وَتَفْعَلَانِ وَيَفْعَلُونَ وَتَفْعَلُونَ وَتَفْعَلِينَ، فَإِنَّهَا تُرْفَعُ بِثُبُوتِ النُّونِ، وَتُنْصَبُ وَتُجْزَمُ بِحَذْفِهَا.»
- **Examples**: al-usul-al-munifa:2:s25:18 بَنُو; al-usul-al-munifa:14:s13:30 يَزَالُونَ; al-usul-al-munifa:24:s15:54 ضَالَّتَانِ

### T-C-raf — Case ending and role — DabtEngine · E — the engine is wrong · 36

- **Shape**: engine: rafʿ (fāʿil / mubtadaʾ / khabar / nāʾib / ism kāna) on a word the text writes and the author parses as manṣūb or majrūr (an object, a ḥāl, a muḍāf ilayh: صَلَاحِ الدِّينِ، نُورِ الدِّينِ)
- **Judgement**: The author's office is the one the vowel shows: the second word of a compound name (صَلَاحُ الدِّينِ) is a muḍāf ilayh (S.274), not the doer.
- **Book**: `shudhur-al-dhahab-src.txt` l.131 «بَابٌ– الْمَرْفُوعَاتُ عَشَرَةٌ: أحَدُهَا الْفَاعِلُ، وَهُوَ: مَا قُدِّمَ الْفِعْلُ أوْ شِبْهُهُ عَلَيْهِ وَأُسْنِدَ إلَيْهِ»; `shudhur-al-dhahab-src.txt` l.147 «الثَّالِثُ الْمُبْتَدَأُ، وَهُوَ: الْمُجَرَّدُ عَنِ الْعَوَامِلِ اللَّفْظِيَّةِ: مُخْبَرًا عَنْهُ، أَوْ وَصْفًا رَافِعًا لِمُكْتَفًى بِهِ»; `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»
- **Examples**: al-kafiya:39:s1:15 زَائِدَةً; al-usul-al-munifa:12:s3:4 ثَوْبَانُ; al-usul-al-munifa:12:s3:29 الرِّزْقَ

### T-C-jarr — Case ending and role — DabtEngine · E — the engine is wrong · 35

- **Shape**: engine: jarr (muḍāf ilayh / after a jarr letter) on a word the text writes and the author parses as manṣūb or marfūʿ, or naṣb on a written majrūr after a preposition
- **Judgement**: The author's office is the one the vowel shows (S.25); the engine annexes a word to a neighbour that is not its muḍāf (S.274 needs a muḍāf stripped of tanwīn).
- **Book**: `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Examples**: al-kafiya:16:s11:12 الصَّلَاةَ; al-usul-al-munifa:2:s26:3 مَيْمُونِ; al-usul-al-munifa:14:s18:17 الْقَدَرِيَّةَ

### T-C-muqaddar — Case ending and role — DabtEngine · E — the engine is wrong · 33

- **Shape**: engine: a shown vowel on a word whose case is estimated (الْيَمَانِي، الْمَاضِي، السَّاعِي، صَالِ، تَوَالِي، عَمِّي)
- **Judgement**: S.54: the ḍamma and kasra are estimated on the manqūṣ, every vowel on the maqṣūr and before the speaker's yāʾ.
- **Book**: `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا»
- **Examples**: al-maqamat-birgivi:4:s2:10 سُنَّتِي; al-maqamat-birgivi:8:s7:5 فَخْرِي; al-maqamat-birgivi:11:s2:10 بِأَذَى

### T-T03 — Taʿalluq — TaalluqEngine · E — the engine is wrong · 32

- **Shape**: author: an explicit verb / participle the phrase is fronted before or follows (يَغْفِرُ … لِمَنْ يَشَاءُ، بِهَا تَسْتَعِدُّ، بَعْدَ السَّفَاهَةِ يَحْلُمُ، كَانُوا لَنَا خَاشِعِينَ) / engine: «مُتَعَلِّقٌ بِمَحْذُوفٍ» (ḥāl, ṣifa, khabar, khabar kāna or inna)
- **Judgement**: A governor that is present is not deleted: «أَوْ لَمْ يُحْذَفْ مُتَعَلَّقُهُ يُسَمَّيَانِ ظَرْفًا لَغْوًا» (I.16); a fronted laghw keeps its governor (I.15). The khabar of kāna / inna is the written word (خَاشِعِينَ، يَحْلُمُ), so the phrase cannot be it.
- **Book**: `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»; `izhar-al-asrar-matn-lithograph.txt` l.15 «ويجوز تقديم ما عدا هذا على متعلقه نحو بزيد مررت.»
- **Examples**: aqaid-ahl-al-sunna:2:s2:3 لِلْخَلْقِ; aqaid-ahl-al-sunna:2:s4:4 بِهَا; aqaid-ahl-al-sunna:39:s1:11 لِمَنْ

### T-C-mamnu — Case ending and role — DabtEngine · E — the engine is wrong · 31

- **Shape**: engine: kasra / tanwīn on a diptote the author declines with the fatḥa (جَهَنَّمَ، سَقَرَ، حِمْصَ، فَارِسَ، تِرْمِذَ، عَوْجَاءَ، أَشْأَمَ) or the opposite
- **Judgement**: «مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ» (S.30).
- **Book**: `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ»
- **Examples**: adam-wa-iblis:1:s2:4 الْأَشْيَاءِ; al-usul-al-munifa:14:s20:35 جَهَنَّمَ; al-usul-al-munifa:19:s7:33 جَهَنَّمَ

### T-J04 — Clause maḥall — JumlaMahallEngine · C — both right · 30

- **Shape**: OFFERED: the author names a reading the books allow beside the engine's two (ḥāl where the engine offers naʿt-or-khabar, istiʾnāf where it offers naʿt-or-ḥāl, the outer maqūl against the inner khabar, the taʿlīliyya إِذْ, the follower of a clause after لَمَّا / إِذْ), often citing the poem's commentator
- **Judgement**: Both readings stand (m.51 ḥāl, m.84 naʿt, m.86 the follower); the engine marks its own line «offered» for exactly this reason.
- **Book**: `qawaid-al-irab-ibn-hisham-matn.txt` l.51 «ومحلهما النصب.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.84 «والسادسة … التابعة لمفرد … فالجملة المنعوت بها …»; `qawaid-al-irab-ibn-hisham-matn.txt` l.86 «والسابعة … التابعة لجملة لها محل … نحو: زيدٌ قام أبوه وقعد أخوه.»
- **Examples**: muallaqat-amr-ibn-kulthum:13:s6:5 نُحَاذِرُ; muallaqat-tarafa:3:s1:2 تُرَاعِي; muallaqat-tarafa:7:s2:2 تَعْرِفُ

### T-S01 — Sign of the case — SignEngine · L — the line is wrong (certain) · 24

- **Shape**: author: «مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ» on a SINGULAR whose nūn is a root letter (دُونَ، حِينَ، دِينَ، الْمِسْكِينَ، نُونَ) / engine: fatḥa
- **Judgement**: دُونَ، حِينَ، دِينَ، نُونَ، الْمِسْكِينَ are singular nouns (the nūn is the third radical); the sound masculine plural is «كَالزَّيْدُونَ وَالْمُسْلِمُونَ» (l.43) — these take the base sign, naṣb by the fatḥa (l.25).
- **Book**: `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»; `shudhur-al-dhahab-src.txt` l.43 «الْخَامِسُ: جَمْعُ الْمُذَكَّرِ السَّالِمُ، كَالزَّيْدُونَ وَالْمُسْلِمُونَ، فَإِنَّهُ يُرْفَعُ بِالْوَاوِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَكْسُورِ مَا قَبْلَهَا الْمَفْتُوحِ مَا بَعْدَهَا.»
- **Examples**: al-usul-al-munifa:3:s11:21 دِينَكُمْ; al-usul-al-munifa:14:s4:19 دُونَ; al-usul-al-munifa:18:s12:30 دُونَ

### T-C-nasb — Case ending and role — DabtEngine · E — the engine is wrong · 22

- **Shape**: engine: another naṣb office (ḥāl, tamyīz, ẓarf, khabar kāna, ism inna, ism lā) on a word the text writes in another case
- **Judgement**: The written vowel and the line agree; the engine's office has no governor here (a majrūr naʿt read as ḥāl: مُسْلِمٍ … مُكَلَّفٍ).
- **Book**: `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»; `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»
- **Examples**: al-maqamat-birgivi:3:s3:10 مُكَلَّفٍ; al-usul-al-munifa:19:s2:23 قَبْلِ; al-usul-al-munifa:25:s15:51 بِوَاحِدَةٍ

### T-C-hikaya — Case ending and role — DabtEngine · E — the engine is wrong · 22

- **Shape**: engine: a case ending on a QUOTED word (لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ: تَفَعَّلَ، اسْتَفْعَلَ، أَلْ، خُذْ، اِيدَدْ)
- **Judgement**: A quoted word keeps its own form; its case is maḥallī (the author says «فِي مَحَلِّ …»). iʿrāb falls on the declinable noun in use (S.22).
- **Book**: `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»
- **Examples**: shudhur-al-dhahab:1:s5:14 هَاتِ; shudhur-al-dhahab:4:s1:16 أَلْ; talkhis-al-miftah:55:s6:5 مِثْلِ

### T-I01 — إِنَّ / أَنَّ — InnaEngine · E — the engine is wrong · 21

- **Shape**: engine: kasr «in the ibtidāʾ / istiʾnāf / ʿaṭf» on a أَنَّ that opens a new sentence, follows a colon, or follows «غَيْرَ» / author: fatḥ — the maṣdar is the khabar (الْفَرْقُ …: أَنَّ …، وَمِنْهَا أَنَّ …، فَإِنَّهَا: أَنَّكَ …) or is joined by و to an earlier maṣdar (وَأَنَّا الْعَاصِمُونَ، وَأَنَّ اللهَ بَاقٍ) or follows غَيْرَ
- **Judgement**: Kasr only in the seats l.179 lists, «وتُفْتَحُ في الباقي». A sentence break in the reader is not the grammar's ibtidāʾ when the maṣdar is still owed to an earlier word (khabar, maʿṭūf, object of أَلْهَمَ, the bāʾ of «أَنِّي قَدْ جِئْتُكُمْ»).
- **Book**: `shudhur-al-dhahab-src.txt` l.179 «وتُكسَرُ «إِنَّ» في الابْتِدَاءِ، وَفي أَوَّلِ الصِّلَةِ وَالصِّفةِ والْجُملة الحاليَّة، وَالمُضَافِ إِلَيْهَا ما يخْتَصُّ بالجُمَلِ، والمَحْكيّةِ بالْقَوْل، وَجَوَابِ الْقسَم، والمُخْبَر بها عن اسم عَيْنٍ، وَقبْلَ اللَّامِ المُعلِّقةِ، … وتُفْتَحُ في الباقي.»
- **Examples**: al-kafiya:17:s2:6 أَنَّ; al-kafiya:24:s9:2 أَنَّ; al-kafiya:43:s6:5 أَنَّ

### T-T04 — Taʿalluq — TaalluqEngine · C — both right · 21

- **Shape**: author: the maṣdar / noun right before the phrase (قِيَامٌ بِذَاتِهِ، أَمَانٌ عَنِ الْعِصْيَانِ، عَقْدٌ عَلَى الْمَنَافِعِ، هُدًى لِلْمُتَّقِينَ، يَكُونُ لِي وَلَدٌ) / engine: a deleted naʿt / ḥāl of that noun (or kāna nāqiṣa); or author the maṣdar, engine the verb (خَوْفًا عَلَى … / سَارَ)
- **Judgement**: Both readings are the books': laghw with the maṣdar (I.16) or mustaqarr as its ṣifa / ḥāl (I.15); kāna complete with the phrase laghw, or nāqiṣa with the phrase its fronted khabar. The meaning does not change.
- **Book**: `izhar-al-asrar-matn-lithograph.txt` l.15 «ومجرور ما عدا هذه السبعة منصوب المحل على أنه مفعول فيه لمتعلقه … وقد يحذف المتعلق، فإن كان المحذوف فعلا عاما متضمنا في الجار والمجرور يسميان ظرفا مستقرا نحو زيد في الدار أي»; `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»
- **Examples**: aqaid-ahl-al-sunna:28:s2:5 بِذَاتِهِ; bad-al-amali:6:s28:5 عَنِ; bad-al-amali:7:s34:4 عَلَى

### T-J02 — Clause maḥall — JumlaMahallEngine · C — both right · 15

- **Shape**: exact rules: the author names another true fact about the same clause — a follower (ʿaṭf on a clause with a seat), the outer ṣila while the engine names the inner khabar, istiʾnāf / duʿāʾ for a muʿtariḍa, the maqūl's first word, the verb's own jazm, the oath's answer inside a khabar
- **Judgement**: Ruled in v339-M one by one: m.86 (the follower shares its head clause's seat), m.124 (the ṣila and the khabar inside it), m.128 (the muʿtariḍa has no seat, as the istiʾnāfiyya).
- **Book**: `qawaid-al-irab-ibn-hisham-matn.txt` l.86 «والسابعة … التابعة لجملة لها محل … نحو: زيدٌ قام أبوه وقعد أخوه.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.124 «الثانيةً الواقعةَ صلةً لاسمٍ، نحو: جاء الَّذي قام أبوه …»
- **settled-by**: CLAUDE.md v339-M narrowing pass (compatible facts)
- **Examples**: bad-al-amali:3:s11:4 تَعَالَى; izhar-al-asrar:4:s8:12 لَتَنُوءُ; marah-al-arwah:9:s3:13 وَضَارِبٍ

### T-T05 — Taʿalluq — TaalluqEngine · C — both right · 14

- **Shape**: audit artefact: the author names the governor by description («الْفِعْلُ قَبْلَهُ», «خَبَرُ كَانَ الْمُقَدَّمُ», «حَالٌ: كَائِنَتَيْنِ», «رَسُولٌ (أَوْ بِمَحْذُوفٍ حَالٌ)») and the engine names that same word or seat
- **Judgement**: The two agree; the v328 comparison reads «مُتَعَلِّقٌ بِـX» literally and cannot match a description. A fix belongs in the audit's reader (GrammarAudit339.taalluq), not in the engine or the line.
- **Book**: `izhar-al-asrar-matn-lithograph.txt` l.15 «ومجرور ما عدا هذه السبعة منصوب المحل على أنه مفعول فيه لمتعلقه … وقد يحذف المتعلق، فإن كان المحذوف فعلا عاما متضمنا في الجار والمجرور يسميان ظرفا مستقرا نحو زيد في الدار أي»
- **Examples**: qisas-al-nabiyyin-1:9:s10:2 مَعَنَا; qisas-al-nabiyyin-1:13:s7:3 لَهُمَا; qisas-al-nabiyyin-1:20:s8:13 عَلَيْهِ

### T-S03 — Sign of the case — SignEngine · E — the engine is wrong · 13

- **Shape**: author: «حَذْفُ النُّونِ» on a five-verb of a weak-final lemma (يَغْزُوا، تَغْزِي، يَرْمِيَا، يَحُلُّوا، تَرَيَا، تَرَيْنَ، يَغُرُّوكُمْ) / engine: ḥadhf ḥarf al-ʿilla or sukūn
- **Judgement**: The dual / plural / feminine-singular muḍāriʿ is one of the five verbs whatever its lemma: «وَتُنْصَبُ وَتُجْزَمُ بِحَذْفِهَا» (l.48) — the nūn, not the weak letter.
- **Book**: `shudhur-al-dhahab-src.txt` l.48 «السَّادِسُ: يَفْعَلَانِ وَتَفْعَلَانِ وَيَفْعَلُونَ وَتَفْعَلُونَ وَتَفْعَلِينَ، فَإِنَّهَا تُرْفَعُ بِثُبُوتِ النُّونِ، وَتُنْصَبُ وَتُجْزَمُ بِحَذْفِهَا.»
- **Examples**: al-kafiya:22:s5:19 فَلْيُصَلُّوا; muallaqat-al-harith:8:s4:2 يَغُرُّوكُمُ; muallaqat-al-harith:13:s3:2 يُحِلُّوا

### T-H02 — The Shudhūr rules — Sh336Engine (v336-Sh) · C — both right · 13

- **Shape**: author: the verb's own iʿrāb, silent on its suspension / engine: adds «فِعْلٌ قَلْبِيٌّ مُعَلَّقٌ عَنِ الْعَمَلِ …» (R209); مَاذَا: author mubtadaʾ + relative khabar «وَيَجُوزُ …», engine the object reading «أَوْ …»; صَفِيفَ: both say object of مُنْضِجٍ
- **Judgement**: Compatible facts: the author names the verb, the engine names one more true fact (the taʿlīq by the question / لَوْ / the lām). Both readings of مَاذَا are named in both lines.
- **Book**: `shudhur-al-dhahab-src.txt` l.303 «وَيَجُوزُ إِلْغَاءُ الْقَلْبِيَّةِ الْمُتَصَرِّفَةِ مُتَوَسِّطَةً أَوْ مُتَأَخِّرَةً، وَيَجِبُ تَعْلِيقُهَا قَبْلَ لَامِ الابْتِدَاءِ أو القَسَم، أوِ اسْتِفْهَامٍ، أَوْ نَفْيٍ بِما مُطْلَقًا …»
- **Examples**: al-usul-al-munifa:2:s16:18 تَدْرِي; al-usul-al-munifa:5:s5:7 رَأَيْتَ; al-usul-al-munifa:5:s6:6 أَرَأَيْتَ

### T-S05 — Sign of the case — SignEngine · E — the engine is wrong · 12

- **Shape**: author: a case vowel on a declinable noun (بَيْنَ، كُلَّمَا، أَيِّكُمْ، أَيَّتِهِمَا، هَمٍّ، هَمُّهُ، هَنٍ، جِنِّي، عَصًا، رَبِّي، وَاللهِ) / engine: «mahall» (reads it as a particle or a built word)
- **Judgement**: Each is a mutamakkin noun (l.22) — بَيْنَ and كُلَّ are declinable ẓurūf, أَيّ is muʿrab outside the one relative case (l.88), هَمّ / هَن are nouns; the author is right.
- **Book**: `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»; `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ، نَحْوُ «بِأَفْضَلِكُمْ» «وَبِالْأَفْضَلِ».»; `shudhur-al-dhahab-src.txt` l.88 «… وَ«أيٌّ» الْمَوصُولَةُ إذا أضِيفَتْ وكانَ صَدْرُ صِلَتِهَا ضَمِيرًا مَحذُوفًا، نحو: ﴿أَيُّهُمْ أَشَدُّ﴾ [مريم ٦٩] وَبَعْضُهُمْ يُعْرِبُهَا مُطلَقًا.»
- **Examples**: dawud-wa-jalut:4:s1:7 بِعَصًا; dawud-wa-jalut:4:s2:8 بِرَبِّي; marah-al-arwah:6:s3:12 بِأَيِّكُمُ

### T-S07 — Sign of the case — SignEngine · E — the engine is wrong · 10

- **Shape**: the class misread on a single word: مَعَانٍ (manqūṣ diptote, fatḥa estimated) read as sound; مُثَنَّاهَا (singular maqṣūr) read as dual; أَخَاهُ / أَبَاهُ (five nouns) read as dual; أَيَّمَا read as dual; قَنَاتَنَا (singular) and قُضَاتَهَا (broken plural) read as feminine plural; عَمْرٌو read as a plural; نَاصِرِينَ after the extra مِنْ; لَتُبْلَوُنَّ (thubūt al-nūn deleted)
- **Judgement**: Each authored line names the right sign: قُضَاة is «رَأَيْتُ قُضَاةً» of l.32 (not a feminine plural); أَخَاهُ / أَبَاهُ l.34; the rest by l.54 and l.48.
- **Book**: `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا، وَالضَّمَّةُ وَالْفَتْحَةُ فِي نَحْوِ «يَخْشَى»، وَالضَّمَّةُ فِي نَحْوِ «يَدْعُو» «وَيَرْمِي».»; `shudhur-al-dhahab-src.txt` l.34 «الثَّالِثُ: «ذُو» بِمَعْنَى صَاحِبٍ، وَمَا أُضِيفَ لِغَيْرِ الْيَاءِ مِنْ «أَبٍ» «وَأَخٍ» «وَحَمٍ» «وَهَنٍ» «وَفَمٍ» بِغَيْرِ مِيمٍ، فَإِنَّهَا تُعْرَبُ بِالْوَاوِ وَالْأَلِفِ وَالْيَاءِ.»; `shudhur-al-dhahab-src.txt` l.32 «الثَّانِي: مَا جُمِعَ بِأَلِفٍ وَتَاءٍ مَزِيدَتَيْنِ، «كَهِنْدَاتٍ» فَإِنَّهُ يُنْصَبُ بِالْكَسْرَةِ نَحْوُ: «خَلَقَ اللهُ السَّمَاوَاتِ» «فَانْفِرُوا ثُبَاتٍ» بِخِلَافِ نَحْوِ: «وَكُنْتُمْ أَمْوَاتًا» «وَرَأَيْتُ قُضَاةً»، وَأُلْحِقَ بِهِ «أُولَاتُ».»
- **Examples**: al-kafiya:20:s7:14 مَعَانٍ; al-kafiya:20:s8:16 وَمُثَنَّاهَا; ibn-khaldun-wa-timur:3:s3:11 قُضَاتَهَا

### T-A04 — The muʿrib's etiquette — AdabEngine · L — the line is wrong (certain) · 7

- **Shape**: the short term: لَمْ «حَرْفُ نَفْيٍ وَجَزْمٍ» (no قَلْب), لَنْ without اسْتِقْبَال, إِنَّ / أَنَّ «حَرْفٌ نَاسِخٌ»
- **Judgement**: Bāb 4's full expressions (the chapter's own list).
- **Book**: `qawaid-al-irab-turkish.txt` l.70 «(bāb 4) «İ'rab yazarken tam tabir kullanılır: … lem (mazinin hudûsunu nefyeden), len (istikbaldeki hudûsu nefyeden) … inne meksure (ismini nasb haberini ref eden tekid harfi), enne meftuha (aynı amel + mastar te'vili)» — «لَمْ نَفْيٌ وَجَزْمٌ وَقَلْبٌ، لَنْ نَفْيٌ وَنَصْبٌ وَاسْتِقْبَالٌ، إِنَّ تَوْكِيدٌ وَنَصْبٌ، أَنَّ مَعَ الْمَصْدَرِ»»
- **listed-before**: CLAUDE.md wave 40 (v202): the AdabEngine findings «listed in the lab for scholarly review»
- **Examples**: izhar-al-asrar:18:s1:11 لَمْ; izhar-al-asrar:29:s3:14 لَمْ; izhar-al-asrar:42:s5:7 لَمْ

### T-A05 — The muʿrib's etiquette — AdabEngine · L — the line is wrong (likely) · 6

- **Shape**: a bare «زَائِدٌ» on a letter of a Qurʾānic verse
- **Judgement**: Bāb 4: in the Book of God «زَائِدٌ» is said only with its sense — emphasis.
- **Book**: `qawaid-al-irab-turkish.txt` l.80 «(bāb 4) «Allah'ın kitabında herhangi bir harf için «zâiddir» demekten kaçınmak (zâid = manası yalnız te'kid olan demektir)» — «لَا يُقَالُ فِي كِتَابِ اللهِ «حَرْفٌ زَائِدٌ»»»
- **listed-before**: CLAUDE.md wave 40 (v202): the AdabEngine findings «listed in the lab for scholarly review»
- **Examples**: al-kafiya:7:s6:7 مِنْ; al-kafiya:7:s10:10 مِنْ; qisas-al-nabiyyin-4:33:s2:13 نَاصِرِينَ

### T-S09 — Sign of the case — SignEngine · L — the line is wrong (certain) · 6

- **Shape**: author: kasra / ḍamma on a dual or the number two (الِاثْنَيْنِ، لِلِاثْنَيْنِ، اسْمَيْنِ، لِاسْمَيِ، حَيَّانِ) / engine: the letter
- **Judgement**: The dual and اثْنَانِ (l.41) take the letters: rafʿ by the alif, jarr by the yāʾ (l.39).
- **Book**: `shudhur-al-dhahab-src.txt` l.39 «الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَفْتُوحِ مَا قَبْلَهَا الْمَكْسُورِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.41 «وَأُلْحِقَ بِهِ اثْنَانِ، وَاثْنَتَانِ، وَثِنْتَانِ مُطْلَقًا، وَكِلَا وَكِلْتَا مُضَافَيْنِ إِلَى مُضْمَرٍ.»
- **Examples**: izhar-al-asrar:1:s16:13 اسْمَيْنِ; tasrif-al-izzi:10:s1:18 الِاثْنَيْنِ; tasrif-al-izzi:10:s1:28 لِلِاثْنَيْنِ

### T-S11 — Sign of the case — SignEngine · L — the line is wrong (likely) · 6

- **Shape**: jazm sign on كَانَ / the maqṣūr verb: author «حَذْفُ حَرْفِ الْعِلَّةِ / بِحَذْفِ الْوَاوِ» on يَكُ / نَكُ / تَكُنْ, «السُّكُونُ» on يُسَمَّ / engine: the opposite
- **Judgement**: كَانَ is not weak-final (its last letter is the nūn): its jazm is the sukūn (l.25), the wāw fell for the two sukūns and the nūn for lightness. يُسَمَّى IS weak-final: «يُجْزَمُ بِحَذْفِهِ» (l.51).
- **Book**: `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»; `shudhur-al-dhahab-src.txt` l.51 «السَّابِعُ: الْفِعْلُ الْمُعْتَلُّ الْآخِرِ، كَيَغْزُو، وَيَخْشَى، وَيَرْمِي، فَإِنَّهُ يُجْزَمُ بِحَذْفِهِ، وَنَحْوُ «إِنَّهُ مَنْ يَتَّقِي وَيَصْبِرْ» مُؤَوَّلٌ.»
- **Examples**: al-usul-al-munifa:25:s19:52 يَكُ; al-usul-al-munifa:30:s3:43 نَكُ; al-usul-al-munifa:30:s3:47 نَكُ

### T-M01 — The manṣūb offices — MansubEngine (v332) · L — the line is wrong (certain) · 6

- **Shape**: author: «ظَرْفٌ» on the counted noun after أَرْبَعِينَ (لَيْلَةً، يَوْمًا، حَدِيثًا) / engine: tamyīz
- **Judgement**: The number stands in the ẓarf's seat; the noun after it «يَرْفَعُ إِبْهَامَ اسْمٍ» — the tamyīz (l.230).
- **Book**: `shudhur-al-dhahab-src.txt` l.230 «الثَّامِنُ التَّمْييز، وَهُوَ: اسْمٌ، نَكِرَةٌ، فَضْلَةٌ، يَرْفَعُ إِبْهَامَ اسْمٍ، أو إِجْمَالَ نِسْبَةٍ.»
- **listed-before**: CLAUDE.md v332 (corpus slips for the hoca)
- **Examples**: al-usul-al-munifa:1:s5:10 حَدِيثًا; al-usul-al-munifa:12:s2:27 لَيْلَةً; al-usul-al-munifa:12:s2:32 لَيْلَةً

### T-S06 — Sign of the case — SignEngine · E — the engine is wrong · 5

- **Shape**: diptote misjudged by the engine: author fatḥa on an unannexed diptote (لِلُقْمَانَ، بِقَارُونَ، أَجَشَّ، قَاصِرِينَا), kasra on one with «أَلْ» (كَالرَّحْمٰنِ) / engine: the opposite
- **Judgement**: «فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ … إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ» (l.30): لُقْمَانَ، قَارُونَ (ʿalam), أَجَشَّ (waṣf + afʿal, not annexed) by the fatḥa; الرَّحْمٰنِ with أَلْ by the kasra. The author is right in all five.
- **Book**: `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ، نَحْوُ «بِأَفْضَلِكُمْ» «وَبِالْأَفْضَلِ».»
- **Examples**: luqman-wa-ibnuh:1:s4:2 لِلُقْمَانَ; marah-al-arwah:43:s9:9 كَالرَّحْمٰنِ; muallaqat-amr-ibn-kulthum:2:s7:8 وَقَاصِرِينَا

### T-M02 — The manṣūb offices — MansubEngine (v332) · L — the line is wrong (certain) · 5

- **Shape**: author: ḥāl / mafʿūl muṭlaq on the tamyīz of an elative or of «مِثْقَالَ ذَرَّةٍ» (مَنْزِلَةً، خَيْرًا، شَرًّا); ḥāl on a same-root maṣdar after its verb (رَحِمَهُ … رَحْمَةً، يُفَسِّرُونَهُ تَفْسِيرًا) / engine: tamyīz; mafʿūl muṭlaq
- **Judgement**: l.230 (the tamyīz removes the vagueness of a measure or of a relation); l.204 (the maṣdar that confirms or qualifies its own verb is the mafʿūl muṭlaq).
- **Book**: `shudhur-al-dhahab-src.txt` l.230 «الثَّامِنُ التَّمْييز، وَهُوَ: اسْمٌ، نَكِرَةٌ، فَضْلَةٌ، يَرْفَعُ إِبْهَامَ اسْمٍ، أو إِجْمَالَ نِسْبَةٍ.»; `shudhur-al-dhahab-src.txt` l.204 «الثَّاني المَفْعُول المطلَقُ، وَهُوَ: الْمَصْدَرُ الْفَضْلَةُ الْمُؤَكِّدُ لِعَامِلِهِ أو الْمبيِّنُ لِنَوْعِهِ أَوْ لِعَدَدِهِ، كـ«ضَرَبْتُ ضَرْبًا» أَو «ضَرْبَ الأميرِ»»
- **listed-before**: CLAUDE.md v332 (corpus slips for the hoca)
- **Examples**: al-usul-al-munifa:24:s20:7 مَنْزِلَةً; al-usul-al-munifa:26:s2:75 خَيْرًا; al-usul-al-munifa:26:s2:81 شَرًّا

### T-M03 — The manṣūb offices — MansubEngine (v332) · L — the line is wrong (likely) · 5

- **Shape**: author: an office with no governor for it — naʿt for the delayed ism of إِنَّ (فَإِنَّ لِكُلِّ حَقٍّ حَقِيقَةً) and for kāna's khabar (يَكُونُ الْوَاحِدُ … مُؤْمِنًا); mafʿūl bihi after a verb whose object is already taken or that is intransitive (خَلَقَهُ مُؤْمِنًا، أَنْظُرُ إِلَى عَرْشِ رَبِّي بَارِزًا، يَفِرُّ مِنْهُ مَخَافَةَ …) / engine: ism inna, khabar kāna, ḥāl, mafʿūl lahu
- **Judgement**: A ḥāl is «وَصْفٌ فَضْلَةٌ مَسُوقٌ لِبَيَانِ هَيْئَةِ صَاحِبِهِ» (l.222) — بَارِزًا، مُؤْمِنًا after a complete clause; the maṣdar of motive is the mafʿūl lahu (l.208); there is no naʿt without a described noun of its case.
- **Book**: `shudhur-al-dhahab-src.txt` l.222 «السَّابعُ الْحَالُ، وَهُوَ: وَصْفٌ فَضْلَةٌ مَسُوقٌ لِبَيَانِ هَيْئَةِ صَاحِبِهِ أوْ تَأْكِيدِهِ، أَوْ تأْكِيدِ عَامِلِهِ»; `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»; `shudhur-al-dhahab-src.txt` l.208 «الثالث المَفْعُول لهُ، وهوَ المَصْدَرُ الْفَضْلَةُ الْمُعَلِّل لِحَدَثٍ شَاركه في الزَّمَان والْفاعِل، كـ«قُمتُ إِجْلَالًا لَكَ»»; `shudhur-al-dhahab-src.txt` l.174 «الثامنُ خبرُ «إِنَّ» وأَخَوَاتِهَا: وَلكِنَّ، وَكَأَنَّ، وَلَيْتَ، ولَعَلَّ، نحوُ: ﴿إِنَّ ٱلسَّاعَةَ ءَاتِيَةٌ﴾»
- **Examples**: al-usul-al-munifa:20:s2:45 حَقِيقَةً; al-usul-al-munifa:22:s1:34 مُؤْمِنًا; al-usul-al-munifa:14:s2:17 مُؤْمِنًا

### T-I02 — إِنَّ / أَنَّ — InnaEngine · E — the engine is wrong · 4

- **Shape**: engine: fatḥ on a received إِنَّ that opens a sentence or answers an oath (﴿إِنَّهُ مِنْ عِبَادِنَا﴾، ﴿إِنِّي أَخَافُ عَلَيْكُمْ﴾، «إِنَّ اللهَ أَرَادَ»، إِنَّنِي after the oath) / author: kasr
- **Judgement**: l.179: kasr «في الابتداء … وجواب القسم». The Qurʾān and the poem are received text.
- **Book**: `shudhur-al-dhahab-src.txt` l.179 «وتُكسَرُ «إِنَّ» في الابْتِدَاءِ، وَفي أَوَّلِ الصِّلَةِ وَالصِّفةِ والْجُملة الحاليَّة، وَالمُضَافِ إِلَيْهَا ما يخْتَصُّ بالجُمَلِ، والمَحْكيّةِ بالْقَوْل، وَجَوَابِ الْقسَم، والمُخْبَر بها عن اسم عَيْنٍ، وَقبْلَ اللَّامِ المُعلِّقةِ، … وتُفْتَحُ في الباقي.»
- **Examples**: al-usul-al-munifa:14:s15:33 إِنَّهُ; muallaqat-tarafa:12:s5:4 إِنَّنِي; qisas-al-nabiyyin-2:7:s7:17 إِنِّي

### T-J01 — Clause maḥall — JumlaMahallEngine · L — the line is wrong (certain) · 4

- **Shape**: author: «فِي مَحَلِّ جَزْمٍ» on a jāzim's answer with no fāʾ (قَتَلْتُكُمْ، جَاءَكُمْ، ارْتَدَعَ); ḥāl for the clause after a pure indefinite carrying its pronoun (غَذَاهَا) / engine: no seat; naʿt
- **Judgement**: m.67 «إن قام أخوك قامَ عمرٌو»: the verb is jazm, the clause has no seat; m.84: the clause after a pure indefinite is its naʿt.
- **Book**: `qawaid-al-irab-ibn-hisham-matn.txt` l.67 «فأما نحو: إن قام أخوك قامَ عمرٌو.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.84 «والسادسة … التابعة لمفرد … فالجملة المنعوت بها …»
- **settled-by**: CLAUDE.md v339-M narrowing pass («The 19 exact contradictions, each read»: authored slips)
- **listed-before**: CLAUDE.md v339-M
- **Examples**: ashab-al-kahf:1:s3:15 قَتَلْتُكُمْ; hud-wa-aad:2:s7:6 جَاءَكُمْ; talkhis-al-miftah:4:s3:12 ارْتَدَعَ

### T-S04 — Sign of the case — SignEngine · E — the engine is wrong · 4

- **Shape**: author: fatḥa (shown or estimated) on a muḍāriʿ after أَنْ whose final alif is the verse's alif al-iṭlāq or a pronoun-carrying maqṣūr (نَدِينَا، يَكُونَا، تَلِينَا، تَرَاهُ) / engine: «five verbs, ḥadhf al-nūn»
- **Judgement**: «أَنْ نَدِينَا» is نَدِينَ + the rhyme's alif (the poem's commentator says so in the line); «أَنْ تَرَاهُ» is تَرَى + the pronoun, fatḥa estimated on the alif (l.54). Neither is a dual.
- **Book**: `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»; `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا، وَالضَّمَّةُ وَالْفَتْحَةُ فِي نَحْوِ «يَخْشَى»، وَالضَّمَّةُ فِي نَحْوِ «يَدْعُو» «وَيَرْمِي».»
- **Examples**: izhar-al-asrar:19:s11:7 تَرَاهُ; muallaqat-amr-ibn-kulthum:5:s3:9 نَدِينَا; muallaqat-amr-ibn-kulthum:8:s2:10 يَكُونَا

### T-S10 — Sign of the case — SignEngine · L — the line is wrong (likely) · 4

- **Shape**: the author's line contradicts itself: a wrong vowel first, then the right letter after « — » (لِلصَّابِرِينَ «بِالْكَسْرَةِ — بِالْيَاءِ»، كَثِيرِينَ، آخَرُونَ، وَيُكَلِّلُونَ)
- **Judgement**: The second clause is right (l.43, l.48); the first must go — the parser read the first.
- **Book**: `shudhur-al-dhahab-src.txt` l.39 «الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَفْتُوحِ مَا قَبْلَهَا الْمَكْسُورِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.43 «الْخَامِسُ: جَمْعُ الْمُذَكَّرِ السَّالِمُ، كَالزَّيْدُونَ وَالْمُسْلِمُونَ، فَإِنَّهُ يُرْفَعُ بِالْوَاوِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَكْسُورِ مَا قَبْلَهَا الْمَفْتُوحِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.48 «السَّادِسُ: يَفْعَلَانِ وَتَفْعَلَانِ وَيَفْعَلُونَ وَتَفْعَلُونَ وَتَفْعَلِينَ، فَإِنَّهَا تُرْفَعُ بِثُبُوتِ النُّونِ، وَتُنْصَبُ وَتُجْزَمُ بِحَذْفِهَا.»
- **Examples**: ayyub-wa-al-sabr:4:s3:4 لِلصَّابِرِينَ; dhu-al-qarnayn-wa-al-sadd:1:s2:12 كَثِيرِينَ; juha-wa-al-himar:2:s1:5 آخَرُونَ

### T-S15 — Sign of the case — SignEngine · L — the line is wrong (certain) · 4

- **Shape**: author: «مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ» on a singular in ـَاة before a pronoun (صَلَاتَهُمْ، مَرْضَاتَهُ، زَكَاتَهُ) / engine: fatḥa
- **Judgement**: صَلَاة، مَرْضَاة، زَكَاة are singulars; their tāʾ is the feminine tāʾ, not «أَلِفٌ وَتَاءٌ مَزِيدَتَانِ» (l.32) — naṣb by the fatḥa (l.25), as the written vowel shows.
- **Book**: `shudhur-al-dhahab-src.txt` l.32 «الثَّانِي: مَا جُمِعَ بِأَلِفٍ وَتَاءٍ مَزِيدَتَيْنِ، «كَهِنْدَاتٍ» فَإِنَّهُ يُنْصَبُ بِالْكَسْرَةِ نَحْوُ: «خَلَقَ اللهُ السَّمَاوَاتِ» «فَانْفِرُوا ثُبَاتٍ» بِخِلَافِ نَحْوِ: «وَكُنْتُمْ أَمْوَاتًا» «وَرَأَيْتُ قُضَاةً»، وَأُلْحِقَ بِهِ «أُولَاتُ».»; `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Examples**: al-usul-al-munifa:22:s11:21 وَصَلَاتَهُمْ; al-usul-al-munifa:23:s7:34 مَرْضَاتَهُ; al-usul-al-munifa:24:s7:36 زَكَاتَهُ

### T-H01 — The Shudhūr rules — Sh336Engine (v336-Sh) · C — both right · 4

- **Shape**: «مَا» nāfiya: author «نَافِيَةٌ» (khabar «مَرْفُوعٌ مَحَلًّا» — the Tamīmī reading) / engine: ḥijāziyya working as لَيْسَ, or muhmala (both named)
- **Judgement**: Both are the books' (bāb 28: what works like لَيْسَ; Tamīm leave it idle); the engine names both and the author one of them.
- **Book**: `shudhur-al-dhahab-src.txt` l.170 «وَ«ما» وَ«لا» النَّافِيَتَانِ في لُغَةِ الْحِجَازِ، وَ«إِنِ» النَّافِيَةُ في لُغَةِ أَهْلِ الْعَالِيَةِ، وَشَرْطُ إِعْمَالِهِنَّ …»
- **Examples**: al-kafiya:32:s4:24 مَا; al-kafiya:32:s4:26 بِقَائِمٍ; qisas-al-nabiyyin-2:32:s6:8 وَمَا

### T-A06 — The muʿrib's etiquette — AdabEngine · L — the line is wrong (likely) · 3

- **Shape**: a muḍāf whose own case is not stated (بِدَارِ، بِأَنْوَاعِ: the line names the bāʾ and «وَهُوَ مُضَافٌ» only); a stray «— الْمُضَافُ» closing the line on كَانَ
- **Judgement**: Bāb 4: the muḍāf's iʿrāb is stated by its governor («مَجْرُورٌ بِالْبَاءِ»).
- **Book**: `qawaid-al-irab-turkish.txt` l.79 «(bāb 4) «muzaf hakkında «üzerine i'rab zahir olmaz» demek (i'rabı sabittir, âmiline göredir)» — «إِعْرَابُ الْمُضَافِ ثَابِتٌ بِحَسَبِ عَامِلِهِ»»
- **listed-before**: CLAUDE.md wave 40 (v202): the AdabEngine findings «listed in the lab for scholarly review»
- **Examples**: bad-al-amali:7:s32:3 بِدَارِ; bad-al-amali:8:s40:5 بِأَنْوَاعِ; izhar-al-asrar:42:s6:2 كَانَ

### T-C-L6 — Case ending and role — DabtEngine · L — the line is wrong (certain) · 3

- **Shape**: the same three singulars as T-S15 (صَلَاتَهُمْ، مَرْضَاتَهُ، زَكَاتَهُ) — here the case engine agrees with the wrong line and contradicts the written fatḥa
- **Judgement**: As T-S15.
- **Book**: `shudhur-al-dhahab-src.txt` l.32 «الثَّانِي: مَا جُمِعَ بِأَلِفٍ وَتَاءٍ مَزِيدَتَيْنِ … فَإِنَّهُ يُنْصَبُ بِالْكَسْرَةِ»
- **listed-before**: CLAUDE.md v329 / v333 (corpus slips for the hoca)
- **Examples**: al-usul-al-munifa:23:s7:34 مَرْضَاتَهُ; al-usul-al-munifa:24:s7:36 زَكَاتَهُ; al-usul-al-munifa:24:s7:59 زَكَاتَهُ

### T-C-C1 — Case ending and role — DabtEngine · C — both right · 3

- **Shape**: the written form is the pausal / isolated one (أَوْ، أَكْثَرِهِمْ، كُلِّهِمْ in a verse); the engine names the connected-speech vowel before a hamzat al-waṣl
- **Judgement**: Both right: the line parses the word; the engine names the vowel of the joining (iltiqāʾ al-sākinayn). Not a case question.
- **Book**: `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Examples**: al-kafiya:27:s5:18 أَكْثَرِهِمْ; al-kafiya:28:s6:20 أَوْ; muallaqat-amr-ibn-kulthum:8:s5:3 كُلِّهِمُ

### T-S12 — Sign of the case — SignEngine · L — the line is wrong (likely) · 3

- **Shape**: single slips: وَكِلَا «مَرْفُوعٌ بِأَلِفٍ مُقَدَّرَةٍ» (a cited كِلَا, maqṣūr: ḍamma estimated); كَرَضِيَ «مَجْرُورٌ بِالْفَتْحَةِ» (a quoted verb: jarr by ḥikāya, no sign); بَابَيْ read as «بَابِي» with the speaker's yāʾ (a dual annexed: the yāʾ)
- **Judgement**: l.54 (all vowels estimated on the maqṣūr's alif); l.39 for بَابَيْ; a quoted verb has no case of its own.
- **Book**: `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا، وَالضَّمَّةُ وَالْفَتْحَةُ فِي نَحْوِ «يَخْشَى»، وَالضَّمَّةُ فِي نَحْوِ «يَدْعُو» «وَيَرْمِي».»
- **Examples**: izhar-al-asrar:53:s5:10 وَكِلَا; tasrif-al-izzi:16:s16:4 كَرَضِيَ; tasrif-al-izzi:15:s29:10 بَابَيْ

### T-S13 — Sign of the case — SignEngine · undecided · 3

- **Shape**: «بِلَا» with لَا «بِمَعْنَى غَيْرٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ» / engine: a particle, maḥall
- **Judgement**: Whether لَا in بِلَا is a noun (the Kūfan reading the author follows) or a particle the jarr crosses: no line of the books on the shelf decides it.
- **Book**: — (no book line decides)
- **Examples**: izhar-al-asrar:11:s3:5 بِلَا; izhar-al-asrar:11:s5:12 بِلَا; izhar-al-asrar:13:s6:4 بِلَا

### T-C-L2 — Case ending and role — DabtEngine · L — the line is wrong (certain) · 2

- **Shape**: author parses a verb as something else: «فَاعْبُدُونِ» as «مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ»; «وَأَلْزَمَهُمْ» (a māḍī, Q 48:26) as «فِعْلٌ مُضَارِعٌ مَنْصُوبٌ»
- **Judgement**: فَاعْبُدُونِ is an amr built on the dropping of the nūn, the nūn of protection and the yāʾ (dropped) its object; أَلْزَمَ is a māḍī built on the fatḥ (S.71).
- **Book**: `shudhur-al-dhahab-src.txt` l.71 «أو الفَتْحِ، وَهُوَ سَبْعَةٌ: الماضي المجرَّدُ كضَرَبَ وضرَبكَ وضَرَبَا،»; `shudhur-al-dhahab-src.txt` l.195 «ومِنْهُ الْمُنَادَى، وَإِنَّمَا يَظْهَرُ نَصْبُهُ إذا كَانَ مضَافًا أوْ شِبْهَهُ أو نكِرَةً مَجْهُولَةً، نَحْوُ: «يَا عَبْدَ اللهِ»»
- **Examples**: al-usul-al-munifa:16:s2:27 فَاعْبُدُونِ; al-usul-al-munifa:18:s11:3 وَأَلْزَمَهُمْ

### T-C-U1 — Case ending and role — DabtEngine · undecided · 2

- **Shape**: فَيُسَمِّيهِ after «بِأَنْ يَكُونَ … وَيُظْهِرَ» (ʿaṭf in naṣb, or a fresh rafʿ?); أَمُرْسَلِينَ هُمَا (the line says «بِالْوَاوِ», the text writes the yāʾ)
- **Judgement**: Whether the fāʾ joins or resumes, and how the received fiqh text is to be read, no book line decides.
- **Book**: — (no book line decides)
- **Examples**: al-usul-al-munifa:18:s8:36 فَيُسَمِّيهِ; al-usul-al-munifa:19:s4:18 أَمُرْسَلِينَ

### T-I03 — إِنَّ / أَنَّ — InnaEngine · L — the line is wrong (likely) · 2

- **Shape**: text and line: أَنَّ where the books require kasr — before the suspending lām (عَنَوْا أَنَّكَ لَفِي كُفْرِكَ) and as the quoted clause after تَقُولُ (وَلَا تَقُولُ أَنَّهُمْ مِنْ أَهْلِ النَّارِ) / engine: kasr
- **Judgement**: l.179: «والمحكيّة بالقول … وقبل اللام المعلِّقة». The line's «أَنْ حَرْفُ تَوْكِيدٍ» should read «إِنَّ» (and the token's hamza). Not a received Qurʾānic text; the hoca decides whether the edition printed أن.
- **Book**: `shudhur-al-dhahab-src.txt` l.179 «وتُكسَرُ «إِنَّ» في الابْتِدَاءِ، وَفي أَوَّلِ الصِّلَةِ وَالصِّفةِ والْجُملة الحاليَّة، وَالمُضَافِ إِلَيْهَا ما يخْتَصُّ بالجُمَلِ، والمَحْكيّةِ بالْقَوْل، وَجَوَابِ الْقسَم، والمُخْبَر بها عن اسم عَيْنٍ، وَقبْلَ اللَّامِ المُعلِّقةِ، … وتُفْتَحُ في الباقي.»
- **Examples**: al-usul-al-munifa:24:s11:14 أَنَّكَ; al-usul-al-munifa:25:s6:31 أَنَّهُمْ

### T-S08 — Sign of the case — SignEngine · L — the line is wrong (certain) · 2

- **Shape**: author: «مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ» on a maqṣūr WITH tanwīn (مَعْنًى، لِمَعْنًى) / engine: kasra
- **Judgement**: مَعْنًى is munawwan, so not a diptote; the M01 ruling (fatḥa for kasra) is for the maqṣūr DIPTOTE only. All vowels are estimated on its alif (l.54): jarr by the kasra estimated.
- **Book**: `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا، وَالضَّمَّةُ وَالْفَتْحَةُ فِي نَحْوِ «يَخْشَى»، وَالضَّمَّةُ فِي نَحْوِ «يَدْعُو» «وَيَرْمِي».»
- **settled-by**: CLAUDE.md v333 (rule M01 scope: the maqṣūr diptote only)
- **Examples**: izhar-al-asrar:51:s7:13 مَعْنًى; marah-al-arwah:53:s1:41 لِمَعْنًى

### T-S14 — Sign of the case — SignEngine · E — the engine is wrong · 2

- **Shape**: known engine gaps listed before: سِيَّمَا read as a dual; لَمَ الْقَهُمَا read as a built verb
- **Judgement**: سِيَّ is the ism of لَا, manṣūb by the fatḥa as authored; «الْقَهُمَا» is a jussive (the hoca is asked about the printed text).
- **Book**: `shudhur-al-dhahab-src.txt` l.41 «وَأُلْحِقَ بِهِ اثْنَانِ، وَاثْنَتَانِ، وَثِنْتَانِ مُطْلَقًا، وَكِلَا وَكِلْتَا مُضَافَيْنِ إِلَى مُضْمَرٍ.»
- **listed-before**: CLAUDE.md v333 («Left: SignEngine — يَمَانُونْ، سِيَّمَا، وَاللهِ»; ʿAntara «لَمَ الْقَهُمَا» for the hoca)
- **Examples**: muallaqat-imri-al-qays:3:s4:8 سِيَّمَا; muallaqat-antara:12:s6:8 الْقَهُمَا

### T-H04 — The Shudhūr rules — Sh336Engine (v336-Sh) · L — the line is wrong (likely) · 2

- **Shape**: مَرْضَاتَهُ «خَبَرُ كَانَ … بِالْكَسْرَةِ» (the object of طَالِبًا); وَإِلَّا قَاتَلْتَهُ «أَدَاةُ اسْتِثْنَاءٍ» (إِنْ + لَا, the condition dropped)
- **Judgement**: As listed before: the object of the participle (l.188) in the fatḥa; إِلَّا here is the condition's إِنْ with the negation.
- **Book**: `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»
- **listed-before**: CLAUDE.md v336-Sh (engine-found slips for the hoca); v329
- **Examples**: al-usul-al-munifa:23:s7:34 مَرْضَاتَهُ; al-usul-al-munifa:32:s6:8 وَإِلَّا

### T-O01 — Order — TartibEngine · E — the engine is wrong · 2

- **Shape**: «وَغَيْرَانِ الْمُكَوَّنُ» read as two definites (غَيْرَانِ is indefinite: the fronted khabar is free); «لَا يَجُوزُ فِي إِدْغَامِهِنَّ إِلَّا الْإِدْغَامُ» read as an object before the doer (the jarr phrase is no object)
- **Judgement**: The orders are kept: an indefinite khabar may come first; the only noun after إِلَّا is the doer itself.
- **Book**: `shudhur-al-dhahab-src.txt` l.147 «الثَّالِثُ الْمُبْتَدَأُ … مُخْبَرًا عَنْهُ»; `shudhur-al-dhahab-src.txt` l.131 «… أحَدُهَا الْفَاعِلُ»
- **Examples**: bad-al-amali:10:s49:2 الْمُكَوَّنُ; marah-al-arwah:50:s2:3 يَجُوزُ

### T-A07 — The muʿrib's etiquette — AdabEngine · C — both right · 1

- **Shape**: لَعَلَّ «حَرْفُ جَرٍّ فِي لُغَةِ عُقَيْلٍ» flagged as a short term for the inna sister
- **Judgement**: The Iẓhār matn itself lists لَعَلَّ among the jarr letters in that dialect (I.15); the line is right in the example it parses.
- **Book**: `izhar-al-asrar-matn-lithograph.txt` l.15 «ومجرور لولا ولعل مبتدأ وما بعده خبره نحو لولاك لهلك زيد ولعل زيد قائم.»
- **Examples**: izhar-al-asrar:2:s5:12 وَلَعَلَّ

### T-A08 — The muʿrib's etiquette — AdabEngine · E — the engine is wrong · 1

- **Shape**: «أَيْتَامُهَا» «فَاعِلٌ لِـ«شَوَارِعًا»» (the active participle's doer, al-Durra) flagged as a passive's «fāʿil»
- **Judgement**: شَوَارِع is an active participle; its marfūʿ is its fāʿil. The lint took the passive verb of the clause for its governor.
- **Book**: `qawaid-al-irab-turkish.txt` l.70 «(bāb 4) «naibü'l-fail (fail yerine geçen)» — the rule is for the PASSIVE verb's marfūʿ»
- **Examples**: muallaqat-labid:13:s1:8 أَيْتَامُهَا

### T-C-L1 — Case ending and role — DabtEngine · L — the line is wrong (certain) · 1

- **Shape**: author: «مَجْزُومٌ … السُّكُونُ، وَحُرِّكَ آخِرُهُ بِالْفَتْحِ … لِأَنَّهُ مُضَاعَفٌ» on فَلْيُصَلِّ — read as a doubled verb
- **Judgement**: يُصَلِّي (صَلَّى) is weak-final, not doubled: «يُجْزَمُ بِحَذْفِهِ» (S.51); the kasra on the lām is its own.
- **Book**: `shudhur-al-dhahab-src.txt` l.51 «السَّابِعُ: الْفِعْلُ الْمُعْتَلُّ الْآخِرِ، كَيَغْزُو، وَيَخْشَى، وَيَرْمِي، فَإِنَّهُ يُجْزَمُ بِحَذْفِهِ»
- **Examples**: al-usul-al-munifa:31:s4:25 فَلْيُصَلِّ

### T-C-L3 — Case ending and role — DabtEngine · L — the line is wrong (likely) · 1

- **Shape**: author: «مَفْعُولٌ بِهِ» on عَبْدَ in «فَأَنْتَ عَبْدَ اللهِ مُؤْمِنٌ» (no verb governs it)
- **Judgement**: The manṣūb muḍāf with no verb is the munādā with its letter dropped: «يَا عَبْدَ اللهِ» (S.195).
- **Book**: `shudhur-al-dhahab-src.txt` l.195 «ومِنْهُ الْمُنَادَى، وَإِنَّمَا يَظْهَرُ نَصْبُهُ إذا كَانَ مضَافًا أوْ شِبْهَهُ أو نكِرَةً مَجْهُولَةً، نَحْوُ: «يَا عَبْدَ اللهِ»»
- **Examples**: al-usul-al-munifa:20:s12:12 عَبْدَ

### T-C-L4 — Case ending and role — DabtEngine · L — the line is wrong (likely) · 1

- **Shape**: the VOWEL written on the word contradicts the authored line (the line is right): الْمُسْنَدُ written with ḍamma where the line makes it «بَدَلٌ مِنْ هِنْدًا مَنْصُوبٌ»
- **Judgement**: A badal of a manṣūb is manṣūb by the fatḥa (S.25): الْمُسْنَدَ. The text's vowel, not the line, is the slip; the engine follows the line.
- **Book**: `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Examples**: al-kafiya:44:s4:25 الْمُسْنَدُ

### T-C-L5 — Case ending and role — DabtEngine · L — the line is wrong (likely) · 1

- **Shape**: كَرَضِيَ: «وَالِاسْمُ مَجْرُورٌ بِالْفَتْحَةِ» on a quoted verb
- **Judgement**: رَضِيَ is a verb quoted (ḥikāya): «فِي مَحَلِّ جَرٍّ بِالْكَافِ، لَفْظٌ مَحْكِيٌّ». The engine's kasra is also wrong.
- **Book**: `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»
- **Examples**: tasrif-al-izzi:16:s16:4 كَرَضِيَ

### T-M04 — The manṣūb offices — MansubEngine (v332) · E — the engine is wrong · 1

- **Shape**: engine withdraws a naʿt (case mismatch) by taking the nearer majrūr (فِعْلٍ قَلْبِيٍّ) as its head; the author's head is أَفْعَالٌ (marfūʿ): «أَفْعَالٌ تَدُلُّ …، دَاخِلَةٌ …، نَاصِبَةٌ …»
- **Judgement**: The second and third naʿt follow the first head across its own naʿt clause; the veto saw the wrong head.
- **Book**: — (no book line decides)
- **Examples**: izhar-al-asrar:9:s3:11 دَاخِلَةٌ

### T-M05 — The manṣūb offices — MansubEngine (v332) · C — both right · 1

- **Shape**: «وَقَدْ يَبْقَى مَجْرُورًا عَلَى الشُّذُوذِ» — author: khabar of يَبْقَى / engine: ḥāl (offered)
- **Judgement**: بَقِيَ used as a nāqiṣ verb (its khabar) or complete with a ḥāl: both readings are read in the commentaries; the meaning is the same.
- **Book**: `shudhur-al-dhahab-src.txt` l.245 «وَالْبَوَاقي خَبَرُ كَانَ وَأَخَوَاتِها …»; `shudhur-al-dhahab-src.txt` l.222 «السَّابعُ الْحَالُ، وَهُوَ: وَصْفٌ فَضْلَةٌ مَسُوقٌ لِبَيَانِ هَيْئَةِ صَاحِبِهِ أوْ تَأْكِيدِهِ، أَوْ تأْكِيدِ عَامِلِهِ»
- **Examples**: izhar-al-asrar:3:s16:3 مَجْرُورًا

### T-H03 — The Shudhūr rules — Sh336Engine (v336-Sh) · E — the engine is wrong · 1

- **Shape**: «وَمَنْ كَانَ حَفِيظًا وَمَا كَانَ عَلِيمًا لَا يَعْلَمُ …» — author: the clause is the khabar of مَنْ / engine: naʿt of عَلِيمًا
- **Judgement**: عَلِيمًا is kāna's khabar (a single word); the clause after it completes the sentence opened by مَنْ (l.155).
- **Book**: `shudhur-al-dhahab-src.txt` l.155 «الرَّابِعُ خَبَرُهُ، وَهُوَ: مَا تَحْصُلُ بِهِ الْفَائِدَةُ مَعَ مُبْتَدَأ غَيْرِ الْوَصْفِ الْمَذْكُورِ.»
- **Examples**: qisas-al-nabiyyin-1:15:s23:8 يَعْلَمُ

