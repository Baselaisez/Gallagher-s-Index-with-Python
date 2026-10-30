# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 6: THE NOUN-VERBS, THE SOUNDS AND THE COMPOUNDS. The noun-verb defined (a noun with the meaning of a command or of
a past verb: رُوَيْدَ زَيْدًا، هَيْهَاتَ ذَاكَ), فَعَالِ from the triliteral as a productive pattern of command (نَزَالِ، تَرَاكِ), what resembles it in
deflection and pattern — the definite maṣdar فَجَارِ, the description يَا فَسَاقِ, the women's names قَطَامِ and غَلَابِ — mabnī for the Ḥijāzīs and
declined by Tamīm unless it ends in a rāʾ (حَضَارِ); the sound-words (غَاقِ، نَخِّ); the compounds of two words with no relation between them
(خَمْسَةَ عَشَرَ and its sisters, حَادِيَ عَشَرَ to تَاسِعَ عَشَرَ, the exception اثْنَا عَشَرَ, and بَعْلَبَكَّ).
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~189-190 of the transcription.

  VERBATIM from the notebook's Arabic: the three definitions (s1, s7, s9) and every example.
  RESTORED (the ruling stands in Turkish; the received matn of the Kafiya is written and marked): s2, s3, s4, s5, s6, s8, s10, s11, s12.
  COMMENTARY (the notebook's explanation): s13 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 author_kafiya_ch6.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "asma-al-afal-wal-aswat-wal-murakkabat"
K3 = "al-mabni-wal-mudmar"
AF = "ism-fil"
TITLE = {"ar": "أَسْمَاءُ الْأَفْعَالِ وَالْأَصْوَاتُ وَالْمُرَكَّبَاتُ", "en": "The noun-verbs, the sounds and the compounds", "tr": "Fiil isimleri, sesler ve mürekkebler"}
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
def ka_(full, lex, pos, tags, ar, en, tr, inner, punct=None, segs=None):
    return W(full, lex, pos, ["huruf-jarr"] + tags, "الْكَافُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=(segs if segs else [seg("كَ", "ka", "prep"), seg(inner, lex, pos)]))

# ----------- s1 (VERBATIM): the definition
S.append({"id": "s1", "translation": {
 "en": "The noun-verbs: what has the meaning of a command or of a past verb.",
 "tr": "Fiil isimleri: emir ya da mâzî manasında olanlardır."},
 "tokens": [
  W("أَسْمَاءُ", "ism", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir", AF], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ — جَمْعُ اسْمٍ.", "«the nouns of» — the mubtada.", "«isimleri» — mübtedâ."),
  W("الْأَفْعَالِ", "fil", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ فِعْلٍ.", "«verbs».", "«fiil».", punct=":"),
  W("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«what» — the khabar.", "«... olan» — haber."),
  W("كَانَ", "kana", "verb", ["ism-mawsul", "kana-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«is» — kāna, its ism the ʿāʾid; the ṣila.", "«olan» — kâne, ismi âid; sıla."),
  W("بِمَعْنَى", "mana", "noun", ["huruf-jarr", "kana-wa-akhawatuha", "idafa-definiteness", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُوَ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ.", "«in the meaning of» — the jarr phrase as kāna's khabar.", "«manasında» — câr-mecrûr, kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  W("الْأَمْرِ", "amr", "noun", ["idafa-definiteness", "imperative-amr"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the command».", "«emir»."),
  W("أَوِ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or».", "«ya da»."),
  W("الْمَاضِي", "madi", "noun", ["atf-nasaq", "ism-maqsur-manqus"], "مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past verb».", "«mâzî».", punct="."),
 ]})

# ----------- s2 (RESTORED + the notebook's examples)
S.append({"id": "s2", "translation": {
 "en": "As in «grant Zayd respite!» and «far be that!»." + R_EN,
 "tr": "«Zeyd'e mühlet ver!» ve «şu uzak olsun!» gibi." + R_TR},
 "tokens": [
  nahwu(),
  cited("رُوَيْدَ", "ruwayd", "pron", ["idafa-definiteness", AF, "imperative-amr"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ؛ وَفِي الْمِثَالِ اسْمُ فِعْلِ أَمْرٍ بِمَعْنَى أَمْهِلْ، وَفَاعِلُهُ مُسْتَتِرٌ.", "«grant respite!» — a noun with the force of أَمْهِلْ; its doer concealed.", "«mühlet ver!» — emhil manasında isim; fâili gizli."),
  W("زَيْدًا", "zayd", "propn", ["maful-bihi", AF], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَمِلَ فِيهِ اسْمُ الْفِعْلِ.", "«Zayd» — the object the noun-verb governs.", "«Zeyd'e» — fiil isminin amel ettiği mef'ûl."),
  cited_wa("وَهَيْهَاتَ", "hayhat", "noun", [AF], "هَيْهَاتَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — اسْمُ فِعْلٍ مَاضٍ بِمَعْنَى بَعُدَ.", "«and far be it!» — a noun with the force of بَعُدَ.", "«ve uzak olsun!» — be'ude manasında isim.", "هَيْهَاتَ"),
  W("ذَاكَ", "dhalika", "pron", ["fail", AF, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«that» — the doer of هَيْهَاتَ.", "«şu» — heyhâte'nin fâili.", punct=".", segments=[seg("ذَا", "dha", "pron"), seg("كَ", "kaf-letter", "part")]),
 ]})

# ----------- s3 (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And فَعَالِ from the triliteral is productive in the meaning of a command, as in «come down!» and «leave off!»." + R_EN,
 "tr": "Sülâsîden emir manasında فَعَالِ kıyâsîdir: «in!» ve «bırak!» gibi." + R_TR},
 "tokens": [
  cited_wa("وَفَعَالِ", "faali-wazn", "noun", ["mubtada-khabar", AF], "فَعَالِ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — مَبْنِيٌّ عَلَى الْكَسْرِ.", "«and فَعَالِ» — the mubtada, built on the kasr.", "«ve fe'âli» — mübtedâ, kesr üzere mebnî.", "فَعَالِ"),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الثُّلَاثِيِّ", "thulathi", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the triliteral».", "«sülâsîden»."),
  W("قِيَاسٌ", "qiyas", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — أَيْ: مَقِيسٌ، يُبْنَى مِنْ كُلِّ ثُلَاثِيٍّ.", "«is productive» — the khabar: built from any triliteral.", "«kıyâsîdir» — haber: her sülâsîden yapılır."),
  W("بِمَعْنَى", "mana", "noun", ["huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«in the meaning of».", "«manasında».", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  W("الْأَمْرِ", "amr", "noun", ["idafa-definiteness", "imperative-amr"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a command».", "«emir».", punct="،"),
  nahwu(punct=None),
  cited("نَزَالِ", "nazal", "noun", ["idafa-definiteness", AF], "فِي مَحَلِّ جَرٍّ؛ بِمَعْنَى انْزِلْ — لَازِمٌ.", "«come down!» — for اِنْزِلْ, intransitive.", "«in!» — inzil manasında, lâzım."),
  cited_wa("وَتَرَاكِ", "taraki", "noun", [AF], "تَرَاكِ مَعْطُوفٌ — بِمَعْنَى اتْرُكْ، مُتَعَدٍّ.", "«and leave off!» — for اُتْرُكْ, transitive.", "«ve bırak!» — ütrük manasında, müteaddî.", "تَرَاكِ", punct="."),
 ]})

# ----------- s4 (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "And what comes on it as a definite maṣdar, like فَجَارِ, or as a description, like «O wicked one!», or as a woman's name, like قَطَامِ and غَلَابِ," + R_EN,
 "tr": "Bu vezinde ma'rife masdar olarak gelen فَجَارِ gibi, sıfat olarak gelen «ey fâsıka!» gibi, kadın adı olarak gelen قَطَامِ ve غَلَابِ gibi olanlar," + R_TR},
 "tokens": [
  atf_wa("وَمَا", "ma-mawsula", "pron", ["mubtada-khabar", "ism-mawsul", "anwa-ma"], "مَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، خَبَرُهُ فَمَبْنِيٌّ فِي الْجُمْلَةِ التَّالِيَةِ.", "«and what» — the mubtada; its khabar is the next sentence's فَمَبْنِيٌّ.", "«ve ... olanlar» — mübtedâ; haberi sonraki cümledeki فَمَبْنِيٌّ.", "مَا"),
  W("جَاءَ", "jaa", "verb", ["ism-mawsul", "fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — الْعَائِدُ، وَالْجُمْلَةُ صِلَةٌ.", "«comes» — the ṣila.", "«gelen» — sıla."),
  W("مِنْهُ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — أَيْ: مِنْ هٰذَا الْوَزْنِ.", "«on it» — on this pattern.", "«bu vezinden».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  W("مَصْدَرًا", "masdar-noun", "noun", ["hal"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«as a maṣdar» — the ḥāl.", "«masdar olarak» — hâl."),
  W("مَعْرِفَةً", "marifa", "noun", ["naat-sifa"], "صِفَةٌ لِمَصْدَرًا مَنْصُوبَةٌ.", "«definite».", "«ma'rife»."),
  ka_("كَفَجَارِ", "fajar", "noun", [AF], "فَجَارِ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — بِمَعْنَى الْفُجُورِ.", "«like فَجَارِ» — «the debauchery».", "«fecâri gibi» — el-fücûr manasında.", "فَجَارِ", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("صِفَةً", "sifa", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ عَلَى مَصْدَرًا مَنْصُوبٌ.", "«as a description».", "«sıfat olarak»."),
  ka_("كَيَا", "ya-nida", "part", ["vocative-munada"], "يَا حَرْفُ نِدَاءٍ — وَالْجُمْلَةُ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«like: O» — the call, cited whole.", "«ey ... gibi» — nidâ, bütünüyle hikâye.", "يَا"),
  W("فَسَاقِ", "fasaq", "noun", ["vocative-munada", AF], "مُنَادًى مَبْنِيٌّ عَلَى الْكَسْرِ — بِمَعْنَى يَا فَاسِقَةُ.", "«wicked one!» — for يَا فَاسِقَةُ.", "«fâsıka!» — yâ fâsikatü manasında.", punct="،"),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("عَلَمًا", "alam-name", "noun", ["atf-nasaq", "hal"], "مَعْطُوفٌ مَنْصُوبٌ.", "«as a name».", "«alem olarak»."),
  W("لِمُؤَنَّثٍ", "muannath", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَمُؤَنَّثٍ مَجْرُورٌ.", "«of a woman».", "«bir müennese».", segments=[seg("لِ", "li", "prep"), seg("مُؤَنَّثٍ", "muannath", "noun")]),
  ka_("كَقَطَامِ", "qatam", "propn", [AF, "mamnu-min-sarf"], "قَطَامِ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«like قَطَامِ».", "«Katâmi gibi».", "قَطَامِ"),
  cited_wa("وَغَلَابِ", "ghalab", "propn", [AF], "غَلَابِ مَعْطُوفٌ.", "«and غَلَابِ».", "«ve Galâbi».", "غَلَابِ", punct="،"),
 ]})

# ----------- s5 (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "it is mabnī for the Ḥijāzīs, because of its resemblance to it in deflection and in pattern." + R_EN,
 "tr": "Hicazlılara göre mebnîdir; çünkü adl ve vezin yönünden ona benzer." + R_TR},
 "tokens": [
  W("فَمَبْنِيٌّ", "mabni", "noun", ["mubtada-khabar", K3, "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ دَاخِلَةٌ عَلَى خَبَرِ الْمَوْصُولِ، وَمَبْنِيٌّ خَبَرُ الْمُبْتَدَإِ مَا مَرْفُوعٌ.", "«is mabnī» — the khabar of مَا, with the fāʾ a relative's khabar takes.", "«mebnîdir» — mâ'nın haberi; mevsûlün haberine giren fâ ile.", segments=[seg("فَ", "fa", "conj"), seg("مَبْنِيٌّ", "mabni", "noun")]),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْحِجَازِيِّينَ", "hijazi", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ.", "«the Ḥijāzīs».", "«Hicazlılara».", punct="،"),
  W("لِشَبَهِهِ", "shabah", "noun", ["huruf-jarr", "lam-taleel", "idafa-definiteness"], "اللَّامُ لِلتَّعْلِيلِ، وَشَبَهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«because of its resemblance».", "«benzerliği sebebiyle».", segments=[seg("لِ", "lam-taleel", "part"), seg("شَبَهِ", "shabah", "noun"), pr3msi()]),
  W("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — أَيْ: بِفَعَالِ الْأَمْرِ.", "«to it» — to the فَعَالِ of command.", "«ona» — emir fe'âli'ne.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("عَدْلًا", "adl", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — الْعَدْلُ عَنِ الْفُجُورِ وَالْفَاسِقَةِ.", "«in deflection» — the tamyīz: deflected from الْفُجُور and الْفَاسِقَة.", "«adl yönünden» — temyîz: el-fücûr ve el-fâsıka'dan çevrilmiştir."),
  atf_wa("وَوَزْنًا", "wazn", "noun", ["tamyiz"], "وَزْنًا مَعْطُوفٌ مَنْصُوبٌ.", "«and in pattern».", "«ve vezin yönünden».", "وَزْنًا", punct="."),
 ]})

# ----------- s6 (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And the Banū Tamīm decline it so long as its last letter is not a rāʾ, like حَضَارِ." + R_EN,
 "tr": "Benî Temîm ise, sonu râ olmadıkça onu mu'reb kılar; حَضَارِ gibi." + R_TR},
 "tokens": [
  atf_wa("وَبَنُو", "ibn", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-mudhakkar-salim"], "بَنُو مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«and the sons of» — rafʿ by the wāw, its nūn dropped for the iḍāfa.", "«ve oğulları» — vâv ile merfû; izâfet için nûnu düşmüş.", "بَنُو"),
  W("تَمِيمٍ", "tamim", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«Tamīm».", "«Temîm»."),
  W("يُعْرِبُونَهُ", "araba", "verb", ["mubtada-khabar", "fail", "maful-bihi", "afal-khamsa", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ خَبَرٌ.", "«decline it» — the khabar clause; the wāw its doer.", "«onu mu'reb kılar» — haber cümlesi; vâv fâil.", segments=[seg("يُعْرِبُونَ", "araba", "verb"), pr3ms()]),
  W("مَا", "ma-masdariyya", "part", ["anwa-ma", "maful-fih"], "مَا الْمَصْدَرِيَّةُ الظَّرْفِيَّةُ — أَيْ: مُدَّةَ كَوْنِهِ.", "«so long as» — the maṣdar-and-time مَا.", "«... olduğu sürece» — masdariyye-i zarfiyye mâ."),
  W("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«... olmadıkça»."),
  W("يَكُنْ", "kana", "verb", ["lam-jazim", "kana-wa-akhawatuha"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِالسُّكُونِ.", "«is» — kāna in jazm.", "«olmadıkça» — meczûm kâne."),
  W("آخِرُهُ", "akhir", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَكُنْ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its last letter» — the ism of kāna.", "«sonu» — kâne'nin ismi.", segments=[seg("آخِرُ", "akhir", "noun"), pr3ms()]),
  W("رَاءً", "ra-letter", "noun", ["kana-wa-akhawatuha"], "خَبَرُ يَكُنْ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a rāʾ» — the khabar.", "«râ» — haberi."),
  ka_("كَحَضَارِ", "hadar", "propn", [AF], "حَضَارِ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — عَلَمٌ لِنَجْمٍ، فَهُوَ مَبْنِيٌّ عِنْدَهُمْ أَيْضًا.", "«like حَضَارِ» — the star's name, mabnī for them too.", "«Hadâri gibi» — yıldızın adı; onlara göre de mebnî.", "حَضَارِ", punct="."),
 ]})

# ----------- s7 (VERBATIM): the sounds
S.append({"id": "s7", "translation": {
 "en": "The sounds: every utterance by which a sound is imitated, or by which a call is made to beasts.",
 "tr": "Sesler: kendisiyle bir sesin hikâye edildiği ya da hayvanlara seslenildiği her lafızdır."},
 "tokens": [
  W("الْأَصْوَاتُ", "sawt", "noun", ["mubtada-khabar", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the sounds» — the mubtada.", "«sesler» — mübtedâ.", punct=":"),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«every» — the khabar.", "«her» — haber."),
  W("لَفْظٍ", "lafz", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«utterance».", "«lafız»."),
  W("حُكِيَ", "haka", "verb", ["naib-al-fail", "jumla-sifa", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِفَةٌ لِلَفْظٍ.", "«is imitated» — the passive; the clause a ṣifa of لَفْظ.", "«hikâye edilen» — meçhul; cümle lafzın sıfatı."),
  W("بِهِ", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ إِلَى لَفْظٍ.", "«by which» — the pronoun returns to لَفْظ.", "«kendisiyle» — lafza dönen zamir.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("صَوْتٌ", "sawt", "noun", ["naib-al-fail"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«a sound» — the deputy doer.", "«bir ses» — nâib-i fâil."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("صُوِّتَ", "sawwata", "verb", ["naib-al-fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«a call is made» — the passive; its deputy the jarr phrase.", "«seslenilen» — meçhul; nâibi câr-mecrûr."),
  W("بِهِ", "bi", "prep", ["huruf-jarr", "naib-al-fail"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ، فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.", "«by which» — the deputy doer.", "«kendisiyle» — nâib-i fâil.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  W("لِلْبَهَائِمِ", "bahima", "noun", ["huruf-jarr", "jam-taksir", "mamnu-min-sarf"], "اللَّامُ حَرْفُ جَرٍّ، وَالْبَهَائِمِ مَجْرُورٌ بِالْكَسْرَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، جُرَّتْ بِالْكَسْرَةِ لِأَجْلِ ال.", "«to beasts» — a ṣīghat muntahā al-jumūʿ, kasra because of the article.", "«hayvanlara» — müntehe'l-cumû' sîgası; el aldığı için kesre.", punct=".", segments=[seg("لِ", "li", "prep"), seg("لْبَهَائِمِ", "bahima", "noun")]),
 ]})

# ----------- s8 (RESTORED + the notebook's examples)
S.append({"id": "s8", "translation": {
 "en": "As in غَاقِ and نَخِّ." + R_EN,
 "tr": "غَاقِ ve نَخِّ gibi." + R_TR},
 "tokens": [
  nahwu(),
  cited("غَاقِ", "ghaq", "part", ["idafa-definiteness"], "فِي مَحَلِّ جَرٍّ — حِكَايَةُ صَوْتِ الْغُرَابِ، مَبْنِيٌّ.", "«caw» — the crow's cry imitated.", "«gâk» — karganın sesinin hikâyesi."),
  cited_wa("وَنَخِّ", "nakh", "part", [], "نَخِّ مَعْطُوفٌ — مَا يُقَالُ لِلْبَعِيرِ لِيَبْرُكَ.", "«and نَخِّ» — said to a camel to make it kneel.", "«ve nah» — deveyi çöktürmek için söylenir.", "نَخِّ", punct="."),
 ]})

# ----------- s9 (VERBATIM): the compounds
S.append({"id": "s9", "translation": {
 "en": "The compounds: every noun made of two words with no relation between them.",
 "tr": "Mürekkebler: aralarında nisbet bulunmayan iki kelimeden olan her isimdir."},
 "tokens": [
  W("الْمُرَكَّبَاتُ", "murakkab", "noun", ["mubtada-khabar", "jam-muannath-salim"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the compounds» — the mubtada.", "«mürekkebler» — mübtedâ.", punct=":"),
  W("كُلُّ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«every» — the khabar.", "«her» — haber."),
  W("اسْمٍ", "ism", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«noun».", "«isim»."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("كَلِمَتَيْنِ", "kalima", "noun", ["huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two words» — jarr by the yāʾ.", "«iki kelime» — yâ ile mecrûr."),
  W("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "jumla-sifa"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَالْجُمْلَةُ صِفَةٌ لِكَلِمَتَيْنِ.", "«there is not» — the clause a ṣifa of the two words.", "«... bulunmayan» — cümle kelimeteyn'in sıfatı."),
  W("بَيْنَهُمَا", "bayna", "noun", ["kana-wa-akhawatuha", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ خَبَرُ لَيْسَ مُقَدَّمٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«between them» — the fronted khabar of لَيْسَ.", "«aralarında» — leyse'nin öne alınmış haberi.", segments=[seg("بَيْنَ", "bayna", "noun"), pr3d()]),
  W("نِسْبَةٌ", "nisba", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a relation» — the delayed ism of لَيْسَ.", "«nisbet» — leyse'nin geriye bırakılmış ismi.", punct="."),
 ]})

# ----------- s10 (RESTORED)
S.append({"id": "s10", "translation": {
 "en": "If the second carries a letter within it, both are built — as in «fifteen» and its sisters, and «eleventh» up to «nineteenth»." + R_EN,
 "tr": "İkinci cüz' bir harf tazammun ederse ikisi de mebnî olur — «on beş» ve kardeşleri, «on birinci»den «on dokuzuncu»ya kadar gibi." + R_TR},
 "tokens": [
  W("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if».", "«eğer».", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("تَضَمَّنَ", "tadammana", "verb", ["in-shartiyya", "fail", "form-v-verbs"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.", "«carries within» — the condition's verb.", "«tazammun ederse» — şart fiili."),
  W("الثَّانِي", "thani", "noun", ["fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second» — the doer, a manqūṣ.", "«ikincisi» — fâil, mankûs."),
  W("حَرْفًا", "harf", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَاوَ الْعَطْفِ فِي خَمْسَةَ عَشَرَ.", "«a letter» — the object: the wāw of joining inside «fifteen».", "«bir harf» — mef'ûl: «on beş»teki atıf vâvı."),
  W("بُنِيَا", "bana", "verb", ["al-majzum-wal-shart-wal-jaza", "naib-al-fail", "al-muthanna", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ.", "«both are built» — the answer; the alif its deputy doer.", "«ikisi de mebnî kılınır» — cevap; elif nâib-i fâil.", punct="،"),
  nahwu(punct=None),
  cited("خَمْسَةَ", "khamsa", "noun", ["idafa-definiteness", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "فِي مَحَلِّ جَرٍّ — الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«fifteen» — the first part built on the fatḥ.", "«on beş» — birinci cüz' feth üzere mebnî."),
  W("عَشَرَ", "ashar", "noun", ["al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — تَضَمَّنَ الْوَاوَ.", "— the second part, built on the fatḥ: it carries the wāw.", "— ikinci cüz', feth üzere mebnî: vâvı tazammun eder."),
  atf_wa("وَأَخَوَاتِهَا", "ukht", "noun", ["idafa-definiteness", "jam-muannath-salim"], "أَخَوَاتِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its sisters» — eleven to nineteen.", "«ve kardeşleri» — on birden on dokuza.", "أَخَوَاتِ", punct="،", extra_segs=[seg("أَخَوَاتِ", "ukht", "noun"), pr3fs()]),
  cited_wa("وَحَادِيَ", "hadi-ashar", "noun", ["al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "حَادِيَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مَبْنِيٌّ عَلَى الْفَتْحِ.", "«and eleventh».", "«ve on birinci».", "حَادِيَ"),
  W("عَشَرَ", "ashar", "noun", ["al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part.", "— ikinci cüz'."),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«up to».", "«-e kadar»."),
  W("تَاسِعَ", "tasi", "noun", ["huruf-jarr", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — مَبْنِيٌّ عَلَى الْفَتْحِ.", "«nineteenth».", "«on dokuzuncu»."),
  W("عَشَرَ", "ashar", "noun", ["al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ.", "— the second part.", "— ikinci cüz'.", punct="،"),
 ]})

# ----------- s11 (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "except «twelve»." + R_EN,
 "tr": "«on iki» müstesnâ." + R_TR},
 "tokens": [
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«... müstesnâ»."),
  W("اثْنَيْ", "ithnan", "noun", ["istithna", "al-muthanna", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "مُسْتَثْنًى مَنْصُوبٌ بِالْيَاءِ — مُعْرَبٌ إِعْرَابَ الْمُثَنَّى لِشَبَهِهِ بِالْمُضَافِ بِحَذْفِ نُونِهِ.", "«two-» — the exception, declined like a dual since its nūn drops like a muḍāf's.", "«on i-» — müstesnâ; nûnu muzâf gibi düştüğünden tesniye gibi mu'reb."),
  W("عَشَرَ", "ashar", "noun", ["al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar"], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — تَضَمَّنَ الْحَرْفَ.", "«-teen» — the second part stays built.", "«-ki» — ikinci cüz' mebnî kalır.", punct="."),
 ]})

# ----------- s12 (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "Otherwise the second is declined as a diptote and the first is built on the fatḥ, like بَعْلَبَكَّ." + R_EN,
 "tr": "Aksi hâlde ikincisi gayr-i munsarif olarak i'râblanır, birincisi feth üzere mebnî kılınır; بَعْلَبَكَّ gibi." + R_TR},
 "tokens": [
  W("وَإِلَّا", "illa", "part", ["in-shartiyya", "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ وَلَا، وَفِعْلُ الشَّرْطِ مَحْذُوفٌ — وَإِنْ لَا يَتَضَمَّنْ.", "«otherwise» — إِنْ + لَا with the verb dropped.", "«aksi hâlde» — in + lâ, fiil hazfedilmiş.", segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  W("أُعْرِبَ", "araba", "verb", ["al-majzum-wal-shart-wal-jaza", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "«is declined» — the answer.", "«i'râblanır» — cevap."),
  W("الثَّانِي", "thani", "noun", ["naib-al-fail", "ism-maqsur-manqus"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«the second» — the deputy doer.", "«ikincisi» — nâib-i fâil."),
  W("غَيْرَ", "ghayr", "noun", ["hal", "idafa-definiteness"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ مُضَافٌ.", "«as non-» — the ḥāl.", "«gayr-i» — hâl."),
  W("مُنْصَرِفٍ", "munsarif", "noun", ["idafa-definiteness", "mamnu-min-sarf", "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لِلْعَلَمِيَّةِ وَالتَّرْكِيبِ.", "«-triptote» — a diptote for being a name and compound.", "«munsarif» — alemlik ve terkib yüzünden gayr-i munsarif."),
  atf_wa("وَبُنِيَ", "bana", "verb", ["naib-al-fail", "naqis-verbs"], "بُنِيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — مَعْطُوفٌ عَلَى أُعْرِبَ.", "«and is built».", "«ve mebnî kılınır».", "بُنِيَ"),
  W("الْأَوَّلُ", "awwal", "noun", ["naib-al-fail"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«the first».", "«birincisi»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("الْفَتْحِ", "fath", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the fatḥ».", "«feth»."),
  ka_("كَبَعْلَبَكَّ", "baalabakk", "propn", ["mamnu-min-sarf"], "بَعْلَبَكَّ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — بَعْلَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَبَكَّ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ غَيْرُ مُنْصَرِفٍ.", "«like Baalbek» — بَعْلَ built on the fatḥ, بَكَّ in jarr by a fatḥa as a diptote.", "«Ba'lebek gibi» — ba'le feth üzere mebnî, bekke gayr-i munsarif olarak fetha ile mecrûr.", "بَعْلَبَكَّ", punct="."),
 ]})

# ----------- s13 (COMMENTARY)
S.append({"id": "s13", "translation": {
 "en": "For the first part has fallen in the middle of the word, and the second carries the letter — so both are built." + C_EN,
 "tr": "Çünkü birinci cüz' kelimenin ortasında kalmış, ikincisi de harfi tazammun etmiştir — bu yüzden ikisi de mebnî olur." + C_TR},
 "tokens": [
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("الْأَوَّلَ", "awwal", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the first» — the ism of أَنَّ.", "«birincisi» — enne'nin ismi."),
  W("وَقَعَ", "waqaa", "verb", ["inna-wa-akhawatuha", "fail", "mithal-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«has fallen» — the khabar of أَنَّ.", "«düşmüştür» — enne'nin haberi."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("وَسَطِ", "wasat", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the middle of».", "«ortasında»."),
  W("الْكَلِمَةِ", "kalima", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the word».", "«kelimenin».", punct="،"),
  atf_wa("وَالثَّانِيَ", "thani", "noun", ["inna-wa-akhawatuha", "ism-maqsur-manqus"], "الثَّانِيَ مَعْطُوفٌ عَلَى اسْمِ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — الْمَنْقُوصُ تَظْهَرُ فَتْحَتُهُ.", "«and the second» — joined to the ism of أَنَّ; a manqūṣ shows its fatḥa.", "«ve ikincisi» — enne'nin ismine atıf; mankûsun fethası görünür.", "الثَّانِيَ"),
  W("تَضَمَّنَ", "tadammana", "verb", ["fail", "form-v-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ.", "«carries» — the khabar.", "«tazammun etmiştir» — haber."),
  W("الْحَرْفَ", "harf", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the letter».", "«harfi».", punct="،"),
  W("فَبُنِيَا", "bana", "verb", ["naib-al-fail", "al-muthanna", "al-fa-fi-jawab-al-shart"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَبُنِيَا فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْأَلِفُ نَائِبُ الْفَاعِلِ.", "«so both are built» — the alif the deputy doer.", "«bu yüzden ikisi de mebnî olur» — elif nâib-i fâil.", punct=".", segments=[seg("فَ", "fa", "conj"), seg("بُنِيَا", "bana", "verb")]),
 ]})

# ---------------------------------------------------------------- NFC
def _nfc(o):
    if isinstance(o, str): return N(o)
    if isinstance(o, list): return [_nfc(x) for x in o]
    if isinstance(o, dict): return {k: _nfc(v) for k, v in o.items()}
    return o
S = _nfc(S)
for _s in S:
    for _t in _s["tokens"]: _t["surface"]["bare"] = bare(_t["surface"]["full"])

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "qatam": need("qatam", "قَطَامِ", None, "propn", "Qaṭāmi — a woman's name on the pattern فَعَالِ, built on the kasra for the Ḥijāzīs", "Katâmi — fe'âli vezninde bir kadın adı; Hicazlılara göre kesr üzere mebnî", 5),
 "ghalab": need("ghalab", "غَلَابِ", "غ ل ب", "propn", "Ghalābi — a woman's name on the pattern فَعَالِ", "Galâbi — fe'âli vezninde bir kadın adı", 5),
 "hadar": need("hadar", "حَضَارِ", "ح ض ر", "propn", "Ḥaḍāri — a star's name on فَعَالِ ending in a rāʾ, which even Tamīm leave built", "Hadâri — fe'âli vezninde, sonu râ olan bir yıldız adı; Temîm de mebnî bırakır", 5),
 "ra-letter": need("ra-letter", "الرَّاء", None, "noun", "the letter rāʾ", "râ harfi", 2),
 "wasat": need("wasat", "وَسَط", "و س ط", "noun", "middle", "orta", 2),
 "ma-masdariyya": need("ma-masdariyya", "مَا (الْمَصْدَرِيَّة)", None, "part", "the maṣdar-making مَا — with a time sense («so long as») it is the مَا المصدرية الظرفية", "masdariyye mâ — zaman manasıyla («... olduğu sürece») masdariyye-i zarfiyye", 4),
 "lam-jazima": need("lam-jazima", "لَمْ", None, "part", "not (the jazm particle that turns the muḍāriʿ to the past)", "-madı (muzâriyi mâzîye çeviren cezm edatı)", 2),
 "ya-nida": need("ya-nida", "يَا", None, "part", "O! (the particle of calling)", "ey! (nidâ harfi)", 1),
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
print("kafiya ch6 gloss+morph ok", len(GLOSS_ADD))

NOTE = {
 "id": K,
 "title": {"ar": "أَسْمَاءُ الْأَفْعَالِ وَالْأَصْوَاتُ وَالْمُرَكَّبَاتُ", "en": "The noun-verbs (رُوَيْدَ، هَيْهَاتَ، the فَعَالِ of command and what resembles it), the sound-words, and the compounds of two words", "tr": "Fiil isimleri (رُوَيْدَ، هَيْهَاتَ، emir fe'âli'si ve ona benzeyenler), ses kelimeleri ve iki kelimeli mürekkebler"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — أسماء الأفعال: ما كان بمعنى الأمر أو الماضي؛ الأصوات: كل لفظ حكي به صوت أو صوت به للبهائم؛ المركبات: كل اسم من كلمتين ليس بينهما نسبة", "ضياء صونغور اوغلى — دفتر الكافية: التعريفات الثلاثة بلفظها، أمثلة فَعَالِ، خلاف الحجاز وتميم، خمسة عشر واثنا عشر وبعلبك"],
 "question": {
  "en": ["What is a NOUN-VERB? A noun carrying the meaning of a command or of a past verb and governing like it: رُوَيْدَ زَيْدًا (= أَمْهِلْهُ, with an object), هَيْهَاتَ ذَاكَ (= بَعُدَ, with a doer). It is mabnī.",
         "Which pattern is productive? فَعَالِ from any triliteral in the meaning of a command — نَزَالِ (= اِنْزِلْ), تَرَاكِ (= اُتْرُكْ) — built on the kasra.",
         "What resembles it? Three things on the same pattern that are not commands: the definite maṣdar (فَجَارِ = الْفُجُور), the description in the call (يَا فَسَاقِ = يَا فَاسِقَة), a woman's name (قَطَامِ، غَلَابِ). All three are deflected from another form (ʿadl) and share the pattern (wazn) — so the Ḥijāzīs build them like نَزَالِ.",
         "What do the Banū Tamīm do? They decline these as diptotes — unless the word ends in a rāʾ (حَضَارِ, the star), which they build too.",
         "What is a SOUND-WORD? An utterance that imitates a sound (غَاقِ, the crow) or calls to a beast (نَخِّ, to a camel). It is mabnī and has no iʿrāb at all.",
         "What is a COMPOUND? Two words made one noun with no relation (no iḍāfa, no predication) between them: خَمْسَةَ عَشَرَ. If the second part carries a letter within (the wāw of joining: five AND ten), both parts are built on the fatḥ — eleven to nineteen and the ordinals حَادِيَ عَشَرَ … تَاسِعَ عَشَرَ — except اثْنَا عَشَرَ, whose first part declines like a dual because its nūn drops like a muḍāf's. If no letter is carried (بَعْلَبَكَّ), the first part is built on the fatḥ and the second is declined as a diptote."],
  "tr": ["FİİL İSMİ nedir? Emir ya da mâzî manası taşıyan ve onun gibi amel eden isim: رُوَيْدَ زَيْدًا (= أَمْهِلْهُ, mef'ûlüyle), هَيْهَاتَ ذَاكَ (= بَعُدَ, fâiliyle). Mebnîdir.",
         "Hangi vezin kıyâsîdir? Her sülâsîden emir manasında فَعَالِ — نَزَالِ (= اِنْزِلْ), تَرَاكِ (= اُتْرُكْ) — kesr üzere mebnî.",
         "Ona ne benzer? Aynı vezinde emir olmayan üç şey: ma'rife masdar (فَجَارِ = الْفُجُور), nidâdaki sıfat (يَا فَسَاقِ = يَا فَاسِقَة), kadın adı (قَطَامِ، غَلَابِ). Üçü de başka bir şekilden çevrilmiştir (adl) ve vezni paylaşır — Hicazlılar bunları نَزَالِ gibi mebnî kılar.",
         "Benî Temîm ne yapar? Bunları gayr-i munsarif olarak i'râblar — kelime râ ile bitmedikçe (حَضَارِ, yıldız); onu onlar da mebnî kılar.",
         "SES KELİMESİ nedir? Bir sesi hikâye eden (غَاقِ, karga) ya da bir hayvana seslenen (نَخِّ, deveye) lafız. Mebnîdir, hiç i'râbı yoktur.",
         "MÜREKKEB nedir? Aralarında nisbet (izâfet, isnâd) bulunmayan, tek isim olmuş iki kelime: خَمْسَةَ عَشَرَ. İkinci cüz' içinde bir harf taşıyorsa (atıf vâvı: beş VE on) iki cüz' de feth üzere mebnî olur — on birden on dokuza ve حَادِيَ عَشَرَ … تَاسِعَ عَشَرَ sıra sayıları — اثْنَا عَشَرَ hariç: birinci cüz'ü nûnu muzâf gibi düştüğünden tesniye gibi i'râblanır. Harf taşınmıyorsa (بَعْلَبَكَّ) birinci cüz' feth üzere mebnî, ikincisi gayr-i munsarif olarak mu'rebdir."]},
 "plain": {
  "en": "Some nouns act like verbs (رُوَيْدَ = «grant respite!», هَيْهَاتَ = «far be it!»); the pattern فَعَالِ makes such a command from any three-letter root, and words that merely look like it are frozen the same way by the Ḥijāzīs. Sound-words and two-word compounds like «fifteen» are frozen too.",
  "tr": "Bazı isimler fiil gibi çalışır (رُوَيْدَ = «mühlet ver!», هَيْهَاتَ = «uzak olsun!»); فَعَالِ vezni her üç harfli kökten böyle bir emir yapar, ona yalnız benzeyen kelimeleri de Hicazlılar aynı şekilde dondurur. Ses kelimeleri ve «on beş» gibi iki kelimeli mürekkebler de donmuştur."},
 "explanation": {
  "en": "Three of the eight mabnī classes the Kāfiya listed in its mabnī chapter are defined here, each by a one-line ḥadd the notebook preserves in Arabic. The noun-verb is defined by its MEANING — a command or a past act — and it does a verb's work without a verb's form: رُوَيْدَ takes an object, هَيْهَاتَ a doer. One pattern of it is productive, فَعَالِ from the triliteral, and the chapter's real teaching is what happens to words that merely share that pattern: a maṣdar used as a definite name of the act (فَجَارِ), a description thrown at a woman in the call (فَسَاقِ), a woman's proper name (قَطَامِ). None of them is a command, but each is a deflection (ʿadl) from a fuller form and stands on the same wazn, and the Ḥijāzī Arabs let that double resemblance freeze them on the kasra; the Tamīmīs instead decline them as diptotes (ʿadl + a reason), unless the rāʾ at the end — which their dialect pronounces with an imāla that wants the kasra — keeps even them from declining (حَضَارِ). The sound-words are the simplest mabnī of all: an imitation (غَاقِ) or a call to a beast (نَخِّ) has no iʿrāb because it enters no sentence. The compounds close the chapter with the rule the number chapters use: two words with no iḍāfa or predication between them are one noun; where the second part carries a swallowed letter (the wāw of «five AND ten») both halves are built on the fatḥ — the whole series eleven to nineteen and its ordinals — while «twelve» keeps its first half declining like a dual because its nūn drops as a muḍāf's would; and where no letter is carried, as in بَعْلَبَكَّ, the first half is built and the second declines as a diptote for being a compound name.",
  "tr": "Kâfiye'nin mebnî bâbında saydığı sekiz mebnî sınıfından üçü burada, defterin Arapçasıyla koruduğu birer satırlık hadlerle tarif edilir. Fiil ismi MANASIYLA tarif edilir — bir emir ya da geçmiş bir iş — ve fiil şekli olmadan fiilin işini yapar: رُوَيْدَ mef'ûl alır, هَيْهَاتَ fâil alır. Bir vezni kıyâsîdir, sülâsîden فَعَالِ; bâbın asıl dersi ise yalnız bu vezni paylaşan kelimelere ne olduğudur: işin ma'rife adı olarak kullanılan masdar (فَجَارِ), nidâda bir kadına atılan sıfat (فَسَاقِ), bir kadın adı (قَطَامِ). Hiçbiri emir değildir; ama her biri daha dolu bir şekilden çevrilmiştir (adl) ve aynı vezinde durur; Hicazlı Araplar bu çifte benzerliğin onları kesre üzerinde dondurmasına izin verir. Temîmliler ise bunları gayr-i munsarif olarak i'râblar (adl + bir sebep) — sondaki râ hariç: lehçelerinin kesre isteyen imâlesiyle söylediği râ, onları bile i'râbdan alıkoyar (حَضَارِ). Ses kelimeleri mebnîlerin en yalınıdır: bir taklit (غَاقِ) ya da hayvana bir sesleniş (نَخِّ) hiçbir cümleye girmediğinden i'râbı yoktur. Mürekkebler bâbı sayı bâblarının kullandığı kuralla kapatır: aralarında izâfet ya da isnâd bulunmayan iki kelime tek isimdir; ikinci cüz' yutulmuş bir harf taşıyorsa («beş VE on»un vâvı) iki yarı da feth üzere mebnîdir — on birden on dokuza bütün dizi ve sıra sayıları — «on iki» ise birinci yarısını tesniye gibi i'râblamaya devam eder, çünkü nûnu bir muzâfınki gibi düşer; harf taşınmıyorsa, بَعْلَبَكَّ'teki gibi, birinci yarı mebnî, ikincisi mürekkeb alem olduğundan gayr-i munsarif olarak mu'rebdir."},
 "examples": [
  {"ar": "أَسْمَاءُ الْأَفْعَالِ: مَا كَانَ بِمَعْنَى الْأَمْرِ أَوِ الْمَاضِي", "en": "The definition.", "tr": "Tarif.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "رُوَيْدَ زَيْدًا، وَهَيْهَاتَ ذَاكَ", "en": "A command and a past act as nouns.", "tr": "İsim olarak bir emir ve bir geçmiş iş.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "نَزَالِ وَتَرَاكِ", "en": "The productive فَعَالِ.", "tr": "Kıyâsî فَعَالِ.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "كَفَجَارِ، وَكَيَا فَسَاقِ، وَكَقَطَامِ وَغَلَابِ", "en": "What resembles it in deflection and pattern.", "tr": "Adl ve vezinde ona benzeyenler.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "الْأَصْوَاتُ: كُلُّ لَفْظٍ حُكِيَ بِهِ صَوْتٌ أَوْ صُوِّتَ بِهِ لِلْبَهَائِمِ", "en": "The sound-words defined.", "tr": "Ses kelimelerinin tarifi.", "sourceStory": "al-kafiya", "sentence": "s7"},
  {"ar": "الْمُرَكَّبَاتُ: كُلُّ اسْمٍ مِنْ كَلِمَتَيْنِ لَيْسَ بَيْنَهُمَا نِسْبَةٌ", "en": "The compounds defined.", "tr": "Mürekkeblerin tarifi.", "sourceStory": "al-kafiya", "sentence": "s9"},
  {"ar": "خَمْسَةَ عَشَرَ وَأَخَوَاتِهَا … إِلَّا اثْنَيْ عَشَرَ … كَبَعْلَبَكَّ", "en": "Both built, the dual exception, the diptote second part.", "tr": "İkisi mebnî, tesniye istisnâsı, gayr-i munsarif ikinci cüz'.", "sourceStory": "al-kafiya", "sentence": "s10"}],
 "commonMistakes": [
  {"wrong": "«رُوَيْدَ زَيْدًا — ruveyde bir zarftır, Zeyd ondan sonra gelen mef'ûl değildir»",
   "right": "«رُوَيْدَ زَيْدًا — ruveyde emhil manasında fiil ismidir, Zeyd onun mef'ûlüdür»",
   "why": {"en": "A noun-verb governs exactly as the verb it means would; the object's naṣb is its work.", "tr": "Fiil ismi, manasındaki fiil nasıl amel ederse öyle amel eder; mef'ûlün nasbı onun işidir."}},
  {"wrong": "«قَطَامِ kesre ile mecrûrdur: مَرَرْتُ بِقَطَامِ»",
   "right": "«قَطَامِ Hicazlılara göre her hâlde kesr üzere mebnîdir; Temîm'e göre gayr-i munsarif: بِقَطَامَ»",
   "why": {"en": "The kasra is a building vowel for the Ḥijāzīs (ʿadl + wazn like نَزَالِ) and a fatḥa of the diptote for Tamīm; it is never the kasra of jarr.", "tr": "Kesre Hicazlılara göre bina harekesidir (نَزَالِ gibi adl + vezin), Temîm'e göre gayr-i munsarifin fethasıdır; cer kesresi asla değildir."}},
  {"wrong": "«اثْنَا عَشَرَ — iki cüz' de mebnîdir, on beş gibi»",
   "right": "«اثْنَا عَشَرَ / اثْنَيْ عَشَرَ — birinci cüz' tesniye gibi i'râblanır, yalnız عَشَرَ mebnîdir»",
   "why": {"en": "The nūn of اثْنَانِ drops before عَشَرَ exactly as before a muḍāf ilayh, so the first part keeps the dual's letters of iʿrāb.", "tr": "اثْنَانِ'nin nûnu عَشَرَ'den önce tam bir muzâfun ileyh önündeki gibi düşer; birinci cüz' tesniyenin i'râb harflerini korur."}},
  {"wrong": "«بَعْلَبَكَّ — ikisi de mebnîdir, çünkü mürekkebdir»",
   "right": "«بَعْلَبَكَّ — ba'le feth üzere mebnî, bekke gayr-i munsarif olarak mu'rebdir: مَرَرْتُ بِبَعْلَبَكَّ»",
   "why": {"en": "Only a second part that carries a letter builds both halves; here none is carried, so the second half declines as a diptote.", "tr": "Yalnız harf taşıyan ikinci cüz' iki yarıyı mebnî kılar; burada harf taşınmaz, ikinci yarı gayr-i munsarif olarak mu'rebdir."}}],
 "relatedNotes": [K3, AF, "mamnu-min-sarf", "al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar", "vocative-munada", "al-muthanna"]}

ADD_EN = (" Chapter 6 (notebook lines ~189-190): the three definitions in the notebook's own Arabic (s1 the noun-verbs, s7 the sounds, s9 the compounds) with every "
          "example it gives; the rulings on فَعَالِ, on the Ḥijāz/Tamīm disagreement and on the compounds restored from the received matn and marked (s2-s6, s8, s10-s12); "
          "the notebook's reason for building both parts as commentary (s13).")
ADD_TR = (" Altıncı bâb (defter satırları ~189-190): üç tarif defterin kendi Arapçasıyla (s1 fiil isimleri, s7 sesler, s9 mürekkebler) ve verdiği her örnek; فَعَالِ, "
          "Hicaz/Temîm ihtilâfı ve mürekkebler hükümleri alınan metinden geri yazılmış ve işaretlenmiştir (s2-s6, s8, s10-s12); iki cüz'ün mebnî kılınma gerekçesi şerh olarak (s13).")
write_out(6, S, TITLE, ADD_EN, ADD_TR, "189-190", GLOSS_ADD, notes=(NOTE,),
          related=((K3, [K]), (AF, [K]), ("al-mabni-al-lazim-al-murakkab-al-adadi-wa-bayta-bayta-wa-ithna-ashar", [K])))
report(6, S, GLOSS_ADD, (NOTE,))
