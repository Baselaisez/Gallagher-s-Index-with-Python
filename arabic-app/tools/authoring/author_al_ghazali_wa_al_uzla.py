"""Author content/samples/al-ghazali-wa-al-uzla — «الْغَزَالِيُّ وَالْعُزْلَةُ», an ORIGINAL historical story at Level 6 (Master).

ORIGINAL graded Arabic in a classical narrative register, kept to the well-attested core of Abū Ḥāmid al-Ghazālī's own
account of his crisis and return in al-Munqidh min al-ḍalāl, with the closing years as the biographers give them (ʿAbd
al-Ghāfir al-Fārisī by way of Ibn ʿAsākir's Tabyīn kadhib al-muftarī; al-Subkī, Ṭabaqāt al-Shāfiʿiyya al-kubrā; Ibn
Khallikān, Wafayāt al-aʿyān): the celebrated teacher of the Niẓāmiyya in Baghdad, with standing and wealth; his heart not
at rest in what he knew, for he sought a knowledge no doubt survives; his search through the ways of the seekers of his
time — kalām, the philosophers, the Bāṭiniyya, then the ṣūfīs, whose way he learns is completed only by knowledge joined
to action; his examination of his own intention in teaching; months of wavering; his tongue held back from teaching and
his strength gone, the physicians unable to cure him, the sickness in his heart; his turning to his Lord; his leaving
Baghdad in 488 AH, giving away his wealth but for what would suffice him; Syria (Damascus, Jerusalem) and the Ḥijāz and the
pilgrimage; about ten years of solitude; his return to teaching at Nīshāpūr, no longer as he had left; his retiring to his
home town (Ṭūs), keeping to his house in worship and teaching until he died there. The story closes on a reflection on
knowledge joined to action.

The account is RETOLD FREELY — no sentence is a quotation from al-Munqidh or from any of the biographers, no āya or ḥadīth is
quoted, and no words are put in al-Ghazālī's mouth (his inner states are told in the narrator's words). Left out on purpose:
the exact length of each stay (Damascus, Jerusalem, Hebron), the stories of meetings on the journey, the minaret of the
Umayyad mosque, the months and the day of the crisis, the arrangements for his family, the vizier who called him back to
Nīshāpūr, the khānqāh and the madrasa by his house, the date of his death, and every disputed anecdote. Ṭūs is not named:
it is «بَلَدُهُ», his home town. Nīshāpūr is named (نَيْسَابُور, a diptote: a foreign proper name), its vowelling as Yāqūt
gives it (بِفَتْحِ أَوَّلِهِ) — listed for the scholar's review with the nisba below.

NAMES. أَبُو حَامِدٍ: a kunya — أَبُو takes the case of its seat by the five-nouns' letters, حَامِدٍ is a fully declined
name. الْغَزَالِيّ: a nisba become his name, read here in its best-known vowelling with a light zāy; the iʿrāb line and the
glossary say that some read it with a doubled zāy (الْغَزَّالِيّ) — the khilāf is taught as a khilāf and listed for review.

Five chapters, thirty sentences. The Level-6 constructions: long periodic sentences (ch2 s2, ch4 s6, ch5 s3); فَبَيْنَمَا …
إِذْ … (ch3 s2); ثُمَّ إِنَّهُ (ch2 s1, ch4 s1); ḥaṣr by إِنَّمَا (ch1 s5; ch3 s4, closed by لَا الْعَاطِفَةُ) and by negation
+ إِلَّا (ch2 s4, ch3 s3, ch4 s2, ch5 s6, ch5 s7), the restricted term always last; كَمِ الْخَبَرِيَّةُ (ch1 s2); the oath
لَعَمْرِي answered by لَقَدْ (ch5 s4); أَمَّا … فَـ twice (ch2 s5); لَا النَّافِيَةُ لِلْجِنْسِ after a pronoun of the matter
(ch3 s5); وَجَدَ with two objects and a number phrase (ch2 s1); the date as a compound number (ch4 s1); نَحْوَ standing in for
an adverb of time (ch4 s5); the wāw of ḥāl before a nominal clause and before قَدْ (ch5 s2); لَمَّا; حَتَّى of ibtidāʾ;
the passive (أُمْسِكَ); مِنْ قَبْلُ cut from its annexation; كَانَ and صَارَ with a hidden noun and a verbal predicate.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf, every verb's paradigm is
the shelf's own (no new verb), and the new entries are only those in NEW_GLOSS. Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_al_ghazali_wa_al_uzla.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "al-ghazali-wa-al-uzla"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)

PRON.update({"هُمُ": "pron-3mp", "هِمُ": "pron-3mp", "هِمْ": "pron-3mp", "هُمْ": "pron-3mp", "هُمَا": "pron-3d", "هِمَا": "pron-3d", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "ي": "pron-1s"})
PRON_AR.update({"هُمُ": "هُمْ", "هِمُ": "هُمْ", "هِمْ": "هُمْ", "هُمْ": "هُمْ", "هُمَا": "هُمَا", "هِمَا": "هُمَا", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "ي": "الْيَاءُ"})

N = lambda s: unicodedata.normalize("NFC", s)
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
def W(t3, *more):
    """join note triples into the kit's note_ar / note_en / note_tr"""
    out = list(t3)
    for m in more:
        out = [a + b for a, b in zip(out, m)]
    return dict(note_ar=out[0], note_en=out[1], note_tr=out[2])

MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
KH_KANA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
KH_SARA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ صَارَ", "; the clause fills the seat of nasb as the predicate of صَارَ", "; cümle sâra'nın haberi olarak mahallen mansûb")
KH_INNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi olarak mahallen merfû")
KH_ANNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", "; the clause fills the seat of raf' as the predicate of أَنَّ", "; cümle enne'nin haberi olarak mahallen merfû")
KH_LAKIN_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَكِنَّ", "; the clause fills the seat of raf' as the predicate of لَكِنَّ", "; cümle lâkinne'nin haberi olarak mahallen merfû")
KH_MUB_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", "; the clause is the predicate of the mubtada, in the seat of raf'", "; cümle mübtedânın haberi, mahallen merfû")
HALCL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause is a hal, in the seat of nasb", "; cümle hâl olarak mahallen mansûb")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
KH_KAM = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَمْ", "; the clause is the khabar of كَمْ, in the seat of raf'", "; cümle kem'in haberi, mahallen merfû")
ATF_CL = (" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "; the clause is conjoined to the one before it", "; cümle öncekine ma'tûftur")
HID_G = ("، يَعُودُ عَلَى الْغَزَالِيِّ", " (al-Ghazālī)", " (Gazzâlî)")
SADDA = lambda v_ar, v_en, v_tr: (" — وَأَنَّ وَمَا بَعْدَهَا فِي تَأْوِيلِ مَصْدَرٍ سَدَّ مَسَدَّ مَفْعُولَيْ «" + v_ar + "»",
                                  "; أَنَّ with its clause stands for a masdar that fills both objects of «" + v_en + "»",
                                  "; enne ve sonrası, «" + v_tr + "»in iki mef'ûlünün yerini tutan müevvel masdardır")
def NAAT_OF(n_ar, n_en, n_tr, case_ar="جَرٍّ"):
    """a jarr phrase hanging on an omitted adjective of a named indefinite noun"""
    return (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«" + n_ar + "»",
            "; the jarr phrase hangs on an omitted adjective of «" + n_en + "»",
            " — câr-mecrûr «" + n_tr + "»in mahzûf na'tına müteallik")

# ---- the names ----------------------------------------------------------------------------------------------------
ABU_ISMK = lambda: tok("أَبُو", "ab", "noun", ["kana-wa-akhawatuha", "five-nouns", "idafa-definiteness"],
    "اسْمُ كَانَ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ — وَأَبُو حَامِدٍ كُنْيَتُهُ.",
    "The noun of كَانَ, in raf' by the waw — one of the five nouns; annexed. «Abū Ḥāmid» is his kunya.",
    "Kâne'nin ismi, esmâ-i hamseden olduğu için vâv ile merfû; muzâf — «Ebû Hâmid» künyesidir.")
HAMID_MI = lambda: MUDAF_ILAYH("حَامِدٍ", "hamid", "propn", note_ar=" — عَلَمٌ مُنْصَرِفٌ، فَنُوِّنَ", note_en=" — a fully declined proper name, so it takes tanwin", note_tr=" — munsarif özel isim; bu yüzden tenvin alır")
GHAZALI_NAAT = lambda punct=None: tok("الْغَزَالِيُّ", "ghazali", "propn", ["naat-sifa", "ism-mansub"],
    "نَعْتٌ لِـ«أَبُو» مَرْفُوعٌ بِالضَّمَّةِ — نِسْبَةٌ صَارَتْ عَلَمًا عَلَيْهِ، وَالْمَشْهُورُ فِي ضَبْطِهَا تَخْفِيفُ الزَّايِ، وَبَعْضُهُمْ يُشَدِّدُهَا (الْغَزَّالِيُّ).",
    "An adjective of «Abū», in raf' — a nisba that became his name; its best-known vowelling has a light zāy, and some double it (al-Ghazzālī).",
    "«Ebû»nun na'tı, merfû — onun adı olmuş bir nisbe; meşhur zabtında zâ şeddesizdir, bazıları şeddeli okur (el-Gazzâlî).", punct=punct)
DIPT_TOWN = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town), barred from tanwin", " — müennes özel isim (şehir adı), gayr-i munsarif")
BAGHDAD_J = lambda punct=None, note=("", "", ""): MAJR("بَغْدَادَ", "baghdad", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_TOWN[0] + note[0], note_en=" — by a fatha standing in for the kasra" + DIPT_TOWN[1] + note[1], note_tr=" — kesre yerine fetha ile" + DIPT_TOWN[2] + note[2], punct=punct)
def BI_TOWN(full, lex, stem, why, punct=None, note=("", "", "")):
    """بِبَغْدَادَ، بِدِمَشْقَ، بِنَيْسَابُورَ: the ba meaning «in» before a diptote town name"""
    return BI_NOUN(full, lex, stem, pos="propn", sign=FATHA_JARR, extra=["mamnu-min-sarf"],
        note_ar=why[0] + " — وَالْبَاءُ بِمَعْنَى «فِي»" + note[0], note_en=" — by a fatha standing in for the kasra" + why[1] + "; the ba here means «in»" + note[1],
        note_tr=" — kesre yerine fetha ile" + why[2] + "; bâ burada «fî» anlamındadır" + note[2], punct=punct)
AJAM_TOWN = ("، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ", " — a foreign proper name (a town), barred from tanwin by ʿalamiyya + ʿujma", " — yabancı özel isim (şehir adı), alemiyet ve ucmet sebebiyle gayr-i munsarif")

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
def WA_MA(pre="istinaf"):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "«ve» + "}[pre]
    return tok("وَمَا", "ma-nafiya", "part", ["la-nafiya"], pre_ar + "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", pre_en + "مَا negates and governs nothing.", pre_tr + "mâ nefiy harfi, amel etmez.",
        segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")])
def ZARF_ENC(full, lex, enc, kind="مَكَانٍ", kind_en="place", kind_tr="mekân", punct=None, note_ar="", note_en="", note_tr=""):
    """عِنْدَهُ، مَعَهُ، وَرَاءَهُ: a ẓarf annexed to its pronoun"""
    return tok(full, lex, "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
        "ظَرْفُ " + kind + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        "An adverb of " + kind_en + ", in nasb and annexed to the attached pronoun, which fills the seat of jarr" + note_en + ".",
        kind_tr + " zarfı, mansûb, bitişik zamire muzâf; zamir mahallen mecrûr" + note_tr + ".", punct=punct,
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
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
def YAKUN(note=("", "", "")):
    return tok("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "lam-jazim", "hollow-verbs"],
        "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ: يَكُونُ)، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + note[0] + ".",
        "The defective present of كَانَ in jazm by لَمْ, its sign the sukun; its waw dropped where two quiescents met (from يَكُونُ). It raises its noun and puts its predicate in nasb" + note[1] + ".",
        "Kâne'nin nâkıs muzârii, lem ile meczûm, alâmeti sükûn; iki sâkin karşılaşınca vâvı düştü (aslı yekûnu). İsmini ref, haberini nasb eder" + note[2] + ".")
def ANNA_X(note=("", "", "")):
    return tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"],
        "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ" + note[0] + ".",
        "أَنَّ «that», the verb-like particle that builds a masdar: it puts its noun in nasb and raises its predicate" + note[1] + ".",
        "Enne — te'kîd, nasb ve masdar harfi: ismini nasb, haberini ref eder" + note[2] + ".")
def ISM_ENC(full, lex, enc, part_ar, part_tr):
    """قَلْبَهُ، طَرِيقَهُمْ: the noun of إِنَّ / أَنَّ / لَكِنَّ, annexed to its pronoun"""
    return tok(full, lex, "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"],
        "اسْمُ " + part_ar + " مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        "The noun of " + part_ar + ", in nasb; annexed to the attached pronoun, which fills the seat of jarr.",
        part_tr + "'nin ismi, mansûb; bitişik zamire muzâf, zamir mahallen mecrûr.",
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def MAN_ONE(seat_ar, seat_en, seat_tr, extra, note=("", "", "")):
    return tok("مَنْ", "man-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ بِمَعْنَى «الَّذِي» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ" + note[0] + ".",
        "The relative pronoun «the one who», built on sukun, in the seat of " + seat_en + "; the clause after it is its ṣila" + note[1] + ".",
        "İsm-i mevsûl «… kimse», sükûn üzere mebnî, mahallen " + seat_tr + "; sonraki cümle sılasıdır" + note[2] + ".")
def MA_MAWSULA(seat_ar, seat_en, seat_tr, extra, note=("", "", "")):
    return tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ" + note[0] + ".",
        "A relative pronoun «what», built on sukun, in the seat of " + seat_en + "; the clause after it is its ṣila" + note[1] + ".",
        "İsm-i mevsûl «…-an şey», sükûn üzere mebnî, mahallen " + seat_tr + "; sonraki cümle sılasıdır" + note[2] + ".")
MA_MAF = lambda note=("", "", ""): MA_MAWSULA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", ["maful-bihi"], note)
def ATF_ENC(full, lex, enc, case="jarr", punct=None, note=("", "", ""), extra=None):
    """وَمَالَهُ: a conjoined noun annexed to its pronoun"""
    stem = full[2:-len(enc)]
    sign = {"raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "raf'", "merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "nasb", "mansûb"), "jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "jarr", "mecrûr")}[case]
    return tok(full, lex, "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"] + (extra or []),
        WA_AR + stem + " مَعْطُوفٌ " + sign[0] + "، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note[0] + ".",
        "The waw conjoins; the noun is conjoined to the one before it, in " + sign[1] + ", and annexed to the attached pronoun, which fills the seat of jarr" + note[1] + ".",
        "Vâv atıf; isim öncekine ma'tûf, " + sign[2] + ", bitişik zamire muzâf; zamir mahallen mecrûr" + note[2] + ".",
        punct=punct, segments=[seg("وَ", "wa", "conj"), seg(stem, lex, "noun"), seg(enc, PRON[enc], "pron")])
def FA_AMMA(full):
    """فَأَمَّا / وَأَمَّا: the particle of detailing"""
    pre = full[:2]
    return tok(full, "amma", "part", ["amma-tafsiliyya"],
        ("الْفَاءُ لِلِاسْتِئْنَافِ" if pre == "فَ" else "الْوَاوُ عَاطِفَةٌ") + "، وَأَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
        ("The fa opens a new sentence" if pre == "فَ" else "The waw conjoins") + "; أَمَّا «as for» is the particle of condition, detailing and emphasis, built on sukun, with no seat — its answer must take the fa.",
        ("Fâ isti'nâf içindir" if pre == "فَ" else "«ve» +") + "; emmâ «…-e gelince»: şart, tafsîl ve te'kîd harfi, sükûn üzere mebnî, mahalli yoktur — cevabı fâ ile bağlanır.",
        segments=[seg(pre, "fa" if pre == "فَ" else "wa", "conj"), seg("أَمَّا", "amma", "part")])
FA_QAD_AMMA = lambda: tok("فَقَدْ", "qad", "part", ["amma-tafsiliyya", "qad-harf"],
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The fa answers أَمَّا; قَدْ affirms the past verb after it.", "Fâ emmâ'nın cevabına gelmiştir; kad tahkîk harfidir.",
    segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")])
def KANA_IN(full, of_ar, of_en, of_tr, pre_ar, pre_en, pre_tr, note=("", "", "")):
    """كَانَ with its noun hidden and named: «its noun is the hidden pronoun, returning to …»"""
    segs = [seg(full[:2], "fa" if full.startswith("فَ") else "wa", "conj"), seg(full[2:], "kana", "verb")] if full[0] in "وف" else None
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        pre_ar + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى " + of_ar + note[0] + ".",
        pre_en + "كَانَ is the defective past verb; its noun is the hidden pronoun «it», returning to " + of_en + note[1] + ".",
        pre_tr + "nâkıs mâzî fiil kâne; ismi " + of_tr + " dönen gizli zamir «o»" + note[2] + ".", segments=segs)
def SARA_HID(full="فَصَارَ", note=("", "", "")):
    return tok(full, "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        FA_AR + "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + note[0] + ".",
        "The fa conjoins; صَارَ «became, came to» is one of كَانَ's sisters: it raises its noun and puts its predicate in nasb; its noun is the hidden pronoun «he»" + note[1] + ".",
        "«bunun üzerine» + sâra «oldu», kâne'nin kardeşlerinden nâkıs fiil; ismini ref, haberini nasb eder; ismi gizli zamir «o»" + note[2] + ".",
        segments=[seg("فَ", "fa", "conj"), seg(full[2:], "sara", "verb")])
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
def FI_ROLE(note, punct=None):
    return PREP("فِي", "fi", note[0], note[1], note[2], gloss_tr="«-de»", punct=punct)
def MIN_ROLE(note, punct=None):
    return PREP("مِنْ", "min", note[0], note[1], note[2], gloss_tr="«-den»", punct=punct)
def AN_P(note=("", "", "")):
    return PREP("عَنْ", "an", note[0], note[1], note[2], gloss_tr="«-den»")
def ALA_ROLE(note=("", "", "")):
    return PREP("عَلَى", "ala", note[0], note[1], note[2], gloss_tr="«üzerine»")
def ILA_ROLE(note=("", "", "")):
    return PREP("إِلَى", "ila", note[0], note[1], note[2], gloss_tr="«-e»")
MINA_ROLE = lambda note: NOTE(MINA(), *note)
SANA_MI = lambda punct=None: tok("سِنِينَ", "sana", "noun", ["idafa-definiteness", "jam-mudhakkar-salim"],
    "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ — جَمْعُ سَنَةٍ.",
    "The second term of the idafa, in jarr by the ya — it is declined like the sound masculine plural (the plural of «year»).",
    "Muzâfun ileyh; cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr — sene'nin cem'i.", punct=punct)

# ============================================ the text ============================================
TITLES = [{"ar": "الْمُعَلِّمُ فِي بَغْدَادَ", "en": "The Teacher in Baghdad", "tr": "Bağdat'taki Hoca"},
          {"ar": "طَلَبُ الْيَقِينِ", "en": "The Search for Certainty", "tr": "Kesin Bilgi Arayışı"},
          {"ar": "مَرَضُ الْقَلْبِ", "en": "The Sickness of the Heart", "tr": "Kalbin Hastalığı"},
          {"ar": "الْخُرُوجُ مِنْ بَغْدَادَ", "en": "Leaving Baghdad", "tr": "Bağdat'tan Ayrılış"},
          {"ar": "الْعِلْمُ وَالْعَمَلُ", "en": "Knowledge and Action", "tr": "İlim ve Amel"}]

def PH(t, lex, span=2):
    """the name-phrase sits on the FIRST token of its span (CLAUDE.md «Idioms/phrases»): both words keep their own iʿrāb"""
    t["phrase"] = {"lex": lex, "span": span}
    return t
LA_ATIFA = lambda: tok("لَا", "la-atifa", "conj", ["atf-nasaq", "aw-imma-am-la-bal-lakin-fil-kafiya"],
    "لَا حَرْفُ عَطْفٍ يَنْفِي عَنِ الْمَعْطُوفِ مَا ثَبَتَ لِلْمَعْطُوفِ عَلَيْهِ.",
    "The conjunction لَا «not», which denies of the second term what was affirmed of the first.",
    "Atıf harfi lâ: ma'tûfun aleyhe sabit olanı ma'tûftan nefyeder.")
WA_LA_ZAIDA = lambda: tok("وَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"],
    WA_AR + "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ لَا عَمَلَ لَهَا.", "The waw conjoins; لَا only strengthens the negation and governs nothing («nor»).",
    "«ve» + lâ, nefyi pekiştirmek için zâiddir, amel etmez («ne de»).", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la-nafiya", "part")])
FA_LA = lambda: tok("فَلَا", "la-nafiya", "part", ["la-nafiya"], FA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; لَا negates and governs nothing.",
    "«bunun üzerine» + nefiy lâ'sı; amel etmez.", segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")])
JARR_FIXED = (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", "; the jarr phrase hangs on the omitted predicate of كَانَ", "; câr-mecrûr kâne'nin mahzûf haberine müteallik")
RESTR = (" — وَهُوَ الْمَقْصُورُ عَلَيْهِ", "; it is what the statement is restricted TO", "; hüküm ona hasredilmiştir")
SILA_G = ("، يَعُودُ عَلَى الْغَزَالِيِّ" + SILA_[0], " (al-Ghazālī)" + SILA_[1], " (Gazzâlî)" + SILA_[2])

# ---- Chapter 1 — الْمُعَلِّمُ فِي بَغْدَادَ ----
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Abū Ḥāmid al-Ghazālī was one of the greatest scholars of his age; he taught people at the Niẓāmiyya school in Baghdad.",
  "tr": "Ebû Hâmid el-Gazzâlî zamanının en büyük âlimlerinden biriydi; Bağdat'taki Nizâmiye Medresesi'nde insanlara ders veriyordu."},
 "tokens": [KANA("كَانَ"), ABU_ISMK(), HAMID_MI(), GHAZALI_NAAT(),
  MIN_ROLE(JARR_FIXED),
  MAJR("أَعْظَمِ", "azam", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en=", annexed — an elative and a diptote, which takes kasra here because it is annexed", note_tr=", muzâf — gayr-i munsarif ism-i tafdîl; muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("عُلَمَاءِ", "alim-scholar", extra=["jam-taksir", "mamnu-min-sarf"], note_ar="، مُضَافٌ — جَمْعُ عَالِمٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ",
       note_en=", annexed — the plural of «scholar»; a diptote (the extended alif of the feminine), it takes kasra here because it is annexed",
       note_tr=", muzâf — âlim'in cem'i; memdûde te'nîs elifi sebebiyle gayr-i munsarif iken muzâf olduğu için kesre ile mecrûr"),
  ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "mudaf", punct="،"),
  MUDARI("يُعَلِّمُ", "allama", ["form-ii-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرٌ ثَانٍ لِكَانَ", note_en="; the clause is a second predicate of كَانَ, in the seat of nasb", note_tr="; cümle kâne'nin ikinci haberi, mahallen mansûb"),
  MAFUL("النَّاسَ", "nas"),
  FI(), MAJR("الْمَدْرَسَةِ", "madrasa"),
  NAAT("النِّظَامِيَّةِ", "nizamiyya", "jarr", extra=["ism-mansub"], note_ar=" — نِسْبَةٌ إِلَى الْوَزِيرِ نِظَامِ الْمُلْكِ", note_en=" — a nisba to the vizier Niẓām al-Mulk", note_tr=" — vezir Nizâmülmülk'e nispet"),
  BI_TOWN("بِبَغْدَادَ", "baghdad", "بَغْدَادَ", DIPT_TOWN, punct=".", note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «الْمَدْرَسَةِ»", "; the jarr phrase hangs on an omitted hal of «the school»", "; câr-mecrûr «medrese»den mahzûf bir hâle müteallik"))]})
S1.append({"id": "s2", "translation": {
  "en": "And how many a student came to him from distant lands!",
  "tr": "Uzak diyarlardan nice talebe ona yöneldi!"},
 "tokens": [KAM("وَكَمْ"), KAM_TAMYIZ("طَالِبٍ", "talib"),
  ENC_MADI("قَصَدَهُ", "qasada", "هُ", hidden=True, note_ar="؛ وَالْفَاعِلُ يَعُودُ عَلَى «كَمْ»، وَالْهَاءُ لِلْغَزَالِيِّ" + KH_KAM[0], note_en="; the hidden doer returns to كَمْ, and «him» is al-Ghazālī" + KH_KAM[1], note_tr="; gizli fâil kem'e, zamir Gazzâlî'ye döner" + KH_KAM[2]),
  MIN_ROLE((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَصَدَهُ»", "; the jarr phrase hangs on «came to him»", "; câr-mecrûr «ona yöneldi»ye müteallik")),
  MAJR("بِلَادٍ", "bilad", extra=["jam-taksir"], note_ar=" — جَمْعُ بَلَدٍ", note_en=" — the plural of «land»", note_tr=" — beled'in cem'i"),
  NAAT("بَعِيدَةٍ", "baid", "jarr", note_ar=" — وَأُنِّثَ لِأَنَّ مَنْعُوتَهُ جَمْعٌ لِغَيْرِ الْعَاقِلِ", note_en=" — feminine, because the noun it describes is a plural of things", note_tr=" — mevsûfu akılsızların cem'i olduğu için müennes geldi", punct="!")]})
S1.append({"id": "s3", "translation": {
  "en": "He had great standing and much wealth.",
  "tr": "Büyük bir itibarı ve çok malı vardı."},
 "tokens": [KANA("وَكَانَ"),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («onun»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ مُقَدَّمٍ", note_en="; the jarr phrase is the FRONTED predicate of كَانَ", note_tr="; câr-mecrûr kâne'nin öne alınmış haberidir"),
  ISMK("جَاهٌ", "jah", muakhkhar=True), NAAT("عَظِيمٌ", "azim", "raf"),
  ATF("وَمَالٌ", "mal", "noun", "raf"), NAAT("كَثِيرٌ", "kathir", "raf", punct=".")]})
S1.append({"id": "s4", "translation": {
  "en": "Yet his heart was not at rest in the knowledge he had.",
  "tr": "Ne var ki kalbi, sahip olduğu ilimle mutmain olmuyordu."},
 "tokens": [tok("وَلَكِنَّ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya"],
      WA_AR + "لَكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "The waw conjoins; لَكِنَّ «but» is the particle of correction (istidrāk): it puts its noun in nasb and raises its predicate.",
      "«ve» + lâkinne: istidrâk ve nasb harfi; ismini nasb, haberini ref eder.",
      segments=[seg("وَ", "wa", "conj"), seg("لَكِنَّ", "lakinna", "part")]),
  ISM_ENC("قَلْبَهُ", "qalb", "هُ", "لَكِنَّ", "Lâkinne"),
  LAM_JAZM("لَمْ"),
  YAKUN(note=("، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى الْقَلْبِ" + KH_LAKIN_CL[0], "; its noun is the hidden «it» (the heart)" + KH_LAKIN_CL[1], "; ismi kalbe dönen gizli zamir «o»" + KH_LAKIN_CL[2])),
  tok("يَطْمَئِنُّ", "itmaanna", "verb", ["mudari-marfu", "rubai-babs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُنْ؛ وَالْفِعْلُ رُبَاعِيٌّ مَزِيدٌ: اطْمَأَنَّ يَطْمَئِنُّ.",
      "Present verb in raf'; the doer is the hidden «it» — the clause fills the seat of nasb as the predicate of يَكُنْ; the verb is an augmented quadriliteral (اطْمَأَنَّ يَطْمَئِنُّ «to be at rest»).",
      "Merfû muzâri; fâil gizli zamir «o» — cümle yekün'ün haberi olarak mahallen mansûb; fiil mezîd rubâîdir (itmeenne yatmeinnu «mutmain olmak»)."),
  ILA(),
  MA_MAWSULA("جَرٍّ بِإِلَى", "jarr after إِلَى", "ilâ ile mecrûr", ["huruf-jarr"]),
  ZARF_ENC("عِنْدَهُ", "inda", "هُ", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةٍ لِـ«مَا»", note_en=" — the adverb hangs on the omitted ṣila of «what»", note_tr=" — zarf «mâ»nın mahzûf sılasına müteallik"),
  MINA_ROLE((" — وَهِيَ لِبَيَانِ «مَا»", "; it is the مِنْ that explains «what»", "; «mâ»yı açıklayan (beyân) min'dir")),
  MAJR("الْعِلْمِ", "ilm", punct=".")]})
S1.append({"id": "s5", "translation": {
  "en": "What he sought was only a knowledge with which no doubt remains.",
  "tr": "O ancak, yanında hiçbir şüphenin kalmadığı bir ilim arıyordu."},
 "tokens": [WA_INNAMA("وَإِنَّمَا"), KANA_HID("كَانَ", note=HID_G),
  MUDARI("يَطْلُبُ", "talaba", **W(KH_KANA)),
  MAFUL("عِلْمًا", "ilm", **W(RESTR)),
  LA_NAFIYA(),
  tok("يَبْقَى", "baqiya", "verb", ["mudari-marfu", "naqis-verbs", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«عِلْمًا».",
      "Present verb in raf' by a damma estimated on the alif; its doer follows — the clause qualifies «a knowledge», in the seat of nasb.",
      "Elif üzerinde takdîrî damme ile merfû muzâri; fâili ondan sonra gelir — cümle «ilim»in na'tı, mahallen mansûb."),
  ZARF_ENC("مَعَهُ", "maa", "هُ", note_ar=" — وَالْهَاءُ رَابِطٌ يَعُودُ عَلَى «عِلْمًا»", note_en=" — the pronoun ties the clause back to «a knowledge»", note_tr=" — zamir «ilim»e dönen râbıttır"),
  FAIL("شَكٌّ", "shakk", punct=".")]})

# ---- Chapter 2 — طَلَبُ الْيَقِينِ ----
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "Then he looked into the ways of those who sought the truth in his time, and found them to be four groups.",
  "tr": "Sonra zamanında hakikati arayanların yollarını inceledi ve onları dört zümre olarak buldu."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  MADI("نَظَرَ", "nazara", hidden=True, **W(HID_G, KH_INNA_CL)),
  FI(), MAJR("طُرُقِ", "tariq", extra=["jam-taksir"], **W(MUDAF, (" — جَمْعُ طَرِيقٍ", " — the plural of «way»", " — tarîk'in cem'i"))),
  tok("الَّذِينَ", "alladhina", "pron", ["ism-mawsul", "idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ لِجَمْعِ الذُّكُورِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
      "The masculine plural relative «those who», built on fatha, in the seat of jarr as the second term of the idafa; the clause after it is its ṣila.",
      "Eril çoğul ism-i mevsûl «… kimseler», fetha üzere mebnî, muzâfun ileyh olarak mahallen mecrûr; sonraki cümle sılasıdır."),
  MUDARI5("يَطْلُبُونَ", "talaba", role_ar=SILA_[0], role_en=SILA_[1], role_tr=SILA_[2]),
  MAFUL("الْحَقَّ", "haqq"),
  FI_ROLE((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَطْلُبُونَ»", "; the jarr phrase hangs on «sought»", "; câr-mecrûr «ararlar»a müteallik")),
  ENC_NOUN("زَمَانِهِ", "zaman", "هِ", "majr", punct="،"),
  ENC_MADI("فَوَجَدَهُمْ", "wajada", "هُمْ", ["zanna-wa-akhawatuha", "mafulayn"], hidden=True,
       note_ar=" — وَوَجَدَ هُنَا مِنْ أَفْعَالِ الْقُلُوبِ يَنْصِبُ مَفْعُولَيْنِ، وَهٰذَا الضَّمِيرُ أَوَّلُهُمَا",
       note_en=" — وَجَدَ here is a verb of the heart («found them to be») with two objects; this pronoun is the first",
       note_tr=" — vecede burada iki mef'ûl alan kalp fiilidir («… olarak buldu»); bu zamir birinci mef'ûldür"),
  tok("أَرْبَعَ", "arba", "noun", ["mafulayn", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَجَاءَ الْعَدَدُ بِلَا تَاءٍ لِأَنَّ مُفْرَدَ الْمَعْدُودِ (طَائِفَة) مُؤَنَّثٌ.",
      "The second object, in nasb and annexed — the number has no ta because the singular of what is counted (طَائِفَة «group») is feminine.",
      "İkinci mef'ûl, mansûb, muzâf — sayılanın tekili (tâife) müennes olduğu için sayı tâsız gelmiştir."),
  MUDAF_ILAYH("طَوَائِفَ", "taifa", extra=["jam-taksir", "mamnu-min-sarf"], sign=FATHA_JARR, note_ar=" — جَمْعُ طَائِفَةٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، مَمْنُوعٌ مِنَ الصَّرْفِ", note_en=" — the plural of «group» on the pattern of the farthest plurals, a diptote", note_tr=" — tâife'nin cem'i; müntehe'l-cumû' sîgasında, gayr-i munsarif", punct=".")]})
ATF_FI = (" — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى «فِي عِلْمِ الْكَلَامِ»", "; the jarr phrase is conjoined to «into the science of kalām»", "; câr-mecrûr «kelâm ilminde»ye ma'tûf")
S2.append({"id": "s2", "translation": {
  "en": "So he examined the science of kalām, then the books of the philosophers, then the doctrine of the Bāṭiniyya, and came to know what each group of them held; yet with none of them did he find what he was seeking.",
  "tr": "Böylece önce kelâm ilmini, sonra filozofların kitaplarını, sonra Bâtınîlerin mezhebini inceledi; her zümrenin elinde ne olduğunu öğrendi, fakat hiçbirinin yanında aradığını bulamadı."},
 "tokens": [MADI("فَنَظَرَ", "nazara", hidden=True),
  FI(), MAJR("عِلْمِ", "ilm", **W(MUDAF)),
  MUDAF_ILAYH("الْكَلَامِ", "kalam", note_ar=" — وَعِلْمُ الْكَلَامِ: عِلْمُ الْعَقَائِدِ وَأَدِلَّتِهَا", note_en=" — ʿilm al-kalām: the science of the articles of faith and their proofs", note_tr=" — kelâm ilmi: akaid ve delilleri ilmi", punct="،"),
  THUMMA(), FI_ROLE(ATF_FI),
  MAJR("كُتُبِ", "kitab", extra=["jam-taksir"], **W(MUDAF, (" — جَمْعُ كِتَابٍ", " — the plural of «book»", " — kitâb'ın cem'i"))),
  MUDAF_ILAYH("الْفَلَاسِفَةِ", "faylasuf", extra=["jam-taksir"], note_ar=" — جَمْعُ فَيْلَسُوفٍ", note_en=" — the plural of «philosopher»", note_tr=" — feylesof'un cem'i", punct="،"),
  THUMMA(), FI_ROLE(ATF_FI),
  MAJR("مَذْهَبِ", "madhhab", **W(MUDAF)),
  MUDAF_ILAYH("الْبَاطِنِيَّةِ", "batiniyya", extra=["ism-mansub"], note_ar=" — اسْمُ فِرْقَةٍ، نِسْبَةٌ إِلَى الْبَاطِنِ", note_en=" — the name of a sect, a nisba to «the inner (meaning)»", note_tr=" — bir fırkanın adı, «bâtın»a nispet", punct="،"),
  MADI("فَعَرَفَ", "arafa", hidden=True),
  MA_MAF(),
  ZARF("عِنْدَ", "inda", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ صِلَةٍ لِـ«مَا»", note_en=" — the adverb hangs on the omitted ṣila of «what»", note_tr=" — zarf «mâ»nın mahzûf sılasına müteallik"),
  MUDAF_ILAYH("كُلِّ", "kull", **W(MUDAF)),
  MUDAF_ILAYH("طَائِفَةٍ", "taifa"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", punct="،", **W(NAAT_OF("طَائِفَةٍ", "group", "zümre"))),
  WA_LAM(),
  JAZM_V("يَجِدْ", "wajada", ["mithal-verbs"], hidden="هُوَ", note_ar=" — وَحُذِفَتْ وَاوُهُ فِي الْمُضَارِعِ (وَجَدَ يَجِدُ)", note_en=" — its waw drops in the present (وَجَدَ يَجِدُ)", note_tr=" — muzâride vâvı düşer (vecede yecidu)"),
  ZARF("عِنْدَ", "inda"),
  MUDAF_ILAYH("أَحَدٍ", "ahad"),
  JARR_PRON("مِنْهُمْ", "min", "مِنْ", "هُمْ", " («onlardan»)", **W(NAAT_OF("أَحَدٍ", "one", "biri"))),
  MA_MAF(),
  KANA_HID("كَانَ", note=SILA_G),
  MUDARI("يَطْلُبُ", "talaba", note_ar=KH_KANA[0] + "، وَالْعَائِدُ عَلَى «مَا» مَحْذُوفٌ تَقْدِيرُهُ: يَطْلُبُهُ", note_en=KH_KANA[1] + "; the pronoun returning to «what» is dropped («seeking [it]»)", note_tr=KH_KANA[2] + "; «mâ»ya dönen zamir hazfedilmiştir («onu arıyordu»)", punct=".")]})
S2.append({"id": "s3", "translation": {
  "en": "Then he turned to the way of the Ṣūfīs: he read their books and came to know their learning.",
  "tr": "Sonra sûfîlerin yoluna yöneldi; kitaplarını okudu ve ilimlerini öğrendi."},
 "tokens": [THUMMA(),
  MADI("أَقْبَلَ", "aqbala", ["form-iv-verbs"], hidden=True),
  ALA_ROLE((" — وَأَقْبَلَ عَلَى الشَّيْءِ: تَوَجَّهَ إِلَيْهِ وَاشْتَغَلَ بِهِ", "; to «come forward upon» a thing is to turn to it and give oneself to it", "; bir şeye «yönelmek», ona dönüp onunla meşgul olmaktır")),
  MAJR("طَرِيقِ", "tariq", **W(MUDAF)),
  MUDAF_ILAYH("الصُّوفِيَّةِ", "sufiyya", extra=["ism-mansub"], punct="،"),
  MADI("فَقَرَأَ", "qaraa", hidden=True),
  ENC_NOUN("كُتُبَهُمْ", "kitab", "هُمْ", "maful", extra=["jam-taksir"], note_ar=" — جَمْعُ كِتَابٍ", note_en=" — the plural of «book»", note_tr=" — kitâb'ın cem'i", punct="،"),
  MADI("وَعَرَفَ", "arafa", hidden=True),
  ENC_NOUN("عِلْمَهُمْ", "ilm", "هُمْ", "maful", punct=".")]})
S2.append({"id": "s4", "translation": {
  "en": "And he learned that their way is made complete only by knowledge and action together.",
  "tr": "Ve onların yolunun ancak ilim ve amel ile tamamlandığını öğrendi."},
 "tokens": [MADI("فَعَلِمَ", "alima", hidden=True),
  ANNA_X(SADDA("عَلِمَ", "learned", "öğrendi")),
  ISM_ENC("طَرِيقَهُمْ", "tariq", "هُمْ", "أَنَّ", "Enne"),
  LA_NAFIYA(),
  tok("يَتِمُّ", "tamma", "verb", ["mudari-marfu", "doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، يَعُودُ عَلَى الطَّرِيقِ" + KH_ANNA_CL[0] + ".",
      "Present verb in raf'; the doer is the hidden «it» (the way)" + KH_ANNA_CL[1] + ".",
      "Merfû muzâri; fâil yola dönen gizli zamir «o»" + KH_ANNA_CL[2] + "."),
  ILLA_HASR(),
  BI_NOUN("بِعِلْمٍ", "ilm", "عِلْمٍ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَتِمُّ»، وَهُوَ الْمَقْصُورُ عَلَيْهِ", note_en="; the jarr phrase hangs on «is completed», and it is what the statement is restricted TO", note_tr=" — câr-mecrûr «tamamlanır»a müteallik; hüküm ona hasredilmiştir"),
  ATF("وَعَمَلٍ", "amal-work", "noun", "jarr", punct=".")]})
S2.append({"id": "s5", "translation": {
  "en": "As for knowledge, it was already his; as for action, it asked of him that he leave his standing and his wealth.",
  "tr": "İlme gelince, o zaten onda vardı; amele gelince, ondan itibarını ve malını bırakmasını istiyordu."},
 "tokens": [FA_AMMA("فَأَمَّا"), MUBTADA("الْعِلْمُ", "ilm"), FA_QAD_AMMA(),
  KANA_IN("كَانَ", "«الْعِلْمُ»", "«knowledge»", "«ilim»e", "", "", "", note=KH_MUB_CL),
  ZARF_ENC("عِنْدَهُ", "inda", "هُ", note_ar=" — وَالظَّرْفُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ كَانَ، وَالْهَاءُ لِلْغَزَالِيِّ", note_en=" — the adverb hangs on the omitted predicate of كَانَ; «him» is al-Ghazālī", note_tr=" — zarf kâne'nin mahzûf haberine müteallik; zamir Gazzâlî'ye döner", punct="،"),
  FA_AMMA("وَأَمَّا"), MUBTADA("الْعَمَلُ", "amal-work"),
  KANA_IN("فَكَانَ", "«الْعَمَلُ»", "«action»", "«amel»e", "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَ", "The fa answers أَمَّا; ", "Fâ emmâ'nın cevabına gelmiştir; ", note=KH_MUB_CL),
  MUDARI("يَطْلُبُ", "talaba", **W(KH_KANA)),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«يَطْلُبُ»", "; the clause it builds fills the seat of nasb as the object of «asked»", "; kurduğu müevvel masdar «isterdi»nin mef'ûlü olarak mahallen mansûb"),
  MANSUB_AN("يَتْرُكَ", "taraka"),
  ENC_NOUN("جَاهَهُ", "jah", "هُ", "maful"),
  ATF_ENC("وَمَالَهُ", "mal", "هُ", case="nasb", punct=".")]})
S2.append({"id": "s6", "translation": {
  "en": "Then he examined his intention in teaching, and saw that the love of standing had entered into it.",
  "tr": "Sonra öğretmedeki niyetine baktı ve ona makam sevgisinin girmiş olduğunu gördü."},
 "tokens": [THUMMA(), MADI("نَظَرَ", "nazara", hidden=True),
  FI(), ENC_NOUN("نِيَّتِهِ", "niyya", "هِ", "majr"),
  FI_ROLE((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نِيَّتِهِ»", "; the jarr phrase hangs on «his intention»", "; câr-mecrûr «niyeti»ne müteallik")),
  MAJR("التَّعْلِيمِ", "talim", punct="،"),
  MADI_ALIF("فَرَأَى", "raa", ["zanna-wa-akhawatuha"], hidden=True, note_ar=" — وَالرُّؤْيَةُ هُنَا قَلْبِيَّةٌ", note_en=" — «saw» here is the seeing of the mind", note_tr=" — rü'yet burada kalbîdir"),
  ANNA_X(SADDA("رَأَى", "saw", "gördü")),
  tok("حُبَّ", "hubb", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb, annexed.", "Enne'nin ismi, mansûb, muzâf."),
  MUDAF_ILAYH("الْجَاهِ", "jah"),
  QAD(),
  ENC_MADI("دَخَلَهَا", "dakhala", "هَا", hidden=True, note_ar="؛ وَالْفَاعِلُ يَعُودُ عَلَى «حُبَّ»، وَالْهَاءُ لِلنِّيَّةِ" + KH_ANNA_CL[0], note_en="; the hidden doer is «the love», and «it» is the intention" + KH_ANNA_CL[1], note_tr="; gizli fâil «sevgi», zamir niyettir" + KH_ANNA_CL[2], punct=".")]})

# ---- Chapter 3 — مَرَضُ الْقَلْبِ ----
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "So for months he stayed like this: one day resolving to leave, then another day turning back from his resolve.",
  "tr": "Böylece aylarca öyle kaldı: bir gün çıkıp gitmeye azmediyor, sonra başka bir gün azminden dönüyordu."},
 "tokens": [MADI("فَبَقِيَ", "baqiya", hidden=True),
  ZARF("أَشْهُرًا", "shahr", mudaf=False, extra=["jam-taksir"], note_ar=" — جَمْعُ شَهْرٍ", note_en=" — the plural of «month»", note_tr=" — şehr'in cem'i", **ZAMAN),
  MUDARI("يَعْزِمُ", "azama", **W(HALCL)),
  ALA(), MAJR("الْخُرُوجِ", "khuruj"),
  ZARF("يَوْمًا", "yawm", mudaf=False, punct="،", **ZAMAN),
  THUMMA(),
  MUDARI("يَرْجِعُ", "rajaa", **W((" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «يَعْزِمُ»", "; the clause is conjoined to «resolving»", "; cümle «azmeder»e ma'tûf"))),
  AN_P(), ENC_NOUN("عَزْمِهِ", "azm-resolve", "هِ", "majr"),
  ZARF("يَوْمًا", "yawm", mudaf=False, **ZAMAN),
  AKHAR_NAAT("آخَرَ", "nasb", punct=".")]})
S3.append({"id": "s2", "translation": {
  "en": "And while he was in that state, all at once his tongue was held back from speech: he would sit for his students and be unable to teach them.",
  "tr": "O bu hâldeyken ansızın dili konuşmaktan tutuldu; talebeleri için oturuyor, fakat onlara ders vermeye güç yetiremiyordu."},
 "tokens": [BAYNAMA(), PRON_MUB("هُوَ", "huwa"),
  PREP("عَلَى", "ala", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ", "; the jarr phrase hangs on the omitted predicate of «he»", "; câr-mecrûr mübtedânın mahzûf haberine müteallik", gloss_tr="«üzere»"),
  DHALIKA("جَرٍّ", "jarr", "mecrûr"),
  IDH_FUJ(),
  MAJHUL("أُمْسِكَ", "amsaka", ["form-iv-verbs"], note_ar="، وَنَائِبُ الْفَاعِلِ بَعْدَهُ", note_en="; its deputy doer follows", note_tr="; nâib-i fâili ondan sonra gelir"),
  tok("لِسَانُهُ", "lisan", "noun", ["naib-al-fail", "idafa-definiteness", "al-bariz-al-muttasil"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The deputy doer (na'ib al-fa'il), in raf'; annexed to the attached pronoun, which fills the seat of jarr.",
      "Nâib-i fâil, merfû; bitişik zamire muzâf, zamir mahallen mecrûr.",
      segments=[seg("لِسَانُ", "lisan", "noun"), seg("هُ", "pron-3ms", "pron")]),
  AN_KASRA(), MAJR("الْكَلَامِ", "kalam", punct="،"),
  KANA_HID("فَكَانَ", note=HID_G),
  MUDARI("يَجْلِسُ", "jalasa", **W(KH_KANA)),
  LI_ENC("لِطُلَّابِهِ", "tullab", "طُلَّابِ", "هِ", note_ar=" — وَاللَّامُ لِلتَّعْلِيلِ: يَجْلِسُ لِأَجْلِهِمْ", note_en=" — the lam of purpose: he sits for their sake", note_tr=" — lâm ta'lîl içindir: onlar için oturur"),
  FA_LA(),
  MUDARI("يَقْدِرُ", "qadara-able", **W((" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «يَجْلِسُ» فَهِيَ مِثْلُهَا فِي مَحَلِّ نَصْبٍ", "; the clause is conjoined to «he would sit» and shares its seat of nasb", "; cümle «otururdu»ya ma'tûf, onun gibi mahallen mansûb"))),
  ALA(), ENC_NOUN("تَعْلِيمِهِمْ", "talim", "هِمْ", "majr", punct=".")]})
S3.append({"id": "s3", "translation": {
  "en": "Then he grew too weak for food, so that he ate only a little, until his strength was gone.",
  "tr": "Sonra yemeğe güç yetiremez oldu; az bir şeyden başkasını yiyemiyordu; sonunda takati tükendi."},
 "tokens": [THUMMA(),
  MADI("ضَعُفَ", "daufa", hidden=True, note_en=" — to be «too weak for» (عَنْ) a thing", note_tr=" — bir şeye (عَنْ) «güç yetirememek»"),
  AN_KASRA(), MAJR("الطَّعَامِ", "taam", punct="،"),
  SARA_HID("فَصَارَ", note=HID_G),
  LA_NAFIYA(),
  MUDARI("يَأْكُلُ", "akala", **W(KH_SARA)),
  ILLA_HASR(),
  tok("قَلِيلًا", "qalil", "noun", ["maful-bihi", "qasr"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، وَهُوَ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، أَيْ: شَيْئًا قَلِيلًا — وَهُوَ الْمَقْصُورُ عَلَيْهِ.",
      "The object, in nasb — an adjective standing for an omitted noun («a little [something]»); it is what the statement is restricted TO.",
      "Mef'ûlün bih, mansûb — mahzûf bir mevsûfun sıfatıdır («az [bir şey]»); hüküm ona hasredilmiştir.", punct="،"),
  HATTA_IBT(),
  MADI("ذَهَبَتْ", "dhahaba", fem=True, **W(FAIL_BAAD)),
  ENC_NOUN("قُوَّتُهُ", "quwwa", "هُ", "fail", punct=".")]})
S3.append({"id": "s4", "translation": {
  "en": "The physicians could not cure him; for what ailed him lay only in his heart, not in his body.",
  "tr": "Hekimler onu tedavi etmekten âciz kaldı; zira derdi ancak kalbindeydi, bedeninde değil."},
 "tokens": [MADI("وَعَجَزَ", "ajaza", **W(FAIL_BAAD)),
  FAIL("الْأَطِبَّاءُ", "tabib", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ طَبِيبٍ، وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", note_en=" — the plural of «physician», a diptote (the extended alif of the feminine)", note_tr=" — tabîb'in cem'i; memdûde te'nîs elifi sebebiyle gayr-i munsarif"),
  AN_P(), ENC_NOUN("عِلَاجِهِ", "ilaj", "هِ", "majr", punct="،"),
  WA_INNAMA("وَإِنَّمَا"), KANA("كَانَ"),
  MA_MAWSULA("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi", ["kana-wa-akhawatuha"]),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onda»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِلَةٍ لِـ«مَا»؛ وَمَا بِهِ: مَا أَصَابَهُ", note_en="; the jarr phrase hangs on the omitted ṣila of «what» — «what is with him» is what has struck him", note_tr="; câr-mecrûr «mâ»nın mahzûf sılasına müteallik — «ondaki şey», ona isabet eden derttir"),
  FI_ROLE((JARR_FIXED[0] + "، وَهُوَ الْمَقْصُورُ عَلَيْهِ", JARR_FIXED[1] + ", and it is what the statement is restricted TO", JARR_FIXED[2] + "; hüküm ona hasredilmiştir")),
  ENC_NOUN("قَلْبِهِ", "qalb", "هِ", "majr", punct="،"),
  LA_ATIFA(),
  FI_ROLE((" — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى «فِي قَلْبِهِ»", "; the jarr phrase is conjoined to «in his heart»", "; câr-mecrûr «kalbinde»ye ma'tûf")),
  ENC_NOUN("جِسْمِهِ", "jism", "هِ", "majr", punct=".")]})
S3.append({"id": "s5", "translation": {
  "en": "When he knew that there was no way out for him, he turned back to his Lord, calling on Him, and it grew easy for him to leave what he had been in.",
  "tr": "Hiçbir çaresi kalmadığını anlayınca Rabbine dua ederek yöneldi; içinde bulunduğu şeyi bırakmak ona kolay geldi."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI("عَرَفَ", "arafa", hidden=True, **W(LAMMA_CL)),
  tok("أَنَّهُ", "anna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"],
      "أَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُهَا، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِـ«عَرَفَ».",
      "أَنَّ «that», the masdar-building verb-like particle; the attached pronoun is the PRONOUN OF THE MATTER (ḍamīr al-shaʾn), its noun, in the seat of nasb — the clause after it is its predicate, in the seat of raf', and the whole stands as the object of «knew».",
      "Enne — te'kîd, nasb ve masdar harfi; bitişik zamir şan zamiridir, ismi olarak mahallen mansûb — sonraki cümle haberi, mahallen merfû; müevvel masdar «anladı»nın mef'ûlüdür.",
      segments=[seg("أَنَّ", "anna", "part"), seg("هُ", "pron-3ms", "pron")]),
  tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"],
      "لَا نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ — وَجُمْلَتُهَا فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.",
      "لَا that denies the whole genus («no … at all»), working like إِنَّ — its clause is the predicate of أَنَّ, in the seat of raf'.",
      "Cinsini nefyeden lâ, inne gibi amel eder — cümlesi enne'nin haberi, mahallen merfû."),
  tok("حِيلَةَ", "hila", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.",
      "The noun of لَا, built on fatha (no tanwin), in the seat of nasb.", "Lâ'nın ismi, fetha üzere mebnî (tenvinsiz), mahallen mansûb."),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («onun»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ لَا", note_en="; the jarr phrase hangs on the omitted predicate of لَا", note_tr="; câr-mecrûr lâ'nın mahzûf haberine müteallik", punct="،"),
  MADI("رَجَعَ", "rajaa", hidden=True, **W(JAWAB_LAMMA)),
  ILA(), ENC_NOUN("رَبِّهِ", "rabb", "هِ", "majr"),
  MUDARI("يَدْعُوهُ", "daa", naqis="و", enc="هُ", **W(HALCL), punct="،"),
  MADI("فَهَانَ", "hana", ["hollow-verbs"], note_ar="، وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ", note_en="; its doer is the masdar-clause that follows", note_tr="; fâili sonraki müevvel masdardır"),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («ona»)"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ فَاعِلُ «هَانَ»", "; the clause it builds is the doer of «grew easy», in the seat of raf'", "; kurduğu müevvel masdar «kolay geldi»nin fâili, mahallen merfû"),
  MANSUB_AN("يَتْرُكَ", "taraka"),
  MA_MAF(),
  KANA_HID("كَانَ", note=SILA_G),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («içinde»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ، وَالْهَاءُ هِيَ الْعَائِدُ عَلَى «مَا»", note_en="; the jarr phrase hangs on the omitted predicate of كَانَ, and the pronoun is the one that returns to «what»", note_tr="; câr-mecrûr kâne'nin mahzûf haberine müteallik; zamir «mâ»ya dönen râbıttır", punct=".")]})
S3.append({"id": "s6", "translation": {
  "en": "So he resolved to leave, and this time he did not turn back from his resolve.",
  "tr": "Bunun üzerine çıkıp gitmeye azmetti ve bu sefer azminden dönmedi."},
 "tokens": [MADI("فَعَزَمَ", "azama", hidden=True),
  ALA(), MAJR("الْخُرُوجِ", "khuruj", punct="،"),
  WA_LAM(), JAZM_V("يَرْجِعْ", "rajaa", hidden="هُوَ"),
  AN_P(), ENC_NOUN("عَزْمِهِ", "azm-resolve", "هِ", "majr"),
  tok("هٰذِهِ", "hadhihi", "pron", ["asma-al-ishara", "maful-fih"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ نَصْبٍ نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ.",
      "The demonstrative «this», built on kasra, in the seat of nasb, standing in for an adverb of time.",
      "İşaret ismi «bu», kesre üzere mebnî, zaman zarfına nâib olarak mahallen mansûb."),
  BADAL("الْمَرَّةَ", "marra-once", "nasb", punct=".")]})

# ---- Chapter 4 — الْخُرُوجُ مِنْ بَغْدَادَ ----
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "Then he left Baghdad in the year four hundred and eighty-eight, leaving teaching and standing behind him.",
  "tr": "Sonra dört yüz seksen sekiz yılında Bağdat'tan çıktı; öğretmeyi ve makamı ardında bıraktı."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  MADI("خَرَجَ", "kharaja", hidden=True, **W(KH_INNA_CL)),
  MIN(), BAGHDAD_J(),
  ZARF("سَنَةَ", "sana", **ZAMAN),
  tok("ثَمَانٍ", "thamani", "noun", ["idafa-definiteness", "asma-al-adad-fil-kafiya", "ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، مَنَعَ مِنْ ظُهُورِهَا الثِّقَلُ، وَالتَّنْوِينُ عِوَضٌ عَنِ الْيَاءِ — اسْمٌ مَنْقُوصٌ، وَجَاءَ بِلَا تَاءٍ لِأَنَّ الْمَعْدُودَ (سَنَة) مُؤَنَّثٌ.",
      "The second term of the idafa, in jarr by a kasra estimated on the ya (too heavy to show), the ya itself dropped where it met the tanwin; the tanwin stands in for the ya — a manqūṣ noun; it has no ta because what is counted (سَنَة «year») is feminine.",
      "Muzâfun ileyh; yâ üzerinde takdîrî kesre ile mecrûr (ağır geldiği için görünmez); yâ, tenvinle karşılaşınca düşmüştür; tenvin yâ'nın yerine gelmiştir — menkûs isim; sayılan (sene) müennes olduğu için tâsızdır."),
  tok("وَثَمَانِينَ", "thamanun", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"],
      WA_AR + "ثَمَانِينَ مَعْطُوفٌ عَلَى «ثَمَانٍ» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.",
      "The waw conjoins; «eighty» is conjoined to «eight», in jarr by the ya — it is declined like the sound masculine plural.",
      "Vâv atıf; «seksen» «sekiz»e ma'tûf, cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr.",
      segments=[seg("وَ", "wa", "conj"), seg("ثَمَانِينَ", "thamanun", "noun")]),
  tok("وَأَرْبَعِمِائَةٍ", "arbaumia", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَرْبَعِ» مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ«مِائَةٍ» مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَحُذِفَتِ التَّاءُ مِنْ أَرْبَعٍ لِأَنَّ الْمِائَةَ مُؤَنَّثَةٌ، وَيُكْتَبُ الْجُزْآنِ كَلِمَةً وَاحِدَةً.",
      "The waw conjoins; «four» is conjoined, in jarr and annexed, and «hundred» is its second term, in jarr — four has no ta because «hundred» is feminine, and the two parts are written as one word.",
      "Vâv atıf; «dört» ma'tûf, mecrûr, muzâf; «yüz» muzâfun ileyh, mecrûr — «yüz» müennes olduğu için erbaʿ tâsızdır; iki parça bitişik yazılır.",
      punct="،", segments=[seg("وَ", "wa", "conj"), seg("أَرْبَعِمِائَةٍ", "arbaumia", "noun")]),
  MADI("وَتَرَكَ", "taraka", hidden=True),
  ZARF_ENC("وَرَاءَهُ", "wara", "هُ"),
  MAFUL("التَّعْلِيمَ", "talim"),
  ATF("وَالْجَاهَ", "jah", "noun", "nasb", punct=".")]})
S4.append({"id": "s2", "translation": {
  "en": "He spent his wealth away, and took of it only what would suffice him.",
  "tr": "Malını dağıttı; ondan ancak kendisine yetecek kadarını aldı."},
 "tokens": [MADI("وَأَنْفَقَ", "anfaqa", ["form-iv-verbs"], hidden=True),
  ENC_NOUN("مَالَهُ", "mal", "هُ", "maful", punct="،"),
  LAM_JAZM("فَلَمْ"),
  JAZM_V("يَأْخُذْ", "akhadha", hidden="هُوَ"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)"),
  ILLA_HASR(),
  MA_MAF(RESTR),
  MUDARI("يَكْفِيهِ", "kafa", naqis="ي", enc="هُ", note_ar="؛ وَالْفَاعِلُ يَعُودُ عَلَى «مَا»، وَالْهَاءُ لِلْغَزَالِيِّ" + SILA_[0], note_en="; the hidden doer is «what», and «him» is al-Ghazālī" + SILA_[1], note_tr="; gizli fâil «mâ», zamir Gazzâlî" + SILA_[2], punct=".")]})
S4.append({"id": "s3", "translation": {
  "en": "Then he travelled to the lands of Syria and stayed in Damascus, then went on from there to Jerusalem.",
  "tr": "Sonra Şam diyarına gitti ve Dımaşk'ta ikamet etti; sonra oradan Beytülmakdis'e geçti."},
 "tokens": [THUMMA(), MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  ILA(), MAJR("بِلَادِ", "bilad", extra=["jam-taksir"], **W(MUDAF)),
  MUDAF_ILAYH("الشَّامِ", "sham", "propn", punct="،"),
  MADI("فَأَقَامَ", "aqama", ["form-iv-verbs", "hollow-verbs"], hidden=True),
  BI_TOWN("بِدِمَشْقَ", "dimashq", "دِمَشْقَ", DIPT_TOWN, punct="،"),
  THUMMA(), MADI("رَحَلَ", "rahala", hidden=True),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («oradan»)", note_ar=" — وَالضَّمِيرُ لِدِمَشْقَ", note_en=" — «it» is Damascus", note_tr=" — zamir Dımaşk'a döner"),
  ILA(),
  PH(MAJR("بَيْتِ", "bayt", **W(MUDAF)), "bayt-al-maqdis"),
  MUDAF_ILAYH("الْمَقْدِسِ", "maqdis", punct=".")]})
S4.append({"id": "s4", "translation": {
  "en": "Then he travelled to the Ḥijāz and made the pilgrimage.",
  "tr": "Sonra Hicaz'a gitti ve hac yaptı."},
 "tokens": [THUMMA(), MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  ILA(), MAJR("الْحِجَازِ", "hijaz", "propn"),
  MADI("فَحَجَّ", "hajja", ["doubled-verbs"], hidden=True, punct=".")]})
S4.append({"id": "s5", "translation": {
  "en": "His solitude lasted about ten years.",
  "tr": "İnzivası on yıl kadar sürdü."},
 "tokens": [MADI("وَدَامَتْ", "dama", ["hollow-verbs", "al-fil-al-tamm-wal-naqis"], fem=True,
       note_ar=" — وَدَامَ هُنَا تَامٌّ بِمَعْنَى «اسْتَمَرَّ» لَا خَبَرَ لَهُ" + FAIL_BAAD[0], note_en=" — دَامَ here is COMPLETE (tāmm), «to last», and takes no predicate" + FAIL_BAAD[1], note_tr=" — dâme burada tâmdır, «sürdü» anlamında; haber almaz" + FAIL_BAAD[2]),
  ENC_NOUN("عُزْلَتُهُ", "uzla", "هُ", "fail"),
  tok("نَحْوَ", "nahw", "noun", ["maful-fih", "idafa-definiteness"],
      "نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — نَابَ عَنِ الظَّرْفِ لِإِضَافَتِهِ إِلَى عَدَدِ الزَّمَانِ، وَمَعْنَاهُ هُنَا: قَرِيبًا مِنْ.",
      "Standing in for an adverb of time, in nasb and annexed — it takes the adverb's place because it is annexed to a count of time; here it means «about».",
      "Zaman zarfına nâib, mansûb, muzâf — zaman sayısına muzâf olduğu için zarfın yerini almıştır; burada «yaklaşık» anlamındadır."),
  MUDAF_ILAYH("عَشْرِ", "ashr", extra=["asma-al-adad-fil-kafiya"], note_ar="، مُضَافٌ — وَجَاءَ بِلَا تَاءٍ لِأَنَّ الْمَعْدُودَ (سَنَة) مُؤَنَّثٌ", note_en=", annexed — it has no ta because what is counted (سَنَة «year») is feminine", note_tr=", muzâf — sayılan (sene) müennes olduğu için tâsızdır"),
  SANA_MI(punct=".")]})
S4.append({"id": "s6", "translation": {
  "en": "Through those years he would withdraw into himself, set his heart right and remember God, seeking neither standing nor wealth, until there appeared to him of certainty what he had been seeking.",
  "tr": "O yıllar boyunca kendi başına çekiliyor, kalbini ıslah ediyor ve Allah'ı zikrediyordu; ne makam ne mal arıyordu; sonunda aradığı kesin bilgi ona göründü."},
 "tokens": [KANA_HID("وَكَانَ", note=HID_G),
  FI_ROLE((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَخْلُو»", "; the jarr phrase hangs on «withdraw»", "; câr-mecrûr «çekilirdi»ye müteallik")),
  TILKA("جَرٍّ", "jarr", "mecrûr"),
  BADAL("السِّنِينَ", "sana", "jarr", extra=["jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_en=", by the ya — declined like the sound masculine plural", note_tr="; cem-i müzekker sâlime mülhak olduğu için yâ ile"),
  MUDARI("يَخْلُو", "khala", naqis="و", **W(KH_KANA)),
  BI_NOUN("بِنَفْسِهِ", "nafs", "نَفْسِهِ", enc="هِ", note_ar=" — وَخَلَا بِنَفْسِهِ: انْفَرَدَ عَنِ النَّاسِ", note_en=" — to «be alone with oneself» is to withdraw from people", note_tr=" — «kendi nefsiyle baş başa kalmak», insanlardan uzaklaşmaktır", punct="،"),
  MUDARI("وَيُصْلِحُ", "aslaha", ["form-iv-verbs"], **W(ATF_CL)),
  ENC_NOUN("قَلْبَهُ", "qalb", "هُ", "maful", punct="،"),
  MUDARI("وَيَذْكُرُ", "dhakara", **W(ATF_CL)),
  ALLAH_MAF(punct="،"),
  LA_NAFIYA(),
  MUDARI("يَطْلُبُ", "talaba", **W(HALCL)),
  MAFUL("جَاهًا", "jah"),
  WA_LA_ZAIDA(),
  ATF("مَالًا", "mal", "noun", "nasb", punct="،"),
  HATTA_IBT(),
  MADI("ظَهَرَ", "zahara", **W(FAIL_BAAD)),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"),
  MINA_ROLE((" — لِبَيَانِ الْجِنْسِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «مَا» مُقَدَّمٍ عَلَيْهِ", "; it explains the kind, and the jarr phrase hangs on an omitted hal of «what», set before it", "; cinsi açıklar; câr-mecrûr «mâ»dan öne alınmış mahzûf hâle müteallik")),
  MAJR("الْيَقِينِ", "yaqin"),
  MA_MAWSULA("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail"]),
  KANA_HID("كَانَ", note=SILA_G),
  MUDARI("يَطْلُبُهُ", "talaba", enc="هُ", note_ar="، وَهِيَ الْعَائِدُ عَلَى «مَا»" + KH_KANA[0], note_en=", the one that returns to «what»" + KH_KANA[1], note_tr="; «mâ»ya dönen râbıt odur" + KH_KANA[2], punct=".")]})

# ---- Chapter 5 — الْعِلْمُ وَالْعَمَلُ ----
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Then he returned to teaching at Nīshāpūr; but he did not come back to it the way he had left it.",
  "tr": "Sonra Nîşâbur'da öğretmeye döndü; fakat ona, onu bıraktığı hâliyle dönmedi."},
 "tokens": [THUMMA(), MADI("رَجَعَ", "rajaa", hidden=True),
  ILA(), MAJR("التَّعْلِيمِ", "talim"),
  BI_TOWN("بِنَيْسَابُورَ", "naysabur", "نَيْسَابُورَ", AJAM_TOWN, punct="،"),
  INNA_ENC("وَلَكِنَّهُ", "هُ", " («o»)"),
  LAM_JAZM("لَمْ"),
  JAZM_V("يَرْجِعْ", "rajaa", hidden="هُوَ", note_ar=KH_LAKIN_CL[0], note_en=KH_LAKIN_CL[1], note_tr=KH_LAKIN_CL[2]),
  JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)", note_ar=" — وَالْهَاءُ لِلتَّعْلِيمِ", note_en=" — «it» is teaching", note_tr=" — zamir öğretmeye döner"),
  KAMA(),
  ENC_MADI("تَرَكَهُ", "taraka", "هُ", hidden=True, note_ar=" — وَالْهَاءُ لِلتَّعْلِيمِ، وَالْجُمْلَةُ صِلَةُ «مَا» الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا", note_en=" — «it» is teaching; the clause is the ṣila of the masdar-making مَا and has no seat", note_tr=" — zamir öğretmeye döner; cümle masdariyye mâ'nın sılasıdır, mahalli yoktur", punct=".")]})
S5.append({"id": "s2", "translation": {
  "en": "Before, he had taught while he loved standing; now he came to teach having left it behind.",
  "tr": "Daha önce makamı severek ders veriyordu; artık onu terk etmiş olarak ders verir oldu."},
 "tokens": [tok("فَقَدْ", "qad", "part", ["qad-harf"], "الْفَاءُ لِلِاسْتِئْنَافِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The fa opens the explanation; قَدْ affirms the past verb after it.", "Fâ isti'nâf içindir; kad tahkîk harfidir.",
      segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")]),
  KANA_HID("كَانَ", note=HID_G),
  MUDARI("يُعَلِّمُ", "allama", ["form-ii-verbs"], **W(KH_KANA)),
  MIN(),
  tok("قَبْلُ", "qablu", "noun", ["maful-fih", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "huruf-jarr"],
      "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ — قُطِعَ عَنِ الْإِضَافَةِ لَفْظًا وَنُوِيَ مَعْنَاهَا (أَيْ: مِنْ قَبْلِ ذٰلِكَ).",
      "An adverb of time built on damma, in the seat of jarr after مِنْ — cut off from its annexation in wording while its sense is kept («before that»).",
      "Zaman zarfı, damme üzere mebnî, min ile mahallen mecrûr — lafzen izâfetten kesilmiş, mânâsı niyet edilmiştir («ondan önce»)."),
  PRON_MUB("وَهُوَ", "huwa", pre="hal"),
  MUDARI("يُحِبُّ", "ahabba", ["form-iv-verbs", "doubled-verbs"], **W(KH_MUB_CL)),
  MAFUL("الْجَاهَ", "jah", punct="،"),
  SARA_HID("فَصَارَ", note=HID_G),
  MUDARI("يُعَلِّمُ", "allama", ["form-ii-verbs"], **W(KH_SARA)),
  WA_QAD(),
  ENC_MADI("تَرَكَهُ", "taraka", "هُ", hidden=True, note_ar=" — وَالْهَاءُ لِلْجَاهِ", note_en=" — «it» is the standing", note_tr=" — zamir makama döner", punct=".")]})
S5.append({"id": "s3", "translation": {
  "en": "Then he left teaching and went back to his home town; there he kept to his house, giving himself to worship and to teaching those who came to him, until he died there.",
  "tr": "Sonra öğretmeyi bıraktı ve memleketine döndü; evine kapandı, ibadete ve kendisine gelenlere ders vermeye yöneldi; nihayet orada vefat etti."},
 "tokens": [THUMMA(), MADI("تَرَكَ", "taraka", hidden=True), MAFUL("التَّعْلِيمَ", "talim"),
  MADI("وَرَجَعَ", "rajaa", hidden=True),
  ILA(), ENC_NOUN("بَلَدِهِ", "balad", "هِ", "majr", punct="،"),
  MADI("فَلَزِمَ", "lazima", hidden=True),
  ENC_NOUN("بَيْتَهُ", "bayt", "هُ", "maful", punct="،"),
  MADI("وَأَقْبَلَ", "aqbala", ["form-iv-verbs"], hidden=True),
  ALA(), MAJR("الْعِبَادَةِ", "ibada"),
  PREP("وَعَلَى", "ala", " — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى «عَلَى الْعِبَادَةِ»", "; the jarr phrase is conjoined to «to worship»", "; câr-mecrûr «ibadete»ye ma'tûf", gloss_tr="«üzerine»"),
  MAJR("تَعْلِيمِ", "talim", **W(MUDAF)),
  MAN_ONE("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"]),
  ENC_MADI("قَصَدَهُ", "qasada", "هُ", hidden=True, note_ar="؛ وَالْفَاعِلُ يَعُودُ عَلَى «مَنْ»، وَالْهَاءُ لِلْغَزَالِيِّ" + SILA_[0], note_en="; the hidden doer returns to «those who», and «him» is al-Ghazālī" + SILA_[1], note_tr="; gizli fâil «men»e, zamir Gazzâlî'ye döner" + SILA_[2], punct="،"),
  HATTA_IBT(), MADI("مَاتَ", "mata-die", ["hollow-verbs"], hidden=True),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («orada»)", note_ar=" — وَالضَّمِيرُ لِبَلَدِهِ", note_en=" — «it» is his home town", note_tr=" — zamir memleketine döner", punct=".")]})
S5.append({"id": "s4", "translation": {
  "en": "By my life, he learned in his solitude what he had not learned in his school.",
  "tr": "Ömrüme andolsun, inzivasında, medresesinde öğrenmediğini öğrendi."},
 "tokens": [LAAMRI(), LAQAD(),
  MADI("تَعَلَّمَ", "taallama", ["form-v-verbs"], hidden=True),
  FI(), ENC_NOUN("عُزْلَتِهِ", "uzla", "هِ", "majr"),
  MA_MAF(),
  LAM_JAZM("لَمْ"),
  tok("يَتَعَلَّمْهُ", "taallama", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-v-verbs", "al-bariz-al-muttasil", "maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَهِيَ الْعَائِدُ عَلَى «مَا»" + SILA_[0] + ".",
      "Present verb in jazm by لَمْ, its sign the sukun; the doer is the hidden «he», and the attached pronoun is its object, in the seat of nasb — the one that returns to «what»" + SILA_[1] + ".",
      "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli zamir «o»; bitişik zamir mef'ûlün bih, mahallen mansûb — «mâ»ya dönen râbıt odur" + SILA_[2] + ".",
      segments=[seg("يَتَعَلَّمْ", "taallama", "verb"), seg("هُ", "pron-3ms", "pron")]),
  FI(), ENC_NOUN("مَدْرَسَتِهِ", "madrasa", "هِ", "majr", punct=".")]})
S5.append({"id": "s5", "translation": {
  "en": "Here was a man who had reached the utmost of knowledge, and then learned that knowledge alone does not suffice.",
  "tr": "İşte bu, ilmin son noktasına ulaşmış, sonra da ilmin tek başına yetmediğini öğrenmiş bir adamdı."},
 "tokens": [tok("فَهٰذَا", "hadha", "pron", ["asma-al-ishara", "mubtada-khabar"],
      "الْفَاءُ لِلِاسْتِئْنَافِ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "The fa opens the closing word; «this» is a demonstrative built on sukun, in the seat of raf' as the mubtada.",
      "Fâ isti'nâf içindir; «bu» işaret ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû.",
      segments=[seg("فَ", "fa", "conj"), seg("هٰذَا", "hadha", "pron")]),
  KHABAR("رَجُلٌ", "rajul"),
  MADI("بَلَغَ", "balagha", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«رَجُلٌ»", note_en="; the clause qualifies «a man», in the seat of raf'", note_tr="; cümle «adam»ın na'tı, mahallen merfû"),
  MINA_ROLE((" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «غَايَتَهُ» مُقَدَّمٍ عَلَيْهِ", "; the jarr phrase hangs on an omitted hal of «its utmost», set before it", "; câr-mecrûr «son noktası»ndan öne alınmış mahzûf hâle müteallik")),
  MAJR("الْعِلْمِ", "ilm"),
  ENC_NOUN("غَايَتَهُ", "ghaya", "هُ", "maful", note_ar=" — وَالْهَاءُ لِلْعِلْمِ", note_en=" — «its» is knowledge's", note_tr=" — zamir ilme döner", punct="،"),
  THUMMA(),
  MADI("عَلِمَ", "alima", hidden=True, note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «بَلَغَ»", note_en="; the clause is conjoined to «reached»", note_tr="; cümle «ulaştı»ya ma'tûf"),
  ANNA_X(SADDA("عَلِمَ", "learned", "öğrendi")),
  tok("الْعِلْمَ", "ilm", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, in nasb.", "Enne'nin ismi, mansûb."),
  tok("وَحْدَهُ", "wahda", "noun", ["hal", "idafa-definiteness", "al-bariz-al-muttasil"],
      "حَالٌ مِنَ «الْعِلْمَ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَوَحْدَهُ لَا يَقَعُ إِلَّا حَالًا.",
      "The hal «alone», of «knowledge», in nasb and annexed to the pronoun «it»; وَحْدَهُ is only ever a hal.",
      "«İlim»den hâl «tek başına», mansûb; «o» zamirine muzâf — vahdehû yalnız hâl olarak gelir.",
      segments=[seg("وَحْدَ", "wahda", "noun"), seg("هُ", "pron-3ms", "pron")]),
  LA_NAFIYA(),
  MUDARI("يَكْفِي", "kafa", naqis="ي", note_ar="، يَعُودُ عَلَى الْعِلْمِ" + KH_ANNA_CL[0], note_en=" (knowledge)" + KH_ANNA_CL[1], note_tr=" (ilim)" + KH_ANNA_CL[2], punct=".")]})
S5.append({"id": "s6", "translation": {
  "en": "Knowledge profits the one who holds it only through action.",
  "tr": "İlim, sahibine ancak amelle fayda verir."},
 "tokens": [WA_MA("istinaf"),
  MUDARI_DF("يَنْفَعُ", "nafaa"),
  FAIL("الْعِلْمُ", "ilm"),
  ENC_NOUN("صَاحِبَهُ", "sahib", "هُ", "maful", note_ar=" — وَالْهَاءُ لِلْعِلْمِ", note_en=" — «its» is knowledge's", note_tr=" — zamir ilme döner"),
  ILLA_HASR(),
  BI_NOUN("بِالْعَمَلِ", "amal-work", "الْعَمَلِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَنْفَعُ»، وَهُوَ الْمَقْصُورُ عَلَيْهِ", note_en="; the jarr phrase hangs on «profits», and it is what the statement is restricted TO", note_tr=" — câr-mecrûr «fayda verir»e müteallik; hüküm ona hasredilmiştir", punct=".")]})
S5.append({"id": "s7", "translation": {
  "en": "For knowledge and action — neither of them is complete except with the other.",
  "tr": "Zira ilim ve amel: ikisinden biri ancak ötekiyle tamamlanır."},
 "tokens": [tok("فَالْعِلْمُ", "ilm", "noun", ["mubtada-khabar"],
      "الْفَاءُ لِلِاسْتِئْنَافِ، وَالْعِلْمُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The fa opens the closing word; «knowledge» is the mubtada, in raf'.", "Fâ isti'nâf içindir; «ilim» mübtedâ, merfû.",
      segments=[seg("فَ", "fa", "conj"), seg("الْعِلْمُ", "ilm", "noun")]),
  ATF("وَالْعَمَلُ", "amal-work", "noun", "raf"),
  LA_NAFIYA(),
  MUDARI_DF("يَتِمُّ", "tamma", extra=["doubled-verbs"], note_ar=KH_MUB_CL[0], note_en=KH_MUB_CL[1], note_tr=KH_MUB_CL[2]),
  ENC_NOUN("أَحَدُهُمَا", "ahad", "هُمَا", "fail", note_ar=" — وَالضَّمِيرُ رَابِطٌ يَعُودُ عَلَى الْمُبْتَدَأِ وَمَا عُطِفَ عَلَيْهِ", note_en=" — the pronoun «the two of them» ties the clause back to the mubtada and what is conjoined to it", note_tr=" — zamir mübtedâya ve ona ma'tûf olana dönen râbıttır"),
  ILLA_HASR(),
  BI_NOUN("بِالْآخَرِ", "akhar", "الْآخَرِ", extra=["mamnu-min-sarf"], note_ar=" — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِدُخُولِ «الْ» عَلَيْهِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَتِمُّ»، وَهُوَ الْمَقْصُورُ عَلَيْهِ",
       note_en="; a diptote that takes kasra here because it carries «al-»; the jarr phrase hangs on «is complete», and it is what the statement is restricted TO",
       note_tr=" — gayr-i munsarif iken «el» aldığı için kesre ile mecrûr; câr-mecrûr «tamamlanır»a müteallik; hüküm ona hasredilmiştir", punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs", "rubai-babs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            if DERIVED & set(t.get("grammar", [])) and "thulathi-mujarrad-babs" in t["grammar"]:
                t["grammar"].remove("thulathi-mujarrad-babs")

# ---- the lexicon: every key by lemma identity from the shelf; the entries below are new -----------------------------------
PREF = ["al-kafiya", "al-amana-wa-al-khashaba", "ashab-al-ghar", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "wasiyyat-abi-yusuf-l5", "adam-wa-iblis",
        "al-asad-wa-al-far", "al-asad-wa-al-arnab", "juha-wa-al-himar", "aqaid-ahl-al-sunna", "talkhis-al-miftah", "qisas-al-nabiyyin-2",
        "salah-al-din-wa-al-quds", "fath-al-qustantiniyya", "alb-arslan-wa-malazgird", "ibn-khaldun-wa-timur"]
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
# where the shelf holds one key in several packages, take the entry whose gloss fits this story
FORCE = {"man-mawsula": "talkhis-al-miftah", "ma-mawsula": "al-asad-wa-al-arnab", "hadha": "ibn-khaldun-wa-timur", "dhalika": "talkhis-al-miftah",
         "hadhihi": "wasiyyat-abi-hanifa-samti", "ab": "abu-hanifa-wa-al-safina", "alim-scholar": "abu-hanifa-wa-al-safina", "kalam": "wasiyyat-abi-yusuf-l5",
         "ilm": "al-bukhari-fi-baghdad", "nas": "salah-al-din-wa-al-quds", "bilad": "alb-arslan-wa-malazgird", "sana": "salah-al-din-wa-al-quds",
         "amma": "al-bukhari-fi-baghdad", "an-masdariyya": "abu-hanifa-wa-al-safina", "an": "abu-hanifa-wa-al-safina", "thamani": "al-kafiya",
         "akhar": "al-amana-wa-al-khashaba", "amal-work": "talkhis-al-miftah", "sara-travel": "abu-hanifa-wa-al-safina", "qadara-able": "alb-arslan-wa-malazgird",
         "kitab": "al-bukhari-fi-baghdad", "baghdad": "al-bukhari-fi-baghdad", "dimashq": "ibn-khaldun-wa-timur", "bayt-al-maqdis": "salah-al-din-wa-al-quds",
         "maqdis": "salah-al-din-wa-al-quds", "bayt": "salah-al-din-wa-al-quds", "rujuu": "ibn-khaldun-wa-timur", "zaman": "abu-hanifa-wa-al-safina",
         "kam": "ibn-khaldun-wa-timur", "baynama": "alb-arslan-wa-malazgird", "innama": "ibn-khaldun-wa-timur", "amr-qasam": "alb-arslan-wa-malazgird",
         "arbaumia": "alb-arslan-wa-malazgird", "wara": "alb-arslan-wa-malazgird", "la-nafiya-lil-jins": "al-bukhari-fi-baghdad", "taifa": "abu-hanifa-wa-al-safina",
         "talib": "al-usul-al-munifa", "sham": "ibn-khaldun-wa-timur", "lakinna": "al-asad-wa-al-far"}
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
 "ghazali": {"lemma": "الْغَزَالِيّ", "pos": "propn", "gloss": {"en": "al-Ghazālī — Abū Ḥāmid Muḥammad ibn Muḥammad (450–505 / 1058–1111), the Shāfiʿī jurist, theologian and ṣūfī of Ṭūs, author of al-Munqidh min al-ḍalāl and Iḥyāʾ ʿulūm al-dīn; a nisba, best known with a light zāy (some read al-Ghazzālī)", "tr": "Gazzâlî — Ebû Hâmid Muhammed b. Muhammed (450–505 / 1058–1111), Tûslu Şâfiî fakih, kelâmcı ve sûfî; el-Munkız mine'd-dalâl ile İhyâü ulûmi'd-dîn'in müellifi; bir nisbe, en meşhur zabtında zâ şeddesizdir (bazıları el-Gazzâlî okur)"}, "level": 6},
 "hamid": {"lemma": "حَامِد", "pos": "propn", "gloss": {"en": "Ḥāmid — a man's name (in the kunya Abū Ḥāmid); fully declined", "tr": "Hâmid — erkek adı (Ebû Hâmid künyesinde); munsarif"}, "level": 5},
 "madrasa": {"lemma": "مَدْرَسَة", "root": "د ر س", "pos": "noun", "gloss": {"en": "a school, a college of learning (noun of place from دَرَسَ)", "tr": "medrese, okul (derase'den mekân ismi)"}, "level": 4},
 "nizamiyya": {"lemma": "النِّظَامِيَّة", "pos": "noun", "gloss": {"en": "the Niẓāmiyya — the colleges founded by the Seljuk vizier Niẓām al-Mulk, chief among them the one in Baghdad (a nisba)", "tr": "Nizâmiye — Selçuklu veziri Nizâmülmülk'ün kurduğu medreseler; en meşhuru Bağdat'takidir (nisbe)"}, "level": 6},
 "batiniyya": {"lemma": "الْبَاطِنِيَّة", "pos": "noun", "gloss": {"en": "the Bāṭiniyya — the sect that claimed an inner (bāṭin) meaning behind the revealed texts, taught by an infallible imam (a nisba)", "tr": "Bâtıniyye — nasların ardında gizli (bâtın) bir mânâ bulunduğunu ve bunun masum bir imamdan öğrenileceğini iddia eden fırka (nisbe)"}, "level": 6},
 "sufiyya": {"lemma": "الصُّوفِيَّة", "pos": "noun", "gloss": {"en": "the Ṣūfīs — the people of the path of purifying the heart (a collective nisba)", "tr": "sûfîler, mutasavvıflar — kalbi arındırma yolunun ehli (topluluk nisbesi)"}, "level": 5},
 "uzla": {"lemma": "عُزْلَة", "root": "ع ز ل", "pos": "noun", "gloss": {"en": "solitude, withdrawal from people", "tr": "inziva, insanlardan uzaklaşma"}, "level": 5},
 "naysabur": {"lemma": "نَيْسَابُور", "pos": "propn", "gloss": {"en": "Nīshāpūr — a great city of Khurāsān (a diptote: a foreign proper name)", "tr": "Nîşâbur — Horasan'ın büyük şehirlerinden (gayr-i munsarif: yabancı özel isim)"}, "level": 6},
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
def REGLOSS(k, en, tr): GLOSS[k] = {**GLOSS[k], "gloss": {"en": en, "tr": tr}}
REGLOSS("kalam", "speech; عِلْمُ الْكَلَامِ — kalām, the science of the articles of faith and their proofs", "söz; عِلْمُ الْكَلَامِ — kelâm ilmi, akaid ve delilleri ilmi")
REGLOSS("faylasuf", "a philosopher; pl. فَلَاسِفَة", "filozof, feylesof; çoğ. فَلَاسِفَة")
REGLOSS("tabib", "a physician; pl. أَطِبَّاء (a diptote)", "hekim, tabip; çoğ. أَطِبَّاء (gayr-i munsarif)")
REGLOSS("taifa", "a group, a party; pl. طَوَائِف (a diptote)", "topluluk, zümre; çoğ. طَوَائِف (gayr-i munsarif)")
REGLOSS("kitab", "a book; pl. كُتُب", "kitap; çoğ. كُتُب")
REGLOSS("tariq", "a way, a road, a path; pl. طُرُق", "yol; çoğ. طُرُق")
REGLOSS("shahr", "a month; pl. أَشْهُر", "ay; çoğ. أَشْهُر")
REGLOSS("hijaz", "the Ḥijāz — western Arabia, the land of Mecca and Medina", "Hicaz — Arabistan'ın batısı, Mekke ve Medine diyarı")
REGLOSS("hana", "to be light, to be easy (عَلَى: for someone); (of words) to grow light", "hafif olmak, (birine — عَلَى) kolay gelmek")
REGLOSS("khala", "to be empty, devoid; خَلَا بِنَفْسِهِ: to withdraw, to be alone with oneself", "boş olmak; خَلَا بِنَفْسِهِ: kendi başına çekilmek, yalnız kalmak")
REGLOSS("anfaqa", "to spend (wealth); to give it away", "(mal) harcamak, dağıtmak")
REGLOSS("amsaka", "to hold, hold back; (passive أُمْسِكَ) to be held back", "tutmak, alıkoymak; (meçhul أُمْسِكَ) tutulmak")
REGLOSS("daufa", "to be weak; ضَعُفَ عَنْ: to be too weak for", "zayıf olmak; ضَعُفَ عَنْ: bir şeye güç yetirememek")
REGLOSS("nahw", "direction, side; (annexed to a number) about, approximately", "yön, taraf; (bir sayıya muzâf) yaklaşık, kadar")
REGLOSS("talim", "teaching", "öğretme, ders verme")
REGLOSS("aqbala", "to come forward; أَقْبَلَ عَلَى: to turn to, to give oneself to", "yönelmek; أَقْبَلَ عَلَى: bir şeye yönelip kendini vermek")
REGLOSS("jah", "standing, rank, prestige", "itibar, makam, nüfuz")
REGLOSS("madhhab", "a way of thought, a doctrine; a school of law", "mezhep, görüş; fıkıh mezhebi")
REGLOSS("wajada", "to find; (with two objects) to find to be", "bulmak; (iki mef'ûlle) … olarak bulmak")
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
 "title": {"ar": "الْغَزَالِيُّ وَالْعُزْلَةُ", "en": "Al-Ghazālī and Solitude", "tr": "Gazzâlî ve İnziva"},
 "subtitle": {"ar": "عَالِمٌ يَتْرُكُ مَجْلِسَهُ فِي بَغْدَادَ طَلَبًا لِلْيَقِينِ، ثُمَّ يَرْجِعُ — قِصَّةٌ لِلْمُسْتَوَى السَّادِسِ",
              "en": "A scholar leaves his chair in Baghdad in search of certainty, and comes back — a story for the sixth level",
              "tr": "Kesin bilgi arayışıyla Bağdat'taki kürsüsünü bırakan ve geri dönen bir âlim — altıncı seviye için bir hikâye"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى السَّادِسُ) لِخَبَرِ أَزْمَةِ أَبِي حَامِدٍ الْغَزَالِيِّ وَخُرُوجِهِ مِنْ بَغْدَادَ سَنَةَ ٤٨٨ هـ وَعُزْلَتِهِ وَرُجُوعِهِ، عَلَى مَا رَوَاهُ هُوَ نَفْسُهُ فِي «الْمُنْقِذِ مِنَ الضَّلَالِ»، وَمَا ذَكَرَهُ الْمُتَرْجِمُونَ لَهُ مِنْ رُجُوعِهِ إِلَى التَّدْرِيسِ بِنَيْسَابُورَ ثُمَّ إِلَى بَلَدِهِ (ابْنُ عَسَاكِرَ فِي «تَبْيِينِ كَذِبِ الْمُفْتَرِي» نَقْلًا عَنْ عَبْدِ الْغَافِرِ الْفَارِسِيِّ، وَالسُّبْكِيُّ فِي «طَبَقَاتِ الشَّافِعِيَّةِ الْكُبْرَى»، وَابْنُ خَلِّكَانَ فِي «وَفَيَاتِ الْأَعْيَانِ»). النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنَ «الْمُنْقِذِ» وَلَا مِنْ غَيْرِهِ، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا قَوْلٌ يُنْسَبُ إِلَى الْغَزَالِيِّ؛ وَتُرِكَتِ التَّفَاصِيلُ الْمُخْتَلَفُ فِيهَا.",
  "en": "ORIGINAL Level-6 graded Arabic in a classical narrative register: the crisis of Abū Ḥāmid al-Ghazālī, his leaving Baghdad in 488 AH / 1095 CE, his years of solitude and his return, RETOLD FREELY along the well-attested core of his own account in al-Munqidh min al-ḍalāl, with his return to teaching at Nīshāpūr and his last years in his home town Ṭūs as the biographers give them (ʿAbd al-Ghāfir al-Fārisī as cited by Ibn ʿAsākir in Tabyīn kadhib al-muftarī; al-Subkī, Ṭabaqāt al-Shāfiʿiyya al-kubrā; Ibn Khallikān, Wafayāt al-aʿyān). No sentence is a quotation from al-Munqidh or from any other source; no āya or ḥadīth is quoted; no words are put in al-Ghazālī's mouth — his inner states are told in the narrator's words, and the closing reflection on knowledge and action is the narrator's. Left out: the exact length of each stay, the stories of meetings on the journey, the months and days of the crisis, the arrangements for his family, the vizier who called him back to Nīshāpūr, the buildings by his house, the date of his death, and every disputed anecdote. Ṭūs is not named in the text («his home town»). The vowelling of the nisba (al-Ghazālī / al-Ghazzālī) and of Nīshāpūr is listed for the scholar's review.",
  "tr": "ÖZGÜN 6. seviye Arapça, klasik anlatı üslûbunda: Ebû Hâmid el-Gazzâlî'nin buhranı, 488 h. / 1095 m. yılında Bağdat'tan ayrılışı, inziva yılları ve dönüşü; kendi anlatısı olan el-Munkız mine'd-dalâl'ın sağlam çekirdeğine bağlı kalınarak, Nîşâbur'da yeniden ders vermesi ile memleketi Tûs'taki son yılları ise biyografi yazarlarının aktardığı şekliyle (İbn Asâkir'in Tebyînü kezibi'l-müfterî'de Abdülgâfir el-Fârisî'den naklettiği; Sübkî, Tabakâtü'ş-Şâfiiyyeti'l-kübrâ; İbn Hallikân, Vefeyâtü'l-a'yân) SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle el-Munkız'dan veya başka bir kaynaktan alıntı değildir; hiçbir âyet veya hadis aktarılmamış, Gazzâlî'nin ağzına söz konmamıştır — iç hâlleri anlatıcının sözleriyle anlatılır; ilim ve amel üzerine kapanış düşüncesi de anlatıcınındır. Dışarıda bırakılanlar: her duraktaki kalış süresi, yolculuktaki karşılaşma hikâyeleri, buhranın ayları ve günleri, ailesi için yaptığı düzenlemeler, onu Nîşâbur'a çağıran vezir, evinin yanındaki binalar, vefat tarihi ve ihtilaflı her rivayet. Tûs metinde adıyla anılmaz («memleketi»). Nisbenin (Gazâlî / Gazzâlî) ve Nîşâbur'un zabtı âlim incelemesine bırakılmıştır.",
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
