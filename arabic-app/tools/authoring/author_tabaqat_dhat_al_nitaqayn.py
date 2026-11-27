"""Author content/samples/tabaqat-dhat-al-nitaqayn — «ذَاتُ النِّطَاقَيْنِ», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the women's volume, Asmāʾ bint Abī Bakr's entry, vol. 8 pp. 196–197
(Shamela pp. 2863–2864): two consecutive akhbār of Hishām ibn ʿUrwa, each whole with its isnād — Asmāʾ's own («أخبرنا أبو أسامة حماد بن
أسامة.» … «فلذلك سميت ذات النطاقين.») and ʿUrwa's («أخبرنا أبو أسامة. حدثنا هشام بن عروة عن أبيه أن أهل الشام» … «فهو والله حق.»), one
chapter each. Ibn al-Zubayr answers with a half-line of Abū Dhuʾayb al-Hudhalī.
The exact passage: research/sources/tabaqat-dhat-al-nitaqayn-src.txt. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_tabaqat_dhat_al_nitaqayn.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-dhat-al-nitaqayn"
AS = ("أَسْمَاءَ", "Asmāʾ", "Esmâ")
AB = ("أَبِي بَكْرٍ", "Abū Bakr", "Ebû Bekir")
IZ = ("ابْنِ الزُّبَيْرِ", "Ibn al-Zubayr", "İbnü'z-Zübeyr")
HD = H("بِـ«حَدَّثَنَا»", "«told us»", "«haddesenâ»ya")
NAPI = ("النِّطَاقِ", "the girdle", "kuşak")
TITLES = [{"ar": "فَشُقِّيهِ بِاثْنَيْنِ", "en": "Split it in two", "tr": "Onu ikiye böl"},
          {"ar": "يَا بْنَ ذَاتِ النِّطَاقَيْنِ", "en": "O son of the two girdles!", "tr": "Ey iki kuşaklının oğlu!"}]
def AKHBARANA_ABU_USAMA(p="."):
    return [ISNAD_AKHBARANA(), NOUN("أَبُو", "ab", "fail", sign="5", mudaf=True), NAME("أُسَامَةَ", "usama", "mi", dipt="tanith", p=p)]
S1 = [
 SEN(1, "Abū Usāma Ḥammād ibn Usāma told us. Hishām ibn ʿUrwa told us, from his father and Fāṭima, from Asmāʾ, who said:",
     "Bize Ebû Üsâme Hammâd b. Üsâme haber verdi. Bize Hişâm b. Urve, babasından ve Fâtıma'dan, onlar Esmâ'dan anlattı; o dedi ki:",
 [*AKHBARANA_ABU_USAMA(p=None), NAME("حَمَّادُ", "hammad-name", "badal", "raf", of=("أَبُو أُسَامَةَ", "Abū Usāma", "Ebû Üsâme"), note=NT), BN("raf", ("حَمَّادُ", "Ḥammād", "Hammâd")),
  NAME("أُسَامَةَ", "usama", "mi", dipt="tanith", p="."),
  ISNAD_HADDATHANA(), NAME("هِشَامُ", "hisham", "fail", note=NT), BN("raf", ("هِشَامُ", "Hishām", "Hişâm")), NAME("عُرْوَةَ", "urwa", "mi", dipt="tanith"),
  AN(hang=HD), NOUN("أَبِيهِ", "ab", "majr", by="عَنْ", sign="5", enc="هِ", ref=("هِشَامٍ", "Hishām", "Hişâm")),
  NAME("وَفَاطِمَةَ", "fatima", "atf", "jarr", pre=("wa",), dipt="tanith", note=(" — هِيَ فَاطِمَةُ بِنْتُ الْمُنْذِرِ، امْرَأَةُ هِشَامٍ", " — Fāṭima bint al-Mundhir, Hishām's wife", " — Hişâm'ın hanımı Fâtıma bint el-Münzir")),
  AN(hang=HD), NAME("أَسْمَاءَ", "asma-hr", "majr", by="عَنْ", dipt="alif"), QALAT_HID(AS)]),
 SEN(2, "I made the Prophet's food-bag — God bless him and grant him peace — in Abū Bakr's house when he meant to emigrate to Medina.",
     "Peygamber'in — Allah ona salât ve selâm etsin — azık torbasını, Medine'ye hicret etmek istediğinde Ebû Bekir'in evinde hazırladım.",
 [VERB("صَنَعْتُ", "sanaa", "mtu"), NOUN("سُفْرَةَ", "sufra-food", "maful", mudaf=True, note=(" — السُّفْرَةُ: طَعَامُ الْمُسَافِرِ وَمَا يُحْمَلُ فِيهِ", " — sufra: the traveller's food and its bag", " — sufra: yolcunun azığı ve torbası")),
  NOUN("النَّبِيِّ", "nabi", "mi"), *SALLA(),
  PREPT("فِي", "fi", H("بِـ«صَنَعْتُ»", "«made»", "«sana'tu»ya")), NOUN("بَيْتِ", "bayt", "majr", mudaf=True), NOUN("أَبِي", "ab", "mi", sign="5", mudaf=True), NAME("بَكْرٍ", "bakr", "mi"),
  NOUN("حِينَ", "hina", "zarf", note=(" — ظَرْفُ زَمَانٍ مُتَعَلِّقٌ بِـ«صَنَعْتُ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", " — of time, hanging on «made», annexed to the clause after it", " — zaman zarfı, «sana'tu»ya müteallik, sonraki cümleye muzâf")),
  VERB("أَرَادَ", "arada", "m", form="form-iv-verbs", g=["hollow-verbs"], hid="هُوَ", ref=("النَّبِيِّ", "the Prophet", "Peygamber")),
  PART("أَنْ", "an-nasiba", "حَرْفٌ مَصْدَرِيٌّ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِـ«أَرَادَ».", "أَنْ, which makes a maṣdar and puts the verb in nasb — the maṣdar is the object of «meant».", "«En» masdar ve nasb harfi — masdar «erâde»nin mef'ûlü.", ["an-masdariyya"]),
  VERB("يُهَاجِرَ", "hajara-emigrate", "us", form="form-iii-verbs", hid="هُوَ", ref=("النَّبِيِّ", "the Prophet", "Peygamber")),
  PREPT("إِلَى", "ila", H("بِـ«يُهَاجِرَ»", "«emigrate»", "«yuhâcire»ye")), NOUN("الْمَدِينَةِ", "madina", "majr", p=".")]),
 SEN(3, "She said: We found nothing to tie his food-bag and his water-skin with, and I said to Abū Bakr: By God, I find nothing to tie it with but my girdle.",
     "Dedi ki: Azık torbasını ve su tulumunu bağlayacak bir şey bulamadık; Ebû Bekir'e dedim ki: Vallahi onu bağlayacak kuşağımdan başka bir şey bulamıyorum.",
 [QALAT_HID(AS),
  PART("فَلَمْ", "lam-jazima", "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The fa resumes; لَمْ negates, puts the verb in jazm and turns it to the past.", "Fâ isti'nâf; «lem» nefy, cezm ve kalb harfi.", ["lam-jazim"], pre=("fa",)),
  VERB("نَجِدْ", "wajada", "uj", g=["mithal-verbs"], hid="نَحْنُ"),
  NOUN("لِسُفْرَتِهِ", "sufra-food", "majr", pre=("li",), enc="هِ", ref=("النَّبِيِّ", "the Prophet", "Peygamber"), note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَرْبِطُ»", " — the phrase hangs on «tie»", " — câr-mecrûr «nerbitu»ya müteallik")),
  PART("وَلَا", "la-nafiya", "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to stress the negation.", "Vâv atıf; «lâ» nefyi te'kîd için zâid.", ["la-nafiya", "huruf-al-ziyada-fil-kafiya"], pre=("wa",)),
  NOUN("لِسِقَائِهِ", "siqaa", "atf", "jarr", pre=("li",), enc="هِ", ref=("النَّبِيِّ", "the Prophet", "Peygamber"), note=(" — وَالسِّقَاءُ: قِرْبَةُ الْمَاءِ", " — siqāʾ: a water-skin", " — sikâ: su tulumu")),
  PART("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«نَجِدْ».", "A relative noun «what», the object of «find».", "İsm-i mevsûl «mâ», «necid»in mef'ûlü, mahallen mansûb.", ["ism-mawsul"], pos="pron"),
  VERB("نَرْبِطُهُمَا", "rabata", "u", enc="هُمَا", encref=("السُّفْرَةِ وَالسِّقَاءِ", "the bag and the skin", "torba ve tulum"), hid="نَحْنُ", cl=SILA_),
  PRON_J("بِهِ", "bi", "هِ", H("بِـ«نَرْبِطُ»، وَهُوَ الْعَائِدُ", "«tie»; it is the returning pronoun", "«nerbitu»ya; âid zamir budur"), ref=("«مَا»", "«what»", "«mâ»")),
  VERB("فَقُلْتُ", "qala", "mtu", g=["hollow-verbs"], pre=("fa",)),
  NOUN("لِأَبِي", "ab", "majr", sign="5", pre=("li",), mudaf=True, note=("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قُلْتُ»", " — the phrase hangs on «said»", " — câr-mecrûr «kultu»ya müteallik")), NAME("بَكْرٍ", "bakr", "mi", p=":"),
  WALLAHI(),
  PART("مَا", "ma-nafiya", "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "مَا negates.", "«Mâ» nefy harfi.", ["anwa-ma"]),
  VERB("أَجِدُ", "wajada", "u", g=["mithal-verbs"], hid="أَنَا", ref=AS, cl=(" — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا", "; the clause answers the oath and has no seat", "; cümle kasemin cevabı, mahalli yok")),
  NOUN("شَيْئًا", "shay", "maful"),
  VERB("أَرْبِطُهُ", "rabata", "u", enc="هُ", encref=("السِّقَاءِ", "the skin", "tulum"), hid="أَنَا", ref=AS, cl=(" — وَالْجُمْلَةُ نَعْتٌ لِـ«شَيْئًا» فِي مَحَلِّ نَصْبٍ", "; the clause describes «anything», in the seat of nasb", "; cümle «şey'en»in na'tı, mahallen mansûb")),
  PRON_J("بِهِ", "bi", "هِ", H("بِـ«أَرْبِطُ»", "«tie»", "«erbitu»ya"), ref=("«شَيْئًا»", "«anything»", "«şey'en»")),
  PART("إِلَّا", "illa", "حَرْفُ اسْتِثْنَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "إِلَّا «but», the particle of exception.", "«İllâ» istisnâ harfi.", ["istithna"]),
  NOUN("نِطَاقِي", "nitaq-amr", "badal", "nasb", sign="ya", enc="ي", of=("شَيْئًا", "anything", "şey'en"), note=(" — بَدَلٌ مِنْ «شَيْئًا» فِي الْكَلَامِ التَّامِّ الْمَنْفِيِّ (وَيَجُوزُ نَصْبُهُ عَلَى الِاسْتِثْنَاءِ)، وَالنِّطَاقُ: مَا تَشُدُّ بِهِ الْمَرْأَةُ وَسَطَهَا", " — a substitute for «anything» in a complete negated sentence (or in nasb as the excepted); niṭāq: the band a woman ties round her waist", " — tam olumsuz sözde «şey'en»den bedel (istisnâ ile nasb da caizdir); nitâk: kadının beline bağladığı kuşak"), p=".")]),
 SEN(4, "He said: Then split it in two, and tie the water-skin with one and the food-bag with the other.",
     "Dedi ki: Öyleyse onu ikiye böl; biriyle tulumu, öbürüyle torbayı bağla.",
 [QALA_HID(AB),
  tok("فَشُقِّيهِ", "shaqqa", "verb", ["imperative-amr", "doubled-verbs", "al-bariz-al-muttasil", "maful-bihi"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ شَرْطٍ مُقَدَّرٍ، وَشُقِّي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى النِّطَاقِ.",
      "The fa answers an understood condition; «split» is an imperative built on dropping the nūn, the ya of the woman addressed its doer, «it» (the girdle) its object.",
      "Fâ takdir edilen şartın cevabında; «şukkî» nûnun hazfi üzere mebnî emir, muhâtaba yâsı fâil, «hû» (kuşak) mef'ûlün bih.",
      segments=[seg("فَ", "fa", "conj"), seg("شُقِّي", "shaqqa", "verb"), seg("هِ", "pron-3ms", "pron")]),
  NOUN("بِاثْنَيْنِ", "ithnan", "majr", sign="du", pre=("bi",), note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«شُقِّي»", " — the phrase hangs on «split»", " — câr-mecrûr «şukkî»ye müteallik")),
  tok("فَارْبِطِي", "rabata", "verb", ["imperative-amr", "atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ، وَارْبِطِي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "The fa conjoins; «tie» is an imperative built on dropping the nūn; the ya of the woman addressed is its doer.", "Fâ atıf; «irbitî» nûnun hazfi üzere mebnî emir; muhâtaba yâsı fâil.",
      segments=[seg("فَ", "fa", "conj"), seg("ارْبِطِ", "rabata", "verb"), seg("ي", "pron-2fs", "pron")]),
  NOUN("بِوَاحِدٍ", "wahid", "majr", pre=("bi",), note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ارْبِطِي»، قُدِّمَا عَلَى الْمَفْعُولِ", " — the phrase hangs on «tie», set before the object", " — câr-mecrûr «irbitî»ye müteallik, mef'ûlden önce geldi")),
  NOUN("السِّقَاءَ", "siqaa", "maful"),
  NOUN("وَبِالْآخَرِ", "akhar", "atf", "jarr", pre=("wa", "bi"), note=(" — مَعْطُوفٌ عَلَى «بِوَاحِدٍ»", " — conjoined to «with one»", " — «bi-vâhidin»e ma'tûf")),
  NOUN("السُّفْرَةَ", "sufra-food", "atf", "nasb", of=("السِّقَاءَ", "the water-skin", "tulum"), p=".")]),
 SEN(5, "So I did; and for that she was called «She of the Two Girdles».",
     "Ben de öyle yaptım; bu yüzden «İki Kuşaklı» diye adlandırıldı.",
 [VERB("فَفَعَلْتُ", "faala", "mtu", pre=("fa",)),
  PART("فَلِذٰلِكَ", "li", "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَذَا اسْمُ إِشَارَةٍ فِي مَحَلِّ جَرٍّ، وَاللَّامُ الثَّانِيَةُ لِلْبُعْدِ وَالْكَافُ لِلْخِطَابِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سُمِّيَتْ».",
       "The fa resumes; the lam «for» is a jarr letter with «that» in its seat of jarr — the phrase hangs on «she was called».", "Fâ isti'nâf; lâm ta'lîl cer harfi, «zâ» işaret ismi mahallen mecrûr — câr-mecrûr «summiyet»e müteallik.",
       ["huruf-jarr", "asma-al-ishara-wa-sighuha"], pre=("fa", "li"), s="dhalika", spos="pron"),
  VERB("سُمِّيَتْ", "samma", "pt", form="form-ii-verbs", g=["naqis-verbs", "naib-al-fail"], hid="هِيَ", ref=AS, note=(" — وَهُوَ مِنْ كَلَامِ الرَّاوِي", " — the narrator's words", " — râvinin sözü")),
  NOUN("ذَاتَ", "dhat", "maful2", mudaf=True, note=(" — لِأَنَّ «سَمَّى» يَنْصِبُ مَفْعُولَيْنِ، وَالْأَوَّلُ نَائِبُ الْفَاعِلِ", " — سَمَّى takes two objects; the first became the deputy doer", " — «semmâ» iki mef'ûl alır; birincisi nâib-i fâil oldu")),
  NOUN("النِّطَاقَيْنِ", "nitaq-amr", "mi", sign="du", p=".")]),
]
S2 = [
 SEN(6, "Abū Usāma told us. Hishām ibn ʿUrwa told us, from his father,",
     "Bize Ebû Üsâme haber verdi. Bize Hişâm b. Urve babasından anlattı:",
 [*AKHBARANA_ABU_USAMA(), ISNAD_HADDATHANA(), NAME("هِشَامُ", "hisham", "fail", note=NT), BN("raf", ("هِشَامُ", "Hishām", "Hişâm")), NAME("عُرْوَةَ", "urwa", "mi", dipt="tanith"),
  AN(hang=HD), NOUN("أَبِيهِ", "ab", "majr", by="عَنْ", sign="5", enc="هِ", ref=("هِشَامٍ", "Hishām", "Hişâm"), p="،")]),
 SEN(7, "that the people of Syria were fighting Ibn al-Zubayr and shouting at him: O son of the two girdles!",
     "Şamlılar İbnü'z-Zübeyr'le savaşıyor ve ona: Ey iki kuşaklının oğlu! diye bağırıyorlardı.",
 [PART("أَنَّ", "anna", "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: يُحَدِّثُ أَنَّ.", "أَنَّ «that» — its maṣdar is the object of an understood «he related».", "«Enne» te'kîd ve nasb harfi — masdar, mahzûf «anlatır»ın mef'ûlü.", ["inna-wa-akhawatuha", "hadhf-wa-taqdir"]),
  NOUN("أَهْلَ", "ahl", "isminna", mudaf=True), NAME("الشَّامِ", "sham", "mi"),
  VERB("كَانُوا", "kana", "mw", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ، وَالْوَاوُ اسْمُهُ", " — defective; the waw is its noun", " — nâkıs; vâv ismi"), cl=KH_INNA_CL),
  VERB("يُقَاتِلُونَ", "qatala-fight", "u5", form="form-iii-verbs", cl=KH_KANA), NOUN("ابْنَ", "ibn", "maful", mudaf=True), NAME("الزُّبَيْرِ", "zubayr", "mi"),
  VERB("وَيَصِيحُونَ", "saha-shout", "u5", g=["hollow-verbs"], pre=("wa",)),
  PRON_J("بِهِ", "bi", "هِ", H("بِـ«يَصِيحُونَ»", "«shouting»", "«yesîhûne»ye"), ref=IZ, p=":"), YA(),
  NOUN("بْنَ", "ibn", "munada", mudaf=True, note=(" — مُنَادًى مُضَافٌ، وَحُذِفَتْ هَمْزَتُهُ وَصْلًا وَخَطًّا", " — a called noun that is annexed; its hamza drops in joining and in writing", " — muzâf münâdâ; hemzesi vasılda ve yazıda düştü")),
  NOUN("ذَاتِ", "dhat", "mi", mudaf=True), NOUN("النِّطَاقَيْنِ", "nitaq-amr", "mi", sign="du", p=".", note=(" — يُعَيِّرُونَهُ بِأُمِّهِ أَسْمَاءَ", " — taunting him with his mother Asmāʾ", " — onu annesi Esmâ ile ayıplıyorlar"))]),
 SEN(8, "Ibn al-Zubayr said: «That is a reproach whose shame has fallen away from you.»",
     "İbnü'z-Zübeyr dedi ki: «Bu, ayıbı senden uzak kalmış bir kınamadır.»",
 [QALA_AFTER(pre=("fa",)), NOUN("ابْنُ", "ibn", "fail", mudaf=True), NAME("الزُّبَيْرِ", "zubayr", "mi", p=":"),
  ISHARA_T("تِلْكَ", "tilka", "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَهُوَ شَطْرُ بَيْتٍ لِأَبِي ذُؤَيْبٍ الْهُذَلِيِّ تَمَثَّلَ بِهِ", "in the seat of raf' as the mubtadaʾ — a half-line of Abū Dhuʾayb al-Hudhalī, quoted as a proverb", "mahallen merfû mübtedâ — Ebû Züeyb el-Hüzelî'nin mısraı, temessül edildi", built="الْكَسْرِ", g=["mubtada-khabar"]),
  NOUN("شَكَاةٌ", "shakat-tf", "khabar", note=(" — الشَّكَاةُ: الذَّمُّ وَالْعَيْبُ", " — shakāt: blame, reproach", " — şekât: kınama, ayıplama")),
  NOUN("ظَاهِرٌ", "zahir", "naat", "raf", of=("شَكَاةٌ", "a reproach", "kınama"), g=["ism-fail"], note=(" — وَهُوَ عَامِلٌ عَمَلَ فِعْلِهِ: «عَارُهَا» فَاعِلُهُ؛ وَظَاهِرٌ عَنْكَ: زَائِلٌ لَا يَلْزَمُكَ", " — working as its verb: «its shame» is its doer; ẓāhir ʿanka: gone off you, not clinging", " — fiili gibi amel eder: «ârühâ» fâilidir; zâhirun anke: senden zâil, sana yapışmaz")),
  PRON_J("عَنْكَ", "an", "كَ", H("بِـ«ظَاهِرٌ»", "«fallen away»", "«zâhir»e"), ref=IZ),
  NOUN("عَارُهَا", "ar-shame", "fail", enc="هَا", ref=("الشَّكَاةِ", "the reproach", "kınama"), note=(" — فَاعِلُ اسْمِ الْفَاعِلِ «ظَاهِرٌ»", " — the doer of the participle «fallen away»", " — ism-i fâil «zâhir»in fâili"), p=".")]),
 SEN(9, "Asmāʾ said to him: Did they taunt you with it? He said: Yes. She said: Then it is, by God, the truth.",
     "Esmâ ona: Seni bununla mı ayıpladılar? dedi. O: Evet, dedi. Esmâ: Öyleyse o, vallahi haktır, dedi.",
 [QALA_AFTER(pre=("fa",), fem=True), PRON_J("لَهُ", "li", "هُ", H("بِـ«قَالَتْ»", "«said»", "«kâlet»e"), ref=IZ), NAME("أَسْمَاءُ", "asma-hr", "fail", dipt="alif", p=":"),
  VERB("عَيَّرُوكَ", "ayyara", "mw", form="form-ii-verbs", enc="كَ", encref=IZ, note=(" — وَهَمْزَةُ الِاسْتِفْهَامِ مُقَدَّرَةٌ: أَعَيَّرُوكَ؟", " — the question's hamza is understood: «did they taunt you?»", " — soru hemzesi takdirîdir: «seni ayıpladılar mı?»")),
  PRON_J("بِهِ", "bi", "هِ", H("بِـ«عَيَّرُوا»", "«taunted»", "«ayyerû»ya"), ref=("نِطَاقَيْهَا", "her two girdles", "iki kuşağı"), p="؟"),
  QALA_HID(IZ),
  PART("نَعَمْ", "naam", "حَرْفُ جَوَابٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "نَعَمْ «yes», a particle of answer.", "«Neam» cevap harfi.", [], p="."),
  QALAT_HID(AS),
  PART("فَهُوَ", "huwa", "الْفَاءُ رَابِطَةٌ لِجَوَابِ شَرْطٍ مُقَدَّرٍ (إِنْ كَانَ كَذٰلِكَ فَهُوَ …)، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ يَعُودُ عَلَى مَا عَيَّرُوهُ بِهِ.",
       "The fa ties the answer of an understood condition; «it» (what they taunted him with) is the mubtadaʾ.", "Fâ takdir edilen şartın cevabını bağlar; «hüve» (ayıpladıkları şey) mübtedâ.", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"], pre=("fa",), pos="pron"),
  NOTE(WALLAHI(), " — وَجُمْلَةُ الْقَسَمِ مُعْتَرِضَةٌ", "; the oath is set in between", "; kasem cümlesi araya girmiştir"),
  NOUN("حَقٌّ", "haqq", "khabar", p=".")]),
]
CHAPS = [S1, S2]
NEW_GLOSS = {
 "sufra-food": NN("سُفْرَة", "س ف ر", "a traveller's food, and the bag it is carried in", "yolcu azığı ve torbası"),
 "urwa": NP("عُرْوَة", "ʿUrwa — here ʿUrwa ibn al-Zubayr, the Medinan Successor", "Urve — burada Medineli tâbiî Urve b. ez-Zübeyr"),
 "siqaa": NN("سِقَاء", "س ق ي", "a water-skin", "su tulumu"),
 "ar-shame": NN("عَار", "ع ي ر", "shame, disgrace", "ayıp, utanç"),
}
GLOSS_HERE = {"usama": ("Usāma — in Abū Usāma Ḥammād ibn Usāma", "Üsâme — Ebû Üsâme Hammâd b. Üsâme'de"), "hammad-name": ("Ḥammād (ibn Usāma, Abū Usāma)", "Hammâd (b. Üsâme, Ebû Üsâme)"),
              "zahir": ("gone away, fallen off (ظَاهِرٌ عَنْكَ: not clinging to you)", "zâil, uzak (ظَاهِرٌ عَنْكَ: sana yapışmayan)"),
              "fatima": ("Fāṭima — here Fāṭima bint al-Mundhir, Hishām ibn ʿUrwa's wife", "Fâtıma — burada Hişâm b. Urve'nin hanımı Fâtıma bint el-Münzir")}
MANIFEST = manifest(SLUG, 4, {"ar": "ذَاتُ النِّطَاقَيْنِ", "en": "She of the Two Girdles", "tr": "İki Kuşaklı"},
  {"ar": "أَسْمَاءُ بِنْتُ أَبِي بَكْرٍ وَنِطَاقُهَا", "en": "Asmāʾ bint Abī Bakr and her girdle", "tr": "Esmâ bint Ebî Bekir ve kuşağı"}, "nisa",
  "Asmāʾ bint Abī Bakr's entry, vol. 8, printed pp. 196–197 (Shamela pp. 2863–2864)", "Esmâ bint Ebî Bekir maddesi, cilt 8, matbû s. 196–197 (Şâmile s. 2863–2864)", "تَرْجَمَةُ أَسْمَاءَ بِنْتِ أَبِي بَكْرٍ، الْجُزْءُ ٨، ص ١٩٦–١٩٧ (الشَّامِلَةُ ص ٢٨٦٣–٢٨٦٤)",
  "two consecutive akhbār of Hishām ibn ʿUrwa, each whole with its isnād: «أخبرنا أبو أسامة حماد بن أسامة.» … «فلذلك سميت ذات النطاقين.» and «أخبرنا أبو أسامة. حدثنا هشام بن عروة عن أبيه أن أهل الشام» … «فهو والله حق.», one chapter each; Ibn al-Zubayr's answer is a half-line of Abū Dhuʾayb al-Hudhalī",
  "Hişâm b. Urve'nin art arda iki haberi, her biri isnadıyla tam: «أخبرنا أبو أسامة حماد بن أسامة.» … «فلذلك سميت ذات النطاقين.» ve «أخبرنا أبو أسامة. حدثنا هشام بن عروة عن أبيه أن أهل الشام» … «فهو والله حق.»; her biri bir bölüm; İbnü'z-Zübeyr'in cevabı Ebû Züeyb el-Hüzelî'nin bir mısraıdır",
  "خَبَرَانِ مُتَتَالِيَانِ لِهِشَامِ بْنِ عُرْوَةَ بِإِسْنَادَيْهِمَا، لِكُلٍّ مِنْهُمَا فَصْلٌ",
  kept=[("«يا بن» بِغَيْرِ أَلِفٍ كَمَا طُبِعَ", "«يا بن» without the alif, as printed", "«يا بن» elifsiz, baskıdaki gibi")],
  hoca=[("«نَرْبِطُ / أَرْبِطُ» with kasra (يَرْبُطُ with ḍamma is also heard)", "«نَرْبِطُ / أَرْبِطُ» kesreyle (ötreli يَرْبُطُ de işitilmiştir)"),
        ("«إِلَّا نِطَاقِي» read as a badal (nasb on the exception is also allowed)", "«إِلَّا نِطَاقِي» bedel okundu (istisnâ üzere nasb da caiz)"),
        ("«تِلْكَ شَكَاةٌ ظَاهِرٌ عَنْكَ عَارُهَا» — Abū Dhuʾayb's half-line, quoted without its «و»", "«تِلْكَ شَكَاةٌ ظَاهِرٌ عَنْكَ عَارُهَا» — Ebû Züeyb'in mısraı, «و»suz aktarıldı")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE)
