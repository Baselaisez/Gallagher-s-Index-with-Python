# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 43: «قِصَّةُ عِيسَى» §38 (ʿĪsā calls to the worship of God alone — the two Gospel sayings, Matthew 4:10 and Luke 4:8, then Āl ʿImrān 3:79–80) and §39 (the Qurʾān states ʿĪsā's call outright — al-Māʾida 5:72). Print pp. 64–65.
python3 tools/authoring/author_qisas4_ch43.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: دَعْوَتُهُ إِلَى عِبَادَةِ اللهِ وَحْدَهُ، وَتَصْرِيحُ الْقُرْآنِ بِهَا (آل عمران ٧٩–٨٠، المائدة ٧٢)", "en": "The story of ʿĪsā: his call to the worship of God alone, and the Qurʾān stating it outright (3:79–80, 5:72)", "tr": "Îsâ kıssası: yalnız Allah'a kulluğa daveti ve Kur'ân'ın bunu açıkça bildirmesi (Âl-i İmrân 79–80, Mâide 72)"}
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

# ---------------------------------------------------------------- §38 عِيسَى يَدْعُو إِلَى عِبَادَةِ اللهِ وَحْدَهُ (print p. 64)
def gospel_saying(ref_punct):
    return quran([
  tok("مَكْتُوبٌ", "maktub", "noun", [MK, "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ (أَوْ مُبْتَدَأٌ خَبَرُهُ الْجُمْلَةُ بَعْدَهُ) — اسْمُ مَفْعُولٍ مِنْ كَتَبَ.", "«it is written» — a passive participle; its mubtadaʾ is unspoken.", "«yazılmıştır» — ism-i mef'ûl; mübtedâsı hazfedilmiş."),
  li_noun("لِلرَّبِّ", "rabb", "«to the Lord»", "«Rabb'e»", extra="، مُتَعَلِّقٌ بِتَسْجُدُ، قُدِّمَ عَلَيْهِ لِلْقَصْرِ: لَهُ لَا لِغَيْرِهِ", tags=["qasr"]),
  noun_pron("إِلٰهِكَ", "ilah", "إِلٰهِ", "كَ", "pron-2ms", "بَدَلٌ مِنَ الرَّبِّ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your God» — in apposition to «the Lord».", "«Allah'ına» — «Rabb»den bedel.", tags=[BD, ID]),
  mudari("تَسْجُدُ", "sajada", "«you shall bow»", "«secde edersin»", tags=[MK], hidden="أَنْتَ", punct="،", extra_ar=" — وَالْجُمْلَةُ خَبَرٌ (أَوْ مَقُولُ الْمَكْتُوبِ)"),
  tok("وَلَهُ", "li", "prep", [AT, HJ, "qasr"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِتَعْبُدُ، قُدِّمَ لِلْقَصْرِ.", "«and Him» — fronted for restriction: Him alone.", "«ve yalnız O'na» — hasr için öne alınmış.", segments=[seg("وَ", "wa", "conj"), seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
  tok("وَحْدَهُ", "wahda", "noun", [HL, ID], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرٌ فِي مَوْضِعِ الْحَالِ: مُنْفَرِدًا.", "«alone» — a maṣdar standing as the ḥāl.", "«tek başına» — hâl yerinde masdar.", segments=[seg("وَحْدَ", "wahda", "noun"), seg("هُ", "pron-3ms", "pron")]),
  mudari("تَعْبُدُ", "abada", "«you shall serve»", "«kulluk edersin»", tags=[AT], hidden="أَنْتَ", punct=ref_punct),
  ])
sen("s1", "And he called, like the other prophets, to the worship of God alone; so among his sayings in the Gospel came: «It is written: to the Lord your God you shall bow, and Him alone you shall serve» (Matthew 4:10),",
        "O da diğer peygamberler gibi yalnız Allah'a kulluğa çağırdı; İncil'deki sözlerinden biri şudur: «Yazılmıştır: Rabbin Allah'a secde edeceksin ve yalnız O'na kulluk edeceksin» (Matta 4:10),", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  tok("دَعَا", "daa", "verb", ["naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (عِيسَى).", "«he called» — a defective māḍī; the doer is concealed.", "«davet etti» — nâkıs mâzî; fâil gizli zamir."),
  tok("كَغَيْرِهِ", "ghayr", "noun", [HJ, ID, HL], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَغَيْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«like others [of him]» — the kāf of likening; the phrase is a ḥāl.", "«diğerleri gibi» — teşbih kâfı; hâl.", segments=[seg("كَ", "ka", "part"), seg("غَيْرِ", "ghayr", "noun"), seg("هِ", "pron-3ms", "pron")]),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  majrur("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberler»", tags=[JT, "mamnu-min-sarf"], ar="مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تَكْسِيرٍ عَلَى أَفْعِلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ، جُرَّ بِالْكَسْرَةِ لِدُخُولِ أَلْ."),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("عِبَادَةِ", "ibada", "«the worship [of]»", "«kulluğuna»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'a»"),
  tok("وَحْدَهُ", "wahda", "noun", [HL, ID], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرٌ فِي مَوْضِعِ الْحَالِ: مُنْفَرِدًا.", "«alone» — a maṣdar standing as the ḥāl.", "«tek başına» — hâl yerinde masdar.", punct="،", segments=[seg("وَحْدَ", "wahda", "noun"), seg("هُ", "pron-3ms", "pron")]),
  mazi("فَجَاءَ", "jaa", "«so there came»", "«nitekim … geldi»", tags=[AT, "hollow-verbs"], hidden=None, wa=True, extra_ar="، وَالْفَاعِلُ الْقَوْلُ الْمَحْكِيُّ بَعْدَهُ (مَكْتُوبٌ…) فِي مَحَلِّ رَفْعٍ"),
  prep("مِنْ", "min", "«among»", "«-den»", ar="حَرْفُ جَرٍّ لِلتَّبْعِيضِ."),
  noun_pron("قَوْلِهِ", "qawl", "قَوْلِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his sayings»", "«sözlerinden»", tags=[HJ, ID]),
  fi(),
  tok("الْإِنْجِيلِ", "injil", "propn", [HJ], "مَجْرُورٌ بِالْكَسْرَةِ.", "«the Gospel»", "«İncil»", punct=":"),
  *gospel_saying("(مَتَّى ٤:١٠)"),
])
sen("s2", "and his saying: «It is written: to the Lord your God you shall bow, and Him alone you shall serve» (Luke 4:8); and God Most High has said:",
        "ve şu sözü: «Yazılmıştır: Rabbin Allah'a secde edeceksin ve yalnız O'na kulluk edeceksin» (Luka 4:8); Allah Teâlâ da şöyle buyurmuştur:", [
  tok("وَقَوْلُهُ", "qawl", "noun", [AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَقَوْلُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ (مَعْطُوفٌ عَلَى مَا قَبْلَهُ عَلَى الْمَعْنَى)، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْخَبَرُ الْجُمْلَةُ الْمَحْكِيَّةُ.", "«and his saying» — the mubtadaʾ; the quoted sentence is its khabar.", "«ve sözü» — mübtedâ; haberi nakledilen cümle.", punct=":", segments=[seg("وَ", "wa", "conj"), seg("قَوْلُ", "qawl", "noun"), seg("هُ", "pron-3ms", "pron")]),
  *gospel_saying("(لُوقَا ٤:٨)"),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ عَاطِفَةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi("قَالَ", "qala", "«said»", "«buyurdu»", tags=["hollow-verbs"], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
])
sen("s3", "«It is not for a human being that God should give him the Book, the judgement and prophethood, and then he should say to the people: be servants to me instead of God; but rather: be devoted to the Lord, by your teaching the Book and by your studying.» (3:79)",
        "«Allah'ın kendisine kitabı, hükmü ve peygamberliği verdiği hiçbir insanın, sonra kalkıp insanlara: Allah'ı bırakıp bana kul olun, demesi olacak şey değildir; fakat: okuduğunuz ve öğrettiğiniz kitap gereğince Rabb'e adanmış kimseler olun [der].» (Âl-i İmrân 79)", [
  *quran([
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not»", "«değildir»"),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ الْمَصْدَرُ الْمُؤَوَّلُ الْمُؤَخَّرُ (أَنْ يُؤْتِيَهُ…).", "«it is» — kāna; its ism is the clause «that God should give him…».", "«olacak şey» — kâne; ismi sonraki masdar-ı müevvel."),
  li_noun("لِبَشَرٍ", "bashar", "«for a human being»", "«bir insan için»", tags=[KN], extra="، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ"),
  tok("أَنْ", "an-masdariyya", "part", [AN, KN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ (إِيتَاؤُهُ) فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ مُؤَخَّرٌ.", "«that» — the clause it heads is kāna's ism, placed last.", "«-mesi» — masdar-ı müevvel kâne'nin ismi."),
  tok("يُؤْتِيَهُ", "aata-bring", "verb", [AN, MB, "form-iv-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ، وَالْهَاءُ مَفْعُولٌ بِهِ أَوَّلُ.", "«should give him» — naṣb after an; the fatḥa shows on the yāʾ; «him» is the first object.", "«ona vermesi» — en ile mansûb; yâ üzerinde fetha; «ona» ilk mef'ûl.", segments=[seg("يُؤْتِيَ", "aata-bring", "verb"), seg("هُ", "pron-3ms", "pron")]),
  allah_fail(),
  maful_("الْكِتَابَ", "kitab", "«the Book»", "«kitabı»", ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  atf("وَالْحُكْمَ", "hukm", "«the judgement»", "«hükmü»", case="nasb"),
  atf("وَالنُّبُوَّةَ", "nubuwwa", "«prophethood»", "«peygamberliği»", case="nasb"),
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ وَالتَّرَاخِي.", "«then»", "«sonra»"),
  mansub("يَقُولَ", "qala", "«he should say»", "«demesi»", tags=[AT, "hollow-verbs"], hidden="هُوَ (الْبَشَرُ)", extra=" — مَعْطُوفٌ عَلَى يُؤْتِيَهُ"),
  li_noun("لِلنَّاسِ", "nas", "«to the people»", "«insanlara»", punct=":"),
  tok("كُونُوا", "kana", "verb", [AM, KN, "hollow-verbs"], "فِعْلُ أَمْرٍ نَاقِصٌ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ اسْمُهُ — مَقُولُ الْقَوْلِ.", "«be» — the imperative of kāna; the wāw is its ism.", "«olun» — kâne'nin emri; vâv ismi."),
  khabar_kana("عِبَادًا", "ibad", "«servants»", "«kullar»", ar="خَبَرُ كُونُوا مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ عَبْدٍ."),
  li_pron("لِي", "ي", "pron-1s", "«to me»", "«bana»"),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ — مِنْ دُونِ اللهِ: غَيْرَهُ، أَوْ مُجَاوِزِينَ اللهَ.", "«instead of [God]»", "«Allah'ı bırakıp»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»"),
  tok("وَلٰكِنْ", "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا يَعْمَلُ.", "«but rather» — the lightened lākin: no government.", "«fakat» — muhaffef lâkin; amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  tok("كُونُوا", "kana", "verb", [AM, KN, "hollow-verbs"], "فِعْلُ أَمْرٍ نَاقِصٌ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ اسْمُهُ — وَالْقَوْلُ مَحْذُوفٌ: وَلٰكِنْ يَقُولُ كُونُوا.", "«be» — a second imperative; its «he says» is unspoken.", "«olun» — ikinci emir; «der» hazfedilmiş."),
  tok("رَبَّانِيِّينَ", "rabbani", "noun", [KN, JS, "ism-mansub"], "خَبَرُ كُونُوا مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — مَنْسُوبٌ إِلَى الرَّبِّ بِزِيَادَةِ الْأَلِفِ وَالنُّونِ لِلْمُبَالَغَةِ.", "«devoted to the Lord» — a nisba with added alif-nūn.", "«Rabbânîler» — elif-nûn ziyadesiyle nisbet.", segments=None),
  bi_ma(extra=" — وَمَا مَوْصُولَةٌ (أَوْ مَصْدَرِيَّةٌ)، وَالْبَاءُ لِلسَّبَبِيَّةِ"),
  tok("كُنْتُمْ", "kana", "verb", [KN, MW, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهُ — صِلَةٌ.", "«you used to» — kāna with the doers' tāʾ; the ṣila.", "«idiniz» — kâne; tâ ismi; sıla.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  khamsa("تُعَلِّمُونَ", "allama", "«teach»", "«öğretiyor»", tags=[KN, "form-ii-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كُنْتُمْ"),
  maful_("الْكِتَابَ", "kitab", "«the Book»", "«kitabı»"),
  tok("وَبِمَا", "ma-mawsula", "pron", [AT, HJ, MW], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«and by what»", "«ve … ile»", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("كُنْتُمْ", "kana", "verb", [KN, MW, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ — صِلَةٌ.", "«you used to»", "«idiniz»", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  khamsa("تَدْرُسُونَ", "darasa", "«study»", "«okuyor»", tags=[KN], extra_ar=" — وَالْجُمْلَةُ خَبَرُ كُنْتُمْ", punct=AYA),
  ]),
])
sen("s4", "«Nor would he command you to take the angels and the prophets as lords. Would he command you to disbelieve after you have been Muslims?» (3:80)",
        "«Melekleri ve peygamberleri rabler edinmenizi de size emretmez. Siz müslüman olduktan sonra size küfrü mü emredecek?» (Âl-i İmrân 80)", [
  *quran([
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ — عَلَى قِرَاءَةِ النَّصْبِ (يَأْمُرَكُمْ) الْمَعْطُوفِ عَلَى يَقُولَ.", "«nor» — the negating lā; the verb after it is joined to «he should say».", "«ve … -mez» — nefiy lâ'sı.", segments=wa_("لَا", "la-nafiya", "part")),
  tok("يَأْمُرَكُمْ", "amara-order", "verb", [AN, AT, MB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْفَتْحَةِ (مَعْطُوفٌ عَلَى يَقُولَ)، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (الْبَشَرُ)، وَكُمْ مَفْعُولٌ بِهِ أَوَّلُ — وَقُرِئَ بِالرَّفْعِ عَلَى الِاسْتِئْنَافِ.", "«would he command you» — naṣb, joined to «he should say»; also read in rafʿ as a fresh start.", "«size emretmez» — nasb (yekûle'ye atıf); ref ile de okunmuştur.", segments=[seg("يَأْمُرَ", "amara-order", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  an_nasb("يَأْمُرَكُمْ الثَّانِي (أَوْ بِنَزْعِ الْخَافِضِ: بِأَنْ)", "«to»", "«-menizi»"),
  tok("تَتَّخِذُوا", "ittakhadha", "verb", [AN, AK, "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«take» — naṣb by the dropped nūn; the wāw is the doer.", "«edinmenizi» — nûn'un hazfiyle mansûb; vâv fâil."),
  maful_("الْمَلَائِكَةَ", "malak", "«the angels»", "«melekleri»", tags=[JT], ar="مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ."),
  tok("وَالنَّبِيِّينَ", "nabi", "noun", [AT, MB, JS], "الْوَاوُ عَاطِفَةٌ، وَالنَّبِيِّينَ مَعْطُوفٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the prophets» — a sound plural; naṣb by the yāʾ.", "«ve peygamberleri» — cem-i müzekker sâlim; yâ ile nasb.", segments=wa_("النَّبِيِّينَ", "nabi", "noun")),
  maful_("أَرْبَابًا", "rabb", "«as lords»", "«rabler»", tags=[JT], ar="مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ رَبٍّ."),
  tok("أَيَأْمُرُكُمْ", "amara-order", "verb", [IS, MB, "mudari-marfu"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَيَأْمُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَكُمْ مَفْعُولٌ بِهِ.", "«would he command you?» — the hamza of denial; rafʿ.", "«size … mi emreder?» — inkârî istifham hemzesi; merfû.", segments=[seg("أَ", "hamza-istifham", "part"), seg("يَأْمُرُ", "amara-order", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  bi_noun("بِالْكُفْرِ", "kufr", "«to disbelieve»", "«küfrü»"),
  tok("بَعْدَ", "bada", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«after» — a ẓarf, annexed.", "«sonra» — zarf, muzâf."),
  tok("إِذْ", "idh", "noun", [ID], "ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when» — a frozen ẓarf, annexed to the sentence after it.", "«-dığı zaman» — mebnî zarf, cümleye muzâf."),
  tok("أَنْتُمْ", "antum", "pron", [MK], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«you» — the mubtadaʾ.", "«siz» — mübtedâ."),
  tok("مُسْلِمُونَ", "muslim", "noun", [MK, JS, "form-iv-verbs"], "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ.", "«Muslims» — the khabar; a sound plural in rafʿ by the wāw.", "«müslümanlar» — haber; vâv ile merfû.", punct="."),
  ]),
])
# ---------------------------------------------------------------- §39 الْقُرْآنُ يُصَرِّحُ بِدَعْوَةِ عِيسَى (print p. 65)
sen("s5", "And the Qurʾān — the Book that confirms what came before it and watches over it — has transmitted of our master ʿĪsā's proclamation of pure tawḥīd and of the call to it, in a style plain and clear beyond which nothing can be added:",
        "Kur'ân — kendinden öncekini tasdik eden ve onu gözeten kitap — efendimiz Îsâ'nın hâlis tevhidi ilânından ve ona davetinden, daha ötesi olmayan açık ve net bir üslûpla şunu nakletmiştir:", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi("نَقَلَ", "naqala", "«has transmitted»", "«nakletmiştir»", hidden=None),
  fail("الْقُرْآنُ", "quran", "«the Qurʾān»", "«Kur'ân»", punct=" —"),
  tok("وَهُوَ", "huwa", "pron", [AT, MK, JM], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ مُعْتَرِضَةٌ بَيْنَ الْفِعْلِ وَمُتَعَلِّقِهِ.", "«and it is» — a parenthesis between the verb and its complement.", "«ki o» — fiil ile müteallakı arasında mu'terıza.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("الْكِتَابُ", "kitab", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Book» — the khabar.", "«kitap» — haber."),
  naat("الْمُصَدِّقُ", "musaddiq", "«confirming»", "«tasdik eden»", case="raf", tags=["ism-fail", "form-ii-verbs"]),
  tok("لِمَا", "ma-mawsula", "pron", [HJ, MW], "اللَّامُ حَرْفُ جَرٍّ (لِتَقْوِيَةِ الْعَامِلِ)، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِالْمُصَدِّقِ.", "«what» — the lām strengthens the participle's government.", "«-ini» — lâm âmili takviye için.", segments=[seg("لِ", "li", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("بَيْنَ", "bayna", "noun", [MF, ID, MW], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةُ الْمَوْصُولِ.", "«between» — a ẓarf; the ṣila's unspoken verb.", "«arasında» — zarf; sılanın hazfedilmiş müteallakı."),
  noun_pron("يَدَيْهِ", "yad", "يَدَيْ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — بَيْنَ يَدَيْهِ: قَبْلَهُ (كِنَايَةٌ).", "«its hands» — a dual in jarr; «between its hands» = before it.", "«iki eli» — tesniye, yâ ile mecrûr; «önünde» = kendinden önce.", tags=[ID, "al-muthanna"]),
  naat("وَالْمُهَيْمِنُ", "muhaymin", "«and watching over»", "«ve gözeten»", case="raf", wa=True, tags=["ism-fail"]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«over it»", "«onu»", punct=" —", extra_ar=" — مُتَعَلِّقٌ بِالْمُهَيْمِنِ"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلتَّبْعِيضِ — مُتَعَلِّقٌ بِنَقَلَ."),
  majrur("إِعْلَانِ", "ilan", "«the proclamation [of]»", "«ilânından»", tags=[ID, "form-iv-verbs"], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — مَصْدَرُ أَعْلَنَ."),
  noun_pron("سَيِّدِنَا", "sayyid", "سَيِّدِ", "نَا", "pron-1p", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master»", "«efendimiz»", tags=[ID]),
  tok("عِيسَى", "isa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ (وَقِيلَ بِفَتْحَةٍ مُقَدَّرَةٍ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ).", "«ʿĪsā» — the muḍāf ilayh; the ending is hidden on the alif.", "«Îsâ» — muzâfun ileyh; alâmet elif üzerinde takdirî."),
  bi_noun("بِالتَّوْحِيدِ", "tawhid", "«of tawḥīd»", "«tevhidi»", tags=["form-ii-verbs"], extra=" — مُتَعَلِّقٌ بِإِعْلَانِ"),
  naat("الْخَالِصِ", "khalis", "«pure»", "«hâlis»"),
  atf("وَالدَّعْوَةِ", "dawa", "«the call»", "«daveti»"),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to it»", "«ona»", punct="،"),
  fi(),
  majrur("أُسْلُوبٍ", "uslub", "«a style»", "«bir üslûpla»"),
  naat("صَرِيحٍ", "sarih", "«plain»", "«açık»"),
  naat2("وَاضِحٍ", "wadih", "«clear»", "«net»", case="jarr"),
  la_jins("لَا"),
  ism_la("مَزِيدَ", "mazid", "«no addition»", "«daha ötesi yok»", khabar="كَائِنٌ", tags=["jumla-sifa"]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon it»", "«ona»", punct=":", extra_ar=" — مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ؛ وَجُمْلَةُ لَا مَزِيدَ عَلَيْهِ نَعْتٌ ثَالِثٌ لِأُسْلُوبٍ"),
])
sen("s6", "«They have disbelieved who say: God is the Messiah son of Maryam. And the Messiah said: O Children of Israel, worship God, my Lord and your Lord. Whoever associates partners with God, God has forbidden him the Garden, and his abode is the Fire; and the wrongdoers have no helpers.» (5:72)",
        "«Allah, Meryem oğlu Mesîh'tir, diyenler andolsun ki kâfir olmuşlardır. Oysa Mesîh: Ey İsrâiloğulları, benim de Rabbim, sizin de Rabbiniz olan Allah'a kulluk edin, demişti. Kim Allah'a ortak koşarsa Allah ona cenneti haram kılmıştır; onun varacağı yer ateştir. Zalimlerin hiçbir yardımcısı yoktur.» (Mâide 72)", [
  *quran([
  tok("لَقَدْ", "qad", "part", ["qad-harf", TA], "اللَّامُ لَامُ الِابْتِدَاءِ (أَوْ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ)، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«certainly» — the lām of emphasis (or of a hidden oath) with qad.", "«andolsun ki» — te'kid lâmı (yahut mukadder kasemin cevabı) ve kad.", segments=[seg("لَ", "lam-ibtida", "part"), seg("قَدْ", "qad", "part")]),
  mazi("كَفَرَ", "kafara", "«have disbelieved»", "«kâfir oldular»", hidden=None),
  alladhina("raf", "فَاعِلٌ", "«those who» — the doer.", "«-enler» — fâil."),
  mazi_pl("قَالُوا", "qala", "«say»", "«diyenler»", tags=[MW, "hollow-verbs"], punct=":"),
  inna(),
  tok("اللهَ", "allah", "propn", [IW], "لَفْظُ الْجَلَالَةِ اسْمُ إِنَّ مَنْصُوبٌ.", "«God» — inna's ism.", "«Allah» — inne'nin ismi."),
  tok("هُوَ", "huwa", "pron", [IW, "tawkid"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ مُبْتَدَأٌ، وَالْمَسِيحُ خَبَرُهُ، وَالْجُمْلَةُ خَبَرُ إِنَّ).", "«He [is]» — the pronoun of separation.", "«O» — fasıl zamiri."),
  tok("الْمَسِيحُ", "masih", "propn", [IW], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — inna's khabar.", "«Mesîh» — inne'nin haberi."),
  tok("ابْنُ", "ibn", "noun", [NA, ID], "نَعْتٌ لِلْمَسِيحِ (أَوْ بَدَلٌ) مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«son [of]» — a naʿt (or badal), annexed.", "«oğlu» — sıfat (yahut bedel), muzâf."),
  tok("مَرْيَمَ", "maryam", "propn", [ID, "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (عَلَمٌ مُؤَنَّثٌ أَعْجَمِيٌّ).", "«Maryam» — a diptote: fatḥa stands for the kasra.", "«Meryem» — gayr-i munsarıf: kesre yerine fetha."),
  mazi("وَقَالَ", "qala", "«and said»", "«ve dedi»", tags=[AT, "hollow-verbs"], hidden=None, wa=True),
  tok("الْمَسِيحُ", "masih", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — the doer.", "«Mesîh» — fâil.", punct=":"),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("بَنِي", "banu-israil", "noun", ["vocative-munada", ID, JS], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ.", "«Children [of]» — the annexed munādā; naṣb by the yāʾ.", "«oğulları» — muzâf münâdâ; yâ ile mansûb."),
  tok("إِسْرَائِيلَ", "israil", "propn", [ID, "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.", "«Israel» — a diptote.", "«İsrâil» — gayr-i munsarıf.", punct="،"),
  tok("اعْبُدُوا", "abada", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — هَمْزَتُهُ هَمْزَةُ وَصْلٍ تُضَمُّ لِضَمِّ عَيْنِ الْمُضَارِعِ.", "«worship» — an imperative; its hamza is a joining hamza with ḍamma.", "«kulluk edin» — emir; vasıl hemzesi ötreli."),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'a» — mef'ûl."),
  tok("رَبِّي", "rabb", "noun", [BD, ID, "ya-al-mutakallim"], "بَدَلٌ مِنْ لَفْظِ الْجَلَالَةِ (أَوْ نَعْتٌ) مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — in apposition; the fatḥa is hidden before the speaker's yāʾ.", "«Rabbim» — bedel; mütekellim yâ'sından önce fetha takdirî.", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
  pron_atf("وَرَبَّكُمْ", "rabb", "رَبَّ", "كُمْ", "pron-2mp", "«and your Lord»", "«ve Rabbiniz»", case="nasb", punct="."),
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ اسْمُهَا، وَالْجُمْلَةُ الشَّرْطِيَّةُ بَعْدَهَا خَبَرُهَا.", "«indeed» — the pronoun of the matter is its ism; the conditional sentence its khabar.", "«şüphesiz» — şe'n zamiri ismi; şart cümlesi haberi.", segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("مَنْ", "man-shartiyya", "pron", [SH, MK], "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«whoever» — the conditional noun, the mubtadaʾ.", "«kim» — şart ismi, mübtedâ."),
  tok("يُشْرِكْ", "ashraka", "verb", [SH, "form-iv-verbs"], "فِعْلُ الشَّرْطِ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«associates partners» — the condition's verb, jussive.", "«ortak koşarsa» — şart fiili, meczûm."),
  tok("بِاللهِ", "allah", "propn", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«with God»", "«Allah'a»", segments=[seg("بِ", "bi", "prep"), seg("اللهِ", "allah", "propn")]),
  tok("فَقَدْ", "qad", "part", [SH, "qad-harf"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«then [indeed]» — the fāʾ binding the answer.", "«artık» — cevap fâ'sı ve kad.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi("حَرَّمَ", "harrama", "«has forbidden»", "«haram kılmıştır»", tags=[SH, "form-ii-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ"),
  allah_fail(),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«to him»", "«ona»"),
  maful_("الْجَنَّةَ", "janna", "«the Garden»", "«cenneti»"),
  tok("وَمَأْوَاهُ", "mawa", "noun", [AT, MK, ID, "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَمَأْوَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ مَكَانٍ مِنْ أَوَى.", "«and his abode» — a maqṣūr noun of place; the mubtadaʾ.", "«ve varacağı yer» — maksûr ism-i mekân; mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("مَأْوَا", "mawa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("النَّارُ", "nar", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Fire» — the khabar.", "«ateştir» — haber."),
  tok("وَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَمَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«and … not»", "«ve … yoktur»", segments=wa_("مَا", "ma-nafiya", "part")),
  tok("لِلظَّالِمِينَ", "zalim", "noun", [HJ, MK, JS], "اللَّامُ حَرْفُ جَرٍّ، وَالظَّالِمِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — خَبَرٌ مُقَدَّمٌ.", "«for the wrongdoers» — the fronted khabar.", "«zalimler için» — öne alınmış haber.", segments=[seg("لِ", "li", "prep"), seg("لظَّالِمِينَ", "zalim", "noun")]),
  prep("مِنْ", "min", "«[any]»", "«hiçbir»", ar="حَرْفُ جَرٍّ زَائِدٌ لِتَأْكِيدِ النَّفْيِ."),
  tok("أَنْصَارٍ", "nasir", "noun", [MK, JT], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ — جَمْعُ نَصِيرٍ.", "«helpers» — the delayed mubtadaʾ, jarr in form by the redundant min.", "«yardımcılar» — sonraya bırakılmış mübtedâ; zâid min ile lafzen mecrûr.", punct="."),
  ]),
])

CAND = {
 "maktub": G("maktub", "مَكْتُوب", "ك ت ب", "noun", "written (a passive participle)", "yazılmış, yazılı (ism-i mef'ûl)", 1),
 "darasa": G("darasa", "دَرَسَ", "د ر س", "verb", "to study, to read closely", "okumak, ders almak", 1),
 "naqala": G("naqala", "نَقَلَ", "ن ق ل", "verb", "to transmit, to carry over", "nakletmek, aktarmak", 1),
 "muhaymin": G("muhaymin", "مُهَيْمِن", "ه ي م ن", "noun", "watching over, guardian (the Qurʾān over the earlier books)", "gözeten, koruyucu (Müheymin)", 2),
 "ilan": G("ilan", "إِعْلَان", "ع ل ن", "noun", "a proclamation, declaring openly (the maṣdar of Form IV)", "ilân, açıkça bildirme (if'âl masdarı)", 2),
 "wadih": G("wadih", "وَاضِح", "و ض ح", "noun", "clear, plain", "açık, vâzıh", 1),
 "janna": G("janna", "جَنَّة", "ج ن ن", "noun", "the Garden, Paradise", "cennet", 1, plural="جَنَّات"),
 "mawa": G("mawa", "مَأْوًى", "أ و ي", "noun", "an abode, a refuge (a noun of place)", "barınak, varılacak yer (me'vâ)", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "me / my", "beni / benim", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masc. sing.)", "seni / senin", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (masc. plur.)", "sizi / sizin", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "him / his / it", "onu / onun", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "darasa", _sg.sound1("nasara", "دَرَس", "دْرُس", "اُدْرُس", "دَرْس / دِرَاسَة", "دَارِس", "مَدْرُوس", "دُرِسَ", "يُدْرَسُ", "دَرَسَ الْكِتَابَ يَدْرُسُهُ: قَرَأَهُ وَتَعَلَّمَهُ؛ وَدَرَسَ الرَّسْمُ: عَفَا وَانْمَحَى."))
put_morph(mo, "naqala", _sg.sound1("nasara", "نَقَل", "نْقُل", "اُنْقُل", "نَقْل", "نَاقِل", "مَنْقُول", "نُقِلَ", "يُنْقَلُ", "نَقَلَ الشَّيْءَ يَنْقُلُهُ: حَوَّلَهُ مِنْ مَوْضِعٍ إِلَى مَوْضِعٍ؛ وَنَقَلَ الْخَبَرَ: رَوَاهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch43 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 43 (print pp. 64–65; ʿĪsā §38–39): his call to the worship of God alone — the Gospel's «to the Lord your God you shall bow» twice, Matthew 4:10 and Luke 4:8 (s1–s2), then Āl ʿImrān 3:79–80: no human given the Book may say «be servants to me», nor command the angels and the prophets be taken as lords (s3–s4); the Qurʾān, confirming and guarding the earlier books, transmits his proclamation outright (s5) — al-Māʾida 5:72, «worship God, my Lord and your Lord; whoever associates partners with God, God has forbidden him the Garden» (s6)."
ADD_TR = " Kırk üçüncü bölüm (baskı s. 64–65; Îsâ §38–39): yalnız Allah'a kulluğa daveti — İncil'in «Rabbin Allah'a secde edeceksin» sözü iki kez, Matta 4:10 ve Luka 4:8 (s1–s2), ardından Âl-i İmrân 79–80: kitap verilen hiçbir insan «bana kul olun» diyemez, melekleri ve peygamberleri rab edinmeyi de emretmez (s3–s4); öncekileri tasdik eden ve gözeten Kur'ân onun ilânını açıkça nakleder (s5) — Mâide 72, «benim de Rabbim, sizin de Rabbiniz olan Allah'a kulluk edin; kim Allah'a ortak koşarsa Allah ona cenneti haram kılmıştır» (s6)."
write_out(43, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §38–39 + 3:79–80, 5:72", GLOSS_ADD, notes=(), related=())
report(43, S, GLOSS_ADD, ())
