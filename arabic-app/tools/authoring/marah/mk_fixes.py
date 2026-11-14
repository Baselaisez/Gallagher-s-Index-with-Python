#!/usr/bin/env python3
"""mk_fixes.py — the author's corrections of the engines' reading of Marāḥ al-Arwāḥ (parts one to three) → fixes.json.
Run from arabic-app:  python3 tools/authoring/marah/mk_fixes.py
A row gives a rule + case where the builder's template then writes the right line, a key where a homograph was keyed,
or a whole line («irab») where no template says it (the quoted word, the omitted mubtadaʾ, the pronoun of separation)."""
import json, pathlib
H = pathlib.Path(__file__).parent
F = {}
def R(where, rule, k, **kw): F[where] = dict(rule=rule, k=k, **kw)
def K(where, key, **kw): F[where] = dict(F.get(where, {}), key=key, **kw)
def L(where, ar, en, tr, **kw): F[where] = dict(F.get(where, {}), irab={"ar": ar, "en": en, "tr": tr}, **kw)
PLW = ("فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
       "The doer (fa'il), in raf'; the sign is the waw — a sound masculine plural whose nun is dropped for annexation; the pronoun «her/its» is the mudaf ilayh.",
       "Fâil, merfû; alâmeti vâv ile — cem'-i müzekker sâlim, izâfet sebebiyle nûnu düşmüştür; zamir «onun (dişil)» muzâfun ileyh.")
QUOTE = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The word itself is quoted; in the place of jarr as the mudaf ilayh.", "Kelimenin kendisi kastedilmiştir (hikâye); mahallen mecrûr, muzâfun ileyh.")
QFI = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ بِـ«فِي».", "The word itself is quoted; in the place of jarr after «فِي».", "Kelimenin kendisi kastedilmiştir (hikâye); «فِي» ile mahallen mecrûr.")
QATF = ("الْوَاوُ عَاطِفَةٌ، وَلَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ فِي مَحَلِّ جَرٍّ.", "The waw conjoins; a quoted word joined to the one before it, in the place of jarr.", "«ve» + hikâye edilen kelime; öncekine ma'tûf, mahallen mecrûr.")
MM = ("مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ الْفِعْلِ قَبْلَهُ، مِنْ تَمَامِ الْمِثَالِ.", "A cognate object (maf'ul mutlaq), in nasb; the sign is the fatha — the masdar of the verb before it, part of the quoted example.", "Mef'ûl-i mutlak, mansûb; alâmeti fetha ile — önceki fiilin masdarı; misâlin devamıdır.")
NAHW = ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «ذٰلِكَ»، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The khabar of an omitted mubtada («that is»), in raf'; the sign is the damma; annexed (mudaf).", "Hazfedilmiş mübtedânın («bu») haberi, merfû; alâmeti damme ile; muzâf.")
YUQAL = ("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ عَلَى الْحِكَايَةِ — أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «هُوَ»، وَالْجُمْلَةُ نَائِبُ الْفَاعِلِ.", "The deputy doer (na'ib al-fa'il), in raf', the word being quoted — or the khabar of an omitted mubtada («it is»), the clause then being the deputy doer.", "Nâib-i fâil, merfû (hikâye yoluyla) — yahut hazfedilmiş mübtedânın («o») haberi; bu takdirde cümle nâib-i fâildir.")
MAQUL = ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «هٰذَا»، مَرْفُوعٌ بِالضَّمَّةِ، وَالْجُمْلَةُ مَحْكِيَّةٌ بِالْقَوْلِ.", "The khabar of an omitted mubtada («this»), in raf'; the sign is the damma; the clause is what is quoted as said.", "Hazfedilmiş mübtedânın («bu») haberi, merfû; alâmeti damme ile; cümle, sözün mahkîsidir.")
# ---- chapter 1
R("1:s2:5", "badal", "raf")                                    # أَحْمَدُ — the name spells out «الْمُفْتَقِرُ»
L("1:s2:13", "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَ«وَالِدَيْهِ» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "The waw conjoins; the lam is a preposition; «his two parents» is in jarr by the ya — a dual whose nun is dropped for annexation; the pronoun «his» is the mudaf ilayh.",
  "«ve» + lâm harf-i cer; «anne-babası» yâ ile mecrûr — tesniye, izâfet sebebiyle nûnu düşmüştür; zamir «onun» muzâfun ileyh.", pos="noun", key="walid-father")
R("1:s3:2", "innaIsm", "nasb")                                 # عِلْمَ
K("1:s3:7", "ab")                                              # أَبُوهَا — the father, not the name
L("1:s3:11", *PLW, pos="noun", key="darin-knower")             # دَارُوهَا — «those who know it», not دَارَ
L("1:s3:15", *PLW, pos="noun", key="arin-devoid")              # عَارُوهَا
R("1:s4:8", "khabar", "raf")                                   # جَنَاحُ النَّجَاحِ
K("1:s4:10", "rah-palm", pos="noun")
R("1:s4:11", "nat", "raf")                                     # رَحْرَاحٌ
L("1:s4:15", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.", "A past verb; its doer is a hidden pronoun «هُوَ».", "Mâzî fiil; fâili gizli zamirdir «هُوَ».")
L("1:s4:16", "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «هُوَ»، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The khabar of an omitted mubtada («it»), in raf'; the sign is the damma; annexed (mudaf).", "Hazfedilmiş mübtedânın («o») haberi, merfû; alâmeti damme ile; muzâf.")
K("1:s4:19", "rah-palm", pos="noun")
L("1:s5:1", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ أَنَا.", "A present verb in raf'; the sign is the visible damma; its doer is a necessarily hidden pronoun «أَنَا».", "Muzâri fiil, merfû; alâmeti zâhir damme; fâili vücûben gizli zamirdir «أَنَا».")
L("1:s5:3", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ إِلَى «مَا».", "A present verb in raf'; the sign is the visible damma; its doer is a hidden pronoun «هُوَ» returning to «مَا».", "Muzâri fiil, merfû; alâmeti zâhir damme; fâili «مَا»ya dönen gizli zamirdir «هُوَ».", pos="verb", key="wasama")
K("1:s5:7", "nima-verb"); K("1:s5:9", "nima-verb")
L("1:s5:8", "فَاعِلُ «نِعْمَ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The doer of «نِعْمَ», in raf'; the sign is a damma estimated on the alif.", "«نِعْمَ»nin fâili, merfû; alâmeti elif üzerinde takdir edilen damme.")
K("1:s5:10", "muin", pos="noun")
# ---- chapter 2
L("2:s2:11", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ.", "The waw conjoins; joined to the word before it, in raf'; the sign is the alif — a dual whose nun is dropped for annexation.", "«ve» + ma'tûf, merfû; alâmeti elif ile — tesniye, izâfet sebebiyle nûnu düşmüştür.")
# ---- chapter 3
L("3:s1:0", "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The mubtada (subject of the nominal sentence), in raf'; the sign is the damma.", "Mübtedâ, merfû; alâmeti damme ile.")
L("3:s1:1", "ضَمِيرُ فَصْلٍ مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "A pronoun of separation; it has no place in the i'rab.", "Fasıl zamiri; i'rabdan mahalli yoktur.")
L("3:s1:2", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ، وَصِلَتُهُ جُمْلَةُ «لَيْسَ» وَمَا بَعْدَهَا.", "A relative noun, built on sukun, in the place of raf' as the khabar; its sila is the clause of «لَيْسَ».", "İsm-i mevsûl, sükûn üzere mebnî; mahallen merfû, haber; sılası «لَيْسَ» cümlesidir.")
L("3:s1:9", "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of laysa, placed after its khabar, in raf'; the sign is the damma; annexed (mudaf).", "Leyse'nin ismi (muahhar), merfû; alâmeti damme ile; muzâf.")
L("3:s2:2", "اللَّامُ حَرْفُ جَرٍّ، وَ«مَا» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَحُذِفَتْ أَلِفُهَا لِدُخُولِ حَرْفِ الْجَرِّ عَلَيْهَا.", "The lam is a preposition and «مَا» the interrogative noun in the place of jarr; its alif is dropped because a preposition has entered on it: «why?».", "Lâm harf-i cer, «مَا» soru ismi, mahallen mecrûr; harf-i cer dâhil olduğu için elifi düşmüştür: «niçin?».", key="lima", pos="noun")
L("3:s2:3", "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "A past verb in the passive.", "Meçhul mâzî fiil.")
L("3:s5:5", "مَعْطُوفٌ عَلَى خَبَرِ أَنَّ «وَاحِدٌ» مَرْفُوعٌ بِالضَّمَّةِ.", "Joined to the khabar of أَنَّ («one»), in raf'; the sign is the damma.", "Enne'nin haberine («وَاحِدٌ») ma'tûf, merfû; alâmeti damme ile.")
R("3:s5:10", "mubtada", "raf")
R("3:s6:2", "kanaKhabar", "nasb"); R("3:s6:5", "kanaKhabar", "nasb")
K("3:s6:3", "fil")
L("3:s7:3", "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ.", "The khabar (predicate), in raf'; the sign is a damma estimated on the dropped yāʾ — a manqūṣ noun.", "Haber, merfû; alâmeti hazfedilmiş yâ üzerinde takdir edilen damme — menkûs isim.")
L("3:s8:2", *YUQAL)
L("3:s8:4", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "A demonstrative, built on kasra, in the place of nasb as the noun of أَنَّ.", "İsm-i işâret, kesre üzere mebnî; mahallen mansûb, enne'nin ismi.")
# ---- chapter 4
R("4:s1:6", "maful", "nasb")
L("4:s1:9", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The waw conjoins; joined to the word before it, in jarr; the sign is a kasra estimated on the alif.", "«ve» + ma'tûf, mecrûr; alâmeti elif üzerinde takdir edilen kesre.")
L("4:s2:0", "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «أَحَدُهَا»، مَرْفُوعٌ بِالضَّمَّةِ.", "The khabar of an omitted mubtada («one of them»), in raf'; the sign is the damma.", "Hazfedilmiş mübtedânın («onlardan biri») haberi, merfû; alâmeti damme ile.")
R("4:s3:0", "atf", "raf")
L("4:s4:0", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "The waw conjoins; joined to the word before it, in raf'; the sign is the damma — an elative, barred from tanwin.", "«ve» + ma'tûf, merfû; alâmeti damme ile — ism-i tafdîl, gayr-i munsarif.", key="akbar", pos="noun")
for w in ("3:s1:13", "4:s2:9", "4:s3:10", "4:s4:11", "5:s4:4"): L(w, *NAHW)   # نَحْوُ: «وَذٰلِكَ نَحْوُ …»
for w in ("4:s2:10", "4:s3:11", "4:s4:12", "5:s4:9"): L(w, *QUOTE)
L("4:s5:4", "الْهَاءُ لِلتَّنْبِيهِ، وَ«هُنَا» اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ.", "The ha calls attention; «هُنَا» is a demonstrative of place, built on sukun, in the place of nasb as an adverb of place: «here».", "Hâ tenbih içindir; «هُنَا» mekân için ism-i işâret, sükûn üzere mebnî; mahallen mansûb, zarf-ı mekân: «burada».", tags=["al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab", "al-maful-fih-wal-maful-lah"])
R("4:s5:6", "nat", "raf")
# ---- chapter 5
R("5:s1:12", "tamyiz", "nasb"); R("5:s2:8", "hal", "nasb")
for w in ("5:s2:3", "5:s2:10", "5:s6:11", "5:s6:14"): L(w, *QFI, pos="verb")
for w in ("5:s2:5", "5:s2:12"): L(w, *QATF)
L("5:s2:4", *MM, key="ida-promise", pos="noun"); L("5:s2:6", *MM); L("5:s2:11", *MM, key="wajal", pos="noun"); L("5:s2:13", *MM)
L("5:s4:10", "تَوْكِيدٌ لَفْظِيٌّ لِلْفِعْلِ قَبْلَهُ.", "A verbal emphasis (tawkid lafzi) repeating the verb before it.", "Önceki fiili tekrar eden lafzî te'kit.")
L("5:s5:2", *YUQAL)
L("5:s5:4", "خَبَرُ «كَوْن» — مَصْدَرِ كَانَ النَّاقِصَةِ — مَنْصُوبٌ بِالْفَتْحَةِ.", "The khabar of «كَوْن», the masdar of the incomplete kāna, in nasb; the sign is the fatha.", "«كَوْن»ün — nâkıs kâne'nin masdarının — haberi, mansûb; alâmeti fetha ile.")
L("5:s5:9", *MAQUL); L("5:s8:1", *MAQUL)
for w in ("5:s5:10", "5:s8:2"): R(w, "nat", "raf", key="adhb", pos="noun")
for w in ("5:s5:11", "5:s8:3"): K(w, "markab", pos="noun")
for w in ("5:s5:12", "5:s8:4"): R(w, "nat", "raf")
L("5:s5:14", "عَطْفُ بَيَانٍ عَلَى «مَشْرَبٌ» مَرْفُوعٌ بِالضَّمَّةِ.", "An explanatory apposition (atf bayan) to «mashrab», in raf'; the sign is the damma.", "«مَشْرَبٌ» kelimesine atf-ı beyân, merfû; alâmeti damme ile.")
R("5:s5:15", "atf", "raf")
K("5:s7:0", "muakkadiyya", pos="noun")
K("5:s8:9", "sala")
# ================================================================ part two (pp. 22–33): chapters 6–8
QMUD = ("مُضَارِعُهُ، مَحْكِيٌّ مَعَهُ مِنْ تَمَامِ الْمِثَالِ.", "Its mudari', quoted with it — part of the example.", "Onun muzârii; onunla birlikte hikâye edilir, misâlin devamıdır.")
QMUBT = ("الْوَاوُ عَاطِفَةٌ، وَلَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَةُ «لَا يَدْخُلُ».", "The waw conjoins; the word itself is quoted, in the place of raf' as the mubtada; its khabar is the clause «لَا يَدْخُلُ».", "«ve» + kelimenin kendisi kastedilmiştir (hikâye); mahallen merfû mübtedâ; haberi «لَا يَدْخُلُ» cümlesidir.")
QAMMA = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ بَعْدَ «أَمَّا».", "The word itself is quoted; in the place of raf' as the mubtada after «أَمَّا».", "Kelimenin kendisi kastedilmiştir (hikâye); «أَمَّا»dan sonra mahallen merfû mübtedâ.")
QATFR = ("الْوَاوُ عَاطِفَةٌ، وَلَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ فِي مَحَلِّ رَفْعٍ.", "The waw conjoins; a quoted word joined to the one before it, in the place of raf'.", "«ve» + hikâye edilen kelime; öncekine ma'tûf, mahallen merfû.")
QRAF = ("لَفْظٌ مَحْكِيٌّ بِالرَّفْعِ كَمَا ضُبِطَ فِي الْأَصْلِ، فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The word is quoted in raf', as the print vowels it; in the place of jarr as the mudaf ilayh.", "Kelime, baskıda harekelendiği gibi ref' ile hikâye edilmiştir; mahallen mecrûr, muzâfun ileyh.")
MAQJ = ("الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The waw conjoins; joined to the word before it, in jarr; the sign is a kasra estimated on the alif.", "«ve» + ma'tûf, mecrûr; alâmeti elif üzerinde takdîr edilen kesre.")
def DOER(pair): return ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ عَلَى «" + pair + "»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
                        "A present verb in raf'; the sign is the written damma; its doer is a hidden pronoun «هُوَ» going back to «" + pair + "»; the clause is the khabar, in the place of raf'.",
                        "Muzâri fiil, merfû; alâmeti zâhir damme; fâili «" + pair + "»ya dönen müstetir «هُوَ» zamiri; cümle mahallen merfû haberdir.")
# ---- chapter 6
L("6:s1:3", "الْوَاوُ عَاطِفَةٌ، وَ«هُوَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَةُ «يَرْتَقِي».", "The waw conjoins; «هُوَ» is a detached pronoun, built on fatha, in the place of raf' as the mubtada; its khabar is the clause «يَرْتَقِي».", "«ve» + «هُوَ» munfasıl zamir, fetha üzere mebnî, mahallen merfû mübtedâ; haberi «يَرْتَقِي» cümlesidir.")
R("6:s1:5", "mudafIlayh", "jarr", key="sibawayh", pos="noun")
L("6:s1:5", "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ — عَلَمٌ مَخْتُومٌ بِـ«وَيْهِ».", "The mudaf ilayh, built on kasra, in the place of jarr — a proper name ending in «-wayhi».", "Muzâfun ileyh; kesre üzere mebnî, mahallen mecrûr — «وَيْهِ» ile biten özel isim.")
R("6:s1:8", "jarr", "jarr")
L("6:s1:8", "مَجْرُورٌ بِـ«إِلَى» بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى.", "In jarr after «إِلَى»; the sign is the ya, because it is attached to the dual.", "«إِلَى» ile mecrûr; alâmeti yâ ile — tesniyeye mülhak olduğu için.")
R("6:s1:9", "atf", "jarr", key="thalathun")
L("6:s1:9", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "The waw conjoins; joined to the word before it, in jarr; the sign is the ya, because it is attached to the sound masculine plural.", "«ve» + ma'tûf, mecrûr; alâmeti yâ ile — cem'-i müzekker sâlime mülhak olduğu için.")
L("6:s2:0", *NAHW)
for w in ("6:s2:7", "6:s2:8", "6:s2:9", "6:s2:17"): R(w, "atf", "jarr"); L(w, *MAQJ)
R("6:s2:10", "atf", "jarr"); R("6:s2:31", "atf", "jarr")
L("6:s3:2", "مَجْرُورٌ بِـ«عَلَى» بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَحُرِّكَتِ الْيَاءُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، مُضَافٌ.", "In jarr after «عَلَى»; the sign is the ya — a dual whose nun is dropped for annexation; the ya takes a kasra because two unvowelled letters meet; annexed (mudaf).", "«عَلَى» ile mecrûr; alâmeti yâ ile — tesniye, izâfet sebebiyle nûnu düşmüştür; iki sâkin karşılaştığı için yâ kesre ile harekelenmiştir; muzâf.")
L("6:s3:5", *NAHW)
R("6:s3:7", "mafulMutlaq", "nasb")
L("6:s3:7", "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ جَاءَ عَلَى وَزْنِ اسْمِ الْفَاعِلِ، أَيْ: قُمْتُ قِيَامًا.", "A cognate object (maf'ul mutlaq), in nasb; the sign is the fatha — a masdar on the measure of the ism fa'il, that is: «قُمْتُ قِيَامًا».", "Mef'ûl-i mutlak, mansûb; alâmeti fetha ile — ism-i fâil vezninde gelmiş masdar, yani: «قُمْتُ قِيَامًا».")
R("6:s3:8", "khabar", "raf")
L("6:s3:8", "الْوَاوُ عَاطِفَةٌ، وَ«نَحْوُ» خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «ذٰلِكَ»، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الَّتِي قَبْلَهَا.", "The waw conjoins; «نَحْوُ» is the khabar of an omitted mubtada («that is»), in raf' by the damma; annexed (mudaf) — the clause is joined to the one before it.", "«ve» + «نَحْوُ», hazfedilmiş mübtedânın («bu») haberi, damme ile merfû; muzâf — cümle öncekine ma'tûftur.")
L("6:s3:11", "الْبَاءُ حَرْفُ جَرٍّ، وَ«أَيِّ» اسْمُ اسْتِفْهَامٍ مُعْرَبٌ مَجْرُورٌ بِالْبَاءِ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ عَلَى مَا ذَهَبَ إِلَيْهِ الْمُصَنِّفُ.", "The ba is a preposition; «أَيّ» is a declining interrogative noun, in jarr by the kasra, annexed; the pronoun «you» is the mudaf ilayh; the jarr phrase is the fronted khabar, on the reading the author follows.", "Bâ harf-i cer; «أَيّ» mu'rab istifhâm ismi, kesre ile mecrûr, muzâf; «siz» zamiri muzâfun ileyh; câr-mecrûr, musannifin tuttuğu görüşe göre mukaddem haberdir.")
R("6:s3:12", "mubtada", "raf")
L("6:s3:12", "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — مَصْدَرٌ جَاءَ عَلَى وَزْنِ اسْمِ الْمَفْعُولِ عِنْدَ الْمُصَنِّفِ، بِمَعْنَى الْفِتْنَةِ.", "The mubtada, placed after its khabar, in raf'; the sign is the damma — for the author a masdar on the measure of the ism maf'ul, meaning «trial».", "Muahhar mübtedâ, merfû; alâmeti damme ile — musannife göre ism-i mef'ûl vezninde gelmiş masdar; «fitne» mânâsında.")
L("6:s4:2", *NAHW); L("6:s4:3", *QRAF)
for w in ("6:s4:4", "6:s4:5", "6:s4:6"): L(w, *QATF)
for w in ("6:s5:9", "6:s5:12", "6:s5:16", "6:s5:19"): L(w, *QFI, pos="verb")
for w in ("6:s5:10", "6:s5:13", "6:s5:17", "6:s5:20"): R(w, "mafulMutlaq", "nasb"); L(w, *MM)
R("6:s5:14", "atf", "nasb")
# ---- chapter 7
K("7:s1:0", "fil", pos="noun")                                 # الْأَفْعَالُ — the plural of فِعْل, not the measure أَفْعَال
L("7:s1:0", "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَخَبَرُهُ جُمْلَةُ «سِتَّةٌ لِلثُّلَاثِيِّ» الِاسْمِيَّةُ، وَالرَّابِطُ مَحْذُوفٌ تَقْدِيرُهُ «مِنْهَا».", "The waw conjoins; the mubtada, in raf' by the damma; its khabar is the nominal clause «six belong to the three-letter verb», whose link back («of them») is omitted.", "«ve» + mübtedâ, damme ile merfû; haberi «سِتَّةٌ لِلثُّلَاثِيِّ» isim cümlesidir; râbıt («مِنْهَا») hazfedilmiştir.")
L("7:s1:1", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ، وَصِلَتُهُ جُمْلَةُ «تُشْتَقُّ …» الْفِعْلِيَّةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ، وَالْعَائِدُ الضَّمِيرُ فِيهَا.", "A relative noun, built on sukun, in the place of raf' as a na't; its sila is the verbal clause «تُشْتَقُّ …», which has no place in the i'rab; the returning pronoun is inside it.", "İsm-i mevsûl, sükûn üzere mebnî, mahallen merfû sıfat; sılası «تُشْتَقُّ …» fiil cümlesidir, i'rabdan mahalli yoktur; âid içindeki zamirdir.")
L("7:s1:5", "الْوَاوُ اعْتِرَاضِيَّةٌ، وَ«هِيَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ مُعْتَرِضَةٌ بَيْنَ الْمُبْتَدَإِ وَخَبَرِهِ.", "The waw opens a parenthesis; «هِيَ» is a detached pronoun, built on fatha, in the place of raf' as a mubtada; the clause stands between the mubtada and its khabar.", "Vâv i'tirâziyyedir; «هِيَ» munfasıl zamir, fetha üzere mebnî, mahallen merfû mübtedâ; cümle, mübtedâ ile haberi arasında mu'tarızadır.")
L("7:s1:7", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "The waw conjoins; joined to the word before it, in raf'; the sign is the waw, because it is attached to the sound masculine plural.", "«ve» + ma'tûf, merfû; alâmeti vâv ile — cem'-i müzekker sâlime mülhak olduğu için.")
R("7:s1:9", "mubtada", "raf")
L("7:s1:9", "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «لِلثُّلَاثِيِّ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ الْأَوَّلِ.", "A second mubtada, in raf' by the damma; its khabar is the jarr phrase «لِلثُّلَاثِيِّ»; the clause is the khabar of the first mubtada, in the place of raf'.", "İkinci mübtedâ, damme ile merfû; haberi «لِلثُّلَاثِيِّ» câr-mecrûrudur; cümle, ilk mübtedânın mahallen merfû haberidir.")
L("7:s2:0", *NAHW); L("7:s2:1", *QUOTE)
for w in ("7:s2:3", "7:s2:5", "7:s2:7", "7:s2:9", "7:s2:11"): L(w, *QATF)
for w in ("7:s2:2", "7:s2:4", "7:s2:6", "7:s2:8", "7:s2:10", "7:s2:12", "7:s4:1", "7:s5:2", "7:s5:4", "7:s6:2", "7:s6:4", "7:s6:6", "7:s7:1", "7:s8:1", "7:s9:3", "7:s9:9", "7:s9:13", "7:s9:15"): L(w, *QMUD)
L("7:s3:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The waw conjoins; a present verb in the passive, in raf'; the sign is a damma estimated on the alif.", "«ve» + meçhul muzâri fiil, merfû; alâmeti elif üzerinde takdîr edilen damme.")
R("7:s3:2", "nat", "raf")
R("7:s3:3", "maful2", "nasb")
L("7:s3:3", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالْمَفْعُولُ الْأَوَّلُ صَارَ نَائِبَ الْفَاعِلِ.", "The second object, in nasb; the sign is the fatha; annexed (mudaf) — the first object has become the deputy doer.", "İkinci mef'ûl, mansûb; alâmeti fetha ile; muzâf — birinci mef'ûl nâib-i fâil olmuştur.")
for w in ("7:s4:0", "7:s7:0", "7:s8:0"): L(w, *QMUBT)
L("7:s4:3", *DOER("فَتَحَ يَفْتَحُ")); L("7:s7:3", *DOER("كَرُمَ يَكْرُمُ")); L("7:s8:3", *DOER("حَسِبَ يَحْسِبُ"))
L("7:s5:1", *QAMMA); L("7:s5:3", *QATFR)
FAAMMA = ("الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ«مِنْ» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "The fa answers «أَمَّا»; «مِنْ» is a preposition, built on sukun, given a fatha because two unvowelled letters meet.", "Fâ «أَمَّا»nın cevabındadır; «مِنْ» harf-i cer, sükûn üzere mebnî; iki sâkin karşılaştığı için fetha ile harekelenmiştir.")
L("7:s5:5", *FAAMMA)
L("7:s5:6", "مَجْرُورٌ بِـ«مِنْ» بِالْكَسْرَةِ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ الْمُبْتَدَإِ.", "In jarr after «مِنْ»; the sign is the kasra; the jarr phrase is the khabar of the mubtada.", "«مِنْ» ile mecrûr; alâmeti kesre ile; câr-mecrûr mübtedânın haberidir.")
L("7:s6:1", *QAMMA, key="baqiya", pos="verb")
L("7:s6:3", *QATFR, key="faniya", pos="verb"); L("7:s6:5", *QATFR)
L("7:s6:7", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَخَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fa answers «أَمَّا»; the khabar (predicate), in raf'; the sign is the damma; annexed (mudaf).", "Fâ «أَمَّا»nın cevabındadır; haber, merfû; alâmeti damme ile; muzâf.")
K("7:s6:8", "ibn", pos="noun")                                  # بَنِي — the sons of, not the diminutive بُنَيّ
L("7:s6:8", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ.", "The mudaf ilayh, in jarr; the sign is the ya, because it is attached to the sound masculine plural; its nun is dropped for annexation; annexed (mudaf).", "Muzâfun ileyh, mecrûr; alâmeti yâ ile — cem'-i müzekker sâlime mülhak olduğu için; izâfet sebebiyle nûnu düşmüştür; muzâf.")
R("7:s6:9", "mudafIlayh", "jarr")
R("7:s9:2", "fail", "raf")
L("7:s9:2", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ فَاعِلُ «جَاءَ».", "The word itself is quoted; in the place of raf' as the doer of «جَاءَ».", "Kelimenin kendisi kastedilmiştir (hikâye); mahallen merfû, «جَاءَ»nın fâili.")
L("7:s9:6", "«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَصِلَتُهُ جُمْلَةُ «قَالَ …» الْفِعْلِيَّةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ، وَالْعَائِدُ الضَّمِيرُ فِيهَا.", "«مَنْ» is a relative noun, built on sukun, in the place of jarr as the mudaf ilayh; its sila is the verbal clause «قَالَ …», which has no place in the i'rab; the returning pronoun is inside it.", "«مَنْ» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr muzâfun ileyh; sılası «قَالَ …» fiil cümlesidir, i'rabdan mahalli yoktur; âid içindeki zamirdir.")
L("7:s9:8", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ — بِضَمِّ الْكَافِ عَلَى هٰذِهِ اللُّغَةِ.", "The word itself is quoted; in the place of nasb as what is said — with a damma on the kaf in this dialect.", "Kelimenin kendisi kastedilmiştir (hikâye); mahallen mansûb, mekûlü'l-kavl — bu lügate göre kâfın zammıyla.", key="kada", pos="verb")
L("7:s9:10", "الْوَاوُ عَاطِفَةٌ، وَ«هِيَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The waw conjoins; «هِيَ» is a detached pronoun, built on fatha, in the place of raf' as the mubtada.", "«ve» + «هِيَ» munfasıl zamir, fetha üzere mebnî, mahallen merfû mübtedâ.")
R("7:s9:11", "khabar", "raf")
L("7:s9:12", "الْكَافُ جَارَّةٌ، وَ«فَضِلَ» لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ بِالْكَافِ.", "The kaf is a preposition; «فَضِلَ» is a quoted word, in the place of jarr after the kaf.", "Kâf harf-i cer; «فَضِلَ» hikâye edilen kelimedir, kâf ile mahallen mecrûr.", key="fadala", pos="verb")
L("7:s9:14", *QATF, key="dama", pos="verb")
# ---- chapter 8
R("8:s1:0", "mubtada", "raf", key="ithnan", pos="noun")
L("8:s1:0", "الْوَاوُ عَاطِفَةٌ، وَ«اثْنَا» مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «لِمُنْشَعِبَةِ».", "The waw conjoins; «اثْنَا» is the mubtada, in raf'; the sign is the alif, because it is attached to the dual; its khabar is the jarr phrase «لِمُنْشَعِبَةِ».", "«ve» + «اثْنَا» mübtedâ, merfû; alâmeti elif ile — tesniyeye mülhak olduğu için; haberi «لِمُنْشَعِبَةِ» câr-mecrûrudur.")
L("8:s1:1", "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ، مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — قَامَ مَقَامَ نُونِ الْمُثَنَّى.", "The second part of the compound number, built on fatha, with no place in the i'rab — it stands where the dual's nun stood.", "Mürekkep sayının ikinci cüz'ü; fetha üzere mebnî, i'rabdan mahalli yoktur — tesniye nûnunun yerine geçmiştir.", key="ashar", pos="noun")
L("8:s2:0", *NAHW); L("8:s2:1", *QUOTE)
R("8:s2:2", "mafulMutlaq", "nasb"); L("8:s2:2", *MM)
for i in range(3, 14): L("8:s2:%d" % i, *QATF)
L("8:s3:0", "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَ«هُمَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The mubtada, in raf' by the damma; annexed; the pronoun «the two of them» is the mudaf ilayh.", "Mübtedâ, damme ile merfû; muzâf; «o ikisi» zamiri muzâfun ileyh.")
L("8:s3:1", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَهُوَ الْأَصْلُ قَبْلَ الْإِدْغَامِ.", "The word itself is quoted; in the place of raf' as the khabar — the underlying form before the contraction.", "Kelimenin kendisi kastedilmiştir (hikâye); mahallen merfû haber — idgamdan önceki asıl.", key="ihmarra-xi", pos="verb")
L("8:s3:2", *QATFR, key="ihmarra", pos="verb")
L("8:s3:3", "الْفَاءُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "The fa conjoins; a past verb in the passive, built on fatha; the alif is an attached pronoun, in the place of raf' as the deputy doer.", "Fâ atıf; meçhul mâzî fiil, fetha üzere mebnî; elif muttasıl zamir, mahallen merfû nâib-i fâil.")
L("8:s4:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.", "The waw conjoins; a present verb in raf'; the sign is the written damma.", "«ve» + muzâri fiil, merfû; alâmeti zâhir damme.")
L("8:s4:2", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ فَاعِلُ «يَدُلُّ».", "The word itself is quoted; in the place of raf' as the doer of «يَدُلُّ».", "Kelimenin kendisi kastedilmiştir (hikâye); mahallen merfû, «يَدُلُّ»nun fâili.")
L("8:s4:3", "الْوَاوُ عَاطِفَةٌ، وَ«هُوَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «مِنْ بَابِ».", "The waw conjoins; «هُوَ» is a detached pronoun, built on fatha, in the place of raf' as the mubtada; its khabar is the jarr phrase «مِنْ بَابِ».", "«ve» + «هُوَ» munfasıl zamir, fetha üzere mebnî, mahallen merfû mübtedâ; haberi «مِنْ بَابِ» câr-mecrûrudur.")
L("8:s4:6", *QUOTE)
for w in ("8:s5:2", "8:s6:3", "8:s7:3", "8:s8:3", "8:s9:3"): L(w, *NAHW)
for w in ("8:s5:3", "8:s6:4", "8:s7:2", "8:s7:4", "8:s8:2", "8:s8:4", "8:s9:2", "8:s9:4"): L(w, *QUOTE)
for w in ("8:s6:5", "8:s6:6", "8:s7:5", "8:s7:6", "8:s7:7", "8:s7:8", "8:s7:9", "8:s8:5", "8:s8:6", "8:s9:5"): L(w, *QATF)
L("8:s8:7", *QATF, key="tarahwaka", pos="verb"); L("8:s8:8", *QATF, key="tamaskana", pos="verb")
R("8:s9:0", "mubtada", "raf")
L("8:s9:0", "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «لِمُلْحَقِ».", "The waw conjoins; the mubtada, in raf'; the sign is the alif, because it is attached to the dual; its khabar is the jarr phrase «لِمُلْحَقِ».", "«ve» + mübtedâ, merfû; alâmeti elif ile — tesniyeye mülhak olduğu için; haberi «لِمُلْحَقِ» câr-mecrûrudur.")
R("8:s10:3", "mudafIlayh", "jarr")
# every quoted verb keeps its lemma and its part of speech, whatever the engine's pass makes of a word standing alone
VQ = {
    "6:s5:9": "kallama", "6:s5:12": "qatala-fight", "6:s5:16": "tahammala", "6:s5:19": "zalzala", "7:s2:1": "daraba", "7:s2:2": "daraba",
    "7:s2:3": "qatala", "7:s2:4": "qatala", "7:s2:5": "alima", "7:s2:6": "alima", "7:s2:7": "fataha", "7:s2:8": "fataha",
    "7:s2:9": "karuma", "7:s2:10": "karuma", "7:s2:11": "hasiba", "7:s2:12": "hasiba", "7:s3:0": "samma", "7:s4:0": "fataha",
    "7:s4:1": "fataha", "7:s4:3": "dakhala", "7:s5:1": "rakana", "7:s5:2": "rakana", "7:s5:3": "aba", "7:s5:4": "aba",
    "7:s6:2": "baqiya", "7:s6:4": "faniya", "7:s6:5": "qalaa", "7:s6:6": "qalaa", "7:s7:0": "karuma", "7:s7:1": "karuma",
    "7:s7:3": "dakhala", "7:s8:0": "hasiba", "7:s8:1": "hasiba", "7:s8:3": "dakhala", "7:s9:3": "faala", "7:s9:9": "kada",
    "7:s9:13": "fadala", "7:s9:15": "dama", "8:s2:1": "akrama", "8:s2:3": "qattaa", "8:s2:4": "qatala-fight", "8:s2:5": "tafaddala",
    "8:s2:6": "tadaraba", "8:s2:7": "insarafa", "8:s2:8": "ihtaqara", "8:s2:9": "istakhraja", "8:s2:10": "ikhshawshana", "8:s2:11": "ijlawwadha",
    "8:s2:12": "ihmarra-xi", "8:s2:13": "ihmarra", "8:s3:3": "adghama", "8:s4:0": "dalla", "8:s4:2": "iraawa", "8:s5:3": "dahraja",
    "8:s6:4": "ihranjama", "8:s6:5": "iqshaarra", "8:s6:6": "tadahraja", "8:s7:2": "dahraja", "8:s7:4": "shamlala", "8:s7:5": "hawqala",
    "8:s7:6": "baytara", "8:s7:7": "jahwara", "8:s7:8": "qalsa", "8:s7:9": "qalnasa", "8:s8:2": "tadahraja", "8:s8:4": "tajalbaba",
    "8:s8:5": "tajawraba", "8:s8:6": "tashaytana", "8:s9:2": "ihranjama", "8:s9:4": "iqansasa", "8:s9:5": "islanqa",
}
for w, k in VQ.items(): F[w]["key"] = k; F[w]["pos"] = "verb"
# ================================================================ part three (pp. 34–40): chapters 9–10
QILA = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ بِـ«إِلَى».", "The word itself is quoted; in the place of jarr after «إِلَى».", "Kelimenin kendisi kastedilmiştir (hikâye); «إِلَى» ile mahallen mecrûr.")
QALA = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ بِـ«عَلَى».", "The word itself is quoted; in the place of jarr after «عَلَى».", "Kelimenin kendisi kastedilmiştir (hikâye); «عَلَى» ile mahallen mecrûr.")
def BIMA(v): return ("الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ خَبَرُ «" + v + "»، وَصِلَتُهُ الظَّرْفُ بَعْدَهُ.",
                     "The ba is an extra preposition strengthening the negation; «مَا» is a relative noun, built on sukun, in the place of nasb as the khabar of «" + v + "»; its sila is the adverb after it.",
                     "Bâ, nefyi pekiştiren zâid harf-i cerdir; «مَا» ism-i mevsûl, sükûn üzere mebnî, mahallen mansûb, «" + v + "»nin haberi; sılası sonraki zarftır.")
WASL = ("الْوَاوُ حَالِيَّةٌ، وَ«إِنْ» وَصْلِيَّةٌ — شَرْطِيَّةٌ لَا جَوَابَ لَهَا تُفِيدُ التَّعْمِيمَ — مَبْنِيَّةٌ عَلَى السُّكُونِ.", "The waw is circumstantial; «إِنْ» is the linking in — a conditional with no answer, meaning «even if» — built on sukun.", "Vâv hâliyyedir; «إِنْ» vasliyyedir — cevabı olmayan, «…se de» mânâsında şart edatı — sükûn üzere mebnî.")
THAMMA = ("اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ بِـ«مِنْ» — «مِنْ ثَمَّ»: مِنْ أَجْلِ ذٰلِكَ.", "A demonstrative of distant place («there»), built on fatha, in the place of jarr after «مِنْ» — «مِنْ ثَمَّ»: hence, for that reason.", "Uzak mekân için ism-i işâret («orada»), feth üzere mebnî, «مِنْ» ile mahallen mecrûr — «مِنْ ثَمَّ»: bundan dolayı.")
# ---- chapter 9
L("9:s1:0", "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«هُوَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَةُ «يَجِيءُ».", "The waw opens a new sentence; «هُوَ» is a detached pronoun, built on fatha, in the place of raf' as the mubtada; its khabar is the clause «يَجِيءُ».", "Vâv isti'nâfiyyedir; «هُوَ» munfasıl zamir, feth üzere mebnî, mahallen merfû mübtedâ; haberi «يَجِيءُ» cümlesidir.")
L("9:s1:3", "الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمُرَكَّبِ «أَرْبَعَةَ عَشَرَ»، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْعَدَدُ فِي مَحَلِّ جَرٍّ بِـ«عَلَى».", "The first half of the compound number «fourteen», built on fatha; the number sits in the place of jarr after «عَلَى».", "«On dört» mürekkeb sayısının ilk cüzü, feth üzere mebnî; sayı «عَلَى» ile mahallen mecrûrdur.")
L("9:s1:4", "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ، مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "The second half of the compound number, built on fatha; it has no place in the i'rab.", "Mürekkeb sayının ikinci cüzü, feth üzere mebnî; i'rabdan mahalli yoktur.")
L("9:s1:6", *NAHW); L("9:s1:7", *QUOTE); L("9:s1:9", *QILA)
for w in ("9:s2:1", "9:s7:6", "9:s7:13"): K(w, "bana", pos="verb")   # بُنِيَ — «was built», never the sons of
R("9:s3:3", "maful", "nasb")
L("9:s3:3", "مَفْعُولٌ بِهِ لِلْمَصْدَرِ «مُشَابَهَة» مَنْصُوبٌ بِالْفَتْحَةِ — وَالْمَصْدَرُ مُضَافٌ إِلَى فَاعِلِهِ.", "The object of the masdar «مُشَابَهَة», in nasb; the sign is the fatha — the masdar is annexed to its doer.", "«مُشَابَهَة» masdarının mef'ûlün bihi, mansûb; alâmeti fetha ile — masdar fâiline muzâftır.")
L("9:s3:8", *NAHW)
L("9:s3:9", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A past verb, built on sukun because the doer's ta is attached; the ta is the doer; the whole sentence is quoted, in the place of jarr as the mudaf ilayh.", "Mâzî fiil, fâil tâsı bitiştiği için sükûn üzere mebnî; tâ fâildir; cümle hikâye edilmiştir, mahallen mecrûr muzâfun ileyh.", key="marra", pos="verb")
L("9:s3:11", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ إِلَى «رَجُلٍ»، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لَهُ.", "A past verb, built on fatha; its doer is a hidden pronoun «هُوَ» going back to «رَجُلٍ»; the clause is in the place of jarr as its na't.", "Mâzî fiil, feth üzere mebnî; fâili «رَجُلٍ»e dönen müstetir «هُوَ» zamiri; cümle mahallen mecrûr, onun sıfatıdır.")
R("9:s3:12", "atf", "jarr")
L("9:s3:12", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ عَلَى مَحَلِّ جُمْلَةِ «ضَرَبَ» مَجْرُورٌ بِالْكَسْرَةِ.", "The waw conjoins; joined to the place of the clause «ضَرَبَ», in jarr; the sign is the kasra.", "«ve» + «ضَرَبَ» cümlesinin mahalline ma'tûf, mecrûr; alâmeti kesre ile.")
R("9:s6:11", "mafulLah", "nasb")
# ---- chapter 10
L("10:s1:9", *QALA)
R("10:s1:10", "mabni", "keep"); L("10:s1:10", *QATF, key="hum", pos="pron"); L("10:s1:11", *QATF, key="hunna", pos="pron")
L("10:s2:3", *QFI); L("10:s2:7", *QUOTE)
LAYSAT = ("فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "A frozen incomplete past verb, one of kāna's sisters, built on fatha; the ta marks the feminine; its noun is a hidden pronoun «هِيَ».", "Câmid nâkıs mâzî fiil, kâne'nin kardeşlerinden, feth üzere mebnî; tâ te'nis içindir; ismi müstetir «هِيَ» zamiridir.")
L("10:s2:10", "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ يَعُودُ إِلَى «الْمِيمَ»، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "A frozen incomplete past verb, one of kāna's sisters, built on fatha; the ta marks the feminine; its noun is a hidden pronoun «هِيَ» going back to «الْمِيمَ»; the clause is the khabar of أَنَّ.", "Câmid nâkıs mâzî fiil, kâne'nin kardeşlerinden, feth üzere mebnî; tâ te'nis içindir; ismi «الْمِيمَ»e dönen müstetir «هِيَ» zamiri; cümle enne'nin haberidir.", key="laysa", pos="verb")
L("10:s7:2", *LAYSAT, key="laysa", pos="verb")
L("10:s2:11", *BIMA("لَيْسَ")); L("10:s3:7", *BIMA("يَكُنْ"))
L("10:s3:2", *QFI)
L("10:s3:3", *WASL); L("10:s14:12", *WASL)
L("10:s4:3", *QFI); L("10:s4:12", *QUOTE); L("10:s4:13", *QATF)
L("10:s6:5", *QFI)
R("10:s6:2", "maful2", "nasb")
L("10:s6:2", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — وَالْمَفْعُولُ الْأَوَّلُ صَارَ نَائِبَ الْفَاعِلِ.", "The second object, in nasb; the sign is the fatha — the first object has become the deputy doer.", "İkinci mef'ûl, mansûb; alâmeti fetha ile — birinci mef'ûl nâib-i fâil olmuştur.")
R("10:s6:11", "mubtada", "raf")
L("10:s6:11", "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins a clause to a clause; the mubtada, in raf'; the sign is the damma.", "«ve» cümleyi cümleye bağlar; mübtedâ, merfû; alâmeti damme ile.")
R("10:s6:13", "khabar", "raf")
L("10:s6:13", "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ.", "The khabar (predicate), in raf'; the sign is a damma estimated on the dropped yāʾ — a manqūṣ noun.", "Haber, merfû; alâmeti hazfedilmiş yâ üzerinde takdir edilen damme — menkûs isim.")
L("10:s7:3", "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَ«ضَمِيرٍ» خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "The ba is an extra preposition strengthening the negation; «ضَمِيرٍ» is the khabar of laysa — in jarr in wording, in nasb in place.", "Bâ, nefyi pekiştiren zâid harf-i cerdir; «ضَمِيرٍ» leyse'nin haberi — lafzan mecrûr, mahallen mansûb.")
L("10:s8:4", *QUOTE); L("10:s8:5", *QATF)
for w in ("10:s9:1", "10:s11:1"): L(w, *THAMMA, key="thamma", pos="noun")
L("10:s9:16", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ تَوْكِيدٌ لِلضَّمِيرِ الْمُتَّصِلِ — التَّاءِ.", "A detached pronoun, built on fatha, in the place of raf': an emphasis (tawkid) of the attached pronoun, the ta.", "Munfasıl zamir, feth üzere mebnî, mahallen merfû: muttasıl zamirin — tânın — te'kididir.")
L("10:s10:1", *QUOTE)
L("10:s8:12", "«فِي» حَرْفُ جَرٍّ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِـ«فِي»، وَصِلَتُهُ الْجُمْلَةُ الِاسْمِيَّةُ بَعْدَهُ «هُوَ كَالْكَلِمَةِ».", "«فِي» is a preposition; «مَا» is a relative noun, built on sukun, in the place of jarr after it; its sila is the nominal clause after it, «هُوَ كَالْكَلِمَةِ».", "«فِي» harf-i cerdir; «مَا» ism-i mevsûl, sükûn üzere mebnî, onunla mahallen mecrûr; sılası sonraki isim cümlesidir: «هُوَ كَالْكَلِمَةِ».")
L("10:s11:5", *QFI)
L("10:s11:8", *[F["5:s5:4"]["irab"][k_] for k_ in ("ar", "en", "tr")])
L("10:s11:15", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ — لُغَةٌ رَدِيَّةٌ فِي «رَمَتَا».", "The word itself is quoted; in the place of nasb as what is said — a poor dialect's form of «رَمَتَا».", "Kelimenin kendisi kastedilmiştir (hikâye); mahallen mansûb, mekûlü'l-kavl — «رَمَتَا»nın zayıf bir lehçedeki şekli.")
L("10:s12:2", *QUOTE)
L("10:s14:3", *QFI)
L("10:s14:14", "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِـ«لَمْ»، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.", "An incomplete present verb, in jazm after «لَمْ»; the sign is the dropping of the nun — one of the five verbs; the alif is the attached pronoun, its noun.", "Nâkıs muzâri fiil, «لَمْ» ile meczûm; alâmeti nûnun hazfi — ef'âl-i hamsedendir; elif muttasıl zamir, ismidir.", key="kana", pos="verb")
L("10:s16:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ الظَّرْفُ «بَيْنَ» بَعْدَهُ — أَوْ ضَمِيرُ الْمَصْدَرِ.", "The waw conjoins; a past verb in the passive, built on fatha; its deputy doer is the adverb «بَيْنَ» after it — or the pronoun of the masdar.", "«ve» + meçhul mâzî fiil, feth üzere mebnî; nâib-i fâili sonraki «بَيْنَ» zarfıdır — yahut masdarın zamiri.", key="sawwa", pos="verb")
L("10:s16:2", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَحُرِّكَتِ الْيَاءُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، مُضَافٌ.", "The mudaf ilayh, in jarr; the sign is the ya — a dual whose nun is dropped for annexation; the ya takes a kasra because two sukuns meet; annexed (mudaf).", "Muzâfun ileyh, mecrûr; alâmeti yâ ile — tesniye, izâfet sebebiyle nûnu düşmüştür; iki sâkin yan yana geldiği için yâ kesrelenmiştir; muzâf.")
VQ3 = {"9:s1:7": "daraba", "9:s1:9": "daraba", "9:s3:11": "daraba", "10:s2:3": "daraba", "10:s2:7": "rama", "10:s3:2": "radiya", "10:s4:3": "daraba", "10:s4:12": "hadara",
       "10:s4:13": "qatala", "10:s6:5": "daraba", "10:s8:4": "daraba", "10:s8:5": "daraba", "10:s10:1": "daraba", "10:s11:5": "rama", "10:s11:15": "rama", "10:s12:2": "daraba", "10:s14:3": "daraba"}
for w, k in VQ3.items(): F[w]["key"] = k; F[w]["pos"] = "verb"
for w in ("10:s14:14", "10:s16:2"): F[w]["enc"] = ""                # تَكُونَا: the alif is the doer's; تَثْنِيَتَيِ: the yāʾ is the dual's letter
F["10:s14:14"]["grammar"] = ["nawasib-wa-jawazim-al-mudari", "al-muthanna", "kana-wa-akhawatuha"]; F["10:s16:2"]["grammar"] = ["idafa-definiteness", "al-muthanna"]
L("10:s14:7", "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ.", "The doer (fa'il), in raf'; the sign is the alif — a dual whose nun is dropped for annexation; annexed (mudaf).", "Fâil, merfû; alâmeti elif ile — tesniye, izâfet sebebiyle nûnu düşmüştür; muzâf.", grammar=["fail", "al-muthanna", "idafa-definiteness"])
KHILB = ("الْبَاءُ حَرْفُ جَرٍّ، وَ«خِلَافِ» مَجْرُورٌ بِهِ بِالْكَسْرَةِ، مُضَافٌ.", "The ba is a preposition; «خِلَافِ» is in jarr after it; the sign is the kasra; annexed (mudaf).", "Bâ harf-i cerdir; «خِلَافِ» onunla mecrûr; alâmeti kesre ile; muzâf.")
L("10:s10:0", *KHILB)
L("10:s2:6", "الْوَاوُ عَاطِفَةٌ، وَ" + KHILB[0], "The waw conjoins; " + KHILB[1][0].lower() + KHILB[1][1:], "«ve» + " + KHILB[2][0].lower() + KHILB[2][1:])
MITHLFI = ("مَجْرُورٌ بِـ«فِي» بِالْكَسْرَةِ، مُضَافٌ.", "In jarr after «فِي»; the sign is the kasra; annexed (mudaf).", "«فِي» ile mecrûr; alâmeti kesre ile; muzâf.")
for w in ("10:s4:11", "10:s5:8", "10:s8:3"): L(w, *MITHLFI)
L("10:s12:1", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "The mudaf ilayh, in jarr; the sign is the kasra; annexed (mudaf).", "Muzâfun ileyh, mecrûr; alâmeti kesre ile; muzâf.")
F["9:s1:9"]["enc"] = ""                                        # ضَرَبْنَا: the نَا is the doer's, no object pronoun
# tags and enclitics the builder would otherwise read off the engine's first guess
for w, tg in (("6:s1:8", ["huruf-jarr", "al-muthanna"]), ("6:s4:3", ["idafa-definiteness"]), ("7:s9:12", ["huruf-jarr"]), ("8:s1:0", ["mubtada-khabar", "al-muthanna"]), ("8:s1:1", []), ("8:s3:1", ["mubtada-khabar"]), ("8:s3:2", ["atf-nasaq"]), ("8:s8:7", ["atf-nasaq"]), ("8:s8:8", ["atf-nasaq"])): F[w]["grammar"] = tg
for w in ("8:s8:7", "8:s8:8"): F[w]["enc"] = ""                # تَرَهْوَكَ، تَمَسْكَنَ: the kāf and the nūn are radicals, no pronoun
# ================================================================ part four (pp. 40–45): chapters 11–12
QKHA = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».", "The word itself is quoted; in the place of raf' as the khabar of «أَنَّ».", "Lafzı kastedilerek hikâye edilmiş söz; «أَنَّ»nin haberi olarak mahallen merfû.")
QISM = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ» — وَالظَّرْفُ قَبْلَهُ مُتَعَلِّقٌ بِالْخَبَرِ «مُضْمَرٌ».", "The word itself is quoted; in the place of nasb as the ism of «أَنَّ» — the ẓarf before it belongs to the khabar «مُضْمَرٌ».", "Lafzı kastedilerek hikâye edilmiş söz; «أَنَّ»nin ismi olarak mahallen mansûb — önündeki zarf, haber olan «مُضْمَرٌ»a bağlıdır.")
QKH = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.", "The word itself is quoted; in the place of raf' as the khabar of the mubtada.", "Lafzı kastedilerek hikâye edilmiş söz; mübtedânın haberi olarak mahallen merfû.")
QSAR = ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ نَصْبٍ خَبَرُ «صَارَ».", "The word itself is quoted; in the place of nasb as the khabar of «صَارَ».", "Lafzı kastedilerek hikâye edilmiş söz; «صَارَ»nin haberi olarak mahallen mansûb.")
MLAH = ("مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The maf'ul li-ajlih (object of reason), in nasb; the sign is the fatha.", "Mef'ûlün lieclih, mansûb; alâmeti fetha ile.")
KHANNA = ("خَبَرُ «أَنَّ» مَرْفُوعٌ بِالضَّمَّةِ.", "The khabar of «أَنَّ», in raf'; the sign is the damma.", "«أَنَّ»nin haberi, merfû; alâmeti damme ile.")
NAIBR = ("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "The deputy doer (na'ib al-fa'il), in raf'; the sign is the damma.", "Nâib-i fâil, merfû; alâmeti damme ile.")
ASLM = ("مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The mubtada, in raf'; the sign is the damma; annexed, and the hāʾ is an attached pronoun in the place of jarr as the mudaf ilayh.", "Mübtedâ, merfû; alâmeti damme ile; muzâftır, hâ ise mahallen mecrûr muzâfun ileyh olan bitişik zamirdir.")
def PASS(pre_ar, pre_en, pre_tr, tail_ar="", tail_en="", tail_tr=""):
    return (pre_ar + "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ" + tail_ar + ".", pre_en + "a passive past verb, built on fatha" + tail_en + ".", pre_tr + "meçhul mâzî fiil, feth üzere mebnî" + tail_tr + ".")
WAW = ("الْوَاوُ عَاطِفَةٌ، وَ", "The waw conjoins; ", "«ve» atıf harfi; ")
FA = ("الْفَاءُ عَاطِفَةٌ، وَ", "The fa conjoins; ", "«fe» atıf harfi; ")
# ---- chapter 11
L("11:s1:3", *QFI)
R("11:s2:5", "fail", "raf"); L("11:s2:5", "فَاعِلُ «حَيَّا» مَرْفُوعٌ بِالضَّمَّةِ.", "The doer (fa'il) of «حَيَّا», in raf'; the sign is the damma.", "«حَيَّا» fiilinin fâili, merfû; alâmeti damme ile.")
R("11:s2:6", "mabni", "keep"); L("11:s2:6", "الْفَاءُ عَاطِفَةٌ، وَ«كَيْفَ» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "The fa conjoins; «كَيْفَ» is an interrogative noun, built on fatha, in the place of raf' as the fronted khabar.", "«fe» atıf harfi; «كَيْفَ» feth üzere mebnî soru ismi, mukaddem haber olarak mahallen merfû.")
R("11:s2:7", "mabni", "keep"); L("11:s2:7", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ، وَالْأَلِفُ لِلْإِشْبَاعِ تَوَلَّدَتْ مِنْ فَتْحَةِ التَّاءِ — وَهُوَ مَوْضِعُ الشَّاهِدِ.", "A detached pronoun, built on fatha, in the place of raf' as the postponed mubtada; the alif is one of lengthening, born of the tāʾ's fatha — this is the point the verse is cited for.", "Feth üzere mebnî munfasıl zamir, muahhar mübtedâ olarak mahallen merfû; elif işbâ içindir, tânın fethasından doğmuştur — beytin şâhit getirildiği yer burasıdır.", key="anta", pos="pron")
K("11:s3:4", "waffa", pos="verb")
L("11:s3:4", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ «حَتَّى»، وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "A passive mudari', in nasb through an «أَنْ» that must stay hidden after «حَتَّى»; the sign is a fatha estimated on the alif, which cannot carry it.", "Meçhul muzâri, «حَتَّى»dan sonra vücûben gizlenen «أَنْ» ile mansûb; alâmeti elif üzerinde takdir edilen fethadır.")
L("11:s3:7", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ، وَصِلَتُهُ جُمْلَةُ «ضَمِنْتَا» وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ «ضَمِنْتَهُ».", "A relative noun, built on sukun, in the place of nasb as the second object; its ṣila is the clause «ضَمِنْتَا», and the returning pronoun is dropped — «ضَمِنْتَهُ».", "Sükûn üzere mebnî ism-i mevsûl, ikinci mef'ûl olarak mahallen mansûb; sılası «ضَمِنْتَا» cümlesidir, âid zamir hazfedilmiştir: «ضَمِنْتَهُ».")
L("11:s3:8", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْأَلِفُ لِلْإِشْبَاعِ — وَهُوَ مَوْضِعُ الشَّاهِدِ.", "A past verb, built on sukun because the doer's tāʾ is attached; the tāʾ is an attached pronoun, built on fatha, in the place of raf' as the doer; the alif is one of lengthening — the point the verse is cited for.", "Fâil tâsı bitiştiği için sükûn üzere mebnî mâzî fiil; tâ, feth üzere mebnî bitişik zamir olup fâil olarak mahallen merfûdur; elif işbâ içindir — beytin şâhit getirildiği yer burasıdır.", enc="")
L("11:s4:0", *PASS(*WAW, "، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "; the tāʾ is the feminine marker, given a kasra because two still letters meet", "; tâ te'nîs içindir, iki sâkin bir araya geldiği için kesre ile harekelenmiştir"))
L("11:s4:3", *QFI)
R("11:s4:6", "mabni", "keep"); L("11:s4:6", *QISM, key="antuma", pos="pron")
L("11:s5:2", *QFI, key="antuma", pos="pron")
R("11:s5:10", "mafulLah", "nasb"); L("11:s5:10", "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — وَالتَّقْدِيرُ: وَقِيلَ أُدْخِلَتْ تَبَعًا لِـ«هُمَا».", "The maf'ul li-ajlih, in nasb; the sign is the fatha — the full wording: «and it is said: it was brought in to follow humā».", "Mef'ûlün lieclih, mansûb; alâmeti fetha ile — takdiri: «وَقِيلَ أُدْخِلَتْ تَبَعًا لِهُمَا».")
L("11:s5:11", "اللَّامُ حَرْفُ جَرٍّ، وَ«هُمَا» لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ فِي مَحَلِّ جَرٍّ بِاللَّامِ — وَلِذٰلِكَ كُسِرَتِ اللَّامُ.", "The lam is a preposition; «هُمَا» is the word itself, quoted, in the place of jarr after the lam — which is why the lam keeps its kasra.", "Lâm harf-i cerdir; «هُمَا» lafzı kastedilerek hikâye edilmiş olup lâm ile mahallen mecrûrdur — lâmın kesreli kalması bundandır.", enc="")
L("11:s6:3", *QFI); L("11:s6:5", *QATF); L("11:s6:7", *QATF)
L("11:s7:0", *PASS(*WAW, "، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ يَعُودُ إِلَى «التَّاءِ»", "; the tāʾ is the feminine marker, and the deputy doer is a hidden pronoun (she) returning to «التَّاء»", "; tâ te'nîs içindir, nâib-i fâil «التَّاء»ya dönen gizli «هِيَ» zamiridir"))
R("11:s7:3", "mafulLah", "nasb"); L("11:s7:3", *MLAH)
L("11:s7:7", "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ «إِنَّ».", "The waw conjoins; «لَا» is the la that denies the whole kind, and it governs like «إِنَّ».", "«ve» atıf harfi; «لَا» cinsi nefyeden lâdır, «إِنَّ» gibi amel eder.")
L("11:s7:8", "اسْمُ «لَا» النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا شِبْهُ الْجُمْلَةِ بَعْدَهُ.", "The ism of the la that denies the kind, built on fatha, in the place of nasb; its khabar is the jarr phrase after it.", "Cinsi nefyeden «لَا»nın ismi, feth üzere mebnî, mahallen mansûb; haberi, ardından gelen şibh-i cümledir.")
R("11:s8:1", "mafulLah", "nasb"); L("11:s8:1", "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — وَالتَّقْدِيرُ: وَقِيلَ ضُمَّتِ اتِّبَاعًا لِلْمِيمِ.", "The maf'ul li-ajlih, in nasb; the sign is the fatha — the full wording: «and it is said: it was given a damma to follow the mim».", "Mef'ûlün lieclih, mansûb; alâmeti fetha ile — takdiri: «وَقِيلَ ضُمَّتِ اتِّبَاعًا لِلْمِيمِ».")
L("11:s9:3", *QFI)
L("11:s10:8", *QKHA)
K("11:s11:7", "wajada", pos="verb")
R("11:s11:11", "naib", "raf"); L("11:s11:11", *NAIBR)
L("11:s11:12", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "An adverb of place, in nasb; the sign is the fatha; annexed, the hāʾ being its mudaf ilayh; the phrase stands in the place of raf' as the fronted khabar.", "Mekân zarfı, mansûb; alâmeti fetha ile; muzâftır, hâ muzâfun ileyhtir; şibh-i cümle mukaddem haber olarak mahallen merfûdur.")
R("11:s11:13", "mubtada", "raf"); L("11:s11:13", "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْجُمْلَةُ «قَبْلَهَا مَضْمُومٌ» فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«وَاوٌ».", "The postponed mubtada, in raf'; the sign is the damma; the clause «قَبْلَهَا مَضْمُومٌ» stands in the place of raf' as the attribute of «وَاوٌ».", "Muahhar mübtedâ, merfû; alâmeti damme ile; «قَبْلَهَا مَضْمُومٌ» cümlesi «وَاوٌ»un sıfatı olarak mahallen merfûdur.")
R("11:s11:16", "mabni", "keep"); L("11:s11:16", *QFI, key="huwa", pos="pron")
L("11:s12:1", *THAMMA, key="thamma", pos="noun")
R("11:s12:6", "naib", "raf"); K("11:s12:6", "dalw", pos="noun")
L("11:s12:6", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِـ«يُقَالُ» — جَمْعُ «دَلْوٍ» عَلَى أَفْعُلٍ، مَنْقُوصٌ حُذِفَتْ يَاؤُهُ وَعُوِّضَ عَنْهَا التَّنْوِينُ.", "The word itself is quoted; in the place of raf' as the deputy doer of «يُقَالُ» — the plural of «دَلْو» on afʿul, a manqūṣ whose yāʾ fell and was made up for by the tanwin.", "Lafzı kastedilerek hikâye edilmiş söz; «يُقَالُ»nun nâib-i fâili olarak mahallen merfû — «دَلْو»ün أَفْعُل vezninde cem'i; yâsı düşmüş, yerine tenvin gelmiş menkûs isim.")
R("11:s12:7", "mubtada", "raf"); L("11:s12:7", *ASLM)
R("11:s12:8", "khabar", "raf"); K("11:s12:8", "dalw", pos="noun")
L("11:s12:8", "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ الْأَصْلُ قَبْلَ قَلْبِ الْوَاوِ يَاءً.", "The khabar of the mubtada, in raf'; the sign is the damma — the original form, before the wāw was turned into a yāʾ.", "Mübtedânın haberi, merfû; alâmeti damme ile — vâvın yâya çevrilmesinden önceki asıl.", enc="")
R("11:s12:11", "maful2", "nasb"); L("11:s12:11", *[F["10:s6:2"]["irab"][k_] for k_ in ("ar", "en", "tr")])
L("11:s13:0", *KHILB); L("11:s13:1", *QUOTE)
L("11:s14:0", "الْوَاوُ عَاطِفَةٌ، وَ" + KHILB[0], "The waw conjoins; " + KHILB[1][0].lower() + KHILB[1][1:], "«ve» + " + KHILB[2][0].lower() + KHILB[2][1:])
L("11:s14:1", *QUOTE, enc="")
# ---- chapter 12
L("12:s1:0", *PASS(*WAW))
R("12:s1:1", "naib", "raf"); L("12:s1:1", *NAIBR)
L("12:s1:3", *QFI); L("12:s1:5", *QUOTE); L("12:s1:8", *QKHA)
L("12:s1:9", *PASS(*FA))
L("12:s2:1", *THAMMA, key="thamma", pos="noun")
K("12:s2:2", "abdala", pos="verb")
R("12:s2:3", "naib", "raf"); L("12:s2:3", *NAIBR)
R("12:s2:9", "mubtada", "raf"); L("12:s2:9", *ASLM)
R("12:s3:1", "mubtada", "raf"); L("12:s3:1", ASLM[0][:-1] + "، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِـ«قِيلَ».", ASLM[1][:-1] + "; the nominal clause stands in the place of raf' as the deputy doer of «قِيلَ».", ASLM[2][:-1] + "; isim cümlesi «قِيلَ»nin nâib-i fâili olarak mahallen merfûdur.")
L("12:s3:2", *QKH)
L("12:s3:3", *PASS(*FA, "، وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ يَكُونَ …»", "; its deputy doer is the masdar read out of «أَنْ يَكُونَ …»", "; nâib-i fâili «أَنْ يَكُونَ …»den te'vil edilen masdardır"))
L("12:s3:6", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ اسْمُ «يَكُونَ»، وَصِلَتُهُ الظَّرْفُ «قَبْلَ النُّونِ».", "A relative noun, built on sukun, in the place of raf' as the ism of «يَكُونَ»; its ṣila is the ẓarf «قَبْلَ النُّونِ».", "Sükûn üzere mebnî ism-i mevsûl, «يَكُونَ»nun ismi olarak mahallen merfû; sılası «قَبْلَ النُّونِ» zarfıdır.")
R("12:s4:6", "mudafIlayh", "jarr"); L("12:s4:6", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "The mudaf ilayh, in jarr; the sign is the yāʾ, since it is a dual.", "Muzâfun ileyh, mecrûr; alâmeti yâ ile, çünkü tesniyedir.")
K("12:s4:12", "alama", pos="noun")
L("12:s5:0", *PASS(*FA))
L("12:s5:7", *PASS("", "", "", "، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ إِلَى «النُّونِ»", "; its deputy doer is a hidden pronoun (he) returning to «النُّون»", "; nâib-i fâili «النُّون»a dönen gizli «هُوَ» zamiridir"))
F["12:s5:7"]["irab"]["en"] = F["12:s5:7"]["irab"]["en"][0].upper() + F["12:s5:7"]["irab"]["en"][1:]; F["12:s5:7"]["irab"]["tr"] = F["12:s5:7"]["irab"]["tr"][0].upper() + F["12:s5:7"]["irab"]["tr"][1:]
L("12:s5:9", *QSAR)
L("12:s6:2", "اللَّامُ حَرْفُ جَرٍّ، وَ«مَ» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، حُذِفَتْ أَلِفُهُ لِدُخُولِ حَرْفِ الْجَرِّ عَلَيْهِ.", "The lam is a preposition; «مَ» is the interrogative «مَا», built on sukun, in the place of jarr — its alif fell because a preposition entered on it.", "Lâm harf-i cerdir; «مَ» soru ismi «مَا»dır, sükûn üzere mebnî, mahallen mecrûr — başına harf-i cer geldiği için elifi düşmüştür.", key="lima", pos="part")
L("12:s6:6", *QFI)
R("12:s6:10", "mabni", "keep"); L("12:s6:10", *QISM, key="ana", pos="pron")
R("12:s6:11", "innaKhabar", "raf"); L("12:s6:11", *KHANNA)
L("12:s8:3", *QFI, enc="")
R("12:s8:6", "mabni", "keep"); L("12:s8:6", *QISM, key="nahnu", pos="pron")
R("12:s8:7", "innaKhabar", "raf"); L("12:s8:7", *KHANNA)
L("12:s9:6", "الْبَاءُ حَرْفُ جَرٍّ، وَ«ضَرَبْنَ» لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِالْبَاءِ.", "The ba is a preposition; «ضَرَبْنَ» is the word itself, quoted, in the place of jarr after the ba.", "Bâ harf-i cerdir; «ضَرَبْنَ» lafzı kastedilerek hikâye edilmiş olup bâ ile mahallen mecrûrdur.")
L("12:s9:8", *QSAR, enc="")
# (wave 183, the doer audit) two passive māḍī lines the engine wrote as active ones
L("11:s5:0", *PASS(*WAW, "، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ يَعُودُ إِلَى «الْمِيمِ»", "; the tāʾ is the feminine marker, and the deputy doer is a hidden pronoun (she) returning to «الْمِيم»", "; tâ te'nîs içindir, nâib-i fâil «الْمِيم»e dönen gizli «هِيَ» zamiridir"))
L("11:s6:0", *PASS(*WAW, "، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "; the tāʾ is the feminine marker, given a kasra because two still letters meet", "; tâ te'nîs içindir, iki sâkin bir araya geldiği için kesre ile harekelenmiştir"))
VQ4 = ["11:s1:3", "11:s4:3", "11:s6:3", "11:s6:5", "11:s6:7", "11:s9:3", "11:s10:8", "11:s13:1", "11:s14:1", "12:s1:3", "12:s1:5", "12:s1:8", "12:s3:2", "12:s5:9", "12:s6:6", "12:s8:3", "12:s9:6", "12:s9:8"]
for w in VQ4: F[w]["key"] = "daraba"; F[w]["pos"] = "verb"
# ================================================================ part five (pp. 45–49)
def PRONM(waw_ar, waw_en, waw_tr, pron, bina_ar, bina_en, bina_tr, verb):
    return (waw_ar + "«" + pron + "» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى " + bina_ar + " فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَةُ «" + verb + "».",
            waw_en + "«" + pron + "» is a detached pronoun, built on " + bina_en + ", in the place of raf' as the mubtada; its khabar is the clause «" + verb + "».",
            waw_tr + "«" + pron + "» munfasıl zamir, " + bina_tr + " üzere mebnî, mahallen merfû mübtedâ; haberi «" + verb + "» cümlesidir.")
HALW = ("الْوَاوُ حَالِيَّةٌ أَوِ اسْتِئْنَافِيَّةٌ، وَ", "The waw is circumstantial, or opens a new sentence; ", "Vâv hâliyye yahut isti'nâfiyyedir; ")
def BADALM(of, case_ar, case_en, case_tr, sign_ar, sign_en, sign_tr):
    return ("بَدَلٌ مِنْ «" + of + "» — بَدَلُ مُفَصَّلٍ مِنْ مُجْمَلٍ — " + case_ar + " " + sign_ar + ".",
            "A badal of «" + of + "» — the detail after the sum — " + case_en + "; the sign is " + sign_en + ".",
            "«" + of + "»den bedel — mücmelden sonra mufassal — " + case_tr + "; alâmeti " + sign_tr + ".")
def NUM1(name_ar, name_en, name_tr, mahall_ar, mahall_en, mahall_tr):
    return ("الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ الْمُرَكَّبِ «" + name_ar + "»، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْعَدَدُ " + mahall_ar + ".",
            "The first half of the compound number «" + name_en + "», built on fatha; the number " + mahall_en + ".",
            "«" + name_tr + "» mürekkeb sayısının ilk cüzü, feth üzere mebnî; sayı " + mahall_tr + ".")
def ITHNA(pre_ar, pre_en, pre_tr, role_ar, role_en, role_tr, alif=True, tail_ar="", tail_en="", tail_tr=""):
    return (pre_ar + "الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ «اثْنَا عَشَرَ»، مُعْرَبٌ إِعْرَابَ الْمُثَنَّى: " + role_ar + (" بِالْأَلِفِ" if alif else " بِالْيَاءِ") + " لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، وَحُذِفَتْ نُونُهُ لِقِيَامِ «عَشَرَ» مَقَامَهَا" + tail_ar + ".",
            pre_en + "the first half of the number «twelve», declined like a dual: " + role_en + "; the sign is " + ("the alif" if alif else "the yāʾ") + " — it follows the dual, and its nūn is dropped because «عَشَرَ» stands in its place" + tail_en + ".",
            pre_tr + "«on iki» sayısının ilk cüzü, tesniye gibi mu'rabdır: " + role_tr + "; alâmeti " + ("elif" if alif else "yâ") + " ile — tesniyeye mülhaktır, nûnu «عَشَرَ» onun yerini tuttuğu için düşmüştür" + tail_tr + ".")
def CAP(t): return (t[0], t[1][0].upper() + t[1][1:], t[2][0].upper() + t[2][1:])
ASHAR2 = tuple(F["9:s1:4"]["irab"][k_] for k_ in ("ar", "en", "tr"))                       # the second half of a compound number, built on fatḥa
ASHARI = ("الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ، مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — قَامَ مَقَامَ نُونِ الْمُثَنَّى.",
          "The second half of the number, built on fatha; it has no place in the i'rab — it stands where the dual's nūn stood.",
          "Sayının ikinci cüzü, feth üzere mebnî; i'rabdan mahalli yoktur — tesniye nûnunun yerini tutmuştur.")
def QUO(mahall_ar, mahall_en, mahall_tr):
    return ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، " + mahall_ar + ".", "The word itself is quoted; " + mahall_en + ".", "Kelimenin kendisi kastedilmiştir (hikâye); " + mahall_tr + ".")
# ---- chapter 13
L("13:s1:5", *PRONM(*HALW, "هِيَ", "الْفَتْحِ", "fatha", "feth", "تَرْتَقِي"))
R("13:s2:3", "innaKhabar", "raf")
R("13:s2:4", "badal", "raf"); L("13:s2:4", *BADALM("ثَلَاثَةٌ", "مَرْفُوعٌ", "in raf'", "merfû", "بِالضَّمَّةِ", "the damma", "damme ile"))
R("13:s2:5", "atf", "raf")
R("13:s3:2", "kanaIsm", "raf"); R("13:s3:4", "kanaKhabar", "nasb")
R("13:s3:5", "mafulLah", "nasb"); L("13:s3:5", *MLAH)
R("13:s6:3", "jarr", "jarr")
L("13:s6:3", "اسْمٌ مَجْرُورٌ بِالْبَاءِ الْمُؤَخَّرَةِ عَنْهُ، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — وَهُوَ مِثَالُ الْمُمْتَنِعِ: تَقْدِيمُ الْمَجْرُورِ عَلَى الْجَارِّ.",
  "In jarr by the bāʾ that is set after it; the sign is the kasra — the author's example of what cannot be said: the majrūr put before its jārr.",
  "Kendisinden sonraya bırakılmış bâ ile mecrûr; alâmeti kesre ile — söylenemeyecek olanın misâli: mecrûrun cârdan öne geçmesi.")
R("13:s6:4", "mabni", "keep")
L("13:s6:4", "حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى الْكَسْرِ، أُخِّرَ عَنْ مَجْرُورِهِ فِي هٰذَا الْمِثَالِ الْمُمْتَنِعِ.",
  "A preposition, built on kasra; in this impossible example it is set after the word it governs.",
  "Harf-i cer, kesre üzere mebnî; bu imkânsız misâlde mecrûrundan sonraya bırakılmıştır.", key="bi")
R("13:s7:3", "badal", "raf"); L("13:s7:3", *BADALM("خَمْسَةٌ", "مَرْفُوعٌ", "in raf'", "merfû", "بِالضَّمَّةِ", "the damma", "damme ile"))
R("13:s7:4", "nat", "raf"); R("13:s7:6", "atf", "raf"); R("13:s7:7", "nat", "raf"); R("13:s7:9", "atf", "raf"); R("13:s7:10", "nat", "raf")
L("13:s8:5", *PRONM(*HALW, "هُوَ", "الْفَتْحِ", "fatha", "feth", "يَحْتَمِلُ"))
R("13:s8:7", "mabni", "keep"); L("13:s8:7", *NUM1("ثَمَانِيَةَ عَشَرَ", "eighteen", "On sekiz", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "sits in the place of nasb as the object", "mahallen mansûb mef'ûlün bihtir"))
R("13:s8:8", "mabni", "keep"); L("13:s8:8", *ASHAR2)
R("13:s8:12", "badal", "nasb"); L("13:s8:12", *BADALM("ثَمَانِيَةَ عَشَرَ", "مَنْصُوبٌ", "in nasb", "mansûb", "بِالْفَتْحَةِ", "the fatha", "fetha ile"))
K("13:s8:17", "mukhataba", pos="noun")
K("13:s9:0", "iktafa", pos="verb")
L("13:s9:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ يَعُودُ إِلَى الْوَاضِعِ الْمَفْهُومِ مِنَ الْمَقَامِ.",
  "The waw conjoins; a past verb, built on a fatha estimated on the alif; its doer is a hidden pronoun «هُوَ» — the one who laid the language down, understood from the context.",
  "«ve» atıf harfi; elif üzerinde mukadder feth üzere mebnî mâzî fiil; fâili gizli zamir «هُوَ» — makamdan anlaşılan vâzıa (dili koyana) döner.")
R("13:s9:4", "jarr", "jarr")
L("13:s9:4", "الْبَاءُ حَرْفُ جَرٍّ، وَ«اشْتِرَاكِ» مَجْرُورٌ بِهِ بِالْكَسْرَةِ، مُضَافٌ.", "The ba is a preposition; «اشْتِرَاكِ» is in jarr after it; the sign is the kasra; annexed (mudaf).", "Bâ harf-i cerdir; «اشْتِرَاكِ» onunla mecrûr; alâmeti kesre ile; muzâf.")
R("13:s9:5", "mudafIlayh", "jarr")
L("13:s11:10", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّهُ مُذَكَّرٌ».",
  "A present verb in the passive, in raf'; the sign is the visible damma; its deputy doer is the masdar read out of «أَنَّهُ مُذَكَّرٌ».",
  "Muzâri fiil (meçhul), merfû; alâmeti zâhir damme; nâib-i fâili «أَنَّهُ مُذَكَّرٌ»den çıkan müevvel masdardır.")
R("13:s12:2", "fail", "raf"); L("13:s12:2", *CAP(ITHNA("", "", "", "فَاعِلُ «بَقِيَ» مَرْفُوعٌ", "the doer of «بَقِيَ», in raf'", "«بَقِيَ»nin fâili, merfû")))
R("13:s12:3", "mabni", "keep"); L("13:s12:3", *ASHARI)
R("13:s13:8", "kanaKhabar", "nasb")
L("13:s13:8", "الْجُزْءُ الْأَوَّلُ مِنَ الْعَدَدِ «اثْنَا عَشَرَ»، خَبَرُ «صَارَ»، وَحَقُّهُ النَّصْبُ بِالْيَاءِ «اثْنَيْ»، وَوَرَدَ فِي الطَّبْعَةِ بِالْأَلِفِ فَأَثْبَتْنَاهُ كَمَا وَرَدَ.",
  "The first half of the number «twelve», the khabar of «صَارَ»; by rule it would stand in nasb with a yāʾ, «اثْنَيْ»; the printing has the alif, and we keep what it prints.",
  "«On iki» sayısının ilk cüzü, «صَارَ»nin haberi; kıyâsen yâ ile mansûb «اثْنَيْ» olmalıydı; baskıda elif ile geçer, biz de geldiği gibi bıraktık.")
R("13:s13:9", "mabni", "keep"); L("13:s13:9", *ASHARI)
R("13:s13:12", "kanaIsm", "raf")
R("13:s13:15", "kanaKhabar", "nasb")
L("13:s13:16", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَاللَّامُ لِلْبُعْدِ وَالْكَافُ حَرْفُ خِطَابٍ.",
  "A demonstrative, built on sukun, in the place of jarr as the mudaf ilayh; the lam marks distance and the kaf is the letter of address.",
  "İsm-i işâret, sükûn üzere mebnî, mahallen mecrûr muzâfun ileyh; lâm uzaklık içindir, kâf hitap harfidir.")
R("13:s14:5", "jarr", "jarr"); L("13:s14:5", *CAP(ITHNA("", "", "", "مَجْرُورٌ بِـ«فِي»", "in jarr after «فِي»", "«فِي» ile mecrûr", alif=False)))
R("13:s14:6", "mabni", "keep"); L("13:s14:6", *ASHARI)
R("13:s14:7", "fail", "raf")
L("13:s12:0", "الْفَاءُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "The fa conjoins; a past verb.", "«bunun üzerine» + mâzî fiil.")                       # its doer is «اثْنَا عَشَرَ»
L("13:s14:0", "الْفَاءُ عَاطِفَةٌ، وَفِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.", "The fa conjoins; a present verb, in raf'.", "«bunun üzerine» + muzâri fiil, merfû.")   # its doer is «سِتُّونَ»
R("13:s15:0", "mubtada", "raf"); L("13:s15:0", *CAP(ITHNA("", "", "", "مُبْتَدَأٌ مَرْفُوعٌ", "the mubtada, in raf'", "mübtedâ, merfû", tail_ar="، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «لِلْمَرْفُوعِ»", tail_en="; its khabar is the jarr phrase «لِلْمَرْفُوعِ»", tail_tr="; haberi «لِلْمَرْفُوعِ» câr-mecrûrudur")))
R("13:s15:1", "mabni", "keep"); L("13:s15:1", *ASHARI)
L("13:s15:4", *NAHW)
K("13:s15:5", "daraba", pos="verb"); L("13:s15:5", *QUOTE)
K("13:s15:7", "daraba", pos="verb"); L("13:s15:7", *QILA, enc="")
R("13:s16:0", "mubtada", "raf"); L("13:s16:0", *ITHNA(*WAW, "مُبْتَدَأٌ مَرْفُوعٌ", "the mubtada, in raf'", "mübtedâ, merfû", tail_ar="، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «لِلْمَرْفُوعِ»", tail_en="; its khabar is the jarr phrase «لِلْمَرْفُوعِ»", tail_tr="; haberi «لِلْمَرْفُوعِ» câr-mecrûrudur"))
R("13:s16:1", "mabni", "keep"); L("13:s16:1", *ASHARI)
L("13:s16:4", *NAHW)
R("13:s16:5", "mabni", "keep")
L("13:s16:5", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ «هُوَ ضَرَبَ» مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "A detached pronoun, built on fatha, in the place of raf' as the mubtada; the clause «هُوَ ضَرَبَ» is quoted, in the place of jarr as the mudaf ilayh.",
  "Munfasıl zamir, feth üzere mebnî, mahallen merfû mübtedâ; «هُوَ ضَرَبَ» cümlesi hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir.")
K("13:s16:6", "daraba", pos="verb")
L("13:s16:6", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «هُوَ».",
  "A past verb; its doer is a hidden pronoun «هُوَ»; the clause is the khabar of «هُوَ», in the place of raf'.", "Mâzî fiil; fâili gizli zamirdir «هُوَ»; cümle «هُوَ»nin haberidir, mahallen merfû.")
R("13:s16:8", "mabni", "keep")
L("13:s16:8", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ «نَحْنُ ضَرَبْنَا» مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ بِـ«إِلَى».",
  "A detached pronoun, built on damma, in the place of raf' as the mubtada; the clause «نَحْنُ ضَرَبْنَا» is quoted, in the place of jarr after «إِلَى».",
  "Munfasıl zamir, damm üzere mebnî, mahallen merfû mübtedâ; «نَحْنُ ضَرَبْنَا» cümlesi hikâye edilmiştir, «إِلَى» ile mahallen mecrûrdur.")
K("13:s16:9", "daraba", pos="verb")
L("13:s16:9", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا» الْفَاعِلِينَ، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «نَحْنُ».",
  "A past verb, built on sukun because the «نَا» of the doers is joined to it; «نَا» is its doer; the clause is the khabar of «نَحْنُ», in the place of raf'.",
  "Mâzî fiil; fâil «نَا»sına bitiştiği için sükûn üzere mebnî; «نَا» fâildir; cümle «نَحْنُ»nün haberidir, mahallen merfû.", enc="")
# ---- chapter 14
L("14:s1:2", *QFI, key="huwa", pos="pron")
L("14:s1:4", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِـ«أَنْ»، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ، وَنَائِبُ الْفَاعِلِ الْأَلْفَاظُ الْمَحْكِيَّةُ بَعْدَهُ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ «الْأَصْلُ».",
  "A present verb in the passive, in nasb after «أَنْ»; the sign is the visible fatha; its deputy doer is the quoted words after it, and the masdar read out of «أَنْ يُقَالَ» is the khabar of the mubtada «الْأَصْلُ».",
  "Muzâri fiil (meçhul), «أَنْ» ile mansûb; alâmeti zâhir fetha; nâib-i fâili ondan sonra hikâye edilen lafızlardır; «أَنْ يُقَالَ»den çıkan müevvel masdar «الْأَصْلُ» mübtedâsının haberidir.")
QNAIB = QUO("فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِـ«يُقَالَ» — الْمُفْرَدُ", "in the place of raf' as the deputy doer of «يُقَالَ» — the singular", "«يُقَالَ»nin nâib-i fâili olarak mahallen merfû — müfred")
L("14:s1:5", *QNAIB, key="huwa", pos="pron")
L("14:s1:6", *QUO("مَعْطُوفٌ عَلَى مَا قَبْلَهُ بِحَذْفِ الْعَاطِفِ — الْمُثَنَّى فِي الْأَصْلِ", "joined to the word before it with the conjunction left out — the dual, in its original pattern", "atıf harfi hazfedilerek öncekine ma'tûf — asıl itibarıyla tesniye"), key="huwa", pos="pron")
L("14:s1:7", *QUO("مَعْطُوفٌ عَلَى مَا قَبْلَهُ بِحَذْفِ الْعَاطِفِ — الْجَمْعُ فِي الْأَصْلِ", "joined to the word before it with the conjunction left out — the plural, in its original pattern", "atıf harfi hazfedilerek öncekine ma'tûf — asıl itibarıyla cemi"), key="huwa", pos="pron")
R("14:s2:4", "maful2", "nasb")
L("14:s2:8", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَ«هُمَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "The mudaf ilayh, in jarr; the sign is the yāʾ, for it is a dual whose nūn is dropped for annexation; «هُمَا» is an attached pronoun, the mudaf ilayh.",
  "Muzâfun ileyh, mecrûr; alâmeti yâ ile — tesniyedir, izâfet sebebiyle nûnu düşmüştür; «هُمَا» bitişik zamir, muzâfun ileyh.", key="makhraj-harf", pos="noun")
R("14:s2:10", "mudafIlayh", "jarr")
L("14:s2:12", *QSAR, key="hum", pos="pron")
L("14:s3:3", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَصِلَتُهُ جُمْلَةُ «مَرَّ».",
  "The lam is the preposition of cause; «مَا» is a relative noun, built on sukun, in the place of jarr; its sila is the clause «مَرَّ».",
  "Lâm ta'lîl için harf-i cerdir; «مَا» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr; sılası «مَرَّ» cümlesidir.", key="ma-mawsula", pos="pron")
L("14:s3:6", *QFI, key="daraba", pos="verb")
L("14:s5:3", *QFI, key="antuma", pos="pron")
L("14:s5:4", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَصِلَتُهُ جُمْلَةُ «ذُكِرَ».",
  "The lam is the preposition of cause; «مَا» is a relative noun, built on sukun, in the place of jarr; its sila is the clause «ذُكِرَ».",
  "Lâm ta'lîl için harf-i cerdir; «مَا» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr; sılası «ذُكِرَ» cümlesidir.", key="ma-mawsula", pos="pron")
L("14:s5:7", *QFI, key="daraba", pos="verb")
L("14:s6:4", *QFI, key="daraba", pos="verb")
L("14:s6:8", *QFI, key="antuma", pos="pron")
L("14:s7:2", *QFI, key="antuma", pos="pron")
L("14:s7:6", *QFI, key="pron-3d", pos="pron")
L("14:s8:2", *QFI, key="pron-3d", pos="pron")
L("14:s8:6", *QFI, key="hum", pos="pron")
L("14:s9:2", *QFI, key="hum", pos="pron")
R("14:s9:4", "mudafIlayh", "jarr")
L("14:s9:5", "اسْمُ إِشَارَةٍ لِلْمَكَانِ الْقَرِيبِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ ظَرْفُ مَكَانٍ، وَ«هَا» قَبْلَهُ لِلتَّنْبِيهِ.",
  "A demonstrative of near place («here»), built on sukun, in the place of nasb as an adverb of place; the «هَا» before it calls attention.",
  "Yakın mekân için ism-i işâret («burada»), sükûn üzere mebnî, mahallen mansûb mekân zarfı; başındaki «هَا» tenbih içindir.")
R("14:s10:2", "naib", "raf"); L("14:s10:2", "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The deputy doer (na'ib al-fa'il), in raf'; the sign is the damma; annexed (mudaf).", "Nâib-i fâil, merfû; alâmeti damme ile; muzâf.")
L("14:s10:3", *QUOTE, key="huwa", pos="pron")
K("14:s10:8", "salih-fit", pos="noun")
# ================================================================ part six (pp. 49–55)
NAIBM = ("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The deputy doer (na'ib al-fa'il), in raf'; the sign is the damma; annexed (mudaf).", "Nâib-i fâil, merfû; alâmeti damme ile; muzâf.")
QMATF = QUO("مَعْطُوفٌ عَلَى مَا قَبْلَهُ فِي مَحَلِّ جَرٍّ", "joined to the word before it, in the place of jarr", "öncekine ma'tûf, mahallen mecrûr")
QRATF = ("لَفْظٌ مَحْكِيٌّ بِالرَّفْعِ كَمَا ضُبِطَ فِي الْأَصْلِ، مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "The word is quoted in raf', as the print vowels it; joined to the one before it.", "Kelime, baskıda harekelendiği gibi ref' ile hikâye edilmiştir; öncekine ma'tûftur.")
KAFM = ("الْكَافُ حَرْفُ جَرٍّ، وَمَجْرُورٌ بِهِ بِالْكَسْرَةِ، مُضَافٌ.", "The kaf is a preposition; in jarr after it; the sign is the kasra; annexed (mudaf).", "Kâf harf-i cerdir; onunla mecrûr; alâmeti kesre ile; muzâf.")
def ISMK(v): return ("اسْمُ «" + v + "» مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of «" + v + "», in raf'; the sign is the damma.", "«" + v + "»nin ismi, merfû; alâmeti damme ile.")
def ISMKM(v): return ("اسْمُ «" + v + "» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of «" + v + "», in raf'; the sign is the damma; annexed (mudaf).", "«" + v + "»nin ismi, merfû; alâmeti damme ile; muzâf.")
def KHK(v): return ("خَبَرُ «" + v + "» مَنْصُوبٌ بِالْفَتْحَةِ.", "The khabar of «" + v + "», in nasb; the sign is the fatha.", "«" + v + "»nin haberi, mansûb; alâmeti fetha ile.")
def BZ(noun, v): return ("الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَ«" + noun + "» خَبَرُ «" + v + "» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.",
                         "The ba is an extra preposition strengthening the negation; «" + noun + "» is the khabar of «" + v + "» — in jarr in wording, in nasb in place.",
                         "Bâ, nefyi pekiştiren zâid harf-i cerdir; «" + noun + "» «" + v + "»nin haberidir — lafzen mecrûr, mahallen mansûb.")
def PMUB(pre, pron, bina_ar, bina_en, bina_tr):
    return (pre[0] + ("ضَمِيرٌ" if pre[0] else "ضَمِيرٌ") + " مُنْفَصِلٌ مَبْنِيٌّ عَلَى " + bina_ar + " فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
            pre[1] + ("a" if pre[1] else "A") + " detached pronoun, built on " + bina_en + ", in the place of raf' as the mubtada.",
            pre[2] + ("munfasıl" if pre[2] else "Munfasıl") + " zamir, " + bina_tr + " üzere mebnî, mahallen merfû mübtedâ.")
# the examples of the hidden pronoun: the verb, its hidden doer by name, and the place of the quoted word
HM = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "A past verb, built on fatha", "Mâzî fiil, feth üzere mebnî")
HMT = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ عَلَامَةُ التَّأْنِيثِ حَرْفٌ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ", "A past verb, built on fatha; the tāʾ is the mark of the feminine, a letter with no place in the i'rab", "Mâzî fiil, feth üzere mebnî; tâ te'nis alâmetidir, i'rabdan mahalli olmayan bir harftir")
HMD = ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ", "A present verb, in raf'; the sign is the visible damma", "Muzâri fiil, merfû; alâmeti zâhir damme")
HLAM = ("اللَّامُ لَامُ الْأَمْرِ، وَفِعْلٌ مُضَارِعٌ مَجْزُومٌ بِهَا، وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "The lam is the lam of command; a present verb in jazm after it; the sign is the sukun", "Lâm emir lâmıdır; onunla meczûm muzâri fiil; alâmeti sükûn")
HLA = ("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَا» النَّاهِيَةِ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "A present verb in jazm after the prohibiting «لَا»; the sign is the sukun", "Nehiy «لَا»sı ile meczûm muzâri fiil; alâmeti sükûn")
HAMR = ("فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ", "An imperative verb, built on sukun", "Emir fiili, sükûn üzere mebnî")
TQ = ("اللَّفْظُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "the word is quoted, in the place of jarr as the mudaf ilayh", "lafız hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir")
TA = ("اللَّفْظُ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ", "the word is quoted, joined to the one before it", "lafız hikâye edilmiştir, öncekine ma'tûftur")
TH = ("اللَّفْظُ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ بِحَذْفِ الْعَاطِفِ", "the word is quoted, joined to the one before it with the conjunction left out", "lafız hikâye edilmiştir, atıf harfi hazfedilerek öncekine ma'tûftur")
def SH(head, pron, wujub, tail=None):
    return (head[0] + "، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ " + ("وُجُوبًا" if wujub else "جَوَازًا") + " تَقْدِيرُهُ «" + pron + "» — وَهُوَ مَوْضِعُ الشَّاهِدِ" + (" — وَ" + tail[0] if tail else "") + ".",
            head[1] + "; its doer is a hidden pronoun «" + pron + "», hidden " + ("by necessity" if wujub else "by choice") + " — the point of the example" + ("; " + tail[1] if tail else "") + ".",
            head[2] + "; fâili " + ("vücûben" if wujub else "cevâzen") + " müstetir «" + pron + "» zamiridir — misâlin şâhidi budur" + ("; " + tail[2] if tail else "") + ".")
def LANAHY(clause):
    return ("«لَا» النَّاهِيَةُ: حَرْفُ نَهْيٍ وَجَزْمٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجُمْلَةُ «" + clause + "» مَحْكِيَّةٌ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا.",
            "The prohibiting «لَا»: a letter of prohibition and jazm, built on sukun; the clause «" + clause + "» is quoted, joined to what is before it.",
            "Nehiy «لَا»sı: nehiy ve cezm harfi, sükûn üzere mebnî; «" + clause + "» cümlesi hikâye edilmiştir, öncekine ma'tûftur.")
def SHV(where, head, pron, wujub, tail=None): L(where, *SH(head, pron, wujub, tail), key="daraba", pos="verb")
def YAQ(clause, m_ar, m_en, m_tr):
    return ("حَرْفُ نِدَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجُمْلَةُ «" + clause + "» مَحْكِيَّةٌ " + m_ar + ".",
            "A vocative particle, built on sukun; the clause «" + clause + "» is quoted, " + m_en + ".",
            "Nidâ harfi, sükûn üzere mebnî; «" + clause + "» cümlesi hikâye edilmiştir, " + m_tr + ".")
YFI = ("فِي مَحَلِّ جَرٍّ بِـ«فِي»", "in the place of jarr after «فِي»", "«فِي» ile mahallen mecrûr")
YQIL = ("عَلَى تَقْدِيرِ «فَيُقَالُ» — وَهِيَ مَا صَارَ إِلَيْهِ الْمِثَالُ بَعْدَ قَلْبِ الْيَاءِ أَلِفًا", "with «فَيُقَالُ» (so one says) understood — what the example becomes once the yāʾ is made an alif", "takdiri «فَيُقَالُ» (denir ki) — yâ elife çevrildikten sonra misâlin aldığı şekil")
L("14:s2:3", "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "An adjective (na't), in raf'; the sign is a damma estimated on the alif.", "Sıfat (na't), merfû; alâmeti elif üzerinde mukadder damme.")
# ---- chapter 15
R("15:s1:1", "naib", "raf"); L("15:s1:1", *NAIBM)
L("15:s1:2", *QUOTE, key="huwa", pos="pron")
R("15:s1:7", "nat", "jarr")
L("15:s1:7", "نَعْتٌ لِـ«شَيْءٍ» مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "An adjective (na't) of «شَيْءٍ», in jarr; the sign is the fatha in place of the kasra, for it is a diptote.", "«شَيْءٍ»in sıfatı (na't), mecrûr; alâmeti kesre yerine fetha ile — gayr-i munsarıftır.")
R("15:s2:2", "hal", "nasb")
L("15:s2:5", *NAHW)
L("15:s2:6", "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَضَمُّهَا مَوْضِعُ الشَّاهِدِ — وَاللَّفْظُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "The lam is a preposition and the hāʾ an attached pronoun, built on damma, in the place of jarr — its damma is the point of the example; the word is quoted, in the place of jarr as the mudaf ilayh.",
  "Lâm harf-i cer, hâ bitişik zamir, damm üzere mebnî, mahallen mecrûr — dammesi misâlin şâhididir; lafız hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir.")
L("15:s3:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ يَعُودُ إِلَى الْهَاءِ.",
  "The waw conjoins; a present verb in the passive, in raf'; the sign is the visible damma; its deputy doer is a hidden pronoun «هِيَ» going back to the hāʾ.",
  "«ve» atıf harfi; muzâri fiil (meçhul), merfû; alâmeti zâhir damme; nâib-i fâili hâ harfine dönen müstetir «هِيَ» zamiridir.")
L("15:s3:2", "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهَا الِاسْمُ الْمَوْصُولُ «مَا» بَعْدَهَا.",
  "An incomplete past verb, one of kāna's sisters, built on fatha; its noun is the relative «مَا» after it.", "Nâkıs mâzî fiil, kâne'nin kardeşlerinden, feth üzere mebnî; ismi kendisinden sonraki ism-i mevsûl «مَا»dır.", key="kana", pos="verb")
L("15:s3:3", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ اسْمُ «كَانَ»، وَصِلَتُهُ الظَّرْفُ «قَبْلَهُ».",
  "A relative noun, built on sukun, in the place of raf' as the noun of «كَانَ»; its sila is the adverb «قَبْلَهُ».", "İsm-i mevsûl, sükûn üzere mebnî, mahallen merfû, «كَانَ»nin ismi; sılası «قَبْلَهُ» zarfıdır.")
L("15:s3:5", *KHK("كَانَ"))
R("15:s3:8", "nat", "nasb")
L("15:s3:17", *NAHW)
L("15:s3:18", "«فِي» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجَارُّ وَالْمَجْرُورُ «فِي غُلَامِهِ» مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "«فِي» is a preposition, built on sukun; the phrase «فِي غُلَامِهِ» is quoted, in the place of jarr as the mudaf ilayh.", "«فِي» harf-i cer, sükûn üzere mebnî; «فِي غُلَامِهِ» câr-mecrûru hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir.")
L("15:s3:19", "مَجْرُورٌ بِـ«فِي» بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — كُسِرَتْ لِانْكِسَارِ مَا قَبْلَهَا، وَهُوَ مَوْضِعُ الشَّاهِدِ.",
  "In jarr after «فِي»; the sign is the kasra; annexed, and the hāʾ is an attached pronoun, built on kasra, the mudaf ilayh — it takes the kasra because the letter before it bears one: the point of the example.",
  "«فِي» ile mecrûr; alâmeti kesre ile; muzâftır, hâ bitişik zamir, kesre üzere mebnî, muzâfun ileyh — önceki harf meksûr olduğu için kesrelenmiştir; misâlin şâhidi budur.")
L("15:s3:21", "«فِي» حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ — كُسِرَتْ لِسُكُونِ الْيَاءِ قَبْلَهَا — وَاللَّفْظُ مَحْكِيٌّ مَعْطُوفٌ عَلَى مَا قَبْلَهُ.",
  "«فِي» is a preposition and the hāʾ an attached pronoun, built on kasra, in the place of jarr — it takes the kasra because a quiescent yāʾ stands before it; the word is quoted, joined to the one before it.",
  "«فِي» harf-i cer, hâ bitişik zamir, kesre üzere mebnî, mahallen mecrûr — önünde sâkin yâ bulunduğu için kesrelenmiştir; lafız hikâye edilmiştir, öncekine ma'tûftur.")
R("15:s4:1", "naib", "raf"); L("15:s4:1", *NAIBM)
L("15:s4:2", *QUOTE, key="hiya", pos="pron")
R("15:s4:3", "maful2", "nasb")
L("15:s4:7", *YAQ("يَا غُلَامِيَ", *YFI))
L("15:s4:8", "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "A vocative that is annexed (munada mudaf), in nasb; the sign is a fatha estimated on the letter before the speaker's yāʾ, kept from showing by the kasra that suits the yāʾ; the yāʾ is an attached pronoun, built on fatha, the mudaf ilayh.",
  "Muzâf münâdâ, mansûb; alâmeti mütekellim yâsından önceki harf üzerinde mukadder fethadır, yâya uygun kesre onun zuhûruna engel olmuştur; yâ bitişik zamir, feth üzere mebnî, muzâfun ileyh.", key="ghulam", pos="noun")
L("15:s4:9", *YAQ("يَا غُلَامَا", *YQIL))
L("15:s4:10", "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ، وَالْأَلِفُ مُنْقَلِبَةٌ عَنْ يَاءِ الْمُتَكَلِّمِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ مَوْضِعُ الشَّاهِدِ.",
  "A vocative that is annexed, in nasb; the sign is the visible fatha; the alif is the speaker's yāʾ turned into an alif, in the place of jarr as the mudaf ilayh — the point of the example.",
  "Muzâf münâdâ, mansûb; alâmeti zâhir fetha; elif, mütekellim yâsından çevrilmiştir, mahallen mecrûr muzâfun ileyhtir — misâlin şâhidi budur.", key="ghulam", pos="noun")
L("15:s4:12", *YAQ("يَا بَادِيَةُ", *YFI))
R("15:s4:13", "mabni", "keep")
L("15:s4:13", "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — نَكِرَةٌ مَقْصُودَةٌ.", "A vocative built on damma, in the place of nasb — an indefinite noun that is meant (nakira maqsuda).", "Damm üzere mebnî münâdâ, mahallen mansûb — nekre-i maksûde.", key="badiya", pos="noun")
L("15:s4:14", *YAQ("يَا بَادَاةُ", *YQIL))
R("15:s4:15", "mabni", "keep")
L("15:s4:15", "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَالْأَلِفُ فِيهِ مُنْقَلِبَةٌ عَنْ يَاءِ «بَادِيَةُ» — وَهُوَ مَوْضِعُ الشَّاهِدِ.",
  "A vocative built on damma, in the place of nasb; its alif is the yāʾ of «بَادِيَةُ» turned into an alif — the point of the example.", "Damm üzere mebnî münâdâ, mahallen mansûb; içindeki elif «بَادِيَةُ»nin yâsından çevrilmiştir — misâlin şâhidi budur.", key="badiya", pos="noun")
R("15:s5:2", "maful2", "nasb")
L("15:s6:1", *NAIBM)
L("15:s6:2", *QUOTE, key="hunna", pos="pron")
L("15:s6:3", *F["14:s3:3"]["irab"].values(), key="ma-mawsula", pos="pron")
L("15:s6:6", *QFI, key="daraba", pos="verb")
# ---- chapter 16
for _s, _j in (("s1", "لِلْمَنْصُوبِ"), ("s6", "لِلْمَنْصُوبِ"), ("s7", "لِلْمَجْرُورِ")):
    R("16:%s:0" % _s, "mubtada", "raf")
    L("16:%s:0" % _s, *ITHNA(*WAW, "مُبْتَدَأٌ مَرْفُوعٌ", "the mubtada, in raf'", "mübtedâ, merfû", tail_ar="، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ «" + _j + "»", tail_en="; its khabar is the jarr phrase «" + _j + "»", tail_tr="; haberi «" + _j + "» câr-mecrûrudur"))
    R("16:%s:1" % _s, "mabni", "keep"); L("16:%s:1" % _s, *ASHARI)
    R("16:%s:4" % _s, "khabar", "raf"); L("16:%s:4" % _s, *NAHW)
def OBJQ(obj_ar, obj_en, obj_tr, tail):
    return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ»، وَ" + obj_ar + " فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَهُوَ مَوْضِعُ الشَّاهِدِ — وَ" + tail[0] + ".",
            "A past verb, built on fatha; its doer is a hidden pronoun «هُوَ»; " + obj_en + ", in the place of nasb as the object — the point of the example; " + tail[1] + ".",
            "Mâzî fiil, feth üzere mebnî; fâili müstetir «هُوَ» zamiri; " + obj_tr + ", mahallen mansûb mef'ûlün bih — misâlin şâhidi budur; " + tail[2] + ".")
TILA = ("اللَّفْظُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِـ«إِلَى»", "the word is quoted, in the place of jarr after «إِلَى»", "lafız hikâye edilmiştir, «إِلَى» ile mahallen mecrûrdur")
L("16:s1:5", *OBJQ("الْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ", "the hāʾ is an attached pronoun, built on damma", "hâ bitişik zamir, damm üzere mebnî", TQ), key="daraba", pos="verb")
L("16:s1:7", *OBJQ("«نَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ", "«نَا» is an attached pronoun, built on sukun", "«نَا» bitişik zamir, sükûn üzere mebnî", TILA), key="daraba", pos="verb")
L("16:s2:4", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَحُرِّكَتِ الْيَاءُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَهُوَ مُضَافٌ.",
  "The mudaf ilayh, in jarr; the sign is the yāʾ, for it is a dual whose nūn is dropped for annexation; the yāʾ takes a kasra because two quiescent letters meet; itself annexed (mudaf).",
  "Muzâfun ileyh, mecrûr; alâmeti yâ ile — tesniyedir, izâfet sebebiyle nûnu düşmüştür; iki sâkin karşılaştığı için yâ kesre ile harekelenmiştir; kendisi de muzâftır.")
K("16:s2:6", "maful-object", pos="noun")
L("16:s2:8", *MITHLFI)
def TAQ(obj_ar, obj_en, obj_tr, note, tail):
    return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَ" + obj_ar + " — " + note[0] + " — وَ" + tail[0] + ".",
            "A past verb, built on sukun because the tāʾ of the doer is joined to it; the tāʾ is an attached pronoun, the doer; " + obj_en + " — " + note[1] + "; " + tail[1] + ".",
            "Mâzî fiil; fâil tâsına bitiştiği için sükûn üzere mebnî; tâ bitişik zamir, fâil; " + obj_tr + " — " + note[2] + "; " + tail[2] + ".")
NMUMT = ("وَهُمَا لِشَخْصٍ وَاحِدٍ، وَهُوَ مِثَالُ الْمُمْتَنِعِ", "both for one person: the author's example of what cannot be said", "ikisi de aynı şahıs içindir; söylenemeyecek olanın misâli")
NQULUB = ("وَجَازَ اجْتِمَاعُهُمَا لِشَخْصٍ وَاحِدٍ لِأَنَّ الْفِعْلَ مِنْ أَفْعَالِ الْقُلُوبِ", "both may stand for one person here, for the verb is a verb of the heart", "fiil kalb fiillerinden olduğu için ikisinin aynı şahıs için bir araya gelmesi câizdir")
OKAF = ("الْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "the kāf is an attached pronoun, the object", "kâf bitişik zamir, mef'ûlün bih")
OYA = ("النُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "the nūn is the nūn of protection and the yāʾ an attached pronoun, the object", "nûn vikâye nûnudur; yâ bitişik zamir, mef'ûlün bih")
OKAF1 = ("الْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ", "the kāf is an attached pronoun, the first object", "kâf bitişik zamir, birinci mef'ûl")
OYA1 = ("النُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ", "the nūn is the nūn of protection and the yāʾ an attached pronoun, the first object", "nûn vikâye nûnudur; yâ bitişik zamir, birinci mef'ûl")
TJQ = ("الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "the clause is quoted, in the place of jarr as the mudaf ilayh", "cümle hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir")
TJA = ("الْجُمْلَةُ مَحْكِيَّةٌ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is quoted, joined to the one before it", "cümle hikâye edilmiştir, öncekine ma'tûftur")
L("16:s2:9", *TAQ(*OKAF, NMUMT, TQ), key="daraba", pos="verb")
L("16:s2:11", *TAQ(*OYA, NMUMT, TA), key="daraba", pos="verb")
L("16:s2:15", *ISMK("يَصِيرَ")); L("16:s2:16", *KHK("يَصِيرَ"))
K("16:s3:2", "afal", pos="noun"); K("16:s3:3", "qalb", pos="noun")
L("16:s3:4", *NAHW)
L("16:s3:5", *TAQ(*OKAF1, NQULUB, TJQ), key="alima", pos="verb")
R("16:s3:6", "maful2", "nasb")
L("16:s3:8", *TAQ(*OYA1, NQULUB, TJA), key="alima", pos="verb")
R("16:s3:9", "maful2", "nasb")
K("16:s4:1", "maful-object", pos="noun")
L("16:s4:4", *BZ("مَفْعُولٍ", "لَيْسَ"))
def TAF(clause, m_ar, m_en, m_tr):
    return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْجُمْلَةُ «" + clause + "» مَحْكِيَّةٌ " + m_ar + ".",
            "A past verb, built on sukun because the tāʾ of the doer is joined to it; the tāʾ is an attached pronoun, the doer; the clause «" + clause + "» is quoted, " + m_en + ".",
            "Mâzî fiil; fâil tâsına bitiştiği için sükûn üzere mebnî; tâ bitişik zamir, fâil; «" + clause + "» cümlesi hikâye edilmiştir, " + m_tr + ".")
L("16:s5:4", *TAF("عَلِمْتُ فَضْلِي", "فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِـ«قِيلَ»", "in the place of raf' as the deputy doer of «قِيلَ»", "«قِيلَ»nin nâib-i fâili olarak mahallen merfûdur"), key="alima", pos="verb")
L("16:s5:7", *TAF("عَلِمْتَ فَضْلَكَ", "مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "joined to the one before it", "öncekine ma'tûftur"), key="alima", pos="verb")
def IYYA(clause, m_ar, m_en, m_tr):
    return ("ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَهُوَ مَوْضِعُ الشَّاهِدِ — وَالْجُمْلَةُ «" + clause + "» مَحْكِيَّةٌ " + m_ar + ".",
            "A detached pronoun of nasb, built, in the place of nasb as the object, set before its verb — the point of the example; the clause «" + clause + "» is quoted, " + m_en + ".",
            "Munfasıl nasb zamiri, mebnî, mahallen mansûb, öne geçmiş mef'ûlün bih — misâlin şâhidi budur; «" + clause + "» cümlesi hikâye edilmiştir, " + m_tr + ".")
L("16:s6:5", *IYYA("إِيَّاهُ ضَرَبَ", "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "in the place of jarr as the mudaf ilayh", "mahallen mecrûr muzâfun ileyhtir"))
L("16:s6:8", *IYYA("إِيَّانَا ضَرَبْنَا", "فِي مَحَلِّ جَرٍّ بِـ«إِلَى»", "in the place of jarr after «إِلَى»", "«إِلَى» ile mahallen mecrûrdur"))
L("16:s6:9", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا» الْفَاعِلِينَ، وَ«نَا» ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
  "A past verb, built on sukun because the «نَا» of the doers is joined to it; «نَا» is its doer.", "Mâzî fiil; fâil «نَا»sına bitiştiği için sükûn üzere mebnî; «نَا» fâildir.", key="daraba", pos="verb", enc="")
def MJQ(pron_ar, pron_en, pron_tr, m_ar, m_en, m_tr):
    return ("لَفْظٌ مَحْكِيٌّ بِالرَّفْعِ كَمَا ضُبِطَ فِي الْأَصْلِ، " + m_ar + "، وَ" + pron_ar + " فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ مَوْضِعُ الشَّاهِدِ.",
            "The word is quoted in raf', as the print vowels it; " + m_en + "; " + pron_en + ", in the place of jarr as the mudaf ilayh — the point of the example.",
            "Kelime, baskıda harekelendiği gibi ref' ile hikâye edilmiştir; " + m_tr + "; " + pron_tr + ", mahallen mecrûr muzâfun ileyh — misâlin şâhidi budur.")
L("16:s7:5", *MJQ("الْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ", "the hāʾ is an attached pronoun, built on damma", "hâ bitişik zamir, damm üzere mebnî", "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "in the place of jarr as the mudaf ilayh", "mahallen mecrûr muzâfun ileyh"))
L("16:s7:7", *MJQ("«نَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ", "«نَا» is an attached pronoun, built on sukun", "«نَا» bitişik zamir, sükûn üzere mebnî", "فِي مَحَلِّ جَرٍّ بِـ«إِلَى»", "in the place of jarr after «إِلَى»", "«إِلَى» ile mahallen mecrûr"))
L("16:s8:2", *QUOTE)
L("16:s8:4", *QKH)
R("16:s8:7", "maful2", "nasb")
L("16:s8:10", "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«مَا» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَصِلَتُهُ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.",
  "The kaf is a preposition of likeness; «مَا» is a relative noun, built on sukun, in the place of jarr; its sila is the jarr phrase after it.", "Kâf teşbih için harf-i cerdir; «مَا» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr; sılası sonraki câr-mecrûrdur.")
L("16:s8:12", *QFI)
L("16:s8:14", *QKH)
# ---- chapter 17
L("17:s1:6", "«فِي» حَرْفُ جَرٍّ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجَارُّ وَالْمَجْرُورُ بَدَلٌ مِنْ «فِي خَمْسَةِ مَوَاضِعَ» — بَدَلُ مُفَصَّلٍ مِنْ مُجْمَلٍ.",
  "«فِي» is a preposition, built on sukun; the jarr phrase is a badal of «فِي خَمْسَةِ مَوَاضِعَ» — the detail after the sum.", "«فِي» harf-i cer, sükûn üzere mebnî; câr-mecrûr «فِي خَمْسَةِ مَوَاضِعَ»den bedeldir — mücmelden sonra mufassal.")
L("17:s1:8", *NAHW); SHV("17:s1:9", HM, "هُوَ", False, TQ); SHV("17:s1:10", HMD, "هُوَ", False, TH); SHV("17:s1:12", HLAM, "هُوَ", False, TA)
L("17:s1:14", *LANAHY("لَا يَضْرِبْ"), key="la-nahiya", pos="part"); SHV("17:s1:15", HLA, "هُوَ", False)
L("17:s2:2", *NAHW); SHV("17:s2:3", HMT, "هِيَ", False, TQ); SHV("17:s2:5", HMD, "هِيَ", False, TA); SHV("17:s2:7", HLAM, "هِيَ", False, TA)
L("17:s2:9", *LANAHY("لَا تَضْرِبْ"), key="la-nahiya", pos="part"); SHV("17:s2:10", HLA, "هِيَ", False)
L("17:s3:2", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«الْمُخَاطَبِ»، وَصِلَتُهُ الْجَارُّ وَالْمَجْرُورُ «فِي غَيْرِ الْمَاضِي».",
  "A relative noun, built on sukun, in the place of jarr as an adjective of «الْمُخَاطَبِ»; its sila is the jarr phrase «فِي غَيْرِ الْمَاضِي».", "İsm-i mevsûl, sükûn üzere mebnî, mahallen mecrûr, «الْمُخَاطَبِ»in sıfatı; sılası «فِي غَيْرِ الْمَاضِي» câr-mecrûrudur.")
L("17:s3:6", *NAHW); SHV("17:s3:7", HMD, "أَنْتَ", True, TQ); SHV("17:s3:9", HAMR, "أَنْتَ", True, TA)
L("17:s3:11", *LANAHY("لَا تَضْرِبْ"), key="la-nahiya", pos="part"); SHV("17:s3:12", HLA, "أَنْتَ", True)
L("17:s4:2", *QFI, key="daraba", pos="verb")
KHM = ('خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.', "The khabar (predicate), in raf'; the sign is the damma; annexed (mudaf).", 'Haber, merfû; alâmeti damme ile; muzâf.')
R("17:s4:3", "khabar", "raf"); L("17:s4:3", *KHM); R("17:s4:5", "mubtada", "raf")
L("17:s5:0", "الْوَاوُ عَاطِفَةٌ، وَظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The waw conjoins; an adverb (zarf), in nasb; the sign is the fatha; annexed (mudaf).", "«ve» atıf harfi; zarf, mansûb; alâmeti fetha ile; muzâf.")
R("17:s5:1", "mabni", "keep")
L("17:s5:1", "عَلَمٌ مَخْتُومٌ بِـ«وَيْهِ» مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A proper name ending in «وَيْهِ», built on kasra, in the place of jarr as the mudaf ilayh.", "«وَيْهِ» ile biten özel isim, kesre üzere mebnî, mahallen mecrûr muzâfun ileyh.", key="sibawayh", pos="propn")
L("17:s5:3", *PMUB(("", "", ""), "هُوَ", "الْفَتْحِ", "fatha", "feth"))
R("17:s5:5", "nat", "raf")
L("17:s5:7", *KAFM)
L("17:s5:8", *QUOTE, key="daraba", pos="verb")
L("17:s6:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
  "The waw conjoins; a past verb in the passive, built on fatha; the tāʾ marks the feminine and takes a kasra because two quiescent letters meet.", "«ve» atıf harfi; mâzî fiil (meçhul), feth üzere mebnî; tâ te'nis içindir, iki sâkin karşılaştığı için kesre ile harekelenmiştir.")
R("17:s6:1", "naib", "raf")
R("17:s6:4", "mabni", "keep")
L("17:s6:4", "اسْمُ إِشَارَةٍ لِلْمُفْرَدَةِ الْمُؤَنَّثَةِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْيَاءُ فِيهِ مَوْضِعُ الشَّاهِدِ — وَالْجُمْلَةُ «هٰذِي أَمَةُ اللهِ» مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ بِـ«فِي».",
  "A demonstrative for the feminine singular, built on sukun, in the place of raf' as the mubtada — its yāʾ is the point of the example; the clause «هٰذِي أَمَةُ اللهِ» is quoted, in the place of jarr after «فِي».",
  "Müfred müennes için ism-i işâret, sükûn üzere mebnî, mahallen merfû mübtedâ — içindeki yâ misâlin şâhididir; «هٰذِي أَمَةُ اللهِ» cümlesi hikâye edilmiştir, «فِي» ile mahallen mecrûrdur.", key="hadhihi", pos="pron")
K("17:s6:5", "ama-handmaid", pos="noun"); R("17:s6:5", "khabar", "raf"); F["17:s6:5"]["key"] = "ama-handmaid"; F["17:s6:5"]["pos"] = "noun"; L("17:s6:5", *KHM)
L("17:s7:1", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِـ«لَمْ»، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ أَلِفُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
  "A present verb in the passive, in jazm after «لَمْ»; the sign is the sukun; its alif is dropped because two quiescent letters meet.", "Muzâri fiil (meçhul), «لَمْ» ile meczûm; alâmeti sükûn; iki sâkin karşılaştığı için elifi düşmüştür.")
L("17:s7:3", *QFI, key="daraba", pos="verb")
L("17:s7:5", "مَجْرُورٌ بِـ«مِنْ» بِالْكَسْرَةِ، مُضَافٌ.", "In jarr after «مِنْ»; the sign is the kasra; annexed (mudaf).", "«مِنْ» ile mecrûr; alâmeti kesre ile; muzâf.")
L("17:s7:6", *QUOTE, key="anti", pos="pron")
R("17:s7:7", "naib", "raf")
R("17:s7:13", "mudafIlayh", "jarr"); R("17:s7:17", "mudafIlayh", "jarr")
L("17:s9:1", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِـ«لَمْ»، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «بِحَرَكَةِ».",
  "A present verb in the passive, in jazm after «لَمْ»; the sign is the sukun; its deputy doer is the jarr phrase «بِحَرَكَةِ».", "Muzâri fiil (meçhul), «لَمْ» ile meczûm; alâmeti sükûn; nâib-i fâili «بِحَرَكَةِ» câr-mecrûrudur.")
L("17:s9:2", "الْبَاءُ حَرْفُ جَرٍّ، وَمَجْرُورٌ بِهِ بِالْكَسْرَةِ، مُضَافٌ.", "The ba is a preposition; in jarr after it; the sign is the kasra; annexed (mudaf).", "Bâ harf-i cerdir; onunla mecrûr; alâmeti kesre ile; muzâf.")
L("17:s9:3", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَصِلَتُهُ الظَّرْفُ «قَبْلَ النُّونِ».",
  "A relative noun, built on sukun, in the place of jarr as the mudaf ilayh; its sila is the adverb «قَبْلَ النُّونِ».", "İsm-i mevsûl, sükûn üzere mebnî, mahallen mecrûr muzâfun ileyh; sılası «قَبْلَ النُّونِ» zarfıdır.")
R("17:s10:7", "nat", "jarr")
L("17:s11:3", *NAHW); SHV("17:s11:4", HMD, "أَنَا", True, TQ); SHV("17:s11:6", HMD, "نَحْنُ", True, TA)
L("17:s11:9", *NAHW)
L("17:s11:10", "لَفْظٌ مَحْكِيٌّ بِالرَّفْعِ كَمَا ضُبِطَ فِي الْأَصْلِ، فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَفِيهِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَهُوَ مَوْضِعُ الشَّاهِدِ.",
  "The word is quoted in raf', as the print vowels it; in the place of jarr as the mudaf ilayh; a hidden pronoun «هُوَ» lies in it — the point of the example.",
  "Kelime, baskıda harekelendiği gibi ref' ile hikâye edilmiştir; mahallen mecrûr muzâfun ileyh; içinde müstetir «هُوَ» zamiri vardır — misâlin şâhidi budur.")
L("17:s11:12", "لَفْظٌ مَحْكِيٌّ بِالرَّفْعِ مَعْطُوفٌ عَلَى مَا قَبْلَهُ، وَفِيهِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُمَا»، وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ لَا ضَمِيرٌ.",
  "The word is quoted in raf', joined to the one before it; a hidden pronoun «هُمَا» lies in it; the alif is the mark of the dual, not a pronoun.", "Kelime ref' ile hikâye edilmiştir, öncekine ma'tûftur; içinde müstetir «هُمَا» zamiri vardır; elif zamir değil, tesniye alâmetidir.")
R("17:s13:11", "mubtada", "raf")
AWLA = ("خَبَرُ الْمُبْتَدَإِ «إِعْطَاءُ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمُ تَفْضِيلٍ.", "The khabar of the mubtada «إِعْطَاءُ», in raf'; the sign is a damma estimated on the alif — an elative (ism tafdil).", "«إِعْطَاءُ» mübtedâsının haberi, merfû; alâmeti elif üzerinde mukadder damme — ism-i tafdîl.")
L("17:s13:15", *AWLA, key="awla-fitter", pos="noun"); L("17:s15:7", *AWLA, key="awla-fitter", pos="noun")
L("17:s14:3", "اسْمٌ مَوْصُولٌ لِلْمُثَنَّى الْمُذَكَّرِ، نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، وَصِلَتُهُ الْجَارُّ وَالْمَجْرُورُ «فِي الْمَاضِي».",
  "A relative noun for the masculine dual, an adjective in jarr; the sign is the yāʾ, for it follows the dual; its sila is the jarr phrase «فِي الْمَاضِي».", "Müzekker tesniye için ism-i mevsûl, sıfat, mecrûr; alâmeti yâ ile — tesniyeye mülhaktır; sılası «فِي الْمَاضِي» câr-mecrûrudur.", key="alladhani", pos="pron")
R("17:s14:11", "atf", "raf")
L("17:s14:11", "مَعْطُوفٌ عَلَى خَبَرِ «أَنَّ» مَرْفُوعٌ بِالضَّمَّةِ — عَطْفُ مَعْمُولَيْنِ عَلَى مَعْمُولَيْ عَامِلٍ وَاحِدٍ.", "Joined to the khabar of «أَنَّ», in raf'; the sign is the damma — two governed words joined to the two governed words of one governor.", "«أَنَّ»nin haberine ma'tûf, merfû; alâmeti damme ile — bir âmilin iki ma'mûlüne iki ma'mûlün atfı.")
L("17:s17:3", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ بِـ«فِي».", "A demonstrative, built on kasra, in the place of jarr after «فِي».", "İsm-i işâret, kesre üzere mebnî, «فِي» ile mahallen mecrûr.")
L("17:s18:0", *PMUB(WAW, "هُوَ", "الْفَتْحِ", "fatha", "feth"))
for _i in (4, 8, 12, 16, 20, 24):
    L("17:s18:%d" % _i, *MITHLFI); L("17:s18:%d" % (_i + 1), *QUOTE, key="daraba", pos="verb")
L("17:s19:0", *PMUB(WAW, "هِيَ", "الْفَتْحِ", "fatha", "feth"))
L("17:s19:1", *LAYSAT, key="laysa", pos="verb")
L("17:s19:2", *BZ("أَسْمَاءٍ", "لَيْسَتْ"))
R("17:s20:0", "atf", "raf")
L("17:s20:0", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ عَلَى «عَدَمُ الْإِبْرَازِ» فِي الْجُمْلَةِ السَّابِقَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; joined to «عَدَمُ الْإِبْرَازِ» in the sentence before, in raf'; the sign is the damma.", "«ve» atıf harfi; önceki cümledeki «عَدَمُ الْإِبْرَازِ»a ma'tûf, merfû; alâmeti damme ile.")
L("17:s20:3", *QRAF); L("17:s20:5", *QRATF); L("17:s20:7", *QRATF)
L("17:s21:4", *ISMKM("يَكُونَ")); L("17:s21:5", *QUOTE, key="daraba", pos="verb")
R("17:s21:6", "kanaKhabar", "nasb"); L("17:s21:6", *KHK("يَكُونَ"))
L("17:s21:7", *KAFM); L("17:s21:8", *QUOTE, key="daraba", pos="verb", enc="")
L("17:s21:14", *NAHW)
L("17:s21:15", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ عَلَامَةُ التَّأْنِيثِ لَمْ تُحْذَفْ مَعَ الْفَاعِلِ الظَّاهِرِ — وَهُوَ مَوْضِعُ الشَّاهِدِ — وَالْجُمْلَةُ «ضَرَبَتْ هِنْدٌ» مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "A past verb, built on fatha; the tāʾ is the mark of the feminine, and it is not dropped though the doer is stated — the point of the example; the clause «ضَرَبَتْ هِنْدٌ» is quoted, in the place of jarr as the mudaf ilayh.",
  "Mâzî fiil, feth üzere mebnî; tâ te'nis alâmetidir, fâil açıkça zikredildiği hâlde düşmemiştir — misâlin şâhidi budur; «ضَرَبَتْ هِنْدٌ» cümlesi hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir.", key="daraba", pos="verb")
R("17:s22:4", "kanaIsm", "raf"); L("17:s22:4", *ISMKM("يَكُونَ"), key="alif-letter", pos="noun")
L("17:s22:5", *QRAF)
L("17:s22:6", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The waw conjoins; joined to the word before it, in raf'; the sign is the damma; annexed (mudaf).", "«ve» atıf harfi; öncekine ma'tûf, merfû; alâmeti damme ile; muzâf.")
L("17:s22:7", *QRAF)
R("17:s22:8", "kanaKhabar", "nasb"); L("17:s22:8", *KHK("يَكُونَ"))
L("17:s23:3", *KAFM)
L("17:s23:4", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَهُوَ مَوْضِعُ الشَّاهِدِ: لَا يَتَغَيَّرُ — وَاللَّفْظُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A present verb, in raf'; the sign is the nūn that stays; the alif is an attached pronoun, the doer — the point of the example: it never changes; the word is quoted, in the place of jarr as the mudaf ilayh.", "Muzâri fiil, merfû; alâmeti nûnun sübûtu; elif bitişik zamir, fâil — misâlin şâhidi budur: değişmez; lafız hikâye edilmiştir, mahallen mecrûr muzâfun ileyhtir.", key="daraba", pos="verb")
L("17:s24:3", *MITHLFI)
L("17:s24:4", *QUOTE, key="faala", pos="verb")
for _i in (6, 8, 10): L("17:s24:%d" % _i, *QMATF, key="faala", pos="verb")
L("17:s25:1", "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجُمْلَةُ «افْعَلْ زَيْدٌ» مَحْكِيَّةٌ فِي مَحَلِّ رَفْعٍ فَاعِلُ «قَبُحَ».", "An imperative verb, built on sukun; the clause «افْعَلْ زَيْدٌ» is quoted, in the place of raf' as the doer of «قَبُحَ».", "Emir fiili, sükûn üzere mebnî; «افْعَلْ زَيْدٌ» cümlesi hikâye edilmiştir, «قَبُحَ»nin fâili olarak mahallen merfûdur.", key="faala", pos="verb")
for _i in (4, 7, 10):
    L("17:s25:%d" % _i, "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْجُمْلَةُ مَحْكِيَّةٌ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا.", "A present verb, in raf'; the sign is the visible damma; the clause is quoted, joined to the one before it.", "Muzâri fiil, merfû; alâmeti zâhir damme; cümle hikâye edilmiştir, öncekine ma'tûftur.", key="faala", pos="verb")
for _i in (2, 5, 8):
    L("17:s25:%d" % _i, "فَاعِلٌ ظَاهِرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ مَوْضِعُ الْقُبْحِ: أُظْهِرَ الْفَاعِلُ حَيْثُ يَجِبُ اسْتِتَارُهُ.", "A stated doer, in raf'; the sign is the damma — this is where the ugliness lies: the doer is stated where it must stay hidden.", "Zâhir fâil, merfû; alâmeti damme ile — çirkinlik buradadır: gizlenmesi vâcip olan yerde fâil açığa çıkarılmıştır.")
L("17:s25:11", "فَاعِلٌ ظَاهِرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَهُوَ مَوْضِعُ الْقُبْحِ: أُظْهِرَ الْفَاعِلُ حَيْثُ يَجِبُ اسْتِتَارُهُ.", "A stated doer, in raf'; the sign is the waw, for it is a sound masculine plural — this is where the ugliness lies: the doer is stated where it must stay hidden.", "Zâhir fâil, merfû; alâmeti vâv ile — cem'-i müzekker sâlimdir; çirkinlik buradadır: gizlenmesi vâcip olan yerde fâil açığa çıkarılmıştır.")
# ================================================================ part seven (pp. 56–60)
TFEM = dict(tail_ar="، وَالتَّاءُ لِلتَّأْنِيثِ", tail_en="; the tāʾ marks the feminine", tail_tr="; tâ te'nis içindir")
TFEMH = dict(tail_ar="، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ يَعُودُ إِلَى حُرُوفِ «أَتَيْنَ»", tail_en="; the tāʾ marks the feminine; its deputy doer is a hidden pronoun «هِيَ» going back to the letters of «أَتَيْنَ»", tail_tr="; tâ te'nis içindir; nâib-i fâili «أَتَيْنَ» harflerine dönen müstetir «هِيَ» zamiridir")
QMATFR = QUO("مَعْطُوفٌ عَلَى مَا قَبْلَهُ فِي مَحَلِّ رَفْعٍ", "joined to the word before it, in the place of raf'", "öncekine ma'tûf, mahallen merfû")
FASL = ("ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — أَوْ مُبْتَدَأٌ ثَانٍ خَبَرُهُ «الَّذِي» وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.", "A pronoun of separation, with no place in the i'rab — or a second mubtada whose khabar is «الَّذِي», the clause being the khabar of the first.", "Fasıl zamiri, i'rabdan mahalli yoktur — yahut haberi «الَّذِي» olan ikinci mübtedâdır; cümle birincinin haberidir.")
def ALLADHI(sila_ar, sila_en, sila_tr):
    return ("اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ، وَصِلَتُهُ " + sila_ar + ".", "A relative noun, built on sukun, in the place of raf' as the khabar of the mubtada; its sila is " + sila_en + ".", "İsm-i mevsûl, sükûn üzere mebnî, mahallen merfû, mübtedânın haberi; sılası " + sila_tr + ".")
MUBTW = ("الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; the mubtada, in raf'; the sign is the damma.", "«ve» atıf harfi; mübtedâ, merfû; alâmeti damme ile.")
MUDRAF = ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.", "A present verb, in raf'; the sign is the visible damma.", "Muzâri fiil, merfû; alâmeti zâhir damme.")
def DIAL(m_ar, m_en, m_tr):
    return ("لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ — بِكَسْرِ حَرْفِ الْمُضَارَعَةِ عَلَى لُغَةٍ — " + m_ar + ".", "The word itself is quoted — with a kasra on the muḍāriʿ's letter, as one dialect says it — " + m_en + ".", "Kelimenin kendisi kastedilmiştir (hikâye) — bir lehçeye göre muzâraat harfi kesreli — " + m_tr + ".")
DMI = ("فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "in the place of jarr as the mudaf ilayh", "mahallen mecrûr muzâfun ileyh")
DAT = ("مَعْطُوفٌ عَلَى مَا قَبْلَهُ", "joined to the word before it", "öncekine ma'tûf")
# ---- chapter 18
L("18:s1:0", *PMUB(WAW, "هُوَ", "الْفَتْحِ", "fatha", "feth"), key="huwa", pos="pron")
R("18:s1:4", "mabni", "keep"); L("18:s1:4", *NUM1("أَرْبَعَةَ عَشَرَ", "fourteen", "On dört", "فِي مَحَلِّ جَرٍّ بِـ«عَلَى»", "sits in the place of jarr after «عَلَى»", "«عَلَى» ile mahallen mecrûrdur"), key="arbaa", pos="noun")
R("18:s1:5", "mabni", "keep"); L("18:s1:5", *ASHAR2, key="ashar", pos="noun")
R("18:s1:7", "khabar", "raf"); L("18:s1:7", *NAHW, key="nahw", pos="noun")
L("18:s1:8", *QUOTE, key="daraba", pos="verb")
R("18:s2:2", "naib", "raf"); L("18:s2:2", *YUQAL, key="mustaqbal", pos="noun")
R("18:s2:7", "jarr", "jarr")
L("18:s2:7", "مَجْرُورٌ بِـ«فِي» بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "In jarr after «فِي»; the sign is a kasra estimated on the alif; annexed, and the hāʾ is an attached pronoun, the mudaf ilayh.", "«فِي» ile mecrûr; alâmeti elif üzerinde mukadder kesre; muzâftır, hâ bitişik zamir, muzâfun ileyh.", key="mana", pos="noun")
R("18:s3:2", "naib", "raf"); L("18:s3:2", *YUQAL, key="mudari", pos="noun")
L("18:s4:5", *MITHLFI, key="mithl", pos="noun")
L("18:s4:6", *TAF("مَرَرْتُ بِرَجُلٍ يَضْرِبُ", "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "in the place of jarr as the mudaf ilayh", "mahallen mecrûr muzâfun ileyhtir"), key="marra", pos="verb", enc="")
L("18:s4:8", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ»، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«رَجُلٍ» — وَهُوَ مَوْضِعُ الشَّاهِدِ.",
  "A present verb, in raf'; the sign is the visible damma; its doer is a hidden pronoun «هُوَ»; the clause is an adjective of «رَجُلٍ», in the place of jarr — the point of the example.",
  "Muzâri fiil, merfû; alâmeti zâhir damme; fâili müstetir «هُوَ» zamiri; cümle «رَجُلٍ»in sıfatıdır, mahallen mecrûr — misâlin şâhidi budur.", key="daraba", pos="verb")
L("18:s4:9", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb of place, in nasb; the sign is the fatha; annexed (mudaf).", "Mekân zarfı, mansûb; alâmeti fetha ile; muzâf.", key="maqam", pos="noun")
R("18:s5:4", "khabar", "raf"); L("18:s5:4", *NAHW, key="nahw", pos="noun")
L("18:s5:8", "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لَامُ الِابْتِدَاءِ، وَفِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ»، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى خَبَرِ «إِنَّ» — وَدُخُولُ اللَّامِ عَلَى الْمُضَارِعِ مَوْضِعُ الشَّاهِدِ.",
  "The waw conjoins; the lam is the lam of beginning; a present verb, in raf', the sign the visible damma; its doer is a hidden pronoun «هُوَ»; the clause is joined to the khabar of «إِنَّ» — the lam entering upon the muḍāriʿ is the point of the example.",
  "«ve» atıf harfi; lâm ibtidâ lâmıdır; muzâri fiil, merfû, alâmeti zâhir damme; fâili müstetir «هُوَ» zamiri; cümle «إِنَّ»nin haberine ma'tûftur — lâmın muzâriye girmesi misâlin şâhididir.", key="qama", pos="verb")
L("18:s7:1", "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَ«مَا» زَائِدَةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» وَمَعْمُولَيْهَا فِي مَحَلِّ جَرٍّ بِالْكَافِ.",
  "The kaf is a preposition of likeness and «مَا» is extra; the masdar read out of «أَنَّ» and its two governed words is in the place of jarr after the kaf.", "Kâf teşbih için harf-i cerdir, «مَا» zâiddir; «أَنَّ» ile iki ma'mûlünden çıkan müevvel masdar kâf ile mahallen mecrûrdur.", key="kama", pos="part")
L("18:s7:9", *MUDRAF, key="ikhtassa", pos="verb")
L("18:s7:10", *QUO("فِي مَحَلِّ رَفْعٍ فَاعِلُ «يَخْتَصُّ»", "in the place of raf' as the doer of «يَخْتَصُّ»", "«يَخْتَصُّ»nün fâili olarak mahallen merfû"), key="daraba", pos="verb")
L("18:s7:11", "الْبَاءُ حَرْفُ جَرٍّ، وَ«سَوْفَ» لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ فِي مَحَلِّ جَرٍّ بِالْبَاءِ.", "The ba is a preposition; «سَوْفَ» is the word itself, quoted, in the place of jarr after the ba.", "Bâ harf-i cerdir; «سَوْفَ» kelimenin kendisidir (hikâye), bâ ile mahallen mecrûrdur.", key="sawfa", pos="part")
R("18:s8:0", "jarr", "jarr")
L("18:s8:0", "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَ«الْعَيْنِ» مَجْرُورٌ بِهِ بِالْكَسْرَةِ — يُرِيدُ لَفْظَ «الْعَيْنِ» الْمُشْتَرَكَ بَيْنَ مَعَانٍ.",
  "The waw conjoins; the ba is a preposition and «الْعَيْنِ» is in jarr after it; the sign is the kasra — he means the WORD «عَيْن», which is shared between several meanings.", "«ve» atıf harfi; bâ harf-i cerdir, «الْعَيْنِ» onunla mecrûr; alâmeti kesre ile — birkaç mânâ arasında müşterek olan «عَيْن» LAFZINI kasteder.", key="ayn", pos="noun")
# ---- chapter 19
L("19:s1:1", *CAP(PASS("", "", "", **TFEM)), key="zada", pos="verb")
R("19:s1:4", "naib", "raf"); L("19:s1:4", *NAIBM, key="harf", pos="noun")
L("19:s1:5", *QUOTE, key="atayna-huruf", pos="noun")
R("19:s1:8", "kanaKhabar", "nasb"); L("19:s1:8", *KHK("يَصِيرَ"), key="mustaqbal", pos="noun")
L("19:s1:14", "خَبَرُ «يَصِيرُ» مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.", "The khabar of «يَصِيرُ», in nasb; the sign is the fatha — an elative, a diptote.", "«يَصِيرُ»nün haberi, mansûb; alâmeti fetha ile — ism-i tafdîl, gayr-i munsarıf.", key="aqall", pos="noun")
L("19:s2:0", *PASS(*WAW, **TFEMH), key="zada", pos="verb")
L("19:s4:0", *PASS(*WAW, **TFEMH), key="zada", pos="verb")
R("19:s4:10", "atf", "nasb")
L("19:s4:10", "الْوَاوُ عَاطِفَةٌ، وَمَعْطُوفٌ عَلَى اسْمِ «أَنَّ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ بَعْدَهُ خَبَرُهُ.", "The waw conjoins; joined to the noun of «أَنَّ», in nasb; the sign is the fatha; annexed — the adverb after it is its khabar.", "«ve» atıf harfi; «أَنَّ»nin ismine ma'tûf, mansûb; alâmeti fetha ile; muzâf — sonraki zarf onun haberidir.", key="zaman", pos="noun")
L("19:s5:9", *PMUB(WAW, "هُوَ", "الْفَتْحِ", "fatha", "feth"), key="huwa", pos="pron")
L("19:s5:13", *FASL, key="huwa", pos="pron")
L("19:s5:14", *ALLADHI("جُمْلَةُ «يَبْتَدِئُ الْكَلَامُ مِنْهُ»", "the clause «يَبْتَدِئُ الْكَلَامُ مِنْهُ»", "«يَبْتَدِئُ الْكَلَامُ مِنْهُ» cümlesidir"), key="alladhi", pos="pron")
L("19:s6:3", "الْوَاوُ عَاطِفَةٌ، وَظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The waw conjoins; an adverb (zarf), in nasb; the sign is the fatha; annexed (mudaf).", "«ve» atıf harfi; zarf, mansûb; alâmeti fetha ile; muzâf.", key="bayna", pos="noun")
L("19:s6:4", *QUOTE, key="ana", pos="pron")
L("19:s7:4", "خَبَرُ «كَوْنِ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ — وَاسْمُهُ الضَّمِيرُ «هَا».", "The khabar of the masdar «كَوْن», in nasb; the sign is a fatha estimated on the alif; annexed — its noun is the pronoun «هَا».", "«كَوْن» masdarının haberi, mansûb; alâmeti elif üzerinde mukadder fetha; muzâf — ismi «هَا» zamiridir.", key="muntaha", pos="noun")
R("19:s7:6", "mubtada", "raf"); L("19:s7:6", *MUBTW, key="mukhatab", pos="noun")
L("19:s7:7", *FASL, key="huwa", pos="pron")
L("19:s7:8", *ALLADHI("جُمْلَةُ «يَنْتَهِي الْكَلَامُ بِهِ»", "the clause «يَنْتَهِي الْكَلَامُ بِهِ»", "«يَنْتَهِي الْكَلَامُ بِهِ» cümlesidir"), key="alladhi", pos="pron")
R("19:s8:3", "maful2", "nasb")
L("19:s8:9", *MITHLFI, key="mithl", pos="noun")
L("19:s8:10", "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — صُورَةٌ مَفْرُوضَةٌ: وَاوُ الْعَطْفِ، ثُمَّ الْوَاوُ لَوْ بَقِيَتْ حَرْفَ مُضَارَعَةٍ، ثُمَّ فَاءُ «وَجِلَ»، فَتَجْتَمِعُ ثَلَاثُ وَاوَاتٍ.",
  "The word itself is quoted; in the place of jarr as the mudaf ilayh — a supposed form: the wāw of joining, then the wāw had it stayed the muḍāriʿ's letter, then the first radical of «وَجِلَ»: three wāws in a row.",
  "Kelimenin kendisi kastedilmiştir (hikâye); mahallen mecrûr, muzâfun ileyh — farazî bir şekil: atıf vâvı, sonra muzâraat harfi olarak kalsaydı vâv, sonra «وَجِلَ»nin fâsı: art arda üç vâv.", key="wajila", pos="verb", enc="")
L("19:s9:1", *THAMMA, key="thamma", pos="noun")
R("19:s9:3", "mubtada", "raf")
L("19:s9:3", "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَخَبَرُهُ جُمْلَةُ «لَا يَصْلُحُ».", "The mubtada, in raf'; the sign is the damma; its khabar is the clause «لَا يَصْلُحُ».", "Mübtedâ, merfû; alâmeti damme ile; haberi «لَا يَصْلُحُ» cümlesidir.", key="awwal", pos="noun")
L("19:s10:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "The waw conjoins; a passive past verb, built on fatha; its deputy doer is the jarr phrase after it.", "«ve» atıf harfi; meçhul mâzî fiil, feth üzere mebnî; nâib-i fâili sonraki câr-mecrûrdur.", key="hakama", pos="verb")
L("19:s10:2", "اسْمُ «أَنَّ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of «أَنَّ», in nasb; the sign is the fatha; annexed (mudaf).", "«أَنَّ»nin ismi, mansûb; alâmeti fetha ile; muzâf.", key="waw-letter", pos="noun")
L("19:s10:3", *QUOTE, key="warantal", pos="noun")
R("19:s10:4", "innaKhabar", "raf"); L("19:s10:4", *KHANNA, key="asli", pos="noun")
R("19:s11:8", "mubtada", "raf"); L("19:s11:8", *MUBTW, key="ghaib", pos="noun")
L("19:s11:9", *FASL, key="huwa", pos="pron")
L("19:s11:10", *ALLADHI("الْجَارُّ وَالْمَجْرُورُ «فِي وَسَطِ كَلَامِ الْمُتَكَلِّمِ وَالْمُخَاطَبِ»", "the jarr phrase «فِي وَسَطِ كَلَامِ الْمُتَكَلِّمِ وَالْمُخَاطَبِ»", "«فِي وَسَطِ كَلَامِ الْمُتَكَلِّمِ وَالْمُخَاطَبِ» câr-mecrûrudur"), key="alladhi", pos="pron")
L("19:s12:10", *QFI, key="daraba", pos="verb", enc="")
L("19:s13:2", "اللَّامُ حَرْفُ جَرٍّ، وَ«مَ» اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ الْمُقَدَّرِ فِي مَحَلِّ جَرٍّ، حُذِفَتْ أَلِفُهُ لِدُخُولِ الْجَارِّ عَلَيْهِ.", "The lam is a preposition; «مَ» is the question noun «مَا», in the place of jarr — its alif is dropped because a jarr letter has come upon it.", "Lâm harf-i cerdir; «مَ» istifhâm ismi «مَا»dır, mahallen mecrûr — üzerine câr girdiği için elifi düşmüştür.", key="lima", pos="pron")
L("19:s13:6", *QFI, key="daraba", pos="verb")
R("19:s14:7", "fail", "raf")
L("19:s14:8", *PMUB(WAW, "هُوَ", "الْفَتْحِ", "fatha", "feth"), key="huwa", pos="pron")
# ---- chapter 20
L("20:s1:0", *PASS(*WAW, **TFEM), key="fataha", pos="verb")
L("20:s1:1", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "A demonstrative, built on kasra, in the place of raf' as the deputy doer.", "İsm-i işâret, kesre üzere mebnî, mahallen merfû nâib-i fâil.", key="hadhihi", pos="pron")
L("20:s1:7", *PMUB(WAW, "هُوَ", "الْفَتْحِ", "fatha", "feth"), key="huwa", pos="pron")
L("20:s1:8", *QKH, key="falala-wazn", pos="noun")
L("20:s1:10", *QMATFR, key="faala", pos="verb")
L("20:s1:12", *QMATFR, key="faaala-wazn", pos="noun")
L("20:s1:14", *QMATFR, key="faaala3-wazn", pos="noun")
L("20:s2:1", "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ».", "A demonstrative, built on kasra, in the place of nasb as the noun of «أَنَّ».", "İsm-i işâret, kesre üzere mebnî, mahallen mansûb, «أَنَّ»nin ismi.", key="hadhihi", pos="pron")
R("20:s2:4", "mubtada", "raf"); L("20:s2:4", *MUBTW, key="rubai", pos="noun")
R("20:s2:5", "khabar", "raf")
L("20:s4:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ.", "The waw conjoins; a present verb in the passive, in raf'; the sign is the visible damma.", "«ve» atıf harfi; muzâri fiil (meçhul), merfû; alâmeti zâhir damme.", key="fataha", pos="verb")
L("20:s4:1", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ، وَصِلَتُهُ الظَّرْفُ «وَرَاءَهُنَّ».", "A relative noun, built on sukun, in the place of raf' as the deputy doer; its sila is the adverb «وَرَاءَهُنَّ».", "İsm-i mevsûl, sükûn üzere mebnî, mahallen merfû nâib-i fâil; sılası «وَرَاءَهُنَّ» zarfıdır.", key="ma-mawsula", pos="pron")
L("20:s5:1", *QAMMA, key="yuhariqu-cited", pos="noun")
L("20:s5:2", "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْجُمْلَةُ «أَصْلُهُ يُرِيقُ» خَبَرُ الْمُبْتَدَإِ الْأَوَّلِ.",
  "A second mubtada, in raf'; the sign is the damma; annexed, and the hāʾ is an attached pronoun, the mudaf ilayh; the clause «أَصْلُهُ يُرِيقُ» is the khabar of the first mubtada.", "İkinci mübtedâ, merfû; alâmeti damme ile; muzâftır, hâ bitişik zamir, muzâfun ileyh; «أَصْلُهُ يُرِيقُ» cümlesi birinci mübtedânın haberidir.", key="asl", pos="noun")
L("20:s5:3", *QKH, key="yuriqu-cited", pos="noun")
L("20:s5:4", *PMUB(WAW, "هُوَ", "الْفَتْحِ", "fatha", "feth"), key="huwa", pos="pron")
L("20:s5:7", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "The fa stands in the answer of «أَمَّا»; a passive past verb, built on fatha; the tāʾ marks the feminine and takes a kasra because two quiescent letters meet.", "Fâ «أَمَّا»nın cevabındadır; meçhul mâzî fiil, feth üzere mebnî; tâ te'nis içindir, iki sâkin karşılaştığı için kesre ile harekelenmiştir.", key="zada", pos="verb")
R("20:s6:19", "khabar", "raf"); L("20:s6:19", *NAHW, key="nahw", pos="noun")
L("20:s6:20", *DIAL(*DMI), key="alima", pos="verb")
for _i in (22, 24, 26): L("20:s6:%d" % _i, *DIAL(*DAT), key="alima", pos="verb")
for _i in (28, 30, 32, 34): L("20:s6:%d" % _i, *DIAL(*DAT), key="istansara", pos="verb")
L("20:s8:0", *PASS(*WAW, **TFEM), key="ayyana-appoint", pos="verb")
L("20:s8:12", "الْفَاءُ لِلتَّفْرِيعِ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fa draws the consequence; the mubtada, in raf'; the sign is the damma; annexed (mudaf).", "Fâ tefrî' içindir; mübtedâ, merfû; alâmeti damme ile; muzâf.", key="ita", pos="noun")
L("20:s8:15", *AWLA, key="awla-fitter", pos="noun")
L("20:s9:2", *MUDRAF, key="lazima", pos="verb")
R("20:s9:5", "fail", "raf")
L("20:s9:5", "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ.", "The doer (fa'il), in raf'; the sign is a damma estimated on the yāʾ, too heavy to show; annexed (mudaf).", "Fâil, merfû; alâmeti yâ üzerinde mukadder damme (sıklet sebebiyle); muzâf.", key="tawali", pos="noun")
L("20:s9:13", *QUOTE, key="yafilu-wazn", pos="noun")
L("20:s9:15", *QMATF, key="faala", pos="verb")
L("20:s10:4", *MITHLFI, key="mithl", pos="noun")
L("20:s10:5", *QUOTE, key="taqallada", pos="verb")
L("20:s10:7", *QMATF, key="tabaaada", pos="verb")
L("20:s10:9", *QMATF, key="tabakhtara", pos="verb")
R("20:s10:11", "mudafIlayh", "jarr")
# ---- part eight (pp. 60–62): the end of the faṣl on the future — the quiescent ḍād and bāʾ, the tāʾ of the one addressed and the
#      absent woman, the nūn of rafʿ, and what «لَمْ» does
LIMA = tuple(F["19:s13:2"]["irab"][k_] for k_ in ("ar", "en", "tr"))
THAMMA = ("اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ بِـ«مِنْ» — وَ«مِنْ ثَمَّ»: مِنْ أَجْلِ ذٰلِكَ.",
          "A demonstrative of place («there»), built on fatha, in the place of jarr after «مِنْ» — «مِنْ ثَمَّ»: for that reason.",
          "Mekân için ism-i işaret («orası»), feth üzere mebnî, «مِنْ» ile mahallen mecrûr — «مِنْ ثَمَّ»: bundan ötürü.")
BAM = ("الْبَاءُ حَرْفُ جَرٍّ، وَمَجْرُورٌ بِهِ بِالْكَسْرَةِ، مُضَافٌ.", "The ba is a preposition; in jarr after it; the sign is the kasra; annexed (mudaf).", "Bâ harf-i cerdir; onunla mecrûr; alâmeti kesre ile; muzâf.")
MIM = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "The mudaf ilayh (second term of the idafa), in jarr; the sign is the kasra; annexed (mudaf).", "Muzâfun ileyh, mecrûr; alâmeti kesre ile; muzâf.")
def TAWK(v): return ("ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ، تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ فِي «" + v + "».",
                     "A detached pronoun, built on fatha, in the place of raf': it emphasises the pronoun hidden in «" + v + "».",
                     "Ayrı zamir, feth üzere mebnî, mahallen merfû: «" + v + "»daki gizli zamirin te'kididir.")

# 21 — سُكُونُ الضَّادِ
L("21:s1:3", *QFI, key="daraba", pos="verb")
R("21:s1:4", "mafulLah", "nasb"); K("21:s1:4", "firar")
R("21:s2:9", "mubtada", "raf")
L("21:s2:9", "الْفَاءُ لِلتَّفْرِيعِ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fāʾ draws the consequence; the mubtada, in raf'; the sign is the damma; annexed (mudaf).", "Fâ tefrî içindir; mübtedâ, merfû; alâmeti damme ile; muzâf.", key="iskan", pos="noun")
R("21:s2:15", "khabar", "raf"); L("21:s2:15", *tuple(x.replace("إِعْطَاءُ", "إِسْكَانُ") for x in AWLA), key="awla-fitter", pos="noun")
# (wave 193: by the packager's rule) L("21:s3:1", *THAMMA, key="thamma", pos="noun")
L("21:s3:5", *QFI, key="daraba", pos="verb", enc="")

# 22 — تَاءُ الْمُخَاطَبِ وَالْغَائِبَةِ
L("22:s1:5", *MITHLFI, key="mithl", pos="noun")
SHV("22:s1:6", HMD, "أَنْتَ", True, TJQ)
L("22:s1:7", *TAWK("تَضْرِبُ"), key="anta", pos="pron")
SHV("22:s1:9", HMD, "هِيَ", False, TJA)
L("22:s1:10", *TAWK("تَضْرِبُ"), key="hiya", pos="pron")
R("22:s1:11", "jarr", "jarr")
L("22:s1:11", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«اسْتِوَاءِ» مَجْرُورٌ بِهِ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ، وَ«هُمَا» ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
  "The lam is a preposition of cause; «اسْتِوَاءِ» is in jarr after it; the sign is the kasra; it is annexed (mudaf), and «هُمَا» is an attached pronoun in the place of jarr as the mudaf ilayh.",
  "Lâm ta'lîl için harf-i cerdir; «اسْتِوَاءِ» onunla mecrûr; alâmeti kesre ile; muzâftır, «هُمَا» da mahallen mecrûr muzâfun ileyh olan bitişik zamirdir.", key="istiwa", pos="noun")
R("22:s1:14", "khabar", "raf"); L("22:s1:14", *NAHW, key="mithl", pos="noun")
L("22:s1:15", *QUOTE, key="nasara", pos="verb", enc="")
L("22:s1:17", *QMATF, key="nasara", pos="verb", enc="")
K("22:s2:2", "askana-sukun")
K("22:s2:7", "ibtida-start")
L("22:s3:7", *MITHLFI, key="mithl", pos="noun")
L("22:s3:8", *QUOTE, key="madaha", pos="verb")
L("22:s4:6", *DIAL(*DMI), key="alima", pos="verb")

# 23 — نُونُ الرَّفْعِ وَ«لَمْ»
# (wave 193: by the packager's rule) L("23:s1:2", *LIMA, key="lima", pos="pron")
L("23:s1:3", *CAP(PASS("", "", "")), key="adkhala", pos="verb")
R("23:s2:1", "hal", "nasb")
L("23:s2:1", "حَالٌ مِنَ النُّونِ مَنْصُوبٌ بِالْفَتْحَةِ، وَعَامِلُهُ مَحْذُوفٌ تَقْدِيرُهُ «أُدْخِلَ».", "A hal (circumstantial) of the nūn, in nasb; the sign is the fatha; its governor is omitted — «it was brought in».", "Nûndan hâl, mansûb; alâmeti fetha ile; âmili mahzuftur, takdiri «أُدْخِلَ»dir.", key="alama", pos="noun")
L("23:s2:7", *BAM, key="ittisal", pos="noun")
L("23:s2:11", *MIM, key="wasat", pos="noun")
L("23:s3:1", "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The excepted noun (mustathna), in nasb; the sign is the fatha; annexed (mudaf).", "Müstesnâ, mansûb; alâmeti fetha ile; muzâf.", key="nun-letter", pos="noun")
L("23:s3:2", *QUOTE, key="daraba", pos="verb", enc="")
L("23:s3:3", *PMUB(HALW, "هُوَ", "الْفَتْحِ", "fatha", "feth"), key="huwa", pos="pron")
L("23:s3:8", *QFI, key="faala", pos="verb", enc="")
# (wave 193: by the packager's rule) L("23:s4:1", *THAMMA, key="thamma", pos="noun")
K("23:s4:8", "alama")   # the annexed dual: the engine writes the line itself since wave 190
L("23:s5:0", *MUBTW, key="ya-letter", pos="noun")
L("23:s5:2", *QFI, key="daraba", pos="verb", enc="")
R("23:s5:3", "khabar", "raf"); L("23:s5:3", *KHM, key="damir", pos="noun")
L("23:s6:1", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَهُوَ فِعْلُ الشَّرْطِ.", "A past verb, built on fatha; it is the verb of the condition.", "Mâzî fiil, feth üzere mebnî; şart fiilidir.", key="dakhala", pos="verb")
L("23:s6:2", *QUO("فِي مَحَلِّ رَفْعٍ فَاعِلُ «دَخَلَ»", "in the place of raf' as the doer of «دَخَلَ»", "«دَخَلَ»nin fâili olarak mahallen merfû"), key="lam-jazima", pos="part")
L("23:s6:3", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.", "A present verb, in raf'; the sign is the visible damma; its clause is the answer of «إِذَا» and has no place in the i'rab.", "Muzâri fiil, merfû; alâmeti zâhir damme ile; cümlesi «إِذَا»nın cevabıdır, i'râbdan mahalli yoktur.", key="intaqala", pos="verb")
R("23:s6:4", "fail", "raf")
L("23:s6:4", "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The doer (fa'il), in raf'; the sign is a damma estimated on the alif, which can carry none; it is annexed (mudaf), and the hāʾ is an attached pronoun in the place of jarr as the mudaf ilayh.", "Fâil, merfû; alâmeti elif üzerinde takdir edilen damme ile (taazzür); muzâftır, hâ da mahallen mecrûr muzâfun ileyh olan bitişik zamirdir.", key="mana", pos="noun")
K("23:s6:8", "mushabih")

PASSMT = ("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هِيَ» يَعُودُ إِلَى تَاءِ الْمُضَارَعَةِ.",
          "A present verb in the passive, in raf'; the sign is the visible damma; its deputy doer is a hidden pronoun, «هِيَ», going back to the tāʾ of the muḍāriʿ.",
          "Meçhul muzâri fiil, merfû; alâmeti zâhir damme ile; nâib-i fâili, muzâraat tâsına dönen gizli «هِيَ» zamiridir.")
L("22:s1:0", *tuple(F["10:s16:0"]["irab"][k_] for k_ in ("ar", "en", "tr")), key="sawwa", pos="verb")
L("22:s2:2", *PASSMT, key="askana-sukun", pos="verb")
L("22:s3:1", *PASSMT, key="damma-verb", pos="verb")
L("22:s4:1", *PASSMT, key="kasara", pos="verb")
# ---- part nine (pp. 63–66): the faṣl on the amr and the nahy opens — the lām of the absent one, its kasra and its sukūn, the dropped letter
#      of the future, and the hamza of connection. Cited VERBS after مِثْل / فِي / خِلَاف are named by the packager's own rule (wave 191).
def MT1(obj_ar="", obj_en="", obj_tr=""):
    return ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + obj_ar + ".",
            "A past verb, built on sukun because the tāʾ of the doer is attached; the tāʾ is an attached pronoun, built on damma, in the place of raf' as the doer" + obj_en + ".",
            "Mâzî fiil, fâil tâsı bitiştiği için sükûn üzere mebnî; tâ, damme üzere mebnî bitişik zamirdir, fâil olarak mahallen merfû" + obj_tr + ".")
PASSF = ("الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ حَرْفٌ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ",
         "The waw conjoins; a passive past verb, built on fatha; the tāʾ marks the feminine, a letter with no place in the i'rab",
         "«ve» atıf harfi; meçhul mâzî fiil, feth üzere mebnî; tâ te'nîs içindir, i'râbda mahalli olmayan bir harftir")
NAIBM = ("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The deputy doer (na'ib al-fa'il), in raf'; the sign is the damma; annexed (mudaf).", "Nâib-i fâil, merfû; alâmeti damme ile; muzâf.")
NAIB = ("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "The deputy doer (na'ib al-fa'il), in raf'; the sign is the damma.", "Nâib-i fâil, merfû; alâmeti damme ile.")

# 24 — الْأَمْرُ وَلَامُ الْغَائِبِ
R("24:s1:7", "khabar", "raf"); L("24:s1:7", *NAHW, key="mithl", pos="noun")
L("24:s6:2", "الْفَاءُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ الثَّانِيَةُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
  "The fa conjoins; a past verb, built on sukun because the nūn of the women is attached; that nūn is an attached pronoun, built on fatha, in the place of raf' as the doer; the second nūn is the nūn of protection, and the yāʾ is an attached pronoun, built on sukun, in the place of nasb as the object.",
  "«fe» atıf harfi; mâzî fiil, nûn-ı nisve bitiştiği için sükûn üzere mebnî; o nûn, feth üzere mebnî bitişik zamirdir, fâil olarak mahallen merfû; ikinci nûn vikâye nûnudur; yâ da sükûn üzere mebnî bitişik zamirdir, mef'ûlün bih olarak mahallen mansûb.", key="shayyaba", pos="verb")
L("24:s6:4", "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ، وَخَبَرُهَا جُمْلَةُ «هَوِيتُ السِّمَانَا».",
  "An incomplete past verb, one of kāna's sisters, built on sukun because the tāʾ of the doer is attached; the tāʾ is an attached pronoun, built on damma, in the place of raf' as kāna's noun; her khabar is the clause «هَوِيتُ السِّمَانَا».",
  "Nâkıs mâzî fiil, kâne'nin kardeşlerinden; fâil tâsı bitiştiği için sükûn üzere mebnî; tâ, damme üzere mebnî bitişik zamirdir, kâne'nin ismi olarak mahallen merfû; haberi «هَوِيتُ السِّمَانَا» cümlesidir.", key="kana", pos="verb", enc="")
R("24:s6:5", "zarf", "nasb"); L("24:s6:5", "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِـ«هَوِيتُ».", "An adverb of time, in nasb; the sign is the fatha; it attaches to «هَوِيتُ».", "Zaman zarfı, mansûb; alâmeti fetha ile; «هَوِيتُ»ye müteallıktır.", key="qidm", pos="noun")
L("24:s6:6", *MT1("، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause is in the place of nasb as kāna's khabar", "; cümle, kâne'nin haberi olarak mahallen mansûbdur"), key="hawiya", pos="verb", enc="")
R("24:s6:7", "maful", "nasb"); L("24:s6:7", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَالْأَلِفُ لِلْإِطْلَاقِ.", "The direct object, in nasb; the sign is the fatha; the alif is the alif of the rhyme (iṭlāq).", "Mef'ûlün bih, mansûb; alâmeti fetha ile; elif ıtlâk (kafiye) elifidir.", key="samin", pos="noun")
R("24:s7:1", "khabar", "raf"); L("24:s7:1", "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «هِيَ»، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The khabar of an omitted mubtada — «they are» — in raf'; the sign is the damma; annexed (mudaf).", "Mahzuf bir mübtedânın («هِيَ») haberi, merfû; alâmeti damme ile; muzâf.", key="harf", pos="noun")
L("24:s7:2", "الْجُمْلَةُ مَحْكِيَّةٌ قُصِدَ لَفْظُهَا، فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ؛ وَ«هَوِيتُ» فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلُهُ.", "The clause is quoted for its wording, in the place of jarr as the mudaf ilayh; «هَوِيتُ» is a past verb and the tāʾ is its doer.", "Cümle lafzı kastedilerek hikâye edilmiştir; mahallen mecrûr, muzâfun ileyh; «هَوِيتُ» mâzî fiildir, tâ fâilidir.", key="hawiya", pos="verb", enc="")
R("24:s8:8", "fail", "raf"); L("24:s8:8", "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "The doer (fa'il), in raf'; the sign is the alif, because it is a dual; its nūn has dropped for the annexation; annexed (mudaf).", "Fâil, merfû; alâmeti elif iledir, çünkü tesniyedir; nûnu izâfet için düşmüştür; muzâf.", key="harf", pos="noun")

# 25 — كَسْرُ لَامِ الْأَمْرِ
K("25:s1:12", "fil")
L("25:s2:0", PASSF[0] + "، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هِيَ» يَعُودُ إِلَى اللَّامِ.", PASSF[1] + "; the deputy doer is a hidden pronoun — «it» — going back to the lām.", PASSF[2] + "; nâib-i fâil, lâma dönen gizli «هِيَ» zamiridir.", key="askana-sukun", pos="verb")
L("25:s2:6", *QMATF, key="thumma", pos="part")
R("25:s2:7", "khabar", "raf"); L("25:s2:7", *NAHW, key="mithl", pos="noun")
L("25:s2:12", "حَرْفُ عَطْفٍ مَحْكِيٌّ مَعَ مَا بَعْدَهُ، وَاللَّفْظُ الْمَحْكِيُّ «ثُمَّ لْيَضْرِبْ» مَعْطُوفٌ عَلَى مَا قَبْلَهُ فِي مَحَلِّ جَرٍّ.", "A conjunction quoted with what follows it; the quoted wording «ثُمَّ لْيَضْرِبْ» is joined to the word before it, in the place of jarr.", "Ardındakiyle birlikte hikâye edilen atıf harfi; hikâye edilen «ثُمَّ لْيَضْرِبْ» lafzı öncekine ma'tûftur, mahallen mecrûr.", key="thumma", pos="part")
L("25:s2:13", "اللَّامُ لَامُ الْأَمْرِ سَاكِنَةٌ بَعْدَ «ثُمَّ»، وَفِعْلٌ مُضَارِعٌ مَجْزُومٌ بِهَا، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ جَوَازًا تَقْدِيرُهُ «هُوَ».", "The lām is the lām of command, quiescent after «ثُمَّ»; a present verb in jazm by it; the sign is the sukun; the doer is a pronoun hidden by choice — «he».", "Lâm, «ثُمَّ»den sonra sâkin olan emir lâmıdır; onunla meczûm muzâri fiil; alâmeti sükûn; fâil, cevâzen gizli «هُوَ» zamiridir.", key="daraba", pos="verb", enc="")
L("25:s3:4", *QFI, key="fakhidh", pos="noun")
L("25:s4:1", *QUO("فِي مَحَلِّ رَفْعٍ خَبَرُ «نَظِيرُهُ»", "in the place of raf' as the khabar of «نَظِيرُهُ»", "«نَظِيرُهُ»nün haberi olarak mahallen merfû"), key="hiya", pos="pron", enc="")
L("25:s4:3", *QMATFR, key="hiya", pos="pron", enc="")
L("25:s6:0", "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "The waw conjoins; a passive past verb, built on fatha.", "«ve» atıf harfi; meçhul mâzî fiil, feth üzere mebnî.", key="ayyana-appoint", pos="verb")
R("25:s6:1", "naib", "raf"); L("25:s6:1", *NAIB, key="hadhf", pos="noun")
L("25:s7:9", *QUO("فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلِ «يُقَالُ»", "in the place of raf' as the deputy doer of «يُقَالُ»", "«يُقَالُ»nün nâib-i fâili olarak mahallen merfû"), key="daraba", pos="verb", enc="")

# 26 — هَمْزَةُ الْوَصْلِ
L("26:s2:3", *QFI, key="daraba", pos="verb", enc="")
L("26:s3:5", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَ«أَنَّ» حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، وَخَبَرُهَا جُمْلَةُ «يَلْزَمُ الْخُرُوجُ».", "The lam is a preposition of cause; «أَنَّ» is a particle of emphasis and nasb; its noun is the pronoun of the matter, omitted, and its khabar is the clause «يَلْزَمُ الْخُرُوجُ».", "Lâm ta'lîl için harf-i cerdir; «أَنَّ» te'kid ve nasb harfidir; ismi mahzuf zamîr-i şe'ndir, haberi «يَلْزَمُ الْخُرُوجُ» cümlesidir.", key="lianna", pos="part")
K("26:s4:2", "kaf-letter")
L("26:s4:9", *KHK("يَكُونُ"), key="hajiz", pos="noun")
R("26:s4:10", "nat", "nasb"); L("26:s4:10", "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "An adjective (na't), in nasb; the sign is the fatha.", "Sıfat (na't), mansûb; alâmeti fetha ile.", key="hasin", pos="noun")
R("26:s5:3", "naib", "raf"); L("26:s5:3", *NAIBM, key="waw-letter", pos="noun")
L("26:s5:5", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb; the sign is the fatha.", "İkinci mef'ûl, mansûb; alâmeti fetha ile.", key="ya-letter", pos="noun")
R("26:s8:0", "zarf", "nasb"); L("26:s8:0", "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِـ«أَشْرَبْ».", "An adverb of time, in nasb; the sign is the fatha; it attaches to «أَشْرَبْ».", "Zaman zarfı, mansûb; alâmeti fetha ile; «أَشْرَبْ»ye müteallıktır.", key="yawm", pos="noun")
L("26:s8:1", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَسُكِّنَ آخِرُهُ لِضَرُورَةِ الشِّعْرِ — وَهُوَ مَوْضِعُ الشَّاهِدِ — وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ «أَنَا».", "A present verb, in raf'; its last letter is made quiescent for the metre — this is the point the verse is quoted for — and the doer is a pronoun hidden by necessity — «I».", "Muzâri fiil, merfû; son harfi şiir zarureti için sâkin kılınmıştır — beytin şâhid yeri burasıdır —; fâil, vücûben gizli «أَنَا» zamiridir.", key="shariba", pos="verb", enc="")
R("26:s8:5", "maful", "nasb"); L("26:s8:5", "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ «مُسْتَحْقِبٍ»، مَنْصُوبٌ بِالْفَتْحَةِ.", "The direct object of the active participle «مُسْتَحْقِبٍ», in nasb; the sign is the fatha.", "İsm-i fâil «مُسْتَحْقِبٍ»in mef'ûlü, mansûb; alâmeti fetha ile.", key="ithm", pos="noun")
L("26:s9:6", "حَرْفُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A conditional particle that governs jazm, built on sukun; the clause is quoted, in the place of jarr as the mudaf ilayh.", "Cezm eden şart harfi, sükûn üzere mebnî; cümle hikâye edilmiştir, mahallen mecrûr, muzâfun ileyh.", key="in-shartiyya", pos="part")
R("26:s10:1", "naib", "raf"); L("26:s10:1", *NAIBM, key="alif-letter", pos="noun", enc="")
L("26:s10:2", *QUOTE, key="aymun", pos="noun", enc="")
R("26:s10:9", "mubtada", "raf"); L("26:s10:9", "الْوَاوُ عَاطِفَةٌ، وَمُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "The waw conjoins; the mubtada, in raf'; the sign is the damma; it is annexed (mudaf), and the hāʾ is an attached pronoun in the place of jarr as the mudaf ilayh; its khabar is the jarr phrase after it.", "«ve» atıf harfi; mübtedâ, merfû; alâmeti damme ile; muzâftır, hâ da mahallen mecrûr muzâfun ileyh olan bitişik zamirdir; haberi ardındaki câr-mecrûrdur.", key="alif-letter", pos="noun")

# ---- part ten (pp. 66–70): the alif of «أَكْرِمْ» and the hamza of «اِعْلَمْ» in writing, the amr apocopated or built, the two nūns of emphasis.
#      Cited verbs and particles are named by the packager's rules (waves 191, 193): after a construct head, after any jarr letter, in a list
#      of cited forms; «لِمَ», «ثَمَّ» and «نَحْوُ» by their written vowels and seat. What is left here is what only the meaning decides.
KHHU = ("خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «هُوَ»، مَرْفُوعٌ بِالضَّمَّةِ", "The khabar of an omitted mubtada — «it is» — in raf'; the sign is the damma", "Mahzuf bir mübtedânın («هُوَ») haberi, merfû; alâmeti damme ile")
MLAH = ("مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The object of purpose (maf'ul li-ajlih), in nasb; the sign is the fatha.", "Mef'ûlün lieclih, mansûb; alâmeti fetha ile.")
def LAMR(tail_ar="", tail_en="", tail_tr=""):
    return ("الْفَاءُ عَاطِفَةٌ، وَاللَّامُ لَامُ الْأَمْرِ سَاكِنَةٌ بَعْدَ الْفَاءِ، وَفِعْلٌ مُضَارِعٌ مَجْزُومٌ بِهَا، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَهُوَ مَوْضِعُ الشَّاهِدِ: أَمْرُ الْمُخَاطَبِ بِاللَّامِ" + tail_ar + ".",
            "The fa conjoins; the lam is the lam of command, quiescent after the fa; a present verb in jazm by it, the sign being the dropped nun; the waw is an attached pronoun, built on sukun, in the place of raf' as the doer — the point of the citation: the one addressed is commanded with the lam" + tail_en + ".",
            "Fâ atıf harfidir; lâm, fâdan sonra sâkin emir lâmıdır; fiil onunla meczûm muzâridir, cezm alâmeti nûnun hazfidir; vâv, sükûn üzere mebnî bitişik zamirdir, fâil olarak mahallen merfû — şâhid yeri: muhâtabın lâm ile emredilmesi" + tail_tr + ".")

# 27 — أَلِفُ «أَكْرِمْ» وَهَمْزَةُ «اِعْلَمْ» فِي الْخَطِّ
R("27:s1:9", "khabar", "raf"); L("27:s1:9", KHHU[0] + "، مُضَافٌ.", KHHU[1] + "; annexed (mudaf).", KHHU[2] + "; muzâf.", key="alif-letter", pos="noun", enc="")
R("27:s1:11", "nat", "raf"); L("27:s1:11", "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "An adjective (na't), in raf'; the sign is the damma.", "Sıfat (na't), merfû; alâmeti damme ile.", key="mahdhuf", pos="noun")
L("27:s2:7", *QUO("فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ»", "in the place of raf' as the khabar of «أَنَّ»", "«أَنَّ»nin haberi olarak mahallen merfû"), key="akrama", pos="verb", enc="")
R("27:s5:3", "mafulMutlaq", "nasb"); L("27:s5:3", "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ، أَيْ: تَرْكًا كَثِيرًا.", "Standing in for the absolute object, in nasb; the sign is the fatha — the adjective of an omitted masdar: «a frequent leaving».", "Mef'ûl-i mutlaktan nâib, mansûb; alâmeti fetha ile — hazfedilmiş bir masdarın sıfatı: «çokça bırakma».", key="kathir", pos="noun")
R("27:s5:10", "atf", "jarr"); L("27:s5:10", "مَعْطُوفٌ عَلَى «عُمَرَ» مَجْرُورٌ بِالْكَسْرَةِ، وَالْوَاوُ فِي آخِرِهِ تُكْتَبُ وَلَا تُنْطَقُ — وَهِيَ مَوْضِعُ الشَّاهِدِ: فَرْقٌ بَيْنَهُ وَبَيْنَ «عُمَرَ» فِي الْخَطِّ.", "Joined to «عُمَرَ», in jarr; the sign is the kasra. The waw at its end is written, not spoken — the point of the citation: it tells the word from «عُمَر» in writing.", "«عُمَرَ»ye ma'tûf, mecrûr; alâmeti kesre ile. Sonundaki vâv yazılır, okunmaz — şâhid yeri budur: yazıda «عُمَر»den ayırır.", key="amr-name", pos="propn")
L("27:s6:2", "الْبَاءُ حَرْفُ جَرٍّ، وَ«اسْمِ» مَجْرُورٌ بِهِ بِالْكَسْرَةِ، مُضَافٌ — وَاللَّفْظُ «بِسْمِ اللهِ» مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِـ«فِي».", "The ba is a preposition; «اسْمِ» is in jarr after it, the sign being the kasra; annexed — and the wording «بِسْمِ اللهِ» is quoted, in the place of jarr after «فِي».", "Bâ harf-i cerdir; «اسْمِ» onunla mecrûr, alâmeti kesre; muzâf — «بِسْمِ اللهِ» lafzı hikâye edilmiştir, «فِي» ile mahallen mecrûr.", key="bism", pos="noun")
L("27:s7:3", "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ «أَنْتَ» — وَاللَّفْظُ الْمَذْكُورُ مِنَ الْآيَةِ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِـ«فِي».", "An imperative verb, built on sukun; its doer is a hidden pronoun «أَنْتَ», hidden by necessity — the words cited from the verse are quoted, in the place of jarr after «فِي».", "Emir fiili, sükûn üzere mebnî; fâili vücûben müstetir «أَنْتَ» zamiridir — âyetten anılan lafız hikâye edilmiştir, «فِي» ile mahallen mecrûr.", key="qaraa", pos="verb", enc="")
L("27:s7:6", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«رَبِّ»، وَصِلَتُهُ لَمْ تُذْكَرْ هُنَا — عِنْدَهُ يَنْتَهِي الْمَحْكِيُّ.", "A relative noun, built on sukun, in the place of jarr as the adjective of «رَبِّ»; its relative clause is not cited here — the quotation stops at it.", "İsm-i mevsûl, sükûn üzere mebnî; «رَبِّ»nin sıfatı olarak mahallen mecrûr; sılası burada anılmamıştır — alıntı onda biter.", key="alladhi", pos="pron")

# 28 — جَزْمُ الْأَمْرِ وَبِنَاؤُهُ
L("28:s2:7", *QUO("فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ»", "in the place of raf' as the khabar of «أَنَّ»", "«أَنَّ»nin haberi olarak mahallen merfû"), key="daraba", pos="verb", enc="")
L("28:s3:9", "الْفَاءُ حَرْفُ عَطْفٍ، وَالْبَاءُ حَرْفُ جَرٍّ، وَ«ذٰلِكَ» اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ، مُتَعَلِّقٌ بِـ«تَفْرَحُوا» — وَاللَّفْظُ الْمَقْرُوءُ مَحْكِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«قَرَأَ».", "The fa conjoins; the ba is a preposition; «ذٰلِكَ» is a demonstrative, built on fatha, in the place of jarr — attached to «تَفْرَحُوا». The wording recited is quoted, in the place of nasb as the object of «قَرَأَ».", "Fâ atıf harfi, bâ harf-i cerdir; «ذٰلِكَ» feth üzere mebnî ism-i işarettir, mahallen mecrûr — «تَفْرَحُوا»ya müteallık. Okunan lafız hikâye edilmiştir; «قَرَأَ»nın mef'ûlü olarak mahallen mansûb.", key="dhalika", pos="pron")
L("28:s3:10", *LAMR(), key="fariha", pos="verb", enc="")
R("28:s7:0", "jarr", "jarr"); L("28:s7:0", "الْفَاءُ نَائِبَةٌ عَنْ «رُبَّ» الْمَحْذُوفَةِ عَامِلَةٌ عَمَلَهَا — وَهُوَ مَوْضِعُ الشَّاهِدِ — وَ«مِثْلِ» مَجْرُورٌ لَفْظًا بِهَا، مَنْصُوبٌ مَحَلًّا مَفْعُولٌ بِهِ مُقَدَّمٌ لِـ«طَرَقْتُ»، وَهُوَ مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The fa stands in for an omitted «رُبَّ» and does its work — the point of the verse; «مِثْلِ» is in jarr in wording by it, and in the place of nasb as the fronted object of «طَرَقْتُ»; it is annexed, and the kaf is an attached pronoun, built on kasra, in the place of jarr as the mudaf ilayh.", "Fâ, hazfedilmiş «رُبَّ»nin yerini tutar ve onun amelini yapar — beytin şâhidi budur; «مِثْلِ» onunla lafzen mecrûr, «طَرَقْتُ»nun öne geçmiş mef'ûlü olarak mahallen mansûbdur; muzâftır, kâf kesre üzere mebnî bitişik zamirdir, muzâfun ileyh olarak mahallen mecrûr.", key="mithl", pos="noun")
R("28:s7:1", "badal", "jarr"); L("28:s7:1", "بَدَلٌ مِنْ «مِثْلِ» مَجْرُورٌ عَلَى اللَّفْظِ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "An appositive (badal) of «مِثْلِ», in jarr with it in wording — by a kasra understood on the alif, which cannot carry it.", "«مِثْلِ»den bedel, lafza uyarak mecrûr; kesre, elif üzerinde mukadderdir (taazzür).", key="hubla", pos="noun")
R("28:s8:2", "khabar", "raf"); L("28:s8:2", KHHU[0] + ".", KHHU[1] + ".", KHHU[2] + ".", key="mabni", pos="noun")
L("28:s10:9", *LAMR("، وَاللَّفْظُ مَحْكِيٌّ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ لِلْمَصْدَرِ «قَوْلُهُ»", "; the wording is quoted, in the place of nasb as what the masdar «قَوْلُهُ» says", "; lafız hikâye edilmiştir, «قَوْلُهُ» masdarının mekûlü olarak mahallen mansûb"), key="fariha", pos="verb", enc="")
R("28:s10:10", "khabar", "raf"); L("28:s10:10", "خَبَرُ «قَوْلُهُ» مَرْفُوعٌ بِالضَّمَّةِ.", "The khabar of «قَوْلُهُ», in raf'; the sign is the damma.", "«قَوْلُهُ»nün haberi, merfû; alâmeti damme ile.", key="murab", pos="noun")

# 29 — نُونَا التَّأْكِيدِ فِي الْأَمْرِ
R("29:s2:4", "mafulLah", "nasb"); L("29:s2:4", *MLAH, key="firar", pos="noun")
R("29:s3:3", "mafulLah", "nasb"); L("29:s3:3", *MLAH, key="iktifa", pos="noun")
R("29:s3:7", "mafulLah", "nasb"); L("29:s3:7", *MLAH, key="iktifa", pos="noun")
L("29:s6:8", "مَجْرُورٌ بِـ«فِي» بِالْكَسْرَةِ، مُضَافٌ.", "In jarr after «فِي»; the sign is the kasra; annexed (mudaf).", "«فِي» ile mecrûr; alâmeti kesre ile; muzâf.", key="mithl", pos="noun")
L("29:s6:9", "حَرْفُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْجُمْلَةُ «هَلْ يَضْرِبَانِّ» مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A question particle, built on sukun; the clause «هَلْ يَضْرِبَانِّ» is quoted, in the place of jarr as the mudaf ilayh.", "İstifhâm harfi, sükûn üzere mebnî; «هَلْ يَضْرِبَانِّ» cümlesi hikâye edilmiştir, muzâfun ileyh olarak mahallen mecrûr.", key="hal", pos="part")
L("29:s6:10", "فِعْلٌ مُضَارِعٌ اتَّصَلَتْ بِهِ أَلِفُ الِاثْنَيْنِ وَنُونُ التَّوْكِيدِ الثَّقِيلَةُ، وَحُذِفَتْ مِنْهُ نُونُ الرَّفْعِ — وَهُوَ مَوْضِعُ الشَّاهِدِ — وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَنُونُ التَّوْكِيدِ حَرْفٌ مَبْنِيٌّ عَلَى الْكَسْرِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "A present verb with the alif of the two and the heavy nun of emphasis attached; the nun of raf' has been dropped from it — the point of the citation. The alif is an attached pronoun, built on sukun, in the place of raf' as the doer; the nun of emphasis is a letter, built on kasra, with no place in the i'rab.", "Tesniye elifi ve şeddeli te'kîd nûnu bitişmiş muzâri fiil; ref nûnu ondan hazfedilmiştir — şâhid yeri budur. Elif, sükûn üzere mebnî bitişik zamirdir, fâil olarak mahallen merfû; te'kîd nûnu kesre üzere mebnî bir harftir, i'râbda mahalli yoktur.", key="daraba", pos="verb", enc="")
L("29:s6:12", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ»، وَصِلَتُهُ الظَّرْفُ «قَبْلَ» وَمَا أُضِيفَ إِلَيْهِ.", "A relative noun, built on sukun, in the place of nasb as the noun of «أَنَّ»; its relative clause is the adverb «قَبْلَ» with what it is annexed to.", "İsm-i mevsûl, sükûn üzere mebnî; «أَنَّ»nin ismi olarak mahallen mansûb; sılası «قَبْلَ» zarfı ve muzâfun ileyhidir.", key="ma-mawsula", pos="pron")
L("29:s6:16", "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ يَعُودُ إِلَى «مَا»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».", "An incomplete present verb, one of kāna's sisters, in raf'; the sign is the damma; its noun is a hidden pronoun going back to «مَا»; the clause is in the place of raf' as the khabar of «أَنَّ».", "Nâkıs muzâri fiil, kâne'nin kardeşlerinden, merfû; alâmeti damme; ismi «مَا»ya dönen gizli zamirdir; cümle, «أَنَّ»nin haberi olarak mahallen merfûdur.", key="sara", pos="verb")
R("29:s6:17", "kanaKhabar", "nasb"); L("29:s6:17", *KHK("تَصِيرُ"), key="mabni", pos="noun")
R("29:s8:1", "mafulLah", "nasb"); L("29:s8:1", "مَفْعُولٌ لِأَجْلِهِ لِفِعْلٍ مَحْذُوفٍ دَلَّ عَلَيْهِ السُّؤَالُ، أَيْ: أُدْخِلَتْ فِرَارًا، مَنْصُوبٌ بِالْفَتْحَةِ.", "The object of purpose of an omitted verb that the question points to — «it was brought in to escape…» — in nasb; the sign is the fatha.", "Sorunun delâlet ettiği mahzuf fiilin mef'ûlün lieclihi — «…kaçınmak için getirildi» — mansûb; alâmeti fetha ile.", key="firar", pos="noun")

json.dump(F, open(H / "fixes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "fixes → fixes.json")
