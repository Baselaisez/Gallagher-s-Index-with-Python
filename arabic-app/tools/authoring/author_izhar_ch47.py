# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 47: the THIRD kind of maʿrifa, the demonstratives — ذَا for the masculine, ذَانِ / ذَيْنِ for its dual; تَا، ذِي، تِي،
# تِهْ، ذِهْ، تِهِي، ذِهِي for the feminine, تَانِ / تَيْنِ for its dual; أُولَاءِ long and short for the plural of both; the particle of alerting prefixed
# (هٰذَا); the kāf of address suffixed (ذَاكَ ذَاكُمَا ذَاكُمْ ذَاكُنَّ, and so the rest), both joined (هٰذَاكَ); تِلْكَ، أُولَالِكَ، ذٰلِكَ، ذَانِّكَ، تَانِّكَ (the two
# with shadda) for the far; ثَمَّةَ، هُنَا، هٰهُنَا، هُنَّا، هُنَاكَ for place only. Print pp. 142–143.
#   python3 author_izhar_ch47.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; MB = "maful-bihi"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HV = "hollow-verbs"; MSD = "masdar"; MR = "mudari-marfu"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; KN = "kana-wa-akhawatuha"; AQ = "al-amil-wa-aqsamuh"; IST = "al-istifham"; LN = "la-nafiya"; AMS = "an-masdariyya"
NSB = "ism-mansub"; MQ = "ism-maqsur-manqus"; JT = "jam-taksir"; F2 = "form-ii-verbs"; F4 = "form-iv-verbs"; F5 = "form-v-verbs"; MNF = "mana-al-fil"; INS = "in-shartiyya"; JZ = "nawasib-wa-jawazim-al-mudari"; YM = "ya-al-mutakallim"; DF = "damir-fasl"
TMZ = "tamyiz"; ISH = "asma-al-ishara"; TRF = "tarif-al-musnad-ilayh"; MMB = "al-murab-wal-mabni-wal-irab"; HTN = "huruf-tanbih"; AMT = "amma-tafsiliyya"; FK = "fa-khabar-mubtada"
K = "asma-al-ishara-wa-sighuha"
K46 = "al-marifa-al-mudmarat-wal-alam"
TITLE = {"ar": "النَّوْعُ الثَّالِثُ: أَسْمَاءُ الْإِشَارَةِ وَصِيَغُهَا، وَحَرْفُ التَّنْبِيهِ وَكَافُ الْخِطَابِ، وَظُرُوفُ الْمَكَانِ", "en": "The third kind: the demonstratives and their forms, the particle of alerting and the kāf of address, and the place-demonstratives", "tr": "Üçüncü nev': işaret isimleri ve şekilleri, tenbih harfi ve hitap kâfı, mekân işaretleri"}

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def F(form, lex, en, tr, ar="لَفْظٌ مَحْكِيٌّ: اسْمُ إِشَارَةٍ مَبْنِيٌّ.", punct=None, segments=None, gr=None): return tok(form, lex, "pron", [K, ISH, MMB] + (gr or []), ar, en, tr, punct=punct, segments=segments)
def wa_(form, lex, en, tr, punct=None, ar="لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: اسْمُ إِشَارَةٍ مَبْنِيٌّ."): return tok(form, lex, "pron", [K, AT, ISH, MMB], "الْوَاوُ عَاطِفَةٌ، وَ" + ar, en, tr, punct=punct, segments=wa(form[2:], lex, "pron"))
def li_(form, lex, en, tr, punct=None, gr=None): return tok(form, lex, "noun", [K, HJ] + (gr or []), "اللَّامُ حَرْفُ جَرٍّ، وَ" + form[2:] + " مَجْرُورٌ.", en, tr, punct=punct, segments=[seg("لِ", "li", "prep"), seg(form[2:], lex, "noun")])

# ----------- s1 — the third kind: the masculine and its dual
S.append({"id": "s1", "translation": {"en": "And the third kind is the demonstratives, and they are: «dhā» for the masculine, and for its dual «dhāni» and «dhayni»;", "tr": "Üçüncü nev' işaret isimleridir; onlar: müzekker için zâ, tesniyesi için zâni ve zeyni;"},
 "tokens": [
  tok("وَالنَّوْعُ", "naw", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالنَّوْعُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the kind»", "«ve nev'»", segments=wa("النَّوْعُ", "naw", "noun")),
  tok("الثَّالِثُ", "thalith", "noun", [K, NA], "نَعْتٌ مَرْفُوعٌ.", "«third»", "«üçüncü»"),
  tok("أَسْمَاءُ", "ism", "noun", [K, MK, ID, JT, ISH, TRF], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the nouns of» — the khabar.", "«isimleri» — haber."),
  tok("الْإِشَارَةِ", "ishara", "noun", [K, ID, ISH, MSD, F4], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«pointing»", "«işaret»", punct="،"),
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and they are»", "«ve onlar»", punct=":", segments=wa("هِيَ", "hiya", "pron")),
  F("ذَا", "dha", "«dhā» — this", "«zâ» — bu", "لَفْظٌ مَحْكِيٌّ: اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ، خَبَرٌ."),
  li_("لِلْمُذَكَّرِ", "mudhakkar", "«for the masculine»", "«müzekker için»", punct="،", gr=[IMF, F2]),
  tok("وَلِمُثَنَّاهُ", "muthanna", "noun", [K, AT, HJ, ID, MTH, MQ], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمُثَنَّاهُ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — خَبَرٌ مُقَدَّمٌ.", "«and for its dual» — a fronted khabar.", "«ve tesniyesi için» — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مُثَنَّا", "muthanna", "noun"), pr3ms()]),
  F("ذَانِ", "dha", "«dhāni» — these two, in rafʿ", "«zâni» — bu ikisi, ref'te", "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — مُثَنَّى ذَا فِي الرَّفْعِ.", gr=[MTH]),
  wa_("وَذَيْنِ", "dha", "«and dhayni» — in naṣb and jarr", "«ve zeyni» — nasb ve cerde", punct="،", ar="ذَيْنِ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مُثَنَّى ذَا فِي النَّصْبِ وَالْجَرِّ."),
 ]})
# ----------- s2 — the feminine and its dual; the plural
S.append({"id": "s2", "translation": {"en": "and for the feminine «tā», «dhī», «tī», «tih», «dhih», «tihī», «dhihī», and for its dual «tāni» and «tayni»; and for the plural of both «ulāʾi», long and short;", "tr": "müennes için tâ, zî, tî, tih, zih, tihî, zihî; tesniyesi için tâni ve teyni; ikisinin cemi için medli ve kasırlı ulâi;"},
 "tokens": [
  tok("وَلِلْمُؤَنَّثِ", "muannath", "noun", [K, AT, HJ, IMF, F2], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَالْمُؤَنَّثِ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.", "«and for the feminine»", "«ve müennes için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("الْمُؤَنَّثِ", "muannath", "noun")]),
  F("تَا", "ta-ishara", "«tā» — this (f.)", "«tâ» — bu (dişil)", "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — اسْمُ إِشَارَةٍ لِلْمُؤَنَّثِ."),
  wa_("وَذِي", "dha", "«and dhī»", "«ve zî»"), wa_("وَتِي", "ta-ishara", "«and tī»", "«ve tî»"), wa_("وَتِهْ", "ta-ishara", "«and tih»", "«ve tih»"), wa_("وَذِهْ", "dha", "«and dhih»", "«ve zih»"), wa_("وَتِهِي", "ta-ishara", "«and tihī»", "«ve tihî»"), wa_("وَذِهِي", "dha", "«and dhihī»", "«ve zihî»", punct="،"),
  tok("وَلِمُثَنَّاهُ", "muthanna", "noun", [K, AT, HJ, ID, MTH, MQ], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَمُثَنَّاهُ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«and for its dual»", "«ve tesniyesi için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("مُثَنَّا", "muthanna", "noun"), pr3ms()]),
  F("تَانِ", "ta-ishara", "«tāni» — in rafʿ", "«tâni» — ref'te", "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — مُثَنَّى تَا فِي الرَّفْعِ.", gr=[MTH]),
  wa_("وَتَيْنِ", "ta-ishara", "«and tayni» — in naṣb and jarr", "«ve teyni» — nasb ve cerde", punct="،"),
  tok("وَلِجَمْعِهِمَا", "jam", "noun", [K, AT, HJ, ID, "jam"], "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ حَرْفُ جَرٍّ، وَجَمْعِهِمَا مَجْرُورٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — الْمُذَكَّرِ وَالْمُؤَنَّثِ.", "«and for the plural of both»", "«ve ikisinin cemi için»", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("جَمْعِ", "jam", "noun"), seg("هِمَا", "pron-3d", "pron")]),
  F("أُولَاءِ", "ula-ishara", "«ulāʾi» — these", "«ulâi» — bunlar", "لَفْظٌ مَحْكِيٌّ: مُبْتَدَأٌ مُؤَخَّرٌ — اسْمُ إِشَارَةٍ لِلْجَمْعِ."),
  tok("مَدًّا", "madd", "noun", [K, "hal", MSD], "حَالٌ مَنْصُوبٌ — أُولَاءِ بِالْهَمْزَةِ.", "«long» — أُولَاءِ with the hamza.", "«medli» — hemzeli ulâi."),
  tok("وَقَصْرًا", "qasr", "noun", [K, AT, MSD], "الْوَاوُ عَاطِفَةٌ، وَقَصْرًا مَعْطُوفٌ مَنْصُوبٌ — أُولَى بِلَا هَمْزَةٍ.", "«and short» — أُولَى without it.", "«ve kasırlı» — hemzesiz ulâ.", punct="،", segments=wa("قَصْرًا", "qasr", "noun")),
 ]})
# ----------- s3 — the particle of alerting and the kāf of address
S.append({"id": "s3", "translation": {"en": "and the particle of alerting is prefixed to their beginning — as in «hādhā» — and the kāf of address is joined to their end, so one says «dhāka, dhākumā, dhākum, dhākunna», and so the rest; and the two are combined — as in «hādhāka» —", "tr": "başlarına tenbih harfi gelir — hâzâ gibi — sonlarına hitap kâfı bitişir; zâke, zâkümâ, zâküm, zâkünne denir, diğerleri de böyle; ikisi birleştirilir de — hâzâke gibi —"},
 "tokens": [
  tok("وَيَلْحَقُ", "lahiqa", "verb", [K, AT, MR, FL], "الْوَاوُ عَاطِفَةٌ، وَيَلْحَقُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is prefixed to»", "«ve gelir»", segments=wa("يَلْحَقُ", "lahiqa", "verb")),
  tok("أَوَّلَهَا", "awwal", "noun", [K, MB, ID], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their beginning»", "«başlarına»", segments=[seg("أَوَّلَ", "awwal", "noun"), pr3fs()]),
  tok("حَرْفُ", "harf", "noun", [K, FL, ID, HTN], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the particle of»", "«harfi»"),
  tok("التَّنْبِيهِ", "tanbih", "noun", [K, ID, HTN, MSD, F2], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — هَا.", "«alerting» — هَا.", "«tenbih» — hâ.", punct="،"),
  nahw(),
  F("هٰذَا", "hadha", "«hādhā» — this", "«hâzâ» — bu", "لَفْظٌ مَحْكِيٌّ: هَا لِلتَّنْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ.", punct="،", segments=[seg("هٰ", "ha-tanbih", "part"), seg("ذَا", "dha", "pron")], gr=[HTN]),
  tok("وَيَتَّصِلُ", "ittasala", "verb", [K, AT, MR, FL, "form-viii-verbs"], "الْوَاوُ عَاطِفَةٌ، وَيَتَّصِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«and is joined»", "«ve bitişir»", segments=wa("يَتَّصِلُ", "ittasala", "verb")),
  tok("بِآخِرِهَا", "akhir", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَآخِرِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«to their end»", "«sonlarına»", segments=[seg("بِ", "bi", "prep"), seg("آخِرِ", "akhir", "noun"), pr3fs()]),
  tok("كَافُ", "kaf-letter", "noun", [K, FL, ID], "فَاعِلٌ مَرْفُوعٌ، مُضَافٌ.", "«the kāf of»", "«kâfı»"),
  tok("الْخِطَابِ", "khitab", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حَرْفٌ لَا مَحَلَّ لَهُ، يَتَصَرَّفُ بِحَسَبِ الْمُخَاطَبِ.", "«address» — a particle with no place, varying with the addressee.", "«hitap» — mahalli olmayan, muhâtaba göre değişen harf.", punct="،"),
  tok("فَيُقَالُ", "qala", "verb", [K, AT, NF, HV, MR], "الْفَاءُ لِلتَّفْرِيعِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«so one says»", "«denir ki»", punct=":", segments=fa("يُقَالُ", "qala", "verb")),
  F("ذَاكَ", "dhaka", "«dhāka» — that (to one man)", "«zâke» — şu (bir erkeğe)", "لَفْظٌ مَحْكِيٌّ: ذَا اسْمُ إِشَارَةٍ، وَالْكَافُ لِلْخِطَابِ.", segments=[seg("ذَا", "dha", "pron"), seg("كَ", "kaf-khitab", "part")]),
  F("ذَاكُمَا", "dhaka", "«dhākumā» — (to two)", "«zâkümâ» — (ikinize)", "ذَا، وَكُمَا لِلْخِطَابِ.", segments=[seg("ذَا", "dha", "pron"), seg("كُمَا", "kaf-khitab", "part")]),
  F("ذَاكُمْ", "dhaka", "«dhākum» — (to many)", "«zâküm» — (size)", "ذَا، وَكُمْ لِلْخِطَابِ.", segments=[seg("ذَا", "dha", "pron"), seg("كُمْ", "kaf-khitab", "part")]),
  F("ذَاكُنَّ", "dhaka", "«dhākunna» — (to women)", "«zâkünne» — (kadınlara)", "ذَا، وَكُنَّ لِلْخِطَابِ.", punct="،", segments=[seg("ذَا", "dha", "pron"), seg("كُنَّ", "kaf-khitab", "part")]),
  tok("وَكَذَا", "kadha", "part", [K, AT, HJ, MK], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ حَرْفُ جَرٍّ، وَذَا فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ.", "«and so»", "«ve böyledir»", segments=wa("كَذَا", "kadha", "part")),
  tok("الْبَوَاقِي", "bawaqi", "noun", [K, MK, JT, MQ], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — تَاكَ وَذَانِكَ وَأُولَئِكَ.", "«the rest» — tāka, dhānika, ulāʾika.", "«diğerleri» — tâke, zânike, ulâike.", punct="،"),
  tok("وَيُجْمَعُ", "jamaa-gather", "verb", [K, AT, NF, MR], "الْوَاوُ عَاطِفَةٌ، وَيُجْمَعُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and are combined»", "«ve birleştirilir»", segments=wa("يُجْمَعُ", "jamaa-gather", "verb")),
  tok("بَيْنَهُمَا", "bayna", "noun", [K, MF, ID, NF], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ، وَهِمَا مُضَافٌ إِلَيْهِ — نَائِبُ الْفَاعِلِ مَحَلًّا: حَرْفُ التَّنْبِيهِ وَكَافُ الْخِطَابِ.", "«the two» — the alerting particle and the kāf.", "«ikisi» — tenbih harfi ve kâf.", punct="،", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  nahw(),
  F("هٰذَاكَ", "hadha", "«hādhāka»", "«hâzâke»", "لَفْظٌ مَحْكِيٌّ: هَا لِلتَّنْبِيهِ، وَذَا اسْمُ إِشَارَةٍ، وَالْكَافُ لِلْخِطَابِ.", punct="،", segments=[seg("هٰ", "ha-tanbih", "part"), seg("ذَا", "dha", "pron"), seg("كَ", "kaf-khitab", "part")], gr=[HTN]),
 ]})
# ----------- s4 — the far forms
S.append({"id": "s4", "translation": {"en": "and one says «tilka», «ulālika», «dhālika», «dhānnika» and «tānnika» — the two with shadda — for the far;", "tr": "uzak için tilke, ulâlike, zâlike, zânnike ve tânnike — ikisi şeddeli — denir;"},
 "tokens": [
  tok("وَيُقَالُ", "qala", "verb", [K, AT, NF, HV, MR], "الْوَاوُ عَاطِفَةٌ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«and one says»", "«ve denir»", punct=":", segments=wa("يُقَالُ", "qala", "verb")),
  F("تِلْكَ", "tilka", "«tilka» — that (f.)", "«tilke» — şu (dişil)", "لَفْظٌ مَحْكِيٌّ: تِي، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ."),
  wa_("وَأُولَالِكَ", "ulalika", "«and ulālika» — those", "«ve ulâlike» — şunlar", ar="أُولَالِكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: أُولَى، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ."),
  wa_("وَذٰلِكَ", "dhalika", "«and dhālika» — that", "«ve zâlike» — şu", ar="ذٰلِكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ: ذَا، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ."),
  wa_("وَذَانِّكَ", "dhanika", "«and dhānnika» — those two", "«ve zânnike» — şu ikisi", ar="ذَانِّكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مُثَنَّى ذَا مَعَ الْكَافِ، وَالنُّونُ مُشَدَّدَةٌ عِوَضًا عَنْ لَامِ الْبُعْدِ."),
  wa_("وَتَانِّكَ", "tanika", "«and tānnika» — those two (f.)", "«ve tânnike» — şu ikisi (dişil)", punct="،", ar="تَانِّكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — مُثَنَّى تَا مَعَ الْكَافِ، وَالنُّونُ مُشَدَّدَةٌ."),
  tok("مُشَدَّدَتَيْنِ", "mushaddad", "noun", [K, "hal", IMF, F2, MTH], "حَالٌ مِنَ الْأَخِيرَيْنِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — بِتَشْدِيدِ النُّونِ.", "«the two with shadda» — the nūn doubled.", "«ikisi şeddeli» — nûn şeddeli.", punct="،"),
  li_("لِلْبَعِيدِ", "baid", "«for the far»", "«uzak için»", punct="،", gr=[ISH]),
 ]})
# ----------- s5 — the place-demonstratives
S.append({"id": "s5", "translation": {"en": "and as for «thammata», «hunā», «hāhunā», «hunnā» and «hunāka», they are for place only.", "tr": "semmete, hünâ, hâhünâ, hünnâ ve hünâke ise yalnız mekân içindir."},
 "tokens": [
  tok("وَأَمَّا", "amma", "part", [K, AT, AMT], "الْوَاوُ عَاطِفَةٌ، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ.", "«and as for»", "«… -e gelince»", segments=wa("أَمَّا", "amma", "part")),
  tok("ثَمَّةَ", "thamma", "noun", [K, MK, AMT, ISH, MF], "لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ رَفْعٍ، مُبْتَدَأٌ — اسْمُ إِشَارَةٍ لِلْمَكَانِ الْبَعِيدِ.", "«thammata» — there (far).", "«semmete» — orada (uzak)."),
  tok("وَهُنَا", "huna", "noun", [K, AT, ISH, MF], "الْوَاوُ عَاطِفَةٌ، وَهُنَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — لِلْمَكَانِ الْقَرِيبِ.", "«and hunā» — here.", "«ve hünâ» — burada.", segments=wa("هُنَا", "huna", "noun")),
  tok("وَهٰهُنَا", "hahuna", "noun", [K, AT, ISH, MF, HTN], "الْوَاوُ عَاطِفَةٌ، وَهٰهُنَا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — هُنَا مَعَ حَرْفِ التَّنْبِيهِ.", "«and hāhunā» — here, with the alerting hā.", "«ve hâhünâ» — tenbih hâ'sıyla burada.", segments=[seg("وَ", "wa", "conj"), seg("هٰ", "ha-tanbih", "part"), seg("هُنَا", "huna", "noun")]),
  tok("وَهُنَّا", "hunna-place", "noun", [K, AT, ISH, MF], "الْوَاوُ عَاطِفَةٌ، وَهُنَّا لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — بِالتَّشْدِيدِ، لِلْمَكَانِ الْبَعِيدِ.", "«and hunnā» — there, with shadda.", "«ve hünnâ» — şeddeli, uzak için.", segments=wa("هُنَّا", "hunna-place", "noun")),
  tok("وَهُنَاكَ", "hunaka", "noun", [K, AT, ISH, MF], "الْوَاوُ عَاطِفَةٌ، وَهُنَاكَ لَفْظٌ مَحْكِيٌّ مَعْطُوفٌ — هُنَا مَعَ كَافِ الْخِطَابِ.", "«and hunāka» — there, with the kāf.", "«ve hünâke» — kâf ile orada.", segments=[seg("وَ", "wa", "conj"), seg("هُنَا", "huna", "noun"), seg("كَ", "kaf-khitab", "part")]),
  tok("فَلِلْمَكَانِ", "makan", "noun", [K, FK, HJ, MK], "الْفَاءُ وَاقِعَةٌ فِي الْخَبَرِ، وَاللَّامُ حَرْفُ جَرٍّ، وَالْمَكَانِ مَجْرُورٌ — خَبَرٌ.", "«then they are for place» — the khabar.", "«mekân içindir» — haber.", segments=[seg("فَ", "fa", "conj"), seg("لِ", "li", "prep"), seg("الْمَكَانِ", "makan", "noun")]),
  tok("خَاصَّةً", "khassa", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ — لَا تُشِيرُ إِلَى غَيْرِ الْمَكَانِ.", "«only» — pointing to nothing but place.", "«yalnız» — mekândan başkasına işaret etmez.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "ta-ishara": G("ta-ishara", "تَا", "ت ا", "pron", "tā — the feminine demonstrative «this» (also tī, tih, tihī; dual tāni/tayni)", "tâ — dişil işaret ismi «bu» (tî, tih, tihî de; tesniye tâni/teyni)", 3),
 "ula-ishara": G("ula-ishara", "أُولَاءِ", "أ ل ي", "pron", "ulāʾi — the plural demonstrative «these» (short form ulā)", "ulâi — çoğul işaret ismi «bunlar» (kasırlı ulâ)", 3),
 "ulalika": G("ulalika", "أُولَالِكَ", "أ ل ي", "pron", "ulālika — «those» (plural, far, with the lām of distance)", "ulâlike — «şunlar» (çoğul, uzak, bu'd lâmıyla)", 4),
 "dhanika": G("dhanika", "ذَانِّكَ", "ذ ا", "pron", "dhānnika — «those two» (masculine dual, far, the nūn doubled)", "zânnike — «şu ikisi» (müzekker tesniye, uzak, nûn şeddeli)", 4),
 "tanika": G("tanika", "تَانِّكَ", "ت ا", "pron", "tānnika — «those two» (feminine dual, far, the nūn doubled)", "tânnike — «şu ikisi» (müennes tesniye, uzak, nûn şeddeli)", 4),
 "ha-tanbih": G("ha-tanbih", "هَا", "ه ا", "part", "hā — the particle of alerting prefixed to demonstratives (hādhā)", "hâ — işaret isimlerinin başına gelen tenbih harfi (hâzâ)", 3),
 "kaf-khitab": G("kaf-khitab", "كَ", "ك", "part", "the kāf of address — a suffixed particle varying with the addressee (dhāka, dhākum)", "hitap kâfı — muhâtaba göre değişen ek harf (zâke, zâküm)", 3),
 "mushaddad": G("mushaddad", "مُشَدَّد", "ش د د", "noun", "doubled, carrying a shadda", "şeddeli", 3),
 "hahuna": G("hahuna", "هٰهُنَا", "ه ن", "noun", "hāhunā — «here», hunā with the alerting hā", "hâhünâ — «burada», tenbih hâ'sıyla hünâ", 3),
 "hunna-place": G("hunna-place", "هُنَّا", "ه ن", "noun", "hunnā — «there» (far), with shadda", "hünnâ — «orada» (uzak), şeddeli", 4),
 "madd": G("madd", "مَدّ", "م د د", "noun", "lengthening — the long form with the hamza (ulāʾi)", "med — hemzeli uzun şekil (ulâi)", 3),
}
used = set()
for s in S:
    for t in s["tokens"]:
        used.add(t["lex"])
        for sg_ in t.get("segments", []): used.add(sg_["lex"])
CAND = {}
for k in sorted(used):
    if k in TG: continue
    if k in NEW: CAND[k] = NEW[k]
    elif _ic.has_gloss(k): CAND[k] = find_gloss(k)
    else: raise SystemExit(f"no gloss anywhere for {k}")
GLOSS_ADD = {k: v for k, v in CAND.items() if v and k not in TG}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"] and _ic.has_morph(_k):
        mo["verbs"][_k] = find_morph(_k)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch47 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("lahiqa", "ittasala", "qala", "jamaa-gather") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "أَسْمَاءُ الْإِشَارَةِ: صِيَغُ الْقَرِيبِ وَالْبَعِيدِ، هَا التَّنْبِيهِ وَكَافُ الْخِطَابِ، وَإِشَارَاتُ الْمَكَانِ", "en": "The demonstratives: the near and far forms, the alerting hā and the kāf of address, and the place-demonstratives", "tr": "İşaret isimleri: yakın ve uzak şekilleri, tenbih hâ'sı ve hitap kâfı, mekân işaretleri"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المعرفة: أسماء الإشارة", "الكافية لابن الحاجب — أسماء الإشارة", "شرح قطر الندى لابن هشام — اسم الإشارة"],
 "amil": "the third maʿrifa, the demonstrative: ذَا (m.), ذَانِ / ذَيْنِ (m. dual, rafʿ / naṣb-jarr), تَا، ذِي، تِي، تِهْ، ذِهْ، تِهِي، ذِهِي (f.), تَانِ / تَيْنِ (f. dual), أُولَاءِ / أُولَى (plural of both); the alerting هَا before (هٰذَا), the kāf of address after, shaped by the addressee (ذَاكَ، ذَاكُمَا، ذَاكُمْ، ذَاكُنَّ), both together (هٰذَاكَ); the far forms تِلْكَ، أُولَالِكَ، ذٰلِكَ with the lām of distance, ذَانِّكَ، تَانِّكَ with the doubled nūn; ثَمَّةَ، هُنَا، هٰهُنَا، هُنَّا، هُنَاكَ point to place only — all built words, their place of iʿrāb by their position",
 "question": {
  "en": ["What are the near demonstratives? ذَا for the masculine, its dual ذَانِ in rafʿ and ذَيْنِ in naṣb and jarr; تَا، ذِي، تِي، تِهْ، ذِهْ، تِهِي، ذِهِي for the feminine, its dual تَانِ and تَيْنِ; أُولَاءِ, long or short أُولَى, for the plural of both.",
         "What is the hā in هٰذَا? The particle of alerting, prefixed; and the kāf in ذَاكَ? The kāf of address, suffixed, a particle with no place that takes the addressee's shape — ذَاكَ، ذَاكِ، ذَاكُمَا، ذَاكُمْ، ذَاكُنَّ.",
         "May both be joined? Yes — هٰذَاكَ; the lām of distance, though, refuses the hā: no هٰذٰلِكَ.",
         "What are the far forms? تِلْكَ، أُولَالِكَ، ذٰلِكَ with the lām of distance and the kāf; ذَانِّكَ and تَانِّكَ for the duals, the nūn doubled in place of the lām.",
         "Which demonstratives point to place only? ثَمَّةَ (far), هُنَا and هٰهُنَا (near), هُنَّا and هُنَاكَ (far) — ẓarfs of place, never pointing to a person or a thing.",
         "Are the demonstratives declinable? No — built, like the pronouns; only the duals ذَانِ / ذَيْنِ and تَانِ / تَيْنِ show the dual's two shapes.",
         "What does the engine READ here? The DabtEngine keeps every cited demonstrative at the author's form as a built word, reads the لِ-phrases (لِلْمُذَكَّرِ، لِمُثَنَّاهُ، لِلْمُؤَنَّثِ، لِجَمْعِهِمَا) as fronted khabars with the cited form as the delayed mubtadaʾ, مَدًّا وَقَصْرًا as ḥāls, and فَلِلْمَكَانِ as the khabar after أَمَّا."],
  "tr": ["Yakın işaret isimleri hangileridir? Müzekker için zâ, tesniyesi ref'te zâni, nasb ve cerde zeyni; müennes için tâ, zî, tî, tih, zih, tihî, zihî, tesniyesi tâni ve teyni; ikisinin cemi için medli ulâi veya kasırlı ulâ.",
         "Hâzâ'daki hâ nedir? Başa gelen tenbih harfi; zâke'deki kâf? Sona bitişen, mahalli olmayan, muhâtabın şeklini alan hitap kâfı — zâke, zâki, zâkümâ, zâküm, zâkünne.",
         "İkisi birleşebilir mi? Evet — hâzâke; bu'd lâmı ise hâ'yı reddeder: hâzâlike denmez.",
         "Uzak şekiller nelerdir? Bu'd lâmı ve kâf ile tilke, ulâlike, zâlike; tesniyeler için lâm yerine nûn şeddeli zânnike ve tânnike.",
         "Hangi işaretler yalnız mekâna işaret eder? Semmete (uzak), hünâ ve hâhünâ (yakın), hünnâ ve hünâke (uzak) — mekân zarfları; kişiye veya şeye işaret etmezler.",
         "İşaret isimleri mu'rab mıdır? Hayır — zamirler gibi mebnîdir; yalnız tesniyeler zâni/zeyni ve tâni/teyni tesniyenin iki şeklini gösterir.",
         "Motor burada neyi OKUR? DabtEngine alıntılanan her işaret ismini mebnî kelime olarak yazarın şeklinde tutar; li-öbeklerini (li'l-müzekker, li-müsennâhu, li'l-müennes, li-cem'ihimâ) sona alınmış mübtedâlı öne alınmış haber; medden ve kasran'ı hâl; fe-li'l-mekân'ı emmâ'dan sonraki haber okur."],
 },
 "plain": {"en": "Pointing words: «dhā» (this, m.), «tā/tī» (this, f.), duals «dhāni/dhayni» and «tāni/tayni», plural «ulāʾi». «Hā» in front alerts the listener («hādhā»); a «k» at the end addresses him and changes with him («dhāka, dhākum»). «Tilka, dhālika, ulālika» point to the far; «hunā, thammata, hunāka» point only to a place.",
           "tr": "İşaret sözcükleri: «zâ» (bu, eril), «tâ/tî» (bu, dişil), tesniyeler «zâni/zeyni» ve «tâni/teyni», çoğul «ulâi». Öndeki «hâ» dinleyeni uyarır («hâzâ»); sondaki «k» muhataba seslenir ve ona göre değişir («zâke, zâküm»). «Tilke, zâlike, ulâlike» uzağı gösterir; «hünâ, semmete, hünâke» yalnız yeri gösterir."},
 "explanation": {"en": "The third kind of maʿrifa is the demonstratives: ذَا for the masculine, and for its dual ذَانِ and ذَيْنِ; for the feminine تَا، ذِي، تِي، تِهْ، ذِهْ، تِهِي، ذِهِي, and for its dual تَانِ and تَيْنِ; for the plural of both أُولَاءِ, long and short. The particle of alerting is prefixed (هٰذَا) and the kāf of address suffixed, so one says ذَاكَ ذَاكُمَا ذَاكُمْ ذَاكُنَّ and so the rest; both may be combined (هٰذَاكَ). One says تِلْكَ، أُولَالِكَ، ذٰلِكَ، ذَانِّكَ، تَانِّكَ — the last two with the doubled nūn — for the far. ثَمَّةَ، هُنَا، هٰهُنَا، هُنَّا and هُنَاكَ are for place only.",
                 "tr": "Ma'rifenin üçüncü nev'i işaret isimleridir: müzekker için zâ, tesniyesi için zâni ve zeyni; müennes için tâ, zî, tî, tih, zih, tihî, zihî, tesniyesi için tâni ve teyni; ikisinin cemi için medli ve kasırlı ulâi. Başlarına tenbih harfi gelir (hâzâ), sonlarına hitap kâfı bitişir; zâke zâkümâ zâküm zâkünne ve diğerleri böyle denir; ikisi birleştirilebilir (hâzâke). Uzak için tilke, ulâlike, zâlike, zânnike, tânnike — son ikisi nûn şeddeli — denir. Semmete, hünâ, hâhünâ, hünnâ ve hünâke yalnız mekân içindir."},
 "examples": [
  {"ar": "ذَا لِلْمُذَكَّرِ، وَلِمُثَنَّاهُ ذَانِ وَذَيْنِ", "en": "the masculine and its dual", "tr": "müzekker ve tesniyesi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "تَا وَذِي وَتِي وَتِهْ وَذِهْ وَتِهِي وَذِهِي … أُولَاءِ مَدًّا وَقَصْرًا", "en": "the feminine forms and the plural", "tr": "müennes şekiller ve cemi", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "هٰذَا؛ ذَاكَ ذَاكُمَا ذَاكُمْ ذَاكُنَّ؛ هٰذَاكَ", "en": "the alerting hā and the kāf of address", "tr": "tenbih hâ'sı ve hitap kâfı", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "تِلْكَ وَأُولَالِكَ وَذٰلِكَ وَذَانِّكَ وَتَانِّكَ لِلْبَعِيدِ", "en": "the far forms", "tr": "uzak şekiller", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
  {"ar": "ثَمَّةَ وَهُنَا وَهٰهُنَا وَهُنَّا وَهُنَاكَ فَلِلْمَكَانِ خَاصَّةً", "en": "the place-demonstratives", "tr": "mekân işaretleri", "sourceStory": "izhar-al-asrar", "sentence": "s5"},
 ],
 "commonMistakes": [
  {"wrong": "رَأَيْتُ ذَانِ الرَّجُلَيْنِ", "right": "رَأَيْتُ ذَيْنِ الرَّجُلَيْنِ", "why": {"en": "the dual demonstrative shows naṣb and jarr by the yāʾ, like the dual noun", "tr": "tesniye işaret ismi nasb ve cerri tesniye isim gibi yâ ile gösterir"}},
  {"wrong": "هٰذٰلِكَ", "right": "ذٰلِكَ (or هٰذَاكَ)", "why": {"en": "the alerting hā is not combined with the lām of distance", "tr": "tenbih hâ'sı bu'd lâmıyla birleşmez"}},
  {"wrong": "هُنَاكَ الرَّجُلُ (pointing to the man himself)", "right": "ذٰلِكَ الرَّجُلُ", "why": {"en": "هُنَاكَ and its sisters point to place only", "tr": "hünâke ve kardeşleri yalnız mekâna işaret eder"}},
 ],
}
ADD_EN = (" Chapter 47 (print pp. 142-143): the demonstratives — the masculine and its dual (s1), the feminine forms, its dual and the plural (s2), the alerting hā, the kāf of address and their combination (s3), the far forms (s4), the place-demonstratives (s5).")
ADD_TR = (" Kırk yedinci bab (baskı s. 142-143): işaret isimleri — müzekker ve tesniyesi (s1), müennes şekiller, tesniyesi ve cemi (s2), tenbih hâ'sı, hitap kâfı ve birleşmeleri (s3), uzak şekiller (s4), mekân işaretleri (s5).")
write_out(47, S, TITLE, ADD_EN, ADD_TR, "pp. 142-143", GLOSS_ADD, notes=(NOTE,),
          related=((K46, [K]), (ISH, [K]), (TRF, [K]), (HTN, [K]), (MMB, [K]), (MTH, [K])))
report(47, S, GLOSS_ADD, (NOTE,))
