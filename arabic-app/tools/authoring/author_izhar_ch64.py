# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 64: the NON-LĀZIM mabnī — what is cut off from annexation with the muḍāf ilayh intended (قَبْلُ، بَعْدُ، تَحْتُ، فَوْقُ،
# قُدَّامُ، أَمَامُ، خَلْفُ، وَرَاءُ، لَا غَيْرُ، لَيْسَ غَيْرُ، حَسْبُ، الْآنَ); and the single definite munādā, built on the sign of its rafʿ when no alif of
# istighātha or nudba follows and no lām precedes (يَا زَيْدُ، يَا مُسْلِمَانِ، يَا مُسْلِمُونَ) — annexed, resembling the annexed, or indefinite, it is in naṣb by an
# estimated verb (يَا عَبْدَ اللهِ، يَا خَيْرًا مِنْ زَيْدٍ، يَا رَجُلًا); with the alif it is built on fatḥa (يَا زَيْدَاهْ); with the lām it is in jarr (يَا لَزَيْدٍ). Print pp. 158–159.
# The Ottoman commentary (izhar-full-corrected l. 1930 ff.) is followed for the readings; the built adverbs are given on their ḍamma.
#   python3 author_izhar_ch64.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; IRB = "al-murab-wal-mabni-wal-irab"; JDS = "jam-mudhakkar-salim"; ND = "vocative-munada"; LJ = "lam-jazim"; F8 = "form-viii-verbs"; TFD = "ism-tafdil"; F10 = "form-x-verbs"
K = "al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"
K63 = "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf"
TITLE = {"ar": "الْمَبْنِيُّ غَيْرُ اللَّازِمِ: الْمَقْطُوعُ عَنِ الْإِضَافَةِ، وَالْمُنَادَى الْمُفْرَدُ الْمَعْرِفَةُ وَأَحْوَالُهُ", "en": "The non-lāzim mabnī: the word cut off from annexation, and the single definite munādā and its states", "tr": "Gayr-ı lâzım mebnî: izafetten kesilen ve müfred ma'rife münâdâ ile hâlleri"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wnahw(punct=None): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=punct, segments=wa("نَحْوُ", "nahw", "noun"))
def adv(form, lex, en, tr, first=False, punct=None, ar=None):
    a = ar or (("لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ — مَبْنِيٌّ عَلَى الضَّمِّ لِقَطْعِهِ عَنِ الْإِضَافَةِ." if first else "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ — مَبْنِيٌّ عَلَى الضَّمِّ."))
    return tok(form, lex, "noun", [K, MF, IRB] + ([ID] if first else [AT]), a, en, tr, punct=punct, segments=None if first else wa(form[2:], lex, "noun"))
def ya(): return tok("يَا", "ya-nida", "part", [K, ND], "لَفْظٌ مَحْكِيٌّ: حَرْفُ نِدَاءٍ.", "«O»", "«ey»")
def wya(): return tok("وَيَا", "ya-nida", "part", [K, AT, ND], "الْوَاوُ عَاطِفَةٌ، وَيَا حَرْفُ نِدَاءٍ.", "«and O»", "«ve ey»", segments=wa("يَا", "ya-nida", "part"))

# ----------- s1 — the non-lāzim: cut off from annexation
S.append({"id": "s1", "translation": {"en": "And the non-lāzim is what is cut off from annexation with the muḍāf ilayh intended in it — as in qablu, baʿdu, taḥtu, fawqu, quddāmu, amāmu, khalfu, warāʾu, lā ghayru, laysa ghayru, ḥasbu and al-āna;", "tr": "Gayr-ı lâzım, muzâfun ileyhi niyet edilerek izafetten kesilendir — kablü, ba'dü, tahtü, fevku, kuddâmü, emâmü, halfü, verâü, lâ gayru, leyse gayru, hasbü ve el-âne gibi;"},
 "tokens": [
  tok("وَغَيْرُ", "ghayr", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَغَيْرُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ.", "«and the non-»", "«gayr-ı»", segments=wa("غَيْرُ", "ghayr", "noun")),
  tok("اللَّازِمِ", "lazim", "noun", [K, ID, IFA, IRB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«lāzim»", "«lâzım»"),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dır»"),
  tok("قُطِعَ", "qataa", "verb", [K, MAW, NF], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةُ مَا.", "«is cut off»", "«kesilen»"),
  tok("عَنِ", "an", "prep", [K, HJ], "حَرْفُ جَرٍّ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from»", "«-den»"),
  tok("الْإِضَافَةِ", "idafa", "noun", [K, HJ, MSD, F4, ID], "مَجْرُورٌ بِعَنْ.", "«annexation»", "«izafetten»"),
  tok("مَنْوِيًّا", "manwi", "noun", [K, "hal", NSB], "حَالٌ مِنْ نَائِبِ الْفَاعِلِ مَنْصُوبٌ — سَبَبِيٌّ، رَافِعٌ لِمَا بَعْدَهُ.", "«intended» — a causal ḥāl.", "«niyet edilmiş» — sebebî hâl."),
  tok("فِيهِ", "fi", "prep", [K, HJ], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«in it»", "«onda»", segments=[seg("فِي", "fi", "prep"), pr3msi()]),
  tok("الْمُضَافُ", "mudaf", "noun", [K, FL, IMF, F4, ID], "فَاعِلُ مَنْوِيًّا مَرْفُوعٌ.", "«the muḍāf»", "«muzâf»"),
  tok("إِلَيْهِ", "ila", "prep", [K, HJ, ID], "إِلَى حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْمُضَافُ إِلَيْهِ.", "«ilayh» — the muḍāf ilayh.", "«ileyh» — muzâfun ileyh.", punct="،", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  nahw(),
  adv("قَبْلُ", "qabl", "«qablu» — before", "«kablü» — önce", first=True),
  adv("وَبَعْدُ", "bada", "«baʿdu» — after", "«ba'dü» — sonra"),
  adv("وَتَحْتُ", "tahta", "«taḥtu» — below", "«tahtü» — altta"),
  adv("وَفَوْقُ", "fawqa", "«fawqu» — above", "«fevku» — üstte"),
  adv("وَقُدَّامُ", "quddam", "«quddāmu» — in front", "«kuddâmü» — önde"),
  adv("وَأَمَامُ", "amama", "«amāmu» — ahead", "«emâmü» — ileride"),
  adv("وَخَلْفُ", "khalf", "«khalfu» — behind", "«halfü» — arkada"),
  adv("وَوَرَاءُ", "wara", "«warāʾu» — behind", "«verâü» — gerisinde"),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and lā»", "«ve lâ»", segments=wa("لَا", "la", "part")),
  tok("غَيْرُ", "ghayr", "noun", [K, MF, IRB], "مَبْنِيٌّ عَلَى الضَّمِّ — لَا غَيْرُ: لَا غَيْرَ ذٰلِكَ.", "«ghayru» — «nothing else».", "«gayru» — «başkası değil»."),
  tok("وَلَيْسَ", "laysa", "verb", [K, AT, KN], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ.", "«and laysa»", "«ve leyse»", segments=wa("لَيْسَ", "laysa", "verb")),
  tok("غَيْرُ", "ghayr", "noun", [K, KN, IRB], "خَبَرُ لَيْسَ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَاسْمُهَا مُسْتَتِرٌ.", "«ghayru» — laysa's khabar, built.", "«gayru» — leyse'nin haberi, mebnî."),
  adv("وَحَسْبُ", "hasb", "«ḥasbu» — enough", "«hasbü» — yeter"),
  adv("وَالْآنَ", "al-an", "«al-āna» — now, built on fatḥa", "«el-âne» — şimdi, fetha üzere mebnî", punct="،", ar="الْوَاوُ عَاطِفَةٌ، وَالْآنَ مَعْطُوفٌ — مَبْنِيٌّ عَلَى الْفَتْحِ."),
 ]})
# ----------- s2 — the single definite munādā
S.append({"id": "s2", "translation": {"en": "and the single definite munādā, for it is built on what it would be raised by, if no alif of istighātha or of nudba attaches to its end, and no lām to its beginning — as in «O Zayd», «O two Muslims», «O Muslims»;", "tr": "ve müfred ma'rife münâdâ; çünkü sonuna istigâse ya da nüdbe elifi, başına lâm bitişmezse, kendisiyle ref' edildiği şey üzere mebnîdir — «ey Zeyd», «ey iki müslüman», «ey müslümanlar» gibi;"},
 "tokens": [
  tok("وَالْمُنَادَى", "munada", "noun", [K, AT, IMF, ND, MQ], "الْوَاوُ عَاطِفَةٌ، وَالْمُنَادَى مَعْطُوفٌ عَلَى مَا قُطِعَ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the munādā»", "«ve münâdâ»", segments=wa("الْمُنَادَى", "munada", "noun")),
  tok("الْمُفْرَدُ", "mufrad", "noun", [K, NA, IMF, F4, ND], "نَعْتٌ مَرْفُوعٌ — غَيْرُ الْمُضَافِ وَلَا شَبِيهِهِ.", "«single» — not annexed nor like the annexed.", "«müfred» — muzâf ve benzeri değil."),
  tok("الْمَعْرِفَةُ", "marifa", "noun", [K, NA, ND], "نَعْتٌ ثَانٍ مَرْفُوعٌ — عَلَمًا أَوْ نَكِرَةً مَقْصُودَةً.", "«definite» — a name, or an indefinite made definite by the address.", "«ma'rife» — alem ya da nidâ ile belirlenmiş nekre."),
  tok("فَإِنَّهُ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا.", "«for it»", "«çünkü o»", segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part"), pr3ms()]),
  tok("مَبْنِيٌّ", "mabni", "noun", [K, IN, IMF, IRB], "خَبَرُ إِنَّ مَرْفُوعٌ.", "«is built»", "«mebnîdir»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"),
  tok("مَا", "ma-mawsula", "pron", [K, HJ, MAW], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«what»", "«şey»"),
  tok("يُرْفَعُ", "rafaa", "verb", [K, MAW, MR, NF], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — صِلَةُ مَا.", "«it would be raised»", "«ref' edildiği»"),
  tok("بِهِ", "bi", "prep", [K, HJ, MAW], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ: الضَّمَّةُ أَوِ الْأَلِفُ أَوِ الْوَاوُ.", "«by» — the ḍamma, alif or wāw.", "«-le» — damme, elif ya da vâv."),
  tok("إِنْ", "in-shartiyya", "part", [K, INS, JZ], "حَرْفُ شَرْطٍ جَازِمٌ، وَالْجَوَابُ مَحْذُوفٌ لِدَلَالَةِ مَا قَبْلَهُ.", "«if»", "«eğer»"),
  tok("لَمْ", "lam", "part", [K, LJ, JZ], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not»", "«-mezse»"),
  tok("يَلْحَقْ", "lahiqa", "verb", [K, INS, LJ, JZ], "فِعْلُ الشَّرْطِ، مُضَارِعٌ مَجْزُومٌ.", "«attaches»", "«bitişmezse»"),
  tok("بِآخِرِهِ", "akhir", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَآخِرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its end»", "«sonuna»", segments=[seg("بِ", "bi", "prep"), seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("أَلِفُ", "alif-letter", "noun", [K, FL, ID, ND], "فَاعِلُ يَلْحَقْ مَرْفُوعٌ، مُضَافٌ.", "«the alif of»", "«elifi»"),
  tok("الِاسْتِغَاثَةِ", "istighatha", "noun", [K, ID, MSD, F10, ND], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — يَا زَيْدَا لِعَمْرٍو.", "«istighātha» — the call for help: yā zaydā li-ʿamrin.", "«istigâse» — yardıma çağırma: yâ zeydâ li-amrin."),
  tok("أَوِ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«or»", "«ya da»"),
  tok("النُّدْبَةِ", "nudba", "noun", [K, AT, MSD, ND], "مَعْطُوفٌ عَلَى الِاسْتِغَاثَةِ مَجْرُورٌ — وَا زَيْدَاهْ.", "«nudba» — the lament: wā zaydāh.", "«nüdbe» — ağıt: vâ zeydâh."),
  tok("وَلَا", "la", "part", [K, AT, LN], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "«nor»", "«ne de»", segments=wa("لَا", "la", "part")),
  tok("بِأَوَّلِهِ", "awwal", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَأَوَّلِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its beginning»", "«başına»", segments=[seg("بِ", "bi", "prep"), seg("أَوَّلِ", "awwal", "noun"), pr3msi()]),
  tok("لَامٌ", "lam-letter", "noun", [K, AT, FL, ND], "مَعْطُوفٌ عَلَى أَلِفُ مَرْفُوعٌ — لَامُ الِاسْتِغَاثَةِ.", "«a lām» — the lām of istighātha.", "«bir lâm» — istigâse lâmı.", punct="،"),
  nahw(punct=":"),
  ya(),
  tok("زَيْدُ", "zayd", "propn", [K, ND, IRB], "مُنَادًى مُفْرَدٌ مَعْرِفَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "«Zayd» — built on ḍamma, naṣb by position.", "«Zeyd» — damme üzere mebnî, mahallen mansûb.", punct="،"),
  wya(),
  tok("مُسْلِمَانِ", "muslim", "noun", [K, ND, MTH, IRB], "مُنَادًى مَبْنِيٌّ عَلَى الْأَلِفِ فِي مَحَلِّ نَصْبٍ — نَكِرَةٌ مَقْصُودَةٌ.", "«two Muslims» — built on the alif.", "«iki müslüman» — elif üzere mebnî.", punct="،"),
  wya(),
  tok("مُسْلِمُونَ", "muslim", "noun", [K, ND, JDS, IRB], "مُنَادًى مَبْنِيٌّ عَلَى الْوَاوِ فِي مَحَلِّ نَصْبٍ.", "«Muslims» — built on the wāw.", "«müslümanlar» — vâv üzere mebnî.", punct="،"),
 ]})
# ----------- s3 — the annexed, the resembling, the indefinite
S.append({"id": "s3", "translation": {"en": "and if it is annexed, or resembling the annexed, or indefinite, it is put in naṣb by an estimated verb — as in «O servant of God», «O one better than Zayd», «O man»;", "tr": "muzâf, muzâfa benzer ya da nekre ise takdir edilen bir fiille nasbedilir — «ey Allah'ın kulu», «ey Zeyd'den hayırlı», «ey adam» gibi;"},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — الْمُنَادَى.", "«it is»", "«ise»"),
  tok("مُضَافًا", "mudaf", "noun", [K, KN, IMF, F4, ID], "خَبَرُ كَانَ مَنْصُوبٌ.", "«annexed»", "«muzâf»"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("مُشَابِهًا", "mushabih", "noun", [K, AT, KN, IFA], "مَعْطُوفٌ مَنْصُوبٌ.", "«resembling»", "«benzer»"),
  tok("بِهِ", "bi", "prep", [K, HJ], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — بِالْمُضَافِ: مَا اتَّصَلَ بِهِ شَيْءٌ مِنْ تَمَامِ مَعْنَاهُ.", "«it» — the annexed: what has something attached completing its sense.", "«ona» — muzâfa: manasını tamamlayan bir şey bitişmiş olan.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("نَكِرَةً", "nakira", "noun", [K, AT, KN, ND], "مَعْطُوفٌ مَنْصُوبٌ — غَيْرَ مَقْصُودَةٍ.", "«indefinite» — not a particular one.", "«nekre» — belirli olmayan."),
  tok("يُنْصَبُ", "nasaba-nahw", "verb", [K, INS, MR, NF], "جَوَابُ الشَّرْطِ: فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«it is put in naṣb»", "«nasbedilir»"),
  tok("بِفِعْلٍ", "fil", "noun", [K, HJ, ND, HT], "الْبَاءُ حَرْفُ جَرٍّ، وَفِعْلٍ مَجْرُورٌ.", "«by a verb»", "«bir fiille»", segments=[seg("بِ", "bi", "prep"), seg("فِعْلٍ", "fil", "noun")]),
  tok("مُقَدَّرٍ", "muqaddar", "noun", [K, NA, IMF, F2, HT], "نَعْتٌ مَجْرُورٌ — أَدْعُو أَوْ أُنَادِي.", "«estimated» — adʿū or unādī.", "«takdir edilen» — ed'û ya da ünâdî.", punct="،"),
  nahw(punct=":"),
  ya(),
  tok("عَبْدَ", "abd", "noun", [K, ND, MB, ID], "مُنَادًى مُضَافٌ مَنْصُوبٌ، مُضَافٌ.", "«servant of» — the annexed munādā in naṣb.", "«kulu» — muzâf münâdâ, mansûb."),
  tok("اللهِ", "allah", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«God»", "«Allah'ın»", punct="،"),
  wya(),
  tok("خَيْرًا", "khayr", "noun", [K, ND, MB, TFD], "مُنَادًى شَبِيهٌ بِالْمُضَافِ مَنْصُوبٌ — تَعَلَّقَ بِهِ مَا بَعْدَهُ.", "«one better» — resembling the annexed.", "«daha hayırlı» — muzâfa benzer."),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«than»", "«-den»"),
  tok("زَيْدٍ", "zayd", "propn", [K, HJ], "مَجْرُورٌ بِمِنْ — مُتَعَلِّقٌ بِخَيْرًا.", "«Zayd»", "«Zeyd»", punct="،"),
  wya(),
  tok("رَجُلًا", "rajul", "noun", [K, ND, MB], "مُنَادًى نَكِرَةٌ غَيْرُ مَقْصُودَةٍ مَنْصُوبٌ.", "«a man» — the unspecified indefinite.", "«bir adam» — belirsiz nekre.", punct="،"),
 ]})
# ----------- s4 — the alif and the lām
S.append({"id": "s4", "translation": {"en": "and if an alif attaches to its end, it is built on fatḥa — as in «O Zaydāh»; and if a lām is joined to its beginning, it is put in jarr — as in «O, for Zayd!».", "tr": "sonuna elif bitişirse fetha üzere mebnî olur — «ey Zeydâh» gibi; başına lâm bitişirse mecrûr olur — «yâ le-Zeyd» gibi."},
 "tokens": [
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("لَحِقَ", "lahiqa", "verb", [K, INS], "فِعْلُ الشَّرْطِ، مَاضٍ فِي مَحَلِّ جَزْمٍ.", "«attaches»", "«bitişirse»"),
  tok("بِآخِرِهِ", "akhir", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَآخِرِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its end»", "«sonuna»", segments=[seg("بِ", "bi", "prep"), seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("أَلِفٌ", "alif-letter", "noun", [K, FL, ND], "فَاعِلٌ مَرْفُوعٌ — أَلِفُ الِاسْتِغَاثَةِ أَوِ النُّدْبَةِ.", "«an alif»", "«bir elif»"),
  tok("يُبْنَى", "bana", "verb", [K, INS, MR, NF, MQ, IRB], "جَوَابُ الشَّرْطِ: مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«it is built»", "«mebnî olur»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«üzere»"),
  tok("الْفَتْحِ", "fath", "noun", [K, HJ, MSD, IRB], "مَجْرُورٌ بِعَلَى.", "«fatḥa»", "«fetha»", punct="،"),
  nahw(punct=":"),
  ya(),
  tok("زَيْدَاهْ", "zayd", "propn", [K, ND, IRB], "مُنَادًى مَنْدُوبٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْأَلِفُ لِلنُّدْبَةِ، وَالْهَاءُ لِلسَّكْتِ.", "«Zaydāh» — on fatḥa; the alif of nudba, the hāʾ of pause.", "«Zeydâh» — fetha üzere; nüdbe elifi, sekte hâsı.", punct="،"),
  tok("وَإِنِ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and if»", "«ve eğer»", segments=wa("إِنِ", "in-shartiyya", "part")),
  tok("اتَّصَلَ", "ittasala", "verb", [K, INS, F8], "فِعْلُ الشَّرْطِ، مَاضٍ فِي مَحَلِّ جَزْمٍ.", "«is joined»", "«bitişirse»"),
  tok("بِأَوَّلِهِ", "awwal", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَأَوَّلِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«to its beginning»", "«başına»", segments=[seg("بِ", "bi", "prep"), seg("أَوَّلِ", "awwal", "noun"), pr3msi()]),
  tok("لَامٌ", "lam-letter", "noun", [K, FL, ND], "فَاعِلٌ مَرْفُوعٌ — لَامُ الِاسْتِغَاثَةِ، مَفْتُوحَةٌ.", "«a lām» — the lām of istighātha, on fatḥa.", "«bir lâm» — istigâse lâmı, fethalı."),
  tok("يُجَرُّ", "jarra", "verb", [K, INS, MR, NF, "doubled-verbs", IRB], "جَوَابُ الشَّرْطِ: مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«it is put in jarr»", "«mecrûr olur»", punct="،"),
  nahw(punct=":"),
  ya(),
  tok("لَزَيْدٍ", "zayd", "propn", [K, ND, HJ, IRB], "اللَّامُ لَامُ الِاسْتِغَاثَةِ جَارَّةٌ، وَزَيْدٍ مَجْرُورٌ — الْمُسْتَغَاثُ بِهِ.", "«for Zayd» — the one called to help, in jarr.", "«Zeyd'e» — yardıma çağrılan, mecrûr.", punct=".", segments=[seg("لَ", "li", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "munada": G("munada", "مُنَادًى", "ن د و", "noun", "the munādā, the one called (passive participle of nādā)", "münâdâ, çağrılan (nâdâ'nın ism-i mef'ûlü)", 3),
 "istighatha": G("istighatha", "اِسْتِغَاثَة", "غ و ث", "noun", "istighātha — the call for help (yā la-zaydin); form X maṣdar", "istigâse — yardıma çağırma (yâ le-zeydin); X. bab mastarı", 4),
 "nudba": G("nudba", "نُدْبَة", "ن د ب", "noun", "nudba — the lament over one lost (wā zaydāh)", "nüdbe — yitirilene ağıt (vâ zeydâh)", 4),
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
print("izhar ch64 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("qataa", "rafaa", "lahiqa", "kana", "nasaba-nahw", "bana", "ittasala", "jarra", "laysa") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "الْمَبْنِيُّ غَيْرُ اللَّازِمِ: الْغَايَاتُ الْمَقْطُوعَةُ عَنِ الْإِضَافَةِ، وَالْمُنَادَى الْمُفْرَدُ الْمَعْرِفَةُ عَلَى عَلَامَةِ رَفْعِهِ، وَنَصْبُ الْمُضَافِ وَشَبِيهِهِ وَالنَّكِرَةِ، وَأَلِفُ النُّدْبَةِ وَلَامُ الِاسْتِغَاثَةِ", "en": "The non-lāzim mabnī: the limit-words cut off from annexation; the single definite munādā on its rafʿ sign; the naṣb of the annexed, the resembling and the indefinite; the alif of nudba and the lām of istighātha", "tr": "Gayr-ı lâzım mebnî: izafetten kesilen gâyeler; ref' alâmeti üzere müfred ma'rife münâdâ; muzâf, benzeri ve nekrenin nasbı; nüdbe elifi ve istigâse lâmı"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — المبني غير اللازم", "الكافية لابن الحاجب — الغايات، المنادى", "شرح قطر الندى لابن هشام — المنادى"],
 "amil": "the non-lāzim mabnī: what is cut off from annexation with the muḍāf ilayh intended — قَبْلُ، بَعْدُ، تَحْتُ، فَوْقُ، قُدَّامُ، أَمَامُ، خَلْفُ، وَرَاءُ، لَا غَيْرُ، لَيْسَ غَيْرُ، حَسْبُ، الْآنَ; and the single definite munādā, built on the sign of its rafʿ (يَا زَيْدُ، يَا مُسْلِمَانِ، يَا مُسْلِمُونَ) when no alif of istighātha or nudba follows and no lām precedes; the annexed, the resembling and the indefinite take naṣb by an estimated verb (يَا عَبْدَ اللهِ، يَا خَيْرًا مِنْ زَيْدٍ، يَا رَجُلًا); with the alif it is built on fatḥa (يَا زَيْدَاهْ), with the lām in jarr (يَا لَزَيْدٍ).",
 "question": {
  "en": ["What is the non-lāzim mabnī? A word built only in a certain setting and declined elsewhere — the limit-words when cut off from annexation, and the munādā under its conditions.",
         "Why are قَبْلُ and بَعْدُ built on ḍamma? Because they are cut off from annexation while the muḍāf ilayh is still intended (جِئْتُ مِنْ قَبْلُ = مِنْ قَبْلِ ذٰلِكَ); with a muḍāf ilayh they decline (مِنْ قَبْلِ الْفَجْرِ).",
         "Which words share this ruling? تَحْتُ، فَوْقُ، قُدَّامُ، أَمَامُ، خَلْفُ، وَرَاءُ, the ghayru of لَا غَيْرُ and لَيْسَ غَيْرُ, حَسْبُ, and الْآنَ, built on fatḥa.",
         "When is the munādā built? When it is single (not annexed nor resembling the annexed) and definite — a name or an indefinite the call makes definite — with no alif of istighātha or nudba at its end and no lām at its start: it is built on what would be its rafʿ sign (يَا زَيْدُ، يَا مُسْلِمَانِ، يَا مُسْلِمُونَ), in the position of naṣb.",
         "When does the munādā take naṣb? When annexed (يَا عَبْدَ اللهِ), resembling the annexed (يَا خَيْرًا مِنْ زَيْدٍ) or an unspecified indefinite (يَا رَجُلًا) — by the estimated verb adʿū.",
         "What do the alif and the lām do? The alif of nudba or istighātha builds the munādā on fatḥa (يَا زَيْدَاهْ, with the hāʾ of pause); the lām of istighātha, on fatḥa, puts it in jarr (يَا لَزَيْدٍ).",
         "What does the engine READ here? The DabtEngine reads the cited limit-words on their ḍamma as built forms after نَحْوُ, the munādā يَا زَيْدُ on its ḍamma and يَا مُسْلِمَانِ / يَا مُسْلِمُونَ on alif and wāw, يَا عَبْدَ اللهِ and يَا رَجُلًا in naṣb, يَا زَيْدَاهْ on fatḥa and يَا لَزَيْدٍ in jarr by the lām."],
  "tr": ["Gayr-ı lâzım mebnî nedir? Yalnız belirli bir durumda mebnî olup başka yerde mu'reb olan kelime — izafetten kesilince gâyeler ve şartlarıyla münâdâ.",
         "Kablü ve ba'dü neden damme üzere mebnîdir? Muzâfun ileyh niyet edilirken izafetten kesildikleri için (ci'tü min kablü = min kabli zâlike); muzâfun ileyh ile mu'rebdirler (min kabli'l-fecri).",
         "Hangi kelimeler bu hükmü paylaşır? Tahtü, fevku, kuddâmü, emâmü, halfü, verâü, lâ gayru ve leyse gayru'nun gayru'su, hasbü ve fetha üzere el-âne.",
         "Münâdâ ne zaman mebnîdir? Müfred (muzâf ve benzeri değil) ve ma'rife olunca — alem ya da nidâ ile belirlenmiş nekre — sonunda istigâse ya da nüdbe elifi, başında lâm yokken: ref' alâmeti olacak şey üzere mebnîdir (yâ Zeydü, yâ müslimâni, yâ müslimûne), nasb mahallinde.",
         "Münâdâ ne zaman nasb alır? Muzâf (yâ abdellâh), muzâfa benzer (yâ hayran min Zeydin) ya da belirsiz nekre (yâ racülen) olunca — takdîrî ed'û fiiliyle.",
         "Elif ve lâm ne yapar? Nüdbe ya da istigâse elifi münâdâyı fetha üzere mebnî kılar (yâ Zeydâh, sekte hâsıyla); fethalı istigâse lâmı onu mecrûr kılar (yâ le-Zeydin).",
         "Motor burada neyi OKUR? DabtEngine alıntı gâyeleri dammeleriyle nahvü'den sonra mebnî şekiller, yâ Zeydü'yü dammesiyle ve yâ müslimâni / yâ müslimûne'yi elif ve vâvla, yâ abdellâh ve yâ racülen'i mansûb, yâ Zeydâh'ı fetha üzere ve yâ le-Zeydin'i lâm ile mecrûr okur."],
 },
 "plain": {"en": "Some words freeze only in certain uses. «Before» and «after» take a fixed -u when their complement is unsaid (min qablu); so do taḥtu and fawqu. A called name freezes on its rafʿ ending: yā Zaydu, yā Muslimūna. But «O servant of God» takes -a; yā Zaydāh (a lament) ends in -ā, yā la-Zaydin (a cry for help) in -in.",
           "tr": "Bazı sözcükler yalnız belirli kullanımlarda donar. «Önce» ve «sonra», tamlayanı söylenmeyince sabit -u alır (min kablü); tahtü ve fevku da öyle. Seslenilen ad ref' sonu üzerinde donar: yâ Zeydü, yâ müslimûne. Ama «ey Allah'ın kulu» -a alır; yâ Zeydâh (ağıt) -â ile, yâ le-Zeydin (yardım çağrısı) -in ile biter."},

 "explanation": {"en": "The non-lāzim mabnī is what is cut off from annexation with the muḍāf ilayh intended in it: قَبْلُ، بَعْدُ، تَحْتُ، فَوْقُ، قُدَّامُ، أَمَامُ، خَلْفُ، وَرَاءُ، لَا غَيْرُ، لَيْسَ غَيْرُ، حَسْبُ، and الْآنَ. And the single definite munādā: it is built on what it would be raised by, if no alif of istighātha or nudba attaches to its end and no lām to its beginning — يَا زَيْدُ، يَا مُسْلِمَانِ، يَا مُسْلِمُونَ. If it is annexed, resembling the annexed, or indefinite, it is put in naṣb by an estimated verb — يَا عَبْدَ اللهِ، يَا خَيْرًا مِنْ زَيْدٍ، يَا رَجُلًا. If an alif attaches to its end, it is built on fatḥa — يَا زَيْدَاهْ; if a lām is joined to its beginning, it is put in jarr — يَا لَزَيْدٍ. The badal and the joined word of the munādā, the particles of calling, the ism of lā, and the muḍāriʿ with the nūn follow.",
                 "tr": "Gayr-ı lâzım mebnî, muzâfun ileyhi niyet edilerek izafetten kesilendir: kablü, ba'dü, tahtü, fevku, kuddâmü, emâmü, halfü, verâü, lâ gayru, leyse gayru, hasbü ve el-âne. Ve müfred ma'rife münâdâ: sonuna istigâse ya da nüdbe elifi, başına lâm bitişmezse, kendisiyle ref' edildiği şey üzere mebnîdir — yâ Zeydü, yâ müslimâni, yâ müslimûne. Muzâf, muzâfa benzer ya da nekre ise takdir edilen bir fiille nasbedilir — yâ abdellâh, yâ hayran min Zeydin, yâ racülen. Sonuna elif bitişirse fetha üzere mebnî olur — yâ Zeydâh; başına lâm bitişirse mecrûr olur — yâ le-Zeydin. Münâdânın bedeli ve ma'tûfu, nidâ harfleri, lâ'nın ismi ve nûnlu muzâri gelir."},
 "examples": [
  {"ar": "نَحْوُ قَبْلُ وَبَعْدُ وَتَحْتُ وَفَوْقُ … وَحَسْبُ وَالْآنَ", "en": "the limit-words cut off from annexation", "tr": "izafetten kesilen gâyeler", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "يَا زَيْدُ، وَيَا مُسْلِمَانِ، وَيَا مُسْلِمُونَ", "en": "the single definite munādā on its rafʿ sign", "tr": "ref' alâmeti üzere müfred ma'rife münâdâ", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "يَا عَبْدَ اللهِ، وَيَا خَيْرًا مِنْ زَيْدٍ، وَيَا رَجُلًا", "en": "the munādā in naṣb", "tr": "mansûb münâdâ", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "يَا زَيْدَاهْ — يَا لَزَيْدٍ", "en": "the alif of nudba and the lām of istighātha", "tr": "nüdbe elifi ve istigâse lâmı", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "جِئْتُ مِنْ قَبْلِ (with nothing after)", "right": "جِئْتُ مِنْ قَبْلُ", "why": {"en": "cut off from annexation with its complement intended, qabl is built on ḍamma", "tr": "tamlayanı niyet edilerek izafetten kesilince kabl damme üzere mebnîdir"}},
  {"wrong": "يَا زَيْدًا", "right": "يَا زَيْدُ", "why": {"en": "the single definite munādā is built on its rafʿ sign", "tr": "müfred ma'rife münâdâ ref' alâmeti üzere mebnîdir"}},
  {"wrong": "يَا عَبْدُ اللهِ", "right": "يَا عَبْدَ اللهِ", "why": {"en": "the annexed munādā takes naṣb by the estimated verb", "tr": "muzâf münâdâ takdîrî fiille nasb alır"}},
  {"wrong": "يَا لَزَيْدُ", "right": "يَا لَزَيْدٍ", "why": {"en": "the lām of istighātha puts the munādā in jarr", "tr": "istigâse lâmı münâdâyı mecrûr kılar"}},
 ],
}
ADD_EN = (" Chapter 64 (print pp. 158-159): the non-lāzim mabnī — the limit-words cut off from annexation (s1); the single definite munādā built on its rafʿ sign (s2); the annexed, the resembling and the indefinite munādā in naṣb (s3); the alif of nudba and the lām of istighātha (s4).")
ADD_TR = (" Altmış dördüncü bab (baskı s. 158-159): gayr-ı lâzım mebnî — izafetten kesilen gâyeler (s1); ref' alâmeti üzere mebnî müfred ma'rife münâdâ (s2); mansûb muzâf, benzer ve nekre münâdâ (s3); nüdbe elifi ve istigâse lâmı (s4).")
write_out(64, S, TITLE, ADD_EN, ADD_TR, "pp. 158-159", GLOSS_ADD, notes=(NOTE,),
          related=((K63, [K]), (IRB, [K]), (ND, [K]), (MF, [K]), (ID, [K])))
report(64, S, GLOSS_ADD, (NOTE,))
