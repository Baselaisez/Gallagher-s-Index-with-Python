# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 11: «سَفِينَةُ نُوحٍ» §18 السَّفِينَةُ (God answers Nūḥ's prayer and wills to drown his people, yet wills that Nūḥ and the believers be saved; He commands a great ship; Nūḥ builds it and the people find a pastime, mocking: «since when a carpenter? did we not tell you not to sit with the lowly? where will this ship walk — in the sand, or up the mountain? the sea is far: will the jinn carry it or the oxen drag it?»; Nūḥ hears it all and endures — «if you mock us, we mock you as you mock», 11:38). Print pp. 27–28.
python3 tools/authoring/author_qisas2_ch11.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: السَّفِينَةُ", "en": "The ship of Nūḥ: the ship", "tr": "Nûh'un gemisi: gemi"}
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
    c = conj_of(full)
    segs = ([seg(c, "wa" if c == "وَ" else "fa", "conj")] if c else []) + [seg(full[(2 if c else 0):-1], stem_lex_part, pos), seg("ا", "pron-1p", "pron")]
    return tok(full, lex, pos, ([AT] if c else []) + list(tags), ar, en, tr, punct=punct, segments=segs)
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

# ---------------------------------------------------------------- § chapter 10's own small helpers
def alf_sana(role_ar="ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — الْعَدَدُ أَلْفٌ يُضَافُ إِلَى مُفْرَدٍ مَجْرُورٍ", en="«a thousand» — a time adverbial by its annexed noun; the number alf takes a singular muḍāf ilayh.", tr="«bin» — zarf; elf sayısı tekil muzâfun ileyh alır.", tags=(MF, ID)):
    return [tok("أَلْفَ", "alf", "noun", list(tags), role_ar + ".", en, tr),
            tok("سَنَةٍ", "sana", "noun", [ID, "tamyiz"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — تَمْيِيزُ الْعَدَدِ.", "«year» — the muḍāf ilayh; the number's tamyīz.", "«yıl» — muzâfun ileyh; sayının temyizi."),
            tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ — الْكَلَامُ تَامٌّ مُوجَبٌ فَالْمُسْتَثْنَى وَاجِبُ النَّصْبِ.", "«less» — the exceptive; the sentence being complete and affirmative, what follows must take naṣb.", "«eksik» — istisnâ edatı; cümle tam ve müsbet olduğundan müstesnâ mansub."),
            tok("خَمْسِينَ", "khamsun", "noun", [IST, JS], "مُسْتَثْنًى مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ (أَلْفَاظُ الْعُقُودِ).", "«fifty» — the excepted, naṣb by the yāʾ: the tens decline like the sound plural.", "«elli» — müstesnâ; ukûd lafızları cemi müzekker sâlime mülhak, yâ ile mansub."),
            tok("عَامًا", "aam-year", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — تَمْيِيزُ الْعُقُودِ مُفْرَدٌ مَنْصُوبٌ.", "«years» — the tamyīz of the tens: singular, in naṣb.", "«yıl» — ukûdun temyizi: tekil, mansub.")]
def ila_mata(fa=False):
    return [tok("فَإِلَى" if fa else "إِلَى", "ila", "prep", ([AT] if fa else []) + [HJ, IS], ("الْفَاءُ لِلتَّفْرِيعِ، وَ" if fa else "") + "إِلَى حَرْفُ جَرٍّ.", ("«so» + " if fa else "") + "«until»", ("«o hâlde» + " if fa else "") + "«-e kadar»", segments=([seg("فَ", "fa", "conj"), seg("إِلَى", "ila", "prep")] if fa else None)),
            tok("مَتَى", "mata-istifham", "pron", [IS, HJ], "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِإِلَى.", "«when» — the question noun of time, in the place of jarr after ilā.", "«ne zamana» — zaman soru ismi; ilâ'dan sonra mahallen mecrûr.")]
def yara_(tags=(MB,)): return tok("يَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«will he see» — the ḍamma estimated on the alif.", "«görecek» — damme elif üzerinde takdîrî.")
def wa_lam(): return tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not» — lam.", "«ve … -medi» — lem.", segments=wa_("لَمْ", "lam-jazima", "part"))
def allahu_akbar(punct):
    return [tok("اللهُ", "allah", "propn", [MK], "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«God» — the mubtadaʾ.", "«Allah» — mübtedâ."),
            tok("أَكْبَرُ", "akbar", "noun", [MK, "ism-tafdil", MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«[is] greatest» — the khabar; the elative, a diptote.", "«en büyüktür» — haber; ism-i tafdil, gayr-i munsarıf.", punct=punct)]
def innahu(sha=False):
    return tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ " + ("ضَمِيرُ الشَّأْنِ اسْمُهَا" if sha else "ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا") + ".", ("«indeed [it is so that]» — inna with the pronoun of the matter as its ism." if sha else "«indeed he» — inna + its ism."), ("«şu muhakkak ki» — inne + ismi olan şe'n zamiri." if sha else "«şüphesiz o» — inne + ismi."), segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")])

# ---------------------------------------------------------------- § chapter 11's own small helpers
def safina_kabira(punct=None):
    return [maful_("سَفِينَةً", "safina", "«a ship»", "«bir gemi»"), naat("كَبِيرَةً", "kabir", "«great»", "«büyük»", case="nasb", punct=punct)]
def ya_nuhu(punct=None):
    return [tok("يَا", "ya-nida", "part", [VM], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
            tok("نُوحُ", "nuh", "propn", [VM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Nūḥ» — a single proper name called: built on ḍamma, in the place of naṣb.", "«Nûh» — müfred alem münâdâ; damme üzere mebnî, mahallen mansub.", punct=punct)]
def sirta_najjaran(full="صِرْتَ", fa=False, punct=None):
    return [tok(("فَ" if fa else "") + full, "sara", "verb", ([AT] if fa else []) + [KN, "hollow-verbs"], ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "") + "صِرْتَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ اسْمُهُ — أَجْوَفُ حُذِفَتْ عَيْنُهُ (صِرْتَ).", ("«so» + " if fa else "") + "«you have become» — ṣāra before the tāʾ, its ism; the hollow verb drops its middle.", ("«ve böylece» + " if fa else "") + "«oldun» — tâ'dan önce sâra; tâ ismi; ecvef ortasını düşürür.", segments=([seg("فَ", "fa", "conj")] if fa else []) + [seg("صِرْ", "sara", "verb"), seg("تَ", "pron-2ms", "pron")]),
            tok("نَجَّارًا", "najjar", "noun", [KN, "sighat-mubalagha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ — فَعَّالٌ لِلْحِرْفَةِ.", "«a carpenter» — ṣāra's khabar; the فَعَّال of trades.", "«bir marangoz» — sâra'nın haberi; meslek bildiren fa''âl.", punct=punct)]
def a_tamshi_hadhihi(wa=False):
    return [tok("أَتَمْشِي", "masha", "verb", [IS, "mudari-marfu", "naqis-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَتَمْشِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ بَعْدَهُ.", "«does … walk» — the question hamza; the defective muḍāriʿ; the doer follows.", "«… yürür mü» — soru hemzesi; nâkıs muzâri; fâil sonra.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَمْشِي", "masha", "verb")]),
            tok("هٰذِهِ", "hadhihi", "pron", [FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this [one]» — the doer.", "«bu» — fâil.")]
def am_(punct=None): return tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ لِلتَّعْيِينِ بَعْدَ هَمْزَةِ الِاسْتِفْهَامِ (الْمُتَّصِلَةُ).", "«or» — the am of choice after the question hamza.", "«yoksa» — soru hemzesinden sonra tayin bildiren em.", punct=punct)
def mudari_fail_after_(full, lex, en, tr, punct=None, tags=()): return tok(full, lex, "verb", ["mudari-marfu"] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.", en + " — a muḍāriʿ; the doer follows.", tr + " — muzâri; fâil sonra.", punct=punct)
def mudari_pron_fail_after(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "verb", ["mudari-marfu", MB] + list(tags), "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.", en + " — the object pronoun aboard; the doer follows.", tr + " — mef'ûl zamir bitişik; fâil sonra.", punct=punct, segments=[seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")])
def kana_nuh_yasmau():
    return [kana(), nuh_ism_kana(),
            mudari("يَسْمَعُ", "samia", "«used to hear»", "«işitirdi»", tags=[KN, MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ")]

# ---------------------------------------------------------------- §18 السَّفِينَةُ (print pp. 27–28)
sen("s1", "And God answered the prayer of Nūḥ and willed to drown his people.", "Allah Nûh'un duasını kabul etti ve kavmini boğmayı diledi.", [
  mazi("وَأَجَابَ", "ajaba", "«and answered»", "«ve kabul etti»", tags=[AT, "form-iv-verbs", "hollow-verbs"], hidden=None, wa=True),
  allah_fail(),
  tok("دَعْوَةَ", "dawa", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the prayer [of]» — the object, annexed.", "«duasını» — mef'ûl, muzâf."),
  tok("نُوحٍ", "nuh", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ»", "«Nûh'un»"),
  mazi("وَأَرَادَ", "arada", "«and willed»", "«ve diledi»", tags=[AT, "form-iv-verbs", "hollow-verbs"], wa=True),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِأَرَادَ", "«to»", "«-meyi»"),
  mansub("يُغْرِقَ", "aghraqa", "«drown»", "«boğmayı»", tags=["form-iv-verbs"]),
  qawm_pron("قَوْمَهُ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the object.", "«kavmini» — mef'ûl.", tags=[MB, ID], punct="."),
])
sen("s2", "But God wills likewise that Nūḥ and the believers be saved.", "Fakat Allah aynı şekilde Nûh'un ve mü'minlerin kurtulmasını da diler.", [
  tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kız kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  allah_ism(part="لٰكِنَّ"),
  mudari("يُرِيدُ", "arada", "«wills»", "«diler»", tags=[IW, MB, "form-iv-verbs", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  tok("كَذٰلِكَ", "kadhalika", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ (أَوِ اسْمٌ بِمَعْنَى مِثْلَ)، وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — بِمَعْنَى أَيْضًا.", "«likewise» — ka + the demonstrative: «so too».", "«aynı şekilde» — kâf + ism-i işâret: «öylece».", segments=None),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيُرِيدُ", "«that»", "«-masını»"),
  tok("يَنْجُوَ", "naja-escape", "verb", [AN, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْوَاوِ، وَالْفَاعِلُ بَعْدَهُ — نَاقِصٌ وَاوِيٌّ (نَجَا يَنْجُو).", "«be saved» — naṣb by an; the defective wāw shows its fatḥa; the doer follows.", "«kurtulmasını» — en ile mansub; nâkıs vâv fethasını gösterir; fâil sonra."),
  nuh_fail(),
  tok("وَالْمُؤْمِنُونَ", "mumin", "noun", [AT, JS, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَالْمُؤْمِنُونَ مَعْطُوفٌ عَلَى الْفَاعِلِ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the believers» — joined to the doer; rafʿ by the wāw.", "«ve mü'minler» — fâile ma'tûf; vâv ile merfû.", punct=".", segments=wa_("الْمُؤْمِنُونَ", "mumin", "noun")),
])
sen("s3", "So He commanded Nūḥ to make a great ship.", "Bunun üzerine Nûh'a büyük bir gemi yapmasını emretti.", [
  mazi("فَأَمَرَ", "amara-command", "«so He commanded»", "«bunun üzerine emretti»", tags=[AT, MB], wa=True),
  nuh_maful(),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِأَمَرَ (أَوْ مَجْرُورٌ بِبَاءٍ مَحْذُوفَةٍ: بِأَنْ يَصْنَعَ)", "«to»", "«-masını»"),
  mansub("يَصْنَعَ", "sanaa", "«make»", "«yapmasını»"),
  *safina_kabira(punct="."),
])
sen("s4", "And Nūḥ began to make a great ship.", "Nûh büyük bir gemi yapmaya başladı.", [
  mazi("وَبَدَأَ", "badaa", "«and began»", "«ve başladı»", tags=[AT, KN], hidden=None, wa=True, extra_ar=" — مِنْ أَفْعَالِ الشُّرُوعِ، تَعْمَلُ عَمَلَ كَانَ وَخَبَرُهَا جُمْلَةٌ مُضَارِعِيَّةٌ"),
  nuh_ism_kana(),
  mudari("يَصْنَعُ", "sanaa", "«to make»", "«yapmaya»", tags=[KN, MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ بَدَأَ"),
  *safina_kabira(punct="."),
])
sen("s5", "And his people saw him at this work and found a pastime.", "Kavmi onu bu işte gördü ve eğlence buldu.", [
  v_pron("وَرَآهُ", "raa", "رَآ", "هُ", "pron-3ms", "«and … saw him» — the defective māḍī before the pronoun; the doer follows.", "«ve onu gördü» — zamirden önce nâkıs mâzî; fâil sonra.", hidden=None, wa=True, tags=["naqis-verbs"]),
  qawm_pron("قَوْمُهُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the doer.", "«kavmi» — fâil.", tags=[FL, ID]),
  fi(),
  tok("هٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«this» — after fī.", "«bu» — fî'den sonra."),
  tok("الشُّغْلِ", "shughl", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«work» — a badal of the demonstrative.", "«işte» — ism-i işâretten bedel."),
  mazi_pl("فَوَجَدُوا", "wajada", "«and they found»", "«ve buldular»", tags=[AT, MB, "mithal-verbs"], wa=True),
  maful("شُغْلًا", "shughl", "«a pastime»", "«bir eğlence»", punct=".", extra_ar=" — الشُّغْلُ الْأَوَّلُ الْعَمَلُ وَالثَّانِي مَا يَشْغَلُ وَيُلْهِي"),
])
sen("s6", "And they took to mocking him.", "Ve onunla alay etmeye başladılar.", [
  saru(),
  khamsa("يَسْخَرُونَ", "sakhira", "«mocking»", "«alay ediyorlar»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ"),
  tok("مِنْهُ", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — سَخِرَ مِنْهُ.", "«him» — sakhira takes min.", "«onunla» — sahire min alır.", punct=".", segments=[seg("مِنْ", "min", "prep"), seg("هُ", "pron-3ms", "pron")]),
])
sen("s7", "What is this, O Nūḥ? Since when have you become a carpenter?", "Bu ne, ey Nûh? Ne zamandan beri marangoz oldun?", [
  tok("مَا", "ma-istifham", "pron", [IS, MK], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the question word; the mubtadaʾ.", "«ne» — soru ismi; mübtedâ."),
  tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "«[is] this» — the khabar.", "«bu» — haber."),
  *ya_nuhu(punct="؟"),
  prep("مِنْ", "min", "«since»", "«-den beri»"),
  tok("مَتَى", "mata-istifham", "pron", [IS, HJ], "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِمِنْ.", "«when» — the question noun of time, in the place of jarr after min.", "«ne zaman» — zaman soru ismi; min'den sonra mahallen mecrûr."),
  *sirta_najjaran(punct="؟"),
])
sen("s8", "Did we not use to tell you: do not sit with these lowly people?", "Sana «bu ayak takımıyla oturma» demez miydik?", [
  tok("أَمَا", "ama", "part", [IS, "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَمَا نَافِيَةٌ.", "«did … not» — the question hamza of affirmation + the negating mā.", "«… -mez miydik» — takrîrî istifham hemzesi + nefiy mâ'sı.", segments=[seg("أَ", "hamza-istifham", "part"), seg("مَا", "ma-nafiya", "part")]),
  tok("كُنَّا", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا اسْمُهُ — أُدْغِمَتْ نُونُ الْفِعْلِ فِي نُونِ الضَّمِيرِ.", "«we used to» — kāna before nā, its ism; the two nūns merge.", "«idik» — nâ'dan önce kâne; nâ ismi; iki nûn idgam.", segments=[seg("كُ", "kana", "verb"), seg("نَّا", "pron-1p", "pron")]),
  tok("نَقُولُ", "qala", "verb", [KN, "mudari-marfu", "hollow-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: نَحْنُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ، وَمَقُولُ الْقَوْلِ مَفْعُولُهُ.", "«tell» — the clause is kāna's khabar; what is said is its object.", "«derdik» — cümle kâne'nin haberi; söylenen söz mef'ûlü."),
  li_pron("لَكَ", "كَ", "pron-2ms", "«you»", "«sana»"),
  tok("لَا", "la-nahiya", "part", ["la-nahiya"], "لَا النَّاهِيَةُ تَجْزِمُ الْمُضَارِعَ.", "«do not» — the prohibitive lā.", "«-me» — nehiy lâ'sı."),
  tok("تَجْلِسْ", "jalasa", "verb", ["la-nahiya"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«sit» — jazm by the prohibitive lā.", "«oturma» — nehiy lâ'sıyla meczûm."),
  ila_(),
  haulai("jarr", "بِإِلَى", "«these» — after ilā.", "«bu» — ilâ'dan sonra.", tags=[HJ]),
  tok("الْأَرَاذِلِ", "ardhal", "noun", [BD, JT, MM], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ أَرْذَلَ عَلَى أَفَاعِلَ، مَمْنُوعٌ مِنَ الصَّرْفِ، يُجَرُّ بِالْكَسْرَةِ لِدُخُولِ ال.", "«lowly people» — a badal; the diptote plural takes kasra under al.", "«ayak takımı» — bedel; gayr-i munsarıf cem, lâm-ı ta'rîf ile kesre alır.", punct="."),
])
sen("s9", "But you did not heed our words, and you sat with the carpenters and the smiths, and so you have become a carpenter!", "Fakat sen sözümüzü dinlemedin, marangozlarla ve demircilerle oturdun ve böylece marangoz oldun!", [
  tok("وَلٰكِنَّكَ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ اسْمُهَا.", "«but you» — lākinna + the kāf, its ism.", "«fakat sen» — lâkinne + ismi olan kâf.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not»", "«-medin»"),
  tok("سَمِعْتَ", "samia", "verb", [IW, "la-nafiya", MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ.", "«you heeded» — the doer's tāʾ; the clause is lākinna's khabar.", "«dinledin» — fâil tâ'sı; cümle lâkinne'nin haberi.", segments=[seg("سَمِعْ", "samia", "verb"), seg("تَ", "pron-2ms", "pron")]),
  noun_pron("كَلَامَنَا", "kalam", "كَلَامَ", "نَا", "pron-1p", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our words» — the object.", "«sözümüzü» — mef'ûl.", tags=[MB, ID]),
  tok("وَجَلَسْتَ", "jalasa", "verb", [AT], "الْوَاوُ عَاطِفَةٌ، وَجَلَسْتَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ.", "«and you sat»", "«ve oturdun»", segments=[seg("وَ", "wa", "conj"), seg("جَلَسْ", "jalasa", "verb"), seg("تَ", "pron-2ms", "pron")]),
  ila_(),
  tok("النَّجَّارِينَ", "najjar", "noun", [HJ, JS, "sighat-mubalagha"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — فَعَّالٌ لِلْحِرْفَةِ.", "«the carpenters» — jarr by the yāʾ.", "«marangozlarla» — yâ ile mecrûr."),
  tok("وَالْحَدَّادِينَ", "haddad", "noun", [AT, JS, "sighat-mubalagha"], "الْوَاوُ عَاطِفَةٌ، وَالْحَدَّادِينَ مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the smiths» — joined; jarr by the yāʾ.", "«ve demircilerle» — ma'tûf; yâ ile mecrûr.", segments=wa_("الْحَدَّادِينَ", "haddad", "noun")),
  *sirta_najjaran(fa=True, punct="!"),
])
sen("s10", "And where will this ship walk, O Nūḥ? Your whole affair is a wonder.", "Bu gemi nereye yürüyecek, ey Nûh? Senin işin baştan sona bir hayret!", [
  tok("وَأَيْنَ", "ayna", "pron", [AT, IS, MF], "الْوَاوُ عَاطِفَةٌ، وَأَيْنَ اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«and where» — the question noun of place, an adverbial.", "«ve nereye» — mekân soru ismi, zarf.", segments=wa_("أَيْنَ", "ayna", "pron")),
  mudari_fail_after_("تَمْشِي", "masha", "«will … walk»", "«yürüyecek»", tags=["naqis-verbs"]),
  tok("هٰذِهِ", "hadhihi", "pron", [FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«this» — the doer.", "«bu» — fâil."),
  tok("السَّفِينَةُ", "safina", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "«ship» — a badal.", "«gemi» — bedel."),
  *ya_nuhu(punct="؟"),
  inna(),
  noun_pron("أَمْرَكَ", "amr", "أَمْرَ", "كَ", "pron-2ms", "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your affair» — inna's ism.", "«senin işin» — inne'nin ismi.", tags=[IW, ID]),
  noun_pron("كُلَّهُ", "kull", "كُلَّ", "هُ", "pron-3ms", "تَوْكِيدٌ مَعْنَوِيٌّ لِاسْمِ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ إِلَى ضَمِيرٍ يَعُودُ عَلَى الْمُؤَكَّدِ.", "«all of it» — the emphasis of inna's ism, annexed to a pronoun returning to it.", "«baştan sona» — inne'nin isminin manevî tekidi; mükkede dönen zamire muzâf.", tags=[TW, ID]),
  khabar_inna("عَجَبٌ", "ajab", "«[is] a wonder»", "«bir hayrettir»", punct="."),
])
sen("s11", "Will this walk in the sand, or climb the mountain?", "Bu kumda mı yürüyecek, yoksa dağa mı tırmanacak?", [
  *a_tamshi_hadhihi(),
  fi(), majrur("الرَّمْلِ", "raml", "«the sand»", "«kumda»"),
  am_(),
  mudari("تَصْعَدُ", "saada-climb", "«climb»", "«tırmanacak»", hidden="هِيَ", tags=[IS, MB]),
  maful("الْجَبَلَ", "jabal", "«the mountain»", "«dağa»", punct="؟"),
])
sen("s12", "The sea is very far from here: will the jinn carry it, or will the oxen drag it?", "Deniz buradan çok uzak: onu cinler mi taşıyacak, yoksa öküzler mi çekecek?", [
  tok("الْبَحْرُ", "bahr", "noun", [MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the sea» — the mubtadaʾ.", "«deniz» — mübtedâ."),
  prep("مِنْ", "min", "«from»", "«-dan»"),
  tok("هُنَا", "huna", "noun", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِمِنْ.", "«here» — the demonstrative of place, after min.", "«burası» — mekân ism-i işâreti; min'den sonra."),
  khabar("بَعِيدٌ", "baid", "«[is] far»", "«uzaktır»", tags=["sifa-mushabbaha"]),
  tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (يَبْعُدُ جِدًّا).", "«very» — stands in for the mafʿūl muṭlaq.", "«çok» — mef'ûl-i mutlakın nâibi.", punct="،"),
  tok("هَلْ", "hal-istifham", "part", [IS], "حَرْفُ اسْتِفْهَامٍ.", "«?» — the question particle.", "«mı» — soru harfi."),
  mudari_pron_fail_after("يَحْمِلُهَا", "hamala", "يَحْمِلُ", "هَا", "pron-3fs", "«will carry it»", "«onu taşıyacak»", tags=[IS]),
  fail("الْجِنُّ", "jinn", "«the jinn»", "«cinler»"),
  am_(),
  mudari_pron_fail_after("تَجُرُّهَا", "jarra", "تَجُرُّ", "هَا", "pron-3fs", "«will drag it» — the doubled verb.", "«onu çekecek» — muzâaf fiil.", tags=[IS, "doubled-verbs"]),
  fail("الثِّيرَانُ", "thawr", "«the oxen»", "«öküzler»", tags=[JT], punct="؟", extra_ar=" — جَمْعُ ثَوْرٍ"),
])
sen("s13", "And Nūḥ used to hear all that and endure — and he had heard worse than this and endured!", "Nûh bütün bunları işitir ve sabrederdi — bundan daha ağırını da işitmiş ve sabretmişti!", [
  *kana_nuh_yasmau(),
  tok("كُلَّ", "kull", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«all [of]» — the object, annexed.", "«bütün» — mef'ûl, muzâf."),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that» — the muḍāf ilayh.", "«bunları» — muzâfun ileyh."),
  mudari_wa("وَيَصْبِرُ", "sabara", "«and endure»", "«ve sabrederdi»", tags=[KN], extra=" — مَعْطُوفٌ عَلَى جُمْلَةِ الْخَبَرِ", punct="،"),
  tok("وَقَدْ", "qad", "part", [AT, QD], "الْوَاوُ لِلْحَالِ (أَوْ عَاطِفَةٌ)، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — the wāw of the ḥāl + qad.", "«ve gerçekten» — hâl vâvı + kad.", segments=wa_("قَدْ", "qad", "part")),
  mazi("سَمِعَ", "samia", "«he had heard»", "«işitmişti»", tags=[MB, HL]),
  tok("أَشَدَّ", "ashadd", "noun", [MB, "ism-tafdil", MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«worse» — the object; the elative, a diptote.", "«daha ağırını» — mef'ûl; ism-i tafdil, gayr-i munsarıf."),
  prep("مِنْ", "min", "«than»", "«-dan»"),
  tok("هٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«this»", "«bundan»"),
  mazi("فَصَبَرَ", "sabara", "«and endured»", "«ve sabretti»", tags=[AT], wa=True, punct="!"),
])
sen("s14", "But he used to say to them at times: «if you mock us, we mock you as you mock» (11:38).", "Fakat onlara bazen derdi: «bizimle alay ederseniz, siz nasıl alay ediyorsanız biz de sizinle alay ederiz» (11:38).", [
  tok("وَلٰكِنَّهُ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«but he» — lākinna + the hāʾ, its ism.", "«fakat o» — lâkinne + ismi olan hâ.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُ", "pron-3ms", "pron")]),
  kana("كَانَ", wa=False),
  tok("يَقُولُ", "qala", "verb", [KN, IW, "mudari-marfu", "hollow-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ، وَجُمْلَةُ كَانَ خَبَرُ لٰكِنَّ.", "«say» — kāna's khabar; the kāna clause is lākinna's khabar.", "«derdi» — kâne'nin haberi; kâne cümlesi lâkinne'nin haberi."),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»"),
  tok("أَحْيَانًا", "ahyanan", "noun", [MF, JT], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ حِينٍ.", "«at times» — a time adverbial; the plural of ḥīn.", "«bazen» — zaman zarfı; hîn'in cem'i.", punct=":"),
  *quran([
    tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
    tok("تَسْخَرُوا", "sakhira", "verb", [SH, AK], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«you mock» — the condition's verb, jazm by the dropped nūn.", "«alay ederseniz» — şart fiili; nûnun hazfiyle meczûm."),
    tok("مِنَّا", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — أُدْغِمَتْ نُونُ مِنْ فِي نُونِ الضَّمِيرِ.", "«at us» — the two nūns merge.", "«bizimle» — iki nûn idgam.", segments=[seg("مِ", "min", "prep"), seg("نَّا", "pron-1p", "pron")]),
    na_pron("فَإِنَّا", "inna", "part", "inna", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَنَا اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "«then we» — the fāʾ of the answer + inna + nā.", "«o zaman biz» — cevap fâ'sı + inne + nâ.", tags=[IW, SH]),
    mudari1("نَسْخَرُ", "sakhira", "«mock»", "«alay ederiz»", "نَحْنُ", tags=[IW], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
    tok("مِنْكُمْ", "min", "prep", [HJ], "مِنْ حَرْفُ جَرٍّ، وَكُمْ فِي مَحَلِّ جَرٍّ.", "«at you»", "«sizinle»", segments=[seg("مِنْ", "min", "prep"), seg("كُمْ", "pron-2mp", "pron")]),
    tok("كَمَا", "kama", "part", [HJ, "maful-mutlaq"], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ، وَالْجَارُّ وَالْمَجْرُورُ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ (سُخْرِيَةً كَسُخْرِيَتِكُمْ).", "«as» — ka + the maṣdar-mā; the phrase stands in for the mafʿūl muṭlaq.", "«… gibi» — kâf + masdariyye mâ; ibare mef'ûl-i mutlakın nâibi."),
    khamsa("تَسْخَرُونَ", "sakhira", "«you mock»", "«alay ediyorsunuz»", punct="."),
  ]),
])

CAND = {
 "ajaba": G("ajaba", "أَجَابَ", "ج و ب", "verb", "to answer, accept (an invitation)", "cevap vermek, kabul etmek (if'âl, ecvef)", 1),
 "allah": G("allah", "اللَّه", None, "propn", "Allah", "Allah", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "supplication, call", "dua, davet", 1, plural="دَعَوَات"),
 "nuh": G("nuh", "نُوح", None, "propn", "Nūḥ (Noah)", "Nûh", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to will, to want", "dilemek, istemek", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that (masdar-maker, governs nasb)", "-mesi (masdariyye, nasbeder)", 1),
 "aghraqa": G("aghraqa", "أَغْرَقَ", "غ ر ق", "verb", "to drown (someone), to sink (Form IV)", "boğmak, batırmak (if'âl)", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people, a group", "kavim, topluluk", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "his / its (attached pronoun)", "onun (bitişik)", 1),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but — the corrective sister of inna", "fakat — inne'nin istidrâk bildiren kız kardeşi", 1),
 "kadhalika": G("kadhalika", "كَذَلِكَ", None, "part", "likewise, so too (ka + dhalika)", "böylece, aynı şekilde", 1),
 "naja-escape": G("naja-escape", "نَجَا", "ن ج و", "verb", "to be saved, to escape (نَجَا يَنْجُو)", "kurtulmak (nâkıs vâvî)", 1),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "believer (ism fa'il of Form IV)", "mü'min, inanan", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, for (fa)", "bunun üzerine", 1),
 "amara-command": G("amara-command", "أَمَرَ", "أ م ر", "verb", "to command, to order (its amr is مُرْ)", "emretmek (emri مُرْ)", 1),
 "sanaa": G("sanaa", "صَنَعَ", "ص ن ع", "verb", "to make, to manufacture", "yapmak, imal etmek", 1),
 "safina": G("safina", "سَفِينَة", "س ف ن", "noun", "ship", "gemi", 1, plural="سُفُن"),
 "kabir": G("kabir", "كَبِير", "ك ب ر", "noun", "big; great", "büyük", 1, plural="كِبَار"),
 "badaa": G("badaa", "بَدَأَ", "ب د أ", "verb", "to begin", "başlamak", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this (masc.)", "bu (müzekker)", 1),
 "shughl": G("shughl", "شُغْل", "ش غ ل", "noun", "work, occupation; a pastime", "iş, meşguliyet; eğlence", 1, plural="أَشْغَال"),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find; (passive) to be found", "bulmak", 1),
 "sara": G("sara", "صَارَ", "ص ي ر", "verb", "to become (a sister of كان)", "olmak (kâne'nin kız kardeşi)", 1),
 "sakhira": G("sakhira", "سَخِرَ", "س خ ر", "verb", "to mock, to ridicule (سَخِرَ مِنْ)", "alay etmek (sahire min)", 1),
 "min": G("min", "مِنْ", None, "prep", "from; than (with ism tafdil)", "-den", 1),
 "ma-istifham": G("ma-istifham", "مَا (الِاسْتِفْهَامِيَّة)", None, "pron", "what? (the question mā)", "ne? (soru mâ'sı)", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O! (vocative)", "ey! (nidâ)", 1),
 "mata-istifham": G("mata-istifham", "مَتَى", None, "pron", "when? (interrogative; the same word also conditions)", "ne zaman? (soru ismi)", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you (masc. sg., attached)", "sen / senin (bitişik)", 1),
 "najjar": G("najjar", "نَجَّار", "ن ج ر", "noun", "carpenter (the فَعَّال of trades)", "marangoz (meslek bildiren fa''âl)", 1, plural="نَجَّارُونَ"),
 "ama": G("ama", "أَمَا", None, "part", "did … not? (the question hamza over the negating mā)", "… -medi mi? (nefiy mâ'sı üzerine soru hemzesi)", 1),
 "hamza-istifham": G("hamza-istifham", "أَ (الِاسْتِفْهَام)", None, "part", "the question hamza — what follows it is the thing asked about", "soru hemzesi", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (negating ma)", "değil, -medi (nefiy mâ'sı)", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we, us (attached)", "biz, bizi (bitişik)", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "do not — the prohibitive la", "-me — nehiy lâ'sı", 1),
 "jalasa": G("jalasa", "جَلَسَ", "ج ل س", "verb", "to sit", "oturmak", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these (the plural demonstrative, built on kasra)", "bunlar (çoğul ism-i işâret)", 1),
 "ardhal": G("ardhal", "أَرْذَل", "ر ذ ل", "noun", "lowest, most base (ism tafdil)", "en aşağı, en alçak (ism-i tafdil)", 1, plural="أَرَاذِل"),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear, listen", "işitmek, dinlemek", 1),
 "kalam": G("kalam", "كَلَام", "ك ل م", "noun", "speech (masdar)", "söz, kelâm", 1),
 "haddad": G("haddad", "حَدَّاد", "ح د د", "noun", "smith, blacksmith (the فَعَّال of trades)", "demirci (meslek bildiren fa''âl)", 1, plural="حَدَّادُونَ"),
 "ayna": G("ayna", "أَيْنَ", None, "pron", "where?", "nerede, nereye?", 1),
 "masha": G("masha", "مَشَى", "م ش ي", "verb", "to walk", "yürümek", 1),
 "hadhihi": G("hadhihi", "هَذِهِ", None, "pron", "this (fem.)", "bu (müennes)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed, verily", "şüphesiz", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "matter, affair", "iş, mesele", 1, plural="أُمُور"),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every; the whole of it", "her, bütün", 1),
 "ajab": G("ajab", "عَجَب", "ع ج ب", "noun", "a wonder, astonishment", "hayret, şaşılacak şey", 1),
 "raml": G("raml", "رَمْل", "ر م ل", "noun", "sand", "kum", 1, plural="رِمَال"),
 "am": G("am", "أَمْ", None, "part", "or…? (the ta'yin connective, paired with the question hamza)", "yoksa …? (soru hemzesiyle eşli em)", 1),
 "saada-climb": G("saada-climb", "صَعِدَ", "ص ع د", "verb", "to climb, ascend", "tırmanmak, çıkmak", 1),
 "jabal": G("jabal", "جَبَل", "ج ب ل", "noun", "mountain", "dağ", 1, plural="جِبَال"),
 "bahr": G("bahr", "بَحْر", "ب ح ر", "noun", "sea", "deniz", 1, plural="بِحَار"),
 "huna": G("huna", "هُنَا", None, "noun", "here (the demonstrative of place)", "burada (mekân ism-i işâreti)", 1),
 "baid": G("baid", "بَعِيد", "ب ع د", "noun", "far, distant", "uzak", 1),
 "jiddan": G("jiddan", "جِدًّا", "ج د د", "noun", "very, very much (an absolute object used adverbially)", "çok, pek", 1),
 "hal-istifham": G("hal-istifham", "هَلْ", None, "part", "…? (yes/no question)", "mı/mi? (soru harfi)", 1),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry; to construe one wording by another", "taşımak", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / its (attached pronoun, fem.)", "onun (müennes, bitişik)", 1),
 "jinn": G("jinn", "جِنّ", "ج ن ن", "noun", "the jinn", "cinler", 1),
 "jarra": G("jarra", "جَرَّ", "ج ر ر", "verb", "to drag; to put in the genitive (doubled)", "çekmek, sürüklemek; cer etmek (muzâaf)", 1),
 "thawr": G("thawr", "ثَوْر", "ث و ر", "noun", "a bull; the wild bull (oryx)", "öküz, boğa", 1, plural="ثِيرَان"),
 "dhalika": G("dhalika", "ذَلِكَ", None, "pron", "that (masc.)", "şu, o (müzekker)", 1),
 "sabara": G("sabara", "صَبَرَ", "ص ب ر", "verb", "to be patient", "sabretmek", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed (before a past verb)", "gerçekten (mâzîden önce tahkik)", 1),
 "ashadd": G("ashadd", "أَشَدّ", "ش د د", "noun", "most intense, greatest", "daha şiddetli, en şiddetli", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them (attached)", "onlar / onları (bitişik)", 1),
 "ahyanan": G("ahyanan", "أَحْيَانًا", "ح ي ن", "noun", "at times, sometimes", "bazen", 1),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (conditional, governs jazm)", "eğer, -se (cezmeden şart)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you (pl.) / your (attached)", "siz / sizin (bitişik)", 1),
 "kama": G("kama", "كَمَا", None, "part", "as, just as (ka + the masdar-ma)", "… gibi, nasıl ki (kâf + masdariyye mâ)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
put_morph(mo, "aghraqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَغْرَق", "غْرِق", "أَغْرِق", "إِغْرَاق", "مُغْرِق", "مُغْرَق", "أُغْرِقَ", "يُغْرَقُ", "أَغْرَقَهُ فِي الْمَاءِ: جَعَلَهُ يَغْرَقُ — بَابُ الْإِفْعَالِ، مُتَعَدٍّ مِنْ غَرِقَ اللَّازِمِ."))
put_morph(mo, "naja-escape", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "نَجَ", "نْج", "u", "اُنْج", "نَجَاة", "نَاجٍ (النَّاجِي)", None, None, None, "نَجَا مِنَ الْخَطَرِ يَنْجُو نَجَاةً: سَلِمَ وَخَلَصَ — لَازِمٌ، يَتَعَدَّى بِمِنْ."))
put_morph(mo, "amara-command", _sg.sound1("nasara", "أَمَر", "أْمُر", "مُر", "أَمْر", "آمِر", "مَأْمُور", "أُمِرَ", "يُؤْمَرُ", "أَمَرَهُ بِالشَّيْءِ يَأْمُرُهُ: طَلَبَ مِنْهُ فِعْلَهُ — مَهْمُوزُ الْفَاءِ؛ أَمْرُهُ مُرْ (حُذِفَتْ هَمْزَتُهُ مَعَ هَمْزَةِ الْوَصْلِ تَخْفِيفًا)، وَيَجُوزُ اؤْمُرْ بَعْدَ الْوَاوِ وَالْفَاءِ."))
put_morph(mo, "sanaa", _sg.sound1("fataha", "صَنَع", "صْنَع", "اِصْنَع", "صُنْع", "صَانِع", "مَصْنُوع", "صُنِعَ", "يُصْنَعُ", "صَنَعَ الشَّيْءَ يَصْنَعُهُ: عَمِلَهُ — يَتَعَدَّى إِلَى مَفْعُولٍ."))
put_morph(mo, "sakhira", _sg.sound1("samia", "سَخِر", "سْخَر", "اِسْخَر", "سُخْرِيَة", "سَاخِر", None, None, None, "سَخِرَ مِنْهُ يَسْخَرُ سُخْرِيَةً: هَزِئَ بِهِ — لَازِمٌ، يَتَعَدَّى بِمِنْ."))
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch11 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 11 (print pp. 27–28; Nūḥ §18): the ship — God answers Nūḥ's prayer and wills to drown his people, yet wills that Nūḥ and the believers be saved; He commands a great ship; Nūḥ builds it and his people find a pastime, mocking him: «what is this, O Nūḥ — since when a carpenter? did we not tell you not to sit with the lowly? you sat with the carpenters and the smiths and became one; where will this ship walk — in the sand, or up the mountain? the sea is far: will the jinn carry it or the oxen drag it?»; Nūḥ hears it all and endures — he had heard worse; at times he answers «if you mock us, we mock you as you mock» (11:38) (s1–s14).")
ADD_TR = (" On birinci bölüm (basılı s. 27–28; Nûh §18): gemi — Allah Nûh'un duasını kabul eder, kavmini boğmayı diler; fakat Nûh ile mü'minlerin kurtulmasını da diler; büyük bir gemi emreder; Nûh yapar, kavmi eğlence bulup alay eder: «bu ne, ey Nûh — ne zamandan beri marangozsun? sana ayak takımıyla oturma demez miydik? marangozlarla, demircilerle oturdun ve marangoz oldun; bu gemi nereye yürüyecek — kumda mı, dağa mı? deniz uzak: cinler mi taşıyacak, öküzler mi çekecek?»; Nûh hepsini işitir ve sabreder — daha ağırını da işitmişti; bazen cevap verir: «bizimle alay ederseniz, siz nasıl alay ediyorsanız biz de alay ederiz» (11:38) (s1–s14).")
write_out(11, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §18, pp. 27–28", GLOSS_ADD, notes=(), related=())
report(11, S, GLOSS_ADD, ())
