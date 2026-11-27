"""Author content/samples/ibn-khaldun-wa-timur — «ابْنُ خَلْدُونَ وَتَيْمُورُ», an ORIGINAL historical story at Level 6 (Master).

ORIGINAL graded Arabic in a classical narrative register, kept to the well-attested core of Ibn Khaldūn's own account of
the year 803 AH / 1400–1401 CE in his autobiography (al-Taʿrīf bi-Ibn Khaldūn wa-Riḥlatihi Gharban wa-Sharqan): the
Maghribī scholar settled in Egypt and a judge there, the author of the Muqaddima; Tīmūr comes out of the East, takes
Aleppo and lays siege to Damascus; the Mamluk sultan marches to Syria with his armies, taking the judges and scholars with
him, Ibn Khaldūn among them; after some days of fighting the sultan and his emirs go back to Egypt by night; Ibn Khaldūn
stays in the city; the people of Damascus seek terms, their judges go out to Tīmūr; Ibn Khaldūn goes to the wall at
daybreak and is let down by a rope, finds Tīmūr's men at the gate and is taken to him; he is received with honour, is
asked about the lands of the Maghrib, talks with Tīmūr through an interpreter over many sessions of history and the reports
of kings, brings him a gift, and with his leave returns to Egypt, where he dies a few years later. The story closes on the
reflection that the author of the Muqaddima — the book on the rise and fall of states — saw one of history's turning days.

The account is RETOLD FREELY — no sentence is a quotation from al-Taʿrīf or from the Muqaddima, no āya or ḥadīth is quoted,
no words are put in a historical person's mouth. Left out on purpose: the reported content of the conversations beyond their
general topics (the Maghrib; history and kings), the description of the Maghrib that Ibn Khaldūn wrote for Tīmūr, the reason
the sultan turned back, the motives of the parties, the dates and the length of the stay, the names of the qāḍīs and the
interpreter, the robbery on the road home, and every figure of the sack of Damascus. The year is given as «the opening of the
ninth century» (803 AH) — the numeral 803 is not put into vowelled Arabic.

NAMES. تَيْمُور is a foreign proper name, a diptote for ʿalamiyya + ʿujma (the shelf's line for أَرْمَانُوس). دِمَشْق is a city,
a diptote for ʿalamiyya + taʾnīth (the shelf's line for حَلَب). خَلْدُون is read in its common vowelling as a diptote
(ابْنُ خَلْدُونَ), like زَيْدُونَ and حَمْدُونَ; the iʿrāb line says that some decline it — the khilāf is taught as a khilāf and
is listed for the scholar's review.

Five chapters, twenty-nine sentences. The Level-6 constructions: long periodic sentences (ch3 s3, ch5 s6); فَبَيْنَمَا … إِذْ …;
ثُمَّ إِنَّهُ; ḥaṣr by negation + إِلَّا (لَمْ يَكُنْ … إِلَّا أَنْ …) and by إِنَّمَا (twice, the restricted term last); the oath
لَعَمْرِي answered by لَقَدْ; كَمِ الْخَبَرِيَّةُ (its line notes why كَمْ is no fronted object: the verb is busy with its pronoun — ishtighāl); tanāzuʿ over the fāʿil (اسْتَقْبَلَهُ وَأَكْرَمَهُ تَيْمُورُ, the Basran reading); the
mafʿūl muṭlaq of kind (مَعْرِفَةَ مَنْ عَاشَ بَيْنَهُمْ); the mafʿūl lahu (خَوْفًا); tamyīz after an elative (أَكْثَرَ … جُنْدًا);
kāna tāmma (مَا يَكُونُ); أَمَّا … فَـ; relative clauses with resumptive pronouns (لَهُ، فِيهَا، عَنْهُ); لَمَّا; حَتَّى with the
subjunctive and حَتَّى of ibtidāʾ; the wāw of ḥāl before a nominal clause; the passive (يُقَالُ، أُنْزِلَ).

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf, every verb's paradigm is
the shelf's own (no new verb), and the new entries are only those in NEW_GLOSS (تَيْمُور، دِمَشْق، خَلْدُون، مُقَدِّمَة and the
name-phrase ابْنُ خَلْدُونَ). Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_ibn_khaldun_wa_timur.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "ibn-khaldun-wa-timur"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"هُمُ": "pron-3mp", "هِمُ": "pron-3mp", "هِمْ": "pron-3mp", "هُمْ": "pron-3mp", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "ي": "pron-1s"})
PRON_AR.update({"هُمُ": "هُمْ", "هِمُ": "هُمْ", "هِمْ": "هُمْ", "هُمْ": "هُمْ", "هُمَا": "هُمَا", "هِمَا": "هُمَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "ي": "الْيَاءُ"})

N = lambda s: unicodedata.normalize("NFC", s)
def PH(t, lex, span=2):
    """the name-phrase sits on the FIRST token of its span (CLAUDE.md «Idioms/phrases»): both words keep their own iʿrāb"""
    t["phrase"] = {"lex": lex, "span": span}
    return t
def NOTE(t, ar="", en="", tr=""):
    """append a remark to a kit line, before its closing full stop"""
    for k, v in (("ar", ar), ("en", en), ("tr", tr)):
        if v:
            s = t["irab"][k]
            t["irab"][k] = N((s[:-1] if s.endswith(".") else s) + v + ".")
    return t
def TAG(t, *tags):
    for g in tags:
        if g not in t.setdefault("grammar", []): t["grammar"].append(g)
    return t
def ISTINAF(t):
    """a chapter-opening wāw is the wāw of a new start, not of conjunction"""
    i = t["irab"]
    i["ar"] = N(i["ar"].replace(N(WA_AR), N("الْوَاوُ لِلِاسْتِئْنَافِ، وَ"), 1))
    i["en"] = i["en"].replace("The waw conjoins; ", "The waw opens a new sentence; ", 1)
    i["tr"] = i["tr"].replace("«ve» + ", "Vâv isti'nâf içindir; ", 1)
    return t
def W(t3, *more):
    """join note triples"""
    out = list(t3)
    for m in more:
        out = [a + b for a, b in zip(out, m)]
    return dict(note_ar=out[0], note_en=out[1], note_tr=out[2])

MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
KH_KANA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
KH_INNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi olarak mahallen merfû")
KH_ANNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
KH_MUB_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the clause is the predicate of the mubtada, in the seat of raf'", "; cümle mübtedânın haberi, mahallen merfû")
HALCL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause is a hal, in the seat of nasb", "; cümle hâl olarak mahallen mansûb")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
KH_KAM = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَمْ", "; the clause is the khabar of كَمْ, in the seat of raf'", "; cümle kem'in haberi, mahallen merfû")
NAIB_HID = ("، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", "; its deputy doer is the hidden «he»", "; nâib-i fâil gizli zamir «o»")
KH_AMMA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the clause is the predicate of the mubtada, in the seat of raf'", "; cümle mübtedânın haberi, mahallen merfû")
def NAAT_OF(n_ar, n_en, n_tr, case_ar="نَصْبٍ", case_en="nasb", case_tr="mansûb", nth=("", "", "")):
    """a jarr phrase hanging on an omitted adjective of a named noun"""
    return (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ" + nth[0] + " لِـ«" + n_ar + "»",
            "; the jarr phrase hangs on an omitted " + (nth[1] + " " if nth[1] else "") + "adjective of «" + n_en + "»",
            " — câr-mecrûr «" + n_tr + "»in mahzûf " + (nth[2] + " " if nth[2] else "") + "na'tına müteallik")

# ---- the names --------------------------------------------------------------------------------------------------
AJAM = ("عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ",
        "a foreign proper name, a diptote by ʿalamiyya + ʿujma (proper name + foreign origin)",
        "yabancı özel isim, alemiyet ve ucmet sebebiyle gayr-i munsarif")
DIPT_F2 = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town), barred from tanwin", " — müennes özel isim (şehir adı), gayr-i munsarif")
DIPT_LAND = (DIPT_F2[0], DIPT_F2[1].replace("a town", "a land"), DIPT_F2[2].replace("şehir adı", "ülke adı"))
NO_TANWIN = ("، مِنْ غَيْرِ تَنْوِينٍ", ", with no tanwin", ", tenvinsiz")

def TIMUR(role, punct=None, note=("", "", "")):
    """تَيْمُور — ʿalam + ʿujma: no tanwin, and a fatḥa for jarr"""
    a = (" — " + AJAM[0] + note[0], " — " + AJAM[1] + note[1], " — " + AJAM[2] + note[2])
    if role == "fail":
        return FAIL("تَيْمُورُ", "timur", "propn", ["mamnu-min-sarf"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=a[0], note_en=", with no tanwin" + a[1], note_tr=", tenvinsiz" + a[2], punct=punct)
    if role == "naib":
        return tok("تَيْمُورُ", "timur", "propn", ["naib-al-fail", "mamnu-min-sarf"],
            "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — وَهُوَ الِاسْمُ الْمَقُولُ نَفْسُهُ؛ " + AJAM[0] + ".",
            "The deputy doer of «is called», in raf' with no tanwin — the very name that is said; " + AJAM[1] + ".",
            "«Denir»in nâib-i fâili, tenvinsiz merfû — söylenen ismin kendisi; " + AJAM[2] + ".", punct=punct)
    if role == "majr":
        return MAJR("تَيْمُورَ", "timur", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=a[0], note_en=" — by a fatha standing in for the kasra" + a[1], note_tr=" — kesre yerine fetha ile" + a[2], punct=punct)
    if role == "mi":
        return MUDAF_ILAYH("تَيْمُورَ", "timur", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=a[0], note_en=" — by a fatha standing in for the kasra" + a[1], note_tr=" — kesre yerine fetha ile" + a[2], punct=punct)
    if role == "maful":
        return MAFUL("تَيْمُورَ", "timur", "propn", ["mamnu-min-sarf"], sign="بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=a[0], note_en=", with no tanwin" + a[1], note_tr=", tenvinsiz" + a[2], punct=punct)
    raise ValueError(role)

def DIMASHQ(role, punct=None):
    """دِمَشْق — a city: ʿalam + taʾnīth"""
    if role == "majr":
        return MAJR("دِمَشْقَ", "dimashq", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F2[0], note_en=" — by a fatha standing in for the kasra" + DIPT_F2[1], note_tr=" — kesre yerine fetha ile" + DIPT_F2[2], punct=punct)
    if role == "mi":
        return MUDAF_ILAYH("دِمَشْقَ", "dimashq", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F2[0], note_en=" — by a fatha standing in for the kasra" + DIPT_F2[1], note_tr=" — kesre yerine fetha ile" + DIPT_F2[2], punct=punct)
    if role == "mubtada":
        return MUBTADA("دِمَشْقُ", "dimashq", "propn", ["mamnu-min-sarf", "amma-tafsiliyya"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ",
            note_ar=DIPT_F2[0], note_en=", with no tanwin" + DIPT_F2[1], note_tr=", tenvinsiz" + DIPT_F2[2], punct=punct)
    raise ValueError(role)

def MISR_J(punct=None, mi=False):
    f = MUDAF_ILAYH if mi else MAJR
    return f("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_LAND[0], note_en=DIPT_LAND[1], note_tr=DIPT_LAND[2], punct=punct)

IBN_ROLE = {
 "ismk": (["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ كَانَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ", "The noun of كَانَ, in raf', annexed", "Kâne'nin ismi, merfû, muzâf"),
 "fail": (["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ", "The doer (fa'il), in raf', annexed", "Fâil, merfû, muzâf"),
 "mubtada_m": (["mubtada-khabar", "al-hal-jumla-wa-rabituha", "idafa-definiteness"],
               "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ بَعْدَ الْوَاوِ فِي مَحَلِّ نَصْبٍ حَالٌ",
               "The mubtada, placed after its fronted predicate, in raf', annexed — the nominal clause after the waw is a hal, in the seat of nasb",
               "Haberinden sonraya bırakılmış mübtedâ, merfû, muzâf — vâvdan sonraki isim cümlesi hâl olarak mahallen mansûb"),
}
def IBN(role, punct=None):
    g, ar, en, tr = IBN_ROLE[role]
    return PH(tok("ابْنُ", "ibn", "noun", g, ar + " — وَابْنُ خَلْدُونَ اسْمٌ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ.",
        en + " — Ibn Khaldūn is a name built as an idafa.", tr + " — İbn Haldun, izâfet terkibiyle kurulmuş bir isimdir.", punct=punct), "ibn-khaldun")
KHALDUN_LINE = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — عَلَمٌ يُضْبَطُ فِي الْمَشْهُورِ مَمْنُوعًا مِنَ الصَّرْفِ كَزَيْدُونَ وَحَمْدُونَ، وَبَعْضُهُمْ يَصْرِفُهُ.",
                "The second term of the idafa, in jarr by a fatha standing in for the kasra — in its usual vowelling this proper name is a diptote, like Zaydūn and Ḥamdūn; some read it fully declined.",
                "Muzâfun ileyh, kesre yerine fetha ile mecrûr — bu özel isim meşhur zabtında Zeydûn ve Hamdûn gibi gayr-i munsariftir; bazıları onu munsarif okur.")
KHALDUN_MI = lambda punct=None: tok("خَلْدُونَ", "khaldun", "propn", ["idafa-definiteness", "mamnu-min-sarf"], *KHALDUN_LINE, punct=punct)

# ---- particles and frames the kit does not hold (most copied from the Level-6 stories on the shelf) ----------------
def KAM(full="وَكَمْ"):
    return tok(full, "kam", "pron", ["al-kinayat-wal-zuruf-al-mabniyya", "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf", "mubtada-khabar"],
        "الْوَاوُ لِلِاسْتِئْنَافِ، وَكَمْ خَبَرِيَّةٌ بِمَعْنَى «كَثِيرٍ» مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، مُضَافٌ — وَالْجُمْلَةُ بَعْدَ تَمْيِيزِهَا خَبَرُهَا.",
        "The waw opens a new sentence; كَمْ here is the كَمْ OF REPORT (khabariyya) meaning «many a»: built on sukun, in the seat of raf' as the mubtada, annexed to its specifier — the verbal clause after the specifier is its khabar.",
        "Vâv isti'nâf içindir; kem burada haberiyye kem'dir («nice, nice nice»): sükûn üzere mebnî, mübtedâ olarak mahallen merfû, temyîzine muzâf — temyîzinden sonraki fiil cümlesi haberidir.",
        segments=[seg("وَ", "wa", "conj"), seg("كَمْ", "kam", "pron")])
def KAM_TAMYIZ(full, lex, punct=None):
    return tok(full, lex, "noun", ["tamyiz", "al-kinayat-wal-zuruf-al-mabniyya", "idafa-definiteness"],
        "تَمْيِيزُ كَمِ الْخَبَرِيَّةِ مَجْرُورٌ بِإِضَافَتِهَا إِلَيْهِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ — وَتَمْيِيزُهَا مُفْرَدٌ مَجْرُورٌ.",
        "The specifier (tamyiz) of the khabari كَمْ, in jarr because كَمْ is annexed to it — the specifier of this كَمْ is a SINGULAR in jarr.",
        "Haberiyye kem'in temyîzi; kem ona muzâf olduğu için mecrûr, alâmeti kesre — bu kem'in temyîzi mecrûr müfreddir.", punct=punct)
def BAYNAMA(full="فَبَيْنَمَا"):
    return tok(full, "baynama", "noun", ["maful-fih", "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha", "anwa-ma"],
        "الْفَاءُ عَاطِفَةٌ، وَبَيْنَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَمَا زَائِدَةٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ بَعْدَهُ فِي مَحَلِّ جَرٍّ بِالْإِضَافَةِ، وَقِيلَ: مَا كَافَّةٌ عَنِ الْإِضَافَةِ فَلَا مَحَلَّ لِلْجُمْلَةِ؛ وَجَوَابُهُ الْجُمْلَةُ الْمُصَدَّرَةُ بِإِذِ الْفُجَائِيَّةِ.",
        "The fa carries the story on; بَيْنَمَا «while»: بَيْنَ is an adverb of time in nasb and مَا is extra — the nominal clause after it is annexed to it, in the seat of jarr (some say مَا cuts the annexation and the clause has no seat); its answer is the clause opened by the إِذْ of surprise.",
        "Fâ atıf; beynemâ «…iken»: beyne mansûb zaman zarfı, mâ zâid — sonraki isim cümlesi ona muzâfun ileyh, mahallen mecrûr (bir görüşe göre mâ izâfeti engeller, cümlenin mahalli yoktur); cevabı müfâcee iz'i ile başlayan cümledir.",
        segments=[seg("فَ", "fa", "conj"), seg("بَيْنَمَا", "baynama", "noun")])
IDH_FUJ = lambda: tok("إِذْ", "idh", "noun", ["al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "al-kinayat-wal-zuruf-al-mabniyya"],
    "إِذْ لِلْمُفَاجَأَةِ، مَبْنِيٌّ عَلَى السُّكُونِ: حَرْفٌ لَا مَحَلَّ لَهُ عِنْدَ قَوْمٍ، وَظَرْفٌ عِنْدَ آخَرِينَ — وَالْجُمْلَةُ بَعْدَهُ جَوَابُ بَيْنَمَا.",
    "The إِذْ OF SURPRISE («and all at once»), built on sukun — a particle with no seat for some grammarians, an adverb for others; the clause after it answers بَيْنَمَا.",
    "Müfâcee iz'i («derken, ansızın»), sükûn üzere mebnî — kimine göre mahalli olmayan harf, kimine göre zarf; sonraki cümle beynemâ'nın cevabıdır.")
ILLA_HASR = lambda: tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "turuq-al-qasr", "qasr"],
    "إِلَّا أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ، فَمَا بَعْدَهَا يُعْرَبُ بِحَسَبِ مَوْقِعِهِ.",
    "إِلَّا here RESTRICTS (ḥaṣr by negation and exception) and governs nothing: the exception is emptied, so what follows takes the case of its own seat.",
    "İllâ burada hasr edatıdır, amel etmez: istisnâ müferrağdır; sonrası kendi mevkiine göre i'râb alır.")
def WA_INNAMA(full="وَإِنَّمَا", pre="istinaf"):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "«ve» + "}[pre]
    return tok(full, "innama", "part", ["innama-kaffa", "qasr", "turuq-al-qasr"],
        pre_ar + "إِنَّمَا أَدَاةُ حَصْرٍ: إِنَّ كَفَّتْهَا مَا الزَّائِدَةُ عَنِ الْعَمَلِ — وَالْمَقْصُورُ عَلَيْهِ هُوَ الْمُؤَخَّرُ فِي الْكَلَامِ.",
        pre_en + "إِنَّمَا «only» is the tool of restriction: the extra مَا has stopped إِنَّ from governing — what is restricted TO comes last in the clause.",
        pre_tr + "innemâ hasr edatıdır: zâid mâ, inne'yi amelden alıkoymuştur — kendisine hasredilen şey cümlede sona gelir.",
        segments=[seg("وَ", "wa", "conj"), seg("إِنَّمَا", "innama", "part")])
def WA_MA(pre="atf", note=("", "", "")):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "«ve» + "}[pre]
    return tok("وَمَا", "ma-nafiya", "part", ["la-nafiya"], pre_ar + "مَا نَافِيَةٌ لَا عَمَلَ لَهَا" + note[0] + ".", pre_en + "مَا negates and governs nothing" + note[1] + ".", pre_tr + "mâ nefiy harfi, amel etmez" + note[2] + ".",
        segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")])
def ZARF_ENC(full, lex, enc, kind="مَكَانٍ", kind_en="place", kind_tr="mekân", punct=None, note_ar="", note_en="", note_tr=""):
    """بَيْنَهُ، عِنْدَهُ، حَوْلَهَا: a ẓarf annexed to its pronoun"""
    return tok(full, lex, "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
        "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        "An adverb of " + kind_en + ", in nasb and annexed to the attached pronoun, which fills the seat of jarr" + note_en + ".",
        kind_tr + " zarfı, mansûb, bitişik zamire muzâf; zamir mahallen mecrûr" + note_tr + ".", punct=punct,
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
WA_BAYNA = lambda: tok("وَبَيْنَ", "bayna", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness"],
    WA_AR + "بَيْنَ ظَرْفٌ مَعْطُوفٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَتُكَرَّرُ بَيْنَ إِذَا عُطِفَ عَلَى الضَّمِيرِ.",
    "The waw conjoins a second «between», in nasb and annexed — بَيْنَ is repeated when the first term is a pronoun.",
    "Vâv atıf; ikinci «arasında», mansûb zarf, muzâf — ilk terim zamir olunca beyne tekrarlanır.",
    segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun")])
def MAA_X(full, enc, note=("", "", ""), punct=None):
    return ZARF_ENC(full, "maa", enc, punct=punct, note_ar=note[0], note_en=note[1], note_tr=note[2])
def MAFUL_LAHU(full, lex, punct=None, note_ar="", note_en="", note_tr="", mudaf=False):
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"] + (["idafa-definiteness"] if mudaf else []),
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ" + ("، مُضَافٌ" if mudaf else "") + " — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ" + note_ar + ".",
        "The maf'ul li-ajlih (object of cause), in nasb" + (" and annexed" if mudaf else "") + " — a masdar of the heart giving the reason for the act, sharing its time and its doer" + note_en + ".",
        "Mef'ûlün lieclih, mansûb" + (", muzâf" if mudaf else "") + " — fiilin sebebini bildiren kalbî masdar; fiille zamanda ve fâilde ortak" + note_tr + ".", punct=punct)
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
DH_MI = ("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh")
def TILKA(seat_ar, seat_en, seat_tr, punct=None):
    return tok("تِلْكَ", "tilka", "pron", ["asma-al-ishara"],
        "اسْمُ إِشَارَةٍ لِلْمُؤَنَّثِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "The feminine demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "Müennes işaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
def YAKUN():
    return tok("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "lam-jazim", "hollow-verbs"],
        "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ: يَكُونُ)، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
        "The defective present of كَانَ in jazm by لَمْ, its sign the sukun; its waw dropped where two quiescents met (from يَكُونُ). It raises its noun and puts its predicate in nasb.",
        "Kâne'nin nâkıs muzârii, lem ile meczûm, alâmeti sükûn; iki sâkin karşılaşınca vâvı düştü (aslı yekûnu). İsmini ref, haberini nasb eder.")
def ANNA_X(note=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + note[0] + ".",
        "أَنَّ «that», the verb-like particle that builds a masdar: it puts its noun in nasb and raises its predicate" + note[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + note[2] + ".")
def SADDA(verb_ar, verb_en, verb_tr):
    return (" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «" + verb_ar + "»",
            "; أَنَّ with its clause stands for a masdar that fills both objects of «" + verb_en + "»",
            "; enne ve sonrası, «" + verb_tr + "»in iki mef'ûlünün yerini tutan müevvel masdardır")
def ISM_ANNA_ENC(full, lex, enc, extra=None, which="anna"):
    p_ar, p_tr = {"inna": ("إِنَّ", "İnne"), "anna": ("أَنَّ", "Enne")}[which]
    return tok(full, lex, "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        "اسْمُ " + p_ar + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        "The noun of " + p_ar + ", in nasb; annexed to the attached pronoun, which fills the seat of jarr.",
        p_tr + "'nin ismi, mansûb; bitişik zamire muzâf, zamir mahallen mecrûr.",
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def WA_HAL_MUB(full, lex):
    """وَالْعَدُوُّ: the waw of hal opening a nominal clause"""
    stem = full[2:]
    return tok(full, lex, "noun", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"],
        "الْوَاوُ حَالِيَّةٌ، وَ" + stem + " مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ بَعْدَ الْوَاوِ فِي مَحَلِّ نَصْبٍ حَالٌ.",
        "The waw opens a hal clause; the noun after it is the mubtada, in raf' — the nominal clause after the waw is a hal, in the seat of nasb.",
        "Hâl vâvı; sonraki isim mübtedâ, merfû — vâvdan sonraki isim cümlesi hâl olarak mahallen mansûb.",
        segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "noun")])
def MAN_ONE(seat_ar, seat_en, seat_tr, extra, note=("", "", "")):
    return tok("مَنْ", "man-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ بِمَعْنَى «الَّذِي» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ" + note[0] + ".",
        "The relative pronoun «the one who», built on sukun, in the seat of " + seat_en + "; the clause after it is its ṣila" + note[1] + ".",
        "İsm-i mevsûl «… kimse», sükûn üzere mebnî, mahallen " + seat_tr + "; sonraki cümle sılasıdır" + note[2] + ".")
def MA_MAWSULA(seat_ar, seat_en, seat_tr, extra):
    return tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
        "A relative pronoun «what», built on sukun, in the seat of " + seat_en + "; the clause after it is its ṣila.",
        "İsm-i mevsûl «…-an şey», sükûn üzere mebnî, mahallen " + seat_tr + "; sonraki cümle sılasıdır.")
def ALLADHI(case, of_ar, of_en, of_tr):
    seat = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[case]
    return tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"],
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat[0] + " نَعْتٌ " + of_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
        "A relative pronoun built on sukun, in the seat of " + seat[1] + " as the adjective of «" + of_en + "»; the clause after it is its ṣila.",
        "İsm-i mevsûl, sükûn üzere mebnî, «" + of_tr + "»nin na'tı olarak mahallen " + seat[2] + "; sonraki cümle sılasıdır.")
def ALLATI(case, of_ar, of_en, of_tr):
    seat = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[case]
    return tok("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"],
        "اسْمٌ مَوْصُولٌ لِلْمُفْرَدَةِ الْمُؤَنَّثَةِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat[0] + " نَعْتٌ " + of_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
        "The feminine singular relative pronoun, built on sukun, in the seat of " + seat[1] + " as the adjective of «" + of_en + "» (a broken plural of things takes the feminine singular); the clause after it is its ṣila.",
        "Müfred müennes ism-i mevsûl, sükûn üzere mebnî, «" + of_tr + "»in na'tı olarak mahallen " + seat[2] + " (eşya için kırık cem' müfred müennes alır); sonraki cümle sılasıdır.")
def ATF_ENC(full, lex, enc, case="jarr", punct=None, note=("", "", ""), extra=None):
    """وَأَهْلِهَا، وَمُلُوكِهَا: a conjoined noun annexed to its pronoun"""
    stem = full[2:-len(enc)]
    sign = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr", "mecrûr")}[case]
    return tok(full, lex, "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        WA_AR + stem + " مَعْطُوفٌ " + sign[0] + "، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note[0] + ".",
        "The waw conjoins; the noun is conjoined to the one before it, in " + sign[1] + ", and annexed to the attached pronoun, which fills the seat of jarr" + note[1] + ".",
        "Vâv atıf; isim öncekine ma'tûf, " + sign[2] + ", bitişik zamire muzâf; zamir mahallen mecrûr" + note[2] + ".",
        punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "noun"), seg(enc, PRON[enc], "pron")])
LAAMRI = lambda: tok("وَلَعَمْرِي", "amr-qasam", "noun", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "mubtada-khabar", "ya-al-mutakallim", "hadhf-wa-taqdir"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْخَبَرُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي؛ وَهٰذِهِ صِيغَةُ قَسَمٍ.",
    "The waw opens a new sentence; the lam is the lam of ibtidāʾ; عَمْر «life» is the mubtada, in raf' by a damma estimated before the speaker's ya (the kasra the ya demands holds its place), annexed to the ya — its predicate is dropped by rule («[is my oath]»): this is a FORM OF OATH, «by my life».",
    "Vâv isti'nâf içindir; lâm ibtidâ lâmıdır; «ömür» mübtedâ, mütekellim yâ'sından önce takdîrî damme ile merfû (yerini yâ'nın gerektirdiği kesre tutmuştur), yâ'ya muzâf — haberi vücûben hazfedilmiştir («yeminimdir»): bu bir yemin kalıbıdır, «ömrüme andolsun».",
    segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-ibtida", "part"), seg("عَمْرِ", "amr-qasam", "noun"), seg("ي", "pron-1s", "pron")])
LAQAD = lambda: tok("لَقَدْ", "qad", "part", ["qad-harf", "al-qasam-wal-shart-fil-kafiya"],
    "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُمَا جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The lam opens the ANSWER of the oath and قَدْ affirms the past verb after it — the clause is the oath's answer and has no seat.",
    "Lâm kasemin cevabına gelmiştir, kad tahkîk harfidir — sonraki cümle kasemin cevabıdır, i'râbdan mahalli yoktur.",
    segments=[seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")])
def FA_AMMA(full):
    """فَأَمَّا / وَأَمَّا: the particle of detailing"""
    pre = full[:2]
    return tok(full, "amma", "part", ["amma-tafsiliyya"],
        ("الْفَاءُ لِلِاسْتِئْنَافِ" if pre == "فَ" else "الْوَاوُ لِلِاسْتِئْنَافِ") + "، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
        ("The fa opens a new sentence" if pre == "فَ" else "The waw opens a new sentence") + "; أَمَّا «as for» is the particle of condition, detailing and emphasis, built on sukun, with no seat — its answer must take the fa.",
        ("Fâ isti'nâf içindir" if pre == "فَ" else "Vâv isti'nâf içindir") + "; emmâ «…-e gelince»: şart, tafsîl ve te'kîd harfi, sükûn üzere mebnî, mahalli yoktur — cevabı fâ ile bağlanır.",
        segments=[seg(pre, "fa" if pre == "فَ" else "wa", "conj"), seg("أَمَّا", "amma", "part")])
FA_QAD_AMMA = lambda: tok("فَقَدْ", "qad", "part", ["amma-tafsiliyya", "qad-harf"],
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The fa answers أَمَّا; قَدْ affirms the past verb after it.", "Fâ emmâ'nın cevabına gelmiştir; kad tahkîk harfidir.",
    segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")])
HATTA_NASB = lambda: tok("حَتَّى", "hatta", "prep", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari", "ila-hatta-fi-wal-ba-fil-kafiya"],
    "حَرْفُ غَايَةٍ وَجَرٍّ بِمَعْنَى «إِلَى أَنْ»، وَالْفِعْلُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «until» (the limit), a jarr letter after which an unspoken أَنْ must put the verb in nasb; the masdar so built is in jarr by حَتَّى.",
    "Hattâ «-inceye kadar» (gâye), cer harfi; sonraki fiil vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr.")
def FI_ROLE(note):
    return PREP("فِي", "fi", note[0], note[1], note[2], gloss_tr="«-de»")
def MIN_ROLE(note, punct=None):
    return PREP("مِنْ", "min", note[0], note[1], note[2], gloss_tr="«-den»", punct=punct)
def AN_P(note=("", "", "")):
    return PREP("عَنْ", "an", note[0], note[1], note[2], gloss_tr="«hakkında»")

# ============================================ the text ============================================
TITLES = [{"ar": "صَاحِبُ الْمُقَدِّمَةِ", "en": "The Author of the Muqaddima", "tr": "Mukaddime'nin Sahibi"},
          {"ar": "تَيْمُورُ عِنْدَ دِمَشْقَ", "en": "Tīmūr before Damascus", "tr": "Timur Şam Önlerinde"},
          {"ar": "مِنْ فَوْقِ السُّورِ", "en": "From the Top of the Wall", "tr": "Surun Üstünden"},
          {"ar": "مَجَالِسُ الْحَدِيثِ", "en": "Sessions of Talk", "tr": "Sohbet Meclisleri"},
          {"ar": "الرُّجُوعُ إِلَى مِصْرَ", "en": "The Return to Egypt", "tr": "Mısır'a Dönüş"}]

# ---- Chapter 1 — صَاحِبُ الْمُقَدِّمَةِ ----
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Ibn Khaldūn was one of the scholars of the Maghrib: he journeyed to Egypt and settled there, and held the office of judge.",
  "tr": "İbn Haldun Mağrib âlimlerinden biriydi; Mısır'a göç edip oraya yerleşti ve kadılık görevini üstlendi."},
 "tokens": [KANA("كَانَ"), IBN("ismk"), KHALDUN_MI(),
  KHK("عَالِمًا", "alim-scholar"),
  MIN_ROLE(NAAT_OF("عَالِمًا", "a scholar", "âlim")),
  MAJR("عُلَمَاءِ", "alim-scholar", extra=["jam-taksir", "mamnu-min-sarf"], note_ar="، مُضَافٌ — جَمْعُ عَالِمٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ",
       note_en=", annexed — the plural of «scholar»; a diptote (the extended alif of the feminine), it takes kasra here because it is annexed",
       note_tr=", muzâf — âlim'in cem'i; memdûde te'nîs elifi sebebiyle gayr-i munsarif iken muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("الْمَغْرِبِ", "maghrib", punct="،"),
  MADI("رَحَلَ", "rahala", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِـ«عَالِمًا»", note_en="; the clause is a second adjective of «a scholar», in the seat of nasb", note_tr="; cümle «âlim»in ikinci na'tı, mahallen mansûb"),
  ILA(), MISR_J(),
  MADI("فَنَزَلَ", "nazala", hidden=True),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»", note_en=" — the ba here means «in»", note_tr=" — bâ burada «fî» anlamındadır", punct="،"),
  MADI("وَوَلِيَ", "waliya", hidden=True),
  MAFUL("الْقَضَاءَ", "qada", note_ar=" — وَالْقَضَاءُ هُنَا: وِلَايَةُ الْقَاضِي", note_en=" — «judgeship», the office of the judge", note_tr=" — kazâ burada kadılık makamıdır", punct=".")]})
S1.append({"id": "s2", "translation": {
  "en": "Before that he had written a great book of history and made for it an introduction, in which he showed how a state rises, then weakens, then passes away.",
  "tr": "Bundan önce tarih üzerine büyük bir kitap yazmış ve ona bir mukaddime koymuştu; onda bir devletin nasıl kurulduğunu, sonra zayıfladığını, sonra yok olup gittiğini açıklamıştı."},
 "tokens": [KANA_HID("وَكَانَ", note=("، يَعُودُ عَلَى ابْنِ خَلْدُونَ", " (Ibn Khaldūn)", " (İbn Haldun)")), QAD(),
  MADI("كَتَبَ", "kataba", hidden=True, **W(KH_KANA)),
  ZARF("قَبْلَ", "qabla", **ZAMAN), DHALIKA(*DH_MI),
  MAFUL("كِتَابًا", "kitab"), NAAT("كَبِيرًا", "kabir", "nasb"),
  FI_ROLE(NAAT_OF("كِتَابًا", "a book", "kitap", nth=(" ثَانٍ", "second", "ikinci"))),
  MAJR("التَّارِيخِ", "tarikh", punct="،"),
  MADI("جَعَلَ", "jaala", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَالِثٌ لِـ«كِتَابًا»", note_en="; the clause is a third adjective of «a book», in the seat of nasb", note_tr="; cümle «kitap»ın üçüncü na'tı, mahallen mansûb"),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)", note_ar=" — وَالْهَاءُ رَابِطٌ يَعُودُ عَلَى «كِتَابًا»", note_en=" — the pronoun ties the clause back to «a book»", note_tr=" — zamir «kitap»a dönen râbıttır"),
  MAFUL("مُقَدِّمَةً", "muqaddima"),
  MADI("بَيَّنَ", "bayyana", ["form-ii-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«مُقَدِّمَةً»", note_en="; the clause is the adjective of «an introduction», in the seat of nasb", note_tr="; cümle «mukaddime»nin na'tı, mahallen mansûb"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", note_ar=" — وَالْهَاءُ رَابِطٌ يَعُودُ عَلَى «مُقَدِّمَةً»", note_en=" — the pronoun ties the clause back to «an introduction»", note_tr=" — zamir «mukaddime»ye dönen râbıttır"),
  tok("كَيْفَ", "kayfa", "noun", ["al-istifham", "hal"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الدَّوْلَةُ» — وَجُمْلَةُ الِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«بَيَّنَ».",
      "The interrogative noun «how», built on fatha, in the seat of nasb as a hal of «the state» — the whole question fills the seat of nasb as the object of «showed».",
      "İstifhâm ismi «nasıl», fetha üzere mebnî, «devlet»ten hâl olarak mahallen mansûb — soru cümlesinin tamamı «açıkladı»nın mef'ûlü olarak mahallen mansûb."),
  tok("تَقُومُ", "qama", "verb", ["mudari-marfu", "hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالتَّاءُ فِي أَوَّلِهِ لِتَأْنِيثِ الْفَاعِلِ، وَالْفَاعِلُ بَعْدَهُ.",
      "Present verb in raf'; its opening ta marks a feminine doer, and the doer follows.",
      "Merfû muzâri; baştaki tâ fâilin müennes olduğunu gösterir; fâili ondan sonra gelir."),
  FAIL("الدَّوْلَةُ", "dawla", punct="،"),
  THUMMA(), MUDARI_F("تَضْعُفُ", "daufa", note_ar=" — يَعُودُ عَلَى الدَّوْلَةِ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «تَقُومُ»", note_en=" (the state); the clause is conjoined to «rises»", note_tr=" (devlet); cümle «kurulur»a ma'tûf", punct="،"),
  THUMMA(), MUDARI_F("تَذْهَبُ", "dhahaba", note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ كَذٰلِكَ", note_en="; the clause is conjoined likewise", note_tr="; cümle o da ma'tûftur", punct=".")]})
S1.append({"id": "s3", "translation": {
  "en": "And how many a king he had served in the lands of the Maghrib, and then watched his kingdom pass away!",
  "tr": "Mağrib diyarında nice hükümdara hizmet etmiş, sonra onun saltanatının elden gidişini görmüştü!"},
 "tokens": [KAM("وَكَمْ"), KAM_TAMYIZ("مَلِكٍ", "malik-king"),
  ENC_MADI("خَدَمَهُ", "khadama-serve", "هُ", hidden=True, note_ar="، وَالْهَاءُ تَعُودُ عَلَى كَمْ؛ وَلَمْ تُعْرَبْ «كَمْ» مَفْعُولًا مُقَدَّمًا لِـ«خَدَمَ» لِأَنَّ الْفِعْلَ اشْتَغَلَ عَنْهَا بِضَمِيرِهَا" + KH_KAM[0],
       note_en="; the attached pronoun returns to كَمْ — كَمْ is not the fronted object of «served», because the verb is already busy with its pronoun (ishtighāl)" + KH_KAM[1],
       note_tr="; zamir kem'e döner — fiil onun zamiriyle meşgul olduğu için (iştiğâl) kem «hizmet etti»nin öne alınmış mef'ûlü sayılmaz" + KH_KAM[2]),
  FI(), MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUDAF_ILAYH("الْمَغْرِبِ", "maghrib", punct="،"),
  THUMMA(),
  MADI_ALIF("رَأَى", "raa", hidden=True, note_ar=" — وَالرُّؤْيَةُ هُنَا بَصَرِيَّةٌ تَنْصِبُ مَفْعُولًا وَاحِدًا، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «خَدَمَهُ» فَهِيَ مِثْلُهَا فِي مَحَلِّ رَفْعٍ",
       note_en="; «saw» here is the seeing of the eye, with one object — the clause is conjoined to «he served him» and shares its seat of raf'",
       note_tr="; rü'yet burada gözle görmedir, tek mef'ûl alır — cümle «hizmet etti»ye ma'tûf, onun gibi mahallen merfû"),
  ENC_NOUN("مُلْكَهُ", "mulk", "هُ", "maful", note_ar=" — وَالْهَاءُ لِلْمَلِكِ، وَهِيَ الَّتِي تَرْبِطُ الْجُمْلَةَ الْمَعْطُوفَةَ بِكَمْ", note_en=" — «his» is the king's: the pronoun that ties the conjoined clause to كَمْ", note_tr=" — zamir hükümdara döner; ma'tûf cümleyi kem'e bağlayan odur"),
  MUDARI("يَذْهَبُ", "dhahaba", note_ar=" — يَعُودُ عَلَى الْمُلْكِ" + HALCL[0] + " مِنْ «مُلْكَهُ»", note_en=" (the kingdom)" + HALCL[1] + " of «his kingdom»", note_tr=" (saltanat)" + HALCL[2] + " — «saltanatı»ndan", punct="!")]})
S1.append({"id": "s4", "translation": {
  "en": "So he knew the ways of kings as one knows them who has lived among them.",
  "tr": "Bu yüzden hükümdarların hâllerini, onların arasında yaşamış birinin bildiği gibi bilirdi."},
 "tokens": [KANA_HID("فَكَانَ", note=("، يَعُودُ عَلَى ابْنِ خَلْدُونَ", " (Ibn Khaldūn)", " (İbn Haldun)")),
  MUDARI("يَعْرِفُ", "arafa", **W(KH_KANA)),
  MAFUL("أَحْوَالَ", "hal-state", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ حَالٍ", note_en=MUDAF[1] + " — the plural of «state»", note_tr=MUDAF[2] + " — hâl'in cem'i"),
  MUDAF_ILAYH("الْمُلُوكِ", "malik-king", extra=["jam-taksir"]),
  tok("مَعْرِفَةَ", "marifa", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar", "idafa-definiteness"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مَصْدَرُ «عَرَفَ»، وَبِإِضَافَتِهِ يُبَيِّنُ نَوْعَ الْمَعْرِفَةِ.",
      "The absolute object (maf'ul mutlaq), in nasb and annexed — the masdar of «to know»; through its annexation it tells the KIND of knowing («with the knowing of one who …»).",
      "Mef'ûlün mutlak, mansûb, muzâf — «bildi» fiilinin masdarı; izâfetiyle bilmenin TÜRÜNÜ bildirir («… kimsenin bilişiyle»)."),
  MAN_ONE("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"]),
  MADI("عَاشَ", "asha-live", ["hollow-verbs"], hidden=True, **W(SILA_)),
  ZARF_ENC("بَيْنَهُمْ", "bayna", "هُمْ", note_ar=" — وَالضَّمِيرُ لِلْمُلُوكِ", note_en=" — «them» is the kings", note_tr=" — zamir hükümdarlara döner", punct=".")]})
S1.append({"id": "s5", "translation": {
  "en": "Nor did he know that the days would bring him together with one of the greatest kings of his age.",
  "tr": "Günlerin onu, zamanının en büyük hükümdarlarından biriyle bir araya getireceğini bilmiyordu."},
 "tokens": [WA_MA("istinaf"),
  KANA_HID("كَانَ", note=("، يَعُودُ عَلَى ابْنِ خَلْدُونَ", " (Ibn Khaldūn)", " (İbn Haldun)")),
  MUDARI("يَعْلَمُ", "alima", **W(KH_KANA)),
  ANNA_X(SADDA("يَعْلَمُ", "knew", "bilir")),
  tok("الْأَيَّامَ", "yawm", "noun", ["inna-wa-akhawatuha", "jam-taksir"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ يَوْمٍ.", "The noun of أَنَّ, in nasb — the plural of «day».", "Enne'nin ismi, mansûb — yevm'in cem'i."),
  tok("سَتَجْمَعُ", "jamaa-gather", "verb", ["mudari-marfu"],
      "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَتَجْمَعُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى الْأَيَّامِ" + KH_ANNA_CL[0] + ".",
      "The sin points to the future; «will gather» is a present verb in raf' whose doer is the hidden «they» (the days — a broken plural takes a feminine singular pronoun)" + KH_ANNA_CL[1] + ".",
      "Sîn istikbâl harfi; «bir araya getirecek» merfû muzâri, fâili günlere dönen gizli zamir «o» (kırık cem' müfred müennes zamir alır)" + KH_ANNA_CL[2] + ".",
      segments=[seg("سَ", "sa", "part"), seg("تَجْمَعُ", "jamaa-gather", "verb")]),
  ZARF_ENC("بَيْنَهُ", "bayna", "هُ"), WA_BAYNA(),
  MUDAF_ILAYH("مَلِكٍ", "malik-king"),
  MIN_ROLE(NAAT_OF("مَلِكٍ", "a king", "hükümdar", case_ar="جَرٍّ")),
  MAJR("أَعْظَمِ", "azam", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en=", annexed — an elative and a diptote, which takes kasra here because it is annexed", note_tr=", muzâf — gayr-i munsarif ism-i tafdîl; muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("مُلُوكِ", "malik-king", extra=["jam-taksir"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf", punct=".")]})

# ---- Chapter 2 — تَيْمُورُ عِنْدَ دِمَشْقَ ----
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "At the opening of the ninth century (of the Hijra) a king called Tīmūr came out of the East — of all the kings of his age the richest in troops.",
  "tr": "(Hicrî) dokuzuncu asrın başında Doğu'dan Timur denen bir hükümdar çıkageldi; zamanının hükümdarları içinde askeri en çok olan oydu."},
 "tokens": [ISTINAF(PREP("وَفِي", "fi", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَقْبَلَ»", "; the jarr phrase hangs on «came»", "; câr-mecrûr «çıkageldi»ye müteallik", gloss_tr="«-de»")),
  MAJR("أَوَّلِ", "awwal", **W(MUDAF)),
  MUDAF_ILAYH("الْمِائَةِ", "mia", note_ar=" — وَالْمِائَةُ هُنَا: الْقَرْنُ مِنَ الْهِجْرَةِ", note_en=" — «the hundred» here is the century of the Hijra", note_tr=" — mi'e burada hicrî asırdır"),
  NAAT("التَّاسِعَةِ", "tasi", "jarr"),
  MADI("أَقْبَلَ", "aqbala", ["form-iv-verbs"], **W(FAIL_BAAD)),
  MINA(), MAJR("الْمَشْرِقِ", "mashriq"),
  FAIL("مَلِكٌ", "malik-king"),
  tok("يُقَالُ", "qala", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "hollow-verbs", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«مَلِكٌ».",
      "A present verb in the passive, in raf' — the clause qualifies «a king», in the seat of raf'.",
      "Meçhul muzâri, merfû — cümle «hükümdar»ın na'tı, mahallen merfû."),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"),
  TIMUR("naib", punct="،"),
  KANA_HID("وَكَانَ", note=("، يَعُودُ عَلَى تَيْمُورَ", " (Tīmūr)", " (Timur)")),
  KHK("أَكْثَرَ", "akthar", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ عَلَى وَزْنِ أَفْعَلَ", note_en=", annexed — an elative on the أَفْعَل pattern", note_tr=", muzâf — ef'al vezninde ism-i tafdîl"),
  MUDAF_ILAYH("مُلُوكِ", "malik-king", extra=["jam-taksir"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf"),
  TAMYIZ("جُنْدًا", "jund", punct=".")]})
S2.append({"id": "s2", "translation": {
  "en": "He took Aleppo, then marched on Damascus until he encamped before it.",
  "tr": "Halep'i aldı, sonra Şam'a yürüdü ve nihayet onun önüne kondu."},
 "tokens": [MADI("فَأَخَذَ", "akhadha", hidden=True),
  MAFUL("حَلَبَ", "halab", "propn", ["mamnu-min-sarf"], sign="بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=DIPT_F2[0], note_en=", with no tanwin" + DIPT_F2[1], note_tr=", tenvinsiz" + DIPT_F2[2], punct="،"),
  THUMMA(), MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True), ILA(), DIMASHQ("majr"),
  HATTA_IBT(), MADI("نَزَلَ", "nazala", hidden=True),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («onun önüne»)", note_ar=" — وَالضَّمِيرُ لِدِمَشْقَ؛ وَنَزَلَ عَلَى الْمَدِينَةِ: حَطَّ جَيْشَهُ عِنْدَهَا", note_en=" — «it» is Damascus; to «come down upon» a city is to camp before it", note_tr=" — zamir Şam'a döner; şehre «inmek», ordusuyla önüne konmaktır", punct=".")]})
S2.append({"id": "s3", "translation": {
  "en": "The sultan of Egypt went out to Syria with his armies, fearing for it; the judges and the scholars went out with him — and Ibn Khaldūn among them.",
  "tr": "Mısır sultanı Şam diyarı için endişelenerek ordularıyla oraya çıktı; kadılar ve âlimler de onunla birlikte çıktı; İbn Haldun da onların arasındaydı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja", **W(FAIL_BAAD)),
  FAIL("سُلْطَانُ", "sultan", **W(MUDAF)), MISR_J(mi=True),
  BI_NOUN("بِجُيُوشِهِ", "jaysh", "جُيُوشِهِ", enc="هِ", extra=["jam-taksir"], note_ar=" — جَمْعُ جَيْشٍ، وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the plural of «army»; the ba of company («with»)", note_tr=" — ceyş'in cem'i; bâ musâhabe içindir («ile»)"),
  ILA(), MAJR("الشَّامِ", "sham", "propn"),
  MAFUL_LAHU("خَوْفًا", "khawf"),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («onun için»)", note_ar=" — مُتَعَلِّقٌ بِـ«خَوْفًا»، وَالضَّمِيرُ لِلشَّامِ", note_en=" — it hangs on «fearing»; «it» is Syria", note_tr=" — «korku»ya müteallik; zamir Şam diyarına döner", punct="،"),
  MADI("وَخَرَجَ", "kharaja", **W(FAIL_BAAD)),
  MAA_X("مَعَهُ", "هُ"),
  FAIL("الْقُضَاةُ", "qadi", extra=["jam-taksir"], note_ar=" — جَمْعُ قَاضٍ", note_en=" — the plural of «judge»", note_tr=" — kâdî'nin cem'i"),
  ATF("وَالْعُلَمَاءُ", "alim-scholar", "noun", "raf", extra=["jam-taksir"], punct="،"),
  tok("وَفِيهِمُ", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "al-hal-jumla-wa-rabituha", "taqdim-al-musnad"],
      "الْوَاوُ حَالِيَّةٌ، وَفِي حَرْفُ جَرٍّ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
      "The waw opens a hal clause; فِي is a jarr letter and «them» an attached pronoun in the seat of jarr (its mim takes damma where two quiescents meet) — the jarr phrase hangs on the omitted, FRONTED predicate.",
      "Hâl vâvı; fî cer harfi, «onlar» bitişik zamir, mahallen mecrûr (iki sâkin karşılaştığı için mîm damme aldı) — câr-mecrûr öne alınmış mahzûf habere müteallik.",
      segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), seg("هِمُ", "pron-3mp", "pron")]),
  IBN("mubtada_m"), KHALDUN_MI(punct=".")]})
S2.append({"id": "s4", "translation": {
  "en": "They encamped near Damascus, and for some days there was fighting between the two armies.",
  "tr": "Şam'ın yakınına kondular; iki ordu arasında günlerce çarpışma oldu."},
 "tokens": [VERB_WAW("فَنَزَلُوا", "nazala"),
  tok("قَرِيبًا", "qarib", "noun", ["maful-fih", "hadhf-wa-taqdir"],
      "نَائِبٌ عَنْ ظَرْفِ الْمَكَانِ مَنْصُوبٌ بِالْفَتْحَةِ — وَهُوَ صِفَةٌ لِظَرْفٍ مَحْذُوفٍ، أَيْ: مَكَانًا قَرِيبًا.",
      "Standing in for an adverb of place, in nasb — it is the adjective of an omitted adverb («[at a place] near»).",
      "Mekân zarfının nâibi, mansûb — hazfedilmiş bir zarfın sıfatıdır («yakın [bir yer]e»)."),
  MIN(), DIMASHQ("majr", punct="،"),
  MADI_ALIF("وَجَرَى", "jara", **W(FAIL_BAAD)),
  ZARF("بَيْنَ", "bayna"),
  tok("الْجَيْشَيْنِ", "jaysh", "noun", ["al-muthanna", "idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ.",
      "The second term of the idafa, in jarr by the ya because it is a dual; the nun stands for the tanwin of the singular.",
      "Muzâfun ileyh; tesniye olduğu için yâ ile mecrûr; nûn, müfreddeki tenvinin yerini tutar."),
  FAIL("قِتَالٌ", "qital"),
  ZARF("أَيَّامًا", "yawm", mudaf=False, extra=["jam-taksir"], note_ar=" — جَمْعُ يَوْمٍ", note_en=" — the plural of «day»", note_tr=" — yevm'in cem'i", punct=".", **ZAMAN)]})
S2.append({"id": "s5", "translation": {
  "en": "And while the people were waiting to see what would come, all at once the sultan and his emirs went back to Egypt by night.",
  "tr": "İnsanlar ne olacağını beklerken, sultan ve emîrleri ansızın gece vakti Mısır'a geri döndü."},
 "tokens": [BAYNAMA(), MUBTADA("النَّاسُ", "nas"),
  MUDARI5("يَنْتَظِرُونَ", "intazara", ["form-viii-verbs"], role_ar=KH_MUB_CL[0], role_en=KH_MUB_CL[1], role_tr=KH_MUB_CL[2]),
  MA_MAWSULA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"]),
  tok("يَكُونُ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "mudari-marfu", "hollow-verbs"],
      "كَانَ هُنَا تَامَّةٌ بِمَعْنَى «يَحْدُثُ»: فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَفَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى «مَا»، وَلَا خَبَرَ لَهُ" + SILA_[0] + ".",
      "كَانَ here is COMPLETE (tāmma), meaning «to happen»: a present verb in raf' whose doer is the hidden «it», returning to مَا; it takes no predicate" + SILA_[1] + ".",
      "Kâne burada tâmmedir, «olur, meydana gelir» anlamında: merfû muzâri; fâili «mâ»ya dönen gizli zamir «o»; haber almaz" + SILA_[2] + ".", punct="،"),
  IDH_FUJ(), MADI("رَجَعَ", "rajaa", **W(FAIL_BAAD)), FAIL("السُّلْطَانُ", "sultan"),
  tok("وَأُمَرَاؤُهُ", "amir", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
      WA_AR + "أُمَرَاءُ مَعْطُوفٌ عَلَى «السُّلْطَانُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ أَمِيرٍ، وَكُتِبَتْ هَمْزَتُهُ عَلَى الْوَاوِ لِضَمِّهَا.",
      "The waw conjoins; «his emirs» is conjoined to «the sultan», in raf', annexed to the pronoun, which fills the seat of jarr — the plural of «emir», its hamza written on a waw because it carries damma.",
      "Vâv atıf; «emîrleri» «sultan»a ma'tûf, merfû, zamire muzâf; zamir mahallen mecrûr — emîr'in cem'i; hemzesi damme aldığı için vâv üzerine yazılmıştır.",
      segments=[seg("وَ", "wa", "conj"), seg("أُمَرَاؤُ", "amir", "noun"), seg("هُ", "pron-3ms", "pron")]),
  ILA(), MISR_J(), FI(), MAJR("اللَّيْلِ", "layl", punct=".")]})
S2.append({"id": "s6", "translation": {
  "en": "Ibn Khaldūn stayed on in the city with its people, the enemy all around it.",
  "tr": "İbn Haldun şehirde halkıyla birlikte kaldı; düşman ise şehrin etrafını sarmıştı."},
 "tokens": [MADI("وَبَقِيَ", "baqiya", **W(FAIL_BAAD)), IBN("fail"), KHALDUN_MI(),
  FI(), MAJR("الْمَدِينَةِ", "madina"),
  MAA(), ENC_NOUN("أَهْلِهَا", "ahl", "هَا", "mudaf", punct="،"),
  WA_HAL_MUB("وَالْعَدُوُّ", "aduww"),
  ZARF_ENC("حَوْلَهَا", "hawla", "هَا", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", note_en=" — the adverb hangs on the omitted predicate of «the enemy»", note_tr=" — zarf mübtedânın mahzûf haberine müteallik", punct=".")]})

# ---- Chapter 3 — مِنْ فَوْقِ السُّورِ ----
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "After that, nothing was left to the people of Damascus but to ask for a guarantee of safety.",
  "tr": "Bundan sonra Şam halkına emân dilemekten başka bir yol kalmadı."},
 "tokens": [WA_LAM(), YAKUN(),
  LI_AL("لِأَهْلِ", "ahl", "أَهْلِ", note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ يَكُنْ مُقَدَّمٌ", note_en=" and annexed — the jarr phrase is the FRONTED predicate of يَكُنْ", note_tr=", muzâf — câr-mecrûr yekün'ün öne alınmış haberidir"),
  DIMASHQ("mi"),
  ZARF("بَعْدَ", "bada", **ZAMAN), DHALIKA(*DH_MI),
  ILLA_HASR(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ اسْمُ يَكُنْ مُؤَخَّرٌ، وَهُوَ الْمَقْصُورُ عَلَيْهِ", "; the clause it builds is the noun of يَكُنْ, placed last, in the seat of raf' — it is what the statement is restricted TO", "; kurduğu müevvel masdar, sona bırakılmış yekün ismi olarak mahallen merfû — hüküm ona hasredilmiştir"),
  FIVE_NASB("يَطْلُبُوا", "talaba"),
  MAFUL("الْأَمَانَ", "aman", punct=".")]})
S3.append({"id": "s2", "translation": {
  "en": "So its judges and a party of its people went out to Tīmūr, to speak with him about terms.",
  "tr": "Bunun üzerine kadıları ve halkından bir topluluk sulh hakkında konuşmak üzere Timur'un yanına çıktı."},
 "tokens": [MADI("فَخَرَجَ", "kharaja", note_ar=" — وَالْفَاعِلُ «قُضَاتُهَا» بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «its judges» comes after the jarr phrase", note_tr="; fâili «kadıları» câr-mecrûrdan sonra gelir"),
  ILA(), TIMUR("majr"),
  ENC_NOUN("قُضَاتُهَا", "qadi", "هَا", "fail", extra=["jam-taksir"], note_ar=" — جَمْعُ قَاضٍ، وَالضَّمِيرُ لِدِمَشْقَ", note_en=" — the plural of «judge»; «its» is Damascus", note_tr=" — kâdî'nin cem'i; zamir Şam'a döner"),
  ATF("وَجَمَاعَةٌ", "jamaa", "noun", "raf"),
  MIN_ROLE(NAAT_OF("جَمَاعَةٌ", "a party", "topluluk", case_ar="رَفْعٍ")),
  ENC_NOUN("أَهْلِهَا", "ahl", "هَا", "majr", punct="،"),
  tok("يُكَلِّمُونَهُ", "kallama", "verb", ["afal-khamsa", "mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "form-ii-verbs", "hal"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْفَاعِلِ، وَهِيَ حَالٌ مُقَدَّرَةٌ: خَرَجُوا قَاصِدِينَ كَلَامَهُ.",
      "One of the five verbs, in raf' by the kept nun; the waw is its doer and the attached «him» its object, in the seat of nasb — the clause is a hal of the doer, in the seat of nasb: an ANTICIPATED hal («went out meaning to speak with him»).",
      "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâil, bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle fâilden hâl, mahallen mansûb: mukadder hâldir («onunla konuşmak üzere çıktılar»).",
      segments=[seg("يُكَلِّمُونَ", "kallama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  FI(), MAJR("الصُّلْحِ", "sulh", punct=".")]})
S3.append({"id": "s3", "translation": {
  "en": "So when Ibn Khaldūn saw what had come down upon the people of the city, and learned that its judges had gone out to Tīmūr, he went out to the wall at daybreak, and was let down from the top of it by a rope, until he reached the ground.",
  "tr": "İbn Haldun şehir halkının başına geleni görüp kadılarının Timur'a çıktığını öğrenince, sabahleyin sura gitti; surun üstünden bir iple aşağı indirildi ve nihayet yere ulaştı."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI_ALIF("رَأَى", "raa", note_ar=FAIL_BAAD[0] + LAMMA_CL[0], note_en=FAIL_BAAD[1] + LAMMA_CL[1], note_tr=FAIL_BAAD[2] + LAMMA_CL[2]),
  IBN("fail"), KHALDUN_MI(),
  MA_MAWSULA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"]),
  MADI("نَزَلَ", "nazala", hidden=True, note_ar="، يَعُودُ عَلَى «مَا»" + SILA_[0], note_en=", returning to مَا" + SILA_[1], note_tr=", «mâ»ya döner" + SILA_[2]),
  BI_NOUN("بِأَهْلِ", "ahl", "أَهْلِ", note_ar="، مُضَافٌ — نَزَلَ بِهِمُ الْأَمْرُ: أَصَابَهُمْ", note_en="; it is annexed — a thing «comes down upon» people when it befalls them", note_tr="; muzâf — bir işin birilerine «inmesi», onların başına gelmesidir"),
  MUDAF_ILAYH("الْمَدِينَةِ", "madina", punct="،"),
  MADI("وَعَلِمَ", "alima", hidden=True, note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «رَأَى» فِي حَيِّزِ لَمَّا", note_en="; the clause is conjoined to «saw», still under لَمَّا", note_tr="; cümle «gördü»ye ma'tûf, lemmâ'nın kapsamındadır"),
  ANNA_X(SADDA("عَلِمَ", "learned", "öğrendi")),
  ISM_ANNA_ENC("قُضَاتَهَا", "qadi", "هَا", extra=["jam-taksir"]),
  QAD(), VERB_WAW("خَرَجُوا", "kharaja", **W(KH_ANNA_CL)),
  ILA(), TIMUR("majr", punct="،"),
  MADI("خَرَجَ", "kharaja", hidden=True, **W(JAWAB_LAMMA)),
  FI(), MAJR("الصُّبْحِ", "subh"), ILA(), MAJR("السُّورِ", "sur-wall", punct="،"),
  MAJHUL("فَأُنْزِلَ", "anzala", ["form-iv-verbs"], **W(NAIB_HID)),
  MIN(), ENC_NOUN("فَوْقِهِ", "fawqa", "هِ", "majr", note_ar=" — ظَرْفٌ جُرَّ بِمِنْ، وَالْهَاءُ لِلسُّورِ", note_en=" — an adverb drawn into jarr by مِنْ; «it» is the wall", note_tr=" — min ile mecrûr olmuş zarf; zamir sura döner"),
  BI_NOUN("بِحَبْلٍ", "habl", "حَبْلٍ", note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ", note_en=" — the ba of the instrument («by means of»)", note_tr=" — bâ isti'âne içindir («ile»)"),
  HATTA_IBT(), MADI("بَلَغَ", "balagha", hidden=True), MAFUL("الْأَرْضَ", "ard", punct=".")]})
S3.append({"id": "s4", "translation": {
  "en": "At the gate he found some of Tīmūr's men, and they took him to him.",
  "tr": "Kapının önünde Timur'un adamlarından bir topluluk buldu; onu Timur'a götürdüler."},
 "tokens": [MADI("فَوَجَدَ", "wajada", hidden=True),
  ZARF("عِنْدَ", "inda"), MUDAF_ILAYH("الْبَابِ", "bab"),
  MAFUL("قَوْمًا", "qawm"),
  MIN_ROLE(NAAT_OF("قَوْمًا", "some men", "topluluk")),
  MAJR("أَصْحَابِ", "sahib", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ صَاحِبٍ", note_en=MUDAF[1] + " — the plural of «companion»", note_tr=MUDAF[2] + " — sâhib'in cem'i"),
  TIMUR("mi", punct="،"),
  VERB_WAW("فَذَهَبُوا", "dhahaba"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onu»)", note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ: ذَهَبُوا بِهِ، أَيْ: أَخَذُوهُ مَعَهُمْ", note_en=" — the ba makes the verb transitive: «went with him», i.e. took him along", note_tr=" — bâ ta'diye içindir: «onunla gittiler», yani onu götürdüler"),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)", note_ar=" — وَالضَّمِيرُ لِتَيْمُورَ", note_en=" — «him» is Tīmūr", note_tr=" — zamir Timur'a döner", punct=".")]})
S3.append({"id": "s5", "translation": {
  "en": "By my life, it was a strange thing: an old man of learning going out to a king whom people feared.",
  "tr": "Ömrüme andolsun, bu şaşılacak bir işti: ilim ehlinden yaşlı bir adam, insanların korktuğu bir hükümdarın huzuruna çıkıyordu."},
 "tokens": [LAAMRI(), LAQAD(), KANA("كَانَ"),
  DHALIKA("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi", extra=["kana-wa-akhawatuha"]),
  KHK("أَمْرًا", "amr-noun"), NAAT("عَجِيبًا", "ajib", "nasb", punct=":"),
  MUBTADA("شَيْخٌ", "shaykh", note_ar=" — نَكِرَةٌ سَوَّغَ الِابْتِدَاءَ بِهَا وَصْفُهَا، وَالْجُمْلَةُ مُسْتَأْنَفَةٌ تُفَسِّرُ ذٰلِكَ الْأَمْرَ لَا مَحَلَّ لَهَا",
          note_en=" — an indefinite noun, allowed to open the clause because it is described; the clause explains «that thing» and has no seat",
          note_tr=" — nekre; sıfatlandığı için mübtedâ olabilmiştir; cümle «o iş»i açıklayan müste'nef cümledir, mahalli yoktur"),
  MIN_ROLE(NAAT_OF("شَيْخٌ", "an old man", "yaşlı adam", case_ar="رَفْعٍ")),
  MAJR("أَهْلِ", "ahl", **W(MUDAF)), MUDAF_ILAYH("الْعِلْمِ", "ilm"),
  MUDARI("يَخْرُجُ", "kharaja", **W(KH_MUB_CL)),
  ILA(), MAJR("مَلِكٍ", "malik-king"),
  tok("يَخَافُهُ", "khafa", "verb", ["mudari-marfu", "hollow-verbs", "al-bariz-al-muttasil", "maful-bihi", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَهِيَ الرَّابِطُ الْعَائِدُ عَلَى «مَلِكٍ»، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«مَلِكٍ».",
      "Present verb in raf'; the attached «him» is its object, in the seat of nasb — the pronoun that ties the clause back to «a king»; its doer follows — the clause qualifies «a king», in the seat of jarr.",
      "Merfû muzâri; bitişik «ondan» mef'ûlün bih, mahallen mansûb — cümleyi «hükümdar»a bağlayan râbıt odur; fâili ondan sonra gelir — cümle «hükümdar»ın na'tı, mahallen mecrûr.",
      segments=[seg("يَخَافُ", "khafa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  FAIL("النَّاسُ", "nas", punct=".")]})
S3.append({"id": "s6", "translation": {
  "en": "When Tīmūr learned that he had come, he gave him leave to enter his presence.",
  "tr": "Timur onun geldiğini öğrenince huzuruna girmesine izin verdi."},
 "tokens": [LAMMA2("وَلَمَّا"),
  MADI("عَلِمَ", "alima", **W(FAIL_BAAD, LAMMA_CL)), TIMUR("fail"),
  BI_NOUN("بِمَجِيئِهِ", "maji", "مَجِيئِهِ", enc="هِ", extra=["masdar"], note_ar=" — مَصْدَرُ جَاءَ", note_en=" — the masdar of «to come»", note_tr=" — câe'nin masdarı"),
  MADI("أَذِنَ", "adhina", hidden=True, **W(JAWAB_LAMMA)),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"),
  FI(), MAJR("الدُّخُولِ", "dukhul"),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («yanına»)", note_ar=" — مُتَعَلِّقٌ بِـ«الدُّخُولِ»", note_en=" — it hangs on «entering» («to go in upon him»)", note_tr=" — «girme»ye müteallik", punct=".")]})

# ---- Chapter 4 — مَجَالِسُ الْحَدِيثِ ----
TANAZU = ("تَنَازَعَ الْفِعْلَانِ «اسْتَقْبَلَهُ» وَ«أَكْرَمَهُ» الْفَاعِلَ «تَيْمُورُ»، فَأُعْمِلَ فِيهِ الثَّانِي لِقُرْبِهِ عَلَى مَذْهَبِ الْبَصْرِيِّينَ، وَأُضْمِرَ فَاعِلُ الْأَوَّلِ",
          "the two verbs «received him» and «honoured him» contend for the one doer «Tīmūr» (tanāzuʿ): on the Basran view the NEARER verb governs it, and the first takes its pronoun",
          "«onu karşıladı» ve «ona ikram etti» fiilleri tek fâil «Timur» için çekişir (tenâzu): Basra görüşüne göre YAKIN fiil onda amel eder, ilki onun zamirini alır")
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "When he came in to him, Tīmūr received him and honoured him.",
  "tr": "Huzuruna girince Timur onu karşıladı ve ona ikram etti."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI("دَخَلَ", "dakhala", hidden=True, **W(LAMMA_CL)),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («yanına»)", punct="،"),
  ENC_MADI("اسْتَقْبَلَهُ", "istaqbala", "هُ", ["form-x-verbs", "tanazu"], hidden=True,
       note_ar=" — وَالْفَاعِلُ الْمُسْتَتِرُ يَعُودُ عَلَى «تَيْمُورُ» الْمُتَأَخِّرِ لَفْظًا؛ " + TANAZU[0] + JAWAB_LAMMA[0],
       note_en=" — the hidden doer returns to «Tīmūr», which comes later in the words; " + TANAZU[1] + JAWAB_LAMMA[1],
       note_tr=" — gizli fâil lafızda sonra gelen «Timur»a döner; " + TANAZU[2] + JAWAB_LAMMA[2]),
  ENC_MADI("وَأَكْرَمَهُ", "akrama", "هُ", ["form-iv-verbs", "tanazu"],
       note_ar=FAIL_BAAD[0] + " — وَهُوَ الْفِعْلُ الثَّانِي الَّذِي أُعْمِلَ فِي الِاسْمِ الْمُتَنَازَعِ فِيهِ",
       note_en=FAIL_BAAD[1] + " — this is the second verb, the one that governs the contested noun",
       note_tr=FAIL_BAAD[2] + " — çekişilen isimde amel eden ikinci fiil budur"),
  TIMUR("fail", punct=".", note=(" — وَهُوَ فَاعِلُ «أَكْرَمَهُ»، وَلِـ«اسْتَقْبَلَهُ» ضَمِيرُهُ", "; it is the doer of «honoured him», and «received him» has its pronoun", "; «ikram etti»nin fâilidir, «karşıladı» ise onun zamirini alır")),
 ]})
S4[-1]["tokens"][-1]["grammar"].append("tanazu")
S4.append({"id": "s2", "translation": {
  "en": "Then he asked him about the lands of the Maghrib — about its cities, its people and its kings.",
  "tr": "Sonra ona Mağrib diyarını sordu: şehirlerini, halkını ve hükümdarlarını."},
 "tokens": [THUMMA(),
  ENC_MADI("سَأَلَهُ", "saala", "هُ", hidden=True, note_ar=" — وَالْفَاعِلُ الْمُسْتَتِرُ لِتَيْمُورَ، وَالْهَاءُ لِابْنِ خَلْدُونَ", note_en=" — the hidden doer is Tīmūr, the «him» Ibn Khaldūn", note_tr=" — gizli fâil Timur, zamir İbn Haldun"),
  AN_P(), MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUDAF_ILAYH("الْمَغْرِبِ", "maghrib", punct=":"),
  TAG(AN_P((" — وَالْجَارُّ وَالْمَجْرُورُ بَدَلٌ مِنْ «عَنْ بِلَادِ الْمَغْرِبِ» بِإِعَادَةِ الْجَارِّ، بَدَلُ بَعْضٍ مِنْ كُلٍّ", "; the jarr phrase is a badal of «about the lands of the Maghrib», the letter repeated — a badal of the part for the whole", "; câr-mecrûr, harf tekrarlanarak «Mağrib diyarı hakkında»dan bedeldir — bedel-i ba'z min kül")), "badal"),
  ENC_NOUN("مُدُنِهَا", "madina", "هَا", "majr", extra=["jam-taksir"], note_ar=" — جَمْعُ مَدِينَةٍ، وَالضَّمِيرُ لِبِلَادِ الْمَغْرِبِ", note_en=" — the plural of «city»; «its» is the lands of the Maghrib", note_tr=" — medîne'nin cem'i; zamir Mağrib diyarına döner"),
  ATF_ENC("وَأَهْلِهَا", "ahl", "هَا"),
  ATF_ENC("وَمُلُوكِهَا", "malik-king", "هَا", extra=["jam-taksir"], note=(" — جَمْعُ مَلِكٍ", " — the plural of «king»", " — melik'in cem'i"), punct=".")]})
S4.append({"id": "s3", "translation": {
  "en": "And Ibn Khaldūn answered him on everything he asked about.",
  "tr": "İbn Haldun da onun sorduğu her şeye cevap veriyordu."},
 "tokens": [KANA("وَكَانَ"), IBN("ismk"), KHALDUN_MI(),
  MUDARI("يُجِيبُهُ", "ajaba", ["form-iv-verbs", "hollow-verbs"], enc="هُ", **W(KH_KANA)),
  AN_P(), MAJR("كُلِّ", "kull", **W(MUDAF)),
  MA_MAWSULA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"]),
  MADI("سَأَلَ", "saala", hidden=True, **W(SILA_)),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («onu»)", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en=" — the pronoun is the one that returns to the relative", note_tr=" — zamir mevsûle dönen râbıttır", punct=".")]})
S4.append({"id": "s4", "translation": {
  "en": "Their talk, though, passed only through an interpreter.",
  "tr": "Aralarındaki konuşma ise ancak bir tercüman aracılığıyla oluyordu."},
 "tokens": [WA_INNAMA("وَإِنَّمَا"), KANA("كَانَ"),
  ISMK("الْكَلَامُ", "kalam"),
  ZARF_ENC("بَيْنَهُمَا", "bayna", "هُمَا", note_ar=" — مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْكَلَامُ»", note_en=" — it hangs on an omitted hal of «the talk»", note_tr=" — «konuşma»dan mahzûf bir hâle müteallik"),
  BI_NOUN("بِتَرْجُمَانٍ", "tarjuman", "تَرْجُمَانٍ", note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ، وَهُوَ الْمَقْصُورُ عَلَيْهِ",
          note_en=" — the ba of the means; the jarr phrase hangs on the omitted predicate of كَانَ, and it is what the statement is restricted TO",
          note_tr=" — bâ isti'âne içindir; câr-mecrûr kâne'nin mahzûf haberine müteallik — hüküm ona hasredilmiştir", punct=".")]})
S4.append({"id": "s5", "translation": {
  "en": "Ibn Khaldūn stayed with him some days, sitting with him in many sessions in which the two of them talked of history and the reports of kings.",
  "tr": "İbn Haldun günlerce onun yanında kaldı; pek çok mecliste onunla oturuyor, bu meclislerde ikisi tarih ve hükümdarların haberleri üzerine konuşuyorlardı."},
 "tokens": [MADI("وَبَقِيَ", "baqiya", **W(FAIL_BAAD)), IBN("fail"), KHALDUN_MI(),
  ZARF_ENC("عِنْدَهُ", "inda", "هُ"),
  ZARF("أَيَّامًا", "yawm", mudaf=False, extra=["jam-taksir"], punct="،", **ZAMAN),
  MUDARI("يَجْلِسُ", "jalasa", **W(HALCL)),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («onunla»)", note_ar=" — جَلَسَ إِلَيْهِ: جَالَسَهُ", note_en=" — to «sit to» someone is to keep him company", note_tr=" — «ona oturmak», onunla oturup sohbet etmektir"),
  FI(),
  MAJR("مَجَالِسَ", "majlis", extra=["jam-taksir", "mamnu-min-sarf"], sign=FATHA_JARR, note_ar=" — جَمْعُ مَجْلِسٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=" — the plural of «session» on the pattern of the farthest plurals, a diptote", note_tr=" — meclis'in cem'i; müntehe'l-cumû' sîgasında, gayr-i munsarif"),
  NAAT("كَثِيرَةٍ", "kathir", "jarr"),
  DUAL_MUDARI("يَتَحَدَّثَانِ", "tahaddatha", (" — وَالْأَلِفُ لِابْنِ خَلْدُونَ وَتَيْمُورَ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِـ«مَجَالِسَ»", "; the two are Ibn Khaldūn and Tīmūr — the clause is a second adjective of «sessions», in the seat of jarr", "; elif İbn Haldun ile Timur'dur — cümle «meclisler»in ikinci na'tı, mahallen mecrûr"), extra=["form-v-verbs", "jumla-sifa"]),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onlarda»)", note_ar=" — وَالْهَاءُ رَابِطٌ يَعُودُ عَلَى «مَجَالِسَ»", note_en=" — the pronoun ties the clause back to «sessions»", note_tr=" — zamir «meclisler»e dönen râbıttır"),
  AN_KASRA(), MAJR("التَّارِيخِ", "tarikh"),
  ATF("وَأَخْبَارِ", "khabar", "noun", "jarr", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ خَبَرٍ", note_en=MUDAF[1] + " — the plural of «report»", note_tr=MUDAF[2] + " — haber'in cem'i"),
  MUDAF_ILAYH("الْمُلُوكِ", "malik-king", extra=["jam-taksir"], punct=".")]})
S4.append({"id": "s6", "translation": {
  "en": "On one of those days he brought him a gift, and he accepted it from him.",
  "tr": "O günlerin birinde ona bir hediye götürdü; o da hediyeyi ondan kabul etti."},
 "tokens": [MADI("وَحَمَلَ", "hamala", hidden=True, note_ar="، يَعُودُ عَلَى ابْنِ خَلْدُونَ", note_en=" (Ibn Khaldūn)", note_tr=" (İbn Haldun)"),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)"),
  FI(), MAJR("بَعْضِ", "bad", **W(MUDAF)), TILKA(*DH_MI),
  BADAL("الْأَيَّامِ", "yawm", "jarr", extra=["jam-taksir"]),
  MAFUL("هَدِيَّةً", "hadiyya", punct="،"),
  ENC_MADI("فَقَبِلَهَا", "qabila", "هَا", hidden=True, note_ar=" — وَالْفَاعِلُ الْمُسْتَتِرُ لِتَيْمُورَ، وَالْهَاءُ لِلْهَدِيَّةِ", note_en=" — the hidden doer is Tīmūr, «it» the gift", note_tr=" — gizli fâil Timur, zamir hediye"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", punct=".")]})

# ---- Chapter 5 — الرُّجُوعُ إِلَى مِصْرَ ----
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Then he asked Tīmūr's leave to return to Egypt; he granted it, and he left Syria and travelled on until he reached Egypt.",
  "tr": "Sonra Timur'dan Mısır'a dönmek için izin istedi; Timur izin verdi; o da Şam diyarından çıktı ve nihayet Mısır'a ulaştı."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  MADI("اسْتَأْذَنَ", "istadhana", ["form-x-verbs"], hidden=True, **W(KH_INNA_CL)),
  TIMUR("maful"),
  FI(), MAJR("الرُّجُوعِ", "rujuu"), ILA(), MISR_J(punct="،"),
  MADI("فَأَذِنَ", "adhina", hidden=True, note_ar="، يَعُودُ عَلَى تَيْمُورَ", note_en=" (Tīmūr)", note_tr=" (Timur)"),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)", punct="،"),
  MADI("فَخَرَجَ", "kharaja", hidden=True, note_ar="، يَعُودُ عَلَى ابْنِ خَلْدُونَ", note_en=" (Ibn Khaldūn)", note_tr=" (İbn Haldun)"),
  MINA(), MAJR("الشَّامِ", "sham", "propn"),
  HATTA_IBT(), MADI("بَلَغَ", "balagha", hidden=True),
  MAFUL("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign="بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=DIPT_LAND[0], note_en=", with no tanwin" + DIPT_LAND[1], note_tr=", tenvinsiz" + DIPT_LAND[2], punct=".")]})
S5.append({"id": "s2", "translation": {
  "en": "As for Damascus, a great calamity befell it after that.",
  "tr": "Şam'a gelince, bundan sonra onu büyük bir felaket vurdu."},
 "tokens": [FA_AMMA("وَأَمَّا"), DIMASHQ("mubtada"), FA_QAD_AMMA(),
  ENC_MADI("أَصَابَهَا", "asaba", "هَا", ["form-iv-verbs", "hollow-verbs"], note_ar=FAIL_BAAD[0] + KH_AMMA[0], note_en=FAIL_BAAD[1] + KH_AMMA[1], note_tr=FAIL_BAAD[2] + KH_AMMA[2]),
  ZARF("بَعْدَ", "bada", **ZAMAN), DHALIKA(*DH_MI),
  FAIL("بَلَاءٌ", "bala"), NAAT("عَظِيمٌ", "azim", "raf", punct=".")]})
S5.append({"id": "s3", "translation": {
  "en": "Ibn Khaldūn remained in Egypt until he died there a few years later.",
  "tr": "İbn Haldun Mısır'da kaldı ve birkaç yıl sonra orada vefat etti."},
 "tokens": [MADI("وَبَقِيَ", "baqiya", **W(FAIL_BAAD)), IBN("fail"), KHALDUN_MI(),
  BI_NOUN("بِمِصْرَ", "misr", "مِصْرَ", pos="propn", sign=FATHA_JARR, extra=["mamnu-min-sarf"], note_ar=DIPT_LAND[0] + " — وَالْبَاءُ بِمَعْنَى «فِي»", note_en=DIPT_LAND[1] + "; the ba here means «in»", note_tr=DIPT_LAND[2] + "; bâ burada «fî» anlamındadır"),
  HATTA_IBT(), MADI("مَاتَ", "mata-die", ["hollow-verbs"], hidden=True),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)"),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  tok("سِنِينَ", "sana", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — جَمْعُ سَنَةٍ.",
      "The second term of the idafa, in jarr by the ya — it is declined like the sound masculine plural (the plural of «year»).",
      "Muzâfun ileyh; cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr — sene'nin cem'i."),
  NAAT("قَلِيلَةٍ", "qalil", "jarr", note_ar=" — وَأُنِّثَ لِأَنَّ مَنْعُوتَهُ جَمْعٌ لِغَيْرِ الْعَاقِلِ", note_en=" — feminine, because the noun it describes is a plural of things", note_tr=" — mevsûfu akılsızların cem'i olduğu için müennes geldi", punct=".")]})
S5.append({"id": "s4", "translation": {
  "en": "In his Muqaddima he had held that a state has a life like the life of a man: it grows strong in its beginnings, then weakens until it passes away.",
  "tr": "Mukaddime'sinde devletin de insanınki gibi bir ömrü olduğu görüşündeydi: başlangıcında güçlenir, sonra zayıflar, nihayet yok olup gider."},
 "tokens": [KANA_HID("وَكَانَ", note=("، يَعُودُ عَلَى ابْنِ خَلْدُونَ", " (Ibn Khaldūn)", " (İbn Haldun)")),
  MUDARI("يَرَى", "raa", naqis="ا", note_ar=" — وَالرُّؤْيَةُ هُنَا قَلْبِيَّةٌ بِمَعْنَى الِاعْتِقَادِ" + KH_KANA[0], note_en=" — «see» here is the seeing of the mind: to hold a view" + KH_KANA[1], note_tr=" — rü'yet burada kalbîdir, «kanaatinde olmak» anlamında" + KH_KANA[2]),
  FI(), ENC_NOUN("مُقَدِّمَتِهِ", "muqaddima", "هِ", "majr"),
  ANNA_X(SADDA("يَرَى", "held", "görür")),
  LI_AL("لِلدَّوْلَةِ", "dawla", "الدَّوْلَةِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ أَنَّ مُقَدَّمٌ", note_en=" — the jarr phrase is the FRONTED predicate of أَنَّ", note_tr=" — câr-mecrûr enne'nin öne alınmış haberidir"),
  tok("عُمْرًا", "umr", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, placed after its predicate, in nasb.", "Enne'nin haberinden sonraya bırakılmış ismi, mansûb."),
  tok("كَعُمْرِ", "ka", "prep", ["huruf-jarr", "idafa-definiteness"],
      "الْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَعُمْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«عُمْرًا».",
      "The kaf of likening is a jarr letter; «life» after it is in jarr and annexed — the jarr phrase hangs on an omitted adjective of «a life».",
      "Teşbih kâfı cer harfi; «ömür» mecrûr, muzâf — câr-mecrûr «ömür»ün mahzûf na'tına müteallik.",
      segments=[seg("كَ", "ka", "prep"), seg("عُمْرِ", "umr", "noun")]),
  MUDAF_ILAYH("الْإِنْسَانِ", "insan", punct=":"),
  MUDARI("تَقْوَى", "qawiya", who="هِيَ", naqis="ا", note_ar=" — يَعُودُ عَلَى الدَّوْلَةِ، وَالْجُمْلَةُ مُسْتَأْنَفَةٌ تُبَيِّنُ ذٰلِكَ الْعُمْرَ لَا مَحَلَّ لَهَا", note_en=" (the state); the clause opens afresh to explain that life and has no seat", note_tr=" (devlet); cümle o ömrü açıklayan müste'nef cümledir, mahalli yoktur"),
  FI(), MAJR("أَوَّلِ", "awwal", **W(MUDAF)), ENC_NOUN("أَمْرِهَا", "amr-noun", "هَا", "mudaf", punct="،"),
  THUMMA(), MUDARI("تَضْعُفُ", "daufa", who="هِيَ"),
  HATTA_NASB(),
  MANSUB_AN("تَذْهَبَ", "dhahaba", who="هِيَ", by="أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", punct=".")]})
S5[-1]["tokens"][-1]["irab"]["en"] = S5[-1]["tokens"][-1]["irab"]["en"].replace("in nasb by أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", "in nasb by the unspoken أَنْ after حَتَّى")
S5[-1]["tokens"][-1]["irab"]["tr"] = S5[-1]["tokens"][-1]["irab"]["tr"].replace("أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى ile mansûb", "hattâ'dan sonra gizli en ile mansûb")
S5.append({"id": "s5", "translation": {
  "en": "Only one who has read his Muqaddima knows the full worth of this story.",
  "tr": "Bu haberin değerini ancak onun Mukaddime'sini okuyan bilir."},
 "tokens": [WA_INNAMA("وَإِنَّمَا"),
  tok("يَعْرِفُ", "arafa", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ «مَنْ» الْمُؤَخَّرُ.", "Present verb in raf'; its doer is the مَنْ that comes last.", "Merfû muzâri; fâili sona bırakılan «men»dir."),
  MAFUL("قَدْرَ", "qadr", **W(MUDAF)),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A demonstrative «this», built on sukun, in the seat of jarr as the second term of the idafa.", "İşaret ismi «bu», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  BADAL("الْخَبَرِ", "khabar", "jarr"),
  MAN_ONE("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail", "qasr"], note=(" — وَهُوَ الْمَقْصُورُ عَلَيْهِ", "; it is what the statement is restricted TO", "; hüküm ona hasredilmiştir")),
  MADI("قَرَأَ", "qaraa", hidden=True, **W(SILA_)),
  ENC_NOUN("مُقَدِّمَتَهُ", "muqaddima", "هُ", "maful", punct=".")]})
S5.append({"id": "s6", "translation": {
  "en": "So the author of the Muqaddima, who wrote of the rise of the state and its fall, had seen with his own eyes one of the days on which history turns.",
  "tr": "Böylece devletin kuruluşunu ve yıkılışını yazan Mukaddime sahibi, tarihin yön değiştirdiği günlerden birini kendi gözüyle görmüştü."},
 "tokens": [tok("فَصَاحِبُ", "sahib", "noun", ["mubtada-khabar", "idafa-definiteness"],
      "الْفَاءُ لِلِاسْتِئْنَافِ، وَصَاحِبُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The fa opens the closing word; «the author» is the mubtada, in raf', annexed.", "Fâ isti'nâf içindir; «sahip» mübtedâ, merfû, muzâf.",
      segments=[seg("فَ", "fa", "conj"), seg("صَاحِبُ", "sahib", "noun")]),
  MUDAF_ILAYH("الْمُقَدِّمَةِ", "muqaddima", punct="،"),
  ALLADHI("raf", "لِـ«صَاحِبُ»", "the author", "sahip"),
  MADI("كَتَبَ", "kataba", hidden=True, **W(SILA_)),
  FI(), MAJR("قِيَامِ", "qiyam", **W(MUDAF)), MUDAF_ILAYH("الدَّوْلَةِ", "dawla"),
  ATF_ENC("وَسُقُوطِهَا", "suqut", "هَا", punct="،"),
  QAD(), MADI_ALIF("رَأَى", "raa", hidden=True, **W(KH_MUB_CL)),
  BI_NOUN("بِعَيْنِهِ", "ayn-eye", "عَيْنِهِ", enc="هِ"),
  MAFUL("يَوْمًا", "yawm"),
  NOTE(MINA(), *NAAT_OF("يَوْمًا", "a day", "gün")),
  MAJR("الْأَيَّامِ", "yawm", extra=["jam-taksir"]),
  ALLATI("jarr", "لِـ«الْأَيَّامِ»", "the days", "günler"),
  tok("يَتَحَوَّلُ", "tahawwala", "verb", ["mudari-marfu", "form-v-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ" + SILA_[0] + ".", "Present verb in raf'; its doer follows" + SILA_[1] + ".", "Merfû muzâri; fâili ondan sonra gelir" + SILA_[2] + "."),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onlarda»)", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en=" — the pronoun is the one that returns to the relative", note_tr=" — zamir mevsûle dönen râbıttır"),
  FAIL("التَّارِيخُ", "tarikh", punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            if DERIVED & set(t.get("grammar", [])) and "thulathi-mujarrad-babs" in t["grammar"]:
                t["grammar"].remove("thulathi-mujarrad-babs")

# ---- the lexicon: every key by lemma identity from the shelf; the entries below are new -----------------------------------
PREF = ["al-kafiya", "al-amana-wa-al-khashaba", "ashab-al-ghar", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "wasiyyat-abi-yusuf-l5", "adam-wa-iblis",
        "al-asad-wa-al-far", "al-asad-wa-al-arnab", "juha-wa-al-himar", "aqaid-ahl-al-sunna", "talkhis-al-miftah", "qisas-al-nabiyyin-2",
        "salah-al-din-wa-al-quds", "fath-al-qustantiniyya", "alb-arslan-wa-malazgird"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
# the packages staged beside this one (parallel authors) count as shelf for the global-key check
PREF += sorted(d.name for d in OUT_ROOT.iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG) if OUT_ROOT != ROOT / "content/samples" else []
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
# where the shelf holds one lemma under one key in several packages, take the entry whose gloss fits this story
FORCE = {"man-mawsula": "talkhis-al-miftah", "ma-mawsula": "al-asad-wa-al-arnab", "bad": "alb-arslan-wa-malazgird", "hadha": "talkhis-al-miftah",
         "jund": "alb-arslan-wa-malazgird", "kathir": "salah-al-din-wa-al-quds", "qital": "salah-al-din-wa-al-quds", "sulh": "salah-al-din-wa-al-quds",
         "jaysh": "salah-al-din-wa-al-quds", "sultan": "alb-arslan-wa-malazgird", "bilad": "alb-arslan-wa-malazgird", "khabar": "tariq-ibn-ziyad",
         "nas": "salah-al-din-wa-al-quds", "ahl": "salah-al-din-wa-al-quds", "sana": "salah-al-din-wa-al-quds", "madina": "salah-al-din-wa-al-quds",
         "an": "abu-hanifa-wa-al-safina", "raa": "wasiyyat-abi-yusuf-l5", "dakhala": "wasiyyat-abi-yusuf-l5", "kalam": "wasiyyat-abi-yusuf-l5",
         "qadr": "wasiyyat-abi-yusuf-l5", "ibn": "talkhis-al-miftah", "dhalika": "talkhis-al-miftah", "kitab": "al-bukhari-fi-baghdad", "alim-scholar": "abu-hanifa-wa-al-safina", "qadi": "al-kafiya", "amir": "tariq-ibn-ziyad"}
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

def PHRASE(lemma, lvl, g_en, g_tr, l_en, l_tr, n_en, n_tr):
    return {"lemma": lemma, "pos": "phrase", "level": lvl, "gloss": {"en": g_en, "tr": g_tr}, "literal": {"en": l_en, "tr": l_tr}, "note": {"en": n_en, "tr": n_tr}}
NEW_GLOSS = {
 "timur": {"lemma": "تَيْمُور", "pos": "propn", "gloss": {"en": "Tīmūr (Tamerlane, d. 807 / 1405), the conqueror from Central Asia; a diptote (a proper name of foreign origin: ʿalamiyya + ʿujma)", "tr": "Timur (ö. 807 / 1405), Orta Asyalı fatih; gayr-i munsarif (yabancı asıllı özel isim: alemiyet + ucmet)"}, "level": 6},
 "dimashq": {"lemma": "دِمَشْق", "pos": "propn", "gloss": {"en": "Damascus — the chief city of Syria (a diptote: a feminine proper name)", "tr": "Şam (Dımaşk) — Suriye'nin başşehri (gayr-i munsarif: müennes özel isim)"}, "level": 4},
 "khaldun": {"lemma": "خَلْدُون", "pos": "propn", "gloss": {"en": "Khaldūn — the forefather after whom the family of Ibn Khaldūn was named; read in its usual vowelling as a diptote (ابْنُ خَلْدُونَ), though some decline it", "tr": "Haldûn — İbn Haldun ailesinin adını aldığı ata; meşhur zabtında gayr-i munsarif okunur (ابْنُ خَلْدُونَ), bazıları munsarif sayar"}, "level": 6},
 # the same lemma is minted under the same key by the parallel story ayn-jalut (its vanguard sense): the entry is kept
 # word for word identical to that one, so the two packages agree when they land together
 "muqaddima": {"lemma": "مُقَدِّمَة", "root": "ق د م", "pos": "noun", "gloss": {"en": "the vanguard (of an army) — the part that marches in front; (of a book) the introduction", "tr": "öncü kuvvet (ordunun) — önden giden kısım; (kitabın) mukaddimesi, girişi"}, "level": 5},
 "ibn-khaldun": PHRASE("ابْنُ خَلْدُونَ", 5, "Ibn Khaldūn — ʿAbd al-Raḥmān ibn Muḥammad (732–808 / 1332–1406), the Maghribī historian and judge, author of the Muqaddima", "İbn Haldun — Abdurrahman b. Muhammed (732–808 / 1332–1406), Mağribli tarihçi ve kadı, Mukaddime'nin yazarı",
    "literally «the son of Khaldūn»", "lafzen «Haldûn'un oğlu»",
    "A name built as an idafa: ابْنُ takes the case of its seat, and خَلْدُونَ stays in jarr — in its usual vowelling by a fatha (a diptote, like زَيْدُونَ), though some read it fully declined.",
    "İzâfetle kurulmuş bir isim: ابْنُ bulunduğu yerin i'râbını alır, خَلْدُونَ daima mecrûrdur — meşhur zabtında fetha ile (Zeydûn gibi gayr-i munsarif); bazıları onu munsarif okur."),
}
# a key is a global claim: a NEW key must not already name something else on the shelf (or in a parallel staged package)
for k in NEW_GLOSS:
    hit = [p for p in PREF if k in _G[p] and _G[p][k].get("lemma") != NEW_GLOSS[k]["lemma"]]
    assert not hit, (k, hit)

used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
            if t.get("phrase"): used.add(t["phrase"]["lex"])
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k)
    if e is None: missing.append(k)
    else: GLOSS[k] = e
assert not missing, missing
# same lemma and key as the shelf, but the gloss shown in THIS story is the sense its sentences use
GLOSS["qada"] = {**GLOSS["qada"], "gloss": {"en": "judgeship, the office of judge; a decree", "tr": "kadılık, hâkimlik makamı; hüküm, kazâ"}}
GLOSS["maghrib"] = {**GLOSS["maghrib"], "gloss": {"en": "the west, the place of sunset; al-Maghrib — North Africa west of Egypt", "tr": "batı, güneşin battığı yer; Mağrib — Mısır'ın batısındaki Kuzey Afrika"}}
GLOSS["jamaa"] = {**GLOSS["jamaa"], "gloss": {"en": "a group, a party of people; the community", "tr": "topluluk, cemaat"}}
GLOSS["tarjuman"] = {**GLOSS["tarjuman"], "gloss": {"en": "an interpreter, a translator", "tr": "tercüman"}}
GLOSS["anzala"] = {**GLOSS["anzala"], "gloss": {"en": "to send down; to let down, to lower (a man from a wall)", "tr": "indirmek; (surdan birini) aşağı indirmek"}}
GLOSS["nazala"] = {**GLOSS["nazala"], "gloss": {"en": "to descend, dismount; to settle; to encamp (عَلَى: before a city); to befall (بِـ: someone)", "tr": "inmek; yerleşmek; (bir şehrin) önüne konmak (عَلَى); (birinin) başına gelmek (بِـ)"}}
GLOSS["qiyam"] = {**GLOSS["qiyam"], "gloss": {"en": "standing, rising; (of a state) its rise", "tr": "kalkış, ayakta durma; (devletin) kuruluşu"}}
GLOSS["suqut"] = {**GLOSS["suqut"], "gloss": {"en": "falling, dropping; (of a state) its fall (masdar of سَقَطَ)", "tr": "düşme; (devletin) yıkılışı (sakata'nın masdarı)"}}
GLOSS["sahib"] = {**GLOSS["sahib"], "gloss": {"en": "companion; owner, holder; صَاحِبُ الْكِتَابِ the author of the book", "tr": "arkadaş; sahip; صَاحِبُ الْكِتَابِ kitabın yazarı"}}
GLOSS["waliya"] = {**GLOSS["waliya"], "gloss": {"en": "to take charge of personally; to hold (an office)", "tr": "bizzat üstlenmek; (bir göreve) gelmek"}}
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
 "title": {"ar": "ابْنُ خَلْدُونَ وَتَيْمُورُ", "en": "Ibn Khaldūn and Tīmūr", "tr": "İbn Haldun ve Timur"},
 "subtitle": {"ar": "دِمَشْقُ الْمُحَاصَرَةُ، وَعَالِمٌ يُنْزَلُ مِنْ سُورِهَا بِحَبْلٍ، وَمَجَالِسُ مَعَ الْفَاتِحِ — قِصَّةٌ لِلْمُسْتَوَى السَّادِسِ",
              "en": "Damascus under siege, a scholar let down from its wall by a rope, and sessions with the conqueror — a story for the sixth level",
              "tr": "Kuşatılmış Şam, surlarından iple indirilen bir âlim ve fatihle sohbet meclisleri — altıncı seviye için bir hikâye"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى السَّادِسُ) لِخَبَرِ لِقَاءِ ابْنِ خَلْدُونَ بِتَيْمُورَ عِنْدَ دِمَشْقَ سَنَةَ ٨٠٣ هـ / ١٤٠١ م، عَلَى مَا رَوَاهُ ابْنُ خَلْدُونَ نَفْسُهُ فِي «التَّعْرِيفِ بِابْنِ خَلْدُونَ وَرِحْلَتِهِ غَرْبًا وَشَرْقًا». النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ «التَّعْرِيفِ» وَلَا مِنَ «الْمُقَدِّمَةِ»، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا قَوْلٌ يُنْسَبُ إِلَى أَحَدٍ؛ وَتُرِكَ مَا دَارَ فِي الْمَجَالِسِ إِلَّا جُمْلَةَ مَوْضُوعَاتِهِ، وَتُرِكَتِ التَّفَاصِيلُ الْمُخْتَلَفُ فِيهَا.",
  "en": "ORIGINAL Level-6 graded Arabic in a classical narrative register: Ibn Khaldūn's meeting with Tīmūr at Damascus (803 AH / 1400–1401 CE), RETOLD FREELY along the well-attested core of Ibn Khaldūn's own account in his autobiography, al-Taʿrīf bi-Ibn Khaldūn wa-Riḥlatihi Gharban wa-Sharqan; the closing remark on the life of states paraphrases the doctrine of his Muqaddima. No sentence is a quotation from al-Taʿrīf or from the Muqaddima; no āya or ḥadīth is quoted; no words are put in a historical person's mouth. Left out: what was said in the sessions beyond its general topics (the lands of the Maghrib; history and the reports of kings), the description of the Maghrib Ibn Khaldūn wrote for Tīmūr, the reason the sultan turned back, the length of the stay, the names of the judges and of the interpreter, the robbery on the road home, and the figures of the sack of Damascus. The year is given in the text as «the opening of the ninth century» of the Hijra.",
  "tr": "ÖZGÜN 6. seviye Arapça, klasik anlatı üslûbunda: İbn Haldun'un Şam önlerinde Timur'la görüşmesi (803 h. / 1400–1401 m.), İbn Haldun'un kendi hayat hikâyesinde — et-Ta'rîf bi-İbn Haldûn ve Rihletihî Garben ve Şarkan — anlattığı sağlam çekirdeğe bağlı kalınarak SERBESTÇE yeniden anlatılmıştır; devletin ömrüne dair kapanış sözü Mukaddime'nin görüşünü kendi ifademizle aktarır. Hiçbir cümle et-Ta'rîf'ten veya Mukaddime'den alıntı değildir; hiçbir âyet veya hadis aktarılmamış, tarihî bir şahsın ağzına söz konmamıştır. Dışarıda bırakılanlar: meclislerde konuşulanların genel konular (Mağrib diyarı; tarih ve hükümdarların haberleri) dışındaki içeriği, İbn Haldun'un Timur için yazdığı Mağrib tasviri, sultanın geri dönüş sebebi, kalış süresi, kadıların ve tercümanın adları, dönüş yolundaki soygun ve Şam'ın yağmasına dair rakamlar. Yıl, metinde hicrî «dokuzuncu asrın başı» olarak verilmiştir.",
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
