# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 66: the OPTIONAL building — the adverbs annexed to a sentence, and إِذْ, may be built on fatḥa (﴿هٰذَا يَوْمُ يَنْفَعُ
# الصَّادِقِينَ صِدْقُهُمْ﴾ al-Māʾida 5:119 — read يَوْمَ on fatḥa; and يَوْمَئِذٍ); likewise مِثْل and غَيْر with مَا, أَنْ and أَنَّ; the ism of the repeated lā joined to it,
# single and indefinite (﴿لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ﴾) — building both on fatḥa, rafʿ of both, fatḥa of the first with naṣb or rafʿ of the second, rafʿ of
# the first with fatḥa of the second: five ways allowed in its likes; and the single ṣifa of lā's built ism joined to it — built on fatḥa (لَا رَجُلَ ظَرِيفَ)
# or declined in rafʿ and naṣb (لَا رَجُلَ ظَرِيفٌ وَظَرِيفًا). Print p. 160.
# Readings: the verse is cited for the fatḥa reading (يَوْمَ, Nāfiʿ) that the matn illustrates; the iʿrāb line names the ḍamma reading too. The Ottoman
# commentary (izhar-full-corrected l. 1960 ff.) is followed for the five ways. The lithograph's وأن وأن is given as وَأَنْ وَأَنَّ.
#   python3 author_izhar_ch66.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"; AMS = "an-masdariyya"
NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; INS = "in-shartiyya"; JZ = "nawasib-wa-jawazim-al-mudari"; YM = "ya-al-mutakallim"; DF = "damir-fasl"
TMZ = "tamyiz"; IRB = "al-murab-wal-mabni-wal-irab"; LNJ = "la-nafiya-lil-jins"; IQ = "al-iqtibas-wal-tadmin"; JDS = "jam-mudhakkar-salim"; MJ = "mawadi-irab-al-jumla"; ISH = "asma-al-ishara-wa-sighuha"; MST = "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"
K = "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"
K65 = "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"
TITLE = {"ar": "جَائِزُ الْبِنَاءِ: الظُّرُوفُ الْمُضَافَةُ إِلَى الْجُمْلَةِ وَإِذْ وَمِثْلٌ وَغَيْرٌ، وَاسْمُ لَا الْمُكَرَّرَةِ وَأَوْجُهُهُ الْخَمْسَةُ، وَصِفَةُ اسْمِ لَا", "en": "The optional building: the adverbs annexed to a sentence, idh, mithl and ghayr; the ism of the repeated lā and its five ways; the ṣifa of lā's ism", "tr": "Câiz binâ: cümleye muzâf zarflar, iz, misl ve gayr; tekrarlanan lâ'nın ismi ve beş vechi; lâ'nın isminin sıfatı"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def fainnahu(): return tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا — ضَمِيرُ الشَّأْنِ.", "«for it»", "«çünkü»", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()])
def yajuzu(): return tok("يَجُوزُ", "jaaza", "verb", [K, IN, MR, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«it is allowed»", "«câizdir»")
def binauha(): return tok("بِنَاؤُهَا", "bina", "noun", [K, FL, ID, MSD, IRB], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«to build them»", "«mebnî olmaları»", segments=[seg("بِنَاؤُ", "bina", "noun"), pr3fs()])
def ala_fath(punct=None): return [tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"), tok("الْفَتْحِ", "fath", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَلَى.", "«fatḥa»", "«fetha»", punct=punct)]

# ----------- s1 — the adverbs annexed to a sentence, and idh
S.append({"id": "s1", "translation": {"en": "As for the optional building: the adverbs annexed to a sentence, and idh — for it is allowed to build them on fatḥa, as in His saying, exalted be He: «this is the day when the truthful will profit from their truthfulness», and «on that day»;", "tr": "Câiz binâya gelince: cümleye muzâf zarflar ve iz — bunların fetha üzere mebnî kılınması câizdir; Allah Teâlâ'nın «bu, doğruların doğruluklarının kendilerine fayda vereceği gündür» sözü ve «o gün» gibi;"},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, "amma-tafsiliyya"], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«-e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("جَائِزُ", "jaiz", "noun", [K, MK, ID, IFA], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«the optional»", "«câiz»"),
  tok("الْبِنَاءِ", "bina", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«building»", "«binâ»"),
  tok("فَالظُّرُوفُ", "zarf", "noun", [K, AT, MK, JT, MF], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَالظُّرُوفُ خَبَرٌ مَرْفُوعٌ.", "«the adverbs»", "«zarflardır»", segments=fa("الظُّرُوفُ", "zarf", "noun")),
  tok("الْمُضَافَةُ", "mudaf", "noun", [K, NA, IMF, F4, ID], "نَعْتٌ مَرْفُوعٌ.", "«annexed»", "«muzâf olan»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْجُمْلَةِ", "jumla", "noun", [K, HJ, MJ], "مَجْرُورٌ بِإِلَى — يَوْمَ وَحِينَ وَإِذَا.", "«a sentence» — yawma, ḥīna, idhā.", "«cümleye» — yevme, hîne, izâ."),
  tok("وَإِذْ", "idh", "part", [K, AT, MF], "الْوَاوُ عَاطِفَةٌ، وَإِذْ مَعْطُوفٌ عَلَى الظُّرُوفُ — لَفْظٌ مَحْكِيٌّ.", "«and idh»", "«ve iz»", segments=wa("إِذْ", "idh", "part")),
  fainnahu(),
  yajuzu(),
  binauha(),
  *ala_fath(),
  nahw(),
  tok("قَوْلِهِ", "qawl", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying»", "«O'nun sözü»", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  tok("تَعَالَى", "taala", "part", [K], "فِعْلٌ مَاضٍ لِلتَّعْظِيمِ.", "«exalted be He»", "«Teâlâ»", punct=":"),
  tok("هٰذَا", "hadha", "pron", [K, MK, ISH, IQ], "اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — ﴿الْمَائِدَة ٥: ١١٩﴾.", "«this» — al-Māʾida 5:119.", "«bu» — Mâide 5:119."),
  tok("يَوْمَ", "yawm", "noun", [K, MK, MF, ID, IQ, IRB], "خَبَرٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ لِإِضَافَتِهِ إِلَى الْجُمْلَةِ — قِرَاءَةُ نَافِعٍ؛ وَبِالضَّمِّ مُعْرَبًا فِي قِرَاءَةِ الْبَاقِينَ.", "«the day» — built on fatḥa by annexation to the clause (Nāfiʿ); the others read the ḍamma.", "«gün» — cümleye izafetle fetha üzere mebnî (Nâfi'); diğerleri damme okur."),
  tok("يَنْفَعُ", "nafaa", "verb", [K, ID, MR, MJ, IQ], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«will profit» — the clause is the muḍāf ilayh.", "«fayda verir» — cümle muzâfun ileyh."),
  tok("الصَّادِقِينَ", "sadiq", "noun", [K, MB, IFA, JDS, IQ], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِالْيَاءِ.", "«the truthful» — the object, put first.", "«doğrulara» — öne alınmış mef'ûl."),
  tok("صِدْقُهُمْ", "sidq", "noun", [K, FL, ID, MSD, IQ], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their truthfulness» — the doer.", "«doğrulukları» — fâil.", segments=[seg("صِدْقُ", "sidq", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("وَيَوْمَئِذٍ", "yawmaidhin", "noun", [K, AT, MF, ID, IRB], "الْوَاوُ عَاطِفَةٌ، وَيَوْمَئِذٍ مَعْطُوفٌ — يَوْمَ مَبْنِيٌّ عَلَى الْفَتْحِ، مُضَافٌ إِلَى إِذْ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْجُمْلَةِ.", "«and on that day» — yawma built on fatḥa, annexed to idh; the tanwīn stands for the dropped clause.", "«ve o gün» — yevme fetha üzere mebnî, iz'e muzâf; tenvin düşen cümlenin ivazı.", punct="،", segments=wa("يَوْمَئِذٍ", "yawmaidhin", "noun")),
 ]})
# ----------- s2 — mithl and ghayr
S.append({"id": "s2", "translation": {"en": "and likewise mithl and ghayr with mā, an and anna;", "tr": "mâ, en ve enne ile misl ve gayr da böyledir;"},
 "tokens": [
  tok("وَكَذٰلِكَ", "kadhalika", "part", [K, AT, MK, ISH], "الْوَاوُ عَاطِفَةٌ، وَكَذٰلِكَ خَبَرٌ مُقَدَّمٌ.", "«and likewise»", "«ve böyledir»", segments=wa("كَذٰلِكَ", "kadhalika", "part")),
  tok("مِثْلٌ", "mithl", "noun", [K, MK, IRB], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — لَفْظٌ مَحْكِيٌّ.", "«mithl»", "«misl»"),
  tok("وَغَيْرٌ", "ghayr", "noun", [K, AT, IRB], "الْوَاوُ عَاطِفَةٌ، وَغَيْرٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and ghayr»", "«ve gayr»", segments=wa("غَيْرٌ", "ghayr", "noun")),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — حَالٌ.", "«with»", "«ile»"),
  tok("مَا", "ma-masdariyya", "part", [K, ID, AMS], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ — مَا الْمَصْدَرِيَّةُ: مِثْلَ مَا فَعَلْتَ.", "«mā» — the maṣdar-mā: mithla mā faʿalta.", "«mâ» — mastar mâ'sı: misle mâ fealte."),
  tok("وَأَنْ", "an-masdariyya", "part", [K, AT, AMS], "الْوَاوُ عَاطِفَةٌ، وَأَنْ مَعْطُوفٌ — أَنِ الْمَصْدَرِيَّةُ.", "«and an»", "«ve en»", segments=wa("أَنْ", "an-masdariyya", "part")),
  tok("وَأَنَّ", "anna", "part", [K, AT, IN], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ مَعْطُوفٌ — الْمُشَدَّدَةُ: غَيْرَ أَنَّ زَيْدًا قَائِمٌ.", "«and anna» — the doubled: ghayra anna zaydan qāʾimun.", "«ve enne» — şeddeli: gayra enne Zeyden kâimün.", punct="،", segments=wa("أَنَّ", "anna", "part")),
 ]})
# ----------- s3 — the repeated lā: five ways
S.append({"id": "s3", "translation": {"en": "and the ism of the repeated lā, the single indefinite one joined to it — as in «there is no power and no strength save with God» — for it is allowed to build both on fatḥa, to put both in rafʿ, to give the first fatḥa with the second in naṣb or in rafʿ, and to put the first in rafʿ with the second on fatḥa: these five ways are allowed in its likes;", "tr": "tekrarlanan lâ'nın ona bitişik müfred nekre ismi — «Allah'tan başka ne güç ne kuvvet vardır» gibi — ikisini de fetha üzere mebnî kılmak, ikisini de ref' etmek, birinciyi fetha üzere kılıp ikinciyi nasb ya da ref' etmek ve birinciyi ref' edip ikinciyi fetha üzere kılmak câizdir: bu beş vecih benzerlerinde câizdir;"},
 "tokens": [
  tok("وَاسْمُ", "ism", "noun", [K, AT, MK, ID, LNJ], "الْوَاوُ عَاطِفَةٌ، وَاسْمُ مَعْطُوفٌ عَلَى الظُّرُوفُ مَرْفُوعٌ، مُضَافٌ.", "«and the ism of»", "«ve ismi»", segments=wa("اسْمُ", "ism", "noun")),
  tok("لَا", "la", "part", [K, ID, LNJ], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«lā»", "«lâ»"),
  tok("الْمُكَرَّرَةِ", "mukarrar", "noun", [K, NA, IMF, F2], "نَعْتٌ لِلَا مَجْرُورٌ.", "«repeated»", "«tekrarlanan»"),
  tok("الْمُتَّصِلِ", "muttasil", "noun", [K, NA, IFA, "form-viii-verbs"], "نَعْتٌ لِاسْمُ مَجْرُورٌ.", "«joined»", "«bitişik»"),
  tok("بِهَا", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — بِلَا.", "«to it»", "«ona»", segments=[seg("بِ", "bi", "prep"), pr3fs()]),
  tok("الْمُفْرَدِ", "mufrad", "noun", [K, NA, IMF, F4, LNJ], "نَعْتٌ ثَانٍ مَجْرُورٌ.", "«single»", "«müfred»"),
  tok("النَّكِرَةِ", "nakira", "noun", [K, NA, LNJ], "نَعْتٌ ثَالِثٌ مَجْرُورٌ.", "«indefinite»", "«nekre»"),
  nahw(punct=":"),
  tok("لَا", "la", "part", [K, LNJ, IQ], "لَفْظٌ مَحْكِيٌّ: لَا النَّافِيَةُ لِلْجِنْسِ — الذِّكْرُ الْمَأْثُورُ.", "«no» — lā of the genus; the well-known invocation.", "«ne» — cins lâ'sı; meşhur zikir."),
  tok("حَوْلَ", "hawl", "noun", [K, LNJ, IRB, IQ], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — الْوَجْهُ الْأَوَّلُ.", "«power» — built on fatḥa, the first way.", "«güç» — fetha üzere mebnî, birinci vecih."),
  tok("وَلَا", "la", "part", [K, AT, LNJ, IQ], "الْوَاوُ عَاطِفَةٌ، وَلَا مُكَرَّرَةٌ.", "«and no»", "«ne de»", segments=wa("لَا", "la", "part")),
  tok("قُوَّةَ", "quwwa", "noun", [K, LNJ, IRB, IQ], "اسْمُ لَا الثَّانِيَةِ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«strength» — the second lā's ism, built.", "«kuvvet» — ikinci lâ'nın ismi, mebnî."),
  tok("إِلَّا", "illa", "part", [K, MST, IQ], "أَدَاةُ اسْتِثْنَاءٍ.", "«save»", "«başka»"),
  tok("بِاللهِ", "allah", "propn", [K, HJ, MK, IQ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — خَبَرُ لَا.", "«with God» — lā's khabar.", "«Allah ile» — lâ'nın haberi.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  fainnahu(),
  yajuzu(),
  tok("بِنَاؤُهُمَا", "bina", "noun", [K, FL, ID, MSD, IRB], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«to build both»", "«ikisinin mebnî olması»", segments=[seg("بِنَاؤُ", "bina", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  *ala_fath(),
  tok("وَرَفْعُهُمَا", "raf", "noun", [K, AT, FL, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَرَفْعُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — لَا حَوْلٌ وَلَا قُوَّةٌ.", "«and rafʿ of both» — lā ḥawlun wa-lā quwwatun.", "«ve ikisinin ref'i» — lâ havlün ve lâ kuvvetün.", segments=[seg("وَ", "wa", "conj"), seg("رَفْعُ", "raf", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  tok("وَفَتْحُ", "fath", "noun", [K, AT, FL, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَفَتْحُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ.", "«and fatḥa of»", "«ve fethası»", segments=wa("فَتْحُ", "fath", "noun")),
  tok("الْأَوَّلِ", "awwal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the first»", "«birincinin»"),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("نَصْبِ", "nasb", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — لَا حَوْلَ وَلَا قُوَّةً.", "«naṣb of» — lā ḥawla wa-lā quwwatan.", "«nasbı» — lâ havle ve lâ kuvveten."),
  tok("الثَّانِي", "thani", "noun", [K, ID, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second»", "«ikincinin»"),
  tok("وَرَفْعِهِ", "raf", "noun", [K, AT, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَرَفْعِ مَعْطُوفٌ عَلَى نَصْبِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — لَا حَوْلَ وَلَا قُوَّةٌ.", "«or rafʿ of it» — lā ḥawla wa-lā quwwatun.", "«ya da ref'i» — lâ havle ve lâ kuvvetün.", segments=[seg("وَ", "wa", "conj"), seg("رَفْعِ", "raf", "noun"), pr3msi()]),
  tok("وَرَفْعُ", "raf", "noun", [K, AT, FL, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَرَفْعُ مَعْطُوفٌ عَلَى بِنَاؤُهُمَا مَرْفُوعٌ، مُضَافٌ.", "«and rafʿ of»", "«ve ref'i»", segments=wa("رَفْعُ", "raf", "noun")),
  tok("الْأَوَّلِ", "awwal", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the first»", "«birincinin»"),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("فَتْحِ", "fath", "noun", [K, ID, MSD, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — لَا حَوْلٌ وَلَا قُوَّةَ.", "«fatḥa of» — lā ḥawlun wa-lā quwwata.", "«fethası» — lâ havlün ve lâ kuvvete."),
  tok("الثَّانِي", "thani", "noun", [K, ID, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second»", "«ikincinin»"),
  tok("وَهٰذِهِ", "hadhihi", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذِهِ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and these»", "«ve bu»", segments=wa("هٰذِهِ", "hadhihi", "pron")),
  tok("خَمْسَةُ", "khamsa", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«five»", "«beş»"),
  tok("أَوْجُهٍ", "wajh", "noun", [K, ID, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ وَجْهٍ.", "«ways»", "«vecihtir»"),
  tok("تَجُوزُ", "jaaza", "verb", [K, NA, MR, HV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ نَعْتٌ.", "«are allowed»", "«câizdir»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("أَمْثَالِهِ", "mithl", "noun", [K, HJ, ID, JT], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ مِثْلٍ.", "«its likes» — every repeated lā of this shape.", "«benzerlerinde» — bu şekildeki her tekrarlanan lâ.", punct="،", segments=[seg("أَمْثَالِ", "mithl", "noun"), pr3msi()]),
 ]})
# ----------- s4 — the ṣifa of lā's built ism
S.append({"id": "s4", "translation": {"en": "and the ṣifa of the built ism of lā, the single one joined to it — for it is allowed to build it on fatḥa, as in «no man, clever», and to decline it in rafʿ and in naṣb, as in «no man, clever (ẓarīfun) / (ẓarīfan)».", "tr": "ve lâ'nın mebnî isminin ona bitişik müfred sıfatı — onu fetha üzere mebnî kılmak câizdir, «lâ racüle zarîfe» gibi; ref' ve nasb ile i'râblamak da câizdir, «lâ racüle zarîfün» ve «zarîfen» gibi."},
 "tokens": [
  tok("وَصِفَةُ", "sifa", "noun", [K, AT, MK, ID, NA], "الْوَاوُ عَاطِفَةٌ، وَصِفَةُ مَعْطُوفٌ عَلَى الظُّرُوفُ مَرْفُوعٌ، مُضَافٌ.", "«and the ṣifa of»", "«ve sıfatı»", segments=wa("صِفَةُ", "sifa", "noun")),
  tok("اسْمِ", "ism", "noun", [K, ID, LNJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the ism of»", "«isminin»"),
  tok("لَا", "la", "part", [K, ID, LNJ], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ.", "«lā»", "«lâ»"),
  tok("الْمَبْنِيِّ", "mabni", "noun", [K, NA, IMF, IRB], "نَعْتٌ لِاسْمِ مَجْرُورٌ.", "«built»", "«mebnî»"),
  tok("الْمُفْرَدَةِ", "mufrad", "noun", [K, NA, IMF, F4], "نَعْتٌ لِصِفَةُ مَرْفُوعٌ لَفْظًا — جُرَّ لِلْجِوَارِ أَوْ عَلَى تَقْدِيرِ الْإِضَافَةِ؛ هٰكَذَا فِي الطَّبْعِ.", "«single» — describing the ṣifa; the print's jarr kept.", "«müfred» — sıfatı niteler; baskının ceri korunmuş."),
  tok("الْمُتَّصِلَةِ", "muttasil", "noun", [K, NA, IFA, "form-viii-verbs"], "نَعْتٌ ثَانٍ.", "«joined»", "«bitişik»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — بِاسْمِ لَا.", "«to it» — to lā's ism.", "«ona» — lâ'nın ismine.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  fainnahu(),
  yajuzu(),
  binauha(),
  *ala_fath(),
  nahw(punct=":"),
  tok("لَا", "la", "part", [K, LNJ], "لَفْظٌ مَحْكِيٌّ: لَا النَّافِيَةُ لِلْجِنْسِ.", "«no»", "«hiç»"),
  tok("رَجُلَ", "rajul", "noun", [K, LNJ, IRB], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«man»", "«adam»"),
  tok("ظَرِيفَ", "zarif", "noun", [K, NA, IRB], "صِفَةٌ مَبْنِيَّةٌ عَلَى الْفَتْحِ مَعَ اسْمِ لَا — كَالْمُرَكَّبِ.", "«clever» — built on fatḥa with lā's ism, like a compound.", "«zarif» — lâ'nın ismiyle fetha üzere mebnî, mürekkep gibi.", punct="،"),
  tok("وَإِعْرَابُهَا", "irab", "noun", [K, AT, FL, ID, MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَإِعْرَابُ مَعْطُوفٌ عَلَى بِنَاؤُهَا مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and to decline it»", "«ve i'râblamak»", segments=[seg("وَ", "wa", "conj"), seg("إِعْرَابُ", "irab", "noun"), pr3fs()]),
  tok("رَفْعًا", "raf", "noun", [K, "hal", MSD, IRB], "حَالٌ مَنْصُوبٌ — عَلَى مَحَلِّ لَا مَعَ اسْمِهَا.", "«in rafʿ» — on the position of lā with its ism.", "«ref' ile» — lâ ile isminin mahalline göre."),
  tok("وَنَصْبًا", "nasb", "noun", [K, AT, "hal", MSD, IRB], "الْوَاوُ عَاطِفَةٌ، وَنَصْبًا مَعْطُوفٌ مَنْصُوبٌ — عَلَى مَحَلِّ اسْمِهَا.", "«and in naṣb» — on the position of its ism.", "«ve nasb ile» — isminin mahalline göre.", punct="،", segments=wa("نَصْبًا", "nasb", "noun")),
  nahw(punct=":"),
  tok("لَا", "la", "part", [K, LNJ], "لَفْظٌ مَحْكِيٌّ: لَا النَّافِيَةُ لِلْجِنْسِ.", "«no»", "«hiç»"),
  tok("رَجُلَ", "rajul", "noun", [K, LNJ, IRB], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«man»", "«adam»"),
  tok("ظَرِيفٌ", "zarif", "noun", [K, NA, IRB], "صِفَةٌ مَرْفُوعَةٌ عَلَى مَحَلِّ لَا وَاسْمِهَا.", "«clever» — rafʿ on the position of lā and its ism.", "«zarif» — lâ ve isminin mahalline göre merfû."),
  tok("وَظَرِيفًا", "zarif", "noun", [K, AT, NA, IRB], "الْوَاوُ عَاطِفَةٌ، وَظَرِيفًا مَعْطُوفٌ — صِفَةٌ مَنْصُوبَةٌ عَلَى مَحَلِّ اسْمِ لَا.", "«and clever» — naṣb on the position of lā's ism.", "«ve zarîfen» — lâ'nın isminin mahalline göre mansûb.", punct=".", segments=wa("ظَرِيفًا", "zarif", "noun")),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "zarif": G("zarif", "ظَرِيف", "ظ ر ف", "noun", "clever, witty, elegant", "zarif, nüktedan", 2, plural="ظُرَفَاء"),
}
used = set()
for s in S:
    for t in s["tokens"]:
        used.add(t["lex"])
        for sg_ in t.get("segments", []): used.add(sg_["lex"])
CAND = {}
for k in sorted(used):
    if k in TG: continue
    if k in NEW: CAND[k] = NEW[k]
    elif _ic.has_gloss(k): CAND[k] = find_gloss(k)
    else: raise SystemExit(f"no gloss anywhere for {k}")
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch66 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "nafaa", "taala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "جَائِزُ الْبِنَاءِ: الظَّرْفُ الْمُضَافُ إِلَى الْجُمْلَةِ وَإِذْ وَمِثْلٌ وَغَيْرٌ مَعَ مَا وَأَنْ وَأَنَّ، وَالْأَوْجُهُ الْخَمْسَةُ فِي لَا الْمُكَرَّرَةِ، وَصِفَةُ اسْمِ لَا بَيْنَ الْبِنَاءِ وَالْإِعْرَابِ", "en": "The optional building: the adverb annexed to a sentence, idh, mithl and ghayr with mā, an and anna; the five ways of the repeated lā; the ṣifa of lā's ism between building and declension", "tr": "Câiz binâ: cümleye muzâf zarf, iz, mâ, en ve enne ile misl ve gayr; tekrarlanan lâ'da beş vecih; binâ ile i'râb arasında lâ'nın isminin sıfatı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — جائز البناء", "الكافية لابن الحاجب — الظروف المضافة إلى الجملة، لا لنفي الجنس", "شرح قطر الندى لابن هشام — لا النافية للجنس وتوابع اسمها"],
 "amil": "the optional building: the adverbs annexed to a sentence and idh may be built on fatḥa (﴿هٰذَا يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ﴾ on Nāfiʿ's reading; يَوْمَئِذٍ); so mithl and ghayr with mā, an and anna; the single indefinite ism of a repeated lā joined to it (﴿لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ﴾) has five ways — both built, both rafʿ, first built with the second in naṣb or rafʿ, first rafʿ with the second built; the single ṣifa of lā's built ism joined to it may be built on fatḥa (لَا رَجُلَ ظَرِيفَ) or declined in rafʿ or naṣb (ظَرِيفٌ، ظَرِيفًا).",
 "question": {
  "en": ["What is the optional building? Where a word may be built or declined at will — the adverb annexed to a sentence, idh, mithl and ghayr before mā, an and anna, the ism of a repeated lā, and the ṣifa of lā's built ism.",
         "Why may the adverb annexed to a sentence be built? Annexation to a sentence, which has no iʿrāb, lets the adverb take the sentence's indeclinability: هٰذَا يَوْمَ يَنْفَعُ on fatḥa — Nāfiʿ's reading; the others read يَوْمُ in rafʿ as the khabar.",
         "What is يَوْمَئِذٍ? Yawma built on fatḥa, annexed to idh, whose clause is dropped and replaced by the tanwīn.",
         "When may mithl and ghayr be built? When annexed to mā, an or anna — مِثْلَ مَا، غَيْرَ أَنَّ — on fatḥa, like the adverb before a sentence.",
         "What are the five ways of لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ? Both built (حَوْلَ … قُوَّةَ); both rafʿ (حَوْلٌ … قُوَّةٌ); the first built with the second in naṣb (قُوَّةً) or in rafʿ (قُوَّةٌ); the first rafʿ with the second built (حَوْلٌ … قُوَّةَ) — allowed in every like phrase.",
         "How may the ṣifa of lā's built ism be read? Built on fatḥa with it, as one compound (لَا رَجُلَ ظَرِيفَ); or declined — rafʿ on the position of lā with its ism (ظَرِيفٌ), naṣb on the position of the ism (ظَرِيفًا) — if single and joined to it.",
         "What does the engine READ here? The DabtEngine reads يَوْمَ before its clause on the cited fatḥa, يَوْمَئِذٍ as built with the tanwīn of compensation, the repeated lā with حَوْلَ and قُوَّةَ built and بِاللهِ as its khabar, and ظَرِيفَ / ظَرِيفٌ / ظَرِيفًا as the three readings of the ṣifa."],
  "tr": ["Câiz binâ nedir? Kelimenin isteğe göre mebnî ya da mu'reb olabildiği yer — cümleye muzâf zarf, iz, mâ, en ve enne önünde misl ve gayr, tekrarlanan lâ'nın ismi ve lâ'nın mebnî isminin sıfatı.",
         "Cümleye muzâf zarf neden mebnî olabilir? İ'râbı olmayan cümleye izafet, zarfın cümlenin binâsını almasına izin verir: hâzâ yevme yenfeu fetha üzere — Nâfi' kıraati; diğerleri yevmü'yü haber olarak merfû okur.",
         "Yevmeizin nedir? Fetha üzere mebnî yevme, iz'e muzâf; iz'in cümlesi düşmüş, yerine tenvin gelmiş.",
         "Misl ve gayr ne zaman mebnî olabilir? Mâ, en ya da enne'ye muzâf olunca — misle mâ, gayra enne — cümle önündeki zarf gibi fetha üzere.",
         "Lâ havle ve lâ kuvvete illâ billâh'ın beş vechi nedir? İkisi mebnî (havle … kuvvete); ikisi merfû (havlün … kuvvetün); birinci mebnî, ikinci mansûb (kuvveten) ya da merfû (kuvvetün); birinci merfû, ikinci mebnî (havlün … kuvvete) — her benzer ifadede câiz.",
         "Lâ'nın mebnî isminin sıfatı nasıl okunabilir? Onunla birlikte fetha üzere mebnî, tek mürekkep gibi (lâ racüle zarîfe); ya da mu'reb — lâ ile isminin mahalline göre merfû (zarîfün), ismin mahalline göre mansûb (zarîfen) — müfred ve bitişikse.",
         "Motor burada neyi OKUR? DabtEngine cümlesi önündeki yevme'yi alıntılanan fethasıyla, yevmeizin'i ivaz tenviniyle mebnî, tekrarlanan lâ'yı havle ve kuvvete mebnî ve billâhi haberi olarak, zarîfe / zarîfün / zarîfen'i sıfatın üç okunuşu olarak okur."],
 },
 "plain": {"en": "Some words may freeze or not, as you like. A time-word before a clause, and idh, may end in a fixed -a (yawma …, yawmaʾidhin); so may mithl and ghayr before mā, an or anna. In «lā ḥawla wa-lā quwwata» each noun may end in -a or -un, five patterns in all. The adjective after lā's noun may freeze on -a or be declined.",
           "tr": "Bazı sözcükler isteğe göre donar ya da donmaz. Cümle önündeki zaman sözü ve iz sabit -a ile bitebilir (yevme …, yevmeizin); mâ, en ya da enne önünde misl ve gayr da öyle. «Lâ havle ve lâ kuvvete»de her isim -a ya da -ün ile bitebilir: beş kalıp. Lâ'nın isminden sonraki sıfat -a üzerinde donabilir ya da i'râb alır."},
 "explanation": {"en": "As for the optional building: the adverbs annexed to a sentence, and idh, may be built on fatḥa — ﴿هٰذَا يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ﴾ (al-Māʾida 5:119), cited for the fatḥa reading of Nāfiʿ that the matn illustrates, the others reading يَوْمُ with ḍamma; and يَوْمَئِذٍ. Likewise mithl and ghayr with mā, an and anna. The ism of the repeated lā, single and indefinite and joined to it — ﴿لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ﴾ — may have both built on fatḥa, both in rafʿ, the first on fatḥa with the second in naṣb or in rafʿ, or the first in rafʿ with the second on fatḥa: five ways allowed in its likes. And the ṣifa of lā's built ism, single and joined to it, may be built on fatḥa — لَا رَجُلَ ظَرِيفَ — or declined in rafʿ and in naṣb — لَا رَجُلَ ظَرِيفٌ وَظَرِيفًا. The lithograph writes the two particles as وأن وأن, given here as وَأَنْ وَأَنَّ.",
                 "tr": "Câiz binâya gelince: cümleye muzâf zarflar ve iz fetha üzere mebnî kılınabilir — hâzâ yevme yenfeu's-sâdikîne sıdkuhum (Mâide 5:119), metnin örneklediği Nâfi'in fetha kıraati için alıntılanmıştır; diğerleri yevmü'yü damme ile okur; ve yevmeizin. Mâ, en ve enne ile misl ve gayr da böyledir. Tekrarlanan lâ'nın ona bitişik müfred nekre ismi — lâ havle ve lâ kuvvete illâ billâh — ikisi fetha üzere mebnî, ikisi merfû, birinci fethalı ikinci mansûb ya da merfû, birinci merfû ikinci fethalı olabilir: benzerlerinde câiz beş vecih. Ve lâ'nın mebnî isminin ona bitişik müfred sıfatı fetha üzere mebnî olabilir — lâ racüle zarîfe — ya da ref' ve nasb ile mu'reb — lâ racüle zarîfün ve zarîfen. Litografi iki harfi وأن وأن yazar; burada ve en ve enne olarak verilir."},
 "examples": [
  {"ar": "هٰذَا يَوْمَ يَنْفَعُ الصَّادِقِينَ صِدْقُهُمْ، وَيَوْمَئِذٍ", "en": "the adverb annexed to a sentence, built on fatḥa (al-Māʾida 5:119)", "tr": "cümleye muzâf zarf, fetha üzere mebnî (Mâide 5:119)", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "مِثْلٌ وَغَيْرٌ مَعَ مَا وَأَنْ وَأَنَّ", "en": "mithl and ghayr before the maṣdar particles", "tr": "mastar harfleri önünde misl ve gayr", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "لَا حَوْلَ وَلَا قُوَّةَ إِلَّا بِاللهِ — خَمْسَةُ أَوْجُهٍ", "en": "the repeated lā and its five ways", "tr": "tekrarlanan lâ ve beş vechi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "لَا رَجُلَ ظَرِيفَ، وَلَا رَجُلَ ظَرِيفٌ وَظَرِيفًا", "en": "the ṣifa of lā's ism: built or declined", "tr": "lâ'nın isminin sıfatı: mebnî ya da mu'reb", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "يَوْمَإِذٍ (with a seated hamza)", "right": "يَوْمَئِذٍ", "why": {"en": "the hamza of idh sits on the yāʾ after the kasra-coloured joining; the tanwīn replaces the dropped clause", "tr": "iz'in hemzesi birleşmede yâ üzerine oturur; tenvin düşen cümlenin yerine geçer"}},
  {"wrong": "لَا حَوْلٍ وَلَا قُوَّةٍ", "right": "لَا حَوْلَ وَلَا قُوَّةَ (or one of the other four ways)", "why": {"en": "jarr is not among the five ways; lā's ism is built on fatḥa or raised", "tr": "cer beş vecih içinde değildir; lâ'nın ismi fetha üzere mebnî ya da merfûdur"}},
  {"wrong": "لَا رَجُلَ ظَرِيفٍ", "right": "لَا رَجُلَ ظَرِيفَ / ظَرِيفٌ / ظَرِيفًا", "why": {"en": "the ṣifa follows the building, the position of lā with its ism, or the position of the ism — never jarr", "tr": "sıfat binâya, lâ ile isminin mahalline ya da ismin mahalline uyar — asla cer almaz"}},
  {"wrong": "غَيْرُ أَنَّ زَيْدًا قَائِمٌ (only rafʿ allowed)", "right": "غَيْرَ أَنَّ … is also allowed, built on fatḥa", "why": {"en": "ghayr before anna may be built like the adverb before a sentence", "tr": "enne önünde gayr cümle önündeki zarf gibi mebnî olabilir"}},
 ],
}
ADD_EN = (" Chapter 66 (print p. 160): the optional building — the adverb annexed to a sentence and idh, al-Māʾida 5:119 on the fatḥa reading, yawmaʾidhin (s1); mithl and ghayr with mā, an and anna (s2); the repeated lā of lā ḥawla wa-lā quwwata and its five ways (s3); the ṣifa of lā's built ism, built or declined (s4).")
ADD_TR = (" Altmış altıncı bab (baskı s. 160): câiz binâ — cümleye muzâf zarf ve iz, fetha kıraatiyle Mâide 5:119, yevmeizin (s1); mâ, en ve enne ile misl ve gayr (s2); lâ havle ve lâ kuvvete'nin tekrarlanan lâ'sı ve beş vechi (s3); lâ'nın mebnî isminin sıfatı, mebnî ya da mu'reb (s4).")
write_out(66, S, TITLE, ADD_EN, ADD_TR, "p. 160", GLOSS_ADD, notes=(NOTE,),
          related=((K65, [K]), (LNJ, [K]), (MF, [K]), (IRB, [K]), (IQ, [K]), (MJ, [K])))
report(66, S, GLOSS_ADD, (NOTE,))
