# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 31: the FIFTH to NINTH marfūʿ — the ism of the bāb of كَانَ (its rule the doer's); the khabar of
# the bāb of إِنَّ (as the khabar of the mubtadaʾ, but not fronted before the ism unless an adverb: إِنَّ فِي الدَّارِ رَجُلًا); the
# khabar of لَا of genus-negation (لَا غُلَامَ رَجُلٍ عِنْدَنَا); the ism of مَا and لَا likened to لَيْسَ (its rule the mubtadaʾ's); and
# the muḍāriʿ free of the nāṣibs and jāzims (يَضْرِبُ، يَضْرِبَانِ). Print pp. 131–132.
#   python3 author_izhar_ch31.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
LNJ = "la-nafiya-lil-jins"; MLM = "ma-la-mushabbaha"; MLL = "ma-la-laysa-wa-la-al-jins"; TN = "al-fil-al-tamm-wal-naqis"; ZM = "zarf-mustaqarr-wa-laghw"
K = "al-marfuat-al-khamis-ila-al-tasi"
K29 = "khabar-al-mubtada-wa-ahkamuh"; K21 = "al-marfuat-al-fail-wa-naibuh"
TITLE = {"ar": "الْمَرْفُوعَاتُ مِنَ الْخَامِسِ إِلَى التَّاسِعِ: اسْمُ كَانَ، خَبَرُ إِنَّ، خَبَرُ لَا، اسْمُ مَا وَلَا، الْمُضَارِعُ", "en": "The fifth to ninth marfūʿāt: the ism of kāna, the khabar of inna, the khabar of lā, the ism of mā and lā, and the muḍāriʿ", "tr": "Beşinciden dokuzuncuya merfûlar: kâne'nin ismi, inne'nin haberi, lâ'nın haberi, mâ ve lâ'nın ismi, muzâri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wahukmuhu(): return tok("وَحُكْمُهُ", "hukm", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَحُكْمُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its rule»", "«ve hükmü»", segments=[seg("وَ", "wa", "conj"), seg("حُكْمُ", "hukm", "noun"), pr3ms()])
def kahukmi(): return tok("كَحُكْمِ", "hukm", "noun", [K, HJ, ID, MK], "الْكَافُ حَرْفُ جَرٍّ، وَحُكْمِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«like the rule of» — the khabar.", "«… hükmü gibi» — haber.", segments=[seg("كَ", "ka", "prep"), seg("حُكْمِ", "hukm", "noun")])
def khabari(): return tok("خَبَرِ", "khabar", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the khabar of»", "«haberinin»")
def mubtadai(punct=None): return tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtadaʾ»", "«mübtedânın»", punct=punct)
def babi(): return tok("بَابِ", "bab", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the bāb of»", "«bâbının»")

# ----------- s1 — the fifth: the ism of kāna
S.append({"id": "s1", "translation": {"en": "And the fifth is the ism of the bāb of «kāna», and its rule is the rule of the doer.", "tr": "Beşincisi kâne bâbının ismidir; hükmü fâilin hükmüdür."},
 "tokens": [
  tok("وَالْخَامِسُ", "khamis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَامِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the fifth»", "«beşincisi»", segments=wa("الْخَامِسُ", "khamis", "noun")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, KN], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the ism of» — the khabar.", "«ismi» — haber."),
  babi(),
  tok("كَانَ", "kana", "verb", [K, ID, KN, TN], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ — الْفِعْلُ النَّاقِصُ.", "«kāna» — the defective verb.", "«kâne» — nâkıs fiil.", punct="،"),
  wahukmuhu(),
  tok("حُكْمُ", "hukm", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the rule of» — the khabar.", "«hükmü» — haber."),
  tok("الْفَاعِلِ", "fail-doer", "noun", [K, ID, FL], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَرْفُوعٌ، لَا يُحْذَفُ، يَلِي عَامِلَهُ.", "«the doer» — raised, never dropped, following its governor.", "«fâil» — merfû, hazfedilmez, âmilini izler.", punct="."),
 ]})
# ----------- s2 — the sixth: the khabar of inna
S.append({"id": "s2", "translation": {"en": "And the sixth is the khabar of the bāb of «inna», and its matter is as the matter of the khabar of the mubtadaʾ,", "tr": "Altıncısı inne bâbının haberidir; durumu mübtedânın haberinin durumu gibidir,"},
 "tokens": [
  tok("وَالسَّادِسُ", "sadis", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّادِسُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sixth»", "«altıncısı»", segments=wa("السَّادِسُ", "sadis", "noun")),
  tok("خَبَرُ", "khabar", "noun", [K, MK, ID, IN], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the khabar of» — the khabar.", "«haberi» — haber."),
  babi(),
  tok("إِنَّ", "inna", "part", [K, ID, IN], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«inna»", "«inne»", punct="،"),
  tok("وَأَمْرُهُ", "amr", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَأَمْرُهُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its matter»", "«ve durumu»", segments=[seg("وَ", "wa", "conj"), seg("أَمْرُ", "amr", "noun"), pr3ms()]),
  tok("كَأَمْرِ", "amr", "noun", [K, HJ, ID, MK], "الْكَافُ حَرْفُ جَرٍّ، وَأَمْرِ مَجْرُورٌ، مُضَافٌ — خَبَرٌ.", "«as the matter of» — the khabar.", "«… durumu gibi» — haber.", segments=[seg("كَ", "ka", "prep"), seg("أَمْرِ", "amr", "noun")]),
  khabari(),
  mubtadai("،"),
 ]})
# ----------- s3 — but not fronted before the ism, unless an adverb
S.append({"id": "s3", "translation": {"en": "but its fronting before her ism is not allowed, unless it is an adverb — as in «surely in the house is a man».", "tr": "fakat isminin önüne alınması câiz değildir; zarf olması müstesnâ — «muhakkak evde bir adam vardır» gibi."},
 "tokens": [
  tok("لٰكِنْ", "lakin", "part", [K, AT], "حَرْفُ اسْتِدْرَاكٍ.", "«but»", "«fakat»"),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«değildir»"),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, MR, LN], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«it is allowed»", "«câiz»"),
  tok("تَقْدِيمُهُ", "taqdim", "noun", [K, FL, ID, MSD, F2], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْخَبَرُ.", "«its fronting» — the doer.", "«öne alınması» — fâil.", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("اسْمِهَا", "ism", "noun", [K, HJ, ID, IN], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — اسْمُ إِنَّ.", "«her ism» — the ism of inna.", "«isminin» — inne'nin ismi.", segments=[seg("اسْمِ", "ism", "noun"), pr3fs()]),
  tok("إِلَّا", "illa", "part", [K, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«unless»", "«ancak … müstesnâ»"),
  tok("أَنْ", "an-masdariyya", "part", [K, AMS, "istithna"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ مُسْتَثْنًى.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", [K, KN, AMS, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — الْخَبَرُ.", "«it be» — the khabar.", "«olması» — haber."),
  tok("ظَرْفًا", "zarf", "noun", [K, KN, MF, ZM], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«an adverb»", "«zarf»", punct="،"),
  nahw(),
  tok("إِنَّ", "inna", "part", [K, IN], "لَفْظٌ مَحْكِيٌّ: حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«surely»", "«muhakkak»"),
  tok("فِي", "fi", "prep", [K, HJ, IN, ZM], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ مُقَدَّمٌ.", "«in» — the prepositional phrase as fronted khabar.", "«-de» — câr-mecrûr öne alınmış haber."),
  tok("الدَّارِ", "dar", "noun", [K, HJ, IN], "مَجْرُورٌ بِفِي.", "«the house»", "«ev»"),
  tok("رَجُلًا", "rajul", "noun", [K, IN], "اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ.", "«a man» — the delayed ism of inna.", "«bir adam» — inne'nin sona alınmış ismi.", punct="."),
 ]})
# ----------- s4 — the seventh: the khabar of lā of genus-negation
S.append({"id": "s4", "translation": {"en": "And the seventh is the khabar of «lā» for the negation of the genus, and its rule too is like the rule of the khabar of the mubtadaʾ — as in «no servant of a man is with us».", "tr": "Yedincisi cins nefyi için olan lâ'nın haberidir; hükmü de mübtedânın haberinin hükmü gibidir — «bizde hiçbir adamın kölesi yoktur» gibi."},
 "tokens": [
  tok("وَالسَّابِعُ", "sabi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّابِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the seventh»", "«yedincisi»", segments=wa("السَّابِعُ", "sabi", "noun")),
  tok("خَبَرُ", "khabar", "noun", [K, MK, ID, LNJ], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the khabar of» — the khabar.", "«haberi» — haber."),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, ID, LNJ], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«lā»", "«lâ'nın»"),
  tok("لِنَفْيِ", "nafy", "noun", [K, HJ, ID, MSD], "اللَّامُ حَرْفُ جَرٍّ، وَنَفْيِ مَجْرُورٌ، مُضَافٌ.", "«for the negation of»", "«nefyi için»", segments=[seg("لِ", "li", "prep"), seg("نَفْيِ", "nafy", "noun")]),
  tok("الْجِنْسِ", "jins", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the genus»", "«cins»", punct="،"),
  wahukmuhu(),
  tok("أَيْضًا", "aydan", "noun", [K, "maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ.", "«too»", "«de»"),
  kahukmi(),
  khabari(),
  mubtadai("،"),
  nahw(),
  tok("لَا", "la-nafiya-lil-jins", "part", [K, LNJ], "لَفْظٌ مَحْكِيٌّ: نَافِيَةٌ لِلْجِنْسِ.", "«no»", "«hiçbir … yok»"),
  tok("غُلَامَ", "ghulam", "noun", [K, LNJ, ID], "اسْمُ لَا مَنْصُوبٌ لِأَنَّهُ مُضَافٌ.", "«servant of» — the ism of lā, naṣb because annexed.", "«kölesi» — lâ'nın ismi; muzâf olduğundan mansûb."),
  tok("رَجُلٍ", "rajul", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a man»", "«bir adamın»"),
  tok("عِنْدَنَا", "inda", "noun", [K, MF, ID, LNJ, ZM], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — خَبَرُ لَا.", "«with us» — the khabar of lā.", "«bizde» — lâ'nın haberi.", punct=".", segments=[seg("عِنْدَ", "inda", "noun"), seg("نَا", "pron-1p", "pron")]),
 ]})
# ----------- s5 — the eighth: the ism of mā and lā likened to laysa
S.append({"id": "s5", "translation": {"en": "And the eighth is the ism of «mā» and «lā» likened to «laysa», and its rule is like the rule of the mubtadaʾ.", "tr": "Sekizincisi leyse'ye benzetilen mâ ve lâ'nın ismidir; hükmü mübtedânın hükmü gibidir."},
 "tokens": [
  tok("وَالثَّامِنُ", "thamin-eighth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّامِنُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the eighth»", "«sekizincisi»", segments=wa("الثَّامِنُ", "thamin-eighth", "noun")),
  tok("اسْمُ", "ism", "noun", [K, MK, ID, MLM], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the ism of» — the khabar.", "«ismi» — haber."),
  tok("مَا", "ma-hijaziyya", "part", [K, ID, MLM, MLL], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ — مَا الْحِجَازِيَّةُ.", "«mā» — the Ḥijāzī mā.", "«mâ» — Hicâz mâ'sı."),
  tok("وَلَا", "la-nafiya", "part", [K, AT, MLM], "الْوَاوُ عَاطِفَةٌ، وَلَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and lā»", "«ve lâ»", segments=wa("لَا", "la-nafiya", "part")),
  tok("الْمُشَبَّهَتَيْنِ", "mushabbah", "noun", [K, NA, MTH, IMF, F2], "نَعْتٌ لِمَا وَلَا مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«the two likened» — a dual qualifier.", "«benzetilen ikisi» — tesniye sıfat."),
  tok("بِلَيْسَ", "laysa", "verb", [K, HJ, TN], "الْبَاءُ حَرْفُ جَرٍّ، وَلَيْسَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«to laysa»", "«leyse'ye»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("لَيْسَ", "laysa", "verb")]),
  wahukmuhu(),
  kahukmi(),
  mubtadai("."),
 ]})
# ----------- s6 — the ninth: the muḍāriʿ free of nāṣib and jāzim
S.append({"id": "s6", "translation": {"en": "And the ninth is the muḍāriʿ free of the nāṣibs and the jāzims — as in «he strikes» and «they two strike».", "tr": "Dokuzuncusu nâsıb ve câzimlerden hâlî olan muzâridir — «vurur» ve «o ikisi vurur» gibi."},
 "tokens": [
  tok("وَالتَّاسِعُ", "tasi", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالتَّاسِعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the ninth»", "«dokuzuncusu»", segments=wa("التَّاسِعُ", "tasi", "noun")),
  tok("الْمُضَارِعُ", "mudari", "noun", [K, MK, MR], "خَبَرٌ مَرْفُوعٌ.", "«the muḍāriʿ» — the khabar.", "«muzâri» — haber."),
  tok("الْخَالِي", "khali", "noun", [K, NA, IFA, MQ], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«free» — a manqūṣ qualifier.", "«hâlî» — mankûs sıfat."),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«of»", "«-den»"),
  tok("النَّوَاصِبِ", "nasib", "noun", [K, HJ, JT, JZ], "مَجْرُورٌ بِعَنْ.", "«the nāṣibs»", "«nâsıblar»"),
  tok("وَالْجَوَازِمِ", "jazim", "noun", [K, AT, JT, JZ], "الْوَاوُ عَاطِفَةٌ، وَالْجَوَازِمِ مَعْطُوفٌ مَجْرُورٌ.", "«and the jāzims»", "«ve câzimler»", punct="،", segments=wa("الْجَوَازِمِ", "jazim", "noun")),
  nahw(),
  tok("يَضْرِبُ", "daraba", "verb", [K, MR, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ لِتَجَرُّدِهِ.", "«he strikes» — raised by the ḍamma.", "«vurur» — damme ile merfû."),
  tok("وَيَضْرِبَانِ", "daraba", "verb", [K, AT, MR, FL, MTH, "afal-khamsa"], "الْوَاوُ عَاطِفَةٌ، وَيَضْرِبَانِ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ.", "«and they two strike» — raised by the nūn's standing.", "«ve o ikisi vurur» — nûnun sübûtuyla merfû.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("يَضْرِبَ", "daraba", "verb"), seg("انِ", "pron-3d", "pron")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {}
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
print("izhar ch31 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("jaaza", "kana", "daraba", "laysa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَرْفُوعَاتُ الْخَامِسُ إِلَى التَّاسِعِ: اسْمُ كَانَ، خَبَرُ إِنَّ، خَبَرُ لَا، اسْمُ مَا وَلَا، وَالْمُضَارِعُ الْمُجَرَّدُ", "en": "The fifth to ninth marfūʿāt: the ism of kāna, the khabar of inna, the khabar of lā, the ism of mā and lā, and the bare muḍāriʿ", "tr": "Beşinciden dokuzuncuya merfûlar: kâne'nin ismi, inne'nin haberi, lâ'nın haberi, mâ ve lâ'nın ismi ve mücerred muzâri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المرفوعات التسعة", "الكافية لابن الحاجب — المرفوعات", "شرح قطر الندى لابن هشام — النواسخ"],
 "amil": "the nine marfūʿāt close: the fifth is the ism of the bāb of كَانَ, ruled as the doer; the sixth the khabar of the bāb of إِنَّ, ruled as the khabar of the mubtadaʾ save that it may not stand before the ism unless an adverb (إِنَّ فِي الدَّارِ رَجُلًا); the seventh the khabar of لَا of genus-negation, ruled as the mubtadaʾ's khabar (لَا غُلَامَ رَجُلٍ عِنْدَنَا); the eighth the ism of مَا and لَا likened to لَيْسَ, ruled as the mubtadaʾ; the ninth the muḍāriʿ free of the nāṣibs and jāzims (يَضْرِبُ، يَضْرِبَانِ)",
 "question": {
  "en": ["What is the fifth marfūʿ? The ism of the bāb of كَانَ — and its rule is the doer's: raised after its governor, never dropped, the verb agreeing with it in gender.",
         "What is the sixth? The khabar of the bāb of إِنَّ, whose matter is that of the khabar of the mubtadaʾ — single or multiplied, word or sentence — except that it may not be fronted before her ism unless it is an adverb: إِنَّ فِي الدَّارِ رَجُلًا.",
         "What is the seventh? The khabar of لَا of genus-negation, ruled as the khabar of the mubtadaʾ: لَا غُلَامَ رَجُلٍ عِنْدَنَا — the ism annexed takes naṣb, the khabar عِنْدَنَا is an adverb standing for a raised khabar.",
         "What is the eighth? The ism of مَا and لَا likened to لَيْسَ — the Ḥijāzī مَا and the لَا that negates one thing — ruled as the mubtadaʾ: raised, usually definite or specified.",
         "What is the ninth? The muḍāriʿ free of the nāṣibs and the jāzims: يَضْرِبُ by the ḍamma, يَضْرِبَانِ by the standing of the nūn — raised by the absence of a governor, the maʿnawī governor of the muḍāriʿ.",
         "What does the engine READ here? The DabtEngine raises the noun after the ordinal as its khabar, keeps the quoted particles (كَانَ، إِنَّ، لَا، مَا، لَيْسَ) at the author's form, reads فِي الدَّارِ رَجُلًا after إِنَّ as a fronted adverbial khabar with a delayed naṣb ism, reads the ism of لَا as annexed naṣb with the adverb عِنْدَنَا as khabar, and raises the bare muḍāriʿ يَضْرِبُ and the dual يَضْرِبَانِ with their proper signs."],
  "tr": ["Beşinci merfû nedir? Kâne bâbının ismi — hükmü fâilin hükmüdür: âmilinden sonra merfû, hazfedilmez, fiil ona cinsiyette uyar.",
         "Altıncısı? İnne bâbının haberi; durumu mübtedânın haberinin durumu gibidir — tek veya taaddüd, kelime veya cümle — fakat zarf olmadıkça isminin önüne alınamaz: inne fi'd-dâri racülen.",
         "Yedincisi? Cins nefyi için olan lâ'nın haberi; hükmü mübtedânın haberinin hükmü gibidir: lâ gulâme racülin indenâ — muzâf ism mansûb, haber indenâ merfû bir haberin yerindeki zarf.",
         "Sekizincisi? Leyse'ye benzetilen mâ ve lâ'nın ismi — Hicâz mâ'sı ve tek şeyi nefyeden lâ — hükmü mübtedânın hükmü gibidir: merfû, çoğunlukla ma'rife veya tahsîs edilmiş.",
         "Dokuzuncusu? Nâsıb ve câzimlerden hâlî muzâri: yadribu damme ile, yadribâni nûnun sübûtuyla — âmilin yokluğuyla merfû: muzârinin ma'nevî âmili.",
         "Motor burada neyi OKUR? DabtEngine sıra sayısından sonraki ismi haber olarak ref' eder; alıntılanan edatları (kâne, inne, lâ, mâ, leyse) yazarın şeklinde tutar; inne'den sonraki fi'd-dâri racülen'i sona alınmış mansûb ismli öne alınmış zarf haber okur; lâ'nın ismini muzâf mansûb, indenâ zarfını haber okur; mücerred muzâri yadribu ile tesniye yadribâni'yi alâmetleriyle ref' eder."],
 },
 "plain": {"en": "Five more raised words close the list: the subject of «kāna» (like a doer), the predicate of «inna» (like a normal predicate, but not before the subject unless it is a place phrase), the predicate of «no» denying a whole kind, the subject of «mā» and «lā» used like «laysa», and the present-tense verb with no governor.",
           "tr": "Merfûlar listesi beş tane daha ile biter: kâne'nin öznesi (fâil gibi), inne'nin yüklemi (normal yüklem gibi, ama zarf değilse öznenin önüne geçemez), bütün bir cinsi yok sayan lâ'nın yüklemi, leyse gibi kullanılan mâ ve lâ'nın öznesi ve üzerinde âmil olmayan muzâri fiil."},
 "explanation": {"en": "The fifth marfūʿ is the ism of the bāb of كَانَ; its rule is the doer's: raised, never dropped, following its governor. The sixth is the khabar of the bāb of إِنَّ; its matter is that of the khabar of the mubtadaʾ — it may be multiplied, be a sentence with a returner, be definite or indefinite — except that it may not be fronted before her ism unless it is an adverb (إِنَّ فِي الدَّارِ رَجُلًا). The seventh is the khabar of لَا for the negation of the genus, ruled too as the khabar of the mubtadaʾ (لَا غُلَامَ رَجُلٍ عِنْدَنَا — the annexed ism in naṣb, the adverb as khabar). The eighth is the ism of مَا and لَا likened to لَيْسَ, ruled as the mubtadaʾ. The ninth is the muḍāriʿ free of the nāṣibs and the jāzims (يَضْرِبُ، يَضْرِبَانِ), raised by the ḍamma or the standing of the nūn. With these the nine marfūʿāt of the governed word are complete, and the thirteen manṣūbāt follow.",
                 "tr": "Beşinci merfû kâne bâbının ismidir; hükmü fâilin hükmüdür: merfû, hazfedilmez, âmilini izler. Altıncısı inne bâbının haberidir; durumu mübtedânın haberinin durumu gibidir — taaddüd edebilir, âidli cümle olabilir, ma'rife veya nekre olabilir — fakat zarf olmadıkça isminin önüne alınamaz (inne fi'd-dâri racülen). Yedincisi cins nefyi için olan lâ'nın haberidir; o da mübtedânın haberi gibidir (lâ gulâme racülin indenâ — muzâf ism mansûb, zarf haber). Sekizincisi leyse'ye benzetilen mâ ve lâ'nın ismidir; hükmü mübtedânın hükmüdür. Dokuzuncusu nâsıb ve câzimlerden hâlî muzâridir (yadribu, yadribâni); damme veya nûnun sübûtuyla merfûdur. Böylece ma'mûlün dokuz merfûsu tamamlanır; on üç mansûb bunu izler."},
 "examples": [
  {"ar": "اسْمُ بَابِ كَانَ، وَحُكْمُهُ حُكْمُ الْفَاعِلِ", "en": "the fifth: the ism of kāna", "tr": "beşinci: kâne'nin ismi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "إِنَّ فِي الدَّارِ رَجُلًا", "en": "the sixth: the adverbial khabar of inna fronted", "tr": "altıncı: inne'nin öne alınmış zarf haberi", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "لَا غُلَامَ رَجُلٍ عِنْدَنَا", "en": "the seventh: the khabar of lā of genus-negation", "tr": "yedinci: cins nefyi lâ'sının haberi", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "اسْمُ مَا وَلَا الْمُشَبَّهَتَيْنِ بِلَيْسَ", "en": "the eighth: the ism of mā and lā likened to laysa", "tr": "sekizinci: leyse'ye benzeyen mâ ve lâ'nın ismi", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "يَضْرِبُ وَيَضْرِبَانِ", "en": "the ninth: the bare muḍāriʿ", "tr": "dokuzuncu: mücerred muzâri", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "إِنَّ قَائِمٌ زَيْدًا", "right": "إِنَّ زَيْدًا قَائِمٌ", "why": {"en": "the khabar of inna may not be fronted before the ism unless it is an adverb", "tr": "inne'nin haberi zarf olmadıkça isminin önüne alınamaz"}},
  {"wrong": "لَا غُلَامُ رَجُلٍ عِنْدَنَا", "right": "لَا غُلَامَ رَجُلٍ عِنْدَنَا", "why": {"en": "the annexed ism of lā of genus-negation takes naṣb; only the khabar is raised", "tr": "cins nefyi lâ'sının muzâf ismi mansûbdur; yalnız haberi merfûdur"}},
  {"wrong": "يَضْرِبَ (with no nāṣib before it)", "right": "يَضْرِبُ", "why": {"en": "the muḍāriʿ free of nāṣib and jāzim is raised — the ninth marfūʿ", "tr": "nâsıb ve câzimden hâlî muzâri merfûdur — dokuzuncu merfû"}},
 ],
}
ADD_EN = (" Chapter 31 (print pp. 131-132): the fifth to ninth marfūʿāt — the ism of kāna (s1), the khabar of inna (s2) and its adverbial fronting (s3), the khabar of lā of genus-negation (s4), the ism of mā and lā likened to laysa (s5), the bare muḍāriʿ (s6).")
ADD_TR = (" Otuz birinci bab (baskı s. 131-132): beşinciden dokuzuncuya merfûlar — kâne'nin ismi (s1), inne'nin haberi (s2) ve zarf olarak öne alınması (s3), cins nefyi lâ'sının haberi (s4), leyse'ye benzeyen mâ ve lâ'nın ismi (s5), mücerred muzâri (s6).")
write_out(31, S, TITLE, ADD_EN, ADD_TR, "pp. 131-132", GLOSS_ADD, notes=(NOTE,),
          related=((K29, [K]), (K21, [K]), (KN, [K]), (IN, [K]), (LNJ, [K]), (MLM, [K]), (MR, [K])))
report(31, S, GLOSS_ADD, (NOTE,))
