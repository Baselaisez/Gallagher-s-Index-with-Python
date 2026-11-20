# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 9: «سَفِينَةُ نُوحٍ» §15 حُجَّةُ الْأَغْنِيَاءِ (what Nūḥ calls to is neither true nor good — why? we have tried: we are first in every good; the people follow us; good never misses us — «had it been good they would not have preceded us to it», 46:11) and §16 دَعْوَةُ نُوحٍ (Nūḥ calls and counsels: 71:2–4; God had withheld the rain, tillage and offspring grew scarce; «if you believe, God is pleased with you and this punishment departs»; «do you not know God? these are His signs around you»; who created the heavens, the moon a light, the sun a lamp, the earth a carpet? — but the people of Nūḥ did not reason, did not believe; they put their fingers in their ears; how can one understand who does not hear?). Print pp. 23–25.
python3 tools/authoring/author_qisas2_ch9.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: حُجَّةُ الْأَغْنِيَاءِ — دَعْوَةُ نُوحٍ", "en": "The ship of Nūḥ: the argument of the rich — the call of Nūḥ", "tr": "Nûh'un gemisi: zenginlerin delili — Nûh'un daveti"}
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
    return tok(full, lex, "verb", [AT, "la-nafiya", "mudari-marfu"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ، وَ" + full[4:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", "«and … not» + " + en, "«ve … -mez» + " + tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part"), seg(full[4:], lex, "verb")])

def wa_kana(ism_note=""):
    return tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ" + ism_note + ".", "«and … was»", "«ve … idi»", segments=wa_("كَانَ", "kana", "verb"))
def ism_kana(full, lex, en, tr, punct=None, tags=(), ar="اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ."): return tok(full, lex, "noun", [KN] + list(tags), ar, en + " — kāna's ism.", tr + " — kâne'nin ismi.", punct=punct)
def khabar_kana(full, lex, en, tr, punct=None, tags=(), ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ."): return tok(full, lex, "noun", [KN] + list(tags), ar, en + " — kāna's khabar.", tr + " — kâne'nin haberi.", punct=punct)
def js_khabar(full, lex, stem, en, tr, note, punct=None, tags=(), role="خَبَرُ كَانُوا"):
    return tok(full, lex, "noun", [KN, JS, ID] + list(tags), role + " مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ" + note + ".", en + " — a sound plural in naṣb, its nūn dropped for the annexation.", tr + " — cemi müzekker sâlim, nûnu izâfet için düşmüş.", punct=punct)

def tafdil_hum(full, lex, stem, en, tr, punct=None, wa=True, first=False):
    return tok(full, lex, "noun", ([AT] if wa else []) + [KN, ID, "ism-tafdil"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + stem + (" خَبَرُ كَانَ مَنْصُوبٌ" if first else " مَعْطُوفٌ مَنْصُوبٌ") + " بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — اسْمُ تَفْضِيلٍ.", ("«and» + " if wa else "") + en + " — an elative annexed to the pronoun.", ("«ve» + " if wa else "") + tr + " — zamire muzâf ism-i tafdîl.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "noun"), seg("هُمْ", "pron-3mp", "pron")])
def tamyiz(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "noun", ["tamyiz"] + list(tags), "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — a tamyīz.", tr + " — temyiz.", punct=punct)

def qatalu_hu(full, lex, en, tr, punct=None):
    stem = full[4:len(full)-2]
    return tok(full, lex, "verb", [AT, MB, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ، وَ" + stem + "ا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and they did not» + " + en, "«ve onu» + " + tr, punct=punct, segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part"), seg(stem, lex, "verb"), seg("هُ", "pron-3ms", "pron")])

def fa_qalu(punct=":"):
    return tok("فَقَالُوا", "qala", "verb", [AT, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَقَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they said»", "«bunun üzerine dediler»", segments=[seg("فَ", "fa", "conj"), seg("قَالُوا", "qala", "verb")], punct=punct)
def wa_qalu(punct=":"):
    return mazi_pl("وَقَالُوا", "qala", "«and they said»", "«ve dediler»", tags=[AT, "hollow-verbs"], wa=True, punct=punct)

# ---------------------------------------------------------------- § the chapter's own small helpers
def allah_maful(full="اللهَ", punct=None):
    return tok(full, "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object, in naṣb.", "«Allah» — lafza-i celâl, mef'ûl, mansub.", punct=punct)
def allah_mi(punct=None): return tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah'ın» — muzâfun ileyh.", punct=punct)
def group_pron(full, lex, stem, pron_form, pron_lex, en, tr, ar_tail, punct=None, tags=(), wa=False):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ""
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if wa else []) + [AK, "mudari-marfu", MB] + list(tags), pre + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + ar_tail + ".", ("«and» + " if wa else "") + en + " — a muḍāriʿ of the five; the attached pronoun is its object.", ("«ve» + " if wa else "") + tr + " — beş fiilden muzâri; bitişik zamir mef'ûl.", punct=punct, segments=segs)
def abahum(role_ar, en, tr, tags=(), punct=None):
    return noun_pron("آبَاءَهُمْ", "ab", "آبَاءَ", "هُمْ", "pron-3mp", role_ar + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ أَبٍ.", en, tr, tags=[MB, ID, JT] + list(tags), punct=punct)
def yarawnahum(punct=None):
    return tok("يَرَوْنَهُمْ", "raa", "verb", [KN, AK, "mudari-marfu", MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ: يَرَى + ونَ)، وَالْوَاوُ فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«they saw them» — the defective muḍāriʿ before the group's wāw (yarā + ūna → yarawna); the pronoun is the first object; the clause is kāna's khabar.", "«onları görürlerdi» — cemaat vâvından önce nâkıs muzâri (yerâ + ûne → yerevne); zamir birinci mef'ûl; cümle kâne'nin haberi.", punct=punct, segments=[seg("يَرَوْنَ", "raa", "verb"), seg("هُمْ", "pron-3mp", "pron")])
def indaha(punct=None): return noun_pron("عِنْدَهَا", "inda", "عِنْدَ", "هَا", "pron-3fs", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«by them» — a place adverbial, annexed to the pronoun.", "«onların yanında» — mekân zarfı, zamire muzâf.", tags=[MF, ID], punct=punct)
def saru(full="وَصَارُوا", wa=True):
    return tok(full, "sara", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "صَارُوا فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ اسْمُهَا.", ("«and» + " if wa else "") + "«they came to» — ṣāra, a sister of kāna; the wāw is its ism.", ("«ve» + " if wa else "") + "«… oldular» — kâne'nin kız kardeşi sâra; vâv ismi.", segments=(wa_("صَارُوا", "sara", "verb") if wa else None))
def idol(full, lex, en, tr, punct=None, mamnu=False):
    return tok(full, lex, "propn", [MK] + ([MM] if mamnu else []), "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ صَنَمٍ" + ("، عَلَمٌ عَلَى وَزْنِ الْفِعْلِ مَمْنُوعٌ مِنَ الصَّرْفِ" if mamnu else "") + ".", en + " — the khabar; the name of an idol" + (", a diptote on a verb's pattern" if mamnu else "") + ".", tr + " — haber; bir put adı" + (", fiil vezninde gayr-i munsarif" if mamnu else "") + ".", punct=punct)
def wa_ishara(full, lex, en, tr):
    return tok(full, lex, "pron", [AT, "asma-al-ishara", MK], "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and» + " + en + " — a demonstrative, built; the mubtada.", "«ve» + " + tr + " — ism-i işâret; mübtedâ.", segments=wa_(full[2:], lex, "pron"))
def a_li_hadha(verb_ar):
    return tok("أَلِهٰذَا", "hadha", "pron", [IS, HJ, "asma-al-ishara"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَاسْمُ الْإِشَارَةِ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ" + verb_ar + ".", "«is it for this [that]» — the denying question's hamza + the lām of cause + the demonstrative.", "«bunun için mi» — inkârî istifham hemzesi + ta'lil lâmı + ism-i işâret.", segments=[seg("أَ", "a-istifham", "part"), seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")])
def billah(punct=None): return tok("بِاللهِ", "allah", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«in God» — bi + the name of God.", "«Allah'a» — bi + lafza-i celâl.", punct=punct, segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")])
def inna_hadha_zulm(punct="!"):
    return [inna(),
            tok("هٰذَا", "hadha", "pron", [IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«this» — the demonstrative; inna's ism.", "«bu» — ism-i işâret; inne'nin ismi."),
            tok("لَظُلْمٌ", "zulm", "noun", [IW], "اللَّامُ الْمُزَحْلَقَةُ، وَظُلْمٌ خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«[is] a wrong» — the slid lām + inna's khabar.", "«bir zulümdür» — müzahlaka lâm + inne'nin haberi.", segments=[seg("لَ", "la-ibtida", "part"), seg("ظُلْمٌ", "zulm", "noun")]),
            naat("عَظِيمٌ", "azim", "«great»", "«büyük»", case="raf", punct=punct)]
def lakinna_nas_ma(full_verb, lex, en, tr, punct, tags=()):
    return [tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kız kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
            ism_inna("النَّاسَ", "nas", "«the people»", "«insanlar»", part="لٰكِنَّ"),
            tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
            tok(full_verb, lex, "verb", [IW, "la-nafiya"] + list(tags), "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", en + " — a māḍī on the group's wāw; the clause is lākinna's khabar.", tr + " — cemaat vâvı üzere mâzî; cümle lâkinne'nin haberi.", punct=punct)]

# ---------------------------------------------------------------- § the small helpers shared with chapter 5
MH = "maful-fih"; IST = "istithna"
def idha(full="إِذَا", wa=False, punct=None):
    return tok(full, "idha", "part", ["idha-shartiyya"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", ("«and» + " if wa else "") + "«when» — the conditional time-adverb, built.", ("«ve» + " if wa else "") + "«-dığı zaman» — şart mânâlı zaman zarfı, mebnî.", punct=punct, segments=(wa_("إِذَا", "idha", "part") if wa else None))
def arada_allah(full="وَأَرَادَ", wa=True, fa=False):
    c = "فَ" if fa else ("وَ" if wa else "")
    body = full[2:] if c else full
    pre = {"فَ": "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَ", "وَ": "الْوَاوُ عَاطِفَةٌ، وَ", "": ""}[c]
    return [tok(full, "arada", "verb", ([AT] if c else []) + ["hollow-verbs", "form-iv-verbs"], pre + body + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ الْإِفْعَالِ (أَرَادَ يُرِيدُ).",
                ({"فَ": "«so» + ", "وَ": "«and» + ", "": ""}[c]) + "«willed» — a māḍī of Form IV, hollow.", ({"فَ": "«bunun üzerine» + ", "وَ": "«ve» + ", "": ""}[c]) + "«diledi» — if'âl bâbından ecvef mâzî.",
                segments=([seg(c, "fa" if c == "فَ" else "wa", "conj"), seg(body, "arada", "verb")] if c else None)),
            allah_fail()]
def an_yursila(full="يُرْسِلَ", obj_of="فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِأَرَادَ"):
    return [an_nasb(obj_of, "«to»", "«… -mesini»"),
            tok(full, "arsala", "verb", [AN, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«send» — naṣb by an; the doer (God) is concealed.", "«göndermesini» — en ile mansub; fâil gizli (O).")]
def yukallimuhum(wa=False, punct=None, role=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ"):
    full = "وَيُكَلِّمُهُمْ" if wa else "يُكَلِّمُهُمْ"
    return tok(full, "kallama", "verb", ([AT] if wa else []) + ["mudari-marfu", MB, "form-ii-verbs", NA], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "يُكَلِّمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ" + role + ".",
               ("«and» + " if wa else "") + "«who speaks to them» — the muḍāriʿ clause is a ṣifa of the indefinite noun before it.", ("«ve» + " if wa else "") + "«onlarla konuşan» — muzâri cümlesi, önceki nekre ismin sıfatı.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("يُكَلِّمُ", "kallama", "verb"), seg("هُمْ", "pron-3mp", "pron")])
def wa_yansah(punct="."):
    return [mudari_wa("وَيَنْصَحُ", "nasaha", "«and counsels»", "«ve öğüt verir»", tags=[NA], extra=" — مَعْطُوفٌ عَلَى جُمْلَةِ الصِّفَةِ"),
            li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«them» — the counselled, after li.", "«onlara» — li'den sonra.", punct=punct)]
def inna_allah_la(verb, lex, en, tr, tags=()):
    return [inna(), allah_ism(), la_nafiya(),
            tok(verb, lex, "verb", [IW, "la-nafiya", "mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", en + " — the verbal clause is inna's khabar.", tr + " — fiil cümlesi inne'nin haberi.")]
def wahidan_wahidan(punct):
    return [maful_("وَاحِدًا", "wahid", "«one»", "«birer»"),
            tok("وَاحِدًا", "wahid", "noun", ["tawkid"], "تَوْكِيدٌ لَفْظِيٌّ مَنْصُوبٌ بِالْفَتْحَةِ — التَّكْرَارُ لِلتَّفْصِيلِ: وَاحِدًا بَعْدَ وَاحِدٍ.", "«by one» — the repeated word: one by one.", "«birer» — tekrar: tek tek.", punct=punct)]
def inna_muluk_la(verb, lex, en, tr, tags=()):
    return [inna(), ism_inna("الْمُلُوكَ", "malik-king", "«the kings»", "«krallar»", tags=[JT]), la_nafiya(),
            khamsa(verb, lex, en, tr, tags=[IW, "la-nafiya"] + list(tags), extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ")]
def kull_ahad(case, punct=None, role=""):
    C = {"nasb": ("مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", [MB, ID]), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", [HJ, ID]), "raf": ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", [FL, ID])}[case]
    return [tok("كُلَّ" if case == "nasb" else ("كُلِّ" if case == "jarr" else "كُلُّ"), "kull", "noun", C[1], C[0] + "، مُضَافٌ" + role + ".", "«every» — annexed.", "«her» — muzâf."),
            mudaf_ilayh("أَحَدٍ", "ahad", "«one»", "«bir(i)»", punct=punct)]
def ifal_kadha(punct, wa=False):
    return [tok("افْعَلْ", "faala", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ — وَهَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«do» — an imperative, built on sukūn; the doer «you» is concealed.", "«yap» — sükûn üzere mebnî emir; fâil gizli (sen)."),
            tok("كَذَا", "kadha", "part", [MB], "كِنَايَةٌ عَنِ الْفِعْلِ، فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«such-and-such» — stands for the thing to do; the object.", "«şöyle» — yapılacak şeyin yerini tutar; mef'ûl.", punct=punct)]
def yaqul_lahu(full, pl=False):
    stem = full[2:] if full.startswith("وَ") else full
    if pl: v = khamsa(full, "qala", "«saying»", "«diyerek»", tags=["hollow-verbs", HL], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ")
    else: v = tok(full, "qala", "verb", ["mudari-marfu", "hollow-verbs", HL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«saying» — the clause is a ḥāl.", "«diyerek» — cümle hâl.")
    return [v, li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»")]
def pron_mubtada(full, lex, en, tr, wa=False, punct=None):
    return tok(full, lex, "pron", ([AT] if wa else []) + [MK], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + (full[2:] if wa else full) + " ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", ("«and» + " if wa else "") + en + " — a detached pronoun; the mubtadaʾ.", ("«ve» + " if wa else "") + tr + " — munfasıl zamir; mübtedâ.", punct=punct, segments=(wa_(full[2:], lex, "pron") if wa else None))
def khabar(full, lex, en, tr, punct=None, tags=(), extra=""):
    return tok(full, lex, "noun", [MK] + list(tags), "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ" + extra + ".", en + " — the khabar.", tr + " — haber.", punct=punct)
def idha_kana_rasul(khabar_form, lex, en, tr):
    return [idha("وَإِذَا", wa=True), kana("كَانَ", wa=False), ism_kana("الرَّسُولُ", "rasul", "«the messenger»", "«elçi»"),
            khabar_kana(khabar_form, lex, en, tr)]
def qala_nas(punct=":"):
    return [tok("قَالَ", "qala", "verb", ["hollow-verbs", MB, "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — جَوَابُ إِذَا، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«[then] say» — the answer of idhā; what is said is its object.", "«derler» — izâ'nın cevabı; söylenen söz mef'ûl."), nas_fail(punct=punct)]
def qala_jawab(punct=None):
    return tok("قَالَ", "qala", "verb", ["hollow-verbs", MB, "idha-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جَوَابُ إِذَا، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«[then] he says» — the answer of idhā; the doer is the messenger.", "«der» — izâ'nın cevabı; fâil gizli (elçi).", punct=punct)
def mudari1(full, lex, en, tr, hidden, punct=None, tags=(), wa=False, fa=False, extra=""):
    c = "فَ" if fa else ("وَ" if wa else "")
    body = full[2:] if c else full
    pre = {"فَ": "الْفَاءُ عَاطِفَةٌ، وَ", "وَ": "الْوَاوُ عَاطِفَةٌ، وَ", "": ""}[c]
    return tok(full, lex, "verb", ([AT] if c else []) + ["mudari-marfu"] + list(tags), pre + body + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: " + hidden + extra + ".",
               ({"فَ": "«so» + ", "وَ": "«and» + ", "": ""}[c]) + en + " — a muḍāriʿ; the doer «" + {"نَحْنُ": "we", "أَنَا": "I", "أَنْتَ": "you"}[hidden] + "» is necessarily concealed.", ({"فَ": "«o hâlde» + ", "وَ": "«ve» + ", "": ""}[c]) + tr + " — muzâri; fâil vücûben gizli (" + {"نَحْنُ": "biz", "أَنَا": "ben", "أَنْتَ": "sen"}[hidden] + ").", punct=punct, segments=([seg(c, "fa" if c == "فَ" else "wa", "conj"), seg(body, lex, "verb")] if c else None))
def mudari1_pron(full, lex, stem, hidden, en, tr, punct=None, wa=False, tags=()):
    return tok(full, lex, "verb", ([AT] if wa else []) + ["mudari-marfu", MB] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: " + hidden + "، وَالْهَاءُ مَفْعُولٌ بِهِ.", ("«and» + " if wa else "") + en + " — the muḍāriʿ with its object pronoun.", ("«ve» + " if wa else "") + tr + " — mef'ûl zamirli muzâri.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg(stem, lex, "verb"), seg("هُ", "pron-3ms", "pron")])
def lana_ahl(full_li, pron_form, pron_lex, en_li, tr_li, punct=None):
    return [tok(full_li, "li", "prep", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالضَّمِيرُ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and " + en_li + "» — a fronted khabar.", "«ve " + tr_li + "» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg(full_li[2:3] + full_li[3:4], "li", "prep"), seg(pron_form, pron_lex, "pron")]),
            tok("أَهْلٌ", "ahl", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«family» — the delayed mubtadaʾ.", "«aile» — sonraya bırakılmış mübtedâ."),
            atf("وَذُرِّيَّةٌ", "dhurriyya", "«offspring»", "«zürriyet»", case="raf", punct=punct)]
def fa_kayfa():
    return tok("فَكَيْفَ", "kayfa", "noun", [AT, IS, HL], "الْفَاءُ لِلتَّفْرِيعِ (عَاطِفَةٌ)، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«so how» — the question noun, in the place of a ḥāl.", "«o hâlde nasıl» — soru ismi, mahallen mansub hâl.", segments=[seg("فَ", "fa", "conj"), seg("كَيْفَ", "kayfa", "noun")])
def la_khamsa(full, lex, en, tr, punct=None, tags=(), wa=False):
    return khamsa(full, lex, en, tr, tags=["la-nafiya"] + list(tags), punct=punct, wa=wa)
def innaka(wa=False):
    full = "وَإِنَّكَ" if wa else "إِنَّكَ"
    return tok(full, "inna", "part", ([AT] if wa else []) + [IW], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", ("«and» + " if wa else "") + "«indeed you» — inna with its ism, the attached kāf.", ("«ve» + " if wa else "") + "«şüphesiz sen» — inne + ismi olan bitişik kâf.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")])
def la_mudari2(full, lex, en, tr, punct=None, tags=(), wa=False, first=False):
    pre = "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ، وَ" if wa else ""
    body = full[4:] if wa else full
    role = " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ" if first else ""
    return tok(full, lex, "verb", ([AT] if wa else []) + ["la-nafiya", "mudari-marfu"] + ([IW] if first else []) + list(tags), pre + body + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ" + role + ".", ("«and … not» + " if wa else "") + en + " — the doer «you» is concealed" + ("; the clause is inna's khabar." if first else "."), ("«ve … -mezsin» + " if wa else "") + tr + " — fâil gizli (sen)" + ("; cümle inne'nin haberi." if first else "."), punct=punct, segments=([seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part"), seg(body, lex, "verb")] if wa else None))
def daiman(punct=None):
    return tok("دَائِمًا", "daiman", "noun", [MH], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (صِفَةٌ نَابَتْ عَنِ الظَّرْفِ: وَقْتًا دَائِمًا).", "«always» — a time adverbial.", "«daima» — zaman zarfı.", punct=punct)

# ---------------------------------------------------------------- § the small helpers shared with chapter 7
def nuh_fail(full="نُوحٌ", punct=None): return tok(full, "nuh", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the doer.", "«Nûh» — fâil.", punct=punct)
def nuh_ism_kana(punct=None): return tok("نُوحٌ", "nuh", "propn", [KN], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«Nūḥ» — kāna's ism.", "«Nûh» — kâne'nin ismi.", punct=punct)
def qawm_pron(full, pron_form, pron_lex, ar_role, en, tr, punct=None, tags=()):
    return noun_pron(full, "qawm", full[:len(full) - len(pron_form)], pron_form, pron_lex, ar_role, en, tr, tags=list(tags), punct=punct)
DF = "damir-fasl"; YM = "ya-al-mutakallim"; VM = "vocative-munada"; AM2 = "anwa-ma"; NW = "huruf-jarr-nawadir"; TW = "tawkid"; QD = "qad-harf"
def yarawna(full="يَرَوْنَ", wa=False):
    return tok(full, "raa", "verb", [KN, AK, "mudari-marfu", "naqis-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ: يَرَى + ونَ)، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ يَسُدُّ مَسَدَّ مَفْعُولَيْهِ.", "«used to hold» — a muḍāriʿ of the five, its final yāʾ dropped before the wāw; kāna's khabar; the anna-clause fills the seat of its two objects.", "«görüyorlardı / sayıyorlardı» — beş fiilden; lâm-ı fiil düştü; kâne'nin haberi; enne cümlesi iki mef'ûlün yerini tutar.")
def yara(full="يَرَى"):
    return tok(full, "raa", "verb", [KN, "mudari-marfu", "naqis-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ يَسُدُّ مَسَدَّ مَفْعُولَيْهِ.", "«held» — the muḍāriʿ with its ḍamma estimated on the alif; kāna's khabar.", "«görüyordu / sayıyordu» — damme elif üzerinde takdîrî; kâne'nin haberi.")
def anna_(wa=False, obj="يَرَى"):
    return anna(wa=wa, obj_of=obj)
def ibadat_asnam(case="nasb", part="أَنَّ", punct=None):
    ar = {"nasb": "اسْمُ " + part + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."}[case]
    return [tok("عِبَادَةَ", "ibada", "noun", [IW, ID], ar, "«the worship [of]» — anna's ism, annexed.", "«… -e tapmak» — enne'nin ismi, muzâf."),
            mudaf_ilayh("الْأَصْنَامِ", "sanam", "«the idols»", "«putlara»", punct=punct, tags=[JT])]
def huwa_fasl(en="«is»", tr="«-dır»"):
    return tok("هُوَ", "huwa", "pron", [DF, IW], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ (وَيَجُوزُ جَعْلُهُ مُبْتَدَأً وَمَا بَعْدَهُ خَبَرُهُ) — جَاءَ مُذَكَّرًا لِأَنَّ الْخَبَرَ مُذَكَّرٌ.", "«it» — the pronoun of separation between anna's ism and khabar, with no place in iʿrāb (or a mubtadaʾ with the next word as its khabar); masculine, agreeing with the khabar.", "«o / -dır» — isim ile haber arasındaki fasıl zamiri, i'râbdan mahalli yok (ya da mübtedâ); habere uyarak müzekker.")
def khabar_anna(full, lex, en, tr, punct=None, tags=()):
    return khabar_inna(full, lex, en, tr, part="أَنَّ", punct=punct, tags=list(tags))
def fi_dalala(punct=None, role=""):
    return [fi(), majrur("ضَلَالَةٍ", "dalalah-error", "«error»", "«sapıklık»", ar="مَجْرُورٌ بِالْكَسْرَةِ" + role + "."), atf("وَسَفَاهَةٍ", "sifaha", "«folly»", "«ve beyinsizlik»", case="jarr", punct=punct)]
def asnam_maful(punct=None): return maful_("الْأَصْنَامَ", "sanam", "«the idols»", "«putlara»", punct=punct, tags=[JT])
def kanu_yabuduna(wa=False, punct=None):
    return [kana_pl("وَكَانُوا" if wa else "كَانُوا", wa=wa), khamsa("يَعْبُدُونَ", "abada", "«worship»", "«tapıyorlardı»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ")]
def ya_qawmi():
    return [tok("يَا", "ya-nida", "part", [VM], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("قَوْمِ", "qawm", "noun", [VM, ID, YM], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا.", "«my people» — the munādā, annexed to the dropped yāʾ of the speaker: the kasra marks it.", "«kavmim» — münâdâ, hazfedilmiş mütekellim yâ'sına muzâf; kesre onun delili.")]

# ---------------------------------------------------------------- § chapter 8's own small helpers
def nuh_maful(punct=None, extra=""):
    return tok("نُوحًا", "nuh", "propn", [MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ (ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ)" + extra + ".", "«Nūḥ» — the object; the name takes tanwīn (three letters, the middle one still).", "«Nûh» — mef'ûl; üç harfli, ortası sâkin olduğu için tenvinli.", punct=punct)
def haulai(case, role_ar, en, tr, punct=None, tags=()):
    return tok("هٰؤُلَاءِ", "haulai", "pron", ["asma-al-ishara"] + list(tags), "اسْمُ إِشَارَةٍ لِلْجَمْعِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ " + {"raf": "رَفْعٍ", "nasb": "نَصْبٍ", "jarr": "جَرٍّ"}[case] + " " + role_ar + ".", en, tr, punct=punct)
def masakin(case, role_ar, en, tr, punct=None, tags=()):
    C = {"raf": "مَرْفُوعٌ بِالضَّمَّةِ", "nasb": "مَنْصُوبٌ بِالْفَتْحَةِ", "jarr": "مَجْرُورٌ بِالْكَسْرَةِ"}[case]
    return tok("الْمَسَاكِينَ" if case != "raf" else "الْمَسَاكِينُ", "miskin", "noun", [BD, JT] + list(tags), role_ar + " " + C + " — جَمْعُ مِسْكِينٍ عَلَى مَفَاعِيلَ.", en, tr, punct=punct)
def lakin_light(full="وَلٰكِنْ", punct=None):
    return tok(full, "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin: no government.", "«fakat» — tahfif edilmiş lâkin; amel etmez.", punct=punct, segments=wa_("لٰكِنْ", "lakin", "part"))
def ma_amana(full="آمَنَ", wa=False):
    toks = [tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not» — the negating mā.", "«-medi» — nefiy mâ'sı."),
            mazi(full, "aamana", "«believed»", "«iman etti»", tags=["form-iv-verbs", "la-nafiya"], hidden=None, extra_ar=" (الْفَاعِلُ بَعْدَ إِلَّا)")]
    return toks
def illa_mufarragh(punct=None):
    return tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ: الْكَلَامُ مَنْفِيٌّ وَالْمُسْتَثْنَى مِنْهُ مَحْذُوفٌ، فَمَا بَعْدَهَا يَأْخُذُ إِعْرَابَ الْفِعْلِ.", "«but» — the «emptied» exception: the word after it takes the verb's own case.", "«ancak, -den başka» — müferrağ istisnâ: sonraki kelime fiilin i'râbını alır.", punct=punct)
def bad_afrad(role="فَاعِلٌ", en="«some of the individuals»", tr="«bazı kimseler»"):
    return [tok("بَعْضُ", "baad", "noun", [FL, ID], role + " مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«some [of]» — the doer (after illā), annexed.", "«bazısı» — fâil (illâ'dan sonra), muzâf."),
            mudaf_ilayh("الْأَفْرَادِ", "fard-single", en, tr, tags=[JT])]
def nuh_ism_inna_light(punct=None):
    return tok("نُوحًا", "nuh", "propn", [IW], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — lākinna's ism.", "«Nûh» — lâkinne'nin ismi.", punct=punct)


# ---------------------------------------------------------------- § chapter 9's own small helpers
def laysa_bi(full, lex, en, tr, punct=None, wa=False, tags=()):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ""
    return tok(full, lex, "noun", ([AT] if wa else []) + [HJ, KN] + list(tags), pre + "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَ" + full[(4 if wa else 2):] + " مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ لَيْسَ.", ("«and» + " if wa else "") + en + " — the added bāʾ on laysa's khabar: jarr in form, naṣb by place.", ("«ve» + " if wa else "") + tr + " — leyse'nin haberine gelen zâid bâ; lafzan mecrûr, mahallen mansub.", punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("بِ", "bi", "prep"), seg(full[(4 if wa else 2):], lex, "noun")])
def laysa_(full="لَيْسَ", wa=False, role=""):
    return tok(full, "laysa", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"] + ([MK] if role else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ" + role + ".", ("«and» + " if wa else "") + "«is not» — laysa with its concealed ism" + (": the clause is the khabar of the mubtadaʾ." if role else "."), ("«ve» + " if wa else "") + "«değildir» — leyse, ismi gizli" + ("; cümle mübtedânın haberi." if role else "."), segments=(wa_("لَيْسَ", "laysa", "verb") if wa else None))
def na_pron(full, lex, pos, stem_lex_part, ar, en, tr, tags=(), punct=None, wa=False):
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg(full[(2 if wa else 0):-1], stem_lex_part, pos), seg("ا", "pron-1p", "pron")]
    return tok(full, lex, pos, ([AT] if wa else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
def lana(full="لَنَا", wa=False, role=" — خَبَرٌ مُقَدَّمٌ", en="«ours [is]» — a fronted khabar.", tr="«bizimdir» — öne alınmış haber.", punct=None, tags=(MK,)):
    return tok(full, "li", "prep", ([AT] if wa else []) + [HJ] + list(tags), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "اللَّامُ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ" + role + ".", ("«and» + " if wa else "") + en, ("«ve» + " if wa else "") + tr, punct=punct, segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("لَ", "li", "prep"), seg("نَا", "pron-1p", "pron")])
def kull_mubtada(punct=None): return tok("كُلُّ", "kull", "noun", [MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«every» — the delayed mubtadaʾ, annexed.", "«her» — sonraya bırakılmış mübtedâ, muzâf.", punct=punct)
def kull_jarr(punct=None): return tok("كُلِّ", "kull", "noun", [HJ, ID], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«every» — after the preposition, annexed.", "«her» — harf-i cerden sonra, muzâf.", punct=punct)
def mina(punct=None): return tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of / from» — its nūn takes a fatḥa before the next hamzat al-waṣl.", "«-den» — nûnu iki sâkin yüzünden fetha aldı.", punct=punct)
def a_la(punct=None):
    return tok("أَلَا", "hamza-istifham", "part", [IS, "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَا نَافِيَةٌ.", "«do … not?» — the question hamza of affirmation + the negating lā.", "«… -mez misiniz?» — takrîrî istifham hemzesi + nefiy lâ'sı.", punct=punct, segments=[seg("أَ", "hamza-istifham", "part"), seg("لَا", "la-nafiya", "part")])
def tanzuruna(punct=None): return khamsa("تَنْظُرُونَ", "nazara", "«you look»", "«bakmıyor musunuz»", tags=[IS, "la-nafiya"], punct=punct)
def ila_(punct=None): return prep("إِلَى", "ila", "«to / at»", "«-e»", punct=punct)
def kum_mim(full, lex, pre_form, pre_lex, en, tr, punct=None, tags=(), letter="حَرْفُ جَرٍّ"):
    return tok(full, lex, "prep", [HJ] + list(tags), pre_form + " " + letter + "، وَكُمْ فِي مَحَلِّ جَرٍّ، حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", en + " — the mīm of «you» takes a ḍamma before the next hamzat al-waṣl.", tr + " — mîm iki sâkin yüzünden damme aldı.", punct=punct, segments=[seg(pre_form, pre_lex, "prep"), seg("كُمُ", "pron-2mp", "pron")])
def wa_jaala(): return mazi("وَجَعَلَ", "jaala", "«and made»", "«ve kıldı»", tags=[AT, MX], wa=True, extra_ar=" — يَنْصِبُ مَفْعُولَيْنِ")
def obj1(full, lex, en, tr, punct=None): return tok(full, lex, "noun", [MB, MX], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the first object.", tr + " — birinci mef'ûl.", punct=punct)
def obj2(full, lex, en, tr, punct=None): return tok(full, lex, "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", en + " — the second object.", tr + " — ikinci mef'ûl.", punct=punct)
def lakinna_qawm_nuh():
    return [tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kız kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
            tok("قَوْمَ", "qawm", "noun", [IW, ID], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the people [of]» — lākinna's ism, annexed.", "«kavmi» — lâkinne'nin ismi, muzâf.", ),
            tok("نُوحٍ", "nuh", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the muḍāf ilayh.", "«Nûh'un» — muzâfun ileyh."),
            tok("لَمْ", "lam-jazima", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«did not» — lam: it negates, jazms and turns the tense back.", "«-medi» — nefiy, cezm ve kalb harfi lem.")]
def lam_khamsa(full, lex, en, tr, punct=None, tags=(), role=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"):
    return tok(full, lex, "verb", [LJ, AK] + list(tags), "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ" + role + ".", en + " — jazm by the dropped nūn; the wāw is the doer.", tr + " — nûnun hazfiyle meczûm; vâv fâil.", punct=punct)
def wa_kayfa(): return tok("وَكَيْفَ", "kayfa", "noun", [AT, IS, HL], "الْوَاوُ عَاطِفَةٌ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«and how» — the question noun, in the place of a ḥāl.", "«ve nasıl» — soru ismi; mahallen mansub hâl.", segments=wa_("كَيْفَ", "kayfa", "noun"))
def mudari_fail_after(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.", en + " — a muḍāriʿ; the doer follows.", tr + " — muzâri; fâil sonra.", punct=punct)
def man_fail(): return tok("مَنْ", "man", "pron", [MW, FL], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«one who» — the relative; the doer.", "«… kimse» — ism-i mevsûl; fâil.")
def wa_daa_nuh_qawmahu(punct="،"):
    return [tok("وَدَعَا", "daa", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ (اسْتِئْنَافِيَّةٌ)، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«and … called» — the defective māḍī, its fatḥa estimated on the alif.", "«ve çağırdı» — nâkıs mâzî, fethası elif üzerinde takdîrî.", segments=wa_("دَعَا", "daa", "verb")),
            nuh_fail(),
            qawm_pron("قَوْمَهُ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the object.", "«kavmini» — mef'ûl.", tags=[MB, ID], punct=punct)]

# ---------------------------------------------------------------- §15 حُجَّةُ الْأَغْنِيَاءِ (print p. 23)
sen("s1", "And the rich said: what Nūḥ calls to is not true and is not good.", "Zenginler dediler: Nûh'un çağırdığı şey hak değildir ve hayır değildir.", [
  qala("وَقَالَ", wa=True, punct=None),
  fail("الْأَغْنِيَاءُ", "ghani", "«the rich»", "«zenginler»", tags=[JT], punct=":"),
  tok("الَّذِي", "alladhi", "pron", [MW, MK], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what / that which» — the relative; the mubtadaʾ.", "«… şey» — ism-i mevsûl; mübtedâ."),
  tok("يَدْعُو", "daa", "verb", ["mudari-marfu", MW, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "«calls» — the defective muḍāriʿ, its ḍamma estimated on the wāw; the ṣila; the doer follows.", "«çağırıyor» — nâkıs muzâri, dammesi vâv üzerinde takdîrî; sıla; fâil sonra."),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to it» — the ʿāʾid, the pronoun returning to the relative.", "«ona» — mevsûle dönen âid zamir.", tags=[MW], extra_ar=" — الْعَائِدُ عَلَى الْمَوْصُولِ"),
  nuh_fail(),
  laysa_(role=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ"),
  laysa_bi("بِحَقٍّ", "haqq", "«true»", "«hak»"),
  laysa_("وَلَيْسَ", wa=True),
  laysa_bi("بِخَيْرٍ", "khayr", "«good»", "«hayır»", punct="."),
])
sen("s2", "Why?", "Niçin?", [
  tok("لِمَاذَا", "limadha", "pron", [IS, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَبَقِيَّةُ السُّؤَالِ مَحْذُوفَةٌ: لِمَاذَا لَيْسَ بِحَقٍّ؟", "«why?» — li + the question word; the rest of the question is understood.", "«niçin?» — li + soru ismi; sorunun gerisi hazfedilmiş.", punct="؟"),
])
sen("s3", "Because we have found by experience that we are the first in every good thing.", "Çünkü tecrübeyle gördük ki her hayırda öncü olan biziz.", [
  tok("لِأَنَّا", "lianna", "part", [HJ, IW, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا (أَنَّنَا: أُدْغِمَتِ النُّونُ) — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ.", "«because we» — li + anna + nā (anna-nā contracted); the pronoun is anna's ism.", "«çünkü biz» — li + enne + nâ (enne-nâ idgamlı); zamir enne'nin ismi.", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), seg("ا", "pron-1p", "pron")]),
  tok("جَرَّبْنَا", "jarraba", "verb", [IW, "form-ii-verbs", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ؛ وَجَرَّبَ هُنَا بِمَعْنَى عَلِمَ.", "«we have found by experience» — a Form II māḍī on nā; the clause is anna's khabar; «tried» here means «came to know».", "«tecrübeyle gördük» — tef'îl bâbından mâzî, nâ fâil; cümle enne'nin haberi; burada «bildik» mânâsında.", segments=[seg("جَرَّبْ", "jarraba", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("أَنَّا", "anna", "part", [IW, MB], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ يَسُدُّ مَسَدَّ مَفْعُولَيْ جَرَّبْنَا.", "«that we» — anna + nā; the clause fills the seat of the two objects.", "«biz … olduğumuzu» — enne + nâ; cümle iki mef'ûlün yerini tutar.", segments=[seg("أَنَّ", "anna", "part"), seg("ا", "pron-1p", "pron")]),
  tok("نَحْنُ", "nahnu", "pron", [DF, IW], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ (أَوْ تَوْكِيدٌ لِاسْمِ أَنَّ).", "«we» — the pronoun of separation (or an emphasis of anna's ism).", "«biz» — fasıl zamiri (ya da enne'nin isminin tekidi)."),
  tok("السَّابِقُونَ", "sabiq", "noun", [IW, JS, "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the first» — anna's khabar, rafʿ by the wāw.", "«öncüler» — enne'nin haberi; vâv ile merfû."),
  fi(), kull_jarr(),
  mudaf_ilayh("خَيْرٍ", "khayr", "«good thing»", "«hayırda»", punct="."),
])
sen("s4", "Ours is every good thing of food, and ours is every fine thing of clothing.", "Yiyeceğin her iyisi bizimdir, giyeceğin her güzeli bizimdir.", [
  lana(), kull_mubtada(),
  mudaf_ilayh("طَيِّبٍ", "tayyib-good", "«good thing»", "«iyi şey»"),
  mina(), majrur("الطَّعَامِ", "taam", "«food»", "«yiyecekten»", punct="،"),
  lana("وَلَنَا", wa=True), kull_mubtada(),
  mudaf_ilayh("جَمِيلٍ", "jamil", "«fine thing»", "«güzel şey»"),
  mina(), majrur("اللِّبَاسِ", "libas", "«clothing»", "«giyecekten»", punct="."),
])
sen("s5", "And the people, in everything, are our followers.", "İnsanlar da her şeyde bize tâbidir.", [
  tok("وَالنَّاسُ", "nas", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالنَّاسُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and the people» — the mubtadaʾ.", "«ve insanlar» — mübtedâ.", segments=wa_("النَّاسُ", "nas", "noun")),
  fi(), kull_jarr(), mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeyde»"),
  lana(role=" — مُتَعَلِّقٌ بِالْخَبَرِ", en="«to us» — hanging on the khabar.", tr="«bize» — habere müteallik.", tags=()),
  khabar("تَبَعٌ", "tabaa-followers", "«followers»", "«tâbidir»", punct=".", extra=" — مَصْدَرٌ بِمَعْنَى اسْمِ الْفَاعِلِ (تَابِعُونَ)، يَسْتَوِي فِيهِ الْوَاحِدُ وَالْجَمْعُ"),
])
sen("s6", "And we have seen that good does not miss us and does not pass us by in the city.", "Ve gördük ki hayır bizi ıskalamaz ve şehirde bizi geçip gitmez.", [
  na_pron("وَإِنَّا", "inna", "part", "inna", "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا (إِنَّنَا: أُدْغِمَتِ النُّونُ).", "«and indeed we» — inna + nā.", "«ve şüphesiz biz» — inne + nâ.", tags=[IW], wa=True),
  tok("رَأَيْنَا", "raa", "verb", [IW, MB, "naqis-verbs", "zanna-wa-akhawatuha"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ؛ وَرَأَى هُنَا عِلْمِيَّةٌ تَنْصِبُ مَفْعُولَيْنِ.", "«we have seen» — raʾā of knowing, taking two objects; the clause is inna's khabar.", "«gördük / anladık» — iki mef'ûl alan ilim bildiren raâ; cümle inne'nin haberi.", segments=[seg("رَأَيْ", "raa", "verb"), seg("نَا", "pron-1p", "pron")]),
  anna(obj_of="رَأَيْنَا (سَدَّ مَسَدَّ مَفْعُولَيْهِ)"),
  ism_inna("الْخَيْرَ", "khayr", "«the good»", "«hayır»", part="أَنَّ"),
  la_nafiya(),
  tok("يُخْطِئُنَا", "akhtaa", "verb", [IW, "la-nafiya", "mudari-marfu", MB, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "«misses us» — Form IV; nā is the object; the clause is anna's khabar.", "«bizi ıskalar» — if'âl; nâ mef'ûl; cümle enne'nin haberi.", segments=[seg("يُخْطِئُ", "akhtaa", "verb"), seg("نَا", "pron-1p", "pron")]),
  la_nafiya("وَلَا", wa=True),
  tok("يُجَاوِزُنَا", "jawaza3", "verb", [AT, "la-nafiya", "mudari-marfu", MB, "form-iii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا مَفْعُولٌ بِهِ — مَعْطُوفٌ عَلَى جُمْلَةِ الْخَبَرِ.", "«passes us by» — Form III; joined to the khabar clause.", "«bizi geçip gitmez» — mufâale; haber cümlesine ma'tûf.", segments=[seg("يُجَاوِزُ", "jawaza3", "verb"), seg("نَا", "pron-1p", "pron")]),
  fi(), majrur("الْمَدِينَةِ", "madina", "«the city»", "«şehirde»", punct="."),
])
sen("s7", "So had this religion been good, it would have come to us before these poor people — «had it been good, they would not have preceded us to it» (46:11).",
        "O hâlde bu din hayırlı olsaydı bu yoksullardan önce bize gelirdi — «eğer hayırlı olsaydı ona bizden önce varamazlardı» (46:11).", [
  tok("فَلَوْ", "law", "part", [AT, SH], "الْفَاءُ لِلتَّفْرِيعِ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ (امْتِنَاعٌ لِامْتِنَاعٍ).", "«so had» — law, the unreal condition.", "«o hâlde eğer … olsaydı» — cezmetmeyen şart harfi lev.", segments=[seg("فَ", "fa", "conj"), seg("لَوْ", "law", "part")]),
  kana("كَانَ", wa=False),
  tok("هٰذَا", "hadha", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "«this» — kāna's ism.", "«bu» — kâne'nin ismi."),
  tok("الدِّينُ", "din", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ (أَوْ عَطْفُ بَيَانٍ).", "«religion» — a badal of the demonstrative.", "«din» — ism-i işâretten bedel."),
  khabar_kana("خَيْرًا", "khayr", "«good»", "«hayırlı»"),
  tok("لَأَتَانَا", "ata", "verb", [SH, MB, "naqis-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَأَتَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَنَا مَفْعُولٌ بِهِ.", "«it would have come to us» — the lām of law's answer; the defective māḍī; nā is the object.", "«bize gelirdi» — lev'in cevap lâmı; nâkıs mâzî; nâ mef'ûl.", segments=[seg("لَ", "lam-jawab", "part"), seg("أَتَا", "ata", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("قَبْلَ", "qabla", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«before» — a time adverbial, annexed.", "«-den önce» — zaman zarfı, muzâf."),
  haulai("jarr", "مُضَافٌ إِلَيْهِ", "«these» — the muḍāf ilayh.", "«bu» — muzâfun ileyh.", tags=[ID]),
  tok("الْمَسَاكِينِ", "miskin", "noun", [BD, JT, MM], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مِسْكِينٍ عَلَى مَفَاعِيلَ، مَمْنُوعٌ مِنَ الصَّرْفِ، وَيُجَرُّ بِالْكَسْرَةِ لِدُخُولِ ال عَلَيْهِ.", "«poor people» — a badal; the diptote plural takes kasra here because it wears al.", "«yoksullar» — bedel; gayr-i munsarıf cem, lâm-ı ta'rîf aldığı için kesre ile mecrûr."),
  *quran([
    tok("لَوْ", "law", "part", [SH], "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ.", "«had»", "«eğer … olsaydı»"),
    tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الدِّينُ).", "«it been» — kāna, its ism concealed.", "«olsaydı» — kâne, ismi gizli."),
    khabar_kana("خَيْرًا", "khayr", "«good»", "«hayırlı»"),
    tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ — وَالْجُمْلَةُ بَعْدَهَا جَوَابُ لَوْ.", "«not» — the clause is the answer of law.", "«-mazlardı» — cümle lev'in cevabı."),
    tok("سَبَقُونَا", "sabaqa", "verb", [SH, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَنَا مَفْعُولٌ بِهِ.", "«they would have preceded us» — the group's wāw is the doer; nā is the object.", "«bizden önce varırlardı» — cemaat vâvı fâil; nâ mef'ûl.", segments=[seg("سَبَقُو", "sabaqa", "verb"), seg("نَا", "pron-1p", "pron")]),
    prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to it»", "«ona»", punct="."),
  ]),
])

# ---------------------------------------------------------------- §16 دَعْوَةُ نُوحٍ (print pp. 24–25)
sen("s8", "And Nūḥ called his people and strove in counsel.", "Nûh kavmini çağırdı ve nasihatte çok çabaladı.", [
  *wa_daa_nuh_qawmahu(punct="،"),
  mazi("وَاجْتَهَدَ", "ijtahada", "«and strove»", "«ve çabaladı»", tags=[AT, "form-viii-verbs"], wa=True),
  fi(), majrur("النَّصِيحَةِ", "nasiha", "«counsel»", "«nasihatte»", punct="."),
])
sen("s9", "«He said: O my people, I am to you a plain warner — that you worship God and fear Him and obey me; He will forgive you of your sins and reprieve you to an appointed term; indeed the term of God, when it comes, is not put back — if only you knew» (71:2–4).", "«Dedi: ey kavmim, ben size apaçık bir uyarıcıyım — Allah'a kulluk edin, O'ndan sakının ve bana itaat edin; günahlarınızdan bağışlar ve sizi belli bir vakte kadar erteler; Allah'ın eceli geldiğinde ertelenmez — keşke bilseydiniz» (71:2–4).", [
  *quran([
    qala("قَالَ", punct=None, hidden="هُوَ"),
    *ya_qawmi(),
    tok("إِنِّي", "inna", "part", [IW, YM], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«indeed I» — inna + the speaker's yāʾ, its ism.", "«şüphesiz ben» — inne + ismi olan mütekellim yâ'sı.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
    li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«to you» — hanging on the khabar.", "«size» — habere müteallik."),
    khabar_inna("نَذِيرٌ", "nadhir", "«a warner»", "«bir uyarıcıyım»"),
    naat("مُبِينٌ", "mubin", "«plain»", "«apaçık»", case="raf", punct="،", tags=["ism-fail"]),
    tok("أَنِ", "an-tafsiriyya", "part", ["mana-al-fil"], "أَنْ تَفْسِيرِيَّةٌ (بِمَعْنَى أَيْ) لَا مَحَلَّ لَهَا، كُسِرَتْ نُونُهَا لِالْتِقَاءِ السَّاكِنَيْنِ.", "«that [is]» — the explanatory an (= «namely»); its nūn takes a kasra before the next hamzat al-waṣl.", "«yani» — tefsîriyye en; nûnu iki sâkin yüzünden kesre aldı.", segments=None),
    tok("اعْبُدُوا", "abada", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَهَمْزَتُهُ هَمْزَةُ وَصْلٍ.", "«worship» — an imperative, built on the dropped nūn; the wāw is the doer.", "«kulluk edin» — nûnun hazfi üzere mebnî emir; vâv fâil."),
    allah_maful(),
    tok("وَاتَّقُوهُ", "ittaqa", "verb", [AT, AM, MB, "form-viii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاتَّقُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and fear Him» — joined; the dropped nūn; the hāʾ is the object.", "«ve O'ndan sakının» — ma'tûf; nûn düşmüş; hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("اتَّقُو", "ittaqa", "verb"), seg("هُ", "pron-3ms", "pron")]),
    tok("وَأَطِيعُونِ", "ataa", "verb", [AT, AM, MB, "form-iv-verbs", "hollow-verbs", YM], "الْوَاوُ عَاطِفَةٌ، وَأَطِيعُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ الْمَحْذُوفَةُ مَفْعُولٌ بِهِ (أَطِيعُونِي).", "«and obey me» — the nūn of protection; the speaker's yāʾ, dropped in the āya, is the object.", "«ve bana itaat edin» — vikâye nûnu; âyette hazfedilen mütekellim yâ'sı mef'ûl.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("أَطِيعُو", "ataa", "verb"), seg("نِ", "pron-1s", "pron")]),
    tok("يَغْفِرْ", "ghafara", "verb", ["jawab-al-talab"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الطَّلَبِ (اعْبُدُوا … يَغْفِرْ)، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«He will forgive» — jazm as the answer of the command.", "«bağışlar» — emrin cevabı olarak meczûm."),
    li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«you»", "«sizi»"),
    prep("مِنْ", "min", "«of»", "«-dan»"),
    noun_pron("ذُنُوبِكُمْ", "dhanb", "ذُنُوبِ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — جَمْعُ ذَنْبٍ.", "«your sins»", "«günahlarınızdan»", tags=[HJ, ID, JT]),
    tok("وَيُؤَخِّرْكُمْ", "akhkhara", "verb", [AT, "jawab-al-talab", MB, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُؤَخِّرْ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِالْعَطْفِ عَلَى جَوَابِ الطَّلَبِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَكُمْ مَفْعُولٌ بِهِ.", "«and reprieve you» — joined to the jazm'd answer; kum is the object.", "«ve sizi erteler» — cevaba ma'tûf, meczûm; küm mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يُؤَخِّرْ", "akhkhara", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
    ila_(), majrur("أَجَلٍ", "ajal", "«a term»", "«bir vakte»"),
    tok("مُسَمًّى", "musamma", "noun", [NA, "ism-maful", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِلتَّنْوِينِ — اسْمُ مَفْعُولٍ مَقْصُورٌ.", "«appointed» — a naʿt; the maqṣūr passive participle hides its kasra.", "«belli» — sıfat; maksûr ism-i mef'ûl, kesresi takdîrî."),
    inna(),
    tok("أَجَلَ", "ajal", "noun", [IW, ID], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the term [of]» — inna's ism, annexed.", "«eceli» — inne'nin ismi, muzâf."),
    allah_mi(),
    idha(),
    tok("جَاءَ", "jaa", "verb", ["idha-shartiyya", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — فِعْلُ الشَّرْطِ.", "«it comes» — the condition's verb.", "«geldiğinde» — şart fiili."),
    la_nafiya(),
    tok("يُؤَخَّرُ", "akhkhara", "verb", [IW, "la-nafiya", "mudari-marfu", NF, "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ، وَهِيَ جَوَابُ إِذَا.", "«is not put back» — the passive muḍāriʿ; the clause is inna's khabar and the answer of idhā.", "«ertelenmez» — meçhul muzâri; cümle inne'nin haberi ve izâ'nın cevabı."),
    tok("لَوْ", "law", "part", [SH], "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ، وَجَوَابُهُ مَحْذُوفٌ.", "«if [only]» — law; its answer is understood.", "«keşke» — lev; cevabı mahzuf."),
    tok("كُنْتُمْ", "kana", "verb", [KN, SH, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ اسْمُهُ.", "«you were» — kāna before the doer's tāʾ, its ism.", "«idiniz» — fâil tâ'sından önce kâne; tâ ismi.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
    khamsa("تَعْلَمُونَ", "alima", "«knew»", "«bilseydiniz»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", punct="."),
  ]),
])
sen("s10", "And God had withheld the rain from them and was angry with them, and the tillage grew scarce and the offspring grew scarce.", "Allah onlardan yağmuru tutmuş ve onlara gazap etmişti; ekin azaldı, nesil azaldı.", [
  kana(),
  tok("اللهُ", "allah", "propn", [KN], "لَفْظُ الْجَلَالَةِ اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«God» — kāna's ism.", "«Allah» — kâne'nin ismi."),
  mazi("حَبَسَ", "habasa", "«had withheld»", "«tutmuştu»", tags=[KN, MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ (كَانَ + الْمَاضِي: الْمَاضِي الْبَعِيدُ)"),
  tok("عَنْهُمُ", "an-prep", "prep", [HJ], "عَنْ حَرْفُ جَرٍّ، وَهُمْ فِي مَحَلِّ جَرٍّ، حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from them» — the mīm takes a ḍamma before the next hamzat al-waṣl.", "«onlardan» — mîm iki sâkin yüzünden damme aldı.", segments=[seg("عَنْ", "an-prep", "prep"), seg("هُمُ", "pron-3mp", "pron")]),
  maful("الْمَطَرَ", "matar", "«the rain»", "«yağmuru»"),
  mazi("وَغَضِبَ", "ghadiba", "«and was angry»", "«ve gazap etti»", tags=[AT], wa=True),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«with them»", "«onlara»"),
  tok("وَقَلَّ", "qalla", "verb", [AT, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَلَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مُضَاعَفٌ (قَلَّ يَقِلُّ).", "«and … grew scarce» — a doubled verb.", "«ve azaldı» — muzâaf fiil.", segments=wa_("قَلَّ", "qalla", "verb")),
  fail("الْحَرْثُ", "harth", "«the tillage»", "«ekin»"),
  tok("وَقَلَّ", "qalla", "verb", [AT, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَقَلَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مُضَاعَفٌ.", "«and … grew scarce»", "«ve azaldı»", segments=wa_("قَلَّ", "qalla", "verb")),
  fail("النَّسْلُ", "nasl-offspring", "«the offspring»", "«nesil»", punct="."),
])
sen("s11", "So Nūḥ said: O my people, if you believe, God will be pleased with you and this punishment will depart.", "Bunun üzerine Nûh dedi: ey kavmim, eğer iman ederseniz Allah sizden razı olur ve bu azap kalkar.", [
  qala("فَقَالَ", wa=True, punct=None), nuh_fail(punct=":"), *ya_qawmi(),
  tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional in.", "«eğer» — cezmeden şart harfi."),
  tok("آمَنْتُمْ", "aamana", "verb", [SH, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«you believe» — the condition's verb; the doer's tāʾ.", "«iman ederseniz» — şart fiili; fâil tâ'sı.", segments=[seg("آمَنْ", "aamana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("رَضِيَ", "radiya", "verb", [SH], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالْفَاعِلُ بَعْدَهُ.", "«[then] … is pleased» — the condition's answer; the doer follows.", "«razı olur» — şartın cevabı; fâil sonra."),
  kum_mim("عَنْكُمُ", "an-prep", "عَنْ", "an-prep", "«with you»", "«sizden»"),
  allah_fail(),
  tok("وَزَالَ", "zala", "verb", [AT, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَزَالَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ (زَالَ يَزُولُ)، مَعْطُوفٌ عَلَى جَوَابِ الشَّرْطِ.", "«and … departs» — a hollow verb joined to the answer.", "«ve kalkar» — ecvef fiil; cevaba ma'tûf.", segments=wa_("زَالَ", "zala", "verb")),
  tok("هٰذَا", "hadha", "pron", [FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this» — the doer.", "«bu» — fâil."),
  tok("الْعَذَابُ", "adhab", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "«punishment» — a badal.", "«azap» — bedel.", punct="."),
])
sen("s12", "And He will send the rains upon you and bless you in provision and children.", "Üzerinize yağmurları gönderir ve rızıkta ve çocuklarda size bereket verir.", [
  mazi("وَأَرْسَلَ", "arsala", "«and sends»", "«ve gönderir»", tags=[AT, "form-iv-verbs"], wa=True, extra_ar=" — مَعْطُوفٌ عَلَى جَوَابِ الشَّرْطِ"),
  kum_mim("عَلَيْكُمُ", "ala", "عَلَيْ", "ala", "«upon you»", "«üzerinize»"),
  maful("الْأَمْطَارَ", "matar", "«the rains»", "«yağmurları»", tags=[JT]),
  mazi("وَبَارَكَ", "baraka-bless", "«and blesses»", "«ve bereket verir»", tags=[AT, "form-iii-verbs"], wa=True),
  li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«you»", "«size»"),
  fi(), majrur("الرِّزْقِ", "rizq", "«provision»", "«rızıkta»"),
  atf("وَالْأَوْلَادِ", "walad", "«children»", "«çocuklarda»", case="jarr", punct=".", tags=[JT]),
])
sen("s13", "And Nūḥ called his people to God and said to them: do you not know God?", "Nûh kavmini Allah'a çağırdı ve onlara dedi: Allah'ı tanımıyor musunuz?", [
  *wa_daa_nuh_qawmahu(punct=None),
  ila_(), majrur("اللهِ", "allah", "«God»", "«Allah'a»"),
  qala("وَقَالَ", wa=True, punct=None),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»", punct=":"),
  a_la(),
  khamsa("تَعْرِفُونَ", "arafa", "«you know»", "«tanımıyor musunuz»", tags=[IS, "la-nafiya"]),
  allah_maful(punct="؟"),
])
sen("s14", "These are the signs of God around you — do you not look at them?", "Bunlar çevrenizdeki Allah'ın âyetleridir — onlara bakmıyor musunuz?", [
  tok("هٰذِهِ", "hadhihi", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«these» — the mubtadaʾ.", "«bunlar» — mübtedâ."),
  tok("آيَاتُ", "aya", "noun", [MK, ID, JM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«[are] the signs [of]» — the khabar, annexed; a sound feminine plural.", "«âyetleridir» — haber, muzâf; cemi müennes sâlim."),
  allah_mi(),
  noun_pron("حَوْلَكُمْ", "hawla", "حَوْلَ", "كُمْ", "pron-2mp", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — حَالٌ (أَوْ خَبَرٌ ثَانٍ).", "«around you» — a place adverbial; a ḥāl.", "«çevrenizde» — mekân zarfı; hâl.", tags=[MF, ID, HL]),
  a_la(), tanzuruna(),
  prep_pron("إِلَيْهَا", "ila", "هَا", "pron-3fs", "«at them»", "«onlara»", punct="؟"),
])
sen("s15", "Do you not look at the sky and the earth? Do you not look at the sun and the moon?", "Göğe ve yere bakmıyor musunuz? Güneşe ve aya bakmıyor musunuz?", [
  a_la(), tanzuruna(), ila_(),
  majrur("السَّمَاءِ", "sama", "«the sky»", "«göğe»"),
  atf("وَالْأَرْضِ", "ard", "«the earth»", "«yere»", case="jarr", punct="؟"),
  a_la(), tanzuruna(), ila_(),
  majrur("الشَّمْسِ", "shams", "«the sun»", "«güneşe»"),
  atf("وَالْقَمَرِ", "qamar", "«the moon»", "«aya»", case="jarr", punct="؟"),
])
sen("s16", "Who created the heavens, and made the moon in them a light, and made the sun a lamp?", "Gökleri kim yarattı, ayı onlarda bir nur, güneşi bir kandil kim kıldı?", [
  tok("مَنْ", "man", "pron", [IS, MK], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the question noun; the mubtadaʾ.", "«kim» — soru ismi; mübtedâ."),
  mazi("خَلَقَ", "khalaqa", "«created»", "«yarattı»", tags=[MK, MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  tok("السَّمٰوَاتِ", "samawat", "noun", [MB, JM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ — رُسِمَ بِالْأَلِفِ الْخَنْجَرِيَّةِ.", "«the heavens» — the object; a sound feminine plural takes kasra for naṣb; written with the dagger alif.", "«gökleri» — mef'ûl; cemi müennes sâlim nasbda kesre alır; hançer elifle yazılmış.", punct="؟"),
  wa_jaala(),
  obj1("الْقَمَرَ", "qamar", "«the moon»", "«ayı»"),
  tok("فِيهِنَّ", "fi", "prep", [HJ], "فِي حَرْفُ جَرٍّ، وَهُنَّ فِي مَحَلِّ جَرٍّ — يَعُودُ عَلَى السَّمٰوَاتِ.", "«in them» — the pronoun returns to the heavens.", "«onların içinde» — zamir göklere döner.", segments=[seg("فِي", "fi", "prep"), seg("هِنَّ", "pron-3fp", "pron")]),
  obj2("نُورًا", "nur", "«a light»", "«bir nur»"),
  wa_jaala(),
  obj1("الشَّمْسَ", "shams", "«the sun»", "«güneşi»"),
  obj2("سِرَاجًا", "siraj", "«a lamp»", "«bir kandil»", punct="؟"),
])
sen("s17", "And who created you, and made the earth a carpet for you?", "Sizi kim yarattı, yeri sizin için bir döşek kim kıldı?", [
  tok("وَمَنْ", "man", "pron", [AT, IS, MK], "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and who» — the question noun; the mubtadaʾ.", "«ve kim» — soru ismi; mübtedâ.", segments=wa_("مَنْ", "man", "pron")),
  v_pron("خَلَقَكُمْ", "khalaqa", "خَلَقَ", "كُمْ", "pron-2mp", "«created you» — the clause is the khabar.", "«sizi yarattı» — cümle haber.", punct=".", tags=[MK]),
  wa_jaala(),
  kum_mim("لَكُمُ", "li", "لَ", "li", "«for you»", "«sizin için»"),
  obj1("الْأَرْضَ", "ard", "«the earth»", "«yeri»"),
  obj2("بِسَاطًا", "bisat", "«a carpet»", "«bir döşek»", punct="؟"),
])
sen("s18", "But the people of Nūḥ did not use their reason! But the people of Nūḥ did not believe!", "Fakat Nûh'un kavmi akıl etmedi! Fakat Nûh'un kavmi iman etmedi!", [
  *lakinna_qawm_nuh(),
  lam_khamsa("يَعْقِلُوا", "aqala", "«did not use their reason»", "«akıl etmediler»", punct="!", tags=[IW]),
  *lakinna_qawm_nuh(),
  lam_khamsa("يُؤْمِنُوا", "aamana", "«did not believe»", "«iman etmediler»", punct="!", tags=[IW, "form-iv-verbs"]),
])
sen("s19", "Rather, when Nūḥ called them to God they put their fingers in their ears.", "Bilakis Nûh onları Allah'a çağırınca parmaklarını kulaklarına tıkadılar.", [
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ.", "«rather» — bal, the particle of turning away.", "«bilakis» — idrâb harfi."),
  idha(),
  v_pron("دَعَاهُمْ", "daa", "دَعَا", "هُمْ", "pron-3mp", "«called them» — the condition's verb; the defective māḍī keeps its alif before the pronoun.", "«onları çağırdı» — şart fiili; nâkıs mâzî zamirden önce elifini korur.", hidden=None, tags=[SH, "naqis-verbs"]),
  nuh_fail(), ila_(), majrur("اللهِ", "allah", "«God»", "«Allah'a»"),
  tok("جَعَلُوا", "jaala", "verb", [SH, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — جَوَابُ إِذَا.", "«they put» — the answer of idhā; the wāw is the doer.", "«koydular» — izâ'nın cevabı; vâv fâil."),
  noun_pron("أَصَابِعَهُمْ", "isba", "أَصَابِعَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ إِصْبَعٍ عَلَى أَفَاعِلَ.", "«their fingers» — the object; the plural pattern أَفَاعِل.", "«parmaklarını» — mef'ûl; efâil vezninde cem.", tags=[MB, ID, JT]),
  fi(),
  noun_pron("آذَانِهِمْ", "udhun", "آذَانِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — جَمْعُ أُذُنٍ عَلَى أَفْعَالٍ (أَأْذَان → آذَان).", "«their ears» — the plural أَفْعَال of udhun; the two hamzas become ā.", "«kulaklarına» — uzun'un ef'âl cem'i; iki hemze â oldu.", tags=[HJ, ID, JT], punct="."),
])
sen("s20", "And how can one understand who does not hear? And how can one hear who does not want to hear?", "İşitmeyen nasıl anlar? İşitmek istemeyen nasıl işitir?", [
  wa_kayfa(),
  mudari_fail_after("يَفْهَمُ", "fahima", "«understands»", "«anlar»"),
  man_fail(), la_nafiya(),
  neg_mudari("يَسْمَعُ", "samia", "«does not hear»", "«işitmez»", hidden="هُوَ", tags=[MW], extra=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ", punct="؟"),
  wa_kayfa(),
  mudari_fail_after("يَسْمَعُ", "samia", "«hears»", "«işitir»"),
  man_fail(), la_nafiya(),
  neg_mudari("يُرِيدُ", "arada", "«does not want»", "«istemez»", hidden="هُوَ", tags=[MW, "form-iv-verbs", "hollow-verbs"], extra=" — صِلَةُ الْمَوْصُولِ"),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيُرِيدُ", "«to»", "«-mek»"),
  mansub("يَسْمَعَ", "samia", "«hear»", "«işitmek»", punct="؟"),
])

CAND = {
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "the one who, which (masc.)", "o ki, … olan", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to pray, call", "çağırmak, dua etmek", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "his / its (attached pronoun)", "onun (bitişik)", 1),
 "nuh": G("nuh", "نُوح", None, "propn", "Nūḥ (Noah)", "Nûh", 1),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not", "değildir", 1),
 "haqq": G("haqq", "حَقّ", "ح ق ق", "noun", "truth, true", "hak, gerçek", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good", "hayır, iyilik", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, for (fa)", "bunun üzerine", 1),
 "limadha": G("limadha", "لِمَاذَا", None, "pron", "why? (for what?)", "niçin?", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (heavy anna)", "ki (şeddeli enne)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we, us (attached)", "biz, bizi (bitişik)", 1),
 "jarraba": G("jarraba", "جَرَّبَ", "ج ر ب", "verb", "to try, to test, to find by experience (Form II)", "denemek, tecrübe etmek (tef'îl)", 1),
 "nahnu": G("nahnu", "نَحْنُ", None, "pron", "we (detached)", "biz (munfasıl)", 1),
 "sabiq": G("sabiq", "سَابِق", "س ب ق", "noun", "preceding, earlier (ism fa'il of سَبَقَ)", "önceki, öncü (ism-i fâil)", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every; the whole of it", "her, bütün", 1),
 "tayyib-good": G("tayyib-good", "طَيِّب", "ط ي ب", "noun", "good, pleasant, wholesome", "iyi, hoş, temiz", 1),
 "min": G("min", "مِنْ", None, "prep", "from; than (with ism tafdil)", "-den", 1),
 "taam": G("taam", "طَعَام", "ط ع م", "noun", "food", "yiyecek", 1),
 "jamil": G("jamil", "جَمِيل", "ج م ل", "noun", "beautiful", "güzel", 1),
 "libas": G("libas", "لِبَاس", "ل ب س", "noun", "clothing", "giyecek, elbise", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "tabaa-followers": G("tabaa-followers", "تَبَع", "ت ب ع", "noun", "followers, dependants (a masdar used for one and many)", "tâbi olanlar, uyanlar (tek ve çok için masdar)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed, verily", "şüphesiz", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (simple negation)", "değil, -mez (nefiy lâ'sı)", 1),
 "akhtaa": G("akhtaa", "أَخْطَأَ", "خ ط أ", "verb", "to err, to miss the mark (Form IV; أَخْطَأَهُ: it missed him)", "hata etmek; ıskalamak (if'âl)", 1),
 "jawaza3": G("jawaza3", "جَاوَزَ", "ج و ز", "verb", "to pass beyond, to go past (Form III)", "aşmak, geçip gitmek (mufâale)", 1),
 "madina": G("madina", "مَدِينَة", "م د ن", "noun", "city", "şehir", 1, plural="مُدُن"),
 "law": G("law", "لَوْ", None, "part", "if (unreal — imtina' li-imtina')", "eğer …-seydi (imtinâ لَوْ'i)", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this (masc.)", "bu (müzekker)", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come", "gelmek", 1),
 "lam-jawab": G("lam-jawab", "لَ (لَامُ الْجَوَابِ)", None, "part", "the lām that opens the answer of law / qasam", "lev'in / kasemin cevap lâmı", 1),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before (a zarf of time or place)", "önce (zarf)", 1),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these (the plural demonstrative, built on kasra)", "bunlar (çoğul ism-i işâret)", 1),
 "miskin": G("miskin", "مِسْكِين", "س ك ن", "noun", "poor, destitute", "yoksul, miskin", 1, plural="مَسَاكِين"),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (negating ma)", "değil, -medi (nefiy mâ'sı)", 1),
 "sabaqa": G("sabaqa", "سَبَقَ", "س ب ق", "verb", "to precede, to get there first (سَبَقَ يَسْبِقُ)", "önce varmak, öne geçmek", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people, a group", "kavim, topluluk", 1),
 "ijtahada": G("ijtahada", "اِجْتَهَدَ", "ج ه د", "verb", "to strive, to exert oneself (Form VIII)", "çabalamak, gayret etmek (iftiâl)", 1),
 "nasiha": G("nasiha", "نَصِيحَة", "ن ص ح", "noun", "counsel, sincere advice", "nasihat, öğüt", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O! (vocative)", "ey! (nidâ)", 1),
 "nadhir": G("nadhir", "نَذِير", "ن ذ ر", "noun", "a warner", "uyarıcı", 1),
 "mubin": G("mubin", "مُبِين", "ب ي ن", "noun", "clear, making clear (ism fāʿil of أَبَانَ)", "apaçık", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you (pl.) / your (attached)", "siz / sizin (bitişik)", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "my (attached pronoun)", "benim (bitişik)", 1),
 "an-tafsiriyya": G("an-tafsiriyya", "أَنْ (التَّفْسِيرِيَّة)", None, "part", "that is, namely — the explanatory an after a word carrying the sense of saying", "yani — söz mânâsı taşıyan bir kelimeden sonra gelen tefsîriyye en", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek", 1),
 "allah": G("allah", "اللَّه", None, "propn", "Allah", "Allah", 1),
 "ittaqa": G("ittaqa", "اِتَّقَى", "و ق ي", "verb", "to fear (Allah), be wary", "sakınmak, takvâ üzere olmak", 1),
 "ataa": G("ataa", "أَطَاعَ", "ط و ع", "verb", "to obey", "itaat etmek (if'âl, ecvef)", 1),
 "ghafara": G("ghafara", "غَفَرَ", "غ ف ر", "verb", "to forgive, cover over", "bağışlamak", 1),
 "dhanb": G("dhanb", "ذَنْب", "ذ ن ب", "noun", "sin", "günah", 1, plural="ذُنُوب"),
 "akhkhara": G("akhkhara", "أَخَّرَ", "أ خ ر", "verb", "to put back, delay (Form II)", "ertelemek, geri bırakmak (tef'îl)", 1),
 "ajal": G("ajal", "أَجَل", "أ ج ل", "noun", "an appointed term", "ecel, belirlenmiş vakit", 1, plural="آجَال"),
 "musamma": G("musamma", "مُسَمًّى", "س م و", "noun", "the named, name-bearer", "adlandırılmış, belirlenmiş", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come; (with ba) to bring", "gelmek; (bâ ile) getirmek", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ınca", 1),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know", "bilmek", 1),
 "habasa": G("habasa", "حَبَسَ", "ح ب س", "verb", "to hold back, to detain", "hapsetmek, tutmak", 1),
 "an-prep": G("an-prep", "عَنْ", None, "prep", "from, about, away from", "-den, hakkında", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them (attached)", "onlar / onları (bitişik)", 1),
 "matar": G("matar", "مَطَر", "م ط ر", "noun", "rain", "yağmur", 1, plural="أَمْطَار"),
 "ghadiba": G("ghadiba", "غَضِبَ", "غ ض ب", "verb", "to become angry", "gazap etmek, öfkelenmek", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, üzere", 1),
 "qalla": G("qalla", "قَلَّ", "ق ل ل", "verb", "to be few (doubled: قَلَّ يَقِلُّ)", "azalmak, az olmak (muzâaf)", 1),
 "harth": G("harth", "حَرْث", "ح ر ث", "noun", "tilth, tillage", "ekin, tarla", 1),
 "nasl-offspring": G("nasl-offspring", "نَسْل", "ن س ل", "noun", "offspring, progeny", "nesil, döl", 1),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (conditional, governs jazm)", "eğer, -se (cezmeden şart)", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV; آمَنَ بِ)", "iman etmek (if'âl; âmene bi)", 1),
 "radiya": G("radiya", "رَضِيَ", "ر ض و", "verb", "to be pleased with, approve (with بِ)", "razı olmak", 1),
 "zala": G("zala", "زَالَ", "ز و ل", "verb", "to cease, to pass away, to depart (زَالَ يَزُولُ)", "kalkmak, yok olmak, geçip gitmek (ecvef)", 1),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment", "azap", 1),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send", "göndermek", 1),
 "baraka-bless": G("baraka-bless", "بَارَكَ", "ب ر ك", "verb", "to bless (بَارَكَ فِي: to put blessing in)", "bereket vermek (bâreke fî)", 1),
 "rizq": G("rizq", "رِزْق", "ر ز ق", "noun", "provision", "rızık", 1, plural="أَرْزَاق"),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "child, offspring (one or many)", "çocuk", 1, plural="أَوْلَاد"),
 "hamza-istifham": G("hamza-istifham", "أَ (الِاسْتِفْهَام)", None, "part", "the question hamza — what follows it is the thing asked about", "soru hemzesi", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, recognize", "bilmek, tanımak", 1),
 "hadhihi": G("hadhihi", "هَذِهِ", None, "pron", "this (fem.)", "bu (müennes)", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "sign; verse of the Qur'an", "âyet, işaret", 1, plural="آيَات"),
 "hawla": G("hawla", "حَوْلَ", "ح و ل", "noun", "around", "çevresinde, etrafında", 1),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look (at)", "bakmak", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / its (attached pronoun, fem.)", "onun (müennes, bitişik)", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "heaven, sky", "gök", 1),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "land, earth", "yer, toprak", 1, plural="أَرَاضٍ"),
 "shams": G("shams", "شَمْس", "ش م س", "noun", "the sun", "güneş", 1, plural="شُمُوس"),
 "qamar": G("qamar", "قَمَر", "ق م ر", "noun", "moon", "ay", 1, plural="أَقْمَار"),
 "man": G("man", "مَنْ", None, "pron", "who, whoever — the relative and conditional noun", "kim, kimse", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1),
 "samawat": G("samawat", "سَمَاء", "س م و", "noun", "sky, heaven", "gök", 1, plural="سَمَاوَات"),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make, set", "kılmak, yapmak", 1),
 "pron-3fp": G("pron-3fp", "ـهُنَّ", None, "pron", "them / their (f. pl.)", "onlar / onların (müennes çoğul)", 1),
 "nur": G("nur", "نُور", "ن و ر", "noun", "light", "nur, ışık", 1),
 "siraj": G("siraj", "سِرَاج", "س ر ج", "noun", "a lamp", "kandil, lamba", 1, plural="سُرُج"),
 "bisat": G("bisat", "بِسَاط", "ب س ط", "noun", "a carpet, something spread out", "döşek, yaygı", 1),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but — the corrective sister of inna", "fakat — inne'nin istidrâk bildiren kız kardeşi", 1),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "did not (negates, jazm, turns the tense back)", "-medi (nefiy, cezm, kalb)", 1),
 "aqala": G("aqala", "عَقَلَ", "ع ق ل", "verb", "to use one's reason, to understand", "akıl etmek, anlamak", 1),
 "bal": G("bal", "بَلْ", None, "part", "nay, rather", "bilakis, aksine", 1),
 "isba": G("isba", "إِصْبَع", "ص ب ع", "noun", "finger", "parmak", 1, plural="أَصَابِع"),
 "udhun": G("udhun", "أُذُن", "أ ذ ن", "noun", "ear", "kulak", 1, plural="آذَان"),
 "kayfa": G("kayfa", "كَيْفَ", None, "noun", "how? (an interrogative NOUN, not a letter)", "nasıl? (soru ismi)", 1),
 "fahima": G("fahima", "فَهِمَ", "ف ه م", "verb", "to understand", "anlamak", 1),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear, listen", "işitmek, dinlemek", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to will, to want", "dilemek, istemek", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that (masdar-maker, governs nasb)", "-mesi (masdariyye, nasbeder)", 1),
 "lianna": G("lianna", "لِأَنَّ", None, "part", "because", "çünkü", 1),
}
CAND = {k: v for k, v in CAND.items() if v}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
put_morph(mo, "jarraba", _sg.derived(_sg.B2, _sg.W2, "ُ", "جَرَّب", "جَرِّب", "جَرِّب", "تَجْرِبَة", "مُجَرِّب", "مُجَرَّب", "جُرِّبَ", "يُجَرَّبُ", "جَرَّبَ الشَّيْءَ: اخْتَبَرَهُ مَرَّةً بَعْدَ مَرَّةٍ لِيَعْرِفَهُ — يَتَعَدَّى إِلَى مَفْعُولٍ؛ وَمَصْدَرُهُ تَجْرِبَةٌ عَلَى تَفْعِلَة لِأَنَّ لَامَهُ لَيْسَتْ مُعْتَلَّةً وَلَا مَهْمُوزَةً — سَمَاعِيٌّ."))
put_morph(mo, "zala", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "زَال", "زُل", "زُول", "زُل", "زُول", "زُل", "زَوَال", "زَائِل", None, None, None, "زَالَ الشَّيْءُ يَزُولُ زَوَالًا: ذَهَبَ وَانْقَضَى — لَازِمٌ؛ وَهُوَ غَيْرُ «مَا زَالَ» النَّاقِصَةِ (زَالَ يَزَالُ) الَّتِي تَعْمَلُ عَمَلَ كَانَ."))
put_morph(mo, "aqala", _sg.sound1("daraba", "عَقَل", "عْقِل", "اِعْقِل", "عَقْل", "عَاقِل", "مَعْقُول", "عُقِلَ", "يُعْقَلُ", "عَقَلَ الشَّيْءَ يَعْقِلُهُ: فَهِمَهُ وَأَدْرَكَهُ؛ وَعَقَلَ: كَانَ ذَا عَقْلٍ — يَتَعَدَّى وَيَلْزَمُ."))
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch9 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 9 (print pp. 23–25; Nūḥ §15–16): the argument of the rich — what Nūḥ calls to is neither true nor good: «we have found by experience that we are the first in every good thing; the people follow us; good never misses us; had this religion been good it would have come to us before these poor people» — «had it been good they would not have preceded us to it» (46:11); the call of Nūḥ — he counsels: «I am to you a plain warner: worship God, fear Him and obey me; He will forgive you and reprieve you to an appointed term» (71:2–4); God had withheld the rain and tillage and offspring had grown scarce: «if you believe He will be pleased with you, this punishment will depart, He will send the rains and bless you»; «do you not know God? these are His signs around you — the sky and the earth, the sun and the moon; who created the heavens and made the moon a light and the sun a lamp, who created you and made the earth a carpet?»; but they did not reason, did not believe: when he called them they put their fingers in their ears — and how can one understand who does not hear? (s1–s20).")
ADD_TR = (" Dokuzuncu bölüm (basılı s. 23–25; Nûh §15–16): zenginlerin delili — Nûh'un çağırdığı şey ne haktır ne hayır: «tecrübeyle gördük ki her hayırda öncü biziz; insanlar bize tâbidir; hayır bizi ıskalamaz; bu din hayırlı olsaydı bu yoksullardan önce bize gelirdi» — «hayırlı olsaydı ona bizden önce varamazlardı» (46:11); Nûh'un daveti — nasihat eder: «ben size apaçık bir uyarıcıyım: Allah'a kulluk edin, O'ndan sakının, bana itaat edin; sizi bağışlar ve belli bir vakte kadar erteler» (71:2–4); Allah yağmuru tutmuş, ekin ve nesil azalmıştı: «iman ederseniz sizden razı olur, bu azap kalkar, yağmurları gönderir ve bereket verir»; «Allah'ı tanımıyor musunuz? bunlar çevrenizdeki âyetleri — gök ve yer, güneş ve ay; gökleri kim yarattı, ayı nur, güneşi kandil kim kıldı, sizi kim yarattı, yeri döşek kim kıldı?»; fakat akıl etmediler, iman etmediler: çağırınca parmaklarını kulaklarına tıkadılar — işitmeyen nasıl anlar? (s1–s20).")
write_out(9, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §15–16, pp. 23–25", GLOSS_ADD, notes=(), related=())
report(9, S, GLOSS_ADD, ())
