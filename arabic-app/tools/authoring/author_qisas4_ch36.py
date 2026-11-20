# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 36: «قِصَّةُ عِيسَى» §17 (his wandering and his call: patient in hardship, content with what keeps life going), §18 (the disciples ask for a table from heaven), §19 (bad manners: «can your Lord send down…?» — miracles are not conjuring tricks), §20 (he warns them of the evil end); print pp. 51–53.
python3 tools/authoring/author_qisas4_ch36.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: سِيَاحَتُهُ وَدَعْوَتُهُ، وَالْحَوَارِيُّونَ يَطْلُبُونَ مَائِدَةَ السَّمَاءِ", "en": "The story of ʿĪsā: his wandering and his call; the disciples ask for the table from heaven", "tr": "Îsâ'nın kıssası: seyahati ve daveti; havârîler gök sofrasını ister"}
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

# ---------------------------------------------------------------- §17 سِيَاحَتُهُ وَدَعْوَتُهُ (print pp. 51–52)
sen("s1", "And our master ʿĪsā used to spend most of his time in wandering and moving from place to place, calling the Children of Israel to God and guiding their lost sheep to their Lord and Master;",
        "Efendimiz Îsâ vaktinin çoğunu seyahatle, bir yerden bir yere göçmekle geçirir; İsrâiloğulları'nı Allah'a çağırır, kaybolmuş koyunlarını Rablerine ve Efendilerine iletirdi;", [
  tok("وَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and … was»", "«ve … idi»", segments=wa_("كَانَ", "kana", "verb")),
  noun_pron("سَيِّدُنَا", "sayyid", "سَيِّدُ", "نَا", "pron-1p", "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master» — kāna's ism.", "«efendimiz» — kâne'nin ismi.", tags=[KN, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — a badal.", "«Îsâ» — bedel."),
  mudari("يَقْضِي", "qada-judge", "«spend»", "«geçirir»", tags=[KN, "naqis-verbs"], extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ؛ وَالْجُمْلَةُ خَبَرُ كَانَ؛ قَضَى الْوَقْتَ: أَمْضَاهُ"),
  maful_("أَكْثَرَ", "akthar", "«most [of]»", "«çoğunu»", tags=[ID, "ism-tafdil"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ."),
  noun_pron("أَوْقَاتِهِ", "waqt", "أَوْقَاتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his time»", "«vaktinin»", tags=[ID, JT]),
  fi(),
  majrur("السِّيَاحَةِ", "siyaha", "«wandering»", "«seyahatle»", punct="،"),
  atf("وَالِانْتِقَالِ", "intiqal", "«moving»", "«ve göçmekle»", tags=["form-viii-verbs"]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("مَكَانٍ", "makan", "«a place»", "«bir yerden»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("مَكَانٍ", "makan", "«a place»", "«bir yere»", punct="،"),
  tok("يَدْعُو", "daa", "verb", [HL, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ حَالٌ.", "«calling» — a ḥāl clause.", "«çağırarak» — hâl cümlesi."),
  tok("بَنِي", "banu-israil", "noun", [MB, ID, JS], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«the Children [of]» — the object, naṣb by the yāʾ.", "«oğullarını» — mef'ûl, yâ ile mansub."),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Israel»", "«İsrâil»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God»", "«Allah'a»", punct="،"),
  mudari_wa("وَيَهْدِي", "hada", "«and guiding»", "«ve iletir»", tags=["naqis-verbs", HL], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ"),
  noun_pron("خِرَافَهُمُ", "kharuf", "خِرَافَ", "هُمُ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ، ضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — اسْتِعَارَةٌ مِنْ لُغَةِ الْإِنْجِيلِ.", "«their sheep» — the object; a metaphor in the Gospel's idiom.", "«koyunlarını» — mef'ûl; İncil üslûbundan istiâre.", tags=[MB, ID, JT]),
  naat("الضَّالَّةَ", "dall", "«lost»", "«kaybolmuş»", case="nasb", tags=["ism-fail", "doubled-verbs"]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  noun_pron("رَبِّهَا", "rabb", "رَبِّ", "هَا", "pron-3fs", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their Lord»", "«Rablerine»", tags=[HJ, ID]),
  pron_atf("وَسَيِّدِهَا", "sayyid", "سَيِّدِ", "هَا", "pron-3fs", "«their Master»", "«ve Efendilerine»", punct="،"),
])
sen("s2", "and in these rounds and journeys ease and hardship, straitness and plenty would come his way; he would bear that patiently and accept this gratefully, bear hunger, and content himself with what keeps the last breath going.",
        "bu gezilerde ve yolculuklarda kolaylık da zorluk da, darlık da bolluk da başına gelir; onu sabırla taşır, bunu şükürle kabul eder, açlığa sabreder ve can damarını ayakta tutan ile yetinirdi.", [
  mudari_wa("وَيَتَّفِقُ", "ittafaqa", "«and would come»", "«ve … gelir»", tags=["form-viii-verbs", HL], hidden="هُوَ", extra=" — وَفَاعِلُهُ الْيُسْرُ بَعْدَهُ؛ اتَّفَقَ لَهُ الْأَمْرُ: حَصَلَ"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«his way»", "«başına»"),
  fi(),
  tok("هٰذِهِ", "hadhihi", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«these»", "«bu»"),
  tok("الْجَوْلَاتِ", "jawla", "noun", [BD, JM], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«rounds» — a badal of the demonstrative.", "«gezilerde» — işaret isminden bedel."),
  atf("وَالرِّحْلَاتِ", "rihla", "«journeys»", "«ve yolculuklarda»", tags=[JM]),
  fail("الْيُسْرُ", "yusr", "«ease»", "«kolaylık»", extra_ar=" — فَاعِلُ يَتَّفِقُ"),
  atf("وَالْعُسْرُ", "usr", "«hardship»", "«ve zorluk»", "raf", punct="،"),
  atf("وَالضِّيقُ", "diq", "«straitness»", "«darlık»", "raf"),
  atf("وَالرَّخَاءُ", "rakha", "«plenty»", "«ve bolluk»", "raf", punct="،"),
  mudari_wa("وَيَتَحَمَّلُ", "tahammala", "«and he would bear»", "«ve taşır»", tags=["form-v-verbs"]),
  tok("ذٰلِكَ", "dhalika", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the object.", "«onu» — mef'ûl."),
  hal_pair("صَابِرًا", "sabir", "«patiently»", "«sabırla»", punct="،"),
  mudari_wa("وَيَقْبَلُ", "qabila", "«and accept»", "«ve kabul eder»"),
  tok("هٰذَا", "hadha", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this» — the object.", "«bunu» — mef'ûl."),
  hal_pair("شَاكِرًا", "shakir", "«gratefully»", "«şükürle»", punct="،"),
  mudari_wa("وَيَصْبِرُ", "sabara", "«and bear»", "«ve sabreder»"),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("الْجُوعِ", "ju", "«hunger»", "«açlığa»", punct="،"),
  mudari_wa("وَيَجْتَزِئُ", "ijtazaa", "«and content himself»", "«ve yetinir»", tags=["form-viii-verbs"], extra=" — مَهْمُوزُ اللَّامِ: اجْتَزَأَ بِالشَّيْءِ: اكْتَفَى بِهِ"),
  bi_ma(),
  mudari("يَسُدُّ", "sadda-block", "«keeps … going»", "«ayakta tutan»", tags=[MW, "doubled-verbs"], extra_ar=" — وَالْجُمْلَةُ صِلَةٌ؛ سَدَّ الرَّمَقَ: أَمْسَكَ بَقِيَّةَ الرُّوحِ"),
  maful_("الرَّمَقَ", "ramaq", "«the last breath»", "«can damarını»", punct="."),
])
# ---------------------------------------------------------------- §18 الْحَوَارِيُّونَ يَطْلُبُونَ مَائِدَةَ السَّمَاءِ (print p. 52)
sen("s3", "As for the disciples, they were not at his rank of patience, endurance, austerity and renunciation, and something of that befell them; so they asked our master ʿĪsā to ask God to send down to them a table from heaven, from which they would eat and be filled after hunger, and enjoy ease after toil.",
        "Havârîlere gelince, onlar sabırda, dayanıklılıkta, kanaatte ve zühdde onun derecesinde değillerdi; onlara bundan bir şey isabet etti; bunun üzerine efendimiz Îsâ'dan, Allah'tan kendilerine gökten bir sofra indirmesini istemesini dilediler ki ondan yiyip açlıktan sonra doysunlar, zahmetten sonra rahat etsinler.", [
  tok("أَمَّا", "amma", "part", ["amma-tafsiliyya", SH], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«-e gelince»"),
  tok("الْحَوَارِيُّونَ", "hawari", "noun", [MK, JS], "مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the disciples» — the mubtadaʾ.", "«havârîler» — mübtedâ."),
  tok("فَلَمْ", "lam", "part", [SH, LJ], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«… not» — the fāʾ of ammā's answer with lam.", "«… değil» — emmâ'nın cevap fâ'sı ile lem.", segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam", "part")]),
  tok("يَكُونُوا", "kana", "verb", [LJ, KN, AK, MK, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ اسْمُهُ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«they were» — jazm by dropping the nūn; the clause is the khabar.", "«idiler» — nûnun hazfi ile meczûm; cümle haber."),
  tok("بِمَنْزِلَتِهِ", "manzila", "noun", [HJ, ID, KN], "الْبَاءُ حَرْفُ جَرٍّ، وَمَنْزِلَتِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونُوا.", "«at his rank» — kāna's khabar.", "«onun derecesinde» — kâne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("مَنْزِلَتِ", "manzila", "noun"), seg("هِ", "pron-3ms", "pron")]),
  prep("مِنَ", "min", "«of»", "«-de»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الصَّبْرِ", "sabr", "«patience»", "«sabır»"),
  atf("وَالْجَلَدِ", "jalad", "«endurance»", "«dayanıklılık»"),
  atf("وَالتَّقَشُّفِ", "taqashshuf", "«austerity»", "«kanaat»", tags=["form-v-verbs"]),
  atf("وَالزَّهَادَةِ", "zahada", "«renunciation»", "«ve zühd»", punct="،"),
  v_pron("وَأَصَابَهُمْ", "asaba", "أَصَابَ", "هُمْ", "pron-3mp", "«and befell them»", "«ve onlara isabet etti»", tags=["hollow-verbs", "form-iv-verbs"], wa=True, hidden=None),
  fail("شَيْءٌ", "shay", "«something»", "«bir şey»"),
  prep("مِنْ", "min", "«of»", "«-den»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«bundan»", punct="،"),
  tok("فَطَلَبُوا", "talaba", "verb", [AT], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَطَلَبُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«so they asked»", "«bunun üzerine istediler»", segments=[seg("فَ", "fa", "conj"), seg("طَلَبُوا", "talaba", "verb")]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[HJ, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ'dan»"),
  an_nasb("مَفْعُولٌ بِهِ لِطَلَبُوا", "«to»", "«-mesini»"),
  mansub("يَسْأَلَ", "saala", "«ask»", "«istemesini»", tags=[MX]),
  tok("اللهَ", "allah", "propn", [MB, MX], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«God» — the first object.", "«Allah'tan» — ilk mef'ûl."),
  an_nasb("مَفْعُولٌ ثَانٍ لِيَسْأَلَ", "«to»", "«-mesini»"),
  mansub("يُنْزِلَ", "anzala", "«send down»", "«indirmesini»", tags=["form-iv-verbs"]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«kendilerine»"),
  maful_("مَائِدَةً", "maida", "«a table»", "«bir sofra»"),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("السَّمَاءِ", "sama", "«heaven»", "«gökten»"),
  khamsa("يَأْكُلُونَ", "akala", "«from which they would eat»", "«ki ondan yesinler»", tags=["jumla-sifa"], extra_ar=" — وَالْجُمْلَةُ نَعْتٌ لِمَائِدَةً"),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«from it»", "«ondan»"),
  khamsa_wa("وَيَشْبَعُونَ", "shabia", "«and be filled»", "«ve doysunlar»"),
  zarf("بَعْدَ", "bad-after", "«after»", "«-den sonra»", kind="زَمَانٍ"),
  mudaf_ilayh("جُوعٍ", "ju", "«hunger»", "«açlık»", punct="،"),
  khamsa_wa("وَيَنْعَمُونَ", "naima", "«and enjoy ease»", "«ve rahat etsinler»"),
  zarf("بَعْدَ", "bad-after", "«after»", "«-den sonra»", kind="زَمَانٍ"),
  mudaf_ilayh("عَنَاءٍ", "ana-toil", "«toil»", "«zahmet»", punct="."),
])
# ---------------------------------------------------------------- §19 سُوءُ أَدَبٍ (print pp. 52–53)
sen("s4", "And they were not well-mannered in their asking, for they said: «Can your Lord send down to us a table from heaven?»",
        "Soruşlarında edepli değillerdi; «Rabbin bize gökten bir sofra indirebilir mi?» dediler.", [
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … değil»", segments=wa_("لَمْ", "lam", "part")),
  tok("يَكُونُوا", "kana", "verb", [LJ, KN, AK, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِحَذْفِ النُّونِ، وَالْوَاوُ اسْمُهُ.", "«they were»", "«idiler»"),
  tok("مُتَأَدِّبِينَ", "mutaaddib", "noun", [KN, JS, "ism-fail", "form-v-verbs"], "خَبَرُ يَكُونُوا مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«well-mannered» — kāna's khabar.", "«edepli» — kâne'nin haberi."),
  fi(),
  noun_pron("سُؤَالِهِمْ", "sual", "سُؤَالِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their asking»", "«soruşlarında»", tags=[HJ, ID], punct="،"),
  tok("فَقَالُوا", "qala", "verb", [AT, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْسِيرِ)، وَقَالُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ.", "«for they said»", "«dediler»", segments=[seg("فَ", "fa", "conj"), seg("قَالُوا", "qala", "verb")], punct=":"),
  tok("هَلْ", "hal-istifham", "part", [IS, IQ], "حَرْفُ اسْتِفْهَامٍ — مَقُولُ الْقَوْلِ، كَمَا فِي الْآيَةِ (5:112).", "«can» — the interrogative particle; the saying as in 5:112.", "«… mi» — istifhâm harfi; 5:112'deki söz."),
  mudari("يَسْتَطِيعُ", "istataa", "«is able»", "«gücü yeter»", tags=["hollow-verbs", "form-x-verbs"], hidden=None),
  noun_pron("رَبُّكَ", "rabb", "رَبُّ", "كَ", "pron-2ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord» — the doer.", "«Rabbin» — fâil.", tags=[FL, ID]),
  an_nasb("مَفْعُولٌ بِهِ لِيَسْتَطِيعُ", "«to»", "«-mesine»"),
  mansub("يُنَزِّلَ", "nazzala", "«send down»", "«indirmeye»", tags=["form-ii-verbs"]),
  prep_pron("عَلَيْنَا", "ala", "نَا", "pron-1p", "«to us»", "«bize»"),
  maful_("مَائِدَةً", "maida", "«a table»", "«bir sofra»"),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("السَّمَاءِ", "sama", "«heaven»", "«gökten»", punct="."),
])
sen("s5", "Their question did not please ʿĪsā, and he disliked the manner in which they addressed him.",
        "Soruları Îsâ'nın hoşuna gitmedi; kendisine hitap ettikleri üslûbu beğenmedi.", [
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not»", "«ve … -medi»", segments=wa_("لَمْ", "lam", "part")),
  tok("يُعْجِبْ", "ajaba-please", "verb", [LJ, "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ.", "«please» — jazm by sukūn.", "«hoşuna gitmedi» — sükûn ile meczûm."),
  tok("عِيسَى", "isa", "propn", [MB, MM, "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — the object, before the doer.", "«Îsâ'nın» — fâilden önce gelen mef'ûl."),
  noun_pron("سُؤَالُهُمْ", "sual", "سُؤَالُ", "هُمْ", "pron-3mp", "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their question» — the delayed doer.", "«soruları» — sonraya kalan fâil.", tags=[FL, ID], punct="،"),
  mazi("وَكَرِهَ", "kariha", "«and he disliked»", "«ve beğenmedi»", tags=[AT], wa=True, hidden="هُوَ"),
  maful_("الْأُسْلُوبَ", "uslub", "«the manner»", "«üslûbu»"),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ.", "«in which» — the relative, a naʿt.", "«ki» — sıfat olan mevsûl."),
  mazi_pl("خَاطَبُوا", "khataba", "«they addressed»", "«hitap ettiler»", tags=[MW, "form-iii-verbs"]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with it»", "«onunla»", punct="."),
])
sen("s6", "And all the prophets demand of their nations belief in the unseen and lay it upon them; miracles are not conjuring tricks with which children are amused and simpletons diverted; they are only signs from God which He makes appear at the hands of His prophets when He wills, by which God's proof against His servants is established, so that they are given no respite once they have appeared and been denied.",
        "Peygamberlerin hepsi ümmetlerinden gayba imanı ister ve onu üzerlerine yükler; mucizeler çocukların oyalandığı, saf kimselerin eğlendirildiği hokkabazlıklar değildir; onlar ancak Allah'ın dilediğinde peygamberlerinin eliyle gösterdiği âyetlerdir; onlarla Allah'ın kullara karşı hücceti ayakta durur; ortaya çıkıp inkâr edildikten sonra artık mühlet verilmez.", [
  tok("وَالْأَنْبِيَاءُ", "nabi", "noun", [AT, MK, JT], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْأَنْبِيَاءُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the prophets» — the mubtadaʾ.", "«ve peygamberler» — mübtedâ.", segments=wa_("الْأَنْبِيَاءُ", "nabi", "noun")),
  tok("جَمِيعًا", "jami", "noun", [HL, "tawkid"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ (بِمَعْنَى التَّوْكِيدِ: كُلُّهُمْ).", "«all» — a ḥāl with the force of emphasis.", "«hepsi» — te'kid mânalı hâl."),
  khamsa("يُطَالِبُونَ", "talaba-demand", "«demand»", "«ister»", tags=[MK, "form-iii-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ"),
  noun_pron("أُمَمَهُمْ", "umma", "أُمَمَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«their nations» — the object.", "«ümmetlerinden» — mef'ûl.", tags=[MB, ID, JT]),
  bi_noun("بِالْإِيمَانِ", "iman", "«belief»", "«imanı»"),
  bi_noun("بِالْغَيْبِ", "ghayb", "«in the unseen»", "«gayba»", punct="،"),
  tok("وَيُكَلِّفُونَهَا", "kallafa", "verb", [AT, AK, MX, "mudari-marfu", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُكَلِّفُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ أَوَّلُ.", "«and lay upon them» — two objects; hā is the first.", "«ve onlara yükler» — iki mef'ûl; hâ ilki.", segments=[seg("وَ", "wa", "conj"), seg("يُكَلِّفُونَ", "kallafa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("إِيَّاهُ", "iyya", "pron", [MX, MB], "ضَمِيرُ نَصْبٍ مُنْفَصِلٌ مَفْعُولٌ بِهِ ثَانٍ — فُصِلَ لِاجْتِمَاعِ ضَمِيرَيْنِ.", "«it» — the detached object pronoun as second object: two pronouns cannot both attach.", "«onu» — ikinci mef'ûl olan munfasıl nasb zamiri; iki zamir bitişemez.", punct="،"),
  tok("وَلَيْسَتِ", "laysa", "verb", [AT, KN], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَتْ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and … are not» — laysa with the feminine tāʾ.", "«ve … değildir» — leyse, te'nis tâ'sı ile.", segments=wa_("لَيْسَتِ", "laysa", "verb")),
  tok("الْمُعْجِزَاتُ", "mujiza", "noun", [KN, JM], "اسْمُ لَيْسَ مَرْفُوعٌ بِالضَّمَّةِ.", "«miracles» — laysa's ism.", "«mucizeler» — leyse'nin ismi."),
  tok("مَخَارِيقَ", "makhariq", "noun", [KN, JT, MM], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ مَمْنُوعَةٌ مِنَ الصَّرْفِ.", "«conjuring tricks» — laysa's khabar; a muntahā plural, diptote.", "«hokkabazlıklar» — leyse'nin haberi; müntehe'l-cumû', gayr-i munsarıf."),
  tok("يُسَلَّى", "salla-amuse", "verb", [NF, "jumla-sifa", "mudari-marfu", "naqis-verbs", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَالْجُمْلَةُ نَعْتٌ لِمَخَارِيقَ.", "«are amused» — a passive; the clause describes the tricks.", "«oyalanır» — meçhul; cümle sıfat."),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«with which»", "«onlarla»"),
  tok("الْأَطْفَالُ", "tifl", "noun", [NF, JT], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«children» — the deputy doer.", "«çocuklar» — nâib-i fâil.", punct="،"),
  tok("وَيُلْهَى", "alha", "verb", [AT, NF, "mudari-marfu", "naqis-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُلْهَى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and are diverted» — a passive.", "«ve eğlendirilir» — meçhul.", segments=wa_("يُلْهَى", "alha", "verb")),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«with which»", "«onlarla»"),
  tok("الْأَغْمَارُ", "ghumr", "noun", [NF, JT], "نَائِبُ فَاعِلٍ مَرْفُوعٌ — جَمْعُ غُمْرٍ: الَّذِي لَمْ يُجَرِّبِ الْأُمُورَ.", "«simpletons» — the deputy doer; ghumr: one untried by affairs.", "«saf kimseler» — nâib-i fâil; gumr: işleri denememiş kişi.", punct="،"),
  tok("وَإِنَّمَا", "innama", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَإِنَّمَا أَدَاةُ حَصْرٍ (كَافَّةٌ وَمَكْفُوفَةٌ).", "«they are only» — innamā restricts.", "«onlar ancak» — innemâ hasr edatı.", segments=wa_("إِنَّمَا", "innama", "part")),
  tok("هِيَ", "hiya", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«they» — the mubtadaʾ.", "«onlar» — mübtedâ."),
  tok("آيَاتٌ", "aya", "noun", [MK, JM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«signs» — the khabar.", "«âyetler» — haber."),
  prep("مِنَ", "min", "«from»", "«-den»", ar="حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — صِفَةٌ لِآيَاتٌ."),
  tok("اللهِ", "allah", "propn", [HJ, NA], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«God»", "«Allah'tan»"),
  v_pron("يُظْهِرُهَا", "azhara", "يُظْهِرُ", "هَا", "pron-3fs", "«which He makes appear»", "«gösterdiği»", tags=["jumla-sifa", "mudari-marfu", "form-iv-verbs"]),
  prep("عَلَى", "ala", "«at»", "«-de»"),
  majrur("أَيْدِي", "yad", "«the hands [of]»", "«elleri»", tags=[ID, JT, "ism-maqsur-manqus"], ar="مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، مُضَافٌ — أَيْدٍ مَنْقُوصٌ ظَهَرَتْ يَاؤُهُ بِالْإِضَافَةِ."),
  noun_pron("أَنْبِيَائِهِ", "nabi", "أَنْبِيَائِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His prophets»", "«peygamberlerinin»", tags=[ID, JT]),
  tok("حِينَ", "hina", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when» — a time ẓarf annexed to the clause.", "«-dığında» — cümleye muzâf zaman zarfı."),
  yasha(punct="،"),
  mudari_wa("وَتَقُومُ", "qama", "«and stands»", "«ve ayakta durur»", tags=["hollow-verbs"], hidden=None, extra=" — وَفَاعِلُهُ حُجَّةُ بَعْدَهُ"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«by them»", "«onlarla»"),
  fail("حُجَّةُ", "hujja", "«the proof [of]»", "«hücceti»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  prep("عَلَى", "ala", "«against»", "«-e karşı»"),
  majrur("الْعِبَادِ", "ibad", "«the servants»", "«kullara»", tags=[JT], punct="؛"),
  tok("فَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ.", "«so … not»", "«artık … -mez»", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("يُمْهَلُونَ", "amhala", "verb", [NF, AK, "la-nafiya", "mudari-marfu", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ نَائِبُ فَاعِلٍ.", "«are they given respite» — a passive of the five verbs; the wāw is the deputy doer.", "«mühlet verilir» — ef'âl-i hamseden meçhul; vâv nâib-i fâil."),
  zarf("بَعْدَ", "bad-after", "«after»", "«-den sonra»", kind="زَمَانٍ"),
  noun_pron("ظُهُورِهَا", "zuhur", "ظُهُورِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their appearing»", "«ortaya çıkmalarından»", tags=[ID]),
  pron_atf("وَإِنْكَارِهَا", "inkar", "إِنْكَارِ", "هَا", "pron-3fs", "«their denial»", "«ve inkâr edilmelerinden»", punct="."),
])
# ---------------------------------------------------------------- §20 تَحْذِيرُ قَوْمِهِ مِنْ سُوءِ الْعَاقِبَةِ (print p. 53)
sen("s7", "For that reason our master ʿĪsā feared for them, warned them of the evil end, and forbade them to put God Most High to the test; for He is higher and more majestic than that.",
        "Bu yüzden efendimiz Îsâ onlar için korktu; onları kötü sondan sakındırdı ve Allah Teâlâ'yı imtihan etmekten nehyetti; çünkü O bundan daha yüce ve daha uludur.", [
  tok("لِذٰلِكَ", "dhalika", "pron", [HJ, TA, "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِخَافَ.", "«for that reason» — the lām of cause with the demonstrative.", "«bu yüzden» — ta'lil lâmı ile işaret ismi.", segments=[seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  mazi("خَافَ", "khafa", "«feared»", "«korktu»", tags=["hollow-verbs"], hidden=None),
  noun_pron("سَيِّدُنَا", "sayyid", "سَيِّدُ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master» — the doer.", "«efendimiz» — fâil.", tags=[FL, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ»"),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«for them»", "«onlar için»", punct="،"),
  v_pron("وَحَذَّرَهُمْ", "hadhdhara", "حَذَّرَ", "هُمْ", "pron-3mp", "«and warned them»", "«ve onları sakındırdı»", tags=["form-ii-verbs"], wa=True),
  prep("مِنْ", "min", "«of»", "«-den»"),
  majrur("سُوءِ", "su", "«the evil [of]»", "«kötü»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْعَاقِبَةِ", "aqiba", "«the end»", "«sondan»", punct="،"),
  tok("وَنَهَاهُمْ", "naha", "verb", [AT, MB, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَنَهَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", "«and forbade them» — a defective māḍī.", "«ve onları nehyetti» — nâkıs mâzî.", segments=[seg("وَ", "wa", "conj"), seg("نَهَا", "naha", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("عَنِ", "an", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  majrur("امْتِحَانِ", "imtihan", "«testing»", "«imtihan etmekten»", tags=[ID, "form-viii-verbs"], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct="؛"),
  tok("فَهُوَ", "huwa", "pron", [AT, MK], "الْفَاءُ لِلتَّعْلِيلِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«for He» — the mubtadaʾ.", "«çünkü O» — mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("أَعْلَى", "ala-highest", "noun", [MK, "ism-tafdil", "ism-maqsur-manqus", MM], "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — اسْمُ تَفْضِيلٍ.", "«higher» — the khabar; an elative.", "«daha yüce» — haber; ism-i tafdîl."),
  tok("وَأَجَلُّ", "ajall", "noun", [AT, MK, "ism-tafdil", MM, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَجَلُّ مَعْطُوفٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ مِنَ الْمُضَاعَفِ: أَجْلَلُ أُدْغِمَ.", "«and more majestic» — an elative from a doubled root, assimilated.", "«ve daha ulu» — muzâaf kökten ism-i tafdîl, idgamlı.", segments=wa_("أَجَلُّ", "ajall", "noun")),
  prep("مِنْ", "min", "«than»", "«-den»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«bundan»", punct="."),
])

CAND = {
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "qada-judge": G("qada-judge", "قَضَى", "ق ض ي", "verb", "to decree, to judge; (the time) to spend (defective)", "hükmetmek; (vakti) geçirmek (nâkıs)", 1),
 "akthar": G("akthar", "أَكْثَر", "ك ث ر", "noun", "more, most (an elative)", "daha çok (ism-i tafdîl)", 1),
 "waqt": G("waqt", "وَقْت", "و ق ت", "noun", "time", "vakit", 1, plural="أَوْقَات"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "siyaha": G("siyaha", "سِيَاحَة", "س ي ح", "noun", "wandering, travelling", "seyahat, dolaşma", 2),
 "intiqal": G("intiqal", "اِنْتِقَال", "ن ق ل", "noun", "moving, transfer (the maṣdar of Form VIII)", "göç, intikal (iftiâl masdarı)", 2),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "makan": G("makan", "مَكَان", "ك و ن", "noun", "a place", "yer, mekân", 1, plural="أَمْكِنَة"),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call, to summon; to pray", "çağırmak; dua etmek", 1),
 "banu-israil": G("banu-israil", "بَنُو إِسْرَائِيلَ", "ب ن ي", "noun", "the Children of Israel", "İsrâiloğulları", 1),
 "israil": G("israil", "إِسْرَائِيل", None, "propn", "Israel (Yaʿqūb)", "İsrâil (Yâkub)", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "hada": G("hada", "هَدَى", "ه د ي", "verb", "to guide (defective)", "hidâyet etmek, iletmek (nâkıs)", 1),
 "kharuf": G("kharuf", "خَرُوف", "خ ر ف", "noun", "a sheep, a lamb", "koyun, kuzu", 1, plural="خِرَاف"),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "dall": G("dall", "ضَالّ", "ض ل ل", "noun", "lost, astray (an active participle of a doubled root)", "kaybolmuş, sapmış (muzâaf kökün ism-i fâili)", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "ittafaqa": G("ittafaqa", "اِتَّفَقَ", "و ف ق", "verb", "to happen (li: to someone); to agree (Form VIII)", "(li ile) başına gelmek; anlaşmak (iftiâl)", 2),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu (müennes)", 1),
 "jawla": G("jawla", "جَوْلَة", "ج و ل", "noun", "a round, a tour", "gezi, tur", 2, plural="جَوْلَات"),
 "rihla": G("rihla", "رِحْلَة", "ر ح ل", "noun", "a journey", "yolculuk", 1, plural="رِحْلَات"),
 "yusr": G("yusr", "يُسْر", "ي س ر", "noun", "ease", "kolaylık", 1),
 "usr": G("usr", "عُسْر", "ع س ر", "noun", "hardship", "zorluk, güçlük", 1),
 "diq": G("diq", "ضِيق", "ض ي ق", "noun", "straitness, narrowness", "darlık, sıkıntı", 2),
 "rakha": G("rakha", "رَخَاء", "ر خ و", "noun", "plenty, ease of life", "bolluk, refah", 2),
 "tahammala": G("tahammala", "تَحَمَّلَ", "ح م ل", "verb", "to bear, to endure (Form V)", "taşımak, katlanmak (tefa''ul)", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "sabir": G("sabir", "صَابِر", "ص ب ر", "noun", "patient (an active participle)", "sabırlı, sabreden (ism-i fâil)", 1, plural="صَابِرُونَ"),
 "qabila": G("qabila", "قَبِلَ", "ق ب ل", "verb", "to accept", "kabul etmek", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "shakir": G("shakir", "شَاكِر", "ش ك ر", "noun", "grateful (an active participle)", "şükreden (ism-i fâil)", 1),
 "sabara": G("sabara", "صَبَرَ", "ص ب ر", "verb", "to be patient (ʿalā: with)", "sabretmek", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "ju": G("ju", "جُوع", "ج و ع", "noun", "hunger", "açlık", 1),
 "ijtazaa": G("ijtazaa", "اِجْتَزَأَ", "ج ز أ", "verb", "to content oneself (bi: with) (Form VIII, hamza-final)", "yetinmek (iftiâl, mehmûzü'l-lâm)", 3),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "ma-mawsula": G("ma-mawsula", "مَا (الْمَوْصُولَة)", None, "pron", "what, that which", "… şey, -dığı", 1),
 "sadda-block": G("sadda-block", "سَدَّ", "س د د", "verb", "to block, to close up; (al-ramaq) to keep life going (doubled)", "kapatmak; (remak) hayatta tutmak (muzâaf)", 1),
 "ramaq": G("ramaq", "رَمَق", "ر م ق", "noun", "the last breath of life", "son nefes, can", 3),
 "amma": G("amma", "أَمَّا", None, "part", "as for", "-e gelince", 1),
 "hawari": G("hawari", "حَوَارِيّ", "ح و ر", "noun", "a disciple (of ʿĪsā)", "havârî", 2, plural="حَوَارِيُّونَ"),
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "manzila": G("manzila", "مَنْزِلَة", "ن ز ل", "noun", "a rank, a station", "mertebe, derece", 1),
 "sabr": G("sabr", "صَبْر", "ص ب ر", "noun", "patience", "sabır", 1),
 "jalad": G("jalad", "جَلَد", "ج ل د", "noun", "endurance, fortitude", "dayanıklılık, metanet", 3),
 "taqashshuf": G("taqashshuf", "تَقَشُّف", "ق ش ف", "noun", "austerity (the maṣdar of Form V)", "kanaat, zühd hayatı (tefa''ul masdarı)", 3),
 "zahada": G("zahada", "زَهَادَة", "ز ه د", "noun", "renunciation, asceticism", "zühd", 2),
 "asaba": G("asaba", "أَصَابَ", "ص و ب", "verb", "to befall; to hit (Form IV, hollow)", "isabet etmek, başına gelmek (if'âl, ecvef)", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "talaba": G("talaba", "طَلَبَ", "ط ل ب", "verb", "to ask for, to seek", "istemek, talep etmek", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "saala": G("saala", "سَأَلَ", "س أ ل", "verb", "to ask (two objects)", "sormak, istemek (iki mef'ûl)", 1),
 "anzala": G("anzala", "أَنْزَلَ", "ن ز ل", "verb", "to send down (Form IV)", "indirmek (if'âl)", 1),
 "maida": G("maida", "مَائِدَة", "م ي د", "noun", "a table (spread with food)", "sofra", 1, plural="مَوَائِد"),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "a heaven, the sky", "gök", 1, plural="سَمَاوَات"),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "shabia": G("shabia", "شَبِعَ", "ش ب ع", "verb", "to be filled, to be sated", "doymak", 1),
 "bad-after": G("bad-after", "بَعْدَ", "ب ع د", "noun", "after", "-den sonra", 1),
 "naima": G("naima", "نَعِمَ", "ن ع م", "verb", "to live in ease, to enjoy (bi)", "nimet içinde olmak, rahat etmek", 2),
 "ana-toil": G("ana-toil", "عَنَاء", "ع ن ي", "noun", "toil, trouble", "zahmet, meşakkat", 2),
 "mutaaddib": G("mutaaddib", "مُتَأَدِّب", "أ د ب", "noun", "well-mannered (an active participle of Form V)", "edepli (tefa''ul ism-i fâili)", 2),
 "sual": G("sual", "سُؤَال", "س أ ل", "noun", "a question, a request", "soru, istek", 1, plural="أَسْئِلَة"),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "hal-istifham": G("hal-istifham", "هَلْ", None, "part", "is it that…? (the interrogative particle)", "… mi? (istifhâm harfi)", 1),
 "istataa": G("istataa", "اِسْتَطَاعَ", "ط و ع", "verb", "to be able (Form X, hollow)", "güç yetirmek, yapabilmek (istif'âl, ecvef)", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "nazzala": G("nazzala", "نَزَّلَ", "ن ز ل", "verb", "to send down (Form II)", "indirmek (tef'îl)", 1),
 "ajaba-please": G("ajaba-please", "أَعْجَبَ", "ع ج ب", "verb", "to please (Form IV)", "hoşuna gitmek, beğendirmek (if'âl)", 1),
 "kariha": G("kariha", "كَرِهَ", "ك ر ه", "verb", "to dislike, to hate", "hoşlanmamak, kerih görmek", 1),
 "uslub": G("uslub", "أُسْلُوب", "س ل ب", "noun", "a manner, a style", "üslûp", 1, plural="أَسَالِيب"),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which (m.)", "ki o, -an", 1),
 "khataba": G("khataba", "خَاطَبَ", "خ ط ب", "verb", "to address (Form III)", "hitap etmek (müfâale)", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "jami": G("jami", "جَمِيع", "ج م ع", "noun", "all, the whole", "hep, bütün", 1),
 "talaba-demand": G("talaba-demand", "طَالَبَ", "ط ل ب", "verb", "to demand (bi: something) of (Form III)", "talep etmek, istemek (müfâale)", 2),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "a nation, a community", "ümmet", 1, plural="أُمَم"),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith, belief", "iman", 1),
 "ghayb": G("ghayb", "غَيْب", "غ ي ب", "noun", "the unseen", "gayb", 1),
 "kallafa": G("kallafa", "كَلَّفَ", "ك ل ف", "verb", "to charge, to lay upon (two objects) (Form II)", "yükümlü kılmak (iki mef'ûl) (tef'îl)", 1),
 "iyya": G("iyya", "إِيَّا", None, "pron", "the detached object pronoun base", "munfasıl nasb zamirinin gövdesi", 2),
 "laysa": G("laysa", "لَيْسَ", "ل ي س", "verb", "is not (a frozen verb)", "değildir (câmid fiil)", 1),
 "mujiza": G("mujiza", "مُعْجِزَة", "ع ج ز", "noun", "a miracle", "mucize", 1, plural="مُعْجِزَات"),
 "makhariq": G("makhariq", "مَخَارِيق", "خ ر ق", "noun", "conjuring tricks, sleights (a plural)", "hokkabazlıklar, göz boyamalar (çoğul)", 3),
 "salla-amuse": G("salla-amuse", "سَلَّى", "س ل و", "verb", "to amuse, to console (Form II, defective)", "oyalamak, teselli etmek (tef'îl, nâkıs)", 2),
 "tifl": G("tifl", "طِفْل", "ط ف ل", "noun", "a child", "çocuk", 1, plural="أَطْفَال"),
 "alha": G("alha", "أَلْهَى", "ل ه و", "verb", "to divert, to distract (Form IV, defective)", "oyalamak, eğlendirip meşgul etmek (if'âl, nâkıs)", 2),
 "ghumr": G("ghumr", "غُمْر", "غ م ر", "noun", "a simpleton, one untried by affairs", "saf, tecrübesiz kimse", 3, plural="أَغْمَار"),
 "innama": G("innama", "إِنَّمَا", None, "part", "only (inna + the restraining mā)", "ancak, yalnızca (inne + kâffe mâ)", 1),
 "hiya": G("hiya", "هِيَ", None, "pron", "she / it (f.)", "o (müennes)", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "azhara": G("azhara", "أَظْهَرَ", "ظ ه ر", "verb", "to make appear, to show (Form IV)", "göstermek, ortaya çıkarmak (if'âl)", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1, plural="أَيْدٍ"),
 "hina": G("hina", "حِينَ", "ح ي ن", "noun", "when, at the time of", "-dığı zaman, … vakti", 1),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will (hollow)", "dilemek (ecvef)", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to rise, to stand (hollow)", "kalkmak, ayağa kalkmak (ecvef)", 1),
 "hujja": G("hujja", "حُجَّة", "ح ج ج", "noun", "a proof, an argument", "hüccet, delil", 1, plural="حُجَج"),
 "ibad": G("ibad", "عِبَاد", "ع ب د", "noun", "servants (of God)", "kullar", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "amhala": G("amhala", "أَمْهَلَ", "م ه ل", "verb", "to give respite (Form IV)", "mühlet vermek (if'âl)", 2),
 "zuhur": G("zuhur", "ظُهُور", "ظ ه ر", "noun", "appearing, emergence", "ortaya çıkma, zuhur", 1),
 "inkar": G("inkar", "إِنْكَار", "ن ك ر", "noun", "denial", "inkâr", 1),
 "khafa": G("khafa", "خَافَ", "خ و ف", "verb", "to fear (hollow)", "korkmak (ecvef)", 1),
 "hadhdhara": G("hadhdhara", "حَذَّرَ", "ح ذ ر", "verb", "to warn (min: of) (Form II)", "sakındırmak, uyarmak (tef'îl)", 1),
 "su": G("su", "سُوء", "س و أ", "noun", "evil, badness", "kötülük", 1),
 "aqiba": G("aqiba", "عَاقِبَة", "ع ق ب", "noun", "the end, the outcome", "âkıbet, son", 1, plural="عَوَاقِب"),
 "naha": G("naha", "نَهَى", "ن ه ي", "verb", "to forbid (ʿan: from) (defective)", "nehyetmek, yasaklamak (nâkıs)", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "imtihan": G("imtihan", "اِمْتِحَان", "م ح ن", "noun", "a test, a trial (the maṣdar of Form VIII)", "imtihan, sınama (iftiâl masdarı)", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he / it", "o", 1),
 "ala-highest": G("ala-highest", "أَعْلَى", "ع ل و", "noun", "higher, highest (an elative)", "daha yüce, en yüce (ism-i tafdîl)", 1),
 "ajall": G("ajall", "أَجَلّ", "ج ل ل", "noun", "more majestic (an elative of a doubled root)", "daha ulu (muzâaf kökten ism-i tafdîl)", 3),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tahammala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَمَّل", "تَحَمَّل", "تَحَمَّل", "تَحَمُّل", "مُتَحَمِّل", "مُتَحَمَّل", "تُحُمِّلَ", "يُتَحَمَّلُ", "تَحَمَّلَ الْأَذَى: صَبَرَ عَلَيْهِ وَاحْتَمَلَهُ."))
put_morph(mo, "ijtazaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِجْتَزَأ", "جْتَزِئ", "اِجْتَزِئ", "اِجْتِزَاء", "مُجْتَزِئ", None, None, None, "اِجْتَزَأَ بِالشَّيْءِ: اكْتَفَى بِهِ — مَهْمُوزُ اللَّامِ."))
put_morph(mo, "shabia", _sg.sound1("samia", "شَبِع", "شْبَع", "اِشْبَع", "شِبَع / شَبْع", "شَبْعَان / شَابِع", None, None, None, "شَبِعَ يَشْبَعُ: امْتَلَأَ مِنَ الطَّعَامِ — صِفَتُهُ شَبْعَانُ عَلَى فَعْلَانَ."))
put_morph(mo, "naima", _sg.sound1("samia", "نَعِم", "نْعَم", "اِنْعَم", "نَعْمَة / نَعِيم", "نَاعِم", None, None, None, "نَعِمَ يَنْعَمُ: طَابَ عَيْشُهُ وَتَرَفَّهَ؛ وَنَعِمَ بِالشَّيْءِ: تَمَتَّعَ بِهِ."))
put_morph(mo, "nazzala", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَزَّل", "نَزِّل", "نَزِّل", "تَنْزِيل", "مُنَزِّل", "مُنَزَّل", "نُزِّلَ", "يُنَزَّلُ", "نَزَّلَ الشَّيْءَ: أَنْزَلَهُ شَيْئًا بَعْدَ شَيْءٍ."))
put_morph(mo, "ajaba-please", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْجَب", "عْجِب", "أَعْجِب", "إِعْجَاب", "مُعْجِب", "مُعْجَب", "أُعْجِبَ", "يُعْجَبُ", "أَعْجَبَهُ الشَّيْءُ: رَاقَهُ وَحَسُنَ عِنْدَهُ."))
put_morph(mo, "talaba-demand", _sg.derived(_sg.B3, _sg.W3, "ُ", "طَالَب", "طَالِب", "طَالِب", "مُطَالَبَة", "مُطَالِب", "مُطَالَب", "طُولِبَ", "يُطَالَبُ", "طَالَبَهُ بِالشَّيْءِ: طَلَبَهُ مِنْهُ بِإِلْحَاحٍ."))
put_morph(mo, "salla-amuse", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "سَلَّ", "سَلّ", "i", "سَلّ", "تَسْلِيَة", "مُسَلٍّ (الْمُسَلِّي)", "مُسَلًّى", "سُلِّيَ", "يُسَلَّى", "سَلَّاهُ: جَعَلَهُ يَسْلُو وَيَنْسَى هَمَّهُ؛ وَسَلَّى الطِّفْلَ: لَهَّاهُ — نَاقِصٌ: يُسَلِّي، لَمْ يُسَلِّ."))
put_morph(mo, "alha", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَلْهَ", "لْه", "i", "أَلْه", "إِلْهَاء", "مُلْهٍ (الْمُلْهِي)", "مُلْهًى", "أُلْهِيَ", "يُلْهَى", "أَلْهَاهُ الشَّيْءُ: شَغَلَهُ وَصَرَفَهُ — نَاقِصٌ: يُلْهِي، لَمْ يُلْهِ."))
put_morph(mo, "amhala", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَمْهَل", "مْهِل", "أَمْهِل", "إِمْهَال", "مُمْهِل", "مُمْهَل", "أُمْهِلَ", "يُمْهَلُ", "أَمْهَلَهُ: أَخَّرَهُ وَأَنْظَرَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch36 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 36 (print pp. 51–53; ʿĪsā §17–20): his wandering and call — patient in hardship, content with what keeps the last breath going (s1–s2); the disciples ask for a table from heaven (s3); their ill-mannered «can your Lord…?» — miracles are not conjuring tricks but God's proof (s4–s6); he warns them of the evil end and of testing God (s7)."
ADD_TR = " Otuz altıncı bölüm (baskı s. 51–53; Îsâ §17–20): seyahati ve daveti — zorlukta sabır, can damarını tutan ile yetinme (s1–s2); havârîler gökten sofra ister (s3); edepsiz «Rabbin … -ebilir mi?» — mucizeler hokkabazlık değil, Allah'ın hüccetidir (s4–s6); kötü sondan ve Allah'ı imtihandan sakındırma (s7)."
write_out(36, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §17–20", GLOSS_ADD, notes=(), related=())
report(36, S, GLOSS_ADD, ())
