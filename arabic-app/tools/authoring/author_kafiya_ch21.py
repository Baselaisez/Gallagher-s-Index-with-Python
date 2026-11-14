# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 21: THE NĀṢIBS OF THE MUḌĀRIʿ. Rafʿ when bare of nāṣib and jāzim; naṣb by أَنْ، لَنْ، كَيْ، إِذَنْ and by a hidden
أَنْ after حَتَّى, the lām of كَيْ, the lām of denial, the fāʾ, the wāw and أَوْ; the notebook's account of each: أَنْ turns the clause into a
maṣdar (أُرِيدُ أَنْ تُحْسِنَ إِلَيَّ، أَنْ تَصُومُوا خَيْرٌ لَكُمْ) and after verbs of certainty is the lightened أَنَّ; لَنْ denies the future with
emphasis, not for ever; إِذَنْ needs two conditions; كَيْ is cause; حَتَّى in the sense of كَيْ or إِلَى, or a particle of beginning before a
present; the fāʾ after the six (command, prohibition, question, negation, wish, offer), the wāw of joining, أَوْ as إِلَى أَنْ / إِلَّا أَنْ, the
hidden أَنْ after a conjunction on a plain noun, and when أَنْ may or must be written out (لِئَلَّا).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~296-301 of the transcription.

  RESTORED (received matn, marked): s1, s2. COMMENTARY (the notebook): s3-s11.
  DIVERGENCES recorded in the manifest: the notebook's فَأَشْرَبَهَا is read فَأَشْرَبَهُ (مَاء is masculine); its لَأُلْزِمَنَّكَ is cited in Form I, لَأَلْزَمَنَّكَ.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch21.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "nawasib-al-mudari-fil-kafiya"
NJ = "nawasib-wa-jawazim-al-mudari"
JT = "jawab-al-talab"
TITLE = {"ar": "نَوَاصِبُ الْمُضَارِعِ", "en": "The nāṣibs of the muḍāriʿ", "tr": "Muzârinin nasb edicileri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
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
def AN_HIDDEN(): return W("مُضْمَرَةٍ", "mudmar", "noun", ["naat-sifa", NJ, "hadhf-wa-taqdir"], "صِفَةٌ لِأَنْ مَجْرُورَةٌ.", "«hidden».", "«gizli».")
def NASB_V(full, lex, en, tr, punct=None, segs=None, extra=""):
    return cited(full, lex, "verb", [NJ, "fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ" + extra + ".", en, tr, punct=punct, segments=segs)
def JANNA(punct=None): return cited("الْجَنَّةَ", "janna", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Paradise».", "«cennete».", punct=punct)
def ASLAMTU(): return cited("أَسْلَمْتُ", "aslama", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I became Muslim».", "«müslüman oldum».", segments=[seg("أَسْلَمْ", "aslama", "verb"), prT()])

# ----------- s1 (RESTORED): rafʿ
S.append({"id": "s1", "translation": {
 "en": "And the muḍāriʿ takes rafʿ when it is bare of a nāṣib and a jāzim — as يَقُومُ زَيْدٌ." + R_EN,
 "tr": "Muzâri, nasb edici ve cezm ediciden soyulduğunda merfû olur — يَقُومُ زَيْدٌ gibi." + R_TR},
 "tokens": [
  atf_wa("وَيُرْفَعُ", "rafaa", "verb", ["naib-al-fail"], "يُرْفَعُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and … takes rafʿ».", "«ve merfû olur».", "يُرْفَعُ"),
  W("الْمُضَارِعُ", "mudari", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the muḍāriʿ».", "«muzâri»."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  W("تَجَرَّدَ", "tajarrada", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«it is bare».", "«soyulduğunda»."),
  W("عَنِ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of».", "«-den»."),
  W("النَّاصِبِ", "nasib", "noun", ["huruf-jarr", NJ], "مَجْرُورٌ.", "«a nāṣib».", "«nasb edici»."),
  atf_wa("وَالْجَازِمِ", "jazim", "noun", [NJ], "الْجَازِمِ مَعْطُوفٌ مَجْرُورٌ.", "«and a jāzim».", "«ve cezm edici».", "الْجَازِمِ", punct="،"),
  nahwu(),
  cited("يَقُومُ", "qama", "verb", ["idafa-definiteness", "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — لَا نَاصِبَ وَلَا جَازِمَ.", "«stands».", "«kalkar»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct="."),
 ]})

# ----------- s2 (RESTORED): the nāṣibs
S.append({"id": "s2", "translation": {
 "en": "And it takes naṣb by أَنْ, لَنْ, كَيْ and إِذَنْ, and by a hidden أَنْ after حَتَّى, the lām of كَيْ, the lām of denial, the fāʾ, the wāw and أَوْ." + R_EN,
 "tr": "أَنْ, لَنْ, كَيْ ve إِذَنْ ile, ve حَتَّى, kéy lâmı, cuhûd lâmı, fâ, vâv ve أَوْ'den sonra gizli bir أَنْ ile mansûb olur." + R_TR},
 "tokens": [
  atf_wa("وَيُنْصَبُ", "nasaba-nahw", "verb", ["naib-al-fail", NJ], "يُنْصَبُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it takes naṣb».", "«ve mansûb olur».", "يُنْصَبُ"),
  bi_("بِأَنْ", "an-nasiba", "part", [NJ], "أَنْ فِي مَحَلِّ جَرٍّ — حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«by an».", "«en ile».", "أَنْ"),
  cited_wa("وَلَنْ", "lan", "part", [NJ], "لَنْ مَعْطُوفٌ.", "«and lan».", "«ve len».", "لَنْ"),
  cited_wa("وَكَيْ", "kay", "part", [NJ], "كَيْ مَعْطُوفٌ.", "«and kay».", "«ve key».", "كَيْ"),
  cited_wa("وَإِذَنْ", "idhan-jawab", "part", [NJ], "إِذَنْ مَعْطُوفٌ.", "«and idhan».", "«ve izen».", "إِذَنْ", punct="،"),
  atf_wa("وَبِأَنْ", "an-nasiba", "part", [NJ, "hadhf-wa-taqdir"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَنْ فِي مَحَلِّ جَرٍّ.", "«and by an».", "«ve en ile».", "أَنْ", extra_segs=[seg("بِ", "bi", "prep"), seg("أَنْ", "an-nasiba", "part")]),
  AN_HIDDEN(),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... -den sonra»."),
  cited("حَتَّى", "hatta", "part", ["idafa-definiteness", NJ], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«ḥattā».", "«hattâ»."),
  atf_wa("وَلَامِ", "lam-letter", "noun", ["idafa-definiteness", NJ], "لَامِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the lām of».", "«ve lâmı».", "لَامِ"),
  cited("كَيْ", "kay", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — لَامُ التَّعْلِيلِ.", "«kay» — the lām of purpose.", "«key» — ta'lil lâmı."),
  atf_wa("وَلَامِ", "lam-letter", "noun", ["idafa-definiteness", NJ], "لَامِ مَعْطُوفٌ، وَهُوَ مُضَافٌ.", "«and the lām of».", "«ve lâmı».", "لَامِ"),
  W("الْجُحُودِ", "juhud", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — بَعْدَ مَا كَانَ وَلَمْ يَكُنْ.", "«denial» — after مَا كَانَ.", "«cuhûd» — مَا كَانَ'den sonra."),
  atf_wa("وَالْفَاءِ", "fa", "conj", [NJ, JT], "الْفَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and the fāʾ».", "«ve fâ».", "الْفَاءِ"),
  atf_wa("وَالْوَاوِ", "waw-letter", "noun", [NJ, "anwa-al-waw"], "الْوَاوِ مَعْطُوفٌ مَجْرُورٌ.", "«and the wāw».", "«ve vâv».", "الْوَاوِ"),
  cited_wa("وَأَوْ", "aw", "conj", [NJ], "أَوْ مَعْطُوفٌ.", "«and aw».", "«ve ev».", "أَوْ", punct="."),
 ]})

# ----------- s3 (COMMENTARY): أَنْ
S.append({"id": "s3", "translation": {
 "en": "So أَنْ puts the muḍāriʿ in naṣb and gives the clause the sense of a maṣdar — as أُرِيدُ أَنْ تُحْسِنَ إِلَيَّ, and أَنْ تَصُومُوا خَيْرٌ لَكُمْ, where the naṣb of تَصُومُوا is by dropping the nūn." + C_EN,
 "tr": "أَنْ muzâriyi nasb eder ve cümleye masdar mânâsı verdirir — أُرِيدُ أَنْ تُحْسِنَ إِلَيَّ ve أَنْ تَصُومُوا خَيْرٌ لَكُمْ gibi; تَصُومُوا'nun nasbı nûnun hazfiyledir." + C_TR},
 "tokens": [
  W("فَأَنْ", "an-nasiba", "part", ["mubtada-khabar", NJ, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَأَنْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«so an».", "«en».", segments=[seg("فَ", "fa", "conj"), seg("أَنْ", "an-nasiba", "part")]),
  W("تَنْصِبُ", "nasaba-nahw", "verb", ["fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ خَبَرٌ.", "«puts … in naṣb».", "«nasb eder»."),
  W("الْمُضَارِعَ", "mudari", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the muḍāriʿ».", "«muzâriyi»."),
  atf_wa("وَتَجْعَلُ", "jaala", "verb", ["fail", "mafulayn"], "تَجْعَلُ فِعْلٌ مُضَارِعٌ مَعْطُوفٌ.", "«and gives».", "«ve kılar».", "تَجْعَلُ"),
  W("الْجُمْلَةَ", "jumla", "noun", ["mafulayn"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ.", "«the clause».", "«cümleyi»."),
  W("فِي", "fi", "prep", ["huruf-jarr", "mafulayn"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مَفْعُولٌ ثَانٍ.", "«in».", "«-de»."),
  W("مَعْنَى", "mana", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the sense of».", "«mânâsında»."),
  W("الْمَصْدَرِ", "masdar-noun", "noun", ["idafa-definiteness", "an-masdariyya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a maṣdar».", "«masdar».", punct="،"),
  nahwu(),
  cited("أُرِيدُ", "arada", "verb", ["fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I want».", "«istiyorum»."),
  cited("أَنْ", "an-nasiba", "part", [NJ, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أُرِيدُ.", "«that».", "«-mani»."),
  NASB_V("تُحْسِنَ", "ahsana", "«you do good».", "«ihsan etmeni».", extra=" — صَحِيحٌ لَا ضَمِيرَ بَارِزًا فِيهِ"),
  cited("إِلَيَّ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ.", "«to me».", "«bana».", punct="،", segments=[seg("إِلَ", "ila", "prep"), seg("يَّ", "pron-1s", "pron")]),
  cited_wa("وَأَنْ", "an-nasiba", "part", ["mubtada-khabar", NJ, "an-masdariyya"], "أَنْ حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ: صِيَامُكُمْ.", "«and that».", "«ve -manız».", "أَنْ"),
  cited("تَصُومُوا", "saama", "verb", [NJ, "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«you fast» — naṣb by the dropped nūn.", "«oruç tutmanız» — nûnun hazfiyle mansûb."),
  cited("خَيْرٌ", "khayr", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ.", "«is better».", "«daha hayırlıdır»."),
  cited("لَكُمْ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ مَجْرُورٌ.", "«for you».", "«sizin için».", punct="،", segments=[seg("لَ", "li", "prep"), pr2mp()]),
  W("فَنَصْبُ", "nasb", "noun", ["mubtada-khabar", "idafa-definiteness", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَنَصْبُ مُبْتَدَأٌ، وَهُوَ مُضَافٌ.", "«and the naṣb of».", "«nasbı».", segments=[seg("فَ", "fa", "conj"), seg("نَصْبُ", "nasb", "noun")]),
  cited("تَصُومُوا", "saama", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«taṣūmū».", "«tesûmû'nun»."),
  bi_("بِحَذْفِ", "hadhf", "noun", ["mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"], "حَذْفِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«is by dropping».", "«hazfiyledir».", "حَذْفِ"),
  W("النُّونِ", "nun-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the nūn».", "«nûnun».", punct="."),
 ]})

# ----------- s4 (COMMENTARY): after certainty and opinion
S.append({"id": "s4", "translation": {
 "en": "And أَنْ after verbs of certainty, such as knowing, is the one lightened from the heavy, not the nāṣib — as عَلِمْتُ أَنْ سَيَقُومُ; and after verbs of opinion both are possible — as وَحَسِبُوا أَنْ لَا تَكُونَ فِتْنَةٌ." + C_EN,
 "tr": "Bilmek gibi yakîn fiillerinden sonraki أَنْ, nasb eden değil, sakîleden hafifletilmiş olandır — عَلِمْتُ أَنْ سَيَقُومُ gibi; zan fiillerinden sonra iki vecih de câizdir — وَحَسِبُوا أَنْ لَا تَكُونَ فِتْنَةٌ gibi." + C_TR},
 "tokens": [
  cited_wa("وَأَنْ", "an-nasiba", "part", ["mubtada-khabar"], "أَنْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and an».", "«ve en».", "أَنْ"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«sonra»."),
  W("أَفْعَالِ", "fil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«verbs of».", "«fiillerinden»."),
  W("الْيَقِينِ", "yaqin", "noun", ["idafa-definiteness", "zanna-wa-akhawatuha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«certainty».", "«yakîn»."),
  W("كَالْعِلْمِ", "ilm", "noun", ["huruf-jarr"], "الْكَافُ حَرْفُ جَرٍّ، وَالْعِلْمِ مَجْرُورٌ.", "«such as knowing».", "«bilmek gibi».", segments=[seg("كَ", "ka", "prep"), seg("الْعِلْمِ", "ilm", "noun")]),
  W("هِيَ", "hiya", "pron", ["mubtada-khabar"], "ضَمِيرُ فَصْلٍ، أَوْ مُبْتَدَأٌ ثَانٍ.", "«is».", "«-dır»."),
  W("الْمُخَفَّفَةُ", "mukhaffafa", "noun", ["mubtada-khabar", "inna-wa-akhawatuha", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "خَبَرٌ مَرْفُوعٌ.", "«the lightened one».", "«muhaffefe»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الثَّقِيلَةِ", "thaqila", "noun", ["huruf-jarr"], "مَجْرُورٌ — أَنَّ.", "«the heavy» — أَنَّ.", "«sakîle» — أَنَّ."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«değil»."),
  W("النَّاصِبَةُ", "nasib", "noun", ["atf-nasaq", NJ], "مَعْطُوفٌ مَرْفُوعٌ.", "«the nāṣib».", "«nasb eden».", punct="،"),
  nahwu(),
  cited("عَلِمْتُ", "alima", "verb", ["fail", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I knew».", "«bildim».", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
  cited("أَنْ", "an-masdariyya-lex", "part", ["inna-wa-akhawatuha", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ.", "«that» — the lightened أَنَّ.", "«-ğını» — muhaffefe."),
  cited("سَيَقُومُ", "qama", "verb", ["fail", "hollow-verbs"], "السِّينُ لِلِاسْتِقْبَالِ، وَيَقُومُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — لَا نَصْبَ.", "«he will stand» — no naṣb.", "«kalkacak» — nasb yok.", punct="؛", segments=[seg("سَ", "sin-letter", "part"), seg("يَقُومُ", "qama", "verb")]),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("أَفْعَالِ", "fil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«verbs of».", "«fiillerinden»."),
  W("الظَّنِّ", "zann", "noun", ["idafa-definiteness", "zanna-wa-akhawatuha"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«opinion».", "«zan»."),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«are possible».", "«câizdir»."),
  W("الْوَجْهَانِ", "wajh", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ.", "«both».", "«iki vecih».", punct="،"),
  nahwu(),
  cited_wa("وَحَسِبُوا", "hasiba", "verb", ["fail", "zanna-wa-akhawatuha"], "حَسِبُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«and they thought».", "«ve sandılar».", "حَسِبُوا"),
  cited("أَنْ", "an-nasiba", "part", [NJ, "inna-wa-akhawatuha"], "نَاصِبَةٌ، أَوِ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ.", "«that» — either reading.", "«-ki» — iki okunuş."),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-ma-»."),
  cited("تَكُونَ", "kana", "verb", [NJ, "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ عَلَى الْأَوَّلِ، وَرُوِيَ بِالرَّفْعِ عَلَى الثَّانِي.", "«there would be» — naṣb on the first reading.", "«olmayacak» — birinci okunuşta mansûb."),
  cited("فِتْنَةٌ", "fitna", "noun", ["kana-wa-akhawatuha"], "اسْمُ تَكُونَ مَرْفُوعٌ، أَوْ فَاعِلُ كَانَ التَّامَّةِ.", "«a trial».", "«bir fitne».", punct="."),
 ]})

# ----------- s5 (COMMENTARY): لَنْ
S.append({"id": "s5", "translation": {
 "en": "And لَنْ is for negation in the future with emphasis, not for ever — as لَنْ أَبْرَحَ, «I will certainly not depart», not «never for all time»." + C_EN,
 "tr": "لَنْ, te'kîdli olarak istikbâlde nefy içindir, ebedîlik için değil — لَنْ أَبْرَحَ gibi: «kat'iyyen ayrılmayacağım», «ebediyyen» değil." + C_TR},
 "tokens": [
  cited_wa("وَلَنْ", "lan", "part", ["mubtada-khabar", NJ], "لَنْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and lan».", "«ve len».", "لَنْ"),
  li_("لِلنَّفْيِ", "nafy", "noun", ["mubtada-khabar"], "النَّفْيِ مَجْرُورٌ — خَبَرٌ.", "«is for negation».", "«nefy içindir».", "النَّفْيِ", segs=[seg("لِ", "li", "prep"), seg("لنَّفْيِ", "nafy", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الِاسْتِقْبَالِ", "istiqbal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the future».", "«istikbâl»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("التَّأْكِيدِ", "takid", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«emphasis».", "«te'kîd»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«değil»."),
  li_("لِلتَّأْبِيدِ", "tabid", "noun", ["atf-nasaq"], "التَّأْبِيدِ مَجْرُورٌ — مَعْطُوفٌ.", "«for ever».", "«ebedîlik için».", "التَّأْبِيدِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لتَّأْبِيدِ", "tabid", "noun")]),
  nahwu(),
  cited("لَنْ", "lan", "part", [NJ], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "«not».", "«-mayacağım»."),
  NASB_V("أَبْرَحَ", "bariha", "«will I depart».", "«ayrılmayacağım».", punct="."),
 ]})

# ----------- s6 (COMMENTARY): إِذَنْ
S.append({"id": "s6", "translation": {
 "en": "And إِذَنْ puts in naṣb on two conditions: that what follows it not lean on what precedes it, and that the verb be future — as إِذَنْ تَدْخُلَ الْجَنَّةَ to one who says «I have become Muslim»; if a condition is missing the verb takes rafʿ, as أَنَا إِذَنْ أَظُنُّكَ كَاذِبًا; and after the wāw and the fāʾ both are permitted, as فَإِذَنْ أُكْرِمَكَ." + C_EN,
 "tr": "إِذَنْ iki şartla nasb eder: mâba'dinin mâkabline dayanmaması ve fiilin müstakbel olması — «müslüman oldum» diyene إِذَنْ تَدْخُلَ الْجَنَّةَ gibi; bir şart eksikse fiil merfû olur, أَنَا إِذَنْ أَظُنُّكَ كَاذِبًا gibi; vâv ve fâdan sonra iki vecih de câizdir, فَإِذَنْ أُكْرِمَكَ gibi." + C_TR},
 "tokens": [
  cited_wa("وَإِذَنْ", "idhan-jawab", "part", ["mubtada-khabar", NJ], "إِذَنْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and idhan».", "«ve izen».", "إِذَنْ"),
  W("تَنْصِبُ", "nasaba-nahw", "verb", ["fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«puts in naṣb».", "«nasb eder»."),
  bi_("بِشَرْطَيْنِ", "shart", "noun", ["al-muthanna"], "شَرْطَيْنِ مَجْرُورٌ بِالْيَاءِ.", "«on two conditions».", "«iki şartla».", "شَرْطَيْنِ", punct=":"),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", NJ], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ بَدَلٌ مِنْ شَرْطَيْنِ.", "«that».", "«-ması»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-ma-»."),
  W("يَعْتَمِدَ", "itamada", "verb", [NJ, "fail", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«lean».", "«dayanması»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«what».", "«... olan»."),
  W("بَعْدَهَا", "bada", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«follows it».", "«ondan sonra».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what».", "«... olan»."),
  W("قَبْلَهَا", "qabla", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«precedes it».", "«ondan önce».", punct="،", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  atf_wa("وَأَنْ", "an-masdariyya", "part", ["an-masdariyya", NJ], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«and that».", "«ve -ması».", "أَنْ"),
  W("يَكُونَ", "kana", "verb", [NJ, "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«be».", "«olması»."),
  W("الْفِعْلُ", "fil", "noun", ["kana-wa-akhawatuha"], "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the verb».", "«fiilin»."),
  W("مُسْتَقْبَلًا", "mustaqbal", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«future».", "«müstakbel».", punct="،"),
  nahwu(),
  cited("إِذَنْ", "idhan-jawab", "part", [NJ], "حَرْفُ جَوَابٍ وَجَزَاءٍ وَنَصْبٍ.", "«then».", "«o hâlde»."),
  NASB_V("تَدْخُلَ", "dakhala", "«you will enter».", "«girersin»."),
  JANNA(),
  li_("لِمَنْ", "man", "pron", ["ism-mawsul"], "مَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who».", "«diyene».", "مَنْ"),
  W("قَالَ", "qala", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«says».", "«diyen»."),
  ASLAMTU(),
  W("؛", "wa", "part", [], "عَلَامَةُ وَقْفٍ.", "", "", punct=None) if False else cited("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("فُقِدَ", "faqada", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ.", "«is missing».", "«eksikse»."),
  W("شَرْطٌ", "shart", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a condition».", "«bir şart»."),
  W("رُفِعَ", "rafaa", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it takes rafʿ».", "«merfû olur».", punct="،"),
  nahwu(),
  cited("أَنَا", "ana", "pron", ["mubtada-khabar"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«I».", "«ben»."),
  cited("إِذَنْ", "idhan-jawab", "part", [NJ], "حَرْفُ جَوَابٍ مُهْمَلٌ — مَا بَعْدَهُ خَبَرُ مَا قَبْلَهُ.", "«then» — not governing.", "«o hâlde» — amel etmez."),
  cited("أَظُنُّكَ", "zanna", "verb", ["fail", "mafulayn", "zanna-wa-akhawatuha", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — خَبَرُ أَنَا، وَالْكَافُ مَفْعُولٌ أَوَّلُ.", "«I think you» — rafʿ.", "«seni sanıyorum» — merfû.", segments=[seg("أَظُنُّ", "zanna", "verb"), pr2ms()]),
  cited("كَاذِبًا", "kadhib-liar", "noun", ["mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a liar».", "«yalancı».", punct="؛"),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("الْوَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the wāw».", "«vâv»."),
  atf_wa("وَالْفَاءِ", "fa", "conj", [], "الْفَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and the fāʾ».", "«ve fâ».", "الْفَاءِ"),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«are permitted».", "«câizdir»."),
  W("الْوَجْهَانِ", "wajh", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ.", "«both».", "«iki vecih».", punct="،"),
  nahwu(),
  cited("فَإِذَنْ", "idhan-jawab", "part", [NJ], "الْفَاءُ عَاطِفَةٌ، وَإِذَنْ حَرْفُ جَوَابٍ.", "«then».", "«o hâlde».", segments=[seg("فَ", "fa", "conj"), seg("إِذَنْ", "idhan-jawab", "part")]),
  cited("أُكْرِمَكَ", "akrama", "verb", [NJ, "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ أَوْ مَرْفُوعٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I honour you» — either case.", "«sana ikram ederim» — iki hâl de.", punct=".", segments=[seg("أُكْرِمَ", "akrama", "verb"), pr2ms()]),
 ]})

# ----------- s7 (COMMENTARY): كَيْ and حَتَّى
S.append({"id": "s7", "translation": {
 "en": "And كَيْ is for cause — as أَسْلَمْتُ كَيْ أَدْخُلَ الْجَنَّةَ; and حَتَّى puts in naṣb by a hidden أَنْ when it means كَيْ or إِلَى and the verb after it is future — as أَسْلَمْتُ حَتَّى أَدْخُلَ الْجَنَّةَ, and أَسِيرُ حَتَّى تَغِيبَ الشَّمْسُ." + C_EN,
 "tr": "كَيْ sebebiyet içindir — أَسْلَمْتُ كَيْ أَدْخُلَ الْجَنَّةَ gibi; حَتَّى, كَيْ veya إِلَى mânâsında olup ardındaki fiil müstakbel olduğunda gizli bir أَنْ ile nasb eder — أَسْلَمْتُ حَتَّى أَدْخُلَ الْجَنَّةَ ve أَسِيرُ حَتَّى تَغِيبَ الشَّمْسُ gibi." + C_TR},
 "tokens": [
  cited_wa("وَكَيْ", "kay", "part", ["mubtada-khabar", NJ], "كَيْ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and kay».", "«ve key».", "كَيْ"),
  li_("لِلسَّبَبِيَّةِ", "sababiyya", "noun", ["mubtada-khabar"], "السَّبَبِيَّةِ مَجْرُورٌ — خَبَرٌ.", "«is for cause».", "«sebebiyet içindir».", "السَّبَبِيَّةِ", segs=[seg("لِ", "li", "prep"), seg("لسَّبَبِيَّةِ", "sababiyya", "noun")]),
  nahwu(),
  ASLAMTU(),
  cited("كَيْ", "kay", "part", [NJ], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«so that».", "«-mek için»."),
  NASB_V("أَدْخُلَ", "dakhala", "«I enter».", "«gireyim»."),
  JANNA(punct="؛"),
  cited_wa("وَحَتَّى", "hatta", "part", ["mubtada-khabar", NJ], "حَتَّى لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and ḥattā».", "«ve hattâ».", "حَتَّى"),
  W("تَنْصِبُ", "nasaba-nahw", "verb", ["fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«puts in naṣb».", "«nasb eder»."),
  bi_("بِأَنْ", "an-nasiba", "part", [NJ, "hadhf-wa-taqdir"], "أَنْ فِي مَحَلِّ جَرٍّ.", "«by an».", "«en ile».", "أَنْ"),
  AN_HIDDEN(),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«it is».", "«olursa»."),
  bi_("بِمَعْنَى", "mana", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ كَانَتْ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("كَيْ", "kay", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«kay».", "«key»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  cited("إِلَى", "ila", "prep", ["atf-nasaq"], "مَعْطُوفٌ.", "«ilā».", "«ilâ»."),
  atf_wa("وَالْفِعْلُ", "fil", "noun", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"], "الْفِعْلُ مُبْتَدَأٌ — وَالْجُمْلَةُ حَالٌ.", "«and the verb».", "«ve fiil».", "الْفِعْلُ"),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ondan sonraki».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("مُسْتَقْبَلٌ", "mustaqbal", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is future».", "«müstakbeldir».", punct="،"),
  nahwu(),
  ASLAMTU(),
  cited("حَتَّى", "hatta", "part", [NJ], "حَرْفُ غَايَةٍ بِمَعْنَى كَيْ، وَالنَّاصِبُ أَنْ مُضْمَرَةٌ.", "«so that» — كَيْ.", "«-mek için» — key mânâsında."),
  NASB_V("أَدْخُلَ", "dakhala", "«I enter».", "«gireyim».", extra=" بِأَنْ مُضْمَرَةٍ"),
  JANNA(punct="،"),
  cited_wa("وَأَسِيرُ", "sara-go", "verb", ["fail", "hollow-verbs"], "أَسِيرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«and I walk».", "«ve yürürüm».", "أَسِيرُ"),
  cited("حَتَّى", "hatta", "part", [NJ], "حَرْفُ غَايَةٍ بِمَعْنَى إِلَى.", "«until» — إِلَى.", "«-e kadar» — ilâ mânâsında."),
  NASB_V("تَغِيبَ", "ghaba", "«sets».", "«batana».", extra=" بِأَنْ مُضْمَرَةٍ"),
  cited("الشَّمْسُ", "shams", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the sun».", "«güneş».", punct="."),
 ]})

# ----------- s8 (COMMENTARY): ḥattā of beginning
S.append({"id": "s8", "translation": {
 "en": "And if the present is meant, in truth or in narration, حَتَّى is a particle of beginning and the verb takes rafʿ — as مَرِضَ فُلَانٌ حَتَّى لَا يَرْجُونَهُ, and كُنْتُ سِرْتُ أَمْسِ حَتَّى أَدْخُلُ الْبَلَدَ." + C_EN,
 "tr": "Hakikaten veya hikâyeten hâl kastedilirse حَتَّى ibtidâ harfidir ve fiil merfû olur — مَرِضَ فُلَانٌ حَتَّى لَا يَرْجُونَهُ ve كُنْتُ سِرْتُ أَمْسِ حَتَّى أَدْخُلُ الْبَلَدَ gibi." + C_TR},
 "tokens": [
  W("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("أُرِيدَ", "arada", "verb", ["naib-al-fail", "al-majzum-wal-shart-wal-jaza", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ.", "«is meant».", "«kastedilirse»."),
  W("الْحَالُ", "hal-state", "noun", ["naib-al-fail", "hikayat-al-hal"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the present».", "«hâl»."),
  W("حَقِيقَةً", "haqiqa", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«in truth».", "«hakikaten»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("حِكَايَةً", "hikaya", "noun", ["atf-nasaq", "hikayat-al-hal"], "مَعْطُوفٌ مَنْصُوبٌ.", "«in narration».", "«hikâyeten»."),
  W("فَحَتَّى", "hatta", "part", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَحَتَّى لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«ḥattā is».", "«hattâ».", segments=[seg("فَ", "fa", "conj"), seg("حَتَّى", "hatta", "part")]),
  W("حَرْفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«a particle of».", "«harfidir»."),
  W("ابْتِدَاءٍ", "ibtida-start", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«beginning».", "«ibtidâ»."),
  atf_wa("وَالْفِعْلُ", "fil", "noun", ["mubtada-khabar"], "الْفِعْلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the verb».", "«ve fiil».", "الْفِعْلُ"),
  W("مَرْفُوعٌ", "marfu", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«takes rafʿ».", "«merfû olur».", punct="،"),
  nahwu(),
  cited("مَرِضَ", "marida", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«fell ill».", "«hastalandı»."),
  cited("فُلَانٌ", "fulan", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«so-and-so».", "«falan»."),
  cited("حَتَّى", "hatta", "part", [NJ, "hikayat-al-hal"], "حَرْفُ ابْتِدَاءٍ — الْحَالُ حَقِيقَةً.", "«so that (now)» — a true present.", "«öyle ki» — hakikî hâl."),
  cited("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mi-»."),
  cited("يَرْجُونَهُ", "raja", "verb", ["fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«they hope for him» — rafʿ by the nūn.", "«ondan ümit ediyorlar» — nûn ile merfû.", punct="،", segments=[seg("يَرْجُونَ", "raja", "verb"), pr3ms()]),
  cited_wa("وَكُنْتُ", "kana", "verb", ["kana-wa-akhawatuha"], "كُنْتُ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهَا.", "«and I had».", "«ve -mıştım».", "كُنْتُ", extra_segs=[seg("كُنْ", "kana", "verb"), prT()]),
  cited("سِرْتُ", "sara-go", "verb", ["kana-wa-akhawatuha", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كُنْتُ.", "«walked».", "«yürümüştüm».", segments=[seg("سِرْ", "sara-go", "verb"), prT()]),
  cited("أَمْسِ", "ams", "noun", ["maful-fih", "al-mabni-wal-mudmar"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ.", "«yesterday».", "«dün»."),
  cited("حَتَّى", "hatta", "part", [NJ, "hikayat-al-hal"], "حَرْفُ ابْتِدَاءٍ — الْحَالُ حِكَايَةً.", "«until» — a narrated present.", "«-inceye kadar» — hikâye edilen hâl."),
  cited("أَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«I enter» — rafʿ.", "«giriyorum» — merfû."),
  cited("الْبَلَدَ", "balad", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the town».", "«beldeye».", punct="."),
 ]})

# ----------- s9 (COMMENTARY): the fāʾ after the six
S.append({"id": "s9", "translation": {
 "en": "And the fāʾ puts in naṣb by a hidden أَنْ after a command, a prohibition, a question, a negation, a wish and an offer — as زُرْنِي فَأُكْرِمَكَ, لَا تَشْتُمْنِي فَأَضْرِبَكَ, هَلْ عِنْدَكُمْ مَاءٌ فَأَشْرَبَهُ, مَا تَأْتِينَا فَتُحَدِّثَنَا, لَيْتَ لِي مَالًا فَأُنْفِقَهُ, أَلَا تَنْزِلُ فَتُصِيبَ خَيْرًا." + C_EN,
 "tr": "Fâ, emir, nehiy, istifhâm, nefy, temennî ve arzdan sonra gizli bir أَنْ ile nasb eder — زُرْنِي فَأُكْرِمَكَ, لَا تَشْتُمْنِي فَأَضْرِبَكَ, هَلْ عِنْدَكُمْ مَاءٌ فَأَشْرَبَهُ, مَا تَأْتِينَا فَتُحَدِّثَنَا, لَيْتَ لِي مَالًا فَأُنْفِقَهُ, أَلَا تَنْزِلُ فَتُصِيبَ خَيْرًا gibi." + C_TR},
 "tokens": [
  atf_wa("وَالْفَاءُ", "fa", "conj", ["mubtada-khabar", NJ, JT], "الْفَاءُ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and the fāʾ».", "«ve fâ».", "الْفَاءُ"),
  W("تَنْصِبُ", "nasaba-nahw", "verb", ["fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«puts in naṣb».", "«nasb eder»."),
  bi_("بِأَنْ", "an-nasiba", "part", [NJ, "hadhf-wa-taqdir"], "أَنْ فِي مَحَلِّ جَرٍّ.", "«by an».", "«en ile».", "أَنْ"),
  AN_HIDDEN(),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... -den sonra»."),
  W("الْأَمْرِ", "amr-noun", "noun", ["idafa-definiteness", JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a command».", "«emir»."),
  atf_wa("وَالنَّهْيِ", "nahy", "noun", [JT], "النَّهْيِ مَعْطُوفٌ مَجْرُورٌ.", "«a prohibition».", "«nehiy».", "النَّهْيِ"),
  atf_wa("وَالِاسْتِفْهَامِ", "istifham", "noun", [JT], "الِاسْتِفْهَامِ مَعْطُوفٌ.", "«a question».", "«istifhâm».", "الِاسْتِفْهَامِ"),
  atf_wa("وَالنَّفْيِ", "nafy", "noun", [JT], "النَّفْيِ مَعْطُوفٌ.", "«a negation».", "«nefy».", "النَّفْيِ"),
  atf_wa("وَالتَّمَنِّي", "tamanni", "noun", [JT, "ism-maqsur-manqus"], "التَّمَنِّي مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«a wish».", "«temennî».", "التَّمَنِّي"),
  atf_wa("وَالْعَرْضِ", "ard-offer", "noun", [JT], "الْعَرْضِ مَعْطُوفٌ.", "«and an offer».", "«ve arz».", "الْعَرْضِ", punct="،"),
  nahwu(),
  cited("زُرْنِي", "zara", "verb", ["fail", "maful-bihi", "hollow-verbs", JT], "فِعْلُ أَمْرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«visit me».", "«beni ziyaret et».", segments=[seg("زُرْ", "zara", "verb"), pr1s()]),
  cited("فَأُكْرِمَكَ", "akrama", "verb", [NJ, JT, "fail", "maful-bihi", "form-iv-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَأُكْرِمَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«so that I honour you».", "«ki sana ikram edeyim».", punct="،", segments=[seg("فَ", "fa", "conj"), seg("أُكْرِمَ", "akrama", "verb"), pr2ms()]),
  cited("لَا", "la-nahiya", "part", ["la-nahiya", JT], "نَاهِيَةٌ جَازِمَةٌ.", "«do not».", "«-me»."),
  cited("تَشْتُمْنِي", "shatama", "verb", ["la-nahiya", "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«insult me».", "«bana sövme».", segments=[seg("تَشْتُمْ", "shatama", "verb"), pr1s()]),
  cited("فَأَضْرِبَكَ", "daraba", "verb", [NJ, JT, "fail", "maful-bihi"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَأَضْرِبَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«lest I strike you».", "«ki seni döveyim».", punct="،", segments=[seg("فَ", "fa", "conj"), seg("أَضْرِبَ", "daraba", "verb"), pr2ms()]),
  cited("هَلْ", "hal-istifham", "part", ["adawat-al-tasawwur", JT], "حَرْفُ اسْتِفْهَامٍ.", "«is there».", "«var mı»."),
  cited("عِنْدَكُمْ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَكُمْ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«with you».", "«sizde».", segments=[seg("عِنْدَ", "inda", "noun"), pr2mp()]),
  cited("مَاءٌ", "ma-water", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«water».", "«su»."),
  cited("فَأَشْرَبَهُ", "shariba", "verb", [NJ, JT, "fail", "maful-bihi"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَأَشْرَبَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«that I may drink it».", "«ki içeyim».", punct="،", segments=[seg("فَ", "fa", "conj"), seg("أَشْرَبَ", "shariba", "verb"), pr3ms()]),
  cited("مَا", "ma-nafiya", "part", ["ma-la-laysa-wa-la-al-jins", JT], "نَافِيَةٌ.", "«not».", "«-mi-»."),
  cited("تَأْتِينَا", "ata", "verb", ["fail", "maful-bihi", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَا مَفْعُولٌ بِهِ.", "«do you come to us».", "«bize gelmiyorsun».", segments=[seg("تَأْتِي", "ata", "verb"), seg("نَا", "pron-1p", "pron")]),
  cited("فَتُحَدِّثَنَا", "haddatha", "verb", [NJ, JT, "fail", "maful-bihi", "form-ii-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَتُحَدِّثَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَنَا مَفْعُولٌ بِهِ.", "«to talk with us».", "«ki bize anlatasın».", punct="،", segments=[seg("فَ", "fa", "conj"), seg("تُحَدِّثَ", "haddatha", "verb"), seg("نَا", "pron-1p", "pron")]),
  cited("لَيْتَ", "layta", "part", ["inna-wa-akhawatuha", JT], "حَرْفُ تَمَنٍّ وَنَصْبٍ.", "«would that».", "«keşke»."),
  cited("لِي", "li", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ — خَبَرُ لَيْتَ مُقَدَّمٌ.", "«I had».", "«benim».", segments=[seg("لِ", "li", "prep"), seg("ي", "pron-1s", "pron")]),
  cited("مَالًا", "mal", "noun", ["inna-wa-akhawatuha"], "اسْمُ لَيْتَ مُؤَخَّرٌ مَنْصُوبٌ.", "«wealth».", "«malım olsa»."),
  cited("فَأُنْفِقَهُ", "anfaqa", "verb", [NJ, JT, "fail", "maful-bihi", "form-iv-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَأُنْفِقَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«that I might spend it».", "«ki onu harcayayım».", punct="،", segments=[seg("فَ", "fa", "conj"), seg("أُنْفِقَ", "anfaqa", "verb"), pr3ms()]),
  cited("أَلَا", "ala-tanbih", "part", [JT], "حَرْفُ عَرْضٍ.", "«won't you».", "«-mez misin»."),
  cited("تَنْزِلُ", "nazala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«come down».", "«inmez misin»."),
  cited("فَتُصِيبَ", "asaba", "verb", [NJ, JT, "fail", "form-iv-verbs", "hollow-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَتُصِيبَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«and find».", "«ki erişesin».", segments=[seg("فَ", "fa", "conj"), seg("تُصِيبَ", "asaba", "verb")]),
  cited("خَيْرًا", "khayr", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«good».", "«hayra».", punct="."),
 ]})

# ----------- s10 (COMMENTARY): the wāw, أَوْ, the conjunction
S.append({"id": "s10", "translation": {
 "en": "And the wāw likewise after the six, for joining — as زُرْنِي وَأُكْرِمَكَ; and أَوْ in the sense of إِلَى أَنْ or إِلَّا أَنْ — as لَأَلْزَمَنَّكَ أَوْ تُعْطِيَنِي حَقِّي; and after a conjunction when what it joins to is a plain noun — as أَعْجَبَنِي ضَرْبُكَ زَيْدًا وَتَشْتُمَ." + C_EN,
 "tr": "Vâv da altısından sonra cem'iyyet için öyledir — زُرْنِي وَأُكْرِمَكَ gibi; أَوْ, إِلَى أَنْ veya إِلَّا أَنْ mânâsında — لَأَلْزَمَنَّكَ أَوْ تُعْطِيَنِي حَقِّي gibi; ve ma'tûfun aleyhi sarîh isim olan atıf harfinden sonra — أَعْجَبَنِي ضَرْبُكَ زَيْدًا وَتَشْتُمَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَالْوَاوُ", "waw-letter", "noun", ["mubtada-khabar", NJ, "anwa-al-waw"], "الْوَاوُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the wāw».", "«ve vâv».", "الْوَاوُ"),
  W("كَذَلِكَ", "kadhalika", "part", ["mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَذَلِكَ فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«likewise».", "«öyledir»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«sonra»."),
  W("السِّتَّةِ", "sitta", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the six».", "«altısından»."),
  li_("لِلْجَمْعِيَّةِ", "jamiyya", "noun", ["anwa-al-waw"], "الْجَمْعِيَّةِ مَجْرُورٌ — لِلتَّعْلِيلِ.", "«for joining».", "«cem'iyyet için».", "الْجَمْعِيَّةِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لْجَمْعِيَّةِ", "jamiyya", "noun")]),
  nahwu(),
  cited("زُرْنِي", "zara", "verb", ["fail", "maful-bihi", "hollow-verbs", JT], "فِعْلُ أَمْرٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«visit me».", "«beni ziyaret et».", segments=[seg("زُرْ", "zara", "verb"), pr1s()]),
  cited("وَأُكْرِمَكَ", "akrama", "verb", [NJ, JT, "fail", "maful-bihi", "anwa-al-waw"], "الْوَاوُ لِلْجَمْعِيَّةِ، وَأُكْرِمَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«and I will honour you».", "«ve sana ikram edeyim».", punct="؛", segments=[seg("وَ", "wa", "conj"), seg("أُكْرِمَ", "akrama", "verb"), pr2ms()]),
  cited_wa("وَأَوْ", "aw", "conj", ["mubtada-khabar", NJ], "أَوْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and aw».", "«ve ev».", "أَوْ"),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("إِلَى", "ila", "prep", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«ilā».", "«ilâ»."),
  cited("أَنْ", "an-nasiba", "part", [], "حَرْفٌ مَصْدَرِيٌّ.", "«an».", "«en»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  cited("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ مَحْكِيَّةٌ.", "«illā».", "«illâ»."),
  cited("أَنْ", "an-nasiba", "part", [], "حَرْفٌ مَصْدَرِيٌّ.", "«an».", "«en».", punct="،"),
  nahwu(),
  cited("لَأَلْزَمَنَّكَ", "lazima", "verb", ["fail", "maful-bihi", "nun-tawkid"], "اللَّامُ لِلْقَسَمِ، وَأَلْزَمَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I will surely cleave to you».", "«elbette yakanı bırakmam».", segments=[seg("لَ", "lam-jawab", "part"), seg("أَلْزَمَنَّ", "lazima", "verb"), pr2ms()]),
  cited("أَوْ", "aw", "conj", [NJ], "بِمَعْنَى إِلَى أَنْ، وَالنَّاصِبُ أَنْ مُضْمَرَةٌ.", "«until».", "«-inceye kadar»."),
  cited("تُعْطِيَنِي", "ata-give", "verb", [NJ, "fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ أَوَّلُ.", "«you give me».", "«bana verinceye».", segments=[seg("تُعْطِيَ", "ata-give", "verb"), pr1s()]),
  cited("حَقِّي", "haqq", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my right».", "«hakkımı».", punct="؛", segments=[seg("حَقِّ", "haqq", "noun"), seg("ي", "pron-1s", "pron")]),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَيُنْصَبُ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("حَرْفِ", "harf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«a particle of».", "«harfinden»."),
  W("الْعَطْفِ", "atf", "noun", ["idafa-definiteness", "atf-nasaq"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«conjunction».", "«atıf»."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«is».", "«olursa»."),
  W("الْمَعْطُوفُ", "matuf", "noun", ["kana-wa-akhawatuha", "atf-nasaq"], "اسْمُ كَانَ مَرْفُوعٌ.", "«what it joins».", "«ma'tûfun»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — تَمَامُ الْمُصْطَلَحِ.", "«to».", "«aleyh».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  W("اسْمًا", "ism", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a noun».", "«isim»."),
  W("صَرِيحًا", "sarih", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«plain».", "«sarîh».", punct="،"),
  nahwu(),
  cited("أَعْجَبَنِي", "ajaba-please", "verb", ["fail", "maful-bihi", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«pleased me».", "«hoşuma gitti».", segments=[seg("أَعْجَبَ", "ajaba-please", "verb"), pr1s()]),
  cited("ضَرْبُكَ", "darb", "noun", ["fail", "idafa-definiteness", "imal-al-masdar"], "فَاعِلٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — مَصْدَرٌ صَرِيحٌ.", "«your striking» — a plain maṣdar.", "«vurman» — sarîh masdar.", segments=[seg("ضَرْبُ", "darb", "noun"), pr2ms()]),
  cited("زَيْدًا", "zayd", "propn", ["maful-bihi", "imal-al-masdar"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ مَنْصُوبٌ.", "«Zayd».", "«Zeyd'i»."),
  cited("وَتَشْتُمَ", "shatama", "verb", [NJ, "fail", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَتَشْتُمَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ — وَالْمَصْدَرُ مَعْطُوفٌ عَلَى ضَرْبُكَ.", "«and that you insult» — joined to the maṣdar.", "«ve sövmen» — masdara ma'tûf.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("تَشْتُمَ", "shatama", "verb")]),
 ]})

# ----------- s11 (COMMENTARY): showing أَنْ
S.append({"id": "s11", "translation": {
 "en": "And showing أَنْ is permitted after the lām of كَيْ and after a conjunction — as أَسْلَمْتُ لِأَنْ أَدْخُلَ الْجَنَّةَ, and وَأَنْ تَشْتُمَ — and obligatory when لَا enters on the muḍāriʿ, as لِئَلَّا يَعْلَمَ." + C_EN,
 "tr": "Kéy lâmından ve atıf harfinden sonra أَنْ'in izhârı câizdir — أَسْلَمْتُ لِأَنْ أَدْخُلَ الْجَنَّةَ ve وَأَنْ تَشْتُمَ gibi — muzâriye لَا dâhil olduğunda vâcibdir, لِئَلَّا يَعْلَمَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted».", "«ve câizdir».", "يَجُوزُ"),
  W("إِظْهَارُ", "izhar", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«showing».", "«izhârı»."),
  cited("أَنْ", "an-nasiba", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«an».", "«en»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«sonra»."),
  W("لَامِ", "lam-letter", "noun", ["idafa-definiteness", NJ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the lām of».", "«lâmından»."),
  cited("كَيْ", "kay", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ.", "«kay».", "«key»."),
  atf_wa("وَحَرْفِ", "harf", "noun", ["idafa-definiteness"], "حَرْفِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and a particle of».", "«ve harfinden».", "حَرْفِ"),
  W("الْعَطْفِ", "atf", "noun", ["idafa-definiteness", "atf-nasaq"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«conjunction».", "«atıf».", punct="،"),
  nahwu(),
  ASLAMTU(),
  cited("لِأَنْ", "an-nasiba", "part", [NJ, "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ مُظْهَرٌ.", "«in order that» — أَنْ written out.", "«-mek için» — en izhâr edilmiş.", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنْ", "an-nasiba", "part")]),
  NASB_V("أَدْخُلَ", "dakhala", "«I enter».", "«gireyim»."),
  JANNA(punct="،"),
  cited_wa("وَأَنْ", "an-nasiba", "part", [NJ, "atf-nasaq"], "أَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ مُظْهَرٌ بَعْدَ الْعَاطِفِ.", "«and that».", "«ve -men».", "أَنْ"),
  NASB_V("تَشْتُمَ", "shatama", "«you insult».", "«sövmen».", punct="،"),
  atf_wa("وَيَجِبُ", "wajaba", "verb", ["fail", "mithal-verbs"], "يَجِبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: الْإِظْهَارُ.", "«and it is obligatory».", "«ve vâcibdir».", "يَجِبُ"),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("دَخَلَتْ", "dakhala", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«enters».", "«dâhil olduğunda»."),
  cited("لَا", "la-nafiya", "part", ["fail", "la-nafiya"], "فَاعِلٌ — الْحَرْفُ مَحْكِيٌّ.", "«lā».", "«lâ»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the muḍāriʿ».", "«muzâriye».", punct="،"),
  nahwu(),
  cited("لِئَلَّا", "an-nasiba", "part", [NJ, "lam-taleel", "la-nafiya"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنْ نَاصِبَةٌ مُظْهَرَةٌ، وَلَا نَافِيَةٌ — أَصْلُهُ لِأَنْ لَا، أُدْغِمَتِ النُّونُ فِي اللَّامِ.", "«lest» — لِ + أَنْ + لَا, the nūn merged.", "«-memesi için» — لِ + أَنْ + لَا, nûn idgâm edilmiş."),
  NASB_V("يَعْلَمَ", "alima", "«he know».", "«bilmesin».", punct="."),
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
 "juhud": need("juhud", "جُحُود", "ج ح د", "noun", "denial — the lām of denial after مَا كَانَ / لَمْ يَكُنْ (مَا كَانَ اللهُ لِيَظْلِمَهُمْ)", "cuhûd — مَا كَانَ / لَمْ يَكُنْ'den sonraki cuhûd lâmı", 5),
 "fitna": need("fitna", "فِتْنَة", "ف ت ن", "noun", "a trial, a temptation, strife", "fitne, imtihan, kargaşa", 2),
 "tabid": need("tabid", "تَأْبِيد", "أ ب د", "noun", "perpetuity — «for ever», which لَنْ does not assert", "ebedîlik — لَنْ'in iddia etmediği «sonsuza dek»", 5),
 "sababiyya": need("sababiyya", "سَبَبِيَّة", "س ب ب", "noun", "causality — what precedes is the cause of what follows (كَيْ, the fāʾ)", "sebebiyet — öncekinin sonrakine sebep olması (كَيْ, fâ)", 4),
 "tamanni": need("tamanni", "تَمَنٍّ", "م ن ي", "noun", "a wish (لَيْتَ) — one of the six that let the fāʾ govern", "temennî (لَيْتَ) — fâya amel ettiren altıdan biri", 4),
 "ard-offer": need("ard-offer", "عَرْض", "ع ر ض", "noun", "an offer, a gentle suggestion (أَلَا تَنْزِلُ) — one of the six", "arz, nazik teklif (أَلَا تَنْزِلُ) — altıdan biri", 4),
 "jamiyya": need("jamiyya", "جَمْعِيَّة", "ج م ع", "noun", "joining — the wāw of accompaniment's sense: both things together", "cem'iyyet — maiyyet vâvının mânâsı: iki şey birlikte", 5),
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
print("kafiya ch21 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "نَوَاصِبُ الْمُضَارِعِ فِي الْكَافِيَةِ", "en": "The nāṣibs of the muḍāriʿ in the Kafiya: the four that govern openly, the six places of the hidden أَنْ, and the notebook's conditions for each", "tr": "Kâfiye'de muzârinin nasb edicileri: açıkça amel eden dört, gizli أَنْ'in altı yeri ve defterin her biri için şartları"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المضارع يرفع إذا تجرد عن الناصب والجازم؛ وينصب بأن ولن وكي وإذن، وبأن مضمرة بعد حتى ولام كي ولام الجحود والفاء والواو وأو", "ضياء صونغور اوغلى — دفتر الكافية: أن المصدرية والمخففة بعد العلم والظن؛ لن للتأكيد لا للتأبيد؛ شرطا إذن؛ كي للسببية؛ حتى بمعنى كي وإلى وحرف الابتداء؛ الفاء والواو بعد الستة؛ أو بمعنى إلى أن؛ إظهار أن وإضمارها"],
 "question": {
  "en": ["When is a muḍāriʿ in RAFʿ? When nothing governs it — no nāṣib, no jāzim: يَقُومُ زَيْدٌ. Rafʿ is the absence of a governor, which is why the Iẓhār calls its governor «maʿnawī».",
         "Which particles put it in NAṢB openly? Four: أَنْ, لَنْ, كَيْ, إِذَنْ. And a hidden أَنْ does the work in six more places: after حَتَّى, the lām of كَيْ, the lām of denial, the fāʾ, the wāw and أَوْ.",
         "What does أَنْ do? It makes the clause a maṣdar — أُرِيدُ أَنْ تُحْسِنَ إِلَيَّ is «I want your doing-good», أَنْ تَصُومُوا خَيْرٌ لَكُمْ «your fasting is better». After a verb of certainty (عَلِمْتُ) the أَنْ is the lightened أَنَّ and governs nothing (عَلِمْتُ أَنْ سَيَقُومُ); after a verb of opinion both readings stand (وَحَسِبُوا أَنْ لَا تَكُونَ فِتْنَةٌ).",
         "What of لَنْ and إِذَنْ? لَنْ denies the future emphatically, not eternally (لَنْ أَبْرَحَ). إِذَنْ governs only when its clause does not lean on what came before AND the verb is future (إِذَنْ تَدْخُلَ الْجَنَّةَ); lose either and the verb is raised (أَنَا إِذَنْ أَظُنُّكَ كَاذِبًا); after وَ or فَ both are allowed.",
         "When does حَتَّى govern? When it means كَيْ or إِلَى and the verb after it is future from the standpoint of what precedes (أَسْلَمْتُ حَتَّى أَدْخُلَ الْجَنَّةَ، أَسِيرُ حَتَّى تَغِيبَ الشَّمْسُ). If a present is meant, actual or narrated, it is a particle of beginning and the verb stays in rafʿ (مَرِضَ فُلَانٌ حَتَّى لَا يَرْجُونَهُ).",
         "When do the fāʾ and the wāw govern? Only after the SIX — command, prohibition, question, negation, wish, offer — the fāʾ for cause (زُرْنِي فَأُكْرِمَكَ: your visit causes my honouring) and the wāw for joining (زُرْنِي وَأُكْرِمَكَ: both together). أَوْ governs when it means «until» or «unless» (لَأَلْزَمَنَّكَ أَوْ تُعْطِيَنِي حَقِّي), and any conjunction does when it joins a verb to a plain noun (ضَرْبُكَ زَيْدًا وَتَشْتُمَ).",
         "May the hidden أَنْ be written? After the lām of كَيْ and after a conjunction, yes (لِأَنْ أَدْخُلَ، وَأَنْ تَشْتُمَ); when لَا follows the lām it must be, and the three fuse into لِئَلَّا. The engine's analyzer pushes a verb expectation after each of these and refuses to read a مَا after لِئَلَّا as anything but the merged negation."],
  "tr": ["Muzâri ne zaman REF'tedir? Onu yöneten yokken — nasb edici de cezm edici de yok: يَقُومُ زَيْدٌ. Ref' âmilin yokluğudur; İzhâr'ın âmiline «ma'nevî» demesinin sebebi budur.",
         "Hangi edatlar onu açıkça NASB eder? Dört: أَنْ, لَنْ, كَيْ, إِذَنْ. Altı yerde daha işi gizli bir أَنْ görür: حَتَّى, kéy lâmı, cuhûd lâmı, fâ, vâv ve أَوْ'den sonra.",
         "أَنْ ne yapar? Cümleyi masdar kılar — أُرِيدُ أَنْ تُحْسِنَ إِلَيَّ «ihsan etmeni istiyorum», أَنْ تَصُومُوا خَيْرٌ لَكُمْ «oruç tutmanız daha hayırlıdır». Yakîn fiilinden sonra (عَلِمْتُ) أَنْ, hafifletilmiş أَنَّ'dir ve amel etmez (عَلِمْتُ أَنْ سَيَقُومُ); zan fiilinden sonra iki okunuş da durur (وَحَسِبُوا أَنْ لَا تَكُونَ فِتْنَةٌ).",
         "Ya لَنْ ve إِذَنْ? لَنْ istikbâli te'kîdle nefy eder, ebediyyen değil (لَنْ أَبْرَحَ). إِذَنْ yalnız cümlesi öncekine dayanmadığında VE fiil müstakbel olduğunda amel eder (إِذَنْ تَدْخُلَ الْجَنَّةَ); biri eksilince fiil ref'edilir (أَنَا إِذَنْ أَظُنُّكَ كَاذِبًا); وَ ya da فَ'dan sonra ikisi de câizdir.",
         "حَتَّى ne zaman amel eder? كَيْ veya إِلَى mânâsında olup ardındaki fiil öncekine göre müstakbel olduğunda (أَسْلَمْتُ حَتَّى أَدْخُلَ الْجَنَّةَ، أَسِيرُ حَتَّى تَغِيبَ الشَّمْسُ). Hakikî ya da hikâye edilen hâl kastedilirse ibtidâ harfidir ve fiil ref'te kalır (مَرِضَ فُلَانٌ حَتَّى لَا يَرْجُونَهُ).",
         "Fâ ve vâv ne zaman amel eder? Yalnız ALTI'dan sonra — emir, nehiy, istifhâm, nefy, temennî, arz — fâ sebep için (زُرْنِي فَأُكْرِمَكَ: ziyaretin ikramıma sebep), vâv cem'iyyet için (زُرْنِي وَأُكْرِمَكَ: ikisi birlikte). أَوْ «-inceye kadar» ya da «-medikçe» mânâsında amel eder (لَأَلْزَمَنَّكَ أَوْ تُعْطِيَنِي حَقِّي); her atıf harfi de fiili sarîh bir isme bağladığında (ضَرْبُكَ زَيْدًا وَتَشْتُمَ).",
         "Gizli أَنْ yazılabilir mi? Kéy lâmından ve atıf harfinden sonra evet (لِأَنْ أَدْخُلَ، وَأَنْ تَشْتُمَ); lâmı لَا izlediğinde yazılması gerekir ve üçü لِئَلَّا olarak kaynaşır. Motorun analizörü bunların her birinden sonra bir fiil beklentisi iter ve لِئَلَّا'dan sonraki bir مَا'yı birleşik nefyden başka bir şey okumayı reddeder."]},
 "plain": {
  "en": "A present-future verb ends in -u unless something governs it. Four words (أَنْ، لَنْ، كَيْ، إِذَنْ) switch it to -a openly; six more do it through an unspoken أَنْ: حَتَّى, the lām of purpose, the lām of denial, the fāʾ and wāw after a command, prohibition, question, negation, wish or offer, and أَوْ meaning «until».",
  "tr": "Şimdiki-gelecek zaman fiili bir şey onu yönetmedikçe -u ile biter. Dört kelime (أَنْ، لَنْ، كَيْ، إِذَنْ) onu açıkça -a'ya çevirir; altı yapı daha bunu gizli bir أَنْ ile yapar: حَتَّى, ta'lil lâmı, cuhûd lâmı, emir, nehiy, soru, nefy, dilek ya da teklif sonrası fâ ve vâv, ve «-inceye kadar» anlamındaki أَوْ."},
 "explanation": {
  "en": "The matn gives the list in two lines — four open nāṣibs and six seats for a hidden أَنْ — and the notebook spends five pages on what each requires, which is the material the chapter keeps as commentary. The organising fact is that أَنْ is the only real nāṣib of meaning: it turns a clause into a maṣdar, and every hidden-أَنْ case is a place where the language wants that maṣdar reading without pronouncing the particle. That is why حَتَّى governs only when it means «in order to» or «until» and the verb is still ahead — a present state, actual or narrated, makes it a mere particle of beginning — and why the fāʾ and the wāw govern only after the six kinds of non-assertion, where «visit me, that I may honour you» names a consequence rather than stating a fact. The notebook's distinctions are the ones a learner will be asked: the أَنْ after عَلِمْتُ is the lightened أَنَّ and governs nothing, while after حَسِبَ either reading stands; لَنْ is emphatic, not eternal; إِذَنْ needs independence and futurity and loses its force after a conjunction; the fāʾ means cause and the wāw means togetherness. The chapter closes with the surface forms: أَنْ may be shown after the lām of purpose and after a conjunction, and must be shown when لَا follows, where the three letters fuse into لِئَلَّا — a spelling the analyzer has to recognise as a unit. Two readings diverge from the notebook and are recorded: فَأَشْرَبَهُ for its فَأَشْرَبَهَا, and the Form I لَأَلْزَمَنَّكَ for its Form IV.",
  "tr": "Metin listeyi iki satırda verir — dört açık nasb edici ve gizli أَنْ için altı yer — defter ise her birinin ne gerektirdiğine beş sayfa harcar; bâbın şerh olarak tuttuğu malzeme budur. Düzenleyici olgu, أَنْ'in mânâca tek gerçek nasb edici olmasıdır: cümleyi masdara çevirir ve her gizli-أَنْ hâli, dilin edatı söylemeden o masdar okunuşunu istediği bir yerdir. حَتَّى'nın yalnız «-mek için» ya da «-inceye kadar» anlamına gelip fiil hâlâ ileride olduğunda amel etmesinin — hakikî ya da hikâye edilen bir hâl onu salt ibtidâ harfi yapar — ve fâ ile vâvın yalnız altı tür iddiasızlıktan sonra amel etmesinin sebebi budur; «beni ziyaret et ki sana ikram edeyim» bir olguyu değil bir sonucu adlandırır. Defterin ayrımları öğrenciye sorulacak olanlardır: عَلِمْتُ'den sonraki أَنْ hafifletilmiş أَنَّ'dir ve amel etmez, حَسِبَ'den sonra ise iki okunuş da durur; لَنْ te'kîdlidir, ebedî değil; إِذَنْ bağımsızlık ve istikbâl ister, atıf harfinden sonra gücünü yitirir; fâ sebep, vâv birliktelik demektir. Bâb yüzey biçimleriyle kapanır: أَنْ ta'lil lâmından ve atıf harfinden sonra gösterilebilir, لَا izlediğinde gösterilmelidir; orada üç harf لِئَلَّا olarak kaynaşır — analizörün bir birim olarak tanıması gereken bir yazım. Defterden iki okuyuş ayrılır ve kaydedilir: فَأَشْرَبَهَا yerine فَأَشْرَبَهُ, IV. bâb yerine I. bâb لَأَلْزَمَنَّكَ."},
 "examples": [
  {"ar": "يُنْصَبُ بِأَنْ وَلَنْ وَكَيْ وَإِذَنْ، وَبِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى وَلَامِ كَيْ وَلَامِ الْجُحُودِ وَالْفَاءِ وَالْوَاوِ وَأَوْ", "en": "The matn's list.", "tr": "Metnin listesi.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "أُرِيدُ أَنْ تُحْسِنَ إِلَيَّ — أَنْ تَصُومُوا خَيْرٌ لَكُمْ", "en": "أَنْ as a maṣdar-maker.", "tr": "Masdar kılan أَنْ.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "عَلِمْتُ أَنْ سَيَقُومُ — وَحَسِبُوا أَنْ لَا تَكُونَ فِتْنَةٌ", "en": "After certainty, after opinion.", "tr": "Yakînden, zandan sonra.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "إِذَنْ تَدْخُلَ الْجَنَّةَ — أَنَا إِذَنْ أَظُنُّكَ كَاذِبًا", "en": "إِذَنْ governing and not.", "tr": "Amel eden ve etmeyen إِذَنْ.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "أَسِيرُ حَتَّى تَغِيبَ الشَّمْسُ — مَرِضَ فُلَانٌ حَتَّى لَا يَرْجُونَهُ", "en": "حَتَّى of end, حَتَّى of beginning.", "tr": "Gâye hattâsı, ibtidâ hattâsı.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "زُرْنِي فَأُكْرِمَكَ … أَلَا تَنْزِلُ فَتُصِيبَ خَيْرًا", "en": "The fāʾ after the six.", "tr": "Altıdan sonra fâ.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "لِئَلَّا يَعْلَمَ", "en": "The obligatory written أَنْ.", "tr": "Vâcib izhâr edilen أَنْ.", "sourceStory": "al-kafiya", "sentence": "s11"}],
 "commonMistakes": [
  {"wrong": "«عَلِمْتُ أَنْ يَقُومَ»",
   "right": "«عَلِمْتُ أَنْ سَيَقُومُ — yakîn fiilinden sonra أَنْ hafifletilmiş أَنَّ'dir, nasb etmez»",
   "why": {"en": "Certainty cannot take the hoping أَنْ; the lightened أَنَّ follows and the verb stays raised, often with a sīn or قَدْ between.", "tr": "Yakîn ümit bildiren أَنْ'i alamaz; hafifletilmiş أَنَّ gelir ve fiil merfû kalır, çoğu kez araya sîn ya da قَدْ girer."}},
  {"wrong": "«لَنْ أَبْرَحَ — ebediyyen ayrılmayacağım»",
   "right": "«kat'iyyen ayrılmayacağım — لَنْ te'kîd içindir, ebedîlik için değil»",
   "why": {"en": "The notebook rejects the eternity reading explicitly.", "tr": "Defter ebedîlik okunuşunu açıkça reddeder."}},
  {"wrong": "«أَنَا إِذَنْ أَظُنَّكَ كَاذِبًا»",
   "right": "«أَنَا إِذَنْ أَظُنُّكَ كَاذِبًا — fiil öncekinin haberidir ve hâl içindir; إِذَنْ amel etmez»",
   "why": {"en": "Both of إِذَنْ's conditions fail: the verb leans on أَنَا and is present.", "tr": "إِذَنْ'in iki şartı da düşer: fiil أَنَا'ya dayanır ve hâl içindir."}},
  {"wrong": "«يَزُورُنِي فَأُكْرِمَهُ — fâ nasb eder»",
   "right": "«fâ yalnız emir, nehiy, istifhâm, nefy, temennî ve arzdan sonra nasb eder; haberden sonra fiil merfû kalır»",
   "why": {"en": "After a plain statement the fāʾ is an ordinary conjunction.", "tr": "Düz bir haberden sonra fâ sıradan bir atıf harfidir."}}],
 "relatedNotes": [NJ, "an-masdariyya", JT, "anwa-al-waw", "hikayat-al-hal", "zanna-wa-akhawatuha", "al-fil-wal-madi-wal-mudari-fil-kafiya"]}

ADD_EN = (" Chapter 21 (notebook lines ~296-301): the rafʿ of the bare muḍāriʿ and the list of nāṣibs restored from the received matn and marked (s1-s2); the notebook's account of أَنْ (and the lightened أَنْ after certainty and opinion), لَنْ, إِذَنْ, كَيْ, حَتَّى in both roles, "
          "the fāʾ and the wāw after the six, أَوْ, the conjunction on a plain noun and the showing of أَنْ as commentary (s3-s11). DIVERGENCES: the notebook's فَأَشْرَبَهَا is read فَأَشْرَبَهُ (مَاء is masculine); its لَأُلْزِمَنَّكَ is cited in Form I as لَأَلْزَمَنَّكَ.")
ADD_TR = (" Yirmi birinci bâb (defter satırları ~296-301): çıplak muzârinin ref'i ve nasb edicilerin listesi alınan metinden geri yazılmış ve işaretlenmiştir (s1-s2); defterin أَنْ (yakîn ve zandan sonraki hafifletilmiş أَنْ dahil), لَنْ, إِذَنْ, كَيْ, iki rolüyle حَتَّى, "
          "altıdan sonra fâ ve vâv, أَوْ, sarîh isim üzerine atıf ve أَنْ'in izhârı hakkındaki açıklaması şerh olarak (s3-s11). FARKLAR: defterin فَأَشْرَبَهَا'sı فَأَشْرَبَهُ okunmuştur (مَاء müzekkerdir); لَأُلْزِمَنَّكَ'si I. bâbdan لَأَلْزَمَنَّكَ olarak zikredilmiştir.")
write_out(21, S, TITLE, ADD_EN, ADD_TR, "296-301", GLOSS_ADD, notes=(NOTE,),
          related=((NJ, [K]), (JT, [K]), ("an-masdariyya", [K])))
report(21, S, GLOSS_ADD, (NOTE,))
