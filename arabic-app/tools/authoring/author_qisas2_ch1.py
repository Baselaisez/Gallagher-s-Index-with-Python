# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 45: «قِصَّةُ عِيسَى» §42 (from an obscure creed to open idolatry — Europe, the Greeks and the Romans, Constantine; the author's footnote; the straying road; al-Fātiḥa 1:6–7; the tragedy of Europe; «to God belongs the command before and after»). Print pp. 68–70 — the END of the book's text.
python3 tools/authoring/author_qisas4_ch45.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: بَعْدَ آدَمَ — حَسَدُ الشَّيْطَانِ", "en": "The ship of Nūḥ: after Ādam — the envy of Satan", "tr": "Nûh'un gemisi: Âdem'den sonra — Şeytan'ın hasedi"}
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
def adam_mi(punct=None, role="مُضَافٌ إِلَيْهِ"):
    return tok("آدَمَ", "adam-prophet", "propn", [ID, MM], role + " مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ādam» — the mudaf ilayh; a foreign name, a diptote: fatḥa for the kasra.", "«Âdem» — muzâfun ileyh; yabancı özel isim, gayr-i munsarif: kesre yerine fetha.", punct=punct)
def allah_maful(full="اللهَ", punct=None):
    return tok(full, "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«Allah» — the object, in naṣb.", "«Allah» — lafza-i celâl, mef'ûl, mansub.", punct=punct)
def kanat(full="وَكَانَتْ", wa=True, punct=None):
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "كَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ.", ("«and» + " if wa else "") + "«there was» — kāna with the feminine tāʾ.", ("«ve» + " if wa else "") + "«vardı» — te'nis tâsı almış kâne.", punct=punct, segments=(wa_("كَانَتْ", "kana", "verb") if wa else None))
def ala_istifham(punct=None):
    return tok("أَلَا", "a-istifham", "part", [IS, "la-nafiya"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَلَا نَافِيَةٌ.", "«does … not?» — the hamza of the (denying) question + the negating lā.", "«… değil mi?» — inkârî istifham hemzesi + nefiy lâ'sı.", punct=punct, segments=[seg("أَ", "a-istifham", "part"), seg("لَا", "la-nafiya", "part")])
def yazalu(punct=None):
    return tok("يَزَالُ", "zala", "verb", [KN, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ (مَا زَالَ) مَرْفُوعٌ بِالضَّمَّةِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.", "«… still» — the defective yazālu (of mā zāla), a sister of kāna: it raises its ism and puts its khabar in naṣb.", "«hâlâ …» — nâkıs yezâlu (mâ zâle), kâne'nin kız kardeşi: ismini ref, haberini nasb eder.", punct=punct)
def nas_ism_kana(punct=None, of="يَزَالُ"):
    return tok("النَّاسُ", "nas", "noun", [KN], f"اسْمُ {of} مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — the ism of " + ("yazālu" if of == "يَزَالُ" else "kāna") + ".", "«insanlar» — " + ("yezâlu" if of == "يَزَالُ" else "kâne") + "'nun ismi.", punct=punct)
def inna_dhalika_la_yakunu(punct="!", wa=False):
    return [inna("وَإِنَّ" if wa else "إِنَّ", wa=wa),
            tok("ذٰلِكَ", "dhalika", "pron", [IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«that» — a demonstrative, built; the ism of inna.", "«bu» — ism-i işâret, mebnî; inne'nin ismi."),
            la_nafiya(),
            tok("يَكُونُ", "kana", "verb", ["la-nafiya", "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — أَيْ: لَا يَحْدُثُ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«will [not] be» — the complete yakūnu («happen»); the clause is inna's khabar.", "«olmaz» — tam yekûnu («vuku bulmak»); cümle inne'nin haberi.", punct=punct)]

# ---------------------------------------------------------------- §1 بَعْدَ آدَمَ (print p. 8)
sen("s1", "God blessed the offspring of Ādam, and there came to be many men in it, and women. And the offspring of Ādam spread and grew many.",
        "Allah Âdem'in zürriyetini bereketlendirdi; içinde pek çok erkek ve kadınlar oldu. Âdem'in zürriyeti yayıldı ve çoğaldı.", [
  mazi("بَارَكَ", "baraka-bless", "«blessed»", "«bereketlendirdi»", tags=["form-iii-verbs"], hidden=None),
  allah_fail(),
  fi(),
  majrur("ذُرِّيَّةِ", "dhurriyya", "«the offspring [of]»", "«zürriyetine»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  adam_mi(),
  kana("فَكَانَ", wa=True),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it»", "«onda»", extra_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ"),
  ism_kana("رِجَالٌ", "rajul", "«men»", "«erkekler»", tags=[JT], ar="اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ رَجُلٍ."),
  naat2("كَثِيرٌ", "kathir", "«many»", "«pek çok»", case="raf", n=""),
  atf("وَنِسَاءٌ", "nisa", "«women»", "«kadınlar»", case="raf", punct=".", tags=[JT]),
  mazi_ta("وَانْتَشَرَتْ", "intashara", "«and spread»", "«ve yayıldı»", tags=["form-viii-verbs"], wa=True),
  fail("ذُرِّيَّةُ", "dhurriyya", "«the offspring [of]»", "«zürriyeti»", tags=[ID], extra_ar="، مُضَافٌ"),
  adam_mi(),
  mazi_ta("وَكَثُرَتْ", "kathura", "«and grew many»", "«ve çoğaldı»", wa=True, punct="."),
])
sen("s2", "Had Ādam come back and seen his children, he would not have known them.",
        "Âdem dönüp çocuklarını görseydi, tanımazdı.", [
  tok("فَلَوْ", "law", "part", ["in-shartiyya", AT], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ (حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ).", "«and had …» — the fāʾ opens the sentence; law, the non-jussive conditional («had it been so»).", "«… olsaydı» — fâ cümleyi başlatır; lev, cezmetmeyen şart edatı.", segments=[seg("فَ", "fa", "conj"), seg("لَوْ", "law", "part")]),
  mazi("رَجَعَ", "rajaa", "«came back»", "«dönseydi»", tags=["in-shartiyya"], hidden=None),
  fail_name("آدَمُ", "adam-prophet", "«Ādam»", "«Âdem»"),
  mazi("وَرَأَى", "raa", "«and saw»", "«ve görseydi»", tags=["naqis-verbs", AT], wa=True),
  noun_pron("أَوْلَادَهُ", "walad", "أَوْلَادَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ وَلَدٍ.", "«his children» — the object, annexed to the pronoun.", "«çocuklarını» — mef'ûl, zamire muzâf.", tags=[MB, ID, JT]),
  tok("لَمَا", "la-jawab-law", "part", ["in-shartiyya", "la-nafiya"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَمَا نَافِيَةٌ.", "«… not» — the lām that opens law's answer + the negating mā.", "«… -mazdı» — lev'in cevabına giren lâm + nefiy mâ'sı.", segments=[seg("لَ", "la-jawab-law", "part"), seg("مَا", "ma-nafiya", "part")]),
  mazi("عَرَفَ", "arafa", "«he would have known [them]»", "«tanırdı»", tags=["in-shartiyya"], punct="."),
])
sen("s3", "And had it been said to him: «This is your offspring, O Ādam», he would have wondered greatly.",
        "Ona «Ey Âdem, bu senin zürriyetindir» denseydi, çok şaşardı.", [
  tok("وَلَوْ", "law", "part", ["in-shartiyya", AT], "الْوَاوُ عَاطِفَةٌ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ.", "«and had …» — law, the non-jussive conditional.", "«ve … olsaydı» — lev, cezmetmeyen şart edatı.", segments=wa_("لَوْ", "law", "part")),
  tok("قِيلَ", "qala", "verb", [NF, "hollow-verbs", "in-shartiyya"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَقُولَةُ (أَوْ ضَمِيرٌ مُسْتَتِرٌ).", "«it were said» — the passive qīla of qāla; what is said stands for the doer.", "«denseydi» — kâle'nin meçhulü kîle; söylenen söz nâib-i fâildir."),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to him»", "«ona»", punct=":"),
  ishara("هٰذِهِ", "hadhihi", "raf", "«this»", "«bu»", tags=[MK]),
  noun_pron("ذُرِّيَّتُكَ", "dhurriyya", "ذُرِّيَّتُ", "كَ", "pron-2ms", "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your offspring» — the khabar, annexed to «you».", "«senin zürriyetin» — haber, zamire muzâf.", tags=[MK, ID]),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O» — the vocative particle.", "«ey» — nidâ harfi."),
  tok("آدَمُ", "adam-prophet", "propn", ["vocative-munada", MM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Ādam» — a single-name munādā, built on ḍamma in the place of naṣb.", "«Âdem» — müfred alem münâdâ, zamme üzere mebnî, mahallen mansub."),
  tok("لَتَعَجَّبَ", "taajjaba", "verb", ["in-shartiyya", "form-v-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَتَعَجَّبَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "«he would have wondered» — the lām of law's answer + the māḍī; the doer is concealed.", "«şaşardı» — lev'in cevabının lâmı + mâzî; fâil gizli.", segments=[seg("لَ", "la-jawab-law", "part"), seg("تَعَجَّبَ", "taajjaba", "verb")]),
  tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — أَيْ: تَعَجُّبًا كَثِيرًا.", "«greatly» — standing for the mafʿūl muṭlaq («a great wondering»).", "«çok» — mef'ûl-i mutlak yerine («çok bir şaşma»).", punct="."),
])
sen("s4", "And he would have said: «Glory be to God! Are these all my children? Is all this my offspring?!»",
        "Ve derdi ki: «Sübhânallah! Bunların hepsi benim çocuklarım mı? Bunların hepsi benim zürriyetim mi?!»", [
  qala("وَقَالَ", wa=True),
  tok("سُبْحَانَ", "subhan", "noun", ["maful-mutlaq", ID], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«glory [be to]» — the mafʿūl muṭlaq of a deleted verb (usabbiḥu), annexed.", "«tesbih» — mahzuf fiilin mef'ûl-i mutlakı (üsebbihu), muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "«God» — the mudaf ilayh.", "«Allah» — muzâfun ileyh.", punct="!"),
  ishara("هٰؤُلَاءِ", "haulai", "raf", "«these»", "«bunlar»", tags=[MK]),
  noun_pron("كُلُّهُمْ", "kull", "كُلُّ", "هُمْ", "pron-3mp", "تَوْكِيدٌ مَعْنَوِيٌّ لِاسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«all of them» — the emphasis (tawkīd) of the demonstrative, annexed.", "«hepsi» — ism-i işâretin manevî tekidi, muzâf.", tags=["tawkid", ID]),
  noun_pron("أَوْلَادِي", "walad", "أَوْلَادِ", "ي", "pron-1s", "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my children» — the khabar; the ḍamma is hidden under the kasra that the yāʾ demands.", "«benim çocuklarım» — haber; damme, yâ'nın istediği kesrenin altında gizli.", tags=[MK, ID, JT, "ya-al-mutakallim"], punct="؟"),
  ishara("هٰذِهِ", "hadhihi", "raf", "«this»", "«bu»", tags=[MK]),
  noun_pron("كُلُّهَا", "kull", "كُلُّ", "هَا", "pron-3fs", "تَوْكِيدٌ مَعْنَوِيٌّ لِاسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«all of it» — the emphasis of the demonstrative, annexed.", "«hepsi» — ism-i işâretin tekidi, muzâf.", tags=["tawkid", ID]),
  noun_pron("ذُرِّيَّتِي", "dhurriyya", "ذُرِّيَّتِ", "ي", "pron-1s", "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my offspring» — the khabar; the ḍamma hidden before the speaker's yāʾ.", "«benim zürriyetim» — haber; damme mütekellim yâ'sından önce gizli.", tags=[MK, ID, "ya-al-mutakallim"], punct="؟!"),
])
sen("s5", "And the offspring of Ādam had many villages, and they built many houses.",
        "Âdem'in zürriyetinin pek çok köyü vardı; pek çok ev yaptılar.", [
  kanat(),
  li_noun("لِذُرِّيَّةِ", "dhurriyya", "«the offspring [of]»", "«zürriyetinin»", tags=[ID], extra="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ"),
  adam_mi(),
  tok("قُرًى", "qarya", "noun", [KN, JT, "ism-maqsur-manqus"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — جَمْعُ قَرْيَةٍ، مَقْصُورٌ مُنَوَّنٌ.", "«villages» — kāna's ism, delayed; a maqṣūr plural of qarya, its ḍamma hidden on the alif.", "«köyler» — kâne'nin ismi, muahhar; karye'nin maksur çoğulu, dammesi elif üzerinde gizli."),
  naat2("كَثِيرَةٌ", "kathir", "«many»", "«pek çok»", case="raf", n="", punct="،"),
  tok("وَبَنَوْا", "bana", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَبَنَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَوَاوُ الْجَمَاعَةِ فَاعِلٌ.", "«and they built» — the defective māḍī before the group's wāw: its alif drops (banā → banaw); the wāw is the doer.", "«ve yaptılar» — cemaat vâvından önce nâkıs mâzî: elifi düşer (benâ → benev); vâv fâildir.", segments=[seg("وَ", "wa", "conj"), seg("بَنَ", "bana", "verb"), seg("وْا", "pron-3mp", "pron")]),
  maful_("بُيُوتًا", "bayt", "«houses»", "«evler»", tags=[JT]),
  naat("كَثِيرَةً", "kathir", "«many»", "«pek çok»", case="nasb", punct="."),
])
sen("s6", "And they used to till the earth, and sow, and live.",
        "Toprağı sürer, ekip biçer ve yaşarlardı.", [
  kana_pl(),
  khamsa("يَحْرُثُونَ", "haratha", "«till»", "«sürerlerdi»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  maful_("الْأَرْضَ", "ard", "«the earth»", "«toprağı»"),
  khamsa("وَيَزْرَعُونَ", "zaraa", "«and sow»", "«ve ekerlerdi»", tags=[AT], wa=True),
  khamsa("وَيَعِيشُونَ", "asha-live", "«and live»", "«ve yaşarlardı»", tags=[AT, "hollow-verbs"], wa=True, punct="."),
])
sen("s7", "And the people were on the religion of their father Ādam: they worshipped God and associated nothing with Him!",
        "İnsanlar babaları Âdem'in dini üzereydi: Allah'a ibadet eder, O'na hiçbir şeyi ortak koşmazlardı!", [
  kana(),
  ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»"),
  prep("عَلَى", "ala", "«on»", "«üzere»"),
  majrur("دِينِ", "din", "«the religion [of]»", "«dini»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  noun_pron("أَبِيهِمْ", "ab", "أَبِي", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their father» — the mudaf ilayh; one of the five nouns, its jarr written as the yāʾ.", "«babalarının» — muzâfun ileyh; beş isimden, cerri yâ ile.", tags=[ID, "five-nouns"]),
  tok("آدَمَ", "adam-prophet", "propn", [BD, MM], "بَدَلٌ مِنْ أَبِيهِمْ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ādam» — the substitute (badal) of «their father»; a diptote: fatḥa for the kasra.", "«Âdem» — «babaları»nın bedeli; gayr-i munsarif: kesre yerine fetha.", punct="،"),
  khamsa("يَعْبُدُونَ", "abada", "«they worshipped»", "«ibadet ederlerdi»", tags=[HL], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  allah_maful(),
  la_nafiya("وَلَا", wa=True),
  khamsa("يُشْرِكُونَ", "ashraka", "«associated»", "«ortak koşmazlardı»", tags=[AT, "form-iv-verbs", "la-nafiya"]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with Him»", "«O'na»"),
  maful_("شَيْئًا", "shay", "«anything»", "«hiçbir şeyi»", punct="!"),
])
sen("s8", "And the people were one community: their father was Ādam and their Lord was God.",
        "İnsanlar tek bir ümmetti: babaları Âdem, Rableri Allah'tı.", [
  kana(),
  ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»"),
  khabar_kana("أُمَّةً", "umma", "«a community»", "«bir ümmet»"),
  naat("وَاحِدَةً", "wahid", "«one»", "«tek»", case="nasb"),
  noun_pron("أَبُوهُمْ", "ab", "أَبُو", "هُمْ", "pron-3mp", "مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ لِأُمَّةٍ.", "«their father» — the mubtada; one of the five nouns, its rafʿ written as the wāw; the clause describes «community».", "«babaları» — mübtedâ; beş isimden, ref'i vâv ile; cümle «ümmet»in sıfatı.", tags=[MK, ID, "five-nouns", "jumla-sifa"]),
  tok("آدَمُ", "adam-prophet", "propn", [MK, MM], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ādam» — the khabar.", "«Âdem» — haber."),
  tok("وَرَبُّهُمُ", "rabb", "noun", [AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَرَبُّ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ (حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ).", "«and their Lord» — a second mubtada, annexed; the mīm takes a ḍamma before the hamzat al-waṣl.", "«ve Rableri» — ikinci mübtedâ, muzâf; mîm, vasıl hemzesinden önce damme alır.", segments=[seg("وَ", "wa", "conj"), seg("رَبُّ", "rabb", "noun"), seg("هُمُ", "pron-3mp", "pron")]),
  tok("اللهُ", "allah", "propn", [MK], "لَفْظُ الْجَلَالَةِ خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«God» — the khabar.", "«Allah» — haber.", punct="."),
])
# ---------------------------------------------------------------- §2 حَسَدُ الشَّيْطَانِ (print p. 9)
sen("s9", "But how could Iblīs and his offspring be content with this? Would the people go on worshipping God?",
        "Fakat İblis ve zürriyeti buna nasıl razı olsun? İnsanlar Allah'a ibadet etmeye devam mı edecek?", [
  tok("وَلٰكِنْ", "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin, a particle of correction with no government.", "«fakat» — muhaffef lâkin, amel etmeyen istidrâk harfi.", segments=wa_("لٰكِنْ", "lakin", "part")),
  tok("كَيْفَ", "kayfa", "noun", [IS, HL], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — the interrogative, built; in the place of a ḥāl.", "«nasıl» — istifham ismi, mebnî; mahallen hâl."),
  tok("يَرْضَى", "radiya", "verb", ["mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "«is content» — a defective muḍāriʿ; the ḍamma hidden on the alif.", "«razı olur» — nâkıs muzâri; damme elif üzerinde gizli."),
  fail_name("إِبْلِيسُ", "iblis", "«Iblīs»", "«İblis»"),
  pron_atf("وَذُرِّيَّتُهُ", "dhurriyya", "ذُرِّيَّتُ", "هُ", "pron-3ms", "«and his offspring»", "«ve zürriyeti»", case="raf"),
  tok("بِهٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمُ الْإِشَارَةِ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«with this» — bi + the demonstrative, built in the place of jarr.", "«buna» — bi + ism-i işâret, mahallen mecrur.", punct="؟", segments=[seg("بِ", "bi", "prep"), seg("هٰذَا", "hadha", "pron")]),
  ala_istifham(),
  yazalu(),
  nas_ism_kana(),
  khamsa("يَعْبُدُونَ", "abada", "«worshipping»", "«ibadet eder»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ يَزَالُ"),
  allah_maful(punct="؟"),
])
sen("s10", "Would the people go on being one community that does not differ? That shall not be! That shall not be!",
        "İnsanlar ihtilâfa düşmeyen tek bir ümmet olmaya devam mı edecek? Bu olmaz! Bu olmaz!", [
  ala_istifham(),
  yazalu(),
  nas_ism_kana(),
  khabar_kana("أُمَّةً", "umma", "«a community»", "«bir ümmet»", ar="خَبَرُ يَزَالُ مَنْصُوبٌ بِالْفَتْحَةِ."),
  naat("وَاحِدَةً", "wahid", "«one»", "«tek»", case="nasb"),
  la_nafiya(),
  khamsa("يَخْتَلِفُونَ", "ikhtalafa", "«they do not differ»", "«ihtilâfa düşmezler»", tags=["la-nafiya", "form-viii-verbs", "jumla-sifa"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِأُمَّةٍ", punct="؟"),
  *inna_dhalika_la_yakunu("!"),
  *inna_dhalika_la_yakunu("!"),
])
sen("s11", "Shall the offspring of Ādam enter Paradise, while Iblīs and his offspring enter the Fire?",
        "Âdem'in zürriyeti cennete girsin de İblis ve zürriyeti ateşe mi girsin?", [
  tok("هَلْ", "hal-istifham", "part", [IS], "حَرْفُ اسْتِفْهَامٍ.", "«does … ?» — the interrogative particle.", "«… mi?» — istifham harfi."),
  tok("يَدْخُلُ", "dakhala", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«enter[s]» — a muḍāriʿ in rafʿ.", "«girer» — merfû muzâri."),
  fail("ذُرِّيَّةُ", "dhurriyya", "«the offspring [of]»", "«zürriyeti»", tags=[ID], extra_ar="، مُضَافٌ"),
  adam_mi(),
  maful_("الْجَنَّةَ", "janna", "«Paradise»", "«cennete»", punct="،"),
  tok("وَيَدْخُلُ", "dakhala", "verb", [AT, "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَدْخُلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«and enter[s]»", "«ve girer»", segments=wa_("يَدْخُلُ", "dakhala", "verb")),
  fail_name("إِبْلِيسُ", "iblis", "«Iblīs»", "«İblis»"),
  pron_atf("وَذُرِّيَّتُهُ", "dhurriyya", "ذُرِّيَّتُ", "هُ", "pron-3ms", "«and his offspring»", "«ve zürriyeti»", case="raf"),
  maful_("النَّارَ", "nar", "«the Fire»", "«ateşe»", punct="؟"),
])
sen("s12", "That shall not be; that shall not be!",
        "Bu olmaz, bu olmaz!", [
  *inna_dhalika_la_yakunu("،"),
  *inna_dhalika_la_yakunu("!"),
])
sen("s13", "He had not prostrated to Ādam, so God drove him out and cursed him.",
        "O, Âdem'e secde etmemişti; bu yüzden Allah onu kovmuş ve lânetlemişti.", [
  tok("إِنَّهُ", "inna", "part", [IW], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ إِنَّ.", "«indeed he» — inna + its ism, the pronoun.", "«şüphesiz o» — inne + ismi olan zamir.", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("لَمْ", "lam", "part", [LJ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«did not» — the jussive lam: it negates, cuts, and turns the sense to the past.", "«-medi» — cezm eden lem: nefyeder, cezmeder, mânâyı maziye çevirir."),
  tok("يَسْجُدْ", "sajada", "verb", [LJ, IW], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "«prostrate» — jussive by lam, its sign the sukūn; the clause is inna's khabar.", "«secde etmedi» — lem ile meczum, alâmeti sükûn; cümle inne'nin haberi."),
  tok("لِآدَمَ", "adam-prophet", "propn", [HJ, MM], "اللَّامُ حَرْفُ جَرٍّ، وَآدَمَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«to Ādam» — li + the diptote name: fatḥa for the kasra.", "«Âdem'e» — li + gayr-i munsarif isim: kesre yerine fetha.", segments=[seg("لِ", "li", "prep"), seg("آدَمَ", "adam-prophet", "propn")]),
  v_pron("فَطَرَدَهُ", "tarada-expel", "طَرَدَ", "هُ", "pron-3ms", "«so [God] drove him out»", "«bu yüzden onu kovdu»", fa=True, hidden=None),
  allah_fail(),
  v_pron("وَلَعَنَهُ", "laana", "لَعَنَ", "هُ", "pron-3ms", "«and cursed him»", "«ve onu lânetledi»", wa=True, punct="."),
])
sen("s14", "Will he not take revenge on the children of Ādam, so that they enter the Fire with him?",
        "Âdemoğullarından intikam alıp onları kendisiyle beraber ateşe sokmayacak mı?", [
  ala_istifham(),
  mudari("يَنْتَقِمُ", "intaqama", "«he takes revenge»", "«intikam alır»", tags=["form-viii-verbs", "la-nafiya"]),
  prep("مِنْ", "min", "«on»", "«-den»"),
  tok("بَنِي", "ibn", "noun", [HJ, ID, JS], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، مُضَافٌ.", "«the children [of]» — banī: jarr by the yāʾ (attached to the sound plural); the nūn drops for the iḍāfa.", "«oğulları» — benî: yâ ile mecrur (cem-i müzekker sâlime mülhak); izâfetle nûn düşer."),
  adam_mi(),
  tok("فَيَدْخُلُوا", "dakhala", "verb", [AK, AN], "الْفَاءُ لِلسَّبَبِيَّةِ فِي جَوَابِ الِاسْتِفْهَامِ، وَيَدْخُلُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ الْفَاءِ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«so that they enter» — the fāʾ of consequence after the question; naṣb by a hidden an, the nūn dropped; the wāw is the doer.", "«… girsinler diye» — istifhamın cevabındaki sebebiyet fâ'sı; gizli en ile mansub, nûn düşmüş; vâv fâil.", segments=[seg("فَ", "fa", "conj"), seg("يَدْخُلُ", "dakhala", "verb"), seg("وا", "pron-3mp", "pron")]),
  noun_pron("مَعَهُ", "maa", "مَعَ", "هُ", "pron-3ms", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with him» — a ẓarf, annexed to the pronoun.", "«onunla beraber» — zarf, zamire muzâf.", tags=[MF, ID]),
  maful_("النَّارَ", "nar", "«the Fire»", "«ateşe»", punct="؟"),
])
sen("s15", "That must be! That must be.",
        "Bu mutlaka olacak! Bu mutlaka olacak.", [
  la_jins("لَا"),
  ism_la("بُدَّ", "budd", "«[there is no] escape»", "«çare [yok]»", khabar="لَنَا"),
  tok("أَنْ", "an-masdariyya", "part", [AN, "hadhf-al-jarr"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِمِنْ مَحْذُوفَةٍ: لَا بُدَّ مِنْ كَوْنِ ذٰلِكَ.", "«that» — the masdar-making an; the clause stands under a deleted min («no escape from that being»).", "«-ması» — masdar en; cümle mahzuf min'in altında («bunun olmasından kaçış yok»)."),
  tok("يَكُونَ", "kana", "verb", [AN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ تَامٌّ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«be» — the complete yakūna, naṣb by an.", "«olması» — tam yekûne, en ile mansub."),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", FL], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«that» — the demonstrative, built; in the place of the doer.", "«bu» — ism-i işâret, mebnî; mahallen fâil.", punct="!"),
  la_jins("لَا"),
  ism_la("بُدَّ", "budd", "«[there is no] escape»", "«çare [yok]»", khabar="لَنَا"),
  tok("أَنْ", "an-masdariyya", "part", [AN, "hadhf-al-jarr"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِمِنْ مَحْذُوفَةٍ.", "«that» — the masdar-making an under a deleted min.", "«-ması» — mahzuf min'in altındaki masdar en."),
  tok("يَكُونَ", "kana", "verb", [AN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ تَامٌّ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«be» — the complete yakūna, naṣb by an.", "«olması» — tam yekûne, en ile mansub."),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", FL], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«that» — the demonstrative, built; in the place of the doer.", "«bu» — ism-i işâret, mebnî; mahallen fâil.", punct="."),
])

CAND = {
 "baraka-bless": G("baraka-bless", "بَارَكَ", "ب ر ك", "verb", "to bless (Form III)", "bereketlendirmek, mübarek kılmak (mufâale)", 1),
 "dhurriyya": G("dhurriyya", "ذُرِّيَّة", "ذ ر ر", "noun", "offspring, progeny", "zürriyet, nesil", 1, plural="ذُرِّيَّات / ذَرَارِيّ"),
 "adam-prophet": G("adam-prophet", "آدَم", None, "propn", "Ādam (the first man and prophet)", "Âdem (ilk insan ve peygamber)", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam, erkek", 1, plural="رِجَال"),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "nisa": G("nisa", "نِسَاء", "ن س و", "noun", "women (a plural with no singular of its own)", "kadınlar (kendi tekili olmayan bir çoğul)", 1),
 "intashara": G("intashara", "اِنْتَشَرَ", "ن ش ر", "verb", "to spread, to become widespread (Form VIII)", "yayılmak (iftiâl)", 1),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, to grow numerous", "çoğalmak, çok olmak", 1),
 "law": G("law", "لَوْ", None, "part", "if (contrary to fact: «had it been so»)", "eğer (olmayana bağlı şart: «olsaydı»)", 1),
 "rajaa": G("rajaa", "رَجَعَ", "ر ج ع", "verb", "to return, to come back", "dönmek", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see", "görmek", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "child, son", "çocuk, oğul", 1, plural="أَوْلَاد"),
 "la-jawab-law": G("la-jawab-law", "لَ (فِي جَوَابِ لَوْ)", None, "part", "the lām that opens the answer of law", "lev'in cevabına giren lâm", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not — the negating mā", "değil, -medi — nefiy mâ'sı", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, to recognize", "bilmek, tanımak", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O — the vocative particle", "ey — nidâ harfi", 1),
 "taajjaba": G("taajjaba", "تَعَجَّبَ", "ع ج ب", "verb", "to wonder, to be amazed (Form V)", "şaşmak, hayret etmek (tefa''ul)", 1),
 "subhan": G("subhan", "سُبْحَان", "س ب ح", "noun", "glory (be to …) — the masdar of praise", "tesbih, (… münezzehtir)", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these", "bunlar", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, bütün", 1),
 "qarya": G("qarya", "قَرْيَة", "ق ر ي", "noun", "village, town", "köy, kasaba", 1, plural="قُرًى"),
 "bana": G("bana", "بَنَى", "ب ن ي", "verb", "to build", "yapmak, inşa etmek", 1),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "house", "ev", 1, plural="بُيُوت"),
 "haratha": G("haratha", "حَرَثَ", "ح ر ث", "verb", "to till, to plough", "toprağı sürmek, çift sürmek", 1),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "earth, land", "yer, toprak", 1, plural="أَرَضُونَ / أَرَاضٍ"),
 "zaraa": G("zaraa", "زَرَعَ", "ز ر ع", "verb", "to sow, to plant", "ekmek, dikmek", 1),
 "asha-live": G("asha-live", "عَاشَ", "ع ي ش", "verb", "to live (hollow)", "yaşamak (ecvef)", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon", "üzerine, üzere", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1, plural="أَدْيَان"),
 "ab": G("ab", "أَب", "أ ب و", "noun", "father", "baba", 1, plural="آبَاء"),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek, tapmak", 1),
 "ashraka": G("ashraka", "أَشْرَكَ", "ش ر ك", "verb", "to associate (a partner with God) (Form IV)", "ortak koşmak, şirk koşmak (if'âl)", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "umma": G("umma", "أُمَّة", "أ م م", "noun", "community, nation", "ümmet, topluluk", 1, plural="أُمَم"),
 "wahid": G("wahid", "وَاحِد", "و ح د", "noun", "one", "bir, tek", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but (the lightened lākin)", "fakat (muhaffef lâkin)", 1),
 "kayfa": G("kayfa", "كَيْفَ", None, "noun", "how", "nasıl", 1),
 "radiya": G("radiya", "رَضِيَ", "ر ض و", "verb", "to be content, to be pleased (with: بِ)", "razı olmak (bi: -e)", 1),
 "iblis": G("iblis", "إِبْلِيس", None, "propn", "Iblīs — Satan", "İblis — Şeytan", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this (masculine)", "bu (müzekker)", 1),
 "a-istifham": G("a-istifham", "أَ", None, "part", "the interrogative hamza («…?»)", "istifham hemzesi («… mi?»)", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "not — the negating lā", "değil, -mez — nefiy lâ'sı", 1),
 "zala": G("zala", "زَالَ (مَا زَالَ)", "ز ي ل", "verb", "to cease (mā zāla / lā yazālu: to go on, still be)", "zâil olmak (mâ zâle / lâ yezâlu: devam etmek, hâlâ … olmak)", 1),
 "ikhtalafa": G("ikhtalafa", "اِخْتَلَفَ", "خ ل ف", "verb", "to differ, to disagree (Form VIII)", "ihtilâf etmek, ayrılığa düşmek (iftiâl)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — the emphasizing particle", "şüphesiz — tekid harfi", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that (masculine)", "o, şu (müzekker)", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "hal-istifham": G("hal-istifham", "هَلْ", None, "part", "does …? — the interrogative particle", "… mi? — istifham harfi", 1),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "janna": G("janna", "جَنَّة", "ج ن ن", "noun", "garden; Paradise", "bahçe; cennet", 1, plural="جَنَّات"),
 "nar": G("nar", "نَار", "ن و ر", "noun", "fire; the Fire (Hell)", "ateş; cehennem", 1),
 "lam": G("lam", "لَمْ", None, "part", "did not — the jussive lam", "-medi — cezm eden lem", 1),
 "sajada": G("sajada", "سَجَدَ", "س ج د", "verb", "to prostrate", "secde etmek", 1),
 "tarada-expel": G("tarada-expel", "طَرَدَ", "ط ر د", "verb", "to drive away, to expel", "kovmak, sürmek", 1),
 "laana": G("laana", "لَعَنَ", "ل ع ن", "verb", "to curse", "lânetlemek", 1),
 "intaqama": G("intaqama", "اِنْتَقَمَ", "ن ق م", "verb", "to take revenge (on: مِنْ) (Form VIII)", "intikam almak (min: -den) (iftiâl)", 1),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "ibn": G("ibn", "ابْن", "ب ن و", "noun", "son", "oğul", 1, plural="بَنُونَ"),
 "maa": G("maa", "مَعَ", None, "noun", "with", "ile, beraber", 1),
 "budd": G("budd", "بُدّ", "ب د د", "noun", "escape, way out (لَا بُدَّ: it must be)", "kaçış, çare (lâ budde: mutlaka)", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the masdar-making an", "-mesi — masdar en'i", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "fa": G("fa", "فَ", None, "conj", "so, then", "bunun üzerine", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "she / it / her (attached)", "o / onun (bitişik)", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masculine singular, attached)", "sen / senin (bitişik)", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "me / my (attached)", "beni / benim (bitişik)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "intashara", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَشَر", "نْتَشِر", "اِنْتَشِر", "اِنْتِشَار", "مُنْتَشِر", None, None, None, "اِنْتَشَرَ الشَّيْءُ: تَفَرَّقَ وَذَاعَ — لَازِمٌ."))
put_morph(mo, "haratha", _sg.sound1("nasara", "حَرَث", "حْرُث", "اُحْرُث", "حَرْث", "حَارِث", "مَحْرُوث", "حُرِثَ", "يُحْرَثُ", "حَرَثَ الْأَرْضَ يَحْرُثُهَا: شَقَّهَا لِلزَّرْعِ."))
put_morph(mo, "tarada-expel", _sg.sound1("nasara", "طَرَد", "طْرُد", "اُطْرُد", "طَرْد", "طَارِد", "مَطْرُود", "طُرِدَ", "يُطْرَدُ", "طَرَدَهُ يَطْرُدُهُ: أَبْعَدَهُ وَنَحَّاهُ."))
put_morph(mo, "intaqama", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَقَم", "نْتَقِم", "اِنْتَقِم", "اِنْتِقَام", "مُنْتَقِم", None, None, None, "اِنْتَقَمَ مِنْهُ: عَاقَبَهُ جَزَاءَ مَا فَعَلَ — يَتَعَدَّى بِمِنْ."))
put_morph(mo, "zala", _sg.hollow1("fataha", "أَجْوَفُ يَائِيٌّ — نَاقِصٌ مِنْ أَخَوَاتِ كَانَ (مَا زَالَ، لَا يَزَالُ)", "زَال", "زِل", "زَال", "زَل", "زَال", "زَل", "زَوَال", "زَائِل", None, None, None, "مَا زَالَ يَفْعَلُ كَذَا: اسْتَمَرَّ — زَالَ يَزَالُ مِنْ بَابِ فَتَحَ (أَصْلُهُ زَيِلَ)؛ لَا يُسْتَعْمَلُ نَاقِصًا إِلَّا مَسْبُوقًا بِنَفْيٍ أَوْ نَهْيٍ أَوْ دُعَاءٍ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch1 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 1 (print pp. 8–9; Nūḥ §1–2): after Ādam — God blesses his offspring, they spread, build villages and houses, till and sow, and stay on their father's religion, one community (s1–s8); "
          "the envy of Satan — how can Iblīs be content? that shall not be; he who refused to prostrate and was cursed must take his revenge (s9–s15). One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" Birinci bölüm (basılı s. 8–9; Nûh §1–2): Âdem'den sonra — Allah zürriyetini bereketlendirir, yayılırlar, köyler ve evler yaparlar, sürüp ekerler ve babalarının dini üzere tek bir ümmet kalırlar (s1–s8); "
          "Şeytan'ın hasedi — İblis buna nasıl razı olsun? bu olmaz; secdeyi reddedip lânetlenen, intikamını almalıdır (s9–s15). Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(1, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §1–2, pp. 8–9", GLOSS_ADD, notes=(), related=())
report(1, S, GLOSS_ADD, ())
