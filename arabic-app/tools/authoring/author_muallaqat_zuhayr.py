"""Author content/samples/muallaqat-zuhayr — «مُعَلَّقَةُ زُهَيْرِ بْنِ أَبِي سُلْمَى», a RECEIVED text at Level 6 (Master).

Ten chapters. Chapter 1 is the poet's khabar, VERBATIM from Ibn Qutayba, «الشعر والشعراء» (Dār al-Ḥadīth, Cairo 1423,
1/144, §§ 212–213; shamela.ws/book/23785/137). Chapters 2–10 are the WHOLE Muʿallaqa — all 62 verses, none left out —
in al-Zawzanī's text, order and count («شرح المعلقات السبع», shamela.ws/book/11253/143–162): vv. 1–7, 8–15, 16–21, 22–27,
28–34, 35–40, 41–48, 49–55, 56–62 (PLAN, below). A verse is ONE sentence; the last token of its first hemistich carries
punctAfter "•". The iʿrāb of every token was checked against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب
المعلقات العشر الطوال» (shamela.ws/book/151017/808–901) and is written in the shelf's own wording; the balāgha is named on
the token that carries it, after the syntax, in the categories of al-Qazwīnī's Talkhīṣ. The verbatim source lives in
research/sources/muallaqat-zuhayr-src.txt.

History of the file: the verses were written in two passes (first a selection — S2..S6 — then the rest, through VV()
into EXTRA), so they are filed by verse number and the chapters are cut from that sequence. DIV lists every departure
from the edition's print with its witness; FLAGS the editorial vowels left for the scholar.

Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_zuhayr.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-zuhayr"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre
import sarf_gen as _sg

PRON.update({"هُمُ": "pron-3mp", "هِمْ": "pron-3mp", "هُمْ": "pron-3mp", "هَا": "pron-3fs", "هِ": "pron-3ms", "هُ": "pron-3ms", "كُمْ": "pron-2mp", "هُمَا": "pron-3d", "كَ": "pron-2ms"})
PRON_AR.update({"هُمُ": "هُمْ", "هِمْ": "هُمْ", "هُمْ": "هُمْ", "هَا": "هَا", "هِ": "الْهَاءُ", "هُ": "الْهَاءُ", "كُمْ": "كُمْ", "هُمَا": "هُمَا", "كَ": "الْكَافُ"})

def T(full, lex, pos, g, ar, en, tr, p=None, segs=None):
    return tok(full, lex, pos, g, ar, en, tr, punct=p, segments=segs)
def SG(*triples): return [seg(f, l, q) for f, l, q in triples]
def PH(t, lex, span=2):
    t["phrase"] = {"lex": lex, "span": span}
    return t
def W(*triples):
    out = ["", "", ""]
    for m in triples: out = [a + b for a, b in zip(out, m)]
    return dict(note_ar=out[0], note_en=out[1], note_tr=out[2])
def HEM(t):
    """the last word of the first hemistich: the reader centres the verse and draws its ornament from this mark alone"""
    t["punctAfter"] = "•"
    return t

MUD = ("، مُضَافٌ", ", annexed", ", muzâf")
FAIL_BAAD = ("، وَالْفَاعِلُ بَعْدَهُ", "; its doer follows", "; fâili ondan sonra gelir")
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; söylenen söz mef'ûlün bihtir")
SILA_ = (" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the relative's ṣila and has no seat of its own", "; cümle sıla cümlesidir, i'râbdan mahalli yoktur")
# the rhyme: the poem's rawī is a mīm with kasra, the qāfiya is muṭlaqa (al-Zawzanī on v. 1)
RAWI_J = (" — وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ وَأُشْبِعَتْ كَسْرَةُ الرَّوِيِّ", " — at the rhyme its tanwin is dropped and the kasra of the rawī is lengthened", " — kâfiyede tenvini düşer, revînin kesresi uzatılır")
RAWI_AL = (" — وَأُشْبِعَتْ كَسْرَةُ الرَّوِيِّ لِلْإِطْلَاقِ", " — the kasra of the rawī is lengthened, the rhyme being unbound", " — kâfiye mutlak olduğu için revînin kesresi uzatılır")
SGN = {
 "sukun": ("السُّكُونُ", "the sukun", "sükûn"),
 "kasr2": ("السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ", "the sukun — voweled with kasra because two quiescents meet (the ال after it)", "sükûn — iki sâkin karşılaştığı için kesre ile harekelendi"),
 "rawi": ("السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِلرَّوِيِّ — وَهِيَ حَرَكَةُ الْقَافِيَةِ الْمُطْلَقَةِ، تُشْبَعُ فِي الْإِنْشَادِ", "the sukun — which gives way to the kasra of the rhyme (the ḥarakat al-rawī: the qāfiya is unbound, and the kasra is lengthened in recitation)", "sükûn — yerini revî harekesi olan kesreye bırakmıştır (kâfiye mutlaktır; kesre inşâdda uzatılır)"),
 "ya": ("حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْكَسْرَةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا", "the dropping of the weak letter (the ya), the kasra before it left as its trace", "illet harfinin (yâ'nın) hazfi; önceki kesre ona delildir"),
 "alif": ("حَذْفُ حَرْفِ الْعِلَّةِ (الْأَلِفِ)، وَالْفَتْحَةُ قَبْلَهَا دَلِيلٌ عَلَيْهَا", "the dropping of the weak letter (the alif), the fatha before it left as its trace", "illet harfinin (elifin) hazfi; önceki fetha ona delildir"),
 "nun": ("حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ", "the dropping of the nun, for it is one of the five verbs", "ef'âl-i hamseden olduğu için nûnun hazfi"),
}
HUWA = ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»", "; the doer is the hidden «he», which returns to مَنْ", "; fâil, «men»e dönen gizli zamir «o»")
NAIB_HUWA = ("، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»", "; its deputy doer is the hidden «he», which returns to مَنْ", "; nâib-i fâil, «men»e dönen gizli zamir «o»")
HIYA_HARB = ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْحَرْبِ", "; the doer is the hidden «she» — the war", "; fâil, harbe dönen gizli zamir «o»")
G_SHART = ["al-majzum-wal-shart-wal-jaza", "jawazim-al-mudari-wal-amr-fil-kafiya"]

def MAN(full, sh, jw, lead=None, seat=None, tail=("", "", "")):
    """مَنْ الشَّرْطِيَّة with its full line: the conditional noun, its seat, the condition's verb and the answer with the sign of
    each jazm. sh / jw are (ar, en, tr) triples; lead overrides the reading of the waw before it."""
    has = full[0] in "وف"
    lead = lead or ((WA_AR, "The waw conjoins; ", "«ve» + ") if has else ("", "", ""))
    seat = seat or ("فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ", "in the seat of raf' as mubtada", "mübtedâ olarak mahallen merfû")
    return tok(full, "man", "pron", G_SHART + ["mubtada-khabar", "al-mabni-wal-mudmar"],
        lead[0] + "مَنْ اسْمُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ، مَبْنِيٌّ عَلَى السُّكُونِ " + seat[0] + " — فِعْلُ الشَّرْطِ: " + sh[0] + "؛ وَجَوَابُهُ: " + jw[0] + "؛ وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُ «مَنْ»" + tail[0] + ".",
        lead[1] + "مَنْ «whoever» is the conditional noun that puts two verbs in jazm, built on sukun " + seat[1] + " — the condition's verb: " + sh[1] + "; its answer: " + jw[1] + "; the condition and its answer together are the khabar of مَنْ" + tail[1] + ".",
        lead[2] + "men «kim …-sa»: iki fiili cezmeden şart ismi, sükûn üzere mebnî, " + seat[2] + " — şart fiili: " + sh[2] + "; cevabı: " + jw[2] + "; şart ve cevap cümleleri «men»in haberidir" + tail[2] + ".",
        segments=[seg(full[:2], "wa" if full[0] == "و" else "fa", "conj"), seg("مَنْ", "man", "pron")] if has else None)
def D(word, sign):
    """«يَعِشْ» مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ … — one half of a MAN line"""
    s = SGN[sign]
    return ("«" + word + "» مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ " + s[0], "«" + word + "», in jazm, its sign " + s[1], "«" + word + "», meczûm, alâmeti " + s[2])
def JV(full, lex, role, sign, g=None, doer=HUWA, note=("", "", ""), p=None, segs=None, passive=False, pre=None):
    """a muḍāriʿ put in jazm by the conditional noun: role = shart | jawab | atf-shart | atf-jawab"""
    R = {"shart": ("لِأَنَّهُ فِعْلُ الشَّرْطِ", "as the condition's verb", "şart fiili olarak"),
         "jawab": ("لِأَنَّهُ جَوَابُ الشَّرْطِ", "as the answer of the condition", "şartın cevabı olarak"),
         "atf-shart": ("مَعْطُوفٌ عَلَى فِعْلِ الشَّرْطِ", "conjoined to the condition's verb", "şart fiiline ma'tûf olarak"),
         "atf-jawab": ("مَعْطُوفٌ عَلَى جَوَابِ الشَّرْطِ", "conjoined to the answer of the condition", "şartın cevabına ma'tûf olarak")}[role]
    s = SGN[sign]
    pre = pre or ("", "", "")
    mj = (" مَبْنِيٌّ لِلْمَجْهُولِ", " passive", " meçhûl") if passive else ("", "", "")
    return tok(full, lex, "verb", G_SHART + (["al-qafiya"] if sign == "rawi" else []) + (g or []),
        pre[0] + "فِعْلٌ مُضَارِعٌ" + mj[0] + " مَجْزُومٌ " + R[0] + " وَعَلَامَةُ جَزْمِهِ " + s[0] + doer[0] + note[0] + ".",
        cap(pre[1] + "present" + mj[1] + " verb in jazm " + R[1] + ", its sign " + s[1] + doer[1] + note[1] + "."),
        cap(pre[2] + R[2] + " meczûm" + mj[2] + " muzâri, alâmeti " + s[2] + doer[2] + note[2] + "."), punct=p, segments=segs)
WA3 = (WA_AR, "The waw conjoins; ", "«ve» + ")
FA3 = (FA_AR, "The fa conjoins; ", "«fe» + ")
def cap(s): return s[:1].upper() + s[1:]

CH = {}

# =====================================================================================================================
# Chapter 1 — خَبَرُ زُهَيْرٍ (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/144, §§ 212–213 — verbatim, contiguous)
# =====================================================================================================================
DIPT_UMAR = ("، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ", " — a proper name barred from tanwin (a name turned from the pattern فَاعِل)", " — alemiyet ve adl sebebiyle gayr-i munsarif özel isim")
def RADIYA():
    return [T("رَضِيَ", "radiya", "verb", ["naqis-verbs", "khabar-fi-mana-al-insha", "jumla-mutarida"],
        "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ: خَبَرٌ لَفْظًا إِنْشَاءٌ مَعْنًى.",
        "Past verb built on fatha; its doer follows — a parenthetical prayer with no seat of its own: a report in form, a request in meaning («may God be pleased with him»).",
        "Fetha üzere mebnî mâzî; fâili ondan sonra gelir — i'râbdan mahalli olmayan dua cümlesi (mu'tarıza): lafzen haber, mânen inşâ («Allah ondan razı olsun»)."),
      ALLAH_F(),
      JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَضِيَ»", note_en="; the phrase hangs on «be pleased»", note_tr="; câr-mecrûr «razı oldu»ya müteallik")]
def QALA_(full="قَالَ", who=None, p=":"):
    """قَالَ with a hidden doer named in the line"""
    pr = _pre(full)
    return T(full, "qala", "verb", ["hollow-verbs", "maful-bihi"],
        pr[3] + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + who[0] + "، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ.",
        pr[4] + "past verb built on fatha; the doer is the hidden «he»" + who[1] + "; what is said is its object.",
        pr[5] + "fetha üzere mebnî mâzî; fâil gizli zamir «o»" + who[2] + "; söylenen söz mef'ûlün bihtir.", p=p,
        segs=[pr[2], seg(pr[1], "qala", "verb")] if pr[2] else None)

S1 = []
S1.append({"id": "s1", "translation": {
  "en": "Abū ʿUbayda said: Those who rank Zuhayr above all the poets say that he is the best of them at praise and the tightest of them in the weave of his verse.",
  "tr": "Ebû Ubeyde dedi ki: Züheyr'i bütün şairlerden üstün tutanlar şöyle der: O, şairlerin en iyi medheden ve şiirinin örgüsü en sağlam olanıdır."},
 "tokens": [MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD, MAQUL)),
  PH(T("أَبُو", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"],
     "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.",
     "The doer, in raf' by the waw — one of the five nouns — and annexed.",
     "Fâil; esmâ-i hamseden olduğu için vâv ile merfû, muzâf."), "abu-ubayda"),
  MUDAF_ILAYH("عُبَيْدَةَ", "ubayda", "propn", ["mamnu-min-sarf"], sign=FATHA_JARR, note_ar="، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ — وَأَبُو عُبَيْدَةَ: مَعْمَرُ بْنُ الْمُثَنَّى", note_en=" — by the fatha: a proper name with the feminine ta, barred from tanwin (Abū ʿUbayda is Maʿmar ibn al-Muthannā)", note_tr=" — fetha ile: lafzî te'nîsli özel isim, gayr-i munsarif (Ebû Ubeyde: Ma'mer b. el-Müsennâ)", punct=":"),
  T("يَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", "maful-bihi"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ «قَالَ».",
     "Present verb in raf'; its doer follows, and what is said is its object — the clause is what Abū ʿUbayda said, in the seat of nasb.",
     "Merfû muzâri; fâili ondan sonra gelir, söylenen söz mef'ûlün bihtir — cümle «dedi»nin mekûlü, mahallen mansûb."),
  T("مَنْ", "man-mawsula", "pron", ["ism-mawsul", "fail"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ «يَقُولُ».",
     "A relative noun «those who», built on sukun, in the seat of raf' as the doer of «say».",
     "İsm-i mevsûl «…-en kimse(ler)», sükûn üzere mebnî; «der»in fâili olarak mahallen merfû."),
  MADI("فَضَّلَ", "faddala", ["form-ii-verbs"], note_ar="، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»" + SILA_[0], note_en="; the doer is the hidden «he», returning to مَنْ" + SILA_[1], note_tr="; fâil «men»e dönen gizli zamir" + SILA_[2]),
  MAFUL("زُهَيْرًا", "zuhayr", "propn"),
  ALA(), MAJR("جَمِيعِ", "jami", **W(MUD)),
  MUDAF_ILAYH("الشُّعَرَاءِ", "shair", extra=["jam-taksir"], note_ar=" — جَمْعُ شَاعِرٍ عَلَى فُعَلَاءَ", note_en=" — the plural of «poet», on the pattern فُعَلَاء", note_tr=" — şâir'in fu'alâ vezninde cem'i", punct=":"),
  T("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha", "mawadi-kasr-inna", "al-bariz-al-muttasil"],
     "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ — كُسِرَتْ هَمْزَتُهَا لِوُقُوعِهَا بَعْدَ الْقَوْلِ — وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا، يَعُودُ عَلَى زُهَيْرٍ.",
     "إِنَّ, the particle of emphasis that puts its noun in nasb — its hamza takes kasra because it follows «say» — and the attached «he» (Zuhayr) is its noun, in the seat of nasb.",
     "İnne: te'kîd ve nasb harfi — kavlden sonra geldiği için hemzesi kesrelidir — bitişik zamir (Züheyr) ismidir, mahallen mansûb.",
     segs=SG(("إِنَّ", "inna", "part"), ("هُ", "pron-3ms", "pron"))),
  T("أَمْدَحُ", "amdah", "noun", ["inna-wa-akhawatuha", "ism-tafdil", "idafa-definiteness"],
     "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ مِنْ مَدَحَ.",
     "The predicate of إِنَّ, in raf' and annexed — the elative of «to praise»: «the best at praise».",
     "İnne'nin haberi, merfû, muzâf — «medh etmek»ten ism-i tafdîl: «en iyi medheden»."),
  MUDAF_ILAYH("الْقَوْمِ", "qawm", note_ar=" — أَيِ الشُّعَرَاءِ", note_en=" — «the company» is the poets", note_tr=" — «kavim» burada şairlerdir"),
  T("وَأَشَدُّهُمْ", "ashadd", "noun", ["atf-nasaq", "ism-tafdil", "idafa-definiteness", "al-bariz-al-muttasil"],
     WA_AR + "أَشَدُّ مَعْطُوفٌ عَلَى «أَمْدَحُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "The waw conjoins; «the strongest» is joined to «the best at praise», in raf'; it is annexed to the attached «them», in the seat of jarr.",
     "«ve» + «en şiddetlisi»: «en iyi medheden»e ma'tûf, merfû; bitişik zamire muzâf, zamir mahallen mecrûr.",
     segs=SG(("وَ", "wa", "conj"), ("أَشَدُّ", "ashadd", "noun"), ("هُمْ", "pron-3mp", "pron"))),
  T("أَسْرَ", "asr-weave", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "idafa-definiteness"],
     "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالْأَسْرُ: إِحْكَامُ الصُّنْعِ وَشَدُّهُ.",
     "A tamyiz, in nasb, annexed — الْأَسْر is the tight binding of a thing's make: «strongest in the weave of verse».",
     "Temyîz, mansûb, muzâf — «esr»: bir şeyin yapısının sıkı ve sağlam örülmesi."),
  MUDAF_ILAYH("شِعْرٍ", "shir", punct=".")]})
S1.append({"id": "s2", "translation": {
  "en": "He said: And I heard Abū ʿAmr ibn al-ʿAlāʾ say: al-Farazdaq is likened to Zuhayr.",
  "tr": "Dedi ki: Ebû Amr b. el-Alâ'yı şöyle derken işittim: Ferezdak, Züheyr'e benzetilir."},
 "tokens": [QALA_("قَالَ", (" يَعُودُ عَلَى أَبِي عُبَيْدَةَ", " (Abū ʿUbayda)", " (Ebû Ubeyde)")),
  MADI_T("وَسَمِعْتُ", "samia", who="ana", note_ar=" — وَالْوَاوُ تَعْطِفُ هٰذَا الْخَبَرَ عَلَى مَا تَقَدَّمَ مِنْ كَلَامِهِ", note_en=" — the waw joins this report to what he said before", note_tr=" — vâv bu haberi onun önceki sözüne bağlar"),
  PH(T("أَبَا", "ab", "noun", ["maful-bihi", "five-nouns", "idafa-definiteness"],
     "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.",
     "The direct object, in nasb by the alif — one of the five nouns — and annexed.",
     "Mef'ûlün bih; esmâ-i hamseden olduğu için elif ile mansûb, muzâf."), "abu-amr-ibn-al-ala", 4),
  MUDAF_ILAYH("عَمْرِو", "amr-name", "propn", note_ar=" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْن» مُضَافًا إِلَى عَلَمٍ، وَالْوَاوُ فِي آخِرِهِ لِلْفَرْقِ بَيْنَهُ وَبَيْنَ «عُمَر»", note_en=" — its tanwin drops because the name is described by «son of» + a name; the final waw is only written, to tell it from ʿUmar", note_tr=" — «ibn» ile vasıflanıp başka bir aleme muzâf olduğu için tenvini düşer; sondaki vâv yalnızca «Ömer»den ayırmak için yazılır"),
  T("بْنَ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
     "نَعْتٌ لِـ«أَبَا عَمْرٍو» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
     "A na't of «Abū ʿAmr», in nasb and annexed — its alif is dropped because it stands between two names.",
     "«Ebû Amr»ın na'tı, mansûb, muzâf — iki alem arasında olduğu için elifi yazılmaz."),
  MUDAF_ILAYH("الْعَلَاءِ", "ala-name", "propn"),
  MUDARI("يَقُولُ", "qala", ["hollow-verbs", "hal", "al-hal-jumla-wa-rabituha"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «أَبَا عَمْرٍو»، وَمَقُولُ الْقَوْلِ مَا بَعْدَهُ", note_en=" — the clause is a hal of «Abū ʿAmr», in the seat of nasb; what he says follows", note_tr=" — cümle «Ebû Amr»dan hâl, mahallen mansûb; söylenen söz ondan sonradır", punct=":"),
  MUBTADA("الْفَرَزْدَقُ", "farazdaq", "propn", note_ar=" — لَقَبُ الشَّاعِرِ هَمَّامِ بْنِ غَالِبٍ", note_en=" — the byname of the poet Hammām ibn Ghālib", note_tr=" — şair Hemmâm b. Gâlib'in lakabı"),
  T("يُشَبَّهُ", "shabbaha", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mudari-marfu", "form-ii-verbs", "anwa-al-khabar"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.",
     "A present verb in the passive, in raf'; its deputy doer is the hidden «he» — the clause is the khabar, in the seat of raf'.",
     "Meçhul muzâri, merfû; nâib-i fâil gizli zamir «o» — cümle mübtedânın haberi, mahallen merfû."),
  BI_NOUN("بِزُهَيْرٍ", "zuhayr", "زُهَيْرٍ", pos="propn", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُشَبَّهُ»", note_en="; the phrase hangs on «is likened»", note_tr="; câr-mecrûr «benzetilir»e müteallik", punct=".")]})
S1.append({"id": "s3", "translation": {
  "en": "And al-Aṣmaʿī used to say: Zuhayr, al-Ḥuṭayʾa and their like are the slaves of poetry, because they refined it and did not take it the way of the naturally gifted.",
  "tr": "Asmaî de şöyle derdi: Züheyr, Hutay'e ve benzerleri şiirin köleleridir; çünkü onu ayıklayıp düzelttiler ve onda tabiatıyla söyleyenlerin yolunu tutmadılar."},
 "tokens": [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "anwa-al-waw"],
     WA_ISTINAF[0] + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
     WA_ISTINAF[1] + "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb.",
     WA_ISTINAF[2] + "kâne: nâkıs mâzî fiil; ismini ref, haberini nasb eder.",
     segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  ISMK("الْأَصْمَعِيُّ", "asmai", "propn", ["ism-mansub"]),
  MUDARI_KH("يَقُولُ", "qala", ["hollow-verbs"], punct=":"),
  MUBTADA("زُهَيْرٌ", "zuhayr", "propn"),
  ATF("وَالْحُطَيْئَةُ", "hutaya", "propn", note_ar=" — لَقَبُ الشَّاعِرِ جَرْوَلِ بْنِ أَوْسٍ", note_en=" — the byname of the poet Jarwal ibn Aws", note_tr=" — şair Cervel b. Evs'in lakabı"),
  T("وَأَشْبَاهُهُمَا", "shibh", "noun", ["atf-nasaq", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
     WA_AR + "أَشْبَاهُ مَعْطُوفٌ عَلَى «زُهَيْرٌ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ شِبْهٍ.",
     "The waw conjoins; «the likes» (plural of شِبْه) is joined to «Zuhayr», in raf'; it is annexed to the attached «of the two», in the seat of jarr.",
     "«ve» + «benzerleri» (şibh'in cem'i): «Züheyr»e ma'tûf, merfû; bitişik tesniye zamirine muzâf, zamir mahallen mecrûr.",
     segs=SG(("وَ", "wa", "conj"), ("أَشْبَاهُ", "shibh", "noun"), ("هُمَا", "pron-3d", "pron"))),
  KHABAR("عَبِيدُ", "abd", ["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ عَبْدٍ؛ سَمَّاهُمْ عَبِيدَ الشِّعْرِ لِطُولِ خِدْمَتِهِمْ إِيَّاهُ بِالتَّنْقِيحِ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ", note_en=", annexed — the plural of «slave»: he calls them poetry's slaves for their long service of it in revising — the sentence is what al-Aṣmaʿī said", note_tr=", muzâf — abd'in cem'i: şiire uzun uzun hizmet edip onu ayıkladıkları için «şiirin köleleri» demiştir — cümle mekûlü'l-kavldir"),
  MUDAF_ILAYH("الشِّعْرِ", "shir", punct="،"),
  T("لِأَنَّهُمْ", "lianna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "huruf-jarr"],
     "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ.",
     "The lam is a jarr letter of cause; أَنَّ puts its noun in nasb, and the attached «they» is that noun — the masdar the clause builds is in jarr by the lam.",
     "Lâm ta'lîl için cer harfi; enne te'kîd ve nasb harfi; bitişik zamir ismidir, mahallen mansûb — müevvel masdar lâm ile mecrûr.",
     segs=SG(("لِ", "li", "prep"), ("أَنَّ", "anna", "part"), ("هُمْ", "pron-3mp", "pron"))),
  VERB_WAW_ENC("نَقَّحُوهُ", "naqqaha", "هُ", ["form-ii-verbs"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ؛ وَالتَّنْقِيحُ: تَهْذِيبُ الْكَلَامِ وَتَخْلِيصُ جَيِّدِهِ مِنْ رَدِيئِهِ", note_en=" — the clause is the predicate of أَنَّ, in the seat of raf'; تَنْقِيح is pruning speech and sifting its good from its bad", note_tr=" — cümle enne'nin haberi, mahallen merfû; tenkîh: sözü budayıp iyisini kötüsünden ayıklamak"),
  WA_LAM(),
  FIVE_JAZM("يَذْهَبُوا", "dhahaba", "لَمْ", "لَمْ", "lem"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onu»)", note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ: ذَهَبَ بِهِ أَيْ سَارَ بِهِ", note_en="; the ba makes the verb transitive: «to go with it» is to take it", note_tr="; bâ ta'diye içindir: «onunla gitti», yani onu götürdü"),
  T("مَذْهَبَ", "madhhab", "noun", ["maful-mutlaq", "idafa-definiteness"],
     "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَهُوَ مَصْدَرٌ مِيمِيٌّ مِنْ ذَهَبَ.",
     "A maf'ul mutlaq that states the kind, in nasb, annexed — a mimi masdar of «to go»: «the way of …».",
     "Nev'i bildiren mef'ûl-i mutlak, mansûb, muzâf — «gitmek»ten mîmî masdar: «…-in gidişiyle»."),
  T("الْمَطْبُوعِينَ", "matbu-gifted", "noun", ["idafa-definiteness", "jam-mudhakkar-salim", "ism-maful"],
     "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَالْمَطْبُوعُ: مَنْ يَقُولُ الشِّعْرَ عَلَى طَبْعِهِ مِنْ غَيْرِ تَكَلُّفٍ.",
     "The second term of the idafa, in jarr by the ya, a sound masculine plural — the مَطْبُوع is the poet who speaks by his nature, without labouring.",
     "Muzâfun ileyh; cem-i müzekker sâlim olduğu için yâ ile mecrûr — «matbû'»: zorlanmadan, tabiatıyla şiir söyleyen.", p=".")]})
S1.append({"id": "s4", "translation": {
  "en": "He said: And Zuhayr used to call the greatest of his odes «the year-long ones».",
  "tr": "Dedi ki: Züheyr, kasidelerinin en büyüklerine «Havliyyât» (yıllıklar) adını verirdi."},
 "tokens": [QALA_("قَالَ", (" يَعُودُ عَلَى أَبِي عُبَيْدَةَ", " (Abū ʿUbayda)", " (Ebû Ubeyde)")),
  KANA("وَكَانَ"),
  ISMK("زُهَيْرٌ", "zuhayr", "propn"),
  T("يُسَمِّي", "samma", "verb", ["kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs", "form-ii-verbs", "mafulayn"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَيَنْصِبُ مَفْعُولَيْنِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
     "Present verb in raf' by a damma estimated on the ya; the doer is the hidden «he»; it takes two objects — the clause is the predicate of كَانَ, in the seat of nasb.",
     "Yâ üzerinde takdîrî damme ile merfû muzâri; fâil gizli zamir «o»; iki mef'ûl alır — cümle kâne'nin haberi, mahallen mansûb."),
  T("كُبَرَ", "kubra", "noun", ["maful-bihi", "mafulayn", "idafa-definiteness", "jam-taksir"],
     "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — جَمْعُ كُبْرَى، أَيْ قَصَائِدَهُ الْكُبَرَ (وَالضَّبْطُ مِنَ الْمُحَرِّرِ، وَلَمْ يُشْكَلْ فِي الْمَطْبُوعِ).",
     "The first object, in nasb, annexed — the plural of كُبْرَى «the greatest»: «the great ones of his odes» (the vowels are editorial; the edition prints the word bare).",
     "Birinci mef'ûlün bih, mansûb, muzâf — kübrâ'nın cem'i: «kasidelerinin en büyükleri» (harekeler editoryaldir; baskıda kelime harekesizdir)."),
  T("قَصَائِدِهِ", "qasida", "noun", ["idafa-definiteness", "jam-taksir", "al-bariz-al-muttasil"],
     "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ قَصِيدَةٍ.",
     "The second term of the idafa, in jarr; annexed to the attached «his», in the seat of jarr — the plural of «ode».",
     "Muzâfun ileyh, mecrûr; bitişik zamire muzâf, zamir mahallen mecrûr — kasîde'nin cem'i.",
     segs=SG(("قَصَائِدِ", "qasida", "noun"), ("هِ", "pron-3ms", "pron"))),
  T("الْحَوْلِيَّاتِ", "hawliyyat", "noun", ["maful-bihi", "mafulayn", "jam-muannath-salim", "ism-mansub"],
     "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ — نِسْبَةٌ إِلَى الْحَوْلِ وَهُوَ السَّنَةُ.",
     "The second object, in nasb by the kasra that stands for the fatha — a sound feminine plural; a nisba to الْحَوْل «the year»: odes worked over for a whole year.",
     "İkinci mef'ûlün bih; cem-i müennes sâlim olduğu için fetha yerine kesre ile mansûb — «havl»e (yıl) nisbet: üzerinde bir yıl çalışılan kasideler.", p=".")]})
S1.append({"id": "s5", "translation": {
  "en": "And the best of his poetry was on Harim ibn Sinān al-Murrī.",
  "tr": "Şiirinin en güzeli de Herim b. Sinân el-Mürrî hakkındaydı."},
 "tokens": [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "anwa-al-waw"],
     WA_ISTINAF[0] + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
     WA_ISTINAF[1] + "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb.",
     WA_ISTINAF[2] + "kâne: nâkıs mâzî fiil; ismini ref, haberini nasb eder.",
     segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  ISMK("جَيِّدُ", "jayyid", **W(MUD)),
  ENC_NOUN("شِعْرِهِ", "shir", "هِ", "mudaf"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ", "; the jarr phrase hangs on the omitted predicate of كَانَ", " — câr-mecrûr kâne'nin mahzûf haberine müteallik")),
  PH(MAJR("هَرِمِ", "harim", "propn", note_ar=" — وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْن» مُضَافًا إِلَى عَلَمٍ", note_en=" — its tanwin drops because the name is described by «son of» + a name", note_tr=" — «ibn» ile vasıflanıp başka bir aleme muzâf olduğu için tenvini düşer"), "harim-ibn-sinan", 3),
  T("بْنِ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
     "نَعْتٌ لِـ«هَرِمِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
     "A na't of «Harim», in jarr and annexed — its alif is dropped because it stands between two names.",
     "«Herim»in na'tı, mecrûr, muzâf — iki alem arasında olduğu için elifi yazılmaz."),
  MUDAF_ILAYH("سِنَانٍ", "sinan-name", "propn"),
  T("الْمُرِّيِّ", "murri", "noun", ["naat-sifa", "ism-mansub"],
     "نَعْتٌ ثَانٍ لِـ«هَرِمِ» مَجْرُورٌ بِالْكَسْرَةِ — نِسْبَةٌ إِلَى مُرَّةَ بْنِ عَوْفٍ مِنْ ذُبْيَانَ.",
     "A second na't of «Harim», in jarr — a nisba to Murra ibn ʿAwf, a clan of Dhubyān.",
     "«Herim»in ikinci na'tı, mecrûr — Zübyân'dan Mürre b. Avf'a nisbet.", p=".")]})
S1.append({"id": "s6", "translation": {
  "en": "ʿUmar — may God be pleased with him — said to one of Harim's sons: Recite to me some of what Zuhayr said about you. So he recited it to him,",
  "tr": "Ömer — Allah ondan razı olsun — Herim'in oğullarından birine: «Züheyr'in sizin hakkınızda söylediklerinden bir kısmını bana oku» dedi; o da ona okudu,"},
 "tokens": [MADI("وَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD, MAQUL)),
  FAIL("عُمَرُ", "umar", "propn", ["mamnu-min-sarf"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", **W(DIPT_UMAR)),
  *RADIYA(),
  T("لِبَعْضِ", "li", "prep", ["huruf-jarr", "idafa-definiteness"],
     "اللَّامُ حَرْفُ جَرٍّ، وَبَعْضِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ».",
     "The lam is a jarr letter; «one of» is in jarr and annexed — the phrase hangs on «said».",
     "Lâm cer harfi; «biri» mecrûr, muzâf — câr-mecrûr «dedi»ye müteallik.",
     segs=SG(("لِ", "li", "prep"), ("بَعْضِ", "bad", "noun"))),
  MUDAF_ILAYH("وَلَدِ", "walad", note_ar="، مُضَافٌ — وَالْوَلَدُ يَقَعُ عَلَى الْوَاحِدِ وَالْجَمْعِ", note_en=", annexed — وَلَد serves for one child and for many", note_tr=", muzâf — «veled» tekil için de çoğul için de kullanılır"),
  MUDAF_ILAYH("هَرِمٍ", "harim", "propn", punct=":"),
  AMR("أَنْشِدْنِي", "anshada", ["form-iv-verbs", "mafulayn"], enc="نِي", wiqaya=True, note_ar=" — وَالْيَاءُ مَفْعُولُهُ الْأَوَّلُ", note_en=" — the ya is its first object", note_tr=" — yâ birinci mef'ûldür"),
  MAFUL("بَعْضَ", "bad", extra=["mafulayn", "idafa-definiteness"], note_ar="، مُضَافٌ — وَهُوَ الْمَفْعُولُ الثَّانِي", note_en=", annexed — the second object", note_tr=", muzâf — ikinci mef'ûl"),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "A relative noun «what», built on sukun, in the seat of jarr as the second term of the idafa.",
     "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî; muzâfun ileyh olarak mahallen mecrûr."),
  MADI("قَالَ", "qala", ["hollow-verbs", "ism-mawsul"], note_ar=FAIL_BAAD[0] + "، وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: قَالَهُ" + SILA_[0], note_en=FAIL_BAAD[1] + "; the pronoun returning to مَا is dropped («what he said [it]»)" + SILA_[1], note_tr=FAIL_BAAD[2] + "; «mâ»ya dönen âid zamir hazfedilmiştir" + SILA_[2]),
  JARR_PRON("فِيكُمْ", "fi", "فِي", "كُمْ", " («sizin hakkınızda»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَالَ»", note_en="; the phrase hangs on «said»", note_tr="; câr-mecrûr «söyledi»ye müteallik"),
  FAIL("زُهَيْرٌ", "zuhayr", "propn", punct="،"),
  ENC_MADI("فَأَنْشَدَهُ", "anshada", "هُ", ["form-iv-verbs"], hidden=True, note_ar=" — وَالْفَاعِلُ وَلَدُ هَرِمٍ وَالْهَاءُ لِعُمَرَ، وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ", note_en=" — the doer is Harim's son and «him» is ʿUmar; the second object is left out", note_tr=" — fâil Herim'in oğlu, «ona» Ömer'dir; ikinci mef'ûl hazfedilmiştir", punct="،")]})
S1.append({"id": "s7", "translation": {
  "en": "and ʿUmar said: Truly he used to speak of you, and speak well. He said: Commander of the Faithful, we used to give to him, and give richly!",
  "tr": "Ömer: «Gerçekten o sizin hakkınızda söyler ve güzel söylerdi» dedi. O da: «Ey müminlerin emîri, biz de ona verir, bol bol verirdik!» dedi."},
 "tokens": [QALA_("فَقَالَ", (" يَعُودُ عَلَى عُمَرَ", " (ʿUmar)", " (Ömer)")),
  T("لَقَدْ", "qad", "part", ["qad-harf", "huruf-al-qasam-fil-kafiya"],
     "اللَّامُ وَاقِعَةٌ فِي جَوَابِ قَسَمٍ مُقَدَّرٍ، وَقَدْ حَرْفُ تَحْقِيقٍ.",
     "The lam opens the answer of an unspoken oath, and قَدْ affirms the past verb after it.",
     "Lâm, takdîr edilen bir yeminin cevabını açar; kad tahkîk harfidir.",
     segs=SG(("لَ", "lam-qasam", "part"), ("قَدْ", "qad", "part"))),
  KANA_HID("كَانَ", note=(" يَعُودُ عَلَى زُهَيْرٍ", " (Zuhayr)", " (Züheyr)")),
  MUDARI_KH("يَقُولُ", "qala", ["hollow-verbs"]),
  JARR_PRON("فِيكُمْ", "fi", "فِي", "كُمْ", " («sizin hakkınızda»)"),
  T("فَيُحْسِنُ", "ahsana", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs"],
     FA_AR + "يُحْسِنُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ مَعْطُوفٌ عَلَى «يَقُولُ»، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
     "The fa conjoins; «does well» is a present verb in raf', joined to «speaks»; the doer is the hidden «he».",
     "«fe» + «güzel yapar»: «söyler»e ma'tûf merfû muzâri; fâil gizli zamir «o».",
     p="،", segs=SG(("فَ", "fa", "conj"), ("يُحْسِنُ", "ahsana", "verb"))),
  QALA_("فَقَالَ", (" يَعُودُ عَلَى وَلَدِ هَرِمٍ", " (Harim's son)", " (Herim'in oğlu)")),
  YA(),
  T("أَمِيرَ", "amir", "noun", ["vocative-munada", "idafa-definiteness"],
     "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "The one called — annexed, so in nasb.", "Muzâf münâdâ, mansûb."),
  T("الْمُؤْمِنِينَ", "mumin", "noun", ["idafa-definiteness", "jam-mudhakkar-salim", "ism-fail"],
     "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
     "The second term of the idafa, in jarr by the ya — a sound masculine plural.",
     "Muzâfun ileyh; cem-i müzekker sâlim olduğu için yâ ile mecrûr."),
  T("إِنَّا", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil"],
     "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَحُذِفَتْ إِحْدَى النُّونَاتِ تَخْفِيفًا.",
     "إِنَّ, the particle of emphasis that puts its noun in nasb; the attached «we» is its noun — one of the three nuns is dropped for lightness.",
     "İnne: te'kîd ve nasb harfi; bitişik «biz» zamiri ismidir, mahallen mansûb — nûnlardan biri hafiflik için düşmüştür.",
     segs=SG(("إِنَّ", "inna", "part"), ("نَا", "pron-1p", "pron"))),
  T("كُنَّا", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "al-bariz-al-muttasil"],
     "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهَا — وَأُدْغِمَتْ نُونُ الْفِعْلِ فِي نُونِ الضَّمِيرِ؛ وَجُمْلَةُ كَانَ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.",
     "كَانَ, the defective past verb, built on sukun because نَا is attached; that «we» is its noun, in the seat of raf' — the verb's nun is merged into the pronoun's; the كَانَ clause is the predicate of إِنَّ, in the seat of raf'.",
     "Kâne: «nâ» bitiştiği için sükûn üzere mebnî nâkıs mâzî; «nâ» ismidir, mahallen merfû — fiilin nûnu zamirin nûnuna idgam edilmiştir; kâne cümlesi inne'nin haberi, mahallen merfû.",
     segs=SG(("كُنْ", "kana", "verb"), ("نَا", "pron-1p", "pron"))),
  T("نُعْطِيهِ", "aata", "verb", ["kana-wa-akhawatuha", "mudari-marfu", "naqis-verbs", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi", "hadhf-al-maful"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ، وَالثَّانِي مَحْذُوفٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
     "Present verb in raf' by a damma estimated on the ya; the doer «we» must stay hidden; the attached «him» is its first object and the second is left out — the clause is the predicate of كَانَ, in the seat of nasb.",
     "Yâ üzerinde takdîrî damme ile merfû muzâri; fâil vücûben gizli «biz»; bitişik «ona» birinci mef'ûl, ikincisi mahzûf — cümle kâne'nin haberi, mahallen mansûb.",
     segs=SG(("نُعْطِي", "aata", "verb"), ("هِ", "pron-3ms", "pron"))),
  T("فَنُجْزِلُ", "ajzala", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs", "hadhf-al-maful"],
     FA_AR + "نُجْزِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ مَعْطُوفٌ عَلَى «نُعْطِيهِ»، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ، وَالْمَفْعُولُ مَحْذُوفٌ أَيِ الْعَطَاءَ.",
     "The fa conjoins; «give richly» is a present verb in raf', joined to «give to him»; the doer «we» must stay hidden, and its object («the gift») is left out.",
     "«fe» + «bol veririz»: «ona veririz»e ma'tûf merfû muzâri; fâil vücûben gizli «biz»; mef'ûlü («atâyı») mahzûf.",
     p="!", segs=SG(("فَ", "fa", "conj"), ("نُجْزِلُ", "ajzala", "verb")))]})
S1.append({"id": "s8", "translation": {
  "en": "Then ʿUmar — may God be pleased with him — said: What you gave him is gone, and what he gave you has remained.",
  "tr": "Bunun üzerine Ömer — Allah ondan razı olsun — şöyle dedi: Sizin ona verdiğiniz gitti; onun size verdiği ise kaldı."},
 "tokens": [MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD, MAQUL)),
  FAIL("عُمَرُ", "umar", "propn", ["mamnu-min-sarf"], sign="بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ", **W(DIPT_UMAR)),
  *RADIYA()[:2], RADIYA()[2] | {"punctAfter": ":"},
  MADI("ذَهَبَ", "dhahaba", ["tibaq", "muqabala"], note_ar=FAIL_BAAD[0] + " — وَفِيهِ طِبَاقٌ بَيْنَ «ذَهَبَ» وَ«بَقِيَ»، وَمُقَابَلَةٌ بَيْنَ الْجُمْلَتَيْنِ: ذَهَبَ ↔ بَقِيَ، مَا أَعْطَيْتُمُوهُ ↔ مَا أَعْطَاكُمْ", note_en=FAIL_BAAD[1] + " — a tibaq of «is gone» and «has remained», and a muqabala of the two clauses: gone ↔ remained, what you gave him ↔ what he gave you", note_tr=FAIL_BAAD[2] + " — «gitti» ile «kaldı» arasında tıbâk, iki cümle arasında mukâbele vardır: gitti ↔ kaldı, sizin verdiğiniz ↔ onun verdiği"),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ «ذَهَبَ» — وَهُوَ الْمَالُ.",
     "A relative noun «what», built on sukun, in the seat of raf' as the doer of «is gone» — the wealth.",
     "İsm-i mevsûl «…-diğiniz şey», sükûn üzere mebnî; «gitti»nin fâili olarak mahallen merfû — yani mal."),
  T("أَعْطَيْتُمُوهُ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "fail", "mafulayn", "ism-mawsul"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْوَاوُ لِإِشْبَاعِ ضَمَّةِ الْمِيمِ قَبْلَ الضَّمِيرِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَهِيَ إِمَّا لِزُهَيْرٍ وَالْعَائِدُ مَحْذُوفٌ، وَإِمَّا الْعَائِدُ عَلَى «مَا» وَالْمَفْعُولُ الْأَوَّلُ مَحْذُوفٌ" + SILA_[0] + ".",
     "Past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer, in the seat of raf'; the waw only lengthens the mim's damma before the pronoun; the attached هُ is an object — either «him» (Zuhayr), with the pronoun returning to مَا left out, or that returning pronoun itself, with the first object left out" + SILA_[1] + ".",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir, mahallen merfû; vâv, zamirden önce mîmin dammesini işbâ' içindir; bitişik «hû» mef'ûlün bihtir — ya Züheyr'e döner ve âid mahzûftur, ya da «mâ»ya dönen âiddir ve birinci mef'ûl mahzûftur" + SILA_[2] + ".",
     segs=SG(("أَعْطَيْتُمُو", "aata", "verb"), ("هُ", "pron-3ms", "pron"))),
  MADI("وَبَقِيَ", "baqiya", ["naqis-verbs", "tibaq"], **W(FAIL_BAAD)),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ «بَقِيَ» — وَهُوَ الْمَدِيحُ.",
     "A relative noun «what», built on sukun, in the seat of raf' as the doer of «has remained» — the praise.",
     "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî; «kaldı»nın fâili olarak mahallen merfû — yani medih."),
  T("أَعْطَاكُمْ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "mafulayn", "ism-mawsul"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى زُهَيْرٍ، وَكُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ، وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: أَعْطَاكُمُوهُ" + SILA_[0] + ".",
     "Past verb built on a fatha estimated on the alif; the doer is the hidden «he» (Zuhayr); the attached كُمْ «you» is its first object, and the pronoun returning to مَا is left out" + SILA_[1] + ".",
     "Elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil Züheyr'e dönen gizli zamir «o»; bitişik «küm» birinci mef'ûl, «mâ»ya dönen âid mahzûf" + SILA_[2] + ".",
     p=".", segs=SG(("أَعْطَا", "aata", "verb"), ("كُمْ", "pron-2mp", "pron")))]})
CH[1] = S1

# =====================================================================================================================
# Chapter 2 — أَطْلَالُ أُمِّ أَوْفَى (al-Zawzanī vv. 1–6)
# =====================================================================================================================
def LAM_J(full="لَمْ"): return LAM_JAZM(full)
def LAM_V(full, lex, who, whose, g=None, note=("", "", ""), p="."):
    """a muḍāriʿ in jazm by لَمْ at the rhyme: the sukun gives way to the kasra of the rawī"""
    return T(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "al-qafiya"] + (g or []),
        "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + who + whose[0] + note[0] + ".",
        "Present verb in jazm by لَمْ, its sign " + SGN["rawi"][1] + "; the doer is the hidden pronoun" + whose[1] + note[1] + ".",
        "Lem ile meczûm muzâri, alâmeti " + SGN["rawi"][2] + "; fâil gizli zamir" + whose[2] + note[2] + ".", p=p)

def V(S, en, tr, first, second):
    """one verse = one sentence: «•» closes the first hemistich, a full stop the verse"""
    first, second = [t for t in first if t], [t for t in second if t]
    first[-1]["punctAfter"] = "•"
    second[-1].setdefault("punctAfter", ".")
    S.append({"id": "s%d" % (len(S) + 1), "translation": {"en": en, "tr": tr}, "tokens": first + second})

S2 = []
# ---- v. 1 ----
V(S2, "Is it of Umm Awfā's dwellings — a blackened trace that does not speak, at Ḥawmānat al-Darrāj and al-Mutathallam?",
  "Havmânetü'd-Derrâc ile Mütesellem'deki, konuşmayan (soruya cevap vermeyen) şu kararmış yurt izi, Ümmü Evfâ'nın konak yerlerinden midir?",
 [T("أَمِنْ", "min", "prep", ["al-istifham", "huruf-jarr", "taqdim-al-musnad", "hadhf-al-mudaf-wal-mudaf-ilayh", "ilm-al-arud"],
     "الْهَمْزَةُ حَرْفُ اسْتِفْهَامٍ، وَمِنْ حَرْفُ جَرٍّ لِلتَّبْعِيضِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، عَلَى حَذْفِ مُضَافٍ: أَمِنْ مَنَازِلِ أُمِّ أَوْفَى. وَالِاسْتِفْهَامُ خَرَجَ مَخْرَجَ الشَّكِّ: لِبُعْدِ عَهْدِهِ بِالدِّمْنَةِ وَفَرْطِ تَغَيُّرِهَا لَمْ يَعْرِفْهَا مَعْرِفَةَ قَطْعٍ (الزَّوْزَنِيُّ). وَالْقَصِيدَةُ مِنَ الْبَحْرِ الطَّوِيلِ.",
     "The hamza is the particle of question and مِنْ a jarr letter of «part of» — the jarr phrase hangs on the omitted, FRONTED khabar, with an annexed word left out: «is it of [the dwellings of] Umm Awfā…?». The question is cast as doubt: so long is it since he saw the trace, and so changed is it, that he does not know it for certain (al-Zawzanī). The ode is in the metre al-ṭawīl.",
     "Hemze istifhâm harfi, «min» teb'îz bildiren cer harfi — câr-mecrûr, öne alınmış mahzûf habere müteallik; muzâf hazfedilmiştir: «Ümmü Evfâ'nın [konak yerlerinden] midir?». İstifhâm şek kalıbında gelmiştir: izi görmeyeli çok olduğu ve iz çok değiştiği için onu kesin olarak tanıyamamıştır (Zevzenî). Kaside tavîl bahrindendir.",
     segs=SG(("أَ", "hamza-istifham", "part"), ("مِنْ", "min", "prep"))),
  PH(MAJR("أُمِّ", "umm", **W(MUD)), "umm-awfa"),
  MUDAF_ILAYH("أَوْفَى", "awfa-name", "propn", ["ism-maqsur-manqus", "mamnu-min-sarf"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ نِيَابَةً عَنِ الْكَسْرَةِ", note_ar="، عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ — وَأُمُّ أَوْفَى كُنْيَةُ الْحَبِيبَةِ", note_en=" — by a fatha estimated on the alif, standing for the kasra: a proper name on a verb's pattern, barred from tanwin; Umm Awfā is the beloved's kunya", note_tr=" — kesre yerine elif üzerinde takdîrî fetha ile: fiil vezninde özel isim, gayr-i munsarif; Ümmü Evfâ sevgilinin künyesidir"),
  MUBTADA("دِمْنَةٌ", "dimna", note_ar=" — مُبْتَدَأٌ مُؤَخَّرٌ، وَسَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ تَقَدُّمُ الْخَبَرِ وَهُوَ شِبْهُ جُمْلَةٍ", note_en=" — placed after its khabar: an indefinite may stand as mubtada when its khabar, a jarr phrase, goes before it", note_tr=" — haberinden sonraya bırakılmıştır: haber şibh-i cümle olup öne geçtiği için nekre mübtedâ olabilmiştir"),
  LAM_JAZM("لَمْ"),
  T("تَكَلَّمِ", "takallama", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-v-verbs", "al-qafiya", "jumla-sifa", "majaz-aqli"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + " — وَأَصْلُهُ تَتَكَلَّمْ فَحُذِفَتْ إِحْدَى التَّاءَيْنِ — وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الدِّمْنَةِ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«دِمْنَةٌ». وَإِسْنَادُ التَّكَلُّمِ إِلَى الدِّمْنَةِ مَجَازٌ عَقْلِيٌّ عَلَى قَوْلِ مَنْ قَالَ: الْمُرَادُ لَمْ يَتَكَلَّمْ أَهْلُهَا (الدُّرَّةُ)؛ وَفَسَّرَهُ الزَّوْزَنِيُّ: لَا تُجِيبُ سُؤَالَهَا.",
     "Present verb in jazm by لَمْ, its sign " + SGN["rawi"][1] + " — it is تَتَكَلَّمْ with one of its two ta's dropped — the doer is the hidden «she» (the trace), and the clause is a na't of «a trace», in the seat of raf'. To give «speaking» to the trace is a majaz of attribution on the reading «its people do not speak» (al-Durra); al-Zawzanī glosses: «it does not answer when asked».",
     "Lem ile meczûm muzâri, alâmeti " + SGN["rawi"][2] + " — aslı «tetekellem»dir, iki tâ'dan biri hazfedilmiştir — fâil ize dönen gizli zamir «o»; cümle «dimne»nin na'tı, mahallen merfû. Konuşmanın ize isnadı, «halkı konuşmuyor» demek olduğunu söyleyenlere göre mecâz-ı aklîdir (Dürre); Zevzenî «sorusuna cevap vermez» diye açıklar.")],
 [T("بِحَوْمَانَةِ", "bi", "prep", ["huruf-jarr", "idafa-definiteness"],
     "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَحَوْمَانَةِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«دِمْنَةٌ».",
     "The ba is a jarr letter meaning «in»; «Ḥawmāna» is in jarr and annexed — the jarr phrase hangs on an omitted second na't of «a trace».",
     "Bâ «-de» anlamında cer harfi; «Havmâne» mecrûr, muzâf — câr-mecrûr, «dimne»nin mahzûf ikinci na'tına müteallik.",
     segs=SG(("بِ", "bi", "prep"), ("حَوْمَانَةِ", "hawmana", "noun"))),
  MUDAF_ILAYH("الدَّرَّاجِ", "darraj", "propn", note_ar=" — اسْمُ مَوْضِعٍ؛ بِفَتْحِ الدَّالِ، وَقَالَ أَبُو عَمْرٍو بِضَمِّهَا (الدُّرَّةُ)", note_en=" — a place-name; with fatha on the dal, and Abū ʿAmr read it with damma (al-Durra)", note_tr=" — yer adı; dâl'ın fethasıyla, Ebû Amr ise dammesiyle okumuştur (Dürre)"),
  T("فَالْمُتَثَلَّمِ", "mutathallam", "propn", ["atf-nasaq", "al-qafiya"],
     "الْفَاءُ عَاطِفَةٌ، وَالْمُتَثَلَّمِ مَعْطُوفٌ عَلَى «حَوْمَانَةِ» مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَوْضِعٍ" + RAWI_AL[0] + ".",
     "The fa conjoins; «al-Mutathallam», a place-name, is joined to «Ḥawmāna», in jarr" + RAWI_AL[1] + ".",
     "Fâ atıf harfi; yer adı «Mütesellem», «Havmâne»ye ma'tûf, mecrûr" + RAWI_AL[2] + ".",
     segs=SG(("فَ", "fa", "conj"), ("الْمُتَثَلَّمِ", "mutathallam", "propn")))])
# ---- v. 2 ----
V(S2, "And [is it of hers] a dwelling at al-Raqmatān, whose traces are like the retraced lines of a tattoo in the sinews of a wrist?",
  "Ve Rakmeteyn'de ona ait, [izleri] bir bileğin damarlarındaki yenilenmiş dövme çizgilerine benzeyen bir yurt [onun konaklarından mıdır]?",
 [ATF("وَدَارٌ", "dar", sign="مَرْفُوعٌ بِالضَّمَّةِ", note_ar=" — عُطِفَ عَلَى «دِمْنَةٌ»، أَيْ: أَمِنْ مَنَازِلِهَا دَارٌ؛ وَأَرَادَ دَارَيْنِ فَاجْتَزَأَ بِالْوَاحِدِ عَنِ التَّثْنِيَةِ لِزَوَالِ اللَّبْسِ (الزَّوْزَنِيُّ)", note_en=" — joined to «a trace»: «is it of her dwellings — a house …?»; he means two houses and lets the singular stand for the dual, there being no room for confusion (al-Zawzanī)", note_tr=" — «dimne»ye atfedilmiştir: «onun konaklarından bir yurt mudur?»; iki yurt kastedilmiş, karışıklık olmadığı için tekil tesniye yerine yetmiştir (Zevzenî)"),
  LAHU2("لَهَا", "pron-3fs", " («onun»)", note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«دَارٌ»", "; the phrase hangs on an omitted na't of «a house»", "; câr-mecrûr «dâr»ın mahzûf na'tına müteallik")),
  T("بِالرَّقْمَتَيْنِ", "bi", "prep", ["huruf-jarr", "al-muthanna"],
     "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَالرَّقْمَتَيْنِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«دَارٌ».",
     "The ba is a jarr letter meaning «in»; «al-Raqmatān» is in jarr by the ya, being a dual — the phrase hangs on an omitted second na't of «a house».",
     "Bâ «-de» anlamında cer harfi; «Rakmeteyn» tesniye olduğu için yâ ile mecrûr — câr-mecrûr «dâr»ın mahzûf ikinci na'tına müteallik.",
     segs=SG(("بِ", "bi", "prep"), ("الرَّقْمَتَيْنِ", "raqmatan", "propn"))),
  T("كَأَنَّهَا", "kaanna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "tashbih", "aqsam-al-tashbih", "hadhf-al-mudaf-wal-mudaf-ilayh"],
     "كَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا، عَلَى حَذْفِ مُضَافٍ: كَأَنَّ رُسُومَهَا — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَالِثٌ لِـ«دَارٌ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ رُسُومُ الدَّارِ، وَالْمُشَبَّهُ بِهِ مَرَاجِيعُ الْوَشْمِ فِي نَوَاشِرِ الْمِعْصَمِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الظُّهُورُ بَعْدَ الِانْمِحَاءِ: السُّيُولُ تُجَدِّدُ الرُّسُومَ بِكَشْفِ التُّرَابِ عَنْهَا كَمَا يُجَدَّدُ الْوَشْمُ (الزَّوْزَنِيُّ).",
     "كَأَنَّ «as if» is the particle of likening that puts its noun in nasb; the attached هَا is that noun, with an annexed word left out: «as if its traces» — the clause is a third na't of «a house», in the seat of raf'. Here is a tashbih mursal mujmal: the thing likened is the traces of the house; the thing it is likened to, the retraced lines of a tattoo in the sinews of a wrist; the tool is كَأَنَّ; the point of likeness is left unsaid — showing again after fading: the torrents renew the traces by stripping the dust from them, as a tattoo is renewed (al-Zawzanī).",
     "Keenne: teşbîh ve nasb harfi; bitişik «hâ» ismidir, mahallen mansûb; muzâf hazfedilmiştir: «sanki izleri» — cümle «dâr»ın üçüncü na'tı, mahallen merfû. Burada mürsel mücmel bir teşbîh vardır: müşebbeh yurdun izleri; müşebbehün bih bir bileğin damarlarındaki yenilenmiş dövme çizgileri; edat «keenne»; vech-i şebeh hazfedilmiştir — silindikten sonra yeniden belirmek: seller toprağı sıyırarak izleri yeniler, tıpkı dövmenin yenilenmesi gibi (Zevzenî).",
     segs=SG(("كَأَنَّ", "kaanna", "part"), ("هَا", "pron-3fs", "pron")))],
 [T("مَرَاجِيعُ", "marju-retraced", "noun", ["inna-wa-akhawatuha", "jam-taksir", "idafa-definiteness", "tashbih"],
     "خَبَرُ كَأَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — جَمْعُ مَرْجُوعٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ؛ وَهُوَ الْمُشَبَّهُ بِهِ.",
     "The predicate of كَأَنَّ, in raf', annexed — the plural of مَرْجُوع «gone over again», on the pattern of the farthest plurals; it is the thing the traces are likened to.",
     "Keenne'nin haberi, merfû, muzâf — «mercû'»un («üzerinden yeniden geçilmiş») muntehe'l-cumû' vezninde cem'i; müşebbehün bihtir."),
  MUDAF_ILAYH("وَشْمٍ", "washm"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «مَرَاجِيعُ وَشْمٍ»", "; the jarr phrase hangs on an omitted hal of «the retraced lines of a tattoo»", " — câr-mecrûr «dövme çizgileri»nin mahzûf hâline müteallik")),
  MAJR("نَوَاشِرِ", "nashir", extra=["jam-taksir", "idafa-definiteness", "mamnu-min-sarf"], note_ar="، مُضَافٌ — جَمْعُ نَاشِرٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَجُرَّ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ", note_en=", annexed — the plural of نَاشِر, a «farthest plural» (a diptote), yet in jarr by the kasra because it is annexed", note_tr=", muzâf — «nâşir»in muntehe'l-cumû' vezninde cem'i (gayr-i munsarif), muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("مِعْصَمِ", "misam", extra=["al-qafiya"], **W(RAWI_J))])
# ---- v. 3 ----
V(S2, "In it the wide-eyed wild cows and the white gazelles walk herd after herd, and their young rise from every place where they lay.",
  "Orada iri gözlü yaban sığırları ile ak ceylanlar, sürü sürü birbiri ardınca yürür; yavruları da yattıkları her yerden kalkar.",
 [JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)", extra=["taqdim-al-musnad"], note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ", note_en="; the ba means «in», and the phrase hangs on the omitted, fronted khabar", note_tr="; bâ «-de» anlamındadır; câr-mecrûr öne alınmış mahzûf habere müteallik"),
  MUBTADA("الْعِينُ", "ayan-wide-eyed", extra=["jam-taksir", "ijaz-al-hadhf", "sifa-mushabbaha"], note_ar=" — مُبْتَدَأٌ مُؤَخَّرٌ؛ جَمْعُ عَيْنَاءَ وَأَعْيَنَ. وَفِيهِ إِيجَازٌ بِحَذْفِ الْمَوْصُوفِ: أَيِ الْبَقَرُ الْعِينُ، حُذِفَ لِدَلَالَةِ الصِّفَةِ عَلَيْهِ (الزَّوْزَنِيُّ)", note_en=" — placed after its khabar; the plural of عَيْنَاء / أَعْيَن «wide-eyed». Here is brevity by dropping the thing described: «the wide-eyed [cows]», dropped because the quality points to it (al-Zawzanī)", note_tr=" — haberinden sonraya bırakılmıştır; «aynâ' / a'yen»in («iri gözlü») cem'i. Burada mevsûfun hazfiyle îcâz vardır: «iri gözlü [sığırlar]»; sıfat ona delâlet ettiği için hazfedilmiştir (Zevzenî)"),
  ATF("وَالْأَرْآمُ", "rim", extra=["jam-taksir"], note_ar=" — جَمْعُ رِئْمٍ وَهُوَ الظَّبْيُ الْأَبْيَضُ", note_en=" — the plural of رِئْم, the pure-white gazelle", note_tr=" — «ri'm»in cem'i: bembeyaz ceylan"),
  T("يَمْشِينَ", "masha", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail", "hal", "al-hal-jumla-wa-rabituha"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْعِينِ وَالْأَرْآمِ عَلَى مَذْهَبِ سِيبَوَيْهِ، وَعِنْدَ الْجُمْهُورِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لَهُمَا (الدُّرَّةُ).",
     "Present verb built on sukun because the nun of the women is attached; that nun is the doer, in the seat of raf' — the clause is a hal of «the wide-eyed and the gazelles», in the seat of nasb, on Sībawayh's view; for the majority it is their na't, in the seat of raf' (al-Durra).",
     "Nûn-ı nisve bitiştiği için sükûn üzere mebnî muzâri; nûn fâildir, mahallen merfû — cümle Sîbeveyh'e göre «sığırlar ve ceylanlar»dan hâl, mahallen mansûb; cumhura göre onların na'tı, mahallen merfû (Dürre)."),
  HAL("خِلْفَةً", "khilfa", note_ar="، وَصَاحِبُهُ نُونُ النِّسْوَةِ: يَخْلُفُ بَعْضُهَا بَعْضًا", note_en=" — its owner is the nun of «walk»: one herd coming after another", note_tr=" — sahibi nûn-ı nisvedir: bir sürü gidince öbürü gelir")],
 [T("وَأَطْلَاؤُهَا", "tala-fawn", "noun", ["mubtada-khabar", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
     WA_AR + "أَطْلَاءُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ طَلًا وَهُوَ وَلَدُ الظَّبْيَةِ وَالْبَقَرَةِ الْوَحْشِيَّةِ.",
     "The waw conjoins; «the young» is a mubtada, in raf'; it is annexed to the attached «their», in the seat of jarr — the plural of طَلًا, the young of the gazelle and the wild cow.",
     "«ve» + «yavruları»: mübtedâ, merfû; bitişik zamire muzâf, zamir mahallen mecrûr — «talâ»nın cem'i: ceylan ve yaban sığırı yavrusu.",
     segs=SG(("وَ", "wa", "conj"), ("أَطْلَاؤُ", "tala-fawn", "noun"), ("هَا", "pron-3fs", "pron"))),
  T("يَنْهَضْنَ", "nahada", "verb", ["al-bariz-al-muttasil", "fail", "anwa-al-khabar"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.",
     "Present verb built on sukun because the nun of the women is attached; that nun is the doer — the clause is the khabar, in the seat of raf'.",
     "Nûn-ı nisve bitiştiği için sükûn üzere mebnî muzâri; nûn fâildir — cümle mübtedânın haberi, mahallen merfû."),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَنْهَضْنَ»", "; the phrase hangs on «rise»", " — câr-mecrûr «kalkarlar»a müteallik")),
  MAJR("كُلِّ", "kull", **W(MUD)),
  MUDAF_ILAYH("مَجْثَمِ", "majtham", extra=["al-qafiya"], note_ar=" — اسْمُ مَكَانٍ مِنْ جَثَمَ يَجْثُمُ: مَوْضِعُ الْجُثُومِ، وَيُرْوَى «مَجْثِمِ» مِنْ يَجْثِمُ" + RAWI_J[0], note_en=" — a noun of place from جَثَمَ يَجْثُمُ: the spot where a beast lies down; also read مَجْثِمِ, from يَجْثِمُ" + RAWI_J[1], note_tr=" — «cesm etmek»ten ism-i mekân: hayvanın çöküp yattığı yer; «mecsim» diye de rivayet edilir" + RAWI_J[2])])
# ---- v. 4 ----
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
V(S2, "I stopped there after twenty years, and only with toil did I know the dwelling, after taking thought.",
  "Yirmi yıl sonra orada durdum; yurdu ancak güçlükle, epey düşünüp tahmin ettikten sonra tanıdım.",
 [MADI_T("وَقَفْتُ", "waqafa", who="ana", extra=["mithal-verbs"]),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («orada»)", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَقَفْتُ»", note_en="; the ba means «in», and the phrase hangs on «I stopped»", note_tr="; bâ «-de» anlamındadır; câr-mecrûr «durdum»a müteallik"),
  MIN(),
  MAJR("بَعْدِ", "bada", **W(MUD, (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وَقَفْتُ»", "; the phrase hangs on «I stopped»", "; câr-mecrûr «durdum»a müteallik"))),
  MUDAF_ILAYH("عِشْرِينَ", "ishrun", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_en=" — by the ya: «twenty» is declined like the sound masculine plural", note_tr=" — yâ ile: «yirmi» cem-i müzekker sâlime mülhaktır"),
  TAMYIZ("حِجَّةً", "hijja-year")],
 [T("فَلَأْيًا", "lay", "noun", ["maful-mutlaq", "hal", "hadhf-al-maful"],
     "الْفَاءُ عَاطِفَةٌ، وَلَأْيًا مَنْصُوبٌ عَلَى الْمَصْدَرِيَّةِ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ لِـ«عَرَفْتُ»، وَقِيلَ: حَالٌ مِنَ التَّاءِ أَيْ جَاهِدًا، وَقِيلَ: ظَرْفٌ عَلَى حَذْفِ مُضَافٍ أَيْ بَعْدَ لَأْيٍ (الدُّرَّةُ). وَقُدِّمَ عَلَى عَامِلِهِ لِلِاهْتِمَامِ: لَمْ يُثْبِتْهَا إِلَّا بَعْدَ جَهْدٍ وَمَشَقَّةٍ (الزَّوْزَنِيُّ).",
     "The fa conjoins; لَأْيًا «with toil» is in nasb as a masdar standing for the maf'ul mutlaq of «I knew»; some read it as a hal of the «I» («toiling»), others as an adverb with an annexed word dropped («after toil») (al-Durra). It is put before its verb because it is what matters: he made the place out only after effort and hardship (al-Zawzanī).",
     "Fâ atıf harfi; «le'yen» («güçlükle»), «tanıdım»ın mef'ûl-i mutlakı yerine masdar olarak mansûb; bir görüşe göre tâ'dan hâl («zorlanarak»), bir görüşe göre muzâfı hazfedilmiş zarftır («güçlükten sonra») (Dürre). Önem verildiği için âmilinden öne alınmıştır: orayı ancak zahmet ve meşakkatten sonra tanıyabilmiştir (Zevzenî).",
     segs=SG(("فَ", "fa", "conj"), ("لَأْيًا", "lay", "noun"))),
  MADI_T("عَرَفْتُ", "arafa", who="ana"),
  MAFUL("الدَّارَ", "dar"),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«عَرَفْتُ»", note_en=", hanging on «I knew»", note_tr="; «tanıdım»a müteallik"),
  MUDAF_ILAYH("تَوَهُّمِ", "tawahhum", extra=["masdar", "al-qafiya"], **W(RAWI_J))])
# ---- v. 5 ----
V(S2, "— soot-black hearth-stones where a cauldron once stood, and a trench like the base of a water-trough, not yet broken down.",
  "— bir kazanın konduğu yerde isten kararmış ocak taşları ve bir havuzun dibi gibi, henüz yıkılmamış bir çadır arkı.",
 [T("أَثَافِيَّ", "uthfiyya", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "jam-taksir", "mamnu-min-sarf"],
     "بَدَلٌ مِنَ «الدَّارَ» فِي الْبَيْتِ قَبْلَهُ — بَدَلُ بَعْضٍ مِنْ كُلٍّ — مَنْصُوبٌ بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ؛ جَمْعُ أُثْفِيَّةٍ.",
     "A badal of «the dwelling» in the verse before — a part for the whole — in nasb by the fatha with no tanwin, a diptote on the pattern of the farthest plurals; the plural of أُثْفِيَّة «hearth-stone».",
     "Önceki beyitteki «yurdu»dan bedel — bedel-i ba'z mine'l-kül — tenvinsiz fetha ile mansûb; muntehe'l-cumû' vezninde gayr-i munsarif; «üsfiyye»nin («ocak taşı») cem'i."),
  NAAT("سُفْعًا", "asfa", "nasb", extra=["jam-taksir"], note_ar=" — جَمْعُ أَسْفَعَ وَسَفْعَاءَ: السُّودُ", note_en=" — the plural of أَسْفَع / سَفْعَاء «soot-black»", note_tr=" — «esfa' / sef'â'»nın cem'i: isten kararmış"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«أَثَافِيَّ»", "; the jarr phrase hangs on an omitted second na't of «hearth-stones»", " — câr-mecrûr «ocak taşları»nın mahzûf ikinci na'tına müteallik")),
  MAJR("مُعَرَّسِ", "muarras", extra=["istiara", "idafa-definiteness"], note_ar="، مُضَافٌ — اسْمُ مَكَانٍ مِنَ التَّعْرِيسِ وَهُوَ النُّزُولُ وَقْتَ السَّحَرِ. وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَ مَنْزِلُ الْمُسَافِرِ لِلْمَكَانِ الَّذِي تُنْصَبُ فِيهِ الْقِدْرُ (الزَّوْزَنِيُّ)", note_en=", annexed — a noun of place from تَعْرِيس, the traveller's halt before dawn. Here is an isti'ara tasrihiyya: the traveller's halting-place is lent to the spot where the pot is set (al-Zawzanī)", note_tr=", muzâf — «ta'rîs»ten (seher vakti konaklama) ism-i mekân. Burada istiâre-i tasrîhiyye vardır: yolcunun konak yeri, kazanın kurulduğu yer için ödünç alınmıştır (Zevzenî)"),
  MUDAF_ILAYH("مِرْجَلٍ", "mirjal")],
 [ATF("وَنُؤْيًا", "nuy", case="nasb", note_ar=" — عُطِفَ عَلَى «أَثَافِيَّ»", note_en=" — joined to «hearth-stones»", note_tr=" — «ocak taşları»na atfedilmiştir"),
  T("كَجِذْمِ", "ka", "prep", ["huruf-jarr", "idafa-definiteness", "tashbih", "aqsam-al-tashbih"],
     "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَجِذْمِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«نُؤْيًا». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ النُّؤْيُ، وَالْمُشَبَّهُ بِهِ جِذْمُ الْحَوْضِ أَيْ أَصْلُهُ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ غَيْرُ مَذْكُورٍ؛ وَ«لَمْ يَتَثَلَّمِ» وَصْفٌ لِلْمُشَبَّهِ يُومِئُ إِلَيْهِ: بَقِيَ غَيْرَ مُتَثَلِّمٍ كَأَنَّهُ أَصْلُ حَوْضٍ (الزَّوْزَنِيُّ).",
     "The kaf is a jarr letter of likening; «base» is in jarr and annexed — the jarr phrase hangs on an omitted na't of «a trench». Here is a tashbih mursal mujmal: the thing likened is the trench; the thing it is likened to, the base of a trough; the tool is the kaf; the point of likeness is not stated — «not broken down», a description of the trench, hints at it: it has stayed whole, like the base of a trough (al-Zawzanī).",
     "Kâf cer ve teşbîh harfi; «dip» mecrûr, muzâf — câr-mecrûr «ark»ın mahzûf na'tına müteallik. Burada mürsel mücmel bir teşbîh vardır: müşebbeh çadır arkı; müşebbehün bih havuzun dibi; edat kâf; vech-i şebeh zikredilmemiştir — müşebbehin vasfı olan «yıkılmamış» ona işaret eder: bir havuzun dibi gibi sapasağlam kalmıştır (Zevzenî).",
     segs=SG(("كَ", "ka", "prep"), ("جِذْمِ", "jidhm", "noun"))),
  MUDAF_ILAYH("الْحَوْضِ", "hawd"),
  LAM_JAZM("لَمْ"),
  LAM_V("يَتَثَلَّمِ", "tathallama", "هُوَ", (" يَعُودُ عَلَى النُّؤْيِ", " «it» (the trench)", " «o» (ark)"), g=["form-v-verbs", "jumla-sifa"],
        note=(" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِـ«نُؤْيًا»", " — the clause is a second na't of «a trench», in the seat of nasb", " — cümle «ark»ın ikinci na'tı, mahallen mansûb"))])
# ---- v. 6 ----
V(S2, "When I knew the dwelling I said to its ground: A good morning to you, O dwelling-ground, and peace be yours!",
  "Yurdu tanıyınca onun konak yerine şöyle dedim: Sabahın hayrolsun ey konak yeri, selâmette ol!",
 [LAMMA2("فَلَمَّا"),
  MADI_T("عَرَفْتُ", "arafa", who="ana", **W(LAMMA_CL)),
  MAFUL("الدَّارَ", "dar"),
  MADI_T("قُلْتُ", "qala", who="ana", extra=["hollow-verbs"], note_ar=" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ، وَمَقُولُ الْقَوْلِ مَا بَعْدَهُ", note_en="; the clause is the answer of لَمَّا and has no seat; what is said follows", note_tr="; cümle lemmâ'nın cevabıdır, mahalli yoktur; söylenen söz ondan sonradır"),
  LI_ENC("لِرَبْعِهَا", "rab", "رَبْعِ", "هَا", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قُلْتُ»", note_en="; the phrase hangs on «I said»", note_tr="; câr-mecrûr «dedim»e müteallik")],
 [T("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"],
     "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ لَا عَمَلَ لَهُ.", "A particle of opening and alerting; it governs nothing.", "İstiftâh ve tenbîh harfi; ameli yoktur."),
  T("انْعَمْ", "naima", "verb", ["imperative-amr", "al-amr-wa-wujuhuh", "al-fail-al-mudmar-al-mustatir-wujuban"],
     "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ. وَالْأَمْرُ خَرَجَ إِلَى الدُّعَاءِ وَالتَّحِيَّةِ: طَابَ عَيْشُكَ فِي صَبَاحِكَ (الزَّوْزَنِيُّ)؛ وَفِيهِ لُغَةٌ أُخْرَى: عِمْ صَبَاحًا.",
     "Imperative built on sukun; the doer «you» must stay hidden — the clause is what is said, in the seat of nasb. The command has left its own sense for prayer and greeting: «may your life be sweet this morning» (al-Zawzanī); the greeting is also said عِمْ صَبَاحًا.",
     "Sükûn üzere mebnî emir; fâil vücûben gizli «sen» — cümle mekûlü'l-kavl, mahallen mansûb. Emir, asıl mânâsından dua ve selâma çıkmıştır: «sabahında yaşayışın hoş olsun» (Zevzenî); «ım sabâhan» şekli de vardır."),
  ZARF("صَبَاحًا", "sabah", mudaf=False, **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«انْعَمْ»، وَقِيلَ: تَمْيِيزٌ مُحَوَّلٌ عَنِ الْفَاعِلِ (الدُّرَّةُ)", note_en=", hanging on «be at ease»; some read it as a tamyiz turned from the doer (al-Durra)", note_tr="; «in'am»a müteallik; bir görüşe göre fâilden çevrilmiş temyîzdir (Dürre)"),
  T("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "al-mabni-ghayr-al-lazim-al-maqtu-an-al-idafa-wal-munada"],
     "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَهَا حَرْفُ تَنْبِيهٍ. وَنَادَى الرَّبْعَ وَهُوَ لَا يَعْقِلُ، فَنَزَّلَهُ مَنْزِلَةَ مَنْ يُخَاطَبُ وَيُحَيَّا.",
     "The one called, with the calling particle left out: an intended indefinite, built on damma in the seat of nasb; هَا is a particle of alerting. He calls the dwelling-ground, a thing without reason, and so treats it as one who can be spoken to and greeted.",
     "Nidâ harfi hazfedilmiş münâdâ: nekre-i maksûde, damme üzere mebnî, mahallen mansûb; «hâ» tenbîh harfi. Akıl sahibi olmayan konak yerine seslenerek onu hitap edilen ve selâmlanan biri yerine koymuştur.",
     segs=SG(("أَيُّ", "ayyuha", "noun"), ("هَا", "ha-tanbih", "part"))),
  T("الرَّبْعُ", "rab", "noun", ["badal", "atf-bayan", "vocative-munada"],
     "بَدَلٌ مِنْ «أَيُّ» أَوْ عَطْفُ بَيَانٍ عَلَيْهِ، مَرْفُوعٌ بِالضَّمَّةِ تَبَعًا لِلَفْظِهِ.",
     "A badal of أَيُّ, or its explanatory apposition ('atf bayan), in raf' after its wording.",
     "«Eyyü»den bedel yahut atf-ı beyân; onun lafzına uyarak merfû.", p="،"),
  T("وَاسْلَمِ", "salima-safe", "verb", ["imperative-amr", "al-amr-wa-wujuhuh", "atf-nasaq", "al-qafiya", "al-fail-al-mudmar-al-mustatir-wujuban"],
     WA_AR + "اسْلَمْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِلرَّوِيِّ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «انْعَمْ»، وَالْأَمْرُ لِلدُّعَاءِ.",
     "The waw conjoins; اسْلَمْ is an imperative built on sukun — here the sukun gives way to the kasra of the rhyme — and the doer «you» must stay hidden; the clause is joined to «be at ease», and the command is a prayer.",
     "«ve» + «selâmette ol»: sükûn üzere mebnî emir — sükûn burada revînin kesresine bırakılmıştır — fâil vücûben gizli «sen»; cümle «in'am»a ma'tûf; emir dua içindir.",
     segs=SG(("وَ", "wa", "conj"), ("اسْلَمِ", "salima-safe", "verb")))])
CH[2] = S2

# =====================================================================================================================
# Chapter 3 — السَّيِّدَانِ (al-Zawzanī vv. 16–21)
# =====================================================================================================================
S3 = []
# ---- v. 16 ----
V(S3, "So I swore by the House around which men have walked who built it, of Quraysh and Jurhum:",
  "Kureyş ve Cürhüm'den, onu bina eden adamların çevresinde tavaf ettiği Beyt'e yemin ettim:",
 [MADI_T("فَأَقْسَمْتُ", "aqsama", who="ana", extra=["form-iv-verbs", "khabar-insha"], note_ar=" — وَالْقَسَمُ إِنْشَاءٌ غَيْرُ طَلَبِيٍّ", note_en=" — an oath is an insha that asks for nothing", note_tr=" — yemin, talebî olmayan inşâdır"),
  BI_NOUN("بِالْبَيْتِ", "bayt", "الْبَيْتِ", note_ar=" — وَهُوَ الْكَعْبَةُ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَقْسَمْتُ»", note_en=" — «the House» is the Kaʿba; the phrase hangs on «I swore»", note_tr=" — «Beyt» Kâbe'dir; câr-mecrûr «yemin ettim»e müteallik"),
  T("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«الْبَيْتِ».", "A relative noun «which», built on sukun, in the seat of jarr as a na't of «the House».", "İsm-i mevsûl «ki o», sükûn üzere mebnî; «Beyt»in na'tı olarak mahallen mecrûr."),
  MADI("طَافَ", "tafa", ["hollow-verbs"], note_ar=FAIL_BAAD[0] + SILA_[0], note_en=FAIL_BAAD[1] + SILA_[1], note_tr=FAIL_BAAD[2] + SILA_[2]),
  T("حَوْلَهُ", "hawla", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
     "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«طَافَ»، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ الْعَائِدُ عَلَى «الَّذِي».",
     "An adverb of place, in nasb, hanging on «walked round»; annexed to the attached «it», in the seat of jarr — the pronoun that returns to «which».",
     "Mekân zarfı, mansûb, «tavaf etti»ye müteallik; bitişik zamire muzâf, zamir mahallen mecrûr — «ki o»ya dönen âid zamirdir.",
     segs=SG(("حَوْلَ", "hawla", "noun"), ("هُ", "pron-3ms", "pron")))],
 [FAIL("رِجَالٌ", "rajul", extra=["jam-taksir"], note_ar=" — فَاعِلُ «طَافَ»؛ جَمْعُ رَجُلٍ", note_en=" — the doer of «walked round»; the plural of «man»", note_tr=" — «tavaf etti»nin fâili; racül'ün cem'i"),
  T("بَنَوْهُ", "bana", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi", "jumla-sifa"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«رِجَالٌ».",
     "Past verb built on a fatha estimated on the alif, which dropped where two quiescents met; the waw is the doer, in the seat of raf', and the attached «it» the object, in the seat of nasb — the clause is a na't of «men», in the seat of raf'.",
     "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; vâv fâil, mahallen merfû; bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle «adamlar»ın na'tı, mahallen merfû.",
     segs=SG(("بَنَ", "bana", "verb"), ("وْ", "pron-3mp", "pron"), ("هُ", "pron-3ms", "pron"))),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ وَاوِ الْجَمَاعَةِ", "; the jarr phrase hangs on an omitted hal of the waw of «built»", " — câr-mecrûr «bina ettiler»deki vâvın mahzûf hâline müteallik")),
  MAJR("قُرَيْشٍ", "quraysh", "propn"),
  ATF("وَجُرْهُمِ", "jurhum", "propn", case="jarr", extra=["al-qafiya"], note_ar=" — قَبِيلَةٌ قَدِيمَةٌ وَلِيَتِ الْبَيْتَ قَبْلَ قُرَيْشٍ؛ صُرِفَ عَلَى إِرَادَةِ الْحَيِّ" + RAWI_J[0], note_en=" — an ancient tribe that held the House before Quraysh; declined in full as the name of a clan" + RAWI_J[1], note_tr=" — Kureyş'ten önce Beyt'i elinde tutan eski bir kabile; «hay» (oymak) kastedilerek munsarif okunmuştur" + RAWI_J[2])])
# ---- v. 17 ----
V(S3, "an oath: excellent lords indeed were you two found, in every case, the single-twisted and the firm-plied alike.",
  "bir yemin ki: gerçekten siz ikiniz her halde — tek kat bükülmüşünde de çift kat bükülmüşünde de (kolayda da zorda da) — ne güzel iki efendi bulundunuz.",
 [T("يَمِينًا", "yamin", "noun", ["maful-mutlaq"],
     "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ، عَامِلُهُ «أَقْسَمْتُ» مِنْ غَيْرِ لَفْظِهِ: أَيْ حَلَفْتُ حَلِفًا.",
     "A maf'ul mutlaq, in nasb; its governor is «I swore», a verb of another root: «I swore an oath».",
     "Mef'ûl-i mutlak, mansûb; âmili, lafzı başka olan «yemin ettim»dir: «bir yeminle yemin ettim»."),
  T("لَنِعْمَ", "nima-verb", "verb", ["afal-al-madh-wal-dhamm-fil-kafiya", "huruf-al-qasam-fil-kafiya", "khabar-insha"],
     "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَنِعْمَ فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ مَبْنِيٌّ عَلَى الْفَتْحِ.",
     "The lam opens the answer of the oath; نِعْمَ is the frozen past verb that performs praise, built on fatha.",
     "Lâm yeminin cevabını açar; «ni'me» medh inşâsı için câmid mâzî fiil, fetha üzere mebnî.",
     segs=SG(("لَ", "lam-qasam", "part"), ("نِعْمَ", "nima-verb", "verb"))),
  FAIL("السَّيِّدَانِ", "sayyid", extra=["al-muthanna"], sign="بِالْأَلِفِ لِأَنَّهُ مُثَنًّى", note_ar=" — وَهُمَا هَرِمُ بْنُ سِنَانٍ وَالْحَارِثُ بْنُ عَوْفٍ؛ وَجُمْلَةُ «نِعْمَ السَّيِّدَانِ» فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ مُقَدَّمٌ لِـ«وُجِدْتُمَا»", note_en=" — by the alif, a dual: the two lords are Harim ibn Sinān and al-Ḥārith ibn ʿAwf; the clause «excellent are the two lords» is the fronted second object of «you were found», in the seat of nasb", note_tr=" — tesniye olduğu için elif ile: iki efendi Herim b. Sinân ile Hâris b. Avf'tır; «ne güzel iki efendi» cümlesi «bulundunuz»un öne alınmış ikinci mef'ûlü, mahallen mansûb"),
  T("وُجِدْتُمَا", "wajada", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "mafulayn", "al-bariz-al-muttasil", "mithal-verbs"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ — وَهُوَ الْمَفْعُولُ الْأَوَّلُ — وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ؛ وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
     "A past verb in the passive, built on sukun because a pronoun of raf' is attached; the ta is its deputy doer, in the seat of raf' — the first object — and the mim and alif mark the dual; the clause is the answer of the oath and has no seat.",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî meçhul mâzî; tâ nâib-i fâildir, mahallen merfû — birinci mef'ûl odur — mîm ile elif tesniye alâmetidir; cümle yeminin cevabıdır, mahalli yoktur.")],
 [ALA(), MAJR("كُلِّ", "kull", **W(MUD, (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وُجِدْتُمَا»", "; the phrase hangs on «you were found»", "; câr-mecrûr «bulundunuz»a müteallik"))),
  MUDAF_ILAYH("حَالٍ", "hal-state"),
  MIN(role=(" — وَمِنْ بَيَانِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«حَالٍ»", "; مِنْ here explains, and the phrase hangs on an omitted na't of «case»", " — «min» beyâniyyedir; câr-mecrûr «hal»in mahzûf na'tına müteallik")),
  MAJR("سَحِيلٍ", "sahil-thread", extra=["istiara", "tibaq"], note_ar=" — وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: السَّحِيلُ الْخَيْطُ الْمَفْتُولُ عَلَى قُوَّةٍ وَاحِدَةٍ، اسْتُعِيرَ لِلْحَالِ الضَّعِيفَةِ، وَالْمُبْرَمُ الْمَفْتُولُ عَلَى قُوَّتَيْنِ اسْتُعِيرَ لِلْحَالِ الْقَوِيَّةِ (الزَّوْزَنِيُّ)؛ وَقِيلَ: هُمَا كِنَايَةٌ عَنْ سُهُولَةِ الْأَمْرِ وَصُعُوبَتِهِ (الدُّرَّةُ). وَبَيْنَ «سَحِيلٍ» وَ«مُبْرَمِ» طِبَاقٌ", note_en=" — here is an isti'ara tasrihiyya: the سَحِيل, a thread twisted of one strand, is lent to the weak case, and the مُبْرَم, twisted of two, to the strong one (al-Zawzanī); others call the pair a kinaya for a matter's ease and its hardship (al-Durra). «Single-twisted» and «firm-plied» also make a tibaq", note_tr=" — burada istiâre-i tasrîhiyye vardır: «sahîl» tek kat bükülmüş ip, zayıf hal için; «mübrem» çift kat bükülmüş ip, kuvvetli hal için ödünç alınmıştır (Zevzenî); bir görüşe göre ikisi, işin kolaylığından ve zorluğundan kinâyedir (Dürre). «Sahîl» ile «mübrem» arasında ayrıca tıbâk vardır"),
  ATF("وَمُبْرَمِ", "mubram", case="jarr", extra=["ism-maful", "tibaq", "al-qafiya"], **W(RAWI_J))])
# ---- v. 18 ----
V(S3, "You two retrieved ʿAbs and Dhubyān after they had worn each other out and had pounded between them the perfume of Manshim.",
  "Abs ile Zübyân'ı, birbirlerini tüketip aralarında Menşim'in ıtrını dövdükten (savaş hepsini kırıp geçirdikten) sonra siz ikiniz kurtardınız.",
 [T("تَدَارَكْتُمَا", "tadaraka", "verb", ["form-vi-verbs", "al-bariz-al-muttasil", "fail", "hadhf-al-mudaf-wal-mudaf-ilayh"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ وَالتَّدَارُكُ: التَّلَافِي.",
     "Past verb built on sukun because a pronoun of raf' is attached; the ta is the doer, in the seat of raf', and the mim and alif mark the dual — a new sentence; تَدَارُك is to reach a thing in time and mend it.",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; tâ fâildir, mahallen merfû; mîm ile elif tesniye alâmetidir — cümle müste'nefedir; «tedârük»: bir işe vaktinde yetişip onu düzeltmek."),
  MAFUL("عَبْسًا", "abs", "propn", ["hadhf-al-mudaf-wal-mudaf-ilayh"], note_ar=" — عَلَى حَذْفِ مُضَافٍ: تَدَارَكْتُمَا أَمْرَ عَبْسٍ وَذُبْيَانَ (الزَّوْزَنِيُّ)", note_en=" — with an annexed word left out: «you retrieved [the affair of] ʿAbs and Dhubyān» (al-Zawzanī)", note_tr=" — muzâf hazfedilmiştir: «Abs ile Zübyân'ın [işini] düzelttiniz» (Zevzenî)"),
  ATF("وَذُبْيَانَ", "dhubyan", "propn", case="nasb", extra=["mamnu-min-sarf"], sign="مَنْصُوبٌ بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=" — عَلَمٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَزِيَادَةِ الْأَلِفِ وَالنُّونِ", note_en=" — with no tanwin: a proper name ending in the added alif and nun, a diptote", note_tr=" — tenvinsiz: sonunda zâid elif-nûn bulunan özel isim, gayr-i munsarif"),
  T("بَعْدَمَا", "bada", "noun", ["maful-fih", "an-masdariyya", "idafa-definiteness"],
     "بَعْدَ ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«تَدَارَكْتُمَا»، مُضَافٌ، وَمَا مَصْدَرِيَّةٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهَا وَمِنَ الْفِعْلِ بَعْدَهَا فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ: بَعْدَ تَفَانِيهِمْ.",
     "بَعْدَ is an adverb of time, in nasb, hanging on «you retrieved», and annexed; مَا is the masdar-making particle — the masdar it builds with the verb after it fills the seat of jarr: «after their wearing each other out».",
     "«Ba'de» zaman zarfı, mansûb, «kurtardınız»a müteallik, muzâf; «mâ» masdariyyedir — sonraki fiille oluşturduğu müevvel masdar muzâfun ileyh olarak mahallen mecrûr: «birbirlerini tüketmelerinden sonra».",
     segs=SG(("بَعْدَ", "bada", "noun"), ("مَا", "ma-masdariyya", "part")))],
 [T("تَفَانَوْا", "tafana", "verb", ["form-vi-verbs", "naqis-verbs", "al-bariz-al-muttasil", "fail"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ «مَا» الْمَصْدَرِيَّةِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ وَالتَّفَانِي: التَّشَارُكُ فِي الْفَنَاءِ.",
     "Past verb built on a fatha estimated on the alif, which dropped where two quiescents met; the waw is the doer, in the seat of raf' — the clause is the ṣila of the masdar-making مَا and has no seat; تَفَانٍ is to share in perishing, each side destroying the other.",
     "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; vâv fâildir, mahallen merfû — cümle masdariyye «mâ»nın sılasıdır, mahalli yoktur; «tefânî»: yok oluşta ortak olmak, karşılıklı birbirini tüketmek.",
     segs=SG(("تَفَانَ", "tafana", "verb"), ("وْا", "pron-3mp", "pron"))),
  VERB_WAW("وَدَقُّوا", "daqqa", ["doubled-verbs", "majaz-murakkab"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «تَفَانَوْا». وَ«دَقُّوا بَيْنَهُمْ عِطْرَ مَنْشِمِ» مَثَلٌ سَائِرٌ، فَهُوَ اسْتِعَارَةٌ تَمْثِيلِيَّةٌ: شُبِّهَتْ حَالُهُمْ وَقَدْ أَتَى الْقِتَالُ عَلَى آخِرِهِمْ بِحَالِ قَوْمٍ تَعَطَّرُوا بِعِطْرِ مَنْشِمَ وَتَحَالَفُوا عَلَى الْقِتَالِ فَقُتِلُوا عَنْ آخِرِهِمْ (الزَّوْزَنِيُّ)", note_en=" — the clause is joined to «wore each other out». «They pounded between them the perfume of Manshim» is a current proverb, and so an isti'ara of tamthil: their state, when the fighting had made an end of them, is likened to that of the men who scented themselves with Manshim's perfume, swore to fight, and were killed to the last man (al-Zawzanī)", note_tr=" — cümle «birbirlerini tükettiler»e ma'tûf. «Aralarında Menşim'in ıtrını dövdüler» yaygın bir meseldir; dolayısıyla istiâre-i temsîliyyedir: savaşın sonuncularına kadar kırıp geçirdiği halleri, Menşim'in ıtrıyla kokulanıp savaşmak üzere ahitleşen ve son ferdine kadar öldürülen kavmin haline benzetilmiştir (Zevzenî)"),
  T("بَيْنَهُمْ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
     "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«دَقُّوا»، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "An adverb of place, in nasb, hanging on «pounded»; annexed to the attached «them», in the seat of jarr.",
     "Mekân zarfı, mansûb, «dövdüler»e müteallik; bitişik zamire muzâf, zamir mahallen mecrûr.",
     segs=SG(("بَيْنَ", "bayna", "noun"), ("هُمْ", "pron-3mp", "pron"))),
  MAFUL("عِطْرَ", "itr", **W(MUD)),
  MUDAF_ILAYH("مَنْشِمِ", "manshim", "propn", ["al-qafiya", "mamnu-min-sarf"], note_ar=" — قِيلَ: اسْمُ امْرَأَةٍ عَطَّارَةٍ، فَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ وَالْجَرُّ بِالْفَتْحَةِ، وَكُسِرَ هُنَا لِلْقَافِيَةِ ضَرُورَةً؛ وَقِيلَ: اسْمُ رَجُلٍ عَطَّارٍ فَلَا ضَرُورَةَ — وَضَبْطُ الشِّينِ بِالْكَسْرِ مِنَ الْمُحَرِّرِ", note_en=" — said to be a woman who sold perfume, so that by rule it is a diptote, in jarr by the fatha, and takes the kasra here only for the rhyme, a poet's licence; others say a man's name, and then there is no licence — the kasra on the shin is editorial", note_tr=" — bir görüşe göre ıtır satan bir kadının adıdır; o halde gayr-i munsarif olup fetha ile cer edilmesi gerekirken burada kâfiye için zarûreten kesrelenmiştir; bir görüşe göre erkek adıdır ve zarûret yoktur — şîn'in kesresi editoryaldir")])
# ---- v. 19 ----
V(S3, "And you two had said: If we reach peace made wide, by wealth and by fair words, we shall be safe.",
  "Siz ikiniz şöyle demiştiniz: Malla ve güzel sözle geniş bir barışa ulaşırsak selâmete ereriz.",
 [T("وَقَدْ", "qad", "part", ["qad-harf"], WA_AR + "قَدْ حَرْفُ تَحْقِيقٍ.", "The waw conjoins; قَدْ affirms the past verb after it.", "«ve» + kad: tahkîk harfi.", segs=SG(("وَ", "wa", "conj"), ("قَدْ", "qad", "part"))),
  T("قُلْتُمَا", "qala", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ، وَمَقُولُ الْقَوْلِ جُمْلَةُ الشَّرْطِ بَعْدَهُ.",
     "Past verb built on sukun because a pronoun of raf' is attached; the ta is the doer, in the seat of raf'; the mim and alif mark the dual; what is said is the conditional sentence after it.",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; tâ fâildir, mahallen merfû; mîm ile elif tesniye alâmetidir; mekûlü'l-kavl sonraki şart cümlesidir."),
  T("إِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza"], "حَرْفُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ: «نُدْرِكِ» وَ«نَسْلَمِ».", "The conditional إِنْ «if», which puts two verbs in jazm: «we reach» and «we shall be safe».", "Cezmeden şart harfi «in»: iki fiili — «ulaşırsak» ve «selâmete ereriz» — cezmeder."),
  JV("نُدْرِكِ", "adraka", "shart", "kasr2", g=["form-iv-verbs", "in-shartiyya"], doer=("، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ", "; the doer «we» must stay hidden", "; fâil vücûben gizli «biz»")),
  MAFUL("السِّلْمَ", "silm", extra=["mulhaq-bil-jinas", "radd-al-ajuz"], note_ar=" — وَهُوَ الصُّلْحُ، يُذَكَّرُ وَيُؤَنَّثُ، وَتُفْتَحُ سِينُهُ وَتُكْسَرُ (وَالْكَسْرُ هُنَا مِنَ الْمُحَرِّرِ). وَبَيْنَ «السِّلْمَ» وَ«نَسْلَمِ» اشْتِقَاقٌ مُلْحَقٌ بِالْجِنَاسِ، وَهُوَ مِنْ رَدِّ الْعَجُزِ عَلَى الصَّدْرِ: أَحَدُهُمَا فِي حَشْوِ الْمِصْرَاعِ الْأَوَّلِ وَالْآخَرُ فِي آخِرِ الْبَيْتِ", note_en=" — «peace», a word both masculine and feminine, said with kasra or fatha on the sin (the kasra here is editorial). السِّلْم and نَسْلَم share a root — the derivation that is attached to jinas — and make a radd al-'ajuz 'ala al-sadr: one stands inside the first hemistich, the other closes the verse", note_tr=" — «barış»; hem müzekker hem müennes kullanılır, sîn'i fethalı da kesreli de okunur (buradaki kesre editoryaldir). «Silm» ile «neslem» arasında cinâsa mülhak iştikâk vardır; bu aynı zamanda reddü'l-acüz ale's-sadrdır: biri ilk mısraın içinde, diğeri beytin sonundadır"),
  HAL("وَاسِعًا", "wasi-wide", extra=["ism-fail"], note_ar="، وَصَاحِبُهُ «السِّلْمَ»", note_en=" — its owner is «peace»", note_tr=" — sahibi «barış»tır")],
 [BI_NOUN("بِمَالٍ", "mal", "مَالٍ", note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نُدْرِكِ»", note_en=" — the ba of means; the phrase hangs on «we reach»", note_tr=" — bâ istiâne içindir; câr-mecrûr «ulaşırsak»a müteallik"),
  ATF("وَمَعْرُوفٍ", "maruf", case="jarr", extra=["ism-maful"]),
  MINA(), MAJR("الْقَوْلِ", "qawl", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَعْرُوفٍ»", note_en="; the phrase hangs on an omitted na't of «fair dealing»", note_tr="; câr-mecrûr «ma'rûf»un mahzûf na'tına müteallik"),
  JV("نَسْلَمِ", "salima-safe", "jawab", "rawi", g=["in-shartiyya", "mulhaq-bil-jinas", "radd-al-ajuz"], doer=("، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ", "; the doer «we» must stay hidden", "; fâil vücûben gizli «biz»"), note=(" — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", " — the conditional sentence is what was said, in the seat of nasb", " — şart cümlesi cevabıyla birlikte mekûlü'l-kavl, mahallen mansûb"))])
# ---- v. 20 ----
V(S3, "So you came to stand, in that peace, on the best of ground — far, in it, from any wronging of kin and from any sin.",
  "Böylece o barışta en hayırlı yerde durur oldunuz; orada akrabaya isyandan da günahtan da uzaksınız.",
 [T("فَأَصْبَحْتُمَا", "asbaha", "verb", ["kana-wa-akhawatuha", "form-iv-verbs", "al-bariz-al-muttasil"],
     FA_AR + "أَصْبَحَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ، وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ.",
     "The fa conjoins; أَصْبَحَ «came to be» is one of كَانَ's sisters, built on sukun because a pronoun of raf' is attached; the ta is its noun, in the seat of raf', and the mim and alif mark the dual.",
     "«fe» + asbaha «oldu»: kâne'nin kardeşlerinden nâkıs mâzî; ref' zamiri bitiştiği için sükûn üzere mebnî; tâ ismidir, mahallen merfû; mîm ile elif tesniye alâmetidir.",
     segs=SG(("فَ", "fa", "conj"), ("أَصْبَحْتُمَا", "asbaha", "verb"))),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)", note_ar=" — وَالضَّمِيرُ لِلسِّلْمِ وَهِيَ تُؤَنَّثُ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَصْبَحْتُمَا»", note_en="; «it» is the peace, here feminine; the phrase hangs on «you came to be»", note_tr="; zamir, burada müennes sayılan «barış»a döner; câr-mecrûr «oldunuz»a müteallik"),
  ALA(), MAJR("خَيْرِ", "khayr", extra=["ism-tafdil"], **W(MUD, (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «أَصْبَحَ»", "; the jarr phrase hangs on the omitted predicate of أَصْبَحَ", "; câr-mecrûr «asbaha»nın mahzûf haberine müteallik"))),
  MUDAF_ILAYH("مَوْطِنٍ", "mawtin")],
 [T("بَعِيدَيْنِ", "baid", "noun", ["kana-wa-akhawatuha", "al-muthanna", "sifa-mushabbaha"],
     "خَبَرٌ ثَانٍ لِـ«أَصْبَحَ» مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَقِيلَ: حَالٌ مِنِ اسْمِهَا (الدُّرَّةُ).",
     "A second predicate of أَصْبَحَ, in nasb by the ya, being a dual; some read it as a hal of its noun (al-Durra).",
     "«Asbaha»nın ikinci haberi; tesniye olduğu için yâ ile mansûb; bir görüşe göre isminden hâldir (Dürre)."),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بَعِيدَيْنِ»", note_en="; the phrase hangs on «far»", note_tr="; câr-mecrûr «uzak»a müteallik"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«بَعِيدَيْنِ»", "; the phrase hangs on «far»", " — câr-mecrûr «uzak»a müteallik")),
  MAJR("عُقُوقٍ", "uquq", extra=["masdar"], note_ar=" — وَهُوَ الْعِصْيَانُ وَقَطِيعَةُ الرَّحِمِ", note_en=" — defiance of one's kin, the cutting of the tie of the womb", note_tr=" — isyan, akrabalık bağını koparmak"),
  ATF("وَمَأْثَمِ", "matham", case="jarr", extra=["masdar", "al-qafiya"], note_ar=" — مَصْدَرٌ مِيمِيٌّ بِمَعْنَى الْإِثْمِ" + RAWI_J[0], note_en=" — a mimi masdar meaning «sin»" + RAWI_J[1], note_tr=" — «günah» anlamında mîmî masdar" + RAWI_J[2])])
# ---- v. 21 ----
V(S3, "— great, on the heights of Maʿadd; may you both be guided! And whoever finds a treasure of glory free for the taking grows great.",
  "— Maadd'in en yüce mertebesinde iki büyük olarak; hidayet üzere olun! Kim şereften, helâl bulduğu bir hazineyi ele geçirirse büyür.",
 [T("عَظِيمَيْنِ", "azim", "noun", ["kana-wa-akhawatuha", "hal", "al-muthanna", "sifa-mushabbaha", "radd-al-ajuz", "mulhaq-bil-jinas"],
     "خَبَرٌ ثَالِثٌ لِـ«أَصْبَحَ» فِي الْبَيْتِ قَبْلَهُ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى (الدُّرَّةُ)، وَقِيلَ: حَالٌ — وَعَلَيْهِ الزَّوْزَنِيُّ: ظَفِرْتُمَا بِالصُّلْحِ فِي حَالِ عَظَمَتِكُمَا. وَبَيْنَ «عَظِيمَيْنِ» وَ«يَعْظُمِ» اشْتِقَاقٌ، وَهُوَ مِنْ رَدِّ الْعَجُزِ عَلَى الصَّدْرِ: أَحَدُهُمَا فِي صَدْرِ الْبَيْتِ وَالْآخَرُ فِي آخِرِهِ.",
     "A third predicate of أَصْبَحَ in the verse before, in nasb by the ya, being a dual (al-Durra); others read it as a hal — so al-Zawzanī: «you won the peace while great». عَظِيمَيْنِ and يَعْظُمِ share a root, and make a radd al-'ajuz 'ala al-sadr: one opens the verse and the other closes it.",
     "Önceki beyitteki «asbaha»nın üçüncü haberi; tesniye olduğu için yâ ile mansûb (Dürre); bir görüşe göre hâldir — Zevzenî böyle okur: «büyüklüğünüz halinde barışı elde ettiniz». «Azîmeyn» ile «ya'zum» arasında iştikâk vardır; bu aynı zamanda reddü'l-acüz ale's-sadrdır: biri beytin başında, diğeri sonundadır."),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَظِيمَيْنِ»", "; the phrase hangs on «great»", " — câr-mecrûr «büyük»e müteallik")),
  MAJR("عُلْيَا", "ulya", extra=["ism-maqsur-manqus", "ism-tafdil", "idafa-definiteness"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar="، مُضَافٌ — تَأْنِيثُ الْأَعْلَى: أَيِ الرُّتْبَةِ الْعُلْيَا مِنْ شَرَفِ مَعَدٍّ", note_en=" — by a kasra estimated on the alif; annexed — the feminine of «highest»: the highest rank of Maʿadd's honour", note_tr=" — elif üzerinde takdîrî kesre ile; muzâf — «a'lâ»nın müennesi: Maadd şerefinin en yüksek mertebesi"),
  MUDAF_ILAYH("مَعَدٍّ", "maadd-name", "propn", note_ar=" — مَعَدُّ بْنُ عَدْنَانَ أَبُو الْعَرَبِ الْعَدْنَانِيَّةِ", note_en=" — Maʿadd son of ʿAdnān, forefather of the northern Arabs", note_tr=" — Adnânî Arapların atası Maadd b. Adnân"),
  T("هُدِيتُمَا", "hada", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "naqis-verbs", "al-bariz-al-muttasil", "khabar-fi-mana-al-insha", "itirad", "jumla-mutarida"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ، وَالْمِيمُ وَالْأَلِفُ عَلَامَةُ التَّثْنِيَةِ — وَالْجُمْلَةُ مُعْتَرِضَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ. وَهِيَ خَبَرٌ لَفْظًا إِنْشَاءٌ مَعْنًى: دُعَاءٌ لَهُمَا (الزَّوْزَنِيُّ)؛ وَالِاعْتِرَاضُ بِالدُّعَاءِ مِنَ الْإِطْنَابِ.",
     "A past verb in the passive, built on sukun because a pronoun of raf' is attached; the ta is its deputy doer, in the seat of raf', and the mim and alif mark the dual — a parenthetical clause with no seat. It is a report in form and a request in meaning: a prayer for the two (al-Zawzanī); the parenthesis that prays is one of the kinds of itnab.",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî meçhul mâzî; tâ nâib-i fâildir, mahallen merfû; mîm ile elif tesniye alâmetidir — cümle mu'tarızadır, mahalli yoktur. Lafzen haber, mânen inşâdır: ikisi için duadır (Zevzenî); dua ile yapılan i'tirâz ıtnâb çeşitlerindendir.")],
 [MAN("وَمَنْ", D("يَسْتَبِحْ", "sukun"), D("يَعْظُمِ", "rawi"), lead=WA_ISTINAF,
      tail=(" — وَفِي خَبَرِهِ خِلَافٌ: قِيلَ جُمْلَةُ الشَّرْطِ، وَقِيلَ جُمْلَةُ الْجَوَابِ، وَقِيلَ هُمَا مَعًا", " — on its khabar there are three views: the condition's clause, the answer's, or both together", " — haberi konusunda üç görüş vardır: şart cümlesi, cevap cümlesi yahut ikisi birden")),
  JV("يَسْتَبِحْ", "istabaha", "shart", "sukun", g=["form-x-verbs", "hollow-verbs"], note=(" — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (يَسْتَبِيحُ ← يَسْتَبِحْ)؛ وَالِاسْتِبَاحَةُ: وُجُودُ الشَّيْءِ مُبَاحًا، وَالِاسْتِئْصَالُ", " — a hollow verb whose middle letter drops where two quiescents meet (يَسْتَبِيحُ → يَسْتَبِحْ); اِسْتِبَاحَة is to find a thing free to take, and to take it all", " — ecvef fiil; iki sâkin karşılaştığı için aynü'l-fiili düşmüştür (yestebîhu → yestebih); «istibâha»: bir şeyi mubah bulmak ve kökünden almak")),
  MAFUL("كَنْزًا", "kanz"),
  MINA(), MAJR("الْمَجْدِ", "majd", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«كَنْزًا»", note_en="; the phrase hangs on an omitted na't of «a treasure»", note_tr="; câr-mecrûr «hazine»nin mahzûf na'tına müteallik"),
  JV("يَعْظُمِ", "azuma", "jawab", "rawi", g=["radd-al-ajuz", "mulhaq-bil-jinas"], note=(" — وَيُرْوَى «يُعْظَمِ» مِنَ الْإِعْظَامِ بِمَعْنَى التَّعْظِيمِ (الزَّوْزَنِيُّ)", " — also read يُعْظَمِ «is held great», from إِعْظَام (al-Zawzanī)", " — «yu'zam» («büyük sayılır») diye de rivayet edilir (Zevzenî)"))])
CH[3] = S3

# =====================================================================================================================
# Chapter 4 — الْحَرْبُ (al-Zawzanī vv. 28–32)
# =====================================================================================================================
S4 = []
ATF_JAWAB = (" — مَعْطُوفٌ عَلَى جَوَابِ الشَّرْطِ فِي الْبَيْتِ قَبْلَهُ", " — joined to the answer of the condition in the verse before", " — önceki beyitteki şart cevabına ma'tûf")
# ---- v. 28 ----
V(S4, "War is nothing but what you have known and tasted; and what I say of it is no tale of guesswork.",
  "Savaş, sizin bilip tattığınızdan başka bir şey değildir; bu (söylediğim) onun hakkında zanla söylenmiş bir söz de değildir.",
 [T("وَمَا", "ma-nafiya", "part", ["qasr", "turuq-al-qasr", "anwa-al-waw"],
     WA_ISTINAF[0] + "مَا نَافِيَةٌ مُهْمَلَةٌ لِانْتِقَاضِ نَفْيِهَا بِـ«إِلَّا». وَفِيهِ قَصْرٌ بِالنَّفْيِ وَالِاسْتِثْنَاءِ: قُصِرَتِ الْحَرْبُ عَلَى مَا عَلِمُوهُ وَذَاقُوهُ.",
     WA_ISTINAF[1] + "مَا negates and governs nothing here, its negation being undone by إِلَّا. Here is a qasr by negation and exception: war is confined to what they have known and tasted.",
     WA_ISTINAF[2] + "«mâ» nâfiyedir; nefyi «illâ» ile bozulduğu için amel etmez. Burada nefy ve istisnâ ile kasr vardır: savaş, onların bilip tattıkları şeye hasredilmiştir.",
     segs=SG(("وَ", "wa", "conj"), ("مَا", "ma-nafiya", "part"))),
  MUBTADA("الْحَرْبُ", "harb", note_ar=" — وَهِيَ مُؤَنَّثَةٌ", note_en=" — a feminine noun", note_tr=" — müennes bir isimdir"),
  T("إِلَّا", "illa", "part", ["istithna-mufarragh", "qasr"], "أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ.", "The particle of restriction, governing nothing — the exception is emptied.", "Hasr edatı, ameli yoktur — istisnâ müferrağdır."),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "mubtada-khabar"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.",
     "A relative noun «what», built on sukun, in the seat of raf' as the khabar.",
     "İsm-i mevsûl «…-diğiniz şey», sükûn üzere mebnî; haber olarak mahallen merfû."),
  T("عَلِمْتُمْ", "alima", "verb", ["al-bariz-al-muttasil", "fail", "ism-mawsul", "hadhf-al-maful"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: عَلِمْتُمُوهُ" + SILA_[0] + ".",
     "Past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer, in the seat of raf'; the pronoun returning to مَا is left out («what you have known [it]»)" + SILA_[1] + ".",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir, mahallen merfû; «mâ»ya dönen âid zamir hazfedilmiştir" + SILA_[2] + "."),
  T("وَذُقْتُمُ", "dhaqa", "verb", ["atf-nasaq", "hollow-verbs", "al-bariz-al-muttasil", "fail", "istiara", "istiara-tabaiyya"],
     WA_AR + "ذُقْتُمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَضُمَّتِ الْمِيمُ وَأُشْبِعَتْ لِإِقَامَةِ الْوَزْنِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الصِّلَةِ. وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شُبِّهَتْ تَجْرِبَةُ شَدَائِدِ الْحَرْبِ بِالذَّوْقِ، ثُمَّ اشْتُقَّ مِنْهُ «ذُقْتُمْ» بِمَعْنَى جَرَّبْتُمْ (الزَّوْزَنِيُّ: الذَّوْقُ التَّجْرِبَةُ).",
     "The waw conjoins; ذُقْتُمْ is a past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer; the mim takes a lengthened damma to keep the metre — the clause is joined to the ṣila. Here is an isti'ara tasrihiyya taba'iyya: undergoing the hardships of war is likened to tasting, and from that «you tasted» is drawn for «you tried» (al-Zawzanī: «tasting is trying»).",
     "«ve» + «tattınız»: ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir; vezin için mîm dammelenip uzatılmıştır — cümle sılaya ma'tûf. Burada istiâre-i tasrîhiyye-i tebeiyye vardır: savaşın şiddetlerini yaşamak tatmaya benzetilmiş, sonra ondan «tattınız» fiili «denediniz» anlamında türetilmiştir (Zevzenî: «zevk tecrübedir»).",
     segs=SG(("وَ", "wa", "conj"), ("ذُقْتُمُ", "dhaqa", "verb")))],
 [T("وَمَا", "ma-hijaziyya", "part", ["ma-la-mushabbaha", "atf-nasaq"],
     WA_AR + "مَا نَافِيَةٌ حِجَازِيَّةٌ تَعْمَلُ عَمَلَ لَيْسَ: تَرْفَعُ الِاسْمَ وَتَنْصِبُ الْخَبَرَ.",
     "The waw conjoins; this مَا negates in the Ḥijāzī way and works like لَيْسَ: it raises its noun and puts its predicate in nasb.",
     "«ve» + Hicâzî «mâ»: nefy bildirir ve «leyse» gibi amel eder; ismini ref, haberini nasb eder.",
     segs=SG(("وَ", "wa", "conj"), ("مَا", "ma-hijaziyya", "part"))),
  T("هُوَ", "huwa", "pron", ["ma-la-mushabbaha", "al-mabni-wal-mudmar"],
     "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ اسْمُ «مَا» — يَعُودُ عَلَى الْعِلْمِ الْمَفْهُومِ مِنْ «عَلِمْتُمْ» (الدُّرَّةُ)، وَعِنْدَ الزَّوْزَنِيِّ: مَا هٰذَا الَّذِي أَقُولُ.",
     "A detached pronoun built on fatha, in the seat of raf' as the noun of مَا — it returns to the «knowing» understood from «you have known» (al-Durra); for al-Zawzanī: «this that I am saying».",
     "Fetha üzere mebnî munfasıl zamir; «mâ»nın ismi olarak mahallen merfû — «bildiniz»den anlaşılan «bilgi»ye döner (Dürre); Zevzenî'ye göre: «şu söylediğim şey»."),
  JARR_PRON("عَنْهَا", "an", "عَنْ", "هَا", " («onun hakkında»)", note_ar=" — وَالضَّمِيرُ لِلْحَرْبِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«هُوَ» لِأَنَّهُ بِمَعْنَى الْعِلْمِ (الدُّرَّةُ)، وَعَلَى تَفْسِيرِ الزَّوْزَنِيِّ بِـ«الْحَدِيثِ»: بِحَدِيثٍ مُرَجَّمٍ عَنِ الْحَرْبِ", note_en="; «it» is the war; the phrase hangs on هُوَ, which stands for «the knowing» (al-Durra) — or, as al-Zawzanī paraphrases, on «tale»: «a guessed tale about war»", note_tr="; zamir harbe döner; câr-mecrûr, «bilgi» anlamındaki «hüve»ye (Dürre), Zevzenî'nin açıklamasına göre ise «söz»e müteallik: «harp hakkında zanla söylenmiş söz»"),
  T("بِالْحَدِيثِ", "bi", "prep", ["huruf-al-ziyada-fil-kafiya", "ma-la-mushabbaha", "huruf-jarr"],
     "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَالْحَدِيثِ خَبَرُ «مَا» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا.",
     "The ba is an added jarr letter that strengthens the negation; «the tale» is the predicate of مَا — in jarr in wording, in nasb in its seat.",
     "Bâ, nefyi te'kîd eden zâid cer harfi; «söz», «mâ»nın haberi — lafzen mecrûr, mahallen mansûb.",
     segs=SG(("بِ", "bi", "prep"), ("الْحَدِيثِ", "hadith", "noun"))),
  T("الْمُرَجَّمِ", "murajjam", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
     "نَعْتٌ لِـ«الْحَدِيثِ» مَجْرُورٌ عَلَى اللَّفْظِ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ مِنْ رَجَّمَ: الَّذِي يُرْجَمُ فِيهِ بِالظُّنُونِ" + RAWI_AL[0] + ".",
     "A na't of «the tale», in jarr after its wording — the passive participle of رَجَّمَ: a tale in which one pelts with guesses" + RAWI_AL[1] + ".",
     "«Söz»ün na'tı; lafza uyarak mecrûr — «reccem»den ism-i mef'ûl: hakkında zanla taş atılan, tahminle söylenen" + RAWI_AL[2] + ".")])
# ---- v. 29 ----
V(S4, "Whenever you rouse it you rouse it to your blame; it grows fierce when you whet it, and then it blazes.",
  "Onu ne zaman uyandırırsanız, kınanmış olarak uyandırırsınız; onu kışkırttığınızda kızışır ve alev alır.",
 [T("مَتَى", "mata", "part", G_SHART + ["maful-fih"],
     "اسْمُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ مُتَعَلِّقٌ بِفِعْلِ الشَّرْطِ — فِعْلُ الشَّرْطِ «تَبْعَثُوهَا» الْأَوَّلُ وَجَوَابُهُ «تَبْعَثُوهَا» الثَّانِي، وَكِلَاهُمَا مَجْزُومٌ بِحَذْفِ النُّونِ.",
     "A conditional noun that puts two verbs in jazm, built on sukun in the seat of nasb as an adverb of time hanging on the condition's verb — the condition is the first «you rouse it» and the answer the second, each in jazm by the dropping of its nun.",
     "İki fiili cezmeden şart ismi; sükûn üzere mebnî, zaman zarfı olarak mahallen mansûb, şart fiiline müteallik — şart fiili birinci «uyandırırsanız», cevabı ikinci «uyandırırsınız»; ikisi de nûnun hazfiyle meczûm."),
  T("تَبْعَثُوهَا", "baatha", "verb", G_SHART + ["afal-khamsa", "al-bariz-al-muttasil", "fail", "maful-bihi", "istiara-makniyya"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ لِأَنَّهُ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ " + SGN["nun"][0] + "، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى الْحَرْبِ.",
     "Present verb in jazm as the condition's verb, its sign " + SGN["nun"][1] + "; the waw is the doer, in the seat of raf', and the attached «it» (the war) the object, in the seat of nasb.",
     "Şart fiili olarak meczûm muzâri, alâmeti " + SGN["nun"][2] + "; vâv fâil, mahallen merfû; bitişik «onu» (harbi) mef'ûlün bih, mahallen mansûb.",
     segs=SG(("تَبْعَثُو", "baatha", "verb"), ("هَا", "pron-3fs", "pron"))),
  T("تَبْعَثُوهَا", "baatha", "verb", G_SHART + ["afal-khamsa", "al-bariz-al-muttasil", "fail", "maful-bihi"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ لِأَنَّهُ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ " + SGN["nun"][0] + "، وَالْوَاوُ فَاعِلٌ وَهَا مَفْعُولٌ بِهِ. وَاتَّحَدَ لَفْظُ الشَّرْطِ وَالْجَوَابِ، وَالْفَائِدَةُ فِي الْحَالِ بَعْدَهُ: «ذَمِيمَةً».",
     "Present verb in jazm as the answer of the condition, its sign " + SGN["nun"][1] + "; the waw is the doer and هَا the object. Condition and answer are one and the same word; what the answer adds lies in the hal after it: «blamed».",
     "Şartın cevabı olarak meczûm muzâri, alâmeti " + SGN["nun"][2] + "; vâv fâil, «hâ» mef'ûlün bih. Şart ile cevabın lafzı aynıdır; cevabın getirdiği fayda sonraki hâldedir: «kınanmış olarak».",
     segs=SG(("تَبْعَثُو", "baatha", "verb"), ("هَا", "pron-3fs", "pron"))),
  HAL("ذَمِيمَةً", "dhamim", extra=["sifa-mushabbaha"], note_ar="، وَصَاحِبُهُ «هَا» ضَمِيرُ الْحَرْبِ — فَعِيلٌ بِمَعْنَى مَفْعُولٍ: مَذْمُومَةً، أَيْ تُذَمُّونَ عَلَى إِثَارَتِهَا", note_en=" — its owner is the «it» of the war; a فَعِيل in the sense of the passive participle: «blamed», that is, you are blamed for stirring it", note_tr=" — sahibi harbe dönen «hâ»dır; mef'ûl anlamında faîl: «kınanmış», yani onu kışkırttığınız için kınanırsınız")],
 [JV("وَتَضْرَ", "dariya", "atf-jawab", "alif", g=["naqis-verbs", "atf-nasaq", "jinas", "jinas-naqis", "mulhaq-bil-jinas", "radd-al-ajuz"], doer=HIYA_HARB, pre=WA3,
     note=(" — وَأَصْلُهُ تَضْرَى. وَبَيْنَهُ وَبَيْنَ «ضَرَّيْتُمُوهَا» اشْتِقَاقٌ، وَبَيْنَ «تَضْرَ» وَ«تَضْرَمِ» جِنَاسٌ نَاقِصٌ بِزِيَادَةِ حَرْفٍ فِي الْآخِرِ، عَلَى حَدِّ شَاهِدِ التَّلْخِيصِ «عَوَاصٍ عَوَاصِمِ»؛ وَهُوَ مِنْ رَدِّ الْعَجُزِ عَلَى الصَّدْرِ: أَحَدُهُمَا فِي صَدْرِ الْمِصْرَاعِ الثَّانِي وَالْآخَرُ فِي آخِرِ الْبَيْتِ",
           " — it is تَضْرَى. It shares a root with ضَرَّيْتُمُوهَا; and تَضْرَ with تَضْرَمِ makes a jinas naqis, one letter more at the end, like the Talkhīṣ's own example عَوَاصٍ عَوَاصِمِ; it is also a radd al-'ajuz 'ala al-sadr: one opens the second hemistich and the other closes the verse",
           " — aslı «tadrâ»dır. «Darreytümûhâ» ile arasında iştikâk vardır; «tadra» ile «tadram» arasında ise sonda bir harf fazlalığıyla cinâs-ı nâkıs bulunur — Telhîs'in «avâsın avâsımü» şâhidi gibi; bu aynı zamanda reddü'l-acüz ale's-sadrdır: biri ikinci mısraın başında, diğeri beytin sonundadır"),
     segs=SG(("وَ", "wa", "conj"), ("تَضْرَ", "dariya", "verb"))),
  T("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"],
     "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«تَضْرَ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
     "An adverb for time to come, built on sukun in the seat of nasb, hanging on «it grows fierce» and annexed to the clause after it.",
     "Gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb, «kızışır»a müteallik; sonraki cümleye muzâf."),
  T("ضَرَّيْتُمُوهَا", "darra-whet", "verb", ["form-ii-verbs", "naqis-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi", "mulhaq-bil-jinas"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْوَاوُ لِإِشْبَاعِ ضَمَّةِ الْمِيمِ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ؛ وَالتَّضْرِيَةُ: الْحَمْلُ عَلَى الضَّرَاوَةِ.",
     "Past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer; the waw only lengthens the mim's damma; the attached «it» is the object, in the seat of nasb — the clause fills the seat of jarr after إِذَا; تَضْرِيَة is to set a thing on to fierceness.",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir; vâv mîmin dammesini işbâ' içindir; bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle «izâ»ya muzâfun ileyh olarak mahallen mecrûr; «tadriye»: bir şeyi azgınlığa sevk etmek.",
     segs=SG(("ضَرَّيْتُمُو", "darra-whet", "verb"), ("هَا", "pron-3fs", "pron"))),
  JV("فَتَضْرَمِ", "darima", "atf-jawab", "rawi", g=["atf-nasaq", "istiara-makniyya", "jinas-naqis", "radd-al-ajuz"], doer=HIYA_HARB, pre=FA3,
     note=(" — مَعْطُوفٌ عَلَى «تَضْرَ». وَفِيهِ اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَتِ الْحَرْبُ بِالنَّارِ ثُمَّ حُذِفَ الْمُشَبَّهُ بِهِ وَرُمِزَ إِلَيْهِ بِلَازِمِهِ وَهُوَ الِاضْطِرَامُ (الزَّوْزَنِيُّ: إِذَا أَوْقَدْتُمْ نَارَ الْحَرْبِ … فَتَلْتَهِبُ نِيرَانُهَا)",
           " — joined to «it grows fierce». Here is an isti'ara makniyya: war is likened to fire, the fire is left unnamed, and it is pointed to by what belongs to fire — blazing (al-Zawzanī: «when you kindle the fire of war … its flames blaze»)",
           " — «kızışır»a ma'tûf. Burada istiâre-i mekniyye vardır: harp ateşe benzetilmiş, müşebbehün bih hazfedilmiş ve ona lâzımıyla — alevlenmekle — işaret edilmiştir (Zevzenî: «harp ateşini tutuşturduğunuzda … alevleri yükselir»)"),
     segs=SG(("فَ", "fa", "conj"), ("تَضْرَمِ", "darima", "verb")))])
# ---- v. 30 ----
V(S4, "Then it grinds you as the millstone grinds, with its mat beneath it; it conceives twice in the year, then gives birth, and bears twins.",
  "Sonra sizi, altındaki örtüsüyle birlikte değirmen taşının öğütmesi gibi öğütür; yılda iki kez gebe kalır, sonra doğurur, hem de ikiz doğurur.",
 [T("فَتَعْرُكُكُمْ", "araka", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "al-atf-bil-huruf-wa-ahkamuh"],
     "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَتَعْرُكُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ عَلَى الِاسْتِئْنَافِ — أَيْ: فَهِيَ تَعْرُكُكُمْ — وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْحَرْبِ، وَكُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ. هٰكَذَا ضُبِطَ فِي مَطْبُوعِ الزَّوْزَنِيِّ بِضَمِّ الْكَافِ الْأُولَى؛ وَيُرْوَى بِالْجَزْمِ «فَتَعْرُكْكُمُ» عَطْفًا عَلَى جَوَابِ الشَّرْطِ، وَعَلَيْهِ أَعْرَبَهُ الدُّرَّةُ.",
     "The fa opens a new clause; تَعْرُكُ is a present verb in raf', by a fresh start — «and so it grinds you» — the doer is the hidden «she» (the war), and the attached كُمْ «you» is the object, in the seat of nasb. So the Zawzanī edition vowels it, with damma on the first kaf; it is also read in jazm, فَتَعْرُكْكُمُ, joined to the answer of the condition, and that is how al-Durra parses it.",
     "Fâ isti'nâf içindir; «ta'rukü» isti'nâf üzere merfû muzâri — yani «o da sizi öğütür» — fâil harbe dönen gizli zamir «o»; bitişik «küm» mef'ûlün bih, mahallen mansûb. Zevzenî baskısında ilk kâf'ın dammesiyle böyle harekelenmiştir; şartın cevabına atıfla cezimli «fe-ta'rukkümü» diye de rivayet edilir, Dürre de böyle i'râb etmiştir.",
     segs=SG(("فَ", "fa", "conj"), ("تَعْرُكُ", "araka", "verb"), ("كُمْ", "pron-2mp", "pron"))),
  T("عَرْكَ", "ark", "noun", ["maful-mutlaq", "idafa-definiteness", "tashbih", "aqsam-al-tashbih", "imal-al-masdar"],
     "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ إِلَى فَاعِلِهِ، وَمَفْعُولُهُ مَحْذُوفٌ أَيِ الْحَبَّ. وَفِيهِ تَشْبِيهٌ بَلِيغٌ — مُؤَكَّدٌ مُجْمَلٌ — جَاءَ فِي صُورَةِ الْمَفْعُولِ الْمُطْلَقِ: الْمُشَبَّهُ عَرْكُ الْحَرْبِ إِيَّاهُمْ أَيْ إِفْنَاؤُهَا لَهُمْ، وَالْمُشَبَّهُ بِهِ عَرْكُ الرَّحَى الْحَبَّ، وَحُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ (الزَّوْزَنِيُّ: جَعَلَ إِفْنَاءَ الْحَرْبِ إِيَّاهُمْ بِمَنْزِلَةِ طَحْنِ الرَّحَى الْحَبَّ).",
     "A maf'ul mutlaq that states the kind, in nasb, annexed to its doer; its object — the grain — is left out. Here is a tashbih baligh — mu'akkad and mujmal — in the dress of a maf'ul mutlaq: the thing likened is war's grinding of them, its wearing them to nothing; the thing it is likened to, the millstone's grinding of grain; tool and point of likeness are both dropped (al-Zawzanī: «he made war's destroying them stand as the millstone's milling the grain»).",
     "Nev'i bildiren mef'ûl-i mutlak, mansûb; fâiline muzâf, mef'ûlü — tane — mahzûf. Burada mef'ûl-i mutlak suretinde gelmiş bir teşbîh-i belîğ — müekked mücmel — vardır: müşebbeh harbin onları ezmesi, yani yok etmesi; müşebbehün bih değirmen taşının taneyi ezmesi; edat ve vech-i şebeh hazfedilmiştir (Zevzenî: «harbin onları yok edişini değirmen taşının taneyi öğütmesi yerine koymuştur»)."),
  MUDAF_ILAYH("الرَّحَى", "raha", extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_en=" — by a kasra estimated on the alif", note_tr=" — elif üzerinde takdîrî kesre ile"),
  T("بِثِفَالِهَا", "bi", "prep", ["huruf-jarr", "idafa-definiteness", "al-bariz-al-muttasil"],
     "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «مَعَ»، وَثِفَالِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «الرَّحَى»: أَيْ طَاحِنَةً وَمَعَهَا ثِفَالُهَا، وَلَا يُبْسَطُ الثِّفَالُ إِلَّا عِنْدَ الطَّحْنِ (الزَّوْزَنِيُّ)؛ وَعَلَّقَهُمَا الدُّرَّةُ بِالْمَصْدَرِ «عَرْكَ».",
     "The ba is a jarr letter meaning «with»; «mat» is in jarr and annexed to the attached «its», in the seat of jarr — the jarr phrase hangs on an omitted hal of «the millstone»: grinding, with its mat under it — and the mat is spread only when it grinds (al-Zawzanī); al-Durra hangs the phrase on the masdar «grinding».",
     "Bâ «ile» anlamında cer harfi; «sifâl» mecrûr, bitişik zamire muzâf, zamir mahallen mecrûr — câr-mecrûr «değirmen taşı»nın mahzûf hâline müteallik: altında örtüsü olduğu halde öğüten — örtü ancak öğütme sırasında serilir (Zevzenî); Dürre câr-mecrûru «ark» masdarına bağlar.",
     segs=SG(("بِ", "bi", "prep"), ("ثِفَالِ", "thifal", "noun"), ("هَا", "pron-3fs", "pron")))],
 [JV("وَتَلْقَحْ", "laqiha", "atf-jawab", "sukun", g=["atf-nasaq", "istiara-makniyya", "tarshih-wa-tajrid"], doer=HIYA_HARB, pre=WA3,
     note=(" — مَعْطُوفٌ عَلَى جَوَابِ «مَتَى». وَفِيهِ اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَتِ الْحَرْبُ بِالنَّاقَةِ ثُمَّ حُذِفَ الْمُشَبَّهُ بِهِ وَرُمِزَ إِلَيْهِ بِلَوَازِمِهِ: اللِّقَاحِ وَالنَّتَاجِ وَالْإِتْآمِ، ثُمَّ الْإِرْضَاعِ وَالْفِطَامِ فِي الْبَيْتِ بَعْدَهُ تَرْشِيحًا (الزَّوْزَنِيُّ: جَعَلَ صُنُوفَ الشَّرِّ تَتَوَلَّدُ مِنْ تِلْكَ الْحُرُوبِ بِمَنْزِلَةِ الْأَوْلَادِ النَّاشِئَةِ مِنَ الْأُمَّهَاتِ)",
           " — joined to the answer of مَتَى. Here is an isti'ara makniyya: war is likened to a she-camel; the camel is left unnamed and pointed to by what belongs to her — conceiving, bringing forth, bearing twins — and then, in the next verse, suckling and weaning, which carry the figure further (al-Zawzanī: «he made the kinds of evil born of those wars stand as children sprung from their mothers»)",
           " — «metâ»nın cevabına ma'tûf. Burada istiâre-i mekniyye vardır: harp dişi deveye benzetilmiş, müşebbehün bih hazfedilmiş ve ona lâzımlarıyla — gebe kalmak, doğurmak, ikiz doğurmak — işaret edilmiş; sonraki beyitteki emzirme ve sütten kesme de terşîhtir (Zevzenî: «o harplerden doğan türlü şerleri, analardan yetişen evlâtlar yerine koymuştur»)"),
     segs=SG(("وَ", "wa", "conj"), ("تَلْقَحْ", "laqiha", "verb"))),
  T("كِشَافًا", "kishaf", "noun", ["maful-mutlaq", "hal"],
     "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ عِنْدَ الْكُوفِيِّينَ، وَعِنْدَ الْبَصْرِيِّينَ مَصْدَرٌ فِي مَوْضِعِ الْحَالِ (الدُّرَّةُ) — وَالْكِشَافُ: أَنْ تَلْقَحَ فِي السَّنَةِ مَرَّتَيْنِ.",
     "A maf'ul mutlaq, in nasb, for the Kufans; for the Basrans a masdar standing in the place of a hal (al-Durra) — كِشَاف is to conceive twice in one year.",
     "Kûfelilere göre mef'ûl-i mutlak, mansûb; Basralılara göre hâl yerinde masdar (Dürre) — «kişâf»: yılda iki kez gebe kalmak."),
  THUMMA(),
  JV("تُنْتَجْ", "nataja", "atf-jawab", "sukun", g=["naib-al-fail", "al-majhul-fil-kafiya", "tarshih-wa-tajrid"], passive=True, doer=("، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْحَرْبِ", "; its deputy doer is the hidden «she» — the war", "; nâib-i fâil harbe dönen gizli zamir «o»"),
     note=(" — يُقَالُ: نُتِجَتِ النَّاقَةُ تُنْتَجُ أَيْ وَلَدَتْ", " — one says نُتِجَتِ النَّاقَةُ تُنْتَجُ, «the she-camel has given birth»", " — «nüticeti'n-nâkatü tüntecü» denir: «dişi deve doğurdu»")),
  JV("فَتُتْئِمِ", "atama-twin", "atf-jawab", "rawi", g=["atf-nasaq", "form-iv-verbs", "tarshih-wa-tajrid"], doer=HIYA_HARB, pre=FA3,
     note=(" — وَالْإِتْآمُ: أَنْ تَلِدَ الْأُنْثَى تَوْأَمَيْنِ؛ وَبَالَغَ فِي وَصْفِهَا بِاسْتِتْبَاعِ الشَّرِّ بِشَيْئَيْنِ: جَعْلِهَا لَاقِحَةً كِشَافًا، وَإِتْآمِهَا (الزَّوْزَنِيُّ)", " — إِتْآم is for a female to bear twins; he heightens the picture of the evil war drags after it in two ways: she conceives twice a year, and she bears twins (al-Zawzanī)", " — «it'âm»: dişinin ikiz doğurması; harbin ardından şer getirmesini iki şeyle mübalağalı anlatmıştır: yılda iki kez gebe kalması ve ikiz doğurması (Zevzenî)"),
     segs=SG(("فَ", "fa", "conj"), ("تُتْئِمِ", "atama-twin", "verb")))])
# ---- v. 31 ----
V(S4, "Then it bears you boys of ill omen, every one of them like the Red Man of ʿĀd; then it suckles, and then it weans.",
  "Sonra size uğursuzluk çocukları doğurur; hepsi Âd'ın Kızıl'ı (deveyi boğazlayan) gibidir; sonra emzirir, sonra da sütten keser.",
 [JV("فَتُنْتِجْ", "antaja", "atf-jawab", "sukun", g=["atf-nasaq", "form-iv-verbs", "tarshih-wa-tajrid"], doer=HIYA_HARB, pre=FA3,
     note=(" — مَعْطُوفٌ عَلَى «تُتْئِمِ»؛ وَأَنْتَجَتْ: وَلَدَتْ، وَهُوَ تَرْشِيحٌ لِلِاسْتِعَارَةِ الْمَكْنِيَّةِ فِي الْبَيْتِ قَبْلَهُ", " — joined to «bears twins»; أَنْتَجَتْ «she brought forth» carries on the isti'ara makniyya of the verse before", " — «ikiz doğurur»a ma'tûf; «entecet»: doğurdu; önceki beyitteki istiâre-i mekniyyenin terşîhidir"),
     segs=SG(("فَ", "fa", "conj"), ("تُنْتِجْ", "antaja", "verb"))),
  LAHU2("لَكُمْ", "pron-2mp", " («size»)", note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُنْتِجْ»", "; the phrase hangs on «bears»", "; câr-mecrûr «doğurur»a müteallik")),
  MAFUL("غِلْمَانَ", "ghulam", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ غُلَامٍ؛ وَتَرْكُ تَنْوِينِهِ دَلِيلُ الْإِضَافَةِ", note_en=", annexed — the plural of «boy»; that it has no tanwin shows the annexation", note_tr=", muzâf — gulâm'ın cem'i; tenvinsiz oluşu izâfetin delilidir"),
  MUDAF_ILAYH("أَشْأَمَ", "ashamm", extra=["mamnu-min-sarf", "ism-tafdil"], sign=FATHA_JARR, note_ar=" لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ — أَيْ غِلْمَانَ شُؤْمٍ أَوْ غِلْمَانَ امْرِئٍ أَشْأَمَ؛ وَأَعْرَبَهُ الدُّرَّةُ نَعْتًا لِـ«غِلْمَانَ» ثُمَّ ذَكَرَ الْإِضَافَةَ", note_en=" — by the fatha: an adjective on أَفْعَل, barred from tanwin — «boys of ill omen», or «boys of a most ill-omened man»; al-Durra first parses it as a na't of «boys», then gives the annexation", note_tr=" — fetha ile: ef'al vezninde sıfat, gayr-i munsarif — «uğursuzluk çocukları» yahut «pek uğursuz bir kimsenin çocukları»; Dürre önce «gılmân»ın na'tı olarak i'râb etmiş, sonra izâfeti zikretmiştir"),
  T("كُلُّهُمْ", "kull", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil", "jumla-sifa"],
     "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«غِلْمَانَ».",
     "A mubtada, in raf'; annexed to the attached «them», in the seat of jarr — the nominal clause is a na't of «boys», in the seat of nasb.",
     "Mübtedâ, merfû; bitişik zamire muzâf, zamir mahallen mecrûr — isim cümlesi «gılmân»ın na'tı, mahallen mansûb.",
     segs=SG(("كُلُّ", "kull", "noun"), ("هُمْ", "pron-3mp", "pron")))],
 [T("كَأَحْمَرِ", "ka", "prep", ["huruf-jarr", "idafa-definiteness", "tashbih", "aqsam-al-tashbih", "mubtada-khabar"],
     "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَأَحْمَرِ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «كُلُّهُمْ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْغِلْمَانُ، وَالْمُشَبَّهُ بِهِ أَحْمَرُ عَادٍ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ الشُّؤْمُ وَلَمْ يُصَرَّحْ بِهِ وَجْهًا، وَإِنَّمَا ذُكِرَ وَصْفًا لِلْمُشَبَّهِ فِي «أَشْأَمَ» (الزَّوْزَنِيُّ: كُلُّ وَاحِدٍ مِنْهُمْ يُضَاهِي فِي الشُّؤْمِ عَاقِرَ النَّاقَةِ).",
     "The kaf is a jarr letter of likening; «the Red Man» is in jarr by the kasra, since it is annexed — the jarr phrase hangs on the omitted khabar of «every one of them». Here is a tashbih mursal mujmal: the thing likened is the boys; the thing they are likened to, the Red Man of ʿĀd; the tool is the kaf; the point of likeness is ill omen — not stated as such, only named as a quality of the boys in «of ill omen» (al-Zawzanī: «each of them matches, in ill omen, the hamstringer of the she-camel»).",
     "Kâf cer ve teşbîh harfi; «kızıl» muzâf olduğu için kesre ile mecrûr — câr-mecrûr «hepsi»nin mahzûf haberine müteallik. Burada mürsel mücmel bir teşbîh vardır: müşebbeh çocuklar; müşebbehün bih Âd'ın Kızıl'ı; edat kâf; vech-i şebeh uğursuzluktur — vech olarak açıkça söylenmemiş, yalnızca «eş'em» ile müşebbehin vasfı olarak anılmıştır (Zevzenî: «her biri uğursuzlukta deveyi boğazlayana denktir»).",
     segs=SG(("كَ", "ka", "prep"), ("أَحْمَرِ", "ahmar", "noun"))),
  MUDAF_ILAYH("عَادٍ", "aad", "propn", note_ar=" — أَرَادَ أَحْمَرَ ثَمُودَ وَهُوَ قُدَارُ بْنُ سَالِفٍ عَاقِرُ النَّاقَةِ (الزَّوْزَنِيُّ)؛ وَقِيلَ: لَيْسَ بِغَلَطٍ لِأَنَّ ثَمُودَ يُقَالُ لَهَا عَادٌ الْآخِرَةُ (الدُّرَّةُ عَنِ الْمُبَرِّدِ)", note_en=" — he means the Red Man of Thamūd, Qudār ibn Sālif, who hamstrung the she-camel (al-Zawzanī); some say it is no slip, for Thamūd is called «the later ʿĀd» (al-Durra, from al-Mubarrad)", note_tr=" — Semûd'un Kızıl'ını, deveyi boğazlayan Kudâr b. Sâlif'i kastetmiştir (Zevzenî); bir görüşe göre yanlışlık değildir, çünkü Semûd'a «sonraki Âd» denir (Dürre, Müberred'den)"),
  THUMMA(),
  JV("تُرْضِعْ", "ardaa", "atf-jawab", "sukun", g=["form-iv-verbs", "tarshih-wa-tajrid", "hadhf-al-maful"], doer=HIYA_HARB,
     note=(" — وَالْمَفْعُولُ مَحْذُوفٌ: تُرْضِعْهُمْ؛ وَهُوَ تَرْشِيحٌ لِلِاسْتِعَارَةِ", " — its object is left out: «it suckles them»; it carries the isti'ara further", " — mef'ûlü mahzûf: «onları emzirir»; istiârenin terşîhidir")),
  JV("فَتَفْطِمِ", "fatama", "atf-jawab", "rawi", g=["atf-nasaq", "tarshih-wa-tajrid", "hadhf-al-maful"], doer=HIYA_HARB, pre=FA3,
     note=(" — وَالْمَفْعُولُ مَحْذُوفٌ: أَيْ تَكُونُ وِلَادَتُهُمْ وَنُشُوءُهُمْ فِي الْحُرُوبِ (الزَّوْزَنِيُّ)", " — its object is left out: they are born and reared in the wars (al-Zawzanī)", " — mef'ûlü mahzûf: yani doğumları ve yetişmeleri harpler içinde olur (Zevzenî)"),
     segs=SG(("فَ", "fa", "conj"), ("تَفْطِمِ", "fatama", "verb")))])
# ---- v. 32 ----
V(S4, "And so it yields you a harvest such as villages in Iraq never yield their people, in measures of grain and in silver coin.",
  "Böylece size öyle bir «hasılat» getirir ki, Irak'taki köyler ölçek ölçek tahıl ve dirhem olarak onu kendi halkına getirmez.",
 [JV("فَتُغْلِلْ", "aghalla", "atf-jawab", "sukun", g=["atf-nasaq", "form-iv-verbs", "doubled-verbs", "aqsam-al-istiara", "istiara"], doer=HIYA_HARB, pre=FA3,
     note=(" — وَفُكَّ إِدْغَامُهُ فِي الْجَزْمِ. وَفِيهِ اسْتِعَارَةٌ تَهَكُّمِيَّةٌ: اسْتُعِيرَتِ الْغَلَّةُ لِضِدِّهَا وَهُوَ مَا تَجُرُّهُ الْحَرْبُ مِنَ الْمَضَارِّ — يَتَهَكَّمُ وَيَهْزَأُ بِهِمْ (الزَّوْزَنِيُّ)", " — in jazm its doubled letter is unmerged. Here is an isti'ara of mockery (tahakkumiyya): «harvest» is lent to its opposite, the harm that war brings in — he is mocking them (al-Zawzanī)", " — cezim halinde idgâmı çözülmüştür. Burada istiâre-i tehekkümiyye vardır: «hasılat» zıddı için, harbin getirdiği zararlar için ödünç alınmıştır — onlarla alay etmektedir (Zevzenî)"),
     segs=SG(("فَ", "fa", "conj"), ("تُغْلِلْ", "aghalla", "verb"))),
  LAHU2("لَكُمْ", "pron-2mp", " («size»)", note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُغْلِلْ»", "; the phrase hangs on «yields»", "; câr-mecrûr «getirir»e müteallik")),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
     "A relative noun «what», built on sukun, in the seat of nasb as the direct object.",
     "İsm-i mevsûl «…-diği şey», sükûn üzere mebnî; mef'ûlün bih olarak mahallen mansûb."),
  LA_NAFIYA(),
  T("تُغِلُّ", "aghalla", "verb", ["mudari-marfu", "form-iv-verbs", "doubled-verbs", "ism-mawsul", "hadhf-al-maful"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ «قُرًى» بَعْدَهُ، وَالْعَائِدُ مَحْذُوفٌ تَقْدِيرُهُ: تُغِلُّهُ" + SILA_[0] + ".",
     "Present verb in raf'; its doer, «villages», follows; the pronoun returning to مَا is left out («yield [it]»)" + SILA_[1] + ".",
     "Merfû muzâri; fâili sonraki «köyler»dir; «mâ»ya dönen âid zamir mahzûf" + SILA_[2] + "."),
  LI_ENC("لِأَهْلِهَا", "ahl", "أَهْلِ", "هَا", note_ar=" — وَالضَّمِيرُ لِلْقُرَى، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُغِلُّ»", note_en="; «their» is the villages, and the phrase hangs on «yield»", note_tr="; zamir köylere döner; câr-mecrûr «getirir»e müteallik")],
 [FAIL("قُرًى", "qarya", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لَفْظًا لِالْتِقَاءِ السَّاكِنَيْنِ", note_ar=" — جَمْعُ قَرْيَةٍ", note_en=" — by a damma estimated on the alif, which drops in sound before the tanwin; the plural of «village»", note_tr=" — tenvinden önce telaffuzda düşen elif üzerinde takdîrî damme ile; karye'nin cem'i"),
  BI_NOUN("بِالْعِرَاقِ", "iraq", "الْعِرَاقِ", pos="propn", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«قُرًى»", note_en=" — the ba means «in»; the phrase hangs on an omitted na't of «villages»", note_tr=" — bâ «-de» anlamındadır; câr-mecrûr «köyler»in mahzûf na'tına müteallik"),
  MIN(role=(" — وَمِنْ بَيَانِيَّةٌ تُبَيِّنُ «مَا»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الْعَائِدِ الْمَحْذُوفِ", "; مِنْ explains the مَا, and the phrase hangs on an omitted hal of the dropped returning pronoun", " — «min» beyâniyyedir, «mâ»yı açıklar; câr-mecrûr mahzûf âid zamirin mahzûf hâline müteallik")),
  MAJR("قَفِيزٍ", "qafiz", note_ar=" — مِكْيَالٌ", note_en=" — a measure of grain", note_tr=" — bir tahıl ölçeği"),
  ATF("وَدِرْهَمِ", "dirham", case="jarr", extra=["al-qafiya"], **W(RAWI_J))])
CH[4] = S4

# =====================================================================================================================
# Chapter 5 — الْحِكَمُ، الْقِسْمُ الْأَوَّلُ (al-Zawzanī vv. 46–52)
# =====================================================================================================================
S5 = []
MAN_OBJ = ("فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِفِعْلِ الشَّرْطِ", "in the seat of nasb as the fronted object of the condition's verb", "şart fiilinin öne alınmış mef'ûlü olarak mahallen mansûb")
# ---- v. 46 ----
V(S5, "I am weary of the burdens of life; and whoever lives eighty years — mark it well! — grows weary.",
  "Hayatın külfetlerinden usandım; kim seksen yıl yaşarsa — iyi bil ki — elbette usanır.",
 [MADI_T("سَئِمْتُ", "saima", who="ana", extra=["radd-al-ajuz", "mulhaq-bil-jinas"], note_ar=" — وَبَيْنَ «سَئِمْتُ» فِي صَدْرِ الْبَيْتِ وَ«يَسْأَمِ» فِي آخِرِهِ رَدُّ الْعَجُزِ عَلَى الصَّدْرِ، وَيَجْمَعُهُمَا الِاشْتِقَاقُ", note_en=" — «I am weary» at the head of the verse and «grows weary» at its close make a radd al-'ajuz 'ala al-sadr; the two are of one root", note_tr=" — beytin başındaki «usandım» ile sonundaki «usanır» arasında reddü'l-acüz ale's-sadr vardır; ikisi aynı köktendir"),
  MAFUL("تَكَالِيفَ", "takalif", extra=["jam-taksir", "mamnu-min-sarf", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعٌ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ: الْمَشَاقُّ وَالشَّدَائِدُ", note_en=", annexed — a «farthest plural»: hardships and toils", note_tr=", muzâf — muntehe'l-cumû' vezninde cemi: meşakkatler, sıkıntılar"),
  MUDAF_ILAYH("الْحَيَاةِ", "hayat"),
  MAN("وَمَنْ", D("يَعِشْ", "sukun"), D("يَسْأَمِ", "rawi"), lead=("الْوَاوُ عَاطِفَةٌ أَوْ حَالِيَّةٌ (الدُّرَّةُ)، وَ", "The waw conjoins, or opens a hal clause (al-Durra); ", "Vâv atıf yahut hâl içindir (Dürre); ")),
  JV("يَعِشْ", "asha-live", "shart", "sukun", g=["hollow-verbs"], note=(" — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (يَعِيشُ ← يَعِشْ)", " — a hollow verb whose middle letter drops where two quiescents meet (يَعِيشُ → يَعِشْ)", " — ecvef fiil; iki sâkin karşılaştığı için aynü'l-fiili düşmüştür (yeîşü → yeiş)"))],
 [T("ثَمَانِينَ", "thamanun", "noun", ["maful-fih", "asma-al-adad-fil-kafiya", "jam-mudhakkar-salim"],
     "نَائِبٌ عَنْ ظَرْفِ الزَّمَانِ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، مُتَعَلِّقٌ بِـ«يَعِشْ» — وَقِيلَ: مَفْعُولٌ بِهِ (الدُّرَّةُ).",
     "It stands for an adverb of time, in nasb by the ya — «eighty» is declined like the sound masculine plural — and hangs on «lives»; some read it as a direct object (al-Durra).",
     "Zaman zarfı yerine geçer; cem-i müzekker sâlime mülhak olduğu için yâ ile mansûb, «yaşarsa»ya müteallik; bir görüşe göre mef'ûlün bihtir (Dürre)."),
  TAMYIZ("حَوْلًا", "hawl-year"),
  T("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "itirad", "jumla-mutarida"],
     "نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ. وَجُمْلَةُ «لَا أَبَا لَكَ» مُعْتَرِضَةٌ بَيْنَ الشَّرْطِ وَجَوَابِهِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ وَهِيَ كَلِمَةٌ جَافِيَةٌ لَا يُرَادُ بِهَا الْجَفَاءُ وَإِنَّمَا يُرَادُ بِهَا التَّنْبِيهُ وَالْإِعْلَامُ (الزَّوْزَنِيُّ) — وَالِاعْتِرَاضُ مِنَ الْإِطْنَابِ.",
     "The لَا that denies the whole genus, working like إِنَّ. The clause «you have no father» is a parenthesis between the condition and its answer, with no seat of its own; a rough phrase by which no roughness is meant, only to rouse and to tell (al-Zawzanī) — and the parenthesis is one of the kinds of itnab.",
     "Cinsi nefyeden «lâ»; inne gibi amel eder. «Lâ ebâ leke» cümlesi şart ile cevabı arasında mu'tarızadır, mahalli yoktur; kaba bir sözdür ama kabalık kastedilmez, yalnızca uyarmak ve bildirmek kastedilir (Zevzenî) — i'tirâz ıtnâb çeşitlerindendir."),
  T("أَبَا", "ab", "noun", ["la-nafiya-lil-jins", "five-nouns"],
     "اسْمُ «لَا» مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ إِلَى الْكَافِ وَاللَّامُ مُقْحَمَةٌ بَيْنَهُمَا؛ وَقِيلَ: مَبْنِيٌّ عَلَى الْأَلِفِ عَلَى لُغَةِ الْقَصْرِ وَ«لَكَ» خَبَرٌ (الدُّرَّةُ).",
     "The noun of لَا, in nasb by the alif — one of the five nouns — annexed to the kaf, with the lam thrust in between them; others read it as built, on the dialect that keeps the alif throughout, with لَكَ as the predicate (al-Durra).",
     "«Lâ»nın ismi; esmâ-i hamseden olduğu için elif ile mansûb; kâfa muzâf olup lâm aralarına sokulmuştur; bir görüşe göre kasr lügatine göre elif üzere mebnîdir ve «leke» haberdir (Dürre)."),
  LAHU2("لَكَ", "pron-2ms", " («senin için»)", note=(" — وَاللَّامُ مُقْحَمَةٌ عَلَى الْوَجْهِ الْأَوَّلِ، وَخَبَرُ «لَا» مَحْذُوفٌ تَقْدِيرُهُ: مَوْجُودٌ", "; on the first reading the lam is thrust in, and the predicate of لَا is left out: «[exists]»", "; ilk vecihte lâm mukhamedir; «lâ»nın haberi mahzûftur: «mevcut»")),
  JV("يَسْأَمِ", "saima", "jawab", "rawi", g=["radd-al-ajuz", "mulhaq-bil-jinas"])])
# ---- v. 47 ----
V(S5, "I know what is in today, and in yesterday before it; but to the knowledge of what is in tomorrow I am blind.",
  "Bugünde olanı ve ondan önceki dünde olanı bilirim; fakat yarında olanı bilmeye karşı körüm.",
 [T("وَأَعْلَمُ", "alima", "verb", ["mudari-marfu", "al-fail-al-mudmar-al-mustatir-wujuban", "mulhaq-bil-jinas", "anwa-al-waw"],
     WA_ISTINAF[0] + "أَعْلَمُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا. وَبَيْنَهُ وَبَيْنَ «عِلْمِ» اشْتِقَاقٌ مُلْحَقٌ بِالْجِنَاسِ.",
     WA_ISTINAF[1] + "أَعْلَمُ is a present verb in raf'; the doer «I» must stay hidden. It shares a root with عِلْمِ — the derivation that is attached to jinas.",
     WA_ISTINAF[2] + "«bilirim»: merfû muzâri; fâil vücûben gizli «ben». «İlm» ile arasında cinâsa mülhak iştikâk vardır.",
     segs=SG(("وَ", "wa", "conj"), ("أَعْلَمُ", "alima", "verb"))),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
     "A relative noun «what», built on sukun, in the seat of nasb as the direct object.",
     "İsm-i mevsûl «…-an şey», sükûn üzere mebnî; mef'ûlün bih olarak mahallen mansûb."),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِلَةِ الْمَوْصُولِ", "; the jarr phrase hangs on the omitted ṣila of the relative", " — câr-mecrûr ism-i mevsûlün mahzûf sılasına müteallik")),
  MAJR("الْيَوْمِ", "yawm", extra=["tibaq"], note_ar=" — وَبَيْنَ «الْيَوْمِ» وَ«الْأَمْسِ» وَ«غَدٍ» طِبَاقٌ", note_en=" — «today», «yesterday» and «tomorrow» make a tibaq", note_tr=" — «bugün», «dün» ve «yarın» arasında tıbâk vardır"),
  ATF("وَالْأَمْسِ", "ams", case="jarr", extra=["tibaq"], note_ar=" — وَهُوَ مُعْرَبٌ لِاقْتِرَانِهِ بِأَلْ", note_en=" — declined here because it carries the article", note_tr=" — elif-lâm aldığı için burada mu'rebdir"),
  T("قَبْلَهُ", "qabla", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "ijaz-itnab-musawat"],
     "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنَ «الْأَمْسِ»، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْيَوْمِ. وَهُوَ حَشْوٌ غَيْرُ مُفْسِدٍ لِلْمَعْنَى لِأَنَّ الْأَمْسَ لَا يَكُونُ إِلَّا قَبْلَ الْيَوْمِ؛ وَبِهٰذَا الْبَيْتِ مَثَّلَ صَاحِبُ التَّلْخِيصِ لَهُ فِي بَابِ الْإِيجَازِ وَالْإِطْنَابِ، وَرِوَايَتُهُ: «وَأَعْلَمُ عِلْمَ الْيَوْمِ».",
     "An adverb of time, in nasb, hanging on an omitted hal of «yesterday»; annexed to the attached «it» (today), in the seat of jarr. It is padding that does no harm to the sense (ḥashw ghayr mufsid), since yesterday can only be before today; this is the very verse the Talkhīṣ cites for it, in the chapter of ijaz and itnab, in the reading وَأَعْلَمُ عِلْمَ الْيَوْمِ.",
     "Zaman zarfı, mansûb; «dün»ün mahzûf hâline müteallik; bitişik zamire muzâf, zamir (bugün) mahallen mecrûr. Mânâyı bozmayan bir haşivdir, çünkü dün ancak bugünden önce olur; Telhîs sahibi îcâz ve ıtnâb bâbında buna tam da bu beyti misal getirir; onun rivayeti «ve a'lemü ilme'l-yevmi» şeklindedir.",
     segs=SG(("قَبْلَ", "qabla", "noun"), ("هُ", "pron-3ms", "pron")))],
 [T("وَلٰكِنَّنِي", "lakinna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "ya-al-mutakallim", "kaanna-lakinna-layta-laalla-fil-kafiya"],
     WA_AR + "لٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.",
     "The waw conjoins; لٰكِنَّ «but» is the particle of correction that puts its noun in nasb; the nun guards it, and the ya «I» is its noun, in the seat of nasb.",
     "«ve» + lâkinne «fakat»: istidrâk ve nasb harfi; nûn vikâye içindir; yâ ismidir, mahallen mansûb.",
     segs=SG(("وَ", "wa", "conj"), ("لٰكِنَّ", "lakinna", "part"), ("نِ", "nun-wiqaya", "part"), ("ي", "pron-1s", "pron"))),
  PREP("عَنْ", "an", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَمِي»", role_en="; the phrase hangs on «blind»", role_tr="; câr-mecrûr «kör»e müteallik", gloss_tr="«-den»"),
  MAJR("عِلْمِ", "ilm", extra=["masdar", "mulhaq-bil-jinas", "idafa-definiteness"], note_ar="، مُضَافٌ إِلَى مَفْعُولِهِ", note_en=", annexed to its object", note_tr=", mef'ûlüne muzâf"),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "A relative noun «what», built on sukun, in the seat of jarr as the second term of the idafa.",
     "İsm-i mevsûl «…-an şey», sükûn üzere mebnî; muzâfun ileyh olarak mahallen mecrûr."),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِلَةِ الْمَوْصُولِ", "; the jarr phrase hangs on the omitted ṣila of the relative", " — câr-mecrûr ism-i mevsûlün mahzûf sılasına müteallik")),
  MAJR("غَدٍ", "ghad", extra=["tibaq"]),
  T("عَمِي", "amin-blind", "noun", ["inna-wa-akhawatuha", "ism-maqsur-manqus", "sifa-mushabbaha", "al-qafiya", "istiara", "istiara-tabaiyya"],
     "خَبَرُ لٰكِنَّ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَأَصْلُهُ عَمٍ — وَهٰذِهِ الْيَاءُ الْمَرْسُومَةُ لِلْإِشْبَاعِ وَالْإِطْلَاقِ لَا يَاءُ الْمَنْقُوصِ (الدُّرَّةُ). وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شُبِّهَ الْجَهْلُ بِمَا فِي غَدٍ بِالْعَمَى، ثُمَّ اشْتُقَّ مِنْهُ «عَمٍ» بِمَعْنَى جَاهِلٍ (الزَّوْزَنِيُّ: عَمِيُّ الْقَلْبِ عَنِ الْإِحَاطَةِ بِمَا هُوَ مُنْتَظَرٌ).",
     "The predicate of لٰكِنَّ, in raf' by a damma estimated on the ya, which is dropped where two quiescents meet — the word is عَمٍ — and the ya written here is the lengthening of the rhyme, not the ya of the manqūṣ (al-Durra). Here is an isti'ara tasrihiyya taba'iyya: not knowing what tomorrow holds is likened to blindness, and from it «blind» is drawn for «unknowing» (al-Zawzanī: «blind of heart to what is still awaited»).",
     "Lâkinne'nin haberi; iki sâkin karşılaştığı için hazfedilen yâ üzerinde takdîrî damme ile merfû — aslı «amin»dir — buradaki yazılı yâ mankûsun yâ'sı değil, kâfiyenin işbâ' ve ıtlâk yâ'sıdır (Dürre). Burada istiâre-i tasrîhiyye-i tebeiyye vardır: yarında olanı bilmemek körlüğe benzetilmiş, sonra ondan «kör» kelimesi «bilmeyen» anlamında türetilmiştir (Zevzenî: «beklenen şeyi kuşatmaya karşı kalbi kör»).")])
# ---- v. 48 ----
V(S5, "I have seen the Fates strike like a night-blind she-camel's stumbling: whom they hit they kill, and whom they miss is given long life, and grows old.",
  "Ecelleri, gece görmeyen devenin rastgele basışı gibi çarparken gördüm: kime isabet ederlerse onu öldürürler; kimi de ıskalarlarsa ömrü uzatılır ve ihtiyarlar.",
 [MADI_T("رَأَيْتُ", "raa", who="ana", extra=["naqis-verbs", "mafulayn", "al-mutaaddi-wa-afal-al-qulub"], note_ar=" — وَهِيَ عِلْمِيَّةٌ تَنْصِبُ مَفْعُولَيْنِ", note_en=" — «saw» in the sense of «knew», with two objects", note_tr=" — «bildim» anlamında, iki mef'ûl alır"),
  MAFUL("الْمَنَايَا", "maniyya", extra=["jam-taksir", "ism-maqsur-manqus", "mafulayn"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — الْمَفْعُولُ الْأَوَّلُ؛ جَمْعُ مَنِيَّةٍ", note_en=" — by a fatha estimated on the alif; the first object; the plural of مَنِيَّة «death, fate»", note_tr=" — elif üzerinde takdîrî fetha ile; birinci mef'ûl; «meniyye»nin (ölüm, ecel) cem'i"),
  T("خَبْطَ", "khabt", "noun", ["maful-mutlaq", "idafa-definiteness", "tashbih", "aqsam-al-tashbih", "mafulayn"],
     "مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ: تَخْبِطُ خَبْطَ عَشْوَاءَ، مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ إِلَى فَاعِلِهِ — وَالْجُمْلَةُ الْمَحْذُوفَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ لِـ«رَأَيْتُ». وَفِيهِ تَشْبِيهٌ بَلِيغٌ — مُؤَكَّدٌ مُجْمَلٌ: الْمُشَبَّهُ إِصَابَةُ الْمَنَايَا النَّاسَ، وَالْمُشَبَّهُ بِهِ خَبْطُ الْعَشْوَاءِ وَهِيَ النَّاقَةُ الَّتِي لَا تُبْصِرُ لَيْلًا، وَحُذِفَتِ الْأَدَاةُ وَوَجْهُ الشَّبَهِ وَهُوَ الْوُقُوعُ عَلَى غَيْرِ نَسَقٍ وَبَصِيرَةٍ (الزَّوْزَنِيُّ).",
     "A maf'ul mutlaq of an omitted verb — «they strike with the striking of a night-blind camel» — in nasb, annexed to its doer; the omitted clause is the second object of «I have seen», in the seat of nasb. Here is a tashbih baligh — mu'akkad and mujmal: the thing likened is the Fates' falling on people; the thing it is likened to, the stumbling of the عَشْوَاء, the she-camel that cannot see by night; the tool is dropped, and so is the point of likeness — falling without order and without sight (al-Zawzanī).",
     "Mahzûf bir fiilin mef'ûl-i mutlakı — «gece körü devenin çarpması gibi çarparlar» — mansûb, fâiline muzâf; mahzûf cümle «gördüm»ün ikinci mef'ûlü, mahallen mansûb. Burada teşbîh-i belîğ — müekked mücmel — vardır: müşebbeh ecellerin insanlara isabeti; müşebbehün bih «aşvâ'»nın, yani gece görmeyen dişi devenin rastgele basışı; edat da vech-i şebeh de — düzensiz ve görmeden vâki olmak — hazfedilmiştir (Zevzenî)."),
  MUDAF_ILAYH("عَشْوَاءَ", "ashwa", extra=["mamnu-min-sarf", "ism-mamdud"], sign=FATHA_JARR, note_ar=" لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ — تَأْنِيثُ الْأَعْشَى", note_en=" — by the fatha: a diptote, for its lengthened feminine alif — the feminine of أَعْشَى «night-blind»", note_tr=" — fetha ile: elif-i memdûde-i te'nîs sebebiyle gayr-i munsarif — «a'şâ»nın (gece körü) müennesi"),
  MAN("مَنْ", D("تُصِبْ", "sukun"), D("تُمِتْهُ", "sukun"), seat=MAN_OBJ,
      tail=(" — وَقِيلَ: «مَنْ» مُبْتَدَأٌ وَمَفْعُولُ «تُصِبْ» مَحْذُوفٌ، وَعَلَيْهِ تَفْسِيرُ الزَّوْزَنِيِّ. وَفِي الْبَيْتِ مُقَابَلَةُ اثْنَيْنِ بِاثْنَيْنِ: «تُصِبْ … تُمِتْهُ» وَ«تُخْطِئْ … يُعَمَّرْ»", " — others read مَنْ as a mubtada with the object of «they hit» left out, and so al-Zawzanī explains it. The verse holds a muqabala of two with two: «hit … kill» against «miss … is given long life»", " — bir görüşe göre «men» mübtedâdır ve «isabet ederlerse»nin mef'ûlü mahzûftur; Zevzenî'nin açıklaması buna göredir. Beyitte ikiye iki mukâbele vardır: «isabet — öldürme» ile «ıskalama — ömür verme»")),
  JV("تُصِبْ", "asaba", "shart", "sukun", g=["form-iv-verbs", "hollow-verbs", "muqabala", "tibaq"], doer=("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْمَنَايَا", "; the doer is the hidden «she» — the Fates", "; fâil ecellere dönen gizli zamir «o»"),
     note=(" — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (تُصِيبُ ← تُصِبْ)؛ وَبَيْنَهُ وَبَيْنَ «تُخْطِئْ» طِبَاقٌ", " — a hollow verb whose middle letter drops where two quiescents meet (تُصِيبُ → تُصِبْ); with «miss» it makes a tibaq", " — ecvef fiil; iki sâkin karşılaştığı için aynü'l-fiili düşmüştür (tusîbü → tusib); «ıskalarlarsa» ile arasında tıbâk vardır"))],
 [T("تُمِتْهُ", "amata", "verb", G_SHART + ["form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil", "maful-bihi", "muqabala", "tibaq"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ لِأَنَّهُ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْمَنَايَا، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى «مَنْ» — وَبَيْنَهُ وَبَيْنَ «يُعَمَّرْ» طِبَاقٌ.",
     "Present verb in jazm as the answer of the condition, its sign the sukun; the doer is the hidden «she» (the Fates), and the attached «him», returning to مَنْ, is the object, in the seat of nasb — with «is given long life» it makes a tibaq.",
     "Şartın cevabı olarak meczûm muzâri, alâmeti sükûn; fâil ecellere dönen gizli zamir «o»; «men»e dönen bitişik «onu» mef'ûlün bih, mahallen mansûb — «ömrü uzatılır» ile arasında tıbâk vardır.",
     segs=SG(("تُمِتْ", "amata", "verb"), ("هُ", "pron-3ms", "pron"))),
  MAN("وَمَنْ", D("تُخْطِئْ", "sukun"), D("يُعَمَّرْ", "sukun"), seat=MAN_OBJ,
      tail=(" — أَوْ مُبْتَدَأٌ عَلَى حَذْفِ الْمَفْعُولِ: وَمَنْ تُخْطِئْهُ (الزَّوْزَنِيُّ)", " — or a mubtada, with the object left out: «and whom they miss [him]» (al-Zawzanī)", " — yahut mef'ûlün hazfiyle mübtedâ: «kimi ıskalarlarsa» (Zevzenî)")),
  JV("تُخْطِئْ", "akhtaa", "shart", "sukun", g=["form-iv-verbs", "muqabala", "tibaq", "hadhf-al-maful"], doer=("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْمَنَايَا", "; the doer is the hidden «she» — the Fates", "; fâil ecellere dönen gizli zamir «o»"),
     note=(" — وَالسُّكُونُ ظَاهِرٌ عَلَى الْهَمْزَةِ", " — the sukun shows on the hamza", " — sükûn hemze üzerinde zâhirdir")),
  JV("يُعَمَّرْ", "ammara-life", "jawab", "sukun", g=["form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya", "muqabala", "tibaq"], passive=True, doer=NAIB_HUWA,
     note=(" — وَالتَّعْمِيرُ: تَطْوِيلُ الْعُمُرِ", " — تَعْمِير is the lengthening of one's life", " — «ta'mîr»: ömrün uzatılması")),
  JV("فَيَهْرَمِ", "harima", "atf-jawab", "rawi", g=["atf-nasaq"], pre=FA3, segs=SG(("فَ", "fa", "conj"), ("يَهْرَمِ", "harima", "verb")))])
# ---- v. 49 ----
V(S5, "Whoever does not deal gently with people in many matters is bitten with fangs and trodden under a camel's foot.",
  "Kim birçok işte insanlarla güzel geçinmezse, köpek dişleriyle ısırılır ve deve tabanıyla çiğnenir.",
 [MAN("وَمَنْ", ("«يُصَانِعْ» مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَ«لَمْ يُصَانِعْ» فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "«deal gently», in jazm by لَمْ, its sign the sukun — and لَمْ يُصَانِعْ stands in the seat of jazm as the condition's verb", "«güzel geçinmezse»; lem ile meczûm, alâmeti sükûn — «lem yusâni'» şart fiili olarak mahallen meczûm"), D("يُضَرَّسْ", "sukun")),
  LAM_JAZM("لَمْ"),
  T("يُصَانِعْ", "sanaa-deal", "verb", G_SHART + ["lam-jazim", "form-iii-verbs", "hadhf-al-maful"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + HUWA[0] + "، وَالْمَفْعُولُ مَحْذُوفٌ أَيِ النَّاسَ — وَ«لَمْ» وَمَا دَخَلَتْ عَلَيْهِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ؛ وَالْمُصَانَعَةُ: الْمُدَارَاةُ.",
     "Present verb in jazm by لَمْ, its sign the sukun" + HUWA[1] + "; its object — «people» — is left out — لَمْ with its verb stands in the seat of jazm as the condition's verb; مُصَانَعَة is to deal gently, to humour.",
     "Lem ile meczûm muzâri, alâmeti sükûn" + HUWA[2] + "; mef'ûlü — «insanlar» — mahzûf — «lem» ve fiili şart fiili olarak mahallen meczûm; «musâna'a»: idare etmek, güzel geçinmek."),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُصَانِعْ»", "; the phrase hangs on «deal gently»", " — câr-mecrûr «güzel geçinmezse»ye müteallik")),
  MAJR("أُمُورٍ", "amr", extra=["jam-taksir"], note_ar=" — جَمْعُ أَمْرٍ", note_en=" — the plural of «matter»", note_tr=" — emr'in cem'i"),
  NAAT("كَثِيرَةٍ", "kathir", "jarr")],
 [JV("يُضَرَّسْ", "darrasa", "jawab", "sukun", g=["form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya", "istiara", "istiara-tabaiyya"], passive=True, doer=NAIB_HUWA,
     note=(" — وَالتَّضْرِيسُ مُبَالَغَةُ الضَّرْسِ وَهُوَ الْعَضُّ بِالضِّرْسِ. وَفِيهِ وَفِي «يُوطَأْ» اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شُبِّهَ قَهْرُ النَّاسِ لَهُ وَإِذْلَالُهُمْ إِيَّاهُ بِالْعَضِّ بِالْأَنْيَابِ وَالْوَطْءِ بِالْمَنْسِمِ (الزَّوْزَنِيُّ: قَهَرُوهُ وَأَذَلُّوهُ كَالَّذِي يُضَرَّسُ بِالنَّابِ وَيُوطَأُ بِالْمَنْسِمِ)", " — تَضْرِيس is the intensive of ضَرْس, biting with the back teeth. In it and in «is trodden» there is an isti'ara tasrihiyya taba'iyya: people's overpowering and abasing him is likened to biting with fangs and treading under a camel's foot (al-Zawzanī: «they overpower and abase him, like one bitten by the fang and trodden by the foot»)", " — «tadrîs», azı dişiyle ısırmak anlamındaki «dars»ın mübalağasıdır. Bunda ve «çiğnenir»de istiâre-i tasrîhiyye-i tebeiyye vardır: insanların onu kahredip zelil etmesi, dişlerle ısırmaya ve deve tabanıyla çiğnemeye benzetilmiştir (Zevzenî: «onu kahreder ve zelil ederler; tıpkı dişle ısırılan ve tabanla çiğnenen gibi»)")),
  BI_NOUN("بِأَنْيَابٍ", "nab", "أَنْيَابٍ", extra=["jam-taksir"], note_ar=" — جَمْعُ نَابٍ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُضَرَّسْ»", note_en=" — the plural of «fang»; the phrase hangs on «is bitten»", note_tr=" — nâb'ın cem'i; câr-mecrûr «ısırılır»a müteallik"),
  JV("وَيُوطَأْ", "watia", "atf-jawab", "sukun", g=["atf-nasaq", "naib-al-fail", "al-majhul-fil-kafiya", "mithal-verbs", "istiara"], passive=True, doer=NAIB_HUWA, pre=WA3,
     note=(" — وَالسُّكُونُ ظَاهِرٌ عَلَى الْهَمْزَةِ؛ وَيَجُوزُ فِي الْمَعْطُوفِ عَلَى الْجَوَابِ الرَّفْعُ وَالنَّصْبُ أَيْضًا (الدُّرَّةُ)", " — the sukun shows on the hamza; a verb joined to the answer may also be read in raf' or in nasb (al-Durra)", " — sükûn hemze üzerinde zâhirdir; cevaba atfedilen fiilde ref ve nasb da caizdir (Dürre)"),
     segs=SG(("وَ", "wa", "conj"), ("يُوطَأْ", "watia", "verb"))),
  BI_NOUN("بِمَنْسِمِ", "mansim", "مَنْسِمِ", extra=["al-qafiya"], note_ar=" — وَهُوَ لِلْبَعِيرِ بِمَنْزِلَةِ السُّنْبُكِ لِلْفَرَسِ" + RAWI_J[0], note_en=" — the camel's foot-pad, what the hoof-tip is to a horse" + RAWI_J[1], note_tr=" — devenin tabanı; atın tırnak ucu ne ise deve için odur" + RAWI_J[2])])
# ---- helpers for the rest of the وَمَنْ run ----
SGN["nun-kana"] = ("السُّكُونُ عَلَى النُّونِ الْمَحْذُوفَةِ لِلتَّخْفِيفِ", "the sukun on its nun — and the nun itself is dropped for lightness", "hafiflik için hazfedilen nûn üzerindeki sükûn")
def LAM_SH(word, en, tr):
    """«لَمْ يَفْعَلْ» as the condition of مَنْ: the verb is in jazm by لَمْ, and لَمْ with its verb stands in the seat of jazm"""
    return ("«" + word + "» مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَ«لَمْ " + word + "» فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ",
            "«" + en + "», in jazm by لَمْ, its sign the sukun — and لَمْ " + word + " stands in the seat of jazm as the condition's verb",
            "«" + tr + "»; lem ile meczûm, alâmeti sükûn — «lem» ve fiili şart fiili olarak mahallen meczûm")
def KJ(full, role, sign, ism, note=("", "", ""), g=None):
    """the defective كَانَ in jazm as condition or answer: يَكُ، يَكُنْ، تَكُنْ"""
    R = {"shart": ("لِأَنَّهُ فِعْلُ الشَّرْطِ", "as the condition's verb", "şart fiili olarak"),
         "jawab": ("لِأَنَّهُ جَوَابُ الشَّرْطِ", "as the answer of the condition", "şartın cevabı olarak")}[role]
    s = SGN[sign]
    return T(full, "kana", "verb", G_SHART + ["kana-wa-akhawatuha", "hollow-verbs"] + (g or []),
        "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ " + R[0] + " وَعَلَامَةُ جَزْمِهِ " + s[0] + "، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + ism[0] + note[0] + ".",
        "The defective present verb (of كَانَ), in jazm " + R[1] + ", its sign " + s[1] + "; it raises its noun and puts its predicate in nasb" + ism[1] + note[1] + ".",
        cap(R[2] + " meczûm nâkıs muzâri (kâne'den), alâmeti " + s[2] + "; ismini ref, haberini nasb eder" + ism[2] + note[2] + "."))
LA_SH = lambda: T("لَا", "la-nafiya", "part", ["la-nafiya"],
    "لَا نَافِيَةٌ لَا عَمَلَ لَهَا، وَلَا تَحُولُ بَيْنَ اسْمِ الشَّرْطِ وَجَزْمِ الْفِعْلِ بَعْدَهَا.",
    "The negating لَا, which governs nothing — and does not come between the conditional noun and the jazm of the verb after it.",
    "Nefiy lâ'sı; amel etmez — şart ismi ile ondan sonraki fiilin cezmi arasına da girmez.")

# ---- v. 50 ----
V(S5, "Whoever sets kindness as a shield before his honour keeps it whole; and whoever does not guard against abuse is abused.",
  "Kim iyiliği ırzının önüne siper ederse onu korur (çoğaltır); kim de sövülmekten sakınmazsa sövülür.",
 [MAN("وَمَنْ", D("يَجْعَلِ", "kasr2"), D("يَفِرْ", "sukun")),
  JV("يَجْعَلِ", "jaala", "shart", "kasr2"),
  MAFUL("الْمَعْرُوفَ", "maruf", extra=["ism-maful"], note_ar=" — وَهُوَ كُلُّ مَا يَحْسُنُ مِنْ قَوْلٍ أَوْ فِعْلٍ", note_en=" — «kindness»: every fair word or deed", note_tr=" — «ma'rûf»: güzel olan her söz ve iş"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَجْعَلِ»", "; the phrase hangs on «sets»", " — câr-mecrûr «kılarsa»ya müteallik")),
  MAJR("دُونِ", "duna", **W(MUD, (" — أَيْ: أَمَامَ عِرْضِهِ حَاجِزًا عَنْهُ", " — «before his honour», as a barrier in front of it", " — yani ırzının önünde, ona siper olarak"))),
  ENC_NOUN("عِرْضِهِ", "ird", "هِ", "mudaf", note_ar=" — وَالْعِرْضُ: مَوْضِعُ الْمَدْحِ وَالذَّمِّ مِنَ الْإِنْسَانِ", note_en=" — عِرْض is that in a man which is praised or blamed: his honour", note_tr=" — «ırz»: insanın övülen yahut yerilen yönü, şerefi")],
 [T("يَفِرْهُ", "wafara", "verb", G_SHART + ["mithal-verbs", "al-bariz-al-muttasil", "maful-bihi"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ لِأَنَّهُ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + HUWA[0] + "، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى الْعِرْضِ — مِثَالٌ وَاوِيٌّ حُذِفَتْ فَاؤُهُ فِي الْمُضَارِعِ (وَفَرَ يَفِرُ)؛ وَفَرْتُ الشَّيْءَ أَفِرُهُ وَفْرًا: أَكْثَرْتُهُ (الزَّوْزَنِيُّ)، أَيْ يَصُنْهُ وَافِرًا.",
     "Present verb in jazm as the answer of the condition, its sign the sukun" + HUWA[1] + "; the attached «it» (his honour) is the object, in the seat of nasb — a verb whose first radical, waw, drops in the present (وَفَرَ يَفِرُ); «I made the thing abundant» (al-Zawzanī): he keeps his honour whole.",
     "Şartın cevabı olarak meczûm muzâri, alâmeti sükûn" + HUWA[2] + "; ırza dönen bitişik «onu» mef'ûlün bih, mahallen mansûb — fâü'l-fiili vâv olan misâl; vâv muzâride düşer (vefera yefiru); «bir şeyi çoğalttım» (Zevzenî): yani ırzını eksiksiz korur.",
     segs=SG(("يَفِرْ", "wafara", "verb"), ("هُ", "pron-3ms", "pron"))),
  MAN("وَمَنْ", D("يَتَّقِ", "ya"), D("يُشْتَمِ", "rawi")),
  LA_SH(),
  JV("يَتَّقِ", "ittaqa", "shart", "ya", g=["form-viii-verbs", "naqis-verbs"], note=(" — وَأَصْلُهُ يَوْتَقِي: قُلِبَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ فِي تَاءِ الِافْتِعَالِ", " — it is يَوْتَقِي: the waw turns to ta and merges into the ta of Form VIII", " — aslı «yevtakî»dir: vâv tâ'ya çevrilip iftiâl tâ'sına idgam edilmiştir")),
  MAFUL("الشَّتْمَ", "shatm", extra=["masdar", "mulhaq-bil-jinas"], note_ar=" — أَيْ شَتْمَ النَّاسِ إِيَّاهُ (الزَّوْزَنِيُّ). وَبَيْنَهُ وَبَيْنَ «يُشْتَمِ» اشْتِقَاقٌ مُلْحَقٌ بِالْجِنَاسِ", note_en=" — «people's abuse of him» (al-Zawzanī). It shares a root with «is abused» — the derivation that is attached to jinas", note_tr=" — yani insanların ona sövmesini (Zevzenî). «Sövülür» ile arasında cinâsa mülhak iştikâk vardır"),
  JV("يُشْتَمِ", "shatama", "jawab", "rawi", g=["naib-al-fail", "al-majhul-fil-kafiya", "mulhaq-bil-jinas"], passive=True, doer=NAIB_HUWA)])
# ---- v. 51 ----
V(S5, "Whoever has abundance and is miserly with it toward his own people — they do without him, and he is blamed.",
  "Kim servet sahibi olur da servetini kavminden esirgerse, ondan müstağni kalınır ve yerilir.",
 [MAN("وَمَنْ", D("يَكُ", "nun-kana"), D("يُسْتَغْنَ", "alif")),
  KJ("يَكُ", "shart", "nun-kana", ("، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»", "; its noun is the hidden «he», which returns to مَنْ", "; ismi «men»e dönen gizli zamir «o»"),
     note=(" — وَأَصْلُهُ يَكُونُ: حُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ عِنْدَ الْجَزْمِ فَصَارَ يَكُنْ، ثُمَّ حُذِفَتِ النُّونُ تَخْفِيفًا لِكَثْرَةِ الِاسْتِعْمَالِ", " — it is يَكُونُ: in jazm the waw drops where two quiescents meet, giving يَكُنْ, and then the nun drops for lightness, the word being so much used", " — aslı «yekûnü»dür: cezimde iki sâkin karşılaştığı için vâv düşer, «yekün» olur; sonra çok kullanıldığı için hafiflik maksadıyla nûn da hazfedilir")),
  T("ذَا", "dhu", "noun", ["kana-wa-akhawatuha", "five-nouns", "idafa-definiteness"],
     "خَبَرُ «يَكُ» مَنْصُوبٌ بِالْأَلِفِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.",
     "The predicate of يَكُ, in nasb by the alif — one of the five nouns — and annexed: «possessed of».",
     "«Yekü»nün haberi; esmâ-i hamseden olduğu için elif ile mansûb, muzâf: «sahibi»."),
  MUDAF_ILAYH("فَضْلٍ", "fadl", note_ar=" — وَالْفَضْلُ هُنَا: الْمَالُ الزَّائِدُ عَنِ الْحَاجَةِ", note_en=" — فَضْل here is wealth beyond one's need", note_tr=" — «fazl» burada ihtiyaçtan artan maldır"),
  JV("فَيَبْخَلْ", "bakhila", "atf-shart", "sukun", g=["atf-nasaq"], pre=FA3,
     note=(" — وَيَجُوزُ فِي الْمَعْطُوفِ عَلَى فِعْلِ الشَّرْطِ بِالْفَاءِ النَّصْبُ أَيْضًا (الدُّرَّةُ)", " — a verb joined by the fa to the condition's verb may also be read in nasb (al-Durra)", " — şart fiiline fâ ile atfedilen fiilde nasb da caizdir (Dürre)"),
     segs=SG(("فَ", "fa", "conj"), ("يَبْخَلْ", "bakhila", "verb"))),
  BI_NOUN("بِفَضْلِهِ", "fadl", "فَضْلِهِ", enc="هِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَبْخَلْ»", note_en="; the phrase hangs on «is miserly»", note_tr="; câr-mecrûr «cimrilik ederse»ye müteallik")],
 [ALA(), ENC_NOUN("قَوْمِهِ", "qawm", "هِ", "majr", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَبْخَلْ» أَيْضًا", note_en="; this phrase too hangs on «is miserly»", note_tr="; bu câr-mecrûr da «cimrilik ederse»ye müteallik"),
  JV("يُسْتَغْنَ", "istaghna", "jawab", "alif", g=["form-x-verbs", "naqis-verbs", "naib-al-fail", "al-majhul-fil-kafiya"], passive=True,
     doer=("، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ «عَنْهُ»", "; its deputy doer is the jarr phrase «of him»", "; nâib-i fâili «anhü» câr-mecrûrudur"),
     note=(" — وَأَصْلُهُ يُسْتَغْنَى", " — it is يُسْتَغْنَى", " — aslı «yüstağnâ»dır")),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)", extra=["naib-al-fail"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِـ«يُسْتَغْنَ»", note_en="; the phrase stands in the seat of raf' as the deputy doer of «is done without»", note_tr="; câr-mecrûr «müstağni kalınır»ın nâib-i fâili olarak mahallen merfû"),
  JV("وَيُذْمَمِ", "dhamma", "atf-jawab", "rawi", g=["atf-nasaq", "doubled-verbs", "naib-al-fail", "al-majhul-fil-kafiya"], passive=True, doer=NAIB_HUWA, pre=WA3,
     note=(" — وَأَظْهَرَ التَّضْعِيفَ عَلَى لُغَةِ أَهْلِ الْحِجَازِ: لُغَتُهُمْ فَكُّ الْإِدْغَامِ فِي الْجَزْمِ (الزَّوْزَنِيُّ)؛ وَيَجُوزُ فِي الْمَعْطُوفِ عَلَى الْجَوَابِ الرَّفْعُ وَالنَّصْبُ، وَلٰكِنَّ الْقَافِيَةَ بِالْجَزْمِ (الدُّرَّةُ)", " — he unmerges the doubled letter in the Ḥijāzī way: in jazm they say يُذْمَمْ, not يُذَمَّ (al-Zawzanī); a verb joined to the answer may also be read in raf' or nasb, but the rhyme needs the jazm (al-Durra)", " — Hicâz lügati üzere şeddeyi çözmüştür: onlar cezimde idgâmı fekkederler (Zevzenî); cevaba atfedilen fiilde ref ve nasb da caizdir, fakat kâfiye cezmi gerektirir (Dürre)"),
     segs=SG(("وَ", "wa", "conj"), ("يُذْمَمِ", "dhamma", "verb")))])
# ---- v. 52 ----
V(S5, "Whoever keeps faith is not blamed; and he whose heart is led to goodness that sets the heart at rest does not falter.",
  "Kim sözünde durursa yerilmez; kimin kalbi de gönlü yatıştıran bir iyiliğe yöneltilirse tereddüt etmez.",
 [MAN("وَمَنْ", D("يُوفِ", "ya"), D("يُذْمَمْ", "sukun")),
  JV("يُوفِ", "awfa", "shart", "ya", g=["form-iv-verbs", "naqis-verbs", "hadhf-al-maful"], note=(" — وَأَصْلُهُ يُوفِي؛ وَمُتَعَلَّقُهُ مَحْذُوفٌ أَيْ: بِعَهْدِهِ. وَفَيْتُ بِالْعَهْدِ وَأَوْفَيْتُ بِهِ لُغَتَانِ، وَالثَّانِيَةُ لُغَةُ الْقُرْآنِ (الزَّوْزَنِيُّ)", " — it is يُوفِي; what he keeps is left unsaid: «his covenant». وَفَى and أَوْفَى are both said, and the second is the Qurʾān's usage (al-Zawzanī)", " — aslı «yûfî»dir; neye vefa ettiği söylenmemiştir: «ahdine». «Vefâ» da «evfâ» da denir; ikincisi Kur'ân'ın lügatidir (Zevzenî)")),
  LA_SH(),
  JV("يُذْمَمْ", "dhamma", "jawab", "sukun", g=["doubled-verbs", "naib-al-fail", "al-majhul-fil-kafiya"], passive=True, doer=NAIB_HUWA,
     note=(" — بِفَكِّ الْإِدْغَامِ فِي الْجَزْمِ", " — the doubled letter is unmerged in jazm", " — cezimde idgâm çözülmüştür")),
  MAN("وَمَنْ", D("يُهْدَ", "alif"), D("يَتَجَمْجَمِ", "rawi")),
  JV("يُهْدَ", "hada", "shart", "alif", g=["naqis-verbs", "naib-al-fail", "al-majhul-fil-kafiya"], passive=True,
     doer=("، وَنَائِبُ الْفَاعِلِ «قَلْبُهُ» بَعْدَهُ", "; its deputy doer, «his heart», follows", "; nâib-i fâili sonraki «kalbi»dir"),
     note=(" — وَأَصْلُهُ يُهْدَى؛ وَيُرْوَى «يُفْضِ قَلْبُهُ» (الدُّرَّةُ)", " — it is يُهْدَى; also read يُفْضِ قَلْبُهُ «whose heart comes through to» (al-Durra)", " — aslı «yühdâ»dır; «yüfdi kalbühû» diye de rivayet edilir (Dürre)")),
  T("قَلْبُهُ", "qalb", "noun", ["naib-al-fail", "idafa-definiteness", "al-bariz-al-muttasil"],
     "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ الرَّابِطُ الْعَائِدُ عَلَى «مَنْ».",
     "The deputy doer, in raf'; annexed to the attached «his», in the seat of jarr — the pronoun that ties the clause back to مَنْ.",
     "Nâib-i fâil, merfû; bitişik zamire muzâf, zamir mahallen mecrûr — cümleyi «men»e bağlayan âid zamir odur.",
     segs=SG(("قَلْبُ", "qalb", "noun"), ("هُ", "pron-3ms", "pron")))],
 [PREP("إِلَى", "ila", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُهْدَ»", role_en="; the phrase hangs on «is led»", role_tr="; câr-mecrûr «yöneltilirse»ye müteallik", gloss_tr="«-e»"),
  MAJR("مُطْمَئِنِّ", "mutmainn", extra=["ism-fail", "idafa-definiteness"], note_ar="، مُضَافٌ — اسْمُ فَاعِلٍ مِنِ اطْمَأَنَّ، مِنْ إِضَافَةِ الصِّفَةِ إِلَى مَوْصُوفِهَا: إِلَى الْبِرِّ الْمُطْمَئِنِّ، أَيْ: بِرٍّ يَطْمَئِنُّ الْقَلْبُ إِلَى حُسْنِهِ وَيَسْكُنُ إِلَى وُقُوعِهِ مَوْقِعَهُ (الزَّوْزَنِيُّ)", note_en=", annexed — the active participle of اِطْمَأَنَّ, a quality annexed to the thing it describes: «goodness at rest», that is, a good deed in whose fairness and fitness the heart rests easy (al-Zawzanī)", note_tr=", muzâf — «itmeenne»den ism-i fâil; sıfatın mevsûfuna izâfeti: «mutmain iyilik», yani güzelliğine ve yerini bulduğuna kalbin yatıştığı iyilik (Zevzenî)"),
  MUDAF_ILAYH("الْبِرِّ", "birr", note_ar=" — وَالْبِرُّ: اسْمٌ جَامِعٌ لِخِصَالِ الْخَيْرِ", note_en=" — بِرّ gathers every kind of good", note_tr=" — «birr»: bütün hayır hasletlerini toplayan isim"),
  LA_SH(),
  JV("يَتَجَمْجَمِ", "tajamjama", "jawab", "rawi", note=(" — وَالتَّجَمْجُمُ: التَّرَدُّدُ وَالتَّتَعْتُعُ، أَيْ: لَمْ يَتَتَعْتَعْ فِي إِسْدَائِهِ وَإِيلَائِهِ (الزَّوْزَنِيُّ) — رُبَاعِيٌّ مَزِيدٌ بِالتَّاءِ عَلَى تَفَعْلَلَ", " — تَجَمْجُم is hanging back, stammering: «he does not stumble in doing and bestowing it» (al-Zawzanī) — a four-letter verb with the added ta, on تَفَعْلَلَ", " — «tecemcüm»: tereddüt etmek, kekelemek; yani «onu yapıp vermekte duraksamaz» (Zevzenî) — tâ ziyadesiyle rubâî mezîd, «tefa'lele» vezninde"))])
CH[5] = S5

# =====================================================================================================================
# Chapter 6 — الْحِكَمُ، الْقِسْمُ الثَّانِي (al-Zawzanī vv. 53–58)
# =====================================================================================================================
S6 = []
MADI_SH = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ", "Past verb built on fatha, standing in the seat of jazm as the condition's verb", "Fetha üzere mebnî mâzî; şart fiili olarak mahallen meczûm")
# ---- v. 53 ----
V(S6, "Whoever dreads the ways by which death comes — they reach him, though he climb the tracts of the sky by a ladder.",
  "Kim ölümün sebeplerinden korkarsa, onlar yine de ona erişir; merdivenle göğün kapılarına çıksa bile.",
 [MAN("وَمَنْ", ("«هَابَ» فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ", "«dreads», a past verb standing in the seat of jazm", "«korkarsa»; mâzî fiil, mahallen meczûm"),
      ("«يَنَلْنَهُ» مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ فِي مَحَلِّ جَزْمٍ", "«they reach him», built on sukun because the nun of the women is attached, in the seat of jazm", "«ona erişirler»; nûn-ı nisve bitiştiği için sükûn üzere mebnî, mahallen meczûm")),
  T("هَابَ", "haba-awe", "verb", G_SHART + ["hollow-verbs"],
     MADI_SH[0] + HUWA[0] + " — وَالْمَاضِي لَا يَظْهَرُ فِيهِ الْجَزْمُ فَيَكُونُ مَحَلِّيًّا؛ هَابَ: خَافَ.",
     MADI_SH[1] + HUWA[1] + " — jazm cannot show on a past verb, so it is a jazm of seat; هَابَ is «to fear».",
     MADI_SH[2] + HUWA[2] + " — mâzîde cezim zâhir olmaz, mahallî olur; «hâbe»: korktu."),
  MAFUL("أَسْبَابَ", "sabab", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ سَبَبٍ: مَا يُتَوَصَّلُ بِهِ إِلَى الشَّيْءِ", note_en=", annexed — the plural of سَبَب: whatever leads to a thing", note_tr=", muzâf — «sebeb»in cem'i: bir şeye ulaştıran vasıta"),
  MUDAF_ILAYH("الْمَنَايَا", "maniyya", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_en=" — by a kasra estimated on the alif", note_tr=" — elif üzerinde takdîrî kesre ile"),
  T("يَنَلْنَهُ", "nala", "verb", G_SHART + ["hollow-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ يَعُودُ عَلَى الْمَنَايَا، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى «مَنْ» — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (يَنَالُ ← يَنَلْنَ).",
     "Present verb built on sukun because the nun of the women is attached, standing in the seat of jazm as the answer of the condition; the nun (the Fates) is the doer, in the seat of raf', and the attached «him», returning to مَنْ, the object, in the seat of nasb — a hollow verb whose middle letter drops where two quiescents meet (يَنَالُ → يَنَلْنَ).",
     "Nûn-ı nisve bitiştiği için sükûn üzere mebnî muzâri; şartın cevabı olarak mahallen meczûm; ecellere dönen nûn fâil, mahallen merfû; «men»e dönen bitişik «ona» mef'ûlün bih, mahallen mansûb — ecvef fiil; iki sâkin karşılaştığı için aynü'l-fiili düşmüştür (yenâlü → yenelne).",
     segs=SG(("يَنَلْنَ", "nala", "verb"), ("هُ", "pron-3ms", "pron")))],
 [T("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza", "hal", "al-hal-jumla-wa-rabituha"],
     "الْوَاوُ حَالِيَّةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ — وَهِيَ الْوَصْلِيَّةُ الَّتِي يُؤْتَى بِهَا لِلْغَايَةِ — وَجَوَابُهَا مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ: وَإِنْ يَرْقَ … يَنَلْنَهُ؛ وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْهَاءِ فِي «يَنَلْنَهُ». وَهٰذَا قِيَاسٌ عَلَى إِعْرَابِ الدُّرَّةِ لِلرِّوَايَةِ الْأُخْرَى: «وَلَوْ رَامَ أَسْبَابَ السَّمَاءِ»، وَقَدْ ذَكَرَهَا الزَّوْزَنِيُّ.",
     "The waw opens a hal clause; إِنْ is the conditional particle of jazm — here the «linking» إِنْ that marks the farthest case, «even if» — and its answer is left out, shown by what goes before: «even if he climbs …, they reach him»; the clause is a hal of the «him» in «they reach him», in the seat of nasb. This follows al-Durra's parsing of the other reading, وَلَوْ رَامَ أَسْبَابَ السَّمَاءِ «though he sought the tracts of the sky», which al-Zawzanī also records.",
     "Vâv hâliyyedir; «in» cezmeden şart harfi — burada gayeyi bildiren vasliyye «in»: «…-se bile» — cevabı mahzûf olup öncesi ona delâlet eder: «çıksa bile … ona erişirler»; cümle «yenelnehû»daki «hû»dan hâl, mahallen mansûb. Bu i'râb, Dürre'nin öbür rivayeti — Zevzenî'nin de zikrettiği «ve lev râme esbâbe's-semâi» — i'râb edişine kıyasladır.",
     segs=SG(("وَ", "wa", "conj"), ("إِنْ", "in-shartiyya", "part"))),
  JV("يَرْقَ", "raqiya", "shart", "alif", g=["naqis-verbs", "in-shartiyya"], doer=HUWA,
     note=(" — وَهُوَ فِعْلُ شَرْطِ «إِنْ»، وَأَصْلُهُ يَرْقَى؛ رَقِيَ فِي السُّلَّمِ يَرْقَى: صَعِدَ فِيهِ (الزَّوْزَنِيُّ)", " — the condition of إِنْ; it is يَرْقَى: «he went up the ladder» (al-Zawzanī)", " — «in»in şart fiilidir; aslı «yerkâ»dır: «merdivene çıktı» (Zevzenî)")),
  MAFUL("أَسْبَابَ", "sabab", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — وَأَسْبَابُ السَّمَاءِ: نَوَاحِيهَا وَأَبْوَابُهَا الَّتِي يُتَوَصَّلُ بِهَا إِلَيْهَا", note_en=", annexed — the «ways» of the sky are its tracts and gates, by which it is reached", note_tr=", muzâf — göğün «sebepleri»: ona ulaştıran yanları ve kapıları"),
  MUDAF_ILAYH("السَّمَاءِ", "sama", extra=["ism-mamdud"]),
  BI_NOUN("بِسُلَّمِ", "sullam", "سُلَّمِ", extra=["al-qafiya"], note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَرْقَ»" + RAWI_J[0], note_en=" — the ba of means; the phrase hangs on «climb»" + RAWI_J[1], note_tr=" — bâ istiâne içindir; câr-mecrûr «çıksa»ya müteallik" + RAWI_J[2])])
# ---- v. 54 ----
V(S6, "Whoever bestows kindness on those unworthy of it — his praise turns to blame upon him, and he repents.",
  "Kim iyiliği ehli olmayana yaparsa, (beklediği) övgü kendi aleyhine yergi olur ve pişman olur.",
 [MAN("وَمَنْ", D("يَجْعَلِ", "kasr2"), D("يَكُنْ", "sukun")),
  JV("يَجْعَلِ", "jaala", "shart", "kasr2"),
  MAFUL("الْمَعْرُوفَ", "maruf", extra=["ism-maful"]),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَجْعَلِ»، وَيَجُوزُ تَعْلِيقُهُمَا بِمَحْذُوفٍ حَالٍ مِنَ «الْمَعْرُوفَ» (الدُّرَّةُ)", "; the jarr phrase hangs on «bestows» — or on an omitted hal of «kindness» (al-Durra)", " — câr-mecrûr «yaparsa»ya müteallik; «iyilik»in mahzûf hâline müteallik olması da caizdir (Dürre)")),
  MAJR("غَيْرِ", "ghayr", **W(MUD)),
  ENC_NOUN("أَهْلِهِ", "ahl", "هِ", "mudaf", note_ar=" — وَالضَّمِيرُ لِلْمَعْرُوفِ: أَيْ فِي مَنْ لَا يَسْتَحِقُّهُ", note_en=" — «its» is the kindness: on one who does not deserve it", note_tr=" — zamir iyiliğe döner: yani ona lâyık olmayana")],
 [KJ("يَكُنْ", "jawab", "sukun", ("، وَاسْمُهُ «حَمْدُهُ» بَعْدَهُ", "; its noun, «his praise», follows", "; ismi sonraki «övgüsü»dür"),
     note=(" — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (يَكُونُ ← يَكُنْ)", " — a hollow verb whose middle letter drops where two quiescents meet (يَكُونُ → يَكُنْ)", " — ecvef fiil; iki sâkin karşılaştığı için aynü'l-fiili düşmüştür (yekûnü → yekün)")),
  ENC_NOUN("حَمْدُهُ", "hamd", "هُ", "ismk", extra=["masdar", "tibaq"], note_ar=" — وَهُوَ اسْمُ «يَكُنْ»، وَفِي الْهَاءِ الرَّابِطُ الْعَائِدُ عَلَى «مَنْ»: أَيِ الْحَمْدُ الَّذِي يَرْجُوهُ يَصِيرُ ذَمًّا، ذَمَّهُ الَّذِي أُحْسِنَ إِلَيْهِ وَلَمْ يَحْمَدْهُ (الزَّوْزَنِيُّ). وَبَيْنَ «حَمْدُهُ» وَ«ذَمًّا» طِبَاقٌ", note_en=" — the noun of يَكُنْ; its pronoun ties the clause back to مَنْ: the praise he looks for turns to blame — «the one he was good to blames him and does not praise him» (al-Zawzanī). «Praise» and «blame» make a tibaq", note_tr=" — «yekün»ün ismidir; zamiri cümleyi «men»e bağlar: umduğu övgü yergiye döner — «iyilik ettiği kimse onu över değil, yerer» (Zevzenî). «Övgü» ile «yergi» arasında tıbâk vardır"),
  KHK("ذَمًّا", "dhamm", extra=["masdar", "tibaq"], note_ar=" — خَبَرُ «يَكُنْ»", note_en=" — the predicate of يَكُنْ", note_tr=" — «yekün»ün haberi"),
  JARR_PRON("عَلَيْهِ", "ala", "عَلَيْ", "هِ", " («onun aleyhine»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ذَمًّا»، أَوْ بِمَحْذُوفٍ نَعْتٍ لَهُ (الدُّرَّةُ)", note_en="; the phrase hangs on «blame», or on an omitted na't of it (al-Durra)", note_tr="; câr-mecrûr «yergi»ye yahut onun mahzûf na'tına müteallik (Dürre)"),
  JV("وَيَنْدَمِ", "nadima", "atf-jawab", "rawi", g=["atf-nasaq"], pre=WA3,
     note=(" — وَيَجُوزُ رَفْعُهُ وَنَصْبُهُ، وَلٰكِنَّ الْقَافِيَةَ بِالْجَزْمِ (الدُّرَّةُ)", " — raf' and nasb are also possible, but the rhyme needs the jazm (al-Durra)", " — ref ve nasbı da caizdir, fakat kâfiye cezmi gerektirir (Dürre)"),
     segs=SG(("وَ", "wa", "conj"), ("يَنْدَمِ", "nadima", "verb")))])
# ---- v. 55 ----
V(S6, "Whoever defies the butt-ends of the spears will surely obey their upper shafts, each fitted with a long blade.",
  "Kim mızrakların dip demirlerine (barış işaretine) baş kaldırırsa, her birine uzun temren takılmış mızrak uçlarına boyun eğer.",
 [MAN("وَمَنْ", D("يَعْصِ", "ya"),
      ("الْجُمْلَةُ الِاسْمِيَّةُ «فَإِنَّهُ يُطِيعُ الْعَوَالِي» الْمُقْتَرِنَةُ بِالْفَاءِ، فِي مَحَلِّ جَزْمٍ", "the nominal sentence «then he obeys the upper shafts», joined by the fa, in the seat of jazm", "fâ ile gelen «fe-innehû yutî'u'l-avâlî» isim cümlesi, mahallen meczûm")),
  JV("يَعْصِ", "asa", "shart", "ya", g=["naqis-verbs", "tibaq", "kinaya"],
     note=(" — وَأَصْلُهُ يَعْصِي. وَبَيْنَهُ وَبَيْنَ «يُطِيعُ» طِبَاقٌ. وَ«يَعْصِ أَطْرَافَ الزِّجَاجِ» كِنَايَةٌ عَنْ إِبَاءِ الصُّلْحِ: كَانَتِ الْفِئَتَانِ إِذَا الْتَقَتَا سَدَّدَتْ كُلُّ وَاحِدَةٍ زِجَاجَ الرِّمَاحِ نَحْوَ صَاحِبَتِهَا وَسَعَى السَّاعُونَ فِي الصُّلْحِ، فَإِنْ أَبَتَا قَلَبَتَا الرِّمَاحَ وَاقْتَتَلَتَا بِالْأَسِنَّةِ؛ وَتَحْرِيرُ الْمَعْنَى: مَنْ أَبَى الصُّلْحَ ذَلَّلَتْهُ الْحَرْبُ وَلَيَّنَتْهُ (الزَّوْزَنِيُّ)",
           " — it is يَعْصِي. With «obeys» it makes a tibaq. «He defies the butt-ends of the spears» is a kinaya for refusing peace: when two bands met, each held its spears butt-forward toward the other while the peacemakers went between; if they refused, they turned the spears and fought with the blades. The plain sense: whoever spurns peace, war humbles and softens him (al-Zawzanī)",
           " — aslı «ya'sî»dir. «İtaat eder» ile arasında tıbâk vardır. «Mızrakların dip demirlerine isyan eder» barışı reddetmekten kinâyedir: iki topluluk karşılaştığında her biri mızraklarının dip demirini ötekine doğrultur, arabulucular barış için çalışırdı; kabul etmezlerse mızrakları çevirip temrenlerle savaşırlardı. Mânânın özü: barışı reddedeni savaş zelil eder ve yumuşatır (Zevzenî)")),
  MAFUL("أَطْرَافَ", "taraf", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ طَرَفٍ", note_en=", annexed — the plural of «end»", note_tr=", muzâf — «taraf»ın cem'i"),
  MUDAF_ILAYH("الزِّجَاجِ", "zujj", extra=["jam-taksir"], note_ar=" — جَمْعُ زُجٍّ: الْحَدِيدَةُ الْمُرَكَّبَةُ فِي أَسْفَلِ الرُّمْحِ", note_en=" — the plural of زُجّ, the iron shoe at the foot of a spear", note_tr=" — «zücc»ün cem'i: mızrağın dibine takılan demir"),
  T("فَإِنَّهُ", "inna", "part", ["al-fa-fi-jawab-al-shart", "inna-wa-akhawatuha", "al-bariz-al-muttasil", "al-majzum-wal-shart-wal-jaza"],
     "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ — وَجَبَ اقْتِرَانُهُ بِهَا لِأَنَّهُ جُمْلَةٌ اسْمِيَّةٌ — وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا يَعُودُ عَلَى «مَنْ»؛ وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
     "The fa ties the answer to the condition — it must come, for the answer is a nominal sentence — and إِنَّ is the particle of emphasis that puts its noun in nasb; the attached «he», returning to مَنْ, is that noun; the nominal sentence stands in the seat of jazm as the answer of the condition.",
     "Fâ şartın cevabını bağlar — cevap isim cümlesi olduğu için gelmesi vâciptir — inne te'kîd ve nasb harfi; «men»e dönen bitişik zamir ismidir, mahallen mansûb; isim cümlesi şartın cevabı olarak mahallen meczûm.",
     segs=SG(("فَ", "fa", "conj"), ("إِنَّ", "inna", "part"), ("هُ", "pron-3ms", "pron")))],
 [T("يُطِيعُ", "ataa", "verb", ["mudari-marfu", "form-iv-verbs", "hollow-verbs", "anwa-al-khabar", "tibaq", "kinaya"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ. وَبَيْنَهُ وَبَيْنَ «يَعْصِ» طِبَاقٌ، وَ«يُطِيعُ الْعَوَالِيَ» كِنَايَةٌ عَنِ الْخُضُوعِ لِلْحَرْبِ. وَيُرْوَى «مُطِيعُ الْعَوَالِي» بِالْإِضَافَةِ (الدُّرَّةُ).",
     "Present verb in raf'; the doer is the hidden «he» — the clause is the predicate of إِنَّ, in the seat of raf'. With «defies» it makes a tibaq; and «he obeys the upper shafts» is a kinaya for being bent by war. Also read مُطِيعُ الْعَوَالِي, as an idafa (al-Durra).",
     "Merfû muzâri; fâil gizli zamir «o» — cümle inne'nin haberi, mahallen merfû. «İsyan eder» ile arasında tıbâk vardır; «mızrak uçlarına itaat eder» savaşa boyun eğmekten kinâyedir. İzâfetle «mutî'u'l-avâlî» diye de rivayet edilir (Dürre)."),
  T("الْعَوَالِي", "aliya", "noun", ["maful-bihi", "ism-maqsur-manqus", "jam-taksir", "kinaya"],
     "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — وَكَانَ حَقُّهُ أَنْ يَقُولَ «الْعَوَالِيَ» بِفَتْحِ الْيَاءِ، وَلٰكِنَّهُ سَكَّنَهَا لِإِقَامَةِ الْوَزْنِ ضَرُورَةً، وَحَمَلَ النَّصْبَ عَلَى الرَّفْعِ وَالْجَرِّ (الزَّوْزَنِيُّ). جَمْعُ عَالِيَةٍ: أَعْلَى الرُّمْحِ مِمَّا يَلِي السِّنَانَ، ضِدُّ سَافِلَتِهِ.",
     "The direct object, in nasb by a fatha estimated on the ya — by rule he should say الْعَوَالِيَ, with fatha on the ya, but he stills it to keep the metre, a poet's licence, treating nasb like raf' and jarr (al-Zawzanī). The plural of عَالِيَة: the upper part of the spear, next to the blade, the opposite of its foot.",
     "Mef'ûlün bih; yâ üzerinde takdîrî fetha ile mansûb — kaideye göre yâ'nın fethasıyla «el-avâliye» demesi gerekirdi; fakat vezni tutturmak için zarûreten yâ'yı sâkin kılmış, nasbı ref ve cerre hamletmiştir (Zevzenî). «Âliye»nin cem'i: mızrağın temrene yakın üst kısmı; dibinin zıddı."),
  T("رُكِّبَتْ", "rakkaba", "verb", ["form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya", "mafulayn", "jumla-sifa"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْعَوَالِي — وَهُوَ الْمَفْعُولُ الْأَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«الْعَوَالِي» عَلَى أَنَّ «أَلْ» فِيهَا لِلْجِنْسِ، أَوْ حَالٌ مِنْهَا عَلَى أَنَّهَا لِلتَّعْرِيفِ (الدُّرَّةُ).",
     "A past verb in the passive, built on fatha; the ta marks the feminine; its deputy doer is the hidden «they» (the upper shafts) — the first object — and the clause is a na't of «the upper shafts», in the seat of nasb, if the article names the kind; or a hal of them, if it makes them definite (al-Durra).",
     "Fetha üzere mebnî meçhul mâzî; tâ te'nîs içindir; nâib-i fâil mızrak uçlarına dönen gizli zamir — birinci mef'ûl odur — cümle, «el» cins için sayılırsa «avâlî»nin na'tı, ta'rîf için sayılırsa ondan hâl olarak mahallen mansûb (Dürre)."),
  MAFUL("كُلَّ", "kull", extra=["mafulayn", "idafa-definiteness"], note_ar="، مُضَافٌ — وَهُوَ الْمَفْعُولُ الثَّانِي لِـ«رُكِّبَتْ»", note_en=", annexed — the second object of «were fitted»", note_tr=", muzâf — «takıldı»nın ikinci mef'ûlü"),
  MUDAF_ILAYH("لَهْذَمِ", "lahdham", extra=["al-qafiya"], note_ar=" — وَهُوَ السِّنَانُ الطَّوِيلُ (الزَّوْزَنِيُّ)، وَقِيلَ: الْحَادُّ (الدُّرَّةُ)" + RAWI_J[0], note_en=" — the long spear-blade (al-Zawzanī); others say the sharp one (al-Durra)" + RAWI_J[1], note_tr=" — uzun mızrak temreni (Zevzenî); keskin temren de denmiştir (Dürre)" + RAWI_J[2])])
# ---- v. 56 ----
V(S6, "Whoever does not drive men from his cistern with his weapons has it torn down; and whoever does not wrong people is wronged.",
  "Kim silahıyla havuzunu (harîmini) savunmazsa havuzu yıkılır; kim de insanlara zulmetmezse zulme uğrar.",
 [MAN("وَمَنْ", LAM_SH("يَذُدْ", "drive off", "savunmazsa"), D("يُهَدَّمْ", "sukun")),
  LAM_JAZM("لَمْ"),
  T("يَذُدْ", "dhada", "verb", G_SHART + ["lam-jazim", "hollow-verbs", "hadhf-al-maful"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + HUWA[0] + "، وَالْمَفْعُولُ مَحْذُوفٌ أَيْ: أَعْدَاءَهُ — وَ«لَمْ» وَمَا دَخَلَتْ عَلَيْهِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ. أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ (يَذُودُ ← يَذُدْ)؛ وَالذَّوْدُ: الْكَفُّ وَالرَّدْعُ.",
     "Present verb in jazm by لَمْ, its sign the sukun" + HUWA[1] + "; its object — «his enemies» — is left out — لَمْ with its verb stands in the seat of jazm as the condition's verb. A hollow verb whose middle letter drops where two quiescents meet (يَذُودُ → يَذُدْ); ذَوْد is holding back and driving off.",
     "Lem ile meczûm muzâri, alâmeti sükûn" + HUWA[2] + "; mef'ûlü — «düşmanlarını» — mahzûf — «lem» ve fiili şart fiili olarak mahallen meczûm. Ecvef fiil; iki sâkin karşılaştığı için aynü'l-fiili düşmüştür (yezûdü → yezüd); «zevd»: engellemek, geri püskürtmek."),
  PREP("عَنْ", "an", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَذُدْ»", role_en="; the phrase hangs on «drive off»", role_tr="; câr-mecrûr «savunmazsa»ya müteallik", gloss_tr="«-den»"),
  ENC_NOUN("حَوْضِهِ", "hawd", "هِ", "majr", extra=["istiara", "arkan-al-istiara"], note_ar=". وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتَعَارَ الْحَوْضَ لِلْحَرِيمِ، أَيْ: مَنْ لَمْ يَحْمِ حَرِيمَهُ اسْتُبِيحَ (الزَّوْزَنِيُّ)؛ وَقِيلَ: هُوَ كِنَايَةٌ عَمَّا يَجِبُ عَلَى الْإِنْسَانِ حِفْظُهُ مِنْ نَفْسٍ وَعِرْضٍ وَمَالٍ (الدُّرَّةُ)", note_en=". Here is an isti'ara tasrihiyya: he lends «cistern» to a man's inviolable ground — «whoever does not defend what is his to guard has it overrun» (al-Zawzanī); others call it a kinaya for what a man must guard: life, honour and wealth (al-Durra)", note_tr=". Burada istiâre-i tasrîhiyye vardır: «havuz» harîm (korunması gereken şey) için ödünç alınmıştır — «harîmini korumayanın harîmi çiğnenir» (Zevzenî); bir görüşe göre insanın koruması gereken can, ırz ve maldan kinâyedir (Dürre)"),
  BI_NOUN("بِسِلَاحِهِ", "silah", "سِلَاحِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَذُدْ» أَيْضًا", note_en=" — the ba of means; this phrase too hangs on «drive off»", note_tr=" — bâ istiâne içindir; bu câr-mecrûr da «savunmazsa»ya müteallik")],
 [JV("يُهَدَّمْ", "haddama", "jawab", "sukun", g=["form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya"], passive=True,
     doer=("، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْحَوْضِ", "; its deputy doer is the hidden «it» — the cistern", "; nâib-i fâil havuza dönen gizli zamir «o»"),
     note=(" — وَالرَّابِطُ بِـ«مَنْ» مُقَدَّرٌ: يُهَدَّمْ حَوْضُهُ", " — the tie to مَنْ is understood: «his cistern is torn down»", " — «men»e bağlayan zamir mukadderdir: «havuzu yıkılır»")),
  MAN("وَمَنْ", D("يَظْلِمِ", "kasr2"), D("يُظْلَمِ", "rawi")),
  LA_SH(),
  JV("يَظْلِمِ", "zalama", "shart", "kasr2", g=["mulhaq-bil-jinas"], note=(" — وَبَيْنَهُ وَبَيْنَ «يُظْلَمِ» اشْتِقَاقٌ: الْأَوَّلُ مَبْنِيٌّ لِلْمَعْلُومِ وَالثَّانِي لِلْمَجْهُولِ", " — it shares a root with يُظْلَمِ: the first is active, the second passive", " — «yuzlem» ile arasında iştikâk vardır: ilki ma'lûm, ikincisi meçhuldür")),
  MAFUL("النَّاسَ", "nas"),
  JV("يُظْلَمِ", "zalama", "jawab", "rawi", g=["naib-al-fail", "al-majhul-fil-kafiya", "mulhaq-bil-jinas"], passive=True, doer=NAIB_HUWA,
     note=(" — أَيْ: مَنْ كَفَّ عَنْ ظُلْمِ النَّاسِ ظَلَمَهُ النَّاسُ (الزَّوْزَنِيُّ)", " — «whoever holds back from wronging people, people wrong him» (al-Zawzanī)", " — yani «insanlara zulmetmekten el çekene insanlar zulmeder» (Zevzenî)"))])
# ---- v. 57 ----
V(S6, "Whoever goes abroad takes an enemy for his friend; and whoever does not honour himself is not honoured.",
  "Kim gurbete çıkarsa düşmanı dostu sanır; kim de kendine değer vermezse ona değer verilmez.",
 [MAN("وَمَنْ", D("يَغْتَرِبْ", "sukun"), D("يَحْسِبْ", "sukun")),
  JV("يَغْتَرِبْ", "ightaraba", "shart", "sukun", g=["form-viii-verbs"], note=(" — وَالِاغْتِرَابُ: الْبُعْدُ عَنِ الْأَهْلِ وَالْوَطَنِ", " — اِغْتِرَاب is to be far from one's people and home", " — «iğtirâb»: ehlinden ve vatanından uzak düşmek")),
  JV("يَحْسِبْ", "hasiba", "jawab", "sukun", g=["mafulayn", "al-mutaaddi-wa-afal-al-qulub"], note=(" — مِنْ أَفْعَالِ الْقُلُوبِ يَنْصِبُ مَفْعُولَيْنِ؛ وَسِينُهُ تُكْسَرُ وَتُفْتَحُ (وَالْكَسْرُ ضَبْطُ الْمَطْبُوعِ)", " — a verb of the heart, with two objects; its sin is read with kasra or fatha (the kasra is the edition's)", " — ef'âl-i kulûbdandır, iki mef'ûl alır; sîn'i kesreli de fethalı da okunur (kesre baskının harekesidir)")),
  MAFUL("عَدُوًّا", "aduww", extra=["mafulayn", "tibaq"], note_ar=" — الْمَفْعُولُ الْأَوَّلُ. وَبَيْنَ «عَدُوًّا» وَ«صَدِيقَهُ» طِبَاقٌ", note_en=" — the first object. «Enemy» and «friend» make a tibaq", note_tr=" — birinci mef'ûl. «Düşman» ile «dost» arasında tıbâk vardır"),
  ENC_NOUN("صَدِيقَهُ", "sadiq-friend", "هُ", "maful", extra=["mafulayn", "tibaq"], note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي: أَيْ يَحْسِبُ الْأَعْدَاءَ أَصْدِقَاءَ لِأَنَّهُ لَمْ يُجَرِّبْهُمْ (الزَّوْزَنِيُّ)", note_en=" — the second object: he takes enemies for friends, not having tried them (al-Zawzanī)", note_tr=" — ikinci mef'ûl: onları denemediği için düşmanları dost sanar (Zevzenî)")],
 [MAN("وَمَنْ", LAM_SH("يُكَرِّمْ", "honour", "değer vermezse"),
      ("«يُكَرَّمِ» مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + "، وَ«لَمْ يُكَرَّمِ» فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ",
       "«is honoured», in jazm by لَمْ, its sign " + SGN["rawi"][1] + " — and لَمْ يُكَرَّمِ stands in the seat of jazm as the answer",
       "«değer verilmez»; lem ile meczûm, alâmeti " + SGN["rawi"][2] + " — «lem yükerrami» şartın cevabı olarak mahallen meczûm")),
  LAM_JAZM("لَمْ"),
  T("يُكَرِّمْ", "karrama", "verb", G_SHART + ["lam-jazim", "form-ii-verbs", "mulhaq-bil-jinas"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + HUWA[0] + " — وَ«لَمْ» وَمَا دَخَلَتْ عَلَيْهِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ. وَبَيْنَهُ وَبَيْنَ «يُكَرَّمِ» اشْتِقَاقٌ: الْأَوَّلُ مَبْنِيٌّ لِلْمَعْلُومِ وَالثَّانِي لِلْمَجْهُولِ.",
     "Present verb in jazm by لَمْ, its sign the sukun" + HUWA[1] + " — لَمْ with its verb stands in the seat of jazm as the condition's verb. It shares a root with يُكَرَّمِ: the first is active, the second passive.",
     "Lem ile meczûm muzâri, alâmeti sükûn" + HUWA[2] + " — «lem» ve fiili şart fiili olarak mahallen meczûm. «Yükerram» ile arasında iştikâk vardır: ilki ma'lûm, ikincisi meçhuldür."),
  ENC_NOUN("نَفْسَهُ", "nafs", "هُ", "maful", note_ar=" — أَيْ: بِتَجَنُّبِ الدَّنَايَا (الزَّوْزَنِيُّ)", note_en=" — that is, by keeping clear of base things (al-Zawzanī)", note_tr=" — yani bayağı işlerden sakınarak (Zevzenî)"),
  LAM_JAZM("لَمْ"),
  T("يُكَرَّمِ", "karrama", "verb", G_SHART + ["lam-jazim", "form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya", "al-qafiya", "mulhaq-bil-jinas"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + NAIB_HUWA[0] + " — وَ«لَمْ» وَمَا دَخَلَتْ عَلَيْهِ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
     "A present verb in the passive, in jazm by لَمْ, its sign " + SGN["rawi"][1] + NAIB_HUWA[1] + " — لَمْ with its verb stands in the seat of jazm as the answer of the condition.",
     "Lem ile meczûm meçhul muzâri, alâmeti " + SGN["rawi"][2] + NAIB_HUWA[2] + " — «lem» ve fiili şartın cevabı olarak mahallen meczûm.")])
# ---- v. 58 ----
V(S6, "And whatever trait a man may have — though he think it hidden from people — it comes to be known.",
  "Bir kimsede hangi huy bulunursa bulunsun — o bunu insanlardan gizli kalır sansa da — mutlaka bilinir.",
 [T("وَمَهْمَا", "mahma", "pron", G_SHART + ["mubtada-khabar", "al-mabni-wal-mudmar", "anwa-al-waw"],
     WA_ISTINAF[0] + "مَهْمَا اسْمُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — فِعْلُ الشَّرْطِ: «تَكُنْ» مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ؛ وَجَوَابُهُ: «تُعْلَمِ» مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + "؛ وَجُمْلَتَا الشَّرْطِ وَالْجَوَابِ خَبَرُهُ. وَأَجَازَ الْبَصْرِيُّونَ أَنْ يَكُونَ خَبَرًا مُقَدَّمًا لِـ«تَكُنْ» فِي مَحَلِّ نَصْبٍ، وَ«مِنْ» زَائِدَةً وَ«خَلِيقَةٍ» اسْمَهَا (الدُّرَّةُ).",
     WA_ISTINAF[1] + "مَهْمَا «whatever» is a conditional noun that puts two verbs in jazm, built on sukun in the seat of raf' as mubtada — the condition's verb: «may be», in jazm, its sign the sukun; its answer: «is known», in jazm, its sign " + SGN["rawi"][1] + "; the condition and its answer together are its khabar. The Basrans also allow it to be the fronted predicate of تَكُنْ, in the seat of nasb, with مِنْ added and «trait» as the noun of تَكُنْ (al-Durra).",
     WA_ISTINAF[2] + "mehmâ «her ne …-se»: iki fiili cezmeden şart ismi, sükûn üzere mebnî, mübtedâ olarak mahallen merfû — şart fiili: «olursa», meczûm, alâmeti sükûn; cevabı: «bilinir», meczûm, alâmeti " + SGN["rawi"][2] + "; şart ve cevap cümleleri haberidir. Basralılar onun «tekün»ün öne alınmış haberi olarak mahallen mansûb, «min»in zâid ve «halîka»nın ismi olmasını da caiz görmüşlerdir (Dürre).",
     segs=SG(("وَ", "wa", "conj"), ("مَهْمَا", "mahma", "pron"))),
  KJ("تَكُنْ", "shart", "sukun", ("، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «مَهْمَا» — وَأُنِّثَ لِأَنَّهَا مُفَسَّرَةٌ بِالْخَلِيقَةِ", "; its noun is the hidden «she», returning to مَهْمَا — feminine because مَهْمَا is explained by «trait»", "; ismi «mehmâ»ya dönen gizli zamir «o» — «mehmâ» «halîka» ile açıklandığı için müennes gelmiştir")),
  ZARF("عِنْدَ", "inda", note_ar=" — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «تَكُنْ»", note_en=", hanging on the omitted predicate of تَكُنْ", note_tr="; «tekün»ün mahzûf haberine müteallik"),
  MUDAF_ILAYH("امْرِئٍ", "imru", note_ar=" — وَعَيْنُهُ تَتْبَعُ لَامَهُ فِي الْحَرَكَةِ: امْرُؤٌ، امْرَأً، امْرِئٍ", note_en=" — its middle vowel follows its ending: امْرُؤٌ، امْرَأً، امْرِئٍ", note_tr=" — orta harfinin harekesi son harfinkine uyar: امْرُؤٌ، امْرَأً، امْرِئٍ"),
  MIN(role=(" — وَمِنْ بَيَانِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «مَهْمَا» عَلَى رَأْيِ سِيبَوَيْهِ، أَوْ مِنْ ضَمِيرِهَا الْمُسْتَتِرِ فِي «تَكُنْ» عِنْدَ الْجُمْهُورِ (الدُّرَّةُ)", "; مِنْ explains, and the phrase hangs on an omitted hal of مَهْمَا, on Sībawayh's view — or of its pronoun hidden in تَكُنْ, on the majority's (al-Durra)", " — «min» beyâniyyedir; câr-mecrûr Sîbeveyh'e göre «mehmâ»nın, cumhura göre onun «tekün»deki gizli zamirinin mahzûf hâline müteallik (Dürre)")),
  MAJR("خَلِيقَةٍ", "khalaiq", note_ar=" — وَالْخَلِيقَةُ وَالْخُلُقُ وَاحِدٌ", note_en=" — خَلِيقَة and خُلُق are one: a trait of character", note_tr=" — «halîka» ile «hulk» aynıdır: huy")],
 [T("وَإِنْ", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza", "itirad", "jumla-mutarida"],
     "الْوَاوُ اعْتِرَاضِيَّةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ، وَجَوَابُهُ مَحْذُوفٌ لِدَلَالَةِ جَوَابِ «مَهْمَا» عَلَيْهِ — وَ«إِنْ» وَمَا دَخَلَتْ عَلَيْهِ كَلَامٌ مُعْتَرِضٌ بَيْنَ فِعْلِ شَرْطِ «مَهْمَا» وَجَوَابِهِ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ؛ وَقِيلَ: «إِنْ» وَصْلِيَّةٌ وَالْوَاوُ حَالِيَّةٌ (الدُّرَّةُ). وَالِاعْتِرَاضُ مِنَ الْإِطْنَابِ: يَدْفَعُ تَوَهُّمَ أَنَّ الْكِتْمَانَ يَنْفَعُ.",
     "The waw opens a parenthesis; إِنْ is the conditional particle of jazm, and its answer is left out, the answer of مَهْمَا standing for it — إِنْ and its clause are a parenthesis between the condition of مَهْمَا and its answer, with no seat of their own; others read إِنْ as the «linking» one and the waw as opening a hal (al-Durra). The parenthesis is one of the kinds of itnab: it heads off the thought that hiding helps.",
     "Vâv i'tirâziyyedir; «in» cezmeden şart harfi, cevabı «mehmâ»nın cevabı ona delâlet ettiği için mahzûf — «in» ve cümlesi, «mehmâ»nın şart fiili ile cevabı arasında mu'tarıza olup i'râbdan mahalli yoktur; bir görüşe göre «in» vasliyye, vâv hâliyyedir (Dürre). İ'tirâz ıtnâb çeşitlerindendir: gizlemenin fayda vereceği vehmini giderir.",
     segs=SG(("وَ", "wa", "conj"), ("إِنْ", "in-shartiyya", "part"))),
  T("خَالَهَا", "khala-think", "verb", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza", "hollow-verbs", "mafulayn", "al-mutaaddi-wa-afal-al-qulub", "al-bariz-al-muttasil"],
     MADI_SH[0] + "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «امْرِئٍ»، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ يَعُودُ عَلَى الْخَلِيقَةِ — وَخَالَ مِنْ أَفْعَالِ الْقُلُوبِ بِمَعْنَى ظَنَّ.",
     MADI_SH[1] + "; the doer is the hidden «he» (the man), and the attached «it» (the trait) is the first object, in the seat of nasb — خَالَ is a verb of the heart: «to suppose».",
     MADI_SH[2] + "; fâil «kişi»ye dönen gizli zamir «o»; huya dönen bitişik «onu» birinci mef'ûl, mahallen mansûb — «hâle» ef'âl-i kulûbdandır: «zannetti».",
     segs=SG(("خَالَ", "khala-think", "verb"), ("هَا", "pron-3fs", "pron"))),
  T("تَخْفَى", "khafiya", "verb", ["mudari-marfu", "naqis-verbs", "mafulayn"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْخَلِيقَةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ لِـ«خَالَ».",
     "Present verb in raf' by a damma estimated on the alif; the doer is the hidden «she» (the trait) — the clause is the second object of خَالَ, in the seat of nasb.",
     "Elif üzerinde takdîrî damme ile merfû muzâri; fâil huya dönen gizli zamir «o» — cümle «hâle»nin ikinci mef'ûlü, mahallen mansûb."),
  PREP("عَلَى", "ala", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَخْفَى»", role_en="; the phrase hangs on «is hidden»", role_tr="; câr-mecrûr «gizli kalır»a müteallik", gloss_tr="«-e»"),
  MAJR("النَّاسِ", "nas"),
  JV("تُعْلَمِ", "alima", "jawab", "rawi", g=["naib-al-fail", "al-majhul-fil-kafiya"], passive=True,
     doer=("، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْخَلِيقَةِ", "; its deputy doer is the hidden «she» — the trait", "; nâib-i fâil huya dönen gizli zamir «o»"),
     note=(" — وَهُوَ جَوَابُ «مَهْمَا»", " — the answer of مَهْمَا", " — «mehmâ»nın cevabıdır"))])
CH[6] = S6

# =====================================================================================================================
# The poem is kept WHOLE (owner's ruling): every verse of al-Zawzanī's recension, in his order. The verses written first
# (S2..S6) and those added later (EXTRA, through VV) are filed by verse number; the chapters are cut from that sequence.
EXTRA = {}
def VV(n, en, tr, first, second):
    tmp = []
    V(tmp, en, tr, first, second)
    assert n not in EXTRA, n
    EXTRA[n] = tmp[0]

# ---- helpers for the verses added when the poem was made whole ----
def MT(ar, en, tr):
    """«وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ…» — tr carries its own case ending"""
    return (" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«" + ar + "»", "; the phrase hangs on «" + en + "»", "; câr-mecrûr «" + tr + " müteallik")
def NUN_M(full, lex, g=None, note=("", "", ""), pre=None, segs=None, p=None):
    """a past verb with the nun of the women: بَكَرْنَ، وَضَعْنَ"""
    pre = pre or ("", "", "")
    return T(full, lex, "verb", ["al-bariz-al-muttasil", "fail"] + (g or []),
        pre[0] + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + note[0] + ".",
        cap(pre[1] + "past verb built on sukun because the nun of the women is attached; that nun is the doer, in the seat of raf'" + note[1] + "."),
        cap(pre[2] + "nûn-ı nisve bitiştiği için sükûn üzere mebnî mâzî; nûn fâildir, mahallen merfû" + note[2] + "."), p=p, segs=segs)
MAWSUF = lambda ar, en, tr: (" — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: " + ar, " — a quality whose noun is left out: " + en, " — mevsûfu hazfedilmiş sıfat: " + tr)

# =====================================================================================================================
# vv. 7–15 — الظَّعَائِنُ
# =====================================================================================================================
VV(7, "Look well, my friend: do you see any women borne in litters, who have set out over the high ground above Jurthum?",
  "İyi bak dostum: Cürsüm suyunun üstündeki yüksek arazide yola koyulmuş, hevdeçlerde giden kadınlar görüyor musun?",
 [T("تَبَصَّرْ", "tabassara", "verb", ["imperative-amr", "form-v-verbs", "al-fail-al-mudmar-al-mustatir-wujuban", "ijaz-al-hadhf"],
     "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ، أَوْ مَقُولُ قَوْلٍ مَحْذُوفٍ (الدُّرَّةُ)، وَعَلَيْهِ الزَّوْزَنِيُّ: فَقُلْتُ لِخَلِيلِي: انْظُرْ؛ فَفِيهِ إِيجَازٌ بِحَذْفِ الْقَوْلِ. وَالتَّبَصُّرُ: النَّظَرُ.",
     "Imperative built on sukun; the doer «you» must stay hidden — a new sentence, or what was said after an omitted «I said» (al-Durra); so al-Zawzanī: «and I said to my friend: Look» — brevity by dropping the verb of saying. تَبَصُّر is looking closely.",
     "Sükûn üzere mebnî emir; fâil vücûben gizli «sen» — cümle müste'nefedir yahut mahzûf bir «dedim»in mekûlüdür (Dürre); Zevzenî de böyle açıklar: «dostuma dedim ki: bak» — kavlin hazfiyle îcâz vardır. «Tebassur»: dikkatle bakmak."),
  T("خَلِيلِي", "khalil", "noun", ["vocative-munada", "idafa-definiteness", "ya-al-mutakallim", "al-bariz-al-muttasil"],
     "مُنَادًى بِحَرْفِ نِدَاءٍ مَحْذُوفٍ، مُضَافٌ، مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "The one called, with the calling particle left out; annexed, and so in nasb — by a fatha estimated on the letter before the ya of the speaker, which the kasra that suits the ya keeps from showing; the ya is the second term of the idafa, in the seat of jarr.",
     "Nidâ harfi hazfedilmiş münâdâ; muzâf olduğu için mansûb — mütekellim yâ'sından önceki harf üzerinde takdîrî fetha ile; münasebet kesresi fethanın zuhûruna engeldir; yâ muzâfun ileyh, mahallen mecrûr.",
     segs=SG(("خَلِيلِ", "khalil", "noun"), ("ي", "pron-1s", "pron"))),
  T("هَلْ", "hal-istifham", "part", ["al-istifham"], "حَرْفُ اسْتِفْهَامٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.", "The particle of question; it has no seat.", "İstifhâm harfi; i'râbdan mahalli yoktur."),
  T("تَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs", "al-fail-al-mudmar-al-mustatir-wujuban", "khuruj-al-istifham"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولُ «تَبَصَّرْ» الْمُعَلَّقِ عَنِ الْعَمَلِ بِالِاسْتِفْهَامِ (الدُّرَّةُ). وَالِاسْتِفْهَامُ لَيْسَ عَلَى حَقِيقَتِهِ: بَرَّحَ بِهِ الْوَجْدُ حَتَّى ظَنَّ الْمُحَالَ، لِأَنَّ كَوْنَهُنَّ بِحَيْثُ يَرَاهُنَّ خَلِيلُهُ بَعْدَ عِشْرِينَ سَنَةً مُحَالٌ (الزَّوْزَنِيُّ).",
     "Present verb in raf' by a damma estimated on the alif; the doer «you» must stay hidden — the clause is the object of «look», which the question keeps from governing in wording (al-Durra). The question is not a real one: longing has so wrung him that he fancies the impossible — for his friend to see the women after twenty years cannot be (al-Zawzanī).",
     "Elif üzerinde takdîrî damme ile merfû muzâri; fâil vücûben gizli «sen» — cümle, istifhâm sebebiyle lafzen amelden ta'lîk edilmiş «bak»ın mef'ûlüdür, mahallen mansûb (Dürre). İstifhâm hakiki değildir: özlem onu öyle sarsmıştır ki muhali zanneder; çünkü kadınların yirmi yıl sonra dostunun görebileceği yerde olması muhaldir (Zevzenî)."),
  T("مِنْ", "min", "prep", ["huruf-al-ziyada-fil-kafiya", "huruf-jarr"],
     "حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ الْعُمُومِ بَعْدَ الِاسْتِفْهَامِ؛ وَقِيلَ: أَصْلِيٌّ، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ الْمَفْعُولِ بِهِ (الدُّرَّةُ).",
     "An added jarr letter, strengthening «any» after the question; others take it as a true jarr letter, the phrase standing where the object stands (al-Durra).",
     "İstifhâmdan sonra umumu te'kîd eden zâid cer harfi; bir görüşe göre aslîdir ve câr-mecrûr mef'ûl yerindedir (Dürre)."),
  T("ظَعَائِنٍ", "zaina", "noun", ["maful-bihi", "jam-taksir", "mamnu-min-sarf"],
     "مَفْعُولٌ بِهِ لِـ«تَرَى» مَجْرُورٌ لَفْظًا بِـ«مِنْ» الزَّائِدَةِ مَنْصُوبٌ مَحَلًّا — جَمْعُ ظَعِينَةٍ: الْمَرْأَةُ فِي الْهَوْدَجِ، سُمِّيَتْ بِهِ لِأَنَّهَا تَظْعَنُ مَعَ زَوْجِهَا. وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ لِصِيغَةِ مُنْتَهَى الْجُمُوعِ، وَصُرِفَ لِضَرُورَةِ الشِّعْرِ (الدُّرَّةُ).",
     "The object of «see» — in jarr in wording, by the added مِنْ, in nasb in its seat — the plural of ظَعِينَة, a woman in her litter, so called because she travels with her husband. By rule a «farthest plural» takes no tanwin; it is declined in full here by poetic licence (al-Durra).",
     "«Görüyor musun»un mef'ûlü — zâid «min» ile lafzen mecrûr, mahallen mansûb — «zaîne»nin cem'i: hevdeçteki kadın; kocasıyla göç ettiği için böyle adlandırılmıştır. Muntehe'l-cumû' vezninde olduğu için gayr-i munsarif olması gerekirken şiir zarûretiyle tenvinlenmiştir (Dürre).")],
 [NUN_M("تَحَمَّلْنَ", "tahammala", g=["form-v-verbs", "jumla-sifa"], note=(" — وَالْجُمْلَةُ نَعْتٌ لِـ«ظَعَائِنٍ»؛ وَالتَّحَمُّلُ: التَّرَحُّلُ", " — the clause is a na't of «women in litters»; تَحَمُّل is loading up and moving off", " — cümle «zaâin»in na'tıdır; «tehammül»: yükü yükleyip göç etmek")),
  BI_NOUN("بِالْعَلْيَاءِ", "alya", "الْعَلْيَاءِ", extra=["ism-mamdud", "ijaz-al-hadhf"], note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَحَمَّلْنَ»؛ أَيْ بِالْأَرْضِ الْعَلْيَاءِ الْمُرْتَفِعَةِ، فَحُذِفَ الْمَوْصُوفُ (الزَّوْزَنِيُّ)", note_en=" — the ba means «in», and the phrase hangs on «set out»; «the high [ground]», with the noun described left out (al-Zawzanī)", note_tr=" — bâ «-de» anlamındadır; câr-mecrûr «yola koyulmuş»a müteallik; yani «yüksek [arazi]de», mevsûf hazfedilmiştir (Zevzenî)"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«الْعَلْيَاءِ» أَوْ حَالٍ مِنْهَا (الدُّرَّةُ)", "; the jarr phrase hangs on an omitted na't of «the high ground», or a hal of it (al-Durra)", " — câr-mecrûr «yüksek arazi»nin mahzûf na'tına yahut hâline müteallik (Dürre)")),
  MAJR("فَوْقِ", "fawqa", **W(MUD)),
  MUDAF_ILAYH("جُرْثُمِ", "jurthum", "propn", ["al-qafiya"], note_ar=" — مَاءٌ بِعَيْنِهِ" + RAWI_J[0], note_en=" — the name of a watering-place" + RAWI_J[1], note_tr=" — belirli bir suyun adı" + RAWI_J[2])])
# ---- v. 8 ----
VV(8, "They kept al-Qanān and its rough ground on their right — and how many there are at al-Qanān, of those under no bond and those under a sacred one!",
  "Kanân dağını ve onun sert arazisini sağlarına aldılar — Kanân'da nice hürmeti olmayan ve hürmeti olan kimse vardır!",
 [NUN_M("جَعَلْنَ", "jaala", g=["mafulayn", "jumla-sifa"], note=(" — يَعُودُ عَلَى الظَّعَائِنِ فِي الْبَيْتِ قَبْلَهُ، وَالْجُمْلَةُ نَعْتٌ ثَانٍ لِـ«ظَعَائِنٍ»، وَيَجُوزُ الِاسْتِئْنَافُ (الدُّرَّةُ)", " — it returns to the women of the verse before; the clause is a second na't of «women in litters», or a fresh start (al-Durra)", " — önceki beyitteki kadınlara döner; cümle «zaâin»in ikinci na'tıdır, isti'nâf da caizdir (Dürre)")),
  MAFUL("الْقَنَانَ", "qanan", "propn", ["mafulayn"], note_ar=" — الْمَفْعُولُ الْأَوَّلُ؛ جَبَلٌ لِبَنِي أَسَدٍ", note_en=" — the first object; a mountain of the Banū Asad", note_tr=" — birinci mef'ûl; Benî Esed'e ait bir dağ"),
  PREP("عَنْ", "an", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَعَلْنَ» فِي مَحَلِّ الْمَفْعُولِ الثَّانِي", role_en="; the phrase hangs on «kept» and stands where the second object stands", role_tr="; câr-mecrûr «aldılar»a müteallik, ikinci mef'ûl yerindedir", gloss_tr="«-den»"),
  MAJR("يَمِينٍ", "yamin", note_ar=" — أَيْ عَنْ يَمِينِهِنَّ", note_en=" — «on [their] right»", note_tr=" — yani «sağlarında»"),
  T("وَحَزْنَهُ", "hazn", "noun", ["atf-nasaq", "idafa-definiteness", "al-bariz-al-muttasil"],
     WA_AR + "حَزْنَ مَعْطُوفٌ عَلَى «الْقَنَانَ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْحَزْنُ: مَا غَلُظَ مِنَ الْأَرْضِ.",
     "The waw conjoins; «rough ground» is joined to «al-Qanān», in nasb; it is annexed to the attached «its», in the seat of jarr — حَزْن is hard, rugged land.",
     "«ve» + «sert arazisi»: «Kanân»a ma'tûf, mansûb; bitişik zamire muzâf, zamir mahallen mecrûr — «hazn»: sert, engebeli arazi.",
     segs=SG(("وَ", "wa", "conj"), ("حَزْنَ", "hazn", "noun"), ("هُ", "pron-3ms", "pron")))],
 [T("وَكَمْ", "kam", "pron", ["al-kinayat-wal-zuruf-al-mabniyya", "mubtada-khabar", "al-mabni-wal-mudmar", "anwa-al-waw"],
     WA_ISTINAF[0] + "كَمْ خَبَرِيَّةٌ بِمَعْنَى «كَثِيرٍ»، مَبْنِيَّةٌ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
     WA_ISTINAF[1] + "كَمْ here states — «many a» — and is built on sukun in the seat of raf' as mubtada.",
     WA_ISTINAF[2] + "«kem» haberiyyedir, «nice» anlamındadır; sükûn üzere mebnî, mübtedâ olarak mahallen merfû.",
     segs=SG(("وَ", "wa", "conj"), ("كَمْ", "kam", "pron"))),
  BI_NOUN("بِالْقَنَانِ", "qanan", "الْقَنَانِ", pos="propn", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «كَمْ»", note_en=" — the ba means «in»; the phrase hangs on the omitted khabar of كَمْ", note_tr=" — bâ «-de» anlamındadır; câr-mecrûr «kem»in mahzûf haberine müteallik"),
  T("مِنْ", "min", "prep", ["huruf-jarr", "al-kinayat-wal-zuruf-al-mabniyya"], "حَرْفُ جَرٍّ يَجُرُّ تَمْيِيزَ «كَمْ» الْخَبَرِيَّةِ إِذَا فُصِلَ بَيْنَهُمَا؛ وَعَدَّهُ الدُّرَّةُ زَائِدًا.", "A jarr letter: it takes the tamyiz of كَمْ when the two are parted; al-Durra counts it as added.", "Araya fasıla girdiğinde haberî «kem»in temyîzini cerreden cer harfi; Dürre onu zâid sayar."),
  T("مُحِلٍّ", "muhill", "noun", ["tamyiz", "ism-fail", "tibaq"],
     "تَمْيِيزُ «كَمْ» مَجْرُورٌ بِـ«مِنْ» — اسْمُ فَاعِلٍ مِنْ أَحَلَّ. قَالَ الْأَصْمَعِيُّ: مِنْ مُحِلٍّ وَمُحْرِمٍ: مَنْ لَا حُرْمَةَ لَهُ وَمَنْ لَهُ حُرْمَةٌ؛ وَقَالَ غَيْرُهُ: مَنْ دَخَلَ فِي أَشْهُرِ الْحِلِّ وَمَنْ دَخَلَ فِي أَشْهُرِ الْحُرُمِ (الزَّوْزَنِيُّ). وَبَيْنَ «مُحِلٍّ» وَ«مُحْرِمِ» طِبَاقٌ.",
     "The tamyiz of كَمْ, in jarr by مِنْ — the active participle of أَحَلَّ. Al-Aṣmaʿī: «one who has no sacred bond and one who has»; others: «one who has entered the free months and one who has entered the sacred months» (al-Zawzanī). The two words make a tibaq.",
     "«Kem»in temyîzi, «min» ile mecrûr — «ehalle»den ism-i fâil. Asmaî: «hürmeti olmayan ve hürmeti olan»; başkaları: «hill aylarına giren ve haram aylara giren» demiştir (Zevzenî). İki kelime arasında tıbâk vardır."),
  ATF("وَمُحْرِمِ", "muhrim", case="jarr", extra=["ism-fail", "tibaq", "al-qafiya"], **W(RAWI_J))])
# ---- v. 9 ----
VV(9, "They had spread fine figured cloths and a thin veil over the litters — red at the borders, the colour of blood.",
  "Hevdeçlerin üzerine değerli örtüler ve ince bir perde atmışlardı — kenarları kırmızı, renkleri kana benzer.",
 [NUN_M("عَلَوْنَ", "ala-rise", g=["naqis-verbs"], note=(" — وَالْوَاوُ لَامُ الْفِعْلِ. وَالْبَاءُ بَعْدَهُ لِلتَّعْدِيَةِ: أَيْ أَعْلَيْنَ أَنْمَاطًا، أَلْقَيْنَهَا عَلَى الْهَوَادِجِ وَغَشَّيْنَهَا بِهَا؛ وَيُرْوَى «وَعَالَيْنَ أَنْمَاطًا» (الزَّوْزَنِيُّ)", " — the waw is the verb's own last radical. The ba after it makes it transitive: «they raised cloths», threw them over the litters and covered them; also read وَعَالَيْنَ أَنْمَاطًا (al-Zawzanī)", " — vâv fiilin lâmıdır. Sonraki bâ ta'diye içindir: «örtüleri yukarı kaldırdılar», yani hevdeçlerin üzerine atıp onları örttüler; «ve âleyne enmâtan» diye de rivayet edilir (Zevzenî)")),
  BI_NOUN("بِأَنْمَاطٍ", "namat", "أَنْمَاطٍ", extra=["jam-taksir"], note_ar=" — وَالْبَاءُ لِلتَّعْدِيَةِ؛ جَمْعُ نَمَطٍ: مَا يُبْسَطُ مِنْ صُنُوفِ الثِّيَابِ. وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَلَوْنَ»", note_en=" — the ba of transitivity; the plural of نَمَط, a cloth that is spread out. The phrase hangs on «raised»", note_tr=" — bâ ta'diye içindir; «nemat»ın cem'i: serilen kumaş türlerinden biri. Câr-mecrûr «kaldırdılar»a müteallik"),
  NAAT("عِتَاقٍ", "atiq-noble", "jarr", extra=["jam-taksir"], note_ar=" — جَمْعُ عَتِيقٍ: الْكَرِيمُ", note_en=" — the plural of عَتِيق «noble, choice»", note_tr=" — «atîk»in cem'i: değerli, seçkin"),
  ATF("وَكِلَّةٍ", "killa", case="jarr", note_ar=" — عُطِفَ عَلَى «أَنْمَاطٍ»؛ وَالْكِلَّةُ: السِّتْرُ الرَّقِيقُ", note_en=" — joined to «cloths»; a كِلَّة is a thin veil or curtain", note_tr=" — «örtüler»e atfedilmiştir; «kille»: ince perde")],
 [NAAT("وِرَادٍ", "ward-red", "jarr", extra=["jam-taksir", "sifa-mushabbaha"], note_ar=" — نَعْتٌ سَبَبِيٌّ لِمَا تَقَدَّمَ؛ جَمْعُ وَرْدٍ وَهُوَ الْأَحْمَرُ، وَجَازَ الْوَصْفُ بِهِ وَهُوَ جَمْعٌ لِأَنَّهُ عَلَى لَفْظِ الْوَاحِدِ كَكِتَابٍ (الدُّرَّةُ)", note_en=" — a na't of what goes before, by way of what belongs to it; the plural of وَرْد «red», and it can describe though a plural, being shaped like a singular such as كِتَاب (al-Durra)", note_tr=" — öncekilerin sebebî na'tı; «verd»in («kırmızı») cem'i; cemi olduğu halde sıfat olabilmesi, «kitâb» gibi müfred lafzında olmasındandır (Dürre)"),
  T("حَوَاشِيهَا", "hashiya", "noun", ["fail", "jam-taksir", "ism-maqsur-manqus", "idafa-definiteness", "al-bariz-al-muttasil"],
     "فَاعِلٌ لِلصِّفَةِ «وِرَادٍ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ حَاشِيَةٍ: أَيْ حُمْرِ الْحَوَاشِي.",
     "The doer of the adjective «red», in raf' by a damma estimated on the ya; annexed to the attached «their», in the seat of jarr — the plural of حَاشِيَة «border»: «red-bordered».",
     "«Kırmızı» sıfatının fâili; yâ üzerinde takdîrî damme ile merfû; bitişik zamire muzâf, zamir mahallen mecrûr — «hâşiye»nin («kenar») cem'i: «kenarları kırmızı».",
     segs=SG(("حَوَاشِي", "hashiya", "noun"), ("هَا", "pron-3fs", "pron"))),
  T("مُشَاكِهَةِ", "mushakih", "noun", ["naat-sifa", "ism-fail", "idafa-definiteness", "tashbih", "aqsam-al-tashbih"],
     "نَعْتٌ آخَرُ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ إِلَى مَفْعُولِهِ — اسْمُ فَاعِلٍ مِنْ شَاكَهَ: شَابَهَ. وَيَحْتَمِلُ الرَّفْعَ خَبَرًا لِـ«حَوَاشِيهَا»، وَلَمْ يُشْكَلْ آخِرُهُ فِي الْمَطْبُوعِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ تِلْكَ الثِّيَابُ فِي أَلْوَانِهَا، وَالْمُشَبَّهُ بِهِ الدَّمُ، وَالْأَدَاةُ لَفْظُ «مُشَاكِهَةِ»، وَوَجْهُ الشَّبَهِ شِدَّةُ الْحُمْرَةِ وَلَمْ يُصَرَّحْ بِهِ (الزَّوْزَنِيُّ: يُشْبِهُ أَلْوَانُهَا الدَّمَ فِي شِدَّةِ الْحُمْرَةِ).",
     "A further na't, in jarr, annexed to its object — the active participle of شَاكَهَ «to resemble». It could also be read in raf', as the khabar of «their borders»; the edition leaves its ending bare. Here is a tashbih mursal mujmal: the thing likened is those cloths in their colour; the thing they are likened to, blood; the tool is the word «resembling»; the point of likeness — deep redness — is not stated (al-Zawzanī: «their colours are like blood in the depth of their red»).",
     "Bir başka na't, mecrûr, mef'ûlüne muzâf — «şâkehe»den («benzedi») ism-i fâil. «Kenarları»nın haberi olarak merfû okunması da mümkündür; baskıda son harfi harekesizdir. Burada mürsel mücmel bir teşbîh vardır: müşebbeh renkleri bakımından o örtüler; müşebbehün bih kan; edat «müşâkihe» lafzı; vech-i şebeh — koyu kırmızılık — açıkça söylenmemiştir (Zevzenî: «renkleri kırmızılığın şiddetinde kana benzer»)."),
  MUDAF_ILAYH("الدَّمِ", "dam", extra=["al-qafiya"], **W(RAWI_AL))])
# ---- v. 10 ----
VV(10, "They rode sideways on their mounts in al-Sūbān, climbing its ridge, with the airs of one who lives soft and makes much of it.",
  "Sûbân'da bineklerinin sağrılarına yan oturup onun sırtına tırmandılar; üzerlerinde refah içinde yaşayıp nazlanan kimsenin edası vardı.",
 [NUN_M("وَوَرَّكْنَ", "warraka", g=["form-ii-verbs", "atf-nasaq"], pre=WA3, segs=SG(("وَ", "wa", "conj"), ("وَرَّكْنَ", "warraka", "verb")),
     note=(" — وَالتَّوْرِيكُ: رُكُوبُ أَوْرَاكِ الدَّوَابِّ", " — تَوْرِيك is riding on the haunches of the beasts", " — «tevrîk»: bineklerin sağrısına binmek")),
  FI(role=MT("وَرَّكْنَ", "they rode", "bindiler»e")),
  MAJR("السُّوبَانِ", "suban", "propn", note_ar=" — اسْمُ عَلَمٍ لِأَرْضٍ مُرْتَفِعَةٍ", note_en=" — the proper name of a stretch of high ground", note_tr=" — yüksek bir arazinin özel adı"),
  T("يَعْلُونَ", "ala-rise", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail", "hal", "al-hal-jumla-wa-rabituha"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ — وَالْوَاوُ لَامُ الْفِعْلِ — وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ نُونِ «وَرَّكْنَ».",
     "Present verb built on sukun because the nun of the women is attached — the waw is the verb's own last radical — and that nun is the doer; the clause is a hal of the nun of «they rode», in the seat of nasb.",
     "Nûn-ı nisve bitiştiği için sükûn üzere mebnî muzâri — vâv fiilin lâmıdır — nûn fâildir; cümle «bindiler»deki nûndan hâl, mahallen mansûb."),
  ENC_NOUN("مَتْنَهُ", "matn", "هُ", "maful", note_ar=" — وَالضَّمِيرُ لِلسُّوبَانِ؛ وَالْمَتْنُ: مَا ارْتَفَعَ وَصَلُبَ مِنَ الْأَرْضِ", note_en=" — «its» is al-Sūbān; مَتْن is the raised, hard back of a land", note_tr=" — zamir Sûbân'a döner; «metn»: arazinin yükselmiş sert sırtı")],
 [T("عَلَيْهِنَّ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "taqdim-al-musnad", "hal", "al-hal-jumla-wa-rabituha"],
     "حَرْفُ جَرٍّ، وَهُنَّ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ ثَانِيَةٌ مِنْ فَاعِلِ «وَرَّكْنَ».",
     "A jarr letter; the attached «them» fills the seat of jarr — the phrase hangs on the omitted, fronted khabar, and the nominal clause is a second hal of the doer of «they rode», in the seat of nasb.",
     "Cer harfi; bitişik «hünne» mahallen mecrûr — câr-mecrûr öne alınmış mahzûf habere müteallik; isim cümlesi «bindiler»in fâilinden ikinci hâl, mahallen mansûb.",
     segs=SG(("عَلَيْ", "ala", "prep"), ("هِنَّ", "pron-3fp", "pron"))),
  MUBTADA("دَلُّ", "dall-coquetry", extra=["idafa-definiteness"], note_ar="، مُضَافٌ — مُبْتَدَأٌ مُؤَخَّرٌ؛ وَالدَّلُّ وَالدَّلَالُ وَاحِدٌ", note_en=", annexed — placed after its khabar; دَلّ and دَلَال are one: a woman's winning airs", note_tr=", muzâf — haberinden sonraya bırakılmıştır; «dell» ile «delâl» aynıdır: naz, eda"),
  MUDAF_ILAYH("النَّاعِمِ", "naim-soft", extra=["ism-fail", "ijaz-al-hadhf"], **W(MAWSUF("الْإِنْسَانِ النَّاعِمِ، أَيِ الطَّيِّبِ الْعَيْشِ (الزَّوْزَنِيُّ)", "«the [person] who lives in ease» (al-Zawzanī)", "«refah içinde yaşayan [kimse]» (Zevzenî)"))),
  T("الْمُتَنَعِّمِ", "mutanaim", "noun", ["naat-sifa", "ism-fail", "al-qafiya", "mulhaq-bil-jinas"],
     "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنْ تَنَعَّمَ: تَكَلَّفَ النَّعْمَةَ؛ وَبَيْنَهُ وَبَيْنَ «النَّاعِمِ» اشْتِقَاقٌ" + RAWI_AL[0] + ".",
     "A second na't of the omitted noun, in jarr — the active participle of تَنَعَّمَ, to make a show of soft living; it shares a root with النَّاعِمِ" + RAWI_AL[1] + ".",
     "Mahzûf mevsûfun ikinci na'tı, mecrûr — «tena''ame»den ism-i fâil: refahı tekellüfle göstermek; «en-nâim» ile arasında iştikâk vardır" + RAWI_AL[2] + ".")])
# ---- v. 11 ----
VV(11, "They set out at first light and were on the road before dawn; and they and the valley of al-Rass are as the hand is to the mouth.",
  "Sabah erkenden yola çıktılar, seher vaktinde yürüdüler; onlar ile Ress vadisi, elin ağza gidişi gibidir (şaşmadan oraya varırlar).",
 [NUN_M("بَكَرْنَ", "bakara", note=(" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ بَكَرَ: سَارَ بُكْرَةً", " — a new sentence; بَكَرَ is to set out in the early morning", " — cümle müste'nefedir; «bekera»: sabah erkenden yola çıktı")),
  T("بُكُورًا", "bukur", "noun", ["maful-mutlaq", "masdar"], "مَفْعُولٌ مُطْلَقٌ مُؤَكِّدٌ لِعَامِلِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "A maf'ul mutlaq that strengthens its verb, in nasb.", "Âmilini te'kîd eden mef'ûl-i mutlak, mansûb."),
  NUN_M("وَاسْتَحَرْنَ", "istahara", g=["form-x-verbs", "atf-nasaq", "mulhaq-bil-jinas"], pre=WA3, segs=SG(("وَ", "wa", "conj"), ("اسْتَحَرْنَ", "istahara", "verb")),
     note=(" — اسْتَحَرَ: سَارَ سَحَرًا؛ وَبَيْنَهُ وَبَيْنَ «بِسُحْرَةٍ» اشْتِقَاقٌ مُلْحَقٌ بِالْجِنَاسِ", " — اِسْتَحَرَ is to travel in the last of the night; it shares a root with «before dawn» — the derivation that is attached to jinas", " — «istehara»: seher vakti yürüdü; «bi-suhratin» ile arasında cinâsa mülhak iştikâk vardır")),
  BI_NOUN("بِسُحْرَةٍ", "suhra", "سُحْرَةٍ", extra=["mulhaq-bil-jinas"], note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَسُحْرَةٌ اسْمٌ لِلسَّحَرِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اسْتَحَرْنَ»", note_en=" — the ba means «in», and سُحْرَة is a name for the hour before dawn; the phrase hangs on «were on the road»", note_tr=" — bâ «-de» anlamındadır; «suhra» seher vaktinin adıdır; câr-mecrûr «yürüdüler»e müteallik")],
 [T("فَهُنَّ", "hunna", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar", "atf-nasaq"],
     FA_AR + "هُنَّ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The fa conjoins; «they» is a detached pronoun built on fatha, in the seat of raf' as mubtada.", "«fe» + «onlar»: fetha üzere mebnî munfasıl zamir; mübtedâ olarak mahallen merfû.",
     segs=SG(("فَ", "fa", "conj"), ("هُنَّ", "hunna", "pron"))),
  T("وَوَادِي", "wadi-valley", "noun", ["atf-nasaq", "ism-maqsur-manqus", "idafa-definiteness"],
     WA_AR + "وَادِي مَعْطُوفٌ عَلَى الضَّمِيرِ «هُنَّ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ.",
     "The waw conjoins; «valley» is joined to the pronoun «they», in raf' by a damma estimated on the ya, and annexed.",
     "«ve» + «vadi»: «onlar» zamirine ma'tûf; yâ üzerinde takdîrî damme ile merfû, muzâf.",
     segs=SG(("وَ", "wa", "conj"), ("وَادِي", "wadi-valley", "noun"))),
  MUDAF_ILAYH("الرَّسِّ", "rass", "propn", note_ar=" — وَادِي الرَّسِّ: وَادٍ بِعَيْنِهِ", note_en=" — Wādī al-Rass is a particular valley", note_tr=" — Vâdi'r-Ress belirli bir vadidir"),
  T("كَالْيَدِ", "ka", "prep", ["huruf-jarr", "tashbih", "aqsam-al-tashbih", "mubtada-khabar"],
     "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَالْيَدِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الظَّعَائِنُ فِي قَصْدِهِنَّ وَادِيَ الرَّسِّ، وَالْمُشَبَّهُ بِهِ الْيَدُ الْقَاصِدَةُ لِلْفَمِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ إِصَابَةُ الْمَقْصِدِ مِنْ غَيْرِ خَطَإٍ (الزَّوْزَنِيُّ: قَاصِدَاتٌ لِوَادِي الرَّسِّ لَا يُخْطِئْنَهُ كَالْيَدِ الْقَاصِدَةِ لِلْفَمِ لَا تُخْطِئُهُ).",
     "The kaf is a jarr letter of likening; «the hand» is in jarr — the phrase hangs on the omitted khabar of the mubtada. Here is a tashbih mursal mujmal: the thing likened is the women making for Wādī al-Rass; the thing they are likened to, the hand going to the mouth; the tool is the kaf; the point of likeness is left unsaid — reaching the mark without a miss (al-Zawzanī: «they make for Wādī al-Rass and do not miss it, as the hand that makes for the mouth does not miss it»).",
     "Kâf cer ve teşbîh harfi; «el» mecrûr — câr-mecrûr mübtedânın mahzûf haberine müteallik. Burada mürsel mücmel bir teşbîh vardır: müşebbeh Ress vadisine yönelen kadınlar; müşebbehün bih ağza yönelen el; edat kâf; vech-i şebeh hazfedilmiştir — hedefi şaşmadan bulmak (Zevzenî: «Ress vadisine yönelirler ve onu şaşırmazlar; ağza yönelen elin onu şaşırmaması gibi»).",
     segs=SG(("كَ", "ka", "prep"), ("الْيَدِ", "yad", "noun"))),
  T("لِلْفَمِ", "li", "prep", ["huruf-jarr", "al-qafiya"],
     "اللَّامُ حَرْفُ جَرٍّ، وَالْفَمِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «الْيَدِ»: أَيْ قَاصِدَةً لِلْفَمِ" + RAWI_AL[0] + "؛ وَيُرْوَى «فِي الْفَمِ» (الدُّرَّةُ).",
     "The lam is a jarr letter; «the mouth» is in jarr — the phrase hangs on an omitted hal of «the hand»: «making for the mouth»" + RAWI_AL[1] + "; also read فِي الْفَمِ (al-Durra).",
     "Lâm cer harfi; «ağız» mecrûr — câr-mecrûr «el»in mahzûf hâline müteallik: «ağza yönelmiş olarak»" + RAWI_AL[2] + "; «fi'l-fem» diye de rivayet edilir (Dürre).",
     segs=SG(("لِ", "li", "prep"), ("الْفَمِ", "fam", "noun")))])
# ---- v. 12 ----
VV(12, "In them there is delight for the man of fine taste, and a sight that charms the eye of one who looks with discernment.",
  "Onlarda zarif kimse için bir eğlence ve dikkatle bakan gözün hoşuna giden bir manzara vardır.",
 [T("وَفِيهِنَّ", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "taqdim-al-musnad", "anwa-al-waw"],
     WA_ISTINAF[0] + "فِي حَرْفُ جَرٍّ، وَهُنَّ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
     WA_ISTINAF[1] + "فِي is a jarr letter, and the attached «them» fills the seat of jarr — the phrase hangs on the omitted, fronted khabar.",
     WA_ISTINAF[2] + "«fî» cer harfi; bitişik «hünne» mahallen mecrûr — câr-mecrûr öne alınmış mahzûf habere müteallik.",
     segs=SG(("وَ", "wa", "conj"), ("فِي", "fi", "prep"), ("هِنَّ", "pron-3fp", "pron"))),
  MUBTADA("مَلْهًى", "malha", extra=["ism-maqsur-manqus"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لَفْظًا لِالْتِقَاءِ السَّاكِنَيْنِ", note_ar=" — مُبْتَدَأٌ مُؤَخَّرٌ؛ وَالْمَلْهَى: اللَّهْوُ وَمَوْضِعُهُ", note_en=" — by a damma estimated on the alif, which drops in sound before the tanwin; placed after its khabar; مَلْهًى is amusement, or a place for it", note_tr=" — tenvinden önce telaffuzda düşen elif üzerinde takdîrî damme ile; haberinden sonraya bırakılmıştır; «melhâ»: eğlence yahut eğlence yeri"),
  T("لِلَّطِيفِ", "li", "prep", ["huruf-jarr", "ijaz-al-hadhf"],
     "اللَّامُ حَرْفُ جَرٍّ، وَاللَّطِيفِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَلْهًى» أَوْ بِمَحْذُوفٍ نَعْتٍ لَهُ (الدُّرَّةُ)؛ وَاللَّطِيفُ: الْمُتَأَنِّقُ الْحَسَنُ الْمَنْظَرِ، صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ.",
     "The lam is a jarr letter; «the refined» is in jarr — the phrase hangs on «delight», or on an omitted na't of it (al-Durra); the لَطِيف is the man of nice taste and fair looks, a quality whose noun is left out.",
     "Lâm cer harfi; «zarif» mecrûr — câr-mecrûr «eğlence»ye yahut onun mahzûf na'tına müteallik (Dürre); «latîf»: ince zevkli, güzel görünüşlü kimse; mevsûfu hazfedilmiş sıfattır.",
     segs=SG(("لِ", "li", "prep"), ("اللَّطِيفِ", "latif", "noun"))),
  ATF("وَمَنْظَرٌ", "manzar", note_ar=" — عُطِفَ عَلَى «مَلْهًى»", note_en=" — joined to «delight»", note_tr=" — «eğlence»ye atfedilmiştir")],
 [NAAT("أَنِيقٌ", "aniq", "raf", extra=["sifa-mushabbaha"], note_ar=" — فَعِيلٌ بِمَعْنَى مُفْعِلٍ: الْمُعْجِبُ، كَالْحَكِيمِ بِمَعْنَى الْمُحْكِمِ (الزَّوْزَنِيُّ)", note_en=" — a فَعِيل in the sense of مُفْعِل: «charming, pleasing», as حَكِيم is for مُحْكِم (al-Zawzanī)", note_tr=" — «müf'il» anlamında faîl: «hoşa giden»; «hakîm»in «muhkim» anlamına gelmesi gibi (Zevzenî)"),
  T("لِعَيْنِ", "li", "prep", ["huruf-jarr", "idafa-definiteness"],
     "اللَّامُ حَرْفُ جَرٍّ، وَعَيْنِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَنِيقٌ».",
     "The lam is a jarr letter; «eye» is in jarr and annexed — the phrase hangs on «charming».",
     "Lâm cer harfi; «göz» mecrûr, muzâf — câr-mecrûr «hoşa giden»e müteallik.",
     segs=SG(("لِ", "li", "prep"), ("عَيْنِ", "ayn-eye", "noun"))),
  MUDAF_ILAYH("النَّاظِرِ", "nazir-looking", extra=["ism-fail", "ijaz-al-hadhf"], **W(MAWSUF("الرَّجُلِ النَّاظِرِ", "«the [man] who looks»", "«bakan [adam]»"))),
  T("الْمُتَوَسِّمِ", "mutawassim", "noun", ["naat-sifa", "ism-fail", "al-qafiya"],
     "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنْ تَوَسَّمَ: تَفَرَّسَ وَتَتَبَّعَ مَحَاسِنَ الشَّيْءِ" + RAWI_AL[0] + ".",
     "A second na't of the omitted noun, in jarr — the active participle of تَوَسَّمَ, to read a thing closely, tracing its beauties" + RAWI_AL[1] + ".",
     "Mahzûf mevsûfun ikinci na'tı, mecrûr — «tevesseme»den ism-i fâil: bir şeyin güzelliklerini dikkatle süzmek, ferasetle bakmak" + RAWI_AL[2] + ".")])
# ---- v. 13 ----
VV(13, "The tufts of dyed wool, at every place where they halted, are like nightshade berries not yet crushed.",
  "Konakladıkları her yerde (hevdeçlerden dökülen) boyalı yün parçaları, ezilmemiş it üzümü taneleri gibidir.",
 [T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "aqsam-al-tashbih"],
     "حَرْفُ تَشْبِيهٍ وَنَصْبٍ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ فُتَاتُ الْعِهْنِ، وَالْمُشَبَّهُ بِهِ حَبُّ الْفَنَا قَبْلَ حَطْمِهِ، وَالْأَدَاةُ «كَأَنَّ»، وَوَجْهُ الشَّبَهِ الْحُمْرَةُ وَلَمْ يُذْكَرْ؛ وَقَيَّدَ الْمُشَبَّهَ بِهِ بِـ«لَمْ يُحَطَّمِ» لِأَنَّهُ إِذَا حُطِّمَ زَايَلَهُ لَوْنُهُ (الزَّوْزَنِيُّ).",
     "«As if»: the particle of likening that puts its noun in nasb. Here is a tashbih mursal mujmal: the thing likened is the tufts of dyed wool; the thing they are likened to, nightshade berries before they are crushed; the tool is كَأَنَّ; the point of likeness, redness, is not stated; and the berries are tied to «not crushed» because once crushed they lose their colour (al-Zawzanī).",
     "«Sanki»: teşbîh ve nasb harfi. Burada mürsel mücmel bir teşbîh vardır: müşebbeh boyalı yün parçaları; müşebbehün bih ezilmeden önceki it üzümü taneleri; edat «keenne»; vech-i şebeh olan kırmızılık zikredilmemiştir; müşebbehün bih «ezilmemiş» kaydıyla kayıtlanmıştır, çünkü ezilince rengi gider (Zevzenî)."),
  T("فُتَاتَ", "futat", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"],
     "اسْمُ كَأَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالْفُتَاتُ: مَا انْفَتَّ مِنَ الشَّيْءِ أَيْ تَقَطَّعَ وَتَفَرَّقَ.",
     "The noun of كَأَنَّ, in nasb, annexed — فُتَات is what has crumbled off a thing, its scattered bits.",
     "Keenne'nin ismi, mansûb, muzâf — «fütât»: bir şeyden kopup dağılan parçalar."),
  MUDAF_ILAYH("الْعِهْنِ", "ihn", note_ar=" — الصُّوفُ الْمَصْبُوغُ", note_en=" — dyed wool", note_tr=" — boyalı yün"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «فُتَاتَ الْعِهْنِ»", "; the jarr phrase hangs on an omitted hal of «the tufts of wool»", " — câr-mecrûr «yün parçaları»nın mahzûf hâline müteallik")),
  MAJR("كُلِّ", "kull", **W(MUD)),
  MUDAF_ILAYH("مَنْزِلٍ", "manzil")],
 [NUN_M("نَزَلْنَ", "nazala", g=["jumla-sifa"], note=(" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«مَنْزِلٍ»", " — the clause is a na't of «halting-place», in the seat of jarr", " — cümle «konak»ın na'tı, mahallen mecrûr")),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («orada»)", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالضَّمِيرُ هُوَ الرَّابِطُ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَزَلْنَ»", note_en="; the ba means «in», and the pronoun ties the clause to «halting-place»; the phrase hangs on «halted»", note_tr="; bâ «-de» anlamındadır; zamir cümleyi «konak»a bağlar; câr-mecrûr «konakladılar»a müteallik"),
  T("حَبُّ", "habb-grain", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "tashbih"],
     "خَبَرُ كَأَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَهُوَ الْمُشَبَّهُ بِهِ.", "The predicate of كَأَنَّ, in raf', annexed — the thing the tufts are likened to.", "Keenne'nin haberi, merfû, muzâf — müşebbehün bihtir."),
  MUDAF_ILAYH("الْفَنَا", "fana-berry", extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=" — عِنَبُ الثَّعْلَبِ", note_en=" — by a kasra estimated on the alif; «fox-grape», black nightshade, whose berries are red", note_tr=" — elif üzerinde takdîrî kesre ile; it üzümü; taneleri kırmızıdır"),
  LAM_JAZM("لَمْ"),
  T("يُحَطَّمِ", "hattama", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya", "al-qafiya", "hal", "al-hal-jumla-wa-rabituha"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + "، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «حَبُّ الْفَنَا» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ (الدُّرَّةُ).",
     "A present verb in the passive, in jazm by لَمْ, its sign " + SGN["rawi"][1] + "; its deputy doer is the hidden «it» — the berries — and the clause is a hal of them, in the seat of nasb (al-Durra).",
     "Lem ile meczûm meçhul muzâri, alâmeti " + SGN["rawi"][2] + "; nâib-i fâil «it üzümü taneleri»ne dönen gizli zamir — cümle ondan hâl, mahallen mansûb (Dürre).")])
# ---- v. 14 ----
VV(14, "And when they came down to the water, its gathered pools clear and blue, they laid down their staffs like one who settles and pitches his tent.",
  "Birikmiş suları masmavi, dupduru olan suya vardıklarında, çadır kurup yerleşen kimse gibi asâlarını bıraktılar (konakladılar).",
 [LAMMA2("فَلَمَّا"),
  NUN_M("وَرَدْنَ", "warada", g=["mithal-verbs"], note=LAMMA_CL),
  MAFUL("الْمَاءَ", "ma-water"),
  T("زُرْقًا", "azraq", "noun", ["hal", "jam-taksir", "sifa-mushabbaha"],
     "حَالٌ مِنَ «الْمَاءَ» مَنْصُوبٌ بِالْفَتْحَةِ — حَالٌ سَبَبِيَّةٌ؛ جَمْعُ أَزْرَقَ، وَالزُّرْقَةُ هُنَا: شِدَّةُ الصَّفَاءِ.",
     "A hal of «the water», in nasb — a hal by way of what belongs to it; the plural of أَزْرَق, and «blue» here is the depth of its clearness.",
     "«Su»dan hâl, mansûb — sebebî hâl; «ezrak»ın cem'i; mavilik burada duruluğun şiddetidir."),
  T("جِمَامُهُ", "jamm-water", "noun", ["fail", "jam-taksir", "idafa-definiteness", "al-bariz-al-muttasil"],
     "فَاعِلٌ لِـ«زُرْقًا» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ جَمٍّ: مَا اجْتَمَعَ مِنَ الْمَاءِ فِي الْبِئْرِ وَالْحَوْضِ. هٰكَذَا بِالرَّفْعِ عِنْدَ الدُّرَّةِ نَصًّا وَإِعْرَابًا؛ وَفِي مَطْبُوعِ الزَّوْزَنِيِّ «جِمَامَهُ» بِفَتْحِ الْمِيمِ.",
     "The doer of «blue», in raf'; annexed to the attached «its», in the seat of jarr — the plural of جَمّ, the water that gathers in a well or a trough. So, in rafʿ, in al-Durra's text and iʿrāb; the Zawzanī edition prints جِمَامَهُ, with fatha on the mim.",
     "«Mavi»nin fâili, merfû; bitişik zamire muzâf, zamir mahallen mecrûr — «cemm»in cem'i: kuyuda ve havuzda biriken su. Dürre'nin metninde ve i'râbında böyle merfûdur; Zevzenî baskısında mîm'in fethasıyla «cimâmehû» basılmıştır.",
     segs=SG(("جِمَامُ", "jamm-water", "noun"), ("هُ", "pron-3ms", "pron")))],
 [NUN_M("وَضَعْنَ", "wadaa", g=["mithal-verbs", "kinaya", "aqsam-al-kinaya"], note=(" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ. وَ«وَضْعُ الْعِصِيِّ» كِنَايَةٌ عَنِ الْإِقَامَةِ، لِأَنَّ الْمُسَافِرِينَ إِذَا أَقَامُوا وَضَعُوا عِصِيَّهُمْ (الزَّوْزَنِيُّ) — وَهِيَ كِنَايَةٌ عَنْ صِفَةٍ", " — the clause is the answer of لَمَّا and has no seat. «Laying down the staffs» is a kinaya for settling, since travellers lay down their staffs when they stay (al-Zawzanī) — a kinaya for a quality", " — cümle lemmâ'nın cevabıdır, mahalli yoktur. «Asâları bırakmak» ikametten kinâyedir; çünkü yolcular konakladıklarında asâlarını bırakırlar (Zevzenî) — sıfattan kinâyedir")),
  MAFUL("عِصِيَّ", "asa-staff", extra=["jam-taksir", "idafa-definiteness"], note_ar="، مُضَافٌ — جَمْعُ عَصًا، وَتُكْسَرُ عَيْنُهُ وَتُضَمُّ (وَالْكَسْرُ مِنَ الْمُحَرِّرِ)", note_en=", annexed — the plural of عَصًا, said with kasra or damma on the ʿayn (the kasra here is editorial)", note_tr=", muzâf — «asâ»nın cem'i; aynı kesreli de dammeli de okunur (buradaki kesre editoryaldir)"),
  MUDAF_ILAYH("الْحَاضِرِ", "hadir", extra=["ism-fail", "ijaz-al-hadhf"], **W(MAWSUF("الرَّجُلِ الْحَاضِرِ، أَيِ النَّازِلِ عَلَى الْمَاءِ الْمُقِيمِ؛ أَيْ: عَزَمْنَ عَلَى الْإِقَامَةِ كَالْحَاضِرِ الْمُبْتَنِي الْخَيْمَةَ (الزَّوْزَنِيُّ)", "«the [man] who is settled» at a water; that is, they resolved to stay, like a settler who builds his tent (al-Zawzanī)", "«su başına yerleşmiş [kimse]»; yani çadır kuran yerleşik kimse gibi ikamete karar verdiler (Zevzenî)"))),
  T("الْمُتَخَيِّمِ", "mutakhayyim", "noun", ["naat-sifa", "ism-fail", "al-qafiya"],
     "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنْ تَخَيَّمَ: ابْتَنَى الْخَيْمَةَ" + RAWI_AL[0] + ".",
     "A second na't of the omitted noun, in jarr — the active participle of تَخَيَّمَ, to put up a tent" + RAWI_AL[1] + ".",
     "Mahzûf mevsûfun ikinci na'tı, mecrûr — «tehayyeme»den ism-i fâil: çadır kurmak" + RAWI_AL[2] + ".")])
# ---- v. 15 ----
VV(15, "They came up out of al-Sūbān, then crossed it again, each on a Qaynī saddle, new and made wide.",
  "Sûbân'dan yukarı çıktılar, sonra onu bir kez daha kestiler; her biri yeni ve geniş yapılmış bir Kaynî semer üzerindeydi.",
 [NUN_M("ظَهَرْنَ", "zahara", note=(" — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ أَيْ: عَلَوْنَ مِنْ وَادِي السُّوبَانِ", " — a new sentence; that is, they climbed up out of the valley of al-Sūbān", " — cümle müste'nefedir; yani Sûbân vadisinden yukarı çıktılar")),
  MINA(), MAJR("السُّوبَانِ", "suban", "propn", **W(MT("ظَهَرْنَ", "they came up", "çıktılar»a"))),
  THUMMA(),
  T("جَزَعْنَهُ", "jazaa-cross", "verb", ["al-bariz-al-muttasil", "fail", "maful-bihi", "atf-nasaq"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى السُّوبَانِ — وَالْجَزْعُ: قَطْعُ الْوَادِي؛ أَيْ قَطَعْنَهُ مَرَّةً أُخْرَى لِأَنَّهُ اعْتَرَضَ لَهُنَّ فِي طَرِيقِهِنَّ مَرَّتَيْنِ (الزَّوْزَنِيُّ).",
     "Past verb built on sukun because the nun of the women is attached; that nun is the doer, and the attached «it» (al-Sūbān) the object, in the seat of nasb — جَزْع is cutting across a valley: they crossed it a second time, for it lay across their road twice (al-Zawzanī).",
     "Nûn-ı nisve bitiştiği için sükûn üzere mebnî mâzî; nûn fâil; Sûbân'a dönen bitişik «onu» mef'ûlün bih, mahallen mansûb — «cez'»: vadiyi enine kesmek; yani onu bir kez daha geçtiler, çünkü yollarına iki kez çıkmıştı (Zevzenî).",
     segs=SG(("جَزَعْنَ", "jazaa-cross", "verb"), ("هُ", "pron-3ms", "pron")))],
 [PREP("عَلَى", "ala", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَزَعْنَهُ» (الدُّرَّةُ)، أَوْ بِمَحْذُوفٍ حَالٍ: وَهُنَّ عَلَى كُلِّ رَحْلٍ (الزَّوْزَنِيُّ)", role_en="; the phrase hangs on «crossed it» (al-Durra), or on an omitted hal: «while they were on …» (al-Zawzanī)", role_tr="; câr-mecrûr «kestiler»e (Dürre) yahut mahzûf bir hâle müteallik: «… üzerinde oldukları halde» (Zevzenî)", gloss_tr="«üzerinde»"),
  MAJR("كُلِّ", "kull", **W(MUD)),
  MUDAF_ILAYH("قَيْنِيٍّ", "qayni", extra=["ism-mansub", "ijaz-al-hadhf"], **W(MAWSUF("رَحْلٍ قَيْنِيٍّ — نِسْبَةٌ إِلَى الْقَيْنِ، وَهُوَ هُنَا الرَّحَّالُ صَانِعُ الرِّحَالِ؛ وَيُرْوَى «حِيرِيٍّ» نِسْبَةً إِلَى الْحِيرَةِ (الزَّوْزَنِيُّ)", "«a Qaynī [saddle]» — a nisba to the قَيْن, here the saddle-maker; also read حِيرِيٍّ, «of al-Ḥīra» (al-Zawzanī)", "«Kaynî [semer]» — «kayn»e nisbet; burada semer ustası; Hîre'ye nisbetle «hîrî» diye de rivayet edilir (Zevzenî)"))),
  NAAT("قَشِيبٍ", "qashib", "jarr", extra=["sifa-mushabbaha"], note_ar=" — الْجَدِيدُ", note_en=" — «new»", note_tr=" — «yeni»"),
  ATF("وَمُفْأَمِ", "mufam-wide", case="jarr", extra=["ism-maful", "al-qafiya"], note_ar=" — اسْمُ مَفْعُولٍ مِنْ أَفْأَمَ: الْمُوَسَّعُ" + RAWI_J[0], note_en=" — the passive participle of أَفْأَمَ: «made wide»" + RAWI_J[1], note_tr=" — «ef'eme»den ism-i mef'ûl: «genişletilmiş»" + RAWI_J[2])])
def MJ(full, lex, why, sign, doer, g=None, passive=False, pre=None, segs=None, note=("", "", ""), p=None):
    """a muḍāriʿ in jazm for any stated reason: why = (ar, en, tr), e.g. «مَعْطُوفٌ عَلَى …»"""
    s = SGN[sign]; pre = pre or ("", "", "")
    mj = (" مَبْنِيٌّ لِلْمَجْهُولِ", " passive", " meçhûl") if passive else ("", "", "")
    return T(full, lex, "verb", ["nawasib-wa-jawazim-al-mudari"] + (["al-qafiya"] if sign == "rawi" else []) + (["naib-al-fail", "al-majhul-fil-kafiya"] if passive else []) + (g or []),
        pre[0] + "فِعْلٌ مُضَارِعٌ" + mj[0] + " مَجْزُومٌ " + why[0] + " وَعَلَامَةُ جَزْمِهِ " + s[0] + doer[0] + note[0] + ".",
        cap(pre[1] + "present" + mj[1] + " verb in jazm, " + why[1] + ", its sign " + s[1] + doer[1] + note[1] + "."),
        cap(pre[2] + why[2] + " meczûm" + mj[2] + " muzâri, alâmeti " + s[2] + doer[2] + note[2] + "."), p=p, segs=segs)
NF = lambda ar, en, tr: ("، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: " + ar, "; its deputy doer is the hidden " + en, "; nâib-i fâil " + tr)
FH = lambda ar, en, tr: ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: " + ar, "; the doer is the hidden " + en, "; fâil " + tr)

# =====================================================================================================================
# vv. 22–27 — الدِّيَاتُ، وَرِسَالَةٌ إِلَى الْأَحْلَافِ
# =====================================================================================================================
VV(22, "The wounds are wiped out by hundreds of camels, and now those camels are paid out in instalments by men who had no guilt in that bloodshed.",
  "Yaralar yüzlerce deveyle silinir; o develeri de bu kan dökmede hiçbir suçu olmayan kimseler taksit taksit öder oldu.",
 [T("تُعَفَّى", "affa-efface", "verb", ["mudari-marfu", "naqis-verbs", "form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَنَائِبُ الْفَاعِلِ بَعْدَهُ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ وَالتَّعْفِيَةُ: التَّمْحِيَةُ.",
     "A present verb in the passive, in raf' by a damma estimated on the alif; its deputy doer follows — a new sentence; تَعْفِيَة is wiping out.",
     "Elif üzerinde takdîrî damme ile merfû meçhul muzâri; nâib-i fâili ondan sonra gelir — cümle müste'nefedir; «ta'fiye»: silmek, yok etmek."),
  T("الْكُلُومُ", "kalm-wound", "noun", ["naib-al-fail", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ كَلْمٍ وَهُوَ الْجُرْحُ.", "The deputy doer, in raf' — the plural of كَلْم «wound».", "Nâib-i fâil, merfû — «kelm»in («yara») cem'i."),
  BI_NOUN("بِالْمِئِينَ", "mia", "الْمِئِينَ", extra=["asma-al-adad-fil-kafiya", "jam-mudhakkar-salim", "ijaz-al-hadhf"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ", note_ar=" — جَمْعُ مِئَةٍ؛ وَالْمَعْدُودُ مَحْذُوفٌ: بِالْمِئِينَ مِنَ الْإِبِلِ (الزَّوْزَنِيُّ). وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُعَفَّى»", note_en=" — by the ya: «hundreds» is declined like the sound masculine plural; the thing counted is left out: «hundreds [of camels]» (al-Zawzanī). The phrase hangs on «are wiped out»", note_tr=" — yâ ile: «yüzler» cem-i müzekker sâlime mülhaktır; sayılan şey hazfedilmiştir: «yüzlerce [deve]» (Zevzenî). Câr-mecrûr «silinir»e müteallik"),
  T("فَأَصْبَحَتْ", "asbaha", "verb", ["kana-wa-akhawatuha", "form-iv-verbs", "atf-nasaq"],
     FA_AR + "أَصْبَحَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «الْمِئِينَ» أَيِ الْإِبِلِ.",
     "The fa conjoins; أَصْبَحَ «came to be» is a defective past verb built on fatha; the ta marks the feminine; its noun is the hidden «they» — the hundreds, that is, the camels.",
     "«fe» + asbaha «oldu»: fetha üzere mebnî nâkıs mâzî; tâ te'nîs içindir; ismi «yüzler»e, yani develere dönen gizli zamir.",
     segs=SG(("فَ", "fa", "conj"), ("أَصْبَحَتْ", "asbaha", "verb")))],
 [T("يُنَجِّمُهَا", "najjama", "verb", ["mudari-marfu", "form-ii-verbs", "al-bariz-al-muttasil", "maful-bihi", "kana-wa-akhawatuha"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ «مَنْ» بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «أَصْبَحَتْ». يُنَجِّمُهَا: يُعْطِيهَا نُجُومًا، أَيْ أَقْسَاطًا مُتَفَرِّقَةً، وَكَذٰلِكَ تُعْطَى الدِّيَاتُ.",
     "Present verb in raf'; the attached «them» is the object, in the seat of nasb, and the doer, مَنْ, follows — the clause is the predicate of أَصْبَحَتْ, in the seat of nasb. يُنَجِّمُهَا: he gives them «by stars», in separate instalments — as blood-money is paid.",
     "Merfû muzâri; bitişik «onları» mef'ûlün bih, mahallen mansûb; fâili sonraki «men»dir — cümle «asbahat»ın haberi, mahallen mansûb. «Yüneccimühâ»: onları «necim necim», yani ayrı taksitlerle verir; diyetler böyle ödenir.",
     segs=SG(("يُنَجِّمُ", "najjama", "verb"), ("هَا", "pron-3fs", "pron"))),
  T("مَنْ", "man-mawsula", "pron", ["ism-mawsul", "fail"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ «يُنَجِّمُ» — يُرِيدُ السَّيِّدَيْنِ: هُمَا بِمَعْزِلٍ عَنْ إِرَاقَةِ الدِّمَاءِ وَقَدْ ضَمِنَا الدِّيَاتِ (الزَّوْزَنِيُّ).",
     "A relative noun «he who», built on sukun, in the seat of raf' as the doer of «pays out» — he means the two lords: they had no part in the bloodshed, yet took the blood-money on themselves (al-Zawzanī).",
     "İsm-i mevsûl «…-en kimse», sükûn üzere mebnî; «taksitle öder»in fâili olarak mahallen merfû — iki efendiyi kasteder: kan dökmekten uzaktırlar, ama diyetleri üstlenmişlerdir (Zevzenî)."),
  T("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "ism-mawsul"],
     "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»" + SILA_[0] + ".",
     "A frozen defective past verb built on fatha; its noun is the hidden «he», returning to مَنْ" + SILA_[1] + ".",
     "Fetha üzere mebnî câmid nâkıs mâzî; ismi «men»e dönen gizli zamir «o»" + SILA_[2] + "."),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)", note_ar=" — أَيْ فِي هٰذِهِ الْحُرُوبِ (الزَّوْزَنِيُّ)؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُجْرِمِ»", note_en="; «in it» is «in these wars» (al-Zawzanī); the phrase hangs on «guilty»", note_tr="; yani «bu savaşlarda» (Zevzenî); câr-mecrûr «suçlu»ya müteallik"),
  T("بِمُجْرِمِ", "bi", "prep", ["huruf-al-ziyada-fil-kafiya", "kana-wa-akhawatuha", "huruf-jarr", "ism-fail", "al-qafiya"],
     "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَمُجْرِمِ خَبَرُ «لَيْسَ» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا" + RAWI_J[0] + ".",
     "The ba is an added jarr letter that strengthens the negation; «guilty» is the predicate of لَيْسَ — in jarr in wording, in nasb in its seat" + RAWI_J[1] + ".",
     "Bâ, nefyi te'kîd eden zâid cer harfi; «suçlu», «leyse»nin haberi — lafzen mecrûr, mahallen mansûb" + RAWI_J[2] + ".",
     segs=SG(("بِ", "bi", "prep"), ("مُجْرِمِ", "mujrim", "noun")))])
# ---- v. 23 ----
VV(23, "One people pays them out, in instalments, to another as a debt of indemnity — and they themselves had not shed among them so much blood as would fill a cupping-glass.",
  "Onları bir kavim başka bir kavme tazminat olarak taksit taksit öder — oysa kendileri aralarında bir hacamat şişesi dolusu kan bile dökmemişlerdi.",
 [T("يُنَجِّمُهَا", "najjama", "verb", ["mudari-marfu", "form-ii-verbs", "al-bariz-al-muttasil", "maful-bihi", "badal"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ بَدَلٌ مِنْ جُمْلَةِ «يُنَجِّمُهَا مَنْ …» فِي الْبَيْتِ قَبْلَهُ (الدُّرَّةُ).",
     "Present verb in raf'; the attached «them» is the object, in the seat of nasb; the doer follows — the clause is a badal of the clause «those pay them out who …» in the verse before (al-Durra).",
     "Merfû muzâri; bitişik «onları» mef'ûlün bih, mahallen mansûb; fâili ondan sonradır — cümle, önceki beyitteki «yüneccimühâ men …» cümlesinden bedeldir (Dürre).",
     segs=SG(("يُنَجِّمُ", "najjama", "verb"), ("هَا", "pron-3fs", "pron"))),
  FAIL("قَوْمٌ", "qawm", note_ar=" — وَهُمَا السَّيِّدَانِ", note_en=" — the «people» are the two lords", note_tr=" — «kavim» iki efendidir"),
  T("لِقَوْمٍ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَقَوْمٍ مَجْرُورٌ بِالْكَسْرَةِ — أَيْ لِأَوْلِيَاءِ الْقَتْلَى؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُنَجِّمُ».", "The lam is a jarr letter; «a people» is in jarr — the kin of the slain; the phrase hangs on «pays out».", "Lâm cer harfi; «kavim» mecrûr — yani öldürülenlerin velileri; câr-mecrûr «öder»e müteallik.",
     segs=SG(("لِ", "li", "prep"), ("قَوْمٍ", "qawm", "noun"))),
  T("غَرَامَةً", "gharama", "noun", ["maful-mutlaq", "masdar"],
     "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ، عَامِلُهُ «يُنَجِّمُ» (الدُّرَّةُ) — أَيْ يَغْرَمُونَهَا غَرَامَةً، لِأَنَّ الدِّيَاتِ تَلْزَمُ غَيْرَهُمَا (الزَّوْزَنِيُّ).",
     "A maf'ul mutlaq, in nasb, governed by «pays out» (al-Durra) — «as an indemnity they owe», though the blood-money was in truth others' to pay (al-Zawzanī).",
     "Mef'ûl-i mutlak, mansûb; âmili «öder»dir (Dürre) — yani «tazminat olarak öderler»; oysa diyetler aslında başkalarının borcudur (Zevzenî).")],
 [T("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "hal", "al-hal-jumla-wa-rabituha"],
     "الْوَاوُ حَالِيَّةٌ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw opens a hal clause; لَمْ is the particle of negation and jazm that turns the present to the past.", "Vâv hâliyyedir; lem nefy, cezm ve kalb harfidir.",
     segs=SG(("وَ", "wa", "conj"), ("لَمْ", "lam-jazima", "part"))),
  T("يُهَرِيقُوا", "haraqa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "afal-khamsa", "al-bariz-al-muttasil", "fail", "hollow-verbs", "ijaz-al-hadhf"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["nun"][0] + "، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «قَوْمٌ»، وَسَوَّغَ مَجِيءَ الْحَالِ مِنَ النَّكِرَةِ الْوَاوُ (الدُّرَّةُ). هَرَاقَ يُهَرِيقُ لُغَةٌ فِي أَرَاقَ يُرِيقُ، وَالْهَاءُ بَدَلٌ مِنَ الْهَمْزَةِ (الزَّوْزَنِيُّ).",
     "Present verb in jazm by لَمْ, its sign " + SGN["nun"][1] + "; the waw is the doer, in the seat of raf' — the clause is a hal of «a people», in the seat of nasb; the waw is what lets a hal come from an indefinite (al-Durra). هَرَاقَ يُهَرِيقُ is a form of أَرَاقَ يُرِيقُ «to shed», its ha standing for the hamza (al-Zawzanī).",
     "Lem ile meczûm muzâri, alâmeti " + SGN["nun"][2] + "; vâv fâildir, mahallen merfû — cümle «kavim»den hâl, mahallen mansûb; nekreden hâl gelmesini vâv caiz kılmıştır (Dürre). «Herâka yüherîku», «erâka yürîku»nun («döktü») bir lügatidir; hâ hemzeden bedeldir (Zevzenî).",
     segs=SG(("يُهَرِيقُ", "haraqa", "verb"), ("وا", "pron-3mp", "pron"))),
  T("بَيْنَهُمْ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
     "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«يُهَرِيقُوا»، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "An adverb of place, in nasb, hanging on «shed»; annexed to the attached «them», in the seat of jarr.",
     "Mekân zarfı, mansûb, «dökmediler»e müteallik; bitişik zamire muzâf, zamir mahallen mecrûr.",
     segs=SG(("بَيْنَ", "bayna", "noun"), ("هُمْ", "pron-3mp", "pron"))),
  MAFUL("مِلْءَ", "mil", extra=["idafa-definiteness", "ijaz-al-hadhf"], note_ar="، مُضَافٌ — وَالْمِلْءُ: مِقْدَارُ مَا يَمْلَأُ الْإِنَاءَ؛ وَالْمُمَيَّزُ مَحْذُوفٌ: مِلْءَ مِحْجَمٍ مِنَ الدِّمَاءِ (الزَّوْزَنِيُّ)", note_en=", annexed — مِلْء is as much as fills a vessel; what it measures is left out: «a cupping-glass-full [of blood]» (al-Zawzanī)", note_tr=", muzâf — «mil'»: bir kabı dolduran miktar; ölçülen şey hazfedilmiştir: «bir hacamat şişesi dolusu [kan]» (Zevzenî)"),
  MUDAF_ILAYH("مِحْجَمِ", "mihjam", extra=["al-qafiya"], note_ar=" — آلَةُ الْحَجَّامِ" + RAWI_J[0], note_en=" — the cupper's glass" + RAWI_J[1], note_tr=" — hacamatçının şişesi" + RAWI_J[2])])
# ---- v. 24 ----
VV(24, "So there came to flow among them, out of your inherited wealth, spoils of many kinds — young camels with slit ears.",
  "Böylece onların arasında, sizin atadan kalma malınızdan, türlü türlü ganimetler — kulakları çentikli genç develer — akar oldu.",
 [T("فَأَصْبَحَ", "asbaha", "verb", ["kana-wa-akhawatuha", "form-iv-verbs", "atf-nasaq", "tanazu"],
     FA_AR + "أَصْبَحَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ. وَقَدْ تَنَازَعَ هُوَ وَ«يَجْرِي» الِاسْمَ «مَغَانِمُ»: الْأَوَّلُ يَطْلُبُهُ اسْمًا لَهُ وَالثَّانِي فَاعِلًا، فَيَعْمَلُ فِيهِ أَحَدُهُمَا وَيُضْمَرُ فِي الْآخَرِ؛ وَلَمْ يُؤَنَّثْ وَاحِدٌ مِنْهُمَا لِذٰلِكَ (الدُّرَّةُ).",
     "The fa conjoins; أَصْبَحَ «came to be» is a defective past verb built on fatha. It and «flows» both lay claim to the noun «spoils» — the first as its noun, the second as its doer — so one governs it and the other holds a pronoun; that is why neither takes the feminine sign (al-Durra).",
     "«fe» + asbaha «oldu»: fetha üzere mebnî nâkıs mâzî. O ve «akar» fiili «ganimetler» ismi üzerinde tenâzu etmiştir: birincisi onu isim, ikincisi fâil olarak ister; biri onda amel eder, diğerinde zamir takdir edilir; bu yüzden ikisi de müennes yapılmamıştır (Dürre).",
     segs=SG(("فَ", "fa", "conj"), ("أَصْبَحَ", "asbaha", "verb"))),
  T("يَجْرِي", "jara", "verb", ["mudari-marfu", "naqis-verbs", "kana-wa-akhawatuha", "tanazu"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «أَصْبَحَ».",
     "Present verb in raf' by a damma estimated on the ya — the clause is the predicate of أَصْبَحَ, in the seat of nasb.",
     "Yâ üzerinde takdîrî damme ile merfû muzâri — cümle «asbaha»nın haberi, mahallen mansûb."),
  T("فِيهِمُ", "fi", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
     "فِي حَرْفُ جَرٍّ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — يَعُودُ عَلَى أَوْلِيَاءِ الْمَقْتُولِينَ — وَضُمَّتِ الْمِيمُ وَأُشْبِعَتْ لِإِقَامَةِ الْوَزْنِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَجْرِي».",
     "فِي is a jarr letter, and the attached «them» — the kin of the slain — fills the seat of jarr; its mim takes a lengthened damma to keep the metre; the phrase hangs on «flows».",
     "«fî» cer harfi; bitişik «hüm» — öldürülenlerin velileri — mahallen mecrûr; vezin için mîm dammelenip uzatılmıştır; câr-mecrûr «akar»a müteallik.",
     segs=SG(("فِي", "fi", "prep"), ("هِمُ", "pron-3mp", "pron"))),
  MIN(role=MT("يَجْرِي", "flows", "akar»a")),
  ENC_NOUN("تِلَادِكُمْ", "tilad", "كُمْ", "majr", note_ar=" — وَالتِّلَادُ: الْمَالُ الْقَدِيمُ الْمَوْرُوثُ", note_en=" — تِلَاد is old, inherited wealth", note_tr=" — «tilâd»: eskiden beri gelen, miras kalmış mal")],
 [T("مَغَانِمُ", "maghnam", "noun", ["kana-wa-akhawatuha", "fail", "jam-taksir", "mamnu-min-sarf", "tanazu"],
     "اسْمُ «أَصْبَحَ» مُؤَخَّرٌ — أَوْ فَاعِلُ «يَجْرِي» — مَرْفُوعٌ بِالضَّمَّةِ مِنْ غَيْرِ تَنْوِينٍ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ؛ جَمْعُ مَغْنَمٍ وَهُوَ الْغَنِيمَةُ.",
     "The noun of أَصْبَحَ, placed late — or the doer of «flows» — in raf' by the damma with no tanwin, a diptote on the pattern of the farthest plurals; the plural of مَغْنَم «spoil».",
     "«Asbaha»nın sonraya bırakılmış ismi — yahut «akar»ın fâili — tenvinsiz damme ile merfû; muntehe'l-cumû' vezninde gayr-i munsarif; «mağnem»in («ganimet») cem'i."),
  NAAT("شَتَّى", "shatta", "raf", extra=["ism-maqsur-manqus"], note_ar=" — بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ؛ أَيْ مُتَفَرِّقَةٌ", note_en=" — its damma estimated on the alif; «of sundry kinds»", note_tr=" — dammesi elif üzerinde takdîrîdir; «çeşit çeşit»"),
  MIN(role=(" — وَمِنْ بَيَانِيَّةٌ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«مَغَانِمُ»", "; مِنْ explains, and the phrase hangs on an omitted second na't of «spoils»", " — «min» beyâniyyedir; câr-mecrûr «ganimetler»in mahzûf ikinci na'tına müteallik")),
  MAJR("إِفَالٍ", "afil", extra=["jam-taksir"], note_ar=" — جَمْعُ أَفِيلٍ: الصَّغِيرُ السِّنِّ مِنَ الْإِبِلِ؛ وَخَصَّ الصِّغَارَ لِأَنَّ الدِّيَاتِ تُعْطَى مِنْهَا (الزَّوْزَنِيُّ)", note_en=" — the plural of أَفِيل, a young camel; he names the young because blood-money is paid in them (al-Zawzanī)", note_tr=" — «efîl»in cem'i: genç deve; diyetler onlardan ödendiği için küçükleri anmıştır (Zevzenî)"),
  NAAT("مُزَنَّمِ", "muzannam", "jarr", extra=["ism-maful", "al-qafiya"], note_ar=" — الْمُعَلَّمُ بِزَنَمَةٍ؛ وَلَمْ يَقُلْ «الْمُزَنَّمَةِ» حَمْلًا عَلَى لَفْظِ «إِفَالٍ»، لِأَنَّ فِعَالًا مِمَّا يَشْتَرِكُ فِيهِ الْآحَادُ وَالْجُمُوعُ (الزَّوْزَنِيُّ)" + RAWI_J[0], note_en=" — marked by a slit in the ear; it is masculine singular, after the form of إِفَال, since فِعَال is a pattern singulars and plurals share (al-Zawzanī)" + RAWI_J[1], note_tr=" — kulağı çentilerek işaretlenmiş; «ifâl» lafzına uyularak müzekker müfred gelmiştir, çünkü «fiâl» müfred ile cemin ortak veznidir (Zevzenî)" + RAWI_J[2])])
# ---- v. 25 ----
VV(25, "Now carry from me a message to the allies, and to Dhubyān: You have sworn, have you not, every oath there is.",
  "Haydi, müttefiklere ve Zübyân'a benden şu mesajı ulaştır: Siz gerçekten her türlü yemini ettiniz.",
 [T("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ لَا عَمَلَ لَهُ.", "A particle of opening and alerting; it governs nothing.", "İstiftâh ve tenbîh harfi; ameli yoktur."),
  T("أَبْلِغِ", "ablagha", "verb", ["imperative-amr", "form-iv-verbs", "mafulayn", "al-fail-al-mudmar-al-mustatir-wujuban"],
     "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — يَنْصِبُ مَفْعُولَيْنِ.",
     "Imperative built on sukun, voweled with kasra because two quiescents meet; the doer «you» must stay hidden — it takes two objects.",
     "Sükûn üzere mebnî emir; iki sâkin karşılaştığı için kesre ile harekelenmiştir; fâil vücûben gizli «sen» — iki mef'ûl alır."),
  MAFUL("الْأَحْلَافَ", "halif", extra=["jam-taksir", "mafulayn"], note_ar=" — الْمَفْعُولُ الْأَوَّلُ؛ جَمْعُ حَلِيفٍ، كَشَرِيفٍ وَأَشْرَافٍ (الزَّوْزَنِيُّ)", note_en=" — the first object; the plural of حَلِيف «sworn ally», like شَرِيف and أَشْرَاف (al-Zawzanī)", note_tr=" — birinci mef'ûl; «halîf»in («yeminli müttefik») cem'i; «şerîf – eşrâf» gibi (Zevzenî)"),
  T("عَنِّي", "an", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"],
     "عَنْ حَرْفُ جَرٍّ، وَالنُّونُ الثَّانِيَةُ لِلْوِقَايَةِ أُدْغِمَتْ فِيهَا نُونُ «عَنْ»، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَبْلِغْ».",
     "عَنْ is a jarr letter; the second nun is the nun of protection, into which the nun of عَنْ is merged; the ya «me» fills the seat of jarr — the phrase hangs on «carry».",
     "«an» cer harfi; ikinci nûn vikâye nûnudur, «an»ın nûnu ona idgam edilmiştir; yâ mahallen mecrûr — câr-mecrûr «ulaştır»a müteallik.",
     segs=SG(("عَنْ", "an", "prep"), ("نِ", "nun-wiqaya", "part"), ("ي", "pron-1s", "pron"))),
  MAFUL("رِسَالَةً", "risala", extra=["mafulayn"], note_ar=" — الْمَفْعُولُ الثَّانِي", note_en=" — the second object", note_tr=" — ikinci mef'ûl")],
 [ATF("وَذُبْيَانَ", "dhubyan", "propn", case="nasb", extra=["mamnu-min-sarf"], sign="مَنْصُوبٌ بِالْفَتْحَةِ مِنْ غَيْرِ تَنْوِينٍ", note_ar=" — عُطِفَ عَلَى «الْأَحْلَافَ»", note_en=" — joined to «the allies»; a diptote, with no tanwin", note_tr=" — «müttefikler»e atfedilmiştir; gayr-i munsarif, tenvinsiz"),
  T("هَلْ", "hal-istifham", "part", ["al-istifham", "khuruj-al-istifham"],
     "حَرْفُ اسْتِفْهَامٍ خَرَجَ إِلَى التَّحْقِيقِ وَالتَّقْرِيرِ: هَلْ أَقْسَمْتُمْ أَيْ قَدْ أَقْسَمْتُمْ، كَقَوْلِهِ تَعَالَى ﴿هَلْ أَتَىٰ عَلَى الْإِنْسَانِ﴾ أَيْ قَدْ أَتَى (الزَّوْزَنِيُّ).",
     "The particle of question, here turned to affirming: «have you sworn» means «you have indeed sworn» — as in the Qurʾān's ﴿هَلْ أَتَىٰ عَلَى الْإِنْسَانِ﴾ (al-Insān 1), that is, «there has indeed come» (al-Zawzanī).",
     "İstifhâm harfi; burada tahkîk ve takrîre çıkmıştır: «yemin ettiniz mi» yani «gerçekten yemin ettiniz» — Kur'ân'daki ﴿هَلْ أَتَىٰ عَلَى الْإِنْسَانِ﴾ (İnsân 1) gibi; yani «gerçekten gelmiştir» (Zevzenî)."),
  T("أَقْسَمْتُمُ", "aqsama", "verb", ["form-iv-verbs", "al-bariz-al-muttasil", "fail", "mulhaq-bil-jinas"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَضُمَّتِ الْمِيمُ وَأُشْبِعَتْ لِإِقَامَةِ الْوَزْنِ — وَالْجُمْلَةُ مُفَسِّرَةٌ لِـ«رِسَالَةً» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ (الدُّرَّةُ). وَبَيْنَهُ وَبَيْنَ «مُقْسَمِ» اشْتِقَاقٌ.",
     "Past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer; the mim takes a lengthened damma to keep the metre — the clause explains «a message» and has no seat (al-Durra). It shares a root with مُقْسَمِ.",
     "Ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir; vezin için mîm dammelenip uzatılmıştır — cümle «mesaj»ı tefsir eder, mahalli yoktur (Dürre). «Muksem» ile arasında iştikâk vardır."),
  T("كُلَّ", "kull", "noun", ["maful-mutlaq", "idafa-definiteness"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "It stands for the maf'ul mutlaq, in nasb, and is annexed.", "Mef'ûl-i mutlaktan nâib, mansûb, muzâf."),
  MUDAF_ILAYH("مُقْسَمِ", "muqsam", extra=["masdar", "al-qafiya", "mulhaq-bil-jinas"], note_ar=" — مَصْدَرٌ مِيمِيٌّ بِمَعْنَى الْإِقْسَامِ: أَيْ قَدْ حَلَفْتُمْ عَلَى إِبْرَامِ حَبْلِ الصُّلْحِ كُلَّ حَلِفٍ، فَتَحَرَّجُوا مِنَ الْحِنْثِ (الزَّوْزَنِيُّ)" + RAWI_J[0], note_en=" — a mimi masdar meaning «swearing»: you have sworn every oath to make the bond of peace fast, so shrink from breaking it (al-Zawzanī)" + RAWI_J[1], note_tr=" — «yemin etme» anlamında mîmî masdar: barış bağını pekiştirmek üzere her türlü yemini ettiniz; öyleyse yemini bozmaktan sakının (Zevzenî)" + RAWI_J[2])])
# ---- v. 26 ----
VV(26, "So do not hide from God what is in your souls, that it may stay hidden; whatever is kept from God, He knows.",
  "Öyleyse içinizdekini gizli kalsın diye Allah'tan saklamayın; Allah'tan ne gizlenirse gizlensin, O bilir.",
 [T("فَلَا", "la-nahiya", "part", ["al-nahy-wa-wujuhuh", "nawasib-wa-jawazim-al-mudari"],
     "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "The fa opens a new clause; لَا is the prohibiting particle, which puts the verb in jazm.", "Fâ isti'nâf içindir; «lâ» nehiy edatıdır, fiili cezmeder.",
     segs=SG(("فَ", "fa", "conj"), ("لَا", "la-nahiya", "part"))),
  T("تَكْتُمُنَّ", "katama", "verb", ["al-nahy-wa-wujuhuh", "nawasib-wa-jawazim-al-mudari", "afal-khamsa", "nun-tawkid", "mafulayn", "mulhaq-bil-jinas"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ " + SGN["nun"][0] + "، وَوَاوُ الْجَمَاعَةِ الْمَحْذُوفَةُ لِالْتِقَاءِ السَّاكِنَيْنِ — الْمَدْلُولُ عَلَيْهَا بِالضَّمَّةِ — ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ نُونُ التَّوْكِيدِ الثَّقِيلَةُ. وَبَيْنَهُ وَبَيْنَ «يُكْتَمِ» اشْتِقَاقٌ.",
     "Present verb in jazm by the prohibiting لَا, its sign " + SGN["nun"][1] + "; the waw of the plural — dropped where two quiescents meet, the damma left as its trace — is the doer, in the seat of raf'; the nun is the heavy nun of emphasis. It shares a root with يُكْتَمِ.",
     "Nehiy «lâ»sı ile meczûm muzâri, alâmeti " + SGN["nun"][2] + "; iki sâkin karşılaştığı için hazfedilen — damme ile delâlet edilen — cemi vâvı fâildir, mahallen merfû; nûn te'kîd-i sakîle nûnudur. «Yüktem» ile arasında iştikâk vardır."),
  T("اللهَ", "allah", "propn", ["maful-bihi", "mafulayn"], "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ عَلَى التَّعْظِيمِ بِالْفَتْحَةِ — أَيْ: لَا تَكْتُمُوا مِنَ اللهِ.", "The Name of Majesty: the first object, in nasb — «do not hide from God».", "Lafza-i Celâl: birinci mef'ûl, ta'zîm üzere mansûb — yani «Allah'tan gizlemeyin»."),
  T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi", "mafulayn"],
     "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ — أَيْ مَا تُضْمِرُونَ مِنَ الْغَدْرِ وَنَقْضِ الْعَهْدِ (الزَّوْزَنِيُّ).",
     "A relative noun «what», built on sukun, in the seat of nasb as the second object — the treachery and breach of covenant you harbour (al-Zawzanī).",
     "İsm-i mevsûl «…-an şey», sükûn üzere mebnî; ikinci mef'ûl olarak mahallen mansûb — yani içinizde beslediğiniz hıyanet ve ahdi bozma niyeti (Zevzenî)."),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ صِلَةِ الْمَوْصُولِ", "; the jarr phrase hangs on the omitted ṣila of the relative", " — câr-mecrûr ism-i mevsûlün mahzûf sılasına müteallik")),
  ENC_NOUN("نُفُوسِكُمْ", "nafs", "كُمْ", "majr", extra=["jam-taksir"], note_ar=" — جَمْعُ نَفْسٍ؛ وَيُرْوَى «صُدُورِكُمْ» (الدُّرَّةُ)", note_en=" — the plural of نَفْس; also read صُدُورِكُمْ «your breasts» (al-Durra)", note_tr=" — «nefs»in cem'i; «sudûriküm» («göğüsleriniz») diye de rivayet edilir (Dürre)")],
 [T("لِيَخْفَى", "khafiya", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "naqis-verbs"],
     "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَيَخْفَى فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَهَا وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَا» — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَكْتُمُنَّ».",
     "The lam is the lam of purpose, a jarr letter; يَخْفَى is a present verb in nasb by an unspoken أَنْ after it, its sign a fatha estimated on the alif; the doer is the hidden «it», returning to مَا — the masdar the clause builds is in jarr by the lam, and the phrase hangs on «hide».",
     "Lâm ta'lîl lâmıdır, cer harfi; «yahfâ» ondan sonra gizli «en» ile mansûb muzâri, alâmeti elif üzerinde takdîrî fetha; fâil «mâ»ya dönen gizli zamir — müevvel masdar lâm ile mecrûr; câr-mecrûr «gizlemeyin»e müteallik.",
     segs=SG(("لِ", "li", "prep"), ("يَخْفَى", "khafiya", "verb"))),
  T("وَمَهْمَا", "mahma", "pron", G_SHART + ["al-mabni-wal-mudmar", "atf-nasaq", "maful-mutlaq"],
     WA_AR + "مَهْمَا اسْمُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ مُطْلَقٌ لِفِعْلِ الشَّرْطِ: أَيَّ كِتْمَانٍ يُكْتَمِ (الدُّرَّةُ)؛ وَعَلَى أَنَّ «كَتَمَ» يَتَعَدَّى إِلَى اثْنَيْنِ هُوَ مَفْعُولُهُ الثَّانِي: وَمَهْمَا يُكْتَمْ مِنْ شَيْءٍ (الزَّوْزَنِيُّ) — فِعْلُ الشَّرْطِ: «يُكْتَمِ» مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ " + SGN["kasr2"][0] + "؛ وَجَوَابُهُ: «يَعْلَمِ» مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + ".",
     "The waw conjoins; مَهْمَا «whatever» is a conditional noun that puts two verbs in jazm, built on sukun in the seat of nasb as the maf'ul mutlaq of the condition's verb — «whatever hiding is done» (al-Durra); if كَتَمَ is taken with two objects it is the second: «whatever thing is kept from God» (al-Zawzanī) — the condition's verb: «is kept», in jazm, its sign " + SGN["kasr2"][1] + "; its answer: «He knows», in jazm, its sign " + SGN["rawi"][1] + ".",
     "«ve» + mehmâ «her ne …-se»: iki fiili cezmeden şart ismi; sükûn üzere mebnî, şart fiilinin mef'ûl-i mutlakı olarak mahallen mansûb — «hangi gizleme yapılırsa» (Dürre); «keteme» iki mef'ûl alır sayılırsa ikinci mef'ûlüdür: «Allah'tan ne gizlenirse» (Zevzenî) — şart fiili: «gizlenirse», meczûm, alâmeti " + SGN["kasr2"][2] + "; cevabı: «bilir», meczûm, alâmeti " + SGN["rawi"][2] + ".",
     segs=SG(("وَ", "wa", "conj"), ("مَهْمَا", "mahma", "pron"))),
  JV("يُكْتَمِ", "katama", "shart", "kasr2", g=["naib-al-fail", "al-majhul-fil-kafiya", "mulhaq-bil-jinas"], passive=True, doer=("، وَنَائِبُ الْفَاعِلِ لَفْظُ الْجَلَالَةِ بَعْدَهُ", "; its deputy doer, the Name of Majesty, follows", "; nâib-i fâili sonraki Lafza-i Celâl'dir")),
  T("اللهُ", "allah", "propn", ["naib-al-fail"], "لَفْظُ الْجَلَالَةِ نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ — أَيْ: يُكْتَمْ مِنَ اللهِ (الزَّوْزَنِيُّ).", "The Name of Majesty: the deputy doer, in raf' — «is kept from God» (al-Zawzanī).", "Lafza-i Celâl: nâib-i fâil, merfû — yani «Allah'tan gizlenirse» (Zevzenî)."),
  JV("يَعْلَمِ", "alima", "jawab", "rawi", g=["hadhf-al-maful"], doer=FH("هُوَ يَعُودُ عَلَى اللهِ، وَالْمَفْعُولُ مَحْذُوفٌ: يَعْلَمْهُ", "«He» — God; its object is left out: «He knows [it]»", "Allah'a dönen gizli zamir; mef'ûlü mahzûf: «onu bilir»"),
     note=(" — يُرِيدُ أَنَّ اللهَ عَالِمٌ بِالْخَفِيَّاتِ وَالسَّرَائِرِ (الزَّوْزَنِيُّ)", " — he means that God knows all hidden things and secrets (al-Zawzanī)", " — yani Allah gizlileri ve sırları bilir (Zevzenî)"))])
# ---- v. 27 ----
VV(27, "It is put off, set down in a book and stored up for the Day of Reckoning — or it is brought forward, and punished now.",
  "(O gizlenen şey) ya ertelenir, bir kitaba yazılıp hesap günü için saklanır; ya da öne alınır ve cezası (dünyada) verilir.",
 [MJ("يُؤَخَّرْ", "akhkhara", ("قِيلَ: بَدَلٌ مِنْ «يَعْلَمِ» فِي الْبَيْتِ قَبْلَهُ، وَقِيلَ: جَوَابٌ لِلنَّهْيِ «فَلَا تَكْتُمُنَّ» وَاسْتَحْسَنَهُ الدُّرَّةُ،", "as a badal of «He knows» in the verse before, on one view — or, as al-Durra prefers, as the answer of the prohibition «do not hide»", "bir görüşe göre önceki beyitteki «bilir»den bedel, Dürre'nin tercih ettiği görüşe göre «gizlemeyin» nehyinin cevabı olarak"), "sukun",
     NF("هُوَ يَعُودُ عَلَى «مَا فِي نُفُوسِكُمْ»", "«it» — what is in your souls", "«içinizdeki»ne dönen gizli zamir"), g=["form-ii-verbs", "tibaq"], passive=True,
     note=(" — أَيْ يُؤَخَّرْ عِقَابُهُ. وَبَيْنَهُ وَبَيْنَ «يُعَجَّلْ» طِبَاقٌ", " — that is, its punishment is put off. With «is brought forward» it makes a tibaq", " — yani cezası ertelenir. «Öne alınır» ile arasında tıbâk vardır")),
  MJ("فَيُوضَعْ", "wadaa", ("مَعْطُوفٌ عَلَى «يُؤَخَّرْ»", "joined to «is put off»", "«ertelenir»e ma'tûf olarak"), "sukun", NF("هُوَ", "«it»", "gizli zamir «o»"), g=["atf-nasaq", "mithal-verbs"], passive=True, pre=FA3, segs=SG(("فَ", "fa", "conj"), ("يُوضَعْ", "wadaa", "verb"))),
  FI(role=MT("يُوضَعْ", "is set down", "konur»a")),
  MAJR("كِتَابٍ", "kitab"),
  MJ("فَيُدَّخَرْ", "iddakhara", ("مَعْطُوفٌ عَلَى «يُوضَعْ»", "joined to «is set down»", "«konur»a ma'tûf olarak"), "sukun", NF("هُوَ", "«it»", "gizli zamir «o»"), g=["atf-nasaq", "form-viii-verbs"], passive=True, pre=FA3, segs=SG(("فَ", "fa", "conj"), ("يُدَّخَرْ", "iddakhara", "verb")),
     note=(" — وَأَصْلُهُ يُذْتَخَرُ: قُلِبَتْ تَاءُ الِافْتِعَالِ دَالًا وَأُدْغِمَتِ الذَّالُ فِيهَا", " — it is يُذْتَخَرُ: the ta of Form VIII turns to dal, and the dhal merges into it", " — aslı «yüztehar»dır: iftiâl tâ'sı dâl'e çevrilmiş, zâl ona idgam edilmiştir"))],
 [T("لِيَوْمِ", "li", "prep", ["huruf-jarr", "idafa-definiteness"], "اللَّامُ حَرْفُ جَرٍّ، وَيَوْمِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُدَّخَرْ».", "The lam is a jarr letter; «day» is in jarr and annexed — the phrase hangs on «is stored up».", "Lâm cer harfi; «gün» mecrûr, muzâf — câr-mecrûr «saklanır»a müteallik.",
     segs=SG(("لِ", "li", "prep"), ("يَوْمِ", "yawm", "noun"))),
  MUDAF_ILAYH("الْحِسَابِ", "hisab"),
  T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّقْسِيمِ: لَا مَخْلَصَ مِنْ عِقَابِ الذَّنْبِ آجِلًا أَوْ عَاجِلًا (الزَّوْزَنِيُّ).", "A conjunction that divides the cases: there is no escape from the punishment of a sin, late or soon (al-Zawzanī).", "Taksîm bildiren atıf harfi: günahın cezasından er ya da geç kurtuluş yoktur (Zevzenî)."),
  MJ("يُعَجَّلْ", "ajjala-hasten", ("مَعْطُوفٌ عَلَى «يُؤَخَّرْ»", "joined to «is put off»", "«ertelenir»e ma'tûf olarak"), "sukun", NF("هُوَ", "«it»", "gizli zamir «o»"), g=["atf-nasaq", "form-ii-verbs", "tibaq"], passive=True,
     note=(" — أَيْ يُعَجَّلِ الْعِقَابُ فِي الدُّنْيَا قَبْلَ الْمَصِيرِ إِلَى الْآخِرَةِ", " — that is, the punishment is brought forward, in this world, before the passage to the next", " — yani ceza âhirete varmadan dünyada öne alınır")),
  MJ("فَيُنْقَمِ", "naqama", ("مَعْطُوفٌ عَلَى «يُعَجَّلْ»", "joined to «is brought forward»", "«öne alınır»a ma'tûf olarak"), "rawi", NF("هُوَ", "«it»", "gizli zamir «o»"), g=["atf-nasaq"], passive=True, pre=FA3, segs=SG(("فَ", "fa", "conj"), ("يُنْقَمِ", "naqama", "verb")),
     note=(" — أَيْ فَيُنْتَقَمَ مِنْ صَاحِبِهِ (الزَّوْزَنِيُّ)", " — that is, vengeance is taken on the one who did it (al-Zawzanī)", " — yani sahibinden intikam alınır (Zevzenî)"))])
# =====================================================================================================================
# vv. 33–40 — حُصَيْنُ بْنُ ضَمْضَمٍ، وَمَوْرِدُ الْمَنَايَا
# =====================================================================================================================
HUSAYN = (" يَعُودُ عَلَى حُصَيْنٍ", " (Ḥuṣayn)", " (Husayn)")
VV(33, "By my life, a fine tribe it is on whom Ḥuṣayn ibn Ḍamḍam brought down a thing they had no part in!",
  "Ömrüme yemin olsun ki, Husayn b. Damdam'ın, kendisine uymadıkları bir işle başlarına belâ getirdiği o kabile ne güzel kabiledir!",
 [T("لَعَمْرِي", "amr-qasam", "noun", ["huruf-al-qasam-fil-kafiya", "mubtada-khabar", "khabar-insha", "ya-al-mutakallim", "al-bariz-al-muttasil"],
     "اللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرِ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي. وَالْقَسَمُ إِنْشَاءٌ غَيْرُ طَلَبِيٍّ: أُقْسِمُ بِحَيَاتِي (الزَّوْزَنِيُّ).",
     "The lam is the lam of beginning; «life» is a mubtada, in raf' by a damma estimated on the letter before the ya of the speaker, which the kasra that suits the ya keeps from showing; it is annexed to that ya, in the seat of jarr — and its khabar must be left out: «[is my oath]». An oath is an insha that asks for nothing: «I swear by my life» (al-Zawzanī).",
     "Lâm ibtidâ lâmıdır; «ömr» mübtedâ; mütekellim yâ'sından önceki harf üzerinde takdîrî damme ile merfû — münasebet kesresi zuhûruna engeldir — yâ'ya muzâf, yâ mahallen mecrûr; haberi vücûben mahzûftur: «yeminimdir». Yemin, talebî olmayan inşâdır: «hayatıma yemin ederim» (Zevzenî).",
     segs=SG(("لَ", "lam-ibtida", "part"), ("عَمْرِ", "amr-qasam", "noun"), ("ي", "pron-1s", "pron"))),
  T("لَنِعْمَ", "nima-verb", "verb", ["afal-al-madh-wal-dhamm-fil-kafiya", "huruf-al-qasam-fil-kafiya", "khabar-insha"],
     "اللَّامُ وَاقِعَةٌ فِي جَوَابِ الْقَسَمِ، وَنِعْمَ فِعْلٌ مَاضٍ جَامِدٌ لِإِنْشَاءِ الْمَدْحِ مَبْنِيٌّ عَلَى الْفَتْحِ — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
     "The lam opens the answer of the oath; نِعْمَ is the frozen past verb that performs praise, built on fatha — the clause is the answer of the oath and has no seat.",
     "Lâm yeminin cevabını açar; «ni'me» medh inşâsı için câmid mâzî fiil, fetha üzere mebnî — cümle yeminin cevabıdır, mahalli yoktur.",
     segs=SG(("لَ", "lam-qasam", "part"), ("نِعْمَ", "nima-verb", "verb"))),
  FAIL("الْحَيُّ", "hayy-tribe", note_ar=" — فَاعِلُ «نِعْمَ»، وَالْمَخْصُوصُ بِالْمَدْحِ مَحْذُوفٌ؛ وَالْحَيُّ: الْقَبِيلَةُ", note_en=" — the doer of نِعْمَ; the one singled out for the praise is left unsaid; حَيّ is a tribe", note_tr=" — «ni'me»nin fâili; mahsûs bi'l-medh hazfedilmiştir; «hayy»: kabile"),
  MADI("جَرَّ", "jarra", ["doubled-verbs", "hal", "al-hal-jumla-wa-rabituha"], note_ar="، وَفَاعِلُهُ «حُصَيْنُ» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ «الْحَيُّ»، أَوْ فِي مَحَلِّ رَفْعٍ نَعْتٌ لَهُ عَلَى أَنَّ «أَلْ» جِنْسِيَّةٌ (الدُّرَّةُ)؛ جَرَّ عَلَيْهِمْ: جَنَى عَلَيْهِمْ", note_en="; its doer is «Ḥuṣayn» — the clause is a hal of «the tribe», in the seat of nasb, or its na't, in the seat of raf', if the article names the kind (al-Durra); جَرَّ عَلَيْهِمْ is «he brought a crime upon them»", note_tr="; fâili «Husayn»dır — cümle «kabile»den hâl, mahallen mansûb; «el» cins için sayılırsa onun na'tı, mahallen merfû (Dürre); «cerra aleyhim»: başlarına bir cinayet getirdi"),
  T("عَلَيْهِمُ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil"],
     "حَرْفُ جَرٍّ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَضُمَّتِ الْمِيمُ وَأُشْبِعَتْ لِإِقَامَةِ الْوَزْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَرَّ».",
     "A jarr letter; the attached «them» fills the seat of jarr, its mim taking a lengthened damma to keep the metre — the phrase hangs on «brought down».",
     "Cer harfi; bitişik «hüm» mahallen mecrûr; vezin için mîm dammelenip uzatılmıştır — câr-mecrûr «getirdi»ye müteallik.",
     segs=SG(("عَلَيْ", "ala", "prep"), ("هِمُ", "pron-3mp", "pron")))],
 [T("بِمَا", "bi", "prep", ["huruf-jarr", "ism-mawsul"],
     "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَرَّ».",
     "The ba is a jarr letter; مَا is a relative noun «what», built on sukun, in the seat of jarr — the phrase hangs on «brought down».",
     "Bâ cer harfi; «mâ» ism-i mevsûl, sükûn üzere mebnî, mahallen mecrûr — câr-mecrûr «getirdi»ye müteallik.",
     segs=SG(("بِ", "bi", "prep"), ("مَا", "ma-mawsula", "pron"))),
  LA_NAFIYA(),
  T("يُؤَاتِيهِمْ", "aata-comply", "verb", ["mudari-marfu", "naqis-verbs", "form-iii-verbs", "al-bariz-al-muttasil", "maful-bihi", "ism-mawsul"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَا»، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + SILA_[0] + "؛ يُؤَاتِيهِمْ: يُوَافِقُهُمْ، أَيْ: وَإِنْ لَمْ يُوَافِقُوهُ فِي إِضْمَارِ الْغَدْرِ وَنَقْضِ الْعَهْدِ (الزَّوْزَنِيُّ).",
     "Present verb in raf' by a damma estimated on the ya; the doer is the hidden «it», returning to مَا, and the attached «them» is the object, in the seat of nasb" + SILA_[1] + "; يُؤَاتِيهِمْ is «suits them, falls in with them»: they did not go along with him in harbouring treachery and breaking the covenant (al-Zawzanī).",
     "Yâ üzerinde takdîrî damme ile merfû muzâri; fâil «mâ»ya dönen gizli zamir; bitişik «onlara» mef'ûlün bih, mahallen mansûb" + SILA_[2] + "; «yüâtîhim»: onlara uyar; yani hıyanet beslemekte ve ahdi bozmakta ona uymadılar (Zevzenî).",
     segs=SG(("يُؤَاتِي", "aata-comply", "verb"), ("هِمْ", "pron-3mp", "pron"))),
  PH(FAIL("حُصَيْنُ", "husayn-murri", "propn", note_ar=" — فَاعِلُ «جَرَّ»؛ وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ عَلَمٌ مَوْصُوفٌ بِـ«ابْن» مُضَافًا إِلَى عَلَمٍ", note_en=" — the doer of «brought down»; its tanwin drops because the name is described by «son of» + a name", note_tr=" — «getirdi»nin fâili; «ibn» ile vasıflanıp başka bir aleme muzâf olduğu için tenvini düşer"), "husayn-ibn-damdam", 3),
  T("بْنُ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«حُصَيْنُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.", "A na't of «Ḥuṣayn», in raf' and annexed — its alif is dropped because it stands between two names.", "«Husayn»ın na'tı, merfû, muzâf — iki alem arasında olduğu için elifi yazılmaz."),
  MUDAF_ILAYH("ضَمْضَمِ", "damdam", "propn", ["al-qafiya"], **W(RAWI_J))])
# ---- v. 34 ----
VV(34, "He had folded his flank over a hidden purpose; he neither showed it nor moved before his time.",
  "O, böğrünü gizli bir niyetin üzerine dürmüştü (içinde bir kin saklamıştı); onu ne açığa vurdu ne de vaktinden önce davrandı.",
 [T("وَكَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "anwa-al-waw"],
     WA_ISTINAF[0] + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى حُصَيْنٍ.",
     WA_ISTINAF[1] + "كَانَ is the defective past verb; its noun is the hidden «he» — Ḥuṣayn.",
     WA_ISTINAF[2] + "kâne: nâkıs mâzî; ismi Husayn'a dönen gizli zamir «o».",
     segs=SG(("وَ", "wa", "conj"), ("كَانَ", "kana", "verb"))),
  T("طَوَى", "tawa", "verb", ["kana-wa-akhawatuha", "naqis-verbs", "kinaya", "aqsam-al-kinaya"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + HUSAYN[0] + " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ. وَ«طَوَى كَشْحَهُ عَلَى كَذَا» كِنَايَةٌ عَنْ إِضْمَارِهِ فِي الصَّدْرِ (الزَّوْزَنِيُّ) — كِنَايَةٌ عَنْ صِفَةٍ.",
     "Past verb built on a fatha estimated on the alif; the doer is the hidden «he»" + HUSAYN[1] + " — the clause is the predicate of كَانَ, in the seat of nasb. «He folded his flank over a thing» is a kinaya for harbouring it in the breast (al-Zawzanī) — a kinaya for a quality.",
     "Elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil gizli zamir «o»" + HUSAYN[2] + " — cümle kâne'nin haberi, mahallen mansûb. «Böğrünü bir şeyin üzerine dürdü», onu içinde gizlemekten kinâyedir (Zevzenî) — sıfattan kinâye."),
  MAFUL("كَشْحًا", "kashh", note_ar=" — وَالْكَشْحُ: مُنْقَطَعُ الْأَضْلَاعِ", note_en=" — كَشْح is the flank, where the ribs end", note_tr=" — «keşh»: böğür, kaburgaların bittiği yer"),
  PREP("عَلَى", "ala", role_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«طَوَى»، أَوْ بِمَحْذُوفٍ نَعْتٍ لِـ«كَشْحًا» (الدُّرَّةُ)", role_en="; the phrase hangs on «folded», or on an omitted na't of «flank» (al-Durra)", role_tr="; câr-mecrûr «dürdü»ye yahut «böğür»ün mahzûf na'tına müteallik (Dürre)", gloss_tr="«üzerine»"),
  MAJR("مُسْتَكِنَّةٍ", "mustakinn", extra=["ism-fail", "ijaz-al-hadhf"], **W(MAWSUF("نِيَّةٍ مُسْتَكِنَّةٍ، أَيْ مُسْتَتِرَةٍ (الزَّوْزَنِيُّ)", "«a hidden [intent]» (al-Zawzanī)", "«gizli [bir niyet]» (Zevzenî)")))],
 [T("فَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq"],
     "الْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ لَا عَمَلَ لَهَا — وَ«لَا» مَعَ الْمَاضِي بِمَنْزِلَةِ «لَمْ» مَعَ الْمُضَارِعِ فِي الْمَعْنَى: فَلَا هُوَ أَبْدَاهَا أَيْ فَلَمْ يُبْدِهَا، كَقَوْلِهِ تَعَالَى ﴿فَلَا صَدَّقَ وَلَا صَلَّىٰ﴾ (الزَّوْزَنِيُّ).",
     "The fa conjoins; لَا negates and governs nothing — with a past verb it means what لَمْ means with the present: «he did not show it», as in the Qurʾān's ﴿فَلَا صَدَّقَ وَلَا صَلَّىٰ﴾ (al-Qiyāma 31) (al-Zawzanī).",
     "Fâ atıf harfi; «lâ» nâfiyedir, amel etmez — mâzî ile birlikte, muzâri ile gelen «lem»in mânâsını verir: «onu açığa vurmadı»; Kur'ân'daki ﴿فَلَا صَدَّقَ وَلَا صَلَّىٰ﴾ (Kıyâme 31) gibi (Zevzenî).",
     segs=SG(("فَ", "fa", "conj"), ("لَا", "la-nafiya", "part"))),
  T("هُوَ", "huwa", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun built on fatha, in the seat of raf' as mubtada.", "Fetha üzere mebnî munfasıl zamir; mübtedâ olarak mahallen merfû."),
  T("أَبْدَاهَا", "abda", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "anwa-al-khabar"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى الْمُسْتَكِنَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.",
     "Past verb built on a fatha estimated on the alif; the doer is the hidden «he», and the attached «it» (the hidden purpose) is the object, in the seat of nasb — the clause is the khabar, in the seat of raf'.",
     "Elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil gizli zamir «o»; gizli niyete dönen bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle mübtedânın haberi, mahallen merfû.",
     segs=SG(("أَبْدَا", "abda", "verb"), ("هَا", "pron-3fs", "pron"))),
  T("وَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "atf-nasaq"], WA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins; لَمْ is the particle of negation and jazm that turns the present to the past.", "«ve» + lem: nefy, cezm ve kalb harfi.",
     segs=SG(("وَ", "wa", "conj"), ("لَمْ", "lam-jazima", "part"))),
  LAM_V("يَتَقَدَّمِ", "taqaddama", "هُوَ", HUSAYN, g=["form-v-verbs"], note=(" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «أَبْدَاهَا»: أَيْ لَمْ يَتَقَدَّمْ عَلَيْهَا قَبْلَ إِمْكَانِ الْفُرْصَةِ، وَلٰكِنْ أَخَّرَهَا حَتَّى تُمْكِنَهُ (الزَّوْزَنِيُّ)", " — the clause is joined to «showed it»: he did not act on it before the chance came, but held it back until it did (al-Zawzanī)", " — cümle «açığa vurdu»ya ma'tûf: fırsat doğmadan harekete geçmedi; onu fırsat bulana dek erteledi (Zevzenî)"))])
# ---- v. 35 ----
VV(35, "He said: I will do what I have to do, and then guard myself from my enemy with a thousand bridled horses at my back.",
  "Dedi ki: Önce işimi göreceğim; sonra arkamda gemli bin atla düşmanımdan korunacağım.",
 [QALA_("وَقَالَ", HUSAYN, p=None),
  T("سَأَقْضِي", "qada-verb", "verb", ["mudari-marfu", "naqis-verbs", "al-fail-al-mudmar-al-mustatir-wujuban"],
     "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَأَقْضِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
     "The sin marks the future; أَقْضِي is a present verb in raf' by a damma estimated on the ya; the doer «I» must stay hidden — the clause is what he said, in the seat of nasb.",
     "Sîn istikbâl harfi; «akdî» yâ üzerinde takdîrî damme ile merfû muzâri; fâil vücûben gizli «ben» — cümle mekûlü'l-kavl, mahallen mansûb.",
     segs=SG(("سَ", "sa-istiqbal", "part"), ("أَقْضِي", "qada-verb", "verb"))),
  T("حَاجَتِي", "haja", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "al-bariz-al-muttasil"],
     "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — أَيْ مِنْ قَتْلِ قَاتِلِ أَخِي أَوْ كُفْءٍ لَهُ (الزَّوْزَنِيُّ).",
     "The direct object, in nasb by a fatha estimated on the letter before the ya of the speaker; annexed to that ya, in the seat of jarr — his «need» is to kill his brother's killer, or a man his equal (al-Zawzanī).",
     "Mef'ûlün bih; mütekellim yâ'sından önceki harf üzerinde takdîrî fetha ile mansûb; yâ'ya muzâf, yâ mahallen mecrûr — «işi», kardeşinin katilini yahut ona denk birini öldürmektir (Zevzenî).",
     segs=SG(("حَاجَتِ", "haja", "noun"), ("ي", "pron-1s", "pron"))),
  THUMMA(),
  T("أَتَّقِي", "ittaqa", "verb", ["mudari-marfu", "naqis-verbs", "form-viii-verbs", "atf-nasaq", "al-fail-al-mudmar-al-mustatir-wujuban"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مَعْطُوفٌ عَلَى «أَقْضِي»، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — أَيْ أَجْعَلُ بَيْنِي وَبَيْنَ عَدُوِّي وِقَايَةً.",
     "Present verb in raf' by a damma estimated on the ya, joined to «I will do»; the doer «I» must stay hidden — «I will put a shield between me and my enemy».",
     "Yâ üzerinde takdîrî damme ile merfû muzâri; «göreceğim»e ma'tûf; fâil vücûben gizli «ben» — yani «düşmanımla aramda bir siper edineceğim».")],
 [T("عَدُوِّي", "aduww", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "al-bariz-al-muttasil"],
     "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "The direct object, in nasb by a fatha estimated on the letter before the ya of the speaker; annexed to that ya, in the seat of jarr.",
     "Mef'ûlün bih; mütekellim yâ'sından önceki harf üzerinde takdîrî fetha ile mansûb; yâ'ya muzâf, yâ mahallen mecrûr.",
     segs=SG(("عَدُوِّ", "aduww", "noun"), ("ي", "pron-1s", "pron"))),
  BI_NOUN("بِأَلْفٍ", "alf", "أَلْفٍ", extra=["asma-al-adad-fil-kafiya", "ijaz-al-hadhf"], note_ar=" — وَالْبَاءُ لِلِاسْتِعَانَةِ، وَالْمَعْدُودُ مَحْذُوفٌ: أَلْفِ فَارِسٍ مُلْجِمٍ فَرَسَهُ، أَوْ أَلْفٍ مِنَ الْخَيْلِ (الزَّوْزَنِيُّ)؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَتَّقِي»", note_en=" — the ba of means; the thing counted is left out: «a thousand horsemen, their horses bridled», or «a thousand horses» (al-Zawzanī); the phrase hangs on «I will guard myself»", note_tr=" — bâ istiâne içindir; sayılan şey hazfedilmiştir: «atı gemli bin süvari» yahut «bin at» (Zevzenî); câr-mecrûr «korunacağım»a müteallik"),
  MIN(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«أَلْفٍ»", "; the jarr phrase hangs on an omitted na't of «a thousand»", " — câr-mecrûr «bin»in mahzûf na'tına müteallik")),
  T("وَرَائِيَ", "wara", "noun", ["huruf-jarr", "idafa-definiteness", "ya-al-mutakallim", "al-bariz-al-muttasil", "ism-mamdud"],
     "مَجْرُورٌ بِـ«مِنْ» بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "In jarr by مِنْ, with a kasra estimated on the letter before the ya of the speaker; annexed to that ya — here built on fatha — in the seat of jarr.",
     "«Min» ile mecrûr; mütekellim yâ'sından önceki harf üzerinde takdîrî kesre ile; yâ'ya muzâf; yâ burada fetha üzere mebnî, mahallen mecrûr.",
     segs=SG(("وَرَائِ", "wara", "noun"), ("يَ", "pron-1s", "pron"))),
  NAAT("مُلْجَمِ", "muljam", "jarr", extra=["ism-maful", "al-qafiya"], note_ar=" — نَعْتٌ لِـ«أَلْفٍ» عَلَى لَفْظِهِ؛ اسْمُ مَفْعُولٍ مِنْ أَلْجَمَ" + RAWI_J[0], note_en=" — a na't of «a thousand», after its form; the passive participle of أَلْجَمَ «to bridle»" + RAWI_J[1], note_tr=" — lafzına uyarak «bin»in na'tı; «elceme»den («gem vurdu») ism-i mef'ûl" + RAWI_J[2])])
# ---- v. 36 ----
VV(36, "Then he charged — and he startled no great number of tents — at the place where Death, the mother of Qashʿam, had thrown down her saddle.",
  "Sonra hamle etti — pek çok çadırı da ürkütmedi — Ümmü Kaş'am'ın (ölümün) yükünü indirdiği yerde.",
 [MADI("فَشَدَّ", "shadda", ["doubled-verbs"], hidden=True, note_ar=HUSAYN[0] + "؛ وَالشَّدَّةُ: الْحَمْلَةُ، أَيْ حَمَلَ عَلَى الرَّجُلِ الَّذِي رَامَ قَتْلَهُ بِأَخِيهِ", note_en=HUSAYN[1] + "; شَدَّة is a charge: he fell on the man he meant to kill for his brother", note_tr=HUSAYN[2] + "; «şedde»: hamle; kardeşine karşılık öldürmek istediği adamın üzerine atıldı"),
  LAM_JAZM("فَلَمْ"),
  T("يُفْزِعْ", "afzaa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-iv-verbs"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ" + HUSAYN[0] + " — وَالْإِفْزَاعُ: الْإِخَافَةُ؛ أَيْ لَمْ يَتَعَرَّضْ لِغَيْرِهِ. وَرِوَايَةُ الدُّرَّةِ «وَلَمْ» بِوَاوِ الْحَالِ.",
     "Present verb in jazm by لَمْ, its sign the sukun; the doer is the hidden «he»" + HUSAYN[1] + " — إِفْزَاع is frightening: he troubled no one else. Al-Durra reads وَلَمْ, with a waw that opens a hal.",
     "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli zamir «o»" + HUSAYN[2] + " — «ifzâ'»: korkutmak; yani başkasına ilişmedi. Dürre'nin rivayeti hâl vâvı ile «ve lem»dir."),
  MAFUL("بُيُوتًا", "bayt", extra=["jam-taksir"], note_ar=" — جَمْعُ بَيْتٍ", note_en=" — the plural of «tent, house»", note_tr=" — «beyt»in cem'i"),
  NAAT("كَثِيرَةً", "kathir", "nasb")],
 [T("لَدَى", "lada", "noun", ["maful-fih", "idafa-definiteness", "ism-maqsur-manqus"],
     "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُتَعَلِّقٌ بِـ«شَدَّ»، مُضَافٌ.",
     "An adverb of place, in nasb by a fatha estimated on the alif, hanging on «charged», and annexed.",
     "Mekân zarfı; elif üzerinde takdîrî fetha ile mansûb, «hamle etti»ye müteallik, muzâf."),
  T("حَيْثُ", "haythu", "noun", ["idafa-definiteness", "jaiz-al-bina-al-zuruf-al-mudafa-ila-al-jumla-wa-la-al-mukarrara-wa-sifat-ismiha"],
     "ظَرْفُ مَكَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَهُوَ مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
     "An adverb of place built on damma, in the seat of jarr as the second term of the idafa; it is itself annexed to the clause after it.",
     "Damme üzere mebnî mekân zarfı; muzâfun ileyh olarak mahallen mecrûr; kendisi de sonraki cümleye muzâftır."),
  T("أَلْقَتْ", "alqa", "verb", ["form-iv-verbs", "naqis-verbs", "istiara-makniyya"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ «أُمُّ قَشْعَمِ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ. وَفِيهِ اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَتِ الْمَنِيَّةُ بِمُسَافِرٍ نَزَلَ، ثُمَّ حُذِفَ الْمُشَبَّهُ بِهِ وَرُمِزَ إِلَيْهِ بِلَازِمِهِ وَهُوَ إِلْقَاءُ الرَّحْلِ: مُلْقَى الرَّحْلِ الْمَنْزِلُ لِأَنَّ الْمُسَافِرَ يُلْقِي بِهِ رَحْلَهُ، وَجَعَلَهُ مَنْزِلَ الْمَنِيَّةِ لِحُلُولِهَا ثَمَّ بِمَنْ قَتَلَهُ حُصَيْنٌ (الزَّوْزَنِيُّ).",
     "Past verb built on a fatha estimated on the alif, which dropped where two quiescents met; the ta marks the feminine; its doer is «the mother of Qashʿam» — the clause fills the seat of jarr after حَيْثُ. Here is an isti'ara makniyya: Death is likened to a traveller who has halted; the traveller is left unnamed and pointed to by what belongs to him — throwing down the saddle: where a saddle is thrown down is a halting-place, and he makes this Death's halting-place because she alighted there on the man Ḥuṣayn killed (al-Zawzanī).",
     "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; tâ te'nîs içindir; fâili «Ümmü Kaş'am»dır — cümle «haysü»ye muzâfun ileyh olarak mahallen mecrûr. Burada istiâre-i mekniyye vardır: ölüm, konaklayan bir yolcuya benzetilmiş, müşebbehün bih hazfedilmiş ve ona lâzımıyla — semeri indirmekle — işaret edilmiştir: semerin indirildiği yer konaktır; Husayn'ın öldürdüğü kimseye orada indiği için orayı ölümün konağı kılmıştır (Zevzenî)."),
  ENC_NOUN("رَحْلَهَا", "rahl", "هَا", "maful"),
  PH(FAIL("أُمُّ", "umm", extra=["idafa-definiteness", "kinaya", "aqsam-al-kinaya"], note_ar="، مُضَافٌ — فَاعِلُ «أَلْقَتْ»؛ وَ«أُمُّ قَشْعَمٍ» كُنْيَةُ الْمَنِيَّةِ (الزَّوْزَنِيُّ)، فَهِيَ كِنَايَةٌ عَنْ مَوْصُوفٍ", note_en=", annexed — the doer of «threw down»; «the mother of Qashʿam» is a kunya of Death (al-Zawzanī), and so a kinaya for a thing described", note_tr=", muzâf — «indirdi»nin fâili; «Ümmü Kaş'am» ölümün künyesidir (Zevzenî); dolayısıyla mevsûftan kinâyedir"), "umm-qasham"),
  MUDAF_ILAYH("قَشْعَمِ", "qasham", "noun", ["al-qafiya"], note_ar=" — وَالْقَشْعَمُ: النَّسْرُ الْمُسِنُّ" + RAWI_J[0], note_en=" — قَشْعَم is an old vulture" + RAWI_J[1], note_tr=" — «kaş'am»: yaşlı akbaba" + RAWI_J[2])])
# ---- v. 37 ----
VV(37, "— beside a lion bristling with weapons, one hurled again and again into battle, heavy-maned, his claws never clipped.",
  "— silahı tam, savaşlara atılıp duran, yeleli ve pençeleri hiç kesilmemiş bir aslanın yanında.",
 [T("لَدَى", "lada", "noun", ["maful-fih", "idafa-definiteness", "ism-maqsur-manqus"],
     "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُتَعَلِّقٌ بِـ«شَدَّ» فِي الْبَيْتِ قَبْلَهُ — أَوْ بَدَلٌ مِنْ «لَدَى» الْأُولَى (الدُّرَّةُ) — مُضَافٌ.",
     "An adverb of place, in nasb by a fatha estimated on the alif, hanging on «charged» in the verse before — or a badal of the first لَدَى (al-Durra) — and annexed.",
     "Mekân zarfı; elif üzerinde takdîrî fetha ile mansûb; önceki beyitteki «hamle etti»ye müteallik — yahut ilk «ledâ»dan bedel (Dürre) — muzâf."),
  MUDAF_ILAYH("أَسَدٍ", "asad", extra=["istiara", "arkan-al-istiara", "tarshih-wa-tajrid"], note_ar=". وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ أَصْلِيَّةٌ: اسْتُعِيرَ الْأَسَدُ لِلرَّجُلِ الشُّجَاعِ — وَهُوَ حُصَيْنٌ، وَالْبَيْتُ كُلُّهُ مِنْ صِفَتِهِ (الزَّوْزَنِيُّ). وَبِهٰذَا الْبَيْتِ مَثَّلَ صَاحِبُ التَّلْخِيصِ لِاجْتِمَاعِ التَّجْرِيدِ وَالتَّرْشِيحِ: «شَاكِي السِّلَاحِ مُقَذَّفٍ» يُلَائِمُ الْمُسْتَعَارَ لَهُ فَهُوَ تَجْرِيدٌ، وَ«لَهُ لِبَدٌ أَظْفَارُهُ لَمْ تُقَلَّمِ» يُلَائِمُ الْمُسْتَعَارَ مِنْهُ فَهُوَ تَرْشِيحٌ", note_en=". Here is an isti'ara tasrihiyya asliyya: «lion» is lent to the brave man — Ḥuṣayn himself; the whole verse describes him (al-Zawzanī). It is the verse the Talkhīṣ cites for tajrid and tarshih together: «bristling with weapons, hurled into battle» suits the man, the thing the word is lent to — that is tajrid; «he has a mane, his claws unclipped» suits the lion, the thing it is borrowed from — that is tarshih", note_tr=". Burada istiâre-i tasrîhiyye-i asliyye vardır: «aslan» cesur adam için — bizzat Husayn için — ödünç alınmıştır; beytin tamamı onun vasfıdır (Zevzenî). Telhîs sahibi tecrîd ile terşîhin bir arada bulunmasına bu beyti misal verir: «silahı tam, savaşa atılan» müsteârun lehe (adama) uygun olduğundan tecrîd; «yelesi var, pençeleri kesilmemiş» müsteârun minhe (aslana) uygun olduğundan terşîhtir"),
  T("شَاكِي", "shaki", "noun", ["naat-sifa", "ism-maqsur-manqus", "idafa-definiteness", "idafa-lafziyya", "tarshih-wa-tajrid"],
     "نَعْتٌ لِـ«أَسَدٍ» مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مُضَافٌ إِضَافَةً لَفْظِيَّةً — شَاكِي السِّلَاحِ وَشَائِكُهُ: تَامُّ السِّلَاحِ، مِنَ الشَّوْكَةِ وَهِيَ الْعُدَّةُ وَالْقُوَّةُ؛ وَهُوَ تَجْرِيدٌ.",
     "A na't of «a lion», in jarr by a kasra estimated on the ya, annexed in wording only — شَاكِي السِّلَاحِ, also شَائِك, is «fully armed», from شَوْكَة «arms and strength»; it is the tajrid.",
     "«Aslan»ın na'tı; yâ üzerinde takdîrî kesre ile mecrûr; izâfeti lafzîdir — «şâki's-silâh» (şâikü's-silâh da denir): silahı tam; «şevke»den («teçhizat ve kuvvet»); tecrîddir."),
  MUDAF_ILAYH("السِّلَاحِ", "silah"),
  NAAT("مُقَذَّفٍ", "muqadhdhaf", "jarr", extra=["ism-maful", "tarshih-wa-tajrid"], note_ar=" — نَعْتٌ ثَانٍ لِـ«أَسَدٍ»: يُقْذَفُ بِهِ كَثِيرًا إِلَى الْوَقَائِعِ، وَالتَّقْذِيفُ مُبَالَغَةُ الْقَذْفِ", note_en=" — a second na't of «a lion»: one flung again and again into battles; تَقْذِيف is the intensive of قَذْف", note_tr=" — «aslan»ın ikinci na'tı: savaşlara çokça atılan; «takzîf», «kazf»ın mübalağasıdır")],
 [LAHU2("لَهُ", "pron-3ms", " («onun»)", grammar=["taqdim-al-musnad", "jumla-sifa"], note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَالِثٌ لِـ«أَسَدٍ»", "; the phrase hangs on the omitted, fronted khabar, and the nominal clause is a third na't of «a lion», in the seat of jarr", "; câr-mecrûr öne alınmış mahzûf habere müteallik; isim cümlesi «aslan»ın üçüncü na'tı, mahallen mecrûr")),
  MUBTADA("لِبَدٌ", "libad", extra=["jam-taksir", "tarshih-wa-tajrid"], note_ar=" — مُبْتَدَأٌ مُؤَخَّرٌ؛ جَمْعُ لِبْدَةٍ: مَا تَلَبَّدَ مِنْ شَعْرِ الْأَسَدِ عَلَى مَنْكِبَيْهِ؛ وَهُوَ تَرْشِيحٌ", note_en=" — placed after its khabar; the plural of لِبْدَة, the matted hair on a lion's shoulders; it is the tarshih", note_tr=" — haberinden sonraya bırakılmıştır; «libde»nin cem'i: aslanın omuzlarındaki keçeleşmiş tüy; terşîhtir"),
  ENC_NOUN("أَظْفَارُهُ", "zufr", "هُ", "mubtada", extra=["jam-taksir", "jumla-sifa"], note_ar=" — جَمْعُ ظُفْرٍ؛ وَالْجُمْلَةُ الِاسْمِيَّةُ نَعْتٌ آخَرُ لِـ«أَسَدٍ»", note_en=" — the plural of ظُفْر «claw»; the nominal clause is a further na't of «a lion»", note_tr=" — «zufr»un («pençe») cem'i; isim cümlesi «aslan»ın bir başka na'tıdır"),
  LAM_JAZM("لَمْ"),
  T("تُقَلَّمِ", "qallama", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-ii-verbs", "naib-al-fail", "al-majhul-fil-kafiya", "al-qafiya", "anwa-al-khabar", "tarshih-wa-tajrid"],
     "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["rawi"][0] + "، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْأَظْفَارِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَظْفَارُهُ»؛ يُرِيدُ أَنَّهُ لَا يَعْتَرِيهِ ضَعْفٌ كَمَا أَنَّ الْأَسَدَ لَا تُقَلَّمُ بَرَاثِنُهُ (الزَّوْزَنِيُّ).",
     "A present verb in the passive, in jazm by لَمْ, its sign " + SGN["rawi"][1] + "; its deputy doer is the hidden «they» — the claws — and the clause is the khabar of «his claws», in the seat of raf'; he means that no weakness comes over him, as a lion's talons are never clipped (al-Zawzanī).",
     "Lem ile meczûm meçhul muzâri, alâmeti " + SGN["rawi"][2] + "; nâib-i fâil pençelere dönen gizli zamir — cümle «pençeleri»nin haberi, mahallen merfû; aslanın pençeleri kesilmediği gibi ona da zaaf ârız olmaz, demek ister (Zevzenî).")])
# ---- v. 38 ----
VV(38, "— bold: whenever he is wronged he pays the wrong back at once; and if he is not attacked first, he does the wrong himself.",
  "— cüretkâr: ne zaman zulme uğrasa zulmünün karşılığını hemen verir; kendisine önce zulmedilmezse o zulmeder.",
 [NAAT("جَرِيءٍ", "jari-bold", "jarr", extra=["sifa-mushabbaha"], note_ar=" — نَعْتٌ آخَرُ لِـ«أَسَدٍ» فِي الْبَيْتِ قَبْلَهُ، وَيَجُوزُ رَفْعُهُ خَبَرًا لِمُبْتَدَأٍ مَحْذُوفٍ (الدُّرَّةُ)", note_en=" — a further na't of «a lion» in the verse before; it may also be read in raf', as the khabar of an omitted mubtada (al-Durra)", note_tr=" — önceki beyitteki «aslan»ın bir başka na'tı; mahzûf mübtedânın haberi olarak ref'i de caizdir (Dürre)"),
  T("مَتَى", "mata", "part", G_SHART + ["maful-fih", "jumla-sifa"],
     "اسْمُ شَرْطٍ جَازِمٌ يَجْزِمُ فِعْلَيْنِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ مُتَعَلِّقٌ بِفِعْلِ الشَّرْطِ — فِعْلُ الشَّرْطِ «يُظْلَمْ» وَجَوَابُهُ «يُعَاقِبْ»، وَكِلَاهُمَا مَجْزُومٌ بِالسُّكُونِ؛ وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«أَسَدٍ».",
     "A conditional noun that puts two verbs in jazm, built on sukun in the seat of nasb as an adverb of time hanging on the condition's verb — the condition is «he is wronged» and the answer «he pays back», each in jazm by the sukun; the conditional sentence is a na't of «a lion», in the seat of jarr.",
     "İki fiili cezmeden şart ismi; sükûn üzere mebnî, zaman zarfı olarak mahallen mansûb, şart fiiline müteallik — şart fiili «zulme uğrarsa», cevabı «karşılık verir»; ikisi de sükûn ile meczûm; şart cümlesi cevabıyla birlikte «aslan»ın na'tı, mahallen mecrûr."),
  JV("يُظْلَمْ", "zalama", "shart", "sukun", g=["naib-al-fail", "al-majhul-fil-kafiya", "mulhaq-bil-jinas", "radd-al-ajuz"], passive=True, doer=NF("هُوَ يَعُودُ عَلَى «أَسَدٍ»", "«he» — the lion", "«aslan»a dönen gizli zamir"),
     note=(" — وَبَيْنَهُ وَبَيْنَ «يَظْلِمِ» فِي آخِرِ الْبَيْتِ اشْتِقَاقٌ، وَهُوَ مِنْ رَدِّ الْعَجُزِ عَلَى الصَّدْرِ: أَحَدُهُمَا فِي حَشْوِ الْمِصْرَاعِ الْأَوَّلِ وَالْآخَرُ فِي آخِرِ الْبَيْتِ", " — it shares a root with يَظْلِمِ at the close of the verse, and the two make a radd al-'ajuz 'ala al-sadr: one stands inside the first hemistich, the other ends the verse", " — beytin sonundaki «yazlim» ile arasında iştikâk vardır; bu aynı zamanda reddü'l-acüz ale's-sadrdır: biri ilk mısraın içinde, diğeri beytin sonundadır")),
  JV("يُعَاقِبْ", "aqaba", "jawab", "sukun", g=["form-iii-verbs", "hadhf-al-maful"], doer=FH("هُوَ، وَالْمَفْعُولُ مَحْذُوفٌ أَيِ الظَّالِمَ", "«he»; its object — the wrongdoer — is left out", "gizli zamir «o»; mef'ûlü — zâlim — mahzûf")),
  BI_NOUN("بِظُلْمِهِ", "zulm", "ظُلْمِهِ", enc="هِ", extra=["mulhaq-bil-jinas"], note_ar=" — وَالْبَاءُ لِلْمُقَابَلَةِ: يُعَاقِبُ الظَّالِمَ بِظُلْمِهِ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُعَاقِبْ»", note_en=" — the ba of return: he punishes the wrongdoer for his wrong; the phrase hangs on «pays back»", note_tr=" — bâ mukabele içindir: zâlimi zulmüne karşılık cezalandırır; câr-mecrûr «karşılık verir»e müteallik")],
 [T("سَرِيعًا", "sari", "noun", ["maful-mutlaq", "hal", "sifa-mushabbaha"],
     "نَعْتٌ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ نَابَ عَنْهُ: يُعَاقِبْ عِقَابًا سَرِيعًا، مَنْصُوبٌ بِالْفَتْحَةِ؛ أَوْ حَالٌ بِمَعْنَى مُسْرِعًا (الدُّرَّةُ).",
     "A na't of an omitted maf'ul mutlaq, standing in for it — «he pays back a swift paying» — in nasb; or a hal, «making haste» (al-Durra).",
     "Mahzûf mef'ûl-i mutlakın na'tı olup onun yerine geçmiştir: «süratli bir karşılıkla karşılık verir», mansûb; yahut «acele ederek» anlamında hâl (Dürre)."),
  T("وَإِلَّا", "in-shartiyya", "part", ["in-shartiyya", "al-majzum-wal-shart-wal-jaza", "la-nafiya", "atf-nasaq"],
     WA_AR + "إِلَّا أَصْلُهَا «إِنْ لَا»: إِنْ حَرْفُ شَرْطٍ جَازِمٌ أُدْغِمَتْ نُونُهُ فِي اللَّامِ، وَلَا نَافِيَةٌ — فِعْلُ الشَّرْطِ «يُبْدَ» وَجَوَابُهُ «يَظْلِمِ».",
     "The waw conjoins; إِلَّا is إِنْ لَا — the conditional إِنْ, its nun merged into the lam, and the negating لَا — the condition is «he is attacked first» and the answer «he wrongs».",
     "«ve» + illâ: aslı «in lâ»dır — cezmeden şart harfi «in» (nûnu lâma idgam edilmiştir) ve nâfiye «lâ» — şart fiili «kendisine başlanırsa», cevabı «zulmeder».",
     segs=SG(("وَ", "wa", "conj"), ("إِنْ", "in-shartiyya", "part"), ("لَا", "la-nafiya", "part"))),
  JV("يُبْدَ", "badaa", "shart", "alif", g=["naib-al-fail", "al-majhul-fil-kafiya", "in-shartiyya"], passive=True, doer=NF("هُوَ", "«he»", "gizli zamir «o»"),
     note=(" — وَأَصْلُهُ يُبْدَأْ بِالْهَمْزِ: قُلِبَتِ الْهَمْزَةُ أَلِفًا ثُمَّ حُذِفَتْ لِلْجَازِمِ (الزَّوْزَنِيُّ)، وَهُوَ ضَرُورَةٌ", " — it is يُبْدَأْ, with hamza: the hamza is turned to alif, and the alif then dropped for the jazm (al-Zawzanī) — a poet's licence", " — aslı hemzeli «yübde'»dir: hemze elife çevrilmiş, sonra câzim sebebiyle elif hazfedilmiştir (Zevzenî) — zarûrettir")),
  BI_NOUN("بِالظُّلْمِ", "zulm", "الظُّلْمِ", extra=["mulhaq-bil-jinas"], **W(MT("يُبْدَ", "is attacked first", "başlanırsa»ya"))),
  JV("يَظْلِمِ", "zalama", "jawab", "rawi", g=["in-shartiyya", "mulhaq-bil-jinas", "radd-al-ajuz"], doer=FH("هُوَ", "«he»", "gizli zamir «o»"),
     note=(" — أَيْ: وَإِنْ لَمْ يَظْلِمْهُ أَحَدٌ ظَلَمَ النَّاسَ إِظْهَارًا لِغَنَائِهِ وَحُسْنِ بَلَائِهِ (الزَّوْزَنِيُّ)", " — that is, if no one wrongs him he wrongs others, to show his worth and his prowess (al-Zawzanī)", " — yani kimse ona zulmetmezse, gücünü ve yararlığını göstermek için o insanlara zulmeder (Zevzenî)"))])
# ---- v. 39 ----
VV(39, "They grazed out their time between waterings; then, when it was done, they brought their herds down to deep pools that split open with weapons and with blood.",
  "İki sulama arasındaki sürelerini otlattılar; süre dolunca (develerini) silahla ve kanla yarılan derin sulara indirdiler.",
 [T("رَعَوْا", "raa-graze", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail", "majaz-murakkab"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ. وَهٰذَا كُلُّهُ اسْتِعَارَةٌ — تَمْثِيلِيَّةٌ تَمْتَدُّ إِلَى الْبَيْتِ بَعْدَهُ: شُبِّهَتْ حَالُهُمْ فِي كَفِّهِمْ عَنِ الْقِتَالِ مُدَّةً ثُمَّ عَوْدِهِمْ إِلَى الْوَقَائِعِ بِحَالِ مَنْ يَرْعَى إِبِلَهُ مُدَّةً ثُمَّ يُورِدُهَا، فَالْحُرُوبُ بِمَنْزِلَةِ الْغِمَارِ (الزَّوْزَنِيُّ).",
     "Past verb built on a fatha estimated on the alif, which dropped where two quiescents met; the waw is the doer, in the seat of raf' — a new sentence. All of this is isti'ara — an isti'ara of tamthil that runs on into the next verse: their holding off from fighting for a while and then returning to battle is likened to a man's grazing his camels for a while and then bringing them down to water; the wars stand as the deep pools (al-Zawzanī).",
     "İki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; vâv fâil, mahallen merfû — cümle müste'nefedir. Bunların hepsi istiâredir — sonraki beyte uzanan istiâre-i temsîliyye: bir süre savaştan el çekip sonra yeniden çarpışmaya dönmeleri, develerini bir süre otlatıp sonra suya indiren kimsenin haline benzetilmiştir; harpler derin sular yerindedir (Zevzenî).",
     segs=SG(("رَعَ", "raa-graze", "verb"), ("وْا", "pron-3mp", "pron"))),
  ENC_NOUN("ظِمْأَهُمْ", "zim", "هُمْ", "maful", note_ar=" — وَالظِّمْءُ: مَا بَيْنَ الْوِرْدَيْنِ؛ وَالْمَعْنَى: رَعَوْا إِبِلَهُمُ الْكَلَأَ مُدَّةَ ظِمْئِهِمْ (الزَّوْزَنِيُّ)", note_en=" — ظِمْء is the stretch between two waterings; the sense: they grazed their camels for the length of it (al-Zawzanī)", note_tr=" — «zım'»: iki sulama arasındaki süre; mânâ: develerini o süre boyunca otlattılar (Zevzenî)"),
  T("حَتَّى", "hatta", "part", ["ila-hatta-fi-wal-ba-fil-kafiya"], "حَرْفُ ابْتِدَاءٍ لَا عَمَلَ لَهُ.", "حَتَّى here opens a new clause and governs nothing.", "İbtidâ harfi; ameli yoktur."),
  T("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ بِجَوَابِهِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb for time to come that carries the sense of a condition, built on sukun in the seat of nasb by its answer, and annexed to the clause after it.", "Şart mânâsı taşıyan gelecek zaman zarfı; sükûn üzere mebnî, cevabı ile mahallen mansûb; sonraki cümleye muzâf."),
  MADI("تَمَّ", "tamma", ["doubled-verbs"], note_ar="، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الظِّمْءِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the doer is the hidden «it» — the time between waterings — and the clause fills the seat of jarr after إِذَا", note_tr="; fâil süreye dönen gizli zamir — cümle «izâ»ya muzâfun ileyh olarak mahallen mecrûr"),
  VERB_WAW("أَوْرَدُوا", "awrada", ["form-iv-verbs", "mithal-verbs", "hadhf-al-maful"], note_ar=" — وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ، وَالْمَفْعُولُ الْأَوَّلُ مَحْذُوفٌ: أَوْرَدُوا إِبِلَهُمْ", note_en=" — the clause is the answer of إِذَا and has no seat; its first object is left out: «they brought [their camels] down»", note_tr=" — cümle «izâ»nın cevabıdır, mahalli yoktur; birinci mef'ûl mahzûf: «[develerini] indirdiler»")],
 [MAFUL("غِمَارًا", "ghamr", extra=["jam-taksir"], note_ar=" — جَمْعُ غَمْرٍ: الْمَاءُ الْكَثِيرُ", note_en=" — the plural of غَمْر, deep and plentiful water", note_tr=" — «gamr»ın cem'i: bol ve derin su"),
  T("تَفَرَّى", "tafarra", "verb", ["mudari-marfu", "naqis-verbs", "form-v-verbs", "jumla-sifa"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — وَأَصْلُهُ تَتَفَرَّى فَحُذِفَتْ إِحْدَى التَّاءَيْنِ — وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْغِمَارِ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«غِمَارًا». وَالتَّفَرِّي: التَّشَقُّقُ؛ أَيْ تَنْشَقُّ عَنْهُمْ بِاسْتِعْمَالِ السِّلَاحِ وَسَفْكِ الدِّمَاءِ (الزَّوْزَنِيُّ)؛ وَيُرْوَى «تَسِيلُ» (الدُّرَّةُ).",
     "Present verb in raf' by a damma estimated on the alif — it is تَتَفَرَّى with one of its two ta's dropped — the doer is the hidden «they» (the pools), and the clause is a na't of «pools», in the seat of nasb. تَفَرٍّ is splitting open: the pools part before them by the use of weapons and the shedding of blood (al-Zawzanī); also read تَسِيلُ «flow» (al-Durra).",
     "Elif üzerinde takdîrî damme ile merfû muzâri — aslı «tetefarrâ»dır, iki tâ'dan biri hazfedilmiştir — fâil sulara dönen gizli zamir; cümle «sular»ın na'tı, mahallen mansûb. «Teferrî»: yarılmak; yani silah kullanmak ve kan dökmekle önlerinde yarılır (Zevzenî); «tesîlü» («akar») diye de rivayet edilir (Dürre)."),
  BI_NOUN("بِالسِّلَاحِ", "silah", "السِّلَاحِ", **W(MT("تَفَرَّى", "split open", "yarılır»a"))),
  T("وَبِالدَّمِ", "bi", "prep", ["huruf-jarr", "atf-nasaq", "al-qafiya"], WA_AR + "الْبَاءُ حَرْفُ جَرٍّ، وَالدَّمِ مَجْرُورٌ بِالْكَسْرَةِ — مَعْطُوفَانِ عَلَى «بِالسِّلَاحِ»" + RAWI_AL[0] + ".", "The waw conjoins; the ba is a jarr letter and «blood» is in jarr — joined to «with weapons»" + RAWI_AL[1] + ".", "«ve» + bâ cer harfi; «kan» mecrûr — «silahla»ya ma'tûf" + RAWI_AL[2] + ".",
     segs=SG(("وَ", "wa", "conj"), ("بِ", "bi", "prep"), ("الدَّمِ", "dam", "noun")))])
# ---- v. 40 ----
VV(40, "So they dealt out deaths among themselves to the full, and then drove back to a pasture found foul and unwholesome.",
  "Böylece aralarında ölümleri tamamına erdirdiler; sonra ağır ve sağlığa zararlı bulunan bir otlağa geri döndürdüler.",
 [T("فَقَضَّوْا", "qadda-fulfil", "verb", ["form-ii-verbs", "naqis-verbs", "al-bariz-al-muttasil", "fail", "atf-nasaq", "majaz-murakkab"],
     FA_AR + "قَضَّوْا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «رَعَوْا». قَضَيْتُ الشَّيْءَ وَقَضَّيْتُهُ: أَحْكَمْتُهُ وَأَتْمَمْتُهُ؛ أَيْ قَتَلَ كُلُّ وَاحِدٍ مِنَ الْحَيَّيْنِ صِنْفًا مِنَ الْآخَرِ (الزَّوْزَنِيُّ).",
     "The fa conjoins; قَضَّوْا is a past verb built on a fatha estimated on the alif, which dropped where two quiescents met; the waw is the doer — the clause is joined to «they grazed». قَضَى and قَضَّى a thing is to finish and make it sure: each tribe killed its share of the other (al-Zawzanī).",
     "«fe» + «tamamladılar»: iki sâkin karşılaştığı için düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; vâv fâildir — cümle «otlattılar»a ma'tûf. «Kadâ» ve «kaddâ»: bir şeyi sağlama alıp tamamlamak; yani iki kabilenin her biri ötekinden bir kısmını öldürdü (Zevzenî).",
     segs=SG(("فَ", "fa", "conj"), ("قَضَّ", "qadda-fulfil", "verb"), ("وْا", "pron-3mp", "pron"))),
  MAFUL("مَنَايَا", "maniyya", extra=["jam-taksir", "ism-maqsur-manqus", "mamnu-min-sarf"], sign="بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_en=" — by a fatha estimated on the alif", note_tr=" — elif üzerinde takdîrî fetha ile"),
  T("بَيْنَهُمْ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil"],
     "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِـ«قَضَّوْا» أَوْ بِمَحْذُوفٍ نَعْتٍ لِـ«مَنَايَا» (الدُّرَّةُ)، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
     "An adverb of place, in nasb, hanging on «dealt out», or on an omitted na't of «deaths» (al-Durra); annexed to the attached «them», in the seat of jarr.",
     "Mekân zarfı, mansûb; «tamamladılar»a yahut «ölümler»in mahzûf na'tına müteallik (Dürre); bitişik zamire muzâf, zamir mahallen mecrûr.",
     segs=SG(("بَيْنَ", "bayna", "noun"), ("هُمْ", "pron-3mp", "pron"))),
  THUMMA(),
  VERB_WAW("أَصْدَرُوا", "asdara", ["form-iv-verbs", "hadhf-al-maful", "tibaq"], note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا، وَالْمَفْعُولُ مَحْذُوفٌ: أَصْدَرُوا إِبِلَهُمْ. أَصْدَرَ ضِدُّ أَوْرَدَ، فَبَيْنَهُ وَبَيْنَ «أَوْرَدُوا» فِي الْبَيْتِ قَبْلَهُ طِبَاقٌ", note_en=" — the clause is joined to what goes before; its object is left out: «they drove [their camels] back». أَصْدَرَ is the opposite of أَوْرَدَ, so it makes a tibaq with «brought down» in the verse before", note_tr=" — cümle öncesine ma'tûf; mef'ûlü mahzûf: «[develerini] geri çevirdiler». «Asdera», «evrade»nin zıddıdır; önceki beyitteki «indirdiler» ile arasında tıbâk vardır")],
 [PREP("إِلَى", "ila", role_ar=MT("أَصْدَرُوا", "", "")[0], role_en="; the phrase hangs on «drove back»", role_tr="; câr-mecrûr «geri çevirdiler»e müteallik", gloss_tr="«-e»"),
  MAJR("كَلَإٍ", "kala", extra=["istiara", "majaz-murakkab"], note_ar=" — وَالْكَلَأُ: الْعُشْبُ. جَعَلَ اعْتِزَامَهُمْ عَلَى الْحَرْبِ ثَانِيَةً وَالِاسْتِعْدَادَ لَهَا بِمَنْزِلَةِ كَلَإٍ وَبِيلٍ وَخِيمٍ (الزَّوْزَنِيُّ)، وَهُوَ تَمَامُ الِاسْتِعَارَةِ التَّمْثِيلِيَّةِ", note_en=" — كَلَأ is herbage, pasture. He makes their resolve to fight again, and their making ready for it, stand as a foul and unwholesome pasture (al-Zawzanī) — which completes the isti'ara of tamthil", note_tr=" — «kele'»: ot, otlak. Yeniden savaşa azmetmelerini ve ona hazırlanmalarını ağır ve zararlı bir otlak yerine koymuştur (Zevzenî) — istiâre-i temsîliyye bununla tamamlanır"),
  NAAT("مُسْتَوْبَلٍ", "mustawbal", "jarr", extra=["ism-maful"], note_ar=" — اسْمُ مَفْعُولٍ مِنِ اسْتَوْبَلَ: اسْتَوْبَلْتُ الشَّيْءَ وَجَدْتُهُ وَبِيلًا، وَالْوَبِيلُ الَّذِي لَا يُسْتَمْرَأُ (الزَّوْزَنِيُّ) — وَضُبِطَ فِي الْمَطْبُوعِ بِكَسْرِ الْبَاءِ", note_en=" — the passive participle of اِسْتَوْبَلَ: «I found the thing وَبِيل», heavy and not to be digested (al-Zawzanī) — the edition prints it with kasra on the ba", note_tr=" — «istevbele»den ism-i mef'ûl: «bir şeyi vebîl (ağır, hazmedilmez) buldum» (Zevzenî) — baskıda bâ'nın kesresiyle harekelenmiştir"),
  NAAT("مُتَوَخَّمِ", "mutawakhkham", "jarr", extra=["ism-maful", "al-qafiya"], note_ar=" — نَعْتٌ ثَانٍ لِـ«كَلَإٍ»؛ اسْمُ مَفْعُولٍ مِنْ تَوَخَّمَ: تَوَخَّمْتُهُ وَاسْتَوْخَمْتُهُ وَجَدْتُهُ وَخِيمًا (الزَّوْزَنِيُّ)" + RAWI_J[0], note_en=" — a second na't of «pasture»; the passive participle of تَوَخَّمَ: «I found it وَخِيم», unwholesome (al-Zawzanī)" + RAWI_J[1], note_tr=" — «otlak»ın ikinci na'tı; «tevahhame»den ism-i mef'ûl: «onu vahîm (sağlığa zararlı) buldum» (Zevzenî)" + RAWI_J[2])])
# =====================================================================================================================
# vv. 41–45 — عَاقِلُو الْقَتْلَى
# =====================================================================================================================
VV(41, "By your life, their spears brought on them no guilt for the blood of Ibn Nahīk, nor for the man slain at al-Muthallam,",
  "Ömrüne yemin olsun ki, onların mızrakları kendilerine ne İbn Nehîk'in kanını yükledi ne de Müsellem maktulünün kanını,",
 [T("لَعَمْرُكَ", "amr-qasam", "noun", ["huruf-al-qasam-fil-kafiya", "mubtada-khabar", "khabar-insha", "al-bariz-al-muttasil"],
     "اللَّامُ لَامُ الِابْتِدَاءِ، وَعَمْرُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَخَبَرُهُ مَحْذُوفٌ وُجُوبًا تَقْدِيرُهُ: قَسَمِي؛ أَيْ: أُقْسِمُ بِبَقَائِكَ وَحَيَاتِكَ (الزَّوْزَنِيُّ).",
     "The lam is the lam of beginning; «life» is a mubtada, in raf'; it is annexed to the attached «your», in the seat of jarr — and its khabar must be left out: «[is my oath]»; that is, «I swear by your life» (al-Zawzanī).",
     "Lâm ibtidâ lâmıdır; «ömr» mübtedâ, merfû; bitişik kâfa muzâf, kâf mahallen mecrûr — haberi vücûben mahzûftur: «yeminimdir»; yani «bekâna ve hayatına yemin ederim» (Zevzenî).",
     segs=SG(("لَ", "lam-ibtida", "part"), ("عَمْرُ", "amr-qasam", "noun"), ("كَ", "pron-2ms", "pron"))),
  T("مَا", "ma-nafiya", "part", ["huruf-al-qasam-fil-kafiya"], "مَا نَافِيَةٌ لَا عَمَلَ لَهَا، وَبِهَا يُتَلَقَّى الْقَسَمُ فِي النَّفْيِ.", "مَا negates and governs nothing; it is what an oath is answered with when the answer is a denial.", "«mâ» nâfiyedir, amel etmez; cevabı menfî olan yemin onunla karşılanır."),
  MADI("جَرَّتْ", "jarra", ["doubled-verbs"], fem=True, note_ar=FAIL_BAAD[0] + " — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ أَيْ: لَمْ تَجْنِ عَلَيْهِمْ رِمَاحُهُمْ دِمَاءَ هٰؤُلَاءِ، لَمْ يَسْفِكُوهَا وَلَمْ يُشَارِكُوا قَاتِلِيهِمْ (الزَّوْزَنِيُّ)", note_en=FAIL_BAAD[1] + " — the clause is the answer of the oath and has no seat; that is, their spears did not bring on them the blood of these men: they neither shed it nor had part with the killers (al-Zawzanī)", note_tr=FAIL_BAAD[2] + " — cümle yeminin cevabıdır, mahalli yoktur; yani mızrakları bu kimselerin kanını onlara yüklemedi: ne döktüler ne de katillere ortak oldular (Zevzenî)"),
  JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onlara»)", note_ar=" — أَيْ عَلَى الَّذِينَ يَعْقِلُونَ الْقَتْلَى؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَرَّتْ»", note_en="; «them» is those who pay for the slain; the phrase hangs on «brought»", note_tr="; «onlar» diyetleri ödeyenlerdir; câr-mecrûr «getirdi»ye müteallik"),
  ENC_NOUN("رِمَاحُهُمْ", "rumh", "هُمْ", "fail", extra=["jam-taksir"], note_ar=" — جَمْعُ رُمْحٍ", note_en=" — the plural of «spear»", note_tr=" — «rumh»un cem'i")],
 [MAFUL("دَمَ", "dam", **W(MUD)),
  MUDAF_ILAYH("ابْنِ", "ibn", note_ar="، مُضَافٌ", note_en=", itself annexed", note_tr=", kendisi de muzâf"),
  MUDAF_ILAYH("نَهِيكٍ", "nahik", "propn", note_ar=" — ابْنُ نَهِيكٍ: أَحَدُ الْقَتْلَى", note_en=" — Ibn Nahīk is one of the slain", note_tr=" — İbn Nehîk öldürülenlerden biridir"),
  T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «veya»."),
  T("قَتِيلِ", "qatil-slain", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى «ابْنِ نَهِيكٍ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — فَعِيلٌ بِمَعْنَى مَفْعُولٍ.", "Joined to «Ibn Nahīk», in jarr, and annexed — a فَعِيل in the sense of the passive participle: «the slain man».", "«İbn Nehîk»e ma'tûf, mecrûr, muzâf — mef'ûl anlamında faîl: «maktul»."),
  MUDAF_ILAYH("الْمُثَلَّمِ", "muthallam", "propn", ["al-qafiya"], note_ar=" — مَوْضِعٌ" + RAWI_AL[0], note_en=" — a place" + RAWI_AL[1], note_tr=" — bir yer" + RAWI_AL[2])])
# ---- v. 42 ----
VV(42, "nor had they any share in the death — in the blood of Nawfal, nor of Wahab, nor of Ibn al-Mukhazzam.",
  "ne de ölümde — ne Nevfel'in, ne Vehb'in, ne de İbnü'l-Muhazzem'in kanında — ortak oldular.",
 [T("وَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq", "huruf-al-ziyada-fil-kafiya"], WA_AR + "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to strengthen the negation.", "«ve» + nefyi te'kîd eden zâid «lâ».",
     segs=SG(("وَ", "wa", "conj"), ("لَا", "la-nafiya", "part"))),
  MADI("شَارَكَتْ", "sharaka", ["form-iii-verbs"], fem=True, note_ar="، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الرِّمَاحِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «مَا جَرَّتْ» فِي الْبَيْتِ قَبْلَهُ؛ وَتَأْنِيثُ الْفِعْلِ لِلرِّمَاحِ (الزَّوْزَنِيُّ)", note_en="; the doer is the hidden «they» — the spears — and the clause is joined to «did not bring» in the verse before; the verb is feminine for the spears (al-Zawzanī)", note_tr="; fâil mızraklara dönen gizli zamir — cümle önceki beyitteki «getirmedi»ye ma'tûf; fiilin müennesliği mızraklar içindir (Zevzenî)"),
  FI(role=MT("شَارَكَتْ", "had a share", "ortak oldular»a")),
  MAJR("الْمَوْتِ", "mawt"),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«شَارَكَتْ» أَيْضًا، وَجَعْلُهُمَا بَدَلًا مِمَّا قَبْلَهُمَا جَيِّدٌ (الدُّرَّةُ)", "; this phrase too hangs on «had a share» — or, better, is a badal of the one before (al-Durra)", " — bu câr-mecrûr da «ortak oldular»a müteallik; öncekinden bedel sayılması da güzeldir (Dürre)")),
  MAJR("دَمِ", "dam", **W(MUD)),
  MUDAF_ILAYH("نَوْفَلٍ", "nawfal", "propn", note_ar=" — أَحَدُ الْقَتْلَى", note_en=" — one of the slain", note_tr=" — öldürülenlerden biri")],
 [T("وَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq", "huruf-al-ziyada-fil-kafiya"], WA_AR + "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to strengthen the negation.", "«ve» + nefyi te'kîd eden zâid «lâ».",
     segs=SG(("وَ", "wa", "conj"), ("لَا", "la-nafiya", "part"))),
  T("وَهَبٍ", "wahab-name", "propn", ["atf-nasaq"], "مَعْطُوفٌ عَلَى «نَوْفَلٍ» مَجْرُورٌ بِالْكَسْرَةِ — أَحَدُ الْقَتْلَى.", "Joined to «Nawfal», in jarr — one of the slain.", "«Nevfel»e ma'tûf, mecrûr — öldürülenlerden biri."),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «وَهَبٍ» (الدُّرَّةُ)", note_en="; the phrase hangs on an omitted hal of «Wahab» (al-Durra)", note_tr="; câr-mecrûr «Vehb»in mahzûf hâline müteallik (Dürre)"),
  T("وَلَا", "la-nafiya", "part", ["la-nafiya", "atf-nasaq", "huruf-al-ziyada-fil-kafiya"], WA_AR + "لَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to strengthen the negation.", "«ve» + nefyi te'kîd eden zâid «lâ».",
     segs=SG(("وَ", "wa", "conj"), ("لَا", "la-nafiya", "part"))),
  T("ابْنِ", "ibn", "noun", ["atf-nasaq", "idafa-definiteness"], "مَعْطُوفٌ عَلَى «وَهَبٍ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ.", "Joined to «Wahab», in jarr, and annexed.", "«Vehb»e ma'tûf, mecrûr, muzâf."),
  MUDAF_ILAYH("الْمُخَزَّمِ", "mukhazzam", "propn", ["al-qafiya"], note_ar=" — ابْنُ الْمُخَزَّمِ: أَحَدُ الْقَتْلَى" + RAWI_AL[0], note_en=" — Ibn al-Mukhazzam is one of the slain" + RAWI_AL[1], note_tr=" — İbnü'l-Muhazzem öldürülenlerden biridir" + RAWI_AL[2])])
# ---- v. 43 ----
VV(43, "And yet I see that they have come to pay for every one of them, in sound camels of their herds climbing the mountain pass.",
  "Buna rağmen görüyorum ki onların her birinin diyetini, dağ geçidine tırmanan sağlam develerle öder olmuşlar.",
 [T("فَكُلًّا", "kull", "noun", ["maful-bihi"],
     "الْفَاءُ عَاطِفَةٌ، وَكُلًّا مَنْصُوبٌ عَلَى الِاشْتِغَالِ بِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «يَعْقِلُونَهُ» بَعْدَهُ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ: فَكُلَّ وَاحِدٍ مِنَ الْقَتْلَى؛ وَيَجُوزُ رَفْعُهُ عَلَى الِابْتِدَاءِ (الدُّرَّةُ).",
     "The fa conjoins; كُلًّا is in nasb by ishtighal — by an omitted verb that «they pay for him» after it explains — its sign the fatha; the tanwin stands for the dropped second term: «each one of the slain»; it could also be read in raf', as a mubtada (al-Durra).",
     "Fâ atıf harfi; «küllen» iştigâl üzere, sonraki «diyetini öderler»in tefsir ettiği mahzûf bir fiille mansûb, alâmeti fetha — tenvin muzâfun ileyhten ivazdır: «öldürülenlerin her birini»; mübtedâ olarak ref'i de caizdir (Dürre).",
     segs=SG(("فَ", "fa", "conj"), ("كُلًّا", "kull", "noun"))),
  T("أَرَاهُمْ", "raa", "verb", ["mudari-marfu", "naqis-verbs", "al-bariz-al-muttasil", "mafulayn", "al-mutaaddi-wa-afal-al-qulub", "al-fail-al-mudmar-al-mustatir-wujuban"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ — أَيْ أَرَى الْعَاقِلِينَ.",
     "Present verb in raf' by a damma estimated on the alif; the doer «I» must stay hidden; the attached «them» is the first object, in the seat of nasb — «I see those who pay».",
     "Elif üzerinde takdîrî damme ile merfû muzâri; fâil vücûben gizli «ben»; bitişik «onları» birinci mef'ûl, mahallen mansûb — yani «diyet ödeyenleri görüyorum».",
     segs=SG(("أَرَا", "raa", "verb"), ("هُمْ", "pron-3mp", "pron"))),
  T("أَصْبَحُوا", "asbaha", "verb", ["kana-wa-akhawatuha", "form-iv-verbs", "al-bariz-al-muttasil", "mafulayn"],
     "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ اسْمُهُ — وَجُمْلَةُ «أَصْبَحُوا يَعْقِلُونَهُ» فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ لِـ«أَرَى» الْقَلْبِيَّةِ، أَوْ حَالٌ عَلَى أَنَّهَا بَصَرِيَّةٌ (الدُّرَّةُ).",
     "A defective past verb built on damma because the waw of the group is attached; that waw is its noun, in the seat of raf' — the clause «they have come to pay for him» is the second object of «I see» as a verb of the heart, in the seat of nasb, or a hal if it is the seeing of the eye (al-Durra).",
     "Cemâat vâvı bitiştiği için damme üzere mebnî nâkıs mâzî; vâv ismidir, mahallen merfû — «diyetini öder oldular» cümlesi, kalbî «görüyorum»un ikinci mef'ûlü olarak mahallen mansûb; basarî sayılırsa hâldir (Dürre).",
     segs=SG(("أَصْبَحُو", "asbaha", "verb"), ("ا", "pron-3mp", "pron"))),
  T("يَعْقِلُونَهُ", "aqala-diya", "verb", ["mudari-marfu", "afal-khamsa", "al-bariz-al-muttasil", "fail", "maful-bihi", "kana-wa-akhawatuha"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ يَعُودُ عَلَى «كُلًّا» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «أَصْبَحُوا». عَقَلْتُ الْقَتِيلَ: وَدَيْتُهُ، وَسُمِّيَتِ الدِّيَةُ عَقْلًا لِأَنَّهَا تَعْقِلُ الدَّمَ عَنِ السَّفْكِ، أَوْ لِأَنَّ الْوَادِيَ كَانَ يَعْقِلُ الْإِبِلَ بِأَفْنِيَةِ الْقَتِيلِ (الزَّوْزَنِيُّ).",
     "Present verb in raf' by the keeping of its nun, being one of the five verbs; the waw is the doer, in the seat of raf', and the attached «him», returning to كُلًّا, the object, in the seat of nasb — the clause is the predicate of أَصْبَحُوا, in the seat of nasb. عَقَلْتُ الْقَتِيلَ is «I paid the blood-price for the slain man»; blood-money is called عَقْل because it «hobbles» blood from being shed — or because the payer used to hobble the camels in the dead man's yard (al-Zawzanī).",
     "Ef'âl-i hamseden olduğu için nûnun sübûtu ile merfû muzâri; vâv fâil, mahallen merfû; «küllen»e dönen bitişik «onu» mef'ûlün bih, mahallen mansûb — cümle «asbahû»nun haberi, mahallen mansûb. «Akaltü'l-katîle»: maktulün diyetini ödedim; diyete «akl» denmesi, kanın dökülmesini «bağladığı» için yahut diyeti ödeyenin develeri maktulün avlusunda bağladığı içindir (Zevzenî).",
     segs=SG(("يَعْقِلُونَ", "aqala-diya", "verb"), ("هُ", "pron-3ms", "pron")))],
 [T("صَحِيحَاتِ", "sahih", "noun", ["maful-bihi", "mafulayn", "jam-muannath-salim", "idafa-definiteness", "hal"],
     "مَفْعُولٌ بِهِ ثَانٍ لِـ«يَعْقِلُ» عَلَى تَعْدِيَتِهِ إِلَى اثْنَيْنِ، أَوْ حَالٌ (الدُّرَّةُ)، مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ، مُضَافٌ — أَيْ: يَعْقِلُونَهُ بِصَحِيحَاتِ إِبِلٍ (الزَّوْزَنِيُّ).",
     "The second object of «pay», if the verb takes two — or a hal (al-Durra) — in nasb by the kasra that stands for the fatha, a sound feminine plural, and annexed — «they pay for him with sound camels» (al-Zawzanī).",
     "«Öderler» iki mef'ûl alır sayılırsa ikinci mef'ûlü, yahut hâl (Dürre); cem-i müennes sâlim olduğu için fetha yerine kesre ile mansûb, muzâf — yani «onun diyetini sağlam develerle öderler» (Zevzenî)."),
  MUDAF_ILAYH("مَالٍ", "mal", note_ar=" — وَالْمَالُ عِنْدَ الْعَرَبِ الْإِبِلُ", note_en=" — «wealth», among the Arabs, is camels", note_tr=" — Araplarda «mal» develerdir"),
  T("طَالِعَاتٍ", "tali", "noun", ["naat-sifa", "jam-muannath-salim", "ism-fail"],
     "نَعْتٌ لِـ«صَحِيحَاتِ» مَنْصُوبٌ بِالْكَسْرَةِ نِيَابَةً عَنِ الْفَتْحَةِ لِأَنَّهُ جَمْعُ مُؤَنَّثٍ سَالِمٌ — طَلَعْتُ الثَّنِيَّةَ: عَلَوْتُهَا.",
     "A na't of «sound ones», in nasb by the kasra that stands for the fatha, a sound feminine plural — طَلَعْتُ الثَّنِيَّةَ is «I climbed the pass».",
     "«Sağlam olanlar»ın na'tı; cem-i müennes sâlim olduğu için fetha yerine kesre ile mansûb — «tala'tü's-seniyyete»: geçide tırmandım."),
  BI_NOUN("بِمَخْرِمِ", "makhrim", "مَخْرِمِ", extra=["al-qafiya"], note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»؛ الْمَخْرِمُ: مُنْقَطَعُ أَنْفِ الْجَبَلِ وَالطَّرِيقُ فِيهِ: تَعْلُو فِي طُرُقِ الْجِبَالِ عِنْدَ سَوْقِهَا إِلَى أَوْلِيَاءِ الْمَقْتُولِينَ. وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«طَالِعَاتٍ»" + RAWI_J[0], note_en=" — the ba means «in»; a مَخْرِم is where a mountain's spur breaks off, and the road through it: the camels climb the mountain paths as they are driven to the kin of the slain. The phrase hangs on «climbing»" + RAWI_J[1], note_tr=" — bâ «-de» anlamındadır; «mahrim»: dağ burnunun kesildiği yer ve oradaki yol: develer maktullerin velilerine sürülürken dağ yollarına tırmanır. Câr-mecrûr «tırmanan»a müteallik" + RAWI_J[2])])
# ---- v. 44 ----
VV(44, "— for the sake of a tribe dwelling together, whose word shields people when one of the nights comes down with a great trouble;",
  "— bir arada konan öyle bir kabile uğruna ki, gecelerden biri büyük bir belâyla çıkageldiğinde onların emri insanları korur;",
 [T("لِحَيٍّ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَحَيٍّ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَعْقِلُونَهُ» فِي الْبَيْتِ قَبْلَهُ: يَعْقِلُونَ الْقَتْلَى لِأَجْلِ حَيٍّ (الزَّوْزَنِيُّ).", "The lam is a jarr letter of cause; «a tribe» is in jarr — the phrase hangs on «they pay for him» in the verse before: they pay for the slain for the sake of a tribe (al-Zawzanī).", "Lâm ta'lîl için cer harfi; «kabile» mecrûr — câr-mecrûr önceki beyitteki «diyetini öderler»e müteallik: maktullerin diyetini bir kabile uğruna öderler (Zevzenî).",
     segs=SG(("لِ", "li", "prep"), ("حَيٍّ", "hayy-tribe", "noun"))),
  NAAT("حِلَالٍ", "hall-dwelling", "jarr", extra=["jam-taksir"], note_ar=" — جَمْعُ حَالٍّ كَصَاحِبٍ وَصِحَابٍ: النَّازِلُونَ؛ وَجُمِعَ النَّعْتُ لِأَنَّ الْحَيَّ جَمْعٌ فِي الْمَعْنَى", note_en=" — the plural of حَالّ, like صَاحِب and صِحَاب: «those camped together»; the na't is plural because «tribe» is many in sense", note_tr=" — «hâll»in cem'i, «sâhib – sıhâb» gibi: «konmuş olanlar»; «kabile» mânen çoğul olduğu için na't cemi gelmiştir"),
  T("يَعْصِمُ", "asama", "verb", ["mudari-marfu", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَفَاعِلُهُ «أَمْرُهُمْ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِـ«حَيٍّ»؛ يَعْصِمُ: يَمْنَعُ.", "Present verb in raf'; its doer is «their word» — the clause is a second na't of «a tribe», in the seat of jarr; يَعْصِمُ is «defends».", "Merfû muzâri; fâili «emirleri»dir — cümle «kabile»nin ikinci na'tı, mahallen mecrûr; «ya'sımü»: korur."),
  MAFUL("النَّاسَ", "nas", note_ar=" — أَيْ جِيرَانَهُمْ وَحُلَفَاءَهُمْ", note_en=" — their neighbours and allies", note_tr=" — yani komşularını ve müttefiklerini"),
  ENC_NOUN("أَمْرُهُمْ", "amr", "هُمْ", "fail")],
 [T("إِذَا", "idha", "part", ["idha-shartiyya", "maful-fih"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مُتَعَلِّقٌ بِـ«يَعْصِمُ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time built on sukun, in the seat of nasb, hanging on «shields», and annexed to the clause after it.", "Sükûn üzere mebnî zaman zarfı; mahallen mansûb, «korur»a müteallik; sonraki cümleye muzâf."),
  MADI("طَرَقَتْ", "taraqa", ["majaz-aqli"], fem=True, note_ar=FAIL_BAAD[0] + " — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ؛ وَالطُّرُوقُ: الْإِتْيَانُ لَيْلًا. وَإِسْنَادُ الطُّرُوقِ إِلَى اللَّيْلَةِ مَجَازٌ عَقْلِيٌّ، لِأَنَّ اللَّيَالِيَ لَا تَطْرُقُ وَلَا تَأْتِي بِشَيْءٍ وَإِنَّمَا هِيَ ظَرْفٌ لِلْحَوَادِثِ (الدُّرَّةُ)", note_en=FAIL_BAAD[1] + " — the clause fills the seat of jarr after إِذَا; طُرُوق is coming by night. To give the «coming» to the night is a majaz of attribution, for nights do not come upon people or bring anything: they are only the time in which things happen (al-Durra)", note_tr=FAIL_BAAD[2] + " — cümle «izâ»ya muzâfun ileyh olarak mahallen mecrûr; «turûk»: geceleyin gelmek. Gelmenin geceye isnadı mecâz-ı aklîdir; çünkü geceler ne gelir ne bir şey getirir, yalnızca hadiselerin zarfıdır (Dürre)"),
  FAIL("إِحْدَى", "ihda", extra=["ism-maqsur-manqus", "idafa-definiteness"], sign="بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar="، مُضَافٌ", note_en=" — by a damma estimated on the alif; annexed", note_tr=" — elif üzerinde takdîrî damme ile; muzâf"),
  MUDAF_ILAYH("اللَّيَالِي", "layla", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", note_en=" — by a kasra estimated on the ya", note_tr=" — yâ üzerinde takdîrî kesre ile"),
  BI_NOUN("بِمُعْظَمِ", "muzam", "مُعْظَمِ", extra=["al-qafiya", "ijaz-al-hadhf"], note_ar=" — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: بِأَمْرٍ مُعْظَمٍ أَيْ فَظِيعٍ عَظِيمٍ؛ وَالْبَاءُ لِلتَّعْدِيَةِ أَوْ بِمَعْنَى «مَعَ» (الزَّوْزَنِيُّ)، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«طَرَقَتْ». وَالظَّاءُ مَفْتُوحَةٌ فِي الْمَطْبُوعِ؛ وَعَلَى قَوْلِهِ «أَعْظَمَ الْأَمْرُ: صَارَ إِلَى حَالِ الْعِظَمِ» يَكُونُ اسْمَ فَاعِلٍ بِكَسْرِهَا" + RAWI_J[0], note_en=" — a quality whose noun is left out: «a grave [matter]»; the ba makes the verb transitive, or means «with» (al-Zawzanī); the phrase hangs on «comes down». The edition prints fatha on the ẓāʾ; on al-Zawzanī's gloss — «the matter أَعْظَمَ: came to be great» — it would be the active participle, with kasra" + RAWI_J[1], note_tr=" — mevsûfu hazfedilmiş sıfat: «büyük [bir iş]»; bâ ta'diye içindir yahut «ile» anlamındadır (Zevzenî); câr-mecrûr «çıkageldi»ye müteallik. Baskıda zâ fethalıdır; Zevzenî'nin «a'zame'l-emru: büyüklük haline vardı» açıklamasına göre kesreli ism-i fâil olur" + RAWI_J[2])])
# ---- v. 45 ----
VV(45, "— a noble tribe: the man with a grudge does not get his revenge on them, nor is one of theirs who has done a wrong given up.",
  "— soylu bir kabile: kin güden onlardan öcünü alamaz; içlerinden suç işleyen de (düşmana) teslim edilmez.",
 [NAAT("كِرَامٍ", "karim", "jarr", extra=["jam-taksir"], note_ar=" — نَعْتٌ آخَرُ لِـ«حَيٍّ» فِي الْبَيْتِ قَبْلَهُ؛ جَمْعُ كَرِيمٍ", note_en=" — a further na't of «a tribe» in the verse before; the plural of كَرِيم", note_tr=" — önceki beyitteki «kabile»nin bir başka na'tı; «kerîm»in cem'i"),
  T("فَلَا", "la-hijaziyya", "part", ["ma-la-mushabbaha", "ma-la-laysa-wa-la-al-jins"],
     "الْفَاءُ لِلتَّفْرِيعِ، وَلَا نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ (الدُّرَّةُ) — وَاسْمُهَا هُنَا مَعْرِفَةٌ وَهُوَ قَلِيلٌ — وَيَجُوزُ إِهْمَالُهَا فَيَكُونُ مَا بَعْدَهَا مُبْتَدَأً وَخَبَرًا.",
     "The fa draws a consequence; لَا negates and works like لَيْسَ (al-Durra) — its noun here is definite, which is rare — or it may be left without government, what follows being mubtada and khabar.",
     "Fâ tefrî' içindir; «lâ» nâfiyedir ve «leyse» gibi amel eder (Dürre) — ismi burada ma'rifedir, bu nadirdir — ihmâli de caizdir; o zaman sonrası mübtedâ ve haber olur.",
     segs=SG(("فَ", "fa", "conj"), ("لَا", "la-hijaziyya", "part"))),
  T("ذُو", "dhu", "noun", ["ma-la-mushabbaha", "five-nouns", "idafa-definiteness"], "اسْمُ «لَا» مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The noun of لَا, in raf' by the waw — one of the five nouns — and annexed.", "«Lâ»nın ismi; esmâ-i hamseden olduğu için vâv ile merfû, muzâf."),
  MUDAF_ILAYH("الضِّغْنِ", "dighn", note_ar=" — مَا اسْتَكَنَّ فِي الْقَلْبِ مِنَ الْعَدَاوَةِ", note_en=" — the enmity that lies hidden in the heart", note_tr=" — kalpte gizlenen düşmanlık"),
  T("يُدْرِكُ", "adraka", "verb", ["mudari-marfu", "form-iv-verbs", "ma-la-mushabbaha"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «ذُو الضِّغْنِ» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «لَا».", "Present verb in raf'; the doer is the hidden «he» — the man with the grudge — and the clause is the predicate of لَا, in the seat of nasb.", "Merfû muzâri; fâil «kin sahibi»ne dönen gizli zamir — cümle «lâ»nın haberi, mahallen mansûb."),
  ENC_NOUN("تَبْلَهُ", "tabl", "هُ", "maful", note_ar=" — وَالتَّبْلُ: الْحِقْدُ وَالْوِتْرُ، أَيْ لَا يُدْرِكُ ذُو الْوِتْرِ وِتْرَهُ عِنْدَهُمْ (الزَّوْزَنِيُّ)", note_en=" — تَبْل is a grudge, a blood-debt: he who is owed vengeance does not get it from them (al-Zawzanī)", note_tr=" — «tebl»: kin, öç; yani öç sahibi onlardan öcünü alamaz (Zevzenî)")],
 [T("وَلَا", "la-hijaziyya", "part", ["ma-la-mushabbaha", "atf-nasaq"], WA_AR + "لَا نَافِيَةٌ تَعْمَلُ عَمَلَ لَيْسَ.", "The waw conjoins; لَا negates and works like لَيْسَ.", "«ve» + «leyse» gibi amel eden nâfiye «lâ».",
     segs=SG(("وَ", "wa", "conj"), ("لَا", "la-hijaziyya", "part"))),
  T("الْجَارِمُ", "jarim", "noun", ["ma-la-mushabbaha", "ism-fail", "ijaz-al-hadhf"], "اسْمُ «لَا» مَرْفُوعٌ بِالضَّمَّةِ — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: الرَّجُلُ الْجَارِمُ، أَيْ ذُو الْجُرْمِ، كَاللَّابِنِ وَالتَّامِرِ (الزَّوْزَنِيُّ).", "The noun of لَا, in raf' — a quality whose noun is left out: «the [man] who has done a crime», that is, «he of the crime», like لَابِن and تَامِر (al-Zawzanī).", "«Lâ»nın ismi, merfû — mevsûfu hazfedilmiş sıfat: «suç işleyen [adam]», yani «suç sahibi»; «lâbin» ve «tâmir» gibi (Zevzenî)."),
  NAAT("الْجَانِي", "jani", "raf", extra=["ism-fail", "ism-maqsur-manqus"], note_ar=" — بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ؛ وَالْجَارِمُ وَالْجَانِي وَاحِدٌ", note_en=" — its damma estimated on the ya; جَارِم and جَانٍ mean the same", note_tr=" — dammesi yâ üzerinde takdîrîdir; «cârim» ile «cânî» aynı anlamdadır"),
  JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onlara»)", **dict(zip(("note_ar", "note_en", "note_tr"), MT("الْجَانِي", "has done a wrong", "suç işleyen»e")))),
  T("بِمُسْلَمِ", "bi", "prep", ["huruf-al-ziyada-fil-kafiya", "ma-la-mushabbaha", "huruf-jarr", "ism-maful", "al-qafiya"],
     "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَمُسْلَمِ خَبَرُ «لَا» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — اسْمُ مَفْعُولٍ مِنْ أَسْلَمَهُ: خَذَلَهُ" + RAWI_J[0] + ".",
     "The ba is an added jarr letter that strengthens the negation; «given up» is the predicate of لَا — in jarr in wording, in nasb in its seat — the passive participle of أَسْلَمَهُ «he forsook him»" + RAWI_J[1] + ".",
     "Bâ, nefyi te'kîd eden zâid cer harfi; «teslim edilmiş», «lâ»nın haberi — lafzen mecrûr, mahallen mansûb — «eslemehû»dan («onu yardımsız bıraktı») ism-i mef'ûl" + RAWI_J[2] + ".",
     segs=SG(("بِ", "bi", "prep"), ("مُسْلَمِ", "muslam-forsaken", "noun")))])
# =====================================================================================================================
# vv. 59–62 — خَاتِمَةُ الْقَصِيدَةِ
# =====================================================================================================================
VV(59, "How many a silent man you see who pleases you — and whether he is more or less shows only when he speaks.",
  "Nice susan kimse görürsün ki hoşuna gider; oysa onun fazlalığı da eksikliği de ancak konuşmasında ortaya çıkar.",
 [T("وَكَائِنْ", "kaayyin", "pron", ["al-kinayat-wal-zuruf-al-mabniyya", "mubtada-khabar", "al-mabni-wal-mudmar", "anwa-al-waw"],
     WA_ISTINAF[0] + "كَائِنْ اسْمُ كِنَايَةٍ عَنِ الْعَدَدِ الْكَثِيرِ بِمَعْنَى «كَمِ» الْخَبَرِيَّةِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَفِيهِ ثَلَاثُ لُغَاتٍ: كَأَيِّنْ وَكَائِنْ وَكَأْيٍ (الزَّوْزَنِيُّ).",
     WA_ISTINAF[1] + "كَائِنْ is a noun that stands for a large number, like the stating كَمْ «how many a», built on sukun in the seat of raf' as mubtada — it has three forms: كَأَيِّنْ, كَائِنْ and كَأْيٍ (al-Zawzanī).",
     WA_ISTINAF[2] + "«kâin» çok sayıdan kinâye isimdir, haberî «kem» anlamındadır; sükûn üzere mebnî, mübtedâ olarak mahallen merfû — üç lügati vardır: «keeyyin», «kâin» ve «ke'yin» (Zevzenî).",
     segs=SG(("وَ", "wa", "conj"), ("كَائِنْ", "kaayyin", "pron"))),
  T("تَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs", "al-fail-al-mudmar-al-mustatir-wujuban", "anwa-al-khabar", "hadhf-al-maful"],
     "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «كَائِنْ»، وَالرَّابِطُ مَفْعُولُهُ الْمَحْذُوفُ: تَرَاهُ (الدُّرَّةُ).",
     "Present verb in raf' by a damma estimated on the alif; the doer «you» must stay hidden — the clause is the khabar of كَائِنْ, in the seat of raf', and what ties it is its dropped object: «you see [him]» (al-Durra).",
     "Elif üzerinde takdîrî damme ile merfû muzâri; fâil vücûben gizli «sen» — cümle «kâin»in haberi, mahallen merfû; bağlayan zamir hazfedilmiş mef'ûldür: «onu görürsün» (Dürre)."),
  T("مِنْ", "min", "prep", ["huruf-jarr", "al-kinayat-wal-zuruf-al-mabniyya"], "حَرْفُ جَرٍّ يَجُرُّ تَمْيِيزَ «كَائِنْ»؛ وَعَدَّهُ الدُّرَّةُ زَائِدًا.", "A jarr letter that takes the tamyiz of كَائِنْ; al-Durra counts it as added.", "«Kâin»in temyîzini cerreden cer harfi; Dürre onu zâid sayar."),
  T("صَامِتٍ", "samit", "noun", ["tamyiz", "ism-fail", "ijaz-al-hadhf", "tibaq"],
     "تَمْيِيزُ «كَائِنْ» مَجْرُورٌ بِـ«مِنْ» — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ: رَجُلٍ صَامِتٍ. وَبَيْنَهُ وَبَيْنَ «التَّكَلُّمِ» طِبَاقٌ.",
     "The tamyiz of كَائِنْ, in jarr by مِنْ — a quality whose noun is left out: «a silent [man]». With «speaking» it makes a tibaq.",
     "«Kâin»in temyîzi, «min» ile mecrûr — mevsûfu hazfedilmiş sıfat: «susan [adam]». «Konuşma» ile arasında tıbâk vardır."),
  LAHU2("لَكَ", "pron-2ms", " («senin»)", note=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُعْجِبٍ»", "; the phrase hangs on «pleasing»", "; câr-mecrûr «hoşa giden»e müteallik")),
  NAAT("مُعْجِبٍ", "mujib-pleasing", "jarr", extra=["ism-fail"], note_ar=" — نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ؛ اسْمُ فَاعِلٍ مِنْ أَعْجَبَ: يُعْجِبُكَ صَمْتُهُ فَتَسْتَحْسِنُهُ (الزَّوْزَنِيُّ)", note_en=" — a second na't of the omitted noun; the active participle of أَعْجَبَ: his silence pleases you and you think well of him (al-Zawzanī)", note_tr=" — mahzûf mevsûfun ikinci na'tı; «a'cebe»den ism-i fâil: susması hoşuna gider, onu beğenirsin (Zevzenî)")],
 [ENC_NOUN("زِيَادَتُهُ", "ziyada", "هُ", "mubtada", extra=["masdar", "tibaq"], note_ar=" — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ: زِيَادَتُهُ عَلَى غَيْرِهِ. وَبَيْنَ «زِيَادَتُهُ» وَ«نَقْصُهُ» طِبَاقٌ", note_en=" — the masdar annexed to its doer: his surpassing others. «His being more» and «his being less» make a tibaq", note_tr=" — masdarın fâiline izâfeti: başkasından fazla oluşu. «Fazlalığı» ile «eksikliği» arasında tıbâk vardır"),
  T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «veya»."),
  T("نَقْصُهُ", "naqs", "noun", ["atf-nasaq", "masdar", "idafa-definiteness", "al-bariz-al-muttasil", "tibaq"],
     "مَعْطُوفٌ عَلَى «زِيَادَتُهُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — أَيْ نُقْصَانُهُ عَنْ غَيْرِهِ.",
     "Joined to «his being more», in raf'; annexed to the attached «his», in the seat of jarr — his falling short of others.",
     "«Fazlalığı»na ma'tûf, merfû; bitişik zamire muzâf, zamir mahallen mecrûr — yani başkasından eksik oluşu.",
     segs=SG(("نَقْصُ", "naqs", "noun"), ("هُ", "pron-3ms", "pron"))),
  FI(role=(" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَأِ، وَالْجُمْلَةُ الِاسْمِيَّةُ خَبَرٌ ثَانٍ لِـ«كَائِنْ»، أَوْ مُسْتَأْنَفَةٌ (الدُّرَّةُ)", "; the jarr phrase hangs on the omitted khabar of the mubtada, and the nominal clause is a second khabar of كَائِنْ — or a fresh start (al-Durra)", " — câr-mecrûr mübtedânın mahzûf haberine müteallik; isim cümlesi «kâin»in ikinci haberidir yahut müste'nefedir (Dürre)")),
  MAJR("التَّكَلُّمِ", "takallum", extra=["masdar", "tibaq", "al-qafiya"], note_ar=" — أَيْ: إِنَّمَا تَظْهَرُ زِيَادَتُهُ وَنُقْصَانُهُ عِنْدَ تَكَلُّمِهِ (الزَّوْزَنِيُّ)" + RAWI_AL[0], note_en=" — that is, his worth or his want shows only when he speaks (al-Zawzanī)" + RAWI_AL[1], note_tr=" — yani fazlalığı da eksikliği de ancak konuştuğunda ortaya çıkar (Zevzenî)" + RAWI_AL[2])])
# ---- v. 60 ----
VV(60, "A man's tongue is one half of him, and the other half is his heart; beyond these nothing is left but the shape of flesh and blood.",
  "Kişinin dili yarısıdır, öbür yarısı da kalbidir; geriye et ve kan suretinden başka bir şey kalmaz.",
 [MUBTADA("لِسَانُ", "lisan", extra=["idafa-definiteness"], **W(MUD)),
  MUDAF_ILAYH("الْفَتَى", "fata-youth", extra=["ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_en=" — by a kasra estimated on the alif", note_tr=" — elif üzerinde takdîrî kesre ile"),
  KHABAR("نِصْفٌ", "nisf", note_ar=" — وَهٰذَا كَقَوْلِ الْعَرَبِ: الْمَرْءُ بِأَصْغَرَيْهِ: لِسَانِهِ وَجَنَانِهِ (الزَّوْزَنِيُّ)", note_en=" — this is the Arabs' saying: «a man is his two smallest parts, his tongue and his heart» (al-Zawzanī)", note_tr=" — bu, Arapların «kişi iki küçük uzvuyladır: dili ve kalbi» sözü gibidir (Zevzenî)"),
  T("وَنِصْفٌ", "nisf", "noun", ["mubtada-khabar", "taqdim-al-musnad", "atf-nasaq"], WA_AR + "نِصْفٌ خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The waw conjoins; «a half» is the khabar, put first, in raf'.", "«ve» + «yarı»: öne alınmış haber, merfû.",
     segs=SG(("وَ", "wa", "conj"), ("نِصْفٌ", "nisf", "noun"))),
  ENC_NOUN("فُؤَادُهُ", "fuad", "هُ", "mubtada", note_ar=" — مُبْتَدَأٌ مُؤَخَّرٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الَّتِي قَبْلَهَا", note_en=" — placed after its khabar; the clause is joined to the one before", note_tr=" — haberinden sonraya bırakılmıştır; cümle öncekine ma'tûf")],
 [LAM_JAZM("فَلَمْ"),
  T("يَبْقَ", "baqiya", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs", "qasr", "turuq-al-qasr"],
     "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ " + SGN["alif"][0] + "، وَفَاعِلُهُ «صُورَةُ» بَعْدَ «إِلَّا». وَفِيهِ قَصْرٌ بِالنَّفْيِ وَالِاسْتِثْنَاءِ: قُصِرَ الْبَاقِي مِنَ الْفَتَى بَعْدَ لِسَانِهِ وَفُؤَادِهِ عَلَى صُورَةِ اللَّحْمِ وَالدَّمِ.",
     "Present verb in jazm by لَمْ, its sign " + SGN["alif"][1] + "; its doer, «shape», comes after إِلَّا. Here is a qasr by negation and exception: what is left of a man, his tongue and heart apart, is confined to the shape of flesh and blood.",
     "Lem ile meczûm muzâri, alâmeti " + SGN["alif"][2] + "; fâili «illâ»dan sonraki «suret»tir. Burada nefy ve istisnâ ile kasr vardır: kişiden dili ve kalbi dışında geriye kalan, et ve kan suretine hasredilmiştir."),
  T("إِلَّا", "illa", "part", ["istithna-mufarragh", "qasr"], "أَدَاةُ حَصْرٍ لَا عَمَلَ لَهَا — وَالِاسْتِثْنَاءُ مُفَرَّغٌ.", "The particle of restriction, governing nothing — the exception is emptied.", "Hasr edatı, ameli yoktur — istisnâ müferrağdır."),
  FAIL("صُورَةُ", "sura", extra=["idafa-definiteness", "istithna-mufarragh"], **W(MUD)),
  MUDAF_ILAYH("اللَّحْمِ", "lahm"),
  ATF("وَالدَّمِ", "dam", case="jarr", extra=["al-qafiya"], **W(RAWI_AL))])
# ---- v. 61 ----
RAF_RAWI = (" — وَحَقُّهُ الرَّفْعُ بِالضَّمَّةِ لِتَجَرُّدِهِ مِنَ النَّاصِبِ وَالْجَازِمِ، وَكُسِرَ آخِرُهُ لِلرَّوِيِّ ضَرُورَةً؛ وَلَوْ رُفِعَ لَكَانَ فِي الْقَصِيدَةِ إِقْوَاءٌ (الدُّرَّةُ)", " — by rule it is in raf', with damma, having nothing to put it in nasb or jazm; its last letter takes the kasra of the rhyme by poetic licence; were it read with damma the ode would have an iqwāʾ, a break in the rhyme-vowel (al-Durra)", " — nâsıb ve câzimden hâlî olduğu için kaideye göre damme ile merfû olmalıdır; son harfi revî için zarûreten kesrelenmiştir; dammeli okunsaydı kasidede ikvâ (revî harekesinin değişmesi) olurdu (Dürre)")
VV(61, "The folly of an old man has no good sense to follow it; but a young man, after his folly, grows wise.",
  "İhtiyarın sefihliğinden sonra akıl başa gelmez; genç ise sefihlikten sonra hilim sahibi olur.",
 [T("وَإِنَّ", "inna", "part", ["inna-wa-akhawatuha", "anwa-al-waw"], WA_ISTINAF[0] + "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", WA_ISTINAF[1] + "إِنَّ is the particle of emphasis that puts its noun in nasb.", WA_ISTINAF[2] + "inne: te'kîd ve nasb harfi.",
     segs=SG(("وَ", "wa", "conj"), ("إِنَّ", "inna", "part"))),
  T("سَفَاهَ", "safah", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar", "tibaq", "muqabala"],
     "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ. وَبَيْنَ «سَفَاهَ» وَ«حِلْمَ» طِبَاقٌ، وَبَيْنَ «الشَّيْخِ» وَ«الْفَتَى» طِبَاقٌ، وَفِي الْبَيْتِ مُقَابَلَةٌ: «سَفَاهُ الشَّيْخِ لَا حِلْمَ بَعْدَهُ» ↔ «الْفَتَى بَعْدَ السَّفَاهَةِ يَحْلُمُ».",
     "The noun of إِنَّ, in nasb, annexed. «Folly» and «good sense» make a tibaq, and so do «the old man» and «the young man»; the verse holds a muqabala: «the old man's folly has no sense after it» against «the young man, after folly, grows wise».",
     "İnne'nin ismi, mansûb, muzâf. «Sefihlik» ile «hilim», «ihtiyar» ile «genç» arasında tıbâk vardır; beyitte mukâbele bulunur: «ihtiyarın sefihliğinden sonra hilim yoktur» ↔ «genç, sefihlikten sonra hilim sahibi olur»."),
  MUDAF_ILAYH("الشَّيْخِ", "shaykh", extra=["tibaq"]),
  T("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"], "نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ — وَالْجُمْلَةُ الِاسْمِيَّةُ «لَا حِلْمَ بَعْدَهُ» فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.", "The لَا that denies the whole genus, working like إِنَّ — the nominal clause «there is no good sense after it» is the predicate of إِنَّ, in the seat of raf'.", "Cinsi nefyeden «lâ»; inne gibi amel eder — «ondan sonra hilim yoktur» isim cümlesi inne'nin haberi, mahallen merfû."),
  T("حِلْمَ", "hilm", "noun", ["la-nafiya-lil-jins", "tibaq", "radd-al-ajuz", "mulhaq-bil-jinas"],
     "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ. وَبَيْنَهُ وَبَيْنَ «يَحْلُمِ» اشْتِقَاقٌ، وَهُوَ مِنْ رَدِّ الْعَجُزِ عَلَى الصَّدْرِ: أَحَدُهُمَا فِي حَشْوِ الْمِصْرَاعِ الْأَوَّلِ وَالْآخَرُ فِي آخِرِ الْبَيْتِ.",
     "The noun of لَا, built on fatha in the seat of nasb. It shares a root with يَحْلُمِ, and the two make a radd al-'ajuz 'ala al-sadr: one stands inside the first hemistich, the other ends the verse.",
     "«Lâ»nın ismi; fetha üzere mebnî, mahallen mansûb. «Yahlüm» ile arasında iştikâk vardır; bu aynı zamanda reddü'l-acüz ale's-sadrdır: biri ilk mısraın içinde, diğeri beytin sonundadır."),
  T("بَعْدَهُ", "bada", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "la-nafiya-lil-jins"],
     "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ «لَا»، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهُوَ الرَّابِطُ؛ أَيْ: لَا حَالَ بَعْدَ الشَّيْبِ إِلَّا الْمَوْتُ (الزَّوْزَنِيُّ).",
     "An adverb of time, in nasb, hanging on the omitted predicate of لَا; annexed to the attached «it», in the seat of jarr — the pronoun that ties the clause; that is, after grey hair there is no state left but death (al-Zawzanī).",
     "Zaman zarfı, mansûb; «lâ»nın mahzûf haberine müteallik; bitişik zamire muzâf, zamir mahallen mecrûr — cümleyi bağlayan odur; yani ihtiyarlıktan sonra ölümden başka hal yoktur (Zevzenî).",
     segs=SG(("بَعْدَ", "bada", "noun"), ("هُ", "pron-3ms", "pron")))],
 [T("وَإِنَّ", "inna", "part", ["inna-wa-akhawatuha", "atf-nasaq"], WA_AR + "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "The waw conjoins; إِنَّ is the particle of emphasis that puts its noun in nasb.", "«ve» + inne: te'kîd ve nasb harfi.",
     segs=SG(("وَ", "wa", "conj"), ("إِنَّ", "inna", "part"))),
  T("الْفَتَى", "fata-youth", "noun", ["inna-wa-akhawatuha", "ism-maqsur-manqus", "tibaq"], "اسْمُ إِنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "The noun of إِنَّ, in nasb by a fatha estimated on the alif.", "İnne'nin ismi; elif üzerinde takdîrî fetha ile mansûb."),
  ZARF("بَعْدَ", "bada", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", note_ar=" — مُتَعَلِّقٌ بِـ«يَحْلُمِ»", note_en=", hanging on «grows wise»", note_tr="; «hilim sahibi olur»a müteallik"),
  MUDAF_ILAYH("السَّفَاهَةِ", "sifaha", extra=["masdar"]),
  T("يَحْلُمِ", "haluma", "verb", ["mudari-marfu", "anwa-al-khabar", "al-qafiya", "radd-al-ajuz", "mulhaq-bil-jinas", "tibaq"],
     "فِعْلٌ مُضَارِعٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَتَى، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ" + RAF_RAWI[0] + ".",
     "Present verb; the doer is the hidden «he» — the young man — and the clause is the predicate of إِنَّ, in the seat of raf'" + RAF_RAWI[1] + ".",
     "Muzâri; fâil gence dönen gizli zamir «o»; cümle inne'nin haberi, mahallen merfû" + RAF_RAWI[2] + ".")])
# ---- v. 62 ----
VV(62, "We asked and you gave; we came again and you gave again — but he who asks too often will one day be refused.",
  "İstedik, verdiniz; yine geldik, yine verdiniz — ama çok isteyen bir gün mahrum bırakılır.",
 [T("سَأَلْنَا", "saala", "verb", ["al-bariz-al-muttasil", "fail", "hadhf-al-maful", "mulhaq-bil-jinas"],
     "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَمَفْعُولَاهُ مَحْذُوفَانِ: سَأَلْنَاكُمْ رِفْدَكُمْ وَمَعْرُوفَكُمْ (الزَّوْزَنِيُّ). وَبَيْنَهُ وَبَيْنَ «التَّسْآلَ» اشْتِقَاقٌ.",
     "Past verb built on sukun because نَا is attached; that «we» is the doer, in the seat of raf'; its two objects are left out: «we asked you for your bounty» (al-Zawzanī). It shares a root with التَّسْآلَ.",
     "«Nâ» bitiştiği için sükûn üzere mebnî mâzî; «nâ» fâildir, mahallen merfû; iki mef'ûlü mahzûf: «sizden ihsanınızı istedik» (Zevzenî). «Tes'âl» ile arasında iştikâk vardır.",
     segs=SG(("سَأَلْ", "saala", "verb"), ("نَا", "pron-1p", "pron"))),
  T("فَأَعْطَيْتُمْ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "fail", "atf-nasaq", "hadhf-al-maful"],
     FA_AR + "أَعْطَيْتُمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَمَفْعُولَاهُ مَحْذُوفَانِ.",
     "The fa conjoins; أَعْطَيْتُمْ is a past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer; its two objects are left out.",
     "«fe» + «verdiniz»: ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir; iki mef'ûlü mahzûf.",
     segs=SG(("فَ", "fa", "conj"), ("أَعْطَيْتُمْ", "aata", "verb"))),
  T("وَعُدْنَا", "ada-return", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "atf-nasaq"],
     WA_AR + "عُدْنَا فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — أَيْ عُدْنَا إِلَى السُّؤَالِ.",
     "The waw conjoins; عُدْنَا is a past verb built on sukun because نَا is attached; that «we» is the doer — «we went back to asking».",
     "«ve» + «döndük»: «nâ» bitiştiği için sükûn üzere mebnî mâzî; «nâ» fâildir — yani «yine istemeye döndük».",
     segs=SG(("وَ", "wa", "conj"), ("عُدْ", "ada-return", "verb"), ("نَا", "pron-1p", "pron"))),
  T("فَعُدْتُمُ", "ada-return", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "atf-nasaq"],
     FA_AR + "عُدْتُمْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ، وَتُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَضُمَّتِ الْمِيمُ وَأُشْبِعَتْ لِإِقَامَةِ الْوَزْنِ — أَيْ عُدْتُمْ إِلَى النَّوَالِ.",
     "The fa conjoins; عُدْتُمْ is a past verb built on sukun because a pronoun of raf' is attached; تُمْ «you» is the doer; the mim takes a lengthened damma to keep the metre — «you went back to giving».",
     "«fe» + «döndünüz»: ref' zamiri bitiştiği için sükûn üzere mebnî mâzî; «tüm» fâildir; vezin için mîm dammelenip uzatılmıştır — yani «yine vermeye döndünüz».",
     segs=SG(("فَ", "fa", "conj"), ("عُدْتُمُ", "ada-return", "verb")))],
 [T("وَمَنْ", "man-mawsula", "pron", ["ism-mawsul", "mubtada-khabar", "anwa-al-waw"],
     WA_ISTINAF[0] + "مَنْ اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ (الدُّرَّةُ) — وَلَيْسَتْ شَرْطِيَّةً، فَإِنَّ «سَيُحْرَمِ» لَمْ يُجْزَمْ وَلَمْ يَقْتَرِنْ بِالْفَاءِ.",
     WA_ISTINAF[1] + "مَنْ is a relative noun «he who», built on sukun, in the seat of raf' as mubtada (al-Durra) — not the conditional مَنْ, for «will be refused» is neither in jazm nor joined by a fa.",
     WA_ISTINAF[2] + "«men» ism-i mevsûldür, sükûn üzere mebnî, mübtedâ olarak mahallen merfû (Dürre) — şart ismi değildir; çünkü «mahrum bırakılır» ne meczûmdur ne de fâ almıştır.",
     segs=SG(("وَ", "wa", "conj"), ("مَنْ", "man-mawsula", "pron"))),
  MADI("أَكْثَرَ", "akthara", ["form-iv-verbs"], note_ar="، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»" + SILA_[0], note_en="; the doer is the hidden «he», returning to مَنْ" + SILA_[1], note_tr="; fâil «men»e dönen gizli zamir" + SILA_[2]),
  MAFUL("التَّسْآلَ", "tasal", extra=["masdar", "mulhaq-bil-jinas"], note_ar=" — التَّسْآلُ: السُّؤَالُ، وَتَفْعَالٌ مِنْ أَبْنِيَةِ الْمَصَادِرِ (الزَّوْزَنِيُّ)", note_en=" — تَسْآل is «asking»; تَفْعَال is one of the masdar patterns (al-Zawzanī)", note_tr=" — «tes'âl»: istemek; «tef'âl» masdar vezinlerindendir (Zevzenî)"),
  ZARF("يَوْمًا", "yawm", mudaf=False, kind="زَمَانٍ", kind_en="time", kind_tr="zaman", note_ar=" — مُتَعَلِّقٌ بِـ«أَكْثَرَ» (الدُّرَّةُ)، وَعَلَى تَفْسِيرِ الزَّوْزَنِيِّ بِـ«سَيُحْرَمِ»: حُرِمَ يَوْمًا لَا مَحَالَةَ", note_en=", hanging on «asks too often» (al-Durra) — or, as al-Zawzanī paraphrases, on «will be refused»: «he is refused one day, without fail»", note_tr="; «çok isteyen»e müteallik (Dürre) — Zevzenî'nin açıklamasına göre «mahrum bırakılır»a: «bir gün mutlaka mahrum kalır»"),
  T("سَيُحْرَمِ", "harama-deprive", "verb", ["mudari-marfu", "naib-al-fail", "al-majhul-fil-kafiya", "anwa-al-khabar", "al-qafiya"],
     "السِّينُ حَرْفُ اسْتِقْبَالٍ، وَيُحْرَمُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ»، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «مَنْ»" + RAF_RAWI[0] + ".",
     "The sin marks the future; يُحْرَمُ is a present verb in the passive; its deputy doer is the hidden «he», returning to مَنْ, and the clause is the khabar of مَنْ, in the seat of raf'" + RAF_RAWI[1] + ".",
     "Sîn istikbâl harfi; «yuhramü» meçhul muzâri; nâib-i fâil «men»e dönen gizli zamir; cümle «men»in haberi, mahallen merfû" + RAF_RAWI[2] + ".",
     segs=SG(("سَ", "sa-istiqbal", "part"), ("يُحْرَمِ", "harama-deprive", "verb")))])
# >>> NEW VERSES ABOVE THIS LINE <<<
VERSES = {}
for _nums, _S in ((range(1, 7), S2), (range(16, 22), S3), (range(28, 33), S4), (range(46, 53), S5), (range(53, 59), S6)):
    assert len(_S) == len(_nums), (_nums, len(_S))
    VERSES.update(zip(_nums, _S))
assert not set(EXTRA) & set(VERSES)
VERSES.update(EXTRA)
POEM_END = 62
PLAN = [(1, 7), (8, 15), (16, 21), (22, 27), (28, 34), (35, 40), (41, 48), (49, 55), (56, 62)]
CHAPS, VNUMS = [CH[1]], []
for _a, _b in PLAN:
    if not all(n in VERSES for n in range(_a, _b + 1)): break
    _S = [VERSES[n] for n in range(_a, _b + 1)]
    for _i, _s in enumerate(_S, 1): _s["id"] = "s%d" % _i
    CHAPS.append(_S); VNUMS.append((_a, _b))
DONE_TO = VNUMS[-1][1] if VNUMS else 0
ALL_AUTHORED = [CH[1]] + [[VERSES[n]] for n in sorted(VERSES)]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-vi-verbs", "form-vii-verbs", "form-viii-verbs", "form-x-verbs"}
for S in ALL_AUTHORED:
    for s in S:
        for t in s["tokens"]:
            if DERIVED & set(t.get("grammar", [])) and "thulathi-mujarrad-babs" in t["grammar"]:
                t["grammar"].remove("thulathi-mujarrad-babs")
            t["grammar"] = list(dict.fromkeys(t.get("grammar", [])))
            if not t["grammar"]: del t["grammar"]
_GR = {p.stem for p in (ROOT / "content/grammar").glob("*.json")}
_bad = sorted({g for S in ALL_AUTHORED for s in S for t in s["tokens"] for g in t.get("grammar", []) if g not in _GR})
assert not _bad, _bad
# a segment never opens with a bare vowel mark: «لَكُمْ» is لَ + كُمْ
import re as _re
for S in ALL_AUTHORED:
    for s in S:
        for t in s["tokens"]:
            for sg2 in t.get("segments", []):
                sg2["form"] = _re.sub("^[ً-ْ]+", "", sg2["form"])

# ---- the lexicon: every shelf key by lemma identity; the entries in NEW_GLOSS are new ---------------------------------
PREF = ["qisas-al-nabiyyin-4", "talkhis-al-miftah", "al-kafiya", "sibawayh-fi-al-basra", "ayn-jalut", "bina-baghdad", "al-usul-al-munifa",
        "wasiyyat-abi-yusuf-l5", "shudhur-al-dhahab", "marah-al-arwah", "tasrif-al-izzi"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {}
for p in PREF:
    try: _M[p] = json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {})
    except FileNotFoundError: _M[p] = {}
# where the shelf holds one key in several senses, take the entry this poem uses
FORCE = {"fadl": "kitab-al-buyu", "madhhab": "al-ghazali-wa-al-uzla", "rajul": "al-bukhari-fi-baghdad", "dar": "wasiyyat-abi-yusuf-l5"}
def find_gloss(k):
    if FORCE.get(k) and k in _G.get(FORCE[k], {}): return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k, lemma):
    for p in PREF:
        if k in _M[p] and _G[p].get(k, {}).get("lemma") == lemma: return _M[p][k]
    return None
# a reused entry keeps its lemma, root and level; where its shelf gloss was written for another book, the gloss is fitted to the poem
TAILOR = {
 "hawd": ("a watering-trough, a cistern (pl. أَحْوَاض، حِيَاض) — in v. 56 it stands for what a man must defend", "havuz, hayvan sulanan yalak (ç. أَحْوَاض، حِيَاض) — 56. beyitte kişinin koruması gereken şey yerine kullanılmıştır"),
 "rakkaba": ("to fit one thing onto another, to mount (a blade on a shaft); to compound (Form II)", "bir şeyi başka bir şeye takmak, (temreni mızrağa) geçirmek; terkîb etmek (tef'îl)"),
 "taraf": ("end, tip, side (pl. أَطْرَاف)", "uç, taraf (ç. أَطْرَاف)"),
 "sabab": ("a cause, a means, whatever leads to a thing; a rope (pl. أَسْبَاب)", "sebep, vasıta, bir şeye ulaştıran şey; ip (ç. أَسْبَاب)"),
 "haba-awe": ("to fear, to hold in awe (هَابَ يَهَابُ)", "korkmak, heybet duymak (هَابَ يَهَابُ)"),
 "hadith": ("talk, a report, a tale", "söz, haber, anlatılan şey"),
 "duna": ("before, in front of; short of, other than (an adverb, always annexed)", "önünde, berisinde; -den başka (zarf; daima muzâf)"),
 "ala-tanbih": ("the opening, alerting أَلَا — it wakes the hearer and governs nothing", "istiftâh ve tenbîh أَلَا'sı — dinleyeni uyarır, amel etmez"),
 "nab": ("fang, canine tooth (pl. أَنْيَاب)", "köpek dişi, sivri diş (ç. أَنْيَاب)"),
 "nataja": ("to deliver (a she-camel) of her young; passive نُتِجَتْ: she gave birth", "(deveyi) doğurtmak; meçhulü نُتِجَتْ: doğurdu"),
 "naima": ("to live in ease; اِنْعَمْ صَبَاحًا «a good morning to you» (نَعِمَ يَنْعَمُ)", "refah içinde yaşamak; اِنْعَمْ صَبَاحًا «sabahın hayrolsun» (نَعِمَ يَنْعَمُ)"),
 "awfa": ("to keep (a covenant) in full, to fulfil (Form IV; with بِ)", "(ahdi) tam yerine getirmek, vefa etmek (if'âl; بِ ile)"),
 "khalaiq": ("a trait of character, a nature (pl. خَلَائِق) — the same as خُلُق", "huy, tabiat (ç. خَلَائِق) — خُلُق ile aynı"),
 "bayt": ("house; الْبَيْت: the Kaʿba (pl. بُيُوت)", "ev; الْبَيْت: Kâbe (ç. بُيُوت)"),
 "ahmar": ("red (the colour-أَفْعَل; a diptote) — أَحْمَرُ عَادٍ «the Red Man of ʿĀd»: the man who hamstrung the she-camel", "kırmızı (renk bildiren ef'al; gayr-i munsarif) — أَحْمَرُ عَادٍ «Âd'ın Kızıl'ı»: deveyi boğazlayan adam"),
 "shibh": ("a like, a counterpart (pl. أَشْبَاه)", "benzer, denk (ç. أَشْبَاه)"),
 "dhaqa": ("to taste; to undergo, to come to know by trial (hollow; ذُقْتُ)", "tatmak; başından geçirmek, deneyerek öğrenmek (ecvef; ذُقْتُ)"),
 "yamin": ("an oath; the right hand", "yemin; sağ el"),
 "walad": ("child, offspring (one or many)", "çocuk, evlât (tekil ve çoğul için)"),
 "asaba": ("to hit the mark; to strike, to befall (Form IV, hollow)", "isabet etmek; çarpmak, başa gelmek (if'âl, ecvef)"),
 "akhtaa": ("to miss the mark; to err (Form IV; أَخْطَأَ يُخْطِئُ)", "ıskalamak; hata etmek (if'âl; أَخْطَأَ يُخْطِئُ)"),
 "wajada": ("to find; with two objects, to find to be; (passive) to be found", "bulmak; iki mef'ûlle: … olarak bulmak; (meçhul) bulunmak"),
 "raa": ("to see; with two objects, to know, to deem", "görmek; iki mef'ûlle: bilmek, saymak"),
 "birr": ("goodness, right dealing — a name that gathers every kind of good", "iyilik, hayır — bütün hayır hasletlerini toplayan isim"),
 "ulya": ("highest (the feminine of أَعْلَى); the highest rank", "en yüce (أَعْلَى'nın müennesi); en yüksek mertebe"),
 "silah": ("weapons, arms", "silah"),
 "maruf": ("kindness, a good deed, fair dealing (ism maf'ul of عَرَفَ: the known good)", "iyilik, güzel muamele (عَرَفَ'den ism-i mef'ûl: bilinen iyilik)"),
 "tawahhum": ("conjecture, taking thought; fancying (masdar of Form V تَوَهَّمَ)", "tahmin, zihnen canlandırma; vehmetme (tefa''ul bâbından masdar)"),
 "nahada": ("to rise, to get up", "kalkmak, doğrulmak"),
 "saima": ("to be weary of, to tire of (سَئِمَ يَسْأَمُ)", "usanmak, bıkmak (سَئِمَ يَسْأَمُ)"),
 "qarya": ("a village, a town (pl. قُرًى)", "köy, kasaba (ç. قُرًى)"),
 "istaghna": ("to do without, to have no need of (Form X, naqis; with عَنْ)", "müstağni olmak, ihtiyaç duymamak (istif'âl, nâkıs; عَنْ ile)"),
}
_sg1 = _sg.sound1
def N(lemma, root, en, tr, plural=None, pos="noun"):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": 6}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
def P(lemma, en, tr): return {"lemma": lemma, "pos": "propn", "gloss": {"en": en, "tr": tr}, "level": 6}
def VB(lemma, root, en, tr, form=None):
    e = {"lemma": lemma, "pos": "verb", "gloss": {"en": en, "tr": tr}, "level": 6, "root": root}
    if form: e["form"] = form
    return e
def PHRASE(lemma, g_en, g_tr, l_en, l_tr, n_en, n_tr):
    return {"lemma": lemma, "pos": "phrase", "level": 6, "gloss": {"en": g_en, "tr": g_tr}, "literal": {"en": l_en, "tr": l_tr}, "note": {"en": n_en, "tr": n_tr}}

NEW_GLOSS = {
 # ---- the khabar ----
 "ubayda": P("عُبَيْدَة", "ʿUbayda — in the kunya Abū ʿUbayda; a diptote (a name with the feminine ta)", "Ubeyde — «Ebû Ubeyde» künyesinde; gayr-i munsarif (lafzî te'nîsli alem)"),
 "abu-ubayda": PHRASE("أَبُو عُبَيْدَةَ", "Abū ʿUbayda — Maʿmar ibn al-Muthannā (d. c. 209 AH), the Basran master of the Arabs' language, lore and battle-days", "Ebû Ubeyde — Ma'mer b. el-Müsennâ (ö. yak. 209 h.), Basralı dil, ahbâr ve eyyâmü'l-Arab âlimi",
    "literally «father of ʿUbayda»", "lafzen «Ubeyde'nin babası»",
    "A kunya built as an idafa: أَبُو is one of the five nouns and takes the case of its seat (أَبُو، أَبَا، أَبِي); عُبَيْدَةَ stays in jarr by the fatha, a diptote.",
    "İzâfetle kurulmuş künye: أَبُو esmâ-i hamsedendir ve bulunduğu yerin i'râbını alır (أَبُو، أَبَا، أَبِي); عُبَيْدَةَ gayr-i munsarif olduğu için fetha ile mecrûr kalır."),
 "ala-name": P("الْعَلَاء", "al-ʿAlāʾ — the father of Abū ʿAmr ibn al-ʿAlāʾ", "Alâ — Ebû Amr b. el-Alâ'nın babası"),
 "abu-amr-ibn-al-ala": PHRASE("أَبُو عَمْرِو بْنُ الْعَلَاءِ", "Abū ʿAmr ibn al-ʿAlāʾ (d. 154 AH) — the Basran reader of the Qurʾān, one of the Seven, and the first great authority on the Arabs' verse", "Ebû Amr b. el-Alâ (ö. 154 h.) — Basralı kıraat imamı, yedi kurrâdan biri ve Arap şiirinin ilk büyük otoritesi",
    "literally «the father of ʿAmr, son of al-ʿAlāʾ»", "lafzen «Amr'ın babası, Alâ'nın oğlu»",
    "أَبُو takes the case of its seat; عَمْرٍو loses its tanwin before «son of» + a name; بْن follows أَبُو in case and is written without its alif between two names.",
    "أَبُو bulunduğu yerin i'râbını alır; عَمْرٍو, «ibn» + alemden önce tenvinini kaybeder; بْن i'râbda أَبُو'ya uyar ve iki alem arasında elifsiz yazılır."),
 "farazdaq": P("الْفَرَزْدَق", "al-Farazdaq — the byname of Hammām ibn Ghālib of Tamīm (d. c. 110 AH), one of the three great Umayyad poets", "Ferezdak — Temîmli Hemmâm b. Gâlib'in (ö. yak. 110 h.) lakabı; Emevî devrinin üç büyük şairinden biri"),
 "hutaya": P("الْحُطَيْئَة", "al-Ḥuṭayʾa — the byname of Jarwal ibn Aws of ʿAbs, a poet of both the Jāhiliyya and Islam, Zuhayr's reciter", "Hutay'e — Absli Cervel b. Evs'in lakabı; hem câhiliyeyi hem İslâm'ı idrak etmiş şair, Züheyr'in râvisi"),
 "asmai-zuhayr-unused": None,
 "amdah": N("أَمْدَح", "م د ح", "better / best at praise (the elative of مَدَحَ)", "daha / en iyi medheden (مَدَحَ'den ism-i tafdîl)"),
 "asr-weave": N("أَسْر", "أ س ر", "the tight binding of a thing's make, firm build — أَسْرُ الشِّعْرِ: the close weave of verse", "bir şeyin yapısının sıkı örülmesi, sağlam kuruluş — أَسْرُ الشِّعْرِ: şiirin sağlam örgüsü"),
 "naqqaha": VB("نَقَّحَ", "ن ق ح", "to prune and refine (speech, verse), to sift its good from its bad (Form II)", "(sözü, şiiri) budayıp düzeltmek, iyisini kötüsünden ayıklamak (tef'îl)", "II"),
 "matbu-gifted": N("مَطْبُوع", "ط ب ع", "a poet by nature, one who composes without labour (ism maf'ul of طَبَعَ)", "tabiatıyla şair olan, zorlanmadan söyleyen (طَبَعَ'den ism-i mef'ûl)"),
 "kubra": N("كُبْرَى", "ك ب ر", "greatest (the feminine of أَكْبَر; pl. كُبَر)", "en büyük (أَكْبَر'in müennesi; ç. كُبَر)", plural="كُبَر"),
 "qasida": N("قَصِيدَة", "ق ص د", "an ode, a poem of full length (pl. قَصَائِد)", "kaside, uzun şiir (ç. قَصَائِد)", plural="قَصَائِد"),
 "hawliyyat": N("الْحَوْلِيَّات", "ح و ل", "«the year-long ones» — Zuhayr's name for his great odes, each worked over for a whole year (a nisba to حَوْل «year»)", "«Havliyyât» (yıllıklar) — Züheyr'in, her biri üzerinde bir yıl çalıştığı büyük kasidelerine verdiği ad (حَوْل «yıl»a nisbet)"),
 "harim": P("هَرِم", "Harim — Harim ibn Sinān al-Murrī, the lord of Dhubyān whom Zuhayr praised", "Herim — Herim b. Sinân el-Mürrî; Züheyr'in medhettiği Zübyân efendisi"),
 "sinan-name": P("سِنَان", "Sinān — Sinān ibn Abī Ḥāritha al-Murrī, Harim's father", "Sinân — Sinân b. Ebî Hârise el-Mürrî; Herim'in babası"),
 "harim-ibn-sinan": PHRASE("هَرِمُ بْنُ سِنَانٍ", "Harim ibn Sinān al-Murrī — one of the two lords who made peace between ʿAbs and Dhubyān and bore the blood-money", "Herim b. Sinân el-Mürrî — Abs ile Zübyân arasında barışı kurup diyetleri üstlenen iki efendiden biri",
    "literally «Harim son of Sinān»", "lafzen «Sinân oğlu Herim»",
    "هَرِم takes the case of its seat and loses its tanwin before «son of» + a name; بْن follows it in case; سِنَانٍ is the second term of the idafa.",
    "هَرِم bulunduğu yerin i'râbını alır ve «ibn» + alemden önce tenvinini kaybeder; بْن i'râbda ona uyar; سِنَانٍ muzâfun ileyhtir."),
 "murri": N("الْمُرِّيّ", "م ر ر", "al-Murrī — of the clan of Murra ibn ʿAwf, of Dhubyān (a nisba)", "Mürrî — Zübyân'dan Mürre b. Avf oymağına mensup (nisbet)"),
 "ajzala": VB("أَجْزَلَ", "ج ز ل", "to give richly, to make (a gift) large (Form IV)", "bol bol vermek, (atâyı) büyük tutmak (if'âl)", "IV"),
 # ---- the ruins ----
 "awfa-name": P("أَوْفَى", "Awfā — in the kunya Umm Awfā; a diptote (a name on a verb's pattern)", "Evfâ — «Ümmü Evfâ» künyesinde; gayr-i munsarif (fiil vezninde alem)"),
 "umm-awfa": PHRASE("أُمُّ أَوْفَى", "Umm Awfā — the kunya of the beloved whose deserted camp opens the ode", "Ümmü Evfâ — kasidenin, terk edilmiş yurduyla açıldığı sevgilinin künyesi",
    "literally «mother of Awfā»", "lafzen «Evfâ'nın annesi»",
    "A kunya built as an idafa: أُمّ takes the case of its seat, and أَوْفَى stays in jarr — by a fatha estimated on its alif, for it is a diptote.",
    "İzâfetle kurulmuş künye: أُمّ bulunduğu yerin i'râbını alır; أَوْفَى mecrûr kalır — gayr-i munsarif olduğu için elifi üzerinde takdîrî fetha ile."),
 "dimna": N("دِمْنَة", "د م ن", "the blackened trace of a camp — what dung, ashes and the like have darkened (pl. دِمَن)", "yurt izi — gübre, kül ve benzeri şeylerle kararmış konak kalıntısı (ç. دِمَن)", plural="دِمَن"),
 "hawmana": N("حَوْمَانَة", "ح و م", "a stretch of hard, rough ground — here in the place-name حَوْمَانَةُ الدَّرَّاجِ", "sert ve engebeli arazi — burada حَوْمَانَةُ الدَّرَّاجِ yer adında"),
 "darraj": P("الدَّرَّاج", "al-Darrāj — a place; حَوْمَانَةُ الدَّرَّاجِ is one of the two sites of Umm Awfā's camp", "Derrâc — bir yer; حَوْمَانَةُ الدَّرَّاجِ Ümmü Evfâ'nın yurdunun bulunduğu iki yerden biri"),
 "mutathallam": P("الْمُتَثَلَّم", "al-Mutathallam — a place, the second site of Umm Awfā's camp", "Mütesellem — bir yer; Ümmü Evfâ'nın yurdunun ikinci yeri"),
 "raqmatan": P("الرَّقْمَتَانِ", "al-Raqmatān — «the two Raqmas»: two lava-tracts, one near Basra and one near Medina (a dual)", "Rakmetân — «iki Rakme»: biri Basra'ya, biri Medine'ye yakın iki kara taşlık (tesniye)"),
 "marju-retraced": N("مَرْجُوع", "ر ج ع", "gone over again — of a tattoo: its lines retraced and renewed (pl. مَرَاجِيع)", "üzerinden yeniden geçilmiş — dövme için: çizgileri tekrarlanıp yenilenmiş (ç. مَرَاجِيع)", plural="مَرَاجِيع"),
 "washm": N("وَشْم", "و ش م", "a tattoo", "dövme"),
 "nashir": N("نَاشِر", "ن ش ر", "a sinew or vein of the forearm (pl. نَوَاشِر)", "ön koldaki damar yahut sinir (ç. نَوَاشِر)", plural="نَوَاشِر"),
 "misam": N("مِعْصَم", "ع ص م", "the wrist, the place of the bracelet (pl. مَعَاصِم)", "bilek, bileziğin takıldığı yer (ç. مَعَاصِم)", plural="مَعَاصِم"),
 "ayan-wide-eyed": N("أَعْيَن", "ع ي ن", "wide-eyed (fem. عَيْنَاء, pl. عِين) — الْعِينُ: the wild cows, named by their eyes", "iri gözlü (müennesi عَيْنَاء, ç. عِين) — الْعِينُ: gözleriyle anılan yaban sığırları", plural="عِين"),
 "rim": N("رِئْم", "ر أ م", "the pure-white gazelle (pl. أَرْآم)", "bembeyaz ceylan (ç. أَرْآم)", plural="أَرْآم"),
 "khilfa": N("خِلْفَة", "خ ل ف", "one after another, in turns: when one herd passes another comes", "birbiri ardınca, nöbetleşe: bir sürü gidince öbürü gelir"),
 "tala-fawn": N("طَلًا", "ط ل و", "the young of the gazelle and the wild cow, from birth to a month or so (pl. أَطْلَاء)", "ceylan ve yaban sığırı yavrusu; doğumdan bir ay kadar sonrasına dek (ç. أَطْلَاء)", plural="أَطْلَاء"),
 "majtham": N("مَجْثَم", "ج ث م", "the spot where a beast or bird lies down (a noun of place from جَثَمَ)", "hayvanın yahut kuşun çöküp yattığı yer (جَثَمَ'den ism-i mekân)"),
 "hijja-year": N("حِجَّة", "ح ج ج", "a year (pl. حِجَج)", "yıl (ç. حِجَج)", plural="حِجَج"),
 "lay": N("لَأْي", "ل أ ي", "toil and hardship; لَأْيًا: only with effort, hardly", "zahmet ve meşakkat; لَأْيًا: güçlükle, zar zor"),
 "uthfiyya": N("أُثْفِيَّة", "أ ث ف", "a hearth-stone, one of the stones a cooking-pot is set on (pl. أَثَافِيّ)", "ocak taşı, üzerine kazan konan taşlardan biri (ç. أَثَافِيّ)", plural="أَثَافِيّ"),
 "asfa": N("أَسْفَع", "س ف ع", "soot-black, blackened by fire (fem. سَفْعَاء, pl. سُفْع)", "isten kararmış, ateşten siyahlaşmış (müennesi سَفْعَاء, ç. سُفْع)", plural="سُفْع"),
 "muarras": N("مُعَرَّس", "ع ر س", "a halting-place (from تَعْرِيس, a traveller's halt before dawn) — here the spot where the cauldron is set", "konak yeri (تَعْرِيس'ten: yolcunun seher vakti konaklaması) — burada kazanın kurulduğu yer"),
 "mirjal": N("مِرْجَل", "ر ج ل", "a cauldron, a cooking-pot (pl. مَرَاجِل)", "kazan, tencere (ç. مَرَاجِل)", plural="مَرَاجِل"),
 "nuy": N("نُؤْي", "ن أ ي", "the trench dug round a tent to carry off the rain (pl. آنَاء، نُئِيّ)", "yağmur suyunu akıtmak için çadırın çevresine kazılan ark (ç. آنَاء، نُئِيّ)"),
 "jidhm": N("جِذْم", "ج ذ م", "the base, the root of a thing", "bir şeyin dibi, kökü"),
 "tathallama": VB("تَثَلَّمَ", "ث ل م", "to be notched, to break down at the edge (Form V)", "gedik açılmak, kenarı yıkılmak (tefa''ul)", "V"),
 "rab": N("رَبْع", "ر ب ع", "a dwelling-ground, the place where a clan camps (pl. رُبُوع)", "konak yeri, bir oymağın konduğu yurt (ç. رُبُوع)", plural="رُبُوع"),
 # ---- the two lords ----
 "jurhum": P("جُرْهُم", "Jurhum — the ancient tribe among whom Ismāʿīl married, keepers of the Kaʿba before Khuzāʿa and Quraysh", "Cürhüm — Hz. İsmâil'in aralarından evlendiği eski kabile; Huzâa ve Kureyş'ten önce Kâbe'nin bakıcıları"),
 "sahil-thread": N("سَحِيل", "س ح ل", "a thread twisted of a single strand — a figure for the weak or easy case", "tek kat bükülmüş ip — zayıf yahut kolay hal için mecaz"),
 "mubram": N("مُبْرَم", "ب ر م", "a rope twisted of two strands or more, firm-plied — a figure for the strong or hard case (ism maf'ul of أَبْرَمَ)", "iki veya daha çok kat bükülmüş sağlam ip — kuvvetli yahut zor hal için mecaz (أَبْرَمَ'den ism-i mef'ûl)"),
 "tadaraka": VB("تَدَارَكَ", "د ر ك", "to reach a thing in time and set it right, to retrieve (Form VI)", "bir işe vaktinde yetişip düzeltmek, telâfi etmek (tefâ'ul)", "VI"),
 "abs": P("عَبْس", "ʿAbs — the tribe of Ghaṭafān that fought its sister-tribe Dhubyān in the war of Dāḥis and al-Ghabrāʾ", "Abs — Dâhis ve Gabrâ savaşında kardeş kabilesi Zübyân'la savaşan Gatafân kabilesi"),
 "dhubyan": P("ذُبْيَان", "Dhubyān — the tribe of Ghaṭafān, sister-tribe and foe of ʿAbs; a diptote", "Zübyân — Gatafân'dan bir kabile; Abs'ın kardeşi ve hasmı; gayr-i munsarif"),
 "tafana": VB("تَفَانَى", "ف ن ي", "to destroy one another, to wear each other out (Form VI, naqis)", "birbirini yok etmek, karşılıklı tükenmek (tefâ'ul, nâkıs)", "VI"),
 "daqqa": VB("دَقَّ", "د ق ق", "to pound, to crush (doubled; دَقَّ يَدُقُّ)", "dövmek, ezmek (muzâaf; دَقَّ يَدُقُّ)"),
 "manshim": P("مَنْشِم", "Manshim — a perfume-seller of the proverb: men who dipped their hands in her perfume to seal an oath were killed to the last, so «Manshim's perfume» became a byword for ruin", "Menşim — meseldeki ıtır satıcısı: yeminlerini pekiştirmek için ellerini onun ıtrına batıranlar son ferdine kadar öldürüldü; «Menşim'in ıtrı» böylece yıkımın darbımeseli oldu"),
 "silm": N("سِلْم", "س ل م", "peace, a truce (said with kasra or fatha; masculine and feminine)", "barış, sulh (sîn'i kesreli ve fethalı okunur; müzekker ve müennes)"),
 "mawtin": N("مَوْطِن", "و ط ن", "a place to stand, ground one takes (pl. مَوَاطِن)", "durulan yer, tutulan mevki (ç. مَوَاطِن)", plural="مَوَاطِن"),
 "uquq": N("عُقُوق", "ع ق ق", "defiance of one's kin, the breaking of the tie of kinship (masdar of عَقَّ)", "akrabaya isyan, sıla-i rahmi koparmak (عَقَّ'nin masdarı)"),
 "matham": N("مَأْثَم", "أ ث م", "sin, a sinful deed (a mimi masdar of أَثِمَ)", "günah (أَثِمَ'den mîmî masdar)"),
 "maadd-name": P("مَعَدّ", "Maʿadd — Maʿadd ibn ʿAdnān, forefather of the northern Arabs", "Maadd — Maadd b. Adnân; Adnânî Arapların atası"),
 "istabaha": VB("اِسْتَبَاحَ", "ب و ح", "to find a thing free for the taking and take it all (Form X, hollow)", "bir şeyi mubah bulup tamamını almak (istif'âl, ecvef)", "X"),
 "azuma": VB("عَظُمَ", "ع ظ م", "to be great, to grow great (عَظُمَ يَعْظُمُ)", "büyük olmak, büyümek (عَظُمَ يَعْظُمُ)"),
 # ---- war ----
 "murajjam": N("مُرَجَّم", "ر ج م", "guessed at — of a tale told by conjecture, not by knowledge (ism maf'ul of رَجَّمَ)", "zanla söylenmiş — bilgiye değil tahmine dayanan söz (رَجَّمَ'den ism-i mef'ûl)"),
 "dhamim": N("ذَمِيم", "ذ م م", "blamed, blameworthy (a فَعِيل in the sense of the passive participle)", "kınanmış, yerilmiş (mef'ûl anlamında faîl)"),
 "dariya": VB("ضَرِيَ", "ض ر ي", "to grow fierce, to become keen and savage (ضَرِيَ يَضْرَى)", "kızışmak, azgınlaşmak (ضَرِيَ يَضْرَى)"),
 "darra-whet": VB("ضَرَّى", "ض ر ي", "to set on to fierceness, to whet (Form II, naqis)", "azgınlığa sevk etmek, kışkırtmak (tef'îl, nâkıs)", "II"),
 "darima": VB("ضَرِمَ", "ض ر م", "to blaze, to flare up (of fire; ضَرِمَ يَضْرَمُ)", "alev almak, tutuşmak (ateş için; ضَرِمَ يَضْرَمُ)"),
 "araka": VB("عَرَكَ", "ع ر ك", "to rub hard, to grind down (عَرَكَ يَعْرُكُ)", "ovmak, ezip öğütmek (عَرَكَ يَعْرُكُ)"),
 "ark": N("عَرْك", "ع ر ك", "rubbing, grinding (masdar of عَرَكَ)", "ovma, ezip öğütme (عَرَكَ'nin masdarı)"),
 "thifal": N("ثِفَال", "ث ف ل", "the cloth or hide spread under a handmill to catch the flour", "un dökülsün diye el değirmeninin altına serilen bez yahut deri"),
 "laqiha": VB("لَقِحَ", "ل ق ح", "to conceive, to become pregnant (of a she-camel; لَقِحَ يَلْقَحُ)", "gebe kalmak (dişi deve için; لَقِحَ يَلْقَحُ)"),
 "kishaf": N("كِشَاف", "ك ش ف", "conceiving twice in one year, or year upon year without rest", "yılda iki kez yahut dinlenmeden her yıl gebe kalmak"),
 "atama-twin": VB("أَتْأَمَ", "ت أ م", "to bear twins (Form IV)", "ikiz doğurmak (if'âl)", "IV"),
 "antaja": VB("أَنْتَجَ", "ن ت ج", "to bring forth young, to give birth (of a she-camel; Form IV)", "yavrulamak, doğurmak (dişi deve için; if'âl)", "IV"),
 "ashamm": N("أَشْأَم", "ش أ م", "most ill-omened (the elative of شُؤْم; a diptote; pl. أَشَائِم)", "en uğursuz (شُؤْم'den ism-i tafdîl; gayr-i munsarif; ç. أَشَائِم)"),
 "fatama": VB("فَطَمَ", "ف ط م", "to wean (فَطَمَ يَفْطِمُ)", "sütten kesmek (فَطَمَ يَفْطِمُ)"),
 "aghalla": VB("أَغَلَّ", "غ ل ل", "to yield a crop, to bring in revenue (Form IV, doubled)", "mahsul vermek, gelir getirmek (if'âl, muzâaf)", "IV"),
 "qafiz": N("قَفِيز", "ق ف ز", "a qafīz — an old dry measure for grain (pl. أَقْفِزَة، قُفْزَان)", "kafîz — eski bir tahıl ölçeği (ç. أَقْفِزَة، قُفْزَان)"),
 # ---- the wisdom verses ----
 "takalif": N("تَكَالِيف", "ك ل ف", "burdens, hardships, the toils a thing lays on one (a plural)", "külfetler, meşakkatler, bir şeyin yüklediği sıkıntılar (cemi)"),
 "hawl-year": N("حَوْل", "ح و ل", "a year (pl. أَحْوَال)", "yıl (ç. أَحْوَال)", plural="أَحْوَال"),
 "amin-blind": N("عَمٍ", "ع م ي", "blind — above all blind of heart, unknowing (a manqūṣ: عَمٍ، الْعَمِي)", "kör — özellikle kalbi kör, bilmeyen (mankûs: عَمٍ، الْعَمِي)"),
 "khabt": N("خَبْط", "خ ب ط", "striking out with the forefoot, treading at random (masdar of خَبَطَ)", "ön ayağıyla vurmak, rastgele basmak (خَبَطَ'nin masdarı)"),
 "ashwa": N("عَشْوَاء", "ع ش و", "the night-blind she-camel, that treads without seeing (the feminine of أَعْشَى; a diptote)", "gece görmeyen, görmeden basan dişi deve (أَعْشَى'nın müennesi; gayr-i munsarif)"),
 "ammara-life": VB("عَمَّرَ", "ع م ر", "to give long life to; passive عُمِّرَ: to be granted a long life (Form II)", "uzun ömür vermek; meçhulü عُمِّرَ: ömrü uzatılmak (tef'îl)", "II"),
 "harima": VB("هَرِمَ", "ه ر م", "to grow very old, to reach decrepit age (هَرِمَ يَهْرَمُ)", "çok yaşlanmak, pîr-i fânî olmak (هَرِمَ يَهْرَمُ)"),
 "sanaa-deal": VB("صَانَعَ", "ص ن ع", "to deal gently with people, to humour and conciliate (Form III)", "insanlarla güzel geçinmek, idare etmek (müfâale)", "III"),
 "darrasa": VB("ضَرَّسَ", "ض ر س", "to bite hard with the teeth, to mangle (Form II; the intensive of ضَرَسَ)", "dişleriyle sertçe ısırmak, dişlemek (tef'îl; ضَرَسَ'nin mübalağası)", "II"),
 "mansim": N("مَنْسِم", "ن س م", "the foot-pad of a camel — what the hoof-tip is to a horse (pl. مَنَاسِم)", "devenin tabanı — atın tırnak ucu ne ise deve için o (ç. مَنَاسِم)", plural="مَنَاسِم"),
 "ird": N("عِرْض", "ع ر ض", "honour, good name — that in a man which is praised or blamed (pl. أَعْرَاض)", "ırz, şeref — insanın övülen yahut yerilen yönü (ç. أَعْرَاض)", plural="أَعْرَاض"),
 "wafara": VB("وَفَرَ", "و ف ر", "to make abundant, to keep whole and unimpaired (وَفَرَ يَفِرُ)", "çoğaltmak, eksiksiz ve dokunulmamış tutmak (وَفَرَ يَفِرُ)"),
 "shatm": N("شَتْم", "ش ت م", "abuse, reviling (masdar of شَتَمَ)", "sövme, hakaret (شَتَمَ'nin masdarı)"),
 "mutmainn": N("مُطْمَئِنّ", "ط م ن", "at rest, settled; that in which the heart rests easy (ism fa'il of اِطْمَأَنَّ)", "sükûn bulmuş, yatışmış; kalbin kendisiyle huzur bulduğu (اِطْمَأَنَّ'den ism-i fâil)"),
 "tajamjama": VB("تَجَمْجَمَ", "ج م ج م", "to falter, to hang back, to mumble and not speak out (a four-letter verb on تَفَعْلَلَ)", "duraksamak, tereddüt etmek, açıkça söylemeyip gevelemek (تَفَعْلَلَ vezninde rubâî mezîd)"),
 "raqiya": VB("رَقِيَ", "ر ق ي", "to climb, to go up (رَقِيَ يَرْقَى)", "çıkmak, tırmanmak (رَقِيَ يَرْقَى)"),
 "sullam": N("سُلَّم", "س ل م", "a ladder (pl. سَلَالِم)", "merdiven (ç. سَلَالِم)", plural="سَلَالِم"),
 "zujj": N("زُجّ", "ز ج ج", "the iron shoe at the foot of a spear (pl. زِجَاج)", "mızrağın dibine takılan demir (ç. زِجَاج)", plural="زِجَاج"),
 "lahdham": N("لَهْذَم", "ل ه ذ م", "a long, keen spear-blade (pl. لَهَاذِم)", "uzun, keskin mızrak temreni (ç. لَهَاذِم)", plural="لَهَاذِم"),
 "dhada": VB("ذَادَ", "ذ و د", "to drive off, to keep away from (ذَادَ يَذُودُ; with عَنْ)", "geri püskürtmek, uzak tutmak (ذَادَ يَذُودُ; عَنْ ile)"),
 "haddama": VB("هَدَّمَ", "ه د م", "to tear down utterly, to demolish (Form II; the intensive of هَدَمَ)", "büsbütün yıkmak (tef'îl; هَدَمَ'nin mübalağası)", "II"),
 "ightaraba": VB("اِغْتَرَبَ", "غ ر ب", "to go abroad, to live far from one's people and home (Form VIII)", "gurbete çıkmak, ehlinden ve vatanından uzak yaşamak (iftiâl)", "VIII"),
}
del NEW_GLOSS["asmai-zuhayr-unused"]

HOLLOW_N = "أَجْوَفُ: تُحْذَفُ عَيْنُهُ عِنْدَ السُّكُونِ — "
NEW_VERBS = {
 "araka": _sg1("nasara", "عَرَك", "عْرُك", "اُعْرُك", "عَرْك", "عَارِك", "مَعْرُوك", "عُرِكَ", "يُعْرَكُ"),
 "azuma": _sg1("karuma", "عَظُم", "عْظُم", "اُعْظُم", "عِظَم", "عَظِيم", note="لَازِمٌ، وَالْوَصْفُ مِنْهُ عَظِيمٌ عَلَى فَعِيلٍ."),
 "darima": _sg1("samia", "ضَرِم", "ضْرَم", "اِضْرَم", "ضَرَم", "ضَرِم", note="ضَرِمَتِ النَّارُ تَضْرَمُ ضَرَمًا: الْتَهَبَتْ — لَازِمٌ، وَالْوَصْفُ مِنْهُ ضَرِمٌ."),
 "fatama": _sg1("daraba", "فَطَم", "فْطِم", "اِفْطِم", "فَطْم / فِطَام", "فَاطِم", "مَفْطُوم", "فُطِمَ", "يُفْطَمُ"),
 "harima": _sg1("samia", "هَرِم", "هْرَم", "اِهْرَم", "هَرَم", "هَرِم", note="لَازِمٌ، وَالْوَصْفُ مِنْهُ هَرِمٌ."),
 "laqiha": _sg1("samia", "لَقِح", "لْقَح", "اِلْقَح", "لَقَح / لَقَاح", "لَاقِح", note="لَقِحَتِ النَّاقَةُ تَلْقَحُ: حَمَلَتْ — لَازِمٌ."),
 "daqqa": _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "دَقّ", "دَاقّ", _sg.mazi14("دَقّ", "دَقَق"), _sg.mudari14("َ", "دُقّ", "دْقُق"),
     ["دُقَّ", "دُقَّا", "دُقُّوا", "دُقِّي", "دُقَّا", "اُدْقُقْنَ"], "يَدُقَّ", "يَدُقَّ", "تَدُقَّ", "مَدْقُوق", "دُقَّ", "يُدَقُّ",
     "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ لِلتَّخَلُّصِ مِنَ الْتِقَاءِ السَّاكِنَيْنِ — لَمْ يَدُقَّ، وَيَجُوزُ لَمْ يَدْقُقْ."),
 "dariya": _sg.naqis1("samia", "نَاقِصٌ", "y", "ضَرِ", "ضْر", "a", "اِضْر", "ضَرًى / ضَرَاوَة", "ضَارٍ (الضَّارِي)", note="نَاقِصٌ: ضَرِيَ يَضْرَى — لَمْ يَضْرَ، بِحَذْفِ الْأَلِفِ."),
 "raqiya": _sg.naqis1("samia", "نَاقِصٌ يَائِيٌّ", "y", "رَقِ", "رْق", "a", "اِرْق", "رُقِيّ", "رَاقٍ (الرَّاقِي)", note="نَاقِصٌ: رَقِيَ يَرْقَى — لَمْ يَرْقَ، بِحَذْفِ الْأَلِفِ."),
 "dhada": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "ذَاد", "ذُد", "ذُود", "ذُد", "ذُود", "ذُد", "ذَوْد / ذِيَاد", "ذَائِد", "مَذُود", "ذِيدَ", "يُذَادُ", HOLLOW_N + "يَذُودُ ← لَمْ يَذُدْ."),
 "wafara": _sg.entry("مِنْ بَابِ ضَرَبَ يَضْرِبُ — مِثَالٌ وَاوِيٌّ", "فَعَلَ يَفْعِلُ", "وَفْر", "وَافِر", _sg.mazi14("وَفَر"), _sg.mudari14("َ", "فِر"), _sg.amr_attach("فِر"),
     "يَفِرَ", "يَفِرْ", "تَفِرْ", "مَوْفُور", "وُفِرَ", "يُوفَرُ", "مِثَالٌ وَاوِيٌّ: تُحْذَفُ وَاوُهُ فِي الْمُضَارِعِ وَالْأَمْرِ — يَفِرُ، فِرْ؛ وَفَرْتُ الشَّيْءَ أَفِرُهُ وَفْرًا: أَكْثَرْتُهُ (الزَّوْزَنِيُّ)."),
 "naqqaha": _sg.derived(_sg.B2, _sg.W2, "ُ", "نَقَّح", "نَقِّح", "نَقِّح", "تَنْقِيح", "مُنَقِّح", "مُنَقَّح", "نُقِّحَ", "يُنَقَّحُ"),
 "ammara-life": _sg.derived(_sg.B2, _sg.W2, "ُ", "عَمَّر", "عَمِّر", "عَمِّر", "تَعْمِير", "مُعَمِّر", "مُعَمَّر", "عُمِّرَ", "يُعَمَّرُ"),
 "darrasa": _sg.derived(_sg.B2, _sg.W2, "ُ", "ضَرَّس", "ضَرِّس", "ضَرِّس", "تَضْرِيس", "مُضَرِّس", "مُضَرَّس", "ضُرِّسَ", "يُضَرَّسُ"),
 "haddama": _sg.derived(_sg.B2, _sg.W2, "ُ", "هَدَّم", "هَدِّم", "هَدِّم", "تَهْدِيم", "مُهَدِّم", "مُهَدَّم", "هُدِّمَ", "يُهَدَّمُ"),
 "darra-whet": _sg.derived_naqis(_sg.B2 + " — نَاقِصٌ", _sg.W2, "ُ", "ضَرَّ", "ضَرّ", "i", "ضَرّ", "تَضْرِيَة", "مُضَرٍّ", "مُضَرًّى", "ضُرِّيَ", "يُضَرَّى", "نَاقِصٌ مِنَ التَّفْعِيلِ: يُضَرِّي ← لَمْ يُضَرِّ."),
 "sanaa-deal": _sg.derived(_sg.B3, _sg.W3, "ُ", "صَانَع", "صَانِع", "صَانِع", "مُصَانَعَة", "مُصَانِع", "مُصَانَع", "صُونِعَ", "يُصَانَعُ"),
 "ajzala": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَجْزَل", "جْزِل", "أَجْزِل", "إِجْزَال", "مُجْزِل", "مُجْزَل", "أُجْزِلَ", "يُجْزَلُ"),
 "antaja": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْتَج", "نْتِج", "أَنْتِج", "إِنْتَاج", "مُنْتِج", note="أَنْتَجَتِ النَّاقَةُ: وَلَدَتْ."),
 "atama-twin": _sg.derived(_sg.B4 + " — مَهْمُوزُ الْعَيْنِ", _sg.W4, "ُ", "أَتْأَم", "تْئِم", "أَتْئِم", "إِتْآم", "مُتْئِم", note="أَتْأَمَتِ الْأُنْثَى: وَلَدَتْ تَوْأَمَيْنِ — لَازِمٌ."),
 "aghalla": _sg.entry(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "إِغْلَال", "مُغِلّ", _sg.mazi14("أَغَلّ", "أَغْلَل"), _sg.mudari14("ُ", "غِلّ", "غْلِل"),
     ["أَغِلَّ", "أَغِلَّا", "أَغِلُّوا", "أَغِلِّي", "أَغِلَّا", "أَغْلِلْنَ"], "يُغِلَّ", "يُغِلَّ", "تُغِلَّ",
     note="أَغَلَّتِ الْأَرْضُ: صَارَتْ ذَاتَ غَلَّةٍ — مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ (لَمْ يُغِلَّ)، وَأَهْلُ الْحِجَازِ يَفُكُّونَ الْإِدْغَامَ: لَمْ يُغْلِلْ، وَعَلَيْهِ «فَتُغْلِلْ» فِي الْمُعَلَّقَةِ."),
 "tathallama": _sg.derived(_sg.B5, _sg.W5, "َ", "تَثَلَّم", "تَثَلَّم", "تَثَلَّم", "تَثَلُّم", "مُتَثَلِّم"),
 "tadaraka": _sg.derived(_sg.B6, _sg.W6, "َ", "تَدَارَك", "تَدَارَك", "تَدَارَك", "تَدَارُك", "مُتَدَارِك", "مُتَدَارَك", "تُدُورِكَ", "يُتَدَارَكُ"),
 "tafana": _sg.derived_naqis(_sg.B6 + " — نَاقِصٌ", _sg.W6, "َ", "تَفَانَ", "تَفَان", "a", "تَفَان", "تَفَانٍ (التَّفَانِي)", "مُتَفَانٍ", note="نَاقِصٌ مِنَ التَّفَاعُلِ: تَفَانَوْا — تَشَارَكُوا فِي الْفَنَاءِ."),
 "ightaraba": _sg.derived(_sg.B8, _sg.W8, "َ", "اِغْتَرَب", "غْتَرِب", "اِغْتَرِب", "اِغْتِرَاب", "مُغْتَرِب"),
 "istabaha": _sg.derived_hollow(_sg.B10 + " — أَجْوَفُ", _sg.W10, "َ", "اِسْتَبَاح", "اِسْتَبَح", "سْتَبِيح", "سْتَبِح", "اِسْتَبِيح", "اِسْتَبِح", "اِسْتِبَاحَة", "مُسْتَبِيح", "مُسْتَبَاح", "اُسْتُبِيحَ", "يُسْتَبَاحُ",
     "أَجْوَفُ مِنَ الِاسْتِفْعَالِ: يَسْتَبِيحُ ← لَمْ يَسْتَبِحْ."),
 "tajamjama": _sg.derived("مَزِيدُ الرُّبَاعِيِّ: تَفَعْلَلَ يَتَفَعْلَلُ", "تَفَعْلَلَ يَتَفَعْلَلُ", "َ", "تَجَمْجَم", "تَجَمْجَم", "تَجَمْجَم", "تَجَمْجُم", "مُتَجَمْجِم"),
}
# ---- vv. 7–15 ----
NEW_GLOSS.update({
 "tabassara": VB("تَبَصَّرَ", "ب ص ر", "to look closely, to look and consider (Form V)", "dikkatle bakmak, bakıp düşünmek (tefa''ul)", "V"),
 "zaina": N("ظَعِينَة", "ظ ع ن", "a woman riding in her litter on the march — so called because she travels (تَظْعَنُ) with her husband (pl. ظَعَائِن)", "göç sırasında hevdeçte giden kadın — kocasıyla göç ettiği (تَظْعَنُ) için böyle denir (ç. ظَعَائِن)", plural="ظَعَائِن"),
 "jurthum": P("جُرْثُم", "Jurthum — the name of a watering-place", "Cürsüm — bir suyun adı"),
 "qanan": P("الْقَنَان", "al-Qanān — a mountain of the Banū Asad", "Kanân — Benî Esed'e ait bir dağ"),
 "hazn": N("حَزْن", "ح ز ن", "hard, rugged ground (pl. حُزُون)", "sert, engebeli arazi (ç. حُزُون)", plural="حُزُون"),
 "muhill": N("مُحِلّ", "ح ل ل", "one who is out of the sacred state or the sacred months; one under no sacred bond (ism fa'il of أَحَلَّ)", "ihramdan yahut haram aylardan çıkmış kimse; hürmeti olmayan (أَحَلَّ'den ism-i fâil)"),
 "muhrim": N("مُحْرِم", "ح ر م", "one who is in the sacred state or the sacred months; one under a sacred bond (ism fa'il of أَحْرَمَ)", "ihramda yahut haram aylarda olan kimse; hürmeti olan (أَحْرَمَ'den ism-i fâil)"),
 "atiq-noble": N("عَتِيق", "ع ت ق", "noble, choice, of old and fine make (pl. عِتَاق)", "değerli, seçkin, eski ve soylu (ç. عِتَاق)", plural="عِتَاق"),
 "killa": N("كِلَّة", "ك ل ل", "a thin veil or curtain (pl. كِلَل)", "ince perde, örtü (ç. كِلَل)", plural="كِلَل"),
 "ward-red": N("وَرْد", "و ر د", "red, rose-coloured — of a thing whose colour runs to red (pl. وِرَاد)", "kırmızı, gül renkli — rengi kırmızıya çalan (ç. وِرَاد)", plural="وِرَاد"),
 "mushakih": N("مُشَاكِه", "ش ك ه", "resembling, like (ism fa'il of شَاكَهَ «to resemble»)", "benzeyen (شَاكَهَ «benzedi»den ism-i fâil)"),
 "warraka": VB("وَرَّكَ", "و ر ك", "to ride on the haunch of a beast, sitting sideways; to turn aside into (Form II)", "bineğin sağrısına yan binmek; bir yere sapmak (tef'îl)", "II"),
 "suban": P("السُّوبَان", "al-Sūbān — the proper name of a valley and its high ground", "Sûbân — bir vadinin ve yüksek arazisinin özel adı"),
 "dall-coquetry": N("دَلّ", "د ل ل", "a woman's winning airs, coquetry — the same as دَلَال", "naz, eda, işve — دَلَال ile aynı"),
 "mutanaim": N("مُتَنَعِّم", "ن ع م", "one who lives delicately and makes a show of it (ism fa'il of تَنَعَّمَ)", "nazlı büyümüş, refahını gösteren (تَنَعَّمَ'den ism-i fâil)"),
 "bakara": VB("بَكَرَ", "ب ك ر", "to set out in the early morning (بَكَرَ يَبْكُرُ)", "sabah erkenden yola çıkmak (بَكَرَ يَبْكُرُ)"),
 "bukur": N("بُكُور", "ب ك ر", "setting out in the early morning (masdar of بَكَرَ)", "sabah erkenden çıkış (بَكَرَ'nin masdarı)"),
 "istahara": VB("اِسْتَحَرَ", "س ح ر", "to travel in the last of the night, before dawn (Form X)", "seher vakti yola çıkmak (istif'âl)", "X"),
 "suhra": N("سُحْرَة", "س ح ر", "the hour before dawn — a name for السَّحَر", "seher vakti — السَّحَر için bir isim"),
 "rass": P("الرَّسّ", "al-Rass — وَادِي الرَّسِّ is a particular valley on the women's road", "Ress — وَادِي الرَّسِّ, kadınların yolu üzerindeki belirli bir vadi"),
 "malha": N("مَلْهًى", "ل ه و", "amusement, or a place of amusement (a maqṣūr; pl. مَلَاهٍ)", "eğlence yahut eğlence yeri (maksûr; ç. مَلَاهٍ)", plural="مَلَاهٍ"),
 "aniq": N("أَنِيق", "أ ن ق", "charming, pleasing to look at (a فَعِيل in the sense of مُفْعِل)", "hoşa giden, göz alıcı (müf'il anlamında faîl)"),
 "mutawassim": N("مُتَوَسِّم", "و س م", "one who reads the signs, who looks closely and traces a thing's beauties (ism fa'il of تَوَسَّمَ)", "alâmetleri okuyan, dikkatle süzüp güzellikleri izleyen (تَوَسَّمَ'den ism-i fâil)"),
 "futat": N("فُتَات", "ف ت ت", "crumbs, bits broken off and scattered", "kırıntı, kopup dağılan parçalar"),
 "ihn": N("عِهْن", "ع ه ن", "dyed wool (pl. عُهُون)", "boyalı yün (ç. عُهُون)", plural="عُهُون"),
 "habb-grain": N("حَبّ", "ح ب ب", "grain, seeds, berries (a collective; one: حَبَّة)", "tane, tohum (cins ismi; teki: حَبَّة)"),
 "fana-berry": N("الْفَنَا", "ف ن و", "«fox-grape», black nightshade — a plant with small red berries (a maqṣūr)", "it üzümü — küçük kırmızı taneli bir bitki (maksûr)"),
 "hattama": VB("حَطَّمَ", "ح ط م", "to crush, to break to pieces (Form II; the intensive of حَطَمَ)", "ezmek, paramparça etmek (tef'îl; حَطَمَ'nin mübalağası)", "II"),
 "azraq": N("أَزْرَق", "ز ر ق", "blue; of water or a blade: very clear, bright (a diptote; pl. زُرْق)", "mavi; su ve kılıç için: dupduru, parlak (gayr-i munsarif; ç. زُرْق)", plural="زُرْق"),
 "jamm-water": N("جَمّ", "ج م م", "the water that gathers in a well or a trough (pl. جِمَام)", "kuyuda ve havuzda biriken su (ç. جِمَام)", plural="جِمَام"),
 "mutakhayyim": N("مُتَخَيِّم", "خ ي م", "one who pitches his tent, who camps to stay (ism fa'il of تَخَيَّمَ)", "çadır kuran, yerleşmek üzere konan (تَخَيَّمَ'den ism-i fâil)"),
 "jazaa-cross": VB("جَزَعَ", "ج ز ع", "to cut across (a valley), to cross it (جَزَعَ يَجْزَعُ)", "(vadiyi) enine kesmek, geçmek (جَزَعَ يَجْزَعُ)"),
 "qayni": N("قَيْنِيّ", "ق ي ن", "made by a قَيْن — a craftsman, here the saddle-maker (a nisba)", "«kayn»in — zanaatkârın, burada semer ustasının — yaptığı (nisbet)"),
 "qashib": N("قَشِيب", "ق ش ب", "new, fresh", "yeni, taze"),
 "mufam-wide": N("مُفْأَم", "ف أ م", "made wide and roomy — of a saddle or a litter (ism maf'ul of أَفْأَمَ)", "genişletilmiş, ferah yapılmış — semer yahut hevdeç için (أَفْأَمَ'den ism-i mef'ûl)"),
})
NEW_VERBS.update({
 "tabassara": _sg.derived(_sg.B5, _sg.W5, "َ", "تَبَصَّر", "تَبَصَّر", "تَبَصَّر", "تَبَصُّر", "مُتَبَصِّر"),
 "warraka": _sg.derived(_sg.B2, _sg.W2, "ُ", "وَرَّك", "وَرِّك", "وَرِّك", "تَوْرِيك", "مُوَرِّك"),
 "bakara": _sg1("nasara", "بَكَر", "بْكُر", "اُبْكُر", "بُكُور", "بَاكِر"),
 "istahara": _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَحَر", "سْتَحِر", "اِسْتَحِر", "اِسْتِحَار", "مُسْتَحِر"),
 "hattama": _sg.derived(_sg.B2, _sg.W2, "ُ", "حَطَّم", "حَطِّم", "حَطِّم", "تَحْطِيم", "مُحَطِّم", "مُحَطَّم", "حُطِّمَ", "يُحَطَّمُ"),
 "jazaa-cross": _sg1("fataha", "جَزَع", "جْزَع", "اِجْزَع", "جَزْع", "جَازِع", "مَجْزُوع", "جُزِعَ", "يُجْزَعُ"),
})
TAILOR.update({
 "khalil": ("an intimate friend (pl. أَخِلَّاء)", "candan dost (ç. أَخِلَّاء)"),
 "tahammala": ("to load up and move off; to bear, to endure (Form V)", "yükü yükleyip göç etmek; yüklenmek, katlanmak (tefa''ul)"),
 "alya": ("high ground; eminence (a mamdud)", "yüksek arazi; yücelik (memdûd)"),
 "ala-rise": ("to go up, to rise above; عَلَا بِـ: to raise, to put up (عَلَا يَعْلُو)", "yükselmek, üstüne çıkmak; عَلَا بِـ: yukarı kaldırmak (عَلَا يَعْلُو)"),
 "namat": ("a figured cloth that is spread out — here over a litter (pl. أَنْمَاط); a kind, a pattern", "serilen nakışlı örtü — burada hevdecin üzerine (ç. أَنْمَاط); tür, tarz"),
 "hashiya": ("edge, border, hem (pl. حَوَاشٍ); a retinue", "kenar, etek (ç. حَوَاشٍ); maiyet"),
 "matn": ("the raised, hard back of a land; a back, a surface; a text", "arazinin yükselmiş sert sırtı; sırt, yüzey; metin"),
 "naim-soft": ("living in ease; soft, smooth (ism fa'il)", "refah içinde yaşayan; yumuşak (ism-i fâil)"),
 "latif": ("refined, of nice taste; subtle, gentle", "zarif, ince zevkli; latîf"),
 "warada": ("to come down to water; to come, to arrive (وَرَدَ يَرِدُ)", "suya varmak; gelmek, ulaşmak (وَرَدَ يَرِدُ)"),
 "hadir": ("one settled at a water, a dweller; present", "su başına yerleşmiş, mukim; hazır"),
 "zahara": ("to appear; ظَهَرَ مِنْ: to come up out of", "görünmek; ظَهَرَ مِنْ: bir yerden yukarı çıkmak"),
 "asa-staff": ("a staff, a stick (a maqsur noun; pl. عِصِيّ)", "asâ, değnek (maksûr; ç. عِصِيّ)"),
})
# ---- vv. 22–27 ----
NEW_GLOSS.update({
 "affa-efface": VB("عَفَّى", "ع ف و", "to wipe out, to efface (Form II, naqis)", "silmek, izini yok etmek (tef'îl, nâkıs)", "II"),
 "najjama": VB("نَجَّمَ", "ن ج م", "to pay by instalments, at set times — «star by star» (Form II)", "taksit taksit, belirli vadelerle ödemek — «necim necim» (tef'îl)", "II"),
 "haraqa": VB("هَرَاقَ", "ر ي ق", "to shed, to pour out (blood, water) — a form of أَرَاقَ with ha for the hamza (هَرَاقَ يُهَرِيقُ)", "(kan, su) dökmek — hemze yerine hâ ile أَرَاقَ'nin bir lügati (هَرَاقَ يُهَرِيقُ)", "IV"),
 "mihjam": N("مِحْجَم", "ح ج م", "a cupping-glass, the cupper's instrument (pl. مَحَاجِم)", "hacamat şişesi, hacamatçının aleti (ç. مَحَاجِم)", plural="مَحَاجِم"),
 "tilad": N("تِلَاد", "ت ل د", "old, inherited wealth — the same as تَلِيد", "eskiden beri gelen, miras kalmış mal — تَلِيد ile aynı"),
 "maghnam": N("مَغْنَم", "غ ن م", "a spoil, a gain (pl. مَغَانِم)", "ganimet, kazanç (ç. مَغَانِم)", plural="مَغَانِم"),
 "afil": N("أَفِيل", "أ ف ل", "a young camel (pl. إِفَال)", "genç deve (ç. إِفَال)", plural="إِفَال"),
 "muzannam": N("مُزَنَّم", "ز ن م", "marked by a زَنَمَة — a strip cut from the ear and left hanging (ism maf'ul of زَنَّمَ)", "«zeneme» ile işaretlenmiş — kulaktan kesilip sarkık bırakılan parça (زَنَّمَ'den ism-i mef'ûl)"),
 "halif": N("حَلِيف", "ح ل ف", "a sworn ally, a confederate (pl. أَحْلَاف، حُلَفَاء)", "yeminli müttefik (ç. أَحْلَاف، حُلَفَاء)", plural="أَحْلَاف"),
 "muqsam": N("مُقْسَم", "ق س م", "swearing, an oath (a mimi masdar of أَقْسَمَ)", "yemin etme, yemin (أَقْسَمَ'den mîmî masdar)"),
 "katama": VB("كَتَمَ", "ك ت م", "to hide, to keep secret — كَتَمَهُ الشَّيْءَ: to keep a thing from him (كَتَمَ يَكْتُمُ)", "gizlemek, saklamak — كَتَمَهُ الشَّيْءَ: bir şeyi ondan gizlemek (كَتَمَ يَكْتُمُ)"),
 "ajjala-hasten": VB("عَجَّلَ", "ع ج ل", "to bring forward, to hasten (Form II)", "öne almak, çabuklaştırmak (tef'îl)", "II"),
})
NEW_VERBS.update({
 "affa-efface": _sg.derived_naqis(_sg.B2 + " — نَاقِصٌ", _sg.W2, "ُ", "عَفَّ", "عَفّ", "i", "عَفّ", "تَعْفِيَة", "مُعَفٍّ", "مُعَفًّى", "عُفِّيَ", "يُعَفَّى", "نَاقِصٌ مِنَ التَّفْعِيلِ: يُعَفِّي ← لَمْ يُعَفِّ."),
 "najjama": _sg.derived(_sg.B2, _sg.W2, "ُ", "نَجَّم", "نَجِّم", "نَجِّم", "تَنْجِيم", "مُنَجِّم", "مُنَجَّم", "نُجِّمَ", "يُنَجَّمُ"),
 "haraqa": _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ، وَالْهَاءُ بَدَلٌ مِنَ الْهَمْزَةِ", _sg.W4, "ُ", "هَرَاق", "هَرَق", "هَرِيق", "هَرِق", "هَرِيق", "هَرِق", "هِرَاقَة", "مُهَرِيق", "مُهَرَاق", "هُرِيقَ", "يُهَرَاقُ",
     "هَرَاقَ الْمَاءَ وَالدَّمَ يُهَرِيقُهُ: لُغَةٌ فِي أَرَاقَ يُرِيقُ، وَالْهَاءُ بَدَلٌ مِنَ الْهَمْزَةِ فَتَثْبُتُ مَفْتُوحَةً فِي الْمُضَارِعِ (الزَّوْزَنِيُّ)."),
 "katama": _sg1("nasara", "كَتَم", "كْتُم", "اُكْتُم", "كِتْمَان / كَتْم", "كَاتِم", "مَكْتُوم", "كُتِمَ", "يُكْتَمُ"),
 "ajjala-hasten": _sg.derived(_sg.B2, _sg.W2, "ُ", "عَجَّل", "عَجِّل", "عَجِّل", "تَعْجِيل", "مُعَجِّل", "مُعَجَّل", "عُجِّلَ", "يُعَجَّلُ"),
})
TAILOR.update({
 "kalm-wound": ("a wound (pl. كُلُوم، كِلَام)", "yara (ç. كُلُوم، كِلَام)"),
 "mil": ("as much as fills a vessel — مِلْءُ مِحْجَمٍ: a cupping-glass-full", "bir kabı dolduran miktar — مِلْءُ مِحْجَمٍ: bir hacamat şişesi dolusu"),
 "jara": ("to run, to flow; to take effect", "akmak, koşmak; cereyan etmek"),
 "risala": ("a message; messengership", "mesaj, haber; risâlet"),
 "naqama": ("to take vengeance, to punish; to resent, to hold against (نَقَمَ يَنْقِمُ)", "intikam almak, cezalandırmak; hoş görmemek (نَقَمَ يَنْقِمُ)"),
 "gharama": ("an indemnity, a debt one must pay", "tazminat, ödenmesi gereken borç"),
 "hisab": ("reckoning, account — يَوْمُ الْحِسَابِ: the Day of Reckoning", "hesap — يَوْمُ الْحِسَابِ: hesap günü"),
})
# ---- vv. 33–40 ----
NEW_GLOSS.update({
 "hayy-tribe": N("حَيّ", "ح ي ي", "a tribe, a tribal encampment (pl. أَحْيَاء)", "kabile, oymak (ç. أَحْيَاء)", plural="أَحْيَاء"),
 "husayn-murri": P("حُصَيْن", "Ḥuṣayn — Ḥuṣayn ibn Ḍamḍam al-Murrī of Dhubyān, who hid from the peace and killed a man of ʿAbs for his brother", "Husayn — Zübyân'dan Husayn b. Damdam el-Mürrî; barıştan gizlenip kardeşine karşılık Abs'tan bir adamı öldüren kişi"),
 "damdam": P("ضَمْضَم", "Ḍamḍam — the father of Ḥuṣayn and of Harim ibn Ḍamḍam, whom a man of ʿAbs had killed", "Damdam — Husayn'ın ve Abslı birinin öldürdüğü Herim b. Damdam'ın babası"),
 "husayn-ibn-damdam": PHRASE("حُصَيْنُ بْنُ ضَمْضَمٍ", "Ḥuṣayn ibn Ḍamḍam al-Murrī — the man of Dhubyān whose private vengeance, taken after the peace, nearly broke it", "Husayn b. Damdam el-Mürrî — barıştan sonra aldığı şahsî intikamla barışı neredeyse bozan Zübyânlı",
    "literally «Ḥuṣayn son of Ḍamḍam»", "lafzen «Damdam oğlu Husayn»",
    "حُصَيْن takes the case of its seat and loses its tanwin before «son of» + a name; بْن follows it in case; ضَمْضَمٍ is the second term of the idafa.",
    "حُصَيْن bulunduğu yerin i'râbını alır ve «ibn» + alemden önce tenvinini kaybeder; بْن i'râbda ona uyar; ضَمْضَمٍ muzâfun ileyhtir."),
 "aata-comply": VB("آتَى", "أ ت ي", "to fall in with, to suit, to go along with (Form III: آتَى يُؤَاتِي مُؤَاتَاةً)", "uymak, muvafakat etmek (müfâale: آتَى يُؤَاتِي مُؤَاتَاةً)", "III"),
 "kashh": N("كَشْح", "ك ش ح", "the flank, between the last rib and the hip — طَوَى كَشْحَهُ عَلَى كَذَا: he harboured it in his breast (pl. كُشُوح)", "böğür, son kaburga ile kalça arası — طَوَى كَشْحَهُ عَلَى كَذَا: onu içinde gizledi (ç. كُشُوح)", plural="كُشُوح"),
 "mustakinn": N("مُسْتَكِنّ", "ك ن ن", "hidden, lying concealed (ism fa'il of اِسْتَكَنَّ)", "gizli, saklı (اِسْتَكَنَّ'den ism-i fâil)"),
 "muljam": N("مُلْجَم", "ل ج م", "bridled (ism maf'ul of أَلْجَمَ)", "gem vurulmuş (أَلْجَمَ'den ism-i mef'ûl)"),
 "afzaa": VB("أَفْزَعَ", "ف ز ع", "to frighten, to startle (Form IV)", "korkutmak, ürkütmek (if'âl)", "IV"),
 "qasham": N("قَشْعَم", "ق ش ع م", "an old vulture — أُمُّ قَشْعَمٍ «the mother of Qashʿam»: Death; war (pl. قَشَاعِم)", "yaşlı akbaba — أُمُّ قَشْعَمٍ «Kaş'am'ın anası»: ölüm; harp (ç. قَشَاعِم)", plural="قَشَاعِم"),
 "umm-qasham": PHRASE("أُمُّ قَشْعَمٍ", "Death — «the mother of Qashʿam», a kunya of death (and of war, and of calamity)", "Ölüm — «Ümmü Kaş'am», ölümün (ayrıca harbin ve musibetin) künyesi",
    "literally «mother of the old vulture»", "lafzen «yaşlı akbabanın anası»",
    "A kunya built as an idafa: أُمّ takes the case of its seat, and قَشْعَمٍ is its second term, in jarr.",
    "İzâfetle kurulmuş künye: أُمّ bulunduğu yerin i'râbını alır; قَشْعَمٍ muzâfun ileyhtir, mecrûr."),
 "zim": N("ظِمْء", "ظ م أ", "the stretch between two waterings of the camels (pl. أَظْمَاء)", "develerin iki sulaması arasındaki süre (ç. أَظْمَاء)", plural="أَظْمَاء"),
 "tafarra": VB("تَفَرَّى", "ف ر ي", "to split open, to be cleft (Form V, naqis)", "yarılmak, çatlamak (tefa''ul, nâkıs)", "V"),
 "qadda-fulfil": VB("قَضَّى", "ق ض ي", "to carry through to the end, to complete (Form II, naqis; the same as قَضَى)", "sonuna kadar götürmek, tamamlamak (tef'îl, nâkıs; قَضَى ile aynı)", "II"),
 "kala": N("كَلَأ", "ك ل أ", "herbage, pasture", "ot, otlak"),
 "mustawbal": N("مُسْتَوْبَل", "و ب ل", "found heavy and unwholesome — وَبِيل (ism maf'ul of اِسْتَوْبَلَ)", "ağır ve hazmedilmez bulunan — وَبِيل (اِسْتَوْبَلَ'den ism-i mef'ûl)"),
 "mutawakhkham": N("مُتَوَخَّم", "و خ م", "found unwholesome, bad for the health — وَخِيم (ism maf'ul of تَوَخَّمَ)", "sağlığa zararlı bulunan — وَخِيم (تَوَخَّمَ'den ism-i mef'ûl)"),
})
NEW_VERBS.update({
 "aata-comply": _sg.derived_naqis(_sg.B3 + " — مَهْمُوزُ الْفَاءِ نَاقِصٌ", _sg.W3, "ُ", "آتَ", "ؤَات", "i", "آت", "مُؤَاتَاة", "مُؤَاتٍ", note="آتَاهُ عَلَى الْأَمْرِ يُؤَاتِيهِ مُؤَاتَاةً: وَافَقَهُ وَطَاوَعَهُ — مِنَ الْمُفَاعَلَةِ، وَلَيْسَ مِنْ «آتَى» بِمَعْنَى أَعْطَى."),
 "afzaa": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْزَع", "فْزِع", "أَفْزِع", "إِفْزَاع", "مُفْزِع", "مُفْزَع", "أُفْزِعَ", "يُفْزَعُ"),
 "tafarra": _sg.derived_naqis(_sg.B5 + " — نَاقِصٌ", _sg.W5, "َ", "تَفَرَّ", "تَفَرّ", "a", "تَفَرّ", "تَفَرٍّ (التَّفَرِّي)", "مُتَفَرٍّ", note="نَاقِصٌ مِنَ التَّفَعُّلِ: يَتَفَرَّى ← لَمْ يَتَفَرَّ."),
 "qadda-fulfil": _sg.derived_naqis(_sg.B2 + " — نَاقِصٌ", _sg.W2, "ُ", "قَضَّ", "قَضّ", "i", "قَضّ", "تَقْضِيَة", "مُقَضٍّ", "مُقَضًّى", "قُضِّيَ", "يُقَضَّى", "نَاقِصٌ مِنَ التَّفْعِيلِ: يُقَضِّي ← لَمْ يُقَضِّ."),
})
TAILOR.update({
 "jarra": ("to drag; جَرَّ عَلَيْهِ: to bring (a crime, a harm) upon him (doubled; جَرَّ يَجُرُّ)", "çekmek, sürüklemek; جَرَّ عَلَيْهِ: başına (bir cinayet, bir zarar) getirmek (muzâaf; جَرَّ يَجُرُّ)"),
 "shadda": ("to charge, to fall upon (شَدَّ عَلَى); to tighten (doubled: شَدَّ يَشُدُّ)", "hamle etmek, üzerine atılmak (شَدَّ عَلَى); sıkmak (muzâaf: شَدَّ يَشُدُّ)"),
 "lada": ("at, beside, in the presence of (a zarf, always annexed)", "yanında, nezdinde (zarf; daima muzâf)"),
 "alqa": ("to throw down, to cast (Form IV)", "atmak, yere bırakmak (if'âl)"),
 "rahl": ("a camel-saddle; a traveller's gear", "deve semeri; yolcunun eşyası"),
 "badaa": ("to begin; بَدَأَهُ بِـ: to be the first to do a thing to him", "başlamak; بَدَأَهُ بِـ: birine bir şeyi ilk yapan olmak"),
 "awrada": ("to bring (the herds) down to water; to bring forward (Form IV)", "(sürüyü) suya indirmek; öne sürmek (if'âl)"),
 "asdara": ("to bring (the herds) back from water — the opposite of أَوْرَدَ; to issue (Form IV)", "(sürüyü) sudan geri çevirmek — أَوْرَدَ'nin zıddı; çıkarmak (if'âl)"),
 "ghamr": ("deep, plentiful water (pl. غِمَار); abundant", "derin, bol su (ç. غِمَار); bol"),
 "tawa": ("to fold, to roll up — طَوَى كَشْحَهُ عَلَى: to keep hidden in the breast", "dürmek, katlamak — طَوَى كَشْحَهُ عَلَى: içinde gizlemek"),
 "qada-verb": ("to carry out, to fulfil (a need); to decree; to judge", "yerine getirmek, (ihtiyacı) gidermek; hükmetmek"),
 "raa-graze": ("to graze, to pasture (the herds) (naqis: رَعَى يَرْعَى)", "(sürüyü) otlatmak, otlamak (nâkıs: رَعَى يَرْعَى)"),
})
# ---- vv. 41–45 ----
NEW_GLOSS.update({
 "nahik": P("نَهِيك", "Nahīk — in ابْنُ نَهِيكٍ, one of those slain in the war of ʿAbs and Dhubyān", "Nehîk — ابْنُ نَهِيكٍ adında; Abs–Zübyân savaşında öldürülenlerden biri"),
 "muthallam": P("الْمُثَلَّم", "al-Muthallam — a place; قَتِيلُ الْمُثَلَّمِ is the man killed there", "Müsellem — bir yer; قَتِيلُ الْمُثَلَّمِ orada öldürülen kimse"),
 "sharaka": VB("شَارَكَ", "ش ر ك", "to share with, to take part in (Form III; with فِي)", "ortak olmak, katılmak (müfâale; فِي ile)", "III"),
 "nawfal": P("نَوْفَل", "Nawfal — one of those slain in the war", "Nevfel — savaşta öldürülenlerden biri"),
 "wahab-name": P("وَهَب", "Wahab — one of those slain in the war", "Vehb — savaşta öldürülenlerden biri"),
 "mukhazzam": P("الْمُخَزَّم", "al-Mukhazzam — in ابْنُ الْمُخَزَّمِ, one of those slain in the war", "Muhazzem — ابْنُ الْمُخَزَّمِ adında; savaşta öldürülenlerden biri"),
 "aqala-diya": VB("عَقَلَ", "ع ق ل", "to pay the blood-price for (a slain man) — عَقَلَ الْقَتِيلَ: وَدَاهُ (عَقَلَ يَعْقِلُ)", "(maktulün) diyetini ödemek — عَقَلَ الْقَتِيلَ: وَدَاهُ (عَقَلَ يَعْقِلُ)"),
 "makhrim": N("مَخْرِم", "خ ر م", "the break in a mountain's spur and the road through it; a pass (pl. مَخَارِم)", "dağ burnunun kesildiği yer ve oradaki yol; geçit (ç. مَخَارِم)", plural="مَخَارِم"),
 "hall-dwelling": N("حَالّ", "ح ل ل", "one who alights and camps (ism fa'il of حَلَّ; pl. حِلَال)", "bir yere konan, konaklayan (حَلَّ'den ism-i fâil; ç. حِلَال)", plural="حِلَال"),
 "muzam": N("مُعْظَم", "ع ظ م", "a grave thing, a great trouble", "büyük iş, ağır belâ"),
 "la-hijaziyya": {"lemma": "لَا (الْحِجَازِيَّة)", "pos": "part", "gloss": {"en": "«la» that governs like laysa", "tr": "«leyse» gibi amel eden «lâ»"}, "level": 6},
 "tabl": N("تَبْل", "ت ب ل", "a grudge, a blood-debt to be avenged (pl. تُبُول)", "kin, alınacak öç (ç. تُبُول)", plural="تُبُول"),
 "jarim": N("جَارِم", "ج ر م", "one who has done a crime, «he of the crime» (ism fa'il of جَرَمَ)", "suç işleyen, «suç sahibi» (جَرَمَ'den ism-i fâil)"),
 "jani": N("جَانٍ", "ج ن ي", "one who commits an offence, who brings harm on (a manqūṣ: جَانٍ، الْجَانِي)", "cinayet işleyen, zarar getiren (mankûs: جَانٍ، الْجَانِي)"),
 "muslam-forsaken": N("مُسْلَم", "س ل م", "given up, forsaken, handed over to his foe (ism maf'ul of أَسْلَمَ)", "terk edilmiş, düşmanına teslim edilmiş (أَسْلَمَ'den ism-i mef'ûl)"),
})
NEW_VERBS.update({
 "sharaka": _sg.derived(_sg.B3, _sg.W3, "ُ", "شَارَك", "شَارِك", "شَارِك", "مُشَارَكَة", "مُشَارِك", "مُشَارَك", "شُورِكَ", "يُشَارَكُ"),
 "aqala-diya": _sg1("daraba", "عَقَل", "عْقِل", "اِعْقِل", "عَقْل", "عَاقِل", "مَعْقُول", "عُقِلَ", "يُعْقَلُ", note="عَقَلْتُ الْقَتِيلَ: وَدَيْتُهُ، وَعَقَلْتُ عَنْهُ: أَدَّيْتُ عَنْهُ الدِّيَةَ الَّتِي لَزِمَتْهُ (الزَّوْزَنِيُّ)."),
})
TAILOR.update({
 "rumh": ("a spear, a lance (pl. رِمَاح)", "mızrak (ç. رِمَاح)"),
 "tali": ("climbing, going up; rising (ism fāʿil of طَلَعَ)", "tırmanan, yukarı çıkan; doğan (طَلَعَ'den ism-i fâil)"),
 "asama": ("to defend, to shield (from) (عَصَمَ يَعْصِمُ)", "korumak, savunmak (عَصَمَ يَعْصِمُ)"),
 "taraqa": ("to come by night, to come upon unlooked-for; to knock", "geceleyin gelmek, ansızın çıkagelmek; kapı çalmak"),
 "sahih": ("sound, whole, without defect; correct", "sağlam, kusursuz; sahîh"),
 "mal": ("wealth, property — among the desert Arabs, above all camels (pl. أَمْوَال)", "mal, servet — bâdiye Araplarında özellikle develer (ç. أَمْوَال)"),
 "karim": ("noble, generous (pl. كِرَام)", "soylu, cömert (ç. كِرَام)"),
 "adraka": ("to reach, to catch up with, to attain; to grasp", "ulaşmak, yetişmek, elde etmek; kavramak"),
 "amr": ("an affair, a matter; a command (pl. أُمُور، أَوَامِر)", "iş, mesele; emir (ç. أُمُور، أَوَامِر)"),
})
# ---- vv. 59–62 ----
NEW_GLOSS.update({
 "samit": N("صَامِت", "ص م ت", "silent, one who holds his tongue (ism fa'il of صَمَتَ)", "susan, sükût eden (صَمَتَ'den ism-i fâil)"),
 "mujib-pleasing": N("مُعْجِب", "ع ج ب", "pleasing, admirable (ism fa'il of أَعْجَبَ)", "hoşa giden, beğenilen (أَعْجَبَ'den ism-i fâil)"),
 "takallum": N("تَكَلُّم", "ك ل م", "speaking (masdar of تَكَلَّمَ)", "konuşma (تَكَلَّمَ'nin masdarı)"),
 "haluma": VB("حَلُمَ", "ح ل م", "to be forbearing and of sound mind, to grow wise (حَلُمَ يَحْلُمُ)", "halîm ve akl-ı selîm sahibi olmak (حَلُمَ يَحْلُمُ)"),
 "tasal": N("تَسْآل", "س أ ل", "asking, much asking (a masdar of سَأَلَ on تَفْعَال)", "isteme, çok isteme (سَأَلَ'den تَفْعَال vezninde masdar)"),
})
NEW_VERBS.update({
 "haluma": _sg1("karuma", "حَلُم", "حْلُم", "اُحْلُم", "حِلْم", "حَلِيم", note="لَازِمٌ، وَالْوَصْفُ مِنْهُ حَلِيمٌ عَلَى فَعِيلٍ."),
})
TAILOR.update({
 "kaayyin": ("how many a … — a noun standing for a large number, like the stating كَمْ; said كَأَيِّنْ and كَائِنْ", "nice … — çok sayıdan kinâye isim; haberî كَمْ gibi; كَأَيِّنْ ve كَائِنْ denir"),
 "naqs": ("falling short, deficiency (masdar of نَقَصَ)", "eksiklik, noksanlık (نَقَصَ'nin masdarı)"),
 "fata-youth": ("a young man; a man (a maqṣūr noun; pl. فِتْيَان)", "genç, yiğit; kişi (maksûr; ç. فِتْيَان)"),
 "hilm": ("forbearance, good sense, a settled mind (pl. أَحْلَام)", "hilim, akl-ı selîm, ağırbaşlılık (ç. أَحْلَام)"),
 "shaykh": ("an old man; an elder, a shaykh (pl. شُيُوخ)", "ihtiyar; yaşlı, şeyh (ç. شُيُوخ)"),
 "sura": ("form, shape, outward look (pl. صُوَر)", "suret, şekil, dış görünüş (ç. صُوَر)"),
 "ada-return": ("to return, to come back; to do again", "dönmek, geri gelmek; yeniden yapmak"),
 "harama-deprive": ("to deprive, to refuse (someone a thing) (حَرَمَ يَحْرِمُ)", "mahrum etmek, vermemek (حَرَمَ يَحْرِمُ)"),
 "akthara": ("to do much of, to do often (Form IV)", "çok yapmak, sık yapmak (if'âl)"),
})
# >>> NEW GLOSS ABOVE THIS LINE <<<
# a key is a global claim: a NEW key must not name anything else on the shelf, nor in a sibling's staged package
_STAGED = {}
for d in OUT_ROOT.iterdir() if OUT_ROOT.exists() else []:
    if d.name != SLUG and (d / "glossary.json").exists():
        try: _STAGED[d.name] = json.loads((d / "glossary.json").read_text(encoding="utf-8"))["entries"]
        except Exception: pass
for k, e in NEW_GLOSS.items():
    hit = [p for p in PREF if k in _G[p]]
    assert not hit, (k, hit)
    for p, g in _STAGED.items():
        if k in g: assert g[k].get("lemma") == e["lemma"], ("staged clash", k, p, g[k].get("lemma"))
assert set(NEW_VERBS) == {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}, set(NEW_VERBS) ^ {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}

def _keys(chs):
    out = set()
    for S in chs:
        for s in S:
            for t in s["tokens"]:
                out.add(t["lex"])
                for sg2 in t.get("segments", []): out.add(sg2["lex"])
                if t.get("phrase"): out.add(t["phrase"]["lex"])
    return out
used_all, used = _keys(ALL_AUTHORED), _keys(CHAPS)
missing = sorted(k for k in used_all if not (NEW_GLOSS.get(k) or find_gloss(k)))
assert not missing, missing
unused_new = sorted(set(NEW_GLOSS) - used_all)
assert not unused_new, unused_new
GLOSS = {}
for k in sorted(used):
    e = json.loads(json.dumps(NEW_GLOSS.get(k) or find_gloss(k)))
    if k in TAILOR: e["gloss"] = {"en": TAILOR[k][0], "tr": TAILOR[k][1]}
    GLOSS[k] = e
MORPH = {"verbs": {}}
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = NEW_VERBS.get(k) or find_verb(k, e["lemma"])
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par

_AD = lambda n: str(n).translate(str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩"))
TITLES_ALL = [
 {"ar": "خَبَرُ زُهَيْرٍ", "en": "Zuhayr's Story", "tr": "Züheyr'in Haberi"},
 {"ar": "أَطْلَالُ أُمِّ أَوْفَى", "en": "The Ruins of Umm Awfā", "tr": "Ümmü Evfâ'nın Yurt İzleri"},
 {"ar": "الظَّعَائِنُ", "en": "The Women Departing in Their Litters", "tr": "Hevdeçlerde Göç Eden Kadınlar"},
 {"ar": "السَّيِّدَانِ", "en": "The Two Peacemakers", "tr": "İki Efendi: Barışı Kuranlar"},
 {"ar": "الدِّيَاتُ، وَرِسَالَةٌ إِلَى الْأَحْلَافِ", "en": "The Blood-Money, and a Message to the Allies", "tr": "Diyetler ve Müttefiklere Mesaj"},
 {"ar": "الْحَرْبُ، وَضِغْنُ حُصَيْنٍ", "en": "War, and Ḥuṣayn's Hidden Grudge", "tr": "Savaş ve Husayn'ın Gizli Kini"},
 {"ar": "وَثْبَةُ حُصَيْنٍ، وَمَوْرِدُ الْمَنَايَا", "en": "Ḥuṣayn's Blow, and the Watering-Place of Death", "tr": "Husayn'ın Hamlesi ve Ölümlerin Suvadı"},
 {"ar": "عَاقِلُو الْقَتْلَى، وَسَآمَةُ الثَّمَانِينَ", "en": "Those Who Paid for the Slain, and the Weariness of Eighty Years", "tr": "Diyetleri Ödeyenler ve Seksen Yılın Usancı"},
 {"ar": "الْحِكَمُ (١): وَمَنْ … وَمَنْ …", "en": "The Wisdom Verses, Part One: «And Whoever …»", "tr": "Hikmet Beyitleri (1): «Ve Kim …»"},
 {"ar": "الْحِكَمُ (٢)، وَخَاتِمَةُ الْقَصِيدَةِ", "en": "The Wisdom Verses, Part Two, and the Close of the Ode", "tr": "Hikmet Beyitleri (2) ve Kasidenin Sonu"},
]
TITLES = TITLES_ALL[:len(CHAPS)]
WHOLE = DONE_TO == POEM_END
# where the edition's own print is departed from — (verse, ar, en, tr); every one against a witness
DIV = [
 (3, "الْبَيْتُ ٣ «مِجْثَمِ» ← «مَجْثَمِ»، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ (الْمَفْعَلُ مِنْ جَثَمَ) وَشَرْحُ الدُّرَّةِ", "v. 3 «مِجْثَمِ» → «مَجْثَمِ» — witness: al-Zawzanī's own commentary on the verse (the مَفْعَل of جَثَمَ) and al-Durra's", "3. beyit «مِجْثَمِ» → «مَجْثَمِ» — şâhit: Zevzenî'nin bu beyte kendi şerhi (جَثَمَ'den mef'al) ve Dürre'nin şerhi"),
 (29, "الْبَيْتُ ٢٩ «ذَمِيمَةٌ» ← «ذَمِيمَةً» عَلَى الْحَالِ، وَالشَّاهِدُ نَصُّ الدُّرَّةِ وَإِعْرَابُهُ", "v. 29 «ذَمِيمَةٌ» → «ذَمِيمَةً», a hal — witness: al-Durra's text and iʿrāb", "29. beyit «ذَمِيمَةٌ» → «ذَمِيمَةً», hâl olarak — şâhit: Dürre'nin metni ve i'râbı"),
 (52, "الْبَيْتُ ٥٢ «يُذَمَم» ← «يُذْمَمْ»، وَالشَّاهِدُ الْوَزْنُ وَإِعْرَابُ الدُّرَّةِ", "v. 52 «يُذَمَم» → «يُذْمَمْ» — witness: the metre, and al-Durra's iʿrāb", "52. beyit «يُذَمَم» → «يُذْمَمْ» — şâhit: vezin ve Dürre'nin i'râbı"),
]
# editorial vowels that neither metre nor commentary settles — left for the scholar
FLAGS = [
 (0, "«كُبَرَ قَصَائِدِهِ» فِي الْخَبَرِ", "«كُبَرَ قَصَائِدِهِ» in the khabar", "haberdeki «كُبَرَ قَصَائِدِهِ»"),
 (1, "دَالُ «الدَّرَّاجِ» (ب ١)", "the dāl of «الدَّرَّاجِ» (v. 1)", "«الدَّرَّاجِ»in dâl'ı (b. 1)"),
 (18, "شِينُ «مَنْشِمِ» (ب ١٨)", "the shīn of «مَنْشِمِ» (v. 18)", "«مَنْشِمِ»in şîn'i (b. 18)"),
 (19, "سِينُ «السِّلْمَ» (ب ١٩)", "the sīn of «السِّلْمَ» (v. 19)", "«السِّلْمَ»in sîn'i (b. 19)"),
]
# keep the registers in one place: later sections may add to DIV / FLAGS before the manifest is built
DIV += [
 (9, "الْبَيْتُ ٩ «بِأَنْمَاطِ» ← «بِأَنْمَاطٍ» بِالتَّنْوِينِ، وَالشَّاهِدُ الْوَزْنُ وَشَرْحُ الزَّوْزَنِيِّ (أَنْمَاطًا كِرَامًا) وَنَصُّ الدُّرَّةِ", "v. 9 «بِأَنْمَاطِ» → «بِأَنْمَاطٍ», with tanwin — witness: the metre, al-Zawzanī's gloss («fine cloths») and al-Durra's text", "9. beyit «بِأَنْمَاطِ» → «بِأَنْمَاطٍ», tenvinle — şâhit: vezin, Zevzenî'nin şerhi («değerli örtüler») ve Dürre'nin metni"),
 (12, "الْبَيْتُ ١٢ «للطّيفِ» ← «لِلَّطِيفِ» (الشَّدَّةُ عَلَى اللَّامِ)، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ: «اللَّطِيفُ: الْمُتَأَنِّقُ»", "v. 12 «للطّيفِ» → «لِلَّطِيفِ» (the shadda belongs on the lam) — witness: al-Zawzanī's gloss «اللَّطِيف: the man of nice taste»", "12. beyit «للطّيفِ» → «لِلَّطِيفِ» (şedde lâm üzerindedir) — şâhit: Zevzenî'nin şerhi: «اللَّطِيف: ince zevkli kimse»"),
 (14, "الْبَيْتُ ١٤ «جِمَامَهُ» ← «جِمَامُهُ» بِالرَّفْعِ فَاعِلًا لِـ«زُرْقًا»، وَالشَّاهِدُ نَصُّ الدُّرَّةِ وَإِعْرَابُهُ", "v. 14 «جِمَامَهُ» → «جِمَامُهُ», in rafʿ as the doer of «blue» — witness: al-Durra's text and iʿrāb", "14. beyit «جِمَامَهُ» → «جِمَامُهُ», «zurkan»ın fâili olarak merfû — şâhit: Dürre'nin metni ve i'râbı"),
 (15, "الْبَيْتُ ١٥ «قَيْنِيِّ» ← «قَيْنِيٍّ» بِالتَّنْوِينِ، وَالشَّاهِدُ الْوَزْنُ وَنَصُّ الدُّرَّةِ وَإِعْرَابُهُ", "v. 15 «قَيْنِيِّ» → «قَيْنِيٍّ», with tanwin — witness: the metre, and al-Durra's text and iʿrāb", "15. beyit «قَيْنِيِّ» → «قَيْنِيٍّ», tenvinle — şâhit: vezin, Dürre'nin metni ve i'râbı"),
]
FLAGS += [
 (9, "آخِرُ «مُشَاكِهَةِ» (ب ٩: الْجَرُّ نَعْتًا أَوِ الرَّفْعُ خَبَرًا)", "the ending of «مُشَاكِهَةِ» (v. 9: jarr as a na't, or rafʿ as a khabar)", "«مُشَاكِهَةِ»in sonu (b. 9: na't olarak cer yahut haber olarak ref)"),
 (14, "عَيْنُ «عِصِيَّ» وَمِيمُ «جِمَامُهُ» (ب ١٤)", "the ʿayn of «عِصِيَّ» and the mīm of «جِمَامُهُ» (v. 14)", "«عِصِيَّ»nin aynı ve «جِمَامُهُ»nun mîmi (b. 14)"),
]
DIV += [
 (35, "الْبَيْتُ ٣٥ «مِنَ وَرَائِيَ» ← «مِنْ وَرَائِيَ» بِسُكُونِ النُّونِ، وَالشَّاهِدُ الْوَزْنُ وَنَصُّ الدُّرَّةِ", "v. 35 «مِنَ وَرَائِيَ» → «مِنْ وَرَائِيَ», with sukun on the nun — witness: the metre, and al-Durra's text", "35. beyit «مِنَ وَرَائِيَ» → «مِنْ وَرَائِيَ», nûn'un sükûnuyla — şâhit: vezin ve Dürre'nin metni"),
 (37, "الْبَيْتُ ٣٧ «مُقَذَّفِ» ← «مُقَذَّفٍ» بِالتَّنْوِينِ، وَالشَّاهِدُ الْوَزْنُ وَنَصُّ الدُّرَّةِ وَ«التَّلْخِيصِ»", "v. 37 «مُقَذَّفِ» → «مُقَذَّفٍ», with tanwin — witness: the metre, al-Durra's text and the Talkhīṣ", "37. beyit «مُقَذَّفِ» → «مُقَذَّفٍ», tenvinle — şâhit: vezin, Dürre'nin metni ve Telhîs"),
 (40, "الْبَيْتُ ٤٠ «مُسْتَوْبِلٍ مُتَوَخِّمِ» ← «مُسْتَوْبَلٍ مُتَوَخَّمِ» اسْمَيْ مَفْعُولٍ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ: «اسْتَوْبَلْتُ الشَّيْءَ: وَجَدْتُهُ وَبِيلًا»", "v. 40 «مُسْتَوْبِلٍ مُتَوَخِّمِ» → «مُسْتَوْبَلٍ مُتَوَخَّمِ», passive participles — witness: al-Zawzanī's own gloss, «I found the thing وَبِيل»", "40. beyit «مُسْتَوْبِلٍ مُتَوَخِّمِ» → «مُسْتَوْبَلٍ مُتَوَخَّمِ», ism-i mef'ûl olarak — şâhit: Zevzenî'nin kendi şerhi: «bir şeyi vebîl buldum»"),
]
FLAGS += [
 (40, "بَاءُ «مُسْتَوْبَلٍ» وَخَاءُ «مُتَوَخَّمِ» (ب ٤٠: الْفَتْحُ اسْمَ مَفْعُولٍ، وَفِي الْمَطْبُوعِ الْكَسْرُ)", "the bāʾ of «مُسْتَوْبَلٍ» and the khāʾ of «مُتَوَخَّمِ» (v. 40: fatha, as passive participles; the edition prints kasra)", "«مُسْتَوْبَلٍ»in bâ'sı ve «مُتَوَخَّمِ»in hâ'sı (b. 40: ism-i mef'ûl olarak fetha; baskıda kesre)"),
]
DIV += [
 (41, "الْبَيْتُ ٤١ «أَوْ قَتْلِ الْمُثَلَّمِ» ← «أَوْ قَتِيلِ الْمُثَلَّمِ» (سَقَطَتِ الْيَاءُ فِي الْمَطْبُوعِ)، وَ«نَهِيكِ» ← «نَهِيكٍ» بِالتَّنْوِينِ، وَالشَّاهِدُ الْوَزْنُ وَنَصُّ الدُّرَّةِ وَإِعْرَابُهُ", "v. 41 «أَوْ قَتْلِ الْمُثَلَّمِ» → «أَوْ قَتِيلِ الْمُثَلَّمِ» (the edition has dropped the yāʾ), and «نَهِيكِ» → «نَهِيكٍ», with tanwin — witness: the metre, and al-Durra's text and iʿrāb", "41. beyit «أَوْ قَتْلِ الْمُثَلَّمِ» → «أَوْ قَتِيلِ الْمُثَلَّمِ» (baskıda yâ düşmüştür) ve «نَهِيكِ» → «نَهِيكٍ», tenvinle — şâhit: vezin, Dürre'nin metni ve i'râbı"),
 (42, "الْبَيْتُ ٤٢ «نَوْفَلِ» ← «نَوْفَلٍ» بِالتَّنْوِينِ، وَالشَّاهِدُ الْوَزْنُ وَنَصُّ الدُّرَّةِ", "v. 42 «نَوْفَلِ» → «نَوْفَلٍ», with tanwin — witness: the metre, and al-Durra's text", "42. beyit «نَوْفَلِ» → «نَوْفَلٍ», tenvinle — şâhit: vezin ve Dürre'nin metni"),
 (44, "الْبَيْتُ ٤٤ «لَحَيٍّ» ← «لِحَيٍّ» بِكَسْرِ اللَّامِ الْجَارَّةِ، وَالشَّاهِدُ شَرْحُ الزَّوْزَنِيِّ (لِأَجْلِ حَيٍّ) وَإِعْرَابُ الدُّرَّةِ", "v. 44 «لَحَيٍّ» → «لِحَيٍّ», with kasra on the lam of jarr — witness: al-Zawzanī's gloss («for the sake of a tribe») and al-Durra's iʿrāb", "44. beyit «لَحَيٍّ» → «لِحَيٍّ», cer lâmının kesresiyle — şâhit: Zevzenî'nin şerhi («bir kabile uğruna») ve Dürre'nin i'râbı"),
]
FLAGS += [
 (44, "ظَاءُ «بِمُعْظَمِ» (ب ٤٤: مَفْتُوحَةٌ فِي الْمَطْبُوعِ)", "the ẓāʾ of «بِمُعْظَمِ» (v. 44: fatha in the edition)", "«بِمُعْظَمِ»in zâ'sı (b. 44: baskıda fethalı)"),
]
# >>> NEW DIVERGENCES ABOVE THIS LINE <<<
_div = sorted(d for d in DIV if d[0] <= DONE_TO)
_flg = sorted(f for f in FLAGS if f[0] <= DONE_TO)
_ch_ar = "؛ ".join("الْفَصْلُ %s: %s–%s" % (_AD(i + 2), _AD(a), _AD(b)) for i, (a, b) in enumerate(VNUMS))
_ch_en = "; ".join("chapter %d: vv. %d–%d" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_ch_tr = "; ".join("%d. bölüm: %d–%d. beyitler" % (i + 2, a, b) for i, (a, b) in enumerate(VNUMS))
_ord = lambda k: "(%s) " % _AD(k)
if WHOLE:
    _scope = ("وَالْفُصُولُ بَعْدَهُ مُعَلَّقَتُهُ كَامِلَةً — اثْنَانِ وَسِتُّونَ بَيْتًا لَمْ يُتْرَكْ مِنْهَا بَيْتٌ وَلَمْ يُقَدَّمْ وَلَمْ يُؤَخَّرْ",
              "The chapters after it are his Muʿallaqa WHOLE — sixty-two verses, none left out and none moved",
              "Sonraki bölümler onun muallakasının TAMAMIDIR — altmış iki beyit; hiçbiri atlanmamış, hiçbirinin yeri değiştirilmemiştir")
    _rest = ("", "", "")
else:
    _scope = ("وَالْفُصُولُ بَعْدَهُ الْأَبْيَاتُ %s–%s مِنْ مُعَلَّقَتِهِ مُتَتَالِيَةً لَمْ يُتْرَكْ مِنْ بَيْنِهَا بَيْتٌ" % (_AD(1), _AD(DONE_TO)),
              "The chapters after it are vv. 1–%d of his Muʿallaqa, consecutive, with no verse dropped from among them" % DONE_TO,
              "Sonraki bölümler onun muallakasının 1–%d. beyitleridir; ardışıktır, aralarından beyit atlanmamıştır" % DONE_TO)
    _rest = (" وَالْقَصِيدَةُ فِي رِوَايَتِهِ اثْنَانِ وَسِتُّونَ بَيْتًا، وَبَقِيَّتُهَا (%s–%s) تُلْحَقُ عَلَى هٰذَا النَّسَقِ." % (_AD(DONE_TO + 1), _AD(62)),
             " In his recension the ode has sixty-two verses; the rest (vv. %d–62) is to follow in the same manner." % (DONE_TO + 1),
             " Onun rivayetinde kaside altmış iki beyittir; kalanı (%d–62. beyitler) aynı usulle eklenecektir." % (DONE_TO + 1))
_div_ar = "؛ ".join(_ord(i + 1) + d[1] for i, d in enumerate(_div))
_div_en = "; ".join("(%d) " % (i + 1) + d[2] for i, d in enumerate(_div))
_div_tr = "; ".join("(%d) " % (i + 1) + d[3] for i, d in enumerate(_div))
ATTR_AR = ("نَصٌّ مَنْقُولٌ بِلَفْظِهِ. الْفَصْلُ الْأَوَّلُ خَبَرُ زُهَيْرِ بْنِ أَبِي سُلْمَى مِنْ «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةِ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ كَمَا فِي الْمَكْتَبَةِ الشَّامِلَةِ (الْكِتَابُ ٢٣٧٨٥)، ج ١ ص ١٤٤، الْفِقْرَتَانِ ٢١٢ وَ٢١٣: قِطْعَةٌ مُتَّصِلَةٌ وَاحِدَةٌ لَمْ يُحْذَفْ مِنْ وَسَطِهَا شَيْءٌ، وَتُرِكَتْ أَرْقَامُ الْفِقَرِ وَحَوَاشِي الْمُحَقِّقِ. "
    + _scope[0] + " — وَهِيَ مِنَ الْبَحْرِ الطَّوِيلِ، وَرَوِيُّهَا مِيمٌ مَكْسُورَةٌ وَقَافِيَتُهَا مُطْلَقَةٌ — بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) وَتَرْتِيبِهِ وَعَدِّهِ فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةِ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م (الْكِتَابُ ١١٢٥٣)، ص ١٣٣–١٥٢. " + _ch_ar + ". وَالْبَيْتُ جُمْلَةٌ وَاحِدَةٌ، وَعَلَامَةُ «•» آخِرُ صَدْرِهِ." + _rest[0] + " "
    "الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ عَلَى حَالِهِ بِإِمْلَاءِ هٰذَا الرَّفِّ، وَمَا تَرَكَتْهُ عَارِيًا — وَهُوَ حَرَكَاتُ خَبَرِ ابْنِ قُتَيْبَةَ كُلُّهَا سِوَى الشَّدَّاتِ، وَكَثِيرٌ مِنْ حُرُوفِ الْأَبْيَاتِ — ضَبَطَهُ الْمُحَرِّرُ بِمَا يُوجِبُهُ الْوَزْنُ وَالشَّرْحُ. وَخُولِفَ الْمَطْبُوعُ فِي هٰذِهِ الْمَوَاضِعِ، وَكُلُّهَا سَهْوُ طِبَاعَةٍ يَشْهَدُ عَلَيْهِ شَاهِدٌ: " + _div_ar + ". وَفِي الْبَيْتِ ٣٠ أُبْقِيَ «فَتَعْرُكُكُمْ» بِالرَّفْعِ كَمَا فِي الْمَطْبُوعِ، وَالرِّوَايَةُ الْأُخْرَى بِالْجَزْمِ. وَمِمَّا ضَبَطَهُ الْمُحَرِّرُ وَلَمْ يَقْطَعْ بِهِ وَزْنٌ وَلَا شَرْحٌ: " + "، وَ".join(f[1] for f in _flg) + ". "
    "إِعْرَابُ كُلِّ كَلِمَةٍ بِعِبَارَةِ هٰذَا الرَّفِّ، وَقَدْ رُوجِعَ عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ: إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهَ الدُّرَّة (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م؛ الْكِتَابُ ١٥١٠١٧، ج ٢) — وَهُوَ يَرْوِي الْقَصِيدَةَ بِتَرْتِيبٍ وَعَدٍّ آخَرَ وَيَزِيدُ أَبْيَاتًا لَيْسَتْ عِنْدَ الزَّوْزَنِيِّ — وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ، وَلَمْ يُذْكَرْ مِنْهَا إِلَّا مَا يَشْهَدُ لَهُ شَرْحُ الزَّوْزَنِيِّ أَوْ شَرْحُ الدُّرَّةِ أَوِ التَّلْخِيصُ نَفْسُهُ. وَالتَّرْجَمَةُ مَعْنَى الْبَيْتِ عَلَى شَرْحِ الزَّوْزَنِيِّ، لَا شِعْرٌ. وَتَقْسِيمُ الْفُصُولِ وَعَنَاوِينُهَا وَعَلَامَاتُ التَّرْقِيمِ مِنَ الْمُحَرِّرِ، وَالنَّصُّ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.")
ATTR_EN = ("The RECEIVED text, word for word. Chapter 1 is the khabar of Zuhayr ibn Abī Sulmā from Ibn Qutayba (d. 276 AH), al-Shiʿr wa-l-shuʿarāʾ, in the edition al-Maktaba al-Shāmila names «Dār al-Ḥadīth, Cairo, 1423 AH» (book 23785), vol. 1 p. 144, §§ 212–213: one contiguous span with nothing cut from inside it; only the paragraph numbers and the editor's footnote marks are left out. "
    + _scope[1] + " — in the metre al-ṭawīl, rhyming on a mīm with kasra, the rhyme unbound — in the recension, order and verse-count of al-Zawzanī (d. 486 AH), Sharḥ al-Muʿallaqāt al-sabʿ, the edition Shamela names «Dār Iḥyāʾ al-Turāth al-ʿArabī, 1423 AH / 2002 CE» (book 11253), pp. 133–152: " + _ch_en + ". Each verse is one sentence, and «•» marks the end of its first hemistich." + _rest[1] + " "
    "The vowelling has two layers. What the edition vowels is kept, in this shelf's spelling; what it leaves bare — every short vowel of Ibn Qutayba's khabar (the edition prints only its shaddas) and many letters of the verses — is supplied editorially, as the metre and the commentary require. The edition's print is departed from in these places, each a slip of the press with a witness against it: " + _div_en + ". In v. 30 the edition's «فَتَعْرُكُكُمْ», in rafʿ, is kept; the other reading is in jazm. Editorial vowels that neither metre nor commentary settles: " + ", ".join(f[2] for f in _flg) + ". "
    "Every token's iʿrāb is written in this shelf's own wording and was checked against Muḥammad ʿAlī Ṭāhā al-Durra, Fatḥ al-Kabīr al-Mutaʿāl: Iʿrāb al-Muʿallaqāt al-ʿashr al-ṭiwāl (Maktabat al-Sawādī, Jeddah, 2nd ed., 1409 AH / 1989 CE; book 151017, vol. 2), who gives the ode in another order and count and has verses al-Zawzanī does not; where he offers two readings the first is given and the second mentioned. The figures of balāgha are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ, and only where al-Zawzanī's commentary, al-Durra's, or the Talkhīṣ itself supports them. The translations give each verse's plain meaning after al-Zawzanī; they are not verse. The division into chapters, their titles and the punctuation are editorial. Pending scholarly review.")
ATTR_TR = ("Metin LAFZIYLA aktarılmıştır. 1. bölüm, Züheyr b. Ebî Sülmâ'nın haberidir: İbn Kuteybe (ö. 276 h.), eş-Şi'r ve'ş-şuarâ, el-Mektebetü'ş-Şâmile'nin «Dâru'l-Hadîs, Kahire, 1423 h.» diye andığı baskı (kitap 23785), c. 1 s. 144, §§ 212–213: içinden hiçbir şey çıkarılmamış tek ve kesintisiz bir parça; yalnızca paragraf numaraları ve muhakkikin dipnot işaretleri alınmamıştır. "
    + _scope[2] + " — kaside tavîl bahrindendir, revîsi kesreli mîm, kâfiyesi mutlaktır — Zevzenî'nin (ö. 486 h.) Şerhu'l-Muallakâti's-seb'indeki rivayeti, sırası ve beyit sayımıyla; Şâmile'nin «Dâru İhyâi't-Türâsi'l-Arabî, 1423 h. / 2002 m.» diye andığı baskı (kitap 11253), s. 133–152: " + _ch_tr + ". Her beyit tek cümledir; «•» ilk mısraın sonunu gösterir." + _rest[2] + " "
    "Harekeleme iki katmandır: baskının harekelediği yerler bu rafın imlâsıyla korunmuş; harekesiz bıraktığı yerler — İbn Kuteybe haberinin bütün kısa harekeleri (baskı yalnızca şeddeleri basar) ve beyitlerdeki pek çok harf — vezin ve şerhin gerektirdiği şekilde editörce harekelenmiştir. Baskıdan şu yerlerde ayrılınmıştır; hepsi, aleyhine şâhit bulunan dizgi sehvidir: " + _div_tr + ". 30. beyitte baskıdaki merfû «فَتَعْرُكُكُمْ» korunmuştur; öbür rivayet cezimlidir. Vezin ve şerhin kesinleştirmediği editoryal harekeler: " + ", ".join(f[3] for f in _flg) + ". "
    "Her kelimenin i'râbı bu rafın kendi ifadesiyle yazılmış ve Muhammed Ali Tâhâ ed-Dürre'nin Fethu'l-Kebîri'l-Müteâl: İ'râbü'l-Muallakâti'l-aşri't-tıvâl'i (Mektebetü's-Sevâdî, Cidde, 2. baskı, 1409 h. / 1989 m.; kitap 151017, c. 2) ile karşılaştırılmıştır; o, kasideyi başka bir sıra ve sayımla rivayet eder ve Zevzenî'de bulunmayan beyitler ekler; iki vecih verdiği yerde birincisi esas alınmış, ikincisi belirtilmiştir. Belâgat nükteleri Kazvînî'nin Telhîsu'l-Miftâh'ındaki bâblara göre adlandırılmış ve yalnızca Zevzenî'nin şerhinin, Dürre'nin şerhinin yahut bizzat Telhîs'in desteklediği yerlerde zikredilmiştir. Çeviriler beytin Zevzenî'ye göre düz mânâsını verir; şiir değildir. Bölümlere ayırma, bölüm başlıkları ve noktalama editoryaldir. Metin ilmî incelemeyi beklemektedir.")
MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ زُهَيْرِ بْنِ أَبِي سُلْمَى", "en": "The Muʿallaqa of Zuhayr ibn Abī Sulmā", "tr": "Züheyr b. Ebî Sülmâ'nın Muallakası"},
 "subtitle": {"ar": ("الْمُعَلَّقَةُ كَامِلَةً" if WHOLE else "الْمُعَلَّقَةُ") + " بِرِوَايَةِ الزَّوْزَنِيِّ، مَعَ خَبَرِ الشَّاعِرِ عَنِ ابْنِ قُتَيْبَةَ — بَيْتًا بَيْتًا بِالْإِعْرَابِ وَالْبَلَاغَةِ",
              "en": ("The whole ode" if WHOLE else "The ode") + " in al-Zawzanī's recension, with the poet's story from Ibn Qutayba — verse by verse, with full iʿrāb and balāgha",
              "tr": "Zevzenî rivayetiyle muallaka" + ("nın tamamı" if WHOLE else "") + " ve İbn Kuteybe'den şairin haberi — beyit beyit, tam i'râb ve belâgatıyla"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "siblings": [],
 "attribution": {"ar": ATTR_AR, "en": ATTR_EN, "tr": ATTR_TR, "reviewStatus": "pending-scholarly-review"},
}
import shutil as _sh
if (PKG / "chapters").exists(): _sh.rmtree(PKG / "chapters")
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("chapters:", len(CHAPS), "verses in package: 1-%d" % DONE_TO, "| verses authored:", len(VERSES), "of", POEM_END, "| missing:", [n for n in range(1, POEM_END + 1) if n not in VERSES],
      "| sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
