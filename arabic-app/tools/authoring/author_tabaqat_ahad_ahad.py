"""Author content/samples/tabaqat-ahad-ahad — «أَحَدٌ أَحَدٌ», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Companions, Bilāl ibn Rabāḥ's entry, vol. 3 p. 175 (Shamela p.
853): two consecutive akhbār, each whole with its isnād — ʿUmayr ibn Isḥāq's («قال: أخبرنا عثمان بن عمر» … «إن لساني لا يحسنه.») and
Muḥammad [ibn Sīrīn]'s («قال: أخبرنا عارم بن الفضل» … «قد أعتقته يا رسول الله.»), one chapter each.
The exact passage: research/sources/tabaqat-ahad-ahad-src.txt. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_tabaqat_ahad_ahad.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-ahad-ahad"
ISNAD_V = H("بِـ«أَخْبَرَنَا»", "«told us»", "«ahberanâ»ya")
BL = ("بِلَالٍ", "Bilāl", "Bilâl")
AB = ("أَبِي بَكْرٍ", "Abū Bakr", "Ebû Bekir")
MSH = ("الْمُشْرِكِينَ الْمُعَذِّبِينَ", "his torturers", "ona işkence edenler")
AHAD_KH = (" — تَقْدِيرُهُ: هُوَ أَحَدٌ، يَعْنِي اللهَ تَعَالَى", " — understood: «He is One», meaning God", " — takdiri: «O birdir», yani Allah Teâlâ")
def AHAD2(p="."):
    return [NOUN("أَحَدٌ", "ahad", "khmh", note=AHAD_KH),
            NOUN("أَحَدٌ", "ahad", "tawkid", "raf", note=(" — تَوْكِيدٌ لَفْظِيٌّ لِمَا قَبْلَهُ", " — the word repeated for emphasis", " — öncekinin lafzî te'kîdi"), p=p)]
TITLES = [{"ar": "إِنَّ لِسَانِي لَا يُحْسِنُهُ", "en": "My tongue cannot say it", "tr": "Dilim onu beceremez"},
          {"ar": "الشَّرِكَةَ يَا أَبَا بَكْرٍ", "en": "A share, Abū Bakr!", "tr": "Ortaklık, ey Ebû Bekir!"}]
S1 = [
 SEN(1, "He said: ʿUthmān ibn ʿUmar and Muḥammad ibn ʿAbd Allāh al-Anṣārī told us — they both said: Ibn ʿAwn told us, from ʿUmayr ibn Isḥāq, who said:",
     "Dedi ki: Bize Osman b. Ömer ile Muhammed b. Abdullah el-Ensârî haber verdi; ikisi dediler ki: Bize İbn Avn, Umeyr b. İshâk'tan haber verdi; o dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(),
  NAME("عُثْمَانُ", "uthman", "fail", dipt="nun", note=(" — وَلَا تَنْوِينَ فِيهِ لِلْمَنْعِ وَلِلْوَصْفِ بِـ«ابْن»", " — no tanwin in any case", " — her hâlükârda tenvinsiz")),
  BN("raf", ("عُثْمَانُ", "ʿUthmān", "Osman")), NAME("عُمَرَ", "umar", "mi", dipt="adl"),
  NAME("وَمُحَمَّدُ", "muhammad", "atf", "raf", pre=("wa",), note=NT), BN("raf", ("مُحَمَّدُ", "Muḥammad", "Muhammed")),
  NOUN("عَبْدِ", "abd", "mi", mudaf=True), ALLAH_MI(), NOUN("الْأَنْصَارِيُّ", "ansari", "naat", "raf", of=("مُحَمَّدُ", "Muḥammad", "Muhammed"), note=(" — نِسْبَةٌ إِلَى الْأَنْصَارِ", " — a nisba to the Anṣār", " — Ensâr'a nisbet")),
  VERB("قَالَا", "qala", "mA", g=["hollow-verbs"], cl=QALA_W, p=":"), ISNAD_AKHBARANA(),
  NOUN("ابْنُ", "ibn", "fail", mudaf=True), NAME("عَوْنٍ", "awn-name", "mi"),
  AN(hang=ISNAD_V), NAME("عُمَيْرِ", "umayr", "majr", by="عَنْ", note=NT), BN("jarr", ("عُمَيْرِ", "ʿUmayr", "Umeyr")), NAME("إِسْحَاقَ", "ishaq", "mi", dipt="ujma"),
  QALA_HID(("عُمَيْرِ بْنِ إِسْحَاقَ", "ʿUmayr ibn Isḥāq", "Umeyr b. İshâk"))]),
 SEN(2, "Whenever they pressed hard on him in the torment, Bilāl would say: One! One!",
     "Bilâl, işkencede ona şiddetlendikleri zaman: Bir! Bir! derdi.",
 [VERB("كَانَ", "kana", "m", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَيُفِيدُ هُنَا الِاسْتِمْرَارَ", " — the defective verb; here it tells of a habit", " — nâkıs; burada âdet bildirir")),
  NAME("بِلَالٌ", "bilal", "ismk"),
  PART("إِذَا", "idha", "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ غَيْرُ جَازِمٍ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ الشَّرْطِ — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ».",
       "إِذَا «whenever», an adverb of time carrying a condition, governing no jazm, annexed to its clause — the condition and its answer are the predicate of كَانَ.",
       "«İzâ» şart anlamı taşıyan, cezmetmeyen zaman zarfı, şart cümlesine muzâf — şart ve cevabı «kâne»nin haberi, mahallen mansûb.", ["maful-fih", "idha-shartiyya"], pos="noun"),
  VERB("اشْتَدُّوا", "ishtadda", "mw", form="form-viii-verbs", g=["doubled-verbs"], note=(" — يَعُودُ عَلَى مُعَذِّبِيهِ", " (his torturers)", " (işkencecileri)"), cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "; the clause is in the seat of jarr, annexed to إِذَا", "; cümle «izâ»ya muzâfun ileyh, mahallen mecrûr")),
  PRON_J("عَلَيْهِ", "ala", "هِ", H("بِـ«اشْتَدُّوا»", "«pressed hard»", "«işteddû»ya"), ref=BL),
  PREPT("فِي", "fi", H("بِـ«اشْتَدُّوا»", "«pressed hard»", "«işteddû»ya")), NOUN("الْعَذَابِ", "adhab", "majr"),
  VERB("قَالَ", "qala", "m", g=["hollow-verbs"], hid="هُوَ", ref=BL, cl=(" — وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا، وَمَا بَعْدَهَا مَقُولُ الْقَوْلِ", "; the clause answers إِذَا and has no seat; what follows is what he said", "; cümle «izâ»nın cevabı, mahalli yok; sonrası mekūlü'l-kavl"), p=":"),
  *AHAD2()]),
 SEN(3, "They would say to him: Say as we say.",
     "Ona: Bizim dediğimiz gibi de! derlerdi.",
 [VERB("فَيَقُولُونَ", "qala", "u5", g=["hollow-verbs"], pre=("fa",), note=(" — يَعُودُ عَلَى مُعَذِّبِيهِ", " (his torturers)", " (işkencecileri)"), cl=QALA_W),
  PRON_J("لَهُ", "li", "هُ", H("بِـ«يَقُولُونَ»", "«say»", "«yekūlûne»ye"), ref=BL, p=":"),
  VERB("قُلْ", "qala", "amr", g=["hollow-verbs"], note=(" — وَحُذِفَتْ عَيْنُهُ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ", " — its middle waw drops where two sukūns meet", " — iki sâkin karşılaştığı için orta harfi (vâv) düştü")),
  PART("كَمَا", "ka", "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَصْدَرٍ مَحْذُوفٍ: قُلْ قَوْلًا كَقَوْلِنَا.",
       "The kaf «as», a jarr letter, with مَا that makes a maṣdar — «say a saying like our saying».", "Kâf teşbih için cer harfi; «mâ» masdar harfi — «bizim sözümüz gibi bir söz söyle».", ["huruf-jarr", "an-masdariyya"], pre=("ka",), s="ma-masdariyya", spos="part"),
  VERB("نَقُولُ", "qala", "u", g=["hollow-verbs"], hid="نَحْنُ", p=".")]),
 SEN(4, "And he would say: My tongue cannot do it well.",
     "O da: Benim dilim onu beceremez! derdi.",
 [VERB("فَيَقُولُ", "qala", "u", g=["hollow-verbs"], hid="هُوَ", ref=BL, pre=("fa",), cl=QALA_W, p=":"),
  PART("إِنَّ", "inna", "حَرْفُ تَوْكِيدٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ مَبْنِيٌّ عَلَى الْفَتْحِ.", "إِنَّ, the particle of emphasis that puts its noun in nasb.", "«İnne» te'kîd ve nasb harfi.", ["inna-wa-akhawatuha"]),
  NOUN("لِسَانِي", "lisan", "isminna", sign="ya", enc="ي"),
  PART("لَا", "la-nafiya", "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "لَا negates.", "«Lâ» nefy harfi.", ["la-nafiya"]),
  VERB("يُحْسِنُهُ", "ahsana", "u", form="form-iv-verbs", enc="هُ", encref=("قَوْلِهِمْ", "what they say", "onların sözü"), hid="هُوَ", ref=("اللِّسَانِ", "the tongue", "dil"), cl=KH_INNA_CL, p=".")]),
]
S2 = [
 SEN(5, "He said: ʿĀrim ibn al-Faḍl told us; he said: Ḥammād ibn Zayd told us, from Ayyūb, from Muḥammad,",
     "Dedi ki: Bize Ârim b. el-Fadl haber verdi; dedi ki: Bize Hammâd b. Zeyd, Eyyûb'dan, o Muhammed'den haber verdi:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("عَارِمُ", "arim", "fail", note=NT), BN("raf", ("عَارِمُ", "ʿĀrim", "Ârim")), NAME("الْفَضْلِ", "fadl-alam", "mi"),
  QALA_HID(("عَارِمٍ", "ʿĀrim", "Ârim")), ISNAD_AKHBARANA(), NAME("حَمَّادُ", "hammad-name", "fail", note=NT), BN("raf", ("حَمَّادُ", "Ḥammād", "Hammâd")), NAME("زَيْدٍ", "zayd", "mi"),
  AN(hang=ISNAD_V), NAME("أَيُّوبَ", "ayyub", "majr", by="عَنْ", dipt="ujma"), AN(hang=ISNAD_V), NAME("مُحَمَّدٍ", "muhammad", "majr", by="عَنْ", p="،",
   note=(" — هُوَ مُحَمَّدُ بْنُ سِيرِينَ", " — Muḥammad ibn Sīrīn", " — Muhammed b. Sîrîn"))]),
 SEN(6, "that Bilāl's masters took him, stretched him out and threw stones of the valley and a cowhide on him, and they began to say: Your lord is al-Lāt and al-ʿUzzā.",
     "Bilâl'i sahipleri yakaladılar, yere uzattılar, üstüne vadinin taşlarını ve bir sığır derisi attılar; ve: Senin rabbin Lât ile Uzzâ'dır! demeye başladılar.",
 [PART("أَنَّ", "anna", "حَرْفُ تَوْكِيدٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: يُحَدِّثُ أَنَّ.",
       "أَنَّ «that», which puts its noun in nasb — the maṣdar it makes is the object of an understood «he related».", "«Enne» te'kîd ve nasb harfi — masdar, mahzûf «anlatır» fiilinin mef'ûlü.", ["inna-wa-akhawatuha", "hadhf-wa-taqdir"]),
  NAME("بِلَالًا", "bilal", "isminna"),
  VERB("أَخَذَهُ", "akhadha", "m", g=["mahmuz-verbs"], enc="هُ", encref=BL, doer_after=True, cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ»", "; the clause is the predicate of أَنَّ, in the seat of raf'", "; cümle «enne»nin haberi, mahallen merfû")),
  NOUN("أَهْلُهُ", "ahl", "fail", enc="هُ", ref=BL, note=(" — يَعْنِي مَوَالِيَهُ", " — his masters", " — efendileri")),
  VERB("فَمَطُّوهُ", "matta", "mw", g=["doubled-verbs"], enc="هُ", encref=BL, pre=("fa",), note=(" — مَطَّهُ: مَدَّهُ", " — مَطَّ: to stretch out", " — matta: uzattı")),
  VERB("وَأَلْقَوْا", "alqa", "mwa", form="form-iv-verbs", g=["naqis-verbs"], pre=("wa",)),
  PRON_J("عَلَيْهِ", "ala", "هِ", H("بِـ«أَلْقَوْا»", "«threw»", "«elkav»a"), ref=BL),
  PREPT("مِنَ", "min", H("بِـ«أَلْقَوْا»، وَهُوَ فِي مَحَلِّ الْمَفْعُولِ بِهِ", "«threw», standing as its object", "«elkav»a; mef'ûl yerinde"), ("، وَحُرِّكَتْ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ، لِلتَّبْعِيضِ", " of part, voweled with fatḥa before the sukūn", " (teb'îz; iki sâkin karşılaştığı için fetha)")),
  NOUN("الْبَطْحَاءِ", "batha", "majr", note=(" — الْبَطْحَاءُ: حَصَى الْمَسِيلِ", " — al-baṭḥāʾ: the pebbles of a stream-bed", " — el-bathâ: sel yatağının çakılları")),
  NOUN("وَجِلْدَ", "jild", "atf", "nasb", pre=("wa",), mudaf=True, note=(" — مَعْطُوفٌ عَلَى مَحَلِّ «مِنَ الْبَطْحَاءِ»", " — conjoined to the seat of «of the stones»", " — «mine'l-bathâ»nın mahalline ma'tûf")),
  NOUN("بَقَرَةٍ", "baqara", "mi"),
  VERB("فَجَعَلُوا", "jaala", "mw", pre=("fa",), note=(" — مِنْ أَفْعَالِ الشُّرُوعِ، وَالْوَاوُ اسْمُهُ", " — a verb of beginning; the waw is its noun", " — şürû' fiillerinden; vâv onun ismi"), g=["afal-al-muqaraba"]),
  VERB("يَقُولُونَ", "qala", "u5", g=["hollow-verbs"], cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «جَعَلَ»، وَمَا بَعْدَهَا مَقُولُ الْقَوْلِ", "; the clause is the predicate of «began»; what follows is what they said", "; cümle «ceale»nin haberi; sonrası mekūlü'l-kavl"), p=":"),
  NOUN("رَبُّكَ", "rabb", "mubt", enc="كَ", ref=BL), NAME("اللَّاتُ", "lat", "khabar", note=(" — اسْمُ صَنَمٍ", " — the name of an idol", " — bir putun adı")),
  NAME("وَالْعُزَّى", "uzza", "atf", "raf", sign="maq", pre=("wa",), note=(" — اسْمُ صَنَمٍ", " — the name of an idol", " — bir putun adı"), p=".")]),
 SEN(7, "And he would say: One! One!",
     "O ise: Bir! Bir! derdi.",
 [VERB("وَيَقُولُ", "qala", "u", g=["hollow-verbs"], hid="هُوَ", ref=BL, pre=("wa-hal",), cl=QALA_W, p=":"), *AHAD2()]),
 SEN(8, "He said: Then Abū Bakr came upon him and said: Over what are you tormenting this man?",
     "Dedi ki: Ebû Bekir onun yanına geldi ve: Bu insana ne diye işkence ediyorsunuz? dedi.",
 [VERB("قَالَ", "qala", "m", g=["hollow-verbs"], hid="هُوَ", ref=("مُحَمَّدِ بْنِ سِيرِينَ", "Muḥammad ibn Sīrīn", "Muhammed b. Sîrîn"), cl=QALA_W),
  VERB("فَأَتَى", "ata", "ma", g=["mahmuz-verbs", "naqis-verbs"], doer_after=True, pre=("fa",)),
  PRON_J("عَلَيْهِ", "ala", "هِ", H("بِـ«أَتَى»", "«came»", "«etâ»ya"), ref=BL), NOUN("أَبُو", "ab", "fail", sign="5", mudaf=True), NAME("بَكْرٍ", "bakr", "mi"),
  QALA_HID(AB, pre=("fa",)),
  PART("عَلَامَ", "ala", "عَلَى حَرْفُ جَرٍّ، وَمَا اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَحُذِفَتْ أَلِفُهُ لِدُخُولِ حَرْفِ الْجَرِّ عَلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُعَذِّبُونَ».",
       "عَلَى «over» with the question noun مَا «what», its alif dropped after the jarr letter — the phrase hangs on «torment».",
       "«Alâ» cer harfi ve «mâ» soru ismi; cer harfi girdiği için elifi düştü — câr-mecrûr «tu'azzibûne»ye müteallik.", ["huruf-jarr", "al-istifham"], pos="prep"),
  VERB("تُعَذِّبُونَ", "adhdhaba", "u5", form="form-ii-verbs"),
  ISHARA_T("هٰذَا", "hadha", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "in the seat of nasb as the object", "mahallen mansûb mef'ûlün bih"),
  NOUN("الْإِنْسَانَ", "insan", "badal", "nasb", of=("هٰذَا", "this", "bu"), p="؟")]),
 SEN(9, "He said: So he bought him for seven ounces and set him free.",
     "Dedi ki: Bunun üzerine onu yedi ukiyyeye satın aldı ve azat etti.",
 [QALA_HID(("مُحَمَّدِ بْنِ سِيرِينَ", "Muḥammad ibn Sīrīn", "Muhammed b. Sîrîn")),
  VERB("فَاشْتَرَاهُ", "ishtara", "ma", form="form-viii-verbs", g=["naqis-verbs"], enc="هُ", encref=BL, hid="هُوَ", ref=AB, pre=("fa",)),
  NOUN("بِسَبْعِ", "sab-seven", "majr", pre=("bi",), mudaf=True, note=("، وَالْبَاءُ لِلْعِوَضِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اشْتَرَى»", " — the ba of price; the phrase hangs on «bought»", " — bedel bâsı; câr-mecrûr «iştarâ»ya müteallik")),
  NOUN("أَوَاقٍ", "uqiyya", "mi", note=(" — تَمْيِيزُ الْعَدَدِ، جَمْعُ أُوقِيَّةٍ، مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْيَاءِ",
        " — the number's specifier, plural of أُوقِيَّة «ounce» (of silver): a furthest-pattern plural, its jarr an estimated fatḥa on the dropped ya; the tanwin stands for the ya",
        " — sayının temyîzi, ukiyye'nin çoğulu: müntehe'l-cumû' kalıbında, cerri düşen yâ üzerinde takdîrî fetha ile; tenvin yâya bedeldir")),
  VERB("فَأَعْتَقَهُ", "ataqa-free", "m", form="form-iv-verbs", enc="هُ", encref=BL, hid="هُوَ", ref=AB, pre=("fa",), p=".")]),
 SEN(10, "That was told to the Prophet — God bless him and grant him peace.",
     "Bu, Peygamber'e — Allah ona salât ve selâm etsin — anlatıldı.",
 [VERB("فَذَكَرَ", "dhakara", "m", hid="هُوَ", ref=AB, pre=("fa",)),
  ISHARA_T("ذٰلِكَ", "dhalika", "فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "in the seat of nasb as the object", "mahallen mansûb mef'ûlün bih"),
  NOUN("لِلنَّبِيِّ", "nabi", "majr", pre=("li",), note=("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ذَكَرَ»", " — the phrase hangs on «told»", " — câr-mecrûr «zekera»ye müteallik")), *SALLA(p=".")]),
 SEN(11, "He said: A share, O Abū Bakr!",
     "Buyurdu ki: Ortaklık, ey Ebû Bekir!",
 [QALA_HID(("النَّبِيِّ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ", "the Prophet", "Peygamber"), pre=("fa",)),
  PART("الشَّرِكَة", "shirka", "يَحْتَمِلُ النَّصْبَ بِفِعْلٍ مَحْذُوفٍ (اجْعَلْ لِيَ الشَّرِكَةَ) وَالرَّفْعَ — فَتُرِكَ ضَبْطُ آخِرِهِ لِلْعَالِمِ؛ وَالشَّرِكَةُ: أَنْ يَكُونَ لَهُ فِيهِ نَصِيبٌ.",
       "Open to nasb by a dropped verb («give me the share») and to raf' — its last vowel is left for the scholar; the share: a part in the purchase.",
       "Mahzûf bir fiille nasb («bana ortaklık ver») ve ref mümkündür — son harekesi hocaya bırakıldı; ortaklık: azatta bir payı olması.", ["hadhf-wa-taqdir"], pos="noun"),
  YA(), NOUN("أَبَا", "ab", "munada", sign="5", mudaf=True, note=(" — مُنَادًى مُضَافٌ", " — a called noun that is annexed", " — muzâf münâdâ")), NAME("بَكْرٍ", "bakr", "mi", p="!")]),
 SEN(12, "He said: I have set him free already, O Messenger of God.",
     "O da: Onu zaten azat ettim, ey Allah'ın Resûlü! dedi.",
 [QALA_HID(AB, pre=("fa",)), QAD(),
  VERB("أَعْتَقْتُهُ", "ataqa-free", "mtu", form="form-iv-verbs", enc="هُ", encref=BL), YA(),
  *RASUL("munada", "nasb", salla=False, p=".", note=(" — مُنَادًى مُضَافٌ", " — a called noun that is annexed", " — muzâf münâdâ"))]),
]
CHAPS = [S1, S2]
NEW_GLOSS = {
 "bilal": NP("بِلَال", "Bilāl ibn Rabāḥ, the Prophet's muezzin", "Bilâl b. Rebâh, Peygamber'in müezzini"),
 "awn-name": NP("عَوْن", "ʿAwn — in «Ibn ʿAwn», the Baṣran ʿAbd Allāh ibn ʿAwn", "Avn — «İbn Avn»da; Basralı Abdullah b. Avn"),
 "arim": NP("عَارِم", "ʿĀrim — the nickname of Muḥammad ibn al-Faḍl al-Sadūsī", "Ârim — Muhammed b. el-Fadl es-Sedûsî'nin lakabı"),
 "ansari": NN("أَنْصَارِيّ", "ن ص ر", "of the Anṣār (a nisba)", "Ensârî (nisbe)"),
 "matta": NV("مَطَّ", "م ط ط", "I", "to stretch out", "uzatmak, germek"),
 "batha": NN("بَطْحَاء", "ب ط ح", "the pebbles of a stream-bed; a pebbly valley", "sel yatağının çakılları; çakıllı vadi"),
 "lat": NP("اللَّات", "al-Lāt, an idol of the pagan Arabs", "Lât, Arap müşriklerinin putu"),
 "uzza": NP("الْعُزَّى", "al-ʿUzzā, an idol of the pagan Arabs", "Uzzâ, Arap müşriklerinin putu"),
 "uqiyya": NN("أُوقِيَّة", "و ق ي", "an ounce (of silver, forty dirhams); pl. أَوَاقٍ", "ukiyye (kırk dirhem gümüş); çoğ. evâk"),
 "shirka": NN("شَرِكَة", "ش ر ك", "a share, partnership", "ortaklık, pay"),
}
GLOSS_HERE = {"ayyub": ("Ayyūb (al-Sakhtiyānī, the Baṣran Successor)", "Eyyûb (es-Sahtiyânî, Basralı tâbiî)"), "hammad-name": ("Ḥammād (ibn Zayd)", "Hammâd (b. Zeyd)")}
V_NEW = {"matta": FROM_PARADIGM("radda", {"ر": "م", "د": "ط"}, note="مُضَاعَفٌ مِنْ بَابِ نَصَرَ: مَطَّهُ يَمُطُّهُ مَطًّا؛ الْمَجْهُولُ مُطَّ.")}
MANIFEST = manifest(SLUG, 3, {"ar": "أَحَدٌ أَحَدٌ", "en": "One! One!", "tr": "Bir! Bir!"},
  {"ar": "بِلَالٌ فِي الْعَذَابِ وَأَبُو بَكْرٍ يَشْتَرِيهِ", "en": "Bilāl under torment, and Abū Bakr buys him free", "tr": "İşkence altındaki Bilâl ve onu satın alıp azat eden Ebû Bekir"}, "sahaba",
  "Bilāl ibn Rabāḥ's entry, vol. 3, printed p. 175 (Shamela p. 853)", "Bilâl b. Rebâh maddesi, cilt 3, matbû s. 175 (Şâmile s. 853)", "تَرْجَمَةُ بِلَالِ بْنِ رَبَاحٍ، الْجُزْءُ ٣، ص ١٧٥ (الشَّامِلَةُ ص ٨٥٣)",
  "two consecutive akhbār, each whole with its isnād: ʿUmayr ibn Isḥāq's («قال: أخبرنا عثمان بن عمر» … «إن لساني لا يحسنه.») and Muḥammad ibn Sīrīn's («قال: أخبرنا عارم بن الفضل» … «قد أعتقته يا رسول الله.»), one chapter each",
  "art arda iki haber, her biri isnadıyla tam: Umeyr b. İshâk'ınki («قال: أخبرنا عثمان بن عمر» … «إن لساني لا يحسنه.») ve Muhammed b. Sîrîn'inki («قال: أخبرنا عارم بن الفضل» … «قد أعتقته يا رسول الله.»); her biri bir bölüm",
  "خَبَرَانِ مُتَتَالِيَانِ بِإِسْنَادَيْهِمَا: خَبَرُ عُمَيْرِ بْنِ إِسْحَاقَ وَخَبَرُ مُحَمَّدِ بْنِ سِيرِينَ، لِكُلٍّ مِنْهُمَا فَصْلٌ",
  kept=[("«اهله» بِلَا هَمْزٍ وَ«علا م» مَفْصُولَةً كَمَا فِي النَّصِّ الْإِلِكْتُرُونِيِّ، وَكُتِبَتَا هُنَا «أَهْلُهُ» وَ«عَلَامَ» بِالْحُرُوفِ نَفْسِهَا", "the e-text's «اهله» (no hamza seat) and «علا م» (split) are written أَهْلُهُ and عَلَامَ — the same letters", "e-metnin «اهله» (hemzesiz) ve «علا م» (ayrık) yazımı aynı harflerle أَهْلُهُ ve عَلَامَ yazıldı")],
  hoca=[("«الشَّرِكَة» — its last vowel left unwritten (nasb by a dropped verb, or raf')", "«الشَّرِكَة» — son harekesi yazılmadı (mahzûf fiille nasb ya da ref)"),
        ("«فَمَطُّوهُ» read from مَطَّ «to stretch out» (the e-text فمطوه)", "«فَمَطُّوهُ» «uzattı» anlamındaki مَطَّ'dan okundu (e-metin فمطوه)"),
        ("«عَارِمُ بْنُ الْفَضْلِ» — the laqab with the father's name, as printed", "«عَارِمُ بْنُ الْفَضْلِ» — lakap babanın adıyla, baskıdaki gibi")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V_NEW)
