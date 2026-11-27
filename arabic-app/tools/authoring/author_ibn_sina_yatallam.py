"""Author content/samples/ibn-sina-yatallam — «ابْنُ سِينَا يَتَعَلَّمُ», an ORIGINAL historical story at Level 4 (Upper Intermediate).

ORIGINAL graded Arabic: the education of Ibn Sīnā as he tells it in his own autobiography (al-Sīra, transmitted by his student
Abū ʿUbayd al-Jūzjānī and carried by Ibn Abī Uṣaybiʿa in ʿUyūn al-anbāʾ fī ṭabaqāt al-aṭibbāʾ). He is born in a village near
Bukhārā and brought to the city as a small boy; he reads the Qurʾān and adab with teachers and knows the Qurʾān by heart
while still young; he studies fiqh, then logic with a man who comes to Bukhārā, and his teacher marvels at him. He turns to
medicine, finds it easy, sees physicians come to learn from him while still young, and treats the sick. He gives himself to philosophy,
going to the mosque to pray when a question defeats him; he reads the Metaphysics forty times, knows it by heart and still
does not grasp its aim, and despairs of it. In the book market he buys, almost against his will, a cheap book of al-Fārābī
on the aims of the Metaphysics, and its meaning opens to him; the next day he gives much to the poor in thanks to God. The
emir of Bukhārā, Nūḥ ibn Manṣūr, falls gravely ill; Ibn Sīnā, whose name is already known, is summoned, treats him with the
physicians, and is given leave to enter the emir's library, where he reads books he had never seen. The chapter order
follows al-Sīra (medicine comes before the Metaphysics there). The exact ages vary in the reports, so the story says only
«while still young» (صَغِيرًا، وَهُوَ صَبِيٌّ، وَهُوَ شَابٌّ); the one number kept is the «forty times» of the reading. Nothing is
quoted and no words are put in his mouth: every step is narration. Aristotle is not named in the Arabic (the vowels of his
name are not on the shelf); the book is called by its Arabic title كِتَابُ مَا بَعْدَ الطَّبِيعَةِ and «a book of the Greeks».

Five chapters, twenty-six sentences, in the Level-4 register: كَانَ with a hidden noun and a verbal khabar, كَانَ + قَدْ + past
(the pluperfect), صَارَ with a verbal khabar, كَانَ with a conditional khabar (إِذَا of habit), لٰكِنَّ / أَنَّ / لِأَنَّ with their
nouns and clause predicates, the ḥāl as a word (صَغِيرًا) and as a clause (وَهُوَ صَبِيٌّ، يَشْكُرُ اللهَ), the passive (وُلِدَ،
دُعِيَ), وَجَدَ and ظَنَّ as verbs of the heart, لَنْ + subjunctive with أَبَدًا, لَمْ + jussive (يَفْهَمْ، يَرَهَا with the dropped
weak letter), the fronted jarr khabar before an indefinite mubtadaʾ, the maqṣūr diptote names سِينَا and بُخَارَى, the forty of
a count with its tamyīz, and قَبْلُ cut from annexation. Written on the authoring kit (story_kit.py). Four entries are new — the
names سِينَا (`sina`), بُخَارَى (`bukhara`; spelled as the shelf spells it in the nisba notes of al-bukhari-fi-baghdad), الْفَارَابِيّ
(`farabi`) and the man's name مَنْصُور (`mansur-name`; the shelf's `mansur` is the participle). No verb is new: every paradigm is
copied from a package that already owns the verb. Regenerate with:
python3 tools/authoring/author_ibn_sina_yatallam.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "ibn-sina-yatallam"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"نَا": "pron-1p", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms"})
PRON_AR.update({"نَا": "نَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ"})

# ---- the clause seats and short notes ------------------------------------------------------------------------------------
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
DOER_AFTER = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
NO_SEAT_JAWAB = (" — جَوَابُ الشَّرْطِ، وَالْجُمْلَةُ لَا مَحَلَّ لَهَا لِأَنَّهَا جَوَابُ شَرْطٍ غَيْرِ جَازِمٍ",
                 " — the answer of the condition; its clause has no seat, being the answer of a condition that governs no jazm",
                 " — şartın cevabı; cezm etmeyen şartın cevabı olduğu için cümlenin i'râbdan mahalli yoktur")
SHART_IDHA = (" — فِعْلُ الشَّرْطِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا",
              " — the condition's verb; its clause is in the seat of jarr, annexed to إِذَا",
              " — şart fiili; cümlesi izâ'ya muzâfun ileyh olarak mahallen mecrûr")
IBN_DROP = (" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ مَوْصُوفٌ بِـ«ابْنٍ» مُضَافٍ إِلَى عَلَمٍ",
            " — it loses its tanwin because it is described by «ibn» annexed to a name",
            " — alem'e muzâf «ibn» ile vasıflandığı için tenvini düşmüştür")
KH_ANNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
KH_SARA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ", "; the clause fills the seat of nasb as the predicate of صَارَ", "; cümle sâra'nın haberi olarak mahallen mansûb")
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
def ATTACH(of_ar, of_en, of_tr):
    return ("؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«" + of_ar + "»", "; the jarr phrase attaches to «" + of_en + "»", "; câr-mecrûr «" + of_tr + "»e müteallik")

# ---- the names: two maqṣūr diptotes, a nisba and a name ---------------------------------------------------------------
DIPT_G = ["mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"]
SINA_N = ("، وَسِينَا عَلَمٌ أَعْجَمِيٌّ مَقْصُورٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ، فَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ، مُقَدَّرَةً عَلَى الْأَلِفِ لِلتَّعَذُّرِ",
          " — سِينَا is a foreign maqṣūr name barred from tanwin (a name and foreign): its sign of jarr is the fatha standing for the kasra, estimated on the alif",
          " — Sînâ yabancı ve maksûr bir özel isimdir; alemiyet ve ucmet sebebiyle gayr-i munsarif: cer alâmeti kesre yerine fethadır ve elif üzerinde takdîrîdir")
def SINA(punct=None):
    return tok("سِينَا", "sina", "propn", ["idafa-definiteness", "ism-maqsur-manqus"] + DIPT_G,
        "مُضَافٌ إِلَيْهِ مَجْرُورٌ" + SINA_N[0] + ".", "The second term of the idafa, in jarr" + SINA_N[1] + ".", "Muzâfun ileyh, mecrûr" + SINA_N[2] + ".", punct=punct)
def IBN(role, punct=None):
    """ابْنُ سِينَا — «ibn» carries the case of its seat, سِينَا is annexed to it"""
    r = {"naib": ("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ", "The deputy doer (na'ib al-fa'il), in raf'", "Nâib-i fâil, merfû", "naib-al-fail"),
         "fail": ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "The doer (fa'il), in raf'", "Fâil, merfû", "fail"),
         "mudaf": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", "idafa-definiteness")}[role]
    full = {"naib": "ابْنُ", "fail": "ابْنُ", "mudaf": "ابْنِ"}[role]
    return [tok(full, "ibn", "noun", [r[3], "idafa-definiteness"], r[0] + "، مُضَافٌ.", r[1] + ", annexed.", r[2] + ", muzâf."), SINA(punct)]
BUKH_N = ("، وَهُوَ عَلَمٌ عَلَى بَلَدٍ، مَقْصُورٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ",
          " — the name of a city, a maqṣūr diptote (a name and foreign)",
          " — bir şehir adı; alemiyet ve ucmet sebebiyle gayr-i munsarif maksûr isim")
def BUKHARA(role, punct=None, note=("", "", "")):
    r = {"majr": ("مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ، مُقَدَّرَةً عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "In jarr after the letter: the fatha stands for the kasra, estimated on the alif", "Cer harfiyle mecrûr: kesre yerine fetha, elif üzerinde takdîrî", "huruf-jarr"),
         "mudaf": ("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ، مُقَدَّرَةً عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "The second term of the idafa, in jarr: the fatha stands for the kasra, estimated on the alif", "Muzâfun ileyh, mecrûr: kesre yerine fetha, elif üzerinde takdîrî", "idafa-definiteness"),
         "maful": ("مَفْعُولٌ بِهِ مُقَدَّمٌ عَلَى الْفَاعِلِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "The direct object, placed before the doer, in nasb by a fatha estimated on the alif", "Fâilden önce gelen mef'ûlün bih, elif üzerinde takdîrî fetha ile mansûb", "maful-bihi")}[role]
    return tok("بُخَارَى", "bukhara", "propn", [r[3], "ism-maqsur-manqus"] + DIPT_G,
        r[0] + BUKH_N[0] + note[0] + ".", r[1] + BUKH_N[1] + note[1] + ".", r[2] + BUKH_N[2] + note[2] + ".", punct=punct)

# ---- the verb and particle shapes the kit does not carry -----------------------------------------------------------------
def MADI_D(full, lex, extra=None, hidden=False, punct=None, note_ar="", note_en="", note_tr=""):
    """a past verb of a DERIVED form (انْتَقَلَ، أَقْبَلَ، تَعَلَّمَ) — MADI without the mujarrad-bāb anchor"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", extra or [],
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ" + hid + note_ar + ".",
        en0 + "past verb built on fatha" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "fetha üzere mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def MADI_DA(full, lex, extra=None, hidden=True, punct=None, note_ar="", note_en="", note_tr=""):
    """صَلَّى، أَعْطَى: a past verb of a derived form ending in alif, built on an estimated fatha"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    hid = "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" if hidden else ""
    return tok(full, lex, "verb", ["naqis-verbs"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ" + hid + note_ar + ".",
        en0 + "past verb built on a fatha estimated on the alif" + ("; the doer is a hidden pronoun" if hidden else "") + note_en + ".",
        tr0 + "elif üzerindeki takdîrî fetha ile mebnî mâzî" + ("; fâil gizli zamirdir" if hidden else "") + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on fatha, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», fetha üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
def PREP_DHALIKA(full, head, head_lex, head_ar, head_en, head_tr, attach, punct=None):
    """لِذٰلِكَ، بِذٰلِكَ: a jarr letter with the far demonstrative"""
    return tok(full, "dhalika", "pron", ["asma-al-ishara", "huruf-jarr"],
        head_ar + "، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ، وَاللَّامُ الَّتِي فِيهِ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ" + attach[0] + ".",
        head_en + "; «that» is a demonstrative built on fatha in the seat of jarr (its own lam marks distance, its kaf is a particle of address)" + attach[1] + ".",
        head_tr + "; «o» işaret ismi, fetha üzere mebnî, mahallen mecrûr (içindeki lâm uzaklık, kâf hitap içindir)" + attach[2] + ".",
        punct=punct, segments=[seg(head, head_lex, "prep"), seg("ذٰلِكَ", "dhalika", "pron")])
def MA_MAWSULA(seat_ar, seat_en, seat_tr, extra, note=("", "", "")):
    return tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ بِمَعْنَى «الَّذِي» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + note[0] + ".",
        "A relative noun «what» (= that which), built on sukun, in the seat of " + seat_en + note[1] + ".",
        "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî, mahallen " + seat_tr + note[2] + ".")
def IDHA_T(full="إِذَا", note=("", "", "")):
    return tok(full, "idha", "noun", ["idha-shartiyya", "maful-fih", "huruf-al-shart-fil-kafiya"],
        "إِذَا ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ غَيْرُ جَازِمٍ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ الشَّرْطِ" + note[0] + ".",
        "إِذَا «when(ever)»: an adverb of time carrying the sense of a condition, which governs no jazm; built on sukun in the seat of nasb, annexed to the condition's clause" + note[1] + ".",
        "İzâ «-dığı zaman»: şart mânâsı taşıyan, cezm etmeyen zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf" + note[2] + ".")
def WA_FI(istinaf=False, note=("", "", "")):
    a = ("الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "The waw opens a new sentence; ", "Vâv isti'nâf içindir; ") if istinaf else (WA_AR, "The waw conjoins; ", "«ve» + ")
    return tok("وَفِي", "fi", "prep", ["huruf-jarr"], a[0] + "فِي حَرْفُ جَرٍّ" + note[0] + ".", a[1] + "فِي «in» is a jarr letter" + note[1] + ".", a[2] + "fî «-de» — cer harfi" + note[2] + ".",
        segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")])
def BADAL_OF(full, lex, case, of_ar, of_en, of_tr, extra=None, punct=None, pos="noun", note=("", "", "")):
    sign = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr", "mecrûr")}[case]
    return tok(full, lex, pos, ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"] + (extra or []),
        "بَدَلٌ مِنْ «" + of_ar + "» " + sign[0] + note[0] + ".", "A badal of «" + of_en + "», in " + sign[1] + " like it" + note[1] + ".", "«" + of_tr + "»den bedel, " + sign[2] + note[2] + ".", punct=punct)
def LIANNAHU_(note=("", "", "")):
    """لِأَنَّهُ (of a man): the lam of cause, أَنَّ and its attached noun «he»"""
    return tok("لِأَنَّهُ", "lianna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "huruf-jarr"],
        "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُهَا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ" + note[0] + ".",
        "The lam of cause («because») is a jarr letter; أَنَّ is the verb-like particle and the attached «he» is its noun, in the seat of nasb — the clause after it is its predicate, and the masdar they build is in jarr by the lam" + note[1] + ".",
        "Lâm ta'lîl için cer harfi; enne te'kîd ve nasb harfi, bitişik «o» zamiri ismi, mahallen mansûb — sonraki cümle haberi; müevvel masdar lâm ile mecrûr" + note[2] + ".",
        segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")])
def MA_BADA_TABIA(punct=None):
    """the Arabic title of the Metaphysics after an annexed «كِتَاب»: مَا (relative) + بَعْدَ (its ṣila's adverb) + الطَّبِيعَةِ"""
    return [MA_MAWSULA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"],
                       note=(" — وَ«مَا بَعْدَ الطَّبِيعَةِ» اسْمُ الْكِتَابِ", "; «what comes after nature» is the book's name (the Metaphysics)", " — «tabiattan sonra gelen» kitabın adıdır (Metafizik)")),
            tok("بَعْدَ", "bada", "noun", ["maful-fih", "idafa-definiteness", "ism-mawsul"],
                "ظَرْفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَشِبْهُ الْجُمْلَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةُ الْمَوْصُولِ، تَقْدِيرُهُ: مَا اسْتَقَرَّ بَعْدَ الطَّبِيعَةِ.",
                "An adverb «after», in nasb and annexed — the adverbial phrase attaches to an omitted verb that is the ṣila of مَا («what is after nature»).",
                "Zarf «sonra», mansûb, muzâf — zarf, mevsûlün sılası olan hazfedilmiş bir fiile müteallik («tabiattan sonra olan»)."),
            MUDAF_ILAYH("الطَّبِيعَةِ", "tabia", punct=punct)]
def LAHU_(punct=None):
    return tok("لَهُ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
        "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ — وَفُتِحَتِ اللَّامُ مَعَ الضَّمِيرِ.",
        "The lam is a jarr letter; the attached «him» is built on damma and fills the seat of jarr — the lam takes fatha before a pronoun.",
        "Lâm cer harfi; bitişik «o» zamiri damme üzere mebnî, mahallen mecrûr («ona») — lâm zamirle fethalı okunur.",
        punct=punct, segments=[seg("لَ", "li", "prep"), seg("هُ", "pron-3ms", "pron")])
QABLU = lambda punct=None: tok("قَبْلُ", "qablu", "noun", ["al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada", "huruf-jarr"],
    "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِـ«مِنْ»، لِأَنَّهُ قُطِعَ عَنِ الْإِضَافَةِ لَفْظًا وَنُوِيَ مَعْنَاهَا — أَيْ: مِنْ قَبْلِ ذٰلِكَ.",
    "An adverb of time «before», built on damma in the seat of jarr after مِنْ, because it is cut off from its annexation in wording while the meaning is kept («before that»).",
    "Zaman zarfı «önce», damme üzere mebnî, «min» ile mahallen mecrûr; lafzen izâfetten kesilip mânâsı niyet edildiği için («ondan önce»).", punct=punct)

TITLES = [{"ar": "صَبِيٌّ فِي بُخَارَى", "en": "A boy in Bukhārā", "tr": "Buhârâ'da bir çocuk"},
          {"ar": "الطَّبِيبُ الشَّابُّ", "en": "The young physician", "tr": "Genç hekim"},
          {"ar": "كِتَابٌ صَعْبٌ", "en": "A hard book", "tr": "Zor bir kitap"},
          {"ar": "فِي سُوقِ الْكُتُبِ", "en": "In the book market", "tr": "Kitap çarşısında"},
          {"ar": "خِزَانَةُ الْكُتُبِ", "en": "The library", "tr": "Kütüphane"}]

# =========================================== Chapter 1 — صَبِيٌّ فِي بُخَارَى ===========================================
S1 = []
S1.append({"id": "s1", "translation": {"en": "Ibn Sīnā was born in a village near Bukhārā; then his father moved with him to Bukhārā while he was a little boy.",
                                      "tr": "İbn Sînâ, Buhârâ'ya yakın bir köyde doğdu; sonra o küçük bir çocukken babası onunla birlikte oraya taşındı."},
 "tokens": [MAJHUL("وُلِدَ", "walada", ["thulathi-mujarrad-babs", "mithal-verbs"], note_ar="، وَنَائِبُ الْفَاعِلِ بَعْدَهُ", note_en="; its deputy doer follows", note_tr="; nâib-i fâili ondan sonra gelir"),
  *IBN("naib"), FI(), MAJR("قَرْيَةٍ", "qarya"), NAAT("قَرِيبَةٍ", "qarib", "jarr"), MIN(),
  BUKHARA("majr", punct="،", note=ATTACH("قَرِيبَةٍ", "near", "yakın")),
  THUMMA(),
  MADI_D("انْتَقَلَ", "intaqala", ["form-viii-verbs"], note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ: انْتَقَلَ وَهُوَ مَعَهُ", note_en=" — the ba of company: he moved with him", note_tr=" — bâ musâhabet içindir: onu yanında götürdü"),
  tok("أَبُوهُ", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"],
    "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The doer, in raf' by the waw — one of the five nouns; annexed, and the attached «his» is the second term of the idafa, in the seat of jarr.",
    "Fâil, esmâ-i hamseden olduğu için vâv ile merfû; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr.",
    segments=[seg("أَبُو", "ab", "noun"), seg("هُ", "pron-3ms", "pron")]),
  JARR_PRON("إِلَيْهَا", "ila", "إِلَيْ", "هَا", " («oraya»)", note_ar="، وَهَا عَائِدٌ عَلَى «بُخَارَى»", note_en="; «it» returns to «Bukhārā»", note_tr="; zamir «Buhârâ»ya döner"),
  WA_HUWA_HAL(), KHABAR("صَبِيٌّ", "sabi-boy"), NAAT("صَغِيرٌ", "saghir", punct=".")]})

S1.append({"id": "s2", "translation": {"en": "He read the Qurʾān with one teacher, and learned adab — language and letters — from another.",
                                      "tr": "Kur'ân'ı bir hocaya okudu, edebi (dil ve edebiyatı) da başka bir hocadan öğrendi."},
 "tokens": [MADI("وَقَرَأَ", "qaraa", hidden=True), MAFUL("الْقُرْآنَ", "quran"), ALA(),
  MAJR("مُعَلِّمٍ", "muallim", punct="،", note_ar=" — وَ«قَرَأَ عَلَيْهِ»: قَرَأَ بَيْنَ يَدَيْهِ لِيَسْمَعَ مِنْهُ", note_en=" — «to read to (ʿalā)» a teacher: to read before him so that he hears", note_tr=" — «birine okumak»: hocanın önünde, onun duyacağı şekilde okumak"),
  MADI_D("وَتَعَلَّمَ", "taallama", ["form-v-verbs"], hidden=True), MAFUL("الْأَدَبَ", "adab"), ALA(), MAJR("مُعَلِّمٍ", "muallim"),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"],
    "نَعْتٌ لِـ«مُعَلِّمٍ» مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ، لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ.",
    "An adjective (na't) of «a teacher», in jarr: the fatha stands for the kasra, because آخَر «another» is barred from tanwin (an adjective on the أَفْعَل pattern).",
    "«Hoca»nın na'tı, mecrûr: vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile.", punct=".")]})

S1.append({"id": "s3", "translation": {"en": "He learned the Qurʾān by heart while still young, and came to know much of adab.",
                                      "tr": "Kur'ân'ı küçük yaşta ezberledi ve edebden de pek çok şey öğrendi."},
 "tokens": [MADI("فَحَفِظَ", "hafiza", hidden=True, note_ar=" — وَ«حَفِظَ الْقُرْآنَ»: اسْتَظْهَرَهُ", note_en=" — «ḥafiẓa the Qurʾān»: he knew it by heart", note_tr=" — «Kur'ân'ı hıfzetti»: ezberledi"),
  MAFUL("الْقُرْآنَ", "quran"), HAL("صَغِيرًا", "saghir", punct="،", note_ar="، وَصَاحِبُ الْحَالِ الْفَاعِلُ الْمُسْتَتِرُ", note_en=" (here the hidden doer: «while young»)", note_tr=" (sahibi gizli fâildir: «küçükken»)"),
  MADI("وَعَرَفَ", "arafa", hidden=True), MAFUL("كَثِيرًا", "kathir"), MINA(),
  MAJR("الْأَدَبِ", "adab", punct=".", note_ar=JAR_NAAT("nasb", "كَثِيرًا", "much", "çok")[0], note_en=JAR_NAAT("nasb", "كَثِيرًا", "much", "çok")[1], note_tr=JAR_NAAT("nasb", "كَثِيرًا", "much", "çok")[2])]})

S1.append({"id": "s4", "translation": {"en": "Then he studied fiqh under a shaykh, one of the scholars of his town.",
                                      "tr": "Sonra fıkhı, beldesinin âlimlerinden bir şeyhin yanında okudu."},
 "tokens": [THUMMA(), MADI("دَرَسَ", "darasa", hidden=True), MAFUL("الْفِقْهَ", "fiqh"), ALA(), MAJR("شَيْخٍ", "shaykh"), MIN(),
  MAJR("عُلَمَاءِ", "alim-scholar", extra=["jam-taksir", "idafa-definiteness"],
    note_ar="، مُضَافٌ — جَمْعُ عَالِمٍ عَلَى فُعَلَاءَ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ" + JAR_NAAT("jarr", "شَيْخٍ", "a shaykh", "şeyh")[0],
    note_en=", annexed — the plural of عَالِم on فُعَلَاء; a diptote, but it takes the kasra because it is annexed" + JAR_NAAT("jarr", "شَيْخٍ", "a shaykh", "şeyh")[1],
    note_tr=", muzâf — âlim'in fuʿalâ' veznindeki cem'i; gayr-i munsarif iken muzâf olduğu için kesre ile mecrûr" + JAR_NAAT("jarr", "شَيْخٍ", "a shaykh", "şeyh")[2]),
  ENC_NOUN("بَلَدِهِ", "balad", "هِ", "mudaf", punct=".")]})

S1.append({"id": "s5", "translation": {"en": "Then a man who knew logic came to Bukhārā, and Ibn Sīnā studied it under him.",
                                      "tr": "Sonra Buhârâ'ya mantığı bilen bir adam geldi; İbn Sînâ mantığı onun yanında okudu."},
 "tokens": [THUMMA(),
  MADI("قَدِمَ", "qadima", note_ar=DOER_AFTER[0] + " — وَ«قَدِمَ» يَتَعَدَّى إِلَى الْبَلَدِ الَّذِي يَأْتِيهِ", note_en=DOER_AFTER[1] + " — «came» takes the town it comes to as its object", note_tr=DOER_AFTER[2] + " — «geldi» fiili vardığı şehri mef'ûl alır"),
  BUKHARA("maful"), FAIL("رَجُلٌ", "rajul", note_ar=" — مُؤَخَّرٌ عَنِ الْمَفْعُولِ", note_en=" — placed after the object", note_tr=" — mef'ûlden sonraya bırakılmış"),
  MUDARI("يَعْرِفُ", "arafa", ["jumla-sifa"], note_ar=NAAT_OF("raf", "رَجُلٌ", "a man", "adam")[0], note_en=NAAT_OF("raf", "رَجُلٌ", "a man", "adam")[1], note_tr=NAAT_OF("raf", "رَجُلٌ", "a man", "adam")[2]),
  MAFUL("الْمَنْطِقَ", "mantiq", punct="،"),
  ENC_MADI("فَدَرَسَهُ", "darasa", "هُ", ["thulathi-mujarrad-babs"], note_ar=DOER_AFTER[0] + "، وَالْهَاءُ عَائِدٌ عَلَى «الْمَنْطِقَ»", note_en=DOER_AFTER[1] + ", and «it» returns to logic", note_tr=DOER_AFTER[2] + "; zamir «mantık»a döner"),
  *IBN("fail"), ALAYHI(punct=".")]})

S1.append({"id": "s6", "translation": {"en": "He understood difficult questions, and his teacher marveled at him.",
                                      "tr": "Zor meseleleri anlıyordu; hocası da ona hayran kaldı."},
 "tokens": [KANA_HID("وَكَانَ"), MUDARI_KH("يَفْهَمُ", "fahima"),
  MAFUL("الْمَسَائِلَ", "masala", extra=["jam-taksir"], note_ar=" — جَمْعُ مَسْأَلَةٍ", note_en=" — the plural of مَسْأَلَة", note_tr=" — mes'ele'nin cem'i"),
  NAAT("الصَّعْبَةَ", "sab", "nasb", punct="،", note_ar=" — وَأُنِّثَ لِأَنَّ مَوْصُوفَهُ جَمْعُ تَكْسِيرٍ لِغَيْرِ الْعَاقِلِ", note_en=" — feminine singular, because it describes a broken plural of things", note_tr=" — akılsızların cem-i mükesseri vasfedildiği için müfred müennes"),
  MADI("فَعَجِبَ", "ajiba", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]), MINHU(),
  ENC_NOUN("مُعَلِّمُهُ", "muallim", "هُ", "fail", punct=".")]})

# ============================================= Chapter 2 — الطَّبِيبُ الشَّابُّ =============================================
S2 = []
S2.append({"id": "s1", "translation": {"en": "Then he came to desire the science of medicine, and read its books.", "tr": "Sonra tıp ilmine rağbet etti ve onun kitaplarını okudu."},
 "tokens": [THUMMA(), MADI("رَغِبَ", "raghiba", hidden=True), FI(), MAJR("عِلْمِ", "ilm", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الطِّبِّ", "tibb", punct="،"), MADI("فَقَرَأَ", "qaraa", hidden=True),
  ENC_NOUN("كُتُبَهُ", "kitab", "هُ", "maful", ["jam-taksir"], punct=".", note_ar=" — جَمْعُ كِتَابٍ، وَالْهَاءُ عَائِدٌ عَلَى الطِّبِّ", note_en=" — the plural of كِتَاب; «its» returns to medicine", note_tr=" — kitâb'ın cem'i; zamir tıbba döner")]})

S2.append({"id": "s2", "translation": {"en": "He learned it in a short time, because he found it easy.", "tr": "Onu kısa bir zamanda öğrendi, çünkü onu kolay buldu."},
 "tokens": [ENC_MADI("فَتَعَلَّمَهُ", "taallama", "هُ", ["form-v-verbs"], hidden=True), FI(), MAJR("وَقْتٍ", "waqt"), NAAT("قَصِيرٍ", "qasir", "jarr", punct="،"),
  LIANNAHU_(),
  ENC_MADI("وَجَدَهُ", "wajada", "هُ", ["thulathi-mujarrad-babs", "zanna-wa-akhawatuha", "mafulayn"], hidden=True,
    note_ar=" — وَهُوَ مَفْعُولُهُ الْأَوَّلُ، وَ«وَجَدَ» هُنَا مِنْ أَفْعَالِ الْقُلُوبِ يَنْصِبُ مَفْعُولَيْنِ" + KH_ANNA_CL[0],
    note_en=" — its first object: وَجَدَ «found (to be)» is here a verb of the heart taking two objects" + KH_ANNA_CL[1],
    note_tr=" — birinci mef'ûlü: vecede burada iki mef'ûl alan ef'âl-i kulûbdandır" + KH_ANNA_CL[2]),
  tok("سَهْلًا", "sahl", "noun", ["mafulayn", "zanna-wa-akhawatuha"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb («easy»).", "İkinci mef'ûlün bih, mansûb («kolay»).", punct=".")]})

S2.append({"id": "s3", "translation": {"en": "Physicians came to learn from him while he was still a young man.", "tr": "O daha genç bir adamken hekimler ondan öğrenir oldu."},
 "tokens": [SARA("وَصَارَ"),
  tok("الْأَطِبَّاءُ", "tabib", "noun", ["kana-wa-akhawatuha", "jam-taksir"], "اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ طَبِيبٍ.", "The noun of صَارَ, in raf' — the plural of طَبِيب «physician».", "Sâra'nın ismi, merfû — tabîb'in cem'i."),
  MUDARI5("يَتَعَلَّمُونَ", "taallama", ["form-v-verbs", "kana-wa-akhawatuha"], role_ar=KH_SARA_CL[0], role_en=KH_SARA_CL[1], role_tr=KH_SARA_CL[2]),
  MINHU(), WA_HUWA_HAL(), KHABAR("شَابٌّ", "shabb", punct=".")]})

S2.append({"id": "s4", "translation": {"en": "He treated the sick, and so he learned much from experience.", "tr": "Hastaları tedavi ediyordu; böylece tecrübeden pek çok ilim öğrendi."},
 "tokens": [KANA_HID("وَكَانَ"), MUDARI_KH("يُعَالِجُ", "alaja", ["form-iii-verbs"]),
  MAFUL("الْمَرْضَى", "marid", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", punct="،",
    note_ar=" — جَمْعُ مَرِيضٍ عَلَى فَعْلَى", note_en=" (the fatha is estimated on the alif) — the plural of مَرِيض on فَعْلَى", note_tr=" (fetha elif üzerinde takdîrî) — marîz'in fa'lâ veznindeki cem'i"),
  MADI_D("فَتَعَلَّمَ", "taallama", ["form-v-verbs"], hidden=True), MINA(), MAJR("التَّجْرِبَةِ", "tajriba"), MAFUL("عِلْمًا", "ilm"), NAAT("كَثِيرًا", "kathir", "nasb", punct=".")]})

# =============================================== Chapter 3 — كِتَابٌ صَعْبٌ ===============================================
S3 = []
S3.append({"id": "s1", "translation": {"en": "Then he gave himself to the sciences of philosophy, reading by night and by day.", "tr": "Sonra hikmet ilimlerine yöneldi; gece gündüz okuyordu."},
 "tokens": [THUMMA(), MADI_D("أَقْبَلَ", "aqbala", ["form-iv-verbs"], hidden=True), ALA(),
  MAJR("عُلُومِ", "ilm", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ عِلْمٍ", note_en=", annexed — the plural of عِلْم", note_tr=", muzâf — ilm'in cem'i"),
  MUDAF_ILAYH("الْحِكْمَةِ", "hikma", punct="،"), KANA_HID("فَكَانَ"), MUDARI_KH("يَقْرَأُ", "qaraa"), FI(), MAJR("اللَّيْلِ", "layl"),
  ATF("وَالنَّهَارِ", "nahar", case="jarr", punct=".")]})

S3.append({"id": "s2", "translation": {"en": "Whenever he could not understand a question, he would go to the mosque, pray, and call upon God.",
                                      "tr": "Bir meseleyi anlamadığında mescide gider, namaz kılar ve Allah'a dua ederdi."},
 "tokens": [KANA_HID("وَكَانَ", note=(" — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ بَعْدَهُ فِي مَحَلِّ نَصْبٍ خَبَرُهُ، وَكَانَ مَعَ إِذَا تُفِيدُ الْعَادَةَ فِي الْمَاضِي",
    "; the conditional sentence after it is its predicate, in the seat of nasb — كَانَ with إِذَا tells a habit in the past («whenever … he would …»)",
    "; sonraki şart cümlesi haberi, mahallen mansûb — kâne, izâ ile geçmişteki âdeti bildirir")),
  IDHA_T(), LAM_JAZM(),
  JAZM_V("يَفْهَمْ", "fahima", hidden="هُوَ", note_ar=SHART_IDHA[0], note_en=SHART_IDHA[1], note_tr=SHART_IDHA[2]),
  MAFUL("مَسْأَلَةً", "masala"),
  MADI("ذَهَبَ", "dhahaba", ["idha-shartiyya"], hidden=True, note_ar=NO_SEAT_JAWAB[0], note_en=NO_SEAT_JAWAB[1], note_tr=NO_SEAT_JAWAB[2]),
  ILA(), MAJR("الْمَسْجِدِ", "masjid", punct="،"),
  MADI_DA("فَصَلَّى", "salla", ["form-ii-verbs", "atf-nasaq"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جَوَابِ الشَّرْطِ", note_en="; the clause is conjoined to the answer of the condition", note_tr="; cümle şartın cevabına ma'tûf"),
  MADI_ALIF("وَدَعَا", "daa", ["atf-nasaq"], hidden=True), ALLAH_MAF(punct=".")]})

S3.append({"id": "s3", "translation": {"en": "He read the book of the Metaphysics («what comes after nature»), a book of the Greeks on philosophy.",
                                      "tr": "«Mâ ba'de't-tabîa» (Metafizik) kitabını okudu; o, Yunanlıların hikmete dair kitaplarından biridir."},
 "tokens": [MADI("وَقَرَأَ", "qaraa", hidden=True), MAFUL("كِتَابَ", "kitab", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  *MA_BADA_TABIA(punct="،"),
  tok("وَهُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، يَعُودُ عَلَى الْكِتَابِ.",
    "The waw opens a new sentence; «it» is a detached pronoun built on fatha, in the seat of raf' as mubtada, returning to the book.",
    "Vâv isti'nâf içindir; «o» munfasıl zamir, fetha üzere mebnî, mübtedâ olarak mahallen merfû; kitaba döner.",
    segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  KHABAR("كِتَابٌ", "kitab"), MIN(),
  MAJR("كُتُبِ", "kitab", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ كِتَابٍ" + JAR_NAAT("raf", "كِتَابٌ", "a book", "kitap")[0],
    note_en=", annexed — the plural of كِتَاب" + JAR_NAAT("raf", "كِتَابٌ", "a book", "kitap")[1], note_tr=", muzâf — kitâb'ın cem'i" + JAR_NAAT("raf", "كِتَابٌ", "a book", "kitap")[2]),
  MUDAF_ILAYH("الْيُونَانِ", "yunan", "propn", note_ar=" — اسْمُ أُمَّةٍ", note_en=" — the name of a nation, the Greeks", note_tr=" — bir milletin adı, Yunanlılar"),
  FI(), MAJR("الْحِكْمَةِ", "hikma", punct=".", note_ar=JAR_NAAT("jarr", "كُتُبِ", "books", "kitaplar")[0], note_en=JAR_NAAT("jarr", "كُتُبِ", "books", "kitaplar")[1], note_tr=JAR_NAAT("jarr", "كُتُبِ", "books", "kitaplar")[2])]})

S3.append({"id": "s4", "translation": {"en": "He read it forty times, until he knew it by heart; but he did not understand its aim.",
                                      "tr": "Onu kırk kere okudu, sonunda ezberledi; fakat maksadını anlamadı."},
 "tokens": [ENC_MADI("فَقَرَأَهُ", "qaraa", "هُ", ["thulathi-mujarrad-babs"], hidden=True),
  tok("أَرْبَعِينَ", "arbaun", "noun", ["maful-mutlaq", "jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"],
    "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — يُبَيِّنُ عَدَدَ الْقِرَاءَةِ.",
    "Stands in for the absolute object, in nasb by the ya — the tens decline like the sound masculine plural; it counts the readings.",
    "Mef'ûlün mutlakın nâibi, cem-i müzekker sâlime mülhak olduğu için yâ ile mansûb — okumanın sayısını bildirir."),
  tok("مَرَّةً", "marra-once", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"], "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ الْمَعْدُودَ بَعْدَ الْعَدَدِ.",
    "A specifier (tamyiz), in nasb — it names what the number counts («times»).", "Temyîz, mansûb — sayının neyi saydığını bildirir («kere»)."),
  HATTA_IBT(), ENC_MADI("حَفِظَهُ", "hafiza", "هُ", ["thulathi-mujarrad-babs"], hidden=True, punct="،"),
  tok("وَلٰكِنَّهُ", "lakinna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"],
    "الْوَاوُ عَاطِفَةٌ، وَلٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَتَوْكِيدٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُهَا.",
    "The waw conjoins; لٰكِنَّ «but», a sister of إِنَّ that corrects what came before, puts its noun in nasb: the attached «he» is its noun, in the seat of nasb — the clause after it is its predicate, in the seat of raf'.",
    "«ve» + lâkinne: istidrâk (düzeltme) bildiren, inne'nin kardeşi; bitişik «o» zamiri ismi, mahallen mansûb — sonraki cümle haberi, mahallen merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("هُ", "pron-3ms", "pron")]),
  LAM_JAZM(),
  JAZM_V("يَفْهَمْ", "fahima", hidden="هُوَ", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ", note_en="; the clause fills the seat of raf' as the predicate of لٰكِنَّ", note_tr="; cümle lâkinne'nin haberi olarak mahallen merfû"),
  ENC_NOUN("غَرَضَهُ", "gharad", "هُ", "maful", punct=".")]})

S3.append({"id": "s5", "translation": {"en": "He grieved at that, and thought that he would never understand it.", "tr": "Buna üzüldü ve onu asla anlayamayacağını sandı."},
 "tokens": [MADI("فَحَزِنَ", "hazina", hidden=True),
  PREP_DHALIKA("لِذٰلِكَ", "لِ", "li", "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ", "The lam is a jarr letter of cause («because of»)", "Lâm ta'lîl için cer harfi («bu yüzden»)",
    ATTACH("حَزِنَ", "grieved", "üzüldü"), punct="،"),
  MADI("وَظَنَّ", "zanna", ["doubled-verbs", "zanna-wa-akhawatuha"], hidden=True,
    note_ar=" — وَأَنَّ وَمَعْمُولَاهَا سَدَّتْ مَسَدَّ مَفْعُولَيْهِ", note_en="; أَنَّ with its noun and predicate stands in place of its two objects", note_tr="; enne ve iki ma'mûlü onun iki mef'ûlünün yerini tutar"),
  ANNAHU(note=(" — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ رَفْعٍ خَبَرُهَا", "; the clause after it is its predicate, in the seat of raf'", " — sonraki cümle haberi, mahallen merfû")),
  tok("لَنْ", "lan", "part", ["nawasib-wa-jawazim-al-mudari"], "حَرْفُ نَفْيٍ وَنَصْبٍ وَاسْتِقْبَالٍ.", "لَنْ «will never»: it negates the future and puts the present verb in nasb.", "Len: istikbâli nefyeden ve muzâriyi nasbeden harf."),
  MANSUB_AN("يَفْهَمَهُ", "fahima", enc="هُ", by="لَنْ", note_ar=KH_ANNA_CL[0], note_en=KH_ANNA_CL[1], note_tr=KH_ANNA_CL[2]),
  tok("أَبَدًا", "abadan", "noun", ["maful-fih"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — لِاسْتِغْرَاقِ الْمُسْتَقْبَلِ بَعْدَ النَّفْيِ.",
    "An adverb of time in nasb — after a negation it covers all the future («ever»: «never»).", "Zaman zarfı, mansûb — nefiyden sonra bütün geleceği kapsar («asla»).", punct=".")]})

# ============================================ Chapter 4 — فِي سُوقِ الْكُتُبِ ============================================
S4 = []
S4.append({"id": "s1", "translation": {"en": "One day he passed through the book market, and a man came to him with a book he was selling.",
                                      "tr": "Bir gün kitap çarşısından geçti; bir adam ona sattığı bir kitabı getirdi."},
 "tokens": [MADI("وَمَرَّ", "marra", ["doubled-verbs"], hidden=True),
  ZARF("يَوْمًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False),
  BI_NOUN("بِسُوقِ", "suq", "سُوقِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — وَ«مَرَّ بِهِ»: اجْتَازَهُ", note_en="; it is annexed — «marra bi»: to pass by or through", note_tr="; muzâf — «merra bihî»: yanından/içinden geçti"),
  MUDAF_ILAYH("الْكُتُبِ", "kitab", extra=["jam-taksir"], punct="،", note_ar=" — جَمْعُ كِتَابٍ", note_en=" — the plural of كِتَاب", note_tr=" — kitâb'ın cem'i"),
  ENC_MADI("فَجَاءَهُ", "jaa", "هُ", ["hollow-verbs"], note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  FAIL("رَجُلٌ", "rajul"),
  BI_NOUN("بِكِتَابٍ", "kitab", "كِتَابٍ", note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ: «جَاءَهُ بِكِتَابٍ» أَتَاهُ بِهِ", note_en=" — the ba makes «came» take a thing: «came to him with a book», brought it", note_tr=" — bâ ta'diye içindir: «ona bir kitapla geldi», kitabı getirdi"),
  MUDARI("يَبِيعُهُ", "baa", ["hollow-verbs", "jumla-sifa"], enc="هُ", punct=".",
    note_ar=NAAT_OF("jarr", "كِتَابٍ", "a book", "kitap")[0] + "، وَالْهَاءُ عَائِدٌ عَلَى الْكِتَابِ", note_en=NAAT_OF("jarr", "كِتَابٍ", "a book", "kitap")[1] + "; «it» returns to the book", note_tr=NAAT_OF("jarr", "كِتَابٍ", "a book", "kitap")[2] + "; zamir kitaba döner")]})

S4.append({"id": "s2", "translation": {"en": "At first he turned it away; then he bought it, because its price was small.", "tr": "Önce onu geri çevirdi; sonra fiyatı az olduğu için onu satın aldı."},
 "tokens": [ENC_MADI("فَرَدَّهُ", "radda", "هُ", ["doubled-verbs"], hidden=True), FI(),
  MAJR("أَوَّلِ", "awwal", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْأَمْرِ", "amr", punct="،"),
  THUMMA(), ENC_MADI("اشْتَرَاهُ", "ishtara", "هُ", ["form-viii-verbs"], alif=True, hidden=True),
  tok("لِأَنَّ", "lianna", "part", ["inna-wa-akhawatuha", "huruf-jarr"],
    "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنَّ وَمَعْمُولَيْهَا مَجْرُورٌ بِاللَّامِ.",
    "The lam of cause («because») is a jarr letter; أَنَّ puts its noun in nasb and raises its predicate — the masdar built from أَنَّ and its two terms is in jarr by the lam.",
    "Lâm ta'lîl için cer harfi; enne ismini nasb, haberini ref eder — enne ve iki ma'mûlünden kurulan müevvel masdar lâm ile mecrûr.",
    segments=[seg("لِ", "li", "prep"), seg("أَنَّ", "anna", "part")]),
  tok("ثَمَنَهُ", "thaman", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"],
    "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The noun of أَنَّ, in nasb; annexed, and the attached «its» is the second term of the idafa, in the seat of jarr.",
    "Enne'nin ismi, mansûb; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr.",
    segments=[seg("ثَمَنَ", "thaman", "noun"), seg("هُ", "pron-3ms", "pron")]),
  KANA_HID("كَانَ", note=KH_ANNA_CL), KHK("قَلِيلًا", "qalil", punct=".")]})

S4.append({"id": "s3", "translation": {"en": "The book was by al-Fārābī, and in it was an explanation of the aims of the Metaphysics.",
                                      "tr": "Kitap Fârâbî'nindi; onda «Mâ ba'de't-tabîa» kitabının maksatlarının bir şerhi vardı."},
 "tokens": [KANA("وَكَانَ"), ISMK("الْكِتَابُ", "kitab"),
  tok("لِلْفَارَابِيِّ", "li", "prep", ["huruf-jarr", "kana-wa-akhawatuha"],
    "اللَّامُ حَرْفُ جَرٍّ تُفِيدُ النِّسْبَةَ، وَالْفَارَابِيِّ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
    "The lam is a jarr letter of belonging («by, of»); al-Fārābī after it is in jarr — the jarr phrase is the predicate of كَانَ, in the seat of nasb.",
    "Lâm aidiyet bildiren cer harfi; Fârâbî mecrûr — câr-mecrûr kâne'nin haberi, mahallen mansûb.", punct="،",
    segments=[seg("لِ", "li", "prep"), seg("الْفَارَابِيِّ", "farabi", "propn")]),
  tok("وَفِيهِ", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "mubtada-khabar"],
    "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.",
    "The waw conjoins; فِي is a jarr letter and the attached «it» fills the seat of jarr — the jarr phrase is the FRONTED predicate, in the seat of raf'.",
    "«ve» + fî cer harfi; bitişik zamir mahallen mecrûr — câr-mecrûr öne alınmış haber, mahallen merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  MUBTADA("شَرْحٌ", "sharh", note_ar=" — مُؤَخَّرٌ؛ وَجَازَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ شِبْهِ الْجُمْلَةِ",
    note_en=" — placed after its predicate; an indefinite mubtada is allowed because the jarr-phrase predicate comes first",
    note_tr=" — haberinden sonraya bırakılmış; câr-mecrûr haber öne geçtiği için nekire mübtedâ caizdir"),
  tok("لِأَغْرَاضِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "jam-taksir"],
    "اللَّامُ حَرْفُ جَرٍّ، وَأَغْرَاضِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — جَمْعُ غَرَضٍ عَلَى أَفْعَالٍ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«شَرْحٌ».",
    "The lam is a jarr letter; «aims» after it is in jarr and annexed — the plural of غَرَض on أَفْعَال; the jarr phrase attaches to «an explanation».",
    "Lâm cer harfi; «maksatlar» mecrûr, muzâf — garaz'ın ef'âl veznindeki cem'i; câr-mecrûr «şerh»e müteallik.",
    segments=[seg("لِ", "li", "prep"), seg("أَغْرَاضِ", "gharad", "noun")]),
  MUDAF_ILAYH("كِتَابِ", "kitab", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  *MA_BADA_TABIA(punct=".")]})

S4.append({"id": "s4", "translation": {"en": "He went back to his house and read it, and at once he understood what he had not understood before, because he knew the first book by heart.",
                                      "tr": "Evine döndü ve onu okudu; daha önce anlamadığını hemen anladı, çünkü ilk kitabı ezbere biliyordu."},
 "tokens": [MADI("فَرَجَعَ", "rajaa", hidden=True), ILA(), ENC_NOUN("بَيْتِهِ", "bayt", "هِ", "majr"),
  ENC_MADI("وَقَرَأَهُ", "qaraa", "هُ", ["thulathi-mujarrad-babs"], hidden=True, punct="،",
    note_ar="، وَالْهَاءُ عَائِدٌ عَلَى كِتَابِ الْفَارَابِيِّ", note_en="; «it» returns to al-Fārābī's book", note_tr="; zamir Fârâbî'nin kitabına döner"),
  MADI("فَفَهِمَ", "fahima", hidden=True), FI(),
  MAJR("الْحَالِ", "hal-state", note_ar=" — وَ«فِي الْحَالِ»: فِي الْوَقْتِ نَفْسِهِ", note_en=" — «fī l-ḥāl»: at once, in that very moment", note_tr=" — «fi'l-hâl»: hemen, o anda"),
  MA_MAWSULA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"]), LAM_JAZM(),
  tok("يَفْهَمْهُ", "fahima", "verb", ["nawasib-wa-jawazim-al-mudari", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَهُوَ الْعَائِدُ عَلَى «مَا»" + SILA[0] + ".",
    "Present verb in jazm by لَمْ, its sign the sukun; the doer is a hidden pronoun «he», and the attached «it» is its object, in the seat of nasb — the pronoun that returns to مَا" + SILA[1] + ".",
    "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli zamir «o»; bitişik zamir mef'ûlün bih, mahallen mansûb — «mâ»ya dönen zamir" + SILA[2] + ".",
    segments=[seg("يَفْهَمْ", "fahima", "verb"), seg("هُ", "pron-3ms", "pron")]),
  MIN(), QABLU(punct="،"),
  LIANNAHU_(), KANA_HID("كَانَ", note=KH_ANNA_CL), MUDARI_KH("يَحْفَظُ", "hafiza"), MAFUL("الْكِتَابَ", "kitab"), NAAT("الْأَوَّلَ", "awwal", "nasb", punct=".")]})

S4.append({"id": "s5", "translation": {"en": "He rejoiced at that, and the next day he gave the poor much wealth, thanking God.",
                                      "tr": "Buna sevindi ve ertesi gün, Allah'a şükrederek fakirlere çok mal verdi."},
 "tokens": [MADI("فَفَرِحَ", "fariha", hidden=True),
  PREP_DHALIKA("بِذٰلِكَ", "بِ", "bi", "الْبَاءُ حَرْفُ جَرٍّ", "The ba is a jarr letter", "Bâ cer harfi", ATTACH("فَرِحَ", "rejoiced", "sevindi"), punct="،"),
  MADI_DA("وَأَعْطَى", "aata", ["form-iv-verbs", "mafulayn"], note_ar=" — وَهُوَ يَنْصِبُ مَفْعُولَيْنِ", note_en="; it takes two objects", note_tr="; iki mef'ûl alır"),
  tok("الْفُقَرَاءَ", "faqir", "noun", ["maful-bihi", "mafulayn", "jam-taksir"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ فَقِيرٍ عَلَى فُعَلَاءَ.",
    "The first object, in nasb — the plural of فَقِير on فُعَلَاء.", "Birinci mef'ûlün bih, mansûb — fakîr'in fuʿalâ' veznindeki cem'i."),
  FI(), MAJR("الْغَدِ", "ghad", note_ar=" — وَ«فِي الْغَدِ»: فِي الْيَوْمِ الَّذِي بَعْدَهُ", note_en=" — «on the morrow»: on the following day", note_tr=" — «ertesi gün»"),
  tok("مَالًا", "mal", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb.", "İkinci mef'ûlün bih, mansûb."),
  NAAT("كَثِيرًا", "kathir", "nasb", punct="،"),
  MUDARI("يَشْكُرُ", "shakara", ["hal", "al-hal-jumla-wa-rabituha"], note_ar=HAL_CL[0] + " مِنْ فَاعِلِ «أَعْطَى»", note_en=HAL_CL[1] + " of the doer of «gave»", note_tr=HAL_CL[2] + " («verdi»nin fâilinden)"),
  ALLAH_MAF(punct=".")]})

# ============================================ Chapter 5 — خِزَانَةُ الْكُتُبِ ============================================
S5 = []
S5.append({"id": "s1", "translation": {"en": "In that time the emir of Bukhārā, Nūḥ ibn Manṣūr, fell ill with an illness that was hard for the physicians.",
                                      "tr": "O zamanda Buhârâ emîri Nûh b. Mansûr, hekimlere zor gelen bir hastalığa yakalandı."},
 "tokens": [WA_FI(istinaf=True), DHALIKA("جَرٍّ", "jarr", "mecrûr"), BADAL_OF("الزَّمَانِ", "zaman", "jarr", "ذٰلِكَ", "that", "o"),
  MADI("مَرِضَ", "marida", note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]),
  FAIL("أَمِيرُ", "amir", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  BUKHARA("mudaf", punct="،"),
  BADAL_OF("نُوحُ", "nuh", "raf", "أَمِيرُ", "emir", "emîr", pos="propn", note=IBN_DROP),
  tok("بْنُ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«نُوحُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
    "An adjective (na't) of «Nūḥ», in raf' and annexed — its alif is dropped in writing because it stands between two names.", "«Nûh»un na'tı, merfû, muzâf — iki alem arasında geldiği için elifi yazıda düşer."),
  MUDAF_ILAYH("مَنْصُورٍ", "mansur-name", "propn", punct="،", note_ar=" — عَلَمٌ مُنْصَرِفٌ", note_en=" — a proper name that keeps its tanwin", note_tr=" — munsarif özel isim"),
  tok("مَرَضًا", "marad", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «مَرِضَ»، مَوْصُوفٌ فَيُبَيِّنُ نَوْعَ الْفِعْلِ.",
    "The absolute object, in nasb — the masdar of «fell ill»; being described, it states the KIND of the act.", "Mef'ûlün mutlak, mansûb — «hastalandı»nın masdarı; sıfatlandığı için fiilin türünü bildirir."),
  NAAT("صَعْبًا", "sab", "nasb"), ALA(),
  MAJR("الْأَطِبَّاءِ", "tabib", extra=["jam-taksir"], punct=".", note_ar=" — جَمْعُ طَبِيبٍ" + ATTACH("صَعْبًا", "hard", "zor")[0], note_en=" — the plural of طَبِيب" + ATTACH("صَعْبًا", "hard", "zor")[1], note_tr=" — tabîb'in cem'i" + ATTACH("صَعْبًا", "hard", "zor")[2])]})

S5.append({"id": "s2", "translation": {"en": "Ibn Sīnā's name had already become known, so he was summoned to the emir's palace.", "tr": "İbn Sînâ'nın adı zaten duyulmuştu; bu yüzden emîrin sarayına çağrıldı."},
 "tokens": [KANA("وَكَانَ"), ISMK("اسْمُ", "ism-name", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), *IBN("mudaf"), QAD_K(),
  MADI_D("اشْتَهَرَ", "ishtahara", ["form-viii-verbs", "kana-wa-akhawatuha"], hidden=True, punct="،",
    note_ar=KH_KANA_CL[0] + " — وَكَانَ مَعَ قَدْ وَالْمَاضِي تُفِيدُ أَنَّ الْأَمْرَ تَمَّ قَبْلَ مَا بَعْدَهُ", note_en=KH_KANA_CL[1] + " — كَانَ + قَدْ + a past verb: it «had» already happened", note_tr=KH_KANA_CL[2] + " — kâne + kad + mâzî: iş daha önce olmuştu"),
  MAJHUL("فَدُعِيَ", "daa", ["naqis-verbs"], note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَلَامُهُ وَاوٌ فِي الْأَصْلِ (دَعَا يَدْعُو) قُلِبَتْ يَاءً لِانْكِسَارِ مَا قَبْلَهَا",
    note_en="; its deputy doer is the hidden «he» — its last radical is a waw (دَعَا يَدْعُو), turned into ya after the kasra", note_tr="; nâib-i fâil gizli zamir «o» — lâmı aslen vâvdır (deâ yed'û), kesreden sonra yâ'ya dönmüştür"),
  ILA(), MAJR("قَصْرِ", "qasr-palace", extra=["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْأَمِيرِ", "amir", punct=".")]})

S5.append({"id": "s3", "translation": {"en": "He treated him together with the physicians, and God healed him.", "tr": "Hekimlerle birlikte onu tedavi etti; Allah da ona şifa verdi."},
 "tokens": [ENC_MADI("فَعَالَجَهُ", "alaja", "هُ", ["form-iii-verbs"], hidden=True), MAA(),
  MUDAF_ILAYH("الْأَطِبَّاءِ", "tabib", extra=["jam-taksir"], punct="،", note_ar=" — جَمْعُ طَبِيبٍ", note_en=" — the plural of طَبِيب", note_tr=" — tabîb'in cem'i"),
  ENC_MADI("فَشَفَاهُ", "shafa", "هُ", ["thulathi-mujarrad-babs"], alif=True, note_ar=DOER_AFTER[0], note_en=DOER_AFTER[1], note_tr=DOER_AFTER[2]), ALLAH_F(punct=".")]})

S5.append({"id": "s4", "translation": {"en": "He asked the emir's leave to enter the store of his books, and the emir gave him leave.", "tr": "Emîrden kitaplarının hazinesine girmek için izin istedi; emîr de ona izin verdi."},
 "tokens": [MADI_D("فَاسْتَأْذَنَ", "istadhana", ["form-x-verbs"], hidden=True), MAFUL("الْأَمِيرَ", "amir"), FI(),
  MAJR("دُخُولِ", "dukhul", extra=["idafa-definiteness", "masdar"], note_ar="، مُضَافٌ — مَصْدَرُ دَخَلَ", note_en=", annexed — the masdar of دَخَلَ", note_tr=", muzâf — dehale'nin masdarı"),
  MUDAF_ILAYH("خِزَانَةِ", "khizana", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ENC_NOUN("كُتُبِهِ", "kitab", "هِ", "mudaf", ["jam-taksir"], punct="،", note_ar=" — جَمْعُ كِتَابٍ، وَالْهَاءُ عَائِدٌ عَلَى الْأَمِيرِ", note_en=" — the plural of كِتَاب; «his» returns to the emir", note_tr=" — kitâb'ın cem'i; zamir emîre döner"),
  MADI("فَأَذِنَ", "adhina", hidden=True, note_ar=" — يَعُودُ عَلَى الْأَمِيرِ", note_en=" (the emir)", note_tr=" (emîr)"), LAHU_(punct=".")]})

S5.append({"id": "s5", "translation": {"en": "He entered a house with many rooms, and in every room were the books of one of the sciences.", "tr": "Pek çok odası olan bir eve girdi; her odada ilimlerden birinin kitapları vardı."},
 "tokens": [MADI("فَدَخَلَ", "dakhala", hidden=True), MAFUL("دَارًا", "dar"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«دَارًا»",
    note_en=" — the jarr phrase is the fronted predicate, and the nominal clause qualifies «a house», in the seat of nasb", note_tr=" — câr-mecrûr öne alınmış haber; isim cümlesi «ev»in na'tı, mahallen mansûb"),
  MUBTADA("بُيُوتٌ", "bayt", extra=["jam-taksir"], note_ar=" — مُؤَخَّرٌ، جَمْعُ بَيْتٍ", note_en=" — placed after its predicate; the plural of بَيْت (here: the rooms of a house)", note_tr=" — haberinden sonraya bırakılmış; beyt'in cem'i (burada: evin odaları)"),
  NAAT("كَثِيرَةٌ", "kathir", punct="،", note_ar=" — وَأُنِّثَ لِأَنَّ مَوْصُوفَهُ جَمْعُ تَكْسِيرٍ لِغَيْرِ الْعَاقِلِ", note_en=" — feminine singular, describing a broken plural of things", note_tr=" — akılsızların cem-i mükesserini vasfettiği için müfred müennes"),
  WA_FI(),
  MAJR("كُلِّ", "kull", extra=["idafa-definiteness"], note_ar="، مُضَافٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", note_en=", annexed; the jarr phrase is the FRONTED predicate", note_tr=", muzâf; câr-mecrûr öne alınmış haber"),
  MUDAF_ILAYH("بَيْتٍ", "bayt"),
  MUBTADA("كُتُبُ", "kitab", extra=["jam-taksir", "idafa-definiteness"], note_ar=" — مُؤَخَّرٌ، مُضَافٌ — جَمْعُ كِتَابٍ", note_en=" — placed after its predicate, and annexed; the plural of كِتَاب", note_tr=" — haberinden sonraya bırakılmış, muzâf; kitâb'ın cem'i"),
  MUDAF_ILAYH("عِلْمٍ", "ilm"), MINA(),
  MAJR("الْعُلُومِ", "ilm", extra=["jam-taksir"], punct=".", note_ar=" — جَمْعُ عِلْمٍ" + JAR_NAAT("jarr", "عِلْمٍ", "a science", "ilim")[0], note_en=" — the plural of عِلْم" + JAR_NAAT("jarr", "عِلْمٍ", "a science", "ilim")[1], note_tr=" — ilm'in cem'i" + JAR_NAAT("jarr", "عِلْمٍ", "a science", "ilim")[2])]})

S5.append({"id": "s6", "translation": {"en": "He read many books he had never seen before, and drew benefit from them.", "tr": "Daha önce görmediği pek çok kitap okudu ve onlardan faydalandı."},
 "tokens": [MADI("فَقَرَأَ", "qaraa", hidden=True), MAFUL("كُتُبًا", "kitab", extra=["jam-taksir"], note_ar=" — جَمْعُ كِتَابٍ", note_en=" — the plural of كِتَاب", note_tr=" — kitâb'ın cem'i"),
  NAAT("كَثِيرَةً", "kathir", "nasb"), LAM_JAZM(),
  tok("يَرَهَا", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "jumla-sifa"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (يَرَى ← يَرَ)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«كُتُبًا».",
    "Present verb in jazm by لَمْ, its sign the dropped weak letter (يَرَى → يَرَ); the doer is a hidden pronoun «he», and the attached «them» is its object, in the seat of nasb — the clause qualifies «books», in the seat of nasb.",
    "Lem ile meczûm muzâri, alâmeti illet harfinin hazfi (yerâ → yera); fâil gizli zamir «o»; bitişik zamir mef'ûlün bih, mahallen mansûb — cümle «kitaplar»ın na'tı, mahallen mansûb.",
    segments=[seg("يَرَ", "raa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  MIN(), QABLU(punct="،"),
  MADI_D("وَانْتَفَعَ", "intafaa", ["form-viii-verbs"], hidden=True),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onlardan»)", punct=".", note_ar="، وَهَا عَائِدٌ عَلَى «كُتُبًا»", note_en="; «them» returns to the books", note_tr="; zamir kitaplara döner")]})

CHAPS = [S1, S2, S3, S4, S5]

# ---- the lexicon: every key by lemma identity from the shelf (the majority reading of a key wins) -------------------------
PKGS = sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
_M = {p: (json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
          if (ROOT / "content/samples" / p / "morphology.json").exists() else {}) for p in PKGS}
# packages staged by parallel authors (not yet on the shelf): a NEW key must not collide with theirs either
STAGED = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", "")) if os.environ.get("QISSA_PKG_ROOT") else None
_GS = {}
if STAGED and STAGED.exists():
    for d in STAGED.iterdir():
        if d.name != SLUG and d.name not in PKGS and (d / "glossary.json").exists():
            _GS[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
DIA_ = re.compile("[ً-ٰ]")
def _lemma_id(e): return DIA_.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))
# keys whose first majority holder carries a gloss written for another context — pinned to a package whose gloss is plain
FORCE = {"kitab": "al-bukhari-fi-baghdad", "hafiza": "abu-hanifa-wa-al-safina", "ibn": "al-bukhari-fi-baghdad"}
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
 "sina": {"lemma": "سِينَا", "pos": "propn", "gloss": {"en": "Sīnā — in «Ibn Sīnā», the name by which the physician and philosopher Abū ʿAlī al-Ḥusayn ibn ʿAbd Allāh (d. 428 / 1037) is known; a foreign maqṣūr name, a diptote", "tr": "Sînâ — hekim ve filozof Ebû Ali el-Hüseyin b. Abdullah'ın (ö. 428 / 1037) tanındığı «İbn Sînâ» adında; yabancı, maksûr, gayr-i munsarif özel isim"}, "level": 4},
 "bukhara": {"lemma": "بُخَارَى", "pos": "propn", "gloss": {"en": "Bukhārā — the city of Transoxiana, seat of the Sāmānid emirs; a foreign maqṣūr name, a diptote", "tr": "Buhârâ — Mâverâünnehir'de, Sâmânî emîrlerinin oturduğu şehir; yabancı, maksûr, gayr-i munsarif özel isim"}, "level": 4},
 "farabi": {"lemma": "الْفَارَابِيّ", "pos": "propn", "gloss": {"en": "al-Fārābī — Abū Naṣr Muḥammad al-Fārābī (d. 339 / 950), the philosopher, called «the Second Teacher»", "tr": "Fârâbî — «Muallim-i Sânî» denilen filozof Ebû Nasr Muhammed el-Fârâbî (ö. 339 / 950)"}, "level": 4},
 "mansur-name": {"lemma": "مَنْصُور", "root": "ن ص ر", "pos": "propn", "gloss": {"en": "Manṣūr — a man's name (here the father of the emir Nūḥ ibn Manṣūr); it keeps its tanwin", "tr": "Mansûr — erkek adı (burada emîr Nûh b. Mansûr'un babası); munsariftir"}, "level": 4},
}
# keys on the shelf whose only gloss was written for another context: the lemma, root and pos are kept, the gloss is this story's
REGLOSS = {
 "fiqh": {"en": "fiqh — the science of the rulings of the Law, jurisprudence", "tr": "fıkıh — şer'î hükümlerin ilmi"},
 "adab": {"en": "adab — good manners; also the learning of letters: the Arabic language, poetry and literary lore", "tr": "edeb — güzel ahlâk; ayrıca dil, şiir ve edebî bilgiler ilmi"},
 "mantiq": {"en": "speech; logic — the science of right reasoning (عِلْمُ الْمَنْطِقِ)", "tr": "konuşma; mantık — doğru düşünmenin ilmi (ilmü'l-mantık)"},
 "hikma": {"en": "wisdom; philosophy — عُلُومُ الْحِكْمَةِ, the philosophical sciences", "tr": "hikmet; felsefe — ulûmü'l-hikme, felsefî ilimler"},
 "salla": {"en": "to pray, to perform the prayer; to bless (صَلَّى عَلَى)", "tr": "namaz kılmak; (alâ ile) salât etmek"},
 "hafiza": {"en": "to preserve, to keep; to learn by heart (حَفِظَ يَحْفَظُ)", "tr": "korumak, muhafaza etmek; ezberlemek (hafıza yahfazu)"},
 "nuh": {"en": "Nūḥ — a man's name; here Nūḥ ibn Manṣūr, the Sāmānid emir of Bukhārā (a three-letter name with a quiet middle: it declines in full)", "tr": "Nûh — erkek adı; burada Buhârâ'nın Sâmânî emîri Nûh b. Mansûr (ortası sâkin üç harfli isim: munsariftir)"},
 "khizana": {"en": "a treasury, a storehouse; خِزَانَةُ الْكُتُبِ: a library", "tr": "hazine, ambar; hizânetü'l-kütüb: kütüphane"},
 "bayt": {"en": "a house; a room of a house (pl. بُيُوت)", "tr": "ev; bir evin odası (çoğ. buyût)"},
 "tabia": {"en": "nature; مَا بَعْدَ الطَّبِيعَةِ «what comes after nature»: metaphysics", "tr": "tabiat; mâ ba'de't-tabîa «tabiattan sonra gelen»: metafizik"},
}
for k in NEW_GLOSS:
    hit = [p for p in PKGS if k in _G[p]] + [p for p in _GS if k in _GS[p] and _lemma_id(_GS[p][k]) != _lemma_id(NEW_GLOSS[k])]
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
 "title": {"ar": "ابْنُ سِينَا يَتَعَلَّمُ", "en": "Ibn Sīnā Learns", "tr": "İbn Sînâ Öğreniyor"},
 "subtitle": {"ar": "صَبِيٌّ مِنْ بُخَارَى يَطْلُبُ الْعِلْمَ، فَيَقْرَأُ كِتَابًا صَعْبًا أَرْبَعِينَ مَرَّةً، وَيُعَالِجُ أَمِيرَ بَلَدِهِ — قِصَّةٌ لِلْمُسْتَوَى الرَّابِعِ",
              "en": "A boy from Bukhārā seeks knowledge, reads a hard book forty times, and treats the emir of his land — a story for the fourth level",
              "tr": "Buhârâlı bir çocuk ilim peşine düşer, zor bir kitabı kırk kere okur ve ülkesinin emîrini tedavi eder — dördüncü seviye için bir hikâye"},
 "level": 4,
 "levelName": "Upper Intermediate",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُتَدَرِّجَةٌ (الْمُسْتَوَى الرَّابِعُ) لِخَبَرِ تَعَلُّمِ ابْنِ سِينَا كَمَا يَحْكِيهِ هُوَ فِي سِيرَتِهِ الَّتِي رَوَاهَا عَنْهُ تِلْمِيذُهُ، وَنَقَلَهَا ابْنُ أَبِي أُصَيْبِعَةَ فِي «عُيُونِ الْأَنْبَاءِ فِي طَبَقَاتِ الْأَطِبَّاءِ»: صِبَاهُ فِي بُخَارَى وَقِرَاءَتِهِ الْقُرْآنَ وَالْأَدَبَ، ثُمَّ الْفِقْهِ وَالْمَنْطِقِ، ثُمَّ الطِّبِّ وَعِلَاجِهِ الْمَرْضَى، ثُمَّ قِرَاءَتِهِ كِتَابَ مَا بَعْدَ الطَّبِيعَةِ أَرْبَعِينَ مَرَّةً، وَشِرَائِهِ كِتَابَ الْفَارَابِيِّ فِي أَغْرَاضِهِ وَصَدَقَتِهِ شُكْرًا لِلّٰهِ، ثُمَّ عِلَاجِهِ الْأَمِيرَ نُوحَ بْنَ مَنْصُورٍ وَدُخُولِهِ خِزَانَةَ كُتُبِهِ. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ مَصْدَرٍ، وَلَا آيَةٌ وَلَا نَصُّ حَدِيثٍ، وَلَمْ يُوضَعْ عَلَى لِسَانِهِ كَلَامٌ؛ وَتُرِكَتِ الْأَعْمَارُ لِاخْتِلَافِ الرِّوَايَاتِ فِيهَا.",
  "en": "ORIGINAL Level-4 graded Arabic: the education of Ibn Sīnā as he tells it in his own autobiography (al-Sīra), transmitted by his student Abū ʿUbayd al-Jūzjānī and carried by Ibn Abī Uṣaybiʿa in ʿUyūn al-anbāʾ fī ṭabaqāt al-aṭibbāʾ — his boyhood in Bukhārā, the Qurʾān and adab, then fiqh and logic; medicine, learned quickly, and the sick he treated while still young; the Metaphysics (Aristotle's, here called by its Arabic title) read forty times without its aim becoming clear, until al-Fārābī's book on the aims of the Metaphysics, bought cheaply in the book market, opened it to him, and the alms he gave the next day in thanks to God; and the Sāmānid emir Nūḥ ibn Manṣūr, whom he treated with the physicians and who gave him leave to enter his library — RETOLD FREELY in the wording of a graded reader, in the order of the Sīra. No sentence is a quotation of a source; no verse and no ḥadīth text is quoted; no words are put in his mouth. The ages at each step vary in the reports, so they are not given: the story says only «while still young».",
  "tr": "ÖZGÜN 4. seviye kademeli Arapça: İbn Sînâ'nın kendi hayat hikâyesinde (es-Sîre) anlattığı şekliyle tahsili — talebesi Ebû Ubeyd el-Cûzcânî'nin rivayetiyle, İbn Ebû Usaybia'nın «Uyûnü'l-enbâ fî tabakāti'l-etıbbâ»sında yer alır: Buhârâ'daki çocukluğu, Kur'ân ve edeb, ardından fıkıh ve mantık; çabucak öğrendiği tıp ve daha gençken tedavi ettiği hastalar; maksadı anlaşılmadan kırk kere okunan Metafizik (Aristoteles'in kitabı; burada Arapça adıyla anılır), ta ki kitap çarşısında ucuza alınan, Fârâbî'nin Metafizik'in maksatlarına dair kitabı onu kendisine açana dek, ve ertesi gün Allah'a şükür için verdiği sadaka; hekimlerle birlikte tedavi ettiği ve kendisine kütüphanesine girme izni veren Sâmânî emîri Nûh b. Mansûr — kademeli okuyucu üslûbuyla, Sîre'nin sırasıyla SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir kaynaktan alıntı değildir; hiçbir âyet ve hiçbir hadis metni aktarılmamıştır; onun ağzına söz konmamıştır. Her adımdaki yaşlar rivayetlerde farklı geldiği için verilmemiştir: hikâye yalnızca «daha gençken» der.",
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
