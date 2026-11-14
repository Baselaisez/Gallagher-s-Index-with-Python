# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Two — chapter 5: «سَفِينَةُ نُوحٍ» §9 الرَّسُول (why God sends a man from among the people; kings do not speak to each one; no one sees God but whom He wills) and §10 بَشَرٌ أَمْ مَلَك (the messenger must be a human: the people's excuses if he were an angel, and the answer when he is a man like them). Print pp. 15–17.
python3 tools/authoring/author_qisas2_ch5.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: الرَّسُولُ — بَشَرٌ أَمْ مَلَكٌ؟", "en": "The ship of Nūḥ: the messenger — a human or an angel?", "tr": "Nûh'un gemisi: elçi — insan mı, melek mi?"}
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

# ---------------------------------------------------------------- § chapter 5's own small helpers
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

# ---------------------------------------------------------------- §9 الرَّسُولُ (print pp. 15–16)
sen("s1", "And God willed to send to them a man from among them who would speak to them and counsel them.",
        "Allah onlara, kendilerinden, onlarla konuşacak ve onlara öğüt verecek bir adam göndermeyi diledi.", [
  *arada_allah(),
  *an_yursila(),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«to them»", "«onlara»"),
  maful_("رَجُلًا", "rajul", "«a man»", "«bir adam»"),
  prep_pron("مِنْهُمْ", "min", "هُمْ", "pron-3mp", "«from among them» — the phrase is a ṣifa of «a man».", "«onlardan» — ibare «adam»ın sıfatı.", tags=[NA], extra_ar=" — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِرَجُلًا"),
  yukallimuhum(),
  *wa_yansah("."),
])
sen("s2", "God does not speak to each one, one by one; God does not address every single person, saying to him: do this, do that.",
        "Allah herkesle tek tek konuşmaz; Allah her bir kişiye «şunu yap, bunu yap» diye hitap etmez.", [
  *inna_allah_la("يُكَلِّمُ", "kallama", "«does not speak to»", "«konuşmaz»", tags=["form-ii-verbs"]),
  *wahidan_wahidan("،"),
  *inna_allah_la("يُخَاطِبُ", "khataba", "«does not address»", "«hitap etmez»", tags=["form-iii-verbs"]),
  *kull_ahad("nasb"),
  *yaqul_lahu("يَقُولُ"),
  *ifal_kadha("،"),
  *ifal_kadha("."),
])
sen("s3", "Kings do not speak to each one, one by one;", "Krallar herkesle tek tek konuşmaz;", [
  *inna_muluk_la("يُكَلِّمُونَ", "kallama", "«do not speak to»", "«konuşmazlar»", tags=["form-ii-verbs"]),
  *wahidan_wahidan(None),
])
sen("s4", "kings do not go to every single person, saying to him: do this, do that.", "krallar her bir kişiye gidip ona «şunu yap, bunu yap» demezler.", [
  *inna_muluk_la("يَذْهَبُونَ", "dhahaba", "«do not go»", "«gitmezler»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  *kull_ahad("jarr"),
  *yaqul_lahu("يَقُولُونَ", pl=True),
  *ifal_kadha("،"),
  *ifal_kadha("."),
])
sen("s5", "And kings are humans like [other] humans: everyone can see them and hear their speech; but no one can see God, hear His speech and speak to Him — no one can do that except whom God wills, when God wills.",
        "Krallar da insanlar gibi insandır: herkes onları görebilir ve sözlerini işitebilir; fakat kimse Allah'ı göremez, sözünü işitemez ve O'nunla konuşamaz — buna ancak Allah'ın dilediği kimse, Allah dilediği zaman güç yetirir.", [
  tok("وَالْمُلُوكُ", "malik-king", "noun", [AT, MK, JT], "الْوَاوُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَالْمُلُوكُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ مَلِكٍ.", "«and the kings» — the mubtadaʾ; a broken plural of malik.", "«ve krallar» — mübtedâ; melik'in cem-i teksîri.", segments=wa_("الْمُلُوكُ", "malik-king", "noun")),
  khabar("بَشَرٌ", "bashar", "«[are] humans»", "«insandır»"),
  ka_prep("كَالْبَشَرِ", "bashar", "«[other] humans» — the phrase is a ṣifa of the khabar.", "«insanlar» — ibare haberin sıfatı.", punct="،", tags=[NA]),
  mudari("يَقْدِرُ", "qadara-able", "«is able»", "«güç yetirir»", hidden=None, extra_ar=" (الْفَاعِلُ بَعْدَهُ)"),
  *kull_ahad("raf"),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيَقْدِرُ (أَوْ مَجْرُورٌ بِعَلَى الْمَحْذُوفَةِ)", "«to»", "«-meye»"),
  tok("يَرَاهُمْ", "raa", "verb", [AN, MB, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«see them» — naṣb by an, the fatḥa estimated on the alif.", "«onları görmeye» — en ile mansub; fetha elif üzerinde takdîrî.", segments=[seg("يَرَى", "raa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("وَيَسْمَعَ", "samia", "verb", [AT, AN], "الْوَاوُ عَاطِفَةٌ، وَيَسْمَعَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَرَاهُمْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and hear» — naṣb by being joined to the verb before it.", "«ve işitmeye» — öncekine atıfla mansub.", segments=wa_("يَسْمَعَ", "samia", "verb")),
  noun_pron("كَلَامَهُمْ", "kalam", "كَلَامَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their speech» — the object, annexed to the pronoun.", "«sözlerini» — mef'ûl, zamire muzâf.", tags=[MB, ID], punct="،"),
  la_nafiya("وَلَا", wa=True),
  tok("يَقْدِرُ", "qadara-able", "verb", ["la-nafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ بَعْدَهُ.", "«is able» — the doer follows.", "«güç yetirir» — fâil sonra gelir."),
  fail("أَحَدٌ", "ahad", "«anyone»", "«kimse»"),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيَقْدِرُ", "«to»", "«-meye»"),
  tok("يَرَى", "raa", "verb", [AN, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«see» — naṣb by an, the fatḥa estimated on the alif.", "«görmeye» — en ile mansub; fetha elif üzerinde takdîrî."),
  allah_maful(),
  tok("وَيَسْمَعَ", "samia", "verb", [AT, AN], "الْوَاوُ عَاطِفَةٌ، وَيَسْمَعَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَرَى، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and hear» — naṣb by being joined.", "«ve işitmeye» — atıfla mansub.", segments=wa_("يَسْمَعَ", "samia", "verb")),
  noun_pron("كَلَامَهُ", "kalam", "كَلَامَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His speech» — the object, annexed to the pronoun.", "«sözünü» — mef'ûl, zamire muzâf.", tags=[MB, ID]),
  tok("وَيُكَلِّمَهُ", "kallama", "verb", [AT, AN, MB, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُكَلِّمَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and speak to Him» — naṣb by being joined; the pronoun is its object.", "«ve O'nunla konuşmaya» — atıfla mansub; zamir mef'ûl.", punct="،", segments=[seg("وَ", "wa", "conj"), seg("يُكَلِّمَ", "kallama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  la_nafiya("وَلَا", wa=True),
  tok("يَقْدِرُ", "qadara-able", "verb", ["la-nafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ بَعْدَ إِلَّا.", "«is able» — the doer comes after illā.", "«güç yetirir» — fâil illâ'dan sonra gelir."),
  prep("عَلَى", "ala", "«to [do]»", "«-e»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«that» — the demonstrative after ʿalā.", "«buna» — alâ'dan sonra ism-i işâret."),
  tok("إِلَّا", "illa", "part", [IST], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ (الْكَلَامُ مَنْفِيٌّ وَالْمُسْتَثْنَى مِنْهُ مَحْذُوفٌ)، لَا عَمَلَ لَهَا هُنَا.", "«except» — the exception is «emptied»: the negated sentence has no stated whole, so the word after illā takes the verb's own case.", "«ancak» — müferrağ istisnâ: müstesnâ minh zikredilmemiş; illâ'dan sonraki kelime fiilin kendi i'râbını alır."),
  tok("مَنْ", "man", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ يَقْدِرُ.", "«whom» — the relative noun; the doer of «is able».", "«kimse» — ism-i mevsûl; «güç yetirir»in fâili."),
  mazi("أَرَادَ", "arada", "«God wills»", "«Allah'ın dilediği»", tags=[MW, "hollow-verbs", "form-iv-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: أَرَادَهُ"),
  allah_fail(punct="،"),
  idha(),
  mazi("أَرَادَ", "arada", "«wills»", "«dilediği»", tags=["idha-shartiyya", "hollow-verbs", "form-iv-verbs"], hidden=None, extra_ar=" — فِعْلُ الشَّرْطِ، وَجَوَابُهُ مَدْلُولٌ عَلَيْهِ بِمَا قَبْلَهُ"),
  allah_fail(punct="."),
])
sen("s6", "So God willed to send to the people a messenger who would speak to them and counsel them.", "Bunun üzerine Allah insanlara, onlarla konuşacak ve onlara öğüt verecek bir elçi göndermeyi diledi.", [
  *arada_allah("فَأَرَادَ", fa=True),
  *an_yursila(),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlara»"),
  maful_("رَسُولًا", "rasul", "«a messenger»", "«bir elçi»"),
  yukallimuhum(),
  *wa_yansah("."),
])
# ---------------------------------------------------------------- §10 بَشَرٌ أَمْ مَلَكٌ (print pp. 16–17)
sen("s7", "And God willed that this messenger be a human, and that he be one of the people — whom the people know, and whose speech they understand.",
        "Allah bu elçinin bir insan olmasını, insanlardan biri olmasını diledi: insanlar onu tanısın ve sözünü anlasınlar.", [
  *arada_allah(),
  an_nasb("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِأَرَادَ", "«that»", "«… olmasını»"),
  tok("يَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«be» — kāna's muḍāriʿ, naṣb by an.", "«olmasını» — kâne'nin muzârii, en ile mansub."),
  tok("هٰذَا", "hadha", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُونَ.", "«this» — the demonstrative; the ism of yakūna.", "«bu» — ism-i işâret; yekûne'nin ismi."),
  tok("الرَّسُولُ", "rasul", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ (أَوْ عَطْفُ بَيَانٍ).", "«messenger» — a badal of the demonstrative.", "«elçi» — ism-i işâretten bedel."),
  khabar_kana("بَشَرًا", "bashar", "«a human»", "«bir insan»", punct="،", ar="خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ."),
  tok("وَأَنْ", "an-masdariyya", "part", [AT, AN], "الْوَاوُ عَاطِفَةٌ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْأَوَّلِ.", "«and that» — a second an-clause, joined to the first.", "«ve … olmasını» — ikinci en cümlesi, ilkine ma'tûf.", segments=wa_("أَنْ", "an-masdariyya", "part")),
  tok("يَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«he be» — kāna's muḍāriʿ; its ism is the concealed pronoun.", "«olmasını» — kâne'nin muzârii; ismi gizli zamir."),
  khabar_kana("وَاحِدًا", "wahid", "«one»", "«biri»", ar="خَبَرُ يَكُونَ مَنْصُوبٌ بِالْفَتْحَةِ."),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlardan»", punct="،"),
  tok("يَعْرِفُهُ", "arafa", "verb", ["mudari-marfu", MB, NA], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِوَاحِدًا.", "«whom … know» — the clause is a ṣifa of «one».", "«onu tanıdığı» — cümle «biri»nin sıfatı.", segments=[seg("يَعْرِفُ", "arafa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  nas_fail(),
  khamsa("وَيَفْهَمُونَ", "fahima", "«and understand»", "«ve anladıkları»", tags=[AT, NA], wa=True),
  noun_pron("كَلَامَهُ", "kalam", "كَلَامَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his speech» — the object, annexed to the pronoun.", "«sözünü» — mef'ûl, zamire muzâf.", tags=[MB, ID], punct="."),
])
sen("s8", "And if the messenger were an angel, the people would say: what have we to do with him?", "Elçi bir melek olsaydı insanlar derdi ki: bizim onunla ne işimiz var?", [
  *idha_kana_rasul("مَلَكًا", "malak", "«an angel»", "«bir melek»"),
  *qala_nas(":"),
  tok("مَا", "ma-istifham", "pron", [IS, MK], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«what» — the question noun; the mubtadaʾ.", "«ne» — soru ismi; mübtedâ."),
  tok("لَنَا", "li", "prep", [HJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَنَا فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«to us» — the phrase is the khabar.", "«bize» — ibare haber.", segments=[seg("لَ", "li", "prep"), seg("نَا", "pron-1p", "pron")]),
  tok("وَلَهُ", "li", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ (وَاوُ الْمَعِيَّةِ عِنْدَ بَعْضِهِمْ)، وَاللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ.", "«and to him» — joined; the idiom means «what have we to do with him?».", "«ve ona» — ma'tûf; deyim «onunla ne işimiz var?» demektir.", punct="؟", segments=[seg("وَ", "wa", "conj"), seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
])
sen("s9", "He is an angel and we are humans!", "O bir melek, biz ise insanız!", [
  pron_mubtada("هُوَ", "huwa", "«he»", "«o»"),
  khabar("مَلَكٌ", "malak", "«[is] an angel»", "«melektir»"),
  pron_mubtada("وَنَحْنُ", "nahnu", "«we»", "«biz»", wa=True),
  khabar("بَشَرٌ", "bashar", "«[are] humans»", "«insanız»", punct="!"),
])
sen("s10", "We eat and drink, and we have family and offspring; so how should we worship God?", "Biz yer içeriz, ailemiz ve zürriyetimiz vardır; o hâlde Allah'a nasıl ibadet edelim?", [
  pron_mubtada("نَحْنُ", "nahnu", "«we»", "«biz»"),
  mudari1("نَأْكُلُ", "akala", "«eat»", "«yeriz»", "نَحْنُ", tags=[MK], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  mudari1("وَنَشْرَبُ", "shariba", "«and drink»", "«ve içeriz»", "نَحْنُ", wa=True),
  *lana_ahl("وَلَنَا", "نَا", "pron-1p", "we have", "bizim … var", punct="،"),
  fa_kayfa(),
  mudari1("نَعْبُدُ", "abada", "«should we worship»", "«ibadet edelim»", "نَحْنُ"),
  allah_maful(punct="؟"),
])
sen("s11", "And if the messenger were a human, he would say: I eat and drink, I have family and offspring, and I worship God — so why do you not worship God?",
        "Elçi bir insan olunca der ki: ben yer içerim, ailem ve zürriyetim var, ve ben Allah'a ibadet ediyorum — öyleyse siz niçin Allah'a ibadet etmiyorsunuz?", [
  *idha_kana_rasul("بَشَرًا", "bashar", "«a human»", "«bir insan»"),
  qala_jawab(),
  pron_mubtada("أَنَا", "ana", "«I»", "«ben»"),
  mudari1("آكُلُ", "akala", "«eat»", "«yerim»", "أَنَا", tags=[MK], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ؛ هَمْزَةُ الْمُضَارَعَةِ وَهَمْزَةُ الْفَاءِ اجْتَمَعَتَا فَكُتِبَتَا مَدَّةً"),
  mudari1("وَأَشْرَبُ", "shariba", "«and drink»", "«ve içerim»", "أَنَا", wa=True),
  *lana_ahl("وَلِي", "ي", "pron-1s", "I have", "benim … var"),
  pron_mubtada("وَأَنَا", "ana", "«and I»", "«ve ben»", wa=True),
  mudari1("أَعْبُدُ", "abada", "«worship»", "«ibadet ederim»", "أَنَا", tags=[MK], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  allah_maful(),
  tok("فَلِمَ", "lima", "pron", [AT, IS, HJ], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَا اسْتِفْهَامِيَّةٌ فِي مَحَلِّ جَرٍّ، حُذِفَتْ أَلِفُهَا لِدُخُولِ حَرْفِ الْجَرِّ عَلَيْهَا.", "«so why» — li + the question mā, its alif dropped after the preposition (لِمَ).", "«o hâlde niçin» — li + soru mâ'sı; harf-i cerden sonra elifi düştü (لِمَ).", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("مَ", "ma-istifham", "pron")]),
  la_nafiya(),
  la_khamsa("تَعْبُدُونَ", "abada", "«do you [not] worship»", "«ibadet etmiyorsunuz»"),
  allah_maful(punct="؟"),
])
sen("s12", "And if the messenger were an angel, the people would say: you do not thirst and do not hunger; you do not fall ill and do not die — so you worship God and remember Him always!",
        "Elçi bir melek olsaydı insanlar derdi ki: sen susamazsın, acıkmazsın; hastalanmazsın, ölmezsin — bu yüzden Allah'a ibadet eder ve O'nu daima anarsın!", [
  *idha_kana_rasul("مَلَكًا", "malak", "«an angel»", "«bir melek»"),
  *qala_nas(":"),
  innaka(),
  la_nafiya(),
  la_mudari2("تَعْطَشُ", "atisha", "«thirst»", "«susamazsın»", first=True),
  la_nafiya("وَلَا", wa=True),
  la_mudari2("تَجُوعُ", "jaa-hunger", "«hunger»", "«acıkmazsın»", tags=["hollow-verbs", AT], punct="،"),
  innaka(wa=True),
  la_nafiya(),
  la_mudari2("تَمْرَضُ", "marida", "«fall ill»", "«hastalanmazsın»", first=True),
  la_nafiya("وَلَا", wa=True),
  la_mudari2("تَمُوتُ", "mata-die", "«die»", "«ölmezsin»", tags=["hollow-verbs", AT]),
  mudari1("فَتَعْبُدُ", "abada", "«so you worship»", "«bu yüzden ibadet edersin»", "أَنْتَ", fa=True),
  allah_maful(),
  tok("وَتَذْكُرُهُ", "dhakara", "verb", [AT, "mudari-marfu", MB], "الْوَاوُ عَاطِفَةٌ، وَتَذْكُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا: أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and remember Him» — the muḍāriʿ with its object pronoun.", "«ve O'nu anarsın» — mef'ûl zamirli muzâri.", segments=[seg("وَ", "wa", "conj"), seg("تَذْكُرُ", "dhakara", "verb"), seg("هُ", "pron-3ms", "pron")]),
  daiman(punct="!"),
])
sen("s13", "But we are humans: we thirst and hunger, fall ill and die — so how should we worship God and remember Him always?",
        "Biz ise insanız: susar ve acıkırız, hastalanır ve ölürüz — o hâlde Allah'a nasıl ibadet edelim ve O'nu daima analım?", [
  pron_mubtada("وَنَحْنُ", "nahnu", "«and we»", "«biz ise»", wa=True),
  khabar("بَشَرٌ", "bashar", "«[are] humans»", "«insanız»"),
  mudari1("نَعْطَشُ", "atisha", "«we thirst»", "«susarız»", "نَحْنُ", tags=[NA], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِبَشَرٌ (أَوْ حَالٌ)"),
  mudari1("وَنَجُوعُ", "jaa-hunger", "«and hunger»", "«ve acıkırız»", "نَحْنُ", wa=True, tags=["hollow-verbs"], punct="،"),
  mudari1("وَنَمْرَضُ", "marida", "«and fall ill»", "«ve hastalanırız»", "نَحْنُ", wa=True),
  mudari1("وَنَمُوتُ", "mata-die", "«and die»", "«ve ölürüz»", "نَحْنُ", wa=True, tags=["hollow-verbs"], punct="،"),
  fa_kayfa(),
  mudari1("نَعْبُدُ", "abada", "«should we worship»", "«ibadet edelim»", "نَحْنُ"),
  allah_maful(),
  mudari1_pron("وَنَذْكُرُهُ", "dhakara", "نَذْكُرُ", "نَحْنُ", "«and remember Him»", "«ve O'nu analım»", wa=True),
  daiman(punct="؟"),
])
sen("s14", "And if the messenger were a human, he would say: I am like you — I thirst and hunger, fall ill and die, and I worship God and remember Him; so why do you not worship God and not remember Him?",
        "Elçi bir insan olunca der ki: ben sizin gibiyim — susar ve acıkırım, hastalanır ve ölürüm, ve Allah'a ibadet eder, O'nu anarım; öyleyse siz niçin Allah'a ibadet etmiyor ve O'nu anmıyorsunuz?", [
  *idha_kana_rasul("بَشَرًا", "bashar", "«a human»", "«bir insan»"),
  qala_jawab(),
  pron_mubtada("أَنَا", "ana", "«I»", "«ben»"),
  noun_pron("مِثْلُكُمْ", "mithl", "مِثْلُ", "كُمْ", "pron-2mp", "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«like you» — the khabar, annexed to the pronoun.", "«sizin gibiyim» — haber, zamire muzâf.", tags=[MK, ID]),
  mudari1("أَعْطَشُ", "atisha", "«I thirst»", "«susarım»", "أَنَا", tags=[HL], extra=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ (أَوْ خَبَرٌ ثَانٍ)"),
  mudari1("وَأَجُوعُ", "jaa-hunger", "«and hunger»", "«ve acıkırım»", "أَنَا", wa=True, tags=["hollow-verbs"]),
  mudari1("وَأَمْرَضُ", "marida", "«and fall ill»", "«ve hastalanırım»", "أَنَا", wa=True),
  mudari1("وَأَمُوتُ", "mata-die", "«and die»", "«ve ölürüm»", "أَنَا", wa=True, tags=["hollow-verbs"]),
  mudari1("وَأَعْبُدُ", "abada", "«and worship»", "«ve ibadet ederim»", "أَنَا", wa=True),
  allah_maful(),
  mudari1_pron("وَأَذْكُرُهُ", "dhakara", "أَذْكُرُ", "أَنَا", "«and remember Him»", "«ve O'nu anarım»", wa=True, punct="،"),
  tok("فَلِمَاذَا", "limadha", "pron", [AT, IS, HJ], "الْفَاءُ لِلتَّفْرِيعِ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«so why» — li + mādhā, the question word in the place of jarr.", "«öyleyse niçin» — li + mâzâ, mahallen mecrur soru ismi.", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("مَاذَا", "limadha", "pron")]),
  la_nafiya(),
  la_khamsa("تَعْبُدُونَ", "abada", "«do you [not] worship»", "«ibadet etmiyorsunuz»"),
  allah_maful(),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and not»", "«ve … -mıyor»", segments=wa_("لَا", "la-nafiya", "part")),
  tok("تَذْكُرُونَهُ", "dhakara", "verb", [AT, AK, "mudari-marfu", MB, "la-nafiya"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«remember Him» — one of the five verbs; the attached pronoun is its object.", "«O'nu anmıyorsunuz» — beş fiilden; bitişik zamir mef'ûl.", punct="؟", segments=[seg("تَذْكُرُونَ", "dhakara", "verb"), seg("هُ", "pron-3ms", "pron")]),
])
sen("s15", "So the people's talk is cut short, and they find no excuse.", "Böylece insanların sözü kesilir ve bir mazeret bulamazlar.", [
  tok("فَيَنْقَطِعُ", "inqataa", "verb", [AT, "mudari-marfu", "form-vii-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَيَنْقَطِعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ — مِنْ بَابِ الِانْفِعَالِ (مُطَاوِعُ قَطَعَ).", "«so … is cut short» — a Form VII muḍāriʿ; the doer follows.", "«böylece … kesilir» — infiâl bâbından muzâri; fâil sonra gelir.", segments=[seg("فَ", "fa", "conj"), seg("يَنْقَطِعُ", "inqataa", "verb")]),
  fail("كَلَامُ", "kalam", "«the talk [of]»", "«sözü»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("النَّاسِ", "nas", "«the people»", "«insanların»"),
  la_nafiya("وَلَا", wa=True),
  la_khamsa("يَجِدُونَ", "wajada", "«they [do not] find»", "«bulamazlar»", tags=["mithal-verbs"]),
  maful_("عُذْرًا", "udhr", "«an excuse»", "«bir mazeret»", punct="."),
])

CAND = {
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend", "istemek, dilemek", 1),
 "arsala": G("arsala", "أَرْسَلَ", "ر س ل", "verb", "to send", "göndermek", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ (الْمَصْدَرِيَّة)", None, "part", "that, to (+ subjunctive)", "-mek, -mesi (muzâriyi nasbeder)", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam", 1, plural="رِجَال"),
 "kallama": G("kallama", "كَلَّمَ", "ك ل م", "verb", "to speak to", "konuşmak (biriyle), söz söylemek", 1),
 "nasaha": G("nasaha", "نَصَحَ", "ن ص ح", "verb", "to advise sincerely, to counsel", "öğüt vermek, nasihat etmek", 1),
 "wahid": G("wahid", "وَاحِد", "و ح د", "noun", "one", "bir, tek", 1),
 "khataba": G("khataba", "خَاطَبَ", "خ ط ب", "verb", "to address (Form III)", "hitap etmek (müfâale)", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every; the whole of it", "her, bütün", 1),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "anyone, one", "biri, kimse", 1),
 "faala": G("faala", "فَعَلَ", "ف ع ل", "verb", "to do", "yapmak", 1),
 "kadha": G("kadha", "كَذَا", None, "part", "such-and-such", "şöyle, falan", 1),
 "malik-king": G("malik-king", "مَلِك", "م ل ك", "noun", "king", "kral, melik", 1, plural="مُلُوك"),
 "dhahaba": G("dhahaba", "ذَهَبَ", "ذ ه ب", "verb", "to go", "gitmek", 1),
 "bashar": G("bashar", "بَشَر", "ب ش ر", "noun", "human beings, mankind", "insan, beşer", 1),
 "qadara-able": G("qadara-able", "قَدَرَ", "ق د ر", "verb", "to be able (عَلَى: to)", "güç yetirmek, muktedir olmak (alâ: -e)", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "samia": G("samia", "سَمِعَ", "س م ع", "verb", "to hear, listen", "işitmek, dinlemek", 1),
 "kalam": G("kalam", "كَلَام", "ك ل م", "noun", "speech, talk", "söz, kelâm", 1),
 "dhalika": G("dhalika", "ذَلِكَ", None, "pron", "that (masc.)", "şu, o", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except, but (exception)", "ancak, -den başka (istisnâ)", 1),
 "man": G("man", "مَنْ", None, "pron", "who, whoever — the relative and conditional noun", "kim, kimse — ism-i mevsûl ve şart ismi", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ınca", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "messenger", "elçi, resûl", 1, plural="رُسُل"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "hadha": G("hadha", "هَذَا", None, "pron", "this (masc.)", "bu", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, recognize", "tanımak, bilmek", 1),
 "fahima": G("fahima", "فَهِمَ", "ف ه م", "verb", "to understand", "anlamak", 1),
 "malak": G("malak", "مَلَك", "م ل ك", "noun", "angel", "melek", 1, plural="مَلَائِكَة"),
 "ma-istifham": G("ma-istifham", "مَا (الاِسْتِفْهَامِيَّة)", None, "pron", "what? (interrogative ma)", "ne? (soru mâ'sı)", 1),
 "huwa": G("huwa", "هُوَ", None, "pron", "he", "o", 1),
 "nahnu": G("nahnu", "نَحْنُ", None, "pron", "we (detached)", "biz (munfasıl)", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "shariba": G("shariba", "شَرِبَ", "ش ر ب", "verb", "to drink", "içmek", 1),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "people of, those belonging to", "aile, ehil", 1),
 "dhurriyya": G("dhurriyya", "ذُرِّيَّة", "ذ ر ر", "noun", "offspring, progeny", "zürriyet, soy", 1),
 "kayfa": G("kayfa", "كَيْفَ", None, "noun", "how? (an interrogative NOUN, not a letter)", "nasıl? (soru İSMİ)", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek", 1),
 "ana": G("ana", "أَنَا", None, "pron", "I (detached)", "ben (munfasıl)", 1),
 "lima": G("lima", "لِمَ", None, "pron", "why? — li + the question mā, its alif dropped (لِمَ)", "niçin? — li + soru mâ'sı; elifi düşmüş (لِمَ)", 1),
 "limadha": G("limadha", "لِمَاذَا", None, "pron", "why? (for what?)", "niçin? (ne için?)", 1),
 "atisha": G("atisha", "عَطِشَ", "ع ط ش", "verb", "to be thirsty", "susamak", 1),
 "jaa-hunger": G("jaa-hunger", "جَاعَ", "ج و ع", "verb", "to be hungry", "acıkmak", 1),
 "marida": G("marida", "مَرِضَ", "م ر ض", "verb", "to fall ill", "hastalanmak", 1),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die", "ölmek", 1),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to mention; to remember", "anmak, zikretmek", 1),
 "daiman": G("daiman", "دَائِمًا", "د و م", "noun", "always (an adverb of time)", "daima, her zaman (zaman zarfı)", 1),
 "mithl": G("mithl", "مِثْل", "م ث ل", "noun", "like, similar to", "gibi, benzer", 1),
 "inqataa": G("inqataa", "اِنْقَطَعَ", "ق ط ع", "verb", "to be cut off", "kesilmek (infiâl)", 1),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find", "bulmak", 1),
 "udhr": G("udhr", "عُذْر", "ع ذ ر", "noun", "excuse", "mazeret, özür", 1, plural="أَعْذَار"),
 "pron-2ms": G("pron-2ms", "ـكَ", None, "pron", "you / your (attached pronoun)", "sen / senin (bitişik)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you (pl.) / your (attached)", "siz / sizin (bitişik)", 1),
 "pron-1p": G("pron-1p", "ـنَا", None, "pron", "us / our (attached)", "biz / bizim (bitişik)", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "my (attached pronoun)", "benim (bitişik)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to, towards", "-e, -e doğru", 1),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon; against", "üzerine, -e", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not (simple negation)", "değil, -mez (nefiy lâ'sı)", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "nas": G("nas", "النَّاس", "ن و س", "noun", "the people", "insanlar", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "fa": G("fa", "فَـ", None, "part", "so, for, then", "bunun üzerine, böylece", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — the emphasizing particle", "şüphesiz — tekid harfi", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
_missing = [k for k, v in GLOSS_ADD.items() if v.get("pos") == "verb" and k not in mo["verbs"]]
assert not _missing, f"verbs without a paradigm: {_missing}"
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch5 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 5 (print pp. 15–17; Nūḥ §9–10): the messenger — God wills to send the people a man from among them who speaks to them and counsels them; God does not address each person one by one, nor do kings; kings are humans whom everyone can see and hear, but no one sees God or hears Him except whom He wills (s1–s6). "
          "A human or an angel? — the messenger must be one of the people: were he an angel they would say «what have we to do with him? he is an angel and we are humans; we eat and drink and have families — how should we worship?», and when he is a man he answers «I eat and drink and have a family, and I worship God — so why do you not?»; were he an angel: «you neither thirst nor hunger, neither sicken nor die, so you worship always», and the man answers «I am like you», and their talk is cut short (s7–s15). One printed line is one sentence.")
ADD_TR = (" Beşinci bölüm (basılı s. 15–17; Nûh §9–10): elçi — Allah insanlara, kendilerinden, onlarla konuşup öğüt verecek bir adam göndermeyi diler; Allah herkese tek tek hitap etmez, krallar da etmez; krallar herkesin görüp işitebildiği insanlardır, Allah'ı ise ancak O'nun dilediği görür ve işitir (s1–s6). "
          "İnsan mı, melek mi? — elçi insanlardan biri olmalıdır: melek olsaydı «bizim onunla ne işimiz var? o melek, biz insanız; biz yer içeriz, ailemiz var — nasıl ibadet edelim?» derlerdi; insan olunca «ben de yer içerim, ailem var ve Allah'a ibadet ediyorum — siz niçin etmiyorsunuz?» der; melek olsaydı «sen ne susar ne acıkırsın, ne hastalanır ne ölürsün, o yüzden hep ibadet edersin» derlerdi; insan olunca «ben sizin gibiyim» der ve sözleri kesilir (s7–s15). Basılı her satır bir cümledir.")
write_out(5, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §9–10, pp. 15–17", GLOSS_ADD, notes=(), related=())
report(5, S, GLOSS_ADD, ())
