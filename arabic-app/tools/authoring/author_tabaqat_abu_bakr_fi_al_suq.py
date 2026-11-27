"""Author content/samples/tabaqat-abu-bakr-fi-al-suq — «فَمِنْ أَيْنَ أُطْعِمُ عِيَالِي؟», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Companions, Abū Bakr's entry, vol. 3 p. 137 (Shamela p. 815):
ʿAṭāʾ ibn al-Sāʾib's khabar whole, isnād included — «قال: أخبرنا مسلم بن إبراهيم» … «ما يختصم إلي فيه اثنان.» — in two chapters cut at
the turn of the dialogue («فمن أين أطعم عيالي؟»).
The exact passage: research/sources/tabaqat-abu-bakr-fi-al-suq-src.txt. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_tabaqat_abu_bakr_fi_al_suq.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-abu-bakr-fi-al-suq"
AB = ("أَبِي بَكْرٍ", "Abū Bakr", "Ebû Bekir")
UM = ("عُمَرَ", "ʿUmar", "Ömer")
TWO = ("عُمَرَ وَأَبِي عُبَيْدَةَ", "ʿUmar and Abū ʿUbayda", "Ömer ile Ebû Ubeyde")
QALA_TWO = lambda p=":", pre=(): VERB(("فَ" if pre == ("fa",) else "") + "قَالَا", "qala", "mA", g=["hollow-verbs"], note=("، يَعُودُ عَلَى " + TWO[0], " (" + TWO[1] + ")", " (" + TWO[2] + ")"), cl=QALA_W, p=p, pre=pre)
TITLES = [{"ar": "أَيْنَ تُرِيدُ يَا خَلِيفَةَ رَسُولِ اللهِ؟", "en": "Where are you going, caliph?", "tr": "Nereye, ey Resûlullah'ın halifesi?"},
          {"ar": "شَطْرُ شَاةٍ", "en": "Half a sheep", "tr": "Yarım koyun"}]
S1 = [
 SEN(1, "He said: Muslim ibn Ibrāhīm told us; he said: Hishām al-Dastuwāʾī told us; he said: ʿAṭāʾ ibn al-Sāʾib told us; he said:",
     "Dedi ki: Bize Müslim b. İbrâhim haber verdi; dedi ki: Bize Hişâm ed-Destuvâî haber verdi; dedi ki: Bize Atâ b. es-Sâib haber verdi; dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("مُسْلِمُ", "muslim-name", "fail", note=NT), BN("raf", ("مُسْلِمُ", "Muslim", "Müslim")), NAME("إِبْرَاهِيمَ", "ibrahim", "mi", dipt="ujma"),
  QALA_HID(("مُسْلِمِ بْنِ إِبْرَاهِيمَ", "Muslim ibn Ibrāhīm", "Müslim b. İbrâhim")), ISNAD_AKHBARANA(), NAME("هِشَامٌ", "hisham", "fail"),
  NOUN("الدَّسْتُوَائِيُّ", "dastuwai", "naat", "raf", of=("هِشَامٌ", "Hishām", "Hişâm"), note=(" — نِسْبَةٌ إِلَى دَسْتُوَاءَ", " — a nisba to Dastuwāʾ", " — Destuvâ'ya nisbet")),
  QALA_HID(("هِشَامٍ", "Hishām", "Hişâm")), ISNAD_AKHBARANA(), NAME("عَطَاءُ", "ata-name", "fail", note=NT), BN("raf", ("عَطَاءُ", "ʿAṭāʾ", "Atâ")), NAME("السَّائِبِ", "saib-name", "mi"),
  QALA_HID(("عَطَاءِ بْنِ السَّائِبِ", "ʿAṭāʾ ibn al-Sāʾib", "Atâ b. es-Sâib"))]),
 SEN(2, "When Abū Bakr was made caliph, he set out in the morning for the market with garments on his neck to trade in;",
     "Ebû Bekir halife yapıldığında, sabah erkenden boynunda ticaretini yaptığı elbiselerle çarşıya gitti;",
 [PART("لَمَّا", "lamma", "ظَرْفٌ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِجَوَابِهِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
       "An adverb meaning «when», built on sukūn in the seat of nasb, hanging on its answer, annexed to the clause after it.", "«-ınca» anlamında zarf, mahallen mansûb; cevabına müteallik, sonraki cümleye muzâf.", ["maful-fih"]),
  VERB("اسْتُخْلِفَ", "istakhlafa", "p", form="form-x-verbs", g=["al-majhul-fil-kafiya"], doer_after=True, cl=LAMMA_SHART),
  NOUN("أَبُو", "ab", "naib", sign="5", mudaf=True), NAME("بَكْرٍ", "bakr", "mi"),
  VERB("أَصْبَحَ", "asbaha", "m", form="kana-wa-akhawatuha", g=["form-iv-verbs"], hid="هُوَ", ref=AB, note=(" — مِنْ أَخَوَاتِ كَانَ، وَاسْمُهُ مُسْتَتِرٌ", " — a sister of kāna; its noun is hidden", " — kâne'nin kardeşi; ismi gizli"), cl=JAWAB_LAMMA),
  NOUN("غَادِيًا", "lb-ghadin", "khk", note=(" — اسْمُ فَاعِلٍ مِنْ «غَدَا»: ذَاهِبًا أَوَّلَ النَّهَارِ", " — active participle of غَدَا: going early in the day", " — «gadâ»dan ism-i fâil: sabah erkenden giden"), g=["ism-fail"]),
  PREPT("إِلَى", "ila", H("بِـ«غَادِيًا»", "«going»", "«gâdiyen»e")), NOUN("السُّوقِ", "suq", "majr"),
  PREPT("وَعَلَى", "ala", H("بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ — وَالْجُمْلَةُ حَالٌ", "an omitted, fronted khabar — the clause is a ḥāl", "öne alınmış mahzûf habere — cümle hâl"), ("، وَالْوَاوُ حَالِيَّةٌ", ", with the waw of the ḥāl", "; vâv hâliyye")),
  NOUN("رَقَبَتِهِ", "raqaba", "majr", enc="هِ", ref=AB),
  NOUN("أَثْوَابٌ", "thawb", "mubtm", note=(" — جَمْعُ ثَوْبٍ", " — plural of ثَوْب", " — sevb'in çoğulu")),
  VERB("يَتَّجِرُ", "ittajara", "u", form="form-viii-verbs", hid="هُوَ", ref=AB, cl=(" — وَالْجُمْلَةُ نَعْتٌ لِـ«أَثْوَابٌ» فِي مَحَلِّ رَفْعٍ", "; the clause describes «garments», in the seat of raf'", "; cümle «esvâb»ın na'tı, mahallen merfû")),
  PRON_J("بِهَا", "bi", "هَا", H("بِـ«يَتَّجِرُ»", "«trade»", "«yettecir»e"), ref=("الْأَثْوَابِ", "the garments", "elbiseler"), p="؛")]),
 SEN(3, "ʿUmar ibn al-Khaṭṭāb and Abū ʿUbayda ibn al-Jarrāḥ met him and said to him: Where are you going, O caliph of the Messenger of God?",
     "Ömer b. el-Hattâb ile Ebû Ubeyde b. el-Cerrâh onu karşıladılar ve ona: Nereye gidiyorsun, ey Resûlullah'ın halifesi? dediler.",
 [VERB("فَلَقِيَهُ", "laqiya", "m", g=["naqis-verbs"], enc="هُ", encref=AB, doer_after=True, pre=("fa",)),
  NAME("عُمَرُ", "umar", "fail", note=NT), BN("raf", ("عُمَرُ", "ʿUmar", "Ömer")), NAME("الْخَطَّابِ", "khattab", "mi"),
  NOUN("وَأَبُو", "ab", "atf", "raf", sign="5", mudaf=True, pre=("wa",)), NAME("عُبَيْدَةَ", "ubayda", "mi", dipt="tanith"), BN("raf", ("أَبُو عُبَيْدَةَ", "Abū ʿUbayda", "Ebû Ubeyde")), NAME("الْجَرَّاحِ", "jarrah", "mi"),
  QALA_TWO(p=None, pre=("fa",)), PRON_J("لَهُ", "li", "هُ", H("بِـ«قَالَا»", "«said»", "«kâlâ»ya"), ref=AB, p=":"),
  PART("أَيْنَ", "ayna", "اسْمُ اسْتِفْهَامٍ عَنِ الْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِـ«تُرِيدُ».", "A question noun «where», built on fatḥa, the fronted object of «want».", "Mekân soran soru ismi «eyne», fetha üzere mebnî, «turîdu»nun öne alınmış mef'ûlü.", ["al-istifham"], pos="pron"),
  VERB("تُرِيدُ", "arada", "u", form="form-iv-verbs", g=["hollow-verbs"], hid="أَنْتَ", ref=AB), YA(),
  NOUN("خَلِيفَةَ", "khalifa", "munada", mudaf=True, note=(" — مُنَادًى مُضَافٌ", " — a called noun that is annexed", " — muzâf münâdâ")), *RASUL("mi", salla=False, p="؟")]),
 SEN(4, "He said: The market.",
     "Dedi ki: Çarşıya.",
 [QALA_HID(AB), NOUN("السُّوقَ", "suq", "maful", note=(" — لِفِعْلٍ مَحْذُوفٍ دَلَّ عَلَيْهِ السُّؤَالُ: أُرِيدُ السُّوقَ", " — of a verb left out, shown by the question: «I want the market»", " — sorunun delâlet ettiği mahzûf fiilin: «çarşıyı istiyorum»"), g=["hadhf-wa-taqdir"], p=".")]),
 SEN(5, "They said: Doing what — when you have taken charge of the Muslims' affairs?",
     "Dediler ki: Ne yapacaksın, hâlbuki Müslümanların işini üstlendin?",
 [QALA_TWO(),
  VERB("تَصْنَعُ", "sanaa", "u", hid="أَنْتَ", ref=AB),
  PART("مَاذَا", "madha", "اسْمُ اسْتِفْهَامٍ مُرَكَّبٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«تَصْنَعُ»، وَأُخِّرَ عَنْهُ عَلَى غَيْرِ الْغَالِبِ.", "A compound question noun «what», the object of «do», placed after it, as is less usual.",
       "Mürekkep soru ismi «mâzâ», «tasna'u»nun mef'ûlü, mahallen mansûb; alışılmışın aksine ondan sonra geldi.", ["al-istifham"], pos="pron"),
  PART("وَقَدْ", "qad", "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The waw of the ḥāl; قَدْ of assurance.", "Hâl vâvı; «kad» tahkîk harfi.", ["qad-harf", "al-hal-jumla-wa-rabituha"], pre=("wa",)),
  VERB("وَلِيتَ", "waliya", "mta", g=["mithal-verbs", "naqis-verbs", "lafif-verbs"], cl=HALCL),
  NOUN("أَمْرَ", "amr", "maful", mudaf=True), NOUN("الْمُسْلِمِينَ", "muslim", "mi", sign="smp", p="؟")]),
 SEN(6, "He said: Then where am I to feed my household from?",
     "Dedi ki: Peki ailemi nereden doyuracağım?",
 [QALA_HID(AB),
  PART("فَمِنْ", "min", "الْفَاءُ عَاطِفَةٌ عَلَى كَلَامٍ مُقَدَّرٍ، وَمِنْ حَرْفُ جَرٍّ.", "The fa follows on from something understood; مِنْ «from», a jarr letter.", "Fâ takdir edilen bir söze atfeder; «min» cer harfi.", ["huruf-jarr"], pre=("fa",), pos="prep"),
  PART("أَيْنَ", "ayna", "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ بِـ«مِنْ» — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أُطْعِمُ».", "A question noun «where», in the seat of jarr after «from» — the phrase hangs on «feed».", "Soru ismi «eyne», «min» ile mahallen mecrûr — câr-mecrûr «ut'imu»ya müteallik.", ["al-istifham"], pos="pron"),
  VERB("أُطْعِمُ", "atama", "u", form="form-iv-verbs", hid="أَنَا", ref=AB),
  NOUN("عِيَالِي", "iyal", "maful", sign="ya", enc="ي", p="؟")]),
]
S2 = [
 SEN(7, "They said to him: Come along, so that we may fix something for you.",
     "Ona dediler ki: Gel, sana bir şey takdir edelim.",
 [QALA_TWO(p=None), PRON_J("لَهُ", "li", "هُ", H("بِـ«قَالَا»", "«said»", "«kâlâ»ya"), ref=AB, p=":"),
  VERB("انْطَلِقْ", "intalaqa", "amr", form="form-vii-verbs"),
  PART("حَتَّى", "hatta", "حَرْفُ غَايَةٍ وَتَعْلِيلٍ وَجَرٍّ، وَبَعْدَهُ «أَنْ» مُضْمَرَةٌ تَنْصِبُ الْمُضَارِعَ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِـ«حَتَّى».", "حَتَّى «so that», a jarr letter with أَنْ understood after it, putting the verb in nasb.", "«Hattâ» gâye ve ta'lîl için cer harfi; ardından gizli «en» muzâriyi nasbeder.", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari"], pos="prep"),
  VERB("نَفْرِضَ", "farada", "us", hid="نَحْنُ", note=(" — مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ «حَتَّى»", " — in nasb by أَنْ understood after حَتَّى", " — «hattâ»dan sonra gizli «en» ile mansûb")),
  PRON_J("لَكَ", "li", "كَ", H("بِـ«نَفْرِضَ»", "«fix»", "«nefride»ye"), ref=AB), NOUN("شَيْئًا", "shay", "maful", p=".")]),
 SEN(8, "So he went along with them, and they fixed for him every day half a sheep, and they bargained with him over the head and the belly.",
     "O da onlarla birlikte gitti; ona her gün için yarım koyun takdir ettiler ve baş ile işkembe konusunda onunla pazarlık ettiler.",
 [VERB("فَانْطَلَقَ", "intalaqa", "m", form="form-vii-verbs", hid="هُوَ", ref=AB, pre=("fa",)),
  NOUN("مَعَهُمَا", "maa", "zarf", enc="هُمَا", ref=TWO, note=(" — ظَرْفُ مَكَانٍ مُتَعَلِّقٌ بِـ«انْطَلَقَ»", " — an adverb of company, hanging on «went»", " — zarf, «intalaka»ya müteallik")),
  VERB("فَفَرَضُوا", "farada", "mw", pre=("fa",)), PRON_J("لَهُ", "li", "هُ", H("بِـ«فَرَضُوا»", "«fixed»", "«faradû»ya"), ref=AB),
  NOUN("كُلَّ", "kull", "zarf", mudaf=True, note=(" — نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ لِإِضَافَتِهِ إِلَيْهِ", " — standing for an adverb of time, being annexed to one", " — zamana muzâf olduğu için zaman zarfının nâibi")),
  NOUN("يَوْمٍ", "yawm", "mi"), NOUN("شَطْرَ", "shatr", "maful", mudaf=True, note=(" — وَالشَّطْرُ: النِّصْفُ", " — shaṭr: a half", " — şatr: yarım")), NOUN("شَاةٍ", "shat", "mi"),
  VERB("وَمَاكَسُوهُ", "maakasa", "mw", form="form-iii-verbs", enc="هُ", encref=AB, pre=("wa",), note=(" — الْمُمَاكَسَةُ: الْمُشَاحَّةُ فِي الثَّمَنِ وَطَلَبُ النَّقْصِ مِنْهُ", " — mumākasa: haggling, pressing a price down", " — mümâkese: fiyatta çekişme, indirim isteme")),
  PREPT("فِي", "fi", H("بِـ«مَاكَسُوا»", "«bargained»", "«mâkesû»ya")), NOUN("الرَّأْسِ", "ras", "majr"), NOUN("وَالْبَطْنِ", "batn", "atf", "jarr", pre=("wa",), p=".")]),
 SEN(9, "ʿUmar said: To the judging.",
     "Ömer: Kadılığa (bana) dedi.",
 [QALA_AFTER(pre=("fa",)), NAME("عُمَرُ", "umar", "fail", dipt="adl", p=":"),
  PREPT("إِلَى", "ila", H("بِمَحْذُوفٍ تَقْدِيرُهُ: إِلَيَّ الْقَضَاءُ أَوْ أَنْصَرِفُ إِلَى الْقَضَاءِ", "an understood «to me belongs» or «I turn to»", "takdir edilen «bana aittir» ya da «yönelirim»e")),
  NOUN("الْقَضَاءِ", "qada", "majr", p=".")]),
 SEN(10, "And Abū ʿUbayda said: And to the fayʾ.",
     "Ebû Ubeyde de: Fey'e de (ben) dedi.",
 [QALA_AFTER(pre=("wa",)), NOUN("أَبُو", "ab", "fail", sign="5", mudaf=True), NAME("عُبَيْدَةَ", "ubayda", "mi", dipt="tanith", p=":"),
  PREPT("وَإِلَى", "ila", H("بِمِثْلِ مَا تَعَلَّقَ بِهِ الْأَوَّلُ", "the same understood verb", "birincinin müteallikine"), ("، وَالْوَاوُ عَاطِفَةٌ", ", with the conjoining waw", "; vâv atıf")),
  NOUN("الْفَيْءِ", "fay", "majr", note=(" — الْفَيْءُ: مَا صَارَ لِلْمُسْلِمِينَ مِنْ أَمْوَالِ الْعَدُوِّ بِغَيْرِ قِتَالٍ", " — fayʾ: wealth that comes to the Muslims from the enemy without fighting", " — fey': düşmandan savaşsız Müslümanlara geçen mal"), p=".")]),
 SEN(11, "ʿUmar said: And indeed a month would pass over me in which no two came to me with a dispute.",
     "Ömer dedi ki: Andolsun, üzerimden bir ay geçerdi de iki kişi bile bana dava için gelmezdi.",
 [QALA_AFTER(), NAME("عُمَرُ", "umar", "fail", dipt="adl", p=":"),
  PART("فَلَقَدْ", "qad", "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The fa resumes; the lam answers an understood oath; قَدْ of assurance.", "Fâ isti'nâf; lâm takdir edilen kasemin cevabında; «kad» tahkîk harfi.", ["qad-harf", "huruf-al-qasam-fil-kafiya"],
       pre=(), s=None),
  VERB("كَانَ", "kana", "m", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ، وَاسْمُهُ ضَمِيرُ الشَّأْنِ مُسْتَتِرٌ", " — defective; its noun is the hidden pronoun of the matter", " — nâkıs; ismi gizli şan zamiri")),
  VERB("يَأْتِي", "ata", "uy", g=["mahmuz-verbs", "naqis-verbs"], doer_after=True, cl=KH_KANA),
  PRON_J("عَلَيَّ", "ala", "يَّ", H("بِـ«يَأْتِي»", "«pass»", "«ye'tî»ye"), ref=UM),
  NOUN("الشَّهْرُ", "shahr", "fail"),
  PART("مَا", "ma-nafiya", "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "مَا negates.", "«Mâ» nefy harfi.", ["anwa-ma"]),
  VERB("يَخْتَصِمُ", "ikhtasama", "u", form="form-viii-verbs", doer_after=True, cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الشَّهْرُ»", "; the clause is a ḥāl of «the month»", "; cümle «eş-şehr»den hâl")),
  PRON_J("إِلَيَّ", "ila", "يَّ", H("بِـ«يَخْتَصِمُ»", "«dispute»", "«yahtasımu»ya"), ref=UM),
  PRON_J("فِيهِ", "fi", "هِ", H("بِـ«يَخْتَصِمُ»", "«dispute»", "«yahtasımu»ya"), ref=("الشَّهْرِ", "the month", "ay")),
  NOUN("اثْنَانِ", "ithnan", "fail", sign="du", p=".")]),
]
CHAPS = [S1, S2]
NEW_GLOSS = {
 "muslim-name": NP("مُسْلِم", "Muslim — a man's name (here Muslim ibn Ibrāhīm al-Farāhīdī)", "Müslim — erkek adı (burada Müslim b. İbrâhim el-Ferâhîdî)"),
 "dastuwai": NN("دَسْتُوَائِيّ", "د س ت و", "al-Dastuwāʾī (a nisba)", "ed-Destuvâî (nisbe)"),
 "istakhlafa": NV("اسْتَخْلَفَ", "خ ل ف", "X", "to appoint as successor (passive: to be made caliph)", "halef tayin etmek (meçhul: halife yapılmak)"),
 "maakasa": NV("مَاكَسَ", "م ك س", "III", "to haggle with, to beat down a price", "pazarlık etmek, fiyat kırmak"),
 "fay": NN("فَيْء", "ف ي أ", "fayʾ — wealth taken from the enemy without fighting", "fey' — düşmandan savaşsız alınan mal"),
}
GLOSS_HERE = {"raqaba": ("neck", "boyun"), "shat": ("a sheep", "koyun"), "ubayda": ("ʿUbayda — in the kunya Abū ʿUbayda (ibn al-Jarrāḥ)", "Ubeyde — Ebû Ubeyde (b. el-Cerrâh) künyesinde")}
V_NEW = {"istakhlafa": SG.derived(SG.B10, SG.W10, "َ", "اِسْتَخْلَف", "سْتَخْلِف", "اِسْتَخْلِف", "اِسْتِخْلَاف", "مُسْتَخْلِف", "مُسْتَخْلَف", "اُسْتُخْلِفَ", "يُسْتَخْلَفُ", "اسْتَخْلَفَهُ يَسْتَخْلِفُهُ: جَعَلَهُ خَلِيفَةً."),
         "maakasa": SG.derived(SG.B3, SG.W3, "ُ", "مَاكَس", "مَاكِس", "مَاكِس", "مُمَاكَسَة", "مُمَاكِس", "مُمَاكَس", "مُوكِسَ", "يُمَاكَسُ", "مَاكَسَهُ يُمَاكِسُهُ مُمَاكَسَةً: شَاحَّهُ فِي الثَّمَنِ.")}
MANIFEST = manifest(SLUG, 4, {"ar": "فَمِنْ أَيْنَ أُطْعِمُ عِيَالِي؟", "en": "Then Where Am I to Feed My Household From?", "tr": "Peki Ailemi Nereden Doyuracağım?"},
  {"ar": "الْخَلِيفَةُ يَغْدُو إِلَى السُّوقِ", "en": "The caliph sets out for the market", "tr": "Halife çarşıya gider"}, "sahaba",
  "Abū Bakr's entry, vol. 3, printed p. 137 (Shamela p. 815)", "Ebû Bekir maddesi, cilt 3, matbû s. 137 (Şâmile s. 815)", "تَرْجَمَةُ أَبِي بَكْرٍ، الْجُزْءُ ٣، ص ١٣٧ (الشَّامِلَةُ ص ٨١٥)",
  "ʿAṭāʾ ibn al-Sāʾib's khabar whole, isnād included, from «قال: أخبرنا مسلم بن إبراهيم» to «ما يختصم إلي فيه اثنان.», in two chapters cut at «فمن أين أطعم عيالي؟»",
  "Atâ b. es-Sâib'in haberi, isnadıyla tam, «قال: أخبرنا مسلم بن إبراهيم»den «ما يختصم إلي فيه اثنان.»a kadar; «فمن أين أطعم عيالي؟»de ikiye bölündü",
  "خَبَرُ عَطَاءِ بْنِ السَّائِبِ كُلُّهُ بِإِسْنَادِهِ، فِي فَصْلَيْنِ",
  hoca=[("«وَلِيتَ» read active (or the passive وُلِّيتَ «you were put in charge»)", "«وَلِيتَ» malûm okundu (ya da meçhul وُلِّيتَ «başa getirildin»)"),
        ("«يَأْتِي عَلَيَّ الشَّهْرُ» — the e-text «على الشهر» read عَلَيَّ «upon me»; كَانَ with the pronoun of the matter", "«يَأْتِي عَلَيَّ الشَّهْرُ» — e-metindeki «على الشهر» عَلَيَّ «üzerime» okundu; «kâne» şan zamiriyle"),
        ("«السُّوقَ» in nasb as the answer to «أَيْنَ تُرِيدُ»", "«السُّوقَ» «eyne turîdu»ya cevap olarak mansûb"),
        ("«إِلَى الْقَضَاءِ / وَإِلَى الْفَيْءِ»: what the phrases hang on is understood", "«إِلَى الْقَضَاءِ / وَإِلَى الْفَيْءِ»: müteallik takdir edildi")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V_NEW)
