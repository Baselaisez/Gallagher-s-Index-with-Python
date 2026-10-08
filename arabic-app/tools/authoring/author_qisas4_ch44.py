# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 44: «قِصَّةُ عِيسَى» §40 (the rank of tawḥīd in his call — al-Nisāʾ 4:172–173) and §41 (a splendid scene of the Resurrection — al-Māʾida 5:116–120). Print pp. 65–68.
python3 tools/authoring/author_qisas4_ch44.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: مَنْزِلَةُ التَّوْحِيدِ فِي دَعْوَتِهِ، وَمَشْهَدٌ رَائِعٌ مِنْ مَشَاهِدِ الْقِيَامَةِ (النساء ١٧٢–١٧٣، المائدة ١١٦–١٢٠)", "en": "The story of ʿĪsā: the rank of tawḥīd in his call, and a splendid scene of the Resurrection (4:172–173, 5:116–120)", "tr": "Îsâ kıssası: davetinde tevhidin yeri ve kıyamet sahnelerinden muhteşem bir sahne (Nisâ 172–173, Mâide 116–120)"}
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

# ---------------------------------------------------------------- §40 مَنْزِلَةُ التَّوْحِيدِ فِي دَعْوَتِهِ (print pp. 65–66)
def fa_qad_shart(): return tok("فَقَدْ", "qad", "part", [SH, "qad-harf"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«then [indeed]» — the fāʾ binding the answer.", "«artık» — cevap fâ'sı ve kad.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")])
def worship_tokens():
    return [tok("اعْبُدُوا", "abada", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — هَمْزَتُهُ هَمْزَةُ وَصْلٍ تُضَمُّ لِضَمِّ عَيْنِ الْمُضَارِعِ.", "«worship» — an imperative; its hamza is a joining hamza with ḍamma.", "«kulluk edin» — emir; vasıl hemzesi ötreli."),
            tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God» — the object.", "«Allah'a» — mef'ûl."),
            tok("رَبِّي", "rabb", "noun", [BD, ID, "ya-al-mutakallim"], "بَدَلٌ مِنْ لَفْظِ الْجَلَالَةِ (أَوْ نَعْتٌ) مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Lord» — in apposition; the fatḥa is hidden before the speaker's yāʾ.", "«Rabbim» — bedel; mütekellim yâ'sından önce fetha takdirî.", segments=[seg("رَبِّ", "rabb", "noun"), seg("ي", "pron-1s", "pron")]),
            pron_atf("وَرَبَّكُمْ", "rabb", "رَبَّ", "كُمْ", "pron-2mp", "«and your Lord»", "«ve Rabbiniz»", case="nasb")]
def tu_mazi(full, lex, stem, en, tr, ar, tags=(), punct=None, obj=None, obj_lex=None, person="تُ", person_lex="pron-1s"):
    segs = ([seg(full[:2], "wa" if full[:2] == "وَ" else "fa", "conj")] if full[:2] in ("وَ", "فَ") else []) + [seg(stem, lex, "verb"), seg(person, person_lex, "pron")] + ([seg(obj, obj_lex, "pron")] if obj else [])
    return tok(full, lex, "verb", list(tags), ar, en, tr, punct=punct, segments=segs)
sen("s1", "And he spoke, in a beautiful and eloquent style savoured by everyone who knows the rank of tawḥīd and the way of the prophets and messengers, and what they were moulded upon of knowing God Most High, of submission to Him and of awe of Him:",
        "Tevhidin yerini, peygamberlerin ve resullerin sîretini, Allah Teâlâ'yı tanımak, O'na boyun eğmek ve O'ndan korkmak üzere nasıl yoğrulduklarını bilen herkesin tadına vardığı güzel ve beliğ bir üslûpla şöyle dedi:", [
  mazi("وَقَالَ", "qala", "«and he said»", "«ve dedi»", tags=[AT, "hollow-verbs"], hidden="هُوَ (عِيسَى)", wa=True, extra_ar="، وَالْمَقُولُ الْآيَةُ بَعْدَهُ"),
  fi(),
  majrur("أُسْلُوبٍ", "uslub", "«a style»", "«bir üslûpla»"),
  naat("جَمِيلٍ", "jamil", "«beautiful»", "«güzel»"),
  naat2("بَلِيغٍ", "baligh", "«eloquent»", "«beliğ»", case="jarr"),
  tok("يَتَذَوَّقُهُ", "tadhawwaqa", "verb", ["jumla-sifa", MB, "form-v-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَالِثٌ لِأُسْلُوبٍ.", "«savoured by» — a third naʿt as a sentence; «it» is its object.", "«tadına vardığı» — cümle hâlinde üçüncü sıfat; «onu» mef'ûl.", segments=[seg("يَتَذَوَّقُ", "tadhawwaqa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("كُلُّ", "kull", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«everyone» — the doer, annexed.", "«herkes» — fâil, muzâf."),
  tok("مَنْ", "man-mawsula", "pron", [ID, MW], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«who» — the relative, annexed to.", "«-en kimse» — ism-i mevsûl, muzâfun ileyh."),
  mazi("عَرَفَ", "arafa", "«knows»", "«bilen»", tags=[MW], hidden="هُوَ", extra_ar=" — صِلَةُ الْمَوْصُولِ"),
  maful_("مَنْزِلَةَ", "manzila", "«the rank [of]»", "«yerini»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("التَّوْحِيدِ", "tawhid", "«tawḥīd»", "«tevhidin»", tags=["form-ii-verbs"]),
  atf("وَسِيرَةَ", "sira", "«the way [of]»", "«sîretini»", case="nasb", tags=[ID]),
  mudaf_ilayh("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberlerin»", tags=[JT, "mamnu-min-sarf"]),
  tok("وَالْمُرْسَلِينَ", "mursal", "noun", [AT, ID, JS, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَالْمُرْسَلِينَ مَعْطُوفٌ عَلَى الْأَنْبِيَاءِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«and the messengers» — joined; jarr by the yāʾ.", "«ve resullerin» — atıf; yâ ile mecrûr.", punct="،", segments=wa_("الْمُرْسَلِينَ", "mursal", "noun")),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW, MB], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى مَنْزِلَةَ.", "«and what» — joined to «the rank».", "«ve … şeyi» — «yerini»ne atıf.", segments=wa_("مَا", "ma-mawsula", "pron")),
  tok("طُبِعُوا", "tabaa", "verb", [MW, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — صِلَةٌ؛ طُبِعَ عَلَى الشَّيْءِ: جُبِلَ عَلَيْهِ.", "«they were moulded» — a passive; the wāw is the deputy doer; the ṣila.", "«yoğruldular» — meçhul; vâv nâib-i fâil; sıla."),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«upon [it]»", "«üzerine»"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  majrur("مَعْرِفَةِ", "marifa", "«knowing»", "«tanımaktan»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ı»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct="،"),
  atf("وَالْخُضُوعِ", "khudu", "«submission»", "«boyun eğmekten»"),
  li_pron("لَهُ", "هُ", "pron-3ms", "«to Him»", "«O'na»", punct="،"),
  atf("وَالرَّهْبَةِ", "rahba", "«awe»", "«korkmaktan»"),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of Him»", "«O'ndan»", punct=":"),
])
sen("s2", "«The Messiah will never disdain to be a servant of God, nor will the angels brought near. And whoever disdains His worship and is proud — He will gather them to Himself all together.» (4:172)",
        "«Mesîh, Allah'a kul olmaktan asla çekinmez; Allah'a yakın melekler de. Kim O'na kulluktan çekinir ve büyüklenirse, Allah onların hepsini huzurunda toplayacaktır.» (Nisâ 172)", [
  *quran([
  tok("لَنْ", "lan", "part", [], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "«never» — negation of the future, with naṣb.", "«asla» — gelecek için nefiy ve nasb harfi."),
  tok("يَسْتَنْكِفَ", "istankafa", "verb", ["form-x-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — اِسْتَنْكَفَ: أَنِفَ وَامْتَنَعَ تَرَفُّعًا.", "«will disdain» — naṣb after lan; Form X: to hold oneself above.", "«çekinmez» — len ile mansûb; istif'âl: kendini üstün görüp kaçınmak."),
  tok("الْمَسِيحُ", "masih", "propn", [FL], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Messiah» — the doer.", "«Mesîh» — fâil."),
  an_nasb("يَسْتَنْكِفَ (عَلَى نَزْعِ الْخَافِضِ: عَنْ أَنْ يَكُونَ)", "«to»", "«-maktan»"),
  tok("يَكُونَ", "kana", "verb", [AN, KN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«be» — kāna in naṣb; its ism is concealed.", "«olmak» — mansûb kâne; ismi gizli."),
  khabar_kana("عَبْدًا", "abd", "«a servant»", "«kul»"),
  tok("لِلّٰهِ", "allah", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — مُتَعَلِّقٌ بِعَبْدًا.", "«to God»", "«Allah'a»", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  la_nafiya("وَلَا", wa=True),
  tok("الْمَلَائِكَةُ", "malak", "noun", [AT, FL, JT], "مَعْطُوفٌ عَلَى الْمَسِيحُ مَرْفُوعٌ بِالضَّمَّةِ.", "«the angels» — joined to «the Messiah».", "«melekler» — «Mesîh»e atıf."),
  tok("الْمُقَرَّبُونَ", "muqarrab", "noun", [NA, JS, "form-ii-verbs"], "نَعْتٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«brought near» — a naʿt; rafʿ by the wāw.", "«yakın kılınmış» — sıfat; vâv ile merfû."),
  tok("وَمَنْ", "man-shartiyya", "pron", [AT, SH, MK], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and whoever» — the conditional noun, the mubtadaʾ.", "«ve kim» — şart ismi, mübtedâ.", segments=wa_("مَنْ", "man-shartiyya", "pron")),
  tok("يَسْتَنْكِفْ", "istankafa", "verb", [SH, "form-x-verbs"], "فِعْلُ الشَّرْطِ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«disdains» — the condition's verb, jussive.", "«çekinirse» — şart fiili, meczûm."),
  prep("عَنْ", "an", "«from»", "«-dan»"),
  noun_pron("عِبَادَتِهِ", "ibada", "عِبَادَتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His worship»", "«O'na kulluktan»", tags=[HJ, ID]),
  tok("وَيَسْتَكْبِرْ", "istakbara", "verb", [AT, SH, "form-x-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَسْتَكْبِرْ مَعْطُوفٌ عَلَى فِعْلِ الشَّرْطِ مَجْزُومٌ بِالسُّكُونِ.", "«and is proud» — joined to the condition's verb, jussive.", "«ve büyüklenirse» — şart fiiline atıf, meczûm.", segments=wa_("يَسْتَكْبِرْ", "istakbara", "verb")),
  tok("فَسَيَحْشُرُهُمْ", "hashara", "verb", [SH, MB, "mudari-marfu"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَالسِّينُ لِلِاسْتِقْبَالِ، وَيَحْشُرُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ (اللهُ)، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«then He will gather them» — the fāʾ of the answer, the sīn of the future; «them» is the object.", "«onları toplayacaktır» — cevap fâ'sı, istikbal sîn'i; «onları» mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("سَ", "sa", "part"), seg("يَحْشُرُ", "hashara", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Himself»", "«huzuruna»"),
  hal("جَمِيعًا", "jami", "«all together»", "«hepsini»", punct=AYA),
  ]),
])
sen("s3", "«As for those who believed and did righteous deeds, He will pay them their rewards in full and give them more of His bounty; and as for those who disdained and were proud, He will punish them with a painful punishment, and they will find for themselves, besides God, no protector and no helper.» (4:173)",
        "«İman edip sâlih ameller işleyenlere gelince, Allah onların mükâfatlarını eksiksiz verecek ve lütfundan daha fazlasını da verecektir. Çekinip büyüklenenlere gelince, onları acı bir azapla cezalandıracak; onlar Allah'tan başka kendilerine ne bir dost ne de bir yardımcı bulacaklardır.» (Nisâ 173)", [
  *quran([
  tok("فَأَمَّا", "amma", "part", [AT, "amma-tafsiliyya", SH], "الْفَاءُ اسْتِئْنَافِيَّةٌ (لِلتَّفْصِيلِ)، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ.", "«as for» — the particle of detailing.", "«-e gelince» — tafsil harfi.", segments=[seg("فَ", "fa", "conj"), seg("أَمَّا", "amma", "part")]),
  alladhina("raf", "مُبْتَدَأٌ", "«those who» — the mubtadaʾ.", "«-enler» — mübtedâ."),
  mazi_pl("آمَنُوا", "aamana", "«believed»", "«iman ettiler»", tags=[MW, "form-iv-verbs"]),
  mazi_pl("وَعَمِلُوا", "amila", "«and did»", "«ve işlediler»", tags=[AT, MW], wa=True),
  tok("الصَّالِحَاتِ", "salih", "noun", [MB, "ism-fail"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«righteous deeds» — the object; a sound feminine plural takes kasra for the fatḥa.", "«sâlih amelleri» — mef'ûl; cem-i müennes sâlimde fetha yerine kesre."),
  tok("فَيُوَفِّيهِمْ", "waffa", "verb", [SH, MB, "form-ii-verbs", "naqis-verbs", "mudari-marfu"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا (وَاقِعَةٌ فِي الْخَبَرِ)، وَيُوَفِّي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهِمْ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«He will pay them in full» — the fāʾ of ammā's answer; the ḍamma is hidden on the yāʾ.", "«onlara tastamam verir» — emmâ'nın cevap fâ'sı; zamme yâ üzerinde takdirî.", segments=[seg("فَ", "fa", "conj"), seg("يُوَفِّي", "waffa", "verb"), seg("هِمْ", "pron-3mp", "pron")]),
  noun_pron("أُجُورَهُمْ", "ajr", "أُجُورَ", "هُمْ", "pron-3mp", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — جَمْعُ أَجْرٍ.", "«their rewards» — the second object.", "«mükâfatlarını» — ikinci mef'ûl.", tags=[MB, ID, JT]),
  tok("وَيَزِيدُهُمْ", "zada", "verb", [AT, MB, "hollow-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَزِيدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«and give them more» — joined; «them» the object.", "«ve onlara artırır» — atıf; «onlara» mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("يَزِيدُ", "zada", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("مِنْ", "min", "«of»", "«-ndan»", ar="حَرْفُ جَرٍّ لِلتَّبْعِيضِ."),
  noun_pron("فَضْلِهِ", "fadl", "فَضْلِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His bounty»", "«lütfundan»", tags=[HJ, ID]),
  tok("وَأَمَّا", "amma", "part", [AT, "amma-tafsiliyya", SH], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«-e gelince de»", segments=wa_("أَمَّا", "amma", "part")),
  alladhina("raf", "مُبْتَدَأٌ", "«those who» — the mubtadaʾ.", "«-enler» — mübtedâ."),
  mazi_pl("اسْتَنْكَفُوا", "istankafa", "«disdained»", "«çekindiler»", tags=[MW, "form-x-verbs"]),
  mazi_pl("وَاسْتَكْبَرُوا", "istakbara", "«and were proud»", "«ve büyüklendiler»", tags=[AT, MW, "form-x-verbs"], wa=True),
  tok("فَيُعَذِّبُهُمْ", "adhdhaba", "verb", [SH, MB, "form-ii-verbs", "mudari-marfu"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ أَمَّا، وَيُعَذِّبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«He will punish them» — the answer's fāʾ; «them» the object.", "«onları cezalandırır» — cevap fâ'sı; «onları» mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("يُعَذِّبُ", "adhdhaba", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("عَذَابًا", "adhab", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ مَصْدَرٍ نَابَ عَنِ الْمَصْدَرِ (تَعْذِيبًا).", "«with a punishment» — an absolute object; the noun of the maṣdar stands for it.", "«bir azapla» — mef'ûl-i mutlak; masdar yerine ism-i masdar."),
  naat("أَلِيمًا", "alim-painful", "«painful»", "«acı»", case="nasb", tags=["sighat-mubalagha"]),
  la_nafiya("وَلَا", wa=True),
  khamsa("يَجِدُونَ", "wajada", "«they will find»", "«bulurlar»", tags=["mithal-verbs"], extra_ar=" — فُتِحَتْ عَيْنُ الْمُضَارِعِ وَحُذِفَتْ فَاؤُهُ الْوَاوُ لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ (يَوْجِدُ → يَجِدُ)"),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«for themselves»", "«kendilerine»"),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«besides [God]»", "«… başka»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'tan»"),
  maful_("وَلِيًّا", "wali", "«any protector»", "«bir dost»"),
  la_nafiya("وَلَا", wa=True),
  tok("نَصِيرًا", "nasir", "noun", [AT, MB], "مَعْطُوفٌ عَلَى وَلِيًّا مَنْصُوبٌ بِالْفَتْحَةِ.", "«nor helper» — joined to «protector».", "«ne de bir yardımcı» — «dost»a atıf.", punct="."),
  ]),
])
# ---------------------------------------------------------------- §41 مَشْهَدٌ رَائِعٌ مِنْ مَشَاهِدِ الْقِيَامَةِ (print pp. 66–68)
sen("s4", "And the Qurʾān, in its eloquence and inimitability, has painted one of the splendid scenes of the Resurrection, in which our master ʿĪsā disowns what people fabricated about him and the way they treated him, makes his call plain with strength and truthfulness, and in this matter condemns the extremists of his community — that they alone are answerable for this crime;",
        "Kur'ân, belâgati ve i'câzıyla, kıyametin muhteşem sahnelerinden birini tasvir etmiştir: Efendimiz Îsâ o sahnede insanların kendisi hakkında uydurduklarından ve ona yaptıklarından uzak olduğunu bildirir, davetini güç ve doğrulukla açıklar, bu meselede ümmetinin aşırıya gidenlerini kınar ve bu suçtan yalnızca onların sorumlu olduğunu söyler;", [
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi("صَوَّرَ", "sawwara", "«has painted»", "«tasvir etmiştir»", tags=["form-ii-verbs"], hidden=None),
  fail("الْقُرْآنُ", "quran", "«the Qurʾān»", "«Kur'ân»"),
  fi(),
  noun_pron("بَلَاغَتِهِ", "balagha-eloquence", "بَلَاغَتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its eloquence»", "«belâgatiyle»", tags=[HJ, ID]),
  pron_atf("وَإِعْجَازِهِ", "ijaz-inimitability", "إِعْجَازِ", "هِ", "pron-3ms", "«and its inimitability»", "«ve i'câzıyla»", case="jarr", punct="،", tags=["form-iv-verbs"]),
  maful_("مَشْهَدًا", "mashhad", "«a scene»", "«bir sahne»"),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلتَّبْعِيضِ."),
  majrur("مَشَاهِدِ", "mashhad", "«the scenes [of]»", "«sahnelerinden»", tags=[ID, JT, "mamnu-min-sarf"], ar="مَجْرُورٌ بِالْكَسْرَةِ لِإِضَافَتِهِ (وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ: صِيغَةُ مُنْتَهَى الْجُمُوعِ)، مُضَافٌ."),
  mudaf_ilayh("الْقِيَامَةِ", "qiyama", "«the Resurrection»", "«kıyametin»"),
  naat("الرَّائِعَةِ", "rai", "«splendid»", "«muhteşem»", punct="،"),
  tok("يَتَبَرَّأُ", "tabarraa", "verb", ["jumla-sifa", "form-v-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِمَشْهَدًا؛ تَبَرَّأَ مِنْهُ: تَنَزَّهَ عَنْهُ.", "«disowns» — a sentence serving as the naʿt of «a scene».", "«uzak olduğunu bildirir» — «bir sahne»nin sıfatı olan cümle."),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«in which»", "«o sahnede»"),
  noun_pron("سَيِّدُنَا", "sayyid", "سَيِّدُ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master» — the doer.", "«efendimiz» — fâil.", tags=[FL, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "عَطْفُ بَيَانٍ (أَوْ بَدَلٌ) مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — in apposition to «our master».", "«Îsâ» — atf-ı beyan."),
  tok("عَمَّا", "ma-mawsula", "pron", [HJ, MW], "عَنْ حَرْفُ جَرٍّ أُدْغِمَتْ نُونُهُ فِي مِيمِ مَا، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِيَتَبَرَّأُ.", "«from what» — ʿan with its nūn merged into mā.", "«… -dan» — nûn'u mâ'nın mîm'ine idğam edilmiş an.", segments=[seg("عَنْ", "an", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("تَقَوَّلَهُ", "taqawwala", "verb", [MW, MB, "form-v-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ مَفْعُولٌ بِهِ — صِلَةُ الْمَوْصُولِ؛ تَقَوَّلَ عَلَيْهِ: افْتَرَى.", "«fabricated» — the ṣila; «it» its object; taqawwala ʿalā = to invent a saying against.", "«uydurdukları» — sıla; «onu» mef'ûl.", segments=[seg("تَقَوَّلَ", "taqawwala", "verb"), seg("هُ", "pron-3ms", "pron")]),
  fail("النَّاسُ", "nas", "«people»", "«insanlar»"),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«about him»", "«onun hakkında»", punct="،"),
  v_pl_pron("وَعَامَلُوهُ", "amala", "عَامَلُو", "هُ", "pron-3ms", "«and treated him»", "«ve ona davrandıkları»", tags=[MW, "form-iii-verbs"], wa=True),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with [it]»", "«onunla»", punct="،"),
  mudari_wa("وَيُوضِحُ", "awdaha", "«and makes plain»", "«ve açıklar»", tags=["form-iv-verbs", "mithal-verbs"], hidden="هُوَ (عِيسَى)"),
  noun_pron("دَعْوَتَهُ", "dawa", "دَعْوَتَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his call» — the object.", "«davetini» — mef'ûl.", tags=[MB, ID]),
  fi(),
  majrur("قُوَّةٍ", "quwwa", "«strength»", "«güç»"),
  atf("وَصِدْقٍ", "sidq", "«truthfulness»", "«doğruluk»", punct="،"),
  mudari_wa("وَيُدِينُ", "adana", "«and condemns»", "«ve kınar»", tags=["form-iv-verbs", "hollow-verbs"], hidden="هُوَ", extra=" — أَدَانَهُ: حَكَمَ عَلَيْهِ وَاتَّهَمَهُ"),
  fi(),
  tok("هٰذِهِ", "hadhihi", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("الْقَضِيَّةِ", "qadiyya", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ (أَوْ عَطْفُ بَيَانٍ) مَجْرُورٌ بِالْكَسْرَةِ.", "«matter» — in apposition to «this».", "«mesele» — işaret isminden bedel."),
  maful_("الْغُلَاةَ", "ghali-extremist", "«the extremists»", "«aşırıya gidenleri»", tags=[JT], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ غَالٍ: الْمُجَاوِزُ الْحَدَّ."),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ."),
  noun_pron("أُمَّتِهِ", "umma", "أُمَّتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his community»", "«ümmetinden»", punct="،", tags=[HJ, ID]),
  tok("وَأَنَّهُمْ", "anna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهُمْ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى مَفْعُولِ يُدِينُ (يُدِينُ كَوْنَهُمْ…) أَوْ مَجْرُورٌ بِبَاءٍ مَحْذُوفَةٍ.", "«and that they» — the anna-clause joined to the object of «condemns».", "«ve onların … olduğunu» — enne cümlesi «kınar»ın mef'ûlüne atıf.", segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("هُمُ", "hum", "pron", [IW, "tawkid"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ مُبْتَدَأٌ)، حُرِّكَ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«they [alone]» — the pronoun of separation; its ḍamma breaks two sukūns.", "«onlar» — fasıl zamiri; iki sâkinden ötürü ötre."),
  tok("الْمَسْئُولُونَ", "masul", "noun", [IW, JS], "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ مَفْعُولٍ مِنْ سَأَلَ.", "«answerable» — anna's khabar; a passive participle.", "«sorumlu» — enne'nin haberi; ism-i mef'ûl."),
  tok("وَحْدَهُمْ", "wahda", "noun", [HL, ID], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — مُنْفَرِدِينَ.", "«alone» — a ḥāl.", "«yalnızca» — hâl.", segments=[seg("وَحْدَ", "wahda", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("عَنْ", "an", "«for»", "«-dan»"),
  tok("هٰذِهِ", "hadhihi", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("الْجَرِيمَةِ", "jarima", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«crime» — in apposition.", "«suç» — bedel.", punct="،"),
])
sen("s5", "read the Qurʾān, and let yourselves feel the majesty of the moment and the splendour of the scene:",
        "Kur'ân'ı okuyun ve o anın heybetini, sahnenin ihtişamını hissedin:", [
  tok("اقْرَؤُوا", "qaraa", "verb", [AM, MB], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَهْمُوزُ اللَّامِ: كُتِبَتْ هَمْزَتُهُ عَلَى وَاوٍ لِضَمِّهَا بَعْدَ فَتْحٍ.", "«read» — an imperative; the final hamza sits on a wāw.", "«okuyun» — emir; son hemze vâv üzerinde."),
  maful_("الْقُرْآنَ", "quran", "«the Qurʾān»", "«Kur'ân'ı»", punct="،"),
  tok("وَلْتَسْتَشْعِرُوا", "istashara", "verb", [AT, AM, MB, "form-x-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لَامُ الْأَمْرِ سُكِّنَتْ بَعْدَ الْوَاوِ، وَتَسْتَشْعِرُوا فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَامِ الْأَمْرِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ — قِرَاءَةٌ مُصَحَّحَةٌ: الْمَطْبُوعُ «وَلِنَسْتَشْعِرُوا» تَصْحِيفٌ (لَا تَجْتَمِعُ نُونُ الْمُتَكَلِّمِ وَوَاوُ الْجَمَاعَةِ).", "«and let yourselves feel» — the lām of command, sukūn after the wāw; the verb is jussive by its dropped nūn. The print's «wa-li-nastashʿirū» is a misprint (a 1st-person prefix cannot carry the group's wāw); read as declared.", "«ve hissedin» — emir lâmı, vâv'dan sonra sâkin; nûn'un hazfiyle meczûm. Baskıdaki «ve-li-nesteş'irû» tashif (mütekellim nûn'u ile cemi vâv'ı birleşmez); okunuş beyan edilmiştir.", segments=[seg("وَ", "wa", "conj"), seg("لْتَسْتَشْعِرُوا", "istashara", "verb")]),
  maful_("جَلَالَ", "jalal", "«the majesty [of]»", "«heybetini»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("الْمَوْقِفِ", "mawqif", "«the moment»", "«o anın»"),
  atf("وَرَوْعَةَ", "rawa-splendour", "«and the splendour [of]»", "«ve ihtişamını»", case="nasb", tags=[ID]),
  mudaf_ilayh("الْمَشْهَدِ", "mashhad", "«the scene»", "«sahnenin»", punct=":"),
])
sen("s6", "«And when God says: O ʿĪsā son of Maryam, did you say to the people: take me and my mother as two gods besides God? He says: Glory be to You! It is not for me to say what I have no right to. If I had said it, You would have known it. You know what is in my soul, and I do not know what is in Yours; You are the Knower of the unseen.» (5:116)",
        "«Allah: Ey Meryem oğlu Îsâ, insanlara: Allah'ı bırakıp beni ve annemi iki ilâh edinin, diye sen mi söyledin? dediğinde, o: Seni tenzih ederim, hakkım olmayan bir şeyi söylemek bana yakışmaz; eğer söylemiş olsaydım elbette bilirdin. Sen benim içimdekini bilirsin, ben Senin zâtındakini bilmem; şüphesiz Sen gaybları hakkıyla bilensin, der.» (Mâide 116)", [
  *quran([
  tok("وَإِذْ", "idh", "noun", [AT, MF], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِذْ ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: اذْكُرْ.", "«and when» — the ẓarf; its governing «remember» is unspoken.", "«ve … zaman» — zarf; âmili «hatırla» mahzûf.", segments=wa_("إِذْ", "idh", "noun")),
  mazi("قَالَ", "qala", "«says»", "«der»", tags=["hollow-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  allah_fail(),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("عِيسَى", "isa", "propn", ["vocative-munada", MM], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ.", "«ʿĪsā» — the munādā, a single proper name.", "«Îsâ» — müfred alem münâdâ."),
  tok("ابْنَ", "ibn", "noun", [NA, ID, "vocative-munada"], "نَعْتٌ لِعِيسَى مَنْصُوبٌ بِالْفَتْحَةِ (وَيَجُوزُ ضَمُّهُ)، مُضَافٌ.", "«son [of]» — a naʿt of the munādā, in naṣb (ḍamma also allowed), annexed.", "«oğlu» — münâdânın sıfatı, mansûb; muzâf."),
  tok("مَرْيَمَ", "maryam", "propn", [ID, "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Maryam» — a diptote.", "«Meryem» — gayr-i munsarıf."),
  tok("أَأَنْتَ", "anta", "pron", [IS, MK], "الْهَمْزَةُ لِلِاسْتِفْهَامِ (تَقْرِيرٌ وَتَوْبِيخٌ لِلْمُدَّعِينَ)، وَأَنْتَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«did you» — the hamza of the question; «you» the mubtadaʾ.", "«sen mi» — istifham hemzesi; «sen» mübtedâ.", segments=[seg("أَ", "hamza-istifham", "part"), seg("أَنْتَ", "anta", "pron")]),
  tu_mazi("قُلْتَ", "qala", "قُلْ", "«said» — the māḍī with the doer's tāʾ; the sentence is the khabar.", "«söyledin» — fâil tâ'sı; cümle haber.", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرٌ.", tags=[MK, "hollow-verbs"], person="تَ", person_lex="pron-2ms"),
  li_noun("لِلنَّاسِ", "nas", "«to the people»", "«insanlara»", punct=":"),
  tok("اتَّخِذُونِي", "ittakhadha", "verb", [AM, MB, "form-viii-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ أَوَّلُ — مَقُولُ الْقَوْلِ.", "«take me» — an imperative; the guarding nūn, then «me» as first object.", "«beni edinin» — emir; vikâye nûn'u, «beni» ilk mef'ûl.", segments=[seg("اتَّخِذُو", "ittakhadha", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tok("وَأُمِّيَ", "umm", "noun", [AT, MB, ID, "ya-al-mutakallim"], "الْوَاوُ عَاطِفَةٌ، وَأُمِّ مَعْطُوفٌ عَلَى يَاءِ الْمُتَكَلِّمِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ (فُتِحَتْ).", "«and my mother» — joined to «me».", "«ve annemi» — «beni»ye atıf.", segments=[seg("وَ", "wa", "conj"), seg("أُمِّ", "umm", "noun"), seg("يَ", "pron-1s", "pron")]),
  tok("إِلٰهَيْنِ", "ilah", "noun", [MB, "al-muthanna"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.", "«as two gods» — the second object; a dual in naṣb by the yāʾ.", "«iki ilâh» — ikinci mef'ûl; tesniye."),
  prep("مِنْ", "min", "«[from]»", "«-den»"),
  tok("دُونِ", "duna", "noun", [HJ, ID], "مَجْرُورٌ بِمِنْ، مُضَافٌ.", "«besides [God]»", "«Allah'ı bırakıp»"),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah»", punct="؟"),
  mazi("قَالَ", "qala", "«he says»", "«der»", tags=["hollow-verbs"], hidden="هُوَ (عِيسَى)", punct=":"),
  tok("سُبْحَانَكَ", "subhan", "noun", [ID, "maful-mutlaq", "hadhf-wa-taqdir"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ وُجُوبًا (أُسَبِّحُ)، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«glory be to You» — an absolute object whose verb is always unspoken.", "«Seni tenzih ederim» — fiili dâimâ hazfedilen mef'ûl-i mutlak.", segments=[seg("سُبْحَانَ", "subhan", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not»", "«değil»"),
  tok("يَكُونُ", "kana", "verb", [KN, "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«it is» — kāna; its ism is the clause «that I should say».", "«olur» — kâne; ismi masdar-ı müevvel."),
  li_pron("لِي", "ي", "pron-1s", "«for me»", "«bana»", extra=" — خَبَرُ يَكُونُ مُقَدَّمٌ"),
  tok("أَنْ", "an-masdariyya", "part", [AN, KN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ اسْمُ يَكُونُ مُؤَخَّرٌ.", "«that» — its clause is kāna's ism.", "«-mek» — masdar-ı müevvel kâne'nin ismi."),
  tok("أَقُولَ", "qala", "verb", [AN, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا.", "«I should say» — naṣb; the doer «I» concealed.", "«söylemem» — mansûb; fâil gizli «ben»."),
  ma_mawsul_obj("«what»", "«… şeyi»"),
  tok("لَيْسَ", "laysa", "verb", [MW, KN], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — صِلَةُ الْمَوْصُولِ.", "«is not» — the frozen laysa; the ṣila.", "«değildir» — câmid leyse; sıla."),
  li_pron("لِي", "ي", "pron-1s", "«for me»", "«benim»", extra=" — مُتَعَلِّقٌ بِخَبَرِ لَيْسَ"),
  bi_noun("بِحَقٍّ", "haqq", "«a right»", "«hakkım»", extra=" — الْبَاءُ زَائِدَةٌ، وَحَقٍّ خَبَرُ لَيْسَ مَنْصُوبٌ مَحَلًّا (أَوْ حَالٌ)"),
  tok("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tu_mazi("كُنْتُ", "kana", "كُنْ", "«I had» — kāna as the condition's verb; the tāʾ is its ism.", "«idiysem» — şart fiili kâne; tâ ismi.", "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهُ.", tags=[SH, KN, "hollow-verbs"]),
  tu_mazi("قُلْتُهُ", "qala", "قُلْ", "«said it» — the khabar of kuntu; «it» the object.", "«onu söyledim» — küntü'nün haberi; «onu» mef'ûl.", "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ كُنْتُ.", tags=[KN, MB, "hollow-verbs"], obj="هُ", obj_lex="pron-3ms"),
  fa_qad_shart(),
  tu_mazi("عَلِمْتَهُ", "alima", "عَلِمْ", "«You would have known it» — the answer of the condition.", "«onu bilirdin» — şartın cevabı.", "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", tags=[SH, MB], person="تَ", person_lex="pron-2ms", obj="هُ", obj_lex="pron-3ms", punct="."),
  mudari("تَعْلَمُ", "alima", "«You know»", "«bilirsin»", tags=[MK], hidden="أَنْتَ", extra_ar=" — اسْتِئْنَافٌ بَيَانِيٌّ"),
  ma_mawsul_obj("«what»", "«… -i»"),
  fi(),
  tok("نَفْسِي", "nafs", "noun", [HJ, ID, "ya-al-mutakallim", MW], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ صِلَةُ مَا.", "«my soul» — the kasra is hidden before the speaker's yāʾ; the phrase is the ṣila.", "«içimde» — mütekellim yâ'sından önce kesre takdirî; sıla.", segments=[seg("نَفْسِ", "nafs", "noun"), seg("ي", "pron-1s", "pron")]),
  la_nafiya("وَلَا", wa=True),
  neg_mudari("أَعْلَمُ", "alima", "«I know»", "«bilirim»", hidden="أَنَا"),
  ma_mawsul_obj("«what»", "«… -i»"),
  fi(),
  noun_pron("نَفْسِكَ", "nafs", "نَفْسِ", "كَ", "pron-2ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — صِلَةٌ؛ نَفْسُ اللهِ: ذَاتُهُ.", "«Your self» — God's essence; the ṣila.", "«Senin zâtında» — sıla.", tags=[HJ, ID, MW], punct="."),
  tok("إِنَّكَ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ اسْمُهَا.", "«indeed You»", "«şüphesiz Sen»", segments=[seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَنْتَ", "anta", "pron", [IW, "tawkid"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ (أَوْ تَوْكِيدٌ لِلْكَافِ، أَوْ مُبْتَدَأٌ).", "«You» — the pronoun of separation.", "«Sen» — fasıl zamiri."),
  tok("عَلَّامُ", "allam", "noun", [IW, ID, "sighat-mubalagha"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَعَّالٍ.", "«the all-Knower [of]» — inna's khabar; an intensive on faʿʿāl.", "«hakkıyla bilen» — inne'nin haberi; fa'âl vezninde mübalağa."),
  mudaf_ilayh("الْغُيُوبِ", "ghayb", "«the unseen things»", "«gaybların»", tags=[JT], punct=AYA),
  ]),
])
sen("s7", "«I said to them nothing but what You commanded me: worship God, my Lord and your Lord. I was a witness over them as long as I remained among them; and when You took me up, You were the Watcher over them, and You are Witness over all things.» (5:117)",
        "«Ben onlara, bana emrettiğinden başkasını söylemedim: benim de Rabbim, sizin de Rabbiniz olan Allah'a kulluk edin, dedim. Aralarında bulunduğum sürece onlara şahittim; beni aralarından aldığında artık onları gözeten Sen'din. Sen her şeye şahitsin.» (Mâide 117)", [
  *quran([
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "«not»", "«-medim»"),
  tu_mazi("قُلْتُ", "qala", "قُلْ", "«I said»", "«söyledim»", "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ.", tags=["hollow-verbs"]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»"),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ حَصْرٍ (اسْتِثْنَاءٌ مُفَرَّغٌ).", "«except» — restriction: the exception is emptied.", "«-den başka» — hasr; müferrağ istisnâ."),
  ma_mawsul_obj("«what»", "«… şeyi»"),
  tok("أَمَرْتَنِي", "amara-order", "verb", [MW, MB], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — صِلَةُ الْمَوْصُولِ.", "«You commanded me» — the ṣila; the guarding nūn before «me».", "«bana emrettin» — sıla; vikâye nûn'u.", segments=[seg("أَمَرْ", "amara-order", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«[with it]»", "«onu»", punct=":"),
  tok("أَنِ", "an-masdariyya", "part", [AN, BD], "حَرْفٌ مَصْدَرِيٌّ (أَوْ تَفْسِيرِيٌّ)، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْمَصْدَرُ بَدَلٌ مِنْ مَا، أَوِ الْجُمْلَةُ تَفْسِيرٌ لَهُ.", "«that» — the explanatory an, with kasra before the joining hamza.", "«ki» — tefsir en'i; iki sâkinden ötürü kesre."),
  *worship_tokens(),
  tu_mazi("وَكُنْتُ", "kana", "كُنْ", "«and I was» — kāna with the tāʾ as its ism.", "«ve idim» — kâne; tâ ismi.", "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ.", tags=[AT, KN, "hollow-verbs"]),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«over them»", "«onlara»"),
  khabar_kana("شَهِيدًا", "shahid-witness", "«a witness»", "«şahit»"),
  tok("مَا", "ma-masdariyya", "part", [MF], "مَا مَصْدَرِيَّةٌ ظَرْفِيَّةٌ: مُدَّةَ دَوَامِي.", "«as long as» — the temporal maṣdar-mā.", "«-dığı sürece» — zarfî masdariyye mâ."),
  tu_mazi("دُمْتُ", "dama", "دُمْ", "«I remained» — dāma with the tāʾ as its ism; the phrase after it is its khabar.", "«kaldım» — dâme; tâ ismi.", "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ، وَالظَّرْفُ بَعْدَهُ خَبَرُهُ.", tags=[KN, "hollow-verbs"]),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«among them»", "«aralarında»", punct="."),
  tok("فَلَمَّا", "lamma", "noun", [AT, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the ẓarf carrying the sense of a condition.", "«-ınca» — şart mânâsı taşıyan zarf.", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "noun")]),
  tok("تَوَفَّيْتَنِي", "tawaffa", "verb", [MB, "form-v-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا.", "«You took me up» — a defective Form V with the doer's tāʾ.", "«beni aldığında» — nâkıs tefe''ul; fâil tâ'sı.", segments=[seg("تَوَفَّيْ", "tawaffa", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  tu_mazi("كُنْتَ", "kana", "كُنْ", "«You were» — the answer of lammā.", "«Sen idin» — lemmâ'nın cevabı.", "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ اسْمُهُ — جَوَابُ لَمَّا.", tags=[KN, "hollow-verbs"], person="تَ", person_lex="pron-2ms"),
  tok("أَنْتَ", "anta", "pron", [KN, "tawkid"], "ضَمِيرُ فَصْلٍ (أَوْ تَوْكِيدٌ لِلتَّاءِ).", "«You» — the pronoun of separation.", "«Sen» — fasıl zamiri."),
  khabar_kana("الرَّقِيبَ", "raqib", "«the Watcher»", "«gözeten»", tags=["sighat-mubalagha"]),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«over them»", "«onları»", punct="."),
  tok("وَأَنْتَ", "anta", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَأَنْتَ مُبْتَدَأٌ.", "«and You» — the mubtadaʾ.", "«ve Sen» — mübtedâ.", segments=wa_("أَنْتَ", "anta", "pron")),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeye»"),
  tok("شَهِيدٌ", "shahid-witness", "noun", [MK, "sighat-mubalagha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«Witness» — the khabar.", "«şahitsin» — haber.", punct=AYA),
  ]),
])
sen("s8", "«If You punish them, they are Your servants; and if You forgive them, You are the Mighty, the Wise.» (5:118)",
        "«Onlara azap edersen, onlar Senin kullarındır; onları bağışlarsan, şüphesiz Sen azîz ve hakîmsin.» (Mâide 118)", [
  *quran([
  tok("إِنْ", "in-shartiyya", "part", [SH, "in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("تُعَذِّبْهُمْ", "adhdhaba", "verb", [SH, MB, "form-ii-verbs"], "فِعْلُ الشَّرْطِ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَهُمْ مَفْعُولٌ بِهِ.", "«You punish them» — the condition's verb, jussive.", "«onlara azap edersen» — şart fiili, meczûm.", segments=[seg("تُعَذِّبْ", "adhdhaba", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("فَإِنَّهُمْ", "inna", "part", [SH, IW], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَهُمْ اسْمُهَا.", "«then they» — the answer opens with inna.", "«artık onlar» — cevap inne ile.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  noun_pron("عِبَادُكَ", "ibad", "عِبَادُ", "كَ", "pron-2ms", "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ فِي مَحَلِّ جَزْمٍ.", "«Your servants» — inna's khabar.", "«Senin kullarındır» — inne'nin haberi.", tags=[IW, ID]),
  tok("وَإِنْ", "in-shartiyya", "part", [AT, SH], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa_("إِنْ", "in-shartiyya", "part")),
  tok("تَغْفِرْ", "ghafara", "verb", [SH], "فِعْلُ الشَّرْطِ مَجْزُومٌ بِالسُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«You forgive» — jussive.", "«bağışlarsan» — meczûm."),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«them»", "«onları»"),
  tok("فَإِنَّكَ", "inna", "part", [SH, IW], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَإِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ اسْمُهَا.", "«then You»", "«şüphesiz Sen»", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَنْتَ", "anta", "pron", [IW, "tawkid"], "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ.", "«You» — the pronoun of separation.", "«Sen» — fasıl zamiri."),
  tok("الْعَزِيزُ", "aziz", "noun", [IW, "sighat-mubalagha"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Mighty» — inna's khabar.", "«azîz» — inne'nin haberi."),
  tok("الْحَكِيمُ", "hakim", "noun", [IW, "sighat-mubalagha"], "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ.", "«the Wise» — a second khabar.", "«hakîm» — ikinci haber.", punct=AYA),
  ]),
])
sen("s9", "«God says: This is the Day when the truthful will profit from their truthfulness. Theirs are gardens beneath which rivers flow, abiding therein for ever. God is pleased with them and they are pleased with Him. That is the great triumph.» (5:119)",
        "«Allah buyurur: Bu, doğrulara doğruluklarının fayda vereceği gündür. Onlara, içinde ebedî kalacakları, altından ırmaklar akan cennetler vardır. Allah onlardan razı olmuş, onlar da O'ndan razı olmuşlardır. İşte büyük kurtuluş budur.» (Mâide 119)", [
  *quran([
  mazi("قَالَ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs"], hidden=None),
  allah_fail(punct=":"),
  tok("هٰذَا", "hadha", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«this» — the mubtadaʾ.", "«bu» — mübtedâ."),
  tok("يَوْمُ", "yawm", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ (وَقُرِئَ بِالنَّصْبِ عَلَى الظَّرْفِيَّةِ).", "«the Day» — the khabar, annexed to the sentence after it.", "«gündür» — haber; sonraki cümleye muzâf."),
  tok("يَنْفَعُ", "nafaa", "verb", [ID, "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«profits» — its sentence is the muḍāf ilayh of «Day».", "«fayda verir» — cümle «gün»ün muzâfun ileyhi."),
  tok("الصَّادِقِينَ", "sadiq", "noun", [MB, JS, "ism-fail"], "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the truthful» — the object, placed before the doer.", "«doğrulara» — fâilden önce gelen mef'ûl."),
  noun_pron("صِدْقُهُمْ", "sidq", "صِدْقُ", "هُمْ", "pron-3mp", "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ.", "«their truthfulness» — the delayed doer.", "«doğrulukları» — sonraya bırakılmış fâil.", tags=[FL, ID], punct="."),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«theirs»", "«onlara»", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ"),
  tok("جَنَّاتٌ", "janna", "noun", [MK, JT], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«gardens» — the delayed mubtadaʾ.", "«cennetler» — sonraya bırakılmış mübtedâ."),
  tok("تَجْرِي", "jara", "verb", ["jumla-sifa", "naqis-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِجَنَّاتٌ.", "«flow» — the ḍamma hidden on the yāʾ; the sentence is a naʿt of «gardens».", "«akar» — zamme yâ üzerinde takdirî; cümle «cennetler»in sıfatı."),
  prep("مِنْ", "min", "«from»", "«-ndan»"),
  noun_pron("تَحْتِهَا", "tahta", "تَحْتِ", "هَا", "pron-3fs", "ظَرْفُ مَكَانٍ مَجْرُورٌ بِمِنْ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«beneath them»", "«altından»", tags=[HJ, ID]),
  fail("الْأَنْهَارُ", "nahr", "«the rivers»", "«ırmaklar»", tags=[JT]),
  tok("خَالِدِينَ", "khalid", "noun", [HL, JS, "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — صَاحِبُ الْحَالِ الضَّمِيرُ فِي لَهُمْ.", "«abiding» — a ḥāl of «them».", "«ebedî kalıcılar olarak» — «onlara»nın hâli."),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«therein»", "«orada»"),
  tok("أَبَدًا", "abad-eternity", "noun", [MF], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ لِلتَّأْبِيدِ.", "«for ever» — a ẓarf of time.", "«ebediyen» — zaman zarfı.", punct="."),
  mazi("رَضِيَ", "radiya", "«is pleased»", "«razı oldu»", tags=["naqis-verbs"], hidden=None, extra_ar=" — اسْتِئْنَافٌ (أَوْ حَالٌ)"),
  allah_fail(),
  prep_pron("عَنْهُمْ", "an", "هُمْ", "pron-3mp", "«with them»", "«onlardan»"),
  tok("وَرَضُوا", "radiya", "verb", [AT, "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرَضُوا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، حُذِفَتْ لَامُهُ (الْيَاءُ) لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ فَاعِلٌ.", "«and they are pleased» — the defective verb's yāʾ dropped before the group's wāw.", "«ve onlar razı oldular» — nâkıs fiilin yâ'sı cemi vâvından önce düşmüş.", segments=wa_("رَضُوا", "radiya", "verb")),
  prep_pron("عَنْهُ", "an", "هُ", "pron-3ms", "«with Him»", "«O'ndan»", punct="."),
  tok("ذٰلِكَ", "dhalika", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«that» — the mubtadaʾ.", "«işte bu» — mübtedâ."),
  tok("الْفَوْزُ", "fawz", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the triumph» — the khabar.", "«kurtuluş» — haber."),
  naat("الْعَظِيمُ", "azim", "«great»", "«büyük»", case="raf", punct=AYA),
  ]),
])
sen("s10", "«To God belongs the dominion of the heavens and the earth and what is in them, and He has power over all things.» (5:120)",
        "«Göklerin, yerin ve içindekilerin mülkü Allah'ındır; O her şeye kâdirdir.» (Mâide 120)", [
  *quran([
  tok("لِلّٰهِ", "allah", "propn", [HJ, MK], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«to God» — the fronted khabar.", "«Allah'ındır» — öne alınmış haber.", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("مُلْكُ", "mulk", "noun", [MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the dominion [of]» — the delayed mubtadaʾ.", "«mülkü» — sonraya bırakılmış mübtedâ."),
  mudaf_ilayh("السَّمَاوَاتِ", "sama", "«the heavens»", "«göklerin»", tags=[JT]),
  atf("وَالْأَرْضِ", "ard", "«and the earth»", "«ve yerin»"),
  tok("وَمَا", "ma-mawsula", "pron", [AT, MW], "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مَعْطُوفٌ عَلَى السَّمَاوَاتِ.", "«and what» — joined to «the heavens».", "«ve … şeylerin» — «gökler»e atıf.", segments=wa_("مَا", "ma-mawsula", "pron")),
  prep_pron("فِيهِنَّ", "fi", "هِنَّ", "pron-3fp", "«is in them»", "«içlerindeki»", extra_ar=" — صِلَةُ الْمَوْصُولِ؛ وَالضَّمِيرُ لِلسَّمَاوَاتِ وَالْأَرْضِ (جَمْعُ مَا لَا يَعْقِلُ)"),
  tok("وَهُوَ", "huwa", "pron", [AT, MK], "الْوَاوُ عَاطِفَةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and He» — the mubtadaʾ.", "«ve O» — mübtedâ.", segments=wa_("هُوَ", "huwa", "pron")),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«thing»", "«şeye»"),
  tok("قَدِيرٌ", "qadir-almighty", "noun", [MK, "sighat-mubalagha"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — فَعِيلٌ بِمَعْنَى قَادِرٍ لِلْمُبَالَغَةِ.", "«has power» — the khabar; faʿīl for qādir, intensified.", "«kâdirdir» — haber; mübalağa için fa'îl.", punct="."),
  ]),
])

CAND = {
 "jamil": G("jamil", "جَمِيل", "ج م ل", "noun", "beautiful", "güzel", 1),
 "tabaa": G("tabaa", "طَبَعَ", "ط ب ع", "verb", "to stamp, to mould; ṭubiʿa ʿalā: to be moulded upon", "basmak, damgalamak; tubia alâ: … üzere yaratılmak", 2),
 "khudu": G("khudu", "خُضُوع", "خ ض ع", "noun", "submission, humbling oneself", "boyun eğme, huşû", 1),
 "istankafa": G("istankafa", "اِسْتَنْكَفَ", "ن ك ف", "verb", "to disdain, to hold oneself above (Form X)", "çekinmek, kendini üstün görüp kaçınmak (istif'âl)", 2),
 "hashara": G("hashara", "حَشَرَ", "ح ش ر", "verb", "to gather, to assemble (the dead for judgement)", "toplamak, haşretmek", 1),
 "zada": G("zada", "زَادَ", "ز ي د", "verb", "to increase, to give more", "artırmak, fazlasını vermek", 1),
 "alim-painful": G("alim-painful", "أَلِيم", "أ ل م", "noun", "painful", "acı, elîm", 1),
 "wali": G("wali", "وَلِيّ", "و ل ي", "noun", "a protector, an ally", "dost, velî", 1, plural="أَوْلِيَاء"),
 "sawwara": G("sawwara", "صَوَّرَ", "ص و ر", "verb", "to depict, to paint a picture of (Form II)", "tasvir etmek (tef'îl)", 1),
 "balagha-eloquence": G("balagha-eloquence", "بَلَاغَة", "ب ل غ", "noun", "eloquence", "belâgat", 1),
 "ijaz-inimitability": G("ijaz-inimitability", "إِعْجَاز", "ع ج ز", "noun", "inimitability (of the Qurʾān); rendering others unable", "i'câz; âciz bırakma", 2),
 "mashhad": G("mashhad", "مَشْهَد", "ش ه د", "noun", "a scene", "sahne, manzara", 1, plural="مَشَاهِد"),
 "rai": G("rai", "رَائِع", "ر و ع", "noun", "splendid, magnificent", "muhteşem, harikulâde", 1),
 "tabarraa": G("tabarraa", "تَبَرَّأَ", "ب ر أ", "verb", "to disown, to declare oneself free of (Form V)", "berî olduğunu bildirmek, uzak durmak (tefe''ul)", 2),
 "taqawwala": G("taqawwala", "تَقَوَّلَ", "ق و ل", "verb", "to fabricate a saying (against someone) (Form V)", "(birine) söz uydurmak, iftira etmek (tefe''ul)", 2),
 "awdaha": G("awdaha", "أَوْضَحَ", "و ض ح", "verb", "to make clear (Form IV)", "açıklamak, izah etmek (if'âl)", 1),
 "adana": G("adana", "أَدَانَ", "د ي ن", "verb", "to condemn, to hold guilty (Form IV)", "kınamak, suçlu bulmak (if'âl)", 2),
 "ghali-extremist": G("ghali-extremist", "غَالٍ", "غ ل و", "noun", "an extremist, one who exceeds the limit", "aşırıya giden, gulât", 2, plural="غُلَاة"),
 "masul": G("masul", "مَسْئُول", "س أ ل", "noun", "answerable, responsible (a passive participle)", "sorumlu (ism-i mef'ûl)", 1),
 "istashara": G("istashara", "اِسْتَشْعَرَ", "ش ع ر", "verb", "to feel inwardly, to sense (Form X)", "içinde hissetmek, duymak (istif'âl)", 2),
 "jalal": G("jalal", "جَلَال", "ج ل ل", "noun", "majesty", "celâl, heybet", 1),
 "rawa-splendour": G("rawa-splendour", "رَوْعَة", "ر و ع", "noun", "splendour, awe-inspiring beauty", "ihtişam, hayranlık veren güzellik", 2),
 "allam": G("allam", "عَلَّام", "ع ل م", "noun", "the all-Knowing (an intensive form)", "her şeyi hakkıyla bilen (mübalağa sîgası)", 1),
 "shahid-witness": G("shahid-witness", "شَهِيد", "ش ه د", "noun", "a witness (an intensive form)", "şahit (mübalağa sîgası)", 1),
 "tawaffa": G("tawaffa", "تَوَفَّى", "و ف ي", "verb", "to take (a soul) in full, to cause to die (Form V)", "(ruhu) tam olarak almak, vefat ettirmek (tefe''ul)", 2),
 "ghafara": G("ghafara", "غَفَرَ", "غ ف ر", "verb", "to forgive", "bağışlamak", 1),
 "nahr": G("nahr", "نَهْر", "ن ه ر", "noun", "a river", "nehir, ırmak", 1, plural="أَنْهَار"),
 "khalid": G("khalid", "خَالِد", "خ ل د", "noun", "abiding for ever (an active participle)", "ebedî kalan (ism-i fâil)", 1),
 "abad-eternity": G("abad-eternity", "أَبَد", "أ ب د", "noun", "eternity; abadan: for ever", "ebed; ebeden: sonsuza dek", 1),
 "radiya": G("radiya", "رَضِيَ", "ر ض و", "verb", "to be pleased (with)", "razı olmak", 1),
 "fawz": G("fawz", "فَوْز", "ف و ز", "noun", "triumph, success", "kurtuluş, başarı", 1),
 "qadir-almighty": G("qadir-almighty", "قَدِير", "ق د ر", "noun", "all-powerful (an intensive form)", "her şeye gücü yeten, Kadîr (mübalağa)", 1),
 "pron-3fp": G("pron-3fp", "ـهُنَّ", None, "pron", "them / their (fem. plur.)", "onları / onların (dişil çoğul)", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "me / my", "beni / benim", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masc. sing.)", "seni / senin", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (masc. plur.)", "sizi / sizin", 1),
 "pron-3ms": G("pron-3ms", "ـهُ", None, "pron", "him / his / it", "onu / onun", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them / their", "onları / onların", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it", "onu / onun (dişil)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tabaa", _sg.sound1("fataha", "طَبَع", "طْبَع", "اِطْبَع", "طَبْع", "طَابِع", "مَطْبُوع", "طُبِعَ", "يُطْبَعُ", "طَبَعَ الشَّيْءَ يَطْبَعُهُ: خَتَمَهُ وَصَاغَهُ عَلَى مِثَالٍ؛ وَطُبِعَ عَلَى الْخُلُقِ: جُبِلَ عَلَيْهِ."))
put_morph(mo, "istankafa", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَنْكَف", "سْتَنْكِف", "اِسْتَنْكِف", "اِسْتِنْكَاف", "مُسْتَنْكِف", None, None, None, "اِسْتَنْكَفَ عَنِ الشَّيْءِ: أَنِفَ مِنْهُ وَامْتَنَعَ تَرَفُّعًا."))
put_morph(mo, "hashara", _sg.sound1("nasara", "حَشَر", "حْشُر", "اُحْشُر", "حَشْر", "حَاشِر", "مَحْشُور", "حُشِرَ", "يُحْشَرُ", "حَشَرَ النَّاسَ يَحْشُرُهُمْ: جَمَعَهُمْ وَسَاقَهُمْ."))
put_morph(mo, "zada", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "زَاد", "زِد", "زِيد", "زِد", "زِد", "زِد", "زِيَادَة", "زَائِد", "مَزِيد", "زِيدَ", "يُزَادُ", "زَادَ الشَّيْءُ يَزِيدُ: نَمَا؛ وَزَادَهُ كَذَا: أَعْطَاهُ فَوْقَ مَا عِنْدَهُ."))
put_morph(mo, "sawwara", _sg.derived(_sg.B2, _sg.W2, "ُ", "صَوَّر", "صَوِّر", "صَوِّر", "تَصْوِير", "مُصَوِّر", "مُصَوَّر", "صُوِّرَ", "يُصَوَّرُ", "صَوَّرَ الشَّيْءَ: جَعَلَ لَهُ صُورَةً، وَرَسَمَهُ؛ وَصَوَّرَ الْمَشْهَدَ: وَصَفَهُ وَصْفًا يُرِيهِ."))
put_morph(mo, "tabarraa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَرَّأ", "تَبَرَّأ", "تَبَرَّأ", "تَبَرُّؤ", "مُتَبَرِّئ", None, None, None, "تَبَرَّأَ مِنْهُ: تَنَزَّهَ عَنْهُ وَأَعْلَنَ بَرَاءَتَهُ — مَهْمُوزُ اللَّامِ."))
put_morph(mo, "taqawwala", _sg.derived(_sg.B5, _sg.W5, "َ", "تَقَوَّل", "تَقَوَّل", "تَقَوَّل", "تَقَوُّل", "مُتَقَوِّل", "مُتَقَوَّل", "تُقُوِّلَ", "يُتَقَوَّلُ", "تَقَوَّلَ عَلَيْهِ قَوْلًا: افْتَرَاهُ وَنَسَبَهُ إِلَيْهِ."))
put_morph(mo, "awdaha", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَوْضَح", "وضِح", "أَوْضِح", "إِيضَاح", "مُوضِح", "مُوضَح", "أُوضِحَ", "يُوضَحُ", "أَوْضَحَ الشَّيْءَ: بَيَّنَهُ وَكَشَفَهُ — مِثَالٌ وَاوِيٌّ: تَسْكُنُ وَاوُهُ بَعْدَ ضَمَّةِ الْمُضَارِعِ."))
put_morph(mo, "adana", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَدَان", "أَدَن", "دِين", "دِن", "أَدِين", "أَدِن", "إِدَانَة", "مُدِين", "مُدَان", "أُدِينَ", "يُدَانُ", "أَدَانَهُ: حَكَمَ عَلَيْهِ بِالذَّنْبِ وَاتَّهَمَهُ — أَجْوَفُ يَائِيٌّ."))
put_morph(mo, "istashara", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَشْعَر", "سْتَشْعِر", "اِسْتَشْعِر", "اِسْتِشْعَار", "مُسْتَشْعِر", "مُسْتَشْعَر", "اُسْتُشْعِرَ", "يُسْتَشْعَرُ", "اِسْتَشْعَرَ الشَّيْءَ: أَحَسَّ بِهِ فِي نَفْسِهِ."))
put_morph(mo, "tawaffa", _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَوَفَّ", "تَوَفّ", "a", "تَوَفّ", "تَوَفٍّ (التَّوَفِّي)", "مُتَوَفٍّ (الْمُتَوَفِّي)", "مُتَوَفًّى", "تُوُفِّيَ", "يُتَوَفَّى", "تَوَفَّى اللهُ فُلَانًا: قَبَضَ رُوحَهُ وَاسْتَوْفَى أَجَلَهُ — نَاقِصٌ يَائِيٌّ."))
put_morph(mo, "ghafara", _sg.sound1("daraba", "غَفَر", "غْفِر", "اِغْفِر", "غُفْرَان / مَغْفِرَة", "غَافِر", "مَغْفُور", "غُفِرَ", "يُغْفَرُ", "غَفَرَ لَهُ ذَنْبَهُ يَغْفِرُهُ: سَتَرَهُ وَعَفَا عَنْهُ."))
put_morph(mo, "radiya", _sg.naqis1("samia", "نَاقِصٌ وَاوِيٌّ (مِنْ بَابِ سَمِعَ)، مَاضِيهِ عَلَى فَعِلَ", "y", "رَضِ", "رْض", "a", "اِرْض", "رِضًا / رِضْوَان", "رَاضٍ (الرَّاضِي)", "مَرْضِيّ", "رُضِيَ", "يُرْضَى", "رَضِيَ عَنْهُ يَرْضَى: قَبِلَهُ وَأَحَبَّهُ، ضِدُّ سَخِطَ."))
# the hamza seats the generator cannot see: تَبَرَّأَا → تَبَرَّآ، تَبَرَّأُوا → تَبَرَّؤُوا (and the same in the muḍāriʿ and the amr)
def _hamza_seats(x):
    if isinstance(x, list): return [_hamza_seats(c) for c in x]
    if isinstance(x, str): return x.replace("أَا", "آ").replace("أُو", "ؤُو")
    return x
for _k in ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2"):
    if _k in mo["verbs"]["tabarraa"]: mo["verbs"]["tabarraa"][_k] = _hamza_seats(mo["verbs"]["tabarraa"][_k])
# رَضِيَ: the māḍī on فَعِلَ keeps its yāʾ (رَضِيَ، رَضِيَتْ، رَضِيتَ) and drops it only before the group's wāw (رَضُوا) — the
# fatḥa-type generator cannot write it, so the fourteen cells are given by hand (the muḍāriʿ يَرْضَى it writes correctly)
mo["verbs"]["radiya"]["mazi"] = ["رَضِيَ", "رَضِيَا", "رَضُوا", "رَضِيَتْ", "رَضِيَتَا", "رَضِينَ", "رَضِيتَ", "رَضِيتُمَا", "رَضِيتُمْ", "رَضِيتِ", "رَضِيتُمَا", "رَضِيتُنَّ", "رَضِيتُ", "رَضِينَا"]
mo["verbs"]["radiya"]["amr"] = ["اِرْضَ", "اِرْضَيَا", "اِرْضَوْا", "اِرْضَيْ", "اِرْضَيَا", "اِرْضَيْنَ"]
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch44 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 44 (print pp. 65–68; ʿĪsā §40–41): the rank of tawḥīd in his call — the beautiful style savoured by whoever knows the prophets' way (s1), al-Nisāʾ 4:172–173: the Messiah never disdains to be God's servant, nor the angels brought near; the two parties on the Day (s2–s3); the Qurʾān's splendid scene of the Resurrection, in which ʿĪsā disowns what was fabricated about him and condemns the extremists of his community (s4–s5) — al-Māʾida 5:116–120: «did you say: take me and my mother as two gods?», «I said to them nothing but what You commanded me», the Day the truthful profit, and God's dominion over all (s6–s10)."
ADD_TR = " Kırk dördüncü bölüm (baskı s. 65–68; Îsâ §40–41): davetinde tevhidin yeri — peygamberlerin yolunu bilenlerin tadına vardığı güzel üslûp (s1), Nisâ 172–173: Mesîh Allah'a kul olmaktan asla çekinmez, yakın melekler de; o gün iki taraf (s2–s3); Kur'ân'ın muhteşem kıyamet sahnesi: Îsâ hakkında uydurulanlardan uzak olduğunu bildirir, ümmetinin aşırılarını kınar (s4–s5) — Mâide 116–120: «beni ve annemi iki ilâh edinin, diye sen mi söyledin?», «onlara bana emrettiğinden başkasını söylemedim», doğrulara doğruluklarının fayda vereceği gün ve her şeyin Allah'ın mülkü oluşu (s6–s10)."
write_out(44, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §40–41 + 4:172–173, 5:116–120", GLOSS_ADD, notes=(), related=())
report(44, S, GLOSS_ADD, ())
