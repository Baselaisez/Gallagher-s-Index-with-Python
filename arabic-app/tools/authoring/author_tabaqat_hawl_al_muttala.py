"""Author content/samples/tabaqat-hawl-al-muttala — «مِنْ هَوْلِ الْمُطَّلَعِ», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Companions, ʿUmar ibn al-Khaṭṭāb's entry (his death), vol. 3 p. 270
(Shamela p. 948): al-Shaʿbī's khabar whole, isnād included — «قال: أخبرنا يزيد بن هارون» … «من هول المطلع.».
The exact passage: research/sources/tabaqat-hawl-al-muttala-src.txt. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_tabaqat_hawl_al_muttala.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-hawl-al-muttala"
UM = ("عُمَرَ", "ʿUmar", "Ömer")
AKH = H("بِـ«أَخْبَرَنَا»", "«told us»", "«ahberanâ»ya")
TITLES = [{"ar": "مِنْ هَوْلِ الْمُطَّلَعِ", "en": "From the terror of the rising", "tr": "Muttala'ın dehşetinden"}]
S1 = [
 SEN(1, "He said: Yazīd ibn Hārūn told us; he said: Ismāʿīl ibn Abī Khālid told us, from al-Shaʿbī, who said:",
     "Dedi ki: Bize Yezîd b. Hârûn haber verdi; dedi ki: Bize İsmâil b. Ebî Hâlid, Şa'bî'den haber verdi; o dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("يَزِيدُ", "yazid", "fail", dipt="wazn"), BN("raf", ("يَزِيدُ", "Yazīd", "Yezîd")), NAME("هَارُونَ", "harun", "mi", dipt="ujma"),
  QALA_HID(("يَزِيدَ بْنِ هَارُونَ", "Yazīd ibn Hārūn", "Yezîd b. Hârûn")), ISNAD_AKHBARANA(),
  NAME("إِسْمَاعِيلُ", "ismail", "fail", dipt="ujma"), BN("raf", ("إِسْمَاعِيلُ", "Ismāʿīl", "İsmâil")), NOUN("أَبِي", "ab", "mi", sign="5", mudaf=True), NAME("خَالِدٍ", "khalid", "mi"),
  AN("عَنِ", AKH), NAME("الشَّعْبِيِّ", "shabi", "majr", by="عَنْ"), QALA_HID(("الشَّعْبِيِّ", "al-Shaʿbī", "Şa'bî"))]),
 SEN(2, "ʿUmar ibn al-Khaṭṭāb called for milk after he had been stabbed, and drank; it came out of his wound, and he said: God is greatest!",
     "Ömer b. el-Hattâb hançerlendikten sonra süt istedi ve içti; süt yarasından dışarı çıktı; bunun üzerine: Allahu ekber! dedi.",
 [VERB("دَعَا", "daa", "ma", g=["naqis-verbs"], doer_after=True), NAME("عُمَرُ", "umar", "fail", note=NT), BN("raf", ("عُمَرُ", "ʿUmar", "Ömer")), NAME("الْخَطَّابِ", "khattab", "mi"),
  NOUN("بِلَبَنٍ", "laban", "majr", pre=("bi",), note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«دَعَا»: طَلَبَهُ", " — the phrase hangs on «called for»", " — câr-mecrûr «de'â»ya müteallik: onu istedi")),
  NOUN("بَعْدَ", "bada", "zarf", mudaf=True, note=(" — ظَرْفُ زَمَانٍ مُتَعَلِّقٌ بِـ«دَعَا»", " — of time, hanging on «called»", " — zaman zarfı, «de'â»ya müteallik")),
  PART("مَا", "ma-masdariyya", "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِنَ الْفِعْلِ بَعْدَهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ: بَعْدَ طَعْنِهِ.", "مَا that makes a maṣdar — with the verb after it, the second term of «after»: «after his stabbing».",
       "Masdar harfi «mâ» — sonraki fiille birlikte «ba'de»nin muzâfun ileyhi: «yaralanmasından sonra».", ["an-masdariyya"]),
  VERB("طُعِنَ", "taana", "p", g=["naib-al-fail"], hid="هُوَ", ref=UM),
  VERB("فَشَرِبَ", "shariba", "m", hid="هُوَ", ref=UM, pre=("fa",)),
  VERB("فَخَرَجَ", "kharaja", "m", hid="هُوَ", ref=("اللَّبَنِ", "the milk", "süt"), pre=("fa",)),
  PREPT("مِنْ", "min", H("بِـ«خَرَجَ»", "«came out»", "«harace»ye")), NOUN("جِرَاحَتِهِ", "jiraha", "majr", enc="هِ", ref=UM),
  QALA_HID(UM, pre=("fa",)), ALLAH_MUBT(), NOUN("أَكْبَرُ", "akbar", "khabar", g=["ism-tafdil"], note=(" — اسْمُ تَفْضِيلٍ لَا يُنَوَّنُ", " — an elative, without tanwin", " — ism-i tafdîl, tenvinsiz"), p=".")]),
 SEN(3, "His companions began to praise him, and he said: Whoever is deceived by his length of life is deceived indeed.",
     "Meclisindekiler onu övmeye başladılar; bunun üzerine dedi ki: Ömrünün aldattığı kimse, gerçekten aldanmıştır.",
 [VERB("فَجَعَلَ", "jaala", "m", g=["afal-al-muqaraba"], doer_after=True, pre=("fa",), note=(" — مِنْ أَفْعَالِ الشُّرُوعِ", " — a verb of beginning", " — şürû' fiillerinden")),
  NOUN("جُلَسَاؤُهُ", "jalis", "ismk", enc="هُ", ref=UM, note=(" — اسْمُ «جَعَلَ»، جَمْعُ جَلِيسٍ", " — the noun of «began», plural of جَلِيس", " — «ceale»nin ismi, celîs'in çoğulu")),
  VERB("يُثْنُونَ", "athna-ant", "u5", form="form-iv-verbs", g=["naqis-verbs"], cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «جَعَلَ»", "; the clause is the predicate of «began»", "; cümle «ceale»nin haberi")),
  PRON_J("عَلَيْهِ", "ala", "هِ", H("بِـ«يُثْنُونَ»", "«praise»", "«yusnûne»ye"), ref=UM),
  QALA_HID(UM, pre=("fa",)),
  PART("إِنَّ", "inna", "حَرْفُ تَوْكِيدٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ.", "إِنَّ, the particle of emphasis that puts its noun in nasb.", "«İnne» te'kîd ve nasb harfi.", ["inna-wa-akhawatuha"]),
  PART("مَنْ", "man", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُ «إِنَّ».", "A relative noun «whoever», in the seat of nasb as the noun of إِنَّ.", "İsm-i mevsûl «men», mahallen mansûb, «inne»nin ismi.", ["ism-mawsul", "inna-wa-akhawatuha"], pos="pron"),
  VERB("غَرَّهُ", "gharra", "m", g=["doubled-verbs"], enc="هُ", encref=("«مَنْ»", "«whoever»", "«men»"), doer_after=True, cl=SILA_),
  NOUN("عُمُرُهُ", "umr", "fail", enc="هُ", ref=("«مَنْ»", "«whoever»", "«men»"), note=(" — وَالْعُمُرُ: مُدَّةُ الْحَيَاةِ", " — ʿumur: the span of life", " — umur: hayat süresi")),
  NOUN("لَمَغْرُورٌ", "maghrur", "khinna", pre=("la-muz",), g=["ism-maful"], p=".")]),
 SEN(4, "By God, I would love to come out of it as I went into it.",
     "Vallahi, ona (halifeliğe) girdiğim gibi ondan çıkmayı ne çok isterdim.",
 [WALLAHI(),
  VERB("لَوَدِدْتُ", "wadda", "mtu", g=["doubled-verbs"], note=(" — وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَفُكَّ إِدْغَامُهُ لِاتِّصَالِهِ بِالضَّمِيرِ", " — the lam answers the oath; the doubling is undone before the pronoun", " — lâm kasemin cevabında; zamire bitiştiği için idgâm çözüldü")),
  PART("أَنِّي", "anna", "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْيَاءُ اسْمُهَا — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ مَفْعُولٌ بِهِ لِـ«وَدِدْتُ».", "أَنَّ «that» with the ya «I» as its noun — the clause stands as a maṣdar, the object of «I would love».",
       "«Enne» ve ismi yâ — «enne» ve sonrası masdar te'vîlinde «vedidtu»nun mef'ûlü.", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"], enc="ي"),
  VERB("أَخْرُجُ", "kharaja", "u", hid="أَنَا", ref=UM, cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ»", "; the clause is the predicate of أَنَّ", "; cümle «enne»nin haberi")),
  PRON_J("مِنْهَا", "min", "هَا", H("بِـ«أَخْرُجُ»", "«come out»", "«ahrucu»ya"), ref=("الْخِلَافَةِ", "the caliphate", "hilâfet")),
  PART("كَمَا", "ka", "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَمَا حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْكَافِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ أَوْ نَعْتٍ لِمَصْدَرٍ مَحْذُوفٍ.",
       "The kaf «as», a jarr letter, with مَا that makes a maṣdar — «like my going in».", "Kâf teşbih için cer harfi; «mâ» masdar harfi — «girişim gibi».", ["huruf-jarr", "an-masdariyya"], pre=("ka",), s="ma-masdariyya", spos="part"),
  VERB("دَخَلْتُ", "dakhala", "mtu"), PRON_J("فِيهَا", "fi", "هَا", H("بِـ«دَخَلْتُ»", "«went in»", "«dehaltu»ya"), ref=("الْخِلَافَةِ", "the caliphate", "hilâfet"), p=".")]),
 SEN(5, "By God, if I had all that the sun rises upon, I would ransom myself with it from the terror of the rising.",
     "Vallahi, güneşin üzerine doğduğu her şey benim olsaydı, muttala'ın (kıyamet sahnesinin) dehşetinden kurtulmak için onu fidye verirdim.",
 [WALLAHI(),
  PART("لَوْ", "law", "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ غَيْرُ جَازِمٍ مَبْنِيٌّ عَلَى السُّكُونِ.", "لَوْ «if (it were)», the particle of a thing withheld because another is withheld; it governs no jazm.", "«Lev» imtinâ' li-imtinâ' harfi, cezmetmez.", ["al-qasam-wal-shart-fil-kafiya"]),
  VERB("كَانَ", "kana", "m", form="kana-wa-akhawatuha", g=["hollow-verbs"], note=(" — نَاقِصٌ، فِعْلُ الشَّرْطِ", " — defective, the verb of the condition", " — nâkıs, şart fiili")),
  PRON_J("لِي", "li", "ي", H("بِمَحْذُوفٍ خَبَرِ «كَانَ» مُقَدَّمٍ", "the fronted, omitted predicate of كَانَ", "«kâne»nin öne alınmış mahzûf haberine"), ref=UM),
  PART("مَا", "ma-mawsula", "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ اسْمُ «كَانَ» مُؤَخَّرٌ.", "A relative noun «what», the noun of كَانَ placed after its predicate.", "İsm-i mevsûl «mâ», sonraya bırakılmış «kâne»nin ismi, mahallen merfû.", ["ism-mawsul", "kana-wa-akhawatuha"], pos="pron"),
  VERB("طَلَعَتْ", "talaa", "mt", doer_after=True, cl=SILA_),
  PRON_J("عَلَيْهِ", "ala", "هِ", H("بِـ«طَلَعَتْ»", "«rises»", "«tala'at»a"), ref=("«مَا»", "«what»", "«mâ»")), NOUN("الشَّمْسُ", "shams", "fail"),
  VERB("لَافْتَدَيْتُ", "iftada-tf", "mtu", form="form-viii-verbs", g=["naqis-verbs"], note=(" — وَاللَّامُ وَاقِعَةٌ فِي جَوَابِ «لَوْ»", " — the lam opens the answer of لَوْ", " — lâm «lev»in cevabında"),
       cl=(" — وَالْجُمْلَةُ جَوَابُ «لَوْ» لَا مَحَلَّ لَهَا، وَسَدَّتْ مَسَدَّ جَوَابِ الْقَسَمِ", "; the answer of لَوْ, with no seat, standing also for the oath's answer", "; «lev»in cevabı, mahalli yok; kasemin cevabı yerine de geçer")),
  PRON_J("بِهِ", "bi", "هِ", H("بِـ«افْتَدَيْتُ»", "«ransom»", "«iftedeytu»ya"), ref=("«مَا»", "«what»", "«mâ»")),
  PREPT("مِنْ", "min", H("بِـ«افْتَدَيْتُ»", "«ransom»", "«iftedeytu»ya")), NOUN("هَوْلِ", "hawl-amr", "majr", mudaf=True),
  NOUN("الْمُطَّلَعِ", "muttala", "mi", note=(" — الْمُطَّلَعُ: مَوْضِعُ الِاطِّلَاعِ مِنْ إِشْرَافٍ، وَأُرِيدَ بِهِ مَا يُشْرِفُ عَلَيْهِ الْمَيِّتُ مِنْ أَمْرِ الْآخِرَةِ", " — al-muṭṭalaʿ: a place one looks down from; here what the dead man looks out upon of the next world", " — el-muttala': yukarıdan bakılan yer; burada ölünün âhiret hâlinden göreceği şey"), p=".")]),
]
CHAPS = [S1]
NEW_GLOSS = {
 "maghrur": NN("مَغْرُور", "غ ر ر", "deceived, deluded", "aldanmış"),
 "muttala": NN("مُطَّلَع", "ط ل ع", "a place one looks down from; (here) the scene of the next world beheld at death", "yukarıdan bakılan yer; (burada) ölümde görülen âhiret manzarası"),
}
GLOSS_HERE = {"yazid": ("Yazīd — here Yazīd ibn Hārūn al-Wāsiṭī", "Yezîd — burada Yezîd b. Hârûn el-Vâsıtî"), "harun": ("Hārūn — Yazīd's father", "Hârûn — Yezîd'in babası"),
              "khalid": ("Khālid — in «Ismāʿīl ibn Abī Khālid»", "Hâlid — «İsmâil b. Ebî Hâlid»de")}
MANIFEST = manifest(SLUG, 5, {"ar": "مِنْ هَوْلِ الْمُطَّلَعِ", "en": "From the Terror of the Rising", "tr": "Muttala'ın Dehşetinden"},
  {"ar": "كَلِمَةُ عُمَرَ بَعْدَ مَا طُعِنَ", "en": "ʿUmar's words after he was stabbed", "tr": "Ömer'in yaralandıktan sonraki sözü"}, "sahaba",
  "ʿUmar ibn al-Khaṭṭāb's entry, vol. 3, printed p. 270 (Shamela p. 948)", "Ömer b. el-Hattâb maddesi, cilt 3, matbû s. 270 (Şâmile s. 948)", "تَرْجَمَةُ عُمَرَ بْنِ الْخَطَّابِ، الْجُزْءُ ٣، ص ٢٧٠ (الشَّامِلَةُ ص ٩٤٨)",
  "al-Shaʿbī's khabar whole, isnād included, from «قال: أخبرنا يزيد بن هارون» to «من هول المطلع.»", "Şa'bî'nin haberi, isnadıyla tam, «قال: أخبرنا يزيد بن هارون»dan «من هول المطلع.»a kadar",
  "خَبَرُ الشَّعْبِيِّ كُلُّهُ بِإِسْنَادِهِ",
  hoca=[("«مَنْ غَرَّهُ عُمُرُهُ» — the e-text «عمره» read عُمُرُهُ «his length of life»", "«مَنْ غَرَّهُ عُمُرُهُ» — e-metindeki «عمره» عُمُرُهُ «ömrü» okundu"),
        ("«فَخَرَجَ» — its hidden doer taken as the milk", "«فَخَرَجَ» — gizli fâili süt olarak alındı")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE)
