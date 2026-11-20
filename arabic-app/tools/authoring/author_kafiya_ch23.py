# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 23: THE PASSIVE (الْمَجْهُول). The notebook's rules: the māḍī's first letter takes a ḍamma and the letter before the
last a kasra (نُصِرَ، أُكْرِمَ، قُوتِلَ); forms opening on a hamzat al-waṣl take the ḍamma on the hamza AND on the third letter, lest the
forms be confused (اُقْتُدِرَ، اُسْتُخْرِجَ); forms opening on a tāʾ take it on the tāʾ and the second (تُجُوهِلَ); a hollow ʿayn gives the most
eloquent قِيلَ and بِيعَ — also with ishmām — and the weak قُولَ and بُوعَ, with the notebook's derivation of قِيلَ from قُوِلَ; iftiʿāl and
infiʿāl passives follow the triliteral's three readings (اُخْتِيرَ، اُنْقِيدَ) while istifʿāl and ifʿāl do not (أُقِيمَ); the muḍāriʿ's first
letter takes a ḍamma and the letter before the last a fatḥa (يُضْرَبُ، يُكْرَمُ، يُسْتَخْرَجُ), the hollow ʿayn turning to alif (يُقَالُ، يُخْتَارُ).
Source: the Ottoman notebook (Ziya Sungur-oglu), line ~307 of the transcription.

  COMMENTARY throughout (the notebook's ṣarf exposition): s1-s7 — marked C_EN/C_TR.
  OMITTED examples (verbs the corpus holds no paradigm for): فُرِّحَ، اُنْطُلِقَ، تُعُلِّمَ، اُسْتُخِيرَ، يُلْتَزَمُ، يُتَدَحْرَجُ — recorded in the manifest.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch23.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-majhul-fil-kafiya"
MJ = "naib-al-fail"
TITLE = {"ar": "الْفِعْلُ الْمَجْهُولُ", "en": "The passive verb", "tr": "Meçhûl fiil"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
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
def jw(full):
    """after a joined wāw the waṣl alif drops its vowel (the corpus convention: وَاسْتُخْرِجَ, not وَاُسْتُخْرِجَ)"""
    return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full
def pv(full, lex, en, tr, first=False, punct=None, extra="", tags=()):
    ar = "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ" + extra + "."
    return (cited(full, lex, "verb", ["idafa-definiteness", MJ] + list(tags), "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — " + ar, en, tr, punct=punct) if first
            else cited_wa("وَ" + jw(full), lex, "verb", [MJ] + list(tags), full + " مَعْطُوفٌ — " + ar, en, tr, jw(full), punct=punct))
def pmv(full, lex, en, tr, first=False, punct=None, extra="", tags=()):
    ar = "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ" + extra + "."
    return (cited(full, lex, "verb", ["idafa-definiteness", MJ] + list(tags), "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — " + ar, en, tr, punct=punct) if first
            else cited_wa("وَ" + full, lex, "verb", [MJ] + list(tags), full + " مَعْطُوفٌ — " + ar, en, tr, full, punct=punct))
def AKHIR(): return [W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«what».", "«... olan»."),
                     W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةُ مَا.", "«is before».", "«öncesinde olan»."),
                     W("آخِرِهِ", "akhir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its last».", "«sonunun».", segments=[seg("آخِرِ", "akhir", "noun"), pr3msi()])]

# ----------- s1: the māḍī
S.append({"id": "s1", "translation": {
 "en": "When the passive verb is a māḍī, its first letter is given a ḍamma and the letter before its last a kasra — as نُصِرَ, أُكْرِمَ, قُوتِلَ." + C_EN,
 "tr": "Meçhûl fiil mâzî ise evveli zammelenir, sonundan öncesi kesrelenir — نُصِرَ, أُكْرِمَ, قُوتِلَ gibi." + C_TR},
 "tokens": [
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-se»."),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«ise»."),
  W("الْفِعْلُ", "fil", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the verb».", "«fiil»."),
  W("الْمَجْهُولُ", "majhul", "noun", ["naat-sifa", MJ], "صِفَةٌ مَرْفُوعَةٌ.", "«passive».", "«meçhûl»."),
  W("مَاضِيًا", "madi", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a māḍī».", "«mâzî»."),
  W("ضُمَّ", "damma-verb", "verb", ["naib-al-fail", "al-fa-fi-jawab-al-shart", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ إِذَا.", "«is given a ḍamma».", "«zammelenir»."),
  W("أَوَّلُهُ", "awwal", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its first letter».", "«evveli».", segments=[seg("أَوَّلُ", "awwal", "noun"), pr3ms()]),
  atf_wa("وَكُسِرَ", "kasara", "verb", ["naib-al-fail"], "كُسِرَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … a kasra».", "«ve kesrelenir».", "كُسِرَ"),
  *AKHIR(),
  nahwu(),
  pv("نُصِرَ", "nasara", "«he was helped».", "«yardım edildi».", first=True, extra=" — مُجَرَّدٌ"),
  pv("أُكْرِمَ", "akrama", "«he was honoured».", "«ikram edildi».", extra=" — إِفْعَالٌ", tags=["form-iv-verbs"]),
  pv("قُوتِلَ", "qatala-fight", "«he was fought».", "«savaşıldı».", punct=".", extra=" — مُفَاعَلَةٌ، أَلِفُهُ وَاوٌ", tags=["form-iii-verbs"]),
 ]})

# ----------- s2: the waṣl hamza and the tāʾ
S.append({"id": "s2", "translation": {
 "en": "And in the five- and six-lettered forms that open on a hamzat al-waṣl, the third letter is given a ḍamma together with the hamza, so that there be no confusion — as اُقْتُدِرَ and اُسْتُخْرِجَ; and in those that open on a tāʾ, the second letter together with the tāʾ — as تُجُوهِلَ." + C_EN,
 "tr": "Evvelinde vasl hemzesi olan humâsî ve südâsî bâblarda karışıklık olmasın diye hemze ile birlikte üçüncü harf zammelenir — اُقْتُدِرَ ve اُسْتُخْرِجَ gibi; evvelinde tâ olanlarda tâ ile birlikte ikinci harf — تُجُوهِلَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("الْخُمَاسِيِّ", "khumasi", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the five-lettered».", "«humâsî»."),
  atf_wa("وَالسُّدَاسِيِّ", "sudasi", "noun", [], "السُّدَاسِيِّ مَعْطُوفٌ مَجْرُورٌ.", "«and six-lettered».", "«ve südâsî».", "السُّدَاسِيِّ"),
  W("الْمَبْدُوءَيْنِ", "mabdu", "noun", ["naat-sifa", "al-muthanna", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ بِالْيَاءِ.", "«that open».", "«başlayan»."),
  bi_("بِهَمْزَةِ", "hamza-letter", "noun", ["idafa-definiteness"], "هَمْزَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«on a hamza of».", "«hemzesiyle».", "هَمْزَةِ"),
  W("الْوَصْلِ", "wasl", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«waṣl».", "«vasl»."),
  W("يُضَمُّ", "damma-verb", "verb", ["naib-al-fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is given a ḍamma».", "«zammelenir»."),
  W("الثَّالِثُ", "thalith", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the third letter».", "«üçüncü harf»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«together with».", "«ile birlikte»."),
  W("الْهَمْزَةِ", "hamza-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the hamza».", "«hemze»."),
  li_("لِئَلَّا", "an-nasiba", "part", ["nawasib-wa-jawazim-al-mudari", "lam-taleel", "la-nafiya"], "أَصْلُهُ لِأَنْ لَا — لِلتَّعْلِيلِ.", "«so that … not».", "«-maması için».", "ئَلَّا", segs=[seg("لِ", "lam-taleel", "part"), seg("ئَلَّا", "an-nasiba", "part")]),
  W("يَقَعَ", "waqaa", "verb", ["nawasib-wa-jawazim-al-mudari", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«there be».", "«olmaması»."),
  W("الْتِبَاسٌ", "iltibas", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«confusion».", "«karışıklık».", punct="،"),
  nahwu(),
  pv("اُقْتُدِرَ", "iqtadara", "«it was mastered».", "«güç yetirildi».", first=True, extra=" — افْتِعَالٌ، ضُمَّتْ هَمْزَتُهُ وَثَالِثُهُ", tags=["form-viii-verbs"]),
  pv("اُسْتُخْرِجَ", "istakhraja", "«it was extracted».", "«istihrac edildi».", punct="؛", extra=" — اسْتِفْعَالٌ", tags=["form-x-verbs"]),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("الْمَبْدُوءِ", "mabdu", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«what opens».", "«başlayanda»."),
  bi_("بِالتَّاءِ", "ta-letter", "noun", [], "التَّاءِ مَجْرُورٌ.", "«on a tāʾ».", "«tâ ile».", "التَّاءِ"),
  W("يُضَمُّ", "damma-verb", "verb", ["naib-al-fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is given a ḍamma».", "«zammelenir»."),
  W("الثَّانِي", "thani", "noun", ["naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second letter».", "«ikinci harf»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«together with».", "«ile birlikte»."),
  W("التَّاءِ", "ta-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tāʾ».", "«tâ».", punct="،"),
  nahwu(),
  pv("تُجُوهِلَ", "tajahala", "«it was feigned ignorance of».", "«bilmezlikten gelindi».", first=True, punct=".", extra=" — تَفَاعُلٌ، ضُمَّتْ تَاؤُهُ وَثَانِيهِ", tags=["form-vi-verbs"]),
 ]})

# ----------- s3: the hollow ʿayn
S.append({"id": "s3", "translation": {
 "en": "And in those whose ʿayn is weak, the most eloquent reading is قِيلَ and بِيعَ; it also came, eloquently, with ishmām; and it came, weakly, as قُولَ and بُوعَ." + C_EN,
 "tr": "Aynü'l-fiili illetli olanlarda en fasîh okuyuş قِيلَ ve بِيعَ'dir; fasîh olarak işmâm ile de geldi; zayıf olarak قُولَ ve بُوعَ diye de geldi." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«those».", "«... olanlarda»."),
  W("عَيْنُهُ", "ayn", "noun", ["ism-mawsul", "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«whose ʿayn».", "«aynü'l-fiili».", segments=[seg("عَيْنُ", "ayn", "noun"), pr3ms()]),
  W("مُعْتَلَّةٌ", "mutall", "noun", ["mubtada-khabar", "hollow-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«is weak».", "«illetli»."),
  W("الْأَفْصَحُ", "afsah", "noun", ["mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the most eloquent».", "«en fasîh»."),
  cited("قِيلَ", "qala", "verb", ["mubtada-khabar", MJ, "hollow-verbs"], "خَبَرٌ — فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، أَصْلُهُ قُوِلَ.", "«qīla» — from قُوِلَ.", "«kîle» — aslı قُوِلَ."),
  cited_wa("وَبِيعَ", "baa", "verb", [MJ, "hollow-verbs"], "بِيعَ مَعْطُوفٌ — أَصْلُهُ بُيِعَ.", "«and bīʿa» — from بُيِعَ.", "«ve bî'a» — aslı بُيِعَ.", "بِيعَ", punct="؛"),
  atf_wa("وَجَاءَ", "jaa", "verb", ["fail"], "جَاءَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and it came».", "«ve geldi».", "جَاءَ"),
  W("فَصِيحًا", "fasih", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«eloquently».", "«fasîh olarak»."),
  bi_("بِالْإِشْمَامِ", "ishmam", "noun", [MJ], "الْإِشْمَامِ مَجْرُورٌ — إِمَالَةُ كَسْرَةِ الْفَاءِ إِلَى الضَّمَّةِ وَالْيَاءِ إِلَى الْوَاوِ.", "«with ishmām» — the kasra leaning toward the ḍamma.", "«işmâm ile» — kesrenin zammeye meyli.", "الْإِشْمَامِ", punct="،"),
  atf_wa("وَجَاءَ", "jaa", "verb", ["fail"], "جَاءَ فِعْلٌ مَاضٍ.", "«and it came».", "«ve geldi».", "جَاءَ"),
  W("ضَعِيفًا", "daif", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«weakly».", "«zayıf olarak»."),
  cited("قُولَ", "qala", "verb", ["fail", MJ, "hollow-verbs"], "فَاعِلٌ — الْوَجْهُ الضَّعِيفُ.", "«qūla».", "«kûle»."),
  cited_wa("وَبُوعَ", "baa", "verb", [MJ, "hollow-verbs"], "بُوعَ مَعْطُوفٌ.", "«and būʿa».", "«ve bû'a».", "بُوعَ", punct="."),
 ]})

# ----------- s4: the derivation of قِيلَ
S.append({"id": "s4", "translation": {
 "en": "And قِيلَ was originally قُوِلَ; the ḍamma of the qāf before the kasra of the wāw was heavy on the tongue, so the qāf's ḍamma was dropped and the wāw's kasra given to the qāf, becoming قِوْلَ; then the wāw, quiescent after a kasra, was turned into a yāʾ: قِيلَ. And بِيعَ was originally بُيِعَ." + C_EN,
 "tr": "قِيلَ aslında قُوِلَ idi; vâvın kesresinden önce kâfın zammesi dile ağır geldiği için kâfın zammesi hazfedildi ve vâvın kesresi kâfa verildi, قِوْلَ oldu; sonra vâv, kesreden sonra sâkin olduğundan yâya kalbedildi: قِيلَ. بِيعَ de aslında بُيِعَ idi." + C_TR},
 "tokens": [
  cited_wa("وَقِيلَ", "qala", "verb", ["mubtada-khabar", MJ, "hollow-verbs"], "قِيلَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and qīla».", "«ve kîle».", "قِيلَ"),
  W("أَصْلُهُ", "asl", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its origin».", "«aslı».", segments=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  cited("قُوِلَ", "qala", "verb", ["mubtada-khabar", MJ, "hollow-verbs"], "خَبَرٌ — الْأَصْلُ قَبْلَ الْإِعْلَالِ.", "«quwila» — before iʿlāl.", "«kuvile» — i'lâlden önce.", punct="؛"),
  W("ثَقُلَتْ", "thaqula", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«was heavy».", "«ağır geldi»."),
  W("ضَمَّةُ", "damma", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the ḍamma of».", "«zammesi»."),
  W("الْقَافِ", "qaf-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the qāf».", "«kâfın»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«önce»."),
  W("كَسْرَةِ", "kasra", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the kasra of».", "«kesresinden»."),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wāw».", "«vâvın»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("اللِّسَانِ", "lisan", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the tongue».", "«dile».", punct="،"),
  W("فَحُذِفَتْ", "hadhafa", "verb", ["naib-al-fail", "al-fa-fi-khabar-al-mubtada", "hadhf-wa-taqdir"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَحُذِفَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«so … was dropped».", "«bu yüzden hazfedildi».", segments=[seg("فَ", "fa", "conj"), seg("حُذِفَتْ", "hadhafa", "verb")]),
  W("ضَمَّةُ", "damma", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the ḍamma of».", "«zammesi»."),
  W("الْقَافِ", "qaf-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the qāf».", "«kâfın»."),
  atf_wa("وَأُعْطِيَتْ", "ata-give", "verb", ["naib-al-fail", "form-iv-verbs"], "أُعْطِيَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and … was given».", "«ve verildi».", "أُعْطِيَتْ"),
  W("كَسْرَةُ", "kasra", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the kasra of».", "«kesresi»."),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wāw».", "«vâvın»."),
  li_("لِلْقَافِ", "qaf-letter", "noun", [], "الْقَافِ مَجْرُورٌ.", "«to the qāf».", "«kâfa».", "الْقَافِ", segs=[seg("لِ", "li", "prep"), seg("لْقَافِ", "qaf-letter", "noun")]),
  W("فَصَارَ", "sara", "verb", ["kana-wa-akhawatuha", "al-fa-fi-khabar-al-mubtada", "hollow-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَصَارَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ.", "«becoming».", "«oldu».", segments=[seg("فَ", "fa", "conj"), seg("صَارَ", "sara", "verb")]),
  cited("قِوْلَ", "qala", "verb", ["kana-wa-akhawatuha", MJ, "hollow-verbs"], "خَبَرُ صَارَ — مَرْحَلَةٌ وُسْطَى بَعْدَ النَّقْلِ.", "«qiwla» — the middle stage, after naql.", "«kıvle» — nakilden sonraki ara basamak.", punct="؛"),
  W("ثُمَّ", "thumma", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«then».", "«sonra»."),
  W("قُلِبَتِ", "qalaba", "verb", ["naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«was turned».", "«kalbedildi»."),
  W("الْوَاوُ", "waw-letter", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the wāw».", "«vâv»."),
  W("يَاءً", "ya-letter", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«into a yāʾ».", "«yâya»."),
  li_("لِسُكُونِهَا", "sukun", "noun", ["idafa-definiteness"], "سُكُونِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — لِلتَّعْلِيلِ.", "«since it was quiescent».", "«sâkin olduğundan».", "سُكُونِ", segs=[seg("لِ", "li", "prep"), seg("سُكُونِ", "sukun", "noun"), pr3fs()]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«sonra»."),
  W("كَسْرَةٍ", "kasra", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a kasra».", "«kesreden».", punct=":"),
  cited("قِيلَ", "qala", "verb", [MJ, "hollow-verbs"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فَصَارَ — الصُّورَةُ الْأَخِيرَةُ.", "«qīla» — the final form.", "«kîle» — son biçim.", punct="؛"),
  cited_wa("وَبِيعَ", "baa", "verb", ["mubtada-khabar", MJ, "hollow-verbs"], "بِيعَ مُبْتَدَأٌ.", "«and bīʿa».", "«ve bî'a».", "بِيعَ"),
  W("أَصْلُهُ", "asl", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its origin».", "«aslı».", segments=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  cited("بُيِعَ", "baa", "verb", ["mubtada-khabar", MJ, "hollow-verbs"], "خَبَرٌ.", "«buyiʿa».", "«büyi'a».", punct="."),
 ]})

# ----------- s5: iftiʿāl and infiʿāl against istifʿāl and ifʿāl
S.append({"id": "s5", "translation": {
 "en": "And the passives of iftiʿāl, as اُخْتِيرَ, and of infiʿāl, as اُنْقِيدَ, are like the triliteral's passive in admitting the three readings; but the passive of ifʿāl, as أُقِيمَ, is not." + C_EN,
 "tr": "اُخْتِيرَ gibi iftiâl ve اُنْقِيدَ gibi infiâl bâbının meçhûlleri üç vechin gelmesinde sülâsînin meçhûlü gibidir; fakat أُقِيمَ gibi ifâl bâbının meçhûlü öyle değildir." + C_TR},
 "tokens": [
  atf_wa("وَمَجْهُولُ", "majhul", "noun", ["mubtada-khabar", "idafa-definiteness", MJ], "مَجْهُولُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the passive of».", "«ve meçhûlü».", "مَجْهُولُ"),
  W("الِافْتِعَالِ", "iftial", "noun", ["idafa-definiteness", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iftiʿāl».", "«iftiâlin»."),
  nahwu(),
  cited("اُخْتِيرَ", "ikhtara", "verb", ["idafa-definiteness", MJ, "form-viii-verbs", "hollow-verbs"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it was chosen».", "«seçildi».", punct="،"),
  atf_wa("وَالِانْفِعَالِ", "infial", "noun", ["idafa-definiteness", "form-vii-verbs"], "الِانْفِعَالِ مَعْطُوفٌ مَجْرُورٌ.", "«and infiʿāl».", "«ve infiâlin».", "الِانْفِعَالِ"),
  nahwu(),
  cited("اُنْقِيدَ", "inqada", "verb", ["idafa-definiteness", MJ, "form-vii-verbs", "hollow-verbs"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it was led».", "«boyun eğdirildi».", punct="،"),
  W("كَمَجْهُولِ", "majhul", "noun", ["huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَمَجْهُولِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«are like the passive of».", "«meçhûlü gibidir».", segments=[seg("كَ", "ka", "prep"), seg("مَجْهُولِ", "majhul", "noun")]),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the triliteral».", "«sülâsînin»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَجِيءِ", "maji", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«admitting».", "«gelmesinde»."),
  W("الْأَوْجُهِ", "wajh", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the readings».", "«vecihlerin»."),
  W("الثَّلَاثَةِ", "thalatha", "noun", ["naat-sifa", "asma-al-adad-fil-kafiya"], "صِفَةٌ مَجْرُورَةٌ.", "«three».", "«üç».", punct="؛"),
  atf_wa("وَمَجْهُولُ", "majhul", "noun", ["mubtada-khabar", "idafa-definiteness", MJ], "مَجْهُولُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«but the passive of».", "«fakat meçhûlü».", "مَجْهُولُ"),
  W("الْإِفْعَالِ", "ifal", "noun", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ifʿāl».", "«ifâlin»."),
  nahwu(),
  cited("أُقِيمَ", "aqama", "verb", ["idafa-definiteness", MJ, "form-iv-verbs", "hollow-verbs"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَجْهٌ وَاحِدٌ.", "«it was established» — one reading.", "«ikâme edildi» — tek vecih."),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "mubtada-khabar"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ.", "«is not».", "«değildir»."),
  W("كَذَلِكَ", "kadhalika", "part", ["kana-wa-akhawatuha"], "الْكَافُ حَرْفُ جَرٍّ، وَذَلِكَ فِي مَحَلِّ جَرٍّ — خَبَرُ لَيْسَ.", "«so».", "«öyle».", punct="."),
 ]})

# ----------- s6: the muḍāriʿ
S.append({"id": "s6", "translation": {
 "en": "And when the passive verb is a muḍāriʿ, its first letter is given a ḍamma and the letter before its last a fatḥa — as يُضْرَبُ, يُكْرَمُ, يُسْتَخْرَجُ." + C_EN,
 "tr": "Meçhûl fiil muzâri ise evveli zammelenir, sonundan öncesi fethalanır — يُضْرَبُ, يُكْرَمُ, يُسْتَخْرَجُ gibi." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... ise».", "إِذَا"),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«ise»."),
  W("الْمَجْهُولُ", "majhul", "noun", ["kana-wa-akhawatuha", MJ], "اسْمُ كَانَ مَرْفُوعٌ.", "«the passive».", "«meçhûl»."),
  W("مُضَارِعًا", "mudari", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a muḍāriʿ».", "«muzâri»."),
  W("ضُمَّ", "damma-verb", "verb", ["naib-al-fail", "al-fa-fi-jawab-al-shart", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ إِذَا.", "«is given a ḍamma».", "«zammelenir»."),
  W("أَوَّلُهُ", "awwal", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its first letter».", "«evveli».", segments=[seg("أَوَّلُ", "awwal", "noun"), pr3ms()]),
  atf_wa("وَفُتِحَ", "fataha", "verb", ["naib-al-fail"], "فُتِحَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … a fatḥa».", "«ve fethalanır».", "فُتِحَ"),
  *AKHIR(),
  nahwu(),
  pmv("يُضْرَبُ", "daraba", "«he is struck».", "«vurulur».", first=True),
  pmv("يُكْرَمُ", "akrama", "«he is honoured».", "«ikram edilir».", tags=["form-iv-verbs"]),
  pmv("يُسْتَخْرَجُ", "istakhraja", "«it is extracted».", "«istihrac edilir».", punct=".", tags=["form-x-verbs"]),
 ]})

# ----------- s7: the hollow muḍāriʿ
S.append({"id": "s7", "translation": {
 "en": "And in those whose ʿayn is weak, be it a wāw or a yāʾ, the ʿayn is turned into an alif — as يُقَالُ and يُخْتَارُ." + C_EN,
 "tr": "Aynü'l-fiili illetli olanlarda, ister vâv ister yâ olsun, aynü'l-fiil elife kalbedilir — يُقَالُ ve يُخْتَارُ gibi." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«those».", "«... olanlarda»."),
  W("عَيْنُهُ", "ayn", "noun", ["ism-mawsul", "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whose ʿayn».", "«aynü'l-fiili».", segments=[seg("عَيْنُ", "ayn", "noun"), pr3ms()]),
  W("مُعْتَلَّةٌ", "mutall", "noun", ["mubtada-khabar", "hollow-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«is weak».", "«illetli».", punct="،"),
  W("وَاوًا", "waw-letter", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ الْمَحْذُوفَةِ مَنْصُوبٌ: سَوَاءٌ كَانَتْ وَاوًا.", "«be it a wāw».", "«ister vâv»."),
  W("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ.", "«it be».", "«olsun»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ister»."),
  W("يَاءً", "ya-letter", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«a yāʾ».", "«yâ».", punct="،"),
  W("تُقْلَبُ", "qalaba", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is turned».", "«kalbedilir»."),
  W("الْعَيْنُ", "ayn", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the ʿayn».", "«aynü'l-fiil»."),
  W("أَلِفًا", "alif-letter", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«into an alif».", "«elife».", punct="،"),
  nahwu(),
  pmv("يُقَالُ", "qala", "«it is said».", "«denir».", first=True, extra=" — أَصْلُهُ يُقْوَلُ", tags=["hollow-verbs"]),
  pmv("يُخْتَارُ", "ikhtara", "«it is chosen».", "«seçilir».", punct=".", extra=" — أَصْلُهُ يُخْتَيَرُ", tags=["form-viii-verbs", "hollow-verbs"]),
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
 "khumasi": need("khumasi", "خُمَاسِيّ", "خ م س", "noun", "five-lettered (of a verb's māḍī) — اِفْتَعَلَ، اِنْفَعَلَ، تَفَعَّلَ، تَفَاعَلَ", "humâsî (mâzîsi beş harfli) — اِفْتَعَلَ، اِنْفَعَلَ، تَفَعَّلَ، تَفَاعَلَ", 4),
 "sudasi": need("sudasi", "سُدَاسِيّ", "س د س", "noun", "six-lettered (of a verb's māḍī) — اِسْتَفْعَلَ", "südâsî (mâzîsi altı harfli) — اِسْتَفْعَلَ", 4),
 "mabdu": need("mabdu", "مَبْدُوء", "ب د أ", "noun", "begun, opened (with a letter) — the ism mafʿūl of بَدَأَ", "başlanan, (bir harfle) açılan — bede'e'nin ism-i mef'ûlü", 5),
 "mutall": need("mutall", "مُعْتَلّ", "ع ل ل", "noun", "weak (of a radical: wāw, yāʾ or alif)", "illetli (bir kök harfi için: vâv, yâ ya da elif)", 4),
 "ishmam": need("ishmam", "إِشْمَام", "ش م م", "noun", "ishmām — leaning the kasra of قِيلَ toward a ḍamma (and the yāʾ toward a wāw), a Qurʾānic reading", "işmâm — قِيلَ'nin kesresini zammeye (yâsını vâva) meylettirme, bir kıraat", 6),
 "qaf-letter": need("qaf-letter", "قَاف", None, "noun", "the letter qāf", "kâf (ق) harfi", 3),
 "thaqula": need("thaqula", "ثَقُلَ", "ث ق ل", "verb", "to be heavy", "ağır olmak, ağır gelmek", 3),
 "infial": need("infial", "اِنْفِعَال", "ف ع ل", "noun", "the pattern اِنْفِعَال — the maṣdar and name of Form VII", "infiâl vezni — VII. bâbın masdarı ve adı", 4),
 "ifal": need("ifal", "إِفْعَال", "ف ع ل", "noun", "the pattern إِفْعَال — the maṣdar and name of Form IV", "ifâl vezni — IV. bâbın masdarı ve adı", 4),
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
put_morph(mo, "thaqula", _sg.sound1("karuma", "ثَقُل", "ثْقُل", "اُثْقُل", "ثِقَل", "ثَاقِل", None, None, None, "ثَقُلَ الشَّيْءُ يَثْقُلُ ثِقَلًا: ضِدُّ خَفَّ — مِنْ بَابِ حَسُنَ، لَازِمٌ؛ وَالصِّفَةُ الْمُشَبَّهَةُ ثَقِيلٌ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch23 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْفِعْلُ الْمَجْهُولُ فِي الْكَافِيَةِ", "en": "The passive in the Kafiya's notebook: the two vowel rules, the waṣl-hamza and tāʾ forms, the hollow passive with its three readings and the derivation of قِيلَ", "tr": "Kâfiye defterinde meçhûl: iki hareke kuralı, vasl hemzeli ve tâlı bâblar, üç vechiyle ecvef meçhûl ve قِيلَ'nin türetilişi"},
 "level": 4, "group": "sarf",
 "classicalSources": ["ضياء صونغور اوغلى — دفتر الكافية: مجهول الماضي بضم أوله وكسر ما قبل آخره؛ ضم الثالث مع همزة الوصل والثاني مع التاء لئلا يلتبس؛ قِيلَ وبِيعَ بالإشمام وقُولَ وبُوعَ؛ أصل قِيلَ قُوِلَ؛ مجهول الافتعال والانفعال كالثلاثي دون الاستفعال والإفعال؛ مجهول المضارع بضم أوله وفتح ما قبل آخره؛ قلب العين ألفا", "الشافية لابن الحاجب — باب المجهول"],
 "question": {
  "en": ["How is a passive MĀḌĪ made? Put a ḍamma on the first letter and a kasra on the letter before the last: نَصَرَ → نُصِرَ, أَكْرَمَ → أُكْرِمَ, قَاتَلَ → قُوتِلَ (the alif of Form III turns into a wāw because it now follows a ḍamma).",
         "What of forms that begin with a waṣl hamza or a tāʾ? The ḍamma goes on the hamza AND on the third letter (اُقْتُدِرَ، اُسْتُخْرِجَ), on the tāʾ AND the second (تُجُوهِلَ) — otherwise, the notebook says, the forms could be confused: a waṣl hamza carries no vowel of its own in speech, so the ḍamma has to be heard somewhere.",
         "How is a passive MUḌĀRIʿ made? A ḍamma on the first letter and a fatḥa before the last: يَضْرِبُ → يُضْرَبُ, يُكْرِمُ → يُكْرَمُ, يَسْتَخْرِجُ → يُسْتَخْرَجُ. The engine's majhūl builder is exactly these two rules and nothing more.",
         "Why is قِيلَ not قُوِلَ? Because a ḍamma before a kasra-bearing wāw is heavy: the qāf's ḍamma is dropped, the wāw's kasra moves back onto the qāf (قِوْلَ), and a quiescent wāw after a kasra becomes a yāʾ — قِيلَ. The same road takes بُيِعَ to بِيعَ. The IlalEngine walks these very steps, naql before qalb.",
         "Are there other readings? Three: قِيلَ (most eloquent), قِيلَ with ishmām — the kasra coloured toward a ḍamma, as in some Qurʾānic readings — and the weak قُولَ. Forms VIII and VII share all three (اُخْتِيرَ، اُنْقِيدَ); Forms X and IV do not (أُقِيمَ only).",
         "And the hollow muḍāriʿ? Its ʿayn, wāw or yāʾ, becomes an alif: يُقَالُ، يُخْتَارُ. This is why the engine refuses to derive a hollow verb's passive from the vowel rule alone and reads it from the stored cell — يُقَالُ is not يُقْوَلُ.",
         "Which verbs did the notebook cite that the chapter leaves out? فُرِّحَ، اُنْطُلِقَ، تُعُلِّمَ، اُسْتُخِيرَ، يُلْتَزَمُ، يُتَدَحْرَجُ — the corpus holds no checked paradigm for them, and a cited verb without one would fail the paradigm gate."],
  "tr": ["Meçhûl MÂZÎ nasıl yapılır? İlk harfe zamme, sondan önceki harfe kesre: نَصَرَ → نُصِرَ, أَكْرَمَ → أُكْرِمَ, قَاتَلَ → قُوتِلَ (III. bâbın elifi artık zammeden sonra geldiği için vâva döner).",
         "Vasl hemzesi ya da tâ ile başlayan bâblar? Zamme hemzeye VE üçüncü harfe (اُقْتُدِرَ، اُسْتُخْرِجَ), tâya VE ikinciye (تُجُوهِلَ) konur — yoksa, defter der, biçimler karışabilir: vasl hemzesinin konuşmada kendi harekesi yoktur, zamme bir yerde duyulmalıdır.",
         "Meçhûl MUZÂRİ nasıl yapılır? İlk harfe zamme, sondan öncekine fetha: يَضْرِبُ → يُضْرَبُ, يُكْرِمُ → يُكْرَمُ, يَسْتَخْرِجُ → يُسْتَخْرَجُ. Motorun meçhûl kurucusu tam bu iki kuraldır, başka bir şey değil.",
         "قِيلَ neden قُوِلَ değildir? Çünkü kesreli vâvdan önce zamme ağırdır: kâfın zammesi düşer, vâvın kesresi geriye kâfa taşınır (قِوْلَ), kesreden sonra sâkin vâv yâ olur — قِيلَ. Aynı yol بُيِعَ'yı بِيعَ'ya götürür. IlalEngine tam bu adımları yürür, kalbden önce nakil.",
         "Başka okuyuşlar var mı? Üç: قِيلَ (en fasîh), işmâm ile قِيلَ — kesre zammeye doğru renklenir, bazı kıraatlerdeki gibi — ve zayıf قُولَ. VIII. ve VII. bâb üçünü paylaşır (اُخْتِيرَ، اُنْقِيدَ); X. ve IV. bâb paylaşmaz (yalnız أُقِيمَ).",
         "Ya ecvef muzâri? Aynı, vâv ya da yâ, elif olur: يُقَالُ، يُخْتَارُ. Motorun ecvef fiilin meçhûlünü yalnız hareke kuralından türetmeyi reddedip saklanan hücreden okumasının sebebi budur — يُقَالُ, يُقْوَلُ değildir.",
         "Defterin zikredip bâbın dışarıda bıraktığı fiiller? فُرِّحَ، اُنْطُلِقَ، تُعُلِّمَ، اُسْتُخِيرَ، يُلْتَزَمُ، يُتَدَحْرَجُ — külliyatta onlar için denetlenmiş bir çekim yok ve çekimsiz zikredilen bir fiil çekim kapısından geçemezdi."]},
 "plain": {
  "en": "To make a verb passive, give its first letter a ḍamma and the letter before its last a kasra in the past (نُصِرَ) or a fatḥa in the present (يُضْرَبُ). Forms opening on a silent hamza or a tāʾ take a second ḍamma. A hollow verb's middle letter turns to yāʾ in the past (قِيلَ) and alif in the present (يُقَالُ).",
  "tr": "Bir fiili meçhûl yapmak için ilk harfe zamme, sondan önceki harfe geçmişte kesre (نُصِرَ), şimdiki zamanda fetha (يُضْرَبُ) verin. Sessiz hemze ya da tâ ile başlayan bâblar zammeyi bir sonraki harekeli harfe de koyar. Ecvef fiilin orta harfi geçmişte yâ (قِيلَ), şimdiki zamanda elif (يُقَالُ) olur."},
 "explanation": {
  "en": "The notebook turns from the verb's tenses to its voice with a page that is pure ṣarf, and the chapter keeps it because the app's own passive builder was written from the same two sentences: ḍamma on the first and kasra before the last for the māḍī, ḍamma on the first and fatḥa before the last for the muḍāriʿ. The notebook's refinements are the places where that rule meets orthography. A form that opens on a waṣl hamza has no vowel of its own to carry the ḍamma, so the third letter takes it as well — اُقْتُدِرَ against اِقْتَدَرَ — and a form that opens on a tāʾ moves the second ḍamma to the second letter, تُجُوهِلَ; the stated reason, so that forms are not confused, is the same reason the engine stores and does not derive these cells. The hollow verb is the chapter's centre. The notebook gives the three received readings of the passive of قَالَ and بَاعَ — the eloquent قِيلَ، بِيعَ, the ishmām reading that colours the kasra toward a ḍamma, and the weak قُولَ، بُوعَ — and then derives قِيلَ step by step from قُوِلَ: the heavy ḍamma is dropped, the wāw's kasra transferred, the quiescent wāw after a kasra turned to yāʾ. That is the IlalEngine's naql-then-qalb order written out by hand. It adds the comparison the student needs: Forms VIII and VII behave like the triliteral and admit all three readings, Forms X and IV admit only one. The muḍāriʿ closes the chapter — the ʿayn becomes an alif, يُقَالُ، يُخْتَارُ — and this is the boundary the engine respects by refusing to vowel-shift a hollow verb into its passive. Six of the notebook's examples are omitted because the corpus holds no checked paradigm for them; the manifest names them.",
  "tr": "Defter fiilin zamanlarından çatısına saf sarf olan bir sayfayla geçer ve bâb onu tutar, çünkü uygulamanın kendi meçhûl kurucusu aynı iki cümleden yazılmıştır: mâzî için ilke zamme sondan öncekine kesre, muzâri için ilke zamme sondan öncekine fetha. Defterin incelikleri bu kuralın imlâyla buluştuğu yerlerdir. Vasl hemzesiyle açılan bir bâbın zammeyi taşıyacak kendi harekesi yoktur, bu yüzden üçüncü harf de onu alır — اِقْتَدَرَ'ye karşı اُقْتُدِرَ — tâ ile açılan bâb ikinci zammeyi ikinci harfe taşır, تُجُوهِلَ; söylenen sebep, biçimlerin karışmaması, motorun bu hücreleri türetmeyip saklamasının da sebebidir. Ecvef fiil bâbın merkezidir. Defter قَالَ ve بَاعَ'nın meçhûlünün alınan üç okuyuşunu verir — fasîh قِيلَ، بِيعَ, kesreyi zammeye doğru renklendiren işmâm okuyuşu ve zayıf قُولَ، بُوعَ — sonra قِيلَ'yi قُوِلَ'den adım adım türetir: ağır zamme düşer, vâvın kesresi taşınır, kesreden sonra sâkin vâv yâya döner. Bu, IlalEngine'in önce-nakil-sonra-kalb sırasının elle yazılmış hâlidir. Öğrencinin ihtiyaç duyduğu karşılaştırmayı ekler: VIII. ve VII. bâb sülâsî gibi davranıp üç okuyuşu da kabul eder, X. ve IV. bâb yalnız birini. Muzâri bâbı kapatır — ayn elif olur, يُقَالُ، يُخْتَارُ — ve bu, motorun ecvef fiili hareke kaydırarak meçhûle çevirmeyi reddederek saygı gösterdiği sınırdır. Defterin altı örneği, külliyatta onlar için denetlenmiş çekim bulunmadığından dışarıda bırakılmıştır; manifest onları adlandırır."},
 "examples": [
  {"ar": "نُصِرَ، أُكْرِمَ، قُوتِلَ", "en": "The māḍī rule.", "tr": "Mâzî kuralı.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "اُقْتُدِرَ، اُسْتُخْرِجَ — تُجُوهِلَ", "en": "The waṣl hamza and the tāʾ.", "tr": "Vasl hemzesi ve tâ.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "قِيلَ وَبِيعَ — قُولَ وَبُوعَ", "en": "The hollow passive's readings.", "tr": "Ecvef meçhûlün okuyuşları.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "قُوِلَ → قِوْلَ → قِيلَ", "en": "The derivation.", "tr": "Türetiliş.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "اُخْتِيرَ، اُنْقِيدَ — أُقِيمَ", "en": "Which forms share the three readings.", "tr": "Hangi bâblar üç okuyuşu paylaşır.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "يُضْرَبُ، يُكْرَمُ، يُسْتَخْرَجُ — يُقَالُ، يُخْتَارُ", "en": "The muḍāriʿ rule and the hollow ʿayn.", "tr": "Muzâri kuralı ve ecvef ayn.", "sourceStory": "al-kafiya", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«اِقْتُدِرَ — hemze kesreli»",
   "right": "«اُقْتُدِرَ — vasl hemzesi de üçüncü harf de zammelenir»",
   "why": {"en": "The ḍamma must be heard; a waṣl hamza alone cannot carry it.", "tr": "Zamme duyulmalıdır; vasl hemzesi tek başına onu taşıyamaz."}},
  {"wrong": "«قُوِلَ»",
   "right": "«قِيلَ (en fasîh), işmâm ile قِيلَ, zayıf قُولَ — قُوِلَ yalnız asıldır»",
   "why": {"en": "The notebook's derivation shows why the origin is never pronounced.", "tr": "Defterin türetilişi aslın neden telaffuz edilmediğini gösterir."}},
  {"wrong": "«يُقْوَلُ»",
   "right": "«يُقَالُ — meçhûl muzâride ecvef ayn elife döner»",
   "why": {"en": "The two-vowel rule is not the last step for a hollow verb; iʿlāl follows it.", "tr": "İki hareke kuralı ecvef fiil için son adım değildir; i'lâl onu izler."}},
  {"wrong": "«أُقِيمَ ile birlikte أُقُومَ de câiz»",
   "right": "«أُقِيمَ — ifâl ve istifâl bâblarının meçhûlünde tek vecih vardır»",
   "why": {"en": "Only the triliteral and Forms VII–VIII admit the three readings.", "tr": "Üç okuyuşu yalnız sülâsî ile VII–VIII. bâblar kabul eder."}}],
 "relatedNotes": [MJ, "naib-al-fail", "hollow-verbs", "form-viii-verbs", "form-vii-verbs", "form-iv-verbs", "al-fil-wal-madi-wal-mudari-fil-kafiya"]}

ADD_EN = (" Chapter 23 (notebook line ~307): the passive — the notebook's two vowel rules for the māḍī and the muḍāriʿ, the waṣl-hamza and tāʾ forms, the hollow passive's three readings with the derivation of قِيلَ, and which forms share them — the notebook's own ṣarf exposition, kept as commentary (s1-s7). "
          "OMITTED: the notebook also cites فُرِّحَ، اُنْطُلِقَ، تُعُلِّمَ، اُسْتُخِيرَ، يُلْتَزَمُ، يُتَدَحْرَجُ; the corpus holds no checked paradigm for these verbs, so they are not cited.")
ADD_TR = (" Yirmi üçüncü bâb (defter satırı ~307): meçhûl — defterin mâzî ve muzâri için iki hareke kuralı, vasl hemzeli ve tâlı bâblar, قِيلَ'nin türetilişiyle ecvef meçhûlün üç okuyuşu ve hangi bâbların bunları paylaştığı — defterin kendi sarf açıklaması, şerh olarak (s1-s7). "
          "DIŞARIDA BIRAKILAN: defter فُرِّحَ، اُنْطُلِقَ، تُعُلِّمَ، اُسْتُخِيرَ، يُلْتَزَمُ، يُتَدَحْرَجُ'yu da zikreder; külliyatta bu fiiller için denetlenmiş çekim bulunmadığından zikredilmemiştir.")
write_out(23, S, TITLE, ADD_EN, ADD_TR, "307", GLOSS_ADD, notes=(NOTE,),
          related=((MJ, [K]), ("hollow-verbs", [K])))
report(23, S, GLOSS_ADD, (NOTE,))
