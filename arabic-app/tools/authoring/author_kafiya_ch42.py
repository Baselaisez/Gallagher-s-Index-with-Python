# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 42: THE OATH MEETING THE CONDITION — an oath at the head makes the condition māḍī (in wording or in sense)
and takes the answer for itself in wording (وَاللهِ إِنْ أَتَيْتَنِي لَأَكْرَمْتُكَ); an oath in the middle may be regarded or cancelled
(أَنَا وَاللهِ إِنْ تَأْتِنِي آتِكَ — the condition regarded, the yāʾ dropped; إِنْ أَتَيْتَنِي وَاللهِ لَآتِيَنَّكَ — the oath regarded);
an implied oath counts like a stated one (59:12 لَئِنْ أُخْرِجُوا لَا يَخْرُجُونَ, 6:121 وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ).
Source: the Ottoman notebook (Ziya Sungur-oglu), line ~347 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch42.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-qasam-wal-shart-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "اِجْتِمَاعُ الْقَسَمِ وَالشَّرْطِ", "en": "When the oath meets the condition — which of the two gets the answer", "tr": "Kasem ile şartın buluşması — cevap ikisinden hangisinin"}
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
QS = "huruf-al-qasam-fil-kafiya"
def WALLAHI(wa=False, punct=None):
    if wa: return cited_wa("وَوَاللهِ", "allah", "propn", [QS, "huruf-jarr"], "الْوَاوُ الْأُولَى عَاطِفَةٌ، وَالثَّانِيَةُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«and by Allah».", "«ve vallahi».", "وَاللهِ", punct=punct, extra_segs=[seg("وَ", "waw-qasam", "part"), seg("اللهِ", "allah", "propn")])
    return cited("وَاللهِ", "allah", "propn", [QS, "huruf-jarr"], "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by Allah».", "«vallahi».", punct=punct, segments=[seg("وَ", "waw-qasam", "part"), seg("اللهِ", "allah", "propn")])
def QASAM(full, tags, ar, en="«the oath».", tr="«kasem».", punct=None): return W(full, "qasam", "noun", tags, ar, en, tr, punct=punct)
def SHART(full, tags, ar, en="«the condition».", tr="«şart».", punct=None): return W(full, "shart", "noun", tags + [SH], ar, en, tr, punct=punct)
def UTUBIRA(full="فَاعْتُبِرَ", segs=None, ar=None, en="«so was regarded».", tr="«... itibar edildi»."):
    segs = segs or [seg("فَ", "fa", "conj"), seg("اعْتُبِرَ", "itabara", "verb")]
    return W(full, "itabara", "verb", ["naib-al-fail", "form-viii-verbs"], ar or "الْفَاءُ لِلتَّفْرِيعِ، وَاعْتُبِرَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", en, tr, segments=segs)
def ULGHIYA(): return atf_wa("وَأُلْغِيَ", "algha", "verb", ["naib-al-fail", "form-iv-verbs", "naqis-verbs"], "أُلْغِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and was cancelled».", "«ve ... lağvedildi».", "أُلْغِيَ")
def MADIYAN(punct=None): return W("مَاضِيًا", "madi", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ الْكَوْنِ مَنْصُوبٌ.", "«past».", "«mâzî».", punct=punct)
def BIKAWN(): return bi_("بِكَوْنِ", "kawn", "noun", ["idafa-definiteness"], "كَوْنِ مَجْرُورٌ، وَهُوَ مُضَافٌ — الْبَاءُ لِلسَّبَبِيَّةِ.", "«by the condition's being».", "«... olmasıyla».", "كَوْنِ")
def WAMAJI(): return atf_wa("وَمَجِيءِ", "maji", "noun", [AT, "idafa-definiteness"], "مَجِيءِ مَعْطُوفٌ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«and the coming of».", "«ve ... gelmesiyle».", "مَجِيءِ")
def FIL_JAWAB(punct=None): return [W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-ta»."), W("الْجَوَابِ", "jawab", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the answer».", "«cevapta».", punct=punct)]
def QUDDIRA(): return [W("قُدِّرَ", "qaddara", "verb", ["naib-al-fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is implied».", "«takdir edilmiştir»."), QASAM("الْقَسَمُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ."), W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."), W("أَوَّلِهِ", "awwal", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its head».", "«başında».", punct="،", segments=[seg("أَوَّلِ", "awwal", "noun"), pr3msi()])]
def LAW_UTUBIRA(): return [cited_wa("وَلَوِ", "law", "part", [SH], "لَوِ حَرْفُ شَرْطٍ لِلِامْتِنَاعِ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and had».", "«ve ... -seydi».", "لَوِ"), W("اعْتُبِرَ", "itabara", "verb", [SH, "naib-al-fail", "form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — فِعْلُ الشَّرْطِ.", "«been regarded».", "«itibar edilseydi»."), SHART("الشَّرْطُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.")]

S.append({"id": "s1", "translation": {
 "en": "And when the oath precedes the condition at the head of the sentence, the condition must be past, in wording or in sense; and the answer is in wording for the oath alone, and in sense for both." + C_EN,
 "tr": "Kasem lafzı sözün başında şartın önüne geçtiğinde şartın lafzen ya da mânen mâzî olması lâzımdır; cevap lafız bakımından yalnız kasemin, mânâ bakımından hem kasemin hem şartın olur." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... zaman».", "إِذَا"),
  W("تَقَدَّمَ", "taqaddama", "verb", ["idha-shartiyya", "fail", "form-v-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«precedes».", "«öne geçtiği»."),
  QASAM("الْقَسَمُ", ["fail", QS], "فَاعِلٌ مَرْفُوعٌ."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«(over)».", "«-ın önüne»."),
  SHART("الشَّرْطِ", ["huruf-jarr"], "مَجْرُورٌ."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-de»."),
  W("صَدْرِ", "sadr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the head of».", "«başında»."),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«sözün»."),
  W("لَزِمَ", "lazima", "verb", ["fail", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ — جَوَابُ إِذَا.", "«must».", "«lâzımdır»."),
  W("كَوْنُ", "kawn", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ — مَصْدَرٌ نَاقِصٌ.", "«the being of».", "«olması»."),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ."),
  MADIYAN(),
  W("لَفْظًا", "lafz", "adv", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in wording».", "«lafzen»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مَعْنًى", "mana", "noun", [AT, "tamyiz", "ism-maqsur-manqus"], "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«in sense».", "«mânen».", punct="؛"),
  atf_wa("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and is».", "«ve ... olur».", "كَانَ"),
  W("الْجَوَابُ", "jawab", "noun", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«the answer».", "«cevap»."),
  li_("لِلْقَسَمِ", "qasam", "noun", ["kana-wa-akhawatuha"], "الْقَسَمِ مَجْرُورٌ — خَبَرُ كَانَ.", "«for the oath».", "«kasemin».", "الْقَسَمِ", segs=[seg("لِ", "li", "prep"), seg("لْقَسَمِ", "qasam", "noun")]),
  W("لَفْظًا", "lafz", "adv", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in wording».", "«lafız bakımından»."),
  atf_wa("وَلَهُمَا", "li", "prep", [AT, "huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ — مَعْطُوفٌ عَلَى لِلْقَسَمِ.", "«and for both».", "«ve ikisinin».", "لَهُمَا", extra_segs=[seg("لَ", "li", "prep"), pr3d()]),
  W("مَعْنًى", "mana", "noun", ["tamyiz", "ism-maqsur-manqus"], "تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«in sense».", "«mânâ bakımından».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "As وَاللهِ إِنْ أَتَيْتَنِي لَأَكْرَمْتُكَ and وَاللهِ إِنْ لَمْ تَأْتِنِي لَأَكْرَمْتُكَ: the condition in the first is past in wording, in the second in sense; and the answer comes with the lām because in wording it is the answer of the oath." + C_EN,
 "tr": "وَاللهِ إِنْ أَتَيْتَنِي لَأَكْرَمْتُكَ ve وَاللهِ إِنْ لَمْ تَأْتِنِي لَأَكْرَمْتُكَ gibi: birincide şart lafzen, ikincide mânen mâzî olmuştur; cevap lafız bakımından kasemin cevabı olduğu için lâm ile gelmiştir." + C_TR},
 "tokens": [
  nahwu(),
  WALLAHI(),
  cited("إِنْ", "in-shartiyya", "part", ["in-shartiyya", SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-sen»."),
  cited("أَتَيْتَنِي", "ata", "verb", [SH, "fail", "maful-bihi", "naqis-verbs"], "فِعْلُ الشَّرْطِ مَاضٍ لَفْظًا، وَالتَّاءُ فَاعِلٌ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you come to me».", "«bana gelirsen».", segments=[seg("أَتَيْ", "ata", "verb"), prTa(), pr1s()]),
  cited("لَأَكْرَمْتُكَ", "akrama", "verb", [QS, "fail", "maful-bihi", "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَأَكْرَمْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — جَوَابُ الْقَسَمِ لَفْظًا، وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ.", "«I will surely honour you».", "«elbette sana ikram ederim».", punct="،", segments=[seg("لَ", "lam-qasam", "part"), seg("أَكْرَمْ", "akrama", "verb"), prT(), pr2ms()]),
  WALLAHI(wa=True),
  cited("إِنْ", "in-shartiyya", "part", ["in-shartiyya", SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«-sen»."),
  cited("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ — يَقْلِبُ الْمُضَارِعَ إِلَى الْمُضِيِّ.", "«not».", "«-me-»."),
  cited("تَأْتِنِي", "ata", "verb", [SH, "nawasib-wa-jawazim-al-mudari", "fail", "maful-bihi", "naqis-verbs"], "فِعْلُ الشَّرْطِ مُضَارِعٌ مَجْزُومٌ بِلَمْ بِحَذْفِ الْيَاءِ — مَاضٍ مَعْنًى، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you come to me».", "«bana gelmezsen».", segments=[seg("تَأْتِ", "ata", "verb"), pr1s()]),
  cited("لَأَكْرَمْتُكَ", "akrama", "verb", [QS, "fail", "maful-bihi", "form-iv-verbs"], "اللَّامُ لِجَوَابِ الْقَسَمِ، وَأَكْرَمْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«I will surely honour you».", "«elbette sana ikram ederim».", punct="؛", segments=[seg("لَ", "lam-qasam", "part"), seg("أَكْرَمْ", "akrama", "verb"), prT(), pr2ms()]),
  W("فَالشَّرْطُ", "shart", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada", SH], "الْفَاءُ لِلتَّفْرِيعِ، وَالشَّرْطُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the condition».", "«şart».", segments=[seg("فَ", "fa", "conj"), seg("الشَّرْطُ", "shart", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْأَوَّلِ", "awwal", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the first».", "«birincide»."),
  W("مَاضٍ", "madi", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ.", "«is past».", "«mâzîdir»."),
  W("لَفْظًا", "lafz", "adv", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in wording».", "«lafzen»."),
  atf_wa("وَفِي", "fi", "prep", [AT, "huruf-jarr"], "فِي حَرْفُ جَرٍّ.", "«and in».", "«ve -de».", "فِي"),
  W("الثَّانِي", "thani", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second».", "«ikincide»."),
  W("مَعْنًى", "mana", "noun", ["tamyiz", "ism-maqsur-manqus"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in sense».", "«mânen».", punct="،"),
  atf_wa("وَجَاءَ", "jaa", "verb", ["fail", "hollow-verbs"], "جَاءَ فِعْلٌ مَاضٍ.", "«and comes».", "«ve ... gelmiştir».", "جَاءَ"),
  W("الْجَوَابُ", "jawab", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the answer».", "«cevap»."),
  bi_("بِاللَّامِ", "lam-letter", "noun", [], "اللَّامِ مَجْرُورٌ.", "«with the lām».", "«lâm ile».", "اللَّامِ", segs=[seg("بِ", "bi", "prep"), seg("اللَّامِ", "lam-letter", "noun")]),
  W("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«because it».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  W("جَوَابُ", "jawab", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is the answer of».", "«cevabıdır»."),
  QASAM("الْقَسَمِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«kasemin»."),
  W("لَفْظًا", "lafz", "adv", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ.", "«in wording».", "«lafız bakımından».", punct="."),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And when the oath falls in the middle — by the fronting of the condition or of something else — it is permitted to regard the oath and cancel the condition, and permitted to regard the condition and cancel the oath." + C_EN,
 "tr": "Kasem, şartın ya da başka bir şeyin öne alınmasıyla sözün ortasına düşerse, kaseme itibar edilip şartın lağvedilmesi de câizdir, şarta itibar edilip kasemin lağvedilmesi de câizdir." + C_TR},
 "tokens": [
  atf_wa("وَإِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "إِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... -se».", "إِذَا"),
  W("تَوَسَّطَ", "tawassata", "verb", ["idha-shartiyya", "fail", "form-v-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«falls in the middle».", "«ortaya düşerse»."),
  QASAM("الْقَسَمُ", ["fail", QS], "فَاعِلٌ مَرْفُوعٌ."),
  bi_("بِتَقْدِيمِ", "taqdim", "noun", ["idafa-definiteness", "form-ii-verbs"], "تَقْدِيمِ مَجْرُورٌ، وَهُوَ مُضَافٌ — الْبَاءُ لِلسَّبَبِيَّةِ.", "«by the fronting of».", "«... öne alınmasıyla».", "تَقْدِيمِ"),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«şartın»."),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("غَيْرِهِ", "ghayr", "noun", [AT, "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«something else».", "«başka bir şeyin».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()]),
  W("جَازَ", "jaaza", "verb", ["fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ — جَوَابُ إِذَا.", "«it is permitted».", "«câizdir»."),
  W("اِعْتِبَارُ", "itibar", "noun", ["fail", "idafa-definiteness", "form-viii-verbs"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«regarding».", "«... itibar edilmesi»."),
  QASAM("الْقَسَمِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«kaseme»."),
  atf_wa("وَإِلْغَاءُ", "ilgha", "noun", [AT, "idafa-definiteness", "form-iv-verbs"], "إِلْغَاءُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and cancelling».", "«ve ... lağvedilmesi».", "إِلْغَاءُ"),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«şartın».", punct="،"),
  atf_wa("وَجَازَ", "jaaza", "verb", ["fail", "hollow-verbs"], "جَازَ فِعْلٌ مَاضٍ.", "«and permitted».", "«ve câizdir».", "جَازَ"),
  W("اِعْتِبَارُ", "itibar", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«regarding».", "«... itibar edilmesi»."),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«şarta»."),
  atf_wa("وَإِلْغَاءُ", "ilgha", "noun", [AT, "idafa-definiteness"], "إِلْغَاءُ مَعْطُوفٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and cancelling».", "«ve ... lağvedilmesi».", "إِلْغَاءُ"),
  QASAM("الْقَسَمِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«kasemin».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "As أَنَا وَاللهِ إِنْ تَأْتِنِي آتِكَ: the oath falls in the middle by the fronting of أَنَا, so the condition is regarded and the oath cancelled — by the dropping of the yāʾ from the answer." + C_EN,
 "tr": "أَنَا وَاللهِ إِنْ تَأْتِنِي آتِكَ gibi: أَنَا'nın öne alınmasıyla kasem ortaya düşmüş, şarta itibar edilip kasem lağvedilmiştir — cezadan yâ'nın düşmesiyle." + C_TR},
 "tokens": [
  nahwu(),
  cited("أَنَا", "ana", "pron", ["mubtada-khabar", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — قُدِّمَ فَتَوَسَّطَ الْقَسَمُ.", "«I».", "«ben»."),
  WALLAHI(),
  cited("إِنْ", "in-shartiyya", "part", ["in-shartiyya", SH], "حَرْفُ شَرْطٍ جَازِمٌ — الْجُمْلَةُ الشَّرْطِيَّةُ خَبَرُ أَنَا.", "«if».", "«-sen»."),
  cited("تَأْتِنِي", "ata", "verb", [SH, "fail", "maful-bihi", "naqis-verbs"], "فِعْلُ الشَّرْطِ مَجْزُومٌ بِحَذْفِ الْيَاءِ، وَالْيَاءُ الْأَخِيرَةُ مَفْعُولٌ بِهِ.", "«you come to me».", "«bana gelirsen».", segments=[seg("تَأْتِ", "ata", "verb"), pr1s()]),
  cited("آتِكَ", "ata", "verb", [SH, "fail", "maful-bihi", "naqis-verbs"], "جَوَابُ الشَّرْطِ مَجْزُومٌ بِحَذْفِ الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ — اعْتُبِرَ الشَّرْطُ.", "«I come to you».", "«ben de sana gelirim».", punct="—", segments=[seg("آتِ", "ata", "verb"), pr2ms()]),
  W("تَوَسَّطَ", "tawassata", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ.", "«falls in the middle».", "«ortaya düşmüş»."),
  QASAM("الْقَسَمُ", ["fail"], "فَاعِلٌ مَرْفُوعٌ."),
  bi_("بِتَقْدِيمِ", "taqdim", "noun", ["idafa-definiteness"], "تَقْدِيمِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by the fronting of».", "«... öne alınmasıyla».", "تَقْدِيمِ"),
  cited("أَنَا", "ana", "pron", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«anā».", "«ene».", punct="،"),
  UTUBIRA(),
  SHART("الشَّرْطُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ."),
  ULGHIYA(),
  QASAM("الْقَسَمُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ."),
  bi_("بِسُقُوطِ", "suqut", "noun", ["idafa-definiteness"], "سُقُوطِ مَجْرُورٌ، وَهُوَ مُضَافٌ — الْبَاءُ لِلسَّبَبِيَّةِ: الدَّلِيلُ.", "«by the dropping of».", "«... düşmesiyle».", "سُقُوطِ"),
  W("الْيَاءِ", "ya-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the yāʾ».", "«yâ'nın»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-dan»."),
  W("الْجَزَاءِ", "jaza-answer", "noun", ["huruf-jarr", SH], "مَجْرُورٌ.", "«the answer».", "«cezadan».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And in إِنْ أَتَيْتَنِي وَاللهِ لَآتِيَنَّكَ the oath falls in the middle by the fronting of the condition, and the oath is regarded and the condition cancelled — by the condition's being past and the coming of the lām in the answer." + C_EN,
 "tr": "إِنْ أَتَيْتَنِي وَاللهِ لَآتِيَنَّكَ sözünde ise şartın öne alınmasıyla kasem ortaya düşmüş, kaseme itibar edilip şart lağvedilmiştir — şartın mâzî olması ve cevapta lâm'ın gelmesiyle." + C_TR},
 "tokens": [
  cited_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", SH, K], "إِنْ حَرْفُ شَرْطٍ — قُدِّمَ الشَّرْطُ.", "«and if».", "«ve ... -sen».", "إِنْ"),
  cited("أَتَيْتَنِي", "ata", "verb", [SH, "fail", "maful-bihi", "naqis-verbs"], "فِعْلُ الشَّرْطِ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«you come to me».", "«bana gelirsen».", segments=[seg("أَتَيْ", "ata", "verb"), prTa(), pr1s()]),
  WALLAHI(),
  cited("لَآتِيَنَّكَ", "ata", "verb", [QS, "nun-tawkid", "fail", "maful-bihi", "naqis-verbs"], "اللَّامُ لِجَوَابِ الْقَسَمِ، وَآتِيَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ، وَالْكَافُ مَفْعُولٌ بِهِ — اعْتُبِرَ الْقَسَمُ.", "«I will surely come to you».", "«elbette sana gelirim».", punct="—", segments=[seg("لَ", "lam-qasam", "part"), seg("آتِيَ", "ata", "verb"), seg("نَّ", "nun-tawkid-seg", "part"), pr2ms()]),
  W("تَوَسَّطَ", "tawassata", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ.", "«falls in the middle».", "«ortaya düşmüş»."),
  QASAM("الْقَسَمُ", ["fail"], "فَاعِلٌ مَرْفُوعٌ."),
  bi_("بِتَقْدِيمِ", "taqdim", "noun", ["idafa-definiteness"], "تَقْدِيمِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by the fronting of».", "«... öne alınmasıyla».", "تَقْدِيمِ"),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«şartın».", punct="،"),
  UTUBIRA(),
  QASAM("الْقَسَمُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ."),
  ULGHIYA(),
  SHART("الشَّرْطُ", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ."),
  BIKAWN(),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«şartın»."),
  MADIYAN(),
  WAMAJI(),
  W("اللَّامِ", "lam-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the lām».", "«lâm'ın»."),
  *FIL_JAWAB(punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And an implied oath is like a stated one — as «لَئِنْ أُخْرِجُوا لَا يَخْرُجُونَ»: the oath is implied at its head and regarded, by the condition's being past and the coming of the negation letter in the answer; had the condition been regarded, the nūn would have dropped from يَخْرُجُونَ for the jazm." + C_EN,
 "tr": "Takdirî kasem zikredilmiş gibidir — «لَئِنْ أُخْرِجُوا لَا يَخْرُجُونَ» gibi: başında kasem takdir edilmiş ve şartın mâzî olması ve cevapta nefy harfinin gelmesiyle ona itibar edilmiştir; şarta itibar edilseydi cezm alâmeti olarak يَخْرُجُونَ'den nûn düşerdi." + C_TR},
 "tokens": [
  atf_wa("وَالْقَسَمُ", "qasam", "noun", ["mubtada-khabar", QS], "الْقَسَمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the oath».", "«ve kasem».", "الْقَسَمُ"),
  W("الْمُقَدَّرُ", "muqaddar", "noun", ["naat-sifa", "ism-maful", "hadhf-wa-taqdir"], "صِفَةٌ مَرْفُوعَةٌ.", "«implied».", "«takdirî»."),
  ka_("كَالْمَذْكُورِ", "madhkur", "noun", ["mubtada-khabar"], "الْمَذْكُورِ مَجْرُورٌ — خَبَرٌ.", "«is like the stated».", "«zikredilmiş gibidir».", "الْمَذْكُورِ", punct="،", segs=[seg("كَ", "ka", "prep"), seg("الْمَذْكُورِ", "madhkur", "noun")]),
  nahwu(),
  cited("لَئِنْ", "in-shartiyya", "part", ["in-shartiyya", SH, QS, K], "اللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ الْمُقَدَّرِ، وَإِنْ حَرْفُ شَرْطٍ.", "«if indeed».", "«andolsun, eğer»."),
  cited("أُخْرِجُوا", "kharaja", "verb", [SH, "naib-al-fail", "form-iv-verbs"], "فِعْلُ الشَّرْطِ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ.", "«they are expelled».", "«çıkarılırlarsa».", segments=[seg("أُخْرِجُ", "kharaja", "verb"), seg("وا", "pron-3mp", "pron")]),
  cited("لَا", "la-nafiya", "part", ["la-nafiya", QS], "نَافِيَةٌ — جَوَابُ الْقَسَمِ الْمُقَدَّرِ.", "«not».", "«-maz-»."),
  cited("يَخْرُجُونَ", "kharaja", "verb", ["fail", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — لَمْ يُجْزَمْ، فَالْجَوَابُ لِلْقَسَمِ.", "«will they go out».", "«çıkmazlar».", punct="—", segments=[seg("يَخْرُجُ", "kharaja", "verb"), seg("ونَ", "pron-3mp", "pron")]),
  *QUDDIRA(),
  UTUBIRA("وَاعْتُبِرَ", [seg("وَ", "waw-atf", "conj"), seg("اعْتُبِرَ", "itabara", "verb")], "الْوَاوُ عَاطِفَةٌ، وَاعْتُبِرَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and regarded».", "«ve ona itibar edilmiştir»."),
  BIKAWN(),
  SHART("الشَّرْطِ", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", tr="«şartın»."),
  MADIYAN(),
  WAMAJI(),
  W("حَرْفِ", "harf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the letter of».", "«harfinin»."),
  W("النَّفْيِ", "nafy", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«negation».", "«nefy»."),
  *FIL_JAWAB(punct="؛"),
  *LAW_UTUBIRA(),
  W("لَسَقَطَتِ", "saqata", "verb", ["fail", SH], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَسَقَطَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«would have dropped».", "«düşerdi».", segments=[seg("لَ", "lam-qasam", "part"), seg("سَقَطَ", "saqata", "verb"), seg("تِ", "ta-tanith", "part")]),
  W("النُّونُ", "nun-letter", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the nūn».", "«nûn»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("يَخْرُجُونَ", "kharaja", "verb", ["huruf-jarr"], "فِي مَحَلِّ جَرٍّ — اللَّفْظُ مَحْكِيٌّ.", "«yakhrujūna».", "«yahrucûne»."),
  li_("لِلْجَزْمِ", "jazm", "noun", ["lam-taleel"], "الْجَزْمِ مَجْرُورٌ — اللَّامُ لِلتَّعْلِيلِ.", "«for the jazm».", "«cezm için».", "الْجَزْمِ", punct=".", segs=[seg("لِ", "lam-taleel", "part"), seg("لْجَزْمِ", "jazm", "noun")]),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And as «وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ»: the oath is implied at its head and regarded, by the coming of إِنَّ in the answer; had the condition been regarded, the fāʾ would have come — فَإِنَّكُمْ لَمُشْرِكُونَ — because the answer is a nominal sentence." + C_EN,
 "tr": "«وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ» gibi: başında kasem takdir edilmiş ve cevapta إِنَّ'nin gelmesiyle ona itibar edilmiştir; şarta itibar edilseydi ceza isim cümlesi olduğu için فَإِنَّكُمْ لَمُشْرِكُونَ diye fâ gelirdi." + C_TR},
 "tokens": [
  atf_wa("وَنَحْوُ", "nahw", "noun", ["mubtada-khabar"], "نَحْوُ مُبْتَدَأٌ لِخَبَرٍ مَحْذُوفٍ.", "«and as».", "«ve ... gibi».", "نَحْوُ", punct=":"),
  cited_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", SH, QS, K], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ، وَالْقَسَمُ مُقَدَّرٌ قَبْلَهَا.", "«and if».", "«ve eğer».", "إِنْ"),
  cited("أَطَعْتُمُوهُمْ", "ataa", "verb", [SH, "fail", "maful-bihi", "form-iv-verbs", "hollow-verbs"], "فِعْلُ الشَّرْطِ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ — وَالْوَاوُ إِشْبَاعٌ.", "«you obey them».", "«onlara itaat ederseniz».", segments=[seg("أَطَعْ", "ataa", "verb"), seg("تُمُو", "pron-2mp", "pron"), pr3mp()]),
  cited("إِنَّكُمْ", "inna", "part", ["inna-wa-akhawatuha", "inna-am-anna", QS], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَكُمْ اسْمُهَا — الْجُمْلَةُ جَوَابُ الْقَسَمِ الْمُقَدَّرِ، بِلَا فَاءٍ.", "«you are surely».", "«siz elbette».", segments=[seg("إِنَّ", "inna", "part"), pr2mp()]),
  cited("لَمُشْرِكُونَ", "mushrik", "noun", ["inna-wa-akhawatuha", "jam-mudhakkar-salim"], "اللَّامُ الْمُزَحْلَقَةُ، وَمُشْرِكُونَ خَبَرُ إِنَّ مَرْفُوعٌ بِالْوَاوِ.", "«polytheists».", "«müşriklersiniz».", punct="—", segments=[seg("لَ", "lam-ibtida", "part"), seg("مُشْرِكُونَ", "mushrik", "noun")]),
  *QUDDIRA(),
  UTUBIRA("وَاعْتُبِرَ", [seg("وَ", "waw-atf", "conj"), seg("اعْتُبِرَ", "itabara", "verb")], "الْوَاوُ عَاطِفَةٌ، وَاعْتُبِرَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and regarded».", "«ve ona itibar edilmiştir»."),
  bi_("بِمَجِيءِ", "maji", "noun", ["idafa-definiteness"], "مَجِيءِ مَجْرُورٌ، وَهُوَ مُضَافٌ — الْبَاءُ لِلسَّبَبِيَّةِ.", "«by the coming of».", "«... gelmesiyle».", "مَجِيءِ"),
  cited("إِنَّ", "inna", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«inna».", "«inne»."),
  *FIL_JAWAB(punct="؛"),
  *LAW_UTUBIRA(),
  W("لَجَاءَتِ", "jaa", "verb", ["fail", "hollow-verbs", SH], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَجَاءَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«would have come».", "«gelirdi».", segments=[seg("لَ", "lam-qasam", "part"), seg("جَاءَ", "jaa", "verb"), seg("تِ", "ta-tanith", "part")]),
  W("الْفَاءُ", "fa-letter", "noun", ["fail", "al-fa-fi-jawab-al-shart"], "فَاعِلٌ مَرْفُوعٌ.", "«the fāʾ».", "«fâ».", punct=":"),
  cited("فَإِنَّكُمْ", "inna", "part", ["al-fa-fi-jawab-al-shart", "inna-wa-akhawatuha"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّ حَرْفُ تَوْكِيدٍ، وَكُمْ اسْمُهَا.", "«then you are surely».", "«o takdirde siz».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr2mp()]),
  cited("لَمُشْرِكُونَ", "mushrik", "noun", ["inna-wa-akhawatuha", "jam-mudhakkar-salim"], "اللَّامُ الْمُزَحْلَقَةُ، وَمُشْرِكُونَ خَبَرُ إِنَّ.", "«polytheists».", "«müşriklersiniz».", punct="،", segments=[seg("لَ", "lam-ibtida", "part"), seg("مُشْرِكُونَ", "mushrik", "noun")]),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الْجَزَاءَ", "jaza-answer", "noun", ["inna-wa-akhawatuha", SH], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the answer».", "«ceza»."),
  W("جُمْلَةٌ", "jumla", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is a sentence».", "«cümlesidir»."),
  W("اسْمِيَّةٌ", "ismiyya", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَرْفُوعَةٌ.", "«nominal».", "«isim».", punct="."),
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
 "itabara": need("itabara", "اِعْتَبَرَ", "ع ب ر", "verb", "to regard, to take into account (Form VIII)", "itibar etmek, hesaba katmak (iftiʿâl)", 4),
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
put_morph(mo, "itabara", _nfc(_sg.derived(_sg.B8, _sg.W8, "َ", "اِعْتَبَر", "عْتَبِر", "اِعْتَبِر", "اِعْتِبَار", "مُعْتَبِر", "مُعْتَبَر", "اُعْتُبِرَ", "يُعْتَبَرُ", "اِعْتَبَرَ الشَّيْءَ: نَظَرَ فِيهِ وَحَسَبَ حِسَابَهُ — بَابُ الِافْتِعَالِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "اِجْتِمَاعُ الْقَسَمِ وَالشَّرْطِ فِي الْكَافِيَةِ", "en": "The oath meeting the condition in the Kafiya: whichever comes first takes the answer, a middle oath may be regarded or cancelled, and an implied oath counts like a stated one", "tr": "Kâfiye'de kasem ile şartın buluşması: önce gelen cevabı alır, ortadaki kaseme itibar da edilebilir lağv da, takdirî kasem zikredilmiş gibidir"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — إذا تقدم القسم على الشرط لزم كون الشرط ماضيا والجواب للقسم؛ إذا توسط جاز الأمران", "ضياء صونغور اوغلى — دفتر الكافية: والله إن أتيتني لأكرمتك؛ أنا والله إن تأتني آتك؛ إن أتيتني والله لآتينك؛ لئن أخرجوا لا يخرجون؛ وإن أطعتموهم إنكم لمشركون"],
 "question": {
  "en": ["Two governors want the same answer — who gets it? The one that came FIRST. With the oath at the head (وَاللهِ إِنْ أَتَيْتَنِي لَأَكْرَمْتُكَ) the answer wears the oath's lām and the condition's verb must be past; the condition's own answer is dropped, shown by the oath's.",
         "What does «past in wording or in sense» mean? أَتَيْتَنِي is a past verb; لَمْ تَأْتِنِي is a present verb turned to the past by لَمْ. Both satisfy the rule, and the analyzer reads لَمْ as a converter of time for exactly this reason.",
         "How do you tell which one was regarded when the oath sits in the middle? Read the ANSWER. آتِكَ with its yāʾ dropped is majzūm, so the condition won (أَنَا وَاللهِ إِنْ تَأْتِنِي آتِكَ); لَآتِيَنَّكَ with the lām and the nūn of emphasis is an oath's answer, so the oath won (إِنْ أَتَيْتَنِي وَاللهِ لَآتِيَنَّكَ). The sign engine reads the first off the ending; the hadhf engine's implied-oath rule reads the second off the lām and the nūn.",
         "Why does 59:12 read لَا يَخْرُجُونَ with the nūn kept? Because an oath is implied before لَئِنْ (its lām is the lām that prepares for an oath) and the oath took the answer; had the condition taken it, the five-verb form would have lost its nūn for jazm. A kept nūn after a condition is the fingerprint of an implied oath, and the hadhf engine raises the oath's seat on لَئِنْ from it.",
         "Why does 6:121 read إِنَّكُمْ without a fāʾ? A nominal answer to a CONDITION needs the fāʾ (فَإِنَّكُمْ); an answer to an OATH does not. The missing fāʾ is the second fingerprint of an implied oath, and the hadhf engine's implied-oath rule treats both fingerprints as evidence."],
  "tr": ["İki âmil aynı cevabı ister — kim alır? ÖNCE gelen. Kasem başta olunca (وَاللهِ إِنْ أَتَيْتَنِي لَأَكْرَمْتُكَ) cevap kasemin lâm'ını giyer ve şartın fiili mâzî olmalıdır; şartın kendi cevabı hazfedilir, kaseminki ona delâlet eder.",
         "«Lafzen ya da mânen mâzî» ne demek? أَتَيْتَنِي mâzî bir fiildir; لَمْ تَأْتِنِي, لَمْ ile geçmişe çevrilmiş bir muzâridir. İkisi de kuralı karşılar ve analizör tam bu sebeple لَمْ'i zaman çeviricisi olarak okur.",
         "Kasem ortada otururken hangisine itibar edildiğini nasıl anlarsın? CEVABI oku. Yâ'sı düşmüş آتِكَ meczumdur, demek şart kazanmıştır (أَنَا وَاللهِ إِنْ تَأْتِنِي آتِكَ); lâm'ı ve te'kid nûnuyla لَآتِيَنَّكَ bir kasem cevabıdır, demek kasem kazanmıştır (إِنْ أَتَيْتَنِي وَاللهِ لَآتِيَنَّكَ). Alâmet motoru birincisini sondan, hazif motorunun takdirî-kasem kuralı ikincisini lâm ve nûndan okur.",
         "59:12 niçin nûnu korunmuş لَا يَخْرُجُونَ okunur? Çünkü لَئِنْ'den önce bir kasem takdir edilir (lâm'ı kaseme hazırlayan lâm'dır) ve cevabı kasem almıştır; şart alsaydı beş fiil şekli cezm için nûnunu kaybederdi. Şarttan sonra korunan nûn takdirî kasemin parmak izidir ve hazif motoru لَئِنْ üzerinde kasemin yerini ondan çıkarır.",
         "6:121 niçin fâ'sız إِنَّكُمْ okunur? ŞARTA isim cümlesi cevap fâ ister (فَإِنَّكُمْ); KASEME cevap istemez. Eksik fâ takdirî kasemin ikinci parmak izidir ve hazif motorunun takdirî-kasem kuralı iki izi de delil sayar."]},
 "plain": {
  "en": "When «by God» and «if» are in the same sentence, only one of them gets the answer clause. Whichever came first wins. If the oath comes first, the answer carries its lām and the if-verb goes to the past. If the oath sits in the middle, the ending of the answer tells you who won.",
  "tr": "«Vallahi» ile «eğer» aynı cümledeyse cevap cümlesini yalnız biri alır. Önce gelen kazanır. Kasem öndeyse cevap onun lâm'ını taşır ve şart fiili geçmişe gider. Kasem ortadaysa cevabın sonu kimin kazandığını söyler."},
 "explanation": {
  "en": "The Kafiya's rule for an oath and a condition in one sentence, in the notebook's expanded form with its five worked examples. The rule has two halves: precedence (the earlier of the two takes the answer; the later's answer is dropped and shown by it) and, for the middle oath, free choice — with the ANSWER's form as the evidence of which was chosen. The two Qur'anic examples (59:12, 6:121) extend the rule to an implied oath and give the two fingerprints by which the implied oath is detected: a five-verb form that keeps its nūn, and a nominal answer with no fāʾ. Both fingerprints are things the engines already read off the surface — the ending and the connector — so the chapter is also a specification for the analyzer's treatment of لَئِنْ.",
  "tr": "Kâfiye'nin bir cümledeki kasem ve şart kuralı, defterin beş işlenmiş örnekli genişletilmiş hâliyle. Kuralın iki yarısı vardır: öncelik (ikisinden önce gelen cevabı alır; sonrakinin cevabı hazfedilir ve ona delâlet eder) ve ortadaki kasem için serbest tercih — hangisinin seçildiğinin delili olarak CEVABIN şekli. İki Kur'ân örneği (59:12, 6:121) kuralı takdirî kaseme uzatır ve takdirî kasemin tanındığı iki parmak izini verir: nûnunu koruyan beş fiil şekli ve fâ'sız isim cümlesi cevap. İki iz de motorların yüzeyden zaten okuduğu şeylerdir — son ek ve bağlayıcı — bu yüzden bâb aynı zamanda analizörün لَئِنْ muamelesinin bir şartnamesidir."},
 "examples": [
  {"ar": "وَاللهِ إِنْ أَتَيْتَنِي لَأَكْرَمْتُكَ", "en": "Oath first: the answer is the oath's.", "tr": "Kasem önde: cevap kasemin.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "أَنَا وَاللهِ إِنْ تَأْتِنِي آتِكَ", "en": "Middle oath, condition regarded: the yāʾ drops.", "tr": "Ortada kasem, şarta itibar: yâ düşer.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "إِنْ أَتَيْتَنِي وَاللهِ لَآتِيَنَّكَ", "en": "Middle oath, oath regarded: the lām and the nūn.", "tr": "Ortada kasem, kaseme itibar: lâm ve nûn.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "لَئِنْ أُخْرِجُوا لَا يَخْرُجُونَ", "en": "Implied oath: the nūn kept.", "tr": "Takdirî kasem: nûn korunur.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "وَإِنْ أَطَعْتُمُوهُمْ إِنَّكُمْ لَمُشْرِكُونَ", "en": "Implied oath: no fāʾ before inna.", "tr": "Takdirî kasem: inne'den önce fâ yok.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«وَاللهِ إِنْ تَأْتِنِي آتِكَ»",
   "right": "«وَاللهِ إِنْ أَتَيْتَنِي لَآتِيَنَّكَ — kasem başta olunca şart mâzî, cevap kasemin»",
   "why": {"en": "An oath at the head takes the answer and makes the condition past.", "tr": "Baştaki kasem cevabı alır ve şartı mâzî kılar."}},
  {"wrong": "«لَئِنْ أُخْرِجُوا لَا يَخْرُجُوا»",
   "right": "«لَا يَخْرُجُونَ — cevap takdirî kasemindir, cezm yoktur»",
   "why": {"en": "The nūn is kept because the oath, not the condition, owns the answer.", "tr": "Nûn korunur, çünkü cevap şartın değil kasemindir."}},
  {"wrong": "«وَإِنْ أَطَعْتُمُوهُمْ فَإِنَّكُمْ لَمُشْرِكُونَ (âyet böyle)»",
   "right": "«إِنَّكُمْ لَمُشْرِكُونَ — fâ'sız; cevap kasemin»",
   "why": {"en": "A nominal answer to a condition would need the fāʾ; its absence marks the oath's answer.", "tr": "Şarta isim cümlesi cevap fâ isterdi; yokluğu kasem cevabını gösterir."}}],
 "relatedNotes": ["huruf-al-qasam-fil-kafiya", "huruf-al-shart-fil-kafiya", "al-majzum-wal-shart-wal-jaza", "al-fa-fi-jawab-al-shart", "nun-tawkid"]}

ADD_EN = (" Chapter 42 (notebook line ~347): the oath meeting the condition — precedence, the middle oath regarded or cancelled with the answer as evidence, the implied oath (59:12, 6:121) — the notebook's exposition, kept as commentary (s1-s7).")
ADD_TR = (" Kırk ikinci bâb (defter satırı ~347): kasem ile şartın buluşması — öncelik, cevabı delil sayarak ortadaki kaseme itibar ya da lağv, takdirî kasem (59:12, 6:121) — defterin açıklaması, şerh olarak (s1-s7).")
write_out(42, S, TITLE, ADD_EN, ADD_TR, "347", GLOSS_ADD, notes=(NOTE,),
          related=(("huruf-al-qasam-fil-kafiya", [K]), ("al-fa-fi-jawab-al-shart", [K])))
report(42, S, GLOSS_ADD, (NOTE,))
