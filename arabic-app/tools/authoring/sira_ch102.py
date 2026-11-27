"""al-Nadwī, al-Sīra al-Nabawiyya — chapter 102: «ولادته الكريمة ونسبه الزكيّ» (1), Shamela pp. 149–150, printed pp. 157–158: from
«وولد رسول الله» to «فتعجّب منه العرب.» — the birth, the lineage to ʿAdnān and Ismāʿīl, the naming."""
from sira_common import *

N_ = 102
TITLE = {"ar": "وِلَادَتُهُ الْكَرِيمَةُ وَنَسَبُهُ الزَّكِيُّ", "en": "His Noble Birth and Pure Lineage", "tr": "Mübarek Doğumu ve Temiz Nesebi"}
META = {"pages": "157–158", "en": "the day of the birth (s1), the lineage to ʿAdnān and Ismāʿīl (s2–s3), ʿAbd al-Muṭṭalib names him Muḥammad (s4–s6)",
        "tr": "doğum günü (s1), Adnân'a ve İsmâil'e uzanan nesep (s2–s3), Abdülmuttalib onu Muhammed diye adlandırır (s4–s6)"}
J = lambda s: "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ " + s
HOCA = [("ch. 102 s1: «شَهْرِ رَبِيعٍ الْأَوَّلِ» — «الْأَوَّلِ» read as the adjective of «رَبِيعٍ» (the month's name with tanwin), not «رَبِيعِ الْأَوَّلِ» by annexation",
         "Bölüm 102 s1: «şehri rebî'in el-evveli» — «el-evvel» «rebî'»in sıfatı okundu (tenvinli ay adı), izâfetle «rebî'i'l-evvel» değil"),
        ("ch. 102 s2: «عَبْدِ مَنَاف» — the last vowel of «مَنَاف» left UNWRITTEN (declined, or barred from tanwin as an idol's name)",
         "Bölüm 102 s2: «Abdi menâf» — «menâf»ın son harekesi YAZILMADI (munsarif mi, put adı olarak gayr-i munsarif mi)"),
        ("ch. 102 s1: «الْإِثْنَيْنِ» keeps the print's hamza on the alif (a waṣl alif by rule)", "Bölüm 102 s1: «el-isneyn» baskıdaki hemzeyi korur (kaideye göre vasl elifi)")]
LEFT = [("ch. 102 s1: the print's date gloss «(٥٧٠ المسيحي)» rides after «الْفِيلِ» as printed (no tokens: a numeral)", "Bölüm 102 s1: baskıdaki tarih açıklaması «(٥٧٠ المسيحي)» «el-fîl»den sonra basıldığı gibi durur (token değil: rakam)")]

TAN = "، وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ"
TAN_EN, TAN_TR = " — its tanwin drops before «ibn» annexed to a name", " — ardından bir aleme muzâf «ibn» geldiği için tenvini düşer"
WHY = {"t": ("لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", "a name feminine in form", "alem ve lafzî te'nîs"),
       "a": ("لِلْعَلَمِيَّةِ وَالْعُجْمَةِ", "a foreign name", "alem ve ucme"),
       "d": ("لِلْعَلَمِيَّةِ وَالْعَدْلِ", "a name turned from its pattern (ʿadl)", "alem ve adl"),
       "n": ("لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", "a name with the added alif and nun", "alem ve elif-nûn ziyâdesi")}
def NAME(full, lex, dip=None, ibn_after=True, p=None, unsure=False):
    """a forefather's name: the second term of the annexation after «بْنِ»"""
    if unsure:
        return T(full, lex, "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَتُرِكَتْ حَرَكَةُ آخِرِهِ لِلْعَالِمِ الْمُرَاجِعِ: أَمَصْرُوفٌ هُوَ أَمْ مَمْنُوعٌ مِنَ الصَّرْفِ.",
                 "The second term of the idafa, in jarr — its last vowel is left unwritten for the scholar (declined, or barred from tanwin).",
                 "Muzâfun ileyh, mecrûr — son harekesi hocaya bırakıldı (munsarif mi, gayr-i munsarif mi).", p=p)
    if dip:
        a, e, t = WHY[dip]
        return T(full, lex, "propn", ["idafa-definiteness", "mamnu-min-sarf"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ، مَمْنُوعٌ مِنَ الصَّرْفِ " + a + ".",
                 "The second term of the idafa, in jarr by the fatha in place of the kasra — " + e + ", barred from tanwin.",
                 "Muzâfun ileyh, kesre yerine fetha ile mecrûr — " + t + " sebebiyle gayr-i munsarif.", p=p)
    return T(full, lex, "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، عَلَمٌ مَصْرُوفٌ" + (TAN if ibn_after else "") + ".",
             "The second term of the idafa, in jarr — a declined name" + (TAN_EN if ibn_after else "") + ".", "Muzâfun ileyh, mecrûr — munsarif alem" + (TAN_TR if ibn_after else "") + ".", p=p)
def B(of): return BN("jarr", of)
CHAIN = [  # after «عَبْدِ الْمُطَّلِبِ»: (name, key, diptote reason, gloss for the next «بْنِ»)
 ("هَاشِمِ", "hashim", None, ("هَاشِمِ", "Hāshim", "Hâşim")), ("عَبْدِ", "abd", "abd", None), ("مَنَاف", "manaf", "?", ("عَبْدِ مَنَاف", "ʿAbd Manāf", "Abdümenâf")),
 ("قُصَيِّ", "qusayy", None, ("قُصَيِّ", "Quṣayy", "Kusay")), ("كِلَابِ", "lb-kilab", None, ("كِلَابِ", "Kilāb", "Kilâb")), ("مُرَّةَ", "murra-name", "t", ("مُرَّةَ", "Murra", "Mürre")),
 ("كَعْبِ", "kab-name", None, ("كَعْبِ", "Kaʿb", "Ka'b")), ("لُؤَيِّ", "luayy", None, ("لُؤَيِّ", "Luʾayy", "Lüey")), ("غَالِبِ", "ghalib-name", None, ("غَالِبِ", "Ghālib", "Gâlib")),
 ("فِهْرِ", "fihr", None, ("فِهْرِ", "Fihr", "Fihr")), ("مَالِكِ", "malik-name", None, ("مَالِكِ", "Mālik", "Mâlik")), ("النَّضْرِ", "nadr", None, ("النَّضْرِ", "al-Naḍr", "Nadr")),
 ("كِنَانَةَ", "kinana", "t", ("كِنَانَةَ", "Kināna", "Kinâne")), ("خُزَيْمَةَ", "khuzayma", "t", ("خُزَيْمَةَ", "Khuzayma", "Huzeyme")), ("مُدْرِكَةَ", "mudrika", "t", ("مُدْرِكَةَ", "Mudrika", "Müdrike")),
 ("إِلْيَاسَ", "ilyas", "a", ("إِلْيَاسَ", "Ilyās", "İlyâs")), ("مُضَرَ", "mudar", "d", ("مُضَرَ", "Muḍar", "Mudar")), ("نِزَارِ", "nizar", None, ("نِزَارِ", "Nizār", "Nizâr")),
 ("مَعَدِّ", "maadd-name", None, ("مَعَدِّ", "Maʿadd", "Mead")), ("عَدْنَانَ", "adnan", "n", None)]
def nasab():
    out = []
    for i, (full, lex, dip, of) in enumerate(CHAIN):
        last = i == len(CHAIN) - 1
        if dip == "abd":
            out.append(T("عَبْدِ", "abd", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "The second term of the idafa, in jarr, itself annexed: «ʿAbd (Manāf)».", "Muzâfun ileyh, mecrûr, muzâf: «Abd(ümenâf)».")); continue
        out.append(NAME(full, lex, None if dip == "?" else dip, ibn_after=not last, p="." if last else None, unsure=dip == "?"))
        if not last: out.append(B(of))
    return out

S = [
 SEN(1, "The Messenger of Allah — Allah bless him and grant him peace — was born on Monday, the twelfth day of the month of Rabīʿ al-Awwal, in the Year of the Elephant (570 CE); and it was the happiest day on which the sun ever rose.",
     "Resûlullah — sallallâhu aleyhi ve sellem — Fil Yılı'nda (milâdî 570) Rebîülevvel ayının on ikinci günü, pazartesi günü doğdu; o gün, güneşin doğduğu en mutlu gündü.",
 [T("وَوُلِدَ", "walada", "verb", ["naib-al-fail", "mithal-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَوُلِدَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ بَعْدَهُ.",
    "The waw resumes; «was born» is a past verb in the passive, built on fatha; its deputy doer follows.", "Vâv isti'nâf içindir; «vulide» meçhul mâzî, fetha üzere mebnî; nâib-i fâili sonra gelir.", pre=("wa",)),
  T("رَسُولُ", "rasul", "noun", ["naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The deputy doer, in raf', annexed: «the Messenger of».", "Nâib-i fâil, merfû, muzâf: «Resûlü»."),
  T("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The name of Allah, the second term of the idafa, in jarr.", "Lafza-i celâl, muzâfun ileyh, mecrûr."),
  *SAW(),
  T("يَوْمَ", "yawm", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، مُتَعَلِّقٌ بِـ«وُلِدَ».", "An adverb of time in nasb, annexed — it hangs on «was born»: «on the day of».", "Zaman zarfı, mansûb, muzâf — «vulide»ye müteallik: «günü»."),
  T("الْإِثْنَيْنِ", "ithnayn-monday", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى — وَهُوَ اسْمُ الْيَوْمِ.",
    "The second term of the idafa, in jarr by the ya (it is treated as a dual) — the name of the day: «Monday».", "Muzâfun ileyh, tesniyeye mülhak olduğu için yâ ile mecrûr — günün adı: «pazartesi»."),
  T("الْيَوْمَ", "yawm", "noun", ["badal"], "بَدَلٌ مِنْ «يَوْمَ الْإِثْنَيْنِ» مَنْصُوبٌ بِالْفَتْحَةِ.", "A substitute for «Monday», in nasb: «the day …».", "«Pazartesi günü»nden bedel, mansûb: «… günü»."),
  T("الثَّانِيَ", "thani", "noun", ["naat-sifa", "asma-al-adad-fil-kafiya"], "نَعْتٌ لِـ«الْيَوْمَ» — وَ«الثَّانِيَ عَشَرَ» عَدَدٌ تَرْتِيبِيٌّ مُرَكَّبٌ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ نَصْبٍ.",
    "An adjective of «the day» — «the twelfth» is a compound ordinal, both parts built on fatha, in the seat of nasb.", "«el-yevm»in na'tı — «on ikinci» mürekkep sıra sayısıdır; iki cüzü fetha üzere mebnî, mahallen mansûb."),
  T("عَشَرَ", "ashar", "noun", ["asma-al-adad-fil-kafiya"], "الْجُزْءُ الثَّانِي مِنَ الْعَدَدِ الْمُرَكَّبِ، مَبْنِيٌّ عَلَى الْفَتْحِ لَا مَحَلَّ لَهُ.", "The second part of the compound number, built on fatha, with no seat of its own.", "Mürekkep sayının ikinci cüzü, fetha üzere mebnî, mahalli yoktur."),
  T("مِنْ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "A jarr letter: «of».", "Cer harfi: «-den»."),
  T("شَهْرِ", "shahr", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِـ«مِنْ» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ" + J("بِمَحْذُوفٍ حَالٍ مِنَ «الْيَوْمَ»") + ".", "In jarr after مِنْ, annexed — the phrase hangs on an omitted hal of «the day».", "«min» ile mecrûr, muzâf — câr-mecrûr «el-yevm»den mahzûf hâle müteallik."),
  T("رَبِيعٍ", "rabi", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ الشَّهْرِ.", "The second term of the idafa, in jarr — the month's name: «Rabīʿ».", "Muzâfun ileyh, mecrûr — ayın adı: «Rebî'»."),
  T("الْأَوَّلِ", "awwal", "noun", ["naat-sifa"], "نَعْتٌ لِـ«رَبِيعٍ» مَجْرُورٌ بِالْكَسْرَةِ.", "An adjective of «Rabīʿ», in jarr: «the first».", "«Rebî'»in na'tı, mecrûr: «birinci».", p="،"),
  T("عَامَ", "aam-year", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، مُتَعَلِّقٌ بِـ«وُلِدَ».", "An adverb of time in nasb, annexed — it hangs on «was born»: «in the year of».", "Zaman zarfı, mansûb, muzâf — «vulide»ye müteallik: «yılında»."),
  T("الْفِيلِ", "fil-elephant", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَ«عَامُ الْفِيلِ» عَامُ أَصْحَابِ الْفِيلِ.", "The second term of the idafa, in jarr — «the Year of the Elephant», the year of the men of the elephant.", "Muzâfun ileyh, mecrûr — «Fil Yılı», fil sahiplerinin yılı.", p=" (٥٧٠ المسيحي)"),
  T("فَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "الْفَاءُ عَاطِفَةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى يَوْمِ مَوْلِدِهِ.",
    "The fa conjoins; كَانَ is the defective past verb; its noun is the hidden «it» (the day of his birth).", "Fâ atıf; «kâne» nâkıs mâzî; ismi gizli «hüve» (doğum günü).", pre=("fa",)),
  T("أَسْعَدَ", "asad-happiest", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"], "خَبَرُ «كَانَ» مَنْصُوبٌ بِالْفَتْحَةِ، اسْمُ تَفْضِيلٍ مُضَافٌ.", "The predicate of كَانَ, in nasb — an elative «the happiest», annexed.", "Kâne'nin haberi, mansûb — ism-i tafdîl «en mutlusu», muzâf."),
  T("يَوْمٍ", "yawm", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The second term of the idafa, in jarr: «day».", "Muzâfun ileyh, mecrûr: «gün»."),
  T("طَلَعَتْ", "talaa", "verb", ["thulathi-mujarrad-babs", "jumla-sifa"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«يَوْمٍ».",
    "A past verb built on fatha «rose»; the ta marks the feminine; its doer follows — the clause is an adjective of «day», in the seat of jarr.", "Fetha üzere mebnî mâzî «doğdu»; tâ te'nîs içindir; fâili sonra gelir — cümle «yevm»in na'tı olarak mahallen mecrûr."),
  T("فِيهِ", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى «يَوْمٍ» — وَهُوَ الرَّابِطُ" + J("بِـ«طَلَعَتْ»") + ".", "A jarr letter with «it» (the day), the clause's link back — the phrase hangs on «rose».", "Cer harfi; zamir («yevm»e döner) râbıttır — câr-mecrûr «tala'at»a müteallik.", enc="هِ"),
  T("الشَّمْسُ", "shams", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The doer, in raf': «the sun».", "Fâil, merfû: «güneş».", p=".")]),
 SEN(2, "He is Muḥammad son of ʿAbd Allāh son of ʿAbd al-Muṭṭalib son of Hāshim son of ʿAbd Manāf son of Quṣayy son of Kilāb son of Murra son of Kaʿb son of Luʾayy son of Ghālib son of Fihr son of Mālik son of al-Naḍr son of Kināna son of Khuzayma son of Mudrika son of Ilyās son of Muḍar son of Nizār son of Maʿadd son of ʿAdnān.",
     "O, Muhammed b. Abdullah b. Abdülmuttalib b. Hâşim b. Abdümenâf b. Kusay b. Kilâb b. Mürre b. Ka'b b. Lüey b. Gâlib b. Fihr b. Mâlik b. Nadr b. Kinâne b. Huzeyme b. Müdrike b. İlyâs b. Mudar b. Nizâr b. Mead b. Adnân'dır.",
 [T("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ يَعُودُ عَلَى رَسُولِ اللهِ.",
    "The waw resumes; «he» (the Messenger of Allah) is a detached pronoun built on fatha, the mubtada, in the seat of raf'.", "Vâv isti'nâf içindir; «hüve» (Resûlullah) fetha üzere mebnî munfasıl zamir, mübtedâ, mahallen merfû.", segs=[("وَ", "wa", "conj"), ("هُوَ", "huwa", "pron")]),
  T("مُحَمَّدُ", "muhammad", "propn", ["mubtada-khabar"], "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ" + TAN + ".", "The predicate, in raf'" + TAN_EN + ".", "Haber, merfû" + TAN_TR + "."),
  BN("raf", ("مُحَمَّدُ", "Muḥammad", "Muhammed")),
  T("عَبْدِ", "abd", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "The second term of the idafa, in jarr, itself annexed: «ʿAbd (Allāh)».", "Muzâfun ileyh, mecrûr, muzâf: «Abd(ullah)»."),
  T("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The name of Allah, the second term of the idafa, in jarr.", "Lafza-i celâl, muzâfun ileyh, mecrûr."),
  B(("عَبْدِ اللهِ", "ʿAbd Allāh", "Abdullah")),
  T("عَبْدِ", "abd", "noun", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "The second term of the idafa, in jarr, itself annexed: «ʿAbd (al-Muṭṭalib)».", "Muzâfun ileyh, mecrûr, muzâf: «Abd(ülmuttalib)»."),
  T("الْمُطَّلِبِ", "muttalib", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The second term of the idafa, in jarr.", "Muzâfun ileyh, mecrûr."),
  B(("عَبْدِ الْمُطَّلِبِ", "ʿAbd al-Muṭṭalib", "Abdülmuttalib")),
  *nasab()]),
 SEN(3, "And ʿAdnān's lineage goes back to our master Ismāʿīl son of Ibrāhīm — peace be upon them both.",
     "Adnân'ın nesebi de efendimiz İbrâhim oğlu İsmâil'e — ikisine de selâm olsun — varır.",
 [T("وَيَنْتَهِي", "intaha", "verb", ["form-viii-verbs", "naqis-verbs", "mudari-marfu"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيَنْتَهِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ بَعْدَهُ.",
    "The waw resumes; «goes back» is a present verb in raf' by a damma estimated on the ya (too heavy to show); its doer follows.", "Vâv isti'nâf içindir; «yentehî» merfû muzâri, damme ağırlık sebebiyle yâ üzerinde takdîrîdir; fâili sonra gelir.", pre=("wa",)),
  T("نَسَبُ", "nasab", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The doer, in raf', annexed: «the lineage of».", "Fâil, merfû, muzâf: «nesebi»."),
  NAME("عَدْنَانَ", "adnan", "n", ibn_after=False),
  T("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ.", "A jarr letter of the end point: «to».", "Gâyenin sonu için cer harfi: «-e»."),
  T("سَيِّدِنَا", "sayyid", "noun", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"], "مَجْرُورٌ بِـ«إِلَى» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + J("بِـ«يَنْتَهِي»") + ".",
    "In jarr after إِلَى, annexed to «our» — the phrase hangs on «goes back»: «our master».", "«ilâ» ile mecrûr, muzâf; «nâ» muzâfun ileyh — câr-mecrûr «yentehî»ye müteallik: «efendimiz».", enc="نَا"),
  T("إِسْمَاعِيلَ", "ismail", "propn", ["badal", "mamnu-min-sarf"], "بَدَلٌ مِنْ «سَيِّدِنَا» مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ، مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
    "A substitute for «our master», in jarr by the fatha in place of the kasra — a foreign name, barred from tanwin.", "«Seyyidinâ»dan bedel, kesre yerine fetha ile mecrûr — alem ve ucme sebebiyle gayr-i munsarif."),
  B(("إِسْمَاعِيلَ", "Ismāʿīl", "İsmâil")),
  NAME("إِبْرَاهِيمَ", "ibrahim", "a", ibn_after=False),
  T("عَلَيْهِمَا", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "jumla-mutarida"], "حَرْفُ جَرٍّ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى إِسْمَاعِيلَ وَإِبْرَاهِيمَ" + J("بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ") + " — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا.",
    "A jarr letter with «them both» (Ismāʿīl and Ibrāhīm) — the phrase is the fronted predicate; the prayer is set in the sentence with no seat.", "Cer harfi; «humâ» (İsmâil ve İbrâhim) — câr-mecrûr öne alınmış habere müteallik; duâ cümlesi ara cümledir, mahalli yoktur.", enc="هِمَا"),
  T("السَّلَامُ", "salam", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The mubtada, placed after its predicate, in raf': «peace».", "Sonraya bırakılmış mübtedâ, merfû: «selâm».", p=".")]),
 SEN(4, "When his mother — Allah bless him and grant him peace — had given birth to him, she sent word to his grandfather ʿAbd al-Muṭṭalib that a boy had been born to him; so he came to him,",
     "Annesi onu — sallallâhu aleyhi ve sellem — doğurunca dedesi Abdülmuttalib'e «Sana bir oğlan doğdu» diye haber gönderdi; o da geldi,",
 [T("فَلَمَّا", "lamma", "part", ["maful-fih"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى «حِينَ» مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِجَوَابِهِ «أَرْسَلَتْ».",
    "The fa resumes; لَمَّا «when» is an adverb with the sense of a condition, built on sukun, in the seat of nasb; it hangs on its answer «she sent».", "Fâ isti'nâf içindir; «lemmâ» şart mânası taşıyan «hîne» anlamında zarf, sükûn üzere mebnî, mahallen mansûb; cevabı «erselet»e müteallik.", pre=("fa",)),
  T("وَضَعَتْهُ", "wadaa", "verb", ["mithal-verbs", "al-bariz-al-muttasil"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «لَمَّا» إِلَيْهَا.",
    "A past verb «gave birth to», the ta of the feminine, «him» its object; its doer follows — the clause is in the seat of jarr, annexed to لَمَّا.", "Mâzî «doğurdu», tâ te'nîs için; zamir mef'ûlün bih; fâili sonra gelir — cümle «lemmâ»ya muzâfun ileyh olarak mahallen mecrûr.",
    segs=[("وَضَعَتْ", "wadaa", "verb"), ("هُ", "pron-3ms", "pron")]),
  T("أُمُّهُ", "umm", "noun", ["fail", "al-bariz-al-muttasil"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The doer, in raf', annexed to «his»: «his mother».", "Fâil, merfû, muzâf; zamir muzâfun ileyh: «annesi».", enc="هُ"),
  *SAW(),
  T("أَرْسَلَتْ", "arsala", "verb", ["form-iv-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ جَوَابُ «لَمَّا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A past verb «she sent», the ta of the feminine; its doer is the hidden «she» — the clause is the answer of لَمَّا, with no seat.", "Mâzî «gönderdi», tâ te'nîs için; fâili gizli «hiye» — cümle «lemmâ»nın cevabıdır, mahalli yoktur."),
  T("إِلَى", "ila", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "A jarr letter: «to».", "Cer harfi: «-e»."),
  T("جَدِّهِ", "jadd", "noun", ["huruf-jarr", "al-bariz-al-muttasil"], "مَجْرُورٌ بِـ«إِلَى» وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + J("بِـ«أَرْسَلَتْ»") + ".",
    "In jarr after إِلَى, annexed to «his»: «his grandfather» — the phrase hangs on «she sent».", "«ilâ» ile mecrûr, muzâf; zamir muzâfun ileyh: «dedesi» — câr-mecrûr «erselet»e müteallik.", enc="هِ"),
  T("عَبْدِ", "abd", "noun", ["badal", "idafa-definiteness"], "بَدَلٌ مِنْ «جَدِّهِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "A substitute for «his grandfather», in jarr, annexed.", "«Ceddihî»den bedel, mecrûr, muzâf."),
  T("الْمُطَّلِبِ", "muttalib", "propn", ["idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The second term of the idafa, in jarr.", "Muzâfun ileyh, mecrûr."),
  T("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُ «أَنَّ» — وَ«أَنَّ» وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَجْرُورٍ بِبَاءٍ مَحْذُوفَةٍ، أَيْ: بِأَنَّهُ.",
    "أَنَّ «that» with the pronoun of the matter (ḍamīr al-shaʾn) as its noun — it and its clause stand for a masdar in jarr by an omitted ba («(sent word) that …»).", "«Enne»; zamir şe'n zamiri, ismidir — kendisi ve sonrası mahzûf bir bâ ile mecrûr masdar yerindedir: «… diye (haber gönderdi)».", segs=[("أَنَّ", "anna", "part"), ("هُ", "pron-3ms", "pron")]),
  T("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "قَدْ confirms the past verb: «(has) indeed».", "«Kad» tahkîk harfi."),
  T("وُلِدَ", "walada", "verb", ["naib-al-fail", "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَائِبُ الْفَاعِلِ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».",
    "A past verb in the passive «has been born»; its deputy doer follows — the clause is the predicate of أَنَّ, in the seat of raf'.", "Meçhul mâzî «doğdu»; nâib-i fâili sonra gelir — cümle «enne»nin haberi olarak mahallen merfû."),
  T("لَكَ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى عَبْدِ الْمُطَّلِبِ" + J("بِـ«وُلِدَ»") + ".",
    "The lam, a jarr letter, with «you» (ʿAbd al-Muṭṭalib) — the phrase hangs on «has been born».", "Lâm cer harfi; «ke» (Abdülmuttalib) mahallen mecrûr — câr-mecrûr «vulide»ye müteallik.", segs=[("لَ", "li", "prep"), ("كَ", "pron-2ms", "pron")]),
  T("غُلَامٌ", "ghulam", "noun", ["naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ.", "The deputy doer, in raf': «a boy».", "Nâib-i fâil, merfû: «bir oğlan»."),
  T("فَأَتَاهُ", "ata", "verb", ["atf-nasaq", "naqis-verbs", "mahmuz-verbs", "al-bariz-al-muttasil"], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَأَتَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى الْمَوْلُودِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى عَبْدِ الْمُطَّلِبِ.",
    "The fa conjoins and marks what follows at once; «came to» is a past verb built on a fatha estimated on the alif; «him» (the newborn) is its object; its doer is the hidden «he» (ʿAbd al-Muṭṭalib).", "Fâ ta'kîb ile atıf içindir; «etâ» elif üzerinde takdîrî fetha ile mebnî mâzî; zamir (yeni doğan) mef'ûlün bih; fâili gizli «hüve» (Abdülmuttalib).",
    p="،", segs=[("فَ", "fa", "conj"), ("أَتَا", "ata", "verb"), ("هُ", "pron-3ms", "pron")])]),
 SEN(5, "looked at him, carried him and went with him into the Kaaba; he stood calling upon Allah and praising Him,",
     "ona baktı, onu kucağına aldı ve onunla Kâbe'ye girdi; Allah'a duâ ederek ve O'na hamd ederek ayakta durdu,",
 [T("فَنَظَرَ", "nazara", "verb", ["atf-nasaq", "thulathi-mujarrad-babs"], "الْفَاءُ عَاطِفَةٌ لِلتَّعْقِيبِ، وَنَظَرَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "The fa conjoins and marks what follows at once; «looked» is a past verb built on fatha; its doer is the hidden «he».", "Fâ ta'kîb ile atıf içindir; «nazara» fetha üzere mebnî mâzî; fâili gizli «hüve».", pre=("fa",)),
  T("إِلَيْهِ", "ila", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ" + J("بِـ«نَظَرَ»") + ".", "A jarr letter with «him» — the phrase hangs on «looked».", "Cer harfi; zamir mahallen mecrûr — câr-mecrûr «nazara»ya müteallik.", p="،", enc="هِ"),
  T("وَحَمَلَهُ", "hamala", "verb", ["atf-nasaq", "thulathi-mujarrad-babs", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَحَمَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "The waw conjoins; «carried» is a past verb built on fatha; «him» its object; its doer the hidden «he».", "Vâv atıf; «hamele» fetha üzere mebnî mâzî; zamir mef'ûlün bih; fâili gizli «hüve».", p="،", pre=("wa",), enc="هُ"),
  T("وَدَخَلَ", "dakhala", "verb", ["atf-nasaq", "thulathi-mujarrad-babs"], "الْوَاوُ عَاطِفَةٌ، وَدَخَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "The waw conjoins; «went into» is a past verb built on fatha; its doer the hidden «he».", "Vâv atıf; «dehale» fetha üzere mebnî mâzî; fâili gizli «hüve».", pre=("wa",)),
  T("بِهِ", "bi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "الْبَاءُ حَرْفُ جَرٍّ لِلْمُصَاحَبَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ" + J("بِـ«دَخَلَ»") + ".", "The ba of company, a jarr letter, with «him»: «with him» — the phrase hangs on «went into».", "Musâhabet bâsı, cer harfi; zamir mahallen mecrûr: «onunla» — câr-mecrûr «dehale»ye müteallik.", enc="هِ"),
  T("الْكَعْبَةَ", "kaaba", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — وَقِيلَ: مَنْصُوبٌ عَلَى التَّوَسُّعِ بِإِسْقَاطِ «فِي».", "The object, in nasb: «the Kaaba» (some say in nasb by the dropping of فِي).", "Mef'ûlün bih, mansûb: «Kâbe» (bir görüşe göre «fî» düşürülerek mansûb).", p="،"),
  T("قَامَ", "qama", "verb", ["hollow-verbs", "thulathi-mujarrad-babs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A past verb «stood», built on fatha; its doer the hidden «he» — the clause starts anew and has no seat.", "Fetha üzere mebnî mâzî «durdu»; fâili gizli «hüve» — cümle isti'nâfiyyedir, mahalli yoktur."),
  T("يَدْعُو", "daa", "verb", ["naqis-verbs", "hal", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «قَامَ».",
    "A present verb in raf' by a damma estimated on the waw (too heavy to show) «calling upon»; its doer the hidden «he» — the clause is a hal of the doer of «stood».", "Merfû muzâri, damme ağırlık sebebiyle vâv üzerinde takdîrî «duâ ederek»; fâili gizli «hüve» — cümle «kâme»nin fâilinden hâl, mahallen mansûb."),
  T("اللهَ", "allah", "propn", ["maful-bihi"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The name of Allah, the object, in nasb.", "Lafza-i celâl, mef'ûlün bih, mansûb.", p="،"),
  T("وَيَحْمَدُهُ", "hamida", "verb", ["atf-nasaq", "thulathi-mujarrad-babs", "al-bariz-al-muttasil", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَحْمَدُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مَعْطُوفٌ عَلَى «يَدْعُو» وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى اللهِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "The waw conjoins; «and praising» is a present verb in raf', conjoined to «calling upon»; «Him» (Allah) its object; its doer the hidden «he».", "Vâv atıf; «yahmedu» «yed'û»ya ma'tûf merfû muzâri; zamir (Allah) mef'ûlün bih; fâili gizli «hüve».", pre=("wa",), enc="هُ")]),
 SEN(6, "and named him «Muḥammad»; this name was unusual, and the Arabs wondered at it.",
     "ve onu «Muhammed» diye adlandırdı; bu isim alışılmamış bir isimdi; Araplar ona şaştılar.",
 [T("وَسَمَّاهُ", "samma", "verb", ["atf-nasaq", "form-ii-verbs", "naqis-verbs", "mafulayn", "al-bariz-al-muttasil"], "الْوَاوُ عَاطِفَةٌ، وَسَمَّى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى عَبْدِ الْمُطَّلِبِ.",
    "The waw conjoins; «named» is a past verb built on a fatha estimated on the alif; «him» is its first object; its doer the hidden «he» (ʿAbd al-Muṭṭalib).", "Vâv atıf; «semmâ» elif üzerinde takdîrî fetha ile mebnî mâzî; zamir birinci mef'ûl; fâili gizli «hüve» (Abdülmuttalib).",
    segs=[("وَ", "wa", "conj"), ("سَمَّا", "samma", "verb"), ("هُ", "pron-3ms", "pron")]),
  *Q([T("مُحَمَّدًا", "muhammad", "propn", ["maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb: «Muḥammad».", "İkinci mef'ûl, mansûb: «Muhammed».")], kind="name"),
  T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ.", "The waw resumes; كَانَ is the defective past verb.", "Vâv isti'nâf içindir; «kâne» nâkıs mâzî.", pre=("wa",)),
  T("هٰذَا", "hadha", "pron", ["kana-wa-akhawatuha", "asma-al-ishara-wa-sighuha"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ اسْمُ «كَانَ».", "A demonstrative «this», built on sukun, in the seat of raf' as the noun of كَانَ.", "İsm-i işaret «bu», sükûn üzere mebnî, kâne'nin ismi olarak mahallen merfû."),
  T("الِاسْمُ", "ism-name", "noun", ["badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "A substitute for the demonstrative, in raf': «(this) name».", "İsm-i işaretten bedel, merfû: «(bu) isim»."),
  T("غَرِيبًا", "gharib", "noun", ["kana-wa-akhawatuha"], "خَبَرُ «كَانَ» مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of كَانَ, in nasb: «unusual».", "Kâne'nin haberi, mansûb: «alışılmamış».", p="،"),
  T("فَتَعَجَّبَ", "taajjaba", "verb", ["atf-nasaq", "form-v-verbs"], "الْفَاءُ عَاطِفَةٌ لِلسَّبَبِيَّةِ، وَتَعَجَّبَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ.", "The fa conjoins and marks the result; «wondered» is a past verb built on fatha; its doer follows.", "Fâ sebebiyye ile atıf içindir; «teaccebe» fetha üzere mebnî mâzî; fâili sonra gelir.", pre=("fa",)),
  T("مِنْهُ", "min", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى الِاسْمِ" + J("بِـ«تَعَجَّبَ»") + ".", "A jarr letter with «it» (the name) — the phrase hangs on «wondered».", "Cer harfi; zamir (isme döner) — câr-mecrûr «teaccebe»ye müteallik.", enc="هُ"),
  T("الْعَرَبُ", "arab", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The doer, in raf': «the Arabs».", "Fâil, merfû: «Araplar».", p=".")]),
]
NEW = {
 "ithnayn-monday": NN("الْإِثْنَيْن", "ث ن ي", "Monday (يَوْمُ الْإِثْنَيْنِ)", "pazartesi", level=4),
 "asad-happiest": NN("أَسْعَد", "س ع د", "happiest (elative of سَعِيد)", "en mutlu (sa'îd'in ism-i tafdîli)", level=4),
 "qusayy": NP("قُصَيّ", "Quṣayy ibn Kilāb, the Prophet's forefather", "Kusay b. Kilâb, Peygamber'in atası", level=5),
 "murra-name": NP("مُرَّة", "Murra ibn Kaʿb, the Prophet's forefather", "Mürre b. Ka'b, Peygamber'in atası", level=5),
 "luayy": NP("لُؤَيّ", "Luʾayy ibn Ghālib, the Prophet's forefather", "Lüey b. Gâlib, Peygamber'in atası", level=5),
 "ghalib-name": NP("غَالِب", "Ghālib ibn Fihr, the Prophet's forefather", "Gâlib b. Fihr, Peygamber'in atası", level=5),
 "fihr": NP("فِهْر", "Fihr ibn Mālik (called Quraysh), the Prophet's forefather", "Fihr b. Mâlik (Kureyş denir), Peygamber'in atası", level=5),
 "kinana": NP("كِنَانَة", "Kināna ibn Khuzayma, the Prophet's forefather", "Kinâne b. Huzeyme, Peygamber'in atası", level=5),
 "khuzayma": NP("خُزَيْمَة", "Khuzayma ibn Mudrika, the Prophet's forefather", "Huzeyme b. Müdrike, Peygamber'in atası", level=5),
 "mudrika": NP("مُدْرِكَة", "Mudrika ibn Ilyās, the Prophet's forefather", "Müdrike b. İlyâs, Peygamber'in atası", level=5),
 "ilyas": NP("إِلْيَاس", "Ilyās ibn Muḍar, the Prophet's forefather", "İlyâs b. Mudar, Peygamber'in atası", level=5),
 "mudar": NP("مُضَر", "Muḍar ibn Nizār, the Prophet's forefather", "Mudar b. Nizâr, Peygamber'in atası", level=5),
 "nizar": NP("نِزَار", "Nizār ibn Maʿadd, the Prophet's forefather", "Nizâr b. Mead, Peygamber'in atası", level=5),
 "adnan": NP("عَدْنَان", "ʿAdnān, forefather of the northern Arabs, of the line of Ismāʿīl", "Adnân, kuzey Araplarının atası, İsmâil soyundan", level=5),
}
GLOSS_HERE = {"lb-kilab": ("Kilāb ibn Murra, the Prophet's forefather", "Kilâb b. Mürre, Peygamber'in atası"),
              "kab-name": ("Kaʿb ibn Luʾayy, the Prophet's forefather", "Ka'b b. Lüey, Peygamber'in atası"),
              "malik-name": ("Mālik ibn al-Naḍr, the Prophet's forefather", "Mâlik b. Nadr, Peygamber'in atası"),
              "nadr": ("al-Naḍr ibn Kināna, the Prophet's forefather", "Nadr b. Kinâne, Peygamber'in atası"),
              "rabi": ("Rabīʿ — شَهْرُ رَبِيعٍ الْأَوَّلِ: the month Rabīʿ al-Awwal", "Rebî' — Rebîülevvel ayı"),
              "hashim": ("Hāshim ibn ʿAbd Manāf, the Prophet's great-grandfather", "Hâşim b. Abdümenâf, Peygamber'in büyük dedesi")}
