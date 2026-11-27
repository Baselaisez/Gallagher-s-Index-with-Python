# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 17: THE SIFA MUSHABBAHA. The definition in the notebook's own Arabic (with حَسَن and كَرِيم); the notebook's
contrast with the ism fa'il (huduth / thubut: آكِل شَارِب against حَسَن قَبِيح); the heard shapes unlike فَاعِل and the notebook's list of
patterns; its government; the two states of the sifa and the three of its governed word — six cases, each in three cases, eighteen;
raf' by doerhood, nasb by likeness to the object (definite) or as tamyiz (indefinite), jarr by annexation; the two barred cases with
their reasons; and the Basran-Kufan split over حَسَنُ وَجْهِهِ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~261-266 of the transcription.

  VERBATIM: s1. RESTORED (received matn, marked): s3, s5, s8, s9. COMMENTARY (the notebook): s2, s4, s6, s7, s10.
  The notebook's seventh pattern-word is printed صِغِرٌ; its reading is uncertain and it is HELD BACK (sixteen of the seventeen are listed);
  the notebook's شُجَاحٌ is read شُجَاعٌ (the فُعَال pattern) — both recorded in the manifest attribution.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch17.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-sifa-al-mushabbaha-fil-kafiya"
SM = "sifa-mushabbaha"
IF = "ism-fail"
TITLE = {"ar": "الصِّفَةُ الْمُشَبَّهَةُ", "en": "The ṣifa mushabbaha", "tr": "Sıfat-ı müşebbehe"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
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
def pat(full, lex, en, tr, first=False, punct=None):
    """one pattern-word of the list, cited; first stands in jarr after نَحْوُ, the rest joined"""
    if first: return cited(full, lex, "noun", ["idafa-definiteness", SM], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", en, tr, punct=punct)
    return cited_wa("وَ" + full, lex, "noun", [SM], full + " مَعْطُوفٌ.", en, tr, full, punct=punct)

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The ṣifa mushabbaha: what is derived from an intransitive verb for the one in whom the event subsists, in the sense of permanence — as in حَسَنٌ and كَرِيمٌ.",
 "tr": "Sıfat-ı müşebbehe: sübût mânâsında olmak üzere, hades kendisiyle kâim olan zât için lâzım fiilden türetilen isimdir — حَسَنٌ ve كَرِيمٌ gibi."},
 "tokens": [
  W("الصِّفَةُ", "sifa", "noun", ["mubtada-khabar", SM], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the ṣifa» — the mubtada.", "«sıfat» — mübtedâ."),
  W("الْمُشَبَّهَةُ", "mushabbaha", "noun", ["naat-sifa", SM, "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ — الْمُشَبَّهَةُ بِاسْمِ الْفَاعِلِ.", "«resembling» — resembling the ism fāʿil.", "«müşebbehe» — ism-i fâile benzeyen.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("اشْتُقَّ", "ishtaqqa", "verb", ["ism-mawsul", "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ.", "«is derived».", "«türetilen»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("فِعْلٍ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«fiil»."),
  W("لَازِمٍ", "lazim", "noun", ["naat-sifa", SM], "صِفَةٌ مَجْرُورَةٌ — غَيْرِ مُتَعَدٍّ.", "«intransitive».", "«lâzım»."),
  li_("لِمَنْ", "man", "pron", ["ism-mawsul"], "مَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«for the one who».", "«... olan için».", "مَنْ"),
  W("قَامَ", "qama", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — الْحَدَثُ.", "«subsists».", "«kâim olan»."),
  W("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«in him».", "«onunla».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ — حَالٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  W("الثُّبُوتِ", "thubut", "noun", ["idafa-definiteness", SM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ضِدُّ الْحُدُوثِ.", "«permanence» — the opposite of occurrence.", "«sübût» — hudûsun zıddı.", punct="،"),
  nahwu(),
  cited("حَسَنٍ", "hasan-adj", "noun", ["idafa-definiteness", SM], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — فَعَلٌ.", "«beautiful» — فَعَل.", "«güzel» — فَعَل."),
  cited_wa("وَكَرِيمٍ", "karim", "noun", [SM], "كَرِيمٍ مَعْطُوفٌ — فَعِيلٌ.", "«and generous» — فَعِيل.", "«ve cömert» — فَعِيل.", "كَرِيمٍ", punct="."),
 ]})

# ----------- s2 (COMMENTARY): the difference
S.append({"id": "s2", "translation": {
 "en": "And the difference between it and the ism fāʿil: the ism fāʿil is for occurrence — آكِلٌ and شَارِبٌ come and go — and the ṣifa mushabbaha for permanence — حَسَنٌ and قَبِيحٌ are fixed and do not pass." + C_EN,
 "tr": "Onunla ism-i fâil arasındaki fark: ism-i fâil hudûs içindir — آكِلٌ ve شَارِبٌ gelip geçicidir — sıfat-ı müşebbehe sübût içindir — حَسَنٌ ve قَبِيحٌ sâbittir, gelip geçici değildir." + C_TR},
 "tokens": [
  atf_wa("وَالْفَرْقُ", "farq", "noun", ["mubtada-khabar"], "الْفَرْقُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the difference».", "«ve fark».", "الْفَرْقُ"),
  W("بَيْنَهَا", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«between it».", "«onunla».", segments=[seg("بَيْنَ", "bayna", "noun"), pr3fs()]),
  atf_wa("وَبَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "بَيْنَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and».", "«ve».", "بَيْنَ"),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil».", punct=":"),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mubtada-khabar"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ الْفَرْقُ.", "«that» — the clause is the khabar.", "«... olmasıdır» — cümle haber."),
  W("اسْمَ", "ism", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  li_("لِلْحُدُوثِ", "huduth", "noun", ["inna-wa-akhawatuha", IF], "الْحُدُوثِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«is for occurrence».", "«hudûs içindir».", "الْحُدُوثِ", segs=[seg("لِ", "li", "prep"), seg("لْحُدُوثِ", "huduth", "noun")]),
  nahwu(),
  cited("آكِلٍ", "akil", "noun", ["idafa-definiteness", IF], "فِي مَحَلِّ جَرٍّ — اسْمُ فَاعِلٍ.", "«eating».", "«yiyen»."),
  cited_wa("وَشَارِبٍ", "sharib", "noun", [IF], "شَارِبٍ مَعْطُوفٌ.", "«and drinking».", "«ve içen».", "شَارِبٍ", punct="،"),
  atf_wa("وَالصِّفَةَ", "sifa", "noun", ["inna-wa-akhawatuha", SM], "الصِّفَةَ مَعْطُوفٌ عَلَى اسْمِ أَنَّ مَنْصُوبٌ.", "«and the ṣifa».", "«ve sıfat-ı».", "الصِّفَةَ"),
  W("الْمُشَبَّهَةَ", "mushabbaha", "noun", ["naat-sifa", SM], "صِفَةٌ مَنْصُوبَةٌ.", "«mushabbaha».", "«müşebbehe»."),
  li_("لِلثُّبُوتِ", "thubut", "noun", ["inna-wa-akhawatuha", SM], "الثُّبُوتِ مَجْرُورٌ — خَبَرٌ.", "«is for permanence».", "«sübût içindir».", "الثُّبُوتِ", segs=[seg("لِ", "li", "prep"), seg("لثُّبُوتِ", "thubut", "noun")]),
  nahwu(),
  cited("حَسَنٍ", "hasan-adj", "noun", ["idafa-definiteness", SM], "فِي مَحَلِّ جَرٍّ.", "«beautiful».", "«güzel»."),
  cited_wa("وَقَبِيحٍ", "qabih", "noun", [SM], "قَبِيحٍ مَعْطُوفٌ.", "«and ugly».", "«ve çirkin».", "قَبِيحٍ", punct="."),
 ]})

# ----------- s3 (RESTORED): the heard shape
S.append({"id": "s3", "translation": {
 "en": "And its heard shape differs from the shape of the ism fāʿil — as in حَسَنٌ, صَعْبٌ and شَدِيدٌ." + R_EN,
 "tr": "Semâî sîgası ism-i fâilin sîgasına muhâliftir — حَسَنٌ، صَعْبٌ ve شَدِيدٌ gibi." + R_TR},
 "tokens": [
  atf_wa("وَصِيغَتُهَا", "sigha", "noun", ["mubtada-khabar", "idafa-definiteness"], "صِيغَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its shape».", "«ve sîgası».", "صِيغَتُ", extra_segs=[seg("صِيغَتُ", "sigha", "noun"), pr3fs()]),
  W("السَّمَاعِيَّةُ", "samai", "noun", ["naat-sifa", SM], "صِفَةٌ مَرْفُوعَةٌ.", "«heard».", "«semâî»."),
  W("مُخَالِفَةٌ", "mukhalif", "noun", ["mubtada-khabar", IF], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ عَامِلٌ.", "«differs» — a working participle.", "«muhâliftir» — amel eden ism-i fâil."),
  li_("لِصِيغَةِ", "sigha", "noun", ["idafa-definiteness"], "صِيغَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«from the shape of».", "«sîgasına».", "صِيغَةِ"),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâilin».", punct="،"),
  nahwu(),
  pat("حَسَنٍ", "hasan-adj", "«beautiful» — فَعَل.", "«güzel» — فَعَل.", first=True),
  pat("صَعْبٍ", "sab", "«hard» — فَعْل.", "«zor» — فَعْل."),
  pat("شَدِيدٍ", "shadid", "«strong» — فَعِيل.", "«şiddetli» — فَعِيل.", punct="."),
 ]})

# ----------- s4 (COMMENTARY): the notebook's patterns
S.append({"id": "s4", "translation": {
 "en": "And its patterns are seventeen, none of them فَاعِلٌ — as in شَكْسٌ, صُلْبٌ, مِلْحٌ, حَسَنٌ, خَشِنٌ, عَجُلٌ, جُنُبٌ, جَبَانٌ, شُجَاعٌ, شَيْظَمٌ, جَيِّدٌ, حَرِيصٌ, سَلِيمٌ, غَيُورٌ, أَبْلَجُ and غَضْبَانُ." + C_EN + " (Sixteen of the notebook's seventeen are given; the seventh as printed is held back pending review.)",
 "tr": "Vezinleri on yedidir, hiçbiri فَاعِلٌ değildir — شَكْسٌ، صُلْبٌ، مِلْحٌ، حَسَنٌ، خَشِنٌ، عَجُلٌ، جُنُبٌ، جَبَانٌ، شُجَاعٌ، شَيْظَمٌ، جَيِّدٌ، حَرِيصٌ، سَلِيمٌ، غَيُورٌ، أَبْلَجُ ve غَضْبَانُ gibi." + C_TR + " (Defterin on yedisinden on altısı verilmiştir; yedincisi basıldığı hâliyle inceleme beklemektedir.)"},
 "tokens": [
  atf_wa("وَأَوْزَانُهَا", "wazn", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "أَوْزَانُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its patterns».", "«ve vezinleri».", "أَوْزَانُ", extra_segs=[seg("أَوْزَانُ", "wazn", "noun"), pr3fs()]),
  W("سَبْعَةَ", "saba-seven", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "خَبَرٌ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ.", "«seventeen» — built on the fatḥa of both parts.", "«on yedi» — iki cüz'ün fethası üzere mebnî."),
  W("عَشَرَ", "ashar", "noun", ["asma-al-adad-fil-kafiya"], "الْجُزْءُ الثَّانِي مِنَ الْمُرَكَّبِ الْعَدَدِيِّ.", "— the second part.", "— ikinci cüz."),
  W("وَزْنًا", "wazn", "noun", ["tamyiz", "asma-al-adad-fil-kafiya"], "تَمْيِيزٌ مَنْصُوبٌ.", "«patterns».", "«vezin».", punct="،"),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«there is not».", "«yoktur»."),
  W("فِيهَا", "fi", "prep", ["huruf-jarr", "kana-wa-akhawatuha"], "فِي حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَيْسَ مُقَدَّمٌ.", "«among them».", "«onlarda».", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  cited("فَاعِلٌ", "fail-doer", "noun", ["kana-wa-akhawatuha", IF], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ — الْوَزْنُ.", "«fāʿil» — the pattern.", "«fâil» — vezin.", punct="،"),
  nahwu(),
  pat("شَكْسٍ", "shaks", "«ill-tempered» — فَعْل.", "«huysuz» — فَعْل.", first=True),
  pat("صُلْبٍ", "sulb-hard", "«hard» — فُعْل.", "«sert» — فُعْل."),
  pat("مِلْحٍ", "milh", "«salty, comely» — فِعْل.", "«tuzlu, güzel» — فِعْل."),
  pat("حَسَنٍ", "hasan-adj", "«beautiful» — فَعَل.", "«güzel» — فَعَل."),
  pat("خَشِنٍ", "khashin", "«rough» — فَعِل.", "«kaba» — فَعِل."),
  pat("عَجُلٍ", "ajul", "«hasty» — فَعُل.", "«aceleci» — فَعُل."),
  pat("جُنُبٍ", "junub", "«a stranger; ritually impure» — فُعُل.", "«yabancı; cünüp» — فُعُل."),
  pat("جَبَانٍ", "jaban", "«cowardly» — فَعَال.", "«korkak» — فَعَال."),
  pat("شُجَاعٍ", "shuja", "«brave» — فُعَال.", "«cesur» — فُعَال."),
  pat("شَيْظَمٍ", "shayzam", "«tall and sturdy» — فَيْعَل.", "«uzun boylu, gürbüz» — فَيْعَل."),
  pat("جَيِّدٍ", "jayyid", "«good» — فَيْعِل.", "«iyi» — فَيْعِل."),
  pat("حَرِيصٍ", "haris", "«eager» — فَعِيل.", "«hırslı» — فَعِيل."),
  pat("سَلِيمٍ", "salim-sound", "«sound» — فَعِيل.", "«sağlam» — فَعِيل."),
  pat("غَيُورٍ", "ghayur", "«jealous» — فَعُول.", "«kıskanç» — فَعُول."),
  cited_wa("وَأَبْلَجَ", "ablaj", "noun", [SM, "mamnu-min-sarf"], "أَبْلَجَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ — أَفْعَلُ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«bright-browed» — أَفْعَل, a diptote.", "«açık alınlı» — أَفْعَل, gayr-i munsarif.", "أَبْلَجَ"),
  cited_wa("وَغَضْبَانَ", "ghadban", "noun", [SM, "mamnu-min-sarf"], "غَضْبَانَ مَعْطُوفٌ مَجْرُورٌ بِالْفَتْحَةِ — فَعْلَانُ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«angry» — فَعْلَان, a diptote.", "«öfkeli» — فَعْلَان, gayr-i munsarif.", "غَضْبَانَ", punct="."),
 ]})

# ----------- s5 (RESTORED): government
S.append({"id": "s5", "translation": {
 "en": "And it governs as its verb governs: it raises a doer when its conditions are found." + R_EN,
 "tr": "Fiilinin ameli gibi amel eder: şartları bulunduğunda fâili ref' eder." + R_TR},
 "tokens": [
  atf_wa("وَتَعْمَلُ", "amila", "verb", ["fail", SM], "تَعْمَلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and it governs».", "«ve amel eder».", "تَعْمَلُ"),
  W("عَمَلَ", "amal-work", "noun", ["maful-mutlaq", "idafa-definiteness"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«as … governs».", "«ameli gibi»."),
  W("فِعْلِهَا", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its verb».", "«fiilinin».", punct=":", segments=[seg("فِعْلِ", "fil", "noun"), pr3fs()]),
  W("فَتَرْفَعُ", "rafaa", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَرْفَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«so it raises».", "«ref' eder».", segments=[seg("فَ", "fa", "conj"), seg("تَرْفَعُ", "rafaa", "verb")]),
  W("الْفَاعِلَ", "fail-doer", "noun", ["maful-bihi", SM], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a doer».", "«fâili»."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("وُجِدَتْ", "wajada", "verb", ["naib-al-fail", "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«are found».", "«bulunursa»."),
  W("شُرُوطُهَا", "shart", "noun", ["naib-al-fail", "idafa-definiteness", "shurut-amal-ism-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — شُرُوطُ اسْمِ الْفَاعِلِ.", "«its conditions» — the ism fāʿil's.", "«şartları» — ism-i fâilin şartları.", punct=".", segments=[seg("شُرُوطُ", "shart", "noun"), pr3fs()]),
 ]})

# ----------- s6 (COMMENTARY): two states, three states
S.append({"id": "s6", "translation": {
 "en": "And it has two states — defined by the lām, as الْحَسَنُ, or bare of it, as حَسَنٌ — and its governed word has three: defined by the lām, as الْوَجْهُ; annexed to the pronoun, as وَجْهُهُ; or bare of both, as وَجْهٌ." + C_EN,
 "tr": "Onun iki hâli vardır — lâm ile ma'rife, الْحَسَنُ gibi; lâmdan mücerred, حَسَنٌ gibi — ve ma'mûlünün üç hâli: lâm ile ma'rife, الْوَجْهُ gibi; zamire muzâf, وَجْهُهُ gibi; ikisinden de mücerred, وَجْهٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَلَهَا", "li", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and it has».", "«ve onun ... vardır».", "لَ", extra_segs=[seg("لَ", "li", "prep"), pr3fs()]),
  W("حَالَانِ", "hal-state", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two states».", "«iki hâl».", punct=":"),
  W("مُعَرَّفَةٌ", "muarraf", "noun", ["badal", "ism-maful"], "بَدَلٌ مِنْ حَالَانِ مَرْفُوعٌ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«defined».", "«ma'rife»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", [], "اللَّامِ مَجْرُورٌ.", "«by the lām».", "«lâm ile».", "اللَّامِ"),
  nahwu(),
  cited("الْحَسَنُ", "hasan-adj", "noun", ["idafa-definiteness", SM], "فِي مَحَلِّ جَرٍّ.", "«al-ḥasan».", "«el-hasen».", punct="،"),
  atf_wa("وَمُجَرَّدَةٌ", "mujarrad", "noun", ["badal", "ism-maful"], "مُجَرَّدَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«or bare».", "«ve mücerred».", "مُجَرَّدَةٌ"),
  W("مِنْهَا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — اللَّامُ.", "«of it».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  nahwu(),
  cited("حَسَنٌ", "hasan-adj", "noun", ["idafa-definiteness", SM], "فِي مَحَلِّ جَرٍّ.", "«ḥasan».", "«hasen».", punct="؛"),
  atf_wa("وَلِمَعْمُولِهَا", "mamul", "noun", ["huruf-jarr", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَمَعْمُولِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«and its governed word has».", "«ve ma'mûlünün ... vardır».", "لِ", extra_segs=[seg("لِ", "li", "prep"), seg("مَعْمُولِ", "mamul", "noun"), pr3fs()]),
  W("ثَلَاثَةُ", "thalatha", "noun", ["mubtada-khabar", "idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«three».", "«üç»."),
  W("أَحْوَالٍ", "hal-state", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«states».", "«hâli».", punct=":"),
  W("مُعَرَّفٌ", "muarraf", "noun", ["badal", "ism-maful"], "بَدَلٌ مَرْفُوعٌ.", "«defined».", "«ma'rife»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", [], "اللَّامِ مَجْرُورٌ.", "«by the lām».", "«lâm ile».", "اللَّامِ"),
  nahwu(),
  cited("الْوَجْهُ", "wajh", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ.", "«the face».", "«yüz».", punct="؛"),
  atf_wa("وَمُضَافٌ", "mudaf", "noun", ["badal", "ism-maful"], "مُضَافٌ مَعْطُوفٌ مَرْفُوعٌ.", "«annexed».", "«ve muzâf».", "مُضَافٌ"),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الضَّمِيرِ", "damir", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the pronoun».", "«zamire»."),
  nahwu(),
  cited("وَجْهُهُ", "wajh", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his face».", "«yüzü».", punct="؛", segments=[seg("وَجْهُ", "wajh", "noun"), pr3ms()]),
  atf_wa("وَمُجَرَّدٌ", "mujarrad", "noun", ["badal", "ism-maful"], "مُجَرَّدٌ مَعْطُوفٌ مَرْفُوعٌ.", "«or bare».", "«ve mücerred».", "مُجَرَّدٌ"),
  W("مِنْهُمَا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ.", "«of both».", "«ikisinden».", segments=[seg("مِنْ", "min", "prep"), pr3d()]),
  nahwu(),
  cited("وَجْهٌ", "wajh", "noun", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ.", "«a face».", "«bir yüz».", punct="."),
 ]})

# ----------- s7 (COMMENTARY): six, eighteen
S.append({"id": "s7", "translation": {
 "en": "So from two multiplied by three come six cases; and every governed word may be marfūʿ, manṣūb or majrūr, so from six multiplied by three come eighteen cases." + C_EN,
 "tr": "İkinin üçle çarpımından altı mesele çıkar; her ma'mûl merfû, mansûb veya mecrûr olabilir, altının üçle çarpımından da on sekiz mesele çıkar." + C_TR},
 "tokens": [
  W("فَمِنْ", "min", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَمِنْ حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«so from».", "«o hâlde ... -den».", segments=[seg("فَ", "fa", "conj"), seg("مِنْ", "min", "prep")]),
  W("ضَرْبِ", "darb", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ — الضَّرْبُ الْحِسَابِيُّ.", "«the multiplying of».", "«çarpımından»."),
  W("الِاثْنَيْنِ", "ithnan", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two».", "«ikinin»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«ile»."),
  W("الثَّلَاثَةِ", "thalatha", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«three».", "«üç»."),
  W("سِتُّ", "sitt", "noun", ["mubtada-khabar", "idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«six».", "«altı»."),
  W("مَسَائِلَ", "masala", "noun", ["idafa-definiteness", "mamnu-min-sarf", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«cases» — a diptote plural.", "«mesele» — gayr-i munsarif cemi.", punct="؛"),
  atf_wa("وَكُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "كُلُّ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and every».", "«ve her».", "كُلُّ"),
  W("مَعْمُولٍ", "mamul", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«governed word».", "«ma'mûl»."),
  W("يَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كُلُّ.", "«may be».", "«olabilir»."),
  W("مَرْفُوعًا", "marfu", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُونُ مَنْصُوبٌ.", "«marfūʿ».", "«merfû»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("مَنْصُوبًا", "mansub", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«manṣūb».", "«mansûb»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("مَجْرُورًا", "majrur", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«majrūr».", "«mecrûr».", punct="،"),
  W("فَمِنْ", "min", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَمِنْ حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«so from».", "«-den».", segments=[seg("فَ", "fa", "conj"), seg("مِنْ", "min", "prep")]),
  W("ضَرْبِ", "darb", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the multiplying of».", "«çarpımından»."),
  W("السِّتَّةِ", "sitta", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«six».", "«altının»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«ile»."),
  W("الثَّلَاثَةِ", "thalatha", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«three».", "«üçle»."),
  W("ثَمَانِيَ", "thamaniya", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "مُبْتَدَأٌ مُؤَخَّرٌ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ رَفْعٍ.", "«eighteen».", "«on sekiz»."),
  W("عَشْرَةَ", "ashara", "noun", ["asma-al-adad-fil-kafiya"], "الْجُزْءُ الثَّانِي مِنَ الْمُرَكَّبِ.", "— the second part.", "— ikinci cüz."),
  W("مَسْأَلَةً", "masala", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«cases».", "«mesele».", punct="."),
 ]})

# ----------- s8 (RESTORED): the three cases and their grounds
S.append({"id": "s8", "translation": {
 "en": "So rafʿ is by doerhood; naṣb by likeness to the object in the definite, and as tamyīz in the indefinite; and jarr by annexation." + R_EN,
 "tr": "Ref' fâillik üzeredir; nasb, ma'rifede mef'ûle teşbîh, nekrede temyiz üzeredir; cer izâfet üzeredir." + R_TR},
 "tokens": [
  W("فَالرَّفْعُ", "raf", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالرَّفْعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the rafʿ».", "«ref'».", segments=[seg("فَ", "fa", "conj"), seg("الرَّفْعُ", "raf", "noun")]),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is by».", "«üzeredir»."),
  W("الْفَاعِلِيَّةِ", "failiyya", "noun", ["huruf-jarr", SM], "مَجْرُورٌ.", "«doerhood».", "«fâillik».", punct="؛"),
  atf_wa("وَالنَّصْبُ", "nasb", "noun", ["mubtada-khabar"], "النَّصْبُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the naṣb».", "«ve nasb».", "النَّصْبُ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ.", "«by».", "«üzere»."),
  W("التَّشْبِيهِ", "tashbih", "noun", ["huruf-jarr", SM], "مَجْرُورٌ.", "«likeness».", "«teşbîh»."),
  bi_("بِالْمَفْعُولِ", "maful-noun", "noun", [SM], "الْمَفْعُولِ مَجْرُورٌ.", "«to the object».", "«mef'ûle».", "الْمَفْعُولِ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمَعْرِفَةِ", "marifa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the definite».", "«ma'rife»."),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ.", "«and as».", "«ve ... üzere».", "عَلَى"),
  W("التَّمْيِيزِ", "tamyiz-noun", "noun", ["huruf-jarr", "tamyiz"], "مَجْرُورٌ.", "«tamyīz».", "«temyiz»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("النَّكِرَةِ", "nakira", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the indefinite».", "«nekre».", punct="؛"),
  atf_wa("وَالْجَرُّ", "jarr", "noun", ["mubtada-khabar"], "الْجَرُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the jarr».", "«ve cer».", "الْجَرُّ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ.", "«by».", "«üzeredir»."),
  W("الْإِضَافَةِ", "idafa", "noun", ["huruf-jarr", "idafa-lafziyya"], "مَجْرُورٌ.", "«annexation».", "«izâfet».", punct="."),
 ]})

# ----------- s9 (RESTORED): the two barred cases
S.append({"id": "s9", "translation": {
 "en": "And of them الْحَسَنُ وَجْهِهِ is barred, because the lafẓī annexation yields no lightness, and الْحَسَنُ وَجْهٍ, because a definite noun is not annexed to an indefinite." + R_EN,
 "tr": "Onlardan الْحَسَنُ وَجْهِهِ mümteni'dir, çünkü lafzî izâfet hafiflik ifade etmez; الْحَسَنُ وَجْهٍ de mümteni'dir, çünkü ma'rife nekreye muzâf olmaz." + R_TR},
 "tokens": [
  atf_wa("وَيَمْتَنِعُ", "imtanaa", "verb", ["fail", "form-viii-verbs"], "يَمْتَنِعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is barred».", "«ve mümteni'dir».", "يَمْتَنِعُ"),
  W("مِنْهَا", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ.", "«of them».", "«onlardan».", segments=[seg("مِنْ", "min", "prep"), pr3fs()]),
  cited("الْحَسَنُ", "hasan-adj", "noun", ["fail", SM, "idafa-lafziyya"], "فِي مَحَلِّ رَفْعٍ فَاعِلٌ — الْجُمْلَةُ الْمَحْكِيَّةُ.", "«al-ḥasanu» — the cited phrase is the doer.", "«el-hasenü» — hikâye edilen ibare fâil."),
  cited("وَجْهِهِ", "wajh", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — دَاخِلَ الْمَحْكِيِّ.", "«wajhihi».", "«vechihî».", punct="،", segments=[seg("وَجْهِ", "wajh", "noun"), pr3msi()]),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الْإِضَافَةَ", "idafa", "noun", ["inna-wa-akhawatuha", "idafa-lafziyya"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the annexation».", "«izâfet»."),
  W("اللَّفْظِيَّةَ", "lafzi", "noun", ["naat-sifa", "idafa-lafziyya"], "صِفَةٌ مَنْصُوبَةٌ.", "«lafẓī».", "«lafzî»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-mez»."),
  W("تُفِدْ", "afada", "verb", ["nawasib-wa-jawazim-al-mudari", "inna-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«yields» — the hollow verb's ʿayn dropped.", "«ifade eder» — ecvefin aynı düşmüş."),
  W("تَخْفِيفًا", "takhfif", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«lightness».", "«hafiflik».", punct="،"),
  cited_wa("وَالْحَسَنُ", "hasan-adj", "noun", ["fail", SM, "idafa-lafziyya"], "الْحَسَنُ مَعْطُوفٌ — الْجُمْلَةُ الثَّانِيَةُ الْمَحْكِيَّةُ.", "«and al-ḥasanu».", "«ve el-hasenü».", "الْحَسَنُ"),
  cited("وَجْهٍ", "wajh", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — دَاخِلَ الْمَحْكِيِّ.", "«wajhin».", "«vechin».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الْمَعْرِفَةَ", "marifa", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«a definite noun».", "«ma'rife»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mez»."),
  W("تُضَافُ", "adafa", "verb", ["naib-al-fail", "inna-wa-akhawatuha", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«is annexed».", "«muzâf olur»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("النَّكِرَةِ", "nakira", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«an indefinite».", "«nekreye».", punct="."),
 ]})

# ----------- s10 (COMMENTARY): the Basran–Kufan split
S.append({"id": "s10", "translation": {
 "en": "And حَسَنُ وَجْهِهِ is disputed: for Sībawayh and the Basrans it is permitted in the necessity of verse, with ugliness, since dropping the pronoun lightens nothing further; for the Kufans it is permitted without ugliness, since lightness is gained by dropping the tanwīn." + C_EN,
 "tr": "حَسَنُ وَجْهِهِ ihtilâflıdır: Sîbeveyh ve Basralılara göre şiir zaruretinde, çirkinlikle birlikte câizdir, çünkü zamirin hazfi daha fazla hafiflik sağlamaz; Kûfelilere göre çirkinlik olmaksızın câizdir, çünkü tenvinin hazfiyle hafiflik hâsıl olur." + C_TR},
 "tokens": [
  atf_wa("وَاخْتُلِفَ", "ikhtalafa", "verb", ["naib-al-fail", "form-viii-verbs"], "اخْتُلِفَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«and it is disputed».", "«ve ihtilâf edildi».", "اخْتُلِفَ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«hakkında»."),
  cited("حَسَنُ", "hasan-adj", "noun", ["huruf-jarr", SM, "idafa-lafziyya"], "فِي مَحَلِّ جَرٍّ — الْجُمْلَةُ الْمَحْكِيَّةُ.", "«ḥasanu».", "«hasenü»."),
  cited("وَجْهِهِ", "wajh", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«wajhihi».", "«vechihî».", punct=":", segments=[seg("وَجْهِ", "wajh", "noun"), pr3msi()]),
  W("فَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَهُوَ مُبْتَدَأٌ.", "«it is».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  W("جَائِزٌ", "jaiz", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«permitted».", "«câizdir»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ.", "«Sībawayh».", "«Sîbeveyh»."),
  atf_wa("وَالْبَصْرِيِّينَ", "basri", "noun", ["jam-mudhakkar-salim"], "الْبَصْرِيِّينَ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ.", "«and the Basrans».", "«ve Basralılara».", "الْبَصْرِيِّينَ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("ضَرُورَةِ", "darura", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the necessity of».", "«zaruretinde»."),
  W("الشِّعْرِ", "shir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verse».", "«şiir»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("الْقُبْحِ", "qubh", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ugliness».", "«çirkinlik».", punct="،"),
  W("إِذْ", "idh", "part", ["maful-fih"], "حَرْفٌ لِلتَّعْلِيلِ.", "«since».", "«çünkü»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  W("يُفِيدُ", "afada", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«yields».", "«sağlar»."),
  W("حَذْفُ", "hadhf", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the dropping of».", "«hazfi»."),
  W("الضَّمِيرِ", "damir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the pronoun».", "«zamirin»."),
  W("تَخْفِيفًا", "takhfif", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«lightness».", "«hafiflik»."),
  W("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "صِفَةٌ مَنْصُوبَةٌ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«further».", "«başka».", punct="؛"),
  atf_wa("وَجَائِزٌ", "jaiz", "noun", ["mubtada-khabar"], "جَائِزٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَهُوَ.", "«and permitted».", "«ve câizdir».", "جَائِزٌ"),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْكُوفِيِّينَ", "kufi", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Kufans».", "«Kûfelilere»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا بِمَعْنَى غَيْرٍ مَجْرُورٌ بِالْبَاءِ.", "«without».", "«-sız».", "لَا"),
  W("قُبْحٍ", "qubh", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«ugliness».", "«çirkinlik».", punct="،"),
  li_("لِحُصُولِ", "husul", "noun", ["idafa-definiteness"], "حُصُولِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«since … is gained».", "«hâsıl olduğundan».", "حُصُولِ"),
  W("التَّخْفِيفِ", "takhfif", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«lightness».", "«hafiflik»."),
  bi_("بِحَذْفِ", "hadhf", "noun", ["idafa-definiteness"], "حَذْفِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by dropping».", "«hazfiyle».", "حَذْفِ"),
  W("التَّنْوِينِ", "tanwin", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tanwīn».", "«tenvinin».", punct="."),
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
 "farq": need("farq", "فَرْق", "ف ر ق", "noun", "a difference", "fark", 2),
 "sharib": need("sharib", "شَارِب", "ش ر ب", "noun", "drinking, a drinker — the ism fāʿil of شَرِبَ", "içen — şeribe'nin ism-i fâili", 2),
 "shaks": need("shaks", "شَكْس", "ش ك س", "noun", "ill-tempered, contrary — a ṣifa mushabbaha on فَعْل", "huysuz, aksi — فَعْل vezninde sıfat-ı müşebbehe", 6),
 "sulb-hard": need("sulb-hard", "صُلْب", "ص ل ب", "noun", "hard, firm — a ṣifa mushabbaha on فُعْل", "sert, katı — فُعْل vezninde sıfat-ı müşebbehe", 4),
 "khashin": need("khashin", "خَشِن", "خ ش ن", "noun", "rough, coarse — a ṣifa mushabbaha on فَعِل", "kaba, pürüzlü — فَعِل vezninde sıfat-ı müşebbehe", 4),
 "ajul": need("ajul", "عَجُل", "ع ج ل", "noun", "hasty — a ṣifa mushabbaha on فَعُل", "aceleci — فَعُل vezninde sıfat-ı müşebbehe", 5),
 "junub": need("junub", "جُنُب", "ج ن ب", "noun", "a stranger; one in major ritual impurity — a ṣifa mushabbaha on فُعُل", "yabancı; cünüp — فُعُل vezninde sıfat-ı müşebbehe", 5),
 "shayzam": need("shayzam", "شَيْظَم", "ش ظ م", "noun", "tall and sturdy (of a horse or man) — a ṣifa mushabbaha on فَيْعَل", "uzun boylu, gürbüz — فَيْعَل vezninde sıfat-ı müşebbehe", 6),
 "ablaj": need("ablaj", "أَبْلَج", "ب ل ج", "noun", "bright-browed, clear — a ṣifa mushabbaha on أَفْعَل, a diptote", "açık alınlı, aydınlık — أَفْعَل vezninde sıfat-ı müşebbehe, gayr-i munsarif", 6),
 "qubh": need("qubh", "قُبْح", "ق ب ح", "noun", "ugliness — of a construction the grammarians tolerate but dislike", "çirkinlik — nahivcilerin hoş görmeyip izin verdiği bir yapı için", 4),
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
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch17 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الصِّفَةُ الْمُشَبَّهَةُ فِي الْكَافِيَةِ", "en": "The ṣifa mushabbaha in the Kafiya: permanence against occurrence, the heard patterns, its government, and the eighteen cases of حَسَنُ الْوَجْهِ with the two that are barred", "tr": "Kâfiye'de sıfat-ı müşebbehe: sübût ile hudûs, semâî vezinler, ameli ve حَسَنُ الْوَجْهِ'nin on sekiz meselesiyle mümteni' olan ikisi"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الصفة المشبهة: ما اشتق من فعل لازم لمن قام به بمعنى الثبوت؛ صيغتها السماعية مخالفة لصيغة اسم الفاعل؛ عملها عمل فعلها؛ الرفع على الفاعلية والنصب على التشبيه بالمفعول في المعرفة والتمييز في النكرة والجر على الإضافة؛ يمتنع الحسن وجهه والحسن وجه", "ضياء صونغور اوغلى — دفتر الكافية: الفرق بين الحدوث والثبوت؛ سبعة عشر وزنا؛ حالان للصفة وثلاثة للمعمول: ست مسائل في ثلاثة أوجه ثماني عشرة؛ خلاف سيبويه والكوفيين في حَسَنُ وَجْهِهِ"],
 "question": {
  "en": ["What is a ṢIFA MUSHABBAHA? A noun derived from an intransitive verb for the one in whom the quality subsists PERMANENTLY — حَسَن is beautiful by nature, كَرِيم generous by nature. The ism fāʿil says the same of a passing state: آكِل is eating now. One word in the two definitions, حُدُوث against ثُبُوت, is the whole difference.",
         "What does it look like? Anything but فَاعِل. The shapes are heard, not derived: شَكْس، صُلْب، مِلْح، حَسَن، خَشِن، عَجُل، جُنُب، جَبَان، شُجَاع، شَيْظَم، جَيِّد، حَرِيص، سَلِيم، غَيُور، أَبْلَج، غَضْبَان — the notebook counts seventeen patterns and the last two are diptotes.",
         "Does it govern? Like its intransitive verb, under the ism fāʿil's conditions: it raises a doer (زَيْدٌ حَسَنٌ وَجْهُهُ — the face is the doer). Having no object, it has no object to take; what it does instead is the chapter's real subject.",
         "What are the EIGHTEEN cases? The ṣifa is either with the article (الْحَسَنُ) or bare (حَسَنٌ): two. Its governed noun is with the article (الْوَجْه), annexed to a pronoun (وَجْهُهُ), or bare (وَجْه): three. Two by three is six, and each of the six may stand in rafʿ, naṣb or jarr: eighteen.",
         "What justifies each case? Rafʿ as the doer (حَسَنٌ وَجْهُهُ); naṣb as a likeness to the object when the noun is definite (حَسَنٌ وَجْهَهُ) and as a tamyīz when it is indefinite (حَسَنٌ وَجْهًا); jarr by annexation (حَسَنُ الْوَجْهِ، حَسَنُ وَجْهٍ).",
         "Which two are BARRED? الْحَسَنُ وَجْهِهِ, because annexing the al-ṣifa to a pronoun-bearing noun lightens nothing (a lafẓī annexation exists only to drop a tanwīn, and الْحَسَنُ has none); and الْحَسَنُ وَجْهٍ, because a definite noun is never annexed to an indefinite. حَسَنُ وَجْهِهِ is a third, disputed case: the Basrans allow it in verse and call it ugly, the Kufans allow it outright.",
         "What does the engine do? The IsmTagger's ROLES list returns «ṣifa mushabbaha» beside «intensive» for فَعِيل — the ambiguity the chapter teaches — and the IlalEngine refuses to turn the weak letter of a colour or a defect on أَفْعَل, the very class the next chapter will bar from the elative."],
  "tr": ["SIFAT-I MÜŞEBBEHE nedir? Vasfın kendisinde SÜREKLİ bulunduğu zât için lâzım fiilden türetilen isim — حَسَن tabiatıyla güzel, كَرِيم tabiatıyla cömerttir. İsm-i fâil aynı şeyi geçici bir hâl için söyler: آكِل şu an yiyen. İki tarifteki tek kelime, حُدُوث'a karşı ثُبُوت, farkın tamamıdır.",
         "Neye benzer? فَاعِل dışında her şeye. Biçimler semâîdir, türetilmez: شَكْس، صُلْب، مِلْح، حَسَن، خَشِن، عَجُل، جُنُب، جَبَان، شُجَاع، شَيْظَم، جَيِّد، حَرِيص، سَلِيم، غَيُور، أَبْلَج، غَضْبَان — defter on yedi vezin sayar ve son ikisi gayr-i munsariftir.",
         "Amel eder mi? Lâzım fiili gibi, ism-i fâilin şartlarıyla: bir fâil ref' eder (زَيْدٌ حَسَنٌ وَجْهُهُ — yüz fâildir). Mef'ûlü olmadığından alacak mef'ûlü yoktur; onun yerine yaptığı şey bâbın asıl konusudur.",
         "ON SEKİZ mesele nedir? Sıfat ya lâmlıdır (الْحَسَنُ) ya çıplak (حَسَنٌ): iki. Ma'mûlü lâmlı (الْوَجْه), zamire muzâf (وَجْهُهُ) ya da çıplaktır (وَجْه): üç. İki kere üç altı; altının her biri ref', nasb ya da cerde olabilir: on sekiz.",
         "Her hâli ne haklı çıkarır? Fâil olarak ref' (حَسَنٌ وَجْهُهُ); isim ma'rife ise mef'ûle benzetilerek nasb (حَسَنٌ وَجْهَهُ), nekre ise temyiz olarak (حَسَنٌ وَجْهًا); izâfetle cer (حَسَنُ الْوَجْهِ، حَسَنُ وَجْهٍ).",
         "Hangi ikisi MÜMTENİ'dir? الْحَسَنُ وَجْهِهِ, çünkü lâmlı sıfatı zamirli isme muzâf etmek hiçbir şeyi hafifletmez (lafzî izâfet yalnız bir tenvin düşürmek için vardır, الْحَسَنُ'nün tenvini yoktur); ve الْحَسَنُ وَجْهٍ, çünkü ma'rife nekreye muzâf olmaz. حَسَنُ وَجْهِهِ üçüncü, ihtilâflı bir hâldir: Basralılar şiirde izin verir ve çirkin der, Kûfeliler doğrudan izin verir.",
         "Motor ne yapar? IsmTagger'ın ROLES listesi فَعِيل için «mübâlağa»nın yanına «sıfat-ı müşebbehe»yi koyar — bâbın öğrettiği belirsizlik — ve IlalEngine, bir sonraki bâbın ism-i tafdîlden men edeceği sınıf olan أَفْعَل veznindeki renk ve kusurun illetli harfini çevirmeyi reddeder."]},
 "plain": {
  "en": "A ṣifa mushabbaha is an adjective that names a lasting quality (حَسَن «beautiful», كَرِيم «generous»), unlike a participle that names a passing act. It can take a «doer» (his face is beautiful) in three cases, and the chapter counts all eighteen combinations, two of which Arabic refuses.",
  "tr": "Sıfat-ı müşebbehe kalıcı bir niteliği adlandıran sıfattır (حَسَن «güzel», كَرِيم «cömert»); geçici bir işi adlandıran ism-i fâilden farklıdır. Üç hâlde bir «fâil» alabilir (yüzü güzel) ve bâb on sekiz bileşimin hepsini sayar; ikisini Arapça reddeder."},
 "explanation": {
  "en": "The chapter is built on a single opposition. The ism fāʿil was defined «in the sense of occurrence»; the ṣifa mushabbaha is defined word for word the same way with «permanence» in that slot and «intransitive» added to the verb — a quality that lasts has nothing to act on. The notebook makes the contrast concrete (آكِل، شَارِب against حَسَن، قَبِيح) and then observes that the shapes are heard: none of the seventeen patterns is فَاعِل, which is exactly why the ism fāʿil's shape could be given as a rule and this one cannot. Government follows the ism fāʿil's conditions, but a ṣifa with no object has to do something else with the noun that follows it, and the rest of the chapter is a grid: the ṣifa with or without the article, the noun with the article, with a pronoun, or bare, and each of the six in three cases. The grounds are the standard ones — rafʿ because the noun is the doer, naṣb either as a likeness to the object (when definite) or as a tamyīz (when indefinite), jarr by annexation — and the point of counting to eighteen is to find the two cells that are empty. The al-ṣifa may not annex a noun carrying the pronoun that already refers back, because a lafẓī annexation earns its keep by dropping a tanwīn and الْحَسَنُ has none to drop; and no definite noun is annexed to an indefinite one, whatever the lightness. The third, حَسَنُ وَجْهِهِ, is where the two schools part — a reading the notebook reports rather than resolves, which is why the chapter reports it the same way.",
  "tr": "Bâb tek bir karşıtlık üzerine kurulur. İsm-i fâil «hudûs mânâsında» tarif edilmişti; sıfat-ı müşebbehe kelimesi kelimesine aynı biçimde, o yere «sübût» konarak ve fiile «lâzım» eklenerek tarif edilir — kalıcı bir niteliğin etkileyeceği bir şey yoktur. Defter karşıtlığı somutlaştırır (آكِل، شَارِب'e karşı حَسَن، قَبِيح) ve sonra biçimlerin semâî olduğunu gözler: on yedi veznin hiçbiri فَاعِل değildir; ism-i fâilin sîgasının kural olarak verilebilip bununkinin verilememesinin sebebi tam budur. Amel ism-i fâilin şartlarını izler, ama mef'ûlü olmayan bir sıfat ardından gelen isimle başka bir şey yapmak zorundadır ve bâbın geri kalanı bir tablodur: lâmlı ya da lâmsız sıfat; lâmlı, zamirli ya da çıplak isim; altısının her biri üç hâlde. Gerekçeler olağandır — isim fâil olduğu için ref', ma'rife ise mef'ûle benzetme nekre ise temyiz olarak nasb, izâfetle cer — ve on sekize kadar saymanın amacı boş iki hücreyi bulmaktır. Lâmlı sıfat zaten geri dönen zamiri taşıyan ismi muzâf edemez, çünkü lafzî izâfet bir tenvin düşürerek hak eder ve الْحَسَنُ'nün düşürecek tenvini yoktur; hafiflik ne olursa olsun hiçbir ma'rife nekreye muzâf olmaz. Üçüncüsü, حَسَنُ وَجْهِهِ, iki mektebin ayrıldığı yerdir — defterin çözmek yerine aktardığı bir okuma; bâbın da aynı biçimde aktarmasının sebebi budur."},
 "examples": [
  {"ar": "الصِّفَةُ الْمُشَبَّهَةُ: مَا اشْتُقَّ مِنْ فِعْلٍ لَازِمٍ لِمَنْ قَامَ بِهِ بِمَعْنَى الثُّبُوتِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "اسْمُ الْفَاعِلِ لِلْحُدُوثِ نَحْوُ آكِلٍ وَشَارِبٍ، وَالصِّفَةُ الْمُشَبَّهَةُ لِلثُّبُوتِ نَحْوُ حَسَنٍ وَقَبِيحٍ", "en": "Occurrence against permanence.", "tr": "Hudûs ile sübût.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "شَكْسٌ، صُلْبٌ، مِلْحٌ، حَسَنٌ … أَبْلَجُ، غَضْبَانُ", "en": "The heard patterns.", "tr": "Semâî vezinler.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "الْحَسَنُ / حَسَنٌ — الْوَجْهُ / وَجْهُهُ / وَجْهٌ", "en": "Two by three: six.", "tr": "İki kere üç: altı.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "الرَّفْعُ عَلَى الْفَاعِلِيَّةِ، وَالنَّصْبُ عَلَى التَّشْبِيهِ بِالْمَفْعُولِ أَوِ التَّمْيِيزِ، وَالْجَرُّ عَلَى الْإِضَافَةِ", "en": "The grounds of the three cases.", "tr": "Üç hâlin gerekçeleri.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "يَمْتَنِعُ الْحَسَنُ وَجْهِهِ وَالْحَسَنُ وَجْهٍ", "en": "The two barred cells.", "tr": "Mümteni' iki hücre.", "sourceStory": "al-kafiya", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«حَسَنٌ bir ism-i fâildir»",
   "right": "«حَسَنٌ sıfat-ı müşebbehedir: فَعَل vezninde, sübût mânâsında; ism-i fâil فَاعِل vezninde, hudûs mânâsındadır»",
   "why": {"en": "The two are told apart by shape and by sense together; neither alone decides.", "tr": "İkisi biçim ve mânâyla birlikte ayrılır; ikisinden biri tek başına karar vermez."}},
  {"wrong": "«الْحَسَنُ وَجْهِهِ — câiz»",
   "right": "«الْحَسَنُ الْوَجْهِ / الْحَسَنُ وَجْهُهُ / الْحَسَنُ وَجْهَهُ; وَجْهِهِ ile izâfet mümteni'dir»",
   "why": {"en": "The al-ṣifa has no tanwīn to drop, so the annexation would lighten nothing and is refused.", "tr": "Lâmlı sıfatın düşürecek tenvini yoktur; izâfet hiçbir şeyi hafifletmez ve reddedilir."}},
  {"wrong": "«حَسَنٌ وَجْهًا — mef'ûl»",
   "right": "«حَسَنٌ وَجْهًا — temyiz; ma'rifede (حَسَنٌ وَجْهَهُ) mef'ûle teşbîhtir»",
   "why": {"en": "The ṣifa comes from an intransitive verb and can have no true object; naṣb is explained by likeness or by tamyīz.", "tr": "Sıfat lâzım fiilden gelir, gerçek mef'ûlü olamaz; nasb teşbîh ya da temyizle açıklanır."}},
  {"wrong": "«أَبْلَجٍ، غَضْبَانٍ»",
   "right": "«أَبْلَجَ، غَضْبَانَ — أَفْعَل ve فَعْلَان gayr-i munsariftir, cerde fetha alır»",
   "why": {"en": "The two last patterns in the list decline as diptotes.", "tr": "Listenin son iki vezni gayr-i munsarif olarak çekilir."}}],
 "relatedNotes": [SM, IF, "ism-al-fail-wal-maful-fil-kafiya", "idafa-lafziyya", "tamyiz", "mamnu-min-sarf"]}

ADD_EN = (" Chapter 17 (notebook lines ~261-266): the ṣifa mushabbaha defined in the notebook's own Arabic (s1); the heard shape, its government, the grounds of the three cases and the two barred cells restored from the received matn and marked (s3, s5, s8, s9); "
          "the ḥudūth/thubūt contrast, the pattern list, the two-by-three grid of eighteen and the Basran–Kufan split on حَسَنُ وَجْهِهِ as commentary (s2, s4, s6, s7, s10). DIVERGENCES: the notebook's seventh pattern-word is printed صِغِرٌ and its reading is uncertain, "
          "so it is held back and sixteen of the seventeen are listed; the notebook's شُجَاحٌ is read شُجَاعٌ (the فُعَال pattern) — both await scholarly review.")
ADD_TR = (" On yedinci bâb (defter satırları ~261-266): sıfat-ı müşebbehe defterin kendi Arapçasıyla tarif edilir (s1); semâî sîga, ameli, üç hâlin gerekçeleri ve mümteni' iki hücre alınan metinden geri yazılmış ve işaretlenmiştir (s3, s5, s8, s9); "
          "hudûs/sübût karşıtlığı, vezin listesi, iki kere üçten on sekiz tablosu ve حَسَنُ وَجْهِهِ üzerindeki Basra–Kûfe ihtilâfı şerh olarak (s2, s4, s6, s7, s10). FARKLAR: defterin yedinci vezin kelimesi صِغِرٌ basılmıştır ve okunuşu kesin değildir, "
          "bu yüzden geri tutulmuş ve on yedinin on altısı listelenmiştir; defterin شُجَاحٌ'ı شُجَاعٌ (فُعَال vezni) okunmuştur — ikisi de ilmî incelemeyi beklemektedir.")
write_out(17, S, TITLE, ADD_EN, ADD_TR, "261-266", GLOSS_ADD, notes=(NOTE,),
          related=((SM, [K]), ("idafa-lafziyya", [K]), ("ism-al-fail-wal-maful-fil-kafiya", [K])))
report(17, S, GLOSS_ADD, (NOTE,))
