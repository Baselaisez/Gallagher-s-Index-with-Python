"""Author content/samples/salah-al-din-wa-al-quds — «صَلَاحُ الدِّينِ وَالْقُدْسُ», an ORIGINAL historical story at Level 6 (Master).

ORIGINAL graded Arabic in a classical narrative register: Jerusalem in Frankish hands since the end of the fifth century AH,
the kings who hoped for it, Nūr al-Dīn's minbar, Saladin's union of Egypt and Syria; the year 583 / 1187 — Ḥiṭṭīn, the
march to Jerusalem, the siege, the terms (each inhabitant ransomed for a fixed sum within a fixed term), the surrender on
Friday 27 Rajab; the clemency set against the slaughter of 492 / 1099; the cross taken down from the Dome of the Rock, the
two sanctuaries cleansed, Nūr al-Dīn's minbar brought from Aleppo, the first Friday prayer. The event is told by Ibn Shaddād
(al-Nawādir al-Sulṭāniyya), ʿImād al-Dīn al-Iṣfahānī (al-Fatḥ al-Qussī) and Ibn al-Athīr (al-Kāmil); it is RETOLD FREELY
here — no sentence is a quotation from them, no āya or ḥadīth is quoted, no words are put in a historical person's mouth,
and the disputed details (ransom figures, numbers of the slain, the dating of the Miʿrāj) are left out.

Five chapters, thirty sentences. The Level-6 constructions: long periodic sentences; فَبَيْنَمَا … إِذْ …; ثُمَّ إِنَّهُ; ḥaṣr by
إِنَّمَا and by مَا … إِلَّا (including مَا … إِلَّا وَقَدْ, the ḥāl after the emptied exception); كَمِ الْخَبَرِيَّةُ (twice); the oath
لَعَمْرِي; the mafʿūl muṭlaq and its deputies (قِتَالًا شَدِيدًا، كُلَّ مَبْلَغٍ، أَشَدَّ الْحِصَارِ); tamyīz (نَفْسًا، فَرَحًا، صَنِيعًا);
the mafʿūl lahu (رَجَاءَ، رَحْمَةً); kāna tāmma (فَلَمَّا كَانَتْ سَنَةُ …); the extra bāʾ in the predicate of a negated kāna;
حَتَّى + the subjunctive and حَتَّى إِذَا; the conditional مَنْ; ḥāl clauses with وَ / وَقَدْ.

Written on the authoring kit (story_kit.py). Every key is reused by lemma identity from the shelf except the new entries in
NEW_GLOSS (place names, سُور، حِصَار، مَبْلَغ، صَنِيع، بَيْنَمَا، عَمْر of the oath, the verb حَاصَرَ with a generated Form-III
paradigm, and five name-phrases).  Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_salah_al_din_wa_al_quds.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "salah-al-din-wa-al-quds"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

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

MUDAF = ("، مُضَافٌ", ", annexed", ", muzâf")
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
DIPT_F2 = ("، عَلَمٌ مُؤَنَّثٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", " — a feminine proper name (a town), barred from tanwin", " — müennes özel isim (şehir adı), gayr-i munsarif")
HITTIN = (" — عَلَمٌ عَلَى مَوْضِعٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ بِتَأْوِيلِ الْبُقْعَةِ",
          " — the name of a place, barred from tanwin (a proper name read as feminine, «the spot»)",
          " — yer adı; «bölge» anlamıyla müennes sayılan özel isim olduğu için gayr-i munsarif")
KH_KANA = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause fills the seat of nasb as the predicate of كَانَ", "; cümle kâne'nin haberi olarak mahallen mansûb")
KH_INNA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the clause fills the seat of raf' as the predicate of إِنَّ", "; cümle inne'nin haberi olarak mahallen merfû")
HALCL = (" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", "; the clause is a hal, in the seat of nasb", "; cümle hâl olarak mahallen mansûb")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
AID = ("، وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", "; the attached pronoun is the one that returns to the relative", "; bitişik zamir mevsûle dönen râbıttır")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")

# ---- the names that recur ----------------------------------------------------------------------------------------
SALAH_F = lambda punct=None: PH(FAIL("صَلَاحُ", "salah", "propn", note_ar=MUDAF[0] + " — صَلَاحُ الدِّينِ لَقَبٌ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ", note_en=MUDAF[1] + " — Ṣalāḥ al-Dīn is an honorific built as an idafa", note_tr=MUDAF[2] + " — Selâhuddîn, izâfet terkibiyle kurulmuş lakaptır", punct=punct), "salah-al-din")
SALAH_J = lambda punct=None: PH(MAJR("صَلَاحِ", "salah", "propn", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2], punct=punct), "salah-al-din")
SALAH_MI = lambda punct=None: PH(MUDAF_ILAYH("صَلَاحِ", "salah", "propn", note_ar=MUDAF[0], note_en=", itself annexed", note_tr=", kendisi de muzâf", punct=punct), "salah-al-din")
NUR_F = lambda punct=None: PH(FAIL("نُورُ", "nur", "propn", note_ar=MUDAF[0] + " — نُورُ الدِّينِ لَقَبٌ مُرَكَّبٌ تَرْكِيبَ إِضَافَةٍ", note_en=MUDAF[1] + " — Nūr al-Dīn is an honorific built as an idafa", note_tr=MUDAF[2] + " — Nûreddîn, izâfet terkibiyle kurulmuş lakaptır", punct=punct), "nur-al-din")
NUR_ISMK = lambda punct=None: PH(ISMK("نُورُ", "nur", "propn", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2], punct=punct), "nur-al-din")
DIN_MI = lambda punct=None: MUDAF_ILAYH("الدِّينِ", "din", punct=punct)
BAYT_ISMK = lambda: PH(ISMK("بَيْتُ", "bayt", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), "bayt-al-maqdis")
BAYT_J = lambda: PH(MAJR("بَيْتِ", "bayt", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), "bayt-al-maqdis")
BAYT_MAF = lambda: PH(MAFUL("بَيْتَ", "bayt", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), "bayt-al-maqdis")
BAYT_F = lambda: PH(FAIL("بَيْتُ", "bayt", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), "bayt-al-maqdis")
MAQDIS_MI = lambda punct=None: MUDAF_ILAYH("الْمَقْدِسِ", "maqdis", punct=punct)
AHL_SALIB = lambda role: [role("أَهْلُ" if role in (FAIL, ISMK) else "أَهْلَ" if role is MAFUL else "أَهْلِ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الصَّلِيبِ", "salib")]
MUSLIMUN_F = lambda punct=None: FAIL("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign="بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the waw, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için vâv ile", punct=punct)
R_MAJR = ("مَجْرُورٌ", "In jarr after the letter", "Cer harfiyle mecrûr", "huruf-jarr")
R_MI = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ", "The second term of the idafa, in jarr", "Muzâfun ileyh, mecrûr", "idafa-definiteness")
MUSLIMIN_J = lambda punct=None: SALIM_J("الْمُسْلِمِينَ", "muslim", R_MAJR, punct=punct)
MUSLIMIN_MI = lambda punct=None: SALIM_J("الْمُسْلِمِينَ", "muslim", R_MI, punct=punct)
BI_MUSLIMIN = lambda punct=None: tok("بِالْمُسْلِمِينَ", "bi", "prep", ["huruf-jarr", "jam-mudhakkar-salim"],
    "الْبَاءُ حَرْفُ جَرٍّ، وَالْمُسْلِمِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
    "The ba is a jarr letter; «the Muslims» is in jarr by the ya — a sound masculine plural.",
    "Bâ cer harfi; «Müslümanlar» cem-i müzekker sâlim olduğu için yâ ile mecrûr.", punct=punct,
    segments=[seg("بِ", "bi", "prep"), seg("الْمُسْلِمِينَ", "muslim", "noun")])
AQSA_J = lambda punct=None: tok("الْأَقْصَى", "aqsa", "noun", ["naat-sifa", "ism-maqsur-manqus", "ism-tafdil"],
    "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمُ تَفْضِيلٍ مَقْصُورٌ.",
    "An adjective agreeing with «the mosque», in jarr by a kasra estimated on the alif — a maqṣūr elative («the farthest»).",
    "Na't, elif üzerinde takdîrî kesre ile mecrûr — maksûr ism-i tafdîl («en uzak»).", punct=punct)

# ---- particles and frames the kit does not hold ---------------------------------------------------------------------
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
ILLA_HAL = lambda: tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "turuq-al-qasr", "qasr", "hal"],
    "إِلَّا أَدَاةُ حَصْرٍ — وَالِاسْتِثْنَاءُ مُفَرَّغٌ مِنْ عُمُومِ الْأَحْوَالِ، فَالْجُمْلَةُ بَعْدَهَا فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "إِلَّا restricts: the exception is emptied out of «every state», so the clause after it is a hal, in the seat of nasb («it did not set except in the state that …»).",
    "İllâ hasr edatıdır: istisnâ «bütün hâller»den müferrağdır; sonraki cümle hâl olarak mahallen mansûb («… hâlinden başka bir hâlde batmadı»).")
def WA_INNAMA(full="وَإِنَّمَا", pre="istinaf"):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "«ve» + "}[pre]
    return tok(full, "innama", "part", ["innama-kaffa", "qasr", "turuq-al-qasr"],
        pre_ar + "إِنَّمَا أَدَاةُ حَصْرٍ: إِنَّ كَفَّتْهَا مَا الزَّائِدَةُ عَنِ الْعَمَلِ — وَالْمَقْصُورُ عَلَيْهِ هُوَ الْمُؤَخَّرُ فِي الْكَلَامِ.",
        pre_en + "إِنَّمَا «only» is the tool of restriction: the extra مَا has stopped إِنَّ from governing — what is restricted TO comes last in the clause.",
        pre_tr + "innemâ hasr edatıdır: zâid mâ, inne'yi amelden alıkoymuştur — kendisine hasredilen şey cümlede sona gelir.",
        segments=[seg("وَ", "wa", "conj"), seg("إِنَّمَا", "innama", "part")])
def WA_MA(pre="atf"):
    pre_ar = {"istinaf": "الْوَاوُ لِلِاسْتِئْنَافِ، وَ", "atf": "الْوَاوُ عَاطِفَةٌ، وَ"}[pre]
    pre_en = {"istinaf": "The waw opens a new sentence; ", "atf": "The waw conjoins; "}[pre]
    pre_tr = {"istinaf": "Vâv isti'nâf içindir; ", "atf": "«ve» + "}[pre]
    return tok("وَمَا", "ma-nafiya", "part", ["la-nafiya"], pre_ar + "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", pre_en + "مَا negates and governs nothing.", pre_tr + "mâ nefiy harfi, amel etmez.",
        segments=[seg("وَ", "wa", "conj"), seg("مَا", "ma-nafiya", "part")])
FA_MA = lambda: tok("فَمَا", "ma-nafiya", "part", ["la-nafiya"], FA_AR + "مَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; مَا negates and governs nothing.", "«bunun üzerine» + mâ nefiy harfi, amel etmez.",
    segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")])
def ZARF_ENC(full, lex, enc, kind="مَكَانٍ", kind_en="place", kind_tr="mekân", punct=None, note_ar="", note_en="", note_tr=""):
    """بَيْنَهُ، تَحْتَهُ، دُونَهُ: a ẓarf annexed to its pronoun"""
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
def MAFUL_LAHU(full, lex, punct=None, note_ar="", note_en="", note_tr="", mudaf=False):
    return tok(full, lex, "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"] + (["idafa-definiteness"] if mudaf else []),
        "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ" + ("، مُضَافٌ" if mudaf else "") + " — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ" + note_ar + ".",
        "The maf'ul li-ajlih (object of cause), in nasb" + (" and annexed" if mudaf else "") + " — a masdar of the heart giving the reason for the act, sharing its time and its doer" + note_en + ".",
        "Mef'ûlün lieclih, mansûb" + (", muzâf" if mudaf else "") + " — fiilin sebebini bildiren kalbî masdar; fiille zamanda ve fâilde ortak" + note_tr + ".", punct=punct)
def TAMYIZ_NISBA(full, lex, asl_ar, asl_en, asl_tr, punct=None):
    return tok(full, lex, "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"],
        "تَمْيِيزُ نِسْبَةٍ مَنْصُوبٌ بِالْفَتْحَةِ — مُحَوَّلٌ عَنِ الْفَاعِلِ، وَالْأَصْلُ: " + asl_ar + ".",
        "A specifier of the relation (tamyiz al-nisba), in nasb — turned from the doer; the plain wording would be «" + asl_en + "».",
        "Nisbet temyîzi, mansûb — fâilden çevrilmiştir; asıl ifade: «" + asl_tr + "».", punct=punct)
def AN_MADI(full="أَنْ"):
    k = full.endswith("ِ")
    return tok(full, "an-masdariyya", "part", ["an-masdariyya"],
        "حَرْفٌ مَصْدَرِيٌّ مَبْنِيٌّ عَلَى السُّكُونِ" + ("، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ" if k else "") + "، دَخَلَ عَلَى الْمَاضِي فَلَمْ يَعْمَلْ فِي لَفْظِهِ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        "The masdar-making أَنْ" + (" (voweled with kasra before the hamzat al-waṣl)" if k else "") + "; before a PAST verb it changes nothing in its form — the clause it builds is annexed to «after», in the seat of jarr.",
        "Masdariyye en" + (" (iki sâkin karşılaştığı için kesre ile harekelendi)" if k else "") + "; mâzî fiile girdiği için lafzında amel etmez — müevvel masdar «sonra»ya muzâfun ileyh, mahallen mecrûr.")
def MAJHUL_FEM_K(full, lex, extra=None, hollow=False):
    """فَسُلِّمَتِ، وَأُقِيمَتِ: a passive past with the feminine ta voweled for the following ال"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    how = ("ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ عَيْنِهِ فَصَارَتْ عَيْنُهُ يَاءً", "its first letter takes damma and the letter before its middle radical a kasra, so the middle radical becomes ya", "evveli mazmûm, aynından önceki harf meksûr; ayn yâ'ya dönmüş") if hollow else \
          ("ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ", "its first letter takes damma and the letter before the last a kasra", "evveli mazmûm, âhirinden önceki harf meksûr")
    return tok(full, lex, "verb", ["naib-al-fail", "al-majhul-fil-kafiya"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — " + how[0] + " — وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
        en0 + "a past verb in the passive, built on fatha — " + how[1] + "; the ta marks the feminine and is voweled with kasra before the following ال.",
        tr0 + "meçhul mâzî, fetha üzere mebnî — " + how[2] + "; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.",
        segments=[sg, seg(stem, lex, "verb")] if sg else None)
def MAJHUL_HOLLOW(full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr=""):
    """وَأُزِيلَ: the passive past of a hollow Form IV"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, lex, "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "hollow-verbs", "form-iv-verbs"] + (extra or []),
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ عَيْنِهِ فَصَارَتْ عَيْنُهُ يَاءً" + note_ar + ".",
        en0 + "a past verb in the passive, built on fatha — its first letter takes damma and the letter before its middle radical a kasra, so the middle radical becomes ya" + note_en + ".",
        tr0 + "meçhul mâzî, fetha üzere mebnî — evveli mazmûm, aynından önceki harf meksûr; ayn yâ'ya dönmüş" + note_tr + ".",
        punct=punct, segments=[sg, seg(stem, lex, "verb")] if sg else None)
def NAIB_ENC(full, lex, enc, punct=None, note_ar="", note_en="", note_tr=""):
    return tok(full, lex, "noun", ["naib-al-fail", "idafa-definiteness", "al-bariz-al-muttasil"],
        "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" + note_ar + ".",
        "The deputy doer (na'ib al-fa'il), in raf'; annexed, and the attached pronoun is the second term of the idafa, in the seat of jarr" + note_en + ".",
        "Nâib-i fâil, merfû; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr" + note_tr + ".", punct=punct,
        segments=[seg(full[:-len(enc)], lex, "noun"), seg(enc, PRON[enc], "pron")])
def ALLADHI(case, of_ar, of_en, of_tr):
    seat = {"raf": ("رَفْعٍ", "raf'", "merfû"), "nasb": ("نَصْبٍ", "nasb", "mansûb"), "jarr": ("جَرٍّ", "jarr", "mecrûr")}[case]
    return tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"],
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat[0] + " نَعْتٌ " + of_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
        "A relative pronoun built on sukun, in the seat of " + seat[1] + " as the adjective of «" + of_en + "»; the clause after it is its ṣila.",
        "İsm-i mevsûl, sükûn üzere mebnî, «" + of_tr + "»nin na'tı olarak mahallen " + seat[2] + "; sonraki cümle sılasıdır.")
def MA_MAWSULA(seat_ar, seat_en, seat_tr, extra):
    return tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"] + extra,
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
        "A relative pronoun «what», built on sukun, in the seat of " + seat_en + "; the clause after it is its ṣila.",
        "İsm-i mevsûl «…-an şey», sükûn üzere mebnî, mahallen " + seat_tr + "; sonraki cümle sılasıdır.")
def DHALIKA(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + "، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ حَرْفُ خِطَابٍ.",
        "A demonstrative «that», built on sukun, in the seat of " + seat_en + "; the lam marks distance and the kaf is a particle of address.",
        "İşaret ismi «o», sükûn üzere mebnî, mahallen " + seat_tr + "; lâm uzaklık için, kâf hitap harfidir.", punct=punct)
BI_DHALIKA = lambda: tok("بِذٰلِكَ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
    "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَذٰلِكَ اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ.",
    "The ba of cause («at that, by that»); the demonstrative after it is built on sukun, in the seat of jarr.",
    "Sebebiyye bâ'sı («bununla»); işaret ismi sükûn üzere mebnî, mahallen mecrûr.",
    segments=[seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")])
KULLAHU = lambda punct=None: tok("كُلَّهُ", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
    "تَوْكِيدٌ مَعْنَوِيٌّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "A tawkid of meaning «the whole of it», in nasb like the object it strengthens; annexed to the pronoun, which fills the seat of jarr.",
    "Ma'nevî te'kîd «tamamını», pekiştirdiği mef'ûl gibi mansûb; zamire muzâf, zamir mahallen mecrûr.", punct=punct,
    segments=[seg("كُلَّ", "kull", "noun"), seg("هُ", "pron-3ms", "pron")])
AN_PREP = lambda role=("", "", ""): PREP("عَنْ", "an", *role, gloss_tr="«-den, adına»")
HAKADHA2 = lambda: tok("وَهٰكَذَا", "hakadha", "pron", ["asma-al-ishara", "huruf-tanbih", "maful-mutlaq"],
    "الْوَاوُ لِلِاسْتِئْنَافِ، وَهَا لِلتَّنْبِيهِ، وَالْكَافُ حَرْفُ جَرٍّ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِفَةٍ لِمَصْدَرٍ مَحْذُوفٍ، أَيْ: عَادَ عَوْدًا كَهٰذَا.",
    "The waw opens a new sentence; «and thus»: the hā of alerting, the kāf of likeness (a jarr letter) and the demonstrative in the seat of jarr — together they describe an omitted masdar («returned in a returning like this»).",
    "Vâv isti'nâf içindir; «işte böylece»: tenbih hâ'sı, teşbih kâfı (cer harfi) ve mahallen mecrûr işaret ismi — bütünü hazfedilmiş masdarın sıfatıdır («böyle bir dönüşle döndü»).",
    segments=[seg("وَ", "wa", "conj"), seg("هٰكَذَا", "hakadha", "pron")])

# ---- three verb shapes the kit does not hold ---------------------------------------------------------------------
def KANA_N(full="كَانَ", note=("", "", "")):
    t = KANA(full)
    return NOTE(t, *note)
def YAKUN():
    return tok("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "lam-jazim", "hollow-verbs"],
        "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ: يَكُونُ)، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
        "The defective present of كَانَ in jazm by لَمْ, its sign the sukun; its waw dropped where two quiescents met (from يَكُونُ). It raises its noun and puts its predicate in nasb.",
        "Kâne'nin nâkıs muzârii, lem ile meczûm, alâmeti sükûn; iki sâkin karşılaşınca vâvı düştü (aslı yekûnu). İsmini ref, haberini nasb eder.")
KANAT_TAMMA = lambda: tok("كَانَتْ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs"],
    "كَانَ هُنَا فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «جَاءَتْ» مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، يَكْتَفِي بِفَاعِلِهِ وَلَا خَبَرَ لَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ لَمَّا إِلَيْهَا.",
    "كَانَ here is COMPLETE (tāmma), meaning «came, arrived»: a past verb built on fatha, the ta marking the feminine; it is satisfied with a doer and takes no predicate — the clause is annexed to لَمَّا, in the seat of jarr.",
    "Kâne burada tâmmedir, «geldi» anlamında: fetha üzere mebnî mâzî, tâ te'nîs içindir; fâiliyle yetinir, haber almaz — cümle lemmâ'ya muzâfun ileyh, mahallen mecrûr.")
def MUDARI5_ENC(full, lex, enc, extra=None, punct=None, role=("", "", "")):
    """يَدْخُلُونَهُ، يُؤَدُّونَهُ: one of the five verbs in raf' with an attached object"""
    return tok(full, lex, "verb", ["afal-khamsa", "mudari-marfu", "al-bariz-al-muttasil", "maful-bihi"] + (extra or []),
        "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَ" + PRON_AR[enc] + " ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + role[0] + ".",
        "One of the five verbs, in raf' by the kept nun; the waw is its doer and the attached pronoun its object, in the seat of nasb" + role[1] + ".",
        "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâil, bitişik zamir mef'ûlün bih — mahallen mansûb" + role[2] + ".", punct=punct,
        segments=[seg(full[:-len(enc)], lex, "verb"), seg(enc, PRON[enc], "pron")])

# ============================================ the text ============================================
TITLES = [{"ar": "قَبْلَ الْفَتْحِ", "en": "Before the conquest", "tr": "Fetihten önce"},
          {"ar": "يَوْمُ حِطِّينَ", "en": "The day of Ḥiṭṭīn", "tr": "Hıttîn günü"},
          {"ar": "الْحِصَارُ وَالصُّلْحُ", "en": "The siege and the terms", "tr": "Kuşatma ve sulh"},
          {"ar": "الْعَفْوُ عِنْدَ الْقُدْرَةِ", "en": "Pardon in the hour of power", "tr": "Güç yetirirken affetmek"},
          {"ar": "مِنْبَرُ نُورِ الدِّينِ", "en": "Nūr al-Dīn's minbar", "tr": "Nûreddin'in minberi"}]

# ---- Chapter 1 — قَبْلَ الْفَتْحِ ----
S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Jerusalem had been taken from the Muslims by the people of the Cross at the end of the fifth century (of the Hijra); in al-Aqṣā Mosque they killed a great many of the scholars and the devout, and over the Dome of the Rock they raised a great cross.",
  "tr": "Beytülmakdis, (hicrî) beşinci asrın sonunda haç ehli tarafından Müslümanların elinden alınmıştı; Mescid-i Aksâ'da âlimlerden ve âbidlerden pek çok kişiyi öldürmüşler, Kubbetü's-Sahra'nın üzerine de büyük bir haç dikmişlerdi."},
 "tokens": [KANA("كَانَ"), BAYT_ISMK(), MAQDIS_MI(), QAD(),
  ENC_MADI("أَخَذَهُ", "akhadha", "هُ", note_ar="، وَالْفَاعِلُ بَعْدَهُ، وَالْهَاءُ تَعُودُ عَلَى اسْمِ كَانَ" + KH_KANA[0], note_en="; its doer follows, and the attached pronoun returns to the noun of كَانَ" + KH_KANA[1], note_tr="; fâili ondan sonra gelir, zamir kâne'nin ismine döner" + KH_KANA[2]),
  *AHL_SALIB(FAIL), MINA(), MUSLIMIN_J(), FI(), MAJR("آخِرِ", "akhir", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("الْمِائَةِ", "mia", note_ar=" — وَالْمِائَةُ هُنَا: الْقَرْنُ مِنَ الْهِجْرَةِ", note_en=" — «the hundred» here is the century of the Hijra", note_tr=" — mi'e burada hicrî asırdır"),
  NAAT("الْخَامِسَةِ", "khamis", "jarr", punct="،"),
  VERB_WAW("فَقَتَلُوا", "qatala"), FI(), PH(MAJR("الْمَسْجِدِ", "masjid"), "al-masjid-al-aqsa"), AQSA_J(),
  MAFUL("خَلْقًا", "khalq"), NAAT("كَثِيرًا", "kathir", "nasb"), MINA(),
  MAJR("الْعُلَمَاءِ", "alim-scholar", extra=["jam-taksir"], note_ar=" — جَمْعُ عَالِمٍ", note_en=" — the plural of «scholar»", note_tr=" — âlim'in cem'i"),
  ATF("وَالْعُبَّادِ", "abid", "noun", "jarr", extra=["jam-taksir"], note_ar=" — جَمْعُ عَابِدٍ", note_en=" — the plural of «worshipper»", note_tr=" — âbid'in cem'i", punct="،"),
  VERB_WAW("وَرَفَعُوا", "rafaa"), ALA(), PH(MAJR("قُبَّةِ", "qubba", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), "qubbat-al-sakhra"), MUDAF_ILAYH("الصَّخْرَةِ", "sakhra"),
  MAFUL("صَلِيبًا", "salib"), NAAT("عَظِيمًا", "azim", "nasb", punct=".")]})
S1.append({"id": "s2", "translation": {
  "en": "And how many a king among the kings of the Muslims hoped to conquer it, and death came between him and that!",
  "tr": "Müslüman hükümdarlarından nice hükümdar onu fethetmeyi umdu da ölüm onunla bu emeli arasına girdi!"},
 "tokens": [KAM(), KAM_TAMYIZ("مَلِكٍ", "malik-king"), MIN(),
  MAJR("مُلُوكِ", "malik-king", extra=["jam-taksir"], note_ar="، مُضَافٌ — جَمْعُ مَلِكٍ؛ وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِمَلِكٍ", note_en=", annexed — the plural of «king»; the jarr phrase qualifies «a king», in the seat of jarr", note_tr=", muzâf — melik'in cem'i; câr-mecrûr «melik»in na'tı, mahallen mecrûr"),
  MUSLIMIN_MI(),
  MADI_ALIF("رَجَا", "raja", hidden=True, note_ar=" — وَهُوَ يَعُودُ عَلَى كَمْ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَمْ", note_en=" — it returns to كَمْ, and the clause fills the seat of raf' as the khabar of كَمْ", note_tr=" — kem'e döner; cümle kem'in haberi olarak mahallen merfû"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِرَجَا", "; the clause it builds is the object of «hoped», in the seat of nasb", "; kurduğu müevvel masdar «umdu»nun mef'ûlü, mahallen mansûb"),
  MANSUB_AN("يَفْتَحَهُ", "fataha", enc="هُ", punct="،", note_ar=" — وَالْهَاءُ لِبَيْتِ الْمَقْدِسِ", note_en=" — «it» is Jerusalem", note_tr=" — zamir Beytülmakdis'e döner"),
  MADI("فَحَالَ", "hala", ["hollow-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), FAIL("الْمَوْتُ", "mawt"),
  ZARF_ENC("بَيْنَهُ", "bayna", "هُ"), WA_BAYNA(), DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", punct="!")]})
S1.append({"id": "s3", "translation": {
  "en": "Nūr al-Dīn had ordered a minbar to be made for al-Aqṣā Mosque, in the hope that God would open it at his hands; but he died before he saw that.",
  "tr": "Nûreddin, Allah'ın onu kendi eliyle fethetmesini umarak Mescid-i Aksâ için bir minber yapılmasını emretmişti; fakat bunu göremeden öldü."},
 "tokens": [KANA("وَكَانَ"), NUR_ISMK(), DIN_MI(), QAD(),
  MADI("أَمَرَ", "amara-command", hidden=True, note_ar=KH_KANA[0], note_en=KH_KANA[1], note_tr=KH_KANA[2]),
  BI_NOUN("بِصُنْعِ", "sun", "صُنْعِ", extra=["masdar"], note_ar="، مُضَافٌ — مَصْدَرُ صَنَعَ", note_en="; it is annexed — the masdar of «to make»", note_tr="; muzâf — sanaa'nın masdarı"),
  MUDAF_ILAYH("مِنْبَرٍ", "minbar"),
  PH(LI_AL("لِلْمَسْجِدِ", "masjid", "الْمَسْجِدِ"), "al-masjid-al-aqsa"), AQSA_J(punct="،"),
  MAFUL_LAHU("رَجَاءَ", "raja-hope", mudaf=True, note_ar="، وَالْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ مُضَافٌ إِلَيْهِ", note_en="; the clause after it is its second term", note_tr="; sonraki müevvel masdar muzâfun ileyhtir"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause it builds is annexed to «hope», in the seat of jarr", "; kurduğu müevvel masdar «ümit»e muzâfun ileyh, mahallen mecrûr"),
  MANSUB_AN("يَفْتَحَهُ", "fataha", enc="هُ", hidden=False, note_ar=" — وَالْهَاءُ لِلْمَسْجِدِ", note_en=" — «it» is the mosque", note_tr=" — zamir mescide döner"),
  ALLAH_F(), ALA(), DUAL_ENC_MAJR("يَدَيْهِ", "yad", "هِ", punct="،"),
  MADI("فَمَاتَ", "mata-die", ["hollow-verbs"], hidden=True), ZARF("قَبْلَ", "qabla", **ZAMAN),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause it builds is annexed to «before», in the seat of jarr", "; kurduğu müevvel masdar «önce»ye muzâfun ileyh, mahallen mecrûr"),
  tok("يَرَى", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "Present verb put in nasb by أَنْ, its fatha estimated on the alif (it cannot be voiced there); the doer «he» is hidden.",
      "En ile mansûb muzâri, fethası elif üzerinde takdîrî (telaffuzu mümkün değil); fâil gizli zamir «o»."),
  DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih", punct=".")]})
S1.append({"id": "s4", "translation": {
  "en": "Then Saladin took up the cause after him: he gathered Egypt and Syria under his hand, and his aim was nothing other than to conquer Jerusalem.",
  "tr": "Sonra ondan sonra işi Selahaddin üstlendi; Mısır'ı ve Şam'ı elinde birleştirdi; gayesi Beytülmakdis'i fethetmekten başka bir şey değildi."},
 "tokens": [THUMMA(), MADI("قَامَ", "qama", ["hollow-verbs"], note_ar=" — وَالْفَاعِلُ «صَلَاحُ» مُؤَخَّرٌ بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «Ṣalāḥ» comes after the jarr phrases", note_tr="; fâili «Selâh» câr-mecrûrlardan sonraya bırakılmıştır"),
  BI_NOUN("بِالْأَمْرِ", "amr-noun", "الْأَمْرِ", note_ar=" — قَامَ بِالْأَمْرِ: تَوَلَّاهُ", note_en=" — «stood up with the matter»: took charge of it", note_tr=" — kâme bi'l-emr: işi üstlendi"), MIN(),
  ENC_NOUN("بَعْدِهِ", "bada", "هِ", "majr", note_ar=" — ظَرْفٌ جُرَّ بِمِنْ", note_en=" — a ẓarf of time drawn into jarr by مِنْ", note_tr=" — min ile mecrûr olmuş zaman zarfı"),
  SALAH_F(), DIN_MI(punct="،"),
  MADI("فَجَمَعَ", "jamaa-gather", hidden=True),
  MAFUL("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign="بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=DIPT_F2[0], note_en=DIPT_F2[1].replace("a town", "a land"), note_tr=DIPT_F2[2].replace("şehir adı", "ülke adı")),
  ATF("وَالشَّامَ", "sham", "propn", "nasb"), ZARF("تَحْتَ", "tahta"), ENC_NOUN("يَدِهِ", "yad", "هِ", "mudaf", punct="،"),
  WA_MA("atf"), KANA("كَانَتْ", fem=True), ENC_NOUN("غَايَتُهُ", "ghaya", "هُ", "ismk"), ILLA_HASR(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the clause it builds is the predicate of كَانَ, in the seat of nasb", "; kurduğu müevvel masdar kâne'nin haberi, mahallen mansûb"),
  MANSUB_AN("يَفْتَحَ", "fataha"), BAYT_MAF(), MAQDIS_MI(punct=".")]})
S1.append({"id": "s5", "translation": {
  "en": "That was no slight matter, for the people of the Cross had taken possession of the whole coast of Syria.",
  "tr": "Bu kolay bir iş değildi; çünkü haç ehli Şam sahilinin tamamına sahip olmuştu."},
 "tokens": [WA_LAM(), YAKUN(), DHALIKA("رَفْعٍ اسْمُ يَكُنْ", "raf' as the noun of يَكُنْ", "merfû — yekün'ün ismi"),
  tok("بِالْأَمْرِ", "amr-noun", "noun", ["huruf-al-ziyada-fil-kafiya", "huruf-jarr", "kana-wa-akhawatuha", "mahall-al-majrur"],
      "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَأْكِيدِ النَّفْيِ، وَالْأَمْرِ خَبَرُ يَكُنْ مَجْرُورٌ لَفْظًا بِالْبَاءِ الزَّائِدَةِ مَنْصُوبٌ مَحَلًّا.",
      "The ba is EXTRA, strengthening the negation; «the matter» is the predicate of يَكُنْ — in jarr in form after the extra ba, in nasb by its seat.",
      "Bâ, nefyi pekiştiren zâid cer harfidir; «iş» yekün'ün haberi — zâid bâ ile lafzen mecrûr, mahallen mansûb.",
      segments=[seg("بِ", "bi", "prep"), seg("الْأَمْرِ", "amr-noun", "noun")]),
  NAAT("الْيَسِيرِ", "yasir", "jarr", note_ar=" — تَبِعَ لَفْظَ مَنْعُوتِهِ", note_en=" — it follows the FORM of its noun", note_tr=" — mevsûfunun lafzına uyar", punct="،"),
  tok("فَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "The fa gives the reason («for»); إِنَّ «indeed» puts its noun in nasb and raises its predicate.", "Fâ ta'lîl içindir («çünkü»); inne: ismini nasb, haberini ref eder.",
      segments=[seg("فَ", "fa", "conj"), seg("إِنَّ", "inna", "part")]),
  tok("أَهْلَ", "ahl", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of إِنَّ, in nasb, annexed.", "İnne'nin ismi, mansûb, muzâf."),
  MUDAF_ILAYH("الصَّلِيبِ", "salib"),
  NOTE(KANU("كَانُوا"), " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", "; the whole clause is the predicate of إِنَّ, in the seat of raf'", "; cümle inne'nin haberi, mahallen merfû"),
  QAD(), VERB_WAW("مَلَكُوا", "malaka", note_ar=KH_KANA[0], note_en=KH_KANA[1], note_tr=KH_KANA[2]),
  MAFUL("سَاحِلَ", "sahil", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الشَّامِ", "sham", "propn"), KULLAHU(punct=".")]})

# ---- Chapter 2 — يَوْمُ حِطِّينَ ----
S2 = []
S2.append({"id": "s1", "translation": {
  "en": "When the year 583 came, Saladin gathered his armies from Egypt and Syria and marched with them until he encamped against Tiberias.",
  "tr": "Beş yüz seksen üç yılı gelince Selahaddin Mısır'dan ve Şam'dan ordularını topladı, onlarla yola çıktı ve nihayet Taberiye önüne kondu."},
 "tokens": [LAMMA2("فَلَمَّا"), KANAT_TAMMA(), FAIL("سَنَةُ", "sana", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("ثَلَاثٍ", "thalath", extra=["asma-al-adad-fil-kafiya"], note_ar=" — وَجَاءَ بِغَيْرِ تَاءٍ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ", note_en=" — written without ta because the counted noun «year» is feminine", note_tr=" — sayılan «sene» müennes olduğu için tâsız gelmiştir"),
  ATF("وَثَمَانِينَ", "thamanun", "noun", "jarr", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  tok("وَخَمْسِمِائَةٍ", "khams", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَخَمْسِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَمِائَةٍ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَتُكْتَبَانِ كَلِمَةً وَاحِدَةً.",
      "The waw conjoins; «five» is conjoined to the numbers before it, in jarr and annexed, and «hundred» is its second term, in jarr — the two are written as one word.",
      "Vâv atıf; «beş» öncekilere ma'tûf, mecrûr, muzâf; «yüz» muzâfun ileyh, mecrûr — ikisi bitişik yazılır.",
      segments=[seg("وَ", "wa", "conj"), seg("خَمْسِ", "khams", "noun"), seg("مِائَةٍ", "mia", "noun")]),
  MADI("جَمَعَ", "jamaa-gather", note_ar=FAIL_BAAD[0] + JAWAB_LAMMA[0], note_en=FAIL_BAAD[1] + JAWAB_LAMMA[1], note_tr=FAIL_BAAD[2] + JAWAB_LAMMA[2]),
  SALAH_F(), DIN_MI(), ENC_NOUN("جُيُوشَهُ", "jaysh", "هُ", "maful", extra=["jam-taksir"], note_ar=" — جَمْعُ جَيْشٍ", note_en=" — the plural of «army»", note_tr=" — ceyş'in cem'i"), MIN(),
  MAJR("مِصْرَ", "misr", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F2[0], note_en=DIPT_F2[1].replace("a town", "a land"), note_tr=DIPT_F2[2].replace("şehir adı", "ülke adı")),
  ATF("وَالشَّامِ", "sham", "propn", "jarr", punct="،"),
  MADI("وَسَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onlarla»)", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ، وَالضَّمِيرُ لِلْجُيُوشِ", note_en=" — the ba of company; «them» is the armies (a broken plural takes a feminine singular pronoun)", note_tr=" — bâ musâhabe içindir; zamir ordulara döner (kırık cem' müfred müennes zamir alır)"),
  HATTA_IBT(), MADI("نَزَلَ", "nazala", hidden=True), ALA(),
  MAJR("طَبَرِيَّةَ", "tabariyya", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F2[0], note_en=DIPT_F2[1], note_tr=DIPT_F2[2], punct=".")]})
S2.append({"id": "s2", "translation": {
  "en": "The people of the Cross had gathered with their hosts and their king at a spring of water; they left it and marched toward him in fierce heat, while the Muslims stood between them and the water.",
  "tr": "Haç ehli de bütün kalabalıklarıyla ve kralıyla bir su kaynağının başında toplanmıştı; orayı bırakıp şiddetli sıcakta ona doğru yürüdüler; Müslümanlar ise onlarla su arasına girmişti."},
 "tokens": [KANA("وَكَانَ"), *AHL_SALIB(ISMK), QAD_K(),
  VERB_WAW("اجْتَمَعُوا", "ijtamaa", ["form-viii-verbs"], note_ar=KH_KANA[0], note_en=KH_KANA[1], note_tr=KH_KANA[2]),
  BI_NOUN("بِجُمُوعِهِمْ", "jam", "جُمُوعِهِمْ", enc="هِمْ", extra=["jam-taksir"], note_ar=" — جَمْعُ جَمْعٍ، وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the plural of «host»; the ba of company («with»)", note_tr=" — cem'in cem'i; bâ musâhabe içindir («ile»)"),
  tok("وَمَلِكِهِمْ", "malik-king", "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"],
      WA_AR + "مَلِكِ مَعْطُوفٌ عَلَى جُمُوعِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The waw conjoins; «their king» is conjoined to «their hosts», in jarr and annexed to the pronoun, which fills the seat of jarr.",
      "Vâv atıf; «kralları» «kalabalıkları»na ma'tûf, mecrûr, zamire muzâf; zamir mahallen mecrûr.",
      segments=[seg("وَ", "wa", "conj"), seg("مَلِكِ", "malik-king", "noun"), seg("هِمْ", "pron-3mp", "pron")]),
  ZARF("عِنْدَ", "inda"), MUDAF_ILAYH("عَيْنِ", "ayn-spring", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("مَاءٍ", "ma-water", punct="،"),
  VERB_WAW_ENC("فَتَرَكُوهَا", "taraka", "هَا"), VERB_WAW("وَسَارُوا", "sara-travel", ["hollow-verbs"]), JARR_PRON("إِلَيْهِ", "ila", "إِلَيْ", "هِ", " («ona»)"),
  FI(), MAJR("حَرٍّ", "harr"), NAAT("شَدِيدٍ", "shadid", "jarr", punct="،"),
  WA_QAD(), MADI("حَالَ", "hala", ["hollow-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), MUSLIMUN_F(),
  ZARF_ENC("بَيْنَهُمْ", "bayna", "هُمْ"), WA_BAYNA(), MUDAF_ILAYH("الْمَاءِ", "ma-water", punct=".")]})
S2.append({"id": "s3", "translation": {
  "en": "And while they were marching, thirst having worn them to the utmost, all at once the Muslims surrounded them on every side, near a village called Ḥiṭṭīn.",
  "tr": "Onlar susuzluk kendilerini son haddine vardırmış hâlde yürürken, Müslümanlar ansızın Hıttîn denen bir köyün yanında onları her yandan kuşattı."},
 "tokens": [BAYNAMA(), PRON_MUB("هُمْ", "hum", built="السُّكُونِ", built_en="sukun", built_tr="sükûn"),
  MUDARI5("يَسِيرُونَ", "sara-travel", ["hollow-verbs"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ", role_en="; the clause is the predicate of «they», in the seat of raf'", role_tr="; cümle mübtedânın haberi, mahallen merfû"),
  WA_QAD(), MADI("بَلَغَ", "balagha", note_ar=" — وَالْفَاعِلُ «الْعَطَشُ» بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «thirst» comes after the jarr phrase", note_tr="; fâili «susuzluk» câr-mecrûrdan sonra gelir"),
  JARR_PRON("مِنْهُمُ", "min", "مِنْ", "هُمُ", " («onlardan»)", note_ar=" — وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the mim takes damma before the following ال", note_tr=" — iki sâkin karşılaştığı için mîm damme aldı"),
  FAIL("الْعَطَشُ", "atash"),
  tok("كُلَّ", "kull", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "idafa-definiteness"],
      "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — كُلٌّ إِذَا أُضِيفَتْ إِلَى مَصْدَرِ الْفِعْلِ نَابَتْ عَنْهُ.",
      "Standing in for the absolute object, in nasb and annexed — كُلّ annexed to the verb's own masdar takes its place («reached … every reaching», i.e. to the utmost).",
      "Mef'ûlün mutlakın nâibi, mansûb, muzâf — fiilin masdarına muzâf olan küll onun yerini tutar («her varışla vardı», yani son haddine)."),
  MUDAF_ILAYH("مَبْلَغٍ", "mablagh", note_ar=" — مَصْدَرٌ مِيمِيٌّ مِنْ بَلَغَ", note_en=" — a mīmī masdar of «to reach»", note_tr=" — belağa'nın mîmî masdarı", punct="،"),
  IDH_FUJ(), MADI("أَحَاطَ", "ahata", ["form-iv-verbs", "hollow-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]),
  JARR_PRON("بِهِمُ", "bi", "بِ", "هِمُ", " («onları»)", note_ar=" — وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the mim takes damma before the following ال", note_tr=" — iki sâkin karşılaştığı için mîm damme aldı"),
  MUSLIMUN_F(), MIN(), MAJR("كُلِّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("جَانِبٍ", "janib"),
  ZARF("عِنْدَ", "inda"), MUDAF_ILAYH("قَرْيَةٍ", "qarya"),
  tok("يُقَالُ", "qala", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "hollow-verbs", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِقَرْيَةٍ.",
      "A present verb in the passive, in raf' — the clause qualifies «a village», in the seat of jarr.",
      "Meçhul muzâri, merfû — cümle «köy»ün na'tı, mahallen mecrûr."),
  JARR_PRON("لَهَا", "li", "لَ", "هَا", " («ona»)"),
  tok("حِطِّينُ", "hittin", "propn", ["naib-al-fail", "mamnu-min-sarf"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ — وَهُوَ اللَّفْظُ الْمَقُولُ" + HITTIN[0] + ".",
      "The deputy doer of «is said», in raf' with no tanwin — the very name that is said" + HITTIN[1] + ".",
      "«Denir»in nâib-i fâili, tenvinsiz merfû — söylenen adın kendisi" + HITTIN[2] + ".", punct=".")]})
S2.append({"id": "s4", "translation": {
  "en": "The Muslims fought them fiercely, and the sun of that day did not set before their army had been broken.",
  "tr": "Müslümanlar onlarla şiddetle savaştı; o günün güneşi batmadan orduları bozulmuştu."},
 "tokens": [ENC_MADI("فَقَاتَلَهُمُ", "qatala-fight", "هُمُ", ["form-iii-verbs"], note_ar="، وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ" + FAIL_BAAD[0], note_en="; the mim takes damma before the following ال" + FAIL_BAAD[1], note_tr="; iki sâkin karşılaştığı için mîm damme aldı" + FAIL_BAAD[2]),
  MUSLIMUN_F(),
  tok("قِتَالًا", "qital", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ قَاتَلَ، يُؤَكِّدُ فِعْلَهُ، وَبِنَعْتِهِ يُبَيِّنُ نَوْعَهُ.",
      "The absolute object (maf'ul mutlaq), in nasb — the masdar of قَاتَلَ: it strengthens its verb, and with its adjective it tells the KIND of fighting.",
      "Mef'ûlün mutlak, mansûb — kâtele'nin masdarı: fiilini pekiştirir, sıfatıyla da savaşın türünü bildirir."),
  NAAT("شَدِيدًا", "shadid", "nasb", punct="،"),
  FA_MA(), MADI("غَابَتْ", "ghaba", ["hollow-verbs"], fem=True, note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]),
  FAIL("شَمْسُ", "shams", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), DHALIKA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh"),
  BADAL("الْيَوْمِ", "yawm", "jarr"), ILLA_HAL(), WA_QAD(), MAJHUL("كُسِرَ", "kasara"),
  NAIB_ENC("جَيْشُهُمْ", "jaysh", "هُمْ", punct=".")]})
S2.append({"id": "s5", "translation": {
  "en": "A great many of them were killed; their king and many of their great men were taken captive; and their greatest cross, under which they used to fight, was taken.",
  "tr": "Onlardan pek çoğu öldürüldü; kralları ve ileri gelenlerinden birçoğu esir edildi; altında savaştıkları en büyük haçları da alındı."},
 "tokens": [MAJHUL("وَقُتِلَ", "qatala"), MINHUM(), NAIB("خَلْقٌ", "khalq"), NAAT("كَثِيرٌ", "kathir", "raf", punct="،"),
  MAJHUL("وَأُسِرَ", "asara-capture"), NAIB_ENC("مَلِكُهُمْ", "malik-king", "هُمْ"), ATF("وَكَثِيرٌ", "kathir", "noun", "raf"), MIN(),
  ENC_NOUN("كُبَرَائِهِمْ", "kabir", "هِمْ", "majr", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ كَبِيرٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ، وَجُرَّ بِالْكَسْرَةِ لِإِضَافَتِهِ", note_en=" — the plural of «great man» on فُعَلَاء, a diptote, takes kasra here because it is annexed", note_tr=" — kebîr'in fuʿalâ' veznindeki cem'i; gayr-i munsarif iken muzâf olduğu için kesre ile mecrûr", punct="،"),
  MAJHUL("وَأُخِذَ", "akhadha"), NAIB_ENC("صَلِيبُهُمُ", "salib", "هُمُ", note_ar=" — وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the mim takes damma before the following ال", note_tr=" — iki sâkin karşılaştığı için mîm damme aldı"),
  NAAT("الْأَعْظَمُ", "azam", "raf", ["ism-tafdil"]), ALLADHI("raf", "لِصَلِيبِهِمْ", "their cross", "haçları"), KANU("كَانُوا"),
  MUDARI5("يُقَاتِلُونَ", "qatala-fight", ["form-iii-verbs"], role_ar=KH_KANA[0], role_en=KH_KANA[1], role_tr=KH_KANA[2]),
  ZARF_ENC("تَحْتَهُ", "tahta", "هُ", punct=".", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en=" — the pronoun is the one that returns to the relative", note_tr=" — zamir mevsûle dönen râbıttır")]})
S2.append({"id": "s6", "translation": {
  "en": "At this the Muslims were glad at heart (literally «good in soul»), and they were certain that the conquest of Jerusalem had drawn near.",
  "tr": "Müslümanların gönülleri bununla ferahladı (lafzen «nefisçe hoş oldular») ve Beytülmakdis'in fethinin yaklaştığına kesin olarak inandılar."},
 "tokens": [MADI("فَطَابَ", "taba", ["hollow-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), MUSLIMUN_F(), BI_DHALIKA(),
  TAMYIZ_NISBA("نَفْسًا", "nafs", "طَابَتْ نُفُوسُ الْمُسْلِمِينَ", "the Muslims' souls were glad", "Müslümanların nefisleri hoş oldu", punct="،"),
  VERB_WAW("وَأَيْقَنُوا", "ayqana", ["form-iv-verbs"]),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna", "hadhf-al-jarr"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرِيٌّ — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ نَصْبٍ بِنَزْعِ الْخَافِضِ، أَيْ: أَيْقَنُوا بِدُنُوِّ فَتْحِهِ.",
      "أَنَّ «that», the verb-like particle that builds a masdar — the clause it builds stands in nasb after a dropped preposition («were certain OF its conquest's drawing near»).",
      "Enne — te'kîd, nasb ve masdar harfi; müevvel masdar hâfızın nez'iyle mahallen mansûb («fethinin yaklaştığından emin oldular»)."),
  PH(tok("بَيْتَ", "bayt", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The noun of أَنَّ, in nasb, annexed.", "Enne'nin ismi, mansûb, muzâf."), "bayt-al-maqdis"),
  MAQDIS_MI(), QAD(),
  MADI_ALIF("دَنَا", "dana", note_ar=FAIL_BAAD[0] + " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ", note_en=FAIL_BAAD[1] + "; the clause is the predicate of أَنَّ, in the seat of raf'", note_tr=FAIL_BAAD[2] + "; cümle enne'nin haberi, mahallen merfû"),
  ENC_NOUN("فَتْحُهُ", "fath", "هُ", "fail", note_ar=" — وَالْهَاءُ رَابِطٌ يَعُودُ عَلَى اسْمِ أَنَّ", note_en=" — the pronoun ties the clause back to the noun of أَنَّ", note_tr=" — zamir enne'nin ismine dönen râbıttır", punct=".")]})

# ---- Chapter 3 — الْحِصَارُ وَالصُّلْحُ ----
S3 = []
S3.append({"id": "s1", "translation": {
  "en": "Then, after Ḥiṭṭīn, he busied himself with nothing but fighting his enemy: he took Acre and many of the cities of the coast, until, when he had finished with them, he marched on Jerusalem.",
  "tr": "Sonra Hıttîn'den sonra düşmanıyla savaşmaktan başka bir şeyle meşgul olmadı; Akkâ'yı ve sahil şehirlerinin birçoğunu fethetti; nihayet onlarla işini bitirince Beytülmakdis'e yürüdü."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"), LAM_JAZM(),
  JAZM_V("يَشْتَغِلْ", "ishtaghala", ["form-viii-verbs"], hidden="هُوَ", note_ar=KH_INNA_CL[0], note_en=KH_INNA_CL[1], note_tr=KH_INNA_CL[2]),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  MUDAF_ILAYH("حِطِّينَ", "hittin", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=HITTIN[0], note_en=HITTIN[1], note_tr=HITTIN[2]),
  BI_NOUN("بِغَيْرِ", "ghayr", "غَيْرِ", note_ar="، مُضَافٌ", note_en="; it is annexed", note_tr="; muzâf"),
  MUDAF_ILAYH("قِتَالِ", "qital", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), ENC_NOUN("عَدُوِّهِ", "aduww", "هِ", "mudaf", punct="،"),
  MADI("فَفَتَحَ", "fataha", hidden=True),
  MAFUL("عَكَّا", "akka", "propn", ["ism-maqsur-manqus"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — عَلَمٌ عَلَى مَدِينَةٍ مَقْصُورٌ", note_en=" — the fatha is estimated on the alif; a maqṣūr name of a city", note_tr=" — fetha elif üzerinde takdîrî; maksûr şehir adı"),
  ATF("وَكَثِيرًا", "kathir", "noun", "nasb"), MIN(),
  MAJR("مُدُنِ", "madina", extra=["jam-taksir"], note_ar="، مُضَافٌ — جَمْعُ مَدِينَةٍ", note_en=", annexed — the plural of «city»", note_tr=", muzâf — medîne'nin cem'i"),
  MUDAF_ILAYH("السَّاحِلِ", "sahil", punct="،"), HATTA_IBT(), IDHA("إِذَا"),
  MADI("فَرَغَ", "faragha", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ إِذَا إِلَيْهَا", note_en="; the clause is annexed to إِذَا, in the seat of jarr", note_tr="; cümle izâ'ya muzâfun ileyh, mahallen mecrûr"),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («onlardan»)", punct=None),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ جَوَابُ إِذَا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", note_en="; the clause is the answer of إِذَا and has no seat of its own", note_tr="; cümle izâ'nın cevabıdır, i'râbdan mahalli yoktur"),
  ILA(), BAYT_J(), MAQDIS_MI(punct=".")]})
S3.append({"id": "s2", "translation": {
  "en": "He encamped against it, while within it was a great host of the people of the Cross who had resolved to fight in its defence until they died.",
  "tr": "Şehrin önüne kondu; içinde ise onu savunmak için ölünceye kadar savaşmaya azmetmiş büyük bir haç ehli kalabalığı vardı."},
 "tokens": [MADI("فَنَزَلَ", "nazala", hidden=True), ALAYHI(),
  tok("وَفِيهِ", "fi", "prep", ["al-hal-jumla-wa-rabituha", "huruf-jarr", "mubtada-khabar", "al-bariz-al-muttasil"],
      "الْوَاوُ حَالِيَّةٌ، وَفِي حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw opens a hal clause; «in it» is a jarr letter with its pronoun — the FRONTED predicate; the nominal clause is a hal, in the seat of nasb.",
      "Hâl vâvı; «içinde» cer harfi ve zamiri — öne alınmış haber; isim cümlesi hâl olarak mahallen mansûb.",
      segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("جَمْعٌ", "jam", "noun", ["mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The mubtada, placed after its fronted predicate, in raf'.", "Mübtedâ (öne alınmış haberinden sonra gelmiş), merfû."), NAAT("عَظِيمٌ", "azim", "raf"), MIN(),
  MAJR("أَهْلِ", "ahl", note_ar="، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِجَمْعٍ", note_en=", annexed — the jarr phrase is a second adjective of «a host», in the seat of raf'", note_tr=", muzâf — câr-mecrûr «kalabalık»ın ikinci na'tı, mahallen merfû"),
  MUDAF_ILAYH("الصَّلِيبِ", "salib", punct="،"), QAD(),
  VERB_WAW("عَزَمُوا", "azama", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَالِثٌ لِجَمْعٍ، وَجُمِعَ الضَّمِيرُ حَمْلًا عَلَى مَعْنَاهُ", note_en="; the clause is a third adjective of «a host», in the seat of raf' — the pronoun is plural, following the MEANING of «host»", note_tr="; cümle «kalabalık»ın üçüncü na'tı, mahallen merfû — zamir anlamına bakılarak cem' gelmiştir"),
  ALA(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِعَلَى", "; the clause it builds is in the seat of jarr after عَلَى", "; kurduğu müevvel masdar alâ ile mahallen mecrûr"),
  FIVE_NASB("يُقَاتِلُوا", "qatala-fight", ["form-iii-verbs"]),
  ZARF_ENC("دُونَهُ", "duna", "هُ", note_ar=" — وَمَعْنَاهُ هُنَا: دِفَاعًا عَنْهُ", note_en=" — here «in its defence»", note_tr=" — burada «onu savunarak»"),
  tok("حَتَّى", "hatta", "part", ["nawasib-wa-jawazim-al-mudari", "huruf-jarr"],
      "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
      "حَتَّى «until», a particle of limit and jarr: the present verb after it is in nasb by an أَنْ that must stay unspoken, and the clause so built is in jarr after حَتَّى.",
      "Hattâ «…-e kadar»: gâye ve cer harfi; sonraki muzâri vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr."),
  FIVE_NASB("يَمُوتُوا", "mata-die", ["hollow-verbs"], by="أَنْ مُضْمَرَةٍ بَعْدَ حَتَّى", by_en="an أَنْ understood after حَتَّى", by_tr="hattâ'dan sonra gizli en", punct=".")]})
S3.append({"id": "s3", "translation": {
  "en": "Saladin laid the severest siege to it, until the Muslims breached its wall and were on the point of entering it.",
  "tr": "Selahaddin onu en şiddetli biçimde kuşattı; nihayet Müslümanlar surunu deldiler ve neredeyse içeri gireceklerdi."},
 "tokens": [ENC_MADI("فَحَاصَرَهُ", "hasara", "هُ", ["form-iii-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), SALAH_F(), DIN_MI(),
  tok("أَشَدَّ", "ashadd", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "ism-tafdil", "idafa-definiteness"],
      "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ أُضِيفَ إِلَى الْمَصْدَرِ فَأَخَذَ حُكْمَهُ.",
      "Standing in for the absolute object, in nasb and annexed — an elative annexed to the masdar takes the masdar's office («besieged it the severest besieging»).",
      "Mef'ûlün mutlakın nâibi, mansûb, muzâf — masdara muzâf olan ism-i tafdîl onun hükmünü alır («en şiddetli kuşatmayla kuşattı»)."),
  MUDAF_ILAYH("الْحِصَارِ", "hisar", note_ar=" — مَصْدَرُ حَاصَرَ", note_en=" — the masdar of «to besiege»", note_tr=" — hâsara'nın masdarı", punct="،"),
  HATTA_IBT(), MADI("خَرَقَ", "kharaqa", note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), MUSLIMUN_F(),
  ENC_NOUN("سُورَهُ", "sur-wall", "هُ", "maful", punct="،"),
  tok("وَكَادُوا", "kada", "verb", ["afal-al-muqaraba", "al-bariz-al-muttasil", "hollow-verbs"],
      WA_AR + "كَادَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَفْعَالِ الْمُقَارَبَةِ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهُ.",
      "The waw conjoins; كَادَ «was on the point of» is a defective verb of nearness, built on damma before the waw of the group; that waw is its noun, in the seat of raf'.",
      "Vâv atıf; kâde «az kalsın …-ecekti»: mukârebe fiillerinden nâkıs fiil, cemâat vâvı bitiştiği için damme üzere mebnî; vâv ismi, mahallen merfû.",
      segments=[seg("وَ", "wa", "conj"), seg("كَادُو", "kada", "verb"), seg("ا", "pron-3mp", "pron")]),
  MUDARI5_ENC("يَدْخُلُونَهُ", "dakhala", "هُ", punct=".", role=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَادَ", "; the clause is the predicate of كَادَ, in the seat of nasb", "; cümle kâde'nin haberi, mahallen mansûb"))]})
S3.append({"id": "s4", "translation": {
  "en": "When the people saw that, they were certain of ruin, and one of their great men came out to Saladin, asking him for safe-conduct.",
  "tr": "Halk bunu görünce helâki kesin bildi; ileri gelenlerinden biri Selahaddin'e çıkıp ondan eman istedi."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI_ALIF("رَأَى", "raa", note_ar=FAIL_BAAD[0] + LAMMA_CL[0], note_en=FAIL_BAAD[1] + LAMMA_CL[1], note_tr=FAIL_BAAD[2] + LAMMA_CL[2]),
  FAIL("الْقَوْمُ", "qawm"), DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih"),
  VERB_WAW("أَيْقَنُوا", "ayqana", ["form-iv-verbs"], note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  BI_NOUN("بِالْهَلَاكِ", "halak", "الْهَلَاكِ", punct="،"),
  MADI("فَخَرَجَ", "kharaja", note_ar=" — وَالْفَاعِلُ «كَبِيرٌ» بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «a great man» comes after the jarr phrase", note_tr="; fâili «bir büyük» câr-mecrûrdan sonra gelir"),
  ILA(), SALAH_J(), DIN_MI(), FAIL("كَبِيرٌ", "kabir"), MIN(),
  ENC_NOUN("كُبَرَائِهِمْ", "kabir", "هِمْ", "majr", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِكَبِيرٍ", note_en=" — the jarr phrase qualifies «a great man», in the seat of raf'", note_tr=" — câr-mecrûr «bir büyük»ün na'tı, mahallen merfû"),
  MUDARI("يَطْلُبُ", "talaba", note_ar=HALCL[0], note_en=HALCL[1], note_tr=HALCL[2]), MINHU(), MAFUL("الْأَمَانَ", "aman", punct=".")]})
S3.append({"id": "s5", "translation": {
  "en": "At first Saladin refused, because of what they had done to the Muslims on the day they took the city.",
  "tr": "Selahaddin, şehri aldıkları gün Müslümanlara yaptıkları yüzünden önce bunu kabul etmedi."},
 "tokens": [MADI_ALIF("فَأَبَى", "aba", note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), SALAH_F(), DIN_MI(),
  DHALIKA("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb — mef'ûlün bih"),
  ZARF("أَوَّلَ", "awwal", **ZAMAN, note_ar=" — أَيْ: فِي أَوَّلِ الْأَمْرِ", note_en=" — «at the first of the matter»", note_tr=" — «işin başında»"),
  MUDAF_ILAYH("الْأَمْرِ", "amr-noun", punct="،"),
  tok("لِمَا", "li", "prep", ["huruf-jarr", "lam-taleel", "ism-mawsul"],
      "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: صَنَعُوهُ.",
      "The lam of cause («because of»); مَا «what» is the relative, built on sukun in the seat of jarr — the pronoun that should return to it is left unsaid («what they did [it]»).",
      "Ta'lîl lâmı («…-den dolayı»); mâ ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr — ona dönen zamir hazfedilmiştir («yaptıkları [şey]»).",
      segments=[seg("لِ", "li", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  VERB_WAW("صَنَعُوا", "sanaa", note_ar=SILA_[0], note_en=SILA_[1], note_tr=SILA_[2]), BI_MUSLIMIN(),
  ZARF("يَوْمَ", "yawm", **ZAMAN, note_ar=" — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the clause after it is its second term, in the seat of jarr", note_tr="; sonraki cümle muzâfun ileyh, mahallen mecrûr"),
  VERB_WAW("أَخَذُوا", "akhadha"), MAFUL("الْمَدِينَةَ", "madina", punct=".")]})
S3.append({"id": "s6", "translation": {
  "en": "Then he granted them terms, on condition that each one of them pay for himself a fixed sum within a fixed term: whoever paid went out in safety, and whoever could not became a captive.",
  "tr": "Sonra her birinin belli bir süre içinde kendi adına belli bir mal ödemesi şartıyla onlarla sulhe razı oldu: ödeyen emniyet içinde çıktı, ödeyemeyen esir oldu."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  ENC_MADI("أَجَابَهُمْ", "ajaba", "هُمْ", ["form-iv-verbs", "hollow-verbs"], hidden=True, note_ar=KH_INNA_CL[0], note_en=KH_INNA_CL[1], note_tr=KH_INNA_CL[2]),
  ILA(), MAJR("الصُّلْحِ", "sulh", punct="،"), ALA(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِعَلَى", "; the clause it builds is in the seat of jarr after عَلَى («on condition that …»)", "; kurduğu müevvel masdar alâ ile mahallen mecrûr («… şartıyla»)"),
  MANSUB_AN("يُؤَدِّيَ", "adda", ["form-ii-verbs", "naqis-verbs"], hidden=False, note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha shows on the ya, which bears it easily", note_tr=" — fetha hafif olduğu için yâ üzerinde zâhirdir"),
  FAIL("كُلُّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("وَاحِدٍ", "wahid"), MINHUM(),
  AN_PREP(), ENC_NOUN("نَفْسِهِ", "nafs", "هِ", "majr"), MAFUL("مَالًا", "mal"), NAAT("مَعْلُومًا", "malum", "nasb", ["ism-maful"]),
  FI(), MAJR("أَجَلٍ", "ajal"), NAAT("مَعْلُومٍ", "malum", "jarr", ["ism-maful"], punct="،"),
  tok("فَمَنْ", "man", "pron", ["al-majzum-wal-shart-wal-jaza", "mubtada-khabar", "al-mabni-wal-mudmar"], "الْفَاءُ اسْتِئْنَافِيَّةٌ تُفَصِّلُ مَا قَبْلَهَا، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُهُ.", "The fa opens the detail of the terms; مَنْ «whoever» is the conditional noun that governs jazm, built on sukun in the seat of raf' as mubtada; the condition and its answer are its khabar.", "Fâ, öncesini açıklayan isti'nâf fâ'sıdır; men «kim …-sa»: cezm eden şart ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû; şart ve cevap cümleleri haberidir.", segments=[seg("فَ", "fa", "conj"), seg("مَنْ", "man", "pron")]),
  tok("أَدَّى", "adda", "verb", ["al-majzum-wal-shart-wal-jaza", "naqis-verbs", "form-ii-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "Past verb built on a fatha estimated on the alif, in the seat of jazm as the condition's verb; the doer «he» is hidden.",
      "Elif üzerinde takdîrî fetha ile mebnî mâzî, şart fiili olarak mahallen meczûm; fâil gizli zamir «o»."),
  JAWAB_V("خَرَجَ", "kharaja"), HAL("آمِنًا", "amin-safe", punct="،"),
  MAN_SHART("وَمَنْ"), SHART_V("عَجَزَ", "ajaza"),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza", "hollow-verbs"],
      "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُ مَنْ.",
      "كَانَ is the defective past verb, built on fatha, in the seat of jazm as the condition's answer; its noun is the hidden «he» — the condition and its answer together are the khabar of «whoever».",
      "Nâkıs mâzî kâne, fetha üzere mebnî, şartın cevabı olarak mahallen meczûm; ismi gizli zamir «o» — şart ve cevap cümleleri men'in haberidir."),
  KHK("أَسِيرًا", "asir", punct=".")]})
S3.append({"id": "s7", "translation": {
  "en": "The city was handed over to him on Friday, the twenty-seventh of the month of Rajab, after it had remained in the hands of the people of the Cross for a long time.",
  "tr": "Şehir, uzun bir süre haç ehlinin elinde kaldıktan sonra, Recep ayının yirmi yedinci günü olan cuma günü ona teslim edildi."},
 "tokens": [MAJHUL_FEM_K("فَسُلِّمَتِ", "sallama", ["form-ii-verbs"]), NAIB("الْمَدِينَةُ", "madina"), ILAYHI(), FI(),
  MAJR("يَوْمِ", "yawm", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الْجُمُعَةِ", "jumua"),
  NAAT("السَّابِعِ", "sabi", "jarr", ["asma-al-adad-fil-kafiya"], note_ar=" — مَنْعُوتُهُ «يَوْمِ» لَا «الْجُمُعَةِ»، وَهُوَ عَدَدٌ تَرْتِيبِيٌّ", note_en=" — the noun it qualifies is «day», not «Friday»: an ordinal", note_tr=" — mevsûfu «cuma» değil «gün»dür; sıra sayısı"),
  ATF("وَالْعِشْرِينَ", "ishrun", "noun", "jarr", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_en=" — in jarr by the ya, declined like the sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  MIN(), MAJR("شَهْرِ", "shahr", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MUDAF_ILAYH("رَجَبٍ", "rajab", "propn", note_ar=" — عَلَمٌ عَلَى الشَّهْرِ مَصْرُوفٌ، إِذْ لَيْسَ فِيهِ مِنْ مَوَانِعِ الصَّرْفِ إِلَّا الْعَلَمِيَّةُ", note_en=" — the month's name keeps its tanwin: being a proper name is its only bar, and one bar is not enough", note_tr=" — ay adı munsariftir: özel isim oluşu tek sebeptir, tek sebep men' için yetmez", punct="،"),
  ZARF("بَعْدَ", "bada", **ZAMAN), AN_MADI("أَنْ"),
  MADI("بَقِيَتْ", "baqiya", ["naqis-verbs"], fem=True, hidden=True), FI(),
  tok("أَيْدِي", "yad", "noun", ["huruf-jarr", "ism-maqsur-manqus", "jam-taksir", "idafa-definiteness"],
      "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ — جَمْعُ يَدٍ.",
      "In jarr by a kasra estimated on the ya (it is too heavy to voice there), annexed — the plural of «hand».",
      "Yâ üzerinde ağırlıktan takdîrî kesre ile mecrûr, muzâf — yed'in cem'i."),
  MUDAF_ILAYH("أَهْلِ", "ahl", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("الصَّلِيبِ", "salib"),
  ZARF("زَمَنًا", "zaman-period", mudaf=False, **ZAMAN), NAAT("طَوِيلًا", "tawil-long", "nasb", punct=".")]})

# ---- Chapter 4 — الْعَفْوُ عِنْدَ الْقُدْرَةِ ----
S4 = []
S4.append({"id": "s1", "translation": {
  "en": "Saladin did not do to the people of the city what the people of the Cross had done to the Muslims on the day they entered it; rather, he gave them safe-conduct for their lives and their goods.",
  "tr": "Selahaddin şehir halkına, haç ehlinin şehre girdikleri gün Müslümanlara yaptığını yapmadı; aksine onlara canları ve malları için eman verdi."},
 "tokens": [WA_LAM(), JAZM_V("يَصْنَعْ", "sanaa"), SALAH_F(), DIN_MI(),
  BI_NOUN("بِأَهْلِ", "ahl", "أَهْلِ", note_ar="، مُضَافٌ", note_en="; it is annexed", note_tr="; muzâf"), MUDAF_ILAYH("الْمَدِينَةِ", "madina"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
      "A relative pronoun «what», built on sukun, the object in the seat of nasb; the clause after it is its ṣila.", "İsm-i mevsûl «…-an şey», sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb; sonraki cümle sılasıdır."),
  ENC_MADI("صَنَعَهُ", "sanaa", "هُ", note_ar=FAIL_BAAD[0] + AID[0] + SILA_[0], note_en=FAIL_BAAD[1] + AID[1] + SILA_[1], note_tr=FAIL_BAAD[2] + AID[2] + SILA_[2]),
  *AHL_SALIB(FAIL), BI_MUSLIMIN(),
  ZARF("يَوْمَ", "yawm", **ZAMAN, note_ar=" — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the clause after it is its second term, in the seat of jarr", note_tr="; sonraki cümle muzâfun ileyh, mahallen mecrûr"),
  VERB_WAW_ENC("دَخَلُوهَا", "dakhala", "هَا", punct="،"),
  tok("بَلْ", "bal", "part", ["aw-imma-am-la-bal-lakin-fil-kafiya", "atf-nasaq"], "حَرْفُ إِضْرَابٍ وَابْتِدَاءٍ — وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ.",
      "بَلْ «rather» turns away from what was denied to what is affirmed; before a whole clause it opens a new sentence.", "Bel «aksine»: idrâb ve ibtidâ harfi — sonraki cümle müste'neftir."),
  ENC_MADI("أَعْطَاهُمُ", "aata", "هُمُ", ["form-iv-verbs", "mafulayn"], alif=True, hidden=True, note_ar=" أَوَّلُ، وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the first of two; the mim takes damma before the following ال", note_tr=" — iki mef'ûlün birincisi; iki sâkin karşılaştığı için mîm damme aldı"),
  tok("الْأَمَانَ", "aman", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — أَعْطَى يَنْصِبُ مَفْعُولَيْنِ.", "The second object, in nasb — أَعْطَى «to give» takes two objects.", "İkinci mef'ûlün bih, mansûb — a'tâ iki mef'ûl alır."), ALA(),
  ENC_NOUN("أَنْفُسِهِمْ", "nafs", "هِمْ", "majr", extra=["jam-taksir"], note_ar=" — جَمْعُ نَفْسٍ", note_en=" — the plural of «self»", note_tr=" — nefs'in cem'i"),
  tok("وَأَمْوَالِهِمْ", "mal", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
      WA_AR + "أَمْوَالِ مَعْطُوفٌ عَلَى أَنْفُسِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ مَالٍ.",
      "The waw conjoins; «their goods» is conjoined to «their lives», in jarr and annexed to the pronoun — the plural of «wealth».",
      "Vâv atıf; «malları» «canları»na ma'tûf, mecrûr, zamire muzâf — mâl'in cem'i.", punct=".",
      segments=[seg("وَ", "wa", "conj"), seg("أَمْوَالِ", "mal", "noun"), seg("هِمْ", "pron-3mp", "pron")])]})
S4.append({"id": "s2", "translation": {
  "en": "He took from them only the money on which they had made terms with him; then he let them go out in safety to what remained to their people of the lands.",
  "tr": "Onlardan yalnızca üzerinde anlaştıkları malı aldı; sonra onları, kavimlerinin elinde kalan topraklara güven içinde çıkıp gitmeleri için serbest bıraktı."},
 "tokens": [WA_INNAMA(), MADI("أَخَذَ", "akhadha", hidden=True),
  JARR_PRON("مِنْهُمُ", "min", "مِنْ", "هُمُ", " («onlardan»)", note_ar=" — وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ", note_en=" — the mim takes damma before the following ال", note_tr=" — iki sâkin karşılaştığı için mîm damme aldı"),
  MAFUL("الْمَالَ", "mal", note_ar=" — وَهُوَ الْمَقْصُورُ عَلَيْهِ", note_en=" — this is what the act is restricted TO", note_tr=" — fiil buna hasredilmiştir"),
  ALLADHI("nasb", "لِلْمَالِ", "the money", "mal"),
  VERB_WAW_ENC("صَالَحُوهُ", "salaha", "هُ", ["form-iii-verbs"], note_ar=SILA_[0], note_en=SILA_[1], note_tr=SILA_[2]),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («onun üzerine»)", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en=" — the pronoun is the one that returns to the relative", note_tr=" — zamir mevsûle dönen râbıttır", punct="،"),
  THUMMA(), ENC_MADI("تَرَكَهُمْ", "taraka", "هُمْ", hidden=True),
  MUDARI5("يَخْرُجُونَ", "kharaja", role_ar=HALCL[0], role_en=HALCL[1], role_tr=HALCL[2]),
  tok("آمِنِينَ", "amin-safe", "noun", ["hal", "jam-mudhakkar-salim", "ism-fail"],
      "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — صَاحِبُهَا وَاوُ يَخْرُجُونَ.",
      "A hal in nasb by the ya — a sound masculine plural; it describes the waw of «they go out».",
      "Hâl, cem-i müzekker sâlim olduğu için yâ ile mansûb — sahibi «çıkıyorlar»ın vâvıdır."),
  ILA(), MA_MAWSULA("جَرٍّ بِإِلَى", "jarr after إِلَى", "mecrûr (ilâ ile)", ["huruf-jarr"]),
  MADI("بَقِيَ", "baqiya", ["naqis-verbs"], hidden=True, note_ar=" — يَعُودُ عَلَى مَا" + SILA_[0], note_en=" — returning to مَا" + SILA_[1], note_tr=" — mâ'ya döner" + SILA_[2]),
  LI_ENC("لِقَوْمِهِمْ", "qawm", "قَوْمِ", "هِمْ"), MINA(),
  MAJR("الْبِلَادِ", "bilad", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ بَيَانٌ لِمَا", note_en=" — the jarr phrase explains «what»", note_tr=" — câr-mecrûr «şey»i açıklar", punct=".")]})
S4.append({"id": "s3", "translation": {
  "en": "Among them were many poor people who could find nothing to pay for themselves, and Saladin and his brother set a great many of them free without ransom.",
  "tr": "Aralarında kendi adlarına ödeyecek bir şey bulamayan pek çok fakir vardı; Selahaddin ve kardeşi onlardan pek çoğunu fidyesiz serbest bıraktı."},
 "tokens": [KANA("وَكَانَ"), JARR_PRON("فِيهِمْ", "fi", "فِي", "هِمْ", " («onların arasında»)", note_ar=KH_MUQ2[0], note_en=KH_MUQ2[1], note_tr=KH_MUQ2[2]),
  ISMK("فُقَرَاءُ", "faqir", extra=["mamnu-min-sarf", "jam-taksir"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", muakhkhar=True, note_ar=" — جَمْعُ فَقِيرٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ", note_en=" — the plural of «poor» on فُعَلَاء, a diptote by its lengthened feminine alif, so no tanwin", note_tr=" — fakîr'in fuʿalâ' veznindeki cem'i; memdûd te'nîs elifi sebebiyle gayr-i munsarif, tenvin almaz"),
  tok("كَثِيرُونَ", "kathir", "noun", ["naat-sifa", "jam-mudhakkar-salim"], "نَعْتٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "An adjective agreeing with «poor people», in raf' by the waw — a sound masculine plural.", "Na't, cem-i müzekker sâlim olduğu için vâv ile merfû."),
  LA_NAFIYA(),
  MUDARI5("يَجِدُونَ", "wajada", ["mithal-verbs"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِفُقَرَاءَ", role_en="; the clause is a second adjective of «poor people», in the seat of raf'", role_tr="; cümle «fakirler»in ikinci na'tı, mahallen merfû"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.",
      "A relative pronoun «what», built on sukun, the object in the seat of nasb; the clause after it is its ṣila.", "İsm-i mevsûl «…-an şey», sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb; sonraki cümle sılasıdır."),
  MUDARI5_ENC("يُؤَدُّونَهُ", "adda", "هُ", ["form-ii-verbs", "naqis-verbs"], role=(AID[0] + SILA_[0], AID[1] + SILA_[1], AID[2] + SILA_[2])),
  AN_PREP(), ENC_NOUN("أَنْفُسِهِمْ", "nafs", "هِمْ", "majr", extra=["jam-taksir"], punct="،"),
  MADI("فَأَطْلَقَ", "atlaqa", ["form-iv-verbs"], note_ar=" — وَالْفَاعِلُ «صَلَاحُ» بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «Ṣalāḥ» comes after the jarr phrase", note_tr="; fâili «Selâh» câr-mecrûrdan sonra gelir"),
  MINHUM(), SALAH_F(), DIN_MI(),
  tok("وَأَخُوهُ", "akh", "noun", ["atf-nasaq", "five-nouns", "idafa-definiteness", "al-bariz-al-muttasil"],
      WA_AR + "أَخُو مَعْطُوفٌ عَلَى صَلَاحُ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The waw conjoins; «his brother» is conjoined to «Ṣalāḥ», in raf' by the waw — one of the five nouns; annexed to the pronoun, which fills the seat of jarr.",
      "Vâv atıf; «kardeşi» «Selâh»a ma'tûf, esmâ-i hamseden olduğu için vâv ile merfû; zamire muzâf, zamir mahallen mecrûr.",
      segments=[seg("وَ", "wa", "conj"), seg("أَخُو", "akh", "noun"), seg("هُ", "pron-3ms", "pron")]),
  MAFUL("خَلْقًا", "khalq"), NAAT("كَثِيرًا", "kathir", "nasb"),
  BI_NOUN("بِغَيْرِ", "ghayr", "غَيْرِ", note_ar="، مُضَافٌ", note_en="; it is annexed", note_tr="; muzâf"), MUDAF_ILAYH("فِدَاءٍ", "fida", punct=".")]})
S4.append({"id": "s4", "translation": {
  "en": "And many an aged old man he set free out of mercy for him!",
  "tr": "Nice yaşlı ihtiyarı da ona acıdığı için serbest bıraktı!"},
 "tokens": [KAM(), KAM_TAMYIZ("شَيْخٍ", "shaykh"), NAAT("كَبِيرٍ", "kabir", "jarr"),
  ENC_MADI("أَطْلَقَهُ", "atlaqa", "هُ", ["form-iv-verbs"], hidden=True, note_ar=" — وَالْهَاءُ تَعُودُ عَلَى كَمْ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَمْ", note_en=" — the attached pronoun returns to كَمْ, and the clause is the khabar of كَمْ, in the seat of raf'", note_tr=" — bitişik zamir kem'e döner; cümle kem'in haberi, mahallen merfû"),
  MAFUL_LAHU("رَحْمَةً", "rahma"), BIHI(punct="!")]})
S4.append({"id": "s5", "translation": {
  "en": "By my life, that did not come from weakness; it came only from power — and pardon in the hour of power is the greatest pardon.",
  "tr": "Ömrüme yemin olsun ki bu zaaftan değildi; ancak kudrettendi. Güç yetirebilecekken affetmek, affın en büyüğüdür."},
 "tokens": [tok("وَلَعَمْرِي", "amr-qasam", "noun", ["huruf-al-qasam-fil-kafiya", "al-qasam-wal-shart-fil-kafiya", "mubtada-khabar", "ya-al-mutakallim", "hadhf-wa-taqdir"],
      "الْوَاوُ لِلِاسْتِئْنَافِ، وَاللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرُ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْخَبَرُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي؛ وَهٰذِهِ صِيغَةُ قَسَمٍ.",
      "The waw opens a new sentence; the lam is the lam of ibtidāʾ; عَمْر «life» is the mubtada, in raf' by a damma estimated before the speaker's ya (the kasra the ya demands holds its place), annexed to the ya — its predicate is dropped by rule («[is my oath]»): this is a FORM OF OATH, «by my life».",
      "Vâv isti'nâf içindir; lâm ibtidâ lâmıdır; «ömür» mübtedâ, mütekellim yâ'sından önce takdîrî damme ile merfû (yerini yâ'nın gerektirdiği kesre tutmuştur), yâ'ya muzâf — haberi vücûben hazfedilmiştir («yeminimdir»): bu bir yemin kalıbıdır, «ömrüme andolsun».",
      segments=[seg("وَ", "wa", "conj"), seg("لَ", "lam-ibtida", "part"), seg("عَمْرِ", "amr-qasam", "noun"), seg("ي", "pron-1s", "pron")]),
  NOTE(MA_NAFIYA(), " — وَالْجُمْلَةُ بَعْدَهَا جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا", "; the clause it opens is the answer of the oath and has no seat", "; açtığı cümle kasemin cevabıdır, mahalli yoktur"),
  KANA("كَانَ"), DHALIKA("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi"),
  AN_PREP(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", "; the jarr phrase hangs on the omitted predicate of كَانَ", "; câr-mecrûr kâne'nin mahzûf haberine müteallik")),
  MAJR("ضَعْفٍ", "daf", punct="،"), WA_INNAMA(pre="atf"), KANA_HID("كَانَ"),
  AN_PREP(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ — وَهُوَ الْمَقْصُورُ عَلَيْهِ", "; the jarr phrase hangs on the omitted predicate of كَانَ — and it is what the statement is restricted TO", "; câr-mecrûr kâne'nin mahzûf haberine müteallik — hüküm ona hasredilmiştir")),
  MAJR("قُدْرَةٍ", "qudra", punct="،"),
  tok("وَالْعَفْوُ", "afw", "noun", ["mubtada-khabar", "masdar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْعَفْوُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The waw opens a new sentence; «pardon» is the mubtada, in raf'.", "Vâv isti'nâf içindir; «af» mübtedâ, merfû.",
      segments=[seg("وَ", "wa", "conj"), seg("الْعَفْوُ", "afw", "noun")]),
  ZARF("عِنْدَ", "inda", note_ar=" — مُتَعَلِّقٌ بِالْعَفْوِ", note_en=" — it hangs on «pardon»", note_tr=" — «af»a müteallik"), MUDAF_ILAYH("الْقُدْرَةِ", "qudra"),
  KHABAR("أَعْظَمُ", "azam", ["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ", note_en=", annexed — an elative", note_tr=", muzâf — ism-i tafdîl"),
  MUDAF_ILAYH("الْعَفْوِ", "afw", punct=".")]})
S4.append({"id": "s6", "translation": {
  "en": "So the Muslims, on the day they entered it, were better in their deed than their enemy on the day he entered it.",
  "tr": "Böylece Müslümanlar şehre girdikleri gün, düşmanlarının şehre girdiği günkünden davranışça daha güzeldi."},
 "tokens": [KANA("فَكَانَ"),
  ISMK("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign="بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ", note_en=" — by the waw, a sound masculine plural", note_tr=" — cem-i müzekker sâlim olduğu için vâv ile"),
  ZARF("يَوْمَ", "yawm", **ZAMAN, note_ar=" — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the clause after it is its second term, in the seat of jarr", note_tr="; sonraki cümle muzâfun ileyh, mahallen mecrûr"),
  VERB_WAW_ENC("دَخَلُوهَا", "dakhala", "هَا"),
  KHK("أَحْسَنَ", "ahsan", extra=["ism-tafdil", "mamnu-min-sarf"], note_ar=" — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ", note_en=" — an elative, barred from tanwin (an adjective on the أَفْعَل pattern)", note_tr=" — ism-i tafdîl; vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif"),
  TAMYIZ("صَنِيعًا", "sani-deed"),
  MIN(role=(" لِلْمُفَاضَلَةِ بَعْدَ اسْمِ التَّفْضِيلِ", " of comparison («than») after the elative", " — tafdîl isminden sonra gelen karşılaştırma min'i («-den daha»)")),
  ENC_NOUN("عَدُوِّهِمْ", "aduww", "هِمْ", "majr"),
  ZARF("يَوْمَ", "yawm", **ZAMAN, note_ar=" — وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the clause after it is its second term, in the seat of jarr", note_tr="; sonraki cümle muzâfun ileyh, mahallen mecrûr"),
  ENC_MADI("دَخَلَهَا", "dakhala", "هَا", hidden=True, punct=".")]})

# ---- Chapter 5 — مِنْبَرُ نُورِ الدِّينِ ----
S5 = []
S5.append({"id": "s1", "translation": {
  "en": "Then he entered the city and gave orders concerning the cross that stood on the Dome of the Rock, and it was taken down; and he gave orders concerning al-Aqṣā Mosque and the Rock, and the two were cleansed.",
  "tr": "Sonra şehre girdi; Kubbetü's-Sahra'nın üzerindeki haç hakkında emir verdi, haç indirildi; Mescid-i Aksâ ve Sahra hakkında emir verdi, ikisi de temizlendi."},
 "tokens": [THUMMA(), INNA_ENC("إِنَّهُ", "هُ", " («o»)"),
  MADI("دَخَلَ", "dakhala", hidden=True, note_ar=KH_INNA_CL[0], note_en=KH_INNA_CL[1], note_tr=KH_INNA_CL[2]), MAFUL("الْمَدِينَةَ", "madina", punct="،"),
  MADI("فَأَمَرَ", "amara-command", hidden=True), BI_NOUN("بِالصَّلِيبِ", "salib", "الصَّلِيبِ"),
  ALLADHI("jarr", "لِلصَّلِيبِ", "the cross", "haç"), KANA_HID("كَانَ"),
  PREP("عَلَى", "ala", "، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ", "; the jarr phrase is the predicate of كَانَ", "; câr-mecrûr kâne'nin haberidir", gloss_tr="«üzerinde»"),
  PH(MAJR("قُبَّةِ", "qubba", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), "qubbat-al-sakhra"), MUDAF_ILAYH("الصَّخْرَةِ", "sakhra"),
  MAJHUL("فَأُنْزِلَ", "anzala", ["form-iv-verbs"], punct="،", note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", note_en="; its deputy doer is the hidden «it»", note_tr="; nâib-i fâil gizli zamir «o»"),
  MADI("وَأَمَرَ", "amara-command", hidden=True),
  PH(BI_NOUN("بِالْمَسْجِدِ", "masjid", "الْمَسْجِدِ"), "al-masjid-al-aqsa"), AQSA_J(), ATF("وَالصَّخْرَةِ", "sakhra", "noun", "jarr"),
  tok("فَطُهِّرَا", "tahhara", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "al-muthanna", "al-bariz-al-muttasil", "form-ii-verbs"],
      FA_AR + "طُهِّرَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — وَغُلِّبَ الْمُذَكَّرُ (الْمَسْجِدُ) عَلَى الْمُؤَنَّثِ (الصَّخْرَةُ).",
      "The fa conjoins; «were cleansed» is a past verb in the passive, built on fatha; the alif of the two is its deputy doer, in the seat of raf' — the masculine «mosque» prevails over the feminine «Rock» in the dual.",
      "Fâ atıf; meçhul mâzî, fetha üzere mebnî; tesniye elifi nâib-i fâil, mahallen merfû — müzekker «mescid», müennes «sahra»ya galip getirilmiştir.",
      punct=".", segments=[seg("فَ", "fa", "conj"), seg("طُهِّرَ", "tahhara", "verb"), seg("ا", "pron-3d", "pron")])]})
S5.append({"id": "s2", "translation": {
  "en": "Everything the people had introduced into them in the way of building was removed from them, until the two returned to what they had been.",
  "tr": "O kavmin ikisine kattığı bütün yapılar onlardan kaldırıldı; nihayet ikisi de eski hâllerine döndü."},
 "tokens": [MAJHUL_HOLLOW("وَأُزِيلَ", "azala"), JARR_PRON("عَنْهُمَا", "an", "عَنْ", "هُمَا", " («o ikisinden»)"),
  NAIB("كُلُّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  MA_MAWSULA("جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "mecrûr — muzâfun ileyh", ["idafa-definiteness"]),
  KANA("كَانَ"), ISMK("الْقَوْمُ", "qawm"), QAD(),
  VERB_WAW_ENC("أَحْدَثُوهُ", "ahdatha", "هُ", ["form-iv-verbs"], note_ar=KH_KANA[0] + AID[0], note_en=KH_KANA[1] + AID[1], note_tr=KH_KANA[2] + AID[2]),
  JARR_PRON("فِيهِمَا", "fi", "فِي", "هِمَا", " («o ikisinde»)"),
  MIN(role=("، وَهِيَ بَيَانِيَّةٌ تُبَيِّنُ مَا", "; this مِنْ explains «what»", "; beyâniyye min — «şey»i açıklar")), MAJR("بِنَاءٍ", "bina", punct="،"),
  HATTA_IBT(), DUAL_MADI("عَادَا", "ada-return", ["hollow-verbs"]), ILA(),
  MA_MAWSULA("جَرٍّ بِإِلَى", "jarr after إِلَى", "mecrûr (ilâ ile)", ["huruf-jarr"]),
  tok("كَانَا", "kana", "verb", ["kana-wa-akhawatuha", "al-muthanna", "al-bariz-al-muttasil", "hollow-verbs"],
      "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهُ" + SILA_[0] + ".",
      "كَانَ, the defective past verb, built on fatha; the alif of the two is its noun, in the seat of raf'" + SILA_[1] + ".",
      "Nâkıs mâzî kâne, fetha üzere mebnî; tesniye elifi ismi, mahallen merfû" + SILA_[2] + ".",
      segments=[seg("كَانَ", "kana", "verb"), seg("ا", "pron-3d", "pron")]),
  ALAYHI(punct=".")]})
NOTE(S5[-1]["tokens"][-1], " — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ، وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", "; the jarr phrase is the predicate of كَانَ, and its pronoun returns to the relative", "; câr-mecrûr kâne'nin haberi; zamir mevsûle döner")
S5.append({"id": "s3", "translation": {
  "en": "Then he gave orders for the minbar which Nūr al-Dīn had ordered to be made, and it was carried from Aleppo and set in al-Aqṣā Mosque.",
  "tr": "Sonra Nûreddin'in yapılmasını emretmiş olduğu minber hakkında emir verdi; minber Halep'ten taşındı ve Mescid-i Aksâ'ya konuldu."},
 "tokens": [THUMMA(), MADI("أَمَرَ", "amara-command", hidden=True), BI_NOUN("بِالْمِنْبَرِ", "minbar", "الْمِنْبَرِ"),
  ALLADHI("jarr", "لِلْمِنْبَرِ", "the minbar", "minber"), KANA("كَانَ"), NUR_ISMK(), DIN_MI(), QAD(),
  MADI("أَمَرَ", "amara-command", hidden=True, note_ar=KH_KANA[0], note_en=KH_KANA[1], note_tr=KH_KANA[2]),
  BI_NOUN("بِصُنْعِهِ", "sun", "صُنْعِهِ", enc="هِ", extra=["masdar"], note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ عَلَى الْمَوْصُولِ", note_en=" — the pronoun returns to the relative", note_tr=" — zamir mevsûle döner", punct="،"),
  MAJHUL("فَحُمِلَ", "hamala", note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", note_en="; its deputy doer is the hidden «it»", note_tr="; nâib-i fâil gizli zamir «o»"), MIN(),
  MAJR("حَلَبَ", "halab", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar=DIPT_F2[0], note_en=DIPT_F2[1], note_tr=DIPT_F2[2]),
  MAJHUL("وَوُضِعَ", "wadaa", ["mithal-verbs"], note_ar="، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", note_en="; its deputy doer is the hidden «it»", note_tr="; nâib-i fâil gizli zamir «o»"),
  FI(), PH(MAJR("الْمَسْجِدِ", "masjid"), "al-masjid-al-aqsa"), AQSA_J(punct=".")]})
S5.append({"id": "s4", "translation": {
  "en": "Nūr al-Dīn had ordered it for nothing but this day; and so what Nūr al-Dīn had hoped for was fulfilled at the hands of Saladin.",
  "tr": "Nûreddin onu ancak bu gün için yaptırmıştı; böylece Nûreddin'in umduğu şey Selahaddin'in elleriyle gerçekleşti."},
 "tokens": [WA_MA("istinaf"), MADI("أَمَرَ", "amara-command", note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), BIHI(), NUR_F(), DIN_MI(), ILLA_HASR(),
  tok("لِهٰذَا", "li", "prep", ["huruf-jarr", "asma-al-ishara", "lam-taleel"],
      "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِأَمَرَ، وَهُمَا الْمَقْصُورُ عَلَيْهِ.",
      "The lam of purpose («for»); the demonstrative after it is built on sukun, in the seat of jarr — the jarr phrase hangs on «ordered», and it is what the statement is restricted TO.",
      "Ta'lîl lâmı («için»); işaret ismi sükûn üzere mebnî, mahallen mecrûr — câr-mecrûr «emretti»ye müteallik; hüküm ona hasredilmiştir.",
      segments=[seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")]),
  BADAL("الْيَوْمِ", "yawm", "jarr", punct="،"),
  MADI("فَتَمَّ", "tamma", ["doubled-verbs"], note_ar=" — وَالْفَاعِلُ «مَا» بَعْدَهُ", note_en="; its doer «what» follows", note_tr="; fâili «mâ» ondan sonra gelir"), ALA(),
  tok("يَدَيْ", "yad", "noun", ["al-muthanna", "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.",
      "In jarr by the ya — a dual, its nun dropped because it is annexed.", "Tesniye olduğu için yâ ile mecrûr; izâfet sebebiyle nûnu düşmüş, muzâf."),
  SALAH_MI(), DIN_MI(),
  MA_MAWSULA("رَفْعٍ فَاعِلٌ", "raf' as the doer", "merfû — fâil", ["fail"]),
  KANA("كَانَ"), NUR_ISMK(), DIN_MI(),
  MUDARI("يَرْجُوهُ", "raja", enc="هُ", naqis="و", punct=".", note_ar=KH_KANA[0] + AID[0], note_en=KH_KANA[1] + AID[1], note_tr=KH_KANA[2] + AID[2])]})
S5.append({"id": "s5", "translation": {
  "en": "The Friday prayer was held in it after it had been cut off from it for a long time, the people having gathered for it from every quarter; and at that they grew the more in joy.",
  "tr": "Uzun bir süre kesildikten sonra orada cuma namazı kılındı; insanlar her yerden onun için toplanmıştı; bununla sevinçleri daha da arttı."},
 "tokens": [MAJHUL_FEM_K("وَأُقِيمَتِ", "aqama", ["form-iv-verbs", "hollow-verbs"], hollow=True),
  NAIB("الْجُمُعَةُ", "jumua", note_ar=" — أَيْ: صَلَاةُ الْجُمُعَةِ", note_en=" — that is, the Friday prayer", note_tr=" — yani cuma namazı"),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)"), ZARF("بَعْدَ", "bada", **ZAMAN), AN_MADI("أَنِ"),
  MADI("انْقَطَعَتْ", "inqataa", ["form-vii-verbs"], fem=True, hidden=True), MINHU(),
  ZARF("زَمَنًا", "zaman-period", mudaf=False, **ZAMAN), NAAT("طَوِيلًا", "tawil-long", "nasb", punct="،"),
  tok("وَقَدِ", "qad", "part", ["al-hal-jumla-wa-rabituha", "qad-harf"],
      "الْوَاوُ حَالِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ حُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ بَعْدَهُمَا فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw opens a hal clause; قَدْ affirms the past and is voweled with kasra before the hamzat al-waṣl — the clause is a hal, in the seat of nasb.",
      "Hâl vâvı; kad tahkîk harfi, iki sâkin karşılaştığı için kesre ile harekelendi — sonraki cümle hâl olarak mahallen mansûb.",
      segments=[seg("وَ", "wa", "conj"), seg("قَدِ", "qad", "part")]),
  MADI("اجْتَمَعَ", "ijtamaa", ["form-viii-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]),
  JARR_PRON("لَهَا", "li", "لَ", "هَا", " («onun için»)"), FAIL("النَّاسُ", "nas"), MIN(),
  MAJR("كُلِّ", "kull", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("نَاحِيَةٍ", "nahiya", punct="،"),
  VERB_WAW("فَازْدَادُوا", "izdada", ["form-viii-verbs", "hollow-verbs"]), BI_DHALIKA(),
  TAMYIZ_NISBA("فَرَحًا", "farah", "ازْدَادَ فَرَحُهُمْ", "their joy increased", "sevinçleri arttı", punct=".")]})
S5.append({"id": "s6", "translation": {
  "en": "And thus Jerusalem returned to the Muslims; and Saladin's pardon on that day is people's talk to this day.",
  "tr": "İşte Beytülmakdis böylece Müslümanlara döndü; Selahaddin'in o günkü affı ise bugüne dek dillerdedir."},
 "tokens": [HAKADHA2(), MADI("عَادَ", "ada-return", ["hollow-verbs"], note_ar=FAIL_BAAD[0], note_en=FAIL_BAAD[1], note_tr=FAIL_BAAD[2]), BAYT_F(), MAQDIS_MI(),
  ILA(), MUSLIMIN_J(punct="،"),
  tok("وَعَفْوُ", "afw", "noun", ["mubtada-khabar", "idafa-definiteness", "masdar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَعَفْوُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.",
      "The waw opens a new sentence; «pardon» is the mubtada, in raf', annexed.", "Vâv isti'nâf içindir; «af» mübtedâ, merfû, muzâf.",
      segments=[seg("وَ", "wa", "conj"), seg("عَفْوُ", "afw", "noun")]),
  SALAH_MI(), DIN_MI(),
  tok("يَوْمَئِذٍ", "yawmaidhin", "noun", ["maful-fih", "idafa-definiteness", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"],
      "يَوْمَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ (وَيَجُوزُ بِنَاؤُهُ عَلَى الْفَتْحِ لِإِضَافَتِهِ إِلَى مَبْنِيٍّ)، مُضَافٌ، وَإِذْ ظَرْفٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالتَّنْوِينُ عِوَضٌ عَنْ جُمْلَةٍ مَحْذُوفَةٍ، وَكُسِرَتِ الذَّالُ لِالْتِقَاءِ السَّاكِنَيْنِ — مُتَعَلِّقٌ بِالْعَفْوِ.",
      "«On that day»: يَوْمَ is an adverb of time in nasb (it may also be built on fatha, being annexed to a built word), annexed to إِذْ, a built adverb in the seat of jarr; the tanwin stands for a dropped clause («the day when [he entered it]») and the dhal takes kasra where two quiescents met — it hangs on «pardon».",
      "«O gün»: yevme mansûb zaman zarfı (mebnî bir kelimeye muzâf olduğu için fetha üzere mebnî de olabilir), iz'e muzâf; iz mebnî zarf, mahallen mecrûr; tenvin hazfedilmiş bir cümlenin yerini tutar, iki sâkin karşılaştığı için zâl kesre aldı — «af»a müteallik."),
  KHABAR("حَدِيثُ", "hadith", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), MUDAF_ILAYH("النَّاسِ", "nas"), ILA(), MAJR("الْيَوْمِ", "yawm", punct=".")]})

CHAPS = [S1, S2, S3, S4, S5]

# ---- the lexicon: every key by lemma identity from the shelf; the entries below are new -----------------------------------
PREF = ["al-kafiya", "al-amana-wa-al-khashaba", "ashab-al-ghar", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "wasiyyat-abi-yusuf-l5", "adam-wa-iblis",
        "al-asad-wa-al-far", "al-asad-wa-al-arnab", "juha-wa-al-himar", "aqaid-ahl-al-sunna", "talkhis-al-miftah", "qisas-al-nabiyyin-2"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
FORCE = {"qatala-fight": "qisas-al-nabiyyin-4", "ma-mawsula": "al-asad-wa-al-arnab"}
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
 "hittin": {"lemma": "حِطِّين", "pos": "propn", "gloss": {"en": "Ḥiṭṭīn — a village west of Tiberias where Saladin broke the Frankish army in 583 / 1187 (a diptote place-name)", "tr": "Hıttîn — Taberiye'nin batısında bir köy; Selahaddin 583 / 1187'de Haçlı ordusunu burada bozdu (gayr-i munsarif yer adı)"}, "level": 5},
 "tabariyya": {"lemma": "طَبَرِيَّة", "pos": "propn", "gloss": {"en": "Tiberias — the town on the Sea of Galilee (a diptote: a feminine proper name)", "tr": "Taberiye — Celile Gölü kıyısındaki şehir (gayr-i munsarif: müennes özel isim)"}, "level": 5},
 "akka": {"lemma": "عَكَّا", "pos": "propn", "gloss": {"en": "Acre — the port city of the Palestinian coast (a maqṣūr name: its case vowels are estimated on the alif)", "tr": "Akkâ — Filistin sahilinde liman şehri (maksûr isim: harekeler elif üzerinde takdîrî)"}, "level": 5},
 "halab": {"lemma": "حَلَب", "pos": "propn", "gloss": {"en": "Aleppo — the city of northern Syria (a diptote: a feminine proper name)", "tr": "Halep — kuzey Şam'da şehir (gayr-i munsarif: müennes özel isim)"}, "level": 4},
 "rajab": {"lemma": "رَجَب", "root": "ر ج ب", "pos": "propn", "gloss": {"en": "Rajab — the seventh month of the Hijri year", "tr": "Recep — hicrî yılın yedinci ayı"}, "level": 4},
 "sur-wall": {"lemma": "سُور", "root": "س و ر", "pos": "noun", "plural": "أَسْوَار", "gloss": {"en": "a city wall, a rampart", "tr": "sur, şehir duvarı"}, "level": 5},
 "hisar": {"lemma": "حِصَار", "root": "ح ص ر", "pos": "noun", "gloss": {"en": "siege (a masdar of حَاصَرَ, Form III)", "tr": "kuşatma, muhasara (mufâale babından hâsara'nın masdarı)"}, "level": 5},
 "mablagh": {"lemma": "مَبْلَغ", "root": "ب ل غ", "pos": "noun", "gloss": {"en": "the extent reached, the utmost (a mīmī masdar of بَلَغَ); بَلَغَ مِنْهُ كُلَّ مَبْلَغٍ «it wore him to the utmost»", "tr": "varılan had, son derece (belağa'nın mîmî masdarı); بَلَغَ مِنْهُ كُلَّ مَبْلَغٍ «onu son haddine vardırdı»"}, "level": 6},
 "sani-deed": {"lemma": "صَنِيع", "root": "ص ن ع", "pos": "noun", "gloss": {"en": "a deed; the way one acts toward others", "tr": "yapılan iş; başkalarına karşı davranış"}, "level": 6},
 "baynama": {"lemma": "بَيْنَمَا", "root": "ب ي ن", "pos": "noun", "gloss": {"en": "while — بَيْنَ with the extra مَا; in narrative its answer is opened by the إِذْ or إِذَا of surprise", "tr": "…iken — zâid mâ ile beyne; hikâyede cevabı müfâcee iz'i veya izâ'sı ile başlar"}, "level": 6},
 "amr-qasam": {"lemma": "عَمْر", "root": "ع م ر", "pos": "noun", "gloss": {"en": "life — the form kept for oaths: لَعَمْرِي «by my life» (its predicate «is my oath» is always left unsaid)", "tr": "ömür — yeminde kullanılan biçim: لَعَمْرِي «ömrüme andolsun» (haberi «yeminimdir» daima hazfedilir)"}, "level": 6},
 "hasara": {"lemma": "حَاصَرَ", "root": "ح ص ر", "pos": "verb", "gloss": {"en": "to besiege (Form III; masdar حِصَار / مُحَاصَرَة)", "tr": "kuşatmak, muhasara etmek (mufâale; masdarı hisâr / muhâsara)"}, "level": 5},
 "bayt-al-maqdis": PHRASE("بَيْتُ الْمَقْدِسِ", 4, "Jerusalem — «the Holy House»", "Beytülmakdis — Kudüs",
    "literally «the house of the sanctuary»", "lafzen «mukaddes mekânın evi»",
    "The classical name of Jerusalem (it is also called الْقُدْسُ). Grammatically an idafa: بَيْتُ takes the case of its seat, and الْمَقْدِسِ is always in jarr.",
    "Kudüs'ün klasik adı (الْقُدْسُ da denir). Gramer bakımından izâfettir: بَيْتُ bulunduğu yerin i'râbını alır, الْمَقْدِسِ daima mecrûrdur."),
 "al-masjid-al-aqsa": PHRASE("الْمَسْجِدُ الْأَقْصَى", 4, "al-Aqṣā Mosque in Jerusalem", "Mescid-i Aksâ",
    "literally «the farthest mosque»", "lafzen «en uzak mescid»",
    "A noun with its adjective. الْأَقْصَى is a maqṣūr elative, so its case never shows: it is estimated on the alif in raf', nasb and jarr alike.",
    "Mevsûf ve sıfattır. الْأَقْصَى maksûr ism-i tafdîldir; i'râbı hiç görünmez: ref, nasb ve cerde elif üzerinde takdîrîdir."),
 "qubbat-al-sakhra": PHRASE("قُبَّةُ الصَّخْرَةِ", 4, "the Dome of the Rock in Jerusalem", "Kubbetü's-Sahra",
    "literally «the dome of the rock»", "lafzen «kayanın kubbesi»",
    "An idafa naming the domed shrine over the Rock on the Temple Mount: قُبَّةُ takes the case of its seat, الصَّخْرَةِ stays in jarr.",
    "Mescid-i Aksâ alanındaki kayanın üzerine kurulmuş kubbeli yapının adı; izâfettir: قُبَّةُ yerinin i'râbını alır, الصَّخْرَةِ mecrûr kalır."),
 "salah-al-din": PHRASE("صَلَاحُ الدِّينِ", 4, "Saladin — Ṣalāḥ al-Dīn Yūsuf ibn Ayyūb (d. 589 / 1193), sultan of Egypt and Syria", "Selahaddin — Selâhuddîn Yûsuf b. Eyyûb (ö. 589 / 1193), Mısır ve Şam sultanı",
    "literally «the rectitude of the religion»", "lafzen «dinin salâhı»",
    "An honorific (laqab) built as an idafa, the usual way such titles are formed. The first word carries the case of its seat; الدِّينِ is always in jarr.",
    "İzâfet terkibiyle kurulmuş bir lakaptır; bu tür unvanlar böyle yapılır. İlk kelime yerinin i'râbını taşır; الدِّينِ daima mecrûrdur."),
 "nur-al-din": PHRASE("نُورُ الدِّينِ", 4, "Nūr al-Dīn Maḥmūd ibn Zankī (d. 569 / 1174), ruler of Syria", "Nûreddin Mahmûd b. Zengî (ö. 569 / 1174), Şam hükümdarı",
    "literally «the light of the religion»", "lafzen «dinin nuru»",
    "An honorific built as an idafa, like صَلَاحُ الدِّينِ: نُورُ carries the case, الدِّينِ stays in jarr.",
    "صَلَاحُ الدِّينِ gibi izâfetle kurulmuş bir lakaptır: نُورُ i'râbı taşır, الدِّينِ mecrûr kalır."),
}
NEW_VERBS = {
 "hasara": _sg.derived(_sg.B3, _sg.W3, "ُ", "حَاصَر", "حَاصِر", "حَاصِر", "حِصَار / مُحَاصَرَة", "مُحَاصِر", maful="مُحَاصَر", pmz="حُوصِرَ", pmd="يُحَاصَرُ",
                       note="حَاصَرَ الْمَدِينَةَ يُحَاصِرُهَا حِصَارًا وَمُحَاصَرَةً: أَحَاطَ بِهَا وَضَيَّقَ عَلَى أَهْلِهَا — بَابُ الْمُفَاعَلَةِ."),
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
 "title": {"ar": "صَلَاحُ الدِّينِ وَالْقُدْسُ", "en": "Saladin and Jerusalem", "tr": "Selahaddin ve Kudüs"},
 "subtitle": {"ar": "يَوْمُ حِطِّينَ، وَفَتْحُ بَيْتِ الْمَقْدِسِ صُلْحًا، وَعَفْوُ الْفَاتِحِ عِنْدَ الْقُدْرَةِ — قِصَّةٌ لِلْمُسْتَوَى السَّادِسِ",
              "en": "The day of Ḥiṭṭīn, Jerusalem surrendered on terms, and the victor's pardon in the hour of power — a story for the sixth level",
              "tr": "Hıttîn günü, Kudüs'ün sulh ile teslimi ve fatihin güç yetirirken affı — altıncı seviye için bir hikâye"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ (الْمُسْتَوَى السَّادِسُ) لِخَبَرِ وَقْعَةِ حِطِّينَ وَفَتْحِ بَيْتِ الْمَقْدِسِ سَنَةَ ٥٨٣ هـ / ١١٨٧ م، عَلَى مَا يَتَّفِقُ عَلَيْهِ مَنْ رَوَاهُ: ابْنُ شَدَّادٍ فِي «النَّوَادِرِ السُّلْطَانِيَّةِ»، وَالْعِمَادُ الْإِصْفَهَانِيُّ فِي «الْفَتْحِ الْقُسِّيِّ فِي الْفَتْحِ الْقُدْسِيِّ»، وَابْنُ الْأَثِيرِ فِي «الْكَامِلِ». النَّصُّ مِنْ تَأْلِيفِ الْمَشْرُوعِ، وَلَيْسَتْ فِيهِ جُمْلَةٌ مَنْقُولَةٌ مِنْ تِلْكَ الْكُتُبِ، وَلَا آيَةٌ وَلَا حَدِيثٌ، وَلَا قَوْلٌ يُنْسَبُ إِلَى أَحَدٍ؛ وَتُرِكَتِ التَّفَاصِيلُ الْمُخْتَلَفُ فِيهَا كَمَقَادِيرِ الْفِدَاءِ وَأَعْدَادِ الْقَتْلَى.",
  "en": "ORIGINAL Level-6 graded Arabic in a classical narrative register: the battle of Ḥiṭṭīn and Saladin's recovery of Jerusalem (583 AH / 1187 CE), RETOLD FREELY along the well-attested core of the classical accounts — Ibn Shaddād (al-Nawādir al-Sulṭāniyya), ʿImād al-Dīn al-Iṣfahānī (al-Fatḥ al-Qussī fī al-Fatḥ al-Qudsī) and Ibn al-Athīr (al-Kāmil fī al-Taʾrīkh). No sentence is a quotation from these works; no āya or ḥadīth is quoted; no words are put in a historical person's mouth. Disputed details (the ransom figures, the numbers of the slain, the dating of the Miʿrāj) are left out.",
  "tr": "ÖZGÜN 6. seviye Arapça, klasik anlatı üslûbunda: Hıttîn savaşı ve Selahaddin'in Kudüs'ü geri alışı (583 h. / 1187 m.), klasik kaynakların — İbn Şeddâd (en-Nevâdirü's-Sultâniyye), İmâdüddîn el-İsfahânî (el-Fethu'l-Kussî fi'l-Fethi'l-Kudsî) ve İbnü'l-Esîr (el-Kâmil fi't-Târîh) — üzerinde birleştiği çekirdeğe bağlı kalınarak SERBESTÇE yeniden anlatılmıştır. Hiçbir cümle bu eserlerden alıntı değildir; hiçbir âyet veya hadis aktarılmamış, tarihî bir şahsın ağzına söz konmamıştır. İhtilaflı ayrıntılar (fidye miktarları, ölü sayıları, Mi'rac'ın tarihi) dışarıda bırakılmıştır.",
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
