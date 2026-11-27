"""Author content/samples/tabaqat-lastu-bi-khalifat-allah — «لَسْتُ بِخَلِيفَةِ اللهِ», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Companions, Abū Bakr's entry, vol. 3 p. 137 (Shamela p. 815):
the whole khabar of Ibn Abī Mulayka, isnād included — «قال: أخبرنا وكيع بن الجراح» … «أنا راض بذلك.».
The exact passage: research/sources/tabaqat-lastu-bi-khalifat-allah-src.txt. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_tabaqat_lastu_bi_khalifat_allah.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-lastu-bi-khalifat-allah"
ISNAD_V = H("بِـ«أَخْبَرَنَا»", "«told us»", "«ahberanâ»ya")
AB = ("أَبِي بَكْرٍ", "Abū Bakr", "Ebû Bekir")
TITLES = [{"ar": "لَسْتُ بِخَلِيفَةِ اللهِ", "en": "I am not God's caliph", "tr": "Ben Allah'ın halifesi değilim"}]
S1 = [
 SEN(1, "He said: Wakīʿ ibn al-Jarrāḥ told us, from Nāfiʿ ibn ʿUmar, from Ibn Abī Mulayka, who said:",
     "Dedi ki: Bize Vekî' b. el-Cerrâh, Nâfi' b. Ömer'den, o İbn Ebî Müleyke'den haber verdi; o dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(),
  NAME("وَكِيعُ", "waki", "fail", note=NT), BN("raf", ("وَكِيعُ", "Wakīʿ", "Vekî'")), NAME("الْجَرَّاحِ", "jarrah", "mi"),
  AN(hang=ISNAD_V), NAME("نَافِعِ", "nafi-name", "majr", by="عَنْ", note=NT), BN("jarr", ("نَافِعِ", "Nāfiʿ", "Nâfi'")), NAME("عُمَرَ", "umar", "mi", dipt="adl"),
  AN("عَنِ", ISNAD_V), NOUN("ابْنِ", "ibn", "majr", by="عَنْ", mudaf=True), NOUN("أَبِي", "ab", "mi", sign="5", mudaf=True), NAME("مُلَيْكَةَ", "mulayka", "mi", dipt="tanith"),
  QALA_HID(("ابْنِ أَبِي مُلَيْكَةَ", "Ibn Abī Mulayka", "İbn Ebî Müleyke"))]),
 SEN(2, "A man said to Abū Bakr: O caliph of God!",
     "Bir adam Ebû Bekir'e: Ey Allah'ın halifesi! dedi.",
 [QALA_AFTER(), NOUN("رَجُلٌ", "rajul", "fail"),
  NOUN("لِأَبِي", "ab", "majr", sign="5", pre=("li",), mudaf=True, note=("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ»", " — the phrase hangs on «said»", " — câr-mecrûr «kâle»ye müteallik")),
  NAME("بَكْرٍ", "bakr", "mi", p=":"), YA(),
  NOUN("خَلِيفَةَ", "khalifa", "munada", mudaf=True, note=(" — مُنَادًى مُضَافٌ", " — a called noun that is annexed", " — muzâf münâdâ")), ALLAH_MI(p=".")]),
 SEN(3, "He said: I am not God's caliph; but I am the caliph of the Messenger of God.",
     "Dedi ki: Ben Allah'ın halifesi değilim; ama ben Resûlullah'ın halifesiyim.",
 [QALA_HID(AB, pre=("fa",)),
  VERB("لَسْتُ", "laysa", "mtu", form="kana-wa-akhawatuha", note=(" — فِعْلٌ نَاقِصٌ جَامِدٌ، وَالتَّاءُ اسْمُهُ", " — a rigid defective verb; the ta is its noun", " — câmid nâkıs fiil; tâ onun ismidir")),
  PART("بِخَلِيفَةِ", "bi", "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَخَلِيفَةِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا خَبَرُ «لَيْسَ»، مُضَافٌ.",
       "The ba is an extra jarr letter; «caliph» is in jarr in form, in nasb in its seat as the predicate of لَيْسَ, annexed.",
       "Bâ zâid cer harfi; «halîfe» lafzen mecrûr, mahallen mansûb «leyse»nin haberi, muzâf.", ["huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha"], pre=("bi",), s="khalifa", spos="noun"),
  ALLAH_MI(),
  PART("وَلٰكِنِّي", "lakinna", "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ، وَالنُّونُ لِلْوِقَايَةِ أُدْغِمَتْ فِي نُونِهِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.",
       "The waw conjoins; لٰكِنَّ «but», the particle of correction that puts its noun in nasb, its guarding nūn merged; the ya «I» is its noun.",
       "Vâv atıf; «lâkinne» istidrâk ve nasb harfi, vikâye nûnu onun nûnuna idgâm edildi; yâ (ben) onun ismi.", ["kaanna-lakinna-layta-laalla-fil-kafiya", "al-bariz-al-muttasil"], pre=("wa",), enc="ي"),
  NOUN("خَلِيفَةُ", "khalifa", "khinna", mudaf=True, note=(" — خَبَرُ «لٰكِنَّ»", " — the predicate of لٰكِنَّ", " — «lâkinne»nin haberi")),
  *RASUL("mi", salla=False, p=".")]),
 SEN(4, "I am content with that.",
     "Ben buna razıyım.",
 [PART("أَنَا", "ana", "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «I», in the seat of raf' as the mubtadaʾ.", "Munfasıl zamir «ene», mahallen merfû mübtedâ.", ["mubtada-khabar"], pos="pron"),
  NOUN("رَاضٍ", "radin", "khabar", sign="manq", note=(" — اسْمُ فَاعِلٍ مَنْقُوصٌ حُذِفَتْ يَاؤُهُ لِلتَّنْوِينِ", " — an active participle whose final ya drops before the tanwin", " — ism-i fâil, menkûs; yâsı tenvin yüzünden düştü"), g=["ism-maqsur-manqus", "ism-fail"]),
  PART("بِذٰلِكَ", "bi", "الْبَاءُ حَرْفُ جَرٍّ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَاضٍ».",
       "The ba is a jarr letter; «that» is a demonstrative in the seat of jarr — the phrase hangs on «content».", "Bâ cer harfi; «zâlike» işaret ismi, mahallen mecrûr — câr-mecrûr «râdın»a müteallik.", ["huruf-jarr", "asma-al-ishara-wa-sighuha"], pre=("bi",), s="dhalika", spos="pron", p=".")]),
]
CHAPS = [S1]
NEW_GLOSS = {
 "waki": NP("وَكِيع", "Wakīʿ (ibn al-Jarrāḥ, the Kūfan ḥadīth master)", "Vekî' (b. el-Cerrâh, Kûfeli hadis hâfızı)"),
 "jarrah": NP("الْجَرَّاح", "al-Jarrāḥ (Wakīʿ's father)", "el-Cerrâh (Vekî'in babası)"),
 "nafi-name": NP("نَافِع", "Nāfiʿ — a man's name (here Nāfiʿ ibn ʿUmar al-Jumaḥī)", "Nâfi' — erkek adı (burada Nâfi' b. Ömer el-Cumahî)"),
}
GLOSS_HERE = {"mulayka": ("Mulayka — in «Ibn Abī Mulayka», the Meccan Successor ʿAbd Allāh ibn ʿUbayd Allāh", "Müleyke — «İbn Ebî Müleyke»de; Mekkeli tâbiî Abdullah b. Ubeydullah")}
MANIFEST = manifest(SLUG, 2, {"ar": "لَسْتُ بِخَلِيفَةِ اللهِ", "en": "I Am Not God's Caliph", "tr": "Ben Allah'ın Halifesi Değilim"},
  {"ar": "أَبُو بَكْرٍ يَرُدُّ لَقَبًا", "en": "Abū Bakr turns down a title", "tr": "Ebû Bekir bir unvanı geri çevirir"}, "sahaba",
  "Abū Bakr's entry, vol. 3, printed p. 137 (Shamela p. 815)", "Ebû Bekir maddesi, cilt 3, matbû s. 137 (Şâmile s. 815)", "تَرْجَمَةُ أَبِي بَكْرٍ، الْجُزْءُ ٣، ص ١٣٧ (الشَّامِلَةُ ص ٨١٥)",
  "the whole khabar of Ibn Abī Mulayka, from «قال: أخبرنا وكيع بن الجراح» to «أنا راض بذلك.»", "İbn Ebî Müleyke haberinin tamamı, «قال: أخبرنا وكيع بن الجراح»den «أنا راض بذلك.»a kadar",
  "خَبَرُ ابْنِ أَبِي مُلَيْكَةَ كُلُّهُ، مِنْ «قَالَ: أَخْبَرَنَا وَكِيعُ بْنُ الْجَرَّاحِ» إِلَى «أَنَا رَاضٍ بِذٰلِكَ»")
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE)
