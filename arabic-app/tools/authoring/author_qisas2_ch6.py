# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 6: «سَفِينَةُ نُوحٍ» §11 نُوحٌ الرَّسُول (God chooses Nūḥ, not the rich and the chiefs; his character; the revelation «warn your people» — 71:1; «I am to you a trustworthy messenger» — 26:107) and §12 مَاذَا أَجَابَهُ الْقَوْمُ؟ (when did this one become a prophet? his friends, the rich and the proud, the ignorant — 23:24; «he wants the chieftainship»). Print pp. 17–19.
python3 tools/authoring/author_qisas2_ch6.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: نُوحٌ الرَّسُولُ — مَاذَا أَجَابَهُ الْقَوْمُ؟", "en": "The ship of Nūḥ: Nūḥ the messenger — what did the people answer him?", "tr": "Nûh'un gemisi: elçi Nûh — kavmi ona ne cevap verdi?"}
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

# ---------------------------------------------------------------- § chapter 6's own small helpers
def nuh_maful(punct=None, extra=""):
    return tok("نُوحًا", "nuh", "propn", [MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ (ثُلَاثِيٌّ سَاكِنُ الْوَسَطِ)" + extra + ".", "«Nūḥ» — the object; the name takes tanwīn (three letters, the middle one still).", "«Nûh» — mef'ûl; üç harfli, ortası sâkin olduğu için tenvinli.", punct=punct)
def nuh_fail(full="نُوحٌ", punct=None): return tok(full, "nuh", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the doer.", "«Nûh» — fâil.", punct=punct)
def nuh_ism_kana(punct=None): return tok("نُوحٌ", "nuh", "propn", [KN], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«Nūḥ» — kāna's ism.", "«Nûh» — kâne'nin ismi.", punct=punct)
def li_risala(punct=None): return noun_pron("لِرِسَالَتِهِ", "risala", "رِسَالَتِ", "هِ", "pron-3ms", "اللَّامُ حَرْفُ جَرٍّ، وَرِسَالَةِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«for His message» — li + the annexed noun.", "«risâleti için» — li + muzâf isim.", tags=[HJ, ID], punct=punct)
def li_risala_segs(punct=None):
    t = li_risala(punct); t["segments"] = [seg("لِ", "li", "prep"), seg("رِسَالَتِ", "risala", "noun"), seg("هِ", "pron-3ms", "pron")]; return t
def kana_khabar_naat(kh, kh_lex, kh_en, kh_tr, na, na_lex, na_en, na_tr, punct=None, kh_tags=(), na_tags=()):
    return [khabar_kana(kh, kh_lex, kh_en, kh_tr, tags=list(kh_tags)), naat(na, na_lex, na_en, na_tr, case="nasb", punct=punct, tags=list(na_tags))]
def allah_yalam(full="اللهُ", wa=False):
    return [tok(full, "allah", "propn", ([AT] if wa else []) + [MK], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", ("«and» + " if wa else "") + "«God» — the mubtadaʾ.", ("«ve» + " if wa else "") + "«Allah» — mübtedâ.", segments=(wa_("اللهُ", "allah", "propn") if wa else None)),
            mudari("يَعْلَمُ", "alima", "«knows»", "«bilir»", tags=[MK], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
            tok("مَنْ", "man", "pron", [MB, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«who» — the relative; the object of «knows».", "«kimin» — ism-i mevsûl; «bilir»in mef'ûlü."),
            mudari("يَحْمِلُ", "hamala", "«carries»", "«taşıdığını»", tags=[MW], extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ")]
def qawm_pron(full, pron_form, pron_lex, ar_role, en, tr, punct=None, tags=()):
    return noun_pron(full, "qawm", full[:len(full) - len(pron_form)], pron_form, pron_lex, ar_role, en, tr, tags=list(tags), punct=punct)
def inni_lakum_rasul(punct=None, quoted=True):
    toks = [tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I» — inna with the yāʾ of the speaker as its ism.", "«şüphesiz ben» — inne; mütekellim yâ'sı ismi.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
            tok("لَكُمْ", "li", "prep", [HJ, IW], "اللَّامُ حَرْفُ جَرٍّ، وَكُمْ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِرَسُولٌ (أَوْ بِمَحْذُوفٍ حَالٌ).", "«to you» — the phrase hangs on «messenger».", "«size» — ibare «elçi»ye bağlı.", segments=[seg("لَ", "li", "prep"), seg("كُمْ", "pron-2mp", "pron")]),
            khabar_inna("رَسُولٌ", "rasul", "«a messenger»", "«bir elçiyim»"),
            naat("أَمِينٌ", "amin", "«trustworthy»", "«güvenilir»", case="raf", punct=punct)]
    return quran(toks) if quoted else toks
def maa_na(role_ar, en="«with us»", tr="«bizimle»", punct=None):
    return tok("مَعَنَا", "maa", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ" + role_ar + ".", en, tr, punct=punct, segments=[seg("مَعَ", "maa", "noun"), seg("نَا", "pron-1p", "pron")])
def ama(punct=None):
    return tok("أَمَا", "ama", "part", [IS, "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَمَا نَافِيَةٌ — بِمَعْنَى أَلَمْ.", "«did … not?» — the question hamza over the negating mā.", "«… -medi mi?» — istifham hemzesi + nefiy mâ'sı.", punct=punct, segments=[seg("أَ", "hamza-istifham", "part"), seg("مَا", "ma-nafiya", "part")])
def wajada_allah(punct=None):
    return [mazi("وَجَدَ", "wajada", "«find»", "«bulmadı mı»", tags=["mithal-verbs"], hidden=None), allah_fail(punct=punct)]

# ---------------------------------------------------------------- §11 نُوحٌ الرَّسُولُ (print pp. 17–18)
sen("s1", "And God willed to send Nūḥ to his people.", "Allah, Nûh'u kavmine göndermeyi diledi.", [
  *arada_allah(),
  *an_yursila(),
  nuh_maful(),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  qawm_pron("قَوْمِهِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavmine»", tags=[HJ, ID], punct="."),
])
sen("s2", "There were among the people rich men and chiefs, but God chose Nūḥ for His message, and did not choose any of them.",
        "Kavmin içinde zenginler ve reisler vardı; fakat Allah risâleti için Nûh'u seçti ve onlardan hiçbirini seçmedi.", [
  kana("كَانَ", wa=False),
  fi(),
  majrur("الْقَوْمِ", "qawm", "«the people» — the phrase is kāna's fronted khabar.", "«kavmin içinde» — ibare kâne'nin öne alınmış haberi.", tags=[KN]),
  tok("أَغْنِيَاءُ", "ghani", "noun", [KN, JT, MM], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ غَنِيٍّ عَلَى أَفْعِلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.", "«rich men» — kāna's delayed ism; the plural أَفْعِلَاء is a diptote.", "«zenginler» — kâne'nin sonraya bırakılmış ismi; ef'ilâ vezni gayr-i munsarıf."),
  tok("وَرُؤَسَاءُ", "rais", "noun", [AT, JT, MM], "الْوَاوُ عَاطِفَةٌ، وَرُؤَسَاءُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ رَئِيسٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and chiefs» — joined; فُعَلَاء, a diptote.", "«ve reisler» — ma'tûf; fuâlâ vezni gayr-i munsarıf.", punct="،", segments=wa_("رُؤَسَاءُ", "rais", "noun")),
  tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kız kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  allah_ism(part="لٰكِنَّ"),
  mazi("اخْتَارَ", "ikhtara", "«chose»", "«seçti»", tags=[IW, "form-viii-verbs", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  nuh_maful(),
  li_risala_segs(punct="."),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not» — the jussive lam.", "«ve … -medi» — cezm eden lem.", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("يَخْتَرْ", "ikhtara", "verb", [LJ, "form-viii-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ أَلِفُهُ (عَيْنُ الْفِعْلِ) لِالْتِقَاءِ السَّاكِنَيْنِ: يَخْتَارْ → يَخْتَرْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«did [not] choose» — jazm by lam; the hollow verb loses its alif before the sukūn (يَخْتَارْ → يَخْتَرْ).", "«seçmedi» — lem ile meczum; ecvef fiilin elifi iki sâkin yüzünden düştü (يَخْتَارْ → يَخْتَرْ)."),
  maful_("أَحَدًا", "ahad", "«anyone»", "«hiçbirini»"),
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«of them» — the phrase is a ṣifa of «anyone».", "«onlardan» — ibare «hiçbiri»nin sıfatı.", tags=[NA], extra_ar=" — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِأَحَدًا", punct="."),
])
sen("s3", "God knows who carries His message, and God knows who carries His trust.", "Allah risâletini kimin taşıyacağını bilir; Allah emanetini kimin taşıyacağını bilir.", [
  *allah_yalam(),
  noun_pron("رِسَالَتَهُ", "risala", "رِسَالَتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His message» — the object, annexed.", "«risâletini» — mef'ûl, muzâf.", tags=[MB, ID], punct="،"),
  *allah_yalam("وَاللهُ", wa=True),
  noun_pron("أَمَانَتَهُ", "amana", "أَمَانَتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His trust» — the object, annexed.", "«emanetini» — mef'ûl, muzâf.", tags=[MB, ID], punct="."),
])
sen("s4", "And Nūḥ was a righteous, noble man; and Nūḥ was a wise, forbearing man.", "Nûh sâlih ve cömert bir adamdı; Nûh akıllı ve halîm bir adamdı.", [
  kana(), nuh_ism_kana(),
  khabar_kana("رَجُلًا", "rajul", "«a man»", "«bir adam»"),
  naat("صَالِحًا", "salih", "«righteous»", "«sâlih»", case="nasb"),
  naat2("كَرِيمًا", "karim", "«noble»", "«cömert»", case="nasb", punct="،"),
  kana(), nuh_ism_kana(),
  khabar_kana("رَجُلًا", "rajul", "«a man»", "«bir adam»"),
  naat("عَاقِلًا", "aqil", "«wise»", "«akıllı»", case="nasb"),
  naat2("حَلِيمًا", "halim", "«forbearing»", "«halîm»", case="nasb", punct="."),
])
sen("s5", "And Nūḥ was a sincere, tender counsellor; and Nūḥ was truthful and trustworthy.", "Nûh öğüt veren, şefkatli biriydi; Nûh doğru sözlü ve güvenilirdi.", [
  kana(), nuh_ism_kana(),
  khabar_kana("نَاصِحًا", "nasih", "«a counsellor»", "«öğüt veren»", tags=["ism-fail"]),
  naat("شَفِيقًا", "shafiq", "«tender»", "«şefkatli»", case="nasb", punct="،"),
  kana(), nuh_ism_kana(),
  khabar_kana("صَادِقًا", "sadiq", "«truthful»", "«doğru sözlü»", tags=["ism-fail"]),
  naat("أَمِينًا", "amin", "«trustworthy»", "«güvenilir»", case="nasb"),
])
sen("s6", "God chose Nūḥ for His message and revealed to him: «that: warn your people before a painful punishment comes to them».",
        "Allah risâleti için Nûh'u seçti ve ona vahyetti: «kavmini, onlara acı bir azap gelmeden önce uyar».", [
  mazi("اخْتَارَ", "ikhtara", "«chose»", "«seçti»", tags=["form-viii-verbs", "hollow-verbs"], hidden=None),
  allah_fail(),
  nuh_maful(),
  li_risala_segs(),
  tok("وَأَوْحَى", "awha", "verb", [AT, "form-iv-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَوْحَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and revealed» — a defective Form IV māḍī; the fatḥa is estimated on the alif.", "«ve vahyetti» — nâkıs if'âl mâzîsi; fetha elif üzerinde takdîrî.", segments=wa_("أَوْحَى", "awha", "verb")),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to him»", "«ona»", punct=":"),
  *quran([
    tok("أَنْ", "an-masdariyya", "part", [AN, IQ], "أَنْ تَفْسِيرِيَّةٌ بِمَعْنَى أَيْ — لِأَنَّ أَوْحَى فِيهِ مَعْنَى الْقَوْلِ دُونَ حُرُوفِهِ؛ وَقِيلَ مَصْدَرِيَّةٌ.", "«that» — the explaining an (= «namely»): the verb «revealed» carries the sense of saying without its letters.", "«ki» — tefsiriyye en (= yani): «vahyetti» söz mânâsı taşır."),
    tok("أَنْذِرْ", "andhara", "verb", [AM, "form-iv-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ.", "«warn» — an imperative of Form IV.", "«uyar» — if'âl bâbından emir."),
    qawm_pron("قَوْمَكَ", "كَ", "pron-2ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your people» — the object.", "«kavmini» — mef'ûl.", tags=[MB, ID]),
    prep("مِنْ", "min", "«from»", "«-den»"),
    tok("قَبْلِ", "qabla", "noun", [HJ, ID, MF], "ظَرْفُ زَمَانٍ مَجْرُورٌ بِمِنْ، مُضَافٌ إِلَى الْمَصْدَرِ الْمُؤَوَّلِ بَعْدَهُ.", "«before» — the time-noun after min, annexed to the an-clause.", "«önce» — min'den sonra zaman ismi; en cümlesine muzâf."),
    an_nasb("فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "«that»", "«-mesi»"),
    tok("يَأْتِيَهُمْ", "ata", "verb", [AN, MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَهُمْ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.", "«comes to them» — naṣb by an, the fatḥa visible on the yāʾ; the pronoun is the object, the doer follows.", "«onlara gelmesi» — en ile mansub; fetha yâ üzerinde açık; zamir mef'ûl, fâil sonra.", segments=[seg("يَأْتِيَ", "ata", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
    fail("عَذَابٌ", "adhab", "«a punishment»", "«bir azap»"),
    naat("أَلِيمٌ", "alim-painful", "«painful»", "«acı»", case="raf", punct="."),
  ]),
])
sen("s7", "So Nūḥ stood up among his people, saying to the people: «I am to you a trustworthy messenger».", "Bunun üzerine Nûh kavminin içinde kalkıp insanlara dedi: «Ben size güvenilir bir elçiyim».", [
  mazi("فَقَامَ", "qama", "«so stood up»", "«bunun üzerine kalktı»", tags=[AT, "hollow-verbs"], hidden=None, wa=True),
  nuh_fail(),
  fi(),
  qawm_pron("قَوْمِهِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavminin içinde»", tags=[HJ, ID]),
  tok("يَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", HL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ نُوحٍ.", "«saying» — the clause is a ḥāl of Nūḥ.", "«diyerek» — cümle Nûh'tan hâl."),
  li_noun("لِلنَّاسِ", "nas", "«the people»", "«insanlara»", punct=":"),
  *inni_lakum_rasul(punct="."),
])
# ---------------------------------------------------------------- §12 مَاذَا أَجَابَهُ الْقَوْمُ؟ (print pp. 18–19)
sen("s8", "And when Nūḥ stood up among his people saying: «I am to you a trustworthy messenger» —", "Nûh kavminin içinde kalkıp «ben size güvenilir bir elçiyim» deyince —", [
  tok("وَلَمَّا", "lamma", "part", [AT, MF, SH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ — وَجَوَابُهُ فِي السَّطْرِ التَّالِي: قَامَ بَعْضُ النَّاسِ.", "«and when» — lammā, the conditional time-adverb; its answer is the next line («some of the people stood up»).", "«ve … -ınca» — şart anlamlı zaman zarfı lemmâ; cevabı sonraki satırdır («bazı insanlar kalktı»).", segments=wa_("لَمَّا", "lamma", "part")),
  mazi("قَامَ", "qama", "«stood up»", "«kalktı»", tags=["hollow-verbs", SH], hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ"),
  nuh_fail(),
  fi(),
  qawm_pron("قَوْمِهِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his people»", "«kavminin içinde»", tags=[HJ, ID]),
  tok("يَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", HL], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«saying» — a ḥāl clause.", "«diyerek» — hâl cümlesi.", punct=":"),
  *inni_lakum_rasul(punct="."),
])
sen("s9", "some of the people stood up saying: when did this one become a prophet?", "bazı insanlar kalkıp dediler: bu ne zaman peygamber oldu?", [
  mazi("قَامَ", "qama", "«stood up»", "«kalktı»", tags=["hollow-verbs", SH], hidden=None, extra_ar=" — جَوَابُ لَمَّا"),
  fail("بَعْضُ", "baad", "«some [of]»", "«bazısı»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("النَّاسِ", "nas", "«the people»", "«insanların»"),
  khamsa("يَقُولُونَ", "qala", "«saying»", "«diyerek»", tags=[HL, "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", punct=":"),
  tok("مَتَى", "mata-istifham", "pron", [IS, MF], "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ ظَرْفُ زَمَانٍ.", "«when» — the question noun of time, in the place of a ẓarf.", "«ne zaman» — zaman soru ismi; mahallen mansub zarf."),
  tok("صَارَ", "sara", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«became» — ṣāra, a sister of kāna.", "«oldu» — kâne'nin kız kardeşi sâre."),
  tok("هٰذَا", "hadha", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ صَارَ.", "«this one» — the demonstrative; ṣāra's ism.", "«bu» — ism-i işâret; sâre'nin ismi."),
  khabar_kana("نَبِيًّا", "nabi", "«a prophet»", "«peygamber»", punct="؟", ar="خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ."),
])
sen("s10", "Yesterday he was a man from among us, and today he says: I am God's messenger to you!", "Dün bizden bir adamdı, bugün ise «ben Allah'ın size elçisiyim» diyor!", [
  tok("بِالْأَمْسِ", "ams", "noun", [HJ, MF], "الْبَاءُ حَرْفُ جَرٍّ، وَأَمْسِ ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ (أَوْ مَجْرُورٌ بِالْكَسْرَةِ عَلَى لُغَةٍ).", "«yesterday» — bi + ams, the time-noun built on kasra.", "«dün» — bi + kesre üzere mebnî zaman ismi emsi.", segments=[seg("بِ", "bi", "prep"), seg("الْأَمْسِ", "ams", "noun")]),
  kana("كَانَ", wa=False),
  khabar_kana("رَجُلًا", "rajul", "«a man»", "«bir adam»", ar="خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ."),
  tok("مِنَّا", "min", "prep", [HJ, NA], "مِنْ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ، أُدْغِمَتِ النُّونُ فِي النُّونِ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِرَجُلًا.", "«from among us» — min + nā, the two nūns assimilated; a ṣifa of «a man».", "«bizden» — min + nâ, iki nûn idgam; «adam»ın sıfatı.", segments=[seg("مِنْ", "min", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("وَالْيَوْمَ", "yawm", "noun", [AT, MF], "الْوَاوُ عَاطِفَةٌ، وَالْيَوْمَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and today» — a time adverbial.", "«ve bugün» — zaman zarfı.", segments=wa_("الْيَوْمَ", "yawm", "noun")),
  tok("يَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.", "«he says» — what is said is its object.", "«diyor» — söylenen söz mef'ûl."),
  pron_mubtada("أَنَا", "ana", "«I»", "«ben»"),
  tok("رَسُولُ", "rasul", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the messenger [of]» — the khabar, annexed.", "«elçisi» — haber, muzâf."),
  allah_mi(),
  prep_pron("إِلَيْكُمْ", "ila", "كُمْ", "pron-2mp", "«to you»", "«size»", punct="!"),
])
sen("s11", "And Nūḥ's friends said: this one used to play with us in childhood and sit with us every day — so when did prophethood come to him? By night or by day?!…",
        "Nûh'un arkadaşları dedi: bu, çocuklukta bizimle oynar, her gün bizimle otururdu — peygamberlik ona ne zaman geldi? Gece mi, gündüz mü?!…", [
  qala("وَقَالَ", wa=True, punct=None),
  tok("أَصْدِقَاءُ", "sadiq-friend", "noun", [FL, ID, JT, MM], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — جَمْعُ صَدِيقٍ عَلَى أَفْعِلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«the friends [of]» — the doer; أَفْعِلَاء, a diptote.", "«arkadaşları» — fâil; ef'ilâ vezni gayr-i munsarıf."),
  tok("نُوحٍ", "nuh", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — the muḍāf ilayh; the name takes tanwīn.", "«Nûh'un» — muzâfun ileyh; tenvinli.", punct=":"),
  tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this one» — the mubtadaʾ.", "«bu» — mübtedâ."),
  tok("كَانَ", "kana", "verb", [KN, MK, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.", "«used to» — kāna; its ism is concealed; the clause is the khabar.", "«-di» — kâne; ismi gizli; cümle haber."),
  mudari("يَلْعَبُ", "laiba", "«play»", "«oynar»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  maa_na(" — مُتَعَلِّقٌ بِيَلْعَبُ"),
  fi(),
  majrur("الصِّغَرِ", "sighar", "«childhood»", "«çocuklukta»"),
  mudari_wa("وَيَجْلِسُ", "jalasa", "«and sit»", "«ve oturur»", tags=[KN], extra=" — مَعْطُوفٌ عَلَى يَلْعَبُ"),
  maa_na(" — مُتَعَلِّقٌ بِيَجْلِسُ"),
  tok("كُلَّ", "kull", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (نَائِبٌ عَنِ الظَّرْفِ)، مُضَافٌ.", "«every» — annexed; the phrase is a time adverbial.", "«her» — muzâf; terkip zaman zarfı."),
  mudaf_ilayh("يَوْمٍ", "yawm", "«day»", "«gün»"),
  tok("فَمَتَى", "mata-istifham", "pron", [AT, IS, MF], "الْفَاءُ لِلتَّفْرِيعِ، وَمَتَى اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفُ زَمَانٍ.", "«so when» — the question noun of time.", "«peki ne zaman» — zaman soru ismi.", segments=[seg("فَ", "fa", "conj"), seg("مَتَى", "mata-istifham", "pron")]),
  tok("جَاءَتْهُ", "jaa", "verb", [MB, "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.", "«came to him» — with the feminine tāʾ; the pronoun is the object, the doer follows.", "«ona geldi» — te'nis tâ'sı; zamir mef'ûl, fâil sonra.", segments=[seg("جَاءَتْ", "jaa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  fail("النُّبُوَّةُ", "nubuwwa", "«prophethood»", "«peygamberlik»", punct="؟"),
  tok("أَلَيْلًا", "layl", "noun", [IS, MF], "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَلَيْلًا ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — مُتَعَلِّقٌ بِجَاءَتْ.", "«by night?» — the question hamza + a time adverbial.", "«gece mi?» — istifham hemzesi + zaman zarfı.", segments=[seg("أَ", "hamza-istifham", "part"), seg("لَيْلًا", "layl", "noun")]),
  tok("أَمْ", "am", "part", [AT, IS], "حَرْفُ عَطْفٍ — أَمِ الْمُتَّصِلَةُ بَعْدَ هَمْزَةِ التَّسْوِيَةِ وَالتَّعْيِينِ.", "«or» — the connected am after the question hamza.", "«yoksa» — hemzeden sonra muttasıla em."),
  tok("نَهَارًا", "nahar", "noun", [AT, MF], "مَعْطُوفٌ عَلَى لَيْلًا مَنْصُوبٌ بِالْفَتْحَةِ — ظَرْفُ زَمَانٍ.", "«by day» — joined to «by night».", "«gündüz» — «gece»ye ma'tûf.", punct="!..."),
])
sen("s12", "And the rich and the proud said: did God not find anyone other than him?", "Zenginler ve kibirliler dedi: Allah ondan başkasını bulamadı mı?", [
  qala("وَقَالَ", wa=True, punct=None),
  tok("الْأَغْنِيَاءُ", "ghani", "noun", [FL, JT], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ غَنِيٍّ.", "«the rich» — the doer; a broken plural.", "«zenginler» — fâil; cem-i teksîr."),
  tok("وَالْمُتَكَبِّرُونَ", "mutakabbir", "noun", [AT, JS, "ism-fail"], "الْوَاوُ عَاطِفَةٌ، وَالْمُتَكَبِّرُونَ مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ فَاعِلٍ مِنْ تَكَبَّرَ.", "«and the proud» — joined; a sound plural, rafʿ by the wāw.", "«ve kibirliler» — ma'tûf; cemi müzekker sâlim, vâv ile merfû.", punct=":", segments=wa_("الْمُتَكَبِّرُونَ", "mutakabbir", "noun")),
  ama(),
  *wajada_allah(),
  maful_("أَحَدًا", "ahad", "«anyone»", "«birini»"),
  tok("غَيْرَهُ", "ghayr", "noun", [NA, ID], "نَعْتٌ لِأَحَدًا مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«other than him» — a naʿt of «anyone», annexed.", "«ondan başka» — «biri»nin sıfatı, muzâf.", punct="؟", segments=[seg("غَيْرَ", "ghayr", "noun"), seg("هُ", "pron-3ms", "pron")]),
])
sen("s13", "Have all the people died? Did He find among the people none but a poor man?", "İnsanların hepsi öldü mü? Kavmin içinde bir fakirden başkasını bulamadı mı?", [
  tok("أَمَاتَ", "mata-die", "verb", [IS, "hollow-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَمَاتَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«have … died?» — the question hamza on the māḍī (not the Form IV أَمَاتَ: the people are the doer).", "«öldü mü?» — istifham hemzesi + mâzî (if'âl bâbı değil: insanlar fâildir).", segments=[seg("أَ", "hamza-istifham", "part"), seg("مَاتَ", "mata-die", "verb")]),
  nas_fail(),
  noun_pron("كُلُّهُمْ", "kull", "كُلُّ", "هُمْ", "pron-3mp", "تَوْكِيدٌ مَعْنَوِيٌّ لِلنَّاسِ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«all of them» — the emphasis of «the people».", "«hepsi» — «insanlar»ın mânevî tekidi.", tags=["tawkid", ID], punct="،"),
  ama(),
  mazi("وَجَدَ", "wajada", "«find»", "«bulmadı mı»", tags=["mithal-verbs"]),
  fi(),
  majrur("الْقَوْمِ", "qawm", "«the people»", "«kavmin içinde»"),
  tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ (الْكَلَامُ مَنْفِيٌّ، وَالْمُسْتَثْنَى مِنْهُ مَحْذُوفٌ).", "«but» — the «emptied» exception: the word after it takes the verb's own case.", "«-den başka» — müferrağ istisnâ: sonraki kelime fiilin kendi i'râbını alır."),
  maful_("فَقِيرًا", "faqir", "«a poor man»", "«bir fakir»", tags=[IST], punct="؟", ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — بَعْدَ إِلَّا الْمُفَرَّغَةِ."),
])
sen("s14", "And the ignorant said: «this is nothing but a human like you».", "Câhiller dedi: «bu, sizin gibi bir insandan başka bir şey değil».", [
  qala("وَقَالَ", wa=True, punct=None),
  tok("الْجُهَّالُ", "jahil", "noun", [FL, JT], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ جَاهِلٍ عَلَى فُعَّالٍ.", "«the ignorant» — the doer; the plural فُعَّال of the participle.", "«câhiller» — fâil; ism-i fâilin fu''âl cem'i.", punct=":"),
  *quran([
    tok("مَا", "ma-nafiya", "part", ["la-nafiya", IQ], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا (لِانْتِقَاضِ النَّفْيِ بِإِلَّا).", "«not» — the negating mā; it does not govern, because illā breaks the negation.", "«değil» — nefiy mâ'sı; illâ nefyi bozduğu için amel etmez."),
    tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bu» — mübtedâ."),
    tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ (حَصْرٍ).", "«but» — the exceptive, here of restriction.", "«… -den başka» — hasr edatı."),
    khabar("بَشَرٌ", "bashar", "«a human»", "«bir insan»"),
    noun_pron("مِثْلُكُمْ", "mithl", "مِثْلُ", "كُمْ", "pron-2mp", "نَعْتٌ لِبَشَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«like you» — a naʿt of «a human», annexed.", "«sizin gibi» — «insan»ın sıfatı, muzâf.", tags=[NA, ID], punct="."),
  ]),
])
sen("s15", "And they said: «had God willed, He would have sent down angels; we never heard of this among our forefathers».", "Ve dediler: «Allah dileseydi melekler indirirdi; biz bunu önceki atalarımızdan işitmedik».", [
  qalu("وَقَالُوا", wa=True),
  *quran([
    tok("لَوْ", "law", "part", [SH, IQ], "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ (حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ).", "«had» — the unreal conditional: the answer failed because the condition failed.", "«-seydi» — cezmetmeyen şart harfi; imtinâ li-imtinâ."),
    mazi("شَاءَ", "shaa", "«willed»", "«dileseydi»", tags=[SH, "hollow-verbs"], hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ"),
    allah_fail(),
    tok("لَأَنْزَلَ", "anzala", "verb", [SH, "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَأَنْزَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جَوَابُ الشَّرْطِ.", "«He would have sent down» — the lām of the answer of law + the māḍī.", "«indirirdi» — lev'in cevabına gelen lâm + mâzî.", segments=[seg("لَ", "la-ibtida", "part"), seg("أَنْزَلَ", "anzala", "verb")]),
    maful_("مَلَائِكَةً", "malak", "«angels»", "«melekler»", tags=[JT], punct="،", ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ مَلَكٍ."),
    tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ.", "«not» — the negating mā.", "«-medik» — nefiy mâ'sı."),
    tok("سَمِعْنَا", "samia", "verb", ["la-nafiya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«we heard» — a māḍī built on sukūn before «we»; nā is its doer.", "«işittik» — nâ'ya bitişince sükûn üzere mebnî; nâ fâil.", segments=[seg("سَمِعْ", "samia", "verb"), seg("نَا", "pron-1p", "pron")]),
    tok("بِهٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمُ الْإِشَارَةِ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«of this» — bi + the demonstrative.", "«bunu» — bâ + ism-i işâret.", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
    fi(),
    noun_pron("آبَائِنَا", "ab", "آبَائِ", "نَا", "pron-1p", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ أَبٍ.", "«our forefathers» — annexed to «our»; the plural of أَب.", "«atalarımız» — nâ'ya muzâf; eb'in cem'i.", tags=[HJ, ID, JT]),
    js_naat("الْأَوَّلِينَ", "awwal", "«former»", "«önceki»"),
  ]),
])
sen("s16", "And some of the people said that Nūḥ wants to attain the chieftainship and honour by this road.", "Bazı insanlar da dedi ki Nûh bu yolla riyâset ve şeref elde etmek istiyor.", [
  qala("وَقَالَ", wa=True, punct=None),
  fail("بَعْضُ", "baad", "«some [of]»", "«bazısı»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("النَّاسِ", "nas", "«the people»", "«insanların»"),
  inna(),
  tok("نُوحًا", "nuh", "propn", [IW], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ — عَلَمٌ مُنْصَرِفٌ.", "«Nūḥ» — inna's ism.", "«Nûh» — inne'nin ismi."),
  mudari("يُرِيدُ", "arada", "«wants»", "«istiyor»", tags=[IW, "form-iv-verbs", "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ"),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيُرِيدُ", "«to»", "«-mek»"),
  tok("يَنَالَ", "nala", "verb", [AN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«attain» — naṣb by an; the doer is concealed.", "«elde etmek» — en ile mansub; fâil gizli."),
  maful_("الرِّيَاسَةَ", "riyasa", "«the chieftainship»", "«riyâseti»"),
  atf("وَالشَّرَفَ", "sharaf", "«honour»", "«şerefi»", case="nasb"),
  tok("بِهٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمُ الْإِشَارَةِ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«by this» — bi + the demonstrative.", "«bu … ile» — bâ + ism-i işâret.", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("الطَّرِيقِ", "tariq", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ (أَوْ عَطْفُ بَيَانٍ).", "«road» — a badal of the demonstrative.", "«yol» — ism-i işâretten bedel.", punct="."),
])

CAND = {
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend", "istemek, dilemek", 1),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send", "göndermek", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ (الْمَصْدَرِيَّة)", None, "part", "that, to (+ subjunctive)", "-mek, -mesi (muzâriyi nasbeder)", 1),
 "nuh": G("nuh", "نُوح", None, "propn", "Nūḥ (Noah)", "Nûh", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people, a group", "kavim, topluluk", 1, plural="أَقْوَام"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de, içinde", 1),
 "ghani": G("ghani", "غَنِيّ", "غ ن ي", "noun", "rich", "zengin", 1, plural="أَغْنِيَاء"),
 "rais": G("rais", "رَئِيس", "ر أ س", "noun", "a chief, a leader", "reis, başkan", 1, plural="رُؤَسَاء"),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but — the corrective sister of inna", "fakat — inne'nin istidrâk kız kardeşi", 1),
 "ikhtara": G("ikhtara", "اخْتَارَ", "خ ي ر", "verb", "to choose (Form VIII, hollow)", "seçmek (iftiâl, ecvef)", 1),
 "risala": G("risala", "رِسَالَة", "ر س ل", "noun", "messengership", "risâlet, elçilik", 1),
 "lam-jazima": G("lam-jazima", "لَمْ", None, "part", "did not (negates, jazm, turns the tense back)", "-medi (nefyeder, cezmeder, mânâyı maziye çevirir)", 1),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "anyone, one", "biri, kimse", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know", "bilmek", 1),
 "man": G("man", "مَنْ", None, "pron", "who, whoever — the relative and conditional noun", "kim, kimse — ism-i mevsûl ve şart ismi", 1),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry", "taşımak", 1),
 "amana": G("amana", "أَمَانَة", "أ م ن", "noun", "trust", "emanet", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam", 1, plural="رِجَال"),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous person", "sâlih", 1),
 "karim": G("karim", "كَرِيم", "ك ر م", "noun", "noble, generous", "cömert, kerim", 1),
 "aqil": G("aqil", "عَاقِل", "ع ق ل", "noun", "wise, sensible (ism fa'il)", "akıllı (ism-i fâil)", 1),
 "halim": G("halim", "حَلِيم", "ح ل م", "noun", "forbearing, mild (ṣifa mushabbaha)", "halîm, yumuşak huylu", 1),
 "nasih": G("nasih", "نَاصِح", "ن ص ح", "noun", "sincere adviser", "öğüt veren, nâsih", 1),
 "shafiq": G("shafiq", "شَفِيق", "ش ف ق", "noun", "tender, compassionate (ṣifa mushabbaha)", "şefkatli, şefik", 1),
 "sadiq": G("sadiq", "صَادِق", "ص د ق", "noun", "truthful", "doğru sözlü, sâdık", 1),
 "amin": G("amin", "أَمِين", "أ م ن", "noun", "trustworthy, faithful (ṣifa mushabbaha)", "güvenilir, emin", 1),
 "awha": G("awha", "أَوْحَى", "و ح ي", "verb", "to inspire, to reveal (Form IV, defective)", "vahyetmek (if'âl, nâkıs)", 1),
 "andhara": G("andhara", "أَنْذَرَ", "ن ذ ر", "verb", "to warn (Form IV)", "uyarmak (if'âl)", 1),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before (a zarf of time or place)", "önce (zaman/mekân zarfı)", 1),
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come", "gelmek", 1),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment", "azap", 1),
 "alim-painful": G("alim-painful", "أَلِيم", "أ ل م", "noun", "painful", "acı, elîm", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to stand; to subsist (بِ: in/through)", "kalkmak, ayağa kalkmak", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "nas": G("nas", "النَّاس", "ن و س", "noun", "the people", "insanlar", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — the emphasizing particle", "şüphesiz — tekid harfi", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "messenger", "elçi, resûl", 1, plural="رُسُل"),
 "lamma": G("lamma", "لَمَّا", None, "part", "when (with a past verb)", "-ınca, -dığı zaman (mâzî ile)", 1),
 "baad": G("baad", "بَعْض", "ب ع ض", "noun", "part, some", "bazı, bir kısmı", 1),
 "mata-istifham": G("mata-istifham", "مَتَى", None, "pron", "when? (interrogative; the same word also serves as a conditional noun)", "ne zaman? (soru ismi; şart ismi de olur)", 1),
 "sara": G("sara", "صَارَ", "ص ي ر", "verb", "to become (a sister of كان)", "olmak, hâline gelmek (kâne'nin kız kardeşi)", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this (masc.)", "bu", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "prophet", "peygamber, nebî", 1, plural="أَنْبِيَاء"),
 "ams": G("ams", "أَمْسِ", None, "noun", "yesterday (a zarf, mabni on the kasra)", "dün (kesre üzere mebnî zarf)", 1),
 "bi": G("bi", "بِ", None, "prep", "by, with, in", "ile, -de", 1),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "day", "gün", 1, plural="أَيَّام"),
 "ana": G("ana", "أَنَا", None, "pron", "I (detached)", "ben (munfasıl)", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "sadiq-friend": G("sadiq-friend", "صَدِيق", "ص د ق", "noun", "friend", "arkadaş, dost", 1, plural="أَصْدِقَاء"),
 "laiba": G("laiba", "لَعِبَ", "ل ع ب", "verb", "to play", "oynamak", 1),
 "maa": G("maa", "مَعَ", None, "adv", "with, together with", "ile, beraber", 1),
 "sighar": G("sighar", "صِغَر", "ص غ ر", "noun", "childhood, smallness (maṣdar of صَغُرَ)", "çocukluk, küçüklük", 1),
 "jalasa": G("jalasa", "جَلَسَ", "ج ل س", "verb", "to sit", "oturmak", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every; the whole of it", "her, bütün", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب أ", "noun", "prophethood", "peygamberlik, nübüvvet", 1),
 "hamza-istifham": G("hamza-istifham", "أَ (الِاسْتِفْهَام)", None, "part", "the question hamza — what follows it is the thing asked about", "soru hemzesi", 1),
 "layl": G("layl", "لَيْل", "ل ي ل", "noun", "night", "gece", 1, plural="لَيَالٍ"),
 "am": G("am", "أَمْ", None, "part", "or…? (the ta'yin connective, paired with a question hamza)", "yoksa …? (soru hemzesiyle)", 1),
 "nahar": G("nahar", "نَهَار", "ن ه ر", "noun", "daytime", "gündüz", 1),
 "mutakabbir": G("mutakabbir", "مُتَكَبِّر", "ك ب ر", "noun", "proud, arrogant (ism fāʿil of تَكَبَّرَ)", "kibirli, mütekebbir", 1),
 "ama": G("ama", "أَمَا", None, "part", "did … not? — the question hamza over the negating mā", "… -medi mi? — soru hemzesi + nefiy mâ'sı", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (negates past verbs)", "değil, -medi (nefiy mâ'sı)", 1),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find", "bulmak", 1),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other, someone else", "başka, gayrı", 1),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die", "ölmek", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except, but (exception)", "ancak, -den başka (istisnâ)", 1),
 "faqir": G("faqir", "فَقِير", "ف ق ر", "noun", "poor (ṣifa mushabbaha)", "fakir", 1, plural="فُقَرَاء"),
 "jahil": G("jahil", "جَاهِل", "ج ه ل", "noun", "ignorant (ism fa'il)", "câhil (ism-i fâil)", 1),
 "bashar": G("bashar", "بَشَر", "ب ش ر", "noun", "human beings, mankind", "insan, beşer", 1),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "like, similar to", "gibi, benzer", 1),
 "law": G("law", "لَوْ", None, "part", "if (unreal — imtina' li-imtina')", "eğer, -seydi (imtinâ li-imtinâ)", 1),
 "shaa": G("shaa", "شَاءَ", "ش ي أ", "verb", "to will", "dilemek", 1),
 "anzala": G("anzala", "أَنْزَلَ", "ن ز ل", "verb", "to send down", "indirmek", 1),
 "la-ibtida": G("la-ibtida", "لَ", None, "part", "the lām of emphasis (lām al-ibtidāʾ)", "tekid lâmı (lâm-ı ibtidâ)", 1),
 "malak": G("malak", "مَلَك", "م ل ك", "noun", "angel", "melek", 1, plural="مَلَائِكَة"),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear, listen", "işitmek, dinlemek", 1),
 "ab": G("ab", "أَب", "أ ب و", "noun", "father (one of the five nouns)", "baba (beş isimden)", 1, plural="آبَاء"),
 "awwal": G("awwal", "أَوَّل", "أ و ل", "noun", "first", "ilk, birinci", 1),
 "nala": G("nala", "نَالَ", "ن ي ل", "verb", "to reach, to attain", "elde etmek, nail olmak", 1),
 "riyasa": G("riyasa", "رِيَاسَة", "ر أ س", "noun", "chieftainship, leadership", "riyâset, başkanlık", 1),
 "sharaf": G("sharaf", "شَرَف", "ش ر ف", "noun", "honour, standing", "şeref", 1),
 "tariq": G("tariq", "طَرِيق", "ط ر ق", "noun", "way, road", "yol", 1, plural="طُرُق"),
 "pron-2ms": G("pron-2ms", "ـكَ", None, "pron", "you / your (attached pronoun)", "sen / senin (bitişik)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you (pl.) / your (attached)", "siz / sizin (bitişik)", 1),
 "pron-1p": G("pron-1p", "ـنَا", None, "pron", "us / our (attached)", "biz / bizim (bitişik)", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "my (attached pronoun)", "benim (bitişik)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "fa": G("fa", "فَـ", None, "part", "so, for, then", "bunun üzerine, böylece", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (simple negation)", "değil, -mez (nefiy lâ'sı)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch6 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 6 (print pp. 17–19; Nūḥ §11–12): Nūḥ the messenger — God wills to send Nūḥ; there were rich men and chiefs, but God chose Nūḥ and none of them, for God knows who carries His message; Nūḥ was righteous and noble, wise and forbearing, a tender counsellor, truthful and trustworthy; the revelation «warn your people before a painful punishment comes to them» (71:1) and Nūḥ's «I am to you a trustworthy messenger» (26:107) (s1–s7). "
          "What did the people answer? — some: when did this one become a prophet? yesterday one of us, today God's messenger!; his friends: he played and sat with us every day — when did prophethood come to him, by night or by day?; the rich and the proud: did God find no one else? have all the people died?; the ignorant: «this is nothing but a human like you» and «had God willed He would have sent down angels» (23:24); and some: he wants the chieftainship and honour by this road (s8–s16). One printed line is one sentence; lammā's answer stands on the next line.")
ADD_TR = (" Altıncı bölüm (basılı s. 17–19; Nûh §11–12): elçi Nûh — Allah Nûh'u göndermeyi diler; kavimde zenginler ve reisler vardı, fakat Allah onlardan hiçbirini değil Nûh'u seçti, çünkü risâletini kimin taşıyacağını Allah bilir; Nûh sâlih ve cömert, akıllı ve halîm, şefkatli bir öğütçü, doğru sözlü ve güvenilirdi; «kavmini, onlara acı bir azap gelmeden önce uyar» vahyi (71:1) ve Nûh'un «ben size güvenilir bir elçiyim» sözü (26:107) (s1–s7). "
          "Kavmi ne cevap verdi? — kimi: bu ne zaman peygamber oldu? dün bizden biriydi, bugün Allah'ın elçisi!; arkadaşları: bizimle oynar, her gün otururdu — peygamberlik ona ne zaman geldi, gece mi gündüz mü?; zenginler ve kibirliler: Allah başkasını bulamadı mı? insanların hepsi öldü mü?; câhiller: «bu sizin gibi bir insandan başkası değil», «Allah dileseydi melekler indirirdi» (23:24); kimi de: bu yolla riyâset ve şeref istiyor (s8–s16). Basılı her satır bir cümledir; lemmâ'nın cevabı sonraki satırdadır.")
write_out(6, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §11–12, pp. 17–19", GLOSS_ADD, notes=(), related=())
report(6, S, GLOSS_ADD, ())
