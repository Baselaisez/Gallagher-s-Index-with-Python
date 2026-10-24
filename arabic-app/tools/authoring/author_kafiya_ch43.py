# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 43: أَمَّا — for detailing what was said in sum (جَاءَتْنِي إِخْوَتُكَ: أَمَّا زَيْدٌ فَأَكْرَمْتُهُ…), sometimes for a
fresh start (أَمَّا بَعْدُ); its verb is dropped; what is placed between أَمَّا and the fāʾ — Sībawayh: a part of the clause after the
fāʾ, whether or not fronting would be allowed; al-Mubarrad: the governed word of the dropped verb, absolutely; al-Māzinī: the
first when the fāʾ is the only obstacle, the second when another obstacle stands — and the difference between the three stated.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~347-348 of the transcription.

  COMMENTARY (the notebook): s1-s6 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch43.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "amma-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "أَمَّا: التَّفْصِيلُ وَفِعْلُهَا الْمَحْذُوفُ وَمَا بَيْنَهَا وَبَيْنَ الْفَاءِ", "en": "Ammā — detailing, its dropped verb, and what stands between it and the fāʾ (Sībawayh, al-Mubarrad, al-Māzinī)", "tr": "Emmâ — tafsil, hazfedilen fiili ve onunla fâ arasında duran (Sîbeveyh, Müberred, Mâzinî)"}
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
AM = "amma-tafsiliyya"
FJ = "al-fa-fi-jawab-al-shart"
def AMMA(full="أَمَّا", wa=False, punct=None, ar="حَرْفُ شَرْطٍ وَتَفْصِيلٍ — فِعْلُهَا مَحْذُوفٌ: مَهْمَا يَكُنْ مِنْ شَيْءٍ."):
    if wa: return cited_wa("وَأَمَّا", "amma-tafsil", "part", [AM, K], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا " + ar, "«and as for».", "«... -e gelince».", "أَمَّا", punct=punct)
    return cited(full, "amma-tafsil", "part", [AM, K], ar, "«as for».", "«-e gelince».", punct=punct)
def FA_V(full, lex, stem, ar_v, en, tr, obj=None, punct=None, tags=()):
    segs = [seg("فَ", "fa", "conj"), seg(stem, lex, "verb"), prT()] + ([obj] if obj else [])
    return cited(full, lex, "verb", [FJ, AM, "fail", "maful-bihi"] + list(tags), "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَ" + ar_v, en, tr, punct=punct, segments=segs)
def INDA(who, lex, en, tr, wa=True, punct=None, extra=()):
    if wa: return [atf_wa("وَعِنْدَ", "inda", "noun", [AT, "maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and according to».", "«... -e göre».", "عِنْدَ"), W(who, lex, "propn", ["idafa-definiteness"] + list(extra), "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", en, tr, punct=punct)]
    return [W("فَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَعِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«according to».", "«... -e göre».", segments=[seg("فَ", "fa", "conj"), seg("عِنْدَ", "inda", "noun")]), W(who, lex, "propn", ["idafa-definiteness"] + list(extra), "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", en, tr, punct=punct)]
def FAA(full="الْفَاءِ", tags=("idafa-definiteness",), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ.", punct=None): return W(full, "fa-letter", "noun", list(tags) + [FJ], ar, "«the fāʾ».", "«fâ».", punct=punct)
def BIJUZ(verb_full, verb_ar, en_v, tr_v, segs=None):
    return [W(verb_full, "ata", "verb", ["naib-al-fail", "naqis-verbs"], verb_ar, en_v, tr_v, segments=segs),
            bi_("بِجُزْءٍ", "juz", "noun", ["naib-al-fail"], "جُزْءٍ مَجْرُورٌ لَفْظًا — فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«a part».", "«bir cüz».", "جُزْءٍ")]
def MAMUL(punct=None): return [bi_("بِمَعْمُولِ", "mamul", "noun", ["naib-al-fail", "idafa-definiteness", "al-mamul-wa-aqsamuh"], "مَعْمُولِ مَجْرُورٌ لَفْظًا مُضَافٌ — فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«the governed word of».", "«... ma'mûlü».", "مَعْمُولِ"), W("الْفِعْلِ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the verb».", "«fiilin»."), W("الْمَحْذُوفِ", "mahdhuf", "noun", ["naat-sifa", "ism-maful", "hadhf-wa-taqdir"], "صِفَةٌ مَجْرُورَةٌ.", "«dropped».", "«hazfedilen».", punct=punct)]

S.append({"id": "s1", "translation": {
 "en": "And أَمَّا is for detailing — as جَاءَتْنِي إِخْوَتُكَ: أَمَّا زَيْدٌ فَأَكْرَمْتُهُ، وَأَمَّا عَمْرٌو فَأَهَنْتُهُ، وَأَمَّا بِشْرٌ فَأَعْرَضْتُ عَنْهُ, «your brothers came to me: as for Zayd, I honoured him; as for ʿAmr, I slighted him; as for Bishr, I turned away from him»." + C_EN,
 "tr": "أَمَّا tafsil içindir — جَاءَتْنِي إِخْوَتُكَ: أَمَّا زَيْدٌ فَأَكْرَمْتُهُ، وَأَمَّا عَمْرٌو فَأَهَنْتُهُ، وَأَمَّا بِشْرٌ فَأَعْرَضْتُ عَنْهُ gibi: «kardeşlerin bana geldi: Zeyd'e gelince ona ikram ettim; Amr'a gelince ona ihanet ettim; Bişr'e gelince ondan yüz çevirdim»." + C_TR},
 "tokens": [
  cited_wa("وَأَمَّا", "amma-tafsil", "part", ["mubtada-khabar", K, AM], "أَمَّا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and ammā».", "«emmâ».", "أَمَّا"),
  li_("لِلتَّفْصِيلِ", "tafsil", "noun", ["mubtada-khabar", "form-ii-verbs"], "التَّفْصِيلِ مَجْرُورٌ — خَبَرٌ.", "«is for detailing».", "«tafsil içindir».", "التَّفْصِيلِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لتَّفْصِيلِ", "tafsil", "noun")]),
  nahwu(),
  cited("جَاءَتْنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs", "al-fail-al-muzhar-wa-tanith-amilih"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — لِأَنَّ الْفَاعِلَ جَمْعُ تَكْسِيرٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), seg("تْ", "ta-tanith", "part"), pr1s()]),
  cited("إِخْوَتُكَ", "akh", "noun", ["fail", "idafa-definiteness", "jam-taksir"], "فَاعِلٌ مَرْفُوعٌ — جَمْعُ أَخٍ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your brothers».", "«kardeşlerin».", punct=":", segments=[seg("إِخْوَتُ", "akh", "noun"), pr2ms()]),
  AMMA(),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar", AM], "مُبْتَدَأٌ مَرْفُوعٌ — الْمُفَصَّلُ الْأَوَّلُ.", "«Zayd».", "«Zeyd»."),
  FA_V("فَأَكْرَمْتُهُ", "akrama", "أَكْرَمْ", "أَكْرَمْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرٌ.", "«I honoured him».", "«ona ikram ettim».", obj=pr3ms(), punct="،", tags=("form-iv-verbs",)),
  AMMA(wa=True),
  cited("عَمْرٌو", "amr-name", "propn", ["mubtada-khabar", AM], "مُبْتَدَأٌ مَرْفُوعٌ.", "«ʿAmr».", "«Amr»."),
  FA_V("فَأَهَنْتُهُ", "ahana", "أَهَنْ", "أَهَنْتُ فِعْلٌ مَاضٍ أَجْوَفُ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«I slighted him».", "«ona ihanet ettim».", obj=pr3ms(), punct="،", tags=("form-iv-verbs", "hollow-verbs")),
  AMMA(wa=True),
  cited("بِشْرٌ", "bishr", "propn", ["mubtada-khabar", AM], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Bishr».", "«Bişr»."),
  FA_V("فَأَعْرَضْتُ", "aarada", "أَعْرَضْ", "أَعْرَضْتُ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I turned away».", "«yüz çevirdim».", tags=("form-iv-verbs",)),
  cited("عَنْهُ", "an-jarr", "prep", ["huruf-jarr"], "عَنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«from him».", "«ondan».", punct=".", segments=[seg("عَنْ", "an-jarr", "prep"), pr3ms()]),
 ]})

S.append({"id": "s2", "translation": {
 "en": "The speaker detailed with أَمَّا what he had said in sum — «your brothers came to me»." + C_EN,
 "tr": "Mütekellim, mücmel olarak söylediği «kardeşlerin bana geldi» sözünü أَمَّا ile tafsil etmiştir." + C_TR},
 "tokens": [
  W("فَصَّلَ", "fassala", "verb", ["fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ.", "«detailed».", "«tafsil etmiştir»."),
  W("الْمُتَكَلِّمُ", "mutakallim", "noun", ["fail", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the speaker».", "«mütekellim»."),
  bi_("بِأَمَّا", "amma-tafsil", "part", [AM], "أَمَّا فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«with ammā».", "«emmâ ile».", "أَمَّا"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«what».", "«... sözünü»."),
  W("قَالَهُ", "qala", "verb", ["ism-mawsul", "fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةٌ.", "«he had said».", "«söylediği».", segments=[seg("قَالَ", "qala", "verb"), pr3ms()]),
  W("مُجْمَلًا", "mujmal", "noun", ["hal", "ism-maful", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ.", "«in sum».", "«mücmel olarak».", punct=":"),
  cited("جَاءَتْنِي", "jaa", "verb", ["fail", "maful-bihi", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْيَاءُ مَفْعُولٌ بِهِ — الْجُمْلَةُ بَدَلٌ مِنْ مَا.", "«came to me».", "«bana geldi».", segments=[seg("جَاءَ", "jaa", "verb"), seg("تْ", "ta-tanith", "part"), pr1s()]),
  cited("إِخْوَتُكَ", "akh", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your brothers».", "«kardeşlerin».", punct=".", segments=[seg("إِخْوَتُ", "akh", "noun"), pr2ms()]),
 ]})

S.append({"id": "s3", "translation": {
 "en": "And أَمَّا may be for a fresh start — as their saying at the beginnings of books: أَمَّا بَعْدُ." + C_EN,
 "tr": "أَمَّا bazen istînaf için olur — kitapların başlarındaki أَمَّا بَعْدُ sözleri gibi." + C_TR},
 "tokens": [
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and may».", "«ve bazen».", "قَدْ"),
  W("تَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«be».", "«olur»."),
  cited("أَمَّا", "amma-tafsil", "part", ["kana-wa-akhawatuha", AM], "اسْمُ تَكُونُ — اللَّفْظُ مَحْكِيٌّ.", "«ammā».", "«emmâ»."),
  li_("لِلِاسْتِئْنَافِ", "istinaf", "noun", ["kana-wa-akhawatuha", "form-x-verbs"], "الِاسْتِئْنَافِ مَجْرُورٌ — خَبَرُ تَكُونُ.", "«for a fresh start».", "«istînaf için».", "الِاسْتِئْنَافِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِئْنَافِ", "istinaf", "noun")]),
  ka_("كَقَوْلِهِمْ", "qawl", "noun", ["idafa-definiteness"], "قَوْلِ مَجْرُورٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«as their saying».", "«... sözleri gibi».", "قَوْلِ", segs=[seg("كَ", "ka", "prep"), seg("قَوْلِ", "qawl", "noun"), pr3mp()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«at».", "«-daki»."),
  W("أَوَائِلِ", "awwal", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ — جَمْعُ أَوَّل، وَهُوَ مُضَافٌ.", "«the beginnings of».", "«başlarındaki»."),
  W("الْكُتُبِ", "kitab", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«books».", "«kitapların».", punct=":"),
  AMMA(ar="حَرْفُ اسْتِئْنَافٍ وَتَفْصِيلٍ."),
  cited("بَعْدُ", "bada", "noun", ["maful-fih", "al-murab-wal-mabni-wal-irab", K], "ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ — وَالْجَوَابُ بَعْدَهُ بِالْفَاءِ.", "«afterwards».", "«bundan sonra».", punct="."),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And the verb of أَمَّا is dropped. According to Sībawayh, a part of the clause that follows the fāʾ is placed between أَمَّا and the fāʾ — whether its fronting would be allowed or not; and according to al-Mubarrad, the governed word of the dropped verb is placed there, absolutely." + C_EN,
 "tr": "أَمَّا'nın fiili hazfedilir. Sîbeveyh'e göre, öne alınması câiz olsun olmasın, أَمَّا ile fâ arasına fâ'dan sonraki kelâmın bir cüz'ü getirilir; Müberred'e göre ise mutlak olarak hazfedilen fiilin ma'mûlü getirilir." + C_TR},
 "tokens": [
  atf_wa("وَفِعْلُ", "fil", "noun", ["mubtada-khabar", "idafa-definiteness"], "فِعْلُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the verb of».", "«ve ... fiili».", "فِعْلُ"),
  cited("أَمَّا", "amma-tafsil", "part", ["idafa-definiteness", AM], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«ammā».", "«emmâ'nın»."),
  W("مَحْذُوفٌ", "mahdhuf", "noun", ["mubtada-khabar", "ism-maful", "hadhf-wa-taqdir"], "خَبَرٌ مَرْفُوعٌ.", "«is dropped».", "«hazfedilir».", punct="."),
  *INDA("سِيبَوَيْهِ", "sibawayh", "«Sībawayh».", "«Sîbeveyh'e».", wa=False, extra=("al-mabni-wal-mudmar",)),
  *BIJUZ("يُؤْتَى", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — الْجُمْلَةُ مُبْتَدَأٌ مُؤَخَّرٌ فِي الْمَعْنَى.", "«is placed».", "«getirilir»."),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«... arasına»."),
  cited("أَمَّا", "amma-tafsil", "part", ["idafa-definiteness", AM], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«ammā».", "«emmâ»."),
  atf_wa("وَالْفَاءِ", "fa-letter", "noun", [AT, FJ], "الْفَاءِ مَعْطُوفٌ مَجْرُورٌ.", "«and the fāʾ».", "«ile fâ».", "الْفَاءِ"),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-ın»."),
  W("الْكَلَامِ", "kalam", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the clause».", "«kelâmın»."),
  W("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa", "asma-al-ishara-wal-mawsulat"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ صِفَةٌ.", "«that».", "«... olan»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةٌ.", "«follows».", "«-dan sonraki»."),
  FAA(punct="،"),
  W("جَازَ", "jaaza", "verb", ["fail", "hollow-verbs", "hal"], "فِعْلٌ مَاضٍ — الْجُمْلَةُ حَالٌ.", "«whether be allowed».", "«câiz olsun»."),
  W("تَقْدِيمُهُ", "taqdim", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its fronting».", "«öne alınması».", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3ms()]),
  W("أَوْ", "aw", "conj", [AT], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَجُزْ", "jaaza", "verb", ["nawasib-wa-jawazim-al-mudari", "fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«be allowed».", "«olmasın».", punct="؛"),
  *INDA("الْمُبَرِّدِ", "mubarrad", "«al-Mubarrad».", "«Müberred'e»."),
  *BIJUZ("يُؤْتَى", "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is placed».", "«getirilir».")[:1],
  *MAMUL(),
  W("مُطْلَقًا", "mutlaq", "noun", ["hal", "ism-maful"], "حَالٌ مَنْصُوبٌ.", "«absolutely».", "«mutlak olarak».", punct="."),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And according to al-Māzinī: if there is no obstacle other than the fāʾ, a part of what follows the fāʾ is placed there, as Sībawayh said; and if there is another obstacle, the governed word of the dropped verb is placed there, as al-Mubarrad said." + C_EN,
 "tr": "Mâzinî'ye göre: fâ'dan başka bir mâni yoksa Sîbeveyh'in dediği gibi fâ'dan sonrakinin bir cüz'ü getirilir; başka bir mâni daha varsa Müberred'in dediği gibi hazfedilen fiilin ma'mûlü getirilir." + C_TR},
 "tokens": [
  *INDA("الْمَازِنِيِّ", "mazini", "«al-Māzinī».", "«Mâzinî'ye».", punct=":"),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«... -sa»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«yok-»."),
  W("يَكُنْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ تَامٌّ مَجْزُومٌ — فِعْلُ الشَّرْطِ.", "«there is».", "«-sa»."),
  W("مَانِعٌ", "mani-preventer", "noun", ["fail", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ.", "«an obstacle».", "«bir mâni»."),
  W("غَيْرُ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ مَرْفُوعَةٌ، وَهُوَ مُضَافٌ.", "«other than».", "«-dan başka»."),
  FAA(punct=None),
  W("أُتِيَ", "ata", "verb", ["naib-al-fail", "naqis-verbs", FJ], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ.", "«is placed».", "«getirilir»."),
  bi_("بِجُزْءٍ", "juz", "noun", ["naib-al-fail"], "جُزْءٍ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«a part».", "«bir cüz».", "جُزْءٍ"),
  W("مِمَّا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "مِنْ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«of what».", "«-nin».", segments=[seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةٌ.", "«follows».", "«-dan sonraki»."),
  FAA(),
  ka_("كَمَا", "ma-masdariyya", "part", ["anwa-ma"], "مَا مَصْدَرِيَّةٌ.", "«as».", "«... gibi».", "مَا", segs=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  W("قَالَ", "qala", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«said».", "«dediği»."),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["fail", "al-mabni-wal-mudmar"], "فَاعِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ.", "«Sībawayh».", "«Sîbeveyh'in».", punct="؛"),
  atf_wa("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "إِنْ حَرْفُ شَرْطٍ.", "«and if».", "«ve ... -sa».", "إِنْ"),
  W("كَانَ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ فِي مَحَلِّ جَزْمٍ.", "«there is».", "«varsa»."),
  W("مَانِعٌ", "mani-preventer", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«an obstacle».", "«bir mâni»."),
  W("آخَرُ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "صِفَةٌ مَرْفُوعَةٌ — غَيْرُ مُنْصَرِفٍ.", "«another».", "«başka»."),
  W("أُتِيَ", "ata", "verb", ["naib-al-fail", "naqis-verbs", FJ], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — جَوَابُ الشَّرْطِ.", "«is placed».", "«getirilir»."),
  *MAMUL(),
  ka_("كَمَا", "ma-masdariyya", "part", ["anwa-ma"], "مَا مَصْدَرِيَّةٌ.", "«as».", "«... gibi».", "مَا", segs=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  W("قَالَ", "qala", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«said».", "«dediği»."),
  W("الْمُبَرِّدُ", "mubarrad", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«al-Mubarrad».", "«Müberred'in».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And the difference between the three imams: Sībawayh made the permissibility of fronting what follows the fāʾ before it a peculiarity of أَمَّا; al-Mubarrad did not make it a peculiarity of أَمَّا; and al-Māzinī said: أَمَّا removes the obstacle that comes from the fāʾ and does not remove another obstacle." + C_EN,
 "tr": "Üç imamın görüşleri arasındaki fark: Sîbeveyh fâ'dan sonrakinin önüne alınmasının cevazını أَمَّا için bir hususiyet kıldı; Müberred bunu أَمَّا için hususiyet kılmadı; Mâzinî ise «أَمَّا fâ'dan gelen mâniyi kaldırır, başka bir mâniyi kaldıramaz» dedi." + C_TR},
 "tokens": [
  atf_wa("وَالْفَرْقُ", "farq", "noun", ["mubtada-khabar"], "الْفَرْقُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the difference».", "«ve fark».", "الْفَرْقُ"),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«... arasındaki»."),
  W("الْأَئِمَّةِ", "imam", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the imams».", "«imamların»."),
  W("الثَّلَاثَةِ", "thalatha", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«three».", "«üç».", punct=":"),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mubtada-khabar"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ خَبَرٌ.", "«that».", "«(şudur:)»."),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["inna-wa-akhawatuha", "al-mabni-wal-mudmar"], "اسْمُ أَنَّ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ.", "«Sībawayh».", "«Sîbeveyh»."),
  W("جَعَلَ", "jaala", "verb", ["inna-wa-akhawatuha", "fail", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ — الْجُمْلَةُ خَبَرُ أَنَّ؛ جَعَلَ بِمَعْنَى صَيَّرَ تَنْصِبُ مَفْعُولَيْنِ.", "«made».", "«kıldı»."),
  W("جَوَازَ", "jawaz", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the permissibility of».", "«cevazını»."),
  W("تَقْدِيمِ", "taqdim", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«fronting».", "«öne alınmasının»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what».", "«-nin»."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — صِلَةٌ.", "«follows».", "«-dan sonraki»."),
  FAA(),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«before».", "«-ın önüne»."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what».", "«-nin»."),
  W("قَبْلَهَا", "qabla", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةٌ.", "«precedes it».", "«ondan önceki».", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  W("خُصُوصِيَّةً", "khususiyya", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a peculiarity».", "«bir hususiyet»."),
  li_("لِأَمَّا", "amma-tafsil", "part", [AM], "أَمَّا فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«of ammā».", "«emmâ için».", "أَمَّا", punct="؛"),
  atf_wa("وَالْمُبَرِّدُ", "mubarrad", "propn", ["mubtada-khabar"], "الْمُبَرِّدُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and al-Mubarrad».", "«Müberred».", "الْمُبَرِّدُ"),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَجْعَلْهُ", "jaala", "verb", ["nawasib-wa-jawazim-al-mudari", "mubtada-khabar", "fail", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ — الْجُمْلَةُ خَبَرٌ.", "«did make it».", "«kıl-».", segments=[seg("يَجْعَلْ", "jaala", "verb"), pr3ms()]),
  W("خُصُوصِيَّةً", "khususiyya", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«a peculiarity».", "«hususiyet»."),
  W("لَهَا", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ.", "«of it».", "«onun için».", punct="؛", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  atf_wa("وَالْمَازِنِيُّ", "mazini", "propn", ["mubtada-khabar", "ism-mansub"], "الْمَازِنِيُّ مُبْتَدَأٌ مَرْفُوعٌ.", "«and al-Māzinī».", "«Mâzinî ise».", "الْمَازِنِيُّ"),
  W("قَالَ", "qala", "verb", ["mubtada-khabar", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ — الْجُمْلَةُ خَبَرٌ.", "«said».", "«dedi».", punct=":"),
  cited("أَمَّا", "amma-tafsil", "part", ["mubtada-khabar", AM, K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«ammā».", "«emmâ»."),
  W("تَرْفَعُ", "rafaa", "verb", ["mubtada-khabar", "fail"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْجُمْلَةُ خَبَرٌ.", "«removes».", "«kaldırır»."),
  W("الْمَانِعَ", "mani-preventer", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the obstacle».", "«mâniyi»."),
  W("الْآتِيَ", "ati-coming", "noun", ["naat-sifa", "ism-fail", "ism-maqsur-manqus"], "صِفَةٌ مَنْصُوبَةٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ.", "«that comes».", "«gelen»."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-dan»."),
  FAA("الْفَاءِ", tags=("huruf-jarr",), ar="مَجْرُورٌ."),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«... -maz».", "لَا"),
  W("تَرْفَعُ", "rafaa", "verb", ["fail"], "فِعْلٌ مُضَارِعٌ.", "«does remove».", "«kaldıramaz»."),
  W("مَانِعًا", "mani-preventer", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«an obstacle».", "«bir mâniyi»."),
  W("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"], "صِفَةٌ مَنْصُوبَةٌ.", "«another».", "«başka».", punct="."),
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
 "bishr": need("bishr", "بِشْر", "ب ش ر", "propn", "Bishr — a man's name used in the grammar books' examples", "Bişr — nahiv kitaplarının örneklerinde bir erkek adı", 3),
 "fassala": need("fassala", "فَصَّلَ", "ف ص ل", "verb", "to set out in detail, to itemise (Form II)", "tafsil etmek, ayrıntılamak (tefʿîl)", 3),
 "khususiyya": need("khususiyya", "خُصُوصِيَّة", "خ ص ص", "noun", "a peculiarity — a property belonging to one word alone", "hususiyet — yalnız bir kelimeye ait özellik", 4),
 "istinaf": need("istinaf", "اِسْتِئْنَاف", "أ ن ف", "noun", "a fresh start — beginning a new sentence not joined to the one before (masdar, Form X)", "istînaf — öncekine bağlanmayan yeni bir cümleye başlama (istifʿâl masdarı)", 4),
 "ati-coming": need("ati-coming", "آتٍ", "أ ت ي", "noun", "coming, that comes (ism fāʿil of أَتَى; manqūṣ)", "gelen, gelecek olan (etâ'nın ism-i fâili; mankûs)", 3),
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
put_morph(mo, "fassala", _nfc(_sg.derived(_sg.B2, _sg.W2, "ُ", "فَصَّل", "فَصِّل", "فَصِّل", "تَفْصِيل", "مُفَصِّل", "مُفَصَّل", "فُصِّلَ", "يُفَصَّلُ", "فَصَّلَ الْكَلَامَ: بَيَّنَهُ جُزْءًا جُزْءًا — بَابُ التَّفْعِيلِ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "أَمَّا فِي الْكَافِيَةِ: التَّفْصِيلُ وَالْفِعْلُ الْمَحْذُوفُ وَمَا بَيْنَهَا وَبَيْنَ الْفَاءِ", "en": "Ammā in the Kafiya: detailing a sum, the fresh-start ammā, the dropped verb, and the three imams on what may stand between ammā and its fāʾ", "tr": "Kâfiye'de emmâ: mücmeli tafsil, istînaf emmâ'sı, hazfedilen fiil ve emmâ ile fâ'sı arasında ne durabileceği üzerine üç imam"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — أما للتفصيل؛ فعلها محذوف؛ يؤتى بين أما والفاء بجزء مما بعد الفاء عند سيبويه وبمعمول الفعل المحذوف عند المبرد", "ضياء صونغور اوغلى — دفتر الكافية: جاءتني إخوتك أما زيد فأكرمته…؛ أما بعد للاستئناف؛ قول المازني والفرق بين الأئمة الثلاثة"],
 "question": {
  "en": ["What does أَمَّا do? It takes a sum already stated («your brothers came») and deals with its items one by one, each item fronted and each answer opened by a fāʾ: أَمَّا زَيْدٌ فَأَكْرَمْتُهُ. At the head of a book it opens a fresh start instead: أَمَّا بَعْدُ.",
         "Why is there a fāʾ after a plain noun? Because أَمَّا is a CONDITIONAL letter whose verb has been dropped — the books restore it as مَهْمَا يَكُنْ مِنْ شَيْءٍ — and the fāʾ is the fāʾ of the condition's answer. The iʿrāb lines here restore exactly this and label the fāʾ as the answer's connector, not as coordination.",
         "What stands between أَمَّا and the fāʾ? Something must, since the dropped verb left a gap: per Sībawayh a part of the clause that follows the fāʾ (زَيْدٌ in أَمَّا زَيْدٌ فَأَكْرَمْتُهُ belongs to أَكْرَمْتُهُ), whether or not fronting that part would otherwise be allowed; per al-Mubarrad the governed word of the dropped verb, always.",
         "What is al-Māzinī's middle position? If the fāʾ is the only thing that would block fronting, read it Sībawayh's way; if a second obstacle exists (a word that cannot be fronted for its own reason), read it al-Mubarrad's way. His formula: أَمَّا removes the obstacle that comes from the fāʾ and no other.",
         "What divides the three in one sentence each? Sībawayh: fronting across the fāʾ is a licence special to أَمَّا. Al-Mubarrad: there is no such licence; what stands there belongs to the dropped verb. Al-Māzinī: the licence is real but reaches only as far as the fāʾ's own obstacle.",
         "Why is بَعْدُ in أَمَّا بَعْدُ on a ḍamma? It is a ẓarf cut off from its muḍāf ilayh (بَعْدَ هَذَا) and built on the ḍamma — the مَبْنِيّ chapter's rule for the cut-off adverbs."],
  "tr": ["أَمَّا ne yapar? Önceden söylenmiş bir mücmeli («kardeşlerin geldi») alır ve maddelerini tek tek ele alır; her madde öne alınır, her cevap bir fâ ile açılır: أَمَّا زَيْدٌ فَأَكْرَمْتُهُ. Kitap başında ise istînaf açar: أَمَّا بَعْدُ.",
         "Düz bir isimden sonra niçin fâ var? Çünkü أَمَّا fiili hazfedilmiş bir ŞART harfidir — kitaplar onu مَهْمَا يَكُنْ مِنْ شَيْءٍ diye geri getirir — ve fâ, şart cevabının fâ'sıdır. Buradaki i'râb satırları tam bunu geri getirir ve fâ'yı atıf değil cevap bağlayıcısı olarak etiketler.",
         "أَمَّا ile fâ arasında ne durur? Bir şey durmalıdır, çünkü hazfedilen fiil boşluk bırakmıştır: Sîbeveyh'e göre fâ'dan sonraki kelâmın bir cüz'ü (أَمَّا زَيْدٌ فَأَكْرَمْتُهُ'daki زَيْدٌ, أَكْرَمْتُهُ'ya aittir), o cüz'ün öne alınması başka türlü câiz olsun olmasın; Müberred'e göre daima hazfedilen fiilin ma'mûlü.",
         "Mâzinî'nin orta görüşü nedir? Öne almayı engelleyen tek şey fâ ise Sîbeveyh gibi oku; ikinci bir mâni varsa (kendi sebebiyle öne alınamayan bir kelime) Müberred gibi oku. Formülü: أَمَّا fâ'dan gelen mâniyi kaldırır, başkasını kaldırmaz.",
         "Üçü birer cümleyle nerede ayrılır? Sîbeveyh: fâ'nın üzerinden öne alma أَمَّا'ya özel bir ruhsattır. Müberred: böyle bir ruhsat yoktur; orada duran hazfedilen fiile aittir. Mâzinî: ruhsat gerçektir ama yalnız fâ'nın kendi mânisine kadar uzanır.",
         "أَمَّا بَعْدُ'daki بَعْدُ niçin damme üzre? Muzâfun ileyhinden (بَعْدَ هَذَا) kesilmiş bir zarftır ve damme üzere mebnîdir — mebnî bâbının kesik zarflar kuralı."]},
 "plain": {
  "en": "Ammā means «as for…». You say the whole first («your brothers came»), then take them one at a time: «as for Zayd, I honoured him». A hidden «whatever may be» verb sits behind it, which is why a fāʾ always follows. The grammarians argued over what exactly may stand between ammā and that fāʾ.",
  "tr": "Emmâ «-e gelince» demektir. Önce bütünü söylersin («kardeşlerin geldi»), sonra tek tek alırsın: «Zeyd'e gelince ona ikram ettim». Arkasında gizli bir «ne olursa olsun» fiili vardır; fâ'nın hep izlemesi bundandır. Nahivciler emmâ ile o fâ arasında tam olarak neyin durabileceğini tartışmıştır."},
 "explanation": {
  "en": "The Kafiya's third conditional letter in the notebook's order: the tafṣīl function with its three-member example, the istiʾnāf use (أَمَّا بَعْدُ), the dropped verb, and the classical dispute over the slot between أَمَّا and the fāʾ — Sībawayh's part-of-the-answer reading, al-Mubarrad's governed-word reading, al-Māzinī's conditional synthesis — closed by the notebook's own question «what is the difference between the three imams?» and its three-line answer. The chapter's iʿrāb keeps one reading per token (the fronted noun as a mubtadaʾ whose khabar is the fāʾ-clause, which is the reading all three accept for the simple case) and leaves the dispute to the note.",
  "tr": "Kâfiye'nin defterdeki sırayla üçüncü şart harfi: üç üyeli örneğiyle tafsil işlevi, istînaf kullanımı (أَمَّا بَعْدُ), hazfedilen fiil ve أَمَّا ile fâ arasındaki yer üzerine klasik tartışma — Sîbeveyh'in cevabın-cüz'ü okuması, Müberred'in ma'mûl okuması, Mâzinî'nin şartlı sentezi — defterin kendi «üç imam arasındaki fark nedir?» sorusu ve üç satırlık cevabıyla kapanır. Bâbın i'râbı her kelimeye tek okuma verir (öne alınmış isim, haberi fâ cümlesi olan bir mübteda — basit hâlde üçünün de kabul ettiği okuma) ve tartışmayı nota bırakır."},
 "examples": [
  {"ar": "جَاءَتْنِي إِخْوَتُكَ: أَمَّا زَيْدٌ فَأَكْرَمْتُهُ، وَأَمَّا عَمْرٌو فَأَهَنْتُهُ، وَأَمَّا بِشْرٌ فَأَعْرَضْتُ عَنْهُ", "en": "Ammā detailing a sum.", "tr": "Mücmeli tafsil eden emmâ.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "أَمَّا بَعْدُ", "en": "The fresh-start ammā.", "tr": "İstînaf emmâ'sı.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "يُؤْتَى بَيْنَ أَمَّا وَالْفَاءِ بِجُزْءٍ مِنَ الْكَلَامِ الَّذِي بَعْدَ الْفَاءِ", "en": "Sībawayh's reading of the slot.", "tr": "Sîbeveyh'in yer okuması.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "أَمَّا تَرْفَعُ الْمَانِعَ الْآتِيَ مِنَ الْفَاءِ وَلَا تَرْفَعُ مَانِعًا آخَرَ", "en": "Al-Māzinī's formula.", "tr": "Mâzinî'nin formülü.", "sourceStory": "al-kafiya", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«أَمَّا زَيْدٌ أَكْرَمْتُهُ»",
   "right": "«أَمَّا زَيْدٌ فَأَكْرَمْتُهُ — emmâ'nın cevabı fâ ister»",
   "why": {"en": "Ammā is a condition with its verb dropped; its answer takes the fāʾ.", "tr": "Emmâ fiili hazfedilmiş bir şarttır; cevabı fâ alır."}},
  {"wrong": "«أَمَّا بَعْدَ»",
   "right": "«أَمَّا بَعْدُ — kesik zarf damme üzere mebnîdir»",
   "why": {"en": "Cut off from its muḍāf ilayh, baʿd is built on the ḍamma.", "tr": "Muzâfun ileyhinden kesilen baʿd damme üzere mebnîdir."}},
  {"wrong": "«fâ'dan sonraki her kelime emmâ'nın önüne alınabilir (Sîbeveyh)»",
   "right": "«Mâzinî: yalnız fâ'nın engellediği; başka bir mâni varsa ma'mûl getirilir»",
   "why": {"en": "The licence removes the fāʾ's obstacle only, on al-Māzinī's reading.", "tr": "Ruhsat, Mâzinî'ye göre yalnız fâ'nın mânisini kaldırır."}}],
 "relatedNotes": ["amma-tafsiliyya", "al-fa-fi-jawab-al-shart", "huruf-al-shart-fil-kafiya", "hadhf-wa-taqdir", "al-murab-wal-mabni-wal-irab"]}

ADD_EN = (" Chapter 43 (notebook lines ~347-348): ammā — detailing, the fresh-start use, the dropped verb, and the three imams on the slot before the fāʾ with the notebook's own question on their difference — the notebook's exposition, kept as commentary (s1-s6).")
ADD_TR = (" Kırk üçüncü bâb (defter satırları ~347-348): emmâ — tafsil, istînaf kullanımı, hazfedilen fiil ve fâ'dan önceki yer üzerine üç imam, defterin farkları üzerine kendi sorusuyla — defterin açıklaması, şerh olarak (s1-s6).")
write_out(43, S, TITLE, ADD_EN, ADD_TR, "347-348", GLOSS_ADD, notes=(NOTE,),
          related=(("amma-tafsiliyya", [K]), ("al-fa-fi-jawab-al-shart", [K])))
report(43, S, GLOSS_ADD, (NOTE,))
