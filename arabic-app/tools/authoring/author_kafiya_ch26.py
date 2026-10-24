# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 26: THE VERBS OF APPROACH (afʿāl al-muqāraba). The definition in the notebook's own Arabic; the three kinds by
what brings the khabar near — hope (عَسَى), occurrence (كَادَ), setting-about (طَفِقَ، كَرَبَ، جَعَلَ، أَخَذَ); عَسَى non-conjugating and
used two ways (defective with an ism and an أَنْ-clause khabar; complete with the clause as its doer), أَنْ sometimes dropped; كَادَ with a
bare muḍāriʿ khabar, sometimes with أَنْ; the dispute on negated كَادَ with the aya of the cow and Dhū l-Rumma's verse and Ibn Shubruma's
correction; the setting-about verbs with the aya of the leaves; أَوْشَكَ used both ways.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~316-319 of the transcription.

  VERBATIM: s1. COMMENTARY (the notebook): s2-s10 — marked C_EN/C_TR. Qurʾānic text (2:71, 7:22) as the source prints it.
  DIVERGENCE recorded in the manifest: the notebook writes يَجِيئُ; the chapter cites the received يَجِيءُ.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch26.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "afal-al-muqaraba-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "أَفْعَالُ الْمُقَارَبَةِ", "en": "The verbs of approach — ʿasā, kāda, ṭafiqa and awshaka", "tr": "Mukârebe fiilleri — asâ, kâde, tafika ve evşeke"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
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
KM = "kada-wa-akhawatuha" if (pathlib.Path(os.environ.get("DRY_GR", "")) / "kada-wa-akhawatuha.json").exists() else "afal-al-muqaraba"
def ZAYD(ar, en="«Zayd».", tr="«Zeyd»."): return cited("زَيْدٌ", "zayd", "propn", [KM], ar, en, tr)
def AN(): return cited("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to».", "«-ması».")
def KH_V(full, lex, ar, en, tr, punct=None, tags=()): return cited(full, lex, "verb", [KM, "nawasib-wa-jawazim-al-mudari"] + list(tags), ar, en, tr, punct=punct)

S.append({"id": "s1", "translation": {
 "en": "The verbs of approach: what was set down for the nearness of the khabar — by hope, by occurrence, or by setting about it.",
 "tr": "Mukârebe fiilleri: haberin yakınlığı için — recâ, husûl ya da ona başlama yoluyla — konulan fiillerdir."},
 "tokens": [
  W("أَفْعَالُ", "fil", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir", KM], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the verbs of».", "«fiilleri»."),
  W("الْمُقَارَبَةِ", "muqaraba", "noun", ["idafa-definiteness", KM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«approach».", "«mukârebe».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«was set down».", "«konulan»."),
  li_("لِدُنُوِّ", "dunuww", "noun", ["idafa-definiteness"], "دُنُوِّ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«for the nearness of».", "«yakınlığı için».", "دُنُوِّ"),
  W("الْخَبَرِ", "khabar", "noun", ["idafa-definiteness", KM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the khabar».", "«haberin»."),
  W("رَجَاءً", "raja-hope", "noun", ["maful-lah", "hal"], "مَفْعُولٌ لَهُ مَنْصُوبٌ، أَوْ حَالٌ.", "«by hope».", "«recâ yoluyla»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("حُصُولًا", "husul", "noun", ["atf-nasaq", "maful-lah"], "مَعْطُوفٌ مَنْصُوبٌ.", "«by occurrence».", "«husûl yoluyla»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("أَخْذًا", "akhdh", "noun", ["atf-nasaq", "maful-lah"], "مَعْطُوفٌ مَنْصُوبٌ.", "«by setting about».", "«başlama yoluyla»."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — يَعُودُ إِلَى الْخَبَرِ.", "«it».", "«ona».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "So the first is عَسَى, and it does not conjugate: it has no muḍāriʿ, no imperative, no prohibition and no passive." + C_EN,
 "tr": "Birincisi عَسَى'dır ve tasarruf etmez: muzârii, emri, nehyi ve meçhulü yoktur." + C_TR},
 "tokens": [
  W("فَالْأَوَّلُ", "awwal", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«so the first».", "«birincisi».", segments=[seg("فَ", "fa", "conj"), seg("الْأَوَّلُ", "awwal", "noun")]),
  cited("عَسَى", "asa-hope", "verb", ["mubtada-khabar", KM, "al-mabni-wal-mudmar"], "خَبَرٌ — فِعْلٌ مَحْكِيٌّ.", "«ʿasā».", "«asâ».", punct="،"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  W("غَيْرُ", "ghayr", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«not».", "«... etmez»."),
  W("مُتَصَرِّفَةٍ", "mutasarrif", "noun", ["idafa-definiteness", "ism-fail", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ تَصَرَّفَ.", "«conjugating».", "«tasarruf».", punct=":"),
  W("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"], "نَافِيَةٌ لِلْجِنْسِ.", "«no».", "«yoktur»."),
  W("مُضَارِعَ", "mudari", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«muḍāriʿ».", "«muzârii»."),
  W("لَهَا", "li", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَا.", "«it has».", "«onun».", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  atf_wa("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"], "لَا نَافِيَةٌ لِلْجِنْسِ.", "«and no».", "«ve ... yok».", "لَا"),
  W("أَمْرَ", "amr", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«imperative».", "«emri»."),
  atf_wa("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"], "لَا نَافِيَةٌ لِلْجِنْسِ.", "«and no».", "«ve ... yok».", "لَا"),
  W("نَهْيَ", "nahy", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«prohibition».", "«nehyi»."),
  atf_wa("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"], "لَا نَافِيَةٌ لِلْجِنْسِ.", "«and no».", "«ve ... yok».", "لَا"),
  W("مَجْهُولَ", "majhul", "noun", ["la-nafiya-lil-jins", "ism-maful"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«passive».", "«meçhulü».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And it is used in two ways: defective — as عَسَى زَيْدٌ أَنْ يَخْرُجَ, where زَيْدٌ is its ism and أَنْ يَخْرُجَ its khabar in the place of naṣb." + C_EN,
 "tr": "İki şekilde kullanılır: nâkıs olarak — عَسَى زَيْدٌ أَنْ يَخْرُجَ gibi; orada زَيْدٌ ismi, أَنْ يَخْرُجَ mahallen mansûb haberidir." + C_TR},
 "tokens": [
  atf_wa("وَتُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "تُسْتَعْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ.", "«and it is used».", "«ve kullanılır».", "تُسْتَعْمَلُ"),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«üzere»."),
  W("وَجْهَيْنِ", "wajh", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ.", "«two ways».", "«iki şekil».", punct=":"),
  W("نَاقِصَةً", "naqis", "noun", ["hal", KM], "حَالٌ مَنْصُوبٌ.", "«defective».", "«nâkıs olarak».", punct="،"),
  nahwu(),
  cited("عَسَى", "asa-hope", "verb", [KM], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«it is hoped».", "«umulur ki»."),
  ZAYD("اسْمُ عَسَى مَرْفُوعٌ."),
  AN(),
  KH_V("يَخْرُجَ", "kharaja", "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ عَسَى.", "«will go out».", "«çıkar».", punct="،"),
  W("فَزَيْدٌ", "zayd", "propn", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَزَيْدٌ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so Zayd».", "«o hâlde Zeyd».", segments=[seg("فَ", "fa", "conj"), seg("زَيْدٌ", "zayd", "propn")]),
  W("اسْمُهَا", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", KM], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its ism».", "«ismidir».", segments=[seg("اسْمُ", "ism", "noun"), pr3fs()]),
  cited_wa("وَأَنْ", "an-masdariyya", "part", ["mubtada-khabar", "an-masdariyya"], "أَنْ — الْمَحْكِيُّ مُبْتَدَأٌ.", "«and an».", "«ve en».", "أَنْ"),
  cited("يَخْرُجَ", "kharaja", "verb", ["mubtada-khabar"], "تَمَامُ الْمَحْكِيِّ.", "«yakhruja».", "«yahruce»."),
  W("خَبَرُهَا", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness", KM], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its khabar».", "«haberidir».", segments=[seg("خَبَرُ", "khabar", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallinde»."),
  W("نَصْبٍ", "nasb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naṣb».", "«nasb».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And complete — as عَسَى أَنْ يَخْرُجَ زَيْدٌ, where زَيْدٌ is the doer of يَخْرُجُ and أَنْ يَخْرُجَ زَيْدٌ is the doer of عَسَى; and أَنْ is sometimes dropped — as عَسَى زَيْدٌ يَخْرُجُ." + C_EN,
 "tr": "Ve tam olarak — عَسَى أَنْ يَخْرُجَ زَيْدٌ gibi; orada زَيْدٌ, يَخْرُجُ'nun fâili, أَنْ يَخْرُجَ زَيْدٌ ise عَسَى'nın fâilidir; أَنْ bazen hazfedilir — عَسَى زَيْدٌ يَخْرُجُ gibi." + C_TR},
 "tokens": [
  atf_wa("وَتَامَّةً", "tamm", "noun", ["hal", KM], "تَامَّةً مَعْطُوفٌ عَلَى نَاقِصَةً مَنْصُوبٌ.", "«and complete».", "«ve tam olarak».", "تَامَّةً", punct="،"),
  nahwu(),
  cited("عَسَى", "asa-hope", "verb", [KM, "fail"], "فِعْلٌ مَاضٍ جَامِدٌ تَامٌّ.", "«it is hoped».", "«umulur ki»."),
  AN(),
  KH_V("يَخْرُجَ", "kharaja", "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ عَسَى.", "«goes out».", "«çıkması»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلُ يَخْرُجَ مَرْفُوعٌ.", "«Zayd».", "«Zeyd'in».", punct="،"),
  W("فَزَيْدٌ", "zayd", "propn", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَزَيْدٌ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so Zayd».", "«o hâlde Zeyd».", segments=[seg("فَ", "fa", "conj"), seg("زَيْدٌ", "zayd", "propn")]),
  W("فَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "idafa-definiteness", "fail"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the doer of».", "«fâilidir»."),
  cited("يَخْرُجُ", "kharaja", "verb", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«yakhruju».", "«yahrucu».", punct="،"),
  cited_wa("وَأَنْ", "an-masdariyya", "part", ["mubtada-khabar", "an-masdariyya"], "أَنْ — الْمَحْكِيُّ مُبْتَدَأٌ.", "«and an».", "«ve en».", "أَنْ"),
  cited("يَخْرُجَ", "kharaja", "verb", ["mubtada-khabar"], "مِنْ تَمَامِ الْمَحْكِيِّ.", "«yakhruja».", "«yahruce»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "تَمَامُ الْمَحْكِيِّ.", "«Zayd».", "«Zeyd»."),
  W("فَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "idafa-definiteness", "fail"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the doer of».", "«fâilidir»."),
  cited("عَسَى", "asa-hope", "verb", ["idafa-definiteness", KM], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«ʿasā».", "«asâ'nın».", punct="؛"),
  atf_wa("وَقَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("تُحْذَفُ", "hadhafa", "verb", ["naib-al-fail", "hadhf-wa-taqdir"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is dropped».", "«hazfedilir»."),
  cited("أَنْ", "an-masdariyya", "part", ["naib-al-fail", "an-masdariyya"], "نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", "«an».", "«en».", punct="،"),
  nahwu(),
  cited("عَسَى", "asa-hope", "verb", [KM], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«it is hoped».", "«umulur ki»."),
  ZAYD("اسْمُ عَسَى مَرْفُوعٌ."),
  cited("يَخْرُجُ", "kharaja", "verb", [KM, "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ عَسَى بِلَا أَنْ.", "«goes out» — the khabar without an.", "«çıkar» — en'siz haber.", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And the second is كَادَ — as كَادَ زَيْدٌ يَجِيءُ, where زَيْدٌ is its ism and the clause يَجِيءُ its khabar in the place of naṣb; and أَنْ sometimes enters on its khabar — as كَادَ زَيْدٌ أَنْ يَجِيءَ." + C_EN,
 "tr": "İkincisi كَادَ'dir — كَادَ زَيْدٌ يَجِيءُ gibi; orada زَيْدٌ ismi, يَجِيءُ cümlesi mahallen mansûb haberidir; bazen haberine أَنْ girer — كَادَ زَيْدٌ أَنْ يَجِيءَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَالثَّانِي", "thani", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second».", "«ikincisi».", "الثَّانِي"),
  cited("كَادَ", "kada", "verb", ["mubtada-khabar", KM, "hollow-verbs"], "خَبَرٌ — فِعْلٌ مَحْكِيٌّ.", "«kāda».", "«kâde».", punct="،"),
  nahwu(),
  cited("كَادَ", "kada", "verb", [KM, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«was about to».", "«az kalsın»."),
  ZAYD("اسْمُ كَادَ مَرْفُوعٌ."),
  cited("يَجِيءُ", "jaa", "verb", [KM, "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كَادَ.", "«come».", "«geliyordu».", punct="،"),
  W("فَزَيْدٌ", "zayd", "propn", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَزَيْدٌ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so Zayd».", "«o hâlde Zeyd».", segments=[seg("فَ", "fa", "conj"), seg("زَيْدٌ", "zayd", "propn")]),
  W("اسْمُهَا", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", KM], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its ism».", "«ismidir».", segments=[seg("اسْمُ", "ism", "noun"), pr3fs()]),
  atf_wa("وَجُمْلَةُ", "jumla", "noun", ["mubtada-khabar", "idafa-definiteness"], "جُمْلَةُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the clause».", "«ve cümlesi».", "جُمْلَةُ"),
  cited("يَجِيءُ", "jaa", "verb", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«yajīʾu».", "«yecîu»."),
  W("خَبَرُهَا", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness", KM], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is its khabar».", "«haberidir».", segments=[seg("خَبَرُ", "khabar", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallinde»."),
  W("نَصْبٍ", "nasb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naṣb».", "«nasb».", punct="؛"),
  atf_wa("وَقَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("تَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«enters».", "«girer»."),
  cited("أَنْ", "an-masdariyya", "part", ["fail", "an-masdariyya"], "فَاعِلٌ — الْحَرْفُ مَحْكِيٌّ.", "«an».", "«en»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("خَبَرِهَا", "khabar", "noun", ["huruf-jarr", "idafa-definiteness", KM], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its khabar».", "«haberine».", punct="،", segments=[seg("خَبَرِ", "khabar", "noun"), pr3fs()]),
  nahwu(),
  cited("كَادَ", "kada", "verb", [KM, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«was about to».", "«az kalsın»."),
  ZAYD("اسْمُ كَادَ مَرْفُوعٌ."),
  AN(),
  KH_V("يَجِيءَ", "jaa", "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ كَادَ.", "«come».", "«gelecekti».", punct=".", tags=["hollow-verbs"]),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And when the particle of negation enters on كَادَ, it is like the other verbs on the soundest view, whether past or present; some said it becomes affirmative, and some said affirmative in the past and like the other verbs in the present." + C_EN,
 "tr": "كَادَ'ye nefy harfi girdiğinde, en sahih görüşe göre mâzî olsun muzâri olsun diğer fiiller gibidir; bazıları müsbet olur dedi, bazıları da mâzîde müsbet, muzâride diğer fiiller gibidir dedi." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -diğinde».", "إِذَا"),
  W("دَخَلَ", "dakhala", "verb", ["idha-shartiyya", "fail"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«enters».", "«girdiğinde»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  cited("كَادَ", "kada", "verb", ["huruf-jarr", KM], "فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«kāda».", "«kâde»."),
  W("حَرْفُ", "harf", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مُرَفُوعٌ مُؤَخَّرٌ، وَهُوَ مُضَافٌ.", "«the particle of».", "«harfi»."),
  W("النَّفْيِ", "nafy", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«negation».", "«nefy»."),
  W("فَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَهِيَ مُبْتَدَأٌ.", "«it is».", "«o».", segments=[seg("فَ", "fa", "conj"), seg("هِيَ", "hiya", "pron")]),
  ka_("كَسَائِرِ", "sair-rest", "noun", ["mubtada-khabar", "idafa-definiteness"], "سَائِرِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«like the other».", "«diğer ... gibidir».", "سَائِرِ"),
  W("الْأَفْعَالِ", "fil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verbs».", "«fiiller»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«göre»."),
  W("الْأَصَحِّ", "asahh", "noun", ["huruf-jarr", "ism-tafdil"], "مَجْرُورٌ — اسْمُ تَفْضِيلٍ.", "«the soundest view».", "«en sahih görüşe».", punct="،"),
  W("مَاضِيًا", "madi", "noun", ["hal", KM], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ.", "«past».", "«mâzî»."),
  W("كَانَ", "kana", "verb", [KM, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "«whether it be».", "«olsun»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُضَارِعًا", "mudari", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ.", "«present».", "«muzâri».", punct="؛"),
  atf_wa("وَقِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ بَعْدَهُ.", "«and it was said».", "«ve denildi».", "قِيلَ", punct=":"),
  W("تَكُونُ", "kana", "verb", [KM, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«it becomes».", "«olur»."),
  W("مُثْبَتَةً", "muthbat", "noun", [KM, "ism-maful"], "خَبَرُ تَكُونُ مَنْصُوبٌ.", "«affirmative».", "«müsbet».", punct="،"),
  atf_wa("وَقِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and it was said».", "«ve denildi».", "قِيلَ", punct=":"),
  W("مُثْبَتَةٌ", "muthbat", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ.", "«affirmative».", "«müsbettir»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past».", "«mâzîde»."),
  ka_("كَسَائِرِ", "sair-rest", "noun", ["mubtada-khabar", "idafa-definiteness"], "سَائِرِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ ثَانٍ.", "«like the other».", "«diğer ... gibidir».", "سَائِرِ"),
  W("الْأَفْعَالِ", "fil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verbs».", "«fiiller»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the present».", "«muzâride».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "Their proof for the past is His word, exalted be He: فَذَبَحُوهَا وَمَا كَادُوا يَفْعَلُونَ — on the first view, they slaughtered her and were near to not doing it; on the affirmative view, the slaughtering proves the act was done." + C_EN,
 "tr": "Mâzî için delilleri Allah Teâlâ'nın فَذَبَحُوهَا وَمَا كَادُوا يَفْعَلُونَ sözüdür — birinci görüşe göre onu kestiler ve neredeyse kesmeyeceklerdi; müsbet diyenlere göre kesmeleri fiilin yapıldığını gösterir." + C_TR},
 "tokens": [
  atf_wa("وَدَلِيلُهُمْ", "dalil-proof", "noun", ["mubtada-khabar", "idafa-definiteness"], "دَلِيلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«and their proof».", "«ve delilleri».", "دَلِيلُ", extra_segs=[seg("دَلِيلُ", "dalil-proof", "noun"), pr3mp()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«için»."),
  W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past».", "«mâzî»."),
  W("قَوْلُهُ", "qawl", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word».", "«... sözüdür».", segments=[seg("قَوْلُ", "qawl", "noun"), pr3ms()]),
  W("تَعَالَى", "taala", "verb", ["fail", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — جُمْلَةٌ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.", "«exalted be He».", "«Teâlâ».", punct=":"),
  cited("فَذَبَحُوهَا", "dhabaha", "verb", ["fail", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَذَبَحُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«so they slaughtered her».", "«onu kestiler».", segments=[seg("فَ", "fa", "conj"), seg("ذَبَحُوا", "dhabaha", "verb"), pr3fs()]),
  cited_wa("وَمَا", "ma-nafiya", "part", ["anwa-ma", "la-nafiya"], "مَا نَافِيَةٌ.", "«and not».", "«ve ... -medi».", "مَا"),
  cited("كَادُوا", "kada", "verb", [KM, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهَا.", "«were they near».", "«neredeyse».", segments=[seg("كَادُ", "kada", "verb"), seg("وا", "pron-3mp", "pron")]),
  cited("يَفْعَلُونَ", "faala", "verb", [KM, "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كَادُوا.", "«to do it».", "«yapmayacaklardı».", punct="،"),
  W("فَعَلَى", "ala", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَعَلَى حَرْفُ جَرٍّ.", "«on».", "«göre».", segments=[seg("فَ", "fa", "conj"), seg("عَلَى", "ala", "prep")]),
  W("الْأَوَّلِ", "awwal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the first».", "«birincisine»."),
  W("ذَبَحُوهَا", "dhabaha", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«they slaughtered her».", "«onu kestiler».", segments=[seg("ذَبَحُوا", "dhabaha", "verb"), pr3fs()]),
  atf_wa("وَقَارَبُوا", "qaraba-near", "verb", ["fail", "form-iii-verbs"], "قَارَبُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ.", "«and were near».", "«ve yaklaştılar».", "قَارَبُوا", extra_segs=[seg("قَارَبُ", "qaraba-near", "verb"), seg("وا", "pron-3mp", "pron")]),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«to».", "«-meye»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-me-»."),
  W("يَفْعَلُوا", "faala", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«do it».", "«yapmamaya».", punct="؛"),
  atf_wa("وَعَلَى", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ.", "«and on».", "«ve ... göre».", "عَلَى"),
  W("الْإِثْبَاتِ", "ithbat", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the affirmative view».", "«müsbet görüşe»."),
  W("دَلَّ", "dalla", "verb", ["fail", "doubled-verbs"], "فِعْلٌ مَاضٍ.", "«proves».", "«gösterir»."),
  W("الذَّبْحُ", "dhabh", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the slaughtering».", "«kesmeleri»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«that».", "«-ını»."),
  W("وُقُوعِ", "wuqu", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the occurrence of».", "«yapıldığ-»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the act».", "«fiilin».", punct="."),
 ]})

S.append({"id": "s8", "translation": {
 "en": "And for the present, the verse of Dhū l-Rumma: «When separation has changed the lovers, the residue of passion from the love of Mayya was scarcely about to depart.»" + C_EN,
 "tr": "Muzâri için de Zü'r-Rumme'nin beyti: «Ayrılık sevenleri değiştirdiğinde, Meyye sevgisinden kalan aşk tortusu ayrılmaya yaklaşmadı.»" + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and for».", "«ve ... için».", "فِي"),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«the present».", "«muzâri»."),
  W("قَوْلُ", "qawl", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the verse of».", "«beyti»."),
  W("ذِي", "dhu-al-rumma", "noun", ["idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ.", "«Dhū».", "«Zü»."),
  W("الرُّمَّةِ", "dhu-al-rumma", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«l-Rumma».", "«'r-Rumme'nin».", punct=":"),
  cited("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  cited("غَيَّرَ", "ghayyara", "verb", ["idha-shartiyya", "fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«has changed».", "«değiştirdiğinde»."),
  cited("الْهَجْرُ", "hajr", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«separation».", "«ayrılık»."),
  cited("الْمُحِبِّينَ", "muhibb", "noun", ["maful-bihi", "jam-mudhakkar-salim", "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ.", "«the lovers».", "«sevenleri»."),
  cited("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-madı»."),
  cited("يَكَدْ", "kada", "verb", [KM, "nawasib-wa-jawazim-al-mudari", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِالسُّكُونِ — جَوَابُ الشَّرْطِ.", "«was scarcely about to».", "«yaklaşmadı».", punct="•"),
  cited("رَسِيسُ", "rasis", "noun", [KM, "idafa-definiteness"], "اسْمُ يَكَدْ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the residue of».", "«tortusu»."),
  cited("الْهَوَى", "hawa-passion", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«passion».", "«aşk»."),
  cited("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("حُبِّ", "hubb", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the love of».", "«sevgisi»."),
  cited("مَيَّةَ", "mayya", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«Mayya».", "«Meyye»."),
  cited("يَبْرَحُ", "bariha", "verb", [KM, "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ يَكَدْ.", "«to depart».", "«ayrılmaya».", punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And Ibn Shubruma told him he had erred in لَمْ يَكَدْ; he accepted it and replaced it with لَمْ أَجِدْ. Those who hold the present affirmative argue: had it not been affirmative, Ibn Shubruma would not have objected nor the poet accepted; and those who hold it negative say both of them erred." + C_EN,
 "tr": "İbn Şübrüme ona لَمْ يَكَدْ'de hata ettiğini söyledi; o da kabul edip onu لَمْ أَجِدْ ile değiştirdi. Muzâride müsbet diyenler: müsbet olmasaydı İbn Şübrüme itiraz etmez, şair de kabul etmezdi der; menfî diyenler ise ikisinin de hata ettiğini söyler." + C_TR},
 "tokens": [
  atf_wa("وَقَالَ", "qala", "verb", ["fail", "hollow-verbs"], "قَالَ فِعْلٌ مَاضٍ.", "«and said».", "«ve dedi».", "قَالَ"),
  W("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to him».", "«ona».", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  W("ابْنُ", "ibn", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«Ibn».", "«İbn»."),
  W("شُبْرُمَةَ", "shubruma", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Shubruma».", "«Şübrüme»."),
  W("إِنَّكَ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا.", "«you».", "«sen».", segments=[seg("إِنَّ", "inna", "part"), pr2ms()]),
  W("أَخْطَأْتَ", "akhtaa", "verb", ["inna-wa-akhawatuha", "fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«erred».", "«hata ettin».", segments=[seg("أَخْطَأْ", "akhtaa", "verb"), prTa()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("لَمْ", "lam-jazima", "part", ["huruf-jarr"], "الْمُرَكَّبُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«lam».", "«lem»."),
  cited("يَكَدْ", "kada", "verb", [KM], "تَمَامُ الْمَحْكِيِّ.", "«yakad».", "«yeked».", punct="،"),
  W("فَقَبِلَ", "qabila", "verb", ["fail"], "الْفَاءُ عَاطِفَةٌ، وَقَبِلَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«so he accepted».", "«o da kabul etti».", segments=[seg("فَ", "fa", "conj"), seg("قَبِلَ", "qabila", "verb")]),
  atf_wa("وَأَبْدَلَهُ", "abdala", "verb", ["fail", "maful-bihi", "form-iv-verbs"], "أَبْدَلَ فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and replaced it».", "«ve onu değiştirdi».", "أَبْدَلَ", extra_segs=[seg("أَبْدَلَ", "abdala", "verb"), pr3ms()]),
  bi_("بِلَمْ", "lam-jazima", "part", [], "لَمْ — الْمُرَكَّبُ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«with lam».", "«lem ile».", "لَمْ"),
  cited("أَجِدْ", "wajada", "verb", ["nawasib-wa-jawazim-al-mudari", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — تَمَامُ الْمَحْكِيِّ.", "«ajid».", "«ecid».", punct="."),
  W("فَمَنْ", "man", "pron", ["ism-mawsul", "mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَمَنْ اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«those who».", "«... diyenler».", segments=[seg("فَ", "fa", "conj"), seg("مَنْ", "man", "pron")]),
  W("قَالَ", "qala", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«hold».", "«diyenler»."),
  bi_("بِالْإِثْبَاتِ", "ithbat", "noun", [], "الْإِثْبَاتِ مَجْرُورٌ.", "«the affirmative».", "«müsbet».", "الْإِثْبَاتِ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the present».", "«muzâride»."),
  W("قَالَ", "qala", "verb", ["mubtada-khabar", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ خَبَرُ مَنْ.", "«argue».", "«der».", punct=":"),
  W("لَوْ", "law", "part", ["al-majzum-wal-shart-wal-jaza"], "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.", "«had».", "«-saydı»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَكُنْ", "kana", "verb", ["nawasib-wa-jawazim-al-mudari", KM, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "«it been».", "«olmasaydı»."),
  W("مُثْبَتًا", "muthbat", "noun", [KM, "ism-maful"], "خَبَرُ يَكُنْ مَنْصُوبٌ.", "«affirmative».", "«müsbet»."),
  W("لَمَا", "lam-jazima", "part", ["al-majzum-wal-shart-wal-jaza", "la-nafiya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَمَا نَافِيَةٌ.", "«… would not have».", "«-mazdı».", segments=[seg("لَ", "lam-jawab", "part"), seg("مَا", "ma-nafiya", "part")]),
  W("اعْتَرَضَ", "itarada", "verb", ["fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ.", "«objected».", "«itiraz etmezdi»."),
  W("ابْنُ", "ibn", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«Ibn».", "«İbn»."),
  W("شُبْرُمَةَ", "shubruma", "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ.", "«Shubruma».", "«Şübrüme»."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«nor».", "«ne de».", "لَا"),
  W("قَبِلَ", "qabila", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«accepted».", "«kabul ederdi»."),
  W("الشَّاعِرُ", "shair", "noun", ["fail", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the poet».", "«şair».", punct="؛"),
  atf_wa("وَمَنْ", "man", "pron", ["ism-mawsul", "mubtada-khabar"], "مَنْ اسْمٌ مَوْصُولٌ مُبْتَدَأٌ.", "«and those who».", "«ve ... diyenler».", "مَنْ"),
  W("قَالَ", "qala", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«hold».", "«diyenler»."),
  bi_("بِالنَّفْيِ", "nafy", "noun", [], "النَّفْيِ مَجْرُورٌ.", "«the negative».", "«menfî».", "النَّفْيِ"),
  W("قَالَ", "qala", "verb", ["mubtada-khabar", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ خَبَرُ مَنْ.", "«say».", "«der».", punct=":"),
  W("أَخْطَأَ", "akhtaa", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ.", "«erred».", "«hata etti»."),
  W("كِلَاهُمَا", "kila", "noun", ["fail", "idafa-definiteness", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«both of them».", "«ikisi de».", punct=".", segments=[seg("كِلَا", "kila", "noun"), pr3d()]),
 ]})

S.append({"id": "s10", "translation": {
 "en": "And the third is طَفِقَ, كَرَبَ, جَعَلَ and أَخَذَ; their khabar is a muḍāriʿ without أَنْ, like كَادَ — as طَفِقَ زَيْدٌ يَفْعَلُ, and His word: وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِنْ وَرَقِ الْجَنَّةِ. And أَوْشَكَ is like عَسَى and كَادَ in use: أَوْشَكَ زَيْدٌ أَنْ يَجِيءَ, أَوْشَكَ أَنْ يَجِيءَ زَيْدٌ, and أَوْشَكَ زَيْدٌ يَجِيءُ." + C_EN,
 "tr": "Üçüncüsü طَفِقَ, كَرَبَ, جَعَلَ ve أَخَذَ'dir; haberleri كَادَ gibi أَنْ'siz muzâridir — طَفِقَ زَيْدٌ يَفْعَلُ ve Allah'ın وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِنْ وَرَقِ الْجَنَّةِ sözü gibi. أَوْشَكَ ise kullanımda عَسَى ve كَادَ gibidir: أَوْشَكَ زَيْدٌ أَنْ يَجِيءَ, أَوْشَكَ أَنْ يَجِيءَ زَيْدٌ ve أَوْشَكَ زَيْدٌ يَجِيءُ." + C_TR},
 "tokens": [
  atf_wa("وَالثَّالِثُ", "thalith", "noun", ["mubtada-khabar"], "الثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third».", "«üçüncüsü».", "الثَّالِثُ"),
  cited("طَفِقَ", "tafiqa", "verb", ["mubtada-khabar", KM], "خَبَرٌ — فِعْلٌ مَحْكِيٌّ.", "«ṭafiqa».", "«tafika»."),
  cited_wa("وَكَرَبَ", "karaba-approach", "verb", [KM], "كَرَبَ مَعْطُوفٌ.", "«karaba».", "«kerabe».", "كَرَبَ"),
  cited_wa("وَجَعَلَ", "jaala", "verb", [KM], "جَعَلَ مَعْطُوفٌ.", "«jaʿala».", "«ceale».", "جَعَلَ"),
  cited_wa("وَأَخَذَ", "akhadha", "verb", [KM], "أَخَذَ مَعْطُوفٌ.", "«and akhadha».", "«ve ehaze».", "أَخَذَ", punct="،"),
  atf_wa("وَخَبَرُهَا", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness", KM], "خَبَرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their khabar».", "«ve haberleri».", "خَبَرُ", extra_segs=[seg("خَبَرُ", "khabar", "noun"), pr3fs()]),
  W("مُضَارِعٌ", "mudari", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a muḍāriʿ».", "«muzâridir»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا — بِلَا مُرَكَّبٌ بِمَعْنَى «مِنْ غَيْرِ».", "«without».", "«-siz».", "لَا"),
  cited("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«an».", "«en»."),
  ka_("كَكَادَ", "kada", "verb", [KM], "كَادَ فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«like kāda».", "«kâde gibi».", "كَادَ", punct="،"),
  nahwu(),
  cited("طَفِقَ", "tafiqa", "verb", [KM], "فِعْلٌ مَاضٍ نَاقِصٌ — لِلشُّرُوعِ.", "«began».", "«başladı»."),
  ZAYD("اسْمُ طَفِقَ مَرْفُوعٌ."),
  cited("يَفْعَلُ", "faala", "verb", [KM, "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ طَفِقَ.", "«to act».", "«yapmaya».", punct="،"),
  atf_wa("وَقَوْلُهُ", "qawl", "noun", ["atf-nasaq", "idafa-definiteness"], "قَوْلُ مَعْطُوفٌ عَلَى الْمَحْكِيِّ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His word».", "«ve ... sözü».", "قَوْلُ", extra_segs=[seg("قَوْلُ", "qawl", "noun"), pr3ms()], punct=":"),
  cited("وَطَفِقَا", "tafiqa", "verb", [KM, "al-muthanna"], "الْوَاوُ عَاطِفَةٌ، وَطَفِقَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالْأَلِفُ اسْمُهَا.", "«and they both began».", "«ikisi de başladılar».", segments=[seg("وَ", "wa", "conj"), seg("طَفِقَ", "tafiqa", "verb"), seg("ا", "pron-3d", "pron")]),
  cited("يَخْصِفَانِ", "khasafa", "verb", [KM, "fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ طَفِقَا.", "«to sew».", "«örtmeye»."),
  cited("عَلَيْهِمَا", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ.", "«upon themselves».", "«üzerlerine».", segments=[seg("عَلَيْ", "ala", "prep"), pr3d()]),
  cited("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("وَرَقِ", "waraq", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the leaves of».", "«yaprakları»."),
  cited("الْجَنَّةِ", "janna", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Garden».", "«cennet».", punct="."),
  cited_wa("وَأَوْشَكَ", "awshaka", "verb", ["mubtada-khabar", KM, "form-iv-verbs"], "أَوْشَكَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and awshaka».", "«ve evşeke».", "أَوْشَكَ"),
  ka_("كَعَسَى", "asa-hope", "verb", ["mubtada-khabar", KM], "عَسَى فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«is like ʿasā».", "«asâ gibidir».", "عَسَى"),
  cited_wa("وَكَادَ", "kada", "verb", [KM], "كَادَ مَعْطُوفٌ.", "«and kāda».", "«ve kâde».", "كَادَ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الِاسْتِعْمَالِ", "istimal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«use».", "«kullanım».", punct=":"),
  cited("أَوْشَكَ", "awshaka", "verb", [KM], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«was on the point».", "«neredeyse»."),
  ZAYD("اسْمُ أَوْشَكَ مَرْفُوعٌ."),
  AN(),
  KH_V("يَجِيءَ", "jaa", "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ أَوْشَكَ.", "«to come».", "«gelecekti».", punct="،", tags=["hollow-verbs"]),
  cited_wa("وَأَوْشَكَ", "awshaka", "verb", [KM, "fail"], "أَوْشَكَ فِعْلٌ مَاضٍ تَامٌّ.", "«and was on the point».", "«ve neredeyse».", "أَوْشَكَ"),
  AN(),
  KH_V("يَجِيءَ", "jaa", "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ أَوْشَكَ.", "«to come».", "«gelmesi».", tags=["hollow-verbs"]),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلُ يَجِيءَ مَرْفُوعٌ.", "«Zayd».", "«Zeyd'in».", punct="،"),
  cited_wa("وَأَوْشَكَ", "awshaka", "verb", [KM], "أَوْشَكَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and was on the point».", "«ve neredeyse».", "أَوْشَكَ"),
  ZAYD("اسْمُ أَوْشَكَ مَرْفُوعٌ."),
  cited("يَجِيءُ", "jaa", "verb", [KM, "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ أَوْشَكَ بِلَا أَنْ.", "«come».", "«geliyordu».", punct="."),
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
 "dunuww": need("dunuww", "دُنُوّ", "د ن و", "noun", "nearness, drawing near — the maṣdar of دَنَا", "yakınlık, yaklaşma — denâ'nın masdarı", 4),
 "sair-rest": need("sair-rest", "سَائِر", "س ي ر", "noun", "the rest of, the other (always annexed)", "diğer, geri kalan (daima muzâf)", 3),
 "muhibb": need("muhibb", "مُحِبّ", "ح ب ب", "noun", "a lover — the Form IV ism fāʿil of أَحَبَّ; plural مُحِبُّونَ", "seven, âşık — ehabbe'nin ism-i fâili; cem'i مُحِبُّونَ", 3),
 "rasis": need("rasis", "رَسِيس", "ر س س", "noun", "the residue, the first trace (of a passion)", "tortu, kalıntı (bir sevdanın ilk izi)", 5),
 "mayya": need("mayya", "مَيَّة", "م ي ي", "propn", "Mayya — the beloved of Dhū l-Rumma's poems", "Meyye — Zü'r-Rumme'nin şiirlerindeki sevgili", 5),
 "shubruma": need("shubruma", "ابْن شُبْرُمَة", "ش ب ر م", "propn", "Ibn Shubruma (d. 144/761) — the Kufan judge and man of letters who corrected Dhū l-Rumma", "İbn Şübrüme (ö. 144/761) — Zü'r-Rumme'yi düzelten Kûfeli kadı ve edip", 5),
 "waraq": need("waraq", "وَرَق", "و ر ق", "noun", "leaves, foliage (collective)", "yaprak, yapraklar (cins ismi)", 2),
 "itarada": need("itarada", "اِعْتَرَضَ", "ع ر ض", "verb", "to object, to raise an objection (Form VIII)", "itiraz etmek (VIII. bâb)", 4),
 "khasafa": need("khasafa", "خَصَفَ", "خ ص ف", "verb", "to stitch together, to patch (leaves, sandals)", "dikmek, yamamak (yaprak, nalın)", 4),
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
put_morph(mo, "itarada", _nfc(_sg.derived(_sg.B8, _sg.W8, "َ", "اِعْتَرَض", "عْتَرِض", "اِعْتَرِض", "اِعْتِرَاض", "مُعْتَرِض", "مُعْتَرَض", "اُعْتُرِضَ", "يُعْتَرَضُ", "اِعْتَرَضَ يَعْتَرِضُ اعْتِرَاضًا: أَوْرَدَ اعْتِرَاضًا — بَابُ الِافْتِعَالِ.")))
put_morph(mo, "khasafa", _nfc(_sg.sound1("daraba", "خَصَف", "خْصِف", "اِخْصِف", "خَصْف", "خَاصِف", "مَخْصُوف", "خُصِفَ", "يُخْصَفُ", "خَصَفَ يَخْصِفُ خَصْفًا: أَلْزَقَ وَرَقًا بِوَرَقٍ أَوْ خَرَزَ النَّعْلَ — بَابُ ضَرَبَ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch26 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "أَفْعَالُ الْمُقَارَبَةِ فِي الْكَافِيَةِ", "en": "The verbs of approach in the Kafiya: hope, occurrence and setting-about — ʿasā's two uses, kāda's bare khabar, the negated-kāda dispute, and awshaka", "tr": "Kâfiye'de mukârebe fiilleri: recâ, husûl ve başlama — asâ'nın iki kullanımı, kâde'nin en'siz haberi, menfî kâde ihtilâfı ve evşeke"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — أفعال المقاربة: ما وضع لدنو الخبر رجاء أو حصولا أو أخذا فيه", "ضياء صونغور اوغلى — دفتر الكافية: عسى غير متصرفة وعلى وجهين؛ كاد وخبرها؛ الخلاف في كاد المنفية مع آية البقرة وبيت ذي الرمة وتصحيح ابن شبرمة؛ طفق وكرب وجعل وأخذ؛ أوشك"],
 "question": {
  "en": ["What makes a verb one of APPROACH? It does not say the khabar happened; it says the khabar is NEAR — and the three kinds are three reasons for nearness: the speaker hopes for it (عَسَى), it was about to occur (كَادَ), or the subject has set about it (طَفِقَ، كَرَبَ، جَعَلَ، أَخَذَ).",
         "Why does عَسَى have no muḍāriʿ? It is jāmid — frozen in the māḍī: no present, no imperative, no prohibition, no passive. The sarf tab shows only the cells that exist; absence is the doctrine, not a gap.",
         "How is عَسَى used? Two ways. Defective: عَسَى زَيْدٌ أَنْ يَخْرُجَ — Zayd is the ism, the أَنْ-clause the khabar in the place of naṣb. Complete: عَسَى أَنْ يَخْرُجَ زَيْدٌ — the whole clause is the DOER of عَسَى and Zayd the doer of يَخْرُجَ. And sometimes أَنْ is simply dropped.",
         "What does كَادَ take? A bare muḍāriʿ as its khabar — كَادَ زَيْدٌ يَجِيءُ — and sometimes أَنْ enters on it. Set it beside عَسَى: the one prefers أَنْ, the other prefers to do without it.",
         "Does negated كَادَ affirm or deny? On the soundest view it behaves like any verb: مَا كَادَ denies. The aya فَذَبَحُوهَا وَمَا كَادُوا يَفْعَلُونَ is read both ways — «they slaughtered her, and had been near to not doing it», or, for those who say negated كَادَ affirms, the slaughter itself proves the act. For the present tense the evidence is Dhū l-Rumma's لَمْ يَكَدْ … يَبْرَحُ and Ibn Shubruma's correction, which each side reads in its own favour.",
         "And the setting-about verbs? Their khabar is a muḍāriʿ without أَنْ, like كَادَ: طَفِقَ زَيْدٌ يَفْعَلُ, and the aya وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِنْ وَرَقِ الْجَنَّةِ. أَوْشَكَ joins the family and is used all three ways.",
         "What does the engine do? The kernel's KANA table already pushes [ism-raf, khabar-naṣb] for كَادَ and عَسَى; the أَنْ before the khabar is read as maṣdariyya by its verb; the jāmid flag on عَسَى keeps the paradigm honest, and the TartibEngine refuses to front the khabar of a verb of approach."],
  "tr": ["Bir fiili MUKÂREBE fiili yapan nedir? Haberin olduğunu söylemez; haberin YAKIN olduğunu söyler — üç kısım yakınlığın üç sebebidir: konuşan onu umar (عَسَى), olmak üzereydi (كَادَ) ya da özne ona başlamıştır (طَفِقَ، كَرَبَ، جَعَلَ، أَخَذَ).",
         "عَسَى'nın neden muzârii yok? Câmiddir — mâzîde donmuştur: muzârisi, emri, nehyi, meçhulü yoktur. Sarf sekmesi yalnız var olan hücreleri gösterir; yokluk bir eksik değil, doktrindir.",
         "عَسَى nasıl kullanılır? İki yolla. Nâkıs: عَسَى زَيْدٌ أَنْ يَخْرُجَ — Zeyd isim, أَنْ cümlesi mahallen mansûb haber. Tam: عَسَى أَنْ يَخْرُجَ زَيْدٌ — bütün cümle عَسَى'nın FÂİLİ, Zeyd ise يَخْرُجَ'nun fâili. Ve bazen أَنْ düpedüz düşer.",
         "كَادَ ne alır? Haber olarak çıplak bir muzâri — كَادَ زَيْدٌ يَجِيءُ — ve bazen ona أَنْ girer. عَسَى ile yan yana koy: biri أَنْ'i tercih eder, öteki onsuz olmayı.",
         "Menfî كَادَ olumlar mı, olumsuzlar mı? En sahih görüşe göre her fiil gibi davranır: مَا كَادَ olumsuzlar. فَذَبَحُوهَا وَمَا كَادُوا يَفْعَلُونَ âyeti iki türlü okunur — «onu kestiler ve neredeyse kesmeyeceklerdi» ya da, menfî كَادَ olumlar diyenlere göre, kesmenin kendisi fiili ispat eder. Muzâri için delil Zü'r-Rumme'nin لَمْ يَكَدْ … يَبْرَحُ'u ve İbn Şübrüme'nin düzeltmesidir; her taraf bunu kendi lehine okur.",
         "Ya başlama fiilleri? Haberleri كَادَ gibi أَنْ'siz muzâridir: طَفِقَ زَيْدٌ يَفْعَلُ ve وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِنْ وَرَقِ الْجَنَّةِ âyeti. أَوْشَكَ aileye katılır ve üç şekilde de kullanılır.",
         "Motor ne yapar? Çekirdeğin KANA tablosu كَادَ ve عَسَى için zaten [ism-ref', haber-nasb] iter; haberin önündeki أَنْ fiili sayesinde masdariyye okunur; عَسَى üzerindeki câmid bayrağı çekimi dürüst tutar ve TartibEngine bir mukârebe fiilinin haberini öne almayı reddeder."]},
 "plain": {
  "en": "The verbs of approach say a thing was close to happening: ʿasā «it is hoped», kāda «was about to», ṭafiqa «began to». They govern like kāna, with their predicate usually a verb clause, sometimes introduced by an. The one puzzle is negated kāda, which the schools read two ways.",
  "tr": "Mukârebe fiilleri bir şeyin olmaya yakın olduğunu söyler: asâ «umulur ki», kâde «az kalsın», tafika «başladı». Kâne gibi amel ederler; yüklemleri çoğunlukla bir fiil cümlesidir, bazen başında en bulunur. Tek bilmece, mekteplerin iki türlü okuduğu menfî kâde'dir."},
 "explanation": {
  "en": "The definition is the Kafiya's and names the class by what it contributes: not an act, but the NEARNESS of the khabar, and the three kinds are three grounds for calling it near. The notebook takes عَسَى first because it is the odd one out twice over — it has no tenses but the past, and it is used both as a defective verb with an ism and a khabar and as a complete one whose doer is the whole أَنْ-clause; the dropping of أَنْ (عَسَى زَيْدٌ يَخْرُجُ) is the bridge to كَادَ, whose khabar is bare by default and takes أَنْ only occasionally. The long middle of the chapter is the dispute on negated كَادَ, and the notebook lays it out as a madrasah would: the ruling (like any verb, on the soundest view), the two minority positions, the aya of the cow read by each side, Dhū l-Rumma's verse with its hemistich break, and the anecdote of Ibn Shubruma — which, tellingly, both sides claim. The setting-about verbs and أَوْشَكَ close the chapter with the Qurʾānic leaves of the Garden, where طَفِقَا carries the dual alif as its ism and يَخْصِفَانِ the retained nūn. The notebook writes يَجِيئُ with the hamza on a yāʾ seat; the chapter cites the received يَجِيءُ and the manifest records the divergence.",
  "tr": "Tarif Kâfiye'nindir ve sınıfı kattığı şeyle adlandırır: bir eylem değil, haberin YAKINLIĞI; üç kısım onu yakın saymanın üç gerekçesidir. Defter önce عَسَى'yı alır, çünkü iki kez istisnadır — mâzîden başka zamanı yoktur ve hem ismi ve haberi olan nâkıs bir fiil, hem de fâili bütün bir أَنْ cümlesi olan tam bir fiil olarak kullanılır; أَنْ'in düşmesi (عَسَى زَيْدٌ يَخْرُجُ) haberi varsayılan olarak çıplak olup أَنْ'i yalnız ara sıra alan كَادَ'ye köprüdür. Bâbın uzun ortası menfî كَادَ ihtilâfıdır ve defter onu bir medresenin yapacağı gibi serer: hüküm (en sahih görüşe göre her fiil gibi), iki azınlık görüşü, her tarafın okuduğu bakara âyeti, mısra ayrımıyla Zü'r-Rumme'nin beyti ve — ibretle — iki tarafın da sahiplendiği İbn Şübrüme kıssası. Başlama fiilleri ve أَوْشَكَ bâbı Kur'ânî cennet yapraklarıyla kapar; orada طَفِقَا tesniye elifini isim olarak, يَخْصِفَانِ sâbit nûnu taşır. Defter يَجِيئُ'yu hemzeyi yâ kürsüsünde yazar; bâb alınan يَجِيءُ'yu zikreder ve manifest farkı kaydeder."},
 "examples": [
  {"ar": "أَفْعَالُ الْمُقَارَبَةِ: مَا وُضِعَ لِدُنُوِّ الْخَبَرِ رَجَاءً أَوْ حُصُولًا أَوْ أَخْذًا فِيهِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "عَسَى زَيْدٌ أَنْ يَخْرُجَ", "en": "ʿasā defective.", "tr": "Nâkıs asâ.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "عَسَى أَنْ يَخْرُجَ زَيْدٌ", "en": "ʿasā complete — the clause is its doer.", "tr": "Tam asâ — cümle fâilidir.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "كَادَ زَيْدٌ يَجِيءُ", "en": "kāda with a bare khabar.", "tr": "Çıplak haberli kâde.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "فَذَبَحُوهَا وَمَا كَادُوا يَفْعَلُونَ", "en": "Negated kāda in the past.", "tr": "Mâzîde menfî kâde.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "لَمْ يَكَدْ رَسِيسُ الْهَوَى مِنْ حُبِّ مَيَّةَ يَبْرَحُ", "en": "Negated kāda in the present.", "tr": "Muzâride menfî kâde.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "وَطَفِقَا يَخْصِفَانِ عَلَيْهِمَا مِنْ وَرَقِ الْجَنَّةِ", "en": "A setting-about verb.", "tr": "Bir başlama fiili.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«يَعْسَى زَيْدٌ أَنْ يَخْرُجَ»",
   "right": "«عَسَى زَيْدٌ أَنْ يَخْرُجَ — asâ câmiddir, muzârii yoktur»",
   "why": {"en": "ʿasā has only the past; the sarf tab offers no other tense.", "tr": "asâ'nın yalnız mâzîsi vardır; sarf sekmesi başka zaman sunmaz."}},
  {"wrong": "«أَنْ يَخْرُجَ, عَسَى أَنْ يَخْرُجَ زَيْدٌ'da haberdir»",
   "right": "«tam asâ: أَنْ يَخْرُجَ زَيْدٌ onun fâilidir, haberi yoktur»",
   "why": {"en": "With nothing between ʿasā and the clause, the clause is the doer of a complete verb.", "tr": "asâ ile cümle arasında bir şey yoksa cümle tam fiilin fâilidir."}},
  {"wrong": "«مَا كَادَ زَيْدٌ يَقُومُ — Zeyd ayağa kalktı»",
   "right": "«en sahih görüşe göre: Zeyd neredeyse kalkmadı — nefy nefydir»",
   "why": {"en": "The affirmative reading is a minority view the notebook records, not the ruling.", "tr": "Müsbet okuyuş defterin kaydettiği bir azınlık görüşüdür, hüküm değil."}},
  {"wrong": "«يَفْعَلُ زَيْدٌ طَفِقَ»",
   "right": "«طَفِقَ زَيْدٌ يَفْعَلُ — mukârebe fiilinin haberi fiilin önüne geçmez»",
   "why": {"en": "The khabar of a verb of approach is a verb clause and stays after its ism.", "tr": "Mukârebe fiilinin haberi bir fiil cümlesidir ve isminin ardında kalır."}}],
 "relatedNotes": [KM, "al-afal-al-naqisa-fil-kafiya", "an-masdariyya", "nawasib-wa-jawazim-al-mudari", "al-muthanna"]}

ADD_EN = (" Chapter 26 (notebook lines ~316-319): the verbs of approach defined in the notebook's own Arabic (s1); ʿasā, kāda, the negated-kāda dispute with the aya of the cow (2:71) and Dhū l-Rumma's verse, the setting-about verbs with the aya of the leaves (7:22), and awshaka — the notebook's exposition, kept as commentary (s2-s10). Qurʾānic text as the source prints it. "
          "DIVERGENCE: the notebook writes يَجِيئُ; the chapter cites the received يَجِيءُ. The chain of the Ibn Shubruma anecdote (ʿUtba's riwāya) is not reproduced.")
ADD_TR = (" Yirmi altıncı bâb (defter satırları ~316-319): mukârebe fiilleri defterin kendi Arapçasıyla tarif edilir (s1); asâ, kâde, bakara âyeti (2:71) ve Zü'r-Rumme'nin beytiyle menfî kâde ihtilâfı, yapraklar âyetiyle (7:22) başlama fiilleri ve evşeke — defterin açıklaması, şerh olarak (s2-s10). Kur'ân metni kaynağın bastığı gibi. "
          "FARK: defter يَجِيئُ yazar; bâb alınan يَجِيءُ'yu zikreder. İbn Şübrüme kıssasının senedi (Utbe rivâyeti) aktarılmamıştır.")
write_out(26, S, TITLE, ADD_EN, ADD_TR, "316-319", GLOSS_ADD, notes=(NOTE,),
          related=((KM, [K]), ("al-afal-al-naqisa-fil-kafiya", [K])))
report(26, S, GLOSS_ADD, (NOTE,))
