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
json.dump(F, open(H / "fixes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "fixes → fixes.json")
