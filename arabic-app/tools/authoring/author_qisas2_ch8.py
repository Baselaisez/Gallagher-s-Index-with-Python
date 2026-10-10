# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 8: «سَفِينَةُ نُوحٍ» §14 اتَّبَعَكَ الْأَرْذَلُونَ (Nūḥ strives; only a few of the humble believe; the rich, held back by pride and busy with wealth and children — «we are nobles and these are the lowly»; «shall we believe you when the lowest follow you?» — 26:111; they ask him to drive the poor away; he refuses — 26:114–115; «who would help me against God if I drove them away?» — 11:30). Print pp. 21–23.
python3 tools/authoring/author_qisas2_ch8.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: اتَّبَعَكَ الْأَرْذَلُونَ", "en": "The ship of Nūḥ: «the lowest follow you»", "tr": "Nûh'un gemisi: «sana en aşağı kimseler uymuş»"}
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

# ---------------------------------------------------------------- §14 اتَّبَعَكَ الْأَرْذَلُونَ (print pp. 21–23)
sen("s1", "And Nūḥ strove hard that his people should believe, worship God and leave the idols.",
        "Nûh, kavminin iman etmesi, Allah'a kulluk etmesi ve putları bırakması için çok çabaladı.", [
  mazi("وَاجْتَهَدَ", "ijtahada", "«and strove»", "«ve çabaladı»", tags=[AT, "form-viii-verbs"], hidden=None, wa=True),
  nuh_fail(),
  tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ (اجْتِهَادًا كَثِيرًا).", "«hard» — stands in for the mafʿūl muṭlaq.", "«çok» — mef'ûl-i mutlakın nâibi."),
  an_nasb("فِي مَحَلِّ جَرٍّ بِحَرْفِ جَرٍّ مَحْذُوفٍ (فِي أَنْ يُؤْمِنَ)", "«that»", "«-mesi için»"),
  tok("يُؤْمِنَ", "aamana", "verb", [AN, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ بَعْدَهُ.", "«believe» — naṣb by an; the doer follows.", "«iman etmesi» — en ile mansub; fâil sonra."),
  qawm_pron("قَوْمُهُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people» — the doer.", "«kavmi» — fâil.", tags=[FL, ID]),
  tok("وَيَعْبُدُوا", "abada", "verb", [AT, AN, AK], "الْوَاوُ عَاطِفَةٌ، وَيَعْبُدُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يُؤْمِنَ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and worship» — naṣb by being joined, its nūn dropped; the wāw is the doer.", "«ve kulluk etmeleri» — atıfla mansub; nûn düştü; vâv fâil.", segments=wa_("يَعْبُدُوا", "abada", "verb")),
  allah_maful(),
  tok("وَيَتْرُكُوا", "taraka", "verb", [AT, AN, AK], "الْوَاوُ عَاطِفَةٌ، وَيَتْرُكُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and leave» — joined; naṣb by the dropped nūn.", "«ve bırakmaları» — ma'tûf; nûnun hazfiyle mansub.", segments=wa_("يَتْرُكُوا", "taraka", "verb")),
  asnam_maful(punct="."),
])
sen("s2", "But none believed in Nūḥ except some individuals of his people.", "Fakat Nûh'a, kavminden birkaç kişiden başkası iman etmedi.", [
  lakin_light(),
  *ma_amana(),
  tok("بِنُوحٍ", "nuh", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَنُوحٍ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«in Nūḥ» — bi + the name (which takes tanwīn).", "«Nûh'a» — bâ + tenvinli özel isim.", segments=[seg("بِ", "bi", "prep"), seg("نُوحٍ", "nuh", "propn")]),
  illa_mufarragh(),
  *bad_afrad(),
  prep("مِنْ", "min", "«of»", "«-den»"),
  qawm_pron("قَوْمِهِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavminden»", tags=[HJ, ID], punct="."),
])
sen("s3", "None believed in him except some individuals who work with their hands and eat what is lawful.", "Ona, elleriyle çalışan ve helâl yiyen birkaç kişiden başkası iman etmedi.", [
  *ma_amana(),
  tok("بِهِ", "bi", "prep", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«in him»", "«ona»", segments=[seg("بِ", "bi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  illa_mufarragh(),
  *bad_afrad(),
  alladhina("jarr", "نَعْتٌ لِلْأَفْرَادِ", "«who» — the relative, a naʿt of «the individuals».", "«… olan» — ism-i mevsûl; «kimseler»in sıfatı.", tags=[NA]),
  khamsa("يَعْمَلُونَ", "amila", "«work»", "«çalışan»", tags=[MW], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ"),
  tok("بِأَيْدِيهِمْ", "yad", "noun", [HJ, ID, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَأَيْدِي مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — جَمْعُ يَدٍ (أَيْدٍ، مَنْقُوصٌ).", "«with their hands» — bi + the manqūṣ plural of yad, annexed.", "«elleriyle» — bâ + yed'in mankûs cem'i, muzâf.", segments=[seg("بِ", "bi", "prep"), seg("أَيْدِي", "yad", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  khamsa("وَيَأْكُلُونَ", "akala", "«and eat»", "«ve yiyen»", tags=[AT, MW], wa=True),
  maful_("الْحَلَالَ", "halal", "«what is lawful»", "«helâli»", punct="."),
])
sen("s4", "As for the rich of his people, their pride kept them from obeying Nūḥ.", "Kavminin zenginlerine gelince, kibirleri onları Nûh'a itaat etmekten alıkoydu.", [
  tok("أَمَّا", "amma-tafsil", "part", [SH], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ، وَجَوَابُهُ مَقْرُونٌ بِالْفَاءِ.", "«as for» — the particle of detailing; its answer is bound to the fāʾ.", "«-e gelince» — tafsil harfi; cevabı fâ ile gelir."),
  tok("الْأَغْنِيَاءُ", "ghani", "noun", [MK, JT], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ غَنِيٍّ.", "«the rich» — the mubtadaʾ.", "«zenginler» — mübtedâ."),
  prep("مِنْ", "min", "«of»", "«-den»"),
  qawm_pron("قَوْمِهِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ.", "«his people» — a ḥāl phrase.", "«kavminin» — hâl ibaresi.", tags=[HJ, ID]),
  tok("فَقَدْ", "qad", "part", [AT, QD, SH], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«[then] indeed» — the fāʾ of ammā's answer + qad.", "«işte» — emmâ'nın cevap fâ'sı + kad.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  v_pron("مَنَعَهُمْ", "manaa", "مَنَعَ", "هُمْ", "pron-3mp", "«kept them» — the object aboard, the doer follows; the clause is the khabar.", "«onları alıkoydu» — mef'ûl zamir, fâil sonra; cümle haber.", hidden=None, tags=[MK]),
  noun_pron("كِبْرُهُمْ", "kibr", "كِبْرُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their pride» — the doer.", "«kibirleri» — fâil.", tags=[FL, ID]),
  an_nasb("فِي مَحَلِّ جَرٍّ بِمِنْ الْمَحْذُوفَةِ (مِنْ أَنْ يُطِيعُوا)", "«from»", "«-mekten»"),
  tok("يُطِيعُوا", "ataa", "verb", [AN, AK, "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«obey» — naṣb by an, the nūn dropped; the wāw is the doer.", "«itaat etmek» — en ile mansub; nûn düştü; vâv fâil."),
  nuh_maful(punct="."),
])
sen("s5", "And their wealth and their children kept them busy from thinking of the hereafter; and they used to say: we are nobles and these are the lowly.",
        "Malları ve çocukları onları âhireti düşünmekten alıkoydu; ve derlerdi: biz eşrafız, bunlar ise ayak takımı.", [
  tok("وَشَغَلَتْهُمْ", "shaghala", "verb", [AT, MB], "الْوَاوُ عَاطِفَةٌ، وَشَغَلَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهُمْ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.", "«and … kept them busy» — the feminine tāʾ; the object aboard; the doer follows.", "«ve onları meşgul etti» — te'nis tâ'sı; mef'ûl zamir; fâil sonra.", segments=[seg("وَ", "wa", "conj"), seg("شَغَلَتْ", "shaghala", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  noun_pron("أَمْوَالُهُمْ", "mal", "أَمْوَالُ", "هُمْ", "pron-3mp", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ مَالٍ.", "«their wealth» — the doer.", "«malları» — fâil.", tags=[FL, ID, JT]),
  pron_atf("وَأَوْلَادُهُمْ", "walad", "أَوْلَادُ", "هُمْ", "pron-3mp", "«their children»", "«çocukları»", case="raf", tags=[JT]),
  an_nasb("فِي مَحَلِّ جَرٍّ بِعَنْ الْمَحْذُوفَةِ (عَنْ أَنْ يُفَكِّرُوا)", "«from»", "«-mekten»"),
  tok("يُفَكِّرُوا", "fakkara", "verb", [AN, AK, "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«think» — naṣb by an, the nūn dropped.", "«düşünmek» — en ile mansub; nûn düştü."),
  fi(),
  majrur("الْآخِرَةِ", "akhira", "«the hereafter»", "«âhireti»"),
  kana_pl("وَكَانُوا", wa=True),
  khamsa("يَقُولُونَ", "qala", "«say»", "«derlerdi»", tags=[KN, "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", punct=":"),
  pron_mubtada("نَحْنُ", "nahnu", "«we»", "«biz»"),
  tok("أَشْرَافٌ", "sharif", "noun", [MK, JT], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ شَرِيفٍ.", "«[are] nobles» — the khabar; the plural of sharīf.", "«eşrafız» — haber; şerîf'in cem'i."),
  tok("وَهٰؤُلَاءِ", "haulai", "pron", [AT, MK, "asma-al-ishara"], "الْوَاوُ عَاطِفَةٌ، وَهٰؤُلَاءِ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and these» — the plural demonstrative; the mubtadaʾ.", "«bunlar ise» — çoğul ism-i işâret; mübtedâ.", segments=wa_("هٰؤُلَاءِ", "haulai", "pron")),
  tok("أَرَاذِلُ", "ardhal", "noun", [MK, JT, MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ أَرْذَلَ عَلَى أَفَاعِلَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ.", "«[are] the lowly» — the khabar; أَفَاعِل, a diptote by its plural pattern.", "«ayak takımı» — haber; efâil vezni, cem-i müntehâ, gayr-i munsarıf.", punct="."),
])
sen("s6", "And when Nūḥ called them to God, they said:", "Nûh onları Allah'a çağırınca dediler:", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF, SH], "الْوَاوُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — lammā.", "«ve … -ınca» — lemmâ.", segments=wa_("لَمَّا", "lamma", "part")),
  v_pron("دَعَاهُمْ", "daa", "دَعَا", "هُمْ", "pron-3mp", "«called them» — the condition's verb; the defective māḍī keeps its alif before the pronoun.", "«onları çağırdı» — şart fiili; nâkıs mâzî zamirden önce elifini korur.", hidden=None, tags=[SH, "naqis-verbs"]),
  nuh_fail(),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("اللهِ", "allah", "«God»", "«Allah'a»"),
  qalu("قَالُوا", punct=":"),
])
sen("s7", "«Shall we believe you, when the lowest follow you?» (26:111).", "«Sana en aşağı kimseler uymuşken sana inanır mıyız?» (26:111).", [
  *quran([
    tok("أَنُؤْمِنُ", "aamana", "verb", [IS, "mudari-marfu", "form-iv-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَنُؤْمِنُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«shall we believe» — the question hamza of denial + the muḍāriʿ.", "«inanır mıyız» — inkârî istifham hemzesi + muzâri.", segments=[seg("أَ", "hamza-istifham", "part"), seg("نُؤْمِنُ", "aamana", "verb")]),
    li_pron("لَكَ", "كَ", "pron-2ms", "«you»", "«sana»"),
    tok("وَاتَّبَعَكَ", "ittabaa", "verb", [HL, MB, "form-viii-verbs"], "الْوَاوُ لِلْحَالِ، وَاتَّبَعَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْكَافُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ (وَقَدْ مُقَدَّرَةٌ).", "«when … have followed you» — the wāw of the ḥāl; the object aboard; the doer follows.", "«sana … uymuşken» — hâl vâvı; mef'ûl zamir; fâil sonra.", segments=[seg("وَ", "wa", "conj"), seg("اتَّبَعَ", "ittabaa", "verb"), seg("كَ", "pron-2ms", "pron")]),
    tok("الْأَرْذَلُونَ", "ardhal", "noun", [FL, JS, "ism-tafdil"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — جَمْعُ أَرْذَلَ، اسْمِ تَفْضِيلٍ.", "«the lowest» — the doer, rafʿ by the wāw of the sound plural; the elative أَرْذَل.", "«en aşağı kimseler» — fâil; cemi müzekker sâlim, vâv ile merfû; ism-i tafdil.", punct="؟."),
  ]),
])
sen("s8", "And they asked Nūḥ to drive these poor people away.", "Ve Nûh'tan bu yoksulları kovmasını istediler.", [
  mazi_pl("وَطَلَبُوا", "talaba", "«and they asked»", "«ve istediler»", tags=[AT], wa=True),
  prep("مِنْ", "min", "«from»", "«-dan»"),
  tok("نُوحٍ", "nuh", "propn", [HJ], "مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ»", "«Nûh'tan»"),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِطَلَبُوا", "«that»", "«-masını»"),
  tok("يَطْرُدَ", "tarada-expel", "verb", [AN], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«drive away» — naṣb by an; the doer is concealed.", "«kovmasını» — en ile mansub; fâil gizli."),
  haulai("nasb", "مَفْعُولٌ بِهِ", "«these» — the object.", "«bunları» — mef'ûl.", tags=[MB]),
  masakin("nasb", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ)", "«poor people» — a badal of the demonstrative.", "«yoksulları» — ism-i işâretten bedel.", punct="."),
])
sen("s9", "But Nūḥ refused and said: «I am not one to drive away the believers»; my door is not a king's door; «I am only a plain warner» (26:114–115).",
        "Fakat Nûh reddetti ve dedi: «Ben mü'minleri kovacak değilim»; benim kapım bir kral kapısı değildir; «ben ancak apaçık bir uyarıcıyım» (26:114–115).", [
  tok("وَلٰكِنْ", "lakin", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ — هُنَا مُشَدَّدٌ فِي الْمَعْنَى نَاصِبٌ (لٰكِنَّ) عَلَى قِرَاءَةِ النَّصْبِ بَعْدَهُ، وَالْمَطْبُوعُ بِالتَّخْفِيفِ.", "«but» — lākin; the print writes it light while the name after it stands in naṣb, as under the heavy lākinna.", "«fakat» — lâkin; baskı tahfifle yazar, sonraki isim ise lâkinne'nin ismi gibi mansubdur.", segments=wa_("لٰكِنْ", "lakin", "part")),
  nuh_ism_inna_light(),
  tok("أَبَى", "aba", "verb", [IW, "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرٌ.", "«refused» — the defective māḍī; the clause is the khabar.", "«reddetti» — nâkıs mâzî; cümle haber."),
  qala("وَقَالَ", wa=True, punct=":"),
  *quran([
    tok("مَا", "ma-nafiya", "part", ["la-nafiya", "anwa-ma"], "مَا نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ (الْحِجَازِيَّةُ).", "«not» — the Ḥijāzī mā that works like laysa.", "«değil» — leyse gibi amel eden Hicaz mâ'sı."),
    tok("أَنَا", "ana", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ مَا.", "«I» — mā's ism.", "«ben» — mâ'nın ismi."),
    tok("بِطَارِدِ", "tarid-expeller", "noun", [HJ, ID, "ism-fail"], "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَطَارِدِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ مَا، مُضَافٌ — اسْمُ فَاعِلٍ.", "«one to drive away» — bi is added; mā's khabar in naṣb by place; the participle annexed.", "«kovacak» — zâid bâ; mahallen mansub mâ'nın haberi; ism-i fâil, muzâf.", segments=[seg("بِ", "bi", "prep"), seg("طَارِدِ", "tarid-expeller", "noun")]),
    tok("الْمُؤْمِنِينَ", "mumin", "noun", [ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the believers» — the muḍāf ilayh; jarr by the yāʾ.", "«mü'minleri» — muzâfun ileyh; yâ ile mecrûr.", punct="،"),
  ]),
  inna(),
  noun_pron("بَابِي", "bab", "بَابِ", "ي", "pron-1s", "اسْمُ إِنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my door» — inna's ism, annexed to the speaker's yāʾ.", "«kapım» — inne'nin ismi; mütekellim yâ'sına muzâf.", tags=[IW, ID, YM]),
  tok("لَيْسَ", "laysa", "verb", [KN, IW, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«is not» — laysa with its concealed ism; the clause is inna's khabar.", "«değildir» — leyse, ismi gizli; cümle inne'nin haberi."),
  tok("بَابَ", "bab", "noun", [KN, ID], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the door [of]» — laysa's khabar, annexed.", "«kapısı» — leyse'nin haberi, muzâf."),
  mudaf_ilayh("مَلِكٍ", "malik-king", "«a king»", "«bir kral»", punct="،"),
  *quran([
    tok("إِنْ", "in-nafiya", "part", ["la-nafiya"], "إِنْ نَافِيَةٌ بِمَعْنَى مَا.", "«not» — the negating in.", "«değil» — nefiy in'i."),
    tok("أَنَا", "ana", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«I» — the mubtadaʾ.", "«ben» — mübtedâ."),
    tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ (حَصْرٍ).", "«only» — the exceptive of restriction.", "«ancak» — hasr edatı."),
    khabar("نَذِيرٌ", "nadhir", "«a warner»", "«bir uyarıcıyım»"),
    naat("مُبِينٌ", "mubin", "«plain»", "«apaçık»", case="raf", punct=".", tags=["ism-fail"]),
  ]),
])
sen("s10", "And Nūḥ knew that these poor people were sincere believers.", "Nûh, bu yoksulların samimi mü'minler olduğunu biliyordu.", [
  kana(), nuh_ism_kana(),
  mudari("يَعْرِفُ", "arafa", "«knew»", "«biliyordu»", tags=[KN, MB], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ؛ وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُهُ"),
  anna_(obj="يَعْرِفُ"),
  haulai("nasb", "اسْمُ أَنَّ", "«these» — anna's ism.", "«bunların» — enne'nin ismi.", tags=[IW]),
  masakin("nasb", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«poor people» — a badal.", "«yoksullar» — bedel."),
  tok("مُؤْمِنُونَ", "mumin", "noun", [IW, JS, "ism-fail"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«[are] believers» — anna's khabar, rafʿ by the wāw.", "«mü'minlerdir» — enne'nin haberi; vâv ile merfû."),
  tok("مُخْلِصُونَ", "mukhlis", "noun", [NA, JS, "ism-fail"], "نَعْتٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«sincere» — a naʿt in rafʿ by the wāw.", "«samimi» — vâv ile merfû sıfat.", punct="."),
])
sen("s11", "And that God would be angry if he drove these poor people away — and then no one would help him.", "Ve Allah'ın, bu yoksulları kovarsa gazap edeceğini — ve o zaman kimsenin ona yardım etmeyeceğini.", [
  anna_(wa=True, obj="يَعْرِفُ"),
  allah_ism(part="أَنَّ"),
  mudari("يَغْضَبُ", "ghadiba", "«is angry»", "«gazap eder»", tags=[IW], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  idha(),
  mazi("طَرَدَ", "tarada-expel", "«he drove away»", "«kovarsa»", tags=["idha-shartiyya"], extra_ar=" — فِعْلُ الشَّرْطِ، وَجَوَابُهُ مَدْلُولٌ عَلَيْهِ بِمَا قَبْلَهُ"),
  haulai("nasb", "مَفْعُولٌ بِهِ", "«these» — the object.", "«bunları» — mef'ûl.", tags=[MB]),
  masakin("nasb", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ", "«poor people» — a badal.", "«yoksulları» — bedel.", punct="،"),
  tok("وَإِذَنْ", "idhan-jawab", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَإِذَنْ حَرْفُ جَوَابٍ وَجَزَاءٍ — مُهْمَلٌ هُنَا لِأَنَّ بَعْدَهُ لَا وَالْفِعْلُ مَرْفُوعٌ.", "«and then» — idhan, the particle of answer; it does not govern here (lā stands between it and the verb, which stays in rafʿ).", "«ve o zaman» — cevap harfi izen; burada amel etmez (lâ araya girer, fiil merfû kalır).", segments=wa_("إِذَنْ", "idhan-jawab", "part")),
  la_nafiya(),
  tok("يَنْصُرُهُ", "nasara", "verb", ["la-nafiya", "mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.", "«helps him» — the object aboard; the doer follows.", "«ona yardım eder» — mef'ûl zamir; fâil sonra.", segments=[seg("يَنْصُرُ", "nasara", "verb"), seg("هُ", "pron-3ms", "pron")]),
  fail("أَحَدٌ", "ahad", "«anyone»", "«kimse»", punct="."),
])
sen("s12", "So Nūḥ said: «O my people, who would help me against God if I drove them away?» (11:30).", "Bunun üzerine Nûh dedi: «Ey kavmim, onları kovarsam Allah'a karşı bana kim yardım eder?» (11:30).", [
  qala("فَقَالَ", wa=True, punct=None),
  nuh_fail(punct=":"),
  *quran([
    *ya_qawmi(),
    tok("مَنْ", "man", "pron", [IS, MK], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«who» — the question noun; the mubtadaʾ.", "«kim» — soru ismi; mübtedâ."),
    tok("يَنْصُرُنِي", "nasara", "verb", ["mudari-marfu", MB, MK], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«would help me» — the nūn of protection before the speaker's yāʾ; the clause is the khabar.", "«bana yardım eder» — vikâye nûnu + mütekellim yâ'sı; cümle haber.", segments=[seg("يَنْصُرُ", "nasara", "verb"), seg("نِي", "pron-1s", "pron")]),
    tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«against»", "«-a karşı»"),
    majrur("اللهِ", "allah", "«God»", "«Allah'a»"),
    tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the conditional in.", "«-se» — cezmeden şart harfi."),
    tok("طَرَدْتُهُمْ", "tarada-expel", "verb", [SH, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ — وَجَوَابُ الشَّرْطِ مَدْلُولٌ عَلَيْهِ بِمَا قَبْلَهُ.", "«I drove them away» — the condition's verb, built on sukūn before the doer's tāʾ; its answer is understood from what precedes.", "«onları kovarsam» — şart fiili; fâil tâ'sı; cevabı öncesinden anlaşılır.", segments=[seg("طَرَدْتُ", "tarada-expel", "verb"), seg("هُمْ", "pron-3mp", "pron")], punct="."),
  ]),
])

CAND = {
 "ijtahada": G("ijtahada", "اِجْتَهَدَ", "ج ه د", "verb", "to strive, to exert oneself (Form VIII)", "çabalamak, gayret etmek (iftiâl)", 1),
 "nuh": G("nuh", "نُوح", None, "propn", "Nūḥ (Noah)", "Nûh", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "much, many", "çok", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ (الْمَصْدَرِيَّة)", None, "part", "that, to (+ subjunctive)", "-mek, -mesi (muzâriyi nasbeder)", 1),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV; آمَنَ بِ)", "iman etmek (if'âl; âmene bi)", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people, a group", "kavim, topluluk", 1, plural="أَقْوَام"),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "taraka": G("taraka", "تَرَكَ", "ت ر ك", "verb", "to leave, abandon", "bırakmak, terk etmek", 1),
 "sanam": G("sanam", "صَنَم", "ص ن م", "noun", "idol", "put", 1, plural="أَصْنَام"),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but, yet (lightened — no government)", "fakat (tahfifli — amel etmez)", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (negates past verbs)", "değil, -medi (nefiy mâ'sı)", 1),
 "bi": G("bi", "بِ", None, "prep", "by, with, in", "ile, -de", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except, but (exception)", "ancak, -den başka (istisnâ)", 1),
 "baad": G("baad", "بَعْض", "ب ع ض", "noun", "part, some", "bazı, bir kısmı", 1),
 "fard-single": G("fard-single", "فَرْد", "ف ر د", "noun", "alone, single", "tek, fert", 1, plural="أَفْرَاد"),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "those who (masc. pl.)", "onlar ki, … olanlar", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to act, work (بِ: act upon)", "çalışmak, iş yapmak", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "hand", "el", 1, plural="أَيْدٍ"),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "halal": G("halal", "الْحَلَال", "ح ل ل", "noun", "what is lawful", "helâl", 1),
 "amma-tafsil": G("amma-tafsil", "أَمَّا", None, "part", "as for … (the particle of detailing; its answer takes the fāʾ)", "-e gelince (tafsil harfi; cevabı fâ alır)", 1),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "qad": G("qad", "قَدْ", None, "part", "indeed (before a past verb)", "gerçekten (mâzîden önce tahkik)", 1),
 "manaa": G("manaa", "مَنَعَ", "م ن ع", "verb", "to withhold, prevent", "alıkoymak, engellemek", 1),
 "kibr": G("kibr", "كِبْر", "ك ب ر", "noun", "pride, self-greatness", "kibir", 1),
 "ataa": G("ataa", "أَطَاعَ", "ط و ع", "verb", "to obey", "itaat etmek (if'âl, ecvef)", 1),
 "shaghala": G("shaghala", "شَغَلَ", "ش غ ل", "verb", "to occupy, to fill", "meşgul etmek", 1),
 "mal": G("mal", "مَال", "م و ل", "noun", "wealth, property", "mal", 1, plural="أَمْوَال"),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "child, offspring (one or many)", "çocuk", 1, plural="أَوْلَاد"),
 "fakkara": G("fakkara", "فَكَّرَ", "ف ك ر", "verb", "to think, to ponder (Form II)", "düşünmek (tef'îl)", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "akhira": G("akhira", "آخِرَة", "أ خ ر", "noun", "the hereafter, the last abode", "âhiret", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "nahnu": G("nahnu", "نَحْنُ", None, "pron", "we (detached)", "biz (munfasıl)", 1),
 "sharif": G("sharif", "شَرِيف", "ش ر ف", "noun", "noble", "şerefli, eşraftan", 1, plural="أَشْرَاف"),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these (the plural demonstrative, built on kasra)", "bunlar (çoğul ism-i işâret)", 1),
 "ardhal": G("ardhal", "أَرْذَل", "ر ذ ل", "noun", "lowest, most base (ism tafdil)", "en aşağı, en alçak (ism-i tafdil)", 1, plural="أَرَاذِل"),
 "lamma": G("lamma", "لَمَّا", None, "part", "when (with a past verb)", "-ınca, -dığı zaman (mâzî ile)", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call, summon", "çağırmak, davet etmek", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "hamza-istifham": G("hamza-istifham", "أَ (الِاسْتِفْهَام)", None, "part", "the question hamza — what follows it is the thing asked about", "soru hemzesi", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "ittabaa": G("ittabaa", "اِتَّبَعَ", "ت ب ع", "verb", "to follow", "uymak, tâbi olmak (iftiâl)", 1),
 "talaba": G("talaba", "طَلَبَ", "ط ل ب", "verb", "to seek, request", "istemek, talep etmek", 1),
 "tarada-expel": G("tarada-expel", "طَرَدَ", "ط ر د", "verb", "to drive away, to expel", "kovmak, sürmek", 1),
 "miskin": G("miskin", "مِسْكِين", "س ك ن", "noun", "poor, destitute", "yoksul, miskin", 1, plural="مَسَاكِين"),
 "aba": G("aba", "أَبَى", "أ ب ي", "verb", "to refuse, turn away", "reddetmek, kaçınmak", 1),
 "ana": G("ana", "أَنَا", None, "pron", "I (detached)", "ben (munfasıl)", 1),
 "tarid-expeller": G("tarid-expeller", "طَارِد", "ط ر د", "noun", "one who drives away (ism fāʿil of طَرَدَ)", "kovan (tarade'nin ism-i fâili)", 1),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "believer (ism fa'il of Form IV)", "mü'min, inanan", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — the emphasizing particle", "şüphesiz — tekid harfi", 1),
 "bab": G("bab", "بَاب", "ب و ب", "noun", "a door; a chapter", "kapı; bab", 1, plural="أَبْوَاب"),
 "laysa": G("laysa", "لَيْسَ", None, "verb", "is not (a verb that never conjugates for tense)", "değildir, yoktur (câmid fiil)", 1),
 "malik-king": G("malik-king", "مَلِك", "م ل ك", "noun", "king", "kral, melik", 1, plural="مُلُوك"),
 "in-nafiya": G("in-nafiya", "إِنْ (النَّافِيَة)", None, "part", "not — the negating in (= mā)", "değil — nefiy in'i (= mâ)", 1),
 "nadhir": G("nadhir", "نَذِير", "ن ذ ر", "noun", "a warner", "uyarıcı", 1),
 "mubin": G("mubin", "مُبِين", "ب ي ن", "noun", "clear, making clear (ism fāʿil of أَبَانَ)", "apaçık", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, recognize", "bilmek, tanımak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (heavy anna)", "ki (şeddeli enne)", 1),
 "mukhlis": G("mukhlis", "مُخْلِص", "خ ل ص", "noun", "sincere (ism fail of أَخْلَصَ)", "ihlâslı, samimi", 1),
 "ghadiba": G("ghadiba", "غَضِبَ", "غ ض ب", "verb", "to become angry", "gazap etmek, öfkelenmek", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ınca", 1),
 "idhan-jawab": G("idhan-jawab", "إِذَنْ", None, "part", "then, in that case (the particle of answer)", "o zaman, öyleyse (cevap harfi)", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (simple negation)", "değil, -mez (nefiy lâ'sı)", 1),
 "nasara": G("nasara", "نَصَرَ", "ن ص ر", "verb", "to help", "yardım etmek", 1),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "anyone, one", "biri, kimse", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O! (vocative)", "ey! (nidâ)", 1),
 "man": G("man", "مَنْ", None, "pron", "who, whoever — the relative and conditional noun", "kim, kimse", 1),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (conditional, governs jazm)", "eğer, -se (cezmeden şart)", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "my (attached pronoun)", "benim (bitişik)", 1),
 "pron-2ms": G("pron-2ms", "ـكَ", None, "pron", "you / your (attached pronoun)", "sen / senin (bitişik)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "fa": G("fa", "فَـ", None, "part", "so, for, then", "bunun üzerine", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch8 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 8 (print pp. 21–23; Nūḥ §14): «the lowest follow you» — Nūḥ strives hard; only a few believe, those who work with their hands and eat what is lawful; the rich are held back by pride and busied by wealth and children («we are nobles and these are the lowly»); «shall we believe you when the lowest follow you?» (26:111); they ask him to drive the poor away; he refuses — «I am not one to drive away the believers», my door is no king's door, «I am only a plain warner» (26:114–115); he knows them sincere and that God would be angry; «who would help me against God if I drove them away?» (11:30) (s1–s12). The print writes وَلٰكِنْ نُوحًا with the light lākin and the name in naṣb; both are kept as printed.")
ADD_TR = (" Sekizinci bölüm (basılı s. 21–23; Nûh §14): «sana en aşağı kimseler uymuş» — Nûh çok çabalar; yalnız elleriyle çalışıp helâl yiyen birkaç kişi inanır; zenginleri kibirleri alıkoyar, mal ve çocukları oyalar («biz eşrafız, bunlar ayak takımı»); «sana en aşağı kimseler uymuşken sana inanır mıyız?» (26:111); yoksulları kovmasını isterler; reddeder — «ben mü'minleri kovacak değilim», kapım kral kapısı değil, «ben ancak apaçık bir uyarıcıyım» (26:114–115); onların samimi olduğunu ve Allah'ın gazap edeceğini bilir; «onları kovarsam Allah'a karşı bana kim yardım eder?» (11:30) (s1–s12). Baskı وَلٰكِنْ نُوحًا'yı tahfifli lâkin ve mansub isimle yazar; ikisi de basıldığı gibi korunur.")
write_out(8, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §14, pp. 21–23", GLOSS_ADD, notes=(), related=())
report(8, S, GLOSS_ADD, ())
