"""Author content/samples/alb-arslan-wa-malazgird — «أَلْب أَرْسَلَانُ وَمَلَاذْكِرْد», an ORIGINAL historical story at Level 6 (Master).

ORIGINAL graded Arabic in a classical narrative register, kept to the well-attested core of the year 463 AH / 1071 CE:
Romanos IV Diogenes (أَرْمَانُوس, as the Arabic chronicles name him) marches east with a great host; Sultan Alp Arslan,
far from most of his troops and with a small force, sends to ask for a truce and is refused; Ibn al-Athīr reports that the
sultan chose to meet them on Friday, at the hour when the preachers pray on the minbars for the Muslims (PRESENTED AS
REPORTED, with Ibn al-Athīr named in the sentence); the Byzantine army is routed and the emperor captured; the sultan speaks
with him and treats him with honour, makes terms with him for a ransom and the release of the Muslim captives, and sets him
free with an escort; the victory opens the lands of the Rūm (Anatolia) to the Muslims. The event is told by Ibn al-Athīr
(al-Kāmil fī al-Taʾrīkh, the events of 463) and Sibṭ ibn al-Jawzī (Mirʾāt al-Zamān); it is RETOLD FREELY here — no sentence is
a quotation from them, no āya or ḥadīth is quoted, no words are put in a historical person's mouth. Left out on purpose:
the famous captor–captive dialogue (its wording varies across the reports), the army sizes, the ransom figures, the name of
the sultan's faqīh, the emperor's later fate, and the battlefield's name in the body (its classical spellings vary —
منازجرد / ملازكرد / ملاذكرد — so it stands only in the title, in the form the brief gives).

NAMES (how the shelf handles a foreign name, followed here): a foreign proper name is a diptote for ʿalamiyya + ʿujma,
written «عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ» with the grammar tag mamnu-min-sarf (story_kit DIPT; قُسْطَنْطِينُ in qiṣaṣ 4;
CLAUDE.md «The foreign names are diptotes whatever the lexicon knows»). أَرْمَانُوس follows that line exactly. أَلْب أَرْسَلَان is
TWO printed words: following the shelf's two-token compound name (مَعْدِي كَرِب, talkhīṣ 56), both tokens state the compound's
one office, the first word is spoken with a quiescent end and carries no case vowel, and the case shows on أَرْسَلَان alone —
a diptote for ʿalamiyya + ʿujma: أَرْسَلَانُ (raf'), أَرْسَلَانَ (nasb AND jarr), never tanwin. Each word has its own lexicon
entry (Turkish alp «hero», arslan «lion») and the pair carries the phrase key alb-arslan (CLAUDE.md «Idioms/phrases»).

Five chapters, thirty sentences. The Level-6 constructions: long periodic sentences; فَبَيْنَمَا … إِذْ …; ثُمَّ إِنَّهُ / ثُمَّ إِنَّ;
فَإِذَا of surprise; ḥaṣr by إِنَّمَا (three times, the restricted term last) and by negation + إِلَّا (لَمْ يَكُنْ … إِلَّا، مَا زَادَتْهُ
… إِلَّا، مَا حَمَلَهُ … إِلَّا) and أَبَى إِلَّا (an exception emptied after a verb negative in meaning); كَمِ الْخَبَرِيَّةُ (four times);
the oath لَعَمْرِي with its answer; the mafʿūl muṭlaq (رَدًّا قَبِيحًا، نَصْرًا عَظِيمًا، إِكْرَامًا عَظِيمًا) and its deputy (قِتَالًا شَدِيدًا
after اقْتَتَلُوا); the mafʿūl lahu (خَوْفًا، رَجَاءَ); tamyīz after an elative (أَقَلُّ … عَدَدًا); ḥāl single and as a clause (يُرِيدُ …،
وَالْعَدُوُّ قَدْ قَرُبَ، وَهُوَ يَعْلَمُ …، وَالنَّاسُ يَدْعُونَ مَعَهُ، يَظُنُّ …) and a ḥāl fronted from an indefinite; kāna tāmma; badal
al-baʿḍ (أَحَدُهُمَا); مَا زَالَ with its khabar.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf, every verb's paradigm
is the shelf's own (no new verb), and the new entries are only those in NEW_GLOSS (the names, هُدْنَة، خَطِيب، التُّرْك, and two
name-phrases). Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_alb_arslan_wa_malazgird.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "alb-arslan-wa-malazgird"
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
def W(t3, *more):
    """join note triples"""
    out = list(t3)
    for m in more:
        out = [a + b for a, b in zip(out, m)]
    return dict(note_ar=out[0], note_en=out[1], note_tr=out[2])

# ---- the names --------------------------------------------------------------------------------------------------
AJAM = ("عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ",
        "a foreign proper name, a diptote by ʿalamiyya + ʿujma (proper name + foreign origin)",
        "yabancı özel isim, alemiyet ve ucmet sebebiyle gayr-i munsarif")
def ARMANUS(role, punct=None):
    """أَرْمَانُوس — Romanos IV, as the Arabic chronicles write him: ʿalam + ʿujma, so no tanwin and a fatḥa for jarr"""
    if role == "fail":
        return FAIL("أَرْمَانُوسُ", "armanus", "propn", ["mamnu-min-sarf"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ",
                    note_ar=" — " + AJAM[0], note_en=", with no tanwin — " + AJAM[1], note_tr=", tenvinsiz — " + AJAM[2], punct=punct)
    if role == "ismk":
        return ISMK("أَرْمَانُوسُ", "armanus", "propn", ["mamnu-min-sarf"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", muakhkhar=True,
                    note_ar=" — " + AJAM[0], note_en=", with no tanwin — " + AJAM[1], note_tr=", tenvinsiz — " + AJAM[2], punct=punct)
    if role == "majr":
        return MAJR("أَرْمَانُوسَ", "armanus", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR,
                    note_ar=" — " + AJAM[0], note_en=" — by a fatha standing in for the kasra: " + AJAM[1], note_tr=" — kesre yerine fetha ile: " + AJAM[2], punct=punct)
    raise ValueError(role)

ALB_ROLE = {
 # role: (first-word head ar/en/tr, last-word line ar/en/tr, grammar)
 "badal": (("بَدَلٌ مِنَ «السُّلْطَانُ»", "A badal of «the sultan»", "«Sultan»dan bedel"),
           ("بَدَلٌ مِنَ «السُّلْطَانُ» مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", "A badal of «the sultan», in raf' by the damma with no tanwin", "«Sultan»dan bedel, tenvinsiz damme ile merfû"),
           ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"]),
 "ism_anna": (("اسْمُ أَنَّ", "The noun of أَنَّ", "Enne'nin ismi"),
              ("اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", "The noun of أَنَّ, in nasb by the fatha with no tanwin", "Enne'nin ismi, tenvinsiz fetha ile mansûb"),
              ["inna-wa-akhawatuha"]),
 "majr": (("مَجْرُورٌ بِإِلَى", "In jarr after إِلَى", "İlâ ile mecrûr"),
          ("مَجْرُورٌ بِإِلَى، وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ مِنْ غَيْرِ تَنْوِينٍ", "In jarr after إِلَى, its sign a fatha standing in for the kasra, with no tanwin", "İlâ ile mecrûr; alâmeti kesre yerine tenvinsiz fetha"),
          ["huruf-jarr"]),
 "fail": (("فَاعِلٌ", "The doer", "Fâil"),
          ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", "The doer, in raf' by the damma with no tanwin", "Fâil, tenvinsiz damme ile merfû"),
          ["fail"]),
}
def ALB_ARSLAN(role, punct=None):
    """أَلْب أَرْسَلَان — two printed words, one compound name in one seat; the case shows on its last word only"""
    head, last, g = ALB_ROLE[role]
    t1 = tok("أَلْب", "alb", "propn", g,
        head[0] + " — وَالْمُرَادُ الْعَلَمُ الْمُرَكَّبُ «أَلْب أَرْسَلَان» كُلُّهُ، وَهٰذَا جُزْؤُهُ الْأَوَّلُ: يُلْفَظُ سَاكِنَ الْآخِرِ، وَلَا تَظْهَرُ عَلَيْهِ حَرَكَةُ إِعْرَابٍ، وَإِنَّمَا يَظْهَرُ الْإِعْرَابُ عَلَى آخِرِ الْمُرَكَّبِ.",
        head[1] + " — the office belongs to the whole compound name «Alp Arslan»; this is its first word, spoken with a quiescent end: no case vowel shows on it — the case shows on the last word of the compound.",
        head[2] + " — bu görev «Alp Arslan» birleşik özel isminin bütününe aittir; bu onun ilk kelimesidir: sonu sâkin okunur, üzerinde i'râb harekesi görünmez — i'râb birleşiğin son kelimesinde görünür.")
    t2 = tok({"badal": "أَرْسَلَانُ", "ism_anna": "أَرْسَلَانَ", "majr": "أَرْسَلَانَ", "fail": "أَرْسَلَانُ"}[role], "arslan", "propn", g + ["mamnu-min-sarf"],
        last[0] + "، ظَهَرَتْ عَلَى آخِرِ الْعَلَمِ الْمُرَكَّبِ «أَلْب أَرْسَلَان» — " + AJAM[0] + " (اسْمٌ تُرْكِيٌّ).",
        last[1] + ", shown on the last word of the compound name «Alp Arslan» — " + AJAM[1] + " (a Turkish name).",
        last[2] + "; i'râb «Alp Arslan» birleşik isminin son kelimesinde görünür — " + AJAM[2] + " (Türkçe bir isim).", punct=punct)
    return [PH(t1, "alb-arslan"), t2]

ARBAUMIA = lambda punct=None: tok("وَأَرْبَعِمِائَةٍ", "arbaumia", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
    "الْوَاوُ عَاطِفَةٌ، وَ«أَرْبَعِ» مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ«مِائَةٍ» مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَحُذِفَتِ التَّاءُ مِنْ أَرْبَعٍ لِأَنَّ الْمِائَةَ مُؤَنَّثَةٌ، وَيُكْتَبُ الْجُزْآنِ كَلِمَةً وَاحِدَةً.",
    "The waw conjoins; «four» is conjoined, in jarr and annexed, and «hundred» is its second term, in jarr — four has no ta because «hundred» is feminine, and the two parts are written as one word.",
    "Vâv atıf; «dört» ma'tûf, mecrûr, muzâf; «yüz» muzâfun ileyh, mecrûr — «yüz» müennes olduğu için erbaʿ tâsızdır; iki parça bitişik yazılır.",
    punct=punct, segments=[seg("وَ", "wa", "conj"), seg("أَرْبَعِمِائَةٍ", "arbaumia", "noun")])

# ---- particles and frames the kit does not hold (most copied from author_salah_al_din_wa_al_quds.py) --------------
def KAM(full="وَكَمْ", pre="istinaf"):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins a second exclamation; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "Vâv atıf; "}[pre]
    return tok(full, "kam", "pron", ["al-kinayat-wal-zuruf-al-mabniyya", "al-mabni-al-lazim-al-kinayat-wal-mutadamminat-wal-zuruf", "mubtada-khabar"],
        pre_ar + "كَمْ خَبَرِيَّةٌ بِمَعْنَى «كَثِيرٍ» مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، مُضَافٌ — وَالْجُمْلَةُ بَعْدَ تَمْيِيزِهَا خَبَرُهَا.",
        pre_en + "كَمْ here is the كَمْ OF REPORT (khabariyya) meaning «many a»: built on sukun, in the seat of raf' as the mubtada, annexed to its specifier — the verbal clause after the specifier is its khabar.",
        pre_tr + "kem burada haberiyye kem'dir («nice, nice nice»): sükûn üzere mebnî, mübtedâ olarak mahallen merfû, temyîzine muzâf — temyîzinden sonraki fiil cümlesi haberidir.",
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
FA_IDHA = lambda: tok("فَإِذَا", "idha", "part", ["huruf-al-shart-fil-kafiya", "al-kinayat-wal-zuruf-al-mabniyya"],
    "الْفَاءُ عَاطِفَةٌ، وَإِذَا لِلْمُفَاجَأَةِ، حَرْفٌ عِنْدَ قَوْمٍ وَظَرْفُ مَكَانٍ عِنْدَ آخَرِينَ، وَلَا تَدْخُلُ إِلَّا عَلَى الْجُمْلَةِ الِاسْمِيَّةِ.",
    "The fa conjoins; إِذَا OF SURPRISE («and lo!») — a particle for some grammarians, an adverb of place for others; it enters only a nominal clause.",
    "Fâ atıf; müfâcee izâ'sı («bir de baktı ki») — kimine göre harf, kimine göre mekân zarfı; yalnızca isim cümlesine girer.",
    segments=[seg("فَ", "fa", "conj"), seg("إِذَا", "idha", "part")])
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
    """بَيْنَهُمَا، مَعَهُ، وَرَاءَهُمْ، بَعْدَهُ: a ẓarf annexed to its pronoun"""
    return tok(full, lex, "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
        "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        "An adverb of " + kind_en + ", in nasb and annexed to the attached pronoun, which fills the seat of jarr" + note_en + ".",
        kind_tr + " zarfı, mansûb, bitişik zamire muzâf; zamir mahallen mecrûr" + note_tr + ".", punct=punct,
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def MAA_X(full, enc, note=("", "", ""), punct=None):
    return ZARF_ENC(full, "maa", enc, punct=punct, note_ar=note[0], note_en=note[1], note_tr=note[2])
MAA_SILA = (" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ تَقْدِيرُهُ «اسْتَقَرَّ»، وَهُوَ صِلَةُ الْمَوْصُولِ", "; the adverb hangs on an omitted «is (found)», and that is the relative's ṣila", "; zarf mahzûf «bulunan»a müteallik; mevsûlün sılasıdır")
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
KANAT_TAMMA = lambda: tok("كَانَتْ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs"],
    "كَانَ هُنَا فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «جَاءَتْ» مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، يَكْتَفِي بِفَاعِلِهِ وَلَا خَبَرَ لَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا إِلَيْهَا.",
    "كَانَ here is COMPLETE (tāmma), meaning «came, arrived»: a past verb built on fatha, the ta marking the feminine; it is satisfied with a doer and takes no predicate — the clause is annexed to لَمَّا, in the seat of jarr.",
    "Kâne burada tâmmedir, «geldi» anlamında: fetha üzere mebnî mâzî, tâ te'nîs içindir; fâiliyle yetinir, haber almaz — cümle lemmâ'ya muzâfun ileyh, mahallen mecrûr.")
KANAT_HID_INNA = lambda: tok("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ" + KH_INNA_CL[0] + ".",
    "كَانَ, the defective past verb, built on fatha; the ta marks the feminine and its noun is the hidden «they» (a broken plural takes a feminine singular pronoun)" + KH_INNA_CL[1] + ".",
    "Nâkıs mâzî kâne, fetha üzere mebnî; tâ te'nîs içindir, ismi gizli zamir «o» (kırık cem' müfred müennes zamir alır)" + KH_INNA_CL[2] + ".")
SARAT_X = lambda: tok("صَارَتْ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، يَعُودُ عَلَى بِلَادِ الرُّومِ.",
    "صَارَ «became», a sister of كَانَ, built on fatha; the ta marks the feminine, and its noun is the hidden «they», returning to the lands of the Rūm.",
    "Sâra «oldu», kâne'nin kardeşi, fetha üzere mebnî; tâ te'nîs içindir, ismi Rum diyarına dönen gizli zamir «o».")
ZALA_X = lambda: tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
    "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ.",
    "زَالَ, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb — after a negation it means «never ceased, still».",
    "Zâle, kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; ismini ref, haberini nasb eder — nefiyle birlikte devam bildirir («hâlâ, hep»).")
FA_INNA = lambda: tok("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
    "The fa gives the reason («for»); إِنَّ «indeed» puts its noun in nasb and raises its predicate.", "Fâ ta'lîl içindir («çünkü»); inne: ismini nasb, haberini ref eder.",
    segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")])
FA_QAD = lambda: tok("فَقَدْ", "qad", "part", [], "الْفَاءُ لِلتَّعْلِيلِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The fa gives the reason («for»); قَدْ affirms the past verb after it.",
    "Fâ ta'lîl içindir («çünkü»); kad tahkîk harfi.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")])
def ANNA_X(note=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + note[0] + ".",
        "أَنَّ «that», the verb-like particle that builds a masdar: it puts its noun in nasb and raises its predicate" + note[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + note[2] + ".")
SADDA_ZANNA = (" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «ظَنَّ»", "; أَنَّ with its clause stands for a masdar that fills both objects of «thought»", "; enne ve sonrası, «zannetti»nin iki mef'ûlünün yerini tutan müevvel masdardır")
def ISM_ANNA_ENC(full, lex, enc, extra=None, which="anna"):
    """جُيُوشَهُ، جُنْدَهُ: the noun of إِنَّ / أَنَّ annexed to its pronoun"""
    p_ar, p_tr = {"inna": ("إِنَّ", "İnne"), "anna": ("أَنَّ", "Enne")}[which]
    return tok(full, lex, "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        "اسْمُ " + p_ar + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        "The noun of " + p_ar + ", in nasb; annexed to the attached pronoun, which fills the seat of jarr.",
        p_tr + "'nin ismi, mansûb; bitişik zamire muzâf, zamir mahallen mecrûr.",
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def WA_HAL_MUB(full, lex):
    """وَالْعَدُوُّ، وَالنَّاسُ: the waw of hal opening a nominal clause"""
    stem = full[2:]
    return tok(full, lex, "noun", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"],
        "الْوَاوُ حَالِيَّةٌ، وَ" + stem + " مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ بَعْدَ الْوَاوِ فِي مَحَلِّ نَصْبٍ حَالٌ.",
        "The waw opens a hal clause; the noun after it is the mubtada, in raf' — the nominal clause after the waw is a hal, in the seat of nasb.",
        "Hâl vâvı; sonraki isim mübtedâ, merfû — vâvdan sonraki isim cümlesi hâl olarak mahallen mansûb.",
        segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "noun")])
def MAN_X(seat_ar, seat_en, seat_tr, extra, sila=("وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ", "the clause after it is its ṣila", "sonraki cümle sılasıdır")):
    return tok("مَنْ", "man-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، " + sila[0] + ".",
        "The relative pronoun «those who», built on sukun, in the seat of " + seat_en + "; " + sila[1] + ".",
        "İsm-i mevsûl «kimse(ler)», sükûn üzere mebnî, mahallen " + seat_tr + "; " + sila[2] + ".")
def BI_MAN(note=("", "", "")):
    return tok("بِمَنْ", "bi", "prep", ["huruf-jarr", "ism-mawsul"],
        "الْبَاءُ حَرْفُ جَرٍّ" + note[0] + "، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالظَّرْفُ بَعْدَهُ صِلَتُهُ.",
        "The ba is a jarr letter" + note[1] + "; «those who» is the relative pronoun, built on sukun, in the seat of jarr — the adverb after it is its ṣila.",
        "Bâ cer harfi" + note[2] + "; «men» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr — sonraki zarf sılasıdır.",
        segments=[seg("بِ", "bi", "prep"), seg("مَنْ", "man-mawsula", "pron")])
FIMAN = lambda: tok("فِيمَنْ", "fi", "prep", ["huruf-jarr", "ism-mawsul"],
    "فِي حَرْفُ جَرٍّ، وَ«مَنْ» اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ مُقَدَّمٌ.",
    "فِي is a jarr letter; «those who» is the relative pronoun, built on sukun, in the seat of jarr, and the clause after it is its ṣila — the jarr phrase is the FRONTED predicate of كَانَ.",
    "Fî cer harfi; «men» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr; sonraki cümle sılasıdır — câr-mecrûr kâne'nin öne alınmış haberidir.",
    segments=[seg("فِي", "fi", "prep"), seg("مَنْ", "man-mawsula", "pron")])
def LI_MUSLIMIN(note=("", "", "")):
    return tok("لِلْمُسْلِمِينَ", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim"],
        "اللَّامُ حَرْفُ جَرٍّ، وَالْمُسْلِمِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ" + note[0] + ".",
        "The lam is a jarr letter; «the Muslims» is in jarr by the ya — a sound masculine plural" + note[1] + ".",
        "Lâm cer harfi; «Müslümanlar» cem-i müzekker sâlim olduğu için yâ ile mecrûr" + note[2] + ".",
        segments=[seg("لِ", "li", "prep"), seg("الْمُسْلِمِينَ", "muslim", "noun")])
MUSLIMUN_F = lambda punct=None: FAIL("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign="بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the waw, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için vâv ile", punct=punct)
R_MAJR = ("مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", "huruf-jarr")
R_MI = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", "idafa-definiteness")
MUSLIMIN_J = lambda punct=None: SALIM_J("الْمُسْلِمِينَ", "muslim", R_MAJR, punct=punct)
MUSLIMIN_MI = lambda punct=None: SALIM_J("الْمُسْلِمِينَ", "muslim", R_MI, punct=punct)
def MUTLAQ_X(full, lex, verb_ar, verb_en, verb_tr, punct=None):
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «" + verb_ar + "»، يُؤَكِّدُ فِعْلَهُ، وَبِنَعْتِهِ يُبَيِّنُ نَوْعَهُ.",
        "The absolute object (maf'ul mutlaq), in nasb — the masdar of «" + verb_en + "»: it strengthens its verb, and with its adjective it tells the KIND.",
        "Mef'ûlün mutlak, mansûb — «" + verb_tr + "» fiilinin masdarı: fiilini pekiştirir, sıfatıyla da türünü bildirir.", punct=punct)
LAAMRI = lambda: tok("وَلَعَمْرِي", "amr-qasam", "noun", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "mubtada-khabar", "ya-al-mutakallim", "hadhf-wa-taqdir"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْخَبَرُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي؛ وَهٰذِهِ صِيغَةُ قَسَمٍ.",
    "The waw opens a new sentence; the lam is the lam of ibtidāʾ; عَمْر «life» is the mubtada, in raf' by a damma estimated before the speaker's ya (the kasra the ya demands holds its place), annexed to the ya — its predicate is dropped by rule («[is my oath]»): this is a FORM OF OATH, «by my life».",
    "Vâv isti'nâf içindir; lâm ibtidâ lâmıdır; «ömür» mübtedâ, mütekellim yâ'sından önce takdîrî damme ile merfû (yerini yâ'nın gerektirdiği kesre tutmuştur), yâ'ya muzâf — haberi vücûben hazfedilmiştir («yeminimdir»): bu bir yemin kalıbıdır, «ömrüme andolsun».",
    segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-ibtida", "part"), seg("عَمْرِ", "amr-qasam", "noun"), seg("ي", "pron-1s", "pron")])
YAWMAIDHIN = lambda note=("", "", ""), punct=None: tok("يَوْمَئِذٍ", "yawmaidhin", "noun", ["maful-fih", "idafa-definiteness", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"],
    "يَوْمَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (وَيَجُوزُ بِنَاؤُهُ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى مَبْنِيٍّ)، مُضَافٌ، وَإِذْ ظَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ مَحْذُوفَةٍ، وَكُسِرَتِ الذَّالُ لِالْتِقَاءِ السَّاكِنَيْنِ" + note[0] + ".",
    "«On that day»: يَوْمَ is an adverb of time in nasb (it may also be built on fatha, being annexed to a built word), annexed to إِذْ, a built adverb in the seat of jarr; the tanwin stands for a dropped clause («the day when [they met]») and the dhal takes kasra where two quiescents met" + note[1] + ".",
    "«O gün»: yevme mansûb zaman zarfı (mebnî bir kelimeye muzâf olduğu için fetha üzere mebnî de olabilir), iz'e muzâf; iz mebnî zarf, mahallen mecrûr; tenvin hazfedilmiş bir cümlenin yerini tutar, iki sâkin karşılaştığı için zâl kesre aldı" + note[2] + ".", punct=punct)

# ---- a few verb shapes the kit does not hold ----------------------------------------------------------------------
YALQAHUM = lambda: tok("يَلْقَاهُمْ", "laqiya", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"],
    "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالضَّمِيرُ لِلرُّومِ.",
    "Present verb put in nasb by أَنْ, its fatha estimated on the alif (it cannot be voiced there); the doer «he» is hidden, and the attached «them» (the Rūm) is its object, in the seat of nasb.",
    "En ile mansûb muzâri, fethası elif üzerinde takdîrî (telaffuzu mümkün değil); fâil gizli zamir «o»; bitişik «onları» (Rumları) mef'ûlün bih, mahallen mansûb.",
    segments=[seg("يَلْقَا", "laqiya", "verb"), seg("هُمْ", "pron-3mp", "pron")])
YADU = lambda: tok("يَدْعُو", "daa", "verb", ["mudari-marfu", "naqis-verbs"],
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ، وَالْفَاعِلُ بَعْدَهُ" + SILA_[0] + ".",
    "Present verb in raf', its damma estimated on the waw (too heavy to voice); its doer follows" + SILA_[1] + ".",
    "Merfû muzâri, dammesi vâv üzerinde takdîrî (ağırlık sebebiyle); fâili ondan sonra gelir" + SILA_[2] + ".")
YAFU = lambda: tok("يَعْفُ", "afa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْوَاوِ، وَأَصْلُهُ: يَعْفُو)، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
    "Present verb in jazm by لَمْ, its sign the DROPPED weak letter (the waw of يَعْفُو); the doer «he» is hidden.",
    "Lem ile meczûm muzâri; alâmeti illet harfinin (yaʿfû'daki vâvın) hazfi; fâil gizli zamir «o».")
QITAL_NAIB = lambda: tok("قِتَالًا", "qital", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
    "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ «قَاتَلَ»، وَهُوَ يُلَاقِي «اقْتَتَلُوا» فِي مَادَّتِهِ وَمَعْنَاهُ فَنَابَ عَنْ مَصْدَرِهِ «اقْتِتَالًا»، وَبِنَعْتِهِ يُبَيِّنُ النَّوْعَ.",
    "Standing in for the absolute object, in nasb — the masdar of قَاتَلَ: it shares the root and the meaning of «fought one another» and takes the place of that verb's own masdar (اقْتِتَال); with its adjective it tells the KIND of fighting.",
    "Mef'ûlün mutlakın nâibi, mansûb — kâtele'nin masdarı: «birbirleriyle savaştılar» fiiliyle kökte ve anlamda buluştuğu için onun masdarının (iktitâl) yerini tuttu; sıfatıyla savaşın türünü bildirir.")

# ============================================ the text ============================================
TITLES = [{"ar": "خُرُوجُ مَلِكِ الرُّومِ", "en": "The King of the Rūm Sets Out", "tr": "Rum Kralı Yola Çıkıyor"},
          {"ar": "الْهُدْنَةُ الْمَرْدُودَةُ", "en": "The Truce Refused", "tr": "Geri Çevrilen Ateşkes"},
          {"ar": "سَاعَةُ الْجُمُعَةِ", "en": "The Friday Hour", "tr": "Cuma Vakti"},
          {"ar": "الْمَلِكُ الْأَسِيرُ", "en": "The Captive King", "tr": "Esir Kral"},
          {"ar": "بَابٌ إِلَى بِلَادِ الرُّومِ", "en": "A Door into the Lands of the Rūm", "tr": "Anadolu'ya Açılan Kapı"}]

# ---- Chapter 1 — خُرُوجُ مَلِكِ الرُّومِ ----
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Sultan Alp Arslan was one of the kings of the Turks, who had come to rule many lands among the lands of the Muslims.",
  "tr": "Sultan Alparslan Türk hükümdarlarından biriydi; Müslüman diyarlarından pek çok ülkeye hâkim olmuştu."},
 "tokens": [KANA("كَانَ"), ISMK("السُّلْطَانُ", "sultan"), *ALB_ARSLAN("badal"),
  KHK("مَلِكًا", "malik-king"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَلِكًا»", "; the jarr phrase hangs on an omitted adjective of «a king»", " — câr-mecrûr «hükümdar»ın mahzûf na'tına müteallik")),
  MAJR("مُلُوكِ", "malik-king", extra=["jam-taksir"], note_ar="، مُضَافٌ — جَمْعُ مَلِكٍ", note_en=", annexed — the plural of «king»", note_tr=", muzâf — melik'in cem'i"),
  MUDAF_ILAYH("التُّرْكِ", "turk", "propn", punct="،"),
  QAD(), MADI("مَلَكَ", "malaka", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِـ«مَلِكًا»", note_en="; the clause is a second adjective of «a king», in the seat of nasb", note_tr="; cümle «hükümdar»ın ikinci na'tı, mahallen mansûb"),
  MAFUL("بِلَادًا", "bilad"), NAAT("كَثِيرَةً", "kathir", "nasb"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«بِلَادًا»", "; the jarr phrase is a second adjective of «lands»", " — câr-mecrûr «ülkeler»in ikinci na'tına müteallik")),
  MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUSLIMIN_MI(punct=".")]})
S1.append({"id": "s2", "translation": {
  "en": "When the year 463 (of the Hijra) came, Romanos, the king of the Rūm (the Byzantines) — Armānūs in the Arabic chronicles — set out from his lands with a great host, making for the lands of Islam.",
  "tr": "Dört yüz altmış üç yılı gelince Rum (Bizans) kralı Romen Diyojen — Arapça kroniklerde Ermânûs — büyük bir orduyla ülkesinden çıktı; İslâm diyarına yöneliyordu."},
 "tokens": [LAMMA2("فَلَمَّا"), KANAT_TAMMA(), FAIL("سَنَةُ", "sana", **W(MUDAF)),
  MUDAF_ILAYH("ثَلَاثٍ", "thalath", extra=["asma-al-adad-fil-kafiya"], note_ar=" — وَجَاءَ بِغَيْرِ تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ", note_en=" — written without ta because the counted noun «year» is feminine", note_tr=" — sayılan «sene» müennes olduğu için tâsız gelmiştir"),
  ATF("وَسِتِّينَ", "sittun", "noun", "jarr", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  ARBAUMIA(punct="،"),
  MADI("خَرَجَ", "kharaja", **W(FAIL_BAAD, JAWAB_LAMMA)), ARMANUS("fail"),
  tok("مَلِكُ", "malik-king", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "idafa-definiteness"],
      "بَدَلٌ مِنْ «أَرْمَانُوسُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A badal of «Romanos», in raf', annexed.", "«Ermânûs»tan bedel, merfû, muzâf."),
  MUDAF_ILAYH("الرُّومِ", "rum", "propn"), MIN(), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ: خَرَجَ فِي جَمْعٍ، أَيْ: مَصْحُوبًا بِهِ", "; the jarr phrase hangs on an omitted hal: «went out in a host», i.e. accompanied by it", " — câr-mecrûr mahzûf bir hâle müteallik: «bir ordu içinde», yani onunla birlikte")),
  MAJR("جَمْعٍ", "jam", note_ar=" — وَالْجَمْعُ هُنَا: الْجَيْشُ الْكَثِيرُ", note_en=" — «gathering» here is a great host", note_tr=" — cem' burada kalabalık ordu demektir"),
  NAAT("عَظِيمٍ", "azim", "jarr", punct="،"),
  MUDARI("يُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"], **W(HALCL)),
  MAFUL("بِلَادَ", "bilad", **W(MUDAF)), MUDAF_ILAYH("الْإِسْلَامِ", "islam", punct=".")]})
S1.append({"id": "s3", "translation": {
  "en": "He had gathered, from the Rūm and from others besides them, many hosts, until he thought that no one could stand against him.",
  "tr": "Rumlardan ve onlardan başkalarından pek çok kalabalık toplamıştı; öyle ki hiç kimsenin karşısında duramayacağını sanıyordu."},
 "tokens": [KANA_HID("وَكَانَ", note=("، يَعُودُ عَلَى أَرْمَانُوسَ", " (Romanos)", " (Ermânûs)")), QAD(),
  MADI("جَمَعَ", "jamaa-gather", hidden=True, **W(KH_KANA)),
  NOTE(MINA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «جُمُوعًا»: كَانَ نَعْتًا لَهُ، فَلَمَّا تَقَدَّمَ عَلَيْهِ صَارَ حَالًا",
       "; the jarr phrase hangs on an omitted hal of «hosts»: it would be the adjective of an indefinite noun, and fronted before it, it becomes a hal",
       "; câr-mecrûr «kalabalıklar»dan mahzûf bir hâle müteallik: nekrenin na'tı iken ondan önce gelince hâl olmuştur"),
  MAJR("الرُّومِ", "rum", "propn"),
  PREP("وَمِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفَانِ عَلَى «مِنَ الرُّومِ»", "; the jarr phrase is conjoined to «from the Rūm»", "; câr-mecrûr «Rumlardan»a ma'tûf", gloss_tr="«-den»"),
  ENC_NOUN("غَيْرِهِمْ", "ghayr", "هِمْ", "majr"),
  MAFUL("جُمُوعًا", "jam", extra=["jam-taksir"], note_ar=" — جَمْعُ جَمْعٍ", note_en=" — the plural of «host»", note_tr=" — cem'in cem'i"),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct="،"),
  HATTA_IBT(), MADI("ظَنَّ", "zanna", ["doubled-verbs"], hidden=True),
  ANNAHU(note=SADDA_ZANNA), LA_NAFIYA(),
  MUDARI_DF("يَقِفُ", "waqafa", ["mithal-verbs"], **W(KH_ANNA_CL)),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («onun karşısında»)", note_ar=" — مُتَعَلِّقَانِ بِيَقِفُ", note_en=" — it hangs on «stand»", note_tr=" — «durur»a müteallik"),
  FAIL("أَحَدٌ", "ahad", punct=".")]})
S1.append({"id": "s4", "translation": {
  "en": "And while the sultan was in one part of his lands, far from most of his troops, all at once the news reached him that the king of the Rūm had set out.",
  "tr": "Sultan ülkesinin bir yerinde, askerlerinin çoğundan uzakta iken, ansızın Rum kralının yola çıktığı haberi ona ulaştı."},
 "tokens": [BAYNAMA(), MUBTADA("السُّلْطَانُ", "sultan"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", "; the jarr phrase hangs on the omitted predicate of «the sultan»", " — câr-mecrûr mübtedânın mahzûf haberine müteallik")),
  MAJR("بَعْضِ", "bad", **W(MUDAF)), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "mudaf", punct="،"),
  HAL("بَعِيدًا", "baid", note_ar=" — وَصَاحِبُهُ الضَّمِيرُ الْمُسْتَتِرُ فِي الْخَبَرِ الْمَحْذُوفِ", note_en="; its owner is the pronoun hidden in the omitted predicate", note_tr="; sahibi mahzûf haberdeki gizli zamirdir"),
  PREP("عَنْ", "an", gloss_tr="«-den»"),
  MAJR("أَكْثَرِ", "akthar", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en=", annexed — an elative and a diptote, which takes kasra here because it is annexed", note_tr=", muzâf — gayr-i munsarif ism-i tafdîl; muzâf olduğu için kesre ile mecrûr"),
  ENC_NOUN("جُنْدِهِ", "jund", "هِ", "mudaf", punct="،"),
  IDH_FUJ(), ENC_MADI("جَاءَهُ", "jaa", "هُ", ["hollow-verbs"], **W(FAIL_BAAD)), FAIL("الْخَبَرُ", "khabar-news"),
  BI_NOUN("بِخُرُوجِ", "khuruj", "خُرُوجِ", extra=["masdar"], note_ar="، مُضَافٌ — مَصْدَرُ خَرَجَ", note_en="; it is annexed — the masdar of «to go out»", note_tr="; muzâf — harace'nin masdarı"),
  MUDAF_ILAYH("مَلِكِ", "malik-king", **W(MUDAF)), MUDAF_ILAYH("الرُّومِ", "rum", "propn", punct=".")]})
S1.append({"id": "s5", "translation": {
  "en": "Of his troops only a few were with him, for his armies were scattered across the lands — and the enemy had already drawn near.",
  "tr": "Yanında askerlerinden ancak az bir kısmı vardı; çünkü orduları memleketlere dağılmıştı, düşman ise yaklaşmıştı."},
 "tokens": [WA_LAM(), YAKUN(),
  MAA_X("مَعَهُ", "هُ", (" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ يَكُنْ مُقَدَّمٌ", "; the adverb is the FRONTED predicate of يَكُنْ", "; zarf yekün'ün öne alınmış haberidir")),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «قَلِيلٌ» تَقَدَّمَتْ عَلَيْهِ", "; the jarr phrase hangs on an omitted hal of «a few», fronted before it", " — câr-mecrûr «az»dan mahzûf, öne alınmış bir hâle müteallik")),
  ENC_NOUN("جُنْدِهِ", "jund", "هِ", "majr"), ILLA_HASR(),
  tok("قَلِيلٌ", "qalil", "noun", ["kana-wa-akhawatuha", "qasr"], "اسْمُ يَكُنْ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ الْمَقْصُورُ عَلَيْهِ.",
      "The noun of يَكُنْ, placed after its predicate, in raf' — it is what the statement is restricted TO.", "Yekün'ün haberinden sonraya bırakılmış ismi, merfû — hüküm ona hasredilmiştir.", punct="،"),
  FA_INNA(), ISM_ANNA_ENC("جُيُوشَهُ", "jaysh", "هُ", extra=["jam-taksir"], which="inna"),
  KANAT_HID_INNA(), KHK("مُتَفَرِّقَةً", "mutafarriq", extra=["ism-fail"]), FI(), MAJR("الْبِلَادِ", "bilad", punct="،"),
  WA_HAL_MUB("وَالْعَدُوُّ", "aduww"), QAD(),
  MADI("قَرُبَ", "qaruba", hidden=True, **W(KH_MUB_CL), punct=".")]})
S1.append({"id": "s6", "translation": {
  "en": "Then he marched with those who were with him toward the enemy, fearing for the lands of the Muslims, knowing all the while that his troops were fewer in number than the troops of the Rūm.",
  "tr": "Sonra Müslümanların toprakları için endişelendiğinden yanındakilerle düşmana doğru yürüdü; askerlerinin sayıca Rum askerlerinden az olduğunu da biliyordu."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True, **W(KH_INNA_CL)),
  BI_MAN((" لِلْمُصَاحَبَةِ", " of company («with»)", " (musâhabe: «ile»)")), MAA_X("مَعَهُ", "هُ", MAA_SILA),
  ZARF("نَحْوَ", "nahw"), MUDAF_ILAYH("الْعَدُوِّ", "aduww"),
  MAFUL_LAHU("خَوْفًا", "khawf"),
  NOTE(ALA(), " — مُتَعَلِّقٌ بِـ«خَوْفًا»", "; it hangs on «fearing»", "; «korku»ya müteallik"),
  MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUSLIMIN_MI(punct="،"),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"),
  MUDARI("يَعْلَمُ", "alima", **W(KH_MUB_CL)),
  ANNA_X((" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «يَعْلَمُ»", "; أَنَّ with its clause stands for a masdar that fills both objects of «knows»", "; enne ve sonrası, «bilir»in iki mef'ûlünün yerini tutan müevvel masdardır")),
  ISM_ANNA_ENC("جُنْدَهُ", "jund", "هُ"),
  tok("أَقَلُّ", "aqall", "noun", ["inna-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"],
      "خَبَرُ أَنَّ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ.",
      "The predicate of أَنَّ, in raf' with no tanwin — an elative, barred from tanwin (an adjective on the أَفْعَل pattern).",
      "Enne'nin haberi, tenvinsiz merfû — vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif ism-i tafdîl."),
  MIN(role=(" لِلْمُفَاضَلَةِ بَعْدَ اسْمِ التَّفْضِيلِ", " of comparison («than») after the elative", " — tafdîl isminden sonra gelen karşılaştırma min'i («-den daha»)")),
  MAJR("جُنْدِ", "jund", **W(MUDAF)), MUDAF_ILAYH("الرُّومِ", "rum", "propn"),
  TAMYIZ("عَدَدًا", "adad", punct=".")]})

# ---- Chapter 2 — الْهُدْنَةُ الْمَرْدُودَةُ ----
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "When the two hosts drew near to one another, the sultan sent Romanos an envoy asking him for a truce.",
  "tr": "İki ordu birbirine yaklaşınca sultan, Ermânûs'a ondan ateşkes isteyen bir elçi gönderdi."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("قَرُبَ", "qaruba", **W(FAIL_BAAD, LAMMA_CL)),
  tok("الْجَمْعَانِ", "jam", "noun", ["fail", "al-muthanna"], "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الِاسْمِ الْمُفْرَدِ.",
      "The doer, in raf' by the alif — a dual; its nun stands in for the tanwin of the singular.", "Fâil, tesniye olduğu için elif ile merfû; nûn, müfred ismin tenvini yerinedir."),
  tok("أَحَدُهُمَا", "ahad", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "idafa-definiteness", "al-bariz-al-muttasil"],
      "بَدَلُ بَعْضٍ مِنْ كُلٍّ مِنَ «الْجَمْعَانِ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ الرَّابِطُ.",
      "A badal of PART FROM WHOLE of «the two hosts», in raf' and annexed; the attached «the two» fills the seat of jarr and links the badal to its whole.",
      "«İki ordu»dan bedel-i ba'z min küll, merfû, muzâf; bitişik «o ikisi» zamiri mahallen mecrûr ve bedeli asla bağlar.",
      segments=[seg("أَحَدُ", "ahad", "noun"), seg("هُمَا", "pron-3d", "pron")]),
  MINA(), MAJR("الْآخَرِ", "akhar", note_ar=" — وَآخَرُ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ أَلْ عَلَيْهِ", note_en=" — آخَر is a diptote; it takes kasra here because it carries the article", note_tr=" — âhar gayr-i munsariftir; elif-lâm aldığı için kesre ile mecrûr", punct="،"),
  MADI("أَرْسَلَ", "arsala", ["form-iv-verbs"], **W(FAIL_BAAD, JAWAB_LAMMA)), FAIL("السُّلْطَانُ", "sultan"),
  ILA(), ARMANUS("majr"), MAFUL("رَسُولًا", "rasul-msg"),
  MUDARI("يَطْلُبُ", "talaba", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«رَسُولًا»", note_en="; the clause qualifies «an envoy», in the seat of nasb", note_tr="; cümle «elçi»nin na'tı, mahallen mansûb"),
  MINHU(), MAFUL("الْهُدْنَةَ", "hudna", punct=".")]})
S2.append({"id": "s2", "translation": {
  "en": "But Romanos would have nothing but war, and he answered the envoy with an ugly answer.",
  "tr": "Fakat Ermânûs savaştan başka bir şeye razı olmadı ve elçiye çirkin bir cevap verdi."},
 "tokens": [MADI_ALIF("فَأَبَى", "aba", note_ar=FAIL_BAAD[0] + " — وَأَبَى فِي مَعْنَى النَّفْيِ (لَمْ يُرِدْ)، فَجَازَ أَنْ يَقَعَ بَعْدَهُ الِاسْتِثْنَاءُ الْمُفَرَّغُ",
      note_en=FAIL_BAAD[1] + " — «refused» carries the meaning of a negation («did not want»), so an emptied exception may follow it",
      note_tr=FAIL_BAAD[2] + " — ebâ olumsuzluk anlamı taşır («istemedi»), bu yüzden ardından müferrağ istisnâ gelebilir"),
  ARMANUS("fail"), ILLA_HASR(),
  MAFUL("الْحَرْبَ", "harb", note_ar=" — وَهُوَ الْمَقْصُورُ عَلَيْهِ", note_en=" — it is what his will is restricted TO", note_tr=" — iradesi ona hasredilmiştir", punct="،"),
  MADI("وَرَدَّ", "radda", ["doubled-verbs"], hidden=True), ALA(), MAJR("الرَّسُولِ", "rasul-msg"),
  MUTLAQ_X("رَدًّا", "radd", "رَدَّ", "to answer back", "reddetti"),
  NAAT("قَبِيحًا", "qabih", "nasb", punct=".")]})
S2.append({"id": "s3", "translation": {
  "en": "It was only the size of his army that drove him to it, for he thought that victory was his.",
  "tr": "Onu buna sevk eden ancak ordusunun kalabalığıydı; çünkü zaferin kendisinin olduğunu sanıyordu."},
 "tokens": [WA_INNAMA(), ENC_MADI("حَمَلَهُ", "hamala", "هُ", note_ar=" — وَالْفَاعِلُ «كَثْرَةُ» بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «the size» comes after the jarr phrase", note_tr="; fâili «kalabalık» câr-mecrûrdan sonra gelir"),
  ALA(), DHALIKA("جَرٍّ بِعَلَى", "jarr after عَلَى", "mecrûr (alâ ile)"),
  FAIL("كَثْرَةُ", "kathra", note_ar=MUDAF[0] + " — وَهُوَ الْمَقْصُورُ عَلَيْهِ، أُخِّرَ لِأَنَّ الْمَحْصُورَ فِيهِ بِإِنَّمَا يَقَعُ آخِرًا", note_en=MUDAF[1] + " — it is what the statement is restricted TO, placed last as إِنَّمَا requires", note_tr=MUDAF[2] + " — hüküm ona hasredilmiştir; innemâ'da hasredilen sona geldiği için sona bırakıldı"),
  ENC_NOUN("جُنْدِهِ", "jund", "هِ", "mudaf", punct="،"),
  FA_QAD(), MADI("ظَنَّ", "zanna", ["doubled-verbs"], hidden=True), ANNA_X(SADDA_ZANNA),
  tok("النَّصْرَ", "nasr", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, in nasb.", "Enne'nin ismi, mansûb."),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («onun»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ أَنَّ", note_en="; the jarr phrase hangs on the omitted predicate of أَنَّ", note_tr="; câr-mecrûr enne'nin mahzûf haberine müteallik", punct=".")]})
S2.append({"id": "s4", "translation": {
  "en": "When the envoy came back with that, the sultan resolved to meet him; and the fewness of those with him only added to his resolve.",
  "tr": "Elçi bu cevapla dönünce sultan onunla karşılaşmaya karar verdi; yanındakilerin azlığı onun azmini artırmaktan başka bir şey yapmadı."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("رَجَعَ", "rajaa", **W(FAIL_BAAD, LAMMA_CL)), FAIL("الرَّسُولُ", "rasul-msg"),
  tok("بِذٰلِكَ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
      "الْبَاءُ حَرْفُ جَرٍّ لِلْمُصَاحَبَةِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.",
      "The ba of company («with that»); the demonstrative after it is built on sukun, in the seat of jarr.",
      "Musâhabe bâ'sı («bununla»); işaret ismi sükûn üzere mebnî, mahallen mecrûr.", punct="،",
      segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  MADI("عَزَمَ", "azama", **W(FAIL_BAAD, JAWAB_LAMMA)), FAIL("السُّلْطَانُ", "sultan"), ALA(),
  ENC_NOUN("لِقَائِهِ", "liqa", "هِ", "majr", extra=["masdar"], note_ar=" — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ", note_en=" — a masdar annexed to its object («meeting HIM»)", note_tr=" — mef'ûlüne muzâf masdar", punct="،"),
  WA_MA("atf"), ENC_MADI("زَادَتْهُ", "zada", "هُ", ["hollow-verbs"], fem=True, note_ar=" — وَهِيَ مَفْعُولُهُ الْأَوَّلُ، وَالْفَاعِلُ بَعْدَهُ", note_en=" — its first object; its doer follows", note_tr=" — birinci mef'ûlü; fâili ondan sonra gelir"),
  FAIL("قِلَّةُ", "qilla", **W(MUDAF)),
  MAN_X("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"],
        sila=("وَالظَّرْفُ بَعْدَهُ صِلَتُهُ", "the adverb after it is its ṣila", "sonraki zarf sılasıdır")),
  MAA_X("مَعَهُ", "هُ", MAA_SILA), ILLA_HASR(),
  tok("عَزْمًا", "azm-resolve", "noun", ["maful-bihi", "istithna-mufarragh", "qasr"],
      "مَفْعُولٌ بِهِ ثَانٍ لِـ«زَادَ» مَنْصُوبٌ بِالْفَتْحَةِ — وَالِاسْتِثْنَاءُ مُفَرَّغٌ، وَهُوَ الْمَقْصُورُ عَلَيْهِ؛ وَقِيلَ: تَمْيِيزٌ.",
      "The second object of «added», in nasb — the exception is emptied and this is what the statement is restricted TO (some read it as a tamyiz).",
      "«Artırdı»nın ikinci mef'ûlü, mansûb — istisnâ müferrağdır, hüküm ona hasredilmiştir (bir görüşe göre temyîzdir).", punct=".")]})
S2.append({"id": "s5", "translation": {
  "en": "Ibn al-Athīr reports that Alp Arslan chose to meet them on Friday, at the hour when the preacher on every minbar prays for the Muslims' victory.",
  "tr": "İbnü'l-Esîr'in naklettiğine göre Alparslan onlarla cuma günü, her minberde hatibin Müslümanların zaferi için dua ettiği saatte karşılaşmayı seçti."},
 "tokens": [MADI("وَذَكَرَ", "dhakara", **W(FAIL_BAAD)),
  PH(FAIL("ابْنُ", "ibn", note_ar=MUDAF[0] + " — «ابْنُ الْأَثِيرِ» عَلَمٌ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ", note_en=MUDAF[1] + " — «Ibn al-Athīr» is a name built as an idafa", note_tr=MUDAF[2] + " — «İbnü'l-Esîr» izâfet terkibiyle kurulmuş bir isimdir"), "ibn-al-athir"),
  MUDAF_ILAYH("الْأَثِيرِ", "athir"),
  ANNA_X((" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«ذَكَرَ»", "; أَنَّ with its clause stands for a masdar, the object of «reports», in the seat of nasb", "; enne ve sonrası «zikretti»nin mef'ûlü olan müevvel masdar, mahallen mansûb")),
  *ALB_ARSLAN("ism_anna"),
  MADI("اخْتَارَ", "ikhtara", ["form-viii-verbs", "hollow-verbs"], hidden=True, **W(KH_ANNA_CL)),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«اخْتَارَ»", "; the clause it builds is the object of «chose», in the seat of nasb", "; kurduğu müevvel masdar «seçti»nin mef'ûlü, mahallen mansûb"),
  YALQAHUM(),
  ZARF("يَوْمَ", "yawm", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«يَلْقَى»", note_en="; it hangs on «meet»", note_tr="; «karşılaşır»a müteallik"),
  MUDAF_ILAYH("الْجُمُعَةِ", "jumua", punct="،"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَلْقَى» أَيْضًا", "; the jarr phrase also hangs on «meet»", " — câr-mecrûr da «karşılaşır»a müteallik")),
  MAJR("السَّاعَةِ", "saa-hour"),
  tok("الَّتِي", "allati", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«السَّاعَةِ»، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
      "A relative pronoun built on sukun, in the seat of jarr as the adjective of «the hour»; the clause after it is its ṣila.", "İsm-i mevsûl, sükûn üzere mebnî, «saat»in na'tı olarak mahallen mecrûr; sonraki cümle sılasıdır."),
  YADU(),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", note_ar=" — وَهُوَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en=" — it is the one that returns to the relative", note_tr=" — mevsûle dönen râbıt budur"),
  FAIL("الْخَطِيبُ", "khatib-preacher"),
  NOTE(ALA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «الْخَطِيبُ»", "; the jarr phrase hangs on an omitted hal of «the preacher»", "; câr-mecrûr «hatip»ten mahzûf bir hâle müteallik"),
  MAJR("كُلِّ", "kull", **W(MUDAF)), MUDAF_ILAYH("مِنْبَرٍ", "minbar"),
  LI_MUSLIMIN((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَدْعُو»", "; the jarr phrase hangs on «prays»", "; câr-mecrûr «dua eder»e müteallik")),
  BI_NOUN("بِالنَّصْرِ", "nasr", "النَّصْرِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَدْعُو»", note_en="; it hangs on «prays»", note_tr="; «dua eder»e müteallik", punct=".")]})
S2.append({"id": "s6", "translation": {
  "en": "He chose that hour only in the hope that God would give him victory through the blessing of that prayer.",
  "tr": "O saati ancak Allah'ın o duanın bereketiyle kendisine zafer vermesini umarak seçmişti."},
 "tokens": [WA_INNAMA(), MADI("اخْتَارَ", "ikhtara", ["form-viii-verbs", "hollow-verbs"], hidden=True),
  TILKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih"), BADAL("السَّاعَةَ", "saa-hour", "nasb"),
  MAFUL_LAHU("رَجَاءَ", "raja-hope", mudaf=True, note_ar="، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ مُضَافٌ إِلَيْهِ — وَهُوَ الْمَقْصُورُ عَلَيْهِ", note_en="; the clause after it is its second term — and it is what the statement is restricted TO", note_tr="; sonraki müevvel masdar muzâfun ileyhtir — hüküm ona hasredilmiştir"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause it builds is annexed to «hope», in the seat of jarr", "; kurduğu müevvel masdar «ümit»e muzâfun ileyh, mahallen mecrûr"),
  MANSUB_AN("يَنْصُرَهُ", "nasara", enc="هُ", hidden=False), ALLAH_F(),
  BI_NOUN("بِبَرَكَةِ", "baraka-blessing", "بَرَكَةِ", note_ar="، مُضَافٌ — وَالْبَاءُ لِلسَّبَبِيَّةِ", note_en="; it is annexed — the ba of cause («through»)", note_tr="; muzâf — bâ sebebiyye içindir"),
  DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh"),
  BADAL("الدُّعَاءِ", "dua", "jarr", punct=".")]})

# ---- Chapter 3 — سَاعَةُ الْجُمُعَةِ ----
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "When that hour came, he led those who were with him in prayer; he wept, and the people wept at his weeping; then he called upon God, the people calling upon Him with him.",
  "tr": "O saat gelince yanındakilere namaz kıldırdı; ağladı, onun ağlamasıyla insanlar da ağladı; sonra Allah'a dua etti, insanlar da onunla birlikte dua ediyordu."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("جَاءَتْ", "jaa", ["hollow-verbs"], fem=True, **W(FAIL_BAAD, LAMMA_CL)),
  TILKA("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil"), BADAL("السَّاعَةُ", "saa-hour", "raf"),
  MADI_ALIF("صَلَّى", "salla", ["form-ii-verbs"], hidden=True, note_ar=" — صَلَّى بِهِمْ: أَمَّهُمْ فِي الصَّلَاةِ" + JAWAB_LAMMA[0], note_en=" — «prayed with them»: led them in prayer" + JAWAB_LAMMA[1], note_tr=" — onlara namaz kıldırdı, imamlık etti" + JAWAB_LAMMA[2]),
  BI_MAN(), MAA_X("مَعَهُ", "هُ", MAA_SILA, punct="،"),
  MADI_ALIF("وَبَكَى", "baka", hidden=True), MADI_ALIF("فَبَكَى", "baka", **W(FAIL_BAAD)), FAIL("النَّاسُ", "nas"),
  LI_ENC("لِبُكَائِهِ", "buka", "بُكَائِ", "هِ", extra=["masdar"], note_ar=" — وَاللَّامُ لِلتَّعْلِيلِ", note_en=" — the lam of cause («at, because of»)", note_tr=" — lâm ta'lîl içindir", punct="،"),
  THUMMA(), MADI_ALIF("دَعَا", "daa", hidden=True), ALLAH_MAF(),
  WA_HAL_MUB("وَالنَّاسُ", "nas"),
  MUDARI5("يَدْعُونَ", "daa", ["naqis-verbs"], role_ar=" — وَأَصْلُهُ يَدْعُوُونَ: اسْتُثْقِلَتِ الضَّمَّةُ عَلَى الْوَاوِ فَحُذِفَتْ، ثُمَّ حُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ" + KH_MUB_CL[0],
          role_en=" — from يَدْعُوُونَ: the damma was too heavy on the waw and dropped, then that waw fell where two quiescents met" + KH_MUB_CL[1],
          role_tr=" — aslı yedʿuvûne: vâv üzerindeki damme ağır geldiği için düştü, sonra iki sâkin karşılaşınca o vâv da düştü" + KH_MUB_CL[2]),
  MAA_X("مَعَهُ", "هُ", (" — مُتَعَلِّقٌ بِـ«يَدْعُونَ»", "; it hangs on «calling»", "; «dua ederler»e müteallik"), punct=".")]})
S3.append({"id": "s2", "translation": {
  "en": "Then he advanced with them against the Rūm, and the Rūm advanced against him, and they fought one another fiercely.",
  "tr": "Sonra onlarla Rumların üzerine yürüdü, Rumlar da onun üzerine yürüdü ve şiddetle çarpıştılar."},
 "tokens": [THUMMA(), MADI("زَحَفَ", "zahafa", hidden=True),
  JARR_PRON("بِهِمْ", "bi", "بِ", "هِمْ", " («onlarla»)", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of company («with them»)", note_tr=" — bâ musâhabe içindir"),
  ILA(), MAJR("الرُّومِ", "rum", "propn", punct="،"),
  MADI("وَزَحَفَ", "zahafa", **W(FAIL_BAAD)), FAIL("الرُّومُ", "rum", "propn"), ILAYHI(punct="،"),
  VERB_WAW("فَاقْتَتَلُوا", "iqtatala", ["form-viii-verbs"]), QITAL_NAIB(), NAAT("شَدِيدًا", "shadid", "nasb", punct=".")]})
S3.append({"id": "s3", "translation": {
  "en": "The Muslims held firm despite their fewness, until God gave them a great victory and routed the Rūm, and those of them who were left fled.",
  "tr": "Müslümanlar azlıklarına rağmen sebat ettiler; nihayet Allah onlara büyük bir zafer verdi ve Rumları bozguna uğrattı; onlardan geriye kalanlar kaçtı."},
 "tokens": [MADI("وَصَبَرَ", "sabara", **W(FAIL_BAAD)), MUSLIMUN_F(),
  NOTE(ALA(), " — وَعَلَى هُنَا بِمَعْنَى «مَعَ»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ", "; عَلَى here means «with, despite», and the jarr phrase hangs on an omitted hal", "; alâ burada «-e rağmen, ile» anlamındadır; câr-mecrûr mahzûf bir hâle müteallik"),
  ENC_NOUN("قِلَّتِهِمْ", "qilla", "هِمْ", "majr", punct="،"),
  HATTA_IBT(),
  ENC_MADI("نَصَرَهُمُ", "nasara", "هُمُ", note_ar=" — وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ" + FAIL_BAAD[0], note_en="; the mim takes damma before the following ال" + FAIL_BAAD[1], note_tr="; iki sâkin karşılaştığı için mîm damme aldı" + FAIL_BAAD[2]),
  ALLAH_F(), MUTLAQ_X("نَصْرًا", "nasr", "نَصَرَ", "to give victory", "nasara"), NAAT("عَظِيمًا", "azim", "nasb", punct="،"),
  MADI("وَهَزَمَ", "hazama", hidden=True, note_ar=" — يَعُودُ عَلَى لَفْظِ الْجَلَالَةِ", note_en=" («He» — God)", note_tr=" («O» — Allah)"),
  MAFUL("الرُّومَ", "rum", "propn", punct="،"),
  MADI("فَفَرَّ", "farra", ["doubled-verbs"], **W(FAIL_BAAD)),
  MAN_X("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail"]),
  MADI("بَقِيَ", "baqiya", ["naqis-verbs"], hidden=True, note_ar=" — يَعُودُ عَلَى مَنْ" + SILA_[0], note_en=" — returning to «those who»" + SILA_[1], note_tr=" — men'e döner" + SILA_[2]),
  MINHUM(punct=".")]})
S3.append({"id": "s4", "translation": {
  "en": "How many a man of them was slain that day, and how many a man was taken captive!",
  "tr": "O gün onlardan nice adam öldürüldü, nice adam da esir alındı!"},
 "tokens": [KAM("وَكَمْ"), KAM_TAMYIZ("رَجُلٍ", "rajul"),
  NOTE(MINHUM(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«رَجُلٍ»", "; the jarr phrase qualifies «man»", "; câr-mecrûr «adam»ın na'tına müteallik"),
  MAJHUL("قُتِلَ", "qatala", note_ar=NAIB_HID[0] + "، يَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=NAIB_HID[1] + ", returning to كَمْ" + KH_KAM[1], note_tr=NAIB_HID[2] + ", kem'e döner" + KH_KAM[2]),
  YAWMAIDHIN((" — مُتَعَلِّقٌ بِـ«قُتِلَ»", "; it hangs on «was slain»", " — «öldürüldü»ye müteallik"), punct="،"),
  KAM("وَكَمْ", pre="atf"), KAM_TAMYIZ("رَجُلٍ", "rajul"),
  MAJHUL("أُسِرَ", "asara-capture", note_ar=NAIB_HID[0] + "، يَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=NAIB_HID[1] + ", returning to كَمْ" + KH_KAM[1], note_tr=NAIB_HID[2] + ", kem'e döner" + KH_KAM[2], punct="!")]})
S3.append({"id": "s5", "translation": {
  "en": "The Rūm left behind them the wealth and the arms they had with them, and the Muslims took it.",
  "tr": "Rumlar yanlarındaki malı ve silahı geride bıraktılar; Müslümanlar da onu aldı."},
 "tokens": [MADI("وَتَرَكَ", "taraka", **W(FAIL_BAAD)), FAIL("الرُّومُ", "rum", "propn"),
  ZARF_ENC("وَرَاءَهُمْ", "wara", "هُمْ"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
      "A relative pronoun «what», built on sukun, the object in the seat of nasb; the clause after it is its ṣila.", "İsm-i mevsûl «…-an şey», sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb; sonraki cümle sılasıdır."),
  KANA_HID("كَانَ", note=("، يَعُودُ عَلَى «مَا»" + SILA_[0], " (it returns to «what»)" + SILA_[1], " (mâ'ya döner)" + SILA_[2])),
  MAA_X("مَعَهُمْ", "هُمْ", (" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ كَانَ", "; the adverb is the predicate of كَانَ", "; zarf kâne'nin haberidir")),
  NOTE(MINA(), " — وَهِيَ بَيَانِيَّةٌ تُبَيِّنُ «مَا»", "; this مِنْ explains «what»", "; beyâniyye min — «şey»i açıklar"),
  MAJR("الْمَالِ", "mal"), ATF("وَالسِّلَاحِ", "silah", "noun", "jarr", punct="،"),
  ENC_MADI("فَأَخَذَهُ", "akhadha", "هُ", **W(FAIL_BAAD)), MUSLIMUN_F(punct=".")]})
S3.append({"id": "s6", "translation": {
  "en": "That victory did not come by great numbers; it came only by endurance and resolve.",
  "tr": "O zafer sayı çokluğuyla olmadı; ancak sabır ve azimle oldu."},
 "tokens": [WA_LAM(), YAKUN(), DHALIKA("رَفْعٍ اسْمُ يَكُنْ", "raf' as the noun of يَكُنْ", "merfû — yekün'ün ismi"),
  BADAL("النَّصْرُ", "nasr", "raf"),
  BI_NOUN("بِكَثْرَةِ", "kathra", "كَثْرَةِ", note_ar="، مُضَافٌ — وَالْبَاءُ لِلسَّبَبِيَّةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ يَكُنْ", note_en="; it is annexed — the ba of cause; the jarr phrase hangs on the omitted predicate of يَكُنْ", note_tr="; muzâf — bâ sebebiyye; câr-mecrûr yekün'ün mahzûf haberine müteallik"),
  MUDAF_ILAYH("الْعَدَدِ", "adad", punct="،"),
  WA_INNAMA(pre="atf"), KANA_HID("كَانَ", note=("، يَعُودُ عَلَى النَّصْرِ", " (the victory)", " (zafer)")),
  BI_NOUN("بِالصَّبْرِ", "sabr", "الصَّبْرِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ، وَهُمَا الْمَقْصُورُ عَلَيْهِ", note_en="; the jarr phrase hangs on the omitted predicate of كَانَ — it is what the statement is restricted TO", note_tr="; câr-mecrûr kâne'nin mahzûf haberine müteallik — hüküm ona hasredilmiştir"),
  ATF("وَالْعَزْمِ", "azm-resolve", "noun", "jarr", punct=".")]})

# ---- Chapter 4 — الْمَلِكُ الْأَسِيرُ ----
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "Among those taken captive was Romanos himself, and he was carried to Alp Arslan.",
  "tr": "Esir alınanlar arasında bizzat Ermânûs da vardı; Alparslan'ın huzuruna götürüldü."},
 "tokens": [KANA("وَكَانَ"), FIMAN(),
  MAJHUL("أُسِرَ", "asara-capture", note_ar=NAIB_HID[0] + "، يَعُودُ عَلَى مَنْ" + SILA_[0], note_en=NAIB_HID[1] + ", returning to «those who»" + SILA_[1], note_tr=NAIB_HID[2] + ", men'e döner" + SILA_[2]),
  ARMANUS("ismk"),
  tok("نَفْسُهُ", "nafs", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A tawkid of meaning «himself», in raf' like the noun it strengthens; annexed to the pronoun, which fills the seat of jarr.",
      "Ma'nevî te'kîd «bizzat kendisi», pekiştirdiği isim gibi merfû; zamire muzâf, zamir mahallen mecrûr.", punct="،",
      segments=[seg("نَفْسُ", "nafs", "noun"), seg("هُ", "pron-3ms", "pron")]),
  MAJHUL("فَحُمِلَ", "hamala", **W(NAIB_HID)), ILA(), *ALB_ARSLAN("majr", punct=".")]})
S4.append({"id": "s2", "translation": {
  "en": "He had set out from his lands thinking himself the victor — and lo, he was a captive in the hands of his enemy.",
  "tr": "Ülkesinden galip geleceğini sanarak çıkmıştı; bir de baktı ki düşmanının elinde esirdi."},
 "tokens": [KANA_HID("وَكَانَ"), QAD(), MADI("خَرَجَ", "kharaja", hidden=True, **W(KH_KANA)),
  MIN(), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr"),
  MUDARI("يَظُنُّ", "zanna", ["doubled-verbs"], **W(HALCL)),
  ANNAHU(note=(" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «يَظُنُّ»", "; أَنَّ with its clause stands for a masdar that fills both objects of «thinking»", "; enne ve sonrası, «sanır»ın iki mef'ûlünün yerini tutan müevvel masdardır")),
  KH_ANNA("غَالِبٌ", "ghalib", ["ism-fail"], punct="،"),
  FA_IDHA(), PRON_MUB("هُوَ", "huwa"), KHABAR("أَسِيرٌ", "asir"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«أَسِيرٌ»", "; the jarr phrase qualifies «a captive»", " — câr-mecrûr «esir»in mahzûf na'tına müteallik")),
  MAJR("يَدِ", "yad", **W(MUDAF)), ENC_NOUN("عَدُوِّهِ", "aduww", "هِ", "mudaf", punct=".")]})
S4.append({"id": "s3", "translation": {
  "en": "When he was brought in before him, the sultan spoke with him, then treated him kindly and honoured him greatly.",
  "tr": "Huzuruna getirilince sultan onunla konuştu, sonra ona iyilik etti ve onu büyük bir ikramla ağırladı."},
 "tokens": [LAMMA2("فَلَمَّا"), MAJHUL("أُدْخِلَ", "adkhala", ["form-iv-verbs"], **W(NAIB_HID, LAMMA_CL)), ALAYHI(),
  ENC_MADI("كَلَّمَهُ", "kallama", "هُ", ["form-ii-verbs"], **W(FAIL_BAAD, JAWAB_LAMMA)), FAIL("السُّلْطَانُ", "sultan", punct="،"),
  THUMMA(), MADI("أَحْسَنَ", "ahsana", ["form-iv-verbs"], hidden=True), ILAYHI(punct="،"),
  ENC_MADI("وَأَكْرَمَهُ", "akrama", "هُ", ["form-iv-verbs"], hidden=True),
  MUTLAQ_X("إِكْرَامًا", "ikram", "أَكْرَمَ", "to honour", "ekrama"), NAAT("عَظِيمًا", "azim", "nasb", punct=".")]})
S4.append({"id": "s4", "translation": {
  "en": "By my life, nothing moved him to that but the nobility of his own soul.",
  "tr": "Ömrüme andolsun ki onu buna sevk eden, nefsinin kereminden başka bir şey değildi."},
 "tokens": [LAAMRI(),
  NOTE(MA_NAFIYA(), " — وَالْجُمْلَةُ بَعْدَهَا جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا", "; the clause it opens is the answer of the oath and has no seat", "; açtığı cümle kasemin cevabıdır, mahalli yoktur"),
  ENC_MADI("حَمَلَهُ", "hamala", "هُ", **W(FAIL_BAAD)), ALA(), DHALIKA("جَرٍّ بِعَلَى", "jarr after عَلَى", "mecrûr (alâ ile)"),
  ILLA_HASR(),
  FAIL("كَرَمُ", "karam", note_ar=MUDAF[0] + " — وَهُوَ الْمَقْصُورُ عَلَيْهِ", note_en=MUDAF[1] + " — it is what the statement is restricted TO", note_tr=MUDAF[2] + " — hüküm ona hasredilmiştir"),
  ENC_NOUN("نَفْسِهِ", "nafs", "هِ", "mudaf", punct=".")]})
S4.append({"id": "s5", "translation": {
  "en": "For pardoning an enemy after gaining power over him is among the ways of noble kings.",
  "tr": "Çünkü güç yetirdikten sonra düşmanı affetmek, kerîm hükümdarların ahlâkındandır."},
 "tokens": [FA_INNA(), ISM_INNA("الْعَفْوَ", "afw", ["masdar"]),
  NOTE(AN_KASRA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْعَفْوَ»", "; the jarr phrase hangs on «pardoning»", "; câr-mecrûr «af»fa müteallik"),
  MAJR("الْعَدُوِّ", "aduww"),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«الْعَفْوَ»", note_en="; it hangs on «pardoning»", note_tr="; «af»fa müteallik"),
  MUDAF_ILAYH("الْقُدْرَةِ", "qudra"),
  NOTE(ALAYHI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْقُدْرَةِ»", "; the jarr phrase hangs on «power»", "; câr-mecrûr «kudret»e müteallik"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ إِنَّ", "; the jarr phrase hangs on the omitted predicate of إِنَّ", " — câr-mecrûr inne'nin mahzûf haberine müteallik")),
  MAJR("أَخْلَاقِ", "khuluq", extra=["jam-taksir"], note_ar="، مُضَافٌ — جَمْعُ خُلُقٍ", note_en=", annexed — the plural of «character»", note_tr=", muzâf — hulk'un cem'i"),
  MUDAF_ILAYH("الْمُلُوكِ", "malik-king", extra=["jam-taksir"], note_ar=" — جَمْعُ مَلِكٍ", note_en=" — the plural of «king»", note_tr=" — melik'in cem'i"),
  NAAT("الْكِرَامِ", "karim", "jarr", extra=["jam-taksir"], note_ar=" — جَمْعُ كَرِيمٍ", note_en=" — the plural of «noble»", note_tr=" — kerîm'in cem'i", punct=".")]})
S4.append({"id": "s6", "translation": {
  "en": "And how many a king has had his enemy in his power and not pardoned him!",
  "tr": "Nice hükümdar düşmanına güç yetirdi de onu affetmedi!"},
 "tokens": [KAM("وَكَمْ"), KAM_TAMYIZ("مَلِكٍ", "malik-king"),
  MADI("قَدَرَ", "qadara-able", hidden=True, note_ar=" — يَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=" — returning to كَمْ" + KH_KAM[1], note_tr=" — kem'e döner" + KH_KAM[2]),
  ALA(), ENC_NOUN("عَدُوِّهِ", "aduww", "هِ", "majr"),
  LAM_JAZM("فَلَمْ"), YAFU(), JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)", punct="!")]})

# ---- Chapter 5 — بَابٌ إِلَى بِلَادِ الرُّومِ ----
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Then the sultan made terms with him: a ransom he would pay, and that he would set free every Muslim captive in his lands.",
  "tr": "Sonra sultan onunla, ödeyeceği bir fidye ve ülkesindeki her Müslüman esiri serbest bırakması şartıyla anlaştı."},
 "tokens": [THUMMA(), INNA(), ISM_INNA("السُّلْطَانَ", "sultan"),
  ENC_MADI("صَالَحَهُ", "salaha", "هُ", ["form-iii-verbs"], hidden=True, **W(KH_INNA_CL)),
  ALA(), MAJR("فِدَاءٍ", "fida"),
  MUDARI("يُؤَدِّيهِ", "adda", ["form-ii-verbs"], enc="هِ", naqis="ي", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«فِدَاءٍ»", note_en="; the clause qualifies «a ransom», in the seat of jarr", note_tr="; cümle «fidye»nin na'tı, mahallen mecrûr", punct="،"),
  PREP("وَعَلَى", "ala", " — وَالْجَارُّ وَمَجْرُورُهُ مَعْطُوفَانِ عَلَى «عَلَى فِدَاءٍ»", "; the jarr phrase is conjoined to «on a ransom»", "; câr-mecrûr «bir fidye üzerine»ye ma'tûf", gloss_tr="«üzerine»"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِعَلَى", "; the clause it builds is in the seat of jarr after عَلَى", "; kurduğu müevvel masdar alâ ile mahallen mecrûr"),
  MANSUB_AN("يُطْلِقَ", "atlaqa", ["form-iv-verbs"]),
  MAFUL("كُلَّ", "kull", **W(MUDAF)), MUDAF_ILAYH("أَسِيرٍ", "asir"),
  NOTE(MINA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«أَسِيرٍ»", "; the jarr phrase qualifies «captive»", "; câr-mecrûr «esir»in mahzûf na'tına müteallik"),
  MUSLIMIN_J(),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«أَسِيرٍ»", "; the jarr phrase is a second qualifier of «captive»", " — câr-mecrûr «esir»in ikinci na'tına müteallik")),
  ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr", punct=".")]})
S5.append({"id": "s2", "translation": {
  "en": "When the peace between them was complete, Alp Arslan set him free, and sent with him an escort that brought him safely to his own lands.",
  "tr": "Aralarındaki sulh tamamlanınca Alparslan onu serbest bıraktı ve yanına, onu ülkesine güven içinde ulaştıracak kimseler kattı."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("تَمَّ", "tamma", ["doubled-verbs"], **W(FAIL_BAAD, LAMMA_CL)), FAIL("الصُّلْحُ", "sulh"),
  ZARF_ENC("بَيْنَهُمَا", "bayna", "هُمَا", punct="،", note_ar=" — مُتَعَلِّقٌ بِـ«تَمَّ»", note_en="; it hangs on «was complete»", note_tr="; «tamamlandı»ya müteallik"),
  ENC_MADI("أَطْلَقَهُ", "atlaqa", "هُ", ["form-iv-verbs"], **W(FAIL_BAAD, JAWAB_LAMMA)), *ALB_ARSLAN("fail", punct="،"),
  MADI("وَبَعَثَ", "baatha", hidden=True),
  MAA_X("مَعَهُ", "هُ", (" — مُتَعَلِّقٌ بِـ«بَعَثَ»", "; it hangs on «sent»", "; «gönderdi»ye müteallik")),
  MAN_X("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"]),
  ENC_MADI("أَوْصَلَهُ", "awsala", "هُ", ["form-iv-verbs", "mithal-verbs"], hidden=True, note_ar=" — وَالْفَاعِلُ الْمُسْتَتِرُ يَعُودُ عَلَى «مَنْ»، وَالْهَاءُ لِأَرْمَانُوسَ" + SILA_[0], note_en=" — the hidden doer returns to «those who», and «him» is Romanos" + SILA_[1], note_tr=" — gizli fâil men'e, «onu» zamiri Ermânûs'a döner" + SILA_[2]),
  ILA(), ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr"),
  HAL("آمِنًا", "amin-safe", ["ism-fail"], note_ar=" — وَصَاحِبُهُ الْهَاءُ فِي «أَوْصَلَهُ»", note_en="; its owner is «him» in «brought him»", note_tr="; sahibi «ulaştırdı»daki «onu» zamiridir", punct=".")]})
S5.append({"id": "s3", "translation": {
  "en": "And many a man of his companions the sultan set free for his sake!",
  "tr": "Onun hatırı için arkadaşlarından nice adamı da serbest bıraktı!"},
 "tokens": [KAM("وَكَمْ"), KAM_TAMYIZ("رَجُلٍ", "rajul"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«رَجُلٍ»", "; the jarr phrase qualifies «man»", " — câr-mecrûr «adam»ın mahzûf na'tına müteallik")),
  ENC_NOUN("أَصْحَابِهِ", "sahib", "هِ", "majr", extra=["jam-taksir"], note_ar=" — جَمْعُ صَاحِبٍ", note_en=" — the plural of «companion»", note_tr=" — sâhib'in cem'i"),
  ENC_MADI("أَطْلَقَهُ", "atlaqa", "هُ", ["form-iv-verbs"], hidden=True, note_ar=" — وَالْهَاءُ تَعُودُ عَلَى كَمْ" + KH_KAM[0], note_en=" — the attached pronoun returns to كَمْ" + KH_KAM[1], note_tr=" — bitişik zamir kem'e döner" + KH_KAM[2]),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («onun için»)", note_ar=" — وَاللَّامُ لِلتَّعْلِيلِ: مِنْ أَجْلِهِ", note_en=" — the lam of cause: «for his sake»", note_tr=" — lâm ta'lîl içindir: «onun hatırı için»", punct="!")]})
S5.append({"id": "s4", "translation": {
  "en": "That victory was a door opened for the Muslims into the lands of the Rūm — Anatolia.",
  "tr": "O zafer, Müslümanlara Rum diyarına — Anadolu'ya — açılan bir kapı oldu."},
 "tokens": [KANA("وَكَانَ"), DHALIKA("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi"), BADAL("النَّصْرُ", "nasr", "raf"),
  KHK("بَابًا", "bab"),
  MAJHUL("فُتِحَ", "fataha", note_ar=NAIB_HID[0] + "، يَعُودُ عَلَى «بَابًا» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لَهُ", note_en=NAIB_HID[1] + ", returning to «a door»; the clause qualifies it, in the seat of nasb", note_tr=NAIB_HID[2] + ", «kapı»ya döner; cümle onun na'tı, mahallen mansûb"),
  LI_MUSLIMIN((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«فُتِحَ»", "; the jarr phrase hangs on «opened»", "; câr-mecrûr «açıldı»ya müteallik")),
  ILA(), MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUDAF_ILAYH("الرُّومِ", "rum", "propn", punct=".")]})
S5.append({"id": "s5", "translation": {
  "en": "They entered those lands after it and settled in them, until they became part of the lands of Islam.",
  "tr": "Ondan sonra o diyara girdiler ve oraya yerleştiler; nihayet orası İslâm diyarından oldu."},
 "tokens": [VERB_WAW_ENC("فَدَخَلُوهَا", "dakhala", "هَا"),
  ZARF_ENC("بَعْدَهُ", "bada", "هُ", **ZAMAN, punct="،", note_ar=" — وَالضَّمِيرُ لِلنَّصْرِ", note_en=" — «it» is the victory", note_tr=" — zamir zafere döner"),
  VERB_WAW_ENC("وَسَكَنُوهَا", "sakana", "هَا", punct="،"),
  HATTA_IBT(), SARAT_X(),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ صَارَ", "; the jarr phrase hangs on the omitted predicate of صَارَ", " — câr-mecrûr sâra'nın mahzûf haberine müteallik")),
  MAJR("بِلَادِ", "bilad", **W(MUDAF)), MUDAF_ILAYH("الْإِسْلَامِ", "islam", punct=".")]})
S5.append({"id": "s6", "translation": {
  "en": "And people have never ceased to remember that day, down to this very day of ours.",
  "tr": "İnsanlar o günü bugünümüze kadar anmaktan hiç vazgeçmediler."},
 "tokens": [WA_MA("istinaf", (" — وَهِيَ مَعَ «زَالَ» تُفِيدُ الِاسْتِمْرَارَ", "; with «ceased» it means «still, never stopped»", "; zâle ile birlikte devam bildirir")),
  ZALA_X(),
  tok("النَّاسُ", "nas", "noun", ["kana-wa-akhawatuha"], "اسْمُ زَالَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of زَالَ, in raf'.", "Zâle'nin ismi, merfû."),
  MUDARI5("يَذْكُرُونَ", "dhakara", role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ", role_en="; the clause is the predicate of زَالَ, in the seat of nasb", role_tr="; cümle zâle'nin haberi, mahallen mansûb"),
  DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih"), BADAL("الْيَوْمَ", "yawm", "nasb"),
  ILA(), ENC_NOUN("يَوْمِنَا", "yawm", "نَا", "majr"),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "naat-sifa"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«يَوْمِ» (وَقِيلَ: بَدَلٌ مِنْهُ).",
      "A demonstrative «this», built on sukun, in the seat of jarr as the adjective of «day» (some call it a badal).",
      "İşaret ismi «bu», sükûn üzere mebnî, «gün»ün na'tı olarak mahallen mecrûr (bir görüşe göre bedel).", punct=".")]})

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
        "salah-al-din-wa-al-quds", "fath-al-qustantiniyya"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
# where the shelf holds one lemma under one key in several packages, take the entry whose gloss fits this story
FORCE = {"an": "abu-hanifa-wa-al-safina", "jam": "salah-al-din-wa-al-quds", "rum": "fath-al-qustantiniyya", "sultan": "fath-al-qustantiniyya",
         "man-mawsula": "talkhis-al-miftah", "jund": "dawud-wa-jalut", "qital": "salah-al-din-wa-al-quds", "kathir": "salah-al-din-wa-al-quds",
         "yad": "salah-al-din-wa-al-quds", "nafs": "salah-al-din-wa-al-quds", "bilad": "salah-al-din-wa-al-quds", "atlaqa": "salah-al-din-wa-al-quds",
         "hamala": "salah-al-din-wa-al-quds", "asir": "salah-al-din-wa-al-quds", "fida": "salah-al-din-wa-al-quds", "sulh": "salah-al-din-wa-al-quds",
         "rajul": "talkhis-al-miftah", "salla": "talkhis-al-miftah", "nasara": "wasiyyat-abi-hanifa-samti", "ahad": "wasiyyat-abi-yusuf-l5"}
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
 "alb": {"lemma": "أَلْب", "pos": "propn", "gloss": {"en": "Alp — Turkish «hero, valiant»: the first word of the name Alp Arslan (spoken with a quiescent end; the case shows on أَرْسَلَان)", "tr": "Alp — Türkçe «yiğit, kahraman»: Alparslan adının ilk kelimesi (sonu sâkin okunur; i'râb أَرْسَلَان üzerinde görünür)"}, "level": 6},
 "arslan": {"lemma": "أَرْسَلَان", "pos": "propn", "gloss": {"en": "Arslan — Turkish «lion»: the second word of the name Alp Arslan; a diptote (a proper name of foreign origin: ʿalamiyya + ʿujma)", "tr": "Arslan — Türkçe «aslan»: Alparslan adının ikinci kelimesi; gayr-i munsarif (yabancı asıllı özel isim: alemiyet + ucmet)"}, "level": 6},
 "armanus": {"lemma": "أَرْمَانُوس", "pos": "propn", "gloss": {"en": "Romanos IV Diogenes, Byzantine emperor (r. 1068–1071) — أَرْمَانُوس in the Arabic chronicles; a diptote (ʿalamiyya + ʿujma)", "tr": "Romen Diyojen (IV. Romanos Diogenes), Bizans imparatoru (s. 1068–1071) — Arapça kroniklerde أَرْمَانُوس; gayr-i munsarif (alemiyet + ucmet)"}, "level": 6},
 "turk": {"lemma": "التُّرْك", "pos": "propn", "gloss": {"en": "the Turks", "tr": "Türkler"}, "level": 4},
 "hudna": {"lemma": "هُدْنَة", "root": "ه د ن", "pos": "noun", "gloss": {"en": "a truce, an armistice", "tr": "ateşkes, mütareke"}, "level": 5},
 "khatib-preacher": {"lemma": "خَطِيب", "root": "خ ط ب", "pos": "noun", "gloss": {"en": "a preacher — the one who gives the Friday sermon (khuṭba) from the minbar", "tr": "hatip — cuma hutbesini minberden okuyan kimse"}, "level": 4},
 "alb-arslan": PHRASE("أَلْب أَرْسَلَان", 6, "Alp Arslan — the Seljuk sultan (r. 455–465 / 1063–1072), victor of Manzikert (463 / 1071)", "Alparslan — Selçuklu sultanı (s. 455–465 / 1063–1072), Malazgirt'in galibi (463 / 1071)",
    "literally «hero lion» (Turkish)", "lafzen «yiğit aslan» (Türkçe)",
    "A compound Turkish name written as two words. The whole name fills one seat in the sentence; the first word is spoken with a quiescent end and the case shows only on the last, أَرْسَلَان — a diptote (ʿalamiyya + ʿujma): أَرْسَلَانُ in raf', أَرْسَلَانَ in nasb and in jarr alike, never with tanwin.",
    "İki kelime olarak yazılan birleşik bir Türkçe isim. İsmin bütünü cümlede tek bir görev üstlenir; ilk kelime sâkin okunur, i'râb yalnızca sondaki أَرْسَلَان üzerinde görünür — gayr-i munsarif (alemiyet + ucmet): refte أَرْسَلَانُ, nasb ve cerde aynı şekilde أَرْسَلَانَ, asla tenvin almaz."),
 "ibn-al-athir": PHRASE("ابْنُ الْأَثِيرِ", 5, "Ibn al-Athīr — ʿIzz al-Dīn ʿAlī ibn Muḥammad (d. 630 / 1233), the historian, author of al-Kāmil fī al-Taʾrīkh", "İbnü'l-Esîr — İzzüddîn Ali b. Muhammed (ö. 630 / 1233), tarihçi, el-Kâmil fi't-Târîh'in yazarı",
    "literally «the son of al-Athīr»", "lafzen «el-Esîr'in oğlu»",
    "A name built as an idafa: ابْنُ takes the case of its seat, الْأَثِيرِ stays in jarr.",
    "İzâfetle kurulmuş bir isim: ابْنُ bulunduğu yerin i'râbını alır, الْأَثِيرِ daima mecrûrdur."),
}
# a key is a global claim: a NEW key must not already name something else on the shelf
for k in NEW_GLOSS:
    hit = [p for p in PREF if k in _G[p]]
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
# the shelf's one entry for ذَكَرَ carries a gloss tied to its own sentence («(here) to speak of with blame»); same lemma and
# key, but the gloss shown in THIS story is the plain sense the two sentences use (to report; to remember)
GLOSS["dhakara"] = {**GLOSS["dhakara"], "gloss": {"en": "to mention, to report; to remember", "tr": "anmak, zikretmek; nakletmek"}}
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
 "title": {"ar": "أَلْب أَرْسَلَانُ وَمَلَاذْكِرْد", "en": "Alp Arslan and Manzikert", "tr": "Alparslan ve Malazgirt"},
 "subtitle": {"ar": "هُدْنَةٌ مَرْدُودَةٌ، وَسَاعَةُ الْجُمُعَةِ، وَمَلِكٌ أَسِيرٌ يُطْلَقُ مُكْرَمًا — قِصَّةٌ لِلْمُسْتَوَى السَّادِسِ",
              "en": "A truce refused, the Friday hour, and a captive king set free with honour — a story for the sixth level",
              "tr": "Reddedilen ateşkes, cuma vakti ve ikramla serbest bırakılan esir kral — altıncı seviye için bir hikâye"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى السَّادِسُ) لِخَبَرِ وَقْعَةِ السُّلْطَانِ أَلْب أَرْسَلَانَ وَمَلِكِ الرُّومِ أَرْمَانُوسَ سَنَةَ ٤٦٣ هـ / ١٠٧١ م، عَلَى مَا يَتَّفِقُ عَلَيْهِ مَنْ رَوَاهُ: ابْنُ الْأَثِيرِ فِي «الْكَامِلِ فِي التَّارِيخِ»، وَسِبْطُ ابْنِ الْجَوْزِيِّ فِي «مِرْآةِ الزَّمَانِ». النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ تِلْكَ الْكُتُبِ، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا قَوْلٌ يُنْسَبُ إِلَى أَحَدٍ؛ وَخَبَرُ سَاعَةِ الْجُمُعَةِ مَحْكِيٌّ عَنِ ابْنِ الْأَثِيرِ. وَتُرِكَتِ الْمُحَاوَرَةُ الْمَشْهُورَةُ بَيْنَ السُّلْطَانِ وَأَسِيرِهِ لِاخْتِلَافِ أَلْفَاظِهَا فِي الرِّوَايَاتِ، وَتُرِكَتْ أَعْدَادُ الْجُيُوشِ وَمَقَادِيرُ الْفِدَاءِ.",
  "en": "ORIGINAL Level-6 graded Arabic in a classical narrative register: Sultan Alp Arslan and the Byzantine emperor Romanos IV Diogenes (أَرْمَانُوس) at Manzikert (463 AH / 1071 CE), RETOLD FREELY along the well-attested core of the classical accounts — Ibn al-Athīr (al-Kāmil fī al-Taʾrīkh) and Sibṭ ibn al-Jawzī (Mirʾāt al-Zamān). No sentence is a quotation from these works; no āya or ḥadīth is quoted; no words are put in a historical person's mouth. The choice of the Friday hour is presented as Ibn al-Athīr's report. Left out: the famous dialogue between the sultan and his captive (its wording varies across the reports), the sizes of the armies and the ransom figures.",
  "tr": "ÖZGÜN 6. seviye Arapça, klasik anlatı üslûbunda: Sultan Alparslan ile Bizans imparatoru Romen Diyojen'in (أَرْمَانُوس) Malazgirt'teki karşılaşması (463 h. / 1071 m.), klasik kaynakların — İbnü'l-Esîr (el-Kâmil fi't-Târîh) ve Sıbt İbnü'l-Cevzî (Mir'âtü'z-Zamân) — üzerinde birleştiği sağlam çekirdeğe bağlı kalınarak SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bu eserlerden alıntı değildir; hiçbir âyet veya hadis aktarılmamış, tarihî bir şahsın ağzına söz konmamıştır. Cuma vaktinin seçilmesi İbnü'l-Esîr'in rivayeti olarak verilmiştir. Dışarıda bırakılanlar: sultan ile esiri arasındaki meşhur konuşma (lafızları rivayetlerde farklıdır), ordu sayıları ve fidye miktarları.",
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
