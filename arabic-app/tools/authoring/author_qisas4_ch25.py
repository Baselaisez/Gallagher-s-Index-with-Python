# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 25: «قِصَّةُ عِيسَى» §4 (contempt and rebellion: what the Roman servitude bred; forgetting equality; believing only what suits their desire; the critic fought) and §5 (God's favour on the Children of Israel: tawḥīd, with 2:47); print pp. 42–43.
python3 tools/authoring/author_qisas4_ch25.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: اسْتِخْفَافٌ وَتَمَرُّدٌ، وَنِعْمَةُ اللهِ عَلَى بَنِي إِسْرَائِيلَ", "en": "The story of ʿĪsā: contempt and rebellion; God's favour on the Children of Israel", "tr": "Îsâ'nın kıssası: istihfaf ve isyan; Allah'ın İsrâiloğulları'na nimeti"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"; IS = "al-istifham"
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
def v_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, fa=False, hidden="هُوَ", ta=False):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    body = (" فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ." if ta else f" فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}، وَالضَّمِيرُ مَفْعُولٌ بِهِ." if hidden else " فِعْلٌ مَاضٍ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.")
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + [MB] + list(tags), pre + stem + body, en + " — a māḍī; the pronoun is its object.", tr + " — mâzî; zamir mef'ûl.", punct=punct, segments=segs)

def hal(full, lex, en, tr, punct=None, tags=(), ar="حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [HL] + list(tags), ar, en + " — a ḥāl.", tr + " — hâl.", punct=punct)
def naat2(full, lex, en, tr, case="raf", punct=None, tags=(), n="ثَانٍ"):
    C = {"jarr": "نَعْتٌ " + n + " مَجْرُورٌ بِالْكَسْرَةِ.", "raf": "نَعْتٌ " + n + " مَرْفُوعٌ بِالضَّمَّةِ.", "nasb": "نَعْتٌ " + n + " مَنْصُوبٌ بِالْفَتْحَةِ."}[case]
    return tok(full, lex, "noun", [NA] + list(tags), C, en + " — a further naʿt.", tr + " — bir sıfat daha.", punct=punct)
def la_jins(full, wa=False, punct=None):
    return tok(full, "la-nafiya", "part", ["la-nafiya-lil-jins"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", ("«and» + " if wa else "") + "«no» — the lā of the genus; it governs like inna.", ("«ve» + " if wa else "") + "«yok» — cins nefyeden lâ; inne gibi amel eder.", punct=punct, segments=(wa_("لَا", "la-nafiya", "part") if wa else None))
def ism_la(full, lex, en, tr, punct=None, tags=(), khabar="مَوْجُودٌ"):
    return tok(full, lex, "noun", ["la-nafiya-lil-jins", "hadhf-wa-taqdir"] + list(tags), f"اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ تَقْدِيرُهُ: {khabar}.", en + " — lā's ism, built on fatḥa; its khabar is understood.", tr + " — lâ'nın ismi, fetha üzere mebnî; haberi mahzuf.", punct=punct)
def v_pl_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), fa=False, wa=False):
    pre = "الْفَاءُ عَاطِفَةٌ، وَ" if fa else ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
    segs = ([seg("فَ" if fa else "وَ", "fa" if fa else "wa", "conj")] if (fa or wa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (fa or wa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", en + " — a māḍī on the group's wāw; the attached pronoun is its object.", tr + " — cemi vâvlı mâzî; bitişik zamir mef'ûl.", punct=punct, segments=segs)
def mazi_wa_alif(full, lex, en, tr, punct=None, tags=(), fa=False, wa=False, extra=""):
    pre = "الْفَاءُ عَاطِفَةٌ، وَ" if fa else ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
    body = full[2:] if (fa or wa) else full
    return tok(full, lex, "verb", ([AT] if (fa or wa) else []) + ["naqis-verbs"] + list(tags), pre + body + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ" + extra + ".", en + " — a defective māḍī before the group's wāw: its alif dropped, the fatḥa stays (أَبَوْا).", tr + " — nâkıs mâzî, cemi vâvı önünde elif düştü; fetha kaldı.", punct=punct, segments=(conj_segs(full, lex, "verb") if (fa or wa) else None))
def mazi_ta_naqis(full, lex, en, tr, punct=None, tags=(), wa=True):
    body = full[2:] if wa else full
    return tok(full, lex, "verb", ([AT] if wa else []) + ["naqis-verbs"] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + body + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", en + " — a defective māḍī (رَغَا) with the feminine tāʾ: the alif dropped before the sukūn, and the tāʾ takes a kasra before the next hamzat al-waṣl.", tr + " — nâkıs mâzî (رَغَا) + te'nis tâ'sı: elif düştü; tâ iki sâkin yüzünden kesre aldı.", punct=punct, segments=(conj_segs(full, lex, "verb") if wa else None))

def alayhi_salam(punct=None):
    return [prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon him» — the fronted khabar.", "«ona» — öne alınmış haber.", tags=[MK], extra_ar=" — خَبَرٌ مُقَدَّمٌ"),
            tok("السَّلَامُ", "salam", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«peace» — the delayed mubtadaʾ; a parenthetical prayer.", "«selâm» — sonraya bırakılmış mübtedâ; duâ cümlesi.", punct=punct)]
def ta_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), fa=False, wa=False, extra=""):
    pre = "الْفَاءُ عَاطِفَةٌ، وَ" if fa else ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "")
    segs = ([seg("فَ" if fa else "وَ", "fa" if fa else "wa", "conj")] if (fa or wa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (fa or wa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", en + " — a feminine māḍī; the attached pronoun is its object.", tr + " — müennes mâzî; bitişik zamir mef'ûl.", punct=punct, segments=segs)

def ma_mawsul_obj(en="«what»", tr="«… -ı»"): return tok("مَا", "ma-mawsula", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", en + " — the relative pronoun, the object.", tr + " — ism-i mevsûl, mef'ûl.")
def yasha(wa=False, punct=None): return tok("وَيَشَاءُ" if wa else "يَشَاءُ", "shaa", "verb", ([AT] if wa else []) + ["hollow-verbs", "mudari-marfu", MW], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "يَشَاءُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", ("«and» + " if wa else "") + "«He wills» — the ṣila.", ("«ve» + " if wa else "") + "«diler» — sıla.", punct=punct, segments=(wa_("يَشَاءُ", "shaa", "verb") if wa else None))

def an_nasb(obj_of, en="«to»", tr="«… -mesini»"): return tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ " + obj_of + ".", en, tr)
def mansub(full, lex, en, tr, punct=None, tags=(), hidden="هُوَ", extra=""):
    return tok(full, lex, "verb", [AN] + list(tags), "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", en + " — naṣb by an.", tr + " — en ile mansub.", punct=punct)

def ka_prep(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [HJ] + list(tags), "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ.", "«like» + " + en, "«gibi» + " + tr, punct=punct, segments=[seg("كَ", "ka", "prep"), seg(full[2:], lex, "noun")])


def li_noun(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [HJ] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".", "«to/for» + " + en, "«-e» + " + tr, punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "noun")])
def bi_noun(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [HJ] + list(tags), "الْبَاءُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ" + extra + ".", "«by/with» + " + en, "«ile» + " + tr, punct=punct, segments=[seg("بِ", "bi", "prep"), seg(full[2:], lex, "noun")])
def zarf(full, lex, en, tr, punct=None, kind="مَكَانٍ"):
    return tok(full, lex, "noun", [MF, ID], "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", en + " — an adverbial (ẓarf), annexed.", tr + " — zarf, muzâf.", punct=punct)
def wa_prep(full, lex, en, tr, punct=None):
    return tok(full, lex, "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " حَرْفُ جَرٍّ.", "«and» + " + en, "«ve» + " + tr, punct=punct, segments=wa_(full[2:], lex, "prep"))
def fa_la(jins=False):
    body = "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ" if jins else "لَا نَافِيَةٌ لَا عَمَلَ لَهَا"
    return tok("فَلَا", "la-nafiya", "part", ["la-nafiya-lil-jins" if jins else "la-nafiya", AT], "الْفَاءُ لِلتَّفْرِيعِ (عَاطِفَةٌ)، وَ" + body + ".", "«so … no» — the fāʾ draws the consequence; " + ("the lā of the genus." if jins else "the negating lā."), "«bu yüzden … yok/-mez» — fâ sonucu bağlar; " + ("cins nefyeden lâ." if jins else "nefiy lâ'sı."), segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")])
def khamsa_wa(full, lex, en, tr, tags=(), punct=None, extra_ar=""): return khamsa(full, lex, en, tr, tags=[AT] + list(tags), punct=punct, extra_ar=extra_ar, wa=True)

def kana_pl(full="وَكَانُوا", wa=True, khabar_note=""):
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا" + khabar_note + ".", ("«and» + " if wa else "") + "«they were» — kāna; the wāw is its ism.", ("«ve» + " if wa else "") + "«idiler» — kâne; vâv ismi.", segments=(wa_("كَانُوا", "kana", "verb") if wa else None))
def pron_atf(full, lex, stem, pron_form, pron_lex, en, tr, case="jarr", punct=None, tags=()):
    C = {"jarr": "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ", "raf": "مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ"}[case]
    return tok(full, lex, "noun", [AT, ID] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + stem + " " + C + "، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«and» + " + en + " — joined; annexed to the pronoun.", "«ve» + " + tr + " — ma'tûf; zamire muzâf.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "noun"), seg(pron_form, pron_lex, "pron")])

# ---------------------------------------------------------------- §4 اسْتِخْفَافٌ وَتَمَرُّدٌ (print pp. 42–43)
sen("s1", "And contempt for the prophets and boldness against them — even to killing — dealing in usury, and toying with the religious teachings bred in them harshness and dryness, and the weakness of human feeling;",
        "Peygamberleri hafife almak ve onlara — öldürmeye varıncaya dek — cüret etmek, faizle muamele ve dinî öğretilerle oynamak, onlarda katılığı ve kuruluğu, insanî duygunun zayıflığını doğurdu;", [
  mazi("وَوَلَّدَ", "wallada", "«and bred»", "«ve doğurdu»", tags=[AT, "form-ii-verbs"], wa=True, hidden=None),
  prep_pron("فِيهِمُ", "fi", "هِمُ", "pron-3mp", "«in them»", "«onlarda»", extra_ar=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الِاسْتِخْفَافُ", "istikhfaf", "«contempt»", "«hafife almak»", tags=["form-x-verbs"], extra_ar=" — مَصْدَرُ اسْتَخَفَّ"),
  bi_noun("بِالْأَنْبِيَاءِ", "nabi", "«for the prophets»", "«peygamberleri»", tags=[JT]),
  atf("وَالِاجْتِرَاءُ", "ijtira", "«boldness»", "«cüret»", "raf", tags=["form-viii-verbs"]),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«against them»", "«onlara»", punct="،"),
  tok("حَتَّى", "hatta", "part", [AT], "حَتَّى هُنَا ابْتِدَائِيَّةٌ لِلْغَايَةِ (بِمَعْنَى: بَلَغَ الِاجْتِرَاءُ الْقَتْلَ)، لَا عَاطِفَةٌ لِدُخُولِهَا عَلَى الْجَارِّ.", "«even» — ḥattā of the extreme limit; it precedes a jarr phrase, so it is not a conjunction here.", "«hatta» — gâye bildiren ibtidâiyye; câr üzerine geldiği için atıf değildir."),
  bi_noun("بِالْقَتْلِ", "qatl", "«to killing»", "«öldürmeye»", punct="،"),
  atf("وَالتَّعَامُلُ", "taamul", "«dealing»", "«muamele»", "raf", tags=["form-vi-verbs"]),
  tok("بِالرِّبَا", "riba", "noun", [HJ, "ism-maqsur-manqus"], "الْبَاءُ حَرْفُ جَرٍّ، وَالرِّبَا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمٌ مَقْصُورٌ.", "«in usury» — a maqṣūr noun; jarr by an estimated kasra.", "«faizle» — maksûr isim; takdîrî kesre.", segments=[seg("بِ", "bi", "prep"), seg("الرِّبَا", "riba", "noun")], punct="،"),
  atf("وَالْعَبَثُ", "abath", "«toying»", "«oynamak»", "raf"),
  bi_noun("بِالتَّعَالِيمِ", "talim", "«with the teachings»", "«öğretilerle»", tags=[JT], extra=" — صِيغَةُ مُنْتَهَى الْجُمُوعِ"),
  naat("الدِّينِيَّةِ", "dini", "«religious»", "«dinî»", tags=["ism-mansub"], punct="،"),
  maful_("الْغِلْظَةَ", "ghilza", "«harshness»", "«katılığı»", ar="مَفْعُولٌ بِهِ لِوَلَّدَ مَنْصُوبٌ بِالْفَتْحَةِ — أُخِّرَ عَنِ الْفَاعِلِ وَمَعْطُوفَاتِهِ."),
  atf("وَالْجَفَافَ", "jafaf", "«dryness»", "«kuruluğu»", "nasb", punct="،"),
  atf("وَضَعْفَ", "daf", "«the weakness [of]»", "«zayıflığını»", "nasb", tags=[ID], sign="بِالْفَتْحَةِ، مُضَافٌ"),
  mudaf_ilayh("الْعَاطِفَةِ", "atifa", "«feeling»", "«duygunun»"),
  naat("الْإِنْسَانِيَّةِ", "insani", "«human»", "«insanî»", tags=["ism-mansub"], punct="،"),
])
sen("s2", "and the hearts of many of them were stripped of the pure love of God, of mercy toward man — whatever his origin and his merit — and of respect for humanity.",
        "onlardan birçoğunun kalbi, Allah'ın hâlis sevgisinden, insana — aslı ve üstünlüğü ne olursa olsun — merhametten ve insanlığa saygıdan sıyrıldı.", [
  mazi_ta("وَتَجَرَّدَتْ", "tajarrada", "«and were stripped»", "«ve sıyrıldı»", tags=[AT, "form-v-verbs"], wa=True),
  fail("قُلُوبُ", "qalb", "«the hearts [of]»", "«kalpleri»", tags=[ID, JT], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("كَثِيرٍ", "kathir", "«many»", "«birçoğunun»"),
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«of them»", "«onlardan»"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("حُبِّ", "hubb", "«the love [of]»", "«sevgisinden»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  naat("الْخَالِصِ", "khalis", "«pure»", "«hâlis»", tags=["ism-fail"], punct="،"),
  atf("وَالرَّحْمَةِ", "rahma", "«mercy»", "«merhametten»"),
  prep("عَلَى", "ala", "«toward»", "«-e»"),
  majrur("الْإِنْسَانِ", "insan", "«man»", "«insana»"),
  tok("مَهْمَا", "mahma", "pron", [SH, KN, "jumla-mutarida"], "اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ — وَالْجُمْلَةُ مُعْتَرِضَةٌ.", "«whatever» — a jussive conditional noun, kāna's fronted khabar; a parenthesis.", "«ne olursa olsun» — cezm eden şart ismi, kâne'nin öne alınmış haberi; itirâzî cümle."),
  tok("كَانَ", "kana", "verb", [KN, SH, "hollow-verbs", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ، وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«was» — the condition's verb; its answer is understood from what precedes.", "«olursa» — şart fiili; cevabı öncesinden anlaşılır, mahzuf."),
  noun_pron("أَصْلُهُ", "asl", "أَصْلُ", "هُ", "pron-3ms", "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his origin» — kāna's ism.", "«aslı» — kâne'nin ismi.", tags=[KN, ID]),
  pron_atf("وَفَضْلُهُ", "fadl", "فَضْلُ", "هُ", "pron-3ms", "«his merit»", "«üstünlüğü»", case="raf"),
  atf("وَاحْتِرَامِ", "ihtiram", "«respect [for]»", "«saygıdan»", tags=[ID, "form-viii-verbs"], sign="بِالْكَسْرَةِ عَلَى حُبِّ، مُضَافٌ"),
  mudaf_ilayh("الْإِنْسَانِيَّةِ", "insaniyya", "«humanity»", "«insanlığa»", punct="."),
])
sen("s3", "And they all but forgot the meanings of solace and equality, of kindness and generosity,",
        "Yardımlaşmanın ve eşitliğin, iyiliğin ve cömertliğin mânalarını neredeyse unuttular;", [
  tok("وَكَادُوا", "kada", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَادُوا فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ (تَعْمَلُ عَمَلَ كَانَ)، وَالْوَاوُ اسْمُهَا.", "«and they all but» — kāda, a verb of nearness that governs like kāna; the wāw is its ism.", "«ve neredeyse» — kâde, mukârebe fiillerinden, kâne gibi amel eder; vâv ismi.", segments=wa_("كَادُوا", "kada", "verb")),
  khamsa("يَنْسَوْنَ", "nasiya", "«forgot»", "«unutuyorlardı»", tags=[KN, "naqis-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَادَ؛ حُذِفَتْ لَامُ الْفِعْلِ (الْأَلِفُ) لِالْتِقَاءِ السَّاكِنَيْنِ: يَنْسَى + ونَ"),
  tok("مَعَانِيَ", "mana", "noun", [MB, ID, JT, MM, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ — مَنْقُوصٌ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ (مَعَانٍ)، مُضَافٌ.", "«the meanings [of]» — the object; a manqūṣ muntahā plural shows its fatḥa.", "«mânalarını» — mef'ûl; müntehe'l-cumû' vezninde mankûs, fethası açıktır."),
  mudaf_ilayh("الْمُؤَاسَاةِ", "muasat", "«solace, mutual aid»", "«yardımlaşmanın»", tags=["form-iii-verbs"]),
  atf("وَالْمُسَاوَاةِ", "musawat", "«equality»", "«eşitliğin»", tags=["form-iii-verbs"], punct="،"),
  atf("وَالْبِرِّ", "birr", "«kindness»", "«iyiliğin»"),
  atf("وَالْكَرَمِ", "karam", "«generosity»", "«cömertliğin»", punct="،"),
])
sen("s4", "and they used to believe in the prophethoods and the messages — the prophets had been many among them and their scriptures teemed with their reports —",
        "peygamberliklere ve risaletlere inanırlardı — aralarında peygamberler çoğalmış, sahifeleri onların haberleriyle dolup taşmıştı —", [
  kana_pl(khabar_note=" — وَخَبَرُهَا الْجُمْلَةُ بَعْدَهَا"),
  khamsa("يُؤْمِنُونَ", "aamana", "«believe»", "«inanırlardı»", tags=[KN, "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  bi_noun("بِالنُّبُوَّاتِ", "nubuwwa", "«in the prophethoods»", "«peygamberliklere»", tags=[JM]),
  atf("وَالرِّسَالَاتِ", "risala", "«the messages»", "«risaletlere»", tags=[JM], punct="،"),
  tok("وَقَدْ", "qad", "part", [HL, "qad-harf"], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]» — the wāw of ḥāl with qad.", "«ve [gerçekten]» — hâl vâvı ile kad.", segments=wa_("قَدْ", "qad", "part")),
  mazi_ta("كَثُرَتْ", "kathura", "«had been many»", "«çoğalmıştı»", tags=[HL]),
  prep_pron("فِيهِمُ", "fi", "هِمُ", "pron-3mp", "«among them»", "«aralarında»", extra_ar=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الْأَنْبِيَاءُ", "nabi", "«the prophets»", "«peygamberler»", tags=[JT], punct="،"),
  mazi_ta("وَزَخَرَتْ", "zakhara", "«and teemed»", "«ve dolup taştı»", tags=[AT], wa=True),
  noun_pron("صُحُفُهُمْ", "sahifa", "صُحُفُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their scriptures» — the doer.", "«sahifeleri» — fâil.", tags=[FL, ID, JT]),
  tok("بِأَخْبَارِهِمْ", "khabar", "noun", [HJ, ID, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَأَخْبَارِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«with their reports»", "«onların haberleriyle»", segments=[seg("بِ", "bi", "prep"), seg("أَخْبَارِ", "khabar", "noun"), seg("هِمْ", "pron-3mp", "pron")], punct="،"),
])
sen("s5", "but in the latest age they had come to believe only in what agreed with their desire and backed them in their way of life and their morals;",
        "fakat son zamanda yalnızca hevâlarına uyan, yaşayışlarında ve ahlâklarında kendilerini destekleyen şeye inanır olmuşlardı;", [
  tok("وَلٰكِنَّهُمْ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَهُمْ اسْمُهَا.", "«but they» — lākinna, a sister of inna; the pronoun is its ism.", "«fakat onlar» — lâkinne, inne'nin kardeşi; zamir ismi.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«[indeed]»", "«[gerçekten]»"),
  tok("أَصْبَحُوا", "asbaha", "verb", [KN, IW, "form-iv-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا — وَالْجُمْلَةُ خَبَرُ لٰكِنَّ.", "«they had come to» — aṣbaḥa, a sister of kāna; the clause is lākinna's khabar.", "«… olmuşlardı» — asbaha, kâne'nin kardeşi; cümle lâkinne'nin haberi."),
  fi(),
  majrur("الزَّمَنِ", "zaman-period", "«the age»", "«zamanda»"),
  naat("الْأَخِيرِ", "akhir-last", "«latest»", "«son»"),
  la_nafiya(),
  khamsa("يُؤْمِنُونَ", "aamana", "«believe»", "«inanır»", tags=[KN, "la-nafiya", "form-iv-verbs"], extra_ar=" — بَعْدَ لَا النَّافِيَةِ؛ وَالْجُمْلَةُ خَبَرُ أَصْبَحَ"),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ (حَصْرٌ).", "«except, only» — an emptied exception: a restriction.", "«ancak» — müferrağ istisnâ: hasr."),
  tok("بِمَا", "ma-mawsula", "pron", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«in what» — the relative after bi.", "«… şeye» — bâ'dan sonra ism-i mevsûl.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  mazi("وَافَقَ", "wafaqa", "«agreed with»", "«uyan»", tags=[MW, "form-iii-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  noun_pron("هَوَاهُمْ", "hawa-desire", "هَوَا", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their desire» — the object; a maqṣūr noun.", "«hevâlarına» — mef'ûl; maksûr isim.", tags=[MB, ID, "ism-maqsur-manqus"], punct="،"),
  v_pron("وَأَيَّدَهُمْ", "ayyada", "أَيَّدَ", "هُمْ", "pron-3mp", "«and backed them»", "«ve kendilerini destekleyen»", tags=[MW, "form-ii-verbs"], wa=True),
  fi(),
  noun_pron("سِيرَتِهِمْ", "sira", "سِيرَتِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their way of life»", "«yaşayışlarında»", tags=[HJ, ID]),
  pron_atf("وَأَخْلَاقِهِمْ", "khuluq", "أَخْلَاقِ", "هِمْ", "pron-3mp", "«their morals»", "«ahlâklarında»", tags=[JT], punct="،"),
])
sen("s6", "as for whoever criticized them and called them to account, and summoned them to the sound religion, the plain truth and the mending of their state, they treated him as an enemy and fought him;",
        "onları eleştiren ve hesaba çeken, sahih dine, apaçık hakka ve hâlin ıslahına çağıran kimseye gelince, ona düşmanlık ettiler ve onunla savaştılar;", [
  tok("أَمَّا", "amma", "part", ["amma-tafsiliyya", SH], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ — وَجَوَابُهَا: عَادَوْهُ، جَاءَ بِلَا فَاءٍ عَلَى طَرِيقَةِ الْمُحْدَثِينَ؛ وَالْأَصْلُ لُزُومُ الْفَاءِ فِي جَوَابِ أَمَّا.", "«as for» — the particle of detailing; its answer «they treated him as an enemy» comes without the fāʾ, as modern prose allows, though the rule requires it.", "«-e gelince» — tafsîl edatı; cevabı «düşmanlık ettiler» fâ'sız gelmiştir (muhdes üslûp); aslında emmâ'nın cevabında fâ lâzımdır."),
  tok("مَنِ", "man-mawsula", "pron", [MK, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«whoever» — the relative as mubtadaʾ; its sukūn turns to kasra before the waṣl.", "«… kimse» — mübtedâ olan ism-i mevsûl; sükûnu vasl önünde kesreye döndü."),
  v_pron("انْتَقَدَهُمْ", "intaqada-criticize", "انْتَقَدَ", "هُمْ", "pron-3mp", "«criticized them»", "«onları eleştiren»", tags=[MW, "form-viii-verbs"]),
  v_pron("وَحَاسَبَهُمْ", "hasaba-call-to-account", "حَاسَبَ", "هُمْ", "pron-3mp", "«and called them to account»", "«ve hesaba çeken»", tags=[MW, "form-iii-verbs"], wa=True, punct="،"),
  v_pron("وَدَعَاهُمْ", "daa", "دَعَا", "هُمْ", "pron-3mp", "«and summoned them»", "«ve onları çağıran»", tags=[MW, "naqis-verbs"], wa=True),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("الدِّينِ", "din", "«the religion»", "«dine»"),
  naat("الصَّحِيحِ", "sahih", "«sound»", "«sahih»"),
  atf("وَالْحَقِّ", "haqq", "«the truth»", "«hakka»"),
  naat("الصَّرِيحِ", "sarih", "«plain»", "«apaçık»"),
  atf("وَإِصْلَاحِ", "islah", "«the mending [of]»", "«ıslahına»", tags=[ID, "form-iv-verbs"], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الْحَالِ", "hal", "«the state»", "«hâlin»", punct="،"),
  tok("عَادَوْهُ", "ada-hunt", "verb", [MK, MB, SH, "naqis-verbs", "form-iii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ وَجَوَابُ أَمَّا.", "«they treated him as an enemy» — a defective Form III māḍī (عَادَى) on the group's wāw; the clause is the khabar and ammā's answer.", "«ona düşmanlık ettiler» — nâkıs müfâale mâzîsi (عَادَى), cemi vâvlı; cümle haber ve emmâ'nın cevabı.", segments=[seg("عَادَوْ", "ada-hunt", "verb"), seg("هُ", "pron-3ms", "pron")]),
  v_pl_pron("وَحَارَبُوهُ", "haraba", "حَارَبُو", "هُ", "pron-3ms", "«and fought him»", "«ve onunla savaştılar»", tags=["form-iii-verbs"], wa=True, punct="،"),
])
sen("s7", "and they had a boldness for slander and fabrication, for concealing the truth, and for false witness.",
        "iftiraya ve uydurmaya, hakkı gizlemeye ve yalancı şahitliğe cüretleri vardı.", [
  tok("وَكَانَتْ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«and there was» — kāna with the feminine tāʾ.", "«ve … vardı» — kâne, te'nis tâ'sı ile.", segments=wa_("كَانَتْ", "kana", "verb")),
  noun_pron("عِنْدَهُمْ", "inda", "عِنْدَ", "هُمْ", "pron-3mp", "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِخَبَرِ كَانَ الْمُقَدَّمِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«with them» — attached to kāna's fronted khabar.", "«onlarda» — kâne'nin öne alınmış haberine bağlı.", tags=[KN, MF, ID]),
  tok("جَرَاءَةٌ", "jaraa", "noun", [KN], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a boldness» — kāna's delayed ism.", "«bir cüret» — kâne'nin sonraya bırakılmış ismi."),
  prep("عَلَى", "ala", "«for»", "«-e»"),
  majrur("الْبَهْتِ", "baht", "«slander»", "«iftiraya»"),
  atf("وَالِافْتِرَاءِ", "iftira", "«fabrication»", "«uydurmaya»", tags=["form-viii-verbs"], punct="،"),
  atf("وَكِتْمَانِ", "kitman", "«concealing [of]»", "«gizlemeye»", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الْحَقِّ", "haqq", "«the truth»", "«hakkı»", punct="،"),
  atf("وَشَهَادَةِ", "shahada", "«witness [of]»", "«şahitliğe»", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الزُّورِ", "zur", "«falsehood»", "«yalan»", punct="."),
])
# ---------------------------------------------------------------- §5 نِعْمَةُ اللهِ عَلَى بَنِي إِسْرَائِيلَ (print p. 43)
sen("s8", "And they were a nation that stood out from the contemporary nations in every age by the creed of tawḥīd; and that is the secret of their being preferred over others, and God Most High has said:",
        "Onlar her çağda tevhid akîdesiyle çağdaş ümmetlerden ayrılan bir ümmetti; işte başkalarına üstün kılınmalarının sırrı budur; Allah Teâlâ buyurmuştur:", [
  kana_pl(),
  tok("أُمَّةً", "umma", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a nation» — kāna's khabar.", "«bir ümmet» — kâne'nin haberi."),
  mudari("تَمْتَازُ", "imtaza", "«stands out»", "«ayrılan»", tags=["jumla-sifa", "hollow-verbs", "form-viii-verbs"], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِأُمَّةً"),
  tok("عَنِ", "an", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its sukūn turns to kasra before the article.", "«-den» — sükûnu harf-i târif önünde kesreye döndü."),
  majrur("الْأُمَمِ", "umma", "«the nations»", "«ümmetlerden»", tags=[JT]),
  naat("الْمُعَاصِرَةِ", "muasir", "«contemporary»", "«çağdaş»", tags=["ism-fail", "form-iii-verbs"]),
  fi(),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("زَمَانٍ", "zaman", "«age»", "«çağda»", punct="،"),
  bi_noun("بِعَقِيدَةِ", "aqida", "«by the creed [of]»", "«akîdesiyle»", tags=[ID], extra="، مُضَافٌ — مُتَعَلِّقٌ بِتَمْتَازُ"),
  mudaf_ilayh("التَّوْحِيدِ", "tawhid", "«tawḥīd»", "«tevhid»", punct="،"),
  tok("وَذٰلِكَ", "dhalika", "pron", [MK, "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and that» — a demonstrative as mubtadaʾ.", "«ve işte bu» — işaret ismi, mübtedâ.", segments=wa_("ذٰلِكَ", "dhalika", "pron")),
  tok("سِرُّ", "sirr", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the secret [of]» — the khabar.", "«sırrı» — haber."),
  noun_pron("تَفْضِيلِهِمْ", "tafdil", "تَفْضِيلِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their being preferred»", "«üstün kılınmalarının»", tags=[ID, "form-ii-verbs"]),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  noun_pron("غَيْرِهِمْ", "ghayr", "غَيْرِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«others»", "«başkalarına»", tags=[HJ, ID], punct="،"),
  tok("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi("قَالَ", "qala", "«said»", "«buyurdu»", tags=["hollow-verbs"], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
])
sen("s9", "«O Children of Israel, remember My favour which I bestowed upon you, and that I preferred you over the worlds.» (2:47)",
        "«Ey İsrâiloğulları! Size verdiğim nimetimi ve sizi âlemlere üstün kıldığımı hatırlayın.» (2:47)", [
  *quran([
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("بَنِي", "banu-israil", "noun", ["vocative-munada", ID, JS], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«Children [of]» — an annexed munādā; naṣb by the yāʾ, its nūn dropped for the annexation.", "«oğulları» — muzâf münâdâ; yâ ile mansub, nûnu izâfet için düştü."),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Israel» — a diptote: fatḥa for kasra.", "«İsrâil» — gayr-i munsarıf: kesre yerine fetha."),
  tok("اذْكُرُوا", "dhakara", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — هَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«remember» — an imperative built on dropping the nūn; the wāw is the doer.", "«hatırlayın» — nûnun hazfi üzere mebnî emir; vâv fâil."),
  noun_pron("نِعْمَتِيَ", "nima", "نِعْمَتِ", "يَ", "pron-1s", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ (فُتِحَتْ).", "«My favour» — the object; the speaker's yāʾ takes a fatḥa here.", "«nimetimi» — mef'ûl; mütekellim yâ'sı burada fethalı.", tags=[MB, ID, "ya-al-mutakallim"]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِنِعْمَتِي.", "«which» — the relative, a naʿt.", "«ki» — sıfat olan ism-i mevsûl."),
  tok("أَنْعَمْتُ", "anama", "verb", [MW, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةٌ.", "«I bestowed» — the tāʾ is the doer; the ṣila.", "«verdim» — tâ fâil; sıla.", segments=[seg("أَنْعَمْ", "anama", "verb"), seg("تُ", "pron-1s", "pron")]),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«upon you»", "«size»"),
  tok("وَأَنِّي", "anna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى نِعْمَتِي.", "«and that I» — anna with the yāʾ as its ism; the clause is joined to «My favour».", "«ve … -ımı» — enne, yâ ismi; te'vîl-i masdar «nimetimi»ye ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("أَنِّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("فَضَّلْتُكُمْ", "faddala", "verb", [IW, MB, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«I preferred you» — the tāʾ the doer, the kāf the object; anna's khabar.", "«sizi üstün kıldım» — tâ fâil, kâf mef'ûl; enne'nin haberi.", segments=[seg("فَضَّلْ", "faddala", "verb"), seg("تُ", "pron-1s", "pron"), seg("كُمْ", "pron-2mp", "pron")]),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  tok("الْعَالَمِينَ", "alam", "noun", [HJ, JS], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«the worlds» — jarr by the yāʾ, as a sound masculine plural.", "«âlemlere» — cemi müzekker sâlime mülhak; yâ ile mecrûr.", punct="."),
  ]),
])

CAND = {
 "wallada": G("wallada", "وَلَّدَ", "و ل د", "verb", "to breed, to generate (Form II)", "doğurmak, meydana getirmek (tef'îl)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "istikhfaf": G("istikhfaf", "اِسْتِخْفَاف", "خ ف ف", "noun", "contempt, making light (bi: of) (the maṣdar of Form X)", "hafife alma, istihfaf (istif'âl masdarı)", 2),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "ijtira": G("ijtira", "اِجْتِرَاء", "ج ر أ", "noun", "boldness, audacity (ʿalā: against) (the maṣdar of Form VIII)", "cüret, küstahlık (iftiâl masdarı)", 3),
 "ala": G("ala", "عَلَى", None, "prep", "on, against", "üzerine, -e karşı", 1),
 "hatta": G("hatta", "حَتَّى", None, "part", "until; even", "-e kadar; hatta", 1),
 "qatl": G("qatl", "قَتْل", "ق ت ل", "noun", "killing", "öldürme", 1),
 "taamul": G("taamul", "تَعَامُل", "ع م ل", "noun", "dealing (bi: in) (the maṣdar of Form VI)", "muamele, alışveriş (tefâul masdarı)", 2),
 "riba": G("riba", "رِبًا", "ر ب و", "noun", "usury, interest (a maqṣūr noun)", "faiz, ribâ (maksûr isim)", 1),
 "abath": G("abath", "عَبَث", "ع ب ث", "noun", "toying, tampering (bi: with); futility", "oyun, kurcalama; abes", 2),
 "talim": G("talim", "تَعْلِيم", "ع ل م", "noun", "teaching; (pl.) teachings, doctrines", "öğretme; (ç.) öğretiler, tâlimat", 1, plural="تَعَالِيم"),
 "dini": G("dini", "دِينِيّ", "د ي ن", "noun", "religious (a nisba)", "dinî (nisbet)", 1),
 "ghilza": G("ghilza", "غِلْظَة", "غ ل ظ", "noun", "harshness, coarseness", "katılık, kabalık", 2),
 "jafaf": G("jafaf", "جَفَاف", "ج ف ف", "noun", "dryness", "kuruluk", 2),
 "daf": G("daf", "ضَعْف", "ض ع ف", "noun", "weakness", "zayıflık", 1),
 "atifa": G("atifa", "عَاطِفَة", "ع ط ف", "noun", "feeling, sentiment", "duygu, âtıfe", 2, plural="عَوَاطِف"),
 "insani": G("insani", "إِنْسَانِيّ", "أ ن س", "noun", "human (a nisba)", "insanî (nisbet)", 1),
 "tajarrada": G("tajarrada", "تَجَرَّدَ", "ج ر د", "verb", "to be stripped (min: of) (Form V)", "sıyrılmak, soyunmak (tefa''ul)", 2),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "a heart", "kalp", 1, plural="قُلُوب"),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "hubb": G("hubb", "حُبّ", "ح ب ب", "noun", "love", "sevgi", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "khalis": G("khalis", "خَالِص", "خ ل ص", "noun", "pure, sincere (an active participle)", "hâlis, katıksız (ism-i fâil)", 1),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet, merhamet", 1),
 "insan": G("insan", "إِنْسَان", "أ ن س", "noun", "a human being", "insan", 1),
 "mahma": G("mahma", "مَهْمَا", None, "pron", "whatever (a jussive conditional noun)", "her ne … olursa olsun (cezm eden şart ismi)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "asl": G("asl", "أَصْل", "أ ص ل", "noun", "origin, root", "asıl, kök", 1, plural="أُصُول"),
 "fadl": G("fadl", "فَضْل", "ف ض ل", "noun", "merit, grace", "fazilet, lütuf", 1),
 "ihtiram": G("ihtiram", "اِحْتِرَام", "ح ر م", "noun", "respect (the maṣdar of Form VIII)", "saygı, ihtiram (iftiâl masdarı)", 1),
 "insaniyya": G("insaniyya", "إِنْسَانِيَّة", "أ ن س", "noun", "humanity (an abstract nisba)", "insanlık (masdar-ı sınâî)", 2),
 "kada": G("kada", "كَادَ", "ك و د", "verb", "to be on the point of, all but (a verb of nearness, hollow)", "neredeyse … -mek (mukârebe fiili, ecvef)", 2),
 "nasiya": G("nasiya", "نَسِيَ", "ن س ي", "verb", "to forget (defective)", "unutmak (nâkıs)", 1),
 "mana": G("mana", "مَعْنًى", "ع ن ي", "noun", "a meaning", "mâna", 1, plural="مَعَانٍ"),
 "muasat": G("muasat", "مُؤَاسَاة", "أ س و", "noun", "solace, sharing another's burden (the maṣdar of Form III)", "yardımlaşma, teselli, muvâsât (müfâale masdarı)", 3),
 "musawat": G("musawat", "مُسَاوَاة", "س و ي", "noun", "equality (the maṣdar of Form III)", "eşitlik, müsâvât (müfâale masdarı)", 2),
 "birr": G("birr", "بِرّ", "ب ر ر", "noun", "kindness, piety", "iyilik, birr", 1),
 "karam": G("karam", "كَرَم", "ك ر م", "noun", "generosity", "cömertlik, kerem", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب أ", "noun", "prophethood", "nübüvvet, peygamberlik", 1, plural="نُبُوَّات"),
 "risala": G("risala", "رِسَالَة", "ر س ل", "noun", "a message; a mission", "risalet; mesaj", 1, plural="رِسَالَات"),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, to abound", "çok olmak, çoğalmak", 1),
 "zakhara": G("zakhara", "زَخَرَ", "ز خ ر", "verb", "to teem, to overflow (bi: with)", "dolup taşmak (bi ile)", 3),
 "sahifa": G("sahifa", "صَحِيفَة", "ص ح ف", "noun", "a scripture, a scroll; a page", "sahife, sayfa; kitap", 1, plural="صُحُف"),
 "khabar": G("khabar", "خَبَر", "خ ب ر", "noun", "a report, news", "haber", 1, plural="أَخْبَار"),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but (a sister of inna)", "fakat (inne'nin kardeşi)", 1),
 "asbaha": G("asbaha", "أَصْبَحَ", "ص ب ح", "verb", "to become (a sister of kāna, Form IV)", "olmak, hâline gelmek (kâne'nin kardeşi, if'âl)", 1),
 "zaman-period": G("zaman-period", "زَمَن", "ز م ن", "noun", "a time, a period", "zaman, dönem", 1, plural="أَزْمَان"),
 "akhir-last": G("akhir-last", "أَخِير", "أ خ ر", "noun", "last, latest", "son, sonuncu", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "wafaqa": G("wafaqa", "وَافَقَ", "و ف ق", "verb", "to agree with, to suit (Form III)", "uymak, muvafık olmak (müfâale)", 1),
 "hawa-desire": G("hawa-desire", "هَوًى", "ه و ي", "noun", "desire, caprice (a maqṣūr noun)", "hevâ, nefsin arzusu (maksûr isim)", 2),
 "ayyada": G("ayyada", "أَيَّدَ", "أ ي د", "verb", "to back, to support (Form II)", "desteklemek, te'yid etmek (tef'îl)", 2),
 "sira": G("sira", "سِيرَة", "س ي ر", "noun", "a way of life, conduct; a biography", "yaşayış, sîret", 1),
 "khuluq": G("khuluq", "خُلُق", "خ ل ق", "noun", "character, a moral trait", "huy, ahlâk", 1, plural="أَخْلَاق"),
 "amma": G("amma", "أَمَّا", None, "part", "as for", "-e gelince", 1),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "whoever, he who", "kim ki, … kimse", 1),
 "intaqada-criticize": G("intaqada-criticize", "اِنْتَقَدَ", "ن ق د", "verb", "to criticize (Form VIII)", "eleştirmek, tenkit etmek (iftiâl)", 2),
 "hasaba-call-to-account": G("hasaba-call-to-account", "حَاسَبَ", "ح س ب", "verb", "to call to account (Form III)", "hesaba çekmek (müfâale)", 2),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call, to summon; to pray", "çağırmak; dua etmek", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "sahih": G("sahih", "صَحِيح", "ص ح ح", "noun", "sound, correct", "sahih, doğru", 1),
 "haqq": G("haqq", "الْحَقّ", "ح ق ق", "noun", "the truth; a right", "hak, gerçek", 1),
 "sarih": G("sarih", "صَرِيح", "ص ر ح", "noun", "plain, explicit", "açık, sarih", 2),
 "islah": G("islah", "إِصْلَاح", "ص ل ح", "noun", "mending, reform (the maṣdar of Form IV)", "ıslah, düzeltme (if'âl masdarı)", 1),
 "hal": G("hal", "حَال", "ح و ل", "noun", "a state, a condition", "hâl, durum", 1, plural="أَحْوَال"),
 "ada-hunt": G("ada-hunt", "عَادَى", "ع د و", "verb", "to treat as an enemy (Form III, defective)", "düşmanlık etmek (müfâale, nâkıs)", 2),
 "haraba": G("haraba", "حَارَبَ", "ح ر ب", "verb", "to fight, to make war on (Form III)", "savaşmak (müfâale)", 1),
 "inda": G("inda", "عِنْدَ", None, "noun", "with, at, in the presence of", "yanında, katında", 1),
 "jaraa": G("jaraa", "جَرَاءَة", "ج ر أ", "noun", "boldness, daring", "cüret, cesaret", 2),
 "baht": G("baht", "بَهْت", "ب ه ت", "noun", "slander, a calumny", "iftira, bühtan", 3),
 "iftira": G("iftira", "اِفْتِرَاء", "ف ر ي", "noun", "fabrication, a lie (the maṣdar of Form VIII)", "iftira, uydurma (iftiâl masdarı)", 2),
 "kitman": G("kitman", "كِتْمَان", "ك ت م", "noun", "concealing", "gizleme, kitman", 2),
 "shahada": G("shahada", "شَهَادَة", "ش ه د", "noun", "testimony, witness", "şahitlik, şehâdet", 1),
 "zur": G("zur", "زُور", "ز و ر", "noun", "falsehood", "yalan, zûr", 2),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "imtaza": G("imtaza", "اِمْتَازَ", "م ي ز", "verb", "to stand out (ʿan: from) (Form VIII, hollow)", "ayrılmak, seçkin olmak (iftiâl, ecvef)", 2),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "muasir": G("muasir", "مُعَاصِر", "ع ص ر", "noun", "contemporary (an active participle of Form III)", "çağdaş, muâsır (müfâale ism-i fâili)", 2),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "zaman": G("zaman", "زَمَان", "ز م ن", "noun", "time, an age", "zaman", 1),
 "aqida": G("aqida", "عَقِيدَة", "ع ق د", "noun", "a creed", "akîde", 1, plural="عَقَائِد"),
 "tawhid": G("tawhid", "تَوْحِيد", "و ح د", "noun", "tawḥīd, the affirming of God's oneness", "tevhid", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "sirr": G("sirr", "سِرّ", "س ر ر", "noun", "a secret", "sır", 1, plural="أَسْرَار"),
 "tafdil": G("tafdil", "تَفْضِيل", "ف ض ل", "noun", "preferring (the maṣdar of Form II)", "üstün kılma, tafdil (tef'îl masdarı)", 2),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not, without", "başka; gayri, -sız", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "banu-israil": G("banu-israil", "بَنُو إِسْرَائِيلَ", "ب ن ي", "noun", "the Children of Israel", "İsrâiloğulları", 1),
 "israil": G("israil", "إِسْرَائِيل", None, "propn", "Israel (Yaʿqūb)", "İsrâil (Yâkub)", 1),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to remember; to mention", "hatırlamak; zikretmek", 1),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a favour, a blessing", "nimet", 1, plural="نِعَم"),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "anama": G("anama", "أَنْعَمَ", "ن ع م", "verb", "to bestow a favour (ʿalā: on) (Form IV)", "nimet vermek (if'âl)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (pl.)", "siz / sizi / sizin", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "faddala": G("faddala", "فَضَّلَ", "ف ض ل", "verb", "to prefer (ʿalā: over) (Form II)", "üstün kılmak (tef'îl)", 1),
 "alam": G("alam", "عَالَم", "ع ل م", "noun", "a world", "âlem", 1, plural="عَالَمُونَ / عَوَالِم"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "wallada", _sg.derived(_sg.B2, _sg.W2, "ُ", "وَلَّد", "وَلِّد", "وَلِّد", "تَوْلِيد", "مُوَلِّد", "مُوَلَّد", "وُلِّدَ", "يُوَلَّدُ", "وَلَّدَ الشَّيْءَ: أَنْتَجَهُ وَأَحْدَثَهُ."))
put_morph(mo, "zakhara", _sg.sound1("fataha", "زَخَر", "زْخَر", "اِزْخَر", "زَخْر / زُخُور", "زَاخِر", None, None, None, "زَخَرَ الْبَحْرُ يَزْخَرُ: امْتَلَأَ وَفَاضَ؛ وَزَخَرَتِ الصُّحُفُ بِالْأَخْبَارِ: امْتَلَأَتْ بِهَا."))
put_morph(mo, "ayyada", _sg.derived(_sg.B2, _sg.W2, "ُ", "أَيَّد", "ؤَيِّد", "أَيِّد", "تَأْيِيد", "مُؤَيِّد", "مُؤَيَّد", "أُيِّدَ", "يُؤَيَّدُ", "أَيَّدَهُ: قَوَّاهُ وَنَصَرَهُ — مَهْمُوزُ الْفَاءِ."))
put_morph(mo, "intaqada-criticize", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَقَد", "نْتَقِد", "اِنْتَقِد", "اِنْتِقَاد", "مُنْتَقِد", "مُنْتَقَد", "اُنْتُقِدَ", "يُنْتَقَدُ", "اِنْتَقَدَ الشَّيْءَ: أَظْهَرَ عُيُوبَهُ وَمَحَاسِنَهُ."))
put_morph(mo, "hasaba-call-to-account", _sg.derived(_sg.B3, _sg.W3, "ُ", "حَاسَب", "حَاسِب", "حَاسِب", "مُحَاسَبَة / حِسَاب", "مُحَاسِب", "مُحَاسَب", "حُوسِبَ", "يُحَاسَبُ", "حَاسَبَهُ: نَاقَشَهُ الْحِسَابَ وَسَأَلَهُ عَمَّا فَعَلَ."))
put_morph(mo, "haraba", _sg.derived(_sg.B3, _sg.W3, "ُ", "حَارَب", "حَارِب", "حَارِب", "مُحَارَبَة / حِرَاب", "مُحَارِب", "مُحَارَب", "حُورِبَ", "يُحَارَبُ", "حَارَبَهُ: قَاتَلَهُ وَنَاصَبَهُ الْحَرْبَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch25 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 25 (print pp. 42–43; ʿĪsā §4–5): contempt and rebellion — what the Roman servitude bred (s1–s2), forgetting equality (s3), believing only what suited their desire and fighting the critic (s4–s7); God's favour on the Children of Israel: tawḥīd, with 2:47 (s8–s9)."
ADD_TR = " Yirmi beşinci bölüm (baskı s. 42–43; Îsâ §4–5): istihfaf ve isyan — Roma köleliğinin doğurdukları (s1–s2), eşitliği unutmak (s3), yalnız hevâya uyana inanmak ve eleştireni savaşmak (s4–s7); Allah'ın İsrâiloğulları'na nimeti: tevhid, 2:47 ile (s8–s9)."
write_out(25, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §4–5", GLOSS_ADD, notes=(), related=())
report(25, S, GLOSS_ADD, ())
