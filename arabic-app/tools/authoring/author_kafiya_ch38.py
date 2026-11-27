# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 38: THE COORDINATION LETTERS (II) — أَوْ, إِمَّا and أَمْ for one of two things undetermined for the speaker; أَمْ
joined (after the hamza of question, asking for the determination; أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا barred by the author, allowed by
Sībawayh; answered by naming, not by yes or no) and أَمْ detached (like بَلْ, then like the hamza: إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ); إِمَّا must be
preceded by إِمَّا, أَوْ may be; لَا, بَلْ and لَكِنْ for one determined thing; and the letters of alerting أَلَا, أَمَا, هَا.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~342-344 of the transcription.

  COMMENTARY (the notebook): s1-s9 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch38.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "aw-imma-am-la-bal-lakin-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الْعَطْفِ: أَوْ وَإِمَّا وَأَمْ وَلَا وَبَلْ وَلَكِنْ، وَحُرُوفُ التَّنْبِيهِ", "en": "The coordination letters — aw, immā, am; lā, bal, lākin — and the letters of alerting", "tr": "Atıf harfleri — ev, immâ, em; lâ, bel, lâkin — ve tenbih harfleri"}
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

AT = "atf-nasaq"
def LET(full, lex, en, tr, wa=True, punct=None, pos="conj"):
    if wa: return cited_wa("وَ" + full, lex, pos, ["mubtada-khabar", K, AT], full + " لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, full, punct=punct)
    return cited(full, lex, pos, ["mubtada-khabar", K, AT], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, punct=punct)
def FOR(full, lex, en, tr, inner, punct=None, segs=None, tags=()):
    return li_(full, lex, "noun", ["mubtada-khabar", K] + list(tags), inner + " مَجْرُورٌ — خَبَرٌ.", en, tr, inner, punct=punct, segs=segs)
def JAANI(): return cited("جَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), pr1s()])
def ZAYD_F(): return cited("زَيْدٌ", "zayd", "propn", ["fail", AT], "فَاعِلٌ مَرْفُوعٌ — الْمَعْطُوفُ عَلَيْهِ.", "«Zayd».", "«Zeyd».")
def AMR_M(ar, en="«ʿAmr».", tr="«Amr».", punct="."): return cited("عَمْرٌو", "amr-name", "propn", [K, AT], "مَعْطُوفٌ مَرْفُوعٌ — " + ar, en, tr, punct=punct)
def LETC(full, lex, ar, en, tr, pos="conj"): return cited(full, lex, pos, [K, AT], ar, en, tr)

S.append({"id": "s1", "translation": {
 "en": "And أَوْ, إِمَّا and أَمْ are for one of two things that is undetermined for the speaker — as جَاءَنِي زَيْدٌ أَوْ عَمْرٌو, جَاءَنِي زَيْدٌ أَمْ عَمْرٌو, and جَاءَنِي إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو." + C_EN,
 "tr": "أَوْ, إِمَّا ve أَمْ, mütekellim nezdinde muayyen olmayan iki işten biri içindir — جَاءَنِي زَيْدٌ أَوْ عَمْرٌو, جَاءَنِي زَيْدٌ أَمْ عَمْرٌو ve جَاءَنِي إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو gibi." + C_TR},
 "tokens": [
  LET("أَوْ", "aw", "«and aw».", "«ve ev»."),
  cited_wa("وَإِمَّا", "imma", "part", [K, AT], "إِمَّا مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«immā».", "«immâ».", "إِمَّا"),
  cited_wa("وَأَمْ", "am", "part", [K, AT], "أَمْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and am».", "«ve em».", "أَمْ"),
  li_("لِأَحَدِ", "ahad", "noun", ["mubtada-khabar", "idafa-definiteness", K], "أَحَدِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«are for one of».", "«... biri içindir».", "أَحَدِ"),
  W("أَمْرَيْنِ", "amr", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two things».", "«iki işten»."),
  W("مُبْهَمٍ", "mubham", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ لِأَحَدِ مَجْرُورَةٌ.", "«undetermined».", "«muayyen olmayan»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«nezdinde»."),
  W("الْمُتَكَلِّمِ", "mutakallim", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker».", "«mütekellim».", punct="،"),
  nahwu(),
  JAANI(), ZAYD_F(),
  LETC("أَوْ", "aw", "حَرْفُ عَطْفٍ لِأَحَدِ الْأَمْرَيْنِ.", "«or».", "«ya da»."),
  AMR_M("بِأَوْ.", punct="،"),
  cited_wa("وَجَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and came to me».", "«ve bana geldi».", "جَاءَنِي", extra_segs=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  ZAYD_F(),
  LETC("أَمْ", "am", "حَرْفُ عَطْفٍ لِأَحَدِ الْأَمْرَيْنِ.", "«or».", "«yoksa».", pos="part"),
  AMR_M("بِأَمْ.", punct="،"),
  cited_wa("وَجَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and came to me».", "«ve bana geldi».", "جَاءَنِي", extra_segs=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  LETC("إِمَّا", "imma", "إِمَّا الْأُولَى — لِلتَّفْصِيلِ، لَيْسَتْ عَاطِفَةً.", "«either».", "«ya».", pos="part"),
  ZAYD_F(),
  cited_wa("وَإِمَّا", "imma", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا الثَّانِيَةُ لِأَحَدِ الْأَمْرَيْنِ.", "«or».", "«ya da».", "إِمَّا"),
  AMR_M("بِالْوَاوِ، وَإِمَّا تُفِيدُ أَحَدَ الْأَمْرَيْنِ."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And أَمْ is of two kinds: joined and detached. The joined أَمْ is for one of two equal things — after one of them has become established for the speaker, to ask the hearer to determine it — one of the two equals following the joined أَمْ and the other following the hamza of question; so the joined أَمْ needs the hamza of question and is not used without it." + C_EN,
 "tr": "أَمْ iki kısımdır: muttasıl ve munkatı. Muttasıl أَمْ, iki müsâvîden biri mütekellim nezdinde sabit olduktan sonra muhataptan tayinini istemek içindir — iki müsâvîden biri muttasıl أَمْ'i, öteki istifham hemzesini takip eder; bu yüzden muttasıl أَمْ istifham hemzesine muhtaçtır ve onsuz kullanılmaz." + C_TR},
 "tokens": [
  cited_wa("وَأَمْ", "am", "part", ["mubtada-khabar", K, AT], "أَمْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and am».", "«ve em».", "أَمْ"),
  W("قِسْمَانِ", "qism", "noun", ["mubtada-khabar", "al-muthanna"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«is of two kinds».", "«iki kısımdır».", punct=":"),
  W("مُتَّصِلَةٌ", "muttasil", "noun", ["badal", "ism-fail", "form-viii-verbs"], "بَدَلٌ مِنْ قِسْمَانِ مَرْفُوعٌ.", "«joined».", "«muttasıl»."),
  atf_wa("وَمُنْقَطِعَةٌ", "munqati", "noun", [AT, "ism-fail", "form-vii-verbs"], "مُنْقَطِعَةٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and detached».", "«ve munkatı».", "مُنْقَطِعَةٌ", punct="."),
  W("فَالْمُتَّصِلَةُ", "muttasil", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْصِيلِ، وَالْمُتَّصِلَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the joined».", "«muttasıl».", segments=[seg("فَ", "fa", "conj"), seg("الْمُتَّصِلَةُ", "muttasil", "noun")]),
  li_("لِأَحَدِ", "ahad", "noun", ["mubtada-khabar", "idafa-definiteness", K], "أَحَدِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is for one of».", "«... biri içindir».", "أَحَدِ"),
  W("الْمُتَسَاوِيَيْنِ", "mutasawin", "noun", ["idafa-definiteness", "al-muthanna", "ism-fail", "form-vi-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two equal things».", "«iki müsâvîden»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... sonra»."),
  W("ثُبُوتِ", "thubut", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the establishing of».", "«sabit olduktan»."),
  W("أَحَدِهِمَا", "ahad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of them».", "«biri».", segments=[seg("أَحَدِ", "ahad", "noun"), pr3d()]),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«nezdinde»."),
  W("الْمُتَكَلِّمِ", "mutakallim", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker».", "«mütekellim».", punct="،"),
  li_("لِطَلَبِ", "talab", "noun", ["idafa-definiteness", "lam-taleel"], "طَلَبِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to ask».", "«istemek için».", "طَلَبِ"),
  W("تَعْيِينِهِ", "tayin", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its determination».", "«tayinini».", segments=[seg("تَعْيِينِ", "tayin", "noun"), pr3msi()]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-tan»."),
  W("الْمُخَاطَبِ", "mukhatab", "noun", ["huruf-jarr", "ism-maful"], "مَجْرُورٌ.", "«the hearer».", "«muhataptan».", punct="—"),
  W("يَتْبَعُ", "tabia-follow", "verb", ["fail", "al-hal-jumla-wa-rabituha"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — الْجُمْلَةُ حَالٌ.", "«following».", "«takip eder»."),
  W("أَحَدُ", "ahad", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«one of».", "«biri»."),
  W("الْمُتَسَاوِيَيْنِ", "mutasawin", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two equals».", "«iki müsâvîden»."),
  cited("أَمِ", "am", "part", ["maful-bihi", AT], "مَفْعُولٌ بِهِ — الْحَرْفُ مَحْكِيٌّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«the am».", "«em'i»."),
  W("الْمُتَّصِلَةَ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«joined».", "«muttasıl»."),
  atf_wa("وَالْآخَرُ", "akhar", "noun", ["mubtada-khabar"], "الْآخَرُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the other».", "«öteki».", "الْآخَرُ"),
  W("هَمْزَةَ", "hamza-letter", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: يَتْبَعُ، وَهُوَ مُضَافٌ.", "«the hamza of».", "«hemzesini»."),
  W("الِاسْتِفْهَامِ", "istifham", "noun", ["idafa-definiteness", "adawat-al-tasawwur"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«question».", "«istifham».", punct="؛"),
  W("فَأَمِ", "am", "part", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada", AT], "الْفَاءُ لِلتَّفْرِيعِ، وَأَمِ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so the am».", "«bu yüzden em».", segments=[seg("فَ", "fa", "conj"), seg("أَمِ", "am", "part")]),
  W("الْمُتَّصِلَةُ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«joined».", "«muttasıl»."),
  W("تَحْتَاجُ", "ihtaja", "verb", ["mubtada-khabar", "fail", "form-viii-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«needs».", "«muhtaçtır»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«-».", "«-e»."),
  W("هَمْزَةِ", "hamza-letter", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the hamza of».", "«hemzesine»."),
  W("الِاسْتِفْهَامِ", "istifham", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«question».", "«istifham»."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... -maz».", "لَا"),
  W("تُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is used».", "«kullanılmaz»."),
  bi_("بِدُونِهَا", "dun", "noun", ["idafa-definiteness"], "دُونِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«without it».", "«onsuz».", "دُونِ", segs=[seg("بِ", "bi", "prep"), seg("دُونِ", "dun", "noun"), pr3fs()], punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "For this reason أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا is not permitted according to the author — for though one of the two equals follows the joined أَمْ, the other does not follow the hamza of question; but according to Sībawayh أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا is permitted and good, though أَزَيْدًا رَأَيْتَ أَمْ عَمْرًا is better." + C_EN,
 "tr": "Bu sebeple أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا musannife göre câiz değildir — zira iki müsâvîden biri muttasıl أَمْ'i takip etmişse de öteki istifham hemzesini takip etmemiştir; fakat Sîbeveyh'e göre أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا câizdir ve güzeldir, ancak أَزَيْدًا رَأَيْتَ أَمْ عَمْرًا daha güzeldir." + C_TR},
 "tokens": [
  W("فَلِذَلِكَ", "dhalika", "pron", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada", "asma-al-ishara-wal-mawsulat"], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ لِلتَّعْلِيلِ، وَذَلِكَ فِي مَحَلِّ جَرٍّ.", "«for this reason».", "«bu sebeple».", segments=[seg("فَ", "fa", "conj"), seg("لِ", "lam-taleel", "part"), seg("ذَلِكَ", "dhalika", "pron")]),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«... değildir»."),
  W("يَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«is permitted».", "«câiz»."),
  cited("أَرَأَيْتَ", "raa", "verb", ["fail", "adawat-al-tasawwur"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَرَأَيْتَ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْجُمْلَةُ مَحْكِيَّةٌ فَاعِلُ يَجُوزُ.", "«did you see».", "«gördün mü».", segments=[seg("أَ", "hamza-istifham", "part"), seg("رَأَيْ", "raa", "verb"), prTa()]),
  cited("زَيْدًا", "zayd", "propn", ["maful-bihi", AT], "مَفْعُولٌ بِهِ مَنْصُوبٌ — لَمْ يَلِ الْهَمْزَةَ.", "«Zayd».", "«Zeyd'i»."),
  LETC("أَمْ", "am", "حَرْفُ عَطْفٍ مُتَّصِلَةٌ.", "«or».", "«yoksa».", pos="part"),
  cited("عَمْرًا", "amr-name", "propn", [K, AT], "مَعْطُوفٌ مَنْصُوبٌ.", "«ʿAmr».", "«Amr'ı»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«according to».", "«... göre»."),
  W("الْمُصَنِّفِ", "musannif", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the author».", "«musannife».", punct="—"),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«zira».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("أَحَدَ", "ahad", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«one of».", "«biri»."),
  W("الْمُتَسَاوِيَيْنِ", "mutasawin", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two equals».", "«iki müsâvîden»."),
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "الْوَاوُ حَالِيَّةٌ، وَإِنْ وَصْلِيَّةٌ.", "«though».", "«... -se de».", "إِنْ"),
  W("تَبِعَ", "tabia-follow", "verb", ["in-shartiyya", "fail"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ.", "«follows».", "«takip etmişse»."),
  cited("أَمِ", "am", "part", ["maful-bihi", AT], "مَفْعُولٌ بِهِ — الْحَرْفُ مَحْكِيٌّ.", "«the am».", "«em'i»."),
  W("الْمُتَّصِلَةَ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«joined».", "«muttasıl».", punct="،"),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-me-»."),
  W("يَتْبَعِ", "tabia-follow", "verb", ["nawasib-wa-jawazim-al-mudari", "fail", "inna-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ — الْجُمْلَةُ خَبَرُ أَنَّ.", "«does follow».", "«takip etmemiştir»."),
  W("الْآخَرُ", "akhar", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the other».", "«öteki»."),
  W("هَمْزَةَ", "hamza-letter", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the hamza of».", "«hemzesini»."),
  W("الِاسْتِفْهَامِ", "istifham", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«question».", "«istifham».", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«but according to».", "«fakat ... göre».", "عِنْدَ"),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ.", "«Sībawayh».", "«Sîbeveyh'e»."),
  cited("أَرَأَيْتَ", "raa", "verb", ["mubtada-khabar", "fail"], "الْجُمْلَةُ مَحْكِيَّةٌ مُبْتَدَأٌ مُؤَخَّرٌ.", "«did you see».", "«gördün mü».", segments=[seg("أَ", "hamza-istifham", "part"), seg("رَأَيْ", "raa", "verb"), prTa()]),
  cited("زَيْدًا", "zayd", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd».", "«Zeyd'i»."),
  LETC("أَمْ", "am", "حَرْفُ عَطْفٍ.", "«or».", "«yoksa».", pos="part"),
  cited("عَمْرًا", "amr-name", "propn", [AT], "مَعْطُوفٌ مَنْصُوبٌ.", "«ʿAmr».", "«Amr'ı»."),
  W("جَائِزٌ", "jaiz", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هُوَ.", "«is permitted».", "«câizdir»."),
  W("حَسَنٌ", "hasan-good", "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ ثَانٍ مَرْفُوعٌ.", "«and good».", "«ve güzeldir».", punct="،"),
  W("لَكِنْ", "lakin", "part", [AT, "atf-nasaq"], "حَرْفُ اسْتِدْرَاكٍ.", "«though».", "«ancak»."),
  cited("أَزَيْدًا", "zayd", "propn", ["mubtada-khabar", "maful-bihi", "taqdim-al-musnad"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدًا مَفْعُولٌ بِهِ مُقَدَّمٌ — يَلِي الْهَمْزَةَ؛ الْجُمْلَةُ مُبْتَدَأٌ.", "«was it Zayd».", "«Zeyd'i mi».", segments=[seg("أَ", "hamza-istifham", "part"), seg("زَيْدًا", "zayd", "propn")]),
  cited("رَأَيْتَ", "raa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you saw».", "«gördün».", segments=[seg("رَأَيْ", "raa", "verb"), prTa()]),
  LETC("أَمْ", "am", "حَرْفُ عَطْفٍ مُتَّصِلَةٌ.", "«or».", "«yoksa».", pos="part"),
  cited("عَمْرًا", "amr-name", "propn", [AT], "مَعْطُوفٌ مَنْصُوبٌ — يَلِي أَمْ.", "«ʿAmr».", "«Amr'ı»."),
  W("أَحْسَنُ", "ahsan", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«is better».", "«daha güzeldir».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And for the same reason the answer to the joined أَمْ is by determining one of the two things, not by نَعَمْ or لَا: to أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو one does not say نَعَمْ or لَا, but زَيْدٌ or عَمْرٌو." + C_EN,
 "tr": "Yine bu sebeple muttasıl أَمْ'in cevabı iki şeyden birini tayin iledir, نَعَمْ ya da لَا ile değil: أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو'ya نَعَمْ ya da لَا denmez, زَيْدٌ ya da عَمْرٌو denir." + C_TR},
 "tokens": [
  atf_wa("وَلِذَلِكَ", "dhalika", "pron", ["huruf-jarr", "asma-al-ishara-wal-mawsulat"], "اللَّامُ لِلتَّعْلِيلِ، وَذَلِكَ فِي مَحَلِّ جَرٍّ.", "«and for the same reason».", "«ve bu sebeple».", "ذَلِكَ", extra_segs=[seg("لِ", "lam-taleel", "part"), seg("ذَلِكَ", "dhalika", "pron")]),
  W("جَوَابُ", "jawab", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the answer to».", "«cevabı»."),
  cited("أَمِ", "am", "part", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«the am».", "«em'in»."),
  W("الْمُتَّصِلَةِ", "muttasil", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«joined».", "«muttasıl»."),
  bi_("بِتَعْيِينِ", "tayin", "noun", ["mubtada-khabar", "idafa-definiteness"], "تَعْيِينِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is by determining».", "«tayin iledir».", "تَعْيِينِ"),
  W("أَحَدِ", "ahad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«one of».", "«birini»."),
  W("الْأَمْرَيْنِ", "amr", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two things».", "«iki şeyden».", punct="،"),
  W("لَا", "la-nafiya", "part", ["la-nafiya", AT], "عَاطِفَةٌ لِلنَّفْيِ.", "«not».", "«... değil»."),
  bi_("بِنَعَمْ", "naam", "part", [AT], "نَعَمْ فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«by yes».", "«evet ile».", "نَعَمْ"),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("لَا", "la", "part", [AT], "مَعْطُوفٌ — حَرْفُ جَوَابٍ مَحْكِيٌّ.", "«no».", "«hayır».", punct=":"),
  W("فَفِي", "fi", "prep", ["huruf-jarr", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَفِي حَرْفُ جَرٍّ.", "«to».", "«-ya».", segments=[seg("فَ", "fa", "conj"), seg("فِي", "fi", "prep")]),
  cited("أَزَيْدٌ", "zayd", "propn", ["huruf-jarr", "mubtada-khabar"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدٌ مُبْتَدَأٌ — الْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«is Zayd».", "«Zeyd mi».", segments=[seg("أَ", "hamza-istifham", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  cited("عِنْدَكَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«with you».", "«yanında».", segments=[seg("عِنْدَ", "inda", "noun"), pr2ms()]),
  LETC("أَمْ", "am", "حَرْفُ عَطْفٍ مُتَّصِلَةٌ.", "«or».", "«yoksa».", pos="part"),
  AMR_M("بِأَمِ الْمُتَّصِلَةِ.", punct="،"),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-mez»."),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«does one say».", "«denmez»."),
  cited("نَعَمْ", "naam", "part", ["naib-al-fail"], "نَائِبُ فَاعِلٍ — الْحَرْفُ مَحْكِيٌّ.", "«yes».", "«evet»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("لَا", "la", "part", [AT], "مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«no».", "«hayır».", punct="،"),
  W("بَلْ", "bal", "conj", [AT, K], "حَرْفُ إِضْرَابٍ وَعَطْفٍ.", "«but».", "«bilakis»."),
  cited("زَيْدٌ", "zayd", "propn", ["naib-al-fail"], "نَائِبُ فَاعِلٍ لِيُقَالُ مَحْذُوفًا — اللَّفْظُ مَحْكِيٌّ.", "«Zayd».", "«Zeyd»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  cited("عَمْرٌو", "amr-name", "propn", [AT], "مَعْطُوفٌ مَرْفُوعٌ — اللَّفْظُ مَحْكِيٌّ.", "«ʿAmr».", "«Amr».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And the detached أَمْ is like بَلْ in turning away from the first, and like the hamza in expressing doubt about the second — as إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ: the speaker first said «they are surely camels», then, seeing they were not camels, turned away from that report and said «or are they sheep?», expressing doubt in the second too." + C_EN,
 "tr": "Munkatı أَمْ, birincisinden i'râzda بَلْ gibi, ikincisinde şek ifade etmekte hemze gibidir — إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ gibi: mütekellim önce «onlar elbette devedir» demiş, sonra deve olmadıklarını anlayınca o haberden vazgeçip «yoksa koyun mu?» diyerek ikinci cümlede de şüphede olduğunu bildirmiştir." + C_TR},
 "tokens": [
  atf_wa("وَالْمُنْقَطِعَةُ", "munqati", "noun", ["mubtada-khabar", K, AT], "الْمُنْقَطِعَةُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the detached».", "«ve munkatı».", "الْمُنْقَطِعَةُ"),
  ka_("كَبَلْ", "bal", "conj", ["mubtada-khabar", AT], "بَلْ فِي مَحَلِّ جَرٍّ — خَبَرٌ.", "«is like bal».", "«bel gibidir».", "بَلْ"),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الْإِضْرَابِ", "idrab", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«turning away».", "«i'râzda»."),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  W("الْأَوَّلِ", "awwal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the first».", "«birincisinden».", punct="،"),
  atf_wa("وَكَالْهَمْزَةِ", "hamza-letter", "noun", [AT, "huruf-jarr"], "الْكَافُ حَرْفُ جَرٍّ، وَالْهَمْزَةِ مَجْرُورٌ — مَعْطُوفٌ عَلَى الْخَبَرِ.", "«and like the hamza».", "«ve hemze gibi».", "الْهَمْزَةِ", extra_segs=[seg("كَ", "ka", "part"), seg("الْهَمْزَةِ", "hamza-letter", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-te»."),
  W("إِفَادَةِ", "ifada", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«expressing».", "«ifade etmekte»."),
  W("الشَّكِّ", "shakk", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«doubt».", "«şek»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«about».", "«-de»."),
  W("الثَّانِي", "thani", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second».", "«ikincisinde».", punct="،"),
  nahwu(),
  cited("إِنَّهَا", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«they are surely».", "«onlar elbette».", segments=[seg("إِنَّ", "inna", "part"), pr3fs()]),
  cited("لَإِبِلٌ", "ibil", "noun", ["inna-wa-akhawatuha"], "اللَّامُ الْمُزَحْلَقَةُ، وَإِبِلٌ خَبَرُ إِنَّ مَرْفُوعٌ.", "«camels».", "«devedir».", segments=[seg("لَ", "lam-ibtida", "part"), seg("إِبِلٌ", "ibil", "noun")]),
  LETC("أَمْ", "am", "أَمِ الْمُنْقَطِعَةُ — بِمَعْنَى بَلْ وَالْهَمْزَةِ.", "«or rather».", "«yoksa».", pos="part"),
  cited("شَاةٌ", "shat", "noun", ["mubtada-khabar", K, AT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: بَلْ أَهِيَ شَاةٌ.", "«are they sheep?».", "«koyun mu?».", punct=":"),
  W("قَالَ", "qala", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«said».", "«dedi»."),
  W("الْمُتَكَلِّمُ", "mutakallim", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the speaker».", "«mütekellim»."),
  W("أَوَّلًا", "awwalan", "adv", ["maful-fih"], "ظَرْفٌ مَنْصُوبٌ.", "«first».", "«önce»."),
  cited("إِنَّهَا", "inna", "part", ["maful-bihi"], "الْمَقُولُ — فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«they are surely».", "«onlar elbette».", segments=[seg("إِنَّ", "inna", "part"), pr3fs()]),
  cited("لَإِبِلٌ", "ibil", "noun", ["inna-wa-akhawatuha"], "اللَّامُ الْمُزَحْلَقَةُ، وَإِبِلٌ خَبَرُ إِنَّ.", "«camels».", "«devedir».", punct="،", segments=[seg("لَ", "lam-ibtida", "part"), seg("إِبِلٌ", "ibil", "noun")]),
  W("ثُمَّ", "thumma", "conj", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then».", "«sonra»."),
  W("لَمَّا", "lamma", "part", ["maful-fih", "al-majzum-wal-shart-wal-jaza"], "ظَرْفٌ بِمَعْنَى حِينَ.", "«when».", "«-ınca»."),
  W("رَأَى", "raa", "verb", ["fail", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«he saw».", "«anlayınca»."),
  W("أَنَّهَا", "anna", "part", ["inna-wa-akhawatuha"], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا — وَالْمَصْدَرُ مَفْعُولُ رَأَى.", "«that they».", "«onların».", segments=[seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("لَيْسَتْ", "laysa", "verb", ["inna-wa-akhawatuha", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ — الْجُمْلَةُ خَبَرُ أَنَّ.", "«were not».", "«olmadıklarını».", segments=[seg("لَيْسَ", "laysa", "verb"), seg("تْ", "ta-tanith", "part")]),
  bi_("بِإِبِلٍ", "ibil", "noun", ["kana-wa-akhawatuha"], "إِبِلٍ مَجْرُورٌ لَفْظًا خَبَرُ لَيْسَتْ — الْبَاءُ زَائِدَةٌ.", "«camels».", "«deve».", "إِبِلٍ", punct="،"),
  W("أَضْرَبَ", "adraba", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ — جَوَابُ لَمَّا.", "«turned away».", "«vazgeçti»."),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الْخَبَرِ", "khabar", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the report».", "«haberden»."),
  W("الْأَوَّلِ", "awwal", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«first».", "«ilk»."),
  atf_wa("وَقَالَ", "qala", "verb", ["fail", "hollow-verbs"], "قَالَ فِعْلٌ مَاضٍ.", "«and said».", "«ve dedi».", "قَالَ"),
  cited("أَمْ", "am", "part", ["maful-bihi", AT], "الْمَقُولُ — أَمِ الْمُنْقَطِعَةُ.", "«or».", "«yoksa»."),
  cited("شَاةٌ", "shat", "noun", ["mubtada-khabar"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«sheep?».", "«koyun mu?».", punct="،"),
  W("مُفِيدًا", "mufid", "noun", ["hal", "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ.", "«expressing».", "«bildirerek»."),
  W("الشَّكَّ", "shakk", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ مَنْصُوبٌ.", "«doubt».", "«şüpheyi»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الثَّانِي", "thani", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second».", "«ikincisinde»."),
  W("أَيْضًا", "aydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ.", "«too».", "«de».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And when coordinating with إِمَّا, another إِمَّا must come before what it is joined to — as جَاءَنِي إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو; and when coordinating with أَوْ, the coming of إِمَّا is allowed — جَاءَنِي إِمَّا زَيْدٌ أَوْ عَمْرٌو is permitted, and so is جَاءَنِي زَيْدٌ أَوْ عَمْرٌو." + C_EN,
 "tr": "إِمَّا ile atıf yapılacağı zaman ma'tûfun aleyhten önce başka bir إِمَّا'nın gelmesi lâzımdır — جَاءَنِي إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو gibi; أَوْ ile atıf yapılacağı zaman إِمَّا'nın gelmesi câizdir — جَاءَنِي إِمَّا زَيْدٌ أَوْ عَمْرٌو câizdir, جَاءَنِي زَيْدٌ أَوْ عَمْرٌو da câizdir." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... zaman».", "إِذَا"),
  W("عُطِفَ", "atafa", "verb", ["idha-shartiyya", "naib-al-fail", AT], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«coordinating».", "«atıf yapılacağı»."),
  bi_("بِإِمَّا", "imma", "part", [K, AT], "إِمَّا فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«with immā».", "«immâ ile».", "إِمَّا"),
  W("لَزِمَ", "lazima", "verb", ["fail", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ — جَوَابُ إِذَا.", "«must».", "«lâzımdır»."),
  W("مَجِيءُ", "maji", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the coming of».", "«gelmesi»."),
  cited("إِمَّا", "imma", "part", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«immā».", "«immâ'nın»."),
  W("أُخْرَى", "ukhra", "noun", ["naat-sifa", "ism-maqsur-manqus", "mamnu-min-sarf"], "صِفَةٌ لِإِمَّا مَجْرُورَةٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«another».", "«başka bir»."),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«-ten önce»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«what it is joined».", "«ma'tûfun»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to».", "«aleyhten».", punct="،", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  nahwu(),
  JAANI(),
  LETC("إِمَّا", "imma", "إِمَّا الْأُولَى لِلتَّفْصِيلِ.", "«either».", "«ya».", pos="part"),
  ZAYD_F(),
  cited_wa("وَإِمَّا", "imma", "part", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَإِمَّا الثَّانِيَةُ.", "«or».", "«ya da».", "إِمَّا"),
  AMR_M("بِالْوَاوِ مَعَ إِمَّا.", punct="؛"),
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... zaman».", "إِذَا"),
  W("عُطِفَ", "atafa", "verb", ["idha-shartiyya", "naib-al-fail", AT], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«coordinating».", "«atıf yapılacağı»."),
  bi_("بِأَوْ", "aw", "conj", [K, AT], "أَوْ فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«with aw».", "«ev ile».", "أَوْ"),
  W("جَازَ", "jaaza", "verb", ["fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ — جَوَابُ إِذَا.", "«is allowed».", "«câizdir»."),
  W("مَجِيءُ", "maji", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the coming of».", "«gelmesi»."),
  cited("إِمَّا", "imma", "part", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«immā».", "«immâ'nın».", punct="—"),
  JAANI(),
  LETC("إِمَّا", "imma", "إِمَّا لِلتَّفْصِيلِ.", "«either».", "«ya».", pos="part"),
  ZAYD_F(),
  LETC("أَوْ", "aw", "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  AMR_M("بِأَوْ بَعْدَ إِمَّا.", punct="،"),
  W("جَائِزٌ", "jaiz", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«is permitted».", "«câizdir».", punct="،"),
  cited_wa("وَجَاءَنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and came to me».", "«ve bana geldi».", "جَاءَنِي", extra_segs=[seg("جَاءَ", "jaa", "verb"), pr1s()]),
  ZAYD_F(),
  LETC("أَوْ", "aw", "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  AMR_M("بِأَوْ بِلَا إِمَّا.", punct="،"),
  W("جَائِزٌ", "jaiz", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ.", "«is permitted».", "«câizdir».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And لَا, بَلْ and لَكِنْ are for one of two things that is determined for the speaker. لَا is to deny of the coordinate the ruling established for what it is joined to — as جَاءَنِي زَيْدٌ لَا عَمْرٌو." + C_EN,
 "tr": "لَا, بَلْ ve لَكِنْ, mütekellim nezdinde muayyen olan iki işten biri içindir. لَا, ma'tûfun aleyh için sabit olan hükmü ma'tûftan nefyetmek içindir — جَاءَنِي زَيْدٌ لَا عَمْرٌو gibi." + C_TR},
 "tokens": [
  cited_wa("وَلَا", "la-nafiya", "part", ["mubtada-khabar", K, AT], "لَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and lā».", "«ve lâ».", "لَا"),
  cited_wa("وَبَلْ", "bal", "conj", [K, AT], "بَلْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«bal».", "«bel».", "بَلْ"),
  cited_wa("وَلَكِنْ", "lakin", "part", [K, AT], "لَكِنْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and lākin».", "«ve lâkin».", "لَكِنْ"),
  li_("لِأَحَدِ", "ahad", "noun", ["mubtada-khabar", "idafa-definiteness", K], "أَحَدِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«are for one of».", "«... biri içindir».", "أَحَدِ"),
  W("أَمْرَيْنِ", "amr", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«two things».", "«iki işten»."),
  W("مُعَيَّنٍ", "muayyan", "noun", ["naat-sifa", "ism-maful", "form-ii-verbs"], "صِفَةٌ لِأَحَدِ مَجْرُورَةٌ.", "«determined».", "«muayyen olan»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«nezdinde»."),
  W("الْمُتَكَلِّمِ", "mutakallim", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker».", "«mütekellim».", punct="."),
  W("فَلَا", "la-nafiya", "part", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada", K, AT], "الْفَاءُ لِلتَّفْصِيلِ، وَلَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«lā».", "«lâ».", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  li_("لِنَفْيِ", "nafy", "noun", ["mubtada-khabar", "idafa-definiteness"], "نَفْيِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is to deny».", "«nefyetmek içindir».", "نَفْيِ"),
  W("الْحُكْمِ", "hukm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ruling».", "«hükmü»."),
  W("الثَّابِتِ", "thabit", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«established».", "«sabit olan»."),
  li_("لِلْمَعْطُوفِ", "matuf", "noun", [AT], "الْمَعْطُوفِ مَجْرُورٌ.", "«for what it is joined».", "«ma'tûfun».", "الْمَعْطُوفِ", segs=[seg("لِ", "li", "prep"), seg("لْمَعْطُوفِ", "matuf", "noun")]),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to».", "«aleyh için».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-tan»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«the coordinate».", "«ma'tûftan».", punct="،"),
  nahwu(),
  JAANI(), ZAYD_F(),
  LETC("لَا", "la-nafiya", "حَرْفُ عَطْفٍ لِلنَّفْيِ.", "«not».", "«... değil».", pos="part"),
  AMR_M("بِلَا — نُفِيَ عَنْهُ الْمَجِيءُ."),
 ]})

S.append({"id": "s8", "translation": {
 "en": "And بَلْ, when it comes after an affirmative, is to turn the ruling from what it is joined to onto the coordinate — as جَاءَنِي زَيْدٌ بَلْ عَمْرٌو; and when it comes after a negative, some said it is to deny of the coordinate, and some said to affirm in the coordinate. And لَكِنْ is not used without a negation, and is in the sense of «but only»: مَا قَامَ زَيْدٌ لَكِنْ عَمْرٌو means لَكِنْ قَامَ عَمْرٌو." + C_EN,
 "tr": "بَلْ, müsbet kelâmdan sonra gelirse hükmü ma'tûfun aleyhten ma'tûfa çevirmek içindir — جَاءَنِي زَيْدٌ بَلْ عَمْرٌو gibi; menfî kelâmdan sonra gelirse bazıları ma'tûftan nefy için, bazıları ma'tûfta isbat için dediler. لَكِنْ nefy olmadan kullanılmaz ve «fakat» mânâsındadır: مَا قَامَ زَيْدٌ لَكِنْ عَمْرٌو demek لَكِنْ قَامَ عَمْرٌو demektir." + C_TR},
 "tokens": [
  cited_wa("وَبَلْ", "bal", "conj", ["mubtada-khabar", K, AT], "بَلْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and bal».", "«ve bel».", "بَلْ"),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-se»."),
  W("جَاءَتْ", "jaa", "verb", ["idha-shartiyya", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«it comes».", "«gelirse».", segments=[seg("جَاءَ", "jaa", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-dan sonra»."),
  W("الْمُثْبَتِ", "muthbat", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«an affirmative».", "«müsbet kelâmdan»."),
  W("فَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ، وَهِيَ مُبْتَدَأٌ.", "«it is».", "«o»."),
  li_("لِصَرْفِ", "sarf-turn", "noun", ["mubtada-khabar", "idafa-definiteness"], "صَرْفِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«to turn».", "«çevirmek içindir».", "صَرْفِ"),
  W("الْحُكْمِ", "hukm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ruling».", "«hükmü»."),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-ten»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«what it is joined».", "«ma'tûfun»."),
  W("عَلَيْهِ", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«to».", "«aleyhten».", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«onto».", "«-a»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«the coordinate».", "«ma'tûfa».", punct="،"),
  nahwu(),
  JAANI(), ZAYD_F(),
  LETC("بَلْ", "bal", "حَرْفُ إِضْرَابٍ وَعَطْفٍ.", "«rather».", "«hayır»."),
  AMR_M("بِبَلْ — انْتَقَلَ الْحُكْمُ إِلَيْهِ.", punct="؛"),
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -se».", "إِذَا"),
  W("جَاءَتْ", "jaa", "verb", ["idha-shartiyya", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«it comes».", "«gelirse».", segments=[seg("جَاءَ", "jaa", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-dan sonra»."),
  W("الْمَنْفِيِّ", "manfi", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a negative».", "«menfî kelâmdan».", punct="،"),
  W("فَقِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ، وَقِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«some said».", "«bazıları dedi».", segments=[seg("فَ", "fa", "conj"), seg("قِيلَ", "qala", "verb")]),
  li_("لِلنَّفْيِ", "nafy", "noun", [], "النَّفْيِ مَجْرُورٌ.", "«to deny».", "«nefy için».", "النَّفْيِ", segs=[seg("لِ", "li", "prep"), seg("لنَّفْيِ", "nafy", "noun")]),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-tan»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«the coordinate».", "«ma'tûftan».", punct="،"),
  atf_wa("وَقِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and some said».", "«ve bazıları dedi».", "قِيلَ"),
  li_("لِلْإِثْبَاتِ", "ithbat", "noun", [], "الْإِثْبَاتِ مَجْرُورٌ.", "«to affirm».", "«isbat için».", "الْإِثْبَاتِ", segs=[seg("لِ", "li", "prep"), seg("لْإِثْبَاتِ", "ithbat", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-ta»."),
  W("الْمَعْطُوفِ", "matuf", "noun", ["huruf-jarr", AT], "مَجْرُورٌ.", "«the coordinate».", "«ma'tûfta».", punct="."),
  cited_wa("وَلَكِنْ", "lakin", "part", ["mubtada-khabar", K, AT], "لَكِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and lākin».", "«ve lâkin».", "لَكِنْ"),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  W("تُسْتَعْمَلُ", "istamala", "verb", ["mubtada-khabar", "naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ خَبَرٌ.", "«is used».", "«kullanılmaz»."),
  bi_("بِلَا", "la-nafiya", "part", [], "لَا — بِلَا بِمَعْنَى مِنْ غَيْرِ.", "«without».", "«-sız».", "لَا"),
  W("نَفْيٍ", "nafy", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a negation».", "«nefy».", punct="،"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and it».", "«ve o».", "هِيَ"),
  bi_("بِمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness"], "مَعْنَى مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is in the sense of».", "«... mânâsındadır».", "مَعْنَى"),
  cited("بَلْ", "bal", "conj", ["idafa-definiteness", AT], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ: لِلِاسْتِدْرَاكِ.", "«but only».", "«fakat».", punct=":"),
  cited("مَا", "ma-nafiya", "part", ["mubtada-khabar", "anwa-ma", "la-nafiya"], "نَافِيَةٌ — الْجُمْلَةُ مَحْكِيَّةٌ مُبْتَدَأٌ.", "«not».", "«-madı»."),
  cited("قَامَ", "qala" if False else "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«did stand».", "«kalkmadı»."),
  ZAYD_F(),
  LETC("لَكِنْ", "lakin", "حَرْفُ عَطْفٍ لِلِاسْتِدْرَاكِ بَعْدَ النَّفْيِ.", "«but».", "«fakat».", pos="part"),
  AMR_M("بِلَكِنْ — أُثْبِتَ لَهُ الْقِيَامُ.", punct="،"),
  W("مَعْنَاهُ", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«means».", "«... demektir».", segments=[seg("مَعْنَا", "mana", "noun"), pr3ms()]),
  cited("لَكِنْ", "lakin", "part", ["mubtada-khabar", AT], "خَبَرٌ — الْجُمْلَةُ الْمُقَدَّرَةُ.", "«but».", "«fakat»."),
  cited("قَامَ", "qama", "verb", ["fail", "hollow-verbs", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ مُقَدَّرٌ.", "«stood».", "«kalktı»."),
  cited("عَمْرٌو", "amr-name", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«ʿAmr».", "«Amr».", punct="."),
 ]})

S.append({"id": "s9", "translation": {
 "en": "The letters of alerting are those that come at the head of a sentence to draw the hearers' attention: أَلَا, أَمَا and هَا — as أَلَا زَيْدٌ قَائِمٌ, أَمَا زَيْدٌ قَائِمٌ, هَا زَيْدٌ قَائِمٌ: «know well, be awake, take note — Zayd is standing»." + C_EN,
 "tr": "Tenbih harfleri, muhatapların dikkatini çekmek için cümlenin başında gelen أَلَا, أَمَا ve هَا harfleridir — أَلَا زَيْدٌ قَائِمٌ, أَمَا زَيْدٌ قَائِمٌ, هَا زَيْدٌ قَائِمٌ gibi: «iyi bil, uyanık ol, dikkat et — Zeyd ayaktadır»." + C_TR},
 "tokens": [
  W("حُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harfleri»."),
  W("التَّنْبِيهِ", "tanbih", "noun", ["idafa-definiteness", "huruf-tanbih"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«alerting».", "«tenbih»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«are those that».", "«... olan»."),
  W("يَقَعُ", "waqaa", "verb", ["ism-mawsul", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ صِلَةٌ.", "«come».", "«gelen»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("صَدْرِ", "sadr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«başında»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a sentence».", "«cümlenin»."),
  li_("لِتَنْبِيهِ", "tanbih", "noun", ["idafa-definiteness", "lam-taleel"], "تَنْبِيهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to draw the attention of».", "«dikkatini çekmek için».", "تَنْبِيهِ"),
  W("الْمُخَاطَبِينَ", "mukhatab", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the hearers».", "«muhatapların».", punct=":"),
  cited("أَلَا", "ala-tanbih", "part", [K, "huruf-tanbih"], "حَرْفُ تَنْبِيهٍ — بَدَلٌ مِنْ حُرُوفُ.", "«alā».", "«elâ»."),
  cited_wa("وَأَمَا", "ama", "part", [K, "huruf-tanbih"], "أَمَا مَعْطُوفٌ — حَرْفُ تَنْبِيهٍ.", "«amā».", "«emâ».", "أَمَا"),
  cited_wa("وَهَا", "ha-tanbih", "part", [K, "huruf-tanbih"], "هَا مَعْطُوفٌ — حَرْفُ تَنْبِيهٍ.", "«and hā».", "«ve hâ».", "هَا", punct="،"),
  nahwu(),
  cited("أَلَا", "ala-tanbih", "part", [K, "huruf-tanbih"], "حَرْفُ تَنْبِيهٍ لَا مَحَلَّ لَهُ.", "«know well».", "«iyi bil»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is standing».", "«ayaktadır».", punct="،"),
  cited("أَمَا", "ama", "part", [K, "huruf-tanbih"], "حَرْفُ تَنْبِيهٍ.", "«be awake».", "«uyanık ol»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is standing».", "«ayaktadır».", punct="،"),
  cited("هَا", "ha-tanbih", "part", [K, "huruf-tanbih"], "حَرْفُ تَنْبِيهٍ.", "«take note».", "«dikkat et»."),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is standing».", "«ayaktadır».", punct="."),
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
 "shat": need("shat", "شَاة", "ش و ه", "noun", "a sheep, a ewe", "koyun", 3),
 "idrab": need("idrab", "إِضْرَاب", "ض ر ب", "noun", "turning away from a statement — the sense of بَلْ and the detached أَمْ", "i'râz, bir sözden dönüş — bel'in ve munkatı em'in mânâsı", 4),
 "adraba": need("adraba", "أَضْرَبَ", "ض ر ب", "verb", "to turn away from, to drop (a statement) (Form IV)", "yüz çevirmek, (bir sözden) vazgeçmek (if'âl)", 4),
 "mutasawin": need("mutasawin", "مُتَسَاوٍ", "س و ي", "noun", "equal, on a par — the Form VI ism fāʿil of تَسَاوَى", "müsâvî, eşit — tesâvâ'nın ism-i fâili", 4),
 "tabia-follow": need("tabia-follow", "تَبِعَ", "ت ب ع", "verb", "to follow, to come after", "takip etmek, ardından gelmek", 2),
 "mufid": need("mufid", "مُفِيد", "ف ي د", "noun", "conveying, expressing — the Form IV ism fāʿil of أَفَادَ", "ifade eden, bildiren — efâde'nin ism-i fâili", 3),
 "ukhra": need("ukhra", "أُخْرَى", "أ خ ر", "noun", "another (feminine of آخَر)", "başka, diğer (âhar'ın müennesi)", 2),
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
put_morph(mo, "adraba", _nfc(_sg.derived(_sg.B4, _sg.W4, "ُ", "أَضْرَب", "ضْرِب", "أَضْرِب", "إِضْرَاب", "مُضْرِب", "مُضْرَب", "أُضْرِبَ", "يُضْرَبُ", "أَضْرَبَ عَنِ الشَّيْءِ: أَعْرَضَ عَنْهُ وَكَفَّ — بَابُ الْإِفْعَالِ.")))
put_morph(mo, "tabia-follow", _nfc(_sg.sound1("samia", "تَبِع", "تْبَع", "اِتْبَع", "تَبَع", "تَابِع", "مَتْبُوع", "تُبِعَ", "يُتْبَعُ", "تَبِعَهُ: مَشَى خَلْفَهُ وَلَحِقَهُ — بَابُ سَمِعَ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "أَوْ وَإِمَّا وَأَمْ وَلَا وَبَلْ وَلَكِنْ وَحُرُوفُ التَّنْبِيهِ فِي الْكَافِيَةِ", "en": "Aw, immā and am; lā, bal and lākin; and the letters of alerting in the Kafiya: one of two undetermined, the joined am with its hamza and its answer, the detached am, the rule of immā, and one of two determined", "tr": "Kâfiye'de ev, immâ ve em; lâ, bel ve lâkin; ve tenbih harfleri: muayyen olmayan ikiden biri, hemzesi ve cevabıyla muttasıl em, munkatı em, immâ kuralı ve muayyen ikiden biri"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — أو وإما وأم لأحد الأمرين مبهما؛ أم متصلة ومنقطعة؛ لا وبل ولكن لأحد الأمرين معينا؛ حروف التنبيه ألا وأما وها", "ضياء صونغور اوغلى — دفتر الكافية: أم المتصلة تحتاج إلى الهمزة؛ أرأيت زيدا أم عمرا بين المصنف وسيبويه؛ جوابها بالتعيين؛ إنها لإبل أم شاة؛ إما قبل المعطوف عليه؛ لا وبل بعد المثبت والمنفي؛ لكن بمعنى بل بعد النفي"],
 "question": {
  "en": ["What do aw, immā and am share? All three join two things of which only ONE applies, and the speaker does not know which — جَاءَنِي زَيْدٌ أَوْ عَمْرٌو. That is the opposite of the first four letters, where both applied.",
         "What makes am «joined»? It answers a question: one of two equals has already happened for the speaker, and he asks the hearer which — so one equal must follow the hamza and the other must follow am. أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو is answered «Zayd» or «ʿAmr», never «yes» or «no». Hence Ibn al-Ḥājib bars أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا (Zayd does not follow the hamza) while Sībawayh allows it and prefers أَزَيْدًا رَأَيْتَ أَمْ عَمْرًا.",
         "And the «detached» am? It is bal plus a hamza: the speaker drops his first statement and doubts a second — إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ, «they are surely camels — or are they sheep?». The reader separates the two faces by whether a hamza of question opened the sentence.",
         "What is the rule of immā? It must be doubled: a first immā before the first term, a second with the wāw before the second (إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو). With aw the first immā is optional.",
         "What do lā, bal and lākin share? One of two things applies and the speaker KNOWS which. Lā denies of the second what was affirmed of the first (جَاءَنِي زَيْدٌ لَا عَمْرٌو); bal after an affirmative moves the ruling to the second (جَاءَنِي زَيْدٌ بَلْ عَمْرٌو), after a negative the schools split; lākin needs a negation before it and then means «but rather» (مَا قَامَ زَيْدٌ لَكِنْ عَمْرٌو).",
         "What are the letters of alerting? أَلَا, أَمَا and هَا at the head of a sentence, to wake the hearer before the news; they govern nothing, and the hub's PARTICLES table lists them beside the coordinators because both open clauses."],
  "tr": ["Ev, immâ ve em'de ortak olan ne? Üçü de yalnız BİRİNİN geçerli olduğu ve konuşanın hangisi olduğunu bilmediği iki şeyi bağlar — جَاءَنِي زَيْدٌ أَوْ عَمْرٌو. Bu, ikisinin de geçerli olduğu ilk dört harfin tersidir.",
         "Em'i «muttasıl» yapan ne? Bir soruya cevap verir: iki müsâvîden biri konuşan için zaten olmuştur ve muhataba hangisi olduğunu sorar — bu yüzden bir müsâvî hemzeyi, öteki em'i takip etmelidir. أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو'ya «Zeyd» ya da «Amr» denir, asla «evet» ya da «hayır». Bundan İbnü'l-Hâcib أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا'yı yasaklar (Zeyd hemzeyi takip etmez); Sîbeveyh izin verir ve أَزَيْدًا رَأَيْتَ أَمْ عَمْرًا'yı tercih eder.",
         "Ya «munkatı» em? Bel artı hemzedir: konuşan ilk sözünü bırakır ve ikincisinden şüphe eder — إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ, «onlar elbette devedir — yoksa koyun mu?». Okuyucu iki yüzü cümleyi istifham hemzesinin açıp açmadığıyla ayırır.",
         "İmmâ kuralı nedir? Çiftlenmelidir: ilk terimden önce birinci immâ, ikinciden önce vâvla ikincisi (إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو). Ev ile ilk immâ ihtiyarîdir.",
         "Lâ, bel ve lâkin'de ortak olan ne? İki şeyden biri geçerlidir ve konuşan hangisi olduğunu BİLİR. Lâ birincide olumlananı ikinciden nefyeder (جَاءَنِي زَيْدٌ لَا عَمْرٌو); bel müsbetten sonra hükmü ikinciye taşır (جَاءَنِي زَيْدٌ بَلْ عَمْرٌو), menfîden sonra mektepler ayrılır; lâkin önünde nefy ister ve o zaman «bilakis» demektir (مَا قَامَ زَيْدٌ لَكِنْ عَمْرٌو).",
         "Tenbih harfleri nelerdir? Cümle başında muhatabı haberden önce uyandıran أَلَا, أَمَا ve هَا; hiçbir şeyi yönetmezler; PARTICLES tablosu ikisi de cümle açtığı için onları atıf harflerinin yanında listeler."]},
 "plain": {
  "en": "Six more joining words. Aw, immā and am say «one of the two, I don't know which» — am with a question in front of it asks you to pick. Lā, bal and lākin say «one of the two, and I know which»: «Zayd, not ʿAmr», «no — ʿAmr», «not Zayd but ʿAmr». And alā, amā, hā just say «listen!» before a sentence.",
  "tr": "Altı bağlayıcı daha. Ev, immâ ve em «ikisinden biri, hangisi bilmem» der — önünde soru olan em seçmeni ister. Lâ, bel ve lâkin «ikisinden biri, hangisi biliyorum» der: «Zeyd, Amr değil», «hayır — Amr», «Zeyd değil Amr». Elâ, emâ, hâ ise bir cümleden önce yalnız «dinle!» der."},
 "explanation": {
  "en": "The Kafiya's second division of the coordinators — one of two things, undetermined or determined for the speaker — and the notebook's catechism on أَمْ, which is the richest part. The joined أَمْ is defined by its pragmatics (one of two equals is already the case; the hearer is asked which) and that definition yields two tests the notebook states: it needs the hamza of question, and its answer is a name, not yes or no. The disputed أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا follows from the first test, and the notebook gives both the author's bar and Sībawayh's leave with his preferred order. The detached أَمْ is defined as بَلْ plus the hamza, with the sheep-and-camels example walked through in the speaker's own mind. إِمَّا's doubling rule and أَوْ's option follow. The determined three are given by their sense in one line each, with the schools' split on بَلْ after a negative recorded and لَكِنْ reduced to بَلْ after a negation. The letters of alerting close the chapter, as they close the notebook's page.",
  "tr": "Kâfiye'nin atıf harflerinin ikinci bölümü — konuşan için muayyen olan ya da olmayan iki şeyden biri — ve defterin en zengin kısmı olan أَمْ sual-cevabı. Muttasıl أَمْ pragmatiğiyle tarif edilir (iki müsâvîden biri zaten vâkidir; muhataba hangisi olduğu sorulur) ve bu tarif defterin söylediği iki testi doğurur: istifham hemzesi ister ve cevabı evet ya da hayır değil bir addır. İhtilâflı أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا birinci testten çıkar; defter hem musannifin yasağını hem Sîbeveyh'in iznini tercih ettiği sırayla verir. Munkatı أَمْ, بَلْ artı hemze olarak tarif edilir ve koyun-deve örneği konuşanın zihninde adım adım yürütülür. إِمَّا'nın çiftlenme kuralı ve أَوْ'nun seçeneği izler. Muayyen üçü birer satırla mânâlarıyla verilir; menfîden sonra بَلْ üzerindeki mektep ayrılığı kaydedilir ve لَكِنْ nefyden sonra بَلْ'e indirgenir. Tenbih harfleri, defterin sayfasını kapadığı gibi bâbı kapar."},
 "examples": [
  {"ar": "جَاءَنِي زَيْدٌ أَوْ عَمْرٌو — جَاءَنِي إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو", "en": "One of two, undetermined.", "tr": "Muayyen olmayan ikiden biri.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "أَزَيْدًا رَأَيْتَ أَمْ عَمْرًا", "en": "The joined am, Sībawayh's preferred order.", "tr": "Muttasıl em, Sîbeveyh'in tercih ettiği sıra.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو — زَيْدٌ / عَمْرٌو", "en": "Answered by naming, not by yes or no.", "tr": "Evet ya da hayırla değil, tayinle cevaplanır.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ", "en": "The detached am.", "tr": "Munkatı em.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "جَاءَنِي زَيْدٌ لَا عَمْرٌو — جَاءَنِي زَيْدٌ بَلْ عَمْرٌو — مَا قَامَ زَيْدٌ لَكِنْ عَمْرٌو", "en": "One of two, determined.", "tr": "Muayyen ikiden biri.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "أَلَا زَيْدٌ قَائِمٌ", "en": "A letter of alerting.", "tr": "Bir tenbih harfi.", "sourceStory": "al-kafiya", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو؟ — نَعَمْ»",
   "right": "«— زَيْدٌ (ya da عَمْرٌو); muttasıl em tayinle cevaplanır»",
   "why": {"en": "The question already assumes one of them; yes or no answers nothing.", "tr": "Soru zaten birini varsayar; evet ya da hayır hiçbir şeyi cevaplamaz."}},
  {"wrong": "«جَاءَنِي زَيْدٌ وَإِمَّا عَمْرٌو»",
   "right": "«جَاءَنِي إِمَّا زَيْدٌ وَإِمَّا عَمْرٌو — immâ çiftlenir»",
   "why": {"en": "A first immā must precede what the second is joined to.", "tr": "İkincinin bağlandığından önce bir ilk immâ gelmelidir."}},
  {"wrong": "«قَامَ زَيْدٌ لَكِنْ عَمْرٌو»",
   "right": "«مَا قَامَ زَيْدٌ لَكِنْ عَمْرٌو — lâkin nefysiz kullanılmaz»",
   "why": {"en": "Lākin corrects a negation; after an affirmative use bal.", "tr": "Lâkin bir nefyi düzeltir; müsbetten sonra bel kullanılır."}},
  {"wrong": "«إِنَّهَا لَإِبِلٌ أَمْ شَاةٌ — muttasıl em»",
   "right": "«munkatı em — önünde istifham hemzesi yoktur; bel ve hemze mânâsındadır»",
   "why": {"en": "Without an opening hamza, am detaches and drops the first statement.", "tr": "Açılış hemzesi olmadan em kopar ve ilk sözü bırakır."}}],
 "relatedNotes": ["huruf-al-atf-fil-kafiya", "atf-nasaq", "adawat-al-tasawwur", "huruf-tanbih", "atf-nasaq"]}
NOTE["relatedNotes"] = ["huruf-al-atf-fil-kafiya", "atf-nasaq", "adawat-al-tasawwur", "huruf-tanbih", "kaanna-lakinna-layta-laalla-fil-kafiya"]

ADD_EN = (" Chapter 38 (notebook lines ~342-344): aw, immā and am (joined and detached; the author against Sībawayh on أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا), the doubling of immā, lā, bal and lākin, and the letters of alerting — the notebook's exposition, kept as commentary (s1-s9).")
ADD_TR = (" Otuz sekizinci bâb (defter satırları ~342-344): ev, immâ ve em (muttasıl ve munkatı; أَرَأَيْتَ زَيْدًا أَمْ عَمْرًا'da musannif Sîbeveyh'e karşı), immâ'nın çiftlenmesi, lâ, bel ve lâkin ve tenbih harfleri — defterin açıklaması, şerh olarak (s1-s9).")
write_out(38, S, TITLE, ADD_EN, ADD_TR, "342-344", GLOSS_ADD, notes=(NOTE,),
          related=(("huruf-al-atf-fil-kafiya", [K]), ("huruf-tanbih", [K])))
report(38, S, GLOSS_ADD, (NOTE,))
