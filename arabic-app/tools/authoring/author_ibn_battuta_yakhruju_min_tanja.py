"""Author content/samples/ibn-battuta-yakhruju-min-tanja — «ابْنُ بَطُّوطَةَ يَخْرُجُ مِنْ طَنْجَةَ», an ORIGINAL historical story at Level 4.

ORIGINAL graded Arabic: in the year 725 AH Ibn Baṭṭūṭa, twenty-two years old, leaves Tangier alone for the pilgrimage, with
no companion and no caravan, and he and his living parents grieve at the parting. He travels east, keeps company with a
party of merchants, falls ill with fever, refuses to stay behind, and ties himself to the saddle with his turban from
weakness. In a great city where no one greets him he weeps from loneliness until a pilgrim greets him; the pilgrims'
caravan makes him its judge. He reaches Alexandria, where a righteous shaykh asks him to greet his brothers in faraway
lands, and then Cairo. After the pilgrimage he does not go home but travels for nearly thirty years, meets the shaykh's
brothers, returns to the Maghrib, and on the sultan's order dictates what he saw to Ibn Juzayy, who writes it down as the
book known as the Riḥla of Ibn Baṭṭūṭa. Every event is one his own Riḥla (Tuḥfat al-nuẓẓār fī gharāʾib al-amṣār) tells; it
is RETOLD FREELY: no sentence quotes the book, and no words are put in anyone's mouth. Place names are spelled only where
the brief and the shelf confirm them (طَنْجَة، الْإِسْكَنْدَرِيَّة، الْقَاهِرَة، مَكَّة); every other place is rephrased.
Five chapters, twenty-four sentences, in the Level-4 register (كَانَ / لَيْسَ, إِنَّ's sisters أَنَّ / لٰكِنَّ, the ḥāl as a word
and as a clause, the passive وُلِدَ / يُعْرَفُ, the conditional إِنْ with past verbs, one exception with إِلَّا, the compound
numbers of a date and an age). Written on the authoring kit (story_kit.py). Regenerate with:
python3 tools/authoring/author_ibn_battuta_yakhruju_min_tanja.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "ibn-battuta-yakhruju-min-tanja"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "كَ": "pron-2ms", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"هُمَا": "هُمَا", "هِمَا": "هُمَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})

# ---- the names ---------------------------------------------------------------------------------------------------------
DIPT_G = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
BAT_D = ("، وَهُوَ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ",
         " — a proper name barred from tanwin: a name that ends in the feminine ta",
         " — alemiyet ve lafzî te'nîs sebebiyle gayr-i munsarif özel isim")
TANJA_D = ("، وَهِيَ اسْمُ مَدِينَةٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ",
           " — a city's name, barred from tanwin: a proper name and feminine",
           " — şehir adı; alemiyet ve te'nîs sebebiyle gayr-i munsarif")
MAKKA_D = TANJA_D
BATTUTA_MI = lambda punct=None: MUDAF_ILAYH("بَطُّوطَةَ", "battuta", "propn", DIPT_G, sign=FATHA_JARR, note_ar=BAT_D[0], note_en=BAT_D[1], note_tr=BAT_D[2], punct=punct)
IBN_F = lambda: FAIL("ابْنُ", "ibn", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf")
TANJA_J = lambda punct=None: MAJR("طَنْجَةَ", "tanja", "propn", DIPT_G, sign=FATHA_JARR, note_ar=TANJA_D[0], note_en=TANJA_D[1], note_tr=TANJA_D[2], punct=punct)
JUZAYY_MI = lambda punct=None: MUDAF_ILAYH("جُزَيٍّ", "juzayy", "propn", note_ar=" — عَلَمٌ مُنْصَرِفٌ عَلَى وَزْنِ التَّصْغِيرِ", note_en=" — a proper name on the diminutive pattern, which keeps its tanwin", note_tr=" — tasgîr veznindeki munsarif özel isim", punct=punct)
HUMMA_F = lambda punct=None: FAIL("الْحُمَّى", "humma-fever", "noun", ["ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ",
    note_ar=" — اسْمٌ مَقْصُورٌ أَلِفُهُ لِلتَّأْنِيثِ، فَأُنِّثَ لَهُ الْفِعْلُ", note_en=" (the damma is estimated on the alif) — a maqṣūr noun whose alif is feminine, so its verb takes the feminine ta",
    note_tr=" (damme elif üzerinde takdîrî) — elifi te'nîs için olan maksûr isim; bu yüzden fiil müennes geldi", punct=punct)

def MADI_D(full, lex, extra=None, hidden=False, punct=None, note_ar="", note_en="", note_tr=""):
    """a past verb of a DERIVED form (سَلَّمَ، أَقْبَلَ، تَعَجَّبَ) — MADI without the mujarrad-bāb anchor"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", extra or [],
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + hid + note_ar + ".",
        en0 + "past verb built on fatha" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)

def KANA_PLAIN(note=("", "", "")):
    """كَانَ with its noun hidden («he» / «it»), no clitic"""
    return tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + note[0] + ".",
        "كَانَ is the defective past verb; its noun is the hidden pronoun «he / it»" + note[1] + ".",
        "nâkıs mâzî fiil kâne; ismi gizli zamir «o»" + note[2] + ".")

YAKUN = lambda note=("", "", ""): tok("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "lam-jazim", "hollow-verbs"],
    "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ: يَكُونْ)، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + note[0] + ".",
    "Present defective verb in jazm by لَمْ, its sign the sukun; its waw drops because two quiescents meet (from يَكُونْ); it raises its noun and puts its predicate in nasb" + note[1] + ".",
    "Lem ile meczûm nâkıs muzâri, alâmeti sükûn; iki sâkin karşılaştığı için vâv düştü (aslı yekûn); ismini ref, haberini nasb eder" + note[2] + ".")

LIANNAHU_HE = lambda: tok("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "huruf-jarr", "lam-taleel"],
    "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنَّ وَمَا بَعْدَهَا مَجْرُورٌ بِاللَّامِ.",
    "The lam is a jarr letter giving the reason; أَنَّ is the verb-like particle and the attached «he» is its noun, in the seat of nasb — the clause it builds stands in jarr after the lam.",
    "Lâm ta'lîl bildiren cer harfi; enne te'kîd ve nasb harfi, bitişik «o» ismi, mahallen mansûb — enne ile sonrasından oluşan müevvel masdar lâm ile mecrûr.",
    segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")])

def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ.",
        "The demonstrative «that», built on fatha, in the seat of " + seat_en + "; the lam marks distance and the kaf address.",
        "İşaret ismi «o», fetha üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık, kâf hitap içindir.", punct=punct)

PREP_NAAT = lambda full, lex, of_ar, of_en, of_tr, tr: PREP(full, lex, "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ " + of_ar,
    "; the jarr phrase hangs on an omitted na't of «" + of_en + "»", "; câr-mecrûr «" + of_tr + "»nın mahzûf na'tına müteallık", gloss_tr=tr)
MINA_BAYAN = lambda of_ar, of_en, of_tr: tok("مِنَ", "min", "prep", ["huruf-jarr"],
    "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ " + of_ar + ".",
    "A jarr letter naming the kind, voweled with fatha before the following ال — the jarr phrase hangs on an omitted na't of «" + of_en + "».",
    "«-den» — cins beyânı için cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi — câr-mecrûr «" + of_tr + "»nın mahzûf na'tına müteallık.")

TITLES = [{"ar": "مِنْ طَنْجَةَ", "en": "From Tangier", "tr": "Tanca'dan"},
          {"ar": "الْحُمَّى فِي الطَّرِيقِ", "en": "Fever on the road", "tr": "Yolda humma"},
          {"ar": "الْغَرِيبُ", "en": "The stranger", "tr": "Garip"},
          {"ar": "الْإِسْكَنْدَرِيَّةُ وَالْقَاهِرَةُ", "en": "Alexandria and Cairo", "tr": "İskenderiye ve Kahire"},
          {"ar": "ثَلَاثُونَ سَنَةً", "en": "Thirty years", "tr": "Otuz yıl"}]

# ---- Chapter 1 — مِنْ طَنْجَةَ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Ibn Baṭṭūṭa was one of the people of Tangier, and it was there that he was born.",
                                       "tr": "İbn Battûta Tanca halkındandı; orada doğmuştu."},
 "tokens": [KANA("كَانَ"),
  ISMK("ابْنُ", "ibn", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  BATTUTA_MI(),
  PREP("مِنْ", "min", " لِلتَّبْعِيضِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ", " of partition («one of»); the jarr phrase hangs on the omitted predicate of كَانَ", " — teb'îz için; câr-mecrûr kâne'nin mahzûf haberine müteallık", gloss_tr="«-den»"),
  MAJR("أَهْلِ", "ahl", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("طَنْجَةَ", "tanja", "propn", DIPT_G, sign=FATHA_JARR, note_ar=TANJA_D[0], note_en=TANJA_D[1], note_tr=TANJA_D[2], punct="،"),
  tok("وَفِيهَا", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
      WA_AR + "فِي حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِوُلِدَ، قُدِّمَ عَلَيْهِ لِلِاهْتِمَامِ.",
      "The waw conjoins; فِي is a jarr letter and the attached «it» (the city) fills the seat of jarr — the jarr phrase hangs on «was born», put before it for emphasis.",
      "«ve» + fî cer harfi; bitişik «orası» zamiri mahallen mecrûr — câr-mecrûr «doğdu»ya müteallıktır, önem için öne alınmıştır.",
      segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), seg("هَا", "pron-3fs", "pron")]),
  MAJHUL("وُلِدَ", "walada", ["thulathi-mujarrad-babs", "mithal-verbs"], punct=".",
      note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", note_en="; its deputy doer is the hidden «he»", note_tr="; nâib-i fâil gizli zamir «o»")]})
S1.append({"id": "s2", "translation": {"en": "In the year 725 he resolved to make the pilgrimage to the House of God.",
                                       "tr": "Yedi yüz yirmi beş yılında Allah'ın Evi'ni haccetmeye karar verdi."},
 "tokens": [PREP("وَفِي", "fi", "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِعَزَمَ", "; the jarr phrase hangs on «resolved»", "; câr-mecrûr «karar verdi»ye müteallık", gloss_tr="«-de»"),
  MAJR("سَنَةِ", "sana", extra=["idafa-definiteness"], note_ar="، مُضَافٌ إِلَى الْعَدَدِ بَعْدَهُ", note_en=", annexed to the number after it", note_tr=", sonraki sayıya muzâf"),
  MUDAF_ILAYH("خَمْسٍ", "khams", extra=["asma-al-adad-fil-kafiya"], note_ar=" — وَجَاءَ بِغَيْرِ تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ",
      note_en=" — written without ta because the thing counted, «year», is feminine", note_tr=" — ma'dûd «sene» müennes olduğu için tâsız"),
  ATF("وَعِشْرِينَ", "ishrun", "noun", "jarr", ["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
      note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  tok("وَسَبْعِمِائَةٍ", "sabumia", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«سَبْعِ» مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ«مِائَةٍ» مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَحُذِفَتِ التَّاءُ مِنْ سَبْعٍ لِأَنَّ الْمِائَةَ مُؤَنَّثَةٌ، وَيُكْتَبُ الْجُزْآنِ كَلِمَةً وَاحِدَةً.",
      "The waw conjoins; «seven» is conjoined, in jarr and annexed, and «hundred» is its second term, in jarr — seven has no ta because «hundred» is feminine, and the two parts are written as one word.",
      "Vâv atıf; «yedi» ma'tûf, mecrûr, muzâf; «yüz» muzâfun ileyh, mecrûr — «yüz» müennes olduğu için seb' tâsızdır; iki parça bitişik yazılır.",
      segments=[seg("وَ", "wa", "conj"), seg("سَبْعِمِائَةٍ", "sabumia", "noun")]),
  MADI("عَزَمَ", "azama", hidden=True), ALA(),
  MAJR("حَجِّ", "hajj", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("بَيْتِ", "bayt", note_ar="، مُضَافٌ", note_en=", itself annexed", note_tr=", kendisi de muzâf"), ALLAH_MI(punct=".")]})
S1.append({"id": "s3", "translation": {"en": "So he left Tangier alone, twenty-two years of age, with no companion and no caravan.",
                                       "tr": "Böylece yirmi iki yaşındayken Tanca'dan tek başına çıktı; yanında ne bir arkadaş vardı ne de bir kervan."},
 "tokens": [MADI("فَخَرَجَ", "kharaja", hidden=True), MIN(), TANJA_J(), WAHDAHU(), WA_HUWA_HAL(),
  KHABAR("ابْنُ", "ibn", ["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("اثْنَتَيْنِ", "ithnatan", extra=["asma-al-adad-fil-kafiya", "al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى",
      note_ar=" — وَأُنِّثَ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ، فَالْوَاحِدُ وَالِاثْنَانِ يُوَافِقَانِ الْمَعْدُودَ",
      note_en=" — in jarr by the ya, declined like a dual; it is feminine because «year» is, for one and two agree with what they count",
      note_tr=" — tesniyeye mülhak olduğu için yâ ile; ma'dûd «sene» müennes olduğu için müennes geldi — bir ve iki ma'dûda uyar"),
  ATF("وَعِشْرِينَ", "ishrun", "noun", "jarr", ["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
      note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  tok("سَنَةً", "sana", "noun", ["tamyiz", "asma-al-adad-fil-kafiya"],
      "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — وَمَعْدُودُ الْأَعْدَادِ الْمَعْطُوفَةِ مِنْ أَحَدٍ وَعِشْرِينَ إِلَى تِسْعَةٍ وَتِسْعِينَ مُفْرَدٌ مَنْصُوبٌ.",
      "A specifier (tamyiz), in nasb — after the conjoined numbers from 21 to 99 the thing counted is a singular in nasb.",
      "Temyîz, mansûb — 21'den 99'a kadar ma'tûf sayıların ma'dûdu tekil ve mansûbdur.", punct="،"),
  tok("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins", "al-hal-jumla-wa-rabituha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَجُمْلَتُهُ فِي مَحَلِّ نَصْبٍ حَالٌ أُخْرَى مِنْ فَاعِلِ خَرَجَ، وَالرَّابِطُ الضَّمِيرُ فِي «مَعَهُ».",
      "لَيْسَ «there is not» is the frozen defective verb, built on fatha: it raises its noun and puts its predicate in nasb — its clause is a further hal of the doer of «left», in the seat of nasb, tied to him by the pronoun in «with him».",
      "Leyse: câmid nâkıs fiil, fetha üzere mebnî; ismini ref, haberini nasb eder — cümlesi «çıktı»nın fâilinden ikinci bir hâl, mahallen mansûb; râbıt «yanında»daki zamirdir."),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "kana-wa-akhawatuha"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ لَيْسَ مُقَدَّمٌ.",
      "An adverb of place «with», in nasb and annexed to «him» — it hangs on the omitted FRONTED predicate of لَيْسَ.",
      "Mekân zarfı «yanında», mansûb, «o»na muzâf — leyse'nin öne alınmış mahzûf haberine müteallık.",
      segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("صَاحِبٌ", "sahib", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَجَاءَ نَكِرَةً لِتَقَدُّمِ خَبَرِهِ الظَّرْفِ.",
      "The noun of لَيْسَ, placed after its predicate, in raf' — it may be indefinite because its adverbial predicate comes first.",
      "Leyse'nin ismi (haberinden sonra), merfû — zarf olan haberi öne geçtiği için nekre gelebilmiştir."),
  tok("وَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], WA_AR + "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
      "The waw conjoins; لَا adds nothing but strength to the negation («nor»).", "«ve» + lâ, nefyi pekiştirmek için zâiddir.",
      segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("قَافِلَةٌ", "qafila", "noun", ["atf-nasaq", "kana-wa-akhawatuha"], "مَعْطُوفٌ عَلَى «صَاحِبٌ» مَرْفُوعٌ بِالضَّمَّةِ.",
      "Conjoined to «companion», in raf' like it.", "«Arkadaş»a ma'tûf, merfû.", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "His parents were still alive; he grieved at parting from them, and they grieved at parting from him.",
                                       "tr": "Anne babası hayattaydı; o onlardan ayrıldığı için üzüldü, onlar da ondan ayrıldıkları için üzüldüler."},
 "tokens": [KANA("وَكَانَ"),
  tok("أَبَوَاهُ", "abawan", "noun", ["kana-wa-akhawatuha", "al-muthanna", "idafa-definiteness", "al-bariz-al-muttasil"],
      "اسْمُ كَانَ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى (أَبَوَانِ: الْأَبُ وَالْأُمُّ تَغْلِيبًا)، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The noun of كَانَ, in raf' by the alif — a dual («the two fathers», i.e. father and mother, the father's name covering both); its nun drops before the annexed «his», which fills the seat of jarr.",
      "Kâne'nin ismi, tesniye olduğu için elif ile merfû (ebeveyn: tağlîb ile baba ve anne); izâfe sebebiyle nûnu düştü; bitişik zamir muzâfun ileyh, mahallen mecrûr.",
      segments=[seg("أَبَوَا", "abawan", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("حَيَّيْنِ", "hayy", "noun", ["kana-wa-akhawatuha", "al-muthanna"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى.",
      "The predicate of كَانَ, in nasb by the ya — a dual.", "Kâne'nin haberi, tesniye olduğu için yâ ile mansûb.", punct="،"),
  MADI("فَحَزِنَ", "hazina", hidden=True),
  LI_ENC("لِفِرَاقِهِمَا", "firaq", "فِرَاقِ", "هِمَا", ["lam-taleel", "masdar"], note_ar=" — وَاللَّامُ لِلتَّعْلِيلِ، وَالْمَصْدَرُ مُضَافٌ إِلَى مَفْعُولِهِ",
      note_en=" — the lam gives the cause, and the masdar is annexed to its object («his parting from them»)", note_tr=" — lâm ta'lîl içindir; masdar mef'ûlüne muzâftır («onlardan ayrılması»)", punct="،"),
  DUAL_MADI("وَحَزِنَا", "hazina", ["thulathi-mujarrad-babs"]),
  LI_ENC("لِفِرَاقِهِ", "firaq", "فِرَاقِ", "هِ", ["lam-taleel", "masdar"], note_ar=" — وَاللَّامُ لِلتَّعْلِيلِ", note_en=" — the lam gives the cause", note_tr=" — lâm ta'lîl içindir", punct=".")]})
S1.append({"id": "s5", "translation": {"en": "But the longing for Mecca was stronger in his heart than the grief.",
                                       "tr": "Fakat Mekke'ye duyduğu özlem, kalbinde hüzünden daha güçlüydü."},
 "tokens": [tok("وَلٰكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"],
      WA_AR + "لٰكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "The waw conjoins; لٰكِنَّ «but» is the corrective sister of إِنَّ: its noun in nasb, its predicate in raf'.",
      "«ve» + lâkinne: istidrâk bildiren, fiile benzeyen harf; ismini nasb, haberini ref eder.",
      segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part")]),
  tok("الشَّوْقَ", "shawq", "noun", ["inna-wa-akhawatuha"], "اسْمُ لٰكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of لٰكِنَّ, in nasb.", "Lâkinne'nin ismi, mansûb."),
  PREP("إِلَى", "ila", "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِالشَّوْقِ", "; the jarr phrase hangs on «longing»", "; câr-mecrûr «özlem»e müteallık", gloss_tr="«-e»"),
  MAJR("مَكَّةَ", "makka", "propn", DIPT_G, sign=FATHA_JARR, note_ar=MAKKA_D[0], note_en=MAKKA_D[1], note_tr=MAKKA_D[2]),
  KANA_PLAIN((" يَعُودُ عَلَى الشَّوْقِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ", ", returning to «the longing» — the clause fills the seat of raf' as the predicate of لٰكِنَّ", " («özlem»e döner) — cümle lâkinne'nin haberi, mahallen merfû")),
  tok("أَقْوَى", "aqwa", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "ism-maqsur-manqus"],
      "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمُ تَفْضِيلٍ عَلَى وَزْنِ أَفْعَلَ.",
      "The predicate of كَانَ, in nasb by a fatha estimated on the alif — an elative on the pattern أَفْعَل «stronger».",
      "Kâne'nin haberi, elif üzerinde takdîrî fetha ile mansûb — ef'al vezninde ism-i tafdîl «daha güçlü»."),
  FI(), ENC_NOUN("قَلْبِهِ", "qalb", "هِ", "majr"),
  tok("مِنَ", "min", "prep", ["huruf-jarr", "ism-tafdil"], "حَرْفُ جَرٍّ يَدْخُلُ عَلَى الْمُفَضَّلِ عَلَيْهِ بَعْدَ اسْمِ التَّفْضِيلِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter that brings in what is surpassed after the elative («stronger THAN»), voweled with fatha before the following ال.",
      "«-den» — ism-i tafdîlden sonra üstün gelinene giren cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("الْحُزْنِ", "huzn", punct=".")]})

# ---- Chapter 2 — الْحُمَّى فِي الطَّرِيقِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "Ibn Baṭṭūṭa travelled eastward, and on his way he kept company with a party of merchants.",
                                       "tr": "İbn Battûta doğuya doğru yol aldı; yolda bir grup tüccara arkadaşlık etti."},
 "tokens": [MADI("وَسَارَ", "sara-travel", ["hollow-verbs"]), IBN_F(), BATTUTA_MI(),
  ZARF("نَحْوَ", "nahw"), MUDAF_ILAYH("الْمَشْرِقِ", "mashriq", punct="،"),
  MADI("وَصَحِبَ", "sahiba", hidden=True), FI(), ENC_NOUN("طَرِيقِهِ", "tariq", "هِ", "majr"),
  MAFUL("قَوْمًا", "qawm"), MINA_BAYAN("لِقَوْمٍ", "a party", "grup"),
  MAJR("التُّجَّارِ", "tajir", extra=["jam-taksir"], note_ar=" — جَمْعُ تَاجِرٍ", note_en=" — the plural of تَاجِر «merchant»", note_tr=" — tâcir'in cem'i", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "Then fever struck him on the road, and his body grew weak.",
                                       "tr": "Sonra yolda onu humma tuttu ve vücudu zayıfladı."},
 "tokens": [THUMMA(),
  tok("أَصَابَتْهُ", "asaba", "verb", ["form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "maful-bihi"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.",
      "Past verb built on fatha; the ta marks the feminine, and the attached «him» is its object, in the seat of nasb, placed before the doer that follows.",
      "Fetha üzere mebnî mâzî; tâ te'nîs içindir; bitişik «onu» mef'ûlün bih, mahallen mansûb, sonra gelen fâilden önce gelmiştir.",
      segments=[seg("أَصَابَتْ", "asaba", "verb"), seg("هُ", "pron-3ms", "pron")]),
  HUMMA_F(), FI(), MAJR("الطَّرِيقِ", "tariq", punct="،"),
  MADI("فَضَعُفَ", "daufa"), ENC_NOUN("جِسْمُهُ", "jism", "هُ", "fail", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "Some of his companions asked him to stay for some days, but he refused.",
                                       "tr": "Arkadaşlarından bazıları ondan birkaç gün kalmasını istedi; fakat o kabul etmedi."},
 "tokens": [MADI("فَطَلَبَ", "talaba"), MINHU(),
  FAIL("بَعْضُ", "bad", extra=["idafa-definiteness"], note_ar=" مُؤَخَّرٌ عَنِ الْجَارِّ وَالْمَجْرُورِ، مُضَافٌ", note_en=", placed after the jarr phrase, and annexed", note_tr=", câr-mecrûrdan sonra gelmiş, muzâf"),
  ENC_NOUN("أَصْحَابِهِ", "sahib", "هِ", "mudaf", ["jam-taksir"], note_ar=" — وَأَصْحَابٌ جَمْعُ صَاحِبٍ", note_en=" — أَصْحَاب is the plural of صَاحِب", note_tr=" — ashâb, sâhib'in cem'i"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِطَلَبَ", "; the clause it builds is the object of «asked», in the seat of nasb", "; kurduğu müevvel masdar «istedi»nin mef'ûlü, mahallen mansûb"),
  MANSUB_AN("يُقِيمَ", "aqama", ["form-iv-verbs", "hollow-verbs"]),
  ZARF("أَيَّامًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False, extra=["jam-taksir"], note_ar=" — جَمْعُ يَوْمٍ", note_en=" — the plural of يَوْم «day»", note_tr=" — yevm'in cem'i", punct="،"),
  MADI_ALIF("فَأَبَى", "aba", hidden=True, punct=".")]})
S2.append({"id": "s4", "translation": {"en": "He judged that if he died on the road, he would die while on his way to the pilgrimage.",
                                       "tr": "Yolda ölürse, hacca giderken ölmüş olacağını düşündü."},
 "tokens": [MADI_ALIF("وَرَأَى", "raa", ["al-mutaaddi-wa-afal-al-qulub", "mafulayn"], hidden=True,
      note_ar=" — وَرَأَى هُنَا قَلْبِيَّةٌ بِمَعْنَى «اعْتَقَدَ»", note_en=" — رَأَى here is a verb of the heart, «judged, held»", note_tr=" — reâ burada kalbî fiildir, «kanaat getirdi»"),
  ANNAHU(note=(" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ رَأَى", "; the clause it builds stands in for both objects of «judged»", "; kurduğu müevvel masdar reâ'nın iki mef'ûlünün yerini tutar")),
  IN_SHART("إِنْ"),
  tok("مَاتَ", "mata-die", "verb", ["al-majzum-wal-shart-wal-jaza", "in-shartiyya", "hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "Past verb built on fatha, in the seat of jazm as the condition's verb; the doer «he» is hidden.",
      "Fetha üzere mebnî mâzî, şart fiili olarak mahallen meczûm; fâil gizli zamir «o»."),
  FI(), MAJR("الطَّرِيقِ", "tariq"),
  tok("مَاتَ", "mata-die", "verb", ["al-majzum-wal-shart-wal-jaza", "in-shartiyya", "hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.",
      "Past verb built on fatha, in the seat of jazm as the condition's answer; the doer «he» is hidden — the condition with its answer is the predicate of أَنَّ, in the seat of raf'.",
      "Fetha üzere mebnî mâzî, şartın cevabı olarak mahallen meczûm; fâil gizli zamir «o» — şart ve cevap cümlesi enne'nin haberi, mahallen merfû."),
  WA_HUWA_HAL(), KHABAR("ذَاهِبٌ", "dhahib", ["ism-fail"], note_ar=" — اسْمُ فَاعِلٍ مِنْ ذَهَبَ", note_en=" — the active participle of ذَهَبَ «going»", note_tr=" — zehebe'nin ism-i fâili"),
  ILA(), MAJR("الْحَجِّ", "hajj", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "The fever grew worse upon him, and he would tie himself to the saddle with his turban, so great was his weakness.",
                                       "tr": "Humma onu iyice sardı; zayıflığının şiddetinden kendini sarığıyla eyere bağlıyordu."},
 "tokens": [tok("وَاشْتَدَّتْ", "ishtadda", "verb", ["form-viii-verbs", "doubled-verbs"], WA_AR + "اشْتَدَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ.",
      "The waw conjoins; اشْتَدَّ «grew severe» is a past verb built on fatha; the ta marks the feminine.", "«ve» + iştedde: fetha üzere mebnî mâzî; tâ te'nîs içindir.",
      segments=[seg("وَ", "wa", "conj"), seg("اشْتَدَّتْ", "ishtadda", "verb")]),
  ALAYHI(), HUMMA_F(punct="،"),
  KANA_HID("فَكَانَ"), MUDARI_KH("يَرْبِطُ", "rabata"),
  ENC_NOUN("نَفْسَهُ", "nafs", "هُ", "maful"),
  BI_NOUN("بِعِمَامَتِهِ", "imama", "عِمَامَتِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ", note_en=" — the ba of the instrument («with»)", note_tr=" — bâ âlet bildirir"),
  ALA(), MAJR("السَّرْجِ", "sarj"),
  MIN((" لِلتَّعْلِيلِ", " giving the cause («from, because of»)", " — sebep bildirir")),
  MAJR("شِدَّةِ", "shidda", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("الضَّعْفِ", "daf", punct=".")]})

# ---- Chapter 3 — الْغَرِيبُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "Then he reached a great city, and its people came out greeting his companions.",
                                       "tr": "Sonra büyük bir şehre vardı; halkı onun arkadaşlarını selâmlayarak dışarı çıktı."},
 "tokens": [THUMMA(), MADI("وَصَلَ", "wasala", ["mithal-verbs"], hidden=True), ILA(), MAJR("مَدِينَةٍ", "madina"), NAAT("كَبِيرَةٍ", "kabir", "jarr", punct="،"),
  MADI("فَخَرَجَ", "kharaja"), ENC_NOUN("أَهْلُهَا", "ahl", "هَا", "fail"),
  MUDARI5("يُسَلِّمُونَ", "sallama", ["form-ii-verbs", "hal", "al-hal-jumla-wa-rabituha"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «أَهْلُهَا»",
      role_en="; the clause is a hal of «its people», in the seat of nasb", role_tr="; cümle «halkı»ndan hâl, mahallen mansûb"),
  ALA(), ENC_NOUN("أَصْحَابِهِ", "sahib", "هِ", "majr", ["jam-taksir"], punct=".")]})
S3.append({"id": "s2", "translation": {"en": "No one greeted him, for he knew none of them.",
                                       "tr": "Kimse ona selâm vermedi; çünkü onlardan hiçbirini tanımıyordu."},
 "tokens": [WA_LAM(), JAZM_V("يُسَلِّمْ", "sallama", ["form-ii-verbs", "lam-jazim"]), ALAYHI(), FAIL("أَحَدٌ", "ahad", punct="،"),
  LIANNAHU_HE(), LAM_JAZM(),
  YAKUN((" — وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; its noun is the hidden «he», and the clause fills the seat of raf' as the predicate of أَنَّ", "; ismi gizli zamir «o»; cümle enne'nin haberi, mahallen merfû")),
  MUDARI_KH("يَعْرِفُ", "arafa"), MINHUM(), MAFUL("أَحَدًا", "ahad", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "He grieved at this until he wept — a stranger, far from his family.",
                                       "tr": "Buna o kadar üzüldü ki ağladı; ailesinden uzak bir garipti."},
 "tokens": [MADI("فَحَزِنَ", "hazina", hidden=True),
  tok("لِذٰلِكَ", "dhalika", "pron", ["huruf-jarr", "asma-al-ishara", "lam-taleel"],
      "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ الثَّانِيَةُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ.",
      "The lam is a jarr letter giving the cause; ذٰلِكَ «that» is a demonstrative built on fatha, in the seat of jarr (its own lam marks distance and its kaf address).",
      "Lâm ta'lîl bildiren cer harfi; zâlike işaret ismi, fetha üzere mebnî, mahallen mecrûr (kendi lâmı uzaklık, kâfı hitap içindir).",
      segments=[seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  HATTA_IBT(), MADI_ALIF("بَكَى", "baka", hidden=True, punct="،"),
  WA_QAD(), KANA_PLAIN(),
  KHK("غَرِيبًا", "gharib"), NAAT("بَعِيدًا", "baid", "nasb"),
  PREP("عَنْ", "an", gloss_tr="«-den»"), ENC_NOUN("أَهْلِهِ", "ahl", "هِ", "majr", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "Then a man from among the pilgrims came up to him, greeted him, and spoke kind words to him.",
                                       "tr": "Derken hacılardan bir adam ona yöneldi, selâm verdi ve onunla güzel sözlerle konuştu."},
 "tokens": [MADI_D("فَأَقْبَلَ", "aqbala", ["form-iv-verbs"]), ALAYHI(), FAIL("رَجُلٌ", "rajul"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِرَجُلٍ.",
      "A jarr letter of partition («one of»), voweled with fatha before the following ال — the jarr phrase hangs on an omitted na't of «a man».",
      "«-den» — teb'îz için cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi — câr-mecrûr «adam»ın mahzûf na'tına müteallık."),
  MAJR("الْحُجَّاجِ", "hajj-pilgrim", extra=["jam-taksir"], note_ar=" — جَمْعُ حَاجٍّ", note_en=" — the plural of حَاجّ «pilgrim»", note_tr=" — hâcc'ın cem'i", punct="،"),
  MADI_D("فَسَلَّمَ", "sallama", ["form-ii-verbs"], hidden=True), ALAYHI(punct="،"),
  ENC_MADI("وَكَلَّمَهُ", "kallama", "هُ", ["form-ii-verbs"], hidden=True),
  BI_NOUN("بِكَلَامٍ", "kalam", "كَلَامٍ"), NAAT("طَيِّبٍ", "tayyib-good", "jarr", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "Then he set out with the pilgrims' caravan, and its people made him judge among them.",
                                       "tr": "Sonra hacılar kervanıyla yola çıktı; kervan halkı onu aralarında kadı yaptı."},
 "tokens": [THUMMA(), MADI("خَرَجَ", "kharaja", hidden=True), MAA(),
  MUDAF_ILAYH("قَافِلَةِ", "qafila", note_ar="، مُضَافٌ", note_en=", itself annexed", note_tr=", kendisi de muzâf"),
  MUDAF_ILAYH("الْحُجَّاجِ", "hajj-pilgrim", extra=["jam-taksir"], note_ar=" — جَمْعُ حَاجٍّ", note_en=" — the plural of حَاجّ «pilgrim»", note_tr=" — hâcc'ın cem'i", punct="،"),
  ENC_MADI("فَجَعَلَهُ", "jaala", "هُ", ["mafulayn"], note_ar=" أَوَّلُ — وَجَعَلَ هُنَا بِمَعْنَى صَيَّرَ، يَنْصِبُ مَفْعُولَيْنِ",
      note_en=" (the first of two) — جَعَلَ here means «made into» and takes two objects", note_tr=" (birinci mef'ûl) — ce'ale burada «yaptı, kıldı» anlamında iki mef'ûl alır"),
  ENC_NOUN("أَهْلُهَا", "ahl", "هَا", "fail"),
  tok("قَاضِيًا", "qadi", "noun", ["maful-bihi", "mafulayn", "ism-maqsur-manqus", "ism-fail"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ — اسْمٌ مَنْقُوصٌ تَظْهَرُ الْفَتْحَةُ عَلَى يَائِهِ لِخِفَّتِهَا.",
      "The second object, in nasb by a fatha that SHOWS on the ya — a manqūṣ noun, whose ya bears the light fatha openly.",
      "İkinci mef'ûl, yâ üzerinde zâhir fetha ile mansûb — mankûs isim; fetha hafif olduğu için yâ'sında görünür."),
  tok("بَيْنَهُمْ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "An adverb of place «among», in nasb and annexed to «them», which fills the seat of jarr.",
      "Mekân zarfı «aralarında», mansûb; «onlar» zamirine muzâf, zamir mahallen mecrûr.",
      punct=".", segments=[seg("بَيْنَ", "bayna", "noun"), seg("هُمْ", "pron-3mp", "pron")])]})

# ---- Chapter 4 — الْإِسْكَنْدَرِيَّةُ وَالْقَاهِرَةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "He travelled with the caravan until he reached Alexandria, a great city on the shore of the sea.",
                                       "tr": "Kervanla birlikte yol aldı ve sonunda deniz kıyısında büyük bir şehir olan İskenderiye'ye vardı."},
 "tokens": [MADI("وَسَارَ", "sara-travel", ["hollow-verbs"], hidden=True), MAA(), MUDAF_ILAYH("الْقَافِلَةِ", "qafila"),
  HATTA_IBT(), MADI("وَصَلَ", "wasala", ["mithal-verbs"], hidden=True), ILA(),
  MAJR("الْإِسْكَنْدَرِيَّةِ", "iskandariyya", "propn", note_ar=" — اسْمُ مَدِينَةٍ دَخَلَتْ عَلَيْهِ أَلْ فَجُرَّ بِالْكَسْرَةِ", note_en=" — a city's name that carries ال, so it takes the kasra", note_tr=" — el- takısı aldığı için kesre ile mecrûr olan şehir adı", punct="،"),
  tok("وَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"],
      "الْوَاوُ لِلِاسْتِئْنَافِ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "The waw opens a new clause; «it» (the city) is a detached pronoun built on fatha, in the seat of raf' as mubtada.",
      "Vâv isti'nâf içindir; «o» (şehir) munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû.",
      segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")]),
  KHABAR("مَدِينَةٌ", "madina"), NAAT("عَظِيمَةٌ", "azim", "raf"),
  PREP("عَلَى", "ala", "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ ثَانٍ لِمَدِينَةٍ", "; the jarr phrase hangs on an omitted second na't of «city»", "; câr-mecrûr «şehir»in mahzûf ikinci na'tına müteallık", gloss_tr="«üzerinde»"),
  MAJR("سَاحِلِ", "sahil", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الْبَحْرِ", "bahr", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "There he met a righteous shaykh, and the shaykh asked him to greet brothers of his in faraway lands.",
                                       "tr": "Orada sâlih bir şeyhle karşılaştı; şeyh ondan, uzak ülkelerdeki kardeşlerine selâm götürmesini istedi."},
 "tokens": [MADI("وَلَقِيَ", "laqiya", ["naqis-verbs"], hidden=True), JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («orada»)"),
  MAFUL("شَيْخًا", "shaykh"), NAAT("صَالِحًا", "salih", "nasb", punct="،"),
  MADI("فَطَلَبَ", "talaba"), MINHU(), FAIL("الشَّيْخُ", "shaykh"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِطَلَبَ", "; the clause it builds is the object of «asked», in the seat of nasb", "; kurduğu müevvel masdar «istedi»nin mef'ûlü, mahallen mansûb"),
  MANSUB_AN("يُسَلِّمَ", "sallama", ["form-ii-verbs"]), ALA(),
  MAJR("إِخْوَةٍ", "akh", extra=["jam-taksir"], note_ar=" — جَمْعُ أَخٍ", note_en=" — the plural of أَخ «brother»", note_tr=" — eh'in cem'i"),
  tok("لَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
      "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَفُتِحَتِ اللَّامُ مَعَ الضَّمِيرِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِإِخْوَةٍ.",
      "The lam is a jarr letter and the attached «him» fills the seat of jarr (the lam takes fatha before a pronoun) — the jarr phrase hangs on an omitted na't of «brothers» («brothers of his»).",
      "Lâm cer harfi; bitişik zamir mahallen mecrûr («onun») — lâm zamirle fethalı okunur; câr-mecrûr «kardeşler»in mahzûf na'tına müteallık.",
      segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]),
  PREP_NAAT("فِي", "fi", "نَعْتٌ ثَانٍ لِإِخْوَةٍ", "brothers (a second one)", "kardeşler (ikinci)", "«-de»"),
  MAJR("بِلَادٍ", "bilad"), NAAT("بَعِيدَةٍ", "baid", "jarr", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "Ibn Baṭṭūṭa was surprised at his words, for he had no wish to travel to those lands.",
                                       "tr": "İbn Battûta onun sözüne şaştı; çünkü o ülkelere gitmek gibi bir niyeti yoktu."},
 "tokens": [MADI_D("فَتَعَجَّبَ", "taajjaba", ["form-v-verbs"]), IBN_F(), BATTUTA_MI(), MIN(), ENC_NOUN("قَوْلِهِ", "qawl", "هِ", "majr", punct="،"),
  tok("وَمَا", "ma-nafiya", "part", ["la-nafiya", "al-hal-jumla-wa-rabituha"],
      "الْوَاوُ حَالِيَّةٌ، وَمَا حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا عَمَلَ لَهُ — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw opens a hal clause; مَا negates and governs nothing — the clause after it is a hal, in the seat of nasb.",
      "Hâl vâvı; mâ nefiy harfi, sükûn üzere mebnî, amel etmez — sonraki cümle hâl, mahallen mansûb.",
      segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  KANA_PLAIN(), MUDARI_KH("يُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"]),
  MAFUL("السَّفَرَ", "safar"), ILA(),
  tok("تِلْكَ", "tilka", "pron", ["asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمُؤَنَّثِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ.",
      "The feminine demonstrative «those», built on fatha, in the seat of jarr.", "Müennes işaret ismi «o», fetha üzere mebnî, mahallen mecrûr."),
  BADAL("الْبِلَادِ", "bilad", "jarr", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "Then he travelled to Cairo, and found it a great city, full of people.",
                                       "tr": "Sonra Kahire'ye gitti; onu kalabalık, büyük bir şehir buldu."},
 "tokens": [THUMMA(), MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True), ILA(),
  MAJR("الْقَاهِرَةِ", "qahira", "propn", note_ar=" — اسْمُ مَدِينَةٍ دَخَلَتْ عَلَيْهِ أَلْ فَجُرَّ بِالْكَسْرَةِ", note_en=" — a city's name that carries ال, so it takes the kasra", note_tr=" — el- takısı aldığı için kesre ile mecrûr olan şehir adı", punct="،"),
  ENC_MADI("فَوَجَدَهَا", "wajada", "هَا", ["mafulayn", "al-mutaaddi-wa-afal-al-qulub"], hidden=True, note_ar=" أَوَّلُ — وَوَجَدَ هُنَا مِنْ أَفْعَالِ الْقُلُوبِ يَنْصِبُ مَفْعُولَيْنِ",
      note_en=" (the first of two) — وَجَدَ here is a verb of the heart, «found (it to be)», taking two objects", note_tr=" (birinci mef'ûl) — vecede burada iki mef'ûl alan kalbî fiildir"),
  tok("مَدِينَةً", "madina", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb.", "İkinci mef'ûl, mansûb."),
  NAAT("عَظِيمَةً", "azim", "nasb"),
  NAAT("كَثِيرَةَ", "kathir", "nasb", ["idafa-lafziyya"], note_ar="، مُضَافٌ — وَإِضَافَتُهُ لَفْظِيَّةٌ لَا تُفِيدُ التَّعْرِيفَ، فَصَحَّ أَنْ يَكُونَ نَعْتًا لِلنَّكِرَةِ",
      note_en=", annexed — a «verbal» idafa that does not make it definite, so it may qualify an indefinite noun", note_tr=", muzâf — izâfesi lafzîdir, marifelik kazandırmaz; bu yüzden nekreye na't olabilir"),
  MUDAF_ILAYH("النَّاسِ", "nas", punct=".")]})

# ---- Chapter 5 — ثَلَاثُونَ سَنَةً ----
S5 = []
S5.append({"id": "s1", "translation": {"en": "Then he made the pilgrimage, and did not return to his country after it; rather he travelled about the earth for a long time.",
                                       "tr": "Sonra haccetti ve bundan sonra memleketine dönmedi; bilakis uzun bir süre yeryüzünü dolaştı."},
 "tokens": [THUMMA(), MADI("حَجَّ", "hajja", ["doubled-verbs"], hidden=True, punct="،"),
  WA_LAM(), JAZM_V("يَرْجِعْ", "rajaa", ["lam-jazim"], hidden="هُوَ"),
  ZARF("بَعْدَ", "bad-after", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr muzâfun ileyh", extra=["idafa-definiteness"]),
  ILA(), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr", punct="،"),
  tok("بَلْ", "bal", "conj", ["aw-imma-am-la-bal-lakin-fil-kafiya"], "حَرْفُ إِضْرَابٍ وَابْتِدَاءٍ مَبْنِيٌّ عَلَى السُّكُونِ — دَخَلَ عَلَى جُمْلَةٍ فَلَيْسَ عَاطِفًا، وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ.",
      "بَلْ «rather» turns away from what came before; before a whole clause it conjoins nothing, and the clause after it opens anew.",
      "Bel: idrâb ve ibtidâ harfi, sükûn üzere mebnî — cümlenin başına geldiği için atıf yapmaz; sonraki cümle müste'neftir."),
  MADI("طَافَ", "tafa", ["hollow-verbs"], hidden=True), FI(), MAJR("الْأَرْضِ", "ard"),
  ZARF("زَمَانًا", "zaman", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False), NAAT("طَوِيلًا", "tawil-long", "nasb", punct=".")]})
S5.append({"id": "s2", "translation": {"en": "On his journeys he met the brothers of that shaykh, and greeted them as the shaykh had asked him.",
                                       "tr": "Yolculuklarında o şeyhin kardeşleriyle karşılaştı ve şeyhin kendisinden istediği gibi onlara selâm verdi."},
 "tokens": [MADI("وَلَقِيَ", "laqiya", ["naqis-verbs"], hidden=True), FI(), ENC_NOUN("أَسْفَارِهِ", "safar", "هِ", "majr", ["jam-taksir"], note_ar=" — وَأَسْفَارٌ جَمْعُ سَفَرٍ", note_en=" — أَسْفَار is the plural of سَفَر «journey»", note_tr=" — esfâr, sefer'in cem'i"),
  MAFUL("إِخْوَةَ", "akh", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr muzâfun ileyh", extra=["idafa-definiteness"]),
  BADAL("الشَّيْخِ", "shaykh", "jarr", punct="،"),
  MADI_D("فَسَلَّمَ", "sallama", ["form-ii-verbs"], hidden=True), ALAYHIM(),
  KAMA(), MADI("طَلَبَ", "talaba", note_ar="، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الشَّيْخِ — وَالْجُمْلَةُ صِلَةُ مَا الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا",
      note_en="; its doer is the hidden «he», the shaykh — the clause is the ṣila of the masdar-making مَا and has no seat", note_tr="; fâil gizli zamir «o» (şeyh) — cümle masdariyye mâ'nın sılasıdır, mahalli yoktur"),
  MINHU(punct=".")]})
S5.append({"id": "s3", "translation": {"en": "His journeys lasted thirty years, all but a little.",
                                       "tr": "Yolculukları otuz yıldan biraz az sürdü."},
 "tokens": [tok("وَدَامَتْ", "dama", "verb", ["hollow-verbs", "al-fil-al-tamm-wal-naqis"],
      WA_AR + "دَامَ فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «بَقِيَ وَاسْتَمَرَّ» مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ لِأَنَّ فَاعِلَهُ جَمْعُ تَكْسِيرٍ.",
      "The waw conjoins; دَامَ here is COMPLETE, meaning «lasted»: a past verb built on fatha; the ta marks the feminine, since its doer is a broken plural.",
      "«ve» + dâme burada tâmdır, «sürdü» anlamında: fetha üzere mebnî mâzî; fâili cem-i teksîr olduğu için tâ te'nîs içindir.",
      segments=[seg("وَ", "wa", "conj"), seg("دَامَتْ", "dama", "verb")]),
  ENC_NOUN("أَسْفَارُهُ", "safar", "هُ", "fail", ["jam-taksir"]),
  tok("ثَلَاثِينَ", "thalathun", "noun", ["maful-fih", "asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"],
      "اسْمُ عَدَدٍ نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — وَنَابَ عَنِ الظَّرْفِ لِأَنَّ مَعْدُودَهُ زَمَانٌ.",
      "A number standing in for an adverb of time, in nasb by the ya — it declines like the sound masculine plural; it takes the adverb's place because what it counts is time.",
      "Zaman zarfının yerini tutan sayı ismi; cem-i müzekker sâlime mülhak olduğu için yâ ile mansûb — ma'dûdu zaman olduğu için zarfın yerini tutar."),
  tok("سَنَةً", "sana", "noun", ["tamyiz", "asma-al-adad-fil-kafiya"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "A specifier (tamyiz) of the number, in nasb.", "Sayının temyîzi, mansûb."),
  tok("إِلَّا", "illa", "part", ["istithna", "al-mustathna-wa-nawah-wa-nasbuh"], "أَدَاةُ اسْتِثْنَاءٍ مَبْنِيَّةٌ عَلَى السُّكُونِ.",
      "The particle of exception «but, less».", "İstisnâ edatı, sükûn üzere mebnî."),
  tok("قَلِيلًا", "qalil", "noun", ["istithna", "al-mustathna-wa-nawah-wa-nasbuh"],
      "مُسْتَثْنًى بِإِلَّا مَنْصُوبٌ بِالْفَتْحَةِ — وَالْكَلَامُ قَبْلَهَا تَامٌّ مُثْبَتٌ فَوَجَبَ نَصْبُهُ.",
      "The excepted, in nasb — the sentence before إِلَّا is complete and affirmative, so the excepted must be in nasb.",
      "Müstesnâ, mansûb — illâ'dan önceki söz tam ve müsbet olduğu için nasbı vâciptir.", punct=".")]})
S5.append({"id": "s4", "translation": {"en": "Then he returned to the Maghrib, and the sultan ordered him to dictate what he had seen on his journeys.",
                                       "tr": "Sonra Mağrib'e döndü; sultan ona yolculuklarında gördüklerini yazdırmasını emretti."},
 "tokens": [THUMMA(), MADI("رَجَعَ", "rajaa", hidden=True), ILA(), MAJR("الْمَغْرِبِ", "maghrib", punct="،"),
  ENC_MADI("فَأَمَرَهُ", "amara-command", "هُ"), FAIL("السُّلْطَانُ", "sultan"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِبَاءٍ مَحْذُوفَةٍ، أَيْ: بِأَنْ يُمْلِيَ", "; the clause it builds stands in jarr after an omitted ba («ordered him TO dictate»)", "; kurduğu müevvel masdar hazfedilmiş bâ ile mahallen mecrûr («yazdırmasını»)"),
  MANSUB_AN("يُمْلِيَ", "amla", ["form-iv-verbs", "naqis-verbs"], note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha shows on the ya, which bears it easily", note_tr=" — fetha hafif olduğu için yâ üzerinde zâhirdir"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "A relative pronoun «what», built on sukun, in the seat of nasb as the object.", "İsm-i mevsûl «-dığı şey», sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb."),
  MADI_ALIF("رَأَى", "raa", hidden=True, note_ar=SILA[0] + "، وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: رَآهُ", note_en=SILA[1] + "; the pronoun returning to مَا is left out («what he saw [it]»)", note_tr=SILA[2] + "; mâ'ya dönen zamir hazfedilmiştir"),
  FI(), ENC_NOUN("أَسْفَارِهِ", "safar", "هِ", "majr", ["jam-taksir"], punct=".")]})
S5.append({"id": "s5", "translation": {"en": "He dictated it to a scholar named Ibn Juzayy, and Ibn Juzayy wrote it down in a book known as the Riḥla of Ibn Baṭṭūṭa.",
                                       "tr": "Onu İbn Cüzey adlı bir âlime yazdırdı; İbn Cüzey de onu «İbn Battûta Seyahatnâmesi» diye bilinen bir kitaba yazdı."},
 "tokens": [ENC_MADI("فَأَمْلَاهُ", "amla", "هُ", ["form-iv-verbs"], alif=True, hidden=True, note_ar=" — وَكُتِبَتْ أَلِفُهُ قَائِمَةً لِاتِّصَالِهِ بِالضَّمِيرِ", note_en=" — its alif is written upright before the pronoun", note_tr=" — zamire bitiştiği için elifi dik yazıldı"),
  ALA(), MAJR("عَالِمٍ", "alim-scholar"),
  ENC_NOUN("اسْمُهُ", "ism-name", "هُ", "mubtada"),
  KHABAR("ابْنُ", "ibn", ["idafa-definiteness", "jumla-sifa"], note_ar="، مُضَافٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِعَالِمٍ",
      note_en=", annexed — the nominal clause «his name is …» qualifies «a scholar», in the seat of jarr", note_tr=", muzâf — isim cümlesi «âlim»in na'tı, mahallen mecrûr"),
  JUZAYY_MI(punct="،"),
  ENC_MADI("فَكَتَبَهُ", "kataba", "هُ"), IBN_F(), JUZAYY_MI(), FI(), MAJR("كِتَابٍ", "kitab"),
  tok("يُعْرَفُ", "arafa", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِكِتَابٍ.",
      "A present verb in the passive, in raf'; its deputy doer is the hidden «it» — the clause qualifies «a book», in the seat of jarr.",
      "Meçhul muzâri, merfû; nâib-i fâil gizli zamir «o» — cümle «kitap»ın na'tı, mahallen mecrûr."),
  BI_NOUN("بِرِحْلَةِ", "rihla", "رِحْلَةِ", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("ابْنِ", "ibn", note_ar="، مُضَافٌ", note_en=", itself annexed", note_tr=", kendisi de muzâf"), BATTUTA_MI(punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]

# ---- the lexicon: every key by lemma identity from the shelf; seven entries are new ----------------------------------
SCR_STORIES = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", "")) if os.environ.get("QISSA_PKG_ROOT") else None
PREF = ["umar-wa-al-qidr", "tariq-ibn-ziyad", "qisas-al-nabiyyin-4", "al-kafiya", "abu-hanifa-wa-al-safina", "al-usul-al-munifa", "musa-wa-firawn",
        "juha-wa-al-himar", "al-amana-wa-al-khashaba", "qisas-al-nabiyyin-1", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
def _pkg_dir(p): return ROOT / "content/samples" / p
FORCE = {"ibn": "al-bukhari-fi-baghdad", "abawan": "qisas-al-nabiyyin-4", "sahiba": "wasiyyat-abi-hanifa-l4", "hajj-pilgrim": "al-kafiya", "mata-die": "al-kafiya"}
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) if (_pkg_dir(p) / "morphology.json").exists() else {} for p in PREF}
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    if FORCE.get(k) and k in _M.get(FORCE[k], {}): return _M[FORCE[k]][k]
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

NEW_GLOSS = {
 "battuta": {"lemma": "بَطُّوطَة", "pos": "propn", "gloss": {"en": "Baṭṭūṭa — in ابْنُ بَطُّوطَةَ, the name by which the Moroccan traveller Abū ʿAbd Allāh Muḥammad al-Lawātī al-Ṭanjī (703–after 770 AH) is known; a diptote", "tr": "Battûta — ابْنُ بَطُّوطَةَ: Faslı seyyah Ebû Abdillâh Muhammed el-Levâtî et-Tancî'nin (h. 703–770'ten sonra) bilinen adı; gayr-i munsarif"}, "level": 4},
 "tanja": {"lemma": "طَنْجَة", "pos": "propn", "gloss": {"en": "Tangier — the port city at the Strait, Ibn Baṭṭūṭa's birthplace (a diptote: a feminine proper name)", "tr": "Tanca — Boğaz'daki liman şehri, İbn Battûta'nın doğduğu yer (gayr-i munsarif: müennes alem)"}, "level": 4},
 "iskandariyya": {"lemma": "الْإِسْكَنْدَرِيَّة", "pos": "propn", "gloss": {"en": "Alexandria — the Egyptian port city on the Mediterranean", "tr": "İskenderiye — Akdeniz kıyısındaki Mısır liman şehri"}, "level": 4},
 "qahira": {"lemma": "الْقَاهِرَة", "pos": "propn", "gloss": {"en": "Cairo — the capital of Egypt", "tr": "Kahire — Mısır'ın başşehri"}, "level": 4},
 "juzayy": {"lemma": "جُزَيّ", "pos": "propn", "gloss": {"en": "Juzayy — in ابْنُ جُزَيٍّ, Muḥammad ibn Juzayy al-Kalbī, the Andalusian scholar and secretary who wrote down Ibn Baṭṭūṭa's Riḥla", "tr": "Cüzey — ابْنُ جُزَيٍّ: İbn Battûta'nın Rihle'sini kaleme alan Endülüslü âlim ve kâtip Muhammed b. Cüzey el-Kelbî"}, "level": 4},
 "sabumia": {"lemma": "سَبْعُمِائَة", "root": "س ب ع", "pos": "noun", "gloss": {"en": "seven hundred", "tr": "yedi yüz"}, "level": 4},
 "humma-fever": {"lemma": "حُمَّى", "root": "ح م م", "pos": "noun", "gloss": {"en": "fever (a maqṣūr noun with the feminine alif)", "tr": "humma, ateşli hastalık (te'nîs elifli maksûr isim)"}, "level": 4},
}
# the shelf's own gloss of غَرِيب is «strange, rare»; here the same lemma names a stranger far from home
GLOSS_OVERRIDE = {"gharib": {"gloss": {"en": "strange; a stranger, one far from home", "tr": "garip; gurbetteki kimse, yabancı"}}}

used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k)
    if e is None: missing.append(k)
    else: GLOSS[k] = {**e, **GLOSS_OVERRIDE.get(k, {})}
assert not missing, missing
# a NEW key must not exist anywhere on the shelf (nor in a staged package) under another lemma
_staged = sorted(p for p in OUT_ROOT.iterdir() if (p / "glossary.json").exists() and p.name != SLUG) if OUT_ROOT != ROOT / "content/samples" else []
for k, e in NEW_GLOSS.items():
    for p in PREF:
        assert k not in _G[p] or _G[p][k]["lemma"] == e["lemma"], ("key taken on the shelf", k, p)
    for p in _staged:
        G2 = json.loads((p / "glossary.json").read_text(encoding="utf-8"))["entries"]
        assert k not in G2 or G2[k]["lemma"] == e["lemma"], ("key taken in a staged package", k, p.name)
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "ابْنُ بَطُّوطَةَ يَخْرُجُ مِنْ طَنْجَةَ", "en": "Ibn Baṭṭūṭa Leaves Tangier", "tr": "İbn Battûta Tanca'dan Çıkıyor"},
 "subtitle": {"ar": "شَابٌّ يَخْرُجُ وَحْدَهُ إِلَى الْحَجِّ، فَتَمْتَدُّ رِحْلَتُهُ ثَلَاثِينَ سَنَةً إِلَّا قَلِيلًا — قِصَّةٌ لِلْمُسْتَوَى الرَّابِعِ",
              "en": "A young man sets out alone for the pilgrimage, and his journey stretches to nearly thirty years — a story for the fourth level",
              "tr": "Hacca tek başına yola çıkan bir genç ve otuz yıla yakın süren yolculuğu — dördüncü seviye için bir hikâye"},
 "level": 4,
 "levelName": "Upper Intermediate",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُتَدَرِّجَةٌ (الْمُسْتَوَى الرَّابِعُ) لِخُرُوجِ ابْنِ بَطُّوطَةَ مِنْ طَنْجَةَ إِلَى الْحَجِّ وَمَا لَقِيَهُ فِي طَرِيقِهِ إِلَى الْإِسْكَنْدَرِيَّةِ وَالْقَاهِرَةِ، كَمَا يَحْكِيهِ هُوَ فِي رِحْلَتِهِ «تُحْفَةِ النُّظَّارِ فِي غَرَائِبِ الْأَمْصَارِ وَعَجَائِبِ الْأَسْفَارِ» الَّتِي أَمْلَاهَا عَلَى ابْنِ جُزَيٍّ الْكَلْبِيِّ. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنَ الرِّحْلَةِ، وَلَا يُنْسَبُ فِيهِ إِلَى أَحَدٍ كَلَامٌ بِلَفْظِهِ، وَأَسْمَاءُ الْبُلْدَانِ الَّتِي لَمْ يُتَحَقَّقْ ضَبْطُهَا تُرِكَتْ وَعُبِّرَ عَنْهَا بِغَيْرِهَا.",
  "en": "ORIGINAL Level-4 graded Arabic: Ibn Baṭṭūṭa's departure from Tangier for the pilgrimage in 725 AH and his road to Alexandria and Cairo, as he himself tells it in his Riḥla, Tuḥfat al-nuẓẓār fī gharāʾib al-amṣār wa-ʿajāʾib al-asfār, dictated to Ibn Juzayy al-Kalbī — RETOLD FREELY in the wording of a graded reader. No sentence is a quotation from the Riḥla and no words are put in anyone's mouth as a recorded saying; the cities between Tangier and Alexandria are left unnamed rather than spelled without a confirmed vocalisation.",
  "tr": "ÖZGÜN 4. seviye kademeli Arapça: İbn Battûta'nın h. 725'te hac için Tanca'dan çıkışı ve İskenderiye ile Kahire'ye uzanan yolu, kendisinin İbn Cüzey el-Kelbî'ye yazdırdığı Rihle'sinde (Tuhfetü'n-nuzzâr fî garâibi'l-emsâr ve acâibi'l-esfâr) anlattığı şekliyle, kademeli okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle Rihle'den alıntı değildir ve hiç kimseye rivayet edilmiş bir söz isnat edilmemiştir; Tanca ile İskenderiye arasındaki şehirlerin adları, harekesi kesinleştirilemediği için anılmamıştır.",
  "reviewStatus": "pending-scholarly-review",
 },
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
