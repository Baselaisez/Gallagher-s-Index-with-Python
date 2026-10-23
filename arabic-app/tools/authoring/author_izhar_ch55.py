# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 55: the QIYĀSĪ ghayr munṣarif, first half — every proper name on a pattern particular to the verb (ضُرِبَ، شَمَّرَ،
# انْقَطَعَ، اجْتَمَعَ، اسْتَخْرَجَ) or beginning with one of the muḍāriʿ augments while a noun, not a verb (يَزِيدَ، يَشْكُرَ); every afʿal of preference and of
# description (أَفْعَلَ، أَبْيَضَ); every foreign noun used as a proper name at its first transfer to the Arabs, exceeding three letters or with a vowelled
# middle (قَالُونَ، إِبْرَاهِيمَ، شَتَرَ); every feminine by the alif, shortened or lengthened (حُبْلَى، حَمْرَاءَ). Print pp. 150–151.
# Readings: the lithograph leaves ضرب unvowelled; the Ottoman commentary (izhar-full-corrected l. 1728) reads ضُرِبَ, which the text follows. The commentary
# (l. 1725-1726) glosses «غير فعل بل اسم» as the name's not accepting the tāʾ; the text reads the clause as a nominal aside (هُوَ) غَيْرُ فِعْلٍ بَلِ اسْمٌ.
# The commentary (l. 1739-1743) explains قَالُونَ as a Greek common noun («good») made a name of Nāfiʿ's transmitter, and شَتَرُ as a fortress near
# Diyarbakır — given in the explanation as the commentary's note.
#   python3 author_izhar_ch55.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; F7 = "form-vii-verbs"; F10 = "form-x-verbs"; ALM = "al-marifa-al-mudmarat-wal-alam"; TFD = "ism-tafdil"; SM = "sifa-mushabbaha"; MN = "al-muannath-wa-alamatuh"
K = "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"
K54 = "al-murab-bil-hadhf-wal-munsarif-wa-ghayruh-al-samai"
TITLE = {"ar": "غَيْرُ الْمُنْصَرِفِ الْقِيَاسِيُّ: الْعَلَمُ عَلَى وَزْنِ الْفِعْلِ، وَأَفْعَلُ، وَالْأَعْجَمِيُّ، وَالْمُؤَنَّثُ بِالْأَلِفِ", "en": "The qiyāsī ghayr munṣarif: the name on a verb pattern, afʿal, the foreign name, the feminine by alif", "tr": "Kıyâsî gayr-ı munsarif: fiil vezninde alem, ef'al, a'cemî, elif ile müennes"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def cit(form, lex, pos, en, tr, first=True, punct=None, extra=(), ar=None):
    a = ar or ("لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — غَيْرُ مُنْصَرِفٍ." if first else "الْوَاوُ عَاطِفَةٌ، وَ" + form[2:] + " مَعْطُوفٌ — لَفْظٌ مَحْكِيٌّ، غَيْرُ مُنْصَرِفٍ.")
    return tok(form, lex, pos, [K, MMS] + ([AT] if not first else [ID]) + list(extra), a, en, tr, punct=punct, segments=None if first else wa(form[2:], lex, pos))
def wakullu(): return tok("وَكُلُّ", "kull", "noun", [K, AT, MK, ID], "الْوَاوُ عَاطِفَةٌ، وَكُلُّ مَعْطُوفٌ عَلَى كُلُّ عَلَمٍ مَرْفُوعٌ، مُضَافٌ.", "«and every»", "«ve her»", segments=wa("كُلُّ", "kull", "noun"))

# ----------- s1 — the qiyāsī: every name on a verb pattern or with a muḍāriʿ augment
S.append({"id": "s1", "translation": {"en": "and qiyāsī — and it is every proper name on a pattern particular to the verb, like ḍuriba, shammara, inqaṭaʿa, ijtamaʿa and istakhraja, or at whose beginning is one of the muḍāriʿ's augments, it being not a verb but a noun — as in Yazīd and Yashkur;", "tr": "ve kıyâsî — o, fiile mahsus bir vezin üzere olan her alemdir, duribe, şemmera, inkataa, ictemea ve istahrece gibi; ya da başında muzârinin zâidlerinden biri bulunan — fiil değil isim olarak — Yezîd ve Yeşkür gibi;"},
 "tokens": [
  tok("وَقِيَاسِيٌّ", "qiyasi", "noun", [K, AT, MK, NSB, MMS], "الْوَاوُ عَاطِفَةٌ، وَقِيَاسِيٌّ مَعْطُوفٌ عَلَى سَمَاعِيٌّ مَرْفُوعٌ — مَا لَهُ قَاعِدَةٌ يُقَاسُ عَلَيْهَا.", "«and qiyāsī» — what has a rule to go by.", "«ve kıyâsî» — kıyas edilecek kuralı olan.", punct="،", segments=wa("قِيَاسِيٌّ", "qiyasi", "noun")),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK], "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«and it is»", "«ve o»", segments=wa("هُوَ", "huwa", "pron")),
  tok("كُلُّ", "kull", "noun", [K, MK, ID], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«every»", "«her»"),
  tok("عَلَمٍ", "alam-name", "noun", [K, ID, ALM, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْعَلَمِيَّةُ أَحَدُ السَّبَبَيْنِ.", "«proper name» — name-hood is one of the two causes.", "«alem» — alemiyet iki sebepten biri."),
  tok("عَلَى", "ala", "prep", [K, HJ, NA], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ نَعْتٌ لِعَلَمٍ.", "«on» — the phrase describes «name».", "«üzere» — öbek alem'in sıfatı."),
  tok("وَزْنٍ", "wazn", "noun", [K, HJ, MMS], "مَجْرُورٌ بِعَلَى.", "«a pattern»", "«bir vezin»"),
  tok("مَخْصُوصٍ", "makhsus", "noun", [K, NA, IMF], "نَعْتٌ مَجْرُورٌ.", "«particular»", "«mahsus»"),
  tok("بِالْفِعْلِ", "fil", "noun", [K, HJ, MMS], "الْبَاءُ حَرْفُ جَرٍّ، وَالْفِعْلِ مَجْرُورٌ — وَزْنُ الْفِعْلِ السَّبَبُ الثَّانِي.", "«to the verb» — the verb-pattern is the second cause.", "«fiile» — fiil vezni ikinci sebep.", segments=[seg("بِ", "bi", "prep"), seg("الْفِعْلِ", "fil", "noun")]),
  tok("كَضُرِبَ", "daraba", "verb", [K, HJ, NF, MMS], "الْكَافُ حَرْفُ جَرٍّ، وَضُرِبَ لَفْظٌ مَحْكِيٌّ فِي مَحَلِّ جَرٍّ — مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ عَلَى قِرَاءَةِ الشَّرْحِ.", "«like ḍuriba» — the commentary's reading of the unvowelled print.", "«duribe gibi» — harekesiz baskının şerhteki okunuşu.", segments=[seg("كَ", "ka", "prep"), seg("ضُرِبَ", "daraba", "verb")]),
  cit("وَشَمَّرَ", "shammara", "verb", "«and shammara»", "«ve şemmera»", first=False, extra=(F2,)),
  cit("وَانْقَطَعَ", "inqataa", "verb", "«and inqaṭaʿa»", "«ve inkataa»", first=False, extra=(F7,)),
  cit("وَاجْتَمَعَ", "ijtamaa", "verb", "«and ijtamaʿa»", "«ve ictemea»", first=False, extra=(F8,)),
  cit("وَاسْتَخْرَجَ", "istakhraja", "verb", "«and istakhraja»", "«ve istahrece»", first=False, punct="،", extra=(F10,)),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("فِي", "fi", "prep", [K, HJ, NA, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى النَّعْتِ.", "«at» — the fronted khabar; the clause joins the description.", "«-de» — öne alınmış haber; cümle sıfata atıflı."),
  tok("أَوَّلِهِ", "awwal", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its beginning»", "«başında»", segments=[seg("أَوَّلِ", "awwal", "noun"), pr3msi()]),
  tok("أَحَدُ", "ahad", "noun", [K, MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«one of»", "«biri»"),
  tok("زَوَائِدِ", "zaid", "noun", [K, ID, JT, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ، مُضَافٌ — جَمْعُ زَائِدَةٍ: الْهَمْزَةُ وَالنُّونُ وَالْيَاءُ وَالتَّاءُ.", "«the augments of» — hamza, nūn, yāʾ, tāʾ.", "«zâidlerinden» — hemze, nûn, yâ, tâ."),
  tok("الْمُضَارِعِ", "mudari", "noun", [K, ID, IFA, MR], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the muḍāriʿ»", "«muzârinin»"),
  tok("غَيْرُ", "ghayr", "noun", [K, MK, ID, HT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هُوَ غَيْرُ، مُضَافٌ — جُمْلَةٌ مُعْتَرِضَةٌ.", "«not» — (it being) not …; an aside.", "«değil» — (o) … değil; ara cümle."),
  tok("فِعْلٍ", "fil", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a verb»", "«fiil»"),
  tok("بَلِ", "bal", "part", [K, AT], "حَرْفُ إِضْرَابٍ، كُسِرَ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«but rather» — kasra for the meeting of two sukūns.", "«bilakis» — iki sâkinin karşılaşmasıyla kesreli."),
  tok("اسْمٌ", "ism", "noun", [K, AT, MK], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: بَلْ هُوَ اسْمٌ.", "«a noun»", "«isim»"),
  nahw(),
  cit("يَزِيدَ", "yazid", "propn", "«Yazīd» — the yāʾ augment on a name", "«Yezîd» — alemde yâ zâidi"),
  cit("وَيَشْكُرَ", "yashkur", "propn", "«and Yashkur»", "«ve Yeşkür»", first=False, punct="؛"),
 ]})
# ----------- s2 — every afʿal of preference and of description
S.append({"id": "s2", "translation": {"en": "and every afʿal of preference and of description — as in afʿal and abyaḍ;", "tr": "ve her tafdîl ve sıfat ef'ali — ef'al ve ebyad gibi;"},
 "tokens": [
  wakullu(),
  tok("أَفْعَلِ", "afal-wazn", "noun", [K, ID, MMS, TFD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ، مُضَافٌ — الْوَزْنُ.", "«afʿal of» — the pattern.", "«ef'al» — vezin."),
  tok("التَّفْضِيلِ", "tafdil", "noun", [K, ID, MSD, F2, TFD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«preference»", "«tafdîl»"),
  tok("وَالصِّفَةِ", "sifa", "noun", [K, AT, ID, SM], "الْوَاوُ عَاطِفَةٌ، وَالصِّفَةِ مَعْطُوفٌ عَلَى التَّفْضِيلِ مَجْرُورٌ — الصِّفَةُ الْمُشَبَّهَةُ.", "«and of description» — the resembling adjective.", "«ve sıfat» — sıfat-ı müşebbehe."),
  nahw(),
  cit("أَفْعَلَ", "afal-wazn", "noun", "«afʿal» — the pattern itself cited", "«ef'al» — veznin kendisi", extra=(TFD,)),
  cit("وَأَبْيَضَ", "abyad", "noun", "«and abyaḍ» — «white»", "«ve ebyad» — «beyaz»", first=False, punct="؛", extra=(SM,)),
 ]})
# ----------- s3 — every foreign noun made a proper name
S.append({"id": "s3", "translation": {"en": "and every foreign noun used, at its first transfer to the Arabs, as a proper name, when it exceeds three letters or its middle is vowelled — as in Qālūn, Ibrāhīm and Shatar;", "tr": "ve Araplara ilk naklinde alem olarak kullanılan, üçten fazla harfli ya da ortası harekeli her a'cemî isim — Kâlûn, İbrâhîm ve Şeter gibi;"},
 "tokens": [
  wakullu(),
  tok("اسْمٍ", "ism", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«noun»", "«isim»"),
  tok("أَعْجَمِيٍّ", "ajami", "noun", [K, NA, NSB, MMS], "نَعْتٌ مَجْرُورٌ — الْعُجْمَةُ أَحَدُ السَّبَبَيْنِ.", "«foreign» — foreignness is one of the two causes.", "«a'cemî» — ucme iki sebepten biri."),
  tok("اسْتُعْمِلَ", "istamala", "verb", [K, NA, NF, F10], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.", "«used» — a second describing clause.", "«kullanılan» — ikinci sıfat cümlesi."),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«at»", "«-de»"),
  tok("أَوَّلِ", "awwal", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the first of»", "«ilk»"),
  tok("نَقْلِهِ", "naql", "noun", [K, ID, MSD], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its transfer»", "«naklinde»", segments=[seg("نَقْلِ", "naql", "noun"), pr3msi()]),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْعَرَبِ", "arab", "noun", [K, HJ], "مَجْرُورٌ بِإِلَى.", "«the Arabs»", "«Araplara»"),
  tok("عَلَمًا", "alam-name", "noun", [K, "hal", ALM, MMS], "حَالٌ مِنْ نَائِبِ الْفَاعِلِ مَنْصُوبٌ — الْعَلَمِيَّةُ السَّبَبُ الثَّانِي.", "«as a proper name» — name-hood, the second cause.", "«alem olarak» — alemiyet ikinci sebep."),
  tok("وَهُوَ", "huwa", "pron", [K, AT, MK, "hal"], "الْوَاوُ لِلْحَالِ، وَهُوَ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«while it is»", "«o … iken»", segments=wa("هُوَ", "huwa", "pron")),
  tok("زَائِدٌ", "zaid", "noun", [K, MK, IFA, HV], "خَبَرٌ مَرْفُوعٌ.", "«exceeding»", "«fazla»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«over»", "«üzerine»"),
  tok("الثَّلَاثَةِ", "thalatha", "noun", [K, HJ], "مَجْرُورٌ بِعَلَى — ثَلَاثَةِ أَحْرُفٍ.", "«three» — three letters.", "«üç» — üç harf."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("مُتَحَرِّكُ", "mutaharrik", "noun", [K, AT, MK, ID, IFA, F5], "مَعْطُوفٌ عَلَى زَائِدٌ مَرْفُوعٌ، مُضَافٌ.", "«vowelled in»", "«harekeli»"),
  tok("الْأَوْسَطِ", "awsat", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَخَرَجَ نُوحٌ وَلُوطٌ، فَإِنَّهُمَا يَنْصَرِفَانِ.", "«the middle» — so Nūḥ and Lūṭ, three-lettered with a still middle, decline.", "«ortası» — Nûh ve Lût üçlü ve ortası sâkin olduğundan munsariftir.", punct="،"),
  nahw(),
  cit("قَالُونَ", "qalun", "propn", "«Qālūn» — the commentary: a Greek word for «good», made a name", "«Kâlûn» — şerh: Rumca «iyi», ad yapılmış"),
  cit("وَإِبْرَاهِيمَ", "ibrahim", "propn", "«and Ibrāhīm»", "«ve İbrâhîm»", first=False),
  cit("وَشَتَرَ", "shatar", "propn", "«and Shatar» — three-lettered but vowelled in the middle", "«ve Şeter» — üç harfli ama ortası harekeli", first=False, punct="؛"),
 ]})
# ----------- s4 — every feminine by the alif
S.append({"id": "s4", "translation": {"en": "and every feminine by the alif, shortened or lengthened — as in ḥublā and ḥamrāʾ.", "tr": "ve maksûre ya da memdûde elif ile her müennes — hublâ ve hamrâ gibi."},
 "tokens": [
  wakullu(),
  tok("مُؤَنَّثٍ", "muannath", "noun", [K, ID, IMF, F2, MN, MMS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«feminine»", "«müennes»"),
  tok("بِالْأَلِفِ", "alif-letter", "noun", [K, HJ, MN, MMS], "الْبَاءُ حَرْفُ جَرٍّ، وَالْأَلِفِ مَجْرُورٌ — أَلِفُ التَّأْنِيثِ تَقُومُ مَقَامَ السَّبَبَيْنِ.", "«by the alif» — the feminine alif counts as both causes.", "«elif ile» — te'nis elifi iki sebep yerine geçer.", segments=[seg("بِ", "bi", "prep"), seg("الْأَلِفِ", "alif-letter", "noun")]),
  tok("مَقْصُورَةً", "maqsur", "noun", [K, "hal", IMF, MQ], "حَالٌ مِنَ الْأَلِفِ مَنْصُوبٌ.", "«shortened» — a ḥāl of the alif.", "«maksûre» — elifin hâli."),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("مَمْدُودَةً", "mamdud", "noun", [K, AT, "hal", IMF], "مَعْطُوفٌ مَنْصُوبٌ.", "«lengthened»", "«memdûde»", punct="،"),
  nahw(),
  cit("حُبْلَى", "hubla", "noun", "«ḥublā» — «pregnant», with the shortened alif; jarr by an implied fatḥa", "«hublâ» — «gebe», maksûre elifle; takdîrî fetha ile mecrûr", ar="لَفْظٌ مَحْكِيٌّ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — غَيْرُ مُنْصَرِفٍ.", extra=(MN, MQ)),
  cit("وَحَمْرَاءَ", "hamra", "noun", "«and ḥamrāʾ» — «red», with the lengthened alif", "«ve hamrâ» — «kırmızı», memdûde elifle", first=False, punct=".", extra=(MN,)),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "shammara": G("shammara", "شَمَّرَ", "ش م ر", "verb", "to roll up (sleeves), to gird oneself (form II) — cited as a verb-pattern", "sıvamak, hazırlanmak (II. bab) — fiil vezni örneği", 4, form="II"),
 "istakhraja": G("istakhraja", "اسْتَخْرَجَ", "خ ر ج", "verb", "to extract, to bring out (form X)", "çıkarmak, istihrâc etmek (X. bab)", 3, form="X"),
 "yashkur": G("yashkur", "يَشْكُرُ", "ش ك ر", "propn", "Yashkur — a tribal name on a muḍāriʿ pattern (diptote)", "Yeşkür — muzâri vezninde kabile adı (gayr-ı munsarif)", 5),
 "afal-wazn": G("afal-wazn", "أَفْعَلُ", "ف ع ل", "noun", "the pattern afʿal — of the elative and of colour/defect adjectives (diptote)", "ef'al vezni — ism-i tafdîl ve renk/kusur sıfatlarının (gayr-ı munsarif)", 4),
 "ajami": G("ajami", "أَعْجَمِيّ", "ع ج م", "noun", "foreign, non-Arabic (of a word)", "a'cemî, Arapça olmayan (kelime)", 4),
 "mutaharrik": G("mutaharrik", "مُتَحَرِّك", "ح ر ك", "noun", "vowelled, bearing a vowel (of a letter)", "harekeli (harf)", 3),
 "qalun": G("qalun", "قَالُونُ", "ق ل ن", "propn", "Qālūn — the name of Nāfiʿ's transmitter; a foreign word (diptote)", "Kâlûn — Nâfi'in râvisinin adı; a'cemî kelime (gayr-ı munsarif)", 5),
 "shatar": G("shatar", "شَتَرُ", "ش ت ر", "propn", "Shatar — a place-name; foreign, three-lettered with a vowelled middle (diptote)", "Şeter — yer adı; a'cemî, üç harfli ve ortası harekeli (gayr-ı munsarif)", 5),
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
put_morph(mo, "shammara", {"bab": "الْبَابُ الثَّانِي فَعَّلَ", "wazn": "فَعَّلَ يُفَعِّلُ", "masdar": "تَشْمِير", "ismFail": "مُشَمِّر",
 "mazi": ["شَمَّرَ", "شَمَّرَا", "شَمَّرُوا", "شَمَّرَتْ", "شَمَّرَتَا", "شَمَّرْنَ", "شَمَّرْتَ", "شَمَّرْتُمَا", "شَمَّرْتُمْ", "شَمَّرْتِ", "شَمَّرْتُمَا", "شَمَّرْتُنَّ", "شَمَّرْتُ", "شَمَّرْنَا"],
 "mudari": ["يُشَمِّرُ", "يُشَمِّرَانِ", "يُشَمِّرُونَ", "تُشَمِّرُ", "تُشَمِّرَانِ", "يُشَمِّرْنَ", "تُشَمِّرُ", "تُشَمِّرَانِ", "تُشَمِّرُونَ", "تُشَمِّرِينَ", "تُشَمِّرَانِ", "تُشَمِّرْنَ", "أُشَمِّرُ", "نُشَمِّرُ"],
 "amr": ["شَمِّرْ", "شَمِّرَا", "شَمِّرُوا", "شَمِّرِي", "شَمِّرَا", "شَمِّرْنَ"], "mansub": "يُشَمِّرَ", "majzum": "يُشَمِّرْ", "majzum2": "تُشَمِّرْ",
 "note": "شَمَّرَ ثَوْبَهُ يُشَمِّرُ تَشْمِيرًا: رَفَعَهُ — مِنَ الْبَابِ الثَّانِي؛ يُذْكَرُ فِي الْمَتْنِ وَزْنًا مَخْصُوصًا بِالْفِعْلِ يُمْنَعُ الْعَلَمُ عَلَيْهِ مِنَ الصَّرْفِ."})
put_morph(mo, "istakhraja", {"bab": "بَابُ الِاسْتِفْعَالِ", "wazn": "اِسْتَفْعَلَ يَسْتَفْعِلُ", "masdar": "اِسْتِخْرَاج", "ismFail": "مُسْتَخْرِج",
 "mazi": ["اِسْتَخْرَجَ", "اِسْتَخْرَجَا", "اِسْتَخْرَجُوا", "اِسْتَخْرَجَتْ", "اِسْتَخْرَجَتَا", "اِسْتَخْرَجْنَ", "اِسْتَخْرَجْتَ", "اِسْتَخْرَجْتُمَا", "اِسْتَخْرَجْتُمْ", "اِسْتَخْرَجْتِ", "اِسْتَخْرَجْتُمَا", "اِسْتَخْرَجْتُنَّ", "اِسْتَخْرَجْتُ", "اِسْتَخْرَجْنَا"],
 "mudari": ["يَسْتَخْرِجُ", "يَسْتَخْرِجَانِ", "يَسْتَخْرِجُونَ", "تَسْتَخْرِجُ", "تَسْتَخْرِجَانِ", "يَسْتَخْرِجْنَ", "تَسْتَخْرِجُ", "تَسْتَخْرِجَانِ", "تَسْتَخْرِجُونَ", "تَسْتَخْرِجِينَ", "تَسْتَخْرِجَانِ", "تَسْتَخْرِجْنَ", "أَسْتَخْرِجُ", "نَسْتَخْرِجُ"],
 "amr": ["اِسْتَخْرِجْ", "اِسْتَخْرِجَا", "اِسْتَخْرِجُوا", "اِسْتَخْرِجِي", "اِسْتَخْرِجَا", "اِسْتَخْرِجْنَ"], "mansub": "يَسْتَخْرِجَ", "majzum": "يَسْتَخْرِجْ", "majzum2": "تَسْتَخْرِجْ",
 "note": "اِسْتَخْرَجَ الشَّيْءَ يَسْتَخْرِجُهُ اسْتِخْرَاجًا: أَخْرَجَهُ وَطَلَبَ خُرُوجَهُ — مِنْ بَابِ الِاسْتِفْعَالِ، هَمْزَتُهُ هَمْزَةُ وَصْلٍ؛ يُذْكَرُ وَزْنًا مَخْصُوصًا بِالْفِعْلِ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch55 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("daraba", "shammara", "inqataa", "ijtamaa", "istakhraja", "istamala") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "غَيْرُ الْمُنْصَرِفِ الْقِيَاسِيُّ: الْعَلَمُ عَلَى وَزْنِ الْفِعْلِ أَوْ بِزَائِدِ الْمُضَارِعِ، وَأَفْعَلُ التَّفْضِيلِ وَالصِّفَةِ، وَالْأَعْجَمِيُّ الْعَلَمُ، وَالْمُؤَنَّثُ بِالْأَلِفِ", "en": "The qiyāsī diptote: the name on a verb pattern or with a muḍāriʿ augment, afʿal of preference and description, the foreign name, the feminine by alif", "tr": "Kıyâsî gayr-ı munsarif: fiil vezninde ya da muzâri zâidli alem, tafdîl ve sıfat ef'ali, a'cemî alem, elif ile müennes"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — غير المنصرف القياسي", "الكافية لابن الحاجب — أسباب منع الصرف", "شرح قطر الندى لابن هشام — الممنوع من الصرف"],
 "amil": "the qiyāsī ghayr munṣarif, by rule: every proper name on a pattern particular to the verb (ضُرِبَ، شَمَّرَ، انْقَطَعَ، اجْتَمَعَ، اسْتَخْرَجَ) or beginning with a muḍāriʿ augment while a noun (يَزِيدَ، يَشْكُرَ); every afʿal of preference and of description (أَفْعَلَ، أَبْيَضَ); every foreign noun used as a name at its first transfer when over three letters or vowelled in the middle (قَالُونَ، إِبْرَاهِيمَ، شَتَرَ); every feminine by the shortened or lengthened alif (حُبْلَى، حَمْرَاءَ).",
 "question": {
  "en": ["What makes the qiyāsī diptote «by rule»? A stated cause-pair that any word meeting it falls under — name-hood plus verb-pattern, description plus verb-pattern, name-hood plus foreignness, or the feminine alif which counts as two.",
         "Which verb patterns bar a name from declining? Those particular to the verb: ضُرِبَ (the commentary's reading), شَمَّرَ, انْقَطَعَ, اجْتَمَعَ, اسْتَخْرَجَ — a man called by any of them is a diptote.",
         "What of يَزِيد and يَشْكُر? Names beginning with one of the muḍāriʿ augments (hamza, nūn, yāʾ, tāʾ) while being nouns, not verbs — the print's «غير فعل بل اسم»; the Ottoman commentary glosses the clause as the name's not accepting the tāʾ.",
         "Why are أَفْعَل of preference and of description barred? Description plus verb-pattern: أَفْضَلُ and أَبْيَضُ sit on the pattern of the verb (أَفْعَلُ as in أَكْرَمُ «I honour»).",
         "When is a foreign name a diptote? When it was used as a name at its first transfer to the Arabs and exceeds three letters (إِبْرَاهِيمَ، قَالُونَ) or has a vowelled middle (شَتَرَ) — not نُوح and لُوط, three-lettered with a still middle.",
         "What is the commentary's note on قَالُون and شَتَر? Qālūn was a Greek common noun («good») made the name of a transmitter of Nāfiʿ's reading; Shatar is a fortress in the region of Diyarbakır (izhar-full-corrected l. 1739-1743).",
         "Why does the feminine alif alone bar declension? Because it stands for both causes — حُبْلَى and حَمْرَاءُ take neither kasra nor tanwīn without any second cause.",
         "What does the engine READ here? The DabtEngine reads the cited patterns and names after نَحْوُ and the kāf at their printed fatḥa as diptotes, حُبْلَى with an implied fatḥa on its alif, and the rule-clauses — كُلُّ عَلَمٍ … أَوْ فِي أَوَّلِهِ أَحَدُ زَوَائِدِ الْمُضَارِعِ — as khabar, description and fronted-khabar chains."],
  "tr": ["Kıyâsî gayr-ı munsarifi «kurallı» kılan nedir? Belirli bir sebep çifti; ona uyan her kelime kapsama girer — alemiyet ve fiil vezni, vasfiyet ve fiil vezni, alemiyet ve ucme, ya da iki sebep yerine geçen te'nis elifi.",
         "Hangi fiil vezinleri alemi sarftan men eder? Fiile mahsus olanlar: duribe (şerhin okuyuşu), şemmera, inkataa, ictemea, istahrece — bunlardan biriyle adlanan kişi gayr-ı munsariftir.",
         "Yezîd ve Yeşkür'ün durumu? Muzâri zâidlerinden biriyle (hemze, nûn, yâ, tâ) başlayan ve fiil değil isim olan alemler — baskının «gayru fi'lin bel ismun»u; Osmanlı şerhi ibareyi alemin tâ'yı kabul etmemesi diye açıklar.",
         "Tafdîl ve sıfat ef'ali neden men edilir? Vasfiyet ve fiil vezni: efdalü ve ebyadu fiil vezni üzeredir (ekremü «ikram ederim» gibi ef'alü).",
         "A'cemî alem ne zaman gayr-ı munsariftir? Araplara ilk naklinde alem olarak kullanılıp üçten fazla harfli (İbrâhîme, Kâlûne) ya da ortası harekeli (Şetere) olunca — Nûh ve Lût üçlü ve ortası sâkin olduğundan değil.",
         "Şerhin Kâlûn ve Şeter notu nedir? Kâlûn Rumca bir cins isimken («iyi») Nâfi' kıraatinin bir râvisine ad yapılmış; Şeter Diyarbakır yöresinde bir kaledir (izhar-full-corrected s. 1739-1743).",
         "Te'nis elifi tek başına neden sarfı men eder? Çünkü iki sebep yerine geçer — hublâ ve hamrâu ikinci sebepsiz kesre ve tenvin almaz.",
         "Motor burada neyi OKUR? DabtEngine nahvü ve kâf'tan sonra alıntılanan vezin ve adları basılı fethalarıyla gayr-ı munsarif, hublâ'yı elifinde takdîrî fetha ile, kural cümlelerini — küllü alemin … ev fî evvelihî ehadü zevâidi'l-muzârii — haber, sıfat ve öne alınmış haber zincirleri olarak okur."],
 },
 "plain": {"en": "Some nouns refuse kasra and tanwīn by rule. A name shaped like a verb (Shammar, Yazīd), an adjective shaped like afʿal (abyaḍ «white», afḍal «better»), a foreign name longer than three letters or with a vowelled middle (Ibrāhīm, Qālūn, Shatar), and any feminine ending in the alif (ḥublā, ḥamrāʾ) take a fatḥa for jarr.",
           "tr": "Bazı isimler kesre ve tenvini kural gereği reddeder. Fiil biçimli bir ad (Şemmer, Yezîd), ef'al biçimli sıfat (ebyad «beyaz», efdal «daha iyi»), üç harften uzun ya da ortası harekeli yabancı ad (İbrâhîm, Kâlûn, Şeter) ve elifle biten her dişil (hublâ, hamrâ) cerde fetha alır."},
 "explanation": {"en": "The qiyāsī ghayr munṣarif is the one with a rule. It is every proper name on a pattern particular to the verb — ضُرِبَ (the Ottoman commentary's vowelling of the print's unvowelled ضرب), شَمَّرَ، انْقَطَعَ، اجْتَمَعَ، اسْتَخْرَجَ — or at whose beginning is one of the muḍāriʿ's augments while it is not a verb but a noun, as يَزِيد and يَشْكُر; the commentary glosses the clause by the name's not accepting the tāʾ. It is every afʿal of preference and of description — أَفْعَلُ and أَبْيَضُ. It is every foreign noun used as a proper name at its first transfer to the Arabs, when it exceeds three letters or its middle is vowelled — قَالُون، إِبْرَاهِيم، شَتَر; the commentary notes that Qālūn was a Greek common noun meaning «good», given as a name to a transmitter of Nāfiʿ, and that Shatar is a fortress in the Diyarbakır region whose vowelled middle bars it though it is three-lettered. And it is every feminine by the alif, shortened or lengthened — حُبْلَى and حَمْرَاء. The remaining qiyāsī kinds follow in the next chapter.",
                 "tr": "Kıyâsî gayr-ı munsarif, kuralı olandır. Fiile mahsus bir vezin üzere olan her alemdir — duribe (baskının harekesiz ضرب'ının Osmanlı şerhindeki harekesi), şemmera, inkataa, ictemea, istahrece — ya da başında muzârinin zâidlerinden biri bulunup fiil değil isim olandır, Yezîd ve Yeşkür gibi; şerh ibareyi alemin tâ'yı kabul etmemesiyle açıklar. Her tafdîl ve sıfat ef'alidir — ef'alü ve ebyadu. Araplara ilk naklinde alem olarak kullanılan, üçten fazla harfli ya da ortası harekeli her a'cemî isimdir — Kâlûn, İbrâhîm, Şeter; şerh, Kâlûn'un Rumca «iyi» anlamında bir cins isimken Nâfi'in bir râvisine ad verildiğini, Şeter'in Diyarbakır yöresinde bir kale olup üç harfli olduğu halde ortası harekeli olduğundan men edildiğini not eder. Ve maksûre ya da memdûde elif ile her müennestir — hublâ ve hamrâ. Kalan kıyâsî türler sonraki babda gelir."},
 "examples": [
  {"ar": "كُلُّ عَلَمٍ عَلَى وَزْنٍ مَخْصُوصٍ بِالْفِعْلِ كَضُرِبَ وَشَمَّرَ", "en": "the name on a verb pattern", "tr": "fiil vezninde alem", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "فِي أَوَّلِهِ أَحَدُ زَوَائِدِ الْمُضَارِعِ، نَحْوُ يَزِيدَ وَيَشْكُرَ", "en": "the name with a muḍāriʿ augment", "tr": "muzâri zâidli alem", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "كُلُّ أَفْعَلِ التَّفْضِيلِ وَالصِّفَةِ، نَحْوُ أَفْعَلَ وَأَبْيَضَ", "en": "afʿal of preference and description", "tr": "tafdîl ve sıfat ef'ali", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "نَحْوُ قَالُونَ وَإِبْرَاهِيمَ وَشَتَرَ", "en": "the foreign names", "tr": "a'cemî adlar", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "كُلُّ مُؤَنَّثٍ بِالْأَلِفِ مَقْصُورَةً أَوْ مَمْدُودَةً، نَحْوُ حُبْلَى وَحَمْرَاءَ", "en": "the feminine by alif", "tr": "elif ile müennes", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "مَرَرْتُ بِيَزِيدٍ", "right": "مَرَرْتُ بِيَزِيدَ", "why": {"en": "a name beginning with a muḍāriʿ augment is a diptote: no tanwīn, jarr by fatḥa", "tr": "muzâri zâidiyle başlayan alem gayr-ı munsariftir: tenvin yok, cer fetha ile"}},
  {"wrong": "مَرَرْتُ بِنُوحَ", "right": "مَرَرْتُ بِنُوحٍ", "why": {"en": "a three-lettered foreign name with a still middle declines", "tr": "üç harfli, ortası sâkin a'cemî alem munsariftir"}},
  {"wrong": "ثَوْبٌ أَبْيَضٌ", "right": "ثَوْبٌ أَبْيَضُ", "why": {"en": "afʿal of description takes no tanwīn", "tr": "sıfat ef'ali tenvin almaz"}},
  {"wrong": "مَرَرْتُ بِحَمْرَاءٍ", "right": "مَرَرْتُ بِحَمْرَاءَ", "why": {"en": "the lengthened feminine alif bars kasra and tanwīn by itself", "tr": "memdûde te'nis elifi tek başına kesre ve tenvini men eder"}},
 ],
}
ADD_EN = (" Chapter 55 (print pp. 150-151): the qiyāsī diptote — the name on a verb pattern or with a muḍāriʿ augment (s1), afʿal of preference and description (s2), the foreign name over three letters or vowelled in the middle (s3), the feminine by the shortened or lengthened alif (s4).")
ADD_TR = (" Elli beşinci bab (baskı s. 150-151): kıyâsî gayr-ı munsarif — fiil vezninde ya da muzâri zâidli alem (s1), tafdîl ve sıfat ef'ali (s2), üçten fazla harfli ya da ortası harekeli a'cemî alem (s3), maksûre ya da memdûde elifle müennes (s4).")
write_out(55, S, TITLE, ADD_EN, ADD_TR, "pp. 150-151", GLOSS_ADD, notes=(NOTE,),
          related=((K54, [K]), (MMS, [K]), (ALM, [K]), (TFD, [K]), (SM, [K]), (MN, [K])))
report(55, S, GLOSS_ADD, (NOTE,))
