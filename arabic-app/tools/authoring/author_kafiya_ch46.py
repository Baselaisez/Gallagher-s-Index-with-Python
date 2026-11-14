# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 46: DEFINITIONS FROM THE NOTEBOOK'S OWN SHEET (p. 96) that the matn chapters do not carry verbatim: the science of
naḥw (definition, subject, aim), waḍʿ, maʿnā, isnād, khāṣṣa, and the one-line definitions of the marfūʿāt, manṣūbāt, majrūrāt and
tawābiʿ. Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~365-405 of the transcription.

  COMMENTARY (the notebook's definitions sheet, in the sharḥ tradition's wording): s1-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch46.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "tarifat-daftar-al-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "تَعْرِيفَاتٌ مِنْ دَفْتَرِ الْكَافِيَةِ", "en": "Definitions from the Kafiya notebook — the science, its subject and aim; waḍʿ, maʿnā, isnād, khāṣṣa; and the four classes in one line each", "tr": "Kâfiye defterinden tarifler — ilim, mevzuu ve gayesi; vaz', mânâ, isnad, hâssa; ve dört sınıf birer satırla"}
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
KK = "al-kalima-wal-kalam"
def DEF(full, lex, en, tr, pos="noun", tags=(), ar=None, wa=True, punct=":"):
    if wa: return atf_wa("وَ" + full, lex, pos, ["mubtada-khabar", K] + list(tags), full + " مُبْتَدَأٌ مَرْفُوعٌ — الْمُعَرَّفُ.", en, tr, full, punct=punct)
    return W(full, lex, pos, ["mubtada-khabar", K] + list(tags), ar or "مُبْتَدَأٌ مَرْفُوعٌ — الْمُعَرَّفُ.", en, tr, punct=punct)
def MA_KH(en="«is that which».", tr="«... -dır».", tags=()):
    return W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"] + list(tags), "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", en, tr)
def ISHTAMALA(punct=None):
    return [W("اشْتَمَلَ", "ishtamala", "verb", ["ism-mawsul", "fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«contains».", "«müştemil olan»."), W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«(on)».", "«üzerine»."), W("عَلَمِ", "alam-sign", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the sign of».", "«alâmetini».")]
def SHAY(full, tags, ar, en, tr, punct=None): return W(full, "shay", "noun", tags, ar, en, tr, punct=punct)

S.append({"id": "s1", "translation": {
 "en": "The science of naḥw is a science by which the states of the Arabic word are known from the side of iʿrāb and bināʾ; its subject is the Arabic word occurring in speech; and its aim is guarding against error in iʿrāb and bināʾ." + C_EN,
 "tr": "Nahiv ilmi, Arapça kelimenin hâllerinin i'râb ve binâ cihetinden kendisiyle bilindiği bir ilimdir; mevzuu kelâmda vâki olan Arapça kelimedir; gayesi i'râb ve binâdaki hatadan sakınmaktır." + C_TR},
 "tokens": [
  W("عِلْمُ", "ilm", "noun", ["mubtada-khabar", "idafa-definiteness", K], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the science of».", "«... ilmi»."),
  W("النَّحْوِ", "nahw", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naḥw».", "«nahiv»."),
  W("عِلْمٌ", "ilm", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is a science».", "«bir ilimdir»."),
  W("يُعْرَفُ", "arafa", "verb", ["naat-sifa", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — الْجُمْلَةُ صِفَةٌ لِعِلْمٌ.", "«by which are known».", "«kendisiyle bilindiği»."),
  bi_("بِهِ", "bi", "prep", [], "الْهَاءُ مَجْرُورٌ بِالْبَاءِ — الْعَائِدُ.", "«by it».", "«kendisiyle».", "هِ", segs=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("أَحْوَالُ", "ahwal", "noun", ["naib-al-fail", "idafa-definiteness", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the states of».", "«hâllerinin»."),
  W("الْكَلِمَةِ", "kalima", "noun", ["idafa-definiteness", KK], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the word».", "«kelimenin»."),
  W("الْعَرَبِيَّةِ", "arabi", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَجْرُورَةٌ.", "«Arabic».", "«Arapça»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("حَيْثُ", "haythu", "noun", ["huruf-jarr", "idafa-definiteness", "al-murab-wal-mabni-wal-irab"], "ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ، وَهُوَ مُضَافٌ.", "«the side of».", "«cihetinden»."),
  W("الْإِعْرَابِ", "irab", "noun", ["idafa-definiteness", "al-murab-wal-mabni-wal-irab"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb».", "«i'râb»."),
  atf_wa("وَالْبِنَاءِ", "bina", "noun", [AT], "الْبِنَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and bināʾ».", "«ve binâ».", "الْبِنَاءِ", punct="؛"),
  atf_wa("وَمَوْضُوعُهُ", "mawdu", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maful"], "مَوْضُوعُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its subject».", "«mevzuu».", "مَوْضُوعُهُ", extra_segs=[seg("مَوْضُوعُ", "mawdu", "noun"), pr3ms()]),
  W("الْكَلِمَةُ", "kalima", "noun", ["mubtada-khabar", KK], "خَبَرٌ مَرْفُوعٌ.", "«is the word».", "«kelimedir»."),
  W("الْعَرَبِيَّةُ", "arabi", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَرْفُوعَةٌ.", "«Arabic».", "«Arapça»."),
  W("الْوَاقِعَةُ", "waqia", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ.", "«occurring».", "«vâki olan»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("الْكَلَامِ", "kalam", "noun", ["huruf-jarr", KK], "مَجْرُورٌ.", "«speech».", "«kelâmda».", punct="؛"),
  atf_wa("وَغَايَتُهُ", "ghaya", "noun", ["mubtada-khabar", "idafa-definiteness"], "غَايَتُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its aim».", "«gayesi».", "غَايَتُهُ", extra_segs=[seg("غَايَتُ", "ghaya", "noun"), pr3ms()]),
  W("الِاحْتِرَازُ", "ihtiraz", "noun", ["mubtada-khabar", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ.", "«is guarding».", "«sakınmaktır»."),
  W("عَنِ", "an-jarr", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«against».", "«-dan»."),
  W("الْخَطَإِ", "khata", "noun", ["huruf-jarr"], "مَجْرُورٌ — الْهَمْزَةُ عَلَى يَاءٍ لِلْكَسْرَةِ.", "«error».", "«hatadan»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-daki»."),
  W("الْإِعْرَابِ", "irab", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«iʿrāb».", "«i'râb»."),
  atf_wa("وَالْبِنَاءِ", "bina", "noun", [AT], "الْبِنَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and bināʾ».", "«ve binâ».", "الْبِنَاءِ", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And waḍʿ — assignment — is the appointing of one thing to another so that whenever the first thing is uttered or perceived, the second thing is understood from it." + C_EN,
 "tr": "Vaz', bir şeyi bir şeye öyle tahsis etmektir ki birincisi söylendiği ya da duyulduğu zaman ondan ikincisi anlaşılır." + C_TR},
 "tokens": [
  DEF("الْوَضْعُ", "wad-put", "«and waḍʿ».", "«vaz'»."),
  W("تَخْصِيصُ", "takhsis", "noun", ["mubtada-khabar", "idafa-definiteness", "form-ii-verbs"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the appointing of».", "«tahsis etmektir»."),
  SHAY("شَيْءٍ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şeyi»."),
  bi_("بِشَيْءٍ", "shay", "noun", [], "شَيْءٍ مَجْرُورٌ.", "«to a thing».", "«bir şeye».", "شَيْءٍ"),
  bi_("بِحَيْثُ", "haythu", "noun", ["al-murab-wal-mabni-wal-irab"], "حَيْثُ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ.", "«so that».", "«öyle ki».", "حَيْثُ"),
  W("مَتَى", "mata", "part", ["al-majzum-wal-shart-wal-jaza", "maful-fih"], "اسْمُ شَرْطٍ ظَرْفٌ.", "«whenever».", "«... zaman»."),
  W("أُطْلِقَ", "atlaqa", "verb", ["al-majzum-wal-shart-wal-jaza", "naib-al-fail", "form-iv-verbs"], "فِعْلُ الشَّرْطِ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is uttered».", "«söylendiği»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("أُحِسَّ", "ahassa", "verb", [AT, "naib-al-fail", "form-iv-verbs", "doubled-verbs"], "مَعْطُوفٌ — مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«perceived».", "«duyulduğu»."),
  SHAY("الشَّيْءُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the thing».", "«şey»."),
  W("الْأَوَّلُ", "awwal", "noun", ["naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«first».", "«birinci»."),
  W("فُهِمَ", "fahima", "verb", ["al-majzum-wal-shart-wal-jaza", "naib-al-fail"], "جَوَابُ الشَّرْطِ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is understood».", "«anlaşılır»."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«from it».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  SHAY("الشَّيْءُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the thing».", "«şey»."),
  W("الثَّانِي", "thani", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«second».", "«ikinci».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And the meaning is what is intended by a thing — as by رَجُل is intended a male, rational and adult." + C_EN,
 "tr": "Mânâ, bir şeyle kastedilendir — رَجُل ile âkil, bâliğ bir erkeğin kastedilmesi gibi." + C_TR},
 "tokens": [
  DEF("الْمَعْنَى", "mana", "«and the meaning».", "«mânâ».", tags=("ism-maqsur-manqus",)),
  MA_KH("«is what».", "«... -dir»."),
  W("يُقْصَدُ", "qasada", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةٌ.", "«is intended».", "«kastedilen»."),
  bi_("بِشَيْءٍ", "shay", "noun", [], "شَيْءٍ مَجْرُورٌ.", "«by a thing».", "«bir şeyle».", "شَيْءٍ", punct="،"),
  ka_("كَمَا", "ma-masdariyya", "part", ["anwa-ma"], "مَا مَصْدَرِيَّةٌ.", "«as».", "«... gibi».", "مَا", segs=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  W("يُقْصَدُ", "qasada", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is intended».", "«kastedilmesi»."),
  bi_("بِرَجُلٍ", "rajul", "noun", [], "رَجُلٍ مَجْرُورٌ — اللَّفْظُ مَحْكِيٌّ.", "«by rajul».", "«racül ile».", "رَجُلٍ"),
  W("ذَكَرٌ", "dhakar", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a male».", "«bir erkek»."),
  W("عَاقِلٌ", "aqil", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَرْفُوعَةٌ.", "«rational».", "«âkil»."),
  W("بَالِغٌ", "baligh-adult", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ.", "«adult».", "«bâliğ».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And isnād — predication — is the relating of one of the two words, really or by ruling, to the other, so that it conveys to the hearer a complete benefit on which silence is proper." + C_EN,
 "tr": "İsnad, iki kelimeden birini hakikaten ya da hükmen ötekine öyle nispet etmektir ki muhataba, üzerine susmanın sahih olduğu tam bir fayda ifade eder." + C_TR},
 "tokens": [
  DEF("الْإِسْنَادُ", "isnad", "«and isnād».", "«isnad».", tags=(KK, "form-iv-verbs")),
  W("نِسْبَةُ", "nisba", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the relating of».", "«nispet etmektir»."),
  W("إِحْدَى", "ihda", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«one of».", "«birini»."),
  W("الْكَلِمَتَيْنِ", "kalima", "noun", ["idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the two words».", "«iki kelimeden»."),
  W("حَقِيقَةً", "haqiqa", "noun", ["hal"], "حَالٌ مَنْصُوبٌ — أَوْ مَفْعُولٌ مُطْلَقٌ.", "«really».", "«hakikaten»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("حُكْمًا", "hukm", "noun", [AT, "hal"], "مَعْطُوفٌ مَنْصُوبٌ.", "«by ruling».", "«hükmen»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الْأُخْرَى", "ukhra", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the other».", "«ötekine»."),
  bi_("بِحَيْثُ", "haythu", "noun", ["al-murab-wal-mabni-wal-irab"], "حَيْثُ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ.", "«so that».", "«öyle ki».", "حَيْثُ"),
  W("يُفِيدُ", "afada", "verb", ["fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: الْإِسْنَادُ.", "«it conveys».", "«ifade eder»."),
  W("الْمُخَاطَبَ", "mukhatab", "noun", ["maful-bihi", "ism-maful"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«to the hearer».", "«muhataba»."),
  W("فَائِدَةً", "faida", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a benefit».", "«bir fayda»."),
  W("تَامَّةً", "tamm", "noun", ["naat-sifa", "sifa-mushabbaha"], "صِفَةٌ مَنْصُوبَةٌ.", "«complete».", "«tam»."),
  W("يَصِحُّ", "sahha", "verb", ["naat-sifa", "fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ — الْجُمْلَةُ صِفَةٌ ثَانِيَةٌ.", "«is proper».", "«sahih olduğu»."),
  W("السُّكُوتُ", "sukut", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«silence».", "«susmanın»."),
  W("عَلَيْهَا", "ala", "prep", ["huruf-jarr"], "عَلَى حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — الْعَائِدُ.", "«on it».", "«üzerine».", punct=".", segments=[seg("عَلَيْ", "ala", "prep"), pr3fs()]),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And the khāṣṣa — the peculiar property — is what belongs specially to a thing and is not found in anything else." + C_EN,
 "tr": "Hâssa, bir şeye mahsus olup başkasında bulunmayandır." + C_TR},
 "tokens": [
  DEF("الْخَاصَّةُ", "khassa", "«and the khāṣṣa».", "«hâssa»."),
  MA_KH("«is what».", "«... -dır»."),
  W("يَخْتَصُّ", "ikhtassa", "verb", ["ism-mawsul", "fail", "form-viii-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ.", "«belongs specially».", "«mahsus olup»."),
  bi_("بِشَيْءٍ", "shay", "noun", [], "شَيْءٍ مَجْرُورٌ.", "«to a thing».", "«bir şeye».", "شَيْءٍ"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«ve ... -maz».", "لَا"),
  W("يُوجَدُ", "wajada", "verb", ["naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«is found».", "«bulunmayan»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-da»."),
  W("غَيْرِهِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«anything else».", "«başkasında».", punct=".", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And the marfūʿāt are what contains the sign of being a doer; the manṣūbāt are what contains the sign of being an object; and the majrūrāt are what contains the sign of the muḍāf ilayh." + C_EN,
 "tr": "Merfûât, fâiliyet alâmetini müştemil olandır; mansûbât, mef'ûliyet alâmetini müştemil olandır; mecrûrât, muzâfun ileyh alâmetini müştemil olandır." + C_TR},
 "tokens": [
  DEF("الْمَرْفُوعَاتُ", "marfuat", "«and the marfūʿāt».", "«merfûât».", tags=("jam-muannath-salim",)),
  MA_KH(),
  *ISHTAMALA(),
  W("الْفَاعِلِيَّةِ", "failiyya", "noun", ["idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«being a doer».", "«fâiliyet».", punct="؛"),
  DEF("الْمَنْصُوبَاتُ", "mansubat", "«the manṣūbāt».", "«mansûbât».", tags=("jam-muannath-salim",)),
  MA_KH(),
  *ISHTAMALA(),
  W("الْمَفْعُولِيَّةِ", "mafuliyya", "noun", ["idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«being an object».", "«mef'ûliyet».", punct="؛"),
  DEF("الْمَجْرُورَاتُ", "majrurat", "«and the majrūrāt».", "«mecrûrât».", tags=("jam-muannath-salim",)),
  MA_KH(),
  *ISHTAMALA(),
  W("الْمُضَافِ", "mudaf", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāf».", "«muzâfun»."),
  W("إِلَيْهِ", "ila", "prep", ["huruf-jarr"], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«ilayh».", "«ileyh».", punct=".", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And the tawābiʿ — the followers — are every second word carrying the iʿrāb of what precedes it from one and the same side." + C_EN,
 "tr": "Tevâbi', bir cihetten sâbıkının i'râbıyla i'râblanan her ikincidir." + C_TR},
 "tokens": [
  DEF("التَّوَابِعُ", "tabi", "«and the tawābiʿ».", "«tevâbi'».", tags=("jam-taksir", "mamnu-min-sarf")),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«are every».", "«her»."),
  W("ثَانٍ", "thani", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَنْقُوصٌ حُذِفَتْ يَاؤُهُ.", "«second word».", "«ikincidir»."),
  bi_("بِإِعْرَابِ", "irab", "noun", ["idafa-definiteness"], "إِعْرَابِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«carrying the iʿrāb of».", "«... i'râbıyla».", "إِعْرَابِ"),
  W("سَابِقِهِ", "sabiq", "noun", ["idafa-definiteness", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«what precedes it».", "«sâbıkının».", segments=[seg("سَابِقِ", "sabiq", "noun"), pr3msi()]),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-ten»."),
  W("جِهَةٍ", "jiha", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a side».", "«bir cihet»."),
  W("وَاحِدَةٍ", "wahid", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«one and the same».", "«bir».", punct="."),
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
 "ihtiraz": need("ihtiraz", "اِحْتِرَاز", "ح ر ز", "noun", "guarding against, avoiding (masdar, Form VIII)", "sakınma, ihtiraz (iftiʿâl masdarı)", 4),
 "ishtamala": need("ishtamala", "اِشْتَمَلَ", "ش م ل", "verb", "to contain, to comprise (Form VIII; اِشْتَمَلَ عَلَى)", "içermek, müştemil olmak (iftiʿâl; اِشْتَمَلَ عَلَى)", 4),
 "baligh-adult": need("baligh-adult", "بَالِغ", "ب ل غ", "noun", "adult, of age (ism fāʿil of بَلَغَ)", "bâliğ, ergin (belağa'nın ism-i fâili)", 3),
 "marfuat": need("marfuat", "مَرْفُوعَات", "ر ف ع", "noun", "the marfūʿāt — the nouns in rafʿ (plural of مَرْفُوع)", "merfûât — ref' hâlindeki isimler (مَرْفُوع'un çoğulu)", 3),
 "mansubat": need("mansubat", "مَنْصُوبَات", "ن ص ب", "noun", "the manṣūbāt — the nouns in naṣb (plural of مَنْصُوب)", "mansûbât — nasb hâlindeki isimler (مَنْصُوب'un çoğulu)", 3),
 "majrurat": need("majrurat", "مَجْرُورَات", "ج ر ر", "noun", "the majrūrāt — the nouns in jarr (plural of مَجْرُور)", "mecrûrât — cer hâlindeki isimler (مَجْرُور'un çoğulu)", 3),
 "tabi": need("tabi", "تَابِع", "ت ب ع", "noun", "follower, dependent (a tābiʿ)", "tâbi", 3, plural="تَوَابِع"),
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
put_morph(mo, "ishtamala", _nfc(_sg.derived(_sg.B8, _sg.W8, "َ", "اِشْتَمَل", "شْتَمِل", "اِشْتَمِل", "اِشْتِمَال", "مُشْتَمِل", "مُشْتَمَل", "اُشْتُمِلَ", "يُشْتَمَلُ", "اِشْتَمَلَ عَلَى الشَّيْءِ: حَوَاهُ وَتَضَمَّنَهُ — بَابُ الِافْتِعَالِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "تَعْرِيفَاتُ دَفْتَرِ الْكَافِيَةِ: الْعِلْمُ وَالْوَضْعُ وَالْمَعْنَى وَالْإِسْنَادُ وَالْخَاصَّةُ وَالْأَقْسَامُ الْأَرْبَعَةُ", "en": "The Kafiya notebook's definitions sheet: the science of naḥw, waḍʿ, maʿnā, isnād, khāṣṣa, and the four classes of nouns in one line each", "tr": "Kâfiye defterinin tarifler sayfası: nahiv ilmi, vaz', mânâ, isnad, hâssa ve dört isim sınıfı birer satırla"},
 "level": 3, "group": "nahw",
 "classicalSources": ["ضياء صونغور اوغلى — دفتر الكافية ص ٩٦: تعريف علم النحو وموضوعه وغايته؛ الوضع؛ المعنى؛ الإسناد؛ الخاصة؛ المرفوعات والمنصوبات والمجرورات والتوابع", "الكافية لابن الحاجب — الكلمة لفظ وضع لمعنى مفرد؛ الكلام ما تضمن كلمتين بالإسناد؛ التوابع كل ثان بإعراب سابقه من جهة واحدة"],
 "question": {
  "en": ["What is naḥw FOR? The sheet answers in three lines: it is the science of the Arabic word's states as to iʿrāb and bināʾ (definition), its subject is the word as it occurs in speech (not the word in the dictionary), and its aim is not to err in iʿrāb and bināʾ. Every engine in this app is an answer to that aim.",
         "What does «assigned to a meaning» (وُضِعَ لِمَعْنًى) in the definition of the word rest on? On waḍʿ: a word is tied to a meaning so that hearing the one brings the other to mind. The glossary is the app's record of waḍʿ; the analyzer's «sure» rows are the words whose waḍʿ it has on file.",
         "What makes two words a sentence? Isnād — relating one to the other so that the hearer gets a complete benefit and may fall silent. قَامَ زَيْدٌ is speech; غُلَامُ زَيْدٍ is not, because the idafa relates without predicating. The analyzer's first question (ismiyya or fiʿliyya) presupposes an isnād found.",
         "What is a khāṣṣa, and why does the Kafiya list the noun's? A property found in a thing and in nothing else — so the noun's khāṣṣa (the article, tanwīn, jarr, being talked about) is a TEST: find one and the word is a noun. The sentence analyzer's noun/verb reading is built on exactly these marks.",
         "How does the sheet define the four classes? Not by case endings but by the SIGN of a role: the marfūʿāt carry the sign of fāʿiliyya, the manṣūbāt of mafʿūliyya, the majrūrāt of the muḍāf ilayh — and the tawābiʿ have no role of their own but carry a preceding word's iʿrāb from one single side. That last clause excludes the khabar (which agrees with the mubtadaʾ in case but from a different side).",
         "Why «from one side»? Because the khabar also carries the mubtadaʾ's rafʿ, yet it is not a follower: it takes rafʿ for being a khabar, not for following. The definition's last three words are what keep the tawābiʿ to five."],
  "tr": ["Nahiv NE İÇİNDİR? Sayfa üç satırla cevap verir: Arapça kelimenin i'râb ve binâ bakımından hâllerinin ilmidir (tarif), mevzuu kelâmda vâki olan kelimedir (sözlükteki kelime değil), gayesi i'râb ve binâda hata etmemektir. Bu uygulamadaki her motor o gayeye bir cevaptır.",
         "Kelimenin tarifindeki «bir mânâya konulmuş» (وُضِعَ لِمَعْنًى) neye dayanır? Vaz'a: kelime bir mânâya öyle bağlanır ki birini duymak ötekini akla getirir. Sözlük, uygulamanın vaz' kaydıdır; analizörün «sure» satırları vaz'ı dosyada olan kelimelerdir.",
         "İki kelimeyi cümle yapan nedir? İsnad — birini ötekine öyle nispet etmek ki muhatap tam bir fayda alır ve susabilir. قَامَ زَيْدٌ kelâmdır; غُلَامُ زَيْدٍ değildir, çünkü izâfet isnad etmeden nispet eder. Analizörün ilk sorusu (isim mi fiil cümlesi mi) bulunmuş bir isnadı varsayar.",
         "Hâssa nedir ve Kâfiye ismin hâssasını niçin sayar? Bir şeyde bulunup başkasında bulunmayan özellik — bu yüzden ismin hâssası (elif-lâm, tenvin, cer, hakkında konuşulma) bir TESTTİR: birini bul, kelime isimdir. Cümle analizörünün isim/fiil okuması tam bu alâmetler üzerine kuruludur.",
         "Sayfa dört sınıfı nasıl tarif eder? Hareke sonlarıyla değil bir rolün ALÂMETİYLE: merfûât fâiliyet alâmetini, mansûbât mef'ûliyet alâmetini, mecrûrât muzâfun ileyh alâmetini taşır — tevâbi'in ise kendi rolü yoktur, önceki kelimenin i'râbını tek bir cihetten taşır. Bu son kayıt haberi dışarıda bırakır (haber mübtedaya i'râbda uyar ama başka bir cihetten).",
         "Niçin «bir cihetten»? Çünkü haber de mübtedanın ref'ini taşır ama tâbi değildir: ref'i izlediği için değil haber olduğu için alır. Tarifin son üç kelimesi tevâbi'i beşte tutan şeydir."]},
 "plain": {
  "en": "A page of short definitions from the notebook. Grammar is the science of how Arabic words end; a word means something because it was assigned to it; two words make a sentence when one is said about the other; a noun's «marks» are what only nouns have; and words are sorted by which role sign they carry.",
  "tr": "Defterden bir sayfa kısa tarif. Nahiv, Arapça kelimelerin nasıl bittiğinin ilmidir; kelime, ona konulduğu için bir şey ifade eder; biri öteki hakkında söylenince iki kelime cümle olur; ismin «alâmetleri» yalnız isimlerde olanlardır; kelimeler taşıdıkları rol alâmetine göre sınıflanır."},
 "explanation": {
  "en": "The notebook ends its Kafiya with a sheet of definitions in the sharḥ tradition's wording. The matn's own definitions (the word, speech, the noun, the muʿrab, iʿrāb, the diptote, the fāʿil, the deputy, the mubtadaʾ and the khabar) are already in the matn chapters and are not repeated; this chapter takes what the matn does not state — the science's definition, subject and aim, the four technical terms waḍʿ, maʿnā, isnād and khāṣṣa, and the sheet's one-line definitions of the four classes by their role signs. The definitions are the vocabulary the whole book has been using; they are placed last because the notebook places them last.",
  "tr": "Defter Kâfiye'sini şerh geleneğinin ifadesiyle bir tarifler sayfasıyla bitirir. Matnın kendi tarifleri (kelime, kelâm, isim, mu'rab, i'râb, gayr-i munsarif, fâil, nâib, mübteda ve haber) matn bâblarında zaten vardır ve tekrarlanmaz; bu bâb matnın söylemediğini alır — ilmin tarifi, mevzuu ve gayesi, dört ıstılah vaz', mânâ, isnad ve hâssa ve sayfanın dört sınıfı rol alâmetleriyle tarif eden birer satırı. Tarifler bütün kitabın kullanageldiği kelime hazinesidir; defter onları sona koyduğu için sona konmuştur."},
 "examples": [
  {"ar": "عِلْمُ النَّحْوِ عِلْمٌ يُعْرَفُ بِهِ أَحْوَالُ الْكَلِمَةِ الْعَرَبِيَّةِ مِنْ حَيْثُ الْإِعْرَابِ وَالْبِنَاءِ", "en": "The science defined.", "tr": "İlmin tarifi.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "الْوَضْعُ تَخْصِيصُ شَيْءٍ بِشَيْءٍ", "en": "Waḍʿ.", "tr": "Vaz'.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "الْإِسْنَادُ نِسْبَةُ إِحْدَى الْكَلِمَتَيْنِ إِلَى الْأُخْرَى", "en": "Isnād.", "tr": "İsnad.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "الْمَرْفُوعَاتُ مَا اشْتَمَلَ عَلَى عَلَمِ الْفَاعِلِيَّةِ", "en": "A class defined by its role sign.", "tr": "Rol alâmetiyle tarif edilen bir sınıf.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "التَّوَابِعُ كُلُّ ثَانٍ بِإِعْرَابِ سَابِقِهِ مِنْ جِهَةٍ وَاحِدَةٍ", "en": "The followers.", "tr": "Tevâbi'.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«غُلَامُ زَيْدٍ bir kelâmdır»",
   "right": "«değildir — izâfet nispettir, isnad değildir; susmak sahih olmaz»",
   "why": {"en": "Speech needs an isnād that yields a complete benefit.", "tr": "Kelâm, tam fayda veren bir isnad ister."}},
  {"wrong": "«haber bir tâbidir, çünkü mübtedanın ref'ini taşır»",
   "right": "«tâbi değildir — ref'i başka bir cihetten alır»",
   "why": {"en": "The followers carry a preceding word's iʿrāb from ONE side; the khabar's rafʿ is its own.", "tr": "Tevâbi' önceki kelimenin i'râbını TEK cihetten taşır; haberin ref'i kendinindir."}},
  {"wrong": "«nahvin mevzuu sözlükteki kelimedir»",
   "right": "«kelâmda vâki olan kelimedir — i'râb cümle içinde doğar»",
   "why": {"en": "Iʿrāb is a property of a word in a sentence, not in a list.", "tr": "İ'râb, listedeki değil cümledeki kelimenin özelliğidir."}}],
 "relatedNotes": ["al-kalima-wal-kalam", "al-murab-wal-mabni-wal-irab", "al-mamul-wa-aqsamuh", "al-amil-wa-aqsamuh", "atf-nasaq"]}

ADD_EN = (" Chapter 46 (notebook lines ~365-405, the definitions sheet of p. 96): the science of naḥw (definition, subject, aim), waḍʿ, maʿnā, isnād, khāṣṣa, and the one-line definitions of the marfūʿāt, manṣūbāt, majrūrāt and tawābiʿ — the sheet's wording in the sharḥ tradition, kept as commentary (s1-s7); the matn's own definitions already carried by chapters 1-2 and 9-24 are not repeated.")
ADD_TR = (" Kırk altıncı bâb (defter satırları ~365-405, s. 96'nın tarifler sayfası): nahiv ilmi (tarif, mevzu, gaye), vaz', mânâ, isnad, hâssa ve merfûât, mansûbât, mecrûrât ve tevâbi'in birer satırlık tarifleri — sayfanın şerh geleneğindeki ifadesi, şerh olarak (s1-s7); 1-2 ve 9-24. bâbların zaten taşıdığı matn tarifleri tekrarlanmaz.")
write_out(46, S, TITLE, ADD_EN, ADD_TR, "365-405", GLOSS_ADD, notes=(NOTE,),
          related=(("al-kalima-wal-kalam", [K]), ("al-mamul-wa-aqsamuh", [K])))
report(46, S, GLOSS_ADD, (NOTE,))
