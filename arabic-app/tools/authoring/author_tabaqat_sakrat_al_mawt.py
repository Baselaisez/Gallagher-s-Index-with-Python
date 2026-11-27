"""Author content/samples/tabaqat-sakrat-al-mawt — «وَجَاءَتْ سَكْرَةُ الْمَوْتِ بِالْحَقِّ», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Companions, Abū Bakr's entry (his death), vol. 3 p. 146 (Shamela
p. 824): ʿĀʾisha's khabar through ʿAbd Allāh al-Bahī, whole with its isnād — «قال: أخبرنا وكيع بن الجراح وعبد الله بن نمير» … «إلى الجديد من
الميت.» — with Ḥātim al-Ṭāʾī's verse and Qāf 50:19 as the text quotes them (the Qurʾān in Ḥafṣ's reading, as the e-text vowels it).
The exact passage: research/sources/tabaqat-sakrat-al-mawt-src.txt. No correction. Every vowel outside the Qurʾān is ours.
Run: python3 tools/authoring/author_tabaqat_sakrat_al_mawt.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-sakrat-al-mawt"
AB = ("أَبِي بَكْرٍ", "Abū Bakr", "Ebû Bekir")
AI = ("عَائِشَةَ", "ʿĀʾisha", "Âişe")
AKH = H("بِـ«أَخْبَرَنَا»", "«told us»", "«ahberanâ»ya")
NAFS = ("النَّفْسِ، وَلَمْ تُذْكَرْ لِلْعِلْمِ بِهَا", "the soul, unnamed because it is understood", "can (zikredilmedi, bilindiği için)")
TITLES = [{"ar": "وَجَاءَتْ سَكْرَةُ الْمَوْتِ بِالْحَقِّ", "en": "And the stupor of death came in truth", "tr": "Ölüm sarhoşluğu hak ile geldi"}]
S1 = [
 SEN(1, "He said: Wakīʿ ibn al-Jarrāḥ, ʿAbd Allāh ibn Numayr and Yaʿlā ibn ʿUbayd told us, from Ismāʿīl ibn Abī Khālid, from ʿAbd Allāh al-Bahī, the client of al-Zubayr, from ʿĀʾisha, who said:",
     "Dedi ki: Bize Vekî' b. el-Cerrâh, Abdullah b. Numeyr ve Ya'lâ b. Ubeyd, İsmâil b. Ebî Hâlid'den, o Zübeyr'in mevlâsı Abdullah el-Behî'den, o Âişe'den haber verdiler; o dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("وَكِيعُ", "waki", "fail", note=NT), BN("raf", ("وَكِيعُ", "Wakīʿ", "Vekî'")), NAME("الْجَرَّاحِ", "jarrah", "mi"),
  NOUN("وَعَبْدُ", "abd", "atf", "raf", pre=("wa",), mudaf=True), ALLAH_MI(), BN("raf", ("عَبْدُ اللهِ", "ʿAbd Allāh", "Abdullah")), NAME("نُمَيْرٍ", "numayr", "mi"),
  NAME("وَيَعْلَى", "yala", "atf", "raf", pre=("wa",), sign="maq", dipt="wazn", note=NT), BN("raf", ("يَعْلَى", "Yaʿlā", "Ya'lâ")), NAME("عُبَيْدٍ", "ubayd-name", "mi"),
  AN(hang=AKH), NAME("إِسْمَاعِيلَ", "ismail", "majr", by="عَنْ", dipt="ujma"), BN("jarr", ("إِسْمَاعِيلَ", "Ismāʿīl", "İsmâil")), NOUN("أَبِي", "ab", "mi", sign="5", mudaf=True), NAME("خَالِدٍ", "khalid", "mi"),
  AN(hang=AKH), NOUN("عَبْدِ", "abd", "majr", by="عَنْ", mudaf=True), ALLAH_MI(), NOUN("الْبَهِيِّ", "bahi", "naat", "jarr", of=("عَبْدِ اللهِ", "ʿAbd Allāh", "Abdullah"), note=(" — لَقَبُهُ", " — his byname", " — lakabı")),
  NOUN("مَوْلَى", "mawla", "naat", "jarr", sign="maq", mudaf=True, of=("عَبْدِ اللهِ", "ʿAbd Allāh", "Abdullah")), NAME("الزُّبَيْرِ", "zubayr", "mi"),
  AN(hang=AKH), NAME("عَائِشَةَ", "aisha", "majr", by="عَنْ", dipt="tanith"), QALAT_HID(AI)]),
 SEN(2, "When death came to Abū Bakr, I spoke a line of Ḥātim's saying:",
     "Ebû Bekir'e ölüm hâli geldiğinde, Hâtim'in sözünden bir beyit söyledim:",
 [PART("لَمَّا", "lamma", "ظَرْفٌ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِجَوَابِهِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
       "An adverb meaning «when», built on sukūn in the seat of nasb, hanging on its answer, annexed to the clause after it.", "«-ınca» anlamında zarf, mahallen mansûb; cevabına müteallik, sonraki cümleye muzâf.", ["maful-fih"]),
  VERB("حُضِرَ", "hadara", "p", g=["naib-al-fail"], doer_after=True, note=(" — حُضِرَ: حَضَرَهُ الْمَوْتُ", " — ḥuḍira: death came to him", " — huzira: ona ölüm geldi"), cl=LAMMA_SHART),
  NOUN("أَبُو", "ab", "naib", sign="5", mudaf=True), NAME("بَكْرٍ", "bakr", "mi"),
  VERB("قُلْتُ", "qala", "mtu", g=["hollow-verbs"], cl=JAWAB_LAMMA), NOUN("كَلِمَةً", "kalima", "maful", note=(" — يَعْنِي بَيْتًا", " — i.e. a line of verse", " — yani bir beyit")),
  PREPT("مِنْ", "min", H("بِمَحْذُوفٍ نَعْتٍ لِـ«كَلِمَةً»", "an omitted adjective of «a word»", "«kelimeten»in mahzûf na'tına"), ("، لِلتَّبْعِيضِ", " of part", " (teb'îz)")),
  NOUN("قَوْلِ", "qawl", "majr", mudaf=True), NAME("حَاتِمٍ", "hatim", "mi", p=":", note=(" — حَاتِمٌ الطَّائِيُّ", " — Ḥātim al-Ṭāʾī", " — Hâtim et-Tâî"))]),
 SEN(3, "By your life, wealth avails a man nothing when one day it rattles and the breast is strait with it.",
     "Ömrüne andolsun, servet yiğide fayda vermez; bir gün can hırıldayıp göğüs onunla daraldığında.",
 [PART("لَعَمْرُكَ", "amr-qasam", "اللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْخَبَرُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي — وَالْعَمْرُ: الْعُمُرُ.",
       "The lam of the opening; «life» is the mubtadaʾ, annexed to «your»; its khabar is necessarily dropped: «(by) your life (is my oath)».",
       "İbtidâ lâmı; «amr» mübtedâ, «ke»ye muzâf; haberi vücûben mahzûf: «ömrün (yeminimdir)».", ["mubtada-khabar", "hadhf-wa-taqdir", "huruf-al-qasam-fil-kafiya"], pre=("la",), enc="كَ", pos="noun", s="amr-qasam", spos="noun"),
  PART("مَا", "ma-nafiya", "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "مَا negates.", "«Mâ» nefy harfi.", ["anwa-ma"]),
  VERB("يُغْنِي", "aghna", "uy", form="form-iv-verbs", g=["naqis-verbs"], doer_after=True, cl=(" — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا", "; the clause answers the oath and has no seat", "; cümle kasemin cevabı, mahalli yok")),
  NOUN("الثَّرَاءُ", "tharaa", "fail", note=(" — الثَّرَاءُ: كَثْرَةُ الْمَالِ", " — tharāʾ: abundant wealth", " — serâ: malın çokluğu")),
  PREPT("عَنِ", "an", H("بِـ«يُغْنِي»", "«avails»", "«yugnî»ye"), ("، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", ", voweled with kasra before the sukūn", " (iki sâkin karşılaştığı için kesre)")),
  NOUN("الْفَتَى", "fata-youth", "majr", sign="maq", p="•"),
  PART("إِذَا", "idha", "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ، وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.",
       "إِذَا «when», an adverb of time carrying a condition, annexed to its clause; its answer is dropped, shown by what came before.", "«İzâ» şart anlamı taşıyan zaman zarfı, sonraki cümleye muzâf; cevabı mahzûf, öncesi ona delâlet eder.", ["maful-fih", "idha-shartiyya"], pos="noun"),
  VERB("حَشْرَجَتْ", "hashraja", "mt", form="rubai-babs", hid="هِيَ", ref=NAFS, note=(" — الْحَشْرَجَةُ: تَرَدُّدُ النَّفَسِ فِي الصَّدْرِ عِنْدَ الْمَوْتِ", " — ḥashraja: the death-rattle of the breath in the chest", " — haşrece: ölüm anında nefesin göğüste hırıldaması"),
       cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "; the clause is in the seat of jarr, annexed to إِذَا", "; cümle «izâ»ya muzâfun ileyh")),
  NOUN("يَوْمًا", "yawm", "zarf", note=(" — ظَرْفُ زَمَانٍ مُتَعَلِّقٌ بِـ«حَشْرَجَتْ»", " — of time, hanging on «rattles»", " — zaman zarfı, «haşracet»e müteallik")),
  VERB("وَضَاقَ", "daqa", "m", g=["hollow-verbs"], doer_after=True, pre=("wa",)),
  PRON_J("بِهَا", "bi", "هَا", H("بِـ«ضَاقَ»", "«is strait»", "«dâka»ya"), ref=NAFS), NOUN("الصَّدْرُ", "sadr", "fail", p=".")]),
 SEN(4, "He said: Do not say so, my little daughter, but say: «And the stupor of death has come in truth: that is what you used to shun.»",
     "Dedi ki: Böyle söyleme kızcağızım; fakat şöyle de: «Ölüm sarhoşluğu hak ile geldi; işte bu, senin kaçıp durduğun şeydir.»",
 [QALA_HID(AB, pre=("fa",)),
  PART("لَا", "la-nahiya", "حَرْفُ نَهْيٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "لَا of forbidding, which puts the verb in jazm.", "Nehiy «lâ»sı, câzim.", ["la-nahiya"]),
  tok("تَقُولِي", "qala", "verb", ["hollow-verbs", "afal-khamsa", "la-nahiya"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَا» النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "A present verb in jazm after the forbidding لَا, by dropping the nūn (one of the five verbs); the ya of the woman addressed is its doer.",
      "Nehiy «lâ»sıyla meczûm muzâri, nûnun hazfiyle (ef'âl-i hamse); muhâtaba yâsı fâildir, mahallen merfû.", segments=[seg("تَقُولِ", "qala", "verb"), seg("ي", "pron-2fs", "pron")]),
  PART("هٰكَذَا", "hakadha", "الْهَاءُ لِلتَّنْبِيهِ، وَالْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَصْدَرٍ مَحْذُوفٍ: قَوْلًا هٰكَذَا.",
       "ها draws attention, the kaf «like» is a jarr letter, ذَا «this» is in its seat of jarr — «(a saying) like this».", "«Hâ» tenbîh, kâf teşbih cer harfi, «zâ» işaret ismi mahallen mecrûr — «böyle (bir söz)».", ["huruf-tanbih", "huruf-jarr", "asma-al-ishara-wa-sighuha"], pos="pron"),
  YA(), NOUN("بُنَيَّةُ", "bunayya", "munada", note=(" — مُنَادًى مُفْرَدٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — تَصْغِيرُ بِنْتٍ لِلتَّحَبُّبِ", " — a single called noun, built on ḍamma in the seat of nasb — the diminutive of bint, of endearment", " — müfred münâdâ, damme üzere mebnî, mahallen mansûb — sevgi için «bint»in tasgîri")),
  PART("وَلٰكِنْ", "lakin", "الْوَاوُ عَاطِفَةٌ، وَلٰكِنْ حَرْفُ اسْتِدْرَاكٍ مُخَفَّفٌ لَا عَمَلَ لَهُ.", "The waw conjoins; لٰكِنْ «but», the light particle of correction, governing nothing.", "Vâv atıf; «lâkin» muhaffef istidrâk harfi, amel etmez.", ["aw-imma-am-la-bal-lakin-fil-kafiya"], pre=("wa",)),
  tok("قُولِي", "qala", "verb", ["hollow-verbs", "imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَمَا بَعْدَهُ مَقُولُ الْقَوْلِ.", "An imperative built on dropping the nūn; the ya of the woman addressed is its doer — what follows is what is said.",
      "Nûnun hazfi üzere mebnî emir; muhâtaba yâsı fâil — sonrası mekūlü'l-kavl.", punct=":", segments=[seg("قُولِ", "qala", "verb"), seg("ي", "pron-2fs", "pron")]),
  *QURAN([
   VERB("وَجَاءَتْ", "jaa", "mt", g=["hollow-verbs", "mahmuz-verbs"], doer_after=True, pre=("wa-isti",)),
   NOUN("سَكْرَةُ", "sakra", "fail", mudaf=True, note=(" — السَّكْرَةُ: شِدَّةُ الْمَوْتِ وَغَمْرَتُهُ", " — sakra: the stupor, the throes of death", " — sekre: ölümün şiddeti ve baygınlığı")), NOUN("الْمَوْتِ", "mawt", "mi"),
   NOUN("بِالْحَقِّ", "haqq", "majr", pre=("bi",), note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ، أَوْ بِـ«جَاءَتْ»", " — the phrase hangs on an omitted ḥāl, or on «came»", " — câr-mecrûr mahzûf hâle ya da «câet»e müteallik")),
   ISHARA_T("ذٰلِكَ", "dhalika", "فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "in the seat of raf' as the mubtadaʾ", "mahallen merfû mübtedâ", g=["mubtada-khabar"]),
   PART("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرٌ.", "A relative noun «what», in the seat of raf' as the khabar.", "İsm-i mevsûl «mâ», mahallen merfû haber.", ["ism-mawsul", "mubtada-khabar"], pos="pron"),
   VERB("كُنْتَ", "kana", "mta", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ، وَالتَّاءُ اسْمُهُ", " — defective; the ta is its noun", " — nâkıs; tâ ismi"), cl=SILA_),
   PRON_J("مِنْهُ", "min", "هُ", H("بِـ«تَحِيدُ»", "«shun»", "«tahîdu»ya"), ref=("«مَا»", "«what»", "«mâ»")),
   VERB("تَحِيدُ", "hada-swerve", "u", g=["hollow-verbs"], hid="أَنْتَ", cl=KH_KANA, note=(" — حَادَ عَنْهُ: مَالَ وَعَدَلَ", " — ḥāda ʿan: to swerve from", " — hâde an: kaçındı, saptı"), p=".")])]),
 SEN(5, "Look at these two sheets of mine: when I die, wash it and shroud me in the two of them, for the living has more need of the new than the dead.",
     "Şu iki çarşafıma bakın; öldüğümde onu yıkayın ve beni o ikisine kefenleyin; çünkü diri, yeniye ölüden daha muhtaçtır.",
 [VERB("انْظُرُوا", "nazara", "amrw", note=(" — وَالْخِطَابُ لِأَهْلِهِ", " — addressed to his family", " — ailesine hitap")),
  NOUN("مُلَاءَتَيَّ", "mulaa", "maful", sign="du", note=("، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَحُذِفَتْ نُونُ الْمُثَنَّى لِلْإِضَافَةِ وَأُدْغِمَتْ يَاؤُهُ فِي يَاءِ الْمُتَكَلِّمِ", ", annexed to the ya «my» — the dual's nūn dropped and its ya merged into the speaker's", ", mütekellim yâsına muzâf — tesniye nûnu düştü ve yâsı idgâm edildi")),
  ISHARA_T("هَاتَيْنِ", "hatani", "— نَعْتٌ لِـ«مُلَاءَتَيَّ» مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى", "— an adjective of «my two sheets», in nasb by the ya (declined like a dual)", "— «iki çarşafım»ın na'tı, yâ ile mansûb (tesniyeye mülhak)", built="الْيَاءِ لَفْظًا", g=["naat-sifa"]),
  PART("فَإِذَا", "idha", "الْفَاءُ عَاطِفَةٌ، وَإِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ غَيْرُ جَازِمٍ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ الشَّرْطِ.",
       "The fa conjoins; إِذَا «when», an adverb of time carrying a condition, annexed to the condition's clause.", "Fâ atıf; «izâ» şart anlamı taşıyan, cezmetmeyen zaman zarfı, şart cümlesine muzâf.", ["maful-fih", "idha-shartiyya"], pre=("fa",), pos="noun"),
  VERB("مِتُّ", "mata-die", "mtu", g=["hollow-verbs"], note=(" — وَأُدْغِمَتْ لَامُهُ فِي التَّاءِ، وَكُسِرَتْ فَاؤُهُ لُغَةً", " — its last radical merged into the ta; the kasra on its first letter is a recognised usage", " — lâmı tâya idgâm edildi; fâsındaki kesre bir lügattir"),
       cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "; the clause is in the seat of jarr, annexed to إِذَا", "; cümle «izâ»ya muzâfun ileyh")),
  tok("فَاغْسِلُوهَا", "ghasala", "verb", ["imperative-amr", "al-bariz-al-muttasil", "maful-bihi"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «إِذَا»، وَاغْسِلُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالْأَلِفُ الْفَارِقَةُ حُذِفَتْ خَطًّا، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ (كَذَا فِي النَّصِّ بِالْإِفْرَادِ) — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ لَا مَحَلَّ لَهَا.",
      "The fa opens the answer of إِذَا; «wash» is an imperative built on dropping the nūn, the waw its doer; «it» (singular, so the text) is its object — the answer, with no seat.",
      "Fâ «izâ»nın cevabında; «iğsilû» nûnun hazfi üzere mebnî emir, vâv fâil; «hâ» (metinde böyle tekil) mef'ûlün bih — cevap cümlesi, mahalli yok.",
      segments=[seg("فَ", "fa", "conj"), seg("اغْسِلُو", "ghasala", "verb"), seg("هَا", "pron-3fs", "pron")]),
  tok("وَكَفِّنُونِي", "kaffana", "verb", ["imperative-amr", "form-ii-verbs", "ya-al-mutakallim", "maful-bihi", "atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَكَفِّنُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "The waw conjoins; «shroud» is an imperative built on dropping the nūn, the waw its doer; the nūn guards it and the ya («me») is its object.",
      "Vâv atıf; «keffinû» nûnun hazfi üzere mebnî emir, vâv fâil; nûn vikâye, yâ (beni) mef'ûlün bih.",
      segments=[seg("وَ", "wa", "conj"), seg("كَفِّنُو", "kaffana", "verb"), seg("نِي", "pron-1s", "pron")]),
  PRON_J("فِيهِمَا", "fi", "هِمَا", H("بِـ«كَفِّنُوا»", "«shroud»", "«keffinû»ya"), ref=("الْمُلَاءَتَيْنِ", "the two sheets", "iki çarşaf")),
  PART("فَإِنَّ", "inna", "الْفَاءُ تَعْلِيلِيَّةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ.", "The fa gives the reason; إِنَّ puts its noun in nasb.", "Fâ ta'lîl içindir; «inne» te'kîd ve nasb harfi.", ["inna-wa-akhawatuha"], pre=("fa",)),
  NOUN("الْحَيَّ", "hayy", "isminna"), NOUN("أَحْوَجُ", "ahwaj", "khinna", g=["ism-tafdil"], note=(" — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ التَّنْوِينِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", " — an elative, barred from tanwin (an adjective on a verb's pattern)", " — ism-i tafdîl, tenvinsiz (vasfiyet ve fiil vezni)")),
  PREPT("إِلَى", "ila", H("بِـ«أَحْوَجُ»", "«more in need»", "«ahvecu»ya")), NOUN("الْجَدِيدِ", "jadid", "majr"),
  PREPT("مِنَ", "min", H("بِـ«أَحْوَجُ»", "«more in need»", "«ahvecu»ya"), ("، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ", ", voweled with fatḥa before the sukūn", " (iki sâkin karşılaştığı için fetha)")),
  NOUN("الْمَيِّتِ", "mayyit", "majr", p=".")]),
]
CHAPS = [S1]
NEW_GLOSS = {
 "numayr": NP("نُمَيْر", "Numayr — a man's name (ʿAbd Allāh ibn Numayr's father)", "Numeyr — erkek adı (Abdullah b. Numeyr'in babası)"),
 "yala": NP("يَعْلَى", "Yaʿlā — a man's name (Yaʿlā ibn ʿUbayd al-Ṭanāfisī)", "Ya'lâ — erkek adı (Ya'lâ b. Ubeyd et-Tanâfisî)"),
 "bahi": NN("بَهِيّ", "ب ه و", "al-Bahī — a byname («the handsome»)", "el-Behî — lakap («güzel yüzlü»)"),
 "tharaa": NN("ثَرَاء", "ث ر و", "wealth, abundance of goods", "servet, mal çokluğu"),
 "hashraja": NV("حَشْرَجَ", "ح ش ر ج", "Q", "to rattle in the throat (of the dying breath)", "can çekişirken hırıldamak"),
 "bunayya": NN("بُنَيَّة", "ب ن و", "little daughter (diminutive of بِنْت)", "kızcağız (bint'in tasgîri)"),
 "sakra": NN("سَكْرَة", "س ك ر", "a stupor; the throes (of death)", "sarhoşluk; (ölüm) baygınlığı"),
 "hada-swerve": NV("حَادَ", "ح ي د", "I", "to swerve from, to shun (with عَنْ / مِنْ)", "sapmak, kaçınmak"),
 "hatani": {"lemma": "هَاتَانِ", "pos": "pron", "gloss": {"en": "these two (fem.) — the dual of هٰذِهِ; هَاتَيْنِ in nasb and jarr", "tr": "bu ikisi (müen.) — hâzihî'nin tesniyesi; nasb ve cerde hâteyni"}, "level": 4},
 "kaffana": NV("كَفَّنَ", "ك ف ن", "II", "to shroud (a dead body)", "kefenlemek"),
 "ahwaj": NN("أَحْوَج", "ح و ج", "more in need (elative)", "daha muhtaç (ism-i tafdîl)"),
}
GLOSS_HERE = {"nazara": ("to look at", "bakmak"), "khalid": ("Khālid — in «Ismāʿīl ibn Abī Khālid»", "Hâlid — «İsmâil b. Ebî Hâlid»de")}
V_NEW = {"hashraja": SG.derived("الرُّبَاعِيُّ الْمُجَرَّدُ: فَعْلَلَ يُفَعْلِلُ فَعْلَلَةً", "فَعْلَلَ يُفَعْلِلُ", "ُ", "حَشْرَج", "حَشْرِج", "حَشْرِج", "حَشْرَجَة", "مُحَشْرِج", None, None, None, "رُبَاعِيٌّ مُجَرَّدٌ: حَشْرَجَ يُحَشْرِجُ حَشْرَجَةً."),
         "hada-swerve": SG.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "حَاد", "حِد", "حِيد", "حِد", "حِيد", "حِد", "حَيْد", "حَائِد", None, None, None, "أَجْوَفُ يَائِيٌّ: حَادَ يَحِيدُ حَيْدًا."),
         "kaffana": SG.derived(SG.B2, SG.W2, "ُ", "كَفَّن", "كَفِّن", "كَفِّن", "تَكْفِين", "مُكَفِّن", "مُكَفَّن", "كُفِّنَ", "يُكَفَّنُ", "كَفَّنَ الْمَيِّتَ يُكَفِّنُهُ تَكْفِينًا.")}
MANIFEST = manifest(SLUG, 6, {"ar": "وَجَاءَتْ سَكْرَةُ الْمَوْتِ بِالْحَقِّ", "en": "And the Stupor of Death Came in Truth", "tr": "Ölüm Sarhoşluğu Hak ile Geldi"},
  {"ar": "أَبُو بَكْرٍ عِنْدَ الْمَوْتِ، وَبَيْتُ حَاتِمٍ", "en": "Abū Bakr at his death, and Ḥātim's verse", "tr": "Ölüm döşeğinde Ebû Bekir ve Hâtim'in beyti"}, "sahaba",
  "Abū Bakr's entry, vol. 3, printed p. 146 (Shamela p. 824)", "Ebû Bekir maddesi, cilt 3, matbû s. 146 (Şâmile s. 824)", "تَرْجَمَةُ أَبِي بَكْرٍ، الْجُزْءُ ٣، ص ١٤٦ (الشَّامِلَةُ ص ٨٢٤)",
  "ʿĀʾisha's khabar through ʿAbd Allāh al-Bahī, whole with its isnād, from «قال: أخبرنا وكيع بن الجراح وعبد الله بن نمير» to «إلى الجديد من الميت.»; Ḥātim al-Ṭāʾī's verse and Qāf 50:19 (Ḥafṣ, vowelled as the e-text vowels it) as the text quotes them",
  "Âişe'nin Abdullah el-Behî yoluyla gelen haberi, isnadıyla tam, «قال: أخبرنا وكيع بن الجراح وعبد الله بن نمير»den «إلى الجديد من الميت.»e kadar; Hâtim et-Tâî'nin beyti ve Kāf 50:19 (Hafs; e-metnin harekelediği gibi) metnin aktardığı şekilde",
  "خَبَرُ عَائِشَةَ مِنْ طَرِيقِ عَبْدِ اللهِ الْبَهِيِّ كُلُّهُ بِإِسْنَادِهِ، وَفِيهِ بَيْتُ حَاتِمٍ وَآيَةُ ق: ١٩",
  kept=[("«فاغسلوها» بِضَمِيرِ الْمُفْرَدِ وَ«فيهما» بِضَمِيرِ الْمُثَنَّى كَمَا فِي النَّصِّ", "«فاغسلوها» with a singular pronoun beside «فيهما» with a dual one, as the text has them", "«فاغسلوها» tekil zamirle, «فيهما» tesniye zamiriyle, metindeki gibi")],
  hoca=[("«حُضِرَ» read in the passive («death came to him»; or the active حَضَرَ)", "«حُضِرَ» meçhul okundu («ona ölüm geldi»; ya da malûm حَضَرَ)"),
        ("«مِتُّ» with kasra (also مُتُّ)", "«مِتُّ» kesreyle (مُتُّ de okunur)"),
        ("«فَاغْسِلُوهَا»: the singular pronoun kept, the two sheets meant", "«فَاغْسِلُوهَا»: tekil zamir korundu; kastedilen iki çarşaf")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V_NEW)
