# -*- coding: utf-8 -*-
"""Al-Kafiya — chapter 4: WHERE THE DETACHED PRONOUN STANDS, and the pronouns of separation and of the matter. The six things that make
the attached impossible (the pronoun fronted before its governor, the separation for a purpose, the dropped governor, the maʿnawī
governor, the particle governor with a rafʿ pronoun, the ṣifa running on other than its owner), two pronouns meeting (أَعْطَيْتُكَهُ /
أَعْطَيْتُكَ إِيَّاهُ; أَعْطَيْتُهُ إِيَّاهُ), the khabar of kāna's bāb (كُنْتُ إِيَّاهُ), لَوْلَا and عَسَى with the khilāf on لَوْلَاكَ and عَسَاكَ, the nūn of
protection (obligatory, optional, preferred), the faṣl pronoun with its condition and the khilāf on its maḥall, and the pronoun of the matter
with its obligatory omission after the lightened أَنْ.
Source: the Ottoman notebook (Ziya Sungur-oglu), lines ~164-173 of the transcription.

  RESTORED (the notebook carries this ruling only in Turkish; the received matn of the Kafiya is written and marked): s1, s2, s3, s4, s5, s6, s8, s9, s10, s11, s12, s13.
  COMMENTARY (the teacher's or the grammarians' explanation, not the matn): s7 — marked C_EN/C_TR.
  DRY_PKG=<copy> DRY_GR=<copy> python3 tools/authoring/author_kafiya_ch4.py
"""
import json, os, sys, pathlib, unicodedata
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"
K3 = "al-mabni-wal-mudmar"
PRON = "al-marifa-al-mudmarat-wal-alam"
FASL = "damir-fasl"
WIQ = "ya-al-mutakallim"
TITLE = {"ar": "مَوَاضِعُ الْمُنْفَصِلِ، وَضَمِيرُ الْفَصْلِ وَالشَّأْنِ", "en": "Where the detached pronoun stands; the pronouns of separation and of the matter", "tr": "Munfasılın yerleri; fasl ve şan zamirleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
R_EN = " (Restored: the notebook carries this ruling only in Turkish; this is the received matn of the Kafiya.)"
R_TR = " (Geri yazım: defter bu hükmü yalnız Türkçe taşır; bu, Kâfiye'nin alınan metnidir.)"

def N(s): return unicodedata.normalize("NFC", s)
def pr1s(): return seg("نِي", "pron-1s-obj", "pron")
def pr1sy(): return seg("ي", "pron-1s", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
def pr2ms(): return seg("كَ", "pron-2ms", "pron")
def prT(form="تُ"): return seg(form, "pron-1s", "pron")
def prTa(): return seg("تَ", "pron-2ms", "pron")
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
def bi_(full, lex, pos, tags, ar, en, tr, inner, punct=None, wa=False):
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg("بِ", "bi", "prep"), seg(inner, lex, pos)]
    return W(full, lex, pos, ["huruf-jarr"] + tags, ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "الْبَاءُ حَرْفُ جَرٍّ، وَ" + ar, en, tr, punct=punct, segments=segs)
def zayd(punct=None, kase="raf"):
    full = {"raf": "زَيْدٌ", "nasb": "زَيْدًا", "jarr": "زَيْدٍ"}[kase]
    return W(full, "zayd", "propn", ["fail" if kase == "raf" else "maful-bihi"], "", "", "", punct=punct)
def quoted(full, lex, pos, tags, ar, en, tr, punct=None, segments=None):
    return W(full, lex, pos, tags, "لَفْظٌ مَحْكِيٌّ — " + ar, en, tr, punct=punct, segments=segments)

# ----------- s1 (RESTORED): the first three excuses
S.append({"id": "s1", "translation": {
 "en": "And the attached becomes impossible through six things: by the pronoun being fronted before its governor, as in «you alone did I beat»; by a separation for a purpose, as in «none beat you but I»; by the governor being dropped, as in «beware of evil»." + R_EN,
 "tr": "Muttasıl altı şeyle imkânsız olur: zamirin âmilinden öne alınmasıyla, «iyyâke darabtü» gibi; bir garaz için yapılan fasl ile, «mâ darabeke illâ ene» gibi; âmilin hazfiyle, «iyyâke ve'ş-şerre» gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَتَعَذَّرُ", "taadhdhara", "verb", ["fail", "form-v-verbs"], "يَتَعَذَّرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and becomes impossible».", "«ve imkânsız olur».", "يَتَعَذَّرُ"),
  W("الْمُتَّصِلُ", "muttasil", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the attached» — the doer.", "«muttasıl» — fâil."),
  bi_("بِسِتَّةِ", "sitta", "noun", ["idafa-definiteness"], "سِتَّةِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«through six».", "«altı ile».", "سِتَّةِ"),
  W("أَشْيَاءَ", "shay", "noun", ["idafa-definiteness", "mamnu-min-sarf", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«things» — the diptote plural, jarr by the fatḥa.", "«şey» — gayr-i munsarif, fetha ile mecrûr.", punct=":"),
  bi_("بِتَقْدِيمِ", "taqdim", "noun", ["idafa-definiteness", "masdar"], "تَقْدِيمِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — بَدَلٌ مِنْ بِسِتَّةِ.", "«by the fronting of» — the first of the six.", "«öne alınmasıyla» — altının ilki.", "تَقْدِيمِ"),
  W("الضَّمِيرِ", "damir", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the pronoun».", "«zamirin»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«before».", "«-den önce»."),
  W("عَامِلِهِ", "amil", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its governor».", "«âmilinden».", segments=[seg("عَامِلِ", "amil", "noun"), pr3msi()]),
  nahwu(punct=None),
  quoted("إِيَّاكَ", "iyya", "pron", ["idafa-definiteness", "maful-bihi", PRON, "qasr"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ؛ وَفِي الْمِثَالِ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«you alone» — the fronted object: the pronoun cannot attach to a verb that comes after it.", "«yalnız seni» — öne alınmış mef'ûl: zamir, sonra gelen fiile bitişemez.", segments=[seg("إِيَّا", "iyya", "pron"), pr2ms()]),
  W("ضَرَبْتُ", "daraba", "verb", ["fail", PRON], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I beat».", "«dövdüm».", punct="،", segments=[seg("ضَرَبْ", "daraba", "verb"), prT()]),
  bi_("وَبِالْفَصْلِ", "fasl", "noun", ["masdar"], "الْفَصْلِ مَجْرُورٌ بِالْكَسْرَةِ — مَعْطُوفٌ عَلَى بِتَقْدِيمِ.", "«and by the separation».", "«ve fasl ile».", "الْفَصْلِ", wa=True),
  W("لِغَرَضٍ", "gharad", "noun", ["huruf-jarr", "lam-taleel"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَغَرَضٍ مَجْرُورٌ بِالْكَسْرَةِ.", "«for a purpose» — the qaṣr, the restriction.", "«bir garaz için» — kasr.", segments=[seg("لِ", "li", "prep"), seg("غَرَضٍ", "gharad", "noun")]),
  nahwu(punct=None),
  quoted("مَا", "ma-nafiya", "part", ["idafa-definiteness", "la-nafiya", "qasr", "anwa-ma"], "فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ؛ وَفِي الْمِثَالِ حَرْفُ نَفْيٍ.", "«none» — the negation that, with إِلَّا, makes the restriction.", "«hiç» — illâ ile kasr yapan nefiy."),
  W("ضَرَبَكَ", "daraba", "verb", ["fail", "maful-bihi", PRON], "فِعْلٌ مَاضٍ، وَالْكَافُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُؤَخَّرٌ.", "«beat you» — the object attached, the doer delayed.", "«seni dövdü» — mef'ûl bitişik, fâil sonra.", segments=[seg("ضَرَبَ", "daraba", "verb"), pr2ms()]),
  W("إِلَّا", "illa", "part", ["istithna-mufarragh", "qasr"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«but».", "«ancak»."),
  W("أَنَا", "ana", "pron", ["fail", PRON, "istithna-mufarragh"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — انْفَصَلَ لِلْفَصْلِ بِإِلَّا.", "«I» — the doer, detached because إِلَّا separates it from the verb.", "«ben» — fâil, illâ ile fiilden ayrıldığı için munfasıl.", punct="،"),
  bi_("وَبِحَذْفِ", "hadhf", "noun", ["idafa-definiteness", "masdar"], "حَذْفِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — مَعْطُوفٌ.", "«and by the dropping of».", "«ve hazfiyle».", "حَذْفِ", wa=True),
  W("الْعَامِلِ", "amil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governor».", "«âmilin»."),
  nahwu(punct=None),
  quoted("إِيَّاكَ", "iyya", "pron", ["idafa-definiteness", "at-tahdhir", "hadhf-wa-taqdir"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ وُجُوبًا تَقْدِيرُهُ أُحَذِّرُ — التَّحْذِيرُ.", "«beware» — the object of a verb dropped of necessity («I warn you»): the taḥdhīr.", "«sakın» — vücûben hazfedilmiş bir fiilin mef'ûlü («seni uyarırım»): tahzîr.", segments=[seg("إِيَّا", "iyya", "pron"), pr2ms()]),
  atf_wa("وَالشَّرَّ", "sharr", "noun", ["at-tahdhir", "maful-bihi"], "الشَّرَّ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and evil» — joined in naṣb.", "«ve şerden» — nasb ile atıf.", "الشَّرَّ", punct="."),
 ]})

# ----------- s2 (RESTORED): the last three excuses
S.append({"id": "s2", "translation": {
 "en": "And by the governor being a meaning, as in «I am Zayd»; by its being a particle while the pronoun is in rafʿ, as in «you are not standing»; and by the ṣifa that runs on other than its owner being predicated of the pronoun, as in «Zayd — ʿAmr is his beater, he»." + R_EN,
 "tr": "Âmilin manevî olmasıyla, «ene Zeydün» gibi; harf olup zamirin merfû olmasıyla, «mâ ente kâimen» gibi; sahibinden başkası üzere cârî olan sıfatın zamire isnâdıyla, «Zeydün Amrun dâribühû hüve» gibi." + R_TR},
 "tokens": [
  bi_("وَبِكَوْنِ", "kawn", "noun", ["idafa-definiteness", "masdar"], "كَوْنِ مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ — مَعْطُوفٌ عَلَى مَا قَبْلَهُ.", "«and by the being of».", "«ve olmasıyla».", "كَوْنِ", wa=True),
  W("الْعَامِلِ", "amil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَصْدَرِ كَوْنِ.", "«the governor» — the maṣdar's subject.", "«âmilin» — masdarın ismi."),
  W("مَعْنَوِيًّا", "manawi", "noun", ["khabar-al-mubtada-wa-ahkamuh", "ism-mansub"], "خَبَرُ الْمَصْدَرِ كَوْنِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a meaning» — the maṣdar's khabar in naṣb.", "«manevî» — masdarın haberi, mansûb."),
  nahwu(punct=None),
  quoted("أَنَا", "ana", "pron", ["idafa-definiteness", "mubtada-khabar", "al-amil-al-manawi", PRON], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ مُبْتَدَأٌ، عَامِلُهُ الِابْتِدَاءُ الْمَعْنَوِيُّ.", "«I» — the mubtada: its governor, the ibtidāʾ, is no word, so nothing can attach.", "«ben» — mübtedâ: âmili ibtidâ olup lafız olmadığından bitişecek şey yoktur."),
  W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ.", "«Zayd» — the khabar.", "«Zeyd'im» — haber.", punct="،"),
  W("وَبِكَوْنِهِ", "kawn", "noun", ["atf-nasaq", "huruf-jarr", "idafa-definiteness", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَكَوْنِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَعْطُوفٌ.", "«and by its being».", "«ve olmasıyla».", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("كَوْنِ", "kawn", "noun"), pr3ms()]),
  W("حَرْفًا", "harf", "noun", ["khabar-al-mubtada-wa-ahkamuh"], "خَبَرُ الْمَصْدَرِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a particle».", "«harf»."),
  atf_wa("وَالضَّمِيرُ", "damir", "noun", ["mubtada-khabar", "hal"], "الْوَاوُ لِلْحَالِ، وَالضَّمِيرُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْجُمْلَةُ حَالٌ.", "«while the pronoun» — a ḥāl clause.", "«zamir ... iken» — hâl cümlesi.", "الضَّمِيرُ"),
  W("مَرْفُوعٌ", "marfu", "noun", ["mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«is in rafʿ».", "«merfû»."),
  nahwu(punct=None),
  quoted("مَا", "ma-nafiya", "part", ["idafa-definiteness", "ma-la-mushabbaha"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ مَا الْحِجَازِيَّةُ الْعَامِلَةُ عَمَلَ لَيْسَ.", "«not» — the Ḥijāzī مَا working like لَيْسَ.", "«değil» — leyse gibi amel eden Hicâzî mâ."),
  W("أَنْتَ", "anta", "pron", ["ma-la-mushabbaha", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُ مَا — لَا يَتَّصِلُ بِالْحَرْفِ.", "«you» — the ism of مَا: a rafʿ pronoun cannot attach to a particle.", "«sen» — mâ'nın ismi: merfû zamir harfe bitişmez."),
  W("قَائِمًا", "qaim", "noun", ["ma-la-mushabbaha", "ism-fail"], "خَبَرُ مَا مَنْصُوبٌ بِالْفَتْحَةِ.", "«standing» — the khabar of مَا in naṣb.", "«ayakta» — mâ'nın haberi, mansûb.", punct="،"),
  bi_("وَبِإِسْنَادِ", "isnad", "noun", ["idafa-definiteness", "masdar"], "إِسْنَادِ مَجْرُورٌ، وَهُوَ مُضَافٌ — مَعْطُوفٌ.", "«and by the predication of».", "«ve isnâdıyla».", "إِسْنَادِ", wa=True),
  W("الصِّفَةِ", "sifa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the ṣifa».", "«sıfatın»."),
  W("الْجَارِيَةِ", "jariya", "noun", ["naat-sifa", "ism-fail"], "صِفَةٌ لِلصِّفَةِ مَجْرُورَةٌ.", "«that runs».", "«cârî olan»."),
  W("عَلَى", "ala", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzere»."),
  W("غَيْرِ", "ghayr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«other than».", "«başkası»."),
  W("مَنْ", "man", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«the one who» — the relative.", "«kimse» — mevsûl."),
  W("هِيَ", "hiya", "pron", ["ism-mawsul", "mubtada-khabar", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ صِلَةٌ.", "«it» — the mubtada of the ṣila.", "«o» — sılanın mübtedâsı."),
  W("لَهُ", "li", "prep", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«belongs» — the jarr phrase as khabar.", "«ona âit» — câr-mecrûr haber.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  W("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«to».", "«-e»."),
  W("الضَّمِيرِ", "damir", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the pronoun».", "«zamire»."),
  nahwu(punct=None),
  quoted("زَيْدٌ", "zayd", "propn", ["idafa-definiteness", "mubtada-khabar"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ مُبْتَدَأٌ أَوَّلُ.", "«Zayd» — the first mubtada.", "«Zeyd» — birinci mübtedâ."),
  W("عَمْرٌو", "amr-name", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.", "«ʿAmr» — the second mubtada.", "«Amr» — ikinci mübtedâ."),
  W("ضَارِبُهُ", "darib", "noun", ["mubtada-khabar", "ism-fail", "idafa-definiteness"], "خَبَرُ الْمُبْتَدَإِ الثَّانِي مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — صِفَةٌ جَارِيَةٌ عَلَى عَمْرٍو وَهِيَ لِزَيْدٍ.", "«his beater» — the khabar; a ṣifa running on ʿAmr while it belongs to Zayd.", "«onu dövücüsü» — haber; Amr üzere cârî, Zeyd'e âit sıfat.", segments=[seg("ضَارِبُ", "darib", "noun"), pr3ms()]),
  W("هُوَ", "huwa", "pron", ["fail", PRON, "ism-fail"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ لِضَارِبٍ — أُبْرِزَ لِئَلَّا يَلْتَبِسَ.", "«he» — the doer of ضَارِب, detached so that the beater is not mistaken for ʿAmr.", "«o» — dâribin fâili; dövenin Amr sanılmaması için açığa çıkarıldı.", punct="."),
 ]})

# ----------- s3 (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And when two pronouns meet and neither is in rafʿ, if the more definite is put first you are free in the second, as in «I gave you it» and «I gave you — it»." + R_EN,
 "tr": "İki zamir bir araya gelip biri merfû olmazsa, daha ma'rife olanı öne alınırsa ikincisinde muhayyersin, «a'taytükehû» ve «a'taytüke iyyâhü» gibi." + R_TR},
 "tokens": [
  W("وَإِذَا", "idha", "part", ["idha-shartiyya"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when».", "«ve ... zaman».", segments=[seg("وَ", "wa", "conj"), seg("إِذَا", "idha", "part")]),
  W("اِجْتَمَعَ", "ijtamaa", "verb", ["idha-shartiyya", "form-viii-verbs", "fail"], "فِعْلٌ مَاضٍ، فِعْلُ الشَّرْطِ.", "«meet».", "«bir araya gelir»."),
  W("ضَمِيرَانِ", "damir", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«two pronouns» — the doer, the dual on its alif.", "«iki zamir» — fâil, tesniye elifle."),
  atf_wa("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "hal"], "الْوَاوُ لِلْحَالِ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ.", "«while not» — لَيْسَ in a ḥāl clause.", "«... değilken» — leyse, hâl cümlesinde.", "لَيْسَ"),
  W("أَحَدُهُمَا", "ahad", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ لَيْسَ مَرْفُوعٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«one of the two» — the ism of لَيْسَ.", "«ikisinden biri» — leyse'nin ismi.", segments=[seg("أَحَدُ", "ahad", "noun"), pr3d()]),
  W("مَرْفُوعًا", "marfu", "noun", ["kana-wa-akhawatuha"], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«in rafʿ» — the khabar of لَيْسَ.", "«merfû» — leyse'nin haberi.", punct="،"),
  W("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-fa-fi-jawab-al-shart"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«then if» — the fāʾ of إِذَا's answer and a second condition.", "«o zaman eğer» — izâ'nın cevabının fâ'sı ve ikinci şart.", segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  W("قُدِّمَ", "qaddama", "verb", ["in-shartiyya", "naib-al-fail", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.", "«is put first» — the passive, the condition's verb.", "«öne alınırsa» — meçhul, şart fiili."),
  W("الْأَعْرَفُ", "arafu", "noun", ["naib-al-fail", "ism-tafdil"], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ — أَفْعَلُ تَفْضِيلٍ: الْمُتَكَلِّمُ أَعْرَفُ مِنَ الْمُخَاطَبِ، وَالْمُخَاطَبُ أَعْرَفُ مِنَ الْغَائِبِ.", "«the more definite» — the deputy doer: the speaker outranks the addressee, the addressee the absent.", "«daha ma'rife olan» — nâib-i fâil: mütekellim muhâtabdan, muhâtab gâibden daha ma'rifedir."),
  W("خُيِّرْتَ", "khayyara", "verb", ["in-shartiyya", "naib-al-fail", "form-ii-verbs", "al-majzum-wal-shart-wal-jaza"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالتَّاءُ نَائِبُ الْفَاعِلِ.", "«you are given the choice» — the answer; the tāʾ its deputy doer.", "«muhayyer kılınırsın» — cevap; tâ nâib-i fâil.", segments=[seg("خُيِّرْ", "khayyara", "verb"), prTa()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الثَّانِي", "thani", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second» — a manqūṣ.", "«ikincisinde» — mankûs.", punct="،"),
  nahwu(punct=None),
  quoted("أَعْطَيْتُكَهُ", "aata", "verb", ["idafa-definiteness", "mafulayn", "fail", PRON], "فِي مَحَلِّ جَرٍّ؛ وَفِيهِ التَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ أَوَّلُ، وَالْهَاءُ مَفْعُولٌ ثَانٍ مُتَّصِلٌ.", "«I gave you it» — the tāʾ the doer, the kāf the first object, the hāʾ the second — attached.", "«sana onu verdim» — tâ fâil, kâf birinci mef'ûl, hâ ikinci — muttasıl.", segments=[seg("أَعْطَيْ", "aata", "verb"), prT(), pr2ms(), pr3ms()]),
  atf_wa("وَأَعْطَيْتُكَ", "aata", "verb", ["mafulayn", "fail", PRON], "أَعْطَيْتُكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — التَّاءُ فَاعِلٌ وَالْكَافُ مَفْعُولٌ أَوَّلُ.", "«and I gave you».", "«ve sana verdim».", "أَعْطَيْ", extra_segs=[seg("أَعْطَيْ", "aata", "verb"), prT(), pr2ms()]),
  W("إِيَّاهُ", "iyya", "pron", ["mafulayn", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ — مُنْفَصِلٌ، وَكِلَاهُمَا جَائِزٌ.", "«it» — the second object detached; both are allowed.", "«onu» — ikinci mef'ûl munfasıl; ikisi de câiz.", punct=".", segments=[seg("إِيَّا", "iyya", "pron"), pr3ms()]),
 ]})

# ----------- s4 (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "Otherwise detachment is obligatory, as in «I gave him — it» and «I gave him — you»." + R_EN,
 "tr": "Aksi hâlde infisâl vâcibdir, «a'taytühû iyyâhü» ve «a'taytühû iyyâke» gibi." + R_TR},
 "tokens": [
  W("وَإِلَّا", "illa", "part", ["in-shartiyya", "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَإِلَّا: إِنْ الشَّرْطِيَّةُ وَلَا النَّافِيَةُ، وَفِعْلُ الشَّرْطِ مَحْذُوفٌ — وَإِنْ لَا يُقَدَّمِ الْأَعْرَفُ.", "«otherwise» — إِنْ + لَا with the condition's verb dropped.", "«aksi hâlde» — in + lâ, şart fiili hazfedilmiş.", segments=[seg("وَ", "wa", "conj"), seg("إِلَّا", "illa", "part")]),
  W("وَجَبَ", "wajaba", "verb", ["al-majzum-wal-shart-wal-jaza", "fail"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "«is obligatory» — the answer.", "«vâcib olur» — cevap."),
  W("الِانْفِصَالُ", "infisal", "noun", ["fail", "masdar", "form-vii-verbs"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«detachment» — the doer.", "«infisâl» — fâil.", punct="،"),
  nahwu(punct=None),
  quoted("أَعْطَيْتُهُ", "aata", "verb", ["idafa-definiteness", "mafulayn", "fail", PRON], "فِي مَحَلِّ جَرٍّ؛ وَفِيهِ التَّاءُ فَاعِلٌ وَالْهَاءُ مَفْعُولٌ أَوَّلُ.", "«I gave him».", "«ona verdim».", segments=[seg("أَعْطَيْ", "aata", "verb"), prT(), pr3ms()]),
  W("إِيَّاهُ", "iyya", "pron", ["mafulayn", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ — وَجَبَ انْفِصَالُهُ لِأَنَّ الْغَائِبَيْنِ لَيْسَ أَحَدُهُمَا أَعْرَفَ.", "«it» — detached of necessity: neither absent pronoun is more definite than the other.", "«onu» — vücûben munfasıl: iki gâibden biri diğerinden daha ma'rife değildir.", segments=[seg("إِيَّا", "iyya", "pron"), pr3ms()]),
  atf_wa("وَأَعْطَيْتُهُ", "aata", "verb", ["mafulayn", "fail", PRON], "أَعْطَيْتُهُ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and I gave him».", "«ve ona verdim».", "أَعْطَيْ", extra_segs=[seg("أَعْطَيْ", "aata", "verb"), prT(), pr3ms()]),
  W("إِيَّاكَ", "iyya", "pron", ["mafulayn", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ — وَجَبَ انْفِصَالُهُ لِأَنَّ الْأَعْرَفَ لَمْ يُقَدَّمْ.", "«you» — detached of necessity: the more definite was not put first.", "«seni» — vücûben munfasıl: daha ma'rife olan öne alınmadı.", punct=".", segments=[seg("إِيَّا", "iyya", "pron"), pr2ms()]),
 ]})

# ----------- s5 (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "And the khabar of kāna's bāb, when it is a pronoun, may attach, and the preferred is its detachment, as in «Zayd was standing, and I was — he»." + R_EN,
 "tr": "Kâne bâbının haberi zamir olunca bitişmesi câiz, munfasıl olması muhtârdır; «kâne Zeydün kâimen ve küntü iyyâhü» gibi." + R_TR},
 "tokens": [
  atf_wa("وَخَبَرُ", "khabar", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the khabar of» — the mubtada.", "«ve haberi» — mübtedâ.", "خَبَرُ"),
  W("بَابِ", "bab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the bāb of».", "«bâbının»."),
  W("كَانَ", "kana", "verb", ["idafa-definiteness", "kana-wa-akhawatuha"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«kāna» — cited, annexed.", "«kâne» — hikâye, muzâfun ileyh."),
  W("إِذَا", "idha", "part", ["idha-shartiyya"], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when».", "«-ince»."),
  W("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "idha-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ.", "«it is» — kāna, its ism concealed.", "«olunca» — kâne, ismi gizli."),
  W("ضَمِيرًا", "damir", "noun", ["kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a pronoun» — the khabar of kāna.", "«zamir» — kâne'nin haberi."),
  W("جَازَ", "jaaza", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ، جَوَابُ إِذَا، وَالْجُمْلَةُ الشَّرْطِيَّةُ خَبَرُ الْمُبْتَدَإِ.", "«is allowed» — the answer; the whole condition is the khabar of the mubtada.", "«câizdir» — cevap; şart cümlesi mübtedânın haberi."),
  W("اِتِّصَالُهُ", "ittisal", "noun", ["fail", "idafa-definiteness", "masdar"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its attaching» — the doer.", "«bitişmesi» — fâil.", segments=[seg("اِتِّصَالُ", "ittisal", "noun"), pr3ms()]),
  atf_wa("وَالْمُخْتَارُ", "mukhtar", "noun", ["mubtada-khabar", "ism-maful"], "الْمُخْتَارُ مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ اخْتَارَ.", "«and the preferred» — the mubtada.", "«ve muhtâr olan» — mübtedâ.", "الْمُخْتَارُ"),
  W("اِنْفِصَالُهُ", "infisal", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its detachment» — the khabar.", "«munfasıl olması» — haber.", punct="،", segments=[seg("اِنْفِصَالُ", "infisal", "noun"), pr3ms()]),
  nahwu(punct=None),
  quoted("كَانَ", "kana", "verb", ["idafa-definiteness", "kana-wa-akhawatuha"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ فِعْلٌ مَاضٍ نَاقِصٌ.", "«was».", "«idi»."),
  W("زَيْدٌ", "zayd", "propn", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«Zayd» — the ism of kāna.", "«Zeyd» — kâne'nin ismi."),
  W("قَائِمًا", "qaim", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ.", "«standing» — its khabar.", "«ayakta» — haberi."),
  atf_wa("وَكُنْتُ", "kana", "verb", ["kana-wa-akhawatuha", PRON], "كُنْتُ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ.", "«and I was» — the tāʾ its ism.", "«ve ben idim» — tâ ismi.", "كُنْ", extra_segs=[seg("كُنْ", "kana", "verb"), prT()]),
  W("إِيَّاهُ", "iyya", "pron", ["kana-wa-akhawatuha", PRON], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ — وَيَجُوزُ كُنْتُهُ.", "«he» — the khabar of kāna detached; كُنْتُهُ is allowed too.", "«o» — kâne'nin haberi munfasıl; küntühû da câiz.", punct=".", segments=[seg("إِيَّا", "iyya", "pron"), pr3ms()]),
 ]})

# ----------- s6 (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And after لَوْلَا the detached, because what follows it is a mubtada, as in «were it not for you»; and after عَسَى the attached, because what follows it is a doer, as in «you may»." + R_EN,
 "tr": "Levlâ'dan sonra munfasıl gelir, çünkü sonrası mübtedâdır, «levlâ ente» gibi; asâ'dan sonra muttasıl gelir, çünkü sonrası fâildir, «aseyte» gibi." + R_TR},
 "tokens": [
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ خَبَرٌ مُقَدَّمٌ، وَهُوَ مُضَافٌ.", "«and after» — the ẓarf, a fronted khabar.", "«ve ... sonra» — zarf, öne alınmış haber.", "بَعْدَ"),
  W("لَوْلَا", "lawla", "part", ["idafa-definiteness", "in-shartiyya"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«لَوْلَا» — cited.", "«levlâ» — hikâye."),
  W("الْمُنْفَصِلُ", "munfasil", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the detached» — the delayed mubtada.", "«munfasıl» — sonraya bırakılmış mübtedâ."),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("مَا", "ma-mawsula", "pron", ["inna-wa-akhawatuha", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«what» — the ism of أَنَّ.", "«... olan» — enne'nin ismi."),
  W("بَعْدَهَا", "bada", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةِ الْمَوْصُولِ الْمَحْذُوفَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«follows it» — the ṣila's ẓarf.", "«ondan sonra olan» — sılanın zarfı.", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("مُبْتَدَأٌ", "mubtada", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is a mubtada» — the khabar of أَنَّ.", "«mübtedâdır» — enne'nin haberi.", punct="،"),
  nahwu(punct=None),
  quoted("لَوْلَا", "lawla", "part", ["idafa-definiteness", "in-shartiyya"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ حَرْفُ امْتِنَاعٍ لِوُجُودٍ.", "«were it not for».", "«olmasaydı»."),
  W("أَنْتَ", "anta", "pron", ["mubtada-khabar", PRON, "hadhf-wa-taqdir"], "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، خَبَرُهُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ مَوْجُودٌ.", "«you» — the mubtada; its khabar dropped of necessity («present»).", "«sen» — mübtedâ; haberi vücûben hazfedilmiş («mevcûd»).", punct="،"),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "بَعْدَ ظَرْفٌ خَبَرٌ مُقَدَّمٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("عَسَى", "asa-hope", "verb", ["idafa-definiteness", "afal-al-muqaraba"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«عَسَى» — cited.", "«asâ» — hikâye."),
  W("الْمُتَّصِلُ", "muttasil", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the attached».", "«muttasıl»."),
  W("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«because».", "«çünkü».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part")]),
  W("مَا", "ma-mawsula", "pron", ["inna-wa-akhawatuha", "ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«what».", "«... olan»."),
  W("بَعْدَهَا", "bada", "noun", ["ism-mawsul", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«follows it».", "«ondan sonra olan».", segments=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("فَاعِلٌ", "fail-doer", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is a doer».", "«fâildir».", punct="،"),
  nahwu(punct=None),
  quoted("عَسَيْتَ", "asa-hope", "verb", ["idafa-definiteness", "afal-al-muqaraba", PRON], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ عَسَى فِعْلٌ جَامِدٌ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فَاعِلٌ.", "«you may» — the tāʾ its doer, attached.", "«ola ki sen» — tâ fâil, muttasıl.", punct=".", segments=[seg("عَسَيْ", "asa-hope", "verb"), prTa()]),
 ]})

# ----------- s7 (COMMENTARY: the khilaf)
S.append({"id": "s7", "translation": {
 "en": "And «were it not for you» and «you may» have come with the attached: for al-Akhfash the pronoun after لَوْلَا is in jarr in the place of rafʿ and after عَسَى in naṣb in the place of rafʿ; for Sībawayh لَوْلَا is a jarr letter and عَسَى is like لَعَلَّ." + C_EN,
 "tr": "«Levlâke» ve «asâke» de gelmiştir: Ahfeş'e göre levlâ'dan sonraki zamir ref' mahallinde mecrûr, asâ'dan sonraki ref' mahallinde mansûbdur; Sîbeveyh'e göre levlâ harf-i cer, asâ ise leâlle gibidir." + C_TR},
 "tokens": [
  W("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed».", "«ve gerçekten».", segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  W("جَاءَ", "jaa", "verb", ["fail", "hollow-verbs"], "فِعْلٌ مَاضٍ.", "«has come».", "«gelmiştir»."),
  W("لَوْلَاكَ", "lawla", "part", ["fail", PRON], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — لَوْلَا وَالْكَافُ مُتَّصِلَةٌ بِهَا.", "«were it not for you» — cited as the doer; the kāf attached to لَوْلَا.", "«levlâke» — fâil olarak hikâye; kâf levlâ'ya bitişik.", segments=[seg("لَوْلَا", "lawla", "part"), pr2ms()]),
  atf_wa("وَعَسَاكَ", "asa-hope", "verb", ["fail", PRON, "afal-al-muqaraba"], "عَسَاكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — عَسَى وَالْكَافُ مُتَّصِلَةٌ بِهَا.", "«and you may» — the kāf attached to عَسَى.", "«ve asâke» — kâf asâ'ya bitişik.", "عَسَا", punct="،", extra_segs=[seg("عَسَا", "asa-hope", "verb"), pr2ms()]),
  W("فَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "الْفَاءُ لِلتَّفْرِيعِ، وَعِنْدَ ظَرْفٌ مَنْصُوبٌ خَبَرٌ مُقَدَّمٌ، وَهُوَ مُضَافٌ.", "«so for» — the fronted khabar.", "«... göre» — öne alınmış haber.", segments=[seg("فَ", "fa", "conj"), seg("عِنْدَ", "inda", "noun")]),
  W("الْأَخْفَشِ", "akhfash", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Akhfash».", "«Ahfeş»."),
  W("الضَّمِيرُ", "damir", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the pronoun» — the mubtada.", "«zamir» — mübtedâ."),
  W("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«after».", "«... sonra»."),
  W("لَوْلَا", "lawla", "part", ["idafa-definiteness"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«لَوْلَا».", "«levlâ»."),
  W("مَجْرُورٌ", "majrur", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«is in jarr» — the khabar.", "«mecrûrdur» — haber."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallinde»."),
  W("رَفْعٍ", "raf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rafʿ».", "«ref'»."),
  atf_wa("وَبَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and after».", "«ve ... sonra».", "بَعْدَ"),
  W("عَسَى", "asa-hope", "verb", ["idafa-definiteness"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«عَسَى».", "«asâ»."),
  W("مَنْصُوبٌ", "mansub", "noun", ["mubtada-khabar", "ism-maful"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — أَيِ الضَّمِيرُ مَنْصُوبٌ.", "«is in naṣb».", "«mansûbdur»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("مَحَلِّ", "mahall", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the place of».", "«mahallinde»."),
  W("رَفْعٍ", "raf", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«rafʿ».", "«ref'».", punct="؛"),
  atf_wa("وَعِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "khabar-al-mubtada-wa-ahkamuh"], "عِنْدَ ظَرْفٌ مَنْصُوبٌ خَبَرٌ مُقَدَّمٌ، وَهُوَ مُضَافٌ.", "«and for».", "«ve ... göre».", "عِنْدَ"),
  W("سِيبَوَيْهِ", "sibawayh", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ — مُرَكَّبٌ مَخْتُومٌ بِوَيْهِ.", "«Sībawayh» — mabni on the kasr: a compound ending in -wayhi.", "«Sîbeveyh» — kesr üzere mebnî: veyh ile biten mürekkeb."),
  W("لَوْلَا", "lawla", "part", ["mubtada-khabar"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«لَوْلَا» — the mubtada.", "«levlâ» — mübtedâ."),
  W("حَرْفُ", "harf", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«is a letter of».", "«harfidir»."),
  W("جَرٍّ", "jarr", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«jarr».", "«cer»."),
  atf_wa("وَعَسَى", "asa-hope", "verb", ["mubtada-khabar"], "عَسَى لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and عَسَى» — the mubtada.", "«ve asâ» — mübtedâ.", "عَسَى"),
  W("كَلَعَلَّ", "laalla", "part", ["huruf-jarr", "mubtada-khabar"], "الْكَافُ حَرْفُ جَرٍّ، وَلَعَلَّ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«is like لَعَلَّ» — the jarr phrase as khabar.", "«leâlle gibidir» — câr-mecrûr haber.", punct=".", segments=[seg("كَ", "ka", "prep"), seg("لَعَلَّ", "laalla", "part")]),
 ]})

# ----------- s8 (RESTORED)
S.append({"id": "s8", "translation": {
 "en": "And the nūn of protection is obligatory with the speaker's yāʾ in the past verb, as in «he beat me», and in the non-past free of the nūn of iʿrāb, as in «he beats me»." + R_EN,
 "tr": "Vikâye nûnu, mütekellim yâsıyla mâzîde lâzımdır, «darabenî» gibi; i'râb nûnundan hâlî muzâride de, «yadribünî» gibi." + R_TR},
 "tokens": [
  atf_wa("وَنُونُ", "nun-letter", "noun", ["mubtada-khabar", "idafa-definiteness", WIQ], "نُونُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and the nūn of» — the mubtada.", "«ve nûnu» — mübtedâ.", "نُونُ"),
  W("الْوِقَايَةِ", "wiqaya", "noun", ["idafa-definiteness", WIQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَقِي الْفِعْلَ مِنَ الْكَسْرِ.", "«protection» — it guards the verb from the kasra.", "«vikâye» — fiili kesreden korur."),
  W("لَازِمَةٌ", "lazim", "noun", ["mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«obligatory» — the khabar.", "«lâzımdır» — haber."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("يَاءِ", "ya-letter", "noun", ["idafa-definiteness", WIQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the yāʾ of».", "«yâsı»."),
  W("الْمُتَكَلِّمِ", "mutakallim", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker».", "«mütekellimin»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمَاضِي", "madi", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the past verb».", "«mâzîde»."),
  nahwu(punct=None),
  quoted("ضَرَبَنِي", "daraba", "verb", ["idafa-definiteness", "maful-bihi", WIQ], "فِي مَحَلِّ جَرٍّ؛ وَفِيهِ النُّونُ لِلْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.", "«he beat me» — the nūn guards, the yāʾ is the object.", "«beni dövdü» — nûn korur, yâ mef'ûl.", punct="،", segments=[seg("ضَرَبَ", "daraba", "verb"), pr1s()]),
  W("وَفِي", "fi", "prep", ["huruf-jarr", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in».", "«ve -de».", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")]),
  W("الْمُضَارِعِ", "mudari", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the non-past».", "«muzâride»."),
  W("الْخَالِي", "khali", "noun", ["naat-sifa", "ism-maqsur-manqus", "ism-fail"], "صِفَةٌ لِلْمُضَارِعِ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«free» — its naʿt, a manqūṣ.", "«hâlî olan» — sıfat, mankûs."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  W("نُونِ", "nun-letter", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnundan»."),
  W("الْإِعْرَابِ", "irab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نُونُ الرَّفْعِ فِي الْأَفْعَالِ الْخَمْسَةِ.", "«iʿrāb» — the rafʿ nūn of the five verbs.", "«i'râb» — beş fiilin ref' nûnu."),
  nahwu(punct=None),
  quoted("يَضْرِبُنِي", "daraba", "verb", ["idafa-definiteness", "maful-bihi", WIQ], "فِي مَحَلِّ جَرٍّ؛ وَفِيهِ النُّونُ لِلْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.", "«he beats me».", "«beni döver».", punct=".", segments=[seg("يَضْرِبُ", "daraba", "verb"), pr1s()]),
 ]})

# ----------- s9 (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "And you are free with the nūn of iʿrāb, with لَدُنْ and with إِنَّ and its sisters, as in «they two beat me» both ways and «indeed I» both ways; and the preferred is keeping it in لَيْتَ، مِنْ، عَنْ، قَدْ and قَطْ, and dropping it in لَعَلَّ." + R_EN,
 "tr": "İ'râb nûnuyla, ledün ile, inne ve kardeşleriyle muhayyersin, «yadribâninî / yadribânî» ve «innenî / innî» gibi; leyte, min, an, kad ve kat'ta isbâtı, leâlle'de hazfi muhtârdır." + R_TR},
 "tokens": [
  atf_wa("وَأَنْتَ", "anta", "pron", ["mubtada-khabar", PRON], "أَنْتَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and you» — the mubtada.", "«ve sen» — mübtedâ.", "أَنْتَ"),
  W("مُخَيَّرٌ", "mukhayyar", "noun", ["mubtada-khabar", "ism-maful", "form-ii-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ خَيَّرَ.", "«free to choose» — the khabar.", "«muhayyer» — haber."),
  W("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("نُونِ", "nun-letter", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ مُضَافٌ.", "«the nūn of».", "«nûnu»."),
  W("الْإِعْرَابِ", "irab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«iʿrāb».", "«i'râb»."),
  atf_wa("وَلَدُنْ", "ladun", "noun", ["idafa-definiteness"], "لَدُنْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ عَلَى نُونِ — ظَرْفٌ مَبْنِيٌّ.", "«and لَدُنْ».", "«ve ledün».", "لَدُنْ"),
  atf_wa("وَإِنَّ", "inna", "part", ["idafa-definiteness", "inna-wa-akhawatuha"], "إِنَّ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and إِنَّ».", "«ve inne».", "إِنَّ"),
  atf_wa("وَأَخَوَاتِهَا", "ukht", "noun", ["idafa-definiteness", "jam-muannath-salim"], "أَخَوَاتِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، وَهَا مُضَافٌ إِلَيْهِ.", "«and its sisters».", "«ve kardeşleriyle».", "أَخَوَاتِ", punct="،", extra_segs=[seg("أَخَوَاتِ", "ukht", "noun"), pr3fs()]),
  nahwu(punct=None),
  quoted("يَضْرِبَانِنِي", "daraba", "verb", ["idafa-definiteness", "afal-khamsa", WIQ], "فِي مَحَلِّ جَرٍّ؛ وَفِيهِ نُونُ الرَّفْعِ ثُمَّ نُونُ الْوِقَايَةِ ثُمَّ الْيَاءُ.", "«they two beat me» — the rafʿ nūn, then the wiqāya nūn, then the yāʾ.", "«ikisi beni döver» — ref' nûnu, vikâye nûnu, yâ.", segments=[seg("يَضْرِبَانِ", "daraba", "verb"), pr1s()]),
  atf_wa("وَيَضْرِبَانِي", "daraba", "verb", ["afal-khamsa", WIQ], "يَضْرِبَانِي لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — أُدْغِمَتِ النُّونُ فِي النُّونِ.", "«and they two beat me» — one nūn merged into the other.", "«ve ikisi beni döver» — nûn nûna idgam edildi.", "يَضْرِبَانِ", punct="،", extra_segs=[seg("يَضْرِبَانِ", "daraba", "verb"), pr1sy()]),
  atf_wa("وَإِنَّنِي", "inna", "part", ["inna-wa-akhawatuha", WIQ], "إِنَّنِي لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — إِنَّ وَنُونُ الْوِقَايَةِ وَالْيَاءُ اسْمُهَا.", "«and indeed I» — with the wiqāya nūn.", "«ve gerçekten ben» — vikâye nûnuyla.", "إِنَّ", extra_segs=[seg("إِنَّ", "inna", "part"), pr1s()]),
  atf_wa("وَإِنِّي", "inna", "part", ["inna-wa-akhawatuha", WIQ], "إِنِّي لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — بِلَا نُونِ وِقَايَةٍ.", "«and indeed I» — without it.", "«ve gerçekten ben» — nûnsuz.", "إِنِّ", punct="؛", extra_segs=[seg("إِنِّ", "inna", "part"), pr1sy()]),
  atf_wa("وَالْمُخْتَارُ", "mukhtar", "noun", ["mubtada-khabar"], "الْمُخْتَارُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the preferred» — the mubtada.", "«ve muhtâr olan» — mübtedâ.", "الْمُخْتَارُ"),
  W("إِثْبَاتُهَا", "ithbat", "noun", ["mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«keeping it» — the khabar.", "«isbâtı» — haber.", segments=[seg("إِثْبَاتُ", "ithbat", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("لَيْتَ", "layta", "part", ["huruf-jarr", "inna-wa-akhawatuha"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«لَيْتَ».", "«leyte»."),
  atf_wa("وَمِنْ", "min", "prep", ["huruf-jarr"], "مِنْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and مِنْ».", "«ve min».", "مِنْ"),
  atf_wa("وَعَنْ", "an", "prep", ["huruf-jarr"], "عَنْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ.", "«and عَنْ».", "«ve an».", "عَنْ"),
  atf_wa("وَقَدْ", "qad", "part", ["qad-harf"], "قَدْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — قَدْ الِاسْمِيَّةُ بِمَعْنَى حَسْبُ.", "«and قَدْ» — the noun قَدْ meaning «enough».", "«ve kad» — hasbü manasına isim olan kad.", "قَدْ"),
  atf_wa("وَقَطْ", "qat-hasb", "noun", [], "قَطْ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — بِمَعْنَى حَسْبُ.", "«and قَطْ» — «enough».", "«ve kat» — «yeter».", "قَطْ", punct="،"),
  atf_wa("وَحَذْفُهَا", "hadhf", "noun", ["mubtada-khabar", "idafa-definiteness", "masdar"], "حَذْفُ مَعْطُوفٌ عَلَى إِثْبَاتُهَا مَرْفُوعٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and dropping it».", "«ve hazfi».", "حَذْفُ", extra_segs=[seg("حَذْفُ", "hadhf", "noun"), pr3fs()]),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("لَعَلَّ", "laalla", "part", ["huruf-jarr", "inna-wa-akhawatuha"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ.", "«لَعَلَّ».", "«leâlle».", punct="."),
 ]})

# ----------- s10 (RESTORED): the fasl pronoun
S.append({"id": "s10", "translation": {
 "en": "And between the mubtada and the khabar, before the governors and after them, there stands the form of the detached rafʿ pronoun agreeing with the mubtada; it is called a separator, because it separates the khabar from the ṣifa — as in «Zayd, he is the standing one» and «You were the watcher over them»." + R_EN,
 "tr": "Mübtedâ ile haber arasına, âmillerden önce ve sonra, mübtedâya mutâbık merfû munfasıl sîgası girer; haberi sıfattan ayırdığı için ona fasl denir — «Zeydün hüve'l-kâimü» ve «künte ente'r-rakîbe» gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَقَعُ", "waqaa", "verb", ["fail", "mithal-verbs", FASL], "يَقَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and there stands».", "«ve vâki olur».", "يَقَعُ"),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«between».", "«arasına»."),
  W("الْمُبْتَدَإِ", "mubtada", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mubtada».", "«mübtedâ»."),
  atf_wa("وَالْخَبَرِ", "khabar", "noun", ["idafa-definiteness"], "الْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar».", "«ile haber».", "الْخَبَرِ", punct="،"),
  W("قَبْلَ", "qabla", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«before».", "«önce»."),
  W("الْعَوَامِلِ", "awamil", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governors».", "«âmillerden»."),
  atf_wa("وَبَعْدَهَا", "bada", "noun", ["maful-fih", "idafa-definiteness"], "بَعْدَ ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and after them».", "«ve sonra».", "بَعْدَ", punct="،", extra_segs=[seg("بَعْدَ", "bada", "noun"), pr3fs()]),
  W("صِيغَةُ", "sigha", "noun", ["fail", "idafa-definiteness", FASL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهُوَ مُضَافٌ.", "«the form of» — the doer.", "«sîgası» — fâil."),
  W("الْمَرْفُوعِ", "marfu", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the rafʿ».", "«merfû»."),
  W("الْمُنْفَصِلِ", "munfasil", "noun", ["naat-sifa"], "صِفَةٌ لِلْمَرْفُوعِ مَجْرُورَةٌ.", "«detached».", "«munfasıl»."),
  W("مُطَابِقَةً", "mutabiq", "noun", ["hal", "ism-fail", "form-iii-verbs"], "حَالٌ مِنْ صِيغَةُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«agreeing» — the ḥāl.", "«mutâbık olarak» — hâl."),
  W("لِلْمُبْتَدَإِ", "mubtada", "noun", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُبْتَدَإِ مَجْرُورٌ.", "«with the mubtada».", "«mübtedâya».", punct="،", segments=[seg("لِ", "li", "prep"), seg("الْمُبْتَدَإِ", "mubtada", "noun")]),
  atf_wa("وَتُسَمَّى", "samma", "verb", ["naib-al-fail", "mafulayn", "form-ii-verbs"], "تُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ.", "«and it is called» — the passive, its deputy concealed.", "«ve ... denir» — meçhul, nâib-i fâil gizli.", "تُسَمَّى"),
  W("فَصْلًا", "fasl", "noun", ["mafulayn", FASL], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a separator» — the second object.", "«fasl» — ikinci mef'ûl."),
  W("لِأَنَّهَا", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because it».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  W("تَفْصِلُ", "fasala", "verb", ["inna-wa-akhawatuha", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ هِيَ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«separates» — the khabar of أَنَّ.", "«ayırır» — enne'nin haberi."),
  W("الْخَبَرَ", "khabar", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the khabar» — the object.", "«haberi» — mef'ûl."),
  W("عَنِ", "an", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from».", "«-den»."),
  W("الصِّفَةِ", "sifa", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the ṣifa».", "«sıfattan».", punct="،"),
  nahwu(punct=None),
  quoted("زَيْدٌ", "zayd", "propn", ["idafa-definiteness", "mubtada-khabar"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ مُبْتَدَأٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  W("هُوَ", "huwa", "pron", [FASL, PRON], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "«he» — the faṣl pronoun, no maḥall.", "«o» — fasl zamiri, mahalli yok."),
  W("الْقَائِمُ", "qaim", "noun", ["mubtada-khabar", FASL], "خَبَرٌ مَرْفُوعٌ — لَوْلَا الْفَصْلُ لَاحْتُمِلَ أَنْ يَكُونَ صِفَةً.", "«the standing one» — the khabar; without the faṣl it could be read as a ṣifa.", "«ayakta olan» — haber; fasl olmasa sıfat sanılabilirdi.", punct="،"),
  W("وَكُنْتَ", "kana", "verb", ["kana-wa-akhawatuha", PRON, "al-iqtibas-wal-tadmin", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَكُنْتَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ.", "«and: You were» — kāna, the tāʾ its ism (al-Māʾida 5:117).", "«ve: sen idin» — kâne, tâ ismi (Mâide 5:117).", segments=[seg("وَ", "wa", "conj"), seg("كُنْ", "kana", "verb"), prTa()]),
  W("أَنْتَ", "anta", "pron", [FASL, PRON], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ — وَقَعَ بَعْدَ الْعَامِلِ.", "«You» — the faṣl pronoun, here after the governor.", "«sen» — fasl zamiri, burada âmilden sonra."),
  W("الرَّقِيبَ", "raqib", "noun", ["kana-wa-akhawatuha", FASL], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the watcher» — the khabar of kāna.", "«gözetleyici» — kâne'nin haberi.", punct="."),
 ]})

# ----------- s11 (RESTORED)
S.append({"id": "s11", "translation": {
 "en": "And its condition is that the khabar be definite or an «afʿal min», as in «Zayd was — he — the standing one» and «Zayd was — he — better than ʿAmr»; and it has no place in iʿrāb for al-Khalīl because it is a particle, while some of the Arabs make it a mubtada." + R_EN,
 "tr": "Şartı, haberin ma'rife ya da «ef'alü min» olmasıdır, «kâne Zeydün hüve'l-kâime» ve «kâne Zeydün hüve efdale min Amrin» gibi; Halîl'e göre harf olduğundan i'râbdan mahalli yoktur, bazı Araplar ise onu mübtedâ yapar." + R_TR},
 "tokens": [
  atf_wa("وَشَرْطُهُ", "shart", "noun", ["mubtada-khabar", "idafa-definiteness"], "شَرْطُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its condition» — the mubtada.", "«ve şartı» — mübtedâ.", "شَرْطُ", extra_segs=[seg("شَرْطُ", "shart", "noun"), pr3ms()]),
  W("كَوْنُ", "kawn", "noun", ["mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the being of» — the khabar.", "«olması» — haber."),
  W("الْخَبَرِ", "khabar", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ الْمَصْدَرِ.", "«the khabar».", "«haberin»."),
  W("مَعْرِفَةً", "marifa", "noun", ["khabar-al-mubtada-wa-ahkamuh"], "خَبَرُ الْمَصْدَرِ كَوْنُ مَنْصُوبٌ.", "«definite».", "«ma'rife»."),
  W("أَوْ", "aw", "conj", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«ya da»."),
  W("أَفْعَلَ", "afal-wazn", "noun", ["atf-nasaq", "ism-tafdil", "mamnu-min-sarf"], "مَعْطُوفٌ عَلَى مَعْرِفَةً مَنْصُوبٌ — وَزْنُ التَّفْضِيلِ.", "«afʿal» — the elative's pattern.", "«ef'al» — tafdîl vezni."),
  W("مِنْ", "min", "prep", ["huruf-jarr", "ism-tafdil"], "لَفْظٌ مَحْكِيٌّ — مِنْ الَّتِي تَصْحَبُ أَفْعَلَ التَّفْضِيلِ.", "«min» — the مِنْ that accompanies the elative.", "«min» — tafdîle eşlik eden min.", punct="،"),
  nahwu(punct=None),
  quoted("كَانَ", "kana", "verb", ["idafa-definiteness", "kana-wa-akhawatuha"], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ فِعْلٌ مَاضٍ نَاقِصٌ.", "«was».", "«idi»."),
  W("زَيْدٌ", "zayd", "propn", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  W("هُوَ", "huwa", "pron", [FASL], "ضَمِيرُ فَصْلٍ.", "«he» — the faṣl.", "«o» — fasl."),
  W("الْقَائِمَ", "qaim", "noun", ["kana-wa-akhawatuha", FASL], "خَبَرُ كَانَ مَنْصُوبٌ — مَعْرِفَةٌ.", "«the standing one» — the khabar, definite.", "«ayakta olan» — haber, ma'rife.", punct="،"),
  atf_wa("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and was».", "«ve idi».", "كَانَ"),
  W("زَيْدٌ", "zayd", "propn", ["kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  W("هُوَ", "huwa", "pron", [FASL], "ضَمِيرُ فَصْلٍ.", "«he».", "«o»."),
  W("أَفْضَلَ", "afdal", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — أَفْعَلُ تَفْضِيلٍ.", "«better» — the khabar, an elative.", "«daha üstün» — haber, ism-i tafdîl."),
  W("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«than».", "«-den»."),
  W("عَمْرٍو", "amr-name", "propn", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ، وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ.", "«ʿAmr» — the silent wāw written to tell the name from عُمَر.", "«Amr» — vâv, Ömer'den ayırmak için yazılır.", punct="؛"),
  W("وَلَا", "la", "part", ["la-nafiya-lil-jins"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا النَّافِيَةُ لِلْجِنْسِ.", "«and no».", "«ve yoktur».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part")]),
  W("مَحَلَّ", "mahall", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.", "«place» — the ism of لَا.", "«mahal» — lâ'nın ismi."),
  W("لَهُ", "li", "prep", ["huruf-jarr", "la-nafiya-lil-jins"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَا.", "«for it» — the khabar of لَا.", "«onun» — lâ'nın haberi.", segments=[seg("لَ", "li", "prep"), pr3ms()]),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-den»."),
  W("الْإِعْرَابِ", "irab", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«iʿrāb».", "«i'râb»."),
  W("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«for».", "«... göre»."),
  W("الْخَلِيلِ", "khalil-name", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«al-Khalīl».", "«Halîl»."),
  W("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ، وَالْهَاءُ اسْمُهَا.", "«because it».", "«çünkü o».", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  W("حَرْفٌ", "harf", "noun", ["inna-wa-akhawatuha"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is a particle».", "«harftir».", punct="،"),
  atf_wa("وَبَعْضُ", "bad", "noun", ["mubtada-khabar", "idafa-definiteness"], "بَعْضُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«and some of».", "«ve bazısı».", "بَعْضُ"),
  W("الْعَرَبِ", "arab", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Arabs».", "«Arapların»."),
  W("يَجْعَلُهُ", "jaala", "verb", ["mubtada-khabar", "mafulayn", "fail"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالْهَاءُ مَفْعُولٌ أَوَّلُ، وَالْجُمْلَةُ خَبَرٌ.", "«make it» — the khabar clause; the hāʾ its first object.", "«onu ... yapar» — haber cümlesi; hâ birinci mef'ûl.", segments=[seg("يَجْعَلُ", "jaala", "verb"), pr3ms()]),
  W("مُبْتَدَأً", "mubtada", "noun", ["mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a mubtada» — the second object.", "«mübtedâ» — ikinci mef'ûl.", punct="."),
 ]})

# ----------- s12 (RESTORED): the sha'n pronoun
S.append({"id": "s12", "translation": {
 "en": "And the absent pronoun precedes a sentence — called the pronoun of the matter in the masculine and the pronoun of the story in the feminine — and the sentence after it explains it, as in «it: Zayd is standing», «it was: Zayd is standing», and «indeed it: Zayd is standing»." + R_EN,
 "tr": "Cümleden önce gâib zamiri gelir — müzekkerde şan, müennesde kıssa zamiri denir — ve sonraki cümle onu açıklar; «hüve Zeydün kâimün», «kâne Zeydün kâimün» ve «innehû Zeydün kâimün» gibi." + R_TR},
 "tokens": [
  atf_wa("وَيَتَقَدَّمُ", "taqaddama", "verb", ["fail", "form-v-verbs"], "يَتَقَدَّمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and precedes».", "«ve önce gelir».", "يَتَقَدَّمُ"),
  W("الْجُمْلَةَ", "jumla", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the sentence» — the object.", "«cümleden» — mef'ûl."),
  W("ضَمِيرُ", "damir", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ.", "«the pronoun of» — the doer.", "«zamiri» — fâil."),
  W("الْغَائِبِ", "ghaib", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the absent».", "«gâib».", punct="،"),
  W("يُسَمَّى", "samma", "verb", ["naib-al-fail", "mafulayn", "naat-sifa"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ، وَالْجُمْلَةُ حَالٌ مِنْ ضَمِيرُ.", "«called» — the passive; the clause a ḥāl.", "«denir» — meçhul; cümle hâl."),
  W("ضَمِيرَ", "damir", "noun", ["mafulayn", "idafa-definiteness"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«the pronoun of» — the second object.", "«zamiri» — ikinci mef'ûl."),
  W("الشَّأْنِ", "shan", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the matter».", "«şan»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمُذَكَّرِ", "mudhakkar", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the masculine».", "«müzekkerde»."),
  atf_wa("وَضَمِيرَ", "damir", "noun", ["mafulayn", "idafa-definiteness"], "ضَمِيرَ مَعْطُوفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«and the pronoun of».", "«ve zamiri».", "ضَمِيرَ"),
  W("الْقِصَّةِ", "qissa", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the story».", "«kıssa»."),
  W("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  W("الْمُؤَنَّثِ", "muannath", "noun", ["huruf-jarr"], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the feminine».", "«müennesde».", punct="،"),
  atf_wa("وَتُفَسِّرُهُ", "fassara", "verb", ["maful-bihi", "form-ii-verbs"], "تُفَسِّرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and explains it».", "«ve onu açıklar».", "تُفَسِّرُ", extra_segs=[seg("تُفَسِّرُ", "fassara", "verb"), pr3ms()]),
  W("الْجُمْلَةُ", "jumla", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the sentence» — the doer.", "«cümle» — fâil."),
  W("بَعْدَهُ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«after it».", "«ondan sonraki».", punct="،", segments=[seg("بَعْدَ", "bada", "noun"), pr3ms()]),
  nahwu(punct=None),
  quoted("هُوَ", "huwa", "pron", ["idafa-definiteness", "mubtada-khabar", PRON], "فِي مَحَلِّ جَرٍّ؛ وَفِي الْمِثَالِ ضَمِيرُ الشَّأْنِ مُبْتَدَأٌ، وَالْجُمْلَةُ بَعْدَهُ خَبَرُهُ — مُنْفَصِلٌ لِأَنَّ عَامِلَهُ مَعْنَوِيٌّ.", "«it» — the shaʾn pronoun as mubtada; detached because its governor is the ibtidāʾ.", "«o» — şan zamiri mübtedâ; âmili manevî olduğundan munfasıl."),
  W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.", "«Zayd» — the second mubtada.", "«Zeyd» — ikinci mübtedâ."),
  W("قَائِمٌ", "qaim", "noun", ["mubtada-khabar"], "خَبَرُ الْمُبْتَدَإِ الثَّانِي، وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.", "«is standing» — the clause is the first mubtada's khabar.", "«ayaktadır» — cümle birincinin haberi.", punct="،"),
  atf_wa("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ ضَمِيرُ الشَّأْنِ مُسْتَتِرٌ.", "«and it was» — the shaʾn pronoun concealed inside kāna.", "«ve idi» — şan zamiri kâne'de gizli.", "كَانَ"),
  W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ."),
  W("قَائِمٌ", "qaim", "noun", ["mubtada-khabar", "kana-wa-akhawatuha"], "خَبَرٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«is standing» — the clause is kāna's khabar in the place of naṣb.", "«ayaktadır» — cümle mahallen mansûb, kâne'nin haberi.", punct="،"),
  atf_wa("وَإِنَّهُ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ اسْمُهَا بَارِزٌ.", "«and indeed it» — the shaʾn pronoun as the apparent ism of إِنَّ.", "«ve gerçekten o» — şan zamiri inne'nin bâriz ismi.", "إِنَّ", extra_segs=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  W("زَيْدٌ", "zayd", "propn", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd».", "«Zeyd»."),
  W("قَائِمٌ", "qaim", "noun", ["mubtada-khabar", "inna-wa-akhawatuha"], "خَبَرٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«is standing» — the clause is the khabar of إِنَّ.", "«ayaktadır» — cümle inne'nin haberi.", punct="."),
 ]})

# ----------- s13 (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And its omission in naṣb is weak, except with the أَنْ lightened from the heavy one, where it is obligatory — as in «and the last of their call is: praise be to God, Lord of the worlds»." + R_EN,
 "tr": "Mansûb iken hazfi zayıftır; ancak sakîlden hafifletilmiş en ile birlikte hazfi lâzımdır — «ve âhiru da'vâhüm eni'l-hamdü lillâhi rabbi'l-âlemîn» gibi." + R_TR},
 "tokens": [
  atf_wa("وَحَذْفُهُ", "hadhf", "noun", ["mubtada-khabar", "idafa-definiteness", "masdar"], "حَذْفُ مُبْتَدَأٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and its omission» — the mubtada.", "«ve hazfi» — mübtedâ.", "حَذْفُ", extra_segs=[seg("حَذْفُ", "hadhf", "noun"), pr3ms()]),
  W("مَنْصُوبًا", "mansub", "noun", ["hal", "ism-maful"], "حَالٌ مِنَ الْهَاءِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«while in naṣb» — the ḥāl.", "«mansûb iken» — hâl."),
  W("ضَعِيفٌ", "daif", "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«is weak» — the khabar.", "«zayıftır» — haber.", punct="،"),
  W("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "«except».", "«ancak»."),
  W("مَعَ", "maa", "noun", ["istithna", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ، وَهُوَ مُضَافٌ.", "«with».", "«ile»."),
  W("أَنْ", "an-mukhaffafa", "part", ["idafa-definiteness", "mawadi-fath-anna"], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«أَنْ» — cited.", "«en» — hikâye."),
  W("الْمُخَفَّفَةِ", "mukhaffafa", "noun", ["naat-sifa", "ism-maful", "form-ii-verbs"], "صِفَةٌ لِأَنْ مَجْرُورَةٌ بِالْكَسْرَةِ.", "«lightened» — its naʿt.", "«hafifletilmiş» — sıfatı."),
  W("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  W("الثَّقِيلَةِ", "thaqila", "noun", ["huruf-jarr", "sifa-mushabbaha"], "مَجْرُورٌ بِالْكَسْرَةِ — أَيْ أَنَّ.", "«the heavy one» — أَنَّ.", "«sakîlden» — enne."),
  W("فَلَازِمٌ", "lazim", "noun", ["mubtada-khabar", "al-fa-fi-khabar-al-mubtada"], "الْفَاءُ لِلْجَزَاءِ، وَلَازِمٌ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ — أَيْ فَحَذْفُهُ لَازِمٌ.", "«it is obligatory» — the khabar of a dropped mubtada.", "«lâzımdır» — hazfedilmiş mübtedânın haberi.", punct="،", segments=[seg("فَ", "fa", "conj"), seg("لَازِمٌ", "lazim", "noun")]),
  nahwu(punct=None),
  W("وَآخِرُ", "akhir", "noun", ["mubtada-khabar", "idafa-definiteness", "al-iqtibas-wal-tadmin"], "الْوَاوُ عَاطِفَةٌ، وَآخِرُ مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ (يُونُسَ ١٠).", "«and the last of» — the mubtada (Yūnus 10:10).", "«ve sonu» — mübtedâ (Yûnus 10:10).", segments=[seg("وَ", "wa", "conj"), seg("آخِرُ", "akhir", "noun")]),
  W("دَعْوَاهُمْ", "dawa-claim", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their call».", "«duâlarının».", segments=[seg("دَعْوَا", "dawa-claim", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  W("أَنِ", "an-mukhaffafa", "part", ["mawadi-fath-anna", "hadhf-wa-taqdir"], "أَنْ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«that» — the lightened أَنْ; its ism, the shaʾn pronoun, dropped.", "«ki» — hafifletilmiş en; ismi olan şan zamiri hazfedilmiş."),
  W("الْحَمْدُ", "hamd", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرُ أَنْ.", "«praise» — the mubtada; the clause is the khabar of أَنْ.", "«hamd» — mübtedâ; cümle en'in haberi."),
  W("لِلّٰهِ", "allah", "propn", ["huruf-jarr", "mubtada-khabar"], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«to God» — the khabar.", "«Allah'a» — haber.", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  W("رَبِّ", "rabb", "noun", ["naat-sifa", "idafa-definiteness"], "صِفَةٌ لِلَفْظِ الْجَلَالَةِ مَجْرُورَةٌ، وَهُوَ مُضَافٌ.", "«Lord of».", "«Rabbi»."),
  W("الْعَالَمِينَ", "alamin", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«the worlds» — jarr by the yāʾ.", "«âlemlerin» — yâ ile mecrûr.", punct="."),
 ]})

for _t in S[12]["tokens"]:
    if _t["surface"]["full"] == "وَآخِرُ": _t["quoteBefore"] = "﴿"
    if _t["surface"]["full"] == "الْعَالَمِينَ": _t["quoteAfter"] = "﴾"
for _t in S[9]["tokens"]:
    if _t["surface"]["full"] == "وَكُنْتَ": _t["quoteBefore"] = "﴿"
    if _t["surface"]["full"] == "الرَّقِيبَ": _t["quoteAfter"] = "﴾"

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
 "khayyara": need("khayyara", "خَيَّرَ", "خ ي ر", "verb", "to give a choice (Form II; خَيَّرَ يُخَيِّرُ; خُيِّرْتَ: you were given the choice)", "muhayyer bırakmak, seçim hakkı vermek (tef'îl; hayyere yuhayyiru)", 4),
 "arafu": need("arafu", "أَعْرَف", "ع ر ف", "noun", "more definite (elative of مَعْرِفَة: the speaker, then the addressee, then the absent)", "daha ma'rife (ma'rifenin ism-i tafdîli: mütekellim, sonra muhâtab, sonra gâib)", 5),
 "mukhtar": need("mukhtar", "مُخْتَار", "خ ي ر", "noun", "preferred, chosen (ism maf'ul of Form VIII اخْتَارَ) — الْمُخْتَارُ: the preferred reading", "muhtâr, tercih edilen (ihtâra'nın ism-i mef'ûlü)", 4),
 "akhfash": need("akhfash", "الْأَخْفَش", None, "propn", "al-Akhfash (Saʿīd b. Masʿada, d. c. 215/830), the Basran grammarian, Sībawayh's pupil", "Ahfeş (Saîd b. Mes'ade, ö. 215/830), Basralı nahivci, Sîbeveyh'in talebesi", 5),
 "khalil-name": need("khalil-name", "الْخَلِيل", "خ ل ل", "propn", "al-Khalīl b. Aḥmad (d. 175/791), Sībawayh's teacher, the founder of ʿarūḍ", "Halîl b. Ahmed (ö. 175/791), Sîbeveyh'in hocası, arûzun kurucusu", 5),
 "qat-hasb": need("qat-hasb", "قَطْ", "ق ط ط", "noun", "«enough» — a noun meaning حَسْبُ, taking the wiqāya nūn before the speaker's yāʾ (قَطْنِي)", "«yeter» — hasbü manasına isim; mütekellim yâsından önce vikâye nûnu alır (katnî)", 5),
 "wiqaya": need("wiqaya", "وِقَايَة", "و ق ي", "noun", "protection — نُونُ الْوِقَايَةِ: the nūn that guards the verb's ending from the kasra before the speaker's yāʾ", "koruma — nûnu'l-vikâye: mütekellim yâsından önce fiilin sonunu kesreden koruyan nûn", 4),
 "mukhayyar": need("mukhayyar", "مُخَيَّر", "خ ي ر", "noun", "free to choose (ism maf'ul of Form II خَيَّرَ)", "muhayyer (hayyere'nin ism-i mef'ûlü)", 4),
 "thaqila": need("thaqila", "ثَقِيلَة", "ث ق ل", "noun", "heavy — أَنَّ الثَّقِيلَةُ: the doubled أَنَّ as against the lightened أَنْ", "sakîle, ağır — enne's-sakîle: hafifletilmiş en'in karşısında şeddeli enne", 4),
 "mukhaffafa": need("mukhaffafa", "مُخَفَّفَة", "خ ف ف", "noun", "lightened — أَنْ الْمُخَفَّفَةُ مِنَ الثَّقِيلَةِ: أَنَّ with its shadda removed, its ism the dropped pronoun of the matter", "muhaffefe — sakîleden hafifletilmiş en: şeddesi kaldırılmış enne, ismi hazfedilmiş şan zamiri", 5),
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

# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "khayyara", _sg.derived(_sg.B2, _sg.W2, "ُ", "خَيَّر", "خَيِّر", "خَيِّر", "تَخْيِير", "مُخَيِّر", "مُخَيَّر", "خُيِّرَ", "يُخَيَّرُ", "خَيَّرَهُ يُخَيِّرُهُ بَيْنَ الْأَمْرَيْنِ: جَعَلَهُ مُخَيَّرًا — مِنَ الْبَابِ الثَّانِي."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch4 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": K,
 "title": {"ar": "مَوَاضِعُ الْمُنْفَصِلِ، وَضَمِيرُ الْفَصْلِ وَضَمِيرُ الشَّأْنِ", "en": "Where the detached pronoun stands: the six excuses, two pronouns meeting, kāna's khabar, lawlā and ʿasā, the nūn of protection; the pronouns of separation and of the matter", "tr": "Munfasılın yerleri: altı özür, iki zamirin buluşması, kâne'nin haberi, levlâ ve asâ, vikâye nûnu; fasl ve şan zamirleri"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — ولا يجوز المنفصل مع إمكان المتصل؛ وإذا اجتمع ضميران وليس أحدهما مرفوعا؛ كنته وكنت إياه؛ لولاك وعساك؛ نون الوقاية؛ ضمير الفصل وشرطه؛ ضمير الشأن والقصة", "ضياء صونغور اوغلى — دفتر الكافية: التعذّر بستة أشياء بأمثلتها، خلاف الأخفش وسيبويه، أمثلة الفصل والشأن"],
 "question": {
  "en": ["When is the DETACHED pronoun used? Only where the attached cannot stand — six excuses: the pronoun fronted before its governor (إِيَّاكَ ضَرَبْتُ), a separation for restriction (مَا ضَرَبَكَ إِلَّا أَنَا), the governor dropped (إِيَّاكَ وَالشَّرَّ), the governor a meaning (أَنَا زَيْدٌ), the governor a particle with a rafʿ pronoun (مَا أَنْتَ قَائِمًا), a ṣifa running on other than its owner (زَيْدٌ عَمْرٌو ضَارِبُهُ هُوَ).",
         "Two pronouns meet, neither in rafʿ: if the more definite comes first (speaker > addressee > absent) you may attach or detach the second — أَعْطَيْتُكَهُ / أَعْطَيْتُكَ إِيَّاهُ; otherwise detach — أَعْطَيْتُهُ إِيَّاهُ، أَعْطَيْتُهُ إِيَّاكَ.",
         "Kāna's khabar as a pronoun: كُنْتُهُ is allowed, كُنْتُ إِيَّاهُ preferred. After لَوْلَا the detached (it is a mubtada: لَوْلَا أَنْتَ), after عَسَى the attached (it is a doer: عَسَيْتَ) — and لَوْلَاكَ / عَسَاكَ are heard, read by al-Akhfash as a jarr / naṣb pronoun in the place of rafʿ and by Sībawayh as a real jarr letter and a real لَعَلَّ.",
         "The nūn of protection: obligatory with the speaker's yāʾ on the past verb (ضَرَبَنِي) and on the non-past without the iʿrāb nūn (يَضْرِبُنِي); optional with the iʿrāb nūn, لَدُنْ and إِنَّ's family (يَضْرِبَانِنِي / يَضْرِبَانِي، إِنَّنِي / إِنِّي); preferred in لَيْتَ، مِنْ، عَنْ، قَدْ، قَطْ and dropped in لَعَلَّ.",
         "What is the FAṢL pronoun? The detached rafʿ form standing between mubtada and khabar, before or after a governor, agreeing with the mubtada — زَيْدٌ هُوَ الْقَائِمُ، كُنْتَ أَنْتَ الرَّقِيبَ — so the khabar is not mistaken for a ṣifa. Condition: the khabar is definite or an elative with مِنْ. Its maḥall: none for al-Khalīl (a particle); some Arabs make it a mubtada.",
         "What is the SHAʾN pronoun? An absent pronoun before a sentence that explains it — هُوَ زَيْدٌ قَائِمٌ (mubtada), كَانَ زَيْدٌ قَائِمٌ (concealed ism of kāna), إِنَّهُ زَيْدٌ قَائِمٌ (ism of إِنَّ) — called the pronoun of the story in the feminine. Dropping it in naṣb is weak except after the lightened أَنْ, where it must drop: ﴿وَآخِرُ دَعْوَاهُمْ أَنِ الْحَمْدُ لِلّٰهِ﴾.",
         "What does the engine read? The DabtEngine seats the fronted إِيَّا object, reads the Ḥijāzī مَا's ism and khabar, keeps the faṣl pronoun out of the seats (no maḥall) and the shaʾn pronoun as mubtada or ism; the InnaEngine knows the lightened أَنْ after a verb of saying's noun."],
  "tr": ["MUNFASIL zamir ne zaman kullanılır? Yalnız muttasılın duramadığı yerde — altı özür: zamirin âmilinden öne alınması (إِيَّاكَ ضَرَبْتُ), kasr için fasl (مَا ضَرَبَكَ إِلَّا أَنَا), âmilin hazfi (إِيَّاكَ وَالشَّرَّ), âmilin manevî olması (أَنَا زَيْدٌ), merfû zamirle âmilin harf olması (مَا أَنْتَ قَائِمًا), sahibinden başkası üzere cârî sıfat (زَيْدٌ عَمْرٌو ضَارِبُهُ هُوَ).",
         "İki zamir buluşur, biri merfû değil: daha ma'rife olan (mütekellim > muhâtab > gâib) önce gelirse ikincisini bitiştirmekte ya da ayırmakta serbestsin — أَعْطَيْتُكَهُ / أَعْطَيْتُكَ إِيَّاهُ; yoksa ayır — أَعْطَيْتُهُ إِيَّاهُ، أَعْطَيْتُهُ إِيَّاكَ.",
         "Kâne'nin haberi zamir olunca: كُنْتُهُ câiz, كُنْتُ إِيَّاهُ muhtâr. Levlâ'dan sonra munfasıl (mübtedâdır: لَوْلَا أَنْتَ), asâ'dan sonra muttasıl (fâildir: عَسَيْتَ) — لَوْلَاكَ / عَسَاكَ de işitilmiştir; Ahfeş'e göre ref' mahallinde mecrûr / mansûb zamir, Sîbeveyh'e göre gerçek harf-i cer ve gerçek leâlle.",
         "Vikâye nûnu: mâzîde (ضَرَبَنِي) ve i'râb nûnsuz muzâride (يَضْرِبُنِي) mütekellim yâsıyla lâzım; i'râb nûnu, ledün ve inne ailesiyle muhayyer (يَضْرِبَانِنِي / يَضْرِبَانِي، إِنَّنِي / إِنِّي); leyte, min, an, kad, kat'ta isbâtı, leâlle'de hazfi muhtâr.",
         "FASL zamiri nedir? Mübtedâ ile haber arasına, âmilden önce ya da sonra giren, mübtedâya mutâbık merfû munfasıl sîga — زَيْدٌ هُوَ الْقَائِمُ، كُنْتَ أَنْتَ الرَّقِيبَ — haberin sıfat sanılmaması için. Şartı: haberin ma'rife ya da min'li ism-i tafdîl olması. Mahalli: Halîl'e göre yok (harftir); bazı Araplar onu mübtedâ yapar.",
         "ŞAN zamiri nedir? Kendisini açıklayan cümleden önce gelen gâib zamiri — هُوَ زَيْدٌ قَائِمٌ (mübtedâ), كَانَ زَيْدٌ قَائِمٌ (kâne'nin gizli ismi), إِنَّهُ زَيْدٌ قَائِمٌ (inne'nin ismi) — müennesde kıssa zamiri denir. Mansûbken hazfi zayıf; hafifletilmiş en'den sonra hazfi lâzım: ﴿وَآخِرُ دَعْوَاهُمْ أَنِ الْحَمْدُ لِلّٰهِ﴾.",
         "Motor neyi okur? DabtEngine öne alınmış إِيَّا mef'ûlünü yerine oturtur, Hicâzî mâ'nın ismini ve haberini okur, fasl zamirini yerlerin dışında (mahalsiz), şan zamirini mübtedâ ya da isim olarak tutar; InnaEngine hafifletilmiş en'i tanır."]},
 "plain": {
  "en": "Use the short attached pronoun wherever it can stand; the long detached one is for the six places it cannot. A detached pronoun between subject and predicate that marks the predicate is the separator, with no case; an absent pronoun opening the sentence that explains it is the pronoun of the matter.",
  "tr": "Kısa muttasıl zamiri durabildiği her yerde kullan; uzun munfasıl, duramadığı altı yer içindir. Özne ile yüklem arasına girip yüklemi işaretleyen munfasıl zamir fasl zamiridir, mahalli yoktur; kendisini açıklayan cümleyi açan gâib zamiri şan zamiridir."},
 "explanation": {
  "en": "The chapter is the working-out of the rule that closed the previous one: pronouns exist for brevity, so the detached form is never used while the attached can stand. Ibn al-Hajib lists where it cannot — the pronoun fronted before its governor, the separation that makes a restriction, the dropped governor of the warning, the governor that is only a meaning (the ibtidāʾ), the particle governor whose pronoun is in rafʿ (the Ḥijāzī مَا), and the adjective that runs on one noun while belonging to another, where the detached هُوَ keeps the beater from being read as ʿAmr. Then the meeting of two pronouns on one verb (أَعْطَيْتُكَهُ), kāna's pronominal khabar (كُنْتُ إِيَّاهُ preferred), the two particles that fix the form after them — لَوْلَا takes a mubtada and so the detached, عَسَى a doer and so the attached — with the heard لَوْلَاكَ and عَسَاكَ and the disagreement of al-Akhfash and Sībawayh over what case the pronoun carries. The nūn of protection is the mechanical side of the same chapter: it shields the verb's last letter from the kasra the speaker's yāʾ would impose, obligatory on the verb, optional on إِنَّ's family and لَدُنْ, preferred on لَيْتَ and the two letters مِنْ and عَنْ, dropped on لَعَلَّ. The chapter closes with the two pronouns that have no ordinary seat: the faṣl, a rafʿ form between mubtada and khabar whose whole job is to say «this is the predicate, not an adjective» (and whose maḥall the grammarians dispute), and the shaʾn, the absent pronoun that opens a sentence and is explained by it — concealed in kāna, apparent after إِنَّ, and obligatorily dropped after the lightened أَنْ, as the Qurʾan's ﴿أَنِ الْحَمْدُ لِلّٰهِ﴾ shows.",
  "tr": "Bâb, öncekini kapatan kuralın işlenişidir: zamirler ihtisar içindir; muttasıl durabildikçe munfasıl kullanılmaz. İbnü'l-Hâcib duramadığı yerleri sayar — zamirin âmilinden öne alınması, kasr yapan fasl, tahzîrin hazfedilmiş âmili, yalnız bir mana olan âmil (ibtidâ), zamiri merfû olan harf âmil (Hicâzî mâ) ve bir isim üzere cârî olup başkasına âit sıfat; burada munfasıl هُوَ dövenin Amr sanılmasını önler. Sonra bir fiilde iki zamirin buluşması (أَعْطَيْتُكَهُ), kâne'nin zamir haberi (كُنْتُ إِيَّاهُ muhtâr), sonrasındaki şekli belirleyen iki edat — لَوْلَا mübtedâ alır, dolayısıyla munfasıl; عَسَى fâil alır, dolayısıyla muttasıl — işitilen لَوْلَاكَ ve عَسَاكَ ile Ahfeş ve Sîbeveyh'in zamirin hâli üzerine ihtilâfı. Vikâye nûnu aynı bâbın mekanik yüzüdür: mütekellim yâsının getireceği kesreden fiilin son harfini korur; fiilde lâzım, inne ailesi ve ledün'de muhayyer, leyte ile min ve an'da muhtâr, leâlle'de hazfi muhtâr. Bâb, sıradan yeri olmayan iki zamirle kapanır: mübtedâ ile haber arasında «bu haberdir, sıfat değil» demekten başka işi olmayan (mahallini nahivcilerin tartıştığı) merfû fasl; ve cümleyi açıp onunla açıklanan gâib şan zamiri — kâne'de gizli, inne'den sonra bâriz, hafifletilmiş en'den sonra vücûben hazfedilmiş; Kur'ân'ın ﴿أَنِ الْحَمْدُ لِلّٰهِ﴾ âyeti bunu gösterir."},
 "examples": [
  {"ar": "إِيَّاكَ ضَرَبْتُ، مَا ضَرَبَكَ إِلَّا أَنَا، إِيَّاكَ وَالشَّرَّ", "en": "The first three excuses.", "tr": "İlk üç özür.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "أَنَا زَيْدٌ، مَا أَنْتَ قَائِمًا، زَيْدٌ عَمْرٌو ضَارِبُهُ هُوَ", "en": "The last three excuses.", "tr": "Son üç özür.", "sourceStory": "al-kafiya", "sentence": "s2"},
  {"ar": "أَعْطَيْتُكَهُ وَأَعْطَيْتُكَ إِيَّاهُ", "en": "Two pronouns, the more definite first: either form.", "tr": "İki zamir, daha ma'rife olan önce: iki şekil de olur.", "sourceStory": "al-kafiya", "sentence": "s3"},
  {"ar": "كَانَ زَيْدٌ قَائِمًا وَكُنْتُ إِيَّاهُ", "en": "Kāna's pronominal khabar, detached by preference.", "tr": "Kâne'nin zamir haberi, tercihen munfasıl.", "sourceStory": "al-kafiya", "sentence": "s5"},
  {"ar": "زَيْدٌ هُوَ الْقَائِمُ، وَكُنْتَ أَنْتَ الرَّقِيبَ", "en": "The faṣl pronoun before and after the governor.", "tr": "Fasl zamiri âmilden önce ve sonra.", "sourceStory": "al-kafiya", "sentence": "s10"},
  {"ar": "هُوَ زَيْدٌ قَائِمٌ، وَكَانَ زَيْدٌ قَائِمٌ، وَإِنَّهُ زَيْدٌ قَائِمٌ", "en": "The shaʾn pronoun in its three dresses.", "tr": "Şan zamiri üç kılığında.", "sourceStory": "al-kafiya", "sentence": "s12"},
  {"ar": "وَآخِرُ دَعْوَاهُمْ أَنِ الْحَمْدُ لِلّٰهِ رَبِّ الْعَالَمِينَ", "en": "The shaʾn pronoun dropped after the lightened أَنْ (10:10).", "tr": "Hafifletilmiş en'den sonra şan zamirinin hazfi (10:10).", "sourceStory": "al-kafiya", "sentence": "s13"}],
 "commonMistakes": [
  {"wrong": "«ضَرَبْتُ إِيَّاكَ — fiilden sonra da munfasıl câizdir»",
   "right": "«ضَرَبْتُكَ — muttasıl mümkünken munfasıl câiz olmaz; munfasıl ancak öne alınınca: إِيَّاكَ ضَرَبْتُ»",
   "why": {"en": "The detached form needs one of the six excuses; after its own verb the pronoun can attach, so it must.", "tr": "Munfasıl şekil altı özürden birini ister; kendi fiilinden sonra zamir bitişebilir, öyleyse bitişmelidir."}},
  {"wrong": "«أَعْطَيْتُهُهُ — iki gâib zamiri de bitişir»",
   "right": "«أَعْطَيْتُهُ إِيَّاهُ — ikincisi vücûben munfasıldır»",
   "why": {"en": "Neither absent pronoun is more definite than the other, so the licence to attach the second is not granted.", "tr": "İki gâib zamirden hiçbiri diğerinden daha ma'rife değildir; ikincisini bitiştirme ruhsatı doğmaz."}},
  {"wrong": "«زَيْدٌ هُوَ الْقَائِمُ — hüve mübtedâ, el-kâimü haberidir»",
   "right": "«زَيْدٌ هُوَ الْقَائِمُ — hüve fasl zamiridir, mahalli yoktur; el-kâimü Zeyd'in haberidir»",
   "why": {"en": "Between a mubtada and a definite khabar the detached pronoun is the separator; reading it as a second mubtada is the minority Arab usage the Kafiya records, not the rule.", "tr": "Mübtedâ ile ma'rife haber arasındaki munfasıl zamir fasldır; onu ikinci mübtedâ okumak Kâfiye'nin kaydettiği azınlık kullanımıdır, kural değil."}},
  {"wrong": "«لَعَلَّنِي — leâlle vikâye nûnu alır»",
   "right": "«لَعَلِّي — leâlle'de vikâye nûnunun hazfi muhtârdır; لَيْتَنِي'de isbâtı»",
   "why": {"en": "The nūn is optional on إِنَّ's family, and the preferred usage splits: kept on لَيْتَ, dropped on لَعَلَّ.", "tr": "Nûn, inne ailesinde muhayyerdir; tercih ayrılır: leyte'de kalır, leâlle'de düşer."}}],
 "relatedNotes": [K3, PRON, FASL, WIQ, "qasr", "at-tahdhir", "ma-la-mushabbaha", "al-amil-al-manawi", "mafulayn", "kana-wa-akhawatuha", "inna-wa-akhawatuha", "afal-al-muqaraba", "mawadi-fath-anna", "ism-tafdil"]}

ADD_EN = (" Chapter 4 (notebook lines ~164-173): the six things that make the attached impossible (s1-s2), two pronouns meeting (s3-s4), kāna's "
          "pronominal khabar (s5), لَوْلَا and عَسَى (s6) with the grammarians' disagreement on لَوْلَاكَ and عَسَاكَ as commentary (s7), the nūn of protection "
          "(s8-s9), the faṣl pronoun with its condition and maḥall (s10-s11), the shaʾn pronoun and its omission after the lightened أَنْ (s12-s13). Rulings "
          "the notebook gives only in Turkish are RESTORED from the received matn and marked; the Qur'anic words of al-Ma'ida 5:117 (s10) and Yunus 10:10 "
          "(s13) are set as the notebook cites them.")
ADD_TR = (" Dördüncü bâb (defter satırları ~164-173): muttasılı imkânsız kılan altı şey (s1-s2), iki zamirin buluşması (s3-s4), kâne'nin zamir haberi (s5), "
          "levlâ ve asâ (s6) ve nahivcilerin levlâke ile asâke üzerine ihtilâfı şerh olarak (s7), vikâye nûnu (s8-s9), şartı ve mahalliyle fasl zamiri "
          "(s10-s11), şan zamiri ve hafifletilmiş en'den sonra hazfi (s12-s13). Defterin yalnız Türkçe verdiği hükümler alınan metinden GERİ YAZILMIŞ ve "
          "işaretlenmiştir; Mâide 5:117 (s10) ve Yûnus 10:10 (s13) âyetlerinin kelimeleri defterin iktibas ettiği gibi dizilmiştir.")
write_out(4, S, TITLE, ADD_EN, ADD_TR, "164-173", GLOSS_ADD, notes=(NOTE,),
          related=((K3, [K]), (PRON, [K]), (FASL, [K]), (WIQ, [K]), ("at-tahdhir", [K]), ("ma-la-mushabbaha", [K])))
report(4, S, GLOSS_ADD, (NOTE,))
