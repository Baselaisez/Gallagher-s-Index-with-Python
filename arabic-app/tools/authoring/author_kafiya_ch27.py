# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 27: THE VERB OF WONDER (fiʿl al-taʿajjub). The definition in the notebook's own Arabic; the two forms
مَا أَفْعَلَهُ and أَفْعِلْ بِهِ, non-conjugating; built only from what the elative is built from — otherwise أَشَدّ and its like;
no fronting of the maʿmūl and no separation (al-Māzinī's ẓarf, the majority's كَانَ); Sībawayh's and al-Akhfash's readings of مَا
in the first form and of بِهِ in the second.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~319-325 of the transcription.

  VERBATIM: s1. COMMENTARY (the notebook): s2-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch27.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "fil-al-taajjub-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "فِعْلُ التَّعَجُّبِ", "en": "The verb of wonder — mā afʿalahu and afʿil bihi", "tr": "Taaccüb fiili — mâ ef'alehû ve ef'il bihî"}
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

def TJ(full, ar, en, tr, punct=None, segs=None, tags=()):
    return cited(full, "ahsana", "verb", [K, "al-mabni-wal-mudmar"] + list(tags), ar, en, tr, punct=punct, segments=segs)

S.append({"id": "s1", "translation": {
 "en": "The verb of wonder: what was set down to bring wonder into being.",
 "tr": "Taaccüb fiili: taaccübü inşâ etmek için konulan fiildir."},
 "tokens": [
  W("فِعْلُ", "fil", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the verb of».", "«fiili»."),
  W("التَّعَجُّبِ", "taajjub", "noun", ["idafa-definiteness", "form-v-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَعَجَّبَ.", "«wonder».", "«taaccüb».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«was set down».", "«konulan»."),
  li_("لِإِنْشَاءِ", "insha", "noun", ["idafa-definiteness"], "إِنْشَاءِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to bring into being».", "«inşâ etmek için».", "إِنْشَاءِ"),
  W("التَّعَجُّبِ", "taajjub", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wonder».", "«taaccübü».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And it has two forms: مَا أَفْعَلَهُ — as مَا أَحْسَنَ زَيْدًا — and أَفْعِلْ بِهِ — as أَحْسِنْ بِزَيْدٍ; and both do not conjugate: they have no muḍāriʿ and no passive." + C_EN,
 "tr": "İki sîgası vardır: مَا أَفْعَلَهُ — مَا أَحْسَنَ زَيْدًا gibi — ve أَفْعِلْ بِهِ — أَحْسِنْ بِزَيْدٍ gibi; ikisi de tasarruf etmez: muzârileri ve meçhulleri yoktur." + C_TR},
 "tokens": [
  atf_wa("وَلَهُ", "li", "prep", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and it has».", "«ve onun ... vardır».", "لَهُ", extra_segs=[seg("لَ", "li", "prep"), pr3ms()]),
  W("صِيغَتَانِ", "sigha", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two forms».", "«iki sîgası».", punct=":"),
  cited("مَا", "ma-taajjubiyya", "pron", [K, "anwa-ma", "mubtada-khabar"], "الصِّيغَةُ الْأُولَى — مَحْكِيَّةٌ، بَدَلٌ مِنْ صِيغَتَانِ.", "«mā».", "«mâ»."),
  cited("أَفْعَلَهُ", "afal-wazn", "noun", [K], "تَمَامُ الصِّيغَةِ — الْوَزْنُ مَعَ ضَمِيرِ الْمُتَعَجَّبِ مِنْهُ.", "«afʿalahu».", "«ef'alehû».", punct="،"),
  nahwu(),
  cited("مَا", "ma-taajjubiyya", "pron", [K, "anwa-ma", "mubtada-khabar"], "نَكِرَةٌ تَامَّةٌ بِمَعْنَى شَيْءٍ، مُبْتَدَأٌ — عِنْدَ سِيبَوَيْهِ.", "«how».", "«ne»."),
  TJ("أَحْسَنَ", "فِعْلُ تَعَجُّبٍ مَاضٍ جَامِدٌ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ إِلَى مَا، وَالْجُمْلَةُ خَبَرٌ.", "«beautiful is».", "«güzel»."),
  cited("زَيْدًا", "zayd", "propn", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُتَعَجَّبُ مِنْهُ.", "«Zayd».", "«Zeyd».", punct="؛"),
  cited_wa("وَأَفْعِلْ", "afal-wazn", "noun", [K], "الصِّيغَةُ الثَّانِيَةُ — مَحْكِيَّةٌ مَعْطُوفَةٌ.", "«and afʿil».", "«ve ef'il».", "أَفْعِلْ"),
  cited("بِهِ", "bi", "prep", [K, "huruf-jarr"], "تَمَامُ الصِّيغَةِ — الْبَاءُ وَضَمِيرُ الْمُتَعَجَّبِ مِنْهُ.", "«bihi».", "«bihî».", punct="،", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  nahwu(),
  TJ("أَحْسِنْ", "فِعْلُ تَعَجُّبٍ عَلَى صُورَةِ الْأَمْرِ، مَبْنِيٌّ عَلَى السُّكُونِ.", "«how beautiful».", "«ne güzel»."),
  bi_("بِزَيْدٍ", "zayd", "propn", [K], "زَيْدٍ مَجْرُورٌ لَفْظًا — فَاعِلٌ عِنْدَ سِيبَوَيْهِ.", "«is Zayd».", "«Zeyd».", "زَيْدٍ", punct="؛"),
  atf_wa("وَهُمَا", "pron-dual", "pron", ["mubtada-khabar", "al-muthanna"], "هُمَا مُبْتَدَأٌ.", "«and both».", "«ve ikisi».", "هُمَا"),
  W("غَيْرُ", "ghayr", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«not».", "«... etmez»."),
  W("مُتَصَرِّفَيْنِ", "mutasarrif", "noun", ["idafa-definiteness", "al-muthanna", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«conjugating».", "«tasarruf».", punct=":"),
  W("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"], "نَافِيَةٌ لِلْجِنْسِ.", "«no».", "«yoktur»."),
  W("مُضَارِعَ", "mudari", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«muḍāriʿ».", "«muzârileri»."),
  W("لَهُمَا", "li", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ — خَبَرُ لَا.", "«they have».", "«onların».", segments=[seg("لَ", "li", "prep"), pr3d()]),
  atf_wa("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"], "لَا نَافِيَةٌ لِلْجِنْسِ.", "«and no».", "«ve ... yok».", "لَا"),
  W("مَجْهُولَ", "majhul", "noun", ["la-nafiya-lil-jins", "ism-maful"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ، وَخَبَرُهَا مَحْذُوفٌ.", "«passive».", "«meçhulleri».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And they are built only from what the elative is built from; so where they are barred — as in the forms augmented beyond the triliteral, and in colour and defect — one says مَا أَشَدَّ اسْتِخْرَاجَهُ and أَشْدِدْ بِاسْتِخْرَاجِهِ." + C_EN,
 "tr": "Yalnız ism-i tafdîlin yapıldığı maddelerden yapılırlar; mümteni oldukları yerde — sülâsîye ziyâdeli bâblarda, renk ve kusurda — مَا أَشَدَّ اسْتِخْرَاجَهُ ve أَشْدِدْ بِاسْتِخْرَاجِهِ denir." + C_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... -maz».", "لَا"),
  W("يُبْنَيَانِ", "bana", "verb", ["naib-al-fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ نَائِبُ فَاعِلٍ.", "«are they built».", "«yapılırlar»."),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ حَصْرٍ.", "«only».", "«yalnız»."),
  W("مِمَّا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«from what».", "«... -dan».", segments=[seg("مِنْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("يُبْنَى", "bana", "verb", ["ism-mawsul", "naib-al-fail", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْجُمْلَةُ صِلَةٌ.", "«is built».", "«yapılan»."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr", "ism-mawsul"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«from it».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  W("أَفْعَلُ", "afal-wazn", "noun", ["naib-al-fail", "idafa-definiteness", "ism-tafdil"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the afʿal of».", "«ef'alü»."),
  W("التَّفْضِيلِ", "tafdil", "noun", ["idafa-definiteness", "ism-tafdil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«preference».", "«'t-tafdîl».", punct="؛"),
  W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«so where».", "«... -dığı yerde».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  W("امْتَنَعَا", "imtanaa", "verb", ["idha-shartiyya", "fail", "al-muthanna", "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالْأَلِفُ فَاعِلٌ — فِعْلُ الشَّرْطِ.", "«they are barred».", "«mümteni oldukları».", punct="،"),
  ka_("كَمَا", "ma-mawsula", "pron", ["ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«as».", "«... gibi».", "مَا"),
  W("فِي", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — الْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«in».", "«-de»."),
  W("الْمَزِيدِ", "mazid", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the augmented».", "«ziyâdeli»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«beyond».", "«-e»."),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the triliteral».", "«sülâsî»."),
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  W("اللَّوْنِ", "lawn", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«colour».", "«renk»."),
  atf_wa("وَالْعَيْبِ", "ayb", "noun", ["atf-nasaq"], "الْعَيْبِ مَعْطُوفٌ مَجْرُورٌ.", "«and defect».", "«ve kusur».", "الْعَيْبِ", punct="،"),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ، وَنَائِبُ الْفَاعِلِ الْمَقُولُ.", "«one says».", "«denir».", punct=":"),
  cited("مَا", "ma-taajjubiyya", "pron", [K, "anwa-ma"], "نَكِرَةٌ تَامَّةٌ مُبْتَدَأٌ.", "«how».", "«ne»."),
  cited("أَشَدَّ", "ashadda", "verb", [K, "doubled-verbs"], "فِعْلُ تَعَجُّبٍ جَامِدٌ، وَالْفَاعِلُ مُسْتَتِرٌ — يُتَوَصَّلُ بِهِ إِلَى الْمُمْتَنِعِ.", "«intense is».", "«ne kadar»."),
  cited("اسْتِخْرَاجَهُ", "istikhraj", "noun", [K, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ الْفِعْلِ الْمُمْتَنِعِ.", "«his extracting».", "«onun çıkarması».", segments=[seg("اسْتِخْرَاجَ", "istikhraj", "noun"), pr3ms()]),
  cited_wa("وَأَشْدِدْ", "ashadda", "verb", [K, "doubled-verbs"], "أَشْدِدْ فِعْلُ تَعَجُّبٍ عَلَى صُورَةِ الْأَمْرِ، فُكَّ إِدْغَامُهُ.", "«and how intense».", "«ve ne kadar».", "أَشْدِدْ"),
  bi_("بِاسْتِخْرَاجِهِ", "istikhraj", "noun", [K, "idafa-definiteness"], "اسْتِخْرَاجِ مَجْرُورٌ لَفْظًا، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«is his extracting».", "«onun çıkarması».", "اسْتِخْرَاجِ", punct=".", segs=[seg("بِ", "bi", "prep"), seg("اسْتِخْرَاجِ", "istikhraj", "noun"), pr3msi()]),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the two forms are not handled by fronting or delaying: one does not say مَا زَيْدًا أَحْسَنَ nor بِزَيْدٍ أَحْسِنْ." + C_EN,
 "tr": "İki sîgada takdim ve te'hirle tasarruf olunmaz: مَا زَيْدًا أَحْسَنَ ve بِزَيْدٍ أَحْسِنْ denmez." + C_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... -maz».", "لَا"),
  W("يُتَصَرَّفُ", "tasarrafa", "verb", ["naib-al-fail", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ.", "«are they handled».", "«tasarruf olunmaz»."),
  W("فِيهِمَا", "fi", "prep", ["huruf-jarr", "naib-al-fail"], "فِي حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ — نَائِبُ فَاعِلٍ.", "«in them».", "«ikisinde».", segments=[seg("فِي", "fi", "prep"), pr3d()]),
  bi_("بِتَقْدِيمٍ", "taqdim", "noun", [], "تَقْدِيمٍ مَجْرُورٌ.", "«by fronting».", "«takdimle».", "تَقْدِيمٍ"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«nor».", "«ve ne».", "لَا"),
  W("تَأْخِيرٍ", "takhir", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«delaying».", "«te'hirle».", punct="،"),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«o hâlde ... -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْمَقُولُ.", "«does one say».", "«denmez»."),
  cited("مَا", "ma-taajjubiyya", "pron", [K, "anwa-ma"], "الْمَقُولُ الْمَمْنُوعُ — نَكِرَةٌ تَامَّةٌ مُبْتَدَأٌ.", "«how».", "«ne»."),
  cited("زَيْدًا", "zayd", "propn", [K, "maful-bihi", "taqdim-al-musnad"], "مَفْعُولٌ بِهِ مُقَدَّمٌ — وَتَقْدِيمُهُ مَمْنُوعٌ.", "«Zayd».", "«Zeyd»."),
  TJ("أَحْسَنَ", "فِعْلُ تَعَجُّبٍ مُؤَخَّرٌ عَنْ مَعْمُولِهِ — وَهُوَ الْمَمْنُوعُ.", "«beautiful is».", "«güzel»."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "«nor».", "«ve ne de».", "لَا"),
  bi_("بِزَيْدٍ", "zayd", "propn", [K, "taqdim-al-musnad"], "زَيْدٍ مَجْرُورٌ — الْمَعْمُولُ مُقَدَّمٌ، وَتَقْدِيمُهُ مَمْنُوعٌ.", "«is Zayd».", "«Zeyd».", "زَيْدٍ"),
  TJ("أَحْسِنْ", "فِعْلُ تَعَجُّبٍ عَلَى صُورَةِ الْأَمْرِ مُؤَخَّرٌ عَنْ مَعْمُولِهِ.", "«how beautiful».", "«ne güzel».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "Nor by separating the governor from the governed; for al-Māzinī the separation by a ẓarf is permitted — as مَا أَحْسَنَ بِالرَّجُلِ أَنْ يَصْدُقَ — and for most of them the separation by كَانَ — as مَا كَانَ أَحْسَنَ زَيْدًا." + C_EN,
 "tr": "Âmil ile ma'mûl arasını ayırmakla da olmaz; Mâzinî'ye göre zarfla fasıl câizdir — مَا أَحْسَنَ بِالرَّجُلِ أَنْ يَصْدُقَ gibi — çoğunluğa göre ise كَانَ ile fasıl — مَا كَانَ أَحْسَنَ زَيْدًا gibi." + C_TR},
 "tokens": [
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ — مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "«nor».", "«ve ... da olmaz».", "لَا"),
  bi_("بِفَصْلٍ", "fasl", "noun", [], "فَصْلٍ مَجْرُورٌ مَعْطُوفٌ عَلَى بِتَقْدِيمٍ.", "«by separating».", "«ayırmakla».", "فَصْلٍ"),
  W("بَيْنَ", "bayna", "adv", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasını»."),
  W("الْعَامِلِ", "amil", "noun", ["idafa-definiteness", "al-amil-wa-aqsamuh"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governor».", "«âmil»."),
  atf_wa("وَالْمَعْمُولِ", "mamul", "noun", ["atf-nasaq", "al-mamul-wa-aqsamuh"], "الْمَعْمُولِ مَعْطُوفٌ مَجْرُورٌ.", "«and the governed».", "«ile ma'mûl».", "الْمَعْمُولِ", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْمَازِنِيِّ", "mazini", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Māzinī».", "«Mâzinî'ye»."),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is permitted».", "«câizdir»."),
  W("الْفَصْلُ", "fasl", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the separation».", "«fasıl»."),
  bi_("بِالظَّرْفِ", "zarf", "noun", ["maful-fih"], "الظَّرْفِ مَجْرُورٌ.", "«by a ẓarf».", "«zarfla».", "الظَّرْفِ", punct="،"),
  nahwu(),
  cited("مَا", "ma-taajjubiyya", "pron", [K, "anwa-ma"], "نَكِرَةٌ تَامَّةٌ مُبْتَدَأٌ.", "«how».", "«ne»."),
  TJ("أَحْسَنَ", "فِعْلُ تَعَجُّبٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«beautiful is».", "«güzeldir»."),
  bi_("بِالرَّجُلِ", "rajul", "noun", ["maful-fih"], "الرَّجُلِ مَجْرُورٌ — الْجَارُّ وَالْمَجْرُورُ ظَرْفٌ فَاصِلٌ بَيْنَ الْفِعْلِ وَمَعْمُولِهِ.", "«in a man».", "«bir adam hakkında».", "الرَّجُلِ"),
  cited("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that».", "«-ması»."),
  cited("يَصْدُقَ", "sadaqa-verb", "verb", ["nawasib-wa-jawazim-al-mudari", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَحْسَنَ: مَا أَحْسَنَ صِدْقَهُ.", "«he be truthful».", "«doğru söyle-».", punct="،"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("أَكْثَرِهِمْ", "akthar", "noun", ["idafa-definiteness", "ism-tafdil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«most of them».", "«çoğunluğa».", segments=[seg("أَكْثَرِ", "akthar", "noun"), pr3mp()]),
  W("الْفَصْلُ", "fasl", "noun", ["fail", "hadhf-wa-taqdir"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ: يَجُوزُ.", "«the separation».", "«fasıl»."),
  bi_("بِكَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "كَانَ فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«by kāna».", "«kâne ile».", "كَانَ", punct="،"),
  nahwu(),
  cited("مَا", "ma-taajjubiyya", "pron", [K, "anwa-ma"], "نَكِرَةٌ تَامَّةٌ مُبْتَدَأٌ.", "«how».", "«ne»."),
  cited("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "زَائِدَةٌ لِلدَّلَالَةِ عَلَى الْمُضِيِّ، فَاصِلَةٌ بَيْنَ مَا وَفِعْلِ التَّعَجُّبِ.", "«was» — redundant, past-marking.", "«idi» — zâid, mâzî bildirir."),
  TJ("أَحْسَنَ", "فِعْلُ تَعَجُّبٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«beautiful».", "«güzel»."),
  cited("زَيْدًا", "zayd", "propn", [K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd».", "«Zeyd».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And مَا in مَا أَفْعَلَهُ is, for Sībawayh, an indefinite meaning «something», a mubtada, and أَفْعَلَهُ its khabar; for al-Akhfash it is a relative, a mubtada, أَفْعَلَهُ its ṣila and the khabar dropped — so مَا أَحْسَنَ زَيْدًا means «what has made Zayd beautiful is something great»." + C_EN,
 "tr": "مَا أَفْعَلَهُ'deki مَا Sîbeveyh'e göre «şey» mânâsında nekre bir mübtedâ, أَفْعَلَهُ haberidir; Ahfeş'e göre ism-i mevsûl bir mübtedâ, أَفْعَلَهُ sılası, haber mahzûftur — مَا أَحْسَنَ زَيْدًا «Zeyd'i güzel kılan büyük bir şeydir» demektir." + C_TR},
 "tokens": [
  cited_wa("وَمَا", "ma-taajjubiyya", "pron", ["mubtada-khabar", K, "anwa-ma"], "مَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and mā».", "«ve mâ».", "مَا"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-deki»."),
  cited("مَا", "ma-taajjubiyya", "pron", ["huruf-jarr", K], "الصِّيغَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«mā».", "«mâ»."),
  cited("أَفْعَلَهُ", "afal-wazn", "noun", [K], "تَمَامُ الصِّيغَةِ.", "«afʿalahu».", "«ef'alehû»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ.", "«Sībawayh».", "«Sîbeveyh'e»."),
  W("نَكِرَةٌ", "nakira", "noun", ["mubtada-khabar", "al-marifa-wal-nakira-fil-kafiya"], "خَبَرٌ مَرْفُوعٌ.", "«an indefinite».", "«nekre»."),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«meaning».", "«mânâsında».", "مَعْنَى"),
  W("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«something».", "«şey»."),
  W("مُبْتَدَأٌ", "mubtada", "noun", ["mubtada-khabar"], "خَبَرٌ ثَانٍ، أَوْ بَدَلٌ مِنْ نَكِرَةٌ.", "«a mubtada».", "«bir mübtedâ».", punct="،"),
  cited_wa("وَأَفْعَلَهُ", "afal-wazn", "noun", ["mubtada-khabar", K], "أَفْعَلَهُ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and afʿalahu».", "«ve ef'alehû».", "أَفْعَلَهُ"),
  W("خَبَرُهَا", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its khabar».", "«haberidir».", punct="؛", segments=[seg("خَبَرُ", "khabar", "noun"), pr3fs()]),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْأَخْفَشِ", "akhfash", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Akhfash».", "«Ahfeş'e»."),
  W("مَوْصُولَةٌ", "mawsul", "noun", ["mubtada-khabar", "ism-mawsul"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ.", "«a relative».", "«ism-i mevsûl»."),
  W("مُبْتَدَأٌ", "mubtada", "noun", ["mubtada-khabar"], "خَبَرٌ ثَانٍ.", "«a mubtada».", "«bir mübtedâ».", punct="،"),
  cited_wa("وَأَفْعَلَهُ", "afal-wazn", "noun", ["mubtada-khabar", K], "أَفْعَلَهُ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and afʿalahu».", "«ve ef'alehû».", "أَفْعَلَهُ"),
  W("صِلَتُهَا", "sila", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-mawsul"], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ṣila».", "«sılasıdır».", segments=[seg("صِلَتُ", "sila", "noun"), pr3fs()]),
  atf_wa("وَالْخَبَرُ", "khabar", "noun", ["mubtada-khabar"], "الْخَبَرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the khabar».", "«ve haber».", "الْخَبَرُ"),
  W("مَحْذُوفٌ", "mahdhuf", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is dropped».", "«mahzûftur».", punct="،"),
  W("فَمَا", "ma-taajjubiyya", "pron", [K, "al-fa-fi-khabar-al-mubtada", "mubtada-khabar"], "الْفَاءُ لِلتَّفْرِيعِ، وَمَا الْمَحْكِيَّةُ مُبْتَدَأٌ.", "«so mā».", "«o hâlde mâ».", segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-taajjubiyya", "pron")]),
  TJ("أَحْسَنَ", "مِنْ تَمَامِ الْمَحْكِيِّ.", "«aḥsana».", "«ahsene»."),
  cited("زَيْدًا", "zayd", "propn", [K], "تَمَامُ الْمَحْكِيِّ.", "«Zayd».", "«Zeyd»."),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«means».", "«... demektir».", "مَعْنَى"),
  cited("الَّذِي", "alladhi", "pron", ["ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ مُبْتَدَأٌ — دَاخِلَ التَّقْدِيرِ.", "«what».", "«... kılan»."),
  TJ("أَحْسَنَ", "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«has made beautiful».", "«güzel kılan»."),
  cited("زَيْدًا", "zayd", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd».", "«Zeyd'i»."),
  cited("شَيْءٌ", "shay", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الْخَبَرُ الْمُقَدَّرُ.", "«is something».", "«bir şeydir»."),
  cited("عَظِيمٌ", "azim", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«great».", "«büyük».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And in أَفْعِلْ بِهِ, for Sībawayh بِهِ is the doer and there is no pronoun in أَفْعِلْ; for al-Akhfash بِهِ is the object — the bāʾ for transitivity if the verb is intransitive and redundant if transitive — and the doer is a pronoun, the sense being أَحْسِنْ أَنْتَ بِزَيْدٍ." + C_EN,
 "tr": "أَفْعِلْ بِهِ'de Sîbeveyh'e göre بِهِ fâildir ve أَفْعِلْ'in altında zamir yoktur; Ahfeş'e göre بِهِ mef'ûldür — bâ, fiil lâzımsa ta'diye için, müteaddî ise zâiddir — fâil zamirdir, takdir أَحْسِنْ أَنْتَ بِزَيْدٍ'dir." + C_TR},
 "tokens": [
  atf_wa("وَفِي", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve ... -de».", "فِي"),
  cited("أَفْعِلْ", "afal-wazn", "noun", ["huruf-jarr", K], "الصِّيغَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«afʿil».", "«ef'il»."),
  cited("بِهِ", "bi", "prep", [K], "تَمَامُ الصِّيغَةِ.", "«bihi».", "«bihî».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ.", "«Sībawayh».", "«Sîbeveyh'e»."),
  cited("بِهِ", "bi", "prep", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«bihi».", "«bihî».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("فَاعِلٌ", "fail-doer", "noun", ["mubtada-khabar", "fail"], "خَبَرٌ مَرْفُوعٌ.", "«is the doer».", "«fâildir»."),
  atf_wa("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"], "لَا نَافِيَةٌ لِلْجِنْسِ.", "«and no».", "«ve ... yoktur».", "لَا"),
  W("ضَمِيرَ", "damir", "noun", ["la-nafiya-lil-jins", "al-mabni-wal-mudmar"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«pronoun».", "«zamir»."),
  W("فِي", "fi", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "حَرْفُ جَرٍّ — خَبَرُ لَا.", "«in».", "«-de»."),
  cited("أَفْعِلْ", "afal-wazn", "noun", ["huruf-jarr", K], "فِي مَحَلِّ جَرٍّ — الصِّيغَةُ مَحْكِيَّةٌ.", "«afʿil».", "«ef'il'in altında».", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("الْأَخْفَشِ", "akhfash", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Akhfash».", "«Ahfeş'e»."),
  cited("بِهِ", "bi", "prep", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«bihi».", "«bihî».", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("مَفْعُولٌ", "maful-object", "noun", ["mubtada-khabar", "maful-bihi"], "خَبَرٌ مَرْفُوعٌ.", "«is the object».", "«mef'ûldür».", punct="،"),
  atf_wa("وَالْبَاءُ", "ba-harf", "noun", ["mubtada-khabar", "huruf-jarr"], "الْبَاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the bāʾ».", "«ve bâ».", "الْبَاءُ"),
  li_("لِلتَّعْدِيَةِ", "tadiya", "noun", ["mubtada-khabar"], "التَّعْدِيَةِ مَجْرُورٌ — خَبَرٌ.", "«is for transitivity».", "«ta'diye içindir».", "التَّعْدِيَةِ", segs=[seg("لِ", "li", "prep"), seg("لتَّعْدِيَةِ", "tadiya", "noun")]),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-sa»."),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is».", "«ise»."),
  W("الْفِعْلُ", "fil", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the verb».", "«fiil»."),
  W("لَازِمًا", "lazim", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«intransitive».", "«lâzım»."),
  atf_wa("وَزَائِدَةٌ", "zaid", "noun", ["mubtada-khabar"], "زَائِدَةٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هِيَ.", "«and redundant».", "«ve zâiddir».", "زَائِدَةٌ"),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-sa»."),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَاسْمُهَا مُسْتَتِرٌ.", "«it is».", "«ise»."),
  W("مُتَعَدِّيًا", "mutaaddi", "noun", ["kana-wa-akhawatuha", "ism-fail", "ism-maqsur-manqus"], "خَبَرُ كَانَ مَنْصُوبٌ — مَنْقُوصٌ ظَهَرَتْ فَتْحَتُهُ.", "«transitive».", "«müteaddî».", punct="،"),
  atf_wa("وَالْفَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "fail"], "الْفَاعِلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the doer».", "«ve fâil».", "الْفَاعِلُ"),
  W("ضَمِيرٌ", "damir", "noun", ["mubtada-khabar", "al-mabni-wal-mudmar"], "خَبَرٌ مَرْفُوعٌ.", "«is a pronoun».", "«zamirdir».", punct="،"),
  atf_wa("وَالتَّقْدِيرُ", "taqdir", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "التَّقْدِيرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sense is».", "«ve takdir».", "التَّقْدِيرُ"),
  TJ("أَحْسِنْ", "خَبَرٌ — الْجُمْلَةُ الْمَحْكِيَّةُ؛ فِعْلُ تَعَجُّبٍ عَلَى صُورَةِ الْأَمْرِ.", "«how beautiful».", "«ne güzel»."),
  cited("أَنْتَ", "anta", "pron", ["fail", "al-mabni-wal-mudmar", "tawkid"], "ضَمِيرٌ مُنْفَصِلٌ — الْفَاعِلُ الْمُقَدَّرُ عِنْدَ الْأَخْفَشِ.", "«you».", "«sen»."),
  bi_("بِزَيْدٍ", "zayd", "propn", [K, "maful-bihi"], "زَيْدٍ مَجْرُورٌ لَفْظًا — مَفْعُولٌ عِنْدَ الْأَخْفَشِ.", "«with Zayd».", "«Zeyd'i».", "زَيْدٍ", punct="."),
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
 "taajjub": need("taajjub", "تَعَجُّب", "ع ج ب", "noun", "wonder, astonishment — the maṣdar of تَعَجَّبَ; the verb of wonder expresses it", "taaccüb, hayret — teaccebe'nin masdarı; taaccüb fiili onu ifade eder", 4),
 "takhir": need("takhir", "تَأْخِير", "أ خ ر", "noun", "delaying, placing later — the maṣdar of أَخَّرَ, the pair of تَقْدِيم", "te'hir, sonraya bırakma — ahhara'nın masdarı, takdîmin eşi", 4),
 "mazini": need("mazini", "الْمَازِنِيّ", "م ز ن", "propn", "Abū ʿUthmān al-Māzinī (d. 249/863) — the Basran grammarian, teacher of al-Mubarrad", "Ebû Osman el-Mâzinî (ö. 249/863) — Basralı nahivci, Müberred'in hocası", 5),
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
print("kafiya ch27 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "فِعْلُ التَّعَجُّبِ فِي الْكَافِيَةِ", "en": "The verb of wonder in the Kafiya: the two forms, what they may be built from, the ban on fronting and separation, and the Sībawayh–Akhfash readings", "tr": "Kâfiye'de taaccüb fiili: iki sîga, nelerden yapılabildiği, takdim ve fasıl yasağı ve Sîbeveyh–Ahfeş okuyuşları"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — فعل التعجب: ما وضع لإنشاء التعجب؛ وله صيغتان: ما أفعله وأفعل به", "ضياء صونغور اوغلى — دفتر الكافية: غير متصرفين؛ لا يبنيان إلا مما يبنى منه أفعل التفضيل؛ أشد وبابه؛ لا تقديم ولا تأخير ولا فصل، والمازني بالظرف والأكثر بكان؛ ما عند سيبويه نكرة وعند الأخفش موصولة؛ به فاعل عند سيبويه ومفعول عند الأخفش"],
 "question": {
  "en": ["What is the verb of wonder for? Not to report — to CREATE wonder as it is spoken (inshāʾ). مَا أَحْسَنَ زَيْدًا does not state that Zayd is beautiful; it exclaims it.",
         "What are its two forms? مَا أَفْعَلَهُ, where the thing wondered at is in naṣb — مَا أَحْسَنَ زَيْدًا — and أَفْعِلْ بِهِ, where it stands after a bāʾ — أَحْسِنْ بِزَيْدٍ. Both are frozen: no muḍāriʿ, no passive. The second looks like an imperative and is not one.",
         "From which verbs? Only from those the elative is built from — a sound triliteral, not a colour, not a defect, not an augmented form. Where the verb is barred, reach for أَشَدّ and hand it the maṣdar: مَا أَشَدَّ اسْتِخْرَاجَهُ، أَشْدِدْ بِاسْتِخْرَاجِهِ.",
         "May the word order move? No. Neither مَا زَيْدًا أَحْسَنَ nor بِزَيْدٍ أَحْسِنْ, and nothing may stand between the verb and its maʿmūl — except, for al-Māzinī, a ẓarf (مَا أَحْسَنَ بِالرَّجُلِ أَنْ يَصْدُقَ), and for most grammarians a redundant كَانَ that dates the wonder (مَا كَانَ أَحْسَنَ زَيْدًا).",
         "What is that مَا? Sībawayh: a complete indefinite meaning «something», the mubtada, with أَحْسَنَ زَيْدًا as its khabar — «something made Zayd beautiful». Al-Akhfash: a relative, mubtada, with a dropped khabar — «what made Zayd beautiful is something great». Two parsings, one meaning.",
         "And the بِهِ of the second form? Sībawayh: the bāʾ-phrase IS the doer and the verb hides no pronoun. Al-Akhfash: it is the object, the bāʾ transitivising or redundant, and the doer is a hidden «you» — أَحْسِنْ أَنْتَ بِزَيْدٍ.",
         "What does the engine do? MaEngine ranks the taʿajjub face on the signal أَفْعَلَ + a manṣūb noun; the TartibEngine lists the verb of wonder among the orders that may not move; the jāmid flag on these forms keeps the paradigm from offering a muḍāriʿ that does not exist."],
  "tr": ["Taaccüb fiili ne içindir? Bildirmek için değil — söylenirken taaccübü YARATMAK (inşâ) için. مَا أَحْسَنَ زَيْدًا Zeyd'in güzel olduğunu bildirmez; bunu haykırır.",
         "İki sîgası nedir? Şaşılan şeyin nasbda olduğu مَا أَفْعَلَهُ — مَا أَحْسَنَ زَيْدًا — ve onun bir bâ'dan sonra durduğu أَفْعِلْ بِهِ — أَحْسِنْ بِزَيْدٍ. İkisi de donmuştur: muzâri yok, meçhul yok. İkincisi emre benzer ve emir değildir.",
         "Hangi fiillerden? Yalnız ism-i tafdîlin yapıldıklarından — sahih sülâsîden; renkten, kusurdan, mezîd bâbdan değil. Fiil mümteni ise أَشَدّ'e uzan ve ona masdarı ver: مَا أَشَدَّ اسْتِخْرَاجَهُ، أَشْدِدْ بِاسْتِخْرَاجِهِ.",
         "Kelime sırası oynayabilir mi? Hayır. Ne مَا زَيْدًا أَحْسَنَ ne بِزَيْدٍ أَحْسِنْ; fiil ile ma'mûlü arasına hiçbir şey giremez — Mâzinî'ye göre bir zarf (مَا أَحْسَنَ بِالرَّجُلِ أَنْ يَصْدُقَ) ve çoğunluğa göre taaccübü tarihleyen zâid bir كَانَ (مَا كَانَ أَحْسَنَ زَيْدًا) hariç.",
         "O مَا nedir? Sîbeveyh: «bir şey» mânâsında tam bir nekre, mübtedâ; أَحْسَنَ زَيْدًا haberi — «bir şey Zeyd'i güzel kıldı». Ahfeş: ism-i mevsûl, mübtedâ, haberi mahzûf — «Zeyd'i güzel kılan büyük bir şeydir». İki i'rab, bir mânâ.",
         "Ya ikinci sîganın بِهِ'si? Sîbeveyh: bâ'lı ibare fâilin KENDİSİDİR, fiil zamir gizlemez. Ahfeş: mef'ûldür, bâ ta'diye edici ya da zâiddir, fâil gizli bir «sen»dir — أَحْسِنْ أَنْتَ بِزَيْدٍ.",
         "Motor ne yapar? MaEngine taaccüb yüzünü أَفْعَلَ + mansûb isim işaretiyle sıralar; TartibEngine taaccüb fiilini yeri oynamayan sıralar arasında listeler; bu sîgalar üzerindeki câmid bayrağı çekimin var olmayan bir muzâri sunmasını önler."]},
 "plain": {
  "en": "The verb of wonder is Arabic's exclamation: «how beautiful Zayd is!» said either as mā aḥsana Zaydan or as aḥsin bi-Zayd. The two shapes never conjugate, never move their words, and can only be made from simple verbs; for the rest you say «how intense is his …» with the maṣdar.",
  "tr": "Taaccüb fiili Arapçanın ünlemidir: «Zeyd ne güzel!» ya mâ ahsene Zeyden ya da ahsin bi-Zeyd diye söylenir. İki kalıp hiç çekimlenmez, kelimelerini oynatmaz ve yalnız basit fiillerden yapılır; gerisi için masdarla «onun ... ne şiddetli» dersin."},
 "explanation": {
  "en": "The definition is the Kafiya's and it names the class by its speech-act: inshāʾ, not khabar — the sentence does not report a state but performs the wonder. The notebook gives the two forms with their stock examples, and the three restrictions that follow are one idea seen three times: the forms are frozen (no tenses, no passive), their word order is frozen (no fronting, no separation), and their lexical base is frozen (only roots that give an elative — a colour, a defect or an augmented verb is barred, and أَشَدّ with the maṣdar supplies what the form cannot). The two licensed separations are given with their holders, al-Māzinī's ẓarf and the majority's كَانَ, the latter a redundant كَانَ that merely dates the wonder, which ties this chapter to كَانَ's fifth face in chapter 25. The parsing dispute is the chapter's crown: Sībawayh takes مَا as a complete indefinite and the verb clause as its khabar, al-Akhfash takes it as a relative with its khabar suppressed, and in the second form the same two readers divide over whether the bāʾ-phrase is the doer itself or an object beside a hidden doer. Both pairs are kept, named, and not adjudicated.",
  "tr": "Tarif Kâfiye'nindir ve sınıfı söz edimiyle adlandırır: haber değil inşâ — cümle bir hâli bildirmez, taaccübü icra eder. Defter iki sîgayı alışılmış örnekleriyle verir; ardından gelen üç kısıtlama üç kez görülen tek fikirdir: sîgalar donmuştur (zaman yok, meçhul yok), kelime sıraları donmuştur (takdim yok, fasıl yok) ve sözlük tabanları donmuştur (yalnız ism-i tafdîl veren kökler — renk, kusur ya da mezîd fiil mümteni; masdarlı أَشَدّ sîganın veremediğini verir). İzin verilen iki fasıl sahipleriyle verilir: Mâzinî'nin zarfı ve çoğunluğun كَانَ'si — ikincisi taaccübü yalnızca tarihleyen zâid bir كَانَ'dir ve bu bâbı yirmi beşinci bâbdaki كَانَ'nin beşinci yüzüne bağlar. İ'rab ihtilâfı bâbın tacıdır: Sîbeveyh مَا'yı tam bir nekre, fiil cümlesini haberi sayar; Ahfeş onu haberi gizlenmiş bir ism-i mevsûl sayar; ikinci sîgada aynı iki okuyucu bâ'lı ibarenin fâilin kendisi mi yoksa gizli bir fâilin yanında mef'ûl mü olduğunda ayrılır. Her iki çift de korunur, adlandırılır ve hüküm verilmez."},
 "examples": [
  {"ar": "فِعْلُ التَّعَجُّبِ: مَا وُضِعَ لِإِنْشَاءِ التَّعَجُّبِ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "مَا أَحْسَنَ زَيْدًا — أَحْسِنْ بِزَيْدٍ", "en": "The two forms.", "tr": "İki sîga.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "مَا أَشَدَّ اسْتِخْرَاجَهُ وَأَشْدِدْ بِاسْتِخْرَاجِهِ", "en": "Reaching the barred verb through ashadd.", "tr": "Mümteni fiile eşedd ile ulaşmak.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "مَا أَحْسَنَ بِالرَّجُلِ أَنْ يَصْدُقَ — مَا كَانَ أَحْسَنَ زَيْدًا", "en": "The two licensed separations.", "tr": "İzin verilen iki fasıl.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "الَّذِي أَحْسَنَ زَيْدًا شَيْءٌ عَظِيمٌ", "en": "Al-Akhfash's paraphrase.", "tr": "Ahfeş'in takdiri.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "أَحْسِنْ أَنْتَ بِزَيْدٍ", "en": "Al-Akhfash's hidden doer.", "tr": "Ahfeş'in gizli fâili.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«مَا زَيْدًا أَحْسَنَ»",
   "right": "«مَا أَحْسَنَ زَيْدًا — taaccüb fiilinde takdim yoktur»",
   "why": {"en": "The maʿmūl may not precede the verb of wonder.", "tr": "Ma'mûl taaccüb fiilinin önüne geçemez."}},
  {"wrong": "«مَا أَحْمَرَ الْوَرْدَ»",
   "right": "«مَا أَشَدَّ حُمْرَةَ الْوَرْدِ — renkten taaccüb fiili yapılmaz»",
   "why": {"en": "Colour and defect roots give no elative and no verb of wonder; ashadd carries the maṣdar.", "tr": "Renk ve kusur kökleri ne ism-i tafdîl ne taaccüb fiili verir; eşedd masdarı taşır."}},
  {"wrong": "«أَحْسِنْ بِزَيْدٍ — Zeyd'e iyilik et!»",
   "right": "«أَحْسِنْ بِزَيْدٍ — Zeyd ne güzel! (emir sûretinde taaccüb)»",
   "why": {"en": "The second form wears the imperative's shape but commands nothing.", "tr": "İkinci sîga emir kalıbını giyer ama hiçbir şey emretmez."}},
  {"wrong": "«يُحْسِنُ بِزَيْدٍ — taaccübün muzârisi»",
   "right": "«taaccüb fiilinin muzârisi ve meçhulü yoktur»",
   "why": {"en": "Both forms are jāmid; the paradigm offers only what exists.", "tr": "İki sîga da câmiddir; çekim yalnız var olanı sunar."}}],
 "relatedNotes": ["ism-al-tafdil-fil-kafiya", "al-afal-al-naqisa-fil-kafiya", "al-amil-wa-aqsamuh", "al-mamul-wa-aqsamuh", "anwa-ma"]}

ADD_EN = (" Chapter 27 (notebook lines ~319-325): the verb of wonder defined in the notebook's own Arabic (s1); the two forms, the restrictions on base, order and separation, and the Sībawayh/al-Akhfash readings — the notebook's exposition, kept as commentary (s2-s7).")
ADD_TR = (" Yirmi yedinci bâb (defter satırları ~319-325): taaccüb fiili defterin kendi Arapçasıyla tarif edilir (s1); iki sîga, taban, sıra ve fasıl kısıtlamaları ve Sîbeveyh/Ahfeş okuyuşları — defterin açıklaması, şerh olarak (s2-s7).")
write_out(27, S, TITLE, ADD_EN, ADD_TR, "319-325", GLOSS_ADD, notes=(NOTE,),
          related=(("ism-al-tafdil-fil-kafiya", [K]), ("anwa-ma", [K])))
report(27, S, GLOSS_ADD, (NOTE,))
