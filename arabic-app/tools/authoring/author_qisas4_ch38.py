# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 38: «قِصَّةُ عِيسَى» §23 (the Jews try to be rid of him: the case before the Roman governor), §24 (the style of the aggrieved and the politicians: a danger to the state), §25 (cunning and guile: religion mixed with politics), §26 (a problem: the foreign rulers cannot see the truth of the matter); print pp. 55–56.
python3 tools/authoring/author_qisas4_ch38.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: الْيَهُودُ يُحَاوِلُونَ التَّخَلُّصَ مِنْ سَيِّدِنَا عِيسَى", "en": "The story of ʿĪsā: the Jews try to be rid of our master ʿĪsā", "tr": "Îsâ'nın kıssası: Yahudiler efendimiz Îsâ'dan kurtulmaya çalışır"}
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

def mudari_wa(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, sign="بِالضَّمَّةِ", extra=""):
    return tok(full, lex, "verb", [AT, "mudari-marfu"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign + (("، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden) if hidden else "") + extra + ".", "«and» + " + en + " — a muḍāriʿ in rafʿ; the doer is concealed.", "«ve» + " + tr + " — merfû muzari; fâil gizli.", punct=punct, segments=wa_(full[2:], lex, "verb"))
def tahaddi(first=False, punct=None):
    return tok("تَحَدِّيًا", "tahaddi", "noun", ([KN] if first else [BD, "tawkid"]) + ["ism-maqsur-manqus", "form-v-verbs"], ("خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ" if first else "بَدَلٌ مُطَابِقٌ (تَوْكِيدٌ لَفْظِيٌّ بِالتَّكْرَارِ) مَنْصُوبٌ") + " — مَصْدَرُ تَحَدَّى، مَنْقُوصٌ: تَحَدٍّ، تَظْهَرُ فَتْحَتُهُ فِي النَّصْبِ.", "«a challenge» — " + ("kāna's khabar; " if first else "repeated as a badal; ") + "the manqūṣ maṣdar of taḥaddā shows its fatḥa in naṣb.", "«bir meydan okuma» — " + ("kâne'nin haberi; " if first else "tekrarla bedel; ") + "tehaddâ'nın mankûs masdarı, nasbda fethası görünür.", punct=punct)

def fa_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", extra=""):
    return tok(full, lex, "verb", [AT, "mudari-marfu"] + list(tags), "الْفَاءُ عَاطِفَةٌ، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", "«so» + " + en + " — a muḍāriʿ; the doer is concealed.", "«böylece» + " + tr + " — muzari; fâil gizli.", segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])
def bi_ma(punct=None, extra=""):
    return tok("بِمَا", "ma-mawsula", "pron", [HJ, MW], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ" + extra + ".", "«of what» — the relative after bi.", "«… şeyi» — bâ'dan sonra ism-i mevsûl.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")])
ISA_FAIL = " — يَعُودُ عَلَى عِيسَى عَلَى مَعْنَى الْآيَةِ (وَأُبْرِئُ)، وَيَصِحُّ عَوْدُهُ عَلَى اللهِ"

def wa_min(en="«and of»", tr="«ve … -den»", extra=""):
    return tok("وَمِنَ", "min", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَمِنَ حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ" + extra + ".", en, tr, segments=wa_("مِنَ", "min", "prep"))
AYA = "۝"

def bi_idhn(punct=None):
    return [bi_noun("بِإِذْنِ", "idhn", "«by the leave [of]»", "«izniyle»", tags=[ID], extra="، مُضَافٌ"),
            tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct=punct)]
def jitukum(wa=False):
    return tok(("وَ" if wa else "") + "جِئْتُكُمْ", "jaa", "verb", ([AT] if wa else [IW]) + [MB, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "جِئْتُ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — أَجْوَفُ: حُذِفَتْ عَيْنُهُ وَكُسِرَ مَا قَبْلَهَا (جِئْتُ)" + ("" if wa else "؛ وَالْجُمْلَةُ خَبَرُ أَنَّ") + ".", ("«and» + " if wa else "") + "«I have come to you» — the hollow verb drops its middle before the tāʾ; the kāf is the object.", ("«ve» + " if wa else "") + "«size geldim» — ecvef fiil tâ önünde ortasını düşürür; kâf mef'ûl.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("جِئْ", "jaa", "verb"), seg("تُ", "pron-1s", "pron"), seg("كُمْ", "pron-2mp", "pron")])
def bi_aya():
    return [bi_noun("بِآيَةٍ", "aya", "«with a sign»", "«bir âyetle»"), prep("مِنْ", "min", "«from»", "«-den»"),
            noun_pron("رَبِّكُمْ", "rabb", "رَبِّ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِآيَةٍ.", "«your Lord» — the phrase is a ṣifa of «a sign».", "«Rabbiniz» — ibare «âyet»in sıfatı.", tags=[HJ, ID, NA])]

def alladhina(case, role, en, tr, tags=()):
    C = {"raf": "رَفْعٍ", "nasb": "نَصْبٍ", "jarr": "جَرٍّ"}[case]
    return tok("الَّذِينَ", "alladhina", "pron", [MW] + list(tags), "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ " + C + " " + role + ".", en, tr)
def kafaru(role=" — صِلَةٌ", en="«disbelieved» — the ṣila.", tr="«inkâr ettiler» — sıla."):
    return tok("كَفَرُوا", "kafara", "verb", [MW], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ" + role + ".", en, tr)
def participle_ka(full, lex, stem, en, tr, tags=(), ar_extra="", wa=True, first=False):
    return tok(full, lex, "noun", ([AT] if wa else []) + [IW, ID, "ism-fail"] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + stem + (" خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ" if first else " مَعْطُوفٌ عَلَى خَبَرِ إِنَّ مَرْفُوعٌ") + "، مُضَافٌ إِلَى الْكَافِ (إِضَافَةٌ لَفْظِيَّةٌ: اسْمُ الْفَاعِلِ إِلَى مَفْعُولِهِ)" + ar_extra + ".", ("«and» + " if wa else "") + en + " — an active participle annexed to its object, the kāf.", ("«ve» + " if wa else "") + tr + " — mef'ûlü olan kâf'a muzâf ism-i fâil.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "noun"), seg("كَ", "pron-2ms", "pron")])

def amanna(wa=False, tags=()):
    return tok(("وَ" if wa else "") + "آمَنَّا", "aamana", "verb", ([AT] if wa else []) + ["form-iv-verbs"] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "آمَنَّا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — أُدْغِمَتْ نُونُ الْفِعْلِ فِي نُونِ الضَّمِيرِ.", ("«and» + " if wa else "") + "«we believe» — nā is the doer.", ("«ve» + " if wa else "") + "«inandık» — nâ fâil.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("آمَ", "aamana", "verb"), seg("نَّا", "pron-1p", "pron")])
def li_anna(full, pron_form, pron_lex, en, tr):
    return tok(full, "anna", "part", [HJ, IW, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ.", en + " — the lām of cause with anna; the pronoun is its ism.", tr + " — ta'lil lâmı ile enne; zamir ismi.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), seg(pron_form, pron_lex, "pron")])
def wa_fiha():
    return tok("وَفِيهَا", "fi", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and in it» — a fronted khabar.", "«ve onda» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")])

def kana_pl(full="وَكَانُوا", wa=True, khabar_note=""):
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كَانُوا فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا" + khabar_note + ".", ("«and» + " if wa else "") + "«they were» — kāna; the wāw is its ism.", ("«ve» + " if wa else "") + "«idiler» — kâne; vâv ismi.", segments=(wa_("كَانُوا", "kana", "verb") if wa else None))
def hal_pair(full, lex, en, tr, punct=None, tags=()):
    return hal(full, lex, en, tr, punct=punct, tags=["ism-fail"] + list(tags))

def maida_min_sama(punct=None):
    return [maful_("مَائِدَةً", "maida", "«a table»", "«bir sofra»"),
            tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
            majrur("السَّمَاءِ", "sama", "«heaven»", "«gökten»", punct=punct)]
def js_naat(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [NA, JS] + list(tags), "نَعْتٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", en + " — a naʿt; jarr by the yāʾ.", tr + " — sıfat; yâ ile mecrûr.", punct=punct)

def wa_la_mudari(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra=""):
    """«وَلَا يَفْعَلُ» as TWO tokens: the joined negating lā, then the muḍāriʿ (wave 32: a token is one printed word)."""
    verb = full.split()[-1]
    return [tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not» — the negating lā, joined.", "«ve … -mez» — ma'tûf nefiy lâ'sı.", segments=wa_("لَا", "la-nafiya", "part")),
            tok(verb, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), verb + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", en, tr, punct=punct)]

# ---------------------------------------------------------------- §23 الْيَهُودُ يُحَاوِلُونَ التَّخَلُّصَ مِنْ سَيِّدِنَا عِيسَى (print p. 55)
sen("s1", "The Jews' patience was exhausted and the cup of their enmity and obstinacy overflowed, so they wanted to be rid of our master ʿĪsā; they brought his case before the Roman governor and said:",
        "Yahudilerin sabrı tükendi, düşmanlık ve inat kâseleri taştı; bunun üzerine efendimiz Îsâ'dan kurtulmak istediler; davasını Roma valisine götürdüler ve dediler:", [
  tok("وَعِيلَ", "ala-overcome", "verb", [AT, NF, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَعِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ: عَالَ يَعِيلُ، كُسِرَ أَوَّلُهُ وَقُلِبَتْ عَيْنُهُ يَاءً فِي الْمَجْهُولِ؛ عِيلَ صَبْرُهُ: نَفِدَ.", "«was exhausted» — the passive of the hollow ʿāla: its first letter takes a kasra and the middle becomes yāʾ; «his patience was overcome».", "«tükendi» — ecvef âle'nin meçhulü: ilk harf kesre, orta harf yâ; «sabrı tükendi».", segments=wa_("عِيلَ", "ala-overcome", "verb")),
  fail("صَبْرُ", "sabr", "«the patience [of]»", "«sabrı»", tags=[NF, ID], extra_ar=" — نَائِبُ فَاعِلٍ، مُضَافٌ"),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»", punct="،"),
  mazi_ta("وَفَاضَتْ", "fada", "«and overflowed»", "«ve taştı»", tags=[AT, "hollow-verbs"], wa=True),
  fail("كَأْسُ", "kas", "«the cup [of]»", "«kâsesi»", tags=[ID], extra_ar="، مُضَافٌ"),
  noun_pron("عَدَائِهِمْ", "ada-hostility", "عَدَائِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their enmity»", "«düşmanlıklarının»", tags=[ID]),
  pron_atf("وَعِنَادِهِمْ", "inad", "عِنَادِ", "هِمْ", "pron-3mp", "«their obstinacy»", "«ve inatlarının»", punct="،"),
  tok("فَأَرَادُوا", "arada", "verb", [AT, "hollow-verbs", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَأَرَادُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they wanted»", "«bunun üzerine istediler»", segments=[seg("فَ", "fa", "conj"), seg("أَرَادُوا", "arada", "verb")]),
  maful_("التَّخَلُّصَ", "takhallus", "«to be rid»", "«kurtulmayı»", tags=["form-v-verbs"]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[HJ, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ'dan»", punct="،"),
  tok("فَرَفَعُوا", "rafaa", "verb", [AT], "الْفَاءُ عَاطِفَةٌ، وَرَفَعُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«they brought»", "«götürdüler»", segments=[seg("فَ", "fa", "conj"), seg("رَفَعُوا", "rafaa", "verb")]),
  noun_pron("قَضِيَّتَهُ", "qadiyya", "قَضِيَّتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his case» — the object.", "«davasını» — mef'ûl.", tags=[MB, ID]),
  prep("إِلَى", "ila", "«before»", "«-e»"),
  majrur("الْحَاكِمِ", "hakim-ruler", "«the governor»", "«valisine»", tags=["ism-fail"]),
  naat("الرُّومِيِّ", "rumi", "«Roman»", "«Roma»", tags=["ism-mansub"]),
  mazi_pl("وَقَالُوا", "qala", "«and said»", "«ve dediler»", tags=[AT, "hollow-verbs"], wa=True, punct=":"),
])
sen("s2", "«He is a rebellious, anarchic man who has broken away from our religion, led our young astray and seduced them by himself, split our ranks, made light of our minds and troubled our peace.",
        "«O, dinimizden çıkmış, gençlerimizi baştan çıkarmış ve onları kendisine kaptırmış, birliğimizi bölmüş, akıllarımızı hafife almış ve huzurumuzu bozmuş âsi, anarşist bir adamdır.", [
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — مَقُولُ الْقَوْلِ.", "«he is indeed» — inna with the hāʾ; the saying.", "«şüphesiz o» — inne ile hâ; söz.", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("رَجُلٌ", "rajul", "noun", [IW], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«a man» — inna's khabar.", "«bir adam» — inne'nin haberi."),
  naat("ثَائِرٌ", "thair", "«rebellious»", "«âsi»", case="raf", tags=["ism-fail", "hollow-verbs"]),
  naat2("فَوْضَوِيٌّ", "fawdawi", "«anarchic»", "«anarşist»", case="raf", tags=["ism-mansub"]),
  mazi("مَرَقَ", "maraqa", "«who has broken away»", "«çıkmış»", tags=["jumla-sifa"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ ثَالِثٌ؛ مَرَقَ مِنَ الدِّينِ: خَرَجَ مِنْهُ كَمَا يَمْرُقُ السَّهْمُ"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("دِينِنَا", "din", "دِينِ", "نَا", "pron-1p", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our religion»", "«dinimizden»", tags=[HJ, ID], punct="،"),
  mazi("وَاسْتَهْوَى", "istahwa", "«and led astray»", "«ve baştan çıkardı»", tags=[AT, "naqis-verbs", "form-x-verbs"], wa=True, hidden="هُوَ", extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  noun_pron("شَبَابَنَا", "shabab", "شَبَابَ", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our young» — the object.", "«gençlerimizi» — mef'ûl.", tags=[MB, ID], punct="،"),
  tok("فَفَتَنَا", "fatana", "verb", [AT, MB], "الْفَاءُ عَاطِفَةٌ، وَفَتَنَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا مَفْعُولٌ بِهِ — فَتَنَهُ: اسْتَمَالَهُ وَأَضَلَّهُ.", "«and seduced us» — nā the object; «he has beguiled us by himself».", "«ve bizi fitneye düşürdü» — nâ mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("فَتَنَ", "fatana", "verb"), seg("نَا", "pron-1p", "pron")]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by himself»", "«kendisiyle»", punct="،"),
  mazi("وَفَرَّقَ", "farraqa", "«and split»", "«ve böldü»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  noun_pron("أَمْرَنَا", "amr", "أَمْرَ", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — فَرَّقَ أَمْرَهُمْ: شَتَّتَ جَمَاعَتَهُمْ.", "«our ranks» — the object; «split our affair».", "«birliğimizi» — mef'ûl.", tags=[MB, ID], punct="،"),
  mazi("وَسَفَّهَ", "saffaha", "«and made light of»", "«ve hafife aldı»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  noun_pron("أَحْلَامَنَا", "hulm", "أَحْلَامَ", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — الْأَحْلَامُ هُنَا: الْعُقُولُ.", "«our minds» — the object; aḥlām here means intellects.", "«akıllarımızı» — mef'ûl; ahlâm burada akıllar.", tags=[MB, ID, JT], punct="،"),
  mazi("وَشَغَلَ", "shaghala", "«and troubled»", "«ve meşgul etti»", tags=[AT], wa=True, hidden="هُوَ"),
  noun_pron("بَالَنَا", "bal-mind", "بَالَ", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — شَغَلَ بَالَهُ: أَقْلَقَهُ.", "«our peace of mind» — the object.", "«huzurumuzu» — mef'ûl.", tags=[MB, ID], punct="."),
])
# ---------------------------------------------------------------- §24 أُسْلُوبُ النَّاقِمِينَ وَالسِّيَاسِيِّينَ (print p. 55)
sen("s3", "«He is a danger to the state: he submits to no order, is bound by no law, honours no great man and holds nothing ancient sacred; he is a revolutionary, and if his evil is not checked it will grow worse; a spark is not to be made light of, however trifling it may be.»",
        "«O devlet için bir tehlikedir: hiçbir düzene boyun eğmez, hiçbir kanunla bağlı değildir, hiçbir büyüğü yüceltmez, hiçbir kadîmi kutsal saymaz; o devrimci bir adamdır; şerri durdurulmazsa büyür; kıvılcım ne kadar önemsiz olursa olsun küçümsenmez.»", [
  tok("وَهُوَ", "huwa", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«and he» — the mubtadaʾ.", "«ve o» — mübtedâ.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("خَطَرٌ", "khatar", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a danger» — the khabar.", "«bir tehlike» — haber."),
  prep("عَلَى", "ala", "«to»", "«için»"),
  majrur("الدَّوْلَةِ", "dawla", "«the state»", "«devlet»", punct="،"),
  la_nafiya(),
  neg_mudari("يَخْضَعُ", "khadaa-submit", "«he submits»", "«boyun eğer»", tags=[HL], hidden="هُوَ", extra=" — وَالْجُمْلَةُ حَالٌ (أَوْ خَبَرٌ ثَانٍ)"),
  li_noun("لِنِظَامٍ", "nizam", "«to any order»", "«bir düzene»", punct="،"),
  *wa_la_mudari("وَلَا يَتَقَيَّدُ", "taqayyada", "«is bound»", "«bağlı değildir»", tags=["form-v-verbs"]),
  bi_noun("بِقَانُونٍ", "qanun", "«by any law»", "«bir kanunla»", punct="،"),
  *wa_la_mudari("وَلَا يُعَظِّمُ", "azzama", "«honours»", "«yüceltir»", tags=["form-ii-verbs"]),
  maful_("عَظِيمًا", "azim", "«any great man»", "«bir büyüğü»", punct="،"),
  *wa_la_mudari("وَلَا يُقَدِّسُ", "qaddasa", "«holds sacred»", "«kutsal sayar»", tags=["form-ii-verbs"]),
  maful_("قَدِيمًا", "qadim", "«anything ancient»", "«bir kadîmi»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ مُبْتَدَأٌ.", "«and he»", "«ve o»", segments=wa_("هُوَ", "huwa", "pron")),
  tok("رَجُلٌ", "rajul", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a man»", "«bir adam»"),
  naat("ثَوْرِيٌّ", "thawri", "«revolutionary»", "«devrimci»", case="raf", tags=["ism-mansub"], punct="،"),
  tok("إِذَا", "idha", "part", ["idha-shartiyya", MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«if»", "«… -sa»"),
  tok("لَمْ", "lam", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mez»"),
  tok("يُكَفَّ", "kaffa", "verb", [LJ, NF, "idha-shartiyya", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ السُّكُونُ الْمُقَدَّرُ، حُرِّكَ بِالْفَتْحِ لِلتَّخَلُّصِ مِنِ الْتِقَاءِ السَّاكِنَيْنِ فِي الْمُضَاعَفِ — فِعْلُ الشَّرْطِ.", "«is checked» — a passive doubled verb in jazm: the fatḥa resolves the two sukūns.", "«durdurulur» — meçhul muzâaf fiil meczûm: iki sâkin yüzünden fetha."),
  noun_pron("شَرُّهُ", "sharr", "شَرُّ", "هُ", "pron-3ms", "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his evil» — the deputy doer.", "«şerri» — nâib-i fâil.", tags=[NF, ID]),
  tok("فَإِنَّهُ", "inna", "part", ["idha-shartiyya", IW], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ إِذَا، وَإِنَّ وَالْهَاءُ اسْمُهَا.", "«it will» — the fāʾ of the answer with inna.", "«o» — cevap fâ'sı ile inne.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  mudari("يَتَفَاقَمُ", "tafaqama", "«grow worse»", "«büyür»", tags=[IW, "form-vi-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ إِنَّ"),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -mez»", segments=wa_("لَا", "la-nafiya", "part")),
  tok("تُسْتَصْغَرُ", "istasghara", "verb", [NF, "la-nafiya", "mudari-marfu", "form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ.", "«is to be made light of» — a passive.", "«küçümsenir» — meçhul."),
  tok("الشَّرَارَةُ", "sharara", "noun", [NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«a spark» — the deputy doer.", "«kıvılcım» — nâib-i fâil."),
  tok("مَهْمَا", "mahma", "pron", [SH, KN], "اسْمُ شَرْطٍ جَازِمٌ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَتْ مُقَدَّمٌ.", "«however» — the conditional noun as kāna's fronted khabar.", "«ne kadar … olursa olsun» — kâne'nin öne alınmış haberi olan şart ismi."),
  tok("كَانَتْ", "kana", "verb", [SH, KN, "hollow-verbs", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«it may be» — the condition; the answer is understood.", "«olursa» — şart; cevabı mahzuf."),
  tok("تَافِهَةً", "tafih", "noun", [KN, "ism-fail"], "خَبَرٌ ثَانٍ لِكَانَتْ (أَوْ حَالٌ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«trifling» — a second khabar of kāna (or a ḥāl).", "«önemsiz» — kâne'nin ikinci haberi (veya hâl).", punct="."),
])
# ---------------------------------------------------------------- §25 مَكْرٌ وَدَهَاءٌ (print pp. 55–56)
sen("s4", "It was speech full of cunning and guile, dyed with a political dye; they knew that the religious side would neither stir the rulers nor rouse them, for it was part of their policy not to interfere in the Jews' religious affairs; and for that reason they mixed the speech with politics.",
        "Bu, hile ve kurnazlıkla dolu, siyasî boyayla boyanmış bir sözdü; biliyorlardı ki dinî taraf yöneticileri ne harekete geçirir ne de kışkırtır; çünkü Yahudilerin dinî işlerine karışmamak siyasetlerindendi; bu yüzden sözü siyasetle karıştırdılar.", [
  tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الْكَلَامُ).", "«and it was» — kāna; its ism is concealed.", "«ve … idi» — kâne; ismi gizli.", segments=wa_("كَانَ", "kana", "verb")),
  tok("كَلَامًا", "kalam", "noun", [KN], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«speech» — kāna's khabar.", "«bir söz» — kâne'nin haberi."),
  naat("مَمْلُوءًا", "mamlu", "«full»", "«dolu»", case="nasb", tags=["ism-maful"]),
  bi_noun("بِالْمَكْرِ", "makr", "«of cunning»", "«hileyle»"),
  atf("وَالدَّهَاءِ", "daha", "«guile»", "«ve kurnazlıkla»", punct="،"),
  naat2("مَصْبُوغًا", "masbugh", "«dyed»", "«boyanmış»", case="nasb", tags=["ism-maful"]),
  bi_noun("بِالصِّبْغَةِ", "sibgha", "«with the dye»", "«boyayla»"),
  naat("السِّيَاسِيَّةِ", "siyasi", "«political»", "«siyasî»", tags=["ism-mansub"], punct="،"),
  kana_pl(),
  khamsa("يَعْرِفُونَ", "arafa", "«knew»", "«biliyorlardı»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  tok("أَنَّ", "anna", "part", [IW, MB], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولِ يَعْرِفُونَ.", "«that» — the clause is the object of «knew».", "«ki» — cümle «biliyorlardı»nın mef'ûlü."),
  tok("الْجَانِبَ", "janib", "noun", [IW], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the side» — anna's ism.", "«taraf» — enne'nin ismi."),
  naat("الدِّينِيَّ", "dini", "«religious»", "«dinî»", case="nasb", tags=["ism-mansub"]),
  la_nafiya(),
  neg_mudari("يُثِيرُ", "athara", "«stirs»", "«harekete geçirir»", tags=[IW, "hollow-verbs", "form-iv-verbs"], hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  maful_("الْحُكَّامَ", "hakim-ruler", "«the rulers»", "«yöneticileri»", tags=[JT]),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«nor»", "«ne de»", segments=wa_("لَا", "la-nafiya", "part")),
  v_pron("يُهِيجُهُمْ", "hayyaja", "يُهِيجُ", "هُمْ", "pron-3mp", "«rouses them»", "«onları kışkırtır»", tags=["la-nafiya", "mudari-marfu", "form-iv-verbs"], punct="،"),
  tok("فَقَدْ", "qad", "part", [AT, "qad-harf"], "الْفَاءُ لِلتَّعْلِيلِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«for [indeed]»", "«çünkü»", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ — وَاسْمُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ، وَخَبَرُهُ الْجَارُّ وَالْمَجْرُورُ مُقَدَّمٌ.", "«it was» — kāna; its ism is the following an-clause, its khabar the fronted phrase.", "«idi» — kâne; ismi sonraki en cümlesi, haberi öne alınmış ibare."),
  prep("مِنْ", "min", "«part of»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ."),
  noun_pron("سِيَاسَتِهِمْ", "siyasa", "سِيَاسَتِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their policy»", "«siyasetlerinden»", tags=[HJ, ID, KN]),
  tok("أَنْ", "an-masdariyya", "part", [AN, KN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ اسْمُ كَانَ مُؤَخَّرٌ.", "«to» — the an-clause is kāna's delayed ism.", "«-mak» — en cümlesi kâne'nin sonraya kalan ismi."),
  la_nafiya(),
  tok("يَتَدَخَّلُوا", "tadakhkhala", "verb", [AN, AK, "la-nafiya", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«interfere» — naṣb by dropping the nūn.", "«karışmak» — nûnun hazfi ile mansub."),
  fi(),
  majrur("أُمُورِ", "amr", "«the affairs [of]»", "«işlerine»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»"),
  naat("الدِّينِيَّةِ", "dini", "«religious»", "«dinî»", tags=["ism-mansub"], punct="،"),
  tok("وَلِذٰلِكَ", "dhalika", "pron", [AT, HJ, TA, "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لِلتَّعْلِيلِ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«and for that reason»", "«ve bu yüzden»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  mazi_pl("خَلَطُوا", "khalata", "«they mixed»", "«karıştırdılar»"),
  maful_("الْكَلَامَ", "kalam", "«the speech»", "«sözü»"),
  bi_noun("بِالسِّيَاسَةِ", "siyasa", "«with politics»", "«siyasetle»", punct="."),
])
# ---------------------------------------------------------------- §26 مُشْكِلَةٌ (print p. 56)
sen("s5", "It was hard for the foreign, polytheist rulers to ascertain the truth of the matter, to know the Jews' aims and the reason for their enmity to the Messiah; they were wholly occupied away from that with administrative affairs.",
        "Yabancı müşrik yöneticilerin işin hakikatini anlaması, Yahudilerin maksatlarını ve Mesîh'e düşmanlıklarının sebebini bilmesi zordu; idarî işlerle bundan alıkoyacak kadar meşguldüler.", [
  tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ — وَاسْمُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«and it was» — kāna; its ism is the an-clause.", "«ve … idi» — kâne; ismi en cümlesi.", segments=wa_("كَانَ", "kana", "verb")),
  prep("مِنَ", "min", "«[a matter] of»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ."),
  majrur("الصَّعْبِ", "sab", "«the hard»", "«zor»", tags=[KN]),
  tok("أَنْ", "an-masdariyya", "part", [AN, KN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ اسْمُ كَانَ مُؤَخَّرٌ.", "«to» — the an-clause is kāna's delayed ism.", "«-ması» — en cümlesi kâne'nin ismi."),
  tok("يَتَحَقَّقَ", "tahaqqaqa", "verb", [AN, "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — وَفَاعِلُهُ الْحُكَّامُ بَعْدَهُ.", "«ascertain» — naṣb by an; the doer follows.", "«anlaması» — en ile mansub; fâili sonra gelir."),
  fail("الْحُكَّامُ", "hakim-ruler", "«the rulers»", "«yöneticiler»", tags=[JT]),
  naat("الْأَجَانِبُ", "ajnabi", "«foreign»", "«yabancı»", case="raf", tags=[JT, MM]),
  tok("الْمُشْرِكُونَ", "mushrik", "noun", [NA, JS, "ism-fail", "form-iv-verbs"], "نَعْتٌ ثَانٍ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«polytheist» — a second naʿt, rafʿ by the wāw.", "«müşrik» — ikinci sıfat, vâv ile merfû."),
  maful_("حَقِيقَةَ", "haqiqa", "«the truth [of]»", "«hakikatini»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("الْأَمْرِ", "amr", "«the matter»", "«işin»", punct="،"),
  tok("وَيَعْرِفُوا", "arafa", "verb", [AT, AN, AK], "الْوَاوُ عَاطِفَةٌ، وَيَعْرِفُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَتَحَقَّقَ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and know» — naṣb by conjunction, the nūn dropped.", "«ve bilmesi» — atıfla mansub, nûn düşmüş.", segments=wa_("يَعْرِفُوا", "arafa", "verb")),
  maful_("أَغْرَاضَ", "gharad", "«the aims [of]»", "«maksatlarını»", tags=[ID, JT], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»", punct="،"),
  atf("وَسَبَبَ", "sabab", "«the reason [for]»", "«ve sebebini»", "nasb", tags=[ID], sign="بِالْفَتْحَةِ، مُضَافٌ"),
  noun_pron("عَدَائِهِمْ", "ada-hostility", "عَدَائِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their enmity»", "«düşmanlıklarının»", tags=[ID]),
  li_noun("لِلْمَسِيحِ", "masih", "«to the Messiah»", "«Mesîh'e»", punct="،"),
  kana_pl(),
  fi(),
  majrur("شُغْلٍ", "shughl", "«an occupation»", "«bir meşguliyette»", tags=[KN]),
  naat("شَاغِلٍ", "shaghil", "«engrossing»", "«meşgul edici»", tags=["ism-fail", "tawkid"]),
  tok("عَنْ", "an", "prep", [HJ], "حَرْفُ جَرٍّ.", "«away from»", "«-den»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«bundan»"),
  bi_noun("بِالْأُمُورِ", "amr", "«with the affairs»", "«işlerle»", tags=[JT]),
  naat("الْإِدَارِيَّةِ", "idari", "«administrative»", "«idarî»", tags=["ism-mansub"], punct="،"),
])
sen("s6", "But the Jews' insistence grew intense and their coming and going went on long, so they wanted to be rid of this case which had become the talk of the town.",
        "Fakat Yahudilerin ısrarı şiddetlendi ve gidip gelmeleri uzadı; bunun üzerine şehrin diline düşmüş olan bu davadan kurtulmak istediler.", [
  tok("وَلٰكِنِ", "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«but» — the lightened lākin; its sukūn turns to kasra before the waṣl.", "«fakat» — muhaffef lâkin; sükûnu vasl öncesi kesreye döndü.", segments=wa_("لٰكِنِ", "lakin", "part")),
  mazi("اشْتَدَّ", "ishtadda", "«grew intense»", "«şiddetlendi»", tags=["doubled-verbs", "form-viii-verbs"], hidden=None),
  fail("إِلْحَاحُ", "ilhah", "«the insistence [of]»", "«ısrarı»", tags=[ID, "form-iv-verbs"], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»", punct="،"),
  mazi("وَطَالَ", "tala-long", "«and went on long»", "«ve uzadı»", tags=[AT, "hollow-verbs"], wa=True, hidden=None),
  noun_pron("تَرَدُّدُهُمْ", "taraddud", "تَرَدُّدُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — مَصْدَرُ تَرَدَّدَ: اخْتَلَفَ ذَهَابًا وَإِيَابًا.", "«their coming and going» — the doer; the maṣdar of taraddada.", "«gidip gelmeleri» — fâil; teraddede'nin masdarı.", tags=[FL, ID, "form-v-verbs"]),
  tok("فَأَرَادُوا", "arada", "verb", [AT, "hollow-verbs", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَأَرَادُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they wanted»", "«bunun üzerine istediler»", segments=[seg("فَ", "fa", "conj"), seg("أَرَادُوا", "arada", "verb")]),
  maful_("التَّخَلُّصَ", "takhallus", "«to be rid»", "«kurtulmayı»", tags=["form-v-verbs"]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  tok("هٰذِهِ", "hadhihi", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("الْقَضِيَّةِ", "qadiyya", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«case» — a badal.", "«davadan» — bedel."),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.", "«which» — the relative, a naʿt.", "«ki» — sıfat olan mevsûl."),
  mazi_ta("أَصْبَحَتْ", "asbaha", "«had become»", "«olmuştu»", tags=[MW, KN, "form-iv-verbs"], extra=" — فِعْلٌ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ؛ وَالْجُمْلَةُ صِلَةٌ"),
  tok("حَدِيثَ", "hadith", "noun", [KN, ID], "خَبَرُ أَصْبَحَتْ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the talk [of]» — aṣbaḥa's khabar.", "«… dedikodusu» — asbaha'nın haberi."),
  mudaf_ilayh("الْبَلَدِ", "balad", "«the town»", "«şehrin»", punct="."),
])

CAND = {
 "ala-overcome": G("ala-overcome", "عَالَ", "ع ي ل", "verb", "to overcome; (passive, ʿīla ṣabruhu) one's patience is exhausted (hollow)", "üstün gelmek; (meçhul, île sabruhu) sabrı tükenmek (ecvef)", 3),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "sabr": G("sabr", "صَبْر", "ص ب ر", "noun", "patience", "sabır", 1),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "fada": G("fada", "فَاضَ", "ف ي ض", "verb", "to overflow (hollow)", "taşmak (ecvef)", 2),
 "kas": G("kas", "كَأْس", "ك أ س", "noun", "a cup (feminine)", "kadeh, kâse (müennes)", 1, plural="كُؤُوس"),
 "ada-hostility": G("ada-hostility", "عَدَاء", "ع د و", "noun", "enmity, hostility", "düşmanlık", 2),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "inad": G("inad", "عِنَاد", "ع ن د", "noun", "obstinacy", "inat", 2),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend (Form IV, hollow)", "istemek (if'âl, ecvef)", 1),
 "takhallus": G("takhallus", "تَخَلُّص", "خ ل ص", "noun", "getting rid (min: of) (the maṣdar of Form V)", "kurtulma (tefa''ul masdarı)", 2),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "rafaa": G("rafaa", "رَفَعَ", "ر ف ع", "verb", "to raise; to bring (a case) before", "yükseltmek; (davayı) götürmek", 1),
 "qadiyya": G("qadiyya", "قَضِيَّة", "ق ض ي", "noun", "a case, an issue", "dava, mesele", 1, plural="قَضَايَا"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "hakim-ruler": G("hakim-ruler", "حَاكِم", "ح ك م", "noun", "a ruler, a governor (an active participle)", "yöneten, vali, hâkim (ism-i fâil)", 1, plural="حُكَّام"),
 "rumi": G("rumi", "الرُّومِيّ", "ر و م", "noun", "Roman, Byzantine (a nisba)", "Rum, Romalı (nisbet)", 2),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "a man", "adam", 1, plural="رِجَال"),
 "thair": G("thair", "ثَائِر", "ث و ر", "noun", "rebellious, a rebel (an active participle)", "âsi, isyancı (ism-i fâil)", 2),
 "fawdawi": G("fawdawi", "فَوْضَوِيّ", "ف و ض", "noun", "anarchic, an anarchist (a nisba)", "anarşist (nisbet)", 3),
 "maraqa": G("maraqa", "مَرَقَ", "م ر ق", "verb", "to break away (min: from), to pass through like an arrow", "(dinden) çıkmak, ok gibi delip geçmek", 3),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "istahwa": G("istahwa", "اِسْتَهْوَى", "ه و ي", "verb", "to seduce, to lead astray (Form X, defective)", "baştan çıkarmak, kendine çekmek (istif'âl, nâkıs)", 3),
 "shabab": G("shabab", "شَبَاب", "ش ب ب", "noun", "youth; the young", "gençlik; gençler", 1),
 "fatana": G("fatana", "فَتَنَ", "ف ت ن", "verb", "to put to trial; to beguile, to seduce", "fitneye düşürmek; baştan çıkarmak", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "farraqa": G("farraqa", "فَرَّقَ", "ف ر ق", "verb", "to distinguish; to split, to scatter (Form II)", "ayırmak; bölmek, dağıtmak (tef'îl)", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1, plural="أُمُور"),
 "saffaha": G("saffaha", "سَفَّهَ", "س ف ه", "verb", "to make light of, to deem foolish (Form II)", "hafife almak, akılsız saymak (tef'îl)", 3),
 "hulm": G("hulm", "حُلْم", "ح ل م", "noun", "a dream; (pl. aḥlām) intellects", "rüya; (ç. ahlâm) akıllar", 1, plural="أَحْلَام"),
 "shaghala": G("shaghala", "شَغَلَ", "ش غ ل", "verb", "to occupy, to trouble", "meşgul etmek, kaygılandırmak", 1),
 "bal-mind": G("bal-mind", "بَال", "ب و ل", "noun", "the mind, the state of mind", "zihin, gönül, hâl", 2),
 "huwa": G("huwa", "هُوَ", None, "pron", "he / it", "o", 1),
 "khatar": G("khatar", "خَطَر", "خ ط ر", "noun", "a danger", "tehlike", 1, plural="أَخْطَار"),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "dawla": G("dawla", "دَوْلَة", "د و ل", "noun", "a state; dominion", "devlet; hâkimiyet", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "khadaa-submit": G("khadaa-submit", "خَضَعَ", "خ ض ع", "verb", "to submit, to bow (li: to)", "boyun eğmek (li ile)", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "nizam": G("nizam", "نِظَام", "ن ظ م", "noun", "an order, a system", "düzen, nizam", 1),
 "taqayyada": G("taqayyada", "تَقَيَّدَ", "ق ي د", "verb", "to be bound (bi: by) (Form V)", "bağlı olmak, kayıtlı olmak (tefa''ul)", 2),
 "qanun": G("qanun", "قَانُون", "ق ن ن", "noun", "a law", "kanun", 1, plural="قَوَانِين"),
 "azzama": G("azzama", "عَظَّمَ", "ع ظ م", "verb", "to magnify, to honour (Form II)", "yüceltmek, büyük tutmak (tef'îl)", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great", "büyük, azîm", 1),
 "qaddasa": G("qaddasa", "قَدَّسَ", "ق د س", "verb", "to hold sacred, to sanctify (Form II)", "kutsal saymak, takdis etmek (tef'îl)", 2),
 "qadim": G("qadim", "قَدِيم", "ق د م", "noun", "ancient, old", "kadîm, eski", 1),
 "thawri": G("thawri", "ثَوْرِيّ", "ث و ر", "noun", "revolutionary (a nisba)", "devrimci (nisbet)", 2),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ırsa", 1),
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "kaffa": G("kaffa", "كَفَّ", "ك ف ف", "verb", "to hold back, to check (doubled)", "durdurmak, alıkoymak (muzâaf)", 2),
 "sharr": G("sharr", "شَرّ", "ش ر ر", "noun", "evil, harm", "şer, kötülük", 1),
 "tafaqama": G("tafaqama", "تَفَاقَمَ", "ف ق م", "verb", "to grow worse, to aggravate (Form VI)", "büyümek, ağırlaşmak (tefâul)", 3),
 "istasghara": G("istasghara", "اِسْتَصْغَرَ", "ص غ ر", "verb", "to belittle, to deem small (Form X)", "küçümsemek (istif'âl)", 2),
 "sharara": G("sharara", "شَرَارَة", "ش ر ر", "noun", "a spark", "kıvılcım", 2),
 "mahma": G("mahma", "مَهْمَا", None, "pron", "whatever (a jussive conditional noun)", "her ne … olursa olsun (cezm eden şart ismi)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "tafih": G("tafih", "تَافِه", "ت ف ه", "noun", "trifling, insignificant (an active participle)", "önemsiz, değersiz (ism-i fâil)", 2),
 "kalam": G("kalam", "كَلَام", "ك ل م", "noun", "speech", "söz, kelâm", 1),
 "mamlu": G("mamlu", "مَمْلُوء", "م ل أ", "noun", "full, filled (a passive participle)", "dolu (ism-i mef'ûl)", 2),
 "makr": G("makr", "مَكْر", "م ك ر", "noun", "cunning, scheming", "hile, tuzak", 2),
 "daha": G("daha", "دَهَاء", "د ه ي", "noun", "guile, shrewdness", "kurnazlık, dehâ", 3),
 "masbugh": G("masbugh", "مَصْبُوغ", "ص ب غ", "noun", "dyed (a passive participle)", "boyanmış (ism-i mef'ûl)", 2),
 "sibgha": G("sibgha", "صِبْغَة", "ص ب غ", "noun", "a dye, a colouring", "boya", 2),
 "siyasi": G("siyasi", "سِيَاسِيّ", "س و س", "noun", "political; a politician (a nisba)", "siyasî; siyasetçi (nisbet)", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, to recognize", "bilmek, tanımak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "janib": G("janib", "جَانِب", "ج ن ب", "noun", "a side", "taraf, yan", 1, plural="جَوَانِب"),
 "dini": G("dini", "دِينِيّ", "د ي ن", "noun", "religious (a nisba)", "dinî (nisbet)", 1),
 "athara": G("athara", "أَثَارَ", "ث و ر", "verb", "to stir up, to provoke (Form IV, hollow)", "harekete geçirmek, kışkırtmak (if'âl, ecvef)", 2),
 "hayyaja": G("hayyaja", "هَيَّجَ", "ه ي ج", "verb", "to rouse, to excite (Form II)", "kışkırtmak, galeyana getirmek (tef'îl)", 3),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "siyasa": G("siyasa", "سِيَاسَة", "س و س", "noun", "policy, politics", "siyaset", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "tadakhkhala": G("tadakhkhala", "تَدَخَّلَ", "د خ ل", "verb", "to interfere (fī: in) (Form V)", "karışmak, müdahale etmek (tefa''ul)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "khalata": G("khalata", "خَلَطَ", "خ ل ط", "verb", "to mix", "karıştırmak", 1),
 "sab": G("sab", "صَعْب", "ص ع ب", "noun", "hard, difficult", "zor", 1),
 "tahaqqaqa": G("tahaqqaqa", "تَحَقَّقَ", "ح ق ق", "verb", "to ascertain; to come true (Form V)", "anlamak, tahkik etmek; gerçekleşmek (tefa''ul)", 2),
 "ajnabi": G("ajnabi", "أَجْنَبِيّ", "ج ن ب", "noun", "foreign, a foreigner", "yabancı", 1, plural="أَجَانِب"),
 "mushrik": G("mushrik", "مُشْرِك", "ش ر ك", "noun", "a polytheist (an active participle of Form IV)", "müşrik (if'âl ism-i fâili)", 1, plural="مُشْرِكُونَ"),
 "haqiqa": G("haqiqa", "حَقِيقَة", "ح ق ق", "noun", "reality, truth", "hakikat", 1),
 "gharad": G("gharad", "غَرَض", "غ ر ض", "noun", "an aim, a purpose", "maksat, amaç", 1, plural="أَغْرَاض"),
 "sabab": G("sabab", "سَبَب", "س ب ب", "noun", "a cause, a means", "sebep", 1, plural="أَسْبَاب"),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "shughl": G("shughl", "شُغْل", "ش غ ل", "noun", "occupation, business", "meşguliyet, iş", 2),
 "shaghil": G("shaghil", "شَاغِل", "ش غ ل", "noun", "engrossing, occupying (an active participle)", "meşgul edici (ism-i fâil)", 2),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "idari": G("idari", "إِدَارِيّ", "د و ر", "noun", "administrative (a nisba)", "idarî (nisbet)", 2),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but (the lightened lākin)", "fakat (muhaffef lâkin)", 1),
 "ishtadda": G("ishtadda", "اِشْتَدَّ", "ش د د", "verb", "to grow intense (Form VIII, doubled)", "şiddetlenmek (iftiâl, muzâaf)", 2),
 "ilhah": G("ilhah", "إِلْحَاح", "ل ح ح", "noun", "insistence (the maṣdar of Form IV)", "ısrar (if'âl masdarı)", 2),
 "tala-long": G("tala-long", "طَالَ", "ط و ل", "verb", "to be long, to last long (hollow)", "uzamak, uzun sürmek (ecvef)", 1),
 "taraddud": G("taraddud", "تَرَدُّد", "ر د د", "noun", "coming and going; hesitation (the maṣdar of Form V)", "gidip gelme; tereddüt (tefa''ul masdarı)", 2),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu (müennes)", 1),
 "allati": G("allati", "الَّتِي", None, "pron", "which, who (f.)", "ki o, -an (müennes)", 1),
 "asbaha": G("asbaha", "أَصْبَحَ", "ص ب ح", "verb", "to become (a sister of kāna, Form IV)", "olmak, hâline gelmek (kâne'nin kardeşi, if'âl)", 1),
 "hadith": G("hadith", "حَدِيث", "ح د ث", "noun", "talk, speech; a ḥadīth", "söz, konuşma; hadis", 1, plural="أَحَادِيث"),
 "balad": G("balad", "بَلَد", "ب ل د", "noun", "a town, a country", "şehir, belde", 1, plural="بِلَاد"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ala-overcome", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "عَال", "عِل", "عِيل", "عِل", "عِل", "عِل", "عَيْل", "عَائِل", None, "عِيلَ", "يُعَالُ", "عَالَهُ الْأَمْرُ يَعِيلُهُ: غَلَبَهُ؛ وَعِيلَ صَبْرُهُ: غُلِبَ وَنَفِدَ — أَجْوَفُ يَائِيٌّ."))
put_morph(mo, "fada", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "فَاض", "فِض", "فِيض", "فِض", "فِض", "فِض", "فَيْض / فَيَضَان", "فَائِض", None, None, None, "فَاضَ الْمَاءُ يَفِيضُ: كَثُرَ حَتَّى سَالَ — أَجْوَفُ يَائِيٌّ."))
put_morph(mo, "maraqa", _sg.sound1("nasara", "مَرَق", "مْرُق", "اُمْرُق", "مُرُوق", "مَارِق", None, None, None, "مَرَقَ السَّهْمُ مِنَ الرَّمِيَّةِ يَمْرُقُ: خَرَجَ مِنَ الْجَانِبِ الْآخَرِ؛ وَمَرَقَ مِنَ الدِّينِ: خَرَجَ مِنْهُ."))
put_morph(mo, "istahwa", _sg.derived_naqis(_sg.B10, _sg.W10, "َ", "اِسْتَهْوَ", "سْتَهْو", "i", "اِسْتَهْو", "اِسْتِهْوَاء", "مُسْتَهْوٍ (الْمُسْتَهْوِي)", "مُسْتَهْوًى", "اُسْتُهْوِيَ", "يُسْتَهْوَى", "اِسْتَهْوَاهُ: اسْتَمَالَهُ وَأَضَلَّهُ."))
put_morph(mo, "fatana", _sg.sound1("daraba", "فَتَن", "فْتِن", "اِفْتِن", "فِتْنَة / فَتْن", "فَاتِن", "مَفْتُون", "فُتِنَ", "يُفْتَنُ", "فَتَنَهُ يَفْتِنُهُ: امْتَحَنَهُ؛ وَفَتَنَهُ: اسْتَمَالَهُ وَأَضَلَّهُ."))
put_morph(mo, "saffaha", _sg.derived(_sg.B2, _sg.W2, "ُ", "سَفَّه", "سَفِّه", "سَفِّه", "تَسْفِيه", "مُسَفِّه", "مُسَفَّه", "سُفِّهَ", "يُسَفَّهُ", "سَفَّهَهُ: نَسَبَهُ إِلَى السَّفَهِ؛ وَسَفَّهَ رَأْيَهُ: اسْتَخَفَّ بِهِ."))
put_morph(mo, "shaghala", _sg.sound1("fataha", "شَغَل", "شْغَل", "اِشْغَل", "شُغْل / شَغْل", "شَاغِل", "مَشْغُول", "شُغِلَ", "يُشْغَلُ", "شَغَلَهُ الْأَمْرُ يَشْغَلُهُ: أَلْهَاهُ وَصَرَفَهُ."))
put_morph(mo, "taqayyada", _sg.derived(_sg.B5, _sg.W5, "َ", "تَقَيَّد", "تَقَيَّد", "تَقَيَّد", "تَقَيُّد", "مُتَقَيِّد", None, None, None, "تَقَيَّدَ بِالشَّيْءِ: الْتَزَمَهُ."))
put_morph(mo, "azzama", _sg.derived(_sg.B2, _sg.W2, "ُ", "عَظَّم", "عَظِّم", "عَظِّم", "تَعْظِيم", "مُعَظِّم", "مُعَظَّم", "عُظِّمَ", "يُعَظَّمُ", "عَظَّمَهُ: فَخَّمَهُ وَكَبَّرَهُ."))
put_morph(mo, "qaddasa", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَدَّس", "قَدِّس", "قَدِّس", "تَقْدِيس", "مُقَدِّس", "مُقَدَّس", "قُدِّسَ", "يُقَدَّسُ", "قَدَّسَهُ: طَهَّرَهُ وَنَزَّهَهُ وَعَظَّمَهُ."))
put_morph(mo, "kaffa", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "كَفّ", "كَافّ", _sg.mazi14("كَفّ", "كَفَف"), _sg.mudari14("َ", "كُفّ", "كْفُف"), ["كُفَّ", "كُفَّا", "كُفُّوا", "كُفِّي", "كُفَّا", "اُكْفُفْنَ"], "يَكُفَّ", "يَكُفَّ", "تَكُفَّ", "مَكْفُوف", "كُفَّ", "يُكَفُّ", "كَفَّهُ عَنِ الشَّيْءِ يَكُفُّهُ: مَنَعَهُ وَصَرَفَهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَكُفَّ."))
put_morph(mo, "tafaqama", _sg.derived(_sg.B6, _sg.W6, "َ", "تَفَاقَم", "تَفَاقَم", "تَفَاقَم", "تَفَاقُم", "مُتَفَاقِم", None, None, None, "تَفَاقَمَ الْأَمْرُ: عَظُمَ وَاشْتَدَّ."))
put_morph(mo, "athara", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَثَار", "أَثَر", "ثِير", "ثِر", "أَثِر", "أَثِر", "إِثَارَة", "مُثِير", "مُثَار", "أُثِيرَ", "يُثَارُ", "أَثَارَ الشَّيْءَ: هَيَّجَهُ وَحَرَّكَهُ — أَجْوَفُ وَاوِيٌّ (ث و ر)."))
put_morph(mo, "hayyaja", _sg.derived(_sg.B2, _sg.W2, "ُ", "هَيَّج", "هَيِّج", "هَيِّج", "تَهْيِيج", "مُهَيِّج", "مُهَيَّج", "هُيِّجَ", "يُهَيَّجُ", "هَيَّجَهُ: أَثَارَهُ وَأَغْضَبَهُ."))
put_morph(mo, "tadakhkhala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَدَخَّل", "تَدَخَّل", "تَدَخَّل", "تَدَخُّل", "مُتَدَخِّل", None, None, None, "تَدَخَّلَ فِي الْأَمْرِ: أَدْخَلَ نَفْسَهُ فِيهِ."))
put_morph(mo, "khalata", _sg.sound1("daraba", "خَلَط", "خْلِط", "اِخْلِط", "خَلْط", "خَالِط", "مَخْلُوط", "خُلِطَ", "يُخْلَطُ", "خَلَطَ الشَّيْءَ بِالشَّيْءِ يَخْلِطُهُ: مَزَجَهُ بِهِ."))
put_morph(mo, "ishtadda", _sg.entry(_sg.B8 + " — مُضَاعَفٌ", _sg.W8, "اِشْتِدَاد", "مُشْتَدّ", _sg.mazi14("اِشْتَدّ", "اِشْتَدَد"), _sg.mudari14("َ", "شْتَدّ", "شْتَدِد"), ["اِشْتَدَّ", "اِشْتَدَّا", "اِشْتَدُّوا", "اِشْتَدِّي", "اِشْتَدَّا", "اِشْتَدِدْنَ"], "يَشْتَدَّ", "يَشْتَدَّ", "تَشْتَدَّ", None, None, None, "اِشْتَدَّ الْأَمْرُ: قَوِيَ وَصَعُبَ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَشْتَدَّ."))
put_morph(mo, "tala-long", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "طَال", "طُل", "طُول", "طُل", "طُل", "طُل", "طُول", "طَائِل", None, None, None, "طَالَ الشَّيْءُ يَطُولُ: امْتَدَّ وَدَامَ — أَجْوَفُ وَاوِيٌّ؛ لَمْ يَطُلْ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch38 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 38 (print pp. 55–56; ʿĪsā §23–26): the Jews' patience exhausted — the case before the Roman governor, «a rebellious, anarchic man» (s1–s2); the politician's style — «a danger to the state», «a spark is not to be made light of» (s3); speech dyed with politics, since the rulers did not interfere in the Jews' religion (s4); the foreign rulers cannot see the truth; the case becomes the talk of the town (s5–s6)."
ADD_TR = " Otuz sekizinci bölüm (baskı s. 55–56; Îsâ §23–26): Yahudilerin sabrı tükenir — dava Roma valisinin önünde, «âsi, anarşist bir adam» (s1–s2); siyasetçi üslûbu — «devlet için tehlike», «kıvılcım küçümsenmez» (s3); yöneticiler Yahudilerin dinine karışmadığından siyasetle boyanmış söz (s4); yabancı yöneticiler hakikati göremez; dava şehrin dedikodusu olur (s5–s6)."
write_out(38, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §23–26", GLOSS_ADD, notes=(), related=())
report(38, S, GLOSS_ADD, ())
