# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 28: THE VERBS OF PRAISE AND BLAME. The definition in the notebook's own Arabic; the three shapes the doer of
نِعْمَ and بِئْسَ may take (lām-definite, annexed to a lām-definite, a pronoun distinguished by a manṣūb indefinite or by مَا);
the makhṣūṣ and its two parsings; its agreement with the doer and the taʾwīl of the aya of the ass-laden people (62:5); the makhṣūṣ
dropped when known (38:44, 51:48); سَاءَ like بِئْسَ (4:97); حَبَّذَا with its frozen ذَا, and the tamyīz or ḥāl around its makhṣūṣ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~325-331 of the transcription.

  VERBATIM: s1. COMMENTARY (the notebook): s2-s10 — marked C_EN/C_TR. Qurʾānic text as the source prints it.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch28.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "afal-al-madh-wal-dhamm-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "أَفْعَالُ الْمَدْحِ وَالذَّمِّ", "en": "The verbs of praise and blame — niʿma, biʾsa, sāʾa and ḥabbadhā", "tr": "Medh ve zem fiilleri — ni'me, bi'se, sâe ve habbezâ"}
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

MD = "takid-al-madh-wal-dhamm"
def NIMA(full="نِعْمَ", en="«excellent is».", tr="«ne güzel».", ar="فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ.", segs=None, lex="nima-verb"):
    return cited(full, lex, "verb", [K, MD, "al-mabni-wal-mudmar"], ar, en, tr, segments=segs)
def FAIL_N(full, lex, ar, en, tr, punct=None, tags=(), segs=None): return cited(full, lex, "noun", [K, MD, "fail"] + list(tags), ar, en, tr, punct=punct, segments=segs)
def MAKH(full, lex, en, tr, punct=None, tags=(), pos="propn"): return cited(full, lex, pos, [K, MD, "mubtada-khabar"] + list(tags), "الْمَخْصُوصُ بِالْمَدْحِ — مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْجُمْلَةُ قَبْلَهُ خَبَرٌ مُقَدَّمٌ.", en, tr, punct=punct)
def HABB(ar="فِعْلٌ مَاضٍ جَامِدٌ لِلْمَدْحِ، وَذَا فَاعِلُهُ لَا يَتَغَيَّرُ."): return cited("حَبَّذَا", "habbadha", "verb", [K, MD, "fail"], ar, "«how lovely is».", "«ne hoştur».", segments=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")])

S.append({"id": "s1", "translation": {
 "en": "The verbs of praise and blame: what was set down to bring praise or blame into being.",
 "tr": "Medh ve zem fiilleri: medh ya da zemmi inşâ etmek için konulan fiillerdir."},
 "tokens": [
  W("أَفْعَالُ", "fil", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the verbs of».", "«fiilleri»."),
  W("الْمَدْحِ", "madh", "noun", ["idafa-definiteness", MD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«praise».", "«medh»."),
  atf_wa("وَالذَّمِّ", "dhamm", "noun", ["atf-nasaq", MD], "الذَّمِّ مَعْطُوفٌ مَجْرُورٌ.", "«and blame».", "«ve zem».", "الذَّمِّ", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«was set down».", "«konulan»."),
  li_("لِإِنْشَاءِ", "insha", "noun", ["idafa-definiteness"], "إِنْشَاءِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to bring into being».", "«inşâ etmek için».", "إِنْشَاءِ"),
  W("مَدْحٍ", "madh", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«praise».", "«medh»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("ذَمٍّ", "dhamm", "noun", ["atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«blame».", "«zemmi».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And the condition for نِعْمَ and بِئْسَ to govern is one of three: that their doer be definite by the lām — as نِعْمَ الرَّجُلُ زَيْدٌ — or annexed to what is definite by the lām — as نِعْمَ صَاحِبُ الرَّجُلِ زَيْدٌ." + C_EN,
 "tr": "نِعْمَ ve بِئْسَ'nin amel şartı üç şeyden biridir: fâillerinin lâm ile marife olması — نِعْمَ الرَّجُلُ زَيْدٌ gibi — ya da lâm ile marife olana muzâf olması — نِعْمَ صَاحِبُ الرَّجُلِ زَيْدٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَشَرْطُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness"], "شَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the condition of».", "«ve ... şartı».", "شَرْطُ"),
  W("عَمَلِ", "amal", "noun", ["idafa-definiteness", "al-amil-wa-aqsamuh"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the governing of».", "«amel»."),
  cited("نِعْمَ", "nima-verb", "verb", ["idafa-definiteness", K, MD], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«niʿma».", "«ni'me»."),
  cited_wa("وَبِئْسَ", "bisa", "verb", [K, MD], "بِئْسَ مَعْطُوفٌ — فِعْلٌ مَحْكِيٌّ.", "«and biʾsa».", "«ve bi'se».", "بِئْسَ"),
  W("أَحَدُ", "ahad", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«one of».", "«... -den biridir»."),
  W("ثَلَاثَةٍ", "thalatha", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«three».", "«üç şey».", punct=":"),
  W("أَنْ", "an-masdariyya", "part", ["an-masdariyya", "nawasib-wa-jawazim-al-mudari"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ بَدَلٌ مِنْ أَحَدُ.", "«that».", "«-ması»."),
  W("يَكُونَ", "kana", "verb", ["nawasib-wa-jawazim-al-mudari", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ.", "«be».", "«olması»."),
  W("فَاعِلُهُمَا", "fail-doer", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "fail"], "اسْمُ يَكُونَ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their doer».", "«fâillerinin».", segments=[seg("فَاعِلُ", "fail-doer", "noun"), pr3d()]),
  W("مُعَرَّفًا", "muarraf", "noun", ["kana-wa-akhawatuha", "ism-maful", "al-marifa-wal-nakira-fil-kafiya"], "خَبَرُ يَكُونَ مَنْصُوبٌ.", "«definite».", "«marife»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", ["al-marifa-wal-nakira-fil-kafiya"], "اللَّامِ مَجْرُورٌ — لَامُ التَّعْرِيفِ.", "«by the lām».", "«lâm ile».", "اللَّامِ", punct="،"),
  nahwu(),
  NIMA(),
  FAIL_N("الرَّجُلُ", "rajul", "فَاعِلُ نِعْمَ مَرْفُوعٌ — مُعَرَّفٌ بِاللَّامِ.", "«the man».", "«adam»."),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd».", punct="؛"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُضَافًا", "mudaf", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى مُعَرَّفًا مَنْصُوبٌ.", "«annexed».", "«muzâf olması»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْمُعَرَّفِ", "muarraf", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«what is definite».", "«marife olana»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", [], "اللَّامِ مَجْرُورٌ.", "«by the lām».", "«lâm ile».", "اللَّامِ", punct="،"),
  nahwu(),
  NIMA(),
  FAIL_N("صَاحِبُ", "sahib", "فَاعِلُ نِعْمَ مَرْفُوعٌ، وَهُوَ مُضَافٌ إِلَى الْمُعَرَّفِ بِاللَّامِ.", "«the companion of».", "«arkadaşı».", tags=["idafa-definiteness"]),
  cited("الرَّجُلِ", "rajul", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the man».", "«adamın»."),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "Or a pronoun distinguished by a manṣūb indefinite or by مَا in the sense of «thing» — as نِعْمَ رَجُلًا زَيْدٌ, and فَنِعِمَّا هِيَ, that is, نِعْمَ شَيْئًا هِيَ." + C_EN,
 "tr": "Ya da mansûb bir nekre ile veya «şey» mânâsındaki مَا ile temyiz edilmiş bir zamir olması — نِعْمَ رَجُلًا زَيْدٌ ve فَنِعِمَّا هِيَ gibi, yani نِعْمَ شَيْئًا هِيَ." + C_TR},
 "tokens": [
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("ضَمِيرًا", "damir", "noun", ["atf-nasaq", "al-mabni-wal-mudmar"], "مَعْطُوفٌ عَلَى مُعَرَّفًا مَنْصُوبٌ.", "«a pronoun».", "«bir zamir»."),
  W("مُمَيَّزًا", "mumayyaz", "noun", ["naat-sifa", "ism-maful", "tamyiz"], "صِفَةٌ مَنْصُوبَةٌ.", "«distinguished».", "«temyiz edilmiş»."),
  bi_("بِنَكِرَةٍ", "nakira", "noun", ["tamyiz"], "نَكِرَةٍ مَجْرُورٌ.", "«by an indefinite».", "«bir nekre ile».", "نَكِرَةٍ"),
  W("مَنْصُوبَةٍ", "mansub", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«manṣūb».", "«mansûb»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  bi_("بِمَا", "ma-nakira", "pron", ["anwa-ma", "tamyiz"], "مَا فِي مَحَلِّ جَرٍّ — نَكِرَةٌ تَامَّةٌ.", "«by mā».", "«mâ ile».", "مَا"),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in the sense of».", "«mânâsındaki».", "مَعْنَى"),
  W("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«thing».", "«şey».", punct="،"),
  nahwu(),
  NIMA(ar="فِعْلٌ مَاضٍ جَامِدٌ لِلْمَدْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ يُفَسِّرُهُ التَّمْيِيزُ."),
  cited("رَجُلًا", "rajul", "noun", [K, MD, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ لِلضَّمِيرِ الْمُسْتَتِرِ.", "«as a man».", "«adam olarak»."),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd».", punct="،"),
  cited_wa("وَفَنِعِمَّا", "nima-verb", "verb", [K, MD, "anwa-ma"], "الْفَاءُ عَاطِفَةٌ، وَنِعِمَّا: نِعْمَ وَمَا النَّكِرَةُ التَّامَّةُ الْمُمَيِّزَةُ، أُدْغِمَتِ الْمِيمُ فِي الْمِيمِ.", "«and «excellent a thing it is»».", "«ve «o ne güzel şeydir»».", "فَنِعِمَّا", extra_segs=[seg("فَ", "fa", "conj"), seg("نِعِمَّ", "nima-verb", "verb"), seg("ا", "ma-nakira", "pron")]),
  cited("هِيَ", "pron-3fs-munfasil", "pron", [K, MD, "mubtada-khabar", "al-mabni-wal-mudmar"], "الْمَخْصُوصُ — مُبْتَدَأٌ مُؤَخَّرٌ فِي مَحَلِّ رَفْعٍ.", "«it» — the makhṣūṣ.", "«o» — mahsûs.", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  NIMA(ar="فِعْلٌ مَاضٍ جَامِدٌ لِلْمَدْحِ، وَالْفَاعِلُ مُسْتَتِرٌ."),
  cited("شَيْئًا", "shay", "noun", [K, MD, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — تَفْسِيرُ مَا.", "«a thing».", "«şey olarak»."),
  cited("هِيَ", "pron-3fs-munfasil", "pron", [K, MD, "mubtada-khabar"], "الْمَخْصُوصُ — مُبْتَدَأٌ مُؤَخَّرٌ.", "«it».", "«o».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And after their doer the makhṣūṣ is mentioned, and on it there are two views: for most it is a delayed mubtada and the sentence before it a fronted khabar; for some it is the khabar of a dropped mubtada, the sense being هُوَ زَيْدٌ." + C_EN,
 "tr": "Fâillerinden sonra mahsûs zikredilir ve onda iki görüş vardır: çoğunluğa göre muahhar mübtedâdır, öncesindeki cümle mukaddem haberdir; bazılarına göre mahzûf bir mübtedânın haberidir, takdir هُوَ زَيْدٌ'dür." + C_TR},
 "tokens": [
  atf_wa("وَيُذْكَرُ", "dhakara", "verb", ["naib-al-fail"], "يُذْكَرُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is mentioned».", "«ve zikredilir».", "يُذْكَرُ"),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«sonra»."),
  W("فَاعِلِهِمَا", "fail-doer", "noun", ["idafa-definiteness", "fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«their doer».", "«fâillerinden».", segments=[seg("فَاعِلِ", "fail-doer", "noun"), pr3d()]),
  W("الْمَخْصُوصُ", "makhsus", "noun", ["naib-al-fail", K, MD, "ism-maful"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the makhṣūṣ».", "«mahsûs».", punct="،"),
  atf_wa("وَفِيهِ", "fi", "prep", ["huruf-jarr", "khabar-al-mubtada-wa-ahkamuh"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and on it».", "«ve onda».", "فِيهِ", extra_segs=[seg("فِي", "fi", "prep"), pr3msi()]),
  W("قَوْلَانِ", "qawl", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two views».", "«iki görüş».", punct=":"),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْأَكْثَرِ", "akthar", "noun", ["idafa-definiteness", "ism-tafdil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«most».", "«çoğunluğa»."),
  W("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "مُبْتَدَأٌ.", "«it is».", "«o»."),
  W("مُبْتَدَأٌ", "mubtada", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a mubtada».", "«mübtedâdır»."),
  W("مُؤَخَّرٌ", "muakhkhar", "noun", ["naat-sifa", "ism-maful", "taqdim-al-musnad"], "صِفَةٌ مَرْفُوعَةٌ.", "«delayed».", "«muahhar»."),
  atf_wa("وَالْجُمْلَةُ", "jumla", "noun", ["mubtada-khabar"], "الْجُمْلَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the sentence».", "«ve cümle».", "الْجُمْلَةُ"),
  W("قَبْلَهُ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«before it».", "«öncesindeki».", segments=[seg("قَبْلَ", "qabla", "noun"), pr3ms()]),
  W("خَبَرٌ", "khabar", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a khabar».", "«haberdir»."),
  W("مُقَدَّمٌ", "muqaddam", "noun", ["naat-sifa", "ism-maful", "taqdim-al-musnad"], "صِفَةٌ مَرْفُوعَةٌ.", "«fronted».", "«mukaddem».", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("بَعْضِهِمْ", "bad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«some».", "«bazılarına».", segments=[seg("بَعْضِ", "bad", "noun"), pr3mp()]),
  W("خَبَرُ", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هُوَ، وَهُوَ مُضَافٌ.", "«the khabar of».", "«haberidir»."),
  W("مُبْتَدَإٍ", "mubtada", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a mubtada».", "«bir mübtedânın»."),
  W("مَحْذُوفٍ", "mahdhuf", "noun", ["naat-sifa", "hadhf-wa-taqdir", "ism-maful"], "صِفَةٌ مَجْرُورَةٌ.", "«dropped».", "«mahzûf».", punct="،"),
  atf_wa("وَالتَّقْدِيرُ", "taqdir", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "التَّقْدِيرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the sense being».", "«takdir».", "التَّقْدِيرُ"),
  cited("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "خَبَرٌ — الْجُمْلَةُ الْمُقَدَّرَةُ؛ هُوَ مُبْتَدَأٌ.", "«he is».", "«o»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — دَاخِلَ التَّقْدِيرِ.", "«Zayd».", "«Zeyd'dir».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And the condition of the makhṣūṣ is that it match the doer in singular, dual and plural, masculine and feminine — as نِعْمَ الرَّجُلُ زَيْدٌ, نِعْمَ الرَّجُلَانِ الزَّيْدَانِ, نِعْمَ الرِّجَالُ الزَّيْدُونَ and نِعْمَتِ الْمَرْأَةُ هِنْدٌ." + C_EN,
 "tr": "Mahsûsun şartı, müfred, tesniye, cemi, müzekker ve müenneste fâile mutâbık olmasıdır — نِعْمَ الرَّجُلُ زَيْدٌ, نِعْمَ الرَّجُلَانِ الزَّيْدَانِ, نِعْمَ الرِّجَالُ الزَّيْدُونَ ve نِعْمَتِ الْمَرْأَةُ هِنْدٌ gibi." + C_TR},
 "tokens": [
  atf_wa("وَشَرْطُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness"], "شَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the condition of».", "«ve ... şartı».", "شَرْطُ"),
  W("الْمَخْصُوصِ", "makhsus", "noun", ["idafa-definiteness", K, MD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the makhṣūṣ».", "«mahsûsun»."),
  W("مُطَابَقَتُهُ", "mutabaqa", "noun", ["mubtada-khabar", "idafa-definiteness", "form-iii-verbs"], "خَبَرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ طَابَقَ.", "«is its matching».", "«mutâbık olmasıdır».", segments=[seg("مُطَابَقَتُ", "mutabaqa", "noun"), pr3ms()]),
  li_("لِلْفَاعِلِ", "fail-doer", "noun", ["fail"], "الْفَاعِلِ مَجْرُورٌ.", "«the doer».", "«fâile».", "الْفَاعِلِ", segs=[seg("لِ", "li", "prep"), seg("لْفَاعِلِ", "fail-doer", "noun")]),
  W("إِفْرَادًا", "ifrad", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in singular».", "«müfred»."),
  atf_wa("وَتَثْنِيَةً", "tathniya", "noun", ["tamyiz", "al-muthanna"], "تَثْنِيَةً مَعْطُوفٌ مَنْصُوبٌ.", "«dual».", "«tesniye».", "تَثْنِيَةً"),
  atf_wa("وَجَمْعًا", "jam", "noun", ["tamyiz"], "جَمْعًا مَعْطُوفٌ مَنْصُوبٌ.", "«and plural».", "«ve cemi».", "جَمْعًا"),
  atf_wa("وَتَذْكِيرًا", "tadhkir", "noun", ["tamyiz"], "تَذْكِيرًا مَعْطُوفٌ مَنْصُوبٌ.", "«masculine».", "«müzekker».", "تَذْكِيرًا"),
  atf_wa("وَتَأْنِيثًا", "tanith", "noun", ["tamyiz", "al-muannath-wa-alamatuh"], "تَأْنِيثًا مَعْطُوفٌ مَنْصُوبٌ.", "«and feminine».", "«ve müennes».", "تَأْنِيثًا", punct="،"),
  nahwu(),
  NIMA(),
  FAIL_N("الرَّجُلُ", "rajul", "فَاعِلٌ مَرْفُوعٌ — مُفْرَدٌ مُذَكَّرٌ.", "«the man».", "«adam»."),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd».", punct="،"),
  cited_wa("وَنِعْمَ", "nima-verb", "verb", [K, MD], "نِعْمَ فِعْلُ مَدْحٍ جَامِدٌ.", "«and excellent are».", "«ve ne güzel».", "نِعْمَ"),
  FAIL_N("الرَّجُلَانِ", "rajul", "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى.", "«the two men».", "«iki adam».", tags=["al-muthanna"]),
  MAKH("الزَّيْدَانِ", "zayd", "«the two Zayds».", "«iki Zeyd».", punct="،", tags=["al-muthanna"]),
  cited_wa("وَنِعْمَ", "nima-verb", "verb", [K, MD], "نِعْمَ فِعْلُ مَدْحٍ جَامِدٌ.", "«and excellent are».", "«ve ne güzel».", "نِعْمَ"),
  FAIL_N("الرِّجَالُ", "rijal", "فَاعِلٌ مَرْفُوعٌ — جَمْعُ تَكْسِيرٍ.", "«the men».", "«adamlar».", tags=["jam-taksir"]),
  MAKH("الزَّيْدُونَ", "zayd", "«the Zayds».", "«Zeydler».", punct="،", tags=["jam-mudhakkar-salim"]),
  cited_wa("وَنِعْمَتِ", "nima-verb", "verb", [K, MD, "al-muannath-wa-alamatuh"], "نِعْمَتْ فِعْلُ مَدْحٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and excellent is».", "«ve ne güzel».", "نِعْمَتِ", extra_segs=[seg("نِعْمَ", "nima-verb", "verb"), seg("تِ", "ta-tanith", "part")]),
  FAIL_N("الْمَرْأَةُ", "imraa", "فَاعِلٌ مَرْفُوعٌ — مُؤَنَّثٌ.", "«the woman».", "«kadın»."),
  MAKH("هِنْدٌ", "hind", "«Hind».", "«Hind».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "As for بِئْسَ مَثَلُ الْقَوْمِ الَّذِينَ كَذَّبُوا, where the doer is singular and the makhṣūṣ plural, its taʾwīl is by supplying مَثَل — بِئْسَ مَثَلُ الْقَوْمِ مَثَلُ الَّذِينَ كَذَّبُوا — or الَّذِينَ is an attribute of الْقَوْم and the makhṣūṣ is dropped: مَثَلُهُمْ." + C_EN,
 "tr": "Fâilin müfred, mahsûsun cemi olduğu بِئْسَ مَثَلُ الْقَوْمِ الَّذِينَ كَذَّبُوا'ya gelince, te'vili مَثَل takdiriyledir — بِئْسَ مَثَلُ الْقَوْمِ مَثَلُ الَّذِينَ كَذَّبُوا — ya da الَّذِينَ, الْقَوْم'in sıfatıdır ve mahsûs mahzûftur: مَثَلُهُمْ." + C_TR},
 "tokens": [
  atf_wa("وَأَمَّا", "amma-tafsil", "part", ["amma-tafsiliyya"], "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for».", "«... gelince».", "أَمَّا"),
  cited("بِئْسَ", "bisa", "verb", [K, MD, "mubtada-khabar"], "فِعْلٌ مَاضٍ جَامِدٌ لِلذَّمِّ — الْآيَةُ مَحْكِيَّةٌ مُبْتَدَأٌ.", "«wretched is».", "«ne kötüdür»."),
  FAIL_N("مَثَلُ", "mathal", "فَاعِلُ بِئْسَ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مُفْرَدٌ.", "«the likeness of».", "«hâli».", tags=["idafa-definiteness"]),
  cited("الْقَوْمِ", "qawm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the people».", "«kavmin»."),
  cited("الَّذِينَ", "alladhina", "pron", [K, MD, "ism-mawsul", "mubtada-khabar"], "اسْمٌ مَوْصُولٌ — الْمَخْصُوصُ بِالذَّمِّ عَلَى الظَّاهِرِ، جَمْعٌ.", "«those who».", "«... olanların»."),
  cited("كَذَّبُوا", "kadhdhaba", "verb", ["ism-mawsul", "fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ، وَالْجُمْلَةُ صِلَةٌ.", "«denied».", "«yalanlayan».", punct="،"),
  atf_wa("وَالْفَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "fail", "al-hal-jumla-wa-rabituha"], "الْفَاعِلُ مُبْتَدَأٌ — الْجُمْلَةُ حَالٌ.", "«where the doer».", "«fâil».", "الْفَاعِلُ"),
  W("مُفْرَدٌ", "mufrad", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is singular».", "«müfred»."),
  atf_wa("وَالْمَخْصُوصُ", "makhsus", "noun", ["mubtada-khabar", K, MD], "الْمَخْصُوصُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the makhṣūṣ».", "«ve mahsûs».", "الْمَخْصُوصُ"),
  W("جَمْعٌ", "jam", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«plural».", "«cemidir».", punct="،"),
  W("فَتَأْوِيلُهُ", "tawil", "noun", ["mubtada-khabar", "idafa-definiteness", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَتَأْوِيلُ مُبْتَدَأٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its taʾwīl is».", "«te'vili».", segments=[seg("فَ", "fa", "conj"), seg("تَأْوِيلُ", "tawil", "noun"), pr3ms()]),
  bi_("بِتَقْدِيرِ", "taqdir", "noun", ["mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"], "تَقْدِيرِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«by supplying».", "«... takdiriyledir».", "تَقْدِيرِ"),
  cited("مَثَلٍ", "mathal", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«mathal».", "«mesel».", punct=":"),
  cited("بِئْسَ", "bisa", "verb", [K, MD], "فِعْلٌ مَاضٍ جَامِدٌ لِلذَّمِّ.", "«wretched is».", "«ne kötüdür»."),
  FAIL_N("مَثَلُ", "mathal", "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the likeness of».", "«hâli».", tags=["idafa-definiteness"]),
  cited("الْقَوْمِ", "qawm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the people».", "«kavmin»."),
  MAKH("مَثَلُ", "mathal", "«the likeness of» — the supplied makhṣūṣ.", "«hâli» — takdir edilen mahsûs.", tags=["idafa-definiteness", "hadhf-wa-taqdir"], pos="noun"),
  cited("الَّذِينَ", "alladhina", "pron", ["ism-mawsul", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«those who».", "«... olanların»."),
  cited("كَذَّبُوا", "kadhdhaba", "verb", ["ism-mawsul", "fail"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«denied».", "«yalanlayan».", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("الَّذِينَ", "alladhina", "pron", ["mubtada-khabar", "ism-mawsul"], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«alladhīna».", "«ellezîne»."),
  W("صِفَةٌ", "sifa", "noun", ["mubtada-khabar", "naat-sifa"], "خَبَرٌ مَرْفُوعٌ.", "«is an attribute».", "«sıfatıdır»."),
  li_("لِلْقَوْمِ", "qawm", "noun", ["naat-sifa"], "الْقَوْمِ مَجْرُورٌ.", "«of the people».", "«kavmin».", "الْقَوْمِ", segs=[seg("لِ", "li", "prep"), seg("لْقَوْمِ", "qawm", "noun")]),
  atf_wa("وَالْمَخْصُوصُ", "makhsus", "noun", ["mubtada-khabar", K, MD], "الْمَخْصُوصُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the makhṣūṣ».", "«ve mahsûs».", "الْمَخْصُوصُ"),
  W("مَحْذُوفٌ", "mahdhuf", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "خَبَرٌ مَرْفُوعٌ.", "«is dropped».", "«mahzûftur».", punct=":"),
  cited("مَثَلُهُمْ", "mathal", "noun", [K, MD, "mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"], "الْمَخْصُوصُ الْمُقَدَّرُ — مُبْتَدَأٌ مُؤَخَّرٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their likeness».", "«onların hâli».", punct=".", segments=[seg("مَثَلُ", "mathal", "noun"), pr3mp()]),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And the makhṣūṣ is sometimes dropped when it is known — as نِعْمَ الْعَبْدُ, that is, أَيُّوبُ; and فَنِعْمَ الْمَاهِدُونَ, that is, نَحْنُ." + C_EN,
 "tr": "Bilindiğinde mahsûs bazen hazfedilir — نِعْمَ الْعَبْدُ gibi, yani أَيُّوبُ; ve فَنِعْمَ الْمَاهِدُونَ, yani نَحْنُ." + C_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("يُحْذَفُ", "hadhafa", "verb", ["naib-al-fail", "hadhf-wa-taqdir"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is dropped».", "«hazfedilir»."),
  W("الْمَخْصُوصُ", "makhsus", "noun", ["naib-al-fail", K, MD], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the makhṣūṣ».", "«mahsûs»."),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-diğinde»."),
  W("عُلِمَ", "alima", "verb", ["idha-shartiyya", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it is known».", "«bilindiğinde».", punct="،"),
  nahwu(),
  NIMA(),
  FAIL_N("الْعَبْدُ", "abd", "فَاعِلٌ مَرْفُوعٌ — مُعَرَّفٌ بِاللَّامِ.", "«the servant».", "«kul».", punct="،"),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("أَيُّوبُ", "ayyub", "propn", [K, MD, "mubtada-khabar", "hadhf-wa-taqdir", "mamnu-min-sarf"], "الْمَخْصُوصُ الْمَحْذُوفُ — مُبْتَدَأٌ مُؤَخَّرٌ؛ وَالْقَرِينَةُ قِصَّتُهُ.", "«Job».", "«Eyyûb».", punct="؛"),
  cited_wa("وَفَنِعْمَ", "nima-verb", "verb", [K, MD], "الْفَاءُ عَاطِفَةٌ، وَنِعْمَ فِعْلُ مَدْحٍ جَامِدٌ.", "«and «excellent are»».", "«ve «ne güzel»».", "فَنِعْمَ", extra_segs=[seg("فَ", "fa", "conj"), seg("نِعْمَ", "nima-verb", "verb")]),
  FAIL_N("الْمَاهِدُونَ", "mahid", "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ — جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the spreaders».", "«döşeyenler».", punct="،", tags=["jam-mudhakkar-salim", "ism-fail"]),
  W("أَيْ", "ay-tafsir", "part", ["hadhf-wa-taqdir"], "حَرْفُ تَفْسِيرٍ.", "«that is».", "«yani»."),
  cited("نَحْنُ", "nahnu", "pron", [K, MD, "mubtada-khabar", "hadhf-wa-taqdir", "al-mabni-wal-mudmar"], "الْمَخْصُوصُ الْمَحْذُوفُ — مُبْتَدَأٌ مُؤَخَّرٌ فِي مَحَلِّ رَفْعٍ.", "«We».", "«Biz».", punct="."),
 ]})

S.append({"id": "s8", "translation": {
 "en": "And سَاءَ is like بِئْسَ in expressing blame, in its conditions and in its rulings — as وَسَاءَتْ مَصِيرًا." + C_EN,
 "tr": "سَاءَ, zem ifadesinde, şartlarında ve hükümlerinde بِئْسَ gibidir — وَسَاءَتْ مَصِيرًا gibi." + C_TR},
 "tokens": [
  cited_wa("وَسَاءَ", "saa-bad", "verb", ["mubtada-khabar", K, MD, "hollow-verbs"], "سَاءَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and sāʾa».", "«ve sâe».", "سَاءَ"),
  ka_("كَبِئْسَ", "bisa", "verb", ["mubtada-khabar", K, MD], "بِئْسَ فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«is like biʾsa».", "«bi'se gibidir».", "بِئْسَ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الذَّمِّ", "dhamm", "noun", ["huruf-jarr", MD], "مَجْرُورٌ.", "«blame».", "«zem»."),
  atf_wa("وَشُرُوطِهِ", "shart", "noun", ["atf-nasaq", "idafa-definiteness", "jam-taksir"], "شُرُوطِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ شَرْطٍ.", "«its conditions».", "«şartlarında».", "شُرُوطِ", extra_segs=[seg("شُرُوطِ", "shart", "noun"), pr3msi()]),
  atf_wa("وَأَحْكَامِهِ", "ahkam", "noun", ["atf-nasaq", "idafa-definiteness", "jam-taksir"], "أَحْكَامِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its rulings».", "«ve hükümlerinde».", "أَحْكَامِ", extra_segs=[seg("أَحْكَامِ", "ahkam", "noun"), pr3msi()], punct="،"),
  nahwu(),
  cited("وَسَاءَتْ", "saa-bad", "verb", [K, MD, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَسَاءَتْ فِعْلُ ذَمٍّ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ يُفَسِّرُهُ التَّمْيِيزُ.", "«and wretched is it».", "«ve ne kötüdür».", segments=[seg("وَ", "wa", "conj"), seg("سَاءَ", "saa-bad", "verb"), seg("تْ", "ta-tanith", "part")]),
  cited("مَصِيرًا", "masir-fate", "noun", [K, MD, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — وَالْمَخْصُوصُ مَحْذُوفٌ: جَهَنَّمُ.", "«as a destination» — the makhṣūṣ dropped.", "«varılacak yer olarak» — mahsûs mahzûf.", punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "And حَبَّذَا is for praise, and its doer is ذَا for ever, unchanging — as حَبَّذَا زَيْدٌ, حَبَّذَا الزَّيْدَانِ, حَبَّذَا الزَّيْدُونَ and حَبَّذَا هِنْدٌ; and the makhṣūṣ after it is like the makhṣūṣ of نِعْمَ." + C_EN,
 "tr": "حَبَّذَا medh içindir ve fâili daima ذَا'dır, değişmez — حَبَّذَا زَيْدٌ, حَبَّذَا الزَّيْدَانِ, حَبَّذَا الزَّيْدُونَ ve حَبَّذَا هِنْدٌ gibi; ondan sonraki mahsûs, نِعْمَ'nin mahsûsu gibidir." + C_TR},
 "tokens": [
  cited_wa("وَحَبَّذَا", "habbadha", "verb", ["mubtada-khabar", K, MD], "حَبَّذَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and ḥabbadhā».", "«ve habbezâ».", "حَبَّذَا"),
  li_("لِلْمَدْحِ", "madh", "noun", ["mubtada-khabar", MD], "الْمَدْحِ مَجْرُورٌ — خَبَرٌ.", "«is for praise».", "«medh içindir».", "الْمَدْحِ", segs=[seg("لِ", "li", "prep"), seg("لْمَدْحِ", "madh", "noun")], punct="،"),
  atf_wa("وَفَاعِلُهَا", "fail-doer", "noun", ["mubtada-khabar", "idafa-definiteness", "fail"], "فَاعِلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its doer».", "«ve fâili».", "فَاعِلُ", extra_segs=[seg("فَاعِلُ", "fail-doer", "noun"), pr3fs()]),
  cited("ذَا", "dha", "pron", ["mubtada-khabar", K, MD, "asma-al-ishara-wal-mawsulat"], "خَبَرٌ — اسْمُ إِشَارَةٍ مَحْكِيٌّ.", "«is dhā».", "«zâ'dır»."),
  W("أَبَدًا", "abadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ.", "«for ever».", "«daima»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mez»."),
  W("يَتَغَيَّرُ", "taghayyara", "verb", ["fail", "form-v-verbs", "al-hal-jumla-wa-rabituha"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ حَالٌ.", "«changing».", "«değişmez».", punct="،"),
  nahwu(),
  HABB(),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd».", punct="،"),
  cited_wa("وَحَبَّذَا", "habbadha", "verb", [K, MD, "fail"], "حَبَّذَا فِعْلُ مَدْحٍ، وَذَا فَاعِلُهُ — مُفْرَدٌ مَعَ الْمُثَنَّى.", "«and how lovely are».", "«ve ne hoştur».", "حَبَّذَا", extra_segs=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")]),
  MAKH("الزَّيْدَانِ", "zayd", "«the two Zayds».", "«iki Zeyd».", punct="،", tags=["al-muthanna"]),
  cited_wa("وَحَبَّذَا", "habbadha", "verb", [K, MD, "fail"], "حَبَّذَا فِعْلُ مَدْحٍ، وَذَا فَاعِلُهُ — مُفْرَدٌ مَعَ الْجَمْعِ.", "«and how lovely are».", "«ve ne hoştur».", "حَبَّذَا", extra_segs=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")]),
  MAKH("الزَّيْدُونَ", "zayd", "«the Zayds».", "«Zeydler».", punct="،", tags=["jam-mudhakkar-salim"]),
  cited_wa("وَحَبَّذَا", "habbadha", "verb", [K, MD, "fail"], "حَبَّذَا فِعْلُ مَدْحٍ، وَذَا فَاعِلُهُ — مُذَكَّرٌ مَعَ الْمُؤَنَّثِ.", "«and how lovely is».", "«ve ne hoştur».", "حَبَّذَا", extra_segs=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")]),
  MAKH("هِنْدٌ", "hind", "«Hind».", "«Hind».", punct="؛"),
  atf_wa("وَالْمَخْصُوصُ", "makhsus", "noun", ["mubtada-khabar", K, MD], "الْمَخْصُوصُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the makhṣūṣ».", "«ve mahsûs».", "الْمَخْصُوصُ"),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ondan sonraki».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  ka_("كَمَخْصُوصِ", "makhsus", "noun", ["mubtada-khabar", "idafa-definiteness", MD], "مَخْصُوصِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«is like the makhṣūṣ of».", "«... mahsûsu gibidir».", "مَخْصُوصِ"),
  cited("نِعْمَ", "nima-verb", "verb", ["idafa-definiteness", K, MD], "مُضَافٌ إِلَيْهِ — الْفِعْلُ مَحْكِيٌّ.", "«niʿma».", "«ni'me'nin».", punct="."),
 ]})

S.append({"id": "s10", "translation": {
 "en": "And before its makhṣūṣ or after it a tamyīz or a ḥāl agreeing with it is permitted — as حَبَّذَا رَجُلًا زَيْدٌ and حَبَّذَا زَيْدٌ رَجُلًا, and حَبَّذَا رَاكِبًا زَيْدٌ and حَبَّذَا هِنْدٌ رَاكِبَةً." + C_EN,
 "tr": "Mahsûsundan önce ya da sonra ona uygun bir temyiz veya hâl câizdir — حَبَّذَا رَجُلًا زَيْدٌ ve حَبَّذَا زَيْدٌ رَجُلًا, حَبَّذَا رَاكِبًا زَيْدٌ ve حَبَّذَا هِنْدٌ رَاكِبَةً gibi." + C_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted».", "«ve câizdir».", "يَجُوزُ"),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«önce»."),
  W("مَخْصُوصِهَا", "makhsus", "noun", ["idafa-definiteness", K, MD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its makhṣūṣ».", "«mahsûsundan».", segments=[seg("مَخْصُوصِ", "makhsus", "noun"), pr3fs()]),
  atf_wa("وَبَعْدَهُ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَعْطُوفٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«or after it».", "«ya da sonra».", "بَعْدَ", extra_segs=[seg("بَعْدَ", "bada", "noun"), pr3ms()]),
  W("تَمْيِيزٌ", "tamyiz-noun", "noun", ["fail", "tamyiz"], "فَاعِلُ يَجُوزُ مَرْفُوعٌ.", "«a tamyīz».", "«bir temyiz»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«veya»."),
  W("حَالٌ", "hal-noun", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ مَرْفُوعٌ.", "«a ḥāl».", "«hâl»."),
  W("مُوَافِقٌ", "muwafiq", "noun", ["naat-sifa", "ism-fail", "form-iii-verbs"], "صِفَةٌ مَرْفُوعَةٌ.", "«agreeing».", "«uygun»."),
  W("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«with it».", "«ona».", punct="،", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  nahwu(),
  HABB(),
  cited("رَجُلًا", "rajul", "noun", [K, MD, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ قَبْلَ الْمَخْصُوصِ.", "«as a man».", "«adam olarak»."),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd»."),
  cited_wa("وَحَبَّذَا", "habbadha", "verb", [K, MD, "fail"], "حَبَّذَا فِعْلُ مَدْحٍ، وَذَا فَاعِلُهُ.", "«and how lovely is».", "«ve ne hoştur».", "حَبَّذَا", extra_segs=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")]),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd»."),
  cited("رَجُلًا", "rajul", "noun", [K, MD, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بَعْدَ الْمَخْصُوصِ.", "«as a man».", "«adam olarak».", punct="،"),
  cited_wa("وَحَبَّذَا", "habbadha", "verb", [K, MD, "fail"], "حَبَّذَا فِعْلُ مَدْحٍ، وَذَا فَاعِلُهُ.", "«and how lovely is».", "«ve ne hoştur».", "حَبَّذَا", extra_segs=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")]),
  cited("رَاكِبًا", "rakib", "noun", [K, MD, "hal", "ism-fail"], "حَالٌ مَنْصُوبٌ قَبْلَ الْمَخْصُوصِ.", "«riding».", "«binmiş olarak»."),
  MAKH("زَيْدٌ", "zayd", "«Zayd».", "«Zeyd»."),
  cited_wa("وَحَبَّذَا", "habbadha", "verb", [K, MD, "fail"], "حَبَّذَا فِعْلُ مَدْحٍ، وَذَا فَاعِلُهُ.", "«and how lovely is».", "«ve ne hoştur».", "حَبَّذَا", extra_segs=[seg("حَبَّ", "habbadha", "verb"), seg("ذَا", "dha", "pron")]),
  MAKH("هِنْدٌ", "hind", "«Hind».", "«Hind»."),
  cited("رَاكِبَةً", "rakib", "noun", [K, MD, "hal", "ism-fail", "al-muannath-wa-alamatuh"], "حَالٌ مَنْصُوبٌ بَعْدَ الْمَخْصُوصِ — مُؤَنَّثٌ مُوَافِقٌ لَهُ.", "«riding».", "«binmiş olarak».", punct="."),
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
 "mahid": need("mahid", "مَاهِد", "م ه د", "noun", "one who spreads out, who smooths a bed — the ism fāʿil of مَهَدَ; plural مَاهِدُونَ", "döşeyen, yayan — mehede'nin ism-i fâili; cem'i مَاهِدُونَ", 4),
 "muwafiq": need("muwafiq", "مُوَافِق", "و ف ق", "noun", "agreeing, in accordance — the Form III ism fāʿil of وَافَقَ", "uygun, mutâbık — vâfeka'nın ism-i fâili", 3),
 "ma-nakira": need("ma-nakira", "مَا (النَّكِرَةُ التَّامَّةُ)", "م ا", "pron", "mā as a complete indefinite meaning «a thing» — the tamyīz of niʿma's hidden doer in نِعِمَّا", "«bir şey» mânâsında tam nekre mâ — نِعِمَّا'da ni'me'nin gizli fâilinin temyizi", 5),
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
print("kafiya ch28 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "أَفْعَالُ الْمَدْحِ وَالذَّمِّ فِي الْكَافِيَةِ", "en": "Niʿma, biʾsa, sāʾa and ḥabbadhā in the Kafiya: the three shapes of the doer, the makhṣūṣ and its two parsings, agreement and its taʾwīl, the dropped makhṣūṣ, and ḥabbadhā's frozen dhā", "tr": "Kâfiye'de ni'me, bi'se, sâe ve habbezâ: fâilin üç şekli, mahsûs ve iki i'rabı, mutâbakat ve te'vili, mahzûf mahsûs ve habbezâ'nın donmuş zâ'sı"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — أفعال المدح والذم: ما وضع لإنشاء مدح أو ذم", "ضياء صونغور اوغلى — دفتر الكافية: شروط عمل نعم وبئس الثلاثة؛ المخصوص وقولا النحاة فيه؛ المطابقة وتأويل آية الجمعة؛ حذف المخصوص إذا علم؛ ساء كبئس؛ حبذا وفاعلها ذا والتمييز والحال"],
 "question": {
  "en": ["What do these verbs do? They PERFORM praise or blame rather than report it — niʿma is not «was good», it is «how excellent!» — so they are jāmid, past in form only, and their subject is read by a different grammar.",
         "What may the doer of niʿma be? One of three: a noun wearing the article (نِعْمَ الرَّجُلُ), a noun annexed to one (نِعْمَ صَاحِبُ الرَّجُلِ), or a hidden pronoun explained by a manṣūb indefinite or by mā (نِعْمَ رَجُلًا، نِعِمَّا). Nothing else — no bare indefinite, no proper name — may sit there.",
         "What is the makhṣūṣ? The one actually praised, named after the doer: زَيْدٌ in نِعْمَ الرَّجُلُ زَيْدٌ. Most read it as a delayed mubtada with the verb-sentence as its fronted khabar; some as the khabar of a dropped هُوَ. Both are stored; neither is adjudicated.",
         "Must it agree with the doer? Yes, in number and gender — الرَّجُلَانِ الزَّيْدَانِ، الرِّجَالُ الزَّيْدُونَ، نِعْمَتِ الْمَرْأَةُ هِنْدٌ. Where the Qurʾān seems not to (بِئْسَ مَثَلُ الْقَوْمِ الَّذِينَ كَذَّبُوا), the notebook gives the two taʾwīls: a supplied مَثَلُ, or الَّذِينَ as an attribute with the makhṣūṣ dropped.",
         "May the makhṣūṣ be dropped? When known: نِعْمَ الْعَبْدُ — Job, from the story it stands in; فَنِعْمَ الْمَاهِدُونَ — We, from the clause before it. The signal that it is dropped is simply that nothing follows the doer.",
         "What about sāʾa and ḥabbadhā? سَاءَ is بِئْسَ in every rule (وَسَاءَتْ مَصِيرًا, the makhṣūṣ dropped). حَبَّذَا praises with a doer that never changes — ذَا, whether Zayd, two Zayds, the Zayds or Hind follows — and admits a tamyīz or ḥāl on either side of its makhṣūṣ.",
         "What does the engine do? The kernel's PARTICLES table knows niʿma, biʾsa, sāʾa and ḥabbadhā as jāmid verbs of praise; the analyzer reads the article-bearing noun after them as the doer and the next marfūʿ as the makhṣūṣ; the jāmid flag keeps their paradigms to the māḍī."],
  "tr": ["Bu fiiller ne yapar? Medh ya da zemmi bildirmez, İCRA eder — ni'me «iyi idi» değil «ne güzel!»dir — bu yüzden câmiddirler, yalnız şekilce mâzîdirler ve özneleri başka bir gramerle okunur.",
         "Ni'me'nin fâili ne olabilir? Üçten biri: lâm giyen bir isim (نِعْمَ الرَّجُلُ), ona muzâf bir isim (نِعْمَ صَاحِبُ الرَّجُلِ) ya da mansûb bir nekre veya mâ ile açıklanan gizli bir zamir (نِعْمَ رَجُلًا، نِعِمَّا). Başka hiçbir şey — ne çıplak nekre ne özel ad — orada duramaz.",
         "Mahsûs nedir? Asıl övülen, fâilden sonra anılan: نِعْمَ الرَّجُلُ زَيْدٌ'deki زَيْدٌ. Çoğunluk onu fiil cümlesi mukaddem haberi olan muahhar mübtedâ okur; bazıları mahzûf هُوَ'nin haberi. İkisi de saklanır; hüküm verilmez.",
         "Fâile uymalı mı? Evet, sayı ve cinste — الرَّجُلَانِ الزَّيْدَانِ، الرِّجَالُ الزَّيْدُونَ، نِعْمَتِ الْمَرْأَةُ هِنْدٌ. Kur'ân uymuyor göründüğünde (بِئْسَ مَثَلُ الْقَوْمِ الَّذِينَ كَذَّبُوا) defter iki te'vili verir: takdir edilen bir مَثَلُ ya da mahsûsu mahzûf bir sıfat olarak الَّذِينَ.",
         "Mahsûs düşebilir mi? Bilindiğinde: نِعْمَ الْعَبْدُ — içinde geçtiği kıssadan Eyyûb; فَنِعْمَ الْمَاهِدُونَ — öncesindeki cümleden Biz. Düştüğünün işareti fâilden sonra hiçbir şeyin gelmemesidir.",
         "Ya sâe ve habbezâ? سَاءَ her kuralda بِئْسَ'dir (وَسَاءَتْ مَصِيرًا, mahsûs mahzûf). حَبَّذَا hiç değişmeyen bir fâille över — ardından Zeyd, iki Zeyd, Zeydler ya da Hind gelsin ذَا — ve mahsûsunun iki yanında temyiz ya da hâl kabul eder.",
         "Motor ne yapar? Çekirdeğin PARTICLES tablosu ni'me, bi'se, sâe ve habbezâ'yı câmid medh fiilleri olarak bilir; analizör ardlarındaki lâmlı ismi fâil, sonraki merfûu mahsûs okur; câmid bayrağı çekimlerini mâzîde tutar."]},
 "plain": {
  "en": "Niʿma and biʾsa are Arabic's «what a fine…» and «what a wretched…». Their subject must wear the article or be explained by a following word, and the person really meant comes last as the makhṣūṣ. Ḥabbadhā does the same with a subject that is always dhā.",
  "tr": "Ni'me ve bi'se Arapçanın «ne güzel…» ve «ne kötü…»südür. Özneleri lâm giymeli ya da sonraki bir kelimeyle açıklanmalıdır; asıl kastedilen kişi en sonda mahsûs olarak gelir. Habbezâ aynı işi daima zâ olan bir özneyle yapar."},
 "explanation": {
  "en": "The chapter is the Kafiya's definition and the notebook's catechism. The definition sets the speech-act (inshāʾ, as in the chapter of wonder), and the notebook's question «what are the conditions of niʿma's governing?» is answered by the three admissible doers, each with its stock example — the madrasah's own list, with فَنِعِمَّا هِيَ (2:271) showing the mā that explains a hidden doer. The makhṣūṣ gets the chapter's only real dispute, and it is a dispute about iʿrāb, not meaning: a delayed mubtada or the khabar of a hidden هُوَ. The agreement rule is then stressed by the one Qurʾānic verse that appears to break it, and the two taʾwīls are given as the notebook gives them; the dropped makhṣūṣ follows with its two Qurʾānic cases and, for each, the qarīna that licenses the dropping. سَاءَ is dispatched in a line, and حَبَّذَا closes with the fact that makes it its own rule — its doer is the demonstrative ذَا and never agrees — plus the tamyīz and ḥāl that may flank its makhṣūṣ. The Iẓhār already teaches these verbs as governors; this chapter is the Kafiya's fuller account of their subject and their makhṣūṣ.",
  "tr": "Bâb, Kâfiye'nin tarifi ve defterin sual-cevabıdır. Tarif söz edimini koyar (taaccüb bâbındaki gibi inşâ) ve defterin «ni'me'nin amel şartları nelerdir?» sorusu her biri alışılmış örneğiyle üç câiz fâille cevaplanır — medresenin kendi listesi; فَنِعِمَّا هِيَ (2:271) gizli fâili açıklayan mâ'yı gösterir. Mahsûs bâbın tek gerçek ihtilâfını alır ve bu mânâ değil i'rab ihtilâfıdır: muahhar mübtedâ mı, gizli هُوَ'nin haberi mi. Mutâbakat kuralı sonra onu bozar görünen tek Kur'ân âyetiyle vurgulanır ve iki te'vil defterin verdiği gibi verilir; mahzûf mahsûs iki Kur'ânî örneği ve her biri için hazfi câiz kılan karîneyle izler. سَاءَ bir satırda geçilir; حَبَّذَا onu kendi kuralı yapan olguyla kapar — fâili işaret ismi ذَا'dır ve hiç uymaz — artı mahsûsunun iki yanına gelebilen temyiz ve hâl. İzhar bu fiilleri zaten âmil olarak öğretir; bu bâb Kâfiye'nin özneleri ve mahsûsları hakkındaki daha dolu anlatımıdır."},
 "examples": [
  {"ar": "أَفْعَالُ الْمَدْحِ وَالذَّمِّ: مَا وُضِعَ لِإِنْشَاءِ مَدْحٍ أَوْ ذَمٍّ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "نِعْمَ الرَّجُلُ زَيْدٌ — نِعْمَ صَاحِبُ الرَّجُلِ زَيْدٌ", "en": "The lām-definite doer and the annexed doer.", "tr": "Lâmlı fâil ve muzâf fâil.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "نِعْمَ رَجُلًا زَيْدٌ — فَنِعِمَّا هِيَ", "en": "The hidden doer explained by a tamyīz or by mā.", "tr": "Temyiz ya da mâ ile açıklanan gizli fâil.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "بِئْسَ مَثَلُ الْقَوْمِ مَثَلُ الَّذِينَ كَذَّبُوا", "en": "The taʾwīl of the aya.", "tr": "Âyetin te'vili.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "نِعْمَ الْعَبْدُ — فَنِعْمَ الْمَاهِدُونَ", "en": "The makhṣūṣ dropped when known.", "tr": "Bilindiğinde mahzûf mahsûs.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "حَبَّذَا الزَّيْدُونَ — حَبَّذَا هِنْدٌ رَاكِبَةً", "en": "Ḥabbadhā's frozen doer and its ḥāl.", "tr": "Habbezâ'nın donmuş fâili ve hâli.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«نِعْمَ رَجُلٌ زَيْدٌ»",
   "right": "«نِعْمَ الرَّجُلُ زَيْدٌ — ya da نِعْمَ رَجُلًا زَيْدٌ; ni'me'nin fâili çıplak nekre olamaz»",
   "why": {"en": "The doer must wear the article, be annexed to one, or be a hidden pronoun explained by a manṣūb tamyīz.", "tr": "Fâil lâm giymeli, lâmlıya muzâf olmalı ya da mansûb temyizle açıklanan gizli zamir olmalıdır."}},
  {"wrong": "«نِعْمَ الرَّجُلُ هِنْدٌ»",
   "right": "«نِعْمَتِ الْمَرْأَةُ هِنْدٌ — mahsûs fâile cinste uyar»",
   "why": {"en": "The makhṣūṣ matches the doer in number and gender.", "tr": "Mahsûs sayı ve cinste fâile uyar."}},
  {"wrong": "«حَبَّذَانِ الزَّيْدَانِ»",
   "right": "«حَبَّذَا الزَّيْدَانِ — zâ hiç değişmez»",
   "why": {"en": "Ḥabbadhā's doer is the frozen demonstrative, whatever follows.", "tr": "Habbezâ'nın fâili donmuş işaret ismidir, ardından ne gelirse gelsin."}},
  {"wrong": "«زَيْدٌ, نِعْمَ الرَّجُلُ زَيْدٌ'da fâildir»",
   "right": "«الرَّجُلُ fâil, زَيْدٌ mahsûstur — muahhar mübtedâ»",
   "why": {"en": "The doer is the article-bearing noun; the name after it is the one praised.", "tr": "Fâil lâmlı isimdir; ardındaki ad övülendir."}}],
 "relatedNotes": [MD, "fil-al-taajjub-fil-kafiya", "tamyiz", "hal", "al-muthanna"]}

ADD_EN = (" Chapter 28 (notebook lines ~325-331): the verbs of praise and blame defined in the notebook's own Arabic (s1); the three doers, the makhṣūṣ and its parsings, agreement and the taʾwīl of 62:5, the dropped makhṣūṣ (2:271, 38:44, 51:48), سَاءَ (4:97) and حَبَّذَا — the notebook's exposition, kept as commentary (s2-s10). Qurʾānic text as the source prints it.")
ADD_TR = (" Yirmi sekizinci bâb (defter satırları ~325-331): medh ve zem fiilleri defterin kendi Arapçasıyla tarif edilir (s1); üç fâil, mahsûs ve i'rabları, mutâbakat ve 62:5'in te'vili, mahzûf mahsûs (2:271, 38:44, 51:48), سَاءَ (4:97) ve حَبَّذَا — defterin açıklaması, şerh olarak (s2-s10). Kur'ân metni kaynağın bastığı gibi.")
write_out(28, S, TITLE, ADD_EN, ADD_TR, "325-331", GLOSS_ADD, notes=(NOTE,),
          related=((MD, [K]), ("fil-al-taajjub-fil-kafiya", [K])))
report(28, S, GLOSS_ADD, (NOTE,))
