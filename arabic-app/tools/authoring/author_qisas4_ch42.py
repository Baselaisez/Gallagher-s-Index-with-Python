# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 42: «قِصَّةُ عِيسَى» §36 (his glad tidings of the mission of our master Muḥammad, with al-Ṣaff 61:6) and §37 (from pure tawḥīd to an obscure creed: the exaltation of the Messiah to divinity, the trinity, the veneration of Maryam, with al-Māʾida 5:75–76); print pp. 62–64.
python3 tools/authoring/author_qisas4_ch42.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: بِشَارَتُهُ بِبِعْثَةِ سَيِّدِنَا مُحَمَّدٍ، وَمِنَ التَّوْحِيدِ الْخَالِصِ إِلَى عَقِيدَةٍ غَامِضَةٍ", "en": "The story of ʿĪsā: his tidings of Muḥammad's mission; from pure tawḥīd to an obscure creed", "tr": "Îsâ'nın kıssası: Muhammed'in gönderilişini müjdelemesi; hâlis tevhidden kapalı bir akîdeye"}
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

# ---------------------------------------------------------------- §36 بِشَارَتُهُ بِبِعْثَةِ سَيِّدِنَا مُحَمَّدٍ (print p. 62)
sen("s1", "And our master the Messiah did not complete his task in the call, because of the intensity of the Jews' warring and their plotting against him, and his weakness and the fewness of his helpers;",
        "Efendimiz Mesîh, Yahudilerin savaşının ve ona kurdukları tuzağın şiddeti, zayıflığı ve yardımcılarının azlığı yüzünden davet görevini tamamlayamadı;", [
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … -madı»", segments=wa_("لَمْ", "lam", "part")),
  tok("يُكْمِلْ", "akmala", "verb", [LJ, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ.", "«complete»", "«tamamladı»"),
  noun_pron("سَيِّدُنَا", "sayyid", "سَيِّدُ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master» — the doer.", "«efendimiz» — fâil.", tags=[FL, ID]),
  tok("الْمَسِيحُ", "masih", "propn", [BD], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah»", "«Mesîh»"),
  noun_pron("مُهِمَّتَهُ", "muhimma", "مُهِمَّتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his task» — the object.", "«görevini» — mef'ûl.", tags=[MB, ID]),
  fi(),
  majrur("الدَّعْوَةِ", "dawa", "«the call»", "«davette»"),
  tok("لِشِدَّةِ", "shidda", "noun", [HJ, ID, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَشِدَّةِ مَجْرُورٌ، مُضَافٌ.", "«because of the intensity [of]»", "«şiddeti yüzünden»", segments=[seg("لِ", "li", "prep"), seg("شِدَّةِ", "shidda", "noun")]),
  majrur("مُحَارَبَةِ", "muharaba", "«the warring [of]»", "«savaşının»", tags=[ID, "form-iii-verbs"], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى فَاعِلِهِ."),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»"),
  pron_atf("وَكَيْدِهِمْ", "kayd", "كَيْدِ", "هِمْ", "pron-3mp", "«their plotting»", "«ve tuzaklarının»"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«against him»", "«ona»", punct="،"),
  pron_atf("وَضَعْفِهِ", "daf", "ضَعْفِ", "هِ", "pron-3ms", "«his weakness»", "«ve zayıflığının»"),
  atf("وَقِلَّةِ", "qilla", "«the fewness [of]»", "«ve azlığının»", tags=[ID, "doubled-verbs"], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  noun_pron("أَنْصَارِهِ", "nasir", "أَنْصَارِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his helpers»", "«yardımcılarının»", tags=[ID, JT], punct="،"),
])
sen("s2", "so he bade people farewell, obeyed his Lord's command, and gave people glad tidings of a messenger coming after him who would complete what he had begun and generalize what he had particularized, by whom God's favour on His servants would be completed and His proof against His creatures established:",
        "bu yüzden insanlara veda etti, Rabbinin emrine uydu ve insanları kendisinden sonra gelecek bir resulle müjdeledi: başladığını tamamlayacak, hususî kıldığını umumî kılacak; onunla Allah'ın kullarına nimeti tamam olacak ve yaratıklarına hücceti ayakta duracak:", [
  tok("فَوَدَّعَ", "waddaa", "verb", [AT, "form-ii-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَوَدَّعَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«so he bade farewell»", "«bu yüzden veda etti»", segments=[seg("فَ", "fa", "conj"), seg("وَدَّعَ", "waddaa", "verb")]),
  maful_("النَّاسَ", "nas", "«people»", "«insanlara»", punct="،"),
  mazi("وَامْتَثَلَ", "imtathala", "«and obeyed»", "«ve uydu»", tags=[AT, "form-viii-verbs"], wa=True, hidden="هُوَ"),
  maful_("أَمْرَ", "amr", "«the command [of]»", "«emrine»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  noun_pron("رَبِّهِ", "rabb", "رَبِّ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his Lord»", "«Rabbinin»", tags=[ID], punct="،"),
  mazi("وَبَشَّرَ", "bashshara", "«and gave glad tidings to»", "«ve müjdeledi»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  maful_("النَّاسَ", "nas", "«people»", "«insanları»"),
  bi_noun("بِرَسُولٍ", "rasul", "«of a messenger»", "«bir resulle»"),
  mudari("يَأْتِي", "ata", "«coming»", "«gelecek»", tags=["jumla-sifa", "naqis-verbs"], extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ؛ وَالْجُمْلَةُ نَعْتٌ لِرَسُولٍ"),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  noun_pron("بَعْدِهِ", "bad-after", "بَعْدِ", "هِ", "pron-3ms", "ظَرْفٌ مَجْرُورٌ بِمِنْ (أُعْرِبَ لِدُخُولِ الْجَارِّ)، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«after him» — the ẓarf declined after min.", "«kendisinden sonra» — min'den sonra mu'rab zarf.", tags=[HJ, ID], punct="،"),
  mudari("يُكْمِلُ", "akmala", "«who would complete»", "«tamamlayacak»", tags=["jumla-sifa", "form-iv-verbs"], extra_ar=" — نَعْتٌ ثَانٍ لِرَسُولٍ"),
  ma_mawsul_obj("«what»", "«… -ı»"),
  v_pron("بَدَأَهُ", "badaa", "بَدَأَ", "هُ", "pron-3ms", "«he had begun»", "«başladığı»", tags=[MW]),
  mudari_wa("وَيُعَمِّمُ", "ammama", "«and generalize»", "«ve umumî kılacak»", tags=["form-ii-verbs"]),
  ma_mawsul_obj("«what»", "«… -ı»"),
  v_pron("خَصَّصَهُ", "khassasa", "خَصَّصَ", "هُ", "pron-3ms", "«he had particularized»", "«hususî kıldığı»", tags=[MW, "form-ii-verbs"], punct="،"),
  prep_pron("وَبِهِ", "bi", "هِ", "pron-3ms", "«and by him» — fronted for emphasis.", "«ve onunla» — öne alınmış.", tags=[AT], extra_ar=" — الْوَاوُ عَاطِفَةٌ، وَقُدِّمَ الْجَارُّ لِلِاهْتِمَامِ"),
  mudari("تَتِمُّ", "tamma", "«would be completed»", "«tamam olacak»", tags=["doubled-verbs"], hidden=None),
  fail("نِعْمَةُ", "nima", "«the favour [of]»", "«nimeti»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  noun_pron("عِبَادِهِ", "ibad", "عِبَادِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His servants»", "«kullarına»", tags=[HJ, ID], punct="،"),
  mudari_wa("وَتَقُومُ", "qama", "«and would stand»", "«ve ayakta duracak»", tags=["hollow-verbs"], hidden=None),
  noun_pron("حُجَّتُهُ", "hujja", "حُجَّتُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His proof» — the doer.", "«hücceti» — fâil.", tags=[FL, ID]),
  prep("عَلَى", "ala", "«against»", "«-e»"),
  noun_pron("خَلْقِهِ", "khalq", "خَلْقِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His creatures»", "«yaratıklarına»", tags=[HJ, ID], punct=":"),
])
sen("s3", "«And when ʿĪsā son of Maryam said: O Children of Israel, I am the Messenger of God to you, confirming what is before me of the Torah and bringing glad tidings of a messenger who will come after me, whose name is Aḥmad.» (61:6)",
        "«Hani Meryem oğlu Îsâ demişti: Ey İsrâiloğulları! Ben size Allah'ın resulüyüm; önümdeki Tevrat'ı doğrulayıcı ve benden sonra gelecek, adı Ahmed olan bir resulü müjdeleyici olarak.» (61:6)", [
  *quran([
  tok("وَإِذْ", "idh", "noun", [AT, MF, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَإِذْ ظَرْفٌ لِمَا مَضَى فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: اذْكُرْ.", "«and when»", "«ve hani»", segments=wa_("إِذْ", "idh", "noun")),
  mazi("قَالَ", "qala", "«said»", "«demişti»", tags=[ID, "hollow-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  tok("عِيسَى", "isa", "propn", [FL, MM, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — the doer.", "«Îsâ» — fâil."),
  tok("ابْنُ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَرْفُوعٌ، مُضَافٌ.", "«son [of]»", "«oğlu»"),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»"),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("بَنِي", "banu-israil", "noun", ["vocative-munada", ID, JS], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«Children [of]» — an annexed munādā.", "«oğulları» — muzâf münâdâ."),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Israel»", "«İsrâil»"),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«şüphesiz ben»", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("رَسُولُ", "rasul", "noun", [IW, ID], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the Messenger [of]» — inna's khabar.", "«resulü» — inne'nin haberi."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  prep_pron("إِلَيْكُمْ", "ila", "كُمْ", "pron-2mp", "«to you»", "«size»"),
  hal("مُصَدِّقًا", "musaddiq", "«confirming»", "«doğrulayıcı olarak»", tags=["ism-fail", "form-ii-verbs"]),
  tok("لِمَا", "ma-mawsula", "pron", [HJ, MW], "اللَّامُ حَرْفُ جَرٍّ لِتَقْوِيَةِ الْعَامِلِ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«… -ı»", segments=[seg("لِ", "li", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("بَيْنَ", "bayna", "noun", [MF, ID, "hadhf-wa-taqdir"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةٍ مَحْذُوفَةٍ، مُضَافٌ.", "«between»", "«arasında»"),
  tok("يَدَيَّ", "yad", "noun", [ID, "al-muthanna", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَأُدْغِمَتْ يَاؤُهُ فِي يَاءِ الْمُتَكَلِّمِ.", "«my two hands» — «before me».", "«iki elim» — «önümde».", segments=[seg("يَدَ", "yad", "noun"), seg("يَّ", "pron-1s", "pron")]),
  tok("مِنَ", "min", "prep", [HJ, HL], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ.", "«of»", "«-den»"),
  majrur("التَّوْرَاةِ", "tawrat", "«the Torah»", "«Tevrat»"),
  tok("وَمُبَشِّرًا", "mubashshir", "noun", [AT, HL, "ism-fail", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمُبَشِّرًا حَالٌ مَعْطُوفٌ مَنْصُوبٌ.", "«and bringing glad tidings» — a second ḥāl.", "«ve müjdeleyici olarak» — ikinci hâl.", segments=wa_("مُبَشِّرًا", "mubashshir", "noun")),
  bi_noun("بِرَسُولٍ", "rasul", "«of a messenger»", "«bir resulü»"),
  mudari("يَأْتِي", "ata", "«who will come»", "«gelecek»", tags=["jumla-sifa", "naqis-verbs"], extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ؛ وَالْجُمْلَةُ نَعْتٌ لِرَسُولٍ"),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  tok("بَعْدِي", "bad-after", "noun", [HJ, ID, "ya-al-mutakallim"], "ظَرْفٌ مَجْرُورٌ بِمِنْ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«after me»", "«benden sonra»", segments=[seg("بَعْدِ", "bad-after", "noun"), seg("ي", "pron-1s", "pron")]),
  noun_pron("اسْمُهُ", "ism", "اسْمُ", "هُ", "pron-3ms", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِرَسُولٍ.", "«whose name» — a mubtadaʾ; the clause is a second naʿt.", "«adı» — mübtedâ; cümle ikinci sıfat.", tags=[MK, ID, "jumla-sifa"]),
  tok("أَحْمَدُ", "ahmad", "propn", [MK, MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ عَلَى وَزْنِ الْفِعْلِ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Aḥmad» — the khabar; a diptote name on a verb pattern.", "«Ahmed» — haber; fiil vezninde gayr-i munsarıf isim.", punct=AYA),
  ]),
])
# ---------------------------------------------------------------- §37 مِنَ التَّوْحِيدِ الْخَالِصِ إِلَى عَقِيدَةٍ غَامِضَةٍ (print pp. 62–63)
sen("s4", "And among the strange things in the history of religions — something at which eyes weep and hearts melt — is that the Messiah's call to pure tawḥīd and to the easy, palatable religion far from every obscurity and complication, every distortion and far-fetched interpretation — the call to the worship of God alone, to asking of Him, to taking refuge in Him and to pure love of Him — turned into an obscure creed and a complicated philosophy;",
        "Dinler tarihinin gariplikleri arasında — gözlerin ağladığı, kalplerin eridiği bir şey — Mesîh'in hâlis tevhide, her kapalılık ve karmaşadan, her tahriften ve uzak te'vilden uzak kolay ve hoş dine davetinin — yalnız Allah'a kulluğa, O'ndan istemeye, O'na sığınmaya ve O'nu hâlis sevmeye davetin — kapalı bir akîdeye ve karmaşık bir felsefeye dönüşmesidir;", [
  tok("وَمِنْ", "min", "prep", [AT, HJ, MK], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمِنْ حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْمُبْتَدَأُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنَّهُ تَحَوَّلَتْ.", "«and among» — the fronted khabar; the mubtadaʾ is the anna-clause.", "«ve … arasında» — öne alınmış haber; mübtedâ enne cümlesi.", segments=wa_("مِنْ", "min", "prep")),
  majrur("غَرَائِبِ", "gharib", "«the strange things [of]»", "«garipleri»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ لِإِضَافَتِهِ، مُضَافٌ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، جَمْعُ غَرِيبَةٍ."),
  majrur("تَارِيخِ", "tarikh", "«the history [of]»", "«tarihinin»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الْأَدْيَانِ", "din", "«religions»", "«dinlerin»", tags=[JT], punct="،"),
  tok("وَمِمَّا", "ma-mawsula", "pron", [AT, HJ, MW], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ أُدْغِمَتْ فِي مَا الْمَوْصُولَةِ — مَعْطُوفٌ عَلَى الْخَبَرِ.", "«and among what» — joined to the fronted khabar.", "«ve … şeyler arasında» — öne alınmış habere ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("مِ", "min", "prep"), seg("مَّا", "ma-mawsula", "pron")]),
  mudari("تَدْمَعُ", "damaa", "«weep»", "«ağlar»", tags=[MW], hidden=None, extra_ar=" — صِلَةٌ؛ وَفَاعِلُهُ الْعُيُونُ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«at it»", "«ona»"),
  fail("الْعُيُونُ", "ayn", "«eyes»", "«gözler»", tags=[JT], punct="،"),
  mudari_wa("وَتَذُوبُ", "dhaba", "«and melt»", "«ve erir»", tags=["hollow-verbs", MW], hidden=None),
  li_pron("لَهُ", "هُ", "pron-3ms", "«at it»", "«ona»"),
  fail("الْقُلُوبُ", "qalb", "«hearts»", "«kalpler»", tags=[JT], punct="،"),
  tok("أَنَّهُ", "anna", "part", [IW, MK], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that» — anna with the pronoun of the matter; the clause is the delayed mubtadaʾ.", "«-mesidir» — enne, ismi zamîr-i şe'n; cümle sonraya kalan mübtedâ.", segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  mazi_ta("تَحَوَّلَتْ", "tahawwala", "«turned»", "«dönüştü»", tags=[IW, "form-v-verbs"], extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ"),
  fail("دَعْوَةُ", "dawa", "«the call [of]»", "«daveti»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الْمَسِيحِ", "masih", "«the Messiah»", "«Mesîh'in»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("التَّوْحِيدِ", "tawhid", "«tawḥīd»", "«tevhide»"),
  naat("الْخَالِصِ", "khalis", "«pure»", "«hâlis»", tags=["ism-fail"]),
  atf("وَالدِّينِ", "din", "«the religion»", "«ve dine»"),
  naat("السَّهْلِ", "sahl", "«easy»", "«kolay»"),
  naat2("السَّائِغِ", "saigh-palatable", "«palatable»", "«hoş»", case="jarr", tags=["ism-fail", "hollow-verbs"]),
  naat2("الْبَعِيدِ", "baid", "«far»", "«uzak»", case="jarr", n="ثَالِثٌ"),
  tok("عَنْ", "an", "prep", [HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("غُمُوضٍ", "ghumud", "«obscurity»", "«kapalılık»"),
  atf("وَتَعْقِيدٍ", "taqid", "«complication»", "«ve karmaşa»", tags=["form-ii-verbs"], punct="،"),
  atf("وَتَحْرِيفٍ", "tahrif", "«distortion»", "«ve tahrif»", tags=["form-ii-verbs"]),
  atf("وَتَأْوِيلٍ", "tawil", "«interpretation»", "«ve te'vil»", tags=["form-ii-verbs"]),
  naat("بَعِيدٍ", "baid", "«far-fetched»", "«uzak»", punct="،"),
  tok("الدَّعْوَةُ", "dawa", "noun", [BD], "بَدَلٌ مِنْ دَعْوَةُ الْمَسِيحِ مَرْفُوعٌ بِالضَّمَّةِ — بَدَلُ كُلٍّ مِنْ كُلٍّ يُفَسِّرُ الدَّعْوَةَ.", "«the call» — a badal restating «the Messiah's call».", "«davet» — «Mesîh'in daveti»ni açıklayan bedel."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("عِبَادَةِ", "ibada", "«the worship [of]»", "«kulluğa»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'a»"),
  noun_pron("وَحْدَهُ", "wahda", "وَحْدَ", "هُ", "pron-3ms", "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (مَصْدَرٌ فِي مَوْضِعِ الْحَالِ: مُنْفَرِدًا)، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«alone» — a maṣdar as ḥāl, annexed to the pronoun.", "«yalnız, tek başına» — hâl yerinde masdar, zamire muzâf.", tags=[HL, ID], punct="،"),
  atf("وَالسُّؤَالِ", "sual", "«asking»", "«ve istemeye»"),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of Him»", "«O'ndan»", punct="،"),
  atf("وَالِالْتِجَاءِ", "iltija", "«taking refuge»", "«ve sığınmaya»", tags=["form-viii-verbs"]),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«in Him»", "«O'na»", punct="،"),
  pron_atf("وَحُبِّهِ", "hubb", "حُبِّ", "هِ", "pron-3ms", "«love of Him»", "«ve O'nu sevmeye»"),
  naat("الْخَالِصِ", "khalis", "«pure»", "«hâlis»", tags=["ism-fail"], punct="،"),
  prep("إِلَى", "ila", "«into»", "«-e»", ar="حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِتَحَوَّلَتْ (انْتِهَاءُ التَّحَوُّلِ)."),
  majrur("عَقِيدَةٍ", "aqida", "«a creed»", "«bir akîdeye»"),
  naat("غَامِضَةٍ", "ghamid", "«obscure»", "«kapalı»", tags=["ism-fail"], punct="،"),
  atf("وَفَلْسَفَةٍ", "falsafa", "«a philosophy»", "«ve bir felsefeye»"),
  naat("مُعَقَّدَةٍ", "muaqqad", "«complicated»", "«karmaşık»", tags=["ism-maful", "form-ii-verbs"], punct="،"),
])
sen("s5", "for his followers went to excess about him and praised him with a praise by which he passed out of the bounds of humanity into the bounds of divinity; so they said: «The Messiah is the son of God», and they said: «God has taken a son», and they said: «God is the Messiah, son of Maryam».",
        "çünkü tâbileri onun hakkında aşırıya gittiler ve onu öyle bir övgüyle övdüler ki onunla beşeriyet sınırlarından ulûhiyet sınırlarına çıktı; «Mesîh Allah'ın oğludur» dediler, «Allah çocuk edindi» dediler, «Allah, Meryem oğlu Mesîh'tir» dediler.", [
  tok("فَغَلَا", "ghala", "verb", [AT, "naqis-verbs"], "الْفَاءُ لِلتَّعْلِيلِ (أَوِ التَّفْرِيعِ)، وَغَلَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.", "«for … went to excess»", "«çünkü aşırıya gitti»", segments=[seg("فَ", "fa", "conj"), seg("غَلَا", "ghala", "verb")]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«about him»", "«onun hakkında»"),
  noun_pron("أَتْبَاعُهُ", "tabi", "أَتْبَاعُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his followers» — the doer.", "«tâbileri» — fâil.", tags=[FL, ID, JT]),
  tok("وَأَطْرَوْهُ", "atra", "verb", [AT, MB, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَطْرَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and praised him» — a defective Form IV on the group's wāw.", "«ve onu övdüler» — cemi vâvlı nâkıs if'âl.", segments=[seg("وَ", "wa", "conj"), seg("أَطْرَوْ", "atra", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("إِطْرَاءً", "itra", "noun", ["maful-mutlaq", "form-iv-verbs"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«with a praise» — an absolute object.", "«bir övgüyle» — mef'ûl-i mutlak."),
  mazi("خَرَجَ", "kharaja", "«by which he passed out»", "«çıktı»", tags=["jumla-sifa"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِإِطْرَاءً"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«by it»", "«onunla»"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("حُدُودِ", "hadd", "«the bounds [of]»", "«sınırlarından»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْبَشَرِيَّةِ", "bashariyya", "«humanity»", "«beşeriyet»"),
  prep("إِلَى", "ila", "«into»", "«-e»"),
  majrur("حُدُودِ", "hadd", "«the bounds [of]»", "«sınırlarına»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْأُلُوهِيَّةِ", "uluhiyya", "«divinity»", "«ulûhiyet»", punct="؛"),
  fa_qalu(),
  tok("الْمَسِيحُ", "masih", "propn", [MK, IQ], "مُبْتَدَأٌ مَرْفُوعٌ — مَقُولُ الْقَوْلِ، حِكَايَةً لِقَوْلِهِمْ كَمَا فِي الْقُرْآنِ (9:30).", "«the Messiah» — the mubtadaʾ; their saying as the Qurʾān reports it (9:30).", "«Mesîh» — mübtedâ; Kur'ân'ın naklettiği sözleri (9:30)."),
  tok("ابْنُ", "ibn", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the son [of]» — the khabar.", "«oğlu» — haber."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct="."),
  wa_qalu(),
  mazi("اتَّخَذَ", "ittakhadha", "«has taken»", "«edindi»", tags=[IQ, "form-viii-verbs"], hidden=None, extra_ar=" — حِكَايَةً لِقَوْلِهِمْ كَمَا فِي الْقُرْآنِ (2:116)"),
  allah_fail(),
  maful_("وَلَدًا", "walad", "«a son»", "«çocuk»", punct="."),
  wa_qalu(),
  inna(tags=[IQ]),
  tok("اللهَ", "allah", "propn", [IW], "لَفْظُ الْجَلَالَةِ اسْمُ إِنَّ مَنْصُوبٌ — حِكَايَةً لِقَوْلِهِمْ كَمَا فِي الْقُرْآنِ (5:72).", "«God» — inna's ism; their saying as the Qurʾān reports it (5:72).", "«Allah» — inne'nin ismi; Kur'ân'ın naklettiği sözleri (5:72)."),
  tok("هُوَ", "huwa", "pron", ["tawkid", IW], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ.", "«is» — the pronoun of separation.", "«-dır» — fasıl zamiri."),
  tok("الْمَسِيحُ", "masih", "propn", [IW], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — inna's khabar.", "«Mesîh» — inne'nin haberi."),
  tok("ابْنُ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَرْفُوعٌ، مُضَافٌ.", "«son [of]»", "«oğlu»"),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»", punct="."),
])
sen("s6", "And out of the One God, the Eternal Refuge, who neither begot nor was begotten, they made a family composed of three members, each of them a god; so they said: the Father, the Son and the Holy Spirit;",
        "Doğurmamış ve doğurulmamış tek ve Samed olan İlâh'tan, her biri ilâh olan üç üyeden oluşan bir aile yaptılar; «Rab, Oğul ve Kutsal Ruh» dediler;", [
  mazi_pl("وَجَعَلُوا", "jaala", "«and they made»", "«ve yaptılar»", tags=[AT, MX], wa=True),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — جَعَلَ مِنْ كَذَا كَذَا: صَيَّرَهُ.", "«out of»", "«-den»"),
  majrur("الْإِلٰهِ", "ilah", "«the God»", "«İlâh»"),
  naat("الْوَاحِدِ", "wahid", "«One»", "«tek»"),
  naat2("الصَّمَدِ", "samad", "«the Eternal Refuge»", "«Samed»", case="jarr"),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَالِثٌ.", "«who» — the relative, a third naʿt.", "«ki» — üçüncü sıfat olan mevsûl."),
  tok("لَمْ", "lam", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-madı»"),
  tok("يَلِدْ", "walada", "verb", [LJ, MW, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةٌ؛ حُذِفَتْ فَاؤُهُ (الْوَاوُ) فِي الْمُضَارِعِ.", "«begot» — jazm; the assimilated wāw drops in the muḍāriʿ.", "«doğurdu» — meczûm; misâl vâv muzaride düştü."),
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«nor»", "«ve … -madı»", segments=wa_("لَمْ", "lam", "part")),
  tok("يُولَدْ", "walada", "verb", [LJ, NF, "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — ثَبَتَتْ وَاوُهُ فِي الْمَجْهُولِ (يُولَدُ).", "«was begotten» — the passive keeps its wāw (yūladu).", "«doğuruldu» — meçhulde vâv kalır (yûledu).", punct="،"),
  maful_("أُسْرَةً", "usra-family", "«a family»", "«bir aile»", tags=[MX], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  naat("مُؤَلَّفَةً", "muallaf", "«composed»", "«oluşan»", case="nasb", tags=["ism-maful", "form-ii-verbs"]),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("ثَلَاثَةِ", "thalatha", "«three»", "«üç»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — عَدَدٌ مُذَكَّرٌ لِلْمَعْدُودِ الْمُؤَنَّثِ (أَعْضَاء، جَمْعُ عُضْوٍ)؛ وَالْمُؤَلِّفُ ذَكَّرَ الْمَعْدُودَ بِالْمَعْنَى."),
  mudaf_ilayh("أَعْضَاءٍ", "udw", "«members»", "«üye»", tags=[JT], punct="،"),
  noun_pron("كُلُّهُمْ", "kull", "كُلُّ", "هُمْ", "pron-3mp", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِأَعْضَاءٍ (أَوْ حَالٌ).", "«each of them» — a mubtadaʾ; the clause describes the members.", "«her biri» — mübtedâ; cümle üyelerin sıfatı.", tags=[MK, ID, "jumla-sifa"]),
  tok("إِلٰهٌ", "ilah", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a god» — the khabar.", "«ilâh» — haber.", punct="؛"),
  fa_qalu(),
  tok("الرَّبُّ", "rabb", "noun", [MK, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ (هُمُ: الرَّبُّ…)، أَوْ مُبْتَدَأٌ خَبَرُهُ مَحْذُوفٌ — مَقُولُ الْقَوْلِ.", "«the Father» — the khabar of an understood «they are».", "«Rab» — mukadder «onlar»ın haberi."),
  atf("وَالِابْنُ", "ibn", "«the Son»", "«ve Oğul»", "raf"),
  atf("وَرُوحُ", "ruh", "«the Spirit [of]»", "«ve Ruhu»", "raf", tags=[ID], sign="بِالضَّمَّةِ، مُضَافٌ"),
  mudaf_ilayh("الْقُدُسِ", "qudus", "«Holiness»", "«Kutsal»", punct="،"),
])
sen("s7", "and they held a belief about Maryam, the mother of the Messiah, and treated her in a way that brings her to the rank of sanctification and worship; so they said: «the Mother of God»; and statues and images of her spread in the churches, before which the Christians bow with recourse and supplication, vows and prostration;",
        "Mesîh'in annesi Meryem hakkında bir inanç edindiler ve ona, onu takdis ve ibadet derecesine ulaştıracak şekilde muamele ettiler; «Tanrı'nın annesi» dediler; kiliselerde heykelleri ve resimleri yayıldı; Hristiyanlar onların önünde sığınma, dua, adak ve eğilmeyle boyun eğer;", [
  mazi_pl("وَاعْتَقَدُوا", "itaqada", "«and they held a belief»", "«ve bir inanç edindiler»", tags=[AT, "form-viii-verbs"], wa=True),
  fi(),
  tok("مَرْيَمَ", "maryam", "propn", [HJ, MM], "مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Maryam»", "«Meryem»"),
  tok("أُمِّ", "umm", "noun", [BD, ID], "بَدَلٌ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«the mother [of]» — a badal.", "«annesi» — bedel."),
  mudaf_ilayh("الْمَسِيحِ", "masih", "«the Messiah»", "«Mesîh'in»", punct="،"),
  v_pl_pron("وَعَامَلُوهَا", "amala", "عَامَلُو", "هَا", "pron-3fs", "«and treated her»", "«ve ona muamele ettiler»", tags=["form-iii-verbs"], wa=True),
  bi_ma(),
  mudari("يَبْلُغُ", "balagha", "«brings»", "«ulaştırır»", tags=[MW], extra_ar=" — صِلَةٌ"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«her»", "«onu»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("دَرَجَةِ", "daraja", "«the rank [of]»", "«derecesine»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("التَّقْدِيسِ", "taqdis", "«sanctification»", "«takdis»"),
  atf("وَالْعِبَادَةِ", "ibada", "«worship»", "«ve ibadet»", punct="؛"),
  fa_qalu(),
  tok("أُمُّ", "umm", "noun", [MK, ID, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ (هِيَ أُمُّ…)، مُضَافٌ — مَقُولُ الْقَوْلِ.", "«the Mother [of]» — the khabar of an understood «she is».", "«annesi» — mukadder «o»nun haberi."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Tanrı'nın»", punct="."),
  mazi_ta("وَشَاعَتْ", "shaa-spread", "«and spread»", "«ve yayıldı»", tags=[AT, "hollow-verbs"], wa=True),
  li_pron("لَهَا", "هَا", "pron-3fs", "«of her»", "«onun»"),
  fail("تَمَاثِيلُ", "timthal", "«statues»", "«heykelleri»", tags=[JT, MM], extra_ar=" — صِيغَةُ مُنْتَهَى الْجُمُوعِ مَمْنُوعَةٌ مِنَ الصَّرْفِ"),
  atf("وَصُوَرٌ", "sura", "«images»", "«ve resimleri»", "raf", tags=[JT]),
  fi(),
  majrur("الْكَنَائِسِ", "kanisa", "«the churches»", "«kiliselerde»", tags=[JT], punct="،"),
  mudari("يَخْضَعُ", "khadaa-submit", "«bow»", "«boyun eğer»", tags=["jumla-sifa"], hidden=None, extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِتَمَاثِيلُ وَصُوَرٌ (أَوْ حَالٌ)"),
  li_pron("لَهَا", "هَا", "pron-3fs", "«before them»", "«onların önünde»"),
  tok("النَّصَارَى", "nasara-christians", "noun", [FL, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«the Christians» — the doer.", "«Hristiyanlar» — fâil."),
  bi_noun("بِاللُّجُوءِ", "luju", "«with recourse»", "«sığınmayla»"),
  atf("وَالدُّعَاءِ", "dua", "«supplication»", "«ve duayla»", punct="،"),
  atf("وَالتَّنَذُّرِ", "tanadhdhur", "«vows»", "«adakla»", tags=["form-v-verbs"]),
  atf("وَالِانْحِنَاءِ", "inhina", "«prostration»", "«ve eğilmeyle»", tags=["form-vii-verbs"], punct="،"),
])
sen("s8", "and God Most High has said, denying what they believed and finding hideous what they did:",
        "Allah Teâlâ inandıklarını reddederek ve yaptıklarını çirkin bularak buyurmuştur:", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi("قَالَ", "qala", "«said»", "«buyurdu»", tags=["hollow-verbs"], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»"),
  hal("مُنْكِرًا", "munkir", "«denying»", "«reddederek»", tags=["ism-fail", "form-iv-verbs"]),
  ma_mawsul_obj("«what»", "«… -ı»"),
  v_pl_pron("اعْتَقَدُوهُ", "itaqada", "اعْتَقَدُو", "هُ", "pron-3ms", "«they believed»", "«inandıkları»", tags=[MW, "form-viii-verbs"], punct="،"),
  hal("مُسْتَبْشِعًا", "mustabshi", "«finding hideous»", "«çirkin bularak»", tags=["ism-fail", "form-x-verbs"], ar="حَالٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  ma_mawsul_obj("«what»", "«… -ı»"),
  v_pl_pron("فَعَلُوهُ", "faala", "فَعَلُو", "هُ", "pron-3ms", "«they did»", "«yaptıkları»", tags=[MW], punct=":"),
])
sen("s9", "«The Messiah son of Maryam was no more than a messenger; messengers had passed away before him; and his mother was a woman of truth; they both used to eat food. See how We make the signs clear to them; then see how they are turned away.» (5:75)",
        "«Meryem oğlu Mesîh ancak bir resuldür; ondan önce de resuller gelip geçmiştir; annesi de dosdoğru bir kadındı; ikisi de yemek yerlerdi. Bak, âyetleri onlara nasıl açıklıyoruz; sonra bak, nasıl da çevriliyorlar.» (5:75)", [
  *quran([
  tok("مَا", "ma-nafiya", "part", ["la-nafiya", "qasr"], "نَافِيَةٌ لَا عَمَلَ لَهَا — وَالنَّفْيُ مَعَ إِلَّا لِلْحَصْرِ.", "«no [more than]» — the negation with illā restricts.", "«ancak» — illâ ile nefiy hasr için."),
  tok("الْمَسِيحُ", "masih", "propn", [MK], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — the mubtadaʾ.", "«Mesîh» — mübtedâ."),
  tok("ابْنُ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَرْفُوعٌ، مُضَافٌ.", "«son [of]»", "«oğlu»"),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»"),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "qasr"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ (حَصْرٌ).", "«but» — restriction.", "«ancak» — hasr."),
  tok("رَسُولٌ", "rasul", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a messenger» — the khabar.", "«bir resul» — haber."),
  tok("قَدْ", "qad", "part", ["qad-harf", "jumla-sifa"], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لِرَسُولٌ (أَوْ حَالٌ).", "«[already]» — the clause describes «a messenger».", "«[zaten]» — cümle resulün sıfatı."),
  mazi_ta("خَلَتْ", "khala", "«had passed away»", "«gelip geçmişti»", tags=["jumla-sifa", "naqis-verbs"], extra=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  noun_pron("قَبْلِهِ", "qabla", "قَبْلِ", "هِ", "pron-3ms", "ظَرْفٌ مَجْرُورٌ بِمِنْ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«before him»", "«ondan önce»", tags=[HJ, ID]),
  fail("الرُّسُلُ", "rasul", "«the messengers»", "«resuller»", tags=[JT]),
  noun_pron("وَأُمُّهُ", "umm", "وَأُمُّ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَأُمُّ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his mother» — a mubtadaʾ.", "«ve annesi» — mübtedâ.", tags=[AT, MK, ID]),
  tok("صِدِّيقَةٌ", "siddiqa", "noun", [MK, "sighat-mubalagha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — صِيغَةُ مُبَالَغَةٍ عَلَى فِعِّيل.", "«a woman of truth» — the khabar; an intensive form.", "«dosdoğru bir kadın» — haber; mübalağa sîgası."),
  tok("كَانَا", "kana", "verb", [KN, "hollow-verbs", "al-muthanna"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَأَلِفُ الِاثْنَيْنِ اسْمُهُ — وَالْجُمْلَةُ اسْتِئْنَافٌ بَيَانِيٌّ (أَوْ خَبَرٌ ثَانٍ).", "«they both were» — kāna with the dual alif as its ism.", "«ikisi … idi» — kâne, tesniye elifi ismi.", segments=[seg("كَانَ", "kana", "verb"), seg("ا", "pron-3md", "pron")]),
  tok("يَأْكُلَانِ", "akala", "verb", [KN, AK, "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ كَانَ.", "«used to eat» — one of the five verbs with the dual alif; kāna's khabar.", "«yerlerdi» — tesniye elifli ef'âl-i hamseden; kâne'nin haberi."),
  maful_("الطَّعَامَ", "taam", "«food»", "«yemek»"),
  tok("انْظُرْ", "nazara", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«see»", "«bak»"),
  tok("كَيْفَ", "kayfa", "pron", [IS, HL], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ انْظُرْ (مُعَلَّقٌ بِالِاسْتِفْهَامِ).", "«how» — the interrogative as a ḥāl; the clause is the object of «see».", "«nasıl» — hâl olan istifhâm ismi; cümle «bak»ın mef'ûlü."),
  mudari("نُبَيِّنُ", "bayyana", "«We make clear»", "«açıklıyoruz»", tags=["form-ii-verbs"], hidden="نَحْنُ"),
  li_pron("لَهُمُ", "هُمُ", "pron-3mp", "«to them»", "«onlara»", extra=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  maful_("الْآيَاتِ", "aya", "«the signs»", "«âyetleri»", tags=[JM], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ."),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then»", "«sonra»"),
  tok("انْظُرْ", "nazara", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«see»", "«bak»"),
  tok("أَنَّى", "anna-istifham", "pron", [IS, HL], "اسْمُ اسْتِفْهَامٍ بِمَعْنَى كَيْفَ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — an interrogative as ḥāl.", "«nasıl» — hâl olan istifhâm ismi."),
  tok("يُؤْفَكُونَ", "afaka", "verb", [NF, AK, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — أُفِكَ عَنِ الشَّيْءِ: صُرِفَ عَنْهُ.", "«they are turned away» — a passive of the five verbs.", "«çevriliyorlar» — ef'âl-i hamseden meçhul.", punct=AYA),
  ]),
])
sen("s10", "«Say: Do you worship, besides God, what has no power to harm or benefit you? And God — He is the All-Hearing, the All-Knowing.» (5:76)",
        "«De ki: Allah'ı bırakıp size ne zarar ne fayda vermeye gücü yeten şeye mi tapıyorsunuz? Allah, işiten ve bilendir.» (5:76)", [
  *quran([
  tok("قُلْ", "qala", "verb", [AM, "hollow-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«say» — the hollow imperative; the wāw drops.", "«de» — ecvef emir; vâv düştü."),
  tok("أَتَعْبُدُونَ", "abada", "verb", [IS, AK, "mudari-marfu"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَتَعْبُدُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«do you worship» — the hamza of rebuke.", "«tapıyor musunuz» — inkârî istifhâm hemzesi.", segments=[seg("أَ", "hamza-istifham", "part"), seg("تَعْبُدُونَ", "abada", "verb")]),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ — مِنْ دُونِ اللهِ: غَيْرَهُ.", "«besides [God]»", "«… bırakıp»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»"),
  ma_mawsul_obj("«what»", "«… şeye»"),
  la_nafiya(),
  neg_mudari("يَمْلِكُ", "malaka", "«has power»", "«gücü yeter»", tags=[MW], hidden="هُوَ", extra=" — صِلَةٌ"),
  li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«for you»", "«size»"),
  maful_("ضَرًّا", "darr", "«harm»", "«zarar»", tags=["doubled-verbs"]),
  la_nafiya("وَلَا", wa=True),
  tok("نَفْعًا", "naf", "noun", [AT, MB], "مَعْطُوفٌ عَلَى ضَرًّا مَنْصُوبٌ بِالْفَتْحَةِ.", "«benefit» — joined to «harm».", "«fayda» — «zarar»a ma'tûf."),
  tok("وَاللهُ", "allah", "propn", [AT, MK], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.", "«and God» — the mubtadaʾ.", "«ve Allah» — mübtedâ.", segments=wa_("اللهُ", "allah", "propn")),
  tok("هُوَ", "huwa", "pron", ["tawkid", MK], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ مُبْتَدَأٌ ثَانٍ).", "«He» — the pronoun of separation.", "«O» — fasıl zamiri."),
  tok("السَّمِيعُ", "sami", "noun", [MK, "sighat-mubalagha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the All-Hearing» — the khabar.", "«işiten» — haber."),
  tok("الْعَلِيمُ", "alim", "noun", [MK, "sighat-mubalagha"], "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«the All-Knowing» — a second khabar.", "«bilen» — ikinci haber.", punct=AYA),
  ]),
])

CAND = {
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "akmala": G("akmala", "أَكْمَلَ", "ك م ل", "verb", "to complete (Form IV)", "tamamlamak (if'âl)", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "muhimma": G("muhimma", "مُهِمَّة", "ه م م", "noun", "a task, a mission", "görev, vazife", 1, plural="مُهِمَّات"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "a call, an invitation; a mission", "davet, çağrı", 1),
 "shidda": G("shidda", "شِدَّة", "ش د د", "noun", "intensity, severity", "şiddet", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "muharaba": G("muharaba", "مُحَارَبَة", "ح ر ب", "noun", "warring, fighting (the maṣdar of Form III)", "savaşma, muharebe (müfâale masdarı)", 2),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "kayd": G("kayd", "كَيْد", "ك ي د", "noun", "a plot, scheming", "tuzak, hile", 2),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "daf": G("daf", "ضَعْف", "ض ع ف", "noun", "weakness", "zayıflık", 1),
 "qilla": G("qilla", "قِلَّة", "ق ل ل", "noun", "fewness, scarcity", "azlık", 1),
 "nasir": G("nasir", "نَصِير", "ن ص ر", "noun", "a helper, a supporter", "yardımcı, nasîr", 1, plural="أَنْصَار"),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "waddaa": G("waddaa", "وَدَّعَ", "و د ع", "verb", "to bid farewell (Form II)", "veda etmek, uğurlamak (tef'îl)", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "imtathala": G("imtathala", "اِمْتَثَلَ", "م ث ل", "verb", "to obey, to comply with (Form VIII)", "uymak, itaat etmek (iftiâl)", 2),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1, plural="أُمُور"),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "bashshara": G("bashshara", "بَشَّرَ", "ب ش ر", "verb", "to give glad tidings (Form II)", "müjdelemek (tef'îl)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resul", 1, plural="رُسُل"),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come (defective)", "gelmek (nâkıs)", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "bad-after": G("bad-after", "بَعْدَ", "ب ع د", "noun", "after", "-den sonra", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "badaa": G("badaa", "بَدَأَ", "ب د أ", "verb", "to begin", "başlamak", 1),
 "ammama": G("ammama", "عَمَّمَ", "ع م م", "verb", "to generalize, to make universal (Form II)", "umumî kılmak, genelleştirmek (tef'îl)", 2),
 "khassasa": G("khassasa", "خَصَّصَ", "خ ص ص", "verb", "to particularize, to specify (Form II)", "hususî kılmak, özgülemek (tef'îl)", 2),
 "tamma": G("tamma", "تَمَّ", "ت م م", "verb", "to be complete (doubled)", "tamamlanmak (muzâaf)", 2),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a favour, a blessing", "nimet", 1, plural="نِعَم"),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, against", "üzerine, -e karşı", 1),
 "ibad": G("ibad", "عِبَاد", "ع ب د", "noun", "servants (of God)", "kullar", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to rise, to stand (hollow)", "kalkmak, ayağa kalkmak (ecvef)", 1),
 "hujja": G("hujja", "حُجَّة", "ح ج ج", "noun", "a proof, an argument", "hüccet, delil", 1, plural="حُجَج"),
 "khalq": G("khalq", "خَلْق", "خ ل ق", "noun", "creation; creatures", "yaratma; yaratıklar", 1),
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "ibn": G("ibn", "ابْن", "ب ن ي", "noun", "a son", "oğul", 1, plural="أَبْنَاء"),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "banu-israil": G("banu-israil", "بَنُو إِسْرَائِيلَ", "ب ن ي", "noun", "the Children of Israel", "İsrâiloğulları", 1),
 "israil": G("israil", "إِسْرَائِيل", None, "propn", "Israel (Yaʿqūb)", "İsrâil (Yâkub)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (pl.)", "siz / sizi / sizin", 1),
 "musaddiq": G("musaddiq", "مُصَدِّق", "ص د ق", "noun", "confirming (an active participle of Form II)", "doğrulayan, tasdik edici (tef'îl ism-i fâili)", 2),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1, plural="أَيْدٍ"),
 "tawrat": G("tawrat", "التَّوْرَاة", None, "propn", "the Torah", "Tevrat", 1),
 "mubashshir": G("mubashshir", "مُبَشِّر", "ب ش ر", "noun", "a bringer of glad tidings (an active participle of Form II)", "müjdeleyici (tef'îl ism-i fâili)", 2),
 "ism": G("ism", "اِسْم", "س م و", "noun", "a name", "isim", 1, plural="أَسْمَاء"),
 "ahmad": G("ahmad", "أَحْمَد", "ح م د", "propn", "Aḥmad (a name of the Prophet Muḥammad)", "Ahmed (Hz. Muhammed'in bir ismi)", 1),
 "gharib": G("gharib", "غَرِيب", "غ ر ب", "noun", "strange; a stranger; (pl. gharāʾib) strange things", "garip, yabancı; (ç. garâib) gariplikler", 1, plural="غُرَبَاء / غَرَائِب"),
 "tarikh": G("tarikh", "تَارِيخ", "أ ر خ", "noun", "history", "tarih", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1, plural="أَدْيَان"),
 "damaa": G("damaa", "دَمَعَ", "د م ع", "verb", "to shed tears, to water (of the eye)", "yaşarmak, ağlamak", 2),
 "ayn": G("ayn", "عَيْن", "ع ي ن", "noun", "an eye; a spring", "göz; pınar", 1, plural="عُيُون"),
 "dhaba": G("dhaba", "ذَابَ", "ذ و ب", "verb", "to melt (hollow)", "erimek (ecvef)", 1),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "a heart", "kalp", 1, plural="قُلُوب"),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "tahawwala": G("tahawwala", "تَحَوَّلَ", "ح و ل", "verb", "to turn (ilā: into), to change (Form V)", "dönüşmek (tefa''ul)", 1),
 "tawhid": G("tawhid", "تَوْحِيد", "و ح د", "noun", "tawḥīd, the affirming of God's oneness", "tevhid", 1),
 "khalis": G("khalis", "خَالِص", "خ ل ص", "noun", "pure, sincere (an active participle)", "hâlis, katıksız (ism-i fâil)", 1),
 "sahl": G("sahl", "سَهْل", "س ه ل", "noun", "easy", "kolay", 1),
 "saigh-palatable": G("saigh-palatable", "سَائِغ", "س و غ", "noun", "palatable, easy to swallow (an active participle)", "hoş, kolay sindirilir (ism-i fâil)", 3),
 "baid": G("baid", "بَعِيد", "ب ع د", "noun", "far, distant; far-fetched", "uzak", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "ghumud": G("ghumud", "غُمُوض", "غ م ض", "noun", "obscurity", "kapalılık, muğlaklık", 2),
 "taqid": G("taqid", "تَعْقِيد", "ع ق د", "noun", "complication (the maṣdar of Form II)", "karmaşa, karmaşıklaştırma (tef'îl masdarı)", 2),
 "tahrif": G("tahrif", "تَحْرِيف", "ح ر ف", "noun", "distortion, tampering (the maṣdar of Form II)", "tahrif (tef'îl masdarı)", 2),
 "tawil": G("tawil", "تَأْوِيل", "أ و ل", "noun", "interpretation (the maṣdar of Form II)", "te'vil, yorum (tef'îl masdarı)", 2),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet, kulluk", 1, plural="عِبَادَات"),
 "wahda": G("wahda", "وَحْد", "و ح د", "noun", "alone (waḥdahu: by himself)", "tek, yalnız (vahdehu: tek başına)", 1),
 "sual": G("sual", "سُؤَال", "س أ ل", "noun", "a question, a request; asking", "soru, istek; isteme", 1, plural="أَسْئِلَة"),
 "iltija": G("iltija", "اِلْتِجَاء", "ل ج أ", "noun", "taking refuge (the maṣdar of Form VIII)", "sığınma, iltica (iftiâl masdarı)", 2),
 "hubb": G("hubb", "حُبّ", "ح ب ب", "noun", "love", "sevgi", 1),
 "aqida": G("aqida", "عَقِيدَة", "ع ق د", "noun", "a creed", "akîde", 1, plural="عَقَائِد"),
 "ghamid": G("ghamid", "غَامِض", "غ م ض", "noun", "obscure (an active participle)", "kapalı, muğlak (ism-i fâil)", 2),
 "falsafa": G("falsafa", "فَلْسَفَة", None, "noun", "philosophy", "felsefe", 1),
 "muaqqad": G("muaqqad", "مُعَقَّد", "ع ق د", "noun", "complicated (a passive participle of Form II)", "karmaşık (tef'îl ism-i mef'ûlü)", 2),
 "ghala": G("ghala", "غَلَا", "غ ل و", "verb", "to go to excess (fī: in) (defective)", "aşırıya gitmek (nâkıs)", 2),
 "tabi": G("tabi", "تَابِع", "ت ب ع", "noun", "a follower (an active participle)", "tâbi, izleyen (ism-i fâil)", 1, plural="أَتْبَاع"),
 "atra": G("atra", "أَطْرَى", "ط ر و", "verb", "to praise lavishly (Form IV, defective)", "aşırı övmek (if'âl, nâkıs)", 3),
 "itra": G("itra", "إِطْرَاء", "ط ر و", "noun", "lavish praise (the maṣdar of Form IV)", "aşırı övgü (if'âl masdarı)", 3),
 "kharaja": G("kharaja", "خَرَجَ", "خ ر ج", "verb", "to go out, to pass out (min: of)", "çıkmak", 1),
 "hadd": G("hadd", "حَدّ", "ح د د", "noun", "a limit, a bound", "sınır, had", 1, plural="حُدُود"),
 "bashariyya": G("bashariyya", "بَشَرِيَّة", "ب ش ر", "noun", "humanity, the human condition (an abstract nisba)", "beşeriyet (masdar-ı sınâî)", 2),
 "uluhiyya": G("uluhiyya", "أُلُوهِيَّة", "أ ل ه", "noun", "divinity (an abstract nisba)", "ulûhiyet (masdar-ı sınâî)", 2),
 "ittakhadha": G("ittakhadha", "اِتَّخَذَ", "أ خ ذ", "verb", "to take, to adopt (two objects) (Form VIII)", "edinmek (iki mef'ûl) (iftiâl)", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child, a son", "çocuk, oğul", 1, plural="أَوْلَاد"),
 "huwa": G("huwa", "هُوَ", None, "pron", "he / it", "o", 1),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make, to set (two objects)", "kılmak, yapmak (iki mef'ûl)", 1),
 "ilah": G("ilah", "إِلَه", "أ ل ه", "noun", "a god", "ilâh", 1, plural="آلِهَة"),
 "wahid": G("wahid", "وَاحِد", "و ح د", "noun", "one, single", "bir, tek", 1),
 "samad": G("samad", "صَمَد", "ص م د", "noun", "the Eternal Refuge (a name of God)", "Samed (Allah'ın bir ismi)", 2),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which (m.)", "ki o, -an", 1),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to beget, to give birth; (passive) to be born (an assimilated verb)", "doğurmak; (meçhul) doğmak (misâl fiil)", 1),
 "usra-family": G("usra-family", "أُسْرَة", "أ س ر", "noun", "a family", "aile", 1, plural="أُسَر"),
 "muallaf": G("muallaf", "مُؤَلَّف", "أ ل ف", "noun", "composed (min: of) (a passive participle of Form II)", "oluşan, müellef (tef'îl ism-i mef'ûlü)", 2),
 "thalatha": G("thalatha", "ثَلَاثَة", "ث ل ث", "noun", "three", "üç", 1),
 "udw": G("udw", "عُضْو", "ع ض و", "noun", "a member, a limb", "üye, uzuv", 2, plural="أَعْضَاء"),
 "ruh": G("ruh", "رُوح", "ر و ح", "noun", "spirit, soul", "ruh", 1, plural="أَرْوَاح"),
 "qudus": G("qudus", "قُدُس", "ق د س", "noun", "holiness; (rūḥ al-qudus) the Holy Spirit", "kutsallık; (rûhu'l-kudüs) Cebrâil", 2),
 "itaqada": G("itaqada", "اِعْتَقَدَ", "ع ق د", "verb", "to believe firmly (Form VIII)", "inanmak, itikat etmek (iftiâl)", 1),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "amala": G("amala", "عَامَلَ", "ع م ل", "verb", "to treat, to deal with (Form III)", "muamele etmek (müfâale)", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "balagha": G("balagha", "بَلَغَ", "ب ل غ", "verb", "to reach; (bihi) to bring to", "ulaşmak; (bihi) ulaştırmak", 1),
 "daraja": G("daraja", "دَرَجَة", "د ر ج", "noun", "a degree, a rank", "derece", 1, plural="دَرَجَات"),
 "taqdis": G("taqdis", "تَقْدِيس", "ق د س", "noun", "sanctifying (the maṣdar of Form II)", "kutsama, takdis (tef'îl masdarı)", 2),
 "shaa-spread": G("shaa-spread", "شَاعَ", "ش ي ع", "verb", "to spread, to become widespread (hollow)", "yayılmak (ecvef)", 2),
 "timthal": G("timthal", "تِمْثَال", "م ث ل", "noun", "a statue", "heykel", 1, plural="تَمَاثِيل"),
 "sura": G("sura", "صُورَة", "ص و ر", "noun", "an image, a picture; a form", "resim, sûret; şekil", 1, plural="صُوَر"),
 "kanisa": G("kanisa", "كَنِيسَة", "ك ن س", "noun", "a church", "kilise", 1, plural="كَنَائِس"),
 "khadaa-submit": G("khadaa-submit", "خَضَعَ", "خ ض ع", "verb", "to submit, to bow (li: to)", "boyun eğmek (li ile)", 1),
 "nasara-christians": G("nasara-christians", "النَّصَارَى", "ن ص ر", "noun", "the Christians", "Hristiyanlar, Nasrânîler", 1),
 "luju": G("luju", "لُجُوء", "ل ج أ", "noun", "recourse, resorting (ilā: to)", "sığınma, başvurma", 2),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "supplication, prayer", "dua", 1),
 "tanadhdhur": G("tanadhdhur", "تَنَذُّر", "ن ذ ر", "noun", "making vows (the maṣdar of Form V)", "adak adama (tefa''ul masdarı)", 3),
 "inhina": G("inhina", "اِنْحِنَاء", "ح ن و", "noun", "bowing, bending (the maṣdar of Form VII)", "eğilme (infiâl masdarı)", 2),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "munkir": G("munkir", "مُنْكِر", "ن ك ر", "noun", "denying, a denier (an active participle of Form IV)", "inkâr eden (if'âl ism-i fâili)", 1),
 "mustabshi": G("mustabshi", "مُسْتَبْشِع", "ب ش ع", "noun", "finding hideous (an active participle of Form X)", "çirkin bulan (istif'âl ism-i fâili)", 3),
 "faala": G("faala", "فَعَلَ", "ف ع ل", "verb", "to do", "yapmak", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā)", "değil, yok (nefiy mâ'sı)", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "khala": G("khala", "خَلَا", "خ ل و", "verb", "to pass away, to be empty (defective)", "gelip geçmek, boş olmak (nâkıs)", 1),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "-den önce", 1),
 "siddiqa": G("siddiqa", "الصِّدِّيقَة", "ص د ق", "noun", "a woman of truth, eminently truthful (an intensive form)", "dosdoğru kadın, sıddîka (mübalağa sîgası)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "pron-3md": G("pron-3md", "ـا (أَلِفُ الِاثْنَيْنِ)", None, "pron", "they two (the dual alif)", "o ikisi (tesniye elifi)", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "taam": G("taam", "طَعَام", "ط ع م", "noun", "food", "yemek, yiyecek", 1),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look, to see", "bakmak", 1),
 "kayfa": G("kayfa", "كَيْفَ", None, "pron", "how", "nasıl", 1),
 "bayyana": G("bayyana", "بَيَّنَ", "ب ي ن", "verb", "to make clear (Form II)", "açıklamak (tef'îl)", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "anna-istifham": G("anna-istifham", "أَنَّى", None, "pron", "how, whence (interrogative)", "nasıl, nereden (istifhâm)", 2),
 "afaka": G("afaka", "أَفَكَ", "أ ف ك", "verb", "to turn away; (passive) to be turned away, deluded", "çevirmek; (meçhul) çevrilmek, saptırılmak", 3),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "tapmak, ibadet etmek", 1),
 "hamza-istifham": G("hamza-istifham", "أَ (هَمْزَةُ الِاسْتِفْهَامِ)", None, "part", "the interrogative hamza", "istifhâm hemzesi", 1),
 "duna": G("duna", "دُونَ", "د و ن", "noun", "below; besides, other than", "aşağısında; -den başka", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "malaka": G("malaka", "مَلَكَ", "م ل ك", "verb", "to possess, to have power over", "sahip olmak, gücü yetmek", 1),
 "darr": G("darr", "ضَرّ", "ض ر ر", "noun", "harm", "zarar", 1),
 "naf": G("naf", "نَفْع", "ن ف ع", "noun", "benefit", "fayda", 1),
 "sami": G("sami", "سَمِيع", "س م ع", "noun", "all-hearing (an intensive form)", "işiten, Semî' (mübalağa sîgası)", 1),
 "alim": G("alim", "عَلِيم", "ع ل م", "noun", "all-knowing (an intensive form)", "bilen, Alîm (mübalağa sîgası)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "ammama", _sg.derived(_sg.B2, _sg.W2, "ُ", "عَمَّم", "عَمِّم", "عَمِّم", "تَعْمِيم", "مُعَمِّم", "مُعَمَّم", "عُمِّمَ", "يُعَمَّمُ", "عَمَّمَ الْحُكْمَ: جَعَلَهُ عَامًّا شَامِلًا."))
put_morph(mo, "khassasa", _sg.derived(_sg.B2, _sg.W2, "ُ", "خَصَّص", "خَصِّص", "خَصِّص", "تَخْصِيص", "مُخَصِّص", "مُخَصَّص", "خُصِّصَ", "يُخَصَّصُ", "خَصَّصَ الشَّيْءَ: جَعَلَهُ خَاصًّا."))
put_morph(mo, "damaa", _sg.sound1("fataha", "دَمَع", "دْمَع", "اِدْمَع", "دَمْع", "دَامِع", None, None, None, "دَمَعَتِ الْعَيْنُ تَدْمَعُ: سَالَ دَمْعُهَا."))
put_morph(mo, "dhaba", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "ذَاب", "ذُب", "ذُوب", "ذُب", "ذُب", "ذُب", "ذَوْب / ذَوَبَان", "ذَائِب", None, None, None, "ذَابَ الشَّيْءُ يَذُوبُ: سَالَ بَعْدَ جُمُودٍ — أَجْوَفُ وَاوِيٌّ؛ لَمْ يَذُبْ."))
put_morph(mo, "tahawwala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَوَّل", "تَحَوَّل", "تَحَوَّل", "تَحَوُّل", "مُتَحَوِّل", None, None, None, "تَحَوَّلَ الشَّيْءُ إِلَى كَذَا: صَارَ إِلَيْهِ وَانْتَقَلَ."))
put_morph(mo, "atra", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَطْرَ", "طْر", "i", "أَطْر", "إِطْرَاء", "مُطْرٍ (الْمُطْرِي)", "مُطْرًى", "أُطْرِيَ", "يُطْرَى", "أَطْرَاهُ: مَدَحَهُ وَبَالَغَ فِي مَدْحِهِ — نَاقِصٌ: يُطْرِي، لَمْ يُطْرِ."))
put_morph(mo, "shaa-spread", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "شَاع", "شِع", "شِيع", "شِع", "شِع", "شِع", "شُيُوع", "شَائِع", None, None, None, "شَاعَ الْخَبَرُ يَشِيعُ: ذَاعَ وَانْتَشَرَ — أَجْوَفُ يَائِيٌّ؛ لَمْ يَشِعْ."))
put_morph(mo, "afaka", _sg.sound1("daraba", "أَفَك", "أْفِك", "اِيفِك", "إِفْك / أَفْك", "آفِك", "مَأْفُوك", "أُفِكَ", "يُؤْفَكُ", "أَفَكَهُ عَنِ الشَّيْءِ يَأْفِكُهُ: صَرَفَهُ عَنْهُ؛ وَأُفِكَ: صُرِفَ وَخُدِعَ — مَهْمُوزُ الْفَاءِ.", cls="مَهْمُوزُ الْفَاءِ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch42 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 42 (print pp. 62–64; ʿĪsā §36–37): his task left incomplete; farewell and the tidings of a messenger after him, with al-Ṣaff 61:6 «whose name is Aḥmad» (s1–s3); from pure tawḥīd to an obscure creed — the Messiah exalted to divinity, «God has taken a son», the trinity, Maryam venerated with statues (s4–s8); al-Māʾida 5:75–76 «the Messiah was no more than a messenger… they both used to eat food» (s9–s10)."
ADD_TR = " Kırk ikinci bölüm (baskı s. 62–64; Îsâ §36–37): tamamlanamayan görev; veda ve kendisinden sonraki resulün müjdesi, Saff 6 «adı Ahmed» ile (s1–s3); hâlis tevhidden kapalı akîdeye — ulûhiyete yükseltilen Mesîh, «Allah çocuk edindi», teslis, heykellerle yüceltilen Meryem (s4–s8); Mâide 75–76 «Mesîh ancak bir resuldür… ikisi de yemek yerlerdi» (s9–s10)."
write_out(42, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §36–37 + 61:6, 5:75–76", GLOSS_ADD, notes=(), related=())
report(42, S, GLOSS_ADD, ())
