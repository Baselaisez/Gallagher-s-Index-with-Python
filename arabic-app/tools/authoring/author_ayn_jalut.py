"""Author content/samples/ayn-jalut — «عَيْنُ جَالُوتَ», an ORIGINAL historical story at Level 6 (Master).

ORIGINAL graded Arabic in a classical narrative register, kept to the well-attested core of the years 656–658 AH /
1258–1260 CE: the Tatars (التَّتَار, as the Arabic chronicles name the Mongol armies) enter Baghdad in 656 and kill the
caliph; they march into al-Shām and take Aleppo; the fear of them spreads; the king of the Tatars sends envoys to Egypt with
a letter calling its people to submit; Quṭuz, the Mamluk sultan of Egypt, gathers the emirs and resolves to march out to the
enemy rather than wait for him; Baybars leads the vanguard, and the Tatar party before it falls back; the king of the Tatars
has gone home with most of his army and left an emir in al-Shām; the two hosts meet at ʿAyn Jālūt in Ramaḍān 658, on a
Friday; the sultan charges in person, the Muslims hold firm, the Tatars are routed and their emir killed, and Baybars
pursues them; the sultan enters al-Shām and its people are safe again; Quṭuz dies soon after, on his way back to Egypt (one
neutral line). The event is told by Ibn Kathīr (al-Bidāya wa-l-nihāya, the events of 656 and 658) and al-Maqrīzī (al-Sulūk
li-maʿrifat duwal al-mulūk); it is RETOLD FREELY here — no sentence is a quotation from them, no āya or ḥadīth is quoted, no
words are put in a historical person's mouth. Left out on purpose: the text of the Mongol letter and the fate of the envoys,
every speech (the council's, and the sultan's cry on the field), the sizes of the armies and the counts of the slain, the
day of the month, the Mongol commander's name, and the manner of Quṭuz's death.

NAMES. بَيْبَرْس is a foreign name of more than three letters: a diptote for ʿalamiyya + ʿujma (story_kit DIPT, the shelf's
أَرْمَانُوس). قُطُز is three letters with a VOWELED middle: the shelf's own doctrine (content/grammar/mamnu-min-sarf.json, after
Birgivi's Iẓhār and the Kāfiya: «a foreign name … over three letters or vowelled in the middle (قَالُونَ، إِبْرَاهِيمَ، شَتَرَ)»)
makes it a diptote, so it is written قُطُزُ / قُطُزَ and never takes tanwin; the line records that other grammarians decline
every three-letter foreign name (left for the scholar). التَّتَار carries the article and declines in full. عَيْنُ جَالُوتَ is a
place-name built as an idafa: عَيْن (the shelf's ayn-spring) takes the case of its seat and جَالُوت (the shelf's jalut, the
same lemma as Goliath in «دَاوُدُ وَجَالُوتُ») stays a diptote in jarr; the pair carries the phrase key ayn-jalut.

Five chapters, thirty sentences. The Level-6 constructions: long periodic sentences; فَبَيْنَمَا … إِذْ … (twice); ثُمَّ إِنَّ /
ثُمَّ إِنَّهُ (three times); ḥaṣr by إِنَّمَا (twice, the restricted term last), by مَا … إِلَّا, and by أَبَى إِلَّا (an exception
emptied after a verb negative in meaning); the oath وَلَعَمْرِي with its answer لَقَدْ; كَمِ الْخَبَرِيَّةُ (three times); tanāzuʿ
(فَقَتَلَ وَأَسَرَ مِنْهُمْ جَمْعًا, the Basran reading: the nearer verb governs); the mafʿūl muṭlaq and its deputy (خَوْفًا شَدِيدًا،
نَصْرًا عَظِيمًا، فَرَحًا عَظِيمًا، قِتَالًا شَدِيدًا after اقْتَتَلُوا); the mafʿūl lahu (طَلَبًا); tamyīz after an elative (أَشَدِّ
الْأُمَرَاءِ بَأْسًا); the fronted predicate of كَانَ (وَكَانَ سُلْطَانَ مِصْرَ … قُطُزُ، وَكَانَ عَلَى مُقَدِّمَتِهِ الْأَمِيرُ); ḥāl single and
as a clause, with وَ, with وَقَدْ and with no link; حَتَّى + the subjunctive; لَامُ التَّعْلِيلِ + the subjunctive; أَنْ before a
past verb; a relative clause with its resumptive pronoun (الَّذِي تَرَكَهُ); the extra bāʾ of the tawkīd (بِنَفْسِهِ); the
passive past and present; مَا زَالَ and صَارَ.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf, every verb's paradigm is
the shelf's own (no new verb), and the new entries are only those in NEW_GLOSS (the names, التَّتَار، مَمْلُوك، مُقَدِّمَة،
سِتُّمِائَة, and the place-name phrase). Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_ayn_jalut.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "ayn-jalut"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"هُمُ": "pron-3mp", "هِمُ": "pron-3mp", "هِمْ": "pron-3mp", "هُمْ": "pron-3mp", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "ي": "pron-1s", "نَا": "pron-1p"})
PRON_AR.update({"هُمُ": "هُمْ", "هِمُ": "هُمْ", "هِمْ": "هُمْ", "هُمْ": "هُمْ", "هُمَا": "هُمَا", "هِمَا": "هُمَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "ي": "الْيَاءُ", "نَا": "نَا"})

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
KH_MUB_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the clause is the predicate of the mubtada, in the seat of raf'", "; cümle mübtedânın haberi, mahallen merfû")
HALCL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause is a hal, in the seat of nasb", "; cümle hâl olarak mahallen mansûb")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
KH_KAM = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَمْ", "; the clause is the khabar of كَمْ, in the seat of raf'", "; cümle kem'in haberi, mahallen merfû")
NAIB_HID = ("، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", "; its deputy doer is the hidden «he»", "; nâib-i fâil gizli zamir «o»")
MIM = ("، وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ", "; the mim takes damma before the following ال (two quiescents met)", "; iki sâkin karşılaştığı için mîm damme aldı")
DIPT_TOWN = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town or a land), barred from tanwin", " — müennes özel isim (şehir ya da ülke), gayr-i munsarif")
NO_TANWIN = "بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ"

# ---- the names --------------------------------------------------------------------------------------------------
AJAM = ("عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ",
        "a foreign proper name, a diptote by ʿalamiyya + ʿujma (proper name + foreign origin)",
        "yabancı özel isim, alemiyet ve ucmet sebebiyle gayr-i munsarif")
AJAM_Q = (AJAM[0] + "، وَهُوَ ثُلَاثِيٌّ مُتَحَرِّكُ الْوَسَطِ كَـ«شَتَرَ» فَمُنِعَ (وَمِنَ النُّحَاةِ مَنْ يَصْرِفُ الثُّلَاثِيَّ الْأَعْجَمِيَّ مُطْلَقًا)",
          AJAM[1] + " — three letters with a VOWELED middle, like شَتَر in the books, so it is barred (some grammarians decline every three-letter foreign name)",
          AJAM[2] + " — orta harfi harekeli üç harfli bir isimdir, kitaplardaki «şeter» gibi; bu yüzden men edilir (bazı nahivciler üç harfli yabancı ismi mutlaka munsarif sayar)")
def QUTUZ(role, punct=None):
    """قُطُز — the Mamluk sultan: ʿalam + ʿujma with a voweled middle, so no tanwin and a fatḥa for jarr"""
    g = ["mamnu-min-sarf"]
    if role == "fail":
        return FAIL("قُطُزُ", "qutuz", "propn", g, sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ",
                    note_ar=" — " + AJAM_Q[0], note_en=", with no tanwin — " + AJAM_Q[1], note_tr=", tenvinsiz — " + AJAM_Q[2], punct=punct)
    if role == "ismk":
        return ISMK("قُطُزُ", "qutuz", "propn", g, sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", muakhkhar=True,
                    note_ar=" — " + AJAM_Q[0], note_en=", with no tanwin — " + AJAM_Q[1], note_tr=", tenvinsiz — " + AJAM_Q[2], punct=punct)
    if role == "majr":
        return MAJR("قُطُزَ", "qutuz", "propn", g, sign=FATHA_JARR,
                    note_ar=" — " + AJAM_Q[0], note_en=" — by a fatha standing in for the kasra: " + AJAM_Q[1], note_tr=" — kesre yerine fetha ile: " + AJAM_Q[2], punct=punct)
    raise ValueError(role)

AJAM_B = (AJAM[0] + " (اسْمٌ تُرْكِيٌّ)", AJAM[1] + " (a Turkish name)", AJAM[2] + " (Türkçe bir isim)")
def BAYBARS(role, punct=None):
    """بَيْبَرْس — the emir of the vanguard: a foreign name of more than three letters, a diptote"""
    if role == "fail":
        return FAIL("بَيْبَرْسُ", "baybars", "propn", ["mamnu-min-sarf"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ",
                    note_ar=" — " + AJAM_B[0], note_en=", with no tanwin — " + AJAM_B[1], note_tr=", tenvinsiz — " + AJAM_B[2], punct=punct)
    if role == "badal":
        return tok("بَيْبَرْسُ", "baybars", "propn", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "mamnu-min-sarf"],
            "بَدَلٌ مِنَ «الْأَمِيرُ» (وَيَجُوزُ أَنْ يَكُونَ عَطْفَ بَيَانٍ) مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — " + AJAM_B[0] + ".",
            "A badal of «the emir» (it may also be read as ʿaṭf bayān), in raf' by the damma with no tanwin — " + AJAM_B[1] + ".",
            "«Emîr»den bedel (atf-ı beyân da olabilir), tenvinsiz damme ile merfû — " + AJAM_B[2] + ".", punct=punct)
    if role == "hal_mub":
        return tok("وَبَيْبَرْسُ", "baybars", "propn", ["mubtada-khabar", "al-hal-jumla-wa-rabituha", "mamnu-min-sarf"],
            "الْوَاوُ حَالِيَّةٌ، وَبَيْبَرْسُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — " + AJAM_B[0] + "؛ وَالْجُمْلَةُ الِاسْمِيَّةُ بَعْدَ الْوَاوِ فِي مَحَلِّ نَصْبٍ حَالٌ.",
            "The waw opens a hal clause; Baybars is the mubtada, in raf' by the damma with no tanwin — " + AJAM_B[1] + "; the nominal clause after the waw is a hal, in the seat of nasb.",
            "Hâl vâvı; Baybars mübtedâ, tenvinsiz damme ile merfû — " + AJAM_B[2] + "; vâvdan sonraki isim cümlesi hâl olarak mahallen mansûb.",
            punct=punct, segments=[seg("وَ", "wa", "conj"), seg("بَيْبَرْسُ", "baybars", "propn")])
    raise ValueError(role)

DIPT_MISR = (DIPT_TOWN[0], " — a feminine proper name, barred from tanwin", " — müennes özel isim, gayr-i munsarif")
MISR_J = lambda punct=None, role="majr": (MAJR if role == "majr" else MUDAF_ILAYH)("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR,
    note_ar=DIPT_MISR[0], note_en=DIPT_MISR[1], note_tr=DIPT_MISR[2], punct=punct)
JALUT_MI = lambda punct=None: MUDAF_ILAYH("جَالُوتَ", "jalut", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR,
    note_ar="، " + AJAM[0] + " — وَ«عَيْنُ جَالُوتَ» اسْمُ مَوْضِعٍ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ",
    note_en=" — " + AJAM[1] + "; «ʿAyn Jālūt» is a place-name built as an idafa",
    note_tr=" — " + AJAM[2] + "; «Ayn Câlût» izâfetle kurulmuş bir yer adıdır", punct=punct)

SITTUMIA = lambda punct=None: tok("وَسِتِّمِائَةٍ", "sittumia", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
    "الْوَاوُ عَاطِفَةٌ، وَ«سِتِّ» مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ«مِائَةٍ» مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَجَاءَ «سِتّ» بِغَيْرِ تَاءٍ لِأَنَّ الْمِائَةَ مُؤَنَّثَةٌ، وَيُكْتَبُ الْجُزْآنِ كَلِمَةً وَاحِدَةً.",
    "The waw conjoins; «six» is conjoined, in jarr and annexed, and «hundred» is its second term, in jarr — six has no ta because «hundred» is feminine, and the two parts are written as one word.",
    "Vâv atıf; «altı» ma'tûf, mecrûr, muzâf; «yüz» muzâfun ileyh, mecrûr — «yüz» müennes olduğu için sitt tâsızdır; iki parça bitişik yazılır.",
    punct=punct, segments=[seg("وَ", "wa", "conj"), seg("سِتِّمِائَةٍ", "sittumia", "noun")])
KHAMSIN = lambda: ATF("وَخَمْسِينَ", "khamsun", "noun", "jarr", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
    note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr")

# ---- particles and frames the kit does not hold (most copied from author_alb_arslan_wa_malazgird.py) --------------
def KAM(full="وَكَمْ", pre="istinaf"):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ", "fa": "الْفَاءُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins a second exclamation; ", "fa": "The fa carries the story on; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "Vâv atıf; ", "fa": "Fâ atıf; "}[pre]
    return tok(full, "kam", "pron", ["al-kinayat-wal-zuruf-al-mabniyya", "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf", "mubtada-khabar"],
        pre_ar + "كَمْ خَبَرِيَّةٌ بِمَعْنَى «كَثِيرٍ» مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، مُضَافٌ — وَالْجُمْلَةُ بَعْدَ تَمْيِيزِهَا خَبَرُهَا.",
        pre_en + "كَمْ here is the كَمْ OF REPORT (khabariyya) meaning «many a»: built on sukun, in the seat of raf' as the mubtada, annexed to its specifier — the verbal clause after the specifier is its khabar.",
        pre_tr + "kem burada haberiyye kem'dir («nice, nice nice»): sükûn üzere mebnî, mübtedâ olarak mahallen merfû, temyîzine muzâf — temyîzinden sonraki fiil cümlesi haberidir.",
        segments=[seg(full[:2], "fa" if pre == "fa" else "wa", "conj"), seg("كَمْ", "kam", "pron")])
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
    """أَمَامَهُمْ، حَوْلَهُ، مَعَهُ: a ẓarf annexed to its pronoun"""
    return tok(full, lex, "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
        "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        "An adverb of " + kind_en + ", in nasb and annexed to the attached pronoun, which fills the seat of jarr" + note_en + ".",
        kind_tr + " zarfı, mansûb, bitişik zamire muzâf; zamir mahallen mecrûr" + note_tr + ".", punct=punct,
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def MAA_X(full, enc, note=("", "", ""), punct=None):
    return ZARF_ENC(full, "maa", enc, punct=punct, note_ar=note[0], note_en=note[1], note_tr=note[2])
def MAFUL_LAHU(full, lex, punct=None, note_ar="", note_en="", note_tr="", mudaf=False):
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"] + (["idafa-definiteness"] if mudaf else []),
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ" + ("، مُضَافٌ" if mudaf else "") + " — مَصْدَرٌ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ" + note_ar + ".",
        "The maf'ul li-ajlih (object of cause), in nasb" + (" and annexed" if mudaf else "") + " — a masdar giving the reason for the act, sharing its time and its doer" + note_en + ".",
        "Mef'ûlün lieclih, mansûb" + (", muzâf" if mudaf else "") + " — fiilin sebebini bildiren masdar; fiille zamanda ve fâilde ortak" + note_tr + ".", punct=punct)
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
DH_MI = ("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh")
ZALA_X = lambda: tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ.",
    "زَالَ, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb — after a negation it means «never ceased, still».",
    "Zâle, kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; ismini ref, haberini nasb eder — nefiyle birlikte devam bildirir («hâlâ, hep»).")
def ANNA_X(note=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + note[0] + ".",
        "أَنَّ «that», the verb-like particle that builds a masdar: it puts its noun in nasb and raises its predicate" + note[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + note[2] + ".")
SADDA_ZANNA = (" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «ظَنَّ»", "; أَنَّ with its clause stands for a masdar that fills both objects of «thought»", "; enne ve sonrası, «zannetti»nin iki mef'ûlünün yerini tutan müevvel masdardır")
def MAN_X(seat_ar, seat_en, seat_tr, extra, sila=("وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ", "the clause after it is its ṣila", "sonraki cümle sılasıdır")):
    return tok("مَنْ", "man-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، " + sila[0] + ".",
        "The relative pronoun «those who», built on sukun, in the seat of " + seat_en + "; " + sila[1] + ".",
        "İsm-i mevsûl «kimse(ler)», sükûn üzere mebnî, mahallen " + seat_tr + "; " + sila[2] + ".")
SILA_ZARF = ("وَالظَّرْفُ بَعْدَهُ صِلَتُهُ", "the adverb after it is its ṣila", "sonraki zarf sılasıdır")
MUSLIMUN_F = lambda punct=None: FAIL("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign="بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the waw, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için vâv ile", punct=punct)
R_MI = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", "idafa-definiteness")
MUSLIMIN_MI = lambda punct=None: SALIM_J("الْمُسْلِمِينَ", "muslim", R_MI, punct=punct)
def MUTLAQ_X(full, lex, verb_ar, verb_en, verb_tr, punct=None):
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «" + verb_ar + "»، يُؤَكِّدُ فِعْلَهُ، وَبِنَعْتِهِ يُبَيِّنُ نَوْعَهُ.",
        "The absolute object (maf'ul mutlaq), in nasb — the masdar of «" + verb_en + "»: it strengthens its verb, and with its adjective it tells the KIND.",
        "Mef'ûlün mutlak, mansûb — «" + verb_tr + "» fiilinin masdarı: fiilini pekiştirir, sıfatıyla da türünü bildirir.", punct=punct)
QITAL_NAIB = lambda: tok("قِتَالًا", "qital", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
    "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «قَاتَلَ»، وَهُوَ يُلَاقِي «اقْتَتَلُوا» فِي مَادَّتِهِ وَمَعْنَاهُ فَنَابَ عَنْ مَصْدَرِهِ «اقْتِتَالًا»، وَبِنَعْتِهِ يُبَيِّنُ النَّوْعَ.",
    "Standing in for the absolute object, in nasb — the masdar of قَاتَلَ: it shares the root and the meaning of «fought one another» and takes the place of that verb's own masdar (اقْتِتَال); with its adjective it tells the KIND of fighting.",
    "Mef'ûlün mutlakın nâibi, mansûb — kâtele'nin masdarı: «birbirleriyle savaştılar» fiiliyle kökte ve anlamda buluştuğu için onun masdarının (iktitâl) yerini tuttu; sıfatıyla savaşın türünü bildirir.")
LAAMRI = lambda: tok("وَلَعَمْرِي", "amr-qasam", "noun", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "mubtada-khabar", "ya-al-mutakallim", "hadhf-wa-taqdir"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْخَبَرُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي؛ وَهٰذِهِ صِيغَةُ قَسَمٍ.",
    "The waw opens a new sentence; the lam is the lam of ibtidāʾ; عَمْر «life» is the mubtada, in raf' by a damma estimated before the speaker's ya (the kasra the ya demands holds its place), annexed to the ya — its predicate is dropped by rule («[is my oath]»): this is a FORM OF OATH, «by my life».",
    "Vâv isti'nâf içindir; lâm ibtidâ lâmıdır; «ömür» mübtedâ, mütekellim yâ'sından önce takdîrî damme ile merfû (yerini yâ'nın gerektirdiği kesre tutmuştur), yâ'ya muzâf — haberi vücûben hazfedilmiştir («yeminimdir»): bu bir yemin kalıbıdır, «ömrüme andolsun».",
    segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-ibtida", "part"), seg("عَمْرِ", "amr-qasam", "noun"), seg("ي", "pron-1s", "pron")])
LAQAD = lambda: tok("لَقَدْ", "qad", "part", ["qad-harf", "al-qasam-wal-shart-fil-kafiya"],
    "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهُمَا جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The lam opens the answer of the oath and قَدْ affirms the past verb — the clause after them is the oath's answer and has no seat of its own.",
    "Lâm kasemin cevabında gelen lâmdır, kad tahkîk harfidir — sonraki cümle kasemin cevabıdır, i'râbdan mahalli yoktur.",
    segments=[seg("لَ", "lam-qasam", "part"), seg("قَدْ", "qad", "part")])
YAWMAIDHIN = lambda note=("", "", ""), punct=None: tok("يَوْمَئِذٍ", "yawmaidhin", "noun", ["maful-fih", "idafa-definiteness", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"],
    "يَوْمَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (وَيَجُوزُ بِنَاؤُهُ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى مَبْنِيٍّ)، مُضَافٌ، وَإِذْ ظَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ مَحْذُوفَةٍ، وَكُسِرَتِ الذَّالُ لِالْتِقَاءِ السَّاكِنَيْنِ" + note[0] + ".",
    "«On that day»: يَوْمَ is an adverb of time in nasb (it may also be built on fatha, being annexed to a built word), annexed to إِذْ, a built adverb in the seat of jarr; the tanwin stands for a dropped clause («the day when …») and the dhal takes kasra where two quiescents met" + note[1] + ".",
    "«O gün»: yevme mansûb zaman zarfı (mebnî bir kelimeye muzâf olduğu için fetha üzere mebnî de olabilir), iz'e muzâf; iz mebnî zarf, mahallen mecrûr; tenvin hazfedilmiş bir cümlenin yerini tutar, iki sâkin karşılaştığı için zâl kesre aldı" + note[2] + ".", punct=punct)
JAMAN_F = lambda: tok("الْجَمْعَانِ", "jam", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ.",
    "The doer, in raf' by the alif — a dual («the two hosts»); its nun stands in for the tanwin of the singular.", "Fâil, tesniye olduğu için elif ile merfû («iki ordu»); nûn, müfred ismin tenvini yerinedir.")
BI_DHALIKA = lambda kind=("", "", ""), tail=("", "", ""): tok("بِذٰلِكَ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
    "الْبَاءُ حَرْفُ جَرٍّ" + kind[0] + "، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ" + tail[0] + ".",
    "The ba is a jarr letter" + kind[1] + "; the demonstrative after it is built on sukun, in the seat of jarr" + tail[1] + ".",
    "Bâ cer harfi" + kind[2] + "; işaret ismi sükûn üzere mebnî, mahallen mecrûr" + tail[2] + ".",
    segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")])

# ---- verb shapes the kit does not hold ------------------------------------------------------------------------------
YUGHLABUN = lambda punct=None: tok("يُغْلَبُونَ", "ghalaba", "verb", ["afal-khamsa", "mudari-marfu", "naib-al-fail", "al-majhul-fil-kafiya", "al-bariz-al-muttasil"],
    "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — ضُمَّ أَوَّلُهُ وَفُتِحَ مَا قَبْلَ آخِرِهِ — مِنَ الْأَفْعَالِ الْخَمْسَةِ، مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«قَوْمٌ».",
    "A present verb in the passive — its first letter takes damma and the letter before the last a fatha — one of the five verbs, in raf' by the kept nun; the waw is its deputy doer, in the seat of raf'. The clause qualifies «a people», in the seat of raf'.",
    "Meçhul muzâri — evveli mazmûm, âhirinden önceki harf meftûh — ef'âl-i hamseden, nûnun sübûtuyla merfû; vâv nâib-i fâil, mahallen merfû. Cümle «kavim»in na'tı, mahallen merfû.", punct=punct)
YALQAHU = lambda punct=None: tok("يَلْقَاهُ", "laqiya", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى الْجَيْشِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَهِيَ لِلْعَدُوِّ.",
    "Present verb put in nasb by أَنْ, its fatha estimated on the alif (it cannot be voiced there); the doer «it» (the army) is hidden, and the attached «him» (the enemy) is its object, in the seat of nasb.",
    "En ile mansûb muzâri, fethası elif üzerinde takdîrî (telaffuzu mümkün değil); fâil gizli zamir «o» (ordu); bitişik «onu» (düşmanı) mef'ûlün bih, mahallen mansûb.", punct=punct,
    segments=[seg("يَلْقَا", "laqiya", "verb"), seg("هُ", "pron-3ms", "pron")])
LI_TARIFA = lambda: tok("لِتَعْرِفَ", "arafa", "verb", ["nawasib-wa-jawazim-al-mudari", "an-masdariyya", "huruf-jarr", "qasr"],
    "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَتَعْرِفَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ جَوَازًا بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى الْمُقَدِّمَةِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَسِيرُ»، وَهُمَا الْمَقْصُورُ عَلَيْهِ.",
    "The lam of purpose is a jarr letter; the present verb after it is in nasb by an أَنْ that may stay hidden after the lam, its sign the fatha; the doer «it» (the vanguard) is hidden — the masdar they build is in jarr by the lam, the phrase hangs on «goes», and it is what the statement is restricted TO.",
    "Lâm ta'lîl lâmı, cer harfi; sonraki muzâri lâmdan sonra cevâzen gizli en ile mansûb, alâmeti fetha; fâil gizli zamir «o» (öncü kuvvet) — müevvel masdar lâm ile mecrûr, câr-mecrûr «gider»e müteallik; hüküm ona hasredilmiştir.",
    segments=[seg("لِ", "li", "prep"), seg("تَعْرِفَ", "arafa", "verb")])
HATTA_NASB = lambda: tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
    "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «until» is a particle of limit and jarr: the present verb after it is in nasb by an أَنْ that must stay hidden, and the masdar they build is in jarr by حَتَّى.",
    "Hattâ «…-e kadar»: gâye ve cer harfi; sonraki muzâri vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr.")
YASILA = lambda: tok("يَصِلَ", "wasala", "verb", ["nawasib-wa-jawazim-al-mudari", "mithal-verbs"],
    "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى الْعَدُوِّ — وَحُذِفَتْ فَاؤُهُ (الْوَاوُ) لِوُقُوعِهَا بَيْنَ يَاءٍ مَفْتُوحَةٍ وَكَسْرَةٍ.",
    "Present verb in nasb by an أَنْ hidden of necessity after حَتَّى, its sign the fatha; the doer «he» (the enemy) is hidden — the verb's first radical (the waw) has dropped, falling between an open ya and a kasra.",
    "Hattâ'dan sonra vücûben gizli en ile mansûb muzâri, alâmeti fetha; fâil gizli zamir «o» (düşman) — fâ'ül-fiili (vâv), meftûh yâ ile kesre arasında kaldığı için düşmüştür.")
BI_AN = lambda: tok("بِأَنْ", "bi", "prep", ["huruf-jarr", "an-masdariyya", "qasr"],
    "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَأَنْ حَرْفٌ مَصْدَرِيٌّ مَبْنِيٌّ عَلَى السُّكُونِ دَخَلَ عَلَى الْمَاضِي فَلَمْ يَعْمَلْ فِيهِ لَفْظًا — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ أَنْ وَمَا بَعْدَهَا مَجْرُورٌ بِالْبَاءِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حُفِظَتْ»، وَهُمَا الْمَقْصُورُ عَلَيْهِ.",
    "The ba of cause is a jarr letter; أَنْ is the masdar-making particle, built on sukun — before a past verb it governs nothing visibly. The masdar built from أَنْ and its clause is in jarr by the ba; the phrase hangs on «was kept», and it is what the statement is restricted TO.",
    "Bâ sebebiyye için cer harfi; en masdar harfi, sükûn üzere mebnî — mâzîye girdiği için lafzen amel etmez. En ve sonrasından oluşan müevvel masdar bâ ile mecrûr; câr-mecrûr «korundu»ya müteallik ve hüküm ona hasredilmiştir.",
    segments=[seg("بِ", "bi", "prep"), seg("أَنْ", "an-masdariyya", "part")])
YANTAZIRHU = lambda punct=None: tok("يَنْتَظِرْهُ", "intazara", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-viii-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «خَرَجَ» فَهِيَ دَاخِلَةٌ فِي صِلَةِ أَنْ.",
    "Present verb in jazm by لَمْ, its sign the sukun; the doer «he» is hidden and the attached «him» is its object, in the seat of nasb — the clause is conjoined to «marched out», so it too belongs to the clause of أَنْ.",
    "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli zamir «o», bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle «çıktı»ya ma'tûftur, bu yüzden o da en'in sılasına dahildir.", punct=punct,
    segments=[seg("يَنْتَظِرْ", "intazara", "verb"), seg("هُ", "pron-3ms", "pron")])
YADHKURUNAHU = lambda punct=None: tok("يَذْكُرُونَهُ", "dhakara", "verb", ["afal-khamsa", "mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "kana-wa-akhawatuha"],
    "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ.",
    "One of the five verbs, in raf' by the kept nun; the waw is its doer, in the seat of raf', and the attached «it» is its object, in the seat of nasb — the clause is the predicate of زَالَ, in the seat of nasb.",
    "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâil, mahallen merfû; bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle zâle'nin haberi, mahallen mansûb.", punct=punct,
    segments=[seg("يَذْكُرُونَ", "dhakara", "verb"), seg("هُ", "pron-3ms", "pron")])
BI_NAFSIHI = lambda: tok("بِنَفْسِهِ", "bi", "prep", ["huruf-al-ziyada-fil-kafiya", "tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
    "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِلتَّوْكِيدِ، وَنَفْسِ تَوْكِيدٌ مَعْنَوِيٌّ لِـ«السُّلْطَانُ» مَجْرُورٌ لَفْظًا بِالْبَاءِ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ (وَقِيلَ: الْبَاءُ أَصْلِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ).",
    "The ba is an EXTRA jarr letter that adds emphasis; نَفْس «himself» is a tawkid of meaning of «the sultan», in jarr in its wording (by the extra ba) and in raf' in its seat; it is annexed to the attached pronoun, which fills the seat of jarr (some take the ba as a real one and the phrase as a hal).",
    "Bâ te'kîd için zâid cer harfi; «nefs» «sultan»ın ma'nevî te'kîdi — lafzen zâid bâ ile mecrûr, mahallen merfû; bitişik zamire muzâf, zamir mahallen mecrûr (bir görüşe göre bâ aslîdir ve câr-mecrûr hâldir).",
    segments=[seg("بِ", "bi", "prep"), seg("نَفْسِ", "nafs", "noun"), seg("هِ", "pron-3ms", "pron")])
TANAZU = (" — وَهٰذَا مِنَ التَّنَازُعِ: تَنَازَعَ «قَتَلَ» وَ«أَسَرَ» الِاسْمَ «جَمْعًا» مَفْعُولًا، فَعَمِلَ فِيهِ الثَّانِي الْأَقْرَبُ عِنْدَ الْبَصْرِيِّينَ، وَحُذِفَ مَفْعُولُ الْأَوَّلِ لِدَلَالَةِ الْكَلَامِ عَلَيْهِ",
          "; this is TANĀZUʿ: «slew» and «took captive» both reach for «a host» as their object — the Basrans give it to the nearer verb, and the first verb's object is left out, the sentence showing what it is",
          "; bu bir tenâzu'dur: «öldürdü» ile «esir aldı» ikisi de «bir kalabalık»ı mef'ûl olarak ister — Basralılara göre yakın fiil amel eder, ilk fiilin mef'ûlü kelâm ona delâlet ettiği için hazfedilir")

# ============================================ the text ============================================
TITLES = [{"ar": "سُقُوطُ بَغْدَادَ", "en": "Baghdad Falls", "tr": "Bağdat'ın Düşüşü"},
          {"ar": "الْعَزْمُ عَلَى الْخُرُوجِ", "en": "The Resolve to March Out", "tr": "Yola Çıkma Azmi"},
          {"ar": "بَيْبَرْسُ فِي الْمُقَدِّمَةِ", "en": "Baybars in the Vanguard", "tr": "Öncü Kuvvette Baybars"},
          {"ar": "يَوْمُ عَيْنِ جَالُوتَ", "en": "The Day of ʿAyn Jālūt", "tr": "Ayn Câlût Günü"},
          {"ar": "نَجَاةُ الشَّامِ", "en": "Al-Shām Delivered", "tr": "Şam Diyarının Kurtuluşu"}]

# ---- Chapter 1 — سُقُوطُ بَغْدَادَ ----
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "In the year 656 (of the Hijra) the Tatars entered Baghdad, and they killed the caliph and many of its people.",
  "tr": "Altı yüz elli altı yılında Tatarlar Bağdat'a girdiler; halifeyi ve halkından pek çoğunu öldürdüler."},
 "tokens": [FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«دَخَلَ»", "; the jarr phrase hangs on «entered»", " — câr-mecrûr «girdi»ye müteallik")),
  MAJR("سَنَةِ", "sana", **W(MUDAF)),
  MUDAF_ILAYH("سِتٍّ", "sitt", extra=["asma-al-adad-fil-kafiya"], note_ar=" — وَجَاءَ بِغَيْرِ تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ", note_en=" — written without ta because the counted noun «year» is feminine", note_tr=" — sayılan «sene» müennes olduğu için tâsız gelmiştir"),
  KHAMSIN(), SITTUMIA(),
  MADI("دَخَلَ", "dakhala", **W(FAIL_BAAD)), FAIL("التَّتَارُ", "tatar", "propn"),
  MAFUL("بَغْدَادَ", "baghdad", "propn", ["mamnu-min-sarf"], sign=NO_TANWIN,
        note_ar=DIPT_TOWN[0] + " — وَقِيلَ: مَنْصُوبٌ عَلَى التَّوَسُّعِ بِنَزْعِ الْخَافِضِ (دَخَلُوا فِي بَغْدَادَ)",
        note_en=DIPT_TOWN[1] + " (some read it as in nasb by the dropping of the jarr letter: «entered into Baghdad»)",
        note_tr=DIPT_TOWN[2] + " (bir görüşe göre cer harfinin hazfiyle mansûbdur: «Bağdat'ın içine girdiler»)", punct="،"),
  VERB_WAW("وَقَتَلُوا", "qatala"), MAFUL("الْخَلِيفَةَ", "khalifa"),
  ATF("وَكَثِيرًا", "kathir", "noun", "nasb"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«كَثِيرًا»", "; the jarr phrase qualifies «many»", " — câr-mecrûr «çok»un mahzûf na'tına müteallik")),
  ENC_NOUN("أَهْلِهَا", "ahl", "هَا", "majr", note_ar=" — وَالضَّمِيرُ لِبَغْدَادَ", note_en=" — «its» is Baghdad", note_tr=" — zamir Bağdat'a döner", punct=".")]})
S1.append({"id": "s2", "translation": {
  "en": "How many a scholar was slain that day, and how much wealth was carried off!",
  "tr": "O gün nice âlim öldürüldü, nice mal da alınıp götürüldü!"},
 "tokens": [KAM("فَكَمْ", pre="fa"), KAM_TAMYIZ("عَالِمٍ", "alim-scholar"),
  MAJHUL("قُتِلَ", "qatala", note_ar=NAIB_HID[0] + "، يَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=NAIB_HID[1] + ", returning to كَمْ" + KH_KAM[1], note_tr=NAIB_HID[2] + ", kem'e döner" + KH_KAM[2]),
  YAWMAIDHIN((" — مُتَعَلِّقٌ بِـ«قُتِلَ»", "; it hangs on «was slain»", " — «öldürüldü»ye müteallik"), punct="،"),
  KAM("وَكَمْ", pre="atf"), KAM_TAMYIZ("مَالٍ", "mal"),
  MAJHUL("أُخِذَ", "akhadha", note_ar=NAIB_HID[0] + "، يَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=NAIB_HID[1] + ", returning to كَمْ" + KH_KAM[1], note_tr=NAIB_HID[2] + ", kem'e döner" + KH_KAM[2], punct="!")]})
S1.append({"id": "s3", "translation": {
  "en": "Then the Tatars marched, after that, into the lands of al-Shām (Syria), and took Aleppo and other cities besides.",
  "tr": "Sonra Tatarlar bunun ardından Şam diyarına yürüdüler; Halep'i ve başka şehirleri aldılar."},
 "tokens": [THUMMA(), INNA(),
  tok("التَّتَارَ", "tatar", "propn", ["inna-wa-akhawatuha"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of إِنَّ, in nasb.", "İnne'nin ismi, mansûb."),
  VERB_WAW("سَارُوا", "sara-travel", ["hollow-verbs"], note_ar=KH_INNA_CL[0], note_en=KH_INNA_CL[1], note_tr=KH_INNA_CL[2]),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«سَارُوا»", note_en="; it hangs on «marched»", note_tr="; «yürüdüler»e müteallik"),
  DHALIKA(*DH_MI),
  ILA(), MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUDAF_ILAYH("الشَّامِ", "sham", "propn", punct="،"),
  VERB_WAW("فَأَخَذُوا", "akhadha"),
  MAFUL("حَلَبَ", "halab", "propn", ["mamnu-min-sarf"], sign=NO_TANWIN, note_ar=DIPT_TOWN[0], note_en=DIPT_TOWN[1], note_tr=DIPT_TOWN[2]),
  tok("وَغَيْرَهَا", "ghayr", "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"],
      "الْوَاوُ عَاطِفَةٌ، وَغَيْرَ مَعْطُوفٌ عَلَى «حَلَبَ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يَعُودُ عَلَى حَلَبَ.",
      "The waw conjoins; «other than» is conjoined to «Aleppo», in nasb, and annexed to the attached «it» (Aleppo), which fills the seat of jarr.",
      "Vâv atıf; «gayr» «Halep»e ma'tûf, mansûb; bitişik «onun» (Halep) zamirine muzâf, zamir mahallen mecrûr.",
      segments=[seg("وَ", "wa", "conj"), seg("غَيْرَ", "ghayr", "noun"), seg("هَا", "pron-3fs", "pron")]),
  NOTE(MINA(), " — وَهِيَ بَيَانِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «غَيْرَ»", "; this مِنْ explains «others» and the phrase is a hal of it", "; beyâniyye min — câr-mecrûr «gayr»dan mahzûf bir hâle müteallik"),
  MAJR("الْمُدُنِ", "madina", extra=["jam-taksir"], note_ar=" — جَمْعُ مَدِينَةٍ", note_en=" — the plural of «city»", note_tr=" — medîne'nin cem'i", punct=".")]})
S1.append({"id": "s4", "translation": {
  "en": "People feared them with a great fear, until many thought them a people who could not be beaten.",
  "tr": "İnsanlar onlardan şiddetle korktular; öyle ki pek çokları onların yenilmez bir kavim olduğunu sandı."},
 "tokens": [ENC_MADI("وَخَافَهُمُ", "khafa", "هُمُ", ["hollow-verbs"], note_ar=MIM[0] + FAIL_BAAD[0], note_en=MIM[1] + FAIL_BAAD[1], note_tr=MIM[2] + FAIL_BAAD[2]),
  FAIL("النَّاسُ", "nas"),
  MUTLAQ_X("خَوْفًا", "khawf", "خَافَ", "to fear", "korkmak"), NAAT("شَدِيدًا", "shadid", "nasb", punct="،"),
  HATTA_IBT(), MADI("ظَنَّ", "zanna", ["doubled-verbs"], **W(FAIL_BAAD)), FAIL("كَثِيرٌ", "kathir"),
  NOTE(MINA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«كَثِيرٌ»", "; the jarr phrase qualifies «many»", "; câr-mecrûr «çok»un mahzûf na'tına müteallik"),
  MAJR("النَّاسِ", "nas"),
  tok("أَنَّهُمْ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"],
      "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا، يَعُودُ عَلَى التَّتَارِ" + SADDA_ZANNA[0] + ".",
      "أَنَّ is the verb-like particle; the attached «they» (the Tatars) is its noun, in the seat of nasb" + SADDA_ZANNA[1] + ".",
      "Enne te'kîd ve nasb harfi; bitişik «onlar» (Tatarlar) ismi, mahallen mansûb" + SADDA_ZANNA[2] + ".",
      segments=[seg("أَنَّ", "anna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  KH_ANNA("قَوْمٌ", "qawm"), LA_NAFIYA(), YUGHLABUN(punct=".")]})
S1.append({"id": "s5", "translation": {
  "en": "And while the people of Egypt were in that fear, all at once there came to them envoys of the king of the Tatars with a letter in which he called them to submit.",
  "tr": "Mısır halkı o korku içindeyken ansızın Tatar kralının elçileri onlara, kendilerini itaate çağırdığı bir mektupla geldi."},
 "tokens": [BAYNAMA(), MUBTADA("أَهْلُ", "ahl", **W(MUDAF)), MISR_J(role="mi"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", "; the jarr phrase hangs on the omitted predicate of «the people»", " — câr-mecrûr mübtedânın mahzûf haberine müteallik")),
  DHALIKA("جَرٍّ بِفِي", "jarr after فِي", "mecrûr (fî ile)"),
  tok("الْخَوْفِ", "khawf", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A badal of the demonstrative, in jarr like it.", "İşaret isminden bedel, mecrûr.", punct="،"),
  IDH_FUJ(),
  ENC_MADI("جَاءَتْهُمْ", "jaa", "هُمْ", ["hollow-verbs"], fem=True, note_ar=FAIL_BAAD[0] + " — وَأُنِّثَ الْفِعْلُ لِأَنَّ فَاعِلَهُ جَمْعُ تَكْسِيرٍ", note_en=FAIL_BAAD[1] + " — the verb is feminine because its doer is a broken plural", note_tr=FAIL_BAAD[2] + " — fâili kırık çoğul olduğu için fiil müennes geldi"),
  FAIL("رُسُلُ", "rasul-msg", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ رَسُولٍ", note_en=MUDAF[1] + " — the plural of «envoy»", note_tr=MUDAF[2] + " — resûl'ün cem'i"),
  MUDAF_ILAYH("مَلِكِ", "malik-king", **W(MUDAF)), MUDAF_ILAYH("التَّتَارِ", "tatar", "propn"),
  BI_NOUN("بِكِتَابٍ", "kitab", "كِتَابٍ", note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ (جَاءَ بِالشَّيْءِ: أَتَى بِهِ)، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَاءَتْ»", note_en="; the ba carries the verb over to its thing («came WITH», i.e. brought); the phrase hangs on «came»", note_tr="; bâ ta'diye içindir («ile geldi», yani getirdi); câr-mecrûr «geldi»ye müteallik"),
  MUDARI("يَدْعُوهُمْ", "daa", enc="هُمْ", naqis="و", note_ar=" — وَالْمُسْتَتِرُ لِمَلِكِ التَّتَارِ، وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«كِتَابٍ»", note_en=" (the king of the Tatars); the clause qualifies «a letter», in the seat of jarr", note_tr=" (Tatar kralı); cümle «mektup»un na'tı, mahallen mecrûr"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)", note_ar=" — وَهُوَ الرَّابِطُ الْعَائِدُ عَلَى «كِتَابٍ»", note_en=" — it is the link that returns to «a letter»", note_tr=" — «mektup»a dönen râbıt budur"),
  ILA(), MAJR("الطَّاعَةِ", "taa", punct=".")]})
S1.append({"id": "s6", "translation": {
  "en": "The sultan of Egypt in those days was Quṭuz, one of the Mamluks.",
  "tr": "O günlerde Mısır'ın sultanı Memlüklerden biri olan Kutuz'du."},
 "tokens": [KANA("وَكَانَ"),
  KHK("سُلْطَانَ", "sultan", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — قُدِّمَ عَلَى اسْمِ كَانَ، وَجَازَ تَقْدِيمُهُ لِظُهُورِ الْإِعْرَابِ عَلَيْهِمَا", note_en=", annexed — the FRONTED predicate of كَانَ: it may come first because the case shows on both words", note_tr=", muzâf — kâne'nin öne alınmış haberi: i'râb ikisinde de göründüğü için öne alınabilir"),
  MISR_J(role="mi"), YAWMAIDHIN(), QUTUZ("ismk", punct="،"),
  tok("أَحَدُ", "ahad", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "idafa-definiteness"],
      "بَدَلٌ مِنْ «قُطُزُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ (وَيَجُوزُ أَنْ يَكُونَ خَبَرًا لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ: هُوَ).",
      "A badal of «Quṭuz», in raf' and annexed (it may also be read as the predicate of an omitted «he»).",
      "«Kutuz»dan bedel, merfû, muzâf (mahzûf bir «o» mübtedâsının haberi de olabilir)."),
  MUDAF_ILAYH("الْمَمَالِيكِ", "mamluk", extra=["jam-taksir"], note_ar=" — جَمْعُ مَمْلُوكٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ أَلْ عَلَيْهِ", note_en=" — the plural of «mamlūk», on the pattern of the farthest plurals (a diptote), here in jarr by the kasra because it carries the article", note_tr=" — memlûk'ün cem'i, muntehe'l-cumû' vezninde (gayr-i munsarif); elif-lâm aldığı için kesre ile mecrûr", punct=".")]})

# ---- Chapter 2 — الْعَزْمُ عَلَى الْخُرُوجِ ----
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "When the letter reached Quṭuz, he gathered the emirs and asked them their view on the enemy's affair.",
  "tr": "Mektup Kutuz'a ulaşınca emîrleri topladı ve düşmanın meselesi hakkında onlara görüşlerini sordu."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("وَصَلَ", "wasala", ["mithal-verbs"], **W(FAIL_BAAD, LAMMA_CL)), FAIL("الْكِتَابُ", "kitab"),
  ILA(), QUTUZ("majr"),
  MADI("جَمَعَ", "jamaa-gather", hidden=True, **W(JAWAB_LAMMA)),
  MAFUL("الْأُمَرَاءَ", "amir", extra=["jam-taksir"], note_ar=" — جَمْعُ أَمِيرٍ عَلَى فُعَلَاءَ", note_en=" — the plural of «emir», on the pattern فُعَلَاء", note_tr=" — emîr'in fu'alâ vezninde cem'i", punct="،"),
  ENC_MADI("وَسَأَلَهُمْ", "saala", "هُمْ", hidden=True),
  PREP("عَنْ", "an", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَأَلَ»", "; the jarr phrase hangs on «asked»", "; câr-mecrûr «sordu»ya müteallik", gloss_tr="«hakkında»"),
  ENC_NOUN("رَأْيِهِمْ", "ray", "هِمْ", "majr"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَأْيِ»", "; the jarr phrase hangs on «view»", " — câr-mecrûr «görüş»e müteallik")),
  MAJR("أَمْرِ", "amr", **W(MUDAF)), MUDAF_ILAYH("الْعَدُوِّ", "aduww", punct=".")]})
S2.append({"id": "s2", "translation": {
  "en": "And Quṭuz would have nothing but to march out to the enemy, and not to wait for him until he reached Egypt.",
  "tr": "Kutuz ise düşmanın üzerine çıkıp gitmekten ve onu Mısır'a varıncaya kadar beklememekten başka bir şeye razı olmadı."},
 "tokens": [MADI_ALIF("فَأَبَى", "aba", note_ar=FAIL_BAAD[0] + " — وَأَبَى فِي مَعْنَى النَّفْيِ (لَمْ يُرِدْ)، فَجَازَ أَنْ يَقَعَ بَعْدَهُ الِاسْتِثْنَاءُ الْمُفَرَّغُ",
      note_en=FAIL_BAAD[1] + " — «refused» carries the meaning of a negation («did not want»), so an emptied exception may follow it",
      note_tr=FAIL_BAAD[2] + " — ebâ olumsuzluk anlamı taşır («istemedi»), bu yüzden ardından müferrağ istisnâ gelebilir"),
  QUTUZ("fail"), ILLA_HASR(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«أَبَى»، وَهُوَ الْمَقْصُورُ عَلَيْهِ", "; the masdar it builds is the object of «refused», in the seat of nasb — and it is what his will is restricted TO", "; kurduğu müevvel masdar «kabul etmedi»nin mef'ûlü, mahallen mansûb — iradesi ona hasredilmiştir"),
  MANSUB_AN("يَخْرُجَ", "kharaja"),
  ILA(), MAJR("الْعَدُوِّ", "aduww", punct="،"),
  WA_LA_NAFIYA(),
  MANSUB_AN("يَنْتَظِرَهُ", "intazara", ["form-viii-verbs"], enc="هُ", note_ar=" — وَهُوَ مَعْطُوفٌ عَلَى «يَخْرُجَ» دَاخِلٌ مَعَهُ فِي عَمَلِ أَنْ", note_en=" — it is conjoined to «march out» and falls under the same أَنْ", note_tr=" — «çıkmak»a ma'tûftur, aynı en'in ameline dahildir"),
  HATTA_NASB(), YASILA(), ILA(), MISR_J(punct=".")]})
S2.append({"id": "s3", "translation": {
  "en": "And by my life, that was a sound judgement.",
  "tr": "Ömrüme andolsun ki bu, isabetli bir görüştü."},
 "tokens": [LAAMRI(), LAQAD(), KANA("كَانَ"), DHALIKA("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi"),
  KHK("رَأْيًا", "ray"), NAAT("حَسَنًا", "hasan-adj", "nasb", punct=".")]})
S2.append({"id": "s4", "translation": {
  "en": "Then he marched out of Egypt with the armies, making for al-Shām, having resolved to meet the enemy.",
  "tr": "Sonra ordularla Mısır'dan çıktı; Şam'a yöneliyordu ve düşmanla karşılaşmaya azmetmişti."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  MADI("خَرَجَ", "kharaja", hidden=True, **W(KH_INNA_CL)),
  BI_NOUN("بِالْجُيُوشِ", "jaysh", "الْجُيُوشِ", extra=["jam-taksir"], note_ar=" — جَمْعُ جَيْشٍ، وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the plural of «army»; the ba of company («with»)", note_tr=" — ceyş'in cem'i; bâ musâhabe içindir («ile»)"),
  MIN(), MISR_J(),
  MUDARI("يُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"], **W(HALCL)),
  MAFUL("الشَّامَ", "sham", "propn", punct="،"),
  WA_QAD(), MADI("عَزَمَ", "azama", hidden=True),
  ALA(), MAJR("لِقَاءِ", "liqa", extra=["masdar"], note_ar="، مُضَافٌ — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ", note_en=", annexed — a masdar annexed to its object («meeting the enemy»)", note_tr=", muzâf — mef'ûlüne muzâf masdar"),
  MUDAF_ILAYH("الْعَدُوِّ", "aduww", punct=".")]})
S2.append({"id": "s5", "translation": {
  "en": "Over his vanguard was the emir Baybars, one of the fiercest of the emirs in war.",
  "tr": "Öncü kuvvetinin başında emîr Baybars vardı; o, savaşta emîrlerin en çetinlerindendi."},
 "tokens": [KANA("وَكَانَ"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ مُقَدَّمٌ", "; the jarr phrase is the FRONTED predicate of كَانَ", "; câr-mecrûr kâne'nin öne alınmış haberine müteallik"),
  ENC_NOUN("مُقَدِّمَتِهِ", "muqaddima", "هِ", "majr", note_ar=" — وَمُقَدِّمَةُ الْجَيْشِ: أَوَّلُهُ الَّذِي يَسِيرُ أَمَامَهُ", note_en=" — the «muqaddima» of an army is its vanguard, the part that marches in front", note_tr=" — ordunun mukaddimesi, önünden giden öncü kısmıdır"),
  ISMK("الْأَمِيرُ", "amir", muakhkhar=True), BAYBARS("badal", punct="،"),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", "; the jarr phrase hangs on the omitted predicate of «he»", " — câr-mecrûr mübtedânın mahzûf haberine müteallik")),
  MAJR("أَشَدِّ", "ashadd", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en=", annexed — an elative and a diptote, which takes kasra here because it is annexed", note_tr=", muzâf — gayr-i munsarif ism-i tafdîl; muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("الْأُمَرَاءِ", "amir", extra=["jam-taksir"], note_ar=" — جَمْعُ أَمِيرٍ", note_en=" — the plural of «emir»", note_tr=" — emîr'in cem'i"),
  TAMYIZ("بَأْسًا", "bas", punct=".")]})
S2.append({"id": "s6", "translation": {
  "en": "For a vanguard goes before the army only to learn the enemy's news before the army meets him.",
  "tr": "Öncü kuvvet ordunun önünden ancak, ordu düşmanla karşılaşmadan önce onun haberlerini öğrenmek için gider."},
 "tokens": [WA_INNAMA(),
  MUDARI_DF("تَسِيرُ", "sara-travel", ["hollow-verbs"]), FAIL("الْمُقَدِّمَةُ", "muqaddima"),
  ZARF("أَمَامَ", "amama", note_ar=" — مُتَعَلِّقٌ بِـ«تَسِيرُ»", note_en="; it hangs on «goes»", note_tr="; «gider»e müteallik"),
  MUDAF_ILAYH("الْجَيْشِ", "jaysh"),
  LI_TARIFA(),
  MAFUL("أَخْبَارَ", "khabar-news", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ خَبَرٍ", note_en=MUDAF[1] + " — the plural of «report»", note_tr=MUDAF[2] + " — haber'in cem'i"),
  MUDAF_ILAYH("الْعَدُوِّ", "aduww"),
  ZARF("قَبْلَ", "qabla", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«تَعْرِفَ»، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ مُضَافٌ إِلَيْهِ", note_en="; it hangs on «learn», and the masdar after it is its second term", note_tr="; «öğrenir»e müteallik; sonraki müevvel masdar muzâfun ileyhtir"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the masdar it builds is annexed to «before», in the seat of jarr", "; kurduğu müevvel masdar «önce»ye muzâfun ileyh, mahallen mecrûr"),
  YALQAHU(punct=".")]})

# ---- Chapter 3 — بَيْبَرْسُ فِي الْمُقَدِّمَةِ ----
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "The king of the Tatars had gone back to his own lands with most of his troops, and had left in al-Shām one of his emirs.",
  "tr": "Tatar kralı askerlerinin çoğuyla kendi ülkesine dönmüş, Şam'da emîrlerinden birini bırakmıştı."},
 "tokens": [KANA("وَكَانَ"), ISMK("مَلِكُ", "malik-king", **W(MUDAF)), MUDAF_ILAYH("التَّتَارِ", "tatar", "propn"),
  QAD(), MADI("رَجَعَ", "rajaa", hidden=True, **W(KH_KANA)),
  ILA(), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr"),
  BI_NOUN("بِأَكْثَرِ", "akthar", "أَكْثَرِ", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — وَالْبَاءُ لِلْمُصَاحَبَةِ؛ وَأَكْثَرُ اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ، جُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en="; it is annexed — the ba of company; أَكْثَر is an elative and a diptote, in jarr by the kasra because it is annexed", note_tr="; muzâf — bâ musâhabe içindir; ekser gayr-i munsarif ism-i tafdîldir, muzâf olduğu için kesre ile mecrûr"),
  ENC_NOUN("جُنْدِهِ", "jund", "هِ", "mudaf", punct="،"),
  MADI("وَتَرَكَ", "taraka", hidden=True, note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «رَجَعَ» فَهِيَ فِي مَحَلِّ نَصْبٍ مِثْلُهَا", note_en="; the clause is conjoined to «had gone back», so it too is in the seat of nasb", note_tr="; cümle «dönmüştü»ye ma'tûftur, o da mahallen mansûb"),
  BI_NOUN("بِالشَّامِ", "sham", "الشَّامِ", pos="propn", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»", note_en=" — the ba here means «in»", note_tr=" — bâ burada «-de» anlamındadır"),
  MAFUL("أَمِيرًا", "amir"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«أَمِيرًا»", "; the jarr phrase qualifies «an emir»", " — câr-mecrûr «emîr»in mahzûf na'tına müteallik")),
  ENC_NOUN("أُمَرَائِهِ", "amir", "هِ", "majr", extra=["jam-taksir"], note_ar=" — جَمْعُ أَمِيرٍ", note_en=" — the plural of «emir»", note_tr=" — emîr'in cem'i", punct=".")]})
S3.append({"id": "s2", "translation": {
  "en": "So Baybars went on ahead of the sultan, seeking news of the enemy, until he drew near a party of the Tatars.",
  "tr": "Baybars düşmanın haberlerini öğrenmek için sultanın önünden yürüdü; nihayet Tatarlardan bir bölüğe yaklaştı."},
 "tokens": [MADI("فَسَارَ", "sara-travel", ["hollow-verbs"], **W(FAIL_BAAD)), BAYBARS("fail"),
  ZARF("أَمَامَ", "amama", note_ar=" — مُتَعَلِّقٌ بِـ«سَارَ»", note_en="; it hangs on «went»", note_tr="; «yürüdü»ye müteallik"),
  MUDAF_ILAYH("السُّلْطَانِ", "sultan"),
  MAFUL_LAHU("طَلَبًا", "talab"),
  tok("لِأَخْبَارِ", "li", "prep", ["huruf-jarr", "idafa-definiteness", "jam-taksir"],
      "اللَّامُ حَرْفُ جَرٍّ — وَهِيَ لَامُ التَّقْوِيَةِ دَخَلَتْ عَلَى مَعْمُولِ الْمَصْدَرِ «طَلَبًا» — وَأَخْبَارِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ (جَمْعُ خَبَرٍ).",
      "The lam is a jarr letter — the lam of strengthening, brought in on what the masdar «seeking» governs; «news» is in jarr and annexed (the plural of «report»).",
      "Lâm cer harfi — «arayarak» masdarının ma'mûlüne giren takviye lâmı; «haberler» mecrûr, muzâf (haber'in cem'i).",
      segments=[seg("لِ", "li", "prep"), seg("أَخْبَارِ", "khabar-news", "noun")]),
  MUDAF_ILAYH("الْعَدُوِّ", "aduww", punct="،"),
  HATTA_IBT(), MADI("قَرُبَ", "qaruba", hidden=True),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَرُبَ»", "; the jarr phrase hangs on «drew near»", " — câr-mecrûr «yaklaştı»ya müteallik")),
  MAJR("طَائِفَةٍ", "taifa"),
  NOTE(MINA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«طَائِفَةٍ»", "; the jarr phrase qualifies «a party»", "; câr-mecrûr «bölük»ün mahzûf na'tına müteallik"),
  MAJR("التَّتَارِ", "tatar", "propn", punct=".")]})
S3.append({"id": "s3", "translation": {
  "en": "When they learned of him, they left their position and drew back from him.",
  "tr": "Onun geldiğini öğrenince yerlerini bırakıp ondan geri çekildiler."},
 "tokens": [LAMMA2("فَلَمَّا"), VERB_WAW("عَلِمُوا", "alima", note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onu»)", note_ar=" — مُتَعَلِّقَانِ بِـ«عَلِمُوا»", note_en=" — it hangs on «learned»", note_tr=" — «öğrendiler»e müteallik"),
  VERB_WAW("تَرَكُوا", "taraka", note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  ENC_NOUN("مَوْضِعَهُمْ", "mawdi", "هُمْ", "maful", punct="،"),
  VERB_WAW("وَرَجَعُوا", "rajaa"),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)", note_ar=" — مُتَعَلِّقَانِ بِـ«رَجَعُوا»", note_en=" — it hangs on «drew back»", note_tr=" — «geri çekildiler»e müteallik", punct=".")]})
S3.append({"id": "s4", "translation": {
  "en": "Then the sultan caught up with him with the rest of the army, and they marched all together toward the enemy, Baybars before them.",
  "tr": "Sonra sultan ordunun geri kalanıyla ona yetişti; hep birlikte düşmana doğru yürüdüler, Baybars da önlerindeydi."},
 "tokens": [THUMMA(), ENC_MADI("لَحِقَهُ", "lahiqa", "هُ", note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), FAIL("السُّلْطَانُ", "sultan"),
  BI_NOUN("بِسَائِرِ", "sair-rest", "سَائِرِ", note_ar="، مُضَافٌ — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en="; it is annexed — the ba of company («with»)", note_tr="; muzâf — bâ musâhabe içindir («ile»)"),
  MUDAF_ILAYH("الْجَيْشِ", "jaysh", punct="،"),
  VERB_WAW("فَسَارُوا", "sara-travel", ["hollow-verbs"]),
  HAL("جَمِيعًا", "jami", note_ar=" — وَصَاحِبُهُ وَاوُ الْجَمَاعَةِ", note_en="; its owner is the waw of the group", note_tr="; sahibi cemâat vâvıdır"),
  ZARF("نَحْوَ", "nahw", note_ar=" — مُتَعَلِّقٌ بِـ«سَارُوا»", note_en="; it hangs on «marched»", note_tr="; «yürüdüler»e müteallik"),
  MUDAF_ILAYH("الْعَدُوِّ", "aduww", punct="،"),
  BAYBARS("hal_mub"),
  ZARF_ENC("أَمَامَهُمْ", "amama", "هُمْ", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", note_en="; the adverb hangs on the omitted predicate of «Baybars»", note_tr="; zarf mübtedânın mahzûf haberine müteallik", punct=".")]})
S3.append({"id": "s5", "translation": {
  "en": "News of the Muslims reached the Tatars, and they came on toward them with their hosts.",
  "tr": "Müslümanların haberi Tatarlara ulaştı; onlar da kalabalıklarıyla Müslümanların üzerine yöneldiler."},
 "tokens": [MADI("وَبَلَغَ", "balagha", **W(FAIL_BAAD)),
  MAFUL("التَّتَارَ", "tatar", "propn", note_ar=" — مُقَدَّمٌ عَلَى الْفَاعِلِ", note_en=" — placed before the doer", note_tr=" — fâilden önce gelmiştir"),
  FAIL("خَبَرُ", "khabar-news", note_ar=MUDAF[0] + " — مُؤَخَّرٌ عَنِ الْمَفْعُولِ", note_en=MUDAF[1] + " — placed after the object", note_tr=MUDAF[2] + " — mef'ûlden sonraya bırakılmıştır"),
  MUSLIMIN_MI(punct="،"),
  VERB_WAW("فَأَقْبَلُوا", "aqbala", ["form-iv-verbs"]),
  JARR_PRON("إِلَيْهِمْ", "ila", "إِلَيْ", "هِمْ", " («onlara»)", note_ar=" — وَالضَّمِيرُ لِلْمُسْلِمِينَ", note_en=" — «them» is the Muslims", note_tr=" — zamir Müslümanlara döner"),
  BI_NOUN("بِجُمُوعِهِمْ", "jam", "جُمُوعِهِمْ", enc="هِمْ", extra=["jam-taksir"], note_ar=" — جَمْعُ جَمْعٍ، وَالْبَاءُ لِلْمُصَاحَبَةِ، وَالضَّمِيرُ لِلتَّتَارِ", note_en=" — the plural of «host»; the ba of company, and «their» is the Tatars", note_tr=" — cem'in cem'i; bâ musâhabe içindir, zamir Tatarlara döner", punct=".")]})
S3.append({"id": "s6", "translation": {
  "en": "And the two hosts met in the month of Ramaḍān of the year 658, at a place in the land of al-Shām whose name is ʿAyn Jālūt — «the Spring of Goliath».",
  "tr": "İki ordu altı yüz elli sekiz yılının Ramazan ayında, Şam topraklarında adı Ayn Câlût («Câlût Pınarı») olan bir yerde karşılaştı."},
 "tokens": [MADI_ALIF("فَالْتَقَى", "iltaqa", ["form-viii-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), JAMAN_F(),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْتَقَى»", "; the jarr phrase hangs on «met»", " — câr-mecrûr «karşılaştı»ya müteallik")),
  MAJR("شَهْرِ", "shahr", **W(MUDAF)),
  MUDAF_ILAYH("رَمَضَانَ", "ramadan", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar="، مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", note_en=" — by a fatha standing in for the kasra: a diptote (a proper name with the added alif and nun)", note_tr=" — kesre yerine fetha ile: alemiyet ve elif-nûn ziyadesi sebebiyle gayr-i munsarif"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «شَهْرِ رَمَضَانَ»", "; the jarr phrase is a hal of «the month of Ramaḍān»", " — câr-mecrûr «Ramazan ayı»ndan mahzûf bir hâle müteallik")),
  MAJR("سَنَةِ", "sana", **W(MUDAF)),
  MUDAF_ILAYH("ثَمَانٍ", "thamani", extra=["asma-al-adad-fil-kafiya", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ",
      note_ar=" — اسْمٌ مَنْقُوصٌ أَصْلُهُ «ثَمَانِي»؛ وَجَاءَ بِغَيْرِ تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ",
      note_en=" — by a kasra estimated on the ya, which dropped before the tanwin (a manqūṣ, from ثَمَانِي); without ta because the counted «year» is feminine",
      note_tr=" — tenvin önünde düşen yâ üzerinde takdîrî kesre ile (mankûs isim, aslı semânî); sayılan «sene» müennes olduğu için tâsız"),
  KHAMSIN(), SITTUMIA(punct="،"),
  BI_NOUN("بِمَوْضِعٍ", "mawdi", "مَوْضِعٍ", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْتَقَى»", note_en=" — the ba here means «at»; the phrase hangs on «met»", note_tr=" — bâ burada «-de» anlamındadır; câr-mecrûr «karşılaştı»ya müteallik"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَوْضِعٍ»", "; the jarr phrase qualifies «a place»", " — câr-mecrûr «yer»in mahzûf na'tına müteallik")),
  MAJR("أَرْضِ", "ard", **W(MUDAF)), MUDAF_ILAYH("الشَّامِ", "sham", "propn"),
  ENC_NOUN("اسْمُهُ", "ism", "هُ", "mubtada", note_ar=" — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِـ«مَوْضِعٍ»، وَالْهَاءُ رَابِطُهَا", note_en="; the nominal clause is a second qualifier of «a place», in the seat of jarr, and the pronoun links it", note_tr="; isim cümlesi «yer»in ikinci na'tı, mahallen mecrûr; zamir râbıttır"),
  PH(KHABAR("عَيْنُ", "ayn-spring", **W(MUDAF)), "ayn-jalut"), JALUT_MI(punct=".")]})

# ---- Chapter 4 — يَوْمُ عَيْنِ جَالُوتَ ----
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "They fought one another on the Friday, a fierce fight.",
  "tr": "Cuma günü birbirleriyle şiddetle çarpıştılar."},
 "tokens": [VERB_WAW("فَاقْتَتَلُوا", "iqtatala", ["form-viii-verbs"]),
  ZARF("يَوْمَ", "yawm", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«اقْتَتَلُوا»", note_en="; it hangs on «fought»", note_tr="; «çarpıştılar»a müteallik"),
  MUDAF_ILAYH("الْجُمُعَةِ", "jumua"), QITAL_NAIB(), NAAT("شَدِيدًا", "shadid", "nasb", punct=".")]})
S4.append({"id": "s2", "translation": {
  "en": "And while the men were in the thick of the fighting, all at once the sultan himself charged the Tatars, and the troops around him charged with him.",
  "tr": "İnsanlar savaşın en kızgın yerindeyken sultan ansızın bizzat Tatarların üzerine atıldı; etrafındaki askerler de onunla birlikte saldırdı."},
 "tokens": [BAYNAMA(), MUBTADA("النَّاسُ", "nas"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", "; the jarr phrase hangs on the omitted predicate of «the men»", " — câr-mecrûr mübtedânın mahzûf haberine müteallik")),
  MAJR("أَشَدِّ", "ashadd", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en=", annexed — an elative and a diptote, in jarr by the kasra because it is annexed («the fiercest of the fighting»)", note_tr=", muzâf — gayr-i munsarif ism-i tafdîl; muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("الْقِتَالِ", "qital", punct="،"),
  IDH_FUJ(),
  MADI("حَمَلَ", "hamala", note_ar=FAIL_BAAD[0] + " — وَحَمَلَ عَلَى الْعَدُوِّ: كَرَّ عَلَيْهِ فِي الْقِتَالِ", note_en=FAIL_BAAD[1] + " — حَمَلَ عَلَى «to charge (an enemy)»", note_tr=FAIL_BAAD[2] + " — hamele alâ: düşmanın üzerine saldırmak"),
  FAIL("السُّلْطَانُ", "sultan"), BI_NAFSIHI(),
  ALA(), MAJR("التَّتَارِ", "tatar", "propn", punct="،"),
  MADI("وَحَمَلَ", "hamala", **W(FAIL_BAAD)),
  MAA_X("مَعَهُ", "هُ", (" — مُتَعَلِّقٌ بِـ«حَمَلَ»", "; it hangs on «charged»", "; «saldırdı»ya müteallik")),
  MAN_X("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail"], sila=SILA_ZARF),
  ZARF_ENC("حَوْلَهُ", "hawl", "هُ", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ تَقْدِيرُهُ «اسْتَقَرَّ»، وَهُوَ صِلَةُ الْمَوْصُولِ", note_en="; the adverb hangs on an omitted «is (found)», and that is the relative's ṣila", note_tr="; zarf mahzûf «bulunan»a müteallik; mevsûlün sılasıdır"),
  NOTE(MINA(), " — وَهِيَ بَيَانِيَّةٌ تُبَيِّنُ «مَنْ»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْهُ", "; this مِنْ explains «those who», and the phrase is a hal of it", "; beyâniyye min — «kimseler»i açıklar; câr-mecrûr ondan mahzûf bir hâle müteallik"),
  MAJR("الْجُنْدِ", "jund", punct=".")]})
S4.append({"id": "s3", "translation": {
  "en": "When the Muslims saw their sultan fighting in front of them, they held firm and endured, until God gave them a great victory and routed the Tatars.",
  "tr": "Müslümanlar sultanlarının önlerinde savaştığını görünce sebat edip direndiler; nihayet Allah onlara büyük bir zafer verdi ve Tatarları bozguna uğrattı."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI_ALIF("رَأَى", "raa", note_ar=FAIL_BAAD[0] + " — وَرَأَى هُنَا بَصَرِيَّةٌ تَنْصِبُ مَفْعُولًا وَاحِدًا" + LAMMA_CL[0], note_en=FAIL_BAAD[1] + " — «saw» with the eye, taking one object" + LAMMA_CL[1], note_tr=FAIL_BAAD[2] + " — re'â burada gözle görmektir, tek mef'ûl alır" + LAMMA_CL[2]),
  MUSLIMUN_F(), ENC_NOUN("سُلْطَانَهُمْ", "sultan", "هُمْ", "maful"),
  MUDARI("يُقَاتِلُ", "qatala-fight", ["form-iii-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «سُلْطَانَهُمْ»", note_en="; the clause is a hal of «their sultan», in the seat of nasb", note_tr="; cümle «sultanları»ndan hâl, mahallen mansûb"),
  ZARF_ENC("أَمَامَهُمْ", "amama", "هُمْ", note_ar=" — مُتَعَلِّقٌ بِـ«يُقَاتِلُ»", note_en="; it hangs on «fighting»", note_tr="; «savaşır»a müteallik"),
  VERB_WAW("ثَبَتُوا", "thabata", note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  VERB_WAW("وَصَبَرُوا", "sabara", punct="،"),
  HATTA_IBT(),
  ENC_MADI("نَصَرَهُمُ", "nasara", "هُمُ", note_ar=MIM[0] + FAIL_BAAD[0], note_en=MIM[1] + FAIL_BAAD[1], note_tr=MIM[2] + FAIL_BAAD[2]),
  ALLAH_F(), MUTLAQ_X("نَصْرًا", "nasr", "نَصَرَ", "to give victory", "zafer vermek"), NAAT("عَظِيمًا", "azim", "nasb", punct="،"),
  MADI("وَهَزَمَ", "hazama", hidden=True, note_ar=" — يَعُودُ عَلَى لَفْظِ الْجَلَالَةِ", note_en=" («He» — God)", note_tr=" («O» — Allah)"),
  MAFUL("التَّتَارَ", "tatar", "propn", punct=".")]})
S4.append({"id": "s4", "translation": {
  "en": "And the men held firm that day only because their sultan held firm.",
  "tr": "O gün insanlar ancak sultanlarının sebatı sayesinde sebat ettiler."},
 "tokens": [WA_MA("istinaf"), MADI("ثَبَتَ", "thabata", **W(FAIL_BAAD)), FAIL("النَّاسُ", "nas"),
  YAWMAIDHIN((" — مُتَعَلِّقٌ بِـ«ثَبَتَ»", "; it hangs on «held firm»", " — «sebat etti»ye müteallik")),
  ILLA_HASR(),
  BI_NOUN("بِثَبَاتِ", "thabat", "ثَبَاتِ", extra=["masdar", "qasr"], note_ar="، مُضَافٌ — وَالْبَاءُ لِلسَّبَبِيَّةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ثَبَتَ»، وَهُمَا الْمَقْصُورُ عَلَيْهِ", note_en="; it is annexed — the ba of cause; the phrase hangs on «held firm», and it is what the statement is restricted TO", note_tr="; muzâf — bâ sebebiyye içindir; câr-mecrûr «sebat etti»ye müteallik ve hüküm ona hasredilmiştir"),
  ENC_NOUN("سُلْطَانِهِمْ", "sultan", "هِمْ", "mudaf", punct=".")]})
S4.append({"id": "s5", "translation": {
  "en": "Their emir — the one their king had left in al-Shām — was killed, and those of them who were left fled.",
  "tr": "Kralları tarafından Şam'da bırakılan emîrleri öldürüldü; onlardan geriye kalanlar da kaçtı."},
 "tokens": [MAJHUL("وَقُتِلَ", "qatala", note_ar="، وَنَائِبُ الْفَاعِلِ بَعْدَهُ", note_en="; its deputy doer follows", note_tr="; nâib-i fâili ondan sonra gelir"),
  tok("أَمِيرُهُمُ", "amir", "noun", ["naib-al-fail", "idafa-definiteness", "al-bariz-al-muttasil"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + MIM[0] + ".",
      "The deputy doer (na'ib al-fa'il), in raf'; annexed to the attached «their», which fills the seat of jarr" + MIM[1] + ".",
      "Nâib-i fâil, merfû; bitişik «onların» zamirine muzâf, zamir mahallen mecrûr" + MIM[2] + ".",
      segments=[seg("أَمِيرُ", "amir", "noun"), seg("هُمُ", "pron-3mp", "pron")]),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«أَمِيرُ»، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
      "A relative pronoun built on sukun, in the seat of raf' as the adjective of «emir»; the clause after it is its ṣila.", "İsm-i mevsûl, sükûn üzere mebnî, «emîr»in na'tı olarak mahallen merfû; sonraki cümle sılasıdır."),
  ENC_MADI("تَرَكَهُ", "taraka", "هُ", note_ar=FAIL_BAAD[0] + " — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", note_en=FAIL_BAAD[1] + " — the attached «him» is the pronoun that returns to the relative; the clause is the relative's ṣila and has no seat of its own", note_tr=FAIL_BAAD[2] + " — bitişik «onu» mevsûle dönen zamirdir; cümle sıla cümlesidir, i'râbdan mahalli yoktur"),
  ENC_NOUN("مَلِكُهُمْ", "malik-king", "هُمْ", "fail"),
  BI_NOUN("بِالشَّامِ", "sham", "الشَّامِ", pos="propn", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَرَكَ»", note_en=" — the ba here means «in»; the phrase hangs on «had left»", note_tr=" — bâ burada «-de» anlamındadır; câr-mecrûr «bıraktı»ya müteallik", punct="،"),
  MADI("وَفَرَّ", "farra", ["doubled-verbs"], **W(FAIL_BAAD)),
  MAN_X("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail"]),
  MADI("بَقِيَ", "baqiya", ["naqis-verbs"], hidden=True, note_ar=" — يَعُودُ عَلَى مَنْ" + SILA_[0], note_en=" — returning to «those who»" + SILA_[1], note_tr=" — men'e döner" + SILA_[2]),
  NOTE(MINHUM(punct="."), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «بَقِيَ»", "; the jarr phrase is a hal of the doer of «were left»", "; câr-mecrûr «kaldı»nın fâilinden mahzûf bir hâle müteallik")]})
S4.append({"id": "s6", "translation": {
  "en": "Baybars pursued them, and of them he slew and took captive a great host.",
  "tr": "Baybars onları takip etti; onlardan büyük bir kalabalığı öldürdü ve esir aldı."},
 "tokens": [ENC_MADI("وَتَبِعَهُمْ", "tabia-follow", "هُمْ", note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), BAYBARS("fail", punct="،"),
  MADI("فَقَتَلَ", "qatala", ["tanazu"], hidden=True, **W(TANAZU)),
  MADI("وَأَسَرَ", "asara-capture", ["tanazu"], hidden=True),
  NOTE(MINHUM(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «جَمْعًا»: كَانَ نَعْتًا لَهُ، فَلَمَّا تَقَدَّمَ عَلَيْهِ صَارَ حَالًا",
       "; the jarr phrase hangs on an omitted hal of «a host»: it would be the adjective of an indefinite noun, and fronted before it, it becomes a hal",
       "; câr-mecrûr «kalabalık»tan mahzûf bir hâle müteallik: nekrenin na'tı iken ondan önce gelince hâl olmuştur"),
  MAFUL("جَمْعًا", "jam", extra=["tanazu"], note_ar=" لِـ«أَسَرَ» الْأَقْرَبِ إِلَيْهِ — وَهُوَ الِاسْمُ الْمُتَنَازَعُ فِيهِ", note_en=" of «took captive», the nearer verb — it is the noun the two verbs contend for", note_tr=" — yakın fiil «esir aldı»nın mef'ûlü; iki fiilin çekiştiği isim budur"),
  NAAT("كَثِيرًا", "kathir", "nasb", punct=".")]})

# ---- Chapter 5 — نَجَاةُ الشَّامِ ----
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Then the sultan entered the lands of al-Shām a few days later, and their people rejoiced at his coming with a great joy.",
  "tr": "Sonra sultan birkaç gün sonra Şam diyarına girdi; halkı onun gelişine büyük bir sevinçle sevindi."},
 "tokens": [THUMMA(), INNA(), ISM_INNA("السُّلْطَانَ", "sultan"),
  MADI("دَخَلَ", "dakhala", hidden=True, **W(KH_INNA_CL)),
  MAFUL("بِلَادَ", "bilad", note_ar=MUDAF[0] + " (وَقِيلَ: مَنْصُوبٌ عَلَى التَّوَسُّعِ بِنَزْعِ الْخَافِضِ)", note_en=MUDAF[1] + " (some read it as in nasb by the dropping of the jarr letter)", note_tr=MUDAF[2] + " (bir görüşe göre cer harfinin hazfiyle mansûbdur)"), MUDAF_ILAYH("الشَّامِ", "sham", "propn"),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«دَخَلَ»", note_en="; it hangs on «entered»", note_tr="; «girdi»ye müteallik"),
  MUDAF_ILAYH("أَيَّامٍ", "yawm", extra=["jam-taksir"], note_ar=" — جَمْعُ يَوْمٍ", note_en=" — the plural of «day»", note_tr=" — yevm'in cem'i", punct="،"),
  MADI("فَفَرِحَ", "fariha", **W(FAIL_BAAD)),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («ona»)", note_ar=" — مُتَعَلِّقَانِ بِـ«فَرِحَ»", note_en=" — it hangs on «rejoiced»", note_tr=" — «sevindi»ye müteallik"),
  ENC_NOUN("أَهْلُهَا", "ahl", "هَا", "fail", note_ar=" — وَالضَّمِيرُ لِبِلَادِ الشَّامِ", note_en=" — «their» is the lands of al-Shām", note_tr=" — zamir Şam diyarına döner"),
  MUTLAQ_X("فَرَحًا", "farah", "فَرِحَ", "to rejoice", "sevinmek"), NAAT("عَظِيمًا", "azim", "nasb", punct=".")]})
S5.append({"id": "s2", "translation": {
  "en": "Those of the Tatars who had been in them fled, and people were safe again after their fear.",
  "tr": "Orada bulunan Tatarlar kaçtı; insanlar da korkularından sonra güvene kavuştu."},
 "tokens": [MADI("وَهَرَبَ", "haraba-flee", **W(FAIL_BAAD)),
  MAN_X("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail"]),
  KANA_HID("كَانَ", note=("، يَعُودُ عَلَى «مَنْ»" + SILA_[0], " (it returns to «those who»)" + SILA_[1], " (men'e döner)" + SILA_[2])),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", note_en=" — the ba means «in»; the phrase hangs on the omitted predicate of كَانَ", note_tr=" — bâ «-de» anlamındadır; câr-mecrûr kâne'nin mahzûf haberine müteallik"),
  NOTE(MINA(), " — وَهِيَ بَيَانِيَّةٌ تُبَيِّنُ «مَنْ»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْهُ", "; this مِنْ explains «those who», and the phrase is a hal of it", "; beyâniyye min — «kimseler»i açıklar; câr-mecrûr ondan mahzûf bir hâle müteallik"),
  MAJR("التَّتَارِ", "tatar", "propn", punct="،"),
  MADI("وَأَمِنَ", "amina", **W(FAIL_BAAD)), FAIL("النَّاسُ", "nas"),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«أَمِنَ»", note_en="; it hangs on «were safe»", note_tr="; «güvene kavuştu»ya müteallik"),
  ENC_NOUN("خَوْفِهِمْ", "khawf", "هِمْ", "mudaf", punct=".")]})
S5.append({"id": "s3", "translation": {
  "en": "How many a land was saved by that victory from the hands of the Tatars!",
  "tr": "Nice diyar o zaferle Tatarların elinden kurtuldu!"},
 "tokens": [KAM("فَكَمْ", pre="fa"), KAM_TAMYIZ("بَلَدٍ", "balad"),
  MADI_ALIF("نَجَا", "naja-escape", hidden=True, note_ar=" — يَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=" — returning to كَمْ" + KH_KAM[1], note_tr=" — kem'e döner" + KH_KAM[2]),
  BI_DHALIKA((" لِلسَّبَبِيَّةِ", " of cause («by»)", " (sebebiyye: «ile»)"), (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَجَا»", "; the phrase hangs on «was saved»", "; câr-mecrûr «kurtuldu»ya müteallik")),
  tok("النَّصْرِ", "nasr", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.", "A badal of the demonstrative, in jarr like it.", "İşaret isminden bedel, mecrûr."),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَجَا»", "; the jarr phrase hangs on «was saved»", " — câr-mecrûr «kurtuldu»ya müteallik")),
  MAJR("أَيْدِي", "yad", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", note_ar="، مُضَافٌ — جَمْعُ يَدٍ، اسْمٌ مَنْقُوصٌ", note_en=" — by a kasra estimated on the ya (too heavy to voice); annexed — the plural of «hand», a manqūṣ", note_tr=" — yâ üzerinde takdîrî kesre ile (ağırlık sebebiyle); muzâf — yed'in cem'i, mankûs isim"),
  MUDAF_ILAYH("التَّتَارِ", "tatar", "propn", punct="!")]})
S5.append({"id": "s4", "translation": {
  "en": "And Egypt was kept safe only because Quṭuz marched out to his enemy and did not wait for him.",
  "tr": "Mısır ancak Kutuz'un düşmanının üzerine çıkıp gitmesi ve onu beklememesi sayesinde korundu."},
 "tokens": [WA_INNAMA(),
  MAJHUL("حُفِظَتْ", "hafiza", fem=True, note_ar="، وَنَائِبُ الْفَاعِلِ بَعْدَهُ", note_en="; its deputy doer follows", note_tr="; nâib-i fâili ondan sonra gelir"),
  tok("مِصْرُ", "misr", "propn", ["naib-al-fail", "mamnu-min-sarf"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ" + DIPT_MISR[0] + ".",
      "The deputy doer (na'ib al-fa'il), in raf' by the damma with no tanwin" + DIPT_MISR[1] + ".", "Nâib-i fâil, tenvinsiz damme ile merfû" + DIPT_MISR[2] + "."),
  BI_AN(),
  MADI("خَرَجَ", "kharaja", **W(FAIL_BAAD)), QUTUZ("fail"),
  ILA(), ENC_NOUN("عَدُوِّهِ", "aduww", "هِ", "majr"),
  WA_LAM(), YANTAZIRHU(punct=".")]})
S5.append({"id": "s5", "translation": {
  "en": "Quṭuz died not long after that, on his way back to Egypt.",
  "tr": "Kutuz bundan kısa bir süre sonra, Mısır'a dönerken vefat etti."},
 "tokens": [THUMMA(), MADI("مَاتَ", "mata-die", ["hollow-verbs"], **W(FAIL_BAAD)), QUTUZ("fail"),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«مَاتَ»", note_en="; it hangs on «died»", note_tr="; «vefat etti»ye müteallik"),
  DHALIKA(*DH_MI),
  BI_NOUN("بِقَلِيلٍ", "qalil", "قَلِيلٍ", note_ar=" — وَالْبَاءُ لِبَيَانِ مِقْدَارِ الْفَرْقِ، أَيْ: بَعْدَهُ بِزَمَنٍ قَلِيلٍ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بَعْدَ»", note_en=" — the ba measures the gap («by a little», i.e. a short time after); the phrase hangs on «after»", note_tr=" — bâ aradaki farkın miktarını bildirir («az bir zamanla»); câr-mecrûr «sonra»ya müteallik", punct="،"),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"),
  KHABAR("رَاجِعٌ", "raji", ["ism-fail"]),
  ILA(), MISR_J(punct=".")]})
S5.append({"id": "s6", "translation": {
  "en": "And the day of ʿAyn Jālūt became one of the famous days of Islam, and people have never ceased to remember it.",
  "tr": "Ayn Câlût günü İslâm'ın meşhur günlerinden biri oldu; insanlar onu anmaktan hiç vazgeçmediler."},
 "tokens": [SARA("فَصَارَ"),
  tok("يَوْمُ", "yawm", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of صَارَ, in raf', annexed.", "Sâra'nın ismi, merfû, muzâf."),
  PH(MUDAF_ILAYH("عَيْنِ", "ayn-spring", **W(MUDAF)), "ayn-jalut"), JALUT_MI(),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ صَارَ", "; the jarr phrase hangs on the omitted predicate of صَارَ", " — câr-mecrûr sâra'nın mahzûf haberine müteallik")),
  MAJR("أَيَّامِ", "yawm", extra=["jam-taksir"], note_ar=MUDAF[0] + " — جَمْعُ يَوْمٍ", note_en=MUDAF[1] + " — the plural of «day»", note_tr=MUDAF[2] + " — yevm'in cem'i"),
  MUDAF_ILAYH("الْإِسْلَامِ", "islam"),
  NAAT("الْمَشْهُورَةِ", "mashhur", "jarr", extra=["ism-maful"], note_ar=" — وَمَنْعُوتُهُ «أَيَّامِ»، وَجَاءَ مُفْرَدًا مُؤَنَّثًا لِأَنَّ مَنْعُوتَهُ جَمْعُ تَكْسِيرٍ لِغَيْرِ الْعَاقِلِ", note_en=" — it qualifies «days», singular and feminine because «days» is a broken plural of things not rational", note_tr=" — «günler»in na'tı; menûtu akılsızlar için kırık çoğul olduğundan müfred müennes gelmiştir", punct="،"),
  WA_MA("atf", (" — وَهِيَ مَعَ «زَالَ» تُفِيدُ الِاسْتِمْرَارَ", "; with «ceased» it means «still, never stopped»", "; zâle ile birlikte devam bildirir")),
  ZALA_X(),
  tok("النَّاسُ", "nas", "noun", ["kana-wa-akhawatuha"], "اسْمُ زَالَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of زَالَ, in raf'.", "Zâle'nin ismi, merfû."),
  YADHKURUNAHU(punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            if DERIVED & set(t.get("grammar", [])) and "thulathi-mujarrad-babs" in t["grammar"]:
                t["grammar"].remove("thulathi-mujarrad-babs")
            t["grammar"] = list(dict.fromkeys(t.get("grammar", [])))
            if not t["grammar"]: del t["grammar"]

# the grammar anchors must all resolve in the registry
_GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
_bad = sorted({g for S in CHAPS for s in S for t in s["tokens"] for g in t.get("grammar", []) if g not in _GR})
assert not _bad, _bad

# ---- the lexicon: every key by lemma identity from the shelf; the entries below are new -----------------------------------
PREF = ["al-kafiya", "alb-arslan-wa-malazgird", "salah-al-din-wa-al-quds", "al-amana-wa-al-khashaba", "ashab-al-ghar", "qisas-al-nabiyyin-4",
        "al-usul-al-munifa", "wasiyyat-abi-yusuf-l5", "adam-wa-iblis", "al-asad-wa-al-far", "al-asad-wa-al-arnab", "juha-wa-al-himar",
        "aqaid-ahl-al-sunna", "talkhis-al-miftah", "qisas-al-nabiyyin-2", "fath-al-qustantiniyya"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
# where the shelf holds one key in several packages, take the entry the sister stories (Malazgird, Ḥiṭṭīn) already took
FORCE = {"an": "abu-hanifa-wa-al-safina", "jam": "salah-al-din-wa-al-quds", "sultan": "fath-al-qustantiniyya",
         "man-mawsula": "talkhis-al-miftah", "jund": "dawud-wa-jalut", "qital": "salah-al-din-wa-al-quds", "kathir": "salah-al-din-wa-al-quds",
         "yad": "salah-al-din-wa-al-quds", "nafs": "salah-al-din-wa-al-quds", "bilad": "salah-al-din-wa-al-quds",
         "hamala": "salah-al-din-wa-al-quds", "rajul": "talkhis-al-miftah", "nasara": "wasiyyat-abi-hanifa-samti", "ahad": "wasiyyat-abi-yusuf-l5",
         "thamani": "al-kafiya", "ism": "adam-wa-iblis", "dhalika": "alb-arslan-wa-malazgird", "amir": "al-kafiya"}
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
 "tatar": {"lemma": "التَّتَار", "pos": "propn", "gloss": {"en": "the Tatars — the name the Arabic chronicles of the 7th/13th century give the Mongol armies", "tr": "Tatarlar — 7./13. yüzyıl Arapça kroniklerinin Moğol ordularına verdiği ad"}, "level": 5},
 "qutuz": {"lemma": "قُطُز", "pos": "propn", "gloss": {"en": "Quṭuz — al-Malik al-Muẓaffar Sayf al-Dīn Quṭuz, Mamluk sultan of Egypt (r. 657–658 / 1259–1260), victor of ʿAyn Jālūt; written here as a diptote (a three-letter foreign name with a voweled middle)", "tr": "Kutuz — el-Melikü'l-Muzaffer Seyfüddin Kutuz, Mısır'ın Memlük sultanı (s. 657–658 / 1259–1260), Ayn Câlût'un galibi; burada gayr-i munsarif yazılır (orta harfi harekeli üç harfli yabancı isim)"}, "level": 6},
 "baybars": {"lemma": "بَيْبَرْس", "pos": "propn", "gloss": {"en": "Baybars — Rukn al-Dīn Baybars al-Bunduqdārī, Mamluk emir and later sultan (r. 658–676 / 1260–1277); a diptote (ʿalamiyya + ʿujma)", "tr": "Baybars — Rükneddin Baybars el-Bundukdârî, Memlük emîri, sonra sultan (s. 658–676 / 1260–1277); gayr-i munsarif (alemiyet + ucmet)"}, "level": 6},
 "mamluk": {"lemma": "مَمْلُوك", "root": "م ل ك", "pos": "noun", "gloss": {"en": "a mamlūk — literally «owned» (the passive participle of مَلَكَ): a slave-soldier; الْمَمَالِيك, the Mamluks who ruled Egypt and Syria", "tr": "memlûk — lafzen «sahip olunan» (مَلَكَ'nin ism-i mef'ûlü): köle asker; الْمَمَالِيك, Mısır ve Şam'a hükmeden Memlükler"}, "level": 5, "plural": "مَمَالِيك"},
 "muqaddima": {"lemma": "مُقَدِّمَة", "root": "ق د م", "pos": "noun", "gloss": {"en": "the vanguard (of an army) — the part that marches in front; (of a book) the introduction", "tr": "öncü kuvvet (ordunun) — önden giden kısım; (kitabın) mukaddimesi, girişi"}, "level": 5},
 "sittumia": {"lemma": "سِتُّمِائَة", "root": "س ت ت", "pos": "noun", "gloss": {"en": "six hundred", "tr": "altı yüz"}, "level": 4},
 "ayn-jalut": PHRASE("عَيْنُ جَالُوتَ", 6, "ʿAyn Jālūt — a spring and the place around it in the Jezreel valley of Palestine, near Baysān, where the Mamluks defeated the Mongols in Ramaḍān 658 / September 1260",
    "Ayn Câlût — Filistin'de Cezreel ovasında, Beysân yakınında bir pınar ve çevresi; Memlükler Moğolları 658 Ramazanı / Eylül 1260'ta burada yendi",
    "literally «the Spring of Jālūt (Goliath)»", "lafzen «Câlût Pınarı»",
    "A place-name built as an idafa: عَيْن «spring» takes the case of its seat (عَيْنُ in raf', عَيْنِ in jarr), and جَالُوت stays its second term — a diptote (a foreign proper name), so its jarr shows as a fatha with no tanwin: عَيْنُ جَالُوتَ، يَوْمُ عَيْنِ جَالُوتَ.",
    "İzâfetle kurulmuş bir yer adı: عَيْن «pınar» bulunduğu yerin i'râbını alır (refte عَيْنُ, cerde عَيْنِ); جَالُوت ise muzâfun ileyh olarak kalır — gayr-i munsarif (yabancı özel isim), bu yüzden cerri tenvinsiz fetha ile görünür: عَيْنُ جَالُوتَ، يَوْمُ عَيْنِ جَالُوتَ."),
}
# a key is a global claim: a NEW key must not already name something else on the shelf (nor in a sibling's staged package)
_STAGED = {}
for d in OUT_ROOT.iterdir() if OUT_ROOT.exists() else []:
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
for k, e in NEW_GLOSS.items():
    hit = [p for p in PREF if k in _G[p]]
    assert not hit, (k, hit)
    for p, g in _STAGED.items():
        if k in g:
            assert g[k].get("lemma") == e["lemma"], ("staged clash", k, p, g[k].get("lemma"))

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
    else: GLOSS[k] = json.loads(json.dumps(e))
assert not missing, missing
# same lemma and key as the shelf; the gloss shown in THIS story names the sense its sentences use
GLOSS["jalut"]["gloss"] = {"en": "Jālūt (Goliath) — the giant champion slain by Dāwūd; here in the place-name عَيْنُ جَالُوتَ «the Spring of Goliath»; a diptote (a foreign proper name)",
                           "tr": "Câlût (Golyat) — Dâvûd'un öldürdüğü dev savaşçı; burada عَيْنُ جَالُوتَ «Câlût Pınarı» yer adında; gayr-i munsarif (yabancı özel isim)"}
GLOSS["bas"]["gloss"] = {"en": "might, valour in war (بَأْسًا after an elative: «in might»); also violent distress", "tr": "savaştaki şiddet, yiğitlik (ism-i tafdîlden sonra بَأْسًا: «şiddet bakımından»); ayrıca sıkıntı, şiddet"}
GLOSS["mashhur"]["gloss"] = {"en": "well-known, famous (the passive participle of شَهَرَ)", "tr": "meşhur, tanınmış (شَهَرَ'nin ism-i mef'ûlü)"}
GLOSS["hamala"]["gloss"] = {"en": "to carry; (with عَلَى) to charge an enemy", "tr": "taşımak, yüklenmek; (عَلَى ile) düşmanın üzerine saldırmak"}
GLOSS["dhakara"]["gloss"] = {"en": "to mention, to report; to remember", "tr": "anmak, zikretmek; hatırlamak"}
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
 "title": {"ar": "عَيْنُ جَالُوتَ", "en": "ʿAyn Jālūt", "tr": "Ayn Câlût"},
 "subtitle": {"ar": "سُقُوطُ بَغْدَادَ، وَسُلْطَانٌ يَخْرُجُ إِلَى عَدُوِّهِ وَلَا يَنْتَظِرُهُ، وَيَوْمٌ مِنْ أَيَّامِ الْإِسْلَامِ — قِصَّةٌ لِلْمُسْتَوَى السَّادِسِ",
              "en": "The fall of Baghdad, a sultan who marches out to his enemy rather than wait for him, and one of the great days of Islam — a story for the sixth level",
              "tr": "Bağdat'ın düşüşü, düşmanını beklemeyip üzerine yürüyen bir sultan ve İslâm'ın büyük günlerinden biri — altıncı seviye için bir hikâye"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى السَّادِسُ) لِخَبَرِ دُخُولِ التَّتَارِ بَغْدَادَ سَنَةَ ٦٥٦ هـ، وَخُرُوجِ السُّلْطَانِ قُطُزَ إِلَيْهِمْ، وَوَقْعَةِ عَيْنِ جَالُوتَ فِي رَمَضَانَ سَنَةَ ٦٥٨ هـ / ١٢٦٠ م، عَلَى مَا يَتَّفِقُ عَلَيْهِ مَنْ رَوَاهُ: ابْنُ كَثِيرٍ فِي «الْبِدَايَةِ وَالنِّهَايَةِ»، وَالْمَقْرِيزِيُّ فِي «السُّلُوكِ لِمَعْرِفَةِ دُوَلِ الْمُلُوكِ». النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ تِلْكَ الْكُتُبِ، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا قَوْلٌ يُنْسَبُ إِلَى أَحَدٍ. وَتُرِكَتْ نُصُوصُ الرَّسَائِلِ وَالْخُطَبِ، وَمَا صُنِعَ بِالرُّسُلِ، وَأَعْدَادُ الْجُيُوشِ وَالْقَتْلَى، وَاسْمُ أَمِيرِ التَّتَارِ، وَخَبَرُ مَقْتَلِ قُطُزَ؛ وَاكْتُفِيَ بِأَنَّهُ مَاتَ بَعْدَ ذٰلِكَ بِقَلِيلٍ.",
  "en": "ORIGINAL Level-6 graded Arabic in a classical narrative register: the Mongol («Tatar») capture of Baghdad in 656 AH, Sultan Quṭuz's decision to march out against them, and the battle of ʿAyn Jālūt in Ramaḍān 658 AH / September 1260 CE, RETOLD FREELY along the well-attested core of the classical accounts — Ibn Kathīr (al-Bidāya wa-l-nihāya, the events of 656 and 658) and al-Maqrīzī (al-Sulūk li-maʿrifat duwal al-mulūk). No sentence is a quotation from these works; no āya or ḥadīth is quoted; no words are put in a historical person's mouth. Left out: the texts of the letters and the speeches (including the sultan's cry on the field), the fate of the envoys, the sizes of the armies and the numbers of the slain, the Mongol commander's name, and the manner of Quṭuz's death — one neutral line says only that he died soon after. The narrator's two judgements (the oath on the soundness of the decision, and what held the men firm) are marked as the narrator's.",
  "tr": "ÖZGÜN 6. seviye Arapça, klasik anlatı üslûbunda: Moğolların («Tatarların») 656 h. yılında Bağdat'ı alışı, Sultan Kutuz'un onların üzerine yürüme kararı ve 658 h. Ramazanı / Eylül 1260 m.'de Ayn Câlût savaşı, klasik kaynakların — İbn Kesîr (el-Bidâye ve'n-Nihâye, 656 ve 658 yılları olayları) ve Makrîzî (es-Sülûk li-ma'rifeti düveli'l-mülûk) — üzerinde birleştiği sağlam çekirdeğe bağlı kalınarak SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bu eserlerden alıntı değildir; hiçbir âyet veya hadis aktarılmamıştır; hiçbir tarihî şahsın ağzına söz konmamıştır. Dışarıda bırakılanlar: mektupların ve konuşmaların metinleri (sultanın savaş meydanındaki nidası dahil), elçilerin akıbeti, ordu büyüklükleri ve ölü sayıları, Moğol komutanının adı ve Kutuz'un ölüm şekli — yalnızca kısa süre sonra vefat ettiğini söyleyen tarafsız bir cümle vardır. Anlatıcının iki hükmü (kararın isabetine dair yemin ve askerleri sebat ettiren şey) anlatıcıya aittir.",
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
