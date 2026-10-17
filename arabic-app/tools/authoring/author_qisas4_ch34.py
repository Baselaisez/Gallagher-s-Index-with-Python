# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 34: «قِصَّةُ عِيسَى» §13 — his life and his call in the Qurʾān: Maryam 19:30–33 (the infant speaks: «I am the servant of God», blessed wherever he is, prayer and zakāt, dutiful to his mother, «peace upon me the day I was born, the day I die and the day I am raised alive»); print p. 49.
python3 tools/authoring/author_qisas4_ch34.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: سِيرَتُهُ وَدَعْوَتُهُ فِي الْقُرْآنِ (مريم ٣٠–٣٣)", "en": "The story of ʿĪsā: his life and his call in the Qurʾān (19:30–33)", "tr": "Îsâ'nın kıssası: Kur'ân'da sîreti ve daveti (Meryem 30–33)"}
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
    return tok(full, lex, "verb", [AT, "mudari-marfu"] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + full[2:] + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ " + sign + "، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", "«and» + " + en + " — a muḍāriʿ in rafʿ; the doer is concealed.", "«ve» + " + tr + " — merfû muzari; fâil gizli.", punct=punct, segments=wa_(full[2:], lex, "verb"))
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

def jaalani(wa=True):
    return tok(("وَ" if wa else "") + "جَعَلَنِي", "jaala", "verb", ([AT] if wa else []) + [MX], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "جَعَلَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", ("«and» + " if wa else "") + "«He made me» — two objects; the yāʾ is the first, after the nūn of protection.", ("«ve» + " if wa else "") + "«beni … kıldı» — iki mef'ûl; vikâye nûnundan sonraki yâ ilki.", segments=([seg("وَ", "wa", "conj")] if wa else []) + [seg("جَعَلَ", "jaala", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
def wa_yawma():
    return tok("وَيَوْمَ", "yawm", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَيَوْمَ ظَرْفُ زَمَانٍ مَعْطُوفٌ مَنْصُوبٌ، مُضَافٌ.", "«and the day»", "«ve … günü»", segments=wa_("يَوْمَ", "yawm", "noun"))

# ---------------------------------------------------------------- §13 سِيرَتُهُ وَدَعْوَتُهُ فِي الْقُرْآنِ (print p. 49)
sen("s1", "And read the Most High's description of his life and his call, in His words:",
        "Allah Teâlâ'nın onun sîretini ve davetini şu sözünde nasıl vasfettiğini de okuyun:", [
  tok("وَاقْرَؤُوا", "qaraa", "verb", [AT, AM], "الْوَاوُ عَاطِفَةٌ، وَاقْرَؤُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and read» — an imperative on the group's wāw.", "«ve okuyun» — cemi vâvlı emir.", segments=wa_("اقْرَؤُوا", "qaraa", "verb")),
  noun_pron("وَصْفَهُ", "wasf", "وَصْفَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالضَّمِيرُ لِلّٰهِ تَعَالَى.", "«His description» — the object; the pronoun is God's.", "«O'nun vasfını» — mef'ûl; zamir Allah'a râcidir.", tags=[MB, ID]),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ بَعْدَ ضَمِيرِ الْجَلَالَةِ.", "«the Most High» — a parenthetical prayer after the pronoun for God.", "«Teâlâ» — Allah'a râci zamirden sonra duâ cümlesi."),
  tok("لِسِيرَتِهِ", "sira", "noun", [HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَسِيرَتِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِوَصْفَهُ.", "«of his life» — attached to «description».", "«sîretini» — «vasf»a bağlı.", segments=[seg("لِ", "li", "prep"), seg("سِيرَتِ", "sira", "noun"), seg("هِ", "pron-3ms", "pron")]),
  pron_atf("وَدَعْوَتِهِ", "dawa", "دَعْوَتِ", "هِ", "pron-3ms", "«his call»", "«davetini»", punct="،"),
  fi(),
  noun_pron("قَوْلِهِ", "qawl", "قَوْلِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His words»", "«sözünde»", tags=[HJ, ID], punct=":"),
])
sen("s2", "«He said: I am the servant of God; He has given me the Book and made me a prophet.» (19:30)",
        "«Dedi: Ben Allah'ın kuluyum; O bana Kitab'ı verdi ve beni peygamber kıldı.» (19:30)", [
  *quran([
  mazi("قَالَ", "qala", "«he said»", "«dedi»", tags=["hollow-verbs"], hidden="هُوَ", extra_ar=" — أَيْ عِيسَى فِي الْمَهْدِ"),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "«indeed I» — inna with the yāʾ.", "«şüphesiz ben» — inne; yâ ismi.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("عَبْدُ", "abd", "noun", [IW, ID], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the servant [of]» — inna's khabar.", "«kulu» — inne'nin haberi."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("آتَانِيَ", "aata-bring", "verb", [MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ (فُتِحَتْ لِالْتِقَاءِ السَّاكِنَيْنِ) — وَالْجُمْلَةُ خَبَرٌ ثَانٍ لِإِنَّ (أَوْ حَالٌ).", "«He has given me» — two objects; the yāʾ after the nūn of protection is the first, with a fatḥa before the waṣl.", "«bana verdi» — iki mef'ûl; vikâye nûnundan sonraki yâ ilki, vasl öncesi fethalı.", segments=[seg("آتَا", "aata-bring", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("يَ", "pron-1s", "pron")]),
  maful_("الْكِتَابَ", "kitab", "«the Book»", "«Kitab'ı»", tags=[MX], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  jaalani(),
  maful_("نَبِيًّا", "nabi", "«a prophet»", "«peygamber»", tags=[MX], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", punct=AYA),
  ]),
])
sen("s3", "«And He made me blessed wherever I am, and enjoined on me prayer and zakāt as long as I live,» (19:31)",
        "«Nerede olursam olayım beni mübarek kıldı; hayatta olduğum sürece bana namazı ve zekâtı emretti,» (19:31)", [
  *quran([
  jaalani(),
  maful_("مُبَارَكًا", "mubarak", "«blessed»", "«mübarek»", tags=[MX, "ism-maful", "form-iii-verbs"], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  tok("أَيْنَ", "ayna", "pron", [SH, MF], "اسْمُ شَرْطٍ جَازِمٌ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ ظَرْفٌ، مُتَعَلِّقٌ بِمُبَارَكًا (أَوْ بِخَبَرِ كُنْتُ).", "«wherever» — a jussive conditional noun of place.", "«nerede» — cezm eden mekân şart ismi."),
  tok("مَا", "ma-zaida", "part", ["tawkid"], "زَائِدَةٌ لِلتَّوْكِيدِ بَعْدَ أَيْنَ.", "«-ever» — an extra mā of emphasis.", "«… olursa» — te'kid için zâid mâ."),
  tok("كُنْتُ", "kana", "verb", [SH, KN, "hollow-verbs", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهُ، وَخَبَرُهُ مَحْذُوفٌ: كَائِنًا؛ وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«I am» — the condition's verb; its khabar and the answer are understood.", "«olursam» — şart fiili; haberi ve cevabı mahzuf.", segments=[seg("كُنْ", "kana", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("وَأَوْصَانِي", "awsa", "verb", [AT, MB, "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَوْصَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«and enjoined on me» — a defective Form IV; the yāʾ is the object.", "«ve bana emretti» — nâkıs if'âl; yâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("أَوْصَا", "awsa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  bi_noun("بِالصَّلَاةِ", "salat", "«prayer»", "«namazı»"),
  atf("وَالزَّكَاةِ", "zakat", "«zakāt»", "«zekâtı»"),
  tok("مَا", "ma-masdariyya", "part", [MF], "مَصْدَرِيَّةٌ ظَرْفِيَّةٌ — أَيْ: مُدَّةَ دَوَامِي حَيًّا.", "«as long as» — the maṣdarī mā of duration.", "«… -dığım sürece» — zarfiyye masdariyye mâ."),
  tok("دُمْتُ", "dama", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهُ — حُذِفَتْ عَيْنُهُ (الْأَلِفُ) لِالْتِقَاءِ السَّاكِنَيْنِ: دُمْتُ.", "«I live» — dāma; the hollow alif drops before the tāʾ.", "«hayatta olduğum» — dâme; ecvef elif tâ önünde düştü.", segments=[seg("دُمْ", "dama", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("حَيًّا", "hayy", "noun", [KN], "خَبَرُ دَامَ مَنْصُوبٌ بِالْفَتْحَةِ.", "«alive» — dāma's khabar.", "«diri» — dâme'nin haberi.", punct=AYA),
  ]),
])
sen("s4", "«and dutiful to my mother; and He has not made me a tyrant, wretched.» (19:32)",
        "«anneme itaatkâr kıldı; beni zorba ve bedbaht kılmadı.» (19:32)", [
  *quran([
  tok("وَبَرًّا", "barr", "noun", [AT, MX], "الْوَاوُ عَاطِفَةٌ، وَبَرًّا مَعْطُوفٌ عَلَى مُبَارَكًا مَنْصُوبٌ (مَفْعُولٌ ثَانٍ لِجَعَلَنِي) — مَصْدَرٌ وُصِفَ بِهِ، أَوْ صِفَةٌ مُشَبَّهَةٌ.", "«and dutiful» — joined to «blessed» as the second object.", "«ve itaatkâr» — «mübarek»e ma'tûf ikinci mef'ûl.", segments=wa_("بَرًّا", "barr", "noun")),
  tok("بِوَالِدَتِي", "walida-mother", "noun", [HJ, ID, "ya-al-mutakallim"], "الْبَاءُ حَرْفُ جَرٍّ، وَوَالِدَتِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِبَرًّا.", "«to my mother» — attached to «dutiful».", "«anneme» — «itaatkâr»a bağlı.", segments=[seg("بِ", "bi", "prep"), seg("وَالِدَتِ", "walida-mother", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … -madı»", segments=wa_("لَمْ", "lam", "part")),
  tok("يَجْعَلْنِي", "jaala", "verb", [LJ, MX], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«He has made me» — jazm by sukūn; the yāʾ is the first object.", "«beni … kıldı» — sükûn ile meczûm; yâ ilk mef'ûl.", segments=[seg("يَجْعَلْ", "jaala", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  maful_("جَبَّارًا", "jabbar", "«a tyrant»", "«zorba»", tags=[MX], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — صِيغَةُ مُبَالَغَةٍ."),
  naat("شَقِيًّا", "shaqi", "«wretched»", "«bedbaht»", case="nasb", punct=AYA),
  ]),
])
sen("s5", "«And peace be upon me the day I was born, the day I die and the day I am raised up alive.» (19:33)",
        "«Doğduğum gün, öleceğim gün ve diri olarak kaldırılacağım gün selâm benim üzerimedir.» (19:33)", [
  *quran([
  tok("وَالسَّلَامُ", "salam", "noun", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالسَّلَامُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and peace» — the mubtadaʾ.", "«ve selâm» — mübtedâ.", segments=wa_("السَّلَامُ", "salam", "noun")),
  prep_pron("عَلَيَّ", "ala", "يَّ", "pron-1s", "«upon me» — the khabar.", "«benim üzerime» — haber.", tags=[MK], extra_ar=" — خَبَرٌ؛ قُلِبَتْ أَلِفُ عَلَى يَاءً وَأُدْغِمَتْ"),
  zarf("يَوْمَ", "yawm", "«the day»", "«… günü»", kind="زَمَانٍ"),
  tok("وُلِدْتُ", "walada", "verb", [ID, NF, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ يَوْمَ.", "«I was born» — a passive; the clause is annexed to «the day».", "«doğduğum» — meçhul; cümle «gün»e muzâfun ileyh.", segments=[seg("وُلِدْ", "walada", "verb"), seg("تُ", "pron-1s", "pron")]),
  wa_yawma(),
  tok("أَمُوتُ", "mata-die", "verb", [ID, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ.", "«I die» — the clause annexed to «the day».", "«öleceğim» — «gün»e muzâfun ileyh cümle."),
  wa_yawma(),
  tok("أُبْعَثُ", "baatha", "verb", [ID, NF, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: أَنَا.", "«I am raised up» — a passive muḍāriʿ.", "«kaldırılacağım» — meçhul muzari."),
  hal("حَيًّا", "hayy", "«alive»", "«diri olarak»", punct=AYA),
  ]),
])

CAND = {
 "qaraa": G("qaraa", "قَرَأَ", "ق ر أ", "verb", "to read, to recite", "okumak", 1),
 "wasf": G("wasf", "وَصْف", "و ص ف", "noun", "a description", "vasıf, tasvir", 1, plural="أَوْصَاف"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "sira": G("sira", "سِيرَة", "س ي ر", "noun", "a way of life, conduct; a biography", "yaşayış, sîret", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "dawa": G("dawa", "دَعْوَة", "د ع و", "noun", "a call, an invitation; a mission", "davet, çağrı", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "qawl": G("qawl", "قَوْل", "ق و ل", "noun", "a saying, speech", "söz", 1, plural="أَقْوَال"),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant, a slave", "kul", 1, plural="عِبَاد"),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "aata-bring": G("aata-bring", "آتَى", "أ ت ي", "verb", "to give, to bring (two objects; Form IV, defective)", "vermek (iki mef'ûl; if'âl, nâkıs)", 1),
 "nun-wiqaya": G("nun-wiqaya", "نِ (نُونُ الْوِقَايَةِ)", None, "part", "the nūn of protection before the speaker's yāʾ", "mütekellim yâ'sından önceki vikâye nûnu", 2),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a book; the Book", "kitap", 1, plural="كُتُب"),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "jaala": G("jaala", "جَعَلَ", "ج ع ل", "verb", "to make, to set (two objects)", "kılmak, yapmak (iki mef'ûl)", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "mubarak": G("mubarak", "مُبَارَك", "ب ر ك", "noun", "blessed (a passive participle of Form III)", "mübarek (müfâale ism-i mef'ûlü)", 1),
 "ayna": G("ayna", "أَيْنَ", None, "pron", "where; wherever", "nerede; nereye", 1),
 "ma-zaida": G("ma-zaida", "مَا (الزَّائِدَة)", None, "part", "the extra mā (of emphasis)", "zâid mâ (te'kid)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "awsa": G("awsa", "أَوْصَى", "و ص ي", "verb", "to enjoin, to bequeath (Form IV, defective)", "vasiyet etmek, emretmek (if'âl, nâkıs)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "salat": G("salat", "صَلَاة", "ص ل و", "noun", "prayer", "namaz", 1, plural="صَلَوَات"),
 "zakat": G("zakat", "زَكَاة", "ز ك و", "noun", "zakāt, the alms-due", "zekât", 1),
 "ma-masdariyya": G("ma-masdariyya", "مَا (الْمَصْدَرِيَّة)", None, "part", "the maṣdarī mā (as long as)", "masdariyye mâ (… -dığı sürece)", 2),
 "dama": G("dama", "دَامَ", "د و م", "verb", "to last, to go on (hollow)", "sürmek, devam etmek (ecvef)", 2),
 "hayy": G("hayy", "حَيّ", "ح ي ي", "noun", "alive, living", "diri, hayy", 1),
 "barr": G("barr", "بَرّ", "ب ر ر", "noun", "dutiful, pious", "iyi, itaatkâr", 1),
 "walida-mother": G("walida-mother", "وَالِدَة", "و ل د", "noun", "a mother", "anne, vâlide", 1),
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "jabbar": G("jabbar", "جَبَّار", "ج ب ر", "noun", "a tyrant; the Compeller", "zorba, cebbâr", 1),
 "shaqi": G("shaqi", "شَقِيّ", "ش ق و", "noun", "wretched", "bedbaht, şakî", 1),
 "salam": G("salam", "سَلَام", "س ل م", "noun", "peace", "selâm, esenlik", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "walada": G("walada", "وَلَدَ", "و ل د", "verb", "to give birth; (passive) to be born (an assimilated verb)", "doğurmak; (meçhul) doğmak (misâl fiil)", 1),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die (hollow)", "ölmek (ecvef)", 1),
 "baatha": G("baatha", "بَعَثَ", "ب ع ث", "verb", "to send; to raise up", "göndermek; diriltmek", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch34 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 34 (print p. 49; ʿĪsā §13): his life and his call in the Qurʾān — Maryam 19:30 «I am the servant of God» (s2), 19:31 blessed wherever he is, prayer and zakāt as long as he lives (s3), 19:32 dutiful to his mother, no tyrant (s4), 19:33 peace on the three days (s5)."
ADD_TR = " Otuz dördüncü bölüm (baskı s. 49; Îsâ §13): Kur'ân'da sîreti ve daveti — Meryem 30 «ben Allah'ın kuluyum» (s2), 31 nerede olursa mübarek, yaşadıkça namaz ve zekât (s3), 32 anneye itaat, zorba değil (s4), 33 üç günde selâm (s5)."
write_out(34, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §13 + 19:30–33", GLOSS_ADD, notes=(), related=())
report(34, S, GLOSS_ADD, ())
