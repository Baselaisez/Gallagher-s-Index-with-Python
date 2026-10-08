# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 31: «قِصَّةُ عِيسَى» §12 continued — Āl ʿImrān 3:48–51: the Book, the Wisdom, the Torah and the Injīl; a messenger to the Children of Israel with the signs (the clay bird, the blind-born and the leper, the dead, what is eaten and stored); confirming the Torah, making lawful some of what was forbidden; «God is my Lord and your Lord, so worship Him»; print pp. 47–48.
python3 tools/authoring/author_qisas4_ch31.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى فِي الْقُرْآنِ: رَسُولًا إِلَى بَنِي إِسْرَائِيلَ (آل عمران ٤٨–٥١)", "en": "The story of ʿĪsā in the Qurʾān: a messenger to the Children of Israel (3:48–51)", "tr": "Kur'ân'da Îsâ kıssası: İsrâiloğulları'na bir resul (Âl-i İmrân 48–51)"}
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

# ---------------------------------------------------------------- §12 (continued): آل عمران ٤٨–٥١ (print pp. 47–48)
sen("s1", "«And He will teach him the Book and the Wisdom, and the Torah and the Injīl,» (3:48)",
        "«Ona Kitab'ı ve hikmeti, Tevrat'ı ve İncil'i öğretecek,» (3:48)", [
  *quran([
  tok("وَيُعَلِّمُهُ", "allama", "verb", [AT, MX, "mudari-marfu", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيُعَلِّمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (اللهُ)، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ — مَعْطُوفٌ عَلَى يُبَشِّرُكِ (أَوْ عَلَى جُمْلَةٍ مُقَدَّرَةٍ).", "«and He will teach him» — two objects; the hāʾ is the first.", "«ve ona öğretecek» — iki mef'ûl; hâ ilki.", segments=[seg("وَ", "wa", "conj"), seg("يُعَلِّمُ", "allama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  maful_("الْكِتَابَ", "kitab", "«the Book»", "«Kitab'ı»", tags=[MX], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  atf("وَالْحِكْمَةَ", "hikma", "«the Wisdom»", "«hikmeti»", "nasb"),
  atf("وَالتَّوْرَاةَ", "tawrat", "«the Torah»", "«Tevrat'ı»", "nasb"),
  atf("وَالْإِنْجِيلَ", "injil", "«the Injīl»", "«İncil'i»", "nasb", punct=AYA),
  ]),
])
sen("s2", "«and [make him] a messenger to the Children of Israel: I have come to you with a sign from your Lord — that I fashion for you out of clay the likeness of a bird, then breathe into it and it becomes a bird by God's leave;» (3:49)",
        "«ve İsrâiloğulları'na bir resul olarak: Ben size Rabbinizden bir âyetle geldim; size çamurdan kuş biçiminde bir şey yapar, ona üflerim de Allah'ın izniyle kuş oluverir;» (3:49)", [
  *quran([
  tok("وَرَسُولًا", "rasul", "noun", [AT, HL, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَرَسُولًا مَعْطُوفٌ عَلَى وَجِيهًا (حَالٌ)، أَوْ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: وَيَجْعَلُهُ رَسُولًا.", "«and a messenger» — joined to «eminent» as a ḥāl, or the object of an understood «and makes him».", "«ve bir resul» — «itibarlı»ya ma'tûf hâl, yahut mahzuf «onu kılar» fiilinin mef'ûlü.", segments=wa_("رَسُولًا", "rasul", "noun")),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("بَنِي", "banu-israil", "noun", [HJ, ID, JS], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«the Children [of]» — jarr by the yāʾ, the nūn dropped for the annexation.", "«oğulları» — yâ ile mecrûr, nûnu izâfet için düştü."),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Israel» — a diptote.", "«İsrâil» — gayr-i munsarıf."),
  tok("أَنِّي", "anna", "part", [IW, "hadhf-al-jarr"], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِحَرْفِ جَرٍّ مَحْذُوفٍ: بِأَنِّي، مُتَعَلِّقٌ بِرَسُولًا.", "«[saying] that I» — anna with the yāʾ; the clause is governed by an understood bi.", "«… ki ben» — enne ile yâ; mukadder bâ ile mecrûr.", segments=[seg("أَنِّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«[indeed]»", "«[gerçekten]»"),
  jitukum(),
  *bi_aya(),
  tok("أَنِّي", "anna", "part", [IW, BD], "أَنَّ وَالْيَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ بَدَلٌ مِنْ آيَةٍ (أَوْ خَبَرُ مُبْتَدَأٍ مَحْذُوفٍ: هِيَ أَنِّي).", "«that I» — the clause is a badal of «a sign».", "«ki ben» — te'vîl-i masdar «âyet»ten bedel.", segments=[seg("أَنِّ", "anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَخْلُقُ", "khalaqa", "verb", [IW, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«I fashion» — anna's khabar.", "«yaparım» — enne'nin haberi."),
  li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«for you»", "«size»"),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«out of»", "«-den»"),
  majrur("الطِّينِ", "tin", "«clay»", "«çamurdan»"),
  tok("كَهَيْئَةِ", "haya-shape", "noun", [HJ, ID, MB], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَهَيْئَةِ مَجْرُورٌ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَوْضِعِ الْمَفْعُولِ بِهِ عَلَى حَذْفِ مَوْصُوفٍ: شَيْئًا كَهَيْئَةِ الطَّيْرِ.", "«the likeness [of]» — stands as the object of an understood «a thing».", "«… biçiminde» — mahzuf «bir şey»in yerinde mef'ûl.", segments=[seg("كَ", "ka", "prep"), seg("هَيْئَةِ", "haya-shape", "noun")]),
  mudaf_ilayh("الطَّيْرِ", "tayr", "«a bird»", "«kuşun»"),
  tok("فَأَنْفُخُ", "nafakha", "verb", [AT, "mudari-marfu"], "الْفَاءُ عَاطِفَةٌ، وَأَنْفُخُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«then I breathe»", "«sonra üflerim»", segments=[seg("فَ", "fa", "conj"), seg("أَنْفُخُ", "nafakha", "verb")]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«into it»", "«ona»"),
  tok("فَيَكُونُ", "kana", "verb", [AT, KN, "hollow-verbs", "mudari-marfu"], "الْفَاءُ عَاطِفَةٌ، وَيَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and it becomes»", "«ve … olur»", segments=[seg("فَ", "fa", "conj"), seg("يَكُونُ", "kana", "verb")]),
  tok("طَيْرًا", "tayr", "noun", [KN], "خَبَرُ يَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a bird» — the khabar.", "«kuş» — haber."),
  *bi_idhn(),
  ]),
])
sen("s3", "«and I cure the blind-born and the leper, and give life to the dead by God's leave, and I tell you of what you eat and what you store in your houses. In that is surely a sign for you, if you are believers.» (3:49)",
        "«Anadan doğma körü ve alacalıyı iyi ederim, Allah'ın izniyle ölüleri diriltirim; yediklerinizi ve evlerinizde biriktirdiklerinizi size haber veririm. Eğer inananlar iseniz bunda sizin için elbette bir âyet vardır.» (3:49)", [
  *quran([
  mudari_wa("وَأُبْرِئُ", "abraa", "«and I cure»", "«ve iyi ederim»", tags=["form-iv-verbs"], hidden="أَنَا", extra=" — مَهْمُوزُ اللَّامِ"),
  maful_("الْأَكْمَهَ", "akmah", "«the blind-born»", "«anadan doğma körü»"),
  atf("وَالْأَبْرَصَ", "abras", "«the leper»", "«alacalıyı»", "nasb"),
  mudari_wa("وَأُحْيِي", "ahya", "«and I give life to»", "«ve diriltirim»", tags=["naqis-verbs", "form-iv-verbs"], hidden="أَنَا", sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ"),
  maful_("الْمَوْتَى", "mayyit", "«the dead»", "«ölüleri»", tags=[JT, "ism-maqsur-manqus"], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ."),
  *bi_idhn(),
  tok("وَأُنَبِّئُكُمْ", "nabbaa", "verb", [AT, MB, "mudari-marfu", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأُنَبِّئُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ — مَهْمُوزُ اللَّامِ.", "«and I tell you» — the kāf is the object.", "«ve size haber veririm» — kâf mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("أُنَبِّئُ", "nabbaa", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  bi_ma(),
  khamsa("تَأْكُلُونَ", "akala", "«you eat»", "«yediklerinizi»", tags=[MW], extra_ar=" — وَالْجُمْلَةُ صِلَةٌ، وَالْعَائِدُ مَحْذُوفٌ: تَأْكُلُونَهُ"),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مَعْطُوفٌ عَلَى مَا الْأُولَى.", "«and what» — a second relative, joined.", "«ve … -diklerinizi» — ilk mâ'ya ma'tûf ikinci mevsûl.", segments=wa_("مَا", "ma-mawsula", "pron")),
  khamsa("تَدَّخِرُونَ", "iddakhara", "«you store»", "«biriktirdiklerinizi»", tags=[MW, "form-viii-verbs"], extra_ar=" — صِلَةٌ؛ أَصْلُهُ تَذْتَخِرُونَ"),
  fi(),
  noun_pron("بُيُوتِكُمْ", "bayt", "بُيُوتِ", "كُمْ", "pron-2mp", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«your houses»", "«evlerinizde»", tags=[HJ, ID, JT]),
  inna(),
  prep("فِي", "fi", "«in»", "«-de»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ مُقَدَّمٌ."),
  tok("ذٰلِكَ", "dhalika", "pron", [HJ, IW, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«that» — in the place of jarr.", "«bunda» — mahallen mecrûr."),
  tok("لَآيَةً", "aya", "noun", [IW, "tawkid"], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ لِلتَّوْكِيدِ، وَآيَةً اسْمُ إِنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«surely a sign» — the emphatic lām slid onto inna's delayed ism.", "«elbette bir âyet» — inne'nin sonraya kalan ismine kayan te'kid lâmı.", segments=[seg("لَ", "lam-ibtida", "part"), seg("آيَةً", "aya", "noun")]),
  li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«for you» — a ṣifa of «a sign».", "«sizin için» — âyetin sıfatı.", tags=[NA], extra=" — صِفَةٌ لِآيَةً"),
  tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if» — the jussive conditional.", "«eğer» — cezm eden şart harfi."),
  tok("كُنْتُمْ", "kana", "verb", [SH, KN, "hollow-verbs", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهُ — حُذِفَتْ عَيْنُهُ وَضُمَّ مَا قَبْلَهَا (كُنْتُمْ)؛ وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«you are» — the condition's verb; its answer is understood from what precedes.", "«iseniz» — şart fiili; cevabı öncesinden anlaşılır.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("مُؤْمِنِينَ", "mumin", "noun", [KN, JS, "ism-fail", "form-iv-verbs"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«believers» — kāna's khabar, naṣb by the yāʾ.", "«inananlar» — kâne'nin haberi, yâ ile mansub.", punct=AYA),
  ]),
])
sen("s4", "«and confirming what is before me of the Torah, and to make lawful for you some of what was forbidden to you; and I have come to you with a sign from your Lord, so fear God and obey me.» (3:50)",
        "«Önümdeki Tevrat'ı doğrulayıcı olarak ve size haram kılınanın bir kısmını helâl kılmak için [geldim]; size Rabbinizden bir âyetle geldim; artık Allah'tan sakının ve bana itaat edin.» (3:50)", [
  *quran([
  tok("وَمُصَدِّقًا", "musaddiq", "noun", [AT, HL, "hadhf-wa-taqdir", "ism-fail", "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمُصَدِّقًا حَالٌ مَنْصُوبٌ مَعْطُوفٌ عَلَى رَسُولًا (أَوْ حَالٌ مِنْ فِعْلٍ مَحْذُوفٍ: جِئْتُكُمْ مُصَدِّقًا).", "«and confirming» — a ḥāl joined to «a messenger», or of an understood «I have come».", "«ve doğrulayıcı olarak» — «bir resul»e ma'tûf hâl, yahut mahzuf «geldim»in hâli.", segments=wa_("مُصَدِّقًا", "musaddiq", "noun")),
  tok("لِمَا", "ma-mawsula", "pron", [HJ, MW], "اللَّامُ حَرْفُ جَرٍّ لِتَقْوِيَةِ الْعَامِلِ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — مَفْعُولُ مُصَدِّقًا فِي الْمَعْنَى.", "«what» — the lām strengthens the participle's government over the relative.", "«… -ı» — lâm ism-i fâilin amelini takviye eder.", segments=[seg("لِ", "li", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("بَيْنَ", "bayna", "noun", [MF, ID, "hadhf-wa-taqdir"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِصِلَةٍ مَحْذُوفَةٍ: اسْتَقَرَّ، مُضَافٌ.", "«between» — attached to the understood ṣila «is».", "«arasında» — mahzuf sılaya bağlı."),
  tok("يَدَيَّ", "yad", "noun", [ID, "al-muthanna", "ya-al-mutakallim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَأُدْغِمَتْ يَاؤُهُ فِي يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — بَيْنَ يَدَيَّ: أَمَامِي.", "«my two hands» — a dual in jarr whose yāʾ merges with the speaker's yāʾ; «before me».", "«iki elim» — yâ'sı mütekellim yâ'sıyla idgam edilen tesniye; «önümde».", segments=[seg("يَدَ", "yad", "noun"), seg("يَّ", "pron-1s", "pron")]),
  tok("مِنَ", "min", "prep", [HJ, HL], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنْ مَا.", "«of» — explanatory min; the phrase is a ḥāl of the relative.", "«-den» — beyan için min; ibare mâ'nın hâli."),
  majrur("التَّوْرَاةِ", "tawrat", "«the Torah»", "«Tevrat»"),
  tok("وَلِأُحِلَّ", "ahalla", "verb", [AT, TA, AN, "doubled-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لَامُ التَّعْلِيلِ، وَأُحِلَّ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ، مُتَعَلِّقٌ بِمَحْذُوفٍ: جِئْتُكُمْ.", "«and to make lawful» — the lām of purpose with a concealed an; attached to an understood «I have come».", "«ve helâl kılmak için» — ta'lil lâmı, gizli en ile; mahzuf «geldim»e bağlı.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "lam-taleel", "part"), seg("أُحِلَّ", "ahalla", "verb")]),
  li_pron("لَكُمْ", "كُمْ", "pron-2mp", "«for you»", "«size»"),
  maful_("بَعْضَ", "bad", "«some [of]»", "«bir kısmını»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  tok("الَّذِي", "alladhi", "pron", [ID, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«what» — the relative as muḍāf ilayh.", "«… -ın» — muzâfun ileyh olan mevsûl."),
  tok("حُرِّمَ", "harrama", "verb", [MW, NF, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِلَةٌ.", "«was forbidden» — a passive; the ṣila.", "«haram kılındı» — meçhul; sıla."),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«to you»", "«size»"),
  jitukum(wa=True),
  *bi_aya(),
  tok("فَاتَّقُوا", "ittaqa", "verb", [AT, AM, "naqis-verbs", "form-viii-verbs"], "الْفَاءُ الْفَصِيحَةُ (لِلتَّفْرِيعِ)، وَاتَّقُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — حُذِفَتْ لَامُهُ (الْيَاءُ) قَبْلَ وَاوِ الْجَمَاعَةِ.", "«so fear» — the fāʾ of consequence; an imperative on the group's wāw, its defective yāʾ dropped.", "«artık sakının» — netice fâ'sı; cemi vâvlı emir, nâkıs yâ düştü.", segments=[seg("فَ", "fa", "conj"), seg("اتَّقُوا", "ittaqa", "verb")]),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'tan» — mef'ûl."),
  tok("وَأَطِيعُونِ", "ataa", "verb", [AT, AM, MB, "hollow-verbs", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَطِيعُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ الْمَحْذُوفَةُ (اكْتِفَاءً بِالْكَسْرَةِ) مَفْعُولٌ بِهِ.", "«and obey me» — the nūn of protection; the speaker's yāʾ is dropped, its kasra remaining.", "«ve bana itaat edin» — vikâye nûnu; mütekellim yâ'sı düşmüş, kesresi kalmış.", segments=[seg("وَ", "wa", "conj"), seg("أَطِيعُو", "ataa", "verb"), seg("نِ", "nun-wiqaya", "part")], punct=AYA),
  ]),
])
sen("s5", "«Indeed God is my Lord and your Lord, so worship Him. This is a straight path.» (3:51)",
        "«Şüphesiz Allah benim de Rabbim, sizin de Rabbinizdir; öyleyse O'na kulluk edin. İşte bu dosdoğru yoldur.» (3:51)", [
  *quran([
  inna(),
  tok("اللهَ", "allah", "propn", [IW], "لَفْظُ الْجَلَالَةِ اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "«God» — inna's ism.", "«Allah» — inne'nin ismi."),
  tok("رَبِّي", "rabb", "noun", [IW, ID, "ya-al-mutakallim"], "خَبَرُ إِنَّ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — inna's khabar; the speaker's yāʾ hides the ḍamma.", "«Rabbim» — inne'nin haberi; mütekellim yâ'sı dammeyi gizler.", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
  pron_atf("وَرَبُّكُمْ", "rabb", "رَبُّ", "كُمْ", "pron-2mp", "«your Lord»", "«Rabbiniz»", case="raf"),
  tok("فَاعْبُدُوهُ", "abada", "verb", [AT, AM, MB], "الْفَاءُ الْفَصِيحَةُ، وَاعْبُدُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«so worship Him» — an imperative on the group's wāw; the hāʾ the object.", "«öyleyse O'na kulluk edin» — cemi vâvlı emir; hâ mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("اعْبُدُو", "abada", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«işte bu» — mübtedâ."),
  tok("صِرَاطٌ", "sirat", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a path» — the khabar.", "«bir yol» — haber."),
  naat("مُسْتَقِيمٌ", "mustaqim", "«straight»", "«dosdoğru»", case="raf", tags=["ism-fail", "form-x-verbs"], punct=AYA),
  ]),
])

CAND = {
 "allama": G("allama", "عَلَّمَ", "ع ل م", "verb", "to teach (Form II)", "öğretmek (tef'îl)", 1),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a book; the Book", "kitap", 1, plural="كُتُب"),
 "hikma": G("hikma", "حِكْمَة", "ح ك م", "noun", "wisdom", "hikmet", 1),
 "tawrat": G("tawrat", "التَّوْرَاة", None, "propn", "the Torah", "Tevrat", 1),
 "injil": G("injil", "إِنْجِيل", None, "propn", "the Injīl (the Gospel)", "İncil", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resul", 1, plural="رُسُل"),
 "banu-israil": G("banu-israil", "بَنُو إِسْرَائِيلَ", "ب ن ي", "noun", "the Children of Israel", "İsrâiloğulları", 1),
 "israil": G("israil", "إِسْرَائِيل", None, "propn", "Israel (Yaʿqūb)", "İsrâil (Yâkub)", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "jaa": G("jaa", "جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (pl.)", "siz / sizi / sizin", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "khalaqa": G("khalaqa", "خَلَقَ", "خ ل ق", "verb", "to create; to fashion", "yaratmak; şekil vermek", 1),
 "tin": G("tin", "طِين", "ط ي ن", "noun", "clay", "çamur", 1),
 "haya-shape": G("haya-shape", "هَيْئَة", "ه ي أ", "noun", "a form, a shape", "biçim, şekil, heyet", 2),
 "tayr": G("tayr", "طَيْر", "ط ي ر", "noun", "a bird; birds", "kuş", 1, plural="طُيُور"),
 "nafakha": G("nafakha", "نَفَخَ", "ن ف خ", "verb", "to breathe (fī: into), to blow", "üflemek", 1),
 "idhn": G("idhn", "إِذْن", "أ ذ ن", "noun", "leave, permission", "izin", 1),
 "abraa": G("abraa", "أَبْرَأَ", "ب ر أ", "verb", "to cure (Form IV, hamza-final)", "iyileştirmek (if'âl, mehmûzü'l-lâm)", 2),
 "akmah": G("akmah", "أَكْمَه", "ك م ه", "noun", "blind from birth", "anadan doğma kör", 3),
 "abras": G("abras", "أَبْرَص", "ب ر ص", "noun", "a leper", "alacalı, cüzamlı", 3),
 "ahya": G("ahya", "أَحْيَا", "ح ي ي", "verb", "to give life (Form IV, defective)", "diriltmek (if'âl, nâkıs)", 1),
 "mayyit": G("mayyit", "مَيِّت", "م و ت", "noun", "dead", "ölü", 1, plural="مَوْتَى"),
 "nabbaa": G("nabbaa", "نَبَّأَ", "ن ب أ", "verb", "to inform, to tell (bi: of) (Form II, hamza-final)", "haber vermek (tef'îl, mehmûzü'l-lâm)", 2),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "iddakhara": G("iddakhara", "اِدَّخَرَ", "ذ خ ر", "verb", "to store up, to hoard (Form VIII of ذ خ ر, assimilated)", "biriktirmek, saklamak (iftiâl, idgamlı)", 2),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "a house", "ev", 1, plural="بُيُوت"),
 "lam-ibtida": G("lam-ibtida", "لَ (لَامُ الِابْتِدَاءِ)", None, "part", "the emphatic lām of inception", "ibtidâ (te'kid) lâmı", 2),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (the jussive conditional)", "eğer (cezm eden şart harfi)", 1),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer (an active participle of Form IV)", "mümin (if'âl ism-i fâili)", 1, plural="مُؤْمِنُونَ"),
 "musaddiq": G("musaddiq", "مُصَدِّق", "ص د ق", "noun", "confirming (an active participle of Form II)", "doğrulayan, tasdik edici (tef'îl ism-i fâili)", 2),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1, plural="أَيْدٍ"),
 "lam-taleel": G("lam-taleel", "لِ (التَّعْلِيل)", None, "part", "the lām of purpose (with a concealed an)", "ta'lil lâmı (gizli en ile)", 2),
 "ahalla": G("ahalla", "أَحَلَّ", "ح ل ل", "verb", "to make lawful (Form IV, doubled)", "helâl kılmak (if'âl, muzâaf)", 1),
 "bad": G("bad", "بَعْض", "ب ع ض", "noun", "some, a part", "bazı, bir kısım", 1),
 "alladhi": G("alladhi", "الَّذِي", None, "pron", "who, which (m.)", "ki o, -an", 1),
 "harrama": G("harrama", "حَرَّمَ", "ح ر م", "verb", "to forbid, to make unlawful (Form II)", "haram kılmak (tef'îl)", 1),
 "ittaqa": G("ittaqa", "اِتَّقَى", "و ق ي", "verb", "to fear (God), to be wary of (Form VIII, defective)", "sakınmak (iftiâl, nâkıs)", 1),
 "ataa": G("ataa", "أَطَاعَ", "ط و ع", "verb", "to obey (Form IV, hollow)", "itaat etmek (if'âl, ecvef)", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "tapmak, ibadet etmek", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "sirat": G("sirat", "صِرَاط", "ص ر ط", "noun", "a path", "yol, sırât", 1),
 "mustaqim": G("mustaqim", "مُسْتَقِيم", "ق و م", "noun", "straight (an active participle of Form X)", "dosdoğru, müstakîm (istif'âl ism-i fâili)", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch31 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 31 (print pp. 47–48; ʿĪsā §12 continued): Āl ʿImrān 3:48 the Book, the Wisdom, the Torah and the Injīl (s1); 3:49 a messenger to the Children of Israel — the clay bird (s2), the blind-born, the leper, the dead, what is eaten and stored (s3); 3:50 confirming the Torah, making lawful some of what was forbidden, «fear God and obey me» (s4); 3:51 «God is my Lord and your Lord» (s5)."
ADD_TR = " Otuz birinci bölüm (baskı s. 47–48; Îsâ §12 devam): Âl-i İmrân 48 Kitap, hikmet, Tevrat ve İncil (s1); 49 İsrâiloğulları'na resul — çamurdan kuş (s2), kör, alacalı, ölüler, yenen ve biriktirilen (s3); 50 Tevrat'ı doğrulama, haramın bir kısmını helâl kılma, «Allah'tan sakının, bana itaat edin» (s4); 51 «Allah benim de Rabbim, sizin de Rabbiniz» (s5)."
write_out(31, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā 3:48–51", GLOSS_ADD, notes=(), related=())
report(31, S, GLOSS_ADD, ())
