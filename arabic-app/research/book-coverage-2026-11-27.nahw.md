# The naḥw books' ledger — v342-N (2026-11-27)

Every rule / section of Shudhūr al-Dhahab, Qawāʿid al-Iʿrāb, Iẓhār al-Asrār and al-Kāfiya, cut by `tools/ledger/build_ledger.py`
from the sources and joined with the maps beside it (`tools/ledger/*_map.py`). **applied** = the book's own example (or, where it
prints none, the shortest school phrase) read by the engine named, every probe passing in the built page; **noted** = a grammar note
quotes or anchors it; **not-automatable** = the reason is given; **open** = none of these. The smoke check «v342 — the ledger …»
re-proves every applied entry and pins the counts. JSON: `content/rules/coverage_<book>.json`.

## Shudhūr al-Dhahab (Ibn Hishām)

Source: `research/sources/shudhur-al-dhahab-qawaid.jsonl + shudhur-al-dhahab-src.txt`. Entries: 235 — applied **146**, noted **65**, not automatable **22**, open **1** (headings 1, lecture fragments 0, cited verses 0, counted apart).

| id | line | status | carried by / reason | the book |
|---|---|---|---|---|
| S4 | 4 | noted | note:al-kalima-wal-kalam | الْكَلِمَةُ قَوْلٌ مُفْرَدٌ. |
| S6 | 6 | noted | note:al-kalima-wal-kalam | وَهِيَ اسْمٌ، وَفِعْلٌ، وَحَرْفٌ. |
| S8 | 8 | noted | note:al-kalima-wal-kalam | فَالِاسْمُ مَا يَقْبَلُ أَلْ، أَوِ النِّدَاءَ، أَوِ الْإِسْنَادَ إِلَيْهِ. |
| S10 | 10 | noted | note:al-kalima-wal-kalam | وَالْفِعْلُ إِمَّا مَاضٍ، وَهُوَ مَا يَقْبَلُ تَاءَ التَّأْنِيثِ السَّاكِنَةَ كَقَامَتْ وَ |
| S11 | 11 | noted | note:al-kalima-wal-kalam | أَوْ أَمْرٌ، وَهُوَ مَا دَلَّ عَلَى الطَّلَبِ مَعَ قَبُولِ يَاءِ الْمُخَاطَبَةِ كَقُومِي،  |
| S12 | 12 | noted | note:al-kalima-wal-kalam | أَوْ مُضَارِعٌ، وَهُوَ مَا يَقْبَلُ لَمْ كَلَمْ يَقُمْ، وَافْتِتَاحُهُ بِحَرْفٍ مِنْ «نَأَ |
| S14 | 14 | noted | note:al-kalima-wal-kalam | وَالْحَرْفُ مَا عَدَا ذٰلِكَ، كَهَلْ وَفِي وَلَمْ. |
| S17 | 17 | noted | note:al-kalima-wal-kalam | وَالْكَلَامُ قَوْلٌ مُفِيدٌ مَقْصُودٌ. |
| S19 | 19 | noted | note:al-kalima-wal-kalam | وَهُوَ خَبَرٌ، وَطَلَبٌ، وَإِنْشَاءٌ. |
| S22 | 22 | applied | engine:TaqdirEngine | الْإِعْرَابُ أَثَرٌ ظَاهِرٌ أَوْ مُقَدَّرٌ يَجْلِبُهُ الْعَامِلُ فِي آخِرِ الِاسْمِ الْمُت |
| S24 | 24 | applied | engine:Murib.line | وَأَنْوَاعُهُ رَفْعٌ وَنَصْبٌ فِي اسْمٍ وَفِعْلٍ «كَزَيْدٌ يَقُومُ» «وَإِنَّ زَيْدًا لَنْ  |
| S25 | 25 | applied | engine:SignEngine | وَالْأَصْلُ كَوْنُ الرَّفْعِ بِالضَّمَّةِ، وَالنَّصْبِ بِالْفَتْحَةِ، وَالْجَرِّ بِالْكَسْ |
| S30 | 30 | applied | engine:SignEngine · the diptote | أَحَدُهَا: مَا لَا يَنْصَرِفُ، فَإِنَّهُ يُجَرُّ بِالْفَتْحَةِ، نَحْوُ «بِأَفْضَلَ مِنْهُ» |
| S32 | 32 | applied | engine:SignEngine · I-10 | الثَّانِي: مَا جُمِعَ بِأَلِفٍ وَتَاءٍ مَزِيدَتَيْنِ، «كَهِنْدَاتٍ» فَإِنَّهُ يُنْصَبُ بِا |
| S34 | 34 | applied | engine:SignEngine · the five nouns | الثَّالِثُ: «ذُو» بِمَعْنَى صَاحِبٍ، وَمَا أُضِيفَ لِغَيْرِ الْيَاءِ مِنْ «أَبٍ» «وَأَخٍ»  |
| S36 | 36 | not-automatable | the better usage of الْهَنُ (declined on its last letter) — a preference among dialects | وَالْأَفْصَحُ فِي الْهَنِ النَّقْصُ. |
| S39 | 39 | applied | engine:SignEngine · the dual | الرَّابِعُ: الْمُثَنَّى، كَالزَّيْدَانِ وَالْهِنْدَانِ، فَإِنَّهُ يُرْفَعُ بِالْأَلِفِ، وَ |
| S41 | 41 | noted | note:al-muthanna — ⚠ the engine still misreads the example: «جَاءَ الرَّجُلَانِ كِلَاهُمَا» → اسم، وعلامته مقدرة، توكيد، والضمير مضاف إليه. | وَأُلْحِقَ بِهِ اثْنَانِ، وَاثْنَتَانِ، وَثِنْتَانِ مُطْلَقًا، وَكِلَا وَكِلْتَا مُضَافَيْ |
| S43 | 43 | applied | engine:SignEngine · the sound plural | الْخَامِسُ: جَمْعُ الْمُذَكَّرِ السَّالِمُ، كَالزَّيْدُونَ وَالْمُسْلِمُونَ، فَإِنَّهُ يُر |
| S45 | 45 | noted | note:jam-mudhakkar-salim — ⚠ the engine still misreads the example: «الْحَمْدُ لِلَّهِ رَبِّ الْعَالَمِينَ» → اسم، مجرور بالحروف، مضاف إليه. | وَأُلْحِقَ بِهِ: أُولُو، وَعَالَمُونَ، وَأَرَضُونَ، وَسِنُونَ، وَعِشْرُونَ وَبَابُهُمَا، و |
| S48 | 48 | applied | engine:Murib.fiveRaf336, note:afal-khamsa | السَّادِسُ: يَفْعَلَانِ وَتَفْعَلَانِ وَيَفْعَلُونَ وَتَفْعَلُونَ وَتَفْعَلِينَ، فَإِنَّهَ |
| S49 | 49 | noted | note:afal-khamsa | وَأَمَّا نَحْوُ «تُحَاجُّونِي» فَالْمَحْذُوفُ نُونُ الْوِقَايَةِ، وَأَمَّا «إِلَّا أَنْ يَ |
| S51 | 51 | applied | engine:Murib.line · T2 | السَّابِعُ: الْفِعْلُ الْمُعْتَلُّ الْآخِرِ، كَيَغْزُو، وَيَخْشَى، وَيَرْمِي، فَإِنَّهُ يُ |
| S54 | 54 | applied | engine:TaqdirEngine | فَصْلٌ: تُقَدَّرُ الْحَرَكَاتُ كُلُّهَا فِي نَحْوِ «غُلَامِي» وَنَحْوِ «الْفَتَى» وَيُسَمَ |
| R1 | 67 | applied | engine:Murib.line · bināʾ | البناء لزوم آخر الكلمة حالة واحدة لفظا أو تقديرا |
| R2 | 67 | applied | engine:Murib.line · T1 (nūn al-niswa) | يَتَرَبَّصْنَ ، يُرْضِعْنَ |
| R3 | 67 | applied | engine:Murib.line · T1 | ضَرَبْتُ ، ضَرَبْنَا ، ضَرَبَكَ زَيْدٌ ، ضَرَبَا ، ضَرَبُوا |
| R4 | 71 | applied | engine:Murib.line · T2 (the amr built on its jazm) | اضْرِبْ ، اضْرِبَا ، اضْرِبُوا ، اضْرِبِي ، اغْزُ ، اخْشَ ، ارْمِ |
| R5 | 71 | applied | engine:DabtEngine · mafʿūl muṭlaq | فَقُولَا لَهُ قَوْلًا لَيِّنًا |
| R6 | 73 | applied | engine:Murib.line · T3 (nūn al-tawkīd on contact) | لَيُنْبَذَنَّ ، لَتُبْلَوُنَّ ، لَتُسْمَعُنَّ |
| R7 | 73 | applied | engine:AdadEngine · I-17 | جَاءَنِي أَحَدَ عَشَرَ ، رَأَيْتُ اثْنَيْ عَشَرَ |
| R8 | 73 | noted | note:al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar — ⚠ the engine still misreads the example: «هُوَ يَأْتِينَا صَبَاحَ مَسَاءَ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، وهو مضاف. | هُوَ يَأْتِينَا صَبَاحَ مَسَاءَ ، صَبَاحَ مَسَاءٍ ، هَمْزَةُ بَيْنٍ بَيْنٍ ، وَلَوْلَا يَو |
| R9 | 73 | noted | note:jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha — ⚠ the engine still misreads the example: «عَلَى حِينَ عَاتَبْتُ» → اسم، مجرور بالحروف. | عَلَى حِينَ عَاتَبْتُ ، هَذَا يَوْمُ يَنْفَعُ ، عَلَى حِينِ التَّوَاصُلُ غَيْرُ دَانِ |
| R10 | 73 | not-automatable | a qirāʾa report (Nāfiʿ alone reads يَوْمَ; the Baṣrans reject the bināʾ) — the reading, not the letters, decides | هَذَا يَوْمُ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ |
| R11 | 73 | noted | note:jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha — ⚠ the engine still misreads the example: «وَمِنْ خِزْيِ يَوْمِئِذٍ» → اسم، مضاف إليه. | وَمِنْ خِزْيِ يَوْمِئِذٍ ، وَمِنَّا دُونَ ذَلِكَ ، لَقَدْ تَقَطَّعَ بَيْنَكُمْ ، إِنَّهُ ل |
| R12 | 81 | applied | engine:Murib.line · lā al-nāfiya li-l-jins (I-10); Nahw342Engine · laDual, note:la-nafiya-lil-jins | لَا رَجُلَ فِي الدَّارِ ، لَا رِجَالَ ، لَا رَجُلَيْنِ ، لَا قَائِمِينَ ، لَا قَائِمَاتِ ، |
| R13 | 81 | noted | note:la-nafiya-lil-jins — ⚠ the engine still misreads the example: «لَا رَجُلَ ظَرِيفًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | لَا رَجُلَ ظَرِيفًا ، لَا رَجُلَ ظَرِيفٌ ، لَا رَجُلَ ظَرِيفَ |
| R14 | 81 | applied | engine:Murib.line, note:la-nafiya-lil-jins | لَا حَوْلَ وَلَا قُوَّةَ ، لَا لَغْوٌ فِيهَا وَلَا تَأْثِيمَ ، لَا بَيْعٌ فِيهِ وَلَا خُلَ |
| R15 | 85 | applied | engine:Sh336Engine · R15 (ـوَيْهِ) | سِيبَوَيْهِ ، عَمْرَوَيْهِ ، نِفْطَوَيْهِ |
| R16 | 85 | applied | engine:Murib.line · ism fiʿl (I-20) | نَزَالِ ، دَرَاكِ ، حَذَارِ ، تَرَاكِهَا |
| R17 | 85 | noted | note:al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab — ⚠ the engine still misreads the example: «يَا خَبَاثِ» → اسم، منادى. | يَا خَبَاثِ ، يَا فَسَاقِ ، يَا لَكَاعِ |
| R18 | 85 | noted | note:al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab — ⚠ the engine still misreads the example: «إِذَا قَالَتْ حَذَامِ فَصَدِّقُوهَا» → اسم، مجرور وعلامة جره الكسرة الظاهرة. | إِذَا قَالَتْ حَذَامِ فَصَدِّقُوهَا ، مَتَى تَرِدَنْ يَوْمًا سَفَارِ ، هَلَكَتْ جَهْرَةً و |
| R19 | 85 | applied | engine:ZarfBinaEngine · أَمْسِ (I-12) | ذَهَبَ أَمْسِ ، ذَهَبَ أَمْسُ ، مُذْ أَمْسَا ، فَعَلْتُ ذَلِكَ أَمْسًا ، مِنْ أُمُوسِ ، كَ |
| R20 | 88 | applied | engine:Nahw342Engine · qabl | لِلَّهِ الْأَمْرُ مِنْ قَبْلُ وَمِنْ بَعْدُ ، وَكُنْتُ قَبْلًا ، فَمَا شَرِبُوا بَعْدًا ،  |
| R21 | 88 | noted | note:al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya — ⚠ the engine still misreads the example: «قَبَضْتُ عَشَرَةً لَيْسَ غَيْرُ» → اسم، مبني لا يتغير آخره، اسم ليس. | قَبَضْتُ عَشَرَةً لَيْسَ غَيْرُ |
| R22 | 88 | applied | engine:Nahw342Engine · qabl | أَتَيْتُ فَوْقَ بَنِي كُلَيْبٍ مِنْ عَلُ ، كَجُلْمُودِ صَخْرٍ حَطَّهُ السَّيْلُ مِنْ عَلِ |
| R23 | 88 | noted | note:ism-mawsul — ⚠ the engine still misreads the example: «اضْرِبْ أَيُّهُمْ أَفْضَلُ» → اسم، والضمير مضاف إليه. | ثُمَّ لَنَنْزِعَنَّ مِنْ كُلِّ شِيعَةٍ أَيُّهُمْ أَشَدُّ ، اضْرِبْ أَيُّهُمْ أَفْضَلُ |
| R24 | 92 | applied | engine:NidaEngine · the single vocative | يَا زَيْدُ ، يَا رَجُلُ ، يَا جِبَالُ أَوِّبِي مَعَهُ ، يَا زَيْدَانِ ، يَا زَيْدُونَ |
| R25 | 92 | applied | engine:Murib.line, note:vocative-munada | يَا عَبْدَ اللهِ ، يَا رَسُولَ اللهِ ، يَا كَثِيرًا بِرُّهُ ، يَا رَجُلًا خُذْ بِيَدِي ، أ |
| R26 | 92 | noted | note:vocative-munada — ⚠ the engine still misreads the example: «سَلَامُ اللهِ يَا مَطَرٌ عَلَيْهَا» → اسم، مبني لا يتغير آخره، منادى. | سَلَامُ اللهِ يَا مَطَرٌ عَلَيْهَا ، يَا عَدِيًّا لَقَدْ وَقَتْكَ الْأَوَاقِي ، يَا زَيْدَ |
| R27 | 95 | applied | engine:Murib.line · the built classes (I-20) | هَلْ ، ثُمَّ ، جَيْرِ ، مُنْذُ ، صَهْ ، آمِينَ ، إِيهِ ، هَيْتَ |
| R28 | 95 | noted | note:asma-al-ishara-wal-mawsulat — ⚠ the engine still misreads the example: «هَذَانِ» → اسم، مبتدأ. | هَذَانِ ، هَذَيْنِ ، اللَّذَيْنِ ، أَيُّكُمْ يَأْتِينِي بِعَرْشِهَا ، أَيَّ مُنْقَلَبٍ يَن |
| R29 | 95 | not-automatable | a dictionary note (صَهْ «be silent», مَهْ «stop», إِيهِ / إِيهٍ by tanwīn) — meaning, not iʿrāb | صَهْ ، مَهْ ، إِيهِ ، إِيهٍ |
| R30 | 95 | applied | engine:ZarfBinaEngine · حَيْثُ (I-12) | أَمَا تَرَى حَيْثُ سُهَيْلٍ طَالِعًا ، سَنَسْتَدْرِجُهُمْ مِنْ حَيْثِ لَا يَعْلَمُونَ |
| R31 | 95 | applied | engine:ZarfBinaEngine · إِذْ (I-12) | وَاذْكُرُوا إِذْ أَنْتُمْ قَلِيلٌ ، وَإِذِ اعْتَزَلْتُمُوهُمْ ، فَبَيْنَمَا الْعُسْرُ إِذْ |
| R32 | 98 | noted | note:huruf-jarr-nawadir — ⚠ the engine still misreads the example: «رُبَّ رَجُلٍ» → حرف جر، لا محل له من الإعراب. | الاسْمُ نَكِرَةٌ وَهُوَ مَا يَقْبَلُ رُبَّ |
| R33 | 98 | applied | engine:Murib.line | رُبَّهُ رَجُلًا ، رُبَّهُ فِتْيَةً دَعَوْتُ |
| R34 | 101 | applied | engine:Nahw342Engine · demKaf | ذَلِكَ ، إِيَّاكَ |
| R35 | 101 | not-automatable | the referent of a third-person pronoun (context, rank, order) — meaning; the engines name the pronoun, not what it returns to | إِنَّا أَنْزَلْنَاهُ ، وَإِذِ ابْتَلَى إِبْرَاهِيمَ رَبُّهُ ، فَأَوْجَسَ فِي نَفْسِهِ خِيف |
| R36 | 107 | not-automatable | the personal vs generic proper name (أُسَامَةُ for the lion) — the denotation, not the letters | زَيْدٌ ، أُسَامَةُ أَشْجَعُ مِنْ ثُعَالَةَ ، هَذَا أُسَامَةُ مُقْبِلًا |
| R37 | 111 | applied | engine:Murib.line | سَعِيدُ كُرْزٍ ، سَعِيدٌ كُرْزٌ ، عَبْدُ اللهِ زَيْنُ الْعَابِدِينَ ، زَيْدٌ زَيْنُ الْعَا |
| R38 | 111 | applied | engine:Nahw342Engine · demHa | هَذَا ، ذَاكَ ، ذَلِكَ |
| R39 | 111 | not-automatable | a writing rule of the demonstratives (no lām of distance in ذَانِكَ، أُولَئِكَ، هَذَاكَ) — what may be said; no iʿrāb changes | ذَانِكَ ، تَانِكَ ، أُولَئِكَ ، هَذَاكَ ، أُولَالِكَ |
| R40 | 115 | applied | engine:Murib.line · silaOf | جَاءَنِي الَّذِي قَامَ ، الَّذِي أَبُوهُ قَائِمٌ ، وَمَنْ عِنْدَهُ لَا يَسْتَكْبِرُونَ ، ا |
| R41 | 115 | applied | engine:Murib.line · silaOf (the ʿāʾid) | جَاءَ الَّذِي قَامَ أَبُوهُ ، سُعَادُ الَّتِي أَضْنَاكَ حُبُّ سُعَادَا |
| R42 | 117 | applied | engine:Sh336Engine · R42 (مَاذَا) | مَاذَا أَنْزَلَ رَبُّكُمْ ، مَنْ ذَا لَقِيتَ ، مَنْ ذَا قَالَهَا ، مَاذَا صَنَعْتَ |
| R43 | 120 | noted | note:ism-mawsul — ⚠ the engine still misreads the example: «الضَّارِبُ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، مبتدأ. | الضَّارِبُ ، الْمَضْرُوبُ ، فَالْمُغِيرَاتِ صُبْحًا فَأَثَرْنَ |
| R44 | 123 | not-automatable | the kinds of the definite article (ʿahd, jins, istighrāq) — meaning; the note anwa-al-lam-al-tarif carries them | جَاءَ الْقَاضِي ، فِيهَا مِصْبَاحٌ الْمِصْبَاحُ ، وَخُلِقَ الْإِنْسَانُ ضَعِيفًا ، ذَلِكَ  |
| R45 | 123 | applied | engine:Murib.line · نِعْمَ / بِئْسَ | نِعْمَ الْعَبْدُ ، بِئْسَ مَثَلُ الْقَوْمِ ، وَلَنِعْمَ دَارُ الْمُتَّقِينَ ، نِعْمَ رَجُل |
| R46 | 123 | applied | engine:IdafaEngine · I-15 (a demonstrative is never muḍāf) | مَالِ هَذَا الْكِتَابِ ، يَا أَيُّهَا الْإِنْسَانُ ، أَلَا أَيُّهَذَا الزَّاجِرِي |
| R47 | 123 | noted | note:vocative-munada — ⚠ the engine still misreads the example: «يَا أَللهُ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، والضمير مضاف إليه. | يَا غُلَامُ ، يَا أَللهُ ، الضَّارِبَا زَيْدٍ ، الضَّارِبُو زَيْدٍ ، الضَّارِبُ الرَّجُلِ  |
| R48 | 128 | not-automatable | the rank of definiteness a muḍāf inherits — a ranking of meaning, nothing in a line changes | غُلَامِي ، غُلَامُ زَيْدٍ ، غُلَامُ هَذَا ، غُلَامُ الَّذِي جَاءَكَ ، غُلَامُ الْقَاضِي |
| R49 | 131 | applied | engine:Nahw342Engine · sababi | الْفَاعِلُ مَا قُدِّمَ الْفِعْلُ أَوْ شِبْهُهُ عَلَيْهِ وَأُسْنِدَ إِلَيْهِ عَلَى جِهَةِ ق |
| R50 | 131 | applied | engine:Murib.line · nawāsikh | كَانَ زَيْدٌ قَائِمًا ، إِنَّ زَيْدًا قَائِمٌ ، ظَنَنْتُ زَيْدًا قَائِمًا |
| R51 | 135 | applied | engine:Nahw342Engine · sababi | وَقُضِيَ الْأَمْرُ ، ضُرِبَ زَيْدٌ ، عَمْرٌو مَضْرُوبٌ غُلَامُهُ |
| R52 | 135 | applied | engine:SentenceAnalyzer · T5 (the hollow passive) | فَإِذَا نُفِخَ فِي الصُّورِ نَفْخَةٌ وَاحِدَةٌ ، صِيمَ رَمَضَانُ ، جُلِسَ أَمَامُكَ ، غَيْ |
| R53 | 135 | not-automatable | which word is the nāʾib in «لَا يُؤْخَذْ مِنْهَا» (the jarr phrase, not a pronoun of كُلَّ عَدْلٍ) is argued from meaning | وَإِنْ تَعْدِلْ كُلَّ عَدْلٍ لَا يُؤْخَذْ مِنْهَا |
| R54 | 138 | applied | engine:Murib.doer · the hidden doer | وَلَا يُحْذَفَانِ بَلْ يَسْتَتِرَانِ وَيُحْذَفُ عَامِلُهُمَا جَوَازًا |
| R55 | 138 | applied | engine:Murib.doer · the hidden doer | لَا يُحْذَفَانِ، بَلْ يَسْتَتِرَانِ |
| R56 | 138 | not-automatable | an optional dropped verb known from the question (زَيْدٌ answering مَنْ قَامَ؟) — needs the dialogue | يُحْذَفُ عَامِلُهُمَا جَوَازًا |
| R57 | 138 | applied | engine:Nahw342Engine · idhaFail | وَالْوَاجِبُ ضَابِطُهُ: أَنْ يَتَأَخَّرَ عَنْهُ فِعْلٌ مُفَسِّرٌ لَهُ |
| R58 | 138 | not-automatable | whether a clause can be a fāʿil (the sound view: never) — a doctrine; the engines never make one | أَنَّهُمَا لَا يَكُونَانِ جُمْلَةً |
| R59 | 138 | noted | note:al-fail-al-muzhar-wa-tanith-amilih — ⚠ the engine still misreads the example: «هِنْدٌ قَامَتْ» → فعل ماض، مبني على الفتح، والفاعل ضمير مستتر جوازا تقديره «هي | وُجُوبًا فِي نَحْوِ «الشَّمْسُ طَلَعَتْ» وَ«قَامَتْ هِنْدٌ» |
| R60 | 138 | applied | engine:Murib.doer | أَنْ يَكُونَ الْفَاعِلُ ظَاهِرًا مُتَّصِلًا مَجَازِيَّ التَّأْنِيثِ |
| R61 | 138 | applied | engine:Murib.doer | جَمْعَ تَكْسِيرٍ، أَوِ اسْمَ جَمْعٍ … فَالتَّأْنِيثُ عَلَى مَعْنَى الْجَمَاعَةِ، وَالتَّذْ |
| R62 | 138 | applied | engine:IstithnaEngine · mufarragh | وَأَمَّا التَّأْنِيثُ الْمَرْجُوحُ فَفِي مَسْأَلَةٍ وَاحِدَةٍ، وَهِيَ: أَنْ يَكُونَ الْفَا |
| R63 | 138 | noted | note:al-fail-al-muzhar-wa-tanith-amilih — ⚠ the engine still misreads the example: «أَكَلُونِي الْبَرَاغِيثُ» → فعل ماض، مبني على الضم لاتصاله بواو الجماعة، وفيه ضمير هو ال | إِنَّ عَامِلَهُمَا لَا تَلْحَقُهُ عَلَامَةُ تَثْنِيَةٍ وَلَا جَمْعٍ، فِي الْأَمْرِ الْغَال |
| R64 | 147 | applied | engine:Murib.khabarOf | الْمُجَرَّدُ عَنِ الْعَوَامِلِ اللَّفْظِيَّةِ: مُخْبَرًا عَنْهُ، أَوْ وَصْفًا رَافِعًا لِم |
| R65 | 147 | applied | engine:Nahw342Engine · wasf | وَالثَّانِي شَرْطُهُ نَفْيٌ أَوِ اسْتِفْهَامٌ |
| R66 | 151 | noted | note:mubtada-khabar — ⚠ the engine still misreads the example: «أَقَائِمٌ أَبَوَاهُ زَيْدٌ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، بدل. | خَرَجَ عَنْ قَوْلِي «مُكْتَفًى بِهِ» نَحْوُ «أَقَائِمٌ أَبَوَاهُ زَيْدٌ» |
| R67 | 151 | applied | engine:Murib.khabarOf | وَلَا يُبْتَدَأُ بِنَكِرَةٍ إِلَّا إِنْ عَمَّتْ … أَوْ خَصَّتْ |
| R68 | 155 | applied | engine:Nahw342Engine · wasf | مَا تَحْصُلُ بِهِ الْفَائِدَةُ مَعَ مُبْتَدَأ غَيْرِ الْوَصْفِ الْمَذْكُورِ |
| R69 | 155 | applied | engine:MansubEngine · v332 (ẓarf as khabar) | وَلَا يَكُونُ زَمَانًا وَالْمُبْتَدَأُ اسْمُ ذَاتٍ |
| R70 | 155 | applied | engine:Murib.line · kāna and its sisters (I-2) | مَا يَعْمَلُ هَذَا الْعَمَلَ بِلَا شَرْطٍ، وَهِيَ ثَمَانِيَةٌ: كَانَ وَلَيْسَ وَمَا بَيْنَ |
| R71 | 155 | applied | engine:Murib.line · زَالَ يَزُولُ complete (I-2) | وَيُشْتَرَطُ فِي «زَالَ» شَرْطٌ آخَرُ، وَهُوَ أَنْ يَكُونَ مَاضِيَ يَزَالُ |
| R72 | 162 | noted | note:kana-wa-akhawatuha — ⚠ the engine still misreads the example: «أَمَّا أَنْتَ مُنْطَلِقًا انْطَلَقْتُ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | وَيَجِبُ حَذْفُ «كَانَ» وَحْدَهَا بَعْدَ «أَمَّا» |
| R73 | 162 | noted | note:kana-wa-akhawatuha — ⚠ the engine still misreads the example: «الْتَمِسْ وَلَوْ خَاتَمًا مِنْ حَدِيدٍ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | حَذْفُ «كَانَ» مَعَ اسْمِهَا وَإِبْقَاءُ خَبَرِهَا … أَنْ يَتَقَدَّمَهَا «إِنْ» أَوْ «لَوْ |
| R74 | 165 | applied | engine:Murib.line · T6 (لَمْ يَكُ) | حَذْفُ نُونِ «كَانَ» … أَنْ تَكُونَ بِلَفْظِ الْمُضَارِعِ … مَجْزُومًا … أَنْ لَا يَقَعَ ب |
| R75 | 165 | applied | engine:MuqarabaEngine · I-16 | وَيَكُونُ خَبَرُهَا مُضَارِعًا |
| R76 | 165 | applied | engine:Murib.line | وَقَدْ جَعَلْتُ إِذَا مَا قُمْتُ يُثْقِلُنِي ثَوْبِي |
| R77 | 168 | noted | note:ma-la-mushabbaha — ⚠ the engine still misreads the example: «وَلَاتَ حِينَ مَنَاصٍ» → اسم، مجرور بالحروف، مضاف إليه، وهو مضاف. | «لَاتَ» … وَلَا تَعْمَلُ إِلَّا فِي الْحِينِ بِكَثْرَةٍ، أَوِ السَّاعَةِ أَوِ الْأَوَانِ ب |
| R78 | 168 | applied | engine:Sh336Engine · R78 (the Ḥijāzī مَا) | شَرْطُ إِعْمَالِهِنَّ نَفْيُ الْخَبَرِ، وَتَأْخِيرُهُ، وَأَنْ لَا يَلِيَهُنَّ مَعْمُولُهُ  |
| R79 | 168 | applied | engine:Sh336Engine · R79 (the Tamīmī مَا) | وَلَا يُعْمِلُهَا بَنُو تَمِيمٍ وَلَوِ اسْتَوْفَتِ الشُّرُوطَ الْأَرْبَعَةَ |
| R80 | 168 | noted | note:ma-la-mushabbaha — ⚠ the engine still misreads the example: «فَلَا شَيْءٌ عَلَى الْأَرْضِ بَاقِيَا» → فعل أمر، مبني لا يتغير آخره، والألف ضمير متصل مبني في محل رف | وَأَمَّا «لَا» فَإِنَّهَا تَعْمَلُ بِالشُّرُوطِ الْمَذْكُورَةِ لِمَا … وَيُضَافُ … أَنْ يَ |
| R81 | 168 | noted | note:ma-la-mushabbaha — ⚠ the engine still misreads the example: «إِنْ ذَلِكَ نَافِعَكَ وَلَا ضَارَّكَ» → اسم، مبتدأ، والضمير مضاف إليه. | وَأَمَّا «إِنْ» فَتَعْمَلُ بِالشُّرُوطِ الْمَذْكُورَةِ … وَتَعْمَلُ فِي اسْمِ مَعْرِفَةٍ و |
| R82 | 174 | applied | engine:InnaEngine · the fronted khabar | وَلَا يَجُوزُ تَقَدُّمُهُ مُطْلَقًا، وَلَا تَوَسُّطُهُ إِلَّا إِنْ كَانَ ظَرْفًا أَوْ مَجْ |
| R83 | 179 | noted | note:mawadi-kasr-inna — ⚠ the engine still misreads the example: «جَلَسْتُ حَيْثُ إِنَّ زَيْدًا جَالِسٌ» → حرف توكيد ونصب، تنصب الاسم وترفع الخبر، لا محل له من الإعراب | وَتُكْسَرُ «إِنَّ» فِي الِابْتِدَاءِ، وَفِي أَوَّلِ الصِّلَةِ وَالصِّفَةِ وَالْجُمْلَةِ ال |
| R84 | 179 | applied | engine:Sh336Engine · R209 (taʿlīq by the lām) | أَنْ تَقَعَ قَبْلَ اللَّامِ الْمُعَلِّقَةِ |
| R85 | 179 | noted | note:mawadi-fath-anna — ⚠ the engine still misreads the example: «أَوَلَمْ يَكْفِهِمْ أَنَّا أَنْزَلْنَا» → ضمير منفصل، مبني على السكون. | وَيَجِبُ الْفَتْحُ فِي ثَمَانِي مَسَائِلَ |
| R86 | 179 | applied | engine:Nahw342Engine · fujaa | وَيَجُوزُ الْوَجْهَانِ فِي ثَلَاثِ مَسَائِلَ |
| R87 | 182 | applied | engine:Murib.line · lā li-l-jins | وَيَجِبُ تَنْكِيرُهُ كَالِاسْمِ، وَتَأْخِيرُهُ وَلَوْ ظَرْفًا |
| R88 | 182 | noted | note:la-nafiya-lil-jins — ⚠ the engine still misreads the example: «لَا قُرَيْشَ بَعْدَ الْيَوْمِ» → اسم، مبتدأ، وخبره شبه الجملة «بعد اليوم» متعلق بمحذوف. | «قَضِيَّةٌ وَلَا أَبَا حَسَنٍ لَهَا» … فَمُؤَوَّلٌ بِتَقْدِيرِ «مِثْلِ» |
| R89 | 185 | applied | engine:Murib.line · lā li-l-jins | وَيَكْثُرُ حَذْفُهُ إِنْ عُلِمَ، وَتَمِيمٌ لَا تَذْكُرُهُ حِينَئِذٍ |
| R90 | 185 | applied | engine:Murib.line · T2 (the muḍāriʿ raised) | الْمُضَارِعُ إِذَا تَجَرَّدَ مِنْ نَاصِبٍ وَجَازِمٍ |
| R91 | 188 | applied | engine:DabtEngine · I-3, note:al-maful-bihi-wa-qismah | مَا وَقَعَ عَلَيْهِ فِعْلُ الْفَاعِلِ |
| R92 | 188 | applied | engine:Sh336Engine · R92 (the participle governs) | الَّذِي يَنْصِبُ الْمَفْعُولَ بِهِ وَاحِدٌ مِنْ أَرْبَعَةٍ: الْفِعْلُ الْمُتَعَدِّي، وَوَص |
| R93 | 188 | not-automatable | the governing verb left out because the question or the situation shows it (قَالُوا خَيْرًا, مَكَّةَ) — needs the dialogue or the scene | وَقَدْ يُضْمَرُ: جَوَازًا إِذَا دَلَّ عَلَيْهِ دَلِيلٌ مَقَالِيٌّ أَوْ حَالِيٌّ |
| R94 | 188 | applied | engine:Sh336Engine · R94 (ishtighāl) | بَابُ الِاشْتِغَالِ، وَحَقِيقَتُهُ: أَنْ يَتَقَدَّمَ اسْمٌ، وَيَتَأَخَّرَ عَنْهُ فِعْلٌ أَ |
| R95 | 195 | applied | engine:Murib.line | وَإِنَّمَا يَظْهَرُ نَصْبُهُ إِذَا كَانَ مُضَافًا أَوْ شِبْهَهُ أَوْ نَكِرَةً مَجْهُولَةً |
| R96 | 199 | applied | engine:Sh336Engine · R96 (ikhtiṣāṣ) | وَالْمَنْصُوبُ بِأَخُصُّ بَعْدَ ضَمِيرِ مُتَكَلِّمٍ |
| R97 | 199 | noted | note:at-tahdhir — ⚠ the engine still misreads the example: «السِّلَاحَ السِّلَاحَ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | وَالْمَنْصُوبُ بِالْزَمْ أَوْ بِاتَّقِ: إِنْ تَكَرَّرَ أَوْ عُطِفَ عَلَيْهِ، أَوْ كَانَ «إ |
| R98 | 199 | not-automatable | proverbs kept as said (الْكِلَابَ عَلَى الْبَقَرِ) — knowing that a phrase is a proverb is not in the letters | وَالْمَحْذُوفُ عَامِلُهُ، وَالْوَاقِعُ فِي مَثَلٍ أَوْ شِبْهِهِ |
| R99 | 204 | applied | engine:DabtEngine · mafʿūl muṭlaq | الْمَصْدَرُ الْفَضْلَةُ الْمُؤَكِّدُ لِعَامِلِهِ أَوِ الْمُبَيِّنُ لِنَوْعِهِ أَوْ لِعَدَد |
| R100 | 208 | applied | engine:Murib.khabarOf | وَقَوْلِي «الْفَضْلَةُ» احْتِرَازٌ مِنْ نَحْوِ قَوْلِكَ: رُكُوعُ زَيْدٍ رُكُوعٌ حَسَنٌ … و |
| R101 | 204 | applied | engine:MansubEngine · v332 I-8 | وَمَا بِمَعْنَى الْمَصْدَرِ مِثْلُهُ |
| R102 | 208 | applied | engine:MansubEngine · v332 I-18 | الْمَصْدَرُ الْفَضْلَةُ الْمُعَلِّلُ لِحَدَثٍ شَارَكَهُ فِي الزَّمَانِ وَالْفَاعِلِ |
| R103 | 208 | not-automatable | whether the reason shares the time and the doer (جِئْتُكَ الْيَوْمَ لِلسَّفَرِ غَدًا) — meaning decides when the lām is needed | وَيَجِبُ فِي مُعَلَّلٍ فَقَدَ شَرْطًا أَنْ يُجَرَّ بِاللَّامِ أَوْ نَائِبِهَا |
| R104 | 211 | applied | engine:CaseEngine · ẓarf (I-11) | مَا ذُكِرَ فَضْلَةً لِأَجْلِ أَمْرٍ وَقَعَ فِيهِ: مِنْ زَمَانٍ مُطْلَقًا، أَوْ مَكَانٍ مُب |
| R105 | 211 | applied | engine:TaalluqEngine · في with a specific place | وَالْمَكَانِيُّ غَيْرُهُنَّ يُجَرُّ بِفِي … وَقَوْلُهُمْ: «دَخَلْتُ الدَّارَ» عَلَى التَّو |
| R106 | 211 | noted | note:maful-fih — ⚠ the engine still misreads the example: «إِنَّا نَخَافُ مِنْ رَبِّنَا يَوْمًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، ظرف — مفعول فيه. | وَقَدْ يَكُونُ الْعَكْسُ … فَهَذِهِ الْأَنْوَاعُ لَا تُسَمَّى ظَرْفًا فِي الِاصْطِلَاحِ، ب |
| R107 | 216 | applied | engine:Murib.line | الِاسْمُ، الْفَضْلَةُ، التَّالِي وَاوَ الْمُصَاحَبَةِ، مَسْبُوقَةً بِفِعْلٍ أَوْ مَا فِيهِ |
| R108 | 216 | not-automatable | أَجْمَعَ applies to ideas, so شُرَكَاءَكُمْ is a mafʿūl maʿahu — the verb's sense decides | وَلَكِنْ إِذَا أَمْكَنَ الْعَطْفُ فَهُوَ أَوْلَى لِأَنَّهُ الْأَصْلُ |
| R109 | 216 | applied | engine:Murib.line · ʿaṭf | وَلَيْسَ مِنَ الْمَفْعُولِ مَعَهُ |
| R110 | 219 | applied | engine:Sh336Engine · R110 (ṣifa mushabbaha) | الْمُشَبَّهُ بِالْمَفْعُولِ بِهِ، نَحْوُ «زَيْدٌ حَسَنٌ وَجْهَهُ» |
| R111 | 219 | applied | engine:MansubEngine · v332 I-4 (ḥāl) | وَصْفٌ فَضْلَةٌ مَسُوقٌ لِبَيَانِ هَيْئَةِ صَاحِبِهِ أَوْ تَأْكِيدِهِ، أَوْ تَأْكِيدِ عَام |
| R112 | 227 | applied | engine:Murib.line · naʿt (I-5) | وَقَوْلِي «مَسُوقٌ لِبَيَانِ هَيْئَةِ مَا هُوَ لَهُ» مُخْرِجٌ لِأَمْرَيْنِ |
| R113 | 227 | applied | engine:MansubEngine · v332 I-4 | وَيَأْتِي مِنَ الْفَاعِلِ، وَمِنَ الْمَفْعُولِ، وَمِنْهُمَا، مُطْلَقًا، وَمِنَ الْمُضَافِ  |
| R114 | 227 | applied | engine:MansubEngine · v332 I-4 | وَحَقُّهَا أَنْ تَكُونَ نَكِرَةً، مُنْتَقِلَةً، مُشْتَقَّةً، وَأَنْ يَكُونَ صَاحِبُهَا مَع |
| R115 | 230 | applied | engine:MansubEngine · v332 I-9 (tamyīz) | اسْمٌ، نَكِرَةٌ، فَضْلَةٌ، يَرْفَعُ إِبْهَامَ اسْمٍ، أَوْ إِجْمَالَ نِسْبَةٍ |
| R116 | 230 | applied | engine:MansubEngine · v332 I-9 | فَالْأَوَّلُ بَعْدَ الْعَدَدِ الْأَحَدَ عَشَرَ فَمَا فَوْقَهَا إِلَى الْمِائَةِ، وَ«كَمْ»  |
| R117 | 230 | applied | engine:MansubEngine · v332 I-9 | وَالثَّانِي إِمَّا مُحَوَّلٌ عَنِ الْفَاعِلِ … أَوْ عَنِ الْمَفْعُولِ … أَوْ عَنْ غَيْرِهِ |
| R118 | 230 | not-automatable | the proof that «مَا أَنْتِ جَارَهْ» holds a tamyīz is a parallel verse — an argument, not a rule over letters | إِذْ كَانَ التَّمْيِيزُ هُوَ الَّذِي يَكُونُ عَلَى مَعْنَى مِنْ، وَأَمَّا الْحَالُ فَهُوَ  |
| R119 | 237 | applied | engine:IstithnaEngine · I-21 (لَيْسَ / لَا يَكُونُ / مَا خَلَا), note:al-mustathna-wa-nawah-wa-nasbuh, note:istithna | الْمُسْتَثْنَى بِلَيْسَ، أَوْ بِلَا يَكُونُ، أَوْ بِمَا خَلَا، أَوْ بِمَا عَدَا، مُطْلَقًا |
| R120 | 237 | applied | engine:IstithnaEngine · I-21, note:al-mustathna-wa-nawah-wa-nasbuh, note:istithna | أَوْ بِإِلَّا بَعْدَ كَلَامٍ تَامٍّ مُوجَبٍ، أَوْ غَيْرِ مُوجَبٍ وَتَقَدَّمَ الْمُسْتَثْنَ |
| R121 | 237 | applied | engine:IstithnaEngine · mufarragh, note:al-mustathna-wa-nawah-wa-nasbuh, note:istithna | وَغَيْرُ الْمُوجَبِ: إِنْ تُرِكَ فِيهِ الْمُسْتَثْنَى مِنْهُ فَلَا أَثَرَ فِيهِ لِـ«إِلَّا |
| R122 | 237 | applied | engine:IstithnaEngine · غَيْر / سِوَى, note:al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa, note:al-mustathna-wa-nawah-wa-nasbuh, note:istithna | وَالْمُسْتَثْنَى بِغَيْرٍ وَسِوَى مَخْفُوضٌ، وَبِخَلَا وَعَدَا وَحَاشَا مَخْفُوضٌ أَوْ مَن |
| R123 | 245 | applied | engine:IstithnaEngine · مَا خَلَا, note:al-mustathna-wa-nawah-wa-nasbuh | الاسم الواقع بعد «ما خلا» و«ما عدا» منصوب؛ لأن «ما» مصدرية لا تدخل إلا على الجملة الفعلية |
| R124 | 245 | applied | engine:IstithnaEngine · مَا عَدَانِي | «عداني»: نون الوقاية دليل على أن «عدا» فعل؛ إذ لا تجيء إلا مع الأفعال (ومع من وعن خاصة) |
| R125 | 245 | applied | engine:IstithnaEngine · I-21, note:al-mustathna-wa-nawah-wa-nasbuh, note:istithna | المستثنى بإلا بعد كلام تام موجب واجب النصب |
| R126 | 245 | noted | note:al-mustathna-wa-nawah-wa-nasbuh — ⚠ the engine still misreads the example: «وَمَا لِيَ إِلَّا آلَ أَحْمَدَ شِيعَةٌ» → فعل ماض، مبني على الفتح، وفاعله «شيعة». | إذا تقدم المستثنى على المستثنى منه وجب نصبه؛ لأن البدل لا يتقدم على المبدل منه |
| R127 | 245 | applied | engine:IstithnaEngine · mufarragh, note:istithna, note:istithna-mufarragh | إن كان المستثنى منه محذوفًا فلا عمل لإلا، ويسمى استثناء مفرغًا |
| R128 | 245 | applied | engine:IstithnaEngine · badal, note:al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa, note:istithna | إن كان متصلًا جاز في المستثنى وجهان: الإبدال (وهو الراجح) والنصب على الاستثناء |
| R129 | 245 | noted | note:al-mustathna-wa-nawah-wa-nasbuh | إن كان منقطعًا فالحجازيون يوجبون نصبه، والتميميون يجيزون الإبدال ويختارون النصب |
| R130 | 245 | applied | engine:IstithnaEngine · غَيْر / سِوَى always in iḍāfa | المستثنى بغير وسوى مخفوض دائمًا؛ لأنهما ملازمان للإضافة |
| R131 | 245 | applied | engine:IstithnaEngine · خَلَا / عَدَا / حَاشَا | المستثنى بخلا وعدا وحاشا يجوز فيه الخفض والنصب؛ ولم يجوز سيبويه بعد عدا غير النصب، ولا بعد |
| R132 | 245 | applied | engine:MuqarabaEngine · I-16 | وَيَجِبُ كَوْنُهُ مُضَارِعًا مُؤَخَّرًا عَنْهَا، رَافِعًا لضَمِيرِ أَسْمَائِهَا |
| R133 | 245 | applied | engine:MuqarabaEngine · I-16 | مُجَرَّدًا مِنْ «أَنْ» بَعْدَ أَفْعَال الشُّرُوع، وَمَقْرُونًا بها بَعْدَ حَرَى وَاخْلَوْل |
| R134 | 245 | applied | engine:MuqarabaEngine · I-16 | عسى وأوشك: الغالب اقتران خبرهما بأن، وندر تجرده |
| R135 | 245 | applied | engine:MuqarabaEngine · I-16 | كاد وكرب: يترجح تجرد خبرهما من أن، وندر اقترانه بها |
| R136 | 245 | applied | engine:Murib.line | وَرُبَّمَا رُفِعَ السَّبَبِيُّ بِخَبَرِ عَسَى؛ ففي «وَمَاذَا عَسَى الْحَجَّاجُ يَبْلُغُ جُ |
| R137 | 245 | open | probe «وَلَاتَ حِينَ مَنَاصٍ» → اسم، مجرور بالحروف، مضاف إليه، وهو مضاف. | ما حمل على ليس أربعة: لات، وما، ولا، وإن النافية |
| R138 | 248 | noted | note:ma-la-mushabbaha — ⚠ the engine still misreads the example: «إِنْ هُوَ مُسْتَوْلِيًا عَلَى أَحَدٍ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | إن النافية العاملة عمل ليس لا تختص بالنكرات كما تختص بها لا |
| R139 | 248 | applied | engine:Murib.line · the kāffa مَا | وَإِنْ قُرِنَتْ بمَا الْمَزِيدَةِ أُلْغِيتْ وُجُوبًا، إِلَّا لَيْتَ فَجَوَازًا |
| R140 | 248 | noted | note:innama-kaffa — ⚠ the engine still misreads the example: «أَيَحْسَبُونَ أَنَّمَا نُمِدُّهُمْ بِهِ مِنْ مَالٍ» → حرف لا محل له من الإعراب. | احترزت بالمزيدة من الموصولة والمصدرية |
| R141 | 250 | applied | engine:Sh336Engine · R141 (إِنْ) | فَتُلْغى لكِنَّ وُجُوبًا، وكَأَنَّ قِليلا، وَإِنَّ غالبًا |
| R142 | 250 | applied | engine:Sh336Engine · R142 (the lām al-fāriqa) | وَيَغْلِبُ مَعَهَا مُهْمَلَةً اللامُ، وَكَوْنُ الْفِعْلِ التَّالي لهَا نَاسِخًا |
| R143 | 250 | applied | engine:AnEngine · I-1 (the light أَنْ) | أنّ المخففة: وجب بقاء عملها، ووجب حذف اسمها، ووجب كون خبرها جملة |
| R144 | 250 | applied | engine:AnEngine · I-1 | وإن كانت فعلية وجب كونها دعائية، أو كون الفعل جامدًا، أو مفصولًا بنفي أو شرط أو قد أو لو أ |
| R145 | 250 | noted | note:inna-wa-akhawatuha — ⚠ the engine still misreads the example: «كَأَنْ ظَبْيَةٌ تَعْطُو إِلَى وَارِقِ السَّلَمْ» → حرف لا محل له من الإعراب. | وَيَغْلِبُ لِكَأَنَّ مَا وَجَبَ لأَنَّ، إِلا أَنَّ الْفِعْلَ بَعْدَهَا دائمًا خَبَرِيٌّ مَ |
| R146 | 250 | noted | note:inna-wa-akhawatuha — ⚠ the engine still misreads the example: «وَلَكِنِ اللهُ قَتَلَهُمْ» → حرف لا محل له من الإعراب. | لكنْ المخففة يجب إلغاؤها؛ لزوال اختصاصها بالجمل الاسمية |
| R147 | 250 | applied | engine:Murib.line · lā's muḍāf ism (I-19) | وَإِنَما يَظْهَرُ نَصْبُهُ إنْ كَانَ مُضَافًا أَوْ شِبْهَهُ |
| R148 | 250 | applied | engine:Murib.line · the quasi-muḍāf | الشبيه بالمضاف ما اتصل به شيء من تمامه: مرفوع به أو منصوب به أو مخفوض بخافض متعلق به |
| R149 | 256 | applied | engine:Murib.line · لَنْ / كَيْ, note:nawasib-wa-jawazim-al-mudari | «لَنْ» أَوْ «كَي» المَصْدَرِيَّةُ مُطْلَقًا |
| R150 | 256 | noted | note:nawasib-wa-jawazim-al-mudari — ⚠ the engine still misreads the example: «جِئْتُ كَيْ تُكْرِمَنِي» → حرف لا محل له من الإعراب. | «كي» شرطها أن تكون مصدرية لا تعليلية؛ وتتعين المصدرية إذا تقدمتها اللام، والتعليلية إذا تأ |
| R151 | 256 | applied | engine:Murib.line, note:nawasib-wa-jawazim-al-mudari | «إذن» تنصب بثلاثة شروط: أن تكون مصدرة، وأن يكون الفعل مستقبلًا، وأن يكون متصلًا أو منفصلًا |
| R152 | 256 | applied | engine:AnEngine · I-1, note:an-masdariyya | «أن» تنصب بشرطين: أن تكون مصدرية لا زائدة ولا مفسرة، وألا تكون مخففة من الثقيلة |
| R153 | 256 | applied | engine:Murib.line, note:an-masdariyya | «أن» المفسرة بثلاثة شروط: أن يتقدم عليها جملة، فيها معنى القول دون حروفه، وألا يدخل عليها  |
| R154 | 259 | noted | note:an-masdariyya, note:nawasib-wa-jawazim-al-mudari — ⚠ the engine still misreads the example: «أَمْ حَسِبْتُمْ أَنْ تَدْخُلُوا الْجَنَّةَ» → فعل مضارع، مجزوم وعلامة جزمه حذف النون — بعامله، والواو ضمير | إذا سبقت «أن» بظن جاز الوجهان: الرفع على إجراء الظن مجرى العلم، والنصب على أصله، وهو الأرج |
| R155 | 259 | applied | engine:Murib.line · I-6 (the hidden أَنْ), note:nawasib-wa-jawazim-al-mudari | حتى: يشترط لإضمار أن بعدها أن يكون الفعل مستقبلًا بالنظر إلى ما قبلها، فإن لم يكن مستقبلًا |
| R156 | 259 | applied | engine:Murib.line · I-6, note:nawasib-wa-jawazim-al-mudari | النصب بعد حتى بأن مضمرة لا بحتى نفسها، خلافًا للكوفيين، ولا يجوز إظهار أن بعدها |
| R157 | 259 | applied | engine:Murib.line · I-6, note:lam-taleel, note:nawasib-wa-jawazim-al-mudari | اللام أربعة: التعليلية، ولام العاقبة، والزائدة بعد فعل متعد، ولام الجحود بعد كون ماض منفي؛ |
| R158 | 259 | applied | engine:Murib.line · I-6, note:nawasib-wa-jawazim-al-mudari | «أو» ينتصب المضارع بعدها بأن مضمرة وجوبًا إذا صح في موضعها «إلى» أو «إلا» |
| R159 | 259 | applied | engine:Murib.line · I-6, note:nawasib-wa-jawazim-al-mudari | الفاء والواو ينتصب بعدهما المضارع بشرطين: أن تكون الفاء للسببية والواو للمعية، وأن يكونا م |
| R160 | 259 | applied | engine:Murib.line · I-6, note:nawasib-wa-jawazim-al-mudari | الطلب يشمل الأمر والنهي والدعاء والعرض والتحضيض والتمني والاستفهام؛ فهذه سبعة مع النفي صار |
| R161 | 259 | noted | note:nawasib-wa-jawazim-al-mudari — ⚠ the engine still misreads the example: «مَا تَأْتِينِي فَأُكْرِمَكَ» → فعل ماض مبني للمجهول، مبني على الفتح، وفيه ضمير هو المفعول ب | «ما تأتيني فأكرمَك»: أربعة أوجه؛ الرفع على عطف اللفظ أو على الاستئناف، والنصب على أن النفي |
| R162 | 259 | applied | engine:Murib.line · I-6, note:nawasib-wa-jawazim-al-mudari | لو قلت «ما تأتينا إلا فتحدثنا» أو «ما تزال تأتينا فتحدثنا» وجب الرفع؛ لأن النفي انتقض بإلا |
| R163 | 259 | noted | note:nawasib-wa-jawazim-al-mudari | شرط النصب في جواب الأمر أن يكون بصيغة الطلب وألا يكون باسم الفعل؛ فلا يجوز «حسبك حديث فينا |
| R164 | 259 | noted | note:nawasib-wa-jawazim-al-mudari | شرط الاستفهام ألا يكون بأداة تليها جملة اسمية خبرها جامد؛ فلا يجوز النصب في «هل أخوك زيد ف |
| R165 | 259 | noted | note:nawasib-wa-jawazim-al-mudari | «ألم تر أن الله أنزل من السماء ماء فتصبحُ الأرض مخضرة» لم ينصب؛ لأن الاستفهام هنا معناه ال |
| R166 | 259 | noted | note:nawasib-wa-jawazim-al-mudari | «لولا أخرتني إلى أجل قريب فأصدق» من باب النصب في جواب الدعاء، لكن استعيرت فيه عبارة التحضي |
| R167 | 259 | applied | engine:Murib.line · I-6 (wāw al-maʿiyya), note:nawasib-wa-jawazim-al-mudari | «لا تأكل السمك وتشرب اللبن»: الجزم نهي عن كل منهما، والنصب نهي عن الجمع بينهما، والرفع على |
| R168 | 259 | noted | note:nawasib-wa-jawazim-al-mudari — ⚠ the engine still misreads the example: «وَمَا كَانَ لِبَشَرٍ أَنْ يُكَلِّمَهُ اللهُ إِلَّا» → فعل مضارع، منصوب وعلامة نصبه الفتحة الظاهرة، والفاعل ضمير مس | وينتصب الفعل المضارع بأن مضمرة جوازًا بعد الفاء وثم والواو وأو إذا عطفن على اسم صريح خالص  |
| R169 | 269 | not-automatable | «explicit noun» excludes a noun only implied (مَا يَكُونُ مِنْكَ إِتْيَانٌ) — a definition argued from meaning | قولي «اسم صريح» احتراز من نحو «ما تأتينا فتحدثنا»؛ فإن الاسم هناك ليس بصريح، فإضمار أن هنا |
| R170 | 269 | not-automatable | the three kinds of jarr (letter, annexation, adjacency) and «by following» is not a fourth — a classification | المجرورات ثلاثة: المجرور بالحرف، وبالإضافة، وبالمجاورة؛ ولم يذكر المجرور بالتبعية لأن العا |
| R171 | 269 | applied | engine:Murib.line · the jarr letters | من وإلى وعن وعلى والباء واللام وفي تجر الظاهر والمضمر؛ والكاف وحتى والواو لا تجر إلا الظاه |
| R172 | 269 | applied | engine:Nahw342Engine · qasam | التاء لا تجر إلا اسم الله، وربّ مضافًا إلى الكعبة أو إلى الياء |
| R173 | 269 | noted | note:huruf-jarr — ⚠ the engine still misreads the example: «عَمَّ يَتَسَاءَلُونَ» → اسم، مبني لا يتغير آخره. | كي لا تجر إلا «ما» الاستفهامية وأن المضمرة وصلتها؛ وما الاستفهامية إذا دخل عليها حرف جر حذ |
| R174 | 271 | not-automatable | مُذْ / مُنْذُ take a specific past or present time — the time's reference is meaning | مذ ومنذ لا يجران إلا اسم زمان معين ماض أو حاضر، لا مستقبلًا ولا مبهمًا |
| R175 | 271 | applied | engine:Murib.line | ربّ إن جرت ضميرًا فلا يكون إلا ضمير غيبة مفردًا مذكرًا، ويجب تفسيره بنكرة بعده مطابقة للمع |
| R176 | 271 | applied | engine:Nahw342Engine · rubba (offered) | وَيَجُوزُ حَذْفُها مَعَهُ، فَيَجِبُ بَقَاءُ عَمَلِهَا، وَذلِكَ بَعْدَ الْوَاوِ كَثِيرٌ، وَ |
| R177 | 271 | noted | note:hadhf-al-jarr — ⚠ the engine still misreads the example: «عَجِبْتُ أَنَّكَ فَاضِلٌ» → حرف لا محل له من الإعراب. | وَحَذْفُ اللَّامِ قَبْل كَي، وَخَافِضِ أَنْ وَأَنَّ مُطْلَقًا |
| R178 | 274 | noted | note:al-mudaf-wa-nawa-al-idafa — ⚠ the engine still misreads the example: «تَبَّتْ يَدَا أَبِي لَهَبٍ» → اسم، وعلامته مقدرة، مضاف إليه. | وَيُجَرَّدُ الْمُضَافُ مِنْ تَنْوِينٍ أَوْ نُونٍ تُشْبِهُهُ مُطْلَقًا |
| R179 | 274 | applied | engine:IdafaEngine · v332 I-5 | ويجرد من التعريف، فلا تقول: الغلامُ زيدٍ، ولا زيدُ عمرٍو مع بقاء زيد على تعريف العلمية، إل |
| R180 | 274 | applied | engine:Murib.line | وَإِذَا كَانَ الْمُضَافُ صِفَةً وَالْمُضَافُ إِلَيْهِ مَعْمُولًا لَهَا سُمِّيَتْ لَفْظِيَّ |
| R181 | 274 | not-automatable | «ضَارِبُ زَيْدٍ أَمْسِ» is pure annexation because the participle means the past — the time of the meaning | «ضاربُ زيدٍ أمسِ» إضافته محضة؛ لأن اسم الفاعل لا يعمل إذا كان بمعنى الماضي |
| R182 | 274 | not-automatable | غَيْر، مِثْل stay indefinite under annexation — a rank of meaning; the naʿt it allows is not a line change | إِلَّا إِذَا كَانَ الْمُضَافُ شَدِيدَ الإِبْهَامِ كَغَيْرٍ وَمِثْلٍ وَخِدْنٍ، أَوْ مَوْضِع |
| R183 | 280 | noted | note:jarr-al-jiwar | المعنوية مقدرة بفي إذا كان المضاف إليه ظرفًا للمضاف، وبمن إذا كان كلًّا له وصالحًا للإخبار |
| R184 | 280 | noted | note:jarr-al-jiwar — ⚠ the engine still misreads the example: «هَذَا جُحْرُ ضَبٍّ خَرِبٍ» → اسم، مجرور وعلامة جره الكسرة الظاهرة، نعت. | الثالثُ المَجرُورُ لِلْمُجَاوَرَةِ، وَهُوَ شَاذٌّ |
| R185 | 280 | noted | note:jarr-al-jiwar | ولَيْسَ مِنْهُ ﴿وَامْسَحُوا بِرُءُوسِكُمْ وَأَرْجُلِكُمْ﴾ عَلَى الأَصَحِّ |
| R186 | 284 | applied | engine:Murib.line · the jāzim of one verb, note:jawazim-al-mudari-wal-amr-fil-kafiya, note:nawasib-wa-jawazim-al-mudari | جازِمٌ لِفِعْلٍ، وَهُوَ: لَمْ، وَلَمَّا، وَلَامُ الأَمْرِ، وَلَا في النَّهْيِ |
| R187 | 284 | applied | engine:ShartEngine · I-7, note:in-shartiyya | إِنْ، وَإِذْ مَا، لمجرَّدِ التَّعْلِيقِ، وَهُما حَرْفَانِ |
| R188 | 284 | applied | engine:ShartEngine · I-7, note:in-shartiyya | وَمَنْ للِعَاقِلِ، وَمَا وَمَهْمَا لِغَيْرِهِ، وَمَتَى وأَيَّانَ لِلزَّمانِ، وَأَيْنَ وأَن |
| R189 | 284 | noted | note:al-majzum-wal-shart-wal-jaza | وَيُسَمَّى أَوَّلُهُمَا شَرْطا، وَلَا يكونُ ماضِيَ المَعْنَى، وَلَا إِنْشَاءً، وَلَا جَامِ |
| R190 | 286 | noted | note:al-fa-fi-jawab-al-shart — ⚠ the engine still misreads the example: «إِنْ كَانَ قَمِيصُهُ قُدَّ مِنْ قُبُلٍ فَصَدَقَتْ» → فعل ماض، مبني على الفتح، والفاعل ضمير مستتر جوازا تقديره «هي | وَقَدْ يَكُونُ وَاحِدًا مِنْ هذِهِ، فَيقْتَرِنُ بِالْفَاءِ |
| R191 | 286 | applied | engine:Murib.line, note:al-fa-fi-jawab-al-shart | «فلا يخافُ بخسًا» بالرفع: الفعل مبني على مبتدأ محذوف، والتقدير: فهو لا يخاف؛ ولولا ذلك لوج |
| R192 | 286 | applied | engine:Nahw342Engine · fujaa, note:al-fa-fi-jawab-al-shart | أَوْ جُمْلَةً اسْمِيَّةً فَيقْتَرِنُ بِهَا أَوْ بِإذَا الْفُجَائِيِّةِ |
| R193 | 289 | noted | note:al-majzum-wal-shart-wal-jaza | يجوز حذف الجواب بشرطين: أن يكون معلومًا، وأن يكون فعل الشرط ماضيًا |
| R194 | 289 | applied | engine:Sh336Engine · R194 (وَإِلَّا), note:al-majzum-wal-shart-wal-jaza | حذف فعل الشرط وحده شرطه دلالة الدليل عليه وكونه واقعًا بعد «وإلا»؛ وبغير «وإلا» شاذ إلا في |
| R195 | 289 | applied | engine:Murib.line · jawāb al-ṭalab, note:jawab-al-talab, note:nawasib-wa-jawazim-al-mudari | حذف أداة الشرط وفعله شرطه أن يتقدم عليهما طلب بلفظه ومعناه أو بمعناه فقط؛ ولا فرق بين كون  |
| R196 | 289 | noted | note:jawab-al-talab | وَشَرْطُ ذَلكَ بَعْدَ النَّهْيِ كَوْنُ الْجَوَابِ مَحْبُوبًا |
| R197 | 293 | noted | note:al-majzum-wal-shart-wal-jaza — ⚠ the engine still misreads the example: «هُوَ ظَالِمٌ إِنْ فَعَلَ» → فعل ماض، مبني على الفتح، والفاعل ضمير مستتر جوازا تقديره «هو | وَيَجِبُ الاسْتِغْنَاءُ عَنْ جَوَابِ الشَّرْطِ بِدَلِيلِهِ مُتَقَدِّمًا لَفْظًا … أو نيَّة |
| R198 | 293 | applied | engine:Murib.line · T3 (the oath's answer), note:al-majzum-wal-shart-wal-jaza | وَبِجَوَابِ ما تَقَدَّمَ مِنْ شَرْطٍ مُطْلَقًا، أوْ قَسَمٍ، إلا إِنْ سَبَقَهُ ذو خَبَرٍ، ف |
| R199 | 295 | applied | engine:Murib.line, note:al-majzum-wal-shart-wal-jaza | وَجَزْمُ مَا بَعْدَ فَاءٍ أَوْ واوٍ مِنْ فِعْلٍ تَالٍ لِلشّرْطِ أَوِ الْجَوَابِ قَوِيٌّ، و |
| R200 | 298 | applied | engine:Murib.line · I-2 | كلُّ الأَفْعَالِ تَرْفَعُ إمَّا الْفَاعِلَ أو نَائِبَهُ أو الْمُشَبّهَ به |
| R201 | 298 | applied | engine:MansubEngine · v332 I-9 | وتَنْصِبُ الأَسْمَاءَ إلا … الخَبرَ وَالتَّميِيزَ وَالْمَفعولَ الْمطلَقَ فَنَاصِبُها الوَص |
| R202 | 298 | applied | engine:LazimEngine · T4 | مَا لَا يَتَعَدَّى إليهِ أَصْلًا: كالدَّالِّ عَلى حُدُوثِ ذَاتٍ … أو صفةٍ حِسِّيَّةٍ … أوْ |
| R203 | 298 | applied | engine:Nahw342Engine · maful2 | احترزت بالحسية من نحو علم وفهم وفرح |
| R204 | 298 | applied | engine:DabtEngine valency | وما يَتعدَّى إلى واحِدٍ دائمًا بالجَارِّ … أو دائمًا بنفسِهِ … أو تارَةً وتارة … ومَا يتعد |
| R205 | 298 | noted | note:mafulayn — ⚠ the engine still misreads the example: «نَقَصْتُ زَيْدًا دِينَارًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، مفعول مطلق. | وما يتعدى إلى اثنين تارة ولا يتعدى إليهما أخرى كنَقَصَ وَزادَ |
| R206 | 298 | applied | engine:DabtEngine · two objects | أو يتعدى إليهما دائمًا: فإما ثانيهما كمفعول شكر، أو أولهما فاعل في المعنى كأعطى وكسا، أو أ |
| R207 | 298 | not-automatable | the heart verbs take two objects only in their heart senses (ظَنَّ not «suspect») — the sense decides | ظَنَّ، لَا بِمَعْنَى اتهم، وعلم لا بمعنى عَرَفَ، وَرَأَى لَا مِنَ الرَّأْيِ، وَوَجَدَ لَا  |
| R208 | 298 | applied | engine:Sh336Engine · R208 (ilghāʾ) | وَيَجُوزُ إِلْغَاءُ الْقَلْبِيَّةِ الْمُتَصَرِّفَةِ مُتَوَسِّطَةً أَوْ مُتَأَخِّرَةً |
| R209 | 298 | applied | engine:Sh336Engine · R209 (taʿlīq) | وَيَجِبُ تَعْلِيقُهَا قَبْلَ لَامِ الابْتِدَاءِ أو القَسَم، أوِ اسْتِفْهَامٍ، أَوْ نَفْيٍ  |
| R210 | 298 | noted | note:mafulayn — ⚠ the engine still misreads the example: «أَعْلَمْتُ زَيْدًا عَمْرًا فَاضِلًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، نعت. | وَمَا يَتَعَدَّى إلى ثَلَاثَةٍ، وَهُوَ أَعْلَمَ وَأَرَى وَمَا ضُمِّنَ مَعْنَاهُمَا مِنْ أَ |

## Qawāʿid al-Iʿrāb (Ibn Hishām)

Source: `research/sources/qawaid-al-irab-ibn-hisham-matn.txt`. Entries: 205 — applied **64**, noted **14**, not automatable **42**, open **30** (headings 14, lecture fragments 21, cited verses 20, counted apart).

| id | line | status | carried by / reason | the book |
|---|---|---|---|---|
| Q32 | 32 | not-automatable | the definition of kalām and jumla (what is «mufīd») — a definition the note anwa-al-jumal teaches; no line changes | اعلم أن اللفظ المفيد يُسَمَّى كلامًا وجملة، ونعني بالمفيدِ ما يَحْسُنُ السكوتُ عليه، وأما  |
| Q34 | 34 | not-automatable | a jumla that is not kalām (the condition and its answer) — the same definition, argued | ألا ترى أن نحو: قام زيدٌ من قولك: إن قام زيدٌ قام عمرٌو تسمى جملة؟، ولا تسمى كلامًا، لأنه  |
| Q36 | 36 | not-automatable | the clause named ismiyya / fiʿliyya / ẓarfiyya by what opens it — a classification; the reader does not print it on a word | ثم الجملةُ تسمى اسمية إن بُدئت باسمٍ، كزيدٌ قائمٌ، وإن زيدًا قائمٌ، وهل زيدٌ قائمٌ؟، وما ز |
| Q38 | 38 | not-automatable | the major and minor clause (زيدٌ أبوه غلامه منضبطٌ) — a classification of nested clauses | وإذا قيل: زيدٌ أبوه غلامه منضبطٌ |
| Q42 | 42 | not-automatable | لَكِنَّا = لَكِنْ أَنَا (the hamza dropped, the nūns merged) — an argued reading of one āya | ومثله: ﴿لَّٰكِنَّا۠ هُوَ ٱللَّهُ رَبِّى﴾   في الأصل هو: لكن أنا هو الله ربي، وإلا لقيل: لك |
| Q47 | 47 | applied | engine:JumlaMahallEngine · khabar | ، وجمل لها محل من الإعراب. وهي سبعٌ إحداها الواقعة خبرًا |
| Q49 | 49 | applied | engine:JumlaMahallEngine · khabar (mubtadaʾ, inna; kāna, kāda), note:anwa-al-jumal | إحداها واقعةٌ خبرًا، وموضعها رفعٌ في بابي المبتدأ، وإن نحو: زيدٌ قام أبوه، وإن زيدًا أبوه  |
| Q51 | 51 | applied | engine:JumlaMahallEngine · ḥāl (offered) | ومحلهما النصب. |
| Q53 | 53 | applied | engine:JumlaMahallEngine · maqūl, note:anwa-al-jumal | والمفعوليةُ تقع في أربعة مواضع، محكيةً بالقول نحو: قال: إني عبد الله، وثانيةً للمفعول الأو |
| Q55 | 55 | open | probe «ظَنَنْتُ زَيْدًا يَقْرَأُ» → فعل مضارع، مرفوع وعلامة رفعه الضمة الظاهرة، والفاعل ضمير مستتر جوازا ت | وثانيةً للمفعول الثاني في بابِ أعلمَ. |
| Q57 | 57 | applied | engine:JumlaMahallEngine · muḍāf ilayh | والرابعة … المضاف إليها ومحلها الجر. |
| Q59 | 59 | applied | engine:JumlaMahallEngine · muḍāf ilayh after إِذْ، إِذَا، حَيْثُ، لَمَّا | وكلُ جملةٍ وقعت بعد إذ، أو إذا، أو حيثُ، أو لما الوجودية، عند من قال باسميتها، أو بينما، أ |
| Q61 | 61 | applied | engine:JumlaMahallEngine · jawāb of a jāzim | والخامسةُ. الواقعة جوابًا لشرطٍ جازم. |
| Q63 | 63 | applied | engine:JumlaMahallEngine · jawāb with the fāʾ; Nahw342Engine · fujaa (the surprise إِذَا) | محلها الجزم إذا كانت مقرونةً بالفاء، أو بـ إذا الفجائية |
| Q65 | 65 | applied | engine:JumlaMahallEngine · jawāb with the fāʾ, note:al-fa-fi-jawab-al-shart, note:anwa-al-jumal, note:jawazim-al-mudari-wal-amr-fil-kafiya | في الأولى … نحو: ﴿مَن يُضْلِلِ ٱللَّهُ فَلَا هَادِيَ لَهُۥ ۚ وَيَذَرُهُمْ﴾  ، ﴿وَيَذَرُهُم |
| Q67 | 67 | noted | note:anwa-al-jumal — ⚠ the engine still misreads the example: «إِنْ قَامَ أَخُوكَ قَامَ عَمْرٌو» → فعل ماض، مبني على الفتح، وفاعله «عمرو»، والجملة جواب الشرط ل | فأما نحو: إن قام أخوك قامَ عمرٌو. |
| Q69 | 69 | open | probe «إِنْ قَامَ أَخُوكَ قَامَ عَمْرٌو» → فعل ماض، مبني على الفتح، وفاعله «أخوك». | وكذلك القول في فعل الشرط. |
| Q71 | 71 | noted | note:anwa-al-jumal — ⚠ the engine still misreads the example: «إِنْ قَامَا وَيَقْعُدَا أَخَوَاكَ» → اسم، وعلامته مقدرة، مفعول به. | ونحو ذلك: إن قاما ويقعدا أخواك. |
| Q73 | 73 | open | probe «إِنْ قَامَا وَيَقْعُدَا أَخَوَاكَ» → اسم، وعلامته مقدرة، مفعول به. | فإذا قلتَ إن قامَا ويقعدَا … فتجزمُ المعطوف قبل أن تكمل الجملة |
| Q75 | 75 | applied | engine:Murib.line | تنبيهٌ! إذا قلت: إن قامَ زيدٌ أقومُ. |
| Q80 | 80 | not-automatable | which is the answer in the verse (يَقُولُ, raised: the answer is «said» by an elided fāʾ, or it is the evidence of an elided answer) — the schools differ | فالجواب قيل. |
| Q82 | 82 | open | probe «إِنْ قَامَا وَيَقْعُدَا أَخَوَاكَ» → اسم، وعلامته مقدرة، مفعول به. | ويظهر أثر ذلك في التابع |
| Q84 | 84 | noted | note:anwa-al-jumal — ⚠ the engine still misreads the example: «مِنْ قَبْلِ أَنْ يَأْتِيَ يَوْمٌ لَا بَيْعٌ فِيهِ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة. | والسادسة … التابعة لمفرد … فالجملة المنعوت بها … فهي موضع رفعٍ في نحو: ﴿مِّن قَبْلِ أَن يَ |
| Q86 | 86 | noted | note:anwa-al-jumal — ⚠ the engine still misreads the example: «زَيْدٌ قَامَ أَبُوهُ وَقَعَدَ أَخُوهُ» → فعل ماض، مبني على الفتح، وفاعله «أخوه». | والسابعة … التابعة لجملة لها محل … نحو: زيدٌ قام أبوه وقعد أخوه. |
| Q88 | 88 | open | probe «زَيْدٌ قَامَ أَبُوهُ وَقَعَدَ أَخُوهُ» → فعل ماض، مبني على الفتح، وفاعله «أخوه». | ولو قدرت العطف على الجملةِ الاسميةِ لم يكن للمعطوفةِ محلٌ. |
| Q90 | 90 | open | probe «زَيْدٌ قَامَ أَبُوهُ وَقَعَدَ أَخُوهُ» → فعل ماض، مبني على الفتح، وفاعله «أخوه». | ولو قدرت الواوَ واوَ الحالِ؛ كانت الجملة في محل نصبٍ، وكانت قد فيها مضمرةً. |
| Q92 | 92 | applied | engine:JumlaMahallEngine · maqūl (the whole quote) | وإذا قلتَ: قال زيدٌ: عبد اللهِ منطلق وعمرٌو مقيمٌ، فليس من هذا القبيل، بل الَّذي محله النص |
| Q98 | 98 | open | probe «إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ» → حرف لا محل له من الإعراب. | إحداها المبتدأةُ. |
| Q102 | 102 | noted | note:anwa-al-jumal — ⚠ the engine still misreads the example: «إِنَّا أَعْطَيْنَاكَ الْكَوْثَرَ» → حرف لا محل له من الإعراب. | والابتدائية قد تكون في أول الكلام مطلقًا، مثل: إنا أعطيناك الكوثر، وقد تُسبق بكلامٍ سابق ل |
| Q104 | 104 | not-automatable | the clause is not the hurtful saying, so it is no maqūl — the sense of the āya decides | ولا يصح أن تكون محكيةً للقول الَّذي نُهي النبي ﷺ عن الحزن بسببه؛ لأنه ليس هو القول الَّذي  |
| Q106 | 106 | not-automatable | «لَا يَسَّمَّعُونَ» is a fresh start, not a naʿt or ḥāl of the indefinite before it — the sense decides | ونحو: ﴿لَّا يَسَّمَّعُونَ﴾ بعد: ﴿وَحِفْظًا مِّن كُلِّ شَيْطَٰنٍ مَّارِدٍ﴾  ، وليست صفةً لل |
| Q108 | 108 | applied | engine:Murib.line | وتقول: ما رأيته مذ يومان |
| Q110 | 110 | applied | engine:Murib.line | ونقول: ما لقيته منذ يومان: |
| Q120 | 120 | not-automatable | al-Zajjāj and Ibn Durustawayh put the clause after the ibtidāʾiyya حَتَّى in jarr — a view the matn reports and rejects | وعن الزجَّاجِ وابن ذو السري أن الجملة بعد حتى الابتدائية في موضع جر بـ حتى. |
| Q122 | 122 | not-automatable | the majority: a jarr letter is never suspended — the argument against the view above | وخالفهما الجمهور … لأن حروف الجر لا تُعَلق عن العمل. |
| Q124 | 124 | applied | engine:Murib.silaOf · ṣila, note:anwa-al-jumal | الثانيةً الواقعةَ صلةً لاسمٍ، نحو: جاء الَّذي قام أبوه، أو لحرفٍ نحو: عجبتُ مما قمتَ: أي م |
| Q128 | 128 | applied | engine:JumlaMahallEngine · muʿtariḍa | الثالثة: … المعترضة اللفظ بين شيئين، في التسديد أو في التبيين. |
| Q132 | 132 | not-automatable | more than one clause may come between (against Abū ʿAlī) — the extent of an aside is the sense | ويجوز الاعتراض من أكثر من جملةٍ واحدةٍ خلافًا لأبي علي. |
| Q134 | 134 | not-automatable | the matn rejects al-Zamakhsharī's reading of one āya as an aside — an argued case | وليس منه هذه الآية، خلافًا للزمخشري، ذكره في سورة آل عمران. |
| Q138 | 138 | applied | engine:Murib.line | الرابعة … التفسيرية، وهي الكاشفة لحقيقة ما تليه وليست عمدةً. |
| Q140 | 140 | not-automatable | «and some say: a badal of it» — a reported view | وقيل: بدلًا منها. |
| Q142 | 142 | not-automatable | «مَسَّتْهُمُ الْبَأْسَاءُ» explains «مَثَلُ الَّذِينَ خَلَوْا» — which clause a tafsīriyya explains is meaning | ونحو: ﴿مَّسَّتْهُمُ ٱلْبَأْسَآءُ وَٱلضَّرَّآءُ﴾   فإنه تفسير لـ: ﴿مَّثَلُ ٱلَّذِينَ خَلَوْ |
| Q144 | 144 | noted | note:anwa-al-jumal | ونحو: ﴿كَمَثَلِ ءَادَمَ ۖ خَلَقَهُۥ مِن تُرَابٍ ثُمَّ قَالَ لَهُۥ كُن فَيَكُونُ﴾  . |
| Q146 | 146 | not-automatable | «تُؤْمِنُونَ» explains «تِجَارَةٍ» — meaning | ونحو: ﴿تُؤْمِنُونَ بِٱللَّهِ وَرَسُولِهِۦ﴾ بعد: ﴿هَلْ أَدُلُّكُمْ عَلَىٰ تِجَٰرَةٍ تُنجِيك |
| Q148 | 148 | not-automatable | «and some say a fresh start meaning «believe», shown by the jazm of يَغْفِرْ» — a reported view | وقيل: مستأنفة، بمعنى آمنوا، بدليل: يغفر لكم بالجزم. |
| Q156 | 156 | applied | engine:Murib.line | وكون الجملة المفسرة لا محل لها هو المشهور. |
| Q160 | 160 | applied | engine:Murib.line | فلا محل للجملة المقدرة. |
| Q164 | 164 | not-automatable | «فَخَلَقْنَاهُ» explains the elided «خَلَقْنَا» — an elided verb restored from meaning | فخلقناه المذكورة مفسرةٌ لـ خلقنا المقدرة. |
| Q166 | 166 | noted | note:anwa-al-jumal — ⚠ the engine still misreads the example: «زَيْدٌ الْخُبْزَ يَأْكُلُهُ» → فعل مضارع، مرفوع وعلامة رفعه الضمة الظاهرة، وفيه ضمير هو الم | ومن ذلك: زيدٌ الخبزَ يأكلَه. |
| Q180 | 180 | applied | engine:WujuhEngine · إِذْ ẓarf | إحداها (إذ) … ظرف لما مضى من الزمان. |
| Q182 | 182 | applied | engine:JumlaMahallEngine · إِذْ annexed to both clauses | ويدخل على الجملتين |
| Q184 | 184 | not-automatable | إِذْ for the future (يَعْلَمُونَ إِذِ الْأَغْلَالُ) — the time is the sense of the āya, the ẓarf is the same | وقد تستعمل للمستقبل. |
| Q188 | 188 | applied | engine:WujuhEngine · إِذْ of surprise | حرف مفاجأة كقوله: |
| Q191 | 191 | open | probe «WujuhEngine.table("وَلَنْ يَنْفَعَكُمُ الْيَوْمَ إِذْ ظَلَمْ» → false | وتارةً حرف تعليل |
| Q195 | 195 | applied | engine:WujuhEngine · لَمَّا of existence | الثانية: (لَمَّا): يقال فيها في نحو: لما جاء زيدٌ جاء  : حرف وجودٍ لوجود … وتختص بالماضي |
| Q197 | 197 | not-automatable | al-Fārisī's view that لَمَّا is a ẓarf — named beside the letter in the clause line (offered), a school view | وزعم الفارسي ومتابعوه أنها ظرفٌ بمعنى حينٍ |
| Q199 | 199 | applied | engine:WujuhEngine · لَمَّا jāzima | ويقال فيها بنحو: ﴿لَّمَّا يَذُوقُوا۟ عَذَابِ﴾  : حرف جزمٍ لنفي المضارع، وقلبه ماضيًا متصلا |
| Q201 | 201 | noted | note:anwa-ma — ⚠ the engine still misreads the example: «WujuhEngine.table("أنشدك الله لما فعلت").items.som» → false | ويقال فيها: حرف استثناء، في نحو: أنشدك الله لما فعلت، أي: ما أسألك إلا فعلك. ومنه: ﴿إِن كُ |
| Q203 | 203 | not-automatable | the meaning «no soul but has a keeper» proves the exceptive لَمَّا; al-Jawharī's denial is set aside — an argument | ألا يُرى أن المعنى: ما كل نفسٍ إلا عليها حافظ؟ ولا التفات إلى إنكار الجوهري ذلك. |
| Q205 | 205 | applied | engine:WujuhEngine · نَعَمْ (taṣdīq, iʿlām, waʿd) | نعم: فيقال فيها حرف تصديقٍ، إذا وقعت بعد الخبر، نحو: قام زيدٌ، أو ما قام زيدٌ. وحرف إعلامٍ |
| Q207 | 207 | open | engine to build: WujuhEngine · نَعَمْ of iʿlām — probe «WujuhEngine.table("فَهَلْ وَجَدْتُمْ مَا وَعَدَ رَبُّكُمْ حَ» → false | ومن مجيئها للإعلام: ﴿فَهَلْ وَجَدتُّم مَّا وَعَدَ رَبُّكُمْ حَقًّا ۖ قَالُوا۟ نَعَمْ﴾  . |
| Q209 | 209 | not-automatable | «Sībawayh did not note this sense» — a remark on the history of the doctrine | وهذا المعنى لم ينبه عليه سيبويه |
| Q211 | 211 | open | probe «WujuhEngine.WORDS.iy.n === 3» → false | الرابعة: إِيْ: بكسر الهمزة وسكون الياء، وهي بمنزلة (نعم) … تكون لتصديق المخبر، وإعلام المس |
| Q215 | 215 | applied | engine:Murib.line · حَتَّى jārra | حتى: فأحد أوجهها أن تكون جارةً. |
| Q217 | 217 | applied | engine:Murib.line · I-6 (حَتَّى + the hidden أَنْ) | وعلى الاسم المؤول من (أن) مضمرةً، ومن الفعل المضارع، فتكون تارةً بمعنى (إلى) ﴿حَتَّىٰ يَرْ |
| Q219 | 219 | not-automatable | حَتَّى may bear both senses (to / so that) — the sense decides | وقد تحتملهما |
| Q221 | 221 | not-automatable | Ibn Hishām al-Khaḍrāwī and Ibn Mālik add حَتَّى = إِلَّا (an exception) — a reported view on one verse | وزعم ابن هشام الخضراوي، وابن مالك |
| Q226 | 226 | open | probe «قَهَرْنَاكُمُ حَتَّى الْكُمَاةَ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | والثاني: أن تكون حرف عطف. |
| Q231 | 231 | open | probe «WujuhEngine.table("وَمَا زَالَتِ الْقَتْلَى تَمُجُّ دِمَاءَه» → false | فتدخل على ثلاثة أشياء:   الفعل الماضي: نحو: ﴿حَتَّىٰ عَفَوا۟ وَّقَالُوا۟﴾  . والمضارع المر |
| Q233 | 233 | not-automatable | «some say: with the māḍī it is jārra and أَنْ is hidden» — a reported view | وقيل: هي مع الماضي جارة، و(أن) بعدها مضمرة. وقد مضى خلاف الزجَّاج وابن درستويه فيهن. |
| Q235 | 235 | applied | engine:WujuhEngine · كَلَّا of deterrence | السادسة (كلا)، ويقال فيها حرف ردعٍ وزجرٍ، بنحو: ﴿وَأَمَّآ إِذَا مَا ٱبْتَلَىٰهُ فَقَدَرَ ع |
| Q237 | 237 | open | probe «WujuhEngine.table("كَلَّا وَالْقَمَرِ").items.some(x => x.ke» → false | وحرف جواب وتصديق، في نحو: ﴿كَلَّا وَٱلْقَمَرِ﴾  .   والمعنى: أي والقمر |
| Q239 | 239 | applied | engine:WujuhEngine · كَلَّا = أَلَا | وبمعنى (حقًّا) أو (ألا) الاستفتاحية، على خلافٍ في ذلك. نحو: ﴿كَلَّا لَا تُطِعْهُ﴾ |
| Q241 | 241 | applied | engine:WujuhEngine · كَلَّا = أَلَا (the kasra of إِنَّ after it) | والصواب الثاني …   لكسر الهمزة في نحو: ﴿كَلَّآ إِنَّ ٱلْإِنسَٰنَ لَيَطْغَىٰٓ﴾  . |
| Q243 | 243 | applied | engine:WujuhEngine · لَا (nāfiya, nāhiya, zāʾida) | السابعة: (لا): فتكون نافيةً وناهيةً وزائدةً. |
| Q250 | 250 | applied | engine:Murib.line · lā al-nāhiya | والناهية تجزم المضارع، نحو: ﴿وَلَا تَمْنُن تَسْتَكْثِرُ﴾  ، ﴿فَلَا يُسْرِف فِّى ٱلْقَتْلِ﴾ |
| Q258 | 258 | applied | engine:WujuhEngine · لَوْلَا of imtināʿ | فيقال فيها تارةً: حرفٌ يقتضي امتناع جوابه لوجود شرطه. |
| Q260 | 260 | open | probe «WujuhEngine.table("لولاي لكان كذا").items.some(x => x.key ==» → false | ومنه: لولاي لكان كذا، أي: لولا أنا موجودٌ. |
| Q262 | 262 | applied | engine:WujuhEngine · لَوْلَا of urging | وتارةً … وتارةً حرف تحضيضٍ وعرضٍ، أي: طلبٌ بإزعاجٍ أو برفقٍ. |
| Q264 | 264 | not-automatable | in the first āya it is ʿarḍ, in the second taḥḍīḍ — the gentleness or force of the asking is sense | والظاهر أنها في الأولى للعرض، وفي الثانية للتحضيض. |
| Q270 | 270 | not-automatable | the readings of Ubayy and Ibn Masʿūd («فَهَلَّا») support the reading — qirāʾa evidence | ويؤيده … أن في حرف أُبيٍّ وعبد الله بن مسعود: «فهلا»، ويلزم من ذلك معنى النفي الذي ذكره ال |
| Q272 | 272 | applied | engine:WujuhEngine · إِنْ shart | الثانية: (إن) المكسورة الخفيفة، فيقال فيها: شرطية، في نحو: ﴿إِن تُخْفُوا۟ مَا فِى صُدُورِك |
| Q274 | 274 | open | engine to build: WujuhEngine · إِنْ nāfiya — probe «WujuhEngine.table("إِنْ عِنْدَكُمْ مِنْ سُلْطَانٍ بِهَذَا").» → false | ونافية، في نحو: ﴿إِنْ عِندَكُم مِّن سُلْطَٰنٍۭ بِهَٰذَآ﴾  . |
| Q276 | 276 | noted | note:in-shartiyya — ⚠ the engine still misreads the example: «WujuhEngine.table("إن أحدٌ خيرًا من أحدٍ إلا بالعا» → false | وأهل العالية … وأهل العالية يعملونها عمل ليس، نحو قول بعضهم: إن أحدٌ خيرًا من أحدٍ إلا بال |
| Q280 | 280 | open | engine to build: Sh336Engine · R141 (إِنْ mukhaffafa) — probe «WujuhEngine.table("وَإِنْ كُلًّا لَمَّا لَيُوَفِّيَنَّهُمْ")» → false | ومخففة من الثقيلة في نحو: ﴿وَإِنَّ كُلًّا لَّمَّا لَيُوَفِّيَنَّهُمْ﴾   في قراءة من خفف ال |
| Q282 | 282 | applied | engine:Sh336Engine · R141 (the working mukhaffafa) | ويقل إعمالها عمل المشددة، كهذه القراءة. |
| Q284 | 284 | applied | engine:WujuhEngine · إِنْ zāʾida | وزائدة، في نحو: ما إن زيدٌ قائمٌ، وحيث اجتمعت (ما) و(إن)، فإن تقدمت (ما) فهي نافية، و(إن)  |
| Q286 | 286 | applied | engine:AnEngine · أَنْ maṣdariyya | والثالثة: (أن) المفتوحة الخفيفة، ويقال فيها: حرفٌ مصدريٌّ ينصب المضارع، نحو: ﴿يُرِيدُ ٱللَ |
| Q288 | 288 | applied | engine:WujuhEngine · أَنْ zāʾida after لَمَّا | وزائدة، في نحو: ﴿فَلَمَّآ أَن جَآءَ ٱلْبَشِيرُ﴾  . وكذا حيث جاءت بعد (لَمَّا). |
| Q292 | 292 | applied | engine:WujuhEngine · أَنْ mufassira | ومفسِّرَة، في نحو: ﴿فَأَوْحَيْنَآ إِلَيْهِ أَنِ ٱصْنَعِ ٱلْفُلْكَ﴾  . |
| Q294 | 294 | applied | engine:WujuhEngine · the conditions of the tafsīriyya (QAWL_SENSE) | وكذلك حيث وقعت بعد جملةٍ فيها معنى القول، دون حروفه، ولم تقترن بخافض |
| Q296 | 296 | applied | engine:AnEngine · I-1 (not tafsīriyya: no clause of saying before it) | فليس منها: ﴿وَءَاخِرُ دَعْوَىٰهُمْ أَنِ ٱلْحَمْدُ لِلَّهِ﴾   … لأن المقدم عليها غير جملة |
| Q298 | 298 | not-automatable | «كَتَبْتُ إِلَيْهِ بِأَنِ افْعَلْ» — the jarr letter makes it maṣdariyya; the edition's vowelling of the example is unsure (v334-N2) | ولا نحو: كتبت إليه بأن افعل |
| Q300 | 300 | not-automatable | the scholars' reading of «مَا قُلْتُ لَهُمْ إِلَّا مَا أَمَرْتَنِي بِهِ أَنِ اعْبُدُوا اللهَ» — an argued case | وقول بعض العلماء في قوله تعالى: ﴿مَا قُلْتُ لَهُمْ إِلَّا مَآ أَمَرْتَنِى بِهِۦٓ أَنِ ٱعْب |
| Q302 | 302 | not-automatable | al-Zamakhsharī allows it if «قُلْتُ» is read as «أَمَرْتُ» — a reported view | وجوز الزمخشري إن أُوِّلَ (قلتُ) بـ (أمرتُ) … وجوز مصدريتها |
| Q304 | 304 | not-automatable | the maṣdar as a bayān of the hā', not a badal — an argued case | على أن المصدر بيانٌ للهاء … لا بدل … لأن تقدير إسقاط الضمير، يخلي الصلة من عائد |
| Q312 | 312 | applied | engine:AnEngine · I-1 (أَنْ mukhaffafa after a verb of knowing) | في ﴿عَلِمَ أَن سَيَكُونُ﴾  ، ﴿وَحَسِبُوٓا۟ أَلَّا تَكُونَ﴾   في قراءةِ الرفعِ، وكذا حيثُ و |
| Q314 | 314 | applied | engine:WujuhEngine · مَنْ (shart, mawṣūl, istifhām), note:in-shartiyya | فتكون شرطيةً في نحو: ﴿من يعمل سوءا يجز به﴾  . وموصولةً، في نحو: ﴿وَمِنَ ٱلنَّاسِ مَن يَقُو |
| Q316 | 316 | noted | note:hal-ma-man — ⚠ the engine still misreads the example: «WujuhEngine.table("مررتُ بِمَنْ مُعجِبٍ لك").items» → false | ونكرةً موصوفة … في: مررتُ بِمَنْ مُعجِبٍ لك |
| Q318 | 318 | open | probe «WujuhEngine.table("مررتُ بِمَنْ مُعجِبٍ لك").items.some(x =>» → false | مررتُ بمن مُعْجِبٍ لك، يعني بإنسانٍ معجبٍ لك |
| Q320 | 320 | not-automatable | al-Fārisī allows مَنْ as a complete indefinite (وَنِعْمَ مَنْ هُوَ) — a reported view | وأجاز الفارسيُّ أن تقع نكرةً تامة … حَمَلَ عليه قوله |
| Q325 | 325 | applied | engine:WujuhEngine · أَيّ (shart, istifhām, nidāʾ) | أَي، فتقعُ شرطيةً، نحو: ﴿أَيَّمَا ٱلْأَجَلَيْنِ قَضَيْتُ فَلَا عُدْوَٰنَ عَلَىَّ﴾  .   واس |
| Q327 | 327 | open | probe «ثُمَّ لَنَنْزِعَنَّ مِنْ كُلِّ شِيعَةٍ أَيُّهُمْ أَشَدُّ» → اسم، والضمير مضاف إليه. | أي: الذي هو أشدُّ |
| Q329 | 329 | not-automatable | «said by Sībawayh and those who follow him» — the attribution | قاله سيبويه ومن تابعه |
| Q331 | 331 | not-automatable | those who say the relative is never built read أَيُّهُمْ as an interrogative mubtadaʾ — a reported view | وقال من رأى أن الموصولةَ لا تُبنى: هي هنا استفهاميةٌ مبتدأ، و﴿أَشَدُّ﴾: خَبَرُه. |
| Q333 | 333 | applied | engine:WujuhEngine · لَوْ of imtināʿ | لو … أن تكون حرف شرطٍ… يقتضى امتناع ما يليه، واستلزامه لتاليه |
| Q335 | 335 | applied | engine:WujuhEngine · لَوْ in the past | وأحدُ أوجهها: أن تكونَ حرفَ شرطٍ في الماضي فيقال فيها |
| Q337 | 337 | not-automatable | «لَمْ يَعْصِهِ» does not fall with «لَمْ يَخَفْ» — the logic of لَوْ, argued | لأنه لا يلزمُ من انتفاءِ (لم يخف) انتفاءُ (لم يعصِ). |
| Q339 | 339 | applied | engine:WujuhEngine · لَوْ of the future | أن تكونَ حرفَ شرطٍ في المستقبل. |
| Q341 | 341 | applied | engine:WujuhEngine · لَوْ of the future | فيقال فيها: حرفُ شرط مرادفٌ لـ(إن)، إلا أنها لا تجزم …   كقوله تعالى: ﴿وَلْيَخْشَ ٱلَّذِين |
| Q345 | 345 | applied | engine:WujuhEngine · لَوْ maṣdariyya | أن تكون حرفًا مصدريًا مرادفًا لـ (أَنْ) |
| Q347 | 347 | applied | engine:WujuhEngine · لَوْ maṣdariyya after وَدَّ | إلا أنها لا تنصب، وأكثر وقوعها بعد (وَدَّ) |
| Q349 | 349 | not-automatable | «most do not accept this kind» — a report of the schools | وأكثرهم لا يُثْبِتُ هذا القسم |
| Q351 | 351 | not-automatable | they read the āya with the verb's object and the answer dropped — a reported view | ويُخَرِّجُ الآيةَ ونحوها على حذفِ مفعول الفعلِ قبلها، والجوابِ بعدها |
| Q353 | 353 | applied | engine:WujuhEngine · لَوْ of wishing | أن تكون للتمني بمنزلة (ليت)، إلا أنها لا تنصبُ ولا ترفع، نحو: ﴿فَلَوْ أَنَّ لَنَا كَرَّةً  |
| Q358 | 358 | noted | note:insha-wa-tamanni — ⚠ the engine still misreads the example: «WujuhEngine.table("لو تَنْزِلُ عندنا فتُصيبَ راحةً» → false | أن تكونَ للعرض … نحو: لو تَنْزِلُ عندنا فتُصيبَ راحةً … ذكره في التسهيل. |
| Q360 | 360 | applied | engine:WujuhEngine · لَوْ of rarity (Ibn Hishām al-Lakhmī) | وذكرَ لها ابنُ هشامٍ اللخميُّ معنىً آخر |
| Q364 | 364 | applied | engine:WujuhEngine · قَدْ ism / ism fiʿl | تكونُ اسمًا بمعنى (حَسْبُ)، واسمَ فعلٍ بمعنى (يكفي)، |
| Q366 | 366 | applied | engine:Murib.line | فأحدُ أوجهها أن تكونَ اسمًا بمعنى (حَسْب)، فيقال: (قَدِي) بغيرِ نونٍ، كما يقال: حسبي. |
| Q368 | 368 | applied | engine:WujuhEngine · قَدْنِي | أن تكونَ اسمَ فعلٍ بمعنى (يكفي)، فيقال: (قَدْنِي)، كما يقال: يكفيني. |
| Q371 | 371 | open | probe «WujuhEngine.table("قد يخرُجُ زيدٌ").items.some(x => x.key ==» → false | أن تكون حرفَ توَقُّع |
| Q373 | 373 | noted | note:qad-harf — ⚠ the engine still misreads the example: «WujuhEngine.table("قد يخرُجُ زيدٌ").items.some(x =» → false | فتدخل عليهما أيضًا … فتقول: قد يخرُجُ زيدٌ |
| Q375 | 375 | applied | engine:WujuhEngine · قَدْ of nearness | تقريب الماضي من الحال |
| Q380 | 380 | not-automatable | al-Zamakhsharī on «لَقَدْ أَرْسَلْنَا نُوحًا» — a reported view | وزعم الزمخشري عندما تكلم على قوله تعالى: ﴿لَقَدْ أَرْسَلْنَا نُوحًا إِلَىٰ قَوْمِهِۦ﴾  ؛ أ |
| Q382 | 382 | applied | engine:WujuhEngine · قَدْ of rarity | التقليل، وهو ضربان: تقليل وقوع الفعل، نحو: قد يصدُق الكذوب، وقد يجودُ البخيل، وتقليلُ متعَ |
| Q384 | 384 | not-automatable | «some say it is of certainty there» — a reported view | وزعم بعضهم أنها في ذلك للتحقيق كما تقدم، وأن التقليل في المثالين الأولين لم يُستَفَد من (ق |
| Q386 | 386 | open | probe «WujuhEngine.table("قَدْ أَتْرُكُ الْقِرْنَ مُصْفَرًّا أَنَام» → false | التكثير، قاله سيبويه في قوله: |
| Q391 | 391 | applied | engine:WawEngine · the two wāws of rafʿ (istiʾnāf, ḥāl) | وذلك أنَّ لنا واوينِ يرتفعُ ما بَعدَهُما: |
| Q393 | 393 | noted | note:anwa-al-waw — ⚠ the engine still misreads the example: «WujuhEngine.table("صِرتُ والنيلَ").items.some(x =>» → false | وواوين ينتصبُ ما بعدهما؛ وهما واو المفعولِ معه، نحو: صِرتُ والنيلَ |
| Q395 | 395 | open | probe «WujuhEngine.table("لَا تَنْهَ عَنْ خُلُقٍ وَتَأْتِيَ مِثْلَه» → false | وواو الجمعِ … الداخلة على المضارع المسبوق بنفيٍ أو طلب، نحو: ﴿وَلَمَّا يَعْلَمِ ٱللَّهُ ٱل |
| Q400 | 400 | open | probe «WujuhEngine.table("وَالتِّينِ وَالزَّيْتُونِ").items.some(x » → false | وواوين ينجرُ ما بعدَهُما، وهما: واو القسم، نحو: ﴿وَٱلتِّينِ وَٱلزَّيْتُونِ﴾   … وواو رُبَّ |
| Q403 | 403 | applied | engine:WawEngine · ʿaṭf | وواوًا يكون ما بعدها على حسبِ ما قبلها، وهي واو العطف. |
| Q405 | 405 | not-automatable | the extra wāw (حَتَّى إِذَا جَاءُوهَا وَفُتِحَتْ) — whether the answer is dropped or the wāw extra is argued | وواوًا يكون دخولها في الكلامِ كخروجها، وهي الواو الزائدة. |
| Q407 | 407 | not-automatable | «some say: joining, the answer dropped» — a reported view | وقيل: إنها عاطِفةٌ، والجواب محذوف، والتقدير: كان كيت وكيت. |
| Q409 | 409 | not-automatable | «the wāw of eight» — named only to be rejected | وقولُ جماعةٍ: إنها واو الثمانية |
| Q415 | 415 | open | engine to build: MaEngine · مَا maʿrifa tāmma — probe «نِعْمَ مَا صَنَعْتَ» → اسم، مبني لا يتغير آخره. | فإنها على ضربين: اسمية، وأوجهها سبعة: معرفة تامة |
| Q417 | 417 | open | engine to build: MaEngine · مَا mawṣūla — probe «مَا عِنْدَ اللهِ خَيْرٌ» → حرف لا محل له من الإعراب. | ومعرفةٌ ناقصةٌ، وهي الموصولة … نحو: ﴿مَا عِندَ ٱللَّهِ خَيْرٌ مِّنَ ٱللَّهْوِ وَمِنَ ٱلتِّ |
| Q419 | 419 | applied | engine:MaEngine · مَا shartiyya, note:in-shartiyya | وشرطية، نحو: ﴿وَمَا تَفْعَلُوا۟ مِنْ خَيْرٍ يَعْلَمْهُ ٱللَّهُ﴾  . واستفهامية، نحو: ﴿وَمَا |
| Q421 | 421 | applied | engine:Sh336Engine · R42 (لِمَاذَا) | وإنما جاز نحو: لماذا فعلتَ؟، بأن ألفها صارت حشوًا في التركيب مع ذا، فأشبهت المنصوب له. |
| Q423 | 423 | open | probe «فَنِعِمَّا هِيَ» → اسم، مبني لا يتغير آخره. | ونكرةٌ تامةٌ … وذلك في ثلاثة مواضع، في كل منها خلاف: أحدها: نحو: ﴿فَنِعِمَّا هِىَ﴾   … ونح |
| Q427 | 427 | not-automatable | «إِنِّي مِمَّا أَنْ أَفْعَلَ» — the second place of the complete indefinite, a reported idiom | والثاني، مما تكون فيه (ما) نكرةً تامةً، قولهم: إني   أن أفعل. |
| Q431 | 431 | applied | engine:Murib.line | والثالث: قولهم في التعجب: ما أحسن زيدًا!، أي: شيءٌ حسَّنَ زيدًا، هذا قول سيبويه. |
| Q433 | 433 | applied | engine:MaEngine · مَا nakira mawṣūfa | ونكرة موصوفة |
| Q435 | 435 | noted | note:anwa-ma | ومنه – في قولٍ –: نعم ما صنعتَ، أي: نعم شيئًا صنعتَه. وما أحسن زيدًا! أي: شيءٌ موصوفٌ بأنه |
| Q437 | 437 | open | probe «لِأَمْرٍ مَا جَدَعَ قَصِيرٌ أَنْفَهُ» → حرف لا محل له من الإعراب. | ونكرةٌ موصوفٌ بها |
| Q439 | 439 | open | engine to build: MaEngine · مَا maṣdariyya — probe «بِمَا نَسُوا يَوْمَ الْحِسَابِ» → حرف لا محل له من الإعراب. | وتأتي حرفيةً، وأوجهها خمسة: مصدرية غير ظرفية: نحو: ﴿بِمَا نَسُوا۟ يَوْمَ ٱلْحِسَابِ﴾  ،    |
| Q441 | 441 | open | engine to build: MaEngine · the kāffa — probe «إِنَّمَا اللهُ إِلَهٌ وَاحِدٌ» → حرف لا محل له من الإعراب. | وكافة عن العمل: وهي ثلاثة أقسام: |
| Q443 | 443 | open | probe «وَقَلَّمَا وِصَالٌ عَلَى طُولِ الصُّدُودِ يَدُومُ» → حرف لا محل له من الإعراب. | كافة عن عمل الرفع، كقوله: |
| Q448 | 448 | applied | engine:Murib.line · the kāffa on إِنَّ | وكافةٌ عن عمل النصب والرفع، وذلك في (إن) وأخواتها، نحو: ﴿إِنَّمَا ٱللَّهُ إِلَٰهٌ وَٰحِدٌ﴾ |
| Q453 | 453 | open | engine to build: MaEngine · مَا zāʾida — probe «فَبِمَا رَحْمَةٍ مِنَ اللهِ لِنْتَ لَهُمْ» → حرف لا محل له من الإعراب. | وزائدة: وتسمى هي وغيرها من الحروف الزائدة صلةً وتوكيدًا، نحو: ﴿فَبِمَا رَحْمَةٍ مِّنَ ٱللَ |

### Bāb 3 word by word — the matn's count of faces against `WujuhEngine.WORDS`

| word | matn lines | faces the matn states | engine n | engine faces | matn examples read right / tried |
|---|---|---:|---:|---|---|
| إِذْ | 176–193 | 3 | 3 | zarf, mufajaa, talil | 2 / 3 (talil not yet) |
| لَمَّا | 195–203 | 3 | 3 | hiniyya, jazima, istithna | 3 / 3  |
| نَعَمْ | 205–209 | 3 | 3 | tasdiq, wad, ilam | 3 / 3  |
| إِي | 211 | 3 | 1 ≠ | qasam | 1 / 1  |
| حَتَّى | 213–233 | 3 | 4 ≠ | jarr, nasb, atf, ibtida | 0 / 1 (ibtida not yet) |
| كَلَّا | 235–241 | 3 | 3 | rad, tasdiq, istiftah | 2 / 3 (tasdiq not yet) |
| لَا | 243–250 | 3 | 3 | nafiya, nahiya, zaida, jins, atifa, jawab | 2 / 2  |
| لَوْلَا | 254–270 | 4 | 4 | imtinaWujud, ard, tawbikh, nafy | 2 / 2  |
| إِنْ | 272–284 | 4 | 4 | shart, nafiya, mukhaffafa, zaida | 2 / 4 (nafiya, mukhaffafa not yet) |
| أَنْ | 286–312 | 4 | 4 | masdariyya, mukhaffafa, tafsiriyya, zaida | 3 / 3  |
| مَنْ | 314–321 | 4 | 4 | shart, mawsul, istifham, mawsufa | 2 / 3 (mawsufa not yet) |
| أَيّ | 323–331 | 5 | 5 | shart, istifham, mawsul, kamal, nida, tafsir | 2 / 2  |
| لَوْ | 333–360 | 5 | 5 | imtina, mustaqbal, masdariyya, tamanni, taqlil | 5 / 6 (ard not yet) |
| قَدْ | 362–387 | 7 | 7 | ism, ismFil, tahqiq, tawaqqu, taqrib, taqlil, takthir | 4 / 6 (tawaqqu, takthir not yet) |
| الْوَاو | 389–411 | 8 | 8 | istinaf, hal, atf, maiyya, jam, qasam, rubba, zaida | 0 / 4 (maiyya, jam, qasam, rubba not yet) |
| مَا | 413–453 | 12 | 12 | mawsula, shartiyya, istifham, taajjub, mawsufa, nakira, nafiya, hijaziyya, masdariyya, zarfiyya, kaffa, zaida | 0 / 0  |

## Iẓhār al-Asrār (Birgivī)

Source: `research/sources/izhar-al-asrar-matn-lithograph.txt`. Entries: 163 — applied **128**, noted **20**, not automatable **5**, open **10** (headings 0, lecture fragments 0, cited verses 0, counted apart).

| id | line | status | carried by / reason | the book |
|---|---|---|---|---|
| I-A01 | 13 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والعامل في اسم واحد حروف تجره تسمى حروف الجر وحروف الإضافة وهي عشرون: الباء للإلصاق، ومن ل |
| I-A02 | 13 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والعامل في اسم واحد حروف تجره تسمى حروف الجر وحروف الإضافة وهي عشرون: الباء للإلصاق، ومن ل |
| I-A03 | 13 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والعامل في اسم واحد حروف تجره تسمى حروف الجر وحروف الإضافة وهي عشرون: الباء للإلصاق، ومن ل |
| I-A04 | 13 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والعامل في اسم واحد حروف تجره تسمى حروف الجر وحروف الإضافة وهي عشرون: الباء للإلصاق، ومن ل |
| I-A05 | 14 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A06 | 14 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A07 | 14 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A08 | 14 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A09 | 14 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A10 | 14 | applied | engine:Murib.line · the jarr letters, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A11 | 14 | applied | engine:Nahw342Engine · qasam, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A12 | 14 | applied | engine:Nahw342Engine · qasam, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A13 | 14 | applied | engine:IstithnaEngine · حَاشَا, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A14 | 14 | applied | engine:Murib.line, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A15 | 14 | applied | engine:Murib.line, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A16 | 14 | applied | engine:IstithnaEngine · خَلَا, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A17 | 14 | applied | engine:IstithnaEngine · عَدَا, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A18 | 14 | applied | engine:Murib.line, note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A19 | 14 | noted | note:al-amil-wa-aqsamuh — ⚠ the engine still misreads the example: «كَيْمَهْ عَصَيْتَ» → حرف استفهام، لا محل له من الإعراب. | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A20 | 14 | noted | note:al-amil-wa-aqsamuh | والمجاوزة، وعلى للاستعلاء، واللام للتعليل والتخصيص، وفي للظرف، والكاف للتشبيه، وحتى للغاية |
| I-A21 | 21 | applied | engine:Murib.line · inna, note:mawadi-kasr-inna | منها: إن وأن للتحقيق، وكأن للتشبيه، ولكن للاستدراك، وليت للتمني، ولعل للترجي. |
| I-A22 | 21 | applied | engine:InnaEngine · أَنَّ, note:mawadi-kasr-inna | منها: إن وأن للتحقيق، وكأن للتشبيه، ولكن للاستدراك، وليت للتمني، ولعل للترجي. |
| I-A23 | 21 | applied | engine:Murib.line · kaʾanna, note:mawadi-kasr-inna | منها: إن وأن للتحقيق، وكأن للتشبيه، ولكن للاستدراك، وليت للتمني، ولعل للترجي. |
| I-A24 | 21 | applied | engine:Murib.line · lākinna, note:mawadi-kasr-inna | منها: إن وأن للتحقيق، وكأن للتشبيه، ولكن للاستدراك، وليت للتمني، ولعل للترجي. |
| I-A25 | 21 | applied | engine:Murib.line · layta, note:mawadi-kasr-inna | منها: إن وأن للتحقيق، وكأن للتشبيه، ولكن للاستدراك، وليت للتمني، ولعل للترجي. |
| I-A26 | 21 | applied | engine:Murib.line · laʿalla, note:mawadi-kasr-inna | منها: إن وأن للتحقيق، وكأن للتشبيه، ولكن للاستدراك، وليت للتمني، ولعل للترجي. |
| I-A27 | 25 | applied | engine:Murib.line · lā li-l-jins, note:ma-la-laysa-wa-la-al-jins | والثامن لا لنفي الجنس، وشرط عملها أن يكون اسمها نكرة مضافة أو مشتبهة بها غير مفصول عنها نح |
| I-A28 | 25 | applied | engine:AnEngine · I-1, note:ma-la-laysa-wa-la-al-jins | والثامن لا لنفي الجنس، وشرط عملها أن يكون اسمها نكرة مضافة أو مشتبهة بها غير مفصول عنها نح |
| I-A29 | 25 | applied | engine:Sh336Engine · R78, note:ma-la-laysa-wa-la-al-jins | والقسم الثاني حرفان ما ولا المشبهتان بليس في كونهما للنفي والدخول على المبتدأ والخبر، وشرط |
| I-A30 | 25 | noted | note:ma-la-laysa-wa-la-al-jins — ⚠ the engine still misreads the example: «لَا رَجُلٌ أَفْضَلَ مِنْكَ» → اسم، نعت. | والثامن لا لنفي الجنس، وشرط عملها أن يكون اسمها نكرة مضافة أو مشتبهة بها غير مفصول عنها نح |
| I-A31 | 26 | applied | engine:AnEngine · I-1, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A32 | 26 | applied | engine:Murib.line · lan, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A33 | 26 | applied | engine:Murib.line · kay, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A34 | 26 | noted | note:nawasib-wa-jawazim-al-mudari — ⚠ the engine still misreads the example: «إِذَنْ أُكْرِمَكَ» → فعل ماض مبني للمجهول، مبني على الفتح، وفيه ضمير هو المفعول ب | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A35 | 26 | applied | engine:Murib.line · lam, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A36 | 26 | applied | engine:Murib.line · lammā, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A37 | 26 | applied | engine:Murib.line · lām al-amr, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A38 | 26 | applied | engine:Murib.line · lā al-nāhiya, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A39 | 26 | applied | engine:ShartEngine, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A40 | 26 | applied | engine:ShartEngine · I-7, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-A41 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A42 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A43 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A44 | 27 | applied | engine:Murib.line | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A45 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A46 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A47 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A48 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A49 | 27 | applied | engine:ShartEngine · I-7 | وأين وأنى للمكان، وإذما وإذا ما ومتى للزمان، ومهما وما وأي ومن. |
| I-A50 | 28 | applied | engine:Murib.doer / DabtEngine, note:al-lazim-wal-mutaaddi | والعامل القياسي ما يمكن أن يذكر في عمله قاعدة كلية موضوعها غير محصور، ولا يضره كون صيغته س |
| I-A51 | 35 | applied | engine:Sh336Engine · R92 | والثاني اسم الفاعل، فهو يعمل عمل فعله المعلوم. |
| I-A52 | 35 | applied | engine:Nahw342Engine · sababi | والثاني اسم الفاعل، فهو يعمل عمل فعله المعلوم. |
| I-A53 | 37 | applied | engine:Sh336Engine · R110 | وجهه. |
| I-A54 | 37 | noted | note:amal-ism-al-tafdil-wal-masdar, note:ism-al-tafdil-fil-kafiya — ⚠ the engine still misreads the example: «زَيْدٌ أَفْضَلُ مِنْ عَمْرٍو» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، خبر. | والخامس اسم التفضيل، وهو لا ينصب المفعول به بالاتفاق، ولا يرفع الفاعل الظاهر إلا إذا صار ب |
| I-A55 | 37 | applied | engine:Murib.line, note:amal-ism-al-tafdil-wal-masdar | والسادس المصدر، وشرط عمله في الفاعل والمفعول به أن لا يكون مصغرا ولا موصوفا ولا مقترنا بال |
| I-A56 | 40 | applied | engine:IdafaEngine, note:al-mudaf-wa-nawa-al-idafa | والسابع اسم المضاف، وهو يعمل الجر، وشرطه أن يكون اسما مجردا عن تنوينه ونائبه لأجل الإضافة، |
| I-A57 | 43 | applied | engine:MansubEngine · v332 I-9, note:al-ism-al-mubham-al-tamm | والثامن الاسم المبهم التام، فإنه ينصب اسما نكرة على التمييز، وتمامه أي كونه على حالة يمتنع |
| I-A58 | 49 | applied | engine:Murib.line · ism fiʿl, note:asma-al-afal-wal-aswat-wal-murakkabat | والتاسع معنى الفعل، والمراد منه كل لفظ يفهم منه معنى فعل، فمنه أسماء الأفعال وهو ما كان بم |
| I-A59 | 52 | applied | engine:Murib.khabarOf | الظاهر إلا بشرط الاعتماد إلا ما ذكر أو الموصول نحو زيد في الدار أبوه وما في الدار أحد وجاء |
| I-A60 | 55 | applied | engine:Murib.line · T2, note:al-amil-al-manawi | والعامل المعنوي ما لا يكون للسان فيه حظ وإنما هو معنى يعرف بالقلب، وهو اثنان: الأول رافع ا |
| I-B01 | 80 | applied | engine:Murib.doer | أو ما بمعناه نحو ضرب زيد وأمضروب الزيدان، ولا يكونان إلا اسمين أو في تأويله غير أن النائب  |
| I-B02 | 80 | applied | engine:Murib.doer | أو ما بمعناه نحو ضرب زيد وأمضروب الزيدان، ولا يكونان إلا اسمين أو في تأويله غير أن النائب  |
| I-B03 | 101 | applied | engine:Murib.khabarOf, note:al-mubtada-wa-nawah | به المسند إليه المجرد عن العوامل اللفظية نحو زيد قائم وحق أنك قائم ولا بد له من خبر، والثا |
| I-B04 | 101 | applied | engine:Nahw342Engine · wasf, note:al-mubtada-wa-nawah | به المسند إليه المجرد عن العوامل اللفظية نحو زيد قائم وحق أنك قائم ولا بد له من خبر، والثا |
| I-B05 | 101 | applied | engine:Murib.khabarOf, note:al-mubtada-wa-nawah | به المسند إليه المجرد عن العوامل اللفظية نحو زيد قائم وحق أنك قائم ولا بد له من خبر، والثا |
| I-B06 | 107 | applied | engine:Murib.line · inna | والسادس خبر باب إن وأمره كأمر خبر المبتدأ لكن لا يجوز تقديمه على اسمها إلا أن يكون ظرفا نح |
| I-B07 | 107 | applied | engine:Murib.line · kāna (I-2), note:al-marfuat-al-khamis-ila-al-tasi | والخامس اسم باب كان وحكمه حكم الفاعل. |
| I-B08 | 107 | applied | engine:Sh336Engine · R78, note:al-marfuat-al-khamis-ila-al-tasi | والخامس اسم باب كان وحكمه حكم الفاعل. |
| I-B09 | 107 | applied | engine:Murib.line · lā li-l-jins | والسادس خبر باب إن وأمره كأمر خبر المبتدأ لكن لا يجوز تقديمه على اسمها إلا أن يكون ظرفا نح |
| I-B10 | 110 | applied | engine:DabtEngine | وأما المنصوب فثلثة عشر: الأول المفعول المطلق وهو اسم ما فعله فاعل عامل مذكور لفظا أو تقدير |
| I-B11 | 110 | applied | engine:DabtEngine | وأما المنصوب فثلثة عشر: الأول المفعول المطلق وهو اسم ما فعله فاعل عامل مذكور لفظا أو تقدير |
| I-B12 | 113 | applied | engine:CaseEngine · ẓarf, note:al-maful-fih-wal-maful-lah | والثالث المفعول فيه وهو اسم ما فعل فيه مضمون عامله من زمان أو مكان، وشرط نصبه لفظا تقدير ف |
| I-B13 | 113 | applied | engine:MansubEngine · v332 I-18, note:al-maful-fih-wal-maful-lah | والثالث المفعول فيه وهو اسم ما فعل فيه مضمون عامله من زمان أو مكان، وشرط نصبه لفظا تقدير ف |
| I-B14 | 113 | noted | note:al-maful-fih-wal-maful-lah — ⚠ the engine still misreads the example: «جِئْتُ وَزَيْدًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، مفعول به. | والثالث المفعول فيه وهو اسم ما فعل فيه مضمون عامله من زمان أو مكان، وشرط نصبه لفظا تقدير ف |
| I-B15 | 113 | noted | note:al-maful-maah-wal-hal — ⚠ the engine still misreads the example: «ضَرَبْتُ زَيْدًا قَائِمًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، مفعول مطلق. | والسادس الحال وهي ما يبين هيئة الفاعل أو المفعول به لفظا أو معنى مثل ضربت زيدا قائما وهذا  |
| I-B16 | 116 | applied | engine:MansubEngine · v332 I-9 | والسابع التمييز وهو ما يرفع |
| I-B17 | 119 | applied | engine:IstithnaEngine, note:al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa, note:al-mustathna-wa-nawah-wa-nasbuh | والثامن المستثنى وهو نوعان: متصل وهو المخرج عن متعدد بإلا أو إحدى أخواتها، ومنقطع وهو المذ |
| I-B18 | 125 | applied | engine:Murib.line · kāna, note:al-mansubat-al-tasi-ila-al-thalith-ashar | والتاسع خبر باب كان وأمره كأمر خبر المبتدأ ويجوز حذف كان دون غيره عند قرينة نحو الناس مجزي |
| I-B19 | 125 | applied | engine:Murib.line · inna, note:al-mansubat-al-tasi-ila-al-thalith-ashar | والعاشر اسم باب إن وهو كالمبتدأ لكن لا يجوز حذفه. |
| I-B20 | 125 | applied | engine:Murib.line · lā li-l-jins, note:al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa, note:madhhab-kalami | بعدها صفة لا مستثنى نحو قوله تعالى لو كان فيهما آلهة إلا الله لفسدتا. |
| I-B21 | 125 | applied | engine:Sh336Engine · R78, note:al-mansubat-al-tasi-ila-al-thalith-ashar | والتاسع خبر باب كان وأمره كأمر خبر المبتدأ ويجوز حذف كان دون غيره عند قرينة نحو الناس مجزي |
| I-B22 | 125 | applied | engine:Murib.line | والثالث عشر المضارع الداخل عليه أحد النواصب نحو لن يضرب. |
| I-B23 | 125 | applied | engine:Murib.line · the jarr letters | وأما المجرور فاثنان: الأول المجرور بحرف الجر وقد مر بيانه، والثاني المجرور بالإضافة ولا يج |
| I-B24 | 125 | applied | engine:IdafaEngine | وأما المجرور فاثنان: الأول المجرور بحرف الجر وقد مر بيانه، والثاني المجرور بالإضافة ولا يج |
| I-B25 | 131 | applied | engine:Murib.line, note:al-majzum-wal-shart-wal-jaza | وأما المجزوم ففعل مضارع دخله أحد الجوازم المذكورة سابقا، فإن كانت كلم المجازاة تقتضي شرطا  |
| I-B26 | 137 | applied | engine:Murib.line · naʿt, note:al-tawabi-wal-sifa | الأول الصفة وهي تابع يدل على معنى في متبوعه مطلقا، ويجوز تعددها نحو جاءني الرجل العالم الف |
| I-B27 | 146 | applied | engine:Murib.line · ʿaṭf, note:al-atf-bil-huruf-wa-ahkamuh, note:huruf-al-atf-fil-kafiya | والثاني العطف بحروف وهو تابع يتوسط بينه وبين متبوعه أحد الحروف العشرة وهي الواو والفاء وثم |
| I-B28 | 146 | applied | engine:TawkidEngine | والألف واللام في اسم الفاعل والمفعول بمعنى الذي أو التي. |
| I-B29 | 152 | applied | engine:Murib.line · badal | والرابع البدل وهو المقصود بالنسبة دونه وأقسامه أربعة: بدل الكل من الكل إن صدقا على واحد نح |
| I-B30 | 152 | noted | note:al-badal-wa-aqsamuh-wa-atf-al-bayan, note:atf-bayan, note:kamal-al-ittisal — ⚠ the engine still misreads the example: «أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة. | والخامس عطف البيان وهو تابع جيء به لإيضاح متبوعه ولا يدل على معنى فيه نحو أقسم بالله أبو ح |
| I-C01 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C02 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C03 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C04 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C05 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C06 | 162 | applied | engine:SignEngine, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | والثاني أيضا إما تام الإعراب بالحروف الثلاثة بالواو رفعا والألف نصبا والياء جرا فهو الأسما |
| I-C07 | 162 | applied | engine:Nahw342Engine · fiveRaf, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C08 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C09 | 162 | applied | engine:SignEngine · T2, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-C10 | 162 | applied | engine:SignEngine, note:al-irab-wa-taqsimuhu-bil-dhat-wal-mahall, note:mamnu-min-sarf, note:naqis-al-irab-bil-harakat-wal-murab-bil-huruf | فهو الاسم المفرد والجمع المكسر المنصرفان نحو جاءني رجل ورجال ورأيت رجلا ورجالا ومررت برجل  |
| I-15.3 | 15 | open | engine to build: TaalluqEngine — probe «بِزَيْدٍ مَرَرْتُ» → اسم، مجرور وعلامة جره الكسرة الظاهرة. | ويجوز تقديم ما عدا هذا على متعلقه نحو بزيد مررت. |
| I-17.2 | 17 | applied | engine:TaalluqEngine, note:hadhf-al-jarr | وإن كان ظرف مكان محدودا، وهو ما ثبت له اسم بسبب أمر داخل في مسماه كالدار والبيت، نحو دار،  |
| I-19.2 | 19 | not-automatable | a rule for the writer (مَرَرْتُ بِزَيْدٍ بِعَمْرٍو is not said); the reader never meets the forbidden form | ولا يجوز تعلق الجارين بمعنى واحد بدون العطف بفعل واحد، فلا يقال مررت بزيد بعمرو ولا ضربت ي |
| I-21.2 | 21 | applied | engine:InnaEngine.verdict | فإن لا تغير معنى الجملة، وأن مع جملتها في حكم المصدر، ومن ثمة وجب الكسر في موضع الجمل والف |
| I-23.2 | 23 | applied | engine:Sh336Engine · R141 | وتخفف المكسورة فيلزم اللام في خبرها، ويجوز إلغاؤها ودخولها على فعل من أفعال المبتدإ نحو قو |
| I-23.3 | 23 | applied | engine:AnEngine · I-1 | وتخفف المفتوحة فتعمل في ضمير شأن مقدر، ويلزم أن يكون قبلها فعل من أفعال التحقيق نحو علمت أ |
| I-24.2 | 24 | open | probe «كَأَنْ ذَا نَابٍ حَقًّا» → حرف لا محل له من الإعراب. | وتخفف كأن فتلغى على الأفصح نحو كأن ذا ناب حقا، وتخفف لكن فيجب الفاء وهما نحو ما جاءني زيد  |
| I-25.1 | 25 | applied | engine:Murib.line · I-19, note:ma-la-laysa-wa-la-al-jins | والثامن لا لنفي الجنس، وشرط عملها أن يكون اسمها نكرة مضافة أو مشتبهة بها غير مفصول عنها نح |
| I-25.2 | 25 | applied | engine:Sh336Engine · R78 (إِلَّا before the khabar), note:ma-la-laysa-wa-la-al-jins | والقسم الثاني حرفان ما ولا المشبهتان بليس في كونهما للنفي والدخول على المبتدأ والخبر، وشرط |
| I-26.0 | 26 | applied | engine:Murib.line, note:nawasib-wa-jawazim-al-mudari | أربعة أحرف: أن للمصدرية، ولن للنفي المؤكد في الاستقبال، وكي للسببية، وإذن للشرط والجزاء، و |
| I-26.1 | 26 | open | engine to build: Murib.line · I-6 — probe «زُرْنِي فَأُكْرِمَكَ» → فعل ماض مبني للمجهول، مبني على الفتح، وفيه ضمير هو المفعول به، ونائب ا | ويجوز إضمار أن خاصة فينتصب المضارع به نحو زرني فأكرمك. |
| I-27.1 | 27 | applied | engine:Murib.line · jawāb al-ṭalab | ويجوز إضمار إن خاصة فيجزم المضارع بها نحو زرني أكرمك. |
| I-29.0 | 29 | applied | engine:Murib.line · نِعْمَ, note:al-lazim-wal-mutaaddi | نعم للمدح وبئس للذم، وشرطهما أن يكون الفاعل معرفا باللام أو مضافا إليه أو مضمرا مميزا بنكر |
| I-29.3 | 29 | not-automatable | dropping the object «with a context or without» — the reader cannot see what was not said | والمتعدي ما لا يتم فهمه بغير ما وقع عليه الفعل، وهو على ثلثة أضرب: الأول متعد إلى مفعول وا |
| I-30.2 | 30 | not-automatable | a rule for the writer: what may be left out | ولا يجوز حذف مفعوليها معا أو أحدهما بدون قرينة، ومع قرينة كثر حذفهما معا وقل حذف أحدهما فق |
| I-33.2 | 33 | open | probe «قَائِمًا كَانَ زَيْدٌ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | ويجوز تقديم أخبارها على أنفسها إلا ما في أوله ما فلا يجوز نحو قائما ما زال زيد، وكذا إن لم |
| I-34.1 | 34 | noted | note:afal-al-muqaraba | ولا يجوز تقديم أخبار أفعال المقاربة على أنفسها. |
| I-35.2 | 35 | applied | engine:Sh336Engine · R92 (the participle with tanwīn) | وشرط عملهما في الفاعل المنفصل والمفعول به أن لا يكونا مصغرين نحو ضويرب ومضيرب، ولا موصوفين |
| I-37.2 | 37 | applied | engine:Murib.line, note:amal-ism-al-tafdil-wal-masdar | والسادس المصدر، وشرط عمله في الفاعل والمفعول به أن لا يكون مصغرا ولا موصوفا ولا مقترنا بال |
| I-40.1 | 40 | applied | engine:IdafaEngine, note:al-mudaf-wa-nawa-al-idafa | والسابع اسم المضاف، وهو يعمل الجر، وشرطه أن يكون اسما مجردا عن تنوينه ونائبه لأجل الإضافة، |
| I-40.2 | 40 | applied | engine:IdafaEngine, note:al-mudaf-wa-nawa-al-idafa | وهي على نوعين معنوية ولفظية، فالمعنوية أن يكون المضاف غير صفة مضافة إلى معمولها نحو غلام ز |
| I-43.1 | 43 | applied | engine:IdafaEngine · v332 I-5, note:al-mudaf-wa-nawa-al-idafa | واللفظية أن يكون المضاف صفة مضافة إلى معمولها ولا تفيد إلا تخفيفا في اللفظ نحو ضارب زيد وح |
| I-43.2 | 43 | applied | engine:MansubEngine · v332 I-9, note:al-ism-al-mubham-al-tamm | والثامن الاسم المبهم التام، فإنه ينصب اسما نكرة على التمييز، وتمامه أي كونه على حالة يمتنع |
| I-46.0 | 46 | applied | engine:AdadEngine, note:al-ism-al-mubham-al-tamm | ماذا أراد الله بهذا مثلا، وبالتنوين إما لفظا نحو رطل زيتا أو تقديرا نحو مثقال ذهبا وأحد عش |
| I-52.0 | 52 | open | probe «زَيْدٌ فِي الدَّارِ أَبُوهُ» → اسم، مرفوع وعلامة رفعه الواو نيابة عن الضمة لأنه من الأسماء الخمسة، مب | الظاهر إلا بشرط الاعتماد إلا ما ذكر أو الموصول نحو زيد في الدار أبوه وما في الدار أحد وجاء |
| I-65.2 | 65 | open | probe «أَعْجَبَنِي أَنْ ضَرَبْتَ» → فعل ماض، مبني على السكون لاتصاله بضمير رفع متحرك، والتاء ضمير متصل مبن | والقسم الثالث ما كان الأصل فيه أن لا يكون معمولا لكن قد يقع موقع القسم الثاني فيكون معمولا |
| I-68.2 | 68 | not-automatable | a clause meant as its own wording (زَيْدٌ قَائِمٌ جُمْلَةٌ) — the reader cannot tell a cited clause from a used one | فإن أريد بالجملة لفظها فلا بد لها من إعراب لكونها في حكم الاسم المفرد حتى يجوز وقوعها في ك |
| I-74.0 | 74 | applied | engine:JumlaMahallEngine · khabar | أبوه فتكون مرفوعة المحل، أو لباب كان نحو كان زيد أبوه عالم أو كاد نحو كاد زيد يخرج أو مفعو |
| I-80.0 | 80 | open | engine to build: Murib.doer — probe «مُرَّ بِزَيْدٍ» → اسم، مجرور وعلامة جره الكسرة الظاهرة. | أو ما بمعناه نحو ضرب زيد وأمضروب الزيدان، ولا يكونان إلا اسمين أو في تأويله غير أن النائب  |
| I-80.1 | 80 | applied | engine:Murib.doer, note:al-fail-al-mudmar-al-mustatir-wujuban | كل منهما قسمان مضمر ومظهر، فالمضمر أيضا على قسمين مستتر وبارز، فالمستتر أيضا قسمان: واجب ا |
| I-89.1 | 89 | applied | engine:Murib.doer, note:al-fail-al-muzhar-wa-tanith-amilih | وأما المظهر فظاهر، وإذا أسند إليه العامل يجب إفراده وغيبته ولو كان مثنى أو مجموعا نحو ضرب  |
| I-92.0 | 92 | applied | engine:Murib.doer, note:al-fail-al-muzhar-wa-tanith-amilih | أو طالعة، وفي غيرهما يجوز تأنيث عامله وتذكيره إن كان مؤنثا نحو طلعت الشمس أو طلع الشمس ونح |
| I-98.1 | 98 | not-automatable | agreement the writer must keep; the reader's line is the same either way | وأما جمع المذكر السالم فيجب تذكير عامله فتقول جاء المسلمون أو رجل قاعد ناصروه، وإذا أسند إ |
| I-98.2 | 98 | applied | engine:Murib.doer, note:al-jumu-wa-tanith-amiliha | وأما جمع المذكر المكسر العاقل إذا أسند إلى ضميره فيجب أن يكون عامله مفردا مؤنثا أو جمعا مذ |
| I-101.0 | 101 | applied | engine:Nahw342Engine · wasf, note:al-mubtada-wa-nawah | به المسند إليه المجرد عن العوامل اللفظية نحو زيد قائم وحق أنك قائم ولا بد له من خبر، والثا |
| I-101.1 | 101 | applied | engine:Murib.line | والرابع خبر المبتدأ وهو المجرد عن العوامل اللفظية المسند به غير الفعل ومعناه نحو قائم في ز |
| I-104.0 | 104 | applied | engine:JumlaMahallEngine · khabar, note:khabar-al-mubtada-wa-ahkamuh | قائم قاعد، وقد يكون جملة اسمية أو فعلية فلا بد من عائد إلى المبتدأ إن لم تكن خبرا عن ضمير  |
| I-104.1 | 104 | applied | engine:Murib.line, note:al-fa-fi-khabar-al-mubtada | وإن كان المبتدأ بعد أما وجب دخول الفاء في خبره نحو أما زيد فمنطلق إلا لضرورة الشعر كقوله أ |
| I-107.0 | 107 | noted | note:al-fa-fi-khabar-al-mubtada — ⚠ the engine still misreads the example: «الَّذِي يَأْتِينِي فَلَهُ دِرْهَمٌ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، فاعل. | الفاء في خبره، وكذا إذا دخل عليه إن وأن ولكن بخلاف سائر نواسخ المبتدأ حرفا كان أو فعلا نحو |
| I-107.2 | 107 | applied | engine:InnaEngine · the fronted khabar | والسادس خبر باب إن وأمره كأمر خبر المبتدأ لكن لا يجوز تقديمه على اسمها إلا أن يكون ظرفا نح |
| I-110.1 | 110 | open | probe «قَعَدْتُ جُلُوسًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | وأما المنصوب فثلثة عشر: الأول المفعول المطلق وهو اسم ما فعله فاعل عامل مذكور لفظا أو تقدير |
| I-110.2 | 110 | noted | note:al-maful-bihi-wa-qismah — ⚠ the engine still misreads the example: «زَيْدًا ضَرَبْتُ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | والثاني المفعول به وهو اسم ما وقع عليه فعل الفاعل وهو على قسمين: عام وهو المجرور بالحرف، و |
| I-113.0 | 113 | applied | engine:CaseEngine · ẓarf, note:al-maful-fih-wal-maful-lah | والثالث المفعول فيه وهو اسم ما فعل فيه مضمون عامله من زمان أو مكان، وشرط نصبه لفظا تقدير ف |
| I-113.1 | 113 | applied | engine:MansubEngine · v332 I-18, note:al-maful-fih-wal-maful-lah | والرابع المفعول له وهو اسم ما فعل لأجله مضمون عامله، وشرط نصبه لفظا تقدير اللام وقد مر شرط |
| I-113.2 | 113 | open | probe «جِئْتُ وَزَيْدًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، مفعول به. | والخامس المفعول معه وهو المذكور بعد الواو لمصاحبة معمول عامل نحو جئت وزيدا، ولا يجوز تقديم |
| I-113.3 | 113 | noted | note:al-maful-maah-wal-hal — ⚠ the engine still misreads the example: «ضَرَبْتُ زَيْدًا قَائِمًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، مفعول مطلق. | والسادس الحال وهي ما يبين هيئة الفاعل أو المفعول به لفظا أو معنى مثل ضربت زيدا قائما وهذا  |
| I-116.0 | 116 | applied | engine:Murib.line, note:al-hal-jumla-wa-rabituha, note:al-maful-maah-wal-hal | أن تكون نكرة ولا تتقدم على العامل المعنوي ولا على ذي الحال المجرور فلا يقال مر بزيد جالسا، |
| I-119.1 | 119 | applied | engine:IstithnaEngine, note:al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa, note:al-mustathna-wa-nawah-wa-nasbuh | والثامن المستثنى وهو نوعان: متصل وهو المخرج عن متعدد بإلا أو إحدى أخواتها، ومنقطع وهو المذ |
| I-122.0 | 122 | noted | note:al-fail-al-mudmar-al-mustatir-wujuban, note:al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa, note:al-mustathna-wa-nawah-wa-nasbuh — ⚠ the engine still misreads the example: «مَا جَاءَنِي إِلَّا زَيْدًا أَحَدٌ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | نحو ما جاءني إلا زيدا أحد أو منقطعا نحو جاءني القوم إلا الحمار أو كان بعد خلا أو عدا في ال |
| I-125.1 | 125 | applied | engine:Murib.line, note:al-mansubat-al-tasi-ila-al-thalith-ashar | والتاسع خبر باب كان وأمره كأمر خبر المبتدأ ويجوز حذف كان دون غيره عند قرينة نحو الناس مجزي |
| I-125.2 | 125 | noted | note:al-mansubat-al-tasi-ila-al-thalith-ashar | والعاشر اسم باب إن وهو كالمبتدأ لكن لا يجوز حذفه. |
| I-128.0 | 128 | noted | note:al-majrur-bil-harf-wa-bil-idafa | تقديمه ولا معموله على المضاف إلا أن يكون المضاف لفظ غير فيجوز تقديم معمول المضاف إليه عليه |
| I-128.1 | 128 | noted | note:hadhf-al-mudaf-wal-mudaf-ilayh | وقد يحذف المضاف فيعطى إعرابه للمضاف إليه وهو القياس نحو قوله تعالى واسأل القرية أي أهل الق |
| I-131.1 | 131 | noted | note:al-majzum-wal-shart-wal-jaza — ⚠ the engine still misreads the example: «إِنْ تَضْرِبْ أَضْرِبْ» → فعل أمر، مبني على السكون، والفاعل ضمير مستتر وجوبا تقديره «أ | وأما المجزوم ففعل مضارع دخله أحد الجوازم المذكورة سابقا، فإن كانت كلم المجازاة تقتضي شرطا  |
| I-134.0 | 134 | applied | engine:JumlaMahallEngine · jawāb with the fāʾ, note:al-fa-fi-jawab-al-shart | وإن كان الجزاء جملة اسمية أو ماضية غير متصرفة أو بمعناه فلا بد من قد ظاهرة أو مقدرة أو مضا |
| I-137.1 | 137 | applied | engine:Murib.line · naʿt (I-5) | وأما المعمول بالتبعية فخمسة ولا يجوز تقديم شيء منها على متبوعها وعاملها عامل متبوعها وإعرا |
| I-137.2 | 137 | applied | engine:JumlaMahallEngine · naʿt, note:al-tawabi-wal-sifa | الأول الصفة وهي تابع يدل على معنى في متبوعه مطلقا، ويجوز تعددها نحو جاءني الرجل العالم الف |
| I-143.1 | 143 | applied | engine:Murib.silaOf, note:al-mawsul-wal-muarraf-bil-lam-wal-mudaf | والنوع الرابع الموصول ولا بد له من صلة جملة خبرية معلومة للسامع فيها ضمير عائد إلى الموصول |
| I-146.3 | 146 | noted | note:al-atf-bil-huruf-wa-ahkamuh, note:huruf-al-atf-fil-kafiya | والثاني العطف بحروف وهو تابع يتوسط بينه وبين متبوعه أحد الحروف العشرة وهي الواو والفاء وثم |
| I-149.0 | 149 | noted | note:al-atf-bil-huruf-wa-ahkamuh — ⚠ the engine still misreads the example: «ضَرَبَ زَيْدٌ عَمْرًا وَبَكْرٌ خَالِدًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | فيجب ويمتنع له، ويجوز عطف شيئين بحرف واحد على معمولي عامل واحد بالاتفاق نحو ضرب زيد عمرا و |
| I-152.0 | 152 | open | probe «ضَرَبْتُ زَيْدًا رَأْسَهُ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، والضمير مضاف إليه. | والرابع البدل وهو المقصود بالنسبة دونه وأقسامه أربعة: بدل الكل من الكل إن صدقا على واحد نح |
| I-171.0 | 171 | applied | engine:MamnuEngine, note:ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh | وحمراء، وكل علم فيه تاء التأنيث لفظا نحو فاطمة وحمزة أو تقديرا وهو زائد على الثلاثة نحو زي |
| I-198.1 | 198 | noted | note:jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha — ⚠ the engine still misreads the example: «وَمِنْ خِزْيِ يَوْمِئِذٍ» → اسم، مضاف إليه. | وأما جائز البناء فالظروف المضافة إلى الجملة وإذ فإنها يجوز بناؤها على الفتح نحو قوله تعالى |

## al-Kāfiya (Ibn al-Ḥājib)

Source: `content/samples/al-kafiya (the matn on the shelf) + research/sources/kafiya-internet-digest.txt`. Entries: 131 — applied **43**, noted **59**, not automatable **20**, open **9** (headings 0, lecture fragments 0, cited verses 0, counted apart).

| id | line | status | carried by / reason | the book |
|---|---|---|---|---|
| K1:s5 | 1:s5 | noted | note:tarifat-daftar-al-kafiya | اللَّفْظُ مَا يَتَلَفَّظُ بِهِ الْإِنْسَانُ حَقِيقَةً أَوْ حُكْمًا مُهْمَلًا كَانَ أَوْ مَ |
| K1:s7 | 1:s7 | noted | note:tarifat-daftar-al-kafiya | وَالْمَعْنَى مَا يُقْصَدُ بِشَيْءٍ |
| K1:s11 | 1:s11 | noted | note:al-kalima-wal-kalam | وَالْكَلَامُ مَا تَضَمَّنَ كَلِمَتَيْنِ بِالْإِسْنَادِ |
| K1:s15 | 1:s15 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya, note:al-harf-wa-huruf-al-jarr-fil-kafiya | وَالِاسْمُ مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ غَيْرِ مُقْتَرِنٍ بِأَحَدِ الْأَزْمِنَةِ ا |
| K1:s16 | 1:s16 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya, note:al-harf-wa-huruf-al-jarr-fil-kafiya | وَالْفِعْلُ مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ مُقْتَرِنٍ بِأَحَدِ الْأَزْمِنَةِ الثَّلَ |
| K1:s17 | 1:s17 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya, note:al-harf-wa-huruf-al-jarr-fil-kafiya | وَالْحَرْفُ مَا دَلَّ عَلَى مَعْنًى فِي غَيْرِهِ |
| K1:s19 | 1:s19 | noted | note:tarifat-daftar-al-kafiya | وَالْخَاصَّةُ مَا يَخْتَصُّ بِشَيْءٍ وَلَا يُوجَدُ فِي غَيْرِهِ |
| K2:s4 | 2:s4 | noted | note:al-murab-wal-mabni-wal-irab | وَالْإِعْرَابُ مَا اخْتَلَفَ آخِرُهُ بِهِ لِيَدُلَّ عَلَى الْمَعَانِي الْمُعْتَوِرَةِ عَلَ |
| K2:s9 | 2:s9 | noted | note:al-murab-wal-mabni-wal-irab | وَالْعَامِلُ مَا بِهِ يَتَقَوَّمُ الْمَعْنَى الْمُقْتَضِي لِلْإِعْرَابِ |
| K3:s1 | 3:s1 | noted | note:al-mabni-wal-mudmar | الْمَبْنِيُّ مَا نَاسَبَ مَبْنِيَّ الْأَصْلِ أَوْ وَقَعَ غَيْرَ مُرَكَّبٍ |
| K3:s6 | 3:s6 | noted | note:al-mabni-wal-mudmar | الْمُضْمَرُ مَا وُضِعَ لِمُتَكَلِّمٍ أَوْ مُخَاطَبٍ أَوْ غَائِبٍ تَقَدَّمَ ذِكْرُهُ لَفْظً |
| K3:s13 | 3:s13 | noted | note:al-mabni-wal-mudmar | وَلَا يَجُوزُ الْمُنْفَصِلُ مَعَ إِمْكَانِ الْمُتَّصِلِ لِأَنَّ الضَّمَائِرَ وُضِعَتْ لِلِ |
| K4:s4 | 4:s4 | applied | engine:DamirEngine · the detached second object | وَإِلَّا وَجَبَ الِانْفِصَالُ نَحْوُ أَعْطَيْتُهُ إِيَّاهُ وَأَعْطَيْتُهُ إِيَّاكَ |
| K4:s5 | 4:s5 | noted | note:mawadi-al-munfasil-wa-damir-al-fasl-wal-shan — ⚠ the engine still misreads the example: «كُنْتُ إِيَّاهُ» → ضمير منفصل، مبني على الضم. | وَخَبَرُ بَابِ كَانَ إِذَا كَانَ ضَمِيرًا جَازَ اِتِّصَالُهُ وَالْمُخْتَارُ اِنْفِصَالُهُ  |
| K4:s11 | 4:s11 | applied | engine:Nahw342Engine · fasl | وَشَرْطُهُ كَوْنُ الْخَبَرِ مَعْرِفَةً أَوْ أَفْعَلَ مِنْ نَحْوُ كَانَ زَيْدٌ هُوَ الْقَائ |
| K5:s1 | 5:s1 | noted | note:asma-al-ishara-wal-mawsulat | اسْمُ الْإِشَارَةِ مَا وُضِعَ لِمُشَارٍ إِلَيْهِ |
| K5:s9 | 5:s9 | noted | note:asma-al-ishara-wal-mawsulat | الْمَوْصُولُ مَا لَا يَتِمُّ جُزْءًا إِلَّا بِصِلَةٍ وَعَائِدٍ |
| K6:s1 | 6:s1 | noted | note:asma-al-afal-wal-aswat-wal-murakkabat | أَسْمَاءُ الْأَفْعَالِ مَا كَانَ بِمَعْنَى الْأَمْرِ أَوِ الْمَاضِي |
| K8:s7 | 8:s7 | noted | note:jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha — ⚠ the engine still misreads the example: «وَمِنْ خِزْيِ يَوْمِئِذٍ» → اسم، مضاف إليه. | وَالظَّرْفُ الْمُضَافُ إِلَى الْجُمْلَةِ أَوْ إِلَى إِذْ يَجُوزُ بِنَاؤُهُ عَلَى الْفَتْحِ |
| K8:s10 | 8:s10 | not-automatable | مِثْلَ may be built or declined in these examples — both readings stand, the reading decides | فَإِنَّ مِثْلَ فِي هٰذِهِ الْأَمْثِلَةِ يَجُوزُ بِنَاؤُهُ عَلَى الْفَتْحِ وَإِعْرَابُهُ مَ |
| K9:s1 | 9:s1 | noted | note:al-marifa-wal-nakira-fil-kafiya | الْمَعْرِفَةُ مَا وُضِعَ لِشَيْءٍ بِعَيْنِهِ |
| K9:s3 | 9:s3 | noted | note:al-marifa-wal-nakira-fil-kafiya | الْعَلَمُ مَا وُضِعَ لِشَيْءٍ بِعَيْنِهِ غَيْرَ مُتَنَاوِلٍ غَيْرَهُ بِوَضْعٍ وَاحِدٍ نَحْ |
| K9:s5 | 9:s5 | noted | note:al-marifa-wal-nakira-fil-kafiya | النَّكِرَةُ مَا وُضِعَ لِشَيْءٍ لَا بِعَيْنِهِ نَحْوُ رَجُلٌ وَامْرَأَةٌ |
| K10:s1 | 10:s1 | noted | note:asma-al-adad-fil-kafiya | أَسْمَاءُ الْعَدَدِ مَا وُضِعَ لِكَمِّيَّةِ آحَادِ الْأَشْيَاءِ |
| K11:s1 | 11:s1 | noted | note:al-muannath-wa-alamatuh, note:al-muannath-wal-mudhakkar-fil-kafiya | الْمُؤَنَّثُ مَا فِيهِ عَلَامَةُ التَّأْنِيثِ لَفْظًا أَوْ تَقْدِيرًا |
| K11:s4 | 11:s4 | noted | note:al-muannath-wal-mudhakkar-fil-kafiya | الْحَقِيقِيُّ مَا بِإِزَائِهِ ذَكَرٌ مِنَ الْحَيَوَانِ نَحْوُ امْرَأَةٌ بِإِزَاءِ رَجُلٍ و |
| K11:s5 | 11:s5 | noted | note:al-muannath-wal-mudhakkar-fil-kafiya | وَاللَّفْظِيُّ مَا لَيْسَ بِإِزَائِهِ ذَكَرٌ مِنَ الْحَيَوَانِ نَحْوُ ظُلْمَةٌ وَعَيْنٌ |
| K12:s1 | 12:s1 | noted | note:al-muthanna-fil-kafiya | الْمُثَنَّى مَا لَحِقَ آخِرَهُ أَلِفٌ أَوْ يَاءٌ مَفْتُوحٌ مَا قَبْلَهَا وَنُونٌ مَكْسُورَ |
| K13:s1 | 13:s1 | noted | note:al-jam-al-salim-fil-kafiya | الْمَجْمُوعُ مَا دَلَّ عَلَى آحَادٍ مَقْصُودَةٍ بِحُرُوفِ مُفْرَدِهِ بِتَغَيُّرٍ مَا |
| K13:s7 | 13:s7 | not-automatable | what may take the sound masculine plural (a rational male name without tāʾ) — a rule for forming the plural; the reader meets the plural made | وَشَرْطُ مُفْرَدِهِ إِنْ كَانَ اسْمًا أَنْ يَكُونَ عَلَمَ مُذَكَّرٍ عَاقِلٍ خَالٍ مِنَ الت |
| K13:s11 | 13:s11 | not-automatable | which adjectives take the feminine plural — a rule for forming it | وَمُفْرَدُهُ إِنْ كَانَ صِفَةً فَشَرْطُهُ أَنْ يَكُونَ لِمُذَكَّرِهِ جَمْعٌ بِالْوَاوِ وَا |
| K14:s1 | 14:s1 | noted | note:jam-al-taksir-fil-kafiya | جَمْعُ التَّكْسِيرِ مَا تَغَيَّرَ بِنَاءُ وَاحِدِهِ نَحْوُ رِجَالٌ وَأَفْرَاسٌ |
| K14:s2 | 14:s2 | noted | note:jam-al-taksir-fil-kafiya | وَجَمْعُ الْقِلَّةِ مَا يُطْلَقُ عَلَى الثَّلَاثَةِ إِلَى الْعَشَرَةِ وَلَهُ أَرْبَعَةُ أَ |
| K15:s6 | 15:s6 | not-automatable | the maṣdar's object never precedes it, its doer is never hidden — a rule for the writer | وَلَا يَتَقَدَّمُ مَعْمُولُهُ عَلَيْهِ فَلَا يُقَالُ أَعْجَبَنِي عَمْرًا ضَرْبُ زَيْدٍ وَل |
| K16:s1 | 16:s1 | noted | note:ism-al-fail-wal-maful-fil-kafiya | اسْمُ الْفَاعِلِ مَا اشْتُقَّ مِنْ فِعْلٍ لِمَنْ قَامَ بِهِ بِمَعْنَى الْحُدُوثِ |
| K16:s5 | 16:s5 | not-automatable | al-Kisāʾī: the participle's annexation is allowed, not required — a school view | فَعِنْدَ الْكِسَائِيِّ الْإِضَافَةُ جَائِزَةٌ لَا وَاجِبَةٌ وَهِيَ لَفْظِيَّةٌ وَالْإِضَاف |
| K16:s7 | 16:s7 | noted | note:ism-al-fail-wal-maful-fil-kafiya — ⚠ the engine still misreads the example: «مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْدًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، بدل. | وَإِذَا دَخَلَتْهُ اللَّامُ عَمِلَ بِلَا شَرْطٍ نَحْوُ مَرَرْتُ بِالضَّارِبِ أَبُوهُ زَيْد |
| K16:s11 | 16:s11 | not-automatable | the nūn of the dual / plural dropped for lightness from the al-participle (الْمُقِيمِي الصَّلَاةَ) — a qirāʾa | وَيَجُوزُ حَذْفُ نُونِ التَّثْنِيَةِ وَالْجَمْعِ تَخْفِيفًا مِنَ الْمُعَرَّفِ بِاللَّامِ ن |
| K16:s12 | 16:s12 | noted | note:ism-al-fail-wal-maful-fil-kafiya | اسْمُ الْمَفْعُولِ مَا اشْتُقَّ مِنْ فِعْلٍ لِمَنْ وَقَعَ عَلَيْهِ |
| K16:s14 | 16:s14 | open | engine to build: Nahw342Engine · sababi — probe «زَيْدٌ مُعْطًى غُلَامُهُ دِرْهَمًا» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، خبر، والضمير مضاف إليه. | وَكَذَا زَيْدٌ مُعْطًى غُلَامُهُ دِرْهَمًا وَمَعَ اللَّامِ يَعْمَلُ بِلَا شَرْطٍ زَيْدٌ ال |
| K17:s1 | 17:s1 | noted | note:al-sifa-al-mushabbaha-fil-kafiya | الصِّفَةُ الْمُشَبَّهَةُ مَا اشْتُقَّ مِنْ فِعْلٍ لَازِمٍ لِمَنْ قَامَ بِهِ بِمَعْنَى الثُ |
| K17:s9 | 17:s9 | not-automatable | الْحَسَنُ وَجْهِهِ is forbidden — a rule for the writer | وَيَمْتَنِعُ مِنْهَا الْحَسَنُ وَجْهِهِ لِأَنَّ الْإِضَافَةَ اللَّفْظِيَّةَ لَمْ تُفِدْ تَ |
| K19:s1 | 19:s1 | noted | note:ism-al-tafdil-fil-kafiya | اسْمُ التَّفْضِيلِ مَا اشْتُقَّ مِنْ فِعْلٍ لِمَوْصُوفٍ بِزِيَادَةٍ عَلَى غَيْرِهِ |
| K19:s4 | 19:s4 | not-automatable | the elative is made only from a bare triliteral that names no colour or defect — a rule of derivation | وَشَرْطُهُ أَنْ يُبْنَى مِنْ ثُلَاثِيٍّ مُجَرَّدٍ لَيْسَ بِلَوْنٍ وَلَا عَيْبٍ نَحْوُ زَيْ |
| K19:s9 | 19:s9 | not-automatable | the two senses of the annexed elative (يُوسُفُ أَحْسَنُ إِخْوَتِهِ) — meaning | وَالْمُضَافُ عَلَى مَعْنَيَيْنِ زِيَادَةُ الْمَوْصُوفِ عَلَى الْمُضَافِ إِلَيْهِ بِشَرْطِ  |
| K19:s10 | 19:s10 | not-automatable | agreement of the elative with its noun by the three ways it is used — a rule for the writer | وَفِي الْأَوَّلِ يَجُوزُ إِفْرَادُهُ وَمُطَابَقَتُهُ لِلْمَوْصُوفِ نَحْوُ الزَّيْدَانِ أَف |
| K19:s12 | 19:s12 | noted | note:amal-ism-al-tafdil-wal-masdar, note:ism-al-tafdil-fil-kafiya — ⚠ the engine still misreads the example: «مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة. | نَحْوُ مَا رَأَيْتُ رَجُلًا أَحْسَنَ فِي عَيْنِهِ الْكُحْلُ مِنْهُ فِي عَيْنِ زَيْدٍ فَالْ |
| K20:s1 | 20:s1 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya, note:al-harf-wa-huruf-al-jarr-fil-kafiya | الْفِعْلُ مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ مُقْتَرِنٍ بِأَحَدِ الْأَزْمِنَةِ الثَّلَاث |
| K20:s4 | 20:s4 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya | الْمَاضِي مَا دَلَّ عَلَى زَمَانٍ قَبْلَ زَمَانِكَ |
| K20:s6 | 20:s6 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya | الْمُضَارِعُ مَا أَشْبَهَ الِاسْمَ بِأَحَدِ حُرُوفِ نَأَيْتَ |
| K21:s4 | 21:s4 | applied | engine:AnEngine · I-1, note:nawasib-al-mudari-fil-kafiya | وَأَنْ بَعْدَ أَفْعَالِ الْيَقِينِ كَالْعِلْمِ هِيَ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ لَا ا |
| K21:s6 | 21:s6 | applied | engine:Murib.line | وَإِذَنْ تَنْصِبُ بِشَرْطَيْنِ أَنْ لَا يَعْتَمِدَ مَا بَعْدَهَا عَلَى مَا قَبْلَهَا وَأَن |
| K21:s11 | 21:s11 | applied | engine:Murib.line · lām kay | وَيَجُوزُ إِظْهَارُ أَنْ بَعْدَ لَامِ كَيْ وَحَرْفِ الْعَطْفِ نَحْوُ أَسْلَمْتُ لِأَنْ أَد |
| K22:s4 | 22:s4 | not-automatable | the verb after لَمَّا may be dropped (قَارَبْتُ الْمَدِينَةَ وَلَمَّا) — the elided verb is read from context | وَيَجُوزُ حَذْفُ الْمَنْفِيِّ بِلَمَّا لِقَرِينَةٍ نَحْوُ قَارَبْتُ الْمَدِينَةَ وَلَمَّا  |
| K23:s3 | 23:s3 | not-automatable | the hollow passive's three lughāt (قِيلَ، the ishmām, قُولَ) — pronunciation | وَفِي مَا عَيْنُهُ مُعْتَلَّةٌ الْأَفْصَحُ قِيلَ وَبِيعَ وَجَاءَ فَصِيحًا بِالْإِشْمَامِ و |
| K23:s7 | 23:s7 | not-automatable | ṣarf (the ʿayn turned to alif in يُقَالُ) — the ṣarf engines' ledger | وَفِي مَا عَيْنُهُ مُعْتَلَّةٌ وَاوًا كَانَتْ أَوْ يَاءً تُقْلَبُ الْعَيْنُ أَلِفًا نَحْوُ |
| K24:s1 | 24:s1 | noted | note:al-mutaaddi-wa-afal-al-qulub-fil-kafiya | الْمُتَعَدِّي مَا يَتَوَقَّفُ فَهْمُهُ عَلَى مُتَعَلَّقٍ نَحْوُ ضَرَبَ |
| K24:s2 | 24:s2 | noted | note:al-mutaaddi-wa-afal-al-qulub-fil-kafiya | وَاللَّازِمُ مَا لَا يَتَوَقَّفُ فَهْمُهُ عَلَى مُتَعَلَّقٍ نَحْوُ قَعَدَ |
| K24:s7 | 24:s7 | not-automatable | one object of a heart verb cannot be mentioned without the other — a rule for the writer | وَمِنْ خَوَاصِّهَا أَنَّ مَفْعُولَيْهَا فِي الْأَصْلِ مُبْتَدَأٌ وَخَبَرٌ فَإِذَا ذُكِرَ أ |
| K24:s8 | 24:s8 | applied | engine:Sh336Engine · R208 (ilghāʾ) | وَمِنْهَا جَوَازُ الْإِلْغَاءِ إِذَا تَوَسَّطَتْ أَوْ تَأَخَّرَتْ نَحْوُ زَيْدٌ عَلِمْتُ ق |
| K25:s1 | 25:s1 | noted | note:al-afal-al-naqisa-fil-kafiya | الْأَفْعَالُ النَّاقِصَةُ مَا وُضِعَ لِتَقْرِيرِ الْفَاعِلِ عَلَى صِفَةٍ |
| K25:s10 | 25:s10 | applied | engine:Murib.line | وَيَجُوزُ تَقْدِيمُ أَخْبَارِهَا عَلَى أَسْمَائِهَا إِذَا لَمْ يَمْنَعْ مَانِعٌ نَحْوُ لَي |
| K26:s1 | 26:s1 | noted | note:afal-al-muqaraba-fil-kafiya | أَفْعَالُ الْمُقَارَبَةِ مَا وُضِعَ لِدُنُوِّ الْخَبَرِ رَجَاءً أَوْ حُصُولًا أَوْ أَخْذًا |
| K27:s1 | 27:s1 | noted | note:fil-al-taajjub-fil-kafiya | فِعْلُ التَّعَجُّبِ مَا وُضِعَ لِإِنْشَاءِ التَّعَجُّبِ |
| K27:s2 | 27:s2 | applied | engine:MaEngine · the taʿajjub | وَلَهُ صِيغَتَانِ مَا أَفْعَلَهُ نَحْوُ مَا أَحْسَنَ زَيْدًا وَأَفْعِلْ بِهِ نَحْوُ أَحْسِ |
| K27:s5 | 27:s5 | noted | note:fil-al-taajjub-fil-kafiya | وَلَا بِفَصْلٍ بَيْنَ الْعَامِلِ وَالْمَعْمُولِ وَعِنْدَ الْمَازِنِيِّ يَجُوزُ الْفَصْلُ ب |
| K27:s6 | 27:s6 | applied | engine:MaEngine · the taʿajjub (Sībawayh's parse), note:fil-al-taajjub-fil-kafiya | وَمَا فِي مَا أَفْعَلَهُ عِنْدَ سِيبَوَيْهِ نَكِرَةٌ بِمَعْنَى شَيْءٍ مُبْتَدَأٌ وَأَفْعَل |
| K28:s2 | 28:s2 | applied | engine:Murib.line · نِعْمَ | وَشَرْطُ عَمَلِ نِعْمَ وَبِئْسَ أَحَدُ ثَلَاثَةٍ أَنْ يَكُونَ فَاعِلُهُمَا مُعَرَّفًا بِال |
| K28:s5 | 28:s5 | not-automatable | the specified noun agrees with the doer — a rule for the writer | وَشَرْطُ الْمَخْصُوصِ مُطَابَقَتُهُ لِلْفَاعِلِ إِفْرَادًا وَتَثْنِيَةً وَجَمْعًا وَتَذْكِ |
| K28:s10 | 28:s10 | noted | note:afal-al-madh-wal-dhamm-fil-kafiya — ⚠ the engine still misreads the example: «حَبَّذَا رَجُلًا زَيْدٌ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، حال. | وَيَجُوزُ قَبْلَ مَخْصُوصِهَا وَبَعْدَهُ تَمْيِيزٌ أَوْ حَالٌ مُوَافِقٌ لَهُ نَحْوُ حَبَّذ |
| K29:s1 | 29:s1 | noted | note:al-fil-wal-madi-wal-mudari-fil-kafiya, note:al-harf-wa-huruf-al-jarr-fil-kafiya | الْحَرْفُ مَا دَلَّ عَلَى مَعْنًى فِي غَيْرِهِ |
| K29:s3 | 29:s3 | noted | note:al-harf-wa-huruf-al-jarr-fil-kafiya | حَرْفُ الْجَرِّ مَا وُضِعَ لِلْإِفْضَاءِ بِفِعْلٍ أَوْ مَعْنَاهُ إِلَى مَا يَلِيهِ |
| K31:s6 | 31:s6 | applied | engine:Murib.line · the kāffa on رُبَّ, note:al-lam-wa-rubba-fil-kafiya | وَتَلْحَقُهَا مَا الْكَافَّةُ فَتَدْخُلُ عَلَى الْجُمْلَةِ نَحْوُ رُبَمَا يَوَدُّ الَّذِين |
| K34:s4 | 34:s4 | applied | engine:Murib.line · the kāffa | وَتَلْحَقُهَا مَا الْكَافَّةُ فَتُكَفُّ عَنِ الْعَمَلِ عَلَى الْأَفْصَحِ وَتَدْخُلُ عَلَى  |
| K34:s9 | 34:s9 | not-automatable | after the fāʾ of the answer, إِنَّ or أَنَّ by the meaning intended — meaning | وَحَيْثُ يَجُوزُ التَّقْدِيرَانِ يَجُوزُ الْأَمْرَانِ الْكَسْرَةُ وَالْفَتْحَةُ فَفِي مَنْ |
| K34:s10 | 34:s10 | applied | engine:InnaEngine · both after the surprise إِذَا, note:al-huruf-al-mushabbaha-bil-fil-fil-kafiya | وَفِي كُنْتُ أُرَى زَيْدًا كَمَا قِيلَ سَيِّدًا إِذَا إِنَّهُ عَبْدُ الْقَفَا وَاللَّهَازِ |
| K35:s1 | 35:s1 | applied | engine:Murib.line, note:masail-inna-wal-mukhaffafa-fil-kafiya | وَيَجُوزُ الْعَطْفُ بِالرَّفْعِ عَلَى مَحَلِّ اسْمِ إِنَّ لَفْظًا وَحُكْمًا لِأَنَّهَا لَا |
| K35:s2 | 35:s2 | not-automatable | the condition that the khabar come first before the raised follower — a rule for the writer | وَشَرْطُهُ تَقْدِيمُ الْخَبَرِ لَفْظًا أَوْ تَقْدِيرًا فَلَفْظًا نَحْوُ إِنَّ زَيْدًا قَائ |
| K35:s5 | 35:s5 | applied | engine:InnaEngine · the muzaḥlaqa lām | وَيَجُوزُ دُخُولُ لَامِ الِابْتِدَاءِ مَعَ إِنَّ دُونَ أَنَّ عَلَى خَبَرِهَا نَحْوُ إِنَّ  |
| K35:s6 | 35:s6 | applied | engine:Sh336Engine · R141 | وَتُخَفَّفُ إِنَّ فَتَبْقَى إِنْ وَيَلْزَمُ خَبَرَهَا اللَّامُ لِلْفَرْقِ بَيْنَهَا وَبَيْ |
| K35:s9 | 35:s9 | applied | engine:AnEngine · I-1, note:an-masdariyya, note:masail-inna-wal-mukhaffafa-fil-kafiya | وَيَلْزَمُ أَنْ مَعَ الْفِعْلِ الْمُتَصَرِّفِ غَيْرِ الشَّرْطِ وَالدُّعَاءِ أَحَدُ أَرْبَع |
| K36:s3 | 36:s3 | noted | note:kaanna-lakinna-layta-laalla-fil-kafiya — ⚠ the engine still misreads the example: «وَلَكِنِ اللهُ قَتَلَهُمْ» → حرف لا محل له من الإعراب. | وَتُخَفَّفُ لَكِنَّ فَتَبْقَى لَكِنْ وَتُهْمَلُ وَيَجُوزُ مَجِيءُ الْوَاوِ مَعَ لَكِنَّ |
| K38:s3 | 38:s3 | not-automatable | أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا — Ibn al-Ḥājib forbids, Sībawayh allows — a school dispute | فَلِذَلِكَ لَا يَجُوزُ أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا عِنْدَ الْمُصَنِّفِ لِأَنَّ أَحَدَ  |
| K38:s6 | 38:s6 | noted | note:aw-imma-am-la-bal-lakin-fil-kafiya | وَإِذَا عُطِفَ بِإِمَّا لَزِمَ مَجِيءُ إِمَّا أُخْرَى قَبْلَ الْمَعْطُوفِ عَلَيْهِ نَحْوُ  |
| K38:s9 | 38:s9 | noted | note:huruf-tanbih | حُرُوفُ التَّنْبِيهِ مَا يَقَعُ فِي صَدْرِ الْجُمْلَةِ لِتَنْبِيهِ الْمُخَاطَبِينَ أَلَا و |
| K39:s6 | 39:s6 | noted | note:huruf-al-ziyada-fil-kafiya — ⚠ the engine still misreads the example: «أَيًّا مَا تَدْعُوا فَلَهُ الْأَسْمَاءُ الْحُسْنَى» → اسم، مبني لا يتغير آخره. | وَمَا تُزَادُ مَعَ إِذَا وَمَتَى وَأَيٍّ وَأَيْنَ وَإِنْ وَتُسْتَعْمَلُ هَذِهِ الْكَلِمَات |
| K40:s9 | 40:s9 | noted | note:al-tahdid-wa-qad-wal-istifham-fil-kafiya | وَتُسْتَعْمَلُ الْهَمْزَةُ فِي مُقَابَلَةِ أَمِ الْمُتَّصِلَةِ نَحْوُ أَزَيْدٌ عِنْدَكَ أَ |
| K41:s7 | 41:s7 | noted | note:huruf-al-shart-fil-kafiya | فَإِنْ كَانَ الْخَبَرُ جَامِدًا جَازَ كَوْنُهُ خَبَرًا إِذْ لَا يُمْكِنُ مَجِيءُ الْفِعْلِ |
| K42:s1 | 42:s1 | applied | engine:Murib.line · T3 (the oath first owns the answer) | وَإِذَا تَقَدَّمَ الْقَسَمُ عَلَى الشَّرْطِ فِي صَدْرِ الْكَلَامِ لَزِمَ كَوْنُ الشَّرْطِ  |
| K42:s3 | 42:s3 | not-automatable | an oath in the middle may be heeded or set aside — both stand | وَإِذَا تَوَسَّطَ الْقَسَمُ بِتَقْدِيمِ الشَّرْطِ أَوْ غَيْرِهِ جَازَ اِعْتِبَارُ الْقَسَم |
| K43:s4 | 43:s4 | noted | note:amma-fil-kafiya | وَفِعْلُ أَمَّا مَحْذُوفٌ فَعِنْدَ سِيبَوَيْهِ يُؤْتَى بِجُزْءٍ بَيْنَ أَمَّا وَالْفَاءِ م |
| K44:s7 | 44:s7 | noted | note:kalla-wa-ta-al-tanith-wal-tanwin-fil-kafiya | تَنْوِينُ التَّمَكُّنِ مَا يَدُلُّ عَلَى أَنَّ الْكَلِمَةَ مُنْصَرِفَةٌ نَحْوُ زَيْدٌ وَتَ |
| K44:s8 | 44:s8 | noted | note:kalla-wa-ta-al-tanith-wal-tanwin-fil-kafiya | وَتَنْوِينُ الْعِوَضِ مَا يَلْحَقُ آخِرَ الِاسْمِ عِوَضًا عَنِ الْمُضَافِ إِلَيْهِ نَحْوُ  |
| K46:s3 | 46:s3 | noted | note:tarifat-daftar-al-kafiya | وَالْمَعْنَى مَا يُقْصَدُ بِشَيْءٍ كَمَا يُقْصَدُ بِرَجُلٍ ذَكَرٌ عَاقِلٌ بَالِغٌ |
| K46:s5 | 46:s5 | noted | note:tarifat-daftar-al-kafiya | وَالْخَاصَّةُ مَا يَخْتَصُّ بِشَيْءٍ وَلَا يُوجَدُ فِي غَيْرِهِ |
| K46:s6 | 46:s6 | noted | note:tarifat-daftar-al-kafiya | وَالْمَرْفُوعَاتُ مَا اشْتَمَلَ عَلَى عَلَمِ الْفَاعِلِيَّةِ وَالْمَنْصُوبَاتُ مَا اشْتَمَ |
| D32 | 32 | applied | engine:MamnuEngine · the nine causes | GAYRI MUNSARIF İLLETLERİ |
| D34 | 34 | applied | engine:MamnuEngine · al / iḍāfa restore the kasra | سلاسلا واغلالا |
| D37 | 37 | applied | engine:TartibEngine · the doer first | نصرموسى عيسى … نصرت زيدا … زيد نصر … ما ضرب زيد الا عمروا … انما ضرب زيد عمروا |
| D42 | 42 | open | engine to build: TartibEngine · the object first — probe «ضَرَبَ زَيْدًا غُلَامُهُ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، والضمير مضاف إليه. | ضرب زيدا غلامه … ما ضرب عمروا الا زيد … انما ضرب عمروا زيد … ضربك زيد |
| D47 | 47 | open | probe «ضَرَبَنِي وَأَكْرَمَنِي زَيْدٌ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، فاعل. | ضرني واكرمنى زيد … ضربتواكرمت زيدا … اكرمنى وضربت زيدا |
| D52 | 52 | applied | engine:TartibEngine · the mubtadaʾ first | من ابوك … زيد المنطلق … افضل منك افضل منِّي … زيد قام |
| D58 | 58 | applied | engine:Murib.line | اين زيد … فى الدار رجل … على التمرة مثلها زبدا … عندىانك قاءم |
| D64 | 64 | open | probe «الَّذِي يَأْتِينِي فَلَهُ دِرْهَمٌ» → اسم، مرفوع وعلامة رفعه الضمة الظاهرة، فاعل. | الذى يأتينى فله درهم … الذى فى الدار فله درهم … كل رجل يأتينى فله درهم … كل رجل يأتينى فله |
| D71 | 71 | not-automatable | the mubtadaʾ dropped («الْهِلَالُ وَاللهِ» = هَذَا الْهِلَالُ) — restored from the scene | الهلال والله اى هذا الهلال والله … الحمدلله اهلُ الحمد … اى هو |
| D74 | 74 | applied | engine:Murib.line | خرجت فاذا السبع … اى واقف … لولا زيد لكان كذا … ضربى زيدا قاءما … اى حاصل قاءما … كل رجل و |
| D84 | 84 | applied | engine:DabtEngine · mafʿūl muṭlaq | جلست جلوسا … جلست جِلسة … جلست جَلسة |
| D88 | 88 | open | probe «سَقْيًا لَكَ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، وخبره شبه الجملة «لك» متعلق بمح | خير مقدم … اى قدمت قدوما خير مقدم … سقيا اى سقاك الله سقيا … رعيا اى رعاك الله رعيا … خيبة |
| D100 | 100 | applied | engine:Murib.line | من اضربُ … اِضربْ زيدا … اِمْرأ ونفسه … اُترُكِ امْرأ ونفسه … يا زيدُ اى ادعو زيدا … زيدا  |
| D108 | 108 | applied | engine:NidaEngine | يا زيدُ … يا زيدون … يا لزيدٍ … يا زيداه … يا عبدَالله … يا رجلاً … يا طالعا جبلا |
| D113 | 113 | open | probe «يَا مَالِ» → اسم، منادى. | ترخيم المنادى … يا حارِ اى حارثُ … يا ثمو اى ثمودُ |
| D118 | 118 | open | engine to build: CaseEngine · ẓarf — probe «صُمْتُ دَهْرًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | صمت دهرا … افطرت اليومَ … جلست خلفك … جلست فى المسجد |
| D126 | 126 | applied | engine:MansubEngine · v332 I-18 | ضربتُ زيدا تأديبا … قعدت عن الحرب خُبْنًا |
| D130 | 130 | applied | engine:Murib.line | استوى الماء والخشبةَ … ما لك وزيدا |
| D132 | 132 | open | probe «زَيْدٌ فِي الدَّارِ قَائِمًا» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة. | ضربت زيدا قاءماً … زيد فى الدار قاءماً … هذا زيد قائماً |
| D136 | 136 | applied | engine:MansubEngine · v332 I-9 | عشرون درهما … رطلٌ زيتاً … قفزان برا … طاب زيد نفسا … زيد طيِّبٌ اباً |
| D145 | 145 | applied | engine:IstithnaEngine | جاءنى القوم الا زيداً |
| D149 | 149 | applied | engine:Murib.line | جاءنى الا زيداً القوم … ما فى الدار احد الا حمارا … ما عدا … ما خلا … لا يكون … ما فعلوه ا |
| D155 | 155 | applied | engine:IstithnaEngine · mufarragh | الا زيدٌ … ما ضربنى … ما جائنى من احدٍ الا زيدٌ |
| D159 | 159 | applied | engine:Murib.line · naʿt | SIFAT KAÇ ÇEŞİTTİR? |
| D167 | 167 | applied | engine:TawkidEngine | جائنى زيد زيد … فسجد الملائكة كلهم اجمعون |
| D170 | 170 | open | probe «ضَرَبْتُ زَيْدًا رَأْسَهُ» → اسم، منصوب وعلامة نصبه الفتحة الظاهرة، والضمير مضاف إليه. | جائني زيد اخوك … ضربت زيدا رأسه … سُلِبَ زيد ثوبه … رأيت زيدا حمارا |
| D197 | 197 | applied | engine:Nahw342Engine · fasl / faslOff | زيد هو العالم … زيد هو افضل من عمروٍ |
| D200 | 200 | applied | engine:Murib.line | قل هو الله احد … فانها لاََتَعْمَى الابصارُ |
| D205 | 205 | applied | engine:AdadEngine | جائنى ثلاثة ُ رجالٍ … جائنى خمسةَََََََََ عشرَ رجلاً … جائنى الفان رجلٍ |
| D209 | 209 | applied | engine:Sh336Engine · R92, note:al-fil-wal-madi-wal-mudari-fil-kafiya, note:al-harf-wa-huruf-al-jarr-fil-kafiya | زيد ضارب ابوه … جاء الضارب ابوه … جاء رجل ضارب ابوه … الفعل ما دل على معنى فى نفسه مقترن ب |
| D220 | 220 | applied | engine:Murib.line · I-6 | سرت حتى ادخلها … مرض فلان حتى لايرجونه … لام كى … اسلمتُ لادخلَ الجنة … لام جحود … وما كان |
| D230 | 230 | applied | engine:Murib.line · jawāb al-ṭalab | زرنى اكرمْك … ان تزرْنى اكرمْك … لاتفعلِ الشرّ يكن خيرا لك … ان لم تفعلْه يكن خيرا لك … هل |
| D253 | 253 | applied | engine:Sh336Engine · R209 (taʿlīq) | افعال الناقصة |
| D316 | 316 | applied | engine:InnaEngine.verdict | إِن زيدا قائمٌ … واللهِ إِن زيدا قائمٌ … واَتَيْناَه من الكُنُوزِ ما إن مفاتحه … زيدٌ إنه  |
| D327 | 327 | noted | note:al-huruf-al-mushabbaha-bil-fil-fil-kafiya — ⚠ the engine still misreads the example: «بَلَغَنِي أَنَّكَ قَائِمٌ» → حرف لا محل له من الإعراب. | بَلَغَنِى أنك قاءمٌ … علمتُ أن زيدا قاءمٌ … عِنْدِى أنك قاءم … إجْلِسْ حيثُ أن زيدا جالسٌ  |

