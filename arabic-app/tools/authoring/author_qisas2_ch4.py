# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 45: «قِصَّةُ عِيسَى» §42 (from an obscure creed to open idolatry — Europe, the Greeks and the Romans, Constantine; the author's footnote; the straying road; al-Fātiḥa 1:6–7; the tragedy of Europe; «to God belongs the command before and after»). Print pp. 68–70 — the END of the book's text.
python3 tools/authoring/author_qisas4_ch45.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas2_common import *
import qisas2_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "سَفِينَةُ نُوحٍ: مِنَ التَّمَاثِيلِ إِلَى الْأَصْنَامِ — غَضَبُ اللهِ", "en": "The ship of Nūḥ: from statues to idols — the anger of God", "tr": "Nûh'un gemisi: heykellerden putlara — Allah'ın gazabı"}
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

# ---------------------------------------------------------------- §7 مِنَ التَّمَاثِيلِ إِلَى الْأَصْنَامِ (print pp. 13–14)
sen("s1", "And these passed away; and the children saw their fathers seeking blessing from them, and saw their fathers honouring them with great honour.",
        "Bunlar da geçip gitti; çocuklar babalarını onlarla teberrük ederken gördüler ve babalarını onları büyük bir tazimle yüceltirken gördüler.", [
  mazi("وَمَضَى", "mada", "«and passed away»", "«ve geçip gitti»", tags=[AT, "naqis-verbs"], hidden=None, wa=True),
  ishara("هٰؤُلَاءِ", "haulai", "raf", "«these»", "«bunlar»", tags=[FL], punct="،"),
  mazi("وَرَأَى", "raa", "«and saw»", "«ve gördü»", tags=[AT, "naqis-verbs"], hidden=None, wa=True),
  fail("الْأَوْلَادُ", "walad", "«the children»", "«çocuklar»", tags=[JT]),
  abahum("مَفْعُولٌ بِهِ أَوَّلُ", "«their fathers» — the first object, annexed.", "«babalarını» — birinci mef'ûl, muzâf."),
  khamsa("يَتَبَرَّكُونَ", "tabarraka", "«seeking blessing»", "«teberrük ederken»", tags=[HL, "form-v-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ (رَأَى الْبَصَرِيَّةُ)"),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«from them»", "«onlarla»"),
  tok("وَرَأَوْا", "raa", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَأَوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ، وَالْوَاوُ فَاعِلٌ.", "«and they saw» — the defective māḍī before the group's wāw.", "«ve gördüler» — cemaat vâvından önce nâkıs mâzî.", segments=[seg("وَ", "wa", "conj"), seg("رَأَ", "raa", "verb"), seg("وْا", "pron-3mp", "pron")]),
  abahum("مَفْعُولٌ بِهِ أَوَّلُ", "«their fathers» — the first object, annexed.", "«babalarını» — birinci mef'ûl, muzâf."),
  group_pron("يُعَظِّمُونَهَا", "azzama", "يُعَظِّمُونَ", "هَا", "pron-3fs", "«honouring them»", "«onları yüceltirken»", " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", tags=[HL, "form-ii-verbs"]),
  tok("تَعْظِيمًا", "tazim", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«an honouring» — the mafʿūl muṭlaq.", "«bir tazimle» — mef'ûl-i mutlak."),
  naat("شَدِيدًا", "shadid", "«great»", "«büyük»", case="nasb", punct="."),
])
sen("s2", "And they used to see them kissing these statues, touching them and praying by them.",
        "Onları bu heykelleri öperken, onlara dokunurken ve yanlarında dua ederken görürlerdi.", [
  kana_pl(),
  yarawnahum(),
  khamsa("يُقَبِّلُونَ", "qabbala", "«kissing»", "«öperken»", tags=[HL, "form-ii-verbs"], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ (أَوْ حَالٌ)"),
  ishara("هٰذِهِ", "hadhihi", "nasb", "«these»", "«bu»"),
  tok("التَّمَاثِيلَ", "timthal", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«statues» — the substitute of the demonstrative, in naṣb.", "«heykelleri» — ism-i işâretin bedeli, mansub.", punct="،"),
  group_pron("وَيَلْمِسُونَهَا", "lamasa", "يَلْمِسُونَ", "هَا", "pron-3fs", "«touching them»", "«onlara dokunurken»", "", wa=True),
  khamsa("وَيَدْعُونَ", "daa", "«and praying»", "«ve dua ederken»", tags=[AT, "naqis-verbs"], wa=True),
  indaha(punct="."),
])
sen("s3", "And they used to see them lowering their heads and bowing by them;",
        "Onları başlarını eğerken ve yanlarında rükû ederken görürlerdi;", [
  kana_pl(),
  yarawnahum(),
  khamsa("يَخْفِضُونَ", "khafada", "«lowering»", "«eğerken»", tags=[HL], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ (أَوْ حَالٌ)"),
  noun_pron("رُؤُوسَهُمْ", "ras", "رُؤُوسَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ رَأْسٍ.", "«their heads» — the object, annexed.", "«başlarını» — mef'ûl, muzâf.", tags=[MB, ID, JT]),
  khamsa("وَيَرْكَعُونَ", "rakaa", "«and bowing»", "«ve rükû ederken»", tags=[AT], wa=True),
  indaha(),
])
sen("s4", "so the sons went beyond the fathers, and came to prostrate to them.",
        "böylece oğullar babaları aştı ve onlara secde eder oldular.", [
  mazi("فَزَادَ", "zada", "«so went beyond»", "«böylece aştı»", tags=[AT, "hollow-verbs"], hidden=None, wa=True),
  fail("الْأَبْنَاءُ", "ibn", "«the sons»", "«oğullar»", tags=[JT], extra_ar=" — جَمْعُ ابْنٍ"),
  prep("عَلَى", "ala", "«over»", "«-i»"),
  tok("الْآبَاءِ", "ab", "noun", [HJ, JT], "مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ أَبٍ.", "«the fathers» — in jarr; a plural of ab.", "«babaları» — mecrur; eb'in çoğulu.", punct="،"),
  saru(),
  khamsa("يَسْجُدُونَ", "sajada", "«prostrate»", "«secde ederler»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ"),
  li_pron("لَهَا", "هَا", "pron-3fs", "«to them»", "«onlara»", punct="."),
])
sen("s5", "And they came to ask them and to slaughter for them.", "Onlardan ister ve onlar için kurban keser oldular.", [
  saru(),
  group_pron("يَسْأَلُونَهَا", "saala", "يَسْأَلُونَ", "هَا", "pron-3fs", "«ask them»", "«onlardan isterler»", " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ", tags=[KN], punct="،"),
  khamsa("وَيَذْبَحُونَ", "dhabaha", "«and slaughter»", "«ve kurban keserler»", tags=[AT], wa=True),
  li_pron("لَهَا", "هَا", "pron-3fs", "«for them»", "«onlar için»", punct="."),
])
sen("s6", "And thus these idols became gods, and the people came to worship them as they used to worship God before.",
        "Böylece bu putlar ilâhlar oldu; insanlar, önceden Allah'a ibadet ettikleri gibi onlara ibadet eder oldular.", [
  tok("وَهٰكَذَا", "hakadha", "pron", [AT], "الْوَاوُ عَاطِفَةٌ، وَهٰكَذَا: هَا لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ — أَيْ: عَلَى هٰذَا النَّحْوِ.", "«and thus» — hā of alerting + the kāf of likeness + the demonstrative: «in this way».", "«ve böylece» — tenbih hâ'sı + teşbih kâfı + ism-i işâret: «bu şekilde».", segments=wa_("هٰكَذَا", "hakadha", "pron")),
  tok("صَارَتْ", "sara", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«became» — ṣāra with the feminine tāʾ.", "«oldu» — te'nis tâlı sâra."),
  tok("هٰذِهِ", "hadhihi", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُ صَارَ.", "«these» — the demonstrative; ṣāra's ism.", "«bu» — ism-i işâret; sâra'nın ismi."),
  tok("الْأَصْنَامُ", "sanam", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ صَنَمٍ.", "«idols» — the substitute of the demonstrative, in rafʿ.", "«putlar» — ism-i işâretin bedeli, merfû."),
  tok("آلِهَةً", "ilah", "noun", [KN, JT], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ إِلٰهٍ.", "«gods» — ṣāra's khabar; a plural of ilāh.", "«ilâhlar» — sâra'nın haberi; ilâh'ın çoğulu.", punct="،"),
  tok("وَصَارَ", "sara", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَصَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ.", "«and came to» — ṣāra, a sister of kāna.", "«ve … oldu» — kâne'nin kız kardeşi sâra.", segments=wa_("صَارَ", "sara", "verb")),
  ism_kana("النَّاسُ", "nas", "«the people»", "«insanlar»", ar="اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ."),
  group_pron("يَعْبُدُونَهَا", "abada", "يَعْبُدُونَ", "هَا", "pron-3fs", "«worship them»", "«onlara ibadet ederler»", " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ", tags=[KN]),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا مَصْدَرِيَّةٌ — أَيْ: كَعِبَادَتِهِمُ اللهَ.", "«as» — the kāf of likeness + the masdar-making mā.", "«gibi» — teşbih kâfı + masdar mâ'sı.", segments=[seg("كَ", "ka", "prep"), seg("مَا", "ma-masdariyya", "part")]),
  kana_pl("كَانُوا", wa=False),
  khamsa("يَعْبُدُونَ", "abada", "«they worshipped»", "«ibadet ederlerdi»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ"),
  allah_maful(),
  prep("مِنْ", "min", "«from»", "«-den»"),
  tok("قَبْلُ", "qablu", "noun", [HJ, MF], "ظَرْفٌ مَقْطُوعٌ عَنِ الْإِضَافَةِ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ.", "«before» — the adverb cut from its annexation, built on ḍamma, in the place of jarr.", "«önce» — izâfetten kesilmiş zarf, zamme üzere mebnî, mahallen mecrur.", punct="."),
])
sen("s7", "And these gods grew many among them: this one is Wadd, that one Suwāʿ, this one Yaghūth, that one Yaʿūq, and this one Nasr.",
        "Bu ilâhlar aralarında çoğaldı: bu Vedd, şu Suvâ', bu Yegûs, şu Ye'ûk, bu da Nesr.", [
  mazi_ta("وَكَثُرَتْ", "kathura", "«and grew many»", "«ve çoğaldı»", tags=[AT], wa=True),
  ishara("هٰذِهِ", "hadhihi", "raf", "«these»", "«bu»", tags=[FL]),
  tok("الْآلِهَةُ", "ilah", "noun", [BD, JT], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ إِلٰهٍ.", "«gods» — the substitute of the demonstrative, in rafʿ.", "«ilâhlar» — ism-i işâretin bedeli, merfû."),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«among them»", "«aralarında»", punct="،"),
  ishara("هٰذَا", "hadha", "raf", "«this»", "«bu»", tags=[MK]),
  idol("وَدٌّ", "wadd", "«Wadd»", "«Vedd»", punct="،"),
  wa_ishara("وَذٰلِكَ", "dhalika", "«that»", "«şu»"),
  idol("سُوَاعٌ", "suwa-idol", "«Suwāʿ»", "«Suvâ'»", punct="،"),
  wa_ishara("وَهٰذَا", "hadha", "«this»", "«bu»"),
  idol("يَغُوثُ", "yaghuth", "«Yaghūth»", "«Yegûs»", punct="،", mamnu=True),
  wa_ishara("وَذٰلِكَ", "dhalika", "«that»", "«şu»"),
  idol("يَعُوقُ", "yauq", "«Yaʿūq»", "«Ye'ûk»", punct="،", mamnu=True),
  wa_ishara("وَهٰذَا", "hadha", "«this»", "«bu»"),
  idol("نَسْرٌ", "nasr-idol", "«Nasr»", "«Nesr»", punct="."),
])
# ---------------------------------------------------------------- §8 غَضَبُ اللهِ (print pp. 14–15)
sen("s8", "And God was angry with the people with a great anger, and cursed them.", "Allah insanlara şiddetle gazap etti ve onları lânetledi.", [
  mazi("وَغَضِبَ", "ghadiba", "«and was angry»", "«ve gazap etti»", tags=[AT], hidden=None, wa=True),
  allah_fail(),
  prep("عَلَى", "ala", "«with»", "«-e»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlara»"),
  tok("غَضَبًا", "ghadab", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«an anger» — the mafʿūl muṭlaq.", "«bir gazapla» — mef'ûl-i mutlak."),
  naat("شَدِيدًا", "shadid", "«great»", "«şiddetli»", case="nasb"),
  v_pron("وَلَعَنَهُمْ", "laana", "لَعَنَ", "هُمْ", "pron-3mp", "«and cursed them»", "«ve onları lânetledi»", wa=True, hidden=None, punct="."),
])
sen("s9", "And why should God not be angry with the people and not curse them?", "Allah insanlara neden gazap etmesin ve onları neden lânetlemesin?", [
  tok("وَلِمَاذَا", "limadha", "part", [IS, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمَاذَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«and why» — li + mādhā, the question word in the place of jarr.", "«peki neden» — li + mâzâ, mahallen mecrur soru ismi.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مَاذَا", "limadha", "part")]),
  la_nafiya(),
  tok("يَغْضَبُ", "ghadiba", "verb", ["la-nafiya", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«be angry» — a muḍāriʿ in rafʿ after the negating lā.", "«gazap etsin» — nefiy lâ'sından sonra merfû muzâri."),
  allah_fail(),
  prep("عَلَى", "ala", "«with»", "«-e»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlara»"),
  la_nafiya("وَلَا", wa=True),
  tok("يَلْعَنُهُمْ", "laana", "verb", ["la-nafiya", "mudari-marfu", MB, AT], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«curse them» — the muḍāriʿ with its object pronoun.", "«onları lânetlesin» — mef'ûl zamirli muzâri.", punct="؟", segments=[seg("يَلْعَنُ", "laana", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
])
sen("s10", "Was it for this that He created them? Is it for this that He provides for them?", "Onları bunun için mi yarattı? Onlara bunun için mi rızık veriyor?", [
  a_li_hadha("خَلَقَهُمْ"),
  v_pron("خَلَقَهُمْ", "khalaqa", "خَلَقَ", "هُمْ", "pron-3mp", "«He created them»", "«onları yarattı»", punct="،"),
  a_li_hadha("يَرْزُقُهُمْ"),
  tok("يَرْزُقُهُمْ", "razaqa", "verb", ["mudari-marfu", MB], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«He provides for them» — the muḍāriʿ with its object pronoun.", "«onlara rızık verir» — mef'ûl zamirli muzâri.", punct="؟", segments=[seg("يَرْزُقُ", "razaqa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
])
sen("s11", "They walk on God's earth and disbelieve in God!", "Allah'ın yeryüzünde yürüyor ve Allah'ı inkâr ediyorlar!", [
  khamsa("يَمْشُونَ", "masha", "«they walk»", "«yürüyorlar»", tags=["naqis-verbs"], extra_ar=" (حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ: يَمْشِي + ونَ)"),
  prep("عَلَى", "ala", "«on»", "«üzerinde»"),
  majrur("أَرْضِ", "ard", "«the earth [of]»", "«yeryüzünde»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  allah_mi(),
  khamsa("وَيَكْفُرُونَ", "kafara", "«and disbelieve»", "«ve inkâr ediyorlar»", tags=[AT], wa=True),
  billah(punct="!"),
])
sen("s12", "They eat God's provision and associate partners with God!", "Allah'ın rızkını yiyor ve Allah'a ortak koşuyorlar!", [
  khamsa("وَيَأْكُلُونَ", "akala", "«and they eat»", "«ve yiyorlar»", tags=[AT], wa=True),
  maful_("رِزْقَ", "rizq", "«the provision [of]»", "«rızkını»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  allah_mi(),
  khamsa("وَيُشْرِكُونَ", "ashraka", "«and associate»", "«ve ortak koşuyorlar»", tags=[AT, "form-iv-verbs"], wa=True),
  billah(punct="!"),
])
sen("s13", "This is a great wrong! This is a great wrong!", "Bu büyük bir zulümdür! Bu büyük bir zulümdür!", [
  *inna_hadha_zulm("!"),
  *inna_hadha_zulm("!"),
])
sen("s14", "God was angry with the people: He withheld the rain and made things hard for them; the crops grew few and the offspring grew few.",
        "Allah insanlara gazap etti: yağmuru tuttu ve onları darlığa soktu. Ekin azaldı, nesil azaldı.", [
  mazi("غَضِبَ", "ghadiba", "«was angry»", "«gazap etti»", hidden=None),
  allah_fail(),
  prep("عَلَى", "ala", "«with»", "«-e»"),
  majrur("النَّاسِ", "nas", "«the people»", "«insanlara»", punct="،"),
  mazi("وَحَبَسَ", "habasa", "«and withheld»", "«ve tuttu»", tags=[AT], wa=True),
  maful_("الْمَطَرَ", "matar", "«the rain»", "«yağmuru»"),
  mazi("وَضَيَّقَ", "dayyaqa", "«and made [things] hard»", "«ve darlığa soktu»", tags=[AT, "form-ii-verbs"], wa=True),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«for them»", "«onlara»", punct="."),
  mazi("وَقَلَّ", "qalla", "«and grew few»", "«ve azaldı»", tags=[AT, "doubled-verbs"], hidden=None, wa=True),
  fail("الْحَرْثُ", "harth", "«the crops»", "«ekin»"),
  mazi("وَقَلَّ", "qalla", "«and grew few»", "«ve azaldı»", tags=[AT, "doubled-verbs"], hidden=None, wa=True),
  fail("النَّسْلُ", "nasl-offspring", "«the offspring»", "«nesil»", punct="."),
])
sen("s15", "But the people did not understand; but the people did not repent.", "Fakat insanlar akıllanmadı; fakat insanlar tövbe etmedi.", [
  *lakinna_nas_ma("عَقَلُوا", "aqala", "«they understood»", "«akıllandılar»", "،"),
  *lakinna_nas_ma("تَابُوا", "taba-repent", "«they repented»", "«tövbe ettiler»", ".", tags=["hollow-verbs"]),
])

CAND = {
 "mada": G("mada", "مَضَى", "م ض ي", "verb", "to pass, to go by (defective)", "geçmek, geçip gitmek (nâkıs)", 1),
 "haulai": G("haulai", "هَؤُلَاءِ", None, "pron", "these", "bunlar", 1),
 "raa": G("raa", "رَأَى", "ر أ ي", "verb", "to see; to see fit", "görmek; uygun görmek", 1),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "child, son", "çocuk, oğul", 1, plural="أَوْلَاد"),
 "ab": G("ab", "أَب", "أ ب و", "noun", "father", "baba", 1, plural="آبَاء"),
 "tabarraka": G("tabarraka", "تَبَرَّكَ", "ب ر ك", "verb", "to seek blessing (from: بِ) (Form V)", "teberrük etmek, bereket ummak (bi: -den) (tefa''ul)", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "azzama": G("azzama", "عَظَّمَ", "ع ظ م", "verb", "to honour, to magnify (Form II)", "yüceltmek, tazim etmek (tef'îl)", 1),
 "tazim": G("tazim", "تَعْظِيم", "ع ظ م", "noun", "veneration, honouring (the masdar of Form II)", "tazim, yüceltme (tef'îl masdarı)", 1),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "severe, strong", "şiddetli, güçlü", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be, was", "olmak, idi", 1),
 "qabbala": G("qabbala", "قَبَّلَ", "ق ب ل", "verb", "to kiss (Form II)", "öpmek (tef'îl)", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "timthal": G("timthal", "تِمْثَال", "م ث ل", "noun", "statue", "heykel", 1, plural="تَمَاثِيل"),
 "lamasa": G("lamasa", "لَمَسَ", "ل م س", "verb", "to touch", "dokunmak", 1),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call; to pray", "çağırmak; dua etmek", 1),
 "inda": G("inda", "عِنْد", None, "adv", "at, by, with (the possessive «at»)", "yanında, -de", 1),
 "khafada": G("khafada", "خَفَضَ", "خ ف ض", "verb", "to lower", "indirmek, eğmek", 1),
 "ras": G("ras", "رَأْس", "ر أ س", "noun", "head", "baş, kafa", 1, plural="رُؤُوس"),
 "rakaa": G("rakaa", "رَكَعَ", "ر ك ع", "verb", "to bow (in worship)", "rükû etmek, eğilmek", 1),
 "zada": G("zada", "زَادَ", "ز ي د", "verb", "to increase, to exceed (hollow)", "artmak, aşmak (ecvef)", 1),
 "ibn": G("ibn", "ابْن", "ب ن و", "noun", "son", "oğul", 1, plural="بَنُونَ"),
 "ala": G("ala", "عَلَى", None, "prep", "on, upon; over", "üzerine; -e", 1),
 "sara": G("sara", "صَارَ", "ص ي ر", "verb", "to become (a sister of kāna, hollow)", "olmak, … hâline gelmek (kâne'nin kız kardeşi, ecvef)", 1),
 "sajada": G("sajada", "سَجَدَ", "س ج د", "verb", "to prostrate", "secde etmek", 1),
 "li": G("li", "لِ", None, "prep", "to, for", "-e, için", 1),
 "saala": G("saala", "سَأَلَ", "س أ ل", "verb", "to ask", "sormak, istemek", 1),
 "dhabaha": G("dhabaha", "ذَبَحَ", "ذ ب ح", "verb", "to slaughter", "boğazlamak, kurban kesmek", 1),
 "hakadha": G("hakadha", "هٰكَذَا", None, "pron", "thus, in this way", "böylece, bu şekilde", 1),
 "sanam": G("sanam", "صَنَم", "ص ن م", "noun", "idol", "put", 1, plural="أَصْنَام"),
 "ilah": G("ilah", "إِلَه", "أ ل ه", "noun", "god, deity", "ilâh, tanrı", 1, plural="آلِهَة"),
 "nas": G("nas", "نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "ibadet etmek, tapmak", 1),
 "kama": G("kama", "كَمَا", None, "part", "as, just as", "gibi, … -dığı gibi", 1),
 "ka": G("ka", "كَـ", None, "prep", "like, as (the kāf of likeness)", "gibi (teşbih kâfı)", 1),
 "ma-masdariyya": G("ma-masdariyya", "مَا (الْمَصْدَرِيَّة)", None, "part", "the masdar-making mā", "masdar mâ'sı", 1),
 "allah": G("allah", "الله", None, "propn", "Allah, God", "Allah", 1),
 "min": G("min", "مِنْ", None, "prep", "from", "-den", 1),
 "qablu": G("qablu", "قَبْلُ", "ق ب ل", "noun", "before (cut from its annexation: مِنْ قَبْلُ)", "önce (izâfetten kesilmiş: min kablü)", 1),
 "kathura": G("kathura", "كَثُرَ", "ك ث ر", "verb", "to be many, to grow numerous", "çoğalmak, çok olmak", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this (masculine)", "bu (müzekker)", 1),
 "wadd": G("wadd", "وَدّ", None, "propn", "Wadd — an idol of the people of Nūḥ (71:23)", "Vedd — Nûh kavminin bir putu (71:23)", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that (masculine)", "o, şu (müzekker)", 1),
 "suwa-idol": G("suwa-idol", "سُوَاع", None, "propn", "Suwāʿ — an idol of the people of Nūḥ (71:23)", "Suvâ' — Nûh kavminin bir putu (71:23)", 1),
 "yaghuth": G("yaghuth", "يَغُوث", None, "propn", "Yaghūth — an idol of the people of Nūḥ (71:23)", "Yegûs — Nûh kavminin bir putu (71:23)", 1),
 "yauq": G("yauq", "يَعُوق", None, "propn", "Yaʿūq — an idol of the people of Nūḥ (71:23)", "Ye'ûk — Nûh kavminin bir putu (71:23)", 1),
 "nasr-idol": G("nasr-idol", "نَسْر", None, "propn", "Nasr — an idol of the people of Nūḥ (71:23)", "Nesr — Nûh kavminin bir putu (71:23)", 1),
 "ghadiba": G("ghadiba", "غَضِبَ", "غ ض ب", "verb", "to be angry (with: عَلَى)", "gazap etmek, kızmak (alâ: -e)", 1),
 "ghadab": G("ghadab", "غَضَب", "غ ض ب", "noun", "anger", "gazap, öfke", 1),
 "laana": G("laana", "لَعَنَ", "ل ع ن", "verb", "to curse", "lânetlemek", 1),
 "limadha": G("limadha", "لِمَاذَا", None, "part", "why", "neden, niçin", 1),
 "la-nafiya": G("la-nafiya", "لَا (النَّافِيَة)", None, "part", "not — the negating lā", "değil, -mez — nefiy lâ'sı", 1),
 "a-istifham": G("a-istifham", "أَ", None, "part", "the interrogative hamza («…?»)", "istifham hemzesi («… mi?»)", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create", "yaratmak", 1),
 "razaqa": G("razaqa", "رَزَقَ", "ر ز ق", "verb", "to provide for, to give sustenance", "rızık vermek", 1),
 "masha": G("masha", "مَشَى", "م ش ي", "verb", "to walk (defective)", "yürümek (nâkıs)", 1),
 "ard": G("ard", "أَرْض", "أ ر ض", "noun", "earth, land", "yer, toprak", 1, plural="أَرَضُونَ / أَرَاضٍ"),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve (in: بِ)", "inkâr etmek, küfretmek (bi: -i)", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "rizq": G("rizq", "رِزْق", "ر ز ق", "noun", "provision, sustenance", "rızık", 1, plural="أَرْزَاق"),
 "ashraka": G("ashraka", "أَشْرَكَ", "ش ر ك", "verb", "to associate (a partner with God) (Form IV)", "ortak koşmak, şirk koşmak (if'âl)", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed — the emphasizing particle", "şüphesiz — tekid harfi", 1),
 "zulm": G("zulm", "ظُلْم", "ظ ل م", "noun", "wrong, injustice", "zulüm, haksızlık", 1),
 "la-ibtida": G("la-ibtida", "لَ", None, "part", "the lām of emphasis (lām al-ibtidāʾ)", "tekid lâmı (lâm-ı ibtidâ)", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great, mighty", "büyük, azim", 1),
 "habasa": G("habasa", "حَبَسَ", "ح ب س", "verb", "to withhold, to confine", "tutmak, hapsetmek", 1),
 "matar": G("matar", "مَطَر", "م ط ر", "noun", "rain", "yağmur", 1, plural="أَمْطَار"),
 "dayyaqa": G("dayyaqa", "ضَيَّقَ", "ض ي ق", "verb", "to make narrow, to make things hard (for: عَلَى) (Form II)", "daraltmak, darlığa sokmak (alâ: -e) (tef'îl)", 1),
 "qalla": G("qalla", "قَلَّ", "ق ل ل", "verb", "to be few, to diminish (doubled)", "azalmak, az olmak (muzâaf)", 1),
 "harth": G("harth", "حَرْث", "ح ر ث", "noun", "tillage, crops", "ekin, ziraat", 1),
 "nasl-offspring": G("nasl-offspring", "نَسْل", "ن س ل", "noun", "offspring, progeny", "nesil, soy", 1),
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but (a sister of inna)", "fakat (inne'nin kız kardeşi)", 1),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not — the negating mā", "değil, -medi — nefiy mâ'sı", 1),
 "aqala": G("aqala", "عَقَلَ", "ع ق ل", "verb", "to understand, to use reason", "akıl etmek, anlamak", 1),
 "taba-repent": G("taba-repent", "تَابَ", "ت و ب", "verb", "to repent (hollow)", "tövbe etmek (ecvef)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "he / him / his (attached)", "o / onun (bitişik)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "they / their (masculine plural, attached)", "onlar / onların (bitişik)", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "she / it / her (attached)", "o / onun (bitişik)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "qabbala", _sg.derived(_sg.B2, _sg.W2, "ُ", "قَبَّل", "قَبِّل", "قَبِّل", "تَقْبِيل", "مُقَبِّل", "مُقَبَّل", "قُبِّلَ", "يُقَبَّلُ", "قَبَّلَهُ: لَثَمَهُ."))
put_morph(mo, "lamasa", _sg.sound1("daraba", "لَمَس", "لْمِس", "اِلْمِس", "لَمْس", "لَامِس", "مَلْمُوس", "لُمِسَ", "يُلْمَسُ", "لَمَسَهُ يَلْمِسُهُ: مَسَّهُ بِيَدِهِ."))
put_morph(mo, "khafada", _sg.sound1("daraba", "خَفَض", "خْفِض", "اِخْفِض", "خَفْض", "خَافِض", "مَخْفُوض", "خُفِضَ", "يُخْفَضُ", "خَفَضَ رَأْسَهُ يَخْفِضُهُ: أَنْزَلَهُ؛ ضِدُّ رَفَعَ."))
put_morph(mo, "rakaa", _sg.sound1("fataha", "رَكَع", "رْكَع", "اِرْكَع", "رُكُوع", "رَاكِع", None, None, None, "رَكَعَ يَرْكَعُ: انْحَنَى — لَازِمٌ."))
put_morph(mo, "dayyaqa", _sg.derived(_sg.B2, _sg.W2, "ُ", "ضَيَّق", "ضَيِّق", "ضَيِّق", "تَضْيِيق", "مُضَيِّق", "مُضَيَّق", "ضُيِّقَ", "يُضَيَّقُ", "ضَيَّقَ عَلَيْهِ: جَعَلَ عَيْشَهُ ضَيِّقًا."))
put_morph(mo, "taba-repent", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "تَاب", "تُب", "تُوب", "تُب", "تُب", "تُب", "تَوْبَة", "تَائِب", None, None, None, "تَابَ يَتُوبُ تَوْبَةً: رَجَعَ عَنِ الذَّنْبِ — لَازِمٌ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas2 ch4 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = (" Chapter 4 (print pp. 13–15; Nūḥ §7–8): from statues to idols — the children see their fathers kiss, touch, bow before the statues; the sons go further and prostrate, ask and slaughter; the statues become gods: Wadd, Suwāʿ, Yaghūth, Yaʿūq, Nasr (s1–s7); "
          "the anger of God — why not? they walk on His earth and disbelieve, eat His provision and associate partners; the rain withheld, crops and offspring grow few; but the people neither understood nor repented (s8–s15). One printed line is one sentence; the printed vowelling is kept.")
ADD_TR = (" Dördüncü bölüm (basılı s. 13–15; Nûh §7–8): heykellerden putlara — çocuklar babalarını heykelleri öperken, dokunurken, önünde eğilirken görür; oğullar ileri gidip secde eder, ister ve kurban keser; heykeller ilâh olur: Vedd, Suvâ', Yegûs, Ye'ûk, Nesr (s1–s7); "
          "Allah'ın gazabı — neden olmasın? O'nun yeryüzünde yürüyüp inkâr ediyor, rızkını yiyip ortak koşuyorlar; yağmur tutulur, ekin ve nesil azalır; fakat insanlar ne akıllandı ne tövbe etti (s8–s15). Basılı her satır bir cümledir; basılı hareke korunmuştur.")
write_out(4, S, TITLE, ADD_EN, ADD_TR, "Nūḥ §7–8, pp. 13–15", GLOSS_ADD, notes=(), related=())
report(4, S, GLOSS_ADD, ())
