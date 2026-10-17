# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 18: «قِصَّةُ يُونُسَ وَحِكْمَتُهَا» — §4 (the story of Yūnus and its wisdom), §5 (Yūnus among his people, with 10:98);
print pp. 28–29.
python3 tools/authoring/author_qisas4_ch18.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "قِصَّةُ يُونُسَ وَحِكْمَتُهَا", "en": "The story of Yūnus and its wisdom", "tr": "Yûnus'un kıssası ve hikmeti"}
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

# ---------------------------------------------------------------- §4 قِصَّةُ يُونُسَ وَحِكْمَتُهَا (print p. 28)
sen("s1", "The story of Yūnus comes joined to the story of Ayyūb, supporting it in affirming the power of God Most High, His kindness to His servants and His coming to their rescue",
        "Yûnus'un kıssası Eyyûb'un kıssasına bitişik gelir; onu Allah Teâlâ'nın kudretini, kullarına lütfunu ve onların imdadına yetişmesini ispat etmekte destekler —", [
  tok("وَتَأْتِي", "ata", "verb", ["mudari-marfu", "naqis-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَتَأْتِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ.", "«and comes» — a defective muḍāriʿ; its ḍamma is estimated on the yāʾ.", "«ve gelir» — nâkıs muzari; dammesi yâ üzerinde takdirî.", segments=wa_("تَأْتِي", "ata", "verb")),
  tok("قِصَّةُ", "qissa", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the story [of]» — the doer, annexed.", "«kıssası» — fâil, muzâf."),
  tok("يُونُسَ", "yunus", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūnus» — jarr by fatḥa (a diptote).", "«Yûnus'un» — gayr-i munsarıf, fetha ile mecrûr."),
  hal("مَقْرُونَةً", "maqrun", "«joined»", "«bitişik»", tags=["ism-maful"]),
  tok("بِقِصَّةِ", "qissa", "noun", [HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَقِصَّةِ مَجْرُورٌ، مُضَافٌ.", "«to the story [of]»", "«kıssasına»", segments=[seg("بِ", "bi", "prep"), seg("قِصَّةِ", "qissa", "noun")]),
  tok("أَيُّوبَ", "ayyub", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Ayyūb»", "«Eyyûb'un»", punct="،"),
  hal("مُؤَيِّدَةً", "muayyid", "«supporting»", "«destekleyerek»", tags=["ism-fail"], ar="حَالٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  li_pron("لَهَا", "هَا", "pron-3fs", "«it»", "«onu»"),
  fi(), majrur("إِثْبَاتِ", "ithbat", "«affirming»", "«ispat etmekte»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("قُدْرَةِ", "qudra", "«the power [of]»", "«kudretini»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High» — a parenthetical prayer.", "«Teâlâ» — duâ cümlesi."),
  noun_pron("وَلُطْفِهِ", "lutf", "وَلُطْفِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَلُطْفِ مَعْطُوفٌ عَلَى قُدْرَةِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His kindness»", "«ve lütfunu»", tags=[AT, ID]),
  noun_pron("بِعِبَادِهِ", "abd", "بِعِبَادِ", "هِ", "pron-3ms", "الْبَاءُ حَرْفُ جَرٍّ، وَعِبَادِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to His servants»", "«kullarına»", tags=[HJ, ID, JT]),
  noun_pron("وَإِغَاثَتِهِ", "ighatha", "وَإِغَاثَتِ", "هِ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَإِغَاثَتِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and His coming to the rescue»", "«ve imdada yetişmesini»", tags=[AT, ID]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«of them»", "«onların»", punct="،"),
])
sen("s2", "when hope is cut off, and deadly despair and pitch darkness cover everything, and every outlet is blocked — no light, no air, no hope, no expectation —",
        "ümidin kesildiği, öldürücü ümitsizliğin ve zifirî karanlığın her yeri bürüdüğü, bütün menfezlerin tıkandığı an — ne ışık ne hava, ne ümit ne beklenti —", [
  tok("حِينَ", "hin", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "«when» — a time adverb annexed to the clause after it.", "«… zaman» — cümleye muzâf zaman zarfı."),
  mudari("يَنْقَطِعُ", "inqataa", "«is cut off»", "«kesilir»", tags=["form-vii-verbs"], hidden=None, extra_ar=""),
  fail("الرَّجَاءُ", "raja-hope", "«hope»", "«ümit»", punct="،"),
  mudari("وَيَغْشَى", "ghashiya", "«and covers»", "«ve bürür»", tags=[AT, "naqis-verbs"], hidden=None, extra_ar=" — مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ"),
  fail("الْيَأْسُ", "yas", "«despair»", "«ümitsizlik»"),
  naat("الْقَاتِلُ", "qatil", "«deadly»", "«öldürücü»", case="raf", tags=["ism-fail"]),
  atf("وَالظَّلَامُ", "zalam", "«darkness»", "«karanlık»", "raf"),
  naat("الْحَالِكُ", "halik", "«pitch-black»", "«zifirî»", case="raf", tags=["ism-fail"], punct="،"),
  mudari("وَتَنْسَدُّ", "insadda", "«and is blocked»", "«ve tıkanır»", tags=[AT, "form-vii-verbs", "doubled-verbs"], hidden=None),
  fail("جَمِيعُ", "jami", "«all [of]»", "«bütün»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الْمَنَافِذِ", "manfadh", "«the outlets»", "«menfezler»", tags=[JT], punct="،"),
  tok("فَلَا", "la-nafiya", "part", [AT, "la-nafiya-lil-jins"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "«so no» — the lā of the genus.", "«artık ne» — cins nefyeden lâ.", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  ism_la("نُورَ", "nur", "«light»", "«ışık»"),
  la_jins("وَلَا", wa=True),
  ism_la("هَوَاءَ", "hawa", "«air»", "«hava»", punct="،"),
  la_jins("وَلَا", wa=True),
  ism_la("أَمَلَ", "amal", "«hope»", "«ümit»"),
  la_jins("وَلَا", wa=True),
  ism_la("رَجَاءَ", "raja-hope", "«expectation»", "«beklenti»", punct="،"),
])
sen("s3", "the millstone of death turns, strong and swift, grinding the grain of life soft and fine.",
        "ölüm değirmeni güçlü ve hızlı döner; hayat tanesini ince ince, yumuşacık öğütür.", [
  mudari("تَدُورُ", "dara-turn", "«turns»", "«döner»", tags=["hollow-verbs"], hidden=None),
  tok("رَحَى", "raha", "noun", [FL, ID, "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ.", "«the millstone [of]» — the doer; a maqṣūr noun, its ḍamma estimated on the alif.", "«değirmeni» — fâil; maksûr isim, dammesi takdirî."),
  mudaf_ilayh("الْمَوْتِ", "mawt", "«death»", "«ölüm»"),
  hal("قَوِيَّةً", "qawi", "«strong»", "«güçlü»"),
  hal("سَرِيعَةً", "sari", "«swift»", "«hızlı»", ar="حَالٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ."),
  mudari("تَطْحَنُ", "tahana", "«grinding»", "«öğütür»", tags=[HL, MB], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ"),
  maful_("حَبَّةَ", "habba", "«the grain [of]»", "«tanesini»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ."),
  mudaf_ilayh("الْحَيَاةِ", "hayat", "«life»", "«hayat»"),
  hal("نَاعِمَةً", "naim-soft", "«soft»", "«yumuşacık»"),
  hal("دَقِيقَةً", "daqiq", "«fine»", "«ince»", ar="حَالٌ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", punct="."),
])
sen("s4", "There the hand of divine power stands forth — strong and overpowering, merciful and wise — and brings this weak human out of the jaws of the ravening lion and of ravaging death,",
        "İşte orada ilâhî kudretin eli belirir — güçlü ve kahredici, merhametli ve hikmetli — ve bu zayıf insanı yırtıcı aslanın çeneleri arasından, kıyıcı ölümün ağzından çıkarır;", [
  tok("هُنَالِكَ", "hunalika", "noun", [MF, "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ فِيهِ.", "«there» — a demonstrative of distant place, in the place of naṣb as adverb.", "«orada» — uzak mekân işâreti, mef'ûlün fîh."),
  mudari("تَبْرُزُ", "baraza", "«stands forth»", "«belirir»", hidden=None),
  fail("يَدُ", "yad", "«the hand [of]»", "«eli»", tags=[ID], extra_ar="، مُضَافٌ"),
  mudaf_ilayh("الْقُدْرَةِ", "qudra", "«power»", "«kudretin»"),
  naat("الْإِلٰهِيَّةِ", "ilahi", "«divine»", "«ilâhî»", tags=["ism-mansub"], punct="،"),
  tok("الْقَوِيَّةُ", "qawi", "noun", [NA], "نَعْتٌ لِيَدُ مَرْفُوعٌ بِالضَّمَّةِ.", "«strong» — the naʿt of «the hand».", "«güçlü» — «el»in sıfatı."),
  naat2("الْقَاهِرَةُ", "qahir", "«overpowering»", "«kahredici»", tags=["ism-fail"], punct="،"),
  naat2("الرَّحِيمَةُ", "rahim-merciful", "«merciful»", "«merhametli»", n="ثَالِثٌ", tags=["sifa-mushabbaha"]),
  naat2("الْحَكِيمَةُ", "hakim", "«wise»", "«hikmetli»", n="رَابِعٌ", tags=["sifa-mushabbaha"], punct="،"),
  tok("فَتُخْرِجُ", "akhraja", "verb", [AT, "mudari-marfu", "form-iv-verbs", MB], "الْفَاءُ عَاطِفَةٌ، وَتُخْرِجُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ.", "«and brings out» — the doer (the hand) is concealed.", "«ve çıkarır» — fâil gizli (el).", segments=[seg("فَ", "fa", "conj"), seg("تُخْرِجُ", "akhraja", "verb")]),
  ishara("هٰذَا", "hadha", "nasb", "«this»", "«bu»"),
  tok("الْإِنْسَانَ", "insan", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ (أَوْ عَطْفُ بَيَانٍ).", "«human» — a badal of the demonstrative.", "«insanı» — ism-i işâretten bedel."),
  naat("الضَّعِيفَ", "daif", "«weak»", "«zayıf»", case="nasb", tags=["sifa-mushabbaha"]),
  prep("مِنْ", "min", "«out of»", "«-den»"),
  majrur("أَشْدَاقِ", "shidq", "«the jaws [of]»", "«çeneleri»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  mudaf_ilayh("الْأَسَدِ", "asad", "«the lion»", "«aslanın»"),
  tok("الضَّارِي", "dari", "noun", [NA, "ism-maqsur-manqus", "ism-fail"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.", "«ravening» — the naʿt; a manqūṣ noun, its kasra estimated on the yāʾ.", "«yırtıcı» — sıfat; mankûs isim, kesresi takdirî."),
  atf("وَالْمَوْتِ", "mawt", "«death»", "«ölüm»", "jarr"),
  naat("الْفَاتِكِ", "fatik", "«ravaging»", "«kıyıcı»", tags=["ism-fail"], punct="،"),
])
sen("s5", "and he comes out sound, not scratched, whole, not diminished — as though he had been on his bed in his house, kept safe among his family.",
        "o da sapasağlam, çizik bile almadan, eksiksiz çıkar — sanki evinde, yatağında, ailesi arasında korunmuş gibi.", [
  tok("فَيَخْرُجُ", "kharaja", "verb", [AT, "mudari-marfu"], "الْفَاءُ عَاطِفَةٌ، وَيَخْرُجُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and he comes out»", "«o da çıkar»", segments=[seg("فَ", "fa", "conj"), seg("يَخْرُجُ", "kharaja", "verb")]),
  hal("سَلِيمًا", "salim-sound", "«sound»", "«sapasağlam»", tags=["sifa-mushabbaha"]),
  tok("غَيْرَ", "ghayr", "noun", [HL, ID], "حَالٌ ثَانٍ مَنْصُوبٌ، مُضَافٌ.", "«not» (lit. other than) — a second ḥāl, annexed.", "«… olmaksızın» — ikinci hâl, muzâf."),
  mudaf_ilayh("مَخْدُوشٍ", "makhdush", "«scratched»", "«çizilmiş»", tags=["ism-maful"], punct="،"),
  hal("كَامِلًا", "kamil", "«whole»", "«eksiksiz»", tags=["ism-fail"]),
  tok("غَيْرَ", "ghayr", "noun", [HL, ID], "حَالٌ مَنْصُوبٌ، مُضَافٌ.", "«not»", "«… olmaksızın»"),
  mudaf_ilayh("مَنْقُوصٍ", "manqus", "«diminished»", "«eksiltilmiş»", tags=["ism-maful"], punct="،"),
  tok("كَأَنَّمَا", "ka-annama", "part", [IW, "innama-kaffa"], "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ كُفَّ عَنِ الْعَمَلِ بِمَا الْكَافَّةِ.", "«as though» — kaʾanna made inoperative by the restraining mā.", "«sanki» — keenne, kâffe mâ ile amelden düşmüş.", segments=[seg("كَأَنَّ", "ka-anna", "part"), seg("مَا", "ma-kaffa", "part")]),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا مُسْتَتِرٌ: هُوَ.", "«he had been» — kāna; its ism is concealed.", "«idi» — kâne; ismi gizli."),
  prep("عَلَى", "ala", "«on»", "«-de»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  noun_pron("فِرَاشِهِ", "firash", "فِرَاشِ", "هِ", "pron-3ms", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his bed»", "«yatağında»", tags=[HJ, ID, KN]),
  fi(), noun_pron("بَيْتِهِ", "bayt", "بَيْتِ", "هِ", "pron-3ms", "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his house»", "«evinde»", tags=[HJ, ID]),
  hal("مَحْفُوظًا", "mahfuz", "«kept safe»", "«korunmuş»", tags=["ism-maful"]),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«among»", "«arasında»"),
  noun_pron("أَهْلِهِ", "ahl", "أَهْلِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his family»", "«ailesi»", tags=[ID], punct="."),
])
# ---------------------------------------------------------------- §5 يُونُسُ بَيْنَ قَوْمِهِ (print p. 29)
sen("s6", "This is the story of Yūnus: God sent him to the people of the town of Nineveh; he called them to God Most High, but they refused him and persisted in their unbelief;",
        "İşte Yûnus'un kıssası: Allah onu Ninova şehrinin halkına gönderdi; onları Allah Teâlâ'ya çağırdı; onlar ise ona karşı çıktılar ve küfürlerinde direndiler;", [
  tok("وَهٰذِهِ", "hadhihi", "pron", [MK, "asma-al-ishara"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذِهِ اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "«and this» — the mubtadaʾ.", "«ve işte bu» — mübtedâ.", segments=wa_("هٰذِهِ", "hadhihi", "pron")),
  tok("قِصَّةُ", "qissa", "noun", [MK, ID], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the story [of]» — the khabar.", "«kıssası» — haber."),
  tok("يُونُسَ", "yunus", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūnus»", "«Yûnus'un»", punct=":"),
  v_pron("بَعَثَهُ", "baatha", "بَعَثَ", "هُ", "pron-3ms", "«sent him»", "«onu gönderdi»", hidden=None),
  allah_fail(),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("أَهْلِ", "ahl", "«the people [of]»", "«halkına»", tags=[ID], ar="مَجْرُورٌ بِإِلَى، مُضَافٌ."),
  mudaf_ilayh("قَرْيَةِ", "qarya", "«the town [of]»", "«şehrinin»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("نِينَوَى", "ninawa", "propn", [ID, MM, "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — عَلَمٌ أَعْجَمِيٌّ مَقْصُورٌ.", "«Nineveh» — a foreign maqṣūr name; its kasra is estimated on the alif.", "«Ninova» — yabancı maksûr özel isim; kesresi takdirî.", punct="،"),
  tok("فَدَعَاهُمْ", "daa", "verb", [AT, MB, "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَدَعَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَهُمْ مَفْعُولٌ بِهِ.", "«and he called them» — a defective māḍī; the pronoun is its object.", "«onları çağırdı» — nâkıs mâzî; zamir mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("دَعَا", "daa", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى.", "«God»", "«Allah'a»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct="،"),
  mazi_wa_alif("فَأَبَوْا", "aba", "«but they refused»", "«onlar ise karşı çıktılar»", fa=True),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«him»", "«ona»", punct="،"),
  mazi_wa_alif("وَتَمَادَوْا", "tamada", "«and persisted»", "«ve direndiler»", wa=True, tags=["form-vi-verbs"]),
  fi(), noun_pron("كُفْرِهِمْ", "kufr", "كُفْرِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِفِي، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their unbelief»", "«küfürlerinde»", tags=[HJ, ID], punct="،"),
])
sen("s7", "so he went out from among them, angry at them, and promised them the punishment after three [days].",
        "o da onlara kızgın olarak aralarından çıktı ve üç gün sonra azabın geleceğini onlara vaat etti.", [
  mazi("فَخَرَجَ", "kharaja", "«so he went out»", "«o da çıktı»", tags=[AT], wa=True, hidden="هُوَ"),
  prep("مِنْ", "min", "«from»", "«-den»"),
  majrur("بَيْنِ", "bayna", "«among»", "«arasından»", tags=[ID], ar="ظَرْفٌ مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  noun_pron("أَظْهُرِهِمْ", "zahr", "أَظْهُرِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — مِنْ بَيْنِ أَظْهُرِهِمْ: مِنْ وَسَطِهِمْ.", "«their midst» (lit. their backs)", "«aralarından» (lafzen: sırtları)", tags=[ID, JT]),
  hal("مُغَاضِبًا", "mughadib", "«angry»", "«kızgın olarak»", tags=["ism-fail", "form-iii-verbs"]),
  li_pron("لَهُمْ", "هُمْ", "pron-3mp", "«at them»", "«onlara»", punct="،"),
  v_pron("وَوَعَدَهُمْ", "waada", "وَعَدَ", "هُمْ", "pron-3mp", "«and promised them»", "«ve onlara vaat etti»", wa=True, tags=["mithal-verbs"]),
  tok("بِالْعَذَابِ", "adhab", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْعَذَابِ مَجْرُورٌ.", "«the punishment»", "«azabı»", segments=[seg("بِ", "bi", "prep"), seg("الْعَذَابِ", "adhab", "noun")]),
  tok("بَعْدَ", "bada", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ.", "«after»", "«sonra»"),
  mudaf_ilayh("ثَلَاثٍ", "thalath", "«three [days]»", "«üç [gün]»", punct="،", ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَيْ: ثَلَاثِ لَيَالٍ."),
])
sen("s8", "When they made sure of that from him, and knew that a prophet does not lie, they went out to the desert with their children, their cattle and their flocks, and separated the mothers from their young;",
        "Bunu ondan iyice anlayıp peygamberin yalan söylemeyeceğini bilince, çocukları, davarları ve sürüleriyle çöle çıktılar; anneleri yavrularından ayırdılar;", [
  tok("فَلَمَّا", "lamma", "part", [AT, MF, SH], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — the ẓarf lammā, with the sense of a condition.", "«… -ınca» — şart mânâlı lemmâ.", segments=[seg("فَ", "fa", "conj"), seg("لَمَّا", "lamma", "part")]),
  mazi_pl("تَحَقَّقُوا", "tahaqqaqa", "«they made sure»", "«iyice anladılar»", tags=["form-v-verbs"]),
  prep_pron("مِنْهُ", "min", "هُ", "pron-3ms", "«from him»", "«ondan»"),
  ishara("ذٰلِكَ", "dhalika", "nasb", "«of that»", "«bunu»"),
  mazi_pl("وَعَلِمُوا", "alima", "«and knew»", "«ve bildiler»", wa=True, tags=[AT, MB]),
  tok("أَنَّ", "anna", "part", [IW], "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَلِمَ.", "«that» — the clause stands for ʿalima's two objects.", "«… -diğini» — müevvel masdar alime'nin iki mef'ûlü yerinde."),
  ism_inna("النَّبِيَّ", "nabi", "«a prophet»", "«peygamberin»", part="أَنَّ"),
  la_nafiya(),
  neg_mudari("يَكْذِبُ", "kadhaba", "«does … lie»", "«yalan söylemez»", hidden="هُوَ", extra=" — وَالْجُمْلَةُ خَبَرُ أَنَّ", tags=[IW], punct="،"),
  mazi_pl("خَرَجُوا", "kharaja", "«they went out»", "«çıktılar»", tags=[SH]),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("الصَّحْرَاءِ", "sahra", "«the desert»", "«çöle»", tags=[MM], ar="مَجْرُورٌ بِإِلَى، وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ لِأَنَّهُ مُعَرَّفٌ بِأَلْ — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ."),
  noun_pron("بِأَطْفَالِهِمْ", "tifl", "بِأَطْفَالِ", "هِمْ", "pron-3mp", "الْبَاءُ حَرْفُ جَرٍّ، وَأَطْفَالِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«with their children»", "«çocuklarıyla»", tags=[HJ, ID, JT]),
  noun_pron("وَأَنْعَامِهِمْ", "anam", "وَأَنْعَامِ", "هِمْ", "pron-3mp", "الْوَاوُ عَاطِفَةٌ، وَأَنْعَامِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«and their cattle»", "«ve davarlarıyla»", tags=[AT, ID]),
  noun_pron("وَمَوَاشِيهِمْ", "mashiya", "وَمَوَاشِي", "هِمْ", "pron-3mp", "الْوَاوُ عَاطِفَةٌ، وَمَوَاشِي مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«and their flocks» — a manqūṣ plural, its kasra estimated.", "«ve sürüleriyle» — mankûs cemi, kesresi takdirî.", tags=[AT, ID, JT, "ism-maqsur-manqus"], punct="،"),
  mazi_pl("وَفَرَّقُوا", "farraqa", "«and separated»", "«ve ayırdılar»", wa=True, tags=[AT, "form-ii-verbs"]),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفُ مَكَانٍ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasını»"),
  mudaf_ilayh("الْأُمَّهَاتِ", "umm", "«the mothers»", "«anneler»", tags=[JM]),
  noun_pron("وَأَوْلَادِهَا", "walad", "وَأَوْلَادِ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَأَوْلَادِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their young»", "«ve yavruları»", tags=[AT, ID, JT], punct="،"),
])
sen("s9", "then they humbled themselves before God, Mighty and Majestic, and cried out to Him; the camels and their calves groaned, the cows and their calves lowed, the sheep and their lambs bleated;",
        "sonra Aziz ve Celîl olan Allah'a yalvardılar, O'na feryat ettiler; develer ve yavruları böğürdü, inekler ve buzağıları böğürdü, koyunlar ve kuzuları meledi;", [
  tok("ثُمَّ", "thumma", "part", [AT], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then»", "«sonra»"),
  mazi_pl("تَضَرَّعُوا", "tadarraa", "«they humbled themselves»", "«yalvardılar»", tags=["form-v-verbs"]),
  prep("إِلَى", "ila", "«before»", "«-e»"),
  tok("اللهِ", "allah", "propn", [HJ], "لَفْظُ الْجَلَالَةِ مَجْرُورٌ بِإِلَى.", "«God»", "«Allah'a»"),
  mazi("عَزَّ", "azza-mighty", "«Mighty»", "«Aziz»", tags=["doubled-verbs", NA], hidden="هُوَ", extra_ar=" — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ"),
  mazi("وَجَلَّ", "jalla", "«and Majestic»", "«ve Celîl»", tags=[AT, "doubled-verbs"], wa=True, hidden="هُوَ", punct="،"),
  mazi_pl("وَجَأَرُوا", "jaara", "«and cried out»", "«ve feryat ettiler»", wa=True, tags=[AT]),
  prep_pron("إِلَيْهِ", "ila", "هِ", "pron-3ms", "«to Him»", "«O'na»", punct="،"),
  mazi_ta_naqis("وَرَغَتِ", "ragha", "«and groaned»", "«ve böğürdü»"),
  fail("الْإِبِلُ", "ibil", "«the camels»", "«develer»", tags=[]),
  noun_pron("وَفُصْلَانُهَا", "fasil", "وَفُصْلَانُ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَفُصْلَانُ مَعْطُوفٌ عَلَى الْفَاعِلِ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their calves»", "«ve yavruları»", tags=[AT, ID, JT], punct="،"),
  tok("وَخَارَتِ", "khara", "verb", [AT, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَخَارَتْ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and lowed» — a hollow māḍī; the tāʾ takes a kasra before the next hamzat al-waṣl.", "«ve böğürdü» — ecvef mâzî; tâ iki sâkin yüzünden kesre aldı.", segments=wa_("خَارَتِ", "khara", "verb")),
  fail("الْبَقَرُ", "baqar", "«the cows»", "«inekler»", tags=[]),
  noun_pron("وَأَوْلَادُهَا", "walad", "وَأَوْلَادُ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَأَوْلَادُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their calves»", "«ve buzağıları»", tags=[AT, ID, JT], punct="،"),
  mazi_ta_naqis("وَثَغَتِ", "thagha", "«and bleated»", "«ve meledi»"),
  fail("الْغَنَمُ", "ghanam", "«the sheep»", "«koyunlar»", tags=[]),
  noun_pron("وَسِخَالُهَا", "sakhla", "وَسِخَالُ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَسِخَالُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their lambs»", "«ve kuzuları»", tags=[AT, ID, JT], punct="،"),
])
sen("s10", "so God lifted the punishment from them. God Most High said:",
        "bunun üzerine Allah azabı onlardan kaldırdı. Allah Teâlâ buyurdu ki:", [
  mazi("فَرَفَعَ", "rafaa", "«so lifted»", "«bunun üzerine kaldırdı»", tags=[AT, MB], wa=True, hidden=None),
  allah_fail(),
  prep_pron("عَنْهُمُ", "an", "هُمُ", "pron-3mp", "«from them»", "«onlardan»", extra_ar="، وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ"),
  maful_("الْعَذَابَ", "adhab", "«the punishment»", "«azabı»", punct="،"),
  qala(hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«Most High»", "«Teâlâ»", punct=":"),
])
sen("s11", "«Why was there not a town that believed, so that its faith profited it — except the people of Yūnus: when they believed, We removed from them the punishment of disgrace in the life of this world, and gave them enjoyment for a while» (10:98).",
        "«Keşke iman edip de imanı kendisine fayda veren bir şehir halkı olsaydı! Yalnız Yûnus'un kavmi: iman edince dünya hayatında rezillik azabını onlardan kaldırdık ve onları bir süreye kadar faydalandırdık» (10:98).", [
  *quran([
  tok("فَلَوْلَا", "lawla", "part", [AT, "hadhf-wa-taqdir"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَلَوْلَا هُنَا لِلتَّحْضِيضِ (بِمَعْنَى هَلَّا) — تَخْتَصُّ بِالْفِعْلِ.", "«why not» — here lawlā is the lawlā of urging (= hallā), tied to a verb.", "«keşke … olsaydı / neden … olmadı» — tahdîd lemmâsı (hellâ mânâsında).", segments=[seg("فَ", "fa", "conj"), seg("لَوْلَا", "lawla", "part")]),
  tok("كَانَتْ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ تَامٌّ (بِمَعْنَى وُجِدَتْ)، وَالتَّاءُ لِلتَّأْنِيثِ.", "«there was» — kāna as a full verb (= existed).", "«oldu / var oldu» — tam kâne."),
  fail("قَرْيَةٌ", "qarya", "«a town»", "«bir şehir [halkı]»", extra_ar=" — عَلَى أَنَّ كَانَ تَامَّةٌ"),
  mazi_ta("آمَنَتْ", "aamana", "«that believed»", "«iman eden»", tags=["jumla-sifa", "form-iv-verbs"], extra=" — وَالْجُمْلَةُ نَعْتٌ لِقَرْيَةٍ"),
  tok("فَنَفَعَهَا", "nafaa", "verb", [AT, MB], "الْفَاءُ عَاطِفَةٌ، وَنَفَعَ فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ مُقَدَّمٌ.", "«so that profited it» — the pronoun is the object, fronted.", "«de ona fayda verdi» — zamir öne alınmış mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("نَفَعَ", "nafaa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  noun_pron("إِيمَانُهَا", "iman", "إِيمَانُ", "هَا", "pron-3fs", "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its faith» — the doer, delayed.", "«imanı» — fâil, sonraya bırakılmış.", tags=[FL, ID]),
  tok("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ — وَالِاسْتِثْنَاءُ مُنْقَطِعٌ عِنْدَ الْأَكْثَرِ.", "«except» — the tool of exception; the exception is disjoined (munqaṭiʿ) for most grammarians.", "«ancak» — istisnâ edatı; istisnâ-i munkatı'."),
  tok("قَوْمَ", "qawm", "noun", ["istithna", ID], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "«the people [of]» — the mustathnā, in naṣb.", "«kavmi» — müstesnâ, mansub."),
  tok("يُونُسَ", "yunus", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Yūnus»", "«Yûnus'un»"),
  tok("لَمَّا", "lamma", "part", [MF, SH], "ظَرْفٌ بِمَعْنَى حِينَ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when»", "«… -ınca»"),
  mazi_pl("آمَنُوا", "aamana", "«they believed»", "«iman ettiler»", tags=["form-iv-verbs"]),
  tok("كَشَفْنَا", "kashafa", "verb", [SH, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — جَوَابُ لَمَّا.", "«We removed» — the answer of lammā; nā is the doer.", "«kaldırdık» — lemmâ'nın cevabı; nâ fâil.", segments=[seg("كَشَفْ", "kashafa", "verb"), seg("نَا", "pron-1p", "pron")]),
  prep_pron("عَنْهُمْ", "an", "هُمْ", "pron-3mp", "«from them»", "«onlardan»"),
  maful_("عَذَابَ", "adhab", "«the punishment [of]»", "«azabını»", tags=[ID], ar="مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ."),
  mudaf_ilayh("الْخِزْيِ", "khizy", "«disgrace»", "«rezillik»"),
  fi(), majrur("الْحَيَاةِ", "hayat", "«the life»", "«hayatında»"),
  tok("الدُّنْيَا", "dunya", "noun", [NA, "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "«of this world» — the naʿt; a maqṣūr noun.", "«dünya» — sıfat; maksûr isim."),
  tok("وَمَتَّعْنَاهُمْ", "mattaa", "verb", [AT, MB, "form-ii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَمَتَّعْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَهُمْ مَفْعُولٌ بِهِ.", "«and We gave them enjoyment» — nā the doer, hum the object.", "«ve onları faydalandırdık» — nâ fâil, hüm mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("مَتَّعْ", "mattaa", "verb"), seg("نَا", "pron-1p", "pron"), seg("هُمْ", "pron-3mp", "pron")]),
  prep("إِلَى", "ila", "«for» (lit. until)", "«-e kadar»"),
  majrur("حِينٍ", "hin", "«a while»", "«bir süre»", punct="."),
  ]),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: raja-hope, dara-turn, naim-soft, rahim-merciful take suffixed keys; hin/hawa/hakim/subhan/ka-anna reused)
CAND = {
 "ata": G("ata", "أَتَى", "أ ت ي", "verb", "to come", "gelmek", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "yunus": G("yunus", "يُونُس", None, "propn", "Yūnus (Jonah)", "Yûnus", 1),
 "maqrun": G("maqrun", "مَقْرُون", "ق ر ن", "noun", "joined, coupled (a passive participle)", "bitişik, birleştirilmiş (ism-i mef'ûl)", 3),
 "ayyub": G("ayyub", "أَيُّوب", None, "propn", "Ayyūb (Job)", "Eyyûb", 1),
 "muayyid": G("muayyid", "مُؤَيِّد", "أ ي د", "noun", "supporting, confirming (an active participle of Form II)", "destekleyen, teyit eden (tef'îl ism-i fâili)", 3),
 "ithbat": G("ithbat", "إِثْبَات", "ث ب ت", "noun", "affirming, establishing (the maṣdar of Form IV)", "ispat (if'âl masdarı)", 2),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "power, ability", "kudret", 1),
 "allah": G("allah", "الله", None, "propn", "God", "Allah", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "to be exalted", "yüce olmak", 1),
 "lutf": G("lutf", "لُطْف", "ل ط ف", "noun", "kindness, gentleness", "lütuf", 2),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant", "kul", 1, plural="عِبَاد"),
 "ighatha": G("ighatha", "إِغَاثَة", "غ و ث", "noun", "coming to the rescue, succour (the maṣdar of Form IV)", "imdada yetişme, yardım (if'âl masdarı)", 3),
 "hin": G("hin", "حِين", "ح ي ن", "noun", "a time, a while; when (as a ẓarf)", "zaman, vakit; -dığı zaman (zarf)", 1),
 "inqataa": G("inqataa", "اِنْقَطَعَ", "ق ط ع", "verb", "to be cut off (Form VII)", "kesilmek (infiâl)", 2),
 "raja-hope": G("raja-hope", "رَجَاء", "ر ج و", "noun", "hope, expectation", "ümit, beklenti", 2),
 "ghashiya": G("ghashiya", "غَشِيَ", "غ ش ي", "verb", "to cover, to overwhelm (defective)", "bürümek, kaplamak (nâkıs)", 2),
 "yas": G("yas", "يَأْس", "ي أ س", "noun", "despair", "ümitsizlik", 2),
 "qatil": G("qatil", "قَاتِل", "ق ت ل", "noun", "deadly, killing (an active participle)", "öldürücü (ism-i fâil)", 2),
 "zalam": G("zalam", "ظَلَام", "ظ ل م", "noun", "darkness", "karanlık", 1),
 "halik": G("halik", "حَالِك", "ح ل ك", "noun", "pitch-black (an active participle)", "zifirî, kapkara (ism-i fâil)", 3),
 "insadda": G("insadda", "اِنْسَدَّ", "س د د", "verb", "to be blocked, stopped up (Form VII, doubled)", "tıkanmak (infiâl, muzâaf)", 3),
 "jami": G("jami", "جَمِيع", "ج م ع", "noun", "all, the whole", "bütün, hepsi", 1),
 "manfadh": G("manfadh", "مَنْفَذ", "ن ف ذ", "noun", "an outlet, a way through", "menfez, çıkış yolu", 3, plural="مَنَافِذ"),
 "la-nafiya": G("la-nafiya", "لَا", None, "part", "no, not", "yok, değil", 1),
 "nur": G("nur", "نُور", "ن و ر", "noun", "light", "ışık, nur", 1),
 "hawa": G("hawa", "هَوَاء", "ه و ي", "noun", "air", "hava", 1),
 "amal": G("amal", "أَمَل", "أ م ل", "noun", "hope", "ümit, emel", 1),
 "dara-turn": G("dara-turn", "دَارَ", "د و ر", "verb", "to turn, to revolve (hollow)", "dönmek (ecvef)", 2),
 "raha": G("raha", "رَحًى", "ر ح ي", "noun", "a millstone (a maqṣūr noun)", "değirmen taşı (maksûr isim)", 3),
 "mawt": G("mawt", "مَوْت", "م و ت", "noun", "death", "ölüm", 1),
 "qawi": G("qawi", "قَوِيّ", "ق و ي", "noun", "strong", "güçlü", 1),
 "sari": G("sari", "سَرِيع", "س ر ع", "noun", "swift, quick", "hızlı", 1),
 "tahana": G("tahana", "طَحَنَ", "ط ح ن", "verb", "to grind", "öğütmek", 3),
 "habba": G("habba", "حَبَّة", "ح ب ب", "noun", "a grain, a seed", "tane, tohum", 2),
 "hayat": G("hayat", "حَيَاة", "ح ي ي", "noun", "life", "hayat", 1),
 "naim-soft": G("naim-soft", "نَاعِم", "ن ع م", "noun", "soft, fine, smooth (an active participle)", "yumuşak, ince (ism-i fâil)", 3),
 "daqiq": G("daqiq", "دَقِيق", "د ق ق", "noun", "fine, minute; flour", "ince; un", 2),
 "hunalika": G("hunalika", "هُنَالِكَ", None, "noun", "there (a demonstrative of distant place)", "orada, işte orada (uzak mekân işâreti)", 2),
 "baraza": G("baraza", "بَرَزَ", "ب ر ز", "verb", "to stand forth, to appear", "belirmek, ortaya çıkmak", 2),
 "yad": G("yad", "يَد", "ي د ي", "noun", "a hand", "el", 1),
 "ilahi": G("ilahi", "إِلٰهِيّ", "أ ل ه", "noun", "divine (a nisba)", "ilâhî (nisbet)", 2),
 "qahir": G("qahir", "قَاهِر", "ق ه ر", "noun", "overpowering, subduing (an active participle)", "kahredici, kahhâr (ism-i fâil)", 2),
 "rahim-merciful": G("rahim-merciful", "رَحِيم", "ر ح م", "noun", "merciful (an adjective)", "merhametli (sıfat)", 1),
 "hakim": G("hakim", "حَكِيم", "ح ك م", "noun", "wise", "hakîm, hikmetli", 1),
 "akhraja": G("akhraja", "أَخْرَجَ", "خ ر ج", "verb", "to bring out (Form IV)", "çıkarmak (if'âl)", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this", "bu", 1),
 "insan": G("insan", "إِنْسَان", "أ ن س", "noun", "a human being", "insan", 1),
 "daif": G("daif", "ضَعِيف", "ض ع ف", "noun", "weak", "zayıf", 1),
 "min": G("min", "مِنْ", None, "prep", "from, of", "-den", 1),
 "shidq": G("shidq", "شِدْق", "ش د ق", "noun", "the corner of the mouth; (pl.) the jaws", "ağız kenarı; (ç.) çeneler", 4, plural="أَشْدَاق"),
 "asad": G("asad", "أَسَد", "أ س د", "noun", "a lion", "aslan", 1),
 "dari": G("dari", "ضَارٍ", "ض ر و", "noun", "ravening, fierce (of a beast; a manqūṣ participle)", "yırtıcı, kana alışmış (mankûs ism-i fâil)", 4),
 "fatik": G("fatik", "فَاتِك", "ف ت ك", "noun", "ravaging, murderous (an active participle)", "kıyıcı, öldürücü (ism-i fâil)", 4),
 "kharaja": G("kharaja", "خَرَجَ", "خ ر ج", "verb", "to go out", "çıkmak", 1),
 "salim-sound": G("salim-sound", "سَلِيم", "س ل م", "noun", "sound, unharmed", "sağlam, sâlim", 2),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than; not", "başka; gayri, -sız", 1),
 "makhdush": G("makhdush", "مَخْدُوش", "خ د ش", "noun", "scratched (a passive participle)", "çizilmiş (ism-i mef'ûl)", 4),
 "kamil": G("kamil", "كَامِل", "ك م ل", "noun", "whole, complete", "tam, eksiksiz", 1),
 "manqus": G("manqus", "مَنْقُوص", "ن ق ص", "noun", "diminished, lacking (a passive participle)", "eksiltilmiş, noksan (ism-i mef'ûl)", 3),
 "ka-annama": G("ka-annama", "كَأَنَّمَا", None, "part", "as though (kaʾanna + the restraining mā)", "sanki (keenne + kâffe mâ)", 2),
 "ka-anna": G("ka-anna", "كَأَنَّ", None, "part", "as if", "sanki", 1),
 "ma-kaffa": G("ma-kaffa", "مَا (الْكَافَّة)", None, "part", "the restraining mā", "kâffe mâ", 2),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "ala": G("ala", "عَلَى", None, "prep", "on", "üzerine", 1),
 "firash": G("firash", "فِرَاش", "ف ر ش", "noun", "a bed", "yatak, döşek", 2),
 "bayt": G("bayt", "بَيْت", "ب ي ت", "noun", "a house", "ev", 1),
 "mahfuz": G("mahfuz", "مَحْفُوظ", "ح ف ظ", "noun", "kept safe, guarded (a passive participle)", "korunmuş, mahfuz (ism-i mef'ûl)", 2),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between, among", "arasında", 1),
 "ahl": G("ahl", "أَهْل", "أ ه ل", "noun", "family; people", "aile; halk", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (f.)", "bu", 1),
 "baatha": G("baatha", "بَعَثَ", "ب ع ث", "verb", "to send", "göndermek", 1),
 "ila": G("ila", "إِلَى", None, "prep", "to", "-e", 1),
 "qarya": G("qarya", "قَرْيَة", "ق ر ي", "noun", "a town, a village", "şehir, köy", 1),
 "ninawa": G("ninawa", "نِينَوَى", None, "propn", "Nineveh", "Ninova", 2),
 "daa": G("daa", "دَعَا", "د ع و", "verb", "to call (defective)", "çağırmak (nâkıs)", 1),
 "aba": G("aba", "أَبَى", "أ ب ي", "verb", "to refuse (defective)", "kabul etmemek, direnmek (nâkıs)", 2),
 "tamada": G("tamada", "تَمَادَى", "م د ي", "verb", "to persist, to go on (Form VI, defective)", "direnmek, ısrar etmek (tefâul, nâkıs)", 3),
 "fi": G("fi", "فِي", None, "prep", "in", "-de", 1),
 "kufr": G("kufr", "كُفْر", "ك ف ر", "noun", "unbelief", "küfür", 1),
 "zahr": G("zahr", "ظَهْر", "ظ ه ر", "noun", "a back; (مِنْ بَيْنِ أَظْهُرِهِمْ) from their midst", "sırt; (aralarından)", 2, plural="أَظْهُر"),
 "mughadib": G("mughadib", "مُغَاضِب", "غ ض ب", "noun", "angry, in anger (an active participle of Form III)", "kızgın, öfkeli (mufâale ism-i fâili)", 3),
 "waada": G("waada", "وَعَدَ", "و ع د", "verb", "to promise", "vaat etmek", 1),
 "adhab": G("adhab", "عَذَاب", "ع ذ ب", "noun", "punishment", "azap", 1),
 "bada": G("bada", "بَعْدَ", "ب ع د", "noun", "after", "sonra", 1),
 "thalath": G("thalath", "ثَلَاث", "ث ل ث", "noun", "three (with a feminine counted noun)", "üç (müennes ma'dûd ile)", 1),
 "lamma": G("lamma", "لَمَّا", None, "part", "when — the ẓarf of a past condition", "-ınca, -dığı zaman", 1),
 "tahaqqaqa": G("tahaqqaqa", "تَحَقَّقَ", "ح ق ق", "verb", "to make sure, to verify (Form V)", "iyice anlamak, emin olmak (tefa''ul)", 2),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o", 1),
 "alima": G("alima", "عَلِمَ", "ع ل م", "verb", "to know", "bilmek", 1),
 "anna": G("anna", "أَنَّ", None, "part", "that", "-dığını", 1),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "kadhaba": G("kadhaba", "كَذَبَ", "ك ذ ب", "verb", "to lie", "yalan söylemek", 1),
 "sahra": G("sahra", "صَحْرَاء", "ص ح ر", "noun", "a desert (a diptote, by the long feminine alif)", "çöl (memdûde te'nis elifi ile gayr-i munsarıf)", 2),
 "tifl": G("tifl", "طِفْل", "ط ف ل", "noun", "a child", "çocuk", 1, plural="أَطْفَال"),
 "anam": G("anam", "أَنْعَام", "ن ع م", "noun", "cattle, livestock", "davar, hayvanlar (en'âm)", 2),
 "mashiya": G("mashiya", "مَاشِيَة", "م ش ي", "noun", "livestock, a flock", "sürü, davar", 3, plural="مَوَاشٍ"),
 "farraqa": G("farraqa", "فَرَّقَ", "ف ر ق", "verb", "to separate (Form II)", "ayırmak (tef'îl)", 2),
 "umm": G("umm", "أُمّ", "أ م م", "noun", "a mother", "anne", 1, plural="أُمَّهَات"),
 "walad": G("walad", "وَلَد", "و ل د", "noun", "a child; (of animals) young", "evlât, çocuk; yavru", 1, plural="أَوْلَاد"),
 "thumma": G("thumma", "ثُمَّ", None, "part", "then", "sonra", 1),
 "tadarraa": G("tadarraa", "تَضَرَّعَ", "ض ر ع", "verb", "to humble oneself in supplication (Form V)", "yalvarmak, tazarru etmek (tefa''ul)", 3),
 "azza-mighty": G("azza-mighty", "عَزَّ", "ع ز ز", "verb", "to be mighty (doubled)", "aziz olmak (muzâaf)", 2),
 "jalla": G("jalla", "جَلَّ", "ج ل ل", "verb", "to be majestic (doubled)", "celîl olmak (muzâaf)", 2),
 "jaara": G("jaara", "جَأَرَ", "ج أ ر", "verb", "to cry out loudly (in supplication)", "feryat etmek, yüksek sesle yalvarmak", 4),
 "ragha": G("ragha", "رَغَا", "ر غ و", "verb", "to groan (of a camel; defective)", "böğürmek (deve; nâkıs)", 4),
 "ibil": G("ibil", "إِبِل", "أ ب ل", "noun", "camels (a collective noun)", "develer (ism-i cem')", 2),
 "fasil": G("fasil", "فَصِيل", "ف ص ل", "noun", "a weaned camel-calf", "sütten kesilmiş deve yavrusu", 4, plural="فُصْلَان"),
 "khara": G("khara", "خَارَ", "خ و ر", "verb", "to low (of a cow; hollow)", "böğürmek (inek; ecvef)", 4),
 "baqar": G("baqar", "بَقَر", "ب ق ر", "noun", "cows, cattle (a collective noun)", "sığır, inekler (ism-i cem')", 1),
 "thagha": G("thagha", "ثَغَا", "ث غ و", "verb", "to bleat (defective)", "melemek (nâkıs)", 4),
 "ghanam": G("ghanam", "غَنَم", "غ ن م", "noun", "sheep and goats (a collective noun)", "koyun, davar (ism-i cem')", 1),
 "sakhla": G("sakhla", "سَخْلَة", "س خ ل", "noun", "a lamb or kid", "kuzu, oğlak", 4, plural="سِخَال"),
 "rafaa": G("rafaa", "رَفَعَ", "ر ف ع", "verb", "to lift, to raise", "kaldırmak", 1),
 "an": G("an", "عَنْ", None, "prep", "from, away from", "-den", 1),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "lawla": G("lawla", "لَوْلَا", None, "part", "were it not for; (with a verb) why not", "olmasaydı; (fiille) keşke, neden … -madı", 2),
 "aamana": G("aamana", "آمَنَ", "أ م ن", "verb", "to believe (Form IV)", "iman etmek (if'âl)", 1),
 "nafaa": G("nafaa", "نَفَعَ", "ن ف ع", "verb", "to benefit", "fayda vermek", 1),
 "iman": G("iman", "إِيمَان", "أ م ن", "noun", "faith", "iman", 1),
 "illa": G("illa", "إِلَّا", None, "part", "except", "ancak, -den başka", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people", "kavim", 1),
 "kashafa": G("kashafa", "كَشَفَ", "ك ش ف", "verb", "to remove, to uncover", "kaldırmak, açmak", 1),
 "khizy": G("khizy", "خِزْي", "خ ز ي", "noun", "disgrace", "rezillik, rüsvalık", 2),
 "dunya": G("dunya", "دُنْيَا", "د ن و", "noun", "this world; the nearer (a maqṣūr elative)", "dünya; en yakın (maksûr ism-i tafdîl)", 1),
 "mattaa": G("mattaa", "مَتَّعَ", "م ت ع", "verb", "to give enjoyment, to let enjoy (Form II)", "faydalandırmak, yararlandırmak (tef'îl)", 2),
 "pron-1p": G("pron-1p", "نَا", None, "pron", "we / us", "biz / bizi", 1),
 "pron-3fs": G("pron-3fs", "هَا", None, "pron", "her / it (f.)", "onu / onun", 1),
 "pron-3mp": G("pron-3mp", "هُمْ", None, "pron", "them / their", "onları / onların", 1),
 "pron-3ms": G("pron-3ms", "هُ", None, "pron", "him / his / it", "onu / onun", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tahaqqaqa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَقَّق", "تَحَقَّق", "تَحَقَّق", "تَحَقُّق", "مُتَحَقِّق", "مُتَحَقَّق مِنْهُ", None, None, "تَحَقَّقَ مِنَ الْأَمْرِ: تَثَبَّتَ مِنْهُ وَتَيَقَّنَ."))
put_morph(mo, "tahana", _sg.sound1("fataha", "طَحَن", "طْحَن", "اِطْحَن", "طَحْن", "طَاحِن", "مَطْحُون", "طُحِنَ", "يُطْحَنُ", "طَحَنَ الْحَبَّ: جَعَلَهُ دَقِيقًا."))
put_morph(mo, "dara-turn", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "دَار", "دُر", "دُور", "دُر", "دُور", "دُر", "دَوَرَان", "دَائِر", None, None, None, "دَارَ الشَّيْءُ يَدُورُ: تَحَرَّكَ حَوْلَ نَفْسِهِ أَوْ حَوْلَ غَيْرِهِ — أَجْوَفُ وَاوِيٌّ؛ لَمْ يَدُرْ."))
put_morph(mo, "baraza", _sg.sound1("nasara", "بَرَز", "بْرُز", "اُبْرُز", "بُرُوز", "بَارِز", None, None, None, "بَرَزَ: ظَهَرَ بَعْدَ خَفَاءٍ."))
put_morph(mo, "tamada", _sg.derived_naqis("مِنْ بَابِ التَّفَاعُلِ", "تَفَاعَلَ يَتَفَاعَلُ", "َ", "تَمَادَ", "تَمَاد", "a", "تَمَاد", "تَمَادٍ (التَّمَادِي)", "مُتَمَادٍ (الْمُتَمَادِي)", None, None, None, "تَمَادَى فِي الْأَمْرِ: لَجَّ فِيهِ وَأَصَرَّ — نَاقِصٌ؛ تَمَادَوْا."))
put_morph(mo, "jaara", _sg.sound1("fataha", "جَأَر", "جْأَر", "اِجْأَر", "جُؤَار", "جَائِر", None, None, None, "جَأَرَ إِلَى اللهِ: رَفَعَ صَوْتَهُ بِالدُّعَاءِ وَالتَّضَرُّعِ — مَهْمُوزُ الْعَيْنِ."))
put_morph(mo, "ragha", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "رَغَ", "رْغ", "u", "اُرْغ", "رُغَاء", "رَاغٍ (الرَّاغِي)", None, None, None, "رَغَا الْبَعِيرُ يَرْغُو: صَوَّتَ وَضَجَّ — نَاقِصٌ وَاوِيٌّ؛ رَغَتْ."))
put_morph(mo, "khara", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "خَار", "خُر", "خُور", "خُر", "خُور", "خُر", "خُوَار", "خَائِر", None, None, None, "خَارَ الثَّوْرُ يَخُورُ: صَاحَ — أَجْوَفُ وَاوِيٌّ؛ خَارَتْ."))
put_morph(mo, "thagha", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "ثَغَ", "ثْغ", "u", "اُثْغ", "ثُغَاء", "ثَاغٍ (الثَّاغِي)", None, None, None, "ثَغَتِ الشَّاةُ تَثْغُو: صَاحَتْ — نَاقِصٌ وَاوِيٌّ."))
put_morph(mo, "tadarraa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَضَرَّع", "تَضَرَّع", "تَضَرَّع", "تَضَرُّع", "مُتَضَرِّع", None, None, None, "تَضَرَّعَ إِلَى اللهِ: خَضَعَ وَذَلَّ وَأَلَحَّ فِي الدُّعَاءِ."))
put_morph(mo, "mattaa", _sg.derived(_sg.B2, _sg.W2, "ُ", "مَتَّع", "مَتِّع", "مَتِّع", "تَمْتِيع", "مُمَتِّع", "مُمَتَّع", "مُتِّعَ", "يُمَتَّعُ", "مَتَّعَهُ اللهُ: أَطَالَ لَهُ الِانْتِفَاعَ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch18 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 18 (print pp. 28–29): the story of Yūnus and its wisdom — rescue when every outlet is blocked (s1–s5); Yūnus among his people: the refusal, the threat, the repentance of Nineveh, with 10:98 (s6–s11)."
ADD_TR = " On sekizinci bölüm (baskı s. 28–29): Yûnus'un kıssası ve hikmeti — bütün menfezler tıkandığında kurtarış (s1–s5); Yûnus kavmi arasında: ret, tehdit, Ninova'nın tövbesi, 10:98 ile (s6–s11)."
write_out(18, S, TITLE, ADD_EN, ADD_TR, "Ayyūb and Yūnus §4–5", GLOSS_ADD, notes=(), related=())
report(18, S, GLOSS_ADD, ())
