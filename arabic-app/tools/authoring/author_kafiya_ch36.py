# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 36: THE FOUR SISTERS — كَأَنَّ for likeness and its lightened كَأَنْ that governs nothing (the verse of the two
caskets); لَكِنَّ for correction between an affirmative and a negative, its lightened لَكِنْ and the wāw it admits; لَيْتَ for wish, and
al-Farrāʾ's naṣb of both its complements; لَعَلَّ for hope — the thing wished for (2:189) and the thing feared (42:17) — and the
irregular jarr with it.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~340-341 of the transcription.

  COMMENTARY (the notebook): s1-s6 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch36.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "kaanna-lakinna-layta-laalla-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "كَأَنَّ وَلَكِنَّ وَلَيْتَ وَلَعَلَّ", "en": "Ka-anna, lākinna, layta and laʿalla", "tr": "Keenne, lâkinne, leyte ve lealle"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr3d(): return seg("هُمَا", "pron-3d", "pron")
def W(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return tok(full, lex, pos, [K] + tags, ar, en, tr, punct=punct, segments=segments)
def nahwu(punct=":"):
    return W("نَحْوُ", "nahw", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness"],
             "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ، وَمَا بَعْدَهُ مُضَافٌ إِلَيْهِ.", "«for instance» — the khabar of a dropped mubtada, annexed to what it cites.",
             "«meselâ» — hazfedilmiş bir mübtedânın haberi; zikrettiğine muzâf.", punct=punct)
def atf_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    segs = [seg("وَ", "wa", "conj")] + (extra_segs if extra_segs else [seg(inner, lex, pos)])
    return W(full, lex, pos, ["atf-nasaq"] + tags, "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=segs)
def cited(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)
def cited_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None, extra_segs=None):
    return atf_wa(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — " + ar, en, tr, inner, punct=punct, extra_segs=extra_segs)
def li_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "اللَّامُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("لِ", "li", "prep"), seg(inner, lex, pos)]))
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]))
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "part"), seg(inner, lex, pos)]))
def jw(full): return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full

IN = "inna-wa-akhawatuha"
AT = "atf-nasaq"
def HEAD(full, lex, en, tr, wa=True, punct=None):
    if wa: return cited_wa("وَ" + full, lex, "part", ["mubtada-khabar", K, IN], full + " لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, full, punct=punct)
    return cited(full, lex, "part", ["mubtada-khabar", K, IN], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, punct=punct)
def FOR(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return li_(full, lex, "noun", ["mubtada-khabar", K] + list(tags), inner + " مَجْرُورٌ — خَبَرٌ.", en, tr, inner, punct=punct, segs=segs)
def ISM(full, lex, en, tr, pos="propn", punct=None, segs=None, tags=(), ar="اسْمُ الْحَرْفِ مَنْصُوبٌ."): return cited(full, lex, pos, [IN] + list(tags), ar, en, tr, punct=punct, segments=segs)
def KHB(full, lex, en, tr, pos="noun", punct=None, ar="خَبَرُ الْحَرْفِ مَرْفُوعٌ.", tags=(), segs=None): return cited(full, lex, pos, [IN] + list(tags), ar, en, tr, punct=punct, segments=segs)

S.append({"id": "s1", "translation": {
 "en": "كَأَنَّ is for likeness; and it is lightened and remains كَأَنْ, and on the most eloquent usage it is stripped of government — as كَأَنْ ثَدْيَاهُ حُقَّانِ, where it did not govern, for had it governed, its ism being a dual would have been ثَدْيَيْهِ, with the yāʾ of naṣb." + C_EN,
 "tr": "كَأَنَّ teşbih içindir; hafifletilir, كَأَنْ kalır ve en fasih kullanışa göre amelden bozulur — كَأَنْ ثَدْيَاهُ حُقَّانِ gibi; orada amel etmemiştir, çünkü etseydi ismi tesniye olduğu için nasb yâsıyla ثَدْيَيْهِ olurdu." + C_TR},
 "tokens": [
  HEAD("كَأَنَّ", "kaanna", "«ka-anna».", "«keenne».", wa=False),
  FOR("لِلتَّشْبِيهِ", "tashbih", "«is for likeness».", "«teşbih içindir».", "التَّشْبِيهِ", segs=[seg("لِ", "li", "prep"), seg("لتَّشْبِيهِ", "tashbih", "noun")], punct="؛", tags=["tashbih"]),
  atf_wa("وَتُخَفَّفُ", "khaffafa", "verb", ["naib-al-fail", "form-ii-verbs"], "تُخَفَّفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it is lightened».", "«ve hafifletilir».", "تُخَفَّفُ"),
  W("فَتَبْقَى", "baqiya", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَبْقَى فِعْلٌ مُضَارِعٌ.", "«and remains».", "«ve ... kalır».", segments=[seg("فَ", "fa", "conj"), seg("تَبْقَى", "baqiya", "verb")]),
  cited("كَأَنْ", "kaan", "part", [K, IN], "كَأَنْ الْمُخَفَّفَةُ — خَبَرُ تَبْقَى.", "«ka-an».", "«keen».", punct="،"),
  atf_wa("وَتُهْمَلُ", "ahmala", "verb", ["naib-al-fail", "form-iv-verbs"], "تُهْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is stripped of government».", "«ve amelden bozulur».", "تُهْمَلُ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«göre»."),
  W("الْأَفْصَحِ", "afsah", "noun", ["huruf-jarr", "ism-tafdil"], "مَجْرُورٌ.", "«the most eloquent usage».", "«en fasih kullanışa».", punct="،"),
  nahwu(),
  cited("كَأَنْ", "kaan", "part", [K, IN], "مُخَفَّفَةٌ مُهْمَلَةٌ.", "«as if».", "«sanki»."),
  cited("ثَدْيَاهُ", "thady", "noun", ["mubtada-khabar", "al-muthanna", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ — لَا اسْمُ كَأَنْ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his two breasts».", "«onun iki memesi».", segments=[seg("ثَدْيَا", "thady", "noun"), pr3ms()]),
  cited("حُقَّانِ", "huqq", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«are two caskets».", "«iki hokkadır».", punct="،"),
  W("فَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«where … not».", "«orada ... -memiştir».", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  W("تَعْمَلْ", "amila", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«did it govern».", "«amel etmemiştir».", punct="،"),
  W("لِأَنَّهَا", "lianna", "part", [IN, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«for had it».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("لَوْ", "law", "part", ["al-majzum-wal-shart-wal-jaza"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«if».", "«-seydi»."),
  W("عَمِلَتْ", "amila", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — فِعْلُ لَوْ.", "«governed».", "«amel etseydi».", segments=[seg("عَمِلَ", "amila", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("لَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«would have been».", "«olurdu».", segments=[seg("لَ", "lam-jawab", "part"), seg("كَانَ", "kana", "verb")]),
  W("اسْمُهَا", "ism", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", IN], "اسْمُ كَانَ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ism».", "«ismi».", segments=[seg("اسْمُ", "ism", "noun"), pr3fs()]),
  W("مُثَنًّى", "muthanna", "noun", ["hal", "al-muthanna", "ism-maqsur-manqus"], "حَالٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«being a dual».", "«tesniye olduğu için»."),
  cited("ثَدْيَيْهِ", "thady", "noun", ["kana-wa-akhawatuha", "al-muthanna", "idafa-definiteness"], "خَبَرُ كَانَ — اللَّفْظُ مَحْكِيٌّ؛ بِالْيَاءِ لَوْ نُصِبَ.", "«thadyayhi».", "«sedyeyhi».", segments=[seg("ثَدْيَيْ", "thady", "noun"), pr3msi()]),
  bi_("بِيَاءِ", "ya-letter", "noun", ["idafa-definiteness"], "يَاءِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«with the yāʾ of».", "«yâsıyla».", "يَاءِ"),
  W("النَّصْبِ", "nasb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naṣb».", "«nasb».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And لَكِنَّ is for correction — that is, to remove a misunderstanding arising from the preceding speech — and it stands between two sentences that differ in sense by affirmation and negation: when one says جَاءَنِي زَيْدٌ, the hearer may suppose his companion ʿAmr came too, and to lift that supposition one says لَكِنَّ عَمْرًا لَمْ يَجِئْ." + C_EN,
 "tr": "لَكِنَّ istidrak içindir — yani önceki kelâmdan doğan yanlış anlama ihtimalini gidermek için — ve mânâca müsbet ve menfî olmakla birbirinden ayrılan iki cümle arasında bulunur: جَاءَنِي زَيْدٌ denince dinleyen arkadaşı Amr'ın da geldiğini sanabilir; bu vehmi kaldırmak için لَكِنَّ عَمْرًا لَمْ يَجِئْ denir." + C_TR},
 "tokens": [
  HEAD("لَكِنَّ", "lakinna", "«and lākinna».", "«ve lâkinne»."),
  FOR("لِلِاسْتِدْرَاكِ", "istidrak", "«is for correction».", "«istidrak içindir».", "الِاسْتِدْرَاكِ", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِدْرَاكِ", "istidrak", "noun")], punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  li_("لِدَفْعِ", "dafaa", "noun", ["idafa-definiteness", "lam-taleel"], "دَفْعِ مَجْرُورٌ، وَهُوَ مُضَافٌ — مَصْدَرُ دَفَعَ.", "«to remove».", "«gidermek için».", "دَفْعِ"),
  W("تَوَهُّمٍ", "tawahhum", "noun", ["idafa-definiteness", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a misunderstanding».", "«yanlış anlama ihtimalini»."),
  W("يَنْشَأُ", "nashaa", "verb", ["naat-sifa", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ صِفَةٌ لِتَوَهُّمٍ.", "«arising».", "«doğan»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الْكَلَامِ", "kalam", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the speech».", "«kelâmdan»."),
  W("السَّابِقِ", "sabiq", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«preceding».", "«önceki».", punct="،"),
  atf_wa("وَتَقَعُ", "waqaa", "verb", ["fail", "mithal-verbs"], "تَقَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it stands».", "«ve bulunur».", "تَقَعُ"),
  W("بَيْنَ", "bayna", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasında»."),
  W("جُمْلَتَيْنِ", "jumla", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two sentences».", "«iki cümle»."),
  W("مُخْتَلِفَتَيْنِ", "mukhtalif", "noun", ["naat-sifa", "al-muthanna", "ism-fail", "form-viii-verbs"], "صِفَةٌ مَجْرُورَةٌ بِالْيَاءِ.", "«that differ».", "«ayrılan»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-ca»."),
  W("الْمَعْنَى", "mana", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«sense».", "«mânâ»."),
  bi_("بِالْإِثْبَاتِ", "ithbat", "noun", [], "الْإِثْبَاتِ مَجْرُورٌ.", "«by affirmation».", "«müsbet».", "الْإِثْبَاتِ"),
  atf_wa("وَالنَّفْيِ", "nafy", "noun", [AT], "النَّفْيِ مَعْطُوفٌ مَجْرُورٌ.", "«and negation».", "«ve menfî olmakla».", "النَّفْيِ", punct=":"),
  W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ince».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  W("قِيلَ", "qala", "verb", ["idha-shartiyya", "naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«one says».", "«denince»."),
  cited("جَاءَنِي", "jaa", "verb", ["naib-al-fail", "fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ نَائِبُ فَاعِلٍ.", "«Zayd came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ — الْجُمْلَةُ الْمُثْبَتَةُ.", "«Zayd».", "«Zeyd».", punct="،"),
  W("رُبَّمَا", "rubba", "part", ["anwa-ma"], "رُبَّ مَكْفُوفَةٌ بِمَا — لِلتَّقْلِيلِ.", "«may».", "«-ebilir».", segments=[seg("رُبَّ", "rubba", "prep"), seg("مَا", "ma-kaffa", "part")]),
  W("تَوَهَّمَ", "tawahhama", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ.", "«suppose».", "«sanabilir»."),
  W("السَّامِعُ", "sami-hearer", "noun", ["fail", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the hearer».", "«dinleyen»."),
  W("مَجِيءَ", "maji", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ — مَصْدَرُ جَاءَ.", "«the coming of».", "«geldiğini»."),
  W("صَاحِبِهِ", "sahib", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his companion».", "«arkadaşı».", segments=[seg("صَاحِبِ", "sahib", "noun"), pr3msi()]),
  cited("عَمْرٍو", "amr-name", "propn", ["badal", "idafa-definiteness"], "بَدَلٌ مِنْ صَاحِبِهِ مَجْرُورٌ.", "«ʿAmr».", "«Amr'ın»."),
  W("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ.", "«too».", "«da».", punct="،"),
  W("فَيُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«so one says».", "«denir».", segments=[seg("فَ", "fa", "conj"), seg("يُقَالُ", "qala", "verb")]),
  li_("لِدَفْعِهِ", "dafaa", "noun", ["idafa-definiteness", "lam-taleel"], "دَفْعِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to lift it».", "«bunu kaldırmak için».", "دَفْعِ", segs=[seg("لِ", "lam-taleel", "part"), seg("دَفْعِ", "dafaa", "noun"), pr3msi()], punct=":"),
  cited("لَكِنَّ", "lakinna", "part", [K, IN], "حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ.", "«but».", "«fakat»."),
  ISM("عَمْرًا", "amr-name", "«ʿAmr».", "«Amr»."),
  cited("لَمْ", "lam-jazima", "part", [IN, "nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — الْجُمْلَةُ خَبَرُ لَكِنَّ، وَهِيَ الْمَنْفِيَّةُ.", "«did not».", "«-medi»."),
  cited("يَجِئْ", "jaa", "verb", ["nawasib-wa-jawazim-al-mudari", "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«come».", "«gelmedi».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And لَكِنَّ is lightened and remains لَكِنْ, and is stripped of government; and the wāw may come with لَكِنَّ." + C_EN,
 "tr": "لَكِنَّ hafifletilir, لَكِنْ kalır ve amelden bozulur; لَكِنَّ ile birlikte vâvın gelmesi câizdir." + C_TR},
 "tokens": [
  atf_wa("وَتُخَفَّفُ", "khaffafa", "verb", ["naib-al-fail", "form-ii-verbs"], "تُخَفَّفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is lightened».", "«ve hafifletilir».", "تُخَفَّفُ"),
  cited("لَكِنَّ", "lakinna", "part", ["naib-al-fail", K, IN], "نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", "«lākinna».", "«lâkinne»."),
  W("فَتَبْقَى", "baqiya", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَبْقَى فِعْلٌ مُضَارِعٌ.", "«and remains».", "«ve ... kalır».", segments=[seg("فَ", "fa", "conj"), seg("تَبْقَى", "baqiya", "verb")]),
  cited("لَكِنْ", "lakin", "part", [K, IN, AT], "لَكِنْ الْمُخَفَّفَةُ — خَبَرُ تَبْقَى.", "«lākin».", "«lâkin».", punct="،"),
  atf_wa("وَتُهْمَلُ", "ahmala", "verb", ["naib-al-fail", "form-iv-verbs"], "تُهْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is stripped of government».", "«ve amelden bozulur».", "تُهْمَلُ", punct="؛"),
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and may».", "«ve câizdir».", "يَجُوزُ"),
  W("مَجِيءُ", "maji", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the coming of».", "«gelmesi»."),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness", "anwa-al-waw"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wāw».", "«vâvın»."),
  W("مَعَ", "maa", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«... ile birlikte»."),
  cited("لَكِنَّ", "lakinna", "part", ["idafa-definiteness", IN], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«lākinna».", "«lâkinne».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And لَيْتَ is for wish; and al-Farrāʾ allowed both of its complements to be in naṣb — لَيْتَ زَيْدًا قَائِمًا." + C_EN,
 "tr": "لَيْتَ temennî içindir; Ferrâ, her iki ma'mûlünün de nasb olmasına cevaz verdi — لَيْتَ زَيْدًا قَائِمًا." + C_TR},
 "tokens": [
  HEAD("لَيْتَ", "layta", "«and layta».", "«ve leyte»."),
  FOR("لِلتَّمَنِّي", "tamanni", "«is for wish».", "«temennî içindir».", "التَّمَنِّي", segs=[seg("لِ", "li", "prep"), seg("لتَّمَنِّي", "tamanni", "noun")], punct="؛", tags=["insha-wa-tamanni"]),
  atf_wa("وَجَوَّزَ", "jawwaza", "verb", ["fail", "form-ii-verbs"], "جَوَّزَ فِعْلٌ مَاضٍ.", "«and allowed».", "«ve cevaz verdi».", "جَوَّزَ"),
  W("الْفَرَّاءُ", "farra-propn", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Farrāʾ».", "«Ferrâ»."),
  W("نَصْبَ", "nasb", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the naṣb of».", "«nasb olmasına»."),
  W("مَعْمُولَيْهَا", "mamul", "noun", ["idafa-definiteness", "al-muthanna", "al-mamul-wa-aqsamuh"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ، وَهَا مُضَافٌ إِلَيْهِ.", "«both its complements».", "«her iki ma'mûlünün».", segments=[seg("مَعْمُولَيْ", "mamul", "noun"), pr3fs()]),
  W("جَمِيعًا", "jami", "noun", ["hal"], "حَالٌ مَنْصُوبٌ، أَوْ تَوْكِيدٌ.", "«together».", "«birlikte».", punct="—"),
  cited("لَيْتَ", "layta", "part", [K, IN], "حَرْفُ تَمَنٍّ وَنَصْبٍ.", "«would that».", "«keşke»."),
  ISM("زَيْدًا", "zayd", "«Zayd».", "«Zeyd»."),
  cited("قَائِمًا", "qaim", "noun", [IN, K], "خَبَرُ لَيْتَ مَنْصُوبٌ عَلَى مَذْهَبِ الْفَرَّاءِ.", "«were standing».", "«ayakta olsaydı».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And لَعَلَّ is for hope — that is, awaiting a thing wished for or a thing feared; in لَعَلَّكُمْ تُفْلِحُونَ it is used for what is wished, and in لَعَلَّ السَّاعَةَ قَرِيبٌ for what is feared." + C_EN,
 "tr": "لَعَلَّ tereccî içindir — yani arzu edilen ya da korkulan bir işi beklemek mânâsına; لَعَلَّكُمْ تُفْلِحُونَ'de arzu edilen yerde, لَعَلَّ السَّاعَةَ قَرِيبٌ'de korkulan yerde kullanılmıştır." + C_TR},
 "tokens": [
  HEAD("لَعَلَّ", "laalla", "«and laʿalla».", "«ve lealle»."),
  FOR("لِلتَّرَجِّي", "tarajji", "«is for hope».", "«tereccî içindir».", "التَّرَجِّي", segs=[seg("لِ", "li", "prep"), seg("لتَّرَجِّي", "tarajji", "noun")], punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  li_("لِانْتِظَارِ", "intizar", "noun", ["idafa-definiteness", "form-viii-verbs"], "انْتِظَارِ مَجْرُورٌ، وَهُوَ مُضَافٌ — مَصْدَرُ انْتَظَرَ.", "«awaiting».", "«beklemek».", "انْتِظَارِ"),
  W("أَمْرٍ", "amr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir işi»."),
  W("مَرْجُوٍّ", "marju", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«wished for».", "«arzu edilen»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَخُوفٍ", "makhuf", "noun", [AT, "ism-maful", "hollow-verbs"], "مَعْطُوفٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ خَافَ.", "«feared».", "«korkulan».", punct="؛"),
  W("فَفِي", "fi", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«in».", "«-de».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  cited("لَعَلَّكُمْ", "laalla", "part", ["huruf-jarr", K, IN], "الْآيَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — لَعَلَّ حَرْفُ تَرَجٍّ، وَكُمْ اسْمُهَا.", "«so that you may».", "«umulur ki siz».", segments=[seg("لَعَلَّ", "laalla", "part"), pr2mp()]),
  KHB("تُفْلِحُونَ", "aflaha", "«prosper».", "«kurtuluşa erersiniz».", pos="verb", ar="فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ لَعَلَّ.", tags=["form-iv-verbs"]),
  W("اسْتُعْمِلَتْ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«it is used».", "«kullanılmıştır».", segments=[seg("اسْتُعْمِلَ", "istamala", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«... yerde»."),
  W("الْمَرْجُوِّ", "marju", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«what is wished».", "«arzu edilen».", punct="،"),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  cited("لَعَلَّ", "laalla", "part", ["huruf-jarr", K, IN], "الْآيَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — لَعَلَّ حَرْفُ تَرَجٍّ.", "«perhaps».", "«belki»."),
  ISM("السَّاعَةَ", "saa-hour", "«the Hour».", "«kıyamet».", pos="noun"),
  KHB("قَرِيبٌ", "qarib", "«is near».", "«yakındır».", tags=["sifa-mushabbaha"]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«... yerde»."),
  W("الْمَخُوفِ", "makhuf", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«what is feared».", "«korkulan».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And jarr by لَعَلَّ is irregular." + C_EN,
 "tr": "لَعَلَّ ile cer şâzdır." + C_TR},
 "tokens": [
  atf_wa("وَالْجَرُّ", "jarr", "noun", ["mubtada-khabar", "huruf-jarr"], "الْجَرُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and jarr».", "«ve cer».", "الْجَرُّ"),
  bi_("بِلَعَلَّ", "laalla", "part", [K, IN], "لَعَلَّ فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«by laʿalla».", "«lealle ile».", "لَعَلَّ"),
  W("شَاذٌّ", "shadhdh", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — لُغَةُ عُقَيْلٍ.", "«is irregular».", "«şâzdır».", punct="."),
 ]})

def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "kaan": need("kaan", "كَأَنْ (الْمُخَفَّفَةُ)", "ك أ ن", "part", "ka-an lightened from ka-anna — «as if», governing nothing on the most eloquent usage", "keenne'den hafifletilmiş keen — «sanki», en fasih kullanışa göre amel etmez", 5),
 "farra-propn": need("farra-propn", "الْفَرَّاء", "ف ر ي", "propn", "Al-Farrāʾ (d. 207/822) — the Kufan grammarian, author of Maʿānī al-Qurʾān", "Ferrâ (ö. 207/822) — Kûfeli nahivci, Meâni'l-Kur'ân'ın müellifi", 5),
 "ahmala": need("ahmala", "أَهْمَلَ", "ه م ل", "verb", "to leave ungoverning, to neglect (Form IV) — of a particle stripped of its government", "ihmal etmek, amelsiz bırakmak (if'âl) — ameli kaldırılan harf için", 4),
 "nashaa": need("nashaa", "نَشَأَ", "ن ش أ", "verb", "to arise, to grow out of", "doğmak, neş'et etmek", 3),
 "sami-hearer": need("sami-hearer", "سَامِع", "س م ع", "noun", "a hearer — the ism fāʿil of سَمِعَ", "dinleyen, sâmi — semia'nın ism-i fâili", 2),
 "makhuf": need("makhuf", "مَخُوف", "خ و ف", "noun", "feared, dreaded — the ism mafʿūl of خَافَ", "korkulan — hâfe'nin ism-i mef'ûlü", 3),
 "intizar": need("intizar", "انْتِظَار", "ن ظ ر", "noun", "awaiting, expectation — the maṣdar of انْتَظَرَ", "bekleme, intizar — intezara'nın masdarı", 3),
}
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ahmala", _nfc(_sg.derived(_sg.B4, _sg.W4, "ُ", "أَهْمَل", "هْمِل", "أَهْمِل", "إِهْمَال", "مُهْمِل", "مُهْمَل", "أُهْمِلَ", "يُهْمَلُ", "أَهْمَلَ الشَّيْءَ: تَرَكَهُ وَلَمْ يَسْتَعْمِلْهُ — بَابُ الْإِفْعَالِ.")))
put_morph(mo, "nashaa", find_morph("nashaa"))   # an identity copy: the key is owned elsewhere
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch36 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "كَأَنَّ وَلَكِنَّ وَلَيْتَ وَلَعَلَّ فِي الْكَافِيَةِ", "en": "Ka-anna, lākinna, layta and laʿalla in the Kafiya: likeness and its ungoverning ka-an, correction between yes and no, wish and al-Farrāʾ's double naṣb, hope for the wished and the feared", "tr": "Kâfiye'de keenne, lâkinne, leyte ve lealle: teşbih ve amelsiz keen, evet ile hayır arasında istidrak, temennî ve Ferrâ'nın çifte nasbı, arzu edilen ve korkulan için tereccî"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — كأن للتشبيه؛ لكن للاستدراك؛ ليت للتمني؛ لعل للترجي", "ضياء صونغور اوغلى — دفتر الكافية: كأن ثدياه حقان؛ لكن بين جملتين مختلفتين إثباتا ونفيا؛ لكن المخففة والواو؛ الفراء وليت زيدا قائما؛ لعلكم تفلحون ولعل الساعة قريب؛ الجر بلعل شاذ"],
 "question": {
  "en": ["What does ka-anna do? It likens: كَأَنَّ زَيْدًا أَسَدٌ. Lightened to ka-an it stops governing on the best usage, and the notebook proves it from a half-line: كَأَنْ ثَدْيَاهُ حُقَّانِ keeps the alif of the dual, so the word is a mubtada and not ka-an's ism — had it been governed it would read ثَدْيَيْهِ. The SignEngine's dual rule is the whole argument.",
         "When is lākinna used? To correct a false inference from what was just said, and so it stands between an affirmative and a negative (or the reverse): «Zayd came to me — but ʿAmr did not». Its lightened lākin governs nothing, and lākinna may take a wāw before it.",
         "What is special about layta? It wishes for what cannot be. Al-Farrāʾ let both its ism and its khabar stand in naṣb — لَيْتَ زَيْدًا قَائِمًا — a Kufan reading the notebook records and does not adopt.",
         "And laʿalla? Hope — awaiting something, whether wished for (لَعَلَّكُمْ تُفْلِحُونَ) or feared (لَعَلَّ السَّاعَةَ قَرِيبٌ). Putting its noun in jarr is irregular, a dialect form the books mention and the engine refuses.",
         "What does the engine do? All four sit in the INNA table with their government; the lightened forms are listed as ungoverning; the analyzer's dual-alif test is what decides ثَدْيَاهُ, and laʿalla's majrūr noun is flagged shādhdh rather than parsed."],
  "tr": ["Keenne ne yapar? Benzetir: كَأَنَّ زَيْدًا أَسَدٌ. Keen'e hafifleyince en iyi kullanışa göre amelden kesilir; defter bunu bir mısradan kanıtlar: كَأَنْ ثَدْيَاهُ حُقَّانِ tesniye elifini tutar, dolayısıyla kelime keen'in ismi değil mübtedâdır — yönetilseydi ثَدْيَيْهِ okunurdu. SignEngine'in tesniye kuralı bütün delildir.",
         "Lâkinne ne zaman kullanılır? Az önce söylenenden çıkan yanlış bir sonucu düzeltmek için; bu yüzden bir müsbet ile bir menfî (ya da tersi) arasında durur: «Zeyd bana geldi — fakat Amr gelmedi». Hafiflemiş lâkin hiçbir şeyi yönetmez ve lâkinne önüne vâv alabilir.",
         "Leyte'de özel olan ne? Olamayacak şeyi diler. Ferrâ hem ismini hem haberini nasbda bıraktı — لَيْتَ زَيْدًا قَائِمًا — defterin kaydettiği ve benimsemediği bir Kûfe okuyuşu.",
         "Ya lealle? Tereccî — ister arzu edilen (لَعَلَّكُمْ تُفْلِحُونَ) ister korkulan (لَعَلَّ السَّاعَةَ قَرِيبٌ) bir şeyi beklemek. İsmini cer etmek şâzdır; kitapların andığı, motorun reddettiği bir lehçe biçimi.",
         "Motor ne yapar? Dördü de amelleriyle INNA tablosunda oturur; hafiflemiş biçimler amelsiz olarak listelenir; analizörün tesniye elifi testi ثَدْيَاهُ'yu belirler; lealle'nin mecrûr ismi çözümlenmek yerine şâz diye işaretlenir."]},
 "plain": {
  "en": "Ka-anna says «as if», lākinna says «but», layta says «if only», laʿalla says «maybe». All four govern like inna. Shortened, ka-an and lākin govern nothing; one grammarian let layta put both its words in naṣb; and laʿalla with a majrūr noun is a dialect oddity.",
  "tr": "Keenne «sanki», lâkinne «fakat», leyte «keşke», lealle «belki» der. Dördü de inne gibi amel eder. Kısalınca keen ve lâkin hiçbir şeyi yönetmez; bir nahivci leyte'nin iki kelimesini de nasbda bıraktı; mecrûr isimli lealle ise bir lehçe tuhaflığıdır."},
 "explanation": {
  "en": "The four remaining sisters, each with its meaning and its one notable ruling. For كَأَنَّ the ruling is the lightened كَأَنْ, and the notebook's proof is the kind a parser can run: in the half-line كَأَنْ ثَدْيَاهُ حُقَّانِ the dual keeps its alif, so nothing governed it. For لَكِنَّ the notebook gives the function — correction of a false inference — and the structural consequence: it sits between an affirmative and a negative, as the stock example shows; the lightened لَكِنْ is ungoverning, and the wāw may precede لَكِنَّ. For لَيْتَ the only ruling is al-Farrāʾ's double naṣb, recorded with his name. For لَعَلَّ the two Qurʾānic cases show hope reaching toward the wished-for and toward the feared, and the chapter closes on the irregular jarr. The chapter is short because the Kafiya is short here; the Iẓhār's chapter on the sisters of إِنَّ supplies the drill.",
  "tr": "Kalan dört kardeş, her biri mânâsı ve dikkate değer tek hükmüyle. كَأَنَّ için hüküm hafiflemiş كَأَنْ'dir ve defterin delili bir çözümleyicinin çalıştırabileceği türdendir: كَأَنْ ثَدْيَاهُ حُقَّانِ mısraında tesniye elifini tutar, demek ki onu hiçbir şey yönetmemiştir. لَكِنَّ için defter işlevi — yanlış bir çıkarımın düzeltilmesi — ve yapısal sonucu verir: alışılmış örneğin gösterdiği gibi bir müsbet ile bir menfî arasında oturur; hafiflemiş لَكِنْ amelsizdir ve لَكِنَّ'nin önüne vâv gelebilir. لَيْتَ için tek hüküm, adıyla kaydedilen Ferrâ'nın çifte nasbıdır. لَعَلَّ için iki Kur'ânî örnek ümidin arzu edilene ve korkulana uzandığını gösterir; bâb şâz cerle kapanır. Bâb kısadır çünkü Kâfiye burada kısadır; İzhar'ın إِنَّ'nin kardeşleri bâbı alıştırmayı sağlar."},
 "examples": [
  {"ar": "كَأَنْ ثَدْيَاهُ حُقَّانِ", "en": "Ka-an lightened and ungoverning.", "tr": "Hafiflemiş ve amelsiz keen.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "جَاءَنِي زَيْدٌ لَكِنَّ عَمْرًا لَمْ يَجِئْ", "en": "Correction between an affirmative and a negative.", "tr": "Müsbet ile menfî arasında istidrak.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "لَيْتَ زَيْدًا قَائِمًا", "en": "Al-Farrāʾ's double naṣb.", "tr": "Ferrâ'nın çifte nasbı.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "لَعَلَّكُمْ تُفْلِحُونَ — لَعَلَّ السَّاعَةَ قَرِيبٌ", "en": "Hope for the wished-for and the feared.", "tr": "Arzu edilen ve korkulan için tereccî.", "sourceStory": "al-kafiya", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«كَأَنْ ثَدْيَيْهِ حُقَّانِ»",
   "right": "«كَأَنْ ثَدْيَاهُ حُقَّانِ — hafif keen amel etmez; isim mübtedâdır»",
   "why": {"en": "The dual's alif shows no governor touched it.", "tr": "Tesniyenin elifi ona hiçbir âmilin dokunmadığını gösterir."}},
  {"wrong": "«جَاءَنِي زَيْدٌ لَكِنَّ عَمْرًا جَاءَ»",
   "right": "«جَاءَنِي زَيْدٌ لَكِنَّ عَمْرًا لَمْ يَجِئْ — iki cümle müsbet ve menfî olmakla ayrılmalı»",
   "why": {"en": "Lākinna corrects; two affirmatives leave nothing to correct.", "tr": "Lâkinne düzeltir; iki müsbet düzeltecek bir şey bırakmaz."}},
  {"wrong": "«لَيْتَ زَيْدًا قَائِمًا — cumhûrun görüşü»",
   "right": "«لَيْتَ زَيْدًا قَائِمٌ — çifte nasb yalnız Ferrâ'nındır»",
   "why": {"en": "The majority keep layta's khabar in rafʿ.", "tr": "Çoğunluk leyte'nin haberini ref'te tutar."}},
  {"wrong": "«لَعَلَّ زَيْدٍ قَائِمٌ»",
   "right": "«لَعَلَّ زَيْدًا قَائِمٌ — lealle ile cer şâzdır»",
   "why": {"en": "Laʿalla governs like inna; the jarr is a dialect oddity.", "tr": "Lealle inne gibi amel eder; cer bir lehçe tuhaflığıdır."}}],
 "relatedNotes": ["al-huruf-al-mushabbaha-bil-fil-fil-kafiya", "masail-inna-wal-mukhaffafa-fil-kafiya", "inna-wa-akhawatuha", "tashbih", "insha-wa-tamanni", "al-muthanna"]}

ADD_EN = (" Chapter 36 (notebook lines ~340-341): ka-anna and its lightened form (the verse of the two caskets), lākinna, layta (al-Farrāʾ) and laʿalla (2:189, 42:17) — the notebook's exposition, kept as commentary (s1-s6). Qurʾānic text as the source prints it.")
ADD_TR = (" Otuz altıncı bâb (defter satırları ~340-341): keenne ve hafiflemiş biçimi (iki hokka beyti), lâkinne, leyte (Ferrâ) ve lealle (2:189, 42:17) — defterin açıklaması, şerh olarak (s1-s6). Kur'ân metni kaynağın bastığı gibi.")
write_out(36, S, TITLE, ADD_EN, ADD_TR, "340-341", GLOSS_ADD, notes=(NOTE,),
          related=(("al-huruf-al-mushabbaha-bil-fil-fil-kafiya", [K]), ("insha-wa-tamanni", [K])))
report(36, S, GLOSS_ADD, (NOTE,))
