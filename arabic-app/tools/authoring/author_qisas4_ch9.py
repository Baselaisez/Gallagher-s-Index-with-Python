# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 9: «قِصَّةُ الْهُدْهُدِ» — §7 (the hoopoe's report of Sabaʾ) and §8 (Sulaymān calls the
queen of Sabaʾ to his religion); print pp. 16–17.
python3 tools/authoring/author_qisas4_ch9.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ الْهُدْهُدِ", "en": "The story of the hoopoe", "tr": "Hüdhüd'ün kıssası"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"
def majrur(full, lex, en, tr, punct=None, tags=(), ar="مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [HJ] + list(tags), ar, en, tr, punct=punct)
def mudaf_ilayh(full, lex, en, tr, punct=None, tags=(), ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ."): return tok(full, lex, "noun", [ID] + list(tags), ar, en, tr, punct=punct)
def naat(full, lex, en, tr, punct=None, tags=(), case="jarr", wa=False):
    C = {"jarr": "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    if wa: return tok(full, lex, "noun", [AT, NA] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C[:-1] + " — مَعْطُوفٌ عَلَى النَّعْتِ قَبْلَهُ.", "«and» + " + en + " — a second naʿt, joined.", "«ve» + " + tr + " — ikinci sıfat, ma'tûf.", punct=punct, segments=wa_(full[2:], lex, "noun"))
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — the naʿt.", tr + " — sıfat.", punct=punct)
def prep_pron(full, lex, pron_form, pron_lex, en, tr, punct=None, tags=(), extra_ar=""):
    pre = full[:len(full) - len(pron_form)]
    return tok(full, lex, "prep", [HJ] + list(tags), "حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra_ar + ".", en, tr, punct=punct, segments=[seg(pre, lex, "prep"), seg(pron_form, pron_lex, "pron")])
def maful_(full, lex, en, tr, punct=None, tags=(), ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [MB] + list(tags), ar, en, tr, punct=punct)
def noun_pron(full, lex, stem, pron_form, pron_lex, ar, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", list(tags), ar, en, tr, punct=punct, segments=[seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])
def atf(full, lex, en, tr, case="jarr", punct=None, tags=(), pos="noun", sign=None):
    C = {"jarr": "مَعْطُوفٌ مَجْرُورٌ " + (sign or "بِالْكَسْرَةِ"), "raf": "مَعْطُوفٌ مَرْفُوعٌ " + (sign or "بِالضَّمَّةِ"), "nasb": "مَعْطُوفٌ مَنْصُوبٌ " + (sign or "بِالْفَتْحَةِ")}[case]
    return tok(full, lex, pos, [AT] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " " + C + ".", "«and» + " + en + " — joined by the wāw.", "«ve» + " + tr + " — vâv ile atıf.", punct=punct, segments=wa_(full[2:], lex, pos))
def prep(full, lex, en, tr, punct=None, ar="حَرْفُ جَرٍّ."): return tok(full, lex, "prep", [HJ], ar, en, tr, punct=punct)
def li_pron(full, pron_form, pron_lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, "li", "prep", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ" + extra + ".", en, tr, punct=punct, segments=[seg(full[:2], "li", "prep"), seg(pron_form, pron_lex, "pron")])
def fa_mazi(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra_ar=""):
    return tok(full, lex, "verb", [AT] + list(tags), "الْفَاءُ عَاطِفَةٌ (لِلتَّعْقِيبِ)، وَ" + full[2:] + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}" if hidden else "") + extra_ar + ".", "«so» + " + en + " — a māḍī after the fāʾ of sequence.", "«de/da» + " + tr + " — ta'kîb fâ'sından sonra mâzî.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])
def khabar_kana(full, lex, en, tr, punct=None, tags=(), ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [KN] + list(tags), ar, en + " — kāna's khabar.", tr + " — kâne'nin haberi.", punct=punct)
def masdar_jarr(full, lex, en, tr, punct=None, wa=False, tags=()):
    if wa: return atf(full, lex, en, tr, "jarr", punct=punct, tags=["masdar"] + list(tags))
    return majrur(full, lex, en, tr, punct=punct, tags=["masdar"] + list(tags))

# ---------------------------------------------------------------- §7 قِصَّةُ هُدْهُدَ (print p. 16)
sen("s1", "The hoopoe was his scout and his eye, guiding him to the places of water and the camping-grounds of the army;",
        "Hüdhüd onun öncüsü ve gözüydü; ona su yerlerini ve ordunun konak yerlerini gösterirdi;", [
  kana(),
  tok("الْهُدْهُدُ", "hudhud", "noun", [KN], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the hoopoe» — kāna's ism.", "«Hüdhüd» — kâne'nin ismi."),
  noun_pron("رَائِدَهُ", "raid", "رَائِدَ", "هُ", "pron-3ms", "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his scout» — kāna's khabar.", "«onun öncüsü» — kâne'nin haberi.", tags=[KN, ID, "ism-fail"]),
  noun_pron("وَعَيْنَهُ", "ayn", "وَعَيْنَ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَعَيْنَ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his eye»", "«ve gözü»", tags=[AT, ID]),
  tok("يَدُلُّهُ", "dalla", "verb", [HL, "mudari-marfu", MB, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ حَالٌ (أَوْ خَبَرٌ ثَانٍ).", "«guiding him» — the hāʾ is the object; the clause is a ḥāl.", "«ona gösterir» — hâ mef'ûl; cümle hâl.", segments=[seg("يَدُلُّ", "dalla", "verb"), pr3ms()]),
  prep("عَلَى", "ala", "«to»", "«-i»"),
  majrur("مَوَاضِعِ", "mawdi", "«the places»", "«yerlerini»", tags=[ID, JT], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  mudaf_ilayh("الْمِيَاهِ", "ma-water", "«of water»", "«su»", tags=[JT], punct="،"),
  atf("وَمَنَازِلِ", "manzil", "«the camping-grounds»", "«konak yerlerini»", "jarr", tags=[ID, JT]),
  mudaf_ilayh("الْجَيْشِ", "jaysh", "«of the army»", "«ordunun»", punct="،"),
])
sen("s2", "but he did not find it, so he was displeased and threatened it; then it was absent a little while and came,",
        "fakat onu bulamadı; buna kızdı ve onu tehdit etti; o kısa bir süre kayboldu, sonra geldi,", [
  tok("فَلَمْ", "lam-jazima", "part", [AT, LJ], "الْفَاءُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«but … not» — lam.", "«fakat … -medi» — lem.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("يَجِدْهُ", "wajada", "verb", [LJ, MB, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ — مِثَالٌ سَقَطَتْ وَاوُهُ.", "«find it» — jazm by lam; an assimilated verb whose wāw drops.", "«onu bulamadı» — lem ile meczum; vâvı düşen misâl fiil.", punct="،", segments=[seg("يَجِدْ", "wajada", "verb"), pr3ms()]),
  fa_mazi("فَأَنْكَرَ", "ankara", "«he was displeased at»", "«buna kızdı»", tags=["form-iv-verbs", MB]),
  tok("ذٰلِكَ", "dhalika", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«bunu» — mef'ûl."),
  tok("وَتَوَعَّدَهُ", "tawaada", "verb", [AT, MB, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَوَعَّدَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and threatened it»", "«ve onu tehdit etti»", punct="،", segments=[seg("وَ", "wa", "conj"), seg("تَوَعَّدَ", "tawaada", "verb"), pr3ms()]),
  fa_mazi("فَغَابَ", "ghaba", "«it was absent»", "«kayboldu»", tags=["hollow-verbs"]),
  tok("زَمَانًا", "zaman", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a while» — a ẓarf of time.", "«bir süre» — zaman zarfı."),
  naat("يَسِيرًا", "yasir", "«little»", "«kısa»", case="nasb", tags=["sifa-mushabbaha"]),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then» — the joining particle of delay.", "«sonra» — terâhî bildiren atıf harfi."),
  mazi("جَاءَ", "jaa", "«came»", "«geldi»", tags=["hollow-verbs"], hidden="هُوَ", punct="،"),
])
sen("s3", "and said to Sulaymān: I have learned what you have not learned, neither you nor your hosts; and I have come to you with sure tidings of Sabaʾ and their queen:",
        "ve Süleyman'a dedi ki: Senin de ordularının da bilmediği bir şeyi öğrendim; sana Sebe' ve kraliçeleri hakkında doğru bir haber getirdim:", [
  qala(full="فَقَالَ", wa=False, hidden="هُوَ", punct=None, tags=[AT]),
  tok("لِسُلَيْمَانَ", "sulayman", "propn", [HJ, MM], "اللَّامُ حَرْفُ جَرٍّ، وَسُلَيْمَانَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to Sulaymān» — jarr by fatḥa (a diptote).", "«Süleyman'a» — gayr-i munsarıf, fetha ile mecrûr.", punct=":", segments=[seg("لِ", "li", "prep"), seg("سُلَيْمَانَ", "sulayman", "propn")]),
  tok("اطَّلَعْتُ", "ittalaa", "verb", ["form-viii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ.", "«I have learned» — the tāʾ is the doer.", "«öğrendim» — tâ fâil.", segments=[seg("اطَّلَعْ", "ittalaa", "verb"), seg("تُ", "pron-1s", "pron")]),
  prep("عَلَى", "ala", "«of»", "«-i»"),
  tok("مَا", "ma-mawsula", "pron", [HJ, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«what» — the relative, in jarr.", "«… -diği şeyi» — ism-i mevsûl, mecrûr."),
  tok("لَمْ", "lam-jazima", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — lam.", "«-medi» — lem."),
  tok("تَطَّلِعْ", "ittalaa", "verb", [LJ, MW, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ — صِلَةٌ.", "«you have learned» — jazm by lam; the ṣila.", "«öğrenmedin» — lem ile meczum; sıla."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«it»", "«onu»"),
  tok("أَنْتَ", "anta", "pron", ["tawkid"], "ضَمِيرٌ مُنْفَصِلٌ تَوْكِيدٌ لِلضَّمِيرِ الْمُسْتَتِرِ.", "«you» — a detached pronoun confirming the concealed one.", "«sen» — gizli zamiri pekiştiren munfasıl zamir."),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor» — the wāw with a lā strengthening the negation.", "«ne de» — vâv ve nefyi pekiştiren lâ.", segments=wa_("لَا", "la-nafiya", "part")),
  noun_pron("جُنُودُكَ", "jund", "جُنُودُ", "كَ", "pron-2ms", "مَعْطُوفٌ عَلَى الضَّمِيرِ مَرْفُوعٌ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your hosts» — joined to the pronoun.", "«orduların» — zamire ma'tûf.", punct="،", tags=[AT, ID, JT]),
  tok("وَجِئْتُكَ", "jaa", "verb", [AT, MB, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَجِئْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.", "«and I have come to you» — the tāʾ the doer, the kāf the object.", "«ve sana geldim» — tâ fâil, kâf mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("كَ", "pron-2ms", "pron")]),
  tok("بِخَبَرٍ", "khabar", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَخَبَرٍ مَجْرُورٌ.", "«with tidings»", "«bir haberle»", segments=[seg("بِ", "bi", "prep"), seg("خَبَرٍ", "khabar", "noun")]),
  naat("صِدْقٍ", "sidq", "«sure» (lit. of truth)", "«doğru»", tags=["masdar"]),
  prep("عَنْ", "an", "«of»", "«hakkında»"),
  majrur("سَبَإٍ", "saba", "«Sabaʾ»", "«Sebe'»"),
  noun_pron("وَمَلِكَتِهِمْ", "malika", "وَمَلِكَتِ", "هِمْ", "pron-3mp", "الْوَاوُ عَاطِفَةٌ، وَمَلِكَتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«and their queen»", "«ve kraliçeleri»", punct="،", tags=[AT, ID]),
])
sen("s4", "they have a great kingdom and a wide realm, and I found them — with all this intelligence, shrewdness, dominion and leadership — people of folly and ignorance:",
        "büyük bir mülkleri ve geniş bir devletleri var; onları — bu akla, zekâya, mülke ve riyasete rağmen — sefahet ve cehalet ehli buldum:", [
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«they have» — a fronted khabar.", "«onların … var» — öne alınmış haber.", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ"),
  tok("مُلْكٌ", "mulk", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«a kingdom» — the delayed mubtadaʾ.", "«bir mülk» — sonraya bırakılmış mübtedâ."),
  naat("عَظِيمٌ", "azim", "«great»", "«büyük»", case="raf", tags=["sifa-mushabbaha"]),
  atf("وَدَوْلَةٌ", "dawla", "«a realm»", "«bir devlet»", "raf"),
  naat("وَاسِعَةٌ", "wasi-wide", "«wide»", "«geniş»", case="raf", tags=["ism-fail"], punct="،"),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed»", "«ve gerçekten»", segments=wa_("قَدْ", "qad", "part")),
  tok("وَجَدْتُهُمْ", "wajada", "verb", [MX, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ أَوَّلُ.", "«I found them» — the tāʾ the doer; hum the first object.", "«onları buldum» — tâ fâil; hüm ilk mef'ûl.", segments=[seg("وَجَدْ", "wajada", "verb"), seg("تُ", "pron-1s", "pron"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("عَلَى", "ala", "«with» (lit. upon)", "«… rağmen»", ar="حَرْفُ جَرٍّ — جُمْلَةٌ مُعْتَرِضَةٌ بَيْنَ الْمَفْعُولَيْنِ."),
  tok("هٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ بِعَلَى.", "«this»", "«bu»"),
  tok("الْعَقْلِ", "aql", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«intelligence» — the badal.", "«akıl» — bedel."),
  atf("وَالْكِيَاسَةِ", "kiyasa", "«shrewdness»", "«zekâ»", "jarr"),
  atf("وَالْمُلْكِ", "mulk", "«dominion»", "«mülk»", "jarr"),
  atf("وَالرِّئَاسَةِ", "riasa", "«leadership»", "«riyaset»", "jarr"),
  tok("أَصْحَابَ", "sahib", "noun", [MB, MX, ID, JT], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«people [of]» — the second object, annexed.", "«ehli» — ikinci mef'ûl, muzâf."),
  mudaf_ilayh("سَفَاهَةٍ", "sifaha", "«folly»", "«sefahet»", tags=["masdar"]),
  atf("وَجَهَالَةٍ", "jahala", "«ignorance»", "«cehalet»", "jarr", tags=["masdar"], punct="،"),
])
sen("s5", "they prostrate to the sun instead of God, they do not guard against that, and they are not guided to the worship of God alone.",
        "Allah'ı bırakıp güneşe secde ediyorlar, bundan sakınmıyorlar ve yalnız Allah'a kulluğa yol bulamıyorlar.", [
  tok("وَهُمْ", "hum", "pron", [MK, HL], "الْوَاوُ لِلْحَالِ (أَوْ لِلِاسْتِئْنَافِ)، وَهُمْ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and they» — the mubtadaʾ.", "«ve onlar» — mübtedâ.", segments=wa_("هُمْ", "hum", "pron")),
  khamsa("يَسْجُدُونَ", "sajada", "«prostrate»", "«secde ediyorlar»", tags=[MK], extra_ar=" — وَالْجُمْلَةُ خَبَرٌ"),
  tok("لِلشَّمْسِ", "shams", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالشَّمْسِ مَجْرُورٌ.", "«to the sun»", "«güneşe»", segments=[seg("لِ", "li", "prep"), seg("الشَّمْسِ", "shams", "noun")]),
  prep("مِنْ", "min", "«instead» (lit. from)", "«… bırakıp»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«besides»", "«başka»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»", punct="،"),
  la_nafiya(wa=True),
  khamsa("يَتَّقُونَ", "ittaqa", "«guard against»", "«sakınıyorlar»", tags=[AT, MB, "form-viii-verbs", "naqis-verbs"]),
  tok("ذٰلِكَ", "dhalika", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«bundan» — mef'ûl.", punct="،"),
  la_nafiya(wa=True),
  khamsa("يَهْتَدُونَ", "ihtada", "«are guided»", "«yol buluyorlar»", tags=[AT, "form-viii-verbs", "naqis-verbs"]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("عِبَادَةِ", "ibada", "«the worship»", "«kulluğa»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِإِلَى، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'a»"),
  noun_pron("وَحْدَهُ", "wahda", "وَحْدَ", "هُ", "pron-3ms", "حَالٌ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ (أَيْ: مُنْفَرِدًا).", "«alone» — a ḥāl, annexed.", "«yalnız» — hâl, muzâf.", punct=".", tags=[HL, ID]),
])

# ---------------------------------------------------------------- §8 سُلَيْمَانُ يَدْعُو مَلِكَةَ سَبَإٍ إِلَى دِينِهِ (print p. 17)
sen("s6", "It weighed on the prophet of God that beside his kingdom there should be a realm and a nation he did not know, which his call had not reached and which still worshipped the sun;",
        "Allah'ın peygamberine, mülkünün yanı başında tanımadığı, davetinin ulaşmadığı ve hâlâ güneşe tapan bir mülk ve ümmetin bulunması ağır geldi;", [
  mazi("وَشَقَّ", "shaqqa", "«and it weighed»", "«ve ağır geldi»", tags=["doubled-verbs"], wa=True, hidden=None),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("نَبِيِّ", "nabi", "«the prophet»", "«peygamberine»", tags=[ID], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ فَاعِلُ شَقَّ.", "«that» — the an of naṣb; the clause is the doer of «weighed».", "«… -ması» — nasb eden en; cümle «ağır geldi»nin fâili."),
  tok("يَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«there should be» — kāna in naṣb after an.", "«bulunması» — en ile mansub kâne."),
  tok("بِجِوَارِ", "jiwar", "noun", [HJ, ID, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَجِوَارِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونَ مُقَدَّمٌ.", "«beside» — the jarr phrase is kāna's fronted khabar.", "«yanı başında» — câr-mecrûr, kâne'nin öne alınmış haberi.", segments=[seg("بِ", "bi", "prep"), seg("جِوَارِ", "jiwar", "noun")]),
  noun_pron("مَمْلَكَتِهِ", "mamlaka", "مَمْلَكَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his kingdom»", "«mülkünün»", tags=[ID]),
  tok("مُلْكٌ", "mulk", "noun", [KN], "اسْمُ يَكُونَ مُؤَخَّرٌ مَرْفُوعٌ.", "«a realm» — kāna's delayed ism.", "«bir mülk» — kâne'nin ismi."),
  atf("وَأُمَّةٌ", "umma", "«a nation»", "«bir ümmet»", "raf"),
  la_nafiya(),
  tok("يَعْرِفُهَا", "arafa", "verb", ["jumla-sifa", "la-nafiya", "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ.", "«he did not know» — the clause is a naʿt.", "«tanımadığı» — cümle sıfat.", segments=[seg("يَعْرِفُ", "arafa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … -medi»", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("تَبْلُغْهَا", "balagha", "verb", [LJ, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَهَا مَفْعُولٌ بِهِ.", "«reached it» — jazm by lam; hā the object.", "«ona ulaşmadı» — lem ile meczum; hâ mef'ûl.", segments=[seg("تَبْلُغْ", "balagha", "verb"), seg("هَا", "pron-3fs", "pron")]),
  noun_pron("دَعْوَتُهُ", "dawa", "دَعْوَتُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his call» — the doer.", "«daveti» — fâil.", punct="،", tags=[FL, ID]),
  la_nafiya(wa=True),
  tok("تَزَالُ", "zala", "verb", [AT, KN, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«still» — lā tazālu, a sister of kāna; its ism concealed.", "«hâlâ» — lâ tezâlu, kâne'nin kardeşi; ismi gizli."),
  mudari("تَعْبُدُ", "abada", "«worshipped»", "«tapıyor»", tags=[KN, MB], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ تَزَالُ"),
  maful_("الشَّمْسَ", "shams", "«the sun»", "«güneşe»", punct="،"),
])
sen("s7", "the religious, prophetic zeal rose in him, and he saw it right to write to their queen and pagan ruler, calling her to Islam, to obedience and submission,",
        "içinde dinî, nebevî hamiyet kabardı; kraliçelerine, müşrik hükümdarlarına yazmayı ve onu İslâm'a, itaate ve teslimiyete çağırmayı doğru buldu;", [
  mazi_ta("وَثَارَتْ", "thara", "«and rose»", "«ve kabardı»", tags=[AT, "hollow-verbs"], wa=True),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in him»", "«içinde»"),
  fail("الْحَمِيَّةُ", "hamiyya", "«the zeal»", "«hamiyet»"),
  naat("الدِّينِيَّةُ", "dini", "«religious»", "«dinî»", case="raf", tags=["ism-mansub"]),
  naat("النَّبَوِيَّةُ", "nabawi", "«prophetic»", "«nebevî»", case="raf", tags=["ism-mansub"], punct="،"),
  mazi("وَرَأَى", "raa", "«and he saw»", "«ve gördü»", tags=[AT, "naqis-verbs"], wa=True, hidden="هُوَ"),
  prep("مِنَ", "min", "«[it] as» (lit. of)", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الصَّوَابِ", "sawab", "«right»", "«doğru»"),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ رَأَى.", "«to» — the an of naṣb; the clause is the object of «saw».", "«… -mayı» — nasb eden en; cümle «gördü»nün mef'ûlü."),
  tok("يَكْتُبَ", "kataba", "verb", [AN], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«write» — naṣb by an.", "«yazmayı» — en ile mansub."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  noun_pron("مَلِكَتِهَا", "malika", "مَلِكَتِ", "هَا", "pron-3fs", "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their queen»", "«kraliçelerine»", tags=[HJ, ID]),
  noun_pron("وَحَاكِمَتِهَا", "hakima", "وَحَاكِمَتِ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَحَاكِمَتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their ruler»", "«ve hükümdarlarına»", tags=[AT, ID, "ism-fail"]),
  naat("الْمُشْرِكَةِ", "mushrik", "«pagan»", "«müşrik»", tags=["ism-fail", "form-iv-verbs"], punct="،"),
  tok("وَيَدْعُوَهَا", "daa", "verb", [AT, AN, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَدْعُوَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ (مَعْطُوفٌ عَلَى يَكْتُبَ)، وَهَا مَفْعُولٌ بِهِ.", "«and call her» — naṣb by a visible fatḥa on the wāw; joined to «write».", "«ve onu çağırmayı» — vâv üzerinde açık fetha ile mansub; «yazmayı»ya ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("يَدْعُوَ", "daa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("الْإِسْلَامِ", "islam", "«Islam»", "«İslâm'a»", tags=["masdar"], punct="،"),
  atf("وَالطَّاعَةِ", "taa", "«obedience»", "«itaate»", "jarr", tags=["masdar"]),
  atf("وَالِاسْتِسْلَامِ", "istislam", "«submission»", "«teslimiyete»", "jarr", tags=["masdar"], punct="،"),
])
sen("s8", "before he marched on her lands with his overwhelming hosts. So he wrote her an eloquent letter and in it called her to Islam and submission;",
        "kahredici ordularıyla ülkesine yürümeden önce. Böylece ona beliğ bir mektup yazdı ve onu İslâm'a ve teslimiyete çağırdı;", [
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ.", "«before» — a ẓarf annexed to the an-clause.", "«önce» — en cümlesine muzâf zarf."),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that»", "«… -meden»"),
  tok("يَزْحَفَ", "zahafa", "verb", [AN], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«he marched» — naṣb by an.", "«yürümeden» — en ile mansub."),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  noun_pron("بِلَادِهَا", "bilad", "بِلَادِ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her lands»", "«ülkesine»", tags=[HJ, ID, JT]),
  noun_pron("بِجُنُودِهِ", "jund", "بِجُنُودِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَجُنُودِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with his hosts»", "«ordularıyla»", tags=[HJ, ID, JT]),
  naat("الْقَاهِرَةِ", "qahir", "«overwhelming»", "«kahredici»", tags=["ism-fail"], punct="،"),
  fa_mazi("فَكَتَبَ", "kataba", "«he wrote»", "«yazdı»", tags=[MB]),
  prep_pron("إِلَيْهَا", "ila", "هَا", "pron-3fs", "«to her»", "«ona»"),
  maful_("كِتَابًا", "kitab", "«a letter»", "«bir mektup»"),
  naat("بَلِيغًا", "baligh", "«eloquent»", "«beliğ»", case="nasb", tags=["sifa-mushabbaha"]),
  tok("وَدَعَاهَا", "daa", "verb", [AT, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهَا مَفْعُولٌ بِهِ.", "«and called her» — hā the object.", "«ve onu çağırdı» — hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("دَعَا", "daa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in it»", "«onda»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("الْإِسْلَامِ", "islam", "«Islam»", "«İslâm'a»", tags=["masdar"]),
  atf("وَالِاسْتِسْلَامِ", "istislam", "«submission»", "«teslimiyete»", "jarr", tags=["masdar"], punct="،"),
])
sen("s9", "and the letter joins gentleness and firmness, the humility of the prophets and the pride of kings.",
        "mektup, yumuşaklık ile sertliği, peygamberlerin tevazuu ile hükümdarların izzetini bir araya getirir.", [
  tok("وَالْكِتَابُ", "kitab", "noun", [MK, HL], "الْوَاوُ لِلْحَالِ، وَالْكِتَابُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the letter» — the mubtadaʾ of a ḥāl clause.", "«ve mektup» — hâl cümlesinin mübtedâsı.", segments=wa_("الْكِتَابُ", "kitab", "noun")),
  mudari("يَجْمَعُ", "jamaa-gather", "«joins»", "«bir araya getirir»", tags=[MK], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرٌ"),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasını»"),
  mudaf_ilayh("الرِّقَّةِ", "riqqa", "«gentleness»", "«yumuşaklık»"),
  atf("وَالصَّرَامَةِ", "sarama", "«firmness»", "«sertlik»", "jarr"),
  atf("وَتَوَاضُعِ", "tawadu", "«the humility»", "«tevazuu»", "jarr", tags=[ID, "masdar"]),
  mudaf_ilayh("الْأَنْبِيَاءِ", "nabi", "«of the prophets»", "«peygamberlerin»", tags=[JT]),
  atf("وَغَيْرَةِ", "ghayra", "«the pride»", "«izzetini»", "jarr", tags=[ID]),
  mudaf_ilayh("الْمُلُوكِ", "malik-king", "«of kings»", "«hükümdarların»", tags=[JT], punct="."),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: malik-king is the new key; tawaada = تَوَعَّدَ and zala = زَالَ (مَا زَالَ) are reused)
CAND = {
 "hudhud": G("hudhud", "هُدْهُد", "ه د ه د", "noun", "a hoopoe", "hüdhüd, ibibik", 2),
 "raid": G("raid", "رَائِد", "ر و د", "noun", "a scout, a pioneer (an active participle)", "öncü, keşifçi (ism-i fâil)", 3),
 "ayn": G("ayn", "عَيْن", "ع ي ن", "noun", "an eye; a spy; a spring", "göz; casus; pınar", 1),
 "dalla": G("dalla", "دَلَّ", "د ل ل", "verb", "to guide, to indicate (doubled)", "göstermek, delâlet etmek (muzâaf)", 1),
 "mawdi": G("mawdi", "مَوْضِع", "و ض ع", "noun", "a place", "yer, mevzi", 2, plural="مَوَاضِع"),
 "ma-water": G("ma-water", "مَاء", "م و ه", "noun", "water", "su", 1, plural="مِيَاه"),
 "manzil": G("manzil", "مَنْزِل", "ن ز ل", "noun", "a camping-ground, a lodging", "konak yeri, menzil", 2, plural="مَنَازِل"),
 "jaysh": G("jaysh", "جَيْش", "ج ي ش", "noun", "an army", "ordu", 1, plural="جُيُوش"),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find (an assimilated verb: يَجِدُ)", "bulmak (misâl fiil: yecidü)", 1),
 "ankara": G("ankara", "أَنْكَرَ", "ن ك ر", "verb", "to disapprove, to deny (Form IV)", "hoş görmemek, inkâr etmek (if'âl)", 2),
 "tawaada": G("tawaada", "تَوَعَّدَ", "و ع د", "verb", "to threaten (Form V)", "tehdit etmek (tefa''ul)", 3),
 "ghaba": G("ghaba", "غَابَ", "غ ي ب", "verb", "to be absent (hollow)", "kaybolmak, gâib olmak (ecvef)", 2),
 "zaman": G("zaman", "زَمَان", "ز م ن", "noun", "time, a while", "zaman", 1),
 "yasir": G("yasir", "يَسِير", "ي س ر", "noun", "little, slight, easy", "az, kısa, kolay", 2),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then — joining with delay", "sonra — terâhî ile atıf", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come (hollow)", "gelmek (ecvef)", 1),
 "ittalaa": G("ittalaa", "اِطَّلَعَ", "ط ل ع", "verb", "to learn of, to come to know (Form VIII, with ʿalā)", "öğrenmek, vâkıf olmak (iftiâl, alâ ile)", 3),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (masc. singular, detached)", "sen (munfasıl)", 1),
 "jund": G("jund", "جُنْد", "ج ن د", "noun", "a host, an army", "ordu", 2, plural="جُنُود"),
 "khabar": G("khabar", "خَبَر", "خ ب ر", "noun", "news, tidings", "haber", 1),
 "sidq": G("sidq", "صِدْق", "ص د ق", "noun", "truth, sincerity", "doğruluk, sıdk", 1),
 "saba": G("saba", "سَبَأ", "س ب أ", "propn", "Sabaʾ (Sheba) — the kingdom of the Yemen", "Sebe' — Yemen'deki krallık", 2),
 "malika": G("malika", "مَلِكَة", "م ل ك", "noun", "a queen", "kraliçe, melike", 1),
 "mulk": G("mulk", "مُلْك", "م ل ك", "noun", "kingship, a kingdom", "mülk", 2),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great", "büyük", 1),
 "dawla": G("dawla", "دَوْلَة", "د و ل", "noun", "a state, a realm", "devlet", 1),
 "wasi-wide": G("wasi-wide", "وَاسِع", "و س ع", "noun", "wide", "geniş", 1),
 "aql": G("aql", "عَقْل", "ع ق ل", "noun", "intelligence, reason", "akıl", 1),
 "kiyasa": G("kiyasa", "كِيَاسَة", "ك ي س", "noun", "shrewdness, cleverness", "zekâ, kiyaset", 3),
 "riasa": G("riasa", "رِئَاسَة", "ر أ س", "noun", "leadership, presidency", "riyaset, reislik", 3),
 "sahib": G("sahib", "صَاحِب", "ص ح ب", "noun", "an owner; a person of", "sahip; ehli", 1, plural="أَصْحَاب"),
 "sifaha": G("sifaha", "سَفَاهَة", "س ف ه", "noun", "folly, foolishness", "sefahet, akılsızlık", 3),
 "jahala": G("jahala", "جَهَالَة", "ج ه ل", "noun", "ignorance", "cehalet", 2),
 "hum": G("hum", "هُمْ", None, "pron", "they (masc. plural, detached)", "onlar (munfasıl)", 1),
 "sajada": G("sajada", "سَجَدَ", "س ج د", "verb", "to prostrate", "secde etmek", 1),
 "shams": G("shams", "شَمْس", "ش م س", "noun", "the sun", "güneş", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "besides, short of", "… -den başka", 2),
 "ittaqa": G("ittaqa", "اِتَّقَى", "و ق ي", "verb", "to guard against, to fear God (Form VIII)", "sakınmak, takvâ üzere olmak (iftiâl)", 2),
 "ihtada": G("ihtada", "اِهْتَدَى", "ه د ي", "verb", "to be guided, to find the way (Form VIII, defective)", "hidayet bulmak, yol bulmak (iftiâl, nâkıs)", 2),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet, kulluk", 1),
 "wahda": G("wahda", "وَحْد", "و ح د", "noun", "alone — وَحْدَهُ, a ḥāl", "yalnız — vahdehû, hâl", 1),
 "shaqqa": G("shaqqa", "شَقَّ", "ش ق ق", "verb", "to split; to weigh heavily on (with ʿalā) (doubled)", "yarmak; ağır gelmek (alâ ile) (muzâaf)", 2),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak, idi", 1),
 "jiwar": G("jiwar", "جِوَار", "ج و ر", "noun", "neighbourhood, vicinity", "civar, komşuluk", 2),
 "mamlaka": G("mamlaka", "مَمْلَكَة", "م ل ك", "noun", "a kingdom", "memleket", 2),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation", "ümmet", 1, plural="أُمَم"),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know", "bilmek", 1),
 "balagha": G("balagha", "بَلَغَ", "ب ل غ", "verb", "to reach", "ulaşmak", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "a call, a mission", "davet", 1),
 "zala": G("zala", "زَالَ (مَا زَالَ)", "ز ي ل", "verb", "to cease — negated: still, continuously (a sister of kāna)", "zâil olmak — olumsuzu: hâlâ, sürekli (kâne'nin kardeşi)", 2),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "tapmak, ibadet etmek", 1),
 "thara": G("thara", "ثَارَ", "ث و ر", "verb", "to rise, to flare up (hollow)", "kabarmak, ayaklanmak (ecvef)", 3),
 "hamiyya": G("hamiyya", "حَمِيَّة", "ح م ي", "noun", "zeal, fervour", "hamiyet, gayret", 3),
 "dini": G("dini", "دِينِيّ", "د ي ن", "noun", "religious (a nisba)", "dinî (nisbet)", 2),
 "nabawi": G("nabawi", "نَبَوِيّ", "ن ب أ", "noun", "prophetic (a nisba)", "nebevî (nisbet)", 2),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see; to deem", "görmek; saymak", 1),
 "sawab": G("sawab", "صَوَاب", "ص و ب", "noun", "what is right, correctness", "doğru, savap", 2),
 "kataba": G("kataba", "كَتَبَ", "ك ت ب", "verb", "to write", "yazmak", 1),
 "hakima": G("hakima", "حَاكِمَة", "ح ك م", "noun", "a female ruler", "kadın hükümdar", 2),
 "mushrik": G("mushrik", "مُشْرِك", "ش ر ك", "noun", "a polytheist, pagan (the active participle of Form IV)", "müşrik (if'âl ism-i fâili)", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call, to invite; to pray", "çağırmak, davet etmek; dua etmek", 1),
 "islam": G("islam", "إِسْلَام", "س ل م", "noun", "Islam, submission to God", "İslâm", 1),
 "taa": G("taa", "طَاعَة", "ط و ع", "noun", "obedience", "itaat", 1),
 "istislam": G("istislam", "اِسْتِسْلَام", "س ل م", "noun", "submission, surrender (maṣdar of Form X)", "teslimiyet, teslim olma (istif'âl masdarı)", 3),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before — a ẓarf of time", "önce — zaman zarfı", 1),
 "zahafa": G("zahafa", "زَحَفَ", "ز ح ف", "verb", "to march (on), to advance", "yürümek, ilerlemek (ordu)", 3),
 "bilad": G("bilad", "بِلَاد", "ب ل د", "noun", "lands, a country (the plural of بَلَد)", "ülke, beldeler (beled'in çoğulu)", 1),
 "qahir": G("qahir", "قَاهِر", "ق ه ر", "noun", "overwhelming, subduing (an active participle)", "kahredici, yenen (ism-i fâil)", 2),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a letter; a book", "mektup; kitap", 1),
 "baligh": G("baligh", "بَلِيغ", "ب ل غ", "noun", "eloquent", "beliğ", 2),
 "jamaa-gather": G("jamaa-gather", "جَمَعَ", "ج م ع", "verb", "to gather, to join", "bir araya getirmek", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "riqqa": G("riqqa", "رِقَّة", "ر ق ق", "noun", "gentleness, tenderness", "yumuşaklık, rikkat", 3),
 "sarama": G("sarama", "صَرَامَة", "ص ر م", "noun", "firmness, sternness", "sertlik, kararlılık", 3),
 "tawadu": G("tawadu", "تَوَاضُع", "و ض ع", "noun", "humility (maṣdar of Form VI)", "tevazu (tefâul masdarı)", 2),
 "ghayra": G("ghayra", "غَيْرَة", "غ ي ر", "noun", "pride, jealous honour", "izzet, gayret, kıskançlık", 3),
 "malik-king": G("malik-king", "مَلِك", "م ل ك", "noun", "a king", "hükümdar, melik", 1, plural="مُلُوك"),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o, şu", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masc. singular, attached)", "sen / senin (bitişik)", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "I / me / my (attached: the tāʾ of the doer, the yāʾ)", "ben / beni / benim (bitişik: fâil tâ'sı, yâ)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ittalaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِطَّلَع", "طَّلِع", "اِطَّلِع", "اِطِّلَاع", "مُطَّلِع", "مُطَّلَع", "اُطُّلِعَ", "يُطَّلَعُ", "اِطَّلَعَ عَلَى الشَّيْءِ: عَلِمَهُ وَوَقَفَ عَلَيْهِ — اِفْتَعَلَ مِنْ طَلَعَ، أُدْغِمَتْ تَاءُ الِافْتِعَالِ فِي الطَّاءِ."))
put_morph(mo, "ihtada", _sg.derived_naqis("مِنْ بَابِ الِافْتِعَالِ", "اِفْتَعَلَ يَفْتَعِلُ", "َ", "اِهْتَدَ", "هْتَد", "i", "اِهْتَد", "اِهْتِدَاء", "مُهْتَدٍ (الْمُهْتَدِي)", None, None, None, "اِهْتَدَى إِلَى الطَّرِيقِ: عَرَفَهُ وَسَلَكَهُ — نَاقِصٌ يَائِيٌّ؛ لَمْ يَهْتَدِ."))
put_morph(mo, "thara", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "ثَار", "ثُر", "ثُور", "ثُر", "ثُور", "ثُر", "ثَوْر / ثَوَرَان", "ثَائِر", None, None, None, "ثَارَ الشَّيْءُ: هَاجَ وَانْتَشَرَ؛ ثَارَتِ الْحَمِيَّةُ فِيهِ: هَاجَتْ."))
put_morph(mo, "zahafa", _sg.sound1("fataha", "زَحَف", "زْحَف", "اِزْحَف", "زَحْف", "زَاحِف", None, None, None, "زَحَفَ الْجَيْشُ إِلَى الْعَدُوِّ: مَشَى إِلَيْهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch9 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 9 (print pp. 16–17, §7–8): the hoopoe's absence and its report of Sabaʾ (s1–s5); Sulaymān's zeal and his letter to the queen (s6–s9)."
ADD_TR = " Dokuzuncu bölüm (baskı s. 16–17, 7–8. kısımlar): Hüdhüd'ün kayboluşu ve Sebe' haberi (s1–s5); Süleyman'ın hamiyeti ve kraliçeye mektubu (s6–s9)."
write_out(9, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §7–8", GLOSS_ADD, notes=(), related=())
report(9, S, GLOSS_ADD, ())
