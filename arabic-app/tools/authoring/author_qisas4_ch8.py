# -*- coding: utf-8 -*-
"""Qiṣaṣ al-Nabiyyīn, Part Four — chapter 8: «فِقْهٌ دَقِيقٌ وَعِلْمٌ عَمِيقٌ» — §5 (the vineyard judgment, with 21:78–79) and
§6 (Sulaymān knows the speech of birds and beasts: the valley of the ants); print pp. 14–16.
python3 tools/authoring/author_qisas4_ch8.py"""
import json, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from qisas4_common import *
import qisas4_common as _qc
import sarf_gen as _sg
PKG = _qc.PKG
TITLE = {"ar": "فِقْهٌ دَقِيقٌ وَعِلْمٌ عَمِيقٌ", "en": "Fine judgment and deep knowledge", "tr": "İnce bir fıkıh ve derin bir ilim"}
S = []; sen = sen_of(S)
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; MK = "mubtada-khabar"; MB = "maful-bihi"; FL = "fail"; IW = "inna-wa-akhawatuha"; IQ = "al-iqtibas-wal-tadmin"; KN = "kana-wa-akhawatuha"; MW = "ism-mawsul"; AK = "afal-khamsa"; MF = "maful-fih"; JS = "jam-mudhakkar-salim"; JT = "jam-taksir"; JM = "jam-muannath-salim"; MM = "mamnu-min-sarf"; NF = "naib-al-fail"; LJ = "lam-jazim"; HL = "hal"; AM = "imperative-amr"; MX = "mafulayn"; TA = "lam-taleel"; BD = "badal"; SH = "in-shartiyya"; LN = "la-nahiya"; IS = "idha-shartiyya"
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
def fa_mazi(full, lex, en, tr, tags=(), hidden="هُوَ", punct=None, extra_ar=""):
    return tok(full, lex, "verb", [AT] + list(tags), "الْفَاءُ عَاطِفَةٌ (لِلتَّعْقِيبِ)، وَ" + full[2:] + " فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + (f"، وَالْفَاعِلُ مُسْتَتِرٌ: {hidden}" if hidden else "") + extra_ar + ".", "«so» + " + en + " — a māḍī after the fāʾ of sequence.", "«de/da» + " + tr + " — ta'kîb fâ'sından sonra mâzî.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])
def fa_mazi_ta(full, lex, en, tr, tags=(), punct=None):
    return tok(full, lex, "verb", [AT] + list(tags), "الْفَاءُ عَاطِفَةٌ (لِلتَّعْقِيبِ)، وَ" + full[2:] + " فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«so» + " + en + " — a māḍī with the feminine tāʾ.", "«de/da» + " + tr + " — te'nis tâ'sı ile mâzî.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg(full[2:], lex, "verb")])

# ---------------------------------------------------------------- §5 فِقْهٌ دَقِيقٌ وَعِلْمٌ عَمِيقٌ (print pp. 14–15)
sen("s1", "His intelligence and his capacity for sound judgment showed in a case raised before his great father:",
        "Zekâsı ve doğru hüküm verme gücü, büyük babasına götürülen bir davada ortaya çıktı:", [
  tok("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — qad.", "«ve gerçekten» — kad.", segments=wa_("قَدْ", "qad", "part")),
  mazi("تَجَلَّى", "tajalla", "«showed»", "«ortaya çıktı»", tags=["naqis-verbs", "form-v-verbs"], hidden=None, extra_ar=" — مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ"),
  noun_pron("ذَكَاؤُهُ", "dhaka-intelligence", "ذَكَاؤُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his intelligence» — the doer.", "«zekâsı» — fâil.", tags=[FL, ID, "ism-mamdud"]),
  noun_pron("وَقُدْرَتُهُ", "qudra", "وَقُدْرَتُ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَقُدْرَتُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his capacity»", "«ve gücü»", tags=[AT, ID]),
  prep("عَلَى", "ala", "«for»", "«-e»"),
  majrur("الْحُكْمِ", "hukm", "«judgment»", "«hüküm»", tags=["masdar"]),
  naat("الصَّحِيحِ", "sahih", "«sound»", "«doğru»"),
  fi(), majrur("قَضِيَّةٍ", "qadiyya", "«a case»", "«bir dava»"),
  tok("رُفِعَتْ", "rafaa", "verb", ["jumla-sifa", NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هِيَ — وَالْجُمْلَةُ نَعْتٌ.", "«raised» — a passive; the clause is a naʿt of the case.", "«götürülen» — meçhul; cümle davanın sıfatı."),
  prep("إِلَى", "ila", "«before»", "«-e»"),
  noun_pron("وَالِدِهِ", "walid-father", "وَالِدِ", "هِ", "pron-3ms", "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his father»", "«babasına»", tags=[HJ, ID, "ism-fail"]),
  naat("الْعَظِيمِ", "azim", "«great»", "«büyük»", tags=["sifa-mushabbaha"], punct="،"),
])
sen("s2", "some people had a vineyard whose clusters had sprouted; the sheep of another people got into it and ruined it, so Dāwūd ruled the sheep to the owner of the vineyard.",
        "Bir topluluğun salkımları yeni sürmüş bir bağı vardı; başka bir topluluğun koyunları içine girip onu harap etti; Dâvûd da koyunları bağ sahibine verdi.", [
  tok("فَكَانَ", "kana", "verb", [AT, KN, "hollow-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«so there was» — kāna after the fāʾ.", "«şöyle ki … vardı» — fâ'dan sonra kâne.", segments=[seg("فَ", "fa", "conj"), seg("كَانَ", "kana", "verb")]),
  tok("لِقَوْمٍ", "qawm", "noun", [HJ, KN], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمٍ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ.", "«to some people» — the jarr phrase is kāna's fronted khabar.", "«bir topluluğun» — câr-mecrûr kâne'nin öne alınmış haberi.", segments=[seg("لِ", "li", "prep"), seg("قَوْمٍ", "qawm", "noun")]),
  tok("كَرْمٌ", "karm", "noun", [KN], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "«a vineyard» — kāna's delayed ism.", "«bir bağ» — kâne'nin sonraya bırakılmış ismi."),
  tok("قَدْ", "qad", "part", ["qad-harf", "jumla-sifa"], "حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُ نَعْتٌ لِكَرْمٌ.", "«had» — qad; the clause is a naʿt of the vineyard.", "«… -miş» — kad; cümle bağın sıfatı."),
  mazi_ta("أَنْبَتَتْ", "anbata", "«sprouted»", "«sürmüştü»", tags=["form-iv-verbs"]),
  noun_pron("عَنَاقِيدُهُ", "unqud", "عَنَاقِيدُ", "هُ", "pron-3ms", "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its clusters» — the doer.", "«salkımları» — fâil.", punct="،", tags=[FL, ID, JT]),
  fa_mazi_ta("فَدَخَلَتْ", "dakhala", "«got in»", "«girdi»"),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«into it»", "«içine»"),
  tok("غَنَمُ", "ghanam", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the sheep» — the doer, annexed.", "«koyunları» — fâil, muzâf."),
  mudaf_ilayh("قَوْمٍ", "qawm", "«of [another] people»", "«bir topluluğun»"),
  tok("فَأَفْسَدَتْهُ", "afsada", "verb", [AT, MB, "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأَفْسَدَ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and ruined it» — the hāʾ is the object.", "«ve onu harap etti» — hâ mef'ûl.", punct="،", segments=[seg("فَ", "fa", "conj"), seg("أَفْسَدَتْ", "afsada", "verb"), pr3ms()]),
  fa_mazi("فَقَضَى", "qada-judge", "«ruled»", "«hükmetti»", tags=["naqis-verbs"], hidden=None, extra_ar=" مُقَدَّرٍ عَلَى الْأَلِفِ"),
  tok("دَاوُدُ", "dawud", "propn", [FL, MM], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Dāwūd» — the doer; a diptote.", "«Dâvûd» — fâil; gayr-i munsarıf."),
  tok("بِالْغَنَمِ", "ghanam", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْغَنَمِ مَجْرُورٌ.", "«the sheep [as compensation]»", "«koyunları»", segments=[seg("بِ", "bi", "prep"), seg("الْغَنَمِ", "ghanam", "noun")]),
  tok("لِصَاحِبِ", "sahib", "noun", [HJ, ID], "اللَّامُ حَرْفُ جَرٍّ، وَصَاحِبِ مَجْرُورٌ، مُضَافٌ.", "«to the owner»", "«sahibine»", segments=[seg("لِ", "li", "prep"), seg("صَاحِبِ", "sahib", "noun")]),
  mudaf_ilayh("الْكَرْمِ", "karm", "«of the vineyard»", "«bağın»", punct="،"),
])
sen("s3", "Then Sulaymān said: Other than this, O prophet of God. He said: And what is that?",
        "Süleyman dedi ki: Bundan başkası, ey Allah'ın peygamberi. O: Nedir o? dedi.", [
  qala(full="فَقَالَ", wa=False, hidden=None, punct=None, tags=[AT]),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»", punct=":"),
  tok("غَيْرُ", "ghayr", "noun", [MK, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ (أَيِ: الْحُكْمُ غَيْرُ هٰذَا) مَرْفُوعٌ، مُضَافٌ.", "«other than» — the khabar of an understood mubtadaʾ; annexed.", "«… -den başkası» — hazfedilmiş mübtedânın haberi; muzâf."),
  tok("هٰذَا", "hadha", "pron", [ID, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«this» — the muḍāf ilayh.", "«bu» — muzâfun ileyh."),
  tok("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "«O»", "«ey»"),
  tok("نَبِيَّ", "nabi", "noun", ["vocative-munada", ID], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "«prophet [of]» — a munādā annexed, in naṣb.", "«peygamberi» — muzâf münâdâ, mansub."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»", punct="."),
  qala(hidden="هُوَ"),
  tok("وَمَا", "ma-istifham", "pron", [MK, "al-istifham"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمَا اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ (أَوْ مُبْتَدَأٌ).", "«and what» — the question-mā, a fronted khabar.", "«ve ne» — soru mâ'sı, öne alınmış haber.", segments=wa_("مَا", "ma-istifham", "pron")),
  tok("ذَاكَ", "dhaka", "pron", [MK, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that» — the delayed mubtadaʾ.", "«o» — sonraya bırakılmış mübtedâ.", punct="؟"),
])
sen("s4", "He said: You hand the vineyard to the owner of the sheep, who tends it until it is as it was, and you hand the sheep to the owner of the vineyard, who takes his share of them;",
        "Dedi ki: Bağı koyun sahibine verirsin, o eskisi gibi oluncaya kadar bağa bakar; koyunları da bağ sahibine verirsin, o da onlardan yararlanır;", [
  qala(hidden="هُوَ"),
  mudari("تَدْفَعُ", "dafaa", "«you hand»", "«verirsin»", tags=[MB], hidden="أَنْتَ"),
  maful_("الْكَرْمَ", "karm", "«the vineyard»", "«bağı»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("صَاحِبِ", "sahib", "«the owner»", "«sahibine»", tags=[ID], ar="مَجْرُورٌ بِإِلَى، مُضَافٌ."),
  mudaf_ilayh("الْغَنَمِ", "ghanam", "«of the sheep»", "«koyunların»"),
  tok("فَيَقُومُ", "qama", "verb", [AT, "mudari-marfu", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيَقُومُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«who tends» — the doer concealed.", "«o bakar» — fâil gizli.", segments=[seg("فَ", "fa", "conj"), seg("يَقُومُ", "qama", "verb")]),
  prep_pron("عَلَيْهِ", "ala", "هِ", "pron-3ms", "«it»", "«ona»"),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ.", "«as» — the kāf with the maṣdar-mā.", "«… gibi» — kâf ve masdariyye mâ."),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ، وَخَبَرُهُ مَحْذُوفٌ (كَمَا كَانَ عَلَيْهِ).", "«it was» — kāna; its ism concealed, its khabar understood.", "«idi» — kâne; ismi gizli, haberi hazfedilmiş.", punct="،"),
  tok("وَتَدْفَعُ", "dafaa", "verb", [AT, "mudari-marfu", MB], "الْوَاوُ عَاطِفَةٌ، وَتَدْفَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and you hand»", "«ve verirsin»", segments=wa_("تَدْفَعُ", "dafaa", "verb")),
  maful_("الْغَنَمَ", "ghanam", "«the sheep»", "«koyunları»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  majrur("صَاحِبِ", "sahib", "«the owner»", "«sahibine»", tags=[ID], ar="مَجْرُورٌ بِإِلَى، مُضَافٌ."),
  mudaf_ilayh("الْكَرْمِ", "karm", "«of the vineyard»", "«bağın»"),
  tok("فَيُصِيبُ", "asaba", "verb", [AT, "mudari-marfu", "hollow-verbs", "form-iv-verbs"], "الْفَاءُ عَاطِفَةٌ، وَيُصِيبُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ.", "«who takes [his share]»", "«o da yararlanır»", segments=[seg("فَ", "fa", "conj"), seg("يُصِيبُ", "asaba", "verb")]),
  prep_pron("مِنْهَا", "min", "هَا", "pron-3fs", "«of them»", "«onlardan»", punct="،"),
])
sen("s5", "until, when the vineyard is as it was, you hand the vineyard back to its owner and the sheep to their owner.",
        "nihayet bağ eski hâline gelince, bağı sahibine, koyunları da sahibine geri verirsin.", [
  tok("حَتَّى", "hatta", "part", ["huruf-jarr"], "حَرْفُ ابْتِدَاءٍ (غَايَةٍ).", "«until» — ḥattā opening the clause.", "«nihayet» — gaye bildiren ibtidâ harfi."),
  tok("إِذَا", "idha", "noun", [IS, MF], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«when» — the conditional ẓarf idhā.", "«… -ınca» — şart anlamı taşıyan zarf izâ."),
  tok("كَانَ", "kana", "verb", [IS, KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ.", "«is» — kāna, the shart verb.", "«olur» — kâne, şart fiili."),
  tok("الْكَرْمُ", "karm", "noun", [KN], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ.", "«the vineyard» — kāna's ism.", "«bağ» — kâne'nin ismi."),
  tok("كَمَا", "kama", "part", [HJ], "الْكَافُ حَرْفُ جَرٍّ، وَمَا مَصْدَرِيَّةٌ — فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "«as» — the phrase is kāna's khabar.", "«… gibi» — ifade kâne'nin haberi."),
  tok("كَانَ", "kana", "verb", [KN, "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«it was»", "«idi»", punct="،"),
  tok("دَفَعْتَ", "dafaa", "verb", [IS, MB], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — جَوَابُ إِذَا.", "«you hand back» — the tāʾ is the doer; the answer of idhā.", "«verirsin» — tâ fâil; izâ'nın cevabı.", segments=[seg("دَفَعْ", "dafaa", "verb"), seg("تَ", "pron-2ms", "pron")]),
  maful_("الْكَرْمَ", "karm", "«the vineyard»", "«bağı»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  noun_pron("صَاحِبِهِ", "sahib", "صَاحِبِ", "هِ", "pron-3ms", "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its owner»", "«sahibine»", punct="،", tags=[HJ, ID]),
  tok("وَدَفَعْتَ", "dafaa", "verb", [AT, MB], "الْوَاوُ عَاطِفَةٌ، وَدَفَعْتَ فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«and you hand»", "«ve verirsin»", segments=[seg("وَ", "wa", "conj"), seg("دَفَعْ", "dafaa", "verb"), seg("تَ", "pron-2ms", "pron")]),
  maful_("الْغَنَمَ", "ghanam", "«the sheep»", "«koyunları»"),
  prep("إِلَى", "ila", "«to»", "«-e»"),
  noun_pron("صَاحِبِهَا", "sahib", "صَاحِبِ", "هَا", "pron-3fs", "مَجْرُورٌ بِإِلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their owner»", "«sahibine»", punct=".", tags=[HJ, ID]),
])
sen("s6", "And God singled him out with fine judgment and deep knowledge, and said:",
        "Allah onu ince bir fıkıh ve derin bir ilimle seçkin kıldı ve buyurdu:", [
  tok("وَخَصَّهُ", "khassa-single-out", "verb", [MB, "doubled-verbs"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَخَصَّ فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«and He singled him out» — the hāʾ is the object.", "«ve onu seçkin kıldı» — hâ mef'ûl.", segments=[seg("وَ", "wa", "conj"), seg("خَصَّ", "khassa-single-out", "verb"), pr3ms()]),
  allah_fail(),
  tok("بِفِقْهٍ", "fiqh", "noun", [HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَفِقْهٍ مَجْرُورٌ.", "«with judgment»", "«bir fıkıhla»", segments=[seg("بِ", "bi", "prep"), seg("فِقْهٍ", "fiqh", "noun")]),
  naat("دَقِيقٍ", "daqiq", "«fine»", "«ince»", tags=["sifa-mushabbaha"]),
  atf("وَعِلْمٍ", "ilm", "«knowledge»", "«ilim»", "jarr"),
  naat("عَمِيقٍ", "amiq", "«deep»", "«derin»", tags=["sifa-mushabbaha"]),
  qala(full="فَقَالَ", wa=False, hidden="هُوَ", tags=[AT]),
])
sen("s7", "«And Dāwūd and Sulaymān, when they judged concerning the field, when the sheep of a people strayed into it by night; and We were witness to their judgment» (21:78).",
        "«Dâvûd ile Süleyman'ı da [an]: hani bir topluluğun koyunlarının geceleyin dağıldığı ekin hakkında hüküm veriyorlardı; biz onların hükmüne şahittik» (21:78).", [
  *quran([
  tok("وَدَاوُدَ", "dawud", "propn", [AT, MB, MM, "hadhf-wa-taqdir"], "الْوَاوُ عَاطِفَةٌ، وَدَاوُدَ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: اذْكُرْ، مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Dāwūd» — the object of an understood «remember»; a diptote.", "«ve Dâvûd'u» — mukadder (an) fiilinin mef'ûlü; gayr-i munsarıf.", segments=wa_("دَاوُدَ", "dawud", "propn")),
  tok("وَسُلَيْمَانَ", "sulayman", "propn", [AT, MM], "الْوَاوُ عَاطِفَةٌ، وَسُلَيْمَانَ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«and Sulaymān» — joined; a diptote.", "«ve Süleyman'ı» — ma'tûf; gayr-i munsarıf.", segments=wa_("سُلَيْمَانَ", "sulayman", "propn")),
  tok("إِذْ", "idh", "noun", [MF, BD], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ، بَدَلُ اشْتِمَالٍ (أَوْ مَفْعُولٌ فِيهِ).", "«when» — the ẓarf of the past; a badal of inclusion.", "«hani … -ken» — mâzî zarfı; bedel-i iştimâl."),
  tok("يَحْكُمَانِ", "hakama", "verb", [AK, "mudari-marfu", "al-muthanna"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذْ.", "«they both judged» — one of the five verbs, rafʿ by the kept nūn; the dual alif is the doer.", "«ikisi hükmediyorlardı» — ef'âl-i hamseden; nûnun sübûtu ile merfû; tesniye elifi fâil."),
  fi(), majrur("الْحَرْثِ", "harth", "«the field»", "«ekin»"),
  tok("إِذْ", "idh", "noun", [MF], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مُتَعَلِّقٌ بِيَحْكُمَانِ.", "«when» — a ẓarf attached to «they judged».", "«… -diği zaman» — yahkumâni'ye bağlı zarf."),
  mazi_ta("نَفَشَتْ", "nafasha", "«strayed by night»", "«geceleyin dağıldı»", tags=[]),
  prep_pron("فِيهِ", "fi", "هِ", "pron-3ms", "«into it»", "«içine»"),
  tok("غَنَمُ", "ghanam", "noun", [FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the sheep» — the doer.", "«koyunları» — fâil."),
  mudaf_ilayh("الْقَوْمِ", "qawm", "«of the people»", "«topluluğun»"),
  tok("وَكُنَّا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ لِلْحَالِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَنَا اسْمُهُ.", "«and We were» — kāna with nā as its ism.", "«ve biz … idik» — kâne; nâ ismi.", segments=[seg("وَ", "wa", "conj"), seg("كُنْ", "kana", "verb"), seg("نَا", "pron-1p", "pron")]),
  noun_pron("لِحُكْمِهِمْ", "hukm", "لِحُكْمِ", "هِمْ", "pron-3mp", "اللَّامُ حَرْفُ جَرٍّ، وَحُكْمِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِشَاهِدِينَ.", "«to their judgment» — attached to the khabar.", "«onların hükmüne» — habere bağlı.", tags=[HJ, ID, "masdar"]),
  tok("شَاهِدِينَ", "shahid", "noun", [KN, JS, "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«witnesses» — kāna's khabar, naṣb by the yāʾ.", "«şahitler» — kâne'nin haberi, yâ ile mansub.", punct="."),
  ]),
])
sen("s8", "«So We made Sulaymān understand it; and to each We gave judgment and knowledge» (21:79).",
        "«Onu Süleyman'a kavrattık; her birine hüküm ve ilim verdik» (21:79).", [
  *quran([
  tok("فَفَهَّمْنَاهَا", "fahhama", "verb", [AT, MX, "form-ii-verbs"], "الْفَاءُ عَاطِفَةٌ، وَفَهَّمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ، وَهَا مَفْعُولٌ بِهِ أَوَّلُ.", "«so We made [him] understand it» — nā the doer; hā the first object.", "«onu kavrattık» — nâ fâil; hâ ilk mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("فَهَّمْ", "fahhama", "verb"), seg("نَا", "pron-1p", "pron"), seg("هَا", "pron-3fs", "pron")]),
  tok("سُلَيْمَانَ", "sulayman", "propn", [MB, MX, MM], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Sulaymān» — the second object; a diptote.", "«Süleyman'a» — ikinci mef'ûl; gayr-i munsarıf."),
  tok("وَكُلًّا", "kull", "noun", [AT, MB, MX], "الْوَاوُ عَاطِفَةٌ، وَكُلًّا مَفْعُولٌ بِهِ أَوَّلُ مُقَدَّمٌ مَنْصُوبٌ، نُوِّنَ لِقَطْعِهِ عَنِ الْإِضَافَةِ.", "«and to each» — the first object, fronted; tanwīn for the cut iḍāfa.", "«ve her birine» — öne alınmış ilk mef'ûl; izâfetten kesildiği için tenvinli.", segments=wa_("كُلًّا", "kull", "noun")),
  tok("آتَيْنَا", "aataa", "verb", [MX, "naqis-verbs", "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَنَا فَاعِلٌ.", "«We gave» — nā the doer.", "«verdik» — nâ fâil.", segments=[seg("آتَيْ", "aataa", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("حُكْمًا", "hukm", "noun", [MB, MX], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "«judgment» — the second object.", "«hüküm» — ikinci mef'ûl."),
  atf("وَعِلْمًا", "ilm", "«knowledge»", "«ilim»", "nasb", punct="."),
  ]),
])

# ---------------------------------------------------------------- §6 سُلَيْمَانُ يَعْرِفُ لُغَةَ الطَّيْرِ وَالْحَيَوَانِ (print pp. 15–16)
sen("s9", "And the Qurʾān told a wise and delightful story in which Sulaymān's alertness in the management of his kingdom and the awe of his authority showed —",
        "Kur'ân, Süleyman'ın mülkünü yönetmedeki uyanıklığının ve saltanatının heybetinin ortaya çıktığı hikmetli, tatlı bir kıssa anlattı:", [
  mazi("وَقَصَّ", "qassa", "«and told»", "«ve anlattı»", tags=["doubled-verbs"], wa=True, hidden=None),
  fail("الْقُرْآنُ", "quran", "«the Qurʾān»", "«Kur'ân»"),
  maful_("قِصَّةً", "qissa", "«a story»", "«bir kıssa»"),
  naat("حَكِيمَةً", "hakim", "«wise»", "«hikmetli»", case="nasb", tags=["sifa-mushabbaha"]),
  naat("مُمْتِعَةً", "mumti", "«delightful»", "«tatlı»", case="nasb", tags=["ism-fail", "form-iv-verbs"]),
  mazi("تَجَلَّى", "tajalla", "«showed»", "«ortaya çıktı»", tags=["jumla-sifa", "naqis-verbs", "form-v-verbs"], hidden=None, extra_ar=" — وَالْجُمْلَةُ نَعْتٌ ثَالِثٌ"),
  prep_pron("فِيهَا", "fi", "هَا", "pron-3fs", "«in which»", "«içinde»"),
  tok("تَيَقُّظُ", "tayaqquz", "noun", [FL, ID, "masdar"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "«the alertness» — the doer, annexed.", "«uyanıklığı» — fâil, muzâf."),
  tok("سُلَيْمَانَ", "sulayman", "propn", [ID, MM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of Sulaymān» — jarr by fatḥa (a diptote).", "«Süleyman'ın» — gayr-i munsarıf, fetha ile mecrûr."),
  fi(), majrur("تَدْبِيرِ", "tadbir", "«the management»", "«yönetme»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  noun_pron("مَمْلَكَتِهِ", "mamlaka", "مَمْلَكَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of his kingdom»", "«mülkünü»", tags=[ID]),
  atf("وَرَهْبَةِ", "rahba", "«the awe»", "«heybeti»", "raf", tags=[ID], sign="— مَعْطُوفٌ عَلَى تَيَقُّظُ، مُضَافٌ"),
  noun_pron("سُلْطَانِهِ", "sultan", "سُلْطَانِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«of his authority»", "«saltanatının»", punct="،", tags=[ID]),
])
sen("s10", "how God joined for him the happiness of this world and the next, and kingship, power and prophethood, and the message in religion; and he knew the speech of birds and beasts.",
        "Allah onun için dünya ve âhiret saadetini, mülk, iktidar ve peygamberliği, dinde risaleti nasıl bir araya getirdi; o, kuşların ve hayvanların dilini bilirdi.", [
  tok("كَيْفَ", "kayfa", "noun", ["al-istifham", HL], "اسْمُ اسْتِفْهَامٍ فِي مَحَلِّ نَصْبٍ حَالٌ.", "«how» — the question-word, in the place of a ḥāl.", "«nasıl» — soru ismi, hâl mahallinde."),
  mazi("جَمَعَ", "jamaa-gather", "«joined»", "«bir araya getirdi»", tags=[], hidden=None),
  allah_fail(),
  li_pron("لَهُ", "هُ", "pron-3ms", "«for him»", "«onun için»"),
  tok("بَيْنَ", "bayna", "noun", [MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«between»", "«arasını»"),
  mudaf_ilayh("سَعَادَةِ", "saada", "«the happiness»", "«saadetini»", tags=[ID], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  mudaf_ilayh("الدُّنْيَا", "dunya", "«of this world»", "«dünya»", ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ."),
  atf("وَالْآخِرَةِ", "akhira", "«the next»", "«âhiret»", "jarr", punct="،"),
  tok("وَبَيْنَ", "bayna", "noun", [AT, MF, ID], "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«and between»", "«ve arasını»", segments=wa_("بَيْنَ", "bayna", "noun")),
  mudaf_ilayh("الْمُلْكِ", "mulk", "«kingship»", "«mülk»"),
  atf("وَالتَّمْكِينِ", "tamkin", "«power»", "«iktidar»", "jarr", tags=["masdar"]),
  atf("وَالنُّبُوَّةِ", "nubuwwa", "«prophethood»", "«peygamberlik»", "jarr"),
  atf("وَالرِّسَالَةِ", "risala", "«the message»", "«risalet»", "jarr"),
  fi(), majrur("الدِّينِ", "din", "«religion»", "«din»", punct="،"),
  kana(),
  mudari("يَعْرِفُ", "arafa", "«he knew»", "«bilirdi»", tags=[KN, MB], hidden="هُوَ", extra_ar=" — وَالْجُمْلَةُ خَبَرُ كَانَ"),
  tok("لُغَةَ", "lugha", "noun", [MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«the speech» — the object, annexed.", "«dilini» — mef'ûl, muzâf."),
  mudaf_ilayh("الطَّيْرِ", "tayr", "«of birds»", "«kuşların»"),
  atf("وَالْحَيَوَانِ", "hayawan", "«beasts»", "«hayvanların»", "jarr", punct="،"),
])
sen("s11", "Once he gathered his hosts of jinn, men and birds, and rode among them in pomp and grandeur; they were in perfect order and under the command of their chiefs.",
        "Bir keresinde cinlerden, insanlardan ve kuşlardan ordularını topladı; debdebe ve ihtişam içinde aralarında yola çıktı; onlar tam bir düzen içinde ve reislerinin kumandası altındaydılar.", [
  mazi("وَجَمَعَ", "jamaa-gather", "«and he gathered»", "«ve topladı»", tags=[AT, MB], wa=True, hidden="هُوَ"),
  noun_pron("جُنُودَهُ", "jund", "جُنُودَ", "هُ", "pron-3ms", "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his hosts»", "«ordularını»", tags=[MB, ID, JT]),
  prep("مِنَ", "min", "«of»", "«-den»", ar="حَرْفُ جَرٍّ لِلْبَيَانِ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ."),
  majrur("الْجِنِّ", "jinn", "«the jinn»", "«cinler»"),
  atf("وَالْإِنْسِ", "ins", "«men»", "«insanlar»", "jarr"),
  atf("وَالطَّيْرِ", "tayr", "«birds»", "«kuşlar»", "jarr"),
  tok("ذَاتَ", "dhat", "noun", [MF, ID], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ (ذَاتَ مَرَّةٍ: مَرَّةً مِنَ الْمَرَّاتِ).", "«once» (lit. «at a time») — a ẓarf, annexed.", "«bir keresinde» — zaman zarfı, muzâf."),
  mudaf_ilayh("مَرَّةٍ", "marra-once", "«a time»", "«kere»", punct="،"),
  mazi("وَرَكِبَ", "rakiba", "«and he rode»", "«ve yola çıktı»", tags=[AT], wa=True, hidden="هُوَ"),
  prep_pron("فِيهِمْ", "fi", "هِمْ", "pron-3mp", "«among them»", "«aralarında»"),
  fi(), majrur("أُبَّهَةٍ", "ubbaha", "«pomp»", "«debdebe»"),
  atf("وَعَظَمَةٍ", "azama-grandeur", "«grandeur»", "«ihtişam»", "jarr", punct="،"),
  tok("وَكَانُوا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ لِلْحَالِ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«and they were» — kāna; the wāw is its ism.", "«ve onlar … idiler» — kâne; vâv ismi.", segments=[seg("وَ", "wa", "conj"), seg("كَانُ", "kana", "verb"), seg("وا", "pron-3mp", "pron")]),
  prep("عَلَى", "ala", "«in»", "«içinde»", ar="حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  majrur("نِظَامٍ", "nizam", "«order»", "«bir düzen»"),
  naat("كَامِلٍ", "kamil", "«perfect»", "«tam»", tags=["ism-fail"], punct="،"),
  tok("وَكَانُوا", "kana", "verb", [AT, KN, "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ، وَالْوَاوُ اسْمُهُ.", "«and they were»", "«ve idiler»", segments=[seg("وَ", "wa", "conj"), seg("كَانُ", "kana", "verb"), seg("وا", "pron-3mp", "pron")]),
  fi(), majrur("قِيَادَةِ", "qiyada", "«the command»", "«kumandası»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ."),
  noun_pron("رُؤَسَائِهِمْ", "rais", "رُؤَسَائِ", "هِمْ", "pron-3mp", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«of their chiefs»", "«reislerinin»", punct="،", tags=[ID, JT]),
])
sen("s12", "Sulaymān passed over the valley of the ants, and an ant feared for its tribe that they would crush it with their hooves while Sulaymān and his hosts did not notice, so it ordered them to go into their dwellings.",
        "Süleyman karınca vadisinden geçti; bir karınca, Süleyman ve orduları farkında olmadan toynaklarıyla kabilesini ezmelerinden korktu ve onlara yuvalarına girmelerini emretti.", [
  fa_mazi("فَمَرَّ", "marra", "«passed»", "«geçti»", tags=["doubled-verbs"], hidden=None),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  prep("عَلَى", "ala", "«over»", "«-den»"),
  majrur("وَادِي", "wadi-valley", "«the valley»", "«vadisi»", tags=[ID, "ism-maqsur-manqus"], ar="مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، مُضَافٌ — مَنْقُوصٌ."),
  mudaf_ilayh("النَّمْلِ", "naml", "«of the ants»", "«karıncaların»", punct="،"),
  fa_mazi_ta("فَخَافَتْ", "khafa", "«feared»", "«korktu»", tags=["hollow-verbs"]),
  fail("نَمْلَةٌ", "namla", "«an ant»", "«bir karınca»"),
  prep("عَلَى", "ala", "«for»", "«için»"),
  noun_pron("قَبِيلَتِهَا", "qabila-tribe", "قَبِيلَتِ", "هَا", "pron-3fs", "مَجْرُورٌ بِعَلَى، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«its tribe»", "«kabilesi»", tags=[HJ, ID]),
  tok("أَنْ", "an-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ (خَافَتْ تَحْطِيمَهَا).", "«that» — the an of naṣb; the clause is the object of «feared».", "«… -mesinden» — nasb eden masdariyye en; cümle «korktu»nun mef'ûlü."),
  tok("تَحْطِمَهَا", "hatama", "verb", ["an-masdariyya", MB], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ (الْجُنُودُ)، وَهَا مَفْعُولٌ بِهِ.", "«they would crush it» — naṣb by an; hā the object.", "«onu ezmelerinden» — en ile mansub; hâ mef'ûl.", segments=[seg("تَحْطِمَ", "hatama", "verb"), seg("هَا", "pron-3fs", "pron")]),
  noun_pron("بِحَوَافِرِهَا", "hafir", "بِحَوَافِرِ", "هَا", "pron-3fs", "الْبَاءُ حَرْفُ جَرٍّ، وَحَوَافِرِ مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«with their hooves»", "«toynaklarıyla»", punct="،", tags=[HJ, ID, JT]),
  la_nafiya(wa=True),
  neg_mudari("يَشْعُرُ", "shaara", "«noticed»", "«farkına varır»", tags=[AT, HL], hidden="هُوَ", extra=" — وَالْجُمْلَةُ حَالٌ"),
  tok("بِذٰلِكَ", "dhalika", "pron", [HJ, "asma-al-ishara"], "الْبَاءُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ.", "«of that»", "«bunun»", segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»"),
  noun_pron("وَجُنُودُهُ", "jund", "وَجُنُودُ", "هُ", "pron-3ms", "الْوَاوُ عَاطِفَةٌ، وَجُنُودُ مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and his hosts»", "«ve orduları»", punct="،", tags=[AT, ID, JT]),
  tok("فَأَمَرَتْهُمْ", "amara-v", "verb", [AT, MB], "الْفَاءُ عَاطِفَةٌ، وَأَمَرَ فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهُمْ مَفْعُولٌ بِهِ.", "«so it ordered them» — hum the object.", "«onlara emretti» — hüm mef'ûl.", segments=[seg("فَ", "fa", "conj"), seg("أَمَرَتْ", "amara-v", "verb"), seg("هُمْ", "pron-3mp", "pron")]),
  tok("بِالدُّخُولِ", "dukhul", "noun", [HJ, "masdar"], "الْبَاءُ حَرْفُ جَرٍّ، وَالدُّخُولِ مَجْرُورٌ.", "«to go in»", "«girmelerini»", segments=[seg("بِ", "bi", "prep"), seg("الدُّخُولِ", "dukhul", "noun")]),
  fi(), noun_pron("مَسَاكِنِهِمْ", "maskan", "مَسَاكِنِ", "هِمْ", "pron-3mp", "مَجْرُورٌ بِفِي، مُضَافٌ، وَهِمْ مُضَافٌ إِلَيْهِ.", "«their dwellings»", "«yuvalarına»", punct="،", tags=[HJ, ID, JT]),
])
sen("s13", "Sulaymān understood this, and no vanity or pride took him for being a prophet among the prophets of God;",
        "Süleyman bunu anladı; Allah'ın peygamberlerinden bir peygamber olmasından dolayı ona ne böbürlenme ne de gurur geldi;", [
  fa_mazi("فَفَهِمَ", "fahima", "«understood»", "«anladı»", tags=[MB], hidden=None),
  tok("ذٰلِكَ", "dhalika", "pron", [MB, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "«this» — the object.", "«bunu» — mef'ûl."),
  fail_name("سُلَيْمَانُ", "sulayman", "«Sulaymān»", "«Süleyman»", punct="،"),
  tok("وَلَمْ", "lam-jazima", "part", [AT, LJ], "الْوَاوُ عَاطِفَةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«and … not» — lam.", "«ve … -medi» — lem.", segments=wa_("لَمْ", "lam-jazima", "part")),
  tok("يَأْخُذْهُ", "akhadha", "verb", [LJ, MB], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«took him» — jazm by lam; the hāʾ the object.", "«onu aldı» — lem ile meczum; hâ mef'ûl.", segments=[seg("يَأْخُذْ", "akhadha", "verb"), pr3ms()]),
  fail("التِّيهُ", "tih", "«vanity»", "«böbürlenme»"),
  tok("وَلَا", "la-nafiya", "part", [AT, "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor» — the wāw with a lā that strengthens the negation.", "«ne de» — vâv ve nefyi pekiştiren lâ.", segments=wa_("لَا", "la-nafiya", "part")),
  tok("الزَّهْوُ", "zahw", "noun", [AT, FL], "مَعْطُوفٌ عَلَى التِّيهُ مَرْفُوعٌ.", "«pride» — joined to «vanity».", "«gurur» — böbürlenmeye ma'tûf."),
  tok("بِأَنَّهُ", "anna", "part", [HJ, IW], "الْبَاءُ لِلسَّبَبِيَّةِ، وَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْبَاءِ.", "«for being» — the bāʾ of cause with anna; the hāʾ its ism.", "«… olmasından dolayı» — sebep bâ'sı ve enne; hâ ismi.", segments=[seg("بِ", "bi", "prep"), seg("أَنَّ", "anna", "part"), pr3ms()]),
  khabar_inna("نَبِيٌّ", "nabi", "«a prophet»", "«bir peygamber»", part="أَنَّ"),
  prep("مِنْ", "min", "«among»", "«-den»"),
  majrur("أَنْبِيَاءِ", "nabi", "«the prophets»", "«peygamberleri»", tags=[ID, JT], ar="مَجْرُورٌ بِمِنْ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»", punct="،"),
])
sen("s14", "rather, that moved him to praise God the Exalted and thank His favour, and to pray for success in righteous work and for entering the ranks of God's righteous servants.",
        "aksine bu onu Allah Teâlâ'ya hamd etmeye, nimetine şükretmeye, salih amelde muvaffakiyet ve Allah'ın salih kulları silsilesine katılma duasına sevk etti.", [
  tok("بَلْ", "bal", "part", [AT], "حَرْفُ إِضْرَابٍ.", "«rather» — bal.", "«aksine» — idrâb harfi."),
  tok("حَمَلَهُ", "hamala", "verb", [MB], "فِعْلٌ مَاضٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«moved him» — the hāʾ the object.", "«onu sevk etti» — hâ mef'ûl.", segments=[seg("حَمَلَ", "hamala", "verb"), pr3ms()]),
  tok("ذٰلِكَ", "dhalika", "pron", [FL, "asma-al-ishara"], "اسْمُ إِشَارَةٍ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "«that» — the doer.", "«bu» — fâil."),
  prep("عَلَى", "ala", "«to»", "«-e»"),
  majrur("حَمْدِ", "hamd", "«praising»", "«hamd etmeye»", tags=[ID, "masdar"], ar="مَجْرُورٌ بِعَلَى، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'a»"),
  tok("تَعَالَى", "taala", "verb", [NA, "naqis-verbs", "form-vi-verbs"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«the Exalted»", "«Teâlâ»"),
  atf("وَشُكْرِ", "shukr", "«thanking»", "«şükretmeye»", "jarr", tags=[ID, "masdar"]),
  noun_pron("نِعْمَتِهِ", "nima", "نِعْمَتِ", "هِ", "pron-3ms", "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«His favour»", "«nimetine»", punct="،", tags=[ID]),
  atf("وَالدُّعَاءِ", "dua", "«praying»", "«dua etmeye»", "jarr", tags=["masdar"]),
  tok("لِلتَّوْفِيقِ", "tawfiq", "noun", [HJ, "masdar"], "اللَّامُ حَرْفُ جَرٍّ، وَالتَّوْفِيقِ مَجْرُورٌ.", "«for success»", "«muvaffakiyet için»", segments=[seg("لِ", "li", "prep"), seg("التَّوْفِيقِ", "tawfiq", "noun")]),
  tok("لِلْعَمَلِ", "amal-work", "noun", [HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْعَمَلِ مَجْرُورٌ.", "«in work»", "«amelde»", segments=[seg("لِ", "li", "prep"), seg("الْعَمَلِ", "amal-work", "noun")]),
  naat("الصَّالِحِ", "salih", "«righteous»", "«salih»", tags=["ism-fail"]),
  atf("وَالِانْخِرَاطِ", "inkhirat", "«entering»", "«katılma»", "jarr", tags=["masdar", "form-vii-verbs"]),
  fi(), majrur("سِلْكِ", "silk", "«the ranks»", "«silsilesine»", tags=[ID], ar="مَجْرُورٌ بِفِي، مُضَافٌ."),
  mudaf_ilayh("عِبَادِ", "abd", "«of the servants»", "«kulları»", tags=[ID, JT], ar="مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ."),
  tok("اللهِ", "allah", "propn", [ID], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of God»", "«Allah'ın»"),
  tok("الصَّالِحِينَ", "salih", "noun", [NA, JS, "ism-fail"], "نَعْتٌ لِعِبَادِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "«righteous» — the naʿt of the servants, jarr by the yāʾ.", "«salih» — kulların sıfatı, yâ ile mecrûr.", punct="."),
])

# ---------------------------------------------------------------- the glossary (lemma_clash.py: dhaka-intelligence, walid-father, khassa-single-out, azama-grandeur, qabila-tribe, wadi-valley take suffixed keys; dhaka = ذَاكَ, marra-once = مَرَّة are reused)
CAND = {
 "tajalla": G("tajalla", "تَجَلَّى", "ج ل و", "verb", "to show, to become manifest (Form V, defective)", "ortaya çıkmak, tecellî etmek (tefa''ul, nâkıs)", 3),
 "dhaka-intelligence": G("dhaka-intelligence", "ذَكَاء", "ذ ك و", "noun", "intelligence, sharpness of mind (a mamdūd noun)", "zekâ (memdûd isim)", 2),
 "qudra": G("qudra", "قُدْرَة", "ق د ر", "noun", "capacity, power", "güç, kudret", 2),
 "hukm": G("hukm", "حُكْم", "ح ك م", "noun", "judgment, a ruling", "hüküm", 1),
 "sahih": G("sahih", "صَحِيح", "ص ح ح", "noun", "sound, correct", "doğru, sahih", 1),
 "qadiyya": G("qadiyya", "قَضِيَّة", "ق ض ي", "noun", "a case, an issue", "dava, mesele", 2),
 "rafaa": G("rafaa", "رَفَعَ", "ر ف ع", "verb", "to raise; to bring (a case) before", "kaldırmak; (davayı) götürmek", 1),
 "walid-father": G("walid-father", "وَالِد", "و ل د", "noun", "a father (an active participle)", "baba (ism-i fâil)", 1),
 "azim": G("azim", "عَظِيم", "ع ظ م", "noun", "great, mighty", "büyük, yüce", 1),
 "qawm": G("qawm", "قَوْم", "ق و م", "noun", "a people", "kavim, topluluk", 1),
 "karm": G("karm", "كَرْم", "ك ر م", "noun", "a vineyard, grapevines", "bağ, üzüm bağı", 3, plural="كُرُوم"),
 "anbata": G("anbata", "أَنْبَتَ", "ن ب ت", "verb", "to sprout, to put forth (Form IV)", "sürmek, bitirmek (if'âl)", 2),
 "unqud": G("unqud", "عُنْقُود", "ع ن ق د", "noun", "a cluster (of grapes)", "salkım", 3, plural="عَنَاقِيد"),
 "dakhala": G("dakhala", "دَخَلَ", "د خ ل", "verb", "to enter", "girmek", 1),
 "ghanam": G("ghanam", "غَنَم", "غ ن م", "noun", "sheep (a collective)", "koyun, davar (cins ismi)", 2),
 "afsada": G("afsada", "أَفْسَدَ", "ف س د", "verb", "to ruin, to corrupt (Form IV)", "bozmak, harap etmek (if'âl)", 2),
 "qada-judge": G("qada-judge", "قَضَى", "ق ض ي", "verb", "to rule, to decree; to judge", "hükmetmek, karar vermek", 2),
 "sahib": G("sahib", "صَاحِب", "ص ح ب", "noun", "an owner; a companion", "sahip; arkadaş", 1, plural="أَصْحَاب"),
 "ghayr": G("ghayr", "غَيْر", "غ ي ر", "noun", "other than — always annexed", "başka, gayrı — dâimâ muzâf", 1),
 "ma-istifham": G("ma-istifham", "مَا (الِاسْتِفْهَامِيَّة)", None, "pron", "what? — the question-mā", "ne? — soru mâ'sı", 1),
 "dhaka": G("dhaka", "ذَاكَ", None, "pron", "that (the middle demonstrative)", "o, şu (orta işaret)", 1),
 "dafaa": G("dafaa", "دَفَعَ", "د ف ع", "verb", "to hand over; to push away", "vermek, teslim etmek; itmek", 1),
 "qama": G("qama", "قَامَ", "ق و م", "verb", "to stand; to take charge of (with ʿalā)", "kalkmak, durmak; (alâ ile) bakmak, üstlenmek", 1),
 "asaba": G("asaba", "أَصَابَ", "ص و ب", "verb", "to hit; to take a share of (with min) (Form IV, hollow)", "isabet etmek; (min ile) yararlanmak (if'âl, ecvef)", 2),
 "hatta": G("hatta", "حَتَّى", None, "part", "until — a particle of jarr, of opening, or of joining", "… -e kadar — cer, ibtidâ ya da atıf harfi", 1),
 "idha": G("idha", "إِذَا", None, "part", "when — the conditional ẓarf of the future", "… -ınca — gelecek zamanın şart zarfı", 1),
 "khassa-single-out": G("khassa-single-out", "خَصَّ", "خ ص ص", "verb", "to single out, to grant especially (doubled)", "tahsis etmek, seçkin kılmak (muzâaf)", 2),
 "fiqh": G("fiqh", "فِقْه", "ف ق ه", "noun", "understanding; fine judgment; jurisprudence", "fıkıh, anlayış", 2),
 "daqiq": G("daqiq", "دَقِيق", "د ق ق", "noun", "fine, subtle, precise", "ince, dakik", 2),
 "amiq": G("amiq", "عَمِيق", "ع م ق", "noun", "deep", "derin", 2),
 "idh": G("idh", "إِذْ", None, "noun", "when — the ẓarf of the past", "hani, … -diği zaman — mâzî zarfı", 1),
 "hakama": G("hakama", "حَكَمَ", "ح ك م", "verb", "to judge, to rule", "hükmetmek", 1),
 "harth": G("harth", "حَرْث", "ح ر ث", "noun", "tillage, a cultivated field", "ekin, tarla", 2),
 "nafasha": G("nafasha", "نَفَشَ", "ن ف ش", "verb", "to stray and graze by night (of sheep)", "(koyun) geceleyin dağılıp otlamak", 3),
 "shahid": G("shahid", "شَاهِد", "ش ه د", "noun", "a witness (an active participle)", "şahit (ism-i fâil)", 1, plural="شُهُود"),
 "fahhama": G("fahhama", "فَهَّمَ", "ف ه م", "verb", "to make understand (Form II; two objects)", "kavratmak, anlatmak (tef'îl; iki mef'ûl)", 2),
 "qassa": G("qassa", "قَصَّ", "ق ص ص", "verb", "to tell, to narrate (doubled)", "anlatmak, kıssa etmek (muzâaf)", 2),
 "qissa": G("qissa", "قِصَّة", "ق ص ص", "noun", "a story", "kıssa, hikâye", 1, plural="قِصَص"),
 "hakim": G("hakim", "حَكِيم", "ح ك م", "noun", "wise", "hikmetli, hakîm", 1),
 "mumti": G("mumti", "مُمْتِع", "م ت ع", "noun", "delightful (the active participle of Form IV)", "tatlı, zevk veren (if'âl ism-i fâili)", 3),
 "tayaqquz": G("tayaqquz", "تَيَقُّظ", "ي ق ظ", "noun", "alertness, wakefulness (maṣdar of Form V)", "uyanıklık (tefa''ul masdarı)", 3),
 "tadbir": G("tadbir", "تَدْبِير", "د ب ر", "noun", "management, planning (maṣdar of Form II)", "yönetim, tedbir (tef'îl masdarı)", 2),
 "mamlaka": G("mamlaka", "مَمْلَكَة", "م ل ك", "noun", "a kingdom", "memleket, krallık", 2),
 "rahba": G("rahba", "رَهْبَة", "ر ه ب", "noun", "awe, dread", "heybet, korku", 3),
 "sultan": G("sultan", "سُلْطَان", "س ل ط", "noun", "authority, power; a sultan", "saltanat, otorite; sultan", 2),
 "kayfa": G("kayfa", "كَيْفَ", None, "noun", "how? — the question-word of state", "nasıl? — hâl soran isim", 1),
 "jamaa-gather": G("jamaa-gather", "جَمَعَ", "ج م ع", "verb", "to gather, to join", "toplamak, bir araya getirmek", 1),
 "saada": G("saada", "سَعَادَة", "س ع د", "noun", "happiness", "saadet, mutluluk", 1),
 "dunya": G("dunya", "دُنْيَا", "د ن و", "noun", "this world", "dünya", 1),
 "akhira": G("akhira", "آخِرَة", "أ خ ر", "noun", "the hereafter", "âhiret", 1),
 "tamkin": G("tamkin", "تَمْكِين", "م ك ن", "noun", "power, establishment (maṣdar of Form II)", "iktidar, yerleştirme (tef'îl masdarı)", 3),
 "nubuwwa": G("nubuwwa", "نُبُوَّة", "ن ب أ", "noun", "prophethood", "peygamberlik, nübüvvet", 1),
 "risala": G("risala", "رِسَالَة", "ر س ل", "noun", "a message; the prophetic mission", "risalet, mesaj", 1),
 "din": G("din", "دِين", "د ي ن", "noun", "religion", "din", 1),
 "arafa": G("arafa", "عَرَفَ", "ع ر ف", "verb", "to know", "bilmek, tanımak", 1),
 "lugha": G("lugha", "لُغَة", "ل غ و", "noun", "a language, speech", "dil", 1),
 "jund": G("jund", "جُنْد", "ج ن د", "noun", "a host, an army", "ordu", 2, plural="جُنُود"),
 "ins": G("ins", "إِنْس", "أ ن س", "noun", "mankind (a collective; beside the jinn)", "insanlar (cins ismi; cinlerin karşıtı)", 2),
 "dhat": G("dhat", "ذَات", None, "noun", "possessor of; «once» in ذَاتَ مَرَّةٍ", "sahibi; «bir keresinde» (zâte merratin)", 2),
 "marra-once": G("marra-once", "مَرَّة", "م ر ر", "noun", "a time, once", "kere, defa", 1),
 "rakiba": G("rakiba", "رَكِبَ", "ر ك ب", "verb", "to ride, to mount", "binmek, yola çıkmak", 1),
 "ubbaha": G("ubbaha", "أُبَّهَة", "أ ب ه", "noun", "pomp, splendour", "debdebe, ihtişam", 3),
 "azama-grandeur": G("azama-grandeur", "عَظَمَة", "ع ظ م", "noun", "grandeur, greatness", "azamet, ihtişam", 2),
 "nizam": G("nizam", "نِظَام", "ن ظ م", "noun", "order, system", "düzen, nizam", 2),
 "kamil": G("kamil", "كَامِل", "ك م ل", "noun", "perfect, complete (an active participle)", "tam, kâmil (ism-i fâil)", 1),
 "qiyada": G("qiyada", "قِيَادَة", "ق و د", "noun", "command, leadership", "kumanda, önderlik", 2),
 "rais": G("rais", "رَئِيس", "ر أ س", "noun", "a chief, a leader", "reis, başkan", 2, plural="رُؤَسَاء"),
 "wadi-valley": G("wadi-valley", "وَادٍ", "و د ي", "noun", "a valley (a manqūṣ noun)", "vadi (mankûs isim)", 1, plural="أَوْدِيَة"),
 "naml": G("naml", "نَمْل", "ن م ل", "noun", "ants (a collective)", "karıncalar (cins ismi)", 1),
 "namla": G("namla", "نَمْلَة", "ن م ل", "noun", "an ant", "bir karınca", 1),
 "khafa": G("khafa", "خَافَ", "خ و ف", "verb", "to fear (hollow)", "korkmak (ecvef)", 1),
 "qabila-tribe": G("qabila-tribe", "قَبِيلَة", "ق ب ل", "noun", "a tribe", "kabile", 1, plural="قَبَائِل"),
 "hatama": G("hatama", "حَطَمَ", "ح ط م", "verb", "to crush, to smash", "ezmek, kırmak", 2),
 "hafir": G("hafir", "حَافِر", "ح ف ر", "noun", "a hoof", "toynak", 3, plural="حَوَافِر"),
 "shaara": G("shaara", "شَعَرَ", "ش ع ر", "verb", "to notice, to feel (with bi)", "fark etmek, hissetmek (bi ile)", 1),
 "amara-v": G("amara-v", "أَمَرَ", "أ م ر", "verb", "to order, to command", "emretmek", 1),
 "dukhul": G("dukhul", "دُخُول", "د خ ل", "noun", "entering", "girme, giriş", 1),
 "maskan": G("maskan", "مَسْكَن", "س ك ن", "noun", "a dwelling", "mesken, yuva", 1, plural="مَسَاكِن"),
 "fahima": G("fahima", "فَهِمَ", "ف ه م", "verb", "to understand", "anlamak", 1),
 "akhadha": G("akhadha", "أَخَذَ", "أ خ ذ", "verb", "to take; to seize", "almak; tutmak", 1),
 "tih": G("tih", "تِيه", "ت ي ه", "noun", "vanity, conceit; a wilderness", "böbürlenme, kibir; çöl", 3),
 "zahw": G("zahw", "زَهْو", "ز ه و", "noun", "pride, boastfulness", "gurur, böbürlenme", 3),
 "anna": G("anna", "أَنَّ", None, "part", "that — anna, the sister of inna that turns its clause into a maṣdar", "… -dığı — cümlesini masdara çeviren inne kardeşi enne", 1),
 "bal": G("bal", "بَلْ", None, "part", "rather, nay — the particle of turning", "bilakis, aksine", 2),
 "hamala": G("hamala", "حَمَلَ", "ح م ل", "verb", "to carry; to move (someone to)", "taşımak; sevk etmek", 1),
 "hamd": G("hamd", "حَمْد", "ح م د", "noun", "praise", "hamd", 1),
 "taala": G("taala", "تَعَالَى", "ع ل و", "verb", "He is exalted", "yücedir", 1),
 "shukr": G("shukr", "شُكْر", "ش ك ر", "noun", "thanks, gratitude", "şükür", 1),
 "nima": G("nima", "نِعْمَة", "ن ع م", "noun", "a favour", "nimet", 1, plural="نِعَم"),
 "dua": G("dua", "دُعَاء", "د ع و", "noun", "prayer, supplication", "dua", 1),
 "tawfiq": G("tawfiq", "تَوْفِيق", "و ف ق", "noun", "success granted by God", "tevfik, muvaffakiyet", 2),
 "amal-work": G("amal-work", "عَمَل", "ع م ل", "noun", "work, a deed", "iş, amel", 1),
 "salih": G("salih", "صَالِح", "ص ل ح", "noun", "righteous", "salih", 1),
 "inkhirat": G("inkhirat", "اِنْخِرَاط", "خ ر ط", "noun", "entering (the ranks of), joining (maṣdar of Form VII)", "(bir sıraya) katılma, girme (infiâl masdarı)", 3),
 "silk": G("silk", "سِلْك", "س ل ك", "noun", "a thread; a rank, a line", "ip; silsile, sıra", 3),
 "abd": G("abd", "عَبْد", "ع ب د", "noun", "a servant", "kul", 1, plural="عِبَاد"),
 "ilm": G("ilm", "عِلْم", "ع ل م", "noun", "knowledge", "ilim", 1),
 "tayr": G("tayr", "طَيْر", "ط ي ر", "noun", "birds", "kuşlar", 1),
 "hayawan": G("hayawan", "حَيَوَان", "ح ي ي", "noun", "an animal", "hayvan", 1),
 "jinn": G("jinn", "جِنّ", "ج ن ن", "noun", "the jinn", "cinler", 1),
 "bayna": G("bayna", "بَيْنَ", "ب ي ن", "noun", "between", "arasında", 1),
 "mulk": G("mulk", "مُلْك", "م ل ك", "noun", "kingship", "mülk", 2),
 "nabi": G("nabi", "نَبِيّ", "ن ب أ", "noun", "a prophet", "peygamber", 1, plural="أَنْبِيَاء"),
 "kull": G("kull", "كُلّ", "ك ل ل", "noun", "every, each, all", "her, hepsi", 1),
 "quran": G("quran", "قُرْآن", "ق ر أ", "propn", "the Qurʾān", "Kur'ân", 1),
 "pron-2ms": G("pron-2ms", "كَ", None, "pron", "you / your (masc. singular, attached); the tāʾ of the doer", "sen / senin (bitişik); fâil tâ'sı", 1),
 "hadha": G("hadha", "هٰذَا", None, "pron", "this (masculine)", "bu", 1),
 "dhalika": G("dhalika", "ذٰلِكَ", None, "pron", "that", "o, şu", 1),
}
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "tajalla", _sg.derived_naqis("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ", "تَجَلَّ", "تَجَلّ", "a", "تَجَلّ", "تَجَلٍّ (التَّجَلِّي)", "مُتَجَلٍّ (الْمُتَجَلِّي)", None, None, None, "تَجَلَّى الشَّيْءُ: ظَهَرَ وَانْكَشَفَ."))
put_morph(mo, "rafaa", _sg.sound1("fataha", "رَفَع", "رْفَع", "اِرْفَع", "رَفْع", "رَافِع", "مَرْفُوع", "رُفِعَ", "يُرْفَعُ", "رَفَعَ الشَّيْءَ: أَعْلَاهُ؛ وَرُفِعَتِ الْقَضِيَّةُ إِلَى الْقَاضِي: قُدِّمَتْ إِلَيْهِ."))
put_morph(mo, "anbata", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْبَت", "نْبِت", "أَنْبِت", "إِنْبَات", "مُنْبِت", "مُنْبَت", "أُنْبِتَ", "يُنْبَتُ", "أَنْبَتَتِ الْأَرْضُ: أَخْرَجَتْ نَبَاتَهَا."))
put_morph(mo, "dakhala", _sg.sound1("nasara", "دَخَل", "دْخُل", "اُدْخُل", "دُخُول", "دَاخِل", "مَدْخُول", "دُخِلَ", "يُدْخَلُ", "دَخَلَ الْمَكَانَ: صَارَ دَاخِلَهُ."))
put_morph(mo, "dafaa", _sg.sound1("fataha", "دَفَع", "دْفَع", "اِدْفَع", "دَفْع", "دَافِع", "مَدْفُوع", "دُفِعَ", "يُدْفَعُ", "دَفَعَ الشَّيْءَ إِلَيْهِ: سَلَّمَهُ إِيَّاهُ."))
put_morph(mo, "qada-judge", _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "قَضَ", "قْض", "i", "اِقْض", "قَضَاء", "قَاضٍ (الْقَاضِي)", "مَقْضِيّ", "قُضِيَ", "يُقْضَى", "قَضَى يَقْضِي: حَكَمَ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ ضَرَبَ؛ لَمْ يَقْضِ."))
put_morph(mo, "asaba", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَصَاب", "أَصَب", "صِيب", "صِب", "أَصِيب", "أَصِب", "إِصَابَة", "مُصِيب", "مُصَاب", "أُصِيبَ", "يُصَابُ", "أَصَابَ مِنَ الشَّيْءِ: نَالَ مِنْهُ."))
put_morph(mo, "khassa-single-out", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "خَصّ / خُصُوص", "خَاصّ", _sg.mazi14("خَصّ", "خَصَص"), _sg.mudari14("َ", "خُصّ", "خْصُص"), ["خُصَّ", "خُصَّا", "خُصُّوا", "خُصِّي", "خُصَّا", "اُخْصُصْنَ"], "يَخُصَّ", "يَخُصَّ", "تَخُصَّ", "مَخْصُوص", "خُصَّ", "يُخَصُّ", "خَصَّهُ بِالشَّيْءِ: أَفْرَدَهُ بِهِ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَخُصَّ."))
put_morph(mo, "hakama", _sg.sound1("nasara", "حَكَم", "حْكُم", "اُحْكُم", "حُكْم", "حَاكِم", "مَحْكُوم", "حُكِمَ", "يُحْكَمُ", "حَكَمَ بَيْنَهُمْ: قَضَى."))
put_morph(mo, "nafasha", _sg.sound1("nasara", "نَفَش", "نْفُش", "اُنْفُش", "نَفْش", "نَافِش", None, None, None, "نَفَشَتِ الْغَنَمُ: رَعَتْ لَيْلًا بِلَا رَاعٍ."))
put_morph(mo, "fahhama", _sg.derived(_sg.B2, _sg.W2, "ُ", "فَهَّم", "فَهِّم", "فَهِّم", "تَفْهِيم", "مُفَهِّم", "مُفَهَّم", "فُهِّمَ", "يُفَهَّمُ", "فَهَّمَهُ الشَّيْءَ: جَعَلَهُ يَفْهَمُهُ."))
put_morph(mo, "qassa", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "قَصَص", "قَاصّ", _sg.mazi14("قَصّ", "قَصَص"), _sg.mudari14("َ", "قُصّ", "قْصُص"), ["قُصَّ", "قُصَّا", "قُصُّوا", "قُصِّي", "قُصَّا", "اُقْصُصْنَ"], "يَقُصَّ", "يَقُصَّ", "تَقُصَّ", "مَقْصُوص", "قُصَّ", "يُقَصُّ", "قَصَّ الْخَبَرَ: حَكَاهُ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَقُصَّ."))
put_morph(mo, "arafa", _sg.sound1("daraba", "عَرَف", "عْرِف", "اِعْرِف", "مَعْرِفَة", "عَارِف", "مَعْرُوف", "عُرِفَ", "يُعْرَفُ", "عَرَفَ الشَّيْءَ: عَلِمَهُ."))
put_morph(mo, "rakiba", _sg.sound1("samia", "رَكِب", "رْكَب", "اِرْكَب", "رُكُوب", "رَاكِب", "مَرْكُوب", "رُكِبَ", "يُرْكَبُ", "رَكِبَ الدَّابَّةَ: عَلَاهَا."))
put_morph(mo, "hatama", _sg.sound1("daraba", "حَطَم", "حْطِم", "اِحْطِم", "حَطْم", "حَاطِم", "مَحْطُوم", "حُطِمَ", "يُحْطَمُ", "حَطَمَ الشَّيْءَ: كَسَرَهُ."))
put_morph(mo, "shaara", _sg.sound1("nasara", "شَعَر", "شْعُر", "اُشْعُر", "شُعُور", "شَاعِر", "مَشْعُور", None, None, "شَعَرَ بِالشَّيْءِ: أَحَسَّ بِهِ وَعَلِمَهُ."))
put_morph(mo, "fahima", _sg.sound1("samia", "فَهِم", "فْهَم", "اِفْهَم", "فَهْم", "فَاهِم", "مَفْهُوم", "فُهِمَ", "يُفْهَمُ", "فَهِمَ الشَّيْءَ: عَقَلَهُ وَعَرَفَهُ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("qisas4 ch8 gloss+morph ok", len(GLOSS_ADD))
ADD_EN = " Chapter 8 (print pp. 14–16, §5–6): the vineyard judgment with 21:78–79 (s1–s8); Sulaymān knows the speech of birds and beasts — the valley of the ants (s9–s14)."
ADD_TR = " Sekizinci bölüm (baskı s. 14–16, 5–6. kısımlar): bağ davası ve 21:78–79 (s1–s8); Süleyman kuşların ve hayvanların dilini bilir — karınca vadisi (s9–s14)."
write_out(8, S, TITLE, ADD_EN, ADD_TR, "Dāwūd and Sulaymān §5–6", GLOSS_ADD, notes=(), related=())
report(8, S, GLOSS_ADD, ())
