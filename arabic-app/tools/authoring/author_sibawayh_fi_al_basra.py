"""Author content/samples/sibawayh-fi-al-basra — «سِيبَوَيْهِ فِي الْبَصْرَةِ», an ORIGINAL historical story at Level 4 (Upper Intermediate).

ORIGINAL graded Arabic: Sībawayh (ʿAmr ibn ʿUthmān), a young man of Persian origin, comes to Basra to seek knowledge and sits
in the ḥadīth circle of Ḥammād ibn Salama; reading a ḥadīth to him, he errs in the iʿrāb of a word and is corrected; he
resolves to learn grammar so that he will not err again, keeps close to al-Khalīl ibn Aḥmad and learns from other Basran
scholars, and writes the book that the grammarians call simply «al-Kitāb». A closing chapter reflects on why grammar guards
the meaning. Only the well-attested core is kept, as the ṭabaqāt books tell it (al-Zubaydī, Ṭabaqāt al-naḥwiyyīn
wa-l-lughawiyyīn; al-Sīrāfī, Akhbār al-naḥwiyyīn al-baṣriyyīn). The words of the slip are reported in varying forms, so they
are NOT quoted: the story says only that he erred in the iʿrāb of a word and was corrected. His resolve is told in narration,
never as a recorded saying. The Baghdad debate with al-Kisāʾī (al-masʾala al-zunbūriyya) is left out: its details are disputed.

Five chapters, twenty-five sentences, in the Level-4 register: kāna and its sisters (كَانَ، كَانَتِ، كَانَ with a hidden noun and
a conditional khabar, صَارَ، مَا زَالَ), إِنَّ with a clause as its khabar, the ḥāl as a clause (يَطْلُبُ، يَكْتُبُ، يَسْأَلُهُ), the passive
(عُرِفَ، ذُكِرَ), the conditionals إِذَا (with a verbal and with a nominal answer bound by فَ) and لَوْ (with the lām of its answer),
the fronted khabar before an indefinite mubtadaʾ, the diptotes (عُثْمَانَ، سَلَمَةَ، أَحْمَدَ، فَارِسَ، عُلَمَاءَ), the name built on kasra
(سِيبَوَيْهِ), حَتَّى of purpose with the subjunctive beside حَتَّى of ibtidāʾ, and the lām of taʿlīl.
Written on the authoring kit (story_kit.py). Three entries are new — نَحْو in its sense «grammar» (`nahw-grammar`; the
shelf's `nahw` is «direction»), the land name فَارِس (`faris-persia`) and the name سَلَمَة (`salama-name`). No verb is new: every
paradigm is copied from a package that already owns the verb. Regenerate with:
python3 tools/authoring/author_sibawayh_fi_al_basra.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "sibawayh-fi-al-basra"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"نَا": "pron-1p", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"نَا": "نَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})
N = lambda s: unicodedata.normalize("NFC", s)

# ---- the clause seats and short notes ------------------------------------------------------------------------------------
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
KH_ZALA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ", "; the clause is the predicate of زَالَ, in the seat of nasb", "; cümle zâle'nin haberi olarak mahallen mansûb")
NO_SEAT_JAWAB = (" — جَوَابُ الشَّرْطِ، وَالْجُمْلَةُ لَا مَحَلَّ لَهَا لِأَنَّهَا جَوَابُ شَرْطٍ غَيْرِ جَازِمٍ",
                 " — the answer of the condition; its clause has no seat, being the answer of a condition that governs no jazm",
                 " — şartın cevabı; cezm etmeyen şartın cevabı olduğu için cümlenin i'râbdan mahalli yoktur")
SHART_IDHA = (" — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا",
              " — the condition's verb; its clause is in the seat of jarr, annexed to إِذَا",
              " — şart fiili; cümlesi izâ'ya muzâfun ileyh olarak mahallen mecrûr")
IBN_DROP = (" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ",
            " — it loses its tanwin because it is described by «ibn» annexed to a name",
            " — alem'e muzâf «ibn» ile vasıflandığı için tenvini düşmüştür")
DIPT_G = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
DIPT_G2 = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh"]
def NAAT_OF(seat, of_ar, of_en, of_tr, second=False):
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return (" — وَالْجُمْلَةُ فِي مَحَلِّ " + s[0] + " نَعْتٌ " + ("ثَانٍ " if second else "") + "لِـ«" + of_ar + "»",
            "; the clause qualifies «" + of_en + "» — " + ("a second na't, " if second else "") + "in the seat of " + s[1],
            "; cümle «" + of_tr + "» için " + ("ikinci " if second else "") + "na't, mahallen " + s[2])
def JAR_NAAT(seat, of_ar, of_en, of_tr, second=False):
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return ("؛ وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ " + s[0] + " نَعْتٌ " + ("ثَانٍ " if second else "") + "لِـ«" + of_ar + "»",
            "; the jarr phrase qualifies «" + of_en + "»" + (" (a second na't)" if second else "") + ", in the seat of " + s[1],
            "; câr-mecrûr «" + of_tr + "» için " + ("ikinci " if second else "") + "na't, mahallen " + s[2])

# ---- the name built on kasra ---------------------------------------------------------------------------------------------
SIB_N = (" — عَلَمٌ مُرَكَّبٌ مَخْتُومٌ بِـ«وَيْهِ»، وَمَا خُتِمَ بِـ«وَيْهِ» يُبْنَى عَلَى الْكَسْرِ",
         " — a compound name ending in «-wayhi»; such names are built on kasra in every seat",
         " — «-veyhi» ile biten mürekkep özel isim; böyle isimler her yerde kesre üzere mebnîdir")
SIB_G = "al-mabni-al-lazim-al-mudmarat-wal-isharat-wal-mawsulat-wa-faali-wal-aswat-wal-murakkab"
def SIB(role, punct=None, pre=None):
    r = {"ismk": ("اسْمُ كَانَ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ", "The noun of كَانَ, built on kasra, in the seat of raf'", "Kâne'nin ismi, kesre üzere mebnî, mahallen merfû", "kana-wa-akhawatuha"),
         "fail": ("فَاعِلٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ", "The doer (fa'il), built on kasra, in the seat of raf'", "Fâil, kesre üzere mebnî, mahallen merfû", "fail"),
         "mubtada": ("مُبْتَدَأٌ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ", "The mubtada, built on kasra, in the seat of raf'", "Mübtedâ, kesre üzere mebnî, mahallen merfû", "mubtada-khabar"),
         "mudaf": ("مُضَافٌ إِلَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ", "The second term of the idafa, built on kasra, in the seat of jarr", "Muzâfun ileyh, kesre üzere mebnî, mahallen mecrûr", "idafa-definiteness")}[role]
    full = ("وَ" if pre == "wa" else "") + "سِيبَوَيْهِ"
    return tok(full, "sibawayh", "propn", [r[3], SIB_G],
        (WA_AR if pre == "wa" else "") + r[0] + SIB_N[0] + ".", ("The waw conjoins; " if pre == "wa" else "") + r[1] + SIB_N[1] + ".",
        ("«ve» + " if pre == "wa" else "") + r[2] + SIB_N[2] + ".", punct=punct,
        segments=[seg("وَ", "wa", "conj"), seg("سِيبَوَيْهِ", "sibawayh", "propn")] if pre == "wa" else None)

# ---- the verb and particle shapes the kit does not carry -----------------------------------------------------------------
def MADI_D(full, lex, extra=None, hidden=False, punct=None, note_ar="", note_en="", note_tr=""):
    """a past verb of a DERIVED form (أَخْطَأَ، بَيَّنَ، تَغَيَّرَ) — MADI without the mujarrad-bāb anchor"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", extra or [],
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + hid + note_ar + ".",
        en0 + "past verb built on fatha" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on fatha, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», fetha üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
def ZALA(hidden=False):
    return tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + ("، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else "") + " — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ.",
        "زَالَ is a defective past verb, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb" + ("; its noun is the hidden pronoun «he»" if hidden else "") + " — after a negation it means «never ceased».",
        "Zâle: kâne'nin kardeşlerinden, fetha üzere mebnî nâkıs mâzî; ismini ref, haberini nasb eder" + ("; ismi gizli zamir «o»" if hidden else "") + " — nefiyle birlikte devamlılık bildirir.")
def LAHU(punct=None):
    return tok("لَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
        "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَفُتِحَتِ اللَّامُ مَعَ الضَّمِيرِ.",
        "The lam is a jarr letter; the attached «him» is built on damma and fills the seat of jarr — the lam takes fatha before a pronoun.",
        "Lâm cer harfi; bitişik «o» zamiri damme üzere mebnî, mahallen mecrûr («ona») — lâm zamirle fethalı okunur.",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")])
def ZARF_BADA():
    return tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.",
        "An adverb of time «after», in nasb and annexed.", "Zaman zarfı «sonra», mansûb, muzâf.")
def MA_MAWSULA(seat_ar, seat_en, seat_tr, extra):
    return tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ بِمَعْنَى «الَّذِي» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + ".",
        "A relative noun «what» (= that which), built on sukun, in the seat of " + seat_en + ".",
        "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî, mahallen " + seat_tr + ".")
def IDHA_T(full="إِذَا", note=("", "", "")):
    pre = full[:2] if full[:2] in ("وَ", "فَ") else ""
    head = {"وَ": (WA_AR, "The waw conjoins; ", "«ve» + "), "فَ": ("الْفَاءُ لِلِاسْتِئْنَافِ، وَ", "The fa opens a new sentence; ", "Fâ isti'nâf içindir; "), "": ("", "", "")}[pre]
    return tok(full, "idha", "noun", ["idha-shartiyya", "maful-fih", "huruf-al-shart-fil-kafiya"],
        head[0] + "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ غَيْرُ جَازِمٍ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ الشَّرْطِ" + note[0] + ".",
        head[1] + "إِذَا «when(ever)»: an adverb of time carrying the sense of a condition, which governs no jazm; built on sukun in the seat of nasb, annexed to the condition's clause" + note[1] + ".",
        head[2] + "İzâ «-dığı zaman»: şart mânâsı taşıyan, cezm etmeyen zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf" + note[2] + ".",
        segments=[seg(pre, "wa" if pre == "وَ" else "fa", "conj"), seg("إِذَا", "idha", "noun")] if pre else None)
def WA_FI(istinaf=False):
    a = ("الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "The waw opens a new sentence; ", "Vâv isti'nâf içindir; ") if istinaf else (WA_AR, "The waw conjoins; ", "«ve» + ")
    return tok("وَفِي", "fi", "prep", ["huruf-jarr"], a[0] + "فِي حَرْفُ جَرٍّ.", a[1] + "فِي «in» is a jarr letter.", a[2] + "fî «-de» — cer harfi.",
        segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")])
def BADAL_OF(full, lex, case, of_ar, of_en, of_tr, extra=None, punct=None):
    sign = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr", "mecrûr")}[case]
    return tok(full, lex, "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"] + (extra or []),
        "بَدَلٌ مِنْ «" + of_ar + "» " + sign[0] + ".", "A badal of «" + of_en + "», in " + sign[1] + " like it.", "«" + of_tr + "»den bedel, " + sign[2] + ".", punct=punct)

TITLES = [{"ar": "شَابٌّ فِي الْبَصْرَةِ", "en": "A young man in Basra", "tr": "Basra'da bir genç"},
          {"ar": "الْخَطَأُ", "en": "The slip", "tr": "Hata"},
          {"ar": "عِنْدَ الْخَلِيلِ", "en": "With al-Khalīl", "tr": "Halîl'in yanında"},
          {"ar": "الْكِتَابُ", "en": "The Book", "tr": "Kitap"},
          {"ar": "النَّحْوُ وَالْمَعْنَى", "en": "Grammar and meaning", "tr": "Nahiv ve mânâ"}]

# =========================================== Chapter 1 — شَابٌّ فِي الْبَصْرَةِ ===========================================
S1 = []
S1.append({"id": "s1", "translation": {"en": "Sībawayh was a young man whose family came from Persia.", "tr": "Sîbeveyh, aslı Fâris (İran) diyarından olan bir gençti."},
 "tokens": [KANA("كَانَ"), SIB("ismk"), KHK("شَابًّا", "shabb"),
  ENC_NOUN("أَصْلُهُ", "asl", "هُ", "mubtada", ["jumla-sifa"], note_ar=NAAT_OF("nasb", "شَابًّا", "a young man", "genç")[0], note_en=NAAT_OF("nasb", "شَابًّا", "a young man", "genç")[1], note_tr=NAAT_OF("nasb", "شَابًّا", "a young man", "genç")[2]),
  MIN(),
  MAJR("فَارِسَ", "faris-persia", "propn", DIPT_G, sign=FATHA_JARR, punct=".",
    note_ar="، عَلَمٌ عَلَى بِلَادٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ",
    note_en=" — a foreign name of a land, barred from tanwin, so the fatha stands for the kasra; the jarr phrase is the predicate of «his origin», in the seat of raf'",
    note_tr=" — yabancı bir ülke adı, gayr-i munsarif; kesre yerine fetha ile mecrûr — câr-mecrûr «aslı»nın haberi, mahallen merfû")]})

S1.append({"id": "s2", "translation": {"en": "His name was ʿAmr ibn ʿUthmān, and Sībawayh was his byname.", "tr": "Adı Amr b. Osman'dı; Sîbeveyh ise lakabıydı."},
 "tokens": [tok("وَاسْمُهُ", "ism-name", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَاسْمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The waw opens a new sentence; «name» is the mubtada, in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr.",
    "Vâv isti'nâf içindir; «isim» mübtedâ, merfû, muzâf; bitişik zamir muzâfun ileyh, mahallen mecrûr.",
    segments=[seg("وَ", "wa", "conj"), seg("اسْمُ", "ism-name", "noun"), seg("هُ", "pron-3ms", "pron")]),
  KHABAR("عَمْرُو", "amr-name", note_ar=IBN_DROP[0] + "، وَالْوَاوُ تُكْتَبُ وَلَا تُنْطَقُ فَرْقًا بَيْنَهُ وَبَيْنَ عُمَرَ",
    note_en=IBN_DROP[1] + "; the waw is written, not spoken, to tell it from ʿUmar", note_tr=IBN_DROP[2] + "; vâv Ömer'den ayırmak için yazılır, okunmaz"),
  tok("بْنُ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«عَمْرُو» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
    "An adjective (na't) of «ʿAmr», in raf' and annexed — its alif is dropped in writing because it stands between two names.", "«Amr»ın na'tı, merfû, muzâf — iki alem arasında geldiği için elifi yazıda düşer."),
  MUDAF_ILAYH("عُثْمَانَ", "uthman", "propn", DIPT_G2, sign=FATHA_JARR, punct="،",
    note_ar="، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", note_en=" — a name barred from tanwin (a name ending in an added alif and nun), so the fatha stands for the kasra",
    note_tr=" — alemiyet ve zâid elif-nûn sebebiyle gayr-i munsarif; kesre yerine fetha ile mecrûr"),
  SIB("mubtada", pre="wa"),
  tok("لَقَبُهُ", "laqab", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"],
    "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The predicate (khabar), in raf' and annexed; the attached «his» is the second term of the idafa, in the seat of jarr.",
    "Haber, merfû, muzâf; bitişik zamir muzâfun ileyh, mahallen mecrûr.", punct=".",
    segments=[seg("لَقَبُ", "laqab", "noun"), seg("هُ", "pron-3ms", "pron")])]})

S1.append({"id": "s3", "translation": {"en": "He came to Basra in his youth, seeking knowledge.", "tr": "Gençliğinde, ilim talep ederek Basra'ya geldi."},
 "tokens": [MADI("وَقَدِمَ", "qadima", hidden=True),
  MAFUL("الْبَصْرَةَ", "basra", "propn", note_ar=" — وَ«قَدِمَ» يَتَعَدَّى إِلَى الْبَلَدِ الَّذِي يَأْتِيهِ", note_en=" — «came» takes the town it comes to as its object", note_tr=" — «geldi» fiili vardığı şehri mef'ûl alır"),
  FI(), ENC_NOUN("شَبَابِهِ", "shabab", "هِ", "majr"),
  MUDARI("يَطْلُبُ", "talaba", ["hal", "al-hal-jumla-wa-rabituha"], note_ar=HAL_CL[0] + " مِنَ الْفَاعِلِ", note_en=HAL_CL[1] + " of the doer", note_tr=HAL_CL[2] + " (fâilden)"),
  MAFUL("الْعِلْمَ", "ilm", punct=".")]})

S1.append({"id": "s4", "translation": {"en": "Basra in that age was a city of learning, and in its mosques there were many circles of scholars.",
                                      "tr": "Basra o zamanda bir ilim şehriydi; mescitlerinde âlimlerin pek çok halkası vardı."},
 "tokens": [KANAT_K("وَكَانَتِ"), ISMK("الْبَصْرَةُ", "basra", "propn"), FI(),
  DHALIKA("جَرٍّ", "jarr", "mecrûr"), BADAL_OF("الزَّمَانِ", "zaman", "jarr", "ذٰلِكَ", "that", "o"),
  KHK("مَدِينَةَ", "madina", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("عِلْمٍ", "ilm", punct="،"),
  WA_FI(),
  ENC_NOUN("مَسَاجِدِهَا", "masjid", "هَا", "majr", ["jam-taksir"],
    note_ar=" — جَمْعُ مَسْجِدٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ",
    note_en=" — the plural of مَسْجِد on the farthest-plural pattern, in jarr by the kasra because it is annexed; the jarr phrase is the FRONTED predicate, in the seat of raf'",
    note_tr=" — mescid'in müntehe'l-cumû' vezninde cem'i, muzâf olduğu için kesre ile mecrûr; câr-mecrûr öne alınmış haber, mahallen merfû"),
  MUBTADA("حَلَقَاتٌ", "halqa", extra=["jam-muannath-salim"],
    note_ar=" — مُؤَخَّرٌ، جَمْعُ حَلْقَةٍ جَمْعَ مُؤَنَّثٍ سَالِمًا؛ وَجَازَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ شِبْهِ الْجُمْلَةِ",
    note_en=" — placed after its predicate; the sound feminine plural of حَلْقَة; an indefinite mubtada is allowed because the jarr-phrase predicate comes first",
    note_tr=" — haberinden sonraya bırakılmış; halka'nın cem-i müennes sâlimi; câr-mecrûr haber öne geçtiği için nekire mübtedâ caizdir"),
  NAAT("كَثِيرَةٌ", "kathir"),
  LI_AL("لِلْعُلَمَاءِ", "alim-scholar", "الْعُلَمَاءِ", extra=["jam-taksir"], punct=".",
    note_ar=" — جَمْعُ عَالِمٍ عَلَى فُعَلَاءَ" + JAR_NAAT("raf", "حَلَقَاتٌ", "circles", "halkalar", True)[0],
    note_en=" — the plural of عَالِم on فُعَلَاء" + JAR_NAAT("raf", "حَلَقَاتٌ", "circles", "halkalar", True)[1],
    note_tr=" — âlim'in fuʿalâ' veznindeki cem'i" + JAR_NAAT("raf", "حَلَقَاتٌ", "circles", "halkalar", True)[2])]})

S1.append({"id": "s5", "translation": {"en": "He sat in the circle of Ḥammād ibn Salama, writing ḥadīth from him; and Ḥammād was one of the imams of ḥadīth.",
                                      "tr": "Hammâd b. Seleme'nin halkasına oturdu, ondan hadis yazıyordu; Hammâd da hadis imamlarından biriydi."},
 "tokens": [MADI("فَجَلَسَ", "jalasa", hidden=True), FI(),
  MAJR("حَلْقَةِ", "halqa", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("حَمَّادِ", "hammad-name", "propn", note_ar=IBN_DROP[0], note_en=IBN_DROP[1], note_tr=IBN_DROP[2]),
  tok("بْنِ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«حَمَّادِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
    "An adjective (na't) of «Ḥammād», in jarr and annexed — its alif is dropped in writing because it stands between two names.", "«Hammâd»ın na'tı, mecrûr, muzâf — iki alem arasında geldiği için elifi yazıda düşer."),
  MUDAF_ILAYH("سَلَمَةَ", "salama-name", "propn", DIPT_G2, sign=FATHA_JARR,
    note_ar="، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ", note_en=" — a name barred from tanwin (a name with the feminine ta), so the fatha stands for the kasra",
    note_tr=" — alemiyet ve lafzî te'nîs sebebiyle gayr-i munsarif; kesre yerine fetha ile mecrûr"),
  MUDARI("يَكْتُبُ", "kataba", ["hal", "al-hal-jumla-wa-rabituha"], note_ar=HAL_CL[0] + " مِنَ الْفَاعِلِ", note_en=HAL_CL[1] + " of the doer", note_tr=HAL_CL[2] + " (fâilden)"),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)"),
  MAFUL("الْحَدِيثَ", "hadith", punct="،"),
  KANA("وَكَانَ"), ISMK("حَمَّادٌ", "hammad-name", "propn"), KHK("إِمَامًا", "imam"), MIN(),
  MAJR("أَئِمَّةِ", "imam", extra=["jam-taksir", "idafa-definiteness"],
    note_ar="، مُضَافٌ — جَمْعُ إِمَامٍ" + JAR_NAAT("nasb", "إِمَامًا", "an imam", "imam")[0],
    note_en=", annexed — the plural of إِمَام" + JAR_NAAT("nasb", "إِمَامًا", "an imam", "imam")[1],
    note_tr=", muzâf — imam'ın cem'i" + JAR_NAAT("nasb", "إِمَامًا", "an imam", "imam")[2]),
  MUDAF_ILAYH("الْحَدِيثِ", "hadith", punct=".")]})

# ================================================= Chapter 2 — الْخَطَأُ =================================================
S2 = []
S2.append({"id": "s1", "translation": {"en": "One day Sībawayh was reading a ḥadīth aloud to his shaykh.", "tr": "Günlerden bir gün Sîbeveyh hocasına bir hadis okuyordu."},
 "tokens": [WA_FI(istinaf=True),
  MAJR("يَوْمٍ", "yawm", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَقْرَأُ»", note_en=" — the jarr phrase attaches to «was reading»", note_tr=" — câr-mecrûr «okuyordu»ya müteallik"),
  MINA(),
  MAJR("الْأَيَّامِ", "yawm", extra=["jam-taksir"], note_ar=" — جَمْعُ يَوْمٍ" + JAR_NAAT("jarr", "يَوْمٍ", "a day", "gün")[0],
    note_en=" — the plural of يَوْم" + JAR_NAAT("jarr", "يَوْمٍ", "a day", "gün")[1], note_tr=" — yevm'in cem'i" + JAR_NAAT("jarr", "يَوْمٍ", "a day", "gün")[2]),
  KANA("كَانَ"), SIB("ismk"),
  MUDARI("يَقْرَأُ", "qaraa", ["kana-wa-akhawatuha"], note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  MAFUL("حَدِيثًا", "hadith"),
  ALA(), ENC_NOUN("شَيْخِهِ", "shaykh", "هِ", "majr", punct=".", note_ar=" — وَ«قَرَأَ عَلَيْهِ»: قَرَأَ بَيْنَ يَدَيْهِ لِيَسْمَعَ مِنْهُ",
    note_en=" — «to read to (ʿalā)» a teacher: to read before him so that he hears", note_tr=" — «birine okumak»: hocanın önünde, onun duyacağı şekilde okumak")]})

S2.append({"id": "s2", "translation": {"en": "He made a mistake in the iʿrāb of one of its words.", "tr": "Onun kelimelerinden birinin i'râbında hata yaptı."},
 "tokens": [MADI_D("فَأَخْطَأَ", "akhtaa", ["form-iv-verbs"], hidden=True), FI(),
  MAJR("إِعْرَابِ", "irab", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("كَلِمَةٍ", "kalima"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", punct=".",
    note_ar="، وَالْهَاءُ عَائِدٌ عَلَى «حَدِيثًا»" + JAR_NAAT("jarr", "كَلِمَةٍ", "a word", "kelime")[0],
    note_en="; the pronoun returns to «a ḥadīth»" + JAR_NAAT("jarr", "كَلِمَةٍ", "a word", "kelime")[1],
    note_tr="; zamir «hadis»e döner" + JAR_NAAT("jarr", "كَلِمَةٍ", "a word", "kelime")[2])]})

S2.append({"id": "s3", "translation": {"en": "Ḥammād corrected him and made clear to him what was right.", "tr": "Hammâd onu düzeltti ve ona doğrusunu açıkladı."},
 "tokens": [MADI("فَرَدَّ", "radda", ["doubled-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَ«رَدَّ عَلَيْهِ»: صَحَّحَ لَهُ خَطَأَهُ",
    note_en="; its doer follows — «radda ʿalayhi»: he set him right", note_tr="; fâili ondan sonra gelir — «redde aleyhi»: onu düzeltti"),
  ALAYHI(), FAIL("حَمَّادٌ", "hammad-name", "propn", punct="،"),
  MADI_D("وَبَيَّنَ", "bayyana", ["form-ii-verbs"], hidden=True), LAHU(), MAFUL("الصَّوَابَ", "sawab", punct=".")]})

S2.append({"id": "s4", "translation": {"en": "So Sībawayh resolved to seek the science of grammar, so that he would not err in iʿrāb after that.",
                                      "tr": "Bunun üzerine Sîbeveyh, bundan sonra i'râbda hata etmemek için nahiv ilmini talep etmeye karar verdi."},
 "tokens": [MADI("فَعَزَمَ", "azama"), SIB("fail"), ALA(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِعَلَى، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«عَزَمَ»", "; the masdar it builds is in jarr after عَلَى, and the phrase attaches to «resolved»", "; kurduğu müevvel masdar alâ ile mecrûr; câr-mecrûr «karar verdi»ye müteallik"),
  MANSUB_AN("يَطْلُبَ", "talaba"),
  MAFUL("عِلْمَ", "ilm", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("النَّحْوِ", "nahw-grammar", punct="،"),
  tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
    "حَرْفُ جَرٍّ بِمَعْنَى «كَيْ» لِلتَّعْلِيلِ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «so that» is a jarr letter of purpose (= كَيْ): the present verb after it is in nasb by an أَنْ that must stay hidden, and the masdar they build is in jarr by حَتَّى.",
    "Hattâ «-sın diye»: ta'lîl için (key anlamında) cer harfi; sonraki muzâri vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr."),
  LA_NAFIYA(),
  tok("يُخْطِئَ", "akhtaa", "verb", ["nawasib-wa-jawazim-al-mudari", "form-iv-verbs"],
    "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "Present verb in nasb by an أَنْ hidden of necessity after حَتَّى, its sign the fatha; the doer is a hidden pronoun «he».",
    "Hattâ'dan sonra vücûben gizli en ile mansûb muzâri, alâmeti fetha; fâil gizli zamir «o»."),
  FI(), MAJR("الْإِعْرَابِ", "irab"), ZARF_BADA(),
  DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", punct=".", extra=["idafa-definiteness"])]})

S2.append({"id": "s5", "translation": {"en": "That small slip was a door to a great science.", "tr": "O küçük hata, büyük bir ilme açılan bir kapı oldu."},
 "tokens": [INNA(),
  ISHARA("هٰذَا", "hadha", "نَصْبٍ اسْمُ إِنَّ", "nasb as the noun of إِنَّ", "mansûb — inne'nin ismi", extra=["inna-wa-akhawatuha"]),
  BADAL_OF("الْخَطَأَ", "khata", "nasb", "هٰذَا", "this", "bu"),
  NAAT("الصَّغِيرَ", "saghir", "nasb"),
  KANA_HID("كَانَ", note=(" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi olarak mahallen merfû")),
  KHK("بَابًا", "bab"), ILA(),
  MAJR("عِلْمٍ", "ilm", note_ar=JAR_NAAT("nasb", "بَابًا", "a door", "kapı")[0], note_en=JAR_NAAT("nasb", "بَابًا", "a door", "kapı")[1], note_tr=JAR_NAAT("nasb", "بَابًا", "a door", "kapı")[2]),
  NAAT("كَبِيرٍ", "kabir", "jarr", punct=".")]})

# ============================================== Chapter 3 — عِنْدَ الْخَلِيلِ ==============================================
S3 = []
S3.append({"id": "s1", "translation": {"en": "He went to al-Khalīl ibn Aḥmad, and al-Khalīl was the most learned man of his time in Arabic.",
                                      "tr": "Halîl b. Ahmed'e gitti; Halîl, zamanının insanları içinde Arapçayı en iyi bilendi."},
 "tokens": [MADI("فَذَهَبَ", "dhahaba", hidden=True), ILA(), MAJR("الْخَلِيلِ", "khalil-name", "propn"),
  tok("بْنِ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«الْخَلِيلِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
    "An adjective (na't) of «al-Khalīl», in jarr and annexed — its alif is dropped in writing because it stands between two names.", "«Halîl»in na'tı, mecrûr, muzâf — iki alem arasında geldiği için elifi yazıda düşer."),
  MUDAF_ILAYH("أَحْمَدَ", "ahmad", "propn", DIPT_G, sign=FATHA_JARR, punct="،",
    note_ar="، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ (أَفْعَل)", note_en=" — a name barred from tanwin (a name on a verb's pattern, أَفْعَل), so the fatha stands for the kasra",
    note_tr=" — alemiyet ve fiil vezni (ef'al) sebebiyle gayr-i munsarif; kesre yerine fetha ile mecrûr"),
  KANA("وَكَانَ"), ISMK("الْخَلِيلُ", "khalil-name", "propn"),
  KHK("أَعْلَمَ", "alam-tafdil", extra=["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ", note_en=", annexed — an elative «most learned»", note_tr=", muzâf — ism-i tafdîl «en bilgili»"),
  MUDAF_ILAYH("أَهْلِ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf"),
  BI_NOUN("بِالْعَرَبِيَّةِ", "arabiyya", "الْعَرَبِيَّةِ", punct=".", note_ar="؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«أَعْلَمَ»", note_en="; the jarr phrase attaches to «most learned»", note_tr="; câr-mecrûr «en bilgili»ye müteallik")]})

S3.append({"id": "s2", "translation": {"en": "Sībawayh kept close to him for a long time, asking him questions and writing down what he heard from him.",
                                      "tr": "Sîbeveyh uzun bir zaman ondan ayrılmadı; ona sorular soruyor, ondan işittiğini yazıyordu."},
 "tokens": [ENC_MADI("فَلَزِمَهُ", "lazima", "هُ", ["thulathi-mujarrad-babs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili ondan sonra gelir"),
  SIB("fail"),
  ZARF("زَمَانًا", "zaman", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False),
  NAAT("طَوِيلًا", "tawil-long", "nasb", punct="،"),
  MUDARI("يَسْأَلُهُ", "saala", ["hal", "al-hal-jumla-wa-rabituha"], enc="هُ", note_ar=HAL_CL[0] + " مِنْ «سِيبَوَيْهِ»", note_en=HAL_CL[1] + " of «Sībawayh»", note_tr=HAL_CL[2] + " («Sîbeveyh»ten)"),
  MUDARI("وَيَكْتُبُ", "kataba", ["atf-nasaq"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ الْحَالِ", note_en="; the clause is conjoined to the hal clause", note_tr="; cümle hâl cümlesine ma'tûf"),
  MA_MAWSULA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"]),
  MUDARI("يَسْمَعُ", "samia", note_ar=SILA[0] + "، وَالْعَائِدُ ضَمِيرٌ مَحْذُوفٌ مَنْصُوبٌ بِالْفِعْلِ", note_en=SILA[1] + "; the pronoun returning to مَا, its object, is dropped", note_tr=SILA[2] + "; mevsûle dönen mef'ûl zamiri hazfedilmiştir"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", punct=".")]})

S3.append({"id": "s3", "translation": {"en": "He also learned from other scholars among the people of Basra.", "tr": "Basra ahalisinden başka âlimlerden de ilim aldı."},
 "tokens": [MADI("وَأَخَذَ", "akhadha", hidden=True), PREP("عَنْ", "an", gloss_tr="«-den»"),
  MAJR("عُلَمَاءَ", "alim-scholar", extra=["jam-taksir", "mamnu-min-sarf"], sign=FATHA_JARR,
    note_ar=" — جَمْعُ عَالِمٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", note_en=" — the plural of عَالِم on فُعَلَاء, a diptote (it ends in the long feminine alif), so the fatha stands for the kasra",
    note_tr=" — âlim'in fuʿalâ' veznindeki cem'i; memdûde te'nîs elifi sebebiyle gayr-i munsarif, kesre yerine fetha ile mecrûr"),
  tok("آخَرِينَ", "akhar", "noun", ["naat-sifa", "jam-mudhakkar-salim"], "نَعْتٌ لِـ«عُلَمَاءَ» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
    "An adjective (na't) of «scholars», in jarr by the ya — a sound masculine plural («other»).", "«Âlimler»in na'tı, cem-i müzekker sâlim olduğu için yâ ile mecrûr («başka»)."),
  MIN(), MAJR("أَهْلِ", "ahl", extra=["idafa-definiteness"], note_ar="، مُضَافٌ" + JAR_NAAT("jarr", "عُلَمَاءَ", "scholars", "âlimler", True)[0],
    note_en=", annexed" + JAR_NAAT("jarr", "عُلَمَاءَ", "scholars", "âlimler", True)[1], note_tr=", muzâf" + JAR_NAAT("jarr", "عُلَمَاءَ", "scholars", "âlimler", True)[2]),
  MUDAF_ILAYH("الْبَصْرَةِ", "basra", "propn", punct=".")]})

S3.append({"id": "s4", "translation": {"en": "Whenever he did not understand a question, he would ask al-Khalīl about it.", "tr": "Bir meseleyi anlamadığında, onu Halîl'e sorardı."},
 "tokens": [KANA_HID("وَكَانَ", note=(" — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ بَعْدَهُ فِي مَحَلِّ نَصْبٍ خَبَرُهُ، وَكَانَ مَعَ إِذَا تُفِيدُ الْعَادَةَ فِي الْمَاضِي",
    "; the conditional sentence after it is its predicate, in the seat of nasb — كَانَ with إِذَا tells a habit in the past («whenever … he would …»)",
    "; sonraki şart cümlesi haberi, mahallen mansûb — kâne, izâ ile geçmişteki âdeti bildirir")),
  IDHA_T(), LAM_JAZM(),
  JAZM_V("يَفْهَمْ", "fahima", hidden="هُوَ", note_ar=SHART_IDHA[0], note_en=SHART_IDHA[1], note_tr=SHART_IDHA[2]),
  MAFUL("مَسْأَلَةً", "masala"),
  MADI("سَأَلَ", "saala", ["idha-shartiyya"], hidden=True, note_ar=NO_SEAT_JAWAB[0], note_en=NO_SEAT_JAWAB[1], note_tr=NO_SEAT_JAWAB[2]),
  JARR_PRON("عَنْهَا", "an", "عَنْ", "هَا", " («onu, onun hakkında»)"),
  MAFUL("الْخَلِيلَ", "khalil-name", "propn", punct=".")]})

S3.append({"id": "s5", "translation": {"en": "He went on learning until he became one of the most learned of men in grammar.", "tr": "Öğrenmeye devam etti; sonunda nahvi en iyi bilen insanlardan biri oldu."},
 "tokens": [tok("فَمَا", "ma-nafiya", "part", ["la-nafiya"], FA_AR + "مَا حَرْفُ نَفْيٍ.", "The fa conjoins; مَا negates the verb after it.", "«bunun üzerine» + mâ nefiy harfi.",
    segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  ZALA(hidden=True),
  MUDARI("يَتَعَلَّمُ", "taallama", ["form-v-verbs", "kana-wa-akhawatuha"], note_ar=KH_ZALA[0], note_en=KH_ZALA[1], note_tr=KH_ZALA[2]),
  HATTA_IBT(),
  tok("صَارَ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "صَارَ «became» is a sister of كَانَ; its noun is the hidden pronoun «he».", "Sâra «oldu», kâne'nin kardeşlerinden; ismi gizli zamir «o»."),
  MIN((" لِلتَّبْعِيضِ", " of partition («one of»)", " (teb'îz için)")),
  MAJR("أَعْلَمِ", "alam-tafdil", extra=["ism-tafdil", "idafa-definiteness", "kana-wa-akhawatuha"],
    note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ جُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ",
    note_en=", annexed — an elative, taking the kasra because it is annexed; the jarr phrase is the predicate of صَارَ, in the seat of nasb",
    note_tr=", muzâf — ism-i tafdîl, muzâf olduğu için kesre ile; câr-mecrûr sâra'nın haberi, mahallen mansûb"),
  MUDAF_ILAYH("النَّاسِ", "nas"),
  BI_NOUN("بِالنَّحْوِ", "nahw-grammar", "النَّحْوِ", punct=".", note_ar="؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«أَعْلَمِ»", note_en="; the jarr phrase attaches to «most learned»", note_tr="; câr-mecrûr «en bilgili»ye müteallik")]})

# ================================================= Chapter 4 — الْكِتَابُ =================================================
S4 = []
S4.append({"id": "s1", "translation": {"en": "Then Sībawayh wrote a book on grammar, in which he gathered what he had learned.", "tr": "Sonra Sîbeveyh nahiv hakkında bir kitap yazdı; öğrendiklerini onda topladı."},
 "tokens": [THUMMA(), MADI("كَتَبَ", "kataba"), SIB("fail"), MAFUL("كِتَابًا", "kitab"), FI(),
  MAJR("النَّحْوِ", "nahw-grammar", punct="،", note_ar=JAR_NAAT("nasb", "كِتَابًا", "a book", "kitap")[0], note_en=JAR_NAAT("nasb", "كِتَابًا", "a book", "kitap")[1], note_tr=JAR_NAAT("nasb", "كِتَابًا", "a book", "kitap")[2]),
  MADI("جَمَعَ", "jamaa-gather", ["jumla-sifa"], hidden=True, note_ar=NAAT_OF("nasb", "كِتَابًا", "a book", "kitap", True)[0], note_en=NAAT_OF("nasb", "كِتَابًا", "a book", "kitap", True)[1], note_tr=NAAT_OF("nasb", "كِتَابًا", "a book", "kitap", True)[2]),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)", note_ar="، وَالْهَاءُ عَائِدٌ عَلَى «كِتَابًا»", note_en="; the pronoun returns to «a book»", note_tr="; zamir «kitap»a döner"),
  MA_MAWSULA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"]),
  ENC_MADI("تَعَلَّمَهُ", "taallama", "هُ", ["form-v-verbs"], hidden=True, punct=".",
    note_ar=SILA[0] + "، وَالْهَاءُ عَائِدٌ عَلَى «مَا»", note_en=SILA[1] + "; the pronoun returns to مَا", note_tr=SILA[2] + "; zamir «mâ»ya döner")]})

S4.append({"id": "s2", "translation": {"en": "In it he mentions his shaykh al-Khalīl very often.", "tr": "Kitabında hocası Halîl'i çok anar."},
 "tokens": [PRON_MUB("وَهُوَ", "huwa", pre="wa"),
  MUDARI("يَذْكُرُ", "dhakara", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)"),
  ENC_NOUN("شَيْخَهُ", "shaykh", "هُ", "maful"),
  BADAL_OF("الْخَلِيلَ", "khalil-name", "nasb", "شَيْخَهُ", "his shaykh", "hocası"),
  tok("كَثِيرًا", "kathir", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ، أَيْ: ذِكْرًا كَثِيرًا.",
    "Stands in for the absolute object, in nasb — the adjective of an omitted masdar («a frequent mentioning»).", "Mef'ûlün mutlakın nâibi, mansûb — hazfedilmiş masdarın sıfatı («çok anmak»).", punct=".")]})

S4.append({"id": "s3", "translation": {"en": "This book became known among the scholars by the name «al-Kitāb» («The Book»).", "tr": "Bu kitap âlimler arasında «el-Kitâb» adıyla tanındı."},
 "tokens": [MAJHUL("وَعُرِفَ", "arafa"),
  ISHARA("هٰذَا", "hadha", "رَفْعٍ نَائِبُ فَاعِلٍ", "raf' as the deputy doer", "merfû — nâib-i fâil", extra=["naib-al-fail"]),
  BADAL_OF("الْكِتَابُ", "kitab", "raf", "هٰذَا", "this", "bu"),
  ZARF("بَيْنَ", "bayna"),
  MUDAF_ILAYH("الْعُلَمَاءِ", "alim-scholar", extra=["jam-taksir"], note_ar=" — جَمْعُ عَالِمٍ", note_en=" — the plural of عَالِم", note_tr=" — âlim'in cem'i"),
  BI_NOUN("بِاسْمِ", "ism-name", "اسْمِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en="; it is annexed", note_tr="; muzâf"),
  MUDAF_ILAYH("الْكِتَابِ", "kitab", punct=".")]})

S4.append({"id": "s4", "translation": {"en": "So when «the Book» is mentioned among the people of grammar, it is the book of Sībawayh.", "tr": "Nahiv ehli arasında «Kitap» denince, o Sîbeveyh'in kitabıdır."},
 "tokens": [IDHA_T("فَإِذَا"),
  MAJHUL("ذُكِرَ", "dhakara", ["idha-shartiyya"], note_ar=SHART_IDHA[0], note_en=SHART_IDHA[1], note_tr=SHART_IDHA[2]),
  NAIB("الْكِتَابُ", "kitab"), INDA(),
  MUDAF_ILAYH("أَهْلِ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("النَّحْوِ", "nahw-grammar", punct="،"),
  tok("فَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-fa-fi-jawab-al-shart"],
    "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ جَوَابُ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The fa binds the answer of the condition (a nominal answer must take it); «it» is a detached pronoun built on fatha, in the seat of raf' as mubtada — the nominal clause answers إِذَا and has no seat.",
    "Fâ şartın cevabını bağlar (isim cümlesi olan cevap fâ alır); «o» munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû — isim cümlesi şartın cevabıdır, mahalli yoktur.",
    segments=[seg("فَ", "fa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("كِتَابُ", "kitab", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The predicate (khabar), in raf' and annexed.", "Haber, merfû, muzâf."),
  SIB("mudaf", punct=".")]})

S4.append({"id": "s5", "translation": {"en": "It is the first great book of grammar to have reached us, and the scholars still turn to it.",
                                      "tr": "O, nahiv hakkında bize ulaşan ilk büyük kitaptır; âlimler hâlâ ona başvurmaktadır."},
 "tokens": [PRON_MUB("وَهُوَ", "huwa", pre="wa"),
  KHABAR("أَوَّلُ", "awwal", ["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("كِتَابٍ", "kitab"), NAAT("كَبِيرٍ", "kabir", "jarr"), FI(),
  MAJR("النَّحْوِ", "nahw-grammar", note_ar=JAR_NAAT("jarr", "كِتَابٍ", "book", "kitap")[0], note_en=JAR_NAAT("jarr", "كِتَابٍ", "book", "kitap")[1], note_tr=JAR_NAAT("jarr", "كِتَابٍ", "book", "kitap")[2]),
  MADI("وَصَلَ", "wasala", ["mithal-verbs", "jumla-sifa"], hidden=True, note_ar=NAAT_OF("jarr", "كِتَابٍ", "book", "kitap", True)[0], note_en=NAAT_OF("jarr", "كِتَابٍ", "book", "kitap", True)[1], note_tr=NAAT_OF("jarr", "كِتَابٍ", "book", "kitap", True)[2]),
  JARR_PRON("إِلَيْنَا", "ila", "إِلَيْ", "نَا", " («bize»)", punct="،"),
  tok("وَمَا", "ma-nafiya", "part", ["la-nafiya"], WA_AR + "مَا حَرْفُ نَفْيٍ.", "The waw conjoins; مَا negates the verb after it.", "«ve» + mâ nefiy harfi.",
    segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  ZALA(),
  tok("الْعُلَمَاءُ", "alim-scholar", "noun", ["kana-wa-akhawatuha", "jam-taksir"], "اسْمُ زَالَ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ عَالِمٍ.", "The noun of زَالَ, in raf' — the plural of عَالِم.", "Zâle'nin ismi, merfû — âlim'in cem'i."),
  MUDARI5("يَرْجِعُونَ", "rajaa", ["kana-wa-akhawatuha"], role_ar=KH_ZALA[0], role_en=KH_ZALA[1], role_tr=KH_ZALA[2]),
  ILAYHI(punct=".")]})

# ============================================= Chapter 5 — النَّحْوُ وَالْمَعْنَى =============================================
S5 = []
S5.append({"id": "s1", "translation": {"en": "In this story there is a lesson for every seeker of knowledge.", "tr": "Bu hikâyede her ilim talebesi için bir ders vardır."},
 "tokens": [WA_FI(istinaf=True),
  ISHARA("هٰذِهِ", "hadhihi", "جَرٍّ", "jarr", "mecrûr", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"),
  BADAL_OF("الْقِصَّةِ", "qissa", "jarr", "هٰذِهِ", "this", "bu"),
  MUBTADA("دَرْسٌ", "dars", note_ar=" — مُؤَخَّرٌ، وَالْجَارُّ وَالْمَجْرُورُ قَبْلَهُ خَبَرٌ مُقَدَّمٌ؛ وَجَازَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ شِبْهِ الْجُمْلَةِ",
    note_en=" — placed after its predicate (the jarr phrase before it is the FRONTED predicate); an indefinite mubtada is allowed because that predicate comes first",
    note_tr=" — haberinden sonraya bırakılmış (önündeki câr-mecrûr öne alınmış haberdir); haber öne geçtiği için nekire mübtedâ caizdir"),
  tok("لِكُلِّ", "li", "prep", ["huruf-jarr", "idafa-definiteness"],
    "اللَّامُ حَرْفُ جَرٍّ، وَكُلِّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ" + JAR_NAAT("raf", "دَرْسٌ", "a lesson", "ders")[0] + ".",
    "The lam is a jarr letter; «every» after it is in jarr and annexed" + JAR_NAAT("raf", "دَرْسٌ", "a lesson", "ders")[1] + ".",
    "Lâm cer harfi; «her» mecrûr, muzâf" + JAR_NAAT("raf", "دَرْسٌ", "a lesson", "ders")[2] + ".",
    segments=[seg("لِ", "li", "prep"), seg("كُلِّ", "kull", "noun")]),
  MUDAF_ILAYH("طَالِبِ", "talib", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("عِلْمٍ", "ilm", punct=".")]})

S5.append({"id": "s2", "translation": {"en": "When the iʿrāb of a word changes, its meaning changes.", "tr": "Bir kelimenin i'râbı değişince mânâsı da değişir."},
 "tokens": [INNA(), ISM_INNA("الْكَلِمَةَ", "kalima"),
  IDHA_T(note=(" — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the condition and its answer together are the predicate of إِنَّ, in the seat of raf'", "; şart ve cevabı birlikte inne'nin haberi, mahallen merfû")),
  MADI_D("تَغَيَّرَ", "taghayyara", ["form-v-verbs", "idha-shartiyya"], note_ar=SHART_IDHA[0], note_en=SHART_IDHA[1], note_tr=SHART_IDHA[2]),
  ENC_NOUN("إِعْرَابُهَا", "irab", "هَا", "fail"),
  MADI_D("تَغَيَّرَ", "taghayyara", ["form-v-verbs", "idha-shartiyya"], note_ar=NO_SEAT_JAWAB[0], note_en=NO_SEAT_JAWAB[1], note_tr=NO_SEAT_JAWAB[2]),
  ENC_NOUN("مَعْنَاهَا", "mana", "هَا", "fail", ["ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", punct=".",
    note_ar=" — اسْمٌ مَقْصُورٌ", note_en=" — a maqṣūr noun: the damma is estimated on the alif", note_tr=" — maksûr isim: damme elif üzerinde takdîrî")]})

S5.append({"id": "s3", "translation": {"en": "If the speaker erred in iʿrāb, the hearer would understand a meaning other than the right one.",
                                      "tr": "Konuşan i'râbda hata etse, dinleyen doğru mânâdan başka bir mânâ anlardı."},
 "tokens": [tok("وَلَوْ", "law", "part", ["huruf-al-shart-fil-kafiya", "al-qasam-wal-shart-fil-kafiya"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ يَدُلُّ عَلَى امْتِنَاعِ الْجَوَابِ لِامْتِنَاعِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ.",
    "The waw opens a new sentence; the conditional لَوْ «if (it were so)» governs no jazm and marks the answer as not happening because the condition did not happen.",
    "Vâv isti'nâf içindir; lev: cezm etmeyen şart harfi; şart gerçekleşmediği için cevabın da gerçekleşmediğini bildirir.",
    segments=[seg("وَ", "wa", "conj"), seg("لَوْ", "law", "part")]),
  MADI_D("أَخْطَأَ", "akhtaa", ["form-iv-verbs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِعْلُ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ",
    note_en="; its doer follows — the clause is the condition and has no seat", note_tr="; fâili ondan sonra gelir — cümle şart cümlesidir, i'râbdan mahalli yoktur"),
  FAIL("الْمُتَكَلِّمُ", "mutakallim", extra=["ism-fail"]), FI(), MAJR("الْإِعْرَابِ", "irab"),
  tok("لَفَهِمَ", "fahima", "verb", ["thulathi-mujarrad-babs", "al-majzum-wal-shart-wal-jaza"],
    "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَفَهِمَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ جَوَابُ لَوْ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The lam opens the answer of لَوْ; «understood» is a past verb built on fatha whose doer follows — the clause answers لَوْ and has no seat.",
    "Lâm, lev'in cevabına gelmiştir; «anlardı» fetha üzere mebnî mâzî, fâili ondan sonra gelir — cümle lev'in cevabıdır, mahalli yoktur.",
    segments=[seg("لَ", "lam-jawab", "part"), seg("فَهِمَ", "fahima", "verb")]),
  FAIL("السَّامِعُ", "sami-hearer", extra=["ism-fail"]),
  MAFUL("مَعْنًى", "mana", extra=["ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ",
    note_ar=" — اسْمٌ مَقْصُورٌ مُنَوَّنٌ", note_en=" — a maqṣūr noun with tanwin: the fatha is estimated on the alif, which drops before the tanwin", note_tr=" — tenvinli maksûr isim: fetha, tenvin önünde düşen elif üzerinde takdîrî"),
  tok("غَيْرَ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«مَعْنًى» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "An adjective (na't) of «a meaning», in nasb and annexed («other than»).", "«Mânâ»nın na'tı, mansûb, muzâf («…-den başka»)."),
  MUDAF_ILAYH("الْمَعْنَى", "mana", extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — اسْمٌ مَقْصُورٌ", note_en=" — a maqṣūr noun: the kasra is estimated on the alif", note_tr=" — maksûr isim: kesre elif üzerinde takdîrî"),
  NAAT("الصَّحِيحِ", "sahih", "jarr", punct=".")]})

S5.append({"id": "s4", "translation": {"en": "So grammar guards the meaning as the wall guards the city.", "tr": "Demek ki nahiv, surun şehri koruduğu gibi mânâyı korur."},
 "tokens": [tok("فَالنَّحْوُ", "nahw-grammar", "noun", ["mubtada-khabar"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَالنَّحْوُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
    "The fa opens a new sentence (drawing the conclusion); «grammar» is the mubtada, in raf'.", "Fâ isti'nâf içindir (sonuç çıkarır); «nahiv» mübtedâ, merfû.",
    segments=[seg("فَ", "fa", "conj"), seg("النَّحْوُ", "nahw-grammar", "noun")]),
  MUDARI("يَحْفَظُ", "hafiza", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]),
  MAFUL("الْمَعْنَى", "mana", extra=["ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — اسْمٌ مَقْصُورٌ", note_en=" — a maqṣūr noun: the fatha is estimated on the alif", note_tr=" — maksûr isim: fetha elif üzerinde takdîrî"),
  KAMA(),
  MUDARI_DF("يَحْفَظُ", "hafiza", note_ar=" — وَالْجُمْلَةُ صِلَةُ «مَا» الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", note_en="; the clause is the ṣila of the masdar-making مَا and has no seat", note_tr="; cümle masdariyye «mâ»nın sılasıdır, mahalli yoktur"),
  FAIL("السُّورُ", "sur-wall"), MAFUL("الْمَدِينَةَ", "madina", punct=".")]})

S5.append({"id": "s5", "translation": {"en": "That is why Sībawayh sought it: to keep safe the meaning of what he read.", "tr": "İşte bu yüzden Sîbeveyh onu talep etti: okuduğu şeyin mânâsını korumak için."},
 "tokens": [tok("وَلِذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "huruf-jarr"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ الثَّانِيَةُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«طَلَبَهُ».",
    "The waw opens a new sentence; the lam is a jarr letter of cause, and «that» is a demonstrative built on fatha in the seat of jarr (its own lam marks distance, its kaf is a particle of address) — «for that reason»; the phrase attaches to «sought it».",
    "Vâv isti'nâf içindir; lâm ta'lîl için cer harfi; «o» işaret ismi, fetha üzere mebnî, mahallen mecrûr (ikinci lâm uzaklık, kâf hitap içindir) — «bu yüzden»; câr-mecrûr «onu talep etti»ye müteallik.",
    segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  ENC_MADI("طَلَبَهُ", "talaba", "هُ", ["thulathi-mujarrad-babs"], note_ar="، وَالْفَاعِلُ بَعْدَهُ، وَالْهَاءُ عَائِدٌ عَلَى النَّحْوِ", note_en="; its doer follows, and «it» returns to grammar", note_tr="; fâili ondan sonra gelir; zamir nahve döner"),
  SIB("fail", punct="،"),
  tok("لِيَحْفَظَ", "hafiza", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari"],
    "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَيَحْفَظَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ جَوَازًا بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«طَلَبَهُ».",
    "The lam of cause («so that») is a jarr letter; «he might keep» is a present verb in nasb by an أَنْ that may stay hidden after the lam, its sign the fatha, its doer the hidden «he» — the masdar they build is in jarr by the lam, and the phrase attaches to «sought it».",
    "Lâm ta'lîl lâmıdır, cer harfi; «korusun» lâmdan sonra cevâzen gizli en ile mansûb muzâri, alâmeti fetha; fâil gizli zamir «o» — müevvel masdar lâm ile mecrûr, câr-mecrûr «talep etti»ye müteallik.",
    segments=[seg("لِ", "lam-taleel", "part"), seg("يَحْفَظَ", "hafiza", "verb")]),
  MAFUL("مَعْنَى", "mana", extra=["ism-maqsur-manqus", "idafa-definiteness"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ",
    note_ar="، مُضَافٌ — اسْمٌ مَقْصُورٌ", note_en=" — a maqṣūr noun: the fatha is estimated on the alif; annexed", note_tr=" — maksûr isim: fetha elif üzerinde takdîrî; muzâf"),
  MA_MAWSULA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"]),
  MUDARI("يَقْرَأُ", "qaraa", punct=".", note_ar=SILA[0] + "، وَالْعَائِدُ ضَمِيرٌ مَحْذُوفٌ مَنْصُوبٌ بِالْفِعْلِ", note_en=SILA[1] + "; the pronoun returning to مَا, its object, is dropped", note_tr=SILA[2] + "; mevsûle dönen mef'ûl zamiri hazfedilmiştir")]})

CHAPS = [S1, S2, S3, S4, S5]

# ---- the lexicon: every key by lemma identity from the shelf (the majority reading of a key wins) -------------------------
PKGS = sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
_M = {p: (json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
          if (ROOT / "content/samples" / p / "morphology.json").exists() else {}) for p in PKGS}
DIA_ = re.compile("[ً-ٰ]")
def _lemma_id(e): return DIA_.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))
# keys whose first majority holder carries a gloss written for another context — pinned to a package whose gloss is plain
FORCE = {"kitab": "al-bukhari-fi-baghdad", "hafiza": "abu-hanifa-wa-al-safina", "uthman": "al-usul-al-munifa"}
def find_entry(k):
    """(gloss entry, owning package) — the reading of the key that most packages hold; ties go to the alphabetical first"""
    holders = [(p, _G[p][k]) for p in PKGS if k in _G[p]]
    if not holders: return None, None
    votes = collections.Counter(_lemma_id(e) for p, e in holders)
    best = votes.most_common(1)[0][0]
    group = [(p, e) for p, e in holders if _lemma_id(e) == best]
    if k in FORCE:
        pinned = [(p, e) for p, e in group if p == FORCE[k]]
        assert pinned, ("FORCE package does not hold the majority reading", k, FORCE[k])
        group = pinned + [g for g in group if g[0] != FORCE[k]]
    if group[0][1].get("pos") == "verb":
        for p, e in group:
            if k in _M[p]: return e, p
    return group[0][1], group[0][0]

NEW_GLOSS = {
 "nahw-grammar": {"lemma": "نَحْو", "root": "ن ح و", "pos": "noun", "gloss": {"en": "grammar — the science by which the iʿrāb of words and the joining of a sentence are known (عِلْمُ النَّحْوِ)", "tr": "nahiv — kelimelerin i'râbının ve cümlenin kuruluşunun bilindiği ilim (ilmü'n-nahv)"}, "level": 4},
 "faris-persia": {"lemma": "فَارِس", "pos": "propn", "gloss": {"en": "Fāris — Persia, the land of the Persians (a foreign name, a diptote)", "tr": "Fâris — İran ülkesi, Farsların diyarı (yabancı isim, gayr-i munsarif)"}, "level": 4},
 "salama-name": {"lemma": "سَلَمَة", "root": "س ل م", "pos": "propn", "gloss": {"en": "Salama — a man's name (here the father of Ḥammād ibn Salama); a diptote, being a name with the feminine ta", "tr": "Seleme — erkek adı (burada Hammâd b. Seleme'nin babası); te'nîs tâ'sı taşıyan özel isim olduğu için gayr-i munsarif"}, "level": 4},
}
# keys on the shelf whose only gloss was written for another context: the lemma, root and pos are kept, the gloss is this story's
REGLOSS = {
 "hammad-name": {"en": "Ḥammād — a man's name; here Ḥammād ibn Salama, the Basran master of ḥadīth with whom Sībawayh first studied", "tr": "Hammâd — erkek adı; burada Sîbeveyh'in ilk ders aldığı Basralı hadis imamı Hammâd b. Seleme"},
 "laqab": {"en": "a byname, a title by which a person is known (pl. أَلْقَاب)", "tr": "lakap, bir kimsenin tanındığı ad (çoğ. elkâb)"},
 "halqa": {"en": "a ring, a circle; a study circle gathered round a teacher (pl. حَلَقَات)", "tr": "halka; bir hocanın etrafında toplanan ders halkası (çoğ. halakât)"},
}
for k in NEW_GLOSS:
    hit = [p for p in PKGS if k in _G[p]]
    assert not hit, ("a key is a global claim — already taken", k, hit)
used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, ORIGIN, missing = {}, {}, []
for k in sorted(used):
    if k in NEW_GLOSS:
        GLOSS[k] = NEW_GLOSS[k]; continue
    e, p = find_entry(k)
    if e is None: missing.append(k)
    else:
        GLOSS[k], ORIGIN[k] = dict(e), p
        if k in REGLOSS: GLOSS[k]["gloss"] = REGLOSS[k]
assert not missing, missing
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    if k in ORIGIN and k in _M[ORIGIN[k]]: MORPH["verbs"][k] = _M[ORIGIN[k]][k]
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "سِيبَوَيْهِ فِي الْبَصْرَةِ", "en": "Sībawayh in Basra", "tr": "Sîbeveyh Basra'da"},
 "subtitle": {"ar": "شَابٌّ يُخْطِئُ فِي إِعْرَابِ كَلِمَةٍ، فَيَطْلُبُ عِلْمَ النَّحْوِ حَتَّى يَكْتُبَ فِيهِ «الْكِتَابَ» — قِصَّةٌ لِلْمُسْتَوَى الرَّابِعِ",
              "en": "A young man errs in the iʿrāb of a word, and seeks the science of grammar until he writes «the Book» on it — a story for the fourth level",
              "tr": "Bir kelimenin i'râbında hata eden bir genç, nahiv ilmini talep eder ve sonunda onda «el-Kitâb»ı yazar — dördüncü seviye için bir hikâye"},
 "level": 4,
 "levelName": "Upper Intermediate",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُتَدَرِّجَةٌ (الْمُسْتَوَى الرَّابِعُ) لِخَبَرِ سِيبَوَيْهِ: قُدُومِهِ الْبَصْرَةَ شَابًّا وَجُلُوسِهِ فِي حَلْقَةِ حَمَّادِ بْنِ سَلَمَةَ، وَخَطَئِهِ فِي إِعْرَابِ كَلِمَةٍ، وَعَزْمِهِ عَلَى طَلَبِ النَّحْوِ، وَلُزُومِهِ الْخَلِيلَ بْنَ أَحْمَدَ، وَتَأْلِيفِهِ «الْكِتَابَ» — كَمَا يَرْوِيهِ الزُّبَيْدِيُّ فِي «طَبَقَاتِ النَّحْوِيِّينَ وَاللُّغَوِيِّينَ»، وَالسِّيرَافِيُّ فِي «أَخْبَارِ النَّحْوِيِّينَ الْبَصْرِيِّينَ». النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ مَصْدَرٍ، وَلَا آيَةٌ وَلَا نَصُّ حَدِيثٍ؛ وَلَمْ تُذْكَرْ أَلْفَاظُ الْخَطَأِ لِاخْتِلَافِ الرِّوَايَاتِ فِيهَا، وَعَزْمُهُ مَحْكِيٌّ بِالْمَعْنَى لَا بِلَفْظٍ مَرْوِيٍّ، وَتُرِكَتْ مُنَاظَرَتُهُ مَعَ الْكِسَائِيِّ بِبَغْدَادَ لِلْخِلَافِ فِي تَفَاصِيلِهَا.",
  "en": "ORIGINAL Level-4 graded Arabic: how Sībawayh came to Basra as a young man and sat in the ḥadīth circle of Ḥammād ibn Salama, erred in the iʿrāb of a word while reading and was corrected, resolved to learn grammar, kept close to al-Khalīl ibn Aḥmad (and learned from other Basran scholars), and wrote the book the grammarians call simply «al-Kitāb» — the well-attested core of the report as the ṭabaqāt books give it (al-Zubaydī, Ṭabaqāt al-naḥwiyyīn wa-l-lughawiyyīn; al-Sīrāfī, Akhbār al-naḥwiyyīn al-baṣriyyīn), RETOLD FREELY in the wording of a graded reader. No sentence is a quotation of a source; no verse and no ḥadīth text is quoted. The words of the slip are reported in varying forms, so they are not given: the story says only that he erred in the iʿrāb of a word and was corrected. His resolve is told in narration, not as a recorded saying, and no words are put in his or Ḥammād's mouth. The later debate with al-Kisāʾī in Baghdad (al-masʾala al-zunbūriyya) is left out, its details being disputed. The closing chapter on grammar and meaning is the project's own reflection.",
  "tr": "ÖZGÜN 4. seviye kademeli Arapça: Sîbeveyh'in genç yaşta Basra'ya gelip Hammâd b. Seleme'nin hadis halkasına oturması, okurken bir kelimenin i'râbında hata edip düzeltilmesi, nahiv öğrenmeye karar vermesi, Halîl b. Ahmed'in yanından ayrılmaması (ve Basra'nın başka âlimlerinden de ders alması) ve nahivcilerin kısaca «el-Kitâb» dediği eseri yazması — tabakāt kitaplarının (Zübeydî, Tabakātü'n-nahviyyîn ve'l-lugaviyyîn; Sîrâfî, Ahbârü'n-nahviyyîne'l-Basriyyîn) verdiği sağlam çekirdek, kademeli okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir kaynaktan alıntı değildir; hiçbir âyet ve hiçbir hadis metni aktarılmamıştır. Hatanın lafzı rivayetlerde farklı geldiği için verilmemiştir: hikâye yalnızca bir kelimenin i'râbında hata ettiğini ve düzeltildiğini söyler. Kararı rivayet edilmiş bir söz olarak değil, anlatı olarak verilmiştir; ne onun ne Hammâd'ın ağzına söz konmuştur. Bağdat'ta Kisâî ile yaptığı münazara (el-mes'eletü'z-zünbûriyye), ayrıntıları ihtilaflı olduğu için anlatılmamıştır. Nahiv ve mânâ üzerine son bölüm, projenin kendi değerlendirmesidir.",
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
