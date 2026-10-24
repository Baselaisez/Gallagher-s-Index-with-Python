# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 9: the MUTAʿADDĪ — understood only with the thing the act fell upon — and its three kinds: to
# ONE object (ضَرَبَ زَيْدٌ عَمْرًا; its object may be dropped with or without a clue); to TWO objects in three divisions — the second
# object a different thing from the first (أَعْطَيْتُ زَيْدًا دِرْهَمًا; both or one may be dropped), the VERBS OF THE HEART that enter on
# the mubtadaʾ and the khabar and put both in naṣb (عَلِمْتُ رَأَيْتُ وَجَدْتُ زَعَمْتُ ظَنَنْتُ خِلْتُ حَسِبْتُ، and the frozen هَبْ) with
# their properties — no dropping of their objects without a clue; ilghāʾ and iʿmāl when the verb stands between or after its two
# governed words; a doer and an object that are one person's two attached pronouns (عَلِمْتُنِي قَائِمًا, shared with جَهِلَ عَدِمَ
# فَقَدَ); أَنَّ entering on their two objects; the TAʿLĪQ — the work annulled in wording, not in sense, by a question word, a negation,
# the lām of ibtidāʾ, an oath, or إِنَّ with the lām in its khabar — reaching every verb of the heart (شَكَكْتُ تَبَيَّنْتُ نَسِيتُ), every
# verb by which knowledge is sought (امْتَحَنْتُ سَأَلْتُ) and the verbs of the five senses; and the verbs ATTACHED to the verbs of the
# heart only in entering on the mubtadaʾ and the khabar (صَيَّرَ جَعَلَ تَرَكَ اتَّخَذَ). Print pp. 102–104.
#   python3 author_izhar_ch9.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
import sarf_gen as _sg
PKG = _ic.PKG

K = "al-mutaaddi-wa-afal-al-qulub"
K8 = "al-lazim-wal-mutaaddi"
TITLE = {"ar": "الْفِعْلُ الْمُتَعَدِّي وَأَضْرُبُهُ، وَأَفْعَالُ الْقُلُوبِ وَالتَّعْلِيقُ", "en": "The mutaʿaddī verb and its kinds, the verbs of the heart and the taʿlīq", "tr": "Müteaddî fiil ve türleri, kalp fiilleri ve ta'lîk"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MW = "ism-mawsul"; MB = "maful-bihi"; FL = "fail"; KN = "kana-wa-akhawatuha"; NF = "naib-al-fail"; AM = "an-masdariyya"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
ZQ = "zanna-wa-akhawatuha"; MFN = "mafulayn"; HM = "hadhf-al-maful"; TSY = "afal-tasyir"; IS = "al-istifham"; IN = "inna-wa-akhawatuha"; MKI = "mawadi-kasr-inna"; AMM = "amma-tafsiliyya"; HL = "hal"; BD = "badal"; IFL = "ism-fil"; HV = "hollow-verbs"; DV = "doubled-verbs"; F5 = "form-v-verbs"; F8 = "form-viii-verbs"; NSB = "ism-mansub"; MSD = "masdar"; MQ = "ism-maqsur-manqus"; TM = "tamyiz"; YA = "ya-al-mutakallim"; LN = "la-nafiya"; LJ = "la-nafiya-lil-jins"; MNS = "mamnu-min-sarf"; JS = "jumla-sifa"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: وَذَلِكَ نَحْوُ — مُضَافٌ إِلَى الْجُمْلَةِ الْمَحْكِيَّةِ.", "«as in» — the khabar of a dropped mubtada, annexed to the quoted example.", "«meselâ» — mahzûf mübtedânın haberi, hikâye edilen cümleye muzâf.", punct=punct)
def quoted(form, lex, pos, tags, role_ar, role_en, role_tr, punct=None, segments=None):
    return tok(form, lex, pos, [K] + tags + [HT], f"لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، {role_ar}", role_en, role_tr, punct=punct, segments=segments)
def qv1(form, lex, stem, en, tr, joined=True, punct=None, extra=()):
    """a quoted first-person māḍī in the list of examples after نَحْوُ: — joined by the wāw onto the first"""
    f = ("وَ" if joined else "") + form
    segs = ([seg("وَ", "wa", "conj")] if joined else []) + [seg(stem, lex, "verb"), seg("تُ", "pron-1s", "pron")]
    return tok(f, lex, "verb", [K, ZQ, HT] + ([AT] if joined else []) + list(extra), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ" + ("، مَعْطُوفٌ عَلَى الْأَوَّلِ فِي مَحَلِّ جَرٍّ" if joined else "، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ") + " — فِعْلٌ مَاضٍ وَالتَّاءُ فَاعِلٌ.", en, tr, punct=punct, segments=segs)
def hadhf_(form="حَذْفُ", role_ar="مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ", en="«the dropping of» — the delayed mubtada, annexed", tr="«hazfi» — muahhar mübtedâ, muzâf", joined=False, punct=None, tags=()):
    f = ("وَ" if joined else "") + form
    return tok(f, "hadhf", "noun", [K, HM, MSD, ID] + ([AT] if joined else []) + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + role_ar + " — مَصْدَرُ حَذَفَ.", en, tr, punct=punct, segments=(wa(form, "hadhf", "noun") if joined else None))
def ahadihima(punct=None, joined=False, role_ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ", en="«one of the two» — annexed to the pronoun", tr="«ikisinden biri» — zamire muzâf"):
    f = ("وَ" if joined else "") + "أَحَدِهِمَا"
    return tok(f, "ahad", "noun", [K, ID, HM] + ([AT] if joined else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + role_ar + ".", en, tr, punct=punct, segments=([seg("وَ", "wa", "conj")] if joined else []) + [seg("أَحَدِ", "ahad", "noun"), seg("هِمَا", "pron-3d", "pron")])
def qarina_bi(punct=None, joined=False):
    f = ("وَ" if joined else "") + "بِقَرِينَةٍ"
    return tok(f, "qarina", "noun", [K, HJ, HM] + ([AT] if joined else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "الْبَاءُ حَرْفُ جَرٍّ، وَقَرِينَةٍ مَجْرُورٌ — الْبَاءُ لِلْمُصَاحَبَةِ.", "«with a clue» — the bāʾ of accompaniment.", "«karîneyle» — musâhabe bâsı.", punct=punct, segments=([seg("وَ", "wa", "conj")] if joined else []) + [seg("بِ", "bi", "prep"), seg("قَرِينَةٍ", "qarina", "noun")])
def biduniha(punct=None):
    return tok("وَبِدُونِهَا", "duna", "noun", [K, AT, HJ, ID, HM], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَدُونِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — بِدُونِ الْقَرِينَةِ.", "«and without it» — without the clue.", "«ve onsuz» — karînesiz.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun"), seg("هَا", "pron-3fs", "pron")])
def zayd(form, role_ar, en, tr, punct=None, tags=()):
    return tok(form, "zayd", "propn", [K] + list(tags), role_ar, en, tr, punct=punct)
def ma_an_pl(punct=None): return tok("مَعًا", "maan", "adv", [K, HL], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَعًا: جَمِيعًا.", "«together» — the ḥāl.", "«birlikte» — hâl.", punct=punct)
def faqat(punct=None): return tok("فَقَطْ", "faqat", "adv", [K, HT], "الْفَاءُ زَائِدَةٌ لِلتَّزْيِينِ، وَقَطْ اسْمٌ بِمَعْنَى حَسْبُ مَبْنِيٌّ عَلَى السُّكُونِ — حَالٌ.", "«only» — mabnī; the ḥāl.", "«yalnız» — mebnî; hâl.", punct=punct)
def qism(ordinal_form, ordinal_lex, ordinal_ar, ordinal_en, ordinal_tr, joined=False, punct=None):
    f = ("وَ" if joined else "") + "الْقِسْمُ"
    return [tok(f, "qism", "noun", [K, MK] + ([AT] if joined else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if joined else "") + "الْقِسْمُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the division» — the mubtada.", "«kısım» — mübtedâ.", segments=(wa("الْقِسْمُ", "qism", "noun") if joined else None)),
            tok(ordinal_form, ordinal_lex, "noun", [K, NA], ordinal_ar, ordinal_en, ordinal_tr, punct=punct)]

# ----------- s1 — the mutaʿaddī defined; the first kind
S.append({"id": "s1", "translation": {"en": "And the mutaʿaddī is that whose understanding is not complete without the thing the act fell upon; and it is of three kinds: the first is transitive to ONE object — as in «Zayd struck ʿAmr» — and its object may be dropped with a clue and without one.", "tr": "Müteaddî, fiilin üzerine vâki olduğu şey olmadan anlaşılması tamam olmayandır; üç türdür: birincisi BİR mef'ûle müteaddîdir — «Zeyd Amr'ı dövdü» gibi — mef'ûlü karîneyle de karînesiz de hazfedilebilir."},
 "tokens": [
  tok("وَالْمُتَعَدِّي", "mutaaddi", "noun", [K, MK, K8, MQ, IFA], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُتَعَدِّي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — مَنْقُوصٌ.", "«and the transitive» — the mubtada; a manqūṣ, its ḍamma estimated.", "«müteaddî» — mübtedâ; mankûs, zammesi takdîrî.", segments=wa("الْمُتَعَدِّي", "mutaaddi", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«that which» — the relative, the khabar.", "«… olandır» — ism-i mevsûl, haber."),
  tok("لَا", "la-nafiya", "part", [K, LN], "حَرْفُ نَفْيٍ.", "«not»", "«-mez»"),
  tok("يَتِمُّ", "tamma", "verb", [K, MW, FL, DV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — صِلَةٌ.", "«is complete» — the ṣila.", "«tamam olur» — sıla."),
  tok("فَهْمُهُ", "fahm", "noun", [K, FL, ID, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَائِدٌ إِلَى مَا.", "«its understanding» — the doer; the pronoun returns to «that which».", "«anlaşılması» — fâil; zamir mâ'ya döner.", segments=[seg("فَهْمُ", "fahm", "noun"), pr3ms()]),
  tok("بِغَيْرِ", "ghayr", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَغَيْرِ مَجْرُورٌ، مُضَافٌ.", "«without» — the jarr phrase; annexed.", "«-sız» — cer; muzâf.", segments=[seg("بِ", "bi", "prep"), seg("غَيْرِ", "ghayr", "noun")]),
  tok("مَا", "ma-mawsula", "pron", [K, MW, ID], "اسْمٌ مَوْصُولٌ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«that which» — the relative, annexed to.", "«… şey» — ism-i mevsûl, muzâfun ileyh."),
  tok("وَقَعَ", "waqaa", "verb", [K, MW, FL, "mithal-verbs"], "فِعْلٌ مَاضٍ — صِلَةٌ، وَالْفَاعِلُ بَعْدَهُ.", "«fell» — the ṣila; its doer follows.", "«vâki oldu» — sıla; fâil sonra."),
  tok("عَلَيْهِ", "ala", "prep", [K, HJ], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — عَائِدٌ إِلَى مَا.", "«upon it» — the returning pronoun.", "«üzerine» — âid zamir.", segments=[seg("عَلَيْ", "ala", "prep"), pr3msi()]),
  tok("الْفِعْلُ", "fil", "noun", [K, FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the act» — the doer.", "«fiil» — fâil.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it» — the mubtada.", "«o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the phrase is the khabar.", "«üzere» — câr-mecrûr haber."),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«three», annexed.", "«üç», muzâf."),
  tok("أَضْرُبٍ", "darb", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ ضَرْبٍ: نَوْعٌ.", "«kinds» — the plural of ضَرْب, a kind.", "«tür» — darbın cemi.", punct=":"),
  tok("الْأَوَّلُ", "awwal", "noun", [K, MK], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the first» — the mubtada.", "«birincisi» — mübtedâ."),
  tok("مُتَعَدٍّ", "mutaaddi", "noun", [K, MK, MQ, IFA, K8], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ مُنَوَّنٌ.", "«transitive» — the khabar; the manqūṣ with its yāʾ dropped.", "«müteaddîdir» — haber; yâsı düşmüş mankûs."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَفْعُولٍ", "maful-object", "noun", [K, HJ, MFN], "مَجْرُورٌ بِإِلَى.", "«an object»", "«mef'ûle»"),
  tok("وَاحِدٍ", "wahid", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«one» — the naʿt.", "«bir» — sıfat.", punct="،"),
  nahw(),
  tok("ضَرَبَ", "daraba", "verb", [K, FL, MB, HT], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا.", "«struck» — the quoted example's verb.", "«dövdü» — hikâye edilen misâlin fiili."),
  zayd("زَيْدٌ", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Zayd» — the doer.", "«Zeyd» — fâil.", tags=[FL]),
  tok("عَمْرًا", "amr-name", "propn", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — الْمَفْعُولُ الْوَاحِدُ.", "«ʿAmr» — the one object.", "«Amr'ı» — tek mef'ûl.", punct="،"),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, HM], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ حَذْفُ.", "«and it is permitted» — its doer is «the dropping».", "«ve câizdir» — fâili hazf.", segments=wa("يَجُوزُ", "jaaza", "verb")),
  hadhf_(role_ar="فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ", en="«the dropping of» — the doer, annexed", tr="«hazfi» — fâil, muzâf"),
  tok("مَفْعُولِهِ", "maful-object", "noun", [K, ID, HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its object»", "«mef'ûlünün»", segments=[seg("مَفْعُولِ", "maful-object", "noun"), pr3msi()]),
  qarina_bi(),
  biduniha(punct="."),
 ]})
# ----------- s2 — the second kind, first division
S.append({"id": "s2", "translation": {"en": "And the second is transitive to TWO objects, and it is of three divisions: the first division is that whose second object is a different thing from the first — as in «I gave Zayd a dirham» — and both may be dropped, or one of them, with a clue and without one.", "tr": "İkincisi İKİ mef'ûle müteaddîdir; üç kısımdır: birinci kısım ikinci mef'ûlü birincisinden ayrı olandır — «Zeyd'e bir dirhem verdim» gibi — ikisi de, biri de karîneyle de karînesiz de hazfedilebilir."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«and the second» — the mubtada.", "«ikincisi» — mübtedâ.", segments=wa("الثَّانِي", "thani", "noun")),
  tok("مُتَعَدٍّ", "mutaaddi", "noun", [K, MK, MQ, K8], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ مُنَوَّنٌ.", "«transitive» — the khabar.", "«müteaddîdir» — haber."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("مَفْعُولَيْنِ", "maful-object", "noun", [K, HJ, MTH, MFN], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two objects» — the dual, jarr by the yāʾ.", "«iki mef'ûle» — tesniye, yâ ile mecrûr.", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«o» — mübtedâ.", segments=wa("هُوَ", "huwa", "pron")),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«of» — the khabar.", "«üzere» — haber."),
  tok("ثَلَاثَةِ", "thalatha", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«three», annexed.", "«üç», muzâf."),
  tok("أَقْسَامٍ", "qism", "noun", [K, ID, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِسْمٍ.", "«divisions»", "«kısım»", punct=":"),
  *qism("الْأَوَّلُ", "awwal", "نَعْتٌ مَرْفُوعٌ.", "«the first» — the naʿt.", "«birinci» — sıfat."),
  tok("مَا", "ma-mawsula", "pron", [K, MW, MK], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«that which» — the khabar.", "«… olandır» — haber."),
  tok("كَانَ", "kana", "verb", [K, KN, MW], "فِعْلٌ مَاضٍ نَاقِصٌ — صِلَةٌ.", "«is» — kāna; the ṣila.", "«olan» — kâne; sıla."),
  tok("مَفْعُولُهُ", "maful-object", "noun", [K, KN, ID, MFN], "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its object» — kāna's ism.", "«mef'ûlü» — kâne'nin ismi.", segments=[seg("مَفْعُولُ", "maful-object", "noun"), pr3ms()]),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«second» — the naʿt.", "«ikinci» — sıfat."),
  tok("مُبَايِنًا", "mubayin", "noun", [K, KN, IFA], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ مِنْ بَايَنَ.", "«different» — kāna's khabar; ism fāʿil of بَايَنَ.", "«ayrı» — kâne'nin haberi; bâyene'nin ism-i fâili."),
  tok("لِلْأَوَّلِ", "awwal", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْأَوَّلِ مَجْرُورٌ — مُتَعَلِّقٌ بِمُبَايِنًا.", "«from the first» — hanging on «different».", "«birincisinden» — mübâyinen'e müteallik.", punct="،", segments=[seg("لِ", "li", "prep"), seg("الْأَوَّلِ", "awwal", "noun")]),
  nahw(),
  tok("أَعْطَيْتُ", "aata", "verb", [K, FL, MFN, HT, "naqis-verbs", "form-iv-verbs"], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا.", "«I gave» — the quoted example; the tāʾ its doer.", "«verdim» — hikâye edilen misâl; tâ fâil.", segments=[seg("أَعْطَيْ", "aata", "verb"), seg("تُ", "pron-1s", "pron")]),
  zayd("زَيْدًا", "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the first object.", "«Zeyd'e» — birinci mef'ûl.", tags=[MB, MFN]),
  tok("دِرْهَمًا", "dirham", "noun", [K, MB, MFN], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — مُبَايِنٌ لِلْأَوَّلِ.", "«a dirham» — the second object, a different thing.", "«bir dirhem» — ikinci mef'ûl, birincisinden ayrı.", punct="،"),
  tok("وَيَجُوزُ", "jaaza", "verb", [K, AT, FL, HV, HM], "الْوَاوُ لِلِاسْتِئْنَافِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ حَذْفُهُمَا.", "«and it is permitted» — its doer «the dropping of both».", "«ve câizdir» — fâili ikisinin hazfi.", segments=wa("يَجُوزُ", "jaaza", "verb")),
  tok("حَذْفُهُمَا", "hadhf", "noun", [K, FL, ID, HM, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ — حَذْفُ الْمَفْعُولَيْنِ.", "«the dropping of both» — the doer.", "«ikisinin hazfi» — fâil.", segments=[seg("حَذْفُ", "hadhf", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  hadhf_(role_ar="مَعْطُوفٌ عَلَى حَذْفُهُمَا مَرْفُوعٌ، مُضَافٌ", en="«and the dropping of» — joined to the doer", tr="«ve hazfi» — fâile ma'tûf", joined=True),
  ahadihima(),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»"),
  biduniha(punct="."),
 ]})
# ----------- s3 — the verbs of the heart
S.append({"id": "s3", "translation": {"en": "The second division is the verbs of the heart: verbs that signify an act of the heart, entering on the mubtadaʾ and the khabar and putting both in naṣb as objects — as in «I knew», «I saw», «I found», «I claimed», «I supposed», «I imagined», «I reckoned» — and «suppose!» in the sense of «I reckon», not conjugable.", "tr": "İkinci kısım kalp fiilleridir: kalbî bir fiile delâlet eden, mübtedâ ve habere dâhil olup ikisini mef'ûl olarak nasb eden fiiller — «bildim», «gördüm», «buldum», «sandım», «zannettim», «hayal ettim», «hesapladım» gibi — ve «farz et!», «sanırım» mânâsında, mutasarrıf olmayan."},
 "tokens": [
  *qism("الثَّانِي", "thani", "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«the second» — the naʿt.", "«ikinci» — sıfat."),
  tok("أَفْعَالُ", "fil", "noun", [K, MK, ID, ZQ, "jam-taksir"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ فِعْلٍ.", "«the verbs of» — the khabar, annexed.", "«fiilleri» — haber, muzâf."),
  tok("الْقُلُوبِ", "qalb", "noun", [K, ID, ZQ, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قَلْبٍ.", "«the hearts»", "«kalp»", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ.", "«and they are» — the mubtada.", "«onlar» — mübtedâ.", segments=wa("هِيَ", "hiya", "pron")),
  tok("أَفْعَالٌ", "fil", "noun", [K, MK, JS, "jam-taksir"], "خَبَرٌ مَرْفُوعٌ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لَهُ.", "«verbs» — the khabar; the clause after it its naʿt.", "«fiillerdir» — haber; sonraki cümle sıfatı."),
  tok("تَدُلُّ", "dalla", "verb", [K, JS, FL, DV], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ نَعْتٌ لِأَفْعَالٍ.", "«signify» — the ṣifa clause.", "«delâlet eden» — sıfat cümlesi."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«an»", "«-e»"),
  tok("فِعْلٍ", "fil", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى.", "«act»", "«fiile»"),
  tok("قَلْبِيٍّ", "qalbi", "noun", [K, NA, NSB], "نَعْتٌ مَجْرُورٌ — مَنْسُوبٌ إِلَى الْقَلْبِ.", "«of the heart» — the nisba, the naʿt.", "«kalbî» — nispet, sıfat.", punct="،"),
  tok("دَاخِلَةٌ", "dakhil", "noun", [K, NA, IFA], "نَعْتٌ ثَانٍ لِأَفْعَالٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ دَخَلَ.", "«entering» — a second naʿt; ism fāʿil of دَخَلَ.", "«dâhil olan» — ikinci sıfat; dehale'nin ism-i fâili."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "مَجْرُورٌ بِعَلَى — الْهَمْزَةُ عَلَى نَبِرَةٍ لِكَسْرِهَا.", "«the mubtada» — its hamza seated on the yāʾ for the kasra.", "«mübtedâya» — hemzesi kesresi için nebre üzerinde."),
  tok("وَالْخَبَرِ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar»", "«ve habere»", punct="،", segments=wa("الْخَبَرِ", "khabar-predicate", "noun")),
  tok("نَاصِبَةٌ", "nasib", "noun", [K, NA, IFA], "نَعْتٌ ثَالِثٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ نَصَبَ يَعْمَلُ عَمَلَ فِعْلِهِ.", "«putting in naṣb» — a third naʿt; the participle governs like its verb.", "«nasb eden» — üçüncü sıfat; ism-i fâil fiili gibi amel eder."),
  tok("إِيَّاهُمَا", "iyya", "pron", [K, MB, ZQ], "ضَمِيرٌ مُنْفَصِلٌ مَفْعُولٌ بِهِ لِنَاصِبَةٍ فِي مَحَلِّ نَصْبٍ — إِيَّا الْمُبْتَدَأَ وَالْخَبَرَ.", "«both of them» — the object of «putting in naṣb».", "«ikisini» — nâsıbe'nin mef'ûlü."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«as»", "«olarak»"),
  tok("الْمَفْعُولِيَّةِ", "mafuliyya", "noun", [K, HJ, MB], "مَجْرُورٌ بِعَلَى — عَلَى أَنَّهُمَا مَفْعُولَانِ.", "«objecthood» — as two objects.", "«mef'ûliyyet» — iki mef'ûl olarak.", punct="،"),
  nahw(),
  qv1("عَلِمْتُ", "alima", "عَلِمْ", "«I knew» — the first of the quoted verbs; annexed to «as in».", "«bildim» — hikâye edilen fiillerin ilki.", joined=False),
  qv1("رَأَيْتُ", "raa", "رَأَيْ", "«I saw»", "«gördüm»", extra=["naqis-verbs"]),
  qv1("وَجَدْتُ", "wajada", "وَجَدْ", "«I found»", "«buldum»", extra=["mithal-verbs"]),
  qv1("زَعَمْتُ", "zaama-claim", "زَعَمْ", "«I claimed»", "«sandım»"),
  qv1("ظَنَنْتُ", "zanna", "ظَنَنْ", "«I supposed» — the doubled verb breaks its twins before the tāʾ.", "«zannettim» — muzâaf, tâ'dan önce fekk.", extra=[DV]),
  qv1("خِلْتُ", "khala-think", "خِلْ", "«I imagined» — the hollow verb shortened before the tāʾ.", "«hayal ettim» — ecvef, tâ'dan önce kısalmış.", extra=[HV]),
  qv1("حَسِبْتُ", "hasiba", "حَسِبْ", "«I reckoned»", "«hesapladım»", punct="،"),
  tok("وَهَبْ", "hab-suppose", "verb", [K, AT, ZQ, HT, MK], "الْوَاوُ عَاطِفَةٌ، وَهَبْ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ: فِعْلُ أَمْرٍ جَامِدٌ — مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and suppose!» — the frozen imperative, mentioned as a word: the mubtada.", "«ve farz et!» — câmid emir, lafzı kastedilen: mübtedâ.", segments=wa("هَبْ", "hab-suppose", "verb")),
  tok("بِمَعْنَى", "mana", "noun", [K, HJ, ID, MK, MQ], "الْبَاءُ حَرْفُ جَرٍّ، وَمَعْنَى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in the sense of» — the khabar; a maqṣūr.", "«mânâsında» — haber; maksûr.", segments=[seg("بِ", "bi", "prep"), seg("مَعْنَى", "mana", "noun")]),
  tok("أَحْسَبُ", "hasiba", "verb", [K, ID, HT, ZQ], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — فِعْلٌ مُضَارِعٌ لِلْمُتَكَلِّمِ مِنْ حَسِبَ يَحْسَبُ.", "«I reckon» — the quoted muḍāriʿ (حَسِبَ يَحْسَبُ), annexed to.", "«sanırım» — hikâye edilen muzâri (hasibe yahsebü), muzâfun ileyh."),
  tok("غَيْرَ", "ghayr", "noun", [K, HL, ID], "حَالٌ مَنْصُوبٌ، مُضَافٌ.", "«not» — the ḥāl, annexed.", "«olmayarak» — hâl, muzâf."),
  tok("مُتَصَرِّفٍ", "mutasarrif", "noun", [K, ID, IFA, F5], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ تَصَرَّفَ.", "«conjugable» — it has no other forms.", "«mutasarrıf» — başka sîgası yok.", punct="."),
 ]})
# ----------- s4 — no dropping of their objects without a clue
S.append({"id": "s4", "translation": {"en": "And it is not permitted to drop both their objects together, or one of the two, without a clue; and with a clue the dropping of both together is frequent and the dropping of one alone is rare.", "tr": "İki mef'ûlünü birlikte yahut birini karînesiz hazfetmek câiz değildir; karîneyle ikisini birlikte hazfetmek çok, yalnız birini hazfetmek azdır."},
 "tokens": [
  tok("وَلَا", "la-nafiya", "part", [K, LN, AT], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not»", "«ve -mez»", segments=wa("لَا", "la-nafiya", "part")),
  tok("يَجُوزُ", "jaaza", "verb", [K, FL, HV, HM], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ حَذْفُ.", "«is permitted» — its doer «the dropping».", "«câiz olmaz» — fâili hazf."),
  hadhf_(role_ar="فَاعِلٌ مَرْفُوعٌ، مُضَافٌ", en="«the dropping of» — the doer, annexed", tr="«hazfi» — fâil, muzâf"),
  tok("مَفْعُولَيْهَا", "maful-object", "noun", [K, ID, MTH, MFN], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their two objects» — the dual by its yāʾ, its nūn dropped for the annexation.", "«iki mef'ûlünü» — tesniye, yâ ile; nûnu izâfet için düşmüş.", segments=[seg("مَفْعُولَيْ", "maful-object", "noun"), pr3fs()]),
  ma_an_pl(),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  ahadihima(role_ar="مَعْطُوفٌ عَلَى مَفْعُولَيْهَا مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ", en="«one of the two» — joined to «their two objects»", tr="«birini» — iki mef'ûlüne ma'tûf"),
  tok("بِدُونِ", "duna", "noun", [K, HJ, ID, HM], "الْبَاءُ حَرْفُ جَرٍّ، وَدُونِ مَجْرُورٌ، مُضَافٌ.", "«without»", "«-sız»", segments=[seg("بِ", "bi", "prep"), seg("دُونِ", "duna", "noun")]),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»", punct="،"),
  tok("وَمَعَ", "maa", "noun", [K, AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَمَعَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ — مُتَعَلِّقٌ بِكَثُرَ.", "«and with» — the ẓarf, hanging on «is frequent».", "«ve … ile» — zarf, kesüra'ya müteallik.", segments=wa("مَعَ", "maa", "noun")),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»"),
  tok("كَثُرَ", "kathura", "verb", [K, FL, HM, "thulathi-mujarrad-babs"], "فِعْلٌ مَاضٍ مِنْ بَابِ حَسُنَ، وَفَاعِلُهُ حَذْفُهُمَا.", "«is frequent» — bāb حَسُنَ; its doer «the dropping of both».", "«çoktur» — hasüne bâbı; fâili ikisinin hazfi."),
  tok("حَذْفُهُمَا", "hadhf", "noun", [K, FL, ID, HM, MSD], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«the dropping of both» — the doer.", "«ikisinin hazfi» — fâil.", segments=[seg("حَذْفُ", "hadhf", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  ma_an_pl(),
  tok("وَقَلَّ", "qalla", "verb", [K, AT, FL, HM, DV], "الْوَاوُ عَاطِفَةٌ، وَقَلَّ فِعْلٌ مَاضٍ مُضَاعَفٌ، وَفَاعِلُهُ حَذْفُ.", "«and is rare» — the doubled verb; its doer «the dropping».", "«ve azdır» — muzâaf; fâili hazf.", segments=wa("قَلَّ", "qalla", "verb")),
  hadhf_(role_ar="فَاعِلٌ مَرْفُوعٌ، مُضَافٌ", en="«the dropping of» — the doer, annexed", tr="«hazfi» — fâil, muzâf"),
  ahadihima(),
  faqat(punct="."),
 ]})
# ----------- s5 — ilgha and imal
S.append({"id": "s5", "translation": {"en": "And among their properties is the permissibility of annulment and of operation when the verb stands between its two governed words — as in «Zayd, I knew, is departing» — or comes after them — as in «Zayd is departing, I knew».", "tr": "Hususiyetlerinden biri, fiil iki ma'mûlü arasına girdiğinde — «Zeyd, bildim, gidiyor» gibi — yahut onlardan sonra geldiğinde — «Zeyd gidiyor, bildim» gibi — ilgâ ve i'mâlin câiz olmasıdır."},
 "tokens": [
  tok("وَمِنْ", "min", "prep", [K, AT, HJ, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنْ حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and among» — the fronted khabar.", "«ve … -den» — mukaddem haber.", segments=wa("مِنْ", "min", "prep")),
  tok("خَصَائِصِهَا", "khasisa", "noun", [K, HJ, ID, MNS, "jam-taksir"], "مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ خَصِيصَةٍ، صِيغَةُ مُنْتَهَى الْجُمُوعِ، جُرَّ بِالْكَسْرَةِ لِلْإِضَافَةِ.", "«their properties» — the ultimate plural, taking its kasra by the annexation.", "«hususiyetlerinden» — müntehe'l-cumû; izâfetle kesre.", segments=[seg("خَصَائِصِ", "khasisa", "noun"), pr3fs()]),
  tok("جَوَازُ", "jawaz", "noun", [K, MK, ID, MSD], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ جَازَ.", "«the permissibility of» — the delayed mubtada.", "«câiz olması» — muahhar mübtedâ."),
  tok("الْإِلْغَاءِ", "ilgha", "noun", [K, ID, ZQ, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — إِبْطَالُ عَمَلِ الْفِعْلِ لَفْظًا وَمَحَلًّا.", "«the annulment» — stripping the verb of its work in wording and in place.", "«ilgâ» — fiilin amelini lafzen ve mahallen iptal."),
  tok("وَالْإِعْمَالِ", "imal", "noun", [K, AT, ZQ, MSD], "الْوَاوُ عَاطِفَةٌ، وَالْإِعْمَالِ مَعْطُوفٌ مَجْرُورٌ.", "«and the operation» — letting it govern.", "«ve i'mâl» — amel ettirmek.", segments=wa("الْإِعْمَالِ", "imal", "noun")),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ — مُتَعَلِّقٌ بِجَوَازُ.", "«when» — the ẓarf of condition, hanging on «permissibility».", "«-dığında» — şart zarfı, cevâz'a müteallik."),
  tok("تَوَسَّطَتْ", "tawassata", "verb", [K, FL, F5, "idha-shartiyya"], "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ (الْأَفْعَالُ) — فِعْلُ الشَّرْطِ.", "«stand between» — the sharṭ; the verbs are its hidden doer.", "«ortaya girdiğinde» — şart fiili; fâili gizli hiye."),
  tok("بَيْنَ", "bayna", "noun", [K, MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between», annexed.", "«arasına», muzâf."),
  tok("مَعْمُولَيْهَا", "mamul", "noun", [K, ID, MTH, ZQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its two governed words» — the dual, its nūn dropped.", "«iki ma'mûlü» — tesniye, nûnu düşmüş.", punct="،", segments=[seg("مَعْمُولَيْ", "mamul", "noun"), pr3fs()]),
  nahw(),
  zayd("زَيْدٌ", "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ — وَالْجُمْلَةُ مُضَافٌ إِلَيْهَا.", "«Zayd» — the quoted example's mubtada.", "«Zeyd» — hikâye edilen misâlin mübtedâsı.", tags=[MK, ZQ, HT]),
  tok("عَلِمْتُ", "alima", "verb", [K, ZQ, FL, HT], "فِعْلٌ مَاضٍ مُلْغًى عَنِ الْعَمَلِ لِتَوَسُّطِهِ، وَالتَّاءُ فَاعِلٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«I knew» — annulled by standing between; a parenthesis.", "«bildim» — ortaya girdiği için mülgâ; mu'teriza cümle.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مُنْطَلِقٌ", "muntaliq", "noun", [K, MK, ZQ, IFA, F8], "خَبَرٌ مَرْفُوعٌ — بَقِيَ عَلَى رَفْعِهِ لِإِلْغَاءِ الْفِعْلِ.", "«departing» — the khabar, kept in rafʿ by the annulment.", "«gidiyor» — haber; ilgâ ile ref'te kalmış.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  tok("تَأَخَّرَتْ", "taakhkhara", "verb", [K, AT, FL, F5], "فِعْلٌ مَاضٍ مَعْطُوفٌ عَلَى تَوَسَّطَتْ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«come after» — joined to «stand between».", "«sonraya kaldığında» — tevessatat'a ma'tûf.", punct="،"),
  nahw(),
  zayd("زَيْدٌ", "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ.", tags=[MK, ZQ, HT]),
  tok("مُنْطَلِقٌ", "muntaliq", "noun", [K, MK, ZQ, IFA], "خَبَرٌ مَرْفُوعٌ.", "«departing» — the khabar.", "«gidiyor» — haber."),
  tok("عَلِمْتُ", "alima", "verb", [K, ZQ, FL, HT], "فِعْلٌ مَاضٍ مُلْغًى لِتَأَخُّرِهِ، وَالتَّاءُ فَاعِلٌ.", "«I knew» — annulled by coming after.", "«bildim» — sonraya kaldığı için mülgâ.", punct=".", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
 ]})
# ----------- s6 — the two attached pronouns of one meaning; anna on the two objects
S.append({"id": "s6", "translation": {"en": "And among them is the permissibility that their doer and their object be two attached pronouns of one meaning — as in «I knew myself to be standing»; and جَهِلَ, عَدِمَ and فَقَدَ stand with them in this permission — and among them is the permissibility of أَنَّ entering on their two objects, as in «I knew that Zayd is standing».", "tr": "Bir diğeri, fâillerinin ve mef'ûllerinin aynı mânâda iki muttasıl zamir olmasının câiz olmasıdır — «kendimi ayakta bildim» gibi; cehile, adime ve fekade de bu cevazda onlarla aynı hükümdedir — bir diğeri de enne'nin iki mef'ûlüne dâhil olmasının câiz olmasıdır: «Zeyd'in ayakta olduğunu bildim» gibi."},
 "tokens": [
  tok("وَمِنْهَا", "min", "prep", [K, AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ: مِنْ خَصَائِصِهَا.", "«and among them» — the fronted khabar.", "«ve onlardan» — mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("جَوَازُ", "jawaz", "noun", [K, MK, ID, MSD], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ.", "«the permissibility that» — annexed to the أَنْ-clause.", "«câiz olması» — en'li cümleye muzâf."),
  tok("أَنْ", "an-masdariyya", "part", [K, AM], "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ.", "«that»", "«-ması»"),
  tok("يَكُونَ", "kana", "verb", [K, AM, KN, HV], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be» — kāna in naṣb.", "«olması» — mansûb kâne."),
  tok("فَاعِلُهَا", "fail-doer", "noun", [K, KN, ID, FL], "اسْمُ يَكُونَ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their doer» — kāna's ism.", "«fâilleri» — kâne'nin ismi.", segments=[seg("فَاعِلُ", "fail-doer", "noun"), pr3fs()]),
  tok("وَمَفْعُولُهَا", "maful-object", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَمَفْعُولُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their object»", "«ve mef'ûlleri»", segments=[seg("وَ", "wa", "conj"), seg("مَفْعُولُ", "maful-object", "noun"), pr3fs()]),
  tok("ضَمِيرَيْنِ", "damir", "noun", [K, KN, MTH], "خَبَرُ يَكُونَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«two pronouns» — kāna's khabar, the dual.", "«iki zamir» — kâne'nin haberi, tesniye."),
  tok("مُتَّصِلَيْنِ", "muttasil", "noun", [K, NA, MTH, IFA, F8], "نَعْتٌ مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنِ اتَّصَلَ.", "«attached» — the naʿt.", "«muttasıl» — sıfat."),
  tok("مُتَّحِدَيِ", "muttahid", "noun", [K, NA, MTH, ID, IFA, F8], "نَعْتٌ ثَانٍ مَنْصُوبٌ بِالْيَاءِ، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَكُسِرَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ، مُضَافٌ.", "«of one» — a second naʿt; the dual's nūn dropped for the annexation, its yāʾ given a kasra for the two sukūns.", "«aynı … olan» — ikinci sıfat; nûnu izâfet için düşmüş, yâsı iki sâkin için kesreli.", segments=[seg("مُتَّحِدَيِ", "muttahid", "noun")]),
  tok("الْمَعْنَى", "mana", "noun", [K, ID, MQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«meaning» — the maqṣūr.", "«mânâ» — maksûr.", punct="،"),
  nahw(),
  tok("عَلِمْتُنِي", "alima", "verb", [K, ZQ, FL, MB, HT, YA], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ — الْفَاعِلُ وَالْمَفْعُولُ ضَمِيرَانِ لِمُتَكَلِّمٍ وَاحِدٍ.", "«I knew myself» — the tāʾ the doer, the yāʾ the first object: two pronouns of one person.", "«kendimi bildim» — tâ fâil, yâ birinci mef'ûl: aynı kişinin iki zamiri.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron"), seg("نِي", "pron-1s", "pron")]),
  tok("قَائِمًا", "qaim", "noun", [K, MB, ZQ, MFN, IFA], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«standing» — the second object.", "«ayakta» — ikinci mef'ûl.", punct="،"),
  tok("وَجَهِلَ", "jahila", "verb", [K, AT, MK, HT, ZQ], "الْوَاوُ لِلِاسْتِئْنَافِ، وَجَهِلَ لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ — مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and جَهِلَ» — the verb mentioned as a word: the mubtada.", "«ve cehile» — lafzı kastedilen fiil: mübtedâ.", segments=wa("جَهِلَ", "jahila", "verb")),
  tok("وَعَدِمَ", "adima", "verb", [K, AT, HT, ZQ], "الْوَاوُ عَاطِفَةٌ، وَعَدِمَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and عَدِمَ» — joined; mentioned as a word.", "«ve adime» — ma'tûf; lafzı kastedilen.", segments=wa("عَدِمَ", "adima", "verb")),
  tok("وَفَقَدَ", "faqada", "verb", [K, AT, HT, ZQ], "الْوَاوُ عَاطِفَةٌ، وَفَقَدَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ رَفْعٍ.", "«and فَقَدَ» — joined; mentioned as a word.", "«ve fekade» — ma'tûf; lafzı kastedilen.", segments=wa("فَقَدَ", "faqada", "verb")),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("هٰذَا", "hadha", "pron", [K, HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَجْرُورٌ بِفِي فِي مَحَلِّ جَرٍّ.", "«this» — the demonstrative under «in».", "«bu» — fî'nin mecrûru."),
  tok("الْجَوَازِ", "jawaz", "noun", [K, BD, MSD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«permission» — the badal of the demonstrative.", "«cevaz» — işaret isminin bedeli."),
  tok("عَلَى", "ala", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«on» — the khabar.", "«üzere» — haber."),
  tok("حَدِّهَا", "hadd", "noun", [K, HJ, ID, DV], "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — عَلَى حَدِّ أَفْعَالِ الْقُلُوبِ: مِثْلِهَا فِي الْحُكْمِ.", "«on their footing» — like the verbs of the heart in the ruling.", "«onların hükmünde» — kalp fiilleri gibi.", punct="،", segments=[seg("حَدِّ", "hadd", "noun"), pr3fs()]),
  tok("وَمِنْهَا", "min", "prep", [K, AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and among them» — the fronted khabar.", "«ve onlardan» — mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("جَوَازُ", "jawaz", "noun", [K, MK, ID, MSD], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the permissibility of» — the delayed mubtada.", "«câiz olması» — muahhar mübtedâ."),
  tok("دُخُولِ", "dukhul", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى فَاعِلِهِ.", "«the entering of» — the masdar annexed to its doer.", "«girmesi» — fâiline muzâf masdar."),
  tok("أَنَّ", "anna", "part", [K, ID, IN, HT, "mawadi-fath-anna"], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«أَنَّ» — the particle mentioned as a word, annexed to.", "«enne» — lafzı kastedilen harf, muzâfun ileyh."),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("مَفْعُولَيْهَا", "maful-object", "noun", [K, HJ, ID, MTH, MFN], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their two objects»", "«iki mef'ûlüne»", punct="،", segments=[seg("مَفْعُولَيْ", "maful-object", "noun"), pr3fs()]),
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, ZQ, FL, HT], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ سَدَّ مَسَدَّ مَفْعُولَيْهِ.", "«I knew» — the أَنَّ-clause fills the place of its two objects.", "«bildim» — enne'li cümle iki mef'ûlünün yerini tutar.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَنَّ", "anna", "part", [K, IN, "mawadi-fath-anna", ZQ], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ مَصْدَرِيٌّ — مَفْتُوحٌ لِوُقُوعِهِ مَوْقِعَ الْمَفْعُولَيْنِ.", "«that» — fatḥa, standing where the two objects stand.", "«-dığını» — iki mef'ûlün yerinde olduğu için fetha."),
  zayd("زَيْدًا", "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the ism of أَنَّ.", "«Zeyd'in» — enne'nin ismi.", tags=[IN]),
  tok("قَائِمٌ", "qaim", "noun", [K, IN, IFA], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«is standing» — the khabar of أَنَّ.", "«ayakta olduğunu» — enne'nin haberi.", punct="."),
 ]})
# ----------- s7 — the taʿlīq defined
S.append({"id": "s7", "translation": {"en": "And as for the taʿlīq by a word of question, or of negation, or by the lām of ibtidāʾ, or by the oath, or by إِنَّ with the kasra when the lām of ibtidāʾ enters its khabar — that is, the annulment of the work of necessity in wording, not in meaning — it is general over these verbs.", "tr": "Soru kelimesiyle, nefiyle, ibtidâ lâmıyla, kasemle yahut haberine ibtidâ lâmı girdiğinde meksûr inne ile TA'LÎK'e gelince — yani amelin vücûben, mânâca değil lafzen iptali — bu fiillerin hepsini kapsar."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, AMM], "الْوَاوُ لِلِاسْتِئْنَافِ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for» — the particle of detailing.", "«… -e gelince» — tafsîl harfi.", segments=wa("أَمَّا", "amma", "part")),
  tok("التَّعْلِيقُ", "taliq", "noun", [K, MK, ZQ, MSD, AMM], "مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ عَلَّقَ: تَرْكُ الْعَمَلِ لَفْظًا لَا مَحَلًّا.", "«the taʿlīq» — the mubtada; suspending the work in wording, not in place.", "«ta'lîk» — mübtedâ; ameli lafzen askıya almak."),
  tok("بِكَلِمَةِ", "kalima", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَكَلِمَةِ مَجْرُورٌ، مُضَافٌ — مُتَعَلِّقٌ بِالتَّعْلِيقِ.", "«by a word of» — hanging on the taʿlīq.", "«… kelimesiyle» — ta'lîk'e müteallik.", segments=[seg("بِ", "bi", "prep"), seg("كَلِمَةِ", "kalima", "noun")]),
  tok("الِاسْتِفْهَامِ", "istifham", "noun", [K, ID, IS, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ اسْتَفْهَمَ.", "«question»", "«istifhâm»"),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or» — kasra for the two sukūns.", "«yahut» — iki sâkin için kesre."),
  tok("النَّفْيِ", "nafy", "noun", [K, AT, MSD], "مَعْطُوفٌ عَلَى الِاسْتِفْهَامِ مَجْرُورٌ.", "«negation» — joined.", "«nefiy» — ma'tûf."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  tok("لَامِ", "lam-letter", "noun", [K, AT, ID], "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ — اسْمُ الْحَرْفِ.", "«the lām of» — the letter's name, annexed.", "«lâmı» — harfin adı, muzâf."),
  tok("الِابْتِدَاءِ", "ibtida-start", "noun", [K, ID, MKI, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — لَامُ الِابْتِدَاءِ: الَّتِي تُؤَكِّدُ مَضْمُونَ الْجُمْلَةِ.", "«ibtidāʾ» — the lām that emphasises the sentence.", "«ibtidâ» — cümleyi te'kid eden lâm."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«yahut»"),
  tok("الْقَسَمِ", "qasam", "noun", [K, AT], "مَعْطُوفٌ مَجْرُورٌ.", "«the oath»", "«kasem»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  tok("إِنَّ", "inna", "part", [K, AT, IN, MKI, HT], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«إِنَّ» — the particle mentioned as a word, joined.", "«inne» — lafzı kastedilen harf, ma'tûf."),
  tok("الْمَكْسُورَةِ", "maksur", "noun", [K, NA, IMF, MKI], "نَعْتٌ لِإِنَّ مَجْرُورٌ — ذَاتِ الْهَمْزَةِ الْمَكْسُورَةِ.", "«with the kasra» — the naʿt: its hamza carrying a kasra.", "«meksûr» — sıfat: hemzesi kesreli."),
  tok("إِذَا", "idha", "part", [K, "idha-shartiyya", MF], "ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«-dığında»"),
  tok("دَخَلَ", "dakhala", "verb", [K, FL, "idha-shartiyya"], "فِعْلٌ مَاضٍ — فِعْلُ الشَّرْطِ، وَالْفَاعِلُ بَعْدَهُ.", "«enters» — the sharṭ; its doer follows.", "«girdiğinde» — şart fiili; fâil sonra."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-e»"),
  tok("خَبَرِهَا", "khabar-predicate", "noun", [K, HJ, ID, IN], "مَجْرُورٌ بِفِي، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرُ إِنَّ.", "«its khabar» — the khabar of إِنَّ.", "«haberine» — inne'nin haberi.", segments=[seg("خَبَرِ", "khabar-predicate", "noun"), pr3fs()]),
  tok("لَامُ", "lam-letter", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the lām of» — the doer.", "«lâmı» — fâil."),
  tok("الِابْتِدَاءِ", "ibtida-start", "noun", [K, ID, MKI], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ibtidāʾ»", "«ibtidâ»", punct="،"),
  tok("أَيْ", "ay", "part", [K, HT], "حَرْفُ تَفْسِيرٍ.", "«that is»", "«yani»"),
  tok("إِبْطَالُ", "ibtal", "noun", [K, BD, ID, MSD, "form-iv-verbs"], "عَطْفُ بَيَانٍ لِلتَّعْلِيقِ، أَوْ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هُوَ إِبْطَالُ — مَصْدَرُ أَبْطَلَ، مُضَافٌ.", "«the annulment of» — explains the taʿlīq; the masdar of أَبْطَلَ.", "«iptali» — ta'lîk'i açıklar; ebtale'nin masdarı."),
  tok("الْعَمَلِ", "amal-governing", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the work»", "«amelin»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«by way of»", "«… yoluyla»"),
  tok("سَبِيلِ", "sabil", "noun", [K, HJ, ID], "مَجْرُورٌ بِعَلَى، مُضَافٌ.", "«way»", "«yol»"),
  tok("الْوُجُوبِ", "wujub", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«necessity»", "«vücûb»"),
  tok("لَفْظًا", "lafz", "noun", [K, TM], "تَمْيِيزٌ مَنْصُوبٌ، أَوْ حَالٌ — مِنْ جِهَةِ اللَّفْظِ.", "«in wording» — the tamyīz.", "«lafzen» — temyiz."),
  tok("لَا", "la-nafiya", "part", [K, LN, AT], "حَرْفُ عَطْفٍ يُفِيدُ النَّفْيَ.", "«not» — the joining lā.", "«değil» — nefiy bildiren atıf."),
  tok("مَعْنًى", "mana", "noun", [K, AT, TM, MQ], "مَعْطُوفٌ عَلَى لَفْظًا مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — مَقْصُورٌ مُنَوَّنٌ.", "«in meaning» — joined; the maqṣūr with its tanwīn.", "«mânen» — ma'tûf; tenvinli maksûr.", punct="،"),
  tok("فَيَعُمُّ", "amma-include", "verb", [K, AMM, FL, DV], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَيَعُمُّ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مُضَاعَفٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (التَّعْلِيقُ) — وَالْجُمْلَةُ خَبَرٌ.", "«it is general over» — the fāʾ of ammā's answer; the clause is the khabar.", "«kapsar» — emmâ'nın cevabının fâsı; cümle haber.", segments=[seg("فَ", "fa", "conj"), seg("يَعُمُّ", "amma-include", "verb")]),
  tok("هٰذِهِ", "hadhihi", "pron", [K, MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.", "«these» — the object.", "«bu» — mef'ûl."),
  tok("الْأَفْعَالَ", "fil", "noun", [K, BD, MB, ZQ, "jam-taksir"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«verbs» — the badal.", "«fiilleri» — bedel.", punct="،"),
 ]})
# ----------- s8 — the examples of the taʿlīq
S.append({"id": "s8", "translation": {"en": "As in «I knew — is Zayd at your place, or ʿAmr?», «I saw — Zayd is not departing», «I found — surely Zayd is departing», and «I knew — indeed Zayd is standing».", "tr": "«Bildim — Zeyd mi senin yanında, yoksa Amr mı?», «gördüm — Zeyd gitmiyor», «buldum — elbette Zeyd gidiyor» ve «bildim — şüphesiz Zeyd ayaktadır» gibi."},
 "tokens": [
  nahw(),
  tok("عَلِمْتُ", "alima", "verb", [K, ZQ, FL, HT, IS], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُعَلَّقٌ عَنِ الْعَمَلِ بِهَمْزَةِ الِاسْتِفْهَامِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ الْمَفْعُولَيْنِ.", "«I knew» — suspended by the question hamza; the clause after it stands for the two objects.", "«bildim» — soru hemzesiyle muallak; sonraki cümle iki mef'ûlün yerini tutar.", segments=[seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("أَزَيْدٌ", "zayd", "propn", [K, IS, MK], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«is Zayd» — the question hamza; the mubtada.", "«Zeyd mi» — soru hemzesi; mübtedâ.", segments=[seg("أَ", "hamza-istifham", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  tok("عِنْدَكَ", "inda", "noun", [K, MF, ID, MK], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«at your place» — the khabar.", "«senin yanında» — haber.", segments=[seg("عِنْدَ", "inda", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَمْ", "am", "part", [K, AT, IS], "حَرْفُ عَطْفٍ لِلتَّعْيِينِ بَعْدَ هَمْزَةِ الِاسْتِفْهَامِ — الْمُتَّصِلَةُ.", "«or» — the am of choice after the hamza.", "«yoksa» — hemzeden sonra tayin bildiren em."),
  tok("عَمْرٌو", "amr-name", "propn", [K, AT, IS], "مَعْطُوفٌ عَلَى زَيْدٌ مَرْفُوعٌ — وَالْوَاوُ زَائِدَةٌ فِي الْخَطِّ لِلْفَرْقِ بَيْنَهُ وَبَيْنَ عُمَرَ.", "«ʿAmr» — joined to Zayd; the silent wāw tells him from ʿUmar.", "«yoksa Amr mı» — Zeyd'e ma'tûf; sessiz vâv onu Ömer'den ayırır.", punct="،"),
  tok("وَرَأَيْتُ", "raa", "verb", [K, AT, ZQ, FL, HT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَأَيْتُ لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُعَلَّقٌ بِمَا النَّافِيَةِ، وَالتَّاءُ فَاعِلٌ.", "«and I saw» — suspended by the negating mā.", "«ve gördüm» — nâfiye mâ ile muallak.", segments=[seg("وَ", "wa", "conj"), seg("رَأَيْ", "raa", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مَا", "ma-nafiya", "part", [K, LN, "anwa-ma", "ma-la-laysa-wa-la-al-jins"], "حَرْفُ نَفْيٍ — مُعَلِّقٌ لِلْفِعْلِ.", "«not» — the suspender.", "«-mez» — muallik."),
  zayd("زَيْدٌ", "مُبْتَدَأٌ مَرْفُوعٌ.", "«Zayd» — the mubtada.", "«Zeyd» — mübtedâ.", tags=[MK]),
  tok("مُنْطَلِقٌ", "muntaliq", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«departing» — the khabar.", "«gitmiyor» — haber.", punct="،"),
  tok("وَوَجَدْتُ", "wajada", "verb", [K, AT, ZQ, FL, HT, "mithal-verbs"], "الْوَاوُ عَاطِفَةٌ، وَوَجَدْتُ لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُعَلَّقٌ بِلَامِ الِابْتِدَاءِ، وَالتَّاءُ فَاعِلٌ.", "«and I found» — suspended by the lām of ibtidāʾ.", "«ve buldum» — ibtidâ lâmıyla muallak.", segments=[seg("وَ", "wa", "conj"), seg("وَجَدْ", "wajada", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("لَزَيْدٌ", "zayd", "propn", [K, MK, MKI], "اللَّامُ لَامُ الِابْتِدَاءِ، وَزَيْدٌ مُبْتَدَأٌ مَرْفُوعٌ.", "«surely Zayd» — the lām of ibtidāʾ; the mubtada.", "«elbette Zeyd» — ibtidâ lâmı; mübtedâ.", segments=[seg("لَ", "lam-ibtida", "part"), seg("زَيْدٌ", "zayd", "propn")]),
  tok("مُنْطَلِقٌ", "muntaliq", "noun", [K, MK, IFA], "خَبَرٌ مَرْفُوعٌ.", "«departing» — the khabar.", "«gidiyor» — haber.", punct="،"),
  tok("وَعَلِمْتُ", "alima", "verb", [K, AT, ZQ, FL, HT, MKI], "الْوَاوُ عَاطِفَةٌ، وَعَلِمْتُ لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ مُعَلَّقٌ بِإِنَّ الْمَكْسُورَةِ لِدُخُولِ اللَّامِ فِي خَبَرِهَا، وَالتَّاءُ فَاعِلٌ.", "«and I knew» — suspended by إِنَّ, kasra'd for the lām in its khabar.", "«ve bildim» — haberinde lâm olduğu için meksûr inne ile muallak.", segments=[seg("وَ", "wa", "conj"), seg("عَلِمْ", "alima", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("إِنَّ", "inna", "part", [K, IN, MKI], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — كُسِرَتْ هَمْزَتُهَا لِدُخُولِ لَامِ الِابْتِدَاءِ فِي خَبَرِهَا.", "«indeed» — its hamza kasra'd by the lām in its khabar.", "«şüphesiz» — haberindeki lâm için hemzesi meksûr."),
  zayd("زَيْدًا", "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Zayd» — the ism of إِنَّ.", "«Zeyd» — inne'nin ismi.", tags=[IN]),
  tok("لَقَائِمٌ", "qaim", "noun", [K, IN, MKI, IFA], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَقَائِمٌ خَبَرُ إِنَّ مَرْفُوعٌ.", "«is standing» — the slid lām; the khabar of إِنَّ.", "«ayaktadır» — kaydırılmış lâm; inne'nin haberi.", punct=".", segments=[seg("لَ", "lam-ibtida", "part"), seg("قَائِمٌ", "qaim", "noun")]),
 ]})
# ----------- s9 — every verb of the heart, every verb seeking knowledge, the senses
S.append({"id": "s9", "translation": {"en": "And every verb of the heart other than these — such as «I doubted», «I made out», «I forgot» — and every verb by which knowledge is sought, as in «I tested» and «I asked»; and among them are the verbs of the five senses, such as «I touched», «I saw», «I heard», «I smelt» and «I tasted».", "tr": "Bunların dışındaki her kalp fiilini de — «şüphe ettim», «anladım», «unuttum» gibi — ve kendisiyle bilgi istenen her fiili de — «sınadım» ve «sordum» gibi; beş duyunun fiilleri de bunlardandır: «dokundum», «gördüm», «işittim», «kokladım» ve «tattım» gibi."},
 "tokens": [
  tok("وَكُلَّ", "kull", "noun", [K, AT, MB, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلَّ مَعْطُوفٌ عَلَى هٰذِهِ الْأَفْعَالَ فِي الْجُمْلَةِ قَبْلَهَا مَنْصُوبٌ، مُضَافٌ — مَفْعُولُ يَعُمُّ.", "«and every» — joined to «these verbs» of the sentence before: the object of «is general over».", "«ve her» — önceki cümledeki «bu fiiller»e ma'tûf, mansûb: ye'ummü'nün mef'ûlü.", segments=wa("كُلَّ", "kull", "noun")),
  tok("فِعْلٍ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«verb»", "«fiili»"),
  tok("قَلْبِيٍّ", "qalbi", "noun", [K, NA, NSB], "نَعْتٌ مَجْرُورٌ.", "«of the heart»", "«kalbî»"),
  tok("غَيْرَ", "ghayr", "noun", [K, NA, ID], "نَعْتٌ ثَانٍ لِفِعْلٍ، أَوْ حَالٌ — مَنْصُوبٌ، مُضَافٌ: غَيْرَ هٰذِهِ الْأَفْعَالِ.", "«other than» — a second naʿt (or the ḥāl), annexed.", "«dışındaki» — ikinci sıfat (yahut hâl), muzâf."),
  tok("هٰذِهِ", "hadhihi", "pron", [K, ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.", "«these»", "«bunların»"),
  tok("كَشَكَكْتُ", "shakka", "verb", [K, HJ, HT, DV, ZQ], "الْكَافُ حَرْفُ جَرٍّ لِلتَّمْثِيلِ، وَشَكَكْتُ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ: فِعْلٌ مَاضٍ مُضَاعَفٌ فُكَّ إِدْغَامُهُ قَبْلَ التَّاءِ، وَالتَّاءُ فَاعِلٌ.", "«such as I doubted» — the kāf of «for instance»; the doubled verb unpacked before the tāʾ.", "«şüphe ettim gibi» — temsil kâfı; muzâaf, tâ'dan önce fekk.", segments=[seg("كَ", "ka", "prep"), seg("شَكَكْ", "shakka", "verb"), seg("تُ", "pron-1s", "pron")]),
  qv1("تَبَيَّنْتُ", "tabayyana", "تَبَيَّنْ", "«and I made out» — joined.", "«ve anladım» — ma'tûf.", extra=[F5]),
  qv1("نَسِيتُ", "nasiya", "نَسِي", "«and I forgot» — the nāqiṣ keeps its yāʾ before the tāʾ.", "«ve unuttum» — nâkıs, tâ'dan önce yâsı kalır.", punct="،", extra=["naqis-verbs"]),
  tok("وَكُلَّ", "kull", "noun", [K, AT, MB, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلَّ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and every» — joined, in naṣb.", "«ve her» — ma'tûf, mansûb.", segments=wa("كُلَّ", "kull", "noun")),
  tok("فِعْلٍ", "fil", "noun", [K, ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لَهُ.", "«verb» — the clause after it its naʿt.", "«fiili» — sonraki cümle sıfatı."),
  tok("يُطْلَبُ", "talaba", "verb", [K, JS, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَالْجُمْلَةُ نَعْتٌ لِفِعْلٍ.", "«is sought» — the passive; the ṣifa clause.", "«istenen» — meçhul; sıfat cümlesi."),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — عَائِدٌ إِلَى فِعْلٍ.", "«by it» — the returning pronoun.", "«kendisiyle» — âid zamir.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الْعِلْمُ", "ilm", "noun", [K, NF], "نَائِبُ الْفَاعِلِ مَرْفُوعٌ بِالضَّمَّةِ.", "«knowledge» — the deputy doer.", "«bilgi» — nâib-i fâil.", punct="،"),
  nahw(),
  qv1("امْتَحَنْتُ", "imtahana", "امْتَحَنْ", "«I tested» — annexed to «as in».", "«sınadım» — meselâ'ya muzâf.", joined=False, extra=[F8]),
  qv1("سَأَلْتُ", "saala", "سَأَلْ", "«and I asked»", "«ve sordum»", punct="،"),
  tok("وَمِنْهَا", "min", "prep", [K, AT, HJ, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنْ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ: مِنَ الْأَفْعَالِ الَّتِي يَعُمُّهَا التَّعْلِيقُ.", "«and among them» — the fronted khabar: among the verbs the taʿlīq covers.", "«bunlardandır» — mukaddem haber: ta'lîkin kapsadığı fiillerden.", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep"), seg("هَا", "pron-3fs", "pron")]),
  tok("أَفْعَالُ", "fil", "noun", [K, MK, ID, "jam-taksir"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the verbs of» — the delayed mubtada.", "«fiilleri» — muahhar mübtedâ."),
  tok("الْحَوَاسِّ", "hawass", "noun", [K, ID, "jam-taksir", MNS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ حَاسَّةٍ عَلَى فَوَاعِلَ.", "«the senses» — the plural of حَاسَّة.", "«duyuların» — hâsse'nin cemi."),
  tok("الْخَمْسِ", "khams", "noun", [K, NA], "نَعْتٌ لِلْحَوَاسِّ مَجْرُورٌ — الْعَدَدُ نَعْتًا.", "«five» — the number as a naʿt.", "«beş» — sıfat olarak sayı."),
  tok("كَلَمَسْتُ", "lamasa", "verb", [K, HJ, HT], "الْكَافُ حَرْفُ جَرٍّ لِلتَّمْثِيلِ، وَلَمَسْتُ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«such as I touched» — the kāf of «for instance».", "«dokundum gibi» — temsil kâfı.", segments=[seg("كَ", "ka", "prep"), seg("لَمَسْ", "lamasa", "verb"), seg("تُ", "pron-1s", "pron")]),
  qv1("أَبْصَرْتُ", "absara", "أَبْصَرْ", "«and I saw»", "«ve gördüm»", extra=["form-iv-verbs"]),
  qv1("سَمِعْتُ", "samia", "سَمِعْ", "«and I heard»", "«ve işittim»"),
  qv1("شَمَمْتُ", "shamma", "شَمَمْ", "«and I smelt» — the doubled verb unpacked.", "«ve kokladım» — muzâaf, fekk.", extra=[DV]),
  qv1("ذُقْتُ", "dhaqa", "ذُقْ", "«and I tasted» — the hollow verb shortened before the tāʾ.", "«ve tattım» — ecvef, kısalmış.", punct=".", extra=[HV]),
 ]})
# ----------- s10 — the mulḥaq
S.append({"id": "s10", "translation": {"en": "And the third division is verbs attached to the verbs of the heart merely in entering on the mubtadaʾ and the khabar and in the impermissibility of dropping both together, or one alone, without a clue — and the dropping of one alone with a clue is rare — as in صَيَّرَ, جَعَلَ, تَرَكَ and اتَّخَذَ.", "tr": "Üçüncü kısım, yalnızca mübtedâ ve habere dâhil olmakta ve karînesiz ikisini birlikte yahut yalnız birini hazfetmenin câiz olmamasında kalp fiillerine ilhak edilen fiillerdir — karîneyle yalnız birini hazfetmek azdır — sayyera, ceale, terake ve ittehaze gibi."},
 "tokens": [
  *qism("الثَّالِثُ", "thalith", "نَعْتٌ مَرْفُوعٌ.", "«the third» — the naʿt.", "«üçüncü» — sıfat.", joined=True),
  tok("أَفْعَالٌ", "fil", "noun", [K, MK, "jam-taksir"], "خَبَرٌ مَرْفُوعٌ.", "«verbs» — the khabar.", "«fiillerdir» — haber."),
  tok("مُلْحَقَةٌ", "mulhaq", "noun", [K, NA, IMF, TSY], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ أَلْحَقَ.", "«attached» — the naʿt; ism mafʿūl of أَلْحَقَ.", "«ilhak edilmiş» — sıfat; elhaka'nın ism-i mef'ûlü."),
  tok("بِأَفْعَالِ", "fil", "noun", [K, HJ, ID, ZQ, "jam-taksir"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَفْعَالِ مَجْرُورٌ، مُضَافٌ — مُتَعَلِّقٌ بِمُلْحَقَةٍ.", "«to the verbs of» — hanging on «attached».", "«fiillerine» — mülhaka'ya müteallik.", segments=[seg("بِ", "bi", "prep"), seg("أَفْعَالِ", "fil", "noun")]),
  tok("الْقُلُوبِ", "qalb", "noun", [K, ID, ZQ, "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the heart»", "«kalp»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("مُجَرَّدِ", "mujarrad", "noun", [K, HJ, ID, IMF], "مَجْرُورٌ بِفِي، مُضَافٌ — اسْمُ مَفْعُولٍ مِنْ جَرَّدَ: مُجَرَّدُ الدُّخُولِ: الدُّخُولُ وَحْدَهُ.", "«merely» — «the mere entering»: the entering alone.", "«yalnızca» — «mücerred duhûl»: yalnız girmek.", segments=[seg("مُجَرَّدِ", "mujarrad", "noun")]),
  tok("الدُّخُولِ", "dukhul", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«entering»", "«girmek»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-e»"),
  tok("الْمُبْتَدَإِ", "mubtada", "noun", [K, HJ, MK], "مَجْرُورٌ بِعَلَى.", "«the mubtada»", "«mübtedâya»"),
  tok("وَالْخَبَرِ", "khabar-predicate", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْخَبَرِ مَعْطُوفٌ مَجْرُورٌ.", "«and the khabar»", "«ve habere»", segments=wa("الْخَبَرِ", "khabar-predicate", "noun")),
  tok("وَعَدَمِ", "adam", "noun", [K, AT, ID, MSD], "الْوَاوُ عَاطِفَةٌ، وَعَدَمِ مَعْطُوفٌ عَلَى مُجَرَّدِ مَجْرُورٌ، مُضَافٌ.", "«and the absence of» — joined to «merely».", "«ve … olmaması» — mücerred'e ma'tûf.", segments=wa("عَدَمِ", "adam", "noun")),
  tok("جَوَازِ", "jawaz", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the permissibility of»", "«câiz»"),
  tok("حَذْفِهِمَا", "hadhf", "noun", [K, ID, HM, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ.", "«dropping both»", "«ikisini hazfetmenin»", segments=[seg("حَذْفِ", "hadhf", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  ma_an_pl(),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«yahut»"),
  ahadihima(role_ar="مَعْطُوفٌ عَلَى حَذْفِهِمَا مَجْرُورٌ، مُضَافٌ، وَهُمَا مُضَافٌ إِلَيْهِ", en="«one of the two» — joined to «dropping both»", tr="«birini» — ma'tûf"),
  faqat(),
  tok("بِلَا", "la-nafiya", "part", [K, HJ, LN], "الْبَاءُ حَرْفُ جَرٍّ، وَلَا اسْمٌ بِمَعْنَى غَيْرٍ مَجْرُورٌ، مُضَافٌ — بِلَا قَرِينَةٍ: بِغَيْرِ قَرِينَةٍ.", "«without» — بِ + لَا as a noun meaning «other than».", "«-sız» — bi + lâ, «gayr» mânâsında.", segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part")]),
  tok("قَرِينَةٍ", "qarina", "noun", [K, ID, HM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a clue»", "«karîne»", punct="،"),
  tok("وَقَلَّ", "qalla", "verb", [K, AT, FL, HM, DV], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَلَّ فِعْلٌ مَاضٍ مُضَاعَفٌ، وَفَاعِلُهُ حَذْفُ.", "«and is rare» — its doer «the dropping».", "«ve azdır» — fâili hazf.", segments=wa("قَلَّ", "qalla", "verb")),
  hadhf_(role_ar="فَاعِلٌ مَرْفُوعٌ، مُضَافٌ", en="«the dropping of» — the doer, annexed", tr="«hazfi» — fâil, muzâf"),
  ahadihima(),
  faqat(),
  tok("بِهَا", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — بِالْقَرِينَةِ.", "«with it» — with the clue.", "«onunla» — karîneyle.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  nahw(),
  tok("صَيَّرَ", "sayyara", "verb", [K, TSY, HT, ID, "form-ii-verbs"], "لَفْظٌ مَحْكِيٌّ قُصِدَ لَفْظُهُ، مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — فِعْلٌ مَاضٍ.", "«صَيَّرَ — to make into» — the verb mentioned as a word.", "«sayyera — kılmak» — lafzı kastedilen fiil."),
  tok("وَجَعَلَ", "jaala", "verb", [K, AT, TSY, HT], "الْوَاوُ عَاطِفَةٌ، وَجَعَلَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and جَعَلَ — to make»", "«ve ceale — kılmak»", segments=wa("جَعَلَ", "jaala", "verb")),
  tok("وَتَرَكَ", "taraka", "verb", [K, AT, TSY, HT], "الْوَاوُ عَاطِفَةٌ، وَتَرَكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ.", "«and تَرَكَ — to leave (in a state)»", "«ve terake — (bir hâlde) bırakmak»", segments=wa("تَرَكَ", "taraka", "verb")),
  tok("وَاتَّخَذَ", "ittakhadha", "verb", [K, AT, TSY, HT, F8], "الْوَاوُ عَاطِفَةٌ، وَاتَّخَذَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ فِي مَحَلِّ جَرٍّ — افْتَعَلَ مِنْ أَخَذَ، أُبْدِلَتْ هَمْزَتُهُ تَاءً وَأُدْغِمَتْ.", "«and اتَّخَذَ — to take as» — Form VIII of أَخَذَ, its hamza turned tāʾ and merged.", "«ve ittehaze — edinmek» — ahaze'nin iftiâli, hemzesi tâ olup idgam edilmiş.", punct=".", segments=wa("اتَّخَذَ", "ittakhadha", "verb")),
 ]})

for s in S:
    for t in s["tokens"]:
        t["grammar"] = [g for i, g in enumerate(t["grammar"]) if g not in t["grammar"][:i]]

CAND = {
 "mubayin": G("mubayin", "مُبَايِن", "ب ي ن", "noun", "different, distinct from (ism fāʿil of بَايَنَ)", "mübâyin — ayrı, farklı", 4),
 "qalbi": G("qalbi", "قَلْبِيّ", "ق ل ب", "noun", "of the heart (nisba of قَلْب)", "kalbî — kalbe ait", 3),
 "maan": G("maan", "مَعًا", "م ع ع", "adv", "together, both at once", "birlikte, beraber", 2),
 "khasisa": G("khasisa", "خَصِيصَة", "خ ص ص", "noun", "a property, a peculiarity", "hususiyet, özellik", 4, plural="خَصَائِص"),
 "tawassata": G("tawassata", "تَوَسَّطَ", "و س ط", "verb", "to stand in the middle, to come between (Form V)", "ortasında bulunmak, araya girmek (tefa''ul)", 3, form="V"),
 "taakhkhara": G("taakhkhara", "تَأَخَّرَ", "أ خ ر", "verb", "to come after, to be delayed (Form V)", "sonra gelmek, gecikmek (tefa''ul)", 3, form="V"),
 "muttahid": G("muttahid", "مُتَّحِد", "و ح د", "noun", "one and the same, united (ism fāʿil of اتَّحَدَ)", "müttehid — bir ve aynı", 4),
 "adima": G("adima", "عَدِمَ", "ع د م", "verb", "to lack, to miss, to be without (bāb سَمِعَ)", "yoksun olmak, kaybetmek (semia bâbı)", 3),
 "taliq": G("taliq", "تَعْلِيق", "ع ل ق", "noun", "the taʿlīq — suspending a verb's work in wording while it stands in sense (masdar of عَلَّقَ)", "ta'lîk — fiilin amelini mânâca durur lafzen askıya almak (allaka'nın masdarı)", 5),
 "istifham": G("istifham", "اِسْتِفْهَام", "ف ه م", "noun", "questioning, the interrogative (masdar of اسْتَفْهَمَ)", "istifhâm — soru (istefheme'nin masdarı)", 3),
 "ibtal": G("ibtal", "إِبْطَال", "ب ط ل", "noun", "annulment, voiding (masdar of أَبْطَلَ)", "iptal — geçersiz kılma (ebtale'nin masdarı)", 4),
 "amma-include": G("amma-include", "عَمَّ", "ع م م", "verb", "to be general over, to include all (doubled; عَمَّ يَعُمُّ)", "kapsamak, umûmî olmak (muzâaf; amme ye'ummü)", 3),
 "dhaqa": G("dhaqa", "ذَاقَ", "ذ و ق", "verb", "to taste (hollow; ذُقْتُ)", "tatmak (ecvef; zuktü)", 2),
 "hab-suppose": G("hab-suppose", "هَبْ", "و ه ب", "part", "suppose! — the frozen imperative of وَهَبَ used as a verb of the heart («I reckon»)", "farz et! — vehebe'nin kalp fiili olarak kullanılan câmid emri («sanırım»)", 4),
 "zaama-claim": G("zaama-claim", "زَعَمَ", "ز ع م", "verb", "to claim, to allege, to suppose (a verb of the heart)", "iddia etmek, sanmak (kalp fiili)", 3),
 # reused from other packages (a key is a global claim)
 "jaaza": G("jaaza", "جَازَ", "ج و ز", "verb", "to be permitted", "câiz olmak", 2),
 "qarina": G("qarina", "قَرِينَة", "ق ر ن", "noun", "a clue, a contextual sign", "karîne", 3),
 "aata": G("aata", "أَعْطَى", "ع ط و", "verb", "to give", "vermek", 1),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "heart", "kalp", 1, plural="قُلُوب"),
 "dalla": G("dalla", "دَلَّ", "د ل ل", "verb", "to indicate, to signify", "delâlet etmek", 2),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find", "bulmak", 1),
 "khala-think": G("khala-think", "خَالَ", "خ ي ل", "verb", "to imagine, to suppose", "sanmak, hayal etmek", 3),
 "hasiba": G("hasiba", "حَسِبَ", "ح س ب", "verb", "to reckon, to suppose", "saymak, sanmak", 2),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, frequent", "çok olmak", 2),
 "qalla": G("qalla", "قَلَّ", "ق ل ل", "verb", "to be few, rare", "az olmak", 2),
 "faqat": G("faqat", "فَقَطْ", "ق ط ط", "adv", "only", "yalnız, sadece", 1),
 "jawaz": G("jawaz", "جَوَاز", "ج و ز", "noun", "permissibility", "cevaz, câiz olma", 3),
 "muntaliq": G("muntaliq", "مُنْطَلِق", "ط ل ق", "noun", "departing, setting out (ism fāʿil of انْطَلَقَ)", "giden, yola çıkan", 3),
 "muttasil": G("muttasil", "مُتَّصِل", "و ص ل", "noun", "attached, connected", "muttasıl — bitişik", 3),
 "jahila": G("jahila", "جَهِلَ", "ج ه ل", "verb", "to be ignorant of, not to know", "bilmemek", 2),
 "faqada": G("faqada", "فَقَدَ", "ف ق د", "verb", "to lose, to miss", "kaybetmek, yitirmek", 2),
 "hadd": G("hadd", "حَدّ", "ح د د", "noun", "limit; definition; footing", "had, sınır; tarif", 2),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "sabil": G("sabil", "سَبِيل", "س ب ل", "noun", "way, path", "yol", 2),
 "wujub": G("wujub", "وُجُوب", "و ج ب", "noun", "obligation, necessity", "vücûb, zorunluluk", 3),
 "shakka": G("shakka", "شَكَّ", "ش ك ك", "verb", "to doubt", "şüphe etmek", 2),
 "tabayyana": G("tabayyana", "تَبَيَّنَ", "ب ي ن", "verb", "to become clear; to make out", "açığa çıkmak; anlamak", 3, form="V"),
 "nasiya": G("nasiya", "نَسِيَ", "ن س ي", "verb", "to forget", "unutmak", 1),
 "talaba": G("talaba", "طَلَبَ", "ط ل ب", "verb", "to seek, to ask for", "istemek, aramak", 1),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim, bilgi", 1),
 "imtahana": G("imtahana", "اِمْتَحَنَ", "م ح ن", "verb", "to test, to examine", "sınamak, imtihan etmek", 3),
 "saala": G("saala", "سَأَلَ", "س أ ل", "verb", "to ask", "sormak", 1),
 "hawass": G("hawass", "حَوَاسّ", "ح س س", "noun", "the senses (plural of حَاسَّة)", "duyular (hâsse'nin cemi)", 3),
 "lamasa": G("lamasa", "لَمَسَ", "ل م س", "verb", "to touch", "dokunmak", 2),
 "absara": G("absara", "أَبْصَرَ", "ب ص ر", "verb", "to see, to perceive", "görmek", 2),
 "shamma": G("shamma", "شَمَّ", "ش م م", "verb", "to smell", "koklamak", 2),
 "mulhaq": G("mulhaq", "مُلْحَق", "ل ح ق", "noun", "attached to, annexed to (ism mafʿūl of أَلْحَقَ)", "mülhak — ilhak edilmiş", 3),
 "mujarrad": G("mujarrad", "مُجَرَّد", "ج ر د", "noun", "bare, mere", "mücerred — yalın, sırf", 3),
 "adam": G("adam", "عَدَم", "ع د م", "noun", "non-existence, absence", "yokluk, adem", 2),
 "sayyara": G("sayyara", "صَيَّرَ", "ص ي ر", "verb", "to make into, to turn into (Form II)", "kılmak, dönüştürmek (tef'îl)", 3),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make, to put", "kılmak, yapmak", 1),
 "taraka": G("taraka", "تَرَكَ", "ت ر ك", "verb", "to leave", "bırakmak", 1),
 "ittakhadha": G("ittakhadha", "اِتَّخَذَ", "أ خ ذ", "verb", "to take as, to adopt (Form VIII)", "edinmek (iftiâl)", 3),
 "am": G("am", "أَمْ", None, "part", "or (in a question with the hamza)", "yoksa (hemzeli soruda)", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
def doubled(bab, yv, m, mm, d, dd, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    b = _sg.BABS[bab]
    return _sg.idgham(_sg.entry(b[0] + " — مُضَاعَفٌ", b[1], masdar, fail, _sg.mazi14(m, mm), _sg.mudari14(yv, d, dd), amr,
                                "يَ" + d + "َ", "يَ" + d + "َ", "تَ" + d + "َ", maful, pmz, pmd, note))
put_morph(mo, "amma-include", doubled("nasara", "َ", "عَمّ", "عَمَم", "عُمّ", "عْمُم", ["عُمَّ", "عُمَّا", "عُمُّوا", "عُمِّي", "عُمَّا", "اُعْمُمْنَ"], "عُمُوم", "عَامّ", "مَعْمُوم", "عُمَّ", "يُعَمُّ", "عَمَّ الْحُكْمُ الْأَفْعَالَ يَعُمُّ عُمُومًا: شَمِلَهَا كُلَّهَا — مُضَاعَفٌ مِنْ بَابِ نَصَرَ."))
put_morph(mo, "dhaqa", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "ذَاق", "ذُق", "ذُوق", "ذُق", "ذُوق", "ذُق", "ذَوْق", "ذَائِق", "مَذُوق", "ذِيقَ", "يُذَاقُ", _sg.HOLLOW_NOTE.format(ex="ذُقْتَ")))
put_morph(mo, "adima", _sg.sound1("samia", "عَدِم", "عْدَم", "اِعْدَم", "عَدَم", "عَادِم", "مَعْدُوم", "عُدِمَ", "يُعْدَمُ", "عَدِمَ الشَّيْءَ يَعْدَمُ عَدَمًا: فَقَدَهُ — مِنْ بَابِ سَمِعَ."))
put_morph(mo, "zaama-claim", _sg.sound1("nasara", "زَعَم", "زْعُم", "اُزْعُم", "زَعْم", "زَاعِم", "مَزْعُوم", "زُعِمَ", "يُزْعَمُ", "زَعَمَ يَزْعُمُ زَعْمًا: قَالَ قَوْلًا يُشَكُّ فِيهِ؛ ظَنَّ — مِنْ أَفْعَالِ الْقُلُوبِ."))
put_morph(mo, "tawassata", _sg.derived(_sg.B5, _sg.W5, "َ", "تَوَسَّط", "تَوَسَّط", "تَوَسَّط", "تَوَسُّط", "مُتَوَسِّط", None, None, None, "تَوَسَّطَ الشَّيْءُ يَتَوَسَّطُ تَوَسُّطًا: صَارَ فِي الْوَسَطِ — لَازِمٌ، يَتَعَدَّى بِبَيْنَ."))
put_morph(mo, "taakhkhara", _sg.derived(_sg.B5, _sg.W5, "َ", "تَأَخَّر", "تَأَخَّر", "تَأَخَّر", "تَأَخُّر", "مُتَأَخِّر", None, None, None, "تَأَخَّرَ يَتَأَخَّرُ تَأَخُّرًا: جَاءَ بَعْدُ — لَازِمٌ، يَتَعَدَّى بِعَنْ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch9 gloss+morph ok", len(GLOSS_ADD), "verbs:", [k for k in ("amma-include", "dhaqa", "adima", "zaama-claim", "tawassata", "taakhkhara", "raa", "wajada", "khala-think", "hasiba", "sayyara", "ittakhadha") if k in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُتَعَدِّي وَأَضْرُبُهُ، وَأَفْعَالُ الْقُلُوبِ وَالتَّعْلِيقُ", "en": "The mutaʿaddī and its kinds; the verbs of the heart and the taʿlīq", "tr": "Müteaddî ve türleri; kalp fiilleri ve ta'lîk"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — العامل القياسي، الفعل المتعدي", "الكافية لابن الحاجب — أفعال القلوب", "قطر الندى لابن هشام — ظن وأخواتها"],
 "amil": "الْفِعْلُ الْمُتَعَدِّي — to one object, to two (the second a different thing; the verbs of the heart over a mubtadaʾ and a khabar; the attached صَيَّرَ family), to three; the taʿlīq suspends the work in wording",
 "question": {
  "en": ["What is a mutaʿaddī verb? One not understood without the thing the act fell upon: ضَرَبَ زَيْدٌ عَمْرًا needs ʿAmr.",
         "How many kinds? Three: to one object, to two objects, to three objects (أَعْلَمَ, أَرَى).",
         "May the single object be dropped? Yes — with a clue or without one (ضَرَبَ زَيْدٌ).",
         "What are the three divisions of the two-object verb? Where the second object is a DIFFERENT thing from the first (أَعْطَيْتُ زَيْدًا دِرْهَمًا); the VERBS OF THE HEART, whose two objects were a mubtadaʾ and a khabar (عَلِمْتُ زَيْدًا قَائِمًا); the verbs ATTACHED to them only in entering on a mubtadaʾ and khabar (صَيَّرَ، جَعَلَ، تَرَكَ، اتَّخَذَ).",
         "Which are the verbs of the heart? عَلِمَ، رَأَى، وَجَدَ، زَعَمَ، ظَنَّ، خَالَ، حَسِبَ, and the frozen هَبْ («suppose!»).",
         "May the objects of a verb of the heart be dropped? Never without a clue; with a clue both go together often, one alone rarely — because the two are a sentence, and half a sentence says nothing.",
         "What is ilghāʾ? When the verb stands BETWEEN its two objects or AFTER them, it may be stripped of its work and the two stay mubtadaʾ and khabar in rafʿ: زَيْدٌ عَلِمْتُ مُنْطَلِقٌ — or it may govern: زَيْدًا عَلِمْتُ مُنْطَلِقًا.",
         "What is the taʿlīq? The work annulled in WORDING but kept in SENSE, of necessity, when a question word, a negation, the lām of ibtidāʾ, an oath, or إِنَّ with the lām in its khabar stands between the verb and its two objects: عَلِمْتُ أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو، رَأَيْتُ مَا زَيْدٌ مُنْطَلِقٌ، وَجَدْتُ لَزَيْدٌ مُنْطَلِقٌ، عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ — the clause stands in the place of the two objects.",
         "What may be special to the verbs of the heart? Their doer and object may be two attached pronouns of ONE person (عَلِمْتُنِي قَائِمًا — shared with جَهِلَ، عَدِمَ، فَقَدَ); and أَنَّ may enter on their two objects (عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ).",
         "How far does the taʿlīq reach? To every verb of the heart (شَكَكْتُ، تَبَيَّنْتُ، نَسِيتُ), to every verb by which knowledge is sought (امْتَحَنْتُ، سَأَلْتُ), and to the verbs of the five senses (لَمَسْتُ، أَبْصَرْتُ، سَمِعْتُ، شَمَمْتُ، ذُقْتُ)."],
  "tr": ["Müteaddî fiil nedir? Fiilin üzerine vâki olduğu şey olmadan anlaşılmayan fiil: darabe Zeydün Amren'de Amr gerekir.",
         "Kaç türdür? Üç: bir mef'ûle, iki mef'ûle, üç mef'ûle (a'leme, erâ).",
         "Tek mef'ûl hazfedilir mi? Evet — karîneyle de karînesiz de (darabe Zeydün).",
         "İki mef'ûllü fiilin üç kısmı nedir? İkinci mef'ûlü birincisinden AYRI bir şey olan (a'taytü Zeyden dirhemen); iki mef'ûlü aslında mübtedâ ve haber olan KALP FİİLLERİ (alimtü Zeyden kâimen); yalnız mübtedâ ve habere girmekte onlara İLHAK edilenler (sayyera, ceale, terake, ittehaze).",
         "Kalp fiilleri hangileridir? Alime, raâ, vecede, zeame, zanne, hâle, hasibe ve câmid heb («farz et!»).",
         "Kalp fiilinin mef'ûlleri hazfedilir mi? Karînesiz asla; karîneyle ikisi birlikte çok, yalnız biri az — çünkü ikisi bir cümledir, yarım cümle bir şey söylemez.",
         "İlgâ nedir? Fiil iki mef'ûlünün ARASINDA yahut SONRASINDA durursa amelden düşürülebilir, ikisi mübtedâ ve haber olarak merfû kalır: Zeydün alimtü muntalikun — yahut amel eder: Zeyden alimtü muntalikan.",
         "Ta'lîk nedir? Fiille iki mef'ûlü arasına soru kelimesi, nefiy, ibtidâ lâmı, kasem yahut haberinde lâm bulunan inne girdiğinde amelin vücûben LAFZEN iptal edilip MÂNÂCA kalması: alimtü e-Zeydün indeke em Amrun, raeytü mâ Zeydün muntalikun, vecedtü le-Zeydün muntalikun, alimtü inne Zeyden le-kâimun — cümle iki mef'ûlün yerindedir.",
         "Kalp fiillerine has olan nedir? Fâil ve mef'ûlleri AYNI kişinin iki muttasıl zamiri olabilir (alimtünî kâimen — cehile, adime, fekade de böyledir); ve iki mef'ûlüne enne dâhil olabilir (alimtü enne Zeyden kâimun).",
         "Ta'lîk nereye kadar uzanır? Her kalp fiiline (şekektü, tebeyyentü, nesîtü), kendisiyle bilgi istenen her fiile (imtehantü, seeltü) ve beş duyunun fiillerine (lemestü, ebsartü, semi'tü, şememtü, zuktü)."]
 },
 "plain": {"en": "A transitive verb needs the thing it acts on. Some take one object, some two — and among the two-object verbs are the verbs of the heart, which swallow a whole sentence (Zayd is standing → I knew Zayd standing); a question word, a negation or an oath in the way stops them governing while they keep their sense.",
           "tr": "Geçişli fiil, etkilediği şeye muhtaçtır. Kimi bir, kimi iki mef'ûl alır — iki mef'ûllülerden kalp fiilleri bütün bir cümleyi yutar (Zeyd ayakta → Zeyd'i ayakta bildim); araya giren soru, nefiy yahut yemin, mânâları durduğu hâlde amellerini durdurur."},
 "explanation": {"en": "The mutaʿaddī is that whose understanding is not complete without the thing the act fell upon. It is of three kinds. The first is transitive to one object (ضَرَبَ زَيْدٌ عَمْرًا), and its object may be dropped with a clue and without one. The second is transitive to two objects, in three divisions: (1) the verb whose second object is a different thing from the first (أَعْطَيْتُ زَيْدًا دِرْهَمًا) — both or one may be dropped, with a clue and without; (2) the verbs of the heart — verbs signifying an act of the heart, entering on the mubtadaʾ and the khabar and putting both in naṣb as objects: عَلِمْتُ، رَأَيْتُ، وَجَدْتُ، زَعَمْتُ، ظَنَنْتُ، خِلْتُ، حَسِبْتُ, and هَبْ in the sense of أَحْسِبُ, not conjugable. Their two objects may not be dropped, both or one, without a clue; with a clue both are dropped often and one alone rarely. Among their properties: ilghāʾ and iʿmāl are both allowed when the verb stands between its two governed words (زَيْدٌ عَلِمْتُ مُنْطَلِقٌ) or after them (زَيْدٌ مُنْطَلِقٌ عَلِمْتُ); their doer and object may be two attached pronouns of one meaning (عَلِمْتُنِي قَائِمًا — and جَهِلَ، عَدِمَ، فَقَدَ share this permission); أَنَّ may enter on their two objects (عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ). The taʿlīq — by a word of question, by a negation, by the lām of ibtidāʾ, by an oath, or by إِنَّ with the kasra when the lām of ibtidāʾ enters its khabar — is the annulment of the work of necessity in wording, not in meaning, and it is general over these verbs (عَلِمْتُ أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو، رَأَيْتُ مَا زَيْدٌ مُنْطَلِقٌ، وَجَدْتُ لَزَيْدٌ مُنْطَلِقٌ، عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ), over every other verb of the heart (شَكَكْتُ، تَبَيَّنْتُ، نَسِيتُ), over every verb by which knowledge is sought (امْتَحَنْتُ، سَأَلْتُ), and over the verbs of the five senses (لَمَسْتُ، أَبْصَرْتُ، سَمِعْتُ، شَمَمْتُ، ذُقْتُ). (3) The verbs attached to the verbs of the heart merely in entering on the mubtadaʾ and the khabar and in the bar on dropping their objects without a clue: صَيَّرَ، جَعَلَ، تَرَكَ، اتَّخَذَ. The third kind — to three objects — follows.",
                 "tr": "Müteaddî, fiilin üzerine vâki olduğu şey olmadan anlaşılması tamam olmayandır. Üç türdür. Birincisi bir mef'ûle müteaddîdir (darabe Zeydün Amren); mef'ûlü karîneyle de karînesiz de hazfedilebilir. İkincisi iki mef'ûle müteaddîdir, üç kısımdır: (1) ikinci mef'ûlü birincisinden ayrı olan fiil (a'taytü Zeyden dirhemen) — ikisi de biri de karîneyle ve karînesiz hazfedilebilir; (2) kalp fiilleri — kalbî bir fiile delâlet eden, mübtedâ ve habere girip ikisini mef'ûl olarak nasb eden fiiller: alimtü, raeytü, vecedtü, zeamtü, zanentü, hıltü, hasibtü ve ahsibü mânâsındaki mutasarrıf olmayan heb. İki mef'ûlleri karînesiz ne birlikte ne tek tek hazfedilir; karîneyle ikisi birlikte çok, yalnız biri az hazfedilir. Hususiyetlerinden: fiil iki ma'mûlünün arasına girdiğinde (Zeydün alimtü muntalikun) yahut sonrasına kaldığında (Zeydün muntalikun alimtü) ilgâ ve i'mâl câizdir; fâil ve mef'ûlleri aynı mânâda iki muttasıl zamir olabilir (alimtünî kâimen — cehile, adime, fekade de bu cevazdadır); iki mef'ûlüne enne girebilir (alimtü enne Zeyden kâimun). Ta'lîk — soru kelimesiyle, nefiyle, ibtidâ lâmıyla, kasemle yahut haberine ibtidâ lâmı giren meksûr inne ile — amelin vücûben lafzen, mânâca değil, iptalidir; bu fiillerin hepsini (alimtü e-Zeydün indeke em Amrun, raeytü mâ Zeydün muntalikun, vecedtü le-Zeydün muntalikun, alimtü inne Zeyden le-kâimun), bunların dışındaki her kalp fiilini (şekektü, tebeyyentü, nesîtü), kendisiyle bilgi istenen her fiili (imtehantü, seeltü) ve beş duyunun fiillerini (lemestü, ebsartü, semi'tü, şememtü, zuktü) kapsar. (3) Yalnız mübtedâ ve habere girmekte ve mef'ûllerinin karînesiz hazfedilememesinde kalp fiillerine ilhak edilen fiiller: sayyera, ceale, terake, ittehaze. Üçüncü tür — üç mef'ûle — bundan sonra gelir."},
 "examples": [
  {"ar": "ضَرَبَ زَيْدٌ عَمْرًا", "en": "transitive to one object", "tr": "bir mef'ûle müteaddî", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "أَعْطَيْتُ زَيْدًا دِرْهَمًا", "en": "two objects, the second a different thing from the first", "tr": "iki mef'ûl, ikincisi birincisinden ayrı", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "زَيْدٌ عَلِمْتُ مُنْطَلِقٌ", "en": "ilghāʾ: the verb between its two governed words, stripped of its work", "tr": "ilgâ: fiil iki ma'mûlü arasında, amelden düşmüş", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
  {"ar": "عَلِمْتُنِي قَائِمًا", "en": "the doer and the object two pronouns of one person", "tr": "fâil ve mef'ûl aynı kişinin iki zamiri", "sourceStory": "izhar-al-asrar", "sentence": "s6"},
  {"ar": "عَلِمْتُ أَزَيْدٌ عِنْدَكَ أَمْ عَمْرٌو", "en": "the taʿlīq by the question word: rafʿ in wording, the clause in the place of the two objects", "tr": "soru kelimesiyle ta'lîk: lafzen ref, cümle iki mef'ûlün yerinde", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ", "en": "the taʿlīq by إِنَّ, kasra'd for the lām in its khabar", "tr": "haberindeki lâm için meksûr inne ile ta'lîk", "sourceStory": "izhar-al-asrar", "sentence": "s8"},
  {"ar": "صَيَّرَ وَجَعَلَ وَتَرَكَ وَاتَّخَذَ", "en": "the verbs attached to the verbs of the heart", "tr": "kalp fiillerine ilhak edilen fiiller", "sourceStory": "izhar-al-asrar", "sentence": "s10"},
 ],
 "commonMistakes": [
  {"wrong": "عَلِمْتُ زَيْدًا", "right": "عَلِمْتُ زَيْدًا قَائِمًا", "why": {"en": "a verb of the heart may not drop one of its two objects without a clue — the two were a sentence", "tr": "kalp fiili karînesiz iki mef'ûlünden birini hazfedemez — ikisi bir cümleydi"}},
  {"wrong": "عَلِمْتُ إِنَّ زَيْدًا قَائِمٌ", "right": "عَلِمْتُ أَنَّ زَيْدًا قَائِمٌ", "why": {"en": "after a verb of the heart the hamza takes a fatḥa — the clause is a maṣdar standing for the two objects; the kasra returns only when the lām of ibtidāʾ enters the khabar (عَلِمْتُ إِنَّ زَيْدًا لَقَائِمٌ)", "tr": "kalp fiilinden sonra hemze fetha alır — cümle iki mef'ûlün yerinde bir masdardır; kesre ancak habere ibtidâ lâmı girince döner (alimtü inne Zeyden le-kâimun)"}},
  {"wrong": "عَلِمْتُ مَا زَيْدًا مُنْطَلِقًا", "right": "عَلِمْتُ مَا زَيْدٌ مُنْطَلِقٌ", "why": {"en": "the negation suspends the verb's work in wording: the two words after it keep their rafʿ", "tr": "nefiy fiilin amelini lafzen askıya alır: ondan sonraki iki kelime ref'te kalır"}},
  {"wrong": "ضَرَبْتُنِي", "right": "عَلِمْتُنِي قَائِمًا", "why": {"en": "only the verbs of the heart (and جَهِلَ، عَدِمَ، فَقَدَ) let the doer and the object be two attached pronouns of one person; elsewhere say ضَرَبْتُ نَفْسِي", "tr": "yalnız kalp fiilleri (ve cehile, adime, fekade) fâil ile mef'ûlün aynı kişinin iki muttasıl zamiri olmasına izin verir; başka yerde darabtü nefsî denir"}},
 ],
}
ADD_EN = (" Chapter 9 (print pp. 102-104): the mutaʿaddī defined and its first kind, to one object (s1); the second kind, to two objects, in three "
          "divisions — the second object a different thing (s2), the verbs of the heart (s3) with their bar on dropping (s4), ilghāʾ and iʿmāl (s5), the "
          "two pronouns of one person and أَنَّ on the two objects (s6), the taʿlīq defined (s7), its four examples (s8) and its reach over every verb of "
          "the heart, of seeking knowledge and of the senses (s9), and the verbs attached to them (s10). Two readings of the lithograph are declared: "
          "«عديم» is read as the verb وَعَدِمَ, and «على حد» as the received عَلَى حَدِّهَا (s6).")
ADD_TR = (" Dokuzuncu bab (baskı s. 102-104): müteaddînin tarifi ve bir mef'ûle olan birinci türü (s1); iki mef'ûle olan ikinci tür, üç kısımda — ikinci "
          "mef'ûlü ayrı olan (s2), kalp fiilleri (s3) ve hazif yasağı (s4), ilgâ ve i'mâl (s5), aynı kişinin iki zamiri ve iki mef'ûle enne (s6), ta'lîkin "
          "tarifi (s7), dört örneği (s8) ve her kalp fiilini, bilgi isteyen fiilleri ve duyu fiillerini kapsaması (s9), onlara ilhak edilen fiiller (s10). "
          "Taşbaskının iki okunuşu bildirilmiştir: «عديم» vâv ile وَعَدِمَ fiili, «على حد» ise rivâyet edilen عَلَى حَدِّهَا olarak okundu (s6).")
write_out(9, S, TITLE, ADD_EN, ADD_TR, "pp. 102-104", GLOSS_ADD, notes=(NOTE,),
          related=((ZQ, [K]), (MFN, [K]), (HM, [K]), (TSY, [K]), (K8, [K]), ("mawadi-kasr-inna", [K]), ("mawadi-fath-anna", [K]), ("al-istifham", [K])))
report(9, S, GLOSS_ADD, (NOTE,))
