# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 25: THE DEFECTIVE VERBS (kāna and her sisters). The definition in the notebook's own Arabic; the seventeen; Sībawayh's
wider rule and why «defective»; كَانَ raising the first part and putting the second in naṣb; its uses — permanence or interruption in the past,
the sense of صَارَ, the shaʾn pronoun as its ism, the complete كَانَ meaning ثَبَتَ, the redundant كَانَ; صَارَ for transition between
qualities or between realities and as a complete verb with إِلَى; the three of the times, the مَا-verbs for continuance, مَا دَامَ for
duration, لَيْسَ for negation (present for the majority, absolute for Sībawayh); fronting the khabar before the ism, and before the verb —
permitted in the eleven from كَانَ to رَاحَ, barred in the مَا-verbs, disputed in لَيْسَ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~311-315 of the transcription.

  VERBATIM: s1. COMMENTARY (the notebook): s2-s10 — marked C_EN/C_TR.
  DIVERGENCE recorded in the manifest: the notebook prints صِنِفَانِ in the verse; the chapter cites the received صِنْفَانِ.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch25.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-afal-al-naqisa-fil-kafiya"
KN = "kana-wa-akhawatuha"
TITLE = {"ar": "الْأَفْعَالُ النَّاقِصَةُ", "en": "The defective verbs — kāna and her sisters", "tr": "Nâkıs fiiller — kâne ve kardeşleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]

def N(s): return unicodedata.normalize("NFC", s)
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
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
def jw(full): return full[0] + full[2:] if full[0] == "ا" and full[1] in "ُِ" else full
def vlist(items, last_punct=None, first_tags=("mubtada-khabar",), first_ar="خَبَرٌ — فِعْلٌ مَحْكِيٌّ."):
    out = []
    for i, it in enumerate(items):
        full, lex, en, tr = it[:4]; segs = it[4] if len(it) > 4 else None
        p = last_punct if i == len(items) - 1 else None
        if i == 0: out.append(cited(full, lex, "verb", list(first_tags) + [KN], first_ar, en, tr, punct=p, segments=segs))
        else:
            if segs: out.append(cited_wa("وَ" + jw(full), lex, "verb", [KN], full + " مَعْطُوفٌ.", en, tr, jw(full), punct=p, extra_segs=segs))
            else: out.append(cited_wa("وَ" + jw(full), lex, "verb", [KN], full + " مَعْطُوفٌ.", en, tr, jw(full), punct=p))
    return out
def MA(): return seg("مَا", "ma-nafiya", "part")
def MAV(lex, v, en, tr, tags=()):
    return [cited_wa("وَمَا", "ma-nafiya", "part", [KN], "مَا نَافِيَةٌ — الْمُرَكَّبُ مَحْكِيٌّ مَعْطُوفٌ.", "«and mā».", "«ve mâ».", "مَا"),
            cited(v, lex, "verb", [KN, "hollow-verbs"] if lex in ("zala", "dama") else [KN] + list(tags), "تَمَامُ الْمَحْكِيِّ.", en, tr)]
def KANA_V(full, ar, en, tr, punct=None, segs=None): return cited(full, "kana", "verb", [KN, "hollow-verbs"], ar, en, tr, punct=punct, segments=segs)
def ZAYD_ISM(): return cited("زَيْدٌ", "zayd", "propn", [KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«Zayd» — kāna's ism.", "«Zeyd» — kâne'nin ismi.")
def KHABAR(full, lex, en, tr, punct=None, tags=()): return cited(full, lex, "noun", [KN] + list(tags), "خَبَرُ كَانَ مَنْصُوبٌ.", en, tr, punct=punct)

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The defective verbs: what was set down to fix the doer upon a quality.",
 "tr": "Nâkıs fiiller: fâili bir sıfat üzerine karar kıldırmak için konulan fiillerdir."},
 "tokens": [
  W("الْأَفْعَالُ", "fil", "noun", ["mubtada-khabar", "jam-taksir", KN], "مُبْتَدَأٌ مَرْفُوعٌ — جَمْعُ فِعْلٍ.", "«the verbs».", "«fiiller»."),
  W("النَّاقِصَةُ", "naqis", "noun", ["naat-sifa", KN], "صِفَةٌ مَرْفُوعَةٌ.", "«defective».", "«nâkıs».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what».", "«... olan»."),
  W("وُضِعَ", "wadaa", "verb", ["ism-mawsul", "naib-al-fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةٌ.", "«was set down».", "«konulan»."),
  li_("لِتَقْرِيرِ", "taqrir", "noun", ["idafa-definiteness"], "تَقْرِيرِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«to fix».", "«karar kıldırmak için».", "تَقْرِيرِ"),
  W("الْفَاعِلِ", "fail-doer", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the doer».", "«fâili»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  W("صِفَةٍ", "sifa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a quality».", "«bir sıfat».", punct="."),
 ]})

# ----------- s2: the seventeen
S.append({"id": "s2", "translation": {
 "en": "And they are: كَانَ, صَارَ, أَصْبَحَ, أَمْسَى, أَضْحَى, ظَلَّ, بَاتَ, آضَ, عَادَ, غَدَا, رَاحَ, مَا زَالَ, مَا انْفَكَّ, مَا فَتِئَ, مَا بَرِحَ, مَا دَامَ and لَيْسَ." + C_EN,
 "tr": "Bunlar: كَانَ, صَارَ, أَصْبَحَ, أَمْسَى, أَضْحَى, ظَلَّ, بَاتَ, آضَ, عَادَ, غَدَا, رَاحَ, مَا زَالَ, مَا انْفَكَّ, مَا فَتِئَ, مَا بَرِحَ, مَا دَامَ ve لَيْسَ." + C_TR},
 "tokens": [
  atf_wa("وَهِيَ", "hiya", "pron", ["mubtada-khabar"], "هِيَ مُبْتَدَأٌ.", "«and they are».", "«ve bunlar».", "هِيَ", punct=":"),
  *vlist([("كَانَ", "kana", "«kāna».", "«kâne»."), ("صَارَ", "sara", "«ṣāra».", "«sâra»."), ("أَصْبَحَ", "asbaha", "«aṣbaḥa».", "«asbaha»."), ("أَمْسَى", "amsa", "«amsā».", "«emsâ»."),
          ("أَضْحَى", "adha-become", "«aḍḥā».", "«adhâ»."), ("ظَلَّ", "zalla-remain", "«ẓalla».", "«zalle»."), ("بَاتَ", "bata", "«bāta».", "«bâte»."), ("آضَ", "ada-become", "«āḍa».", "«âda»."),
          ("عَادَ", "ada-return", "«ʿāda».", "«âde»."), ("غَدَا", "ghada-become", "«ghadā».", "«gadâ»."),
          ("رَاحَ", "raha-become", "«rāḥa».", "«râha».")]),
  *MAV("zala", "زَالَ", "«mā zāla».", "«mâ zâle»."),
  *MAV("infakka", "انْفَكَّ", "«mā infakka».", "«mâ infekke».", tags=["form-vii-verbs", "doubled-verbs"]),
  *MAV("fatia", "فَتِئَ", "«mā fatiʾa».", "«mâ fetie»."),
  *MAV("bariha", "بَرِحَ", "«mā bariḥa».", "«mâ beriha»."),
  *MAV("dama", "دَامَ", "«mā dāma».", "«mâ dâme»."),
  cited_wa("وَلَيْسَ", "laysa", "verb", [KN], "لَيْسَ مَعْطُوفٌ — فِعْلٌ جَامِدٌ.", "«laysa».", "«leyse».", "لَيْسَ", punct="."),
 ]})
S.append({"id": "s3", "translation": {
 "en": "And for Sībawayh every verb that needs a khabar in naṣb is one of them; and they were named defective because they do not complete an utterance with their marfūʿ — so عَلِمَ اللهُ is complete while كَانَ اللهُ is defective." + C_EN,
 "tr": "Sîbeveyh'e göre mansûb bir habere muhtaç olan her fiil onlardandır; nâkıs diye adlandırıldılar çünkü merfûlarıyla kelâmı tamamlamazlar — عَلِمَ اللهُ tamdır, كَانَ اللهُ nâkıstır." + C_TR},
 "tokens": [
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ.", "«Sībawayh».", "«Sîbeveyh»."),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«every».", "«her»."),
  W("فِعْلٍ", "fil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verb».", "«fiil»."),
  W("احْتَاجَ", "ihtaja", "verb", ["naat-sifa", "fail", "form-viii-verbs", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِفَةٌ لِفِعْلٍ.", "«that needs».", "«muhtaç olan»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«a».", "«-e»."),
  W("خَبَرٍ", "khabar", "noun", ["huruf-jarr", KN], "مَجْرُورٌ.", "«khabar».", "«habere»."),
  W("مَنْصُوبٍ", "mansub", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«in naṣb».", "«mansûb».", punct="،"),
  atf_wa("وَسُمِّيَتْ", "samma", "verb", ["naib-al-fail", "form-ii-verbs"], "سُمِّيَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and they were named».", "«ve adlandırıldılar».", "سُمِّيَتْ"),
  W("نَاقِصَةً", "naqis", "noun", ["mafulayn", KN], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«defective».", "«nâkıs»."),
  W("لِأَنَّهَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because they».", "«çünkü onlar».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  W("تَتِمُّ", "tamma", "verb", ["inna-wa-akhawatuha", "fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«complete».", "«tamamlar»."),
  bi_("بِمَرْفُوعِهَا", "marfu", "noun", ["idafa-definiteness"], "مَرْفُوعِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«with their marfūʿ».", "«merfûlarıyla».", "مَرْفُوعِ", segs=[seg("بِ", "bi", "prep"), seg("مَرْفُوعِ", "marfu", "noun"), pr3fs()]),
  W("كَلَامًا", "kalam", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ، أَوْ مَفْعُولٌ بِهِ.", "«an utterance».", "«kelâm».", punct="،"),
  W("فَعَلِمَ", "alima", "verb", ["fail", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَعَلِمَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so ʿalima».", "«alime».", segments=[seg("فَ", "fa", "conj"), seg("عَلِمَ", "alima", "verb")]),
  cited("اللهُ", "allah", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ — دَاخِلَ الْمَحْكِيِّ.", "«God».", "«Allah»."),
  W("تَامٌّ", "tamm", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is complete».", "«tamdır».", punct="،"),
  atf_wa("وَكَانَ", "kana", "verb", ["mubtada-khabar", KN], "كَانَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«while kāna».", "«ve kâne».", "كَانَ"),
  cited("اللهُ", "allah", "propn", [KN], "اسْمُ كَانَ مَرْفُوعٌ — دَاخِلَ الْمَحْكِيِّ، وَالْخَبَرُ مَطْلُوبٌ.", "«God» — a khabar still owed.", "«Allah» — haber hâlâ bekleniyor."),
  W("نَاقِصٌ", "naqis", "noun", ["mubtada-khabar", KN], "خَبَرٌ مَرْفُوعٌ.", "«is defective».", "«nâkıstır».", punct="."),
 ]})

# ----------- s4: kāna's government
S.append({"id": "s4", "translation": {
 "en": "So كَانَ زَيْدٌ قَائِمًا was originally زَيْدٌ قَائِمٌ: كَانَ raised the first part and put the second in naṣb." + C_EN,
 "tr": "كَانَ زَيْدٌ قَائِمًا aslında زَيْدٌ قَائِمٌ idi: كَانَ birinci cüz'ü ref', ikinci cüz'ü nasb etti." + C_TR},
 "tokens": [
  KANA_V("فَكَانَ", "الْفَاءُ لِلتَّفْرِيعِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ — الْجُمْلَةُ الْمَحْكِيَّةُ مُبْتَدَأٌ.", "«so kāna».", "«kâne».", segs=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  ZAYD_ISM(),
  KHABAR("قَائِمًا", "qaim", "«standing».", "«ayakta»."),
  W("أَصْلُهُ", "asl", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«was originally».", "«aslında».", segments=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  cited("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "خَبَرٌ — الْجُمْلَةُ الْمَحْكِيَّةُ؛ مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — دَاخِلَ الْمَحْكِيِّ.", "«is standing».", "«ayaktadır».", punct=":"),
  W("رَفَعَتْ", "rafaa", "verb", ["fail"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«raised».", "«ref' etti»."),
  cited("كَانَ", "kana", "verb", ["fail", KN], "فِي مَحَلِّ رَفْعٍ فَاعِلٌ — الْفِعْلُ مَحْكِيٌّ.", "«kāna».", "«kâne»."),
  W("الْجُزْءَ", "juz", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the part».", "«cüz'ü»."),
  W("الْأَوَّلَ", "awwal", "noun", ["naat-sifa"], "صِفَةٌ مَنْصُوبَةٌ.", "«first».", "«birinci»."),
  atf_wa("وَنَصَبَتِ", "nasaba-nahw", "verb", ["fail"], "نَصَبَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and put … in naṣb».", "«ve nasb etti».", "نَصَبَتِ"),
  W("الثَّانِيَ", "thani", "noun", ["maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.", "«the second».", "«ikinciyi».", punct="."),
 ]})

# ----------- s5: kāna's first sense
S.append({"id": "s5", "translation": {
 "en": "And كَانَ is for the permanence of its khabar to its ism in the past, either lasting or interrupted — as كَانَ اللهُ عَلِيمًا حَكِيمًا, and كَانَ زَيْدٌ غَنِيًّا فَافْتَقَرَ." + C_EN,
 "tr": "كَانَ, haberinin ismine mâzîde sübûtu içindir — dâimî ya da munkatı olarak — كَانَ اللهُ عَلِيمًا حَكِيمًا ve كَانَ زَيْدٌ غَنِيًّا فَافْتَقَرَ gibi." + C_TR},
 "tokens": [
  atf_wa("وَكَانَ", "kana", "verb", ["mubtada-khabar", KN], "كَانَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and kāna».", "«ve kâne».", "كَانَ"),
  li_("لِثُبُوتِ", "thubut", "noun", ["mubtada-khabar", "idafa-definiteness"], "ثُبُوتِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«is for the permanence of».", "«sübûtu içindir».", "ثُبُوتِ"),
  W("خَبَرِهَا", "khabar", "noun", ["idafa-definiteness", KN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its khabar».", "«haberinin».", segments=[seg("خَبَرِ", "khabar", "noun"), pr3fs()]),
  li_("لِاسْمِهَا", "ism", "noun", ["idafa-definiteness", KN], "اسْمِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«to its ism».", "«ismine».", "اسْمِ", segs=[seg("لِ", "li", "prep"), seg("اسْمِ", "ism", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past».", "«mâzîde»."),
  W("دَائِمًا", "daim", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«lasting».", "«dâimî»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مُنْقَطِعًا", "munqati", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ مَنْصُوبٌ.", "«interrupted».", "«munkatı».", punct="،"),
  nahwu(),
  KANA_V("كَانَ", "فِعْلٌ مَاضٍ نَاقِصٌ — الثُّبُوتُ الدَّائِمُ.", "«was».", "«idi».",),
  cited("اللهُ", "allah", "propn", [KN], "اسْمُ كَانَ مَرْفُوعٌ.", "«God».", "«Allah»."),
  KHABAR("عَلِيمًا", "alim", "«all-knowing».", "«alîm».", tags=["sighat-mubalagha"]),
  cited("حَكِيمًا", "hakim", "noun", [KN], "خَبَرٌ ثَانٍ مَنْصُوبٌ.", "«all-wise».", "«hakîm».", punct="،"),
  cited_wa("وَكَانَ", "kana", "verb", [KN, "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ — الثُّبُوتُ الْمُنْقَطِعُ.", "«and was».", "«ve idi».", "كَانَ"),
  ZAYD_ISM(),
  KHABAR("غَنِيًّا", "ghani", "«rich».", "«zengin»."),
  cited("فَافْتَقَرَ", "iftaqara", "verb", ["fail", "form-viii-verbs"], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَافْتَقَرَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«then became poor».", "«sonra fakirleşti».", punct=".", segments=[seg("فَ", "fa", "conj"), seg("افْتَقَرَ", "iftaqara", "verb")]),
 ]})

# ----------- s6: the sense of صَارَ; the shaʾn pronoun
S.append({"id": "s6", "translation": {
 "en": "And it may bear the sense of صَارَ — as قَدْ كَانَتْ فِرَاخًا بُيُوضُهَا — and its ism may be the shaʾn pronoun, explained by the sentence after it — as إِذَا مِتُّ كَانَ النَّاسُ صِنْفَانِ, where النَّاسُ صِنْفَانِ is the khabar, in the place of naṣb." + C_EN,
 "tr": "صَارَ mânâsında olabilir — قَدْ كَانَتْ فِرَاخًا بُيُوضُهَا gibi — ve ismi, ardındaki cümleyle tefsir edilen şan zamiri olabilir — إِذَا مِتُّ كَانَ النَّاسُ صِنْفَانِ gibi; orada النَّاسُ صِنْفَانِ mahallen mansûb haberdir." + C_TR},
 "tokens": [
  atf_wa("وَتَكُونُ", "kana", "verb", [KN, "hollow-verbs"], "تَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ.", "«and it may be».", "«ve olabilir».", "تَكُونُ"),
  bi_("بِمَعْنَى", "mana", "noun", [KN, "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ تَكُونُ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("صَارَ", "sara", "verb", ["idafa-definiteness", KN, "hollow-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«ṣāra».", "«sâra»."),
  nahwu(),
  cited("قَدْ", "qad", "part", [], "حَرْفُ تَحْقِيقٍ.", "«indeed».", "«muhakkak»."),
  KANA_V("كَانَتْ", "فِعْلٌ مَاضٍ نَاقِصٌ بِمَعْنَى صَارَتْ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«have become».", "«oldu».", segs=[seg("كَانَ", "kana", "verb"), seg("تْ", "ta-tanith", "part")]),
  cited("فِرَاخًا", "farkh", "noun", [KN, "jam-taksir"], "خَبَرُ كَانَتْ مُقَدَّمٌ مَنْصُوبٌ — جَمْعُ فَرْخٍ.", "«chicks» — the khabar, fronted.", "«civcivler» — öne alınmış haber."),
  cited("بُيُوضُهَا", "bayda-egg", "noun", [KN, "idafa-definiteness", "jam-taksir"], "اسْمُ كَانَتْ مُؤَخَّرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ بَيْضَةٍ.", "«its eggs» — the ism, delayed.", "«yumurtaları» — sonraya bırakılmış isim.", punct="،", segments=[seg("بُيُوضُ", "bayda-egg", "noun"), pr3fs()]),
  atf_wa("وَقَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«and sometimes».", "«ve bazen».", "قَدْ"),
  W("يَكُونُ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«is».", "«olur»."),
  W("اسْمُهَا", "ism", "noun", [KN, "idafa-definiteness"], "اسْمُ يَكُونُ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its ism».", "«ismi».", segments=[seg("اسْمُ", "ism", "noun"), pr3fs()]),
  W("ضَمِيرَ", "damir", "noun", [KN, "idafa-definiteness", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "خَبَرُ يَكُونُ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the pronoun of».", "«zamiri»."),
  W("الشَّأْنِ", "shan", "noun", ["idafa-definiteness", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the matter».", "«şan»."),
  W("فَتُفَسَّرُ", "fassara", "verb", ["naib-al-fail", "al-fa-fi-khabar-al-mubtada", "form-ii-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَتُفَسَّرُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is explained».", "«ve tefsir edilir».", segments=[seg("فَ", "fa", "conj"), seg("تُفَسَّرُ", "fassara", "verb")]),
  bi_("بِالْجُمْلَةِ", "jumla", "noun", [], "الْجُمْلَةِ مَجْرُورٌ.", "«by the sentence».", "«cümleyle».", "الْجُمْلَةِ"),
  W("بَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«after it».", "«ardındaki».", punct="،", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  nahwu(),
  cited("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ.", "«when».", "«-diğimde»."),
  cited("مِتُّ", "mata-die", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — أُدْغِمَتْ تَاءُ الْفِعْلِ فِي تَاءِ الْفَاعِلِ.", "«I die».", "«öldüğümde»."),
  KANA_V("كَانَ", "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مُسْتَتِرٌ.", "«it will be [that]» — the shaʾn pronoun its ism.", "«olur [ki]» — ismi şan zamiri."),
  cited("النَّاسُ", "nas", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«people».", "«insanlar»."),
  cited("صِنْفَانِ", "sinf", "noun", ["mubtada-khabar", "al-muthanna", KN], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — وَالْجُمْلَةُ خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ.", "«are two kinds» — the clause is kāna's khabar.", "«iki sınıftır» — cümle kâne'nin haberi.", punct="،"),
  W("فَالنَّاسُ", "nas", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلتَّفْرِيعِ، وَالنَّاسُ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«so النَّاسُ».", "«o hâlde النَّاسُ».", segments=[seg("فَ", "fa", "conj"), seg("النَّاسُ", "nas", "noun")]),
  cited("صِنْفَانِ", "sinf", "noun", ["mubtada-khabar", "al-muthanna"], "تَمَامُ الْمَحْكِيِّ.", "«ṣinfāni».", "«sınfâni»."),
  W("خَبَرٌ", "khabar", "noun", ["mubtada-khabar", KN], "خَبَرٌ مَرْفُوعٌ.", "«is the khabar».", "«haberdir»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallinde»."),
  W("نَصْبٍ", "nasb", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«naṣb».", "«nasb».", punct="."),
 ]})

# ----------- s7: complete and redundant
S.append({"id": "s7", "translation": {
 "en": "And it may be complete, in the sense of ثَبَتَ — as كَانَتِ الْكَائِنَةُ, and كُنْ فَيَكُونُ — and redundant, as كَيْفَ نُكَلِّمُ مَنْ كَانَ فِي الْمَهْدِ صَبِيًّا, since its presence or absence does not alter the sense." + C_EN,
 "tr": "Tam olabilir, ثَبَتَ mânâsında — كَانَتِ الْكَائِنَةُ ve كُنْ فَيَكُونُ gibi — ve zâid olabilir, كَيْفَ نُكَلِّمُ مَنْ كَانَ فِي الْمَهْدِ صَبِيًّا gibi; çünkü varlığı yokluğu mânâyı bozmaz." + C_TR},
 "tokens": [
  atf_wa("وَتَكُونُ", "kana", "verb", [KN, "hollow-verbs"], "تَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ.", "«and it may be».", "«ve olabilir».", "تَكُونُ"),
  W("تَامَّةً", "tamm", "noun", [KN], "خَبَرُ تَكُونُ مَنْصُوبٌ.", "«complete».", "«tam»."),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("ثَبَتَ", "thabata", "verb", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«it came to be».", "«sâbit oldu».", punct="،"),
  nahwu(),
  KANA_V("كَانَتِ", "فِعْلٌ مَاضٍ تَامٌّ، وَالتَّاءُ لِلتَّأْنِيثِ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«came to pass» — a complete verb.", "«vuku buldu» — tam fiil.", segs=[seg("كَانَ", "kana", "verb"), seg("تِ", "ta-tanith", "part")]),
  cited("الْكَائِنَةُ", "kaina", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ — لَا خَبَرَ.", "«what was to be» — the doer, no khabar.", "«olacak olan» — fâil, haber yok.", punct="،"),
  cited_wa("وَكُنْ", "kana", "verb", [KN, "hollow-verbs"], "كُنْ فِعْلُ أَمْرٍ تَامٌّ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and «Be»».", "«ve «Ol»».", "كُنْ"),
  cited("فَيَكُونُ", "kana", "verb", ["fail", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and it is».", "«ve olur».", punct="،", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  atf_wa("وَزَائِدَةً", "zaid", "noun", [KN], "زَائِدَةً مَعْطُوفٌ عَلَى تَامَّةً مَنْصُوبٌ.", "«and redundant».", "«ve zâid».", "زَائِدَةً", punct="،"),
  nahwu(),
  cited("كَيْفَ", "kayfa", "noun", ["adawat-al-tasawwur", "hal"], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how».", "«nasıl»."),
  cited("نُكَلِّمُ", "kallama", "verb", ["fail", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«shall we speak to».", "«konuşuruz»."),
  cited("مَنْ", "man", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«one who».", "«... olanla»."),
  KANA_V("كَانَ", "زَائِدَةٌ لَا اسْمَ لَهَا وَلَا خَبَرَ — وَالصِّلَةُ الْجَارُّ وَالْمَجْرُورُ.", "«[was]» — redundant.", "«[idi]» — zâid."),
  cited("فِي", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِلَةُ مَنْ.", "«in».", "«-de»."),
  cited("الْمَهْدِ", "mahd-cradle", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the cradle».", "«beşikte»."),
  cited("صَبِيًّا", "sabi-boy", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«as a child».", "«çocuk olarak».", punct="،"),
  W("إِذْ", "idh", "part", ["maful-fih"], "حَرْفٌ لِلتَّعْلِيلِ.", "«since».", "«çünkü»."),
  W("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "«not».", "«-maz»."),
  W("يَتَغَيَّرُ", "taghayyara", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«alters».", "«değişir»."),
  W("الْمَعْنَى", "mana", "noun", ["fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the sense».", "«mânâ»."),
  bi_("بِوُجُودِهَا", "wujud", "noun", ["idafa-definiteness"], "وُجُودِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«by its presence».", "«varlığıyla».", "وُجُودِ", segs=[seg("بِ", "bi", "prep"), seg("وُجُودِ", "wujud", "noun"), pr3fs()]),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("عَدَمِهَا", "adam", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its absence».", "«yokluğuyla».", punct=".", segments=[seg("عَدَمِ", "adam", "noun"), pr3fs()]),
 ]})

# ----------- s8: ṣāra
S.append({"id": "s8", "translation": {
 "en": "And صَارَ is for transition — from one quality to another, as صَارَ زَيْدٌ عَالِمًا, or from one reality to another, as صَارَ الطِّينُ خَزَفًا — and it may be complete in the sense of اِنْتَقَلَ, then transitive with إِلَى, as صَارَ زَيْدٌ إِلَى بَلَدٍ." + C_EN,
 "tr": "صَارَ intikal içindir — bir sıfattan başka bir sıfata, صَارَ زَيْدٌ عَالِمًا gibi; ya da bir hakikatten başka bir hakikate, صَارَ الطِّينُ خَزَفًا gibi — ve اِنْتَقَلَ mânâsında tam olabilir; o zaman إِلَى ile müteaddî olur, صَارَ زَيْدٌ إِلَى بَلَدٍ gibi." + C_TR},
 "tokens": [
  cited_wa("وَصَارَ", "sara", "verb", ["mubtada-khabar", KN, "hollow-verbs"], "صَارَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and ṣāra».", "«ve sâra».", "صَارَ"),
  li_("لِلِانْتِقَالِ", "intiqal", "noun", ["mubtada-khabar"], "الِانْتِقَالِ مَجْرُورٌ — خَبَرٌ.", "«is for transition».", "«intikal içindir».", "الِانْتِقَالِ", segs=[seg("لِ", "li", "prep"), seg("لِانْتِقَالِ", "intiqal", "noun")]),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("صِفَةٍ", "sifa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«one quality».", "«bir sıfattan»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("صِفَةٍ", "sifa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«another».", "«başka sıfata»."),
  nahwu(),
  cited("صَارَ", "sara", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«became».", "«oldu»."),
  cited("زَيْدٌ", "zayd", "propn", [KN], "اسْمُ صَارَ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("عَالِمًا", "alim-scholar", "noun", [KN], "خَبَرُ صَارَ مَنْصُوبٌ — مِنَ الْجَهْلِ إِلَى الْعِلْمِ.", "«learned» — from ignorance to knowledge.", "«âlim» — cehaletten ilme.", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("حَقِيقَةٍ", "haqiqa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«one reality».", "«bir hakikatten»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("حَقِيقَةٍ", "haqiqa", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«another».", "«başka hakikate»."),
  nahwu(),
  cited("صَارَ", "sara", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«became».", "«oldu»."),
  cited("الطِّينُ", "tin", "noun", [KN], "اسْمُ صَارَ مَرْفُوعٌ.", "«the clay».", "«çamur»."),
  cited("خَزَفًا", "khazaf", "noun", [KN], "خَبَرُ صَارَ مَنْصُوبٌ.", "«pottery».", "«çömlek».", punct="،"),
  atf_wa("وَتَكُونُ", "kana", "verb", [KN, "hollow-verbs"], "تَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هِيَ — صَارَ.", "«and it may be».", "«ve olabilir».", "تَكُونُ"),
  W("تَامَّةً", "tamm", "noun", [KN], "خَبَرُ تَكُونُ مَنْصُوبٌ.", "«complete».", "«tam»."),
  bi_("بِمَعْنَى", "mana", "noun", ["idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("انْتَقَلَ", "intaqala", "verb", ["idafa-definiteness", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«to move».", "«intikal etti»."),
  W("فَتَتَعَدَّى", "taadda", "verb", ["fail", "al-fa-fi-khabar-al-mubtada", "form-v-verbs", "ism-maqsur-manqus"], "الْفَاءُ لِلتَّفْرِيعِ، وَتَتَعَدَّى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«then it is transitive».", "«o zaman müteaddî olur».", segments=[seg("فَ", "fa", "conj"), seg("تَتَعَدَّى", "taadda", "verb")]),
  bi_("بِإِلَى", "ila", "prep", [], "إِلَى فِي مَحَلِّ جَرٍّ — الْحَرْفُ مَحْكِيٌّ.", "«with ilā».", "«ilâ ile».", "إِلَى", punct="،"),
  nahwu(),
  cited("صَارَ", "sara", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ.", "«went».", "«gitti»."),
  cited("زَيْدٌ", "zayd", "propn", ["fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  cited("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  cited("بَلَدٍ", "balad", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«a town».", "«bir beldeye».", punct="."),
 ]})

# ----------- s9: the rest of the sisters
S.append({"id": "s9", "translation": {
 "en": "And أَصْبَحَ, أَمْسَى and أَضْحَى bring the sentence's sense close to their own times, and may bear the sense of صَارَ; مَا زَالَ and her sisters are for continuance, مَا دَامَ for a span; and لَيْسَ is for negation in the present for the majority, and absolutely for Sībawayh." + C_EN,
 "tr": "أَصْبَحَ, أَمْسَى ve أَضْحَى cümlenin mânâsını kendi vakitlerine yaklaştırır ve صَارَ mânâsında olabilir; مَا زَالَ ve kardeşleri devam içindir, مَا دَامَ bir süre içindir; لَيْسَ cumhûra göre hâlde nefy, Sîbeveyh'e göre mutlak nefy içindir." + C_TR},
 "tokens": [
  cited_wa("وَأَصْبَحَ", "asbaha", "verb", ["mubtada-khabar", KN, "form-iv-verbs"], "أَصْبَحَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and aṣbaḥa».", "«ve asbaha».", "أَصْبَحَ"),
  cited_wa("وَأَمْسَى", "amsa", "verb", [KN, "form-iv-verbs"], "أَمْسَى مَعْطُوفٌ.", "«amsā».", "«emsâ».", "أَمْسَى"),
  cited_wa("وَأَضْحَى", "adha-become", "verb", [KN, "form-iv-verbs"], "أَضْحَى مَعْطُوفٌ.", "«and aḍḥā».", "«ve adhâ».", "أَضْحَى"),
  li_("لِتَقْرِيبِ", "taqrib", "noun", ["mubtada-khabar", "idafa-definiteness"], "تَقْرِيبِ مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرٌ.", "«bring … close».", "«yaklaştırmak içindir».", "تَقْرِيبِ"),
  W("مَعْنَى", "mana", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ.", "«the sense of».", "«mânâsını»."),
  W("الْجُمْلَةِ", "jumla", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the sentence».", "«cümlenin»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("أَوْقَاتِهَا", "waqt", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ وَقْتٍ: الصَّبَاحُ وَالْمَسَاءُ وَالضُّحَى.", "«their own times» — morning, evening, forenoon.", "«kendi vakitlerine» — sabah, akşam, kuşluk.", punct="،", segments=[seg("أَوْقَاتِ", "waqt", "noun"), pr3fs()]),
  atf_wa("وَقَدْ", "qad", "part", [], "قَدْ لِلتَّقْلِيلِ.", "«and may».", "«ve bazen».", "قَدْ"),
  W("تَكُونُ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ.", "«be».", "«olur»."),
  bi_("بِمَعْنَى", "mana", "noun", [KN, "idafa-definiteness"], "مَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ — خَبَرُ تَكُونُ.", "«in the sense of».", "«mânâsında».", "مَعْنَى"),
  cited("صَارَ", "sara", "verb", ["idafa-definiteness", KN, "hollow-verbs"], "مُضَافٌ إِلَيْهِ — فِعْلٌ مَحْكِيٌّ.", "«ṣāra».", "«sâra».", punct="؛"),
  cited_wa("وَمَا", "ma-nafiya", "part", ["mubtada-khabar", KN], "مَا نَافِيَةٌ — الْمُرَكَّبُ مَحْكِيٌّ مُبْتَدَأٌ.", "«and mā».", "«ve mâ».", "مَا"),
  cited("زَالَ", "zala", "verb", [KN, "hollow-verbs"], "تَمَامُ الْمَحْكِيِّ.", "«zāla».", "«zâle»."),
  atf_wa("وَأَخَوَاتُهَا", "ukht", "noun", ["idafa-definiteness", "jam-taksir", KN], "أَخَوَاتُ مَعْطُوفٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ أُخْتٍ.", "«and her sisters».", "«ve kardeşleri».", "أَخَوَاتُ", extra_segs=[seg("أَخَوَاتُ", "ukht", "noun"), pr3fs()]),
  li_("لِلِاسْتِمْرَارِ", "istimrar", "noun", ["mubtada-khabar"], "الِاسْتِمْرَارِ مَجْرُورٌ — خَبَرٌ.", "«are for continuance».", "«devam içindir».", "الِاسْتِمْرَارِ", punct="،", segs=[seg("لِ", "li", "prep"), seg("لِاسْتِمْرَارِ", "istimrar", "noun")]),
  cited_wa("وَمَا", "ma-masdariyya", "part", ["mubtada-khabar", KN], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ — الْمُرَكَّبُ مَحْكِيٌّ مُبْتَدَأٌ.", "«and mā».", "«ve mâ».", "مَا"),
  cited("دَامَ", "dama", "verb", [KN, "hollow-verbs"], "تَمَامُ الْمَحْكِيِّ.", "«dāma».", "«dâme»."),
  li_("لِلتَّوْقِيتِ", "tawqit", "noun", ["mubtada-khabar"], "التَّوْقِيتِ مَجْرُورٌ — خَبَرٌ.", "«is for a span».", "«süre bildirmek içindir».", "التَّوْقِيتِ", punct="؛", segs=[seg("لِ", "li", "prep"), seg("لتَّوْقِيتِ", "tawqit", "noun")]),
  cited_wa("وَلَيْسَ", "laysa", "verb", ["mubtada-khabar", KN], "لَيْسَ لَفْظٌ مَحْكِيٌّ مُبْتَدَأٌ.", "«and laysa».", "«ve leyse».", "لَيْسَ"),
  li_("لِلنَّفْيِ", "nafy", "noun", ["mubtada-khabar"], "النَّفْيِ مَجْرُورٌ — خَبَرٌ.", "«is for negation».", "«nefy içindir».", "النَّفْيِ", segs=[seg("لِ", "li", "prep"), seg("لنَّفْيِ", "nafy", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْحَالِ", "hal-state", "noun", ["huruf-jarr"], "مَجْرُورٌ.", "«the present».", "«hâlde»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْجُمْهُورِ", "jumhur", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the majority».", "«cumhûra»."),
  atf_wa("وَمُطْلَقًا", "mutlaqan", "noun", ["hal"], "مُطْلَقًا مَعْطُوفٌ مَنْصُوبٌ.", "«and absolutely».", "«ve mutlak olarak».", "مُطْلَقًا"),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness", "al-mabni-wal-mudmar"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ.", "«Sībawayh».", "«Sîbeveyh'e».", punct="."),
 ]})

# ----------- s10: fronting
S.append({"id": "s10", "translation": {
 "en": "And their khabars may precede their isms when nothing prevents it — as لَيْسَ قَائِمًا زَيْدٌ; as for preceding the verbs themselves, it is permitted in the eleven from كَانَ to رَاحَ, barred in those that open with مَا, and disputed in لَيْسَ." + C_EN,
 "tr": "Bir mâni olmadığında haberleri isimlerinin önüne geçebilir — لَيْسَ قَائِمًا زَيْدٌ gibi; fiillerin kendilerinin önüne geçmeye gelince, كَانَ'den رَاحَ'ya kadar on birinde câiz, başında مَا olanlarda mümteni', لَيْسَ'de ihtilâflıdır." + C_TR},
 "tokens": [
  atf_wa("وَيَجُوزُ", "jaaza", "verb", ["fail", "hollow-verbs"], "يَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and it is permitted».", "«ve câizdir».", "يَجُوزُ"),
  W("تَقْدِيمُ", "taqdim", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«that … precede».", "«öne geçmesi»."),
  W("أَخْبَارِهَا", "khabar", "noun", ["idafa-definiteness", "jam-taksir", KN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ خَبَرٍ.", "«their khabars».", "«haberlerinin».", segments=[seg("أَخْبَارِ", "khabar", "noun"), pr3fs()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«before».", "«önüne»."),
  W("أَسْمَائِهَا", "ism", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", KN], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ اسْمٍ.", "«their isms».", "«isimlerinin».", segments=[seg("أَسْمَائِ", "ism", "noun"), pr3fs()]),
  W("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-dığında»."),
  W("لَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-ma-»."),
  W("يَمْنَعْ", "manaa", "verb", ["nawasib-wa-jawazim-al-mudari", "fail"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ.", "«prevents».", "«mâni olmadığında»."),
  W("مَانِعٌ", "mani-preventer", "noun", ["fail", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ.", "«anything».", "«bir mâni».", punct="،"),
  nahwu(),
  cited("لَيْسَ", "laysa", "verb", [KN], "فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ.", "«is not».", "«değildir»."),
  cited("قَائِمًا", "qaim", "noun", [KN], "خَبَرُ لَيْسَ مُقَدَّمٌ مَنْصُوبٌ.", "«standing» — the khabar, fronted.", "«ayakta» — öne alınmış haber."),
  cited("زَيْدٌ", "zayd", "propn", [KN], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ.", "«Zayd» — the ism, delayed.", "«Zeyd» — sonraya bırakılmış isim.", punct="؛"),
  atf_wa("وَأَمَّا", "amma-tafsil", "part", ["amma-tafsiliyya"], "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for».", "«... gelince».", "أَمَّا"),
  W("تَقْدِيمُهَا", "taqdim", "noun", ["mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ — الْأَخْبَارُ.", "«their preceding».", "«öne geçmeleri».", segments=[seg("تَقْدِيمُ", "taqdim", "noun"), pr3fs()]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«before».", "«önüne»."),
  W("الْأَفْعَالِ", "fil", "noun", ["huruf-jarr", "jam-taksir"], "مَجْرُورٌ.", "«the verbs».", "«fiillerin»."),
  W("أَنْفُسِهَا", "nafs", "noun", ["tawkid", "idafa-definiteness", "jam-taksir"], "تَوْكِيدٌ مَعْنَوِيٌّ مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«themselves».", "«kendilerinin».", segments=[seg("أَنْفُسِ", "nafs", "noun"), pr3fs()]),
  W("فَجَائِزٌ", "jaiz", "noun", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَجَائِزٌ خَبَرٌ مَرْفُوعٌ.", "«is permitted».", "«câizdir».", segments=[seg("فَ", "fa", "conj"), seg("جَائِزٌ", "jaiz", "noun")]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْأَحَدَ", "ahad", "noun", ["huruf-jarr", "asma-al-adad-fil-kafiya"], "مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ جَرٍّ.", "«the eleven».", "«on birinde»."),
  W("عَشَرَ", "ashar", "noun", ["asma-al-adad-fil-kafiya"], "الْجُزْءُ الثَّانِي مِنَ الْمُرَكَّبِ.", "— the second part.", "— ikinci cüz."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  cited("كَانَ", "kana", "verb", ["huruf-jarr", KN], "فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«kāna».", "«kâne»."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  cited("رَاحَ", "raha-become", "verb", ["huruf-jarr", KN], "فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«rāḥa».", "«râha».", punct="،"),
  atf_wa("وَمُمْتَنِعٌ", "mumtani", "noun", ["mubtada-khabar", "ism-fail"], "مُمْتَنِعٌ مَعْطُوفٌ عَلَى جَائِزٌ مَرْفُوعٌ.", "«barred».", "«mümteni'».", "مُمْتَنِعٌ"),
  W("فِيمَا", "fi", "prep", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in those».", "«... olanlarda».", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("فِي", "fi", "prep", ["huruf-jarr", "ism-mawsul"], "حَرْفُ جَرٍّ — خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«in».", "«-de»."),
  W("أَوَّلِهِ", "awwal", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«whose beginning».", "«başında».", segments=[seg("أَوَّلِ", "awwal", "noun"), pr3msi()]),
  cited("مَا", "ma-nafiya", "part", ["mubtada-khabar", "ism-mawsul"], "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ — الْحَرْفُ مَحْكِيٌّ.", "«mā».", "«mâ».", punct="،"),
  atf_wa("وَمُخْتَلَفٌ", "mukhtalaf", "noun", ["mubtada-khabar", "ism-maful"], "مُخْتَلَفٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and disputed».", "«ve ihtilâflı».", "مُخْتَلَفٌ"),
  W("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — نَائِبُ فَاعِلٍ.", "«about».", "«-dır»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  cited("لَيْسَ", "laysa", "verb", ["huruf-jarr", KN], "فِي مَحَلِّ جَرٍّ — الْفِعْلُ مَحْكِيٌّ.", "«laysa».", "«leyse».", punct="."),
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
 "iftaqara": need("iftaqara", "اِفْتَقَرَ", "ف ق ر", "verb", "to become poor (Form VIII)", "fakirleşmek (VIII. bâb)", 4),
 "farkh": need("farkh", "فَرْخ", "ف ر خ", "noun", "a chick; plural فِرَاخ", "civciv, yavru kuş; cem'i فِرَاخ", 3),
 "bayda-egg": need("bayda-egg", "بَيْضَة", "ب ي ض", "noun", "an egg; plural بُيُوض", "yumurta; cem'i بُيُوض", 2),
 "kaina": need("kaina", "كَائِنَة", "ك و ن", "noun", "what comes to pass, an event — the feminine ism fāʿil of the complete كَانَ", "vuku bulan şey, hadise — tam كَانَ'nin müennes ism-i fâili", 5),
 "khazaf": need("khazaf", "خَزَف", "خ ز ف", "noun", "pottery, earthenware", "çömlek, pişmiş toprak", 4),
 "taqrib": need("taqrib", "تَقْرِيب", "ق ر ب", "noun", "bringing near — the maṣdar of قَرَّبَ", "yaklaştırma — karrabe'nin masdarı", 4),
 "ukht": need("ukht", "أُخْت", "أ خ و", "noun", "a sister; plural أَخَوَات — the grammarians' word for a particle's or verb's family", "kız kardeş; cem'i أَخَوَات — nahivcilerin bir edat ya da fiil ailesi için sözü", 2),
 "istimrar": need("istimrar", "اِسْتِمْرَار", "م ر ر", "noun", "continuance — the sense of مَا زَالَ and her sisters", "devam, süreklilik — مَا زَالَ ve kardeşlerinin mânâsı", 4),
 "tawqit": need("tawqit", "تَوْقِيت", "و ق ت", "noun", "fixing a span — the sense of مَا دَامَ", "süre belirleme — مَا دَامَ'nin mânâsı", 4),
 "mumtani": need("mumtani", "مُمْتَنِع", "م ن ع", "noun", "barred, impossible (of a construction)", "mümteni', imkânsız (bir yapı için)", 4),
 "mukhtalaf": need("mukhtalaf", "مُخْتَلَف", "خ ل ف", "noun", "disputed — مُخْتَلَفٌ فِيهِ, «differed about»", "ihtilâflı — مُخْتَلَفٌ فِيهِ, «hakkında ihtilâf edilen»", 4),
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
put_morph(mo, "iftaqara", _nfc(_sg.derived(_sg.B8, _sg.W8, "َ", "اِفْتَقَر", "فْتَقِر", "اِفْتَقِر", "اِفْتِقَار", "مُفْتَقِر", "مُفْتَقَر", "اُفْتُقِرَ", "يُفْتَقَرُ", "اِفْتَقَرَ يَفْتَقِرُ افْتِقَارًا: صَارَ فَقِيرًا — بَابُ الِافْتِعَالِ، لَازِمٌ.")))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch25 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْأَفْعَالُ النَّاقِصَةُ فِي الْكَافِيَةِ", "en": "Kāna and her sisters in the Kafiya: the definition, the seventeen, why «defective», كَانَ's five faces, صَارَ's transition, the sisters' senses, and the fronting rules in three groups", "tr": "Kâfiye'de kâne ve kardeşleri: tarif, on yedi, neden «nâkıs», كَانَ'nin beş yüzü, صَارَ'nin intikali, kardeşlerin mânâları ve üç gruptaki takdim kuralları"},
 "level": 4, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الأفعال الناقصة: ما وضع لتقرير الفاعل على صفة؛ كان وصار وأصبح وأمسى وأضحى وظل وبات وآض وعاد وغدا وراح وما زال وما انفك وما فتئ وما برح وما دام وليس", "ضياء صونغور اوغلى — دفتر الكافية: مذهب سيبويه؛ وجه التسمية؛ كان الدائمة والمنقطعة، كان بمعنى صار، ضمير الشأن، التامة، الزائدة؛ صار من صفة إلى صفة ومن حقيقة إلى حقيقة؛ أصبح وأمسى وأضحى؛ ما زال للاستمرار وما دام للتوقيت؛ ليس بين الجمهور وسيبويه؛ تقديم الخبر على الاسم وعلى الفعل في الأقسام الثلاثة"],
 "question": {
  "en": ["What is a DEFECTIVE verb? One set down to fix its doer upon a quality — not to report an act. كَانَ زَيْدٌ قَائِمًا does not say Zayd did anything; it fixes «standing» on him in the past. The Kafiya counts seventeen; Sībawayh admits any verb that needs a khabar in naṣb.",
         "Why «defective»? Because the verb and its marfūʿ do not make an utterance: عَلِمَ اللهُ is a sentence, كَانَ اللهُ is not — the khabar is still owed. That is exactly the «expectation» the analyzer pushes when it meets a sister of كَانَ.",
         "What does كَانَ do, and what can it mean? It takes a nominal sentence and raises its first part as ism, puts the second in naṣb as khabar. Its senses: permanence in the past, lasting (كَانَ اللهُ عَلِيمًا) or interrupted (كَانَ زَيْدٌ غَنِيًّا فَافْتَقَرَ); the sense of صَارَ (قَدْ كَانَتْ فِرَاخًا بُيُوضُهَا); with the shaʾn pronoun as its ism and a whole sentence as its khabar; complete, meaning ثَبَتَ (كَانَتِ الْكَائِنَةُ، كُنْ فَيَكُونُ); and redundant (مَنْ كَانَ فِي الْمَهْدِ صَبِيًّا).",
         "What is صَارَ? Transition — from quality to quality (صَارَ زَيْدٌ عَالِمًا) or from one reality to another (صَارَ الطِّينُ خَزَفًا); complete when it means «move», and then it takes إِلَى (صَارَ زَيْدٌ إِلَى بَلَدٍ).",
         "And the others? أَصْبَحَ، أَمْسَى، أَضْحَى tie the sentence to morning, evening, forenoon, and may mean صَارَ; ظَلَّ and بَاتَ to day and night; آضَ، عَادَ، غَدَا، رَاحَ mean صَارَ; مَا زَالَ and her sisters say the state continues; مَا دَامَ gives it a span; لَيْسَ negates — in the present for most, absolutely for Sībawayh.",
         "May the khabar come first? Before the ism, yes, unless something prevents it (لَيْسَ قَائِمًا زَيْدٌ). Before the verb itself: permitted for the eleven from كَانَ to رَاحَ, barred for the five that begin with مَا (a negation must open its clause), and disputed for لَيْسَ — the Kufans and al-Mubarrad say no, the Basrans and Sībawayh say yes.",
         "What does the engine do? The kernel's KANA table pushes [ism-raf, khabar-naṣb] at every sister; the TartibEngine's order ledger records whether a fronted khabar is lawful by this three-way rule; the jāmid flag on لَيْسَ keeps the paradigm honest."],
  "tr": ["NÂKIS fiil nedir? Fâilini bir sıfat üzerine karar kıldırmak için konulan fiil — bir iş bildirmek için değil. كَانَ زَيْدٌ قَائِمًا Zeyd'in bir şey yaptığını söylemez; «ayakta»yı mâzîde ona sabitler. Kâfiye on yedi sayar; Sîbeveyh mansûb habere muhtaç her fiili kabul eder.",
         "Neden «nâkıs»? Çünkü fiil ile merfûu bir kelâm oluşturmaz: عَلِمَ اللهُ bir cümledir, كَانَ اللهُ değildir — haber hâlâ bekleniyor. Analizörün كَانَ'nin bir kardeşiyle karşılaşınca ittiği «beklenti» tam budur.",
         "كَانَ ne yapar, ne anlama gelebilir? Bir isim cümlesini alıp birinci cüz'ünü isim olarak ref', ikincisini haber olarak nasb eder. Mânâları: mâzîde sübût, dâimî (كَانَ اللهُ عَلِيمًا) ya da munkatı (كَانَ زَيْدٌ غَنِيًّا فَافْتَقَرَ); صَارَ mânâsı (قَدْ كَانَتْ فِرَاخًا بُيُوضُهَا); ismi şan zamiri, haberi bütün bir cümle; tam, ثَبَتَ mânâsında (كَانَتِ الْكَائِنَةُ، كُنْ فَيَكُونُ); ve zâid (مَنْ كَانَ فِي الْمَهْدِ صَبِيًّا).",
         "صَارَ nedir? İntikal — sıfattan sıfata (صَارَ زَيْدٌ عَالِمًا) ya da bir hakikatten başkasına (صَارَ الطِّينُ خَزَفًا); «gitmek» anlamında tam olur ve o zaman إِلَى alır (صَارَ زَيْدٌ إِلَى بَلَدٍ).",
         "Ya ötekiler? أَصْبَحَ، أَمْسَى، أَضْحَى cümleyi sabaha, akşama, kuşluğa bağlar ve صَارَ anlamına gelebilir; ظَلَّ ve بَاتَ gündüz ve geceye; آضَ، عَادَ، غَدَا، رَاحَ صَارَ demektir; مَا زَالَ ve kardeşleri hâlin sürdüğünü söyler; مَا دَامَ ona bir süre verir; لَيْسَ nefy eder — çoğunluğa göre hâlde, Sîbeveyh'e göre mutlak.",
         "Haber önce gelebilir mi? İsmin önüne, evet, bir mâni yoksa (لَيْسَ قَائِمًا زَيْدٌ). Fiilin kendisinin önüne: كَانَ'den رَاحَ'ya on bir için câiz, مَا ile başlayan beşi için mümteni' (nefy cümlesini açmalıdır), لَيْسَ için ihtilâflı — Kûfeliler ve Müberred hayır, Basralılar ve Sîbeveyh evet der.",
         "Motor ne yapar? Çekirdeğin KANA tablosu her kardeşte [ism-ref', haber-nasb] iter; TartibEngine'in sıra defteri öne alınmış bir haberin bu üçlü kuralla câiz olup olmadığını kaydeder; لَيْسَ üzerindeki câmid bayrağı çekimi dürüst tutar."]},
 "plain": {
  "en": "Kāna and her sisters are verbs that do not describe an act but fix a state on their subject: كَانَ «was», صَارَ «became», لَيْسَ «is not», مَا زَالَ «still is». They take a plain sentence and keep its subject in rafʿ while putting its predicate in naṣb. كَانَ alone has five uses, from «was» to a word that adds nothing.",
  "tr": "Kâne ve kardeşleri bir işi değil özneye bir hâli sabitleyen fiillerdir: كَانَ «idi», صَارَ «oldu», لَيْسَ «değildir», مَا زَالَ «hâlâ». Düz bir cümleyi alır, öznesini ref'te tutup yüklemini nasb ederler. Tek başına كَانَ'nin «idi»den hiçbir şey katmayan bir kelimeye kadar beş kullanımı vardır."},
 "explanation": {
  "en": "The definition is the Kafiya's and the list is the madrasah's: seventeen verbs whose work is not to report an action but to settle a quality on a subject, which is why their «doer» is called an ism and their complement a khabar — the parts of the nominal sentence they entered. The notebook's remark on the name is the key to the whole class: كَانَ with its marfūʿ is not yet a sentence, so a khabar is owed, and every rule in the chapter is about that owed khabar. كَانَ is treated first and at length because it has five faces: the plain past, lasting or interrupted; the sense of «became»; the construction in which its ism is the pronoun of the matter and its khabar an entire clause, which the notebook illustrates with a verse; the complete كَانَ that means «came to pass» and takes a doer like any verb; and the redundant كَانَ of the Qurʾānic cradle, whose removal changes nothing. صَارَ follows with its two transitions and its complete sense with إِلَى. The remaining sisters are given by what they add — a time of day, continuance, a span, negation — and the notebook records the one doctrinal split on لَيْسَ. The chapter ends with the order rules, which are the TartibEngine's material: a khabar may stand before its ism unless something bars it, and before the verb only in the first eleven; the مَا-verbs refuse it because the negation must open the clause, and لَيْسَ divides the schools along the line of whether it is a verb at all. The verse's صِنِفَانِ in the notebook is cited in the received form صِنْفَانِ, and the manifest says so.",
  "tr": "Tarif Kâfiye'nin, liste medresenindir: işi bir eylemi bildirmek değil bir niteliği özneye yerleştirmek olan on yedi fiil; «fâil»lerine isim, tamamlayıcılarına haber denmesinin sebebi budur — girdikleri isim cümlesinin parçaları. Defterin ad üzerine notu bütün sınıfın anahtarıdır: كَانَ merfûuyla henüz cümle değildir, dolayısıyla bir haber beklenir ve bâbdaki her kural o beklenen haber hakkındadır. كَانَ önce ve uzun ele alınır, çünkü beş yüzü vardır: düz mâzî, dâimî ya da munkatı; «oldu» anlamı; isminin şan zamiri, haberinin bütün bir cümle olduğu yapı — defter bunu bir beyitle örnekler; «vuku buldu» anlamına gelip her fiil gibi fâil alan tam كَانَ; ve kaldırılması hiçbir şeyi değiştirmeyen Kur'ânî beşik âyetindeki zâid كَانَ. صَارَ iki intikali ve إِلَى ile tam anlamıyla izler. Kalan kardeşler ekledikleriyle verilir — günün bir vakti, devam, süre, nefy — ve defter لَيْسَ üzerindeki tek doktriner ayrılığı kaydeder. Bâb TartibEngine'in malzemesi olan sıra kurallarıyla biter: haber bir mâni yoksa isminin önünde, fiilin önünde ise yalnız ilk on birde durabilir; مَا-fiilleri reddeder, çünkü nefy cümleyi açmalıdır; لَيْسَ ise mektepleri onun bir fiil olup olmadığı çizgisinde böler. Defterdeki beyitte geçen صِنِفَانِ alınan biçim صِنْفَانِ ile zikredilir ve manifest bunu söyler."},
 "examples": [
  {"ar": "الْأَفْعَالُ النَّاقِصَةُ: مَا وُضِعَ لِتَقْرِيرِ الْفَاعِلِ عَلَى صِفَةٍ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "عَلِمَ اللهُ تَامٌّ، وَكَانَ اللهُ نَاقِصٌ", "en": "Why «defective».", "tr": "Neden «nâkıs».", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "كَانَ اللهُ عَلِيمًا حَكِيمًا — كَانَ زَيْدٌ غَنِيًّا فَافْتَقَرَ", "en": "Lasting and interrupted.", "tr": "Dâimî ve munkatı.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "إِذَا مِتُّ كَانَ النَّاسُ صِنْفَانِ", "en": "The shaʾn pronoun as kāna's ism.", "tr": "Kâne'nin ismi olarak şan zamiri.", "sourceStory": "al-kafiya", "sentence": "s6"},
  {"ar": "كَانَتِ الْكَائِنَةُ — كُنْ فَيَكُونُ — مَنْ كَانَ فِي الْمَهْدِ صَبِيًّا", "en": "Complete and redundant.", "tr": "Tam ve zâid.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "صَارَ الطِّينُ خَزَفًا — صَارَ زَيْدٌ إِلَى بَلَدٍ", "en": "ṣāra's transition and its complete sense.", "tr": "Sâra'nın intikali ve tam anlamı.", "sourceStory": "al-kafiya", "sentence": "s8"},
  {"ar": "لَيْسَ قَائِمًا زَيْدٌ", "en": "The khabar before the ism.", "tr": "Haber ismin önünde.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«كَانَ زَيْدٌ قَائِمٌ»",
   "right": "«كَانَ زَيْدٌ قَائِمًا — kâne ikinci cüz'ü nasb eder»",
   "why": {"en": "The predicate of the nominal sentence becomes kāna's khabar in naṣb.", "tr": "İsim cümlesinin yüklemi kâne'nin mansûb haberi olur."}},
  {"wrong": "«كَانَتِ الْكَائِنَةُ — haberi mahzûf»",
   "right": "«كَانَتِ الْكَائِنَةُ — tam kâne, ثَبَتَ mânâsında; الْكَائِنَةُ fâildir, haber yoktur»",
   "why": {"en": "The complete كَانَ is an ordinary verb with a doer; nothing is owed.", "tr": "Tam كَانَ fâili olan sıradan bir fiildir; beklenen bir şey yoktur."}},
  {"wrong": "«قَائِمًا مَا زَالَ زَيْدٌ»",
   "right": "«مَا زَالَ زَيْدٌ قَائِمًا — مَا ile başlayanların haberi fiilin önüne geçemez»",
   "why": {"en": "The negation must open its clause; only the eleven from كَانَ to رَاحَ allow the khabar before the verb.", "tr": "Nefy cümlesini açmalıdır; haberin fiilin önüne geçmesine yalnız كَانَ'den رَاحَ'ya on bir izin verir."}},
  {"wrong": "«لَيْسَ زَيْدٌ قَائِمًا — Zeyd hiçbir zaman ayakta olmadı»",
   "right": "«cumhûra göre: Zeyd şu an ayakta değil; mutlak nefy yalnız Sîbeveyh'in görüşüdür»",
   "why": {"en": "The notebook keeps both readings and names their holders.", "tr": "Defter iki okuyuşu da tutar ve sahiplerini adlandırır."}}],
 "relatedNotes": [KN, "al-mubtada-wa-nawah", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan", "al-mutaaddi-wa-afal-al-qulub-fil-kafiya", "al-fil-wal-madi-wal-mudari-fil-kafiya"]}

ADD_EN = (" Chapter 25 (notebook lines ~311-315): the defective verbs defined in the notebook's own Arabic (s1); the seventeen, Sībawayh's rule and the name, كَانَ's government and its five uses, صَارَ, the sisters' senses and the three fronting groups — the notebook's exposition, kept as commentary (s2-s10). "
          "DIVERGENCE: the notebook prints the verse's صِنِفَانِ; the chapter cites the received صِنْفَانِ.")
ADD_TR = (" Yirmi beşinci bâb (defter satırları ~311-315): nâkıs fiiller defterin kendi Arapçasıyla tarif edilir (s1); on yedi, Sîbeveyh'in kuralı ve ad, كَانَ'nin ameli ve beş kullanımı, صَارَ, kardeşlerin mânâları ve üç takdim grubu — defterin açıklaması, şerh olarak (s2-s10). "
          "FARK: defter beyitte صِنِفَانِ basar; bâb alınan صِنْفَانِ'yi zikreder.")
write_out(25, S, TITLE, ADD_EN, ADD_TR, "311-315", GLOSS_ADD, notes=(NOTE,),
          related=((KN, [K]), ("al-mubtada-wa-nawah", [K])))
report(25, S, GLOSS_ADD, (NOTE,))
