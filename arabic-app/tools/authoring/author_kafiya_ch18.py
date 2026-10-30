# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 18: THE SIFA MUSHABBAHA, continued — the notebook's grading of the eighteen cases (one pronoun: best, nine;
two pronouns: good, two; no pronoun: ugly, four), how the pronoun is known (in the governed word it shows; in the sifa only when the
governed word is not raised), agreement of the sifa with a feminine, dual or plural mawsuf (هِنْدٌ حَسَنَةُ وَجْهٍ …), and the two
participles that follow the same eighteen (زَيْدٌ قَائِمٌ الْأَبُ / الْأَبَ / الْأَبِ; مَضْرُوبٌ الْأَبُ …) with the one restriction on them.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~266-273 of the transcription.

  COMMENTARY throughout (the notebook's own exposition): s1-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch18.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "masail-al-sifa-al-mushabbaha-fil-kafiya"
SM = "sifa-mushabbaha"
IF = "ism-fail"
IM = "ism-maful"
TITLE = {"ar": "مَسَائِلُ الصِّفَةِ الْمُشَبَّهَةِ", "en": "The cases of the ṣifa mushabbaha", "tr": "Sıfat-ı müşebbehenin meseleleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prTa(): return seg("تَ", "pron-2ms", "pron")
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
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "prep"), seg(inner, lex, pos)]))
def FI(): return W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».")
def ex(sifa_full, sifa_ar, sifa_en, sifa_tr, w_full, w_ar, w_en, w_tr, w_segs=None, punct=None, joined=False):
    """a cited ṣifa + its governed word"""
    a = (cited_wa("وَ" + sifa_full, "hasan-adj", "noun", [SM, "idafa-lafziyya"], sifa_full + " مَعْطُوفٌ — " + sifa_ar, sifa_en, sifa_tr, sifa_full) if joined
         else cited(sifa_full, "hasan-adj", "noun", [SM, "idafa-lafziyya"], sifa_ar, sifa_en, sifa_tr))
    return [a, cited(w_full, "wajh", "noun", [SM], w_ar, w_en, w_tr, punct=punct, segments=w_segs)]

# ----------- s1: one pronoun — best, nine
S.append({"id": "s1", "translation": {
 "en": "And of the eighteen cases, those with one pronoun are the best, because the pronoun is just what is needed; they are nine — seven with the pronoun in the ṣifa, as حَسَنُ وَجْهٍ, and two with the pronoun in the governed word, as حَسَنٌ وَجْهُهُ." + C_EN,
 "tr": "On sekiz meseleden tek zamiri olanlar en iyisidir, çünkü zamir ihtiyaç kadardır; bunlar dokuzdur — yedisinde zamir sıfattadır, حَسَنُ وَجْهٍ gibi; ikisinde zamir ma'mûldedir, حَسَنٌ وَجْهُهُ gibi." + C_TR},
 "tokens": [
  atf_wa("وَمِنَ", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ.", "«and of».", "«ve ... -den».", "مِنَ"),
  W("الثَّمَانِيَ", "thamaniya", "noun", ["huruf-jarr", "asma-al-adad-fil-kafiya"], "مَجْرُورٌ لَفْظًا بِالْفَتْحِ — الْمُرَكَّبُ الْعَدَدِيُّ مَبْنِيٌّ.", "«the eighteen».", "«on sekiz»."),
  W("عَشْرَةَ", "ashara", "noun", ["asma-al-adad-fil-kafiya"], "الْجُزْءُ الثَّانِي مِنَ الْمُرَكَّبِ.", "— the second part.", "— ikinci cüz."),
  W("مَسْأَلَةً", "masala", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«cases».", "«mesele»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«those».", "«... olanlar»."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«with».", "«... olan».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("ضَمِيرٌ", "damir", "noun", ["mubtada-khabar", "ism-mawsul"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — صِلَةُ مَا.", "«a pronoun».", "«zamir»."),
  W("وَاحِدٌ", "wahid", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«one».", "«tek»."),
  W("أَحْسَنُ", "ahsan", "noun", ["mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«are the best».", "«en iyisidir».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الضَّمِيرَ", "damir", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the pronoun».", "«zamir»."),
  bi_("بِقَدْرِ", "qadr", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "قَدْرِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ أَنَّ.", "«is just what».", "«kadardır».", "قَدْرِ"),
  W("الْحَاجَةِ", "haja", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«is needed».", "«ihtiyaç».", punct="؛"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and they are».", "«ve bunlar».", "هِيَ"),
  W("تِسْعٌ", "tis", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "خَبَرٌ مَرْفُوعٌ.", "«nine».", "«dokuzdur».", punct=":"),
  W("سَبْعٌ", "sab-seven", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«seven».", "«yedisi»."),
  W("الضَّمِيرُ", "damir", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.", "«the pronoun».", "«zamir»."),
  FI(),
  W("الصِّفَةِ", "sifa", "noun", ["huruf-jarr", SM], "مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ، وَالْجُمْلَةُ خَبَرُ سَبْعٌ.", "«is in the ṣifa».", "«sıfattadır»."),
  nahwu(),
  *ex("حَسَنُ", "فِي مَحَلِّ جَرٍّ — فِيهِ ضَمِيرٌ يَعُودُ إِلَى الْمَوْصُوفِ.", "«ḥasanu» — the pronoun inside the ṣifa.", "«hasenü» — zamir sıfatın içinde.", "وَجْهٍ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wajhin».", "«vechin».", punct="،"),
  atf_wa("وَاثْنَتَانِ", "ithnatan", "noun", ["mubtada-khabar", "al-muthanna", "asma-al-adad-fil-kafiya"], "اثْنَتَانِ مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ.", "«and two».", "«ve ikisi».", "اثْنَتَانِ"),
  W("الضَّمِيرُ", "damir", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.", "«the pronoun».", "«zamir»."),
  FI(),
  W("الْمَعْمُولِ", "mamul", "noun", ["huruf-jarr"], "مَجْرُورٌ — خَبَرٌ.", "«is in the governed word».", "«ma'mûldedir»."),
  nahwu(),
  *ex("حَسَنٌ", "فِي مَحَلِّ جَرٍّ — لَا ضَمِيرَ فِيهِ.", "«ḥasanun» — no pronoun inside.", "«hasenün» — içinde zamir yok.", "وَجْهُهُ", "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الضَّمِيرُ هُنَا.", "«wajhuhu» — the pronoun is here.", "«vechuhû» — zamir burada.", w_segs=[seg("وَجْهُ", "wajh", "noun"), pr3ms()], punct="."),
 ]})

# ----------- s2: two pronouns — good, two
S.append({"id": "s2", "translation": {
 "en": "And those with two pronouns are good, not best, since the pronoun exceeds the need; they are two, with the governed word in naṣb: الْحَسَنُ وَجْهَهُ and حَسَنٌ وَجْهَهُ." + C_EN,
 "tr": "İki zamiri olanlar iyidir, en iyi değil; çünkü zamir ihtiyaçtan fazladır; bunlar ikidir, ma'mûl mansûb olarak: الْحَسَنُ وَجْهَهُ ve حَسَنٌ وَجْهَهُ." + C_TR},
 "tokens": [
  atf_wa("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and those».", "«ve ... olanlar».", "مَا"),
  W("فِيهِ", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«with».", "«... olan».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("ضَمِيرَانِ", "damir", "noun", ["mubtada-khabar", "al-muthanna", "ism-mawsul"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two pronouns».", "«iki zamir»."),
  W("فَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ زَائِدَةٌ فِي الْخَبَرِ لِشَبَهِ الْمُبْتَدَإِ بِالشَّرْطِ، وَهُوَ مُبْتَدَأٌ.", "«is».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  W("حَسَنٌ", "hasan-adj", "noun", ["mubtada-khabar", SM], "خَبَرٌ مَرْفُوعٌ.", "«good».", "«iyidir»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«değil»."),
  W("أَحْسَنُ", "ahsan", "noun", ["atf-nasaq", "ism-tafdil", "mamnu-min-sarf"], "مَعْطُوفٌ مَرْفُوعٌ.", "«best».", "«en iyi».", punct="،"),
  li_("لِزِيَادَةِ", "ziyada", "noun", ["idafa-definiteness"], "زِيَادَةِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«since … exceeds».", "«fazla olduğundan».", "زِيَادَةِ"),
  W("الضَّمِيرِ", "damir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the pronoun».", "«zamir»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«beyond».", "«-den»."),
  W("الْحَاجَةِ", "haja", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the need».", "«ihtiyaç».", punct="؛"),
  atf_wa("وَهُمَا", "pron-3d", "pron", ["mubtada-khabar"], "هُمَا ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and they are».", "«ve bunlar».", "هُمَا"),
  W("اثْنَتَانِ", "ithnatan", "noun", ["mubtada-khabar", "al-muthanna", "asma-al-adad-fil-kafiya"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two».", "«ikidir»."),
  bi_("بِنَصْبِ", "nasb", "noun", ["idafa-definiteness"], "نَصْبِ مَجْرُورٌ، وَهُوَ مُضَافٌ — حَالٌ.", "«with … in naṣb».", "«nasbıyla».", "نَصْبِ"),
  W("الْمَعْمُولِ", "mamul", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governed word».", "«ma'mûlün».", punct=":"),
  *ex("الْحَسَنُ", "فِي مَحَلِّ رَفْعٍ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — فِيهِ ضَمِيرٌ.", "«al-ḥasanu» — a pronoun inside.", "«el-hasenü» — içinde zamir var.", "وَجْهَهُ", "مَنْصُوبٌ عَلَى التَّشْبِيهِ بِالْمَفْعُولِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الضَّمِيرُ الثَّانِي.", "«wajhahu» — the second pronoun.", "«vechehû» — ikinci zamir.", w_segs=[seg("وَجْهَ", "wajh", "noun"), pr3ms()], punct="،"),
  *ex("حَسَنٌ", "فِيهِ ضَمِيرٌ.", "«and ḥasanun».", "«ve hasenün».", "وَجْهَهُ", "مَنْصُوبٌ عَلَى التَّشْبِيهِ بِالْمَفْعُولِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«wajhahu».", "«vechehû».", w_segs=[seg("وَجْهَ", "wajh", "noun"), pr3ms()], punct=".", joined=True),
 ]})

# ----------- s3: no pronoun — ugly, four
S.append({"id": "s3", "translation": {
 "en": "And those with no pronoun are ugly, for lack of any wording that ties them to the described noun; they are four, as الْحَسَنُ وَجْهٌ." + C_EN,
 "tr": "Hiç zamiri olmayanlar çirkindir, lafzen mevsûfa bağı bulunmadığından; bunlar dörttür, الْحَسَنُ وَجْهٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَمَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and those».", "«ve ... olanlar».", "مَا"),
  W("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ism-mawsul"], "لَا النَّافِيَةُ لِلْجِنْسِ.", "«no».", "«hiç ... yok»."),
  W("ضَمِيرَ", "damir", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«pronoun».", "«zamir»."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرُ لَا.", "«in them».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("فَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ زَائِدَةٌ فِي الْخَبَرِ، وَهُوَ مُبْتَدَأٌ.", "«is».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  W("قَبِيحٌ", "qabih", "noun", ["mubtada-khabar", SM], "خَبَرٌ مَرْفُوعٌ.", "«ugly».", "«çirkindir»."),
  li_("لِعَدَمِ", "adam", "noun", ["idafa-definiteness"], "عَدَمِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«for lack of».", "«bulunmadığından».", "عَدَمِ"),
  W("ارْتِبَاطِهِ", "irtibat", "noun", ["idafa-definiteness", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its tie».", "«bağı».", segments=[seg("ارْتِبَاطِ", "irtibat", "noun"), pr3msi()]),
  bi_("بِالْمَوْصُوفِ", "mawsuf", "noun", [], "الْمَوْصُوفِ مَجْرُورٌ.", "«to the described noun».", "«mevsûfa».", "الْمَوْصُوفِ"),
  W("لَفْظًا", "lafz", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ، أَوْ حَالٌ.", "«in wording».", "«lafzen».", punct="؛"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and they are».", "«ve bunlar».", "هِيَ"),
  W("أَرْبَعٌ", "arba", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "خَبَرٌ مَرْفُوعٌ.", "«four».", "«dörttür».", punct="،"),
  nahwu(),
  *ex("الْحَسَنُ", "فِي مَحَلِّ جَرٍّ — لَا ضَمِيرَ فِيهِ.", "«al-ḥasanu» — no pronoun.", "«el-hasenü» — zamir yok.", "وَجْهٌ", "فَاعِلٌ مَرْفُوعٌ — لَا ضَمِيرَ فِيهِ.", "«wajhun» — no pronoun.", "«vechün» — zamir yok.", punct="."),
 ]})

# ----------- s4: how the pronoun is known
S.append({"id": "s4", "translation": {
 "en": "And the pronoun in the governed word shows; as for the ṣifa, when you raise its governed word there is no pronoun in it, because the governed word is its doer and it is like the verb — and when you put it in naṣb or in jarr, there is in the ṣifa a pronoun returning to the described noun." + C_EN,
 "tr": "Ma'mûldeki zamir açıktır; sıfata gelince, ma'mûlünü ref' ettiğinde onda zamir yoktur, çünkü ma'mûl onun fâilidir ve o fiil gibidir — nasb veya cer ettiğinde ise sıfatta mevsûfa dönen bir zamir vardır." + C_TR},
 "tokens": [
  atf_wa("وَالضَّمِيرُ", "damir", "noun", ["mubtada-khabar"], "الضَّمِيرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the pronoun».", "«ve zamir».", "الضَّمِيرُ"),
  FI(),
  W("الْمَعْمُولِ", "mamul", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«in the governed word».", "«ma'mûlde»."),
  W("ظَاهِرٌ", "zahir", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«shows».", "«açıktır».", punct="؛"),
  atf_wa("وَأَمَّا", "amma-tafsil", "part", ["amma-tafsiliyya"], "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for».", "«... gelince».", "أَمَّا"),
  FI(),
  W("الصِّفَةِ", "sifa", "noun", ["huruf-jarr", SM], "مَجْرُورٌ.", "«the ṣifa».", "«sıfata»."),
  W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  W("رَفَعْتَ", "rafaa", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you raise».", "«ref' ettiğinde».", segments=[seg("رَفَعْ", "rafaa", "verb"), prTa()]),
  W("الْمَعْمُولَ", "mamul", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the governed word».", "«ma'mûlü»."),
  W("فَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "al-fa-fi-jawab-al-shart"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«there is no».", "«yoktur».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya-lil-jins", "part")]),
  W("ضَمِيرَ", "damir", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«pronoun».", "«zamir»."),
  W("فِيهَا", "fi", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "فِي حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَا.", "«in it».", "«onda».", punct="،", segments=[seg("فِي", "fi", "prep"), pr3fs()]),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الْمَعْمُولَ", "mamul", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the governed word».", "«ma'mûl»."),
  W("فَاعِلُهَا", "fail-doer", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its doer».", "«onun fâilidir».", segments=[seg("فَاعِلُ", "fail-doer", "noun"), pr3fs()]),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  ka_("كَالْفِعْلِ", "fil", "noun", ["khabar-al-mubtada-wa-ahkamuh"], "الْفِعْلِ مَجْرُورٌ — خَبَرٌ.", "«is like the verb».", "«fiil gibidir».", "الْفِعْلِ", punct="؛"),
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -diğinde».", "إِذَا"),
  W("نَصَبْتَهُ", "nasaba-nahw", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«you put it in naṣb».", "«nasb ettiğinde».", segments=[seg("نَصَبْ", "nasaba-nahw", "verb"), prTa(), pr3ms()]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("جَرَرْتَهُ", "jarra", "verb", ["atf-nasaq", "fail", "maful-bihi", "doubled-verbs"], "فِعْلٌ مَاضٍ مَعْطُوفٌ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«in jarr».", "«cer ettiğinde».", segments=[seg("جَرَرْ", "jarra", "verb"), prTa(), pr3ms()]),
  W("فَفِيهَا", "fi", "prep", ["huruf-jarr", "al-fa-fi-jawab-al-shart", "khabar-al-mubtada-wa-ahkamuh"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَفِيهَا جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ.", "«there is in it».", "«onda ... vardır».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep"), pr3fs()]),
  W("ضَمِيرٌ", "damir", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a pronoun».", "«bir zamir»."),
  W("يَعُودُ", "ada-return", "verb", ["naat-sifa", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ صِفَةٌ لِضَمِيرٌ.", "«returning».", "«dönen»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْمَوْصُوفِ", "mawsuf", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the described noun».", "«mevsûfa».", punct="."),
 ]})

# ----------- s5: agreement
S.append({"id": "s5", "translation": {
 "en": "And when the described noun is feminine, dual or plural, the ṣifa comes likewise — as in هِنْدٌ حَسَنَةُ وَجْهٍ and حَسَنَةٌ وَجْهًا, الزَّيْدَانِ حَسَنَا وَجْهٍ and حَسَنَانِ وَجْهًا, الزَّيْدُونَ حَسَنُو وَجْهٍ and حَسَنُونَ وَجْهًا." + C_EN,
 "tr": "Mevsûf müennes, tesniye veya cemi olduğunda sıfat da öyle gelir — هِنْدٌ حَسَنَةُ وَجْهٍ ve حَسَنَةٌ وَجْهًا, الزَّيْدَانِ حَسَنَا وَجْهٍ ve حَسَنَانِ وَجْهًا, الزَّيْدُونَ حَسَنُو وَجْهٍ ve حَسَنُونَ وَجْهًا gibi." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... olduğunda».", "إِذَا"),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«olursa»."),
  W("الْمَوْصُوفُ", "mawsuf", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the described noun».", "«mevsûf»."),
  W("مُؤَنَّثًا", "muannath", "noun", ["kana-wa-akhawatuha", "al-muannath-wa-alamatuh"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«feminine».", "«müennes»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("مُثَنًّى", "muthanna", "noun", ["atf-nasaq", "al-muthanna"], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«dual».", "«tesniye»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("مَجْمُوعًا", "majmu", "noun", ["atf-nasaq", "jam-mudhakkar-salim"], "مَعْطُوفٌ مَنْصُوبٌ.", "«plural».", "«cemi»."),
  W("جَاءَتِ", "jaa", "verb", ["fail", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — جَوَابُ إِذَا.", "«comes».", "«gelir»."),
  W("الصِّفَةُ", "sifa", "noun", ["fail", SM], "فَاعِلٌ مَرْفُوعٌ.", "«the ṣifa».", "«sıfat»."),
  W("كَذَلِكَ", "kadhalika", "part", ["hal"], "الْكَافُ حَرْفُ جَرٍّ، وَذَلِكَ فِي مَحَلِّ جَرٍّ — حَالٌ.", "«likewise».", "«öyle».", punct="،"),
  nahwu(),
  cited("هِنْدٌ", "hind", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Hind».", "«Hind»."),
  *ex("حَسَنَةُ", "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مُؤَنَّثٌ لِلْمَوْصُوفِ.", "«beautiful of» — feminine.", "«güzel» — müennes.", "وَجْهٍ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«face».", "«yüzlü»."),
  *ex("حَسَنَةٌ", "خَبَرٌ مَرْفُوعٌ.", "«and beautiful».", "«ve güzel».", "وَجْهًا", "تَمْيِيزٌ مَنْصُوبٌ.", "«of face».", "«yüz bakımından».", punct="،", joined=True),
  cited_wa("وَالزَّيْدَانِ", "zayd", "propn", ["mubtada-khabar", "al-muthanna"], "الزَّيْدَانِ مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ.", "«and the two Zayds».", "«ve iki Zeyd».", "الزَّيْدَانِ"),
  *ex("حَسَنَا", "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«beautiful of» — dual, the nūn dropped for the annexation.", "«güzel» — tesniye, nûnu izâfetle düşmüş.", "وَجْهٍ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«face».", "«yüzlü»."),
  *ex("حَسَنَانِ", "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«and beautiful».", "«ve güzel».", "وَجْهًا", "تَمْيِيزٌ مَنْصُوبٌ.", "«of face».", "«yüz bakımından».", punct="،", joined=True),
  cited_wa("وَالزَّيْدُونَ", "zayd", "propn", ["mubtada-khabar", "jam-mudhakkar-salim"], "الزَّيْدُونَ مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ.", "«and the Zayds».", "«ve Zeydler».", "الزَّيْدُونَ"),
  *ex("حَسَنُو", "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«beautiful of» — plural, the nūn dropped.", "«güzel» — cemi, nûnu düşmüş.", "وَجْهٍ", "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«face».", "«yüzlü»."),
  *ex("حَسَنُونَ", "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ.", "«and beautiful».", "«ve güzel».", "وَجْهًا", "تَمْيِيزٌ مَنْصُوبٌ.", "«of face».", "«yüz bakımından».", punct=".", joined=True),
 ]})

# ----------- s6: the participles that follow
S.append({"id": "s6", "translation": {
 "en": "And the ism fāʿil of the intransitive verb and the ism mafʿūl of the verb transitive to one object are like the ṣifa mushabbaha in the eighteen — as in زَيْدٌ قَائِمٌ الْأَبُ, قَائِمٌ الْأَبَ and قَائِمُ الْأَبِ; and زَيْدٌ مَضْرُوبٌ الْأَبُ, مَضْرُوبٌ الْأَبَ and مَضْرُوبُ الْأَبِ." + C_EN,
 "tr": "Lâzım fiilin ism-i fâili ile bir mef'ûle müteaddî fiilin ism-i mef'ûlü on sekizde sıfat-ı müşebbehe gibidir — زَيْدٌ قَائِمٌ الْأَبُ، قَائِمٌ الْأَبَ، قَائِمُ الْأَبِ; ve زَيْدٌ مَضْرُوبٌ الْأَبُ، مَضْرُوبٌ الْأَبَ، مَضْرُوبُ الْأَبِ gibi." + C_TR},
 "tokens": [
  atf_wa("وَاسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness"], "اسْمُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the noun of».", "«ve ism-i».", "اسْمُ"),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("اللَّازِمِ", "lazim", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the intransitive».", "«lâzım»."),
  atf_wa("وَاسْمُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness"], "اسْمُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the noun of».", "«ve ism-i».", "اسْمُ"),
  W("الْمَفْعُولِ", "maful-noun", "noun", ["idafa-definiteness", IM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the object».", "«mef'ûl»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("الْمُتَعَدِّي", "mutaaddi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the transitive».", "«müteaddî»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("وَاحِدٍ", "wahid", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«one».", "«bir»."),
  ka_("كَالصِّفَةِ", "sifa", "noun", ["khabar-al-mubtada-wa-ahkamuh", SM], "الصِّفَةِ مَجْرُورٌ — خَبَرٌ.", "«are like the ṣifa».", "«sıfat gibidir».", "الصِّفَةِ"),
  W("الْمُشَبَّهَةِ", "mushabbaha", "noun", ["naat-sifa", SM], "صِفَةٌ مَجْرُورَةٌ.", "«mushabbaha».", "«müşebbehe»."),
  FI(),
  W("الثَّمَانِيَ", "thamaniya", "noun", ["huruf-jarr", "asma-al-adad-fil-kafiya"], "مَجْرُورٌ لَفْظًا بِالْفَتْحِ.", "«the eighteen».", "«on sekizde»."),
  W("عَشْرَةَ", "ashara", "noun", ["asma-al-adad-fil-kafiya"], "الْجُزْءُ الثَّانِي.", "— the second part.", "— ikinci cüz.", punct="،"),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar", IF], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ لَازِمٍ.", "«standing».", "«ayakta»."),
  cited("الْأَبُ", "ab", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the father» — the doer.", "«baba» — fâil.", punct="،"),
  cited_wa("وَقَائِمٌ", "qaim", "noun", [IF], "قَائِمٌ مَعْطُوفٌ.", "«and standing».", "«ve ayakta».", "قَائِمٌ"),
  cited("الْأَبَ", "ab", "noun", ["maful-bihi"], "مَنْصُوبٌ عَلَى التَّشْبِيهِ بِالْمَفْعُولِ.", "«the father» — like an object.", "«baba» — mef'ûle benzetilerek.", punct="،"),
  cited_wa("وَقَائِمُ", "qaim", "noun", [IF, "idafa-lafziyya"], "قَائِمُ مَعْطُوفٌ، وَهُوَ مُضَافٌ.", "«and standing of».", "«ve ayakta».", "قَائِمُ"),
  cited("الْأَبِ", "ab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the father».", "«babası».", punct="؛"),
  cited_wa("وَزَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "زَيْدٌ مُبْتَدَأٌ.", "«and Zayd».", "«ve Zeyd».", "زَيْدٌ"),
  cited("مَضْرُوبٌ", "madrub", "noun", ["mubtada-khabar", IM], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ مُتَعَدٍّ إِلَى وَاحِدٍ.", "«struck».", "«vurulmuş»."),
  cited("الْأَبُ", "ab", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the father» — the deputy doer.", "«baba» — nâib-i fâil.", punct="،"),
  cited_wa("وَمَضْرُوبٌ", "madrub", "noun", [IM], "مَضْرُوبٌ مَعْطُوفٌ.", "«and struck».", "«ve vurulmuş».", "مَضْرُوبٌ"),
  cited("الْأَبَ", "ab", "noun", ["maful-bihi"], "مَنْصُوبٌ عَلَى التَّشْبِيهِ بِالْمَفْعُولِ.", "«the father».", "«baba».", punct="،"),
  cited_wa("وَمَضْرُوبُ", "madrub", "noun", [IM, "idafa-lafziyya"], "مَضْرُوبُ مَعْطُوفٌ، وَهُوَ مُضَافٌ.", "«and struck of».", "«ve vurulmuş».", "مَضْرُوبُ"),
  cited("الْأَبِ", "ab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the father».", "«babası».", punct="."),
 ]})

# ----------- s7: the restriction
S.append({"id": "s7", "translation": {
 "en": "But the doer of a transitive verb's ism fāʿil, and the deputy doer of an ism mafʿūl, can only be marfūʿ — never manṣūb or majrūr." + C_EN,
 "tr": "Ancak müteaddî fiilin ism-i fâilinin fâili ve ism-i mef'ûlün nâib-i fâili yalnız merfû olur — mansûb ve mecrûr olmaz." + C_TR},
 "tokens": [
  atf_wa("وَفَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "idafa-definiteness"], "فَاعِلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«but the doer of».", "«ancak fâili».", "فَاعِلُ"),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness", IF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  W("الْمُتَعَدِّي", "mutaaddi", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«transitive».", "«müteaddî»."),
  atf_wa("وَنَائِبُ", "naib", "noun", ["mubtada-khabar", "idafa-definiteness", "naib-al-fail"], "نَائِبُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the deputy».", "«ve nâib-i».", "نَائِبُ"),
  W("فَاعِلِ", "fail-doer", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«doer of».", "«fâili»."),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْمَفْعُولِ", "maful-noun", "noun", ["idafa-definiteness", IM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the object».", "«mef'ûlün»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  W("يَكُونَانِ", "kana", "verb", ["kana-wa-akhawatuha", "mubtada-khabar", "al-muthanna"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ اسْمُهَا — وَالْجُمْلَةُ خَبَرٌ.", "«can be».", "«olurlar»."),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ حَصْرٍ.", "«only».", "«yalnız»."),
  W("مَرْفُوعَيْنِ", "marfu", "noun", ["kana-wa-akhawatuha", "al-muthanna"], "خَبَرُ يَكُونَانِ مَنْصُوبٌ بِالْيَاءِ.", "«marfūʿ».", "«merfû».", punct="."),
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
 "ithnatan": need("ithnatan", "اِثْنَتَانِ", None, "noun", "two (feminine) — declined like a dual", "iki (müennes) — tesniye gibi çekilir", 2),
 "irtibat": need("irtibat", "اِرْتِبَاط", "ر ب ط", "noun", "a tie, connection — the maṣdar of اِرْتَبَطَ", "irtibat, bağ — irtebata'nın masdarı", 4),
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
print("kafiya ch18 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "مَسَائِلُ الصِّفَةِ الْمُشَبَّهَةِ الثَّمَانِيَ عَشْرَةَ", "en": "The eighteen cases of the ṣifa mushabbaha graded: one pronoun is best, two is good, none is ugly — and how the pronoun is found, how the ṣifa agrees, and which participles share the grid", "tr": "Sıfat-ı müşebbehenin on sekiz meselesi derecelendirilir: tek zamir en iyi, iki iyi, hiç çirkin — zamir nasıl bulunur, sıfat nasıl uyar, hangi ismler tabloyu paylaşır"},
 "level": 5, "group": "nahw",
 "classicalSources": ["ضياء صونغور اوغلى — دفتر الكافية: ما فيه ضمير واحد أحسن (تسع)، ما فيه ضميران حسن (اثنتان)، ما لا ضمير فيه قبيح (أربع)؛ الضمير في المعمول ظاهر وفي الصفة بحسب رفع المعمول؛ مطابقة الصفة للموصوف؛ اسم الفاعل من اللازم واسم المفعول من المتعدي إلى واحد كالصفة المشبهة", "شرح الرضي على الكافية — باب الصفة المشبهة: تقسيم المسائل وما يحسن منها وما يقبح"],
 "question": {
  "en": ["How are the sixteen live cases ranked? By counting pronouns. The ṣifa must tie back to its described noun exactly once: one pronoun is BEST (nine cases), two is merely GOOD (two cases), none is UGLY (four cases). Lightness is the measure throughout the chapter.",
         "Where does the pronoun hide? In the governed word it is visible (وَجْهُهُ). In the ṣifa it is there only when the ṣifa is NOT raising its governed word: حَسَنٌ وَجْهُهُ has the noun as doer and the ṣifa works like a verb with no pronoun of its own; حَسَنٌ وَجْهَهُ and حَسَنُ وَجْهٍ have the noun in naṣb or jarr, so a pronoun inside the ṣifa stands for the described noun.",
         "Which nine are best? The seven in which the ṣifa carries the pronoun and the noun is not annexed to one (حَسَنُ وَجْهٍ، حَسَنُ الْوَجْهِ، حَسَنٌ وَجْهًا، الْحَسَنُ الْوَجْهِ …), and the two in which the pronoun sits on the raised noun (حَسَنٌ وَجْهُهُ، الْحَسَنُ وَجْهُهُ).",
         "Which four are ugly? Those with no pronoun anywhere — الْحَسَنُ وَجْهٌ and its kin — because nothing in the wording ties the phrase to زَيْدٌ at all.",
         "Does the ṣifa agree? Fully: هِنْدٌ حَسَنَةُ وَجْهٍ, الزَّيْدَانِ حَسَنَا وَجْهٍ, الزَّيْدُونَ حَسَنُو وَجْهٍ — and in annexation the dual and plural drop their nūn (حَسَنَا، حَسَنُو), exactly as the IdafaEngine builds them.",
         "Who else lives in this grid? The ism fāʿil of an intransitive verb (قَائِمٌ الْأَبُ / الْأَبَ / الْأَبِ) and the ism mafʿūl of a one-object verb (مَضْرُوبٌ الْأَبُ / الْأَبَ / الْأَبِ): both may take their noun in all three cases. A transitive verb's ism fāʿil and any ism mafʿūl keep their doer or deputy doer in rafʿ only.",
         "What does the engine do? The IdafaEngine drops the nūn of حَسَنَا and حَسَنُو and the TartibEngine keeps the described noun first; the eighteen-cell table itself is the kind of exact, enumerable rule the drill bank can replay cell by cell."],
  "tr": ["On altı canlı mesele nasıl sıralanır? Zamir sayarak. Sıfat mevsûfuna tam bir kez bağlanmalıdır: tek zamir EN İYİ (dokuz mesele), iki yalnızca İYİ (iki mesele), hiç ÇİRKİN (dört mesele). Bâb boyunca ölçü hafifliktir.",
         "Zamir nerede saklanır? Ma'mûlde görünür (وَجْهُهُ). Sıfatta yalnız sıfat ma'mûlünü ref' ETMEDİĞİNDE vardır: حَسَنٌ وَجْهُهُ'da isim fâildir ve sıfat kendi zamiri olmayan bir fiil gibi çalışır; حَسَنٌ وَجْهَهُ ve حَسَنُ وَجْهٍ'de isim nasb ya da cerdedir, dolayısıyla sıfatın içindeki bir zamir mevsûfu temsil eder.",
         "En iyi dokuz hangileridir? Sıfatın zamiri taşıdığı ve ismin zamire muzâf olmadığı yedisi (حَسَنُ وَجْهٍ، حَسَنُ الْوَجْهِ، حَسَنٌ وَجْهًا، الْحَسَنُ الْوَجْهِ …) ile zamirin ref'edilmiş isimde oturduğu ikisi (حَسَنٌ وَجْهُهُ، الْحَسَنُ وَجْهُهُ).",
         "Çirkin dört hangileridir? Hiçbir yerde zamiri olmayanlar — الْحَسَنُ وَجْهٌ ve benzerleri — çünkü lafızda ibareyi زَيْدٌ'e bağlayan hiçbir şey yoktur.",
         "Sıfat uyar mı? Tamamen: هِنْدٌ حَسَنَةُ وَجْهٍ, الزَّيْدَانِ حَسَنَا وَجْهٍ, الزَّيْدُونَ حَسَنُو وَجْهٍ — izâfette tesniye ve cemi nûnunu düşürür (حَسَنَا، حَسَنُو), tam IdafaEngine'in kurduğu gibi.",
         "Bu tabloda başka kim yaşar? Lâzım fiilin ism-i fâili (قَائِمٌ الْأَبُ / الْأَبَ / الْأَبِ) ve bir mef'ûllü fiilin ism-i mef'ûlü (مَضْرُوبٌ الْأَبُ / الْأَبَ / الْأَبِ): ikisi de ismini üç hâlde alabilir. Müteaddî fiilin ism-i fâili ve her ism-i mef'ûl fâilini ya da nâib-i fâilini yalnız ref'te tutar.",
         "Motor ne yapar? IdafaEngine حَسَنَا ve حَسَنُو'nun nûnunu düşürür, TartibEngine mevsûfu önde tutar; on sekiz hücreli tablonun kendisi, tatbik bankasının hücre hücre tekrar oynatabileceği türden kesin, sayılabilir bir kuraldır."]},
 "plain": {
  "en": "Of the eighteen ways to say «Zayd is beautiful of face», the best have exactly one pronoun pointing back at Zayd, two pronouns is acceptable, and none at all is ugly. The adjective agrees with Zayd in gender and number, and a few participles can use the same grid.",
  "tr": "«Zeyd yüzü güzel» demenin on sekiz yolundan en iyileri Zeyd'e dönen tam bir zamir taşır; iki zamir kabul edilir, hiç zamir çirkindir. Sıfat Zeyd'e cinsiyet ve sayıda uyar ve birkaç ism aynı tabloyu kullanabilir."},
 "explanation": {
  "en": "The previous chapter counted eighteen cells and emptied two; this one grades the sixteen that remain, and the yardstick is a single idea — the ṣifa must be tied to the noun it describes, once. A pronoun does the tying. Where it sits is not arbitrary: in the governed word it is written (وَجْهُهُ), and in the ṣifa it exists exactly when the ṣifa is not acting as a verb, that is, when its noun is in naṣb or jarr rather than raised as its doer. Counting pronouns then sorts the cells: one tie is best and gives nine cases, two ties are a redundancy the grammarians tolerate and give two, no tie leaves the phrase floating and gives four they call ugly. The agreement rule follows naturally — a ṣifa that stands for a feminine, dual or plural noun takes that noun's form, and in the annexed cases the dual and plural lose their nūn as every muḍāf does. The last two sentences widen the grid: an intransitive verb's ism fāʿil and a one-object verb's ism mafʿūl have a noun after them that can play the same three roles, so قَائِمٌ الْأَبُ and مَضْرُوبُ الْأَبِ sit in the same table; but a transitive verb's ism fāʿil already owes its noun a case, and the doer of such a participle and the deputy doer of any ism mafʿūl keep their rafʿ. The chapter is the notebook's own exposition rather than the matn, and it is kept as commentary.",
  "tr": "Önceki bâb on sekiz hücre sayıp ikisini boşalttı; bu bâb kalan on altıyı derecelendirir ve ölçü tek bir fikirdir — sıfat nitelediği isme bir kez bağlanmalıdır. Bağlamayı zamir yapar. Nerede oturduğu keyfî değildir: ma'mûlde yazılıdır (وَجْهُهُ), sıfatta ise tam olarak sıfat fiil gibi davranmadığında, yani ismi fâil olarak ref'edilmek yerine nasb ya da cerdeyken vardır. Zamir saymak sonra hücreleri sıralar: tek bağ en iyidir ve dokuz mesele verir, iki bağ nahivcilerin hoş gördüğü bir fazlalıktır ve iki verir, hiç bağ ibareyi havada bırakır ve çirkin dedikleri dört verir. Uyum kuralı doğal olarak izler — müennes, tesniye ya da cemi bir ismin yerine duran sıfat o ismin biçimini alır ve muzâf hâllerde tesniye ile cemi her muzâf gibi nûnunu kaybeder. Son iki cümle tabloyu genişletir: lâzım fiilin ism-i fâili ile bir mef'ûllü fiilin ism-i mef'ûlünün ardında aynı üç rolü oynayabilen bir isim vardır; böylece قَائِمٌ الْأَبُ ve مَضْرُوبُ الْأَبِ aynı tabloda oturur; ama müteaddî fiilin ism-i fâili ismine zaten bir hâl borçludur ve böyle bir ismin fâili ile her ism-i mef'ûlün nâib-i fâili ref'ini korur. Bâb metin değil defterin kendi açıklamasıdır ve şerh olarak tutulur."},
 "examples": [
  {"ar": "حَسَنُ وَجْهٍ — حَسَنٌ وَجْهُهُ", "en": "One pronoun: in the ṣifa, or in the governed word.", "tr": "Tek zamir: sıfatta ya da ma'mûlde.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "الْحَسَنُ وَجْهَهُ، حَسَنٌ وَجْهَهُ", "en": "Two pronouns: good, not best.", "tr": "İki zamir: iyi, en iyi değil.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "الْحَسَنُ وَجْهٌ", "en": "No pronoun: ugly.", "tr": "Zamirsiz: çirkin.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "هِنْدٌ حَسَنَةُ وَجْهٍ، الزَّيْدَانِ حَسَنَا وَجْهٍ، الزَّيْدُونَ حَسَنُو وَجْهٍ", "en": "Agreement, with the nūn dropped in annexation.", "tr": "Uyum; izâfette nûn düşer.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "زَيْدٌ قَائِمٌ الْأَبُ، قَائِمٌ الْأَبَ، قَائِمُ الْأَبِ", "en": "The intransitive participle in the same grid.", "tr": "Lâzım fiilin ism-i fâili aynı tabloda.", "sourceStory": "al-kafiya", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«حَسَنٌ وَجْهُهُ — sıfatta zamir var»",
   "right": "«ma'mûl merfû olunca sıfatta zamir yoktur; وَجْهُهُ fâildir ve zamir ondadır»",
   "why": {"en": "A ṣifa raising its noun works like a verb and has no pronoun of its own.", "tr": "İsmini ref' eden sıfat fiil gibi çalışır ve kendi zamiri yoktur."}},
  {"wrong": "«الزَّيْدَانِ حَسَنَانِ وَجْهٍ»",
   "right": "«الزَّيْدَانِ حَسَنَا وَجْهٍ — muzâf tesniye nûnunu düşürür; حَسَنَانِ وَجْهًا ise temyizle»",
   "why": {"en": "In annexation the dual's nūn goes; keep the nūn only when the noun stands as a tamyīz.", "tr": "İzâfette tesniyenin nûnu gider; nûn yalnız isim temyiz olduğunda kalır."}},
  {"wrong": "«زَيْدٌ ضَارِبُ الْأَبِ — fâil mecrûr»",
   "right": "«müteaddî fiilin ism-i fâilinin fâili yalnız merfû olur; الْأَبِ burada mef'ûldür»",
   "why": {"en": "The three-case licence belongs to intransitive participles and the ṣifa; a transitive participle's doer stays marfūʿ.", "tr": "Üç hâl ruhsatı lâzım ismlere ve sıfata aittir; müteaddî ismin fâili merfû kalır."}}],
 "relatedNotes": ["al-sifa-al-mushabbaha-fil-kafiya", SM, "idafa-lafziyya", IF, IM]}

ADD_EN = (" Chapter 18 (notebook lines ~266-273): the notebook's grading of the eighteen cases of the ṣifa mushabbaha (one pronoun best — nine; two good — two; none ugly — four), how the pronoun is found, the ṣifa's agreement "
          "with a feminine, dual or plural described noun, and the two participles that share the grid with the one restriction on them — all the notebook's own exposition, kept as commentary (s1-s7).")
ADD_TR = (" On sekizinci bâb (defter satırları ~266-273): sıfat-ı müşebbehenin on sekiz meselesinin defterdeki derecelendirmesi (tek zamir en iyi — dokuz; iki iyi — iki; hiç çirkin — dört), zamirin nasıl bulunduğu, sıfatın müennes, "
          "tesniye ya da cemi mevsûfa uyumu ve tabloyu paylaşan iki ism ile onlara dair tek kayıt — hepsi defterin kendi açıklaması, şerh olarak tutulmuştur (s1-s7).")
write_out(18, S, TITLE, ADD_EN, ADD_TR, "266-273", GLOSS_ADD, notes=(NOTE,),
          related=(("al-sifa-al-mushabbaha-fil-kafiya", [K]), (SM, [K])))
report(18, S, GLOSS_ADD, (NOTE,))
