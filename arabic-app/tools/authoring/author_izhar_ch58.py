# -*- coding: utf-8 -*-
# Izhar al-Asrar (Birgivi) — chapter 58: the taqdīrī's SECOND position — what is annexed to the speaker's yāʾ other than the dual: the sound masculine
# plural estimated in rafʿ only (جَاءَنِي مُسْلِمِيَّ، أَصْلُهُ مُسْلِمُويَ), anything else estimated throughout (غُلَامِي وَرِجَالِي وَمُسْلِمَاتِي); the THIRD — what carries a
# cited iʿrāb at its end: a sentence moved to name-hood (تَأَبَّطَ شَرًّا), a single word in the Ḥijāzī's speech (مَنْ زَيْدًا؟ to one who said ضَرَبْتُ زَيْدًا;
# دَعْنِي مِنْ تَمْرَتَانِ to one who said إِلَيَّ تَمْرَتَانِ), every compound name whose second part is governed by the first in iʿrāb (إِنَّ زَيْدًا، هَلْ زَيْدٌ، مِنْ زَيْدٍ)
# — unlike عَبْدِ اللهِ and مَضْرُوبٍ غُلَامُهُ, whose first part is lafẓī by its governor and whose second is busy with its cited iʿrāb — or a cited
# indeclinability (خَمْسَةَ عَشَرَ as a name, on the better-known view). Print p. 153.
# Readings: the lithograph's unvowelled «ومن زيد» is read مِنْ زَيْدٍ with the Ottoman commentary (izhar-full-corrected l. 1809: «zaydin was majrūr»);
# the commentary quotes the date example as أَلَكَ تَمْرَتَانِ / دَعْنِي عَنْ تَمْرَتَانِ (l. 1806-1807), while the lithograph prints إلي تمرتان / دعني من تمرتان —
# the text keeps the lithograph (إِلَيَّ تَمْرَتَانِ، دَعْنِي مِنْ تَمْرَتَانِ) and notes the variant in the explanation.
#   python3 author_izhar_ch58.py   (DRY_PKG=<copy> DRY_GR=<grammar copy> for a dry run)
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
TMZ = "tamyiz"; TK = "tawkid"; TW = "tawabi-al-musnad-ilayh"; BM = "al-bariz-al-muttasil"; IRB = "al-murab-wal-mabni-wal-irab"; F8 = "form-viii-verbs"; MMS = "mamnu-min-sarf"; JDS = "jam-mudhakkar-salim"; JMS = "jam-muannath-salim"; ALM = "al-marifa-al-mudmarat-wal-alam"; HK = "hikayat-al-hal"; AMR = "imperative-amr"; ADD = "al-muthanna"; NQV = "naqis-verbs"
K = "al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"
K57 = "taqsim-al-irab-bil-naw-wal-sifa-wal-taqdiri-al-awwal"
TITLE = {"ar": "الْمَوْضِعُ الثَّانِي وَالثَّالِثُ لِلتَّقْدِيرِيِّ: الْمُضَافُ إِلَى يَاءِ الْمُتَكَلِّمِ، وَمَا فِي آخِرِهِ إِعْرَابٌ أَوْ بِنَاءٌ مَحْكِيٌّ", "en": "The second and third positions of the taqdīrī: the word annexed to the speaker's yāʾ, and the word carrying a cited iʿrāb or indeclinability", "tr": "Takdîrînin ikinci ve üçüncü mevzii: mütekellim yâsına muzâf olan ve sonunda hikâye edilen i'râb ya da binâ bulunan"}

def nahw(punct=None): return tok("نَحْوُ", "nahw", "noun", [K, MK, HT, ID], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، مُضَافٌ إِلَى الْمَحْكِيِّ.", "«as in»", "«… gibi»", punct=punct)
def wnahw(punct=None): return tok("وَنَحْوُ", "nahw", "noun", [K, AT, MK, HT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوُ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، مُضَافٌ.", "«and as in»", "«ve … gibi»", punct=punct, segments=wa("نَحْوُ", "nahw", "noun"))
def liman_qala(): return [tok("لِمَنْ", "man-mawsula", "pron", [K, HJ, MAW], "اللَّامُ حَرْفُ جَرٍّ، وَمَنْ اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ.", "«to one who»", "«diyene»", segments=[seg("لِ", "li", "prep"), seg("مَنْ", "man-mawsula", "pron")]), tok("قَالَ", "qala", "verb", [K, MAW, HV, FL], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةُ مَنْ.", "«said»", "«diyen»", punct=":")]

# ----------- s1 — the second position: annexed to the speaker's yāʾ
S.append({"id": "s1", "translation": {"en": "And the second: what is annexed to the speaker's yāʾ, other than the dual. If it is the sound masculine plural, its rafʿ alone is taqdīrī — as in «there came to me my Muslims», whose origin is muslimūya; and if it is other than that, the whole is taqdīrī — as in «my servant», «my men» and «my Muslim women».", "tr": "İkincisi: tesniye dışında mütekellim yâsına muzâf olan. Cem'-i müzekker-i sâlim ise yalnız ref'i takdîrîdir — «bana müslümanlarım geldi» gibi, aslı müslimûye'dir; ondan başkası ise hepsi takdîrîdir — «kölem», «adamlarım» ve «müslüman kadınlarım» gibi."},
 "tokens": [
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dir»"),
  tok("أُضِيفَ", "adafa", "verb", [K, MAW, NF, F4, YM], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — صِلَةُ مَا.", "«is annexed» — the ṣila.", "«muzâf olan» — sıla."),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("يَاءِ", "ya-letter", "noun", [K, HJ, ID, YM], "مَجْرُورٌ بِإِلَى، مُضَافٌ.", "«the yāʾ of»", "«yâsına»"),
  tok("الْمُتَكَلِّمِ", "mutakallim", "noun", [K, ID, IFA, F5, YM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the speaker»", "«mütekellim»"),
  tok("غَيْرَ", "ghayr", "noun", [K, "hal", ID, MST if False else "al-mustathna-badaluhu-wa-jarruh-wa-ghayr-wa-illa"], "مُسْتَثْنًى بِغَيْرَ مَنْصُوبٌ، مُضَافٌ.", "«other than» — the exception.", "«dışında» — istisnâ."),
  tok("التَّثْنِيَةِ", "tathniya", "noun", [K, ID, MSD, F2, MTH], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — فَإِنَّ إِعْرَابَهُ لَفْظِيٌّ: غُلَامَايَ وَغُلَامَيَّ.", "«the dual» — whose iʿrāb stays lafẓī: ghulāmāya, ghulāmayya.", "«tesniye» — i'râbı lafzî kalır: gulâmâye, gulâmeyye.", punct="،"),
  tok("فَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْفَاءُ لِلتَّفْرِيعِ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«so if»", "«eğer»", segments=fa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«it is»", "«ise»"),
  tok("جَمْعَ", "jam", "noun", [K, KN, ID, JDS], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ.", "«the plural of»", "«cem'-i»"),
  tok("الْمُذَكَّرِ", "mudhakkar", "noun", [K, ID, IMF, F2, JDS], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the masculine»", "«müzekker»"),
  tok("السَّالِمَ", "salim", "noun", [K, NA, IFA, JDS], "نَعْتٌ لِجَمْعَ مَنْصُوبٌ.", "«sound»", "«sâlim»"),
  tok("فَرَفْعُهُ", "raf", "noun", [K, INS, MK, ID, MSD, IRB], "الْفَاءُ رَابِطَةٌ لِلْجَوَابِ، وَرَفْعُ مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its rafʿ»", "«ref'i»", segments=[seg("فَ", "fa", "conj"), seg("رَفْعُ", "raf", "noun"), pr3ms()]),
  tok("تَقْدِيرِيٌّ", "taqdiri", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", "«is taqdīrī»", "«takdîrîdir»"),
  tok("فَقَطْ", "faqat", "part", [K], "الْفَاءُ زَائِدَةٌ، وَقَطْ اسْمُ فِعْلٍ بِمَعْنَى: حَسْبُ — أَيْ دُونَ نَصْبِهِ وَجَرِّهِ.", "«only» — not its naṣb and jarr.", "«yalnız» — nasb ve ceri değil.", punct="،"),
  nahw(punct=":"),
  tok("جَاءَنِي", "jaa", "verb", [K, FL, MB, HV], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«there came to me»", "«bana geldi»", segments=[seg("جَاءَ", "jaa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("مُسْلِمِيَّ", "muslim", "noun", [K, FL, JDS, ID, YM, IRB], "فَاعِلٌ مَرْفُوعٌ بِوَاوٍ مُقَدَّرَةٍ قُلِبَتْ يَاءً وَأُدْغِمَتْ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.", "«my Muslims» — the rafʿ wāw estimated, turned to yāʾ and assimilated.", "«müslümanlarım» — ref' vâvı takdîrî, yâ'ya çevrilip idğam edilmiş.", punct="،", segments=[seg("مُسْلِمِي", "muslim", "noun"), seg("يَ", "pron-1s", "pron")]),
  tok("أَصْلُهُ", "asl", "noun", [K, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its origin»", "«aslı»", segments=[seg("أَصْلُ", "asl", "noun"), pr3ms()]),
  tok("مُسْلِمُويَ", "muslim", "noun", [K, MK, JDS, ID, YM], "خَبَرٌ مَرْفُوعٌ — لَفْظٌ مَحْكِيٌّ: الْأَصْلُ قَبْلَ الْإِعْلَالِ، بِالْوَاوِ وَيَاءِ الْمُتَكَلِّمِ.", "«muslimūya» — the form before the sound-change.", "«müslimûye» — i'lâlden önceki şekil.", punct="،", segments=[seg("مُسْلِمُو", "muslim", "noun"), seg("يَ", "pron-1s", "pron")]),
  tok("وَإِنْ", "in-shartiyya", "part", [K, AT, INS, JZ], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and if»", "«ve eğer»", segments=wa("إِنْ", "in-shartiyya", "part")),
  tok("كَانَ", "kana", "verb", [K, INS, KN, HV], "فِعْلُ الشَّرْطِ، مَاضٍ نَاقِصٌ.", "«it is»", "«ise»"),
  tok("غَيْرَهُ", "ghayr", "noun", [K, KN, ID], "خَبَرُ كَانَ مَنْصُوبٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«other than that»", "«ondan başkası»", segments=[seg("غَيْرَ", "ghayr", "noun"), pr3ms()]),
  tok("فَالْكُلُّ", "kull", "noun", [K, INS, MK], "الْفَاءُ رَابِطَةٌ، وَالْكُلُّ مُبْتَدَأٌ مَرْفُوعٌ — الْأَحْوَالُ الثَّلَاثُ.", "«the whole» — all three states.", "«hepsi» — üç hâl.", segments=fa("الْكُلُّ", "kull", "noun")),
  tok("تَقْدِيرِيٌّ", "taqdiri", "noun", [K, MK, NSB, IRB], "خَبَرٌ مَرْفُوعٌ.", "«is taqdīrī»", "«takdîrîdir»", punct="،"),
  nahw(),
  tok("غُلَامِي", "ghulam", "noun", [K, ID, YM, IRB], "لَفْظٌ مَحْكِيٌّ: مُضَافٌ إِلَى الْيَاءِ، الْكَسْرَةُ لِلْمُنَاسَبَةِ وَالْإِعْرَابُ مُقَدَّرٌ.", "«my servant» — the kasra is for the yāʾ; the iʿrāb estimated.", "«kölem» — kesre yâ içindir; i'râb takdîrî.", segments=[seg("غُلَامِ", "ghulam", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَرِجَالِي", "rajul", "noun", [K, AT, JT, ID, YM, IRB], "الْوَاوُ عَاطِفَةٌ، وَرِجَالِي مَعْطُوفٌ — جَمْعُ تَكْسِيرٍ مُضَافٌ إِلَى الْيَاءِ.", "«and my men» — a broken plural.", "«ve adamlarım» — cem'-i mükesser.", segments=[seg("وَ", "wa", "conj"), seg("رِجَالِ", "rajul", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("وَمُسْلِمَاتِي", "muslima", "noun", [K, AT, JMS, ID, YM, IRB], "الْوَاوُ عَاطِفَةٌ، وَمُسْلِمَاتِي مَعْطُوفٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ مُضَافٌ إِلَى الْيَاءِ.", "«and my Muslim women» — the sound feminine plural.", "«ve müslüman kadınlarım» — cem'-i müennes-i sâlim.", punct=".", segments=[seg("وَ", "wa", "conj"), seg("مُسْلِمَاتِ", "muslima", "noun"), seg("ي", "pron-1s", "pron")]),
 ]})
# ----------- s2 — the third position: the cited iʿrāb — sentence and single word
S.append({"id": "s2", "translation": {"en": "And the third: what has at its end a cited iʿrāb — either a sentence moved to name-hood, as in Taʾabbaṭa Sharran; or a single word in the speech of the Ḥijāzī, as in «who — Zaydan?» to one who said «I struck Zaydan», and as in «leave me alone about tamratāni» to one who said «two dates are mine»;", "tr": "Üçüncüsü: sonunda hikâye edilen bir i'râb bulunan — ya alemliğe nakledilmiş bir cümle, Teebbeta Şerran gibi; ya da Hicazlının sözünde bir müfred, «Zeydi dövdüm» diyene «kim — Zeyden?» demek gibi ve «bende iki hurma var» diyene «beni iki hurmadan (temratâni) bırak» demek gibi;"},
 "tokens": [
  tok("وَالثَّالِثُ", "thalith", "noun", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَالثَّالِثُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the third»", "«üçüncüsü»", segments=wa("الثَّالِثُ", "thalith", "noun")),
  tok("مَا", "ma-mawsula", "pron", [K, MK, MAW], "اسْمٌ مَوْصُولٌ خَبَرٌ فِي مَحَلِّ رَفْعٍ.", "«what»", "«-dir»"),
  tok("فِي", "fi", "prep", [K, HJ, MAW, MK], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ صِلَةٌ.", "«at»", "«-de»"),
  tok("آخِرِهِ", "akhir", "noun", [K, HJ, ID], "مَجْرُورٌ بِفِي، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its end»", "«sonunda»", segments=[seg("آخِرِ", "akhir", "noun"), pr3msi()]),
  tok("إِعْرَابٌ", "irab", "noun", [K, MK, MSD, IRB], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«an iʿrāb»", "«bir i'râb»"),
  tok("مَحْكِيٌّ", "mahki", "noun", [K, NA, IMF, NSB, HK], "نَعْتٌ مَرْفُوعٌ — مَنْقُولٌ كَمَا كَانَ.", "«cited» — carried over as it was.", "«hikâye edilen» — olduğu gibi aktarılan.", punct=":"),
  tok("إِمَّا", "imma", "part", [K, AT, "taqsim"], "حَرْفُ تَفْصِيلٍ.", "«either»", "«ya»"),
  tok("جُمْلَةٌ", "jumla", "noun", [K, MK, HT], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ: هُوَ جُمْلَةٌ — أَوْ بَدَلٌ مِنْ إِعْرَابٌ بِتَقْدِيرِ مُضَافٍ.", "«a sentence»", "«bir cümle»"),
  tok("مَنْقُولَةٌ", "manqul", "noun", [K, NA, IMF], "نَعْتٌ مَرْفُوعٌ.", "«moved»", "«nakledilmiş»"),
  tok("إِلَى", "ila", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«to»", "«-e»"),
  tok("الْعَلَمِيَّةِ", "alamiyya", "noun", [K, HJ, NSB, ALM], "مَجْرُورٌ بِإِلَى.", "«name-hood»", "«alemliğe»", punct="،"),
  nahw(),
  tok("تَأَبَّطَ", "taabbata", "verb", [K, ID, ALM, HK, F5], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — الْجُمْلَةُ عَلَمٌ، مُضَافٌ إِلَيْهِ تَقْدِيرًا.", "«he put under his arm» — the sentence is a man's name; its iʿrāb estimated.", "«koltuğuna aldı» — cümle bir adamın adı; i'râbı takdîrî."),
  tok("شَرًّا", "sharr", "noun", [K, MB, HK], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْإِعْرَابُ الْمَحْكِيُّ فِي آخِرِ الْعَلَمِ.", "«an evil» — the cited iʿrāb at the name's end.", "«bir kötülük» — alemin sonundaki hikâye edilen i'râb.", punct="،"),
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ.", "«or»", "«ya da»"),
  tok("مُفْرَدٌ", "mufrad", "noun", [K, AT, IMF, F4], "مَعْطُوفٌ عَلَى جُمْلَةٌ مَرْفُوعٌ.", "«a single word»", "«bir müfred»"),
  tok("فِي", "fi", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«in»", "«-de»"),
  tok("قَوْلِ", "qawl", "noun", [K, HJ, ID, MSD], "مَجْرُورٌ بِفِي، مُضَافٌ.", "«the speech of»", "«sözünde»"),
  tok("الْحِجَازِيِّ", "hijazi", "noun", [K, ID, NSB], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَهْلُ الْحِجَازِ يَحْكُونَ الْمُفْرَدَ، وَبَنُو تَمِيمٍ يُعْرِبُونَهُ.", "«the Ḥijāzī» — the Ḥijāz cites the single word; Tamīm declines it.", "«Hicazlının» — Hicazlılar müfredi hikâye eder; Temîm i'râblar.", punct="،"),
  nahw(punct=":"),
  tok("مَنْ", "man-istifham", "pron", [K, IST, MK], "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ فِي مَحَلِّ رَفْعٍ.", "«who»", "«kim»"),
  tok("زَيْدًا", "zayd", "propn", [K, MK, HK], "خَبَرٌ مَرْفُوعٌ تَقْدِيرًا — مَحْكِيٌّ عَلَى نَصْبِ قَوْلِ الْمُتَكَلِّمِ.", "«Zaydan» — the khabar, estimated rafʿ; the speaker's naṣb cited.", "«Zeyden» — haber, takdîrî ref'; konuşanın nasbı hikâye edilmiş.", punct="؟"),
  *liman_qala(),
  tok("ضَرَبْتُ", "daraba", "verb", [K, FL], "لَفْظٌ مَحْكِيٌّ: فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I struck»", "«dövdüm»", segments=[seg("ضَرَبْ", "daraba", "verb"), seg("تُ", "pron-1s", "pron")]),
  tok("زَيْدًا", "zayd", "propn", [K, MB], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«Zayd»", "«Zeyd'i»", punct="،"),
  wnahw(punct=":"),
  tok("دَعْنِي", "daa", "verb", [K, AMR, MB, NQV], "لَفْظٌ مَحْكِيٌّ: فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ الْآخِرِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«leave me»", "«beni bırak»", segments=[seg("دَعْ", "daa", "verb"), seg("نِي", "pron-1s-obj", "pron")]),
  tok("مِنْ", "min", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«from»", "«-den»"),
  tok("تَمْرَتَانِ", "tamra", "noun", [K, HJ, MTH, HK], "مَجْرُورٌ بِمِنْ تَقْدِيرًا — مَحْكِيٌّ عَلَى رَفْعِ قَوْلِ الْمُتَكَلِّمِ، وَالْحِجَازِيُّ لَا يَقُولُ تَمْرَتَيْنِ.", "«tamratāni» — jarr estimated; the speaker's rafʿ cited, not tamratayni.", "«temratâni» — takdîrî cer; konuşanın ref'i hikâye edilmiş, temrateyni değil.", punct="،"),
  *liman_qala(),
  tok("إِلَيَّ", "ila", "prep", [K, HJ, MK], "إِلَى حَرْفُ جَرٍّ، وَالْيَاءُ مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ؛ الشَّرْحُ: أَلَكَ.", "«mine» — the fronted khabar; the commentary quotes alaka.", "«bende» — öne alınmış haber; şerh eleke der.", segments=[seg("إِلَيْ", "ila", "prep"), seg("يَ", "pron-1s", "pron")]),
  tok("تَمْرَتَانِ", "tamra", "noun", [K, MK, MTH], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ.", "«two dates»", "«iki hurma»", punct="،"),
 ]})
# ----------- s3 — the compound name whose second part is governed by the first
S.append({"id": "s3", "translation": {"en": "and likewise every compound proper name whose second part is governed by the first part in iʿrāb — as in Inna Zaydan, Hal Zaydun and Min Zaydin — unlike the likes of ʿAbd Allāh and of Maḍrūbun ghulāmuhu, for the iʿrāb of the first part of these two is lafẓī according to the governor, and the second is busy with its iʿrāb by citation;", "tr": "ve ikinci cüzü birinci cüze i'râb bakımından ma'mûl olan her mürekkep alem de böyledir — İnne Zeyden, Hel Zeydün ve Min Zeydin gibi — Abdullah ve Madrûbun gulâmuhû gibilerin aksine; çünkü bu ikisinde birinci cüzün i'râbı âmile göre lafzîdir, ikincisi ise hikâye ile i'râbıyla meşguldür;"},
 "tokens": [
  tok("وَكَذَا", "kadha", "part", [K, AT, MK], "الْوَاوُ عَاطِفَةٌ، وَكَذَا: الْكَافُ جَارَّةٌ وَذَا اسْمُ إِشَارَةٍ — خَبَرٌ مُقَدَّمٌ.", "«and likewise» — the fronted khabar.", "«ve böyledir» — öne alınmış haber.", segments=wa("كَذَا", "kadha", "part")),
  tok("كُلُّ", "kull", "noun", [K, MK, ID], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«every»", "«her»"),
  tok("عَلَمٍ", "alam-name", "noun", [K, ID, ALM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«proper name»", "«alem»"),
  tok("مُرَكَّبٍ", "murakkab", "noun", [K, NA, IMF, F2], "نَعْتٌ مَجْرُورٌ.", "«compound»", "«mürekkep»"),
  tok("جُزْؤُهُ", "juz", "noun", [K, NA, MK, ID], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.", "«whose part» — a second describing clause.", "«cüzü» — ikinci sıfat cümlesi.", segments=[seg("جُزْؤُ", "juz", "noun"), pr3ms()]),
  tok("الثَّانِي", "thani", "noun", [K, NA, MQ], "نَعْتٌ لِجُزْؤُهُ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«second»", "«ikinci»"),
  tok("مَعْمُولٌ", "mamul", "noun", [K, MK, IMF, AQ], "خَبَرٌ مَرْفُوعٌ.", "«governed»", "«ma'mûl»"),
  tok("لِلْجُزْءِ", "juz", "noun", [K, HJ], "اللَّامُ حَرْفُ جَرٍّ، وَالْجُزْءِ مَجْرُورٌ.", "«by the part»", "«cüze»", segments=[seg("لِ", "li", "prep"), seg("الْجُزْءِ", "juz", "noun")]),
  tok("الْأَوَّلِ", "awwal", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«first»", "«birinci»"),
  tok("إِعْرَابًا", "irab", "noun", [K, TMZ, MSD, IRB], "تَمْيِيزٌ مَنْصُوبٌ — مَعْمُولٌ مِنْ جِهَةِ الْإِعْرَابِ، لَا الْبِنَاءِ.", "«in iʿrāb» — a tamyīz: governed as to iʿrāb, not indeclinable.", "«i'râb bakımından» — temyiz: binâ değil i'râb yönünden ma'mûl.", punct="،"),
  nahw(punct=":"),
  tok("إِنَّ", "inna", "part", [K, IN, ALM, HK], "لَفْظٌ مَحْكِيٌّ: حَرْفُ تَوْكِيدٍ وَنَصْبٍ — الْجُزْءُ الْأَوَّلُ لِلْعَلَمِ.", "«inna» — the name's first part.", "«inne» — alemin birinci cüzü."),
  tok("زَيْدًا", "zayd", "propn", [K, IN, HK], "اسْمُ إِنَّ مَنْصُوبٌ — إِعْرَابٌ مَحْكِيٌّ فِي آخِرِ الْعَلَمِ.", "«Zaydan» — inna's ism; the cited iʿrāb.", "«Zeyden» — inne'nin ismi; hikâye edilen i'râb.", punct="،"),
  tok("وَهَلْ", "hal-istifham", "part", [K, AT, IST, HK], "الْوَاوُ عَاطِفَةٌ، وَهَلْ حَرْفُ اسْتِفْهَامٍ — الْجُزْءُ الْأَوَّلُ.", "«and hal»", "«ve hel»", segments=wa("هَلْ", "hal-istifham", "part")),
  tok("زَيْدٌ", "zayd", "propn", [K, MK, HK], "مُبْتَدَأٌ مَرْفُوعٌ — مَعْمُولُ الْعَامِلِ الْمَعْنَوِيِّ، مَحْكِيٌّ.", "«Zaydun» — the mubtadaʾ of the abstract governor, cited.", "«Zeydün» — ma'nevî âmilin ma'mûlü, hikâye edilmiş.", punct="،"),
  tok("وَمِنْ", "min", "prep", [K, AT, HJ, HK], "الْوَاوُ عَاطِفَةٌ، وَمِنْ حَرْفُ جَرٍّ — الْجُزْءُ الْأَوَّلُ؛ الطَّبْعُ غَيْرُ مَشْكُولٍ، وَالشَّرْحُ يَقْرَأُ مِنْ زَيْدٍ.", "«and min» — the print is unvowelled; the commentary reads min zaydin.", "«ve min» — baskı harekesiz; şerh min zeydin okur.", segments=wa("مِنْ", "min", "prep")),
  tok("زَيْدٍ", "zayd", "propn", [K, HJ, HK], "مَجْرُورٌ بِمِنْ — مَحْكِيٌّ.", "«Zaydin» — cited jarr.", "«Zeydin» — hikâye edilen cer.", punct="،"),
  tok("بِخِلَافِ", "khilaf", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَخِلَافِ مَجْرُورٌ، مُضَافٌ.", "«unlike»", "«aksine»", segments=[seg("بِ", "bi", "prep"), seg("خِلَافِ", "khilaf", "noun")]),
  tok("نَحْوِ", "nahw", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the likes of»", "«gibisinin»"),
  tok("عَبْدِ", "abd", "noun", [K, ID, ALM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — الْجُزْءُ الْأَوَّلُ يُعْرَبُ لَفْظًا.", "«ʿAbd» — the first part takes shown iʿrāb.", "«Abd» — birinci cüz lafzen i'râblanır."),
  tok("اللهِ", "allah", "propn", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْجُزْءُ الثَّانِي مَشْغُولٌ بِالْجَرِّ.", "«Allāh» — the second part busy with its jarr.", "«Allah» — ikinci cüz cerle meşgul."),
  tok("وَنَحْوِ", "nahw", "noun", [K, AT, ID], "الْوَاوُ عَاطِفَةٌ، وَنَحْوِ مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«and of»", "«ve … gibisinin»", segments=wa("نَحْوِ", "nahw", "noun")),
  tok("مَضْرُوبٍ", "madrub", "noun", [K, ID, IMF, ALM], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ عَامِلٌ، جُزْءٌ أَوَّلُ.", "«Maḍrūbin» — a governing participle, the first part.", "«Madrûbin» — âmil ism-i mef'ûl, birinci cüz."),
  tok("غُلَامُهُ", "ghulam", "noun", [K, NF, ID, HK], "نَائِبُ فَاعِلٍ لِمَضْرُوبٍ مَرْفُوعٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَحْكِيٌّ.", "«ghulāmuhu» — the participle's deputy doer, cited.", "«gulâmuhû» — ism-i mef'ûlün nâib-i fâili, hikâye edilmiş.", punct="،", segments=[seg("غُلَامُ", "ghulam", "noun"), pr3ms()]),
  tok("فَإِنَّ", "inna", "part", [K, AT, IN], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«for»", "«çünkü»", segments=fa("إِنَّ", "inna", "part")),
  tok("إِعْرَابَ", "irab", "noun", [K, IN, ID, MSD, IRB], "اسْمُ إِنَّ مَنْصُوبٌ، مُضَافٌ.", "«the iʿrāb of»", "«i'râbı»"),
  tok("الْجُزْءِ", "juz", "noun", [K, ID], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the part»", "«cüzün»"),
  tok("الْأَوَّلِ", "awwal", "noun", [K, NA], "نَعْتٌ مَجْرُورٌ.", "«first»", "«birinci»"),
  tok("مِنْهُمَا", "min", "prep", [K, HJ], "مِنْ حَرْفُ جَرٍّ، وَهُمَا مَجْرُورٌ.", "«of these two»", "«bu ikisinde»", segments=[seg("مِنْ", "min", "prep"), seg("هُمَا", "pron-3d", "pron")]),
  tok("لَفْظِيٌّ", "lafzi", "noun", [K, IN, NSB, IRB], "خَبَرُ إِنَّ مَرْفُوعٌ.", "«is lafẓī»", "«lafzîdir»"),
  tok("بِحَسَبِ", "hasab", "noun", [K, HJ, ID], "الْبَاءُ حَرْفُ جَرٍّ، وَحَسَبِ مَجْرُورٌ، مُضَافٌ.", "«according to»", "«-e göre»", segments=[seg("بِ", "bi", "prep"), seg("حَسَبِ", "hasab", "noun")]),
  tok("الْعَامِلِ", "amil", "noun", [K, ID, IFA, AQ], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the governor»", "«âmil»", punct="،"),
  tok("وَالثَّانِي", "thani", "noun", [K, AT, MK, MQ], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«and the second»", "«ikincisi»", segments=wa("الثَّانِي", "thani", "noun")),
  tok("مَشْغُولٌ", "mashghul", "noun", [K, MK, IMF], "خَبَرٌ مَرْفُوعٌ.", "«is busy»", "«meşguldür»"),
  tok("بِإِعْرَابِهِ", "irab", "noun", [K, HJ, ID, MSD], "الْبَاءُ حَرْفُ جَرٍّ، وَإِعْرَابِ مَجْرُورٌ، مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with its iʿrāb»", "«i'râbıyla»", segments=[seg("بِ", "bi", "prep"), seg("إِعْرَابِ", "irab", "noun"), pr3msi()]),
  tok("بِالْحِكَايَةِ", "hikaya", "noun", [K, HJ, MSD, HK], "الْبَاءُ حَرْفُ جَرٍّ، وَالْحِكَايَةِ مَجْرُورٌ — فَلَا مَحَلَّ لِإِعْرَابٍ آخَرَ.", "«by citation» — so no room for another iʿrāb.", "«hikâye ile» — başka bir i'râba yer yok.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("الْحِكَايَةِ", "hikaya", "noun")]),
 ]})
# ----------- s4 — or a cited indeclinability
S.append({"id": "s4", "translation": {"en": "or a cited indeclinability — as in khamsata ʿashara as a proper name, on the better-known view.", "tr": "ya da hikâye edilen bir binâ — en meşhur görüşe göre alem olan hamsete aşere gibi."},
 "tokens": [
  tok("أَوْ", "aw", "part", [K, AT], "حَرْفُ عَطْفٍ — عَلَى إِعْرَابٌ مَحْكِيٌّ.", "«or»", "«ya da»"),
  tok("بِنَاءٌ", "bina", "noun", [K, AT, MSD, IRB], "مَعْطُوفٌ مَرْفُوعٌ.", "«an indeclinability»", "«bir binâ»"),
  tok("مَحْكِيٌّ", "mahki", "noun", [K, NA, NSB, HK], "نَعْتٌ مَرْفُوعٌ.", "«cited»", "«hikâye edilen»", punct="،"),
  nahw(),
  tok("خَمْسَةَ", "khamsa", "noun", [K, ID, ADD, ALM, HK], "لَفْظٌ مَحْكِيٌّ: الْجُزْءُ الْأَوَّلُ مِنَ الْمُرَكَّبِ الْعَدَدِيِّ، مَبْنِيٌّ عَلَى الْفَتْحِ.", "«khamsata» — the first part of the numeral compound, built on fatḥa.", "«hamsete» — sayı terkibinin birinci cüzü, fetha üzere mebnî."),
  tok("عَشَرَ", "ashar", "noun", [K, ADD, ALM, HK], "الْجُزْءُ الثَّانِي مَبْنِيٌّ عَلَى الْفَتْحِ — وَالْبِنَاءُ مَحْكِيٌّ فِي الْعَلَمِ، وَالْإِعْرَابُ مُقَدَّرٌ.", "«ʿashara» — built on fatḥa; the indeclinability cited in the name, the iʿrāb estimated.", "«aşere» — fetha üzere mebnî; alemde binâ hikâye edilir, i'râb takdîrî."),
  tok("عَلَمًا", "alam-name", "noun", [K, "hal", ALM], "حَالٌ مَنْصُوبٌ — حَالَ كَوْنِهِ عَلَمًا.", "«as a proper name»", "«alem olarak»"),
  tok("عَلَى", "ala", "prep", [K, HJ], "حَرْفُ جَرٍّ.", "«on»", "«göre»"),
  tok("الْأَشْهَرِ", "ashhar", "noun", [K, HJ, "ism-tafdil"], "مَجْرُورٌ بِعَلَى — أَيْ عَلَى الْقَوْلِ الْأَشْهَرِ.", "«the better-known» — view.", "«en meşhur» — görüşe.", punct="."),
 ]})

for s in S:
    for t in s["tokens"]:
        if "grammar" in t and K not in t["grammar"]: t["grammar"].insert(0, K)
        if "grammar" in t: t["grammar"] = list(dict.fromkeys(t["grammar"]))

NEW = {
 "mahki": G("mahki", "مَحْكِيّ", "ح ك ي", "noun", "cited, quoted as it was (of an iʿrāb or form carried into a name)", "hikâye edilen, olduğu gibi aktarılan (bir i'râb ya da şekil)", 4),
 "alamiyya": G("alamiyya", "عَلَمِيَّة", "ع ل م", "noun", "name-hood, the quality of being a proper name", "alemiyet, alem olma", 4),
 "taabbata": G("taabbata", "تَأَبَّطَ", "أ ب ط", "verb", "to put under one's arm (form V) — Taʾabbaṭa Sharran, a poet's name", "koltuğunun altına almak (V. bab) — Teebbeta Şerran, bir şairin adı", 5, form="V"),
 "hijazi": G("hijazi", "حِجَازِيّ", "ح ج ز", "noun", "Ḥijāzī — of the Ḥijāz; the Ḥijāzīs cite the single word", "Hicazlı — Hicaz'a mensup; Hicazlılar müfredi hikâye eder", 4),
 "tamra": G("tamra", "تَمْرَة", "ت م ر", "noun", "a date (fruit); tamratāni, two dates", "bir hurma; temratâni, iki hurma", 2, plural="تَمْر"),
 "mashghul": G("mashghul", "مَشْغُول", "ش غ ل", "noun", "busy, occupied (passive participle of shaghala)", "meşgul (şeğale'nin ism-i mef'ûlü)", 3),
 "ashhar": G("ashhar", "أَشْهَر", "ش ه ر", "noun", "better-known, more famous (elative)", "daha meşhur, en meşhur (ism-i tafdîl)", 3),
 "man-mawsula": G("man-mawsula", "مَنْ (الْمَوْصُولَة)", "م ن", "pron", "who, the one who — the relative man", "kim ki, o kimse ki — mevsûl men", 2),
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
put_morph(mo, "taabbata", {"bab": "بَابُ التَّفَعُّلِ — مَهْمُوزُ الْفَاءِ", "wazn": "تَفَعَّلَ يَتَفَعَّلُ", "masdar": "تَأَبُّط", "ismFail": "مُتَأَبِّط",
 "mazi": ["تَأَبَّطَ", "تَأَبَّطَا", "تَأَبَّطُوا", "تَأَبَّطَتْ", "تَأَبَّطَتَا", "تَأَبَّطْنَ", "تَأَبَّطْتَ", "تَأَبَّطْتُمَا", "تَأَبَّطْتُمْ", "تَأَبَّطْتِ", "تَأَبَّطْتُمَا", "تَأَبَّطْتُنَّ", "تَأَبَّطْتُ", "تَأَبَّطْنَا"],
 "mudari": ["يَتَأَبَّطُ", "يَتَأَبَّطَانِ", "يَتَأَبَّطُونَ", "تَتَأَبَّطُ", "تَتَأَبَّطَانِ", "يَتَأَبَّطْنَ", "تَتَأَبَّطُ", "تَتَأَبَّطَانِ", "تَتَأَبَّطُونَ", "تَتَأَبَّطِينَ", "تَتَأَبَّطَانِ", "تَتَأَبَّطْنَ", "أَتَأَبَّطُ", "نَتَأَبَّطُ"],
 "amr": ["تَأَبَّطْ", "تَأَبَّطَا", "تَأَبَّطُوا", "تَأَبَّطِي", "تَأَبَّطَا", "تَأَبَّطْنَ"], "mansub": "يَتَأَبَّطَ", "majzum": "يَتَأَبَّطْ", "majzum2": "تَتَأَبَّطْ",
 "note": "تَأَبَّطَ الشَّيْءَ يَتَأَبَّطُهُ تَأَبُّطًا: جَعَلَهُ تَحْتَ إِبْطِهِ — مِنْ بَابِ التَّفَعُّلِ، مَهْمُوزُ الْفَاءِ؛ وَبِالْجُمْلَةِ تَأَبَّطَ شَرًّا سُمِّيَ ثَابِتُ بْنُ جَابِرٍ، فَصَارَتْ عَلَمًا إِعْرَابُهُ مُقَدَّرٌ."})
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("izhar ch58 gloss+morph ok", len(GLOSS_ADD), "missing morph:", [k for k in ("adafa", "kana", "jaa", "qala", "daraba", "daa", "taabbata") if k not in mo["verbs"]])

NOTE = {
 "id": K,
 "title": {"ar": "التَّقْدِيرِيُّ فِي الْمُضَافِ إِلَى يَاءِ الْمُتَكَلِّمِ، وَفِيمَا آخِرُهُ إِعْرَابٌ مَحْكِيٌّ: الْجُمْلَةُ الْعَلَمُ، وَمُفْرَدُ الْحِجَازِيِّ، وَالْمُرَكَّبُ الْمَعْمُولُ ثَانِيهِ، وَالْبِنَاءُ الْمَحْكِيُّ", "en": "The taqdīrī in the word annexed to the speaker's yāʾ, and in the word with a cited iʿrāb: the sentence-name, the Ḥijāzī's single word, the compound with a governed second part, and the cited indeclinability", "tr": "Mütekellim yâsına muzâfta ve sonunda hikâye edilen i'râb bulunanda takdîrî: cümle alem, Hicazlının müfredi, ikincisi ma'mûl mürekkep ve hikâye edilen binâ"},
 "level": 5, "group": "awamil",
 "classicalSources": ["إظهار الأسرار للبركوي — الإعراب التقديري: المواضع الثاني والثالث", "الكافية لابن الحاجب — الإعراب التقديري والحكاية", "شرح قطر الندى لابن هشام — الحكاية"],
 "amil": "the second taqdīrī position: what is annexed to the speaker's yāʾ other than the dual — the sound masculine plural estimated in rafʿ only (مُسْلِمِيَّ from مُسْلِمُويَ), anything else in all three states (غُلَامِي، رِجَالِي، مُسْلِمَاتِي). The third: a cited iʿrāb at the end — a sentence become a name (تَأَبَّطَ شَرًّا), the Ḥijāzī's single word (مَنْ زَيْدًا؟ — دَعْنِي مِنْ تَمْرَتَانِ), every compound name whose second part the first governs (إِنَّ زَيْدًا، هَلْ زَيْدٌ، مِنْ زَيْدٍ) — not عَبْدِ اللهِ or مَضْرُوبٍ غُلَامُهُ, whose first part is lafẓī and whose second is busy with its cited iʿrāb — or a cited indeclinability (خَمْسَةَ عَشَرَ as a name).",
 "question": {
  "en": ["Why is the word annexed to the speaker's yāʾ taqdīrī? The yāʾ wants a kasra before it, so the last letter carries that kasra in every state — غُلَامِي in rafʿ, naṣb and jarr alike — and the case is assumed.",
         "Why is the dual excluded, and the sound masculine plural only partly? The dual keeps its alif and yāʾ (غُلَامَايَ، غُلَامَيَّ), so its iʿrāb shows; the sound plural's rafʿ wāw turns to yāʾ (مُسْلِمُويَ → مُسْلِمِيَّ), so only rafʿ is estimated, while naṣb and jarr keep the yāʾ.",
         "What is a cited iʿrāb? An iʿrāb carried over as it was when a word is moved to name-hood or quoted — the end is busy with it, so the new case can only be estimated.",
         "How does a sentence become a name? تَأَبَّطَ شَرًّا, «he put an evil under his arm», named the poet Thābit ibn Jābir; the sentence keeps its own iʿrāb and the name's case is estimated.",
         "What is the Ḥijāzī's citation of a single word? To one who said ضَرَبْتُ زَيْدًا the Ḥijāzī asks مَنْ زَيْدًا؟, keeping the naṣb; to one who said إِلَيَّ تَمْرَتَانِ he answers دَعْنِي مِنْ تَمْرَتَانِ, keeping the rafʿ — the Ottoman commentary quotes the exchange as أَلَكَ تَمْرَتَانِ / دَعْنِي عَنْ تَمْرَتَانِ.",
         "Which compound names are taqdīrī, and which not? Those whose second part is governed by the first (إِنَّ زَيْدًا، هَلْ زَيْدٌ، مِنْ زَيْدٍ — the commentary's reading of the unvowelled print) are taqdīrī; عَبْدُ اللهِ and مَضْرُوبٌ غُلَامُهُ are not, since their first part is declined by the outer governor and only the second is busy by citation.",
         "What is a cited indeclinability? خَمْسَةَ عَشَرَ made a name on the better-known view — its two fatḥas are the numeral's indeclinability carried over, and the case is estimated.",
         "What does the engine READ here? The DabtEngine reads مُسْلِمِيَّ and غُلَامِي as annexed to the speaker's yāʾ with estimated case, the cited sentence and words at their quoted forms, the three particle-compounds as the particle plus its own governed word, عَبْدِ اللهِ and مَضْرُوبٍ غُلَامُهُ by the outer jarr, and خَمْسَةَ عَشَرَ built on fatḥa."],
  "tr": ["Mütekellim yâsına muzâf olan neden takdîrîdir? Yâ önünde kesre ister; son harf her hâlde o kesreyi taşır — gulâmî ref', nasb ve cerde aynı — ve i'râb varsayılır.",
         "Tesniye neden hariç, cem'-i müzekker-i sâlim neden kısmen? Tesniye elif ve yâsını korur (gulâmâye, gulâmeyye), i'râbı görünür; sâlim ceminin ref' vâvı yâ'ya döner (müslimûye → müslimiyye), yalnız ref' takdîrîdir; nasb ve cer yâ'yı korur.",
         "Hikâye edilen i'râb nedir? Bir söz alemliğe nakledilince ya da aktarılınca olduğu gibi taşınan i'râb — son onunla meşguldür, yeni i'râb ancak takdir edilir.",
         "Cümle nasıl alem olur? Teebbeta şerran, «bir kötülüğü koltuğuna aldı», şair Sâbit b. Câbir'in adı oldu; cümle kendi i'râbını korur, alemin i'râbı takdîrîdir.",
         "Hicazlının müfredi hikâyesi nedir? Darabtü Zeyden diyene Hicazlı men Zeyden? diye sorar, nasbı koruyarak; ileyye temratâni diyene da'nî min temratâni diye cevap verir, ref'i koruyarak — Osmanlı şerhi konuşmayı eleke temratâni / da'nî an temratâni diye aktarır.",
         "Hangi mürekkep alemler takdîrîdir, hangileri değil? İkinci cüzü birincinin ma'mûlü olanlar (inne Zeyden, hel Zeydün, min Zeydin — harekesiz baskının şerhteki okunuşu) takdîrîdir; Abdullah ve Madrûbun gulâmuhû değildir, çünkü birinci cüzleri dış âmille i'râblanır, yalnız ikincisi hikâye ile meşguldür.",
         "Hikâye edilen binâ nedir? En meşhur görüşe göre alem yapılan hamsete aşere — iki fethası sayının taşınan binâsıdır, i'râb takdîrîdir.",
         "Motor burada neyi OKUR? DabtEngine müslimiyye ve gulâmî'yi takdîrî i'râblı mütekellim yâsı muzâfı, hikâye edilen cümle ve kelimeleri aktarılan şekilleriyle, üç harf terkibini harf artı kendi ma'mûlü, Abdillâhi ve madrûbin gulâmuhû'yu dış cerle, hamsete aşere'yi fetha üzere mebnî okur."],
 },
 "plain": {"en": "Two more places where the case vowel is only assumed: a noun with «my» attached (ghulām-ī looks the same in every case), and a word whose ending froze when it became a name or a quotation — Taʾabbaṭa Sharran, Inna Zaydan, or «khamsata ʿashara» as a name. ʿAbd Allāh differs: its first word still shows its case.",
           "tr": "İ'râb harekesinin yalnız varsayıldığı iki yer daha: «-im» eklenmiş isim (gulâm-î «kölem» her hâlde aynı görünür) ve alem ya da alıntı olurken sonu donmuş söz — Teebbeta Şerran, İnne Zeyden ya da ad olarak kullanılan «hamsete aşere». Abdullah farklıdır: ilk sözcüğü i'râbını hâlâ gösterir."},
 "explanation": {"en": "The second taqdīrī position is what is annexed to the speaker's yāʾ, other than the dual: if it is the sound masculine plural, its rafʿ alone is taqdīrī — جَاءَنِي مُسْلِمِيَّ, whose origin is مُسْلِمُويَ; if anything else, the whole is taqdīrī — غُلَامِي، رِجَالِي، مُسْلِمَاتِي. The third is what carries a cited iʿrāb at its end: either a sentence moved to name-hood — تَأَبَّطَ شَرًّا; or a single word in the Ḥijāzī's speech — مَنْ زَيْدًا؟ to one who said ضَرَبْتُ زَيْدًا, and دَعْنِي مِنْ تَمْرَتَانِ to one who said إِلَيَّ تَمْرَتَانِ (the Ottoman commentary quotes أَلَكَ تَمْرَتَانِ and دَعْنِي عَنْ تَمْرَتَانِ; the text keeps the lithograph); and likewise every compound name whose second part the first governs in iʿrāb — إِنَّ زَيْدًا، هَلْ زَيْدٌ، مِنْ زَيْدٍ, the last read with the commentary where the print is unvowelled — unlike عَبْدُ اللهِ and مَضْرُوبٌ غُلَامُهُ, whose first part is lafẓī according to the governor while the second is busy with its iʿrāb by citation; or a cited indeclinability — خَمْسَةَ عَشَرَ as a name, on the better-known view. The fourth to seventh positions follow.",
                 "tr": "Takdîrînin ikinci mevzii, tesniye dışında mütekellim yâsına muzâf olandır: cem'-i müzekker-i sâlim ise yalnız ref'i takdîrîdir — câenî müslimiyye, aslı müslimûye; başkası ise hepsi takdîrîdir — gulâmî, ricâlî, müslimâtî. Üçüncüsü sonunda hikâye edilen i'râb bulunandır: ya alemliğe nakledilmiş bir cümle — teebbeta şerran; ya Hicazlının sözünde bir müfred — darabtü Zeyden diyene men Zeyden?, ileyye temratâni diyene da'nî min temratâni (Osmanlı şerhi eleke temratâni ve da'nî an temratâni diye aktarır; metin litografiyi korur); ikinci cüzü birincinin i'râb bakımından ma'mûlü olan her mürekkep alem de böyledir — inne Zeyden, hel Zeydün, min Zeydin, sonuncusu baskı harekesiz olduğundan şerhle okunur — Abdullah ve madrûbun gulâmuhû'nun aksine, ki bunlarda birinci cüz âmile göre lafzî, ikincisi hikâye ile i'râbıyla meşguldür; ya da hikâye edilen bir binâ — en meşhur görüşe göre alem olan hamsete aşere. Dördüncüden yedinciye mevziler gelir."},
 "examples": [
  {"ar": "جَاءَنِي مُسْلِمِيَّ، أَصْلُهُ مُسْلِمُويَ", "en": "the sound plural annexed to the speaker's yāʾ", "tr": "mütekellim yâsına muzâf sâlim cemi", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "نَحْوُ غُلَامِي وَرِجَالِي وَمُسْلِمَاتِي", "en": "the rest annexed to the yāʾ: all estimated", "tr": "yâ'ya muzâf diğerleri: hepsi takdîrî", "sourceStory": "izhar-al-asrar", "sentence": "s1"},
  {"ar": "نَحْوُ تَأَبَّطَ شَرًّا", "en": "the sentence become a name", "tr": "alem olan cümle", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "مَنْ زَيْدًا؟ لِمَنْ قَالَ: ضَرَبْتُ زَيْدًا", "en": "the Ḥijāzī's cited single word", "tr": "Hicazlının hikâye ettiği müfred", "sourceStory": "izhar-al-asrar", "sentence": "s2"},
  {"ar": "إِنَّ زَيْدًا، وَهَلْ زَيْدٌ، وَمِنْ زَيْدٍ، بِخِلَافِ عَبْدِ اللهِ", "en": "the compound names governed within, and the exception", "tr": "içten ma'mûl mürekkep alemler ve istisnâ", "sourceStory": "izhar-al-asrar", "sentence": "s3"},
  {"ar": "خَمْسَةَ عَشَرَ عَلَمًا عَلَى الْأَشْهَرِ", "en": "the cited indeclinability", "tr": "hikâye edilen binâ", "sourceStory": "izhar-al-asrar", "sentence": "s4"},
 ],
 "commonMistakes": [
  {"wrong": "جَاءَنِي مُسْلِمُويَ", "right": "جَاءَنِي مُسْلِمِيَّ", "why": {"en": "the rafʿ wāw before the speaker's yāʾ turns to yāʾ and assimilates; the rafʿ is estimated", "tr": "mütekellim yâsı önündeki ref' vâvı yâ'ya dönüp idğam olur; ref' takdîrîdir"}},
  {"wrong": "جَاءَنِي غُلَامَيَّ (for the singular)", "right": "جَاءَنِي غُلَامِي", "why": {"en": "only the dual keeps its letters before the yāʾ; the singular takes the kasra of fit", "tr": "yalnız tesniye yâ önünde harflerini korur; müfred münasebet kesresi alır"}},
  {"wrong": "جَاءَنِي تَأَبَّطُ شَرًّا", "right": "جَاءَنِي تَأَبَّطَ شَرًّا", "why": {"en": "the sentence-name keeps its cited form; the rafʿ is estimated, never shown", "tr": "cümle alem hikâye edilen şeklini korur; ref' takdîrîdir, gösterilmez"}},
  {"wrong": "مَرَرْتُ بِعَبْدُ اللهِ", "right": "مَرَرْتُ بِعَبْدِ اللهِ", "why": {"en": "in ʿAbd Allāh the first part is declined by the outer governor", "tr": "Abdullah'ta birinci cüz dış âmille i'râblanır"}},
 ],
}
ADD_EN = (" Chapter 58 (print p. 153): the second taqdīrī position — the word annexed to the speaker's yāʾ, the sound plural in rafʿ only and the rest throughout (s1); the third — the cited iʿrāb: the sentence-name and the Ḥijāzī's single word (s2), the compound name governed within against ʿAbd Allāh (s3), the cited indeclinability khamsata ʿashara (s4).")
ADD_TR = (" Elli sekizinci bab (baskı s. 153): takdîrînin ikinci mevzii — mütekellim yâsına muzâf olan, sâlim cemi yalnız ref'te, diğerleri her hâlde (s1); üçüncüsü — hikâye edilen i'râb: cümle alem ve Hicazlının müfredi (s2), Abdullah'a karşı içten ma'mûl mürekkep alem (s3), hikâye edilen binâ hamsete aşere (s4).")
write_out(58, S, TITLE, ADD_EN, ADD_TR, "p. 153", GLOSS_ADD, notes=(NOTE,),
          related=((K57, [K]), (YM, [K]), (HK, [K]), (ALM, [K]), (JDS, [K]), (IRB, [K])))
report(58, S, GLOSS_ADD, (NOTE,))
