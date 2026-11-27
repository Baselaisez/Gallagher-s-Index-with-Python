"""Author content/samples/tabaqat-innama-ana-habashi — «إِنَّمَا أَنَا حَبَشِيٌّ», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Companions, Bilāl ibn Rabāḥ's entry, vol. 3 p. 180 (Shamela p.
858): two consecutive akhbār, each whole with its isnād — Ibn Murāhin's («قال: أخبرت عن أبي اليمان» … «كنت بالأمس عبدا.») and Qays's
(«قال: أخبرنا محمد بن عبيد الطنافسي» … «فذرني وعملي لله.»), one chapter each.
The exact passage: research/sources/tabaqat-innama-ana-habashi-src.txt. No correction. Every vowel is ours; the name «مراهن» is left unvowelled.
Run: python3 tools/authoring/author_tabaqat_innama_ana_habashi.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-innama-ana-habashi"
BL = ("بِلَالٍ", "Bilāl", "Bilâl")
AB = ("أَبِي بَكْرٍ", "Abū Bakr", "Ebû Bekir")
UKH = H("بِـ«أُخْبِرْتُ»", "«I was told»", "«uhbirtu»ya")
AKH = H("بِـ«أَخْبَرَنَا»", "«told us»", "«ahberanâ»ya")
def ISHTARAYTANI(pre=()):
    return tok("اشْتَرَيْتَنِي", "ishtara", "verb", ["form-viii-verbs", "naqis-verbs", "al-bariz-al-muttasil", "ya-al-mutakallim", "maful-bihi"],
        "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ».",
        "A past verb built on sukūn because the doer's ta is attached; the ta («you») is its doer, the nūn guards it and the ya («me») is its object — the clause is the predicate of «were».",
        "Fâil tâsı bitiştiği için sükûn üzere mebnî mâzî; tâ (sen) fâil, nûn vikâye, yâ (beni) mef'ûlün bih — cümle «kâne»nin haberi.",
        segments=[seg("اشْتَرَيْ", "ishtara", "verb"), seg("تَ", "pron-2ms", "pron"), seg("نِي", "pron-1s", "pron")])
def KUNTA(pre=("wa",)):
    w = "وَ" if pre else ""
    return tok(w + "إِنْ", "in-shartiyya", "part", ["in-shartiyya", "huruf-al-shart-fil-kafiya"],
        ("الْوَاوُ عَاطِفَةٌ، وَ" if pre else "") + "إِنْ حَرْفُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ.", ("The waw conjoins; " if pre else "") + "إِنْ «if», the conditional particle that puts its verbs in jazm.",
        ("Vâv atıf; " if pre else "") + "«In» câzim şart harfi.", segments=[seg("وَ", "wa", "conj"), seg("إِنْ", "in-shartiyya", "part")] if pre else None), \
        VERB("كُنْتَ", "kana", "mta", form="kana-wa-akhawatuha", g=["hollow-verbs", "in-shartiyya"], note=(" — نَاقِصٌ، وَالتَّاءُ اسْمُهُ، وَهُوَ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", " — defective; the ta is its noun; it is the verb of the condition, in the seat of jazm", " — nâkıs; tâ onun ismi; şart fiili, mahallen meczûm")), \
        PART("إِنَّمَا", "innama", "كَافَّةٌ وَمَكْفُوفَةٌ تُفِيدُ الْحَصْرَ: «إِنَّ» كَفَّتْهَا «مَا» عَنِ الْعَمَلِ.", "إِنَّمَا «only»: إِنَّ held off from governing by مَا — it restricts.", "«İnnemâ» kâffe ve mekfûfe, hasr ifade eder.", ["innama-kaffa", "aqsam-al-qasr"])
TITLES = [{"ar": "كُنْتُ بِالْأَمْسِ عَبْدًا", "en": "Yesterday I was a slave", "tr": "Dün bir köleydim"},
          {"ar": "فَذَرْنِي وَعَمَلِي لِلّٰهِ", "en": "Leave me to my work for God", "tr": "Beni Allah için amelimle baş başa bırak"}]
S1 = [
 SEN(1, "He said: I was told, from Abū al-Yamān al-Ḥimṣī, from Jarīr ibn ʿUthmān, from ʿAbd al-Raḥmān ibn Maysara, from Ibn Murāhin(?), who said:",
     "Dedi ki: Bana Ebü'l-Yemân el-Hımsî'den, o Cerîr b. Osman'dan, o Abdurrahman b. Meysere'den, o İbn M-r-h-n'den haber verildi; o dedi ki:",
 [QALA_HID(IBN_SAD), VERB("أُخْبِرْتُ", "akhbara", "mtu", form="form-iv-verbs", g=["naib-al-fail"], note=(" — مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ نَائِبُ الْفَاعِلِ", " — in the passive; the ta («I») is its deputy doer", " — meçhul; tâ nâib-i fâil")),
  AN(hang=UKH), NOUN("أَبِي", "ab", "majr", by="عَنْ", sign="5", mudaf=True), NAME("الْيَمَانِ", "yaman-name", "mi"),
  NOUN("الْحِمْصِيِّ", "himsi", "naat", "jarr", of=("أَبِي الْيَمَانِ", "Abū al-Yamān", "Ebü'l-Yemân"), note=(" — نِسْبَةٌ إِلَى حِمْصَ", " — a nisba to Ḥimṣ", " — Hıms'a nisbet")),
  AN(hang=UKH), NAME("جَرِيرِ", "jarir", "majr", by="عَنْ", note=NT), BN("jarr", ("جَرِيرِ", "Jarīr", "Cerîr")), NAME("عُثْمَانَ", "uthman", "mi", dipt="nun"),
  AN(hang=UKH), NOUN("عَبْدِ", "abd", "majr", by="عَنْ", mudaf=True), NAME("الرَّحْمٰنِ", "rahman", "mi"), BN("jarr", ("عَبْدِ الرَّحْمٰنِ", "ʿAbd al-Raḥmān", "Abdurrahman"), alif=True),
  NAME("مَيْسَرَةَ", "maysara", "mi", dipt="tanith"),
  AN(hang=UKH), NOUN("ابْنِ", "ibn", "majr", by="عَنْ", mudaf=True),
  PART("مراهن", "murahin", "مُضَافٌ إِلَيْهِ — اسْمُ رَاوٍ لَمْ نَقْطَعْ بِضَبْطِهِ فَتُرِكَ غَيْرَ مَشْكُولٍ لِلْعَالِمِ.", "The second term of the iḍāfa — a narrator's name whose vowels we could not settle, left unvowelled for the scholar.",
       "Muzâfun ileyh — harekesini kesinleştiremediğimiz bir râvi adı; hocaya harekesiz bırakıldı.", ["idafa-definiteness"], pos="propn"),
  QALA_HID(("ابْنِ مراهن", "Ibn Murāhin(?)", "İbn M-r-h-n"))]),
 SEN(2, "People used to come to Bilāl and speak of his merit and of the good God had allotted him, and he would say: I am only an Abyssinian; yesterday I was a slave.",
     "İnsanlar Bilâl'e gelir, onun faziletini ve Allah'ın ona ayırdığı hayrı anarlardı; o ise: Ben sadece bir Habeşliyim; dün bir köleydim! derdi.",
 [VERB("كَانَ", "kana", "m", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ", " — the defective verb", " — nâkıs fiil")),
  NOUN("أُنَاسٌ", "unas", "ismk"),
  VERB("يَأْتُونَ", "ata", "u5", g=["mahmuz-verbs", "naqis-verbs"], cl=KH_KANA), NAME("بِلَالًا", "bilal", "maful"),
  VERB("فَيَذْكُرُونَ", "dhakara", "u5", pre=("fa",)), NOUN("فَضْلَهُ", "fadl", "maful", enc="هُ", ref=BL),
  PART("وَمَا", "ma-mawsula", "الْوَاوُ عَاطِفَةٌ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَعْطُوفٌ عَلَى «فَضْلَهُ».", "The waw conjoins; مَا «what» is a relative noun, conjoined to «his merit», in the seat of nasb.",
       "Vâv atıf; «mâ» ism-i mevsûl, «fadlehû»ya ma'tûf, mahallen mansûb.", ["ism-mawsul", "atf-nasaq"], pre=("wa",), pos="pron"),
  VERB("قَسَمَ", "qasama", "m", doer_after=True, cl=SILA_), ALLAH_FAIL(),
  PRON_J("لَهُ", "li", "هُ", H("بِـ«قَسَمَ»", "«allotted»", "«kasame»ye"), ref=BL),
  PREPT("مِنَ", "min", H("بِمَحْذُوفٍ حَالٍ مِنَ الْعَائِدِ الْمَحْذُوفِ", "an omitted ḥāl of the dropped returning pronoun", "mahzûf âid zamirden mahzûf hâle"), ("، بَيَانِيَّةٌ، وَحُرِّكَتْ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ", " that explains, voweled with fatḥa before the sukūn", " (beyân; iki sâkin karşılaştığı için fetha)")),
  NOUN("الْخَيْرِ", "khayr", "majr"),
  VERB("فَكَانَ", "kana", "m", form="kana-wa-akhawatuha", g=["hollow-verbs"], pre=("fa",), hid="هُوَ", ref=BL, note=(" — نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ", " — defective; its noun is hidden", " — nâkıs; ismi gizli")),
  VERB("يَقُولُ", "qala", "u", g=["hollow-verbs"], hid="هُوَ", ref=BL, cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ»، وَمَا بَعْدَهَا مَقُولُ الْقَوْلِ", "; the clause is the predicate of كَانَ; what follows is what he said", "; cümle «kâne»nin haberi; sonrası mekūlü'l-kavl"), p=":"),
  PART("إِنَّمَا", "innama", "كَافَّةٌ وَمَكْفُوفَةٌ تُفِيدُ الْحَصْرَ: «إِنَّ» كَفَّتْهَا «مَا» عَنِ الْعَمَلِ.", "إِنَّمَا «only»: إِنَّ held off from governing by مَا — it restricts.", "«İnnemâ» kâffe ve mekfûfe, hasr ifade eder.", ["innama-kaffa", "aqsam-al-qasr"]),
  PART("أَنَا", "ana", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «I», the mubtadaʾ.", "Munfasıl zamir «ene», mübtedâ, mahallen merfû.", ["mubtada-khabar"], pos="pron"),
  NOUN("حَبَشِيٌّ", "habashi", "khabar", note=(" — نِسْبَةٌ إِلَى الْحَبَشَةِ", " — a nisba to Abyssinia", " — Habeşistan'a nisbet")),
  VERB("كُنْتُ", "kana", "mtu", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ، وَالتَّاءُ اسْمُهُ", " — defective; the ta is its noun", " — nâkıs; tâ onun ismi"), cl=(" — وَالْجُمْلَةُ نَعْتٌ لِـ«حَبَشِيٌّ» فِي مَحَلِّ رَفْعٍ", "; the clause describes «an Abyssinian», in the seat of raf'", "; cümle «habeşî»nin na'tı, mahallen merfû")),
  NOUN("بِالْأَمْسِ", "ams", "majr", pre=("bi",), note=(" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«كُنْتُ»؛ وَ«الْأَمْسِ» بِالْأَلِفِ وَاللَّامِ مُعْرَبٌ", " — the ba means «in»; the phrase hangs on «I was»; with the article, al-ams is declined", " — bâ «fî» anlamında; câr-mecrûr «kuntu»ya müteallik; harf-i ta'rîfle «el-ems» mu'reb")),
  NOUN("عَبْدًا", "abd", "khk", p=".")]),
]
S2 = [
 SEN(3, "He said: Muḥammad ibn ʿUbayd al-Ṭanāfisī told us; he said: Ismāʿīl ibn Abī Khālid told us, from Qays, who said:",
     "Dedi ki: Bize Muhammed b. Ubeyd et-Tanâfisî haber verdi; dedi ki: Bize İsmâil b. Ebî Hâlid, Kays'tan haber verdi; o dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("مُحَمَّدُ", "muhammad", "fail", note=NT), BN("raf", ("مُحَمَّدُ", "Muḥammad", "Muhammed")), NAME("عُبَيْدٍ", "ubayd-name", "mi"),
  NOUN("الطَّنَافِسِيُّ", "tanafisi", "naat", "raf", of=("مُحَمَّدُ", "Muḥammad", "Muhammed"), note=(" — نِسْبَةٌ إِلَى الطَّنَافِسِ", " — a nisba to the carpets (ṭanāfis)", " — halılara (tanâfis) nisbet")),
  QALA_HID(("مُحَمَّدِ بْنِ عُبَيْدٍ", "Muḥammad ibn ʿUbayd", "Muhammed b. Ubeyd")), ISNAD_AKHBARANA(),
  NAME("إِسْمَاعِيلُ", "ismail", "fail", dipt="ujma"), BN("raf", ("إِسْمَاعِيلُ", "Ismāʿīl", "İsmâil")), NOUN("أَبِي", "ab", "mi", sign="5", mudaf=True), NAME("خَالِدٍ", "khalid", "mi"),
  AN(hang=AKH), NAME("قَيْسٍ", "qays-name-tf", "majr", by="عَنْ", note=(" — هُوَ قَيْسُ بْنُ أَبِي حَازِمٍ", " — Qays ibn Abī Ḥāzim", " — Kays b. Ebî Hâzim")),
  QALA_HID(("قَيْسٍ", "Qays", "Kays"))]),
 SEN(4, "Bilāl said to Abū Bakr, when the Messenger of God — God bless him and grant him peace — died:",
     "Resûlullah — Allah ona salât ve selâm etsin — vefat ettiğinde Bilâl Ebû Bekir'e dedi ki:",
 [QALA_AFTER(), NAME("بِلَالٌ", "bilal", "fail"),
  NOUN("لِأَبِي", "ab", "majr", sign="5", pre=("li",), mudaf=True, note=("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ»", " — the phrase hangs on «said»", " — câr-mecrûr «kâle»ye müteallik")), NAME("بَكْرٍ", "bakr", "mi"),
  NOUN("حِينَ", "hina", "zarf", note=(" — ظَرْفُ زَمَانٍ مُتَعَلِّقٌ بِـ«قَالَ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", " — of time, hanging on «said», annexed to the clause after it", " — zaman zarfı, «kâle»ye müteallik, sonraki cümleye muzâf")),
  VERB("تُوُفِّيَ", "tawaffa", "p", form="form-v-verbs", g=["naqis-verbs", "al-majhul-fil-kafiya"], doer_after=True, note=(" — ضُمَّ أَوَّلُهُ وَثَانِيهِ لِأَنَّهُ مَبْدُوءٌ بِتَاءٍ زَائِدَةٍ", " — its first and second letters take ḍamma, as it opens with an added ta", " — zâid tâ ile başladığı için ilk iki harfi ötreli")),
  *RASUL("naib", p=":")]),
 SEN(5, "If you bought me only for yourself, then keep me;",
     "Eğer beni sadece kendin için satın aldıysan, beni tut;",
 [*KUNTA(pre=()), ISHTARAYTANI(),
  NOUN("لِنَفْسِكَ", "nafs", "majr", pre=("li",), enc="كَ", ref=AB, note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اشْتَرَى»", " — the phrase hangs on «bought»", " — câr-mecrûr «iştarâ»ya müteallik")),
  tok("فَأَمْسِكْنِي", "amsaka", "verb", ["form-iv-verbs", "al-fa-fi-jawab-al-shart", "ya-al-mutakallim", "maful-bihi"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَأَمْسِكْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
      "The fa ties the answer; «keep» is an imperative built on sukūn, its doer the hidden «you»; the nūn guards it and the ya («me») is its object — the answer of the condition, in the seat of jazm.",
      "Fâ şartın cevabını bağlar; «emsik» sükûn üzere mebnî emir, fâili gizli «ente»; nûn vikâye, yâ (beni) mef'ûlün bih — şartın cevabı, mahallen meczûm.", punct="؛",
      segments=[seg("فَ", "fa", "conj"), seg("أَمْسِكْ", "amsaka", "verb"), seg("نِي", "pron-1s", "pron")])]),
 SEN(6, "and if you bought me only for God, then leave me to my work for God.",
     "eğer beni sadece Allah için satın aldıysan, beni Allah için amelimle baş başa bırak.",
 [*KUNTA(), ISHTARAYTANI(),
  PART("لِلّٰهِ", "li", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اشْتَرَى».", "The lam «for», a jarr letter, with the name of God in jarr — the phrase hangs on «bought».",
       "Lâm ta'lîl için cer harfi, lafza-i celâl mecrûr — câr-mecrûr «iştarâ»ya müteallik.", ["huruf-jarr", "lam-taleel"], pre=("li",), s="allah", spos="propn"),
  tok("فَذَرْنِي", "wadhara", "verb", ["imperative-amr", "al-fa-fi-jawab-al-shart", "maful-bihi", "mithal-verbs"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَذَرْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
      "The fa ties the answer; ذَرْ «leave» is an imperative built on sukūn; the nūn guards it and the ya («me») is its object; its doer is the hidden «you» — the answer of the condition, in the seat of jazm.",
      "Fâ şartın cevabını bağlar; «zer» sükûn üzere mebnî emir; nûn vikâye, yâ (beni) mef'ûlün bih; fâili gizli «ente» — şartın cevabı, mahallen meczûm.",
      segments=[seg("فَ", "fa", "conj"), seg("ذَرْ", "wadhara", "verb"), seg("نِي", "pron-1s", "pron")]),
  NOUN("وَعَمَلِي", "amal-work", "atf", "nasb", sign="ya", pre=("wa",), enc="ي", of=("الْيَاءِ", "me", "beni"), note=(" — مَعْطُوفٌ عَلَى يَاءِ الْمُتَكَلِّمِ الْمَفْعُولِ بِهِ (أَوِ الْوَاوُ لِلْمَعِيَّةِ وَهُوَ مَفْعُولٌ مَعَهُ)", " — conjoined to the object «me» (or the waw of company, and it is the mafʿūl maʿah)", " — mef'ûl olan yâya ma'tûf (ya da vâv maiyyet içindir, mef'ûlün meah)")),
  PART("لِلّٰهِ", "li", "اللَّامُ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَمَلِي».", "The lam, a jarr letter, with the name of God in jarr — the phrase hangs on «my work».",
       "Lâm cer harfi, lafza-i celâl mecrûr — câr-mecrûr «amelî»ye müteallik.", ["huruf-jarr"], pre=("li",), s="allah", spos="propn", p=".")]),
]
CHAPS = [S1, S2]
NEW_GLOSS = {
 "himsi": NN("حِمْصِيّ", "ح م ص", "of Ḥimṣ (a nisba)", "Hımslı (nisbe)"),
 "maysara": NP("مَيْسَرَة", "Maysara — a man's name", "Meysere — erkek adı"),
 "murahin": NP("مراهن", "Ibn M-r-h-n — a narrator; the vowels of the name are left for the scholar", "İbn M-r-h-n — bir râvi; adın harekeleri hocaya bırakıldı"),
 "habashi": NN("حَبَشِيّ", "ح ب ش", "an Abyssinian", "Habeşli"),
 "tanafisi": NN("طَنَافِسِيّ", "ط ن ف س", "al-Ṭanāfisī (a nisba to carpets)", "et-Tanâfisî (halıya nisbet)"),
}
GLOSS_HERE = {"yaman-name": ("al-Yamān — in the kunya «Abū al-Yamān» (al-Ḥakam ibn Nāfiʿ al-Ḥimṣī)", "el-Yemân — «Ebü'l-Yemân» künyesinde (el-Hakem b. Nâfi' el-Hımsî)"),
              "jarir": ("Jarīr — here Jarīr ibn ʿUthmān al-Raḥabī", "Cerîr — burada Cerîr b. Osman er-Rahabî"),
              "qays-name-tf": ("Qays — here Qays ibn Abī Ḥāzim", "Kays — burada Kays b. Ebî Hâzim"), "khalid": ("Khālid — in «Ismāʿīl ibn Abī Khālid»", "Hâlid — «İsmâil b. Ebî Hâlid»de")}
MANIFEST = manifest(SLUG, 5, {"ar": "إِنَّمَا أَنَا حَبَشِيٌّ", "en": "I Am Only an Abyssinian", "tr": "Ben Sadece Bir Habeşliyim"},
  {"ar": "تَوَاضُعُ بِلَالٍ وَكَلِمَتُهُ لِأَبِي بَكْرٍ", "en": "Bilāl's humility, and his word to Abū Bakr", "tr": "Bilâl'in tevazuu ve Ebû Bekir'e sözü"}, "sahaba",
  "Bilāl ibn Rabāḥ's entry, vol. 3, printed p. 180 (Shamela p. 858)", "Bilâl b. Rebâh maddesi, cilt 3, matbû s. 180 (Şâmile s. 858)", "تَرْجَمَةُ بِلَالِ بْنِ رَبَاحٍ، الْجُزْءُ ٣، ص ١٨٠ (الشَّامِلَةُ ص ٨٥٨)",
  "two consecutive akhbār, each whole with its isnād: «قال: أخبرت عن أبي اليمان» … «كنت بالأمس عبدا.» and «قال: أخبرنا محمد بن عبيد الطنافسي» … «فذرني وعملي لله.», one chapter each",
  "art arda iki haber, her biri isnadıyla tam: «قال: أخبرت عن أبي اليمان» … «كنت بالأمس عبدا.» ve «قال: أخبرنا محمد بن عبيد الطنافسي» … «فذرني وعملي لله.»; her biri bir bölüm",
  "خَبَرَانِ مُتَتَالِيَانِ بِإِسْنَادَيْهِمَا، لِكُلٍّ مِنْهُمَا فَصْلٌ",
  kept=[("«عبد الرحمن ابن ميسرة» بِالْأَلِفِ كَمَا طُبِعَ", "«عبد الرحمن ابن ميسرة» with the alif of ابن, as printed", "«عبد الرحمن ابن ميسرة» ibn'in elifiyle, baskıdaki gibi")],
  hoca=[("the narrator «ابن مراهن» left unvowelled (not settled from the rijāl books)", "«ابن مراهن» râvisi harekesiz bırakıldı (ricâl kitaplarından kesinleştirilemedi)"),
        ("«وَعَمَلِي»: conjoined to the object ya, or a mafʿūl maʿah", "«وَعَمَلِي»: mef'ûl yâya ma'tûf ya da mef'ûlün meah")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE)
