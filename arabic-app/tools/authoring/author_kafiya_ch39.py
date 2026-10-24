# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 39: THE LETTERS OF AUGMENTATION — إِنْ, أَنْ, مَا, لَا, مِنْ, the bāʾ and the lām; what «augmented» means (the
basic meaning survives their removal; they still carry lafẓī and maʿnawī benefit); إِنْ after مَا nāfiya, after مَا maṣdariyya and لَمَّا;
أَنْ after لَمَّا, between the oath and لَوْ, after the kāf; مَا with the conditional tools, with a jarr letter, with the muḍāf; لَا after a
negation with the wāw, after أَنْ, before أُقْسِمُ, with the muḍāf (shādhdh).
Source: the Ottoman notebook (Ziya Sungur-oglu), line ~345 of the transcription.

  COMMENTARY (the notebook): s1-s7 — marked C_EN/C_TR. Qur'anic citations as the mushaf prints them (3:159, 17:110, 12:96, 7:12, 75:1);
  the notebook writes تَدْعُو and أَنْ لَا — recorded as divergences in the attribution.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch39.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "huruf-al-ziyada-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "حُرُوفُ الزِّيَادَةِ", "en": "The letters of augmentation — in, an, mā and lā where they add nothing to the structure and something to the speech", "tr": "Ziyâde harfleri — yapıya bir şey katmayıp söze bir şey katan in, en, mâ ve lâ"}
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
ZD = "huruf-al-ziyada-fil-kafiya"
def ZL(full, lex, en, tr, inner=None, punct=None, pos="part"):
    if inner: return cited_wa(full, lex, pos, [AT, K], inner + " مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", en, tr, inner, punct=punct)
    return cited(full, lex, pos, ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", en, tr, punct=punct)
def TUZAD(en="«is augmented».", tr="«ziyade kılınır».", tags=()):
    return W("تُزَادُ", "zada", "verb", ["mubtada-khabar", "naib-al-fail", "hollow-verbs"] + list(tags), "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — الْجُمْلَةُ خَبَرٌ.", en, tr)
def MAA(en="«with».", tr="«... ile»."): return W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", en, tr)
def ZAYD_N(punct=None): return cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd».", punct=punct)
def QUMTU(punct="."): return cited("قُمْتُ", "qama", "verb", ["fail", "hollow-verbs", "al-fa-fi-jawab-al-shart"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جَوَابُ لَمَّا.", "«I stood».", "«ben de kalktım».", punct=punct, segments=[seg("قُمْ", "qama", "verb"), prT()])
def ZAID_W(full, ar, en, tr, lex, pos="part", punct=None, segments=None):
    return cited(full, lex, pos, [K, "majaz-ziyada-nuqsan"], ar, en, tr, punct=punct, segments=segments)

S.append({"id": "s1", "translation": {
 "en": "The letters of augmentation are إِنْ, أَنْ, مَا, لَا, مِنْ, the bāʾ and the lām; and they are called the letters of augmentation because they are used as augmented in some places — not that they are always used so." + C_EN,
 "tr": "Ziyâde harfleri إِنْ, أَنْ, مَا, لَا, مِنْ, bâ ve lâm'dır; bunlara ziyâde harfleri denmesi bazı yerlerde zâid olarak kullanıldıkları içindir — yoksa daima zâid olarak kullanılırlar demek değildir." + C_TR},
 "tokens": [
  W("حُرُوفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harfleri»."),
  W("الزِّيَادَةِ", "ziyada", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«augmentation».", "«ziyâde».", punct=":"),
  cited("إِنْ", "in-zaida", "part", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ — خَبَرٌ.", "«in».", "«in»."),
  ZL("وَأَنْ", "an-masdariyya", "«an».", "«en».", "أَنْ"),
  ZL("وَمَا", "ma-zaida", "«mā».", "«mâ».", "مَا"),
  ZL("وَلَا", "la-nafiya", "«lā».", "«lâ».", "لَا"),
  ZL("وَمِنْ", "min", "«min».", "«min».", "مِنْ", pos="prep"),
  ZL("وَالْبَاءُ", "ba-harf", "«the bāʾ».", "«bâ».", "الْبَاءُ", pos="noun"),
  ZL("وَاللَّامُ", "lam-letter", "«and the lām».", "«ve lâm».", "اللَّامُ", punct="؛", pos="noun"),
  atf_wa("وَسُمِّيَتْ", "samma", "verb", ["naib-al-fail", "form-ii-verbs", "naqis-verbs"], "سُمِّيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and they are called».", "«ve ... denmesi».", "سُمِّيَتْ", extra_segs=[seg("سُمِّيَ", "samma", "verb"), seg("تْ", "ta-tanith", "part")]),
  W("حُرُوفَ", "harf", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the letters of».", "«harfleri»."),
  W("الزِّيَادَةِ", "ziyada", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«augmentation».", "«ziyâde»."),
  W("لِأَنَّهَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because they».", "«çünkü onlar».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("تُسْتَعْمَلُ", "istamala", "verb", ["inna-wa-akhawatuha", "naib-al-fail", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — الْجُمْلَةُ خَبَرُ أَنَّ.", "«are used».", "«kullanılır»."),
  W("زَائِدَةً", "zaid", "noun", ["hal", "ism-fail"], "حَالٌ مَنْصُوبٌ.", "«as augmented».", "«zâid olarak»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("بَعْضِ", "bad", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«some».", "«bazı»."),
  W("الْمَوَاضِعِ", "mawdi", "noun", ["idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ أُضِيفَتْ فَجُرَّتْ بِالْكَسْرَةِ.", "«places».", "«yerlerde».", punct="،"),
  W("لَا", "la-nafiya", "part", ["la-nafiya", AT], "عَاطِفَةٌ لِلنَّفْيِ.", "«not».", "«... değil»."),
  W("دَائِمًا", "daiman", "adv", ["maful-fih"], "ظَرْفٌ مَنْصُوبٌ.", "«always».", "«daima».", punct="."),
 ]})

S.append({"id": "s2", "translation": {
 "en": "And the meaning of their being augmented is that the basic meaning is not disturbed by their falling away — not that they have no meaning at all; for they have benefits of wording, such as beautifying the speech and making it more eloquent, and benefits of meaning, such as emphasis." + C_EN,
 "tr": "Ziyâde olmalarının mânâsı, düşmeleriyle aslî mânânın bozulmamasıdır — yoksa hiç mânâları yok demek değildir; zira onların sözü güzelleştirmek ve daha fasih kılmak gibi lafzî, te'kid gibi mânevî faydaları vardır." + C_TR},
 "tokens": [
  atf_wa("وَمَعْنَى", "mana", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus"], "مَعْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«and the meaning of».", "«ve ... mânâsı».", "مَعْنَى"),
  W("زِيَادَتِهَا", "ziyada", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their augmentation».", "«ziyâde olmalarının».", segments=[seg("زِيَادَتِ", "ziyada", "noun"), pr3fs()]),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mubtada-khabar"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ خَبَرٌ.", "«is that».", "«... -dır»."),
  W("الْمَعْنَى", "mana", "noun", ["inna-wa-akhawatuha", "ism-maqsur-manqus"], "اسْمُ أَنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«the meaning».", "«mânânın»."),
  W("الْأَصْلِيَّ", "asli", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَنْصُوبَةٌ.", "«basic».", "«aslî»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-ma-»."),
  W("يَخْتَلُّ", "ikhtalla", "verb", ["inna-wa-akhawatuha", "fail", "form-viii-verbs", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — الْجُمْلَةُ خَبَرُ أَنَّ.", "«is disturbed».", "«bozulmaması»."),
  bi_("بِسُقُوطِهَا", "suqut", "noun", ["idafa-definiteness"], "سُقُوطِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — الْبَاءُ لِلسَّبَبِيَّةِ.", "«by their falling away».", "«düşmeleriyle».", "سُقُوطِ", punct="،", segs=[seg("بِ", "bi", "prep"), seg("سُقُوطِ", "suqut", "noun"), pr3fs()]),
  W("لَا", "la-nafiya", "part", ["la-nafiya", AT], "عَاطِفَةٌ لِلنَّفْيِ.", "«not».", "«yoksa ... değil»."),
  W("أَنَّهَا", "anna", "part", ["inna-wa-akhawatuha", AT], "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا — الْمَصْدَرُ مَعْطُوفٌ.", "«that they».", "«onların».", segments=[seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("لَا", "la-nafiya", "part", ["la-nafiya-lil-jins", "inna-wa-akhawatuha"], "لَا النَّافِيَةُ لِلْجِنْسِ — الْجُمْلَةُ خَبَرُ أَنَّ.", "«no».", "«hiç ... yok»."),
  W("مَعْنَى", "mana", "noun", ["la-nafiya-lil-jins", "ism-maqsur-manqus"], "اسْمُ لَا مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ.", "«meaning».", "«mânâları»."),
  W("لَهَا", "li", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَا.", "«to them».", "«onların».", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  W("أَصْلًا", "asl", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ — بِمَعْنَى الْبَتَّةَ.", "«at all».", "«asla».", punct="؛"),
  W("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«zira».", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")]),
  W("لَهَا", "li", "prep", ["huruf-jarr", "inna-wa-akhawatuha", "taqdim-al-musnad"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ إِنَّ مُقَدَّمٌ.", "«they have».", "«onların ... vardır».", segments=[seg("لَ", "li", "prep"), pr3fs()]),
  W("فَوَائِدَ", "faida", "noun", ["inna-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf"], "اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ.", "«benefits».", "«faydaları»."),
  W("لَفْظِيَّةً", "lafzi", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَنْصُوبَةٌ.", "«of wording».", "«lafzî»."),
  ka_("كَتَحْسِينِ", "tahsin", "noun", ["idafa-definiteness", "form-ii-verbs"], "تَحْسِينِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«such as beautifying».", "«güzelleştirmek gibi».", "تَحْسِينِ"),
  W("الْكَلَامِ", "kalam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speech».", "«sözü»."),
  atf_wa("وَتَفْصِيحِهِ", "tafsih", "noun", [AT, "idafa-definiteness"], "تَفْصِيحِ مَعْطُوفٌ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and making it more eloquent».", "«ve daha fasih kılmak».", "تَفْصِيحِهِ", punct="،", extra_segs=[seg("تَفْصِيحِ", "tafsih", "noun"), pr3msi()]),
  atf_wa("وَمَعْنَوِيَّةً", "manawi", "noun", [AT, "ism-mansub"], "مَعْنَوِيَّةً مَعْطُوفٌ عَلَى لَفْظِيَّةً مَنْصُوبٌ.", "«and of meaning».", "«ve mânevî».", "مَعْنَوِيَّةً"),
  ka_("كَالتَّأْكِيدِ", "takid", "noun", [], "التَّأْكِيدِ مَجْرُورٌ.", "«such as emphasis».", "«te'kid gibi».", "التَّأْكِيدِ", punct=".", segs=[seg("كَ", "ka", "prep"), seg("التَّأْكِيدِ", "takid", "noun")]),
 ]})

S.append({"id": "s3", "translation": {
 "en": "So of His saying, exalted is He, «فَبِمَا رَحْمَةٍ مِنَ اللهِ لِنْتَ لَهُمْ» it is said «مَا is augmented», and it is not said «it has no benefit»." + C_EN,
 "tr": "Nitekim Allah Teâlâ'nın «فَبِمَا رَحْمَةٍ مِنَ اللهِ لِنْتَ لَهُمْ» kavli için «مَا zâiddir» denir; fakat «faydasızdır» denmez." + C_TR},
 "tokens": [
  W("فَيُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«so it is said».", "«nitekim ... denir».", segments=[seg("فَ", "fa", "conj"), seg("يُقَالُ", "qala", "verb")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«... için»."),
  W("قَوْلِهِ", "qawl", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His saying».", "«kavli».", segments=[seg("قَوْلِ", "qawl", "noun"), pr3msi()]),
  W("تَعَالَى", "taala", "verb", ["fail", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«exalted is He».", "«Teâlâ».", punct=":"),
  ZAID_W("فَبِمَا", "الْفَاءُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَمَا زَائِدَةٌ لِلتَّأْكِيدِ.", "«so by (-) mercy».", "«(-) bir rahmetle».", "ma-zaida", segments=[seg("فَ", "fa", "conj"), seg("بِ", "bi", "prep"), seg("مَا", "ma-zaida", "part")]),
  cited("رَحْمَةٍ", "rahma", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْبَاءِ — وَمَا الزَّائِدَةُ لَا تَمْنَعُ عَمَلَهَا.", "«mercy».", "«rahmet»."),
  cited("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، فُتِحَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-tan»."),
  cited("اللهِ", "allah", "propn", ["huruf-jarr"], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«Allah».", "«Allah'tan»."),
  cited("لِنْتَ", "lana", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«you were gentle».", "«yumuşak oldun».", segments=[seg("لِنْ", "lana", "verb"), prTa()]),
  cited("لَهُمْ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَهُمْ مَجْرُورٌ.", "«to them».", "«onlara».", punct=":", segments=[seg("لَ", "li", "prep"), pr3mp()]),
  cited("مَا", "ma-zaida", "part", ["mubtada-khabar", K], "لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ — الْمَقُولُ.", "«mā».", "«mâ»."),
  W("زَائِدَةٌ", "zaid", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ.", "«is augmented».", "«zâiddir».", punct="،"),
  atf_wa("وَلَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ.", "«and not».", "«fakat ... -mez».", "لَا"),
  W("يُقَالُ", "qala", "verb", ["naib-al-fail", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«it is said».", "«denmez».", punct=":"),
  W("لَا", "la-nafiya", "part", ["la-nafiya-lil-jins", "naib-al-fail"], "لَا النَّافِيَةُ لِلْجِنْسِ — الْجُمْلَةُ الْمَقُولَةُ نَائِبُ فَاعِلٍ.", "«no».", "«... yoktur»."),
  W("فَائِدَةَ", "faida", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ.", "«benefit».", "«faydası»."),
  W("لَهَا", "li", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرُ لَا.", "«it has».", "«onun».", punct=".", segments=[seg("لَ", "li", "prep"), pr3fs()]),
 ]})

S.append({"id": "s4", "translation": {
 "en": "And إِنْ is often augmented with the negating مَا — as مَا إِنْ رَأَيْتُ زَيْدًا — and rarely with the maṣdar-مَا and with لَمَّا — as اِنْتَظِرْنِي مَا إِنْ جَلَسَ الْقَاضِي and لَمَّا إِنْ قَامَ زَيْدٌ قُمْتُ." + C_EN,
 "tr": "إِنْ, nâfiye مَا ile çokça zâid olur — مَا إِنْ رَأَيْتُ زَيْدًا gibi; masdariye مَا ve لَمَّا ile az zâid olur — اِنْتَظِرْنِي مَا إِنْ جَلَسَ الْقَاضِي ve لَمَّا إِنْ قَامَ زَيْدٌ قُمْتُ gibi." + C_TR},
 "tokens": [
  cited_wa("وَإِنْ", "in-zaida", "part", ["mubtada-khabar", K], "إِنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and in».", "«in».", "إِنْ"),
  TUZAD(),
  W("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ: زِيَادَةً كَثِيرَةً.", "«often».", "«çokça»."),
  MAA(),
  cited("مَا", "ma-nafiya", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«mā».", "«mâ»."),
  W("النَّافِيَةِ", "nafi", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ.", "«the negating».", "«nâfiye».", punct="،"),
  nahwu(),
  cited("مَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "نَافِيَةٌ.", "«not».", "«-me-»."),
  ZAID_W("إِنْ", "زَائِدَةٌ بَعْدَ مَا النَّافِيَةِ لِتَأْكِيدِ النَّفْيِ.", "«(-)».", "«(kesinlikle)».", "in-zaida"),
  cited("رَأَيْتُ", "raa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw».", "«gördüm».", segments=[seg("رَأَيْ", "raa", "verb"), prT()]),
  cited("زَيْدًا", "zayd", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd».", "«Zeyd'i».", punct="،"),
  atf_wa("وَقَلِيلًا", "qalil", "noun", [AT, "maful-mutlaq"], "قَلِيلًا مَعْطُوفٌ عَلَى كَثِيرًا.", "«and rarely».", "«ve az».", "قَلِيلًا"),
  MAA(),
  cited("مَا", "ma-masdariyya", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«mā».", "«mâ»."),
  W("الْمَصْدَرِيَّةِ", "masdariyya", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَجْرُورَةٌ.", "«the maṣdar».", "«masdariye»."),
  cited_wa("وَلَمَّا", "lamma", "part", [AT], "لَمَّا مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and lammā».", "«ve lemmâ».", "لَمَّا", punct="،"),
  nahwu(),
  cited("اِنْتَظِرْنِي", "intazara", "verb", ["fail", "maful-bihi", "form-viii-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«wait for me».", "«beni bekle».", segments=[seg("اِنْتَظِرْ", "intazara", "verb"), pr1s()]),
  cited("مَا", "ma-masdariyya", "part", ["anwa-ma", "maful-fih"], "مَصْدَرِيَّةٌ ظَرْفِيَّةٌ: مُدَّةَ جُلُوسِ الْقَاضِي.", "«as long as».", "«... müddetçe»."),
  ZAID_W("إِنْ", "زَائِدَةٌ بَعْدَ مَا الْمَصْدَرِيَّةِ.", "«(-)».", "«(-)».", "in-zaida"),
  cited("جَلَسَ", "jalasa", "verb", ["fail"], "فِعْلٌ مَاضٍ.", "«sits».", "«oturduğu»."),
  cited("الْقَاضِي", "qadi", "noun", ["fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ.", "«the judge».", "«kadı».", punct="،"),
  cited_wa("وَلَمَّا", "lamma", "part", ["al-majzum-wal-shart-wal-jaza", "maful-fih"], "لَمَّا ظَرْفٌ بِمَعْنَى حِينَ.", "«and when».", "«ve ... -ınca».", "لَمَّا"),
  ZAID_W("إِنْ", "زَائِدَةٌ بَعْدَ لَمَّا.", "«(-)».", "«(-)».", "in-zaida"),
  cited("قَامَ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«stood».", "«kalkınca»."),
  ZAYD_N(),
  QUMTU(),
 ]})

S.append({"id": "s5", "translation": {
 "en": "And أَنْ is often augmented with لَمَّا — as «فَلَمَّا أَنْ جَاءَ الْبَشِيرُ» — and between the oath and لَوْ — as وَاللهِ أَنْ لَوْ قَامَ زَيْدٌ قُمْتُ — and rarely with the kāf — as كَأَنْ ظَبْيَةٍ." + C_EN,
 "tr": "أَنْ, لَمَّا ile çokça zâid olur — «فَلَمَّا أَنْ جَاءَ الْبَشِيرُ» gibi; kasem ile لَوْ arasında da — وَاللهِ أَنْ لَوْ قَامَ زَيْدٌ قُمْتُ gibi; kâf ile az zâid olur — كَأَنْ ظَبْيَةٍ gibi." + C_TR},
 "tokens": [
  cited_wa("وَأَنْ", "an-masdariyya", "part", ["mubtada-khabar", K], "أَنْ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and an».", "«en».", "أَنْ"),
  TUZAD(),
  W("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ.", "«often».", "«çokça»."),
  MAA(),
  cited("لَمَّا", "lamma", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«lammā».", "«lemmâ».", punct="،"),
  nahwu(),
  cited("فَلَمَّا", "lamma", "part", ["al-majzum-wal-shart-wal-jaza", "maful-fih"], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ.", "«so when».", "«... gelince».", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  ZAID_W("أَنْ", "زَائِدَةٌ بَعْدَ لَمَّا.", "«(-)».", "«(-)».", "an-masdariyya"),
  cited("جَاءَ", "jaa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«came».", "«geldi»."),
  cited("الْبَشِيرُ", "bashir", "noun", ["fail", "sifa-mushabbaha"], "فَاعِلٌ مَرْفُوعٌ.", "«the bearer of good news».", "«müjdeci».", punct="،"),
  atf_wa("وَبَيْنَ", "bayna", "noun", [AT, "maful-fih", "idafa-definiteness"], "بَيْنَ ظَرْفٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى مَعَ، وَهُوَ مُضَافٌ.", "«and between».", "«ve ... arasında».", "بَيْنَ"),
  W("الْقَسَمِ", "qasam", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the oath».", "«kasem»."),
  cited_wa("وَلَوْ", "law", "part", [AT], "لَوْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and law».", "«ile lev».", "لَوْ", punct="،"),
  nahwu(),
  cited("وَاللهِ", "allah", "propn", ["huruf-al-qasam-fil-kafiya", "huruf-jarr"], "الْوَاوُ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«by Allah».", "«vallahi».", segments=[seg("وَ", "waw-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  ZAID_W("أَنْ", "زَائِدَةٌ بَيْنَ الْقَسَمِ وَلَوْ.", "«(-)».", "«(-)».", "an-masdariyya"),
  cited("لَوْ", "law", "part", ["al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ لِلِامْتِنَاعِ.", "«if».", "«şayet».", ),
  cited("قَامَ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ.", "«had stood».", "«kalksaydı»."),
  ZAYD_N(),
  cited("قُمْتُ", "qama", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — جَوَابُ لَوْ وَالْقَسَمِ.", "«I would have stood».", "«ben de kalkardım».", punct="،", segments=[seg("قُمْ", "qama", "verb"), prT()]),
  atf_wa("وَقَلِيلًا", "qalil", "noun", [AT, "maful-mutlaq"], "قَلِيلًا مَعْطُوفٌ.", "«and rarely».", "«ve az».", "قَلِيلًا"),
  MAA(),
  W("الْكَافِ", "kaf-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the kāf».", "«kâf».", punct="،"),
  nahwu(),
  ZAID_W("كَأَنْ", "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَأَنْ زَائِدَةٌ.", "«like (-)».", "«(-) gibi».", "an-masdariyya", segments=[seg("كَ", "ka", "prep"), seg("أَنْ", "an-masdariyya", "part")]),
  cited("ظَبْيَةٍ", "zabya", "noun", ["huruf-jarr", "tashbih"], "مَجْرُورٌ بِالْكَافِ.", "«a gazelle».", "«bir ceylan».", punct="."),
 ]})

S.append({"id": "s6", "translation": {
 "en": "And مَا is augmented with إِذَا, مَتَى, أَيّ, أَيْنَ and إِنْ — these words being used with مَا as tools of condition, as «أَيًّا مَا تَدْعُوا فَلَهُ الْأَسْمَاءُ الْحُسْنَى» — and with some jarr letters, as «فَبِمَا رَحْمَةٍ», and rarely with the muḍāf, as غَضِبْتُ مِنْ غَيْرِ مَا جُرْمٍ." + C_EN,
 "tr": "مَا, إِذَا, مَتَى, أَيّ, أَيْنَ ve إِنْ ile zâid olur — bu kelimeler مَا ile şart edatı olarak kullanılır, «أَيًّا مَا تَدْعُوا فَلَهُ الْأَسْمَاءُ الْحُسْنَى» gibi; bazı cer harfleriyle de — «فَبِمَا رَحْمَةٍ» gibi; muzâf ile az zâid olur — غَضِبْتُ مِنْ غَيْرِ مَا جُرْمٍ gibi." + C_TR},
 "tokens": [
  cited_wa("وَمَا", "ma-zaida", "part", ["mubtada-khabar", K], "مَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and mā».", "«mâ».", "مَا"),
  TUZAD(),
  MAA(),
  cited("إِذَا", "idha", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«idhā».", "«izâ»."),
  cited_wa("وَمَتَى", "mata", "part", [AT], "مَتَى مَعْطُوفٌ — اللَّفْظُ مَحْكِيٌّ.", "«matā».", "«metâ».", "مَتَى"),
  cited_wa("وَأَيٍّ", "ayy", "noun", [AT], "أَيٍّ مَعْطُوفٌ مَجْرُورٌ.", "«ayy».", "«eyy».", "أَيٍّ"),
  cited_wa("وَأَيْنَ", "ayna", "part", [AT], "أَيْنَ مَعْطُوفٌ — اللَّفْظُ مَحْكِيٌّ.", "«ayna».", "«eyne».", "أَيْنَ"),
  cited_wa("وَإِنْ", "in-shartiyya", "part", [AT], "إِنْ مَعْطُوفٌ — الْحَرْفُ مَحْكِيٌّ.", "«and in».", "«ve in».", "إِنْ", punct="،"),
  atf_wa("وَتُسْتَعْمَلُ", "istamala", "verb", ["naib-al-fail", "form-x-verbs", "al-hal-jumla-wa-rabituha"], "تُسْتَعْمَلُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — الْجُمْلَةُ حَالٌ.", "«these words being used».", "«kullanılır».", "تُسْتَعْمَلُ"),
  W("هَذِهِ", "hadhihi", "pron", ["naib-al-fail", "asma-al-ishara-wal-mawsulat"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«these».", "«bu»."),
  W("الْكَلِمَاتُ", "kalima", "noun", ["badal", "jam-muannath-salim"], "بَدَلٌ مَرْفُوعٌ.", "«words».", "«kelimeler»."),
  MAA(),
  cited("مَا", "ma-zaida", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ.", "«mā».", "«mâ»."),
  W("أَدَوَاتِ", "adat", "noun", ["hal", "idafa-definiteness", "jam-muannath-salim"], "حَالٌ مَنْصُوبٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«as tools of».", "«edatı olarak»."),
  W("شَرْطٍ", "shart", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«condition».", "«şart».", punct="،"),
  nahwu(),
  cited("أَيًّا", "ayy", "noun", ["maful-bihi", "al-majzum-wal-shart-wal-jaza"], "اسْمُ شَرْطٍ مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ.", "«whichever».", "«hangisiyle»."),
  ZAID_W("مَا", "زَائِدَةٌ بَعْدَ أَيٍّ.", "«(-)».", "«(-)».", "ma-zaida"),
  cited("تَدْعُوا", "daa", "verb", ["al-majzum-wal-shart-wal-jaza", "fail", "naqis-verbs"], "فِعْلُ الشَّرْطِ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«you call».", "«dua ederseniz»."),
  cited("فَلَهُ", "li", "prep", ["al-fa-fi-jawab-al-shart", "huruf-jarr", "taqdim-al-musnad"], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَلَهُ خَبَرٌ مُقَدَّمٌ.", "«to Him belong».", "«O'nundur».", segments=[seg("فَ", "fa", "conj"), seg("لَ", "li", "prep"), pr3ms()]),
  cited("الْأَسْمَاءُ", "ism", "noun", ["mubtada-khabar", "jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the names».", "«isimler»."),
  cited("الْحُسْنَى", "husna", "noun", ["naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«most beautiful».", "«en güzel».", punct="؛"),
  atf_wa("وَمَعَ", "maa", "noun", [AT, "maful-fih", "idafa-definiteness"], "مَعَ ظَرْفٌ مَنْصُوبٌ مَعْطُوفٌ، وَهُوَ مُضَافٌ.", "«and with».", "«ve ... ile».", "مَعَ"),
  W("بَعْضِ", "bad", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«some».", "«bazı»."),
  W("حُرُوفِ", "harf", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«letters of».", "«harfleriyle»."),
  W("الْجَرِّ", "jarr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer».", punct="،"),
  nahwu(),
  ZAID_W("فَبِمَا", "الْفَاءُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَمَا زَائِدَةٌ.", "«so by (-)».", "«(-) ile».", "ma-zaida", segments=[seg("فَ", "fa", "conj"), seg("بِ", "bi", "prep"), seg("مَا", "ma-zaida", "part")]),
  cited("رَحْمَةٍ", "rahma", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْبَاءِ.", "«mercy».", "«bir rahmet».", punct="؛"),
  atf_wa("وَقَلِيلًا", "qalil", "noun", [AT, "maful-mutlaq"], "قَلِيلًا مَعْطُوفٌ.", "«and rarely».", "«ve az».", "قَلِيلًا"),
  MAA(),
  W("الْمُضَافِ", "mudaf", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāf».", "«muzâf».", punct="،"),
  nahwu(),
  cited("غَضِبْتُ", "ghadiba", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I became angry».", "«öfkelendim».", segments=[seg("غَضِبْ", "ghadiba", "verb"), prT()]),
  cited("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  cited("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«without».", "«-sız»."),
  ZAID_W("مَا", "زَائِدَةٌ بَيْنَ الْمُضَافِ وَالْمُضَافِ إِلَيْهِ.", "«(-)».", "«(-)».", "ma-zaida"),
  cited("جُرْمٍ", "jurm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَمْ تَمْنَعْ مَا الزَّائِدَةُ الْإِضَافَةَ.", "«any offence».", "«bir suç».", punct="."),
 ]})

S.append({"id": "s7", "translation": {
 "en": "And لَا is augmented after a negation with the wāw of coordination — as مَا جَاءَ زَيْدٌ وَلَا عَمْرٌو — and after the maṣdar-أَنْ, as in «مَا مَنَعَكَ أَلَّا تَسْجُدَ إِذْ أَمَرْتُكَ», and rarely before أُقْسِمُ, as «لَا أُقْسِمُ بِيَوْمِ الْقِيَامَةِ», and irregularly with the muḍāf, as فِي بِئْرِ لَا حُورٍ." + C_EN,
 "tr": "لَا, nefyden sonra atıf vâvıyla zâid olur — مَا جَاءَ زَيْدٌ وَلَا عَمْرٌو gibi; masdariye أَنْ'den sonra da — «مَا مَنَعَكَ أَلَّا تَسْجُدَ إِذْ أَمَرْتُكَ» âyetindeki gibi; أُقْسِمُ'den önce az zâid olur — «لَا أُقْسِمُ بِيَوْمِ الْقِيَامَةِ» gibi; muzâf ile zâid olması şâzdır — فِي بِئْرِ لَا حُورٍ gibi." + C_TR},
 "tokens": [
  cited_wa("وَلَا", "la-nafiya", "part", ["mubtada-khabar", K], "لَا لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and lā».", "«lâ».", "لَا"),
  TUZAD(),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«-den sonra»."),
  W("النَّفْيِ", "nafy", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a negation».", "«nefy»."),
  MAA(),
  W("وَاوِ", "waw-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the wāw of».", "«vâvıyla»."),
  W("الْعَطْفِ", "atf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«coordination».", "«atıf».", punct="،"),
  nahwu(),
  cited("مَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "نَافِيَةٌ.", "«not».", "«-me-»."),
  cited("جَاءَ", "jaa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«came».", "«geldi»."),
  ZAYD_N(),
  ZAID_W("وَلَا", "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor (-)».", "«ne de (-)».", "la-nafiya", segments=[seg("وَ", "waw-atf", "conj"), seg("لَا", "la-nafiya", "part")]),
  cited("عَمْرٌو", "amr-name", "propn", [AT], "مَعْطُوفٌ مَرْفُوعٌ.", "«ʿAmr».", "«Amr».", punct="،"),
  atf_wa("وَبَعْدَ", "bada", "noun", [AT, "maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَعْطُوفٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... -den sonra».", "بَعْدَ"),
  cited("أَنِ", "an-masdariyya", "part", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — الْحَرْفُ مَحْكِيٌّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«an».", "«en»."),
  W("الْمَصْدَرِيَّةِ", "masdariyya", "noun", ["naat-sifa", "ism-mansub"], "صِفَةٌ مَجْرُورَةٌ.", "«the maṣdar».", "«masdariye».", punct="،"),
  nahwu(),
  cited("مَا", "ma-istifham", "pron", ["mubtada-khabar", "anwa-ma"], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ.", "«what».", "«ne»."),
  cited("مَنَعَكَ", "manaa", "verb", ["mubtada-khabar", "fail", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْكَافُ مَفْعُولٌ بِهِ — الْجُمْلَةُ خَبَرٌ.", "«prevented you».", "«seni alıkoydu».", segments=[seg("مَنَعَ", "manaa", "verb"), pr2ms()]),
  ZAID_W("أَلَّا", "أَنْ مَصْدَرِيَّةٌ نَاصِبَةٌ، وَلَا زَائِدَةٌ — أُدْغِمَتِ النُّونُ فِي اللَّامِ.", "«from (-) ».", "«(-) -maktan».", "alla"),
  cited("تَسْجُدَ", "sajada", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«prostrating».", "«secde etmekten»."),
  cited("إِذْ", "idh", "noun", ["maful-fih"], "ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ عَلَى السُّكُونِ.", "«when».", "«-diğimde»."),
  cited("أَمَرْتُكَ", "amara-command", "verb", ["fail", "maful-bihi", "idafa-definiteness"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — الْجُمْلَةُ مُضَافٌ إِلَيْهَا.", "«I commanded you».", "«sana emrettiğimde».", punct="،", segments=[seg("أَمَرْ", "amara-command", "verb"), prT(), pr2ms()]),
  atf_wa("وَقَلِيلًا", "qalil", "noun", [AT, "maful-mutlaq"], "قَلِيلًا مَعْطُوفٌ.", "«and rarely».", "«ve az».", "قَلِيلًا"),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«-den önce»."),
  cited("أُقْسِمُ", "aqsama", "verb", ["idafa-definiteness", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ — اللَّفْظُ مَحْكِيٌّ.", "«uqsimu».", "«uksimu».", punct="،"),
  nahwu(),
  ZAID_W("لَا", "زَائِدَةٌ قَبْلَ فِعْلِ الْقَسَمِ.", "«(-)».", "«(-)».", "la-nafiya"),
  cited("أُقْسِمُ", "aqsama", "verb", ["fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I swear».", "«yemin ederim»."),
  bi_("بِيَوْمِ", "yawm", "noun", ["idafa-definiteness"], "يَوْمِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«by the Day of».", "«gününe».", "يَوْمِ"),
  cited("الْقِيَامَةِ", "qiyama", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Resurrection».", "«kıyamet».", punct="،"),
  atf_wa("وَشَاذًّا", "shadhdh", "noun", [AT, "hal"], "شَاذًّا حَالٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى قَلِيلًا.", "«and irregularly».", "«ve şâz olarak».", "شَاذًّا"),
  MAA(),
  W("الْمُضَافِ", "mudaf", "noun", ["idafa-definiteness", "ism-maful"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāf».", "«muzâf».", punct="،"),
  nahwu(),
  cited("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("بِئْرِ", "bir", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the well of».", "«kuyusunda»."),
  ZAID_W("لَا", "زَائِدَةٌ بَيْنَ الْمُضَافِ وَالْمُضَافِ إِلَيْهِ — شَاذٌّ.", "«(-)».", "«(-)».", "la-nafiya"),
  cited("حُورٍ", "hur", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«perdition».", "«helâk».", punct="."),
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
 "ikhtalla": need("ikhtalla", "اِخْتَلَّ", "خ ل ل", "verb", "to be disturbed, to be thrown out of order (Form VIII, geminate)", "bozulmak, düzeni sarsılmak (iftiʿâl, muzâaf)", 4),
 "suqut": need("suqut", "سُقُوط", "س ق ط", "noun", "falling away, dropping (masdar of سَقَطَ)", "düşme, sâkıt olma (sekata'nın masdarı)", 3),
 "tafsih": need("tafsih", "تَفْصِيح", "ف ص ح", "noun", "making (speech) more eloquent (masdar, Form II)", "fasih kılma (tefʿîl masdarı)", 4),
 "hur": need("hur", "حُور", "ح و ر", "noun", "perdition, ruin — فِي بِئْرِ لَا حُورٍ «in the well of perdition»", "helâk, hüsran — فِي بِئْرِ لَا حُورٍ «helâk kuyusunda»", 5),
 "alla": need("alla", "أَلَّا", "أ ن", "part", "an + lā written as one — the nāṣib أَنْ with an augmented لَا after it (7:12)", "en + lâ bir yazılmış — nâsıb أَنْ ve ardındaki zâid لَا (7:12)", 4),
 "waw-atf": need("waw-atf", "وَ (الْعَطْف)", "و", "conj", "the wāw of coordination — «and», joining two terms in one ruling", "atıf vâvı — «ve», iki terimi bir hükümde birleştirir", 1),
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
put_morph(mo, "ikhtalla", _nfc(_sg.entry(_sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِخْتِلَال", "مُخْتَلّ", _sg.mazi14("اِخْتَلّ", "اِخْتَلَل"), _sg.mudari14("َ", "خْتَلّ", "خْتَلِل"), ["اِخْتَلَّ", "اِخْتَلَّا", "اِخْتَلُّوا", "اِخْتَلِّي", "اِخْتَلَّا", "اِخْتَلِلْنَ"], "يَخْتَلَّ", "يَخْتَلَّ", "تَخْتَلَّ", "مُخْتَلّ", "اُخْتُلَّ", "يُخْتَلُّ", "اِخْتَلَّ النِّظَامُ: فَسَدَ وَاضْطَرَبَ — بَابُ الِافْتِعَالِ مِنَ الْمُضَاعَفِ، يُدْغَمُ حَيْثُ تَحَرَّكَتِ اللَّامُ الثَّانِيَةُ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch38 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "حُرُوفُ الزِّيَادَةِ فِي الْكَافِيَةِ", "en": "The letters of augmentation in the Kafiya: what «augmented» means, and where in, an, mā and lā are augmented", "tr": "Kâfiye'de ziyâde harfleri: «zâid» ne demektir, in, en, mâ ve lâ nerede zâid olur"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — حروف الزيادة: إن وأن وما ولا ومن والباء واللام", "ضياء صونغور اوغلى — دفتر الكافية: معنى الزيادة أن الأصل لا يختل بسقوطها وليس أن لا فائدة لها؛ مواضع إن وأن وما ولا بأمثلتها"],
 "question": {
  "en": ["What does «augmented» mean? Drop the letter and the sentence still says what it said: مَا رَأَيْتُ زَيْدًا with or without إِنْ. It does NOT mean the letter is useless — the notebook insists the augmented letter beautifies the wording and emphasises the sense.",
         "How does an augmented letter behave on the iʿrāb? It governs nothing and blocks nothing: in فَبِمَا رَحْمَةٍ the bāʾ still puts رَحْمَةٍ in jarr across the مَا, and in غَيْرِ مَا جُرْمٍ the idafa still runs across it. The iʿrāb lines here mark such a letter and let the governor reach past it; the مَا engine does the same for its augmented face.",
         "Where is إِنْ augmented? After the negating مَا (often), after the maṣdar-مَا and after لَمَّا (rarely). Where is أَنْ? After لَمَّا (فَلَمَّا أَنْ جَاءَ الْبَشِيرُ), between an oath and لَوْ, and after the kāf (كَأَنْ ظَبْيَةٍ).",
         "Where is مَا augmented? After the conditional tools إِذَا، مَتَى، أَيّ، أَيْنَ، إِنْ (أَيًّا مَا تَدْعُوا), after some jarr letters (فَبِمَا رَحْمَةٍ), and rarely between a muḍāf and its muḍāf ilayh.",
         "Where is لَا augmented? After a negation with the wāw (مَا جَاءَ زَيْدٌ وَلَا عَمْرٌو), after أَنْ (أَلَّا تَسْجُدَ — the nūn and the lām written together), before أُقْسِمُ, and — irregularly — between a muḍāf and its muḍāf ilayh.",
         "How does the reader tell an augmented لَا from a real one? Try the sentence without it: مَا مَنَعَكَ أَنْ تَسْجُدَ keeps its meaning, so that لَا was augmented; مَا قَامَ زَيْدٌ لَا عَمْرٌو changes its meaning without the لَا, so that one coordinates. The twelve-faced مَا engine applies the same removal test to مَا."],
  "tr": ["«Zâid» ne demektir? Harfi at, cümle hâlâ söylediğini söyler: مَا رَأَيْتُ زَيْدًا إِنْ'li ya da إِنْ'siz. Harfin faydasız olduğu demek DEĞİLDİR — defter zâid harfin lafzı güzelleştirdiğinde ve mânâyı te'kid ettiğinde ısrar eder.",
         "Zâid harf i'râbda nasıl davranır? Hiçbir şeyi yönetmez ve engellemez: فَبِمَا رَحْمَةٍ'de bâ, مَا'nın üzerinden رَحْمَةٍ'i yine cer eder; غَيْرِ مَا جُرْمٍ'de izâfet yine onun üzerinden yürür. Buradaki i'râb satırları böyle bir harfi işaretler ve âmilin onu aşmasına izin verir; مَا motoru zâid yüzü için aynısını yapar.",
         "إِنْ nerede zâid olur? Nâfiye مَا'dan sonra (çok), masdariye مَا'dan ve لَمَّا'dan sonra (az). أَنْ nerede? لَمَّا'dan sonra (فَلَمَّا أَنْ جَاءَ الْبَشِيرُ), kasem ile لَوْ arasında ve kâf'tan sonra (كَأَنْ ظَبْيَةٍ).",
         "مَا nerede zâid olur? Şart edatları إِذَا، مَتَى، أَيّ، أَيْنَ، إِنْ'den sonra (أَيًّا مَا تَدْعُوا), bazı cer harflerinden sonra (فَبِمَا رَحْمَةٍ) ve az olarak muzâf ile muzâfun ileyh arasında.",
         "لَا nerede zâid olur? Nefyden sonra vâv ile (مَا جَاءَ زَيْدٌ وَلَا عَمْرٌو), أَنْ'den sonra (أَلَّا تَسْجُدَ — nûn ile lâm bitişik yazılır), أُقْسِمُ'den önce ve — şâz olarak — muzâf ile muzâfun ileyh arasında.",
         "Okuyucu zâid لَا'yı gerçek olandan nasıl ayırır? Cümleyi onsuz dene: مَا مَنَعَكَ أَنْ تَسْجُدَ mânâsını korur, demek o لَا zâiddi; مَا قَامَ زَيْدٌ لَا عَمْرٌو لَا'sız mânâ değiştirir, demek o atıf eder. On iki yüzlü مَا motoru aynı çıkarma testini مَا'ya uygular."]},
 "plain": {
  "en": "Some little words are sometimes extra: take them out and the sentence means the same. They are not junk — they make the Arabic sound better and press the point. This chapter says where in, an, mā and lā are extra.",
  "tr": "Bazı küçük kelimeler bazen fazladır: çıkar, cümle aynı anlama gelir. Çöp değillerdir — Arapçayı daha güzel kılar ve vurguyu artırır. Bu bâb in, en, mâ ve lâ'nın nerede fazla olduğunu söyler."},
 "explanation": {
  "en": "The Kafiya lists seven letters that are sometimes augmented; the notebook's exposition takes four of them through their places with the received examples, five of them Qur'anic (3:159, 17:110, 12:96, 7:12, 75:1), and opens with the definition that matters for the analyzer: augmentation is a statement about the STRUCTURE — the basic meaning survives the letter's removal — not about its value. Two consequences follow and the chapter's iʿrāb lines state both: the augmented letter governs nothing, and it blocks nothing (the bāʾ reaches across مَا, the idafa across لَا). Where the mushaf writes أَلَّا the notebook separates أَنْ لَا to show the two letters; the chapter keeps the mushaf's spelling and the iʿrāb names the idgham. The remaining three letters — مِنْ in a negation, the bāʾ on the khabar of لَيْسَ and مَا, and the lām — are listed here and taught in the jarr chapters.",
  "tr": "Kâfiye bazen zâid olan yedi harfi sayar; defterin açıklaması dördünü, beşi Kur'ânî (3:159, 17:110, 12:96, 7:12, 75:1) olan alışılmış örneklerle yerlerinden geçirir ve analizör için önemli olan tarifle açar: ziyâde, değer hakkında değil YAPI hakkında bir hükümdür — aslî mânâ harfin kaldırılmasından sağ çıkar. İki sonuç çıkar ve bâbın i'râb satırları ikisini de söyler: zâid harf hiçbir şeyi yönetmez ve hiçbir şeyi engellemez (bâ مَا'nın, izâfet لَا'nın üzerinden ulaşır). Mushaf'ın أَلَّا yazdığı yerde defter iki harfi göstermek için أَنْ لَا'yı ayırır; bâb Mushaf'ın imlâsını korur ve i'râb idgamı adlandırır. Kalan üç harf — nefyde مِنْ, لَيْسَ ve مَا'nın haberindeki bâ ve lâm — burada sayılır ve cer bâblarında öğretilir."},
 "examples": [
  {"ar": "فَبِمَا رَحْمَةٍ مِنَ اللهِ لِنْتَ لَهُمْ", "en": "Augmented mā — not useless.", "tr": "Zâid mâ — faydasız değil.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "مَا إِنْ رَأَيْتُ زَيْدًا", "en": "In after the negating mā.", "tr": "Nâfiye mâ'dan sonra in.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "فَلَمَّا أَنْ جَاءَ الْبَشِيرُ — كَأَنْ ظَبْيَةٍ", "en": "An after lammā and after the kāf.", "tr": "Lemmâ'dan ve kâf'tan sonra en.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "أَيًّا مَا تَدْعُوا فَلَهُ الْأَسْمَاءُ الْحُسْنَى", "en": "Mā after a conditional tool.", "tr": "Şart edatından sonra mâ.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "مَا مَنَعَكَ أَلَّا تَسْجُدَ إِذْ أَمَرْتُكَ", "en": "Lā after an — written as one.", "tr": "En'den sonra lâ — bitişik yazılır.", "sourceStory": "al-kafiya", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«zâid harfin mânâsı yoktur»",
   "right": "«yapıya katkısı yoktur; lafza ve te'kide katkısı vardır»",
   "why": {"en": "The notebook's own warning: augmented is a structural verdict, not a value judgement.", "tr": "Defterin kendi uyarısı: zâid yapısal bir hükümdür, değer yargısı değil."}},
  {"wrong": "«فَبِمَا رَحْمَةٍ — mâ mâni oldu, rahmetin mecrur olmaması lâzım»",
   "right": "«رَحْمَةٍ bâ ile mecrurdur; zâid mâ âmili engellemez»",
   "why": {"en": "An augmented letter is transparent to government.", "tr": "Zâid harf âmile karşı şeffaftır."}},
  {"wrong": "«مَا قَامَ زَيْدٌ لَا عَمْرٌو — lâ zâid»",
   "right": "«lâ atıf harfidir; çıkarılınca mânâ değişir»",
   "why": {"en": "The removal test decides: a lā the sentence needs is not augmented.", "tr": "Çıkarma testi karar verir: cümlenin muhtaç olduğu lâ zâid değildir."}}],
 "relatedNotes": ["anwa-ma", "majaz-ziyada-nuqsan", "huruf-al-atf-fil-kafiya", "aw-imma-am-la-bal-lakin-fil-kafiya", "huruf-al-qasam-fil-kafiya"]}

ADD_EN = (" Chapter 39 (notebook line ~345): the letters of augmentation — the definition (the basic meaning survives their removal; lafẓī and maʿnawī benefit remains) and the places of in, an, mā and lā with the received examples — the notebook's exposition, kept as commentary (s1-s7). Qur'anic citations follow the mushaf: 17:110 تَدْعُوا (the notebook writes تَدْعُو) and 7:12 أَلَّا (the notebook separates أَنْ لَا to show the augmented letter).")
ADD_TR = (" Otuz dokuzuncu bâb (defter satırı ~345): ziyâde harfleri — tarif (aslî mânâ kaldırılmalarından sağ çıkar; lafzî ve mânevî fayda kalır) ve in, en, mâ ve lâ'nın yerleri alışılmış örneklerle — defterin açıklaması, şerh olarak (s1-s7). Kur'ân iktibasları Mushaf'a uyar: 17:110 تَدْعُوا (defter تَدْعُو yazar) ve 7:12 أَلَّا (defter zâid harfi göstermek için أَنْ لَا'yı ayırır).")
write_out(39, S, TITLE, ADD_EN, ADD_TR, "345", GLOSS_ADD, notes=(NOTE,),
          related=(("anwa-ma", [K]), ("majaz-ziyada-nuqsan", [K])))
report(39, S, GLOSS_ADD, (NOTE,))
