# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 37: «قِصَّةُ عِيسَى» §21 (insistence: the disciples hold to their request — not a test but reassurance, a remembrance for the coming generations) and §22 (the Qurʾān tells the story: al-Māʾida 5:112–115 — the table from heaven); print pp. 53–54.
python3 tools/authoring/author_qisas4_ch37.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: إِلْحَاحٌ وَإِصْرَارٌ، وَالْقُرْآنُ يَحْكِي الْقِصَّةَ (المائدة ١١٢–١١٥)", "en": "The story of ʿĪsā: insistence; the Qurʾān tells the story (5:112–115)", "tr": "Îsâ'nın kıssası: ısrar; Kur'ân kıssayı anlatır (Mâide 112–115)"}
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

# ---------------------------------------------------------------- §21 إِلْحَاحٌ وَإِصْرَارٌ (print pp. 53–54)
sen("s1", "But the disciples clung to their request, and stated that they were in earnest in this request: they did not intend a test; they only wanted reassurance,",
        "Fakat havârîler isteklerine tutundular ve bu istekte ciddi olduklarını, bir imtihan kastetmediklerini, yalnızca gönül rahatlığı istediklerini söylediler;", [
  tok("وَلٰكِنَّ", "lakinna", "part", [AT, IW], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ.", "«but» — lākinna, a sister of inna.", "«fakat» — inne'nin kardeşi lâkinne.", segments=wa_("لٰكِنَّ", "lakinna", "part")),
  tok("الْحَوَارِيِّينَ", "hawari", "noun", [IW, JS], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the disciples» — lākinna's ism, naṣb by the yāʾ.", "«havârîler» — lâkinne'nin ismi, yâ ile mansub."),
  mazi_pl("تَشَبَّثُوا", "tashabbatha", "«clung»", "«tutundular»", tags=[IW, "form-v-verbs"]),
  tok("بِسُؤَالِهِمْ", "sual", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَسُؤَالِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«to their request»", "«isteklerine»", segments=[seg("بِ", "bi", "prep"), seg("سُؤَالِ", "sual", "noun"), seg("هِمْ", "pron-3mp", "pron")], punct="،"),
  mazi_pl("وَذَكَرُوا", "dhakara", "«and stated»", "«ve söylediler»", tags=[AT], wa=True),
  tok("أَنَّهُمْ", "anna", "part", [IW, MB], "أَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالضَّمِيرُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ ذَكَرُوا.", "«that they» — the clause is the object of «stated».", "«… olduklarını» — te'vîl-i masdar «söylediler»in mef'ûlü.", segments=[seg("أَنَّ", "anna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("جَادُّونَ", "jadd-serious", "noun", [IW, JS, "ism-fail", "doubled-verbs"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ فَاعِلٍ مِنَ الْمُضَاعَفِ جَدَّ.", "«in earnest» — anna's khabar; the participle of the doubled jadda.", "«ciddi» — enne'nin haberi; muzâaf cedde'nin ism-i fâili."),
  fi(),
  tok("هٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«this»", "«bu»"),
  tok("السُّؤَالِ", "sual", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«request» — a badal of the demonstrative.", "«istekte» — işaret isminden bedel.", punct="،"),
  la_nafiya(),
  khamsa("يَقْصِدُونَ", "qasada", "«they intend»", "«kastederler»", tags=[HL, "la-nafiya"], extra_ar=" — بَعْدَ لَا النَّافِيَةِ؛ وَالْجُمْلَةُ حَالٌ"),
  maful_("امْتِحَانًا", "imtihan", "«a test»", "«bir imtihan»", tags=["form-viii-verbs"], punct="،"),
  tok("إِنَّمَا", "innama", "part", ["qasr"], "أَدَاةُ حَصْرٍ: إِنَّ الْمَكْفُوفَةُ بِمَا.", "«only» — innamā restricts.", "«ancak» — innemâ hasr edatı."),
  khamsa("يُرِيدُونَ", "arada", "«they want»", "«isterler»", tags=["hollow-verbs", "form-iv-verbs"]),
  maful_("اطْمِئْنَانًا", "itminan", "«reassurance»", "«gönül rahatlığı»", punct="،"),
])
sen("s2", "and that it should be a remembrance for the coming generations and a story told and related down the days, so that it be a proof of the truth of this religion and of the rank of the first believers and the truthful disciples.",
        "ve bunun gelecek nesiller için bir hatıra, günler boyunca anlatılıp rivayet edilen bir kıssa olmasını; böylece bu dinin doğruluğuna, ilk müminlerin ve sâdık havârîlerin mertebesine bir delil olmasını [istediler].", [
  tok("وَلِيَكُونَ", "kana", "verb", [AT, TA, AN, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ لَامُ التَّعْلِيلِ، وَيَكُونَ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى اطْمِئْنَانًا فِي الْمَعْنَى: يُرِيدُونَ اطْمِئْنَانًا وَأَنْ يَكُونَ.", "«and so that … be» — the lām of purpose with a concealed an; joined in sense to «reassurance».", "«ve … olması için» — gizli en ile ta'lil lâmı; mânen «gönül rahatlığı»na ma'tûf.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "lam-taleel", "part"), seg("يَكُونَ", "kana", "verb")]),
  tok("ذٰلِكَ", "dhalika", "pron", [KN, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُونَ.", "«it» — kāna's ism.", "«bu» — kâne'nin ismi."),
  tok("ذِكْرَى", "dhikra", "noun", [KN, "ism-maqsur-manqus"], "خَبَرُ يَكُونَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«a remembrance» — kāna's khabar, a maqṣūr.", "«bir hatıra» — kâne'nin haberi, maksûr."),
  li_noun("لِلْأَجْيَالِ", "jil", "«for the generations»", "«nesiller için»", tags=[JT]),
  naat("الْقَادِمَةِ", "qadim-coming", "«coming»", "«gelecek»", tags=["ism-fail"], punct="،"),
  atf("وَقِصَّةً", "qissa", "«a story»", "«ve bir kıssa»", "nasb", tags=[KN]),
  tok("تُحْكَى", "haka", "verb", [NF, "jumla-sifa", "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ نَعْتٌ لِقِصَّةً.", "«told» — a passive; the clause describes «a story».", "«anlatılan» — meçhul; cümle «kıssa»nın sıfatı."),
  tok("وَتُرْوَى", "rawa", "verb", [AT, NF, "mudari-marfu", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتُرْوَى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and related» — a passive.", "«ve rivayet edilen» — meçhul.", segments=wa_("تُرْوَى", "rawa", "verb")),
  prep("عَلَى", "ala", "«down»", "«boyunca»"),
  majrur("مَرِّ", "marr", "«the passing [of]»", "«geçişi»", tags=[ID, "doubled-verbs"], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — مَصْدَرُ مَرَّ."),
  mudaf_ilayh("الْأَيَّامِ", "yawm", "«the days»", "«günlerin»", tags=[JT], punct="،"),
  tok("فَتَكُونُ", "kana", "verb", [AT, KN, "mudari-marfu", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ (لِلسَّبَبِيَّةِ)، وَتَكُونُ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ.", "«so that it be» — the fāʾ of consequence with kāna.", "«böylece … olur» — sebep fâ'sı ile kâne.", segments=[seg("فَ", "fa", "conj"), seg("تَكُونُ", "kana", "verb")]),
  tok("دَلِيلًا", "dalil-proof", "noun", [KN], "خَبَرُ تَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a proof» — kāna's khabar.", "«bir delil» — kâne'nin haberi."),
  prep("عَلَى", "ala", "«of»", "«-e»"),
  majrur("صِدْقِ", "sidq", "«the truth [of]»", "«doğruluğuna»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("هٰذَا", "hadha", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this»", "«bu»"),
  tok("الدِّينِ", "din", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "«religion» — a badal.", "«dinin» — bedel.", punct="،"),
  atf("وَمَنْزِلَةِ", "manzila", "«the rank [of]»", "«ve mertebesine»", tags=[ID], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  tok("الْمُؤْمِنِينَ", "mumin", "noun", [ID, JS, "ism-fail", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the believers»", "«müminlerin»"),
  js_naat("الْأَوَّلِينَ", "awwal", "«first»", "«ilk»", punct="،"),
  atf("وَالْحَوَارِيِّينَ", "hawari", "«the disciples»", "«ve havârîlerin»", tags=[JS], sign="بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ"),
  js_naat("الصَّادِقِينَ", "sadiq", "«truthful»", "«sâdık»", tags=["ism-fail"], punct="."),
])
# ---------------------------------------------------------------- §22 الْقُرْآنُ يَحْكِي الْقِصَّةَ (print p. 54)
sen("s3", "And let the Qurʾān tell this story:",
        "Bırakın bu kıssayı Kur'ân anlatsın:", [
  tok("وَدَعُوا", "wadaa-let", "verb", [AT, AM, "mithal-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَدَعُوا فِعْلُ أَمْرٍ مِنْ وَدَعَ يَدَعُ (أُمِيتَ مَاضِيهِ فِي الْفَصِيحِ)، مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مِثَالٌ حُذِفَتْ فَاؤُهُ فِي الْأَمْرِ وَالْمُضَارِعِ.", "«and let» — the imperative of wadaʿa (its māḍī disused in classical usage); the initial wāw dropped.", "«ve bırakın» — vedea'nın emri (mâzîsi fasih kullanımda terk edilmiş); baştaki vâv düşmüş.", segments=wa_("دَعُوا", "wadaa-let", "verb")),
  maful_("الْقُرْآنَ", "quran", "«the Qurʾān»", "«Kur'ân'ı»"),
  tok("يَحْكِي", "haka", "verb", [HL, "mudari-marfu", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ حَالٌ (أَوْ مَفْعُولٌ ثَانٍ عَلَى تَضْمِينِ دَعْ مَعْنَى اتْرُكْ).", "«tell» — a ḥāl clause, or the second object of «let».", "«anlatsın» — hâl cümlesi, yahut «bırak»ın ikinci mef'ûlü."),
  tok("هٰذِهِ", "hadhihi", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this» — the object.", "«bu» — mef'ûl."),
  tok("الْقِصَّةَ", "qissa", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«story» — a badal.", "«kıssayı» — bedel.", punct=":"),
])
sen("s4", "«When the disciples said: O ʿĪsā son of Maryam, can your Lord send down to us a table from heaven? He said: Fear God, if you are believers.» (5:112)",
        "«Hani havârîler demişti: Ey Meryem oğlu Îsâ! Rabbin bize gökten bir sofra indirebilir mi? Dedi: Eğer inananlar iseniz Allah'tan sakının.» (5:112)", [
  *quran([
  tok("إِذْ", "idh", "noun", [MF, "hadhf-wa-taqdir"], "ظَرْفٌ لِمَا مَضَى مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ: اذْكُرْ.", "«when» — the object of an understood «remember».", "«hani» — mukadder «hatırla»nın mef'ûlü."),
  mazi("قَالَ", "qala", "«said»", "«demişti»", tags=[ID, "hollow-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ"),
  tok("الْحَوَارِيُّونَ", "hawari", "noun", [FL, JS], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the disciples» — the doer.", "«havârîler» — fâil."),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("عِيسَى", "isa", "propn", ["vocative-munada", MM, "ism-maqsur-manqus"], "مُنَادًى مُفْرَدٌ عَلَمٌ: يَجُوزُ بِنَاؤُهُ عَلَى ضَمٍّ مُقَدَّرٍ، أَوْ نَصْبُهُ لِوَصْفِهِ بِابْنٍ الْمُضَافِ إِلَى عَلَمٍ — وَالْأَلِفُ تَحْتَمِلُ الْوَجْهَيْنِ.", "«ʿĪsā» — a proper-name munādā: built on a hidden ḍamma, or in naṣb since «son of Maryam» qualifies it; the alif hides either.", "«Îsâ» — alem münâdâ: gizli damme üzere mebnî, yahut «Meryem oğlu» sıfatı sebebiyle mansub; elif ikisini de gizler."),
  tok("ابْنَ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَنَصْبُهُ وَاجِبٌ لِأَنَّهُ مُضَافٌ.", "«son [of]» — a naʿt in naṣb, necessarily, being annexed.", "«oğlu» — mansub sıfat; muzâf olduğu için nasbı vâcip."),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»"),
  tok("هَلْ", "hal-istifham", "part", [IS], "حَرْفُ اسْتِفْهَامٍ.", "«can»", "«… mi»"),
  mudari("يَسْتَطِيعُ", "istataa", "«is able»", "«gücü yeter»", tags=["hollow-verbs", "form-x-verbs"], hidden=None),
  noun_pron("رَبُّكَ", "rabb", "رَبُّ", "كَ", "pron-2ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your Lord» — the doer.", "«Rabbin» — fâil.", tags=[FL, ID]),
  an_nasb("مَفْعُولٌ بِهِ لِيَسْتَطِيعُ", "«to»", "«-mesine»"),
  mansub("يُنَزِّلَ", "nazzala", "«send down»", "«indirmeye»", tags=["form-ii-verbs"]),
  prep_pron("عَلَيْنَا", "ala", "نَا", "pron-1p", "«to us»", "«bize»"),
  *maida_min_sama(),
  mazi("قَالَ", "qala", "«he said»", "«dedi»", tags=["hollow-verbs"], hidden="هُوَ"),
  tok("اتَّقُوا", "ittaqa", "verb", [AM, "naqis-verbs", "form-viii-verbs"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — حُذِفَتْ لَامُهُ قَبْلَ وَاوِ الْجَمَاعَةِ.", "«fear» — an imperative on the group's wāw.", "«sakının» — cemi vâvlı emir."),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«God»", "«Allah'tan»"),
  tok("إِنْ", "in-shartiyya", "part", [SH], "حَرْفُ شَرْطٍ جَازِمٌ.", "«if»", "«eğer»"),
  tok("كُنْتُمْ", "kana", "verb", [SH, KN, "hollow-verbs", "hadhf-wa-taqdir"], "فِعْلٌ مَاضٍ نَاقِصٌ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ اسْمُهُ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.", "«you are» — the condition; its answer is understood.", "«iseniz» — şart; cevabı mahzuf.", segments=[seg("كُنْ", "kana", "verb"), seg("تُمْ", "pron-2mp", "pron")]),
  tok("مُؤْمِنِينَ", "mumin", "noun", [KN, JS, "ism-fail", "form-iv-verbs"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«believers»", "«inananlar»", punct=AYA),
  ]),
])
sen("s5", "«They said: We wish to eat from it, and that our hearts be reassured, and that we know that you have told us the truth, and that we be witnesses to it.» (5:113)",
        "«Dediler: Ondan yemek, kalplerimizin yatışmasını, bize doğru söylediğini bilmeyi ve ona şahit olanlardan olmayı istiyoruz.» (5:113)", [
  *quran([
  mazi_pl("قَالُوا", "qala", "«they said»", "«dediler»", tags=["hollow-verbs"]),
  mudari("نُرِيدُ", "arada", "«we wish»", "«istiyoruz»", tags=["hollow-verbs", "form-iv-verbs"], hidden="نَحْنُ"),
  an_nasb("مَفْعُولٌ بِهِ لِنُرِيدُ", "«to»", "«-meyi»"),
  mansub("نَأْكُلَ", "akala", "«eat»", "«yemeyi»", hidden="نَحْنُ"),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«from it»", "«ondan»"),
  tok("وَتَطْمَئِنَّ", "itmaanna", "verb", [AT, AN, "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَطْمَئِنَّ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى نَأْكُلَ — مِنَ الرُّبَاعِيِّ الْمَزِيدِ (اطْمَأَنَّ عَلَى افْعَلَلَّ)، مُضَاعَفُ الْآخِرِ.", "«and that … be reassured» — naṣb by conjunction; a doubled quadriliteral (ifʿalalla).", "«ve … yatışmasını» — atıfla mansub; sonu muzâaf rubâî (if'alelle).", segments=wa_("تَطْمَئِنَّ", "itmaanna", "verb")),
  noun_pron("قُلُوبُنَا", "qalb", "قُلُوبُ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our hearts» — the doer.", "«kalplerimiz» — fâil.", tags=[FL, ID, JT]),
  tok("وَنَعْلَمَ", "alima", "verb", [AT, AN], "الْوَاوُ عَاطِفَةٌ، وَنَعْلَمَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ، وَالْفَاعِلُ مُسْتَتِرٌ: نَحْنُ.", "«and that we know»", "«ve bilmeyi»", segments=wa_("نَعْلَمَ", "alima", "verb")),
  tok("أَنْ", "an-mukhaffafa", "part", [IW, "hadhf-wa-taqdir"], "أَنْ مُخَفَّفَةٌ مِنَ الثَّقِيلَةِ، وَاسْمُهَا ضَمِيرُ الشَّأْنِ مَحْذُوفٌ، وَفُصِلَ بَيْنَهَا وَبَيْنَ الْفِعْلِ بِقَدْ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ نَعْلَمَ.", "«that» — the lightened an, its ism the pronoun of the matter; qad separates it from the verb.", "«… -diğini» — muhaffef en; ismi zamîr-i şe'n; kad fiilden ayırır."),
  tok("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "«[indeed]»", "«[gerçekten]»"),
  tok("صَدَقْتَنَا", "sadaqa-be-true", "verb", [IW, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ، وَنَا مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ أَنْ.", "«you have told us the truth» — the tāʾ the doer, nā the object; an's khabar.", "«bize doğru söyledin» — tâ fâil, nâ mef'ûl; en'in haberi.", segments=[seg("صَدَقْ", "sadaqa-be-true", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نَا", "pron-1p", "pron")]),
  tok("وَنَكُونَ", "kana", "verb", [AT, AN, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَنَكُونَ فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِالْعَطْفِ، وَاسْمُهُ مُسْتَتِرٌ: نَحْنُ.", "«and that we be»", "«ve olmayı»", segments=wa_("نَكُونَ", "kana", "verb")),
  prep_pron("عَلَيْهَا", "ala", "هَا", "pron-3fs", "«to it» — attached to «witnesses».", "«ona» — «şahitler»e bağlı.", extra_ar=" — مُتَعَلِّقٌ بِالشَّاهِدِينَ"),
  tok("مِنَ", "min", "prep", [HJ, KN], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ نَكُونَ.", "«of» — the phrase is kāna's khabar.", "«-den» — ibare kâne'nin haberi."),
  tok("الشَّاهِدِينَ", "shahid", "noun", [HJ, JS, "ism-fail"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the witnesses»", "«şahitler»", punct=AYA),
  ]),
])
sen("s6", "«ʿĪsā son of Maryam said: O God, our Lord, send down to us a table from heaven, to be a feast for the first of us and the last of us, and a sign from You; and provide for us, for You are the best of providers.» (5:114)",
        "«Meryem oğlu Îsâ dedi: Allah'ım, Rabbimiz! Bize gökten bir sofra indir ki ilkimiz ve sonumuz için bir bayram ve senden bir âyet olsun; bizi rızıklandır, sen rızık verenlerin en hayırlısısın.» (5:114)", [
  *quran([
  mazi("قَالَ", "qala", "«said»", "«dedi»", tags=["hollow-verbs"], hidden=None),
  tok("عِيسَى", "isa", "propn", [FL, MM, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā» — the doer.", "«Îsâ» — fâil."),
  tok("ابْنُ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«son [of]»", "«oğlu»"),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»"),
  tok("اللّٰهُمَّ", "allahumma", "propn", ["vocative-munada"], "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَالْمِيمُ الْمُشَدَّدَةُ عِوَضٌ عَنْ يَا النِّدَاءِ الْمَحْذُوفَةِ.", "«O God» — a munādā built on ḍamma; the doubled mīm replaces the dropped yā.", "«Allah'ım» — damme üzere mebnî münâdâ; şeddeli mîm düşen yâ'nın yerine."),
  tok("رَبَّنَا", "rabb", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ، أَوْ مُنَادًى ثَانٍ) مَنْصُوبٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — يُنْصَبُ تَابِعُ الْمُنَادَى الْمَبْنِيِّ إِذَا كَانَ مُضَافًا.", "«our Lord» — an annexed follower of the munādā, hence in naṣb.", "«Rabbimiz» — mebnî münâdânın muzâf tâbii, bu yüzden mansub.", segments=[seg("رَبَّ", "rabb", "noun"), seg("نَا", "pron-1p", "pron")]),
  tok("أَنْزِلْ", "anzala", "verb", [AM, "form-iv-verbs"], "فِعْلُ أَمْرٍ (دُعَاءٌ) مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«send down» — an imperative of supplication.", "«indir» — duâ emri."),
  prep_pron("عَلَيْنَا", "ala", "نَا", "pron-1p", "«to us»", "«bize»"),
  *maida_min_sama(),
  tok("تَكُونُ", "kana", "verb", [KN, "jumla-sifa", "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ نَعْتٌ لِمَائِدَةً (وَقُرِئَ بِالْجَزْمِ جَوَابًا لِلطَّلَبِ).", "«to be» — a ṣifa clause of «a table» (also read in jazm as the answer to the request).", "«ki … olsun» — «sofra»nın sıfat cümlesi (talebin cevabı olarak cezimle de okunmuştur)."),
  li_pron("لَنَا", "نَا", "pron-1p", "«for us»", "«bizim için»"),
  tok("عِيدًا", "id", "noun", [KN], "خَبَرُ تَكُونُ مَنْصُوبٌ بِالْفَتْحَةِ.", "«a feast» — kāna's khabar.", "«bir bayram» — kâne'nin haberi."),
  tok("لِأَوَّلِنَا", "awwal", "noun", [HJ, ID, BD], "اللَّامُ حَرْفُ جَرٍّ، وَأَوَّلِ مَجْرُورٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — بَدَلٌ مِنْ لَنَا بِإِعَادَةِ الْجَارِّ.", "«for the first of us» — a badal of «for us», the preposition repeated.", "«ilkimiz için» — câr tekrarıyla «bizim için»den bedel.", segments=[seg("لِ", "li", "prep"), seg("أَوَّلِ", "awwal", "noun"), seg("نَا", "pron-1p", "pron")]),
  pron_atf("وَآخِرِنَا", "akhir", "آخِرِ", "نَا", "pron-1p", "«the last of us»", "«ve sonumuz»"),
  atf("وَآيَةً", "aya", "«a sign»", "«ve bir âyet»", "nasb", tags=[KN]),
  prep_pron("مِنْكَ", "min", "كَ", "pron-2ms", "«from You» — a ṣifa of «a sign».", "«senden» — «âyet»in sıfatı.", tags=[NA], extra_ar=" — صِفَةٌ لِآيَةً"),
  tok("وَارْزُقْنَا", "razaqa", "verb", [AT, AM, MB], "الْوَاوُ عَاطِفَةٌ، وَارْزُقْ فِعْلُ أَمْرٍ (دُعَاءٌ) مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ، وَنَا مَفْعُولٌ بِهِ.", "«and provide for us» — nā the object.", "«ve bizi rızıklandır» — nâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("ارْزُقْ", "razaqa", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("وَأَنْتَ", "anta", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ (أَوْ لِلِاسْتِئْنَافِ)، وَأَنْتَ ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.", "«for You» — the mubtadaʾ of a ḥāl clause.", "«sen» — hâl cümlesinin mübtedâsı.", segments=wa_("أَنْتَ", "anta", "pron")),
  tok("خَيْرُ", "khayr", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "«the best [of]» — the khabar.", "«en hayırlısı» — haber."),
  tok("الرَّازِقِينَ", "raziq", "noun", [ID, JS, "ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«providers»", "«rızık verenlerin»", punct=AYA),
  ]),
])
sen("s7", "«God said: I shall send it down to you; then whoever of you disbelieves afterwards, I shall punish him with a punishment with which I punish no one else in the worlds.» (5:115)",
        "«Allah dedi: Onu size indireceğim; ama bundan sonra sizden kim inkâr ederse, ona âlemlerde hiç kimseye etmediğim bir azapla azap ederim.» (5:115)", [
  *quran([
  mazi("قَالَ", "qala", "«said»", "«dedi»", tags=["hollow-verbs"], hidden=None),
  allah_fail(),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I»", "«şüphesiz ben»", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("مُنَزِّلُهَا", "munazzil", "noun", [IW, ID, "ism-fail", "form-ii-verbs"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ إِلَى الضَّمِيرِ (إِضَافَةٌ لَفْظِيَّةٌ: اسْمُ الْفَاعِلِ إِلَى مَفْعُولِهِ).", "«the One sending it down» — inna's khabar; a participle annexed to its object.", "«onu indirecek olan» — inne'nin haberi; mef'ûlüne muzâf ism-i fâil.", segments=[seg("مُنَزِّلُ", "munazzil", "noun"), seg("هَا", "pron-3fs", "pron")]),
  prep_pron("عَلَيْكُمْ", "ala", "كُمْ", "pron-2mp", "«to you»", "«size»"),
  tok("فَمَنْ", "man-shartiyya", "pron", [AT, SH, MK], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«then whoever» — the jussive conditional noun as mubtadaʾ.", "«ama kim» — mübtedâ olan cezm edici şart ismi.", segments=[seg("فَ", "fa", "conj"), seg("مَنْ", "man-shartiyya", "pron")]),
  tok("يَكْفُرْ", "kafara", "verb", [SH], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«disbelieves» — the condition's verb, in jazm.", "«inkâr ederse» — meczûm şart fiili."),
  tok("بَعْدُ", "badu-after", "noun", [MF], "ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ لَفْظًا لَا مَعْنًى، فِي مَحَلِّ نَصْبٍ.", "«afterwards» — the ẓarf built on ḍamma, cut off from its annexation.", "«bundan sonra» — izâfetten lafzan kesildiği için damme üzere mebnî zarf."),
  prep_pron("مِنْكُمْ", "min", "كُمْ", "pron-2mp", "«of you»", "«sizden»"),
  tok("فَإِنِّي", "inna", "part", [SH, IW], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَإِنَّ وَالْيَاءُ اسْمُهَا — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "«then I» — the fāʾ of the answer with inna.", "«ben» — cevap fâ'sı ile inne.", segments=[seg("فَ", "fa", "conj"), seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أُعَذِّبُهُ", "adhdhaba", "verb", [IW, MB, "mudari-marfu", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنَا، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I shall punish him» — inna's khabar.", "«ona azap ederim» — inne'nin haberi.", segments=[seg("أُعَذِّبُ", "adhdhaba", "verb"), seg("هُ", "pron-3ms", "pron")]),
  tok("عَذَابًا", "adhab", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«with a punishment» — an absolute object.", "«bir azapla» — mef'ûl-i mutlak."),
  la_nafiya(),
  tok("أُعَذِّبُهُ", "adhdhaba", "verb", ["la-nafiya", "jumla-sifa", "mudari-marfu", "form-ii-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بَعْدَ لَا النَّافِيَةِ، وَالْفَاعِلُ: أَنَا، وَالْهَاءُ نَائِبٌ عَنِ الْمَصْدَرِ (أَيْ: لَا أُعَذِّبُ مِثْلَهُ) — وَالْجُمْلَةُ نَعْتٌ لِعَذَابًا.", "«with which I punish» — the clause describes the punishment; the pronoun stands for the maṣdar.", "«… etmediğim» — cümle azabın sıfatı; zamir masdarın yerini tutar.", segments=[seg("أُعَذِّبُ", "adhdhaba", "verb"), seg("هُ", "pron-3ms", "pron")]),
  maful_("أَحَدًا", "ahad", "«anyone»", "«hiç kimseye»"),
  tok("مِنَ", "min", "prep", [HJ, NA], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ — صِفَةٌ لِأَحَدًا.", "«of»", "«-den»"),
  tok("الْعَالَمِينَ", "alam", "noun", [HJ, JS], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«the worlds»", "«âlemler»", punct=AYA),
  ]),
])

CAND = {
 "lakinna": G("lakinna", "لَكِنَّ", None, "part", "but (a sister of inna)", "fakat (inne'nin kardeşi)", 1),
 "hawari": G("hawari", "حَوَارِيّ", "ح و ر", "noun", "a disciple (of ʿĪsā)", "havârî", 2, plural="حَوَارِيُّونَ"),
 "tashabbatha": G("tashabbatha", "تَشَبَّثَ", "ش ب ث", "verb", "to cling (bi: to) (Form V)", "tutunmak, sarılmak (tefa''ul)", 3),
 "sual": G("sual", "سُؤَال", "س أ ل", "noun", "a question, a request", "soru, istek", 1, plural="أَسْئِلَة"),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "dhakara": G("dhakara", "ذَكَرَ", "ذ ك ر", "verb", "to mention, to state; to remember", "zikretmek, söylemek; hatırlamak", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that (a sister of inna)", "… -dığı (inne'nin kardeşi)", 1),
 "jadd-serious": G("jadd-serious", "جَادّ", "ج د د", "noun", "in earnest, serious (an active participle of the doubled jadda)", "ciddi (muzâaf cedde'nin ism-i fâili)", 2),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "qasada": G("qasada", "قَصَدَ", "ق ص د", "verb", "to intend, to aim at", "kastetmek, amaçlamak", 1),
 "imtihan": G("imtihan", "اِمْتِحَان", "م ح ن", "noun", "a test, a trial (the maṣdar of Form VIII)", "imtihan, sınama (iftiâl masdarı)", 1),
 "innama": G("innama", "إِنَّمَا", None, "part", "only (inna + the restraining mā)", "ancak, yalnızca (inne + kâffe mâ)", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to intend (Form IV, hollow)", "istemek (if'âl, ecvef)", 1),
 "itminan": G("itminan", "اِطْمِئْنَان", "ط م أ ن", "noun", "reassurance, tranquillity (the maṣdar of iṭmaʾanna)", "gönül rahatlığı, itmi'nân (itma'enne'nin masdarı)", 2),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "lam-taleel": G("lam-taleel", "لِ (التَّعْلِيل)", None, "part", "the lām of purpose (with a concealed an)", "ta'lil lâmı (gizli en ile)", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "dhikra": G("dhikra", "ذِكْرَى", "ذ ك ر", "noun", "a remembrance, a reminder (a maqṣūr noun)", "hatıra, hatırlatma (maksûr isim)", 2),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "jil": G("jil", "جِيل", "ج ي ل", "noun", "a generation", "nesil, kuşak", 1, plural="أَجْيَال"),
 "qadim-coming": G("qadim-coming", "قَادِم", "ق د م", "noun", "coming, next (an active participle)", "gelecek, gelen (ism-i fâil)", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa, hikâye", 1, plural="قِصَص"),
 "haka": G("haka", "حَكَى", "ح ك ي", "verb", "to tell, to relate (defective)", "anlatmak, hikâye etmek (nâkıs)", 1),
 "rawa": G("rawa", "رَوَى", "ر و ي", "verb", "to relate, to transmit (defective)", "rivayet etmek, nakletmek (nâkıs)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "marr": G("marr", "مَرّ", "م ر ر", "noun", "the passing (of time)", "geçiş, geçme", 2),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "dalil-proof": G("dalil-proof", "دَلِيل", "د ل ل", "noun", "a proof, an evidence", "delil", 1, plural="أَدِلَّة / دَلَائِل"),
 "sidq": G("sidq", "صِدْق", "ص د ق", "noun", "truth, truthfulness", "doğruluk, sıdk", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "manzila": G("manzila", "مَنْزِلَة", "ن ز ل", "noun", "a rank, a station", "mertebe, derece", 1),
 "mumin": G("mumin", "مُؤْمِن", "أ م ن", "noun", "a believer (an active participle of Form IV)", "mümin (if'âl ism-i fâili)", 1, plural="مُؤْمِنُونَ"),
 "awwal": G("awwal", "أَوَّل", "أ و ل", "noun", "first", "ilk, birinci", 1, plural="أَوَّلُونَ"),
 "sadiq": G("sadiq", "صَادِق", "ص د ق", "noun", "truthful (an active participle)", "sâdık, doğru sözlü (ism-i fâil)", 1),
 "wadaa-let": G("wadaa-let", "وَدَعَ", "و د ع", "verb", "to let, to leave (its māḍī disused; the imperative daʿ and muḍāriʿ yadaʿu live)", "bırakmak (mâzîsi kullanılmaz; emir da' ve muzari yedeu yaşar)", 2),
 "quran": G("quran", "الْقُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu (müennes)", 1),
 "idh": G("idh", "إِذْ", None, "noun", "when (of the past)", "hani, -dığı zaman", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "ya-nida": G("ya-nida", "يَا", None, "part", "O (the vocative particle)", "ey (nidâ harfi)", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "ibn": G("ibn", "ابْن", "ب ن ي", "noun", "a son", "oğul", 1, plural="أَبْنَاء"),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "hal-istifham": G("hal-istifham", "هَلْ", None, "part", "is it that…? (the interrogative particle)", "… mi? (istifhâm harfi)", 1),
 "istataa": G("istataa", "اِسْتَطَاعَ", "ط و ع", "verb", "to be able (Form X, hollow)", "güç yetirmek, yapabilmek (istif'âl, ecvef)", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (m. sg.)", "seni / senin", 1),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "nazzala": G("nazzala", "نَزَّلَ", "ن ز ل", "verb", "to send down (Form II)", "indirmek (tef'îl)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "maida": G("maida", "مَائِدَة", "م ي د", "noun", "a table (spread with food)", "sofra", 1, plural="مَوَائِد"),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "a heaven, the sky", "gök", 1, plural="سَمَاوَات"),
 "ittaqa": G("ittaqa", "اِتَّقَى", "و ق ي", "verb", "to fear (God), to be wary of (Form VIII, defective)", "sakınmak (iftiâl, nâkıs)", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "in-shartiyya": G("in-shartiyya", "إِنْ", None, "part", "if (the jussive conditional)", "eğer (cezm eden şart harfi)", 1),
 "pron-2mp": G("pron-2mp", "ـكُمْ", None, "pron", "you / your (pl.)", "siz / sizi / sizin", 1),
 "akala": G("akala", "أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "itmaanna": G("itmaanna", "اِطْمَأَنَّ", "ط م أ ن", "verb", "to be reassured, to be at rest (a doubled quadriliteral, ifʿalalla)", "yatışmak, huzur bulmak (rubâî, if'alelle)", 2),
 "qalb": G("qalb", "قَلْب", "ق ل ب", "noun", "a heart", "kalp", 1, plural="قُلُوب"),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know, to learn", "bilmek", 1),
 "an-mukhaffafa": G("an-mukhaffafa", "أَنْ (الْمُخَفَّفَة)", None, "part", "that — the lightened an (from anna)", "… -dığı — muhaffef en (enne'den)", 2),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "sadaqa-be-true": G("sadaqa-be-true", "صَدَقَ", "ص د ق", "verb", "to speak the truth; to prove true", "doğru söylemek; doğru çıkmak", 1),
 "shahid": G("shahid", "شَاهِد", "ش ه د", "noun", "a witness (an active participle)", "şahit (ism-i fâil)", 1, plural="شُهُود"),
 "allahumma": G("allahumma", "اللّٰهُمَّ", "أ ل ه", "propn", "O God (the vocative with the mīm of compensation)", "Allah'ım (telâfi mîmli nidâ)", 1),
 "anzala": G("anzala", "أَنْزَلَ", "ن ز ل", "verb", "to send down (Form IV)", "indirmek (if'âl)", 1),
 "id": G("id", "عِيد", "ع و د", "noun", "a feast, a festival", "bayram", 1, plural="أَعْيَاد"),
 "akhir": G("akhir", "آخِر", "أ خ ر", "noun", "the last", "son, sonuncu", 1),
 "aya": G("aya", "آيَة", "أ ي ي", "noun", "a sign; a verse", "âyet, işaret", 1, plural="آيَات"),
 "razaqa": G("razaqa", "رَزَقَ", "ر ز ق", "verb", "to provide for", "rızık vermek", 1),
 "anta": G("anta", "أَنْتَ", None, "pron", "you (m. sg.)", "sen", 1),
 "khayr": G("khayr", "خَيْر", "خ ي ر", "noun", "good; better, best", "hayır; daha hayırlı", 1),
 "raziq": G("raziq", "رَازِق", "ر ز ق", "noun", "a provider (an active participle)", "rızık veren (ism-i fâil)", 2),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "pron-1s": G("pron-1s", "ـي", None, "pron", "I / me / my", "ben / beni / benim", 1),
 "munazzil": G("munazzil", "مُنَزِّل", "ن ز ل", "noun", "one who sends down (an active participle of Form II)", "indiren (tef'îl ism-i fâili)", 2),
 "man-shartiyya": G("man-shartiyya", "مَنْ (الشَّرْطِيَّة)", None, "pron", "whoever (the conditional man)", "kim … -se (şart ismi)", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve", "inkâr etmek, küfretmek", 1),
 "badu-after": G("badu-after", "بَعْدُ", "ب ع د", "noun", "afterwards (the ẓarf cut off from annexation)", "sonra (izâfetten kesilmiş zarf)", 1),
 "adhdhaba": G("adhdhaba", "عَذَّبَ", "ع ذ ب", "verb", "to punish, to torment (Form II)", "azap etmek (tef'îl)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment, torment", "azap", 1),
 "ahad": G("ahad", "أَحَد", "أ ح د", "noun", "one; anyone", "bir; hiç kimse", 1),
 "alam": G("alam", "عَالَم", "ع ل م", "noun", "a world", "âlem", 1, plural="عَالَمُونَ / عَوَالِم"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tashabbatha", _sg.derived(_sg.B5, _sg.W5, "َ", "تَشَبَّث", "تَشَبَّث", "تَشَبَّث", "تَشَبُّث", "مُتَشَبِّث", None, None, None, "تَشَبَّثَ بِالشَّيْءِ: تَعَلَّقَ بِهِ وَلَزِمَهُ."))
put_morph(mo, "wadaa-let", _sg.sound1("fataha", "وَدَع", "دَع", "دَع", "وَدْع", "وَادِع", "مَوْدُوع", "وُدِعَ", "يُودَعُ", "وَدَعَ الشَّيْءَ: تَرَكَهُ — مِثَالٌ وَاوِيٌّ، أُمِيتَ مَاضِيهِ وَمَصْدَرُهُ وَاسْمُ فَاعِلِهِ فِي الْفَصِيحِ وَاسْتُغْنِيَ بِتَرَكَ؛ يَبْقَى: يَدَعُ، دَعْ؛ وَالْجَدْوَلُ مَاضِيهِ لِلْقِيَاسِ.", cls="مِثَالٌ وَاوِيٌّ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch37 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 37 (print pp. 53–54; ʿĪsā §21–22): the disciples hold to their request — not a test but reassurance, a remembrance for the generations (s1–s2); «let the Qurʾān tell it» (s3); al-Māʾida 5:112 the question and «fear God» (s4), 5:113 the four wishes (s5), 5:114 the prayer «O God, our Lord, send down to us a table» (s6), 5:115 «I shall send it down… whoever disbelieves afterwards» (s7)."
ADD_TR = " Otuz yedinci bölüm (baskı s. 53–54; Îsâ §21–22): havârîler isteklerinde ısrar eder — imtihan değil gönül rahatlığı, nesiller için hatıra (s1–s2); «bırakın Kur'ân anlatsın» (s3); Mâide 112 soru ve «Allah'tan sakının» (s4), 113 dört dilek (s5), 114 «Allah'ım, Rabbimiz, bize sofra indir» duâsı (s6), 115 «onu indireceğim… kim bundan sonra inkâr ederse» (s7)."
write_out(37, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §21–22 + 5:112–115", GLOSS_ADD, notes=(), related=())
report(37, S, GLOSS_ADD, ())
