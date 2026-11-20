# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 38: the EIGHTH manṣūb, the mustathnā — two kinds: connected (what is taken out of a plurality by إِلَّا or
# one of its sisters) and disconnected (what is mentioned after them without being taken out); the mustathnā takes naṣb after إِلَّا, the
# non-adjectival one, in complete affirmative speech (جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا), or fronted before the mustathnā minhu (مَا جَاءَنِي إِلَّا
# زَيْدًا أَحَدٌ), or disconnected (جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ), or after خَلَا، عَدَا mostly, مَا خَلَا، مَا عَدَا، لَيْسَ، لَا يَكُونُ. Print pp. 135–136.
#   python3 author_izhar_ch38.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TF2 = "ism-tafdil"; IS = "istithna"; ISM = "istithna-mufarragh"; TN = "al-fil-al-tamm-wal-naqis"
K = "al-mustathna-wa-nawah-wa-nasbuh"
K37 = "al-tamyiz-wa-ahkamuh"
TITLE = {"ar": "الْمَنْصُوبُ الثَّامِنُ: الْمُسْتَثْنَى، نَوْعَاهُ وَمَوَاضِعُ نَصْبِهِ", "en": "The eighth manṣūb: the mustathnā, its two kinds and the places of its naṣb", "tr": "Sekizinci mansûb: müstesnâ, iki nev'i ve nasb yerleri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def aw(): return tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»")
def jaani(gr=None): return tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV] + (gr or [IS]), "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s", "pron")])
def alqawmu(): return tok("الْقَوْمُ", "qawm", "noun", [K, FL, IS], "فَاعِلٌ مَرْفُوعٌ — الْمُسْتَثْنَى مِنْهُ.", "«the people» — the mustathnā minhu.", "«kavim» — müstesnâ minh.")
def illa(gr=None): return tok("إِلَّا", "illa", "part", [K] + (gr or [IS]), "أَدَاةُ اسْتِثْنَاءٍ.", "«except»", "«hariç»")
def an_mutaaddid(gr): return [tok("عَنْ", "an", "prep", [K, HJ] + gr, "حَرْفُ جَرٍّ.", "«out of»", "«-dan»"), tok("مُتَعَدِّدٍ", "mutaaddid", "noun", [K, HJ, IFA, F5] + gr, "مَجْرُورٌ بِعَنْ — جَمْعٌ أَوْ مَا فِي حُكْمِهِ.", "«a plurality»", "«bir çokluktan»")]

# ----------- s1 — the eighth: two kinds; the connected
S.append({"id": "s1", "translation": {"en": "And the eighth is the mustathnā, and it is of two kinds: connected — and that is what is taken out of a plurality by «except» or one of its sisters —", "tr": "Sekizincisi müstesnâdır; iki nev'dir: muttasıl — illâ veya kardeşlerinden biriyle bir çokluktan çıkarılan —"},
 "tokens": [
  tok("وَالثَّامِنُ", "thamin-eighth", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّامِنُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the eighth»", "«sekizincisi»", segments=wa("الثَّامِنُ", "thamin-eighth", "noun")),
  tok("الْمُسْتَثْنَى", "mustathna", "noun", [K, MK, IS, MQ, IMF], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the mustathnā» — the khabar.", "«müstesnâ» — haber.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("نَوْعَانِ", "naw", "noun", [K, MK, MTH], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two kinds»", "«iki nev'»", punct=":"),
  tok("مُتَّصِلٌ", "muttasil", "noun", [K, MK, IS, IFA, "form-viii-verbs"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: أَحَدُهُمَا مُتَّصِلٌ.", "«connected»", "«muttasıl»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمُخْرَجُ", "mukhraj", "noun", [K, MK, IMF, F4, IS], "خَبَرٌ مَرْفُوعٌ.", "«what is taken out» — the khabar.", "«çıkarılan» — haber."),
  *an_mutaaddid([IS]),
  tok("بِإِلَّا", "illa", "part", [K, HJ, IS], "الْبَاءُ حَرْفُ جَرٍّ، وَإِلَّا لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«by except»", "«illâ ile»", segments=[seg("بِ", "bi", "prep"), seg("إِلَّا", "illa", "part")]),
  aw(),
  tok("إِحْدَى", "ihda", "noun", [K, AT, ID, MQ], "مَعْطُوفٌ عَلَى إِلَّا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«one of»", "«biri»"),
  tok("أَخَوَاتِهَا", "ukht", "noun", [K, ID, "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — غَيْرٌ وَسِوًى وَخَلَا وَعَدَا وَحَاشَا.", "«its sisters» — ghayr, siwā, khalā, ʿadā, ḥāshā.", "«kardeşlerinden» — gayr, sivâ, halâ, adâ, hâşâ.", punct="،", segments=[seg("أَخَوَاتِ", "ukht", "noun"), pr3fs()]),
 ]})
# ----------- s2 — the disconnected
S.append({"id": "s2", "translation": {"en": "and disconnected — and that is what is mentioned after them without being taken out of a plurality;", "tr": "ve munkatı' — bunlardan sonra bir çokluktan çıkarılmaksızın zikredilen;"},
 "tokens": [
  tok("وَمُنْقَطِعٌ", "munqati", "noun", [K, AT, MK, IS, IFA, "form-vii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمُنْقَطِعٌ مَعْطُوفٌ عَلَى مُتَّصِلٌ مَرْفُوعٌ.", "«and disconnected»", "«ve munkatı'»", punct="،", segments=wa("مُنْقَطِعٌ", "munqati", "noun")),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and that is»", "«o da»", segments=wa("هُوَ", "huwa", "pron")),
  tok("الْمَذْكُورُ", "madhkur", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«what is mentioned» — the khabar.", "«zikredilen» — haber."),
  tok("بَعْدَهَا", "bada", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — بَعْدَ إِلَّا وَأَخَوَاتِهَا.", "«after them» — after illā and its sisters.", "«bunlardan sonra»", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  tok("غَيْرَ", "ghayr", "noun", [K, "hal", ID], "حَالٌ مَنْصُوبٌ، مُضَافٌ.", "«without being»", "«olmaksızın»"),
  tok("مُخْرَجٍ", "mukhraj", "noun", [K, ID, IMF, F4], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«taken out»", "«çıkarılmış»"),
  *an_mutaaddid([]),
 ]})
# ----------- s3 — naṣb after illā in complete affirmative speech
S.append({"id": "s3", "translation": {"en": "and the mustathnā is manṣūb when it is after «except» — the non-adjectival one — in complete affirmative speech, as in «the people came to me except Zayd»;", "tr": "müstesnâ, sıfat olmayan illâ'dan sonra tam ve müsbet sözde gelirse mansûbdur — «kavim bana geldi, Zeyd hariç» gibi;"},
 "tokens": [
  tok("وَالْمُسْتَثْنَى", "mustathna", "noun", [K, AT, MK, IS, MQ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُسْتَثْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the mustathnā»", "«ve müstesnâ»", segments=wa("الْمُسْتَثْنَى", "mustathna", "noun")),
  tok("مَنْصُوبٌ", "mansub", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«manṣūb» — the khabar.", "«mansûbdur» — haber."),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-ince»"),
  tok("كَانَ", "kana", "verb", [K, KN, HV, "idha-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is»", "«olursa»"),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID, KN], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — خَبَرُ كَانَ.", "«after» — the khabar of kāna.", "«sonra» — kâne'nin haberi."),
  tok("إِلَّا", "illa", "part", [K, ID, IS], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«except»", "«illâ»"),
  tok("غَيْرِ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ لِإِلَّا مَجْرُورٌ، مُضَافٌ.", "«not»", "«olmayan»"),
  tok("الصِّفَةِ", "sifa", "noun", [K, ID, NA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — إِلَّا الْوَصْفِيَّةُ بِمَعْنَى غَيْرٍ.", "«the adjectival» — illā in the sense of ghayr.", "«sıfat olan» — gayr mânâsındaki illâ."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("كَلَامٍ", "kalam", "noun", [K, HJ], "مَجْرُورٌ بِفِي.", "«speech»", "«sözde»"),
  tok("مُوجَبٍ", "mujib", "noun", [K, NA, IMF, F4], "نَعْتٌ مَجْرُورٌ — غَيْرِ مَنْفِيٍّ.", "«affirmative» — not negated.", "«müsbet» — menfî olmayan."),
  tok("تَامٍّ", "tamm", "noun", [K, NA, IS], "نَعْتٌ ثَانٍ مَجْرُورٌ — الْمُسْتَثْنَى مِنْهُ مَذْكُورٌ.", "«complete» — the mustathnā minhu mentioned.", "«tam» — müstesnâ minh zikredilmiş.", punct="،"),
  nahw(), jaani(), alqawmu(), illa(),
  tok("زَيْدًا", "zayd", "propn", [K, IS], "مُسْتَثْنًى مَنْصُوبٌ.", "«Zayd» — the mustathnā.", "«Zeyd» — müstesnâ.", punct="،"),
 ]})
# ----------- s4 — fronted before the mustathnā minhu
S.append({"id": "s4", "translation": {"en": "or fronted before the mustathnā minhu — as in «there came to me, except Zayd, no one» —", "tr": "ya da müstesnâ minhin önüne alınmış — «bana, Zeyd hariç, kimse gelmedi» gibi —"},
 "tokens": [
  aw(),
  tok("مُقَدَّمًا", "muqaddam", "noun", [K, AT, KN, IMF, F2], "مَعْطُوفٌ عَلَى خَبَرِ كَانَ مَنْصُوبٌ.", "«fronted»", "«öne alınmış»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«before»", "«önüne»"),
  tok("الْمُسْتَثْنَى", "mustathna", "noun", [K, HJ, IS, MQ], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the mustathnā»", "«müstesnâ»"),
  tok("مِنْهُ", "min", "prep", [K, HJ, IS], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — جُزْءُ الِاسْمِ.", "«minhu» — part of the term.", "«minh» — terimin parçası.", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  nahw(),
  tok("مَا", "ma-nafiya", "part", [K, LN, IS], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نَفْيٍ.", "«not»", "«-medi»"),
  jaani(), illa(),
  tok("زَيْدًا", "zayd", "propn", [K, IS], "مُسْتَثْنًى مُقَدَّمٌ مَنْصُوبٌ.", "«Zayd» — the fronted mustathnā.", "«Zeyd» — öne alınmış müstesnâ."),
  tok("أَحَدٌ", "ahad", "noun", [K, FL, IS], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ — الْمُسْتَثْنَى مِنْهُ.", "«no one» — the delayed doer, the mustathnā minhu.", "«kimse» — sona alınmış fâil, müstesnâ minh.", punct="،"),
 ]})
# ----------- s5 — disconnected
S.append({"id": "s5", "translation": {"en": "or disconnected — as in «the people came to me, except the donkey» —", "tr": "ya da munkatı' — «kavim bana geldi, eşek hariç» gibi —"},
 "tokens": [
  aw(),
  tok("مُنْقَطِعًا", "munqati", "noun", [K, AT, KN, IFA, IS], "مَعْطُوفٌ مَنْصُوبٌ.", "«disconnected»", "«munkatı'»", punct="،"),
  nahw(), jaani(), alqawmu(), illa(),
  tok("الْحِمَارَ", "himar", "noun", [K, IS], "مُسْتَثْنًى مُنْقَطِعٌ مَنْصُوبٌ — لَيْسَ مِنَ الْقَوْمِ.", "«the donkey» — the disconnected mustathnā, no one of the people.", "«eşek» — munkatı' müstesnâ; kavimden değil.", punct="،"),
 ]})
# ----------- s6 — after khalā, ʿadā, mā khalā, mā ʿadā, laysa, lā yakūnu
S.append({"id": "s6", "translation": {"en": "or when it is after «khalā» or «ʿadā» in most cases, or «mā khalā», or «mā ʿadā», or «laysa», or «lā yakūnu».", "tr": "ya da çoğunlukla halâ veya adâ'dan, yahut mâ halâ, mâ adâ, leyse veya lâ yekûnu'dan sonra gelirse."},
 "tokens": [
  aw(),
  tok("كَانَ", "kana", "verb", [K, AT, KN, HV], "فِعْلٌ مَاضٍ نَاقِصٌ مَعْطُوفٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it is»", "«olursa»"),
  tok("بَعْدَ", "bada", "noun", [K, MF, ID, KN], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — خَبَرُ كَانَ.", "«after»", "«sonra»"),
  tok("خَلَا", "khala-except", "part", [K, ID, IS], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — فِعْلٌ أَوْ حَرْفٌ لِلِاسْتِثْنَاءِ.", "«khalā»", "«halâ»"),
  aw(),
  tok("عَدَا", "ada-except", "part", [K, AT, IS], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«ʿadā»", "«adâ»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْأَكْثَرِ", "akthar", "noun", [K, HJ, TF2], "مَجْرُورٌ بِفِي — وَيُجَرُّ بَعْدَهُمَا فِي الْأَقَلِّ.", "«most cases» — jarr after them in the fewer.", "«çoğunlukla» — azı mecrûr olur.", punct="،"),
  aw(),
  tok("مَا", "ma-masdariyya", "part", [K, AT, IS], "لَفْظٌ مَحْكِيٌّ: مَا الْمَصْدَرِيَّةُ.", "«mā»", "«mâ»"),
  tok("خَلَا", "khala-except", "part", [K, IS], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ.", "«khalā»", "«halâ»", punct="،"),
  aw(),
  tok("مَا", "ma-masdariyya", "part", [K, AT, IS], "لَفْظٌ مَحْكِيٌّ: مَا الْمَصْدَرِيَّةُ.", "«mā»", "«mâ»"),
  tok("عَدَا", "ada-except", "part", [K, IS], "فِعْلٌ مَاضٍ لِلِاسْتِثْنَاءِ.", "«ʿadā»", "«adâ»", punct="،"),
  aw(),
  tok("لَيْسَ", "laysa", "verb", [K, AT, IS, TN], "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — لِلِاسْتِثْنَاءِ.", "«laysa»", "«leyse»", punct="،"),
  aw(),
  tok("لَا", "la-nafiya", "part", [K, AT, LN, IS], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نَفْيٍ.", "«lā»", "«lâ»"),
  tok("يَكُونُ", "kana", "verb", [K, KN, HV, MR, IS], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ — لِلِاسْتِثْنَاءِ.", "«yakūnu»", "«yekûnu»", punct="."),
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
print("izhar ch38 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("kana", "jaa", "laysa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُسْتَثْنَى: الْمُتَّصِلُ وَالْمُنْقَطِعُ، وَمَوَاضِعُ نَصْبِهِ", "en": "The mustathnā: connected and disconnected, and the places of its naṣb", "tr": "Müstesnâ: muttasıl ve munkatı', nasb yerleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المنصوبات: المستثنى", "الكافية لابن الحاجب — المستثنى", "شرح قطر الندى لابن هشام — الاستثناء"],
 "amil": "the eighth manṣūb is the mustathnā: connected (taken out of a plurality by إِلَّا or a sister: جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا) or disconnected (mentioned after them without being one of the plurality: جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ); it takes naṣb after the non-adjectival إِلَّا in complete affirmative speech, when fronted before the mustathnā minhu (مَا جَاءَنِي إِلَّا زَيْدًا أَحَدٌ), when disconnected, and after خَلَا، عَدَا (mostly), مَا خَلَا، مَا عَدَا، لَيْسَ، لَا يَكُونُ",
 "question": {
  "en": ["What is the mustathnā? What is taken out of a plurality by إِلَّا or one of its sisters (غَيْر، سِوَى، خَلَا، عَدَا، حَاشَا) — the connected kind.",
         "What is the disconnected mustathnā? What is mentioned after إِلَّا without being one of the plurality: جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ — the donkey was never among the people.",
         "When is the mustathnā manṣūb? After the non-adjectival إِلَّا in complete affirmative speech: جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا — the speech affirmed, the mustathnā minhu mentioned.",
         "And when fronted? Also naṣb, even in negation: مَا جَاءَنِي إِلَّا زَيْدًا أَحَدٌ — the mustathnā precedes its minhu, so the badal is barred.",
         "And the disconnected? Naṣb — nothing for it to replace: إِلَّا الْحِمَارَ.",
         "After which other tools? خَلَا and عَدَا mostly (jarr in the fewer cases), مَا خَلَا and مَا عَدَا always, لَيْسَ and لَا يَكُونُ as the khabar of the hidden ism.",
         "What does the engine READ here? The DabtEngine reads the name after إِلَّا on the author's fatḥa after a complete affirmative clause as the mustathnā in naṣb, the fronted one before أَحَدٌ, the definite disconnected one, and the exception verbs خَلَا، عَدَا، لَيْسَ with their naṣb."],
  "tr": ["Müstesnâ nedir? İllâ veya kardeşlerinden biriyle (gayr, sivâ, halâ, adâ, hâşâ) bir çokluktan çıkarılan — muttasıl nev'i.",
         "Munkatı' müstesnâ nedir? İllâ'dan sonra, çokluktan olmaksızın zikredilen: câenî'l-kavmü ille'l-himâre — eşek zaten kavimden değildi.",
         "Müstesnâ ne zaman mansûbdur? Sıfat olmayan illâ'dan sonra tam ve müsbet sözde: câenî'l-kavmü illâ Zeyden — söz müsbet, müstesnâ minh zikredilmiş.",
         "Öne alınınca? Yine nasb, nefiyde bile: mâ câenî illâ Zeyden ehadün — müstesnâ minhinden önce gelir, bedel kapanır.",
         "Munkatı'da? Nasb — yerini alacağı bir şey yok: ille'l-himâre.",
         "Başka hangi edatlardan sonra? Çoğunlukla halâ ve adâ (azı mecrûr), dâimâ mâ halâ ve mâ adâ, gizli ismin haberi olarak leyse ve lâ yekûnu.",
         "Motor burada neyi OKUR? DabtEngine tam müsbet cümleden sonra illâ'nın ardındaki, yazarın fethalı ismini mansûb müstesnâ; ehadün'den önce öne alınmışı; ma'rife munkatı'ı; ve nasblarıyla halâ, adâ, leyse istisnâ fiillerini okur."],
 },
 "plain": {"en": "The eighth accusative is the exception: «the people came except Zayd». «Connected» when Zayd is one of the people, «disconnected» when the thing was never in the group («except the donkey»). It takes the accusative after a complete positive sentence, before the group word, when disconnected, and after khalā or laysa.",
           "tr": "Sekizinci mansûb istisnâdır: «kavim geldi, Zeyd hariç». Zeyd kavimden ise «muttasıl», hariç tutulan şey zaten topluluktan değilse («eşek hariç») «munkatı'»dır. Tam müsbet cümleden sonra, topluluk sözcüğünün önüne geçince, munkatı' olunca ve halâ, adâ, leyse'den sonra nasb alır."},
 "explanation": {"en": "The eighth manṣūb, the mustathnā, is of two kinds: connected — what is taken out of a plurality by إِلَّا or one of its sisters — and disconnected — what is mentioned after them without being taken out of a plurality, since it was never one of it (جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ). It is manṣūb when it comes after the non-adjectival إِلَّا in complete affirmative speech (جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا), or fronted before the mustathnā minhu (مَا جَاءَنِي إِلَّا زَيْدًا أَحَدٌ), or disconnected, or after خَلَا and عَدَا in most usage, or after مَا خَلَا، مَا عَدَا، لَيْسَ and لَا يَكُونُ. The adjectival إِلَّا — in the sense of غَيْر — and the cases of badal and jarr follow in the next chapter.",
                 "tr": "Sekizinci mansûb müstesnâ iki nev'dir: muttasıl — illâ veya kardeşlerinden biriyle çokluktan çıkarılan — ve munkatı' — bunlardan sonra çokluktan çıkarılmaksızın zikredilen; çünkü zaten ondan değildi (câenî'l-kavmü ille'l-himâre). Sıfat olmayan illâ'dan sonra tam müsbet sözde (câenî'l-kavmü illâ Zeyden), müstesnâ minhin önüne alınmış (mâ câenî illâ Zeyden ehadün), munkatı' olarak, çoğunlukla halâ ve adâ'dan sonra, mâ halâ, mâ adâ, leyse ve lâ yekûnu'dan sonra mansûbdur. Gayr mânâsındaki sıfat illâ ile bedel ve cer hâlleri sonraki bâbdadır."},
 "examples": [
  {"ar": "مُتَّصِلٌ وَهُوَ الْمُخْرَجُ عَنْ مُتَعَدِّدٍ بِإِلَّا أَوْ إِحْدَى أَخَوَاتِهَا", "en": "the connected mustathnā", "tr": "muttasıl müstesnâ", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "وَمُنْقَطِعٌ وَهُوَ الْمَذْكُورُ بَعْدَهَا غَيْرَ مُخْرَجٍ عَنْ مُتَعَدِّدٍ", "en": "the disconnected", "tr": "munkatı'", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا", "en": "naṣb in complete affirmative speech", "tr": "tam müsbet sözde nasb", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "مَا جَاءَنِي إِلَّا زَيْدًا أَحَدٌ", "en": "the mustathnā fronted", "tr": "öne alınmış müstesnâ", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ", "en": "the disconnected in naṣb", "tr": "mansûb munkatı'", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "خَلَا أَوْ عَدَا … أَوْ لَيْسَ أَوْ لَا يَكُونُ", "en": "the other exception tools", "tr": "diğer istisnâ edatları", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي الْقَوْمُ إِلَّا زَيْدٌ", "right": "جَاءَنِي الْقَوْمُ إِلَّا زَيْدًا", "why": {"en": "in complete affirmative speech the mustathnā is manṣūb; the badal is for the negated", "tr": "tam müsbet sözde müstesnâ mansûbdur; bedel menfî içindir"}},
  {"wrong": "مَا جَاءَنِي إِلَّا زَيْدٌ أَحَدٌ", "right": "مَا جَاءَنِي إِلَّا زَيْدًا أَحَدٌ", "why": {"en": "fronted before its minhu the mustathnā takes naṣb even in negation", "tr": "minhinden önce gelen müstesnâ nefiyde bile nasb alır"}},
  {"wrong": "جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارُ", "right": "جَاءَنِي الْقَوْمُ إِلَّا الْحِمَارَ", "why": {"en": "the disconnected mustathnā has nothing to replace and keeps its naṣb", "tr": "munkatı' müstesnânın yerini alacağı bir şey yoktur; nasbını korur"}},
 ],
}
ADD_EN = (" Chapter 38 (print pp. 135-136): the mustathnā connected (s1) and disconnected (s2); its naṣb after the non-adjectival illā in complete affirmative speech (s3), fronted before its minhu (s4), disconnected (s5), after khalā, ʿadā, mā khalā, mā ʿadā, laysa, lā yakūnu (s6).")
ADD_TR = (" Otuz sekizinci bab (baskı s. 135-136): muttasıl (s1) ve munkatı' (s2) müstesnâ; sıfat olmayan illâ'dan sonra tam müsbet sözde (s3), minhinden önce (s4), munkatı' (s5), halâ, adâ, mâ halâ, mâ adâ, leyse, lâ yekûnu'dan sonra (s6) nasbı.")
write_out(38, S, TITLE, ADD_EN, ADD_TR, "pp. 135-136", GLOSS_ADD, notes=(NOTE,),
          related=((K37, [K]), (IS, [K]), (ISM, [K]), ("badal", [K]), (TN, [K])))
report(38, S, GLOSS_ADD, (NOTE,))
