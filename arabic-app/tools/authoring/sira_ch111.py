"""al-Nadwī, al-Sīra al-Nabawiyya — chapter 111: «قصّة الراهب بحيرى» (3), Shamela p. 157, printed p. 165: «وممّا يقدح في هذا الحديث» to
«(انتهى كلام العلامة النعماني).» — Bilāl in the report, and Ibn al-Qayyim's judgement in Zād al-Maʿād."""
from sira_common import *

N_ = 111
TITLE = {"ar": "قِصَّةُ الرَّاهِبِ بَحِيرَى (٣)", "en": "The Story of the Monk Baḥīrā (3)", "tr": "Rahip Bahîrâ'nın Kıssası (3)"}
META = {"pages": "165", "en": "Bilāl in the report (s1); Ibn al-Qayyim: a plain error (s2–s4); the end of Shiblī's words (s5)",
        "tr": "rivayette Bilâl (s1); İbn Kayyim: açık bir hata (s2–s4); Şiblî'nin sözünün sonu (s5)"}
HOCA = [("ch. 111 s3: «وَأَنَّهُ مِنَ الْغَلَطِ الْوَاضِحِ» — the print writes «وأنّه» (hamza above, fatḥ), read conjoined; the sense (Ibn al-Qayyim's own verdict; Zād al-Maʿād «وهو من الغلط») wants «وَإِنَّهُ», a new clause", "Bölüm 111 s3: «ve ennehû mine'l-galati'l-vâzıh» — baskı «وأنّه» yazar (üstte hemze, fetha), ma'tûf okundu; mâna (İbn Kayyim'in kendi hükmü; Zâdü'l-meâd «وهو من الغلط») yeni cümle «ve innehû» ister")]
LEFT = [("ch. 111 s2: the print's reference «(١/ ١٨)» after «زَادِ الْمَعَادِ» rides as printed (no tokens: numerals)", "Bölüm 111 s2: baskıdaki «(١/ ١٨)» atfı «Zâdü'l-meâd»dan sonra basıldığı gibi durur (rakam)")]
ALLAH_MI = lambda p=None: T("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The name of Allah, the second term of the idafa, in jarr.", "Lafza-i celâl, muzâfun ileyh, mecrûr.", p=p)
BILAL = lambda full, case, role, p=None: T(full, "bilal", "propn", role[0],
    role[1] + " " + D[case] + " — عَلَمٌ مَصْرُوفٌ.", role[2] + ", in " + CE[case] + " — a declined name: «Bilāl».", role[3] + ", " + CT[case] + " — munsarif alem: «Bilâl».", p=p)

S = [
 SEN(1, "Among what tells against this ḥadīth is that it says Abū Ṭālib sent the Messenger of Allah — Allah bless him and grant him peace — back with Bilāl;",
     "Bu hadîse halel getiren şeylerden biri de, onda Ebû Tâlib'in Resûlullah'ı — sallallâhu aleyhi ve sellem — Bilâl ile gönderdiğinin geçmesidir;",
 [T("وَمِمَّا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul", "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمِنْ حَرْفُ جَرٍّ لِلتَّبْعِيضِ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ" + J("بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ") + ".",
    "The waw resumes; مِنْ «among» with مَا «what», a relative in the seat of jarr — the phrase is the fronted predicate.", "Vâv isti'nâf içindir; teb'îz için «min» ile «mâ» ism-i mevsûl, mahallen mecrûr — câr-mecrûr öne alınmış habere müteallik.",
    segs=[("وَ", "wa", "conj"), ("مِ", "min", "prep"), ("مَّا", "ma-mawsula", "pron")]),
  T("يَقْدَحُ", "qadaha-impugn", "verb", ["thulathi-mujarrad-babs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا؛ وَقَدَحَ فِيهِ: عَابَهُ وَطَعَنَ فِيهِ.",
    "A present verb in raf' «tells against»; its doer the hidden «it» (the «what») — the clause is the ṣila; قَدَحَ فِي: to impugn.", "Merfû muzâri «halel getirir»; fâili gizli «hüve» («mâ») — cümle sıladır; kadaha fîhi: onu yaraladı, tenkit etti."),
  P_("فِي"),
  T("هٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara-wa-sighuha"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِـ«فِي»" + J("بِـ«يَقْدَحُ»") + ".", "A demonstrative «this», built, in the seat of jarr after فِي — the phrase hangs on «tells against».", "İsm-i işaret «bu», mebnî, «fî» ile mahallen mecrûr — câr-mecrûr «yakdahu»ya müteallik."),
  T("الْحَدِيثِ", "hadith", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A substitute for the demonstrative, in jarr: «(this) ḥadīth».", "İsm-i işaretten bedel, mecrûr: «(bu) hadîs»."),
  T("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ» — وَ«أَنَّ» وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
    "أَنَّ with the pronoun of the matter as its noun — it and its clause stand for a masdar, the mubtada placed after its predicate.", "«Enne»; zamir şe'n zamiri, ismidir — kendisi ve sonrası sonraya bırakılmış mübtedâ olan masdar yerinde.", segs=[("أَنَّ", "anna", "part"), ("هُ", "pron-3ms", "pron")]),
  T("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "قَدْ confirms the past verb.", "«Kad» tahkîk harfi."),
  T("جَاءَ", "jaa", "verb", ["hollow-verbs", "mahmuz-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» الثَّانِيَةِ؛ وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ» الْأُولَى.", "A past verb «it says (has come)» — its doer is the masdar made by the second «that»; the clause is the predicate of the first أَنَّ.", "Mâzî «geçti» — fâili ikinci «enne»den te'vîl edilen masdardır; cümle birinci «enne»nin haberi."),
  JP("فِيهِ", "fi", "هِ", ("جَاءَ", "says", "câe"), ("الْحَدِيثِ", "it (the ḥadīth)", "hadîs"), "in it", "onda"),
  T("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَ«أَنَّ» وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ فِي مَحَلِّ رَفْعٍ فَاعِلُ «جَاءَ».", "أَنَّ «that» — it and its clause stand for a masdar, the doer of «says».", "«Enne» — kendisi ve sonrası «câe»nin fâili olan masdar yerinde."),
  T("أَبَا", "ab", "noun", ["inna-wa-akhawatuha", "five-nouns", "idafa-definiteness"], "اسْمُ «أَنَّ» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْأَلِفُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb by the alif (one of the five nouns), annexed.", "«Enne»nin ismi, elif ile mansûb, muzâf."),
  MI("طَالِبٍ", "talib-name", "Ṭālib", "Tâlib"),
  T("أَرْسَلَ", "arsala", "verb", ["form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى أَبِي طَالِبٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».", "A past verb «sent»; its doer the hidden «he» (Abū Ṭālib) — the clause is the predicate of أَنَّ.", "Mâzî «gönderdi»; fâili gizli «hüve» (Ebû Tâlib) — cümle «enne»nin haberi."),
  T("رَسُولَ", "rasul", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The object, in nasb, annexed.", "Mef'ûlün bih, mansûb, muzâf."), ALLAH_MI(), *SAW(),
  T("مَعَ", "maa", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ دَالٌّ عَلَى الْمُصَاحَبَةِ، مُضَافٌ، مُتَعَلِّقٌ بِـ«أَرْسَلَ».", "An adverb «with», in nasb, annexed — it hangs on «sent».", "Zarf «ile», mansûb, muzâf — «ersele»ye müteallik."),
  BILAL("بِلَالٍ", "jarr", (["idafa-definiteness"], "مُضَافٌ إِلَيْهِ", "The second term of the idafa", "Muzâfun ileyh"), p="،")]),
 SEN(2, "The learned Ibn al-Qayyim says in «Zād al-Maʿād» (1/18):",
     "Allâme İbn Kayyim «Zâdü'l-meâd»da (1/18) şöyle der:",
 [T("قَالَ", "qala", "verb", ["hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ.", "A past verb «said»; its doer follows.", "Mâzî «dedi»; fâili sonra gelir."),
  T("الْعَلَّامَةُ", "allama-mubalagha", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The doer, in raf': «the most learned».", "Fâil, merfû: «allâme»."),
  T("ابْنُ", "ibn", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ مِنَ «الْعَلَّامَةُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A substitute for «the learned», in raf', annexed: «Ibn (al-Qayyim)».", "«El-allâme»den bedel, merfû, muzâf: «İbn (Kayyim)»."),
  MI("الْقَيِّمِ", "qayyim-name", "al-Qayyim", "Kayyim"),
  P_("فِي"),
  *Q([T("زَادِ", "zad", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِـ«فِي» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ" + J("بِـ«قَالَ»") + " — وَهُوَ اسْمُ كِتَابٍ.", "In jarr after فِي, annexed — the phrase hangs on «said»; the title of a book: «Zād».", "«fî» ile mecrûr, muzâf — câr-mecrûr «kâle»ye müteallik; kitap adı: «Zâd»."),
      MI("الْمَعَادِ", "maad", "al-Maʿād (the Return)", "el-Meâd (dönüş)", p=" (١/ ١٨):")], kind="name")]),
 SEN(3, "«It occurs in al-Tirmidhī's book and elsewhere that he sent Bilāl with him; and that is a plain error,",
     "«Tirmizî'nin kitabında ve başka yerlerde, onunla Bilâl'i gönderdiği geçer; bu açık bir hatadır;",
 [T("وَوَقَعَ", "waqaa", "verb", ["mithal-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَوَقَعَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّهُ بَعَثَ»؛ وَالْكَلَامُ الْمَحْكِيُّ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
    "The waw resumes; «it occurs» is a past verb — its doer is the masdar made by «that he sent»; the quoted words are what was said.", "Vâv isti'nâf içindir; «vakaa» mâzî — fâili «ennehû bease»den te'vîl edilen masdar; aktarılan söz mekūlü'l-kavl.", pre=("wa",)),
  P_("فِي"), MJ("كِتَابِ", "kitab", "فِي", ("بِـ«وَقَعَ»", "«occurs»", "«vakaa»ya"), "the book of", ("kitabı", "fî"), mudaf=True),
  MI("التِّرْمِذِيِّ", "tirmidhi", "al-Tirmidhī", "Tirmizî"),
  T("وَغَيْرِهِ", "ghayr", "noun", ["atf-nasaq", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَغَيْرِ مَعْطُوفٌ عَلَى «كِتَابِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The waw conjoins; «and elsewhere» is conjoined to «book», in jarr, annexed to «it».", "Vâv atıf; «gayr» «kitâb»a ma'tûf, mecrûr, muzâf; zamir muzâfun ileyh.", pre=("wa",), enc="هِ"),
  T("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ» يَعُودُ عَلَى أَبِي طَالِبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ فَاعِلُ «وَقَعَ».", "أَنَّ with «he» (Abū Ṭālib) as its noun — the masdar it makes is the doer of «occurs».", "«Enne»; zamir (Ebû Tâlib) ismidir — te'vîl edilen masdar «vakaa»nın fâili.", segs=[("أَنَّ", "anna", "part"), ("هُ", "pron-3ms", "pron")]),
  T("بَعَثَ", "baatha", "verb", ["thulathi-mujarrad-babs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».", "A past verb «sent»; its doer the hidden «he» — the clause is the predicate of أَنَّ.", "Mâzî «gönderdi»; fâili gizli «hüve» — cümle «enne»nin haberi."),
  T("مَعَهُ", "maa", "noun", ["maful-fih", "al-bariz-al-muttasil"], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى النَّبِيِّ؛ مُتَعَلِّقٌ بِـ«بَعَثَ».", "An adverb «with», in nasb, annexed to «him» (the Prophet) — it hangs on «sent».", "Zarf «ile», mansûb, muzâf; zamir (Peygamber) muzâfun ileyh — «besa»ya müteallik.", enc="هُ"),
  BILAL("بِلَالًا", "nasb", (["maful-bihi"], "مَفْعُولٌ بِهِ", "The object", "Mef'ûlün bih"), p="،"),
  T("وَأَنَّهُ", "anna", "part", ["atf-nasaq", "inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ» يَعُودُ عَلَى ذٰلِكَ الْقَوْلِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى الْمَصْدَرِ الْأَوَّلِ.",
    "The waw conjoins; أَنَّ with «it» (that statement) as its noun — the masdar is conjoined to the first: «and that it is …».", "Vâv atıf; «enne», zamir (o söz) ismidir — masdar birinci masdara ma'tûf.", segs=[("وَ", "wa", "conj"), ("أَنَّ", "anna", "part"), ("هُ", "pron-3ms", "pron")]),
  T("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter of part «of», voweled with fatha.", "Teb'îz için cer harfi; fetha aldı."),
  MJ("الْغَلَطِ", "ghalat", "مِنْ", ("بِمَحْذُوفٍ خَبَرِ «أَنَّ»", "the omitted predicate of أَنَّ", "«enne»nin mahzûf haberine"), "error", ("hata", "min")),
  NA("الْوَاضِحِ", "wadih", "الْغَلَطِ", "jarr", ("error", "plain"), ("el-galat", "açık"), p="،", g=("ism-fail",))]),
 SEN(4, "for at that time perhaps Bilāl did not yet exist; and if he did, he was not with his uncle nor with Abū Bakr»",
     "çünkü Bilâl o zaman belki henüz mevcut değildi; mevcut idiyse de ne amcasının ne de Ebû Bekir'in yanındaydı»",
 [T("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْفَاءُ تَعْلِيلِيَّةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "The fa gives the reason; إِنَّ «for, truly».", "Fâ ta'lîl içindir; «inne».", pre=("fa",)),
  BILAL("بِلَالًا", "nasb", (["inna-wa-akhawatuha"], "اسْمُ «إِنَّ»", "The noun of إِنَّ", "«İnne»nin ismi")),
  T("إِذْ", "idh", "noun", ["maful-fih"], "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ، مُتَعَلِّقٌ بِـ«مَوْجُودًا».", "إِذْ «then», an adverb of past time, built, annexed to the clause after it — it hangs on «existing».", "«İz» geçmiş zaman zarfı, mebnî, sonraki cümleye muzâf — «mevcûden»e müteallik."),
  T("ذَاكَ", "dhaka", "pron", ["mubtada-khabar", "asma-al-ishara-wa-sighuha"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ مَحْذُوفٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذْ» إِلَيْهَا.", "A demonstrative «that», the mubtada, its predicate omitted — the clause is annexed to إِذْ.", "İsm-i işaret «o», mübtedâ, haberi mahzûf — cümle «iz»e muzâfun ileyh."),
  T("لَعَلَّهُ", "laalla", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"], "حَرْفُ تَرَجٍّ وَنَصْبٍ — وَهُوَ هُنَا لِلظَّنِّ —، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُ «لَعَلَّ» يَعُودُ عَلَى بِلَالٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «إِنَّ».",
    "لَعَلَّ «perhaps» (here of supposition), with «he» (Bilāl) as its noun — the clause is the predicate of إِنَّ.", "«Lealle» (burada zan için), zamir (Bilâl) ismidir — cümle «inne»nin haberi.", segs=[("لَعَلَّ", "laalla", "part"), ("هُ", "pron-3ms", "pron")]),
  T("لَمْ", "lam", "part", ["jawazim-al-mudari-wal-amr-fil-kafiya"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "لَمْ negates and puts the verb in jazm.", "«Lem» nefy, cezm ve kalb harfi."),
  T("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "jawazim-al-mudari-wal-amr-fil-kafiya"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «لَعَلَّ».", "A defective present verb in jazm after لَمْ; its noun the hidden «he» — the clause is the predicate of لَعَلَّ.", "«lem» ile meczûm nâkıs muzâri; ismi gizli «hüve» — cümle «lealle»nin haberi."),
  T("مَوْجُودًا", "mawjud", "noun", ["kana-wa-akhawatuha", "ism-maful"], "خَبَرُ «يَكُنْ» مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of «be», in nasb: «existing».", "«Yekun»un haberi, mansûb: «mevcut».", p="،"),
  T("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ.", "The waw conjoins; إِنْ «if» is the conditional particle.", "Vâv atıf; «in» câzim şart harfi.", pre=("wa",)),
  T("كَانَ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs", "in-shartiyya"], "فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «وُجِدَ» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى بِلَالٍ.", "A complete past verb «existed», in the seat of jazm as the verb of the condition; its doer the hidden «he» (Bilāl).", "Tâmm mâzî «var idi», şart fiili olarak mahallen meczûm; fâili gizli «hüve» (Bilâl)."),
  T("فَلَمْ", "lam", "part", ["al-fa-fi-jawab-al-shart", "jawazim-al-mudari-wal-amr-fil-kafiya"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The fa binding the answer of the condition; لَمْ negates and puts the verb in jazm.", "Fâ şartın cevabını bağlar; «lem» nefy, cezm ve kalb harfi.", pre=("fa",)),
  T("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "jawazim-al-mudari-wal-amr-fil-kafiya"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.", "A defective present verb in jazm after لَمْ; its noun the hidden «he» — the clause is the answer of the condition, in the seat of jazm.", "«lem» ile meczûm nâkıs muzâri; ismi gizli «hüve» — cümle şartın cevabı, mahallen meczûm."),
  T("مَعَ", "maa", "noun", ["maful-fih", "kana-wa-akhawatuha", "idafa-definiteness"], "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «يَكُنْ».", "An adverb «with», in nasb, annexed — it hangs on the omitted predicate of «be».", "Zarf «ile», mansûb, muzâf — «yekun»un mahzûf haberine müteallik."),
  T("عَمِّهِ", "amm-uncle", "noun", ["idafa-definiteness", "al-bariz-al-muttasil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى النَّبِيِّ.", "The second term of the idafa, in jarr, annexed to «his» (the Prophet): «his uncle».", "Muzâfun ileyh, mecrûr, muzâf; zamir (Peygamber) muzâfun ileyh: «amcası».", enc="هِ"),
  T("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.", "The waw conjoins; لَا strengthens the negation: «nor».", "Vâv atıf; «lâ» nefyi te'kîd için zâide: «ne de».", pre=("wa",)),
  T("مَعَ", "maa", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness"], "ظَرْفٌ مَعْطُوفٌ عَلَى «مَعَ» الْأَوَّلِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adverb «with», conjoined to the first «with», in nasb, annexed.", "Birinci «maa»ya ma'tûf zarf, mansûb, muzâf."),
  T("أَبِي", "ab", "noun", ["idafa-definiteness", "five-nouns"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The second term of the idafa, in jarr by the ya (one of the five nouns), annexed: «Abū (Bakr)».", "Muzâfun ileyh, esmâ-i hamseden olduğu için yâ ile mecrûr, muzâf: «Ebû (Bekir)»."),
  MI("بَكْرٍ", "bakr", "Bakr", "Bekir", note=(" — وَ«أَبُو بَكْرٍ» الصِّدِّيقُ", " — «Abū Bakr» al-Ṣiddīq", " — «Ebû Bekir» es-Sıddîk"))]),
 SEN(5, "(The end of the learned al-Nuʿmānī's words.)",
     "(Allâme Nu'mânî'nin sözü burada biter.)",
 [T("انْتَهَى", "intaha", "verb", ["form-viii-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ اعْتِرَاضِيَّةٌ لَا مَحَلَّ لَهَا، يَخْتِمُ بِهَا الْمُؤَلِّفُ النَّقْلَ.", "A past verb «ended», built on a fatha estimated on the alif; its doer follows — a parenthetical clause with no seat, closing the quotation.", "Elif üzerinde takdîrî fetha ile mebnî mâzî «bitti»; fâili sonra gelir — nakli bitiren ara cümle, mahalli yoktur."),
  T("كَلَامُ", "kalam", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The doer, in raf', annexed: «the words of».", "Fâil, merfû, muzâf: «sözü»."),
  MI("الْعَلَّامَةِ", "allama-mubalagha", "the most learned", "allâme"),
  NA("النُّعْمَانِيِّ", "numani", "الْعَلَّامَةِ", "jarr", ("the learned", "al-Nuʿmānī"), ("el-allâme", "en-Nu'mânî"), p=".", g=("ism-mansub",))]),
]
S[4]["tokens"][0]["quoteBefore"] = "("; S[4]["tokens"][-1]["quoteAfter"] = ")"
S[2]["tokens"][0]["quoteBefore"] = "«"
S[3]["tokens"][-1]["quoteAfter"] = "»"
NEW = {
 "qadaha-impugn": NV("قَدَحَ", "ق د ح", "I", "to impugn, to tell against (فِي)", "halel getirmek, tenkit etmek", level=5),
 "bilal": NP("بِلَال", "Bilāl ibn Rabāḥ, the Companion, the muezzin", "Bilâl b. Rebâh, sahâbî, müezzin", level=4),
 "qayyim-name": NP("الْقَيِّم", "al-Qayyim — in the name Ibn al-Qayyim (al-Jawziyya, d. 751 AH)", "Kayyim — İbn Kayyim (el-Cevziyye, ö. 751) adında", level=5),
 "maad": NN("مَعَاد", "ع و د", "the Return (the Hereafter); in the title «Zād al-Maʿād»", "meâd, ahirete dönüş; «Zâdü'l-meâd» adında", level=5),
}
GLOSS_HERE = {"zad": ("provision (in the title «Zād al-Maʿād»)", "azık («Zâdü'l-meâd» adında)")}
V = {"qadaha-impugn": SG.sound1("fataha", "قَدَح", "قْدَح", "اِقْدَح", "قَدْح", "قَادِح", note="قَدَحَ فِيهِ يَقْدَحُ: عَابَهُ.")}
