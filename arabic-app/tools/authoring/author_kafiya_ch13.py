# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 13: THE PLURAL — THE SOUND MASCULINE AND THE SOUND FEMININE. The plural defined (the notebook's Arabic) with the
three ways the singular changes (commentary); تَمْر and رَكْب outside it, فُلْك inside it by estimation; sound against broken; the sound
masculine plural defined (the notebook's Arabic), قَاضُونَ and مُصْطَفَوْنَ, its conditions for a noun and for a description, the nun in
annexation, سِنُونَ and أَرَضُونَ against the rule; the sound feminine plural defined (the notebook's Arabic) with its conditions.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~222-229 of the transcription.

  VERBATIM from the notebook's Arabic: s1, s5, s10 (the three definitions) and every example.
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s3, s4, s6, s7, s8, s9, s11.
  COMMENTARY (the notebook's explanation): s2 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch13.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-jam-al-salim-fil-kafiya"
JM = "jam-mudhakkar-salim"
JF = "jam-muannath-salim"
JK = "jam-taksir"
TITLE = {"ar": "الْمَجْمُوعُ وَالْجَمْعُ الصَّحِيحُ", "en": "The plural: the sound masculine and the sound feminine", "tr": "Cemi: sâlim müzekker ve sâlim müennes"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
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
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=[seg("كَ", "ka", "prep"), seg(inner, lex, pos)])
def la_wa(full, lex, pos, tags, ar, en, tr, inner, punct=None):
    return W(full, lex, pos, ["atf-nasaq", "la-nafiya"] + tags, "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ، وَ" + ar, en, tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part")])

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The plural: what points to intended units by the letters of its singular, with some change.",
 "tr": "Cemi: bir değişiklikle, müfredinin harfleriyle kastedilen fertlere delâlet edendir."},
 "tokens": [
  W("الْمَجْمُوعُ", "majmu", "noun", ["mubtada-khabar", JK, "ism-maful"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the plural» — the mubtada.", "«cemi» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("دَلَّ", "dalla", "verb", ["ism-mawsul", "fail", "doubled-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«points» — the ṣila.", "«delâlet eden» — sıla."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("آحَادٍ", "aahad", "noun", ["huruf-jarr", JK], "مَجْرُورٌ بِالْكَسْرَةِ.", "«units».", "«fertlere»."),
  W("مَقْصُودَةٍ", "maqsud", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«intended».", "«kastedilen»."),
  W("بِحُرُوفِ", "harf", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَحُرُوفِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by the letters of».", "«harfleriyle».", segments=[seg("بِ", "bi", "prep"), seg("حُرُوفِ", "harf", "noun")]),
  W("مُفْرَدِهِ", "mufrad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its singular».", "«müfredinin».", segments=[seg("مُفْرَدِ", "mufrad", "noun"), pr3msi()]),
  W("بِتَغَيُّرٍ", "taghayyur", "noun", ["huruf-jarr", "masdar", "form-v-verbs"], "الْبَاءُ حَرْفُ جَرٍّ، وَتَغَيُّرٍ مَجْرُورٌ.", "«with a change».", "«bir değişiklikle».", segments=[seg("بِ", "bi", "prep"), seg("تَغَيُّرٍ", "taghayyur", "noun")]),
  W("مَا", "ma-sifa", "pron", ["naat-sifa", "anwa-ma"], "مَا الْإِبْهَامِيَّةُ، صِفَةٌ لِتَغَيُّرٍ — أَيْ: تَغَيُّرٍ مَا.", "«some» — the vague مَا as an adjective.", "«bir» — sıfat olan ibhâm mâ'sı.", punct="."),
 ]})

# ----------- s2 (COMMENTARY): the three changes
S.append({"id": "s2", "translation": {
 "en": "And the change is by addition, as in رِجَالٌ; or by removal, as in كُتُبٌ; or by a change of vowel and sukūn, as in أُسْدٌ." + C_EN,
 "tr": "Değişiklik ya رِجَالٌ'de olduğu gibi ziyâde ile, ya كُتُبٌ'de olduğu gibi noksan ile, ya da أُسْدٌ'de olduğu gibi hareke ve sükûnun değişmesiyledir." + C_TR},
 "tokens": [
  atf_wa("وَالتَّغَيُّرُ", "taghayyur", "noun", ["mubtada-khabar"], "التَّغَيُّرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the change» — the mubtada.", "«ve değişiklik» — mübtedâ.", "التَّغَيُّرُ"),
  W("بِالزِّيَادَةِ", "ziyada", "noun", ["huruf-jarr", "mubtada-khabar"], "الْبَاءُ حَرْفُ جَرٍّ، وَالزِّيَادَةِ مَجْرُورٌ؛ خَبَرٌ.", "«by addition» — the khabar.", "«ziyâde ile» — haber.", segments=[seg("بِ", "bi", "prep"), seg("الزِّيَادَةِ", "ziyada", "noun")]),
  ka_("كَرِجَالٍ", "rajul", "noun", [JK], "رِجَالٍ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — زِيدَتِ الْأَلِفُ.", "«as in رِجَال» — an alif added.", "«ricâl gibi» — elif eklenmiş.", "رِجَالٍ", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("بِالنُّقْصَانِ", "nuqsan", "noun", ["huruf-jarr", "atf-nasaq"], "الْبَاءُ حَرْفُ جَرٍّ، وَالنُّقْصَانِ مَجْرُورٌ.", "«by removal».", "«noksan ile».", segments=[seg("بِ", "bi", "prep"), seg("النُّقْصَانِ", "nuqsan", "noun")]),
  ka_("كَكُتُبٍ", "kitab", "noun", [JK], "كُتُبٍ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — حُذِفَتِ الْأَلِفُ.", "«as in كُتُب» — the alif removed.", "«kütüb gibi» — elif atılmış.", "كُتُبٍ", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("بِتَغَيُّرِ", "taghayyur", "noun", ["huruf-jarr", "atf-nasaq", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَتَغَيُّرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by a change of».", "«değişmesiyle».", segments=[seg("بِ", "bi", "prep"), seg("تَغَيُّرِ", "taghayyur", "noun")]),
  W("الْحَرَكَةِ", "haraka", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the vowel».", "«hareke»."),
  atf_wa("وَالسُّكُونِ", "sukun", "noun", [], "السُّكُونِ مَعْطُوفٌ مَجْرُورٌ.", "«and the sukūn».", "«ve sükûnun».", "السُّكُونِ"),
  ka_("كَأُسْدٍ", "asad", "noun", [JK], "أُسْدٍ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — أَسَدٌ بِتَغَيُّرِ الْحَرَكَاتِ.", "«as in أُسْد» — أَسَد with its vowels changed.", "«üsd gibi» — harekeleri değişmiş esed.", "أُسْدٍ", punct="."),
 ]})

# ----------- s3 (RESTORED): tamr, rakb, fulk
S.append({"id": "s3", "translation": {
 "en": "And تَمْرٌ and رَكْبٌ are not plurals by the soundest view; and فُلْكٌ is a plural, because its change is estimated." + R_EN,
 "tr": "En sahih görüşe göre تَمْرٌ ve رَكْبٌ cemi değildir; فُلْكٌ ise cemidir, çünkü değişmesi takdîrîdir." + R_TR},
 "tokens": [
  cited_wa("وَتَمْرٌ", "tamr", "noun", ["mubtada-khabar", JK], "تَمْرٌ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ جِنْسٍ.", "«and تَمْر» — a generic noun.", "«ve temr» — cins ismi.", "تَمْرٌ"),
  cited_wa("وَرَكْبٌ", "rakb", "noun", [JK], "رَكْبٌ مَعْطُوفٌ — اسْمُ جَمْعٍ.", "«and رَكْب» — a collective.", "«ve rekb» — ism-i cem'.", "رَكْبٌ"),
  W("لَيْسَا", "laysa", "verb", ["kana-wa-akhawatuha", "al-muthanna"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالْأَلِفُ اسْمُهُ.", "«are not» — the alif its ism.", "«değildir» — elif ismi."),
  W("بِجَمْعٍ", "jam", "noun", ["huruf-jarr", "kana-wa-akhawatuha"], "الْبَاءُ زَائِدَةٌ، وَجَمْعٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.", "«plurals» — the khabar of لَيْسَ behind an extra bāʾ.", "«cemi» — zâid bâ ardında leyse'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("جَمْعٍ", "jam", "noun")]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«by».", "«... göre»."),
  W("الْأَصَحِّ", "asahh", "noun", ["huruf-jarr", "ism-tafdil"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the soundest view».", "«en sahih görüşe».", punct="،"),
  cited_wa("وَفُلْكٌ", "fulk", "noun", ["mubtada-khabar", JK], "فُلْكٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«and فُلْك» — the mubtada.", "«ve fülk» — mübtedâ.", "فُلْكٌ"),
  W("جَمْعٌ", "jam", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a plural».", "«cemidir».", punct="،"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("تَغَيُّرَهُ", "taghayyur", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its change».", "«değişmesi».", segments=[seg("تَغَيُّرَ", "taghayyur", "noun"), pr3ms()]),
  W("مُقَدَّرٌ", "muqaddar", "noun", ["inna-wa-akhawatuha", "ism-maful"], "خَبَرُ أَنَّ مَرْفُوعٌ — الْمُفْرَدُ عَلَى قُفْلٍ وَالْجَمْعُ عَلَى أُسْدٍ.", "«is estimated» — the singular on the pattern قُفْل, the plural on أُسْد.", "«takdîrîdir» — müfredi kufl, cem'i üsd vezninde.", punct="."),
 ]})

# ----------- s4 (RESTORED): sound and broken
S.append({"id": "s4", "translation": {
 "en": "And it is sound and broken; and the sound is masculine and feminine." + R_EN,
 "tr": "Sâlim ve mükesserdir; sâlim de müzekker ve müennestir." + R_TR},
 "tokens": [
  atf_wa("وَهُوَ", "huwa", "pron", ["mubtada-khabar"], "هُوَ مُبْتَدَأٌ.", "«and it is».", "«ve o».", "هُوَ"),
  W("صَحِيحٌ", "sahih", "noun", ["mubtada-khabar", JM], "خَبَرٌ مَرْفُوعٌ.", "«sound» — the khabar.", "«sâlim» — haber."),
  atf_wa("وَمُكَسَّرٌ", "mukassar", "noun", [JK, "ism-maful"], "مُكَسَّرٌ مَعْطُوفٌ.", "«and broken».", "«ve mükesser».", "مُكَسَّرٌ", punct="؛"),
  atf_wa("وَالصَّحِيحُ", "sahih", "noun", ["mubtada-khabar"], "الصَّحِيحُ مُبْتَدَأٌ.", "«and the sound».", "«ve sâlim».", "الصَّحِيحُ"),
  W("مُذَكَّرٌ", "mudhakkar", "noun", ["mubtada-khabar", JM], "خَبَرٌ مَرْفُوعٌ.", "«masculine».", "«müzekker»."),
  atf_wa("وَمُؤَنَّثٌ", "muannath", "noun", [JF], "مُؤَنَّثٌ مَعْطُوفٌ.", "«and feminine».", "«ve müennes».", "مُؤَنَّثٌ", punct="."),
 ]})

# ----------- s5 (VERBATIM): the sound masculine plural
S.append({"id": "s5", "translation": {
 "en": "The sound masculine plural: what has joined to its end a wāw with a ḍamma before it, or a yāʾ with a kasra before it, and a nūn with a fatḥa, to show that with it are more than it — as in مُسْلِمُونَ and مُسْلِمِينَ.",
 "tr": "Sâlim müzekker cemi: kendisiyle birlikte kendisinden daha çoğunun bulunduğuna delâlet etsin diye, sonuna mâkabli mazmûm bir vâv ya da mâkabli meksûr bir yâ ile meftûh bir nûn bitişendir — مُسْلِمُونَ ve مُسْلِمِينَ gibi."},
 "tokens": [
  W("جَمْعُ", "jam", "noun", ["mubtada-khabar", "idafa-definiteness", JM], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the plural of» — the mubtada.", "«cem-i» — mübtedâ."),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine».", "«müzekker»."),
  W("السَّالِمُ", "salim", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ لِجَمْعُ مَرْفُوعَةٌ.", "«sound».", "«sâlim».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("لَحِقَ", "lahiqa", "verb", ["ism-mawsul"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«has joined».", "«bitişen»."),
  W("آخِرَهُ", "akhir", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end».", "«sonuna».", segments=[seg("آخِرَ", "akhir", "noun"), pr3ms()]),
  W("وَاوٌ", "waw-letter", "noun", ["fail", JM], "فَاعِلٌ مَرْفُوعٌ — فِي الرَّفْعِ.", "«a wāw» — in rafʿ.", "«bir vâv» — ref'de."),
  W("مَضْمُومٌ", "madmum", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«with a ḍamma».", "«mazmûm»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلُ مَضْمُومٌ.", "«what».", "«... olan»."),
  W("قَبْلَهَا", "qabla", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is before it».", "«ondan önce».", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("يَاءٌ", "ya-letter", "noun", ["atf-nasaq", JM], "مَعْطُوفٌ مَرْفُوعٌ — فِي النَّصْبِ وَالْجَرِّ.", "«a yāʾ» — in naṣb and jarr.", "«bir yâ» — nasb ve cerde."),
  W("مَكْسُورٌ", "maksur", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«with a kasra».", "«meksûr»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فَاعِلُ مَكْسُورٌ.", "«what».", "«... olan»."),
  W("قَبْلَهَا", "qabla", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«is before it».", "«ondan önce».", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  atf_wa("وَنُونٌ", "nun-letter", "noun", [JM], "نُونٌ مَعْطُوفٌ عَلَى وَاوٌ.", "«and a nūn».", "«ve bir nûn».", "نُونٌ"),
  W("مَفْتُوحَةٌ", "maftuh", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«with a fatḥa».", "«meftûh»."),
  W("لِيَدُلَّ", "dalla", "verb", ["lam-taleel", "an-masdariyya", "doubled-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَيَدُلَّ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«to show».", "«delâlet etsin diye».", segments=[seg("لِ", "lam-taleel", "part"), seg("يَدُلَّ", "dalla", "verb")]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«that».", "«-e»."),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«that».", "«... olduğuna»."),
  W("مَعَهُ", "maa", "noun", ["inna-wa-akhawatuha", "maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ خَبَرُ أَنَّ مُقَدَّمٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with it».", "«onunla birlikte».", segments=[seg("مَعَ", "maa", "noun"), pr3ms()]),
  W("أَكْثَرَ", "akthar", "noun", ["inna-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«more» — the ism of أَنَّ.", "«daha çoğu» — enne'nin ismi."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«than it».", "«ondan».", punct="،", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  nahwu(),
  W("مُسْلِمُونَ", "muslim", "noun", ["idafa-definiteness", JM], "فِي مَحَلِّ جَرٍّ — جَمْعٌ مَرْفُوعٌ بِالْوَاوِ.", "«Muslims» — rafʿ by the wāw.", "«Müslümanlar» — vâv ile merfû."),
  cited_wa("وَمُسْلِمِينَ", "muslim", "noun", [JM], "مُسْلِمِينَ مَعْطُوفٌ — مَنْصُوبٌ وَمَجْرُورٌ بِالْيَاءِ.", "«and مُسْلِمِينَ» — naṣb and jarr by the yāʾ.", "«ve müslimîne» — yâ ile mansûb ve mecrûr.", "مُسْلِمِينَ", punct="."),
 ]})

# ----------- s6 (RESTORED): the manqus and the maqsur
S.append({"id": "s6", "translation": {
 "en": "And the yāʾ of the manqūṣ is dropped before it, as in قَاضُونَ; and the alif of the maqṣūr, the fatḥa before it staying, as in مُصْطَفَوْنَ." + R_EN,
 "tr": "Ondan önce mankûsun yâsı düşer, قَاضُونَ gibi; maksûrun elifi de düşer ve mâkablinin fethası kalır, مُصْطَفَوْنَ gibi." + R_TR},
 "tokens": [
  atf_wa("وَتُحْذَفُ", "hadhafa", "verb", ["naib-al-fail"], "تُحْذَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is dropped».", "«ve düşer».", "تُحْذَفُ"),
  W("يَاءُ", "ya-letter", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the yāʾ of».", "«yâsı»."),
  W("الْمَنْقُوصِ", "manqus", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the manqūṣ».", "«mankûsun»."),
  W("قَبْلَهُ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — قَبْلَ الْوَاوِ.", "«before it» — before the wāw.", "«ondan önce» — vâvdan önce.", punct="،", segments=[seg("قَبْلَ", "qabla", "noun"), pr3ms()]),
  nahwu(),
  cited("قَاضُونَ", "qadi", "noun", ["idafa-definiteness", JM, "ism-maqsur-manqus"], "فِي مَحَلِّ جَرٍّ — أَصْلُهُ قَاضِيُونَ: نُقِلَتْ ضَمَّةُ الْيَاءِ إِلَى الضَّادِ وَحُذِفَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«judges» — from قَاضِيُونَ: the yāʾ's ḍamma moved to the ḍād and the yāʾ fell.", "«kadılar» — aslı kâdıyûne: yânın dammesi dâd'a taşındı, yâ düştü.", punct="،"),
  atf_wa("وَأَلِفُ", "alif-letter", "noun", ["naib-al-fail", "idafa-definiteness"], "أَلِفُ مَعْطُوفٌ عَلَى يَاءُ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the alif of».", "«ve elifi».", "أَلِفُ"),
  W("الْمَقْصُورِ", "maqsur", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the maqṣūr».", "«maksûrun»."),
  W("بِبَقَاءِ", "baqa", "noun", ["huruf-jarr", "idafa-definiteness", "hal"], "الْبَاءُ حَرْفُ جَرٍّ، وَبَقَاءِ مَجْرُورٌ، وَهُوَ مُضَافٌ — فِي مَوْضِعِ الْحَالِ.", "«with the staying of».", "«kalmasıyla».", segments=[seg("بِ", "bi", "prep"), seg("بَقَاءِ", "baqa", "noun")]),
  W("الْفَتْحَةِ", "fatha", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the fatḥa».", "«fethanın»."),
  W("قَبْلَهَا", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«before it».", "«ondan önceki».", punct="،", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  nahwu(),
  cited("مُصْطَفَوْنَ", "mustafa", "noun", ["idafa-definiteness", JM, "ism-maqsur-manqus"], "فِي مَحَلِّ جَرٍّ — حُذِفَتِ الْأَلِفُ لِالْتِقَاءِ السَّاكِنَيْنِ وَبَقِيَتِ الْفَتْحَةُ دَلِيلًا عَلَيْهَا.", "«chosen ones» — the alif fell between two sakins, its fatḥa left as its trace.", "«seçilmişler» — elif iki sâkin arasında düştü, fethası izi olarak kaldı.", punct="."),
 ]})

# ----------- s7 (RESTORED): the conditions — a noun
S.append({"id": "s7", "translation": {
 "en": "And the condition of its singular, if it is a noun, is that it be a proper name of a rational male, free of the tāʾ and of compounding — as in زَيْدُونَ." + R_EN,
 "tr": "Müfredi isim ise şartı, tâ'dan ve terkibden hâlî, âkil bir müzekkerin alemi olmasıdır — زَيْدُونَ gibi." + R_TR},
 "tokens": [
  atf_wa("وَشَرْطُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness", JM], "شَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the condition of» — the mubtada.", "«ve şartı» — mübtedâ.", "شَرْطُ"),
  W("مُفْرَدِهِ", "mufrad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its singular».", "«müfredinin».", segments=[seg("مُفْرَدِ", "mufrad", "noun"), pr3msi()]),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«it is».", "«ise»."),
  W("اسْمًا", "ism", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ — غَيْرَ صِفَةٍ.", "«a noun» — not a description.", "«isim» — sıfat olmayan."),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ، وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ شَرْطُ.", "«that» — the clause is the khabar of «condition».", "«-ması» — cümle «şart»ın haberi."),
  W("يَكُونَ", "kana", "verb", ["an-masdariyya", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«it be».", "«olması»."),
  W("عَلَمَ", "alam-name", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ يَكُونَ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«a proper name of».", "«alemi»."),
  W("مُذَكَّرٍ", "mudhakkar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a male».", "«müzekkerin»."),
  W("عَاقِلٍ", "aqil", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«rational».", "«âkil»."),
  W("خَالٍ", "khali", "noun", ["naat-sifa", "ism-maqsur-manqus", "ism-fail"], "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«free».", "«hâlî»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("التَّاءِ", "ta-letter", "noun", ["huruf-jarr"], "مَجْرُورٌ — تَاءِ التَّأْنِيثِ كَطَلْحَةَ.", "«the tāʾ» — like طَلْحَة.", "«tâ» — Talha gibi."),
  atf_wa("وَالتَّرْكِيبِ", "tarkib", "noun", [], "التَّرْكِيبِ مَعْطُوفٌ مَجْرُورٌ — كَبَعْلَبَكَّ.", "«and compounding» — like بَعْلَبَكّ.", "«ve terkib» — Ba'lebek gibi.", "التَّرْكِيبِ", punct="،"),
  nahwu(),
  cited("زَيْدُونَ", "zayd", "propn", ["idafa-definiteness", JM], "فِي مَحَلِّ جَرٍّ — جَمْعُ زَيْدٍ بِالْوَاوِ.", "«Zayds» — the plural of the name.", "«Zeydler» — ismin cem'i.", punct="."),
 ]})

# ----------- s8 (RESTORED): the conditions — a description
S.append({"id": "s8", "translation": {
 "en": "And if it is a description, that it be of a rational male, free of the tāʾ, not on أَفْعَلُ with فَعْلَاءُ, nor on فَعْلَانُ with فَعْلَى, nor of what the masculine and the feminine share — as in مُسْلِمُونَ, not أَحْمَرُ، سَكْرَانُ، جَرِيحٌ، صَبُورٌ، عَلَّامَةٌ." + R_EN,
 "tr": "Sıfat ise, âkil bir müzekkerin sıfatı olup tâ'dan hâlî olması, فَعْلَاءُ'sı olan أَفْعَلُ ve فَعْلَى'sı olan فَعْلَانُ vezninde olmaması ve müzekkeri ile müennesinin eşit olduğu sıfatlardan olmamasıdır — مُسْلِمُونَ gibi; أَحْمَرُ، سَكْرَانُ، جَرِيحٌ، صَبُورٌ، عَلَّامَةٌ değil." + R_TR},
 "tokens": [
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "إِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", "إِنْ"),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«it is».", "«ise»."),
  W("صِفَةً", "sifa", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a description».", "«sıfat»."),
  W("فَلِمُذَكَّرٍ", "mudhakkar", "noun", ["huruf-jarr", "al-fa-fi-jawab-al-shart", "khabar-al-mubtada-wa-ahkamuh"], "الْفَاءُ فِي جَوَابِ الشَّرْطِ، وَاللَّامُ حَرْفُ جَرٍّ، وَمُذَكَّرٍ مَجْرُورٌ — خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: فَشَرْطُهُ أَنْ يَكُونَ لِمُذَكَّرٍ.", "«then of a male» — its condition: that it describe a male.", "«o zaman bir müzekkerin» — şartı: bir müzekkerin sıfatı olması.", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("مُذَكَّرٍ", "mudhakkar", "noun")]),
  W("عَاقِلٍ", "aqil", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«rational».", "«âkil»."),
  W("خَالٍ", "khali", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«free».", "«hâlî»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("التَّاءِ", "ta-letter", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the tāʾ».", "«tâ»."),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "naat-sifa"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِفَةٌ.", "«not being».", "«... olmayan»."),
  W("أَفْعَلَ", "afal-wazn", "noun", ["kana-wa-akhawatuha", "mamnu-min-sarf"], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ — الْوَزْنُ.", "«on أَفْعَلُ» — the pattern.", "«ef'al vezninde» — vezin."),
  cited("فَعْلَاءَ", "falaa-wazn", "noun", [], "لَفْظٌ مَحْكِيٌّ — أَيْ: أَفْعَلُ الَّذِي مُؤَنَّثُهُ فَعْلَاءُ.", "«with فَعْلَاءُ» — the أَفْعَلُ whose feminine is فَعْلَاءُ.", "«fa'lâ ile» — müennesi fa'lâ olan ef'al.", punct="،"),
  la_wa("وَلَا", "la", "part", [], "لَا حَرْفٌ.", "«nor».", "«ne de».", "لَا"),
  cited("فَعْلَانَ", "falan-wazn", "noun", ["atf-nasaq", "mamnu-min-sarf"], "مَعْطُوفٌ عَلَى أَفْعَلَ مَنْصُوبٌ.", "«on فَعْلَانُ».", "«fa'lân vezninde»."),
  cited("فَعْلَى", "fala-wazn", "noun", [], "لَفْظٌ مَحْكِيٌّ — أَيْ: فَعْلَانُ الَّذِي مُؤَنَّثُهُ فَعْلَى.", "«with فَعْلَى».", "«fa'lâ ile».", punct="،"),
  la_wa("وَلَا", "la", "part", [], "لَا حَرْفٌ.", "«nor».", "«ne de».", "لَا"),
  W("مِمَّا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "atf-nasaq", "anwa-ma"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ؛ مَعْطُوفٌ.", "«of what».", "«... olanlardan».", segments=[seg("مِنْ", "min", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("يَسْتَوِي", "istawa", "verb", ["ism-mawsul", "fail", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْجُمْلَةُ صِلَةٌ.", "«are equal».", "«eşit olan»."),
  W("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«in it».", "«onda».", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("الْمُذَكَّرُ", "mudhakkar", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the masculine».", "«müzekker»."),
  atf_wa("وَالْمُؤَنَّثُ", "muannath", "noun", [], "الْمُؤَنَّثُ مَعْطُوفٌ.", "«and the feminine».", "«ve müennes».", "الْمُؤَنَّثُ", punct="،"),
  nahwu(),
  cited("مُسْلِمُونَ", "muslim", "noun", ["idafa-definiteness", JM], "فِي مَحَلِّ جَرٍّ — اسْتَوْفَى الشُّرُوطَ.", "«Muslims» — meets every condition.", "«Müslümanlar» — bütün şartları taşır.", punct="،"),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«değil»."),
  cited("أَحْمَرُ", "ahmar", "noun", [JM, "mamnu-min-sarf"], "لَفْظٌ مَحْكِيٌّ — أَفْعَلُ فَعْلَاءَ: أَحْمَرُ حَمْرَاءُ، جَمْعُهُ حُمْرٌ.", "«أَحْمَرُ» — its plural is حُمْرٌ.", "«ahmer» — cem'i humr."),
  cited_wa("وَسَكْرَانُ", "sakran", "noun", [JM, "mamnu-min-sarf"], "سَكْرَانُ مَعْطُوفٌ — فَعْلَانُ فَعْلَى: سَكْرَانُ سَكْرَى.", "«and سَكْرَانُ» — سَكْرَى its feminine.", "«ve sekrân» — müennesi sekrâ.", "سَكْرَانُ"),
  cited_wa("وَجَرِيحٌ", "jarih", "noun", [JM], "جَرِيحٌ مَعْطُوفٌ — يَسْتَوِي فِيهِ الْمُذَكَّرُ وَالْمُؤَنَّثُ: رَجُلٌ جَرِيحٌ وَامْرَأَةٌ جَرِيحٌ.", "«and جَرِيحٌ» — one form for both genders.", "«ve cerîh» — iki cins için tek şekil.", "جَرِيحٌ"),
  cited_wa("وَصَبُورٌ", "sabur", "noun", [JM], "صَبُورٌ مَعْطُوفٌ — كَذٰلِكَ.", "«and صَبُورٌ» — the same.", "«ve sabûr» — aynı.", "صَبُورٌ"),
  cited_wa("وَعَلَّامَةٌ", "allama-mubalagha", "noun", [JM], "عَلَّامَةٌ مَعْطُوفٌ — فِيهِ تَاءُ التَّأْنِيثِ.", "«and عَلَّامَةٌ» — it carries the tāʾ.", "«ve allâme» — tâ taşır.", "عَلَّامَةٌ", punct="."),
 ]})

# ----------- s9 (RESTORED): the nun in annexation; the irregular plurals
S.append({"id": "s9", "translation": {
 "en": "And its nūn is dropped in annexation, as in «the Muslims of the people came to me»; and سِنُونَ and أَرَضُونَ are against the rule." + R_EN,
 "tr": "Nûnu izâfette hazfedilir, «kavmin Müslümanları bana geldi» gibi; سِنُونَ ve أَرَضُونَ ise kıyâsa aykırıdır." + R_TR},
 "tokens": [
  atf_wa("وَتُحْذَفُ", "hadhafa", "verb", ["naib-al-fail"], "تُحْذَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is dropped».", "«ve hazfedilir».", "تُحْذَفُ"),
  W("نُونُهُ", "nun-letter", "noun", ["naib-al-fail", "idafa-definiteness", JM], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its nūn».", "«nûnu».", segments=[seg("نُونُ", "nun-letter", "noun"), pr3ms()]),
  W("بِالْإِضَافَةِ", "idafa", "noun", ["huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْإِضَافَةِ مَجْرُورٌ.", "«in annexation».", "«izâfetle».", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْإِضَافَةِ", "idafa", "noun")]),
  nahwu(),
  W("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs", "ya-al-mutakallim"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  W("مُسْلِمُو", "muslim", "noun", ["fail", "idafa-definiteness", JM], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهُوَ مُضَافٌ.", "«the Muslims of» — the nūn gone for the iḍāfa.", "«Müslümanları» — izâfet için nûnu düşmüş."),
  W("الْقَوْمِ", "qawm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the people».", "«kavmin».", punct="؛"),
  cited_wa("وَسِنُونَ", "sana", "noun", ["mubtada-khabar", JM], "سِنُونَ مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ — جَمْعُ سَنَةٍ.", "«and سِنُونَ» — the plural of سَنَة.", "«ve sinûn» — sene'nin cem'i.", "سِنُونَ"),
  cited_wa("وَأَرَضُونَ", "ard", "noun", [JM], "أَرَضُونَ مَعْطُوفٌ — جَمْعُ أَرْضٍ بِفَتْحِ الرَّاءِ.", "«and أَرَضُونَ» — the plural of أَرْض.", "«ve aradûn» — arz'ın cem'i.", "أَرَضُونَ"),
  W("شَاذٌّ", "shadhdh", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — لَا مُذَكَّرَ وَلَا عَاقِلَ وَلَا عَلَمَ.", "«against the rule» — neither male, nor rational, nor a name.", "«şâzdır» — ne müzekker, ne âkil, ne alem.", punct="."),
 ]})

# ----------- s10 (VERBATIM): the sound feminine plural
S.append({"id": "s10", "translation": {
 "en": "The sound feminine plural: what has joined to its end an alif and a tāʾ.",
 "tr": "Sâlim müennes cemi: sonuna bir elif ve bir tâ bitişendir."},
 "tokens": [
  W("جَمْعُ", "jam", "noun", ["mubtada-khabar", "idafa-definiteness", JF], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the plural of».", "«cem-i»."),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine».", "«müennes»."),
  W("السَّالِمُ", "salim", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«sound».", "«sâlim».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("لَحِقَ", "lahiqa", "verb", ["ism-mawsul"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«has joined».", "«bitişen»."),
  W("آخِرَهُ", "akhir", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end».", "«sonuna».", segments=[seg("آخِرَ", "akhir", "noun"), pr3ms()]),
  W("أَلِفٌ", "alif-letter", "noun", ["fail", JF], "فَاعِلٌ مَرْفُوعٌ.", "«an alif».", "«bir elif»."),
  atf_wa("وَتَاءٌ", "ta-letter", "noun", [JF], "تَاءٌ مَعْطُوفٌ.", "«and a tāʾ».", "«ve bir tâ».", "تَاءٌ", punct="."),
 ]})

# ----------- s11 (RESTORED): its conditions
S.append({"id": "s11", "translation": {
 "en": "And its singular, if a description, must have a masculine taking the wāw and the nūn, as in نَاصِرَاتٌ and مَنْصُورَاتٌ; if it has no masculine it must not be bare of the tāʾ, so حَائِضٌ is not so pluralised; and if a noun, it is unrestricted." + R_EN,
 "tr": "Müfredi sıfat ise, müzekkerinin vâv ve nûn ile cemi'lenir olması gerekir, نَاصِرَاتٌ ve مَنْصُورَاتٌ gibi; müzekkeri yoksa tâ'dan mücerred olmamalıdır, dolayısıyla حَائِضٌ böyle cemi'lenmez; isim ise mutlaktır." + R_TR},
 "tokens": [
  atf_wa("وَمُفْرَدُهُ", "mufrad", "noun", ["mubtada-khabar", "idafa-definiteness", JF], "مُفْرَدُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its singular» — the mubtada.", "«ve müfredi» — mübtedâ.", "مُفْرَدُ", extra_segs=[seg("مُفْرَدُ", "mufrad", "noun"), pr3ms()]),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«it is».", "«ise»."),
  W("صِفَةً", "sifa", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a description».", "«sıfat»."),
  W("فَشَرْطُهُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness", "al-fa-fi-jawab-al-shart"], "الْفَاءُ فِي جَوَابِ الشَّرْطِ، وَشَرْطُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«then its condition».", "«o zaman şartı».", segments=[seg("فَ", "fa", "conj"), seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ، وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«-ması»."),
  W("يَكُونَ", "kana", "verb", ["an-masdariyya", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«it be».", "«olması»."),
  li_("لِمُذَكَّرِهِ", "mudhakkar", "noun", ["idafa-definiteness", "kana-wa-akhawatuha", "khabar-al-mubtada-wa-ahkamuh"], "مُذَكَّرِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ؛ خَبَرُ يَكُونَ مُقَدَّمٌ.", "«for its masculine».", "«müzekkerinin».", "مُذَكَّرِ", segs=[seg("لِ", "li", "prep"), seg("مُذَكَّرِ", "mudhakkar", "noun"), pr3msi()]),
  W("جَمْعٌ", "jam", "noun", ["kana-wa-akhawatuha"], "اسْمُ يَكُونَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a plural».", "«bir cemi»."),
  W("بِالْوَاوِ", "waw-letter", "noun", ["huruf-jarr", "naat-sifa"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْوَاوِ مَجْرُورٌ.", "«with the wāw».", "«vâv ile».", segments=[seg("بِ", "bi", "prep"), seg("الْوَاوِ", "waw-letter", "noun")]),
  atf_wa("وَالنُّونِ", "nun-letter", "noun", [], "النُّونِ مَعْطُوفٌ.", "«and the nūn».", "«ve nûn».", "النُّونِ", punct="،"),
  nahwu(),
  cited("نَاصِرَاتٌ", "nasir-helper", "noun", ["idafa-definiteness", JF, "ism-fail"], "فِي مَحَلِّ جَرٍّ — مُذَكَّرُهُ نَاصِرُونَ.", "«helpers (f.)» — its masculine is نَاصِرُونَ.", "«yardımcılar (müennes)» — müzekkeri nâsırûne."),
  cited_wa("وَمَنْصُورَاتٌ", "mansur", "noun", [JF, "ism-maful"], "مَنْصُورَاتٌ مَعْطُوفٌ — مُذَكَّرُهُ مَنْصُورُونَ.", "«and helped (f.)».", "«ve yardım edilenler (müennes)».", "مَنْصُورَاتٌ", punct="؛"),
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "إِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", "إِنْ"),
  W("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-mazsa»."),
  W("يَكُنْ", "kana", "verb", ["lam-jazim", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ — تَامَّةٌ.", "«there is».", "«olmazsa»."),
  W("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to it».", "«onun».", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  W("مُذَكَّرٌ", "mudhakkar", "noun", ["fail"], "فَاعِلُ يَكُنْ مَرْفُوعٌ.", "«a masculine».", "«müzekkeri»."),
  W("فَشَرْطُهُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness", "al-fa-fi-jawab-al-shart"], "الْفَاءُ فِي الْجَوَابِ، وَشَرْطُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«then its condition».", "«o zaman şartı».", segments=[seg("فَ", "fa", "conj"), seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ.", "«that».", "«-ması»."),
  W("لَا", "la", "part", ["la-nafiya"], "حَرْفُ نَفْيٍ.", "«not».", "«-maması»."),
  W("يَكُونَ", "kana", "verb", ["an-masdariyya", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«it be».", "«olması»."),
  W("مُجَرَّدًا", "mujarrad", "noun", ["kana-wa-akhawatuha", "ism-maful"], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«bare».", "«mücerred»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("التَّاءِ", "ta-letter", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the tāʾ».", "«tâ».", punct="،"),
  W("فَلَا", "la", "part", ["la-nafiya"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so not».", "«dolayısıyla ... -mez».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la", "part")]),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is it said».", "«denmez».", punct=":"),
  cited("حَائِضَاتٌ", "haid", "noun", ["naib-al-fail", JF], "فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — لِأَنَّ حَائِضًا لَا تَاءَ فِيهِ وَلَا مُذَكَّرَ لَهُ؛ جَمْعُهُ حُيَّضٌ.", "«حَائِضَات» — حَائِض has no tāʾ and no masculine; its plural is حُيَّضٌ.", "«hâizât» — hâiz'de tâ yok, müzekkeri yok; cem'i huyyad.", punct="؛"),
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "إِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", "إِنْ"),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«it is».", "«ise»."),
  W("اسْمًا", "ism", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a noun».", "«isim»."),
  W("فَمُطْلَقٌ", "mutlaq", "noun", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ فِي الْجَوَابِ، وَمُطْلَقٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — فَهُوَ مُطْلَقٌ بِلَا شَرْطٍ.", "«it is unrestricted» — no condition.", "«mutlaktır» — şartsız.", punct="."),
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
 "ma-sifa": need("ma-sifa", "مَا (الصِّفَة)", None, "pron", "the vague مَا used as an adjective: تَغَيُّرٌ مَا «some change», يَوْمًا مَا «some day»", "sıfat olarak kullanılan ibhâm mâ'sı: tağayyurun mâ «bir değişiklik», yevmen mâ «herhangi bir gün»", 5),
 "ziyada": need("ziyada", "زِيَادَة", "ز ي د", "noun", "addition, increase (masdar of زَادَ)", "ziyâde, artma (zâde'nin masdarı)", 3),
 "nuqsan": need("nuqsan", "نُقْصَان", "ن ق ص", "noun", "decrease, removal (masdar of نَقَصَ)", "noksan, eksilme (nekasa'nın masdarı)", 3),
 "haraka": need("haraka", "حَرَكَة", "ح ر ك", "noun", "a vowel mark (fatḥa, ḍamma, kasra); motion", "hareke (fetha, damme, kesre); hareket", 2, plural="حَرَكَات"),
 "sukun": need("sukun", "سُكُون", "س ك ن", "noun", "the sukūn — the mark of no vowel; stillness", "sükûn — harekesizlik alâmeti; durgunluk", 2),
 "asad": need("asad", "أَسَد", "أ س د", "noun", "a lion (plural أُسْد, by a change of vowels)", "aslan (cem'i üsd, harekelerin değişmesiyle)", 2, plural="أُسْد"),
 "tamr": need("tamr", "تَمْر", "ت م ر", "noun", "dates (a generic noun, not a plural: one is تَمْرَة)", "hurma (cins ismi, cemi değil: bir tanesi temre)", 2),
 "asahh": need("asahh", "أَصَحّ", "ص ح ح", "noun", "soundest, most correct (elative of صَحِيح) — عَلَى الْأَصَحِّ: by the soundest view", "en sahih, en doğru (sahîh'in ism-i tafdîli) — ale'l-esahh: en sahih görüşe göre", 4),
 "salim": need("salim", "سَالِم", "س ل م", "noun", "sound, intact — الْجَمْعُ السَّالِمُ: the plural that keeps its singular whole", "sâlim, sağlam — cem-i sâlim: müfredini bütün tutan cemi", 3),
 "baqa": need("baqa", "بَقَاء", "ب ق ي", "noun", "staying, remaining (masdar of بَقِيَ)", "kalma, bekâ (bekıye'nin masdarı)", 3),
 "fatha": need("fatha", "فَتْحَة", "ف ت ح", "noun", "the fatḥa — the vowel a", "fetha — a sesi", 1),
 "falaa-wazn": need("falaa-wazn", "فَعْلَاء", None, "noun", "the pattern فَعْلَاءُ — the feminine of أَفْعَلُ in colours and defects (حَمْرَاءُ)", "fa'lâ vezni — renk ve kusurlarda ef'al'in müennesi (hamrâ)", 4),
 "falan-wazn": need("falan-wazn", "فَعْلَان", None, "noun", "the pattern فَعْلَانُ — whose feminine is فَعْلَى (سَكْرَانُ سَكْرَى)", "fa'lân vezni — müennesi fa'lâ olan (sekrân sekrâ)", 4),
 "fala-wazn": need("fala-wazn", "فَعْلَى", None, "noun", "the pattern فَعْلَى — the feminine of فَعْلَانُ (سَكْرَى)", "fa'lâ vezni — fa'lân'ın müennesi (sekrâ)", 4),
 "ahmar": need("ahmar", "أَحْمَر", "ح م ر", "noun", "red (masc.; fem. حَمْرَاءُ; plural حُمْرٌ) — a diptote", "kırmızı (müzekker; müennesi hamrâ; cem'i humr) — gayr-i munsarif", 2),
 "sakran": need("sakran", "سَكْرَان", "س ك ر", "noun", "drunk (fem. سَكْرَى) — a diptote on فَعْلَان", "sarhoş (müennesi sekrâ) — fa'lân vezninde gayr-i munsarif", 3),
 "jarih": need("jarih", "جَرِيح", "ج ر ح", "noun", "wounded — one form for both genders (رَجُلٌ جَرِيحٌ، امْرَأَةٌ جَرِيحٌ)", "yaralı — iki cins için tek şekil (racülün cerîhun, imraetün cerîhun)", 3),
 "sabur": need("sabur", "صَبُور", "ص ب ر", "noun", "very patient — one form for both genders", "çok sabırlı — iki cins için tek şekil", 3),
 "allama-mubalagha": need("allama-mubalagha", "عَلَّامَة", "ع ل م", "noun", "a great scholar — an intensive on فَعَّالَة whose tāʾ bars the wāw-plural", "allâme — tâ'sı vâvlı cemi'yi engelleyen fa''âle vezninde mübâlağa", 3),
 "shadhdh": need("shadhdh", "شَاذّ", "ش ذ ذ", "noun", "against the rule, irregular (heard but not analogical)", "şâz, kurala aykırı (işitilmiş ama kıyâsî olmayan)", 3),
 "mansur": need("mansur", "مَنْصُور", "ن ص ر", "noun", "helped, given victory (ism maf'ul of نَصَرَ)", "yardım edilen, muzaffer (nasara'nın ism-i mef'ûlü)", 2),
 "haid": need("haid", "حَائِض", "ح ي ض", "noun", "menstruating (a description with no masculine; plural حُيَّضٌ, and حَائِضَاتٌ only from حَائِضَة)", "hayızlı (müzekkeri olmayan sıfat; cem'i huyyad; hâizât ancak hâiza'dan)", 4),
 "mujarrad": need("mujarrad", "مُجَرَّد", "ج ر د", "noun", "bare, stripped (of) — ism maf'ul of Form II جَرَّدَ", "mücerred, soyulmuş (-den) — cerrede'nin ism-i mef'ûlü", 3),
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
print("kafiya ch13 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْمَجْمُوعُ وَالْجَمْعُ الصَّحِيحُ فِي الْكَافِيَةِ", "en": "The plural in the Kafiya: the definition, what is and is not a plural, and the two sound plurals with their conditions", "tr": "Kâfiye'de cemi: tarif, neyin cemi olup olmadığı ve şartlarıyla iki sâlim cemi"},
 "level": 3, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المجموع: ما دل على آحاد مقصودة بحروف مفرده بتغير ما؛ تمر وركب ليسا بجمع على الأصح؛ جمع المذكر السالم وشرط مفرده؛ سنون وأرضون شاذ؛ جمع المؤنث السالم وشرطه", "ضياء صونغور اوغلى — دفتر الكافية: التعريفات الثلاثة بلفظها، الزيادة والنقصان وتغير الحركة، قاضون ومصطفون، الشروط الخمسة، مسلمو القوم، حائض وحيض"],
 "question": {
  "en": ["What is a PLURAL? A word pointing to intended units by the letters of its singular, with some change to them — by addition (رِجَال), removal (كُتُب) or a shift of vowels (أُسْد). A generic noun like تَمْر and a collective like رَكْب are not plurals (they have no singular of their own letters); فُلْك is, because its change is estimated.",
         "What is the SOUND MASCULINE PLURAL? The singular plus a wāw after a ḍamma (rafʿ) or a yāʾ after a kasra (naṣb, jarr) and a nūn with a fatḥa: مُسْلِمُونَ / مُسْلِمِينَ. A manqūṣ loses its yāʾ first (قَاضُونَ), a maqṣūr its alif with the fatḥa kept (مُصْطَفَوْنَ).",
         "Who may take it? A NOUN only if it is the proper name of a rational male with no tāʾ and no compounding (زَيْدُونَ); a DESCRIPTION only if it describes a rational male, has no tāʾ, is not أَفْعَلُ/فَعْلَاءُ (أَحْمَرُ), not فَعْلَانُ/فَعْلَى (سَكْرَانُ), and not shared by both genders (جَرِيحٌ، صَبُورٌ). عَلَّامَةٌ fails by its tāʾ.",
         "What of its nūn? It drops in annexation — جَاءَنِي مُسْلِمُو الْقَوْمِ — exactly like the dual's. سِنُونَ and أَرَضُونَ (from سَنَة and أَرْض) take the ending against every condition and are recorded as irregular.",
         "What is the SOUND FEMININE PLURAL? The singular plus an alif and a tāʾ. A description takes it only if its masculine takes the wāw-plural (نَاصِرَاتٌ، مَنْصُورَاتٌ); one with no masculine must carry the tāʾ (حَائِضَةٌ → حَائِضَاتٌ, but حَائِضٌ → حُيَّضٌ); a plain noun takes it freely.",
         "What does the engine do? The IdafaEngine drops the sound plural's nūn and the dual's before a muḍāf ilayh, and the AlamaEngine declines both by their letters; the plural rules of the Kafiya are the conditions the IsmTagger's wazn roles and the games' plural items are checked against."],
  "tr": ["CEMİ nedir? Müfredinin harfleriyle, onlarda bir değişiklikle kastedilen fertlere delâlet eden kelime — ziyâde ile (رِجَال), noksan ile (كُتُب) ya da hareke değişmesiyle (أُسْد). تَمْر gibi cins ismi ve رَكْب gibi ism-i cem' cemi değildir (kendi harflerinden müfredi yoktur); فُلْك cemidir, çünkü değişmesi takdîrîdir.",
         "SÂLİM MÜZEKKER CEMİ nedir? Müfred + dammeden sonra vâv (ref') ya da kesreden sonra yâ (nasb, cer) ve meftûh nûn: مُسْلِمُونَ / مُسْلِمِينَ. Mankûs önce yâsını kaybeder (قَاضُونَ), maksûr elifini, fethası kalarak (مُصْطَفَوْنَ).",
         "Kim alabilir? İSİM ancak tâsız ve terkibsiz, âkil bir müzekkerin alemiyse (زَيْدُونَ); SIFAT ancak âkil bir müzekkeri niteliyor, tâ taşımıyor, أَفْعَلُ/فَعْلَاءُ (أَحْمَرُ) ve فَعْلَانُ/فَعْلَى (سَكْرَانُ) vezninde değil ve iki cinste ortak değilse (جَرِيحٌ، صَبُورٌ). عَلَّامَةٌ tâ'sı yüzünden elenir.",
         "Ya nûnu? İzâfette düşer — جَاءَنِي مُسْلِمُو الْقَوْمِ — tam tesniyeninki gibi. سِنُونَ ve أَرَضُونَ (سَنَة ve أَرْض'dan) her şarta aykırı olarak eki alır ve şâz diye kaydedilir.",
         "SÂLİM MÜENNES CEMİ nedir? Müfred + elif ve tâ. Sıfat ancak müzekkeri vâvlı cemi alıyorsa alır (نَاصِرَاتٌ، مَنْصُورَاتٌ); müzekkeri olmayan tâ taşımalıdır (حَائِضَةٌ → حَائِضَاتٌ, ama حَائِضٌ → حُيَّضٌ); yalın isim serbestçe alır.",
         "Motor ne yapar? IdafaEngine muzâfun ileyhten önce sâlim ceminin ve tesniyenin nûnunu düşürür, AlamaEngine ikisini harfleriyle i'râblar; Kâfiye'nin cemi kuralları, IsmTagger'ın vezin rollerinin ve oyunlardaki cemi maddelerinin sınandığı şartlardır."]},
 "plain": {
  "en": "A plural changes its singular somehow (letters added, dropped or re-vowelled). Men's names and most adjectives for men take -ūna/-īna; women's and things' nouns take -āt; but an adjective takes -āt only if its masculine takes -ūna. The -na of both sound plurals drops before a possessor.",
  "tr": "Cemi, müfredini bir şekilde değiştirir (harf eklenir, düşer ya da harekesi değişir). Erkek adları ve erkekler için çoğu sıfat -ûne/-îne alır; kadınların ve şeylerin isimleri -ât alır; ama sıfat ancak müzekkeri -ûne alıyorsa -ât alır. İki sâlim ceminin -ne'si bir sahipten önce düşer."},
 "explanation": {
  "en": "The Kafiya defines the plural by a relation to its singular: the same letters, changed somehow, pointing to more than one. That «somehow» is the hinge of the chapter. Three changes are visible (an added alif in رِجَال, a dropped one in كُتُب, re-vowelling in أُسْد); a fourth is only estimated, which is how فُلْك — written alike for one ship and for many — is still a plural, its pattern reckoned قُفْل in the singular and أُسْد in the plural. Where there is no singular of the same letters at all, there is no plural: تَمْر is a generic noun whose unit is تَمْرَة, رَكْب a collective with no unit of its own. The sound plurals then get the longest treatment because they are the plurals a learner can BUILD, and building needs conditions. The masculine ending is reserved, for nouns, to the proper names of rational men, and for descriptions to those of rational men that have no tāʾ, are not the colour-and-defect pattern (أَحْمَرُ، whose plural is حُمْر), not the فَعْلَانُ pattern (سَكْرَانُ), and not the patterns that one form serves for both genders (جَرِيحٌ، صَبُورٌ) — because an ending that says «male plural» can only sit on a word that already says «male». The feminine ending mirrors it: a description takes -āt only where its masculine takes -ūna, so that the pair نَاصِرُونَ / نَاصِرَاتٌ stays a pair, and a description with no masculine must at least wear the tāʾ (حَائِضَةٌ), while an ordinary noun takes -āt without conditions. The exceptions are listed as exceptions: سِنُونَ and أَرَضُونَ wear the masculine ending with none of its conditions, and the notebook keeps حَائِض beside حُيَّض to show the broken plural standing where the sound one is refused.",
  "tr": "Kâfiye cemiyi müfrediyle bir ilişki üzerinden tarif eder: aynı harfler, bir şekilde değişmiş, birden fazlaya delâlet eder. Bu «bir şekilde» bâbın menteşesidir. Üç değişiklik görünür (رِجَال'de eklenen elif, كُتُب'de düşen elif, أُسْد'de hareke değişimi); dördüncüsü yalnız takdîrîdir ki فُلْك — tek gemi için de çok gemi için de aynı yazılır — böylece yine cemidir, vezni müfredde قُفْل, cemide أُسْد sayılır. Aynı harflerden bir müfred hiç yoksa cemi de yoktur: تَمْر birimi تَمْرَة olan bir cins ismi, رَكْب kendi birimi olmayan bir ism-i cem'dir. Sâlim cemiler en uzun ele alınır; çünkü onlar öğrencinin KURABİLECEĞİ cemilerdir ve kurmak şart ister. Müzekker ek, isimlerde âkil erkeklerin alemlerine, sıfatlarda ise tâ taşımayan, renk-kusur vezninde olmayan (أَحْمَرُ, cem'i حُمْر), فَعْلَانُ vezninde olmayan (سَكْرَانُ) ve tek şeklin iki cinse hizmet ettiği vezinlerde olmayan (جَرِيحٌ، صَبُورٌ) âkil erkek sıfatlarına ayrılmıştır — çünkü «erkek çoğul» diyen ek ancak zaten «erkek» diyen bir kelimeye oturabilir. Müennes ek onu yansıtır: sıfat -ât'ı ancak müzekkeri -ûne alıyorsa alır ki نَاصِرُونَ / نَاصِرَاتٌ çifti çift kalsın; müzekkeri olmayan sıfat en azından tâ giymelidir (حَائِضَةٌ); sıradan isim ise -ât'ı şartsız alır. İstisnâlar istisnâ olarak sayılır: سِنُونَ ve أَرَضُونَ hiçbir şartı taşımadan müzekker eki giyer; defter حَائِض'i حُيَّض'in yanında tutar ki sâlimin reddedildiği yerde mükesserin durduğu görülsün."},
 "examples": [
  {"ar": "الْمَجْمُوعُ: مَا دَلَّ عَلَى آحَادٍ مَقْصُودَةٍ بِحُرُوفِ مُفْرَدِهِ بِتَغَيُّرٍ مَا", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "رِجَالٌ — كُتُبٌ — أُسْدٌ", "en": "The three changes.", "tr": "Üç değişiklik.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "مُسْلِمُونَ وَمُسْلِمِينَ — قَاضُونَ — مُصْطَفَوْنَ", "en": "The sound masculine plural and its weak-ended singulars.", "tr": "Sâlim müzekker cemi ve illetli sonlu müfredleri.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "زَيْدُونَ — لَا أَحْمَرُ وَسَكْرَانُ وَجَرِيحٌ وَصَبُورٌ وَعَلَّامَةٌ", "en": "The conditions.", "tr": "Şartlar.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "جَاءَنِي مُسْلِمُو الْقَوْمِ — سِنُونَ وَأَرَضُونَ شَاذٌّ", "en": "The nūn in annexation; the irregular pair.", "tr": "İzâfette nûn; şâz çift.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "نَاصِرَاتٌ وَمَنْصُورَاتٌ — لَا يُقَالُ حَائِضَاتٌ", "en": "The sound feminine plural's conditions.", "tr": "Sâlim müennes ceminin şartları.", "sourceStory": "al-kafiya", "sentence": "s11"}],
 "commonMistakes": [
  {"wrong": "«أَحْمَرُونَ — kırmızılar, sâlim cemi»",
   "right": "«حُمْرٌ — أَفْعَلُ فَعْلَاءُ sıfatı vâvlı cemi almaz; mükesser gelir»",
   "why": {"en": "The colour-and-defect pattern is excluded by name from the sound masculine plural.", "tr": "Renk-kusur vezni sâlim müzekker cemiden adıyla dışlanmıştır."}},
  {"wrong": "«قَاضِيُونَ — mankûs yâsıyla cemi'lenir»",
   "right": "«قَاضُونَ — yânın dammesi dâd'a taşınır, iki sâkin birleşince yâ düşer»",
   "why": {"en": "The notebook's derivation: قَاضِيُونَ → the kasra of the ḍād removed, the yāʾ's ḍamma given to it, two sakins meet, the yāʾ falls.", "tr": "Defterin türetimi: قَاضِيُونَ → dâd'ın kesresi atılır, yânın dammesi ona verilir, iki sâkin birleşir, yâ düşer."}},
  {"wrong": "«حَائِضَاتٌ — hayızlı kadınlar»",
   "right": "«حُيَّضٌ — hâiz'in müzekkeri yok ve tâ'sı yok; -ât alamaz. حَائِضَاتٌ ancak حَائِضَة'dan»",
   "why": {"en": "A description with no masculine must carry the tāʾ to take the alif-and-tāʾ plural.", "tr": "Müzekkeri olmayan sıfat, elif-tâ cemisini alabilmek için tâ taşımalıdır."}},
  {"wrong": "«مُسْلِمُونَ الْقَوْمِ — izâfette nûn kalır»",
   "right": "«مُسْلِمُو الْقَوْمِ — sâlim ceminin nûnu izâfette düşer, tesniyeninki gibi»",
   "why": {"en": "The nūn stands for the tanwīn; a muḍāf takes neither.", "tr": "Nûn tenvinin yerini tutar; muzâf ikisini de almaz."}}],
 "relatedNotes": [JM, JF, JK, "al-muthanna", "idafa-definiteness", "ism-maqsur-manqus", "mamnu-min-sarf", "al-muannath-wa-alamatuh"]}

ADD_EN = (" Chapter 13 (notebook lines ~222-229): the plural, the sound masculine plural and the sound feminine plural defined in the notebook's own Arabic (s1, s5, s10) "
          "with every example it gives; the three changes as the notebook explains them (s2, commentary); تَمْر/رَكْب/فُلْك, sound and broken, قَاضُونَ and مُصْطَفَوْنَ, the "
          "conditions, the nūn in annexation, سِنُونَ/أَرَضُونَ and the feminine plural's conditions restored from the received matn and marked (s3, s4, s6-s9, s11).")
ADD_TR = (" On üçüncü bâb (defter satırları ~222-229): cemi, sâlim müzekker cemi ve sâlim müennes cemi defterin kendi Arapçasıyla tarif edilir (s1, s5, s10), verdiği her "
          "örnekle; üç değişiklik defterin açıkladığı gibi (s2, şerh); تَمْر/رَكْب/فُلْك, sâlim ve mükesser, قَاضُونَ ile مُصْطَفَوْنَ, şartlar, izâfette nûn, سِنُونَ/أَرَضُونَ ve "
          "müennes ceminin şartları alınan metinden geri yazılmış ve işaretlenmiştir (s3, s4, s6-s9, s11).")
write_out(13, S, TITLE, ADD_EN, ADD_TR, "222-229", GLOSS_ADD, notes=(NOTE,),
          related=((JM, [K]), (JF, [K]), (JK, [K])))
report(13, S, GLOSS_ADD, (NOTE,))
