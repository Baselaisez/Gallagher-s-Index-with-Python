# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 26: the FEMININE is what carries the feminine sign in wording or in estimate — the tāʾ paused on
# as hāʾ (طَلْحَة، شَمْس), the shortened alif (حُبْلَى، دَعْوَى), the lengthened alif (حَمْرَاء); not so in three to ten, whose masculine
# takes the tāʾ and whose feminine drops it (ثَلَاثَةُ رِجَالٍ، أَرْبَعُ نِسْوَةٍ); compounded with ten, the tāʾ stays on the first only in the
# masculine (ثَلَاثَةَ عَشَرَ رَجُلًا) and on the second only in the feminine (ثَلَاثَ عَشْرَةَ امْرَأَةً). Print pp. 126–127.
# The print writes ثلثة with the dagger alif; the standard ثَلَاثَة of the earlier chapters is kept.
#   python3 author_izhar_ch26.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from izhar_common import *
import izhar_common as _ic
PKG = _ic.PKG

K = "al-muannath-wa-alamatuh"
K25 = "al-fail-al-muzhar-wa-tanith-amilih"
TITLE = {"ar": "الْمُؤَنَّثُ وَعَلَامَاتُهُ", "en": "The feminine and its signs", "tr": "Müennes ve alâmetleri"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
HJ = "huruf-jarr"; MK = "mubtada-khabar"; ID = "idafa-definiteness"; AT = "atf-nasaq"; NA = "naat-sifa"; HT = "hadhf-wa-taqdir"; MF = "maful-fih"; FL = "fail"; NF = "naib-al-fail"; MTH = "al-muthanna"; IMF = "ism-maful"; IFA = "ism-fail"
HL = "hal"; MSD = "masdar"; MR = "mudari-marfu"; JMA = "jam-muannath-salim"; JT = "jam-taksir"; MAW = "ism-mawsul"; IN = "inna-wa-akhawatuha"; TM = "tamyiz"; ADD = "tamyiz"; MQ = "ism-maqsur-manqus"; MMD = "mamdud-maqsur" if False else "ism-maqsur-manqus"
IDH = "idha-shartiyya"; ISH = "asma-al-ishara"; MM = "maful-mutlaq"; NSB = "ism-mansub"; DIP = "mamnu-min-sarf"

def nahw(punct=":"): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)

# ----------- s1 — the feminine defined
S.append({"id": "s1", "translation": {"en": "And the feminine is what carries the sign of the feminine, in wording or in estimate;", "tr": "Müennes, lafzan veya takdîren te'nîs alâmeti taşıyandır;"},
 "tokens": [
  tok("وَالْمُؤَنَّثُ", "muannath", "noun", [K, AT, MK, IMF], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُؤَنَّثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the feminine» — the mubtada.", "«müennes» — mübtedâ.", segments=wa("الْمُؤَنَّثُ", "muannath", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what» — the khabar.", "«… olan» — haber."),
  tok("فِيهِ", "fi", "prep", [K, HJ, MK, MAW], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ فِي مَحَلِّ جَرٍّ — خَبَرٌ مُقَدَّمٌ فِي الصِّلَةِ.", "«in it» — the fronted khabar of the relative clause.", "«onda» — sılanın öne alınmış haberi.", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("عَلَامَةُ", "alama", "noun", [K, MK, ID, MAW], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the sign of»", "«alâmeti»"),
  tok("التَّأْنِيثِ", "tanith", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the feminine»", "«te'nîs»"),
  tok("لَفْظًا", "lafz", "noun", [K, TM, HL], "تَمْيِيزٌ أَوْ حَالٌ مَنْصُوبٌ — ظَاهِرَةً فِي اللَّفْظِ.", "«in wording» — a sign shown.", "«lafzan» — lafızda görünen."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«veya»"),
  tok("تَقْدِيرًا", "taqdir", "noun", [K, AT, TM, MSD], "مَعْطُوفٌ مَنْصُوبٌ — مُقَدَّرَةً كَشَمْسٍ.", "«in estimate» — as in شَمْس.", "«takdîren» — şems gibi.", punct="؛"),
 ]})
# ----------- s2 — the three signs
S.append({"id": "s2", "translation": {"en": "and that is the tāʾ paused on as hāʾ — as in Ṭalḥa and shams — and the shortened alif — as in ḥublā and daʿwā — and the lengthened alif — as in ḥamrāʾ.", "tr": "o da üzerinde hâ olarak durulan tâ — Talha ve şems gibi —, elif-i maksûre — hublâ ve da'vâ gibi — ve elif-i memdûdedir — hamrâ gibi."},
 "tokens": [
  tok("وَهِيَ", "hiya", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْعَلَامَةُ.", "«and it is» — the sign.", "«o da» — alâmet.", segments=wa("هِيَ", "hiya", "pron")),
  tok("التَّاءُ", "ta-letter", "noun", [K, MK], "خَبَرٌ مَرْفُوعٌ.", "«the tāʾ»", "«tâ»"),
  tok("الْمَوْقُوفُ", "mawquf", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«paused on»", "«vakfedilen»"),
  tok("عَلَيْهَا", "ala", "prep", [K, HJ, NF], "عَلَى حَرْفُ جَرٍّ، وَهَا فِي مَحَلِّ جَرٍّ — نَائِبُ فَاعِلِ الْمَوْقُوفِ.", "«on which» — the participle's deputy doer.", "«üzerinde» — ism-i mef'ûlün nâibi.", segments=[seg("عَلَيْ", "ala", "prep"), pr3fs()]),
  tok("هَاءً", "ha-letter", "noun", [K, HL], "حَالٌ مَنْصُوبٌ — تُقْلَبُ هَاءً فِي الْوَقْفِ.", "«as hāʾ» — turned to hāʾ at the pause.", "«hâ olarak» — vakıfta hâya döner.", punct="،"),
  nahw(),
  tok("طَلْحَةَ", "talha", "propn", [K, DIP, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.", "«Ṭalḥa» — a diptote: a name with the tāʾ.", "«Talha» — alemlik ve te'nîs ile gayr-ı munsarif."),
  tok("وَشَمْسٍ", "shams", "noun", [K, AT], "الْوَاوُ عَاطِفَةٌ، وَشَمْسٍ مَعْطُوفٌ مَجْرُورٌ — تَاؤُهَا مُقَدَّرَةٌ.", "«and shams» — its tāʾ estimated.", "«ve şems» — tâsı takdîrî.", punct="،", segments=wa("شَمْسٍ", "shams", "noun")),
  tok("وَالْأَلِفُ", "alif-letter", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْأَلِفُ مَعْطُوفٌ عَلَى التَّاءُ مَرْفُوعٌ.", "«and the alif»", "«ve elif»", segments=wa("الْأَلِفُ", "alif-letter", "noun")),
  tok("الْمَقْصُورَةُ", "maqsur", "noun", [K, NA, MQ, IMF], "نَعْتٌ مَرْفُوعٌ.", "«shortened»", "«maksûre»", punct="،"),
  nahw(),
  tok("حُبْلَى", "hubla", "noun", [K, MQ, DIP, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ.", "«ḥublā» — pregnant: a diptote by the alif.", "«hublâ» — hâmile: te'nîs elifi ile gayr-ı munsarif."),
  tok("وَدَعْوَى", "dawa-claim", "noun", [K, AT, MQ, DIP], "الْوَاوُ عَاطِفَةٌ، وَدَعْوَى مَعْطُوفٌ.", "«and daʿwā» — a claim.", "«ve da'vâ» — iddia.", punct="،", segments=wa("دَعْوَى", "dawa-claim", "noun")),
  tok("وَالْأَلِفُ", "alif-letter", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالْأَلِفُ مَعْطُوفٌ مَرْفُوعٌ.", "«and the alif»", "«ve elif»", segments=wa("الْأَلِفُ", "alif-letter", "noun")),
  tok("الْمَمْدُودَةُ", "mamdud", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«lengthened»", "«memdûde»", punct="،"),
  nahw(),
  tok("حَمْرَاءَ", "hamra", "noun", [K, DIP, ID], "لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.", "«ḥamrāʾ» — red: a diptote by the lengthened alif.", "«hamrâ» — kırmızı: memdûde elifle gayr-ı munsarif.", punct="."),
 ]})
# ----------- s3 — three to ten reversed
S.append({"id": "s3", "translation": {"en": "And this is in other than three to ten; for their masculine takes the tāʾ and their feminine drops it — as in «three men» and «four women».", "tr": "Bu, üçten ona kadar olanların dışındadır; çünkü onların müzekkeri tâ ile, müennesi tânın hazfiyledir: «üç adam», «dört kadın» gibi."},
 "tokens": [
  tok("وَهٰذَا", "hadha", "pron", [K, AT, MK, ISH], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهٰذَا اسْمُ إِشَارَةٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ — الْحُكْمُ الْمَذْكُورُ.", "«and this» — the ruling just given.", "«bu» — zikredilen hüküm.", segments=wa("هٰذَا", "hadha", "pron")),
  tok("فِي", "fi", "prep", [K, HJ, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«in» — the khabar.", "«-de» — haber."),
  tok("غَيْرِ", "ghayr", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«other than»", "«dışında»"),
  tok("ثَلَاثَةٍ", "thalatha", "noun", [K, ID, ADD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«three»", "«üç»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ لِلْغَايَةِ.", "«to»", "«-e kadar»"),
  tok("عَشَرَةٍ", "ashara", "noun", [K, HJ, ADD], "مَجْرُورٌ بِإِلَى.", "«ten»", "«on»", punct="،"),
  tok("فَإِنَّ", "inna", "part", [K, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for»", "«çünkü»", segments=fa("إِنَّ", "inna", "part")),
  tok("مُذَكَّرَهَا", "mudhakkar", "noun", [K, IN, ID, IMF], "اسْمُ إِنَّ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«their masculine» — inna's ism.", "«müzekkeri» — inne'nin ismi.", segments=[seg("مُذَكَّرَ", "mudhakkar", "noun"), pr3fs()]),
  tok("بِالتَّاءِ", "ta-letter", "noun", [K, HJ, IN], "الْبَاءُ حَرْفُ جَرٍّ، وَالتَّاءِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«with the tāʾ» — inna's khabar.", "«tâ ile» — inne'nin haberi.", segments=[seg("بِ", "bi", "prep"), seg("التَّاءِ", "ta-letter", "noun")]),
  tok("وَمُؤَنَّثَهَا", "muannath", "noun", [K, AT, IN, ID, IMF], "الْوَاوُ عَاطِفَةٌ، وَمُؤَنَّثَهَا مَعْطُوفٌ عَلَى اسْمِ إِنَّ مَنْصُوبٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«and their feminine»", "«ve müennesi»", segments=[seg("وَ", "wa", "conj"), seg("مُؤَنَّثَ", "muannath", "noun"), pr3fs()]),
  tok("بِحَذْفِهَا", "hadhf", "noun", [K, HJ, ID, MSD, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَحَذْفِهَا مَجْرُورٌ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — خَبَرٌ.", "«with dropping it»", "«onun hazfiyle»", punct="،", segments=[seg("بِ", "bi", "prep"), seg("حَذْفِ", "hadhf", "noun"), pr3fs()]),
  nahw(),
  tok("ثَلَاثَةُ", "thalatha", "noun", [K, ID, ADD], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ — بِالتَّاءِ لِلْمَعْدُودِ الْمُذَكَّرِ.", "«three» — with the tāʾ for the masculine counted.", "«üç» — müzekker ma'dûd için tâlı."),
  tok("رِجَالٍ", "rijal", "noun", [K, ID, JT, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — تَمْيِيزُ الْعَدَدِ.", "«men»", "«adam»"),
  tok("وَأَرْبَعُ", "arba", "noun", [K, AT, ID, ADD], "الْوَاوُ عَاطِفَةٌ، وَأَرْبَعُ مَعْطُوفٌ، مُضَافٌ — بِلَا تَاءٍ لِلْمَعْدُودِ الْمُؤَنَّثِ.", "«and four» — without the tāʾ for the feminine counted.", "«ve dört» — müennes ma'dûd için tâsız.", segments=wa("أَرْبَعُ", "arba", "noun")),
  tok("نِسْوَةٍ", "niswa", "noun", [K, ID, JT, TM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِلَّةٍ لِامْرَأَةٍ.", "«women» — a plural of paucity.", "«kadın» — kıllet cem'i.", punct="."),
 ]})
# ----------- s4 — compounded with ten
S.append({"id": "s4", "translation": {"en": "And when three to nine are compounded with ten, the tāʾ is kept on the first only in the masculine — as in «thirteen men» — and on the second only in the feminine — as in «thirteen women».", "tr": "Üçten dokuza kadar olanlar on ile terkîb edilince tâ müzekkerde yalnız ilkinde kalır — «on üç adam» gibi —, müenneste yalnız ikincisinde — «on üç kadın» gibi."},
 "tokens": [
  tok("وَإِذَا", "idha", "part", [K, AT, IDH, MF], "الْوَاوُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when»", "«ve … -ınca»", segments=wa("إِذَا", "idha", "part")),
  tok("رُكِّبَتْ", "rakkaba", "verb", [K, NF, "form-ii-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.", "«are compounded»", "«terkîb edilir»"),
  tok("ثَلَاثَةٌ", "thalatha", "noun", [K, NF, ADD], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«three» — the deputy doer.", "«üç» — nâib-i fâil."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e kadar»"),
  tok("التِّسْعَةِ", "tisa", "noun", [K, HJ, ADD], "مَجْرُورٌ بِإِلَى.", "«nine»", "«dokuz»"),
  tok("مَعَ", "maa", "noun", [K, MF, ID], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with»", "«ile»"),
  tok("عَشَرَةٍ", "ashara", "noun", [K, ID, ADD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«ten»", "«on»", punct="،"),
  tok("أُثْبِتَتِ", "athbata", "verb", [K, NF, "form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ لِالْتِقَاءِ السَّاكِنَيْنِ — جَوَابُ إِذَا.", "«is kept» — the answer of idhā.", "«sabit kalır» — izâ'nın cevâbı."),
  tok("التَّاءُ", "ta-letter", "noun", [K, NF], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the tāʾ»", "«tâ»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«-de»"),
  tok("الْأَوَّلِ", "awwal", "noun", [K, HJ], "مَجْرُورٌ بِفِي — الْجُزْءِ الْأَوَّلِ.", "«the first» — the first part.", "«ilk» — ilk cüz."),
  tok("فَقَطْ", "faqat", "part", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ اسْمُ فِعْلٍ بِمَعْنَى حَسْبُ.", "«only»", "«yalnız»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, HJ, IMF], "مَجْرُورٌ بِفِي.", "«the masculine»", "«müzekkerde»", punct="،"),
  nahw(),
  tok("ثَلَاثَةَ", "thalatha", "noun", [K, ADD, MK], "لَفْظٌ مَحْكِيٌّ: الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ — بِالتَّاءِ.", "«three-» — built on the fatḥa, with the tāʾ.", "«üç-» — fetha üzere mebnî, tâlı."),
  tok("عَشَرَ", "ashar", "noun", [K, ADD], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — بِلَا تَاءٍ.", "«-teen» — without the tāʾ.", "«on» — tâsız."),
  tok("رَجُلًا", "rajul", "noun", [K, TM], "تَمْيِيزٌ مَنْصُوبٌ.", "«men» — the tamyīz.", "«adam» — temyîz.", punct="،"),
  tok("وَفِي", "fi", "prep", [K, AT, HJ], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ.", "«and on»", "«ve -de»", segments=wa("فِي", "fi", "prep")),
  tok("الثَّانِي", "thani", "noun", [K, HJ, MQ], "مَجْرُورٌ بِفِي بِكَسْرَةٍ مُقَدَّرَةٍ.", "«the second»", "«ikinci»"),
  tok("فَقَطْ", "faqat", "part", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ بِمَعْنَى حَسْبُ.", "«only»", "«yalnız»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("الْمُؤَنَّثِ", "muannath", "noun", [K, HJ, IMF], "مَجْرُورٌ بِفِي.", "«the feminine»", "«müenneste»", punct="،"),
  nahw(),
  tok("ثَلَاثَ", "thalath", "noun", [K, ADD, MK], "لَفْظٌ مَحْكِيٌّ: الْجُزْءُ الْأَوَّلُ مَبْنِيٌّ عَلَى الْفَتْحِ — بِلَا تَاءٍ.", "«three-» — without the tāʾ.", "«üç-» — tâsız."),
  tok("عَشْرَةَ", "ashara", "noun", [K, ADD], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — بِالتَّاءِ، وَشِينُهَا سَاكِنَةٌ.", "«-teen» — with the tāʾ, its shīn still.", "«on» — tâlı, şîni sâkin."),
  tok("امْرَأَةً", "imraa", "noun", [K, TM], "تَمْيِيزٌ مَنْصُوبٌ.", "«women» — the tamyīz.", "«kadın» — temyîz.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "alama": G("alama", "عَلَامَة", "ع ل م", "noun", "a sign, a mark — عَلَامَةُ التَّأْنِيثِ", "alâmet — te'nîs alâmeti", 2, plural="عَلَامَات"),
 "ha-letter": G("ha-letter", "هَاء", "ه و ء", "noun", "the letter hāʾ", "hâ harfi", 2),
 "talha": G("talha", "طَلْحَة", "ط ل ح", "propn", "Ṭalḥa — a man's name ending in the tāʾ: a diptote", "Talha — tâ ile biten erkek adı: gayr-ı munsarif", 2),
 "hubla": G("hubla", "حُبْلَى", "ح ب ل", "noun", "pregnant — on the shortened alif of the feminine", "hâmile — te'nîs elif-i maksûresi ile", 3),
 "dawa-claim": G("dawa-claim", "دَعْوَى", "د ع و", "noun", "a claim, a plea — on the shortened alif", "da'vâ — iddia, elif-i maksûre ile", 3),
 "hamra": G("hamra", "حَمْرَاء", "ح م ر", "noun", "red (feminine of أَحْمَر) — on the lengthened alif", "kırmızı (ahmer'in müennesi) — elif-i memdûde ile", 2),
 "niswa": G("niswa", "نِسْوَة", "ن س و", "noun", "women — a plural of paucity of امْرَأَة", "kadınlar — imrae'nin kıllet cem'i", 3),
 "rakkaba": G("rakkaba", "رَكَّبَ", "ر ك ب", "verb", "to compound, to put together", "terkîb etmek, birleştirmek", 3, form="II"),
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
put_morph(mo, "rakkaba", {"bab": "الْبَابُ الثَّانِي فَعَّلَ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَرْكِيب", "ismFail": "مُرَكِّب",
 "mazi": ["رَكَّبَ", "رَكَّبَا", "رَكَّبُوا", "رَكَّبَتْ", "رَكَّبَتَا", "رَكَّبْنَ", "رَكَّبْتَ", "رَكَّبْتُمَا", "رَكَّبْتُمْ", "رَكَّبْتِ", "رَكَّبْتُمَا", "رَكَّبْتُنَّ", "رَكَّبْتُ", "رَكَّبْنَا"],
 "mudari": ["يُرَكِّبُ", "يُرَكِّبَانِ", "يُرَكِّبُونَ", "تُرَكِّبُ", "تُرَكِّبَانِ", "يُرَكِّبْنَ", "تُرَكِّبُ", "تُرَكِّبَانِ", "تُرَكِّبُونَ", "تُرَكِّبِينَ", "تُرَكِّبَانِ", "تُرَكِّبْنَ", "أُرَكِّبُ", "نُرَكِّبُ"],
 "amr": ["رَكِّبْ", "رَكِّبَا", "رَكِّبُوا", "رَكِّبِي", "رَكِّبَا", "رَكِّبْنَ"], "mansub": "يُرَكِّبَ", "majzum": "يُرَكِّبْ", "majzum2": "تُرَكِّبْ",
 "note": "رَكَّبَ يُرَكِّبُ تَرْكِيبًا: جَعَلَ الشَّيْءَ مِنْ أَجْزَاءٍ — مِنَ الْبَابِ الثَّانِي الْمَزِيدِ؛ مَبْنِيُّهُ لِلْمَفْعُولِ رُكِّبَ (رُكِّبَتْ ثَلَاثَةٌ إِلَى التِّسْعَةِ مَعَ عَشَرَةٍ)."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch26 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("rakkaba", "athbata") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمُؤَنَّثُ وَعَلَامَاتُهُ وَتَاءُ الْعَدَدِ", "en": "The feminine, its signs, and the tāʾ of the numbers", "tr": "Müennes, alâmetleri ve sayının tâsı"},
 "level": 4, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المؤنث وعلاماته", "الكافية لابن الحاجب — المؤنث", "شرح قطر الندى لابن هشام — علامات التأنيث والعدد"],
 "amil": "the feminine carries the sign of the feminine in wording or estimate: the tāʾ paused on as hāʾ (طَلْحَة، شَمْس), the shortened alif (حُبْلَى، دَعْوَى), the lengthened alif (حَمْرَاء); three to ten are reversed — the masculine takes the tāʾ, the feminine drops it (ثَلَاثَةُ رِجَالٍ، أَرْبَعُ نِسْوَةٍ) — and compounded with ten the tāʾ stays on the first only in the masculine (ثَلَاثَةَ عَشَرَ رَجُلًا) and on the second only in the feminine (ثَلَاثَ عَشْرَةَ امْرَأَةً)",
 "question": {
  "en": ["What is the feminine? What carries the sign of the feminine, shown in the wording (طَلْحَة) or estimated (شَمْس — its tāʾ appears in the diminutive شُمَيْسَة).",
         "What are the signs? The tāʾ paused on as hāʾ (طَلْحَة، شَمْس), the shortened alif (حُبْلَى، دَعْوَى) and the lengthened alif (حَمْرَاء).",
         "Why are three to ten different? Their masculine takes the tāʾ and their feminine drops it: ثَلَاثَةُ رِجَالٍ، أَرْبَعُ نِسْوَةٍ — the number agrees with the counted noun in reverse.",
         "And compounded with ten? The tāʾ stays on the first part only in the masculine (ثَلَاثَةَ عَشَرَ رَجُلًا) and on the second part only in the feminine (ثَلَاثَ عَشْرَةَ امْرَأَةً).",
         "Why is شَمْس feminine with no visible sign? Its tāʾ is estimated: it shows in شُمَيْسَة and in طَلَعَتِ الشَّمْسُ.",
         "What does the engine READ here? The DabtEngine reads the cited names and signs as quoted words annexed to نَحْوُ, declines the diptotes طَلْحَةَ and حَمْرَاءَ on the fatḥa, keeps the compound numbers built on the fatḥa, and reads رَجُلًا and امْرَأَةً after them as the tamyīz."],
  "tr": ["Müennes nedir? Te'nîs alâmetini lafzan (Talha) veya takdîren (şems — tâsı tasgîrde şümeyse'de görünür) taşıyandır.",
         "Alâmetler nelerdir? Üzerinde hâ olarak durulan tâ (Talha, şems), elif-i maksûre (hublâ, da'vâ) ve elif-i memdûde (hamrâ).",
         "Üçten ona kadar niçin farklıdır? Müzekkeri tâ alır, müennesi tâyı düşürür: selâsetü ricâlin, erba'u nisvetin — sayı ma'dûda ters uyar.",
         "On ile terkîb edilince? Tâ müzekkerde yalnız ilk cüzde kalır (selâsete aşera racülen), müenneste yalnız ikincisinde (selâse aşrate imraeten).",
         "Şems görünür alâmeti olmadan niçin müennestir? Tâsı takdîrîdir: şümeyse'de ve tala'ati'ş-şemsü'de görünür.",
         "Motor burada neyi OKUR? DabtEngine zikredilen adları ve alâmetleri nahvu'ya muzâf nakledilmiş kelimeler olarak okur, gayr-ı munsarif Talhate ve hamrâe'yi fetha ile çeker, mürekkeb sayıları fetha üzere mebnî tutar ve ardındaki racülen ve imraeten'i temyîz okur."],
 },
 "plain": {"en": "A noun is feminine when it carries a feminine mark: the tāʾ that sounds like h at a pause, or one of two final alifs. The numbers three to ten do the opposite: «three» takes the tāʾ with men and drops it with women. From thirteen to nineteen the tāʾ sits on the first word for men and on the second for women.",
           "tr": "Bir isim, te'nîs işareti taşıyorsa müennestir: vakıfta h gibi okunan tâ ya da iki çeşit son elif. Üçten ona kadar sayılar beklenenin tersini yapar: «üç» erkeklerle tâ alır, kadınlarla düşürür. On üçten on dokuza kadar tâ erkeklerde ilk kelimede, kadınlarda ikincisinde durur."},
 "explanation": {"en": "The feminine is what carries the sign of the feminine, in wording or in estimate; the sign is the tāʾ paused on as hāʾ (طَلْحَة، شَمْس), the shortened alif (حُبْلَى، دَعْوَى) and the lengthened alif (حَمْرَاء). This is in other than three to ten: their masculine takes the tāʾ and their feminine drops it (ثَلَاثَةُ رِجَالٍ، أَرْبَعُ نِسْوَةٍ); and when three to nine are compounded with ten, the tāʾ is kept on the first part only in the masculine (ثَلَاثَةَ عَشَرَ رَجُلًا) and on the second only in the feminine (ثَلَاثَ عَشْرَةَ امْرَأَةً).",
                 "tr": "Müennes, lafzan veya takdîren te'nîs alâmeti taşıyandır; alâmet üzerinde hâ olarak durulan tâ (Talha, şems), elif-i maksûre (hublâ, da'vâ) ve elif-i memdûdedir (hamrâ). Bu, üçten ona kadar olanların dışındadır: onların müzekkeri tâ ile, müennesi tânın hazfiyledir (selâsetü ricâlin, erba'u nisvetin); üçten dokuza kadar olanlar on ile terkîb edilince tâ müzekkerde yalnız ilk cüzde (selâsete aşera racülen), müenneste yalnız ikincisinde kalır (selâse aşrate imraeten)."},
 "examples": [
  {"ar": "الْمُؤَنَّثُ مَا فِيهِ عَلَامَةُ التَّأْنِيثِ لَفْظًا أَوْ تَقْدِيرًا", "en": "the feminine defined", "tr": "müennesin tarifi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "طَلْحَةَ وَشَمْسٍ، حُبْلَى وَدَعْوَى، حَمْرَاءَ", "en": "the three signs", "tr": "üç alâmet", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "ثَلَاثَةُ رِجَالٍ وَأَرْبَعُ نِسْوَةٍ", "en": "three to ten reversed", "tr": "üçten ona tersine", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "ثَلَاثَةَ عَشَرَ رَجُلًا، ثَلَاثَ عَشْرَةَ امْرَأَةً", "en": "the compound numbers", "tr": "mürekkeb sayılar", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "ثَلَاثُ رِجَالٍ", "right": "ثَلَاثَةُ رِجَالٍ", "why": {"en": "with a masculine counted noun the number takes the tāʾ", "tr": "müzekker ma'dûd ile sayı tâ alır"}},
  {"wrong": "ثَلَاثَةَ عَشْرَةَ امْرَأَةً", "right": "ثَلَاثَ عَشْرَةَ امْرَأَةً", "why": {"en": "in the feminine compound the tāʾ sits on the second part only", "tr": "müennes mürekkebde tâ yalnız ikinci cüzde durur"}},
  {"wrong": "طَلَعَ الشَّمْسُ taken as proof that شَمْس is masculine", "right": "شَمْس is feminine by an estimated tāʾ; the masculine verb is merely allowed", "why": {"en": "a formal feminine lets its governor stay masculine", "tr": "lafzî müennes âmilinin müzekker kalmasına izin verir"}},
 ],
}
ADD_EN = (" Chapter 26 (print pp. 126-127): the feminine defined (s1), its three signs (s2), three to ten reversed (s3), the compound numbers (s4).")
ADD_TR = (" Yirmi altıncı bab (baskı s. 126-127): müennesin tarifi (s1), üç alâmeti (s2), üçten ona tersine (s3), mürekkeb sayılar (s4).")
write_out(26, S, TITLE, ADD_EN, ADD_TR, "pp. 126-127", GLOSS_ADD, notes=(NOTE,),
          related=((K25, [K]), (ADD, [K]), (TM, [K]), (DIP, [K]), (MQ, [K])))
report(26, S, GLOSS_ADD, (NOTE,))
