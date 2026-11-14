#!/usr/bin/env python3
"""mk_fixes.py — the author's corrections of the engines' reading of Marāḥ al-Arwāḥ (part one) → fixes.json.
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
json.dump(F, open(H / "fixes.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(F), "fixes → fixes.json")
