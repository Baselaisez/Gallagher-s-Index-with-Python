# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 45: «قِصَّةُ عِيسَى» §42 (from an obscure creed to open idolatry — Europe, the Greeks and the Romans, Constantine; the author's footnote; the straying road; al-Fātiḥa 1:6–7; the tragedy of Europe; «to God belongs the command before and after»). Print pp. 68–70 — the END of the book's text.
python3 tools/authoring/author_qisas4_ch45.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: فِكْرَةُ الشَّيْطَانِ — حِيلَةُ الشَّيْطَانِ", "en": "The ship of Nūḥ: Satan's idea — Satan's trick", "tr": "Nûh'un gemisi: Şeytan'ın fikri — Şeytan'ın hilesi"}
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
def shaytan_fail(punct=None): return fail("الشَّيْطَانُ", "shaytan", "«Satan»", "«Şeytan»", punct=punct)
def an_(role_ar, en="«to»", tr="«-mesini»"):
    return tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — " + role_ar + ".", en + " — the masdar-making an.", tr + " — masdar en'i.")
def wa_group_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), ar_body=None):
    """وَيَعْبُدُونَهُ: a joined muḍāriʿ of the five with its object pronoun."""
    return tok(full, lex, "verb", [AT, AK, "mudari-marfu", MB] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ." if ar_body is None else ar_body, "«and» + " + en + " — a muḍāriʿ of the five; the attached pronoun is its object.", "«ve» + " + tr + " — beş fiilden muzâri; bitişik zamir mef'ûl.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")])
def group_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "verb", [AK, "mudari-marfu", MB] + list(tags), stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", en + " — a muḍāriʿ of the five; the attached pronoun is its object.", tr + " — beş fiilden muzâri; bitişik zamir mef'ûl.", punct=punct, segments=[seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")])
def abadan(punct="."): return tok("أَبَدًا", "abadan", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«ever» — a time adverbial.", "«asla» — zaman zarfı.", punct=punct)
def yadkhulu_pl(full, pre_ar, pre_en, pre_tr, punct=None, tags=(), first_seg=None):
    segs = ([first_seg] if first_seg else []) + [seg("يَدْخُلُ", "dakhala", "verb"), seg("وا", "pron-3mp", "pron")]
    return tok(full, "dakhala", "verb", [AK] + list(tags), pre_ar + "يَدْخُلُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", pre_en + "«they enter» — naṣb by the dropped nūn; the wāw is the doer.", pre_tr + "«girerler» — nûnun düşmesiyle mansub; vâv fâil.", punct=punct, segments=segs)
def idha(full="إِذَا", wa=False, punct=None):
    return tok(full, "idha", "part", ["idha-shartiyya"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", ("«and» + " if wa else "") + "«when» — the conditional time-adverb, built.", ("«ve» + " if wa else "") + "«-dığı zaman» — şart mânâlı zaman zarfı, mebnî.", punct=punct, segments=(wa_("إِذَا", "idha", "part") if wa else None))

# ---------------------------------------------------------------- §3 فِكْرَةُ الشَّيْطَانِ (print pp. 9–10)
sen("s1", "And Satan saw fit to call the people to the worship of idols, so that they enter the Fire and never enter Paradise.",
        "Şeytan, insanları putlara tapmaya çağırmayı uygun gördü; böylece ateşe girsinler ve cennete asla girmesinler.", [
  mazi("وَرَأَى", "raa", "«and saw [fit]»", "«ve uygun gördü»", tags=["naqis-verbs", AT], hidden=None, wa=True),
  shaytan_fail(),
  an_("وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِرَأَى: رَأَى دَعْوَةَ النَّاسِ"),
  tok("يَدْعُوَ", "daa", "verb", [AN, "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْوَاوِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "«call» — naṣb by an; the fatḥa shows on the wāw of the defective verb.", "«çağırmak» — en ile mansub; nâkıs fiilin vâvında fetha görünür."),
  maful_("النَّاسَ", "nas", "«the people»", "«insanları»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("عِبَادَةِ", "ibada", "«the worship [of]»", "«ibadetine»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("الْأَصْنَامِ", "sanam", "noun", [ID, JT], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ صَنَمٍ.", "«the idols» — the mudaf ilayh; a broken plural.", "«putların» — muzâfun ileyh; cem-i mükesser."),
  yadkhulu_pl("فَيَدْخُلُوا", "الْفَاءُ لِلسَّبَبِيَّةِ (أَوْ عَاطِفَةٌ عَلَى يَدْعُوَ)، وَ", "«so that» + ", "«böylece» + ", first_seg=seg("فَ", "fa", "conj")),
  maful_("النَّارَ", "nar", "«the Fire»", "«ateşe»"),
  la_nafiya("وَلَا", wa=True),
  yadkhulu_pl("يَدْخُلُوا", "مَعْطُوفٌ عَلَى يَدْخُلُوا الْأُولَى: ", "", "", tags=[AT, "la-nafiya"]),
  maful_("الْجَنَّةَ", "janna", "«Paradise»", "«cennete»"),
  abadan("."),
])
sen("s2", "And Satan knew that God does not forgive associating partners with Him, and forgives everything else if He wills.",
        "Şeytan biliyordu ki Allah şirki bağışlamaz; dilerse her şeyi bağışlar.", [
  kana(),
  ism_kana("الشَّيْطَانُ", "shaytan", "«Satan»", "«Şeytan»"),
  mudari("يَعْرِفُ", "arafa", "«knew»", "«biliyordu»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  anna(obj_of="يَعْرِفُ"),
  allah_ism(part="أَنَّ"),
  la_nafiya(),
  mudari("يَغْفِرُ", "ghafara", "«forgives»", "«bağışlamaz»", tags=["la-nafiya", IW], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ"),
  maful_("الشِّرْكَ", "shirk", "«associating partners»", "«şirki»", punct="،"),
  mudari_wa("وَيَغْفِرُ", "ghafara", "«and forgives»", "«ve bağışlar»"),
  maful_("كُلَّ", "kull", "«every[thing]»", "«her»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeyi»"),
  idha(),
  mazi("أَرَادَ", "arada", "«He wills»", "«dilerse»", tags=["idha-shartiyya", "hollow-verbs", "form-iv-verbs"], punct="."),
])
sen("s3", "So Satan wanted to call them to shirk, so that they never enter Paradise.",
        "Bunun üzerine Şeytan onları şirke çağırmak istedi; böylece cennete asla girmesinler.", [
  mazi("فَأَرَادَ", "arada", "«so wanted»", "«bunun üzerine istedi»", tags=["hollow-verbs", "form-iv-verbs", AT], hidden=None, wa=True),
  shaytan_fail(),
  an_("وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِأَرَادَ"),
  tok("يَدْعُوَهُمْ", "daa", "verb", [AN, "naqis-verbs", MB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«call them» — naṣb by an; the pronoun is its object.", "«onları çağırmak» — en ile mansub; zamir mef'ûl.", segments=[seg("يَدْعُوَ", "daa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("الشِّرْكِ", "shirk", "«shirk»", "«şirke»", punct="."),
  fa_la(),
  yadkhulu_pl("يَدْخُلُوا", "مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ فَاءِ السَّبَبِيَّةِ: ", "", "", tags=[AN, "la-nafiya"]),
  maful_("الْجَنَّةَ", "janna", "«Paradise»", "«cennete»"),
  abadan("."),
])
sen("s4", "But what is the way to that, while the people worship God?",
        "Fakat insanlar Allah'a ibadet ederken buna giden yol nedir?", [
  tok("وَلٰكِنْ", "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin.", "«fakat» — muhaffef lâkin.", segments=wa_("لٰكِنْ", "lakin", "part")),
  tok("كَيْفَ", "kayfa", "noun", [IS, MK], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.", "«how» — the interrogative, built; the fronted khabar.", "«nasıl» — istifham ismi, mebnî; mukaddem haber."),
  tok("الطَّرِيقُ", "tariq", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the way» — the delayed mubtada.", "«yol» — muahhar mübtedâ."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«that» — the demonstrative, built; in the place of jarr.", "«buna» — ism-i işâret, mahallen mecrur.", punct="،"),
  tok("وَالنَّاسُ", "nas", "noun", [MK, HL], "الْوَاوُ لِلْحَالِ، وَالنَّاسُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«while the people» — the wāw of the ḥāl; a mubtada opening the ḥāl clause.", "«insanlar … iken» — hâl vâvı; hâl cümlesini açan mübtedâ.", segments=wa_("النَّاسُ", "nas", "noun")),
  khamsa("يَعْبُدُونَ", "abada", "«worship»", "«ibadet ederler»", tags=[MK], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ"),
  allah_maful(punct="؟"),
])
sen("s5", "Had he gone to the people and said to them «worship the idols and do not worship God», the people would have reviled him and beaten him.",
        "İnsanlara gidip onlara «putlara tapın, Allah'a ibadet etmeyin» deseydi, insanlar ona söver ve onu döverlerdi.", [
  tok("إِنَّهُ", "inna", "part", [IW], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ (أَوْ عَائِدٌ عَلَى الشَّيْطَانِ) فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«indeed» — inna + its ism, the pronoun (of the matter, or Satan).", "«şüphesiz» — inne + ismi olan zamir (şe'n zamiri veya Şeytan).", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("لَوْ", "law", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ.", "«had …» — law, the non-jussive conditional.", "«… olsaydı» — lev, cezmetmeyen şart edatı."),
  mazi("ذَهَبَ", "dhahaba", "«he went»", "«gitseydi»", tags=["in-shartiyya"]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlara»"),
  qala("وَقَالَ", wa=True, punct=None),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»", punct=":"),
  tok("اعْبُدُوا", "abada", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "«worship!» — the imperative on the dropped nūn; the wāw is the doer.", "«tapın!» — nûnun düşmesi üzere mebnî emir; vâv fâil.", segments=[seg("اعْبُدُ", "abada", "verb"), seg("وا", "pron-3mp", "pron")]),
  maful_("الْأَصْنَامَ", "sanam", "«the idols»", "«putlara»", tags=[JT]),
  tok("وَلَا", "la-nahiya", "part", ["la-nahiya", AT], "الْوَاوُ عَاطِفَةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "«and do not» — the prohibiting lā, which jazms.", "«ve -meyin» — cezmeden nehiy lâ'sı.", segments=wa_("لَا", "la-nahiya", "part")),
  tok("تَعْبُدُوا", "abada", "verb", ["la-nahiya", AK], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«worship» — jussive after the prohibiting lā, its nūn dropped.", "«ibadet edin» — nehiy lâ'sıyla meczum, nûnu düşmüş.", segments=[seg("تَعْبُدُ", "abada", "verb"), seg("وا", "pron-3mp", "pron")]),
  allah_maful(),
  tok("لَشَتَمَهُ", "shatama", "verb", ["in-shartiyya", MB], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَشَتَمَ فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«[they] would have reviled him» — the lām of law's answer + the māḍī; the pronoun is its object.", "«ona söverlerdi» — lev'in cevabının lâmı + mâzî; zamir mef'ûl.", segments=[seg("لَ", "la-jawab-law", "part"), seg("شَتَمَ", "shatama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  nas_fail(),
  v_pl_pron("وَضَرَبُوهُ", "daraba", "ضَرَبُو", "هُ", "pron-3ms", "«and beaten him»", "«ve onu döverlerdi»", wa=True, punct="."),
])
sen("s6", "They would have said: «God forbid! Shall we associate partners with our Lord? Shall we worship the idols?»",
        "Derlerdi ki: «Allah korusun! Rabbimize ortak mı koşalım? Putlara mı tapalım?»", [
  qalu(),
  tok("مَعَاذَ", "maadh", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (أَعُوذُ) مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«[I seek] the refuge [of]» — the mafʿūl muṭlaq of a deleted aʿūdhu, annexed.", "«sığınırım» — mahzuf eûzü'nün mef'ûl-i mutlakı, muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah» — muzâfun ileyh.", punct="،"),
  tok("أَنُشْرِكُ", "ashraka", "verb", [IS, "mudari-marfu", "form-iv-verbs"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَنُشْرِكُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: نَحْنُ.", "«shall we associate?» — the denying question's hamza + the muḍāriʿ; the doer is «we», concealed.", "«ortak mı koşalım?» — inkârî istifham hemzesi + muzâri; fâil gizli «biz».", segments=[seg("أَ", "a-istifham", "part"), seg("نُشْرِكُ", "ashraka", "verb")]),
  tok("بِرَبِّنَا", "rabb", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَرَبِّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«with our Lord» — bi + rabb annexed to «our».", "«Rabbimize» — bi + «biz»e muzâf rabb.", punct="؟", segments=[seg("بِ", "bi", "prep"), seg("رَبِّ", "rabb", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("أَنَعْبُدُ", "abada", "verb", [IS, "mudari-marfu"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَنَعْبُدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: نَحْنُ.", "«shall we worship?» — the denying question's hamza + the muḍāriʿ.", "«tapalım mı?» — inkârî istifham hemzesi + muzâri.", segments=[seg("أَ", "a-istifham", "part"), seg("نَعْبُدُ", "abada", "verb")]),
  maful_("الْأَصْنَامَ", "sanam", "«the idols»", "«putlara»", tags=[JT], punct="؟"),
])
sen("s7", "«You are an accursed devil! You are a wicked devil!»",
        "«Sen kovulmuş bir şeytansın! Sen habis bir şeytansın!»", [
  tok("إِنَّكَ", "inna", "part", [IW], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«indeed you» — inna + its ism, the pronoun «you».", "«şüphesiz sen» — inne + ismi olan «sen» zamiri.", segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَشَيْطَانٌ", "shaytan", "noun", [IW], "اللَّامُ لَامُ الِابْتِدَاءِ (الْمُزَحْلَقَةُ)، وَشَيْطَانٌ خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«[are] a devil» — the slid lām of emphasis + inna's khabar.", "«bir şeytansın» — müzahlaka lâm + inne'nin haberi.", segments=[seg("لَ", "la-ibtida", "part"), seg("شَيْطَانٌ", "shaytan", "noun")]),
  naat("رَجِيمٌ", "rajim", "«accursed»", "«kovulmuş»", case="raf", punct="!", tags=["sifa-mushabbaha"]),
  tok("إِنَّكَ", "inna", "part", [IW], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«indeed you» — inna + its ism.", "«şüphesiz sen» — inne + ismi.", segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("لَشَيْطَانٌ", "shaytan", "noun", [IW], "اللَّامُ الْمُزَحْلَقَةُ، وَشَيْطَانٌ خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«[are] a devil» — the slid lām + inna's khabar.", "«bir şeytansın» — müzahlaka lâm + inne'nin haberi.", segments=[seg("لَ", "la-ibtida", "part"), seg("شَيْطَانٌ", "shaytan", "noun")]),
  naat("خَبِيثٌ", "khabith", "«wicked»", "«habis»", case="raf", punct="!", tags=["sifa-mushabbaha"]),
])
# ---------------------------------------------------------------- §4 حِيلَةُ الشَّيْطَانِ (print pp. 10–11)
sen("s8", "But Satan found a door by which to enter the heads of the people.",
        "Fakat Şeytan, insanların kafalarına girebileceği bir kapı buldu.", [
  tok("وَلٰكِنَّ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلِاسْتِدْرَاكِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.", "«but» — lākinna, a sister of inna: it puts its ism in naṣb and its khabar in rafʿ.", "«fakat» — inne'nin kız kardeşi lâkinne: ismini nasb, haberini ref eder.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  ism_inna("الشَّيْطَانَ", "shaytan", "«Satan»", "«Şeytan»", part="لٰكِنَّ"),
  mazi("وَجَدَ", "wajada", "«found»", "«buldu»", tags=[IW], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  maful_("بَابًا", "bab", "«a door»", "«bir kapı»"),
  mudari("يَدْخُلُ", "dakhala", "«[by which] he enters»", "«girer»", tags=["jumla-sifa"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِبَابًا"),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«by it»", "«ondan»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("رُؤُوسِ", "ras", "«the heads [of]»", "«kafalarına»", tags=[ID, JT], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — جَمْعُ رَأْسٍ."),
  mudaf_ilayh("النَّاسِ", "nas", "«the people»", "«insanların»", punct="."),
])
sen("s9", "There were men who feared God, worshipped Him night and day, and remembered Him much.",
        "Allah'tan korkan, O'na gece gündüz ibadet eden ve O'nu çokça zikreden adamlar vardı.", [
  kana("كَانَ", wa=False),
  ism_kana("رِجَالٌ", "rajul", "«men»", "«adamlar»", tags=[JT]),
  khamsa("يَخَافُونَ", "khafa", "«feared»", "«korkarlardı»", tags=[KN, "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  allah_maful(punct="،"),
  wa_group_pron("وَيَعْبُدُونَهُ", "abada", "يَعْبُدُونَ", "هُ", "pron-3ms", "«worshipped Him»", "«O'na ibadet ederlerdi»"),
  tok("لَيْلًا", "layl", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«by night» — a time adverbial.", "«gece» — zaman zarfı."),
  tok("وَنَهَارًا", "nahar", "noun", [AT, MF], "الْوَاوُ عَاطِفَةٌ، وَنَهَارًا ظَرْفُ زَمَانٍ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and by day» — a second time adverbial, joined.", "«ve gündüz» — ma'tûf zaman zarfı.", punct="،", segments=wa_("نَهَارًا", "nahar", "noun")),
  wa_group_pron("وَيَذْكُرُونَهُ", "dhakara", "يَذْكُرُونَ", "هُ", "pron-3ms", "«remembered Him»", "«O'nu zikrederlerdi»"),
  tok("ذِكْرًا", "dhikr", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a remembrance» — the mafʿūl muṭlaq.", "«bir zikirle» — mef'ûl-i mutlak."),
  naat("كَثِيرًا", "kathir", "«much»", "«çokça»", case="nasb", punct="."),
])
sen("s10", "They loved God, and God loved them and answered them; the people loved and honoured them; and Satan knew that well.",
        "Allah'ı severlerdi; Allah da onları sever ve dualarına karşılık verirdi; insanlar onları sever ve yüceltirdi; Şeytan bunu iyi biliyordu.", [
  kana_pl(),
  khamsa("يُحِبُّونَ", "ahabba", "«loved»", "«severlerdi»", tags=[KN, "doubled-verbs", "form-iv-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  allah_maful(punct="،"),
  kana(),
  tok("اللهُ", "allah", "propn", [KN], "لَفْظُ الْجَلَالَةِ اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«God» — kāna's ism.", "«Allah» — kâne'nin ismi."),
  tok("يُحِبُّهُمْ", "ahabba", "verb", [KN, MB, "doubled-verbs", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«loved them» — the muḍāriʿ with its object pronoun; the clause is kāna's khabar.", "«onları severdi» — mef'ûl zamirli muzâri; cümle kâne'nin haberi.", segments=[seg("يُحِبُّ", "ahabba", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  mudari_wa("وَيَسْتَجِيبُ", "istajaba", "«and answered»", "«ve karşılık verirdi»", tags=["form-x-verbs", "hollow-verbs"]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»"),
  kana(),
  ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»"),
  group_pron("يُحِبُّونَهُمْ", "ahabba", "يُحِبُّونَ", "هُمْ", "pron-3mp", "«loved them»", "«onları severdi»", tags=[KN, "doubled-verbs", "form-iv-verbs"]),
  wa_group_pron("وَيُعَظِّمُونَهُمْ", "azzama", "يُعَظِّمُونَ", "هُمْ", "pron-3mp", "«honoured them»", "«onları yüceltirdi»", tags=["form-ii-verbs"], punct="،"),
  kana(),
  ism_kana("الشَّيْطَانُ", "shaytan", "«Satan»", "«Şeytan»"),
  mudari("يَعْرِفُ", "arafa", "«knew»", "«biliyordu»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", MB], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«that» — the demonstrative, built; the object.", "«bunu» — ism-i işâret, mahallen mef'ûl."),
  tok("جَيِّدًا", "jayyid", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ (صِفَتُهُ) مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: مَعْرِفَةً جَيِّدَةً.", "«well» — the adjective standing for the mafʿūl muṭlaq («a good knowing»).", "«iyi» — mef'ûl-i mutlak yerine sıfatı («iyi bir bilme»).", punct="."),
])
sen("s11", "And these had died and passed on to the mercy of God!",
        "Bunlar ölmüş ve Allah'ın rahmetine kavuşmuşlardı!", [
  tok("وَقَدْ", "qad", "part", ["qad-harf", AT], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — the wāw opens the sentence; qad affirms the past.", "«ve gerçekten» — vâv cümleyi açar; kad tahkik harfi.", segments=wa_("قَدْ", "qad", "part")),
  mazi("مَاتَ", "mata-die", "«had died»", "«ölmüştü»", tags=["hollow-verbs", "qad-harf"], hidden=None),
  tok("هٰؤُلَاءِ", "haulai", "pron", ["asma-al-ishara", FL], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«these» — the demonstrative, built; the doer.", "«bunlar» — ism-i işâret, mahallen fâil."),
  mazi_pl("وَانْتَقَلُوا", "intaqala", "«and passed on»", "«ve göçmüşlerdi»", tags=["form-viii-verbs", AT], wa=True),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("رَحْمَةِ", "rahma", "«the mercy [of]»", "«rahmetine»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah'ın» — muzâfun ileyh.", punct="!"),
])
sen("s12", "Satan went to the people and mentioned those men.",
        "Şeytan insanlara gitti ve o adamları andı.", [
  mazi("ذَهَبَ", "dhahaba", "«went»", "«gitti»", hidden=None),
  shaytan_fail(),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlara»"),
  mazi("وَذَكَرَ", "dhakara", "«and mentioned»", "«ve andı»", tags=[AT], wa=True),
  tok("هٰؤُلَاءِ", "haulai", "pron", ["asma-al-ishara", MB], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«those» — the demonstrative, built; the object.", "«o» — ism-i işâret, mahallen mef'ûl."),
  tok("الرِّجَالَ", "rajul", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ رَجُلٍ.", "«men» — the substitute of the demonstrative, in naṣb.", "«adamları» — ism-i işâretin bedeli, mansub.", punct="."),
])
sen("s13", "And he said: «How was so-and-so among you, and so-and-so, and so-and-so?»",
        "Ve dedi ki: «Aranızda falan, falan ve falan nasıldı?»", [
  qala("وَقَالَ", wa=True),
  tok("كَيْفَ", "kayfa", "noun", [IS, KN], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«how» — the interrogative, built; kāna's fronted khabar.", "«nasıl» — istifham ismi; kâne'nin mukaddem haberi."),
  kana("كَانَ", wa=False),
  prep_pron("فِيكُمْ", "fi", "كُمْ", "pron-2mp", "«among you»", "«aranızda»"),
  ism_kana("فُلَانٌ", "fulan", "«so-and-so»", "«falan»", ar="اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ."),
  atf("وَفُلَانٌ", "fulan", "«so-and-so»", "«falan»", case="raf"),
  atf("وَفُلَانٌ", "fulan", "«so-and-so»", "«falan»", case="raf", punct="؟"),
])
sen("s14", "They said: «Glory be to God! The men of God and His friends! Those — when they prayed He answered them, and when they asked He gave them.»",
        "Dediler ki: «Sübhânallah! Allah'ın adamları ve O'nun dostları! Onlar dua ettiklerinde O karşılık verir, istediklerinde verirdi.»", [
  qalu(),
  tok("سُبْحَانَ", "subhan", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«glory [be to]» — the mafʿūl muṭlaq of a deleted verb, annexed.", "«tesbih» — mahzuf fiilin mef'ûl-i mutlakı, muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah» — muzâfun ileyh.", punct="!"),
  tok("رِجَالُ", "rajul", "noun", [MK, ID, JT, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هُمْ، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«[they are] the men [of]» — the khabar of an understood «they», annexed.", "«[onlar] … adamları» — mahzuf «onlar»ın haberi, muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah'ın» — muzâfun ileyh."),
  tok("وَأَوْلِيَاؤُهُ", "wali", "noun", [AT, ID, JT], "الْوَاوُ عَاطِفَةٌ، وَأَوْلِيَاءُ مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ وَلِيٍّ؛ كُتِبَتِ الْهَمْزَةُ عَلَى وَاوٍ لِلضَّمَّةِ.", "«and His friends» — joined, annexed to «His»; the hamza sits on a wāw for the ḍamma.", "«ve O'nun dostları» — ma'tûf, «O»na muzâf; hemze damme için vâv üzerinde.", punct="!", segments=[seg("وَ", "wa", "conj"), seg("أَوْلِيَاؤُ", "wali", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("أُولٰئِكَ", "ulaika", "pron", ["asma-al-ishara", MK], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«those» — the demonstrative, built; the mubtada.", "«onlar» — ism-i işâret, mahallen mübtedâ."),
  idha(),
  tok("دَعَوْا", "daa", "verb", ["idha-shartiyya", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ.", "«they prayed» — the defective māḍī before the group's wāw (daʿā → daʿaw).", "«dua ettiler» — cemaat vâvından önce nâkıs mâzî (deâ → deav).", segments=[seg("دَعَ", "daa", "verb"), seg("وْا", "pron-3mp", "pron")]),
  tok("أَجَابَهُمْ", "ajaba", "verb", [MB, "hollow-verbs", "form-iv-verbs", "idha-shartiyya"], "فِعْلٌ مَاضٍ — جَوَابُ إِذَا، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ (اللهُ)، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ أُولٰئِكَ.", "«He answered them» — the answer of idhā; the doer is He (God), concealed; the clause is the khabar.", "«onlara karşılık verdi» — izâ'nın cevabı; fâil gizli O (Allah); cümle haber.", punct="،", segments=[seg("أَجَابَ", "ajaba", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  idha("وَإِذَا", wa=True),
  mazi_pl("سَأَلُوا", "saala", "«they asked»", "«istediler»", tags=["idha-shartiyya"]),
  tok("أَعْطَاهُمْ", "aata", "verb", [MB, "naqis-verbs", "form-iv-verbs", "idha-shartiyya", MX], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — جَوَابُ إِذَا، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ أَوَّلُ (وَالثَّانِي مَحْذُوفٌ).", "«He gave them» — the answer of idhā; the pronoun is the first object, the second understood.", "«onlara verdi» — izâ'nın cevabı; zamir birinci mef'ûl, ikincisi mahzuf.", punct=".", segments=[seg("أَعْطَا", "aata", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
])

CAND = {
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see; to see fit", "görmek; uygun görmek", 1),
 "shaytan": G("shaytan", "شَيْطَان", "ش ط ن", "noun", "devil, Satan", "şeytan", 1, plural="شَيَاطِين"),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the masdar-making an", "-mesi — masdar en'i", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call; to pray", "çağırmak; dua etmek", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e, -ye", 1),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet", 1),
 "sanam": G("sanam", "صَنَم", "ص ن م", "noun", "idol", "put", 1, plural="أَصْنَام"),
 "fa": G("fa", "فَ", None, "conj", "so, then", "bunun üzerine", 1),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "nar": G("nar", "نَار", "ن و ر", "noun", "fire; the Fire (Hell)", "ateş; cehennem", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not — the negating lā", "değil, -mez — nefiy lâ'sı", 1),
 "janna": G("janna", "جَنَّة", "ج ن ن", "noun", "garden; Paradise", "bahçe; cennet", 1, plural="جَنَّات"),
 "abadan": G("abadan", "أَبَدًا", "أ ب د", "noun", "ever, never (with a negation)", "asla, ebediyen", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, to recognize", "bilmek, tanımak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (after a verb of knowing or saying)", "ki (bilme ve söyleme fiillerinden sonra)", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "ghafara": G("ghafara", "غَفَرَ", "غ ف ر", "verb", "to forgive", "bağışlamak", 1),
 "shirk": G("shirk", "شِرْك", "ش ر ك", "noun", "associating partners with God; polytheism", "şirk", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, bütün", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ınca", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to will (Form IV)", "istemek, dilemek (if'âl)", 1),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but (the lightened lākin)", "fakat (muhaffef lâkin)", 1),
 "kayfa": G("kayfa", "كَيْفَ", None, "noun", "how", "nasıl", 1),
 "tariq": G("tariq", "طَرِيق", "ط ر ق", "noun", "way, road", "yol", 1, plural="طُرُق"),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that (masculine)", "o, şu (müzekker)", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek, tapmak", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — the emphasizing particle", "şüphesiz — tekid harfi", 1),
 "law": G("law", "لَوْ", None, "part", "if (contrary to fact: «had it been so»)", "eğer (olmayana bağlı şart: «olsaydı»)", 1),
 "dhahaba": G("dhahaba", "ذَهَبَ", "ذ ه ب", "verb", "to go", "gitmek", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "la-nahiya": G("la-nahiya", "لَا (النَّاهِيَة)", None, "part", "do not — the prohibiting lā", "-me, -meyin — nehiy lâ'sı", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "shatama": G("shatama", "شَتَمَ", "ش ت م", "verb", "to revile, to insult", "sövmek", 1),
 "la-jawab-law": G("la-jawab-law", "لَ (فِي جَوَابِ لَوْ)", None, "part", "the lām that opens the answer of law", "lev'in cevabına giren lâm", 1),
 "daraba": G("daraba", "ضَرَبَ", "ض ر ب", "verb", "to strike, to beat", "vurmak, dövmek", 1),
 "maadh": G("maadh", "مَعَاذ", "ع و ذ", "noun", "refuge (مَعَاذَ اللهِ: God forbid)", "sığınak (meâzallah: Allah korusun)", 1),
 "a-istifham": G("a-istifham", "أَ", None, "part", "the interrogative hamza («…?»)", "istifham hemzesi («… mi?»)", 1),
 "ashraka": G("ashraka", "أَشْرَكَ", "ش ر ك", "verb", "to associate (a partner with God) (Form IV)", "ortak koşmak, şirk koşmak (if'âl)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "la-ibtida": G("la-ibtida", "لَ", None, "part", "the lām of emphasis (lām al-ibtidāʾ)", "tekid lâmı (lâm-ı ibtidâ)", 1),
 "rajim": G("rajim", "رَجِيم", "ر ج م", "noun", "accursed, stoned (of Satan)", "kovulmuş, taşlanmış (şeytan için)", 1),
 "khabith": G("khabith", "خَبِيث", "خ ب ث", "noun", "wicked, foul", "habis, kötü", 1),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but (a sister of inna)", "fakat (inne'nin kız kardeşi)", 1),
 "wajada": G("wajada", "وَجَدَ", "و ج د", "verb", "to find", "bulmak", 1),
 "bab": G("bab", "بَاب", "ب و ب", "noun", "door, gate", "kapı", 1, plural="أَبْوَاب"),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "ras": G("ras", "رَأْس", "ر أ س", "noun", "head", "baş, kafa", 1, plural="رُؤُوس"),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam, erkek", 1, plural="رِجَال"),
 "khafa": G("khafa", "خَافَ", "خ و ف", "verb", "to fear", "korkmak", 1),
 "layl": G("layl", "لَيْل", "ل ي ل", "noun", "night", "gece", 1),
 "nahar": G("nahar", "نَهَار", "ن ه ر", "noun", "daytime, day", "gündüz", 1),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to mention, to remember", "anmak, zikretmek", 1),
 "dhikr": G("dhikr", "ذِكْر", "ذ ك ر", "noun", "remembrance, mention", "zikir, anma", 1),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "ahabba": G("ahabba", "أَحَبَّ", "ح ب ب", "verb", "to love (Form IV, doubled)", "sevmek (if'âl, muzâaf)", 1),
 "istajaba": G("istajaba", "اِسْتَجَابَ", "ج و ب", "verb", "to answer, to respond (to: لِ) (Form X)", "karşılık vermek, kabul etmek (li: -e) (istif'âl)", 1),
 "azzama": G("azzama", "عَظَّمَ", "ع ظ م", "verb", "to honour, to magnify (Form II)", "yüceltmek, tazim etmek (tef'îl)", 1),
 "jayyid": G("jayyid", "جَيِّد", "ج و د", "noun", "good, well", "iyi, güzel", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already (before a māḍī)", "gerçekten (mâzîden önce)", 1),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die", "ölmek", 1),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these", "bunlar", 1),
 "intaqala": G("intaqala", "انْتَقَلَ", "ن ق ل", "verb", "to move on, to be transferred (Form VIII)", "geçmek, intikal etmek (iftiâl)", 1),
 "rahma": G("rahma", "رَحْمَة", "ر ح م", "noun", "mercy", "rahmet", 1),
 "fulan": G("fulan", "فُلَان", None, "noun", "so-and-so", "falan", 1),
 "subhan": G("subhan", "سُبْحَان", "س ب ح", "noun", "glory (be to …) — the masdar of praise", "tesbih, (… münezzehtir)", 1),
 "wali": G("wali", "وَلِيّ", "و ل ي", "noun", "friend, ally (of God)", "dost, veli", 1, plural="أَوْلِيَاء"),
 "ulaika": G("ulaika", "أُولَئِكَ", None, "pron", "those", "onlar, şunlar", 1),
 "ajaba": G("ajaba", "أَجَابَ", "ج و ب", "verb", "to answer (Form IV, hollow)", "cevap vermek, karşılık vermek (if'âl, ecvef)", 1),
 "saala": G("saala", "سَأَلَ", "س أ ل", "verb", "to ask", "sormak, istemek", 1),
 "aata": G("aata", "أَعْطَى", "ع ط و", "verb", "to give (Form IV, defective)", "vermek (if'âl, nâkıs)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (masculine plural, attached)", "siz / sizin (bitişik)", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masculine singular, attached)", "sen / senin (bitişik)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us / our", "biz", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "shatama", _sg.sound1("daraba", "شَتَم", "شْتِم", "اِشْتِم", "شَتْم", "شَاتِم", "مَشْتُوم", "شُتِمَ", "يُشْتَمُ", "شَتَمَهُ يَشْتِمُهُ: سَبَّهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch2 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 2 (print pp. 9–11; Nūḥ §3–4): Satan's idea — to call the people to idols so that they enter the Fire; God forgives all but shirk; but how, while the people worship God? openly he would be reviled and beaten (s1–s7); "
          "Satan's trick — a door into the people's heads: the God-fearing men who had died, whom the people loved; «how was so-and-so among you?» — «the men of God and His friends!» (s8–s14). One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" İkinci bölüm (basılı s. 9–11; Nûh §3–4): Şeytan'ın fikri — insanları putlara çağırmak ki ateşe girsinler; Allah şirk dışında her şeyi bağışlar; fakat insanlar Allah'a ibadet ederken nasıl? açıkça söylese sövülür ve dövülürdü (s1–s7); "
          "Şeytan'ın hilesi — insanların kafalarına bir kapı: ölmüş, Allah'tan korkan, halkın sevdiği adamlar; «aranızda falan nasıldı?» — «Allah'ın adamları ve dostları!» (s8–s14). Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(2, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §3–4, pp. 9–11", GLOSS_ADD, notes=(), related=())
report(2, S, GLOSS_ADD, ())
