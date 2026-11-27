# Engine faults from the stories' audit — 2026-11-27 (v342-T)

One entry per **E** cluster of `research/story-audit-triage-2026-11-27.md`, ranked by count. Each gives the engine and rule, what it asserts wrongly, a sentence that reproduces it (typed into the analyzer — `SentenceAnalyzer.analyze(text)` — and run through the engine; the output is the one the probe printed on 2026-11-27, scratchpad `triage342/probes.json`, `probes2.json`), the correct output by the book, and the narrowest gate, with the agreeing verdicts the same rule has (what a fix must not lose). The sign probes call `SignEngine.classify / expect` with the token's own tags, as the audit does — the sign engine has no typed path. No engine code was changed by this wave.

| # | cluster | engine | count | the fault in one line |
|---:|---|---|---:|---|
| 1 | T-T02 | taalluq | 163 | TaalluqEngine.of picks the main verb of the sentence or the nearest preceding word, ignoring a maṣdar / participle that the phrase completes, a governor AFTER a |
| 2 | T-C-tanwin | case | 106 | DabtEngine does not see annexation to a following maṣdar clause (أَنْ …), to a proper noun after ابن, or to a definite second term across a line break. |
| 3 | T-C-mood | case | 87 | DabtEngine mood rules: a verb joined by و / ف to an earlier manṣūb verb inherits naṣb across a clause; the jāzim of a condition is not seen through مَنْ / مَهْم |
| 4 | T-T01 | taalluq | 77 | TaalluqEngine.of returns kind:"found" with the nearest preceding noun / verb when a mustaqarr reading (khabar of a nāsikh or of a mubtadaʾ with no other khabar, |
| 5 | T-J03 | jumla | 72 | JumlaMahallEngine.of: `claimed()` gates only the EXACT naʿt; the offered branches (naatOrHal, naatOrKhabar, halOrNaat, hal, naatOffered's first reading) still f |
| 6 | T-C-built | case | 65 | DabtEngine cell rule re-derives the māḍī's person / the amr form from the paradigm and overwrites the written suffix (it should only fill a missing vowel). |
| 7 | T-C-maful | case | 62 | DabtEngine.decide gives the maful office to a noun after a transitive verb even when the noun is annexed to the word before it (a construct chain) or is itself  |
| 8 | T-C-follower | case | 57 | DabtEngine: the follower rule picks the nearest earlier noun as the head (usually a majrūr) across a verb or a comma. |
| 9 | T-C-verse | case | 56 | DabtEngine's rhyme forgiveness covers only the last word of a marked hemistich; a licence named inside the line (mid-verse) is not read. |
| 10 | T-S02 | sign | 43 | SignEngine.classify returns «sahih; sound» (or maqsur / manqus / mabni-harf) for a word whose authored line names a letter sign and whose surface ends ـَانِ/ـَا |
| 11 | T-C-letters | case | 37 | DabtEngine re-vowels the nūn of a dual / plural and the end of a five-verb. |
| 12 | T-C-raf | case | 36 | DabtEngine gives the doer / mubtadaʾ office to the second half of a laqab (… الدِّين) and to an object after a passive-looking verb. |
| 13 | T-C-jarr | case | 35 | DabtEngine treats a noun after a maṣdar / a participle as its muḍāf ilayh, and drops the jarr after a preposition before a diptote-looking plural (أَشْهُرٍ). |
| 14 | T-C-muqaddar | case | 33 | DabtEngine writes the case vowel on a final yāʾ of a manqūṣ in rafʿ / jarr. |
| 15 | T-T03 | taalluq | 32 | TaalluqEngine asserts a mustaqarr seat (khabar of kāna / inna, ḥāl, ṣifa) for a phrase whose nāsikh already has a written khabar later in the clause, or which s |
| 16 | T-C-mamnu | case | 31 | DabtEngine lacks the diptote causes for place names / feminine names / afʿal adjectives the lexicon does not mark. |
| 17 | T-C-nasb | case | 22 | DabtEngine: the ḥāl rule fires on an indefinite adjective that follows an indefinite majrūr noun (a naʿt). |
| 18 | T-C-hikaya | case | 22 | DabtEngine assigns the seat's vowel to a token the author tags محكي; it should skip tokens with that tag. |
| 19 | T-I01 | inna | 21 | InnaEngine reads «ibtidāʾ» from the token position (first in the sentence, after «:») and «istiʾnāf» after و, without asking whether an open frame (a mubtadaʾ a |
| 20 | T-S03 | sign | 13 | SignEngine.expect picks the weak-final rule from the LEMMA before checking the five-verb suffix (ـَا / ـُوا / ـِي with the nūn gone). |
| 21 | T-S05 | sign | 12 | SignEngine.classify falls to «mabni; harf/mabni» on a homograph of a particle or pronoun (هم، هن، بين) or a word behind a fused jarr letter. |
| 22 | T-S07 | sign | 10 | SignEngine.classify: surface heuristics (ـَاتَ، ـَا، ـُو، ـِينَ) without the lexicon's number / lemma. |
| 23 | T-S06 | sign | 5 | SignEngine: a name in ـُونَ read as a plural; أَجَشَّ followed by an adjective read as annexed; الرَّحْمٰن treated as a diptote despite أَلْ. |
| 24 | T-I02 | inna | 4 | InnaEngine seats «riwāya», «khabar maʿnā» and «mafʿūl» reach past a full stop / a quoted verse into a new sentence. |
| 25 | T-S04 | sign | 4 | SignEngine reads a final ـَا in a verse as the dual's alif; it ignores the rhyme (`rhyme` is passed) and the maqṣūr verb before a pronoun. |
| 26 | T-S14 | sign | 2 | known engine gaps listed before: سِيَّمَا read as a dual; لَمَ الْقَهُمَا read as a built verb |
| 27 | T-O01 | tartib | 2 | TartibEngine: mk2 treats a dual غَيْرَانِ as definite; mf2 counts a jarr phrase as the object. |
| 28 | T-A08 | adab | 1 | AdabEngine.check("naibNotFail") reads a «فاعل» within three tokens of any passive verb, even when the line names another governor («فَاعِلٌ لِـ«X»»). |
| 29 | T-M04 | mansub | 1 | MansubEngine / the v332 veto picks the nearest noun as the head of an adjective after a comma; the clause-naʿt «تَدُلُّ …» between them hides the real head. |
| 30 | T-H03 | sh336 | 1 | Sh336 R209 / the clause seat: a clause after a manṣūb khabar of kāna is read as its naʿt. |

## 1. T-T02 — Taʿalluq — TaalluqEngine (163)

- **Asserts wrongly**: author: an explicit governor (verb, maṣdar, participle, elative, or the sense of a word — «لَفْظُ اللهِ لِمَا فِيهِ مِنْ مَعْنَى الْمَعْبُودِ», «مَا فِي كَأَنَّ مِنْ مَعْنَى التَّشْبِيهِ») / engine: another written word (the nearest noun, تَعَالَى, the verb of a neighbouring clause, a fronted object)
- **Where**: TaalluqEngine.of picks the main verb of the sentence or the nearest preceding word, ignoring a maṣdar / participle that the phrase completes, a governor AFTER a fronted phrase, a clause boundary (a comma, a new verb), and treating تَعَالَى and a subject noun as governors.
- **Reproduce (typed)**: `TaalluqEngine.of(rows, 4)` on «لَا يُحِبُّ اللهُ الْجَهْرَ بِالسُّوءِ» → `{"w": "بِالسُّوءِ", "kind": "found", "word": "يُحِبُّ", "alt": null}`
- **Reproduce (story sentence talkhis-al-miftah:29:s5:5, typed as written)**: «لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ.» → `TaalluqEngine.of(rows, 4)` = `مُتَعَلِّقٌ بِـ«يَكُنْ»`; the audit's verdict: مُتَعَلِّقٌ بِـ«يَكُنْ» — [object Object]
- **Correct, by the book**: مُتَعَلِّقٌ بِـ«الْجَهْرَ» — `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»; `izhar-al-asrar-matn-lithograph.txt` l.15 «ويجوز تقديم ما عدا هذا على متعلقه نحو بزيد مررت.»; `izhar-al-asrar-matn-lithograph.txt` l.52 «ومنه كل اسم فهم منه معنى الصفة نحو لفظة الله في قوله تعالى وهو الله في السموات أي المعبود فيها. ومنه اسم الإشارة وليت ولعل وحرف النداء والتشبيه والتنبيه والنفي وغيرها فإنها تعمل»
- **Narrowest gate**: Prefer the maṣdar / participle / elative the phrase completes (الْجَهْرَ بِالسُّوءِ، أَعْلَمُ بِالنَّحْوِ، أَحْرَصُ عَلَى) over the main verb; never bind to تَعَالَى, to a subject noun, or across a comma / a new verb; a fronted phrase binds to the verb AFTER it.
- **Same rule, agreeing**: TaalluqEngine agrees 643
- **Places** (first 6): al-kafiya:1:s12:8 إِلَى; al-kafiya:15:s8:11 بِالسُّوءِ; aqaid-ahl-al-sunna:2:s6:6 بِصِحَّةِ; aqaid-ahl-al-sunna:3:s2:2 بِجَمِيعِ; aqaid-ahl-al-sunna:3:s4:6 بِذَاتِهِ; aqaid-ahl-al-sunna:4:s1:6 إِلَى

## 2. T-C-tanwin — Case ending and role — DabtEngine (106)

- **Asserts wrongly**: same case, wrong tanwīn: the engine adds tanwīn to an annexed noun (شَهَادَةُ أَنْ …، عَذَابُ الْحَرِيقِ، نُورُ الدِّينِ), to a name before «ابْن» (زَيْدِ بْنِ، قَيْسُ بْنُ), or drops it from a fully declined plural (أَسْمَاءٌ)
- **Where**: DabtEngine does not see annexation to a following maṣdar clause (أَنْ …), to a proper noun after ابن, or to a definite second term across a line break.
- **Reproduce (story sentence marah-al-arwah:24:s7:2, typed as written)**: «أَيْ حُرُوفُ هَوِيتُ السِّمَانَ.» → `DabtEngine.decide(rows).out[1]` = `{"out": null, "rule": "mubtada", "k": "raf"}`; the audit's verdict: «حُرُوفٌ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ»
- **Narrowest gate**: DabtEngine: no tanwīn on a noun whose next token begins an annexation it can see — a definite noun or name (نُورُ الدِّينِ), the name after which «ابن / بنت» stands between two names (قَيْسُ بْنُ)، a maṣdar clause opened by أَنْ (شَهَادَةُ أَنْ). أَسْمَاءٌ (lemma اسْم) is not a diptote. Gate on the written word lacking tanwīn AND the authored line saying «مُضَافٌ».
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): fail 3,565 hits / 15 here, jarr 9,370 hits / 15 here, maful 3,534 hits / 13 here, mubtada 3,382 hits / 12 here, khabar 3,071 hits / 12 here, mudafIlayh 6,918 hits / 11 here
- **Places** (first 6): adam-wa-iblis:1:s2:5 كُلِّهَا; al-ghazali-wa-al-uzla:3:s2:1 فَبَيْنَمَا; al-kafiya:19:s12:14 فَاعِلُ; al-kafiya:23:s5:12 الْأَوْجُهِ; al-maqamat-birgivi:2:s3:3 أَالْإِيمَانُ; al-maqamat-birgivi:2:s36:7 وَعَاقِبَةِ

## 3. T-C-mood — Case ending and role — DabtEngine (87)

- **Asserts wrongly**: engine: the wrong mood on a muḍāriʿ — naṣb after a coordinated / fresh verb, rafʿ after لَنْ / أَنْ, rafʿ on a jussive answer of a condition or a request, naṣb after لَامُ الْأَمْرِ
- **Where**: DabtEngine mood rules: a verb joined by و / ف to an earlier manṣūb verb inherits naṣb across a clause; the jāzim of a condition is not seen through مَنْ / مَهْمَا; لِ is read as lām kay before a jussive (وَلْنَسْكُتْ).
- **Reproduce (story sentence talkhis-al-miftah:65:s5:2, typed as written)**: «أَوْ يَظْهَرَ لَهَا عِلَّةٌ غَيْرُ الْمَذْكُورَةِ.» → `DabtEngine.decide(rows).out[1]` = `{"out": null, "rule": "raf", "k": "raf"}`; the audit's verdict: «يَظْهَرُ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.185 «العَاشِرُ المُضَارِعُ إِذَا تَجَرَّدَ مِنْ نَاصِبٍ وَجَازِمٍ.»; `shudhur-al-dhahab-src.txt` l.256 «وَالمضَارِعُ بَعْدَ نَاصِبٍ، وَهُوَ «لَنْ» أَوْ «كَي» المَصْدَرِيَّةُ مُطْلَقًا، و«إِذَنْ» إِنْ صُدِّرَتْ …»; `shudhur-al-dhahab-src.txt` l.284 «بَابٌ– الْمَجْزُومَاتُ الأَفْعَالُ الْمُضَارِعَةُ الدَّاخِلُ عَلَيْهَا جَازِمٌ، وَهُوَ ضَرْبَانِ: جازِمٌ لِفِعْلٍ، وَهُوَ: لَمْ، وَلَمَّا، وَلَامُ الأَمْرِ، وَلَا في النَّهْيِ»
- **Narrowest gate**: DabtEngine mood: (a) a muḍāriʿ joined by و / ف after a full stop / comma, or after a manṣūb verb of ANOTHER clause, keeps rafʿ unless the authored line says «مَعْطُوفٌ عَلَى»; (b) لِ before a jussive written with sukūn is lām al-amr (وَلْنَسْكُتْ)، not lām kay; (c) the jāzim of a condition reaches through مَنْ / مَا / مَهْمَا to the condition verb. Gate on the written ending agreeing with the authored mood.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): raf 5,170 hits / 45 here, nasbVerb 831 hits / 21 here, jazm 611 hits / 11 here, shart 165 hits / 10 here
- **Places** (first 6): al-kafiya:16:s6:9 يَأْخُذْ; al-maqamat-birgivi:2:s42:10 نَزِدْ; al-maqamat-birgivi:4:s5:24 تَجِدَ; al-maqamat-birgivi:12:s5:20 يَعْلَمْهُ; al-usul-al-munifa:2:s3:2 يَتَفَقَّهَ; al-usul-al-munifa:2:s10:28 يَكُفَّ

## 4. T-T01 — Taʿalluq — TaalluqEngine (77)

- **Asserts wrongly**: author: «مُتَعَلِّقٌ بِمَحْذُوفٍ» (khabar / naʿt / ḥāl / khabar kāna — a ẓarf mustaqarr) / engine: a written word nearby (the head noun, the subject, or a verb of the next clause)
- **Where**: TaalluqEngine.of returns kind:"found" with the nearest preceding noun / verb when a mustaqarr reading (khabar of a nāsikh or of a mubtadaʾ with no other khabar, naʿt of an indefinite, ḥāl of a definite) is available.
- **Reproduce (typed)**: `TaalluqEngine.of(rows, 2)` on «وَكَانَ إِبْلِيسُ مَعَهُمْ» → `{"w": "مَعَهُمْ", "kind": "found", "word": "إِبْلِيسُ", "alt": null}`
- **Reproduce (story sentence siyar-ibn-al-mubarak:2:s4:3, typed as written)**: «قَالُوا: عَالِمٌ مِنْ أَهْلِ خُرَاسَانَ قَدِمَ.» → `TaalluqEngine.of(rows, 2)` = `مُتَعَلِّقٌ بِـ«عَالِمٌ»`; the audit's verdict: مُتَعَلِّقٌ بِـ«عَالِمٌ»
- **Correct, by the book**: مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ — `izhar-al-asrar-matn-lithograph.txt` l.15 «ومجرور ما عدا هذه السبعة منصوب المحل على أنه مفعول فيه لمتعلقه … وقد يحذف المتعلق، فإن كان المحذوف فعلا عاما متضمنا في الجار والمجرور يسميان ظرفا مستقرا نحو زيد في الدار أي»; `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»
- **Narrowest gate**: TaalluqEngine.of: before binding to a written word, test the mustaqarr seats in order — khabar of an open nāsikh with no other khabar (كَانَ إِبْلِيسُ مَعَهُمْ)، khabar of lā of the genus (لَا شَكَّ فِيهَا)، naʿt of an indefinite right before (رَجُلٌ مِنَ …)، ḥāl of a definite. Return kind:"mahdhuf" with the seat. Agree total 643 (no per-seat tally exists — keep the v328 smoke list green).
- **Same rule, agreeing**: TaalluqEngine agrees 643 (silent 217) over the shelf
- **Places** (first 6): adam-wa-iblis:1:s4:3 مَعَهُمْ; al-asad-wa-al-arnab:3:s2:9 فِيهَا; al-bukhari-fi-baghdad:4:s1:12 فِيهَا; aqaid-ahl-al-sunna:26:s1:5 كَالْعِلْمِ; aqaid-ahl-al-sunna:27:s2:7 كَالْعِلْمِ; aqaid-ahl-al-sunna:28:s2:12 كَالْجَوْهَرِ

## 5. T-J03 — Clause maḥall — JumlaMahallEngine (72)

- **Asserts wrongly**: OFFERED: the engine offers naʿt-or-ḥāl / naʿt-or-khabar / ḥāl-or-istiʾnāf, and neither reading is the seat an open frame gives the clause — the author names that frame: khabar of kāna / inna / a mubtadaʾ, the answer of إِذَا / لَمَّا / a condition, the ṣila of مَنْ / مَا / الَّذِي, the maqūl after قَالَ, the request's answer (قِفِي نَسْأَلْكِ), ʿaṭf on the previous clause
- **Where**: JumlaMahallEngine.of: `claimed()` gates only the EXACT naʿt; the offered branches (naatOrHal, naatOrKhabar, halOrNaat, hal, naatOffered's first reading) still fire inside an open nāsikh, mubtadaʾ, condition / إِذَا / لَمَّا, relative, قَالَ, or after و joining two verbs.
- **Reproduce (typed)**: `JumlaMahallEngine.line(rows, 2)` on «كُنْتُ قَدَمًا هَوِيتُ السِّمَانَا» → `{"w": "هَوِيتُ", "mahall": "nasb", "seat": "naat", "rule": "naatOrHal", "certainty": "offered", "line": {"ar": "وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«قَدَمًا»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ (النَّكِرَةُ غَيْرُ مَحْضَةٍ)", "en": "two readings: a NAʿT of «قَدَمًا» (naṣb), or a ḤĀL (naṣb) — the indefinite is not a pure one", "tr": "iki vecih: «قَدَمًا» isminin NA'TI (nasb), ya da HÂL (nasb) — nekre mahz değil"}}`
- **Reproduce (story sentence marah-al-arwah:24:s7:3, typed as written)**: «أَيْ حُرُوفُ هَوِيتُ السِّمَانَ.» → `JumlaMahallEngine.line(rows, 2).ar` = `وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«حُرُوفُ»، أَوْ فِي مَحَلِّ رَفْعٍ خَبَرٌ`; the audit's verdict: وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«حُرُوفُ»، أَوْ فِي مَحَلِّ رَفْعٍ خَبَرٌ
- **Correct, by the book**: none offered inside an open kāna (the author: خَبَرُ كَانَ) — `qawaid-al-irab-ibn-hisham-matn.txt` l.49 «إحداها واقعةٌ خبرًا، وموضعها رفعٌ في بابي المبتدأ، وإن نحو: زيدٌ قام أبوه، وإن زيدًا أبوه قائمٌ، ونصبٌ، وموضعها نصبٌ في بابي كان وكاد، نحو: إنهم كانوا يظلمون، وما كادوا يفعلون.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.53 «والمفعوليةُ تقع في أربعة مواضع، محكيةً بالقول نحو: قال: إني عبد الله …»; `qawaid-al-irab-ibn-hisham-matn.txt` l.59 «وكلُ جملةٍ وقعت بعد إذ، أو إذا، أو حيثُ، أو لما الوجودية، عند من قال باسميتها، أو بينما، أو بين؛ فهي في موضع ظرفٍ بإضافتهن إليها.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.67 «فأما نحو: إن قام أخوك قامَ عمرٌو.»; `qawaid-al-irab-ibn-hisham-matn.txt` l.124 «الثانيةً الواقعةَ صلةً لاسمٍ، نحو: جاء الَّذي قام أبوه …»
- **Narrowest gate**: JumlaMahallEngine: apply `claimed()` to the OFFERED branches too — inside an open nāsikh (its khabar still owed), a mubtadaʾ with no khabar, a condition / إِذَا / لَمَّا frame, a relative, قَالَ, or after و joining a verb, offer nothing (silent) rather than naʿt-or-ḥāl. Agreeing: naʿt 260, khabar 624, ḥāl 46 — the exact rules are unchanged.
- **Same rule, agreeing**: JumlaMahallEngine.audit bySeat agree: khabar 624, naʿt 260, ḥāl 46, ṣila 164, maqūl 116
- **Places** (first 6): abu-hanifa-wa-al-safina:1:s1:9 نَحْكِيهِ; abu-hanifa-wa-al-safina:4:s5:8 كَانَ; al-kafiya:1:s13:13 كَقَامَ; al-kafiya:4:s5:7 جَازَ; al-kafiya:4:s11:30 يَجْعَلُهُ; al-kafiya:8:s7:8 يَجُوزُ

## 6. T-C-built — Case ending and role — DabtEngine (65)

- **Asserts wrongly**: engine: rewrites a BUILT word's ending — the person of a māḍī (نَزَلْتِ → نَزَلْتُ، عُنِيتُ → عُنِيَتْ), an amr's pronoun vowel (فَأَلْقِهْ), the mīm of a plural pronoun (مِنْكُمُ)
- **Where**: DabtEngine cell rule re-derives the māḍī's person / the amr form from the paradigm and overwrites the written suffix (it should only fill a missing vowel).
- **Reproduce (story sentence muallaqat-imri-al-qays:1:s1:6, typed as written)**: «فَبَلَغَهُ مَقْتَلُ أَبِيهِ وَهُوَ بِدَمُّونَ، فَقَالَ:» → `DabtEngine.decide(rows).out[5]` = `{"out": null, "rule": "mazi", "k": "cell"}`; the audit's verdict: «فَقَالَا»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.71 «أو الفَتْحِ، وَهُوَ سَبْعَةٌ: الماضي المجرَّدُ كضَرَبَ وضرَبكَ وضَرَبَا،»; `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»
- **Narrowest gate**: The cell rule must not overwrite a built word's written suffix: when the written māḍī carries ـتِ / ـتُ / ـتَ / ـنَ / ـا, keep it (the paradigm only fills a MISSING vowel). Same for the amr's pronoun vowel and the plural mīm's helping ḍamma (مِنْكُمُ) in verse.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): mazi 9,231 hits / 46 here, amr 718 hits / 11 here, jarrPron 2,006 hits / 3 here, mabni 23,621 hits / 3 here, amr-waw 92 hits / 1 here, jazm 611 hits / 1 here
- **Places** (first 6): al-ghazali-wa-al-uzla:1:s4:5 يَطْمَئِنُّ; al-maqamat-birgivi:6:s16:13 أَقْبَلْ; al-maqamat-birgivi:8:s2:6 وَتَرْكُ; al-usul-al-munifa:23:s6:16 أَخَافُ; al-usul-al-munifa:24:s7:67 وَأَخَافُ; al-usul-al-munifa:25:s4:20 أَخَافُ

## 7. T-C-maful — Case ending and role — DabtEngine (62)

- **Asserts wrongly**: engine: «مَفْعُولٌ بِهِ» (naṣb) on a word the text writes and the author parses in another case — a muḍāf ilayh (عَبْدِ اللهِ، الْأَصْنَافِ), a doer (السُّنَّةُ، رَجُلٌ), a jarr follower
- **Where**: DabtEngine.decide gives the maful office to a noun after a transitive verb even when the noun is annexed to the word before it (a construct chain) or is itself the verb's doer.
- **Reproduce (story sentence marah-al-arwah:13:s6:4, typed as written)**: «فَلَا يُقَالُ مَرَرْتُ زَيْدٍ بِ بَلْ يُقَالُ مَرَرْتُ بِزَيْدٍ.» → `DabtEngine.decide(rows).out[3]` = `{"out": null, "rule": "maful", "k": "nasb"}`; the audit's verdict: «زَيْدًا»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»; `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.131 «بَابٌ– الْمَرْفُوعَاتُ عَشَرَةٌ: أحَدُهَا الْفَاعِلُ، وَهُوَ: مَا قُدِّمَ الْفِعْلُ أوْ شِبْهُهُ عَلَيْهِ وَأُسْنِدَ إلَيْهِ»
- **Narrowest gate**: The maful office only for a noun with no muḍāf before it: if the previous token is a noun written without tanwīn and the authored line says «مُضَافٌ إِلَيْهِ», stop. maful agrees 3,534 times — the gate is the construct test.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): maful 3,534 hits / 62 here
- **Places** (first 6): al-bukhari-fi-baghdad:2:s2:5 رَجُلٌ; al-maqamat-birgivi:2:s2:16 خَيْرِهِ; al-maqamat-birgivi:8:s3:22 أَمْرِهِ; al-usul-al-munifa:2:s18:12 السُّنَّةُ; al-usul-al-munifa:3:s13:27 خَيْرِهِ; al-usul-al-munifa:3:s20:20 غَالِبٍ

## 8. T-C-follower — Case ending and role — DabtEngine (57)

- **Asserts wrongly**: engine: naʿt / ʿaṭf / badal / tawkīd copying the case of a head it chose, against the written case the author explains (an object, a muḍāf ilayh, a fresh mubtadaʾ)
- **Where**: DabtEngine: the follower rule picks the nearest earlier noun as the head (usually a majrūr) across a verb or a comma.
- **Reproduce (story sentence tasrif-al-izzi:17:s29:3, typed as written)**: «وَذَاكَ مَرْئِيٌّ كَمَرْعِيٍّ.» → `DabtEngine.decide(rows).out[2]` = `{"out": null, "rule": "nat", "k": "raf"}`; the audit's verdict: «كَمَرْعِيٌّ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»
- **Narrowest gate**: Follower head: the nearest earlier noun only within the same clause (no verb, no comma, no «فِي حَالِ» between); a word the authored line names «مَفْعُولٌ بِهِ» / «تَوْكِيدٌ … مَنْصُوبٌ» is not re-headed. nat agrees 2,522, atf 3,932, tawkid 80.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): nat 2,522 hits / 36 here, atf 3,932 hits / 11 here, badal 519 hits / 8 here, tawkid 80 hits / 2 here
- **Places** (first 6): abu-hanifa-wa-al-safina:1:s2:5 أَهْلِ; al-bukhari-fi-baghdad:1:s2:4 أَهْلِ; al-kafiya:10:s7:18 مُفْرَدٌ; al-kafiya:38:s2:21 الْمُتَّصِلَةَ; al-kafiya:44:s5:29 ضَعِيفٌ; al-maqamat-birgivi:2:s26:9 وَاللِّبَاسِ

## 9. T-C-verse — Case ending and role — DabtEngine (56)

- **Asserts wrongly**: engine: overrides a verse licence the author names in the line (the rhyme's kasra on a jussive, a sukūn for the metre, alif al-iṭlāq, a ḍamma kept for the metre)
- **Where**: DabtEngine's rhyme forgiveness covers only the last word of a marked hemistich; a licence named inside the line (mid-verse) is not read.
- **Reproduce (story sentence talkhis-al-miftah:68:s18:5, typed as written)**: «يَمُدُّونَ مِنْ أَيْدٍ عَوَاصٍ عَوَاصِمِ» → `DabtEngine.decide(rows).out[4]` = `{"out": null, "rule": "nat", "k": "jarr"}`; the audit's verdict: «عَوَاصِمَ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Narrowest gate**: Extend the rhyme / ḍarūra forgiveness to any token whose line names the licence («لِلرَّوِيِّ»، «لِلْقَافِيَةِ»، «ضَرُورَةً»، «لِلْوَزْنِ»، «لِلْإِطْلَاقِ»), not only the last word of a marked hemistich.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): maful 3,534 hits / 10 here, hal 736 hits / 7 here, mudafIlayh 6,918 hits / 6 here, mazi 9,231 hits / 6 here, nat 2,522 hits / 6 here, raf 5,170 hits / 4 here
- **Places** (first 6): bad-al-amali:3:s13:9 الْأَهَالِ; bad-al-amali:8:s37:9 تُبَالِ; bad-al-amali:10:s50:10 قَالِ; muallaqat-al-harith:11:s2:3 وَالتَّعَاشِي; muallaqat-amr-ibn-kulthum:2:s7:4 بِبَعْلَبَكٍّ; muallaqat-amr-ibn-kulthum:2:s7:8 وَقَاصِرِينَا

## 10. T-S02 — Sign of the case — SignEngine (43)

- **Asserts wrongly**: author: alif / wāw / yāʾ on a dual, its ilḥāq (اثْنَا), a sound masculine plural or a five-noun / engine: the vowel (class «sahih; sound» or «maqṣūr annexed»)
- **Where**: SignEngine.classify returns «sahih; sound» (or maqsur / manqus / mabni-harf) for a word whose authored line names a letter sign and whose surface ends ـَانِ/ـَا (annexed) /ـَيْنِ/ـَيْ/ـُونَ/ـِينَ: the dual / plural is recognised only when tagged.
- **Reproduce (story sentence marah-al-arwah:13:s12:3, typed as written)**: «فَبَقِيَ لَكَ اثْنَا عَشَرَ نَوْعًا.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "sahih", "why": "sound", "sign": "damma", "authored": "alif", "opts": {"pos": "noun", "lemma": "اِثْنَانِ", "tags": ["fail", "al-muthanna"]}}`; the audit's verdict: sign «damma» (sahih; sound)
- **Correct, by the book**: yāʾ / alif / wāw as authored — `shudhur-al-dhahab-src.txt` l.39 «الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَفْتُوحِ مَا قَبْلَهَا الْمَكْسُورِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.41 «وَأُلْحِقَ بِهِ اثْنَانِ، وَاثْنَتَانِ، وَثِنْتَانِ مُطْلَقًا، وَكِلَا وَكِلْتَا مُضَافَيْنِ إِلَى مُضْمَرٍ.»; `shudhur-al-dhahab-src.txt` l.43 «الْخَامِسُ: جَمْعُ الْمُذَكَّرِ السَّالِمُ، كَالزَّيْدُونَ وَالْمُسْلِمُونَ، فَإِنَّهُ يُرْفَعُ بِالْوَاوِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ الْمَكْسُورِ مَا قَبْلَهَا الْمَفْتُوحِ مَا بَعْدَهَا.»; `shudhur-al-dhahab-src.txt` l.34 «الثَّالِثُ: «ذُو» بِمَعْنَى صَاحِبٍ، وَمَا أُضِيفَ لِغَيْرِ الْيَاءِ مِنْ «أَبٍ» «وَأَخٍ» «وَحَمٍ» «وَهَنٍ» «وَفَمٍ» بِغَيْرِ مِيمٍ، فَإِنَّهَا تُعْرَبُ بِالْوَاوِ وَالْأَلِفِ وَالْيَاءِ.»
- **Narrowest gate**: In SignEngine.classify, before falling to «sahih», test the authored token's TAGS / lemma for number: a lemma اِثْنَانِ / اِثْنَتَانِ, a tag al-muthanna / jam-mudhakkar, or a lemma that differs from the surface by ـَانِ / ـَيْنِ / ـُونَ / ـِينَ (يَد → يَدَيْهِ). Gate only on the class «sahih; sound» with an authored LETTER sign (alif / yāʾ / wāw), so the 24,261 sound verdicts that agree are untouched.
- **Same rule, agreeing**: SignEngine.audit byClass: sahih 24,261 / 24,328; muthanna 612 / 624; jamMudhakkar 773 / 779; khamsa 332 / 332
- **Places** (first 6): al-kafiya:16:s10:8 وَالزَّيْدُونَ; al-kafiya:18:s5:19 حَسَنَا; al-kafiya:18:s5:23 وَالزَّيْدُونَ; izhar-al-asrar:8:s6:11 الزَّيْدُونَ; izhar-al-asrar:25:s2:16 وَالزَّيْدُونَ; izhar-al-asrar:28:s3:16 الزَّيْدُونَ

## 11. T-C-letters — Case ending and role — DabtEngine (37)

- **Asserts wrongly**: engine: a vowel (or tanwīn) on a dual, a sound plural, a five-noun or a five-verb whose sign the author names as a letter (ضَالَّتَانٌ، حَيَّيْنَ، بَنُونٌ، يَغُرُّوكُمْ)
- **Where**: DabtEngine re-vowels the nūn of a dual / plural and the end of a five-verb.
- **Reproduce (story sentence tasrif-al-izzi:15:s32:3, typed as written)**: «وَارْضَ ارْضَيَا ارْضَوْا، ارْضَيْ ارْضَيَا ارْضَيْنَ.» → `DabtEngine.decide(rows).out[2]` = `{"out": null, "rule": "amr", "k": "cell"}`; the audit's verdict: «ارْضَوُا»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.39 «الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَيُجَرُّ وَيُنْصَبُ بِالْيَاءِ …»; `shudhur-al-dhahab-src.txt` l.48 «السَّادِسُ: يَفْعَلَانِ وَتَفْعَلَانِ وَيَفْعَلُونَ وَتَفْعَلُونَ وَتَفْعَلِينَ، فَإِنَّهَا تُرْفَعُ بِثُبُوتِ النُّونِ، وَتُنْصَبُ وَتُجْزَمُ بِحَذْفِهَا.»
- **Narrowest gate**: Duals, sound plurals, five nouns and five verbs: do not re-vowel the nūn or add tanwīn; follow the line's «بِالْأَلِفِ / بِالْيَاءِ / بِالْوَاوِ / بِحَذْفِ النُّونِ».
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): maful 3,534 hits / 5 here, tawkid 80 hits / 4 here, mazi 9,231 hits / 3 here, raf 5,170 hits / 3 here, atf 3,932 hits / 3 here, jarr 9,370 hits / 3 here
- **Places** (first 6): al-usul-al-munifa:2:s25:18 بَنُو; al-usul-al-munifa:14:s13:30 يَزَالُونَ; al-usul-al-munifa:24:s15:54 ضَالَّتَانِ; bad-al-amali:5:s22:5 ذُو; ibn-battuta-yakhruju-min-tanja:1:s4:3 حَيَّيْنِ; marah-al-arwah:46:s1:5 مُدَّانِّ

## 12. T-C-raf — Case ending and role — DabtEngine (36)

- **Asserts wrongly**: engine: rafʿ (fāʿil / mubtadaʾ / khabar / nāʾib / ism kāna) on a word the text writes and the author parses as manṣūb or majrūr (an object, a ḥāl, a muḍāf ilayh: صَلَاحِ الدِّينِ، نُورِ الدِّينِ)
- **Where**: DabtEngine gives the doer / mubtadaʾ office to the second half of a laqab (… الدِّين) and to an object after a passive-looking verb.
- **Reproduce (story sentence marj-dabiq:5:s2:3, typed as written)**: «ثُمَّ قُتِلَ طُومَانَ بَايُ.» → `DabtEngine.decide(rows).out[2]` = `{"out": null, "rule": "naib", "k": "raf"}`; the audit's verdict: «طُومَانُ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.131 «بَابٌ– الْمَرْفُوعَاتُ عَشَرَةٌ: أحَدُهَا الْفَاعِلُ، وَهُوَ: مَا قُدِّمَ الْفِعْلُ أوْ شِبْهُهُ عَلَيْهِ وَأُسْنِدَ إلَيْهِ»; `shudhur-al-dhahab-src.txt` l.147 «الثَّالِثُ الْمُبْتَدَأُ، وَهُوَ: الْمُجَرَّدُ عَنِ الْعَوَامِلِ اللَّفْظِيَّةِ: مُخْبَرًا عَنْهُ، أَوْ وَصْفًا رَافِعًا لِمُكْتَفًى بِهِ»; `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»
- **Narrowest gate**: The second word of a compound laqab (صَلَاحُ الدِّينِ، نُورُ الدِّينِ، طُومَانْ بَايْ) is a muḍāf ilayh or the second half of a murakkab, never a doer; gate on the authored line saying «مُضَافٌ إِلَيْهِ» / «مُرَكَّبٌ».
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): naib 560 hits / 9 here, mubtada 3,382 hits / 9 here, khabar 3,071 hits / 8 here, fail 3,565 hits / 7 here, kanaIsm 968 hits / 3 here
- **Places** (first 6): al-kafiya:39:s1:15 زَائِدَةً; al-usul-al-munifa:12:s3:4 ثَوْبَانُ; al-usul-al-munifa:12:s3:29 الرِّزْقَ; al-usul-al-munifa:14:s11:9 كُلَّ; al-usul-al-munifa:28:s6:26 عَذَابَ; alb-arslan-wa-malazgird:4:s1:2 فِيمَنْ

## 13. T-C-jarr — Case ending and role — DabtEngine (35)

- **Asserts wrongly**: engine: jarr (muḍāf ilayh / after a jarr letter) on a word the text writes and the author parses as manṣūb or marfūʿ, or naṣb on a written majrūr after a preposition
- **Where**: DabtEngine treats a noun after a maṣdar / a participle as its muḍāf ilayh, and drops the jarr after a preposition before a diptote-looking plural (أَشْهُرٍ).
- **Reproduce (story sentence marah-al-arwah:17:s19:3, typed as written)**: «وَهِيَ لَيْسَتْ بِأَسْمَاءٍ.» → `DabtEngine.decide(rows).out[2]` = `{"out": null, "rule": "jarr", "k": "jarr"}`; the audit's verdict: «بِأَسْمَاءَ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»; `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»
- **Narrowest gate**: Do not annex a noun to a preceding maṣdar / participle when that noun is written manṣūb and the line names an object (فَرَضَ … الْعَمَلَ); keep jarr after a preposition for a plural of the form أَفْعُل / أَفْعَال unless the lexicon marks the diptote. mudafIlayh agrees 6,918, jarr 9,370.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): mudafIlayh 6,918 hits / 22 here, jarr 9,370 hits / 13 here
- **Places** (first 6): al-kafiya:16:s11:12 الصَّلَاةَ; al-usul-al-munifa:2:s26:3 مَيْمُونِ; al-usul-al-munifa:14:s18:17 الْقَدَرِيَّةَ; al-usul-al-munifa:14:s35:20 الطَّاعَةَ; al-usul-al-munifa:14:s38:68 قَوْلَهُ; al-usul-al-munifa:18:s21:25 الْعَمَلَ

## 14. T-C-muqaddar — Case ending and role — DabtEngine (33)

- **Asserts wrongly**: engine: a shown vowel on a word whose case is estimated (الْيَمَانِي، الْمَاضِي، السَّاعِي، صَالِ، تَوَالِي، عَمِّي)
- **Where**: DabtEngine writes the case vowel on a final yāʾ of a manqūṣ in rafʿ / jarr.
- **Reproduce (story sentence muallaqat-al-harith:11:s7:6, typed as written)**: «أَعَلَيْنَا جُنَاحُ كِنْدَةَ أَنْ• يَغْنَمَ غَازِيهِمُ وَمِنَّا الْجَزَاءُ.» → `DabtEngine.decide(rows).out[5]` = `{"out": null, "rule": "maful", "k": "nasb"}`; the audit's verdict: «غَازِيَهُمْ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا»
- **Narrowest gate**: A manqūṣ in rafʿ / jarr (final yāʾ with no shown vowel, or the line says «مُقَدَّرَة») keeps the yāʾ bare; only naṣb shows.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): maful 3,534 hits / 6 here, jarr 9,370 hits / 4 here, mudafIlayh 6,918 hits / 4 here, nasbVerb 831 hits / 3 here, hal 736 hits / 3 here, khabar 3,071 hits / 2 here
- **Places** (first 6): al-maqamat-birgivi:4:s2:10 سُنَّتِي; al-maqamat-birgivi:8:s7:5 فَخْرِي; al-maqamat-birgivi:11:s2:10 بِأَذَى; al-usul-al-munifa:14:s20:51 صَالِ; al-usul-al-munifa:21:s6:7 بَعْدَمَا; al-usul-al-munifa:23:s4:36 وَيَرْجُو

## 15. T-T03 — Taʿalluq — TaalluqEngine (32)

- **Asserts wrongly**: author: an explicit verb / participle the phrase is fronted before or follows (يَغْفِرُ … لِمَنْ يَشَاءُ، بِهَا تَسْتَعِدُّ، بَعْدَ السَّفَاهَةِ يَحْلُمُ، كَانُوا لَنَا خَاشِعِينَ) / engine: «مُتَعَلِّقٌ بِمَحْذُوفٍ» (ḥāl, ṣifa, khabar, khabar kāna or inna)
- **Where**: TaalluqEngine asserts a mustaqarr seat (khabar of kāna / inna, ḥāl, ṣifa) for a phrase whose nāsikh already has a written khabar later in the clause, or which stands before its own verb.
- **Reproduce (typed)**: `TaalluqEngine.of(rows, 4)` on «وَيَغْفِرُ مَا دُونَ ذٰلِكَ لِمَنْ يَشَاءُ» → `{"w": "لِمَنْ", "kind": "mahdhuf", "alt": null}`
- **Reproduce (story sentence talkhis-al-miftah:6:s1:4, typed as written)**: «يَا هَامَانُ ابْنِ لِي صَرْحًا.» → `TaalluqEngine.of(rows, 3)` = `مُتَعَلِّقٌ بِمَحْذُوفٍ`; the audit's verdict: مُتَعَلِّقٌ بِمَحْذُوفٍ
- **Correct, by the book**: مُتَعَلِّقٌ بِـ«يَغْفِرُ» — `izhar-al-asrar-matn-lithograph.txt` l.16 «حصل، وإن لم يكن كذلك أو لم يحذف متعلقه يسميان ظرفا لغوا نحو زيد في الدار أكل ومررت بزيد.»; `izhar-al-asrar-matn-lithograph.txt` l.15 «ويجوز تقديم ما عدا هذا على متعلقه نحو بزيد مررت.»
- **Narrowest gate**: Do not return a mustaqarr seat (khabar of kāna / inna, ḥāl) when the nāsikh has a written khabar later in the clause (كَانُوا لَنَا خَاشِعِينَ، إِنَّ الْفَتَى بَعْدَ السَّفَاهَةِ يَحْلُمُ) or when an explicit verb follows the fronted phrase (بِهَا تَسْتَعِدُّ، لِمَنْ يَشَاءُ after يَغْفِرُ).
- **Same rule, agreeing**: TaalluqEngine agrees 643
- **Places** (first 6): aqaid-ahl-al-sunna:2:s2:3 لِلْخَلْقِ; aqaid-ahl-al-sunna:2:s4:4 بِهَا; aqaid-ahl-al-sunna:39:s1:11 لِمَنْ; bad-al-amali:11:s51:1 وَفِي; bad-al-amali:11:s51:3 عَنْ; bad-al-amali:14:s67:7 بِالْخَيْرِ

## 16. T-C-mamnu — Case ending and role — DabtEngine (31)

- **Asserts wrongly**: engine: kasra / tanwīn on a diptote the author declines with the fatḥa (جَهَنَّمَ، سَقَرَ، حِمْصَ، فَارِسَ، تِرْمِذَ، عَوْجَاءَ، أَشْأَمَ) or the opposite
- **Where**: DabtEngine lacks the diptote causes for place names / feminine names / afʿal adjectives the lexicon does not mark.
- **Reproduce (story sentence marj-dabiq:5:s2:4, typed as written)**: «ثُمَّ قُتِلَ طُومَانَ بَايُ.» → `DabtEngine.decide(rows).out[3]` = `{"out": null, "rule": "maful", "k": "nasb"}`; the audit's verdict: «بَايًا»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ»
- **Narrowest gate**: Read the lexicon / the authored line for the diptote cause (place names, feminine names, afʿal adjectives): if the line says «مَمْنُوعٌ مِنَ الصَّرْفِ», write the fatḥa in jarr and no tanwīn.
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): mudafIlayh 6,918 hits / 9 here, jarr 9,370 hits / 7 here, maful 3,534 hits / 6 here, naib 560 hits / 2 here, mubtada 3,382 hits / 2 here, fail 3,565 hits / 1 here
- **Places** (first 6): adam-wa-iblis:1:s2:4 الْأَشْيَاءِ; al-usul-al-munifa:14:s20:35 جَهَنَّمَ; al-usul-al-munifa:19:s7:33 جَهَنَّمَ; al-usul-al-munifa:24:s7:17 حِمْصَ; al-usul-al-munifa:30:s3:40 سَقَرَ; alb-arslan-wa-malazgird:1:s1:4 أَرْسَلَانُ

## 17. T-C-nasb — Case ending and role — DabtEngine (22)

- **Asserts wrongly**: engine: another naṣb office (ḥāl, tamyīz, ẓarf, khabar kāna, ism inna, ism lā) on a word the text writes in another case
- **Where**: DabtEngine: the ḥāl rule fires on an indefinite adjective that follows an indefinite majrūr noun (a naʿt).
- **Reproduce (story sentence muallaqat-al-harith:10:s6:4, typed as written)**: «وَأَتَيْنَاهُمُ بِتِسْعَةِ• أَمْلَاكٍ كِرَامٍ أَسْلَابُهُمْ أَغْلَاءُ.» → `DabtEngine.decide(rows).out[3]` = `{"out": null, "rule": "hal", "k": "nasb"}`; the audit's verdict: «كِرَامًا»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.188 «بابٌ، الْمَنْصُوبَاتُ خَمْسَةَ عَشَرَ: أَحَدُها الْمفْعُولُ بِهِ، وَهُوَ: مَا وقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ، كـ«ضَرَبْتُ زَيْدًا».»; `shudhur-al-dhahab-src.txt` l.274 «الثَّاني الْمَجْرُورُ بِالإِضَافَةِ كـ«غُلَام زَيْدٍ» وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا»
- **Narrowest gate**: The ḥāl rule must not fire on an indefinite adjective right after an indefinite majrūr noun of its own case (a naʿt); zarf must not add tanwīn to an annexed ẓarf (يَوْمَ لَا …).
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): hal 736 hits / 8 here, zarf 1,612 hits / 5 here, kanaKhabar 839 hits / 4 here, laJins 91 hits / 2 here, innaIsm 680 hits / 2 here, tamyiz 155 hits / 1 here
- **Places** (first 6): al-maqamat-birgivi:3:s3:10 مُكَلَّفٍ; al-usul-al-munifa:19:s2:23 قَبْلِ; al-usul-al-munifa:25:s15:51 بِوَاحِدَةٍ; al-usul-al-munifa:27:s2:50 مَقْطُوعَةٍ; marah-al-arwah:28:s2:6 أَصْلَ; marah-al-arwah:39:s4:10 يَافِعٍ

## 18. T-C-hikaya — Case ending and role — DabtEngine (22)

- **Asserts wrongly**: engine: a case ending on a QUOTED word (لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ: تَفَعَّلَ، اسْتَفْعَلَ، أَلْ، خُذْ، اِيدَدْ)
- **Where**: DabtEngine assigns the seat's vowel to a token the author tags محكي; it should skip tokens with that tag.
- **Reproduce (story sentence tasrif-al-izzi:17:s21:2, typed as written)**: «وَالْأَمْرُ: اِيوِ.» → `DabtEngine.decide(rows).out[1]` = `{"out": null, "rule": "khabar", "k": "raf"}`; the audit's verdict: «اِيوٌ»
- **Correct, by the book**: the ending the authored line states (the written vowel) — `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»
- **Narrowest gate**: Skip any token whose authored line says «مَحْكِيٌّ» / «قُصِدَ لَفْظُهُ» (hikaya agrees 283 times by that same test elsewhere).
- **Same rules, agreeing** (DabtEngine.corpus('endings'), hits by rule): fail 3,565 hits / 4 here, mubtada 3,382 hits / 3 here, khabar 3,071 hits / 3 here, jarr 9,370 hits / 3 here, mudafIlayh 6,918 hits / 2 here, raf 5,170 hits / 2 here
- **Places** (first 6): shudhur-al-dhahab:1:s5:14 هَاتِ; shudhur-al-dhahab:4:s1:16 أَلْ; talkhis-al-miftah:55:s6:5 مِثْلِ; tasrif-al-izzi:3:s6:13 تَفَعَّلَ; tasrif-al-izzi:3:s11:9 اسْتَفْعَلَ; tasrif-al-izzi:6:s1:18 أَنَيْتَ

## 19. T-I01 — إِنَّ / أَنَّ — InnaEngine (21)

- **Asserts wrongly**: engine: kasr «in the ibtidāʾ / istiʾnāf / ʿaṭf» on a أَنَّ that opens a new sentence, follows a colon, or follows «غَيْرَ» / author: fatḥ — the maṣdar is the khabar (الْفَرْقُ …: أَنَّ …، وَمِنْهَا أَنَّ …، فَإِنَّهَا: أَنَّكَ …) or is joined by و to an earlier maṣdar (وَأَنَّا الْعَاصِمُونَ، وَأَنَّ اللهَ بَاقٍ) or follows غَيْرَ
- **Where**: InnaEngine reads «ibtidāʾ» from the token position (first in the sentence, after «:») and «istiʾnāf» after و, without asking whether an open frame (a mubtadaʾ awaiting its khabar, an earlier maṣdar أَنَّ with و, غَيْرَ, a verb owed its object) claims the clause.
- **Reproduce (story sentence qisas-al-nabiyyin-1:3:s33:1, typed as written)**: «وَأَنَّ اللهَ بَاقٍ لَا يَغِيبُ.» → `InnaEngine.table(sentence).inna` = `وَأَنَّ:kasr (ibtida)`; the audit's verdict: kasr (ibtida)
- **Correct, by the book**: fatḥ (the maṣdar continues the earlier أَنَّ / is the khabar) — `shudhur-al-dhahab-src.txt` l.179 «وتُكسَرُ «إِنَّ» في الابْتِدَاءِ، وَفي أَوَّلِ الصِّلَةِ وَالصِّفةِ والْجُملة الحاليَّة، وَالمُضَافِ إِلَيْهَا ما يخْتَصُّ بالجُمَلِ، والمَحْكيّةِ بالْقَوْل، وَجَوَابِ الْقسَم، والمُخْبَر بها عن اسم عَيْنٍ، وَقبْلَ اللَّامِ المُعلِّقةِ، … وتُفْتَحُ في الباقي.»
- **Narrowest gate**: InnaEngine: «ibtidāʾ» only when nothing earlier claims the clause: after «:» test whether the word before the colon is a mubtadaʾ / إِنَّ still owed its khabar (الْفَرْقُ: أَنَّ …)؛ a sentence opening with وَأَنَّ / وَأَنَّهُ joins the previous sentence's أَنَّ (prevTail) — extend prevTail across sentence ends in the same chapter. ibtida agrees 179 / 191, istinaf 20 / 25, atf 65 / 68.
- **Same rule, agreeing**: InnaEngine bySeat: ibtida 179 / 191, istinaf 20 / 25, atf 65 / 68
- **Places** (first 6): al-kafiya:17:s2:6 أَنَّ; al-kafiya:24:s9:2 أَنَّ; al-kafiya:43:s6:5 أَنَّ; al-usul-al-munifa:2:s14:6 أَنَّكَ; izhar-al-asrar:28:s2:15 أَنَّكَ; muallaqat-amr-ibn-kulthum:16:s1:1 وَأَنَّا

## 20. T-S03 — Sign of the case — SignEngine (13)

- **Asserts wrongly**: author: «حَذْفُ النُّونِ» on a five-verb of a weak-final lemma (يَغْزُوا، تَغْزِي، يَرْمِيَا، يَحُلُّوا، تَرَيَا، تَرَيْنَ، يَغُرُّوكُمْ) / engine: ḥadhf ḥarf al-ʿilla or sukūn
- **Where**: SignEngine.expect picks the weak-final rule from the LEMMA before checking the five-verb suffix (ـَا / ـُوا / ـِي with the nūn gone).
- **Reproduce (story sentence tasrif-al-izzi:15:s18:4, typed as written)**: «وَلَنْ يَغْزُوَ لَنْ يَغْزُوَا.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "mudariMutall", "why": "weak-final: the lemma ends in a weak letter", "sign": "fatha", "authored": "hadhfNun", "opts": {"pos": "verb", "lemma": "غَزَا", "tags": ["afal-khamsa", "naqis-verbs", "thulathi-mujarrad-babs"]}}`; the audit's verdict: sign «fatha» (mudariMutall; weak-final: the lemma ends in a weak letter)
- **Correct, by the book**: ḥadhf al-nūn — `shudhur-al-dhahab-src.txt` l.48 «السَّادِسُ: يَفْعَلَانِ وَتَفْعَلَانِ وَيَفْعَلُونَ وَتَفْعَلُونَ وَتَفْعَلِينَ، فَإِنَّهَا تُرْفَعُ بِثُبُوتِ النُّونِ، وَتُنْصَبُ وَتُجْزَمُ بِحَذْفِهَا.»
- **Narrowest gate**: In SignEngine.expect for cls mudariMutall: if the surface ends in the five-verb suffix with its nūn gone (ـَا، ـُوا، ـِي after the root) and the kase is naṣb / jazm, return hadhfNun before the weak-final rule. 852 of 866 mudariMutall verdicts agree — the gate is the suffix test, not the lemma.
- **Same rule, agreeing**: mudariMutall 852 / 866; khamsaVerbs 935 / 940
- **Places** (first 6): al-kafiya:22:s5:19 فَلْيُصَلُّوا; muallaqat-al-harith:8:s4:2 يَغُرُّوكُمُ; muallaqat-al-harith:13:s3:2 يُحِلُّوا; talkhis-al-miftah:50:s5:1 تَرَيَا; tasrif-al-izzi:10:s5:19 تَرَيِنَّ; tasrif-al-izzi:15:s15:4 يَغْزُوَا

## 21. T-S05 — Sign of the case — SignEngine (12)

- **Asserts wrongly**: author: a case vowel on a declinable noun (بَيْنَ، كُلَّمَا، أَيِّكُمْ، أَيَّتِهِمَا، هَمٍّ، هَمُّهُ، هَنٍ، جِنِّي، عَصًا، رَبِّي، وَاللهِ) / engine: «mahall» (reads it as a particle or a built word)
- **Where**: SignEngine.classify falls to «mabni; harf/mabni» on a homograph of a particle or pronoun (هم، هن، بين) or a word behind a fused jarr letter.
- **Reproduce (story sentence dawud-wa-jalut:4:s2:8, typed as written)**: «فَقَالَ دَاوُدُ: أَنْتَ تَثِقُ بِسَيْفِكَ، وَأَنَا أَثِقُ بِرَبِّي.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "mabni", "why": "harf", "sign": "mahall", "authored": "kasra", "opts": {"pos": "prep", "lemma": "بِ", "tags": ["ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil", "huruf-jarr"]}}`; the audit's verdict: sign «mahall» (mabni; harf)
- **Correct, by the book**: the authored vowel (kasra) — `shudhur-al-dhahab-src.txt` l.22 «الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُتَمَكِّنِ وَالْفِعْلِ الْمُضَارِعِ.»; `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ، نَحْوُ «بِأَفْضَلِكُمْ» «وَبِالْأَفْضَلِ».»; `shudhur-al-dhahab-src.txt` l.88 «… وَ«أيٌّ» الْمَوصُولَةُ إذا أضِيفَتْ وكانَ صَدْرُ صِلَتِهَا ضَمِيرًا مَحذُوفًا، نحو: ﴿أَيُّهُمْ أَشَدُّ﴾ [مريم ٦٩] وَبَعْضُهُمْ يُعْرِبُهَا مُطلَقًا.»
- **Narrowest gate**: The «mabni» class agrees 0 of 17 times in the corpus: drop it whenever the authored line names a case VOWEL (ḍamma / fatḥa / kasra, shown or estimated) — the class only fits a line that says «مَبْنِيٌّ … فِي مَحَلِّ». Narrowest: when pos is noun / propn, or the token's segments put a noun after a fused jarr letter (بِرَبِّي، بِعَصًا، وَاللهِ).
- **Same rule, agreeing**: mabni 0 / 17 (every «mabni» verdict on an authored case line is wrong)
- **Places** (first 6): dawud-wa-jalut:4:s1:7 بِعَصًا; dawud-wa-jalut:4:s2:8 بِرَبِّي; marah-al-arwah:6:s3:12 بِأَيِّكُمُ; marah-al-arwah:60:s3:17 بَيْنَ; marah-al-arwah:60:s3:18 بَيْنَ; marah-al-arwah:70:s1:3 جِنِّي

## 22. T-S07 — Sign of the case — SignEngine (10)

- **Asserts wrongly**: the class misread on a single word: مَعَانٍ (manqūṣ diptote, fatḥa estimated) read as sound; مُثَنَّاهَا (singular maqṣūr) read as dual; أَخَاهُ / أَبَاهُ (five nouns) read as dual; أَيَّمَا read as dual; قَنَاتَنَا (singular) and قُضَاتَهَا (broken plural) read as feminine plural; عَمْرٌو read as a plural; نَاصِرِينَ after the extra مِنْ; لَتُبْلَوُنَّ (thubūt al-nūn deleted)
- **Where**: SignEngine.classify: surface heuristics (ـَاتَ، ـَا، ـُو، ـِينَ) without the lexicon's number / lemma.
- **Reproduce (story sentence sibawayh-fi-al-basra:1:s2:2, typed as written)**: «وَاسْمُهُ عَمْرُو بْنُ عُثْمَانَ، وَسِيبَوَيْهِ لَقَبُهُ.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "jamMudhakkar", "why": "sound masculine plural, its nūn dropped", "sign": "waw", "authored": "damma", "opts": {"pos": "noun", "lemma": "عَمْرو", "tags": ["mubtada-khabar"]}}`; the audit's verdict: sign «waw» (jamMudhakkar; sound masculine plural, its nūn dropped)
- **Correct, by the book**: fatḥa / ḍamma as authored — `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا، وَالضَّمَّةُ وَالْفَتْحَةُ فِي نَحْوِ «يَخْشَى»، وَالضَّمَّةُ فِي نَحْوِ «يَدْعُو» «وَيَرْمِي».»; `shudhur-al-dhahab-src.txt` l.34 «الثَّالِثُ: «ذُو» بِمَعْنَى صَاحِبٍ، وَمَا أُضِيفَ لِغَيْرِ الْيَاءِ مِنْ «أَبٍ» «وَأَخٍ» «وَحَمٍ» «وَهَنٍ» «وَفَمٍ» بِغَيْرِ مِيمٍ، فَإِنَّهَا تُعْرَبُ بِالْوَاوِ وَالْأَلِفِ وَالْيَاءِ.»; `shudhur-al-dhahab-src.txt` l.32 «الثَّانِي: مَا جُمِعَ بِأَلِفٍ وَتَاءٍ مَزِيدَتَيْنِ، «كَهِنْدَاتٍ» فَإِنَّهُ يُنْصَبُ بِالْكَسْرَةِ نَحْوُ: «خَلَقَ اللهُ السَّمَاوَاتِ» «فَانْفِرُوا ثُبَاتٍ» بِخِلَافِ نَحْوِ: «وَكُنْتُمْ أَمْوَاتًا» «وَرَأَيْتُ قُضَاةً»، وَأُلْحِقَ بِهِ «أُولَاتُ».»
- **Narrowest gate**: Use the lexicon's lemma / plural before surface endings: a lemma ending ـَاة (قَنَاة) is singular; a broken plural (قُضَاة) is not jamMuannath; عَمْرو with its silent wāw is a name; أَيّ / سِيّ + مَا is not a dual. jamMuannath agrees 374 / 376, muthanna 612 / 624.
- **Same rule, agreeing**: jamMuannath 374 / 376; muthanna 612 / 624; jamMudhakkar 773 / 779
- **Places** (first 6): al-kafiya:20:s7:14 مَعَانٍ; al-kafiya:20:s8:16 وَمُثَنَّاهَا; ibn-khaldun-wa-timur:3:s3:11 قُضَاتَهَا; marah-al-arwah:54:s1:10 خَاهُ; marah-al-arwah:54:s1:13 بَاهُ; muallaqat-al-harith:6:s1:1 أَيَّمَا

## 23. T-S06 — Sign of the case — SignEngine (5)

- **Asserts wrongly**: diptote misjudged by the engine: author fatḥa on an unannexed diptote (لِلُقْمَانَ، بِقَارُونَ، أَجَشَّ، قَاصِرِينَا), kasra on one with «أَلْ» (كَالرَّحْمٰنِ) / engine: the opposite
- **Where**: SignEngine: a name in ـُونَ read as a plural; أَجَشَّ followed by an adjective read as annexed; الرَّحْمٰن treated as a diptote despite أَلْ.
- **Reproduce (story sentence luqman-wa-ibnuh:1:s4:2, typed as written)**: «وَكَانَ لِلُقْمَانَ ابْنٌ صَغِيرٌ يُحِبُّهُ، فَكَانَ يَعِظُهُ كُلَّ يَوْمٍ.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "sahih", "why": "sound", "sign": "kasra", "authored": "fatha", "opts": {"pos": "prep", "lemma": "لِ", "tags": ["huruf-jarr", "mamnu-min-sarf", "kana-wa-akhawatuha"]}}`; the audit's verdict: sign «kasra» (sahih; sound)
- **Correct, by the book**: fatḥa for an unannexed diptote without أَلْ; kasra with أَلْ — `shudhur-al-dhahab-src.txt` l.30 «أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» إِلَّا إِنْ أُضِيفَ أَوْ دَخَلَتْهُ أَلْ، نَحْوُ «بِأَفْضَلِكُمْ» «وَبِالْأَفْضَلِ».»
- **Narrowest gate**: Diptote: (a) a propn ending ـُونَ / ـَانَ with the tag mamnu-min-sarf is a diptote, not a plural (قَارُونَ، لُقْمَانَ); (b) «أَلْ» on the word itself (الرَّحْمٰن) declines it fully (S.30); (c) «annexed» only when the next token is a noun with no tanwīn AND not an adjective agreeing with the head (أَجَشَّ مُهَضَّمِ). mamnu agrees 1,475 of 1,476.
- **Same rule, agreeing**: mamnu 1,475 / 1,476; sahih 24,261 / 24,328
- **Places** (first 6): luqman-wa-ibnuh:1:s4:2 لِلُقْمَانَ; marah-al-arwah:43:s9:9 كَالرَّحْمٰنِ; muallaqat-amr-ibn-kulthum:2:s7:8 وَقَاصِرِينَا; muallaqat-antara:6:s4:9 أَجَشَّ; qarun-wa-kunuzuh:4:s2:4 بِقَارُونَ

## 24. T-I02 — إِنَّ / أَنَّ — InnaEngine (4)

- **Asserts wrongly**: engine: fatḥ on a received إِنَّ that opens a sentence or answers an oath (﴿إِنَّهُ مِنْ عِبَادِنَا﴾، ﴿إِنِّي أَخَافُ عَلَيْكُمْ﴾، «إِنَّ اللهَ أَرَادَ»، إِنَّنِي after the oath) / author: kasr
- **Where**: InnaEngine seats «riwāya», «khabar maʿnā» and «mafʿūl» reach past a full stop / a quoted verse into a new sentence.
- **Reproduce (story sentence muallaqat-tarafa:12:s5:4, typed as written)**: «وَقَرَّبْتُ بِالْقُرْبَى وَجَدِّكَ إِنَّنِي• مَتَى يَكُ أَمْرٌ لِلنَّكِيثَةِ أَشْهَدِ.» → `InnaEngine.table(sentence).inna` = `إِنَّنِي:fath (maful)`; the audit's verdict: fath (maful)
- **Correct, by the book**: kasr — `shudhur-al-dhahab-src.txt` l.179 «وتُكسَرُ «إِنَّ» في الابْتِدَاءِ، وَفي أَوَّلِ الصِّلَةِ وَالصِّفةِ والْجُملة الحاليَّة، وَالمُضَافِ إِلَيْهَا ما يخْتَصُّ بالجُمَلِ، والمَحْكيّةِ بالْقَوْل، وَجَوَابِ الْقسَم، والمُخْبَر بها عن اسم عَيْنٍ، وَقبْلَ اللَّامِ المُعلِّقةِ، … وتُفْتَحُ في الباقي.»
- **Narrowest gate**: riwaya / maful / khabarMana seats must stop at a full stop and at a Qurʾānic quotation boundary; an إِنَّ opening a sentence or answering an oath is kasr (S.179). riwaya 31 / 32, maful 173 / 175, khabarMana 10 / 11.
- **Same rule, agreeing**: riwaya 31 / 32, maful 173 / 175, khabarMana 10 / 11, qawl 105 / 107
- **Places** (first 6): al-usul-al-munifa:14:s15:33 إِنَّهُ; muallaqat-tarafa:12:s5:4 إِنَّنِي; qisas-al-nabiyyin-2:7:s7:17 إِنِّي; qisas-al-nabiyyin-2:30:s12:6 إِنَّ

## 25. T-S04 — Sign of the case — SignEngine (4)

- **Asserts wrongly**: author: fatḥa (shown or estimated) on a muḍāriʿ after أَنْ whose final alif is the verse's alif al-iṭlāq or a pronoun-carrying maqṣūr (نَدِينَا، يَكُونَا، تَلِينَا، تَرَاهُ) / engine: «five verbs, ḥadhf al-nūn»
- **Where**: SignEngine reads a final ـَا in a verse as the dual's alif; it ignores the rhyme (`rhyme` is passed) and the maqṣūr verb before a pronoun.
- **Reproduce (story sentence muallaqat-amr-ibn-kulthum:5:s3:9, typed as written)**: «وَأَيَّامٍ لَنَا غُرٍّ طِوَالٍ• عَصَيْنَا الْمَلْكَ فِيهَا أَنْ نَدِينَا.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "khamsaVerbs", "why": "five verbs", "sign": "hadhfNun", "authored": "fatha", "opts": {"pos": "verb", "lemma": "دَانَ", "tags": ["hollow-verbs"]}}`; the audit's verdict: sign «hadhfNun» (khamsaVerbs; five verbs)
- **Correct, by the book**: fatḥa (shown or estimated) — `shudhur-al-dhahab-src.txt` l.25 «وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْرَةِ، وَالْجَزْمِ بِالسُّكُونِ.»; `shudhur-al-dhahab-src.txt` l.54 «فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَّى مَقْصُورًا، وَالضَّمَّةُ وَالْكَسْرَةُ فِي نَحْوِ «الْقَاضِي» وَيُسَمَّى مَنْقُوصًا، وَالضَّمَّةُ وَالْفَتْحَةُ فِي نَحْوِ «يَخْشَى»، وَالضَّمَّةُ فِي نَحْوِ «يَدْعُو» «وَيَرْمِي».»
- **Narrowest gate**: In SignEngine.classify, a final ـَا on a muḍāriʿ at the rhyme (`rhyme` true, or the line names «الْأَلِفُ لِلْإِطْلَاقِ») or a maqṣūr verb before an attached pronoun (تَرَاهُ) is not the dual's alif: route to sahih / maqsur. khamsaVerbs agrees 935 of 940.
- **Same rule, agreeing**: khamsaVerbs 935 / 940; maqsur 863 / 870
- **Places** (first 6): izhar-al-asrar:19:s11:7 تَرَاهُ; muallaqat-amr-ibn-kulthum:5:s3:9 نَدِينَا; muallaqat-amr-ibn-kulthum:8:s2:10 يَكُونَا; muallaqat-amr-ibn-kulthum:9:s7:10 تَلِينَا

## 26. T-S14 — Sign of the case — SignEngine (2)

- **Asserts wrongly**: known engine gaps listed before: سِيَّمَا read as a dual; لَمَ الْقَهُمَا read as a built verb
- **Reproduce (story sentence muallaqat-imri-al-qays:3:s4:8, typed as written)**: «أَلَا رُبَّ يَوْمٍ لَكَ مِنْهُنَّ صَالِحٍ• وَلَا سِيَّمَا يَوْمٍ بِدَارَةِ جُلْجُلِ.» → `SignEngine.classify + expect (the token's tags)` = `{"cls": "muthanna", "why": "dual, its nūn dropped in annexation", "sign": "ya", "authored": "fatha", "opts": {"pos": "noun", "lemma": "سِيّ", "tags": ["la-nafiya-lil-jins", "idafa-definiteness", "anwa-ma", "hadhf-wa-taqdir"]}}`; the audit's verdict: sign «ya» (muthanna; dual, its nūn dropped in annexation)
- **Correct, by the book**: fatḥa (ism lā) — `shudhur-al-dhahab-src.txt` l.41 «وَأُلْحِقَ بِهِ اثْنَانِ، وَاثْنَتَانِ، وَثِنْتَانِ مُطْلَقًا، وَكِلَا وَكِلْتَا مُضَافَيْنِ إِلَى مُضْمَرٍ.»
- **Narrowest gate**: As T-S07 for سِيَّمَا (a dual only if the lemma is dual); «لَمَ الْقَهُمَا» waits on the hoca's reading of the printed text.
- **Same rule, agreeing**: muthanna 612 / 624
- **Places** (first 6): muallaqat-imri-al-qays:3:s4:8 سِيَّمَا; muallaqat-antara:12:s6:8 الْقَهُمَا

## 27. T-O01 — Order — TartibEngine (2)

- **Asserts wrongly**: «وَغَيْرَانِ الْمُكَوَّنُ» read as two definites (غَيْرَانِ is indefinite: the fronted khabar is free); «لَا يَجُوزُ فِي إِدْغَامِهِنَّ إِلَّا الْإِدْغَامُ» read as an object before the doer (the jarr phrase is no object)
- **Where**: TartibEngine: mk2 treats a dual غَيْرَانِ as definite; mf2 counts a jarr phrase as the object.
- **Reproduce**: no lab path for this engine; the corpus place bad-al-amali:10:s49:2 «الْمُكَوَّنُ» gives `order KM breaks mk2`
- **Correct, by the book**: no violation — `shudhur-al-dhahab-src.txt` l.147 «الثَّالِثُ الْمُبْتَدَأُ … مُخْبَرًا عَنْهُ»; `shudhur-al-dhahab-src.txt` l.131 «… أحَدُهَا الْفَاعِلُ»
- **Narrowest gate**: TartibEngine mk2: a dual / indefinite (غَيْرَانِ) is not definite; mf2: a jarr phrase is not the object. mk2 kept 155, mf2 kept 4.
- **Same rule, agreeing**: TartibEngine: mk2 kept 155 / violated 1; mf2 kept 4 / violated 1
- **Places** (first 6): bad-al-amali:10:s49:2 الْمُكَوَّنُ; marah-al-arwah:50:s2:3 يَجُوزُ

## 28. T-A08 — The muʿrib's etiquette — AdabEngine (1)

- **Asserts wrongly**: «أَيْتَامُهَا» «فَاعِلٌ لِـ«شَوَارِعًا»» (the active participle's doer, al-Durra) flagged as a passive's «fāʿil»
- **Where**: AdabEngine.check("naibNotFail") reads a «فاعل» within three tokens of any passive verb, even when the line names another governor («فَاعِلٌ لِـ«X»»).
- **Reproduce**: no lab path for this engine; the corpus place muallaqat-labid:13:s1:8 «أَيْتَامُهَا» gives `the line breaks the muʿrib's etiquette: naibNotFail`
- **Correct, by the book**: obey — `qawaid-al-irab-turkish.txt` l.70 «(bāb 4) «naibü'l-fail (fail yerine geçen)» — the rule is for the PASSIVE verb's marfūʿ»
- **Narrowest gate**: AdabEngine naibNotFail: skip lines that name another governor («فَاعِلٌ لِـ«X»») — 4,517 obey.
- **Same rule, agreeing**: AdabEngine naibNotFail: obey 4,517 / finding 1
- **Places** (first 6): muallaqat-labid:13:s1:8 أَيْتَامُهَا

## 29. T-M04 — The manṣūb offices — MansubEngine (v332) (1)

- **Asserts wrongly**: engine withdraws a naʿt (case mismatch) by taking the nearer majrūr (فِعْلٍ قَلْبِيٍّ) as its head; the author's head is أَفْعَالٌ (marfūʿ): «أَفْعَالٌ تَدُلُّ …، دَاخِلَةٌ …، نَاصِبَةٌ …»
- **Where**: MansubEngine / the v332 veto picks the nearest noun as the head of an adjective after a comma; the clause-naʿt «تَدُلُّ …» between them hides the real head.
- **Reproduce (typed)**: `Murib.line(rows, 5)` on «أَفْعَالٌ تَدُلُّ عَلَى فِعْلٍ قَلْبِيٍّ، دَاخِلَةٌ عَلَى الْمُبْتَدَإِ» → `{"w": "دَاخِلَةٌ", "line": "اسْمٌ، مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ."}`
- **Reproduce (story sentence izhar-al-asrar:9:s3:11, typed as written)**: «الْقِسْمُ الثَّانِي أَفْعَالُ الْقُلُوبِ، وَهِيَ أَفْعَالٌ تَدُلُّ عَلَى فِعْلٍ قَلْبِيٍّ، دَاخِلَةٌ عَلَى الْمُبْتَدَإِ وَالْخَبَرِ، نَاصِبَةٌ إِيَّاهُمَا عَلَى الْمَفْعُولِيَّةِ، نَحْوُ: عَلِمْتُ وَرَأَيْتُ وَوَجَدْتُ » → `Murib.line(rows, 10).ar` = `اسْمٌ، مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.`; the audit's verdict: اسْمٌ، مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.
- **Correct, by the book**: نَعْتٌ ثَانٍ لِـ«أَفْعَالٌ» مَرْفُوعٌ — — (no book line decides)
- **Narrowest gate**: The v332 naʿt veto: the head of a comma-separated adjective is the first noun of the series (أَفْعَالٌ)، skipping a naʿt clause in between; veto only when NO earlier noun of its case stands in the clause.
- **Same rule, agreeing**: MansubEngine (v332) agrees 151
- **Places** (first 6): izhar-al-asrar:9:s3:11 دَاخِلَةٌ

## 30. T-H03 — The Shudhūr rules — Sh336Engine (v336-Sh) (1)

- **Asserts wrongly**: «وَمَنْ كَانَ حَفِيظًا وَمَا كَانَ عَلِيمًا لَا يَعْلَمُ …» — author: the clause is the khabar of مَنْ / engine: naʿt of عَلِيمًا
- **Where**: Sh336 R209 / the clause seat: a clause after a manṣūb khabar of kāna is read as its naʿt.
- **Reproduce (typed)**: `Murib.line(rows, 7)` on «وَمَنْ كَانَ حَفِيظًا وَمَا كَانَ عَلِيمًا لَا يَعْلَمُ أَيْنَ خَزَائِنُ الْأَرْضِ» → `{"w": "يَعْلَمُ", "line": "فِعْلٌ مُضَارِعٌ، مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ «هُوَ»، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«عَلِيمًا»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ (النَّكِرَةُ غَيْرُ مَحْضَةٍ)، وَهُوَ فِعْلٌ قَلْبِيٌّ مُعَلَّقٌ عَنِ الْعَمَلِ لَفْظًا بِالِاسْتِفْهَامِ، وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ مَفْعُولَيْهِ."}`
- **Reproduce (story sentence qisas-al-nabiyyin-1:15:s23:8, typed as written)**: «وَمَنْ كَانَ حَفِيظًا وَمَا كَانَ عَلِيمًا لَا يَعْلَمُ أَيْنَ خَزَائِنُ الْأَرْضِ وَكَيْفَ يَنْتَفِعُ بِهَا.» → `Murib.line(rows, 7).ar` = `فِعْلٌ مُضَارِعٌ، مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ «هُوَ»، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«عَلِيمًا»، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ (النَّكِرَةُ غَيْرُ مَحْضَةٍ)، وَهُوَ فِعْلٌ قَلْبِيٌّ مُعَلَّقٌ عَنِ الْعَمَلِ لَفْظًا بِالِاسْتِفْهَامِ، وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ مَفْعُولَيْهِ.`; the audit's verdict: فِعْلٌ مُضَارِعٌ، مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ «هُوَ»، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«عَلِيمًا»، أَوْ فِي م
- **Correct, by the book**: the clause completes the مَنْ-sentence (the author: خَبَرُ الْمُبْتَدَإِ «مَنْ») — `shudhur-al-dhahab-src.txt` l.155 «الرَّابِعُ خَبَرُهُ، وَهُوَ: مَا تَحْصُلُ بِهِ الْفَائِدَةُ مَعَ مُبْتَدَأ غَيْرِ الْوَصْفِ الْمَذْكُورِ.»
- **Narrowest gate**: A clause after the khabar of kāna inside a مَنْ / الَّذِي frame belongs to that frame (its khabar), not to the khabar as naʿt.
- **Same rule, agreeing**: Sh336 agrees 184 (all rules)
- **Places** (first 6): qisas-al-nabiyyin-1:15:s23:8 يَعْلَمُ

## Also seen (not engine faults in the iʿrāb)

- `GrammarAudit339.taalluq` prints an offered verdict's alternative as «[object Object]» (25 + 21 offered items): the `alt` object is concatenated, not its text. Audit cosmetics only (the page half of tools/grammar_audit.js).
- The v328 taʿalluq comparison reads «مُتَعَلِّقٌ بِـX» literally: an authored description («الْفِعْلُ قَبْلَهُ», «خَبَرُ كَانَ الْمُقَدَّمُ») counts as a contradiction though the engine names the same word (cluster T-T05, 14 items, C). A reader for descriptions would remove them from the audit.
- The page's SignEngine / DabtEngine / AdabEngine audits cap their lists (80, 400, 40 per rule); `tools/grammar_audit.js` now lifts the caps in its own headless page (the methods re-made from their source with the cap removed) — the engines are unchanged.
