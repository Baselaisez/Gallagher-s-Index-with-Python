# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 41: THE CONDITIONAL LETTERS إِنْ، لَوْ، أَمَّا — head of the sentence; إِنْ for the future even on a māḍī, لَوْ for the
past even on a muḍāriʿ; both enter on a verb stated or implied (وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ); hence لَوْ أَنَّكَ with the fatḥa (أَنَّ
and its clause the fāʿil of an implied ثَبَتَ), the verb in the khabar's place as substitute for the dropped verb, and the jāmid
khabar allowed (وَلَوْ أَنَّ مَا فِي الْأَرْضِ مِنْ شَجَرَةٍ أَقْلَامٌ, 31:27).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~346-347 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch41.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "huruf-al-shart-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الشَّرْطِ: إِنْ وَلَوْ، وَلَوْ أَنَّ", "en": "The conditional letters — in for the future, law for the past, and the fatha of law anna", "tr": "Şart harfleri — gelecek için in, geçmiş için lev ve lev enne'nin fethası"}
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
SH = "al-majzum-wal-shart-wal-jaza"
def DKH(): return W("دَخَلَتْ", "dakhala", "verb", ["in-shartiyya", "fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — فِعْلُ الشَّرْطِ.", "«it enters».", "«girse de».", segments=[seg("دَخَلَ", "dakhala", "verb"), seg("تْ", "ta-tanith", "part")])
def ALA(): return W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«... üzerine».")
def WA_IN_WASL(): return atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "الْوَاوُ حَالِيَّةٌ، وَإِنْ وَصْلِيَّةٌ.", "«even if».", "«... -se de».", "إِنْ")
def AKR(full, ar, en, tr, segs, punct=None, tags=()):
    return cited(full, "akrama", "verb", ["form-iv-verbs", SH] + list(tags), ar, en, tr, punct=punct, segments=segs)
def DRB(full, ar, en, tr, segs, punct=None, tags=()):
    return cited(full, "daraba", "verb", [SH] + list(tags), ar, en, tr, punct=punct, segments=segs)
def LAW_ANNAKA(ar="لَوْ حَرْفُ شَرْطٍ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا."):
    return [cited("لَوْ", "law", "part", [SH, K], "حَرْفُ شَرْطٍ لِلْمَاضِي.", "«if».", "«şayet»."),
            cited("أَنَّكَ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna", K], ar, "«that you».", "«sen».", segments=[seg("أَنَّ", "anna", "part"), pr2ms()])]

S.append({"id": "s1", "translation": {
 "en": "The conditional letters are إِنْ, لَوْ and أَمَّا, and they come at the head of the sentence." + C_EN,
 "tr": "Şart harfleri إِنْ, لَوْ ve أَمَّا'dır; sözün başında gelirler." + C_TR},
 "tokens": [
  W("حُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harfleri»."),
  W("الشَّرْطِ", "shart", "noun", ["idafa-definiteness", SH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«condition».", "«şart».", punct=":"),
  cited("إِنْ", "in-shartiyya", "part", ["mubtada-khabar", K, "in-shartiyya"], "لَفْظٌ مَحْكِيٌّ — خَبَرٌ.", "«in».", "«in»."),
  cited_wa("وَلَوْ", "law", "part", [AT, K], "لَوْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«law».", "«lev».", "لَوْ"),
  cited_wa("وَأَمَّا", "amma-tafsil", "part", [AT, K, "amma-tafsiliyya"], "أَمَّا مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and ammā».", "«ve emmâ».", "أَمَّا", punct="،"),
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and they».", "«ve onlar».", "هِيَ"),
  W("تَقَعُ", "waqaa", "verb", ["mubtada-khabar", "fail", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْجُمْلَةُ خَبَرٌ.", "«come».", "«gelirler»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("صَدْرِ", "sadr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«başında»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«sözün».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "إِنْ is for the future even when it enters on a past verb — as إِنْ تُكْرِمْنِي أُكْرِمْكَ and إِنْ أَكْرَمْتَنِي أَكْرَمْتُكَ — and the meaning of the two is one: «if you honour me, I will honour you»." + C_EN,
 "tr": "إِنْ, mâzînin üzerine girse de istikbal içindir — إِنْ تُكْرِمْنِي أُكْرِمْكَ ve إِنْ أَكْرَمْتَنِي أَكْرَمْتُكَ gibi — ikisinin mânâsı birdir: «bana ikram edersen ben de sana ikram ederim»." + C_TR},
 "tokens": [
  W("فَإِنْ", "in-shartiyya", "part", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada", K], "الْفَاءُ لِلتَّفْصِيلِ، وَإِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«in».", "«in».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  li_("لِلِاسْتِقْبَالِ", "istiqbal", "noun", ["mubtada-khabar", "form-x-verbs"], "الِاسْتِقْبَالِ مَجْرُورٌ — خَبَرٌ.", "«is for the future».", "«istikbal içindir».", "الِاسْتِقْبَالِ", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِقْبَالِ", "istiqbal", "noun")]),
  WA_IN_WASL(), DKH(), ALA(),
  W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«a past verb».", "«mâzînin».", punct="،"),
  nahwu(),
  cited("إِنْ", "in-shartiyya", "part", ["in-shartiyya", SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-se»."),
  AKR("تُكْرِمْنِي", "فِعْلُ الشَّرْطِ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you honour me».", "«bana ikram edersen».", [seg("تُكْرِمْ", "akrama", "verb"), pr1s()]),
  AKR("أُكْرِمْكَ", "جَوَابُ الشَّرْطِ مَجْزُومٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I will honour you».", "«sana ikram ederim».", [seg("أُكْرِمْ", "akrama", "verb"), pr2ms()], punct="،"),
  cited_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", SH], "إِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve ... -se».", "إِنْ"),
  AKR("أَكْرَمْتَنِي", "فِعْلُ الشَّرْطِ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ فَاعِلٌ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you honour me».", "«bana ikram edersen».", [seg("أَكْرَمْ", "akrama", "verb"), prTa(), pr1s()]),
  AKR("أَكْرَمْتُكَ", "جَوَابُ الشَّرْطِ مَاضٍ فِي مَحَلِّ جَزْمٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I will honour you».", "«sana ikram ederim».", [seg("أَكْرَمْ", "akrama", "verb"), prT(), pr2ms()], punct="،"),
  atf_wa("وَمَعْنَاهُمَا", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "مَعْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«and the meaning of the two».", "«ve ikisinin mânâsı».", "مَعْنَاهُمَا", extra_segs=[seg("مَعْنَا", "mana", "noun"), pr3d()]),
  W("وَاحِدٌ", "wahid", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is one».", "«birdir».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And لَوْ is the reverse of إِنْ: for the past even when it enters on a muḍāriʿ — as لَوْ ضَرَبْتَ ضَرَبْتُ and لَوْ تَضْرِبُ أَضْرِبُ, both meaning «had you struck, I would have struck»." + C_EN,
 "tr": "لَوْ, إِنْ'in aksinedir: muzârinin üzerine girse de mâzî içindir — لَوْ ضَرَبْتَ ضَرَبْتُ ve لَوْ تَضْرِبُ أَضْرِبُ gibi; ikisi de «sen dövseydin ben de döverdim» mânâsındadır." + C_TR},
 "tokens": [
  cited_wa("وَلَوْ", "law", "part", ["mubtada-khabar", K], "لَوْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and law».", "«lev».", "لَوْ"),
  bi_("بِعَكْسِ", "aks", "noun", ["mubtada-khabar", "idafa-definiteness"], "عَكْسِ مَجْرُورٌ مُضَافٌ — خَبَرٌ.", "«is the reverse of».", "«... aksinedir».", "عَكْسِ"),
  cited("إِنْ", "in-shartiyya", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«in».", "«in'in».", punct=":"),
  li_("لِلْمُضِيِّ", "mudiyy", "noun", ["mubtada-khabar"], "الْمُضِيِّ مَجْرُورٌ — خَبَرٌ ثَانٍ.", "«for the past».", "«mâzî içindir».", "الْمُضِيِّ", segs=[seg("لِ", "li", "prep"), seg("لْمُضِيِّ", "mudiyy", "noun")]),
  WA_IN_WASL(), DKH(), ALA(),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a muḍāriʿ».", "«muzârinin».", punct="،"),
  nahwu(),
  cited("لَوْ", "law", "part", [SH, K], "حَرْفُ شَرْطٍ لِلْمَاضِي — غَيْرُ جَازِمٍ.", "«had».", "«-seydi»."),
  DRB("ضَرَبْتَ", "فِعْلُ الشَّرْطِ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you struck».", "«sen dövseydin».", [seg("ضَرَبْ", "daraba", "verb"), prTa()]),
  DRB("ضَرَبْتُ", "جَوَابُ لَوْ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I would have struck».", "«ben de döverdim».", [seg("ضَرَبْ", "daraba", "verb"), prT()], punct="،"),
  cited_wa("وَلَوْ", "law", "part", [SH, K], "لَوْ حَرْفُ شَرْطٍ لِلْمَاضِي.", "«and had».", "«ve ... -seydi».", "لَوْ"),
  cited("تَضْرِبُ", "daraba", "verb", [SH, "fail"], "فِعْلُ الشَّرْطِ مُضَارِعٌ مَرْفُوعٌ — لَوْ لَا تَجْزِمُ، وَمَعْنَاهُ الْمُضِيُّ.", "«you struck».", "«sen dövseydin»."),
  cited("أَضْرِبُ", "daraba", "verb", [SH, "fail"], "جَوَابُ لَوْ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I would have struck».", "«ben de döverdim».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And إِنْ and لَوْ enter on a verb, stated or implied — as in His saying, exalted is He, «وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ», where the noun after إِنْ is the doer of an implied verb which the following اسْتَجَارَكَ explains." + C_EN,
 "tr": "إِنْ ve لَوْ lafzen ya da takdiren bir fiilin üzerine girer — Allah Teâlâ'nın «وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ» kavlindeki gibi: إِنْ'den sonraki isim, ardındaki اسْتَجَارَكَ'nin açıkladığı takdirî bir fiilin fâilidir." + C_TR},
 "tokens": [
  cited_wa("وَإِنْ", "in-shartiyya", "part", ["mubtada-khabar", K], "إِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and in».", "«in».", "إِنْ"),
  cited_wa("وَلَوْ", "law", "part", [AT], "لَوْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and law».", "«ve lev».", "لَوْ"),
  W("تَدْخُلَانِ", "dakhala", "verb", ["mubtada-khabar", "fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْأَلِفُ فَاعِلٌ — الْجُمْلَةُ خَبَرٌ.", "«enter».", "«girer»."),
  ALA(),
  W("الْفِعْلِ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«fiilin»."),
  W("لَفْظًا", "lafz", "adv", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«stated».", "«lafzen»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("تَقْدِيرًا", "taqdir", "adv", [AT, "tamyiz"], "مَعْطُوفٌ مَنْصُوبٌ.", "«implied».", "«takdiren».", punct="،"),
  ka_("كَمَا", "ma-masdariyya", "part", ["anwa-ma"], "مَا مَصْدَرِيَّةٌ — أَوْ كَافَّةٌ.", "«as».", "«... gibi».", "مَا", segs=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-deki»."),
  W("قَوْلِهِ", "qawl", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying».", "«kavli».", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  W("تَعَالَى", "taala", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«exalted is He».", "«Teâlâ».", punct=":"),
  cited_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", SH, K], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if».", "«ve eğer».", "إِنْ"),
  cited("أَحَدٌ", "ahad", "noun", ["fail", "hadhf-wa-taqdir", SH], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ بَعْدَهُ: إِنِ اسْتَجَارَكَ أَحَدٌ.", "«any one».", "«biri»."),
  cited("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  cited("الْمُشْرِكِينَ", "mushrik", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "form-iv-verbs"], "مَجْرُورٌ بِالْيَاءِ.", "«the polytheists».", "«müşriklerden».", punct="،"),
  W("فَالِاسْمُ", "ism", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالِاسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the noun».", "«isim».", segments=[seg("فَ", "fa", "conj"), seg("الِاسْمُ", "ism", "noun")]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonraki»."),
  cited("إِنْ", "in-shartiyya", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«in».", "«in»."),
  W("فَاعِلُ", "fail-doer", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the doer of».", "«fâilidir»."),
  W("فِعْلٍ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«bir fiilin»."),
  W("مُقَدَّرٍ", "muqaddar", "noun", ["naat-sifa", "ism-maful", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«implied».", "«takdirî»."),
  W("يُفَسِّرُهُ", "fassara", "verb", ["naat-sifa", "fail", "maful-bihi", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ صِفَةٌ ثَانِيَةٌ.", "«which explains».", "«açıkladığı».", segments=[seg("يُفَسِّرُ", "fassara", "verb"), pr3ms()]),
  cited("اسْتَجَارَكَ", "istajara", "verb", ["fail", "maful-bihi", "form-x-verbs", "hollow-verbs"], "فَاعِلُ يُفَسِّرُ — اللَّفْظُ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«asks you for protection».", "«senden eman dilerse».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And for this reason one says after لَوْ: لَوْ أَنَّكَ, with the fatḥa — because أَنَّ together with its noun and its predicate is the doer of an implied verb, ثَبَتَ." + C_EN,
 "tr": "Bu sebeple لَوْ'den sonra fetha ile لَوْ أَنَّكَ denir — çünkü أَنَّ, ismi ve haberiyle beraber takdirî bir fiilin, ثَبَتَ'nin, fâilidir." + C_TR},
 "tokens": [
  atf_wa("وَلِذَلِكَ", "dhalika", "pron", ["huruf-jarr", "asma-al-ishara-wal-mawsulat"], "اللَّامُ لِلتَّعْلِيلِ، وَذَلِكَ فِي مَحَلِّ جَرٍّ.", "«and for this reason».", "«ve bu sebeple».", "ذَلِكَ", extra_segs=[seg("لِ", "lam-taleel", "part"), seg("ذَلِكَ", "dhalika", "pron")]),
  W("قِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«one says».", "«denir»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonra»."),
  cited("لَوْ", "law", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«law».", "«lev».", punct=":"),
  *LAW_ANNAKA("لَوْ أَنَّكَ — نَائِبُ فَاعِلِ قِيلَ، مَحْكِيٌّ: أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا."),
  bi_("بِالْفَتْحِ", "fath", "noun", ["hal"], "الْفَتْحِ مَجْرُورٌ — فِي مَوْضِعِ الْحَالِ.", "«with the fatḥa».", "«fetha ile».", "الْفَتْحِ", punct="؛", segs=[seg("بِ", "bi", "prep"), seg("الْفَتْحِ", "fath", "noun")]),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  cited("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ — اللَّفْظُ مَحْكِيٌّ فِي مَحَلِّ نَصْبٍ.", "«anna».", "«enne»."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«together with».", "«... ile beraber»."),
  W("اسْمِهَا", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its noun».", "«ismi».", segments=[seg("اسْمِ", "ism", "noun"), pr3fs()]),
  atf_wa("وَخَبَرِهَا", "khabar", "noun", [AT, "idafa-definiteness"], "خَبَرِ مَعْطُوفٌ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its predicate».", "«ve haberiyle».", "خَبَرِهَا", extra_segs=[seg("خَبَرِ", "khabar", "noun"), pr3fs()]),
  W("فَاعِلُ", "fail-doer", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the doer of».", "«fâilidir»."),
  W("فِعْلٍ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«bir fiilin»."),
  W("مُقَدَّرٍ", "muqaddar", "noun", ["naat-sifa", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«implied».", "«takdirî».", punct=":"),
  cited("ثَبَتَ", "thabata", "verb", ["badal", "hadhf-wa-taqdir"], "الْفِعْلُ الْمُقَدَّرُ — بَدَلٌ مِنْ فِعْلٍ، مَحْكِيٌّ: لَوْ ثَبَتَ انْطِلَاقُكَ.", "«thabata, «it is established»».", "«sebete, «sâbit oldu»».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And one says لَوْ أَنَّكَ انْطَلَقْتَ انْطَلَقْتُ in place of لَوْ أَنَّكَ مُنْطَلِقٌ انْطَلَقْتُ — so that the verb mentioned in the place of the active participle stands as a substitute for the dropped verb." + C_EN,
 "tr": "لَوْ أَنَّكَ مُنْطَلِقٌ انْطَلَقْتُ yerine لَوْ أَنَّكَ انْطَلَقْتَ انْطَلَقْتُ denir — ism-i fâil yerinde zikredilen fiil, hazfedilen fiilden ivaz gibi olsun diye." + C_TR},
 "tokens": [
  atf_wa("وَقِيلَ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "قِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and one says».", "«ve ... denir».", "قِيلَ", punct=":"),
  *LAW_ANNAKA(),
  cited("انْطَلَقْتَ", "intalaqa", "verb", ["inna-wa-akhawatuha", "fail", "form-vii-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — الْجُمْلَةُ خَبَرُ أَنَّ، وَقَعَتْ مَوْضِعَ اسْمِ الْفَاعِلِ.", "«set out».", "«yola çıksaydın».", segments=[seg("انْطَلَقْ", "intalaqa", "verb"), prTa()]),
  cited("انْطَلَقْتُ", "intalaqa", "verb", ["fail", "form-vii-verbs", SH], "جَوَابُ لَوْ، وَالتَّاءُ فَاعِلٌ.", "«I would have set out».", "«ben de çıkardım».", segments=[seg("انْطَلَقْ", "intalaqa", "verb"), prT()]),
  W("مَوْضِعَ", "mawdi", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«in place of».", "«yerine».", punct=":"),
  *LAW_ANNAKA(),
  cited("مُنْطَلِقٌ", "muntaliq", "noun", ["inna-wa-akhawatuha", "ism-fail", "form-vii-verbs"], "خَبَرُ أَنَّ مَرْفُوعٌ — اسْمُ فَاعِلٍ.", "«setting out».", "«yola çıkmış olsaydın»."),
  cited("انْطَلَقْتُ", "intalaqa", "verb", ["fail", "form-vii-verbs", SH], "جَوَابُ لَوْ، وَالتَّاءُ فَاعِلٌ.", "«I would have set out».", "«ben de çıkardım».", punct="،", segments=[seg("انْطَلَقْ", "intalaqa", "verb"), prT()]),
  li_("لِيَكُونَ", "kana", "verb", ["nawasib-wa-jawazim-al-mudari", "kana-wa-akhawatuha", "lam-taleel", "hollow-verbs"], "يَكُونَ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ لَامِ التَّعْلِيلِ.", "«so that may be».", "«... olsun diye».", "يَكُونَ", segs=[seg("لِ", "lam-taleel", "part"), seg("يَكُونَ", "kana", "verb")]),
  W("الْفِعْلُ", "fil", "noun", ["kana-wa-akhawatuha"], "اسْمُ يَكُونَ مَرْفُوعٌ.", "«the verb».", "«fiil»."),
  W("الْمَذْكُورُ", "madhkur", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«mentioned».", "«zikredilen»."),
  W("مَوْضِعَ", "mawdi", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«in the place of».", "«yerinde»."),
  W("اسْمِ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the noun of».", "«ism-i»."),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâil»."),
  ka_("كَالْعِوَضِ", "iwad", "noun", ["kana-wa-akhawatuha"], "الْعِوَضِ مَجْرُورٌ — خَبَرُ يَكُونَ.", "«as a substitute».", "«ivaz gibi».", "الْعِوَضِ", segs=[seg("كَ", "ka", "prep"), seg("الْعِوَضِ", "iwad", "noun")]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  W("الْفِعْلِ", "fil", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the verb».", "«fiil»."),
  W("الْمَحْذُوفِ", "mahdhuf", "noun", ["naat-sifa", "ism-maful", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«dropped».", "«hazfedilen».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And if the predicate is a rigid noun, its being the predicate is permitted — since a verb cannot come in its place — as «وَلَوْ أَنَّ مَا فِي الْأَرْضِ مِنْ شَجَرَةٍ أَقْلَامٌ»." + C_EN,
 "tr": "Haber câmid olursa, yerine fiil gelmesi mümkün olmadığından, câmid ismin haber olması câizdir — «وَلَوْ أَنَّ مَا فِي الْأَرْضِ مِنْ شَجَرَةٍ أَقْلَامٌ» âyetindeki أَقْلَامٌ gibi." + C_TR},
 "tokens": [
  W("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", SH], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ.", "«and if».", "«... olursa».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is».", "«olursa»."),
  W("الْخَبَرُ", "khabar", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the predicate».", "«haber»."),
  W("جَامِدًا", "jamid", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«a rigid noun».", "«câmid»."),
  W("جَازَ", "jaaza", "verb", ["fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ — جَوَابُ الشَّرْطِ.", "«is permitted».", "«câizdir»."),
  W("كَوْنُهُ", "kawn", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its being».", "«onun ... olması».", segments=[seg("كَوْنُ", "kawn", "noun"), pr3ms()]),
  W("خَبَرًا", "khabar", "noun", ["maful-bihi"], "خَبَرُ الْمَصْدَرِ النَّاقِصِ مَنْصُوبٌ.", "«the predicate».", "«haber».", punct="،"),
  W("إِذْ", "idh", "noun", ["maful-fih", "lam-taleel"], "حَرْفُ تَعْلِيلٍ.", "«since».", "«... -dığından»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-ma-»."),
  W("يُمْكِنُ", "amkana", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«can».", "«mümkün»."),
  W("مَجِيءُ", "maji", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the coming of».", "«gelmesi»."),
  W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb».", "«fiilin»."),
  W("مَوْضِعَهُ", "mawdi", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in its place».", "«yerine».", punct="،", segments=[seg("مَوْضِعَ", "mawdi", "noun"), pr3ms()]),
  nahwu(),
  cited_wa("وَلَوْ", "law", "part", [SH, K], "الْوَاوُ عَاطِفَةٌ، وَلَوْ حَرْفُ شَرْطٍ.", "«and if».", "«ve eğer».", "لَوْ"),
  cited("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ فَاعِلُ ثَبَتَ الْمُقَدَّرِ.", "«(that)».", "«(ki)»."),
  cited("مَا", "ma-mawsula", "pron", ["inna-wa-akhawatuha", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«what».", "«... olan»."),
  cited("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةٌ.", "«in».", "«-de»."),
  cited("الْأَرْضِ", "ard", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the earth».", "«yerde»."),
  cited("مِنْ", "min", "prep", ["huruf-jarr", "tamyiz"], "حَرْفُ جَرٍّ لِلْبَيَانِ.", "«of».", "«-den»."),
  cited("شَجَرَةٍ", "shajara", "noun", ["huruf-jarr"], "مَجْرُورٌ — بَيَانٌ لِمَا.", "«tree».", "«ağaç»."),
  cited("أَقْلَامٌ", "qalam", "noun", ["inna-wa-akhawatuha", "jam-taksir", K], "خَبَرُ أَنَّ مَرْفُوعٌ — اسْمٌ جَامِدٌ، فَلَمْ يُوضَعْ فِعْلٌ مَوْضِعَهُ.", "«were pens».", "«kalem olsaydı».", punct="."),
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
 "jamid": need("jamid", "جَامِد", "ج م د", "noun", "rigid, non-derived — a noun not taken from a verb (ism jāmid), or a verb with one tense", "câmid — bir fiilden türetilmemiş isim (ism-i câmid) ya da tek zamanlı fiil", 4),
 "mudiyy": need("mudiyy", "مُضِيّ", "م ض ي", "noun", "the past, past time (masdar of مَضَى)", "mâzî zaman, geçmişlik (medâ'nın masdarı)", 4),
 "intalaqa": need("intalaqa", "اِنْطَلَقَ", "ط ل ق", "verb", "to set out, to depart (Form VII)", "yola çıkmak, gitmek (infiʿâl)", 3),
 "istajara": need("istajara", "اِسْتَجَارَ", "ج و ر", "verb", "to ask for protection (Form X, hollow)", "eman dilemek, sığınmak (istifʿâl, ecvef)", 4),
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
put_morph(mo, "intalaqa", _nfc(_sg.derived(_sg.B7, getattr(_sg, "W7", "اِنْفَعَلَ يَنْفَعِلُ"), "َ", "اِنْطَلَق", "نْطَلِق", "اِنْطَلِق", "اِنْطِلَاق", "مُنْطَلِق", "مُنْطَلَق", "اُنْطُلِقَ", "يُنْطَلَقُ", "اِنْطَلَقَ: ذَهَبَ وَمَضَى — بَابُ الِانْفِعَالِ.")))
put_morph(mo, "istajara", _nfc(_sg.entry(_sg.B10 + " — أَجْوَفُ وَاوِيٌّ", _sg.W10, "اِسْتِجَارَة", "مُسْتَجِير", _sg.mazi14("اِسْتَجَار", "اِسْتَجَر"), _sg.mudari14("َ", "سْتَجِير", "سْتَجِر"), ["اِسْتَجِرْ", "اِسْتَجِيرَا", "اِسْتَجِيرُوا", "اِسْتَجِيرِي", "اِسْتَجِيرَا", "اِسْتَجِرْنَ"], "يَسْتَجِيرَ", "يَسْتَجِرْ", "تَسْتَجِرْ", "مُسْتَجَار", "اُسْتُجِيرَ", "يُسْتَجَارُ", "اِسْتَجَارَ بِهِ: طَلَبَ جِوَارَهُ وَحِمَايَتَهُ — بَابُ الِاسْتِفْعَالِ مِنَ الْأَجْوَفِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "حُرُوفُ الشَّرْطِ فِي الْكَافِيَةِ: إِنْ وَلَوْ وَلَوْ أَنَّ", "en": "The conditional letters in the Kafiya: in turns a past verb to the future, law turns a present verb to the past, both need a verb, and that is why law anna takes the fatha", "tr": "Kâfiye'de şart harfleri: in mâzîyi geleceğe, lev muzâriyi geçmişe çevirir, ikisi de fiil ister ve lev enne bu yüzden fetha alır"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — حروف الشرط إن ولو وأما؛ إن للاستقبال وإن دخلت على الماضي؛ لو للماضي وإن دخلت على المضارع؛ لو أنك بالفتح", "ضياء صونغور اوغلى — دفتر الكافية: إن ولو تدخلان على الفعل لفظا أو تقديرا؛ أنّ مع اسمها وخبرها فاعل فعل مقدر؛ الفعل موضع اسم الفاعل كالعوض؛ الخبر الجامد جائز"],
 "question": {
  "en": ["What do إِنْ and لَوْ do to the tense? They override it. إِنْ makes even a past verb future (إِنْ أَكْرَمْتَنِي = «if you honour me», not «if you honoured me»); لَوْ makes even a present verb past (لَوْ تَضْرِبُ = «had you struck»). In a conditional clause the tense is read off the letter, not off the verb's form.",
         "Which of the two governs jazm? Only إِنْ: تُكْرِمْنِي / أُكْرِمْكَ lose their ḍamma. لَوْ governs nothing — تَضْرِبُ / أَضْرِبُ keep their rafʿ — which is why the two are listed together as conditional letters but only one of them among the jāzim governors.",
         "Why does أَحَدٌ follow إِنْ in وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ when a conditional letter wants a verb? Because the verb is there, implied, and the stated اسْتَجَارَكَ after the noun EXPLAINS it: the structure is إِنِ اسْتَجَارَكَ أَحَدٌ … اسْتَجَارَكَ. The noun is the doer of the hidden verb, not a mubtadaʾ.",
         "Why لَوْ أَنَّكَ with the fatḥa and never لَوْ إِنَّكَ? Because the same rule holds: لَوْ wants a verb, so a verb is implied — ثَبَتَ — and أَنَّ with its clause is that verb's DOER, a maṣdar in rafʿ; the hamza is read on the position (inna-am-anna). The iʿrāb lines here supply exactly this ثَبَتَ.",
         "Why do the books prefer لَوْ أَنَّكَ انْطَلَقْتَ to لَوْ أَنَّكَ مُنْطَلِقٌ? Because a verb has been dropped (ثَبَتَ), and putting a verb in the khabar's place — where a participle would otherwise stand — compensates for it. When the khabar is a rigid noun (أَقْلَامٌ, 31:27) no verb can stand there, so the rigid khabar is simply allowed.",
         "What is أَمَّا doing in this list? It is the third conditional letter, with its own fāʾ and its own chapter next; it is named here and treated there."],
  "tr": ["إِنْ ve لَوْ zamana ne yapar? Onu geçersiz kılar. إِنْ mâzîyi bile geleceğe çevirir (إِنْ أَكْرَمْتَنِي = «bana ikram edersen», «ettiysen» değil); لَوْ muzâriyi bile geçmişe çevirir (لَوْ تَضْرِبُ = «dövseydin»). Şart cümlesinde zaman fiilin şeklinden değil harften okunur.",
         "İkisinden hangisi cezm eder? Yalnız إِنْ: تُكْرِمْنِي / أُكْرِمْكَ dammesini kaybeder. لَوْ hiçbir şeyi yönetmez — تَضْرِبُ / أَضْرِبُ ref'ini korur — bu yüzden ikisi şart harfi olarak birlikte sayılır ama câzim âmiller arasında yalnız biri.",
         "Şart harfi fiil isterken وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ'de إِنْ'i niçin أَحَدٌ izler? Çünkü fiil oradadır, takdirîdir ve isimden sonraki zikredilen اسْتَجَارَكَ onu AÇIKLAR: yapı إِنِ اسْتَجَارَكَ أَحَدٌ … اسْتَجَارَكَ'dir. İsim gizli fiilin fâilidir, mübteda değil.",
         "Niçin fetha ile لَوْ أَنَّكَ, asla لَوْ إِنَّكَ değil? Çünkü aynı kural geçerlidir: لَوْ fiil ister, demek bir fiil takdir edilir — ثَبَتَ — ve أَنَّ cümlesiyle o fiilin FÂİLİDİR, merfû bir masdar; hemze konuma göre okunur (inna-am-anna). Buradaki i'râb satırları tam bu ثَبَتَ'yi verir.",
         "Kitaplar لَوْ أَنَّكَ مُنْطَلِقٌ yerine niçin لَوْ أَنَّكَ انْطَلَقْتَ'yi tercih eder? Çünkü bir fiil hazfedilmiştir (ثَبَتَ) ve haberin yerine — aksi hâlde ism-i fâilin duracağı yere — bir fiil koymak onu telâfi eder. Haber câmid bir isim olunca (أَقْلَامٌ, 31:27) oraya fiil gelemez; câmid haber olduğu gibi câizdir.",
         "أَمَّا bu listede ne yapıyor? Kendi fâ'sı ve bir sonraki kendi bâbıyla üçüncü şart harfidir; burada adı anılır, orada işlenir."]},
 "plain": {
  "en": "Two «if» words. In points forward: even a past-tense verb after it means the future. Law points backward: even a present-tense verb after it means «had you…». Both want a verb right after them, so when a noun comes instead, a verb is understood — and that is why you say law anna, with a fatha.",
  "tr": "İki «eğer». İn ileriyi gösterir: ardındaki mâzî bile gelecek demektir. Lev geriyi gösterir: ardındaki muzâri bile «-seydin» demektir. İkisi de hemen ardında fiil ister; isim gelince fiil anlaşılır — lev enne'nin fethayla söylenmesi bundandır."},
 "explanation": {
  "en": "The Kafiya's conditional letters, with the notebook's two symmetrical rules (إِنْ future, لَوْ past, each against the verb's own tense) and the consequence the notebook draws from «they enter on a verb, stated or implied»: the fatḥa of لَوْ أَنَّ, the preference for a verb in the khabar as compensation for the dropped one, and the licence of the rigid khabar. The Qur'anic citations are 9:6 (cited to the span the notebook cites, with the explaining verb named in the iʿrāb) and 31:27. The chapter closes at the point where the notebook turns to the oath meeting the condition, which is the next chapter.",
  "tr": "Kâfiye'nin şart harfleri, defterin iki simetrik kuralıyla (إِنْ gelecek, لَوْ geçmiş, her biri fiilin kendi zamanına karşı) ve defterin «lafzen ya da takdiren bir fiile girerler»den çıkardığı sonuçla: لَوْ أَنَّ'nin fethası, hazfedilen fiile karşılık haberde fiil tercihi ve câmid haberin cevazı. Kur'ân iktibasları 9:6 (defterin iktibas ettiği aralıkla, açıklayan fiil i'râbda adlandırılarak) ve 31:27'dir. Bâb, defterin kasemin şartla buluşmasına döndüğü yerde biter; o bir sonraki bâbdır."},
 "examples": [
  {"ar": "إِنْ أَكْرَمْتَنِي أَكْرَمْتُكَ", "en": "In: a past verb read as future.", "tr": "İn: mâzî gelecek okunur.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "لَوْ تَضْرِبُ أَضْرِبُ", "en": "Law: a present verb read as past.", "tr": "Lev: muzâri geçmiş okunur.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "وَإِنْ أَحَدٌ مِنَ الْمُشْرِكِينَ", "en": "A noun after in — the verb is implied.", "tr": "İn'den sonra isim — fiil takdirîdir.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "لَوْ أَنَّكَ انْطَلَقْتَ انْطَلَقْتُ", "en": "Law anna with the fatha; the verb in the khabar's place.", "tr": "Fethayla lev enne; haber yerinde fiil.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَلَوْ أَنَّ مَا فِي الْأَرْضِ مِنْ شَجَرَةٍ أَقْلَامٌ", "en": "A rigid khabar after law anna.", "tr": "Lev enne'den sonra câmid haber.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«لَوْ إِنَّكَ انْطَلَقْتَ»",
   "right": "«لَوْ أَنَّكَ انْطَلَقْتَ — enne, takdirî ثَبَتَ'nin fâilidir»",
   "why": {"en": "After law a verb is implied and anna's clause is its doer: a masdar position takes the fatha.", "tr": "Lev'den sonra fiil takdir edilir ve enne cümlesi onun fâilidir: masdar konumu fetha alır."}},
  {"wrong": "«لَوْ تَضْرِبْ أَضْرِبْ»",
   "right": "«لَوْ تَضْرِبُ أَضْرِبُ — lev cezm etmez»",
   "why": {"en": "Only in is a jāzim; law leaves the verbs in rafʿ.", "tr": "Yalnız in câzimdir; lev fiilleri ref'te bırakır."}},
  {"wrong": "«إِنْ أَكْرَمْتَنِي = bana ikram ettiysen»",
   "right": "«= bana ikram edersen — in mâzîyi geleceğe çevirir»",
   "why": {"en": "The letter sets the time, not the verb's form.", "tr": "Zamanı fiilin şekli değil harf belirler."}}],
 "relatedNotes": ["in-shartiyya", "al-majzum-wal-shart-wal-jaza", "idha-shartiyya", "inna-am-anna", "hadhf-wa-taqdir", "amma-tafsiliyya"]}

ADD_EN = (" Chapter 41 (notebook lines ~346-347): the conditional letters — in for the future, law for the past, both on a verb stated or implied (9:6 cited to the notebook's span), the fatha of law anna, the verb in the khabar's place, the rigid khabar (31:27) — the notebook's exposition, kept as commentary (s1-s7).")
ADD_TR = (" Kırk birinci bâb (defter satırları ~346-347): şart harfleri — gelecek için in, geçmiş için lev, ikisi de lafzen ya da takdiren fiil üzerine (9:6 defterin aralığıyla), lev enne'nin fethası, haber yerinde fiil, câmid haber (31:27) — defterin açıklaması, şerh olarak (s1-s7).")
write_out(41, S, TITLE, ADD_EN, ADD_TR, "346-347", GLOSS_ADD, notes=(NOTE,),
          related=(("in-shartiyya", [K]), ("inna-am-anna", [K])))
report(41, S, GLOSS_ADD, (NOTE,))
