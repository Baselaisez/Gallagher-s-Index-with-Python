# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 12: THE DUAL. Defined in the notebook's own Arabic; the maqsur's alif turned to waw when it is a third letter
standing for a waw (عَصَوَانِ) and to ya otherwise (رَحَيَانِ، أَعْلَيَانِ); the mamdud's hamza kept when original (قُرَّاءَانِ), turned to waw
when it marks the feminine (حَمْرَاوَانِ), either way where it stands for a radical (كِسَاءَانِ / كِسَاوَانِ); the nun dropped in annexation
(الضَّارِبَا زَيْدٍ); the irregular خُصْيَانِ and أَلْيَانِ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~219-222 of the transcription.

  VERBATIM from the notebook's Arabic: s1 (the definition) and every example.
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s2, s3, s4, s5, s6, s7.
  COMMENTARY (the notebook's explanation): s8 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch12.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-muthanna-fil-kafiya"
MT = "al-muthanna"
TITLE = {"ar": "الْمُثَنَّى", "en": "The dual", "tr": "Tesniye"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
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
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=[seg("كَ", "ka", "prep"), seg(inner, lex, pos)])

# ----------- s1 (VERBATIM)
S.append({"id": "s1", "translation": {
 "en": "The dual: what has joined to its end an alif, or a yāʾ with a fatḥa before it, and a nūn with a kasra, to show that with it is another like it of its kind.",
 "tr": "Tesniye: kendisiyle birlikte cinsinden bir benzeri daha bulunduğuna delâlet etsin diye, sonuna bir elif ya da mâkabli meftûh bir yâ ile meksûr bir nûn bitişendir."},
 "tokens": [
  W("الْمُثَنَّى", "muthanna", "noun", ["mubtada-khabar", MT, "ism-maqsur-manqus"], "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the dual» — the mubtada.", "«tesniye» — mübtedâ.", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("لَحِقَ", "lahiqa", "verb", ["ism-mawsul", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةٌ.", "«has joined».", "«bitişen»."),
  W("آخِرَهُ", "akhir", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — الْعَائِدُ.", "«its end» — the object; the hāʾ the ʿāʾid.", "«sonuna» — mef'ûl; hâ âid.", segments=[seg("آخِرَ", "akhir", "noun"), pr3ms()]),
  W("أَلِفٌ", "alif-letter", "noun", ["fail", MT], "فَاعِلٌ مَرْفُوعٌ — فِي الرَّفْعِ.", "«an alif» — the doer; in rafʿ.", "«bir elif» — fâil; ref'de."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("يَاءٌ", "ya-letter", "noun", ["atf-nasaq", MT], "مَعْطُوفٌ مَرْفُوعٌ — فِي النَّصْبِ وَالْجَرِّ.", "«a yāʾ» — in naṣb and jarr.", "«bir yâ» — nasb ve cerde."),
  W("مَفْتُوحٌ", "maftuh", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ لِيَاءٌ مَرْفُوعَةٌ — صِفَةٌ سَبَبِيَّةٌ.", "«with a fatḥa» — a causal adjective.", "«meftûh» — sebebî sıfat."),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلُ مَفْتُوحٌ.", "«what» — the adjective's doer.", "«... olan» — sıfatın fâili."),
  W("قَبْلَهَا", "qabla", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is before it» — the ṣila.", "«ondan önce» — sıla.", segments=[seg("قَبْلَ", "qabla", "noun"), pr3fs()]),
  atf_wa("وَنُونٌ", "nun-letter", "noun", [MT], "نُونٌ مَعْطُوفٌ عَلَى أَلِفٌ.", "«and a nūn».", "«ve bir nûn».", "نُونٌ"),
  W("مَكْسُورَةٌ", "maksur", "noun", ["naat-sifa", "ism-maful"], "صِفَةٌ مَرْفُوعَةٌ.", "«with a kasra».", "«meksûr»."),
  W("لِيَدُلَّ", "dalla", "verb", ["lam-taleel", "an-masdariyya", "doubled-verbs"], "اللَّامُ لِلتَّعْلِيلِ، وَيَدُلَّ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ.", "«to show» — naṣb by a hidden أَنْ after the lām.", "«delâlet etsin diye» — lâm'dan sonra gizli en ile mansûb.", segments=[seg("لِ", "lam-taleel", "part"), seg("يَدُلَّ", "dalla", "verb")]),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«that».", "«-e»."),
  W("أَنَّ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«that».", "«... olduğuna»."),
  W("مَعَهُ", "maa", "noun", ["inna-wa-akhawatuha", "maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "ظَرْفٌ مَنْصُوبٌ خَبَرُ أَنَّ مُقَدَّمٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with it» — the fronted khabar of أَنَّ.", "«onunla birlikte» — enne'nin öne alınmış haberi.", segments=[seg("مَعَ", "maa", "noun"), pr3ms()]),
  W("مِثْلَهُ", "mithl", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«another like it» — the ism of أَنَّ.", "«bir benzeri» — enne'nin ismi.", segments=[seg("مِثْلَ", "mithl", "noun"), pr3ms()]),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("جِنْسِهِ", "jins", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its kind».", "«cinsinden».", punct="،", segments=[seg("جِنْسِ", "jins", "noun"), pr3msi()]),
  nahwu(),
  W("مُسْلِمَانِ", "muslim", "noun", ["idafa-definiteness", MT], "فِي مَحَلِّ جَرٍّ — مُثَنًّى مَرْفُوعٌ بِالْأَلِفِ.", "«two Muslims» — the dual on its alif.", "«iki Müslüman» — elifle tesniye.", punct="."),
 ]})

# ----------- s2 (RESTORED): the maqsur
S.append({"id": "s2", "translation": {
 "en": "And the alif of the maqṣūr is turned into a wāw if it is a third letter standing for a wāw, as in عَصَوَانِ; and into a yāʾ otherwise, as in رَحَيَانِ and أَعْلَيَانِ." + R_EN,
 "tr": "Maksûrun elifi, üçüncü harf olup vâvdan münkalib ise vâva çevrilir, عَصَوَانِ gibi; bunun dışında yâya çevrilir, رَحَيَانِ ve أَعْلَيَانِ gibi." + R_TR},
 "tokens": [
  atf_wa("وَتُقْلَبُ", "qalaba", "verb", ["naib-al-fail"], "تُقْلَبُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is turned».", "«ve çevrilir».", "تُقْلَبُ"),
  W("أَلِفُ", "alif-letter", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the alif of».", "«elifi»."),
  W("الْمَقْصُورِ", "maqsur", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the maqṣūr».", "«maksûrun»."),
  W("وَاوًا", "waw-letter", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«into a wāw».", "«vâva»."),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if».", "«eğer»."),
  W("كَانَتْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is».", "«ise»."),
  W("ثَالِثَةً", "thalith", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَتْ مَنْصُوبٌ.", "«third».", "«üçüncü»."),
  W("بَدَلًا", "badal", "noun", ["hal"], "حَالٌ مَنْصُوبٌ.", "«standing for».", "«bedel olarak»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-den»."),
  W("وَاوٍ", "waw-letter", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«a wāw».", "«vâv».", punct="،"),
  nahwu(),
  cited("عَصَوَانِ", "asa-staff", "noun", ["idafa-definiteness", MT], "فِي مَحَلِّ جَرٍّ — أَصْلُ عَصًا عَصَوٌ، فَرَجَعَتِ الْوَاوُ.", "«two staffs» — عَصًا was عَصَوٌ, so the wāw returns.", "«iki asâ» — asâ'nın aslı asaven; vâv geri gelir.", punct="،"),
  atf_wa("وَيَاءً", "ya-letter", "noun", ["maful-bihi"], "يَاءً مَعْطُوفٌ عَلَى وَاوًا مَنْصُوبٌ.", "«and into a yāʾ».", "«ve yâya».", "يَاءً"),
  W("فِيمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "فِي حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in what».", "«... olanda».", segments=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("سِوَاهُ", "siwa", "noun", ["ism-mawsul", "idafa-definiteness", "ism-maqsur-manqus"], "ظَرْفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِلَةُ مَا.", "«is other than that».", "«bunun dışında».", punct="،", segments=[seg("سِوَا", "siwa", "noun"), pr3ms()]),
  nahwu(),
  cited("رَحَيَانِ", "raha", "noun", ["idafa-definiteness", MT], "فِي مَحَلِّ جَرٍّ — أَصْلُ رَحًى رَحَيٌ.", "«two millstones» — رَحًى was رَحَيٌ.", "«iki değirmen taşı» — rahâ'nın aslı raheyün."),
  cited_wa("وَأَعْلَيَانِ", "ala-highest", "noun", [MT], "أَعْلَيَانِ مَعْطُوفٌ — الْأَلِفُ رَابِعَةٌ فَتُقْلَبُ يَاءً.", "«and two highest» — a fourth alif turns to yāʾ.", "«ve iki en yüksek» — dördüncü elif yâya çevrilir.", "أَعْلَيَانِ", punct="."),
 ]})

# ----------- s3 (RESTORED): the mamdud
S.append({"id": "s3", "translation": {
 "en": "And the hamza of the mamdūd is turned into a wāw if it is for the feminine, as in حَمْرَاوَانِ; kept if it is original, as in قُرَّاءَانِ; and in what is other than these both ways are allowed, as in كِسَاءَانِ and كِسَاوَانِ." + R_EN,
 "tr": "Memdûdun hemzesi te'nîs için ise vâva çevrilir, حَمْرَاوَانِ gibi; aslî ise sâbit kalır, قُرَّاءَانِ gibi; bunların dışındakilerde iki vecih de câizdir, كِسَاءَانِ ve كِسَاوَانِ gibi." + R_TR},
 "tokens": [
  atf_wa("وَهَمْزَةُ", "hamza-letter", "noun", ["mubtada-khabar", "idafa-definiteness"], "هَمْزَةُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the hamza of» — the mubtada.", "«ve hemzesi» — mübtedâ.", "هَمْزَةُ"),
  W("الْمَمْدُودِ", "mamdud", "noun", ["idafa-definiteness", "ism-mamdud"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mamdūd».", "«memdûdun»."),
  W("تُقْلَبُ", "qalaba", "verb", ["naib-al-fail", "mubtada-khabar"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ.", "«is turned» — the khabar clause.", "«çevrilir» — haber cümlesi."),
  W("وَاوًا", "waw-letter", "noun", ["maful-bihi"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«into a wāw».", "«vâva»."),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  W("كَانَتْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ.", "«it is».", "«ise»."),
  W("لِلتَّأْنِيثِ", "tanith", "noun", ["huruf-jarr", "kana-wa-akhawatuha"], "اللَّامُ حَرْفُ جَرٍّ، وَالتَّأْنِيثِ مَجْرُورٌ؛ خَبَرُ كَانَتْ.", "«for the feminine».", "«te'nîs için».", punct="،", segments=[seg("لِ", "li", "prep"), seg("التَّأْنِيثِ", "tanith", "noun")]),
  nahwu(),
  cited("حَمْرَاوَانِ", "hamra", "noun", ["idafa-definiteness", MT, "ism-mamdud"], "فِي مَحَلِّ جَرٍّ — هَمْزَةُ حَمْرَاءَ لِلتَّأْنِيثِ فَقُلِبَتْ وَاوًا.", "«two red (f.)» — the feminine hamza turned to wāw.", "«iki kırmızı (müennes)» — te'nîs hemzesi vâva çevrildi.", punct="،"),
  atf_wa("وَتَثْبُتُ", "thabata", "verb", ["fail"], "تَثْبُتُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and is kept».", "«ve sâbit kalır».", "تَثْبُتُ"),
  W("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ.", "«if».", "«eğer»."),
  W("كَانَتْ", "kana", "verb", ["in-shartiyya", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ.", "«it is».", "«ise»."),
  W("أَصْلِيَّةً", "asli", "noun", ["kana-wa-akhawatuha", "ism-mansub"], "خَبَرُ كَانَتْ مَنْصُوبٌ.", "«original».", "«aslî».", punct="،"),
  nahwu(),
  cited("قُرَّاءَانِ", "qurra-reciters", "noun", ["idafa-definiteness", MT, "ism-mamdud"], "فِي مَحَلِّ جَرٍّ — الْهَمْزَةُ لَامُ الْكَلِمَةِ مِنْ ق ر أ.", "«two reciters» — the hamza is the root's own.", "«iki okuyucu» — hemze kökün kendi harfi.", punct="،"),
  atf_wa("وَفِيمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "anwa-ma"], "فِي حَرْفُ جَرٍّ، وَمَا فِي مَحَلِّ جَرٍّ.", "«and in what».", "«ve ... olanda».", "مَا", extra_segs=[seg("فِي", "fi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  W("سِوَاهُمَا", "siwa", "noun", ["ism-mawsul", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«is other than these two».", "«bu ikisinin dışında».", segments=[seg("سِوَا", "siwa", "noun"), pr3d()]),
  W("الْوَجْهَانِ", "wajh", "noun", ["mubtada-khabar", MT], "مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ قَبْلَهُ — هَمْزَةٌ مُنْقَلِبَةٌ عَنْ أَصْلٍ.", "«both ways» — a hamza that replaced a radical.", "«iki vecih» — bir aslî harften dönüşmüş hemze.", punct="،"),
  nahwu(),
  cited("كِسَاءَانِ", "kisa", "noun", ["idafa-definiteness", MT, "ism-mamdud"], "فِي مَحَلِّ جَرٍّ — أَصْلُ كِسَاءٍ كِسَاوٌ.", "«two cloaks» — كِسَاء was كِسَاوٌ.", "«iki örtü» — kisâ'nın aslı kisâvün."),
  cited_wa("وَكِسَاوَانِ", "kisa", "noun", [MT], "كِسَاوَانِ مَعْطُوفٌ — بِرَدِّ الْوَاوِ.", "«and كِسَاوَانِ» — with the wāw restored.", "«ve kisâvâni» — vâv geri getirilerek.", "كِسَاوَانِ", punct="."),
 ]})

# ----------- s4 (RESTORED): the nun in annexation
S.append({"id": "s4", "translation": {
 "en": "And its nūn is dropped in annexation, as in «the two beaters of Zayd»." + R_EN,
 "tr": "Nûnu izâfette hazfedilir, «Zeyd'in iki dövücüsü» gibi." + R_TR},
 "tokens": [
  atf_wa("وَتُحْذَفُ", "hadhafa", "verb", ["naib-al-fail"], "تُحْذَفُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and is dropped».", "«ve hazfedilir».", "تُحْذَفُ"),
  W("نُونُهُ", "nun-letter", "noun", ["naib-al-fail", "idafa-definiteness", MT], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its nūn».", "«nûnu».", segments=[seg("نُونُ", "nun-letter", "noun"), pr3ms()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْإِضَافَةِ", "idafa", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«annexation».", "«izâfette».", punct="،"),
  nahwu(),
  W("الضَّارِبَا", "darib", "noun", ["idafa-definiteness", MT, "ism-fail"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ مُثَنًّى مَرْفُوعٌ بِالْأَلِفِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهُوَ مُضَافٌ.", "«the two beaters of» — the nūn gone for the iḍāfa.", "«iki dövücüsü» — izâfet için nûnu düşmüş."),
  W("زَيْدٍ", "zayd", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd».", "«Zeyd'in».", punct="."),
 ]})

# ----------- s5 (RESTORED): the irregular pair
S.append({"id": "s5", "translation": {
 "en": "And they said خُصْيَانِ and أَلْيَانِ, dropping the tāʾ against the rule, because the two are reckoned as one thing." + R_EN,
 "tr": "خُصْيَانِ ve أَلْيَانِ dediler; ikisi bir şey hükmünde olduğundan tâ'yı kıyâsa aykırı olarak düşürdüler." + R_TR},
 "tokens": [
  atf_wa("وَقَالُوا", "qala", "verb", ["fail", "hollow-verbs"], "قَالُوا فِعْلٌ مَاضٍ، وَالْوَاوُ فَاعِلٌ — أَيِ: الْعَرَبُ.", "«and they said» — the Arabs.", "«ve dediler» — Araplar.", "قَالُوا", punct=":"),
  cited("خُصْيَانِ", "khusya", "noun", ["maful-bihi", MT], "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — مُثَنَّى خُصْيَةٍ بِلَا تَاءٍ.", "«the two testicles» — the dual of خُصْيَة without its tāʾ.", "«iki haya» — husye'nin tâsız tesniyesi."),
  cited_wa("وَأَلْيَانِ", "alya-fat", "noun", [MT], "أَلْيَانِ مَعْطُوفٌ — مُثَنَّى أَلْيَةٍ بِلَا تَاءٍ.", "«and the two rump-fats» — the dual of أَلْيَة.", "«ve iki kuyruk yağı» — elye'nin tesniyesi.", "أَلْيَانِ", punct="،"),
  W("بِحَذْفِ", "hadhf", "noun", ["huruf-jarr", "idafa-definiteness", "hal"], "الْبَاءُ حَرْفُ جَرٍّ، وَحَذْفِ مَجْرُورٌ، وَهُوَ مُضَافٌ — فِي مَوْضِعِ الْحَالِ.", "«dropping».", "«hazfiyle».", segments=[seg("بِ", "bi", "prep"), seg("حَذْفِ", "hadhf", "noun")]),
  W("التَّاءِ", "ta-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tāʾ».", "«tâ'yı»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«against».", "«... aykırı»."),
  W("خِلَافِ", "khilaf", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the contrary of».", "«hilâfına»."),
  W("الْقِيَاسِ", "qiyas", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the rule».", "«kıyâsın».", punct="،"),
  W("لِأَنَّهُمَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ، وَهُمَا اسْمُهَا.", "«because the two».", "«çünkü ikisi».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3d()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("حُكْمِ", "hukm", "noun", ["huruf-jarr", "idafa-definiteness", "inna-wa-akhawatuha"], "مَجْرُورٌ، وَهُوَ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ أَنَّ.", "«the reckoning of» — the khabar of أَنَّ.", "«hükmünde» — enne'nin haberi."),
  W("شَيْءٍ", "shay", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing».", "«bir şey»."),
  W("وَاحِدٍ", "wahid", "noun", ["naat-sifa"], "صِفَةٌ مَجْرُورَةٌ.", "«one».", "«tek».", punct="."),
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
 "qalaba": need("qalaba", "قَلَبَ", "ق ل ب", "verb", "to turn (a letter) into another, to invert (قَلَبَ يَقْلِبُ)", "(bir harfi) başkasına çevirmek, kalb etmek (kalebe yaklibü)", 3),
 "qurra-reciters": need("qurra-reciters", "قُرَّاء", "ق ر أ", "noun", "reciters (a plural of قَارِئ) — a mamdūd whose hamza is the root's own", "okuyucular (kârî'in bir cem'i) — hemzesi kökün kendisinden olan memdûd", 4),
 "kisa": need("kisa", "كِسَاء", "ك س و", "noun", "a cloak, a garment — a mamdūd whose hamza stands for a radical wāw", "örtü, elbise — hemzesi aslî bir vâvdan dönüşmüş memdûd", 3),
 "khusya": need("khusya", "خُصْيَة", "خ ص ي", "noun", "a testicle — dual خُصْيَانِ without the tāʾ, against the rule", "haya — tesniyesi kıyâsa aykırı olarak tâsız: husyâni", 5),
 "alya-fat": need("alya-fat", "أَلْيَة", "أ ل ي", "noun", "the fat of a sheep's tail — dual أَلْيَانِ without the tāʾ, against the rule", "kuyruk yağı — tesniyesi kıyâsa aykırı olarak tâsız: elyâni", 5),
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
put_morph(mo, "qalaba", _sg.sound1("daraba", "قَلَب", "قْلِب", "اِقْلِب", "قَلْب", "قَالِب", "مَقْلُوب", "قُلِبَ", "يُقْلَبُ", "قَلَبَ الشَّيْءَ يَقْلِبُهُ قَلْبًا: حَوَّلَهُ عَنْ وَجْهِهِ — مِنَ الْبَابِ الثَّانِي."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch12 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "الْمُثَنَّى فِي الْكَافِيَةِ", "en": "The dual in the Kafiya: its definition, the maqṣūr's alif and the mamdūd's hamza before the dual ending, the nūn in annexation, the irregular pair", "tr": "Kâfiye'de tesniye: tarifi, tesniye ekinden önce maksûrun elifi ve memdûdun hemzesi, izâfette nûn, kıyâsa aykırı çift"},
 "level": 3, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — المثنى: ما لحق آخره ألف أو ياء مفتوح ما قبلها ونون مكسورة ليدل على أن معه مثله من جنسه؛ ألف المقصور وهمزة الممدود؛ نونه تحذف في الإضافة؛ خصيان وأليان", "ضياء صونغور اوغلى — دفتر الكافية: التعريف بلفظه، عصوان ورحيان وأعليان، قراءان وحمراوان وكساءان وكساوان، الضاربا زيد"],
 "question": {
  "en": ["What is the DUAL? A noun that takes, at its end, an alif in rafʿ or a yāʾ (with a fatḥa before it) in naṣb and jarr, plus a nūn with a kasra — the ending saying «and another like it of its kind»: مُسْلِمَانِ / مُسْلِمَيْنِ.",
         "What does a maqṣūr do? Its alif must become a letter again: a wāw when it is the third letter and came from a wāw (عَصًا → عَصَوَانِ), a yāʾ in every other case (رَحًى → رَحَيَانِ; أَعْلَى → أَعْلَيَانِ, a fourth letter).",
         "And a mamdūd? Its hamza stays when it is a root letter (قُرَّاء → قُرَّاءَانِ), turns to wāw when it is the mark of the feminine (حَمْرَاء → حَمْرَاوَانِ), and may do either when it replaced a radical (كِسَاء → كِسَاءَانِ / كِسَاوَانِ).",
         "What happens in annexation? The nūn drops, exactly as the sound plural's does: الضَّارِبَا زَيْدٍ — the alif stays, and that is how a dual muḍāf is known.",
         "Why خُصْيَانِ without the tāʾ? Because the Arabs reckon the pair as one thing; the Kafiya records it as against the rule (and أَلْيَانِ with it), not as a licence to drop any tāʾ.",
         "What does the engine do? The IdafaEngine drops the dual's nūn before a muḍāf ilayh and breaks a dual's yāʾ with a kasra before the article's silent alif; the AlamaEngine and IrabSign read the alif and the yāʾ as letters of iʿrāb, not vowels."],
  "tr": ["TESNİYE nedir? Sonuna ref'de bir elif, nasb ve cerde (mâkabli meftûh) bir yâ ile meksûr bir nûn alan isim — ek «ve cinsinden bir benzeri daha» der: مُسْلِمَانِ / مُسْلِمَيْنِ.",
         "Maksûr ne yapar? Elifi yeniden harf olmalıdır: üçüncü harf olup vâvdan geldiyse vâv (عَصًا → عَصَوَانِ), diğer her durumda yâ (رَحًى → رَحَيَانِ; أَعْلَى → أَعْلَيَانِ, dördüncü harf).",
         "Ya memdûd? Hemzesi kök harfiyse kalır (قُرَّاء → قُرَّاءَانِ), te'nîs alâmetiyse vâva döner (حَمْرَاء → حَمْرَاوَانِ), aslî bir harften dönüşmüşse ikisi de olur (كِسَاء → كِسَاءَانِ / كِسَاوَانِ).",
         "İzâfette ne olur? Nûn, sâlim ceminki gibi düşer: الضَّارِبَا زَيْدٍ — elif kalır; tesniye muzâf böyle tanınır.",
         "Neden tâsız خُصْيَانِ? Çünkü Araplar çifti tek şey sayar; Kâfiye bunu (أَلْيَانِ ile birlikte) kıyâsa aykırı diye kaydeder, her tâ'yı düşürme ruhsatı olarak değil.",
         "Motor ne yapar? IdafaEngine muzâfun ileyhten önce tesniyenin nûnunu düşürür ve lâm-ı tarifin sâkin elifinden önce tesniyenin yâsını kesre ile kırar; AlamaEngine ve IrabSign elif ile yâyı hareke değil i'râb harfi olarak okur."]},
 "plain": {
  "en": "Two of a thing: add -āni (or -ayni in the other cases). A word ending in a short alif turns it back into w or y first (عَصَوَانِ، رَحَيَانِ); a word ending in a long alif-hamza keeps the hamza or turns it to w depending on where the hamza came from. Before a possessor the -ni falls away.",
  "tr": "Bir şeyin ikisi: -âni (öteki hâllerde -eyni) eklenir. Kısa elifle biten kelime önce onu v ya da y'ye geri çevirir (عَصَوَانِ، رَحَيَانِ); uzun elif-hemze ile biten kelime hemzeyi, nereden geldiğine göre korur ya da v'ye çevirir. Bir sahipten önce -ni düşer."},
 "explanation": {
  "en": "The Kafiya defines the dual by its ending and by what the ending says — «with it is another like it of its kind» — and then spends the chapter on the one thing a learner cannot guess: what the last letter of the singular does when the ending arrives. A maqṣūr ends in an alif, and an alif cannot carry the ending, so the letter it replaced comes back: the wāw if the alif is third and came from a wāw (the notebook's عَصَوٌ behind عَصًا), the yāʾ otherwise — for an alif from a yāʾ (رَحَيٌ) and for every alif beyond the third letter, which is turned to yāʾ whatever its origin (أَعْلَيَانِ). A mamdūd ends in alif + hamza, and the hamza has three histories: a root letter keeps its place (قُرَّاءَانِ), the hamza of femininity gives way to wāw (حَمْرَاوَانِ, the same wāw the nisba and the plural of حَمْرَاء show), and a hamza that itself replaced a wāw or yāʾ may do either (كِسَاءَانِ / كِسَاوَانِ) — the IlalEngine's chapter on the mamdūd is this rule seen from the other side. Two rulings close it: the nūn falls in annexation, as it does on the sound plural, leaving الضَّارِبَا زَيْدٍ; and خُصْيَانِ، أَلْيَانِ drop the singular's tāʾ because the two are one thing — recorded as an exception to the rule, which is the Kafiya's way of saying the rule holds everywhere else.",
  "tr": "Kâfiye tesniyeyi ekiyle ve ekin söylediğiyle tarif eder — «kendisiyle birlikte cinsinden bir benzeri daha vardır» — sonra bâbı öğrencinin tahmin edemeyeceği tek şeye harcar: ek gelince müfredin son harfi ne yapar? Maksûr elifle biter, elif eki taşıyamaz; bu yüzden yerini aldığı harf geri gelir: elif üçüncü olup vâvdan geldiyse vâv (defterin عَصًا arkasındaki عَصَوٌ'u), diğer hâllerde yâ — yâdan gelen elif için (رَحَيٌ) ve üçüncü harfin ötesindeki her elif için, aslı ne olursa olsun yâya çevrilir (أَعْلَيَانِ). Memdûd elif + hemze ile biter ve hemzenin üç geçmişi vardır: kök harfi yerinde kalır (قُرَّاءَانِ), te'nîs hemzesi vâva bırakır (حَمْرَاوَانِ, nisbenin ve حَمْرَاء cem'inin gösterdiği aynı vâv) ve kendisi bir vâv ya da yânın yerini almış hemze ikisini de yapabilir (كِسَاءَانِ / كِسَاوَانِ) — IlalEngine'in memdûd faslı bu kuralın öbür yüzden görünüşüdür. İki hüküm kapatır: nûn, sâlim cemideki gibi izâfette düşer ve الضَّارِبَا زَيْدٍ kalır; خُصْيَانِ، أَلْيَانِ ise ikisi bir şey olduğundan müfredin tâ'sını düşürür — kurala istisnâ olarak kaydedilir ki bu Kâfiye'nin kuralın başka her yerde geçerli olduğunu söyleme biçimidir."},
 "examples": [
  {"ar": "الْمُثَنَّى: مَا لَحِقَ آخِرَهُ أَلِفٌ أَوْ يَاءٌ مَفْتُوحٌ مَا قَبْلَهَا وَنُونٌ مَكْسُورَةٌ", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "عَصَوَانِ — رَحَيَانِ، أَعْلَيَانِ", "en": "The maqṣūr's alif.", "tr": "Maksûrun elifi.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "حَمْرَاوَانِ — قُرَّاءَانِ — كِسَاءَانِ وَكِسَاوَانِ", "en": "The mamdūd's hamza.", "tr": "Memdûdun hemzesi.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "الضَّارِبَا زَيْدٍ", "en": "The nūn in annexation.", "tr": "İzâfette nûn.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "خُصْيَانِ وَأَلْيَانِ", "en": "The irregular pair.", "tr": "Kıyâsa aykırı çift.", "sourceStory": "al-kafiya", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«عَصَيَانِ — maksûrun elifi her zaman yâ olur»",
   "right": "«عَصَوَانِ — üçüncü elif vâvdan geldiyse vâva döner; yâ yalnız diğer hâllerde: رَحَيَانِ»",
   "why": {"en": "The alif only disguises a radical; the dual restores the radical it came from.", "tr": "Elif yalnız bir aslî harfi gizler; tesniye geldiği harfi geri getirir."}},
  {"wrong": "«حَمْرَاءَانِ — hemze olduğu gibi kalır»",
   "right": "«حَمْرَاوَانِ — te'nîs hemzesi vâva çevrilir; yalnız kök hemzesi kalır: قُرَّاءَانِ»",
   "why": {"en": "The hamza of femininity is not a root letter, so it cannot carry the dual's alif and gives way to wāw.", "tr": "Te'nîs hemzesi kök harfi değildir; tesniyenin elifini taşıyamaz, vâva bırakır."}},
  {"wrong": "«الضَّارِبَانِ زَيْدٍ — tesniye nûnu izâfette kalır»",
   "right": "«الضَّارِبَا زَيْدٍ — izâfette tesniyenin nûnu, sâlim ceminki gibi düşer»",
   "why": {"en": "The nūn stands in for the tanwīn, and a muḍāf takes no tanwīn.", "tr": "Nûn tenvinin yerini tutar; muzâf tenvin almaz."}},
  {"wrong": "«خُصْيَانِ gibi her tâlı ismin tesniyesinde tâ düşer»",
   "right": "«خُصْيَتَانِ kıyâstır; خُصْيَانِ ve أَلْيَانِ kıyâsa aykırı iki kelimedir, kural değil»",
   "why": {"en": "The Kafiya cites them as heard exceptions; the tāʾ stays in every regular dual (امْرَأَتَانِ، نَاقَتَانِ).", "tr": "Kâfiye onları işitilmiş istisnâlar olarak nakleder; her kıyâsî tesniyede tâ kalır (امْرَأَتَانِ، نَاقَتَانِ)."}}],
 "relatedNotes": [MT, "ism-maqsur-manqus", "ism-mamdud", "idafa-definiteness", "jam-mudhakkar-salim", "al-murab-wal-mabni-wal-irab"]}

ADD_EN = (" Chapter 12 (notebook lines ~219-222): the dual defined in the notebook's own Arabic (s1) with every example it gives; the rulings on the maqṣūr's alif, "
          "the mamdūd's hamza, the nūn in annexation and the irregular خُصْيَانِ / أَلْيَانِ restored from the received matn and marked (s2-s5).")
ADD_TR = (" On ikinci bâb (defter satırları ~219-222): tesniye defterin kendi Arapçasıyla tarif edilir (s1), verdiği her örnekle; maksûrun elifi, memdûdun hemzesi, "
          "izâfette nûn ve kıyâsa aykırı خُصْيَانِ / أَلْيَانِ hükümleri alınan metinden geri yazılmış ve işaretlenmiştir (s2-s5).")
write_out(12, S, TITLE, ADD_EN, ADD_TR, "219-222", GLOSS_ADD, notes=(NOTE,),
          related=((MT, [K]), ("ism-maqsur-manqus", [K]), ("ism-mamdud", [K])))
report(12, S, GLOSS_ADD, (NOTE,))
