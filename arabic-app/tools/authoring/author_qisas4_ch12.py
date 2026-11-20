# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 12: «وَأَسْلَمْتُ مَعَ سُلَيْمَانَ» — §13 (the queen's error at the glass and her confession) and
the opening line of §14 (the Qurʾān tells the story); print pp. 21–22.
python3 tools/authoring/author_qisas4_ch12.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "وَأَسْلَمْتُ مَعَ سُلَيْمَانَ لِلّٰهِ", "en": "«And I submit with Sulaymān to God»", "tr": "«Süleyman ile birlikte Allah'a teslim oldum»"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; AN = "an-masdariyya"
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
def v_ta_pron(full, lex, stem, pron_form, pron_lex, en, tr, punct=None, tags=(), wa=False, fa=False, extra=""):
    pre = "الْوَاوُ عَاطِفَةٌ، وَ" if wa else ("الْفَاءُ عَاطِفَةٌ، وَ" if fa else "")
    segs = ([seg("وَ" if wa else "فَ", "wa" if wa else "fa", "conj")] if (wa or fa) else []) + [seg(stem, lex, "verb"), seg(pron_form, pron_lex, "pron")]
    return tok(full, lex, "verb", ([AT] if (wa or fa) else []) + [MB] + list(tags), pre + stem + " فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالضَّمِيرُ مَفْعُولٌ بِهِ" + extra + ".", en + " — a feminine māḍī; the pronoun is its object.", tr + " — müennes mâzî; zamir mef'ûl.", punct=punct, segments=segs)

# ---------------------------------------------------------------- §13 وَأَسْلَمْتُ مَعَ سُلَيْمَانَ لِلّٰهِ رَبِّ الْعَالَمِينَ (print pp. 21–22)
sen("s1", "And so it was: despite her sharpness and her intelligence she fell into this gross error, took the glass for rippling water that flows and swells, bared her legs, and wished to wade into it.",
        "Ve öyle de oldu: keskin zekâsına ve aklına rağmen bu fahiş hataya düştü; camı akıp dalgalanan pırıl pırıl bir su sandı, bacaklarını açtı ve içine girmek istedi.", [
  tok("وَهٰكَذَا", "hakadha", "part", [KN, "asma-al-ishara"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰكَذَا: الْكَافُ حَرْفُ جَرٍّ وَذَا اسْمُ إِشَارَةٍ — فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.", "«and so» — the kāf with the demonstrative; kāna's fronted khabar.", "«ve böyle» — kâf ve ism-i işâret; kâne'nin öne alınmış haberi.", segments=wa_("هٰكَذَا", "hakadha", "part")),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ (الْأَمْرُ).", "«it was» — kāna; its ism concealed.", "«oldu» — kâne; ismi gizli.", punct="،"),
  tok("فَقَدْ", "qad", "part", ["qad-harf"], "الْفَاءُ لِلتَّفْرِيعِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«indeed»", "«gerçekten»", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  mazi_ta("تَوَرَّطَتْ", "tawarrata", "«she fell»", "«düştü»", tags=["form-v-verbs"]),
  tok("رَغْمَ", "raghma", "noun", [MF, ID], "مَنْصُوبٌ عَلَى الظَّرْفِيَّةِ (أَوْ مَفْعُولٌ مُطْلَقٌ)، مُضَافٌ — بِمَعْنَى: عَلَى الرَّغْمِ مِنْ.", "«despite» — in naṣb, annexed.", "«rağmen» — mansub, muzâf."),
  noun_pron("ذَهَائِهَا", "dhaha", "ذَهَائِ", "هَا", "pron-3fs", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her sharpness»", "«keskin zekâsına»", tags=[ID, "ism-mamdud"]),
  noun_pron("وَذَكَائِهَا", "dhaka-intelligence", "وَذَكَائِ", "هَا", "pron-3fs", "الْوَاوُ عَاطِفَةٌ، وَذَكَائِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and her intelligence»", "«ve aklına»", tags=[AT, ID, "ism-mamdud"]),
  fi(), tok("هٰذَا", "hadha", "pron", [HJ, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ بِفِي.", "«this»", "«bu»"),
  tok("الْخَطَإِ", "khata", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ — رُسِمَتْ هَمْزَتُهُ عَلَى الْيَاءِ لِكَسْرِهَا.", "«error» — the badal; its hamza written on a yāʾ-seat for the kasra.", "«hataya» — bedel; hemzesi kesre için yâ üzerinde."),
  naat("الْفَاحِشِ", "fahish", "«gross»", "«fahiş»", tags=["ism-fail"], punct="،"),
  tok("وَتَوَهَّمَتِ", "tawahhama", "verb", [AT, MX, "form-v-verbs"], "الْوَاوُ عَاطِفَةٌ، وَتَوَهَّمَ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and took … for» — the feminine tāʾ, kasra for the two sukūns.", "«ve … sandı» — te'nis tâ'sı; iki sâkin için kesre.", segments=wa_("تَوَهَّمَتِ", "tawahhama", "verb")),
  tok("الزُّجَاجَةَ", "zujaja", "noun", [MB, MX], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«the glass» — the first object.", "«camı» — ilk mef'ûl."),
  tok("مَاءً", "ma-water", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«water» — the second object.", "«su» — ikinci mef'ûl."),
  naat("رَقْرَاقًا", "raqraq", "«rippling»", "«pırıl pırıl»", case="nasb"),
  mudari("يَسِيلُ", "sala", "«that flows»", "«akan»", tags=["jumla-sifa", "hollow-verbs"], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ نَعْتٌ ثَانٍ"),
  tok("وَيَمُوجُ", "maja", "verb", [AT, "mudari-marfu", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَمُوجُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«and swells»", "«ve dalgalanan»", punct="،", segments=wa_("يَمُوجُ", "maja", "verb")),
  mazi_ta("فَكَشَفَتْ", "kashafa", "«and bared»", "«ve açtı»", tags=[AT], extra=" — وَالْفَاءُ عَاطِفَةٌ"),
  prep("عَنْ", "an", "«(bared) …»", "«-i»"),
  noun_pron("سَاقَيْهَا", "saq", "سَاقَيْ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَهَا مُضَافٌ إِلَيْهِ.", "«her two legs»", "«iki bacağını»", punct="،", tags=[HJ, ID, "al-muthanna"]),
  mazi_ta("وَأَرَادَتْ", "arada", "«and wished»", "«ve istedi»", tags=[AT, "hollow-verbs", "form-iv-verbs", MB], wa=True),
  tok("أَنْ", "an-masdariyya", "part", [AN], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ أَرَادَتْ.", "«to» — the clause is the object of «wished».", "«… -mek» — cümle «istedi»nin mef'ûlü."),
  tok("تَخُوضَهُ", "khada", "verb", [AN, MB, "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«wade into it» — naṣb by an; the hāʾ the object.", "«içine girmek» — en ile mansub; hâ mef'ûl.", punct=".", segments=[seg("تَخُوضَ", "khada", "verb"), pr3ms()]),
])
sen("s2", "There the prophet of God Sulaymān alerted her to her error and said: It is a palace paved with glass; and the veil was lifted from her eyes,",
        "Orada Allah'ın peygamberi Süleyman onu hatasına karşı uyardı ve dedi ki: O, camdan döşenmiş bir saraydır; perde gözlerinden kalktı,", [
  tok("هُنَالِكَ", "hunalika", "noun", [MF, "asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمَكَانِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ ظَرْفٌ.", "«there» — a ẓarf.", "«orada» — zarf."),
  tok("نَبَّهَهَا", "nabbaha", "verb", [MB, "form-ii-verbs"], "فِعْلٌ مَاضٍ، وَهَا مَفْعُولٌ بِهِ.", "«alerted her» — hā the object.", "«onu uyardı» — hâ mef'ûl.", segments=[seg("نَبَّهَ", "nabbaha", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("نَبِيُّ", "nabi", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the prophet [of]» — the doer, annexed.", "«peygamberi» — fâil, muzâf."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»"),
  tok("سُلَيْمَانُ", "sulayman", "propn", [BD, MM], "بَدَلٌ مِنْ نَبِيُّ (أَوْ عَطْفُ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ.", "«Sulaymān» — the badal of «the prophet».", "«Süleyman» — «peygamber»den bedel."),
  prep("عَلَى", "ala", "«to»", "«-e karşı»"),
  noun_pron("خَطَئِهَا", "khata", "خَطَئِ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — رُسِمَتْ هَمْزَتُهُ عَلَى الْيَاءِ لِكَسْرِهَا.", "«her error»", "«hatasına»", punct="،", tags=[HJ, ID]),
  qala(full="وَقَالَ", wa=True, hidden="هُوَ"),
  tok("إِنَّهُ", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا.", "«it is» — inna with the hāʾ.", "«o» — inne; hâ ismi.", segments=[seg("إِنَّ", "inna", "part"), pr3ms()]),
  khabar_inna("صَرْحٌ", "sarh", "«a palace»", "«bir saray»"),
  naat("مُمَرَّدٌ", "mumarrad", "«paved»", "«döşenmiş»", case="raf", tags=["ism-maful", "form-ii-verbs"]),
  prep("مِنْ", "min", "«with»", "«-den»"),
  tok("قَوَارِيرَ", "qarura", "noun", [HJ, JT, MM], "مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ (صِيغَةُ مُنْتَهَى الْجُمُوعِ).", "«glass» (lit. crystal vessels) — a diptote plural, jarr by fatḥa.", "«cam» (sırça) — gayr-i munsarıf çoğul, fetha ile mecrûr.", punct="،"),
  mazi("وَانْكَشَفَ", "inkashafa", "«and was lifted»", "«ve kalktı»", tags=[AT, "form-vii-verbs"], wa=True, hidden=None),
  fail("الْغِطَاءُ", "ghita", "«the veil»", "«perde»", tags=["ism-mamdud"]),
  prep("عَنْ", "an", "«from»", "«-den»"),
  noun_pron("عَيْنَيْهَا", "ayn", "عَيْنَيْ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَنْ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَهَا مُضَافٌ إِلَيْهِ.", "«her two eyes»", "«iki gözünden»", punct="،", tags=[HJ, ID, "al-muthanna"]),
])
sen("s3", "and she recognised her ignorance in measuring the manifestation against the Manifest One, and in worshipping the sun and prostrating to it; and she hastened to say:",
        "görünüşü görünenin üstüne kıyas etmekteki, güneşe tapıp ona secde etmekteki cehaletini anladı ve hemen şöyle demeye koyuldu:", [
  mazi_ta("وَعَرَفَتْ", "arafa", "«and she recognised»", "«ve anladı»", tags=[AT, MB], wa=True),
  noun_pron("جَهْلَهَا", "jahl", "جَهْلَ", "هَا", "pron-3fs", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«her ignorance»", "«cehaletini»", tags=[MB, ID]),
  fi(), majrur("قِيَاسِ", "qiyas", "«measuring»", "«kıyas etmekteki»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("الْمَظْهَرِ", "mazhar", "«the manifestation»", "«görünüşü»"),
  prep("عَلَى", "ala", "«against»", "«üstüne»"),
  majrur("الظَّاهِرِ", "zahir", "«the Manifest One»", "«görünenin»", tags=["ism-fail"], punct="،"),
  atf("وَعِبَادَةِ", "ibada", "«worshipping»", "«tapmaktaki»", "jarr", tags=[ID, "masdar"]),
  mudaf_ilayh("الشَّمْسِ", "shams", "«the sun»", "«güneşe»"),
  atf("وَالسُّجُودِ", "sujud", "«prostrating»", "«secde etmekteki»", "jarr", tags=["masdar"]),
  li_pron("لَهَا", "هَا", "pron-3fs", "«to it»", "«ona»", punct="،"),
  mazi_ta("وَابْتَدَرَتْ", "ibtadara", "«and she hastened»", "«ve hemen koyuldu»", tags=[AT, "form-viii-verbs"], wa=True),
  mudari("تَقُولُ", "qala", "«to say»", "«demeye»", tags=[HL, "hollow-verbs", MB], hidden="هِيَ", extra_ar=" — وَالْجُمْلَةُ حَالٌ", punct=":"),
])
sen("s4", "«My Lord, I have wronged myself, and I submit with Sulaymān to God, the Lord of the worlds» (27:44).",
        "«Rabbim, ben nefsime zulmettim; Süleyman ile birlikte âlemlerin Rabbi Allah'a teslim oldum» (27:44).", [
  *quran([
  tok("رَبِّ", "rabb", "noun", ["vocative-munada", ID, "ya-al-mutakallim"], "مُنَادًى مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، حُذِفَ حَرْفُ النِّدَاءِ.", "«my Lord» — a munādā annexed to the dropped yāʾ of the speaker; the vocative particle dropped.", "«Rabbim» — hazfedilmiş mütekellim yâ'sına muzâf münâdâ; nidâ harfi hazfedilmiş."),
  tok("إِنِّي", "inna", "part", [IW], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْيَاءُ اسْمُهَا.", "«indeed I» — inna with the yāʾ.", "«şüphesiz ben» — inne; yâ ismi.", segments=[seg("إِنِّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("ظَلَمْتُ", "zalama", "verb", [IW, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«I have wronged» — the tāʾ the doer; the clause is inna's khabar.", "«zulmettim» — tâ fâil; cümle inne'nin haberi.", segments=[seg("ظَلَمْ", "zalama", "verb"), seg("تُ", "pron-1s", "pron")]),
  noun_pron("نَفْسِي", "nafs", "نَفْسِ", "ي", "pron-1s", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«myself» — the object, annexed to the yāʾ.", "«nefsime» — mef'ûl, yâ'ya muzâf.", tags=[MB, ID, "ya-al-mutakallim"]),
  tok("وَأَسْلَمْتُ", "aslama", "verb", [AT, "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَسْلَمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ.", "«and I submit» — the tāʾ the doer.", "«ve teslim oldum» — tâ fâil.", segments=[seg("وَ", "wa", "conj"), seg("أَسْلَمْ", "aslama", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("مَعَ", "maa", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile birlikte»"),
  tok("سُلَيْمَانَ", "sulayman", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — jarr by fatḥa.", "«Süleyman» — fetha ile mecrûr."),
  tok("لِلّٰهِ", "allah", "propn", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ.", "«to God»", "«Allah'a»", segments=[seg("لِ", "li", "prep"), seg("لّٰهِ", "allah", "propn")]),
  tok("رَبِّ", "rabb", "noun", [NA, ID], "نَعْتٌ (أَوْ بَدَلٌ) مَجْرُورٌ، مُضَافٌ.", "«the Lord [of]» — a naʿt of the Name, annexed.", "«Rabbi» — lafza-i celâlin sıfatı, muzâf."),
  tok("الْعَالَمِينَ", "alamin", "noun", [ID, JS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "«of the worlds» — jarr by the yāʾ, attached to the sound plural.", "«âlemlerin» — cem'-i müzekker sâlime mülhak, yâ ile mecrûr.", punct="."),
  ]),
])

# ---------------------------------------------------------------- §14 الْقُرْآنُ يَحْكِي قِصَّةَ سُلَيْمَانَ — the opening line (print p. 22)
sen("s5", "And read this delightful, engaging story in the Qurʾān; God the Exalted says:",
        "Bu güzel ve tatlı kıssayı Kur'ân'da okuyun; Allah Teâlâ buyurur ki:", [
  tok("وَاقْرَؤُوا", "qaraa", "verb", [AT, AM, MB], "الْوَاوُ لِلِاسْتِئْنَافِ، وَاقْرَؤُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — مَهْمُوزُ اللَّامِ.", "«and read» — an imperative on the dropped nūn; the wāw is the doer.", "«ve okuyun» — nûnun düşmesi üzere mebnî emir; vâv fâil.", segments=wa_("اقْرَؤُوا", "qaraa", "verb")),
  tok("هٰذِهِ", "hadhihi", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this» — the object.", "«bu» — mef'ûl."),
  tok("الْقِصَّةَ", "qissa", "noun", [BD], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَنْصُوبٌ.", "«story» — the badal.", "«kıssayı» — bedel."),
  naat("الشَّائِقَةَ", "shaiq", "«engaging»", "«güzel»", case="nasb", tags=["ism-fail"]),
  naat("الْمُمْتِعَةَ", "mumti", "«delightful»", "«tatlı»", case="nasb", tags=["ism-fail", "form-iv-verbs"]),
  fi(), majrur("الْقُرْآنِ", "quran", "«the Qurʾān»", "«Kur'ân'da»", punct="،"),
  mudari("يَقُولُ", "qala", "«says»", "«buyurur»", tags=["hollow-verbs", MB], hidden=None),
  allah_fail(),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«the Exalted»", "«Teâlâ»", punct=":"),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: all planned keys clean)
CAND = {
 "hakadha": G("hakadha", "هٰكَذَا", None, "part", "so, thus, like this", "böyle, işte böyle", 1),
 "kana": G("kana", "كَانَ", "ك و ن", "verb", "to be", "olmak", 1),
 "tawarrata": G("tawarrata", "تَوَرَّطَ", "و ر ط", "verb", "to fall into (a trap, an error) (Form V)", "(hataya, tuzağa) düşmek (tefa''ul)", 3),
 "raghma": G("raghma", "رَغْمَ", "ر غ م", "noun", "despite, in spite of", "rağmen", 2),
 "dhaha": G("dhaha", "ذَهَاء", "ذ ه و", "noun", "sharpness of mind, acumen (a mamdūd noun)", "keskin zekâ, dirayet (memdûd isim)", 3),
 "dhaka-intelligence": G("dhaka-intelligence", "ذَكَاء", "ذ ك و", "noun", "intelligence", "zekâ", 2),
 "khata": G("khata", "خَطَأ", "خ ط أ", "noun", "an error", "hata", 1),
 "fahish": G("fahish", "فَاحِش", "ف ح ش", "noun", "gross, outrageous (an active participle)", "fahiş, aşırı (ism-i fâil)", 3),
 "tawahhama": G("tawahhama", "تَوَهَّمَ", "و ه م", "verb", "to take for, to imagine (Form V)", "sanmak (tefa''ul)", 3),
 "zujaja": G("zujaja", "زُجَاجَة", "ز ج ج", "noun", "a piece of glass; the glass (floor)", "cam (parçası); cam döşeme", 2),
 "ma-water": G("ma-water", "مَاء", "م و ه", "noun", "water", "su", 1),
 "raqraq": G("raqraq", "رَقْرَاق", "ر ق ق", "noun", "rippling, glistening (of water)", "pırıl pırıl, hafif dalgalı (su)", 3),
 "sala": G("sala", "سَالَ", "س ي ل", "verb", "to flow (hollow)", "akmak (ecvef)", 2),
 "maja": G("maja", "مَاجَ", "م و ج", "verb", "to swell, to surge (hollow)", "dalgalanmak (ecvef)", 3),
 "kashafa": G("kashafa", "كَشَفَ", "ك ش ف", "verb", "to bare", "açmak", 1),
 "saq": G("saq", "سَاق", "س و ق", "noun", "a leg", "bacak", 2),
 "arada": G("arada", "أَرَادَ", "ر و د", "verb", "to wish", "istemek", 1),
 "khada": G("khada", "خَاضَ", "خ و ض", "verb", "to wade into (hollow)", "içine girmek, dalmak (ecvef)", 3),
 "hunalika": G("hunalika", "هُنَالِكَ", None, "noun", "there", "orada", 1),
 "nabbaha": G("nabbaha", "نَبَّهَ", "ن ب ه", "verb", "to alert, to draw attention (Form II; with ʿalā)", "uyarmak, dikkat çekmek (tef'îl; alâ ile)", 2),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1),
 "sulayman": G("sulayman", "سُلَيْمَان", None, "propn", "Sulaymān", "Süleyman", 1),
 "inna": G("inna", "إِنَّ", None, "part", "indeed", "şüphesiz", 1),
 "sarh": G("sarh", "صَرْح", "ص ر ح", "noun", "a palace, a lofty building", "saray, köşk", 3),
 "mumarrad": G("mumarrad", "مُمَرَّد", "م ر د", "noun", "paved, made smooth (a passive participle of Form II; Qurʾānic)", "döşenmiş, cilalanmış (tef'îl ism-i mef'ûlü; Kur'ânî)", 3),
 "qarura": G("qarura", "قَارُورَة", "ق ر ر", "noun", "a glass vessel, crystal", "sırça, billur kap", 3, plural="قَوَارِير"),
 "inkashafa": G("inkashafa", "اِنْكَشَفَ", "ك ش ف", "verb", "to be lifted (Form VII)", "kalkmak (infiâl)", 2),
 "ghita": G("ghita", "غِطَاء", "غ ط و", "noun", "a veil", "perde", 2),
 "ayn": G("ayn", "عَيْن", "ع ي ن", "noun", "an eye", "göz", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to recognise, to know", "anlamak, bilmek", 1),
 "jahl": G("jahl", "جَهْل", "ج ه ل", "noun", "ignorance", "cehalet", 1),
 "qiyas": G("qiyas", "قِيَاس", "ق ي س", "noun", "measuring, analogy", "kıyas", 2),
 "mazhar": G("mazhar", "مَظْهَر", "ظ ه ر", "noun", "a manifestation", "görünüş, mazhar", 2),
 "zahir": G("zahir", "ظَاهِر", "ظ ه ر", "noun", "the manifest, the apparent; al-Ẓāhir (a name of God)", "zâhir, görünen; ez-Zâhir (Allah'ın bir ismi)", 2),
 "ibada": G("ibada", "عِبَادَة", "ع ب د", "noun", "worship", "ibadet", 1),
 "shams": G("shams", "شَمْس", "ش م س", "noun", "the sun", "güneş", 1),
 "sujud": G("sujud", "سُجُود", "س ج د", "noun", "prostration (a maṣdar)", "secde (masdar)", 1),
 "ibtadara": G("ibtadara", "اِبْتَدَرَ", "ب د ر", "verb", "to hasten to (Form VIII)", "hemen koyulmak, ilk davranmak (iftiâl)", 3),
 "qala": G("qala", "قَالَ", "ق و ل", "verb", "to say", "demek", 1),
 "rabb": G("rabb", "رَبّ", "ر ب ب", "noun", "Lord", "Rab", 1),
 "zalama": G("zalama", "ظَلَمَ", "ظ ل م", "verb", "to wrong", "zulmetmek", 1),
 "nafs": G("nafs", "نَفْس", "ن ف س", "noun", "self, soul", "nefis, kendi", 1),
 "aslama": G("aslama", "أَسْلَمَ", "س ل م", "verb", "to submit, to become Muslim (Form IV)", "teslim olmak, Müslüman olmak (if'âl)", 1),
 "maa": G("maa", "مَعَ", None, "noun", "with", "ile", 1),
 "alamin": G("alamin", "عَالَمِين", "ع ل م", "noun", "the worlds (attached to the sound plural)", "âlemler (cem'-i müzekker sâlime mülhak)", 1),
 "qaraa": G("qaraa", "قَرَأَ", "ق ر أ", "verb", "to read", "okumak", 1),
 "hadhihi": G("hadhihi", "هٰذِهِ", None, "pron", "this (feminine)", "bu", 1),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa", 1),
 "shaiq": G("shaiq", "شَائِق", "ش و ق", "noun", "engaging, delightful (an active participle)", "güzel, ilgi çekici (ism-i fâil)", 3),
 "mumti": G("mumti", "مُمْتِع", "م ت ع", "noun", "delightful", "tatlı, zevk veren", 3),
 "quran": G("quran", "قُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "He is exalted", "yücedir", 1),
 "pron-1s": G("pron-1s", "ي", None, "pron", "I / me / my (attached)", "ben / beni / benim", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tawarrata", _sg.derived(_sg.B5, _sg.W5, "َ", "تَوَرَّط", "تَوَرَّط", "تَوَرَّط", "تَوَرُّط", "مُتَوَرِّط", None, None, None, "تَوَرَّطَ فِي الْأَمْرِ: وَقَعَ فِيهِ وَلَمْ يَكَدْ يَتَخَلَّصُ مِنْهُ."))
put_morph(mo, "sala", _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ (مِنْ بَابِ ضَرَبَ)", "سَال", "سِل", "سِيل", "سِل", "سِيل", "سِل", "سَيْل / سَيَلَان", "سَائِل", None, None, None, "سَالَ الْمَاءُ: جَرَى."))
put_morph(mo, "maja", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "مَاج", "مُج", "مُوج", "مُج", "مُوج", "مُج", "مَوْج / مَوَجَان", "مَائِج", None, None, None, "مَاجَ الْبَحْرُ: اضْطَرَبَ وَارْتَفَعَتْ أَمْوَاجُهُ."))
put_morph(mo, "khada", _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ (مِنْ بَابِ نَصَرَ)", "خَاض", "خُض", "خُوض", "خُض", "خُوض", "خُض", "خَوْض", "خَائِض", "مَخُوض", "خِيضَ", "يُخَاضُ", "خَاضَ الْمَاءَ: مَشَى فِيهِ."))
put_morph(mo, "nabbaha", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَبَّه", "نَبِّه", "نَبِّه", "تَنْبِيه", "مُنَبِّه", "مُنَبَّه", "نُبِّهَ", "يُنَبَّهُ", "نَبَّهَهُ عَلَى الشَّيْءِ: جَعَلَهُ يَتَنَبَّهُ لَهُ."))
put_morph(mo, "ibtadara", _sg.derived(_sg.B8, _sg.W8, "َ", "اِبْتَدَر", "بْتَدِر", "اِبْتَدِر", "اِبْتِدَار", "مُبْتَدِر", "مُبْتَدَر", "اُبْتُدِرَ", "يُبْتَدَرُ", "اِبْتَدَرَ الشَّيْءَ: أَسْرَعَ إِلَيْهِ وَبَادَرَ."))
put_morph(mo, "zalama", _sg.sound1("daraba", "ظَلَم", "ظْلِم", "اِظْلِم", "ظُلْم", "ظَالِم", "مَظْلُوم", "ظُلِمَ", "يُظْلَمُ", "ظَلَمَهُ: جَارَ عَلَيْهِ وَوَضَعَ الشَّيْءَ فِي غَيْرِ مَوْضِعِهِ."))
put_morph(mo, "aslama", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْلَم", "سْلِم", "أَسْلِم", "إِسْلَام", "مُسْلِم", "مُسْلَم", "أُسْلِمَ", "يُسْلَمُ", "أَسْلَمَ: انْقَادَ وَدَخَلَ فِي الْإِسْلَامِ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch12 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 12 (print pp. 21–22, §13 and the opening of §14): the queen's error at the glass and her confession with 27:44 (s1–s4); «read this story in the Qurʾān» (s5)."
ADD_TR = " On ikinci bölüm (baskı s. 21–22, 13. kısım ve 14. kısmın girişi): kraliçenin camdaki hatası ve 27:44 ile itirafı (s1–s4); «bu kıssayı Kur'ân'da okuyun» (s5)."
write_out(12, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §13–14", GLOSS_ADD, notes=(), related=())
report(12, S, GLOSS_ADD, ())
