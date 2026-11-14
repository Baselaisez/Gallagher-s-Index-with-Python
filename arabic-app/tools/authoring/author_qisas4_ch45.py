# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 45: «قِصَّةُ عِيسَى» §42 (from an obscure creed to open idolatry — Europe, the Greeks and the Romans, Constantine; the author's footnote; the straying road; al-Fātiḥa 1:6–7; the tragedy of Europe; «to God belongs the command before and after»). Print pp. 68–70 — the END of the book's text.
python3 tools/authoring/author_qisas4_ch45.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: مِنْ عَقِيدَةٍ غَامِضَةٍ إِلَى وَثَنِيَّةٍ سَافِرَةٍ — خَاتِمَةُ الْكِتَابِ (الفاتحة ٦–٧)", "en": "The story of ʿĪsā: from an obscure creed to open idolatry — the close of the book (1:6–7)", "tr": "Îsâ kıssası: kapalı bir akideden açık putperestliğe — kitabın sonu (Fâtiha 6–7)"}
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

# ---------------------------------------------------------------- §42 مِنْ عَقِيدَةٍ غَامِضَةٍ إِلَى وَثَنِيَّةٍ سَافِرَةٍ (print pp. 68–70)
def tu_mazi(full, lex, stem, en, tr, ar, tags=(), punct=None, obj=None, obj_lex=None, person="تُ", person_lex="pron-1s"):
    segs = ([seg(full[:2], "wa" if full[:2] == "وَ" else "fa", "conj")] if full[:2] in ("وَ", "فَ") else []) + [seg(stem, lex, "verb"), seg(person, person_lex, "pron")] + ([seg(obj, obj_lex, "pron")] if obj else [])
    return tok(full, lex, "verb", list(tags), ar, en, tr, punct=punct, segments=segs)
def kanat(full="وَكَانَتْ", ism_note="", punct=None):
    wa = full.startswith("وَ"); body = full[2:] if wa else full
    return tok(full, "kana", "verb", ([AT] if wa else []) + [KN, "hollow-verbs"], ("الْوَاوُ عَاطِفَةٌ، وَ" if wa else "") + body + " فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ" + ism_note + ".", ("«and» + " if wa else "") + "«was» — kāna with the feminine tāʾ.", ("«ve» + " if wa else "") + "«idi» — te'nis tâ'lı kâne.", punct=punct, segments=(conj_segs(full, "kana", "verb") if wa else None))
def li_noun_mk(full, lex, en, tr, punct=None, tags=()):
    return tok(full, lex, "noun", [HJ, MK] + list(tags), "اللَّامُ حَرْفُ جَرٍّ، وَ" + full[2:] + " مَجْرُورٌ بِالْكَسْرَةِ — خَبَرٌ مُقَدَّمٌ.", "«for» + " + en + " — the fronted khabar.", "«için» + " + tr + " — öne alınmış haber.", punct=punct, segments=[seg("لِ", "li", "prep"), seg(full[2:], lex, "noun")])
def ilah_mk(punct="،"): return tok("إِلٰهٌ", "ilah", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a god» — the delayed mubtadaʾ.", "«bir ilâh» — sonraya bırakılmış mübtedâ.", punct=punct)
sen("s1", "And the preachers of Christianity moved on to Europe by an impulse of their own (1);",
        "Hıristiyanlığın davetçileri, kendilerinden gelen bir saikle Avrupa'ya geçtiler (1);", [
  mazi("وَانْتَقَلَ", "intaqala", "«and moved on»", "«ve geçtiler»", tags=[AT, "form-viii-verbs"], hidden=None, wa=True),
  fail("دُعَاةُ", "dain", "«the preachers [of]»", "«davetçileri»", tags=[ID, JT], extra_ar="، مُضَافٌ — جَمْعُ دَاعٍ عَلَى فُعَلَةٍ"),
  mudaf_ilayh("الْمَسِيحِيَّةِ", "masihiyya", "«Christianity»", "«Hıristiyanlığın»", tags=["ism-mansub"]),
  prep("إِلَى", "ila", "«to»", "«-ya»"),
  tok("أُورُبَّا", "urubba", "propn", [HJ, MM], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ أَعْجَمِيٌّ.", "«Europe» — a foreign name; the ending hidden on the alif.", "«Avrupa» — yabancı özel isim."),
  bi_noun("بِدَافِعٍ", "dafi", "«by an impulse»", "«bir saikle»", tags=["ism-fail"], extra=" — الْبَاءُ لِلسَّبَبِيَّةِ"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("عِنْدِهِمْ", "inda", "عِنْدِ", "هِمْ", "pron-3mp", "ظَرْفُ مَكَانٍ مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِدَافِعٍ: مِنْ تِلْقَاءِ أَنْفُسِهِمْ.", "«their own» — a naʿt of «impulse»: of their own accord.", "«kendilerinden» — «saik»in sıfatı.", tags=[HJ, ID, NA], punct=" (١)؛"),
])
sen("s2", "and open idolatry had long been widespread there and had sunk into it up to the chins. The Greeks were idolaters: they had pictured the attributes of God in the shape of sundry gods, carved statues for them and built them temples and shrines — for provision a god, for mercy a god, for conquest a god;",
        "Orada açık putperestlik çoktan yayılmış ve çenelere kadar içine gömülmüştü. Yunanlılar putperestti: Allah'ın sıfatlarını türlü ilâhlar şeklinde tasavvur etmiş, onlara heykeller yontmuş, mabetler ve tapınaklar yapmışlardı; rızık için bir ilâh, rahmet için bir ilâh, kahır için bir ilâh;", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ حَالٌ مِنْ أُورُبَّا.", "«and [indeed]» — the wāw of state: the sentence describes Europe's condition.", "«ve [gerçekten]» — hâl vâvı.", segments=wa_("قَدْ", "qad", "part")),
  mazi_ta("شَاعَتْ", "shaa-spread", "«had been widespread»", "«yayılmıştı»", tags=["hollow-verbs"], wa=False),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«there»", "«orada»"),
  fail("الْوَثَنِيَّةُ", "wathaniyya", "«idolatry»", "«putperestlik»"),
  naat("السَّافِرَةُ", "safir", "«open»", "«açık»", case="raf", tags=["ism-fail"]),
  prep("مِنْ", "min", "«since»", "«-den beri»", ar="حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ الزَّمَانِيَّةِ."),
  majrur("زَمَانٍ", "zaman", "«a long time»", "«uzun zaman»", punct="،"),
  mazi_ta("وَغَاصَتْ", "ghasa", "«and had sunk»", "«ve gömülmüştü»", tags=[AT, "hollow-verbs"], wa=True),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«into it»", "«içine»"),
  prep("إِلَى", "ila", "«up to»", "«-e kadar»", ar="حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ."),
  majrur("الْأَذْقَانِ", "dhaqan", "«the chins»", "«çenelere»", tags=[JT], punct="،", ar="مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ ذَقَنٍ؛ غَاصَ إِلَى الْأَذْقَانِ: كِنَايَةٌ عَنِ التَّمَكُّنِ التَّامِّ."),
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلتَّفْرِيعِ)، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«so … were» — kāna after the fāʾ of consequence.", "«bu yüzden … idi» — tefrî fâ'sı ve kâne.", segments=conj_segs("فَكَانَ", "kana", "verb")),
  ism_kana("الْيُونَانُ", "yunan", "«the Greeks»", "«Yunanlılar»"),
  tok("وَثَنِيِّينَ", "wathani", "noun", [KN, JS, "ism-mansub"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — مَنْسُوبٌ إِلَى الْوَثَنِ.", "«idolaters» — kāna's khabar; a nisba in the sound plural.", "«putperest» — kâne'nin haberi; nisbet.", punct="،"),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ حَالِيَّةٌ (أَوْ عَاطِفَةٌ)، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi_pl("تَصَوَّرُوا", "tasawwara", "«they had pictured»", "«tasavvur etmişlerdi»", tags=["form-v-verbs"]),
  maful_("صِفَاتِ", "sifa", "«the attributes [of]»", "«sıfatlarını»", tags=[ID, JT], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  fi(),
  majrur("شَكْلِ", "shakl", "«the shape [of]»", "«şeklinde»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("آلِهَةٍ", "ilah", "«gods»", "«ilâhlar»", tags=[JT]),
  tok("شَتَّى", "shatta", "noun", [NA, MM, "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — جَمْعُ شَتِيتٍ: مُتَفَرِّقَةٌ.", "«sundry» — a naʿt; a maqṣūr plural meaning «diverse».", "«türlü» — sıfat; maksûr çoğul.", punct="،"),
  mazi_pl("نَحَتُوا", "nahata", "«they carved»", "«yonttular»", tags=["jumla-sifa"]),
  li_pron("لَهَا", "هَا", "pron-3fs", "«for them»", "«onlara»"),
  maful_("تَمَاثِيلَ", "timthal", "«statues»", "«heykeller»", tags=[JT, "mamnu-min-sarf"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (صِيغَةُ مُنْتَهَى الْجُمُوعِ)، فَلَا يُنَوَّنُ.", punct="،"),
  mazi_wa_alif("وَبَنَوْا", "bana", "«and built»", "«ve yaptılar»", tags=[AT], wa=True),
  li_pron("لَهَا", "هَا", "pron-3fs", "«for them»", "«onlara»"),
  maful_("مَعَابِدَ", "mabad", "«temples»", "«mabetler»", tags=[JT, "mamnu-min-sarf"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (مَفَاعِلُ)."),
  tok("وَهَيَاكِلَ", "haykal", "noun", [AT, MB, JT, "mamnu-min-sarf"], "الْوَاوُ عَاطِفَةٌ، وَهَيَاكِلَ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (فَعَالِلُ).", "«and shrines» — joined; a diptote plural.", "«ve tapınaklar» — atıf; gayr-i munsarıf.", punct="؛", segments=wa_("هَيَاكِلَ", "haykal", "noun")),
  tok("فَلِلرِّزْقِ", "rizq", "noun", [AT, HJ, MK], "الْفَاءُ لِلتَّفْصِيلِ (عَاطِفَةٌ)، وَاللَّامُ حَرْفُ جَرٍّ، وَالرِّزْقِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«so for provision» — the fāʾ of detailing; the fronted khabar.", "«rızık için» — tafsil fâ'sı; öne alınmış haber.", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("لرِّزْقِ", "rizq", "noun")]),
  ilah_mk(),
  tok("وَلِلرَّحْمَةِ", "rahma", "noun", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالرَّحْمَةِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and for mercy»", "«ve rahmet için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لرَّحْمَةِ", "rahma", "noun")]),
  ilah_mk(),
  tok("وَلِلْقَهْرِ", "qahr", "noun", [AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالْقَهْرِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and for conquest»", "«ve kahır için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لْقَهْرِ", "qahr", "noun")]),
  ilah_mk(),
])
sen("s3", "and Rome was deep-rooted in idolatry and in clinging to superstitions: idolatry had blended with its flesh and blood and ran through it as the spirit and the blood run; and the Romans worshipped sundry gods.",
        "Roma da putperestlikte ve hurafelere sarılmakta köklüydü: putperestlik onun etine ve kanına karışmış, ruh ve kan gibi damarlarında dolaşmıştı; Romalılar türlü ilâhlara tapıyorlardı.", [
  kanat("وَكَانَتِ", ism_note="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  ism_kana("الرُّومِيَّةُ", "rumiyya", "«Rome [the Roman state]»", "«Roma»", tags=["ism-mansub"]),
  khabar_kana("عَرِيقَةً", "ariq", "«deep-rooted»", "«köklü»"),
  fi(),
  majrur("الْوَثَنِيَّةِ", "wathaniyya", "«idolatry»", "«putperestlikte»"),
  atf("وَالتَّمَسُّكِ", "tamassuk", "«clinging»", "«sarılmakta»", tags=["form-v-verbs"]),
  bi_noun("بِالْخُرَافَاتِ", "khurafa", "«to superstitions»", "«hurafelere»", tags=[JT], punct="،"),
  tok("وَقَدِ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ عَاطِفَةٌ (أَوْ حَالِيَّةٌ)، وَقَدْ حَرْفُ تَحْقِيقٍ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and [indeed]» — qad takes a kasra before the joining hamza.", "«ve [gerçekten]» — kad, vasıl hemzesinden önce kesreli.", segments=wa_("قَدِ", "qad", "part")),
  mazi_ta("امْتَزَجَتِ", "imtazaja", "«had blended»", "«karışmıştı»", tags=["form-viii-verbs"], wa=False, extra="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الْوَثَنِيَّةُ", "wathaniyya", "«idolatry»", "«putperestlik»"),
  tok("بِلَحْمِهَا", "lahm", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَلَحْمِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«with its flesh»", "«etine»", segments=[seg("بِ", "bi", "prep"), seg("لَحْمِ", "lahm", "noun"), seg("هَا", "pron-3fs", "pron")]),
  pron_atf("وَدَمِهَا", "dam", "دَمِ", "هَا", "pron-3fs", "«and its blood»", "«ve kanına»", case="jarr", punct="،"),
  mazi_ta_naqis("وَجَرَتْ", "jara", "«and ran»", "«ve aktı»", tags=[AT], wa=True),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«through it»", "«onda»"),
  tok("مَجْرَى", "majra", "noun", [MF, ID, "ism-maqsur-manqus"], "مَفْعُولٌ مُطْلَقٌ (أَوْ ظَرْفٌ) مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ — جَرَى مِنْهُ مَجْرَى الدَّمِ: صَارَ كَالدَّمِ فِيهِ.", "«the course [of]» — a maqṣūr noun of place, naṣb hidden on the alif.", "«… gibi» — maksûr ism-i mekân; mef'ûl-i mutlak yahut zarf.", segments=None),
  mudaf_ilayh("الرُّوحِ", "ruh", "«the spirit»", "«ruhun»"),
  atf("وَالدَّمِ", "dam", "«and the blood»", "«ve kanın»", punct="،"),
  wa_kana(ism_note=""),
  ism_kana("الرُّومَانُ", "ruman", "«the Romans»", "«Romalılar»"),
  khamsa("يَعْبُدُونَ", "abada", "«worshipped»", "«tapıyorlardı»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  maful_("آلِهَةً", "ilah", "«gods»", "«ilâhlara»", tags=[JT]),
  tok("شَتَّى", "shatta", "noun", [NA, MM, "ism-maqsur-manqus"], "نَعْتٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«sundry» — a naʿt.", "«türlü» — sıfat.", punct="."),
])
sen("s4", "So when Christianity reached them, and Constantine the Great turned Christian in the year 306, embraced the new religion, adopted it and made it the official religion of the state, Christianity began to take a great deal from the idolatrous creeds, the Roman traditions and Greek philosophy, and to draw near to them little by little;",
        "Hıristiyanlık onlara ulaşıp Büyük Konstantin 306 yılında Hıristiyan olunca, yeni dini bağrına basıp benimseyince ve onu devletin resmî dini yapınca, Hıristiyanlık putperest akidelerden, Roma geleneklerinden ve Yunan felsefesinden pek çok şey almaya, yavaş yavaş onlara yaklaşmaya başladı;", [
  tok("فَلَمَّا", "lamma", "noun", [AT, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، وَجَوَابُهُ بَدَأَتْ.", "«so when» — the conditional ẓarf; its answer is «began».", "«-ınca» — şart mânâlı zarf; cevabı «başladı».", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "noun")]),
  mazi_ta("وَصَلَتْ", "wasala", "«reached»", "«ulaştı»", tags=["mithal-verbs"], wa=False),
  prep_pron("إِلَيْهِمُ", "ila", "هِمُ", "pron-3mp", "«them»", "«onlara»", extra_ar="، حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("النَّصْرَانِيَّةُ", "nasraniyya", "«Christianity»", "«Hıristiyanlık»", punct="،", tags=["ism-mansub"]),
  mazi("وَتَنَصَّرَ", "tanassara", "«and turned Christian»", "«ve Hıristiyan oldu»", tags=[AT, "form-v-verbs"], hidden=None, wa=True),
  fail("قُسْطَنْطِينُ", "qustantin", "«Constantine»", "«Konstantin»", tags=["mamnu-min-sarf"], extra_ar=" — عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ"),
  naat("الْكَبِيرُ", "kabir", "«the Great»", "«Büyük»", case="raf"),
  tok("سَنَةَ", "sana", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ إِلَى الْعَدَدِ بَعْدَهُ.", "«in the year» — a ẓarf of time annexed to the number.", "«yılında» — zaman zarfı, sayıya muzâf.", punct=" ٣٠٦م،"),
  mazi("وَاحْتَضَنَ", "ihtadana", "«and embraced»", "«ve bağrına bastı»", tags=[AT, "form-viii-verbs"], hidden="هُوَ", wa=True),
  maful_("الدِّينَ", "din", "«the religion»", "«dini»"),
  naat("الْجَدِيدَ", "jadid", "«new»", "«yeni»", case="nasb"),
  tok("وَتَبَنَّاهُ", "tabanna", "verb", [AT, MB, "form-v-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَبَنَّى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالْهَاءُ مَفْعُولٌ بِهِ — تَبَنَّاهُ: اتَّخَذَهُ كَالِابْنِ.", "«and adopted it» — a defective Form V; «it» the object.", "«ve onu benimsedi» — nâkıs tefe''ul; «onu» mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("تَبَنَّا", "tabanna", "verb"), seg("هُ", "pron-3ms", "pron")]),
  v_pron("وَجَعَلَهُ", "jaala", "جَعَلَ", "هُ", "pron-3ms", "«and made it»", "«ve onu … yaptı»", wa=True, hidden="هُوَ"),
  maful_("دِينَ", "din", "«the religion [of]»", "«dini»", tags=[ID], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("الدَّوْلَةِ", "dawla", "«the state»", "«devletin»"),
  naat("الرَّسْمِيَّ", "rasmi", "«official»", "«resmî»", case="nasb", tags=["ism-mansub"], punct="،"),
  mazi_ta("بَدَأَتِ", "badaa", "«began»", "«başladı»", wa=False, extra="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — جَوَابُ لَمَّا"),
  fail("النَّصْرَانِيَّةُ", "nasraniyya", "«Christianity»", "«Hıristiyanlık»", tags=["ism-mansub"]),
  mudari("تَأْخُذُ", "akhadha", "«to take»", "«almaya»", hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ بَدَأَتْ (مِنْ أَفْعَالِ الشُّرُوعِ)"),
  maful_("الشَّيْءَ", "shay", "«a deal»", "«şeyi»"),
  naat("الْكَثِيرَ", "kathir", "«great»", "«pek çok»", case="nasb"),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  majrur("الْعَقَائِدِ", "aqida", "«the creeds»", "«akidelerden»", tags=[JT]),
  naat("الْوَثَنِيَّةِ", "wathani", "«idolatrous»", "«putperest»", tags=["ism-mansub"]),
  atf("وَالتَّقَالِيدِ", "taqlid", "«the traditions»", "«geleneklerinden»", tags=[JT]),
  naat("الرُّومِيَّةِ", "rumiyya", "«Roman»", "«Roma»", tags=["ism-mansub"]),
  atf("وَالْفَلْسَفَةِ", "falsafa", "«philosophy»", "«felsefesinden»"),
  naat("الْيُونَانِيَّةِ", "yunani", "«Greek»", "«Yunan»", tags=["ism-mansub"], punct="،"),
  tok("وَتَدْنُو", "dana", "verb", [AT, "naqis-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَتَدْنُو فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — مَعْطُوفٌ عَلَى تَأْخُذُ.", "«and to draw near» — joined to «to take»; the ḍamma hidden on the wāw.", "«ve yaklaşmaya» — «almaya»ya atıf; zamme vâv üzerinde takdirî.", segments=wa_("تَدْنُو", "dana", "verb")),
  prep_pron("إِلَيْهَا", "ila", "هَا", "pron-3fs", "«to them»", "«onlara»"),
  tok("رُوَيْدًا", "ruwaydan", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ (مَصْدَرٌ مُصَغَّرٌ مِنْ إِرْوَادٍ).", "«little [by little]» — an absolute object; a diminutive maṣdar.", "«yavaş» — mef'ûl-i mutlak; tasğir edilmiş masdar."),
  tok("رُوَيْدًا", "ruwaydan", "noun", ["tawkid"], "تَوْكِيدٌ لَفْظِيٌّ مَنْصُوبٌ.", "«by little» — a verbal reinforcement by repetition.", "«yavaş» — lafzî te'kid.", punct="،"),
])
sen("s5", "and it came to lose its prophetic authenticity, its Eastern simplicity and its tawḥīd-fervour; some hypocrites entered it and grafted onto it their old creeds and their idolatrous taste, and out of that a new religion arose in which Christianity and idolatry show equally, side by side.",
        "Peygamberlik asaletini, Doğulu sadeliğini ve tevhid coşkusunu yitirir oldu; içine bazı münafıklar girdi ve ona eski akidelerini, putperest zevklerini aşıladılar; bundan, Hıristiyanlık ile putperestliğin eşit biçimde yan yana göründüğü yeni bir din doğdu.", [
  tok("وَصَارَتْ", "sara", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَصَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«and it came to» — ṣāra, a sister of kāna; its ism concealed.", "«ve … oldu» — kâne'nin kardeşi sâra; ismi gizli.", segments=wa_("صَارَتْ", "sara", "verb")),
  mudari("تَفْقِدُ", "faqada", "«lose»", "«yitirir»", tags=[KN], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ صَارَتْ"),
  noun_pron("أَصَالَتَهَا", "asala-authenticity", "أَصَالَتَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its authenticity» — the object.", "«asaletini» — mef'ûl.", tags=[MB, ID]),
  naat("النَّبَوِيَّةَ", "nabawi", "«prophetic»", "«peygamberlik»", case="nasb", tags=["ism-mansub"], punct="،"),
  pron_atf("وَبَسَاطَتَهَا", "basata-simplicity", "بَسَاطَتَ", "هَا", "pron-3fs", "«and its simplicity»", "«ve sadeliğini»", case="nasb"),
  naat("الشَّرْقِيَّةَ", "sharqi", "«Eastern»", "«Doğulu»", case="nasb", tags=["ism-mansub"], punct="،"),
  pron_atf("وَحَمَاسَتَهَا", "hamasa", "حَمَاسَتَ", "هَا", "pron-3fs", "«and its fervour»", "«ve coşkusunu»", case="nasb"),
  naat("التَّوْحِيدِيَّةَ", "tawhidi", "«of tawḥīd»", "«tevhid»", case="nasb", tags=["ism-mansub"], punct="،"),
  mazi("وَدَخَلَ", "dakhala", "«and entered»", "«ve girdi»", tags=[AT], hidden=None, wa=True),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«it»", "«içine»"),
  fail("بَعْضُ", "bad", "«some [of]»", "«bazı»", tags=[ID], extra_ar="، مُضَافٌ"),
  tok("الْمُنَافِقِينَ", "munafiq", "noun", [ID, JS, "ism-fail", "form-iii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«hypocrites» — jarr by the yāʾ.", "«münafıklar» — yâ ile mecrûr."),
  v_pl_pron("فَطَعَّمُوهَا", "taama", "طَعَّمُو", "هَا", "pron-3fs", "«and grafted onto it»", "«ve ona aşıladılar»", tags=["form-ii-verbs"], fa=True),
  tok("بِعَقَائِدِهِمُ", "aqida", "noun", [HJ, ID, JT], "الْبَاءُ حَرْفُ جَرٍّ، وَعَقَائِدِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ، حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«with their creeds»", "«akideleriyle»", segments=[seg("بِ", "bi", "prep"), seg("عَقَائِدِ", "aqida", "noun"), seg("هِمُ", "pron-3mp", "pron")]),
  naat("الْقَدِيمَةِ", "qadim", "«old»", "«eski»"),
  pron_atf("وَذَوْقِهِمُ", "dhawq", "ذَوْقِ", "هِمُ", "pron-3mp", "«and their taste»", "«ve zevkleriyle»", case="jarr"),
  naat("الْوَثَنِيِّ", "wathani", "«idolatrous»", "«putperest»", tags=["ism-mansub"], punct="،"),
  mazi("وَنَشَأَ", "nashaa", "«and arose»", "«ve doğdu»", tags=[AT], hidden=None, wa=True),
  prep("مِنْ", "min", "«out of»", "«-dan»"),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«that»", "«bu»"),
  fail("دِينٌ", "din", "«a religion»", "«bir din»"),
  naat("جَدِيدٌ", "jadid", "«new»", "«yeni»", case="raf", punct="،"),
  tok("تَتَجَلَّى", "tajalla", "verb", ["jumla-sifa", "form-v-verbs", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِدِينٌ.", "«show» — a sentence as a second naʿt of «religion».", "«görünür» — «din»in ikinci sıfatı olan cümle."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in it»", "«onda»", extra_ar=" — أُنِّثَ الضَّمِيرُ عَلَى مَعْنَى الدِّيَانَةِ"),
  fail("النَّصْرَانِيَّةُ", "nasraniyya", "«Christianity»", "«Hıristiyanlık»", tags=["ism-mansub"]),
  atf("وَالْوَثَنِيَّةُ", "wathaniyya", "«and idolatry»", "«ve putperestlik»", case="raf"),
  hal("سَوَاءً", "sawa", "«equally»", "«eşit olarak»"),
  bi_noun("بِسَوَاءٍ", "sawa", "«side by side»", "«yan yana»", extra=" — سَوَاءً بِسَوَاءٍ: عَلَى حَدٍّ وَاحِدٍ", punct="."),
])
sen("s6", "(1) [The author's footnote:] Because the Messiah had not commanded them to do that; he had declared that he was sent to the lost sheep of Israel.",
        "(1) [Yazarın dipnotu:] Çünkü Mesîh onlara bunu emretmemişti; kendisinin İsrâil'in kaybolmuş koyunlarına gönderildiğini açıkça söylemişti.", [
  tok("لِأَنَّ", "anna", "part", [HJ, IW, TA], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — (حَاشِيَةُ الْمُؤَلِّفِ: تَعْلِيلٌ لِقَوْلِهِ «بِدَافِعٍ مِنْ عِنْدِهِمْ»).", "«because» — the lām of cause with anna (the author's footnote 1).", "«çünkü» — ta'lîl lâmı ve enne (yazarın 1 numaralı dipnotu).", segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part")]),
  tok("الْمَسِيحَ", "masih", "propn", [IW], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the Messiah» — anna's ism.", "«Mesîh» — enne'nin ismi."),
  tok("لَمْ", "lam", "part", [IW], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — negates and turns the present to the past.", "«-medi» — nefiy, cezm ve kalb harfi."),
  tok("يَأْمُرْهُمْ", "amara-order", "verb", [IW, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«had commanded them» — jussive after lam; the sentence is anna's khabar.", "«onlara emretmişti» — lem ile meczûm; cümle enne'nin haberi.", segments=[seg("يَأْمُرْ", "amara-order", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("بِذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that»", "«bunu»", punct="؛", segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  tok("فَقَدْ", "qad", "part", [AT, "qad-harf"], "الْفَاءُ لِلتَّعْلِيلِ (عَاطِفَةٌ)، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«for [indeed]»", "«zira»", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("صَرَّحَ", "sarraha", "«he had declared»", "«açıkça söylemişti»", tags=["form-ii-verbs"], hidden="هُوَ (الْمَسِيحُ)"),
  tok("بِأَنَّهُ", "anna", "part", [HJ, IW], "الْبَاءُ حَرْفُ جَرٍّ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْبَاءِ.", "«that he» — bi + anna; the clause is in jarr.", "«ki o» — bâ ve enne; masdar-ı müevvel mecrûr.", segments=[seg("بِ", "bi", "prep"), seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("أُرْسِلَ", "arsala", "verb", [IW, NF, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«was sent» — a passive; the sentence is anna's khabar.", "«gönderildi» — meçhul; cümle enne'nin haberi."),
  li_noun("لِخِرَافِ", "kharuf", "«to the sheep [of]»", "«koyunlarına»", tags=[ID, JT], extra="، مُضَافٌ — جَمْعُ خَرُوفٍ"),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Israel» — a diptote.", "«İsrâil» — gayr-i munsarıf."),
  naat("الضَّالَّةِ", "dall", "«lost»", "«kaybolmuş»", tags=["doubled-verbs", "ism-fail"], punct="."),
])
sen("s7", "And so the advancing, conquering Christianity walked a road other than the road on which the Messiah had set it and to which he had called;",
        "Böylece ilerleyen, fetheden Hıristiyanlık, Mesîh'in onu üzerinde yürüttüğü ve kendisine çağırdığı yoldan başka bir yolda yürüdü;", [
  tok("وَكَذٰلِكَ", "kadhalika", "noun", [AT, HJ, "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِمَصْدَرٍ مَحْذُوفٍ: سَارَتْ سَيْرًا كَذٰلِكَ.", "«and so» — the kāf of likening with «that»: it walked a walk like that.", "«ve böylece» — teşbih kâfı ve işaret ismi.", segments=[seg("وَ", "wa", "conj"), seg("كَذٰلِكَ", "kadhalika", "noun")]),
  mazi_ta("سَارَتِ", "sara-travel", "«walked»", "«yürüdü»", tags=["hollow-verbs"], wa=False, extra="، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("النَّصْرَانِيَّةُ", "nasraniyya", "«Christianity»", "«Hıristiyanlık»", tags=["ism-mansub"]),
  naat("الزَّاحِفَةُ", "zahif", "«advancing»", "«ilerleyen»", case="raf", tags=["ism-fail"]),
  naat2("الْفَاتِحَةُ", "fatih", "«conquering»", "«fetheden»", case="raf"),
  prep("عَلَى", "ala", "«on»", "«-da»"),
  majrur("دَرْبٍ", "darb-road", "«a road»", "«bir yolda»"),
  tok("غَيْرِ", "ghayr", "noun", [NA, ID], "نَعْتٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«other than» — a naʿt, annexed.", "«-den başka» — sıfat, muzâf."),
  mudaf_ilayh("الدَّرْبِ", "darb-road", "«the road»", "«yoldan»"),
  tok("الَّذِي", "alladhi", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلدَّرْبِ.", "«which» — the relative, a naʿt of «the road».", "«-dığı» — ism-i mevsûl, «yol»un sıfatı."),
  mazi("سَلَكَ", "salaka", "«had set»", "«yürüttüğü»", tags=[MW], hidden=None, extra_ar=" — صِلَةُ الْمَوْصُولِ؛ سَلَكَ بِهِ الطَّرِيقَ: أَدْخَلَهُ فِيهِ"),
  tok("الْمَسِيحُ", "masih", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — the doer.", "«Mesîh» — fâil."),
  prep_pron("بِهَا", "bi", "هَا", "pron-3fs", "«it [Christianity]»", "«onu»", extra_ar=" — الْبَاءُ لِلتَّعْدِيَةِ، وَالضَّمِيرُ لِلنَّصْرَانِيَّةِ"),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«on [which]»", "«üzerinde»", punct="،", extra_ar=" — الْعَائِدُ عَلَى الَّذِي"),
  tok("وَدَعَا", "daa", "verb", [AT, MW, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — مَعْطُوفٌ عَلَى الصِّلَةِ.", "«and had called» — joined to the ṣila.", "«ve çağırdı» — sılaya atıf.", segments=wa_("دَعَا", "daa", "verb")),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to it»", "«ona»", punct="،"),
])
sen("s8", "and it was like a wayfarer who strays from the road — on purpose or not on purpose — in the darkness of the night, and goes on walking on a road that never meets the first road, to the very end.",
        "Gece karanlığında — bilerek ya da bilmeyerek — yoldan sapan ve sonuna kadar ilk yolla hiç kesişmeyen bir yolda yürümeye devam eden bir yolcu gibiydi.", [
  kanat("وَكَانَتْ", ism_note="، وَاسْمُهَا مُسْتَتِرٌ: هِيَ"),
  tok("كَسَالِكِ", "salik", "noun", [HJ, KN, ID, "ism-fail"], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَسَالِكِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَتْ.", "«like a wayfarer [of]» — the kāf of likening; the phrase is kāna's khabar.", "«… yolcusu gibi» — teşbih kâfı; kâne'nin haberi.", segments=[seg("كَ", "ka", "part"), seg("سَالِكِ", "salik", "noun")]),
  mudaf_ilayh("طَرِيقٍ", "tariq", "«a road»", "«bir yol»"),
  tok("يَضِلُّ", "dalla-stray", "verb", ["jumla-sifa", "doubled-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ نَعْتٌ لِسَالِكِ (أَوْ حَالٌ).", "«who strays» — a sentence as the naʿt of «wayfarer».", "«sapan» — «yolcu»nun sıfatı olan cümle."),
  tok("عَنِ", "an", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-dan»"),
  majrur("الطَّرِيقِ", "tariq", "«the road»", "«yoldan»", punct=" —"),
  prep("عَنْ", "an", "«on»", "«-le»"),
  majrur("قَصْدٍ", "qasd", "«purpose»", "«bilerek»", ar="مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مُعْتَرِضَةٌ: قَاصِدًا."),
  tok("أَوْ", "aw", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ.", "«or»", "«ya da»"),
  prep("عَنْ", "an", "«on»", "«-le»"),
  tok("غَيْرِ", "ghayr", "noun", [AT, HJ, ID], "مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«non-» — joined, annexed.", "«olmayan» — atıf, muzâf."),
  mudaf_ilayh("قَصْدٍ", "qasd", "«purpose»", "«bilmeyerek»", punct=" —"),
  fi(),
  majrur("ظَلَامِ", "zalam", "«the darkness [of]»", "«karanlığında»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — مُتَعَلِّقٌ بِيَضِلُّ."),
  mudaf_ilayh("اللَّيْلِ", "layl", "«the night»", "«gecenin»", punct=" —،"),
  fa_mudari("فَيُوَاصِلُ", "wasala-iii", "«and goes on»", "«ve devam eder»", tags=["form-iii-verbs", "mithal-verbs"], hidden="هُوَ"),
  noun_pron("سَيْرَهُ", "sayr", "سَيْرَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his walking» — the object.", "«yürüyüşüne» — mef'ûl.", tags=[MB, ID]),
  prep("عَلَى", "ala", "«on»", "«-da»"),
  majrur("طَرِيقٍ", "tariq", "«a road»", "«bir yolda»"),
  la_nafiya(),
  neg_mudari("يَلْتَقِي", "iltaqa", "«meets»", "«kesişir»", tags=["jumla-sifa", "form-viii-verbs", "naqis-verbs"], hidden="هُوَ", extra=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْجُمْلَةُ نَعْتٌ لِطَرِيقٍ"),
  bi_noun("بِالطَّرِيقِ", "tariq", "«the road»", "«yolla»"),
  naat("الْأَوَّلِ", "awwal", "«first»", "«ilk»"),
  prep("إِلَى", "ila", "«to»", "«-e kadar»"),
  majrur("الْأَخِيرِ", "akhir", "«the very end»", "«sonuna»", punct=".", ar="مَجْرُورٌ بِالْكَسْرَةِ — إِلَى الْأَخِيرِ: إِلَى آخِرِ الطَّرِيقِ."),
])
sen("s9", "And for this subtle wisdom, known only to one who has read the history of this religion, God described them as astray when He described the Jews as the objects of wrath, and said on the tongue of the Muslims:",
        "Bu dinin tarihini okuyanlardan başkasının bilmediği bu ince hikmetten dolayı, Allah Yahudileri gazaba uğramış diye nitelerken onları da sapmış diye niteledi ve müslümanların diliyle şöyle buyurdu:", [
  tok("وَلِهٰذِهِ", "hadhihi", "pron", [AT, HJ, "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَهٰذِهِ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِوَصَفَهُمْ.", "«and for this» — the lām of cause; the phrase hangs on «described them».", "«ve bu … için» — ta'lîl lâmı; «niteledi»ye bağlı.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("هٰذِهِ", "hadhihi", "pron")]),
  tok("الْحِكْمَةِ", "hikma", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«wisdom» — in apposition to «this».", "«hikmet» — işaret isminden bedel."),
  naat("الدَّقِيقَةِ", "daqiq", "«subtle»", "«ince»"),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ.", "«which» — the relative, a second naʿt.", "«-en» — ism-i mevsûl, ikinci sıfat."),
  la_nafiya(),
  tok("يَعْرِفُهَا", "arafa", "verb", [MW, MB, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ — صِلَةُ الْمَوْصُولِ.", "«knows it» — the ṣila; «it» the object before the doer.", "«onu bilir» — sıla; «onu» mef'ûl.", segments=[seg("يَعْرِفُ", "arafa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except» — restriction.", "«-den başka» — hasr."),
  tok("مَنْ", "man-mawsula", "pron", [FL, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«one who» — the relative, the doer.", "«-en kimse» — ism-i mevsûl, fâil."),
  mazi("قَرَأَ", "qaraa", "«has read»", "«okuyan»", tags=[MW], hidden="هُوَ", extra_ar=" — صِلَةٌ"),
  maful_("تَارِيخَ", "tarikh", "«the history [of]»", "«tarihini»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  tok("هٰذِهِ", "hadhihi", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this»", "«bu»"),
  tok("الدِّيَانَةِ", "diyana", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«religion» — in apposition.", "«din» — bedel.", punct="،"),
  tok("وَصَفَهُمُ", "wasafa", "verb", [MB, "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَهُمْ مَفْعُولٌ بِهِ، حُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ — جَوَابُ الِاسْتِئْنَافِ: وَصَفَهُمْ بِالضَّلَالِ لِهٰذِهِ الْحِكْمَةِ.", "«described them» — the main verb; «them» its object, the mīm given a ḍamma before the joining hamza.", "«onları niteledi» — ana fiil; «onları» mef'ûl, mîm iki sâkinden ötürü ötreli.", segments=[seg("وَصَفَ", "wasafa", "verb"), seg("هُمُ", "pron-3mp", "pron")]),
  allah_fail(),
  bi_noun("بِالضَّلَالِ", "dalal", "«as astray»", "«sapıklıkla»"),
  tok("حِينَ", "hina", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when» — a ẓarf annexed to the sentence.", "«-iken» — cümleye muzâf zarf."),
  mazi("وَصَفَ", "wasafa", "«He described»", "«niteledi»", tags=[ID, "mithal-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ حِينَ"),
  maful_("الْيَهُودَ", "yahud", "«the Jews»", "«Yahudileri»"),
  bi_noun("بِالْمَغْضُوبِيَّةِ", "maghdubiyya", "«as the objects of wrath»", "«gazaba uğramışlıkla»", tags=["ism-mansub"], extra=" — مَصْدَرٌ صِنَاعِيٌّ مِنَ الْمَغْضُوبِ عَلَيْهِ", punct="،"),
  mazi("فَقَالَ", "qala", "«and said»", "«ve buyurdu»", tags=[AT, "hollow-verbs"], hidden="هُوَ", wa=True),
  prep("عَلَى", "ala", "«on»", "«-yla»"),
  majrur("لِسَانِ", "lisan", "«the tongue [of]»", "«diliyle»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — عَلَى لِسَانِهِ: بِمَا يَقُولُهُ."),
  tok("الْمُسْلِمِينَ", "muslim", "noun", [ID, JS, "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the Muslims» — jarr by the yāʾ.", "«müslümanların» — yâ ile mecrûr.", punct=":"),
])
sen("s10", "«Guide us to the straight path, the path of those You have favoured, not of those who incur wrath, nor of those astray.» (1:6–7)",
        "«Bizi dosdoğru yola ilet; kendilerine nimet verdiklerinin yoluna, gazaba uğrayanların ve sapanların yoluna değil.» (Fâtiha 6–7)", [
  *quran([
  tok("اهْدِنَا", "hada", "verb", [AM, MB, "naqis-verbs"], "فِعْلُ دُعَاءٍ (أَمْرٌ لَفْظًا) مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَنَا مَفْعُولٌ بِهِ أَوَّلُ.", "«guide us» — a supplication in the imperative form; the weak letter dropped; «us» the first object.", "«bizi ilet» — dua emri; illet harfi düşmüş; «bizi» ilk mef'ûl.", segments=[seg("اهْدِ", "hada", "verb"), seg("نَا", "pron-1p", "pron")]),
  maful_("الصِّرَاطَ", "sirat", "«the path»", "«yola»", ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  naat("الْمُسْتَقِيمَ", "mustaqim", "«straight»", "«dosdoğru»", case="nasb", tags=["form-x-verbs", "ism-fail"], punct=AYA),
  tok("صِرَاطَ", "sirat", "noun", [BD, ID], "بَدَلٌ مِنَ الصِّرَاطَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the path [of]» — a badal of «the path», annexed.", "«yoluna» — «yol»dan bedel, muzâf."),
  alladhina("jarr", "مُضَافٌ إِلَيْهِ", "«those whom» — the muḍāf ilayh.", "«-enlerin» — muzâfun ileyh."),
  tu_mazi("أَنْعَمْتَ", "anama", "أَنْعَمْ", "«You have favoured» — the ṣila; the doer's tāʾ.", "«nimet verdin» — sıla; fâil tâ'sı.", "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — صِلَةُ الْمَوْصُولِ.", tags=[MW, "form-iv-verbs"], person="تَ", person_lex="pron-2ms"),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«upon them»", "«onlara»"),
  tok("غَيْرِ", "ghayr", "noun", [BD, ID], "بَدَلٌ مِنَ الَّذِينَ (أَوْ نَعْتٌ لَهُ) مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«not [those]» — a badal (or naʿt) of «those», annexed.", "«olmayanların» — «-enler»den bedel (yahut sıfat), muzâf."),
  tok("الْمَغْضُوبِ", "maghdub", "noun", [ID, NF], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ، وَنَائِبُ فَاعِلِهِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«the object of wrath» — a passive participle whose deputy doer is the phrase after it.", "«gazaba uğramış» — ism-i mef'ûl; nâib-i fâili sonraki câr-mecrûr."),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«upon them»", "«onlara»", extra_ar=" — فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ"),
  la_nafiya("وَلَا", wa=True),
  tok("الضَّالِّينَ", "dall", "noun", [AT, ID, JS, "ism-fail", "doubled-verbs"], "مَعْطُوفٌ عَلَى الْمَغْضُوبِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ فَاعِلٍ مِنْ ضَلَّ، مُضَاعَفٌ.", "«those astray» — joined; an active participle of the doubled ḍalla.", "«sapmışların» — atıf; muzâaf dalle'nin ism-i fâili.", punct="."),
  ]),
])
sen("s11", "And in that there was a tragedy for Europe, and a tragedy for the humanity that Europe led for a long age and still dominates and controls.",
        "Bunda Avrupa için bir trajedi, uzun bir zaman Avrupa'nın yönettiği ve hâlâ hükmedip denetimi altında tuttuğu insanlık için de bir trajedi vardı.", [
  kanat("وَكَانَتْ", ism_note="، وَاسْمُهَا مُسْتَتِرٌ: هِيَ (الْحَالُ)"),
  fi(),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«that»", "«bunda»"),
  khabar_kana("مَأْسَاةً", "masat", "«a tragedy»", "«bir trajedi»"),
  tok("لِأُورُبَّا", "urubba", "propn", [HJ, NA], "اللَّامُ حَرْفُ جَرٍّ، وَأُورُبَّا مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — نَعْتٌ لِمَأْسَاةً (أَوْ مُتَعَلِّقٌ بِهَا).", "«for Europe»", "«Avrupa için»", punct="،", segments=[seg("لِ", "li", "prep"), seg("أُورُبَّا", "urubba", "propn")]),
  tok("وَمَأْسَاةً", "masat", "noun", [AT, KN], "الْوَاوُ عَاطِفَةٌ، وَمَأْسَاةً مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«and a tragedy»", "«ve bir trajedi»", segments=wa_("مَأْسَاةً", "masat", "noun")),
  li_noun("لِلْإِنْسَانِيَّةِ", "insaniyya", "«for humanity»", "«insanlık için»", tags=["ism-mansub"]),
  tok("الَّتِي", "allati", "pron", [MW, NA], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ نَعْتٌ لِلْإِنْسَانِيَّةِ.", "«which» — a naʿt of «humanity».", "«-dığı» — «insanlık»ın sıfatı."),
  ta_pron("قَادَتْهَا", "qada-lead", "قَادَتْ", "هَا", "pron-3fs", "«led»", "«yönetti»", tags=[MW, "hollow-verbs"], extra=" — صِلَةُ الْمَوْصُولِ"),
  tok("أُورُبَّا", "urubba", "propn", [FL, MM], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«Europe» — the doer.", "«Avrupa» — fâil."),
  tok("زَمَنًا", "zaman-period", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«for an age»", "«bir zaman»"),
  naat("طَوِيلًا", "tawil-long", "«long»", "«uzun»", case="nasb", punct="،"),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not»", "«ve … -maz»", segments=wa_("لَا", "la-nafiya", "part")),
  tok("تَزَالُ", "zala", "verb", [KN, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ (لَا يَعْمَلُ إِلَّا مَسْبُوقًا بِنَفْيٍ)، وَاسْمُهُ مُسْتَتِرٌ: هِيَ (أُورُبَّا).", "«still» — lā tazālu: a sister of kāna that works only after a negation.", "«hâlâ … -dır» — ancak nefiyden sonra amel eden kâne kardeşi."),
  tok("مُسَيْطِرَةً", "musaytir", "noun", [KN, "ism-fail"], "خَبَرُ لَا تَزَالُ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ مِنْ سَيْطَرَ (رُبَاعِيٌّ).", "«dominating» — the khabar; a participle of the quadriliteral sayṭara.", "«hükmeden» — haber; dört harfli saytara'nın ism-i fâili."),
  prep_pron("عَلَيْهَا", "ala", "هَا", "pron-3fs", "«over it»", "«ona»"),
  tok("وَمُتَحَكِّمَةً", "mutahakkim-controlling", "noun", [AT, KN, "ism-fail", "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمُتَحَكِّمَةً مَعْطُوفٌ عَلَى الْخَبَرِ مَنْصُوبٌ.", "«and controlling» — joined to the khabar.", "«ve denetleyen» — habere atıf.", segments=wa_("مُتَحَكِّمَةً", "mutahakkim-controlling", "noun")),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«it»", "«onu»", punct="."),
])
sen("s12", "«And to God belongs the command before and after.» (30:4) — [the END of the story of ʿĪsā, and of the book.]",
        "«Önce de sonra da emir Allah'ındır.» (Rûm 4) — [Îsâ kıssasının ve kitabın SONU.]", [
  *quran([
  tok("وَلِلّٰهِ", "allah", "propn", [AT, HJ, MK], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and to God» — the fronted khabar.", "«ve Allah'ındır» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("الْأَمْرُ", "amr", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the command» — the delayed mubtadaʾ.", "«emir» — sonraya bırakılmış mübtedâ."),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  tok("قَبْلُ", "qablu", "noun", [HJ, "hadhf-wa-taqdir"], "ظَرْفٌ مَقْطُوعٌ عَنِ الْإِضَافَةِ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — نُوِيَ مَعْنَى الْمُضَافِ إِلَيْهِ: مِنْ قَبْلِ ذٰلِكَ.", "«before» — a ẓarf cut from its annexation, built on ḍamma.", "«önce» — izafetten kesilmiş, zamme üzere mebnî zarf."),
  wa_prep("وَمِنْ", "min", "«and [from]»", "«ve -den»"),
  tok("بَعْدُ", "badu-after", "noun", [HJ, "hadhf-wa-taqdir"], "ظَرْفٌ مَقْطُوعٌ عَنِ الْإِضَافَةِ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ.", "«after» — likewise built on ḍamma.", "«sonra» — aynı şekilde zamme üzere mebnî.", punct="."),
  ]),
])

CAND = {
 "intaqala": G("intaqala", "انْتَقَلَ", "ن ق ل", "verb", "to move on, to be transferred (Form VIII)", "geçmek, intikal etmek (iftiâl)", 1),
 "masihiyya": G("masihiyya", "مَسِيحِيَّة", "م س ح", "noun", "Christianity", "Hıristiyanlık, Mesîhîlik", 1),
 "urubba": G("urubba", "أُورُبَّا", None, "propn", "Europe", "Avrupa", 1),
 "dafi": G("dafi", "دَافِع", "د ف ع", "noun", "an impulse, a motive", "saik, güdü", 2),
 "safir": G("safir", "سَافِر", "س ف ر", "noun", "open, unveiled, barefaced", "açık, örtüsüz", 2),
 "dhaqan": G("dhaqan", "ذَقَن", "ذ ق ن", "noun", "a chin", "çene", 1, plural="أَذْقَان"),
 "tasawwara": G("tasawwara", "تَصَوَّرَ", "ص و ر", "verb", "to picture to oneself, to imagine (Form V)", "tasavvur etmek (tefe''ul)", 1),
 "shakl": G("shakl", "شَكْل", "ش ك ل", "noun", "a shape, a form", "şekil, biçim", 1, plural="أَشْكَال"),
 "shatta": G("shatta", "شَتَّى", "ش ت ت", "noun", "sundry, diverse (a plural of shatīt)", "türlü, çeşitli", 2),
 "nahata": G("nahata", "نَحَتَ", "ن ح ت", "verb", "to carve, to hew", "yontmak", 1),
 "mabad": G("mabad", "مَعْبَد", "ع ب د", "noun", "a temple, a place of worship", "mabet, tapınak", 1, plural="مَعَابِد"),
 "haykal": G("haykal", "هَيْكَل", "ه ي ك ل", "noun", "a shrine, a temple; a structure", "tapınak; yapı, iskelet", 2, plural="هَيَاكِل"),
 "qahr": G("qahr", "قَهْر", "ق ه ر", "noun", "conquest, overpowering", "kahır, üstün gelme", 1),
 "rumiyya": G("rumiyya", "رُومِيَّة", "ر و م", "noun", "Rome (the Roman state); Roman (fem.)", "Roma; Roma'ya ait (dişil)", 2),
 "ariq": G("ariq", "عَرِيق", "ع ر ق", "noun", "deep-rooted, of ancient stock", "köklü, asil", 2),
 "khurafa": G("khurafa", "خُرَافَة", "خ ر ف", "noun", "a superstition, a fable", "hurafe", 1, plural="خُرَافَات"),
 "imtazaja": G("imtazaja", "اِمْتَزَجَ", "م ز ج", "verb", "to blend, to mingle (Form VIII)", "karışmak, kaynaşmak (iftiâl)", 2),
 "majra": G("majra", "مَجْرَى", "ج ر ي", "noun", "a course, a channel (a noun of place)", "mecrâ, akış yolu", 2),
 "ruman": G("ruman", "الرُّومَان", "ر و م", "propn", "the Romans", "Romalılar", 1),
 "nasraniyya": G("nasraniyya", "نَصْرَانِيَّة", "ن ص ر", "noun", "Christianity", "Hıristiyanlık, Nasrânîlik", 1),
 "tanassara": G("tanassara", "تَنَصَّرَ", "ن ص ر", "verb", "to become a Christian (Form V)", "Hıristiyan olmak (tefe''ul)", 2),
 "qustantin": G("qustantin", "قُسْطَنْطِين", None, "propn", "Constantine", "Konstantin", 1),
 "ihtadana": G("ihtadana", "اِحْتَضَنَ", "ح ض ن", "verb", "to embrace, to take to one's bosom (Form VIII)", "bağrına basmak, kucaklamak (iftiâl)", 2),
 "tabanna": G("tabanna", "تَبَنَّى", "ب ن و", "verb", "to adopt (as a son; a cause) (Form V)", "evlât edinmek; benimsemek (tefe''ul)", 2),
 "rasmi": G("rasmi", "رَسْمِيّ", "ر س م", "noun", "official", "resmî", 1),
 "taqlid": G("taqlid", "تَقْلِيد", "ق ل د", "noun", "a tradition; imitation", "gelenek; taklit", 1, plural="تَقَالِيد"),
 "yunani": G("yunani", "يُونَانِيّ", None, "noun", "Greek", "Yunan, Yunanlı", 1),
 "dana": G("dana", "دَنَا", "د ن و", "verb", "to draw near", "yaklaşmak", 1),
 "ruwaydan": G("ruwaydan", "رُوَيْدًا", "ر و د", "noun", "gently, little by little (a diminutive maṣdar)", "yavaş yavaş (tasğir edilmiş masdar)", 2),
 "faqada": G("faqada", "فَقَدَ", "ف ق د", "verb", "to lose", "yitirmek, kaybetmek", 1),
 "asala-authenticity": G("asala-authenticity", "أَصَالَة", "أ ص ل", "noun", "authenticity, genuineness", "asalet, özgünlük", 2),
 "basata-simplicity": G("basata-simplicity", "بَسَاطَة", "ب س ط", "noun", "simplicity", "sadelik", 1),
 "sharqi": G("sharqi", "شَرْقِيّ", "ش ر ق", "noun", "Eastern", "Doğulu, şarklı", 1),
 "tawhidi": G("tawhidi", "تَوْحِيدِيّ", "و ح د", "noun", "of tawḥīd, monotheistic", "tevhidî", 2),
 "munafiq": G("munafiq", "مُنَافِق", "ن ف ق", "noun", "a hypocrite", "münafık", 1),
 "taama": G("taama", "طَعَّمَ", "ط ع م", "verb", "to graft; to inoculate (Form II)", "aşılamak (tef'îl)", 2),
 "dhawq": G("dhawq", "ذَوْق", "ذ و ق", "noun", "taste", "zevk", 1, plural="أَذْوَاق"),
 "sawa": G("sawa", "سَوَاء", "س و ي", "noun", "equal, alike", "eşit, müsâvi", 1),
 "sara-travel": G("sara-travel", "سَارَ", "س ي ر", "verb", "to walk, to travel", "yürümek, gitmek", 1),
 "zahif": G("zahif", "زَاحِف", "ز ح ف", "noun", "advancing, creeping forward", "ilerleyen, sürünerek yayılan", 2),
 "darb-road": G("darb-road", "دَرْب", "د ر ب", "noun", "a road, a path", "yol, patika", 1, plural="دُرُوب"),
 "salaka": G("salaka", "سَلَكَ", "س ل ك", "verb", "to take (a road); salaka bihi: to lead someone along", "(yola) girmek, yürümek; birini yürütmek", 1),
 "salik": G("salik", "سَالِك", "س ل ك", "noun", "a wayfarer, one who travels a road", "yolcu, yolda giden", 1),
 "wasala-iii": G("wasala-iii", "وَاصَلَ", "و ص ل", "verb", "to continue, to keep on (Form III)", "sürdürmek, devam etmek (müfâale)", 1),
 "sayr": G("sayr", "سَيْر", "س ي ر", "noun", "walking, going", "yürüyüş, gidiş", 1),
 "iltaqa": G("iltaqa", "اِلْتَقَى", "ل ق ي", "verb", "to meet (Form VIII)", "karşılaşmak, kesişmek (iftiâl)", 1),
 "diyana": G("diyana", "دِيَانَة", "د ي ن", "noun", "a religion, a creed", "din, diyanet", 1),
 "wasafa": G("wasafa", "وَصَفَ", "و ص ف", "verb", "to describe", "nitelemek, vasfetmek", 1),
 "dalal": G("dalal", "ضَلَال", "ض ل ل", "noun", "straying, error", "sapıklık, dalâlet", 1),
 "maghdubiyya": G("maghdubiyya", "مَغْضُوبِيَّة", "غ ض ب", "noun", "the state of being the object of wrath (an abstract noun)", "gazaba uğramışlık (masdar-ı sınâî)", 3),
 "maghdub": G("maghdub", "مَغْضُوب", "غ ض ب", "noun", "the object of wrath (a passive participle)", "gazaba uğramış (ism-i mef'ûl)", 1),
 "masat": G("masat", "مَأْسَاة", "أ س و", "noun", "a tragedy", "trajedi, facia", 1, plural="مَآسٍ"),
 "qada-lead": G("qada-lead", "قَادَ", "ق و د", "verb", "to lead, to drive", "yönetmek, sürmek", 1),
 "musaytir": G("musaytir", "مُسَيْطِر", "س ي ط ر", "noun", "dominating (a participle of the quadriliteral sayṭara)", "hükmeden, hâkim (dört harfli saytara'nın ism-i fâili)", 2),
 "mutahakkim-controlling": G("mutahakkim-controlling", "مُتَحَكِّم", "ح ك م", "noun", "controlling, holding sway over (Form V participle)", "denetimi altında tutan (tefe''ul ism-i fâili)", 2),
 "qablu": G("qablu", "قَبْلُ", "ق ب ل", "noun", "before (cut from annexation: min qablu)", "önce (izafetten kesilmiş: min kablü)", 1),
 "sarraha": G("sarraha", "صَرَّحَ", "ص ر ح", "verb", "to declare openly (Form II)", "açıkça söylemek, tasrih etmek (tef'îl)", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it", "onu / onun (dişil)", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them / their", "onları / onların", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "him / his / it", "onu / onun", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masc. sing.)", "seni / senin", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "nahata", _sg.sound1("daraba", "نَحَت", "نْحِت", "اِنْحِت", "نَحْت", "نَاحِت", "مَنْحُوت", "نُحِتَ", "يُنْحَتُ", "نَحَتَ الْحَجَرَ يَنْحِتُهُ: قَطَعَهُ وَسَوَّاهُ تِمْثَالًا."))
put_morph(mo, "imtazaja", _sg.derived(_sg.B8, _sg.W8, "َ", "اِمْتَزَج", "مْتَزِج", "اِمْتَزِج", "اِمْتِزَاج", "مُمْتَزِج", None, None, None, "اِمْتَزَجَ الشَّيْءَانِ: اخْتَلَطَا."))
put_morph(mo, "tanassara", _sg.derived(_sg.B5, _sg.W5, "َ", "تَنَصَّر", "تَنَصَّر", "تَنَصَّر", "تَنَصُّر", "مُتَنَصِّر", None, None, None, "تَنَصَّرَ: دَخَلَ فِي النَّصْرَانِيَّةِ."))
put_morph(mo, "ihtadana", _sg.derived(_sg.B8, _sg.W8, "َ", "اِحْتَضَن", "حْتَضِن", "اِحْتَضِن", "اِحْتِضَان", "مُحْتَضِن", "مُحْتَضَن", "اُحْتُضِنَ", "يُحْتَضَنُ", "اِحْتَضَنَهُ: ضَمَّهُ إِلَى حِضْنِهِ؛ وَاحْتَضَنَ الدَّعْوَةَ: تَبَنَّاهَا وَرَعَاهَا."))
put_morph(mo, "tabanna", _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَبَنَّ", "تَبَنّ", "a", "تَبَنّ", "تَبَنٍّ (التَّبَنِّي)", "مُتَبَنٍّ (الْمُتَبَنِّي)", "مُتَبَنًّى", "تُبُنِّيَ", "يُتَبَنَّى", "تَبَنَّى الصَّبِيَّ: اتَّخَذَهُ ابْنًا؛ وَتَبَنَّى الْفِكْرَةَ: أَخَذَ بِهَا — نَاقِصٌ يَائِيٌّ."))
put_morph(mo, "taama", _sg.derived(_sg.B2, _sg.W2, "ُ", "طَعَّم", "طَعِّم", "طَعِّم", "تَطْعِيم", "مُطَعِّم", "مُطَعَّم", "طُعِّمَ", "يُطَعَّمُ", "طَعَّمَ الشَّجَرَةَ: أَدْخَلَ فِيهَا غُصْنًا مِنْ غَيْرِهَا؛ وَطَعَّمَ الدِّينَ بِكَذَا: خَلَطَهُ بِهِ."))
put_morph(mo, "salaka", _sg.sound1("nasara", "سَلَك", "سْلُك", "اُسْلُك", "سُلُوك", "سَالِك", "مَسْلُوك", "سُلِكَ", "يُسْلَكُ", "سَلَكَ الطَّرِيقَ يَسْلُكُهُ: مَشَى فِيهِ؛ وَسَلَكَ بِهِ الطَّرِيقَ: أَدْخَلَهُ فِيهِ."))
put_morph(mo, "iltaqa", _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِلْتَقَ", "لْتَق", "i", "اِلْتَق", "اِلْتِقَاء", "مُلْتَقٍ (الْمُلْتَقِي)", "مُلْتَقًى", None, None, "اِلْتَقَى بِهِ وَالْتَقَاهُ: لَقِيَهُ وَاجْتَمَعَ بِهِ — نَاقِصٌ يَائِيٌّ."))
put_morph(mo, "qada-lead", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "قَاد", "قُد", "قُود", "قُد", "قُد", "قُد", "قِيَادَة / قَوْد", "قَائِد", "مَقُود", "قِيدَ", "يُقَادُ", "قَادَ الدَّابَّةَ يَقُودُهَا: مَشَى أَمَامَهَا آخِذًا بِمِقْوَدِهَا؛ وَقَادَ الْقَوْمَ: تَزَعَّمَهُمْ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch45 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 45 (print pp. 68–70; ʿĪsā §42 — the END of the book): from an obscure creed to open idolatry — the preachers move to Europe, where idolatry had sunk in to the chins: the Greeks with their sundry gods, statues and temples, Rome deep-rooted in superstition (s1–s3); Constantine turns Christian in 306 and Christianity takes on idolatrous creeds, Roman traditions and Greek philosophy, losing its prophetic authenticity (s4–s5); the author's footnote: the Messiah was sent to the lost sheep of Israel (s6); the straying wayfarer (s7–s8); why the Qurʾān calls them astray and the Jews the objects of wrath — al-Fātiḥa 1:6–7 (s9–s10); a tragedy for Europe and for humanity (s11); «to God belongs the command before and after» (s12)."
ADD_TR = " Kırk beşinci bölüm (baskı s. 68–70; Îsâ §42 — kitabın SONU): kapalı bir akideden açık putperestliğe — davetçiler, putperestliğin çenelere kadar gömüldüğü Avrupa'ya geçer: türlü ilâhları, heykelleri ve tapınaklarıyla Yunanlılar, hurafede köklü Roma (s1–s3); Konstantin 306'da Hıristiyan olur ve Hıristiyanlık putperest akideleri, Roma geleneklerini ve Yunan felsefesini alarak peygamberlik asaletini yitirir (s4–s5); yazarın dipnotu: Mesîh İsrâil'in kaybolmuş koyunlarına gönderilmişti (s6); yoldan sapan yolcu (s7–s8); Kur'ân'ın onları sapmış, Yahudileri gazaba uğramış diye nitelemesi — Fâtiha 6–7 (s9–s10); Avrupa ve insanlık için bir trajedi (s11); «önce de sonra da emir Allah'ındır» (s12)."
write_out(45, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §42 + 1:6–7, 30:4 — END", GLOSS_ADD, notes=(), related=())
report(45, S, GLOSS_ADD, ())
