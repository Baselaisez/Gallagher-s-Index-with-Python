# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 45: «قِصَّةُ عِيسَى» §42 (from an obscure creed to open idolatry — Europe, the Greeks and the Romans, Constantine; the author's footnote; the straying road; al-Fātiḥa 1:6–7; the tragedy of Europe; «to God belongs the command before and after»). Print pp. 68–70 — the END of the book's text.
python3 tools/authoring/author_qisas4_ch45.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: صُوَرُ الصَّالِحِينَ — مِنَ الصُّوَرِ إِلَى التَّمَاثِيلِ", "en": "The ship of Nūḥ: pictures of the righteous — from pictures to statues", "tr": "Nûh'un gemisi: salihlerin resimleri — resimlerden heykellere"}
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
def kayfa(role_ar, role_en, role_tr, full="كَيْفَ", wa=False, fa=False, punct=None):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj"), seg("كَيْفَ", "kayfa", "noun")] if (wa or fa) else None)
    return tok(full, "kayfa", "noun", [IS] + ([AT] if (wa or fa) else []), pre + "كَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ " + role_ar + ".", ("«and» + " if (wa or fa) else "") + "«how» — the interrogative, built; " + role_en + ".", ("«ve» + " if (wa or fa) else "") + "«nasıl» — istifham ismi, mebnî; " + role_tr + ".", punct=punct, segments=segs)
def ilayhim(punct=None): return prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«to them»", "«onlara»", punct=punct)
def kulla(what, lex, en, tr, punct=None):
    return [tok("كُلَّ", "kull", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (نَائِبٌ عَنِ الظَّرْفِ)، مُضَافٌ.", "«every» — annexed; the phrase is a time adverbial.", "«her» — muzâf; terkip zaman zarfı."),
            mudaf_ilayh(what, lex, en, tr, punct=punct)]
def idha(full="إِذَا", wa=False, punct=None):
    return tok(full, "idha", "part", ["idha-shartiyya"] + ([AT] if wa else []), ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.", ("«and» + " if wa else "") + "«when» — the conditional time-adverb, built.", ("«ve» + " if wa else "") + "«-dığı zaman» — şart mânâlı zaman zarfı, mebnî.", punct=punct, segments=(wa_("إِذَا", "idha", "part") if wa else None))
def salihin(full, role_ar, en, tr, tags=(), punct=None, segs=None, lex="salih"):
    return tok(full, lex, "noun", [JS] + list(tags), role_ar, en, tr, punct=punct, segments=segs)
def wa_group_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "verb", [AT, AK, "mudari-marfu", MB] + list(tags), "الْوَاوُ عَاطِفَةٌ، وَ" + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", "«and» + " + en + " — a muḍāriʿ of the five; the attached pronoun is its object.", "«ve» + " + tr + " — beş fiilden muzâri; bitişik zamir mef'ûl.", punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")])
def neg_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, hidden="هِيَ"):
    pre = "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ، وَ" if wa else "لَا نَافِيَةٌ، وَ"
    segs = ([seg("وَ", "wa", "conj")] if wa else []) + [seg("لَا", "la-nafiya", "part"), seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ["la-nafiya", "mudari-marfu", MB] + ([AT] if wa else []) + list(tags), pre + stem + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + hidden + "، وَالضَّمِيرُ مَفْعُولٌ بِهِ.", ("«and» + " if wa else "") + "«[does] not» + " + en + " — the negating lā; the pronoun is the object.", ("«ve» + " if wa else "") + "«-mez» + " + tr + " — nefiy lâ'sı; zamir mef'ûl.", punct=punct, segments=segs)

# ---------------------------------------------------------------- §5 صُوَرُ الصَّالِحِينَ (print pp. 11–12)
sen("s1", "Satan said: «And how is your grief for them?»", "Şeytan dedi: «Peki onlara olan üzüntünüz nasıl?»", [
  qala(), shaytan_fail(punct=":"),
  kayfa("رَفْعٍ خَبَرٌ مُقَدَّمٌ", "the fronted khabar", "mukaddem haber", full="فَكَيْفَ", fa=True),
  noun_pron("حُزْنُكُمْ", "huzn", "حُزْنُ", "كُمْ", "pron-2mp", "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ.", "«your grief» — the delayed mubtada, annexed to «your».", "«üzüntünüz» — muahhar mübtedâ, zamire muzâf.", tags=[MK, ID]),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«for them»", "«onlara»", punct="؟"),
])
sen("s2", "They said: «Severe.»", "Dediler: «Şiddetli.»", [
  qalu(),
  tok("شَدِيدٌ", "shadid", "noun", [MK, "hadhf-wa-taqdir", "sifa-mushabbaha"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: حُزْنُنَا، مَرْفُوعٌ بِالضَّمَّةِ.", "«severe» — the khabar of an understood «our grief».", "«şiddetli» — mahzuf «üzüntümüz»ün haberi.", punct="."),
])
sen("s3", "He said: «And how is your longing for them?»", "Dedi: «Peki onlara özleminiz nasıl?»", [
  qala(),
  kayfa("رَفْعٍ خَبَرٌ مُقَدَّمٌ", "the fronted khabar", "mukaddem haber", full="وَكَيْفَ", wa=True),
  noun_pron("اشْتِيَاقُكُمْ", "ishtiyaq", "اشْتِيَاقُ", "كُمْ", "pron-2mp", "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَكُمْ مُضَافٌ إِلَيْهِ — مَصْدَرُ اشْتَاقَ.", "«your longing» — the delayed mubtada; the masdar of Form VIII.", "«özleminiz» — muahhar mübtedâ; iftiâl masdarı.", tags=[MK, ID, "masdar", "form-viii-verbs"]),
  ilayhim(punct="؟"),
])
sen("s4", "They said: «Great!»", "Dediler: «Büyük!»", [
  qalu(),
  tok("عَظِيمٌ", "azim", "noun", [MK, "hadhf-wa-taqdir", "sifa-mushabbaha"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: اشْتِيَاقُنَا، مَرْفُوعٌ بِالضَّمَّةِ.", "«great» — the khabar of an understood «our longing».", "«büyük» — mahzuf «özlemimiz»in haberi.", punct="!"),
])
sen("s5", "He said: «And why do you not look at them every day?»", "Dedi: «Peki neden onlara her gün bakmıyorsunuz?»", [
  qala(),
  tok("وَلِمَاذَا", "limadha", "part", [IS, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِتَنْظُرُونَ.", "«and why» — li + mādhā, the question word in the place of jarr.", "«peki neden» — li + mâzâ, mahallen mecrur soru ismi.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مَاذَا", "limadha", "part")]),
  la_nafiya(),
  khamsa("تَنْظُرُونَ", "nazara", "«you look»", "«bakıyorsunuz»", tags=["la-nafiya"]),
  ilayhim(),
  *kulla("يَوْمٍ", "yawm", "«day»", "«gün»", punct="؟"),
])
sen("s6", "They said: «And what way is there to that, when they have died?»", "Dediler: «Onlar ölmüşken buna giden yol nasıl olur?»", [
  qalu(),
  kayfa("رَفْعٍ خَبَرٌ مُقَدَّمٌ", "the fronted khabar", "mukaddem haber", full="وَكَيْفَ", wa=True),
  tok("السَّبِيلُ", "sabil", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the way» — the delayed mubtada.", "«yol» — muahhar mübtedâ."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«that» — the demonstrative in the place of jarr.", "«buna» — mahallen mecrur ism-i işâret."),
  tok("وَقَدْ", "qad", "part", ["qad-harf", HL], "الْوَاوُ لِلْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ حَالٌ.", "«when [they] have» — the wāw of the ḥāl + qad.", "«… iken» — hâl vâvı + kad.", segments=wa_("قَدْ", "qad", "part")),
  mazi_pl("مَاتُوا", "mata-die", "«they died»", "«öldüler»", tags=["hollow-verbs", "qad-harf"], punct="؟"),
])
sen("s7", "He said: «Make pictures of them and look at them every morning.»", "Dedi: «Onların resimlerini yapın ve her sabah onlara bakın.»", [
  qala(),
  tok("اعْمَلُوا", "amila", "verb", [AM], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«make!» — the imperative on the dropped nūn; the wāw is the doer.", "«yapın!» — nûnun düşmesi üzere mebnî emir; vâv fâil.", segments=[seg("اعْمَلُ", "amila", "verb"), seg("وا", "pron-3mp", "pron")]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«for them»", "«onlar için»"),
  maful_("صُوَرًا", "sura", "«pictures»", "«resimler»", tags=[JT]),
  tok("وَانْظُرُوا", "nazara", "verb", [AT, AM], "الْوَاوُ عَاطِفَةٌ، وَانْظُرُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«and look!» — a second imperative, joined.", "«ve bakın!» — ma'tûf ikinci emir.", segments=[seg("وَ", "wa", "conj"), seg("انْظُرُ", "nazara", "verb"), seg("وا", "pron-3mp", "pron")]),
  prep_pron("إِلَيْهَا", "ila", "هَا", "pron-3fs", "«at them»", "«onlara»"),
  *kulla("صَبَاحٍ", "sabah", "«morning»", "«sabah»", punct="."),
])
sen("s8", "And the people were pleased with Iblīs's opinion; they made pictures of the righteous and used to look at these pictures every day, and whenever they saw them they remembered those righteous men.",
        "İnsanlar İblis'in görüşünü beğendiler; salihlerin resimlerini yaptılar ve her gün bu resimlere bakar oldular; onları gördüklerinde o salihleri anarlardı.", [
  tok("وَأُعْجِبَ", "ujiba", "verb", [AT, NF, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُعْجِبَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and were pleased» — the passive uʿjiba («was made to admire»).", "«ve hoşlandılar» — meçhul u'cibe («beğendirildi»).", segments=wa_("أُعْجِبَ", "ujiba", "verb")),
  tok("النَّاسُ", "nas", "noun", [NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«the people» — the deputy of the doer.", "«insanlar» — nâib-i fâil."),
  tok("بِرَأْيِ", "ray", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَرَأْيِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«with the opinion [of]» — bi + the annexed noun.", "«görüşünden» — bi + muzâf isim.", segments=[seg("بِ", "bi", "prep"), seg("رَأْيِ", "ray", "noun")]),
  tok("إِبْلِيسَ", "iblis", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Iblīs» — the mudaf ilayh; a foreign name, a diptote.", "«İblis'in» — muzâfun ileyh; yabancı özel isim, gayr-i munsarif."),
  mazi_pl("وَصَوَّرُوا", "sawwara", "«and they pictured»", "«ve resmettiler»", tags=[AT, "form-ii-verbs"], wa=True),
  salihin("الصَّالِحِينَ", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the righteous» — the object; naṣb by the yāʾ of the sound plural.", "«salihleri» — mef'ûl; cem-i müzekker sâlimin yâ'sıyla mansub.", tags=[MB]),
  kana_pl(),
  khamsa("يَنْظُرُونَ", "nazara", "«looked»", "«bakarlardı»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  prep("إِلَى", "ila", "«at»", "«-e»"),
  ishara("هٰذِهِ", "hadhihi", "jarr", "«these»", "«bu»"),
  tok("الصُّوَرِ", "sura", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ صُورَةٍ.", "«pictures» — the substitute of the demonstrative, in jarr.", "«resimlere» — ism-i işâretin bedeli, mecrur."),
  *kulla("يَوْمٍ", "yawm", "«day»", "«gün»", punct="،"),
  idha("وَإِذَا", wa=True),
  tok("رَأَوْهَا", "raa", "verb", ["idha-shartiyya", "naqis-verbs", MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ.", "«they saw them» — the defective māḍī on the group's wāw; the pronoun is its object.", "«onları gördüler» — cemaat vâvı üzere nâkıs mâzî; zamir mef'ûl.", segments=[seg("رَأَ", "raa", "verb"), seg("وْ", "pron-3mp", "pron"), seg("هَا", "pron-3fs", "pron")]),
  mazi_pl("ذَكَرُوا", "dhakara", "«they remembered»", "«andılar»", tags=["idha-shartiyya"]),
  tok("أُولٰئِكَ", "ulaika", "pron", ["asma-al-ishara", MB], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«those» — the demonstrative in the place of naṣb, the object.", "«o» — mahallen mef'ûl ism-i işâret."),
  salihin("الصَّالِحِينَ", "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the righteous» — the substitute of the demonstrative; naṣb by the yāʾ.", "«salihleri» — ism-i işâretin bedeli; yâ ile mansub.", tags=[BD], punct="."),
])
# ---------------------------------------------------------------- §6 مِنَ الصُّوَرِ إِلَى التَّمَاثِيلِ (print pp. 12–13)
sen("s9", "And they moved on from pictures to statues.", "Resimlerden heykellere geçtiler.", [
  mazi_pl("وَانْتَقَلُوا", "intaqala", "«and they moved on»", "«ve geçtiler»", tags=[AT, "form-viii-verbs"], wa=True),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its nūn takes a fatḥa before the hamzat al-waṣl.", "«-den» — nûnu vasıl hemzesinden önce fetha alır."),
  tok("الصُّوَرِ", "sura", "noun", [HJ, JT], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ صُورَةٍ.", "«pictures» — in jarr.", "«resimlerden» — mecrur."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("التَّمَاثِيلِ", "timthal", "noun", [HJ, JT], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تِمْثَالٍ (صِيغَةُ مُنْتَهَى الْجُمُوعِ، صُرِفَ لِلتَّعْرِيفِ بِأَلْ).", "«statues» — in jarr; a plural of the heaviest pattern, declined fully because of its article.", "«heykellere» — mecrur; müntehe'l-cumû' kalıbı, harf-i tarifle munsarif.", punct="."),
])
sen("s10", "They made many statues of the righteous and set them in their houses and in their mosques.",
        "Salihlerin pek çok heykelini yaptılar; onları evlerine ve mescitlerine koydular.", [
  mazi_pl("وَعَمِلُوا", "amila", "«and they made»", "«ve yaptılar»", tags=[AT], wa=True),
  tok("لِلصَّالِحِينَ", "salih", "noun", [HJ, JS], "اللَّامُ حَرْفُ جَرٍّ، وَالصَّالِحِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«of the righteous» — li + the sound plural, jarr by the yāʾ.", "«salihler için» — li + cem-i müzekker sâlim, yâ ile mecrur.", segments=[seg("لِ", "li", "prep"), seg("الصَّالِحِينَ", "salih", "noun")]),
  tok("تَمَاثِيلَ", "timthal", "noun", [MB, JT, MM], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعٌ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«statues» — the object; a diptote plural, no tanwīn.", "«heykeller» — mef'ûl; gayr-i munsarif çoğul, tenvinsiz."),
  naat("كَثِيرَةً", "kathir", "«many»", "«pek çok»", case="nasb", punct="،"),
  v_pl_pron("وَوَضَعُوهَا", "wadaa", "وَضَعُو", "هَا", "pron-3fs", "«and set them»", "«ve onları koydular»", wa=True, tags=["mithal-verbs"]),
  fi(),
  noun_pron("بُيُوتِهِمْ", "bayt", "بُيُوتِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — جَمْعُ بَيْتٍ.", "«their houses» — in jarr, annexed.", "«evlerine» — mecrur, muzâf.", tags=[HJ, ID, JT]),
  tok("وَفِي", "fi", "prep", [AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and in»", "«ve -de»", segments=wa_("فِي", "fi", "prep")),
  noun_pron("مَسَاجِدِهِمْ", "masjid", "مَسَاجِدِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — جَمْعُ مَسْجِدٍ، صُرِفَ لِلْإِضَافَةِ.", "«their mosques» — in jarr, annexed; the diptote plural declines fully when annexed.", "«mescitlerine» — mecrur, muzâf; gayr-i munsarif çoğul izâfetle munsarif olur.", tags=[HJ, ID, JT], punct="."),
])
sen("s11", "And they used to worship God, associating nothing with Him.", "Allah'a ibadet eder, O'na hiçbir şeyi ortak koşmazlardı.", [
  kana_pl(),
  khamsa("يَعْبُدُونَ", "abada", "«worshipped»", "«ibadet ederlerdi»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  allah_maful(),
  la_nafiya(),
  khamsa("يُشْرِكُونَ", "ashraka", "«associating»", "«ortak koşmazlardı»", tags=["la-nafiya", "form-iv-verbs", HL], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with Him»", "«O'na»"),
  maful_("شَيْئًا", "shay", "«anything»", "«hiçbir şeyi»", punct="."),
])
sen("s12", "And they knew that these were statues of the righteous,", "Bunların salihlerin heykelleri olduğunu bilirlerdi;", [
  kana_pl(),
  khamsa("يَعْرِفُونَ", "arafa", "«knew»", "«bilirlerdi»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  anna(obj_of="يَعْرِفُونَ"),
  tok("هٰذِهِ", "hadhihi", "pron", [IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«these» — the demonstrative; anna's ism.", "«bunlar» — ism-i işâret; enne'nin ismi."),
  tok("تَمَاثِيلُ", "timthal", "noun", [IW, JT, MM], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ فَلَا يُنَوَّنُ.", "«statues» — anna's khabar; a diptote, no tanwīn.", "«heykellerdir» — enne'nin haberi; gayr-i munsarif, tenvinsiz."),
  tok("لِلصَّالِحِينَ", "salih", "noun", [HJ, JS, NA], "اللَّامُ حَرْفُ جَرٍّ، وَالصَّالِحِينَ مَجْرُورٌ بِالْيَاءِ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِتَمَاثِيلَ.", "«of the righteous» — li + the sound plural; the phrase describes «statues».", "«salihlerin» — li + cem-i müzekker sâlim; terkip «heykeller»in sıfatı.", punct=".", segments=[seg("لِ", "li", "prep"), seg("الصَّالِحِينَ", "salih", "noun")]),
])
sen("s13", "and that these were stones that neither benefit them nor harm them nor provide for them; but they used to seek blessing from them and honour them, because they were statues of the righteous.",
        "ve bunların kendilerine ne fayda ne zarar veren ne de rızık veren taşlar olduğunu; fakat onlarla teberrük eder ve onları yüceltirlerdi, çünkü onlar salihlerin heykelleriydi.", [
  anna(wa=True, full="وَأَنَّ", obj_of="يَعْرِفُونَ"),
  tok("هٰذِهِ", "hadhihi", "pron", [IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.", "«these» — anna's ism.", "«bunlar» — enne'nin ismi."),
  tok("حِجَارَةٌ", "hijara", "noun", [IW, JT], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ حَجَرٍ.", "«stones» — anna's khabar; a plural of ḥajar.", "«taşlar» — enne'nin haberi; hacer'in çoğulu."),
  neg_pron("لَا تَنْفَعُهُمْ".replace(" ", " ") if False else "لَا", "la-nafiya", "", "", "", "", "", ) if False else la_nafiya(),
  tok("تَنْفَعُهُمْ", "nafaa", "verb", ["la-nafiya", "mudari-marfu", MB, "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ نَعْتٌ لِحِجَارَةٍ.", "«benefit them» — a muḍāriʿ with its object pronoun; the clause describes «stones».", "«onlara fayda verir» — mef'ûl zamirli muzâri; cümle «taşlar»ın sıfatı.", segments=[seg("تَنْفَعُ", "nafaa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  la_nafiya("وَلَا", wa=True),
  tok("تَضُرُّهُمْ", "darra", "verb", ["la-nafiya", "mudari-marfu", MB, "doubled-verbs", AT], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَهُمْ مَفْعُولٌ بِهِ.", "«harm them»", "«onlara zarar verir»", segments=[seg("تَضُرُّ", "darra", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  la_nafiya("وَلَا", wa=True),
  tok("تَرْزُقُهُمْ", "razaqa", "verb", ["la-nafiya", "mudari-marfu", MB, AT], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَهُمْ مَفْعُولٌ بِهِ.", "«provide for them»", "«onlara rızık verir»", segments=[seg("تَرْزُقُ", "razaqa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("وَلٰكِنَّهُمْ", "lakinna", "part", [IW, AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهُمْ ضَمِيرٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "«but they» — lākinna + its ism, the pronoun.", "«fakat onlar» — lâkinne + ismi olan zamir.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  kana_pl("كَانُوا", wa=False, khabar_note=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ"),
  khamsa("يَتَبَرَّكُونَ", "tabarraka", "«sought blessing»", "«teberrük ederlerdi»", tags=[KN, "form-v-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«from them»", "«onlarla»"),
  wa_group_pron("وَيُعَظِّمُونَهَا", "azzama", "يُعَظِّمُونَ", "هَا", "pron-3fs", "«honoured them»", "«onları yüceltirlerdi»", tags=["form-ii-verbs"], punct="،"),
  li_anna("لِأَنَّهَا", "هَا", "pron-3fs", "«because they»", "«çünkü onlar»"),
  tok("تَمَاثِيلُ", "timthal", "noun", [IW, JT, MM], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«statues» — anna's khabar; a diptote.", "«heykelleridir» — enne'nin haberi; gayr-i munsarif."),
  tok("لِلصَّالِحِينَ", "salih", "noun", [HJ, JS, NA], "اللَّامُ حَرْفُ جَرٍّ، وَالصَّالِحِينَ مَجْرُورٌ بِالْيَاءِ — نَعْتٌ لِتَمَاثِيلَ.", "«of the righteous» — li + the sound plural, describing «statues».", "«salihlerin» — li + cem-i müzekker sâlim, «heykeller»in sıfatı.", punct=".", segments=[seg("لِ", "li", "prep"), seg("الصَّالِحِينَ", "salih", "noun")]),
])
sen("s14", "These statues grew many among them, and their veneration grew.", "Bu heykeller aralarında çoğaldı ve onlara tazim çoğaldı.", [
  mazi_ta("وَكَثُرَتْ", "kathura", "«and grew many»", "«ve çoğaldı»", tags=[AT], wa=True),
  ishara("هٰذِهِ", "hadhihi", "raf", "«these»", "«bu»", tags=[FL]),
  tok("التَّمَاثِيلُ", "timthal", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«statues» — the substitute of the demonstrative, in rafʿ.", "«heykeller» — ism-i işâretin bedeli, merfû."),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«among them»", "«aralarında»", punct="،"),
  mazi("وَكَثُرَ", "kathura", "«and grew»", "«ve çoğaldı»", tags=[AT], hidden=None, wa=True),
  noun_pron("تَعْظِيمُهَا", "tazim", "تَعْظِيمُ", "هَا", "pron-3fs", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — مَصْدَرُ عَظَّمَ.", "«their veneration» — the doer, annexed; the masdar of Form II.", "«onlara tazim» — fâil, muzâf; tef'îl masdarı.", tags=[FL, ID, "masdar"], punct="."),
])
sen("s15", "And whenever a righteous man died among them, they made a statue for him and named it by his name.",
        "Aralarında salih bir adam öldüğünde ona bir heykel yapar ve ona onun adını verirlerdi.", [
  idha("وَإِذَا", wa=True),
  mazi("مَاتَ", "mata-die", "«died»", "«öldü»", tags=["idha-shartiyya", "hollow-verbs"], hidden=None),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«among them»", "«aralarında»"),
  fail("رَجُلٌ", "rajul", "«a man»", "«bir adam»"),
  naat("صَالِحٌ", "salih", "«righteous»", "«salih»", case="raf", tags=["ism-fail"]),
  mazi_pl("عَمِلُوا", "amila", "«they made»", "«yaptılar»", tags=["idha-shartiyya"]),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«ona»"),
  maful_("تِمْثَالًا", "timthal", "«a statue»", "«bir heykel»"),
  tok("وَسَمَّوْهُ", "samma", "verb", [AT, MB, "naqis-verbs", "form-ii-verbs", MX], "الْوَاوُ عَاطِفَةٌ، وَسَمَّوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«and named it» — the defective māḍī on the group's wāw; the pronoun is the first object.", "«ve ona ad verdiler» — cemaat vâvı üzere nâkıs mâzî; zamir birinci mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("سَمَّ", "samma", "verb"), seg("وْ", "pron-3mp", "pron"), seg("هُ", "pron-3ms", "pron")]),
  tok("بِاسْمِهِ", "ism", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَاسْمِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَوْضِعِ الْمَفْعُولِ الثَّانِي.", "«by his name» — bi + ism annexed to «his»; the phrase stands as the second object.", "«onun adıyla» — bi + «onun»a muzâf isim; terkip ikinci mef'ûl yerinde.", punct=".", segments=[seg("بِ", "bi", "prep"), seg("اسْمِ", "ism", "noun"), seg("هِ", "pron-3ms", "pron")]),
])

CAND = {
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1),
 "shaytan": G("shaytan", "شَيْطَان", "ش ط ن", "noun", "devil, Satan", "şeytan", 1, plural="شَيَاطِين"),
 "kayfa": G("kayfa", "كَيْفَ", None, "noun", "how", "nasıl", 1),
 "fa": G("fa", "فَ", None, "conj", "so, then", "bunun üzerine", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "huzn": G("huzn", "حُزْن", "ح ز ن", "noun", "grief, sorrow", "üzüntü, hüzün", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon; for", "üzerine; için", 1),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "severe, strong", "şiddetli, güçlü", 1),
 "ishtiyaq": G("ishtiyaq", "اِشْتِيَاق", "ش و ق", "noun", "longing, yearning (the masdar of Form VIII)", "özlem, iştiyak (iftiâl masdarı)", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e, -ye", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great, mighty", "büyük, azim", 1),
 "limadha": G("limadha", "لِمَاذَا", None, "part", "why", "neden, niçin", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not — the negating lā", "değil, -mez — nefiy lâ'sı", 1),
 "nazara": G("nazara", "نَظَرَ", "ن ظ ر", "verb", "to look (at: إِلَى)", "bakmak (ilâ: -e)", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, bütün", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "day", "gün", 1, plural="أَيَّام"),
 "sabil": G("sabil", "سَبِيل", "س ب ل", "noun", "way, path", "yol", 1, plural="سُبُل"),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that (masculine)", "o, şu (müzekker)", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already (before a māḍī)", "gerçekten (mâzîden önce)", 1),
 "mata-die": G("mata-die", "مَاتَ", "م و ت", "verb", "to die", "ölmek", 1),
 "amila": G("amila", "عَمِلَ", "ع م ل", "verb", "to do, to make", "yapmak, işlemek", 1),
 "sura": G("sura", "صُورَة", "ص و ر", "noun", "picture, image, form", "resim, suret", 1, plural="صُوَر"),
 "sabah": G("sabah", "صَبَاح", "ص ب ح", "noun", "morning", "sabah", 1),
 "ujiba": G("ujiba", "أُعْجِبَ", "ع ج ب", "verb", "to be pleased, to admire (the passive of أَعْجَبَ; with بِ)", "beğenmek, hoşlanmak (a'cebe'nin meçhulü; bi ile)", 1),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "ray": G("ray", "رَأْي", "ر أ ي", "noun", "opinion, view", "görüş, rey", 1, plural="آرَاء"),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "iblis": G("iblis", "إِبْلِيس", None, "propn", "Iblīs — Satan", "İblis — Şeytan", 1),
 "sawwara": G("sawwara", "صَوَّرَ", "ص و ر", "verb", "to picture, to depict (Form II)", "resmetmek, tasvir etmek (tef'îl)", 1),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous, good", "salih, iyi", 1, plural="صَالِحُونَ"),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "idha": G("idha", "إِذَا", None, "part", "when, if", "-dığı zaman, -ınca", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see; to see fit", "görmek; uygun görmek", 1),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to mention, to remember", "anmak, zikretmek", 1),
 "ulaika": G("ulaika", "أُولَئِكَ", None, "pron", "those", "onlar, şunlar", 1),
 "intaqala": G("intaqala", "انْتَقَلَ", "ن ق ل", "verb", "to move on, to be transferred (Form VIII)", "geçmek, intikal etmek (iftiâl)", 1),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "timthal": G("timthal", "تِمْثَال", "م ث ل", "noun", "statue", "heykel", 1, plural="تَمَاثِيل"),
 "kathir": G("kathir", "كَثِير", "ك ث ر", "noun", "many, much", "çok", 1),
 "wadaa": G("wadaa", "وَضَعَ", "و ض ع", "verb", "to put, to place", "koymak", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "house", "ev", 1, plural="بُيُوت"),
 "masjid": G("masjid", "مَسْجِد", "س ج د", "noun", "mosque", "mescit", 1, plural="مَسَاجِد"),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek, tapmak", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "ashraka": G("ashraka", "أَشْرَكَ", "ش ر ك", "verb", "to associate (a partner with God) (Form IV)", "ortak koşmak, şirk koşmak (if'âl)", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "thing", "şey", 1, plural="أَشْيَاء"),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know, to recognize", "bilmek, tanımak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (after a verb of knowing or saying)", "ki (bilme ve söyleme fiillerinden sonra)", 1),
 "hijara": G("hijara", "حِجَارَة", "ح ج ر", "noun", "stones (a plural of حَجَر)", "taşlar (hacer'in çoğulu)", 1),
 "nafaa": G("nafaa", "نَفَعَ", "ن ف ع", "verb", "to benefit", "fayda vermek", 1),
 "darra": G("darra", "ضَرَّ", "ض ر ر", "verb", "to harm (doubled)", "zarar vermek (muzâaf)", 1),
 "razaqa": G("razaqa", "رَزَقَ", "ر ز ق", "verb", "to provide for, to give sustenance", "rızık vermek", 1),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but (a sister of inna)", "fakat (inne'nin kız kardeşi)", 1),
 "tabarraka": G("tabarraka", "تَبَرَّكَ", "ب ر ك", "verb", "to seek blessing (from: بِ) (Form V)", "teberrük etmek, bereket ummak (bi: -den) (tefa''ul)", 1),
 "azzama": G("azzama", "عَظَّمَ", "ع ظ م", "verb", "to honour, to magnify (Form II)", "yüceltmek, tazim etmek (tef'îl)", 1),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, to grow numerous", "çoğalmak, çok olmak", 1),
 "tazim": G("tazim", "تَعْظِيم", "ع ظ م", "noun", "veneration, honouring (the masdar of Form II)", "tazim, yüceltme (tef'îl masdarı)", 1),
 "rajul": G("rajul", "رَجُل", "ر ج ل", "noun", "man", "adam, erkek", 1, plural="رِجَال"),
 "samma": G("samma", "سَمَّى", "س م و", "verb", "to name (Form II, defective)", "ad vermek, isimlendirmek (tef'îl, nâkıs)", 1),
 "ism": G("ism", "اِسْم", "س م و", "noun", "name", "ad, isim", 1, plural="أَسْمَاء"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (masculine plural, attached)", "siz / sizin (bitişik)", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "she / it / her (attached)", "o / onun (bitişik)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tabarraka", _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَرَّك", "تَبَرَّك", "تَبَرَّك", "تَبَرُّك", "مُتَبَرِّك", None, None, None, "تَبَرَّكَ بِالشَّيْءِ: طَلَبَ الْبَرَكَةَ بِهِ — لَازِمٌ يَتَعَدَّى بِالْبَاءِ."))
if "ujiba" not in mo["verbs"] and has_morph("ajaba-please"): mo["verbs"]["ujiba"] = find_morph("ajaba-please")   # the passive of أَعْجَبَ shares its paradigm
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch3 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 3 (print pp. 11–13; Nūḥ §5–6): pictures of the righteous — «how is your grief? your longing? why not look at them every day? make pictures» — the people picture the righteous and look at them daily (s1–s8); "
          "from pictures to statues — many statues in houses and mosques; they still worship God alone and know these are stones that neither help nor harm, yet seek blessing from them; when a righteous man dies they make him a statue with his name (s9–s15). One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" Üçüncü bölüm (basılı s. 11–13; Nûh §5–6): salihlerin resimleri — «üzüntünüz nasıl? özleminiz? neden her gün bakmıyorsunuz? resim yapın» — halk salihleri resmeder ve her gün bakar (s1–s8); "
          "resimlerden heykellere — evlerde ve mescitlerde çok heykel; hâlâ yalnız Allah'a ibadet eder, bunların fayda ve zarar vermeyen taşlar olduğunu bilir, yine de onlarla teberrük ederler; salih biri ölünce ona adıyla bir heykel yaparlar (s9–s15). Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(3, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §5–6, pp. 11–13", GLOSS_ADD, notes=(), related=())
report(3, S, GLOSS_ADD, ())
