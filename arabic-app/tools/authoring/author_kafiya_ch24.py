# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 24: THE TRANSITIVE AND THE INTRANSITIVE, and THE VERBS OF THE HEART. Both definitions in the notebook's own Arabic
(مَا يَتَوَقَّفُ فَهْمُهُ عَلَى مُتَعَلَّقٍ / مَا لَا يَتَوَقَّفُ); one, two and three objects with the seven three-object verbs and why أَعْلَمَ and
أَرَى are among them; the first object like أَعْطَيْتُ's, the second and third like عَلِمْتُ's; the seven verbs of the heart — three of opinion,
three of knowledge, زَعَمْتُ for either — entering on a nominal sentence to say whether it is known or supposed; their properties: both
objects or neither, ilghāʾ when the verb stands in the middle or at the end, doer and first object as two attached pronouns of one person
(عَلِمْتُنِي مُنْطَلِقًا against ضَرَبْتُ نَفْسِي), and the one-object senses (ظَنَّ as suspicion, عَلِمَ as عَرَفَ, رَأَى as أَبْصَرَ, وَجَدَ as أَصَابَ).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~309-311 of the transcription.

  VERBATIM: s1, s2. COMMENTARY (the notebook): s3-s10 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch24.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-mutaaddi-wa-afal-al-qulub-fil-kafiya"
ZA = "zanna-wa-akhawatuha"
MF = "mafulayn"
TITLE = {"ar": "الْمُتَعَدِّي وَاللَّازِمُ وَأَفْعَالُ الْقُلُوبِ", "en": "The transitive, the intransitive, and the verbs of the heart", "tr": "Müteaddî, lâzım ve ef'âl-i kulûb"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
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
def vlist(items, tags=(), first_tags=("idafa-definiteness",), last_punct=None):
    """a cited list of verbs after نَحْوُ: first in jarr, the rest joined"""
    out = []
    for i, (full, lex, en, tr) in enumerate(items):
        p = last_punct if i == len(items) - 1 else None
        if i == 0: out.append(cited(full, lex, "verb", list(first_tags) + list(tags), "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", en, tr, punct=p))
        else: out.append(cited_wa("وَ" + full, lex, "verb", list(tags), full + " مَعْطُوفٌ.", en, tr, full, punct=p))
    return out
def ILA(n_full, n_lex, n_ar, n_en, n_tr, punct=None, n_tags=()):
    return [W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
            W(n_full, n_lex, "noun", ["huruf-jarr"] + list(n_tags), n_ar, n_en, n_tr, punct=punct)]
def ZAYDAN(): return cited("زَيْدًا", "zayd", "propn", [MF, ZA], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ — الْمُبْتَدَأُ فِي الْأَصْلِ.", "«Zayd» — the first object, once the mubtada.", "«Zeyd'i» — birinci mef'ûl, aslında mübtedâ.")
def QAIMAN(punct=None): return cited("قَائِمًا", "qaim", "noun", [MF, ZA], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — الْخَبَرُ فِي الْأَصْلِ.", "«standing» — the second object, once the khabar.", "«ayakta» — ikinci mef'ûl, aslında haber.", punct=punct)
def MUNTALIQAN(punct=None): return cited("مُنْطَلِقًا", "muntaliq", "noun", [MF, ZA], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«departing».", "«giden».", punct=punct)

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The transitive: that whose understanding depends on something it attaches to — as ضَرَبَ.",
 "tr": "Müteaddî: anlaşılması bir müteallaka (fâilden başka bir şeye) bağlı olan fiildir — ضَرَبَ gibi."},
 "tokens": [
  W("الْمُتَعَدِّي", "mutaaddi", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the transitive».", "«müteaddî».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«that».", "«... olan»."),
  W("يَتَوَقَّفُ", "tawaqqafa", "verb", ["ism-mawsul", "fail", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ صِلَةٌ.", "«depends».", "«bağlı olan»."),
  W("فَهْمُهُ", "fahm", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«its understanding».", "«anlaşılması».", segments=[seg("فَهْمُ", "fahm", "noun"), pr3ms()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("مُتَعَلَّقٍ", "mutaallaq", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ — أَمْرٌ غَيْرُ الْفَاعِلِ.", "«something it attaches to» — other than the doer.", "«bir müteallaka» — fâilden başka bir şey.", punct="،"),
  nahwu(),
  cited("ضَرَبَ", "daraba", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَحْكِيٌّ.", "«he struck».", "«vurdu».", punct="."),
 ]})

# ----------- s2 (VERBATIM)
S.append({"id": "s2", "translation": {
 "en": "And the intransitive: that whose understanding does not depend on something it attaches to — as قَعَدَ.",
 "tr": "Lâzım: anlaşılması bir müteallaka bağlı olmayan fiildir — قَعَدَ gibi."},
 "tokens": [
  atf_wa("وَاللَّازِمُ", "lazim", "noun", ["mubtada-khabar"], "اللَّازِمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the intransitive».", "«ve lâzım».", "اللَّازِمُ", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«that».", "«... olan»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mayan»."),
  W("يَتَوَقَّفُ", "tawaqqafa", "verb", ["ism-mawsul", "fail", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ صِلَةٌ.", "«depends».", "«bağlı»."),
  W("فَهْمُهُ", "fahm", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its understanding».", "«anlaşılması».", segments=[seg("فَهْمُ", "fahm", "noun"), pr3ms()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«-e»."),
  W("مُتَعَلَّقٍ", "mutaallaq", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«something it attaches to».", "«bir müteallaka».", punct="،"),
  nahwu(),
  cited("قَعَدَ", "qaada", "verb", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — فِعْلٌ مَحْكِيٌّ لَازِمٌ.", "«he sat».", "«oturdu».", punct="."),
 ]})

# ----------- s3: one, two, three
S.append({"id": "s3", "translation": {
 "en": "And the transitive is of three kinds: transitive to one object, as ضَرَبَ; to two, as أَعْطَى and عَلِمَ; and to three, as أَعْلَمَ, أَرَى, أَنْبَأَ, نَبَّأَ, أَخْبَرَ, خَبَّرَ and حَدَّثَ." + C_EN,
 "tr": "Müteaddî üç türlüdür: bir mef'ûle müteaddî, ضَرَبَ gibi; iki mef'ûle, أَعْطَى ve عَلِمَ gibi; üç mef'ûle, أَعْلَمَ, أَرَى, أَنْبَأَ, نَبَّأَ, أَخْبَرَ, خَبَّرَ ve حَدَّثَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَالْمُتَعَدِّي", "mutaaddi", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "الْمُتَعَدِّي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the transitive».", "«ve müteaddî».", "الْمُتَعَدِّي"),
  W("عَلَى", "ala", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "حَرْفُ جَرٍّ — خَبَرٌ.", "«is of».", "«... üzeredir»."),
  W("ثَلَاثَةِ", "thalatha", "noun", ["huruf-jarr", "idafa-definiteness", "asma-al-adad-fil-kafiya"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«three».", "«üç»."),
  W("أَضْرُبٍ", "darb", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِلَّةٍ لِضَرْبٍ: نَوْعٍ.", "«kinds» — a plural of paucity.", "«tür» — kıllet cemi.", punct=":"),
  W("مُتَعَدٍّ", "mutaaddi", "noun", ["badal", "ism-maqsur-manqus"], "بَدَلٌ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — مَنْقُوصٌ حُذِفَتْ يَاؤُهُ.", "«transitive» — a manqūṣ, its yāʾ dropped.", "«müteaddî» — mankûs, yâsı düşmüş."),
  *ILA("وَاحِدٍ", "wahid", "مَجْرُورٌ.", "«one».", "«bir»."),
  nahwu(),
  *vlist([("ضَرَبَ", "daraba", "«he struck».", "«vurdu».")], last_punct="،"),
  atf_wa("وَإِلَى", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَمُتَعَدٍّ.", "«and to».", "«ve ... -e».", "إِلَى"),
  W("اثْنَيْنِ", "ithnan", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ.", "«two».", "«iki»."),
  nahwu(),
  *vlist([("أَعْطَى", "ata-give", "«he gave».", "«verdi»."), ("عَلِمَ", "alima", "«he knew».", "«bildi».")], last_punct="،"),
  atf_wa("وَإِلَى", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ.", "«and to».", "«ve ... -e».", "إِلَى"),
  W("ثَلَاثَةٍ", "thalatha", "noun", ["huruf-jarr", "asma-al-adad-fil-kafiya"], "مَجْرُورٌ.", "«three».", "«üç»."),
  nahwu(),
  *vlist([("أَعْلَمَ", "aalama", "«he made known».", "«bildirdi»."), ("أَرَى", "ara", "«he showed».", "«gösterdi»."), ("أَنْبَأَ", "anbaa", "«he informed».", "«haber verdi»."),
          ("نَبَّأَ", "nabbaa", "«he informed».", "«haber verdi»."), ("أَخْبَرَ", "akhbara", "«he told».", "«bildirdi»."), ("خَبَّرَ", "khabbara", "«he told».", "«bildirdi»."), ("حَدَّثَ", "haddatha", "«he related».", "«anlattı».")], last_punct="."),
 ]})

# ----------- s4: why أَعْلَمَ and أَرَى
S.append({"id": "s4", "translation": {
 "en": "And أَعْلَمَ and أَرَى are transitive to three because their triliteral was transitive to two and the hamza added a third; the remaining five are transitive to three when they bear the sense of أَعْلَمَ." + C_EN,
 "tr": "أَعْلَمَ ve أَرَى üç mef'ûle müteaddîdir, çünkü sülâsîleri iki mef'ûle müteaddî idi, hemze üçüncüyü ekledi; kalan beşi أَعْلَمَ mânâsında olduklarında üç mef'ûle müteaddî olur." + C_TR},
 "tokens": [
  cited_wa("وَأَعْلَمَ", "aalama", "verb", ["mubtada-khabar", "form-iv-verbs"], "أَعْلَمَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and aʿlama».", "«ve a'leme».", "أَعْلَمَ"),
  cited_wa("وَأَرَى", "ara", "verb", ["mubtada-khabar", "form-iv-verbs"], "أَرَى مَعْطُوفٌ.", "«and arā».", "«ve erâ».", "أَرَى"),
  W("مُتَعَدِّيَانِ", "mutaaddi", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«are transitive».", "«müteaddîdir»."),
  *ILA("ثَلَاثَةٍ", "thalatha", "مَجْرُورٌ.", "«three».", "«üç».", n_tags=["asma-al-adad-fil-kafiya"]),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("ثُلَاثِيَّهُمَا", "thulathi", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their triliteral».", "«sülâsîleri».", segments=[seg("ثُلَاثِيَّ", "thulathi", "noun"), pr3d()]),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "inna-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«was».", "«idi»."),
  W("مُتَعَدِّيًا", "mutaaddi", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«transitive».", "«müteaddî»."),
  *ILA("اثْنَيْنِ", "ithnan", "مَجْرُورٌ بِالْيَاءِ.", "«two».", "«iki».", n_tags=["al-muthanna"]),
  W("فَزَادَتْهُ", "zada", "verb", ["fail", "maful-bihi", "al-fa-fi-khabar-al-mubtada", "hollow-verbs"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَزَادَتْ فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«and … added to it».", "«ve ona ekledi».", segments=[seg("فَ", "fa", "conj"), seg("زَادَتْ", "zada", "verb"), pr3ms()]),
  W("الْهَمْزَةُ", "hamza-letter", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the hamza».", "«hemze»."),
  W("ثَالِثًا", "thalith", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a third».", "«üçüncüyü».", punct="؛"),
  atf_wa("وَالْخَمْسَةُ", "khamsa", "noun", ["mubtada-khabar", "asma-al-adad-fil-kafiya"], "الْخَمْسَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the five».", "«ve beşi».", "الْخَمْسَةُ"),
  W("الْبَاقِيَةُ", "baqi", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَرْفُوعَةٌ.", "«remaining».", "«kalan»."),
  W("مُتَعَدِّيَةٌ", "mutaaddi", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«are transitive».", "«müteaddîdir»."),
  *ILA("ثَلَاثَةٍ", "thalatha", "مَجْرُورٌ.", "«three».", "«üç».", n_tags=["asma-al-adad-fil-kafiya"]),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«they are».", "«olduklarında»."),
  bi_("بِمَعْنَى", "mana", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ كَانَتْ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("أَعْلَمَ", "aalama", "verb", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«aʿlama».", "«a'leme».", punct="."),
 ]})

# ----------- s5: the three objects' rules
S.append({"id": "s5", "translation": {
 "en": "And the first object of these is like the object of the أَعْطَيْتُ class, while the second and the third are like the two objects of the عَلِمْتُ class." + C_EN,
 "tr": "Bunların birinci mef'ûlü أَعْطَيْتُ bâbının mef'ûlü gibidir; ikinci ve üçüncü mef'ûlleri ise عَلِمْتُ bâbının mef'ûlleri gibidir." + C_TR},
 "tokens": [
  atf_wa("وَالْمَفْعُولُ", "maful-object", "noun", ["mubtada-khabar", MF], "الْمَفْعُولُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the object».", "«ve mef'ûl».", "الْمَفْعُولُ"),
  W("الْأَوَّلُ", "awwal", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«first».", "«birinci»."),
  li_("لِهٰذِهِ", "hadhihi", "pron", ["asma-al-ishara-wal-mawsulat"], "هٰذِهِ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — الْأَفْعَالُ السَّبْعَةُ.", "«of these».", "«bunların».", "هٰذِهِ"),
  W("كَمَفْعُولِ", "maful-object", "noun", ["huruf-jarr", "idafa-definiteness", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَمَفْعُولِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«is like the object of».", "«mef'ûlü gibidir».", segments=[seg("كَ", "ka", "prep"), seg("مَفْعُولِ", "maful-object", "noun")]),
  W("بَابِ", "bab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the class of».", "«bâbının»."),
  cited("أَعْطَيْتُ", "ata-give", "verb", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ، وَالتَّاءُ فَاعِلٌ.", "«I gave».", "«verdim».", punct="،", segments=[seg("أَعْطَيْ", "ata-give", "verb"), prT()]),
  atf_wa("وَالثَّانِي", "thani", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "الثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«while the second».", "«ikinci».", "الثَّانِي"),
  atf_wa("وَالثَّالِثُ", "thalith", "noun", [], "الثَّالِثُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the third».", "«ve üçüncü».", "الثَّالِثُ"),
  W("كَمَفْعُولَيْ", "maful-object", "noun", ["huruf-jarr", "idafa-definiteness", "mubtada-khabar", "al-muthanna"], "الْكَافُ حَرْفُ جَرٍّ، وَمَفْعُولَيْ مَجْرُورٌ بِالْيَاءِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ — خَبَرٌ.", "«are like the two objects of».", "«iki mef'ûlü gibidir».", segments=[seg("كَ", "ka", "prep"), seg("مَفْعُولَيْ", "maful-object", "noun")]),
  W("بَابِ", "bab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the class of».", "«bâbının»."),
  cited("عَلِمْتُ", "alima", "verb", ["idafa-definiteness", ZA], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«I knew».", "«bildim».", punct=".", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
 ]})

# ----------- s6: the verbs of the heart
S.append({"id": "s6", "translation": {
 "en": "And the verbs of the heart: ظَنَنْتُ, حَسِبْتُ and خِلْتُ for opinion; زَعَمْتُ now for knowledge, now for opinion; عَلِمْتُ, رَأَيْتُ and وَجَدْتُ for knowledge. They enter on a nominal sentence to show whether it is from knowledge or opinion — as زَيْدٌ قَائِمٌ, then عَلِمْتُ زَيْدًا قَائِمًا and ظَنَنْتُ زَيْدًا قَائِمًا." + C_EN,
 "tr": "Ef'âl-i kulûb: ظَنَنْتُ, حَسِبْتُ, خِلْتُ zan için; زَعَمْتُ bazen ilim bazen zan için; عَلِمْتُ, رَأَيْتُ, وَجَدْتُ ilim için. İsim cümlesinin ilimden mi zandan mı olduğunu bildirmek için üzerine girerler — زَيْدٌ قَائِمٌ, sonra عَلِمْتُ زَيْدًا قَائِمًا ve ظَنَنْتُ زَيْدًا قَائِمًا gibi." + C_TR},
 "tokens": [
  atf_wa("وَأَفْعَالُ", "fil", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir", ZA], "أَفْعَالُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the verbs of».", "«ve fiilleri».", "أَفْعَالُ"),
  W("الْقُلُوبِ", "qalb", "noun", ["idafa-definiteness", "jam-taksir", ZA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قَلْبٍ.", "«the heart».", "«kalp».", punct=":"),
  cited("ظَنَنْتُ", "zanna", "verb", ["mubtada-khabar", ZA, "doubled-verbs"], "خَبَرٌ — فِعْلٌ مَحْكِيٌّ، وَالتَّاءُ فَاعِلٌ.", "«I supposed».", "«sandım».", segments=[seg("ظَنَنْ", "zanna", "verb"), prT()]),
  cited_wa("وَحَسِبْتُ", "hasiba", "verb", [ZA], "حَسِبْتُ مَعْطُوفٌ.", "«I reckoned».", "«saydım».", "حَسِبْ", extra_segs=[seg("حَسِبْ", "hasiba", "verb"), prT()]),
  cited_wa("وَخِلْتُ", "khala-think", "verb", [ZA, "hollow-verbs"], "خِلْتُ مَعْطُوفٌ.", "«I imagined».", "«zannettim».", "خِلْ", extra_segs=[seg("خِلْ", "khala-think", "verb"), prT()]),
  li_("لِلظَّنِّ", "zann", "noun", [ZA], "الظَّنِّ مَجْرُورٌ.", "«for opinion».", "«zan için».", "الظَّنِّ", punct="؛", segs=[seg("لِ", "li", "prep"), seg("لظَّنِّ", "zann", "noun")]),
  cited_wa("وَزَعَمْتُ", "zaama-claim", "verb", ["mubtada-khabar", ZA], "زَعَمْتُ مُبْتَدَأٌ.", "«and I claimed».", "«ve iddia ettim».", "زَعَمْ", extra_segs=[seg("زَعَمْ", "zaama-claim", "verb"), prT()]),
  li_("لِلْعِلْمِ", "ilm", "noun", ["mubtada-khabar"], "الْعِلْمِ مَجْرُورٌ — خَبَرٌ.", "«for knowledge».", "«ilim için».", "الْعِلْمِ", segs=[seg("لِ", "li", "prep"), seg("لْعِلْمِ", "ilm", "noun")]),
  W("تَارَةً", "tara-time", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«now».", "«bazen»."),
  atf_wa("وَلِلظَّنِّ", "zann", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالظَّنِّ مَجْرُورٌ.", "«now for opinion».", "«bazen zan için».", "لِ", extra_segs=[seg("لِ", "li", "prep"), seg("لظَّنِّ", "zann", "noun")]),
  W("تَارَةً", "tara-time", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«now».", "«bazen».", punct="؛"),
  cited_wa("وَعَلِمْتُ", "alima", "verb", ["mubtada-khabar", ZA], "عَلِمْتُ مُبْتَدَأٌ.", "«and I knew».", "«ve bildim».", "عَلِمْ", extra_segs=[seg("عَلِمْ", "alima", "verb"), prT()]),
  cited_wa("وَرَأَيْتُ", "raa", "verb", [ZA], "رَأَيْتُ مَعْطُوفٌ.", "«I saw (knew)».", "«gördüm».", "رَأَيْ", extra_segs=[seg("رَأَيْ", "raa", "verb"), prT()]),
  cited_wa("وَوَجَدْتُ", "wajada", "verb", [ZA, "mithal-verbs"], "وَجَدْتُ مَعْطُوفٌ.", "«I found».", "«buldum».", "وَجَدْ", extra_segs=[seg("وَجَدْ", "wajada", "verb"), prT()]),
  li_("لِلْعِلْمِ", "ilm", "noun", ["mubtada-khabar"], "الْعِلْمِ مَجْرُورٌ — خَبَرٌ.", "«for knowledge».", "«ilim için».", "الْعِلْمِ", punct="؛", segs=[seg("لِ", "li", "prep"), seg("لْعِلْمِ", "ilm", "noun")]),
  W("تَدْخُلُ", "dakhala", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they enter».", "«girerler»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a sentence».", "«cümlesinin»."),
  W("الِاسْمِيَّةِ", "ismiyya", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«nominal».", "«isim»."),
  li_("لِبَيَانِ", "bayan", "noun", ["idafa-definiteness"], "بَيَانِ مَجْرُورٌ، وَهُوَ مُضَافٌ — لِلتَّعْلِيلِ.", "«to show».", "«bildirmek için».", "بَيَانِ"),
  W("أَنَّهَا", "anna", "part", ["inna-wa-akhawatuha", "idafa-definiteness"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا — وَالْمَصْدَرُ مُضَافٌ إِلَيْهِ.", "«whether it».", "«onun».", segments=[seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("عَنْ", "an", "prep", ["huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«is from».", "«-den»."),
  W("عِلْمٍ", "ilm", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«knowledge».", "«ilim»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("ظَنٍّ", "zann", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«opinion».", "«zan».", punct="،"),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is standing».", "«ayaktadır».", punct="،"),
  cited_wa("وَعَلِمْتُ", "alima", "verb", ["fail", ZA, MF], "عَلِمْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — يَنْصِبُ الْمُبْتَدَأَ وَالْخَبَرَ مَفْعُولَيْنِ.", "«and I knew».", "«ve bildim».", "عَلِمْ", extra_segs=[seg("عَلِمْ", "alima", "verb"), prT()]),
  ZAYDAN(),
  QAIMAN(punct="،"),
  cited_wa("وَظَنَنْتُ", "zanna", "verb", ["fail", ZA, MF, "doubled-verbs"], "ظَنَنْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and I supposed».", "«ve sandım».", "ظَنَنْ", extra_segs=[seg("ظَنَنْ", "zanna", "verb"), prT()]),
  ZAYDAN(),
  QAIMAN(punct="."),
 ]})

# ----------- s7: both objects or neither
S.append({"id": "s7", "translation": {
 "en": "And among their properties: since their two objects are in origin a mubtada and a khabar, when one is mentioned the other must be mentioned — unlike the أَعْطَيْتُ class, where one object may be named and the other dropped." + C_EN,
 "tr": "Hâssalarından: iki mef'ûlü aslında mübtedâ ve haber olduğundan biri zikredilince ötekinin zikri de lâzım gelir — أَعْطَيْتُ bâbının aksine; orada biri zikredilip öteki hazfedilebilir." + C_TR},
 "tokens": [
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and among».", "«ve ... -den».", "مِنْ"),
  W("خَوَاصِّهَا", "khassa", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their properties».", "«hâssalarından».", segments=[seg("خَوَاصِّ", "khassa", "noun"), pr3fs()]),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mubtada-khabar"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that».", "«-mesi»."),
  W("مَفْعُولَيْهَا", "maful-object", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-muthanna", MF], "اسْمُ أَنَّ مَنْصُوبٌ بِالْيَاءِ، وَهَا مُضَافٌ إِلَيْهِ.", "«their two objects».", "«iki mef'ûlü».", segments=[seg("مَفْعُولَيْ", "maful-object", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الْأَصْلِ", "asl", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«origin».", "«aslında»."),
  W("مُبْتَدَأٌ", "mubtada", "noun", ["inna-wa-akhawatuha", "mubtada-khabar"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«are a mubtada».", "«mübtedâ»."),
  atf_wa("وَخَبَرٌ", "khabar", "noun", ["mubtada-khabar"], "خَبَرٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a khabar».", "«ve haberdir».", "خَبَرٌ", punct="،"),
  W("فَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«so when».", "«bu yüzden -ince».", segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")]),
  W("ذُكِرَ", "dhakara", "verb", ["naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is mentioned».", "«zikredilince»."),
  W("أَحَدُهُمَا", "ahad", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them».", "«biri».", segments=[seg("أَحَدُ", "ahad", "noun"), pr3d()]),
  W("لَزِمَ", "lazima", "verb", ["fail", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ — جَوَابُ إِذَا.", "«must be».", "«lâzım gelir»."),
  W("ذِكْرُ", "dhikr", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the mention of».", "«zikri»."),
  W("الْآخَرِ", "akhar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the other».", "«ötekinin».", punct="،"),
  bi_("بِخِلَافِ", "khilaf", "noun", ["idafa-definiteness"], "خِلَافِ مَجْرُورٌ، وَهُوَ مُضَافٌ — حَالٌ.", "«unlike».", "«aksine».", "خِلَافِ"),
  W("بَابِ", "bab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the class of».", "«bâbının»."),
  cited("أَعْطَيْتُ", "ata-give", "verb", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«I gave».", "«verdim».", punct="،", segments=[seg("أَعْطَيْ", "ata-give", "verb"), prT()]),
  W("فَيَجُوزُ", "jaaza", "verb", ["fail", "al-fa-fi-khabar-al-mubtada", "hollow-verbs"], "الْفَاءُ لِلتَّعْلِيلِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«where … may».", "«orada ... câizdir».", segments=[seg("فَ", "fa", "conj"), seg("يَجُوزُ", "jaaza", "verb")]),
  W("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("ذِكْرُ", "dhikr", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«naming».", "«zikri»."),
  W("أَحَدِهِمَا", "ahad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one».", "«birinin».", segments=[seg("أَحَدِ", "ahad", "noun"), pr3d()]),
  atf_wa("وَحَذْفُ", "hadhf", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"], "حَذْفُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and dropping».", "«ve hazfi».", "حَذْفُ"),
  W("الْآخَرِ", "akhar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the other».", "«ötekinin».", punct="."),
 ]})

# ----------- s8: ilghāʾ
S.append({"id": "s8", "translation": {
 "en": "And among them: the permission to cancel their government when they stand in the middle or at the end — as زَيْدٌ عَلِمْتُ قَائِمٌ, also زَيْدًا عَلِمْتُ قَائِمًا; and زَيْدٌ قَائِمٌ عَلِمْتُ, also زَيْدًا قَائِمًا عَلِمْتُ." + C_EN,
 "tr": "Onlardan: ortada veya sonda bulunduklarında amellerinin ilgâsının câiz olması — زَيْدٌ عَلِمْتُ قَائِمٌ, زَيْدًا عَلِمْتُ قَائِمًا da câiz; زَيْدٌ قَائِمٌ عَلِمْتُ, زَيْدًا قَائِمًا عَلِمْتُ da câiz." + C_TR},
 "tokens": [
  atf_wa("وَمِنْهَا", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and among them».", "«ve onlardan».", "مِنْ", extra_segs=[seg("مِنْ", "min", "prep"), pr3fs()], punct=":"),
  W("جَوَازُ", "jawaz", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the permission of».", "«câiz olması»."),
  W("الْإِلْغَاءِ", "ilgha", "noun", ["idafa-definiteness", ZA], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — إِبْطَالُ الْعَمَلِ.", "«cancelling» — of the government.", "«ilgâ» — amelin iptali."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("تَوَسَّطَتْ", "tawassata", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«they stand in the middle».", "«ortada bulunduklarında»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("تَأَخَّرَتْ", "taakhkhara", "verb", ["atf-nasaq", "fail", "form-v-verbs"], "فِعْلٌ مَاضٍ مَعْطُوفٌ.", "«at the end».", "«sonda».", punct="،"),
  nahwu(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ — الْفِعْلُ مُلْغًى.", "«Zayd» — the verb cancelled.", "«Zeyd» — fiil ilgâ edilmiş."),
  cited("عَلِمْتُ", "alima", "verb", [ZA], "فِعْلٌ مَاضٍ مُتَوَسِّطٌ مُلْغًى، وَالتَّاءُ فَاعِلٌ.", "«I knew».", "«bildim».", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«standing».", "«ayakta».", punct="،"),
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and … is also permitted».", "«ve ... da câizdir».", "يَجُوزُ"),
  cited("زَيْدًا", "zayd", "propn", ["fail", MF, ZA], "فَاعِلُ يَجُوزُ — الْجُمْلَةُ الْمَحْكِيَّةُ؛ مَفْعُولٌ أَوَّلُ مُقَدَّمٌ.", "«Zayd» — the first object fronted.", "«Zeyd'i» — öne alınmış birinci mef'ûl."),
  cited("عَلِمْتُ", "alima", "verb", [ZA], "فِعْلٌ مَاضٍ عَامِلٌ، وَالتَّاءُ فَاعِلٌ.", "«I knew».", "«bildim».", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
  QAIMAN(punct="؛"),
  cited_wa("وَزَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "زَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and Zayd».", "«ve Zeyd».", "زَيْدٌ"),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«standing».", "«ayakta»."),
  cited("عَلِمْتُ", "alima", "verb", [ZA], "فِعْلٌ مَاضٍ مُتَأَخِّرٌ مُلْغًى.", "«I knew».", "«bildim».", punct="،", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and also».", "«ve ... da câizdir».", "يَجُوزُ"),
  cited("زَيْدًا", "zayd", "propn", ["fail", MF, ZA], "مَفْعُولٌ أَوَّلُ مُقَدَّمٌ.", "«Zayd».", "«Zeyd'i»."),
  QAIMAN(),
  cited("عَلِمْتُ", "alima", "verb", [ZA], "فِعْلٌ مَاضٍ مُتَأَخِّرٌ عَامِلٌ.", "«I knew».", "«bildim».", punct=".", segments=[seg("عَلِمْ", "alima", "verb"), prT()]),
 ]})

# ----------- s9: two attached pronouns
S.append({"id": "s9", "translation": {
 "en": "And among them: their doer and their first object may be two attached pronouns for one and the same person — عَلِمْتُنِي مُنْطَلِقًا, عَلِمْتَكَ مُنْطَلِقًا, عَلِمَهُ مُنْطَلِقًا — unlike other verbs: one does not say ضَرَبْتُنِي but ضَرَبْتُ نَفْسِي." + C_EN,
 "tr": "Onlardan: fâilleri ile birinci mef'ûlleri aynı kişi için iki bitişik zamir olabilir — عَلِمْتُنِي مُنْطَلِقًا, عَلِمْتَكَ مُنْطَلِقًا, عَلِمَهُ مُنْطَلِقًا — başka fiillerin aksine: ضَرَبْتُنِي denmez, ضَرَبْتُ نَفْسِي denir." + C_TR},
 "tokens": [
  atf_wa("وَمِنْهَا", "min", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "مِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and among them».", "«ve onlardan».", "مِنْ", extra_segs=[seg("مِنْ", "min", "prep"), pr3fs()], punct=":"),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mubtada-khabar"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that».", "«-ması»."),
  W("فَاعِلَهَا", "fail-doer", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their doer».", "«fâilleri».", segments=[seg("فَاعِلَ", "fail-doer", "noun"), pr3fs()]),
  atf_wa("وَمَفْعُولَهَا", "maful-object", "noun", ["idafa-definiteness", MF], "مَفْعُولَ مَعْطُوفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their object».", "«ve mef'ûlleri».", "مَفْعُولَ", extra_segs=[seg("مَفْعُولَ", "maful-object", "noun"), pr3fs()]),
  W("الْأَوَّلَ", "awwal", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«first».", "«birinci»."),
  W("يَكُونَانِ", "kana", "verb", ["kana-wa-akhawatuha", "inna-wa-akhawatuha", "al-muthanna"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ اسْمُهَا — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«may be».", "«olabilir»."),
  W("ضَمِيرَيْنِ", "damir", "noun", ["kana-wa-akhawatuha", "al-muthanna"], "خَبَرُ يَكُونَانِ مَنْصُوبٌ بِالْيَاءِ.", "«two pronouns».", "«iki zamir»."),
  W("مُتَّصِلَيْنِ", "muttasil", "noun", ["naat-sifa", "al-muthanna"], "صِفَةٌ مَنْصُوبَةٌ بِالْيَاءِ.", "«attached».", "«bitişik»."),
  li_("لِشَيْءٍ", "shay", "noun", [], "شَيْءٍ مَجْرُورٌ.", "«for one».", "«bir şey için».", "شَيْءٍ"),
  W("وَاحِدٍ", "wahid", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«and the same».", "«aynı».", punct="،"),
  nahwu(),
  cited("عَلِمْتُنِي", "alima", "verb", ["fail", MF, ZA], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ أَوَّلُ — لِلْمُتَكَلِّمِ مَعًا.", "«I knew myself».", "«kendimi bildim».", segments=[seg("عَلِمْ", "alima", "verb"), prT(), pr1s()]),
  MUNTALIQAN(punct="،"),
  cited("عَلِمْتَكَ", "alima", "verb", ["fail", MF, ZA], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ أَوَّلُ — لِلْمُخَاطَبِ مَعًا.", "«you knew yourself».", "«kendini bildin».", segments=[seg("عَلِمْ", "alima", "verb"), seg("تَ", "pron-2ms", "pron"), pr2ms()]),
  MUNTALIQAN(punct="،"),
  cited("عَلِمَهُ", "alima", "verb", ["fail", MF, ZA], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ — لِلْغَائِبِ مَعًا.", "«he knew himself».", "«kendini bildi».", segments=[seg("عَلِمَ", "alima", "verb"), pr3ms()]),
  MUNTALIQAN(punct="،"),
  bi_("بِخِلَافِ", "khilaf", "noun", ["idafa-definiteness"], "خِلَافِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«unlike».", "«aksine».", "خِلَافِ"),
  W("غَيْرِهَا", "ghayr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«other verbs».", "«başkalarının».", punct="؛", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3fs()]),
  W("فَلَا", "la-nafiya", "part", ["la-nafiya", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«bu yüzden -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«does one say».", "«denir»."),
  cited("ضَرَبْتُنِي", "daraba", "verb", ["fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْيَاءُ مَفْعُولٌ بِهِ — مَمْنُوعٌ.", "«I struck me» — barred.", "«beni vurdum» — memnû.", segments=[seg("ضَرَبْ", "daraba", "verb"), prT(), pr1s()]),
  W("بَلْ", "bal", "part", ["atf-nasaq"], "حَرْفُ إِضْرَابٍ.", "«but».", "«bilakis»."),
  cited("ضَرَبْتُ", "daraba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck».", "«vurdum».", segments=[seg("ضَرَبْ", "daraba", "verb"), prT()]),
  cited("نَفْسِي", "nafs", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«myself».", "«kendimi».", punct=".", segments=[seg("نَفْسِ", "nafs", "noun"), seg("ي", "pron-1s", "pron")]),
 ]})

# ----------- s10: the one-object senses
S.append({"id": "s10", "translation": {
 "en": "And some of them have another sense, near the first, by which they are transitive to one object: ظَنَنْتُ in the sense of suspicion, عَلِمْتُ in the sense of عَرَفْتُ, رَأَيْتُ in the sense of أَبْصَرْتُ, وَجَدْتُ in the sense of أَصَبْتُ." + C_EN,
 "tr": "Bazılarının birinci mânâya yakın başka bir mânâsı vardır ve o zaman bir mef'ûle müteaddî olurlar: ظَنَنْتُ ittihâm mânâsında, عَلِمْتُ عَرَفْتُ mânâsında, رَأَيْتُ أَبْصَرْتُ mânâsında, وَجَدْتُ أَصَبْتُ mânâsında." + C_TR},
 "tokens": [
  atf_wa("وَلِبَعْضِهَا", "bad", "noun", ["huruf-jarr", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "اللَّامُ حَرْفُ جَرٍّ، وَبَعْضِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«and some of them have».", "«ve bazılarının ... vardır».", "لِ", extra_segs=[seg("لِ", "li", "prep"), seg("بَعْضِ", "bad", "noun"), pr3fs()]),
  W("مَعْنًى", "mana", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«a sense».", "«bir mânâ»."),
  W("آخَرُ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "صِفَةٌ مَرْفُوعَةٌ.", "«another».", "«başka»."),
  W("قَرِيبٌ", "qarib", "noun", ["naat-sifa"], "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ.", "«near».", "«yakın»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْأَوَّلِ", "awwal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the first».", "«birinciye».", punct="،"),
  W("تَتَعَدَّى", "taadda", "verb", ["fail", "form-v-verbs", "ism-maqsur-manqus"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«they are transitive».", "«müteaddî olurlar»."),
  bi_("بِهِ", "bi", "prep", [], "الْهَاءُ مَجْرُورٌ — بِذَلِكَ الْمَعْنَى.", "«by it».", "«onunla».", "هِ", segs=[seg("بِ", "bi", "prep"), pr3msi()]),
  *ILA("وَاحِدٍ", "wahid", "مَجْرُورٌ.", "«one».", "«bir».", punct=":"),
  cited("ظَنَنْتُ", "zanna", "verb", ["mubtada-khabar", ZA, "doubled-verbs"], "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«ẓanantu».", "«zanentü».", segments=[seg("ظَنَنْ", "zanna", "verb"), prT()]),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  W("الِاتِّهَامِ", "ittiham", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«suspicion».", "«ittihâm».", punct="،"),
  cited_wa("وَعَلِمْتُ", "alima", "verb", ["mubtada-khabar", ZA], "عَلِمْتُ مُبْتَدَأٌ.", "«and ʿalimtu».", "«ve alimtü».", "عَلِمْ", extra_segs=[seg("عَلِمْ", "alima", "verb"), prT()]),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("عَرَفْتُ", "arafa", "verb", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«I recognised».", "«tanıdım».", punct="،", segments=[seg("عَرَفْ", "arafa", "verb"), prT()]),
  cited_wa("وَرَأَيْتُ", "raa", "verb", ["mubtada-khabar", ZA], "رَأَيْتُ مُبْتَدَأٌ.", "«and raʾaytu».", "«ve raeytü».", "رَأَيْ", extra_segs=[seg("رَأَيْ", "raa", "verb"), prT()]),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("أَبْصَرْتُ", "absara", "verb", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«I saw with the eye».", "«gözle gördüm».", punct="،", segments=[seg("أَبْصَرْ", "absara", "verb"), prT()]),
  cited_wa("وَوَجَدْتُ", "wajada", "verb", ["mubtada-khabar", ZA, "mithal-verbs"], "وَجَدْتُ مُبْتَدَأٌ.", "«and wajadtu».", "«ve vecedtü».", "وَجَدْ", extra_segs=[seg("وَجَدْ", "wajada", "verb"), prT()]),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ — خَبَرٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("أَصَبْتُ", "asaba", "verb", ["idafa-definiteness", "form-iv-verbs", "hollow-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ، حُذِفَتْ عَيْنُهُ.", "«I came upon».", "«rastladım».", punct=".", segments=[seg("أَصَبْ", "asaba", "verb"), prT()]),
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
 "khabbara": need("khabbara", "خَبَّرَ", "خ ب ر", "verb", "to tell, to inform (Form II) — transitive to three objects in the sense of أَعْلَمَ", "bildirmek, haber vermek (II. bâb) — أَعْلَمَ mânâsında üç mef'ûle müteaddî", 4),
 "taadda": need("taadda", "تَعَدَّى", "ع د و", "verb", "to pass over to, to be transitive to (Form V)", "geçmek, müteaddî olmak (V. bâb)", 4),
 "ittiham": need("ittiham", "اِتِّهَام", "و ه م", "noun", "suspicion, accusing — the one-object sense of ظَنَّ", "ittihâm, suçlama — ظَنَّ'nin tek mef'ûllü mânâsı", 5),
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
put_morph(mo, "khabbara", _nfc(_sg.derived(_sg.B2, _sg.W2, "ُ", "خَبَّر", "خَبِّر", "خَبِّر", "تَخْبِير", "مُخَبِّر", "مُخَبَّر", "خُبِّرَ", "يُخَبَّرُ", "خَبَّرَهُ بِالْأَمْرِ يُخَبِّرُهُ تَخْبِيرًا: أَخْبَرَهُ — الْبَابُ الثَّانِي.")))
put_morph(mo, "taadda", _nfc(_sg.derived_naqis(_sg.B5 + " — نَاقِصٌ", _sg.W5, "َ", "تَعَدَّ", "تَعَدّ", "a", "تَعَدّ", "تَعَدٍّ", "مُتَعَدٍّ", "مُتَعَدًّى", "تُعُدِّيَ", "يُتَعَدَّى", "تَعَدَّى الْفِعْلُ إِلَى الْمَفْعُولِ يَتَعَدَّى تَعَدِّيًا: جَاوَزَ فَاعِلَهُ إِلَيْهِ — الْبَابُ الْخَامِسُ، نَاقِصٌ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch24 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْمُتَعَدِّي وَاللَّازِمُ وَأَفْعَالُ الْقُلُوبِ فِي الْكَافِيَةِ", "en": "Transitive against intransitive by the test of understanding; one, two and three objects; and the verbs of the heart with their four properties", "tr": "Anlaşılma ölçütüyle müteaddî ile lâzım; bir, iki ve üç mef'ûl; ve dört hâssasıyla ef'âl-i kulûb"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المتعدي: ما يتوقف فهمه على متعلق؛ اللازم: ما لا يتوقف؛ أفعال القلوب وخواصها: الإلغاء، اتحاد الفاعل والمفعول ضميرين", "ضياء صونغور اوغلى — دفتر الكافية: ضرب، أعطى وعلم، أعلم وأرى وأنبأ ونبأ وأخبر وخبر وحدث؛ زيادة الهمزة؛ الأول كمفعول أعطيت والآخران كمفعولي علمت؛ ظننت حسبت خلت زعمت علمت رأيت وجدت؛ لزوم ذكر المفعولين؛ الإلغاء توسطا وتأخرا؛ علمتني منطلقا لا ضربتني؛ المعاني الأخرى"],
 "question": {
  "en": ["How do you tell a TRANSITIVE verb from an intransitive one? By whether understanding it needs something beyond the doer: ضَرَبَ leaves you asking «whom?», قَعَدَ does not. The Kafiya's test is semantic, which is why the glossary stores transitivity and the engine reads it rather than guessing from shape.",
         "How many objects? One (ضَرَبَ), two (أَعْطَى، عَلِمَ) or three (أَعْلَمَ، أَرَى، أَنْبَأَ، نَبَّأَ، أَخْبَرَ، خَبَّرَ، حَدَّثَ). أَعْلَمَ and أَرَى reach three because the hamza was added to a two-object verb; the other five reach three only when they mean أَعْلَمَ. The first of the three behaves like أَعْطَيْتُ's object, the second and third like عَلِمْتُ's pair.",
         "What are the VERBS OF THE HEART? Seven: three of opinion (ظَنَّ، حَسِبَ، خَالَ), three of knowledge (عَلِمَ، رَأَى، وَجَدَ), and زَعَمَ for either. They sit on a nominal sentence and say which it is: زَيْدٌ قَائِمٌ is a fact; عَلِمْتُ زَيْدًا قَائِمًا is that fact known; ظَنَنْتُ زَيْدًا قَائِمًا is it supposed.",
         "Why can neither object be dropped alone? Because the two objects were a mubtada and a khabar, and a sentence cannot lose half of itself; name both or neither. أَعْطَيْتُ's objects are independent and either may go.",
         "What is ILGHĀʾ? Cancelling the verb's government when it stands in the middle or at the end: زَيْدٌ عَلِمْتُ قَائِمٌ, زَيْدٌ قَائِمٌ عَلِمْتُ — permitted beside the governed versions. The sentence was whole before the verb arrived, so a verb that is not in front may be treated as a parenthesis.",
         "What is the two-pronoun licence? A verb of the heart may have doer and first object as two attached pronouns of one person — عَلِمْتُنِي مُنْطَلِقًا, «I knew myself departing» — because the first object is really a mubtada about the doer. Any other verb must say ضَرَبْتُ نَفْسِي; ضَرَبْتُنِي is barred.",
         "When do they take ONE object? When they shift sense: ظَنَّ as suspecting, عَلِمَ as recognising (عَرَفَ), رَأَى as seeing with the eye (أَبْصَرَ), وَجَدَ as coming upon (أَصَابَ). The analyzer's zanna-expectation must therefore be a shortlist — two objects first, the one-object sense underneath."],
  "tr": ["MÜTEADDÎ fiil lâzımdan nasıl ayrılır? Anlaşılmasının fâilden öte bir şeye muhtaç olup olmadığıyla: ضَرَبَ «kimi?» sorusunu bırakır, قَعَدَ bırakmaz. Kâfiye'nin ölçütü mânâya dairdir; sözlüğün müteaddîliği saklayıp motorun biçimden tahmin etmek yerine onu okumasının sebebi budur.",
         "Kaç mef'ûl? Bir (ضَرَبَ), iki (أَعْطَى، عَلِمَ) ya da üç (أَعْلَمَ، أَرَى، أَنْبَأَ، نَبَّأَ، أَخْبَرَ، خَبَّرَ، حَدَّثَ). أَعْلَمَ ve أَرَى üçe ulaşır, çünkü hemze iki mef'ûllü bir fiile eklenmiştir; öteki beşi yalnız أَعْلَمَ anlamındayken üçe ulaşır. Üçün birincisi أَعْطَيْتُ'nün mef'ûlü gibi, ikinci ve üçüncüsü عَلِمْتُ'nün çifti gibi davranır.",
         "EF'ÂL-İ KULÛB nelerdir? Yedi: üçü zan (ظَنَّ، حَسِبَ، خَالَ), üçü ilim (عَلِمَ، رَأَى، وَجَدَ), زَعَمَ ikisi için. Bir isim cümlesinin üzerine oturup hangisi olduğunu söylerler: زَيْدٌ قَائِمٌ bir olgudur; عَلِمْتُ زَيْدًا قَائِمًا o olgunun bilinmesi; ظَنَنْتُ زَيْدًا قَائِمًا sanılması.",
         "Neden mef'ûllerden biri tek başına düşürülemez? Çünkü iki mef'ûl mübtedâ ve haberdi ve bir cümle yarısını kaybedemez; ya ikisi de söylenir ya hiçbiri. أَعْطَيْتُ'nün mef'ûlleri bağımsızdır, biri gidebilir.",
         "İLGÂ nedir? Fiil ortada ya da sonda durduğunda amelinin iptali: زَيْدٌ عَلِمْتُ قَائِمٌ, زَيْدٌ قَائِمٌ عَلِمْتُ — amel eden biçimlerin yanında câiz. Cümle fiil gelmeden önce bütündü; önde olmayan bir fiil cümle-i mu'terize sayılabilir.",
         "İki zamir ruhsatı nedir? Bir kalp fiilinin fâili ile birinci mef'ûlü aynı kişi için iki bitişik zamir olabilir — عَلِمْتُنِي مُنْطَلِقًا, «kendimi giderken bildim» — çünkü birinci mef'ûl gerçekte fâil hakkında bir mübtedâdır. Başka her fiil ضَرَبْتُ نَفْسِي demelidir; ضَرَبْتُنِي memnûdur.",
         "Ne zaman TEK mef'ûl alırlar? Mânâ kaydığında: ظَنَّ suçlamak, عَلِمَ tanımak (عَرَفَ), رَأَى gözle görmek (أَبْصَرَ), وَجَدَ rastlamak (أَصَابَ). Bu yüzden analizörün zanne-beklentisi bir kısa liste olmalıdır — önce iki mef'ûl, altında tek mef'ûllü mânâ."]},
 "plain": {
  "en": "A verb is transitive if it cannot be understood without an object (ضَرَبَ «he struck» — whom?). Some take two objects, a few three. The verbs of the heart (think, know, find) take a whole «X is Y» sentence as their two objects: both are said or neither, and the verb may be switched off when it is not first.",
  "tr": "Bir fiil mef'ûlsüz anlaşılamıyorsa müteaddîdir (ضَرَبَ «vurdu» — kimi?). Bazı fiiller iki, birkaçı üç mef'ûl alır. Kalp fiilleri (sanmak, bilmek, bulmak…) bütün bir «X, Y'dir» cümlesini iki mef'ûl olarak alır; bu yüzden ikisi de söylenir ya da hiçbiri, ve fiil ortada ya da sonda gelince ameli kapatılabilir."},
 "explanation": {
  "en": "The Kafiya defines transitivity by understanding, not by form: a verb is transitive when its sense is incomplete without something beyond the doer. The notebook then builds the ladder of objects — one, two, three — and explains the seven three-object verbs by their history: أَعْلَمَ and أَرَى are عَلِمَ and رَأَى with a causative hamza, which adds an object to the two they already had; the other five join the list only when they mean the same thing. The first of three objects is a plain object like أَعْطَيْتُ's; the second and third are the old mubtada and khabar, which is what the verbs of the heart govern directly. Those seven verbs are the chapter's real subject. They take a nominal sentence and colour it — known or supposed — and every property the notebook lists follows from the fact that their two objects were once a sentence: both must be present because a sentence has two halves; the verb may be cancelled when it does not come first, because the sentence stood before it arrived; the doer and the first object may be the same person in two attached pronouns, because the first object is a mubtada about that person, whereas ضَرَبْتُنِي would make one person both striker and struck in a single act. The last sentence records the senses in which four of them take a single object — suspicion, recognition, sight, finding — and for the analyzer that list is the reason a verb of the heart yields a shortlist rather than a verdict.",
  "tr": "Kâfiye müteaddîliği biçimle değil anlaşılmayla tarif eder: bir fiil, mânâsı fâilden öte bir şey olmadan eksikse müteaddîdir. Defter sonra mef'ûl merdivenini kurar — bir, iki, üç — ve yedi üç mef'ûllü fiili tarihçeleriyle açıklar: أَعْلَمَ ve أَرَى, zaten iki mef'ûlü olan عَلِمَ ve رَأَى'ya ettirgen hemzenin bir mef'ûl eklemesidir; öteki beşi yalnız aynı anlama geldiklerinde listeye katılır. Üç mef'ûlün birincisi أَعْطَيْتُ'nünki gibi düz bir mef'ûldür; ikinci ve üçüncüsü eski mübtedâ ve haberdir — kalp fiillerinin doğrudan yönettiği şey. O yedi fiil bâbın asıl konusudur. Bir isim cümlesini alıp renklendirirler — bilinen ya da sanılan — ve defterin saydığı her hâssa iki mef'ûllerinin bir zamanlar cümle olmasından çıkar: ikisi de bulunmalıdır, çünkü cümlenin iki yarısı vardır; fiil önde gelmediğinde ilgâ edilebilir, çünkü cümle o gelmeden önce ayaktaydı; fâil ile birinci mef'ûl iki bitişik zamirde aynı kişi olabilir, çünkü birinci mef'ûl o kişi hakkında bir mübtedâdır; oysa ضَرَبْتُنِي tek bir fiilde bir kişiyi hem vuran hem vurulan yapardı. Son cümle dördünün tek mef'ûl aldığı mânâları kaydeder — suçlama, tanıma, görme, rastlama — ve analizör için bu liste, bir kalp fiilinin hüküm değil kısa liste vermesinin sebebidir."},
 "examples": [
  {"ar": "الْمُتَعَدِّي: مَا يَتَوَقَّفُ فَهْمُهُ عَلَى مُتَعَلَّقٍ — وَاللَّازِمُ: مَا لَا يَتَوَقَّفُ", "en": "The two definitions.", "tr": "İki tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "أَعْلَمَ وَأَرَى وَأَنْبَأَ وَنَبَّأَ وَأَخْبَرَ وَخَبَّرَ وَحَدَّثَ", "en": "The seven three-object verbs.", "tr": "Yedi üç mef'ûllü fiil.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "عَلِمْتُ زَيْدًا قَائِمًا — ظَنَنْتُ زَيْدًا قَائِمًا", "en": "Knowledge and opinion on one sentence.", "tr": "Bir cümle üzerinde ilim ve zan.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "زَيْدٌ عَلِمْتُ قَائِمٌ — زَيْدٌ قَائِمٌ عَلِمْتُ", "en": "Ilghāʾ in the middle and at the end.", "tr": "Ortada ve sonda ilgâ.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "عَلِمْتُنِي مُنْطَلِقًا — لَا ضَرَبْتُنِي بَلْ ضَرَبْتُ نَفْسِي", "en": "The two-pronoun licence.", "tr": "İki zamir ruhsatı.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "رَأَيْتُ بِمَعْنَى أَبْصَرْتُ، وَوَجَدْتُ بِمَعْنَى أَصَبْتُ", "en": "The one-object senses.", "tr": "Tek mef'ûllü mânâlar.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«عَلِمْتُ زَيْدًا — tek mef'ûlle, «Zeyd'in ayakta olduğunu bildim» anlamında»",
   "right": "«عَلِمْتُ زَيْدًا قَائِمًا — kalp fiilinin iki mef'ûlü birlikte söylenir; tek mef'ûllü عَلِمْتُ زَيْدًا «Zeyd'i tanıdım» demektir»",
   "why": {"en": "The two objects are a sentence; dropping one leaves half a sentence or shifts the verb to its one-object sense.", "tr": "İki mef'ûl bir cümledir; birini düşürmek yarım cümle bırakır ya da fiili tek mef'ûllü mânâsına kaydırır."}},
  {"wrong": "«عَلِمْتُ زَيْدٌ قَائِمٌ»",
   "right": "«عَلِمْتُ زَيْدًا قَائِمًا — fiil önde gelince ilgâ câiz değildir»",
   "why": {"en": "Ilghāʾ is licensed only in the middle or at the end.", "tr": "İlgâ yalnız ortada ya da sonda câizdir."}},
  {"wrong": "«ضَرَبْتُنِي»",
   "right": "«ضَرَبْتُ نَفْسِي — iki bitişik zamir ruhsatı yalnız kalp fiillerine aittir»",
   "why": {"en": "Only where the first object is really a mubtada about the doer can doer and object be one person.", "tr": "Yalnız birinci mef'ûl gerçekte fâil hakkında mübtedâ olduğunda fâil ile mef'ûl aynı kişi olabilir."}},
  {"wrong": "«أَخْبَرَ her zaman üç mef'ûle müteaddîdir»",
   "right": "«أَخْبَرَ, أَعْلَمَ mânâsındayken üç mef'ûl alır; yoksa bir mef'ûl ve bir câr-mecrûr»",
   "why": {"en": "Only أَعْلَمَ and أَرَى are three-object verbs by form; the other five by sense.", "tr": "Yalnız أَعْلَمَ ve أَرَى biçimce üç mef'ûllüdür; öteki beşi mânâca."}}],
 "relatedNotes": [ZA, MF, "fail", "maful-bihi", "al-fil-wal-madi-wal-mudari-fil-kafiya", "al-majhul-fil-kafiya"]}

ADD_EN = (" Chapter 24 (notebook lines ~309-311): the transitive and the intransitive defined in the notebook's own Arabic (s1-s2); one, two and three objects with the seven three-object verbs, the verbs of the heart with their four properties and their one-object senses — the notebook's exposition, kept as commentary (s3-s10).")
ADD_TR = (" Yirmi dördüncü bâb (defter satırları ~309-311): müteaddî ve lâzım defterin kendi Arapçasıyla tarif edilir (s1-s2); bir, iki ve üç mef'ûl, yedi üç mef'ûllü fiil, dört hâssası ve tek mef'ûllü mânâlarıyla ef'âl-i kulûb — defterin açıklaması, şerh olarak (s3-s10).")
write_out(24, S, TITLE, ADD_EN, ADD_TR, "309-311", GLOSS_ADD, notes=(NOTE,),
          related=((ZA, [K]), (MF, [K])))
report(24, S, GLOSS_ADD, (NOTE,))
