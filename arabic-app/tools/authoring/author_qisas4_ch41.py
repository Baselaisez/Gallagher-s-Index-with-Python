# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 41: «قِصَّةُ عِيسَى» §33 (ʿĪsā raised to heaven), §34 (the Qurʾān speaks of the story: al-Nisāʾ 4:156–158 — «they did not kill him nor crucify him, but it was made to appear so to them… God raised him to Himself»; his whole matter a wonder), §35 (his descent at the end of time, with 4:159); print pp. 60–62.
python3 tools/authoring/author_qisas4_ch41.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: رَفْعُ عِيسَى إِلَى السَّمَاءِ، وَنُزُولُهُ عِنْدَ الْقِيَامَةِ (النساء ١٥٦–١٥٩)", "en": "The story of ʿĪsā: raised to heaven; his descent at the end of time (4:156–159)", "tr": "Îsâ'nın kıssası: Îsâ'nın göğe kaldırılması; kıyamete yakın inişi (Nisâ 156–159)"}
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
    """«وَلَا يَفْعَلُ» as TWO tokens: the joined negating lā, then the muḍāriʿ (wave 32: a token is one printed word)."""
    verb = full.split()[-1]
    return [tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and … not» — the negating lā, joined.", "«ve … -mez» — ma'tûf nefiy lâ'sı.", segments=wa_("لَا", "la-nafiya", "part")),
            tok(verb, lex, "verb", ["la-nafiya", "mudari-marfu"] + list(tags), verb + " فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ: " + hidden + extra + ".", en, tr, punct=punct)]

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
    """«وَمَا قَتَلُوهُ» as TWO tokens: the joined negating mā, then the māḍī with its object pronoun (wave 32)."""
    verb = full.split()[-1]; stem = verb[:len(verb) - 2]
    return [tok("وَمَا", "ma-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "«and … not» — the negating mā, joined.", "«ve … -medi» — ma'tûf nefiy mâ'sı.", segments=wa_("مَا", "ma-nafiya", "part")),
            tok(verb, lex, "verb", [MB, "la-nafiya"], stem + "ا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«they did not» + " + en, "«onu» + " + tr, punct=punct, segments=[seg(stem, lex, "verb"), seg("هُ", "pron-3ms", "pron")])]

# ---------------------------------------------------------------- §33 رَفْعُ عِيسَى إِلَى السَّمَاءِ (print p. 60)
sen("s1", "As for our master ʿĪsā son of Maryam, God Most High saved him from the Jews' plot and raised him to Himself, honoured and purified from those who disbelieved.",
        "Efendimiz Meryem oğlu Îsâ'ya gelince, Allah Teâlâ onu Yahudilerin tuzağından kurtardı ve onu, inkâr edenlerden arındırılmış ve şereflendirilmiş olarak katına yükseltti.", [
  tok("أَمَّا", "amma", "part", ["amma-tafsiliyya", SH], "حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«as for»", "«-e gelince»"),
  noun_pron("سَيِّدُنَا", "sayyid", "سَيِّدُ", "نَا", "pron-1p", "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our master» — the mubtadaʾ.", "«efendimiz» — mübtedâ.", tags=[MK, ID]),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.", "«ʿĪsā»", "«Îsâ»"),
  tok("ابْنُ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَرْفُوعٌ، مُضَافٌ.", "«son [of]»", "«oğlu»"),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»"),
  tok("فَقَدْ", "qad", "part", [SH, "qad-harf"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«[indeed]» — the fāʾ of ammā's answer.", "«[gerçekten]» — emmâ'nın cevap fâ'sı.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  tok("نَجَّاهُ", "najja", "verb", [MK, MB, "naqis-verbs", "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.", "«saved him» — a defective Form II; the khabar clause.", "«onu kurtardı» — nâkıs tef'îl; haber cümlesi.", segments=[seg("نَجَّا", "najja", "verb"), seg("هُ", "pron-3ms", "pron")]),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("كَيْدِ", "kayd", "«the plot [of]»", "«tuzağından»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudilerin»"),
  v_pron("وَرَفَعَهُ", "rafaa", "رَفَعَ", "هُ", "pron-3ms", "«and raised him»", "«ve onu yükseltti»", wa=True),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Himself»", "«katına»"),
  hal("مُكَرَّمًا", "mukarram", "«honoured»", "«şereflendirilmiş olarak»", tags=["ism-maful", "form-ii-verbs"]),
  hal("مُطَهَّرًا", "mutahhar", "«purified»", "«arındırılmış olarak»", tags=["ism-maful", "form-ii-verbs"], ar="حَالٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  alladhina("jarr", "مَجْرُورٌ بِمِنْ", "«those who»", "«… -enlerden»", tags=[HJ]),
  kafaru(role=" — صِلَةٌ", en="«disbelieved» — the ṣila.", tr="«inkâr ettiler» — sıla."),
])
# ---------------------------------------------------------------- §34 الْقُرْآنُ يَتَحَدَّثُ عَنِ الْقِصَّةِ (print pp. 60–61)
sen("s2", "And that is His word, Most High, when He speaks of the Jews:",
        "Bu, Allah Teâlâ'nın Yahudilerden söz ederken buyurduğu şu sözdür:", [
  tok("وَذٰلِكَ", "dhalika", "pron", [AT, MK, "asma-al-ishara"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and that» — the mubtadaʾ.", "«ve bu» — mübtedâ.", segments=wa_("ذٰلِكَ", "dhalika", "pron")),
  noun_pron("قَوْلُهُ", "qawl", "قَوْلُ", "هُ", "pron-3ms", "خَبَرٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His word» — the khabar.", "«O'nun sözü» — haber.", tags=[MK, ID]),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»"),
  tok("وَهُوَ", "huwa", "pron", [HL, MK], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ.", "«when He» — a ḥāl clause.", "«O … iken» — hâl cümlesi.", segments=wa_("هُوَ", "huwa", "pron")),
  mudari("يَتَحَدَّثُ", "tahaddatha", "«speaks»", "«söz eder»", tags=[MK, "form-v-verbs"], extra_ar=" — وَالْجُمْلَةُ خَبَرٌ"),
  tok("عَنِ", "an", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«of»", "«-den»"),
  majrur("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudiler»", punct=":"),
])
sen("s3", "«…and for their unbelief, and their uttering against Maryam a tremendous calumny, and their saying: We killed the Messiah, ʿĪsā son of Maryam, the Messenger of God — though they did not kill him nor crucify him, but it was made to appear so to them;» (4:156–157)",
        "«…küfürleri, Meryem'e büyük bir iftira söylemeleri ve «Allah'ın resulü Meryem oğlu Îsâ Mesîh'i biz öldürdük» demeleri yüzünden — hâlbuki onu öldürmediler ve asmadılar; fakat onlara öyle gösterildi;» (4:156–157)", [
  *quran([
  tok("وَبِكُفْرِهِمْ", "kufr", "noun", [AT, HJ, ID, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَكُفْرِ مَجْرُورٌ، مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — مَعْطُوفٌ عَلَى «فَبِمَا نَقْضِهِمْ» فِي الْآيَةِ قَبْلَهَا، وَمُتَعَلِّقُ الْبَاءِ مَحْذُوفٌ: لَعَنَّاهُمْ.", "«and for their unbelief» — the causal bāʾ, joined to the previous verse's «for their breaking»; its governing verb is understood (We cursed them).", "«ve küfürleri yüzünden» — sebep bâ'sı; önceki âyetteki «ahdi bozmaları yüzünden»e ma'tûf; müteallakı mahzuf.", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("كُفْرِ", "kufr", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  pron_atf("وَقَوْلِهِمْ", "qawl", "قَوْلِ", "هِمْ", "pron-3mp", "«their uttering»", "«ve söylemeleri»"),
  prep("عَلَى", "ala", "«against»", "«-e»"),
  tok("مَرْيَمَ", "maryam", "propn", [HJ, MM], "مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Maryam» — a diptote.", "«Meryem» — gayr-i munsarıf."),
  maful_("بُهْتَانًا", "buhtan", "«a calumny»", "«bir iftira»", ar="مَفْعُولٌ بِهِ لِلْمَصْدَرِ قَوْلِهِمْ مَنْصُوبٌ بِالْفَتْحَةِ."),
  naat("عَظِيمًا", "azim", "«tremendous»", "«büyük»", case="nasb", punct=AYA),
  pron_atf("وَقَوْلِهِمْ", "qawl", "قَوْلِ", "هِمْ", "pron-3mp", "«their saying»", "«ve demeleri»"),
  tok("إِنَّا", "inna", "part", [IW], "إِنَّ وَنَا اسْمُهَا — مَقُولُ الْقَوْلِ.", "«we»", "«biz»", segments=[seg("إِنَّ", "inna", "part"), seg("ا", "pron-1p", "pron")]),
  tok("قَتَلْنَا", "qatala", "verb", [IW], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«killed» — inna's khabar.", "«öldürdük» — inne'nin haberi.", segments=[seg("قَتَلْ", "qatala", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("الْمَسِيحَ", "masih", "propn", [MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«the Messiah» — the object.", "«Mesîh'i» — mef'ûl."),
  tok("عِيسَى", "isa", "propn", [BD, MM, "ism-maqsur-manqus"], "بَدَلٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ.", "«ʿĪsā»", "«Îsâ»"),
  tok("ابْنَ", "ibn", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَنْصُوبٌ، مُضَافٌ.", "«son [of]»", "«oğlu»"),
  tok("مَرْيَمَ", "maryam", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ.", "«Maryam»", "«Meryem»"),
  tok("رَسُولَ", "rasul", "noun", [BD, ID], "بَدَلٌ (أَوْ نَعْتٌ) مَنْصُوبٌ، مُضَافٌ — قِيلَ عَلَى سَبِيلِ الِاسْتِهْزَاءِ، أَوْ حِكَايَةً لِقَوْلِ الْمُؤْمِنِينَ.", "«the Messenger [of]» — a badal; said in mockery, or quoting the believers' words.", "«resulü» — bedel; alay yollu, yahut müminlerin sözünün nakli."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  *qatalu_hu("وَمَا قَتَلُوهُ", "qatala", "«kill him»", "«öldürmediler»"),
  *qatalu_hu("وَمَا صَلَبُوهُ", "salaba-crucify", "«crucify him»", "«asmadılar»"),
  tok("وَلٰكِنْ", "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ.", "«but»", "«fakat»", segments=wa_("لٰكِنْ", "lakin", "part")),
  tok("شُبِّهَ", "shabbaha", "verb", [NF, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ (الْأَمْرُ)، أَوِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«it was made to appear so» — a passive; its deputy doer is the understood «the matter», or the phrase «to them».", "«öyle gösterildi» — meçhul; nâib-i fâil mukadder «iş» yahut «onlara» ibaresi."),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«to them»", "«onlara»"),
  ]),
])
sen("s4", "«and those who differ about it are surely in doubt of it: they have no knowledge of it except the following of conjecture, and they did not kill him for certain; rather God raised him to Himself, and God is Mighty, Wise.» (4:157–158)",
        "«Onun hakkında ihtilâfa düşenler bundan elbette şüphe içindedirler; zanna uymak dışında ona dair bir bilgileri yoktur; onu kesinlikle öldürmediler. Aksine Allah onu katına yükseltti; Allah güçlüdür, hikmet sahibidir.» (4:157–158)", [
  *quran([
  inna(wa=True),
  alladhina("nasb", "اسْمُ إِنَّ", "«those who»", "«… -enler»", tags=[IW]),
  mazi_pl("اخْتَلَفُوا", "ikhtalafa", "«differ»", "«ihtilâfa düştüler»", tags=[MW, "form-viii-verbs"]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«about it»", "«onun hakkında»"),
  tok("لَفِي", "fi", "prep", [IW, HJ], "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«surely in» — the emphatic lām on inna's khabar phrase.", "«elbette … içinde» — inne'nin haber ibaresindeki te'kid lâmı.", segments=[seg("لَ", "lam-ibtida", "part"), seg("فِي", "fi", "prep")]),
  majrur("شَكٍّ", "shakk", "«doubt»", "«şüphe»", tags=["doubled-verbs"]),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«of it» — a ṣifa of «doubt».", "«ondan» — «şüphe»nin sıfatı.", tags=[NA], extra_ar=" — صِفَةٌ لِشَكٍّ"),
  tok("مَا", "ma-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ لَا عَمَلَ لَهَا.", "«no»", "«yok»"),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«they have» — a fronted khabar.", "«onların» — öne alınmış haber.", tags=[MK], extra=" — خَبَرٌ مُقَدَّمٌ"),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«of it»", "«ona dair»"),
  prep("مِنْ", "min", "«[any]»", "«bir»", ar="حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ."),
  tok("عِلْمٍ", "ilm", "noun", [MK], "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا بِمِنَ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا.", "«knowledge» — the delayed mubtadaʾ after the extra min.", "«bilgi» — zâid min'den sonra sonraya kalan mübtedâ."),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ — مُنْقَطِعٌ، لِأَنَّ الظَّنَّ لَيْسَ مِنَ الْعِلْمِ.", "«except» — a disjoined exception: conjecture is not knowledge.", "«dışında» — munkatı istisnâ: zan ilimden değildir."),
  tok("اتِّبَاعَ", "ittiba", "noun", ["istithna", ID, "form-viii-verbs"], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ (وَيَجُوزُ كَوْنُهُ مُسْتَثْنًى مُفَرَّغًا بَدَلًا مِنْ عِلْمٍ عَلَى الْمَحَلِّ).", "«the following [of]» — the excepted, in naṣb.", "«uymak» — müstesnâ, mansub."),
  mudaf_ilayh("الظَّنِّ", "zann", "«conjecture»", "«zanna»", tags=["doubled-verbs"]),
  *qatalu_hu("وَمَا قَتَلُوهُ", "qatala", "«kill him»", "«öldürmediler»"),
  tok("يَقِينًا", "yaqin", "noun", ["maful-mutlaq"], "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ (تَيَقَّنُوا ذٰلِكَ يَقِينًا)، أَوْ حَالٌ، أَوْ صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ: قَتْلًا يَقِينًا.", "«for certain» — an absolute object of an understood verb, or a ḥāl.", "«kesinlikle» — mahzuf fiilin mef'ûl-i mutlakı, yahut hâl.", punct=AYA),
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ (انْتِقَالِيٌّ).", "«rather» — the particle of digression.", "«aksine» — idrâb harfi."),
  v_pron("رَفَعَهُ", "rafaa", "رَفَعَ", "هُ", "pron-3ms", "«raised him»", "«onu yükseltti»", hidden=None),
  allah_fail(),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Himself»", "«katına»"),
  wa_kana(),
  tok("اللهُ", "allah", "propn", [KN], "لَفْظُ الْجَلَالَةِ اسْمُ كَانَ مَرْفُوعٌ.", "«God» — kāna's ism.", "«Allah» — kâne'nin ismi."),
  khabar_kana("عَزِيزًا", "aziz", "«Mighty»", "«güçlü»"),
  khabar_kana("حَكِيمًا", "hakim", "«Wise»", "«hikmet sahibi»", ar="خَبَرٌ ثَانٍ لِكَانَ مَنْصُوبٌ بِالْفَتْحَةِ.", punct=AYA),
  ]),
])
sen("s5", "And he is in heaven as God Most High wills him to be — He is the One able over all things; his birth was a wonder, his life a wonder, and his matter from its beginning to its end a wonder, breaking the ordinary course, establishing the absolute divine power.",
        "O, Allah Teâlâ'nın dilediği şekilde göktedir — O her şeye kadirdir; doğumu bir hayret, hayatı bir hayret, işi başından sonuna bir hayrettir; âdeti aşan, mutlak ilâhî kudreti ispat eden.", [
  tok("وَهُوَ", "huwa", "pron", [AT, MK], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and he»", "«ve o»", segments=wa_("هُوَ", "huwa", "pron")),
  prep("فِي", "fi", "«in»", "«-de»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ."),
  majrur("السَّمَاءِ", "sama", "«heaven»", "«gökte»", tags=[MK]),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا مَصْدَرِيَّةٌ.", "«as»", "«… gibi»"),
  v_pron("يُرِيدُهُ", "arada", "يُرِيدُ", "هُ", "pron-3ms", "«wills him»", "«onu diler»", tags=["mudari-marfu", "hollow-verbs", "form-iv-verbs"], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct="،"),
  tok("وَهُوَ", "huwa", "pron", [AT, MK], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَهُوَ مُبْتَدَأٌ — يَعُودُ عَلَى اللهِ.", "«He» — a parenthesis about God.", "«O» — Allah'a dair itirâzî cümle.", segments=wa_("هُوَ", "huwa", "pron")),
  tok("الْقَادِرُ", "qadir", "noun", [MK, "ism-fail"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«the One able» — the khabar.", "«kadir olan» — haber."),
  prep("عَلَى", "ala", "«over»", "«-e»"),
  majrur("كُلِّ", "kull", "«all [of]»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("شَيْءٍ", "shay", "«things»", "«şeye»", punct="،"),
  tok("وَقَدْ", "qad", "part", [AT, "qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi_ta("كَانَتْ", "kana", "«was»", "«idi»", tags=[KN, "hollow-verbs"], extra=" — فِعْلٌ نَاقِصٌ"),
  noun_pron("وِلَادَتُهُ", "wilada", "وِلَادَتُ", "هُ", "pron-3ms", "اسْمُ كَانَ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his birth» — kāna's ism.", "«doğumu» — kâne'nin ismi.", tags=[KN, ID]),
  khabar_kana("عَجَبًا", "ajab", "«a wonder»", "«bir hayret»", punct="،"),
  pron_atf("وَحَيَاتُهُ", "hayat", "حَيَاتُ", "هُ", "pron-3ms", "«his life»", "«ve hayatı»", case="raf"),
  tok("عَجَبًا", "ajab", "noun", [KN], "خَبَرُ كَانَ مَحْذُوفَةٍ (مَعْطُوفَةٍ) مَنْصُوبٌ بِالْفَتْحَةِ.", "«a wonder» — the khabar of an understood repeated kāna.", "«bir hayret» — mukadder kâne'nin haberi.", punct="،"),
  noun_pron("وَأَمْرُهُ", "amr", "وَأَمْرُ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَأَمْرُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his matter» — a mubtadaʾ.", "«ve işi» — mübtedâ.", tags=[AT, MK, ID]),
  prep("مِنْ", "min", "«from»", "«-den»"),
  noun_pron("أَوَّلِهِ", "awwal", "أَوَّلِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its beginning»", "«başından»", tags=[HJ, ID]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  noun_pron("آخِرِهِ", "akhir", "آخِرِ", "هِ", "pron-3ms", "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonuna»", tags=[HJ, ID]),
  tok("عَجَبٌ", "ajab", "noun", [MK], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a wonder» — the khabar.", "«bir hayret» — haber.", punct="،"),
  tok("خَارِقٌ", "khariq", "noun", [MK, "ism-fail"], "خَبَرٌ ثَانٍ (أَوْ نَعْتٌ لِعَجَبٌ) مَرْفُوعٌ.", "«breaking» — a second khabar.", "«aşan» — ikinci haber."),
  li_noun("لِلْعَادَةِ", "ada", "«the ordinary course»", "«âdeti»", extra=" — اللَّامُ لِتَقْوِيَةِ الْعَامِلِ", punct="،"),
  tok("مُثْبِتٌ", "muthbit", "noun", [MK, "ism-fail", "form-iv-verbs"], "خَبَرٌ ثَالِثٌ (أَوْ نَعْتٌ) مَرْفُوعٌ بِالضَّمَّةِ.", "«establishing» — a third khabar.", "«ispat eden» — üçüncü haber."),
  li_noun("لِلْقُدْرَةِ", "qudra", "«the power»", "«kudreti»", extra=" — اللَّامُ لِتَقْوِيَةِ الْعَامِلِ"),
  naat("الْإِلٰهِيَّةِ", "ilahi", "«divine»", "«ilâhî»", tags=["ism-mansub"]),
  naat2("الْمُطْلَقَةِ", "mutlaq", "«absolute»", "«mutlak»", case="jarr", tags=["ism-maful", "form-iv-verbs"], punct="."),
])
# ---------------------------------------------------------------- §35 نُزُولُ عِيسَى عِنْدَ الْقِيَامَةِ (print pp. 61–62)
sen("s6", "And he will descend from heaven when God wills, and establish the proof against those who fell short concerning him and those who went to excess, of the Jews and the Christians; and he will aid the truth and subdue the people of falsehood,",
        "Allah dilediğinde gökten inecek; onun hakkında kusur edenlere ve aşırı gidenlere — Yahudilere ve Hristiyanlara — hücceti ikame edecek; hakka yardım edecek ve bâtıl ehlini ezecek,", [
  tok("وَسَيَنْزِلُ", "nazala", "verb", [AT, "mudari-marfu"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالسِّينُ حَرْفُ اسْتِقْبَالٍ (تَنْفِيسٍ)، وَيَنْزِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and he will descend» — the sīn of the near future.", "«ve inecek» — istikbâl sîn'i.", segments=[seg("وَ", "wa", "conj"), seg("سَ", "sa", "part"), seg("يَنْزِلُ", "nazala", "verb")]),
  tok("مِنَ", "min", "prep", [HJ], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  majrur("السَّمَاءِ", "sama", "«heaven»", "«gökten»"),
  tok("حِينَ", "hina", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when»", "«-dığında»"),
  v_pron("يُرِيدُهُ", "arada", "يُرِيدُ", "هُ", "pron-3ms", "«wills it»", "«onu diler»", tags=[ID, "mudari-marfu", "hollow-verbs", "form-iv-verbs"], hidden=None),
  allah_fail(punct="،"),
  mudari_wa("وَيُقِيمُ", "aqama", "«and establish»", "«ve ikame eder»", tags=["hollow-verbs", "form-iv-verbs"]),
  maful_("الْحُجَّةَ", "hujja", "«the proof»", "«hücceti»"),
  prep("عَلَى", "ala", "«against»", "«-e»"),
  tok("مَنْ", "man-mawsula", "pron", [HJ, MW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«those who»", "«… kimselere»"),
  mazi_pl("فَرَّطُوا", "farrata", "«fell short»", "«kusur ettiler»", tags=[MW, "form-ii-verbs"]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«concerning him»", "«onun hakkında»"),
  mazi_pl("وَأَفْرَطُوا", "afrata", "«and went to excess»", "«ve aşırı gittiler»", tags=[AT, MW, "form-iv-verbs"], wa=True, punct="،"),
  tok("مِنَ", "min", "prep", [HJ, HL], "حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنْ مَنْ.", "«of» — explanatory; a ḥāl of the relative.", "«-den» — beyan için; mevsûlün hâli."),
  majrur("الْيَهُودِ", "yahud", "«the Jews»", "«Yahudiler»"),
  atf("وَالنَّصَارَى", "nasara-christians", "«the Christians»", "«ve Hristiyanlar»", tags=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ", punct="،"),
  mudari_wa("وَيَنْصُرُ", "nasara", "«and aid»", "«ve yardım eder»"),
  maful_("الْحَقَّ", "haqq", "«the truth»", "«hakka»", punct="،"),
  mudari_wa("وَيَكْبِتُ", "kabata", "«and subdue»", "«ve ezer»"),
  maful_("أَهْلَ", "ahl", "«the people [of]»", "«ehlini»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("الْبَاطِلِ", "batil", "«falsehood»", "«bâtıl»", tags=["ism-fail"], punct="،"),
])
sen("s7", "as our Prophet, may God bless him and grant him peace, told of it, and as the sound reports and the mass-transmitted traditions have come down with it, and the Muslims in every age have believed it; and God the Tremendous has spoken truly:",
        "Peygamberimiz (s.a.v.) bunu haber verdiği, sahih haberler ve mütevâtir hadisler bunu bildirdiği ve her çağda Müslümanlar buna inandığı gibi; Yüce Allah doğru söylemiştir:", [
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا مَصْدَرِيَّةٌ.", "«as»", "«… gibi»"),
  mazi("أَخْبَرَ", "akhbara", "«told»", "«haber verdi»", tags=["form-iv-verbs"], hidden=None),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«of it»", "«bunu»"),
  noun_pron("نَبِيُّنَا", "nabi", "نَبِيُّ", "نَا", "pron-1p", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ.", "«our Prophet» — the doer.", "«Peygamberimiz» — fâil.", tags=[FL, ID]),
  mazi("صَلَّى", "salla", "«may bless»", "«salât etsin»", tags=["naqis-verbs", "form-ii-verbs", "jumla-mutarida"], hidden=None, extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ؛ جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ"),
  allah_fail(),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«him»", "«ona»"),
  mazi("وَسَلَّمَ", "sallama", "«and grant peace»", "«ve selâm etsin»", tags=[AT, "form-ii-verbs"], wa=True, hidden="هُوَ"),
  mazi_ta("وَوَرَدَتْ", "warada", "«and have come down»", "«ve bildirdi»", tags=[AT, "mithal-verbs"], wa=True),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«with it»", "«bunu»"),
  fail("الْأَخْبَارُ", "khabar", "«the reports»", "«haberler»", tags=[JT]),
  naat("الصَّحِيحَةُ", "sahih", "«sound»", "«sahih»", case="raf"),
  atf("وَالْأَحَادِيثُ", "hadith", "«the traditions»", "«ve hadisler»", "raf", tags=[JT]),
  naat("الْمُتَوَاتِرَةُ", "mutawatir", "«mass-transmitted»", "«mütevâtir»", case="raf", tags=["ism-fail", "form-vi-verbs"], punct="،"),
  v_pron("وَاعْتَقَدَهُ", "itaqada", "اعْتَقَدَ", "هُ", "pron-3ms", "«and have believed it»", "«ve buna inandı»", tags=["form-viii-verbs"], wa=True, hidden=None),
  tok("الْمُسْلِمُونَ", "muslim", "noun", [FL, JS, "ism-fail", "form-iv-verbs"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«the Muslims» — the doer.", "«Müslümanlar» — fâil."),
  fi(),
  majrur("كُلِّ", "kull", "«every»", "«her»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("عَصْرٍ", "asr", "«age»", "«çağda»", punct="،"),
  mazi("وَصَدَقَ", "sadaqa-be-true", "«and has spoken truly»", "«ve doğru söyledi»", tags=[AT], wa=True, hidden=None),
  allah_fail(),
  naat("الْعَظِيمُ", "azim", "«the Tremendous»", "«Yüce»", case="raf", punct=":"),
])
sen("s8", "«And there is none of the People of the Book but will surely believe in him before his death; and on the Day of Resurrection he will be a witness against them.» (4:159)",
        "«Kitap ehlinden hiç kimse yoktur ki ölümünden önce ona mutlaka inanmasın; kıyamet günü de o, onlara şahit olacaktır.» (4:159)", [
  *quran([
  tok("وَإِنْ", "in-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِنْ نَافِيَةٌ بِمَعْنَى مَا.", "«and … none» — the negating in.", "«ve … yoktur» — nefiy in'i.", segments=wa_("إِنْ", "in-nafiya", "part")),
  prep("مِنْ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِمُبْتَدَأٍ مَحْذُوفٍ: أَحَدٌ مِنْ أَهْلِ الْكِتَابِ."),
  majrur("أَهْلِ", "ahl", "«the People [of]»", "«ehlinden»", tags=[ID, "hadhf-wa-taqdir"], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْمُبْتَدَأُ مَحْذُوفٌ: أَحَدٌ."),
  mudaf_ilayh("الْكِتَابِ", "kitab", "«the Book»", "«Kitap»"),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — وَالْجُمْلَةُ بَعْدَهَا خَبَرٌ (أَوْ صِفَةٌ) لِلْمُبْتَدَأِ الْمَحْذُوفِ.", "«but» — an emptied exception; the clause is the khabar of the understood mubtadaʾ.", "«… ki … -masın» — müferrağ istisnâ; cümle mahzuf mübtedânın haberi."),
  tok("لَيُؤْمِنَنَّ", "aamana", "verb", [MK, "nun-tawkid", "form-iv-verbs"], "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مَحْذُوفٍ، وَيُؤْمِنَنَّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى الْفَتْحِ لِاتِّصَالِهِ بِنُونِ التَّوْكِيدِ الثَّقِيلَةِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«will surely believe» — the lām of an understood oath; the verb is built on fatḥa before the heavy nūn of emphasis.", "«mutlaka inanacaktır» — mukadder kasemin lâmı; şeddeli te'kid nûnu önünde fetha üzere mebnî.", segments=[seg("لَ", "lam-ibtida", "part"), seg("يُؤْمِنَ", "aamana", "verb"), seg("نَّ", "nun-tawkid", "part")]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«in him»", "«ona»"),
  zarf("قَبْلَ", "qabla", "«before»", "«-den önce»", kind="زَمَانٍ"),
  noun_pron("مَوْتِهِ", "mawt", "مَوْتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — يَعُودُ عَلَى عِيسَى (أَوْ عَلَى الْكِتَابِيِّ).", "«his death» — the pronoun refers to ʿĪsā (or to the Scripturary).", "«ölümünden» — zamir Îsâ'ya (yahut ehl-i kitaptan olana) râcidir.", tags=[ID]),
  tok("وَيَوْمَ", "yawm", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ (أَوِ اسْتِئْنَافِيَّةٌ)، وَيَوْمَ ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«and on the Day [of]»", "«ve … günü»", segments=wa_("يَوْمَ", "yawm", "noun")),
  mudaf_ilayh("الْقِيَامَةِ", "qiyama", "«Resurrection»", "«kıyamet»"),
  tok("يَكُونُ", "kana", "verb", [KN, "mudari-marfu", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (عِيسَى).", "«he will be» — kāna; its ism is ʿĪsā.", "«o … olacak» — kâne; ismi Îsâ."),
  prep_pron("عَلَيْهِمْ", "ala", "هِمْ", "pron-3mp", "«against them»", "«onlara»"),
  khabar_kana("شَهِيدًا", "shahid-martyr", "«a witness»", "«şahit»", punct=AYA),
  ]),
])

CAND = {
 "amma": G("amma", "أَمَّا", None, "part", "as for", "-e gelince", 1),
 "sayyid": G("sayyid", "سَيِّد", "س و د", "noun", "a master, a lord", "efendi, seyyid", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "isa": G("isa", "عِيسَى", None, "propn", "ʿĪsā (Jesus)", "Îsâ", 1),
 "ibn": G("ibn", "ابْن", "ب ن ي", "noun", "a son", "oğul", 1, plural="أَبْنَاء"),
 "maryam": G("maryam", "مَرْيَم", None, "propn", "Maryam (Mary)", "Meryem", 1),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "fa": G("fa", "فَ", None, "conj", "so, and then", "böylece, -ınca", 1),
 "najja": G("najja", "نَجَّى", "ن ج و", "verb", "to save, to rescue (Form II, defective)", "kurtarmak (tef'îl, nâkıs)", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "kayd": G("kayd", "كَيْد", "ك ي د", "noun", "a plot, scheming", "tuzak, hile", 2),
 "yahud": G("yahud", "الْيَهُود", "ه و د", "noun", "the Jews", "Yahudiler", 1),
 "rafaa": G("rafaa", "رَفَعَ", "ر ف ع", "verb", "to raise", "yükseltmek", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "mukarram": G("mukarram", "مُكَرَّم", "ك ر م", "noun", "honoured (a passive participle of Form II)", "şereflendirilmiş, mükerrem (tef'îl ism-i mef'ûlü)", 2),
 "mutahhar": G("mutahhar", "مُطَهَّر", "ط ه ر", "noun", "purified (a passive participle of Form II)", "arındırılmış, mutahhar (tef'îl ism-i mef'ûlü)", 2),
 "alladhina": G("alladhina", "الَّذِينَ", None, "pron", "who, those who (pl.)", "ki onlar, … -enler", 1),
 "kafara": G("kafara", "كَفَرَ", "ك ف ر", "verb", "to disbelieve", "inkâr etmek, küfretmek", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "qawl": G("qawl", "قَوْل", "ق و ل", "noun", "a saying, speech", "söz", 1, plural="أَقْوَال"),
 "huwa": G("huwa", "هُوَ", None, "pron", "he / it", "o", 1),
 "tahaddatha": G("tahaddatha", "تَحَدَّثَ", "ح د ث", "verb", "to speak (ʿan: of) (Form V)", "söz etmek, konuşmak (tefa''ul)", 1),
 "an": G("an", "عَنْ", None, "prep", "from, about", "-den, hakkında", 1),
 "kufr": G("kufr", "كُفْر", "ك ف ر", "noun", "unbelief", "küfür", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on, against", "üzerine, -e karşı", 1),
 "buhtan": G("buhtan", "بُهْتَان", "ب ه ت", "noun", "a calumny, a slander", "iftira, bühtan", 2),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great, tremendous", "büyük, azîm", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "qatala": G("qatala", "قَتَلَ", "ق ت ل", "verb", "to kill", "öldürmek", 1),
 "masih": G("masih", "الْمَسِيح", "م س ح", "propn", "the Messiah", "Mesîh", 1),
 "rasul": G("rasul", "رَسُول", "ر س ل", "noun", "a messenger", "resul", 1, plural="رُسُل"),
 "ma-nafiya": G("ma-nafiya", "مَا (النَّافِيَة)", None, "part", "not (the negating mā)", "değil, yok (nefiy mâ'sı)", 1),
 "salaba-crucify": G("salaba-crucify", "صَلَبَ", "ص ل ب", "verb", "to crucify", "çarmıha germek", 2),
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but (the lightened lākin)", "fakat (muhaffef lâkin)", 1),
 "shabbaha": G("shabbaha", "شَبَّهَ", "ش ب ه", "verb", "to make resemble; (passive, shubbiha lahum) it was made to appear so to them (Form II)", "benzetmek; (meçhul, şübbihe lehum) onlara öyle gösterildi (tef'îl)", 1),
 "li": G("li", "لِ", None, "prep", "for, to", "için, -e", 1),
 "ikhtalafa": G("ikhtalafa", "اِخْتَلَفَ", "خ ل ف", "verb", "to differ (Form VIII)", "ihtilâf etmek, ayrılığa düşmek (iftiâl)", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "lam-ibtida": G("lam-ibtida", "لَ (لَامُ الِابْتِدَاءِ)", None, "part", "the emphatic lām of inception", "ibtidâ (te'kid) lâmı", 2),
 "shakk": G("shakk", "شَكّ", "ش ك ك", "noun", "doubt", "şüphe", 1),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge; a science", "ilim", 1, plural="عُلُوم"),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "ittiba": G("ittiba", "اتِّبَاع", "ت ب ع", "noun", "following (the maṣdar of Form VIII)", "uyma, tâbi olma (iftiâl masdarı)", 1),
 "zann": G("zann", "ظَنّ", "ظ ن ن", "noun", "a supposition, conjecture", "zan", 1, plural="ظُنُون"),
 "yaqin": G("yaqin", "يَقِين", "ي ق ن", "noun", "certainty", "yakîn, kesinlik", 1),
 "bal": G("bal", "بَلْ", None, "part", "rather, nay", "aksine, bilakis", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "aziz": G("aziz", "عَزِيز", "ع ز ز", "noun", "mighty; dear", "azîz, güçlü; değerli", 1),
 "hakim": G("hakim", "حَكِيم", "ح ك م", "noun", "wise", "hakîm, hikmetli", 1),
 "sama": G("sama", "سَمَاء", "س م و", "noun", "a heaven, the sky", "gök", 1, plural="سَمَاوَات"),
 "kama": G("kama", "كَمَا", None, "part", "as, just as", "… gibi", 1),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to want, to will (Form IV, hollow)", "istemek, dilemek (if'âl, ecvef)", 1),
 "qadir": G("qadir", "قَادِر", "ق د ر", "noun", "powerful, able (an active participle)", "kadir, gücü yeten (ism-i fâil)", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "shay": G("shay", "شَيْء", "ش ي أ", "noun", "a thing", "şey", 1, plural="أَشْيَاء"),
 "wilada": G("wilada", "وِلَادَة", "و ل د", "noun", "birth", "doğum", 1),
 "ajab": G("ajab", "عَجَب", "ع ج ب", "noun", "a wonder, astonishment", "hayret, şaşılacak şey", 1),
 "hayat": G("hayat", "حَيَاة", "ح ي ي", "noun", "life", "hayat", 1),
 "amr": G("amr", "أَمْر", "أ م ر", "noun", "a matter; a command", "iş; emir", 1, plural="أُمُور"),
 "awwal": G("awwal", "أَوَّل", "أ و ل", "noun", "first; the beginning", "ilk; baş", 1),
 "akhir": G("akhir", "آخِر", "أ خ ر", "noun", "the last; the end", "son", 1),
 "khariq": G("khariq", "خَارِق", "خ ر ق", "noun", "breaking through, extraordinary (an active participle)", "yırtan, aşan; hârika (ism-i fâil)", 2),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "a custom, the ordinary course", "âdet", 1, plural="عَادَات"),
 "muthbit": G("muthbit", "مُثْبِت", "ث ب ت", "noun", "establishing, proving (an active participle of Form IV)", "ispat eden (if'âl ism-i fâili)", 2),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "ilahi": G("ilahi", "إِلٰهِيّ", "أ ل ه", "noun", "divine (a nisba)", "ilâhî (nisbet)", 1),
 "mutlaq": G("mutlaq", "مُطْلَق", "ط ل ق", "noun", "absolute (a passive participle of Form IV)", "mutlak (if'âl ism-i mef'ûlü)", 1),
 "sa": G("sa", "سَـ", None, "part", "the sīn of the near future (will)", "yakın gelecek sîn'i (-ecek)", 1),
 "nazala": G("nazala", "نَزَلَ", "ن ز ل", "verb", "to descend", "inmek", 1),
 "hina": G("hina", "حِينَ", "ح ي ن", "noun", "when, at the time of", "-dığı zaman, … vakti", 1),
 "aqama": G("aqama", "أَقَامَ", "ق و م", "verb", "to establish, to set up (Form IV, hollow)", "ikame etmek, kurmak (if'âl, ecvef)", 1),
 "hujja": G("hujja", "حُجَّة", "ح ج ج", "noun", "a proof, an argument", "hüccet, delil", 1, plural="حُجَج"),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", None, "pron", "whoever, he who", "kim ki, … kimse", 1),
 "farrata": G("farrata", "فَرَّطَ", "ف ر ط", "verb", "to fall short, to neglect (fī) (Form II)", "kusur etmek, ihmal etmek (tef'îl)", 2),
 "afrata": G("afrata", "أَفْرَطَ", "ف ر ط", "verb", "to go to excess (Form IV)", "aşırıya gitmek (if'âl)", 2),
 "nasara-christians": G("nasara-christians", "النَّصَارَى", "ن ص ر", "noun", "the Christians", "Hristiyanlar, Nasrânîler", 1),
 "nasara": G("nasara", "نَصَرَ", "ن ص ر", "verb", "to help, to give victory", "yardım etmek, zafer vermek", 1),
 "haqq": G("haqq", "الْحَقّ", "ح ق ق", "noun", "the truth; a right", "hak, gerçek", 1),
 "kabata": G("kabata", "كَبَتَ", "ك ب ت", "verb", "to subdue, to humble", "ezmek, boyun eğdirmek", 3),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "people, family; the people of", "ehil, aile; … ehli", 1),
 "batil": G("batil", "بَاطِل", "ب ط ل", "noun", "false, vain; falsehood (an active participle)", "bâtıl (ism-i fâil)", 1),
 "akhbara": G("akhbara", "أَخْبَرَ", "خ ب ر", "verb", "to inform, to tell (bi: of) (Form IV)", "haber vermek (if'âl)", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "salla": G("salla", "صَلَّى", "ص ل و", "verb", "to pray; (God) to bless (Form II, defective)", "namaz kılmak; (Allah) salât etmek (tef'îl, nâkıs)", 1),
 "sallama": G("sallama", "سَلَّمَ", "س ل م", "verb", "to greet with peace; to hand over (Form II)", "selâm vermek; teslim etmek (tef'îl)", 1),
 "warada": G("warada", "وَرَدَ", "و ر د", "verb", "to come, to arrive (of a report) (an assimilated verb)", "gelmek, vârit olmak (misâl fiil)", 1),
 "khabar": G("khabar", "خَبَر", "خ ب ر", "noun", "a report, news", "haber", 1, plural="أَخْبَار"),
 "sahih": G("sahih", "صَحِيح", "ص ح ح", "noun", "sound, correct", "sahih, doğru", 1),
 "hadith": G("hadith", "حَدِيث", "ح د ث", "noun", "a ḥadīth; talk", "hadis; söz", 1, plural="أَحَادِيث"),
 "mutawatir": G("mutawatir", "مُتَوَاتِر", "و ت ر", "noun", "mass-transmitted (an active participle of Form VI)", "mütevâtir (tefâul ism-i fâili)", 2),
 "itaqada": G("itaqada", "اِعْتَقَدَ", "ع ق د", "verb", "to believe firmly (Form VIII)", "inanmak, itikat etmek (iftiâl)", 1),
 "muslim": G("muslim", "مُسْلِم", "س ل م", "noun", "a Muslim (an active participle of Form IV)", "müslüman (if'âl ism-i fâili)", 1, plural="مُسْلِمُونَ"),
 "asr": G("asr", "عَصْر", "ع ص ر", "noun", "an age, an era", "çağ, asır", 1),
 "sadaqa-be-true": G("sadaqa-be-true", "صَدَقَ", "ص د ق", "verb", "to speak the truth; to prove true", "doğru söylemek; doğru çıkmak", 1),
 "in-nafiya": G("in-nafiya", "إِنْ (النَّافِيَة)", None, "part", "not (the negating in)", "değil, yok (nefiy in'i)", 2),
 "kitab": G("kitab", "كِتَاب", "ك ت ب", "noun", "a book; the Book", "kitap", 1, plural="كُتُب"),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "nun-tawkid": G("nun-tawkid", "نَّ (نُونُ التَّوْكِيدِ)", None, "part", "the heavy nūn of emphasis", "şeddeli te'kid nûnu", 2),
 "qabla": G("qabla", "قَبْلَ", "ق ب ل", "noun", "before", "-den önce", 1),
 "mawt": G("mawt", "مَوْت", "م و ت", "noun", "death", "ölüm", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "qiyama": G("qiyama", "قِيَامَة", "ق و م", "noun", "the Resurrection", "kıyâmet", 1),
 "shahid-martyr": G("shahid-martyr", "شَهِيد", "ش ه د", "noun", "a witness; a martyr", "şahit; şehit", 1, plural="شُهَدَاء"),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "farrata", _sg.derived(_sg.B2, _sg.W2, "ُ", "فَرَّط", "فَرِّط", "فَرِّط", "تَفْرِيط", "مُفَرِّط", "مُفَرَّط", "فُرِّطَ", "يُفَرَّطُ", "فَرَّطَ فِي الْأَمْرِ: قَصَّرَ فِيهِ وَضَيَّعَهُ."))
put_morph(mo, "afrata", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْرَط", "فْرِط", "أَفْرِط", "إِفْرَاط", "مُفْرِط", None, None, None, "أَفْرَطَ فِي الْأَمْرِ: جَاوَزَ فِيهِ الْحَدَّ."))
put_morph(mo, "kabata", _sg.sound1("daraba", "كَبَت", "كْبِت", "اِكْبِت", "كَبْت", "كَابِت", "مَكْبُوت", "كُبِتَ", "يُكْبَتُ", "كَبَتَهُ يَكْبِتُهُ: أَذَلَّهُ وَصَرَفَهُ وَأَخْزَاهُ."))
put_morph(mo, "itaqada", _sg.derived(_sg.B8, _sg.W8, "َ", "اِعْتَقَد", "عْتَقِد", "اِعْتَقِد", "اِعْتِقَاد", "مُعْتَقِد", "مُعْتَقَد", "اُعْتُقِدَ", "يُعْتَقَدُ", "اِعْتَقَدَ الشَّيْءَ: صَدَّقَ بِهِ وَعَقَدَ عَلَيْهِ قَلْبَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch41 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 41 (print pp. 60–62; ʿĪsā §33–35): God saves him and raises him to Himself (s1); the Qurʾān speaks — al-Nisāʾ 4:156–158: the calumny against Maryam, «they did not kill him nor crucify him, but it was made to appear so», «rather God raised him» (s2–s4); his whole matter a wonder (s5); his descent at the end of time, the proof against both communities, as the Prophet told and the Muslims believed, with 4:159 (s6–s8)."
ADD_TR = " Kırk birinci bölüm (baskı s. 60–62; Îsâ §33–35): Allah onu kurtarır ve katına yükseltir (s1); Kur'ân anlatır — Nisâ 156–158: Meryem'e iftira, «onu öldürmediler, asmadılar; onlara öyle gösterildi», «aksine Allah onu yükseltti» (s2–s4); işi baştan sona hayret (s5); kıyamete yakın inişi, iki ümmete karşı hüccet, Peygamber'in haberi ve Müslümanların inancı, 4:159 ile (s6–s8)."
write_out(41, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §33–35 + 4:156–159", GLOSS_ADD, notes=(), related=())
report(41, S, GLOSS_ADD, ())
