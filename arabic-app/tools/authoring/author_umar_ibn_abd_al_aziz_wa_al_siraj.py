"""Author content/samples/umar-ibn-abd-al-aziz-wa-al-siraj — «عُمَرُ بْنُ عَبْدِ الْعَزِيزِ وَالسِّرَاجُ», an ORIGINAL historical story at
Level 4 (Upper Intermediate).

ORIGINAL graded Arabic: ʿUmar ibn ʿAbd al-ʿAzīz, governor of Madīna in comfort and fine dress, becomes caliph and leaves that
life for plain clothes and the food of the poor, fearing to be asked about the poor on the Day of Resurrection; he returns
wealth that had been taken without right — to its owners when they are known, to the treasury when they are not — beginning
with himself and his own household, and does not turn back when some of his family are angry; at night he writes on the
Muslims' affairs by a lamp lit with the treasury's oil, and when a visitor asks after him and his family he puts that lamp
out and lights his own, because the oil is the Muslims' and his own affair is not theirs; in his short reign, it was said, a
man going out with his zakāt could hardly find anyone to take it. The reports are told in Ibn ʿAbd al-Ḥakam's Sīrat ʿUmar
ibn ʿAbd al-ʿAzīz and in Ibn al-Jawzī's Sīrat wa-manāqib ʿUmar ibn ʿAbd al-ʿAzīz; they are RETOLD FREELY here in a graded
reader's wording: no sentence is a quotation of either book, ʿUmar's answer to the visitor is reported as indirect speech
(فَأَخْبَرَهُ أَنَّ …), never as a recorded saying, and the zakāt report is given as «it was said» (قِيلَ), as the sources give it.
Four chapters, twenty-four sentences, in the Level-4 register: كَانَ and its sisters (كَانَ / صَارَ / لَيْسَ / مَا زَالَ, and كَادَ
of the verbs of nearness), إِنَّ and its sisters (إِنَّ / أَنَّ / لَكِنَّ), the ḥāl as a word and as a clause, the passive (أُخِذَتْ،
عُرِفَ، لَمْ يُعْرَفُوا، أَنْ يُسْأَلَ، يُوقَدُ، قِيلَ), and the conditionals إِذَا / إِنْ / لَوْ. Written on the authoring kit
(story_kit.py) after the model of author_umar_wa_al_qidr.py; one entry is new — the verb أَطْفَأَ «to put out» (Form IV,
hamzated lām) with a paradigm from sarf_gen, spelled as the shelf's أَخْطَأَ.  Regenerate with:
python3 tools/authoring/author_umar_ibn_abd_al_aziz_wa_al_siraj.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "umar-ibn-abd-al-aziz-wa-al-siraj"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

# ============ «عُمَرُ بْنُ عَبْدِ الْعَزِيزِ وَالسِّرَاجُ» — an ORIGINAL historical story at Level 4 ============
PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "هُمَا": "pron-3d", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "هُمَا": "هُمَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})

# --- the diptote name, as in «عُمَرُ وَالْقِدْرُ» -----------------------------------------------------------------------
UMAR_D = ("، وَهُوَ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ (مَعْدُولٌ عَنْ عَامِرٍ)",
          " — a proper name barred from tanwin: a name «turned» (maʿdūl) from ʿĀmir",
          " — alemiyet ve udûl (Âmir'den çevrilmiş) sebebiyle gayr-i munsarif özel isim")
DIPT_G = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
UMAR_F = lambda punct=None: FAIL("عُمَرُ", "umar", "propn", DIPT_G, *UMAR_D, punct=punct)
FULAA = ("، وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ (فُعَلَاءُ)",
         " — barred from tanwin by the extended alif of the feminine (the pattern فُعَلَاء)",
         " — memdûde te'nîs elifi (fu'alâ' vezni) sebebiyle gayr-i munsarif")
FULAA_J = ("، وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُعَرَّفٌ بِأَلْ",
           " — a diptote (the extended alif of the feminine), yet in jarr by the kasra because it carries the article",
           " — memdûde te'nîs elifi sebebiyle gayr-i munsarif; harf-i ta'rîf aldığı için kesre ile mecrûr")

def MADI_D(full, lex, extra=None, hidden=False, punct=None, note_ar="", note_en="", note_tr=""):
    """a past verb of a DERIVED form (أَرَادَ، أَطْفَأَ، أَوْقَدَ) — MADI without the mujarrad-bāb anchor"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", extra or [],
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + hid + note_ar + ".",
        en0 + "past verb built on fatha" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)

IBN_NAAT = lambda: tok("بْنُ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِعُمَرَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
    "An adjective (na't) of «ʿUmar», in raf' and annexed — its alif is dropped in writing because it stands between two names.", "«Ömer»in na'tı, merfû, muzâf — iki alem arasında geldiği için elifi yazıda düşer.")
ABD_MI = lambda: MUDAF_ILAYH("عَبْدِ", "abd", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَعَبْدُ الْعَزِيزِ عَلَمٌ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ، اسْمُ أَبِي عُمَرَ",
    note_en=", annexed — ʿAbd al-ʿAzīz, a name built as an idafa, is the name of ʿUmar's father", note_tr=", muzâf — Abdülazîz, izâfet terkibiyle kurulmuş bir alem, Ömer'in babasının adıdır")
AZIZ_MI = lambda punct=None: MUDAF_ILAYH("الْعَزِيزِ", "aziz", note_ar=" — وَالْعَزِيزُ اسْمٌ مِنْ أَسْمَاءِ اللهِ تَعَالَى", note_en=" — al-ʿAzīz «the Mighty» is one of the names of God", note_tr=" — el-Azîz, Allah'ın isimlerindendir", punct=punct)
MUSLIMIN_MI = lambda punct=None: tok("الْمُسْلِمِينَ", "muslim", "noun", ["idafa-definiteness", "jam-mudhakkar-salim", "ism-fail"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "The second term of the idafa, in jarr by the ya — a sound masculine plural.",
    "Muzâfun ileyh, cem-i müzekker sâlim olduğu için yâ ile mecrûr.", punct=punct)
INDA_KH = lambda: tok("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"],
    "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ كَانَ مُقَدَّمٌ.",
    "An adverb of place «with, in the keeping of», in nasb and annexed — it hangs on an omitted FRONTED predicate of كَانَ.",
    "Mekân zarfı «yanında», mansûb, muzâf — kâne'nin mahzûf ve öne alınmış haberine müteallık.")
IDHA_T = lambda: tok("إِذَا", "idha", "noun", ["idha-shartiyya", "maful-fih", "huruf-al-shart-fil-kafiya"],
    "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ غَيْرُ جَازِمٍ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ الشَّرْطِ.",
    "إِذَا «when(ever)»: an adverb of time carrying the sense of a condition, which governs no jazm; built on sukun in the seat of nasb, annexed to the condition's clause.",
    "İzâ «-dığı zaman»: şart mânâsı taşıyan, cezm etmeyen zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf.")
KANA_IDHA = ("، وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ بَعْدَهُ فِي مَحَلِّ نَصْبٍ خَبَرُهُ، وَكَانَ مَعَ إِذَا تُفِيدُ الْعَادَةَ فِي الْمَاضِي",
             "; the conditional sentence after it is its predicate, in the seat of nasb — كَانَ with إِذَا tells a habit in the past («whenever … he would …»)",
             "; sonraki şart cümlesi haberi, mahallen mansûb — kâne, izâ ile geçmişteki âdeti bildirir")
SHART_IDHA = (" — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا", " — the condition's verb; its clause is in the seat of jarr, annexed to إِذَا",
              " — şart fiili; cümlesi izâ'ya muzâfun ileyh olarak mahallen mecrûr")
JAWAB_IDHA = (" — جَوَابُ الشَّرْطِ، وَالْجُمْلَةُ لَا مَحَلَّ لَهَا لِأَنَّهَا جَوَابُ شَرْطٍ غَيْرِ جَازِمٍ", " — the answer of the condition; its clause has no seat, being the answer of a condition that governs no jazm",
              " — şartın cevabı; cezm etmeyen şartın cevabı olduğu için cümlenin i'râbdan mahalli yoktur")
JAWAB_IN = ("، وَهُوَ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ", "; it stands in the seat of jazm as the answer of the condition", "; şartın cevabı olarak mahallen meczûm")
ANNA_BI = lambda full="أَنَّ": tok(full, "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna", "hadhf-al-jarr"] + (["atf-nasaq"] if full.startswith("وَ") else []),
    (WA_AR if full.startswith("وَ") else "") + "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِمَّا بَعْدَهُ " +
    ("مَعْطُوفٌ عَلَى الْمَصْدَرِ قَبْلَهُ." if full.startswith("وَ") else "مَجْرُورٌ بِبَاءٍ مَحْذُوفَةٍ: أَخْبَرَهُ بِأَنَّ … — وَحَذْفُ الْجَارِّ قَبْلَ أَنَّ قِيَاسٌ."),
    ("The waw conjoins; " if full.startswith("وَ") else "") + "أَنَّ «that», the verb-like particle that builds a masdar — " +
    ("the clause it builds is conjoined to the one before." if full.startswith("وَ") else "the clause it builds is in jarr by a dropped ba («told him OF …»): before أَنَّ a jarr letter may regularly drop."),
    ("«ve» + " if full.startswith("وَ") else "") + "Enne — te'kîd, nasb ve masdar harfi; kurduğu müevvel masdar " +
    ("öncekine ma'tûftur." if full.startswith("وَ") else "hazfedilmiş bâ ile mecrûrdur («ona … diye haber verdi»): enne'den önce cer harfinin düşmesi kıyâsîdir."),
    segments=[seg("وَ", "wa", "conj"), seg("أَنَّ", "anna", "part")] if full.startswith("وَ") else None)

TITLES = [{"ar": "قَبْلَ الْخِلَافَةِ وَبَعْدَهَا", "en": "Before the caliphate and after", "tr": "Hilâfetten önce ve sonra"},
          {"ar": "الْأَمْوَالُ تُرَدُّ إِلَى أَهْلِهَا", "en": "The wealth goes back to its owners", "tr": "Mallar sahiplerine döner"},
          {"ar": "السِّرَاجُ", "en": "The lamp", "tr": "Kandil"},
          {"ar": "الزَّكَاةُ", "en": "The zakat", "tr": "Zekât"}]

# ---- Chapter 1 — قَبْلَ الْخِلَافَةِ وَبَعْدَهَا ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Before the caliphate, ʿUmar ibn ʿAbd al-ʿAzīz was governor over Madina, and he lived in great comfort.",
                                       "tr": "Ömer bin Abdülazîz hilâfetten önce Medine'nin emîriydi ve büyük bir bolluk içinde yaşardı."},
 "tokens": [KANA("كَانَ"), ISMK("عُمَرُ", "umar", "propn", DIPT_G, *UMAR_D), IBN_NAAT(), ABD_MI(), AZIZ_MI(),
  ZARF("قَبْلَ", "qabla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), MUDAF_ILAYH("الْخِلَافَةِ", "khilafa"),
  KHK("أَمِيرًا", "amir"), PREP("عَلَى", "ala", "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«أَمِيرًا»", "; the jarr phrase hangs on «governor»", "; câr-mecrûr «emîr»e müteallıktır", gloss_tr="«üzerine»"),
  MAJR("الْمَدِينَةِ", "madina", punct="،"),
  KANA_HID("وَكَانَ"), MUDARI_KH("يَعِيشُ", "asha-live", ["hollow-verbs"]), FI(), MAJR("نَعِيمٍ", "naim"), NAAT("كَثِيرٍ", "kathir", "jarr", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "He used to wear the finest clothes and to love perfume.", "tr": "En güzel elbiseleri giyer, güzel kokuyu severdi."},
 "tokens": [KANA_HID("وَكَانَ"), MUDARI_KH("يَلْبَسُ", "labisa"),
  MAFUL("أَحْسَنَ", "ahsan", extra=["idafa-definiteness", "ism-tafdil"], note_ar="، مُضَافٌ — وَهُوَ اسْمُ تَفْضِيلٍ", note_en=", annexed — an elative («the finest»)", note_tr=", muzâf — ism-i tafdîl («en güzel»)"),
  MUDAF_ILAYH("الثِّيَابِ", "thawb", extra=["jam-taksir"], note_ar=" — جَمْعُ ثَوْبٍ", note_en=" — the plural of ثَوْب «garment»", note_tr=" — sevb'in cem'i", punct="،"),
  MUDARI("وَيُحِبُّ", "ahabba", ["form-iv-verbs", "doubled-verbs", "kana-wa-akhawatuha"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ يَلْبَسُ فَهِيَ مِثْلُهَا فِي مَحَلِّ نَصْبٍ",
      note_en=" — its clause is conjoined to «he would wear», so it too fills the seat of nasb", note_tr=" — cümlesi «giyerdi»ye ma'tûf, o da mahallen mansûb"),
  MAFUL("الطِّيبَ", "tib", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "Then he became caliph of the Muslims, and he left all of that comfort.", "tr": "Sonra müslümanların halîfesi oldu ve o bolluğun hepsini bıraktı."},
 "tokens": [THUMMA(),
  tok("صَارَ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "صَارَ «became», a sister of كَانَ, built on fatha; its noun is the hidden pronoun «he».", "«oldu» — kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; ismi gizli zamir «o»."),
  tok("خَلِيفَةً", "khalifa", "noun", ["kana-wa-akhawatuha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of صَارَ, in nasb.", "Sâra'nın haberi, mansûb."),
  tok("لِلْمُسْلِمِينَ", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim"], "اللَّامُ حَرْفُ جَرٍّ، وَالْمُسْلِمِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«خَلِيفَةً».",
      "The lam is a jarr letter; «the Muslims» is in jarr by the ya, a sound masculine plural — the phrase hangs on «caliph».", "Lâm cer harfi; «müslümanlar» cem-i müzekker sâlim olduğu için yâ ile mecrûr — câr-mecrûr «halîfe»ye müteallık.",
      punct="،", segments=[seg("لِ", "li", "prep"), seg("الْمُسْلِمِينَ", "muslim", "noun")]),
  MADI("فَتَرَكَ", "taraka", hidden=True),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "maful-bihi"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "A demonstrative built on fatha, in the seat of nasb as the direct object.", "İşaret ismi, fetha üzere mebnî, mef'ûlün bih olarak mahallen mansûb."),
  BADAL("النَّعِيمَ", "naim", "nasb"),
  tok("كُلَّهُ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A tawkid of meaning «all of it», in nasb like the noun it strengthens; annexed to «it», which fills the seat of jarr.",
      "Ma'nevî te'kîd «hepsini», pekiştirdiği isim gibi mansûb; «o» zamirine muzâf, zamir mahallen mecrûr.",
      punct=".", segments=[seg("كُلَّ", "kull", "noun"), seg("هُ", "pron-3ms", "pron")])]})
S1.append({"id": "s4", "translation": {"en": "He wore clothes that caliphs do not wear, and he ate the food of the poor.", "tr": "Halîfelerin giymediği elbiseler giydi ve fakirlerin yemeğini yedi."},
 "tokens": [MADI("فَلَبِسَ", "labisa", hidden=True), MAFUL("ثِيَابًا", "thawb", extra=["jam-taksir"]), LA_NAFIYA(),
  tok("يَلْبَسُهَا", "labisa", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِثِيَابٍ، وَالْهَاءُ هِيَ الرَّابِطُ.",
      "Present verb in raf'; the attached «them» is its object, in the seat of nasb — the clause qualifies «clothes», in the seat of nasb as its na't, and the pronoun ties it back.",
      "Merfû muzâri; bitişik «onları» mef'ûlün bih, mahallen mansûb — cümle «elbiseler»in na'tı, mahallen mansûb; zamir râbıttır.",
      segments=[seg("يَلْبَسُ", "labisa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  FAIL("الْخُلَفَاءُ", "khalifa", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ خَلِيفَةٍ" + FULAA[0], note_en=" — the plural of خَلِيفَة" + FULAA[1], note_tr=" — halîfe'nin cem'i" + FULAA[2], punct="،"),
  MADI("وَأَكَلَ", "akala", hidden=True), MAFUL("طَعَامَ", "taam", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("الْفُقَرَاءِ", "faqir", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ فَقِيرٍ" + FULAA_J[0], note_en=" — the plural of فَقِير" + FULAA_J[1], note_tr=" — fakîr'in cem'i" + FULAA_J[2], punct=".")]})
S1.append({"id": "s5", "translation": {"en": "Had he wanted comfort he would have found it; but he feared that he would be asked about the poor on the Day of Resurrection.",
                                       "tr": "Bolluğu isteseydi onu bulurdu; fakat kıyamet günü fakirlerden sorulmaktan korkuyordu."},
 "tokens": [tok("وَلَوْ", "law", "part", ["huruf-al-shart-fil-kafiya", "al-qasam-wal-shart-fil-kafiya"],
      "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ يَدُلُّ عَلَى امْتِنَاعِ الْجَوَابِ لِامْتِنَاعِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ.",
      "The waw opens a new sentence; the conditional لَوْ «if (it were so)» governs no jazm and marks the answer as not happening because the condition did not happen.",
      "Vâv isti'nâf içindir; lev: cezm etmeyen şart harfi — şart gerçekleşmediği için cevabın da gerçekleşmediğini bildirir.",
      segments=[seg("وَ", "wa", "conj"), seg("لَوْ", "law", "part")]),
  MADI_D("أَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"], hidden=True, note_ar=" — فِعْلُ الشَّرْطِ، وَجُمْلَتُهُ لَا مَحَلَّ لَهَا", note_en=" — the condition's verb; its clause has no seat", note_tr=" — şart fiili; cümlesinin i'râbdan mahalli yoktur"),
  MAFUL("النَّعِيمَ", "naim"),
  tok("لَوَجَدَهُ", "wajada", "verb", ["thulathi-mujarrad-babs", "mithal-verbs", "al-bariz-al-muttasil", "maful-bihi", "huruf-al-shart-fil-kafiya"],
      "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَوَجَدَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ جَوَابُ لَوْ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
      "The lam opens the answer of لَوْ; «found» is a past verb built on fatha, its doer the hidden «he», and the attached «it» its object in the seat of nasb — the clause is the answer of لَوْ and has no seat.",
      "Lâm lev'in cevabına girmiştir; vecede fetha üzere mebnî mâzî, fâili gizli «o», bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle lev'in cevabıdır, i'râbdan mahalli yoktur.",
      punct="،", segments=[seg("لَ", "lam-jawab", "part"), seg("وَجَدَ", "wajada", "verb"), seg("هُ", "pron-3ms", "pron")]),
  INNA_ENC("وَلَكِنَّهُ", "هُ", " («o»)"),
  KANA_HID("كَانَ", note=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَكِنَّ", "; the clause fills the seat of raf' as the predicate of لَكِنَّ", "; cümle lâkinne'nin haberi, mahallen merfû")),
  MUDARI_KH("يَخَافُ", "khafa", ["hollow-verbs"]),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَخَافُ»", "; the clause it builds is the object of «feared», in the seat of nasb", "; kurduğu müevvel masdar «korkardı»nın mef'ûlü, mahallen mansûb"),
  tok("يُسْأَلَ", "saala", "verb", ["nawasib-wa-jawazim-al-mudari", "naib-al-fail", "al-majhul-fil-kafiya"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ.",
      "A present verb in the passive, put in nasb by أَنْ, its sign the fatha; the deputy doer is the hidden «he» — its first letter takes damma and the letter before the last a fatha.",
      "En ile mansûb meçhul muzâri, alâmeti fetha; nâib-i fâil gizli zamir «o» — evveli mazmûm, âhirinden önceki harf meftûh."),
  AN_KASRA(), MAJR("الْفُقَرَاءِ", "faqir", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=FULAA_J[0], note_en=FULAA_J[1], note_tr=FULAA_J[2]),
  ZARF("يَوْمَ", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), MUDAF_ILAYH("الْقِيَامَةِ", "qiyama", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "Whenever he remembered that at night, he would weep in fear.", "tr": "Geceleyin bunu hatırladığında korkuyla ağlardı."},
 "tokens": [KANA_HID("وَكَانَ", note=KANA_IDHA), IDHA_T(),
  MADI_D("تَذَكَّرَ", "tadhakkara", ["form-v-verbs", "idha-shartiyya"], hidden=True, note_ar=SHART_IDHA[0], note_en=SHART_IDHA[1], note_tr=SHART_IDHA[2]),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "maful-bihi"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "A demonstrative built on fatha, in the seat of nasb as the direct object.", "İşaret ismi, fetha üzere mebnî, mef'ûlün bih olarak mahallen mansûb."),
  FI(), MAJR("اللَّيْلِ", "layl"),
  MADI_ALIF("بَكَى", "baka", ["idha-shartiyya"], hidden=True, note_ar=JAWAB_IDHA[0], note_en=JAWAB_IDHA[1], note_tr=JAWAB_IDHA[2]),
  HAL("خَائِفًا", "khaif", ["ism-fail"], punct=".")]})

# ---- Chapter 2 — الْأَمْوَالُ تُرَدُّ إِلَى أَهْلِهَا ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "Some of the princes held wealth that had been taken from the people without right.", "tr": "Bazı emîrlerin elinde, insanlardan haksız yere alınmış mallar vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True), INDA_KH(),
  MUDAF_ILAYH("بَعْضِ", "baad", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("الْأُمَرَاءِ", "amir", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ أَمِيرٍ" + FULAA_J[0], note_en=" — the plural of أَمِير" + FULAA_J[1], note_tr=" — emîr'in cem'i" + FULAA_J[2]),
  ISMK("أَمْوَالٌ", "mal", extra=["jam-taksir"], muakhkhar=True, note_ar=" — وَجَاءَ نَكِرَةً لِتَقَدُّمِ خَبَرِهِ الظَّرْفِ، وَهُوَ جَمْعُ مَالٍ، وَأُنِّثَ لَهُ الْفِعْلُ لِأَنَّهُ جَمْعُ تَكْسِيرٍ",
      note_en=" — it may be indefinite because its adverbial predicate comes first; the plural of مَال, and as a broken plural it lets the verb take the feminine ta",
      note_tr=" — zarf olan haberi öne geçtiği için nekre gelebilmiştir; mâl'in cem'i — cem-i teksîr olduğundan fiil müennes gelebilir"),
  MAJHUL("أُخِذَتْ", "akhadha", ["thulathi-mujarrad-babs", "jumla-sifa"], fem=True, note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِأَمْوَالٍ",
      note_en="; the deputy doer is the hidden «they (f.)» — the clause qualifies «wealth», in the seat of raf' as its na't", note_tr="; nâib-i fâil gizli zamir «o (müennes)» — cümle «mallar»ın na'tı, mahallen merfû"),
  MINA(), MAJR("النَّاسِ", "nas"),
  BI_NOUN("بِغَيْرِ", "ghayr", "غَيْرِ", note_ar="، مُضَافٌ", note_en="; annexed", note_tr="; muzâf"), MUDAF_ILAYH("حَقٍّ", "haqq-sulh", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "So ʿUmar returned it, and he began with himself and his own household.", "tr": "Ömer o malları geri verdi; işe kendisinden ve ev halkından başladı."},
 "tokens": [ENC_MADI("فَرَدَّهَا", "radda", "هَا", extra=["doubled-verbs"]), UMAR_F(punct="،"),
  MADI("وَبَدَأَ", "badaa", hidden=True), BI_NOUN("بِنَفْسِهِ", "nafs", "نَفْسِهِ", enc="هِ"),
  ATF("وَأَهْلِ", "ahl", "noun", "jarr", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  ENC_NOUN("بَيْتِهِ", "bayt", "هِ", "mudaf", punct=".")]})
S2.append({"id": "s3", "translation": {"en": "If the owners of the wealth were known, he returned it to them; and if they were not known, he put it in the treasury.",
                                       "tr": "Malın sahipleri bilinirse onu onlara geri verir, bilinmezlerse beytülmâle koyardı."},
 "tokens": [tok("فَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], FA_AR + "إِنْ حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ.",
      "The fa conjoins; the conditional إِنْ «if», which governs two verbs in jazm.", "«bunun üzerine» + cezmeden şart harfi in: iki fiili cezmeder.",
      segments=[seg("فَ", "fa", "conj"), seg("إِنْ", "in-shartiyya", "part")]),
  MAJHUL("عُرِفَ", "arafa", ["thulathi-mujarrad-babs", "in-shartiyya", "al-majzum-wal-shart-wal-jaza"], note_ar=" — وَهُوَ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ",
      note_en=" — it stands in the seat of jazm as the condition's verb", note_tr=" — şart fiili olarak mahallen meczûm"),
  NAIB("أَهْلُ", "ahl", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الْمَالِ", "mal"),
  ENC_MADI("رَدَّهُ", "radda", "هُ", extra=["doubled-verbs", "al-majzum-wal-shart-wal-jaza"], hidden=True, note_ar=JAWAB_IN[0], note_en=JAWAB_IN[1], note_tr=JAWAB_IN[2]),
  ILAYHIM(punct="،"), IN_SHART("وَإِنْ"), LAM_JAZM(),
  tok("يُعْرَفُوا", "arafa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "afal-khamsa", "al-bariz-al-muttasil", "naib-al-fail", "al-majhul-fil-kafiya", "al-majzum-wal-shart-wal-jaza"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ.",
      "A present verb in the passive, in jazm by لَمْ, its sign the dropped nun (one of the five verbs); the waw is its deputy doer, in the seat of raf' — the clause stands in the seat of jazm as the condition's verb.",
      "Lem ile meczûm meçhul muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv nâib-i fâil, mahallen merfû — cümle şart fiili olarak mahallen meczûm.",
      segments=[seg("يُعْرَفُو", "arafa", "verb"), seg("ا", "pron-3mp", "pron")]),
  ENC_MADI("جَعَلَهُ", "jaala", "هُ", extra=["al-majzum-wal-shart-wal-jaza"], hidden=True, note_ar=JAWAB_IN[0], note_en=JAWAB_IN[1], note_tr=JAWAB_IN[2]),
  FI(), MAJR("بَيْتِ", "bayt", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  MUDAF_ILAYH("الْمَالِ", "mal", note_ar=" — وَبَيْتُ الْمَالِ: خِزَانَةُ الْمُسْلِمِينَ", note_en=" — bayt al-māl «the house of wealth» is the Muslims' treasury", note_tr=" — beytülmâl: müslümanların hazinesi", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "Some of his family were angry, but he did not turn back from his course.", "tr": "Ailesinden bazıları kızdı; fakat o işinden dönmedi."},
 "tokens": [MADI("فَغَضِبَ", "ghadiba"), FAIL("بَعْضُ", "baad", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  ENC_NOUN("أَهْلِهِ", "ahl", "هِ", "mudaf", punct="،"), INNA_ENC("وَلَكِنَّهُ", "هُ", " («o»)"), LAM_JAZM(),
  JAZM_V("يَرْجِعْ", "rajaa", ["lam-jazim"], hidden="هُوَ", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَكِنَّ", note_en="; the clause fills the seat of raf' as the predicate of لَكِنَّ", note_tr="; cümle lâkinne'nin haberi, mahallen merfû"),
  PREP("عَنْ", "an", gloss_tr="«-den»"), ENC_NOUN("أَمْرِهِ", "amr", "هِ", "majr", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "And he told them that that wealth was a right belonging to its owners.", "tr": "Onlara, o malların sahiplerinin hakkı olduğunu bildirdi."},
 "tokens": [ENC_MADI("وَأَخْبَرَهُمْ", "akhbara", "هُمْ", extra=["form-iv-verbs"], hidden=True), ANNA_BI(),
  tok("تِلْكَ", "tilka", "pron", ["asma-al-ishara", "inna-wa-akhawatuha"], "اسْمُ إِشَارَةٍ لِلْبَعِيدِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ اسْمُ أَنَّ.",
      "The far demonstrative «that», built on fatha, in the seat of nasb as the noun of أَنَّ.", "Uzak için işaret ismi «o», fetha üzere mebnî, enne'nin ismi olarak mahallen mansûb."),
  BADAL("الْأَمْوَالَ", "mal", "nasb", extra=["jam-taksir"]),
  KH_ANNA("حَقٌّ", "haqq-sulh"),
  LI_ENC("لِأَهْلِهَا", "ahl", "أَهْلِ", "هَا", punct=".", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِحَقٍّ", note_en="; the phrase hangs on an omitted na't of «a right»", note_tr="; câr-mecrûr «hak»kın mahzûf na'tına müteallık")]})
S2.append({"id": "s6", "translation": {"en": "The people rejoiced at his justice, and they loved him.", "tr": "İnsanlar onun adaletine sevindiler ve onu sevdiler."},
 "tokens": [MADI("فَفَرِحَ", "fariha"), FAIL("النَّاسُ", "nas"), BI_NOUN("بِعَدْلِهِ", "adl", "عَدْلِهِ", enc="هِ", punct="،"),
  VERB_WAW_ENC("وَأَحَبُّوهُ", "ahabba", "هُ", extra=["form-iv-verbs", "doubled-verbs"], punct=".")]})

# ---- Chapter 3 — السِّرَاجُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "ʿUmar had a lamp that was lit with oil from the treasury.", "tr": "Ömer'in yanında beytülmâlden gelen yağla yakılan bir kandil vardı."},
 "tokens": [KANA("وَكَانَ"), INDA_KH(),
  MUDAF_ILAYH("عُمَرَ", "umar", "propn", DIPT_G, sign=FATHA_JARR, note_ar=UMAR_D[0], note_en=" — in jarr by the fatha in place of the kasra" + UMAR_D[1], note_tr=" — kesre yerine fetha ile" + UMAR_D[2]),
  ISMK("سِرَاجٌ", "siraj", muakhkhar=True, note_ar=" — وَجَاءَ نَكِرَةً لِتَقَدُّمِ خَبَرِهِ الظَّرْفِ", note_en=" — it may be indefinite because its adverbial predicate comes first", note_tr=" — zarf olan haberi öne geçtiği için nekre gelebilmiştir"),
  tok("يُوقَدُ", "awqada", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "form-iv-verbs", "mithal-verbs", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِسِرَاجٍ؛ وَهُوَ مِنْ أَوْقَدَ، ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ.",
      "A present verb in the passive, in raf'; the deputy doer is the hidden «it» — the clause qualifies «a lamp», in the seat of raf' as its na't; from أَوْقَدَ «to light», its first letter takes damma and the letter before the last a fatha.",
      "Meçhul muzâri, merfû; nâib-i fâil gizli zamir «o» — cümle «kandil»in na'tı, mahallen merfû; evkade'den, evveli mazmûm, âhirinden önceki harf meftûh."),
  BI_NOUN("بِزَيْتٍ", "zayt", "زَيْتٍ"),
  MIN((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِزَيْتٍ", "; the phrase hangs on an omitted na't of «oil»", "; câr-mecrûr «yağ»ın mahzûf na'tına müteallık")),
  MAJR("بَيْتِ", "bayt", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الْمَالِ", "mal", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "By its light he wrote on the affairs of the Muslims.", "tr": "Onun ışığında müslümanların işlerine dair yazardı."},
 "tokens": [KANA_HID("وَكَانَ"), MUDARI_KH("يَكْتُبُ", "kataba"), ALA(), ENC_NOUN("نُورِهِ", "nur", "هِ", "majr"), FI(),
  MAJR("أُمُورِ", "amr", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ أَمْرٍ", note_en=", annexed — the plural of أَمْر «affair»", note_tr=", muzâf — emr'in cem'i"),
  MUSLIMIN_MI(punct=".")]})
S3.append({"id": "s3", "translation": {"en": "One night a man came in to him while he was writing, and the two talked about the people's affairs.", "tr": "Bir gece o yazarken yanına bir adam girdi; ikisi insanların işleri hakkında konuştular."},
 "tokens": [MADI("فَدَخَلَ", "dakhala"), ALAYHI(), FAIL("رَجُلٌ", "rajul"), ZARF("لَيْلَةً", "layla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False),
  WA_HUWA_HAL(), MUDARI("يَكْتُبُ", "kataba", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", note_en=" — the clause fills the seat of raf' as the khabar", note_tr=" — cümle haber olarak mahallen merfû", punct="،"),
  DUAL_MADI("فَتَكَلَّمَا", "takallama", ["form-v-verbs"]), FI(),
  MAJR("أُمُورِ", "amr", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("النَّاسِ", "nas", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "Then the man asked him about himself and his family; so ʿUmar put out the lamp and lit a lamp of his own.",
                                       "tr": "Sonra adam ona kendi hâlini ve ailesinin hâlini sordu; Ömer de kandili söndürdü ve kendine ait bir kandil yaktı."},
 "tokens": [THUMMA(), ENC_MADI("سَأَلَهُ", "saala", "هُ"), FAIL("الرَّجُلُ", "rajul"), PREP("عَنْ", "an", gloss_tr="«hakkında»"), ENC_NOUN("حَالِهِ", "hal-state", "هِ", "majr"),
  ATF("وَحَالِ", "hal-state", "noun", "jarr", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), ENC_NOUN("أَهْلِهِ", "ahl", "هِ", "mudaf", punct="،"),
  MADI_D("فَأَطْفَأَ", "atfaa", ["form-iv-verbs"], note_ar=" — وَهُوَ مَهْمُوزُ اللَّامِ: أَطْفَأَ يُطْفِئُ إِطْفَاءً", note_en=" — a verb whose last radical is a hamza: أَطْفَأَ يُطْفِئُ «to put out»", note_tr=" — lâmü'l-fiili hemzeli: etfee yutfi'u «söndürmek»"),
  UMAR_F(), MAFUL("السِّرَاجَ", "siraj", punct="،"),
  MADI_D("وَأَوْقَدَ", "awqada", ["form-iv-verbs", "mithal-verbs"], hidden=True), MAFUL("سِرَاجًا", "siraj"),
  LAHU2("لَهُ", "pron-3ms", " («onun»)", punct=".", note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِسِرَاجٍ", "; the phrase hangs on an omitted na't of «a lamp» («a lamp of his own»)", "; câr-mecrûr «kandil»in mahzûf na'tına müteallık"))]})
S3.append({"id": "s5", "translation": {"en": "The man asked him about that, and he told him that the oil of that lamp came from the wealth of the Muslims, and that his own affair was not one of their affairs.",
                                       "tr": "Adam ona bunu sordu; o da ona, o kandilin yağının müslümanların malından olduğunu ve kendi işinin onların işlerinden olmadığını bildirdi."},
 "tokens": [ENC_MADI("فَسَأَلَهُ", "saala", "هُ"), FAIL("الرَّجُلُ", "rajul"), PREP("عَنْ", "an", gloss_tr="«hakkında»"),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "huruf-jarr"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ.", "A demonstrative built on fatha, in the seat of jarr.", "İşaret ismi, fetha üzere mebnî, mahallen mecrûr.", punct="،"),
  ENC_MADI("فَأَخْبَرَهُ", "akhbara", "هُ", extra=["form-iv-verbs"], hidden=True), ANNA_BI(),
  tok("زَيْتَ", "zayt", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb and annexed.", "Enne'nin ismi, mansûb, muzâf."),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A demonstrative built on fatha, in the seat of jarr as the second term.", "İşaret ismi, fetha üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  BADAL("السِّرَاجِ", "siraj", "jarr"),
  MIN(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ أَنَّ", "; the jarr phrase hangs on the omitted predicate of أَنَّ", "; câr-mecrûr enne'nin mahzûf haberine müteallık")),
  MAJR("مَالِ", "mal", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUSLIMIN_MI(punct="،"),
  ANNA_BI("وَأَنَّ"),
  tok("أَمْرَ", "amr", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb and annexed.", "Enne'nin ismi, mansûb, muzâf."),
  ENC_NOUN("نَفْسِهِ", "nafs", "هِ", "mudaf"),
  tok("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins", "inna-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.",
      "لَيْسَ «is not», the frozen defective verb built on fatha: it raises its noun and puts its predicate in nasb; its noun is the hidden «it» — the clause fills the seat of raf' as the predicate of أَنَّ.",
      "Leyse: câmid nâkıs fiil, fetha üzere mebnî; ismini ref, haberini nasb eder; ismi gizli zamir «o» — cümle enne'nin haberi, mahallen merfû."),
  MIN(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ لَيْسَ", "; the jarr phrase hangs on the omitted predicate of لَيْسَ", "; câr-mecrûr leyse'nin mahzûf haberine müteallık")),
  ENC_NOUN("أُمُورِهِمْ", "amr", "هِمْ", "majr", extra=["jam-taksir"], punct=".")]})
S3.append({"id": "s6", "translation": {"en": "Whenever he had finished with the affairs of the Muslims, he would put out their lamp and light his own.", "tr": "Müslümanların işlerini bitirdiğinde onların kandilini söndürür, kendi kandilini yakardı."},
 "tokens": [KANA_HID("وَكَانَ", note=KANA_IDHA), IDHA_T(),
  MADI("فَرَغَ", "faragha", ["idha-shartiyya"], hidden=True, note_ar=SHART_IDHA[0], note_en=SHART_IDHA[1], note_tr=SHART_IDHA[2]),
  MIN(), MAJR("أُمُورِ", "amr", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUSLIMIN_MI(),
  MADI_D("أَطْفَأَ", "atfaa", ["form-iv-verbs", "idha-shartiyya"], hidden=True, note_ar=JAWAB_IDHA[0], note_en=JAWAB_IDHA[1], note_tr=JAWAB_IDHA[2]),
  ENC_NOUN("سِرَاجَهُمْ", "siraj", "هُمْ", "maful", punct="،"),
  MADI_D("وَأَوْقَدَ", "awqada", ["form-iv-verbs", "mithal-verbs"], hidden=True, note_ar=" — مَعْطُوفٌ عَلَى جَوَابِ الشَّرْطِ", note_en=" — conjoined to the answer of the condition", note_tr=" — şartın cevabına ma'tûf"),
  ENC_NOUN("سِرَاجَهُ", "siraj", "هُ", "maful", punct=".")]})

# ---- Chapter 4 — الزَّكَاةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "His caliphate was not long, but the people saw much justice in it.", "tr": "Hilâfeti uzun olmadı; fakat insanlar onda çok adalet gördüler."},
 "tokens": [WA_LAM(),
  tok("تَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "nawasib-wa-jawazim-al-mudari", "lam-jazim"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ — يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلْمُضَارَعَةِ وَالتَّأْنِيثِ.",
      "The defective present of كَانَ, in jazm by لَمْ, its sign the sukun; its middle waw drops where two quiescents meet — it raises its noun and puts its predicate in nasb (the ta marks the feminine).",
      "Lem ile meczûm nâkıs muzâri kâne, alâmeti sükûn; iki sâkin karşılaştığı için aynü'l-fiili (vâv) düşer — ismini ref, haberini nasb eder (tâ müennes içindir)."),
  ENC_NOUN("خِلَافَتُهُ", "khilafa", "هُ", "ismk"), KHK("طَوِيلَةً", "tawil-long", punct="،"),
  tok("وَلَكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"],
      WA_AR + "لَكِنَّ حَرْفُ اسْتِدْرَاكٍ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "The waw conjoins; لَكِنَّ «but», the verb-like particle of correction: its noun in nasb, its predicate in raf'.",
      "«ve» + lâkinne: istidrâk bildiren, fiile benzeyen harf; ismini nasb, haberini ref eder.",
      segments=[seg("وَ", "wa", "conj"), seg("لَكِنَّ", "lakinna", "part")]),
  tok("النَّاسَ", "nas", "noun", ["inna-wa-akhawatuha"], "اسْمُ لَكِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of لَكِنَّ, in nasb.", "Lâkinne'nin ismi, mansûb."),
  RAAW("رَأَوْا", note=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَكِنَّ", "; the clause fills the seat of raf' as the predicate of لَكِنَّ", "; cümle lâkinne'nin haberi, mahallen merfû")),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)"), MAFUL("عَدْلًا", "adl"), NAAT("كَثِيرًا", "kathir", "nasb", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He used to give the people their dues from the treasury.", "tr": "İnsanlara haklarını beytülmâlden verirdi."},
 "tokens": [KANA_HID("وَكَانَ"),
  MUDARI("يُعْطِي", "aata", ["form-iv-verbs", "kana-wa-akhawatuha", "mafulayn"], naqis="ي", note_ar=" — وَهُوَ يَنْصِبُ مَفْعُولَيْنِ" + KH_KANA_CL[0], note_en=" — it takes two objects" + KH_KANA_CL[1], note_tr=" — iki mef'ûl alır" + KH_KANA_CL[2]),
  MAFUL("النَّاسَ", "nas", extra=["mafulayn"], note_ar=" — الْمَفْعُولُ الْأَوَّلُ", note_en=" — the first object", note_tr=" — birinci mef'ûl"),
  ENC_NOUN("حُقُوقَهُمْ", "haqq-sulh", "هُمْ", "maful", extra=["jam-taksir", "mafulayn"], note_ar=" — الْمَفْعُولُ الثَّانِي، وَحُقُوقٌ جَمْعُ حَقٍّ", note_en=" — the second object; حُقُوق is the plural of حَقّ", note_tr=" — ikinci mef'ûl; hukûk, hakk'ın cem'i"),
  MIN(), MAJR("بَيْتِ", "bayt", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الْمَالِ", "mal", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "And it was said that a man would go out with the zakat of his wealth and could hardly find anyone who would accept it from him.",
                                       "tr": "Denildi ki, bir adam malının zekâtıyla çıkar, onu kendisinden kabul edecek kimseyi neredeyse bulamazdı."},
 "tokens": [tok("وَقِيلَ", "qala", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "hollow-verbs"],
      "الْوَاوُ لِلِاسْتِئْنَافِ، وَقِيلَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ، أَصْلُهُ قُوِلَ؛ وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَحْكِيَّةُ بَعْدَهُ.",
      "The waw opens a new sentence; «it was said» is the passive past of the hollow قَالَ, built on fatha (from قُوِلَ); its deputy doer is the sentence reported after it.",
      "Vâv isti'nâf içindir; kîle «denildi» — ecvef kâle'nin meçhul mâzîsi, fetha üzere mebnî (aslı kuvile); nâib-i fâili ondan sonra hikâye edilen cümledir.",
      punct=":", segments=[seg("وَ", "wa", "conj"), seg("قِيلَ", "qala", "verb")]),
  tok("إِنَّ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَكُسِرَتْ هَمْزَتُهُ لِوُقُوعِهِ بَعْدَ الْقَوْلِ.",
      "إِنَّ «indeed» puts its noun in nasb and raises its predicate — its hamza takes kasra because it follows a verb of saying.", "Te'kîd ve nasb harfi inne: ismini nasb, haberini ref eder — kavilden sonra geldiği için hemzesi meksûrdur."),
  ISM_INNA("الرَّجُلَ", "rajul"),
  KANA_HID("كَانَ", note=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi, mahallen merfû")),
  MUDARI_KH("يَخْرُجُ", "kharaja"), BI_NOUN("بِزَكَاةِ", "zakat", "زَكَاةِ", note_ar="، مُضَافٌ", note_en="; annexed", note_tr="; muzâf"),
  ENC_NOUN("مَالِهِ", "mal", "هِ", "mudaf", punct="،"),
  tok("فَلَا", "la-nafiya", "part", ["la-nafiya"], FA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; لَا negates and governs nothing.", "«bunun üzerine» + nefiy lâ'sı; amel etmez.",
      segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("يَكَادُ", "kada", "verb", ["afal-al-muqaraba", "kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ مَرْفُوعٌ بِالضَّمَّةِ، يَرْفَعُ الِاسْمَ وَخَبَرُهُ جُمْلَةٌ فِعْلِيَّةٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَجُمْلَتُهُ مَعْطُوفَةٌ عَلَى جُمْلَةِ يَخْرُجُ؛ وَ«لَا يَكَادُ يَجِدُ»: لَا يَقْرُبُ مِنْ أَنْ يَجِدَ.",
      "The present of كَادَ, a verb of nearness, in raf': it raises its noun, and its predicate is a verb clause; its noun is the hidden «he» — its clause is conjoined to «would go out»; «does not come near to finding» = «can hardly find».",
      "Mukârebe fiili kâde'nin muzârii, merfû: ismini ref eder, haberi fiil cümlesidir; ismi gizli zamir «o» — cümlesi «çıkardı»ya ma'tûf; «bulmaya yaklaşmaz» = «neredeyse bulamaz»."),
  MUDARI("يَجِدُ", "wajada", ["mithal-verbs", "afal-al-muqaraba"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكَادُ", note_en=" — the clause fills the seat of nasb as the predicate of يَكَادُ", note_tr=" — cümle yekâdu'nun haberi, mahallen mansûb"),
  MAFUL("أَحَدًا", "ahad"),
  MUDARI("يَقْبَلُهَا", "qabila", ["jumla-sifa"], enc="هَا", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِأَحَدٍ", note_en=" — the clause qualifies «anyone», in the seat of nasb as its na't", note_tr=" — cümle «kimse»nin na'tı, mahallen mansûb"),
  MINHU(punct=".")]})
S4.append({"id": "s4", "translation": {"en": "So he would go back home with it.", "tr": "Böylece onunla evine geri dönerdi."},
 "tokens": [KANA_HID("فَكَانَ"), MUDARI_KH("يَرْجِعُ", "rajaa"), JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onunla»)"), ILA(), ENC_NOUN("بَيْتِهِ", "bayt", "هِ", "majr", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "Then ʿUmar died, and the people grieved for him.", "tr": "Sonra Ömer vefat etti; insanlar da onun için üzüldüler."},
 "tokens": [THUMMA(), MADI("مَاتَ", "mata-die", ["hollow-verbs"]), UMAR_F(punct="،"), MADI("فَحَزِنَ", "hazina"), ALAYHI(), FAIL("النَّاسُ", "nas", punct=".")]})
S4.append({"id": "s6", "translation": {"en": "And the people still remember his justice and his lamp to this day.", "tr": "İnsanlar onun adaletini ve kandilini bugüne kadar hatırlamaya devam ediyorlar."},
 "tokens": [tok("وَمَا", "ma-nafiya", "part", ["la-nafiya", "kana-wa-akhawatuha"], WA_AR + "مَا حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ — وَنَفْيُ زَالَ إِثْبَاتٌ لِلِاسْتِمْرَارِ.",
      "The waw conjoins; مَا negates — and negating زَالَ «ceased» gives «kept on».", "«ve» + mâ nefiy harfi, sükûn üzere mebnî — zâle'nin nefyi devamı ispat eder.",
      segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَمَا زَالَ تُفِيدُ الِاسْتِمْرَارَ.",
      "A defective past verb, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb — مَا زَالَ «still, kept on» states continuance.",
      "Kâne'nin kardeşlerinden nâkıs mâzî fiil, fetha üzere mebnî; ismini ref, haberini nasb eder — mâ zâle devam bildirir."),
  tok("النَّاسُ", "nas", "noun", ["kana-wa-akhawatuha"], "اسْمُ مَا زَالَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of مَا زَالَ, in raf'.", "Mâ zâle'nin ismi, merfû."),
  MUDARI5("يَتَذَكَّرُونَ", "tadhakkara", ["form-v-verbs", "kana-wa-akhawatuha"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ مَا زَالَ", role_en="; the clause fills the seat of nasb as the predicate of مَا زَالَ", role_tr="; cümle mâ zâle'nin haberi, mahallen mansûb"),
  ENC_NOUN("عَدْلَهُ", "adl", "هُ", "maful"),
  ATF("وَسِرَاجَهُ", "siraj", "noun", "nasb", extra=["idafa-definiteness", "al-bariz-al-muttasil"], note_ar="، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ",
      note_en="; annexed, and the attached «his» is the second term, in the seat of jarr", note_tr="; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr",
      segments=[seg("وَ", "wa", "conj"), seg("سِرَاجَ", "siraj", "noun"), seg("هُ", "pron-3ms", "pron")]),
  ILA(), MAJR("الْيَوْمِ", "yawm", note_ar=" — أَيْ: إِلَى يَوْمِنَا هٰذَا", note_en=" — «to this day»", note_tr=" — «bugüne dek»", punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf; one entry is new ------------------------------------------
PREF = ["umar-wa-al-qidr", "qisas-al-nabiyyin-4", "al-kafiya", "adam-wa-iblis", "al-amana-wa-al-khashaba", "al-usul-al-munifa", "izhar-al-asrar", "al-asad-wa-al-arnab",
        "luqman-wa-ibnuh", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
def _pkg_dir(p): return ROOT / "content/samples" / p
# keys whose spelling the shelf shares between two lemmas: pin the package that holds the lemma meant here
FORCE = {"umar": "al-usul-al-munifa", "ibn-bn": "al-usul-al-munifa", "rajaa": "umar-wa-al-qidr", "an": "umar-wa-al-qidr", "inna": "umar-wa-al-qidr",
         "inda": "umar-wa-al-qidr", "la-nafiya": "umar-wa-al-qidr", "fa": "umar-wa-al-qidr", "nas": "umar-wa-al-qidr", "qiyama": "umar-wa-al-qidr",
         "dhalika": "talkhis-al-miftah", "rajul": "jumal-al-tadrib", "baad": "kitab-al-sulh", "haqq-sulh": "kitab-al-sulh", "siraj": "qisas-al-nabiyyin-2", "khaif": "musa-fi-madyan"}
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
 "atfaa": {"lemma": "أَطْفَأَ", "root": "ط ف أ", "pos": "verb", "gloss": {"en": "to put out, to extinguish (a lamp, a fire) — Form IV, its last radical a hamza", "tr": "söndürmek (kandil, ateş) — if'âl bâbı, lâmü'l-fiili hemzeli"}, "level": 4},
}
NEW_VERBS = {
 "atfaa": _sg.seat_hamza(_sg.derived(_sg.B4 + " — مَهْمُوزُ اللَّامِ", _sg.W4, "ُ", "أَطْفَأ", "طْفِئ", "أَطْفِئ", "إِطْفَاء", "مُطْفِئ", "مُطْفَأ", "أُطْفِئَ", "يُطْفَأُ",
                       "أَطْفَأَ السِّرَاجَ وَالنَّارَ يُطْفِئُهُمَا إِطْفَاءً: أَذْهَبَ ضَوْءَهُمَا — مَهْمُوزُ اللَّامِ، تُرْسَمُ هَمْزَتُهُ عَلَى مَا يُنَاسِبُ حَرَكَتَهَا (كَأَخْطَأَ).")),
}
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
    else: GLOSS[k] = e
assert not missing, missing
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = NEW_VERBS.get(k) or find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "عُمَرُ بْنُ عَبْدِ الْعَزِيزِ وَالسِّرَاجُ", "en": "ʿUmar ibn ʿAbd al-ʿAzīz and the Lamp", "tr": "Ömer b. Abdülaziz ve Kandil"},
 "subtitle": {"ar": "الْخَلِيفَةُ يُطْفِئُ سِرَاجَ بَيْتِ الْمَالِ إِذَا تَكَلَّمَ فِي أَمْرِ نَفْسِهِ، وَيَرُدُّ الْأَمْوَالَ إِلَى أَهْلِهَا — قِصَّةٌ لِلْمُسْتَوَى الرَّابِعِ",
              "en": "The caliph puts out the treasury's lamp when the talk turns to his own affairs, and returns wealth to its owners — a story for the fourth level",
              "tr": "Halife, söz kendi işine gelince beytülmâlin kandilini söndürür ve malları sahiplerine geri verir — dördüncü seviye için bir hikâye"},
 "level": 4,
 "levelName": "Upper Intermediate",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُتَدَرِّجَةٌ (الْمُسْتَوَى الرَّابِعُ) لِأَخْبَارٍ مِنْ سِيرَةِ عُمَرَ بْنِ عَبْدِ الْعَزِيزِ: تَرْكِهِ النَّعِيمَ بَعْدَ الْخِلَافَةِ، وَرَدِّهِ الْأَمْوَالَ الْمَأْخُوذَةَ بِغَيْرِ حَقٍّ، وَسِرَاجِ بَيْتِ الْمَالِ، وَمَا قِيلَ مِنْ قِلَّةِ مَنْ يَقْبَلُ الزَّكَاةَ فِي أَيَّامِهِ — وَهِيَ مَرْوِيَّةٌ فِي سِيرَةِ عُمَرَ بْنِ عَبْدِ الْعَزِيزِ لِابْنِ عَبْدِ الْحَكَمِ، وَفِي سِيرَتِهِ وَمَنَاقِبِهِ لِابْنِ الْجَوْزِيِّ. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ أَحَدِ الْكِتَابَيْنِ، وَجَوَابُ عُمَرَ لِلرَّجُلِ مَحْكِيٌّ بِالْمَعْنَى لَا لَفْظٌ مَرْوِيٌّ، فَلَا يُنْسَبُ شَيْءٌ مِنْهُ إِلَى عُمَرَ وَلَا إِلَى غَيْرِهِ.",
  "en": "ORIGINAL Level-4 graded Arabic: reports from the life of the caliph ʿUmar ibn ʿAbd al-ʿAzīz — his leaving a life of comfort once he became caliph, his returning wealth taken without right, the lamp lit with the treasury's oil, and what was said of how few would accept zakāt in his days — as told in Ibn ʿAbd al-Ḥakam's Sīrat ʿUmar ibn ʿAbd al-ʿAzīz and in Ibn al-Jawzī's Sīrat wa-manāqib ʿUmar ibn ʿAbd al-ʿAzīz, RETOLD FREELY in the wording of a graded reader. No sentence is a quotation from either book; ʿUmar's answer to the visitor is retold as indirect speech and is not a recorded saying, so none of it may be cited as the words of ʿUmar or of anyone else. The zakāt report is given, as the sources give it, as «it was said».",
  "tr": "ÖZGÜN 4. seviye kademeli Arapça: Halife Ömer b. Abdülaziz'in hayatından haberler — halife olunca bolluğu terk etmesi, haksız yere alınmış malları geri vermesi, beytülmâlin yağıyla yanan kandil ve onun günlerinde zekâtı kabul edecek kimsenin pek bulunmadığına dair söylenenler — İbn Abdülhakem'in Sîretü Ömer b. Abdilazîz'inde ve İbnü'l-Cevzî'nin Sîretü ve menâkıbu Ömer b. Abdilazîz'inde anlatıldığı şekliyle, kademeli okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bu iki kitaptan alıntı değildir; Ömer'in ziyaretçiye cevabı dolaylı anlatımla aktarılmıştır, rivayet edilmiş söz değildir; hiçbiri Ömer'in veya bir başkasının sözü olarak nakledilemez. Zekât haberi, kaynaklarda olduğu gibi «denildi ki» diye verilmiştir.",
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
