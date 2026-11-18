"""Author content/samples/umar-wa-al-qidr — «عُمَرُ وَالْقِدْرُ», an ORIGINAL historical story at Level 4 (Upper Intermediate).

ORIGINAL graded Arabic: the caliph ʿUmar ibn al-Khaṭṭāb walks out of Madīna by night with his servant Aslam; they find a
woman whose children cry with hunger while a pot of plain water sits on the fire to quiet them until they sleep; not knowing
him, she complains that ʿUmar has neglected them. He goes back to the flour store (dār al-daqīq), carries flour and fat on
his own back — refusing to let Aslam carry it, since Aslam will not carry his burden on the Day of Resurrection — cooks for
the children himself and stays until they laugh. The report is told in al-Ṭabarī's Tārīkh and in Ibn al-Jawzī's Manāqib
ʿUmar; it is RETOLD FREELY here in a graded reader's wording: no sentence is a quotation of either book, and the dialogue is
a plain retelling, never a recorded saying. Four chapters, twenty-four sentences, in the Level-4 register (kāna and its
sisters كَانَ / لَيْسَ / مَا زَالَ, إِنَّ and its sisters إِنَّ / أَنَّ / لَعَلَّ / لَكِنَّ, the ḥāl as a word and as a clause, the passive,
and the conditionals إِذَا / إِنْ / لَوْ). Written on the authoring kit (story_kit.py); five entries are new — the names أَسْلَم
and الْخَطَّاب, the nouns دَقِيق «flour» and شَحْم, and the verb أَسْكَتَ (Form IV) with a generated paradigm.  Regenerate with:
python3 tools/authoring/author_umar_wa_al_qidr.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "umar-wa-al-qidr"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

# ============ «عُمَرُ وَالْقِدْرُ» — an ORIGINAL historical story at Level 4 ============
PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "هُمَا": "pron-3d", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "هُمَا": "هُمَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})

MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_F = lambda full="فَقَالَ", punct=None, hidden=False: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=hidden, punct=punct, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
KH_ANNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")

# --- the two diptote names --------------------------------------------------------------------------------------------
UMAR_D = ("، وَهُوَ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ (مَعْدُولٌ عَنْ عَامِرٍ)",
          " — a proper name barred from tanwin: a name «turned» (maʿdūl) from ʿĀmir",
          " — alemiyet ve udûl (Âmir'den çevrilmiş) sebebiyle gayr-i munsarif özel isim")
ASLAM_D = ("، وَهُوَ عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ (أَفْعَل)",
           " — a proper name barred from tanwin: a name on a verb's pattern (أَفْعَل)",
           " — alemiyet ve fiil vezni (ef'al) sebebiyle gayr-i munsarif özel isim")
DIPT_G = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
UMAR_F = lambda punct=None: FAIL("عُمَرُ", "umar", "propn", DIPT_G, *UMAR_D, punct=punct)
ASLAM_F = lambda punct=None: FAIL("أَسْلَمُ", "aslam", "propn", DIPT_G, *ASLAM_D, punct=punct)

def MADI_D(full, lex, extra=None, hidden=False, punct=None, note_ar="", note_en="", note_tr=""):
    """a past verb of a DERIVED form (سَلَّمَ، أَخْرَجَ، أَرَادَ، أَطْعَمَ) — MADI without the mujarrad-bāb anchor"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", extra or [],
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + hid + note_ar + ".",
        en0 + "past verb built on fatha" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)

MUMININ_MI = lambda punct=None: tok("الْمُؤْمِنِينَ", "mumin", "noun", ["idafa-definiteness", "jam-mudhakkar-salim", "ism-fail"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.", "The second term of the idafa, in jarr by the ya — a sound masculine plural.",
    "Muzâfun ileyh, cem-i müzekker sâlim olduğu için yâ ile mecrûr.", punct=punct)
MAAHU_HAL = lambda: tok("وَمَعَهُ", "maa", "noun", ["al-hal-jumla-wa-rabituha", "maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar"],
    "الْوَاوُ حَالِيَّةٌ، وَمَعَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ مُتَعَلِّقٌ بِخَبَرٍ مُقَدَّمٍ مَحْذُوفٍ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The waw opens a hal clause; «with him» is an adverb of place in nasb, annexed to the pronoun — it hangs on an omitted FRONTED predicate, and the nominal clause is a hal in the seat of nasb.",
    "Hâl vâvı; «yanında» mansûb mekân zarfı, zamire muzâf — mahzûf ve öne alınmış habere müteallık; isim cümlesi hâl olarak mahallen mansûb.",
    segments=[seg("وَ", "wa", "conj"), seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")])
def INDI(role_ar, role_en, role_tr):
    """عِنْدِي — the ẓarf annexed to the speaker's yāʾ, hanging on a fronted predicate"""
    return tok("عِنْدِي", "inda", "noun", ["maful-fih", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil", "kana-wa-akhawatuha"],
        "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ " + role_ar + ".",
        "An adverb of place «with (me)», in nasb by a fatha estimated before the speaker's ya; annexed, the ya its second term — the adverb hangs on an omitted " + role_en + ".",
        "Mekân zarfı «yanımda», mütekellim yâ'sından önce takdîrî fetha ile mansûb; muzâf, yâ muzâfun ileyh — zarf mahzûf " + role_tr + " müteallıktır.",
        segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")])
ANNI_AN = lambda: tok("عَنِّي", "an", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"],
    "عَنْ حَرْفُ جَرٍّ، وَالنُّونُ لِلْوِقَايَةِ أُدْغِمَتْ فِيهَا نُونُ عَنْ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.",
    "عَنْ «for, in place of» is a jarr letter; the nun of guarding takes the nun of عَنْ into its doubling, and the speaker's ya fills the seat of jarr — «for me».",
    "An cer harfi; an'ın nûnu vikâye nûnuna idgâm edilmiş, mütekellim yâ'sı mahallen mecrûr — «benim yerime».")
TITLES = [{"ar": "اللَّيْلُ", "en": "The night", "tr": "Gece"},
          {"ar": "الْقِدْرُ", "en": "The pot", "tr": "Tencere"},
          {"ar": "دَارُ الدَّقِيقِ", "en": "The flour store", "tr": "Un ambarı"},
          {"ar": "الصِّبْيَانُ يَضْحَكُونَ", "en": "The children laugh", "tr": "Çocuklar güler"}]

# ---- Chapter 1 — اللَّيْلُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "ʿUmar ibn al-Khaṭṭāb was the Commander of the Faithful, and whenever the people slept he would go out to look into their affairs.",
                                       "tr": "Ömer bin Hattâb mü'minlerin emîriydi; insanlar uyuyunca çıkar, onların hâllerini yoklardı."},
 "tokens": [KANA("كَانَ"), ISMK("عُمَرُ", "umar", "propn", DIPT_G, *UMAR_D),
  tok("بْنُ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِعُمَرَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
      "An adjective (na't) of «ʿUmar», in raf' and annexed — its alif is dropped in writing because it stands between two names.", "«Ömer»in na'tı, merfû, muzâf — iki alem arasında geldiği için elifi yazıda düşer."),
  MUDAF_ILAYH("الْخَطَّابِ", "khattab", "propn", note_ar=" — عَلَمٌ عَلَى أَبِي عُمَرَ", note_en=" — the name of ʿUmar's father", note_tr=" — Ömer'in babasının adı"),
  KHK("أَمِيرَ", "amir", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUMININ_MI(punct="،"),
  KANA_HID("وَكَانَ", note=(" — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ بَعْدَهُ فِي مَحَلِّ نَصْبٍ خَبَرُهُ، وَكَانَ مَعَ إِذَا تُفِيدُ الْعَادَةَ فِي الْمَاضِي", "; the conditional sentence after it is its predicate, in the seat of nasb — كَانَ with إِذَا tells a habit in the past («whenever … he would …»)", "; sonraki şart cümlesi haberi, mahallen mansûb — kâne, izâ ile geçmişteki âdeti bildirir")),
  tok("إِذَا", "idha", "noun", ["idha-shartiyya", "maful-fih", "huruf-al-shart-fil-kafiya"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ غَيْرُ جَازِمٍ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ الشَّرْطِ.",
      "إِذَا «when(ever)»: an adverb of time carrying the sense of a condition, which governs no jazm; built on sukun in the seat of nasb, annexed to the condition's clause.",
      "İzâ «-dığı zaman»: şart mânâsı taşıyan, cezm etmeyen zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf."),
  MADI("نَامَ", "nama", ["hollow-verbs", "idha-shartiyya"], note_ar=" — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا", note_en=" — the condition's verb; its clause is in the seat of jarr, annexed to إِذَا", note_tr=" — şart fiili; cümlesi izâ'ya muzâfun ileyh olarak mahallen mecrûr"),
  FAIL("النَّاسُ", "nas"),
  MADI("خَرَجَ", "kharaja", ["idha-shartiyya"], hidden=True, note_ar=" — جَوَابُ الشَّرْطِ، وَالْجُمْلَةُ لَا مَحَلَّ لَهَا لِأَنَّهَا جَوَابُ شَرْطٍ غَيْرِ جَازِمٍ", note_en=" — the answer of the condition; its clause has no seat, being the answer of a condition that governs no jazm", note_tr=" — şartın cevabı; cezm etmeyen şartın cevabı olduğu için cümlenin i'râbdan mahalli yoktur"),
  MUDARI("يَتَفَقَّدُ", "tafaqqada", ["form-v-verbs", "hal", "al-hal-jumla-wa-rabituha"], note_ar=HAL_CL[0], note_en=HAL_CL[1], note_tr=HAL_CL[2]),
  ENC_NOUN("أَحْوَالَهُمْ", "hal-state", "هُمْ", "maful", ["jam-taksir"], punct=".", note_ar=" — وَأَحْوَالٌ جَمْعُ حَالٍ", note_en=" — أَحْوَال is the plural of حَال", note_tr=" — ahvâl, hâl'in cem'idir")]})
S1.append({"id": "s2", "translation": {"en": "One night he went out with his servant Aslam beside him, and the two walked on until they had left Madina.",
                                       "tr": "Bir gece yanında hizmetçisi Eslem olduğu hâlde çıktı; ikisi yürüdüler, sonunda Medine'nin dışına çıktılar."},
 "tokens": [MADI("فَخَرَجَ", "kharaja", hidden=True), ZARF("لَيْلَةً", "layla", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False),
  MAAHU_HAL(),
  tok("خَادِمُهُ", "khadim", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil", "ism-fail"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The mubtada, placed after its predicate, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr.",
      "Mübtedâ (haberinden sonra), merfû, muzâf; bitişik zamir muzâfun ileyh — mahallen mecrûr.",
      segments=[seg("خَادِمُ", "khadim", "noun"), seg("هُ", "pron-3ms", "pron")]),
  tok("أَسْلَمُ", "aslam", "propn", ["badal", "atf-bayan"] + DIPT_G,
      "بَدَلٌ مِنْ «خَادِمُهُ» مَرْفُوعٌ بِالضَّمَّةِ" + ASLAM_D[0] + ".", "A badal of «his servant», in raf' like it" + ASLAM_D[1] + ".", "«Hizmetçisi»nden bedel, merfû" + ASLAM_D[2] + ".", punct="،"),
  DUAL_MADI("فَمَشَيَا", "masha", ["naqis-verbs", "thulathi-mujarrad-babs"], note_ar=" — وَرُدَّتْ أَلِفُ مَشَى إِلَى أَصْلِهَا الْيَاءِ مَعَ أَلِفِ الِاثْنَيْنِ", note_en=" — the alif of مَشَى returns to its original ya before the dual alif", note_tr=" — meşâ'nın elifi tesniye elifinden önce aslı olan yâ'ya döner"),
  HATTA_IBT(), DUAL_MADI("خَرَجَا", "kharaja", ["thulathi-mujarrad-babs"]), MINA(), MAJR("الْمَدِينَةِ", "madina", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "They saw a fire in the distance, and went toward it.", "tr": "Uzakta bir ateş gördüler ve ona doğru gittiler."},
 "tokens": [DUAL_MADI("فَرَأَيَا", "raa", ["naqis-verbs", "thulathi-mujarrad-babs"], note_ar=" — وَرُدَّتْ أَلِفُ رَأَى إِلَى أَصْلِهَا الْيَاءِ مَعَ أَلِفِ الِاثْنَيْنِ", note_en=" — the alif of رَأَى returns to its original ya before the dual alif", note_tr=" — reâ'nın elifi tesniye elifinden önce aslı olan yâ'ya döner"),
  MAFUL("نَارًا", "nar"), MIN(),
  MAJR("بَعِيدٍ", "baid", punct="،", note_ar=" — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: مِنْ مَكَانٍ بَعِيدٍ", note_en=" — the adjective of an omitted noun («from a far place»)", note_tr=" — hazfedilmiş mevsûfun sıfatı: «uzak bir yerden»"),
  DUAL_MADI("فَذَهَبَا", "dhahaba", ["thulathi-mujarrad-babs"]), JARR_PRON("إِلَيْهَا", "ila", "إِلَيْ", "هَا", " («ona»)", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "They found a woman sitting, with small children around her, crying.", "tr": "Oturan bir kadın buldular; etrafında ağlayan küçük çocuklar vardı."},
 "tokens": [DUAL_MADI("فَوَجَدَا", "wajada", ["mithal-verbs", "thulathi-mujarrad-babs"]), MAFUL("امْرَأَةً", "imraa"), NAAT("جَالِسَةً", "jalis-sitting", "nasb", ["ism-fail"], punct="،"),
  tok("وَحَوْلَهَا", "hawla", "noun", ["al-hal-jumla-wa-rabituha", "maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar"],
      "الْوَاوُ حَالِيَّةٌ، وَحَوْلَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ مُتَعَلِّقٌ بِخَبَرٍ مُقَدَّمٍ مَحْذُوفٍ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْمَرْأَةِ.",
      "The waw opens a hal clause; «around her» is an adverb of place in nasb, annexed to «her» — it hangs on an omitted FRONTED predicate, and the nominal clause is a hal of «a woman», in the seat of nasb.",
      "Hâl vâvı; «etrafında» mansûb mekân zarfı, «onun»a muzâf — mahzûf ve öne alınmış habere müteallık; isim cümlesi «kadın»dan hâl, mahallen mansûb.",
      segments=[seg("وَ", "wa", "conj"), seg("حَوْلَ", "hawla", "noun"), seg("هَا", "pron-3fs", "pron")]),
  tok("صِبْيَانٌ", "sabiy", "noun", ["mubtada-khabar", "jam-taksir"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَازَ الِابْتِدَاءُ بِهِ نَكِرَةً لِتَقَدُّمِ خَبَرِهِ الظَّرْفِ، وَهُوَ جَمْعُ تَكْسِيرٍ مُفْرَدُهُ صَبِيٌّ.",
      "The mubtada, placed after its predicate, in raf' — an indefinite may open the clause because its adverbial predicate comes first; a broken plural of صَبِيّ «boy».",
      "Mübtedâ (haberinden sonra), merfû — zarf olan haberi öne geçtiği için nekre olarak mübtedâ olabilmiştir; sabiyy'in cem-i teksîridir."),
  NAAT("صِغَارٌ", "saghir", "raf", ["jam-taksir"], note_ar=" — جَمْعُ صَغِيرٍ", note_en=" — the plural of صَغِير «small»", note_tr=" — sağîr'in cem'i"),
  MUDARI5("يَبْكُونَ", "baka", ["naqis-verbs", "jumla-sifa"], punct=".", role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِصِبْيَانٍ", role_en="; the clause qualifies «children» — in the seat of raf' as its na't", role_tr="; cümle «çocuklar»ın na'tı, mahallen merfû",
      note_ar="؛ وَأَصْلُهُ يَبْكِيُونَ: حُذِفَتِ الْيَاءُ وَضُمَّتِ الْكَافُ لِمُنَاسَبَةِ الْوَاوِ", note_en=" (from يَبْكِيُونَ: the ya drops and the kaf takes damma to suit the waw)", note_tr=" (aslı yebkiyûne: yâ düşer, kâf vâva uysun diye damme alır)")]})
S1.append({"id": "s5", "translation": {"en": "And on the fire there was a pot with water in it.", "tr": "Ateşin üzerinde de içinde su bulunan bir tencere vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True), PREP("عَلَى", "ala", *KH_MUQ, gloss_tr="«üzerinde»"), MAJR("النَّارِ", "nar"),
  ISMK("قِدْرٌ", "qidr", muakhkhar=True, note_ar=" — وَجَاءَ نَكِرَةً لِتَقَدُّمِ خَبَرِهِ شِبْهِ الْجُمْلَةِ، وَالْقِدْرُ مُؤَنَّثَةٌ فَأُنِّثَ لَهَا الْفِعْلُ", note_en=" — it may be indefinite because its jarr-phrase predicate comes first; قِدْر «pot» is feminine, so the verb takes the feminine ta", note_tr=" — câr-mecrûr haberi öne geçtiği için nekre gelebilmiştir; kıdr müennestir, bu yüzden fiil müennes geldi"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içinde»)", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", note_en="; the jarr phrase is the FRONTED predicate", note_tr="; câr-mecrûr öne alınmış haberdir"),
  tok("مَاءٌ", "ma-water", "noun", ["mubtada-khabar", "jumla-sifa"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ «فِيهَا مَاءٌ» فِي مَحَلِّ رَفْعٍ نَعْتٌ لِقِدْرٍ.",
      "The mubtada, placed after its predicate, in raf' — the nominal clause «with water in it» qualifies «a pot», in the seat of raf'.", "Mübtedâ (haberinden sonra), merfû — «içinde su var» isim cümlesi «tencere»nin na'tı, mahallen merfû.", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "ʿUmar greeted her, and asked her about the children's crying.", "tr": "Ömer ona selâm verdi ve çocukların ağlamasını sordu."},
 "tokens": [MADI_D("فَسَلَّمَ", "sallama", ["form-ii-verbs"]), UMAR_F(), JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («ona»)", punct="،"),
  ENC_MADI("وَسَأَلَهَا", "saala", "هَا", hidden=True), PREP("عَنْ", "an", gloss_tr="«hakkında»"),
  MAJR("بُكَاءِ", "bukaa", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الصِّبْيَانِ", "sabiy", extra=["jam-taksir"], punct=".")]})

# ---- Chapter 2 — الْقِدْرُ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "She said: «They are crying from hunger, and I have no food.»", "tr": "Kadın dedi: «Açlıktan ağlıyorlar; yanımda da yiyecek yok.»"},
 "tokens": [QALAT("فَقَالَتْ", punct=":"), INNA_ENC("إِنَّهُمْ", "هُمْ", " («onlar»)"),
  MUDARI5("يَبْكُونَ", "baka", ["naqis-verbs", "inna-wa-akhawatuha"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", role_en="; the clause fills the seat of raf' as the predicate of إِنَّ", role_tr="; cümle inne'nin haberi, mahallen merfû"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ يُفِيدُ التَّعْلِيلَ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter giving the cause («from, because of»), voweled with fatha before the following ال.", "«-den» — sebep bildiren cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("الْجُوعِ", "ju", punct="،"),
  tok("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ma-la-laysa-wa-la-al-jins"], WA_AR + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
      "The waw conjoins; لَيْسَ «there is not» is the frozen defective verb, built on fatha: it raises its noun and puts its predicate in nasb.", "«ve» + leyse: câmid nâkıs fiil, fetha üzere mebnî; ismini ref, haberini nasb eder.",
      segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  INDI("خَبَرُ لَيْسَ مُقَدَّمٌ", "FRONTED predicate of لَيْسَ", "leyse'nin öne alınmış haberine"),
  tok("طَعَامٌ", "taam", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of لَيْسَ, placed after its predicate, in raf'.", "Leyse'nin ismi (haberinden sonra), merfû.", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "ʿUmar said: «What is in this pot?»", "tr": "Ömer dedi: «Bu tencerede ne var?»"},
 "tokens": [QALA_F("فَقَالَ"), UMAR_F(punct=":"),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "mubtada-khabar"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The interrogative «what?», built on sukun, in the seat of raf' as the mubtada.", "İstifhâm ismi «ne?», sükûn üzere mebnî, mübtedâ olarak mahallen merfû."),
  PREP("فِي", "fi", "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ", "; the jarr phrase is the predicate", "; câr-mecrûr mahzûf habere müteallıktır", gloss_tr="«-de»"),
  ISHARA("هٰذِهِ", "hadhihi", "جَرٍّ بِفِي", "jarr after فِي", "mecrûr", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"),
  BADAL("الْقِدْرِ", "qidr", "jarr", punct="؟")]})
S2.append({"id": "s3", "translation": {"en": "She said: «There is water in it, with which I keep them quiet — perhaps they will fall asleep.»", "tr": "Dedi: «İçinde su var, onunla onları susturuyorum; belki uyurlar.»"},
 "tokens": [QALAT("فَقَالَتْ", punct=":"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içinde»)", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", note_en="; the jarr phrase is the FRONTED predicate", note_tr="; câr-mecrûr öne alınmış haberdir"),
  tok("مَاءٌ", "ma-water", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The mubtada, placed after its predicate, in raf'.", "Mübtedâ (haberinden sonra), merfû."),
  MUDARI("أُسْكِتُهُمْ", "askata", ["form-iv-verbs", "jumla-sifa"], who="أَنَا", enc="هُمْ", wujub=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِمَاءٍ", note_en=" — the clause qualifies «water», in the seat of raf' as its na't", note_tr=" — cümle «su»yun na'tı, mahallen merfû"),
  BIHI(punct="،"),
  tok("لَعَلَّهُمْ", "laalla", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya", "al-bariz-al-muttasil"],
      "لَعَلَّ حَرْفُ تَرَجٍّ مُشَبَّهٌ بِالْفِعْلِ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُهَا.",
      "لَعَلَّ «perhaps» is the sister of إِنَّ that hopes: its noun in nasb, its predicate in raf'; the attached «they» is its noun, in the seat of nasb.",
      "Lealle — inne'nin kardeşlerinden terecci harfi: ismini nasb, haberini ref eder; bitişik «onlar» ismi, mahallen mansûb.",
      segments=[seg("لَعَلَّ", "laalla", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  MUDARI5("يَنَامُونَ", "nama", ["hollow-verbs", "inna-wa-akhawatuha"], punct=".", role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَعَلَّ", role_en="; the clause fills the seat of raf' as the predicate of لَعَلَّ", role_tr="; cümle lealle'nin haberi, mahallen merfû")]})
S2.append({"id": "s4", "translation": {"en": "She said: «If I had food, I would not leave them crying.»", "tr": "Dedi: «Yanımda yiyecek olsaydı, onları ağlar hâlde bırakmazdım.»"},
 "tokens": [QALAT("وَقَالَتْ", punct=":"),
  tok("لَوْ", "law", "part", ["huruf-al-shart-fil-kafiya", "al-qasam-wal-shart-fil-kafiya"],
      "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ يَدُلُّ عَلَى امْتِنَاعِ الْجَوَابِ لِامْتِنَاعِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ.",
      "The conditional لَوْ «if (it were so)»: it governs no jazm and marks the answer as not happening because the condition did not happen.",
      "Lev: cezm etmeyen şart harfi; şart gerçekleşmediği için cevabın da gerçekleşmediğini bildirir."),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَهُوَ فِعْلُ الشَّرْطِ.",
      "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb — here the verb of the condition.", "«idi» — nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder — burada şart fiilidir."),
  INDI("خَبَرُ كَانَ مُقَدَّمٌ", "FRONTED predicate of كَانَ", "kâne'nin öne alınmış haberine"),
  ISMK("طَعَامٌ", "taam", muakhkhar=True),
  MA_NAFIYA(),
  MADI_T("تَرَكْتُهُمْ", "taraka", who="ana", enc="هُمْ", note_ar=" — وَالْجُمْلَةُ جَوَابُ لَوْ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ، وَالْأَكْثَرُ فِي جَوَابِ لَوْ الْمَنْفِيِّ بِمَا أَلَّا يَقْتَرِنَ بِاللَّامِ",
      note_en="; the clause is the answer of لَوْ and has no seat — an answer negated by مَا usually goes without the lam", note_tr="; cümle lev'in cevabıdır, i'râbdan mahalli yoktur — mâ ile olumsuzlanan cevap çoğunlukla lâm almaz"),
  MUDARI5("يَبْكُونَ", "baka", ["naqis-verbs", "hal", "al-hal-jumla-wa-rabituha"], punct=".", role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ «هُمْ»", role_en="; the clause is a hal of «them», in the seat of nasb", role_tr="; cümle «onları» zamirinden hâl, mahallen mansûb")]})
S2.append({"id": "s5", "translation": {"en": "Then she complained to him that ʿUmar had neglected her and her children.", "tr": "Sonra ona, Ömer'in kendisini ve çocuklarını ihmal ettiğinden yakındı."},
 "tokens": [THUMMA(),
  tok("شَكَتْ", "shaka", "verb", ["thulathi-mujarrad-babs", "naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَأَصْلُهُ شَكَاتْ.",
      "Past verb built on a fatha estimated on the alif, which dropped before the quiescent ta of the feminine (from شَكَاتْ); the doer is the hidden «she».",
      "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî (aslı şekât); tâ te'nîs içindir; fâil gizli zamir «o»."),
  ILAYHI(),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِمَّا بَعْدَهُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِشَكَتْ.",
      "أَنَّ «that», the verb-like particle that builds a masdar — the clause it builds is the object of «complained», in the seat of nasb.",
      "Enne — te'kîd, nasb ve masdar harfi; kurduğu müevvel masdar «yakındı»nın mef'ûlü, mahallen mansûb."),
  tok("عُمَرَ", "umar", "propn", ["inna-wa-akhawatuha"] + DIPT_G, "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ" + UMAR_D[0] + ".", "The noun of أَنَّ, in nasb" + UMAR_D[1] + ".", "Enne'nin ismi, mansûb" + UMAR_D[2] + "."),
  QAD(), MADI("غَفَلَ", "ghafala", hidden=True, note_ar=KH_ANNA_CL[0], note_en=KH_ANNA_CL[1], note_tr=KH_ANNA_CL[2]),
  JARR_PRON("عَنْهَا", "an", "عَنْ", "هَا", " («ondan»)"), PREP("وَعَنْ", "an", gloss_tr="«-den»"),
  ENC_NOUN("صِبْيَانِهَا", "sabiy", "هَا", "majr", ["jam-taksir"], punct=".")]})
S2.append({"id": "s6", "translation": {"en": "She did not know him; so ʿUmar kept silent, and did not tell her his name.", "tr": "Kadın onu tanımıyordu; Ömer de sustu ve ona adını söylemedi."},
 "tokens": [tok("وَكَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.",
      "The waw conjoins; كَانَ is the defective past verb; the ta marks the feminine, and its noun is the hidden pronoun «she».", "«ve» + nâkıs mâzî fiil kâne; tâ te'nîs içindir, ismi gizli zamir «o».",
      segments=[seg("وَ", "wa", "conj"), seg("كَانَتْ", "kana", "verb")]),
  LA_NAFIYA(), MUDARI("تَعْرِفُهُ", "arafa", ["kana-wa-akhawatuha"], who="هِيَ", enc="هُ", punct="،", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  MADI("فَسَكَتَ", "sakata"), UMAR_F(), WA_LAM(),
  tok("يُخْبِرْهَا", "akhbara", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "Present verb in jazm by لَمْ, its sign the sukun; the doer «he» is hidden and the attached «her» is its object, in the seat of nasb.",
      "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli «o»; bitişik «onu (kadını)» mef'ûlün bih, mahallen mansûb.",
      segments=[seg("يُخْبِرْ", "akhbara", "verb"), seg("هَا", "pron-3fs", "pron")]),
  BI_NOUN("بِاسْمِهِ", "ism-name", "اسْمِهِ", enc="هِ", punct=".")]})

# ---- Chapter 3 — دَارُ الدَّقِيقِ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "ʿUmar and Aslam went back to Madina in haste.", "tr": "Ömer ile Eslem acele ederek Medine'ye döndüler."},
 "tokens": [MADI("فَرَجَعَ", "rajaa"), UMAR_F(), ATF("وَأَسْلَمُ", "aslam", "propn", "raf", DIPT_G, *ASLAM_D), ILA(), MAJR("الْمَدِينَةِ", "madina"),
  DUAL_MUDARI("يُسْرِعَانِ", "asraa", (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ عُمَرَ وَأَسْلَمَ", "; the clause is a hal of ʿUmar and Aslam, in the seat of nasb", "; cümle Ömer ile Eslem'den hâl, mahallen mansûb"),
      extra=["form-iv-verbs", "hal", "al-hal-jumla-wa-rabituha"], punct=".")]})
S3.append({"id": "s2", "translation": {"en": "They came to the flour store, and ʿUmar took out of it a load of flour and some fat.", "tr": "Un ambarına geldiler; Ömer oradan bir yük un ve biraz yağ çıkardı."},
 "tokens": [DUAL_MADI("فَأَتَيَا", "ata", ["naqis-verbs", "thulathi-mujarrad-babs"], note_ar=" — وَأَتَى هُنَا مُتَعَدٍّ بِنَفْسِهِ: أَتَى الْمَكَانَ، وَرُدَّتْ أَلِفُهُ إِلَى أَصْلِهَا الْيَاءِ", note_en=" — أَتَى here takes its object directly («came to the place»); its alif returns to its original ya", note_tr=" — etâ burada doğrudan mef'ûl alır («yere geldi»); elifi aslı olan yâ'ya döner"),
  MAFUL("دَارَ", "dar", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الدَّقِيقِ", "daqiq-flour", punct="،"),
  MADI_D("فَأَخْرَجَ", "akhraja", ["form-iv-verbs"]), UMAR_F(), JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («oradan»)"),
  MAFUL("حِمْلًا", "himl"), PREP("مِنْ", "min", " لِبَيَانِ الْجِنْسِ", " that names the kind («a load OF flour»)", " — cins beyânı için", gloss_tr="«-den»"), MAJR("دَقِيقٍ", "daqiq-flour"),
  ATF("وَشَيْئًا", "shay", "noun", "nasb"), PREP("مِنْ", "min", " لِبَيَانِ الْجِنْسِ", " that names the kind («some OF fat»)", " — cins beyânı için", gloss_tr="«-den»"), MAJR("شَحْمٍ", "shahm", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "Then he said: «Aslam, put it on my back.»", "tr": "Sonra dedi: «Eslem, onu sırtıma koy.»"},
 "tokens": [THUMMA(), QALA_F("قَالَ", punct=":", hidden=True), YA(),
  tok("أَسْلَمُ", "aslam", "propn", ["vocative-munada"], "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.", "The vocative: a single proper name, built on damma, in the seat of nasb.", "Münâdâ: müfred alem, damme üzere mebnî, mahallen mansûb.", punct="،"),
  AMR("ضَعْهُ", "wadaa", ["mithal-verbs"], enc="هُ", note_ar=" — وَحُذِفَتْ وَاوُهُ (فَاءُ الْفِعْلِ) كَمَا حُذِفَتْ فِي مُضَارِعِهِ يَضَعُ", note_en=" — its first radical waw drops, as it does in the present يَضَعُ", note_tr=" — fâ'ü'l-fiili olan vâv, muzârii yeda'da olduğu gibi düşer"),
  ALA(), YA_MUTAKALLIM_N("ظَهْرِي", "zahr", "ظَهْرِ", "مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", extra=["huruf-jarr"], punct=".")]})
S3.append({"id": "s4", "translation": {"en": "Aslam wanted to carry it for him, but ʿUmar refused.", "tr": "Eslem onu onun yerine taşımak istedi; fakat Ömer kabul etmedi."},
 "tokens": [MADI_D("فَأَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"]), ASLAM_F(), AN_MAFUL(),
  MANSUB_AN("يَحْمِلَهُ", "hamala", enc="هُ"), JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («onun yerine»)", punct="،"),
  MADI_ALIF("فَأَبَى", "aba"), UMAR_F(punct=".")]})
S3.append({"id": "s5", "translation": {"en": "He said: «If you carry it for me today, who will carry my burden for me on the Day of Resurrection?»", "tr": "Dedi: «Bugün onu benim yerime sen taşırsan, kıyamet günü benim günah yükümü benim yerime kim taşıyacak?»"},
 "tokens": [QALA_F("وَقَالَ", punct=":", hidden=True), IN_SHART("إِنْ"),
  MADI_T("حَمَلْتَهُ", "hamala", who="anta", enc="هُ", shart=True), ANNI_AN(),
  ZARF("الْيَوْمَ", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False, punct="،"),
  tok("فَمَنْ", "man-istifham", "pron", ["al-fa-fi-jawab-al-shart", "al-istifham", "mubtada-khabar", "al-majzum-wal-shart-wal-jaza"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَمَنْ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
      "The fa binds the answer of the condition (an answer that is a question must take it); مَنْ «who?» is the interrogative, built on sukun in the seat of raf' as mubtada — the nominal clause is the answer, in the seat of jazm.",
      "Fâ şartın cevabını bağlar (soru olan cevap fâ alır); men «kim?» istifhâm ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû — isim cümlesi şartın cevabı, mahallen meczûm.",
      segments=[seg("فَ", "fa", "conj"), seg("مَنْ", "man-istifham", "pron")]),
  MUDARI("يَحْمِلُ", "hamala", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ مَنْ", note_en=" — the clause is the predicate of مَنْ, in the seat of raf'", note_tr=" — cümle men'in haberi, mahallen merfû"),
  ANNI_AN(), YA_MUTAKALLIM_N("وِزْرِي", "wizr", "وِزْرِ", "مَفْعُولٌ بِهِ مَنْصُوبٌ", "The direct object, in nasb", "Mef'ûlün bih, mansûb", extra=["maful-bihi"]),
  ZARF("يَوْمَ", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), MUDAF_ILAYH("الْقِيَامَةِ", "qiyama", punct="؟")]})
S3.append({"id": "s6", "translation": {"en": "ʿUmar carried it on his back and set out on foot to the woman, with Aslam beside him.", "tr": "Ömer onu sırtına aldı ve yürüyerek kadına doğru yola çıktı; Eslem de yanındaydı."},
 "tokens": [ENC_MADI("فَحَمَلَهُ", "hamala", "هُ"), UMAR_F(), ALA(), ENC_NOUN("ظَهْرِهِ", "zahr", "هِ", "majr", punct="،"),
  MADI("وَخَرَجَ", "kharaja", hidden=True),
  tok("مَاشِيًا", "mashi", "noun", ["hal", "ism-maqsur-manqus", "ism-fail"],
      "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ عَلَى الْيَاءِ — يُبَيِّنُ هَيْئَةَ الْفَاعِلِ؛ وَهُوَ اسْمُ فَاعِلٍ مَنْقُوصٌ، تَظْهَرُ الْفَتْحَةُ عَلَى يَائِهِ لِخِفَّتِهَا.",
      "The hal «on foot», in nasb by a fatha that SHOWS on the ya — it states the doer's condition; a manqūṣ active participle, whose ya bears the light fatha openly.",
      "Hâl «yürüyerek», yâ üzerinde zâhir fetha ile mansûb — fâilin hâlini bildirir; mankûs ism-i fâil, fetha hafif olduğu için yâ'sında görünür."),
  ILA(), MAJR("الْمَرْأَةِ", "imraa"),
  tok("وَأَسْلَمُ", "aslam", "propn", ["al-hal-jumla-wa-rabituha", "mubtada-khabar"] + DIPT_G, "الْوَاوُ حَالِيَّةٌ، وَأَسْلَمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ" + ASLAM_D[0] + ".",
      "The waw opens a hal clause; «Aslam» is the mubtada, in raf'" + ASLAM_D[1] + ".", "Hâl vâvı; «Eslem» mübtedâ, merfû" + ASLAM_D[2] + ".", segments=[seg("وَ", "wa", "conj"), seg("أَسْلَمُ", "aslam", "propn")]),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "mubtada-khabar", "al-hal-jumla-wa-rabituha"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "An adverb of place «with», in nasb and annexed to «him» — it hangs on the omitted predicate, and the nominal clause is a hal in the seat of nasb.",
      "Mekân zarfı «yanında», mansûb, «o»na muzâf — mahzûf habere müteallık; isim cümlesi hâl olarak mahallen mansûb.",
      punct=".", segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")])]})

# ---- Chapter 4 — الصِّبْيَانُ يَضْحَكُونَ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "Then he set the load down beside the woman, and put the flour and the fat into the pot.", "tr": "Sonra yükü kadının yanına bıraktı; unu ve yağı tencereye koydu."},
 "tokens": [THUMMA(),
  tok("أَلْقَى", "alqa", "verb", ["form-iv-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "Past verb built on a fatha estimated on the alif; the doer «he» is hidden.", "Elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil gizli «o»."),
  MAFUL("الْحِمْلَ", "himl"), INDA(), MUDAF_ILAYH("الْمَرْأَةِ", "imraa", punct="،"),
  MADI("وَجَعَلَ", "jaala", hidden=True), MAFUL("الدَّقِيقَ", "daqiq-flour"), ATF("وَالشَّحْمَ", "shahm", "noun", "nasb"), FI(), MAJR("الْقِدْرِ", "qidr", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He kept blowing under the pot until the food was cooked.", "tr": "Yemek pişinceye kadar tencerenin altını üfleyip durdu."},
 "tokens": [KANA_HID("وَكَانَ"), MUDARI_KH("يَنْفُخُ", "nafakha"), ZARF("تَحْتَ", "tahta"), MUDAF_ILAYH("الْقِدْرِ", "qidr"), HATTA_IBT(),
  MAJHUL("طُبِخَ", "tabakha", ["thulathi-mujarrad-babs"]), NAIB("الطَّعَامُ", "taam", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "Then he set the food before the children, and they ate until they were full.", "tr": "Sonra yemeği çocukların önüne yaklaştırdı; onlar da doyuncaya kadar yediler."},
 "tokens": [THUMMA(), MADI_D("قَرَّبَ", "qarraba", ["form-ii-verbs"], hidden=True), MAFUL("الطَّعَامَ", "taam"), ILA(), MAJR("الصِّبْيَانِ", "sabiy", extra=["jam-taksir"], punct="،"),
  VERB_WAW("فَأَكَلُوا", "akala", ["thulathi-mujarrad-babs"]), HATTA_IBT(), VERB_WAW("شَبِعُوا", "shabia", ["thulathi-mujarrad-babs"], punct=".")]})
S4.append({"id": "s4", "translation": {"en": "He kept sitting with them until they laughed and played.", "tr": "Onlar gülüp oynayıncaya kadar yanlarında oturmaya devam etti."},
 "tokens": [tok("وَمَا", "ma-nafiya", "part", ["la-nafiya", "kana-wa-akhawatuha"], WA_AR + "مَا حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ — وَنَفْيُ زَالَ إِثْبَاتٌ لِلِاسْتِمْرَارِ.",
      "The waw conjoins; مَا negates — and negating زَالَ «ceased» gives «kept on».", "«ve» + mâ nefiy harfi, sükûn üzere mebnî — zâle'nin nefyi devamı ispat eder.",
      segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَمَا زَالَ تُفِيدُ الِاسْتِمْرَارَ.",
      "A defective past verb, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb; its noun is the hidden «he» — مَا زَالَ «kept on» states continuance.",
      "Kâne'nin kardeşlerinden nâkıs mâzî fiil, fetha üzere mebnî; ismini ref, haberini nasb eder; ismi gizli zamir «o» — mâ zâle devam bildirir."),
  tok("جَالِسًا", "jalis-sitting", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ مَا زَالَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of مَا زَالَ, in nasb.", "Mâ zâle'nin haberi, mansûb."),
  tok("عِنْدَهُمْ", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "An adverb of place «with», in nasb and annexed to «them», which fills the seat of jarr.", "Mekân zarfı «yanlarında», mansûb; «onlar» zamirine muzâf, zamir mahallen mecrûr.",
      segments=[seg("عِنْدَ", "inda", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  HATTA_IBT(), VERB_WAW("ضَحِكُوا", "dahika", ["thulathi-mujarrad-babs"]), VERB_WAW("وَلَعِبُوا", "laiba", ["thulathi-mujarrad-babs"], punct=".")]})
S4.append({"id": "s5", "translation": {"en": "The woman was praying for good for him, but she did not know that he was the Commander of the Faithful.", "tr": "Kadın ona hayır dua ediyordu; fakat onun mü'minlerin emîri olduğunu bilmiyordu."},
 "tokens": [KANAT_K("وَكَانَتِ"), ISMK("الْمَرْأَةُ", "imraa"),
  MUDARI("تَدْعُو", "daa", ["kana-wa-akhawatuha"], who="هِيَ", naqis="و", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  tok("لَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَفُتِحَتِ اللَّامُ مَعَ الضَّمِيرِ.", "The lam is a jarr letter; the attached «him» fills the seat of jarr — the lam takes fatha before a pronoun.", "Lâm cer harfi; bitişik zamir mahallen mecrûr («onun için») — lâm zamirle fethalı okunur.", segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")]), BI_NOUN("بِالْخَيْرِ", "khayr", "الْخَيْرِ", punct="،"),
  INNA_ENC("وَلَكِنَّهَا", "هَا", " («o»)"), LAM_JAZM(), JAZM_V("تَعْلَمْ", "alima", ["mafulayn"], hidden="هِيَ"),
  ANNAHU(note=(" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ تَعْلَمْ", "; the clause it builds stands in for both objects of «know»", "; kurduğu müevvel masdar ta'lem'in iki mef'ûlünün yerini tutar")),
  tok("أَمِيرُ", "amir", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The predicate of أَنَّ, in raf' and annexed.", "Enne'nin haberi, merfû, muzâf."),
  MUMININ_MI(punct=".")]})
S4.append({"id": "s6", "translation": {"en": "Then ʿUmar went back to Madina, the children having fallen asleep.", "tr": "Sonra Ömer Medine'ye döndü; çocuklar da uykuya dalmıştı."},
 "tokens": [THUMMA(), MADI("رَجَعَ", "rajaa"), UMAR_F(), ILA(), MAJR("الْمَدِينَةِ", "madina", punct="،"), WA_QAD(),
  MADI("نَامَ", "nama", ["hollow-verbs", "al-hal-jumla-wa-rabituha"]), FAIL("الصِّبْيَانُ", "sabiy", extra=["jam-taksir"], punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf; five entries are new ---------------------------------
PREF = ["qisas-al-nabiyyin-4", "al-kafiya", "adam-wa-iblis", "al-amana-wa-al-khashaba", "al-usul-al-munifa", "izhar-al-asrar", "al-asad-wa-al-arnab",
        "luqman-wa-ibnuh", "musa-wa-bani-israil", "musa-wa-firawn", "juha-wa-al-himar", "ashab-al-kahf", "talkhis-al-miftah", "aqaid-ahl-al-sunna", "qisas-al-nabiyyin-2"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != PKG.name)
def _pkg_dir(p): return ROOT / "content/samples" / p
FORCE = {"umar": "al-usul-al-munifa", "ibn-bn": "al-usul-al-munifa", "sabiy": "kitab-al-sulh", "ma-istifham": "qisas-al-nabiyyin-4", "man-istifham": "qisas-al-nabiyyin-4"}
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
 "aslam": {"lemma": "أَسْلَمُ", "root": "س ل م", "pos": "propn", "gloss": {"en": "Aslam — ʿUmar's servant (mawlā); a diptote name on the pattern أَفْعَل", "tr": "Eslem — Hz. Ömer'in hizmetçisi (mevlâsı); ef'al vezninde gayr-i munsarif isim"}, "level": 4},
 "khattab": {"lemma": "الْخَطَّاب", "root": "خ ط ب", "pos": "propn", "gloss": {"en": "al-Khaṭṭāb — the father of the caliph ʿUmar (عُمَرُ بْنُ الْخَطَّابِ)", "tr": "Hattâb — Halife Ömer'in babası (Ömer bin Hattâb)"}, "level": 4},
 "daqiq-flour": {"lemma": "دَقِيق", "root": "د ق ق", "pos": "noun", "gloss": {"en": "flour, meal (دَارُ الدَّقِيقِ: the flour store)", "tr": "un (dâru'd-dakîk: un ambarı)"}, "level": 4},
 "shahm": {"lemma": "شَحْم", "root": "ش ح م", "pos": "noun", "plural": "شُحُوم", "gloss": {"en": "fat, suet", "tr": "iç yağı, yağ"}, "level": 4},
 "askata": {"lemma": "أَسْكَتَ", "root": "س ك ت", "pos": "verb", "gloss": {"en": "to quiet, to silence someone (Form IV of سَكَتَ)", "tr": "susturmak (sekete'nin if'âl bâbı)"}, "level": 4},
}
NEW_VERBS = {
 "askata": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَسْكَت", "سْكِت", "أَسْكِت", "إِسْكَات", "مُسْكِت", "مُسْكَت", "أُسْكِتَ", "يُسْكَتُ",
                       "أَسْكَتَهُ يُسْكِتُهُ إِسْكَاتًا: جَعَلَهُ يَسْكُتُ — مُتَعَدٍّ بِالْهَمْزَةِ مِنْ سَكَتَ يَسْكُتُ."),
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
 "id": "umar-wa-al-qidr",
 "storyGroup": "umar-wa-al-qidr",
 "title": {"ar": "عُمَرُ وَالْقِدْرُ", "en": "ʿUmar and the Cooking Pot", "tr": "Ömer ve Tencere"},
 "subtitle": {"ar": "الْخَلِيفَةُ يَحْمِلُ الدَّقِيقَ عَلَى ظَهْرِهِ إِلَى صِبْيَانٍ جِيَاعٍ، وَيَطْبُخُ لَهُمْ بِيَدِهِ — قِصَّةٌ لِلْمُسْتَوَى الرَّابِعِ",
              "en": "The caliph carries flour on his own back to hungry children and cooks for them with his own hand — a story for the fourth level",
              "tr": "Halife, aç çocuklara unu kendi sırtında taşır ve onlar için kendi eliyle yemek pişirir — dördüncü seviye için bir hikâye"},
 "level": 4,
 "levelName": "Upper Intermediate",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُتَدَرِّجَةٌ (الْمُسْتَوَى الرَّابِعُ) لِخَبَرِ عُمَرَ بْنِ الْخَطَّابِ مَعَ الْمَرْأَةِ وَصِبْيَانِهَا وَالْقِدْرِ، الْمَرْوِيِّ فِي تَارِيخِ الطَّبَرِيِّ وَفِي مَنَاقِبِ عُمَرَ لِابْنِ الْجَوْزِيِّ. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ أَحَدِ الْكِتَابَيْنِ، وَالْحِوَارُ فِيهِ حِكَايَةٌ بِالْمَعْنَى لَا لَفْظٌ مَرْوِيٌّ، فَلَا يُنْسَبُ شَيْءٌ مِنْهُ إِلَى عُمَرَ وَلَا إِلَى غَيْرِهِ.",
  "en": "ORIGINAL Level-4 graded Arabic: the report of ʿUmar ibn al-Khaṭṭāb, the woman, her hungry children and the pot of water, told in al-Ṭabarī's Tārīkh al-rusul wa-l-mulūk and in Ibn al-Jawzī's Manāqib ʿUmar ibn al-Khaṭṭāb, RETOLD FREELY in the wording of a graded reader. No sentence is a quotation from either book; the dialogue retells the sense of the report and is not a recorded saying, so none of it may be cited as the words of ʿUmar or of anyone else.",
  "tr": "ÖZGÜN 4. seviye kademeli Arapça: Taberî'nin Târîhu'r-rusul ve'l-mülûk'ünde ve İbnü'l-Cevzî'nin Menâkıbu Ömer'inde anlatılan, Ömer bin Hattâb'ın kadın, aç çocukları ve su kaynayan tencere ile ilgili haberi, kademeli okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bu iki kitaptan alıntı değildir; konuşmalar haberin mânâsını aktarır, rivayet edilmiş söz değildir; hiçbiri Ömer'in veya bir başkasının sözü olarak nakledilemez.",
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
