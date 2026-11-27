"""Author content/samples/abu-hanifa-wa-al-safina — «أَبُو حَنِيفَةَ وَالسَّفِينَةُ», an ORIGINAL story at Level 5 (Advanced).

ORIGINAL graded Arabic: Imam Abū Ḥanīfa's argument with the deniers of the Maker (the dahriyya). He puts to them a ship laden
with goods that crosses the sea, keeps its course, unloads and returns with no sailor and no one to steer it; they answer that
reason cannot accept it; he answers that if a single ship cannot run without someone to run it, the whole ordered world cannot
run without a Maker — and they are silenced (some versions add that they repented). The report is told in the Ḥanafī manāqib
(al-Muwaffaq al-Makkī, Ibn al-Bazzāz al-Kardarī) and in later creed commentaries; it is RETOLD FREELY here and framed as a
retelling: no sentence is a quotation of any source, no āya and no ḥadīth text is quoted, and the dialogue is narrative
paraphrase, not a recorded wording. The details on which the versions differ (swords drawn, the late-arrival variant) are left out; the mosque setting follows the common version.

Four chapters, twenty-eight sentences, in a Level-5 register: mafʿūl muṭlaq (رَدًّا شَدِيدًا، جَوَابَ مَنْ لَا يَشُكُّ، سُكُوتًا طَوِيلًا،
سُبْحَانَ), mafʿūl lahu (طَلَبًا، حَيْرَةً), tamyīz (حُجَّةً، جِدَالًا، مَتَاعًا، شَأْنًا، أَحْوَالًا), istithnāʾ mufarragh (إِلَّا بِصَانِعٍ),
the conditional with لَوْ / إِنْ / إِذَا, the rhetorical question with أَ / هَلْ / كَيْفَ, kāna and its sisters (كَانَ، يَكُونُ، لَيْسَ، صَارَ،
مَا زَالَ), relative clauses with a resumptive pronoun, لَمَّا, حَتَّى + subjunctive and the wāw of ḥāl.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf (the majority reading of a key
wins); five nouns are new — مَنْقَبَة (pl. مَنَاقِب), دَهْرِيَّة, مَلَّاح, مُنَاظَرَة, حَيْرَة — and no new verb is minted (every verb's
paradigm is copied from a package that already owns it).  Regenerate with:
python3 tools/authoring/author_abu_hanifa_wa_al_safina.py
"""
import json, os, pathlib, re, sys, unicodedata, collections

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "abu-hanifa-wa-al-safina"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "هُمْ": "هُمْ", "هِمْ": "هُمْ"})

# ---- the clause seats this story needs (ar, en, tr) -------------------------------------------------------------------
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
KH_ANNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
def NAAT_OF(seat, of_ar, of_en, of_tr, second=False):
    """the clause (or jarr phrase) is the na't of a named indefinite noun"""
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return (" — وَالْجُمْلَةُ فِي مَحَلِّ " + s[0] + " نَعْتٌ " + ("ثَانٍ " if second else "") + "لِـ«" + of_ar + "»",
            "; the clause qualifies «" + of_en + "» — " + ("a second na't, " if second else "") + "in the seat of " + s[1],
            "; cümle «" + of_tr + "» için " + ("ikinci " if second else "") + "na't, mahallen " + s[2])
def JAR_NAAT(seat, of_ar, of_en, of_tr):
    s = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[seat]
    return ("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ " + s[0] + " نَعْتٌ لِـ«" + of_ar + "»",
            "; the jarr phrase qualifies «" + of_en + "», in the seat of " + s[1],
            "; câr-mecrûr «" + of_tr + "» için na't, mahallen " + s[2])

# ---- names and the five nouns ------------------------------------------------------------------------------------------
HANIFA_MI = lambda punct=None: tok("حَنِيفَةَ", "hanifa", "propn", ["idafa-definiteness", "mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-alam-wal-sifa-wal-ajami-wal-muannath"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ.",
    "The second term of the idafa, in jarr — the fatha stands for the kasra: a proper name with the feminine ta, barred from tanwin.",
    "Muzâfun ileyh, mecrûr — alemiyyet ve te'nîs sebebiyle gayr-i munsarif olduğu için kesre yerine fetha ile.", punct=punct)
ABU_ISMK = lambda: tok("أَبُو", "ab", "noun", ["kana-wa-akhawatuha", "five-nouns", "idafa-definiteness"],
    "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.",
    "The noun of كَانَ, in raf' by the waw — one of the five nouns; annexed.", "Kâne'nin ismi, esmâ-i hamseden olduğu için vâv ile merfû; muzâf.")
ABI_BADAL = lambda: tok("أَبِي", "ab", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "five-nouns", "idafa-definiteness"],
    "بَدَلٌ مِنَ «الْإِمَامِ» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.",
    "A badal of «the Imam», in jarr by the ya — one of the five nouns; annexed.", "«İmam»dan bedel, esmâ-i hamseden olduğu için yâ ile mecrûr; muzâf.")

# ---- particles and short words ------------------------------------------------------------------------------------------
def LAHUM(punct=None):
    return tok("لَهُمْ", "li", "prep", ["huruf-jarr", "al-bariz-al-muttasil"], "اللَّامُ حَرْفُ جَرٍّ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.",
        "The lam is a jarr letter; the attached «them» fills the seat of jarr.", "Lâm cer harfi; bitişik «onlar» zamiri mahallen mecrûr («onlara»).", punct=punct,
        segments=[seg("لَ", "li", "prep"), seg("هُمْ", "pron-3mp", "pron")])
AN_PREP = lambda punct=None: PREP("عَنْ", "an", gloss_tr="«-den, hakkında»", punct=punct)
def ANNA_T(role=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + role[0] + ".",
        "أَنَّ «that» is the verb-like particle that builds a masdar: its noun in nasb, its predicate in raf'" + role[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + role[2] + ".")
ISM_ANNA = lambda full, lex: tok(full, lex, "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, in nasb.", "Enne'nin ismi, mansûb.")
BILA = lambda: tok("بِلَا", "bila", "prep", ["huruf-jarr", "la-nafiya"],
    "الْبَاءُ حَرْفُ جَرٍّ، وَلَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ لَا عَمَلَ لَهَا، وَمَا بَعْدَهَا مَجْرُورٌ بِالْبَاءِ.",
    "«without»: the ba is a jarr letter and لَا, slipped in between, only strengthens the negation and governs nothing; the noun after it is in jarr by the ba.",
    "«-sız»: bâ cer harfi; araya giren lâ yalnız nefyi pekiştirir, amel etmez; sonraki isim bâ ile mecrûr.",
    segments=[seg("بِ", "bi", "prep"), seg("لَا", "la-nafiya", "part")])
def BILA_N(full, lex, role=("", "", ""), punct=None, extra=None):
    return tok(full, lex, "noun", ["huruf-jarr"] + (extra or []), "مَجْرُورٌ بِالْبَاءِ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ" + role[0] + ".",
        "In jarr by the ba (لَا between them governs nothing)" + role[1] + ".", "Bâ ile mecrûr; aradaki lâ amel etmez" + role[2] + ".", punct=punct)
WA_LA_ZAIDA = lambda: tok("وَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"], WA_AR + "لَا زَائِدَةٌ لِتَأْكِيدِ النَّفْيِ.",
    "The waw conjoins; لَا only strengthens the negation already in force.", "«ve» + lâ, nefyi pekiştirmek için zâiddir.",
    segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
DHALIKA = lambda seat_ar, seat_en, seat_tr, extra=None, punct=None: ISHARA("ذٰلِكَ", "dhalika", seat_ar, seat_en, seat_tr, built_ar="الْفَتْحِ", built_en="fatha", built_tr="fetha", extra=extra, punct=punct)
HADHA = lambda seat_ar, seat_en, seat_tr, extra=None, punct=None: ISHARA("هٰذَا", "hadha", seat_ar, seat_en, seat_tr, extra=extra, punct=punct)
HATTA = lambda: tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
    "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
    "حَتَّى «until» is a particle of limit and jarr: the present verb after it is in nasb by an أَنْ that must stay hidden, and the masdar they build is in jarr by حَتَّى.",
    "Hattâ — gâye ve cer harfi: sonraki muzâri vücûben gizli en ile mansûb; kurdukları müevvel masdar hattâ ile mecrûr.")
LAW = lambda: tok("لَوْ", "law", "part", ["al-majzum-wal-shart-wal-jaza", "huruf-al-shart-fil-kafiya"],
    "حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ، حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.",
    "لَوْ «if (it were so)»: a conditional particle that governs no jazm — the answer is held back because the condition is held back.",
    "Lev — cezmetmeyen şart harfi, imtinâ' li-imtinâ': şart gerçekleşmediği için cevap da gerçekleşmez.")
WA_ISTINAF_T = lambda full, lex, rest_ar, rest_en, rest_tr, grammar, pos="noun", punct=None: tok(full, lex, pos, grammar,
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَ" + rest_ar, "The waw opens a new sentence; " + rest_en, "Vâv isti'nâf içindir; " + rest_tr, punct=punct,
    segments=[seg("وَ", "wa", "conj"), seg(full[2:], lex, pos)])

# ---- the verb shapes the kit does not carry ------------------------------------------------------------------------------
def MUD_ENC_DF(full, lex, enc, extra=None, punct=None, note=("", "", "")):
    """يَضْرِبُهَا الْمَوْجُ، يَقْبَلُهُ الْعَقْلُ: a present verb in raf' with its object pronoun, the doer following"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, lex, "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi"] + (extra or []),
        ar0 + "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ" + note[0] + ".",
        en0 + "present verb in raf'; the attached pronoun is its object, placed before the doer, which follows" + note[1] + ".",
        tr0 + "merfû muzâri; bitişik zamir fâilden önce gelmiş mef'ûlün bih, mahallen mansûb; fâili ondan sonra gelir" + note[2] + ".",
        punct=punct, segments=[s for s in [sg, seg(stem[:-len(enc)], lex, "verb"), seg(enc, PRON[enc], "pron")] if s])
def SUBJ(full, lex, how, extra=None, punct=None, who="هِيَ", ya=False, note=("", "", "")):
    """a present verb in nasb: how = 'an' (by أَنْ), 'hatta' (by a hidden أَنْ after حَتَّى) or 'atf' (conjoined to تَبْلُغَ)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    gov = {"an": ("مَنْصُوبٌ بِأَنْ", "in nasb by أَنْ", "en ile mansûb"),
           "hatta": ("مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى", "in nasb by an أَنْ hidden of necessity after حَتَّى", "hattâ'dan sonra vücûben gizli en ile mansûb"),
           "atf": ("مَعْطُوفٌ عَلَى «تَبْلُغَ» مَنْصُوبٌ مِثْلَهُ", "conjoined to «reach» and in nasb like it", "«ulaşır»a ma'tûf, onun gibi mansûb")}[how]
    sign = ("وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", "its fatha SHOWS on the ya, which bears it lightly", "fetha hafif olduğu için yâ üzerinde zâhirdir") if ya else \
           ("وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ", "its sign the fatha", "alâmeti fetha")
    hid = ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + who, "; the doer is a hidden pronoun «" + who + "»", "; fâil gizli zamir «" + who + "»") if who else \
          ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
    return tok(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari"] + (["atf-nasaq"] if how == "atf" else []) + (extra or []),
        ar0 + "فِعْلٌ مُضَارِعٌ " + gov[0] + " " + sign[0] + hid[0] + note[0] + ".",
        en0 + "present verb " + gov[1] + ", " + sign[1] + hid[1] + note[1] + ".",
        tr0 + gov[2] + " muzâri, " + sign[2] + hid[2] + note[2] + ".", punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def MUTLAQ_NAW(full, lex, verb_ar, verb_en, verb_tr, how=("بِوَصْفِهِ", "by the adjective after it", "sıfatıyla"), mudaf=False, extra=None, punct=None, note=("", "", "")):
    """رَدًّا شَدِيدًا، سُكُوتًا طَوِيلًا، جَوَابَ مَنْ…: the absolute object that names the KIND of the act"""
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"] + (["idafa-definiteness"] if mudaf else []) + (extra or []),
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ" + ("، مُضَافٌ" if mudaf else "") + " — مَصْدَرُ «" + verb_ar + "» مُبَيِّنٌ لِلنَّوْعِ " + how[0] + note[0] + ".",
        "The absolute object (maf'ul mutlaq), in nasb" + (" and annexed" if mudaf else "") + " — the masdar of «" + verb_en + "», naming the KIND of the act " + how[1] + note[1] + ".",
        "Mef'ûlün mutlak, mansûb" + (", muzâf" if mudaf else "") + " — «" + verb_tr + "» fiilinin masdarı; " + how[2] + " fiilin nev'ini beyan eder" + note[2] + ".", punct=punct)
def LIAJLIH(full, lex, why_ar, why_en, why_tr, punct=None):
    """طَلَبًا، حَيْرَةً: the object of reason (mafʿūl lahu)"""
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"],
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ يُبَيِّنُ عِلَّةَ " + why_ar + "، وَيَتَّحِدُ مَعَهُ فِي الْوَقْتِ وَالْفَاعِلِ.",
        "The object of reason (maf'ul li-ajlihi), in nasb — a masdar giving the cause of " + why_en + "; it shares the verb's time and doer.",
        "Mef'ûlün leh, mansûb — " + why_tr + " sebebini bildiren masdar; fiille vakitte ve fâilde birleşir.", punct=punct)
def TAMYIZ_T(full, lex, what_ar, what_en, what_tr, punct=None):
    return tok(full, lex, "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"],
        "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ " + what_ar + ".", "A specifier (tamyiz), in nasb — it names " + what_en + ".", "Temyîz, mansûb — " + what_tr + " beyan eder.", punct=punct)
TAFDIL_TAMYIZ = ("جِهَةَ التَّفْضِيلِ", "the respect in which the comparison holds", "üstünlüğün hangi yönden olduğunu")

def KHABAR_INNA(full, lex, extra=None, punct=None, note=("", "", "")):
    return tok(full, lex, "noun", ["inna-wa-akhawatuha"] + (extra or []), "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ" + note[0] + ".", "The predicate of إِنَّ, in raf'" + note[1] + ".", "İnne'nin haberi, merfû" + note[2] + ".", punct=punct)

TITLES = [{"ar": "الْإِمَامُ وَالدَّهْرِيَّةُ", "en": "The Imam and the Dahriyya", "tr": "İmam ve Dehriyye"},
          {"ar": "السُّؤَالُ", "en": "The question", "tr": "Soru"},
          {"ar": "الْجَوَابُ", "en": "The answer", "tr": "Cevap"},
          {"ar": "بَعْدَ الْمُنَاظَرَةِ", "en": "After the debate", "tr": "Münazaradan sonra"}]

# ============================================ Chapter 1 — الْإِمَامُ وَالدَّهْرِيَّةُ ============================================
S1 = []
S1.append({"id": "s1", "translation": {"en": "The authors of the manāqib books relate a report about Imam Abū Ḥanīfa, which we tell here in our own words.",
                                      "tr": "Menâkıb yazarları İmam Ebû Hanîfe hakkında bir haber naklederler; biz onu burada kendi sözlerimizle anlatıyoruz."},
 "tokens": [MUDARI_DF("يَذْكُرُ", "dhakara"),
  FAIL("أَصْحَابُ", "sahib", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ صَاحِبٍ", note_en=", annexed — the broken plural of صَاحِب", note_tr=", muzâf — sâhib'in cem-i teksîri"),
  MUDAF_ILAYH("الْمَنَاقِبِ", "manqaba", extra=["jam-taksir", "mamnu-min-sarf", "ghayr-al-munsarif-al-qiyasi-al-tanith-wal-tarkib-wal-alif-nun-wal-jam-wa-insirafuh"],
    note_ar=" — جَمْعُ مَنْقَبَةٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُعَرَّفٌ بِأَلْ",
    note_en=" — the plural of مَنْقَبَة on the farthest-plural pattern; a diptote, it takes the kasra here because it carries ال",
    note_tr=" — menkabe'nin müntehe'l-cumû' vezninde cem'i; gayr-i munsarif iken el-takısı aldığı için kesre ile mecrûr"),
  MAFUL("خَبَرًا", "khabar"), AN_KASRA(), MAJR("الْإِمَامِ", "imam"), ABI_BADAL(), HANIFA_MI(punct="،"),
  MUDARI("نَحْكِيهِ", "haka", ["naqis-verbs", "jumla-sifa"], who="نَحْنُ", enc="هِ", naqis="ي", wujub=True,
    note_ar=NAAT_OF("nasb", "خَبَرًا", "a report", "haber")[0], note_en=NAAT_OF("nasb", "خَبَرًا", "a report", "haber")[1], note_tr=NAAT_OF("nasb", "خَبَرًا", "a report", "haber")[2]),
  HUNA(), BI_NOUN("بِأَلْفَاظِنَا", "lafz", "أَلْفَاظِنَا", enc="نَا", extra=["jam-taksir"], note_ar=" — جَمْعُ لَفْظٍ", note_en=" — «our words», the plural of لَفْظ", note_tr=" — lafz'ın cem'i, «sözlerimiz»", punct=".")]})

S1.append({"id": "s2", "translation": {"en": "Abū Ḥanīfa was the strongest of the people of his time in argument, and the best of them at disputing in defence of the religion.",
                                      "tr": "Ebû Hanîfe, zamanının insanları içinde delilce en güçlüsü, din adına tartışmada da en iyisiydi."},
 "tokens": [KANA("كَانَ"), ABU_ISMK(), HANIFA_MI(),
  KHK("أَقْوَى", "aqwa", extra=["ism-tafdil", "idafa-definiteness"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ",
    note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ", note_en=" — the fatha is estimated on the alif; an elative «strongest», annexed", note_tr=" — fetha elif üzerinde takdîrî; ism-i tafdîl «en güçlü», muzâf"),
  MUDAF_ILAYH("أَهْلِ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf"),
  TAMYIZ_T("حُجَّةً", "hujja", *TAFDIL_TAMYIZ, punct="،"),
  tok("وَأَحْسَنَهُمْ", "ahsan", "noun", ["atf-nasaq", "kana-wa-akhawatuha", "ism-tafdil", "idafa-definiteness", "al-bariz-al-muttasil"],
    WA_AR + "أَحْسَنَ مَعْطُوفٌ عَلَى «أَقْوَى» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — اسْمُ تَفْضِيلٍ.",
    "The waw conjoins; «the best of them» is conjoined to «strongest», a second predicate of كَانَ in nasb, annexed to «them» in the seat of jarr — an elative.",
    "Vâv atıf; «onların en iyisi», «en güçlü»ye ma'tûf, kâne'nin ikinci haberi, mansûb; «onlar» zamirine muzâf, zamir mahallen mecrûr — ism-i tafdîl.",
    segments=[seg("وَ", "wa", "conj"), seg("أَحْسَنَ", "ahsan", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  TAMYIZ_T("جِدَالًا", "jidal", *TAFDIL_TAMYIZ), AN_KASRA(),
  MAJR("الدِّينِ", "din", punct=".", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«جِدَالًا»", note_en=" — the jarr phrase attaches to «disputing»", note_tr=" — câr-mecrûr «tartışma»ya müteallik")]})

S1.append({"id": "s3", "translation": {"en": "In his age there were people of the Dahriyya who denied the Maker and claimed that the world runs by itself.",
                                      "tr": "Onun çağında Dehriyye'den bir topluluk vardı; Yaratıcıyı inkâr ediyor ve âlemin kendi kendine yürüdüğünü iddia ediyorlardı."},
 "tokens": [KANA("وَكَانَ"), FI(), ENC_NOUN("عَصْرِهِ", "asr", "هِ", "majr", note_ar=KH_MUQ[0], note_en=KH_MUQ[1], note_tr=KH_MUQ[2]),
  ISMK("قَوْمٌ", "qawm", muakhkhar=True), MINA(),
  MAJR("الدَّهْرِيَّةِ", "dahriyya", note_ar=JAR_NAAT("raf", "قَوْمٌ", "people", "topluluk")[0], note_en=JAR_NAAT("raf", "قَوْمٌ", "people", "topluluk")[1], note_tr=JAR_NAAT("raf", "قَوْمٌ", "people", "topluluk")[2]),
  MUDARI5("يُنْكِرُونَ", "ankara", extra=["form-iv-verbs", "jumla-sifa"], note_ar=NAAT_OF("raf", "قَوْمٌ", "people", "topluluk", True)[0], note_en=NAAT_OF("raf", "قَوْمٌ", "people", "topluluk", True)[1], note_tr=NAAT_OF("raf", "قَوْمٌ", "people", "topluluk", True)[2]),
  MAFUL("الصَّانِعَ", "sani", extra=["ism-fail"], punct="،"),
  MUDARI5("وَيَزْعُمُونَ", "zaama-claim", extra=["atf-nasaq", "zanna-wa-akhawatuha"], note_ar=" — مَعْطُوفٌ عَلَى «يُنْكِرُونَ»", note_en=" — conjoined to «they denied»", note_tr=" — «inkâr ederler»e ma'tûf"),
  ANNA_T((" — وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ «يَزْعُمُونَ»", "; the clause it builds stands for both objects of «they claimed»", "; kurduğu müevvel masdar «iddia ederler»in iki mef'ûlünün yerini tutar")),
  ISM_ANNA("الْعَالَمَ", "alam"),
  MUDARI("يَجْرِي", "jara", ["naqis-verbs"], naqis="ي", note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]),
  BI_NOUN("بِنَفْسِهِ", "nafs", "نَفْسِهِ", enc="هِ", punct=".")]})

S1.append({"id": "s4", "translation": {"en": "And the Imam used to refute their claim against them with a forceful refutation.",
                                      "tr": "İmam da onların sözünü şiddetli bir şekilde reddederdi."},
 "tokens": [KANA("وَكَانَ"), ISMK("الْإِمَامُ", "imam"),
  MUDARI_KH("يَرُدُّ", "radda", extra=["doubled-verbs"], note_ar=" — كَانَ مَعَ الْمُضَارِعِ تُفِيدُ التَّكْرَارَ فِي الْمَاضِي", note_en="; كَانَ with a present verb tells of what used to happen again and again", note_tr="; kâne muzâri ile geçmişte tekrarlanan işi bildirir"),
  ALAYHIM(), ENC_NOUN("قَوْلَهُمْ", "qawl", "هُمْ", "maful"),
  MUTLAQ_NAW("رَدًّا", "radd", "يَرُدُّ", "refute", "reddeder"), NAAT("شَدِيدًا", "shadid", "nasb", ["sifa-mushabbaha"], punct=".")]})

S1.append({"id": "s5", "translation": {"en": "One day a party of them came to him while he was sitting in his mosque, seeking to debate with him.",
                                      "tr": "Bir gün onlardan bir grup, o mescidinde otururken, onunla münazara etmek isteyerek yanına geldi."},
 "tokens": [ENC_MADI("فَجَاءَتْهُ", "jaa", "هُ", extra=["hollow-verbs"], fem=True), FAIL("طَائِفَةٌ", "taifa"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", note_ar=JAR_NAAT("raf", "طَائِفَةٌ", "a party", "grup")[0], note_en=JAR_NAAT("raf", "طَائِفَةٌ", "a party", "grup")[1], note_tr=JAR_NAAT("raf", "طَائِفَةٌ", "a party", "grup")[2]), ZARF("يَوْمًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"), KHABAR("جَالِسٌ", "jalis-sitting", ["ism-fail"]), FI(), ENC_NOUN("مَسْجِدِهِ", "masjid", "هِ", "majr", punct="،"),
  LIAJLIH("طَلَبًا", "talab", "الْمَجِيءِ", "their coming", "gelişin"),
  LI_ENC("لِمُنَاظَرَتِهِ", "munazara", "مُنَاظَرَتِ", "هِ", punct=".")]})

S1.append({"id": "s6", "translation": {"en": "He said to them: «Answer me one question, then say what you will.»",
                                      "tr": "Onlara dedi: «Bana tek bir soruya cevap verin, sonra dilediğinizi söyleyin.»"},
 "tokens": [MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), LAHUM(punct=":"),
  tok("أَجِيبُونِي", "ajaba", "verb", ["imperative-amr", "form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "ya-al-mutakallim", "maful-bihi"],
    "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَوَاوُ الْجَمَاعَةِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    "Imperative built on the dropped nun; the waw of the group is its doer, in the seat of raf'; the nun guards the verb, and the speaker's ya is its object, in the seat of nasb — «answer me».",
    "Nûnun hazfi üzere mebnî emir; cemâat vâvı fâil, mahallen merfû; nûn vikâye içindir, mütekellim yâ'sı mef'ûlün bih, mahallen mansûb — «bana cevap verin».",
    segments=[seg("أَجِيبُ", "ajaba", "verb"), seg("و", "pron-3mp", "pron"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")]),
  AN_PREP(), MAJR("مَسْأَلَةٍ", "masala"), NAAT("وَاحِدَةٍ", "wahid", "jarr", punct="،"), THUMMA(),
  AMR5("قُولُوا", "qala", ["hollow-verbs"]),
  MAWSUL_MAF("مَا", "ma-mawsula", built="السُّكُونِ", built_en="sukun", built_tr="sükûn"),
  tok("شِئْتُمْ", "shaa", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "ism-mawsul"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ الْمُتَحَرِّكِ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْمِيمُ عَلَامَةُ الْجَمْعِ" + SILA[0] + "، وَالْعَائِدُ مَحْذُوفٌ: مَا شِئْتُمُوهُ.",
    "Past verb built on sukun before the moving pronoun of the doer (its middle letter dropped where two quiescents met); the ta «you» is the doer, the mim marks the plural" + SILA[1] + "; the pronoun that returns to مَا is dropped («what you will [it]»).",
    "Hareketli ref' zamiri bitiştiği için sükûn üzere mebnî mâzî (iki sâkin karşılaşınca aynı düştü); tâ fâil, mîm cem' alâmeti" + SILA[2] + "; mevsûle dönen zamir hazfedilmiştir.", punct=".")]})

S1.append({"id": "s7", "translation": {"en": "They accepted that, and sat waiting for his question.",
                                      "tr": "Onlar bunu kabul ettiler ve sorusunu bekleyerek oturdular."},
 "tokens": [VERB_WAW("فَقَبِلُوا", "qabila"), DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", extra=["maful-bihi"], punct="،"),
  VERB_WAW("وَجَلَسُوا", "jalasa"),
  MUDARI5("يَنْتَظِرُونَ", "intazara", extra=["form-viii-verbs", "hal"], note_ar=HAL_CL[0], note_en=HAL_CL[1], note_tr=HAL_CL[2]),
  ENC_NOUN("سُؤَالَهُ", "sual", "هُ", "maful", punct=".")]})

# ================================================== Chapter 2 — السُّؤَالُ ==================================================
S2 = []
S2.append({"id": "s1", "translation": {"en": "He said: «What do you say of a ship laden with goods, running in the middle of the sea?»",
                                      "tr": "Dedi: «Yükle dolu, denizin ortasında yüzen bir gemi hakkında ne dersiniz?»"},
 "tokens": [MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=":", note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]),
  tok("مَا", "ma-istifham", "pron", ["al-istifham", "maful-bihi"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِـ«تَقُولُونَ».",
    "مَا «what?» is an interrogative noun built on sukun, in the seat of nasb as the fronted object of «you say».", "Mâ «ne?» — istifhâm ismi, sükûn üzere mebnî; «dersiniz»in öne alınmış mef'ûlü olarak mahallen mansûb."),
  MUDARI5("تَقُولُونَ", "qala", extra=["hollow-verbs"]), FI(), MAJR("سَفِينَةٍ", "safina"),
  NAAT("مَمْلُوءَةٍ", "mamlu", "jarr", ["ism-maful"]),
  TAMYIZ_T("مَتَاعًا", "mata-goods", "مَا امْتَلَأَتْ بِهِ السَّفِينَةُ", "what the ship is filled with", "geminin neyle dolu olduğunu", punct="،"),
  MUDARI("تَجْرِي", "jara", ["naqis-verbs", "jumla-sifa"], who="هِيَ", naqis="ي", note_ar=NAAT_OF("jarr", "سَفِينَةٍ", "a ship", "gemi", True)[0], note_en=NAAT_OF("jarr", "سَفِينَةٍ", "a ship", "gemi", True)[1], note_tr=NAAT_OF("jarr", "سَفِينَةٍ", "a ship", "gemi", True)[2]),
  FI(), MAJR("وَسَطِ", "wasat", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْبَحْرِ", "bahr", punct="؟")]})

S2.append({"id": "s2", "translation": {"en": "«The waves strike it from every side, while it goes on straight and does not swerve.»",
                                      "tr": "«Dalgalar onu her yandan döver; o ise dosdoğru ilerler, sapmaz.»"},
 "tokens": [MUD_ENC_DF("يَضْرِبُهَا", "daraba", "هَا"), FAIL("الْمَوْجُ", "mawj"), MIN(), MAJR("كُلِّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("جَانِبٍ", "janib", punct="،"),
  PRON_MUB("وَهِيَ", "hiya", pre="hal"),
  MUDARI("تَمْضِي", "mada", ["naqis-verbs"], who="هِيَ", naqis="ي", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]),
  HAL("مُسْتَقِيمَةً", "mustaqim", ["ism-fail"]), LA_NAFIYA(),
  MUDARI("تَمِيلُ", "mala", ["hollow-verbs", "hal"], who="هِيَ", punct=".", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ", note_en="; the clause is a second hal, in the seat of nasb", note_tr="; cümle ikinci hâl olarak mahallen mansûb")]})

S2.append({"id": "s3", "translation": {"en": "«There is no sailor in it to steer it, and no one to keep it.»",
                                      "tr": "«İçinde onu yürüten bir gemici yok, onu koruyan hiç kimse de yok.»"},
 "tokens": [tok("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "atf-nasaq"], WA_AR + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
    "The waw conjoins; لَيْسَ «there is not» is the frozen defective verb, built on fatha: it raises its noun and puts its predicate in nasb.",
    "«ve» + leyse: fetha üzere mebnî, câmid nâkıs mâzî; ismini ref, haberini nasb eder.", segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («içinde»)", note_ar="، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ لَيْسَ مُقَدَّمٌ", note_en="; the jarr phrase is the FRONTED predicate of لَيْسَ", note_tr="; câr-mecrûr leyse'nin öne alınmış haberi"),
  tok("مَلَّاحٌ", "mallah", "noun", ["kana-wa-akhawatuha"], "اسْمُ لَيْسَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — عَلَى وَزْنِ فَعَّالٍ لِأَصْحَابِ الْحِرَفِ.",
    "The noun of لَيْسَ, placed after its predicate, in raf' — on the pattern فَعَّال used for a trade.", "Leyse'nin ismi (haberinden sonra), merfû — meslek bildiren fa''âl vezninde."),
  MUDARI("يُجْرِيهَا", "ajra", ["form-iv-verbs", "naqis-verbs", "jumla-sifa"], enc="هَا", naqis="ي", punct="،",
    note_ar=NAAT_OF("raf", "مَلَّاحٌ", "a sailor", "gemici")[0], note_en=NAAT_OF("raf", "مَلَّاحٌ", "a sailor", "gemici")[1], note_tr=NAAT_OF("raf", "مَلَّاحٌ", "a sailor", "gemici")[2]),
  WA_LA_ZAIDA(),
  ATF("أَحَدٌ", "ahad", "noun", "raf", note_ar=" عَلَى «مَلَّاحٌ» اسْمِ لَيْسَ", note_en=" — on «a sailor», the noun of لَيْسَ", note_tr=" — leyse'nin ismi «gemici»ye"),
  MUDARI("يَحْفَظُهَا", "hafiza", ["jumla-sifa"], enc="هَا", punct=".", note_ar=NAAT_OF("raf", "أَحَدٌ", "anyone", "kimse")[0], note_en=NAAT_OF("raf", "أَحَدٌ", "anyone", "kimse")[1], note_tr=NAAT_OF("raf", "أَحَدٌ", "anyone", "kimse")[2])]})

S2.append({"id": "s4", "translation": {"en": "«So it travels alone until it reaches the shore, sets down its goods, and then goes back.»",
                                      "tr": "«Böylece tek başına yol alır; sonunda kıyıya varır, yükünü bırakır, sonra geri döner.»"},
 "tokens": [MUDARI("فَتَسِيرُ", "sara-travel", ["hollow-verbs"], who="هِيَ"),
  tok("وَحْدَهَا", "wahda", "noun", ["hal", "idafa-definiteness", "al-bariz-al-muttasil"], "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَ«وَحْدَ» لَا يَقَعُ إِلَّا حَالًا.",
    "The hal «alone», in nasb and annexed to the pronoun «it»; وَحْدَ is only ever a hal.", "Hâl «tek başına», mansûb; «o» zamirine muzâf — vahde yalnız hâl olarak gelir.",
    segments=[seg("وَحْدَ", "wahda", "noun"), seg("هَا", "pron-3fs", "pron")]),
  HATTA(), SUBJ("تَبْلُغَ", "balagha", "hatta"), MAFUL("السَّاحِلَ", "sahil", punct="،"),
  SUBJ("فَتَضَعَ", "wadaa", "atf", ["mithal-verbs"], note=(" — وَحُذِفَتْ فَاؤُهُ الْوَاوُ فِي الْمُضَارِعِ: وَضَعَ يَضَعُ", "; its first radical, the waw, drops in the present (وَضَعَ يَضَعُ)", "; ilk harfi olan vâv muzâride düşer (vadaa yadau)")),
  ENC_NOUN("مَتَاعَهَا", "mata-goods", "هَا", "maful", punct="،"), THUMMA(), SUBJ("تَرْجِعَ", "rajaa", "atf", punct=".")]})

S2.append({"id": "s5", "translation": {"en": "«All of that without a sailor and without anyone to manage it.»",
                                      "tr": "«Bütün bunlar, gemicisiz ve idare edensiz.»"},
 "tokens": [MUBTADA("كُلُّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", extra=["idafa-definiteness"]),
  BILA(), BILA_N("مَلَّاحٍ", "mallah", ("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the jarr phrase is the predicate, in the seat of raf'", "; câr-mecrûr mübtedânın haberi, mahallen merfû"), extra=["mubtada-khabar"]),
  WA_LA_ZAIDA(),
  ATF("مُدَبِّرٍ", "mudabbir", "noun", "jarr", ["ism-fail"], note_ar=" عَلَى «مَلَّاحٍ» — اسْمُ فَاعِلٍ مِنْ دَبَّرَ", note_en=" — on «a sailor»; the active participle of «to manage»", note_tr=" — «gemici»ye; debbera'nın ism-i fâili", punct=".")]})

S2.append({"id": "s6", "translation": {"en": "«Can reason allow this?»", "tr": "«Akıl buna izin verir mi?»"},
 "tokens": [tok("أَيَجُوزُ", "jaaza", "verb", ["al-istifham", "mudari-marfu", "hollow-verbs"],
    "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَيَجُوزُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ.",
    "The hamza asks the question; «is [it] allowed» is a present verb in raf'; its doer follows.", "İstifhâm hemzesi; «câiz olur mu» — merfû muzâri; fâili ondan sonra gelir.",
    segments=[seg("أَ", "hamza-istifham", "part"), seg("يَجُوزُ", "jaaza", "verb")]),
  HADHA("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", extra=["fail"]), FI(), MAJR("الْعَقْلِ", "aql", punct="؟")]})

S2.append({"id": "s7", "translation": {"en": "Then the Imam fell silent, waiting for their answer.", "tr": "Sonra İmam, cevaplarını bekleyerek sustu."},
 "tokens": [THUMMA(), MADI("سَكَتَ", "sakata"), FAIL("الْإِمَامُ", "imam"),
  MUDARI("يَنْتَظِرُ", "intazara", ["form-viii-verbs", "hal"], note_ar=HAL_CL[0], note_en=HAL_CL[1], note_tr=HAL_CL[2]),
  ENC_NOUN("جَوَابَهُمْ", "jawab", "هُمْ", "maful", punct=".")]})

# ================================================== Chapter 3 — الْجَوَابُ ==================================================
S3 = []
S3.append({"id": "s1", "translation": {"en": "When the men heard the question, they answered as one answers who has no doubt.",
                                      "tr": "Topluluk soruyu duyunca, hiç şüphe etmeyen birinin cevabı gibi cevap verdi."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI("سَمِعَ", "samia", note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), FAIL("الْقَوْمُ", "qawm"), MAFUL("الْمَسْأَلَةَ", "masala", punct="،"),
  VERB_WAW("أَجَابُوا", "ajaba", ["form-iv-verbs", "hollow-verbs"], note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  tok("جَوَابَ", "jawab", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "idafa-definiteness"],
    "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اسْمُ مَصْدَرٍ نَائِبٌ عَنِ الْإِجَابَةِ، مُبَيِّنٌ لِنَوْعِ الْإِجَابَةِ بِإِضَافَتِهِ.",
    "The absolute object (maf'ul mutlaq), in nasb and annexed — جَوَاب is a noun of the masdar standing in for إِجَابَة, and its annexation names the KIND of answering.",
    "Mef'ûlün mutlak, mansûb, muzâf — icâbe yerine geçen ism-i masdar; izâfetiyle cevap vermenin nev'ini beyan eder."),
  tok("مَنْ", "man-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A relative noun «one who», built on sukun, in the seat of jarr as the second term of the idafa.", "İsm-i mevsûl «… kimse», sükûn üzere mebnî, muzâfun ileyh olarak mahallen mecrûr."),
  LA_NAFIYA(), MUDARI("يَشُكُّ", "shakka", ["doubled-verbs"], punct=".", note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2])]})

S3.append({"id": "s2", "translation": {"en": "They said: «This is a thing that reason does not accept and that no man of sense would believe.»",
                                      "tr": "Dediler: «Bu, aklın kabul etmediği, hiçbir akıl sahibinin de doğrulamayacağı bir şeydir.»"},
 "tokens": [VERB_WAW("قَالُوا", "qala", ["hollow-verbs", "maful-bihi"], punct=":", note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]),
  HADHA("رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "merfû — mübtedâ", extra=["mubtada-khabar"]), KHABAR("شَيْءٌ", "shay"), LA_NAFIYA(),
  MUD_ENC_DF("يَقْبَلُهُ", "qabila", "هُ", ["jumla-sifa"], note=(" — وَالْهَاءُ عَائِدٌ عَلَى «شَيْءٌ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لَهُ", "; the pronoun returns to «a thing», and the clause is its na't, in the seat of raf'", "; zamir «şey»e döner; cümle onun na'tı, mahallen merfû")),
  FAIL("الْعَقْلُ", "aql", punct="،"), WA_LA_NAFIYA(),
  MUD_ENC_DF("يُصَدِّقُهُ", "saddaqa", "هُ", ["form-ii-verbs", "atf-nasaq"], note=(" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ النَّعْتِ", "; the clause is conjoined to the na't clause", "; cümle na't cümlesine ma'tûf")),
  FAIL("عَاقِلٌ", "aqil", extra=["ism-fail"], punct=".")]})

S3.append({"id": "s3", "translation": {"en": "«If a man told us of it, we would say: he is a liar.»", "tr": "«Bir adam bize bunu anlatsaydı, derdik ki: O yalancıdır.»"},
 "tokens": [LAW(),
  ENC_MADI("حَدَّثَنَا", "haddatha", "نَا", ["form-ii-verbs", "al-majzum-wal-shart-wal-jaza"], note_ar=" مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِعْلُ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ",
    note_en=", placed before the doer, which follows — the clause is the condition and has no seat", note_tr=", fâilden önce; fâili sonra gelir — cümle şart cümlesidir, i'râbdan mahalli yoktur"),
  BIHI(), FAIL("رَجُلٌ", "rajul"),
  tok("لَقُلْنَا", "qala", "verb", ["al-majzum-wal-shart-wal-jaza", "hollow-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
    "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَقُلْنَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ جَوَابُ لَوْ لَا مَحَلَّ لَهَا" + MAQUL[0] + ".",
    "The lam opens the answer of لَوْ; «we said» is a past verb built on sukun before the attached «we» (its middle letter dropped where two quiescents met), and نَا is its doer in the seat of raf' — the clause answers لَوْ and has no seat" + MAQUL[1] + ".",
    "Lâm, lev'in cevabına gelmiştir; «derdik» — «biz» zamiri bitiştiği için sükûn üzere mebnî mâzî (iki sâkin karşılaşınca aynı düştü); nâ fâil, mahallen merfû — cümle lev'in cevabıdır, mahalli yoktur" + MAQUL[2] + ".",
    punct=":", segments=[seg("لَ", "lam-jawab", "part"), seg("قُلْ", "qala", "verb"), seg("نَا", "pron-1p", "pron")]),
  tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna", "al-bariz-al-muttasil"],
    "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَكُسِرَتْ هَمْزَتُهَا لِأَنَّهَا فِي أَوَّلِ مَقُولِ الْقَوْلِ.",
    "إِنَّ «truly» with the attached «he» as its noun, in the seat of nasb — its hamza takes kasra because it opens the words that are said.",
    "İnne; bitişik «o» zamiri ismi, mahallen mansûb — söylenen sözün başında olduğu için hemzesi meksûrdur.",
    segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")]),
  KHABAR_INNA("كَاذِبٌ", "kadhib-liar", ["ism-fail"], punct=".", note=(" — اسْمُ فَاعِلٍ مِنْ كَذَبَ", " — the active participle of «to lie»", " — kezebe'nin ism-i fâili"))]})

S3.append({"id": "s4", "translation": {"en": "The Imam said: «Glory be to God!»", "tr": "İmam dedi: «Sübhânallah!»"},
 "tokens": [MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), FAIL("الْإِمَامُ", "imam", punct=":"),
  tok("سُبْحَانَ", "subhan", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "idafa-definiteness", "hadhf-wa-taqdir"],
    "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: أُسَبِّحُ، مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَهُوَ اسْمُ مَصْدَرٍ لَازِمٌ لِلنَّصْبِ وَالْإِضَافَةِ.",
    "The absolute object of an omitted verb («I glorify»), in nasb and annexed — a noun of the masdar that is always in nasb and always annexed.",
    "Hazfedilmiş bir fiilin («tesbih ederim») mef'ûlün mutlakı, mansûb, muzâf — daima mansûb ve muzâf olan ism-i masdar."),
  ALLAH_MI(punct="!")]})

S3.append({"id": "s5", "translation": {"en": "«If reason will not accept that one ship should run without a sailor, how can it accept that this whole world should run without a Maker?»",
                                      "tr": "«Akıl tek bir geminin gemicisiz yürümesini kabul etmiyorsa, bütün bu âlemin bir Yaratıcı olmadan yürümesini nasıl kabul eder?»"},
 "tokens": [IN_SHART("إِنْ"),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "in-shartiyya"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
    "كَانَ, the defective past verb built on fatha, in the seat of jazm as the verb of the condition: it raises its noun and puts its predicate in nasb.",
    "Kâne: fetha üzere mebnî nâkıs mâzî, şart fiili olarak mahallen meczûm; ismini ref, haberini nasb eder."),
  ISMK("الْعَقْلُ", "aql"), LA_NAFIYA(), MUDARI_KH("يَقْبَلُ", "qabila"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَقْبَلُ»", "; the clause it builds is the object of «accepts»", "; kurduğu müevvel masdar «kabul eder»in mef'ûlü"),
  SUBJ("تَجْرِيَ", "jara", "an", ["naqis-verbs"], who=None, ya=True), FAIL("سَفِينَةٌ", "safina"), NAAT("وَاحِدَةٌ", "wahid", "raf"),
  BILA(), BILA_N("مَلَّاحٍ", "mallah", ("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«تَجْرِيَ»", "; the jarr phrase attaches to «run»", "; câr-mecrûr «yürümesi»ne müteallik"), punct="،"),
  tok("فَكَيْفَ", "kayfa", "noun", ["al-fa-fi-jawab-al-shart", "al-istifham", "khuruj-al-istifham", "hal"],
    "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَكَيْفَ اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ — وَالِاسْتِفْهَامُ لِلْإِنْكَارِ.",
    "The fa binds the answer of the condition (an answer that is a question must take it); كَيْفَ «how?» is an interrogative noun built on fatha, in the seat of nasb as a hal — and the question denies.",
    "Fâ şartın cevabını bağlar; keyfe «nasıl?» — istifhâm ismi, fetha üzere mebnî, hâl olarak mahallen mansûb — istifhâm inkâr içindir.",
    segments=[seg("فَ", "fa", "conj"), seg("كَيْفَ", "kayfa", "noun")]),
  MUDARI("يَقْبَلُ", "qabila", ["al-majzum-wal-shart-wal-jaza"], note_ar=" — وَجُمْلَةُ «فَكَيْفَ يَقْبَلُ…» فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ",
    note_en="; the clause «then how does it accept…» fills the seat of jazm as the answer of the condition", note_tr="; «nasıl kabul eder…» cümlesi şartın cevabı olarak mahallen meczûm"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ", "; the clause it builds is the object", "; kurduğu müevvel masdar mef'ûlün bih"),
  SUBJ("يَجْرِيَ", "jara", "an", ["naqis-verbs"], who=None, ya=True),
  HADHA("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", extra=["fail"]), BADAL("الْعَالَمُ", "alam", "raf"),
  tok("كُلُّهُ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
    "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A tawkid of meaning «the whole of it», in raf' like the doer it strengthens; annexed to the pronoun, which fills the seat of jarr.",
    "Ma'nevî te'kîd «tamamı», pekiştirdiği fâil gibi merfû; zamire muzâf, zamir mahallen mecrûr.", segments=[seg("كُلُّ", "kull", "noun"), seg("هُ", "pron-3ms", "pron")]),
  BILA(), BILA_N("صَانِعٍ", "sani", ("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَجْرِيَ»", "; the jarr phrase attaches to «run»", "; câr-mecrûr «yürümesi»ne müteallik"), extra=["ism-fail"], punct="؟")]})

S3.append({"id": "s6", "translation": {"en": "«Is not this world greater than the ship in standing, and richer than it in changing states?»",
                                      "tr": "«Bu âlem, şan bakımından gemiden daha büyük, hâller bakımından ondan daha çeşitli değil mi?»"},
 "tokens": [tok("أَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-istifham", "khuruj-al-istifham"],
    "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
    "The hamza asks a question that expects assent («is it not…?»); لَيْسَ is the frozen defective verb built on fatha: it raises its noun and puts its predicate in nasb.",
    "Takrîrî istifhâm hemzesi («… değil mi?»); leyse: fetha üzere mebnî câmid nâkıs mâzî; ismini ref, haberini nasb eder.",
    segments=[seg("أَ", "hamza-istifham", "part"), seg("لَيْسَ", "laysa", "verb")]),
  HADHA("رَفْعٍ اسْمُ لَيْسَ", "raf' as the noun of لَيْسَ", "merfû — leyse'nin ismi", extra=["kana-wa-akhawatuha"]), BADAL("الْعَالَمُ", "alam", "raf"),
  tok("أَعْظَمَ", "azam", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"], "خَبَرُ لَيْسَ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ.",
    "The predicate of لَيْسَ, in nasb — an elative, barred from tanwin as an adjective on the pattern of a verb.", "Leyse'nin haberi, mansûb — vasfiyyet ve fiil vezni sebebiyle gayr-i munsarif ism-i tafdîl."),
  MINA(), MAJR("السَّفِينَةِ", "safina"), TAMYIZ_T("شَأْنًا", "shan", *TAFDIL_TAMYIZ, punct="،"),
  tok("وَأَكْثَرَ", "akthar", "noun", ["atf-nasaq", "kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf"],
    WA_AR + "أَكْثَرَ مَعْطُوفٌ عَلَى «أَعْظَمَ» مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ.",
    "The waw conjoins; «more» is conjoined to «greater», in nasb — an elative barred from tanwin.", "Vâv atıf; «daha çok», «daha büyük»e ma'tûf, mansûb — gayr-i munsarif ism-i tafdîl.",
    segments=[seg("وَ", "wa", "conj"), seg("أَكْثَرَ", "akthar", "noun")]),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)"), TAMYIZ_T("أَحْوَالًا", "ahwal", *TAFDIL_TAMYIZ, punct="؟")]})

S3.append({"id": "s7", "translation": {"en": "«Can that be, except by a wise Maker?»", "tr": "«Bu, hikmet sahibi bir Yaratıcı olmadan olabilir mi?»"},
 "tokens": [tok("فَهَلْ", "hal-istifham", "part", ["al-istifham", "khuruj-al-istifham"], FA_AR + "هَلْ حَرْفُ اسْتِفْهَامٍ خَرَجَ إِلَى مَعْنَى النَّفْيِ، فَجَازَ بَعْدَهُ «إِلَّا».",
    "The fa conjoins; هَلْ asks, but the question has turned into a denial — which is why إِلَّا can follow it.", "Fâ atıf; hel istifhâm harfidir, burada nefiy mânâsına çıkmıştır; bu yüzden ardından illâ gelebilir.",
    segments=[seg("فَ", "fa", "conj"), seg("هَلْ", "hal-istifham", "part")]),
  tok("يَكُونُ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
    "The present of كَانَ, in raf': it raises its noun and puts its predicate in nasb.", "Kâne'nin muzârisi, merfû: ismini ref, haberini nasb eder."),
  DHALIKA("رَفْعٍ اسْمُ يَكُونُ", "raf' as the noun of يَكُونُ", "merfû — yekûnu'nun ismi", extra=["kana-wa-akhawatuha"]),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"], "أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ لِأَنَّ الِاسْتِفْهَامَ بِمَعْنَى النَّفْيِ، فَمَا بَعْدَهَا يَأْخُذُ إِعْرَابَهُ مِنْ مَوْقِعِهِ.",
    "إِلَّا «except» governs nothing here: the exception is «emptied» (mufarragh), because the question stands for a negation — what follows takes the case its own position demands.",
    "İllâ burada amel etmez; istifhâm nefiy mânâsında olduğu için istisnâ müferrağdır — sonrası i'râbını kendi mevkiinden alır."),
  BI_NOUN("بِصَانِعٍ", "sani", "صَانِعٍ", extra=["ism-fail", "kana-wa-akhawatuha"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُونُ", note_en="; the jarr phrase is the predicate of يَكُونُ, in the seat of nasb", note_tr="; câr-mecrûr yekûnu'nun haberi, mahallen mansûb"),
  NAAT("حَكِيمٍ", "hakim", "jarr", ["sifa-mushabbaha"], punct="؟")]})

# ============================================== Chapter 4 — بَعْدَ الْمُنَاظَرَةِ ==============================================
S4 = []
S4.append({"id": "s1", "translation": {"en": "The men fell into a long silence, and they looked at one another in bewilderment.",
                                      "tr": "Topluluk uzun bir süre sustu; şaşkınlıktan birbirlerine baktılar."},
 "tokens": [MADI("فَسَكَتَ", "sakata"), FAIL("الْقَوْمُ", "qawm"), MUTLAQ_NAW("سُكُوتًا", "sukut", "سَكَتَ", "fell silent", "sustu"), NAAT("طَوِيلًا", "tawil-long", "nasb", ["sifa-mushabbaha"], punct="،"),
  MADI("وَنَظَرَ", "nazara"), ENC_NOUN("بَعْضُهُمْ", "bad", "هُمْ", "fail"), ILA(), MAJR("بَعْضٍ", "bad"),
  LIAJLIH("حَيْرَةً", "hayra", "النَّظَرِ", "their looking", "bakışın", punct=".")]})

S4.append({"id": "s2", "translation": {"en": "Not one of them was able to answer him back with a single word.", "tr": "İçlerinden hiçbiri ona tek bir kelimeyle karşılık veremedi."},
 "tokens": [WA_LAM(), JAZM_V("يَسْتَطِعْ", "istataa", ["form-x-verbs", "hollow-verbs"], note_ar=" — وَحُذِفَتِ الْيَاءُ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the ya of the hollow root drops where two quiescents meet", note_tr=" — iki sâkin karşılaşınca yâ düştü"),
  FAIL("أَحَدٌ", "ahad"), JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", note_ar=JAR_NAAT("raf", "أَحَدٌ", "one", "kimse")[0], note_en=JAR_NAAT("raf", "أَحَدٌ", "one", "kimse")[1], note_tr=JAR_NAAT("raf", "أَحَدٌ", "one", "kimse")[2]), AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَسْتَطِعْ»", "; the clause it builds is the object of «was able»", "; kurduğu müevvel masdar «gücü yetti»nin mef'ûlü"),
  SUBJ("يَرُدَّ", "radda", "an", ["doubled-verbs"], who="هُوَ"), ALAYHI(), BI_NOUN("بِكَلِمَةٍ", "kalima", "كَلِمَةٍ", punct=".")]})

S4.append({"id": "s3", "translation": {"en": "Some versions of the report add that they repented and turned back from what they had held.", "tr": "Bazı rivayetlerde, onların tevbe edip sözlerinden döndükleri de vardır."},
 "tokens": [PREP("وَفِي", "fi", gloss_tr="«-de»"), MAJR("بَعْضِ", "bad", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الرِّوَايَاتِ", "riwaya", extra=["jam-muannath-salim"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ", note_en=" — the jarr phrase is the FRONTED predicate", note_tr=" — câr-mecrûr öne alınmış haberdir"),
  tok("أَنَّهُمْ", "anna", "part", ["inna-wa-akhawatuha", "inna-am-anna", "mawadi-fath-anna", "mubtada-khabar", "al-bariz-al-muttasil"],
    "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ (تَوْبَتُهُمْ) فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
    "أَنَّ «that» builds a masdar; the attached «they» is its noun in the seat of nasb — the masdar it builds («their repenting») is the mubtada, placed after its predicate, in the seat of raf'.",
    "Enne masdar kurar; bitişik «onlar» ismi, mahallen mansûb — kurduğu müevvel masdar («tevbeleri») haberinden sonra gelen mübtedâ, mahallen merfû.",
    segments=[seg("أَنَّ", "anna", "part"), seg("هُمْ", "pron-3mp", "pron")]),
  VERB_WAW("تَابُوا", "taba-repent", ["hollow-verbs"], punct="،", note_ar=KH_ANNA[0], note_en=KH_ANNA[1], note_tr=KH_ANNA[2]),
  VERB_WAW("وَرَجَعُوا", "rajaa", ["atf-nasaq"], note_ar=" — مَعْطُوفٌ عَلَى «تَابُوا»", note_en=" — conjoined to «they repented»", note_tr=" — «tevbe ettiler»e ma'tûf"),
  AN_PREP(), ENC_NOUN("قَوْلِهِمْ", "qawl", "هِمْ", "majr", punct=".")]})

S4.append({"id": "s4", "translation": {"en": "This report became an example which the scholars mention in the books of creed.", "tr": "Bu haber, âlimlerin akâid kitaplarında andığı bir misal oldu."},
 "tokens": [SARA("وَصَارَ"), HADHA("رَفْعٍ اسْمُ صَارَ", "raf' as the noun of صَارَ", "merfû — sâra'nın ismi", extra=["kana-wa-akhawatuha"]), BADAL("الْخَبَرُ", "khabar", "raf"),
  tok("مَثَلًا", "mathal", "noun", ["kana-wa-akhawatuha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of صَارَ, in nasb.", "Sâra'nın haberi, mansûb."),
  MUD_ENC_DF("يَذْكُرُهُ", "dhakara", "هُ", ["jumla-sifa"], note=(" — وَالْهَاءُ عَائِدٌ عَلَى «مَثَلًا»، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لَهُ", "; the pronoun returns to «an example», and the clause is its na't, in the seat of nasb", "; zamir «misal»e döner; cümle onun na'tı, mahallen mansûb")),
  FAIL("الْعُلَمَاءُ", "alim-scholar", extra=["jam-taksir"], note_ar=" — جَمْعُ عَالِمٍ عَلَى فُعَلَاءَ", note_en=" — the plural of عَالِم on فُعَلَاء", note_tr=" — âlim'in fuʿalâ' veznindeki cem'i"),
  FI(), MAJR("كُتُبِ", "kitab", extra=["jam-taksir"], note_ar="، مُضَافٌ — جَمْعُ كِتَابٍ", note_en=", annexed — the plural of كِتَاب", note_tr=", muzâf — kitâb'ın cem'i"),
  MUDAF_ILAYH("الْعَقَائِدِ", "aqida", extra=["jam-taksir", "mamnu-min-sarf"], punct=".", note_ar=" — جَمْعُ عَقِيدَةٍ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُعَرَّفٌ بِأَلْ",
    note_en=" — the plural of عَقِيدَة; a diptote, it takes the kasra here because it carries ال", note_tr=" — akîde'nin cem'i; gayr-i munsarif iken el-takısı aldığı için kesre ile")]})

S4.append({"id": "s5", "translation": {"en": "And reason, if it will not accept a ship without a sailor, is all the further from accepting a world without a Maker.",
                                      "tr": "Akıl, gemicisiz bir gemiyi kabul etmezse, Yaratıcısız bir âlemi kabul etmekten elbette daha uzak olur."},
 "tokens": [WA_ISTINAF_T("وَالْعَقْلُ", "aql", "الْعَقْلُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ رَفْعٍ خَبَرُهُ.",
    "«reason» is the mubtada, in raf' — the condition and its answer together are its khabar, in the seat of raf'.", "«akıl» mübtedâ, merfû — şart ve cevap cümleleri birlikte haberi, mahallen merfû.", ["mubtada-khabar"]),
  tok("إِذَا", "idha", "noun", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، خَافِضٌ لِشَرْطِهِ مَنْصُوبٌ بِجَوَابِهِ.",
    "إِذَا «when, if»: an adverb of time with the force of a condition, built on sukun in the seat of nasb — annexed to its condition and governed by its answer.",
    "İzâ «-dığı zaman, -se»: şart mânâsı taşıyan zaman zarfı, sükûn üzere mebnî, mahallen mansûb; şartına muzâf, cevabıyla mansûb."),
  LAM_JAZM(), JAZM_V("يَقْبَلْ", "qabila", hidden="هُوَ", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا", note_en="; the clause fills the seat of jarr, annexed to إِذَا", note_tr="; cümle izâ'ya muzâfun ileyh olarak mahallen mecrûr"),
  MAFUL("سَفِينَةً", "safina"), BILA(), BILA_N("مَلَّاحٍ", "mallah", JAR_NAAT("nasb", "سَفِينَةً", "a ship", "gemi"), punct="،"),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "idha-shartiyya"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ جَوَابُ إِذَا لَا مَحَلَّ لَهَا.",
    "كَانَ is the defective past verb built on fatha; its noun is the hidden pronoun «it» — the clause is the answer of إِذَا and has no seat.",
    "Kâne: fetha üzere mebnî nâkıs mâzî; ismi gizli zamir «o» — cümle izâ'nın cevabıdır, mahalli yoktur."),
  KHK("أَبْعَدَ", "abad", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar=" — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", note_en=" — an elative «farther», barred from tanwin", note_tr=" — gayr-i munsarif ism-i tafdîl «daha uzak»"),
  MIN(), AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِمِنْ", "; the masdar it builds is in jarr after مِنْ", "; kurduğu müevvel masdar min ile mecrûr"),
  SUBJ("يَقْبَلَ", "qabila", "an", who="هُوَ"), MAFUL("عَالَمًا", "alam"),
  BILA(), BILA_N("صَانِعٍ", "sani", JAR_NAAT("nasb", "عَالَمًا", "a world", "âlem"), extra=["ism-fail"], punct=".")]})

S4.append({"id": "s6", "translation": {"en": "So a ship runs only by a sailor, and the world stands only by a Maker.", "tr": "Demek ki gemi ancak bir gemiciyle yürür, âlem de ancak bir Yaratıcıyla ayakta durur."},
 "tokens": [tok("فَالسَّفِينَةُ", "safina", "noun", ["mubtada-khabar"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَالسَّفِينَةُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
    "The fa opens a new sentence that draws the conclusion; «the ship» is the mubtada, in raf'.", "Fâ isti'nâf içindir, sonucu bağlar; «gemi» mübtedâ, merfû.", segments=[seg("فَ", "fa", "conj"), seg("السَّفِينَةُ", "safina", "noun")]),
  LA_NAFIYA(), MUDARI("تَجْرِي", "jara", ["naqis-verbs"], who="هِيَ", naqis="ي", note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]), ILLA(),
  BI_NOUN("بِمَلَّاحٍ", "mallah", "مَلَّاحٍ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«تَجْرِي»", note_en="; the jarr phrase attaches to «runs»", note_tr="; câr-mecrûr «yürür»e müteallik", punct="،"),
  tok("وَالْعَالَمُ", "alam", "noun", ["mubtada-khabar", "atf-nasaq"], WA_AR + "الْعَالَمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins a second sentence; «the world» is the mubtada, in raf'.", "Vâv ikinci cümleyi bağlar; «âlem» mübtedâ, merfû.",
    segments=[seg("وَ", "wa", "conj"), seg("الْعَالَمُ", "alam", "noun")]),
  LA_NAFIYA(), MUDARI("يَقُومُ", "qama", ["hollow-verbs"], note_ar=KH_CL[0], note_en=KH_CL[1], note_tr=KH_CL[2]), ILLA(),
  BI_NOUN("بِصَانِعٍ", "sani", "صَانِعٍ", extra=["ism-fail"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«يَقُومُ»", note_en="; the jarr phrase attaches to «stands»", note_tr="; câr-mecrûr «ayakta durur»a müteallik", punct=".")]})

S4.append({"id": "s7", "translation": {"en": "And people have never ceased to relate this report, down to this day.", "tr": "İnsanlar bu haberi bugüne kadar anlatmaya devam etmektedir."},
 "tokens": [WA_ISTINAF_T("وَمَا", "ma-nafiya", "مَا حَرْفُ نَفْيٍ.", "مَا negates the verb after it.", "mâ nefiy harfi.", ["la-nafiya"], pos="part"),
  tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ.",
    "زَالَ is a defective past verb, a sister of كَانَ, built on fatha: it raises its noun and puts its predicate in nasb — after a negation it means «never ceased».",
    "Zâle: kâne'nin kardeşlerinden, fetha üzere mebnî nâkıs mâzî; ismini ref, haberini nasb eder — nefiyle birlikte devamlılık bildirir."),
  tok("النَّاسُ", "nas", "noun", ["kana-wa-akhawatuha"], "اسْمُ زَالَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of زَالَ, in raf'.", "Zâle'nin ismi, merfû."),
  MUDARI5("يَرْوُونَ", "rawa", extra=["naqis-verbs", "kana-wa-akhawatuha"], note_ar=" — وَحُذِفَتْ لَامُهُ (الْيَاءُ) لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ",
    note_en=" — its last radical, the ya, dropped where two quiescents met; the clause is the predicate of زَالَ, in the seat of nasb", note_tr=" — lâm'ı (yâ) iki sâkin karşılaşınca düştü; cümle zâle'nin haberi, mahallen mansûb"),
  HADHA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", extra=["maful-bihi"]), BADAL("الْخَبَرَ", "khabar", "nasb"), ILA(), MAJR("الْيَوْمِ", "yawm", punct=".")]})

CHAPS = [S1, S2, S3, S4]

# ---- the lexicon: every key by lemma identity from the shelf (the majority reading of a key wins); five nouns are new ----
PKGS = sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PKGS}
_M = {p: (json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
          if (ROOT / "content/samples" / p / "morphology.json").exists() else {}) for p in PKGS}
DIA = re.compile("[ً-ٰ]")
def _lemma_id(e): return DIA.sub("", unicodedata.normalize("NFC", e.get("lemma", "")))
def find_entry(k):
    """(gloss entry, owning package) — the reading of the key that most packages hold; ties go to the alphabetical first"""
    holders = [(p, _G[p][k]) for p in PKGS if k in _G[p]]
    if not holders: return None, None
    votes = collections.Counter(_lemma_id(e) for p, e in holders)
    best = votes.most_common(1)[0][0]
    group = [(p, e) for p, e in holders if _lemma_id(e) == best]
    if group[0][1].get("pos") == "verb":
        for p, e in group:
            if k in _M[p]: return e, p
    return group[0][1], group[0][0]

NEW_GLOSS = {
 "manqaba": {"lemma": "مَنْقَبَة", "root": "ن ق ب", "pos": "noun", "plural": "مَنَاقِب", "gloss": {"en": "a merit, a noble trait; (pl. مَنَاقِب) a book of a man's virtues and deeds", "tr": "menkabe, fazilet; (çoğ. menâkıb) bir zâtın faziletlerini anlatan kitap"}, "level": 5},
 "dahriyya": {"lemma": "دَهْرِيَّة", "root": "د ه ر", "pos": "noun", "gloss": {"en": "the Dahriyya — those who deny a Maker and ascribe all things to time (dahr)", "tr": "Dehriyye — Yaratıcıyı inkâr edip her şeyi zamana (dehr) bağlayanlar"}, "level": 5},
 "mallah": {"lemma": "مَلَّاح", "root": "م ل ح", "pos": "noun", "plural": "مَلَّاحُونَ", "gloss": {"en": "a sailor, a seaman (فَعَّال of a trade)", "tr": "gemici, denizci (meslek bildiren fa''âl)"}, "level": 5},
 "munazara": {"lemma": "مُنَاظَرَة", "root": "ن ظ ر", "pos": "noun", "gloss": {"en": "a debate, a disputation (masdar of Form III نَاظَرَ)", "tr": "münazara, tartışma (nâzara'nın masdarı)"}, "level": 5},
 "hayra": {"lemma": "حَيْرَة", "root": "ح ي ر", "pos": "noun", "gloss": {"en": "bewilderment, perplexity (masdar of حَارَ يَحَارُ)", "tr": "hayret, şaşkınlık (hâra yehâru'nun masdarı)"}, "level": 5},
}
used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, ORIGIN, missing = {}, {}, []
for k in sorted(used):
    if k in NEW_GLOSS:
        assert all(k not in _G[p] for p in PKGS), "a key is a global claim — " + k + " is already taken"
        GLOSS[k] = NEW_GLOSS[k]; continue
    e, p = find_entry(k)
    if e is None: missing.append(k)
    else: GLOSS[k], ORIGIN[k] = e, p
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
 "title": {"ar": "أَبُو حَنِيفَةَ وَالسَّفِينَةُ", "en": "Abu Hanifa and the Ship", "tr": "Ebû Hanîfe ve Gemi"},
 "subtitle": {"ar": "مُنَاظَرَةُ الْإِمَامِ لِقَوْمٍ أَنْكَرُوا الصَّانِعَ، وَسُؤَالُهُ عَنْ سَفِينَةٍ تَجْرِي بِلَا مَلَّاحٍ — قِصَّةٌ لِلْمُسْتَوَى الْخَامِسِ",
              "en": "The Imam's debate with men who denied the Maker, and his question about a ship that sails with no sailor — a story for the fifth level",
              "tr": "İmamın Yaratıcıyı inkâr edenlerle münazarası ve gemicisiz yüzen gemi sorusu — beşinci seviye için bir hikâye"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى الْخَامِسُ) لِخَبَرِ مُنَاظَرَةِ الْإِمَامِ أَبِي حَنِيفَةَ لِلدَّهْرِيَّةِ وَسُؤَالِهِ عَنِ السَّفِينَةِ الَّتِي تَجْرِي بِلَا مَلَّاحٍ، كَمَا تَرْوِيهِ كُتُبُ الْمَنَاقِبِ الْحَنَفِيَّةِ (الْمُوَفَّقُ الْمَكِّيُّ، وَابْنُ الْبَزَّازِ الْكَرْدَرِيُّ) وَشُرُوحُ الْعَقَائِدِ بَعْدَهَا. النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ هِيَ نَصُّ مَصْدَرٍ، وَلَا آيَةٌ وَلَا حَدِيثٌ؛ وَالْحِوَارُ حِكَايَةٌ بِالْمَعْنَى لَا بِاللَّفْظِ.",
  "en": "ORIGINAL Level-5 graded Arabic: the report of Imam Abu Hanifa's debate with the Dahriyya, the deniers of the Maker, and his question about a ship that crosses the sea with no sailor — told in the Hanafi manaqib (al-Muwaffaq al-Makki's and Ibn al-Bazzaz al-Kardari's Manaqib Abi Hanifa) and in later creed commentaries — RETOLD FREELY as a retelling. No sentence is a quotation of any source; no verse and no hadith text is quoted; the dialogue is narrative paraphrase, not a recorded wording, and none of it may be cited as the Imam's words. Only the well-attested core is kept: the details on which the versions differ (drawn swords and a threat on his life, the late-arrival variant with the self-building boat) are left out, and the repentance is given as what some versions add.",
  "tr": "ÖZGÜN 5. seviye Arapça: İmam Ebû Hanîfe'nin Yaratıcıyı inkâr eden Dehriyye ile münazarası ve gemicisiz denizi geçen gemi sorusu — Hanefî menâkıb kitaplarında (el-Muvaffak el-Mekkî ve İbnü'l-Bezzâz el-Kerderî'nin Menâkıbu Ebî Hanîfe'leri) ve sonraki akâid şerhlerinde anlatılan haber — SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bir kaynaktan alıntı değildir; hiçbir âyet ve hadis metni aktarılmamıştır; diyaloglar sözlü bir kayıt değil, mânâ ile anlatımdır ve hiçbiri İmam'ın sözü olarak nakledilemez. Yalnız sağlam çekirdek korunmuştur: rivayetlerin ayrıştığı ayrıntılar (çekilen kılıçlar ve hayatına kastedilmesi, kendiliğinden yapılan kayıkla geç gelme rivayeti) çıkarılmış, tevbe ise bazı rivayetlerin eklediği bir husus olarak verilmiştir.",
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
