"""Author content/samples/tabaqat-said-ibn-al-musayyib — «مُنْذُ أَرْبَعِينَ سَنَةً», the shelf «مِنَ الطَّبَقَاتِ الْكُبْرَى» (v358-T).

RECEIVED TEXT: Ibn Saʿd, al-Ṭabaqāt al-kubrā (ed. ʿAṭā; Shamela 1686), the Successors, Saʿīd ibn al-Musayyib's entry, vol. 5 p. 99 (Shamela
p. 1527): the first two akhbār of the run on his prayer in congregation, each whole with its isnād — «قال: أخبرنا موسى بن إسماعيل» …
«منذ ثلاثين سنة.» and «قال: أخبرنا أنس بن عياض» … «منذ أربعين سنة.». The third (ʿUmrān's, «قال. ما فاتته …») is left: its «قال» and
«فاتته» do not agree in the e-text.
The exact passage: research/sources/tabaqat-said-ibn-al-musayyib-src.txt. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_tabaqat_said_ibn_al_musayyib.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from tabaqat_common import *

SLUG = "tabaqat-said-ibn-al-musayyib"
SA = ("سَعِيدِ بْنِ الْمُسَيّبِ", "Saʿīd ibn al-Musayyib", "Saîd b. el-Müseyyeb")
HD = H("بِـ«حَدَّثَنَا»", "«told us»", "«haddesenâ»ya")
AKH = H("بِـ«أَخْبَرَنَا»", "«told us»", "«ahberanâ»ya")
MUSAYYIB_NOTE = (" — وَتُرِكَتْ حَرَكَةُ يَائِهِ: يُقَالُ الْمُسَيَّبُ وَالْمُسَيِّبُ، وَيُرْوَى أَنَّ سَعِيدًا كَانَ يَكْرَهُ الْفَتْحَ", " — the vowel of its ya is left: al-Musayyab and al-Musayyib are both said, and Saʿīd is reported to have disliked the fatḥa", " — yâsının harekesi bırakıldı: Müseyyeb ve Müseyyib ikisi de söylenir; Saîd'in fethayı sevmediği rivayet edilir")
def MUNDHU(n_full, n_lex, p="."):
    return [PART("مُنْذُ", "mundhu", "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ فِي الزَّمَانِ مَبْنِيٌّ عَلَى الضَّمِّ.", "مُنْذُ «for, since», a jarr letter of the start of a time, built on ḍamma.", "«Münzü» zamanda başlangıç bildiren cer harfi, damme üzere mebnî.", ["huruf-jarr-nawadir", "huruf-jarr"], pos="prep"),
            NOUN(n_full, n_lex, "majr", by="مُنْذُ", sign="bn", note=(" — مِنْ أَلْفَاظِ الْعُقُودِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَنْفِيِّ", " — a tens-word; the phrase hangs on the negated verb", " — onlu sayı kelimesi; câr-mecrûr olumsuz fiile müteallik")),
            NOUN("سَنَةً", "sana", "tamyiz", p=p)]
TITLES = [{"ar": "مُنْذُ أَرْبَعِينَ سَنَةً", "en": "For forty years", "tr": "Kırk yıldır"}]
S1 = [
 SEN(1, "He said: Mūsā ibn Ismāʿīl told us; he said: ʿAbd al-Wāḥid ibn Ziyād told us; he said: ʿUthmān ibn Ḥakīm told us; he said: I heard Saʿīd ibn al-Musayyib say:",
     "Dedi ki: Bize Mûsâ b. İsmâil haber verdi; dedi ki: Bize Abdülvâhid b. Ziyâd anlattı; dedi ki: Bize Osman b. Hakîm anlattı; dedi ki: Saîd b. el-Müseyyeb'i şöyle derken işittim:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("مُوسَى", "musa", "fail", sign="maq", note=NT), BN("raf", ("مُوسَى", "Mūsā", "Mûsâ")), NAME("إِسْمَاعِيلَ", "ismail", "mi", dipt="ujma"),
  QALA_HID(("مُوسَى بْنِ إِسْمَاعِيلَ", "Mūsā ibn Ismāʿīl", "Mûsâ b. İsmâil")), ISNAD_HADDATHANA(), NOUN("عَبْدُ", "abd", "fail", mudaf=True), NOUN("الْوَاحِدِ", "wahid", "mi"),
  BN("raf", ("عَبْدُ الْوَاحِدِ", "ʿAbd al-Wāḥid", "Abdülvâhid")), NAME("زِيَادٍ", "ziyad-name", "mi"),
  QALA_HID(("عَبْدِ الْوَاحِدِ", "ʿAbd al-Wāḥid", "Abdülvâhid")), ISNAD_HADDATHANA(), NAME("عُثْمَانُ", "uthman", "fail", dipt="nun"), BN("raf", ("عُثْمَانُ", "ʿUthmān", "Osman")), NAME("حَكِيمٍ", "hakim-name", "mi"),
  QALA_HID(("عُثْمَانَ بْنِ حَكِيمٍ", "ʿUthmān ibn Ḥakīm", "Osman b. Hakîm")),
  VERB("سَمِعْتُ", "samia", "mtu", cl=(" — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", "; the clause is what is said", "; cümle mekūlü'l-kavl")),
  NAME("سَعِيدَ", "said-name", "maful", note=NT), BN("nasb", ("سَعِيدَ", "Saʿīd", "Saîd")), NAME("الْمُسَيّبِ", "musayyab", "mi", note=MUSAYYIB_NOTE),
  VERB("يَقُولُ", "qala", "u", g=["hollow-verbs"], hid="هُوَ", ref=SA, cl=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «سَعِيدَ»، وَمَا بَعْدَهَا مَقُولُ الْقَوْلِ", "; the clause is a ḥāl of «Saʿīd»; what follows is what he says", "; cümle «Saîd»den hâl; sonrası mekūlü'l-kavl"), p=":")]),
 SEN(2, "I have not heard a call to prayer among my family for thirty years.",
     "Otuz yıldır ailemin yanında ezan işitmedim.",
 [PART("مَا", "ma-nafiya", "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا عَمَلَ لَهُ.", "مَا negates; it governs nothing.", "«Mâ» nefy harfi, amel etmez.", ["anwa-ma"]),
  VERB("سَمِعْتُ", "samia", "mtu"), NOUN("تَأْذِينًا", "tadhin", "maful", g=["masdar", "form-ii-verbs"], note=(" — مَصْدَرُ «أَذَّنَ»: النِّدَاءُ لِلصَّلَاةِ", " — the maṣdar of أَذَّنَ: the call to prayer", " — «ezzene»nin masdarı: namaza çağrı")),
  PREPT("فِي", "fi", H("بِـ«سَمِعْتُ»", "«heard»", "«semi'tu»ya")), NOUN("أَهْلِي", "ahl", "majr", sign="ya", enc="ي", note=(" — يَعْنِي: فِي بَيْتِهِ، لِأَنَّهُ يَكُونُ فِي الْمَسْجِدِ قَبْلَ الْأَذَانِ", " — i.e. at home: he was in the mosque before the call", " — yani evinde; çünkü ezandan önce mescidde olurdu")),
  *MUNDHU("ثَلَاثِينَ", "thalathun")]),
 SEN(3, "He said: Anas ibn ʿIyāḍ Abū Ḍamra al-Laythī told us, from ʿAbd al-Raḥmān ibn Ḥarmala, from Saʿīd ibn al-Musayyib, who said:",
     "Dedi ki: Bize Enes b. İyâz Ebû Damre el-Leysî, Abdurrahman b. Harmele'den, o Saîd b. el-Müseyyeb'den haber verdi; o dedi ki:",
 [QALA_HID(IBN_SAD), ISNAD_AKHBARANA(), NAME("أَنَسُ", "anas", "fail", note=NT), BN("raf", ("أَنَسُ", "Anas", "Enes")), NAME("عِيَاضٍ", "iyad", "mi"),
  NOUN("أَبُو", "ab", "badal", "raf", sign="5", mudaf=True, of=("أَنَسُ", "Anas", "Enes"), note=(" — وَهِيَ كُنْيَتُهُ", " — his kunya", " — künyesi")),
  NAME("ضَمْرَةَ", "damra", "mi", dipt="tanith"), NOUN("اللَّيْثِيُّ", "laythi", "naat", "raf", of=("أَنَسُ", "Anas", "Enes"), note=(" — نِسْبَةٌ إِلَى بَنِي لَيْثٍ", " — a nisba to the Banū Layth", " — Benî Leys'e nisbet")),
  AN(hang=AKH), NOUN("عَبْدِ", "abd", "majr", by="عَنْ", mudaf=True), NAME("الرَّحْمٰنِ", "rahman", "mi"), BN("jarr", ("عَبْدِ الرَّحْمٰنِ", "ʿAbd al-Raḥmān", "Abdurrahman")),
  NAME("حَرْمَلَةَ", "harmala", "mi", dipt="tanith"),
  AN(hang=AKH), NAME("سَعِيدِ", "said-name", "majr", by="عَنْ", note=NT), BN("jarr", ("سَعِيدِ", "Saʿīd", "Saîd")), NAME("الْمُسَيّبِ", "musayyab", "mi", note=MUSAYYIB_NOTE),
  QALA_HID(SA)]),
 SEN(4, "For forty years I have not met the people coming away from a prayer.",
     "Kırk yıldır insanlarla bir namazdan dönerlerken karşılaşmadım.",
 [PART("مَا", "ma-nafiya", "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا عَمَلَ لَهُ.", "مَا negates; it governs nothing.", "«Mâ» nefy harfi, amel etmez.", ["anwa-ma"]),
  VERB("لَقِيتُ", "laqiya", "mtu", g=["naqis-verbs"]), NOUN("النَّاسَ", "nas", "maful"),
  NOUN("مُنْصَرِفِينَ", "munsarif", "hal", sign="smp", g=["ism-fail", "form-vii-verbs"], note=(" — اسْمُ فَاعِلٍ مِنَ «انْصَرَفَ»: أَيْ لَمْ يَأْتِ الْمَسْجِدَ بَعْدَ فَرَاغِهِمْ قَطُّ", " — an active participle of انْصَرَفَ: he never came to the mosque after they had finished", " — «insarafe»den ism-i fâil: yani onlar bitirdikten sonra mescide hiç gelmedi")),
  PREPT("مِنْ", "min", H("بِـ«مُنْصَرِفِينَ»", "«coming away»", "«munsarifîn»e")), NOUN("صَلَاةٍ", "salat", "majr"),
  *MUNDHU("أَرْبَعِينَ", "arbaun")]),
]
CHAPS = [S1]
NEW_GLOSS = {
 "tadhin": NN("تَأْذِين", "أ ذ ن", "calling to prayer (the maṣdar of أَذَّنَ)", "ezan okuma («ezzene»nin masdarı)"),
 "iyad": NP("عِيَاض", "ʿIyāḍ — a man's name (Anas ibn ʿIyāḍ's father)", "İyâz — erkek adı (Enes b. İyâz'ın babası)"),
 "damra": NP("ضَمْرَة", "Ḍamra — in the kunya «Abū Ḍamra»", "Damre — «Ebû Damre» künyesinde"),
 "laythi": NN("لَيْثِيّ", "ل ي ث", "of the Banū Layth (a nisba)", "Leysî (Benî Leys'e nisbet)"),
 "harmala": NP("حَرْمَلَة", "Ḥarmala — a man's name (ʿAbd al-Raḥmān ibn Ḥarmala's father)", "Harmele — erkek adı"),
 "hakim-name": NP("حَكِيم", "Ḥakīm — a man's name (ʿUthmān ibn Ḥakīm's father)", "Hakîm — erkek adı (Osman b. Hakîm'in babası)"),
}
GLOSS_HERE = {"munsarif": ("leaving, coming away (from a prayer)", "dönen, ayrılan (namazdan)"),
              "musayyab": ("al-Musayyab / al-Musayyib — Saʿīd's father; the vowel of the ya is disputed", "Müseyyeb / Müseyyib — Saîd'in babası; yânın harekesi ihtilaflı"),
              "anas": ("Anas — here Anas ibn ʿIyāḍ, Abū Ḍamra", "Enes — burada Enes b. İyâz, Ebû Damre")}
LEMMA_HERE = {"musayyab": "الْمُسَيّب"}
MANIFEST = manifest(SLUG, 3, {"ar": "مُنْذُ أَرْبَعِينَ سَنَةً", "en": "For Forty Years", "tr": "Kırk Yıldır"},
  {"ar": "سَعِيدُ بْنُ الْمُسَيّبِ وَصَلَاةُ الْجَمَاعَةِ", "en": "Saʿīd ibn al-Musayyib and the congregational prayer", "tr": "Saîd b. el-Müseyyeb ve cemaatle namaz"}, "tabiun",
  "Saʿīd ibn al-Musayyib's entry, vol. 5, printed p. 99 (Shamela p. 1527)", "Saîd b. el-Müseyyeb maddesi, cilt 5, matbû s. 99 (Şâmile s. 1527)", "تَرْجَمَةُ سَعِيدِ بْنِ الْمُسَيّبِ، الْجُزْءُ ٥، ص ٩٩ (الشَّامِلَةُ ص ١٥٢٧)",
  "the first two akhbār of the run on his prayer in congregation, each whole with its isnād («قال: أخبرنا موسى بن إسماعيل» … «منذ ثلاثين سنة.»; «قال: أخبرنا أنس بن عياض» … «منذ أربعين سنة.»)",
  "cemaatle namazına dair dizinin ilk iki haberi, her biri isnadıyla tam («قال: أخبرنا موسى بن إسماعيل» … «منذ ثلاثين سنة.»; «قال: أخبرنا أنس بن عياض» … «منذ أربعين سنة.»)",
  "أَوَّلُ خَبَرَيْنِ مِنَ الْأَخْبَارِ فِي صَلَاتِهِ فِي الْجَمَاعَةِ، بِإِسْنَادَيْهِمَا",
  left_en="the third khabar of the run (ʿUmrān's, «قال. ما فاتته صلاة الجماعة …»: its «قال» and «فاتته» do not agree in the e-text) and the rest of the entry",
  left_tr="dizinin üçüncü haberi (İmrân'ınki, «قال. ما فاتته صلاة الجماعة …»: e-metinde «قال» ile «فاتته» uyuşmuyor) ve maddenin geri kalanı",
  left_ar="الْخَبَرُ الثَّالِثُ (لِاضْطِرَابِ لَفْظِهِ فِي النَّصِّ الْإِلِكْتُرُونِيِّ) وَبَقِيَّةُ التَّرْجَمَةِ",
  hoca=[("the ya of «الْمُسَيّب» left unvowelled (al-Musayyab / al-Musayyib)", "«الْمُسَيّب»in yâsı harekesiz bırakıldı (Müseyyeb / Müseyyib)"),
        ("«مُنْذُ» parsed as a jarr letter (it may also be read as a noun, the mubtadaʾ)", "«münzü» cer harfi olarak i'râb edildi (isim/mübtedâ olarak da okunabilir)")])
if __name__ == "__main__":
    finish(SLUG, TITLES, CHAPS, NEW_GLOSS, MANIFEST, GLOSS_HERE, LEMMA_HERE)
