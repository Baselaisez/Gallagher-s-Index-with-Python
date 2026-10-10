# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 26: «قِصَّةُ عِيسَى» §6 (ingratitude: false creeds seeping in; the calf; ʿUzayr; shirk attributed to prophets) and §7 (vainglory: «we are God's sons and His beloved», «the Fire will touch us only for numbered days»); print pp. 43–44.
python3 tools/authoring/author_qisas4_ch26.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ عِيسَى: نُكْرَانٌ لِلْجَمِيلِ، وَزَهْوٌ وَدَلَالٌ", "en": "The story of ʿĪsā: ingratitude; vainglory and conceit", "tr": "Îsâ'nın kıssası: nankörlük; kibir ve şımarıklık"}
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

# ---------------------------------------------------------------- §6 نُكْرَانٌ لِلْجَمِيلِ (print pp. 43–44)
sen("s1", "But by force of mixing with and neighbouring the idolatrous, polytheist peoples, and through the long lapse of time since the prophets' teachings, false creeds and pagan customs seeped into them;",
        "Fakat putperest, müşrik kavimlerle karışıp komşuluk etmeleri ve peygamberlerin öğretilerinin üzerinden uzun zaman geçmesi yüzünden onlara sahte akîdeler ve câhiliye âdetleri sızdı;", [
  tok("وَلٰكِنْ", "lakin", "part", [AT], "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "«but» — the lightened lākin; no government.", "«fakat» — muhaffef lâkin; amel etmez.", segments=wa_("لٰكِنْ", "lakin", "part")),
  mazi_ta("تَسَرَّبَتْ", "tasarraba", "«seeped»", "«sızdı»", tags=["form-v-verbs"]),
  prep_pron("إِلَيْهِمْ", "ila", "هِمْ", "pron-3mp", "«into them»", "«onlara»"),
  bi_noun("بِحُكْمِ", "hukm", "«by force [of]»", "«… gereği»", tags=[ID], extra="، مُضَافٌ — أَيْ: بِسَبَبِ"),
  mudaf_ilayh("الِاخْتِلَاطِ", "ikhtilat", "«mixing»", "«karışmanın»", tags=["form-viii-verbs"]),
  atf("وَمُجَاوَرَةِ", "mujawara", "«neighbouring»", "«komşuluğun»", tags=[ID, "form-iii-verbs"], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("الشُّعُوبِ", "shab", "«the peoples»", "«kavimlerle»", tags=[JT]),
  naat("الْوَثَنِيَّةِ", "wathani", "«idolatrous»", "«putperest»", tags=["ism-mansub"]),
  naat2("الْمُشْرِكَةِ", "mushrik", "«polytheist»", "«müşrik»", case="jarr", tags=["ism-fail", "form-iv-verbs"], punct="،"),
  tok("وَبِطُولِ", "tul", "noun", [AT, HJ, ID], "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ حَرْفُ جَرٍّ، وَطُولِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "«and by the length [of]»", "«ve … uzunluğuyla»", segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("طُولِ", "tul", "noun")]),
  mudaf_ilayh("الْعَهْدِ", "ahd", "«the time»", "«zamanın»"),
  bi_noun("بِتَعَالِيمِ", "talim", "«since the teachings [of]»", "«öğretilerine»", tags=[ID, JT], extra="، مُضَافٌ — مُتَعَلِّقٌ بِالْعَهْدِ"),
  mudaf_ilayh("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberlerin»", tags=[JT], punct="،"),
  tok("عَقَائِدُ", "aqida", "noun", [FL, JT, MM], "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — صِيغَةُ مُنْتَهَى الْجُمُوعِ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«creeds» — the delayed doer; a muntahā plural, diptote.", "«akîdeler» — sonraya bırakılmış fâil; müntehe'l-cumû', gayr-i munsarıf."),
  naat("زَائِفَةٌ", "zaif", "«false»", "«sahte»", case="raf", tags=["ism-fail"], punct="،"),
  atf("وَعَادَاتٌ", "ada", "«customs»", "«âdetler»", "raf", tags=[JM]),
  naat("جَاهِلِيَّةٌ", "jahili", "«pagan»", "«câhiliye»", case="raf", tags=["ism-mansub"], punct="،"),
])
sen("s2", "and they had worshipped the calf in Egypt, and went to extremes in sanctifying and magnifying ʿUzayr until they carried him beyond the bounds of humanity,",
        "Mısır'da buzağıya tapmışlardı; Üzeyr'i kutsamakta ve yüceltmekte öyle aşırıya gittiler ki onu beşeriyet sınırlarının ötesine taşıdılar;", [
  tok("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and [indeed]»", "«ve [gerçekten]»", segments=wa_("قَدْ", "qad", "part")),
  mazi_pl("عَبَدُوا", "abada", "«they had worshipped»", "«tapmışlardı»"),
  maful_("الْعِجْلَ", "ijl", "«the calf»", "«buzağıya»"),
  fi(),
  tok("مِصْرَ", "misr", "propn", [HJ, MM], "مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«Egypt» — a diptote (a feminine proper name): fatḥa for kasra.", "«Mısır'da» — gayr-i munsarıf (müennes özel isim): kesre yerine fetha.", punct="،"),
  mazi_pl("وَبَالَغُوا", "balagha-exaggerate", "«and they went to extremes»", "«ve aşırıya gittiler»", tags=[AT, "form-iii-verbs"], wa=True),
  fi(),
  majrur("تَقْدِيسِ", "taqdis", "«sanctifying»", "«kutsamakta»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("عُزَيْرٍ", "uzayr", "propn", [ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُنَوَّنٌ — مُنْصَرِفٌ هُنَا كَمَا فِي قِرَاءَةِ حَفْصٍ «عُزَيْرٌ ابْنُ اللهِ»؛ وَمَنَعَهُ آخَرُونَ لِلْعُجْمَةِ.", "«ʿUzayr» — declined with tanwīn here, as in Ḥafṣ's reading of 9:30; others treat it as a foreign diptote.", "«Üzeyr'i» — burada tenvinli, Hafs kıraatindeki gibi (9:30); bazıları yabancı sayıp gayr-i munsarıf okur."),
  pron_atf("وَتَعْظِيمِهِ", "tazim", "تَعْظِيمِ", "هِ", "pron-3ms", "«magnifying him»", "«yüceltmekte»", tags=["form-ii-verbs"], punct="،"),
  tok("حَتَّى", "hatta", "part", [], "حَرْفُ ابْتِدَاءٍ (غَايَةٍ) يَدْخُلُ عَلَى الْجُمْلَةِ؛ لَا عَمَلَ لَهُ.", "«until» — ḥattā of the limit before a clause; no government.", "«öyle ki» — cümle başına gelen gâye harfi; amel etmez."),
  mazi_wa_alif("تَخَطَّوْا", "takhatta", "«they carried [him] beyond»", "«aştılar»", tags=["form-v-verbs"]),
  prep_pron("بِهِ", "bi", "هِ", "pron-3ms", "«him»", "«onu»"),
  maful_("حُدُودَ", "hadd", "«the bounds [of]»", "«sınırlarını»", tags=[ID, JT], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("الْبَشَرِيَّةِ", "bashariyya", "«humanity»", "«beşeriyetin»", punct="،"),
])
sen("s3", "and their impudence reached the point that they attributed some of the works of shirk and idolatry, works of sorcery and unbelief, and hideous deeds to some of the prophets, and did not fear God in them.",
        "küstahlıkları, şirk ve putperestlik işlerinden, büyü ve küfür işlerinden, çirkin fiillerden bir kısmını bazı peygamberlere nispet edecek dereceye vardı; onlar hakkında Allah'tan korkmadılar.", [
  mazi_ta("وَبَلَغَتْ", "balagha", "«and reached»", "«ve vardı»", tags=[AT], wa=True),
  prep_pron("بِهِمُ", "bi", "هِمُ", "pron-3mp", "«with them»", "«onları»", extra_ar=" — ضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  fail("الْوَقَاحَةُ", "waqaha", "«impudence»", "«küstahlık»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  an_nasb("فِي مَحَلِّ جَرٍّ بِإِلَى", "«that»", "«-mesine»"),
  tok("نَسَبُوا", "nasaba-attribute", "verb", [AN], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ، وَالْوَاوُ فَاعِلٌ — وَأَنْ قَبْلَ الْمَاضِي مَصْدَرِيَّةٌ غَيْرُ عَامِلَةٍ.", "«they attributed» — a māḍī after an: the an is maṣdarī but cannot govern a māḍī.", "«nispet ettiler» — en'den sonra mâzî: masdariyye, fakat mâzîde amel etmez."),
  maful_("بَعْضَ", "bad", "«some [of]»", "«bir kısmını»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ."),
  mudaf_ilayh("أَعْمَالِ", "amal-work", "«the works [of]»", "«işlerinden»", tags=[ID, JT], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الشِّرْكِ", "shirk", "«shirk»", "«şirk»"),
  atf("وَالْوَثَنِيَّةِ", "wathaniyya", "«idolatry»", "«putperestlik»", punct="،"),
  atf("وَأَعْمَالِ", "amal-work", "«works [of]»", "«işlerinden»", tags=[ID, JT], sign="بِالْكَسْرَةِ، مُضَافٌ"),
  mudaf_ilayh("السِّحْرِ", "sihr", "«sorcery»", "«büyü»"),
  atf("وَالْكُفْرِ", "kufr", "«unbelief»", "«küfür»", punct="،"),
  atf("وَالْأَفْعَالِ", "fil", "«the deeds»", "«fiillerden»", tags=[JT]),
  naat("الشَّنِيعَةِ", "shani", "«hideous»", "«çirkin»", punct="،"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("بَعْضِ", "bad", "«some [of]»", "«bazı»", tags=[ID], ar="مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  mudaf_ilayh("الْأَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberlere»", tags=[JT], punct="،"),
  tok("وَلَمْ", "lam", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not» — lam: negation, jazm, and the turn to the past.", "«ve … -madı» — lem: nefiy, cezm ve mâzîye çevirme.", segments=wa_("لَمْ", "lam", "part")),
  tok("يَتَّقُوا", "ittaqa", "verb", [LJ, AK, "naqis-verbs", "form-viii-verbs"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ — نَاقِصٌ، حُذِفَتْ لَامُهُ قَبْلَ وَاوِ الْجَمَاعَةِ: يَتَّقِي + ونَ.", "«they feared» — jazm by dropping the nūn; the defective yāʾ dropped before the wāw.", "«sakındılar» — nûnun hazfi ile meczûm; nâkıs yâ cemi vâvı önünde düştü."),
  tok("اللهَ", "allah", "propn", [MB], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«God» — the object.", "«Allah'tan» — mef'ûl."),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«in them» — concerning the prophets.", "«onlar hakkında»", punct="."),
])
# ---------------------------------------------------------------- §7 زَهْوٌ وَدَلَالٌ (print p. 44)
sen("s4", "And despite all that they were intensely boastful of their lineage, intensely reliant on wishes and dreams,",
        "Bütün bunlara rağmen soylarıyla son derece böbürlenir, kuruntulara ve hayallere son derece güvenirlerdi;", [
  kana_pl(),
  tok("رَغْمَ", "raghma", "noun", [MF, ID], "ظَرْفٌ (أَوْ مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ) مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — بِمَعْنَى: عَلَى الرَّغْمِ مِنْ.", "«despite» — an adverbial maṣdar, annexed.", "«-e rağmen» — muzâf zarf/masdar."),
  mudaf_ilayh("كُلِّ", "kull", "«all [of]»", "«bütün»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ."),
  tok("ذٰلِكَ", "dhalika", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that» — a demonstrative as muḍāf ilayh.", "«bunlara» — muzâfun ileyh olan işaret ismi."),
  tok("شَدِيدِي", "shadid", "noun", [KN, JS, ID], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ — إِضَافَةٌ لَفْظِيَّةٌ: صِفَةٌ مُشَبَّهَةٌ أُضِيفَتْ إِلَى مَعْمُولِهَا.", "«intense [in]» — kāna's khabar, a sound plural in naṣb by the yāʾ; its nūn dropped for the annexation (a lafẓī iḍāfa).", "«son derece … olan» — kâne'nin haberi, yâ ile mansub cemi müzekker sâlim; nûnu izâfet için düştü (lafzî izâfet)."),
  mudaf_ilayh("الْإِدْلَالِ", "idlal", "«boasting»", "«böbürlenmede»", tags=["form-iv-verbs"]),
  bi_noun("بِالنَّسَبِ", "nasab", "«of lineage»", "«soyla»", punct="،"),
  tok("شَدِيدِي", "shadid", "noun", [KN, JS, ID], "خَبَرٌ ثَانٍ لِكَانَ مَنْصُوبٌ بِالْيَاءِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.", "«intense [in]» — a second khabar of kāna.", "«son derece … olan» — kâne'nin ikinci haberi."),
  mudaf_ilayh("الِاعْتِمَادِ", "itimad", "«reliance»", "«güvenmede»", tags=["form-viii-verbs"]),
  prep("عَلَى", "ala", "«on»", "«-e»"),
  majrur("الْأَمَانِيِّ", "umniya", "«wishes»", "«kuruntulara»", tags=[JT], ar="مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ أُمْنِيَّة عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ بِيَاءٍ مُشَدَّدَةٍ."),
  atf("وَالْأَحْلَامِ", "hulm", "«dreams»", "«hayallere»", tags=[JT], punct="،"),
])
sen("s5", "saying: «We are the sons of God and His beloved ones»;",
        "«Biz Allah'ın oğulları ve sevgilileriyiz» derlerdi;", [
  khamsa("يَقُولُونَ", "qala", "«saying»", "«derlerdi»", tags=[HL, "hollow-verbs"], extra_ar=" — وَالْجُمْلَةُ حَالٌ (أَوْ خَبَرٌ ثَالِثٌ لِكَانَ)", punct=":"),
  tok("نَحْنُ", "nahnu", "pron", [MK, IQ], "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ؛ حِكَايَةُ قَوْلِهِمْ كَمَا فِي الْقُرْآنِ (5:18).", "«we» — the mubtadaʾ; the quoted saying as the Qurʾān reports it (5:18).", "«biz» — mübtedâ; Kur'ân'ın naklettiği sözleri (5:18)."),
  tok("أَبْنَاءُ", "ibn", "noun", [MK, ID, JT], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the sons [of]» — the khabar.", "«oğulları» — haber."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  pron_atf("وَأَحِبَّاؤُهُ", "habib", "أَحِبَّاؤُ", "هُ", "pron-3ms", "«His beloved ones»", "«sevgilileri»", case="raf", tags=[JT], punct="."),
])
sen("s6", "and saying: «The Fire will not touch us except for a number of days».",
        "ve «Ateş bize sayılı günlerden başka dokunmayacak» derlerdi.", [
  khamsa("وَيَقُولُونَ", "qala", "«and saying»", "«ve derlerdi»", tags=[AT, HL, "hollow-verbs"], wa=True, punct=":"),
  tok("لَنْ", "lan", "part", [IQ], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ؛ حِكَايَةُ قَوْلِهِمْ كَمَا فِي الْقُرْآنِ (2:80).", "«will not» — lan: negation, naṣb, and the future; their saying as the Qurʾān reports it (2:80).", "«-mayacak» — len: nefiy, nasb ve istikbâl; Kur'ân'ın naklettiği sözleri (2:80)."),
  tok("تَمَسَّنَا", "massa", "verb", [MB, "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِلَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَنَا مَفْعُولٌ بِهِ مُقَدَّمٌ — مُضَاعَفٌ.", "«touch us» — naṣb by lan; nā the fronted object; a doubled verb.", "«bize dokunacak» — len ile mansub; nâ öne alınmış mef'ûl; muzâaf.", segments=[seg("تَمَسَّ", "massa", "verb"), seg("نَا", "pron-1p", "pron")]),
  fail("النَّارُ", "nar", "«the Fire»", "«ateş»"),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.", "«except» — an emptied exception.", "«-den başka» — müferrağ istisnâ."),
  tok("أَيَّامًا", "yawm", "noun", [MF, JT], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — وَالِاسْتِثْنَاءُ مُفَرَّغٌ.", "«[for] days» — an adverb of time.", "«günler» — zaman zarfı."),
  naat("مَعْدُودَةً", "madud", "«numbered»", "«sayılı»", case="nasb", tags=["ism-maful"], punct="."),
])

CAND = {
 "lakin": G("lakin", "لٰكِنْ", None, "part", "but (the lightened lākin)", "fakat (muhaffef lâkin)", 1),
 "tasarraba": G("tasarraba", "تَسَرَّبَ", "س ر ب", "verb", "to seep, to infiltrate (ilā: into) (Form V)", "sızmak (tefa''ul)", 3),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "pron-3mp": G("pron-3mp", "ـهُمْ", None, "pron", "them / their", "onları / onların", 1),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "a ruling; rule", "hüküm; yönetim", 1, plural="أَحْكَام"),
 "ikhtilat": G("ikhtilat", "اِخْتِلَاط", "خ ل ط", "noun", "mixing, intermingling (the maṣdar of Form VIII)", "karışma, ihtilât (iftiâl masdarı)", 2),
 "mujawara": G("mujawara", "مُجَاوَرَة", "ج و ر", "noun", "neighbouring (the maṣdar of Form III)", "komşuluk (müfâale masdarı)", 2),
 "shab": G("shab", "شَعْب", "ش ع ب", "noun", "a people", "halk, kavim", 1, plural="شُعُوب"),
 "wathani": G("wathani", "وَثَنِيّ", "و ث ن", "noun", "idolatrous, pagan (a nisba)", "putperest (nisbet)", 2),
 "mushrik": G("mushrik", "مُشْرِك", "ش ر ك", "noun", "a polytheist (an active participle of Form IV)", "müşrik (if'âl ism-i fâili)", 1),
 "tul": G("tul", "طُول", "ط و ل", "noun", "length", "uzunluk", 1),
 "wa": G("wa", "وَ", None, "conj", "and", "ve", 1),
 "bi": G("bi", "بِ", None, "prep", "with, by", "ile", 1),
 "ahd": G("ahd", "عَهْد", "ع ه د", "noun", "a time, an era; a covenant", "zaman, dönem; ahit", 1, plural="عُهُود"),
 "talim": G("talim", "تَعْلِيم", "ع ل م", "noun", "teaching; (pl.) teachings", "öğretme; (ç.) öğretiler", 1, plural="تَعَالِيم"),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "aqida": G("aqida", "عَقِيدَة", "ع ق د", "noun", "a creed", "akîde", 1, plural="عَقَائِد"),
 "zaif": G("zaif", "زَائِف", "ز ي ف", "noun", "false, counterfeit (an active participle)", "sahte (ism-i fâil)", 2),
 "ada": G("ada", "عَادَة", "ع و د", "noun", "a custom", "âdet", 1, plural="عَادَات"),
 "jahili": G("jahili", "جَاهِلِيّ", "ج ه ل", "noun", "of the Jāhiliyya, pagan (a nisba)", "câhiliye devrine ait (nisbet)", 2),
 "qad": G("qad", "قَدْ", None, "part", "indeed, already", "gerçekten, -mişti", 1),
 "abada": G("abada", "عَبَدَ", "ع ب د", "verb", "to worship", "tapmak, ibadet etmek", 1),
 "ijl": G("ijl", "عِجْل", "ع ج ل", "noun", "a calf", "buzağı", 1),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "misr": G("misr", "مِصْر", None, "propn", "Egypt", "Mısır", 1),
 "balagha-exaggerate": G("balagha-exaggerate", "بَالَغَ", "ب ل غ", "verb", "to go to extremes (fī: in), to exaggerate (Form III)", "aşırıya gitmek, mübalağa etmek (müfâale)", 2),
 "taqdis": G("taqdis", "تَقْدِيس", "ق د س", "noun", "sanctifying (the maṣdar of Form II)", "kutsama, takdis (tef'îl masdarı)", 2),
 "uzayr": G("uzayr", "عُزَيْر", None, "propn", "ʿUzayr (Ezra)", "Üzeyr", 1),
 "tazim": G("tazim", "تَعْظِيم", "ع ظ م", "noun", "magnifying, veneration (the maṣdar of Form II)", "yüceltme, ta'zim (tef'îl masdarı)", 2),
 "hatta": G("hatta", "حَتَّى", None, "part", "until; even", "-e kadar; hatta", 1),
 "takhatta": G("takhatta", "تَخَطَّى", "خ ط و", "verb", "to step beyond, to overstep (Form V, defective)", "aşmak, ötesine geçmek (tefa''ul, nâkıs)", 2),
 "hadd": G("hadd", "حَدّ", "ح د د", "noun", "a limit, a bound", "sınır, had", 1, plural="حُدُود"),
 "bashariyya": G("bashariyya", "بَشَرِيَّة", "ب ش ر", "noun", "humanity, the human condition (an abstract nisba)", "beşeriyet, insanlık (masdar-ı sınâî)", 2),
 "balagha": G("balagha", "بَلَغَ", "ب ل غ", "verb", "to reach", "ulaşmak", 1),
 "waqaha": G("waqaha", "وَقَاحَة", "و ق ح", "noun", "impudence, shamelessness", "küstahlık, yüzsüzlük", 3),
 "an-masdariyya": G("an-masdariyya", "أَنْ", None, "part", "that — the an of naṣb", "… -mesi — nasb eden en", 1),
 "nasaba-attribute": G("nasaba-attribute", "نَسَبَ", "ن س ب", "verb", "to attribute (ilā: to)", "nispet etmek, isnat etmek", 2),
 "bad": G("bad", "بَعْض", "ب ع ض", "noun", "some, a part", "bazı, bir kısım", 1),
 "amal-work": G("amal-work", "عَمَل", "ع م ل", "noun", "a work, a deed", "iş, amel", 1, plural="أَعْمَال"),
 "shirk": G("shirk", "شِرْك", "ش ر ك", "noun", "shirk, associating partners with God", "şirk", 1),
 "wathaniyya": G("wathaniyya", "وَثَنِيَّة", "و ث ن", "noun", "idolatry, paganism (an abstract nisba)", "putperestlik (masdar-ı sınâî)", 2),
 "sihr": G("sihr", "سِحْر", "س ح ر", "noun", "sorcery, magic", "büyü, sihir", 1),
 "kufr": G("kufr", "كُفْر", "ك ف ر", "noun", "unbelief", "küfür", 1),
 "fil": G("fil", "فِعْل", "ف ع ل", "noun", "a deed, an act; a verb", "fiil, iş", 1, plural="أَفْعَال"),
 "shani": G("shani", "شَنِيع", "ش ن ع", "noun", "hideous, repugnant", "çirkin, iğrenç", 2),
 "lam": G("lam", "لَمْ", None, "part", "not (jussive, past)", "-madı (cezm eden lem)", 1),
 "ittaqa": G("ittaqa", "اِتَّقَى", "و ق ي", "verb", "to fear (God), to be wary of (Form VIII, defective)", "sakınmak, (Allah'tan) korkmak (iftiâl, nâkıs)", 1),
 "allah": G("allah", "الله", "أ ل ه", "propn", "God", "Allah", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "raghma": G("raghma", "رَغْمَ", "ر غ م", "noun", "despite, in spite of", "-e rağmen", 1),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "all, every", "her, hepsi", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "shadid": G("shadid", "شَدِيد", "ش د د", "noun", "intense, severe, strong", "şiddetli, güçlü", 1),
 "idlal": G("idlal", "إِدْلَال", "د ل ل", "noun", "boasting, presuming (bi: on) (the maṣdar of Form IV)", "böbürlenme, güvenip şımarma (if'âl masdarı)", 3),
 "nasab": G("nasab", "نَسَب", "ن س ب", "noun", "lineage", "soy, nesep", 1),
 "itimad": G("itimad", "اِعْتِمَاد", "ع م د", "noun", "reliance (ʿalā: on) (the maṣdar of Form VIII)", "güvenme, dayanma, itimat (iftiâl masdarı)", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "umniya": G("umniya", "أُمْنِيَّة", "م ن ي", "noun", "a wish, a vain hope", "kuruntu, temenni", 2, plural="أَمَانِيّ"),
 "hulm": G("hulm", "حُلْم", "ح ل م", "noun", "a dream", "rüya, hayal", 1, plural="أَحْلَام"),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "nahnu": G("nahnu", "نَحْنُ", None, "pron", "we", "biz", 1),
 "ibn": G("ibn", "ابْن", "ب ن ي", "noun", "a son", "oğul", 1, plural="أَبْنَاء"),
 "habib": G("habib", "حَبِيب", "ح ب ب", "noun", "beloved, dear", "sevgili, habib", 1, plural="أَحِبَّاء"),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
 "lan": G("lan", "لَنْ", None, "part", "will not (naṣb)", "-mayacak (nasb eden len)", 1),
 "massa": G("massa", "مَسَّ", "م س س", "verb", "to touch (doubled)", "dokunmak (muzâaf)", 1),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "nar": G("nar", "نَار", "ن و ر", "noun", "fire; the Fire", "ateş; cehennem", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "yawm": G("yawm", "يَوْم", "ي و م", "noun", "a day", "gün", 1, plural="أَيَّام"),
 "madud": G("madud", "مَعْدُود", "ع د د", "noun", "numbered, counted (a passive participle)", "sayılı (ism-i mef'ûl)", 2),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tasarraba", _sg.derived(_sg.B5, _sg.W5, "َ", "تَسَرَّب", "تَسَرَّب", "تَسَرَّب", "تَسَرُّب", "مُتَسَرِّب", None, None, None, "تَسَرَّبَ الْمَاءُ: سَالَ خُفْيَةً؛ وَتَسَرَّبَتِ الْعَقَائِدُ: دَخَلَتْ خُفْيَةً."))
put_morph(mo, "balagha-exaggerate", _sg.derived(_sg.B3, _sg.W3, "ُ", "بَالَغ", "بَالِغ", "بَالِغ", "مُبَالَغَة", "مُبَالِغ", "مُبَالَغ", "بُولِغَ", "يُبَالَغُ", "بَالَغَ فِي الْأَمْرِ: جَاوَزَ الْحَدَّ وَاجْتَهَدَ."))
put_morph(mo, "takhatta", _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَخَطَّ", "تَخَطّ", "a", "تَخَطّ", "تَخَطٍّ (التَّخَطِّي)", "مُتَخَطٍّ (الْمُتَخَطِّي)", "مُتَخَطًّى", "تُخُطِّيَ", "يُتَخَطَّى", "تَخَطَّى الشَّيْءَ: جَاوَزَهُ وَتَعَدَّاهُ — نَاقِصٌ: يَتَخَطَّى، لَمْ يَتَخَطَّ."))
put_morph(mo, "nasaba-attribute", _sg.sound1("nasara", "نَسَب", "نْسُب", "اُنْسُب", "نِسْبَة / نَسَب", "نَاسِب", "مَنْسُوب", "نُسِبَ", "يُنْسَبُ", "نَسَبَ الشَّيْءَ إِلَيْهِ: عَزَاهُ إِلَيْهِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch26 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 26 (print pp. 43–44; ʿĪsā §6–7): ingratitude — false creeds and pagan customs seeping in, the calf in Egypt, ʿUzayr deified, shirk and sorcery attributed to prophets (s1–s3); vainglory — boasting of lineage, «we are God's sons and His beloved» (5:18), «the Fire will touch us only for numbered days» (2:80) (s4–s6)."
ADD_TR = " Yirmi altıncı bölüm (baskı s. 43–44; Îsâ §6–7): nankörlük — sızan sahte akîdeler ve câhiliye âdetleri, Mısır'daki buzağı, ilâhlaştırılan Üzeyr, peygamberlere nispet edilen şirk ve büyü (s1–s3); kibir — soyla böbürlenme, «biz Allah'ın oğulları ve sevgilileriyiz» (5:18), «ateş bize sayılı günlerden başka dokunmayacak» (2:80) (s4–s6)."
write_out(26, S, TITLE, ADD_EN, ADD_TR, "ʿĪsā §6–7", GLOSS_ADD, notes=(), related=())
report(26, S, GLOSS_ADD, ())
