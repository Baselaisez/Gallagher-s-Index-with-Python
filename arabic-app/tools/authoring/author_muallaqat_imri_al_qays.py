"""Author content/samples/muallaqat-imri-al-qays — «مُعَلَّقَةُ امْرِئِ الْقَيْسِ», a RECEIVED text at Level 6 (Master).

Chapter 1 is a contiguous, verbatim span of the poet's khabar from Ibn Qutayba, «الشعر والشعراء» (Shamela book 23785,
1/109: «فبلغه مقتل أبيه وهو بدمّون … حتّى يثأر بأبيه»). The other chapters give the Muʿallaqa WHOLE, in the text, the
order and the numbering of al-Zawzanī's «شرح المعلقات السبع» (Shamela book 11253; 81 verses): PLAN (below) cuts verses
1–81 into thirteen chapters of 6–8 verses, none left out and no run skipped. A verse is ONE sentence; the last word of its
first hemistich carries punctAfter "•". The metre is al-ṭawīl.

THE POEM IS AUTHORED IN STAGES. Each verse is filed by its number — V(None, n, en, tr, tokens) fills VERSE[n] — and the
writer at the foot publishes only the chapters whose verses are ALL authored, contiguously from verse 1; verses written
ahead of the poem's order wait in VERSE until the chapters before them are done (the run prints what is published and
what is waiting). The manifest attribution is BUILT from what is published, so it never claims more than the chapters
hold. To continue: write the next chapter's verses above the marker «# ==== INSERT … ABOVE ====» that covers their
numbers, add their new lexicon entries above «# ==== NEW GLOSS ENTRIES ABOVE ====» (REGLOSS, NEW_VERBS, CORR, SCHOLAR and
TALKHIS have markers too), run, validate.

The iʿrāb of every verse token was checked against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب المعلقات العشر
الطوال» (Shamela book 151017) and written in the shelf's own wording; where he gives two readings the first is given and
the second mentioned. The meanings, the glosses of the rare words and the figures are al-Zawzanī's. Source pages, verbatim:
research/sources/muallaqat-imri-al-qays-src.txt.

VOWELS. The edition's printed vowels are kept (normalised to the shelf's spelling); bare letters are supplied editorially.
The slips of the e-text that are corrected against a witness (al-Tibrīzī's «شرح القصائد العشر», Shamela book 37488; al-Durra;
the metre) are listed in CORR and printed in the manifest attribution. Written on the authoring kit (story_kit.py).
Regenerate with:  QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_muallaqat_imri_al_qays.py
"""
import json, os, pathlib, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "muallaqat-imri-al-qays"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import tok, seg      # the shared token builder (NFC-normalises every Arabic string)
import sarf_gen as _sg

N = lambda s: unicodedata.normalize("NFC", s)
def T(full, lex, pos, g, ar, en, tr, p=None, s=None):
    """one token: surface, key, part of speech, grammar anchors, the trilingual iʿrāb, the mark after it, the clitic chain"""
    return tok(full, lex, pos, g, ar, en, tr, punct=p, segments=[seg(*x) for x in s] if s else None)

# the clitics, as (form, key, pos)
WA, FA = ("وَ", "wa", "conj"), ("فَ", "fa", "conj")
BI, LI, KA = ("بِ", "bi", "prep"), ("لِ", "li", "prep"), ("كَ", "ka", "prep")
def P(form):
    return (form, {"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمْ": "pron-3mp", "كَ": "pron-2ms", "نِي": "pron-1s",
                   "ي": "pron-1s", "يَ": "pron-1s", "نَا": "pron-1p", "كِ": "pron-2fs", "هُمَا": "pron-3d", "هِمَا": "pron-3d",
                   "هُنَّ": "pron-3fp", "هِنَّ": "pron-3fp", "هِمْ": "pron-3mp"}[form], "pron")

# ---- wordings that recur ---------------------------------------------------------------------------------------------
HEMI = "•"
QAFIYA = ("، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ", "; its tanwin is dropped for the rhyme", "; tenvini kafiye için düşmüştür")
MI = ("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ", "The second term of the idafa, in jarr by the kasra", "Muzâfun ileyh, kesre ile mecrûr")
def HARF_JARR(full, lex, ar="", en="", tr="", p=None):
    return T(full, lex, "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ" + ar + ".", "A jarr letter" + en + ".", "Cer harfi" + tr + ".", p)

S1 = []                      # the khabar's sentences, in order
VERSE = {}                   # the Muʿallaqa: al-Zawzanī's verse number -> its sentence (ids are given when the chapters are cut)
S2 = S3 = S4 = S5 = None     # (the first draft kept four lists; a verse is now filed by its NUMBER, whatever list the call names)
def V(chap, n, en, tr, tokens):
    if n == 0: chap.append({"id": "s%d" % (len(chap) + 1), "translation": {"en": en, "tr": tr}, "tokens": tokens})
    else:
        assert n not in VERSE, n
        VERSE[n] = {"translation": {"en": en, "tr": tr}, "tokens": tokens}

# =====================================================================================================================
# Chapter 1 — the khabar (Ibn Qutayba, al-Shiʿr wa-l-shuʿarāʾ 1/109), verbatim
# =====================================================================================================================
V(S1, 0, "Then the news of his father's killing reached him while he was at Dammūn, and he said:",
  "Sonra babasının öldürüldüğü haberi, o Demmûn'dayken kendisine ulaştı; bunun üzerine şöyle dedi:", [
 T("فَبَلَغَهُ", "balagha", "verb", ["atf-nasaq", "thulathi-mujarrad-babs", "maful-bihi"],
   "الْفَاءُ عَاطِفَةٌ عَلَى مَا قَبْلَهَا فِي كَلَامِ ابْنِ قُتَيْبَةَ، وَبَلَغَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالضَّمِيرُ لِامْرِئِ الْقَيْسِ.",
   "The fa conjoins to what comes before it in Ibn Qutayba's account; بَلَغَ is a past verb built on fatha, and the attached هُ is its direct object, placed before the doer, in the seat of nasb — the pronoun is Imruʾ al-Qays.",
   "Fâ, İbn Kuteybe'nin sözünde öncesine atfeder; بَلَغَ fetha üzere mebnî mâzî; bitişik «hû» zamiri öne geçmiş mef'ûlün bih, mahallen mansûb — zamir İmruülkays'a döner.", s=[FA, ("بَلَغَ", "balagha", "verb"), P("هُ")]),
 T("مَقْتَلُ", "maqtal", "noun", ["fail", "idafa-definiteness", "masdar"],
   "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — مَصْدَرٌ مِيمِيٌّ بِمَعْنَى الْقَتْلِ، وَالْمُرَادُ خَبَرُ مَقْتَلِهِ.",
   "The doer, in raf' by the damma, annexed — a masdar with mim, «the killing»; what reached him is the news of it.",
   "Fâil, damme ile merfû, muzâf — mîmli masdar, «öldürülme»; ulaşan, bunun haberidir."),
 T("أَبِيهِ", "ab", "noun", ["idafa-definiteness", "five-nouns"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَهُوَ مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ.",
   "The second term of the idafa, in jarr by the ya — one of the five nouns; it is annexed in turn, and the هِ is its second term — the masdar is annexed to its object.",
   "Muzâfun ileyh, esmâ-i hamseden olduğu için yâ ile mecrûr; kendisi de muzâf, «hî» muzâfun ileyh — masdarın mef'ûlüne izâfeti.", s=[("أَبِي", "ab", "noun"), P("هِ")]),
 T("وَهُوَ", "huwa", "pron", ["al-hal-jumla-wa-rabituha", "mubtada-khabar", "anwa-al-waw"],
   "الْوَاوُ وَاوُ الْحَالِ، وَهُوَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
   "The waw is the waw of the hal; هُوَ is a detached pronoun built on fatha, the mubtada, in the seat of raf'.",
   "Vâv hâliyedir; هُوَ fetha üzere mebnî munfasıl zamir, mübteda, mahallen merfû.", s=[WA, ("هُوَ", "huwa", "pron")]),
 T("بِدَمُّونَ", "dammun", "propn", ["huruf-jarr", "mamnu-min-sarf", "al-hal-jumla-wa-rabituha"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَدَمُّونَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ (عَلَمٌ عَلَى بُقْعَةٍ) — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَإِ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
   "The ba is a jarr letter meaning «in»; Dammūn is in jarr by the fatha in place of the kasra, a diptote (a proper name, read as feminine — the name of a place). The jarr phrase hangs on the omitted predicate of the mubtada, and the clause is a hal, in the seat of nasb.",
   "Bâ «-de» anlamında cer harfi; Demmûn, alemiyet ve te'nîs (bir yerin adı) sebebiyle gayr-i munsarif olduğundan kesre yerine fetha ile mecrûr. Câr-mecrûr mübtedanın mahzûf haberine müteallik; cümle hâl olarak mahallen mansûb.", "،", [BI, ("دَمُّونَ", "dammun", "propn")]),
 T("فَقَالَ", "qala", "verb", ["atf-nasaq", "hollow-verbs"],
   "الْفَاءُ عَاطِفَةٌ، وَقَالَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
   "The fa conjoins; قَالَ is a past verb built on fatha, its doer a hidden pronoun («he»).",
   "Fâ atıf; قَالَ fetha üzere mebnî mâzî, fâili gizli «hüve» zamiri.", ":", [FA, ("قَالَ", "qala", "verb")]),
])
SUKUN_Q = ("، وَسُكِّنَ آخِرُهُ لِلْوَقْفِ عَلَى الْقَافِيَةِ الْمُقَيَّدَةِ", "; its last letter is stilled for the pause on the fettered rhyme", "; son harfi, mukayyed kafiyede vakf için sâkin kılınmıştır")
V(S1, 0, "«The night has grown long upon us, Dammūn! Dammūn, we are a people of Yemen,",
  "«Gece üzerimize uzadıkça uzadı ey Demmûn! Ey Demmûn, biz Yemenli bir topluluğuz;", [
 T("تَطَاوَلَ", "tatawala", "verb", ["form-vi-verbs"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مِنَ التَّفَاعُلِ، أَيِ امْتَدَّ وَطَالَ.",
   "A past verb built on fatha — Form VI: it stretched on, grew long.",
   "Fetha üzere mebnî mâzî — tefâul bâbından: uzadıkça uzadı."),
 T("اللَّيْلُ", "layl", "noun", ["fail", "kinaya"],
   "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — وَفِي تَطَاوُلِ اللَّيْلِ كِنَايَةٌ عَنِ الْهَمِّ وَالسَّهَرِ، لِأَنَّ الْمَغْمُومَ يَسْتَطِيلُ لَيْلَهُ.",
   "The doer, in raf' by the damma — the night's growing long is a kinaya for care and sleeplessness: the grieved man finds his night long.",
   "Fâil, damme ile merfû — gecenin uzaması, keder ve uykusuzluktan kinâyedir; çünkü dertli kişi gecesini uzun bulur."),
 T("عَلَيْنَا", "ala", "prep", ["huruf-jarr"],
   "عَلَى حَرْفُ جَرٍّ، وَنَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَطَاوَلَ».",
   "عَلَى is a jarr letter and نَا an attached pronoun in the seat of jarr — the phrase hangs on «grew long».",
   "عَلَى cer harfi, نَا mahallen mecrûr bitişik zamir — câr-mecrûr «uzadı» fiiline müteallik.", s=[("عَلَيْ", "ala", "prep"), P("نَا")]),
 T("دَمُّونْ", "dammun", "propn", ["vocative-munada", "hadhf-wa-taqdir", "al-qafiya"],
   "مُنَادًى مُفْرَدٌ عَلَمٌ حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ (يَا دَمُّونُ)، مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ" + SUKUN_Q[0] + " — وَالْأَبْيَاتُ مِنْ مَشْطُورِ الرَّجَزِ.",
   "A vocative — a single proper name whose particle is dropped («O Dammūn»), built on damma in the seat of nasb" + SUKUN_Q[1] + " — the lines are rajaz, one hemistich to a line.",
   "Münâdâ — nidâ harfi hazfedilmiş müfred alem («ey Demmûn»), damme üzere mebnî, mahallen mansûb" + SUKUN_Q[2] + " — beyitler meştûr recezdendir.", HEMI),
 T("دَمُّونُ", "dammun", "propn", ["vocative-munada", "hadhf-wa-taqdir"],
   "مُنَادًى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَحَرْفُ النِّدَاءِ مَحْذُوفٌ — كَرَّرَ الِاسْمَ تَوْكِيدًا لِلنِّدَاءِ.",
   "A vocative, a single proper name built on damma in the seat of nasb, its particle dropped — the name is said again to strengthen the call.",
   "Münâdâ, müfred alem, damme üzere mebnî, mahallen mansûb; nidâ harfi mahzûf — isim, nidâyı pekiştirmek için tekrar edilmiştir."),
 T("إِنَّا", "inna", "part", ["inna-wa-akhawatuha"],
   "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَأَصْلُهُ «إِنَّنَا» فَحُذِفَتْ إِحْدَى النُّونَاتِ تَخْفِيفًا.",
   "إِنَّ is the particle of emphasis that puts its noun in nasb; نَا is its noun, in the seat of nasb — from إِنَّنَا, one nun dropped for lightness.",
   "إِنَّ tekit ve nasb harfi; نَا onun ismi, mahallen mansûb — aslı إِنَّنَا'dır, nûnlardan biri hafiflik için düşmüştür.", s=[("إِنَّ", "inna", "part"), P("نَا")]),
 T("مَعْشَرٌ", "mashar", "noun", ["inna-wa-akhawatuha"],
   "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ.", "The predicate of إِنَّ, in raf' by the damma.", "İnne'nin haberi, damme ile merfû."),
 T("يَمَانُونْ", "yamanin", "noun", ["naat-sifa", "jam-mudhakkar-salim", "ism-mansub", "al-qafiya"],
   "نَعْتٌ لِـ«مَعْشَرٌ» مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَسُكِّنَتْ نُونُهُ لِلْقَافِيَةِ — جَمْعُ «يَمَانٍ»، وَهُوَ الْمَنْسُوبُ إِلَى الْيَمَنِ عَلَى غَيْرِ قِيَاسٍ: الْأَلِفُ عِوَضٌ مِنْ إِحْدَى يَاءَيِ النَّسَبِ.",
   "An adjective of «a people», in raf' by the waw — a sound masculine plural, its nun stilled for the rhyme: the plural of يَمَانٍ, the irregular nisba to Yemen, whose alif stands in for one of the two ya's of the nisba.",
   "«Topluluk»un na'tı, cem-i müzekker sâlim olduğu için vâv ile merfû; nûnu kafiye için sâkin — «يَمَانٍ»in cem'i; bu, Yemen'e kıyas dışı nisbettir: elif, nisbet yâlarından birinin yerine gelmiştir.", "،"),
])
V(S1, 0, "and we truly love our own people.»", "ve biz ehlimizi gerçekten severiz.»", [
 T("وَإِنَّنَا", "inna", "part", ["atf-nasaq", "inna-wa-akhawatuha"],
   "الْوَاوُ عَاطِفَةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.",
   "The waw conjoins; إِنَّ is the particle of emphasis and nasb, and نَا is its noun, in the seat of nasb.",
   "Vâv atıf; إِنَّ tekit ve nasb harfi, نَا onun ismi, mahallen mansûb.", s=[WA, ("إِنَّ", "inna", "part"), P("نَا")]),
 T("لِأَهْلِنَا", "ahl", "noun", ["huruf-jarr", "idafa-definiteness", "hadhf-al-maful"],
   "اللَّامُ حَرْفُ جَرٍّ لِتَقْوِيَةِ الْعَامِلِ، وَأَهْلِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُحِبُّونَ»، وَقُدِّمَ الْمَعْمُولُ عَلَى عَامِلِهِ لِلِاهْتِمَامِ بِهِ.",
   "The lam is a jarr letter that strengthens the governing word; أَهْلِ is in jarr by the kasra, annexed, and نَا is its second term. The phrase hangs on «lovers», and is set before the word that governs it because it is what matters to the speaker.",
   "Lâm, âmili güçlendiren cer harfi; أَهْلِ kesre ile mecrûr, muzâf; نَا muzâfun ileyh. Câr-mecrûr «مُحِبُّونَ»ye müteallik; ma'mûl, önemsendiği için âmilinin önüne alınmıştır.", s=[LI, ("أَهْلِ", "ahl", "noun"), P("نَا")]),
 T("مُحِبُّونْ", "muhibb", "noun", ["inna-wa-akhawatuha", "jam-mudhakkar-salim", "ism-fail", "al-qafiya"],
   "خَبَرُ إِنَّ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَسُكِّنَتْ نُونُهُ لِلْقَافِيَةِ — اسْمُ فَاعِلٍ مِنْ «أَحَبَّ».",
   "The predicate of إِنَّ, in raf' by the waw — a sound masculine plural, its nun stilled for the rhyme; the ism fa'il of أَحَبَّ.",
   "İnne'nin haberi, cem-i müzekker sâlim olduğu için vâv ile merfû; nûnu kafiye için sâkin — «أَحَبَّ»nin ism-i fâili.", "."),
])
V(S1, 0, "Then he said: «He left me to waste when I was small, and has loaded his blood on me now that I am grown.",
  "Sonra dedi ki: «Küçükken beni başıboş bıraktı, büyüyünce de kanını (öcünü) bana yükledi.", [
 T("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ وَالتَّرَاخِيَ.", "A conjunction of order with an interval.", "Tertip ve terâhî bildiren atıf harfi."),
 T("قَالَ", "qala", "verb", ["hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
   "A past verb built on fatha; its doer is a hidden pronoun («he»).", "Fetha üzere mebnî mâzî; fâili gizli «hüve» zamiri.", ":"),
 T("ضَيَّعَنِي", "dayyaa", "verb", ["form-ii-verbs", "maful-bihi", "ya-al-mutakallim"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى أَبِيهِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
   "A past verb built on fatha; its doer is a hidden pronoun, his father; the nun guards the verb's ending, and the ya is the direct object, in the seat of nasb — the clause is what was said, in the seat of nasb.",
   "Fetha üzere mebnî mâzî; fâili babasına dönen gizli zamir; nûn vikâye içindir, yâ mef'ûlün bih, mahallen mansûb — cümle mekūlü'l-kavl olarak mahallen mansûb.", s=[("ضَيَّعَ", "dayyaa", "verb"), P("نِي")]),
 T("صَغِيرًا", "saghir", "noun", ["hal", "tibaq", "saj"],
   "حَالٌ مِنْ يَاءِ الْمُتَكَلِّمِ مَنْصُوبٌ بِالْفَتْحَةِ — وَبَيْنَهُ وَبَيْنَ «كَبِيرًا» طِبَاقُ إِيجَابٍ، وَالْفِقْرَتَانِ مَسْجُوعَتَانِ.",
   "A hal of the speaker's ya, in nasb by the fatha — with «grown» it makes a tibaq (two contraries), and the two clauses rhyme (saj').",
   "Mütekellim yâsından hâl, fetha ile mansûb — «كَبِيرًا» ile arasında tıbâk-ı îcâb vardır; iki fıkra da secilidir.", "،"),
 T("وَحَمَّلَنِي", "hammala", "verb", ["atf-nasaq", "form-ii-verbs", "mafulayn", "ya-al-mutakallim"],
   "الْوَاوُ عَاطِفَةٌ، وَحَمَّلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
   "The waw conjoins; حَمَّلَ is a past verb built on fatha with a hidden doer; the nun guards the ending, and the ya is the first object, in the seat of nasb.",
   "Vâv atıf; حَمَّلَ fetha üzere mebnî mâzî, fâili gizli; nûn vikâye için, yâ birinci mef'ûl, mahallen mansûb.", s=[WA, ("حَمَّلَ", "hammala", "verb"), P("نِي")]),
 T("دَمَهُ", "dam-blood", "noun", ["mafulayn", "idafa-definiteness", "majaz-mursal"],
   "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَفِيهِ مَجَازٌ مُرْسَلٌ عَلَاقَتُهُ السَّبَبِيَّةُ: ذَكَرَ الدَّمَ وَأَرَادَ طَلَبَ الثَّأْرِ بِهِ.",
   "The second object, in nasb by the fatha, annexed; the هُ is its second term — a majaz mursal whose tie is cause: he says «his blood» and means the vengeance owed for it.",
   "İkinci mef'ûl, fetha ile mansûb, muzâf; «hû» muzâfun ileyh — alâkası sebebiyet olan mecâz-ı mürsel: «kanı» deyip kan davasını (öcünü almayı) kastetmiştir.", s=[("دَمَ", "dam-blood", "noun"), P("هُ")]),
 T("كَبِيرًا", "kabir", "noun", ["hal", "tibaq", "saj"],
   "حَالٌ مِنْ يَاءِ الْمُتَكَلِّمِ مَنْصُوبٌ بِالْفَتْحَةِ — يُطَابِقُ «صَغِيرًا»، وَهُمَا فَاصِلَتَا السَّجْعِ.",
   "A hal of the speaker's ya, in nasb by the fatha — the contrary of «small»; the two words close the two rhymed clauses.",
   "Mütekellim yâsından hâl, fetha ile mansûb — «صَغِيرًا»nın zıddı; ikisi secinin fâsılalarıdır.", "،"),
])
V(S1, 0, "No sobering today, and no drunkenness tomorrow: today wine, and tomorrow the matter in hand.»",
  "Bugün ayılmak yok, yarın da sarhoşluk yok; bugün şarap, yarın iş.»", [
 T("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins"], "نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", "The لَا that denies the whole kind; it governs as إِنَّ does.", "Cinsi nefyeden lâ; inne gibi amel eder."),
 T("صَحْوَ", "sahw", "noun", ["la-nafiya-lil-jins", "muqabala"],
   "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — وَفِي الْكَلَامِ مُقَابَلَةٌ: الصَّحْوُ وَالْيَوْمُ بِإِزَاءِ السُّكْرِ وَالْغَدِ.",
   "The noun of لَا, built on fatha in the seat of nasb — the saying holds a muqabala: sobriety and today set against drunkenness and tomorrow.",
   "Lâ'nın ismi, fetha üzere mebnî, mahallen mansûb — sözde mukabele vardır: ayıklık ile bugün, sarhoşluk ile yarının karşısındadır."),
 T("الْيَوْمَ", "yawm", "noun", ["maful-fih", "la-nafiya-lil-jins"],
   "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ لَا.", "An adverb of time, in nasb by the fatha; it hangs on the omitted predicate of لَا.", "Zaman zarfı, fetha ile mansûb; lâ'nın mahzûf haberine müteallik.", "،"),
 T("وَلَا", "la-nafiya-lil-jins", "part", ["atf-nasaq", "la-nafiya-lil-jins"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ لِلْجِنْسِ.", "The waw conjoins; لَا denies the whole kind.", "Vâv atıf; lâ cinsi nefyeder.", s=[WA, ("لَا", "la-nafiya-lil-jins", "part")]),
 T("سُكْرَ", "sukr", "noun", ["la-nafiya-lil-jins", "tibaq"],
   "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — يُطَابِقُ «صَحْوَ».", "The noun of لَا, built on fatha in the seat of nasb — the contrary of «sobering».", "Lâ'nın ismi, fetha üzere mebnî, mahallen mansûb — «صَحْوَ»nın zıddı."),
 T("غَدًا", "ghad", "noun", ["maful-fih", "la-nafiya-lil-jins", "tibaq"],
   "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ لَا — يُطَابِقُ «الْيَوْمَ».", "An adverb of time, in nasb by the fatha; it hangs on the omitted predicate of لَا — the contrary of «today».", "Zaman zarfı, fetha ile mansûb; lâ'nın mahzûf haberine müteallik — «الْيَوْمَ»nin zıddı.", "،"),
 T("الْيَوْمَ", "yawm", "noun", ["maful-fih", "mubtada-khabar", "taqdim-al-musnad"],
   "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.", "An adverb of time, in nasb; it hangs on an omitted predicate, set first.", "Zaman zarfı, mansûb; öne geçmiş mahzûf habere müteallik."),
 T("خَمْرٌ", "khamr", "noun", ["mubtada-khabar", "saj"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَ«الْيَوْمَ خَمْرٌ وَغَدًا أَمْرٌ» فِقْرَتَانِ مَسْجُوعَتَانِ، وَقَدْ سَارَتَا مَثَلًا.",
   "The mubtada, placed last, in raf' by the damma — «today wine, and tomorrow the matter» are two rhymed clauses (saj'), and they became a proverb.",
   "Sona bırakılmış mübteda, damme ile merfû — «bugün şarap, yarın iş» secili iki fıkradır ve darbımesel olmuştur.", "،"),
 T("وَغَدًا", "ghad", "noun", ["atf-nasaq", "maful-fih", "mubtada-khabar"],
   "الْوَاوُ عَاطِفَةٌ، وَغَدًا ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.", "The waw conjoins; غَدًا is an adverb of time, in nasb, hanging on an omitted predicate set first.", "Vâv atıf; غَدًا zaman zarfı, mansûb, öne geçmiş mahzûf habere müteallik.", s=[WA, ("غَدًا", "ghad", "noun")]),
 T("أَمْرٌ", "amr", "noun", ["mubtada-khabar", "saj"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — أَيْ: شَأْنٌ عَظِيمٌ هُوَ طَلَبُ الثَّأْرِ؛ وَهُوَ فَاصِلَةُ السَّجْعِ مَعَ «خَمْرٌ».",
   "The mubtada, placed last, in raf' by the damma — a weighty matter, the pursuit of vengeance; it closes the saj' with «wine».",
   "Sona bırakılmış mübteda, damme ile merfû — yani büyük bir iş: öç peşine düşmek; «خَمْرٌ» ile secinin fâsılasıdır.", "."),
])
V(S1, 0, "Then he said:", "Sonra şöyle dedi:", [
 T("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ وَالتَّرَاخِيَ.", "A conjunction of order with an interval.", "Tertip ve terâhî bildiren atıf harfi."),
 T("قَالَ", "qala", "verb", ["hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَمَقُولُ الْقَوْلِ الْبَيْتُ بَعْدَهُ.",
   "A past verb built on fatha; its doer is a hidden pronoun — what he said is the verse that follows.", "Fetha üzere mebnî mâzî; fâili gizli zamir — mekūlü'l-kavl sonraki beyittir.", ":"),
])
V(S1, 0, "«My two friends, today holds no sobering-up for one who drinks — and tomorrow, since what has happened has happened, holds no drinking.»",
  "«Ey iki dostum! Bugün içen için ayılmak yok; olan olduktan sonra yarın da içmek yok.»", [
 T("خَلِيلَيَّ", "khalil", "noun", ["vocative-munada", "al-muthanna", "ya-al-mutakallim", "hadhf-wa-taqdir"],
   "مُنَادًى مُضَافٌ حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ، مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَأُدْغِمَتْ يَاؤُهُ فِي يَاءِ الْمُتَكَلِّمِ، وَهِيَ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْبَيْتُ مِنَ الطَّوِيلِ.",
   "An annexed vocative whose particle is dropped, in nasb by the ya — a dual; its nun falls for the annexation and its ya merges into the speaker's ya, which is the second term, in the seat of jarr — the verse is in al-ṭawīl.",
   "Nidâ harfi hazfedilmiş muzâf münâdâ; tesniye olduğu için yâ ile mansûb, nûnu izâfetle düşmüş, yâsı mütekellim yâsına idgam edilmiştir; o yâ muzâfun ileyh, mahallen mecrûr — beyit tavîl bahrindendir.", s=[("خَلِيلَيْ", "khalil", "noun"), P("يَ")]),
 T("مَا", "ma-nafiya", "part", ["ma-la-mushabbaha"], "نَافِيَةٌ لَا عَمَلَ لَهَا لِتَقَدُّمِ الْخَبَرِ عَلَى الْمُبْتَدَإِ.", "The negating مَا; it governs nothing here because the predicate comes before its subject.", "Nefy edatı mâ; haber mübtedanın önüne geçtiği için amel etmez."),
 HARF_JARR("فِي", "fi"),
 T("الْيَوْمِ", "yawm", "noun", ["huruf-jarr", "taqdim-al-musnad", "tibaq"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ؛ وَيُطَابِقُ «غَدٍ».", "In jarr by the kasra — the jarr phrase hangs on an omitted predicate, set first; the contrary of «tomorrow».", "Kesre ile mecrûr — câr-mecrûr öne geçmiş mahzûf habere müteallik; «غَدٍ»in zıddı."),
 T("مَصْحًى", "mashan", "noun", ["mubtada-khabar", "ism-maqsur-manqus", "masdar"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — مَصْدَرٌ مِيمِيٌّ مِنْ «صَحَا»: الْإِفَاقَةُ مِنَ السُّكْرِ.",
   "The mubtada, placed last, in raf' by a damma estimated on the alif that falls before the tanwin — a masdar with mim from صَحَا: coming round from drunkenness.",
   "Sona bırakılmış mübteda; tenvin sebebiyle düşen elif üzerinde takdîrî damme ile merfû — «صَحَا»dan mîmli masdar: sarhoşluktan ayılma."),
 T("لِشَارِبٍ", "sharib", "noun", ["huruf-jarr", "ism-fail", "naat-sifa"],
   "اللَّامُ حَرْفُ جَرٍّ، وَشَارِبٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَصْحًى».", "The lam is a jarr letter and شَارِبٍ is in jarr by the kasra — the phrase hangs on an omitted adjective of «sobering-up».", "Lâm cer harfi, شَارِبٍ kesre ile mecrûr — câr-mecrûr «مَصْحًى»nın mahzûf na'tına müteallik.", HEMI, [LI, ("شَارِبٍ", "sharib", "noun")]),
 T("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to strengthen the negation.", "Vâv atıf; lâ, nefyi pekiştirmek için zâiddir.", s=[WA, ("لَا", "la-nafiya", "part")]),
 HARF_JARR("فِي", "fi"),
 T("غَدٍ", "ghad", "noun", ["huruf-jarr", "taqdim-al-musnad", "tibaq"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ لِـ«مَشْرَبُ».", "In jarr by the kasra — the jarr phrase hangs on an omitted predicate, set before «drinking».", "Kesre ile mecrûr — câr-mecrûr «مَشْرَبُ»ün öne geçmiş mahzûf haberine müteallik."),
 T("إِذْ", "idh", "noun", ["maful-fih"],
   "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ — وَفِيهِ مَعْنَى التَّعْلِيلِ.", "An adverb for past time, built on sukun in the seat of nasb, annexed to the clause after it — it carries the sense of «since».", "Geçmiş zaman zarfı, sükûn üzere mebnî, mahallen mansûb; sonraki cümleye muzâf — ta'lîl anlamı taşır («madem ki»)."),
 T("كَانَ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs"],
   "فِعْلٌ مَاضٍ تَامٌّ بِمَعْنَى «حَدَثَ» مَبْنِيٌّ عَلَى الْفَتْحِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذْ» إِلَيْهَا.", "A past verb, here COMPLETE («happened»), built on fatha — the clause is in the seat of jarr, annexed to إِذْ.", "Fetha üzere mebnî mâzî; burada tâm fiil («oldu») — cümle «إِذْ»in muzâfun ileyhi olarak mahallen mecrûr."),
 T("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail", "tarif-al-musnad-ilayh"],
   "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلُ «كَانَ» — وَفِي إِبْهَامِ الصِّلَةِ «مَا كَانَ» تَفْخِيمٌ لِلْأَمْرِ وَتَهْوِيلٌ.", "A relative pronoun built on sukun, the doer of «happened», in the seat of raf' — leaving the thing unnamed («what happened») makes it loom large.", "İsm-i mevsûl, sükûn üzere mebnî; «كَانَ»nin fâili, mahallen merfû — sılanın müphem bırakılması («olan») işi büyütür ve korkunçlaştırır."),
 T("كَانَ", "kana", "verb", ["al-fil-al-tamm-wal-naqis", "hollow-verbs", "ism-mawsul"],
   "فِعْلٌ مَاضٍ تَامٌّ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.", "A complete past verb built on fatha; its doer is a hidden pronoun that returns to مَا — the clause is the relative's ṣila and has no seat.", "Fetha üzere mebnî tâm mâzî; fâili «مَا»ya dönen gizli zamir — cümle sıladır, i'râbdan mahalli yoktur."),
 T("مَشْرَبُ", "mashrab", "noun", ["mubtada-khabar", "masdar", "al-qafiya"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ" + QAFIYA[0] + " — مَصْدَرٌ مِيمِيٌّ بِمَعْنَى الشُّرْبِ؛ وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الَّتِي قَبْلَهَا.",
   "The mubtada, placed last, in raf' by the damma" + QAFIYA[1] + " — a masdar with mim, «drinking»; the clause is conjoined to the one before it.",
   "Sona bırakılmış mübteda, damme ile merfû" + QAFIYA[2] + " — «içme» anlamında mîmli masdar; cümle öncekine ma'tûftur.", "."),
])
V(S1, 0, "Then he swore that he would eat no meat and drink no wine until he had taken vengeance for his father.",
  "Sonra, babasının öcünü alıncaya kadar et yememeye ve şarap içmemeye yemin etti.", [
 T("ثُمَّ", "thumma", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ وَالتَّرَاخِيَ.", "A conjunction of order with an interval.", "Tertip ve terâhî bildiren atıf harfi."),
 T("آلَى", "ala-swear", "verb", ["form-iv-verbs", "naqis-verbs"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — مِنَ الْإِفْعَالِ، وَأَصْلُهُ «أَأْلَى»: حَلَفَ.",
   "A past verb built on a fatha estimated on the alif; its doer is a hidden pronoun — Form IV, from أَأْلَى: he swore an oath.",
   "Elif üzerinde takdîrî fetha üzere mebnî mâzî; fâili gizli zamir — if'âl bâbından, aslı «أَأْلَى»: yemin etti."),
 T("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ — وَالْجُمْلَةُ بَعْدَهَا جَوَابُ الْقَسَمِ الَّذِي تَضَمَّنَهُ «آلَى» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.", "The negating لَا — the clause after it answers the oath that «he swore» holds, and has no seat.", "Nefy lâsı — sonraki cümle, «آلَى»nın içerdiği yeminin cevabıdır; i'râbdan mahalli yoktur."),
 T("يَأْكُلُ", "akala", "verb", ["mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "A present verb in raf' by the damma; its doer is a hidden pronoun.", "Damme ile merfû muzâri; fâili gizli zamir."),
 T("لَحْمًا", "lahm", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — نَكِرَةٌ فِي سِيَاقِ النَّفْيِ فَتَعُمُّ.", "The direct object, in nasb by the fatha — an indefinite under a negation, so it takes in every kind.", "Mef'ûlün bih, fetha ile mansûb — nefy siyâkında nekre olduğu için umûm ifade eder."),
 T("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "The waw conjoins; لَا negates.", "Vâv atıf; lâ nefy içindir.", s=[WA, ("لَا", "la-nafiya", "part")]),
 T("يَشْرَبُ", "shariba", "verb", ["mudari-marfu", "atf-nasaq"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جَوَابِ الْقَسَمِ.", "A present verb in raf' by the damma, with a hidden doer — the clause is conjoined to the answer of the oath.", "Damme ile merfû muzâri, fâili gizli — cümle yeminin cevabına ma'tûftur."),
 T("خَمْرًا", "khamr", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The direct object, in nasb by the fatha.", "Mef'ûlün bih, fetha ile mansûb."),
 T("حَتَّى", "hatta", "part", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari"], "حَرْفُ غَايَةٍ وَجَرٍّ، وَالْمُضَارِعُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا.", "حَتَّى «until»: a jarr letter of the end-point; the verb after it is in nasb by an أَنْ that must stay unspoken.", "Gaye bildiren cer harfi «-inceye kadar»; sonraki muzâri vücûben gizli أَنْ ile mansûbdur."),
 T("يَثْأَرَ", "thaara", "verb", ["nawasib-wa-jawazim-al-mudari", "thulathi-mujarrad-babs"],
   "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ حَتَّى، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
   "A present verb in nasb by the unspoken أَنْ after حَتَّى — its sign the fatha; its doer is a hidden pronoun, and the masdar so built is in jarr by حَتَّى.",
   "Hattâ'dan sonra vücûben gizli أَنْ ile mansûb muzâri; nasb alâmeti fetha, fâili gizli zamir — müevvel masdar hattâ ile mecrûr."),
 T("بِأَبِيهِ", "ab", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَأَبِي مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَثْأَرَ»: ثَأَرَ بِهِ أَيْ طَلَبَ دَمَهُ.",
   "The ba is a jarr letter; أَبِي is in jarr by the ya — one of the five nouns — annexed, and the هِ is its second term. The phrase hangs on «take vengeance»: ثَأَرَ بِهِ is to seek a slain man's blood.",
   "Bâ cer harfi; أَبِي esmâ-i hamseden olduğu için yâ ile mecrûr, muzâf; «hî» muzâfun ileyh. Câr-mecrûr «يَثْأَرَ»ye müteallik: ثَأَرَ بِهِ, öldürülenin kanını aramak demektir.", ".", [BI, ("أَبِي", "ab", "noun"), P("هِ")]),
])

# =====================================================================================================================
# The halt at the ruins: verses 1–6 (al-Zawzanī)
# =====================================================================================================================
MAQSUR_J = "بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"
V(S2, 1, "Halt, you two, and let us weep for the memory of a beloved and a dwelling — at the edge of the winding sand between al-Dakhūl and Ḥawmal,",
  "Durun (ey iki yoldaşım), bir sevgilinin ve bir konağın hatırasıyla ağlayalım; Dehûl ile Havmel arasında, kıvrılan kumun inceldiği yerde,", [
 T("قِفَا", "waqafa", "verb", ["imperative-amr", "al-amr-wa-wujuhuh", "mithal-verbs", "husn-al-ibtida-wal-takhallus-wal-intiha"],
   "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِاتِّصَالِهِ بِأَلِفِ الِاثْنَيْنِ، وَالْأَلِفُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — خَاطَبَ صَاحِبَيْهِ، وَقِيلَ: خَاطَبَ وَاحِدًا خِطَابَ الِاثْنَيْنِ عَلَى عَادَةِ الْعَرَبِ، وَقِيلَ: الْأَلِفُ مُنْقَلِبَةٌ عَنْ نُونِ التَّوْكِيدِ الْخَفِيفَةِ فَيَكُونُ مَبْنِيًّا عَلَى الْفَتْحِ. وَالْأَمْرُ لِلِالْتِمَاسِ لِأَنَّهُ مِنَ الرَّفِيقِ لِرَفِيقِهِ؛ وَبِهٰذَا الْمَطْلَعِ مَثَّلَ التَّلْخِيصُ لِحُسْنِ الِابْتِدَاءِ. وَالْقَصِيدَةُ مِنَ الطَّوِيلِ.",
   "An imperative built on dropping the nun because the alif of the dual is attached; the alif is the doer, in the seat of raf'. He speaks to his two companions — or, it is said, to one in the dual, as the Arabs do; or the alif stands for the light nun of emphasis, and the verb is then built on fatha. The command is a request between equals (iltimās); the Talkhīṣ cites this opening for the fine beginning (ḥusn al-ibtidāʾ). The poem is in al-ṭawīl.",
   "Tesniye elifine bitiştiği için nûnun hazfi üzere mebnî emir; elif fâil, mahallen merfû. İki arkadaşına hitap eder; «tek kişiye, Arapların âdeti üzere tesniye ile hitap etmiştir» de denmiş, «elif hafif tekit nûnundan dönmedir, fiil fetha üzere mebnîdir» de denmiştir. Emir, yoldaştan yoldaşa olduğu için iltimâs içindir; Telhîs bu matlaı hüsn-i ibtidâya örnek verir. Kaside tavîl bahrindendir."),
 T("نَبْكِ", "baka", "verb", ["jawab-al-talab", "naqis-verbs"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الْأَمْرِ، وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْيَاءِ) وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: نَحْنُ — وَعِنْدَ الْجُمْهُورِ جَازِمُهُ شَرْطٌ مُقَدَّرٌ: إِنْ تَقِفَا نَبْكِ.",
   "A present verb in jazm as the answer of the command; the sign is the dropped weak letter (the ya), with the kasra left to show it; its doer is the hidden «we» — most grammarians say it is put in jazm by an implied condition: «if you halt, we weep».",
   "Emrin cevabında meczûm muzâri; cezm alâmeti illet harfinin (yâ) hazfi, kesre ona delildir; fâili vücûben gizli «nahnu» — cumhura göre câzimi mukadder şarttır: «durursanız ağlarız»."),
 HARF_JARR("مِنْ", "min", "، وَهُوَ هُنَا لِلتَّعْلِيلِ", " — here it gives the cause", " — burada ta'lîl içindir"),
 T("ذِكْرَى", "dhikra", "noun", ["huruf-jarr", "ism-maqsur-manqus", "idafa-definiteness", "imal-al-masdar"],
   "مَجْرُورٌ " + MAQSUR_J + "، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَبْكِ»؛ مَصْدَرٌ بِمَعْنَى التَّذَكُّرِ.",
   "In jarr by a kasra estimated on the alif, annexed — the jarr phrase hangs on «let us weep»; a masdar, «remembering».",
   "Elif üzerinde takdîrî kesre ile mecrûr, muzâf — câr-mecrûr «نَبْكِ»ye müteallik; «hatırlama» anlamında masdar."),
 T("حَبِيبٍ", "habib", "noun", ["idafa-definiteness", "imal-al-masdar"],
   MI[0] + " — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ.", MI[1] + " — the masdar is annexed to its object.", MI[2] + " — masdarın mef'ûlüne izâfeti."),
 T("وَمَنْزِلِ", "manzil", "noun", ["atf-nasaq", "al-qafiya"],
   "الْوَاوُ عَاطِفَةٌ، وَمَنْزِلِ مَعْطُوفٌ عَلَى «حَبِيبٍ» مَجْرُورٌ بِالْكَسْرَةِ، وَحُذِفَ تَنْوِينُهُ لِلتَّصْرِيعِ: جُعِلَتِ الْعَرُوضُ كَالضَّرْبِ فِي الْوَزْنِ وَالرَّوِيِّ.",
   "The waw conjoins; مَنْزِلِ is conjoined to «a beloved», in jarr by the kasra; its tanwin is dropped for the taṣrīʿ — the end of the first hemistich is made to match the end of the verse in measure and rhyme-letter.",
   "Vâv atıf; مَنْزِلِ «حَبِيبٍ»e ma'tûf, kesre ile mecrûr; tenvini tasrî' için düşmüştür: arûz, vezinde ve revîde darb gibi kılınmıştır.", HEMI, [WA, ("مَنْزِلِ", "manzil", "noun")]),
 T("بِسِقْطِ", "siqt", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَسِقْطِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«مَنْزِلِ»، وَيَجُوزُ تَعْلِيقُهُمَا بِـ«قِفَا» أَوْ «نَبْكِ».",
   "The ba is a jarr letter meaning «in»; سِقْطِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «a dwelling», or it may hang on «halt» or on «let us weep».",
   "Bâ «-de» anlamında cer harfi; سِقْطِ kesre ile mecrûr, muzâf — câr-mecrûr «مَنْزِلِ»in mahzûf na'tına müteallik; «قِفَا»ya ya da «نَبْكِ»ye bağlanması da câizdir.", s=[BI, ("سِقْطِ", "siqt", "noun")]),
 T("اللِّوَى", "liwa", "noun", ["idafa-definiteness", "ism-maqsur-manqus"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + MAQSUR_J + ".", "The second term of the idafa, in jarr by a kasra estimated on the alif.", "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr."),
 T("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"],
   "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِمَا تَعَلَّقَ بِهِ «بِسِقْطِ».", "An adverb of place, in nasb by the fatha, annexed — it hangs on what «at the edge» hangs on.", "Mekân zarfı, fetha ile mansûb, muzâf — «بِسِقْطِ»in bağlandığı şeye müteallik."),
 T("الدَّخُولِ", "dakhul", "propn", ["idafa-definiteness"], MI[0] + " — اسْمُ مَوْضِعٍ.", MI[1] + " — the name of a place.", MI[2] + " — bir yer adı."),
 T("فَحَوْمَلِ", "hawmal", "propn", ["atf-nasaq", "mamnu-min-sarf", "al-qafiya"],
   "الْفَاءُ عَاطِفَةٌ، وَحَوْمَلِ مَعْطُوفٌ عَلَى «الدَّخُولِ» مَجْرُورٌ بِالْكَسْرَةِ لِضَرُورَةِ الشِّعْرِ، وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ لِأَنَّهُ عَلَمٌ — وَالتَّقْدِيرُ: بَيْنَ مَوَاضِعِ الدَّخُولِ فَمَوَاضِعِ حَوْمَلَ.",
   "The fa conjoins; حَوْمَلِ is conjoined to «al-Dakhūl», in jarr by the kasra as verse allows — as a proper name it would be a diptote; the sense is «between the places of al-Dakhūl and then the places of Ḥawmal».",
   "Fâ atıf; حَوْمَلِ «الدَّخُولِ»e ma'tûf, şiir zarûretiyle kesre ile mecrûr; alem olduğu için aslında gayr-i munsariftir — takdiri: «Dehûl'ün yerleri, sonra Havmel'in yerleri arasında».", "،", [FA, ("حَوْمَلِ", "hawmal", "propn")]),
])
V(S2, 2, "and Tūḍiḥ and al-Miqrāt — its trace is not wiped out, because of what the south wind and the north wind have woven over it.",
  "Tûdıh ve Mikrât (arasında). Oranın izi silinmemiştir; çünkü güney ve kuzey rüzgârları onu dokuyup durmuştur.", [
 T("فَتُوضِحَ", "tudih", "propn", ["atf-nasaq", "mamnu-min-sarf"],
   "الْفَاءُ عَاطِفَةٌ، وَتُوضِحَ مَعْطُوفٌ عَلَى «حَوْمَلِ» مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ؛ وَعَلَّلَهُ الدُّرَّةُ بِالْعَلَمِيَّةِ وَالْعُجْمَةِ، وَقِيلَ: بِالْعَلَمِيَّةِ وَالتَّأْنِيثِ.",
   "The fa conjoins; تُوضِحَ is conjoined to «Ḥawmal», in jarr by the fatha in place of the kasra — a diptote: a proper name on the pattern of a verb. Al-Durra gives the cause as the proper name with foreign origin — or, it is said, with the feminine (a place-name).",
   "Fâ atıf; تُوضِحَ «حَوْمَلِ»e ma'tûf, alemiyet ve vezn-i fiil sebebiyle gayr-i munsarif olduğundan kesre yerine fetha ile mecrûr. Dürre sebebi alemiyet ile ucme olarak gösterir; alemiyet ile te'nîs olduğu da söylenmiştir.", s=[FA, ("تُوضِحَ", "tudih", "propn")]),
 T("فَالْمِقْرَاةِ", "miqrat", "propn", ["atf-nasaq"],
   "الْفَاءُ عَاطِفَةٌ، وَالْمِقْرَاةِ مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ — وَسِقْطُ اللِّوَى بَيْنَ هٰذِهِ الْمَوَاضِعِ الْأَرْبَعَةِ.",
   "The fa conjoins; الْمِقْرَاةِ is conjoined, in jarr by the kasra — the edge of the sand lies among these four places.",
   "Fâ atıf; الْمِقْرَاةِ ma'tûf, kesre ile mecrûr — Sıktu'l-Livâ bu dört yerin arasındadır.", s=[FA, ("الْمِقْرَاةِ", "miqrat", "propn")]),
 T("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The particle of negation that puts the verb in jazm and turns it to the past.", "Nefy, cezm ve kalb harfi."),
 T("يَعْفُ", "afa", "verb", ["lam-jazim", "naqis-verbs"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْوَاوِ) وَالضَّمَّةُ دَلِيلٌ عَلَيْهَا — عَفَا الرَّسْمُ: انْمَحَى.",
   "A present verb in jazm by لَمْ; the sign is the dropped weak letter (the waw), with the damma left to show it — عَفَا of a trace: it was wiped out.",
   "Lem ile meczûm muzâri; cezm alâmeti illet harfinin (vâv) hazfi, damme ona delildir — izin «عَفَا»sı: silinmesi."),
 T("رَسْمُهَا", "rasm", "noun", ["fail", "idafa-definiteness", "hal"],
   "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْمَوَاضِعِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهَا.",
   "The doer, in raf' by the damma, annexed; هَا is its second term and returns to the places — the clause is a hal of them, in the seat of nasb.",
   "Fâil, damme ile merfû, muzâf; هَا muzâfun ileyh olup o yerlere döner — cümle onlardan hâl olarak mahallen mansûb.", HEMI, [("رَسْمُ", "rasm", "noun"), P("هَا")]),
 T("لِمَا", "ma-mawsula", "pron", ["huruf-jarr", "ism-mawsul"],
   "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَعْفُ»؛ وَيَجُوزُ أَنْ تَكُونَ «مَا» مَصْدَرِيَّةً.",
   "The lam is a jarr letter of cause; مَا is a relative pronoun built on sukun, in the seat of jarr — the phrase hangs on «is wiped out»; مَا may also be read as the masdar-making مَا.",
   "Lâm ta'lîl bildiren cer harfi; مَا sükûn üzere mebnî ism-i mevsûl, mahallen mecrûr — câr-mecrûr «يَعْفُ»ya müteallik; «مَا»nın masdariyye olması da câizdir.", s=[LI, ("مَا", "ma-mawsula", "pron")]),
 T("نَسَجَتْهَا", "nasaja", "verb", ["thulathi-mujarrad-babs", "maful-bihi", "ism-mawsul", "istiara", "istiara-tabaiyya"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «مَا» الْمُفَسَّرَةِ بِالرِّيحَيْنِ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ — وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ تَبَعِيَّةٌ: شُبِّهَ اخْتِلَافُ الرِّيحَيْنِ عَلَى الرَّسْمِ، تَسْتُرُهُ إِحْدَاهُمَا بِالتُّرَابِ وَتَكْشِفُهُ الْأُخْرَى، بِالنَّسْجِ، ثُمَّ اشْتُقَّ مِنْهُ الْفِعْلُ.",
   "A past verb built on fatha; the ta marks the feminine, هَا is the direct object, and the doer is a hidden «she» returning to مَا, which the two winds explain; the clause is the ṣila. An explicit istiʿāra carried in the verb (tabaʿiyya): the two winds crossing over the trace — one covering it with dust, the other baring it — are likened to weaving, and the verb is drawn from that.",
   "Fetha üzere mebnî mâzî; tâ te'nîs için, هَا mef'ûlün bih, fâil iki rüzgârla açıklanan «مَا»ya dönen gizli «hiye»; cümle sıladır. İstiâre-i tasrîhiyye tebeiyye vardır: iki rüzgârın iz üzerinde gidip gelmesi — biri toprakla örter, öbürü açar — dokumaya benzetilmiş, fiil bundan türetilmiştir.", s=[("نَسَجَتْ", "nasaja", "verb"), P("هَا")]),
 HARF_JARR("مِنْ", "min", " لِبَيَانِ الْجِنْسِ، يُفَسِّرُ مَا أُبْهِمَ فِي «مَا»", " that names the kind: it explains what مَا left unnamed", " — cinsi beyan eder: «مَا»daki kapalılığı açıklar"),
 T("جَنُوبٍ", "janub", "noun", ["huruf-jarr", "tibaq"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ فَاعِلِ «نَسَجَتْ»؛ وَبَيْنَ الْجَنُوبِ وَالشَّمْأَلِ طِبَاقٌ لِتَقَابُلِ الرِّيحَيْنِ.",
   "In jarr by the kasra — the jarr phrase hangs on an omitted hal of the doer of «wove»; south and north make a tibaq, the two winds facing each other.",
   "Kesre ile mecrûr — câr-mecrûr «نَسَجَتْ»in fâilinden mahzûf hâle müteallik; iki rüzgâr birbirinin karşıtı olduğu için güney ile kuzey arasında tıbâk vardır."),
 T("وَشَمْأَلِ", "shamal", "noun", ["atf-nasaq", "tibaq", "al-qafiya"],
   "الْوَاوُ عَاطِفَةٌ، وَشَمْأَلِ مَعْطُوفٌ عَلَى «جَنُوبٍ» مَجْرُورٌ بِالْكَسْرَةِ" + QAFIYA[0] + " — لُغَةٌ فِي الشَّمَالِ.",
   "The waw conjoins; شَمْأَلِ is conjoined to «south wind», in jarr by the kasra" + QAFIYA[1] + " — a dialect form of الشَّمَال.",
   "Vâv atıf; شَمْأَلِ «جَنُوبٍ»a ma'tûf, kesre ile mecrûr" + QAFIYA[2] + " — «الشَّمَال»in bir lügatidir.", ".", [WA, ("شَمْأَلِ", "shamal", "noun")]),
])
V(S2, 3, "You see the droppings of the white antelopes in its courtyards and its level grounds, like peppercorns.",
  "Onun avlularında ve düzlüklerinde ak ceylanların tersini görürsün; sanki karabiber taneleridir.", [
 T("تَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — خِطَابٌ لِغَيْرِ مُعَيَّنٍ.",
   "A present verb in raf' by a damma estimated on the alif; its doer is the hidden «you» — addressed to no one in particular.",
   "Elif üzerinde takdîrî damme ile merfû muzâri; fâili vücûben gizli «ente» — belirli olmayan muhataba hitaptır."),
 T("بَعَرَ", "baar", "noun", ["maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The direct object, in nasb by the fatha, annexed.", "Mef'ûlün bih, fetha ile mansûb, muzâf."),
 T("الْأَرْآمِ", "rim", "noun", ["idafa-definiteness", "jam-taksir"], MI[0] + " — جَمْعُ رِئْمٍ.", MI[1] + " — the plural of رِئْم.", MI[2] + " — «رِئْم»in cem'i."),
 HARF_JARR("فِي", "fi"),
 T("عَرَصَاتِهَا", "arsa-plot", "noun", ["huruf-jarr", "idafa-definiteness", "jam-muannath-salim"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَرَى»؛ جَمْعُ عَرْصَةٍ، وَفُتِحَتْ رَاؤُهُ فِي الْجَمْعِ.",
   "In jarr by the kasra, annexed; هَا is its second term — the jarr phrase hangs on «you see»; the plural of عَرْصَة, whose ra takes a fatha in the plural.",
   "Kesre ile mecrûr, muzâf; هَا muzâfun ileyh — câr-mecrûr «تَرَى»ya müteallik; «عَرْصَة»nin cem'i, cemide râ fethalanır.", HEMI, [("عَرَصَاتِ", "arsa-plot", "noun"), P("هَا")]),
 T("وَقِيعَانِهَا", "qa", "noun", ["atf-nasaq", "idafa-definiteness", "jam-taksir"],
   "الْوَاوُ عَاطِفَةٌ، وَقِيعَانِ مَعْطُوفٌ عَلَى «عَرَصَاتِ» مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ — جَمْعُ قَاعٍ.",
   "The waw conjoins; قِيعَانِ is conjoined to «courtyards», in jarr by the kasra, annexed, and هَا is its second term — the plural of قَاع.",
   "Vâv atıf; قِيعَانِ «عَرَصَاتِ»e ma'tûf, kesre ile mecrûr, muzâf; هَا muzâfun ileyh — «قَاع»ın cem'i.", s=[WA, ("قِيعَانِ", "qa", "noun"), P("هَا")]),
 T("كَأَنَّهُ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا يَعُودُ عَلَى الْبَعَرِ — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ بَعَرُ الْأَرْآمِ، وَالْمُشَبَّهُ بِهِ حَبُّ الْفُلْفُلِ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الْهَيْئَةُ فِي الصِّغَرِ وَاللَّوْنِ.",
   "كَأَنَّ is the verb-like particle of likening; the هُ is its noun, in the seat of nasb, returning to the droppings. A tashbih mursal mujmal: the thing likened is the antelopes' droppings, the thing it is likened to is peppercorns, the particle is كَأَنَّ, and the point of likeness is left unsaid — the look of them, small and dark.",
   "كَأَنَّ teşbih bildiren fiile benzeyen harf; «hû» onun ismi, mahallen mansûb, terse döner. Teşbih-i mürsel mücmeldir: müşebbeh ceylan tersi, müşebbehün bih karabiber tanesi, edat كَأَنَّ; vech-i şebeh mahzûftur — küçüklük ve renkteki görünüş.", s=[("كَأَنَّ", "kaanna", "part"), P("هُ")]),
 T("حَبُّ", "habb-grain", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "hal"],
   "خَبَرُ كَأَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «بَعَرَ الْأَرْآمِ».", "The predicate of كَأَنَّ, in raf' by the damma, annexed — the clause is a hal of «the droppings of the antelopes», in the seat of nasb.", "كَأَنَّ'nin haberi, damme ile merfû, muzâf — cümle «ceylan tersi»nden hâl olarak mahallen mansûb."),
 T("فُلْفُلِ", "fulful", "noun", ["idafa-definiteness", "al-qafiya"], MI[0] + QAFIYA[0] + ".", MI[1] + QAFIYA[1] + ".", MI[2] + QAFIYA[2] + ".", "."),
])
YA_MUQ = "مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ"
V(S2, 4, "On the morning of the parting, the day they loaded and left, I was — by the acacias of the tribe — like one splitting colocynth.",
  "Ayrılık sabahı, yüklerini yükleyip gittikleri gün, kabilenin semure ağaçları yanında sanki Ebucehil karpuzu yaran biri gibiydim.", [
 T("كَأَنِّي", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الشَّاعِرُ، وَالْمُشَبَّهُ بِهِ نَاقِفُ الْحَنْظَلِ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ: الْحَيْرَةُ، وَقِيلَ: سَيَلَانُ الدَّمْعِ لِأَنَّ نَاقِفَ الْحَنْظَلِ تَدْمَعُ عَيْنَاهُ. وَعَدَّهُ ابْنُ قُتَيْبَةَ مِمَّا يُسْتَجَادُ مِنْ تَشْبِيهِهِ.",
   "كَأَنَّ is the verb-like particle of likening; the speaker's ya is its noun, in the seat of nasb. A tashbih mursal mujmal: the thing likened is the poet, the thing he is likened to is the splitter of colocynth, the particle is كَأَنَّ, and the point of likeness is left unsaid — bewilderment; or, it is said, streaming tears, for the eyes of one who splits colocynth water. Ibn Qutayba counts it among his finest similes.",
   "كَأَنَّ teşbih bildiren fiile benzeyen harf; mütekellim yâsı onun ismi, mahallen mansûb. Teşbih-i mürsel mücmeldir: müşebbeh şair, müşebbehün bih Ebucehil karpuzu yaran kişi, edat كَأَنَّ; vech-i şebeh mahzûftur: şaşkınlık; «gözyaşının akması» da denmiştir, çünkü onu yaranın gözleri yaşarır. İbn Kuteybe bunu onun beğenilen teşbihlerinden sayar.", s=[("كَأَنَّ", "kaanna", "part"), P("ي")]),
 T("غَدَاةَ", "ghadat", "noun", ["maful-fih", "idafa-definiteness"],
   "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِـ«نَاقِفُ»، وَيَجُوزُ تَعْلِيقُهُ بِمَا فِي «كَأَنَّ» مِنْ مَعْنَى التَّشْبِيهِ.",
   "An adverb of time, in nasb by the fatha, annexed — it hangs on «splitter», or on the sense of likening in كَأَنَّ.",
   "Zaman zarfı, fetha ile mansûb, muzâf — «نَاقِفُ»e müteallik; «كَأَنَّ»deki teşbih mânâsına bağlanması da câizdir."),
 T("الْبَيْنِ", "bayn-parting", "noun", ["idafa-definiteness"], MI[0] + " — الْبَيْنُ: الْفُرْقَةُ.", MI[1] + " — البَيْن: parting.", MI[2] + " — البَيْن: ayrılık."),
 T("يَوْمَ", "yawm", "noun", ["maful-fih", "badal", "idafa-definiteness"],
   "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، بَدَلٌ مِنْ «غَدَاةَ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time, in nasb by the fatha — a badal of «the morning» — annexed to the clause after it.", "Zaman zarfı, fetha ile mansûb; «غَدَاةَ»den bedel, sonraki cümleye muzâf."),
 T("تَحَمَّلُوا", "tahammala", "verb", ["form-v-verbs", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «يَوْمَ» إِلَيْهَا؛ تَحَمَّلُوا: ارْتَحَلُوا.",
   "A past verb built on damma because the waw of the group is attached; the waw is the doer, in the seat of raf' — the clause is in the seat of jarr, annexed to «the day»; تَحَمَّلُوا: they set off.",
   "Cemâat vâvına bitiştiği için damme üzere mebnî mâzî; vâv fâil, mahallen merfû — cümle «يَوْمَ»nin muzâfun ileyhi olarak mahallen mecrûr; تَحَمَّلُوا: göç ettiler.", HEMI),
 T("لَدَى", "lada", "noun", ["maful-fih", "idafa-definiteness", "ism-maqsur-manqus"],
   "ظَرْفُ مَكَانٍ بِمَعْنَى «عِنْدَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ — مُتَعَلِّقٌ بِمَا تَعَلَّقَ بِهِ «غَدَاةَ».", "An adverb of place meaning «at», in nasb by a fatha estimated on the alif, annexed — it hangs on what «the morning» hangs on.", "«عِنْدَ» anlamında mekân zarfı; elif üzerinde takdîrî fetha ile mansûb, muzâf — «غَدَاةَ»in bağlandığı şeye müteallik."),
 T("سَمُرَاتِ", "samura-tree", "noun", ["idafa-definiteness", "jam-muannath-salim"], MI[0] + "، مُضَافٌ — جَمْعُ سَمُرَةٍ.", MI[1] + ", annexed in turn — the plural of سَمُرَة.", MI[2] + ", muzâf — «سَمُرَة»nin cem'i."),
 T("الْحَيِّ", "hayy-tribe", "noun", ["idafa-definiteness"], MI[0] + ".", MI[1] + ".", MI[2] + "."),
 T("نَاقِفُ", "naqif", "noun", ["inna-wa-akhawatuha", "ism-fail", "idafa-definiteness", "idafa-lafziyya"],
   "خَبَرُ كَأَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ فَاعِلٍ مِنْ «نَقَفَ الْحَنْظَلَ»: شَقَّهُ عَنْ حَبِّهِ.", "The predicate of كَأَنَّ, in raf' by the damma, annexed — the ism fa'il of نَقَفَ الْحَنْظَلَ: to split the colocynth for its seed.", "كَأَنَّ'nin haberi, damme ile merfû, muzâf — «نَقَفَ الْحَنْظَلَ»dan ism-i fâil: Ebucehil karpuzunu çekirdeği için yarmak."),
 T("حَنْظَلِ", "hanzal", "noun", ["idafa-definiteness", "idafa-lafziyya", "al-qafiya"], MI[0] + QAFIYA[0] + " — مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ.", MI[1] + QAFIYA[1] + " — the ism fa'il is annexed to its object.", MI[2] + QAFIYA[2] + " — ism-i fâilin mef'ûlüne izâfeti.", "."),
])
V(S2, 5, "— while my companions, halting their mounts there over me, say: «Do not perish of grief; bear it with grace.»",
  "Arkadaşlarım orada bineklerini başımda durdurmuş, «Üzüntüden helâk olma, metin ol» diyorlardı.", [
 T("وُقُوفًا", "wuquf", "noun", ["hal", "jam-taksir"],
   "حَالٌ مَنْصُوبٌ بِالْفَتْحَةِ، عَامِلُهُ «قِفَا» فِي أَوَّلِ الْقَصِيدَةِ، أَيْ: قِفَا نَبْكِ فِي حَالِ وَقْفِ أَصْحَابِي مَطِيَّهُمْ عَلَيَّ — جَمْعُ وَاقِفٍ كَشَاهِدٍ وَشُهُودٍ، يَرْفَعُ «صَحْبِي» وَيَنْصِبُ «مَطِيَّهُمْ»؛ وَقِيلَ: مَصْدَرٌ فَهُوَ مَفْعُولٌ مُطْلَقٌ.",
   "A hal, in nasb by the fatha, governed by «halt» at the head of the poem: «halt and let us weep, as my companions hold their mounts over me» — the plural of وَاقِف (as شُهُود of شَاهِد); it raises «my companions» and puts «their mounts» in nasb. It is also read as a masdar, and then it is an absolute object.",
   "Hâl, fetha ile mansûb; âmili kasidenin başındaki «قِفَا»dır: «arkadaşlarım bineklerini başımda durdururken durun, ağlayalım» — «وَاقِف»in cem'idir (şâhid–şühûd gibi); «صَحْبِي»yi ref', «مَطِيَّهُمْ»ü nasb eder. Masdar olduğu da söylenmiştir; o takdirde mef'ûlün mutlaktır."),
 T("بِهَا", "bi", "prep", ["huruf-jarr"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى الدِّيَارِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وُقُوفًا».", "The ba is a jarr letter meaning «in»; هَا is in the seat of jarr and returns to the abodes — the phrase hangs on «halting».", "Bâ «-de» anlamında cer harfi; هَا mahallen mecrûr, diyara döner — câr-mecrûr «وُقُوفًا»ya müteallik.", s=[BI, P("هَا")]),
 T("صَحْبِي", "sahb", "noun", ["fail", "idafa-definiteness", "ya-al-mutakallim"],
   "فَاعِلُ «وُقُوفًا» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ صَاحِبٍ.",
   "The doer of «halting», in raf' by a damma estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term — the plural of صَاحِب.",
   "«وُقُوفًا»nın fâili; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû (mahal, münasebet harekesiyle meşguldür); muzâf, yâ muzâfun ileyh — «صَاحِب»in cem'i.", s=[("صَحْبِ", "sahb", "noun"), P("ي")]),
 T("عَلَيَّ", "ala", "prep", ["huruf-jarr", "ya-al-mutakallim"],
   "عَلَى حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«وُقُوفًا»، أَيْ: لِأَجْلِي أَوْ عَلَى رَأْسِي.", "عَلَى is a jarr letter and the ya is in the seat of jarr — the phrase hangs on «halting»: for my sake, or over my head.", "عَلَى cer harfi, yâ mahallen mecrûr — câr-mecrûr «وُقُوفًا»ya müteallik: benim için ya da başımda.", s=[("عَلَيْ", "ala", "prep"), P("يَ")]),
 T("مَطِيَّهُمْ", "matiyy", "noun", ["maful-bihi", "idafa-definiteness"],
   "مَفْعُولٌ بِهِ لِـ«وُقُوفًا» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْمَطِيُّ: الْمَرَاكِبُ، وَاحِدَتُهَا مَطِيَّةٌ.", "The object of «halting», in nasb by the fatha, annexed; هُمْ is its second term — المَطِيّ: riding-beasts, singular مَطِيَّة.", "«وُقُوفًا»nın mef'ûlü, fetha ile mansûb, muzâf; هُمْ muzâfun ileyh — المَطِيّ: binekler, tekili مَطِيَّة.", HEMI, [("مَطِيَّ", "matiyy", "noun"), P("هُمْ")]),
 T("يَقُولُونَ", "qala", "verb", ["afal-khamsa", "hollow-verbs", "al-hal-jumla-wa-rabituha"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «صَحْبِي».", "A present verb in raf' by keeping its nun — one of the five verbs; the waw is the doer, in the seat of raf' — the clause is a hal of «my companions», in the seat of nasb.", "Ef'âl-i hamseden olduğu için nûnun sübûtuyla merfû muzâri; vâv fâil, mahallen merfû — cümle «صَحْبِي»den hâl olarak mahallen mansûb."),
 T("لَا", "la-nahiya", "part", ["la-nahiya", "al-nahy-wa-wujuhuh"], "نَاهِيَةٌ جَازِمَةٌ — وَالنَّهْيُ هُنَا لِلنُّصْحِ وَالْإِرْشَادِ: يَنْهَوْنَهُ عَنِ الْجَزَعِ.", "The prohibitive لَا, which puts the verb in jazm — here the prohibition is counsel: they turn him from despair.", "Cezm eden nehiy lâsı — burada nehiy nasihat ve irşad içindir: onu feryat ve sabırsızlıktan alıkoyarlar."),
 T("تَهْلِكْ", "halaka", "verb", ["la-nahiya", "thulathi-mujarrad-babs"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.", "A present verb in jazm by the prohibitive لَا, its sign the sukun; its doer is the hidden «you» — the clause is what is said, in the seat of nasb.", "Nehiy lâsıyla meczûm muzâri, cezm alâmeti sükûn; fâili vücûben gizli «ente» — cümle mekūlü'l-kavl olarak mahallen mansûb."),
 T("أَسًى", "asan", "noun", ["maful-lah", "ism-maqsur-manqus", "masdar"],
   "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — كَذَا أَعْرَبَهُ الزَّوْزَنِيُّ؛ وَقِيلَ: مَفْعُولٌ مُطْلَقٌ، وَقِيلَ: حَالٌ.", "An object of cause, in nasb by a fatha estimated on the alif that falls before the tanwin — so al-Zawzanī parses it; it is also read as an absolute object, or as a hal.", "Mef'ûlün lieclih; tenvin sebebiyle düşen elif üzerinde takdîrî fetha ile mansûb — Zevzenî böyle i'râb eder; mef'ûlün mutlak ya da hâl olduğu da söylenmiştir."),
 T("وَتَجَمَّلِ", "tajammala", "verb", ["atf-nasaq", "imperative-amr", "al-amr-wa-wujuhuh", "form-v-verbs", "al-qafiya"],
   "الْوَاوُ عَاطِفَةٌ، وَتَجَمَّلِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْأَمْرُ لِلنُّصْحِ وَالْإِرْشَادِ: يَأْمُرُونَهُ بِالصَّبْرِ.", "The waw conjoins; تَجَمَّلِ is an imperative built on sukun, voweled with kasra for the rhyme, with the hidden «you» as doer — the command is counsel: they bid him be patient.", "Vâv atıf; تَجَمَّلِ sükûn üzere mebnî emir, kafiye için kesre ile harekelenmiş; fâili vücûben gizli «ente» — emir nasihat ve irşad içindir: ona sabrı emrederler.", ".", [WA, ("تَجَمَّلِ", "tajammala", "verb")]),
])
V(S2, 6, "My cure is a tear poured out — yet is there, by a worn-out trace, anything to lean on?",
  "Benim şifam, dökülen bir gözyaşıdır; ama silinmiş bir izin yanında dayanılacak bir şey var mı ki?", [
 T("وَإِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "The waw opens a new sentence; إِنَّ is the particle of emphasis and nasb.", "Vâv istînâfiyye; إِنَّ tekit ve nasb harfi.", s=[WA, ("إِنَّ", "inna", "part")]),
 T("شِفَائِي", "shifa", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "ya-al-mutakallim", "ism-mamdud"],
   "اسْمُ إِنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The noun of إِنَّ, in nasb by a fatha estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term.", "İnne'nin ismi; mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb; muzâf, yâ muzâfun ileyh.", s=[("شِفَائِ", "shifa", "noun"), P("ي")]),
 T("عَبْرَةٌ", "abra", "noun", ["inna-wa-akhawatuha"], "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ — الْعَبْرَةُ: الدَّمْعُ.", "The predicate of إِنَّ, in raf' by the damma — العَبْرَة: tears.", "İnne'nin haberi, damme ile merfû — العَبْرَة: gözyaşı."),
 T("مُهَرَاقَةٌ", "muharaq", "noun", ["naat-sifa", "ism-maful"], "نَعْتٌ لِـ«عَبْرَةٌ» مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ مَفْعُولٍ مِنْ «هَرَاقَ» لُغَةٌ فِي «أَرَاقَ»: مَصْبُوبَةٌ.", "An adjective of «a tear», in raf' by the damma — the ism maf'ul of هَرَاقَ, a dialect form of أَرَاقَ: poured out.", "«عَبْرَةٌ»in na'tı, damme ile merfû — «أَرَاقَ»nın bir lügati olan «هَرَاقَ»dan ism-i mef'ûl: dökülmüş.", HEMI),
 T("فَهَلْ", "hal-istifham", "part", ["al-istifham", "khuruj-al-istifham"],
   "الْفَاءُ عَاطِفَةٌ، وَهَلْ حَرْفُ اسْتِفْهَامٍ خَرَجَ إِلَى مَعْنَى الْإِنْكَارِ وَالنَّفْيِ، أَيْ: لَا مُعَوَّلَ عِنْدَ رَسْمٍ دَارِسٍ.", "The fa conjoins; هَلْ is a particle of question that here means denial: there is nothing to lean on by a worn-out trace.", "Fâ atıf; هَلْ istifham harfi, burada inkâr ve nefy mânâsına çıkmıştır: silinmiş bir izin yanında dayanak yoktur.", s=[FA, ("هَلْ", "hal-istifham", "part")]),
 T("عِنْدَ", "inda", "noun", ["maful-fih", "idafa-definiteness", "taqdim-al-musnad"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.", "An adverb of place, in nasb by the fatha, annexed — it hangs on an omitted predicate, set first.", "Mekân zarfı, fetha ile mansûb, muzâf — öne geçmiş mahzûf habere müteallik."),
 T("رَسْمٍ", "rasm", "noun", ["idafa-definiteness"], MI[0] + ".", MI[1] + ".", MI[2] + "."),
 T("دَارِسٍ", "daris", "noun", ["naat-sifa", "ism-fail"], "نَعْتٌ لِـ«رَسْمٍ» مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ فَاعِلٍ مِنْ «دَرَسَ»: عَفَا وَانْمَحَى.", "An adjective of «a trace», in jarr by the kasra — the ism fa'il of دَرَسَ: to be effaced.", "«رَسْمٍ»in na'tı, kesre ile mecrûr — «دَرَسَ»den ism-i fâil: silinip yok olmak."),
 HARF_JARR("مِنْ", "min", " زَائِدٌ لِتَوْكِيدِ النَّفْيِ وَاسْتِغْرَاقِهِ", " — added, to make the denial total", " — zâid; nefyi pekiştirir ve kuşatıcı kılar"),
 T("مُعَوَّلِ", "muawwal-reliance", "noun", ["mubtada-khabar", "al-qafiya"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ — الْمُعَوَّلُ: الْمُعْتَمَدُ وَالْمُتَّكَلُ عَلَيْهِ، وَقِيلَ: الْمَبْكَى.", "The mubtada, placed last, in raf' by a damma that the added jarr letter's kasra keeps from showing — المُعَوَّل: what one relies on; it is also read as «a place for weeping».", "Sona bırakılmış mübteda; zâid cer harfinin harekesi mahalli meşgul ettiği için takdîrî damme ile merfû — المُعَوَّل: dayanılan, güvenilen şey; «ağlanacak yer» de denmiştir.", "؟"),
])

# =====================================================================================================================
# Compact builders for the plain cases of verses 7 onward — the same wording as the lines above, said once
# =====================================================================================================================
def J(*parts):
    """join (ar, en, tr) pieces into one iʿrāb line and close it with a full stop"""
    return tuple("".join(x[i] for x in parts) + "." for i in range(3))
def Dn(ar, en, tr): return (" — " + ar, " — " + en, " — " + tr)                       # a note after the dash
def W(full, lex, pos, g, line, p=None, s=None): return T(full, lex, pos, g, line[0], line[1], line[2], p, s)
FAILR = ("فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ", "The doer, in raf' by the damma", "Fâil, damme ile merfû")
MAFR = ("مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "The direct object, in nasb by the fatha", "Mef'ûlün bih, fetha ile mansûb")
MAJR = ("مَجْرُورٌ بِالْكَسْرَةِ", "In jarr by the kasra", "Kesre ile mecrûr")
MAJR_A = ("مَجْرُورٌ " + MAQSUR_J, "In jarr by a kasra estimated on the alif", "Elif üzerinde takdîrî kesre ile mecrûr")
MUD = ("، مُضَافٌ", ", annexed", ", muzâf")
MADI = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ", "A past verb built on fatha", "Fetha üzere mebnî mâzî")
MADI_F = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "A past verb built on fatha; the ta marks the feminine", "Fetha üzere mebnî mâzî; tâ te'nîs için")
MADI_TU = ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ", "A past verb built on sukun because the doer's ta is attached; the ta is the doer, in the seat of raf'", "Fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, mahallen merfû")
MUDR = ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ", "A present verb in raf' by the damma", "Damme ile merfû muzâri")
_PRN = {"هُ": ("الْهَاءُ", "the هُ", "«hû»"), "هِ": ("الْهَاءُ", "the هِ", "«hî»"), "هَا": ("هَا", "هَا", "هَا"), "ي": ("الْيَاءُ", "the ya", "yâ"), "يَ": ("الْيَاءُ", "the ya", "yâ"),
        "كَ": ("الْكَافُ", "the kaf", "kâf"), "كِ": ("الْكَافُ", "the kaf", "kâf"), "هُمَا": ("هُمَا", "هُمَا", "هُمَا"), "هِمَا": ("هِمَا", "هِمَا", "هِمَا"), "نَا": ("نَا", "نَا", "نَا"),
        "هُمْ": ("هُمْ", "هُمْ", "هُمْ"), "هُنَّ": ("هُنَّ", "هُنَّ", "هُنَّ"), "هِنَّ": ("هِنَّ", "هِنَّ", "هِنَّ")}
def IDF(pr):
    """…, annexed, and the attached pronoun is its second term"""
    a, e, t = _PRN[pr]
    return ("، مُضَافٌ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" % a, ", annexed; %s is its second term" % e, ", muzâf; %s muzâfun ileyh" % t)
def YA_EST(case_ar, case_en, case_tr):
    """a noun annexed to the speaker's ya: its case vowel is estimated"""
    return ("%s مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ %s، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ" % (case_ar, YA_MUQ),
            "%s estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term" % case_en,
            "mütekellim yâsından önceki harf üzerinde takdîrî %s; muzâf, yâ muzâfun ileyh" % case_tr)
def HID(who_ar, who_en, who_tr, ref=None):
    """the hidden doer; ref = (ar, en, tr) of what it returns to"""
    if ref: return ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: %s يَعُودُ عَلَى %s" % (who_ar, ref[0]), "; its doer is a hidden pronoun returning to %s" % ref[1], "; fâili %s dönen gizli zamir" % ref[2])
    # only the first and second persons (أَنَا، نَحْنُ، أَنْتَ) hide OBLIGATORILY; the hidden هُوَ / هِيَ of an ordinary verb hides optionally (second reader's fix)
    w = N(who_ar) in (N("أَنَا"), N("نَحْنُ"), N("أَنْتَ"))
    return ("، وَالْفَاعِلُ مُسْتَتِرٌ %sتَقْدِيرُهُ: %s" % ("وُجُوبًا " if w else "", who_ar), "; its doer is the hidden «%s»" % who_en, "; fâili %sgizli «%s»" % ("vücûben " if w else "", who_tr))
def TA(word, en, tr_suffix):
    """the jarr phrase hangs on «word»"""
    return ("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«%s»" % word, "; the phrase hangs on «%s»" % en, "; câr-mecrûr «%s»%s müteallik" % (word, tr_suffix))
def PRE(kind, word):
    """a conjunction fused to the word: kind = wa / fa / wa-ist / fa-ist / wa-hal"""
    a, e, t = {"wa": ("الْوَاوُ عَاطِفَةٌ، وَ", "The waw conjoins; ", "Vâv atıf; "), "fa": ("الْفَاءُ عَاطِفَةٌ، وَ", "The fa conjoins; ", "Fâ atıf; "),
               "wa-ist": ("الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ", "The waw opens a new sentence; ", "Vâv istînâfiyye; "), "fa-ist": ("الْفَاءُ اسْتِئْنَافِيَّةٌ، وَ", "The fa opens a new sentence; ", "Fâ istînâfiyye; "),
               "wa-hal": ("الْوَاوُ وَاوُ الْحَالِ، وَ", "The waw is the waw of the hal; ", "Vâv hâliye; ")}[kind]
    return (a + word + " ", e + word + " is ", t + word + " ")
def lo(tr3):
    """the same role wording, to follow a PRE(): lower-case openings in English and Turkish"""
    f = lambda x: {"A ": "a ", "An ": "an ", "The ": "the ", "In ": "in "}.get(x.split(" ")[0] + " ", x.split(" ")[0] + " ") + x.split(" ", 1)[1]
    g = lambda x: (x[0].lower() if x[0] not in "İI" else {"İ": "i", "I": "ı"}[x[0]]) + x[1:]
    return (tr3[0], f(tr3[1]), g(tr3[2]))
IDHA = ("ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ شَرْطِهِ", "An adverb for time to come that carries the sense of a condition, built on sukun in the seat of nasb and annexed to its condition clause", "Şart mânâsı taşıyan gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf")

# =====================================================================================================================
# Days remembered — the day at Dārat Juljul: verses 7–12
# =====================================================================================================================
V(None, 7, "Your way with her is as your way was, before her, with Umm al-Ḥuwayrith and her neighbour Umm al-Rabāb at Maʾsal.",
  "(Bu kadınla) hâlin, ondan önce Ümmü'l-Huveyris ve komşusu Ümmü'r-Rebâb ile Me'sel'deki hâlin gibidir.", [
 T("كَدَأْبِكَ", "dab", "noun", ["huruf-jarr", "idafa-definiteness", "masdar", "hadhf-wa-taqdir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih", "iltifat", "tajrid"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَدَأْبِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ، وَالتَّقْدِيرُ: عَادَتُكَ فِي حُبِّ هٰذِهِ كَعَادَتِكَ مِنْ تَيْنِكَ؛ وَقِيلَ: مُتَعَلِّقَانِ بِـ«قِفَا نَبْكِ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ حَالُهُ مَعَ هٰذِهِ، وَالْمُشَبَّهُ بِهِ حَالُهُ مَعَ أُمِّ الْحُوَيْرِثِ وَأُمِّ الرَّبَابِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ قِلَّةُ الْحَظِّ مِنَ الْوِصَالِ وَمُعَانَاةُ الْوَجْدِ. وَفِيهِ الْتِفَاتٌ مِنَ التَّكَلُّمِ فِي «شِفَائِي» إِلَى الْخِطَابِ، وَالْمُخَاطَبُ نَفْسُهُ عَلَى طَرِيقِ التَّجْرِيدِ.",
   "The kaf is a jarr letter of likening; دَأْبِ is in jarr by the kasra, annexed, and the kaf after it is its second term — the masdar annexed to its doer. The phrase hangs on the omitted predicate of an omitted mubtada: «your way in loving this one is like your way with those two» (so al-Zawzanī explains it); it is also hung on «halt, let us weep». A tashbih mursal mujmal: the thing likened is his state with this woman, the thing it is likened to is his state with Umm al-Ḥuwayrith and Umm al-Rabāb, the particle is the kaf, and the point of likeness is left unsaid — little share of union and much suffering of passion. And there is an iltifāt, from the first person of «my cure» to the second: the one addressed is himself, by way of tajrīd.",
   "Kâf teşbih bildiren cer harfi; دَأْبِ kesre ile mecrûr, muzâf; ondan sonraki kâf muzâfun ileyh — masdarın fâiline izâfeti. Câr-mecrûr, mahzûf bir mübtedanın mahzûf haberine müteallik; takdiri: «bu kadını sevmedeki âdetin, o ikisiyle olan âdetin gibidir» (Zevzenî böyle açıklar); «قِفَا نَبْكِ»ye bağlandığı da söylenmiştir. Teşbih-i mürsel mücmeldir: müşebbeh bu kadınla hâli, müşebbehün bih Ümmü'l-Huveyris ve Ümmü'r-Rebâb ile hâli, edat kâf; vech-i şebeh mahzûftur: vuslattan nasibin azlığı ve aşk acısı çekmek. Ayrıca «شِفَائِي»deki tekellümden hitaba iltifât vardır; muhatap, tecrîd yoluyla kendisidir.", s=[KA, ("دَأْبِ", "dab", "noun"), P("كَ")]),
 HARF_JARR("مِنْ", "min"),
 W("أُمِّ", "umm", "noun", ["huruf-jarr", "idafa-definiteness"], J(MAJR, MUD, TA("دَأْبِ", "your way", "e"))),
 W("الْحُوَيْرِثِ", "huwayrith", "propn", ["idafa-definiteness"], J(MI, Dn("«أُمُّ الْحُوَيْرِثِ» كُنْيَةُ امْرَأَةٍ", "«Umm al-Ḥuwayrith» is a woman's kunya", "«Ümmü'l-Huveyris» bir kadının künyesidir"))),
 T("قَبْلَهَا", "qabla", "noun", ["maful-fih", "idafa-definiteness", "hal"],
   "ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ مِنْ «أُمِّ الْحُوَيْرِثِ»، أَيْ: قَبْلَ هٰذِهِ الَّتِي شُغِفَ بِهَا الْآنَ.",
   "An adverb of time, in nasb by the fatha, annexed; هَا is its second term — it hangs on an omitted hal of «Umm al-Ḥuwayrith»: before this woman who has now taken his heart.",
   "Zaman zarfı, fetha ile mansûb, muzâf; هَا muzâfun ileyh — «أُمِّ الْحُوَيْرِثِ»ten mahzûf hâle müteallik: şimdi gönlünü kaptırdığı bu kadından önce.", HEMI, [("قَبْلَ", "qabla", "noun"), P("هَا")]),
 W("وَجَارَتِهَا", "jara-neighbour", "noun", ["atf-nasaq", "idafa-definiteness"], J(PRE("wa", "جَارَتِ"), ("مَعْطُوفٌ عَلَى «أُمِّ» مَجْرُورٌ بِالْكَسْرَةِ", "conjoined to «Umm», in jarr by the kasra", "«أُمِّ»e ma'tûf, kesre ile mecrûr"), IDF("هَا")), s=[WA, ("جَارَتِ", "jara-neighbour", "noun"), P("هَا")]),
 W("أُمِّ", "umm", "noun", ["badal", "idafa-definiteness"], J(("بَدَلٌ مِنْ «جَارَتِهَا» أَوْ عَطْفُ بَيَانٍ مَجْرُورٌ بِالْكَسْرَةِ", "A badal of «her neighbour», or its explanatory apposition, in jarr by the kasra", "«جَارَتِهَا»dan bedel ya da atf-ı beyân, kesre ile mecrûr"), MUD)),
 W("الرَّبَابِ", "rabab", "propn", ["idafa-definiteness"], J(MI)),
 T("بِمَأْسَلِ", "masal", "propn", ["huruf-jarr", "hal", "al-qafiya"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَمَأْسَلِ مَجْرُورٌ بِالْكَسْرَةِ" + QAFIYA[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «أُمِّ الرَّبَابِ»؛ مَأْسَلٌ بِفَتْحِ السِّينِ: جَبَلٌ بِعَيْنِهِ.",
   "The ba is a jarr letter meaning «in»; مَأْسَلِ is in jarr by the kasra" + QAFIYA[1] + " — the phrase hangs on an omitted hal of «Umm al-Rabāb»; Maʾsal, with a fatha on the sin, is a particular mountain.",
   "Bâ «-de» anlamında cer harfi; مَأْسَلِ kesre ile mecrûr" + QAFIYA[2] + " — câr-mecrûr «أُمِّ الرَّبَابِ»dan mahzûf hâle müteallik; sîn'in fethasıyla Me'sel belirli bir dağdır.", ".", [BI, ("مَأْسَلِ", "masal", "propn")]),
])
V(None, 8, "When the two of them rose, the musk spread from them — like the breath of the east wind when it has come bearing the scent of cloves.",
  "İkisi kalktığında onlardan misk kokusu yayılırdı; tıpkı karanfil kokusunu getirmiş sabâ rüzgârının esintisi gibi.", [
 W("إِذَا", "idha", "part", ["maful-fih", "idha-shartiyya"], J(IDHA, Dn("مُتَعَلِّقٌ بِجَوَابِهِ «تَضَوَّعَ»", "it hangs on its answer, «spread»", "cevabı olan «تَضَوَّعَ»ya müteallik"))),
 T("قَامَتَا", "qama", "verb", ["hollow-verbs", "al-muthanna", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ وَحُرِّكَتْ بِالْفَتْحِ لِمُنَاسَبَةِ الْأَلِفِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ يَعُودُ عَلَى أُمِّ الْحُوَيْرِثِ وَأُمِّ الرَّبَابِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "A past verb built on fatha; the ta marks the feminine and takes a fatha before the alif; the alif of the dual is the doer, in the seat of raf' — Umm al-Ḥuwayrith and Umm al-Rabāb. The clause is in the seat of jarr, annexed to إِذَا.",
   "Fetha üzere mebnî mâzî; tâ te'nîs için olup eliften dolayı fethalanmıştır; tesniye elifi fâil, mahallen merfû — Ümmü'l-Huveyris ile Ümmü'r-Rebâb'a döner. Cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr."),
 W("تَضَوَّعَ", "tadawwaa", "verb", ["form-v-verbs", "idha-shartiyya"], J(MADI, Dn("وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ تَضَوَّعَ الطِّيبُ: انْتَشَرَتْ رَائِحَتُهُ", "the clause answers إِذَا and has no seat; تَضَوَّعَ of a scent: it spread abroad", "cümle «إِذَا»nın cevabıdır, i'râbdan mahalli yoktur; kokunun «تَضَوَّعَ»sı: etrafa yayılması"))),
 W("الْمِسْكُ", "misk", "noun", ["fail"], J(FAILR)),
 T("مِنْهُمَا", "min", "prep", ["huruf-jarr"],
   "مِنْ حَرْفُ جَرٍّ، وَهُمَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَضَوَّعَ»، وَيَجُوزُ تَعْلِيقُهُمَا بِمَحْذُوفٍ حَالٍ مِنَ «الْمِسْكُ».",
   "مِنْ is a jarr letter and هُمَا is in the seat of jarr — the phrase hangs on «spread», or on an omitted hal of «the musk».",
   "مِنْ cer harfi, هُمَا mahallen mecrûr — câr-mecrûr «تَضَوَّعَ»ya müteallik; «الْمِسْكُ»ten mahzûf hâle bağlanması da câizdir.", HEMI, [("مِنْ", "min", "prep"), P("هُمَا")]),
 T("نَسِيمَ", "nasim", "noun", ["maful-mutlaq", "idafa-definiteness", "hadhf-wa-taqdir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالْأَصْلُ: تَضَوُّعًا مِثْلَ تَضَوُّعِ نَسِيمِ الصَّبَا، فَحُذِفَ الْمَصْدَرُ وَصِفَتُهُ وَأُقِيمَ الْمُضَافُ إِلَيْهِ مَقَامَهُ. وَفِيهِ تَشْبِيهٌ بَلِيغٌ حُذِفَتْ أَدَاتُهُ وَوَجْهُهُ: شَبَّهَ طِيبَ رَيَّاهُمَا بِطِيبِ نَسِيمٍ هَبَّ عَلَى قَرَنْفُلٍ وَأَتَى بِرَيَّاهُ.",
   "It stands in for the absolute object, in nasb by the fatha, annexed — the full wording is «a spreading like that of the breath of the east wind»: the masdar and its adjective are dropped and the annexed noun is set in their place. A tashbih balīgh, with neither particle nor point of likeness: the sweetness of their scent is likened to the sweetness of a breeze that has blown over cloves and brought their fragrance (al-Zawzanī).",
   "Mef'ûlün mutlakın nâibi, fetha ile mansûb, muzâf — aslı: «sabâ esintisinin yayılışı gibi bir yayılışla»; masdar ve sıfatı hazfedilmiş, muzâfun ileyh onların yerine konmuştur. Edatı ve vechi hazfedilmiş teşbih-i belîğ vardır: ikisinin kokusunun güzelliği, karanfil üzerinden esip onun kokusunu getiren esintinin güzelliğine benzetilmiştir (Zevzenî)."),
 W("الصَّبَا", "saba-wind", "noun", ["idafa-definiteness", "ism-maqsur-manqus"], J(("مُضَافٌ إِلَيْهِ مَجْرُورٌ " + MAQSUR_J, "The second term of the idafa, in jarr by a kasra estimated on the alif", "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr"), Dn("الصَّبَا: الرِّيحُ الشَّرْقِيَّةُ", "الصَّبَا: the east wind", "الصَّبَا: doğudan esen rüzgâr"))),
 T("جَاءَتْ", "jaa", "verb", ["hollow-verbs", "al-hal-jumla-wa-rabituha"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «الصَّبَا» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهَا بِتَقْدِيرِ «قَدْ»، وَيَجُوزُ أَنْ تَكُونَ نَعْتًا لَهَا إِنْ كَانَتْ «أَلْ» لِلْجِنْسِ.",
   "A past verb built on fatha; the ta marks the feminine, and the doer is a hidden «she» returning to «the east wind» — the clause is a hal of it, in the seat of nasb, with قَدْ understood; it may also be an adjective of it, if the article is the article of the kind.",
   "Fetha üzere mebnî mâzî; tâ te'nîs için, fâili «الصَّبَا»ya dönen gizli «hiye» — cümle, «قَدْ» takdiriyle ondan hâl olarak mahallen mansûb; «أَلْ» cins için ise na't olması da câizdir."),
 T("بِرَيَّا", "rayya", "noun", ["huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَرَيَّا مَجْرُورٌ " + MAQSUR_J + "، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَاءَتْ»؛ الرَّيَّا: الرَّائِحَةُ الطَّيِّبَةُ.",
   "The ba is a jarr letter; رَيَّا is in jarr by a kasra estimated on the alif, annexed — the phrase hangs on «has come»; الرَّيَّا: a sweet scent.",
   "Bâ cer harfi; رَيَّا elif üzerinde takdîrî kesre ile mecrûr, muzâf — câr-mecrûr «جَاءَتْ»e müteallik; الرَّيَّا: güzel koku.", s=[BI, ("رَيَّا", "rayya", "noun")]),
 W("الْقَرَنْفُلِ", "qaranful", "noun", ["idafa-definiteness", "al-qafiya"], J(MI), "."),
])
V(None, 9, "So the tears of my eye overflowed for longing, down upon my breast, until my tears wet my sword-belt.",
  "Bunun üzerine gözümün yaşları özlemden göğsümün üstüne doğru taştı; öyle ki gözyaşım kılıcımın hamailini ıslattı.", [
 W("فَفَاضَتْ", "fada", "verb", ["atf-nasaq", "hollow-verbs"], J(("الْفَاءُ عَاطِفَةٌ تُفِيدُ السَّبَبِيَّةَ، وَفَاضَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ", "The fa conjoins, with the sense of cause; فَاضَتْ is a past verb built on fatha, and the ta marks the feminine", "Fâ sebebiyet bildiren atıf; فَاضَتْ fetha üzere mebnî mâzî, tâ te'nîs için"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جَوَابِ «إِذَا» فِي الْبَيْتِ قَبْلَهُ", "the clause is conjoined to the answer of إِذَا in the verse before", "cümle önceki beyitteki «إِذَا»nın cevabına ma'tûftur")), s=[FA, ("فَاضَتْ", "fada", "verb")]),
 W("دُمُوعُ", "dam-tear", "noun", ["fail", "idafa-definiteness", "jam-taksir"], J(FAILR, MUD, Dn("جَمْعُ دَمْعٍ", "the plural of دَمْع", "«دَمْع»in cem'i"))),
 W("الْعَيْنِ", "ayn-eye", "noun", ["idafa-definiteness"], J(MI)),
 T("مِنِّي", "min", "prep", ["huruf-jarr", "ya-al-mutakallim"],
   "مِنْ حَرْفُ جَرٍّ، وَالنُّونُ الثَّانِيَةُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«فَاضَتْ»، وَيَجُوزُ تَعْلِيقُهُمَا بِمَحْذُوفٍ حَالٍ مِنْ «دُمُوعُ الْعَيْنِ».",
   "مِنْ is a jarr letter, the second nun guards it, and the ya is in the seat of jarr — the phrase hangs on «overflowed», or on an omitted hal of «the tears of the eye».",
   "مِنْ cer harfi, ikinci nûn vikâye için, yâ mahallen mecrûr — câr-mecrûr «فَاضَتْ»e müteallik; «دُمُوعُ الْعَيْنِ»den mahzûf hâle bağlanması da câizdir.", s=[("مِنِّ", "min", "prep"), P("ي")]),
 T("صَبَابَةً", "sababa", "noun", ["maful-lah", "masdar"],
   "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — كَذَا أَعْرَبَهُ الزَّوْزَنِيُّ، أَيْ: فَاضَتْ لِلصَّبَابَةِ؛ وَقِيلَ: مَفْعُولٌ مُطْلَقٌ، وَقِيلَ: مَصْدَرٌ فِي مَوْضِعِ الْحَالِ. الصَّبَابَةُ: رِقَّةُ الشَّوْقِ.",
   "An object of cause, in nasb by the fatha — so al-Zawzanī parses it: «they overflowed out of longing»; it is also read as an absolute object, or as a masdar standing as a hal. الصَّبَابَة: the tenderness of longing.",
   "Mef'ûlün lieclih, fetha ile mansûb — Zevzenî böyle i'râb eder: «özlem sebebiyle taştı»; mef'ûlün mutlak ya da hâl yerinde masdar olduğu da söylenmiştir. الصَّبَابَة: özlemin inceliği, yanık hasret.", HEMI),
 HARF_JARR("عَلَى", "ala"),
 W("النَّحْرِ", "nahr-chest", "noun", ["huruf-jarr"], J(MAJR, TA("فَاضَتْ", "overflowed", "e"), Dn("النَّحْرُ: أَعْلَى الصَّدْرِ، مَوْضِعُ الْقِلَادَةِ", "النَّحْر: the top of the breast, where a necklace lies", "النَّحْر: göğsün üst kısmı, gerdanlığın durduğu yer"))),
 T("حَتَّى", "hatta", "part", ["huruf-jarr"],
   "حَرْفُ غَايَةٍ وَجَرٍّ، وَبَعْدَهُ «أَنْ» مُضْمَرَةٌ؛ وَقِيلَ: حَرْفُ ابْتِدَاءٍ وَالْجُمْلَةُ بَعْدَهُ مُسْتَأْنَفَةٌ.",
   "A jarr letter of the end-point, with an أَنْ understood after it; it is also read as a particle of beginning, the clause after it being a fresh sentence.",
   "Gaye bildiren cer harfi; ardında «أَنْ» gizlidir; ibtidâ harfi olup sonraki cümlenin müste'nefe olduğu da söylenmiştir."),
 W("بَلَّ", "balla", "verb", ["thulathi-mujarrad-babs", "doubled-verbs", "an-masdariyya"], J(MADI, Dn("وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنْ» الْمُضْمَرَةِ وَالْفِعْلِ مَجْرُورٌ بِحَتَّى، مُتَعَلِّقٌ بِـ«فَاضَتْ»", "the masdar made by the understood أَنْ and the verb is in jarr by حَتَّى and hangs on «overflowed»", "gizli «أَنْ» ile fiilden oluşan müevvel masdar hattâ ile mecrûr olup «فَاضَتْ»e mütealliktir"))),
 W("دَمْعِيَ", "dam-tear", "noun", ["fail", "idafa-definiteness", "ya-al-mutakallim"], J(("فَاعِلٌ مَرْفُوعٌ ", "The doer, in raf' by ", "Fâil; "), YA_EST("بِضَمَّةٍ", "a damma", "damme ile merfû")), s=[("دَمْعِ", "dam-tear", "noun"), P("يَ")]),
 W("مِحْمَلِي", "mihmal", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "al-qafiya"], J(("مَفْعُولٌ بِهِ مَنْصُوبٌ ", "The direct object, in nasb by ", "Mef'ûlün bih; "), YA_EST("بِفَتْحَةٍ", "a fatha", "fetha ile mansûb"), Dn("الْمِحْمَلُ: حِمَالَةُ السَّيْفِ", "المِحْمَل: the belt a sword hangs from", "المِحْمَل: kılıcın asıldığı kayış, hamail")), ".", [("مِحْمَلِ", "mihmal", "noun"), P("ي")]),
])
V(None, 10, "Yes — many a fine day you have had of them; and none like a day at Dārat Juljul.",
  "Evet, onlardan yana nice güzel günün oldu; hele Dâretü Cülcül'deki bir gün gibisi yoktur.", [
 T("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ.", "A particle of opening and alerting.", "İstiftâh ve tenbih harfi."),
 T("رُبَّ", "rubba", "part", ["al-lam-wa-rubba-fil-kafiya", "huruf-jarr"],
   "حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ لَا يَتَعَلَّقُ بِشَيْءٍ، وَهُوَ هُنَا لِلتَّكْثِيرِ.",
   "A near-redundant jarr letter that hangs on nothing; here it means «many a…».",
   "Zâide benzeyen, hiçbir şeye müteallik olmayan cer harfi; burada teksîr («nice») bildirir."),
 T("يَوْمٍ", "yawm", "noun", ["al-lam-wa-rubba-fil-kafiya", "mubtada-khabar", "hadhf-wa-taqdir"],
   "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ — وَخَبَرُهُ مَحْذُوفٌ تَقْدِيرُهُ: مَوْجُودٌ.",
   "The mubtada, in raf' by a damma that the kasra of the near-redundant jarr letter keeps from showing — its predicate is left out: «there is».",
   "Mübteda; zâide benzeyen cer harfinin harekesi mahalli meşgul ettiği için takdîrî damme ile merfû — haberi mahzûftur, takdiri: «vardır»."),
 T("لَكَ", "li", "prep", ["huruf-jarr", "naat-sifa", "tajrid"],
   "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«يَوْمٍ»، وَيَجُوزُ تَعْلِيقُهُمَا بِـ«صَالِحٍ»؛ وَالْخِطَابُ لِنَفْسِهِ عَلَى التَّجْرِيدِ.",
   "The lam is a jarr letter and the kaf is in the seat of jarr — the phrase hangs on an omitted adjective of «a day», or on «fine»; he is still speaking to himself (tajrīd).",
   "Lâm cer harfi, kâf mahallen mecrûr — câr-mecrûr «يَوْمٍ»in mahzûf na'tına müteallik; «صَالِحٍ»e bağlanması da câizdir; hitap, tecrîd yoluyla kendisinedir.", s=[("لَ", "li", "prep"), P("كَ")]),
 T("مِنْهُنَّ", "min", "prep", ["huruf-jarr", "hal"],
   "مِنْ حَرْفُ جَرٍّ، وَهُنَّ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى النِّسَاءِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الضَّمِيرِ الْمُسْتَقِرِّ فِي «لَكَ».",
   "مِنْ is a jarr letter and هُنَّ is in the seat of jarr, returning to the women — the phrase hangs on an omitted hal of the pronoun lodged in «for you».",
   "مِنْ cer harfi, هُنَّ mahallen mecrûr, kadınlara döner — câr-mecrûr «لَكَ»deki müstekar zamirden mahzûf hâle müteallik.", s=[("مِنْ", "min", "prep"), P("هُنَّ")]),
 W("صَالِحٍ", "salih-fit", "noun", ["naat-sifa", "ism-fail"], J(("نَعْتٌ لِـ«يَوْمٍ» مَجْرُورٌ بِالْكَسْرَةِ تَبَعًا لِلَّفْظِ", "An adjective of «a day», in jarr by the kasra after the wording", "«يَوْمٍ»in na'tı, lafza tâbi olarak kesre ile mecrûr")), HEMI),
 T("وَلَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "anwa-al-waw"], "الْوَاوُ اعْتِرَاضِيَّةٌ، وَقِيلَ: حَالِيَّةٌ أَوِ اسْتِئْنَافِيَّةٌ، وَلَا نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.", "The waw is parenthetical — or, it is said, the waw of the hal or of a new start; لَا denies the whole kind and governs as إِنَّ does.", "Vâv i'tirâziyye — hâliye yahut istînâfiyye olduğu da söylenmiştir; lâ cinsi nefyeder, inne gibi amel eder.", s=[WA, ("لَا", "la-nafiya-lil-jins", "part")]),
 T("سِيَّمَا", "siyy", "noun", ["la-nafiya-lil-jins", "idafa-definiteness", "anwa-ma", "hadhf-wa-taqdir"],
   "سِيَّ اسْمُ لَا مَنْصُوبٌ بِالْفَتْحَةِ لِأَنَّهُ مُضَافٌ، وَمَا زَائِدَةٌ، وَخَبَرُ لَا مَحْذُوفٌ تَقْدِيرُهُ: مَوْجُودٌ — السِّيُّ: الْمِثْلُ، أَيْ: وَلَا مِثْلَ يَوْمٍ. قَالَ الزَّوْزَنِيُّ: أَفَادَتْ «لَا سِيَّمَا» التَّفْضِيلَ وَالتَّخْصِيصَ.",
   "سِيَّ is the noun of لَا, in nasb by the fatha because it is annexed; مَا is added; the predicate of لَا is left out («there is»). السِّيّ is «the like»: «and there is no like of a day…». Al-Zawzanī: لَا سِيَّمَا gives preference and singling-out.",
   "سِيَّ lâ'nın ismi, muzâf olduğu için fetha ile mansûb; مَا zâid; lâ'nın haberi mahzûftur («vardır»). السِّيّ «benzer» demektir: «…bir günün benzeri yoktur». Zevzenî: «لَا سِيَّمَا» üstün tutma ve tahsis bildirir.", s=[("سِيَّ", "siyy", "noun"), ("مَا", "ma-zaida", "part")]),
 T("يَوْمٍ", "yawm", "noun", ["idafa-definiteness"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَيَجُوزُ رَفْعُهُ عَلَى أَنَّ «مَا» مَوْصُولَةٌ وَهُوَ خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: وَلَا سِيَّ الَّذِي هُوَ يَوْمٌ.",
   "The second term of the idafa, in jarr by the kasra — it may also be read in raf', with مَا as a relative and «a day» the predicate of a mubtada left out: «nor the like of that which is a day…».",
   "Muzâfun ileyh, kesre ile mecrûr — «مَا» mevsûle sayılıp mahzûf mübtedanın haberi olarak ref'i de câizdir: «…bir gün olan şeyin benzeri yoktur»."),
 T("بِدَارَةِ", "dara-pool", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَدَارَةِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«يَوْمٍ».",
   "The ba is a jarr letter meaning «at»; دَارَةِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «a day».",
   "Bâ «-de» anlamında cer harfi; دَارَةِ kesre ile mecrûr, muzâf — câr-mecrûr «يَوْمٍ»in mahzûf na'tına müteallik.", s=[BI, ("دَارَةِ", "dara-pool", "noun")]),
 W("جُلْجُلِ", "juljul", "propn", ["idafa-definiteness", "al-qafiya"], J(MI, QAFIYA, Dn("دَارَةُ جُلْجُلٍ: غَدِيرٌ بِعَيْنِهِ", "Dārat Juljul is a particular pool", "Dâretü Cülcül belirli bir gölcüktür")), "."),
])
V(None, 11, "And the day I slaughtered my riding-camel for the maidens — O the wonder of her saddle and gear, and how it was carried!",
  "Bir de bâkireler için bineğimi kestiğim gün; ah, onun (onlarca) yüklenip taşınan semerine ne kadar şaşılır!", [
 T("وَيَوْمَ", "yawm", "noun", ["atf-nasaq", "idafa-definiteness", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"],
   "الْوَاوُ عَاطِفَةٌ، وَيَوْمَ مَعْطُوفٌ عَلَى «يَوْمٍ» فِي الْبَيْتِ قَبْلَهُ، مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ — بَنَاهُ عَلَى الْفَتْحِ لَمَّا أَضَافَهُ إِلَى مَبْنِيٍّ وَهُوَ الْفِعْلُ الْمَاضِي.",
   "The waw conjoins; يَوْمَ is conjoined to «a day» in the verse before, built on fatha in the seat of jarr — he builds it on fatha because he annexes it to a built word, the past verb (al-Zawzanī).",
   "Vâv atıf; يَوْمَ önceki beyitteki «يَوْمٍ»e ma'tûf, fetha üzere mebnî, mahallen mecrûr — mebnî olan mâzî fiile muzâf kıldığı için onu fetha üzere mebnî yapmıştır (Zevzenî).", s=[WA, ("يَوْمَ", "yawm", "noun")]),
 W("عَقَرْتُ", "aqara", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil"], J(MADI_TU, Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «يَوْمَ» إِلَيْهَا", "the clause is in the seat of jarr, annexed to «the day»", "cümle «يَوْمَ»nin muzâfun ileyhi olarak mahallen mecrûr"))),
 T("لِلْعَذَارَى", "adhra", "noun", ["huruf-jarr", "ism-maqsur-manqus", "jam-taksir"],
   "اللَّامُ حَرْفُ جَرٍّ، وَالْعَذَارَى مَجْرُورٌ " + MAQSUR_J + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«عَقَرْتُ»؛ جَمْعُ عَذْرَاءَ وَهِيَ الْبِكْرُ.",
   "The lam is a jarr letter; الْعَذَارَى is in jarr by a kasra estimated on the alif — the phrase hangs on «I slaughtered»; the plural of عَذْرَاء, a maiden.",
   "Lâm cer harfi; الْعَذَارَى elif üzerinde takdîrî kesre ile mecrûr — câr-mecrûr «عَقَرْتُ»ya müteallik; «عَذْرَاء»nın (bâkire) cem'i.", s=[LI, ("الْعَذَارَى", "adhra", "noun")]),
 W("مَطِيَّتِي", "matiyya", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim"], J(("مَفْعُولٌ بِهِ مَنْصُوبٌ ", "The direct object, in nasb by ", "Mef'ûlün bih; "), YA_EST("بِفَتْحَةٍ", "a fatha", "fetha ile mansûb")), HEMI, [("مَطِيَّتِ", "matiyya", "noun"), P("ي")]),
 T("فَيَا", "ya-nida", "part", ["vocative-munada"], "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَيَا حَرْفُ نِدَاءٍ.", "The fa opens a new sentence; يَا is the vocative particle.", "Fâ istînâfiyye; يَا nidâ harfi.", s=[FA, ("يَا", "ya-nida", "part")]),
 T("عَجَبًا", "ajab", "noun", ["vocative-munada", "ya-al-mutakallim", "masdar"],
   "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ، وَالْأَلِفُ مُنْقَلِبَةٌ عَنْ يَاءِ الْمُتَكَلِّمِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْأَصْلُ: يَا عَجَبِي. وَالنِّدَاءُ هُنَا لِلتَّعَجُّبِ: نَادَى الْعَجَبَ اتِّسَاعًا وَمَجَازًا، كَأَنَّهُ قَالَ: يَا عَجَبِي احْضُرْ فَهٰذَا أَوَانُكَ؛ وَقِيلَ: الْمُنَادَى مَحْذُوفٌ، أَيْ: يَا قَوْمِ اشْهَدُوا عَجَبِي.",
   "An annexed vocative, in nasb by the fatha; the alif stands for the speaker's ya, which is its second term — the original is يَا عَجَبِي. The call here is wonder: he calls on Wonder itself by a figure, as if to say «come, my wonder, this is your hour»; or, it is said, the one called is left out: «O people, witness my wonder» (al-Zawzanī).",
   "Muzâf münâdâ, fetha ile mansûb; elif, muzâfun ileyh olan mütekellim yâsından dönmedir — aslı «يَا عَجَبِي». Nidâ burada taaccüb içindir: hayreti mecaz yoluyla çağırmıştır, sanki «ey hayretim, gel; tam senin vaktin» demiştir; «münâdâ mahzûftur: ey kavim, hayretime şahit olun» da denmiştir (Zevzenî)."),
 HARF_JARR("مِنْ", "min"),
 W("كُورِهَا", "kur", "noun", ["huruf-jarr", "idafa-definiteness"], J(MAJR, IDF("هَا"), TA("عَجَبًا", "wonder", "ya"), Dn("الْكُورُ: الرَّحْلُ بِأَدَاتِهِ", "الكُور: a camel's saddle with its gear", "الكُور: takımlarıyla birlikte deve semeri")), s=[("كُورِ", "kur", "noun"), P("هَا")]),
 T("الْمُتَحَمَّلِ", "mutahammal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
   "نَعْتٌ لِـ«كُورِهَا» مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ مِنْ «تَحَمَّلَ»: الْمَحْمُولُ؛ تَعَجَّبَ مِنْ حَمْلِهِنَّ رَحْلَ مَطِيَّتِهِ بَعْدَ عَقْرِهَا.",
   "An adjective of «her saddle», in jarr by the kasra — the ism maf'ul of تَحَمَّلَ: carried; he wonders at the maidens carrying his camel's saddle after she was slaughtered.",
   "«كُورِهَا»nın na'tı, kesre ile mecrûr — «تَحَمَّلَ»den ism-i mef'ûl: yüklenip taşınan; bineği kesildikten sonra kızların onun semerini taşımasına şaşar.", "!"),
])
V(None, 12, "So the maidens spent the day tossing her meat to one another, and fat like the fringes of twisted white silk.",
  "Bâkireler gün boyu onun etini ve bükülmüş ibrişim saçakları gibi olan yağını birbirlerine atıp durdular.", [
 W("فَظَلَّ", "zalla-remain", "verb", ["atf-nasaq", "kana-wa-akhawatuha", "doubled-verbs"], J(PRE("fa", "ظَلَّ"), ("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "a defective past verb built on fatha", "fetha üzere mebnî nâkıs mâzî"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «عَقَرْتُ»", "the clause is conjoined to «I slaughtered»", "cümle «عَقَرْتُ» cümlesine ma'tûftur")), s=[FA, ("ظَلَّ", "zalla-remain", "verb")]),
 W("الْعَذَارَى", "adhra", "noun", ["kana-wa-akhawatuha", "ism-maqsur-manqus", "jam-taksir"], J(("اسْمُ «ظَلَّ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "The noun of ظَلَّ, in raf' by a damma estimated on the alif", "«ظَلَّ»nin ismi, elif üzerinde takdîrî damme ile merfû"))),
 T("يَرْتَمِينَ", "irtama", "verb", ["form-viii-verbs", "naqis-verbs", "kana-wa-akhawatuha", "al-bariz-al-muttasil"],
   "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «ظَلَّ»؛ يَرْتَمِينَ: يُلْقِي بَعْضُهُنَّ إِلَى بَعْضٍ.",
   "A present verb built on sukun because the women's nun is attached; the nun is the doer, in the seat of raf' — the clause is the predicate of ظَلَّ, in the seat of nasb; يَرْتَمِينَ: they throw to one another.",
   "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî muzâri; nûn fâil, mahallen merfû — cümle «ظَلَّ»nin haberi olarak mahallen mansûb; يَرْتَمِينَ: birbirlerine atarlar."),
 W("بِلَحْمِهَا", "lahm", "noun", ["huruf-jarr", "idafa-definiteness"], J(("الْبَاءُ حَرْفُ جَرٍّ، وَلَحْمِ مَجْرُورٌ بِالْكَسْرَةِ", "The ba is a jarr letter; لَحْمِ is in jarr by the kasra", "Bâ cer harfi; لَحْمِ kesre ile mecrûr"), IDF("هَا"), TA("يَرْتَمِينَ", "tossing", "e")), HEMI, [BI, ("لَحْمِ", "lahm", "noun"), P("هَا")]),
 W("وَشَحْمٍ", "shahm", "noun", ["atf-nasaq"], J(PRE("wa", "شَحْمٍ"), ("مَعْطُوفٌ عَلَى «لَحْمِهَا» مَجْرُورٌ بِالْكَسْرَةِ", "conjoined to «her meat», in jarr by the kasra", "«لَحْمِهَا»ya ma'tûf, kesre ile mecrûr")), s=[WA, ("شَحْمٍ", "shahm", "noun")]),
 T("كَهُدَّابِ", "huddab", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَهُدَّابِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«شَحْمٍ» عَلَى مَا شَرَحَهُ الزَّوْزَنِيُّ؛ وَجَعَلَهُمَا الدُّرَّةُ حَالًا مِنْ «لَحْمِهَا». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ شَحْمُ الْمَطِيَّةِ، وَالْمُشَبَّهُ بِهِ هُدَّابُ الدِّمَقْسِ الْمُفَتَّلِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الْبَيَاضُ وَاللِّينُ.",
   "The kaf is a jarr letter of likening; هُدَّابِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «fat», as al-Zawzanī explains it; al-Durra makes it a hal of «her meat». A tashbih mursal mujmal: the thing likened is the camel's fat, the thing it is likened to is the fringes of twisted silk, the particle is the kaf, and the point of likeness — whiteness and softness — is left unsaid.",
   "Kâf teşbih bildiren cer harfi; هُدَّابِ kesre ile mecrûr, muzâf — câr-mecrûr, Zevzenî'nin şerhine göre «شَحْمٍ»in mahzûf na'tına müteallik; Dürre «لَحْمِهَا»dan hâl sayar. Teşbih-i mürsel mücmeldir: müşebbeh devenin yağı, müşebbehün bih bükülmüş ibrişimin saçakları, edat kâf; vech-i şebeh — beyazlık ve yumuşaklık — mahzûftur.", s=[KA, ("هُدَّابِ", "huddab", "noun")]),
 W("الدِّمَقْسِ", "dimaqs", "noun", ["idafa-definiteness"], J(MI, Dn("الدِّمَقْسُ: الْإِبْرِيسَمُ، وَقِيلَ: الْأَبْيَضُ مِنْهُ خَاصَّةً", "الدِّمَقْس: silk — or, it is said, white silk in particular", "الدِّمَقْس: ibrişim; «özellikle beyazı» da denmiştir"))),
 W("الْمُفَتَّلِ", "mufattal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ لِـ«هُدَّابِ» مَجْرُورٌ بِالْكَسْرَةِ", "An adjective of «fringes», in jarr by the kasra", "«هُدَّابِ»ın na'tı, kesre ile mecrûr"), Dn("الَّذِي أُجِيدَ فَتْلُهُ", "well and tightly twisted", "iyice bükülmüş")), "."),
])

# =====================================================================================================================
# ʿUnayza's howdah: verses 13–18
# =====================================================================================================================
YAWM_ATF = ("الْوَاوُ عَاطِفَةٌ، وَيَوْمَ مَعْطُوفٌ عَلَى «يَوْمَ عَقَرْتُ»، مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ لِإِضَافَتِهِ إِلَى الْجُمْلَةِ الْمَاضَوِيَّةِ بَعْدَهُ.",
            "The waw conjoins; يَوْمَ is conjoined to «the day I slaughtered», built on fatha in the seat of jarr because it is annexed to the past-tense clause after it.",
            "Vâv atıf; يَوْمَ «يَوْمَ عَقَرْتُ»ya ma'tûf; sonraki mâzî cümleye muzâf olduğu için fetha üzere mebnî, mahallen mecrûr.")
V(None, 13, "And the day I entered the howdah — ʿUnayza's howdah — and she said: «Woe to you! You will make me go on foot.»",
  "Bir de mahfeye, Uneyze'nin mahfesine girdiğim gün; o da «Vay hâline! Beni yaya bırakacaksın» demişti.", [
 T("وَيَوْمَ", "yawm", "noun", ["atf-nasaq", "idafa-definiteness", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya"], YAWM_ATF[0], YAWM_ATF[1], YAWM_ATF[2], s=[WA, ("يَوْمَ", "yawm", "noun")]),
 W("دَخَلْتُ", "dakhala", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil"], J(MADI_TU, Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «يَوْمَ» إِلَيْهَا", "the clause is in the seat of jarr, annexed to «the day»", "cümle «يَوْمَ»nin muzâfun ileyhi olarak mahallen mecrûr"))),
 T("الْخِدْرَ", "khidr", "noun", ["maful-bihi", "hadhf-al-jarr"],
   "مَنْصُوبٌ بِالْفَتْحَةِ عَلَى التَّوَسُّعِ بِإِسْقَاطِ الْخَافِضِ، فَهُوَ مُنْتَصِبٌ انْتِصَابَ الْمَفْعُولِ بِهِ؛ وَبَعْضُهُمْ يَنْصِبُهُ عَلَى الظَّرْفِيَّةِ الْمَكَانِيَّةِ. الْخِدْرُ هُنَا: الْهَوْدَجُ.",
   "In nasb by the fatha by a widening of usage — the jarr letter is dropped, so it stands as a direct object does; some put it in nasb as an adverb of place. الخِدْر here: the howdah, the woman's litter.",
   "Harf-i cerrin düşürülmesiyle, tevessü' yoluyla fetha ile mansûb; mef'ûlün bih gibi nasbedilmiştir; kimileri mekân zarfı olarak nasbeder. الخِدْر burada: mahfe, hevdec."),
 W("خِدْرَ", "khidr", "noun", ["badal", "idafa-definiteness"], J(("بَدَلٌ مِنَ «الْخِدْرَ» بَدَلُ كُلٍّ مِنْ كُلٍّ مَنْصُوبٌ بِالْفَتْحَةِ", "A badal of «the howdah» — the whole for the whole — in nasb by the fatha", "«الْخِدْرَ»den bedel-i küll, fetha ile mansûb"), MUD)),
 T("عُنَيْزَةٍ", "unayza", "propn", ["idafa-definiteness", "mamnu-min-sarf"],
   MI[0] + " — وَصَرَفَهُ لِضَرُورَةِ الشِّعْرِ، وَهُوَ لَا يَنْصَرِفُ فِي غَيْرِ الشِّعْرِ لِلتَّأْنِيثِ وَالتَّعْرِيفِ؛ عُنَيْزَةُ: اسْمُ صَاحِبَتِهِ، وَقِيلَ: لَقَبٌ لَهَا.",
   MI[1] + " — he gives it tanwin as verse allows; outside verse it is a diptote, feminine and definite (al-Zawzanī). ʿUnayza is the name of the woman — or, it is said, a nickname of hers.",
   MI[2] + " — şiir zarûretiyle munsarif kılınmıştır; şiir dışında te'nîs ve ta'rîf sebebiyle gayr-i munsariftir (Zevzenî). Uneyze kadının adıdır; «lakabıdır» da denmiştir.", HEMI),
 W("فَقَالَتْ", "qala", "verb", ["atf-nasaq", "hollow-verbs"], J(PRE("fa", "قَالَتْ"), lo(MADI_F), HID("هِيَ", "she", "hiye", ("عُنَيْزَةَ", "ʿUnayza", "Uneyze'ye")), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «دَخَلْتُ»", "the clause is conjoined to «I entered»", "cümle «دَخَلْتُ» cümlesine ma'tûftur")), s=[FA, ("قَالَتْ", "qala", "verb")]),
 T("لَكَ", "li", "prep", ["huruf-jarr", "taqdim-al-musnad"],
   "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
   "The lam is a jarr letter and the kaf is in the seat of jarr — the phrase hangs on an omitted predicate, set first.",
   "Lâm cer harfi, kâf mahallen mecrûr — câr-mecrûr öne geçmiş mahzûf habere müteallik.", s=[("لَ", "li", "prep"), P("كَ")]),
 T("الْوَيْلَاتُ", "wayla", "noun", ["mubtada-khabar", "jam-muannath-salim", "khabar-fi-mana-al-insha"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ؛ جَمْعُ وَيْلَةٍ، وَهِيَ وَالْوَيْلُ: شِدَّةُ الْعَذَابِ. وَالْجُمْلَةُ خَبَرِيَّةٌ لَفْظًا إِنْشَائِيَّةٌ مَعْنًى: دُعَاءٌ مِنْهَا عَلَيْهِ عِنْدَ أَكْثَرِ النَّاسِ، وَقِيلَ: دُعَاءٌ لَهُ فِي مَعْرِضِ الدُّعَاءِ عَلَيْهِ، كَقَوْلِهِمْ: قَاتَلَهُ اللهُ مَا أَفْصَحَهُ.",
   "The mubtada, placed last, in raf' by the damma — the clause is what she said, in the seat of nasb; the plural of وَيْلَة, which like وَيْل is «sore torment». A statement in form and a wish in meaning: for most it is her curse upon him; some take it as a blessing in the guise of a curse, as in «God fight him, how eloquent he is!» (al-Zawzanī).",
   "Sona bırakılmış mübteda, damme ile merfû — cümle mekūlü'l-kavl olarak mahallen mansûb; «وَيْلَة»nin cem'i; o da «وَيْل» gibi «şiddetli azap» demektir. Cümle lafzen haber, mânen inşâdır: çoğunluğa göre ona bedduadır; «beddua kalıbında duadır» da denmiştir; «Allah canını alsın, ne fasih adam!» sözü gibi (Zevzenî)."),
 T("إِنَّكَ", "inna", "part", ["inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "إِنَّ is the particle of emphasis and nasb, and the kaf is its noun, in the seat of nasb.", "إِنَّ tekit ve nasb harfi; kâf onun ismi, mahallen mansûb.", s=[("إِنَّ", "inna", "part"), P("كَ")]),
 T("مُرْجِلِي", "murjil", "noun", ["inna-wa-akhawatuha", "ism-fail", "idafa-definiteness", "idafa-lafziyya", "ya-al-mutakallim", "al-qafiya"],
   "خَبَرُ إِنَّ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ — وَالْجُمْلَةُ تَعْلِيلٌ لِلدُّعَاءِ. أَرْجَلَهُ: صَيَّرَهُ رَاجِلًا، أَيْ: تُصَيِّرُنِي رَاجِلَةً لِعَقْرِكَ ظَهْرَ بَعِيرِي.",
   "The predicate of إِنَّ, in raf' by a damma estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term — the ism fa'il annexed to its object. The clause gives the reason for her curse. أَرْجَلَهُ: to make someone go on foot — «you will leave me walking, for you are galling my camel's back».",
   "İnne'nin haberi; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû; muzâf, yâ muzâfun ileyh — ism-i fâilin mef'ûlüne izâfeti. Cümle bedduanın gerekçesidir. أَرْجَلَهُ: birini yaya bırakmak — «devemin sırtını yara ettiğin için beni yaya bırakacaksın».", ".", [("مُرْجِلِ", "murjil", "noun"), P("ي")]),
])
V(None, 14, "She was saying, while the litter leaned over with the two of us: «You have galled my camel's back, Imruʾ al-Qays — get down!»",
  "Mahfe ikimizle birlikte yana yatmışken şöyle diyordu: «Devemin sırtını yara ettin ey İmruülkays, in artık!»", [
 T("تَقُولُ", "qala", "verb", ["mudari-marfu", "hollow-verbs", "hikayat-al-hal"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى عُنَيْزَةَ — وَالْمُضَارِعُ لِحِكَايَةِ الْحَالِ الْمَاضِيَةِ، أَيْ: كَانَتْ تَقُولُ. وَالْجُمْلَةُ مَعْطُوفَةٌ بِعَاطِفٍ مَحْذُوفٍ عَلَى جُمْلَةِ «قَالَتْ» عَلَى تَأْوِيلِ الْمُضَارِعِ بِالْمَاضِي، وَيَجُوزُ أَنْ تَكُونَ مُسْتَأْنَفَةً.",
   "A present verb in raf' by the damma; its doer is a hidden «she», ʿUnayza — the present tense tells a past scene as if it were before the eyes: «she was saying». The clause is conjoined, by a conjunction left out, to «she said», the present read as a past; or it is a fresh sentence.",
   "Damme ile merfû muzâri; fâili Uneyze'ye dönen gizli «hiye» — muzâri, geçmişteki hâlin hikâyesi içindir: «diyordu». Cümle, muzâri mâzî ile tevil edilerek mahzûf bir atıf harfiyle «قَالَتْ» cümlesine ma'tûftur; müste'nefe olması da câizdir."),
 T("وَقَدْ", "qad", "part", ["qad-harf", "al-hal-jumla-wa-rabituha", "anwa-al-waw"], "الْوَاوُ وَاوُ الْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The waw is the waw of the hal; قَدْ is a particle of certainty.", "Vâv hâliye; قَدْ tahkîk harfi.", s=[WA, ("قَدْ", "qad", "part")]),
 W("مَالَ", "mala", "verb", ["hollow-verbs", "thulathi-mujarrad-babs"], J(MADI)),
 W("الْغَبِيطُ", "ghabit", "noun", ["fail"], J(FAILR, Dn("الْغَبِيطُ: ضَرْبٌ مِنَ الرِّحَالِ، وَقِيلَ: مِنَ الْهَوَادِجِ", "الغَبِيط: a kind of camel-saddle — or, it is said, of howdah", "الغَبِيط: bir çeşit deve semeri; «bir çeşit mahfe» de denmiştir"))),
 T("بِنَا", "bi", "prep", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ لِلتَّعْدِيَةِ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَالَ»، أَيْ: أَمَالَنَا الْغَبِيطُ.", "The ba is a jarr letter that makes the verb transitive; نَا is in the seat of jarr — the phrase hangs on «leaned»: the litter tipped us.", "Bâ ta'diye için cer harfi; نَا mahallen mecrûr — câr-mecrûr «مَالَ»ye müteallik: mahfe bizi yana yatırdı.", s=[BI, P("نَا")]),
 T("مَعًا", "maan", "adv", ["hal"], "حَالٌ مِنْ «نَا» مَنْصُوبٌ بِالْفَتْحَةِ، بِمَعْنَى: جَمِيعًا — وَجُمْلَةُ «قَدْ مَالَ الْغَبِيطُ» فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «تَقُولُ».", "A hal of «us», in nasb by the fatha: «both together» — the clause «the litter had leaned» is a hal of the doer of «she was saying», in the seat of nasb.", "«نَا»dan hâl, fetha ile mansûb: «ikimiz birlikte» — «قَدْ مَالَ الْغَبِيطُ» cümlesi «تَقُولُ»nün fâilinden hâl olarak mahallen mansûb.", HEMI),
 T("عَقَرْتَ", "aqara", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ؛ عَقَرْتَ بَعِيرِي أَيْ: أَدْبَرْتَ ظَهْرَهُ.",
   "A past verb built on sukun because the doer's ta is attached; the ta is the doer, in the seat of raf' — the clause is what she said, in the seat of nasb; «you have ʿaqar-ed my camel» means: you have galled his back.",
   "Fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, mahallen merfû — cümle mekūlü'l-kavl olarak mahallen mansûb; «devemi akrettin»: sırtını yara ettin."),
 W("بَعِيرِي", "bair", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim"], J(("مَفْعُولٌ بِهِ مَنْصُوبٌ ", "The direct object, in nasb by ", "Mef'ûlün bih; "), YA_EST("بِفَتْحَةٍ", "a fatha", "fetha ile mansûb")), s=[("بَعِيرِ", "bair", "noun"), P("ي")]),
 T("يَا", "ya-nida", "part", ["vocative-munada"], "حَرْفُ نِدَاءٍ.", "The vocative particle.", "Nidâ harfi."),
 T("امْرَأَ", "imru", "noun", ["vocative-munada", "idafa-definiteness"],
   "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ — وَ«امْرُؤٌ» تَتْبَعُ حَرَكَةُ رَائِهِ حَرَكَةَ هَمْزَتِهِ: امْرُؤٌ وَامْرَأً وَامْرِئٍ.",
   "An annexed vocative, in nasb by the fatha — in امْرُؤ the vowel of the ra follows the vowel of the hamza: امْرُؤٌ, امْرَأً, امْرِئٍ.",
   "Muzâf münâdâ, fetha ile mansûb — «امْرُؤ»de râ'nın harekesi hemzenin harekesine uyar: امْرُؤٌ، امْرَأً، امْرِئٍ."),
 W("الْقَيْسِ", "qays", "propn", ["idafa-definiteness"], J(MI)),
 T("فَانْزِلِ", "nazala", "verb", ["atf-nasaq", "imperative-amr", "thulathi-mujarrad-babs", "al-qafiya"],
   "الْفَاءُ عَاطِفَةٌ تُفِيدُ السَّبَبِيَّةَ، وَانْزِلِ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — أَيْ: فَانْزِلْ عَنِ الْبَعِيرِ.",
   "The fa conjoins, with the sense of cause; انْزِلِ is an imperative built on sukun, voweled with kasra for the rhyme, with the hidden «you» as doer — «so get down from the camel».",
   "Fâ sebebiyet bildiren atıf; انْزِلِ sükûn üzere mebnî emir, kafiye için kesre ile harekelenmiş; fâili vücûben gizli «ente» — «öyleyse deveden in».", "!", [FA, ("انْزِلِ", "nazala", "verb")]),
])
V(None, 15, "So I said to her: «Ride on, and slacken his rein, and do not keep me away from your fruit that is plucked again and again.»",
  "Ona dedim ki: «Yürü, devenin yularını gevşet; beni tekrar tekrar derilen meyvenden uzaklaştırma.»", [
 W("فَقُلْتُ", "qala", "verb", ["atf-nasaq", "hollow-verbs", "al-bariz-al-muttasil"], J(PRE("fa", "قُلْتُ"), lo(MADI_TU)), s=[FA, ("قُلْتُ", "qala", "verb")]),
 T("لَهَا", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قُلْتُ».", "The lam is a jarr letter and هَا is in the seat of jarr — the phrase hangs on «I said».", "Lâm cer harfi, هَا mahallen mecrûr — câr-mecrûr «قُلْتُ»ye müteallik.", s=[("لَ", "li", "prep"), P("هَا")]),
 T("سِيرِي", "sara-travel", "verb", ["imperative-amr", "hollow-verbs", "afal-khamsa"],
   "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ لِاتِّصَالِهِ بِيَاءِ الْمُخَاطَبَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ؛ قَالَ «سِيرِي» وَهِيَ رَاكِبَةٌ، لِأَنَّهُ يُقَالُ لِمَنْ عَلَى الدَّابَّةِ: سَارَ يَسِيرُ.",
   "An imperative built on dropping the nun because the ya of the woman addressed is attached; the ya is the doer, in the seat of raf' — the clause is what he said, in the seat of nasb. He says «go on» though she is riding: سَارَ is said of a rider as of one on foot (al-Zawzanī).",
   "Muhâtaba yâsına bitiştiği için nûnun hazfi üzere mebnî emir; yâ fâil, mahallen merfû — cümle mekūlü'l-kavl olarak mahallen mansûb. Kadın binek üzerindeyken «yürü» demiştir; çünkü «سَارَ» yaya için olduğu gibi binekli için de söylenir (Zevzenî)."),
 T("وَأَرْخِي", "arkha", "verb", ["atf-nasaq", "imperative-amr", "form-iv-verbs", "naqis-verbs"],
   "الْوَاوُ عَاطِفَةٌ، وَأَرْخِي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — مَعْطُوفٌ عَلَى «سِيرِي».",
   "The waw conjoins; أَرْخِي is an imperative built on dropping the nun, and the ya is the doer, in the seat of raf' — conjoined to «ride on».",
   "Vâv atıf; أَرْخِي nûnun hazfi üzere mebnî emir, yâ fâil, mahallen merfû — «سِيرِي»ye ma'tûf.", s=[WA, ("أَرْخِي", "arkha", "verb")]),
 W("زِمَامَهُ", "zimam", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, IDF("هُ"), Dn("وَالضَّمِيرُ لِلْبَعِيرِ", "the pronoun is the camel", "zamir deveye döner")), HEMI, [("زِمَامَ", "zimam", "noun"), P("هُ")]),
 T("وَلَا", "la-nahiya", "part", ["atf-nasaq", "la-nahiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.", "The waw conjoins; لَا is the prohibitive, which puts the verb in jazm.", "Vâv atıf; lâ cezm eden nehiy edatı.", s=[WA, ("لَا", "la-nahiya", "part")]),
 T("تُبْعِدِينِي", "abada-far", "verb", ["la-nahiya", "afal-khamsa", "form-iv-verbs", "maful-bihi", "ya-al-mutakallim"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَيَاءُ الْمُخَاطَبَةِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَقُولِ الْقَوْلِ.",
   "A present verb in jazm by the prohibitive لَا; its sign is the dropped nun — one of the five verbs. The ya of the woman addressed is the doer, in the seat of raf'; the nun guards the ending; the speaker's ya is the direct object, in the seat of nasb. The clause is conjoined to what was said.",
   "Nehiy lâsıyla meczûm muzâri; cezm alâmeti nûnun hazfidir, çünkü ef'âl-i hamsedendir. Muhâtaba yâsı fâil, mahallen merfû; nûn vikâye için; mütekellim yâsı mef'ûlün bih, mahallen mansûb. Cümle mekūlü'l-kavle ma'tûftur.", s=[("تُبْعِدِي", "abada-far", "verb"), P("نِي")]),
 HARF_JARR("مِنْ", "min"),
 T("جَنَاكِ", "jana", "noun", ["huruf-jarr", "ism-maqsur-manqus", "idafa-definiteness", "istiara", "arkan-al-istiara", "istiara-makniyya"],
   "مَجْرُورٌ " + MAQSUR_J + "، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُبْعِدِينِي». الْجَنَى: اسْمٌ لِمَا يُجْتَنَى مِنَ الشَّجَرِ. قَالَ الزَّوْزَنِيُّ: جَعَلَ الْعَشِيقَةَ بِمَنْزِلَةِ الشَّجَرَةِ، وَجَعَلَ مَا نَالَ مِنْهَا بِمَنْزِلَةِ الثَّمَرَةِ لِيَتَنَاسَبَ الْكَلَامُ — فَفِي «الْجَنَى» اسْتِعَارَةٌ تَصْرِيحِيَّةٌ لِمَا يَنَالُهُ مِنْ قُرْبِهَا، وَفِي إِضَافَتِهِ إِلَيْهَا اسْتِعَارَةٌ مَكْنِيَّةٌ: شُبِّهَتْ بِشَجَرَةٍ ثُمَّ حُذِفَ الْمُشَبَّهُ بِهِ وَرُمِزَ إِلَيْهِ بِالْجَنَى.",
   "In jarr by a kasra estimated on the alif, annexed; the kaf is its second term — the phrase hangs on «keep me away». الجَنَى is the name for what is gathered from a tree. Al-Zawzanī: he makes the beloved a tree, and what he had of her its fruit, so that the words suit one another. So «fruit» is an explicit istiʿāra for what he enjoys of her nearness, and annexing it to her is an istiʿāra by kināya — she is likened to a tree, the tree dropped and hinted at by its fruit.",
   "Elif üzerinde takdîrî kesre ile mecrûr, muzâf; kâf muzâfun ileyh — câr-mecrûr «تُبْعِدِينِي»ye müteallik. الجَنَى: ağaçtan derilen şeyin adıdır. Zevzenî: sevgiliyi ağaç, ondan elde ettiğini de meyve yerine koymuştur ki söz birbirine uysun. Demek ki «meyve», yakınlığından elde ettiği şey için istiâre-i tasrîhiyyedir; ona izâfe edilmesinde ise istiâre-i mekniyye vardır: kadın bir ağaca benzetilmiş, müşebbehün bih hazfedilip meyve ile ona işaret edilmiştir.", s=[("جَنَا", "jana", "noun"), P("كِ")]),
 T("الْمُعَلَّلِ", "muallal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
   "نَعْتٌ لِـ«جَنَاكِ» مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ مِنْ «عَلَّلَ»: الْمُكَرَّرُ، مِنْ عَلَّهُ إِذَا كَرَّرَ سَقْيَهُ؛ وَيُرْوَى بِكَسْرِ اللَّامِ أَيِ: الْمُلْهِي.",
   "An adjective of «your fruit», in jarr by the kasra — the ism maf'ul of عَلَّلَ: taken again and again, from عَلَّهُ «to give a second drink»; it is also transmitted with a kasra on the lam: «that beguiles».",
   "«جَنَاكِ»nin na'tı, kesre ile mecrûr — «عَلَّلَ»den ism-i mef'ûl: tekrar tekrar alınan; «ikinci kez su vermek» anlamındaki عَلَّهُ'dan; lâm'ın kesresiyle de rivayet edilir: «oyalayan».", "."),
])
V(None, 16, "Many a woman like you — one with child, and one nursing — I have come to by night, and drawn her mind away from her amuleted one-year-old.",
  "Senin gibi nice gebe ve emzikli kadına gece vakti varmış, onu muskalı, bir yaşındaki yavrusundan alıkoymuşumdur.", [
 T("فَمِثْلِكِ", "mithl", "noun", ["al-lam-wa-rubba-fil-kafiya", "mubtada-khabar", "idafa-definiteness", "hadhf-wa-taqdir"],
   "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَمِثْلِ مَجْرُورٌ لَفْظًا بِـ«رُبَّ» الْمُضْمَرَةِ بَعْدَ الْفَاءِ، وَهُوَ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَيَجُوزُ أَنْ يَكُونَ مَفْعُولًا بِهِ مُقَدَّمًا لِـ«طَرَقْتُ». أَرَادَ: فَرُبَّ امْرَأَةٍ مِثْلِ عُنَيْزَةَ فِي مَيْلِهِ إِلَيْهَا.",
   "The fa opens a new sentence; مِثْلِ wears the kasra of a رُبَّ left unspoken after the fa, and is the mubtada, in raf' by a damma that the near-redundant jarr letter's vowel keeps from showing; annexed, and the kaf is its second term — it may also be the fronted object of «I have come to». He means: many a woman like ʿUnayza in his leaning towards her (al-Zawzanī).",
   "Fâ istînâfiyye; مِثْلِ, fâ'dan sonra gizli «رُبَّ» ile lafzen mecrûr olup mübtedadır; zâide benzeyen cer harfinin harekesi mahalli meşgul ettiği için takdîrî damme ile merfû; muzâf, kâf muzâfun ileyh — «طَرَقْتُ»nun öne geçmiş mef'ûlü olması da câizdir. Maksat: ona meyli bakımından Uneyze gibi nice kadın (Zevzenî).", s=[FA, ("مِثْلِ", "mithl", "noun"), P("كِ")]),
 T("حُبْلَى", "hubla", "noun", ["badal", "mamnu-min-sarf", "ism-maqsur-manqus"],
   "بَدَلٌ مِنْ «مِثْلِ» تَابِعٌ لِلَفْظِهِ، مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَقْصُورَةِ.",
   "A badal of «the like», following its wording: in jarr by a fatha estimated on the alif in place of the kasra — a diptote, for its short feminine alif.",
   "«مِثْلِ»den bedel, lafzına tâbi: elif-i maksûre-i te'nîs sebebiyle gayr-i munsarif olduğundan kesre yerine elif üzerinde takdîrî fetha ile mecrûr."),
 T("قَدْ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ.", "A particle of certainty.", "Tahkîk harfi."),
 W("طَرَقْتُ", "taraqa", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "hadhf-al-maful", "mubtada-khabar"], J(MADI_TU, Dn("وَالْمَفْعُولُ مَحْذُوفٌ أَيْ: طَرَقْتُهَا، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ؛ الطُّرُوقُ: الْإِتْيَانُ لَيْلًا", "the object is dropped («I came to her»), and the clause is the predicate of the mubtada, in the seat of raf'; الطُّرُوق: coming by night", "mef'ûl mahzûftur («ona vardım»); cümle mübtedanın haberi olarak mahallen merfû; الطُّرُوق: gece vakti gelmek"))),
 T("وَمُرْضِعٍ", "murdi", "noun", ["atf-nasaq"],
   "الْوَاوُ عَاطِفَةٌ، وَمُرْضِعٍ مَعْطُوفٌ عَلَى «حُبْلَى» مَجْرُورٌ بِالْكَسْرَةِ — الْمُرْضِعُ: الَّتِي لَهَا وَلَدٌ رَضِيعٌ، وَلَمْ تَلْحَقْهَا التَّاءُ لِأَنَّهَا بِمَعْنَى: ذَاتِ رَضِيعٍ.",
   "The waw conjoins; مُرْضِعٍ is conjoined to «one with child», in jarr by the kasra — المُرْضِع: a woman with a nursling; it takes no feminine ta because it means «she who has a nursling» (al-Zawzanī).",
   "Vâv atıf; مُرْضِعٍ «حُبْلَى»ya ma'tûf, kesre ile mecrûr — المُرْضِع: emzikli çocuğu olan kadın; «emzikli çocuk sahibi» anlamında olduğu için te'nîs tâsı almamıştır (Zevzenî).", HEMI, [WA, ("مُرْضِعٍ", "murdi", "noun")]),
 T("فَأَلْهَيْتُهَا", "alha", "verb", ["atf-nasaq", "form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"],
   "الْفَاءُ عَاطِفَةٌ، وَأَلْهَيْتُ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «طَرَقْتُ».",
   "The fa conjoins; أَلْهَيْتُ is a past verb built on sukun because the doer's ta is attached; the ta is the doer, in the seat of raf', and هَا is the direct object, in the seat of nasb — the clause is conjoined to «I have come to».",
   "Fâ atıf; أَلْهَيْتُ fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, mahallen merfû; هَا mef'ûlün bih, mahallen mansûb — cümle «طَرَقْتُ» cümlesine ma'tûftur.", s=[FA, ("أَلْهَيْتُ", "alha", "verb"), P("هَا")]),
 HARF_JARR("عَنْ", "an"),
 T("ذِي", "dhu", "noun", ["huruf-jarr", "five-nouns", "idafa-definiteness", "hadhf-wa-taqdir", "kinaya", "aqsam-al-kinaya"],
   "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَلْهَيْتُهَا»؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: عَنْ صَبِيٍّ ذِي تَمَائِمَ. وَ«ذِي تَمَائِمَ مُحْوِلِ» كِنَايَةٌ عَنْ مَوْصُوفٍ هُوَ وَلَدُهَا الرَّضِيعُ.",
   "In jarr by the ya — one of the five nouns — annexed; the phrase hangs on «drawn her mind away». It describes a noun left out: «from a child that has amulets». «The amuleted one-year-old» is a kinaya for a thing described: her nursling.",
   "Esmâ-i hamseden olduğu için yâ ile mecrûr, muzâf — câr-mecrûr «أَلْهَيْتُهَا»ya müteallik; mahzûf mevsûfun na'tıdır: «muskalı bir çocuktan». «Muskalı, bir yaşındaki» ifadesi mevsûftan — emzikteki çocuğundan — kinâyedir."),
 W("تَمَائِمَ", "tamima", "noun", ["idafa-definiteness", "mamnu-min-sarf", "jam-taksir"], J(("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ", "The second term of the idafa, in jarr by the fatha in place of the kasra — a diptote, on the pattern of the ultimate plural", "Muzâfun ileyh; müntehe'l-cümû' sîgasında gayr-i munsarif olduğundan kesre yerine fetha ile mecrûr"), Dn("جَمْعُ تَمِيمَةٍ وَهِيَ الْعُوذَةُ تُعَلَّقُ عَلَى الصَّبِيِّ", "the plural of تَمِيمَة, the charm hung on a child", "«تَمِيمَة»nin cem'i: çocuğa takılan muska"))),
 W("مُحْوِلِ", "muhwil", "noun", ["naat-sifa", "ism-fail", "al-qafiya"], J(("نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ", "A second adjective of the omitted noun, in jarr by the kasra", "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr"), QAFIYA, Dn("الْمُحْوِلُ: الَّذِي أَتَى عَلَيْهِ حَوْلٌ", "المُحْوِل: one over whom a year has passed", "المُحْوِل: üzerinden bir yıl geçmiş olan")), "."),
])
V(None, 17, "When he cried behind her, she turned to him with one half, while her other half, beneath me, was not turned away.",
  "Çocuk arkasında ağlayınca bir yanıyla ona dönerdi; öbür yanı ise altımda, çevrilmeden kalırdı.", [
 W("إِذَا", "idha", "part", ["maful-fih", "idha-shartiyya"], J(IDHA, Dn("مُتَعَلِّقٌ بِجَوَابِهِ «انْصَرَفَتْ»", "it hangs on its answer, «she turned»", "cevabı olan «انْصَرَفَتْ»e müteallik"))),
 T("مَا", "ma-zaida", "part", ["anwa-ma"], "زَائِدَةٌ لِلتَّوْكِيدِ.", "The added مَا, for emphasis.", "Tekit için zâid mâ."),
 T("بَكَى", "baka", "verb", ["naqis-verbs", "idha-shartiyya"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الصَّبِيِّ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "A past verb built on a fatha estimated on the alif; its doer is a hidden pronoun returning to the child — the clause is in the seat of jarr, annexed to إِذَا.",
   "Elif üzerinde takdîrî fetha üzere mebnî mâzî; fâili çocuğa dönen gizli zamir — cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr."),
 HARF_JARR("مِنْ", "min"),
 W("خَلْفِهَا", "khalf", "noun", ["huruf-jarr", "idafa-definiteness"], J(MAJR, IDF("هَا"), TA("بَكَى", "cried", "ya")), s=[("خَلْفِ", "khalf", "noun"), P("هَا")]),
 W("انْصَرَفَتْ", "insarafa", "verb", ["form-vii-verbs", "idha-shartiyya"], J(MADI_F, HID("هِيَ", "she", "hiye", ("الْمُرْضِعِ", "the nursing woman", "emzikli kadına")), Dn("وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "the clause answers إِذَا and has no seat", "cümle «إِذَا»nın cevabıdır, i'râbdan mahalli yoktur"))),
 T("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«انْصَرَفَتْ».", "The lam is a jarr letter and the هُ is in the seat of jarr — the phrase hangs on «she turned».", "Lâm cer harfi, «hû» mahallen mecrûr — câr-mecrûr «انْصَرَفَتْ»e müteallik.", HEMI, [("لَ", "li", "prep"), P("هُ")]),
 T("بِشِقٍّ", "shiqq", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَشِقٍّ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«انْصَرَفَتْ»؛ شِقُّ الشَّيْءِ: نِصْفُهُ.", "The ba is a jarr letter and شِقٍّ is in jarr by the kasra — the phrase hangs on «she turned»; the شِقّ of a thing is its half.", "Bâ cer harfi, شِقٍّ kesre ile mecrûr — câr-mecrûr «انْصَرَفَتْ»e müteallik; bir şeyin «شِقّ»i yarısıdır.", s=[BI, ("شِقٍّ", "shiqq", "noun")]),
 T("وَتَحْتِي", "tahta", "noun", ["al-hal-jumla-wa-rabituha", "anwa-al-waw", "maful-fih", "taqdim-al-musnad", "ya-al-mutakallim"],
   "الْوَاوُ وَاوُ الْحَالِ، وَتَحْتِ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
   "The waw is the waw of the hal; تَحْتِ is an adverb of place, in nasb by a fatha estimated before the speaker's ya, annexed, and the ya is its second term — it hangs on an omitted predicate, set first.",
   "Vâv hâliye; تَحْتِ mekân zarfı, mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb, muzâf; yâ muzâfun ileyh — öne geçmiş mahzûf habere müteallik.", s=[WA, ("تَحْتِ", "tahta", "noun"), P("ي")]),
 W("شِقُّهَا", "shiqq", "noun", ["mubtada-khabar", "idafa-definiteness"], J(("مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, placed last, in raf' by the damma", "Sona bırakılmış mübteda, damme ile merfû"), IDF("هَا"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «انْصَرَفَتْ»", "the clause is a hal of the doer of «she turned», in the seat of nasb", "cümle «انْصَرَفَتْ»in fâilinden hâl olarak mahallen mansûb")), s=[("شِقُّ", "shiqq", "noun"), P("هَا")]),
 T("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The particle of negation that puts the verb in jazm and turns it to the past.", "Nefy, cezm ve kalb harfi."),
 T("يُحَوَّلِ", "hawwala", "verb", ["lam-jazim", "form-ii-verbs", "naib-al-fail", "kinaya", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «شِقُّهَا» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «شِقُّهَا». وَالْبَيْتُ كِنَايَةٌ عَنْ غَايَةِ مَيْلِهَا إِلَيْهِ، حَيْثُ لَمْ يَشْغَلْهَا عَنْهُ مَا يَشْغَلُ الْأُمَّهَاتِ عَنْ كُلِّ شَيْءٍ.",
   "A present verb in the passive, in jazm by لَمْ, its sign the sukun, voweled with kasra for the rhyme; its deputy doer is a hidden pronoun returning to «her half» — the clause is a hal of «her half», in the seat of nasb. The verse is a kinaya for how wholly she leaned to him: what takes mothers from everything else did not take her from him (al-Zawzanī).",
   "Lem ile meczûm meçhul muzâri; cezm alâmeti sükûn, kafiye için kesre ile harekelenmiş; nâib-i fâili «شِقُّهَا»ya dönen gizli zamir — cümle «شِقُّهَا»dan hâl olarak mahallen mansûb. Beyit, kadının ona son derece meyletmesinden kinâyedir: anneleri her şeyden alıkoyan şey onu ondan alıkoymamıştır (Zevzenî).", "."),
])
V(None, 18, "And one day, on the back of the sand-dune, she grew hard with me, and swore an oath that left no way out.",
  "Bir gün de kum tepesinin sırtında bana karşı sertleşti ve istisnası olmayan bir yemin etti.", [
 T("وَيَوْمًا", "yawm", "noun", ["maful-fih"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَيَوْمًا ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِـ«تَعَذَّرَتْ».", "The waw opens a new sentence; يَوْمًا is an adverb of time, in nasb by the fatha, hanging on «she grew hard».", "Vâv istînâfiyye; يَوْمًا zaman zarfı, fetha ile mansûb, «تَعَذَّرَتْ»e müteallik.", s=[WA, ("يَوْمًا", "yawm", "noun")]),
 HARF_JARR("عَلَى", "ala"),
 W("ظَهْرِ", "zahr", "noun", ["huruf-jarr", "idafa-definiteness"], J(MAJR, MUD, TA("تَعَذَّرَتْ", "she grew hard", "e"))),
 W("الْكَثِيبِ", "kathib", "noun", ["idafa-definiteness"], J(MI, Dn("الْكَثِيبُ: رَمْلٌ كَثِيرٌ مُجْتَمِعٌ", "الكَثِيب: a great heap of sand, a dune", "الكَثِيب: yığılmış çok kum, kum tepesi"))),
 W("تَعَذَّرَتْ", "taadhdhara", "verb", ["form-v-verbs"], J(MADI_F, HID("هِيَ", "she", "hiye", ("صَاحِبَتِهِ", "the woman", "kadına")), Dn("التَّعَذُّرُ: التَّشَدُّدُ وَالِالْتِوَاءُ", "التَّعَذُّر: to turn stiff and contrary", "التَّعَذُّر: sertleşip yan çizmek")), HEMI),
 T("عَلَيَّ", "ala", "prep", ["huruf-jarr", "ya-al-mutakallim"], "عَلَى حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَعَذَّرَتْ».", "عَلَى is a jarr letter and the ya is in the seat of jarr — the phrase hangs on «she grew hard».", "عَلَى cer harfi, yâ mahallen mecrûr — câr-mecrûr «تَعَذَّرَتْ»e müteallik.", s=[("عَلَيْ", "ala", "prep"), P("يَ")]),
 T("وَآلَتْ", "ala-swear", "verb", ["atf-nasaq", "form-iv-verbs", "naqis-verbs"],
   "الْوَاوُ عَاطِفَةٌ، وَآلَتْ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «تَعَذَّرَتْ».",
   "The waw conjoins; آلَتْ is a past verb built on a fatha estimated on the alif, which falls where two still letters meet; the ta marks the feminine, and the doer is a hidden «she» — the clause is conjoined to «she grew hard».",
   "Vâv atıf; آلَتْ iki sâkinin karşılaşması yüzünden düşen elif üzerinde takdîrî fetha üzere mebnî mâzî; tâ te'nîs için, fâili gizli «hiye» — cümle «تَعَذَّرَتْ» cümlesine ma'tûftur.", s=[WA, ("آلَتْ", "ala-swear", "verb")]),
 T("حَلْفَةً", "halfa", "noun", ["maful-mutlaq"],
   "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — نَصَبَهُ «آلَتْ» لِأَنَّهُ بِمَعْنَى مَصْدَرِهِ، كَأَنَّهُ قَالَ: آلَتْ إِيلَاءً.",
   "An absolute object, in nasb by the fatha — «she swore» governs it because it means what its own masdar means, as if he had said آلَتْ إِيلَاءً (al-Zawzanī).",
   "Mef'ûlün mutlak, fetha ile mansûb — «آلَتْ» onu, kendi masdarının anlamında olduğu için nasbetmiştir; sanki «آلَتْ إِيلَاءً» demiştir (Zevzenî)."),
 T("لَمْ", "lam-jazima", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The particle of negation that puts the verb in jazm and turns it to the past.", "Nefy, cezm ve kalb harfi."),
 T("تَحَلَّلِ", "tahallala", "verb", ["lam-jazim", "form-v-verbs", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَأَصْلُهُ «تَتَحَلَّلْ» فَحُذِفَتْ إِحْدَى التَّاءَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «آلَتْ»؛ وَظَاهِرُ شَرْحِ الزَّوْزَنِيِّ («حَلِفًا لَمْ تَسْتَثْنِ فِيهِ») أَنَّهَا نَعْتٌ لِـ«حَلْفَةً». التَّحَلُّلُ فِي الْيَمِينِ: الِاسْتِثْنَاءُ.",
   "A present verb in jazm by لَمْ, its sign the sukun, voweled with kasra for the rhyme; it is تَتَحَلَّلْ with one of its two ta's dropped, and its doer is a hidden «she» — the clause is a hal of the doer of «she swore», in the seat of nasb; al-Zawzanī's paraphrase («an oath in which she made no exception») reads it as an adjective of «an oath». التَّحَلُّل in an oath is making an exception.",
   "Lem ile meczûm muzâri; cezm alâmeti sükûn, kafiye için kesre ile harekelenmiş; aslı «تَتَحَلَّلْ»dir, iki tâ'dan biri düşmüştür; fâili gizli «hiye» — cümle «آلَتْ»in fâilinden hâl olarak mahallen mansûb; Zevzenî'nin şerhinin zâhiri («içinde istisna yapmadığı bir yemin») ise «حَلْفَةً»nin na'tı olmasıdır. Yeminde «التَّحَلُّل»: istisna etmek.", "."),
])

# =====================================================================================================================
# The reproach to Fāṭima; the lady of the guarded tent: verses 19–25
# =====================================================================================================================
LAM_J = ("حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The particle of negation that puts the verb in jazm and turns it to the past.", "Nefy, cezm ve kalb harfi.")
QAD = ("حَرْفُ تَحْقِيقٍ.", "A particle of certainty.", "Tahkîk harfi.")
MA_Z = ("زَائِدَةٌ لِلتَّوْكِيدِ.", "The added مَا, for emphasis.", "Tekit için zâid mâ.")
KASR_Q = ("، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ", ", voweled with kasra for the rhyme", ", kafiye için kesre ile harekelenmiş")
def PJ(full, prep_form, prep_lex, pron, name3, on, on_en, on_tr, p=None, extra=("", "", ""), g=None):
    """a jarr letter with its attached pronoun: name3 = how the letter is named (ar, en, tr); it hangs on «on»"""
    a, e, t = _PRN[pron]
    return T(full, prep_lex, "prep", g or ["huruf-jarr"],
             "%s حَرْفُ جَرٍّ، وَ%s ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«%s»%s." % (name3[0], a, on, extra[0]),
             "%s is a jarr letter and %s is in the seat of jarr — the phrase hangs on «%s»%s." % (name3[1], e, on_en, extra[1]),
             "%s cer harfi, %s mahallen mecrûr — câr-mecrûr «%s»%s müteallik%s." % (name3[2], t, on, on_tr, extra[2]), p, [(prep_form, prep_lex, "prep"), P(pron)])
MIN3, LAM3, BA3, ALA3, ILA3 = ("مِنْ", "مِنْ", "مِنْ"), ("اللَّامُ", "The lam", "Lâm"), ("الْبَاءُ", "The ba", "Bâ"), ("عَلَى", "عَلَى", "عَلَى"), ("إِلَى", "إِلَى", "إِلَى")
V(None, 19, "O Fāṭima, gently — leave some of this coquetry; and if you have resolved to cut me off, then do it kindly.",
  "Ey Fâtıma, yavaş ol; bu nazın bir kısmını bırak. Eğer benden kopmaya karar verdiysen bunu güzellikle yap.", [
 T("أَفَاطِمَ", "fatima", "propn", ["vocative-munada", "hadhf-wa-taqdir"],
   "الْهَمْزَةُ حَرْفُ نِدَاءٍ لِلْقَرِيبِ، وَفَاطِمَ مُنَادًى مُرَخَّمُ «فَاطِمَةَ»، مَبْنِيٌّ عَلَى الضَّمِّ عَلَى التَّاءِ الْمَحْذُوفَةِ لِلتَّرْخِيمِ فِي مَحَلِّ نَصْبٍ، عَلَى لُغَةِ مَنْ يَنْتَظِرُ — فَبَقِيَتِ الْمِيمُ مَفْتُوحَةً. فَاطِمَةُ: قِيلَ هِيَ عُنَيْزَةُ، وَعُنَيْزَةُ لَقَبٌ لَهَا.",
   "The hamza is the vocative particle for one who is near; فَاطِمَ is a vocative, فَاطِمَة cut short (tarkhīm), built on a damma on the ta that was dropped, in the seat of nasb — in the usage of those who keep the dropped letter in mind, so the mim keeps its fatha. Fāṭima is said to be ʿUnayza herself, ʿUnayza being her nickname.",
   "Hemze, yakın için nidâ harfi; فَاطِمَ, «فَاطِمَة»nin terhîm edilmiş münâdâsıdır; terhîm için düşen tâ üzerinde damme üzere mebnî, mahallen mansûb — düşen harfi bekleyenlerin lügatine göre; bu yüzden mîm fethalı kalmıştır. Fâtıma'nın Uneyze olduğu, Uneyze'nin onun lakabı olduğu söylenir.", s=[("أَ", "hamza-nida", "part"), ("فَاطِمَ", "fatima", "propn")]),
 T("مَهْلًا", "mahl", "noun", ["maful-mutlaq", "al-amr-wa-wujuhuh", "masdar"],
   "مَفْعُولٌ مُطْلَقٌ نَائِبٌ عَنْ فِعْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ، أَيْ: رِفْقًا — وَهُوَ أَمْرٌ بِالْمَصْدَرِ، وَالْأَمْرُ هُنَا لِلِالْتِمَاسِ وَالِاسْتِعْطَافِ.",
   "An absolute object standing in for its verb, in nasb by the fatha: «gently» — a command by the masdar; the command here is a plea, a suing for kindness.",
   "Fiilinin yerini tutan mef'ûlün mutlak, fetha ile mansûb: «yavaş ol» — masdarla emirdir; emir burada iltimâs ve istirham içindir."),
 T("بَعْضَ", "bad", "noun", ["maful-bihi", "idafa-definiteness"],
   "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — نَصَبَهُ «مَهْلًا» لِأَنَّهُ يَنُوبُ مَنَابَ «دَعِي».",
   "A direct object, in nasb by the fatha, annexed — «gently» governs it because it stands for «leave» (al-Zawzanī).",
   "Mef'ûlün bih, fetha ile mansûb, muzâf — «مَهْلًا» onu, «bırak» fiilinin yerini tuttuğu için nasbetmiştir (Zevzenî)."),
 T("هٰذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "الْهَاءُ لِلتَّنْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The ha alerts; ذَا is a demonstrative built on sukun, the second term of the idafa, in the seat of jarr.", "Hâ tenbih için; ذَا sükûn üzere mebnî ism-i işâret, muzâfun ileyh, mahallen mecrûr."),
 W("التَّدَلُّلِ", "tadallul", "noun", ["badal", "masdar", "al-qafiya"], J(("بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ أَوْ عَطْفُ بَيَانٍ مَجْرُورٌ بِالْكَسْرَةِ", "A badal of the demonstrative, or its explanatory apposition, in jarr by the kasra", "İsm-i işâretten bedel ya da atf-ı beyân, kesre ile mecrûr"), Dn("التَّدَلُّلُ: أَنْ يَثِقَ الْإِنْسَانُ بِحُبِّ غَيْرِهِ إِيَّاهُ فَيَتَجَرَّأَ عَلَيْهِ؛ وَفِي الْبَيْتِ تَصْرِيعٌ", "التَّدَلُّل: presuming on another's love and so making bold with him; the verse has taṣrīʿ — both hemistichs end on the rhyme", "التَّدَلُّل: sevildiğine güvenip nazlanmak; beyitte tasrî' vardır — iki mısra da kafiyeyle biter")), HEMI),
 T("وَإِنْ", "in-shartiyya", "part", ["atf-nasaq", "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "The waw conjoins; إِنْ is a conditional particle that governs jazm.", "Vâv atıf; إِنْ cezm eden şart harfi.", s=[WA, ("إِنْ", "in-shartiyya", "part")]),
 T("كُنْتِ", "kana", "verb", ["kana-wa-akhawatuha", "in-shartiyya", "hollow-verbs", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا.",
   "A defective past verb built on sukun, the verb of the condition, in the seat of jazm; the ta is its noun, in the seat of raf'.",
   "Sükûn üzere mebnî nâkıs mâzî; şart fiili olarak mahallen meczûm; tâ onun ismi, mahallen merfû."),
 T("قَدْ", "qad", "part", ["qad-harf"], QAD[0], QAD[1], QAD[2]),
 T("أَزْمَعْتِ", "azmaa", "verb", ["form-iv-verbs", "al-bariz-al-muttasil", "kana-wa-akhawatuha"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «كَانَ»؛ أَزْمَعَ الْأَمْرَ: وَطَّنَ نَفْسَهُ عَلَيْهِ.",
   "A past verb built on sukun because the doer's ta is attached; the ta is the doer, in the seat of raf' — the clause is the predicate of كَانَ, in the seat of nasb; أَزْمَعَ الْأَمْرَ: to set one's mind on a thing.",
   "Fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, mahallen merfû — cümle «كَانَ»nin haberi olarak mahallen mansûb; أَزْمَعَ الْأَمْرَ: bir işe kesin karar vermek."),
 W("صَرْمِي", "sarm", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "masdar", "imal-al-masdar"], J(("مَفْعُولٌ بِهِ مَنْصُوبٌ ", "The direct object, in nasb by ", "Mef'ûlün bih; "), YA_EST("بِفَتْحَةٍ", "a fatha", "fetha ile mansûb"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ؛ الصَّرْمُ: الْقَطْعُ وَالْهِجْرَانُ", "the masdar annexed to its object; الصَّرْم: cutting off, forsaking", "masdarın mef'ûlüne izâfeti; الصَّرْم: ilişkiyi kesmek, terk etmek")), s=[("صَرْمِ", "sarm", "noun"), P("ي")]),
 T("فَأَجْمِلِي", "ajmala", "verb", ["al-fa-fi-jawab-al-shart", "imperative-amr", "al-amr-wa-wujuhuh", "form-iv-verbs", "afal-khamsa", "al-qafiya"],
   "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَأَجْمِلِي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ؛ أَيْ: فَأَجْمِلِي فِي الْهِجْرَانِ، وَالْأَمْرُ لِلِالْتِمَاسِ.",
   "The fa ties the answer to the condition; أَجْمِلِي is an imperative built on dropping the nun, and the ya is the doer, in the seat of raf' — the clause is the answer of the condition, in the seat of jazm: «then be gracious in your forsaking»; the command is a plea.",
   "Fâ şartın cevabını bağlar; أَجْمِلِي nûnun hazfi üzere mebnî emir, yâ fâil, mahallen merfû — cümle şartın cevabı olarak mahallen meczûm: «ayrılırken güzel davran»; emir iltimâs içindir.", ".", [FA, ("أَجْمِلِي", "ajmala", "verb")]),
])
V(None, 20, "Has it made you bold with me that love of you is killing me, and that whatever you bid my heart, it does?",
  "Sevginin beni öldürmesi ve kalbime ne emredersen yapması mı seni bana karşı böyle şımarttı?", [
 T("أَغَرَّكِ", "gharra", "verb", ["al-istifham", "khuruj-al-istifham", "doubled-verbs", "maful-bihi"],
   "الْهَمْزَةُ لِلِاسْتِفْهَامِ، وَغَرَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ. قَالَ الزَّوْزَنِيُّ: وَأَلِفُ الِاسْتِفْهَامِ دَخَلَتْ عَلَى هٰذَا الْقَوْلِ لِلتَّقْرِيرِ لَا لِلِاسْتِفْهَامِ وَالِاسْتِخْبَارِ، أَيْ: قَدْ غَرَّكِ مِنِّي ذٰلِكَ.",
   "The hamza is the hamza of question; غَرَّ is a past verb built on fatha, and the kaf is its direct object, in the seat of nasb. Al-Zawzanī: the question-hamza comes here to affirm (taqrīr), not to ask: «it has indeed made you bold with me».",
   "Hemze istifham içindir; غَرَّ fetha üzere mebnî mâzî, kâf mef'ûlün bih, mahallen mansûb. Zevzenî: istifham elifi bu söze sormak için değil takrîr için girmiştir: «bu seni gerçekten bana karşı şımarttı».", s=[("أَ", "a-istifham", "part"), ("غَرَّ", "gharra", "verb"), P("كِ")]),
 T("مِنِّي", "min", "prep", ["huruf-jarr", "ya-al-mutakallim"], "مِنْ حَرْفُ جَرٍّ، وَالنُّونُ الثَّانِيَةُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«غَرَّ».", "مِنْ is a jarr letter, the second nun guards it, and the ya is in the seat of jarr — the phrase hangs on «made bold».", "مِنْ cer harfi, ikinci nûn vikâye için, yâ mahallen mecrûr — câr-mecrûr «غَرَّ»ye müteallik.", s=[("مِنِّ", "min", "prep"), P("ي")]),
 T("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ وَمَصْدَرٍ.", "The particle of emphasis and nasb that turns its clause into a masdar.", "Tekit, nasb ve masdar harfi."),
 W("حُبَّكِ", "hubb", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar", "imal-al-masdar"], J(("اسْمُ «أَنَّ» مَنْصُوبٌ بِالْفَتْحَةِ", "The noun of أَنَّ, in nasb by the fatha", "«أَنَّ»nin ismi, fetha ile mansûb"), IDF("كِ"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى مَفْعُولِهِ، أَيْ: حُبِّي إِيَّاكِ", "the masdar annexed to its object: «my love of you»", "masdarın mef'ûlüne izâfeti: «seni sevmem»")), s=[("حُبَّ", "hubb", "noun"), P("كِ")]),
 T("قَاتِلِي", "qatil", "noun", ["inna-wa-akhawatuha", "ism-fail", "idafa-definiteness", "idafa-lafziyya", "ya-al-mutakallim", "majaz-aqli"],
   "خَبَرُ «أَنَّ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «أَنَّ» وَمَعْمُولَيْهَا فِي مَحَلِّ رَفْعٍ فَاعِلُ «غَرَّ». وَفِي إِسْنَادِ الْقَتْلِ إِلَى الْحُبِّ مَجَازٌ عَقْلِيٌّ عَلَاقَتُهُ السَّبَبِيَّةُ.",
   "The predicate of أَنَّ, in raf' by a damma estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term — the ism fa'il annexed to its object. The masdar made by أَنَّ and its two terms is the doer of «made bold», in the seat of raf'. Ascribing the killing to love is a majaz ʿaqlī whose tie is cause.",
   "«أَنَّ»nin haberi; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû; muzâf, yâ muzâfun ileyh — ism-i fâilin mef'ûlüne izâfeti. «أَنَّ» ile iki ma'mûlünden oluşan müevvel masdar «غَرَّ»nin fâili olarak mahallen merfû. Öldürmenin sevgiye isnadında alâkası sebebiyet olan mecâz-ı aklî vardır.", HEMI, [("قَاتِلِ", "qatil", "noun"), P("ي")]),
 T("وَأَنَّكِ", "anna", "part", ["atf-nasaq", "inna-wa-akhawatuha"], "الْوَاوُ عَاطِفَةٌ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى فَاعِلِ «غَرَّ».", "The waw conjoins; أَنَّ is the particle of emphasis and nasb, and the kaf is its noun, in the seat of nasb — the masdar so made is conjoined to the doer of «made bold».", "Vâv atıf; أَنَّ tekit ve nasb harfi, kâf onun ismi, mahallen mansûb — müevvel masdar «غَرَّ»nin fâiline ma'tûftur.", s=[WA, ("أَنَّ", "anna", "part"), P("كِ")]),
 T("مَهْمَا", "mahma", "pron", ["al-majzum-wal-shart-wal-jaza", "maful-mutlaq"],
   "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ مُطْلَقٌ عَامِلُهُ «تَأْمُرِي»، أَيْ: أَيَّ أَمْرٍ تَأْمُرِي.",
   "A conditional noun that governs jazm, built on sukun in the seat of nasb as an absolute object of «you bid»: «whatever bidding you bid».",
   "Cezm eden şart ismi; sükûn üzere mebnî, «تَأْمُرِي»nin mef'ûlün mutlakı olarak mahallen mansûb: «hangi emri verirsen»."),
 T("تَأْمُرِي", "amara-command", "verb", ["al-majzum-wal-shart-wal-jaza", "afal-khamsa"],
   "فِعْلٌ مُضَارِعٌ فِعْلُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
   "A present verb, the verb of the condition, in jazm; its sign is the dropped nun — one of the five verbs; the ya is the doer, in the seat of raf'.",
   "Şart fiili olan muzâri, meczûm; cezm alâmeti nûnun hazfidir, çünkü ef'âl-i hamsedendir; yâ fâil, mahallen merfû."),
 W("الْقَلْبَ", "qalb", "noun", ["maful-bihi"], J(MAFR, Dn("أَيْ: قَلْبِي", "that is, «my heart»", "yani «kalbimi»"))),
 T("يَفْعَلِ", "faala", "verb", ["al-majzum-wal-shart-wal-jaza", "hadhf-al-maful", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ جَوَابُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْقَلْبِ، وَالْمَفْعُولُ مَحْذُوفٌ أَيْ: يَفْعَلْهُ — وَجُمْلَةُ الشَّرْطِ وَجَوَابِهِ فِي مَحَلِّ رَفْعٍ خَبَرُ «أَنَّ».",
   "A present verb, the answer of the condition, in jazm, its sign the sukun, voweled with kasra for the rhyme; its doer is a hidden pronoun returning to the heart, and its object is dropped: «it does it». The condition with its answer is the predicate of أَنَّ, in the seat of raf'.",
   "Şartın cevabı olan muzâri, meczûm; cezm alâmeti sükûn, kafiye için kesre ile harekelenmiş; fâili kalbe dönen gizli zamir, mef'ûl mahzûftur: «onu yapar». Şart cümlesi cevabıyla birlikte «أَنَّ»nin haberi olarak mahallen merfû.", "؟"),
])
V(None, 21, "And if some trait of mine has displeased you, then draw my garments out of your garments, and they will slip away.",
  "Eğer bir huyum hoşuna gitmediyse elbisemi elbisenden çekip çıkar; o da sıyrılıp düşsün.", [
 T("وَإِنْ", "in-shartiyya", "part", ["atf-nasaq", "in-shartiyya"], "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "The waw conjoins; إِنْ is a conditional particle that governs jazm.", "Vâv atıf; إِنْ cezm eden şart harfi.", s=[WA, ("إِنْ", "in-shartiyya", "part")]),
 T("تَكُ", "kana", "verb", ["kana-wa-akhawatuha", "in-shartiyya", "hollow-verbs"],
   "فِعْلٌ مُضَارِعٌ نَاقِصٌ فِعْلُ الشَّرْطِ مَجْزُومٌ وَعَلَامَةُ جَزْمِهِ السُّكُونُ عَلَى النُّونِ الْمَحْذُوفَةِ لِلتَّخْفِيفِ، وَاسْمُهُ «خَلِيقَةٌ» الْمُتَأَخِّرُ.",
   "A defective present verb, the verb of the condition, in jazm; its sign is the sukun on the nun, which is dropped for lightness; its noun is «a trait», which comes later.",
   "Şart fiili olan nâkıs muzâri, meczûm; cezm alâmeti, hafiflik için düşen nûn üzerindeki sükûndur; ismi sonradan gelen «خَلِيقَةٌ»dür."),
 T("قَدْ", "qad", "part", ["qad-harf"], QAD[0], QAD[1], QAD[2]),
 T("سَاءَتْكِ", "saa-bad", "verb", ["hollow-verbs", "maful-bihi", "kana-wa-akhawatuha"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «خَلِيقَةٌ» الْمُتَأَخِّرَةِ لَفْظًا الْمُتَقَدِّمَةِ رُتْبَةً — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «تَكُ» مُقَدَّمٌ.",
   "A past verb built on fatha; the ta marks the feminine, the kaf is its direct object, in the seat of nasb, and its doer is a hidden «she» returning to «a trait», which is later in the words but earlier in rank — the clause is the predicate of تَكُ, set first, in the seat of nasb.",
   "Fetha üzere mebnî mâzî; tâ te'nîs için, kâf mef'ûlün bih, mahallen mansûb; fâili, lafzen sonra rütbeten önce gelen «خَلِيقَةٌ»ye dönen gizli «hiye» — cümle «تَكُ»nün öne geçmiş haberi olarak mahallen mansûb.", s=[("سَاءَتْ", "saa-bad", "verb"), P("كِ")]),
 T("مِنِّي", "min", "prep", ["huruf-jarr", "ya-al-mutakallim", "hal"], "مِنْ حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «خَلِيقَةٌ»، كَانَ نَعْتًا لَهَا فَلَمَّا تَقَدَّمَ صَارَ حَالًا.", "مِنْ is a jarr letter and the ya is in the seat of jarr — the phrase hangs on an omitted hal of «a trait»: it was its adjective, and coming before it became a hal.", "مِنْ cer harfi, yâ mahallen mecrûr — câr-mecrûr «خَلِيقَةٌ»den mahzûf hâle müteallik; onun na'tı iken öne geçince hâl olmuştur.", s=[("مِنِّ", "min", "prep"), P("ي")]),
 W("خَلِيقَةٌ", "khalaiq", "noun", ["kana-wa-akhawatuha"], J(("اسْمُ «تَكُ» مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ", "The noun of تَكُ, placed last, in raf' by the damma", "«تَكُ»nün sona bırakılmış ismi, damme ile merfû"), Dn("الْخَلِيقَةُ: الْخُلُقُ وَالْخَصْلَةُ", "الخَلِيقَة: a trait of character", "الخَلِيقَة: huy, haslet")), HEMI),
 T("فَسُلِّي", "salla-draw", "verb", ["al-fa-fi-jawab-al-shart", "imperative-amr", "doubled-verbs", "afal-khamsa"],
   "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَسُلِّي فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
   "The fa ties the answer to the condition; سُلِّي is an imperative built on dropping the nun, and the ya is the doer, in the seat of raf' — the clause is the answer of the condition, in the seat of jazm.",
   "Fâ şartın cevabını bağlar; سُلِّي nûnun hazfi üzere mebnî emir, yâ fâil, mahallen merfû — cümle şartın cevabı olarak mahallen meczûm.", s=[FA, ("سُلِّي", "salla-draw", "verb")]),
 T("ثِيَابِي", "thawb", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "jam-taksir", "kinaya", "aqsam-al-kinaya"],
   "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ. قَالَ الزَّوْزَنِيُّ: مِنَ النَّاسِ مَنْ جَعَلَ الثِّيَابَ هُنَا بِمَعْنَى الْقَلْبِ، وَمِنْهُمْ مَنْ حَمَلَهَا عَلَى الثِّيَابِ الْمَلْبُوسَةِ وَقَالَ: كَنَّى بِتَبَايُنِ الثِّيَابِ وَتَبَاعُدِهَا عَنْ تَبَاعُدِهِمَا، أَيْ: فَفَارِقِينِي — فَهُوَ كِنَايَةٌ عَنِ الْمُفَارَقَةِ.",
   "The direct object, in nasb by a fatha estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term. Al-Zawzanī: some take «garments» here to mean the heart; others take them as the clothes one wears and say: by the garments parting and going far from each other he hints at the two of them going far apart — «then leave me». So it is a kinaya for parting.",
   "Mef'ûlün bih; mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb; muzâf, yâ muzâfun ileyh. Zevzenî: kimileri buradaki «elbise»yi kalp anlamına almış; kimileri de giyilen elbise saymış ve şöyle demiştir: elbiselerin ayrılıp uzaklaşmasıyla ikisinin birbirinden uzaklaşmasını kinâye etmiştir, yani «benden ayrıl» — demek ki ayrılıktan kinâyedir.", s=[("ثِيَابِ", "thawb", "noun"), P("ي")]),
 HARF_JARR("مِنْ", "min"),
 W("ثِيَابِكِ", "thawb", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", "hal"], J(MAJR, IDF("كِ"), Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «ثِيَابِي»، وَيَجُوزُ تَعْلِيقُهُمَا بِـ«تَنْسُلِ»", "the jarr phrase hangs on an omitted hal of «my garments», or on «slip away»", "câr-mecrûr «ثِيَابِي»den mahzûf hâle müteallik; «تَنْسُلِ»e bağlanması da câizdir")), s=[("ثِيَابِ", "thawb", "noun"), P("كِ")]),
 T("تَنْسُلِ", "nasala", "verb", ["jawab-al-talab", "thulathi-mujarrad-babs", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الْأَمْرِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الثِّيَابِ — النُّسُولُ: سُقُوطُ الرِّيشِ وَالْوَبَرِ وَالشَّعَرِ؛ وَيُرْوَى «تَنْسَلِي» مِنَ الِانْسِلَاءِ بِمَعْنَى التَّسَلِّي.",
   "A present verb in jazm as the answer of the command, its sign the sukun, voweled with kasra for the rhyme; its doer is a hidden «they», the garments — النُّسُول is the falling out of feathers, fur or hair; it is also transmitted تَنْسَلِي, «be consoled».",
   "Emrin cevabında meczûm muzâri; cezm alâmeti sükûn, kafiye için kesre ile harekelenmiş; fâili elbiselere dönen gizli «hiye» — النُّسُول: tüyün, yünün, kılın dökülmesi; teselli bulmak anlamında «تَنْسَلِي» de rivayet edilir.", "."),
])
V(None, 22, "Your eyes shed their tears only that you might strike, with your two arrows, the pieces of a heart already brought low.",
  "Gözlerin, ancak iki okunla, iyice boyun eğdirilmiş bir kalbin parçalarına vurasın diye yaş döktü.", [
 T("وَمَا", "ma-nafiya", "part", ["qasr", "turuq-al-qasr"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمَا نَافِيَةٌ — وَالنَّفْيُ مَعَ «إِلَّا» طَرِيقُ قَصْرٍ: قَصَرَ ذَرْفَ عَيْنَيْهَا عَلَى هٰذِهِ الْعِلَّةِ.", "The waw opens a new sentence; مَا negates — and negation with إِلَّا is a way of restriction (qaṣr): the shedding of her tears is confined to this one cause.", "Vâv istînâfiyye; مَا nefy içindir — nefy ile «إِلَّا» kasr yoludur: gözlerinin yaş dökmesini bu tek sebebe hasretmiştir.", s=[WA, ("مَا", "ma-nafiya", "part")]),
 W("ذَرَفَتْ", "dharafa", "verb", ["thulathi-mujarrad-babs"], J(MADI_F, Dn("ذَرَفَتِ الْعَيْنُ: سَالَ دَمْعُهَا", "ذَرَفَت of an eye: its tears flowed", "gözün «ذَرَفَتْ»i: yaşının akması"))),
 T("عَيْنَاكِ", "ayn-eye", "noun", ["fail", "al-muthanna", "idafa-definiteness"],
   "فَاعِلٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
   "The doer, in raf' by the alif — a dual; its nun falls for the annexation, and the kaf is its second term.",
   "Fâil, tesniye olduğu için elif ile merfû; nûnu izâfetle düşmüştür, kâf muzâfun ileyh.", s=[("عَيْنَا", "ayn-eye", "noun"), P("كِ")]),
 T("إِلَّا", "illa", "part", ["istithna-mufarragh", "qasr", "turuq-al-qasr"], "أَدَاةُ حَصْرٍ.", "The particle of restriction.", "Hasr edatı."),
 T("لِتَضْرِبِي", "daraba", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "afal-khamsa"],
   "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَتَضْرِبِي فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ جَوَازًا وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ، مُتَعَلِّقٌ بِـ«ذَرَفَتْ».",
   "The lam is the lam of purpose, a jarr letter; تَضْرِبِي is a present verb in nasb by an أَنْ that may stay unspoken, its sign the dropped nun; the ya is the doer, in the seat of raf' — the masdar so built is in jarr by the lam and hangs on «shed».",
   "Lâm ta'lîl lâmı, cer harfi; تَضْرِبِي cevâzen gizli أَنْ ile mansûb muzâri, nasb alâmeti nûnun hazfi; yâ fâil, mahallen merfû — müevvel masdar lâm ile mecrûr, «ذَرَفَتْ»e müteallik.", HEMI, [LI, ("تَضْرِبِي", "daraba", "verb")]),
 T("بِسَهْمَيْكِ", "sahm", "noun", ["huruf-jarr", "al-muthanna", "idafa-definiteness", "istiara", "arkan-al-istiara"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَسَهْمَيْ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَضْرِبِي». قَالَ الزَّوْزَنِيُّ: قَالَ الْأَكْثَرُونَ: اسْتَعَارَ لِلَحْظِ عَيْنَيْهَا وَدَمْعِهِمَا اسْمَ السَّهْمِ لِتَأْثِيرِهِمَا فِي الْقُلُوبِ وَجَرْحِهِمَا إِيَّاهَا — فَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ؛ وَقَالَ آخَرُونَ: أَرَادَ بِالسَّهْمَيْنِ الْمُعَلَّى وَالرَّقِيبَ مِنْ سِهَامِ الْمَيْسِرِ.",
   "The ba is a jarr letter; سَهْمَيْ is in jarr by the ya — a dual; its nun falls for the annexation, and the kaf is its second term. The phrase hangs on «strike». Al-Zawzanī: most say he borrowed the name of the arrow for the glance of her eyes and their tears, because they work upon hearts and wound them — an explicit istiʿāra; others say he means the two arrows al-Muʿallā and al-Raqīb of the maysir game.",
   "Bâ cer harfi; سَهْمَيْ tesniye olduğu için yâ ile mecrûr, nûnu izâfetle düşmüş, kâf muzâfun ileyh. Câr-mecrûr «تَضْرِبِي»ye müteallik. Zevzenî: çoğunluğa göre, gözlerinin bakışı ve yaşı kalplere tesir edip onları yaraladığı için bunlara ok adını istiâre etmiştir — istiâre-i tasrîhiyyedir; başkalarına göre ise iki okla meysir oklarından Muallâ ile Rakîb'i kastetmiştir.", s=[BI, ("سَهْمَيْ", "sahm", "noun"), P("كِ")]),
 HARF_JARR("فِي", "fi"),
 W("أَعْشَارِ", "ashar-pieces", "noun", ["huruf-jarr", "idafa-definiteness"], J(MAJR, MUD, TA("تَضْرِبِي", "strike", "ye"), Dn("الْأَعْشَارُ: الْقِطَعُ، مِنْ قَوْلِهِمْ: بُرْمَةٌ أَعْشَارٌ إِذَا كَانَتْ قِطَعًا، وَلَا وَاحِدَ لَهَا مِنْ لَفْظِهَا", "الأَعْشَار: pieces — from بُرْمَةٌ أَعْشَارٌ, a pot in fragments; it has no singular of its own form", "الأَعْشَار: parçalar — parça parça olmuş çömlek için söylenen «بُرْمَةٌ أَعْشَارٌ»dan; kendi lafzından tekili yoktur"))),
 W("قَلْبٍ", "qalb", "noun", ["idafa-definiteness"], J(MI)),
 W("مُقَتَّلِ", "muqattal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ لِـ«قَلْبٍ» مَجْرُورٌ بِالْكَسْرَةِ", "An adjective of «a heart», in jarr by the kasra", "«قَلْبٍ»in na'tı, kesre ile mecrûr"), QAFIYA, Dn("الْمُقَتَّلُ: الْمُذَلَّلُ غَايَةَ التَّذْلِيلِ", "المُقَتَّل: utterly subdued", "المُقَتَّل: iyice boyun eğdirilmiş")), "."),
])
V(None, 23, "Many a lady of the curtained tent — an egg in its covert, whose tent none may approach — I have enjoyed dalliance with, unhurried.",
  "Çadırına yaklaşılamayan, perde ardında yumurta gibi korunan nice hanımla acele etmeden hoşça vakit geçirdim.", [
 T("وَبَيْضَةِ", "bayda-egg", "noun", ["al-lam-wa-rubba-fil-kafiya", "anwa-al-waw", "mubtada-khabar", "idafa-definiteness", "istiara", "arkan-al-istiara"],
   "الْوَاوُ وَاوُ رُبَّ، وَبَيْضَةِ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ، مُضَافٌ. أَيْ: وَرُبَّ امْرَأَةٍ لَزِمَتْ خِدْرَهَا، ثُمَّ شَبَّهَهَا بِالْبَيْضِ — فَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ قَرِينَتُهَا الْإِضَافَةُ إِلَى الْخِدْرِ، وَالْجَامِعُ: السَّلَامَةُ، أَوِ الصِّيَانَةُ وَالسِّتْرُ، أَوْ صَفَاءُ اللَّوْنِ وَنَقَاؤُهُ.",
   "The waw is the waw of رُبَّ; بَيْضَةِ is the mubtada, in raf' by a damma that the near-redundant jarr letter's vowel keeps from showing; annexed. That is: many a woman who kept to her tent — and he likens her to an egg (al-Zawzanī). So it is an explicit istiʿāra, its clue the annexing to «tent», and what joins the two is soundness, or being guarded and screened, or clearness and purity of colour.",
   "Vâv, vâv-ı rubbe; بَيْضَةِ mübteda; zâide benzeyen cer harfinin harekesi mahalli meşgul ettiği için takdîrî damme ile merfû; muzâf. Yani: çadırından çıkmayan nice kadın — sonra onu yumurtaya benzetmiştir (Zevzenî). Demek ki istiâre-i tasrîhiyyedir; karînesi «خِدْر»e izâfettir; câmi ise selâmet, yahut korunup örtülü olmak, yahut rengin duruluğu ve temizliğidir.", s=[WA, ("بَيْضَةِ", "bayda-egg", "noun")]),
 W("خِدْرٍ", "khidr", "noun", ["idafa-definiteness"], J(MI)),
 T("لَا", "la-nafiya", "part", ["la-nafiya"], "نَافِيَةٌ.", "The negating لَا.", "Nefy lâsı."),
 W("يُرَامُ", "rama-seek", "verb", ["mudari-marfu", "hollow-verbs", "naib-al-fail"], J(("فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ", "A present verb in the passive, in raf' by the damma", "Damme ile merfû meçhul muzâri"), Dn("الرَّوْمُ: الطَّلَبُ", "الرَّوْم: seeking, making for", "الرَّوْم: istemek, kastetmek"))),
 W("خِبَاؤُهَا", "khiba", "noun", ["naib-al-fail", "idafa-definiteness", "ism-mamdud", "jumla-sifa"], J(("نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ", "The deputy doer, in raf' by the damma", "Nâib-i fâil, damme ile merfû"), IDF("هَا"), Dn("وَالْجُمْلَةُ نَعْتٌ لِـ«بَيْضَةِ خِدْرٍ»؛ الْخِبَاءُ: الْبَيْتُ مِنْ صُوفٍ أَوْ وَبَرٍ أَوْ شَعَرٍ", "the clause qualifies «a lady of the tent»; الخِبَاء: a tent of wool, camel-hair or goat-hair", "cümle «بَيْضَةِ خِدْرٍ»in na'tıdır; الخِبَاء: yünden veya kıldan çadır")), HEMI, [("خِبَاؤُ", "khiba", "noun"), P("هَا")]),
 W("تَمَتَّعْتُ", "tamattaa", "verb", ["form-v-verbs", "al-bariz-al-muttasil", "mubtada-khabar"], J(MADI_TU, Dn("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ", "the clause is the predicate of the mubtada, in the seat of raf'", "cümle mübtedanın haberi olarak mahallen merfû"))),
 HARF_JARR("مِنْ", "min"),
 W("لَهْوٍ", "lahw", "noun", ["huruf-jarr", "masdar"], J(MAJR, TA("تَمَتَّعْتُ", "I have enjoyed", "ya"))),
 PJ("بِهَا", "بِ", "bi", "هَا", BA3, "لَهْوٍ", "dalliance", "e", extra=(" لِأَنَّهُ مَصْدَرٌ", ", a masdar", " (masdar olduğu için)")),
 T("غَيْرَ", "ghayr", "noun", ["hal", "idafa-definiteness"], "حَالٌ مِنْ فَاعِلِ «تَمَتَّعْتُ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَيُرْوَى بِالْجَرِّ نَعْتًا لِـ«لَهْوٍ».", "A hal of the doer of «I have enjoyed», in nasb by the fatha, annexed — it is also transmitted in jarr, as an adjective of «dalliance».", "«تَمَتَّعْتُ»nun fâilinden hâl, fetha ile mansûb, muzâf — «لَهْوٍ»in na'tı olarak cer ile de rivayet edilir."),
 W("مُعْجَلِ", "mujal", "noun", ["idafa-definiteness", "ism-maful", "al-qafiya"], J(MI, QAFIYA, Dn("اسْمُ مَفْعُولٍ مِنْ «أَعْجَلَ»، أَيْ: عَلَى تَمَكُّثٍ لَمْ أُعْجَلْ عَنْهَا", "the ism maf'ul of أَعْجَلَ: at my leisure, not hurried away from her", "«أَعْجَلَ»den ism-i mef'ûl: acele ettirilmeden, ağır ağır")), "."),
])
V(None, 24, "I passed, on my way to her, guards and kinsmen eager against me — eager to kill me, could they do it unseen —",
  "Ona giderken bekçileri ve beni gizlice öldürebilseler buna pek hırslı olan bir topluluğu aşıp geçtim;", [
 W("تَجَاوَزْتُ", "tajawaza-v", "verb", ["form-vi-verbs", "al-bariz-al-muttasil"], J(MADI_TU, Dn("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ ثَانٍ لِلْمُبْتَدَإِ «بَيْضَةِ خِدْرٍ»، أَوْ مُسْتَأْنَفَةٌ", "the clause is a second predicate of the mubtada «a lady of the tent», in the seat of raf', or a fresh sentence", "cümle «بَيْضَةِ خِدْرٍ» mübtedasının ikinci haberi olarak mahallen merfû, ya da müste'nefedir"))),
 W("أَحْرَاسًا", "haris-guard", "noun", ["maful-bihi", "jam-taksir"], J(MAFR, Dn("جَمْعُ حَارِسٍ كَصَاحِبٍ وَأَصْحَابٍ، أَوْ جَمْعُ حَرَسٍ", "the plural of حَارِس (as أَصْحَاب of صَاحِب), or of حَرَس", "«حَارِس»in cem'i (sâhib–ashâb gibi), yahut «حَرَس»in cem'i"))),
 PJ("إِلَيْهَا", "إِلَيْ", "ila", "هَا", ILA3, "تَجَاوَزْتُ", "I passed", "ya"),
 W("وَمَعْشَرًا", "mashar", "noun", ["atf-nasaq"], J(PRE("wa", "مَعْشَرًا"), ("مَعْطُوفٌ عَلَى «أَحْرَاسًا» مَنْصُوبٌ بِالْفَتْحَةِ", "conjoined to «guards», in nasb by the fatha", "«أَحْرَاسًا»ya ma'tûf, fetha ile mansûb"), Dn("الْمَعْشَرُ: الْقَوْمُ", "المَعْشَر: a people, a kindred", "المَعْشَر: topluluk")), HEMI, [WA, ("مَعْشَرًا", "mashar", "noun")]),
 PJ("عَلَيَّ", "عَلَيْ", "ala", "يَ", ALA3, "حِرَاصًا", "eager", "ya", g=["huruf-jarr", "ya-al-mutakallim"]),
 W("حِرَاصًا", "haris", "noun", ["naat-sifa", "jam-taksir", "sifa-mushabbaha"], J(("نَعْتٌ لِـ«مَعْشَرًا» مَنْصُوبٌ بِالْفَتْحَةِ", "An adjective of «kinsmen», in nasb by the fatha", "«مَعْشَرًا»nın na'tı, fetha ile mansûb"), Dn("جَمْعُ حَرِيصٍ كَكَرِيمٍ وَكِرَامٍ", "the plural of حَرِيص (as كِرَام of كَرِيم)", "«حَرِيص»in cem'i (kerîm–kirâm gibi)"))),
 T("لَوْ", "law-masdariyya", "part", ["an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ.", "A particle that turns its clause into a masdar.", "Masdar harfi."),
 T("يُسِرُّونَ", "asarra", "verb", ["afal-khamsa", "form-iv-verbs", "doubled-verbs", "badal"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْ «لَوْ» وَالْفِعْلِ بَدَلُ اشْتِمَالٍ مِنْ يَاءِ «عَلَيَّ»، أَيْ: حِرَاصًا عَلَى إِسْرَارِ مَقْتَلِي. الْإِسْرَارُ: الْإِظْهَارُ وَالْإِضْمَارُ جَمِيعًا، وَهُوَ مِنَ الْأَضْدَادِ؛ وَالْأَوْلَى حَمْلُهُ عَلَى الْإِخْفَاءِ.",
   "A present verb in raf' by keeping its nun — one of the five verbs; the waw is the doer, in the seat of raf'. The masdar made by لَوْ and the verb is a badal of inclusion of the ya in «against me»: «eager for the hiding of my killing». الإِسْرَار is both «showing» and «hiding» — a word of two opposite senses; al-Zawzanī prefers «hiding» here.",
   "Ef'âl-i hamseden olduğu için nûnun sübûtuyla merfû muzâri; vâv fâil, mahallen merfû. «لَوْ» ile fiilden oluşan müevvel masdar «عَلَيَّ»deki yâ'dan bedel-i iştimâldir: «öldürülmemi gizlemeye hırslı». الإِسْرَار hem «açığa vurmak» hem «gizlemek» demektir, ezdâddandır; Zevzenî burada «gizlemek» anlamını tercih eder."),
 W("مَقْتَلِي", "maqtal", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "masdar", "al-qafiya"], J(("مَفْعُولٌ بِهِ مَنْصُوبٌ ", "The direct object, in nasb by ", "Mef'ûlün bih; "), YA_EST("بِفَتْحَةٍ", "a fatha", "fetha ile mansûb"), Dn("مَصْدَرٌ مِيمِيٌّ مُضَافٌ إِلَى مَفْعُولِهِ، أَيْ: قَتْلَهُمْ إِيَّايَ", "a masdar with mim annexed to its object: «their killing me»", "mef'ûlüne muzâf mîmli masdar: «beni öldürmelerini»")), "،", [("مَقْتَلِ", "maqtal", "noun"), P("ي")]),
])
V(None, 25, "at the hour when the Pleiades showed their flank in the sky, as the folds of a sash set with spaced gems show theirs.",
  "Süreyyâ gökte, araları (altınla) ayrılmış taşlı bir kuşağın kıvrımlarının görünüşü gibi yanını gösterdiği vakit.", [
 T("إِذَا", "idha", "part", ["maful-fih"], "ظَرْفُ زَمَانٍ مُجَرَّدٌ عَنِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«تَجَاوَزْتُ» فِي الْبَيْتِ قَبْلَهُ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time with no sense of condition, built on sukun in the seat of nasb; it hangs on «I passed» in the verse before and is annexed to the clause after it.", "Şart mânâsından soyutlanmış zaman zarfı; sükûn üzere mebnî, mahallen mansûb; önceki beyitteki «تَجَاوَزْتُ»ya müteallik, sonraki cümleye muzâf."),
 T("مَا", "ma-zaida", "part", ["anwa-ma"], MA_Z[0], MA_Z[1], MA_Z[2]),
 T("الثُّرَيَّا", "thurayya", "propn", ["fail", "hadhf-wa-taqdir", "ism-maqsur-manqus"],
   "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «تَعَرَّضَتْ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "The doer of an omitted verb that «showed their flank» explains, in raf' by a damma estimated on the alif — the clause is in the seat of jarr, annexed to إِذَا.",
   "«تَعَرَّضَتْ»in tefsir ettiği mahzûf bir fiilin fâili; elif üzerinde takdîrî damme ile merfû — cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr."),
 HARF_JARR("فِي", "fi"),
 W("السَّمَاءِ", "sama", "noun", ["huruf-jarr", "ism-mamdud"], J(MAJR, TA("تَعَرَّضَتْ", "showed their flank", "e"))),
 W("تَعَرَّضَتْ", "taarrada", "verb", ["form-v-verbs"], J(MADI_F, HID("هِيَ", "she", "hiye", ("الثُّرَيَّا", "the Pleiades", "Süreyyâ'ya")), Dn("وَالْجُمْلَةُ تَفْسِيرِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ التَّعَرُّضُ: إِبْدَاءُ الْعُرْضِ وَهُوَ النَّاحِيَةُ", "the clause explains the omitted verb and has no seat; التَّعَرُّض: showing one's side", "cümle tefsîriyyedir, i'râbdan mahalli yoktur; التَّعَرُّض: yanını göstermek")), HEMI),
 T("تَعَرُّضَ", "taarrud", "noun", ["maful-mutlaq", "idafa-definiteness", "masdar", "imal-al-masdar", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَالتَّقْدِيرُ: تَعَرُّضًا مِثْلَ تَعَرُّضِ أَثْنَاءِ الْوِشَاحِ. وَفِيهِ تَشْبِيهٌ بَلِيغٌ حُذِفَتْ أَدَاتُهُ وَوَجْهُهُ: شَبَّهَ نَوَاحِيَ كَوَاكِبِ الثُّرَيَّا عِنْدَ ظُهُورِهَا بِنَوَاحِي جَوَاهِرِ الْوِشَاحِ الْمُفَصَّلِ.",
   "An absolute object, in nasb by the fatha, annexed — in full: «a showing like the showing of the folds of the sash». A tashbih balīgh, with neither particle nor point of likeness: the sides of the stars of the Pleiades as they appear are likened to the sides of the gems of a sash whose beads are spaced out (al-Zawzanī).",
   "Mef'ûlün mutlak, fetha ile mansûb, muzâf — takdiri: «kuşağın kıvrımlarının görünüşü gibi bir görünüşle». Edatı ve vechi hazfedilmiş teşbih-i belîğ vardır: Süreyyâ yıldızlarının belirirkenki yanları, taşlarının arası ayrılmış bir kuşağın cevherlerinin yanlarına benzetilmiştir (Zevzenî)."),
 W("أَثْنَاءِ", "thiny", "noun", ["idafa-definiteness", "jam-taksir", "imal-al-masdar"], J(MI, MUD, Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الْأَثْنَاءُ: النَّوَاحِي وَالْأَوْسَاطُ، وَاحِدُهَا ثِنْيٌ", "the masdar annexed to its doer; الأَثْنَاء: the sides, the folds — singular ثِنْي", "masdarın fâiline izâfeti; الأَثْنَاء: yanlar, kıvrımlar — tekili ثِنْي"))),
 W("الْوِشَاحِ", "wishah", "noun", ["idafa-definiteness"], J(MI)),
 W("الْمُفَصَّلِ", "mufassal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ لِـ«الْوِشَاحِ» مَجْرُورٌ بِالْكَسْرَةِ", "An adjective of «the sash», in jarr by the kasra", "«الْوِشَاحِ»ın na'tı, kesre ile mecrûr"), Dn("الَّذِي فُصِلَ بَيْنَ خَرَزِهِ بِالذَّهَبِ أَوْ غَيْرِهِ", "one whose beads are set apart by gold or the like", "boncuklarının arası altın veya başka şeyle ayrılmış olan")), "."),
])

# =====================================================================================================================
# The visit by night: verses 26–31
# =====================================================================================================================
V(None, 26, "So I came, when she had put off her clothes for sleep, by the curtain — all but the single garment of one lightly clad.",
  "Vardığımda uyumak için perdenin yanında elbiselerini çıkarmış, üzerinde yalnız hafif giyinenin tek giysisini bırakmıştı.", [
 W("فَجِئْتُ", "jaa", "verb", ["atf-nasaq", "hollow-verbs", "al-bariz-al-muttasil"], J(PRE("fa", "جِئْتُ"), lo(MADI_TU), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «تَجَاوَزْتُ»", "the clause is conjoined to «I passed»", "cümle «تَجَاوَزْتُ» cümlesine ma'tûftur")), s=[FA, ("جِئْتُ", "jaa", "verb")]),
 T("وَقَدْ", "qad", "part", ["qad-harf", "al-hal-jumla-wa-rabituha", "anwa-al-waw"], "الْوَاوُ وَاوُ الْحَالِ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "The waw is the waw of the hal; قَدْ is a particle of certainty.", "Vâv hâliye; قَدْ tahkîk harfi.", s=[WA, ("قَدْ", "qad", "part")]),
 T("نَضَّتْ", "nadda", "verb", ["form-ii-verbs", "naqis-verbs", "al-hal-jumla-wa-rabituha"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «جِئْتُ». نَضَا الثِّيَابَ: خَلَعَهَا، وَنَضَّاهَا لِلْمُبَالَغَةِ.",
   "A past verb built on a fatha estimated on the alif, which falls where two still letters meet; the ta marks the feminine, and the doer is a hidden «she» — the clause is a hal of the doer of «I came», in the seat of nasb. نَضَا الثِّيَابَ: to take clothes off; نَضَّى is its intensive.",
   "İki sâkinin karşılaşması yüzünden düşen elif üzerinde takdîrî fetha üzere mebnî mâzî; tâ te'nîs için, fâili gizli «hiye» — cümle «جِئْتُ»nün fâilinden hâl olarak mahallen mansûb. نَضَا الثِّيَابَ: elbiseyi çıkarmak; نَضَّى onun mübalağasıdır."),
 T("لِنَوْمٍ", "nawm", "noun", ["huruf-jarr", "masdar"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَنَوْمٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَضَّتْ».", "The lam is a jarr letter of purpose and نَوْمٍ is in jarr by the kasra — the phrase hangs on «she had put off».", "Lâm ta'lîl bildiren cer harfi, نَوْمٍ kesre ile mecrûr — câr-mecrûr «نَضَّتْ»e müteallik.", s=[LI, ("نَوْمٍ", "nawm", "noun")]),
 W("ثِيَابَهَا", "thawb", "noun", ["maful-bihi", "idafa-definiteness", "jam-taksir"], J(MAFR, IDF("هَا")), HEMI, [("ثِيَابَ", "thawb", "noun"), P("هَا")]),
 T("لَدَى", "lada", "noun", ["maful-fih", "idafa-definiteness", "ism-maqsur-manqus"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ — مُتَعَلِّقٌ بِـ«نَضَّتْ».", "An adverb of place, in nasb by a fatha estimated on the alif, annexed — it hangs on «she had put off».", "Mekân zarfı; elif üzerinde takdîrî fetha ile mansûb, muzâf — «نَضَّتْ»e müteallik."),
 W("السِّتْرِ", "sitr", "noun", ["idafa-definiteness"], J(MI)),
 T("إِلَّا", "illa", "part", ["istithna"], "أَدَاةُ اسْتِثْنَاءٍ.", "The particle of exception.", "İstisnâ edatı."),
 T("لِبْسَةَ", "libsa", "noun", ["istithna", "idafa-definiteness"], "مُسْتَثْنًى مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اللِّبْسَةُ: هَيْئَةُ اللُّبْسِ، كَالْجِلْسَةِ وَالْقِعْدَةِ.", "The thing excepted, in nasb by the fatha, annexed — اللِّبْسَة: a manner of dress (a noun of manner, like الجِلْسَة).", "Müstesnâ, fetha ile mansûb, muzâf — اللِّبْسَة: giyiniş biçimi (ism-i hey'et; الجِلْسَة gibi)."),
 W("الْمُتَفَضِّلِ", "mutafaddil", "noun", ["idafa-definiteness", "ism-fail", "al-qafiya"], J(MI, Dn("الْمُتَفَضِّلُ: اللَّابِسُ ثَوْبًا وَاحِدًا", "المُتَفَضِّل: one who wears a single garment", "المُتَفَضِّل: tek bir giysi giyen")), "."),
])
V(None, 27, "She said: «By God's oath, there is no way to deal with you; nor do I see this folly lifting from you.»",
  "Dedi ki: «Allah'a yemin olsun, sana karşı elimden bir şey gelmiyor; bu sapkınlığın senden sıyrılıp gittiğini de görmüyorum.»", [
 W("فَقَالَتْ", "qala", "verb", ["atf-nasaq", "hollow-verbs"], J(PRE("fa", "قَالَتْ"), lo(MADI_F), HID("هِيَ", "she", "hiye")), ":", [FA, ("قَالَتْ", "qala", "verb")]),
 T("يَمِينَ", "yamin", "noun", ["hadhf-al-jarr", "hadhf-wa-taqdir", "idafa-definiteness"],
   "مَنْصُوبٌ بِالْفَتْحَةِ عَلَى إِضْمَارِ فِعْلِ الْقَسَمِ بَعْدَ نَزْعِ الْخَافِضِ، أَيْ: أَحْلِفُ بِيَمِينِ اللهِ، مُضَافٌ — وَيُرْوَى بِالرَّفْعِ مُبْتَدَأً خَبَرُهُ مَحْذُوفٌ.",
   "In nasb by the fatha: the verb of swearing is left unspoken and the jarr letter dropped — «I swear by God's oath»; annexed. It is also transmitted in raf', a mubtada whose predicate is left out.",
   "Yemin fiilinin gizlenmesi ve harf-i cerrin düşmesiyle fetha ile mansûb: «Allah'ın yeminiyle yemin ederim»; muzâf. Haberi mahzûf mübteda olarak ref' ile de rivayet edilir."),
 T("اللهِ", "allah", "propn", ["idafa-definiteness"], "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.", "The Name of Majesty, the second term of the idafa, in jarr by the kasra.", "Lafza-i celâl, muzâfun ileyh, kesre ile mecrûr."),
 T("مَا", "ma-nafiya", "part", ["ma-la-mushabbaha"], "نَافِيَةٌ لَا عَمَلَ لَهَا.", "The negating مَا; it governs nothing here.", "Nefy edatı mâ; burada amel etmez."),
 T("لَكَ", "li", "prep", ["huruf-jarr", "taqdim-al-musnad"], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.", "The lam is a jarr letter and the kaf is in the seat of jarr — the phrase hangs on an omitted predicate, set first.", "Lâm cer harfi, kâf mahallen mecrûr — câr-mecrûr öne geçmiş mahzûf habere müteallik.", s=[("لَ", "li", "prep"), P("كَ")]),
 T("حِيلَةٌ", "hila", "noun", ["mubtada-khabar"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ أَيْ: مَا لِي لِدَفْعِكَ عَنِّي حِيلَةٌ، وَقِيلَ: مَا لَكَ عُذْرٌ وَحُجَّةٌ فِي زِيَارَتِي.",
   "The mubtada, placed last, in raf' by the damma — the clause answers the oath and has no seat. That is: «I have no means of putting you off»; or, it is said: «you have no excuse for visiting me» (al-Zawzanī).",
   "Sona bırakılmış mübteda, damme ile merfû — cümle yeminin cevabıdır, i'râbdan mahalli yoktur. Yani: «seni kendimden uzaklaştırmaya çarem yok»; «beni ziyaret etmende hiçbir mazeretin yok» da denmiştir (Zevzenî).", HEMI),
 T("وَمَا", "ma-nafiya", "part", ["atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَمَا نَافِيَةٌ.", "The waw conjoins; مَا negates.", "Vâv atıf; مَا nefy içindir.", s=[WA, ("مَا", "ma-nafiya", "part")]),
 T("إِنْ", "in-zaida", "part", ["huruf-al-ziyada-fil-kafiya"], "زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ، وَهِيَ تُزَادُ مَعَ «مَا» النَّافِيَةِ.", "Added to strengthen the negation — it is added after the negating مَا.", "Nefyi pekiştirmek için zâid; nefy «مَا»sından sonra ziyade kılınır."),
 W("أَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs"], J(("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A present verb in raf' by a damma estimated on the alif", "Elif üzerinde takdîrî damme ile merfû muzâri"), HID("أَنَا", "I", "ene"))),
 PJ("عَنْكَ", "عَنْ", "an", "كَ", ("عَنْ", "عَنْ", "عَنْ"), "تَنْجَلِي", "lifting", "ye"),
 W("الْغَوَايَةَ", "ghawaya", "noun", ["maful-bihi", "masdar"], J(MAFR, Dn("الْغَوَايَةُ وَالْغَيُّ: الضَّلَالَةُ، أَيْ: ضَلَالُ الْعِشْقِ", "الغَوَايَة, like الغَيّ: going astray — here the folly of passion", "الغَوَايَة, «الغَيّ» gibi: sapkınlık — burada aşkın şaşkınlığı"))),
 T("تَنْجَلِي", "injala", "verb", ["mudari-marfu", "form-vii-verbs", "naqis-verbs", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «الْغَوَايَةَ» — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ لِـ«أَرَى» إِنْ كَانَتْ عِلْمِيَّةً، أَوْ حَالٌ إِنْ كَانَتْ بَصَرِيَّةً. قَالَ الرُّوَاةُ: هٰذَا أَغْنَجُ بَيْتٍ فِي الشِّعْرِ.",
   "A present verb in raf' by a damma estimated on the ya (too heavy to voice); its doer is a hidden «it» returning to «the folly» — the clause is the second object of «I see», if it is seeing with the mind, or a hal, if it is seeing with the eye. The transmitters said: this is the most coquettish verse in poetry (al-Zawzanī).",
   "Yâ üzerinde ağırlık sebebiyle takdîrî damme ile merfû muzâri; fâili «الْغَوَايَةَ»ye dönen gizli «hiye» — cümle, «أَرَى» ilim anlamındaysa ikinci mef'ûl, görme anlamındaysa hâl olarak mahallen mansûb. Râvîler demiştir ki: bu, şiirdeki en nazlı beyittir (Zevzenî).", "."),
])
V(None, 28, "I led her out, walking, while she trailed behind us, over our two tracks, the skirt of a figured wrap.",
  "Onu dışarı çıkardım; ben yürüyordum, o da ardımızda, ikimizin izleri üzerinde nakışlı örtüsünün eteğini sürüyordu.", [
 W("خَرَجْتُ", "kharaja", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil"], J(MADI_TU, Dn("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "a fresh sentence", "cümle müste'nefedir"))),
 PJ("بِهَا", "بِ", "bi", "هَا", BA3, "خَرَجْتُ", "I went out", "ya", extra=("؛ وَالْبَاءُ لِلتَّعْدِيَةِ، أَيْ: أَخْرَجْتُهَا مِنْ خِدْرِهَا", "; the ba makes the verb transitive: «I brought her out of her tent»", "; bâ ta'diye içindir: «onu çadırından çıkardım»")),
 W("أَمْشِي", "masha", "verb", ["mudari-marfu", "naqis-verbs", "al-hal-jumla-wa-rabituha"], J(("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "A present verb in raf' by a damma estimated on the ya", "Yâ üzerinde takdîrî damme ile merfû muzâri"), HID("أَنَا", "I", "ene"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «خَرَجْتُ»", "the clause is a hal of the doer of «I went out», in the seat of nasb", "cümle «خَرَجْتُ»nun fâilinden hâl olarak mahallen mansûb"))),
 W("تَجُرُّ", "jarra", "verb", ["mudari-marfu", "doubled-verbs", "al-hal-jumla-wa-rabituha"], J(MUDR, HID("هِيَ", "she", "hiye"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ فِي «بِهَا»", "the clause is a hal of the pronoun in «with her», in the seat of nasb", "cümle «بِهَا»daki zamirden hâl olarak mahallen mansûb"))),
 T("وَرَاءَنَا", "wara", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مُتَعَلِّقٌ بِـ«تَجُرُّ».", "An adverb of place, in nasb by the fatha, annexed; نَا is its second term — it hangs on «trailed».", "Mekân zarfı, fetha ile mansûb, muzâf; نَا muzâfun ileyh — «تَجُرُّ»ya müteallik.", HEMI, [("وَرَاءَ", "wara", "noun"), P("نَا")]),
 HARF_JARR("عَلَى", "ala"),
 T("أَثَرَيْنَا", "athar", "noun", ["huruf-jarr", "al-muthanna", "idafa-definiteness"],
   "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَجُرُّ»؛ تَجُرُّ مِرْطَهَا عَلَى أَثَرِهِمَا لِتُعَفِّيَ بِهِ آثَارَ أَقْدَامِهِمَا.",
   "In jarr by the ya — a dual; its nun falls for the annexation, and نَا is its second term. The phrase hangs on «trailed»: she drags her wrap over their tracks to wipe out their footprints (al-Zawzanī).",
   "Tesniye olduğu için yâ ile mecrûr; nûnu izâfetle düşmüş, نَا muzâfun ileyh. Câr-mecrûr «تَجُرُّ»ya müteallik: ayak izlerini silmek için örtüsünü izlerinin üzerinde sürür (Zevzenî).", s=[("أَثَرَيْ", "athar", "noun"), P("نَا")]),
 W("ذَيْلَ", "dhayl", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, MUD)),
 W("مِرْطٍ", "mirt", "noun", ["idafa-definiteness"], J(MI, Dn("الْمِرْطُ: كِسَاءٌ مِنْ خَزٍّ أَوْ صُوفٍ", "المِرْط: a wrap of silk-wool or of wool", "المِرْط: ipekli veya yünlü örtü"))),
 W("مُرَحَّلِ", "murahhal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ لِـ«مِرْطٍ» مَجْرُورٌ بِالْكَسْرَةِ", "An adjective of «a wrap», in jarr by the kasra", "«مِرْطٍ»ın na'tı, kesre ile mecrûr"), QAFIYA, Dn("الْمُرَحَّلُ: الْمُنَقَّشُ بِنُقُوشٍ تُشْبِهُ رِحَالَ الْإِبِلِ", "المُرَحَّل: worked with figures like camel-saddles", "المُرَحَّل: deve semerlerine benzer nakışlarla işlenmiş")), "."),
])
V(None, 29, "Then, when we had crossed the tribe's open ground, and the hollow of a low tract, with its curving dunes of banked sand, had drawn us in,",
  "Kabilenin meydanını geçip de eğri kum tepeleriyle çevrili, kumu kümelenmiş alçak bir düzlüğün içi bizi kendine çekince,", [
 T("فَلَمَّا", "lamma", "part", ["atf-nasaq", "maful-fih"],
   "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفُ زَمَانٍ بِمَعْنَى «حِينَ» مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ — وَجَوَابُهُ «هَصَرْتُ» فِي الْبَيْتِ بَعْدَهُ عِنْدَ الْبَصْرِيِّينَ.",
   "The fa conjoins; لَمَّا is an adverb of time, «when», with the sense of a condition, built on sukun in the seat of nasb and annexed to the clause after it — its answer, for the Basrans, is «I drew» in the next verse.",
   "Fâ atıf; لَمَّا şart mânâsı taşıyan «-ince» anlamında zaman zarfı; sükûn üzere mebnî, mahallen mansûb, sonraki cümleye muzâf — Basralılara göre cevabı sonraki beyitteki «هَصَرْتُ»dur.", s=[FA, ("لَمَّا", "lamma", "part")]),
 T("أَجَزْنَا", "ajaza-cross", "verb", ["form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا» الْفَاعِلِينَ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «لَمَّا» إِلَيْهَا؛ أَجَازَ الْمَكَانَ وَجَازَهُ: قَطَعَهُ.",
   "A past verb built on sukun because the doers' نَا is attached; نَا is the doer, in the seat of raf' — the clause is in the seat of jarr, annexed to لَمَّا; أَجَازَ الْمَكَانَ, like جَازَهُ: to pass through a place.",
   "Fâil «نَا»sına bitiştiği için sükûn üzere mebnî mâzî; نَا fâil, mahallen merfû — cümle «لَمَّا»nın muzâfun ileyhi olarak mahallen mecrûr; أَجَازَ الْمَكَانَ, «جَازَهُ» gibi: bir yeri geçmek."),
 W("سَاحَةَ", "saha-court", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, MUD)),
 W("الْحَيِّ", "hayy-tribe", "noun", ["idafa-definiteness"], J(MI)),
 T("وَانْتَحَى", "intaha-lean", "verb", ["atf-nasaq", "form-viii-verbs", "naqis-verbs"],
   "الْوَاوُ عَاطِفَةٌ، وَانْتَحَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «أَجَزْنَا»؛ وَزَعَمَ أَبُو عُبَيْدَةَ وَأَكْثَرُ الْكُوفِيِّينَ أَنَّ الْوَاوَ زَائِدَةٌ مُقْحَمَةٌ وَأَنَّ «انْتَحَى» جَوَابُ «لَمَّا». الِانْتِحَاءُ: الِاعْتِمَادُ عَلَى الشَّيْءِ.",
   "The waw conjoins; انْتَحَى is a past verb built on a fatha estimated on the alif — the clause is conjoined to «we had crossed». Abū ʿUbayda and most Kufans hold that the waw is an added one and that this verb is the answer of لَمَّا. الاِنْتِحَاء: to lean, to bear upon a thing.",
   "Vâv atıf; انْتَحَى elif üzerinde takdîrî fetha üzere mebnî mâzî — cümle «أَجَزْنَا» cümlesine ma'tûftur. Ebû Ubeyde ve Kûfelilerin çoğu, vâvın zâid olduğunu ve bu fiilin «لَمَّا»nın cevabı olduğunu söyler. الاِنْتِحَاء: bir şeye yaslanmak, yönelmek.", HEMI, [WA, ("انْتَحَى", "intaha-lean", "verb")]),
 PJ("بِنَا", "بِ", "bi", "نَا", BA3, "انْتَحَى", "drew in", "ya"),
 T("بَطْنُ", "batn", "noun", ["fail", "idafa-definiteness", "majaz-aqli"],
   "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — الْبَطْنُ: مَكَانٌ مُطْمَئِنٌّ حَوْلَهُ أَمَاكِنُ مُرْتَفِعَةٌ. قَالَ الزَّوْزَنِيُّ: أَسْنَدَ الْفِعْلَ إِلَى بَطْنِ خَبْتٍ وَالْفِعْلُ عِنْدَ التَّحْقِيقِ لَهُمَا، وَلٰكِنَّهُ ضَرْبٌ مِنَ الِاتِّسَاعِ فِي الْكَلَامِ، وَالْمَعْنَى: صِرْنَا إِلَى مِثْلِ هٰذَا الْمَكَانِ — فَهُوَ مَجَازٌ عَقْلِيٌّ عَلَاقَتُهُ الْمَكَانِيَّةُ.",
   "The doer, in raf' by the damma, annexed — البَطْن: a sunken place with higher ground about it. Al-Zawzanī: he ascribes the verb to «the hollow of a low tract», though in truth the act is theirs — a widening of usage, the sense being «we came to such a place». So it is a majaz ʿaqlī whose tie is place.",
   "Fâil, damme ile merfû, muzâf — البَطْن: çevresi yüksek, kendisi çukur yer. Zevzenî: fiili «çukur düzlüğün içi»ne isnad etmiştir, oysa fiil gerçekte o ikisine aittir; bu, sözde bir genişletmedir, mânâ «böyle bir yere vardık» demektir. Demek ki alâkası mekâniyet olan mecâz-ı aklîdir."),
 W("خَبْتٍ", "khabt-ground", "noun", ["idafa-definiteness"], J(MI, Dn("الْخَبْتُ: أَرْضٌ مُطْمَئِنَّةٌ", "الخَبْت: low, level ground", "الخَبْت: alçak, düz arazi"))),
 W("ذِي", "dhu", "noun", ["naat-sifa", "five-nouns", "idafa-definiteness"], J(("نَعْتٌ لِـ«خَبْتٍ» مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ", "An adjective of «a low tract», in jarr by the ya — one of the five nouns", "«خَبْتٍ»in na'tı, esmâ-i hamseden olduğu için yâ ile mecrûr"), MUD)),
 W("حِقَافٍ", "hiqf", "noun", ["idafa-definiteness", "jam-taksir"], J(MI, Dn("جَمْعُ حِقْفٍ: رَمْلٌ مُشْرِفٌ مُعْوَجٌّ؛ وَيُرْوَى «قِفَافٍ»", "the plural of حِقْف, a high curving ridge of sand; also transmitted قِفَافٍ", "«حِقْف»in cem'i: yüksek, eğri kum sırtı; «قِفَافٍ» de rivayet edilir"))),
 W("عَقَنْقَلِ", "aqanqal", "noun", ["naat-sifa", "al-qafiya"], J(("نَعْتٌ ثَانٍ لِـ«خَبْتٍ» مَجْرُورٌ بِالْكَسْرَةِ", "A second adjective of «a low tract», in jarr by the kasra", "«خَبْتٍ»in ikinci na'tı, kesre ile mecrûr"), QAFIYA, Dn("الْعَقَنْقَلُ: الرَّمْلُ الْمُنْعَقِدُ الْمُتَلَبِّدُ", "العَقَنْقَل: sand knotted and banked together", "العَقَنْقَل: birbirine girip kümelenmiş kum")), "،"),
])
V(None, 30, "I drew her to me by the two sides of her head, and she swayed towards me — slender of waist, full at the ankle.",
  "Başının iki yanından tutup kendime çektim; o da bana doğru eğildi — beli ince, halhal yeri dolgun.", [
 W("هَصَرْتُ", "hasara-pull", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil"], J(MADI_TU, Dn("وَالْجُمْلَةُ جَوَابُ «لَمَّا» لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ الْهَصْرُ: الْجَذْبُ", "the clause answers لَمَّا and has no seat; الهَصْر: pulling, drawing down", "cümle «لَمَّا»nın cevabıdır, i'râbdan mahalli yoktur; الهَصْر: çekmek"))),
 T("بِفَوْدَيْ", "fawd", "noun", ["huruf-jarr", "al-muthanna", "idafa-definiteness"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَفَوْدَيْ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«هَصَرْتُ»؛ الْفَوْدَانِ: جَانِبَا الرَّأْسِ.",
   "The ba is a jarr letter; فَوْدَيْ is in jarr by the ya — a dual; its nun falls for the annexation; annexed. The phrase hangs on «I drew»; الفَوْدَانِ: the two sides of the head.",
   "Bâ cer harfi; فَوْدَيْ tesniye olduğu için yâ ile mecrûr, nûnu izâfetle düşmüş, muzâf. Câr-mecrûr «هَصَرْتُ»ya müteallik; الفَوْدَانِ: başın iki yanı.", s=[BI, ("فَوْدَيْ", "fawd", "noun")]),
 W("رَأْسِهَا", "ras", "noun", ["idafa-definiteness"], J(MI, IDF("هَا")), s=[("رَأْسِ", "ras", "noun"), P("هَا")]),
 W("فَتَمَايَلَتْ", "tamayala", "verb", ["atf-nasaq", "form-vi-verbs"], J(PRE("fa", "تَمَايَلَتْ"), lo(MADI_F), HID("هِيَ", "she", "hiye"), Dn("تَمَايَلَتْ أَيْ: مَالَتْ", "تَمَايَلَتْ: she leaned over", "تَمَايَلَتْ: eğildi")), HEMI, [FA, ("تَمَايَلَتْ", "tamayala", "verb")]),
 PJ("عَلَيَّ", "عَلَيْ", "ala", "يَ", ALA3, "تَمَايَلَتْ", "she swayed", "e", g=["huruf-jarr", "ya-al-mutakallim"]),
 T("هَضِيمَ", "hadim", "noun", ["hal", "idafa-definiteness", "idafa-lafziyya"],
   "حَالٌ مِنْ فَاعِلِ «تَمَايَلَتْ» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَلَمْ يَقُلْ «هَضِيمَةَ» لِأَنَّ فَعِيلًا إِذَا كَانَ بِمَعْنَى مَفْعُولٍ لَمْ تَلْحَقْهُ عَلَامَةُ التَّأْنِيثِ؛ هَضِيمُ الْكَشْحِ: ضَامِرُهُ.",
   "A hal of the doer of «she swayed», in nasb by the fatha, annexed — he does not say هَضِيمَة, because فَعِيل in the sense of مَفْعُول takes no feminine mark (al-Zawzanī); «هَضِيم of waist»: slender there.",
   "«تَمَايَلَتْ»in fâilinden hâl, fetha ile mansûb, muzâf — «هَضِيمَة» dememiştir; çünkü mef'ûl anlamındaki «فَعِيل» te'nîs alâmeti almaz (Zevzenî); «beli هَضِيم»: beli ince."),
 W("الْكَشْحِ", "kashh", "noun", ["idafa-definiteness"], J(MI, Dn("الْكَشْحُ: مُنْقَطَعُ الْأَضْلَاعِ، الْخَصْرُ", "الكَشْح: where the ribs end, the waist", "الكَشْح: kaburgaların bittiği yer, bel"))),
 T("رَيَّا", "rayyan", "noun", ["hal", "ism-maqsur-manqus", "idafa-definiteness", "idafa-lafziyya", "sifa-mushabbaha", "istiara", "istiara-tabaiyya"],
   "حَالٌ ثَانِيَةٌ مَنْصُوبَةٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ — تَأْنِيثُ «الرَّيَّانِ». قَالَ الزَّوْزَنِيُّ: عَبَّرَ عَنْ كَثْرَةِ لَحْمِ السَّاقَيْنِ وَامْتِلَائِهِمَا بِالرِّيِّ — فَهِيَ اسْتِعَارَةٌ تَبَعِيَّةٌ: شُبِّهَ الِامْتِلَاءُ بِالرِّيِّ ثُمَّ اشْتُقَّ مِنْهُ الْوَصْفُ.",
   "A second hal, in nasb by a fatha estimated on the alif, annexed — the feminine of الرَّيَّان «well-watered». Al-Zawzanī: by «being watered» he means the fullness of flesh at her ankles. An istiʿāra carried in the derived word (tabaʿiyya): fullness is likened to being well-watered, and the adjective is drawn from that.",
   "İkinci hâl; elif üzerinde takdîrî fetha ile mansûb, muzâf — «الرَّيَّان»ın (suya kanmış) müennesi. Zevzenî: baldırlarının etli ve dolgun oluşunu «suya kanmışlık» ile ifade etmiştir. İstiâre-i tebeiyye vardır: dolgunluk suya kanmaya benzetilmiş, sıfat bundan türetilmiştir."),
 W("الْمُخَلْخَلِ", "mukhalkhal", "noun", ["idafa-definiteness", "al-qafiya"], J(MI, Dn("الْمُخَلْخَلُ: مَوْضِعُ الْخَلْخَالِ مِنَ السَّاقِ", "المُخَلْخَل: the place of the anklet on the leg", "المُخَلْخَل: bacakta halhalın takıldığı yer")), "."),
])
V(None, 31, "Slender-waisted, fair, not slack of body; the top of her breast smooth and bright as a mirror.",
  "İnce belli, beyaz tenli, gövdesi sarkık değil; göğsünün üstü ayna gibi parlak.", [
 T("مُهَفْهَفَةٌ", "muhafhaf", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "tark-al-musnad"],
   "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ، مَرْفُوعٌ بِالضَّمَّةِ — الْمُهَفْهَفَةُ: اللَّطِيفَةُ الْخَصْرِ الضَّامِرَةُ الْبَطْنِ.",
   "The predicate of a mubtada left out («she is»), in raf' by the damma — المُهَفْهَفَة: slim of waist, flat of belly.",
   "Mahzûf mübtedanın («o») haberi, damme ile merfû — المُهَفْهَفَة: ince belli, karnı çekik."),
 T("بَيْضَاءُ", "bayda", "noun", ["mubtada-khabar", "mamnu-min-sarf", "ism-mamdud"], "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، وَلَمْ يُنَوَّنْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ.", "A second predicate, in raf' by the damma; it takes no tanwin — a diptote, for its long feminine alif.", "İkinci haber, damme ile merfû; elif-i memdûde-i te'nîs sebebiyle gayr-i munsarif olduğundan tenvin almaz."),
 T("غَيْرُ", "ghayr", "noun", ["mubtada-khabar", "idafa-definiteness"], "خَبَرٌ ثَالِثٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "A third predicate, in raf' by the damma, annexed.", "Üçüncü haber, damme ile merfû, muzâf."),
 W("مُفَاضَةٍ", "mufad", "noun", ["idafa-definiteness", "ism-maful"], J(MI, Dn("الْمُفَاضَةُ: الْعَظِيمَةُ الْبَطْنِ الْمُسْتَرْخِيَةُ اللَّحْمِ", "المُفَاضَة: big-bellied, loose of flesh", "المُفَاضَة: karnı büyük, eti sarkık")), HEMI),
 W("تَرَائِبُهَا", "tariba", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir"], J(("مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, in raf' by the damma", "Mübteda, damme ile merfû"), IDF("هَا"), Dn("جَمْعُ تَرِيبَةٍ: مَوْضِعُ الْقِلَادَةِ مِنَ الصَّدْرِ", "the plural of تَرِيبَة, where the necklace lies on the breast", "«تَرِيبَة»nin cem'i: göğüste gerdanlığın durduğu yer")), s=[("تَرَائِبُ", "tariba", "noun"), P("هَا")]),
 W("مَصْقُولَةٌ", "masqul", "noun", ["mubtada-khabar", "ism-maful"], J(("خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ", "The predicate of the mubtada, in raf' by the damma", "Mübtedanın haberi, damme ile merfû"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي الصِّفَاتِ قَبْلَهَا", "the clause is a hal of the pronoun hidden in the adjectives before it, in the seat of nasb", "cümle önceki sıfatlardaki gizli zamirden hâl olarak mahallen mansûb"))),
 T("كَالسَّجَنْجَلِ", "sajanjal", "noun", ["huruf-jarr", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih", "wajh-al-shabah", "al-qafiya"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَالسَّجَنْجَلِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَصْقُولَةٌ». السَّجَنْجَلُ: الْمِرْآةُ، لُغَةٌ رُومِيَّةٌ عَرَّبَتْهَا الْعَرَبُ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ: الْمُشَبَّهُ تَرَائِبُهَا، وَالْمُشَبَّهُ بِهِ السَّجَنْجَلُ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَذْكُورٌ وَهُوَ الصَّقْلُ، أَيِ: الصَّفَاءُ وَالْبَرِيقُ.",
   "The kaf is a jarr letter of likening and السَّجَنْجَلِ is in jarr by the kasra — the phrase hangs on «polished». السَّجَنْجَل: a mirror, a Greek word the Arabs made their own. A tashbih mursal mufaṣṣal: the thing likened is the top of her breast, the thing it is likened to is the mirror, the particle is the kaf, and the point of likeness is SAID — the polish: clearness and gleam.",
   "Kâf teşbih bildiren cer harfi, السَّجَنْجَلِ kesre ile mecrûr — câr-mecrûr «مَصْقُولَةٌ»e müteallik. السَّجَنْجَل: ayna; Arapların Arapçalaştırdığı Rumca bir kelime. Teşbih-i mürsel mufassaldır: müşebbeh göğsünün üstü, müşebbehün bih ayna, edat kâf; vech-i şebeh ZİKREDİLMİŞTİR: cilâ, yani duruluk ve parlaklık.", ".", [KA, ("السَّجَنْجَلِ", "sajanjal", "noun")]),
])

# =====================================================================================================================
# The beloved described: verses 32–37
# =====================================================================================================================
def NAAT(of, case, n="", en_of=None):
    """a plain adjective line: of «of», in the given case (jarr / raf / nasb)"""
    c = {"jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "in jarr by the kasra", "kesre ile mecrûr"), "raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "in raf' by the damma", "damme ile merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "in nasb by the fatha", "fetha ile mansûb")}[case]
    o = {"": ("نَعْتٌ", "An adjective", "na'tı"), "2": ("نَعْتٌ ثَانٍ", "A second adjective", "ikinci na'tı"), "3": ("نَعْتٌ ثَالِثٌ", "A third adjective", "üçüncü na'tı")}[n]
    return ("%s لِـ«%s» %s" % (o[0], of, c[0]), "%s of «%s», %s" % (o[1], en_of or of, c[1]), "«%s»in %s, %s" % (of, o[2], c[2]))
def ATF(of, en_of, case="jarr"):
    c = {"jarr": ("مَجْرُورٌ بِالْكَسْرَةِ", "in jarr by the kasra", "kesre ile mecrûr"), "raf": ("مَرْفُوعٌ بِالضَّمَّةِ", "in raf' by the damma", "damme ile merfû"), "nasb": ("مَنْصُوبٌ بِالْفَتْحَةِ", "in nasb by the fatha", "fetha ile mansûb")}[case]
    return ("مَعْطُوفٌ عَلَى «%s» %s" % (of, c[0]), "conjoined to «%s», %s" % (en_of, c[1]), "«%s»e ma'tûf, %s" % (of, c[2]))
V(None, 32, "She is like the first of eggs, its white mingled with yellow; pure water, unmuddied by many comers, has nourished her.",
  "O, beyazına sarılık karışmış ilk yumurta gibidir; onu, çok kimsenin konup bulandırmadığı duru su beslemiştir.", [
 T("كَبِكْرِ", "bikr", "noun", ["huruf-jarr", "idafa-definiteness", "mubtada-khabar", "hadhf-wa-taqdir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَبِكْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: هِيَ كَبِكْرِ. الْبِكْرُ مِنْ كُلِّ صِنْفٍ: مَا لَمْ يَسْبِقْهُ مِثْلُهُ، وَالْمُرَادُ عَلَى أَوَّلِ الْأَقْوَالِ بِكْرُ الْبَيْضِ، يَعْنِي بَيْضَ النَّعَامِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ ذُكِرَ فِيهِ وَصْفُ الْمُشَبَّهِ بِهِ: شَبَّهَ لَوْنَ الْعَشِيقَةِ بِلَوْنِ بَيْضِ النَّعَامِ فِي أَنَّ فِي كُلٍّ مِنْهُمَا بَيَاضًا خَالَطَتْهُ صُفْرَةٌ يَسِيرَةٌ.",
   "The kaf is a jarr letter of likening; بِكْرِ is in jarr by the kasra, annexed — the phrase hangs on the omitted predicate of an omitted mubtada: «she is like the first of…». البِكْر of any kind is what nothing like it came before; on the first of the explanations it is «the first of eggs», the ostrich egg. A tashbih mursal mujmal in which the thing likened to is described: her colour is likened to that of the ostrich egg, in that each is a white with a little yellow mixed in (al-Zawzanī).",
   "Kâf teşbih bildiren cer harfi; بِكْرِ kesre ile mecrûr, muzâf — câr-mecrûr, mahzûf mübtedanın mahzûf haberine müteallik: «o, … ilki gibidir». Her türün «بِكْر»i, kendisinden önce benzeri gelmemiş olandır; görüşlerin ilkine göre maksat yumurtaların ilki, yani devekuşu yumurtasıdır. Müşebbehün bihin vasfı zikredilmiş teşbih-i mürsel mücmeldir: sevgilinin rengi, her ikisinde de az bir sarılık karışmış beyazlık bulunması bakımından devekuşu yumurtasının rengine benzetilmiştir (Zevzenî).", s=[KA, ("بِكْرِ", "bikr", "noun")]),
 W("الْمُقَانَاةِ", "muqanat", "noun", ["idafa-definiteness", "ism-maful"], J(MI, MUD, Dn("اسْمُ مَفْعُولٍ مِنْ «قَانَى» إِذَا خَلَطَ، أَيِ: الْمَخْلُوطَةِ", "the ism maf'ul of قَانَى «to mix»: «the mingled one»", "«karıştırmak» anlamındaki قَانَى'dan ism-i mef'ûl: «karıştırılmış»"))),
 T("الْبَيَاضِ", "bayad", "noun", ["idafa-definiteness", "idafa-lafziyya", "masdar"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ، مِنْ إِضَافَةِ اسْمِ الْمَفْعُولِ إِلَى نَائِبِ فَاعِلِهِ — وَيُرْوَى بِالنَّصْبِ عَلَى التَّشْبِيهِ بِالْمَفْعُولِ بِهِ، كَقَوْلِهِمْ: زَيْدٌ الْحَسَنُ الْوَجْهِ وَالْحَسَنُ الْوَجْهَ.",
   "The second term of the idafa, in jarr by the kasra — the ism maf'ul annexed to its deputy doer; it is also transmitted in nasb, on the likeness of a direct object, as one says زَيْدٌ الْحَسَنُ الْوَجْهِ and الْحَسَنُ الْوَجْهَ (al-Zawzanī).",
   "Muzâfun ileyh, kesre ile mecrûr — ism-i mef'ûlün nâib-i fâiline izâfeti; mef'ûlün bihe benzetilerek nasb ile de rivayet edilir: «زَيْدٌ الْحَسَنُ الْوَجْهِ» ve «الْحَسَنُ الْوَجْهَ» denmesi gibi (Zevzenî)."),
 T("بِصُفْرَةٍ", "sufra", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَصُفْرَةٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«الْمُقَانَاةِ».", "The ba is a jarr letter and صُفْرَةٍ is in jarr by the kasra — the phrase hangs on «the mingled».", "Bâ cer harfi, صُفْرَةٍ kesre ile mecrûr — câr-mecrûr «الْمُقَانَاةِ»ye müteallik.", HEMI, [BI, ("صُفْرَةٍ", "sufra", "noun")]),
 T("غَذَاهَا", "ghadha", "verb", ["thulathi-mujarrad-babs", "naqis-verbs", "maful-bihi"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ عِنْدَ الدُّرَّةِ حَالٌ مِنْ «بِكْرِ الْمُقَانَاةِ»؛ وَعَلَى أَوَّلِ أَقْوَالِ الزَّوْزَنِيِّ الضَّمِيرُ لِلْعَشِيقَةِ: رَجَعَ إِلَى صِفَتِهَا.",
   "A past verb built on a fatha estimated on the alif; هَا is its direct object, set before the doer, in the seat of nasb. For al-Durra the clause is a hal of «the first of the mingled»; on the first of al-Zawzanī's explanations the pronoun is the beloved — he turns back to describing her.",
   "Elif üzerinde takdîrî fetha üzere mebnî mâzî; هَا öne geçmiş mef'ûlün bih, mahallen mansûb. Dürre'ye göre cümle «بِكْرِ الْمُقَانَاةِ»den hâldir; Zevzenî'nin ilk görüşüne göre zamir sevgiliye döner: yine onun vasfına dönmüştür.", s=[("غَذَا", "ghadha", "verb"), P("هَا")]),
 W("نَمِيرُ", "namir", "noun", ["fail", "idafa-definiteness"], J(FAILR, MUD, Dn("النَّمِيرُ: الْمَاءُ الْعَذْبُ النَّامِي فِي الْجَسَدِ", "النَّمِير: sweet water that makes the body thrive", "النَّمِير: bedene yarayan tatlı su"))),
 W("الْمَاءِ", "ma-water", "noun", ["idafa-definiteness", "ism-mamdud"], J(MI)),
 T("غَيْرُ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], "نَعْتٌ لِـ«نَمِيرُ» مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَيُرْوَى بِالنَّصْبِ حَالًا مِنْهُ.", "An adjective of «pure water», in raf' by the damma, annexed — it is also transmitted in nasb, as a hal of it.", "«نَمِيرُ»in na'tı, damme ile merfû, muzâf — ondan hâl olarak nasb ile de rivayet edilir."),
 W("الْمُحَلَّلِ", "muhallal", "noun", ["idafa-definiteness", "ism-maful", "al-qafiya"], J(MI, Dn("أَيْ: لَمْ يَكْثُرْ حُلُولُ النَّاسِ عَلَيْهِ فَيُكَدِّرَهُ", "that is, not much alighted at by people, who would muddy it", "yani insanların çokça konup bulandırmadığı")), "."),
])
V(None, 33, "She turns aside, and shows a smooth long cheek, and guards herself with the glance of a wild creature of Wajra that has young,",
  "Yüz çevirir de uzun, düzgün bir yanak gösterir ve Vecre'nin yavrulu yaban hayvanlarından birinin bakışıyla (kendini) sakınır;", [
 W("تَصُدُّ", "sadda", "verb", ["mudari-marfu", "doubled-verbs"], J(MUDR, HID("هِيَ", "she", "hiye"), Dn("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ الصَّدُّ: الْإِعْرَاضُ", "a fresh sentence; الصَّدّ: turning away", "cümle müste'nefedir; الصَّدّ: yüz çevirmek"))),
 W("وَتُبْدِي", "abda", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs", "naqis-verbs"], J(PRE("wa", "تُبْدِي"), ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "a present verb in raf' by a damma estimated on the ya", "yâ üzerinde takdîrî damme ile merfû muzâri"), HID("هِيَ", "she", "hiye")), s=[WA, ("تُبْدِي", "abda", "verb")]),
 HARF_JARR("عَنْ", "an"),
 W("أَسِيلٍ", "asil-cheek", "noun", ["huruf-jarr", "sifa-mushabbaha", "hadhf-wa-taqdir", "ijaz-al-hadhf"], J(MAJR, TA("تُبْدِي", "shows", "ye"), Dn("أَيْ: عَنْ خَدٍّ أَسِيلٍ، فَحَذَفَ الْمَوْصُوفَ لِدَلَالَةِ الصِّفَةِ عَلَيْهِ؛ الْأَسَالَةُ: امْتِدَادٌ وَطُولٌ فِي الْخَدِّ", "that is, «a smooth long cheek»: the noun is dropped because its adjective points to it; الأَسَالَة: length and evenness of the cheek", "yani «uzun, düzgün bir yanak»; sıfat delâlet ettiği için mevsûf hazfedilmiştir; الأَسَالَة: yanağın uzun ve düzgün oluşu"))),
 W("وَتَتَّقِي", "ittaqa", "verb", ["atf-nasaq", "mudari-marfu", "form-viii-verbs", "naqis-verbs"], J(PRE("wa", "تَتَّقِي"), ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "a present verb in raf' by a damma estimated on the ya", "yâ üzerinde takdîrî damme ile merfû muzâri"), HID("هِيَ", "she", "hiye"), Dn("الِاتِّقَاءُ: الْحَجْزُ بَيْنَ الشَّيْئَيْنِ", "الاِتِّقَاء: to put something between oneself and another", "الاِتِّقَاء: iki şeyin arasına engel koymak")), HEMI, [WA, ("تَتَّقِي", "ittaqa", "verb")]),
 T("بِنَاظِرَةٍ", "nazira", "noun", ["huruf-jarr", "ism-fail", "hadhf-wa-taqdir", "istiara", "arkan-al-istiara"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَنَاظِرَةٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَتَّقِي»؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: بِعَيْنٍ نَاظِرَةٍ. قَالَ الزَّوْزَنِيُّ: شَبَّهَهَا فِي حُسْنِ عَيْنَيْهَا بِظَبْيَةٍ مُطْفِلٍ أَوْ بِمَهَاةٍ مُطْفِلٍ — فَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَتْ نَاظِرَةُ الْوَحْشِ لِعَيْنِهَا.",
   "The ba is a jarr letter and نَاظِرَةٍ is in jarr by the kasra — the phrase hangs on «guards herself»; it describes a noun left out: «with an eye that looks». Al-Zawzanī: he likens her, for the beauty of her eyes, to a gazelle or a wild cow with young. So it is an explicit istiʿāra: the glancing eye of the wild creature is borrowed for her eye.",
   "Bâ cer harfi, نَاظِرَةٍ kesre ile mecrûr — câr-mecrûr «تَتَّقِي»ye müteallik; mahzûf mevsûfun na'tıdır: «bakan bir gözle». Zevzenî: onu, gözlerinin güzelliği bakımından yavrulu bir ceylana ya da yaban sığırına benzetmiştir. Demek ki istiâre-i tasrîhiyyedir: yaban hayvanının bakan gözü onun gözü için istiâre edilmiştir.", s=[BI, ("نَاظِرَةٍ", "nazira", "noun")]),
 HARF_JARR("مِنْ", "min"),
 T("وَحْشِ", "wahsh", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "hadhf-al-mudaf-wal-mudaf-ilayh", "ijaz-al-hadhf"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ. أَيْ: مِنْ نَوَاظِرِ وَحْشِ وَجْرَةَ، فَحَذَفَ الْمُضَافَ وَأَقَامَ الْمُضَافَ إِلَيْهِ مَقَامَهُ، كَقَوْلِهِ تَعَالَى: «وَاسْأَلِ الْقَرْيَةَ».",
   "In jarr by the kasra, annexed — the phrase hangs on a second omitted adjective of the omitted noun. That is: «of the eyes of the wild creatures of Wajra»: the annexed noun is dropped and its second term set in its place, as in the Qurʾānic «ask the town» (12:82) (al-Zawzanī).",
   "Kesre ile mecrûr, muzâf — câr-mecrûr mahzûf mevsûfun mahzûf ikinci na'tına müteallik. Yani: «Vecre'nin yaban hayvanlarının gözlerinden»; muzâf hazfedilip muzâfun ileyh onun yerine konmuştur; «وَاسْأَلِ الْقَرْيَةَ» (Yûsuf 82) âyetindeki gibi (Zevzenî)."),
 W("وَجْرَةَ", "wajra", "propn", ["idafa-definiteness", "mamnu-min-sarf"], J(("مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ", "The second term of the idafa, in jarr by the fatha in place of the kasra — a diptote: a feminine proper name", "Muzâfun ileyh; alemiyet ve te'nîs sebebiyle gayr-i munsarif olduğundan kesre yerine fetha ile mecrûr"), Dn("وَجْرَةُ: مَوْضِعٌ", "Wajra is a place", "Vecre bir yer adıdır"))),
 W("مُطْفِلِ", "mutfil", "noun", ["naat-sifa", "ism-fail", "al-qafiya"], J(NAAT("وَحْشِ", "jarr", en_of="wild creatures"), QAFIYA, Dn("الْمُطْفِلُ: الَّتِي لَهَا طِفْلٌ؛ وَخَصَّهُنَّ لِنَظَرِهِنَّ إِلَى أَوْلَادِهِنَّ بِالْعَطْفِ وَالشَّفَقَةِ", "المُطْفِل: one that has a young one; he names these because they look on their young with tenderness, and are then loveliest of eye", "المُطْفِل: yavrusu olan; onları anmıştır, çünkü yavrularına şefkatle bakarlar ve o hâlde gözleri en güzeldir")), "،"),
])
V(None, 34, "and a neck like the neck of the white antelope — not over-long when she lifts it, nor bare of ornament;",
  "bir de ak ceylanın boynu gibi bir boyun (gösterir); onu kaldırdığında ölçüsüz uzun değildir, takısız da değildir;", [
 W("وَجِيدٍ", "jid", "noun", ["atf-nasaq"], J(PRE("wa", "جِيدٍ"), ATF("أَسِيلٍ", "a smooth cheek"), Dn("أَيْ: وَتُبْدِي عَنْ جِيدٍ؛ الْجِيدُ: الْعُنُقُ", "that is, «and she shows a neck»; الجِيد: the neck", "yani «bir de boyun gösterir»; الجِيد: boyun")), s=[WA, ("جِيدٍ", "jid", "noun")]),
 T("كَجِيدِ", "jid", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَجِيدِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«جِيدٍ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ جِيدُهَا، وَالْمُشَبَّهُ بِهِ جِيدُ الرِّئْمِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ حُسْنُ الِامْتِدَادِ فِي حَالِ رَفْعِهِ.",
   "The kaf is a jarr letter of likening; جِيدِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «a neck». A tashbih mursal mujmal: the thing likened is her neck, the thing it is likened to is the neck of the white antelope, the particle is the kaf, and the point of likeness is left unsaid — its graceful length when raised.",
   "Kâf teşbih bildiren cer harfi; جِيدِ kesre ile mecrûr, muzâf — câr-mecrûr «جِيدٍ»in mahzûf na'tına müteallik. Teşbih-i mürsel mücmeldir: müşebbeh onun boynu, müşebbehün bih ak ceylanın boynu, edat kâf; vech-i şebeh mahzûftur: kaldırıldığı hâldeki güzel uzunluk.", s=[KA, ("جِيدِ", "jid", "noun")]),
 W("الرِّئْمِ", "rim", "noun", ["idafa-definiteness"], J(MI)),
 T("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "jumla-sifa"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «جِيدٍ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لَهُ.", "A defective past verb built on fatha; its noun is a hidden pronoun returning to «a neck» — the clause is a second adjective of it, in the seat of jarr.", "Fetha üzere mebnî nâkıs mâzî; ismi «جِيدٍ»e dönen gizli zamir — cümle onun ikinci na'tı olarak mahallen mecrûr."),
 T("بِفَاحِشٍ", "fahish", "noun", ["kana-wa-akhawatuha", "huruf-jarr", "ism-fail"],
   "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَفَاحِشٍ خَبَرُ «لَيْسَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ — الْفَاحِشُ: مَا جَاوَزَ الْقَدْرَ الْمَحْمُودَ.",
   "The ba is an added jarr letter that strengthens the negation; فَاحِشٍ is the predicate of لَيْسَ, in nasb by a fatha that the added letter's vowel keeps from showing — الفَاحِش: what goes beyond the praised measure.",
   "Bâ, nefyi pekiştiren zâid cer harfi; فَاحِشٍ «لَيْسَ»nin haberi; zâid harfin harekesi mahalli meşgul ettiği için takdîrî fetha ile mansûb — الفَاحِش: övülen ölçüyü aşan.", HEMI, [BI, ("فَاحِشٍ", "fahish", "noun")]),
 T("إِذَا", "idha", "part", ["maful-fih"], "ظَرْفُ زَمَانٍ مُجَرَّدٌ عَنِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«فَاحِشٍ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time with no sense of condition, built on sukun in the seat of nasb; it hangs on «over-long» and is annexed to the clause after it.", "Şart mânâsından soyutlanmış zaman zarfı; sükûn üzere mebnî, mahallen mansûb; «فَاحِشٍ»e müteallik, sonraki cümleye muzâf."),
 T("هِيَ", "hiya", "pron", ["fail", "hadhf-wa-taqdir"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «نَصَّتْهُ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.", "A detached pronoun built on fatha, the doer of an omitted verb that «she lifts it» explains, in the seat of raf' — the clause is in the seat of jarr, annexed to إِذَا.", "Fetha üzere mebnî munfasıl zamir; «نَصَّتْهُ»nün tefsir ettiği mahzûf fiilin fâili, mahallen merfû — cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr."),
 T("نَصَّتْهُ", "nassa", "verb", ["doubled-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ تَفْسِيرِيَّةٌ لَا مَحَلَّ لَهَا؛ النَّصُّ: الرَّفْعُ.", "A past verb built on fatha; the ta marks the feminine, the هُ is its direct object, in the seat of nasb, and the doer is a hidden «she» — the clause explains the omitted verb and has no seat; النَّصّ: raising.", "Fetha üzere mebnî mâzî; tâ te'nîs için, «hû» mef'ûlün bih, mahallen mansûb; fâili gizli «hiye» — cümle tefsîriyyedir, mahalli yoktur; النَّصّ: kaldırmak.", s=[("نَصَّتْ", "nassa", "verb"), P("هُ")]),
 T("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to strengthen the negation.", "Vâv atıf; lâ, nefyi pekiştirmek için zâiddir.", s=[WA, ("لَا", "la-nafiya", "part")]),
 T("بِمُعَطَّلِ", "muattal", "noun", ["atf-nasaq", "huruf-jarr", "ism-maful", "takmil-wa-tatmim", "al-qafiya"],
   "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ، وَمُعَطَّلِ مَعْطُوفٌ عَلَى «فَاحِشٍ» مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا" + QAFIYA[0] + " — الْمُعَطَّلُ: الْخَالِي مِنَ الْحُلِيِّ. شَبَّهَ عُنُقَهَا بِعُنُقِ الظَّبْيَةِ ثُمَّ ذَكَرَ أَنَّهُ لَا يُشْبِهُهُ فِي التَّعَطُّلِ عَنِ الْحُلِيِّ — وَهُوَ تَكْمِيلٌ يُسَمَّى الِاحْتِرَاسَ: دَفَعَ بِهِ مَا قَدْ يُوهِمُهُ التَّشْبِيهُ.",
   "The ba is an added jarr letter; مُعَطَّلِ is conjoined to «over-long», in jarr in its wording and in nasb in its seat" + QAFIYA[1] + " — المُعَطَّل: bare of ornament. He likens her neck to the gazelle's and then says it is unlike it in being bare of jewels (al-Zawzanī) — a takmīl, called iḥtirās: he wards off what the likeness might wrongly suggest.",
   "Bâ zâid cer harfi; مُعَطَّلِ «فَاحِشٍ»e ma'tûf, lafzen mecrûr mahallen mansûb" + QAFIYA[2] + " — المُعَطَّل: takıdan yoksun. Boynunu ceylanın boynuna benzetmiş, sonra takısız olmakta ona benzemediğini söylemiştir (Zevzenî) — bu, ihtirâs denilen tekmîldir: teşbihin uyandırabileceği yanlış vehmi gidermiştir.", "؛", [BI, ("مُعَطَّلِ", "muattal", "noun")]),
])
V(None, 35, "and hair that graces her back, black as charcoal, thick as the clustered fruit-stalk of a palm.",
  "bir de sırtını süsleyen, kömür karası, hurma ağacının salkım salkım hevengi gibi gür saç (gösterir).", [
 W("وَفَرْعٍ", "far-hair", "noun", ["atf-nasaq"], J(PRE("wa", "فَرْعٍ"), ATF("جِيدٍ", "a neck"), Dn("الْفَرْعُ: الشَّعْرُ التَّامُّ", "الفَرْع: a full head of hair", "الفَرْع: gür ve uzun saç")), s=[WA, ("فَرْعٍ", "far-hair", "noun")]),
 W("يَزِينُ", "zana", "verb", ["mudari-marfu", "hollow-verbs", "jumla-sifa"], J(MUDR, HID("هُوَ", "it", "hüve", ("«فَرْعٍ»", "«hair»", "«فَرْعٍ»e")), Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«فَرْعٍ»", "the clause qualifies «hair», in the seat of jarr", "cümle «فَرْعٍ»in na'tı olarak mahallen mecrûr"))),
 W("الْمَتْنَ", "matn", "noun", ["maful-bihi"], J(MAFR, Dn("أَيْ: ظَهْرَهَا إِذَا أَرْسَلَتْهُ عَلَيْهِ", "that is, her back, when she lets it down upon it", "yani saçını üzerine saldığında sırtını"))),
 W("أَسْوَدَ", "aswad", "noun", ["naat-sifa", "mamnu-min-sarf"], J(("نَعْتٌ لِـ«فَرْعٍ» مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ", "An adjective of «hair», in jarr by the fatha in place of the kasra — a diptote: an adjective on أَفْعَل", "«فَرْعٍ»in na'tı; vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif olduğundan kesre yerine fetha ile mecrûr"))),
 W("فَاحِمٍ", "fahim", "noun", ["naat-sifa", "ism-fail"], J(("نَعْتٌ مُؤَكِّدٌ لِـ«أَسْوَدَ» مَجْرُورٌ بِالْكَسْرَةِ", "An adjective that strengthens «black», in jarr by the kasra", "«أَسْوَدَ»i pekiştiren na't, kesre ile mecrûr"), Dn("الْفَاحِمُ: الشَّدِيدُ السَّوَادِ، مُشْتَقٌّ مِنَ الْفَحْمِ", "الفَاحِم: jet-black, from الفَحْم «charcoal»", "الفَاحِم: simsiyah; «kömür» anlamındaki الفَحْم'den")), HEMI),
 W("أَثِيثٍ", "athith", "noun", ["naat-sifa", "sifa-mushabbaha"], J(NAAT("فَرْعٍ", "jarr", "3", en_of="hair"), Dn("الْأَثِيثُ: الْكَثِيرُ", "الأَثِيث: thick, abundant", "الأَثِيث: gür, sık"))),
 T("كَقِنْوِ", "qinw", "noun", ["huruf-jarr", "idafa-definiteness", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih", "wajh-al-shabah"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَقِنْوِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَثِيثٍ»، وَيَجُوزُ تَعْلِيقُهُمَا بِمَحْذُوفٍ نَعْتٍ. الْقِنْوُ: عِذْقُ النَّخْلَةِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ: شَبَّهَ ذَوَائِبَهَا بِقِنْوِ نَخْلَةٍ أَخْرَجَتْ قِنْوَانَهَا، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَذْكُورٌ وَهُوَ الْأَثَاثَةُ، أَيِ: الْكَثْرَةُ وَالتَّجَعُّدُ.",
   "The kaf is a jarr letter of likening; قِنْوِ is in jarr by the kasra, annexed — the phrase hangs on «thick», or on an omitted adjective. القِنْو: the fruit-stalk of a date-palm with its clusters. A tashbih mursal mufaṣṣal: her tresses are likened to the fruit-stalk of a palm that has put out its bunches; the particle is the kaf, and the point of likeness is said — thickness: abundance and curl (al-Zawzanī).",
   "Kâf teşbih bildiren cer harfi; قِنْوِ kesre ile mecrûr, muzâf — câr-mecrûr «أَثِيثٍ»e müteallik; mahzûf bir na'ta bağlanması da câizdir. القِنْو: hurma hevengi. Teşbih-i mürsel mufassaldır: zülüfleri, salkımlarını çıkarmış hurma ağacının hevengine benzetilmiştir; edat kâf, vech-i şebeh zikredilmiştir: gürlük, yani çokluk ve kıvırcıklık (Zevzenî).", s=[KA, ("قِنْوِ", "qinw", "noun")]),
 W("النَّخْلَةِ", "nakhla", "noun", ["idafa-definiteness"], J(MI)),
 W("الْمُتَعَثْكِلِ", "mutaathkil", "noun", ["naat-sifa", "ism-fail", "al-qafiya"], J(NAAT("قِنْوِ", "jarr", en_of="fruit-stalk"), Dn("الْمُتَعَثْكِلُ: الَّذِي خَرَجَتْ عَثَاكِيلُهُ، أَيْ: شَمَارِيخُهُ", "المُتَعَثْكِل: one whose clusters have come out", "المُتَعَثْكِل: salkımları çıkmış olan")), "."),
])
V(None, 36, "Its locks are twisted up towards the top; the plaits are lost among hair doubled back and hair let loose.",
  "Onun lüleleri yukarıya doğru kaldırılmıştır; örgüleri, bir kısmı katlanmış bir kısmı salıverilmiş saçların içinde kaybolur.", [
 W("غَدَائِرُهُ", "ghadira", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], J(("مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, in raf' by the damma", "Mübteda, damme ile merfû"), IDF("هُ"), Dn("وَالضَّمِيرُ لِلْفَرْعِ؛ جَمْعُ غَدِيرَةٍ: الْخُصْلَةُ مِنَ الشَّعْرِ", "the pronoun is the hair; the plural of غَدِيرَة, a lock of hair", "zamir saça döner; «غَدِيرَة»nin (saç lülesi) cem'i")), s=[("غَدَائِرُ", "ghadira", "noun"), P("هُ")]),
 T("مُسْتَشْزِرَاتٌ", "mustashzir", "noun", ["mubtada-khabar", "jam-muannath-salim", "ism-fail"],
   "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ. الِاسْتِشْزَارُ: الِارْتِفَاعُ وَالرَّفْعُ جَمِيعًا؛ فَبِكَسْرِ الزَّايِ مِنَ اللَّازِمِ أَيْ: مُرْتَفِعَاتٌ، وَبِفَتْحِهَا مِنَ الْمُتَعَدِّي أَيْ: مَرْفُوعَاتٌ. وَبِهٰذِهِ الْكَلِمَةِ مَثَّلَ التَّلْخِيصُ لِتَنَافُرِ الْحُرُوفِ الْمُخِلِّ بِفَصَاحَةِ الْمُفْرَدِ.",
   "The predicate of the mubtada, in raf' by the damma — a fresh sentence. الاِسْتِشْزَار is both rising and raising: with a kasra on the zay it is intransitive, «rising»; with a fatha, transitive, «raised». The Talkhīṣ cites this very word for the clash of letters (tanāfur al-ḥurūf) that mars the purity of a single word.",
   "Mübtedanın haberi, damme ile merfû — cümle müste'nefedir. الاِسْتِشْزَار hem yükselmek hem yükseltmek demektir: zây'ın kesresiyle lâzımdır, «yükselmiş»; fethasıyla müteaddîdir, «yukarı kaldırılmış». Telhîs, müfredin fesâhatini bozan tenâfür-i hurûfa bu kelimeyi örnek verir."),
 HARF_JARR("إِلَى", "ila"),
 W("الْعُلَا", "ulya", "noun", ["huruf-jarr", "ism-maqsur-manqus", "jam-taksir"], J(MAJR_A, TA("مُسْتَشْزِرَاتٌ", "twisted up", "a"), Dn("جَمْعُ الْعُلْيَا، أَيْ: إِلَى فَوْقُ", "the plural of العُلْيَا: «upwards»", "«العُلْيَا»nın cem'i: «yukarıya doğru»")), HEMI),
 W("تَضِلُّ", "dalla-stray", "verb", ["mudari-marfu", "doubled-verbs", "kinaya", "aqsam-al-kinaya"], J(MUDR, Dn("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ تَضِلُّ: تَغِيبُ. وَغِيَابُ الْعِقَاصِ فِي الشَّعْرِ كِنَايَةٌ عَنْ صِفَةٍ: وُفُورِ شَعْرِهَا", "a fresh sentence; تَضِلُّ: are lost from sight. The plaits being lost in the hair is a kinaya for a quality: how abundant her hair is (al-Zawzanī)", "cümle müste'nefedir; تَضِلُّ: gözden kaybolur. Örgülerin saç içinde kaybolması bir sıfattan kinâyedir: saçının bolluğu (Zevzenî)"))),
 W("الْعِقَاصُ", "aqisa", "noun", ["fail", "jam-taksir"], J(FAILR, Dn("جَمْعُ عَقِيصَةٍ: الْخُصْلَةُ الْمَجْمُوعَةُ مِنَ الشَّعْرِ", "the plural of عَقِيصَة, a gathered and plaited lock", "«عَقِيصَة»nin cem'i: toplanıp örülmüş saç tutamı"))),
 HARF_JARR("فِي", "fi"),
 T("مُثَنًّى", "muthanna", "noun", ["huruf-jarr", "ism-maqsur-manqus", "ism-maful", "tibaq"],
   "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَضِلُّ»؛ اسْمُ مَفْعُولٍ مِنْ «ثَنَّى»، أَيْ: فِي شَعْرٍ بَعْضُهُ مَثْنِيٌّ وَبَعْضُهُ مُرْسَلٌ؛ وَبَيْنَهُ وَبَيْنَ «مُرْسَلِ» طِبَاقٌ.",
   "In jarr by a kasra estimated on the alif that falls before the tanwin — the phrase hangs on «are lost»; the ism maf'ul of ثَنَّى: in hair part of which is doubled back and part let loose; with «let loose» it makes a tibaq.",
   "Tenvin sebebiyle düşen elif üzerinde takdîrî kesre ile mecrûr — câr-mecrûr «تَضِلُّ»ye müteallik; «ثَنَّى»dan ism-i mef'ûl: bir kısmı katlanmış, bir kısmı salıverilmiş saç içinde; «مُرْسَلِ» ile arasında tıbâk vardır."),
 W("وَمُرْسَلِ", "mursal", "noun", ["atf-nasaq", "ism-maful", "tibaq", "al-qafiya"], J(PRE("wa", "مُرْسَلِ"), ATF("مُثَنًّى", "doubled back"), QAFIYA, Dn("يُطَابِقُ «مُثَنًّى»", "the contrary of «doubled back»", "«مُثَنًّى»nın zıddı")), ".", [WA, ("مُرْسَلِ", "mursal", "noun")]),
])
V(None, 37, "And a waist fine as a plaited leather rein, slender; and a shank like a reed-stalk of the watered, fruit-bowed palm-grove.",
  "Bir de örme deri yular gibi ince, dar bir bel; ve sulanmış, dalları yükten eğilmiş hurmalığın kamış boğumu gibi bir baldır (gösterir).", [
 W("وَكَشْحٍ", "kashh", "noun", ["atf-nasaq"], J(PRE("wa", "كَشْحٍ"), ATF("جِيدٍ", "a neck")), s=[WA, ("كَشْحٍ", "kashh", "noun")]),
 W("لَطِيفٍ", "latif", "noun", ["naat-sifa", "sifa-mushabbaha"], J(NAAT("كَشْحٍ", "jarr", en_of="a waist"))),
 T("كَالْجَدِيلِ", "jadil", "noun", ["huruf-jarr", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih", "wajh-al-shabah"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَالْجَدِيلِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«لَطِيفٍ». الْجَدِيلُ: خِطَامٌ يُتَّخَذُ مِنَ الْأَدَمِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُفَصَّلٌ: الْمُشَبَّهُ كَشْحُهَا، وَالْمُشَبَّهُ بِهِ الْجَدِيلُ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَذْكُورٌ وَهُوَ اللَّطَافَةُ، أَيِ: الدِّقَّةُ وَالضُّمُورُ.",
   "The kaf is a jarr letter of likening and الْجَدِيلِ is in jarr by the kasra — the phrase hangs on «fine». الجَدِيل: a rein plaited of leather. A tashbih mursal mufaṣṣal: the thing likened is her waist, the thing it is likened to is the plaited rein, the particle is the kaf, and the point of likeness is said — fineness: being thin and drawn in.",
   "Kâf teşbih bildiren cer harfi, الْجَدِيلِ kesre ile mecrûr — câr-mecrûr «لَطِيفٍ»e müteallik. الجَدِيل: deriden örülmüş yular. Teşbih-i mürsel mufassaldır: müşebbeh onun beli, müşebbehün bih örme yular, edat kâf; vech-i şebeh zikredilmiştir: incelik, yani darlık ve çekiklik.", s=[KA, ("الْجَدِيلِ", "jadil", "noun")]),
 W("مُخَصَّرٍ", "mukhassar", "noun", ["naat-sifa", "ism-maful"], J(NAAT("كَشْحٍ", "jarr", "2", en_of="a waist"), Dn("الْمُخَصَّرُ: الدَّقِيقُ الْوَسَطِ", "المُخَصَّر: narrow in the middle", "المُخَصَّر: ortası ince")), HEMI),
 W("وَسَاقٍ", "saq", "noun", ["atf-nasaq"], J(PRE("wa", "سَاقٍ"), ATF("كَشْحٍ", "a waist")), s=[WA, ("سَاقٍ", "saq", "noun")]),
 T("كَأُنْبُوبِ", "unbub", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَأُنْبُوبِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«سَاقٍ». الْأُنْبُوبُ: مَا بَيْنَ الْعُقْدَتَيْنِ مِنَ الْقَصَبِ وَغَيْرِهِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شَبَّهَ صَفَاءَ لَوْنِ سَاقِهَا بِبَرْدِيٍّ بَيْنَ نَخِيلٍ تُظِلُّهُ أَغْصَانُهَا، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ صَفَاءُ اللَّوْنِ وَنَقَاؤُهُ.",
   "The kaf is a jarr letter of likening; أُنْبُوبِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «a shank». الأُنْبُوب: the length between two knots of a reed. A tashbih mursal mujmal: the clear colour of her shank is likened to papyrus growing among palms whose boughs shade it; the particle is the kaf, and the point of likeness — clearness and purity of colour — is left unsaid (al-Zawzanī).",
   "Kâf teşbih bildiren cer harfi; أُنْبُوبِ kesre ile mecrûr, muzâf — câr-mecrûr «سَاقٍ»ın mahzûf na'tına müteallik. الأُنْبُوب: kamışın iki boğumu arası. Teşbih-i mürsel mücmeldir: baldırının renginin duruluğu, dalları kendisini gölgeleyen hurmalar arasındaki berdîye benzetilmiştir; edat kâf; vech-i şebeh — rengin duruluğu ve temizliği — mahzûftur (Zevzenî).", s=[KA, ("أُنْبُوبِ", "unbub", "noun")]),
 T("السَّقِيِّ", "saqiyy", "noun", ["idafa-definiteness", "hadhf-wa-taqdir"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — بِمَعْنَى الْمَسْقِيِّ كَالْجَرِيحِ بِمَعْنَى الْمَجْرُوحِ؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ، وَالتَّقْدِيرُ: كَأُنْبُوبِ النَّخْلِ الْمَسْقِيِّ، وَمِنْهُمْ مَنْ جَعَلَهُ نَعْتًا لِلْبَرْدِيِّ.",
   "The second term of the idafa, in jarr by the kasra — it means «watered», as الجَرِيح means «wounded»; it describes a noun left out: «like a reed of the watered palms»; some make it describe the papyrus itself (al-Zawzanī).",
   "Muzâfun ileyh, kesre ile mecrûr — «sulanmış» anlamındadır (الجَرِيح'in «yaralanmış» anlamında olması gibi); mahzûf mevsûfun na'tıdır, takdiri: «sulanmış hurmalığın kamışı gibi»; kimileri onu berdînin na'tı saymıştır (Zevzenî)."),
 W("الْمُذَلَّلِ", "mudhallal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ", "A second adjective of the omitted noun, in jarr by the kasra", "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr"), Dn("أَيِ: الَّذِي ذُلِّلَتْ أَغْصَانُهُ بِكَثْرَةِ الْحَمْلِ", "whose boughs are bowed low by their load of fruit", "dalları meyve yükünden eğilmiş olan")), "."),
])

# =====================================================================================================================
# Her description completed, and the heart that will not forget: verses 38–43
# =====================================================================================================================
MUDR_W = ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْوَاوِ لِلثِّقَلِ", "A present verb in raf' by a damma estimated on the waw", "Vâv üzerinde takdîrî damme ile merfû muzâri")
MUDR_Y = ("فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", "A present verb in raf' by a damma estimated on the ya", "Yâ üzerinde takdîrî damme ile merfû muzâri")
KHB_KAANNA = ("خَبَرُ كَأَنَّ مَرْفُوعٌ بِالضَّمَّةِ", "The predicate of كَأَنَّ, in raf' by the damma", "كَأَنَّ'nin haberi, damme ile merfû")
IDHA_Z = lambda w, en, tr: ("ظَرْفُ زَمَانٍ مُجَرَّدٌ عَنِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«%s»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ" % w,
                            "An adverb of time with no sense of condition, built on sukun in the seat of nasb; it hangs on «%s» and is annexed to the clause after it" % en,
                            "Şart mânâsından soyutlanmış zaman zarfı; sükûn üzere mebnî, mahallen mansûb; «%s»%s müteallik, sonraki cümleye muzâf" % (w, tr))
V(None, 38, "The forenoon finds her with crumbs of musk upon her bed; she sleeps far into the morning, and does not gird her waist over a working-shift.",
  "Kuşluk vakti onu, yatağının üstünde misk kırıntılarıyla bulur; kuşluğa kadar uyur, iş gömleği giyip de beline kuşak bağlamaz.", [
 T("وَتُضْحِي", "adha-become", "verb", ["kana-wa-akhawatuha", "al-fil-al-tamm-wal-naqis", "form-iv-verbs", "naqis-verbs"],
   "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَتُضْحِي فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَخَبَرُهُ الْجُمْلَةُ بَعْدَهُ. وَفَسَّرَهُ الزَّوْزَنِيُّ عَلَى التَّمَامِ: «تُصَادِفُ الضُّحَى»، فَالْجُمْلَةُ بَعْدَهُ حَالٌ؛ وَيُرْوَى «وَيُضْحِي» بِالْيَاءِ فَـ«فَتِيتُ» اسْمُهُ.",
   "The waw opens a new sentence; تُضْحِي is a defective present verb in raf' by a damma estimated on the ya; its noun is a hidden «she», and its predicate is the clause after it. Al-Zawzanī explains it as a complete verb — «she meets the forenoon» — and then the clause after it is a hal. It is also transmitted «وَيُضْحِي», with a ya, and then «crumbs» is its noun.",
   "Vâv istînâfiyye; تُضْحِي yâ üzerinde takdîrî damme ile merfû nâkıs muzâri; ismi gizli «hiye», haberi sonraki cümledir. Zevzenî onu tam fiil olarak açıklar: «kuşluk vaktine erişir»; o takdirde sonraki cümle hâldir. Yâ ile «وَيُضْحِي» de rivayet edilir; o zaman «فَتِيتُ» onun ismidir.", s=[WA, ("تُضْحِي", "adha-become", "verb")]),
 W("فَتِيتُ", "fatit", "noun", ["mubtada-khabar", "idafa-definiteness"], J(("مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, in raf' by the damma", "Mübteda, damme ile merfû"), MUD, Dn("الْفَتِيتُ وَالْفُتَاتُ: دَقَائِقُ الشَّيْءِ الْحَاصِلَةُ بِالْفَتِّ", "الفَتِيت, الفُتَات: the fine bits of a thing got by crumbling it", "الفَتِيت, الفُتَات: bir şeyin ufalanmasıyla oluşan kırıntılar"))),
 W("الْمِسْكِ", "misk", "noun", ["idafa-definiteness"], J(MI)),
 T("فَوْقَ", "fawqa", "noun", ["maful-fih", "idafa-definiteness", "mubtada-khabar", "al-hal-jumla-wa-rabituha"],
   "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَإِ؛ وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «تُضْحِي»، أَوْ حَالٌ مِنْ فَاعِلِهِ إِنْ كَانَ تَامًّا، وَالرَّابِطُ الضَّمِيرُ فِي «فِرَاشِهَا».",
   "An adverb of place, in nasb by the fatha, annexed — it hangs on the omitted predicate of the mubtada; the nominal clause is the predicate of «تُضْحِي», in the seat of nasb — or, if the verb is complete, a hal of its doer, tied to it by the pronoun in «her bed».",
   "Mekân zarfı, fetha ile mansûb, muzâf — mübtedanın mahzûf haberine müteallik; isim cümlesi «تُضْحِي»nin haberi olarak mahallen mansûb; fiil tam sayılırsa fâilinden hâldir, râbıt «فِرَاشِهَا»daki zamirdir."),
 W("فِرَاشِهَا", "firash", "noun", ["idafa-definiteness"], J(MI, IDF("هَا"), Dn("أَيْ: فِرَاشِهَا الَّذِي بَاتَتْ عَلَيْهِ", "that is, the bed on which she passed the night", "yani üzerinde gecelediği yatağı")), HEMI, [("فِرَاشِ", "firash", "noun"), P("هَا")]),
 T("نَؤُومُ", "nauum", "noun", ["mubtada-khabar", "hadhf-wa-taqdir", "sighat-mubalagha", "idafa-definiteness", "kinaya", "aqsam-al-kinaya"],
   "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هِيَ، مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَيُرْوَى بِالنَّصْبِ عَلَى الْمَدْحِ، وَبِالْجَرِّ بَدَلًا مِنَ الضَّمِيرِ فِي «فِرَاشِهَا». صِيغَةُ مُبَالَغَةٍ عَلَى فَعُولٍ، وَلَمْ تَلْحَقْهَا عَلَامَةُ التَّأْنِيثِ لِأَنَّ فَعُولًا بِمَعْنَى الْفَاعِلِ يَسْتَوِي فِيهِ الْمُذَكَّرُ وَالْمُؤَنَّثُ، كَقَوْلِهِ تَعَالَى: «تَوْبَةً نَصُوحًا». وَفِي الْبَيْتِ كِنَايَةٌ عَنْ صِفَةٍ: كَثْرَةُ فُتَاتِ الْمِسْكِ عَلَى فِرَاشِهَا وَنَوْمُهَا فِي الضُّحَى وَتَرْكُهَا الِانْتِطَاقَ لِلْعَمَلِ، يُرِيدُ بِذٰلِكَ كُلِّهِ أَنَّهَا مَخْدُومَةٌ مُنَعَّمَةٌ تُخْدَمُ وَلَا تَخْدُمُ؛ وَ«نَؤُومُ الضُّحَى» مِنْ أَمْثِلَةِ الْكِنَايَةِ السَّائِرَةِ عِنْدَ الْبَلَاغِيِّينَ.",
   "The predicate of an omitted mubtada, «she», in raf' by the damma, annexed — it is also transmitted in nasb, as praise, and in jarr, as a badal of the pronoun in «her bed». An intensive form on فَعُول; it takes no feminine mark, because فَعُول in the sense of a doer is the same for masculine and feminine, as in the Qurʾānic «تَوْبَةً نَصُوحًا» (66:8) (al-Zawzanī). The verse is a kinaya for a quality: the musk crumbled thick on her bed, her sleeping in the forenoon, her never girding herself for work — by all this he means that she lives in ease, is waited on and waits on no one (al-Zawzanī). «نَؤُومُ الضُّحَى» is one of the stock examples of kinaya among the scholars of balāgha.",
   "Mahzûf mübtedanın («hiye») haberi, damme ile merfû, muzâf — medih üzere nasb ile ve «فِرَاشِهَا»daki zamirden bedel olarak cer ile de rivayet edilir. «فَعُول» vezninde mübalağa sîgasıdır; te'nîs alâmeti almamıştır, çünkü fâil mânâsındaki «فَعُول»de müzekker ile müennes birdir; «تَوْبَةً نَصُوحًا» (Tahrîm 8) âyetindeki gibi (Zevzenî). Beyitte sıfattan kinâye vardır: yatağında misk kırıntılarının çokluğu, kuşlukta uyuması, iş için kuşak bağlamaması; bütün bunlarla onun nimet içinde yaşadığını, hizmet edilip hizmet etmediğini kasteder (Zevzenî). «نَؤُومُ الضُّحَى» belâgat âlimlerinin meşhur kinâye örneklerindendir."),
 T("الضُّحَى", "duha", "noun", ["idafa-definiteness", "ism-maqsur-manqus", "idafa-lafziyya"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + MAQSUR_J + " — مِنْ إِضَافَةِ صِيغَةِ الْمُبَالَغَةِ إِلَى ظَرْفِهَا، أَيْ: كَثِيرَةُ النَّوْمِ فِي وَقْتِ الضُّحَى.",
   "The second term of the idafa, in jarr by a kasra estimated on the alif — the intensive form is annexed to its time: «one who sleeps much in the forenoon».",
   "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr — mübalağa sîgasının zarfına izâfeti: «kuşluk vaktinde çok uyuyan»."),
 T("لَمْ", "lam-jazima", "part", ["lam-jazim"], LAM_J[0], LAM_J[1], LAM_J[2]),
 T("تَنْتَطِقْ", "intataqa", "verb", ["lam-jazim", "form-viii-verbs", "al-hal-jumla-wa-rabituha"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «نَؤُومُ»؛ الِانْتِطَاقُ: شَدُّ الْوَسَطِ بِالنِّطَاقِ.",
   "A present verb in jazm by لَمْ, its sign the sukun; its doer is a hidden «she» — the clause is a hal of the pronoun hidden in «sleeper», in the seat of nasb; الاِنْتِطَاق: to bind the waist with a girdle.",
   "لَمْ ile meczûm muzâri, cezm alâmeti sükûn; fâili gizli «hiye» — cümle «نَؤُومُ»daki gizli zamirden hâl olarak mahallen mansûb; الاِنْتِطَاق: beline kuşak bağlamak."),
 HARF_JARR("عَنْ", "an", " بِمَعْنَى «بَعْدَ»، كَمَا يُقَالُ: اسْتَغْنَى فُلَانٌ عَنْ فَقْرِهِ، أَيْ: بَعْدَ فَقْرِهِ", " — here meaning «after», as one says «he grew rich عَنْ his poverty», after it (al-Zawzanī)", " — burada «sonra» anlamında; «fakirliğinden sonra zengin oldu» denmesi gibi (Zevzenî)"),
 W("تَفَضُّلِ", "tafaddul", "noun", ["huruf-jarr", "masdar", "al-qafiya"], J(MAJR, QAFIYA, TA("تَنْتَطِقْ", "gird herself", "e"), Dn("التَّفَضُّلُ: لُبْسُ الْفُضْلَةِ، وَهِيَ ثَوْبٌ وَاحِدٌ يُلْبَسُ لِلْخِفَّةِ فِي الْعَمَلِ", "التَّفَضُّل: putting on the فُضْلَة, a single garment worn to be light for work", "التَّفَضُّل: «فُضْلَة» giymek; bu, işte hafif olmak için giyilen tek parça elbisedir")), "."),
])
V(None, 39, "She reaches for things with soft fingers, not coarse — they are like the worms of Ẓaby, or the toothsticks of the isḥil tree.",
  "Eşyayı, kaba olmayan yumuşak parmaklarla alır; onlar sanki Zaby kurtçukları ya da ishil ağacından misvaklardır.", [
 W("وَتَعْطُو", "ata-reach", "verb", ["atf-nasaq", "mudari-marfu", "thulathi-mujarrad-babs", "naqis-verbs"], J(PRE("wa", "تَعْطُو"), lo(MUDR_W), HID("هِيَ", "she", "hiye"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا؛ الْعَطْوُ: التَّنَاوُلُ", "the clause is conjoined to the one before; العَطْو: reaching out and taking", "cümle öncekine ma'tûf; العَطْو: uzanıp almak")), s=[WA, ("تَعْطُو", "ata-reach", "verb")]),
 T("بِرَخْصٍ", "rakhs", "noun", ["huruf-jarr", "sifa-mushabbaha", "hadhf-wa-taqdir", "ijaz-al-hadhf"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَرَخْصٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَعْطُو»؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: بِبَنَانٍ رَخْصٍ؛ الرَّخْصُ: اللَّيِّنُ النَّاعِمُ.",
   "The ba is a jarr letter and رَخْصٍ is in jarr by the kasra — the phrase hangs on «reaches»; it describes a noun left out: «with soft fingers»; الرَّخْص: soft and tender.",
   "Bâ cer harfi, رَخْصٍ kesre ile mecrûr — câr-mecrûr «تَعْطُو»ya müteallik; mahzûf mevsûfun na'tıdır: «yumuşak parmaklarla»; الرَّخْص: yumuşak, körpe.", s=[BI, ("رَخْصٍ", "rakhs", "noun")]),
 W("غَيْرِ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], J(("نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ", "A second adjective of the omitted noun, in jarr by the kasra", "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr"), MUD)),
 W("شَثْنٍ", "shathn", "noun", ["idafa-definiteness", "sifa-mushabbaha"], J(MI, Dn("الشَّثْنُ: الْغَلِيظُ الْكَزُّ", "الشَّثْن: thick and rough", "الشَّثْن: kalın ve sert"))),
 T("كَأَنَّهُ", "kaanna", "part", ["inna-wa-akhawatuha", "jumla-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يُفِيدُ التَّشْبِيهَ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهُ يَعُودُ عَلَى الْبَنَانِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَالِثٌ لِلْمَوْصُوفِ الْمَحْذُوفِ، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ أَنَامِلُهَا، وَالْمُشَبَّهُ بِهِ أَسَارِيعُ ظَبْيٍ أَوْ مَسَاوِيكُ الْإِسْحِلِ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ اللِّينُ وَالدِّقَّةُ وَالِاسْتِوَاءُ.",
   "كَأَنَّ is a verb-like particle of likening; the هُ is its noun, in the seat of nasb, and returns to the fingers — the clause is a third adjective of the omitted noun, in the seat of jarr, or a hal of it, in the seat of nasb. A tashbih mursal mujmal: the thing likened is her fingertips, the thing they are likened to is the worms of Ẓaby or the toothsticks of isḥil, the particle is كَأَنَّ, and the point of likeness is left unsaid — softness, slenderness and evenness (al-Zawzanī).",
   "كَأَنَّ teşbih bildiren fiile benzeyen harf; «hû» onun ismi, mahallen mansûb, parmaklara döner — cümle mahzûf mevsûfun üçüncü na'tı olarak mahallen mecrûr ya da ondan hâl olarak mahallen mansûb. Teşbih-i mürsel mücmeldir: müşebbeh onun parmak uçları, müşebbehün bih Zaby kurtçukları ya da ishil misvakları, edat كَأَنَّ; vech-i şebeh mahzûftur: yumuşaklık, incelik ve düzgünlük (Zevzenî).", HEMI, [("كَأَنَّ", "kaanna", "part"), P("هُ")]),
 W("أَسَارِيعُ", "usru", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], J(KHB_KAANNA, MUD, Dn("جَمْعُ أُسْرُوعٍ، وَيُقَالُ يُسْرُوعٌ: دُودٌ يَكُونُ فِي الْبَقْلِ وَالْأَمَاكِنِ النَّدِيَّةِ، تُشَبَّهُ أَنَامِلُ النِّسَاءِ بِهِ", "the plural of أُسْرُوع (also يُسْرُوع): a worm found among herbs and in damp places, to which women's fingertips are likened", "«أُسْرُوع»un (يُسْرُوع da denir) cem'i: sebzelerde ve nemli yerlerde bulunan bir kurtçuk; kadınların parmak uçları ona benzetilir"))),
 W("ظَبْيٍ", "zaby-place", "propn", ["idafa-definiteness"], J(MI, Dn("ظَبْيٌ: مَوْضِعٌ بِعَيْنِهِ", "Ẓaby is a particular place", "Zaby belirli bir yerin adıdır"))),
 T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «veya»."),
 W("مَسَاوِيكُ", "miswak", "noun", ["atf-nasaq", "idafa-definiteness", "jam-taksir"], J(("مَعْطُوفٌ عَلَى «أَسَارِيعُ» مَرْفُوعٌ بِالضَّمَّةِ", "Conjoined to «the worms», in raf' by the damma", "«أَسَارِيعُ»e ma'tûf, damme ile merfû"), MUD, Dn("جَمْعُ مِسْوَاكٍ", "the plural of مِسْوَاك", "«مِسْوَاك»in cem'i"))),
 W("إِسْحِلِ", "ishil", "noun", ["idafa-definiteness", "al-qafiya"], J(MI, QAFIYA, Dn("الْإِسْحِلُ: شَجَرَةٌ تَدِقُّ أَغْصَانُهَا فِي اسْتِوَاءٍ، تُشَبَّهُ الْأَصَابِعُ بِهَا فِي الدِّقَّةِ وَالِاسْتِوَاءِ", "الإِسْحِل: a tree whose twigs grow thin and straight; fingers are likened to them for slenderness and evenness", "الإِسْحِل: dalları ince ve düzgün olan bir ağaç; parmaklar incelik ve düzgünlükte ona benzetilir")), "."),
])
V(None, 40, "At nightfall she lights up the dark, as though she were the evening lamp of a monk withdrawn to his devotions.",
  "Akşamleyin karanlığı aydınlatır; sanki kendini ibadete vermiş bir rahibin akşam kandilidir.", [
 W("تُضِيءُ", "adaa-shine", "verb", ["mudari-marfu", "form-iv-verbs", "hollow-verbs"], J(MUDR, HID("هِيَ", "she", "hiye"), Dn("وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ وَالْإِضَاءَةُ تَكُونُ لَازِمَةً وَمُتَعَدِّيَةً، وَهِيَ هُنَا مُتَعَدِّيَةٌ", "a fresh sentence; أَضَاءَ is both intransitive and transitive — here transitive", "cümle müste'nefedir; أَضَاءَ hem lâzım hem müteaddî olur, burada müteaddîdir"))),
 W("الظَّلَامَ", "zalam", "noun", ["maful-bihi"], J(MAFR)),
 T("بِالْعِشَاءِ", "isha-evening", "noun", ["huruf-jarr", "ism-mamdud"], "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَالْعِشَاءِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تُضِيءُ».", "The ba is a jarr letter meaning «at»; الْعِشَاءِ is in jarr by the kasra — the phrase hangs on «lights up».", "Bâ «-de» anlamında cer harfi; الْعِشَاءِ kesre ile mecrûr — câr-mecrûr «تُضِيءُ»ya müteallik.", s=[BI, ("الْعِشَاءِ", "isha-evening", "noun")]),
 T("كَأَنَّهَا", "kaanna", "part", ["inna-wa-akhawatuha", "al-hal-jumla-wa-rabituha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يُفِيدُ التَّشْبِيهَ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «تُضِيءُ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْعَشِيقَةُ بِنُورِ وَجْهِهَا، وَالْمُشَبَّهُ بِهِ مِصْبَاحُ الرَّاهِبِ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ غَلَبَةُ النُّورِ ظَلَامَ اللَّيْلِ؛ وَخَصَّ مِصْبَاحَ الرَّاهِبِ لِأَنَّهُ يُوقِدُهُ لِيُهْتَدَى بِهِ عِنْدَ الضَّلَالِ فَهُوَ يُضِيئُهُ أَشَدَّ الْإِضَاءَةِ.",
   "كَأَنَّ is a verb-like particle of likening; هَا is its noun, in the seat of nasb — the clause is a hal of the doer of «lights up», in the seat of nasb. A tashbih mursal mujmal: the thing likened is the beloved, by the light of her face; the thing she is likened to is the monk's lamp; the particle is كَأَنَّ; the point of likeness is left unsaid — light overcoming the dark of night. He names the monk's lamp because the monk lights it to guide those who have lost the way, and so makes it burn its brightest (al-Zawzanī).",
   "كَأَنَّ teşbih bildiren fiile benzeyen harf; هَا onun ismi, mahallen mansûb — cümle «تُضِيءُ»nun fâilinden hâl olarak mahallen mansûb. Teşbih-i mürsel mücmeldir: müşebbeh yüzünün nûruyla sevgili, müşebbehün bih rahibin kandili, edat كَأَنَّ; vech-i şebeh mahzûftur: ışığın gece karanlığına galip gelmesi. Rahibin kandilini anmıştır, çünkü rahip onu yolunu şaşıranlar yol bulsun diye yakar, bu yüzden en parlak şekilde yakar (Zevzenî).", HEMI, [("كَأَنَّ", "kaanna", "part"), P("هَا")]),
 W("مَنَارَةُ", "manara", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], J(KHB_KAANNA, MUD, Dn("الْمَنَارَةُ: الْمِسْرَجَةُ، وَالْجَمْعُ الْمَنَاوِرُ وَالْمَنَائِرُ", "المَنَارَة: a lamp-stand, a lamp; plural المَنَاوِر, المَنَائِر", "المَنَارَة: kandil, kandillik; cem'i المَنَاوِر, المَنَائِر"))),
 T("مُمْسَى", "mumsa", "noun", ["idafa-definiteness", "ism-maqsur-manqus"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ " + MAQSUR_J + "، مُضَافٌ — الْمُمْسَى: بِمَعْنَى الْإِمْسَاءِ وَوَقْتِهِ جَمِيعًا.",
   "The second term of the idafa, in jarr by a kasra estimated on the alif, annexed in turn — المُمْسَى: both «coming into the evening» and its time.",
   "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr, muzâf — المُمْسَى: hem «akşama girmek» hem de bunun vakti."),
 W("رَاهِبٍ", "rahib", "noun", ["idafa-definiteness"], J(MI)),
 W("مُتَبَتِّلِ", "mutabattil", "noun", ["naat-sifa", "ism-fail", "al-qafiya"], J(NAAT("رَاهِبٍ", "jarr", en_of="a monk"), QAFIYA, Dn("الْمُتَبَتِّلُ: الْمُنْقَطِعُ إِلَى اللهِ بِنِيَّتِهِ وَعَمَلِهِ، وَالْبَتْلُ: الْقَطْعُ", "المُتَبَتِّل: one cut off for God in intent and deed; البَتْل: cutting", "المُتَبَتِّل: niyeti ve ameliyle kendini Allah'a adamış kimse; البَتْل: kesmek")), "."),
])
V(None, 41, "On the like of her a man of sense gazes long, in tender longing, when she stands tall between the wearers of the woman's shift and of the girl's frock.",
  "Onun gibisine, boyu kadın gömleği giyenlerle çocuk entarisi giyenler arasında uzayıp serpildiğinde, aklı başında adam hasretle uzun uzun bakar.", [
 HARF_JARR("إِلَى", "ila"),
 W("مِثْلِهَا", "mithl", "noun", ["huruf-jarr", "idafa-definiteness"], J(MAJR, IDF("هَا"), TA("يَرْنُو", "gazes", "ya"), Dn("وَقَدْ قُدِّمَا عَلَى الْفِعْلِ", "set before the verb", "fiilden öne alınmıştır")), s=[("مِثْلِ", "mithl", "noun"), P("هَا")]),
 W("يَرْنُو", "rana", "verb", ["mudari-marfu", "thulathi-mujarrad-babs", "naqis-verbs"], J(MUDR_W, Dn("الرُّنُوُّ: إِدَامَةُ النَّظَرِ", "الرُّنُوّ: to gaze long and steadily", "الرُّنُوّ: uzun uzun, gözünü ayırmadan bakmak"))),
 W("الْحَلِيمُ", "halim", "noun", ["fail", "sifa-mushabbaha"], J(FAILR, Dn("أَيِ: الْعَاقِلُ", "that is, the man of sense", "yani akıllı kişi"))),
 W("صَبَابَةً", "sababa", "noun", ["maful-lah", "masdar"], J(("مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ", "An object of cause, in nasb by the fatha", "Mef'ûlün lieclih, fetha ile mansûb"), Dn("أَيْ: كَلَفًا بِهَا وَحَنِينًا إِلَيْهَا", "that is, out of love for her and yearning towards her", "yani ona düşkünlükten ve özlemden")), HEMI),
 W("إِذَا", "idha", "part", ["maful-fih"], J(IDHA_Z("يَرْنُو", "gazes", "ya"))),
 T("مَا", "ma-zaida", "part", ["anwa-ma"], MA_Z[0], MA_Z[1], MA_Z[2]),
 W("اسْبَكَرَّتْ", "isbakarra", "verb", ["rubai-babs", "doubled-verbs"], J(MADI_F, HID("هِيَ", "she", "hiye"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا؛ الِاسْبِكْرَارُ: الطُّولُ وَالِامْتِدَادُ، أَيْ: طَالَ قَدُّهَا وَامْتَدَّتْ قَامَتُهَا", "the clause is in the seat of jarr, annexed to إِذَا; الاِسْبِكْرَار: length and stretching out — «when her figure grows tall»", "cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr; الاِسْبِكْرَار: uzayıp serpilmek — «boyu uzadığında»"))),
 W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], J(("ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ", "An adverb of place, in nasb by the fatha, annexed", "Mekân zarfı, fetha ile mansûb, muzâf"), Dn("مُتَعَلِّقٌ بِـ«اسْبَكَرَّتْ»", "it hangs on «stands tall»", "«اسْبَكَرَّتْ»e müteallik"))),
 T("دِرْعٍ", "dir", "noun", ["idafa-definiteness", "hadhf-al-mudaf-wal-mudaf-ilayh", "ijaz-al-hadhf"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — الدِّرْعُ: قَمِيصُ الْمَرْأَةِ، وَهُوَ مُذَكَّرٌ، وَدِرْعُ الْحَدِيدِ مُؤَنَّثَةٌ. وَالتَّقْدِيرُ: بَيْنَ لَابِسَةِ دِرْعٍ وَلَابِسَةِ مِجْوَلٍ، فَحَذَفَ الْمُضَافَ وَأَقَامَ الْمُضَافَ إِلَيْهِ مَقَامَهُ، أَيْ: بَيْنَ اللَّوَاتِي أَدْرَكْنَ الْحُلُمَ وَاللَّوَاتِي لَمْ يُدْرِكْنَهُ.",
   "The second term of the idafa, in jarr by the kasra — الدِّرْع: a woman's shift (masculine; the coat of mail is feminine). The full wording is «between her who wears a shift and her who wears a frock»: the annexed noun is dropped and its second term set in its place — between the girls who have come of age and those who have not (al-Zawzanī).",
   "Muzâfun ileyh, kesre ile mecrûr — الدِّرْع: kadın gömleği (müzekkerdir; demir zırh mânâsındaki müennestir). Takdiri: «gömlek giyen ile entari giyen arasında»; muzâf hazfedilip muzâfun ileyh onun yerine konmuştur — yani bülûğa ermiş kızlarla henüz ermemiş olanlar arasında (Zevzenî)."),
 W("وَمِجْوَلِ", "mijwal", "noun", ["atf-nasaq", "al-qafiya"], J(PRE("wa", "مِجْوَلِ"), ATF("دِرْعٍ", "a shift"), QAFIYA, Dn("الْمِجْوَلُ: ثَوْبٌ تَلْبَسُهُ الْجَارِيَةُ الصَّغِيرَةُ", "المِجْوَل: a garment worn by a little girl", "المِجْوَل: küçük kız çocuğunun giydiği elbise")), ".", [WA, ("مِجْوَلِ", "mijwal", "noun")]),
])
V(None, 42, "Men have got over the blind follies of youth — but my heart is not one to get over its love of you.",
  "Erkekler gençliğin körlüklerinden sıyrılıp teselli buldular; benim gönlüm ise senin sevgini unutacak değildir.", [
 T("تَسَلَّتْ", "tasalla", "verb", ["form-v-verbs", "naqis-verbs"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ؛ يُقَالُ: سَلَا عَنْ حَبِيبِهِ وَتَسَلَّى وَانْسَلَى، أَيْ: زَالَ حُبُّهُ مِنْ قَلْبِهِ.",
   "A past verb built on a fatha estimated on the alif that falls before the stilled ta; the ta marks the feminine — a fresh sentence; one says سَلَا, تَسَلَّى and اِنْسَلَى of a lover: the love has left his heart.",
   "Sâkin tâ sebebiyle düşen elif üzerinde takdîrî fetha üzere mebnî mâzî; tâ te'nîs için — cümle müste'nefedir; «سَلَا, تَسَلَّى, اِنْسَلَى» denir: sevgisi kalbinden gitti."),
 T("عَمَايَاتُ", "amaya", "noun", ["fail", "idafa-definiteness", "jam-muannath-salim"],
   "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — جَمْعُ عَمَايَةٍ، وَالْعَمَايَةُ وَالْعَمَى وَاحِدٌ، وَالْمُرَادُ الضَّلَالَةُ. قَالَ الزَّوْزَنِيُّ: زَعَمَ أَكْثَرُ الْأَئِمَّةِ أَنَّ فِي الْبَيْتِ قَلْبًا، تَقْدِيرُهُ: تَسَلَّتِ الرِّجَالُ عَنْ عَمَايَاتِ الصِّبَا، أَيْ: خَرَجُوا مِنْ ظُلُمَاتِهِ.",
   "The doer, in raf' by the damma, annexed — the plural of عَمَايَة, which is the same as العَمَى, blindness; error is meant. Al-Zawzanī: most of the masters hold that the verse is inverted (qalb), and stands for «men have got over the blindnesses of youth» — they have come out of its darkness.",
   "Fâil, damme ile merfû, muzâf — «عَمَايَة»nin cem'i; العَمَايَة ile العَمَى (körlük) birdir, maksat sapkınlıktır. Zevzenî: imamların çoğu beyitte kalb bulunduğunu söyler; takdiri: «erkekler gençliğin körlüklerinden sıyrıldılar», yani onun karanlıklarından çıktılar."),
 W("الرِّجَالِ", "rajul", "noun", ["idafa-definiteness", "jam-taksir"], J(MI)),
 HARF_JARR("عَنِ", "an", "، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَقِيلَ: هُوَ هُنَا بِمَعْنَى «بَعْدَ»، أَيْ: بَطَلَتْ ضَلَالَاتُ الرِّجَالِ بَعْدَ مُضِيِّ صِبَاهُمْ", ", voweled with kasra before the stilled letter; some say it means «after» here: men's errors came to nothing once their youth had passed", "; iki sâkinin karşılaşması sebebiyle kesre ile harekelenmiştir; burada «sonra» anlamında olduğu da söylenmiştir: erkeklerin sapkınlıkları gençlikleri geçtikten sonra yok olmuştur"),
 W("الصِّبَا", "siba", "noun", ["huruf-jarr", "ism-maqsur-manqus"], J(MAJR_A, TA("تَسَلَّتْ", "have got over", "e")), HEMI),
 W("وَلَيْسَ", "laysa", "verb", ["atf-nasaq", "kana-wa-akhawatuha"], J(PRE("wa", "لَيْسَ"), ("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ", "a defective past verb built on fatha", "fetha üzere mebnî nâkıs mâzî"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا", "the clause is conjoined to the one before", "cümle öncekine ma'tûf")), s=[WA, ("لَيْسَ", "laysa", "verb")]),
 W("فُؤَادِي", "fuad", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "ya-al-mutakallim"], J(("اسْمُ «لَيْسَ» مَرْفُوعٌ ", "The noun of لَيْسَ, in raf' by ", "«لَيْسَ»nin ismi; "), YA_EST("بِضَمَّةٍ", "a damma", "damme ile merfû")), s=[("فُؤَادِ", "fuad", "noun"), P("ي")]),
 HARF_JARR("عَنْ", "an"),
 T("هَوَاكِ", "hawa-passion", "noun", ["huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus", "iltifat"],
   "مَجْرُورٌ " + MAQSUR_J + "، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مُنْسَلِ». وَفِيهِ الْتِفَاتٌ مِنَ الْغَيْبَةِ فِي «مِثْلِهَا» إِلَى الْخِطَابِ.",
   "In jarr by a kasra estimated on the alif, annexed; the kaf is its second term — the phrase hangs on «one to get over». And there is an iltifāt: from the third person of «the like of her» he turns to address her.",
   "Elif üzerinde takdîrî kesre ile mecrûr, muzâf; kâf muzâfun ileyh — câr-mecrûr «مُنْسَلِ»e müteallik. Burada «مِثْلِهَا»daki gaybetten hitaba iltifât vardır.", s=[("هَوَا", "hawa-passion", "noun"), P("كِ")]),
 T("بِمُنْسَلِ", "munsal", "noun", ["kana-wa-akhawatuha", "huruf-jarr", "ism-fail", "ism-maqsur-manqus", "al-qafiya"],
   "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَمُنْسَلِ خَبَرُ «لَيْسَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ — اسْمُ فَاعِلٍ مَنْقُوصٌ مِنِ «انْسَلَى»، حُذِفَتْ يَاؤُهُ، وَتَنْوِينُهُ لِلْقَافِيَةِ.",
   "The ba is an added jarr letter that strengthens the negation; مُنْسَلِ is the predicate of لَيْسَ, in nasb by a fatha that the added letter's vowel keeps from showing — the ism fa'il of اِنْسَلَى, a noun ending in ya whose ya has dropped; its tanwin too is dropped for the rhyme.",
   "Bâ, nefyi pekiştiren zâid cer harfi; مُنْسَلِ «لَيْسَ»nin haberi; zâid harfin harekesi mahalli meşgul ettiği için takdîrî fetha ile mansûb — «اِنْسَلَى»dan ism-i fâil; yâsı düşmüş menkūs isimdir, tenvini de kafiye için düşmüştür.", ".", [BI, ("مُنْسَلِ", "munsal", "noun")]),
])
V(None, 43, "Many a stubborn adversary on your account have I turned back — sincere in his counsel for all his blaming, and sparing no pains.",
  "Senin yüzünden nice çetin hasmı geri çevirdim; o, bütün kınamasına rağmen öğüdünde samimi idi ve hiçbir çabayı esirgemiyordu.", [
 T("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ.", "A particle of opening and alerting.", "İstiftâh ve tenbih harfi."),
 T("رُبَّ", "rubba", "part", ["al-lam-wa-rubba-fil-kafiya", "huruf-jarr"],
   "حَرْفُ جَرٍّ شَبِيهٌ بِالزَّائِدِ لَا يَتَعَلَّقُ بِشَيْءٍ، وَهُوَ هُنَا لِلتَّكْثِيرِ.",
   "A near-redundant jarr letter that hangs on nothing; here it means «many a…».",
   "Zâide benzeyen, hiçbir şeye müteallik olmayan cer harfi; burada teksîr («nice») bildirir."),
 T("خَصْمٍ", "khasm", "noun", ["al-lam-wa-rubba-fil-kafiya", "mubtada-khabar"],
   "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ — وَتَقْدِيرُ لَفْظِ الْبَيْتِ: أَلَا رُبَّ خَصْمٍ أَلْوَى نَصِيحٍ عَلَى تَعْذَالِهِ غَيْرِ مُؤْتَلٍ رَدَدْتُهُ.",
   "The mubtada, in raf' by a damma that the near-redundant jarr letter's vowel keeps from showing — the verse in plain order is: «many a stubborn adversary, sincere for all his blaming, unsparing, have I turned back» (al-Zawzanī).",
   "Mübteda; zâide benzeyen cer harfinin harekesi mahalli meşgul ettiği için takdîrî damme ile merfû — beytin düz sırası şöyledir: «nice çetin, kınamasına rağmen samimi, kusur etmeyen hasmı geri çevirdim» (Zevzenî)."),
 PJ("فِيكِ", "فِي", "fi", "كِ", ("فِي", "فِي", "فِي"), "خَصْمٍ", "an adversary", "e", extra=(" لِأَنَّهُ فِي الْأَصْلِ مَصْدَرٌ، أَيْ: خَصْمٍ فِي شَأْنِكِ", ", in origin a masdar: «an adversary in what concerns you»", " (aslen masdar olduğu için): «senin hakkında hasım»")),
 T("أَلْوَى", "alwa-contentious", "noun", ["naat-sifa", "ism-maqsur-manqus", "mamnu-min-sarf"],
   "نَعْتٌ لِـ«خَصْمٍ» مَجْرُورٌ تَبَعًا لِلَّفْظِ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَيَجُوزُ رَفْعُهُ تَبَعًا لِلْمَحَلِّ — الْأَلْوَى: الشَّدِيدُ الْخُصُومَةِ، كَأَنَّهُ يَلْوِي خَصْمَهُ عَنْ دَعْوَاهُ.",
   "An adjective of «an adversary», in jarr after its wording by a fatha estimated on the alif in place of the kasra — a diptote: an adjective on أَفْعَل; it may also be read in raf', after its seat — الأَلْوَى: fierce in dispute, as if he twists his opponent away from his claim.",
   "«خَصْمٍ»in na'tı; lafza tâbi olarak, vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif olduğundan kesre yerine elif üzerinde takdîrî fetha ile mecrûr; mahalle tâbi olarak ref'i de câizdir — الأَلْوَى: husumeti şiddetli; sanki hasmını davasından büküp çevirir."),
 T("رَدَدْتُهُ", "radda", "verb", ["doubled-verbs", "al-bariz-al-muttasil", "maful-bihi", "mubtada-khabar"],
   MADI_TU[0] + "، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ؛ وَفُكَّ إِدْغَامُهُ لِاتِّصَالِهِ بِضَمِيرِ الرَّفْعِ الْمُتَحَرِّكِ.",
   MADI_TU[1] + "; the هُ is its direct object, in the seat of nasb — the clause is the predicate of the mubtada, in the seat of raf'; the doubled letter is opened out because a voweled subject pronoun is attached.",
   MADI_TU[2] + "; «hû» mef'ûlün bih, mahallen mansûb — cümle mübtedanın haberi olarak mahallen merfû; harekeli ref' zamirine bitiştiği için idgam çözülmüştür.", HEMI, [("رَدَدْتُ", "radda", "verb"), P("هُ")]),
 W("نَصِيحٍ", "nasih-sincere", "noun", ["naat-sifa", "sifa-mushabbaha"], J(NAAT("خَصْمٍ", "jarr", "2", en_of="an adversary"), Dn("النَّصِيحُ: النَّاصِحُ", "النَّصِيح: one who counsels sincerely", "النَّصِيح: içtenlikle öğüt veren"))),
 HARF_JARR("عَلَى", "ala", " بِمَعْنَى «مَعَ»، أَيْ: مَعَ فَرْطِ لَوْمِهِ إِيَّايَ", " — here «for all», «along with»: for all his excess of blame", " — burada «ile birlikte, rağmen» anlamında: beni aşırı kınamasına rağmen"),
 W("تَعْذَالِهِ", "tadhal", "noun", ["huruf-jarr", "idafa-definiteness", "masdar"], J(MAJR, IDF("هِ"), TA("نَصِيحٍ", "sincere", "e"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ التَّعْذَالُ وَالْعَذْلُ: اللَّوْمُ", "the masdar annexed to its doer; التَّعْذَال, العَذْل: blame", "masdarın fâiline izâfeti; التَّعْذَال, العَذْل: kınama")), s=[("تَعْذَالِ", "tadhal", "noun"), P("هِ")]),
 W("غَيْرِ", "ghayr", "noun", ["naat-sifa", "idafa-definiteness"], J(NAAT("خَصْمٍ", "jarr", "3", en_of="an adversary"), MUD, Dn("وَيَجُوزُ نَصْبُهُ حَالًا", "it may also be read in nasb, as a hal", "hâl olarak nasbı da câizdir"))),
 T("مُؤْتَلِ", "mutal", "noun", ["idafa-definiteness", "ism-fail", "ism-maqsur-manqus", "al-qafiya"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمُ فَاعِلٍ مَنْقُوصٌ مِنِ «ائْتَلَى»: قَصَّرَ، وَحُذِفَ تَنْوِينُهُ لِلْقَافِيَةِ، أَيْ: غَيْرِ مُقَصِّرٍ فِي النَّصِيحَةِ وَاللَّوْمِ.",
   "The second term of the idafa, in jarr by a kasra estimated on the dropped ya — the ism fa'il of اِئْتَلَى «to fall short», a noun ending in ya; its tanwin is dropped for the rhyme: «not falling short in counsel and blame».",
   "Muzâfun ileyh; düşmüş yâ üzerinde takdîrî kesre ile mecrûr — «kusur etmek» anlamındaki «اِئْتَلَى»dan ism-i fâil, menkūs isim; tenvini kafiye için düşmüştür: «öğütte ve kınamada kusur etmeyen».", "."),
])
# ==== INSERT 7-43 ABOVE ====
# =====================================================================================================================
# The night: verses 44–47
# =====================================================================================================================
V(S3, 44, "Many a night like the waves of the sea has let down its curtains upon me, with every kind of care, to try me.",
  "Nice geceler vardır ki, deniz dalgası gibi, beni sınamak için türlü kederlerle perdelerini üzerime salmıştır.", [
 T("وَلَيْلٍ", "layl", "noun", ["al-lam-wa-rubba-fil-kafiya", "anwa-al-waw", "mubtada-khabar", "hadhf-wa-taqdir"],
   "الْوَاوُ وَاوُ رُبَّ، وَلَيْلٍ مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ، وَهُوَ «رُبَّ» الْمَحْذُوفَةُ — وَبِهٰذَا الْبَيْتِ انْتَقَلَ مِنَ النَّسِيبِ إِلَى التَّمَدُّحِ بِالصَّبْرِ وَالْجَلَدِ.",
   "The waw is the waw of رُبَّ («many a…»); لَيْلٍ is the mubtada, in raf' by a damma that the kasra of the near-redundant jarr letter — the dropped رُبَّ — keeps from showing. With this verse he passes from the love-prelude to boasting of his endurance.",
   "Vâv, vâv-ı rubbe'dir; لَيْلٍ mübteda; zâide benzeyen cer harfinin — mahzûf «رُبَّ»nin — harekesi mahalli meşgul ettiği için takdîrî damme ile merfû. Bu beyitle nesîbden, sabır ve dayanıklılıkla övünmeye geçer.", s=[WA, ("لَيْلٍ", "layl", "noun")]),
 T("كَمَوْجِ", "mawj", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَمَوْجِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«لَيْلٍ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ اللَّيْلُ، وَالْمُشَبَّهُ بِهِ مَوْجُ الْبَحْرِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الْهَوْلُ وَالتَّوَحُّشُ وَنَكَارَةُ الْأَمْرِ.",
   "The kaf is a jarr letter of likening; مَوْجِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «a night». A tashbih mursal mujmal: the thing likened is the night, the thing it is likened to is the waves of the sea, the particle is the kaf, and the point of likeness is left unsaid — its terror, its wildness, its strangeness (so al-Zawzanī).",
   "Kâf teşbih bildiren cer harfi; مَوْجِ kesre ile mecrûr, muzâf — câr-mecrûr «لَيْلٍ»in mahzûf na'tına müteallik. Teşbih-i mürsel mücmeldir: müşebbeh gece, müşebbehün bih deniz dalgası, edat kâf; vech-i şebeh mahzûftur: dehşet, ürkütücülük ve işin yadırgatıcılığı (Zevzenî).", s=[KA, ("مَوْجِ", "mawj", "noun")]),
 T("الْبَحْرِ", "bahr", "noun", ["idafa-definiteness"], MI[0] + ".", MI[1] + ".", MI[2] + "."),
 T("أَرْخَى", "arkha", "verb", ["form-iv-verbs", "naqis-verbs", "mubtada-khabar"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «لَيْلٍ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ، وَيَجُوزُ أَنْ تَكُونَ نَعْتًا ثَانِيًا وَالْخَبَرُ مَحْذُوفٌ.",
   "A past verb built on a fatha estimated on the alif; its doer is a hidden pronoun returning to «a night» — the clause is the predicate of the mubtada, in the seat of raf'; it may also be a second adjective, with the predicate left out.",
   "Elif üzerinde takdîrî fetha üzere mebnî mâzî; fâili «لَيْلٍ»e dönen gizli zamir — cümle mübtedanın haberi olarak mahallen merfû; ikinci na't olup haberin mahzûf olması da câizdir."),
 T("سُدُولَهُ", "sidl", "noun", ["maful-bihi", "idafa-definiteness", "jam-taksir", "istiara", "arkan-al-istiara", "tarshih-wa-tajrid"],
   "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — جَمْعُ سِدْلٍ وَهُوَ السِّتْرُ. وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: اسْتُعِيرَتِ السُّدُولُ لِظُلُمَاتِ اللَّيْلِ (قَالَ الزَّوْزَنِيُّ: أَرْخَى عَلَيَّ سُتُورَ ظَلَامِهِ)، وَ«أَرْخَى» تَرْشِيحٌ لَهَا.",
   "The direct object, in nasb by the fatha, annexed; the هُ is its second term — the plural of سِدْل, a curtain. An explicit istiʿāra: «curtains» is borrowed for the night's darkness (al-Zawzanī: «it let down upon me the curtains of its darkness»), and «let down» carries the borrowed image further (tarshīḥ).",
   "Mef'ûlün bih, fetha ile mansûb, muzâf; «hû» muzâfun ileyh — «سِدْل»in (perde) cem'i. İstiâre-i tasrîhiyye vardır: «perdeler» gecenin karanlıkları için ödünç alınmıştır (Zevzenî: «karanlığının perdelerini üzerime saldı»); «أَرْخَى» bu istiârenin terşîhidir.", HEMI, [("سُدُولَ", "sidl", "noun"), P("هُ")]),
 T("عَلَيَّ", "ala", "prep", ["huruf-jarr", "ya-al-mutakallim"], "عَلَى حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَرْخَى».", "عَلَى is a jarr letter and the ya is in the seat of jarr — the phrase hangs on «let down».", "عَلَى cer harfi, yâ mahallen mecrûr — câr-mecrûr «أَرْخَى»ya müteallik.", s=[("عَلَيْ", "ala", "prep"), P("يَ")]),
 T("بِأَنْوَاعِ", "naw", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «مَعَ»، وَأَنْوَاعِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَرْخَى» عَلَى مَا شَرَحَهُ الزَّوْزَنِيُّ؛ وَعَلَّقَهُمَا الدُّرَّةُ بِـ«يَبْتَلِي».",
   "The ba is a jarr letter meaning «with»; أَنْوَاعِ is in jarr by the kasra, annexed — the phrase hangs on «let down», as al-Zawzanī explains it; al-Durra hangs it on «to try».",
   "Bâ «ile birlikte» anlamında cer harfi; أَنْوَاعِ kesre ile mecrûr, muzâf — câr-mecrûr, Zevzenî'nin şerhine göre «أَرْخَى»ya müteallik; Dürre ise «يَبْتَلِي»ye bağlar.", s=[BI, ("أَنْوَاعِ", "naw", "noun")]),
 T("الْهُمُومِ", "hamm", "noun", ["idafa-definiteness", "jam-taksir"], MI[0] + " — جَمْعُ هَمٍّ.", MI[1] + " — the plural of هَمّ.", MI[2] + " — «هَمّ»in cem'i."),
 T("لِيَبْتَلِي", "ibtala", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "form-viii-verbs", "naqis-verbs", "hadhf-al-maful", "al-qafiya"],
   "اللَّامُ لَامُ التَّعْلِيلِ حَرْفُ جَرٍّ، وَيَبْتَلِي فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ جَوَازًا، وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْيَاءِ، وَسُكِّنَتِ الْيَاءُ لِضَرُورَةِ الشِّعْرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَالْمَفْعُولُ مَحْذُوفٌ أَيْ: لِيَبْتَلِيَنِي — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِاللَّامِ مُتَعَلِّقٌ بِـ«أَرْخَى».",
   "The lam is the lam of purpose, a jarr letter; يَبْتَلِي is a present verb in nasb by an أَنْ that may stay unspoken; its sign is a fatha estimated on the ya, which is left still as verse allows. The doer is the hidden «it» and the object is dropped: «to try me» — the masdar so built is in jarr by the lam and hangs on «let down».",
   "Lâm ta'lîl lâmı, cer harfi; يَبْتَلِي cevâzen gizli أَنْ ile mansûb muzâri; nasb alâmeti yâ üzerinde takdîrî fethadır, yâ şiir zarûretiyle sâkin bırakılmıştır. Fâil gizli «hüve», mef'ûl mahzûftur: «beni sınasın diye» — müevvel masdar lâm ile mecrûr, «أَرْخَى»ya müteallik.", ".", [LI, ("يَبْتَلِي", "ibtala", "verb")]),
])
V(S3, 45, "So I said to it, when it stretched out its spine, and followed with its hindquarters, and heaved away with its chest:",
  "O gece belini gerip uzayınca, ardından sağrılarını sürükleyince ve göğsüyle uzaklaşınca ona dedim ki:", [
 T("فَقُلْتُ", "qala", "verb", ["atf-nasaq", "hollow-verbs", "al-bariz-al-muttasil"],
   "الْفَاءُ عَاطِفَةٌ، وَقُلْتُ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.", "The fa conjoins; قُلْتُ is a past verb built on sukun because the doer's ta is attached; the ta is the doer, in the seat of raf'.", "Fâ atıf; قُلْتُ fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, mahallen merfû.", s=[FA, ("قُلْتُ", "qala", "verb")]),
 T("لَهُ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى اللَّيْلِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قُلْتُ».", "The lam is a jarr letter and the هُ is in the seat of jarr, returning to the night — the phrase hangs on «I said».", "Lâm cer harfi, «hû» mahallen mecrûr, geceye döner — câr-mecrûr «قُلْتُ»ye müteallik.", s=[("لَ", "li", "prep"), P("هُ")]),
 T("لَمَّا", "lamma", "part", ["maful-fih"], "ظَرْفُ زَمَانٍ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«قُلْتُ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time, «when», built on sukun in the seat of nasb; it hangs on «I said» and is annexed to the clause after it.", "«حِينَ» anlamında zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «قُلْتُ»ye müteallik, sonraki cümleye muzâf."),
 T("تَمَطَّى", "tamatta", "verb", ["form-v-verbs", "naqis-verbs", "istiara", "arkan-al-istiara", "istiara-makniyya"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى اللَّيْلِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «لَمَّا» إِلَيْهَا. قَالَ الزَّوْزَنِيُّ: اسْتَعَارَ لِلَّيْلِ صُلْبًا، وَاسْتَعَارَ لِطُولِهِ لَفْظَ التَّمَطِّي لِيُلَائِمَ الصُّلْبَ، وَاسْتَعَارَ لِأَوَائِلِهِ لَفْظَ الْكَلْكَلِ وَلِمَآخِيرِهِ لَفْظَ الْأَعْجَازِ؛ فَهِيَ اسْتِعَارَاتٌ تَصْرِيحِيَّةٌ، وَيَصِحُّ إِجْرَاؤُهَا مَكْنِيَّةً: شُبِّهَ اللَّيْلُ بِحَيَوَانٍ ذِي صُلْبٍ وَأَعْجَازٍ وَكَلْكَلٍ ثُمَّ حُذِفَ وَرُمِزَ إِلَيْهِ بِلَوَازِمِهِ.",
   "A past verb built on a fatha estimated on the alif; its doer is a hidden pronoun returning to the night — the clause is in the seat of jarr, annexed to لَمَّا. Al-Zawzanī: he borrowed a spine for the night, borrowed «stretching» for its length to suit the spine, and borrowed «chest» for its first parts and «hindquarters» for its last. These are explicit istiʿāras; they may also be read as an istiʿāra by kināya — the night likened to a beast with spine, hindquarters and chest, the beast dropped and hinted at by what belongs to it.",
   "Elif üzerinde takdîrî fetha üzere mebnî mâzî; fâili geceye dönen gizli zamir — cümle «لَمَّا»nın muzâfun ileyhi olarak mahallen mecrûr. Zevzenî: geceye bir bel ödünç almış, uzunluğu için — bele uysun diye — «gerinme» lafzını, başları için «göğüs», sonları için «sağrılar» lafzını istiâre etmiştir. Bunlar tasrîhî istiârelerdir; mekniyye olarak da yürütülebilir: gece, beli, sağrıları ve göğsü olan bir hayvana benzetilmiş, sonra o hazfedilip levâzımıyla ona işaret edilmiştir."),
 T("بِصُلْبِهِ", "sulb-back", "noun", ["huruf-jarr", "idafa-definiteness", "istiara"],
   "الْبَاءُ حَرْفُ جَرٍّ لِلتَّعْدِيَةِ، وَصُلْبِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَمَطَّى»؛ وَالصُّلْبُ مُسْتَعَارٌ لِلَّيْلِ.", "The ba is a jarr letter that makes the verb transitive; صُلْبِ is in jarr by the kasra, annexed, and the هِ is its second term — the phrase hangs on «stretched»; the spine is borrowed for the night.", "Bâ ta'diye için cer harfi; صُلْبِ kesre ile mecrûr, muzâf; «hî» muzâfun ileyh — câr-mecrûr «تَمَطَّى»ya müteallik; bel, gece için istiâre edilmiştir.", HEMI, [BI, ("صُلْبِ", "sulb-back", "noun"), P("هِ")]),
 T("وَأَرْدَفَ", "ardafa", "verb", ["atf-nasaq", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَأَرْدَفَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «تَمَطَّى» فِي مَحَلِّ جَرٍّ؛ أَرْدَفَ: أَتْبَعَ.", "The waw conjoins; أَرْدَفَ is a past verb built on fatha with a hidden doer — the clause is conjoined to «it stretched», in the seat of jarr; أَرْدَفَ: it made follow.", "Vâv atıf; أَرْدَفَ fetha üzere mebnî mâzî, fâili gizli zamir — cümle «تَمَطَّى» cümlesine ma'tûf, mahallen mecrûr; أَرْدَفَ: ardından getirdi.", s=[WA, ("أَرْدَفَ", "ardafa", "verb")]),
 T("أَعْجَازًا", "ajuz", "noun", ["maful-bihi", "jam-taksir", "istiara"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ عَجُزٍ، مُسْتَعَارٌ لِمَآخِيرِ اللَّيْلِ.", "The direct object, in nasb by the fatha — the plural of عَجُز, borrowed for the last parts of the night.", "Mef'ûlün bih, fetha ile mansûb — «عَجُز»ün cem'i; gecenin son kısımları için istiâre edilmiştir."),
 T("وَنَاءَ", "naa-weigh", "verb", ["atf-nasaq", "hollow-verbs"], "الْوَاوُ عَاطِفَةٌ، وَنَاءَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — قَالَ الزَّوْزَنِيُّ: مَقْلُوبُ «نَأَى» بِمَعْنَى بَعُدَ؛ وَقِيلَ: نَهَضَ بِثِقَلٍ.", "The waw conjoins; نَاءَ is a past verb built on fatha with a hidden doer — al-Zawzanī: it is نَأَى turned about, «was far»; others: «rose under a weight».", "Vâv atıf; نَاءَ fetha üzere mebnî mâzî, fâili gizli zamir — Zevzenî: «uzaklaştı» anlamındaki «نَأَى»nın maklûbudur; «ağırlıkla doğruldu» da denmiştir.", s=[WA, ("نَاءَ", "naa-weigh", "verb")]),
 T("بِكَلْكَلِ", "kalkal", "noun", ["huruf-jarr", "istiara", "al-qafiya"], "الْبَاءُ حَرْفُ جَرٍّ لِلتَّعْدِيَةِ، وَكَلْكَلِ مَجْرُورٌ بِالْكَسْرَةِ" + QAFIYA[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«نَاءَ»؛ وَالْكَلْكَلُ (الصَّدْرُ) مُسْتَعَارٌ لِأَوَائِلِ اللَّيْلِ.", "The ba is a jarr letter that makes the verb transitive; كَلْكَلِ is in jarr by the kasra" + QAFIYA[1] + " — the phrase hangs on «heaved away»; the chest is borrowed for the first parts of the night.", "Bâ ta'diye için cer harfi; كَلْكَلِ kesre ile mecrûr" + QAFIYA[2] + " — câr-mecrûr «نَاءَ»ye müteallik; göğüs, gecenin ilk kısımları için istiâre edilmiştir.", ":", [BI, ("كَلْكَلِ", "kalkal", "noun")]),
])
V(S3, 46, "«O long night, do clear away into a morning — though the morning is no better than you.»",
  "«Ey uzun gece! Haydi artık bir sabahla açıl; gerçi sabah da senden daha iyi değil.»", [
 T("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "حَرْفُ اسْتِفْتَاحٍ وَتَنْبِيهٍ.", "A particle of opening and alerting.", "İstiftâh ve tenbih harfi."),
 T("أَيُّهَا", "ayyuha", "noun", ["vocative-munada", "huruf-tanbih", "hadhf-wa-taqdir"],
   "مُنَادًى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، حُذِفَ مِنْهُ حَرْفُ النِّدَاءِ، وَهَا لِلتَّنْبِيهِ — قَالَ الزَّوْزَنِيُّ: وَخِطَابُهُ مَا لَا يَعْقِلُ يَدُلُّ عَلَى فَرْطِ الْوَلَهِ وَشِدَّةِ التَّحَيُّرِ.",
   "A vocative — an intended indefinite built on damma in the seat of nasb, its particle dropped; هَا alerts. Al-Zawzanī: his speaking to what has no mind shows the excess of his distraction and bewilderment.",
   "Münâdâ — nekre-i maksûde, damme üzere mebnî, mahallen mansûb; nidâ harfi mahzûf, هَا tenbih için. Zevzenî: akılsız varlığa hitabı, aşırı şaşkınlığına ve hayretinin şiddetine delâlet eder."),
 T("اللَّيْلُ", "layl", "noun", ["badal", "vocative-munada", "tibaq"], "بَدَلٌ مِنْ «أَيُّ» أَوْ عَطْفُ بَيَانٍ مَرْفُوعٌ بِالضَّمَّةِ تَبَعًا لِلَّفْظِ — وَبَيْنَ اللَّيْلِ وَالصُّبْحِ طِبَاقٌ.", "A badal of أَيّ, or its explanatory apposition, in raf' by the damma after the wording — night and morning make a tibaq.", "«أَيّ»den bedel ya da atf-ı beyân; lafza tâbi olarak damme ile merfû — gece ile sabah arasında tıbâk vardır."),
 T("الطَّوِيلُ", "tawil-long", "noun", ["naat-sifa", "sifa-mushabbaha"], "نَعْتٌ لِـ«اللَّيْلُ» مَرْفُوعٌ بِالضَّمَّةِ.", "An adjective of «the night», in raf' by the damma.", "«اللَّيْلُ»in na'tı, damme ile merfû."),
 T("أَلَا", "ala-tanbih", "part", ["huruf-tanbih"], "حَرْفُ تَنْبِيهٍ مُؤَكِّدٌ لِلْأَوَّلِ.", "A particle of alerting, strengthening the first.", "Birincisini pekiştiren tenbih harfi."),
 T("انْجَلِي", "injala", "verb", ["imperative-amr", "al-amr-wa-wujuhuh", "insha-wa-tamanni", "form-vii-verbs", "naqis-verbs", "al-qafiya"],
   "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْيَاءُ الْمَكْتُوبَةُ إِشْبَاعٌ لِكَسْرَةِ اللَّامِ لِضَرُورَةِ الشِّعْرِ، وَبِهِ وَافَقَتِ الْعَرُوضُ الضَّرْبَ فِي الرَّوِيِّ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ مَعَ النِّدَاءِ مَقُولُ الْقَوْلِ. وَالْأَمْرُ هُنَا لِلتَّمَنِّي، وَبِهٰذَا الْبَيْتِ مَثَّلَ التَّلْخِيصُ لَهُ.",
   "An imperative built on dropping its weak letter (the ya); the ya that is written only lengthens the lam's kasra, by poetic licence — and so the first half-verse ends on the rhyme letter of the second; its doer is the hidden «you» — the clause, with the call, is what was said. The command here is a wish (tamannī): the Talkhīṣ cites this very verse for it.",
   "İllet harfinin (yâ) hazfi üzere mebnî emir; yazılan yâ, şiir zarûretiyle lâmın kesresinin işbâıdır; böylece birinci mısraın sonu revîde ikincinin sonuna uymuştur; fâili vücûben gizli «ente» — cümle, nidâ ile birlikte mekūlü'l-kavldir. Emir burada temennî içindir; Telhîs buna bu beyti örnek verir.", HEMI),
 T("بِصُبْحٍ", "subh", "noun", ["huruf-jarr", "tibaq"], "الْبَاءُ حَرْفُ جَرٍّ، وَصُبْحٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«انْجَلِ»؛ وَيُطَابِقُ «اللَّيْلُ».", "The ba is a jarr letter and صُبْحٍ is in jarr by the kasra — the phrase hangs on «clear away»; the contrary of «the night».", "Bâ cer harfi, صُبْحٍ kesre ile mecrûr — câr-mecrûr «انْجَلِ»ye müteallik; «اللَّيْلُ»in zıddı.", s=[BI, ("صُبْحٍ", "subh", "noun")]),
 T("وَمَا", "ma-hijaziyya", "part", ["ma-la-mushabbaha", "al-hal-jumla-wa-rabituha", "anwa-al-waw"], "الْوَاوُ وَاوُ الْحَالِ، وَمَا نَافِيَةٌ حِجَازِيَّةٌ تَعْمَلُ عَمَلَ لَيْسَ.", "The waw is the waw of the hal; مَا is the Hijazi negation, governing as لَيْسَ does.", "Vâv hâliye; مَا, leyse gibi amel eden Hicâzî nefy edatı.", s=[WA, ("مَا", "ma-hijaziyya", "part")]),
 T("الْإِصْبَاحُ", "isbah", "noun", ["ma-la-mushabbaha", "masdar"], "اسْمُ مَا مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of مَا, in raf' by the damma.", "Mâ'nın ismi, damme ile merfû."),
 T("مِنْكَ", "min", "prep", ["huruf-jarr"], "مِنْ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَمْثَلِ».", "مِنْ is a jarr letter and the kaf is in the seat of jarr — the phrase hangs on «better».", "مِنْ cer harfi, kâf mahallen mecrûr — câr-mecrûr «أَمْثَلِ»e müteallik.", s=[("مِنْ", "min", "prep"), P("كَ")]),
 T("بِأَمْثَلِ", "amthal", "noun", ["ma-la-mushabbaha", "huruf-jarr", "ism-tafdil", "mamnu-min-sarf", "al-qafiya"],
   "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَأَمْثَلِ خَبَرُ مَا مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ — وَجُرَّ لَفْظُهُ بِالْكَسْرَةِ لِلْقَافِيَةِ، وَحَقُّهُ الْفَتْحَةُ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ. وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
   "The ba is an added jarr letter that strengthens the negation; أَمْثَلِ is the predicate of مَا, in nasb by a fatha that the added letter's vowel keeps from showing — and it wears the kasra for the rhyme, though as a diptote (an adjective on أَفْعَل) it would take the fatha. The clause is a hal, in the seat of nasb.",
   "Bâ, nefyi pekiştiren zâid cer harfi; أَمْثَلِ mâ'nın haberi; zâid harfin harekesi mahalli meşgul ettiği için takdîrî fetha ile mansûb — lafzı kafiye için kesrelidir; vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif olduğundan aslında fetha alırdı. Cümle hâl olarak mahallen mansûb.", ".", [BI, ("أَمْثَلِ", "amthal", "noun")]),
])
V(S3, 47, "What a night you are! — as though its stars were bound with ropes of flax to solid rocks.",
  "Ne gecesin sen! Sanki yıldızları keten halatlarla sert kayalara bağlanmış.", [
 T("فَيَا", "ya-nida", "part", ["vocative-munada"],
   "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَيَا حَرْفُ تَنْبِيهٍ يُرَادُ بِهِ التَّعَجُّبُ؛ وَقِيلَ: حَرْفُ نِدَاءٍ وَالْمُنَادَى مَحْذُوفٌ.", "The fa opens a new sentence; يَا is a particle of alerting used for wonder — or, it is said, a vocative particle whose noun is left out.", "Fâ istînâfiyye; يَا taaccüb için kullanılan tenbih harfi — «nidâ harfidir, münâdâsı mahzûftur» da denmiştir.", s=[FA, ("يَا", "ya-nida", "part")]),
 T("لَكَ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ تَقْدِيرُهُ: أَعْجَبُ لَكَ.", "The lam is a jarr letter and the kaf is in the seat of jarr — the phrase hangs on an omitted «I wonder at you».", "Lâm cer harfi, kâf mahallen mecrûr — câr-mecrûr, takdiri «sana şaşarım» olan mahzûfa müteallik.", s=[("لَ", "li", "prep"), P("كَ")]),
 HARF_JARR("مِنْ", "min", " زَائِدٌ", " — added", " — zâid"),
 T("لَيْلٍ", "layl", "noun", ["tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ.", "A tamyiz, in nasb by a fatha that the added jarr letter's kasra keeps from showing.", "Temyiz; zâid cer harfinin harekesi mahalli meşgul ettiği için takdîrî fetha ile mansûb."),
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "kinaya"],
   "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شُبِّهَتِ النُّجُومُ فِي ثَبَاتِهَا بِأَشْيَاءَ شُدَّتْ بِالْحِبَالِ إِلَى الصُّخُورِ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ عَدَمُ الزَّوَالِ؛ وَذٰلِكَ كِنَايَةٌ عَنْ طُولِ اللَّيْلِ. وَالْجُمْلَةُ نَعْتٌ لِـ«لَيْلٍ».",
   "The verb-like particle of likening. A tashbih mursal mujmal: the stars, in their stillness, are likened to things bound by ropes to rocks; the particle is كَأَنَّ, and the point of likeness — not moving from their places — is left unsaid; and all of it is a kinaya for the length of the night. The clause qualifies «a night».",
   "Teşbih bildiren fiile benzeyen harf. Teşbih-i mürsel mücmeldir: yıldızlar, yerlerinde sabit duruşlarıyla, halatlarla kayalara bağlanmış şeylere benzetilmiştir; edat كَأَنَّ, vech-i şebeh — yerinden ayrılmamak — mahzûftur; bu da gecenin uzunluğundan kinâyedir. Cümle «لَيْلٍ»in na'tıdır."),
 T("نُجُومَهُ", "najm", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], "اسْمُ كَأَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The noun of كَأَنَّ, in nasb by the fatha, annexed; the هُ is its second term.", "كَأَنَّ'nin ismi, fetha ile mansûb, muzâf; «hû» muzâfun ileyh.", HEMI, [("نُجُومَ", "najm", "noun"), P("هُ")]),
 T("بِأَمْرَاسِ", "maras", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", "ijaz-al-hadhf", "hadhf-wa-taqdir"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَأَمْرَاسِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلٍ مَحْذُوفٍ تَقْدِيرُهُ «شُدَّتْ»، وَجُمْلَتُهُ خَبَرُ كَأَنَّ؛ حُذِفَ الْفِعْلُ لِدَلَالَةِ الْكَلَامِ عَلَيْهِ، وَهُوَ إِيجَازُ حَذْفٍ.",
   "The ba is a jarr letter; أَمْرَاسِ is in jarr by the kasra, annexed — the phrase hangs on an omitted verb, «were bound», whose clause is the predicate of كَأَنَّ; the verb is dropped because the words point to it — brevity by omission.",
   "Bâ cer harfi; أَمْرَاسِ kesre ile mecrûr, muzâf — câr-mecrûr, takdiri «شُدَّتْ» olan mahzûf fiile müteallik; o cümle كَأَنَّ'nin haberidir. Söz ona delâlet ettiği için fiil hazfedilmiştir: îcâz-ı hazif.", s=[BI, ("أَمْرَاسِ", "maras", "noun")]),
 T("كَتَّانٍ", "kattan", "noun", ["idafa-definiteness"], MI[0] + " — مِنْ إِضَافَةِ الْبَعْضِ إِلَى الْكُلِّ، أَيْ: بِأَمْرَاسٍ مِنْ كَتَّانٍ.", MI[1] + " — the part annexed to the whole: «ropes of flax».", MI[2] + " — parçanın bütüne izâfeti: «ketenden halatlar»."),
 HARF_JARR("إِلَى", "ila"),
 T("صُمِّ", "asamm", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِالْفِعْلِ الْمَحْذُوفِ؛ جَمْعُ أَصَمَّ وَهُوَ الصُّلْبُ.", "In jarr by the kasra, annexed — the phrase hangs on the omitted verb; the plural of أَصَمّ, «solid».", "Kesre ile mecrûr, muzâf — câr-mecrûr mahzûf fiile müteallik; «sert, som» anlamındaki «أَصَمّ»in cem'i."),
 T("جَنْدَلِ", "jandal", "noun", ["idafa-definiteness", "al-qafiya"], MI[0] + QAFIYA[0] + " — مِنْ إِضَافَةِ الصِّفَةِ إِلَى مَوْصُوفِهَا.", MI[1] + QAFIYA[1] + " — the adjective is annexed to the noun it describes.", MI[2] + QAFIYA[2] + " — sıfatın mevsûfuna izâfeti.", "."),
])


# =====================================================================================================================
# The water-skin, the empty valley and the wolf: verses 48–51 (they close the chapter that the night opens)
# =====================================================================================================================
RUBBA_MUB = ("مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الشَّبِيهِ بِالزَّائِدِ، وَهُوَ «رُبَّ» الْمَحْذُوفَةُ",
             "the mubtada, in raf' by a damma that the kasra of the near-redundant jarr letter — the dropped رُبَّ — keeps from showing",
             "mübteda; zâide benzeyen cer harfinin — mahzûf «رُبَّ»nin — harekesi mahalli meşgul ettiği için takdîrî damme ile merfû")
V(None, 48, "Many a water-skin of the tribe have I carried, its strap laid on a shoulder of mine that is broken in and has borne the saddle many a time.",
  "Kavmin nice su kırbasını taşıdım; askısını, alışmış ve defalarca semer vurulmuş omzuma koydum.", [
 T("وَقِرْبَةِ", "qirba", "noun", ["al-lam-wa-rubba-fil-kafiya", "anwa-al-waw", "mubtada-khabar", "hadhf-wa-taqdir", "idafa-definiteness", "istiara", "arkan-al-istiara"],
   "الْوَاوُ وَاوُ رُبَّ، وَقِرْبَةِ " + RUBBA_MUB[0] + "، مُضَافٌ، وَخَبَرُهُ مَحْذُوفٌ. قَالَ الزَّوْزَنِيُّ: لَمْ يَرْوِ جُمْهُورُ الْأَئِمَّةِ هٰذِهِ الْأَبْيَاتَ الْأَرْبَعَةَ فِي هٰذِهِ الْقَصِيدَةِ، وَزَعَمُوا أَنَّهَا لِتَأَبَّطَ شَرًّا، وَرَوَاهَا بَعْضُهُمْ هُنَا. وَفِي الْمَعْنَى قَوْلَانِ: أَحَدُهُمَا أَنَّهُ تَمَدَّحَ بِتَحَمُّلِ أَثْقَالِ الْحُقُوقِ وَنَوَائِبِ الْأَقْوَامِ، فَاسْتَعَارَ حَمْلَ الْقِرْبَةِ لِتَحَمُّلِ الْحُقُوقِ — وَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ؛ وَالْآخَرُ أَنَّهُ تَمَدَّحَ بِخِدْمَتِهِ الرُّفَقَاءَ فِي السَّفَرِ وَحَمْلِهِ سِقَاءَ الْمَاءِ، فَالْكَلَامُ عَلَى حَقِيقَتِهِ.",
   "The waw is the waw of رُبَّ («many a…»); قِرْبَةِ is " + RUBBA_MUB[1] + "; it is annexed, and its predicate is left out. Al-Zawzanī: most of the masters do not transmit these four verses in this poem and hold them to be by Taʾabbaṭa Sharran; some transmit them here. The sense is read two ways. On the first he boasts of bearing the burdens of dues and of the tribe's misfortunes, and borrows the carrying of the water-skin for the bearing of dues — an explicit istiʿāra. On the second he boasts of serving his companions on a journey and carrying their water, and the words are literal.",
   "Vâv, vâv-ı rubbe'dir; قِرْبَةِ " + RUBBA_MUB[2] + "; muzâftır, haberi mahzûftur. Zevzenî: imamların çoğu bu dört beyti bu kasidede rivayet etmez, Teebbeta Şerran'a ait sayar; kimileri burada rivayet eder. Mânâda iki görüş vardır: birincisine göre hakların ve kavmin musibetlerinin yükünü taşımakla övünmüş, kırba taşımayı hakları yüklenmek için istiâre etmiştir — bu, istiâre-i tasrîhiyyedir; ikincisine göre yolculukta arkadaşlarına hizmet edip su tulumunu taşımakla övünmüştür; o takdirde söz hakikattir.", s=[WA, ("قِرْبَةِ", "qirba", "noun")]),
 W("أَقْوَامٍ", "qawm", "noun", ["idafa-definiteness", "jam-taksir"], J(MI)),
 W("جَعَلْتُ", "jaala", "verb", ["al-bariz-al-muttasil", "jumla-sifa"], J(MADI_TU, Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«قِرْبَةِ» عَلَى اللَّفْظِ، أَوْ فِي مَحَلِّ رَفْعٍ عَلَى الْمَحَلِّ", "the clause qualifies «a water-skin» — in the seat of jarr after its wording, or of raf' after its seat", "cümle «قِرْبَةِ»nin na'tıdır; lafza göre mahallen mecrûr, mahalle göre merfû"))),
 W("عِصَامَهَا", "isam", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, IDF("هَا"), Dn("الْعِصَامُ: وِكَاءُ الْقِرْبَةِ، وَالْجَمْعُ الْعُصُمُ", "العِصَام: the strap or tie of a water-skin; plural العُصُم", "العِصَام: kırbanın bağı, askısı; cem'i العُصُم")), HEMI, [("عِصَامَ", "isam", "noun"), P("هَا")]),
 HARF_JARR("عَلَى", "ala"),
 W("كَاهِلٍ", "kahil", "noun", ["huruf-jarr"], J(MAJR, TA("جَعَلْتُ", "I laid", "ya"), Dn("الْكَاهِلُ: أَعْلَى الظَّهْرِ عِنْدَ مُرَكَّبِ الْعُنُقِ فِيهِ", "الكَاهِل: the top of the back, where the neck is set into it", "الكَاهِل: sırtın, boynun oturduğu en üst kısmı"))),
 T("مِنِّي", "min", "prep", ["huruf-jarr", "ya-al-mutakallim", "naat-sifa"], "مِنْ حَرْفُ جَرٍّ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«كَاهِلٍ».", "مِنْ is a jarr letter and the ya is in the seat of jarr — the phrase hangs on an omitted adjective of «a shoulder».", "مِنْ cer harfi, yâ mahallen mecrûr — câr-mecrûr «كَاهِلٍ»in mahzûf na'tına müteallik.", s=[("مِنِّ", "min", "prep"), P("ي")]),
 T("ذَلُولٍ", "dhalul", "noun", ["naat-sifa", "sighat-mubalagha", "kinaya", "aqsam-al-kinaya"],
   "نَعْتٌ ثَانٍ لِـ«كَاهِلٍ» مَجْرُورٌ بِالْكَسْرَةِ — الذَّلُولُ: الْمُنْقَادُ الَّذِي قَدْ رِيضَ. وَعَبَّرَ بِكَوْنِ الْكَاهِلِ ذَلُولًا مُرَحَّلًا عَنِ اعْتِيَادِهِ تَحَمُّلَ الْحُقُوقِ — وَهِيَ كِنَايَةٌ عَنْ صِفَةٍ.",
   "A second adjective of «a shoulder», in jarr by the kasra — الذَّلُول: tractable, broken in. By calling the shoulder broken in and often saddled he expresses how used he is to bearing dues (al-Zawzanī) — a kinaya for a quality.",
   "«كَاهِلٍ»in ikinci na'tı, kesre ile mecrûr — الذَّلُول: boyun eğmiş, alıştırılmış. Omzun alışmış ve semerlenmiş oluşuyla, hakları yüklenmeye alışkanlığını ifade etmiştir (Zevzenî) — bu, sıfattan kinâyedir."),
 W("مُرَحَّلِ", "murahhal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(NAAT("كَاهِلٍ", "jarr", "3", en_of="a shoulder"), QAFIYA, Dn("التَّرْحِيلُ: مُبَالَغَةُ الرَّحْلِ، يُقَالُ: رَحَّلْتُهُ إِذَا كَرَّرْتَ رَحْلَهُ، أَيْ: قَدْ رُحِلَ مَرَّةً بَعْدَ أُخْرَى", "التَّرْحِيل is the intensive of الرَّحْل «to saddle»: saddled time after time", "التَّرْحِيل, «semer vurmak» anlamındaki الرَّحْل'in mübalağasıdır: defalarca semerlenmiş")), "."),
])
V(None, 49, "Many a valley, bare as the belly of the wild ass, have I crossed, where the wolf howled like an outcast gambler with many mouths to feed.",
  "Yaban eşeğinin karnı gibi bomboş nice vadiyi aştım; orada kurt, çoluk çocuğu çok, kovulmuş bir kumarbaz gibi uluyordu.", [
 T("وَوَادٍ", "wadi-valley", "noun", ["al-lam-wa-rubba-fil-kafiya", "anwa-al-waw", "mubtada-khabar", "hadhf-wa-taqdir", "ism-maqsur-manqus"],
   "الْوَاوُ وَاوُ رُبَّ، وَوَادٍ " + RUBBA_MUB[0] + " — وَهُوَ اسْمٌ مَنْقُوصٌ حُذِفَتْ يَاؤُهُ لِلتَّنْوِينِ.",
   "The waw is the waw of رُبَّ; وَادٍ is " + RUBBA_MUB[1] + " — a noun ending in ya, whose ya has dropped before the tanwin.",
   "Vâv, vâv-ı rubbe'dir; وَادٍ " + RUBBA_MUB[2] + " — tenvin sebebiyle yâsı düşmüş menkūs isimdir.", s=[WA, ("وَادٍ", "wadi-valley", "noun")]),
 T("كَجَوْفِ", "jawf", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "tashbih", "arkan-al-tashbih", "wajh-al-shabah"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَجَوْفِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«وَادٍ». الْجَوْفُ: بَاطِنُ الشَّيْءِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ: الْمُشَبَّهُ الْوَادِي، وَالْمُشَبَّهُ بِهِ جَوْفُ الْعَيْرِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ الْخَلَاءُ، وَقَدْ دَلَّ عَلَيْهِ بِقَوْلِهِ «قَفْرٍ».",
   "The kaf is a jarr letter of likening; جَوْفِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of «a valley». الجَوْف: the inside of a thing. A tashbih mursal: the thing likened is the valley, the thing it is likened to is the belly of the ass, the particle is the kaf, and the point of likeness is emptiness — which he points to with «bare».",
   "Kâf teşbih bildiren cer harfi; جَوْفِ kesre ile mecrûr, muzâf — câr-mecrûr «وَادٍ»in mahzûf na'tına müteallik. الجَوْف: bir şeyin içi. Teşbih-i mürseldir: müşebbeh vadi, müşebbehün bih eşeğin karnı, edat kâf; vech-i şebeh boşluktur, buna «قَفْرٍ» sözüyle işaret etmiştir.", s=[KA, ("جَوْفِ", "jawf", "noun")]),
 T("الْعَيْرِ", "ayr", "noun", ["idafa-definiteness"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — الْعَيْرُ: الْحِمَارُ. قِيلَ: شَبَّهَ الْوَادِيَ فِي خَلَائِهِ مِنَ الْإِنْسِ بِبَطْنِ الْحِمَارِ الْوَحْشِيِّ إِذَا خَلَا مِنَ الْعَلَفِ؛ وَقِيلَ: فِي قِلَّةِ الِانْتِفَاعِ بِهِ؛ وَقِيلَ: أَرَادَ «كَجَوْفِ حِمَارٍ» وَهُوَ رَجُلٌ مِنْ بَقِيَّةِ عَادٍ أُحْرِقَ وَادِيهِ فَلَمْ يُنْبِتْ شَيْئًا، فَغَيَّرَ اللَّفْظَ لِإِقَامَةِ الْوَزْنِ.",
   "The second term of the idafa, in jarr by the kasra — العَيْر: the ass. Some say he likens the valley, empty of people, to the belly of the wild ass when empty of fodder; some, that the likeness is in being of little use; and some, that he meant «the hollow of Ḥimār» — a man of the remnant of ʿĀd whose valley was burnt and grew nothing after — and changed the word to keep the metre (al-Zawzanī).",
   "Muzâfun ileyh, kesre ile mecrûr — العَيْر: eşek. Kimine göre vadiyi, insandan hâlî oluşunda, yemden boşalmış yaban eşeğinin karnına benzetmiştir; kimine göre benzerlik faydasının azlığındadır; kimine göre de «Himâr'ın vadisi gibi» demek istemiş — Himâr, Âd kalıntılarından bir adamdır; vadisi yakılmış, bir daha ot bitirmemiştir — vezni tutturmak için lafzı değiştirmiştir (Zevzenî)."),
 W("قَفْرٍ", "qafr", "noun", ["naat-sifa"], J(NAAT("وَادٍ", "jarr", "2", en_of="a valley"), Dn("الْقَفْرُ: الْمَكَانُ الْخَالِي، وَالْجَمْعُ الْقِفَارُ", "القَفْر: an empty place; plural القِفَار", "القَفْر: boş, ıssız yer; cem'i القِفَار"))),
 T("قَطَعْتُهُ", "qataa", "verb", ["al-bariz-al-muttasil", "maful-bihi", "mubtada-khabar"],
   MADI_TU[0] + "، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ، أَيْ: طَوَيْتُهُ سَيْرًا؛ وَيَجُوزُ أَنْ تَكُونَ نَعْتًا ثَالِثًا لِـ«وَادٍ» وَالْخَبَرُ مَحْذُوفٌ، وَالْأَوَّلُ أَوْلَى.",
   MADI_TU[1] + "; the هُ is its direct object, in the seat of nasb — the clause is the predicate of the mubtada, in the seat of raf': «I crossed it, travelling»; it may also be a third adjective of «a valley», the predicate being left out — the first reading is the better.",
   MADI_TU[2] + "; «hû» mef'ûlün bih, mahallen mansûb — cümle mübtedanın haberi olarak mahallen merfû: «onu yürüyerek aştım»; «وَادٍ»in üçüncü na'tı olması, haberin de mahzûf sayılması câizdir; ilki evlâdır.", HEMI, [("قَطَعْتُ", "qataa", "verb"), P("هُ")]),
 PJ("بِهِ", "بِ", "bi", "هِ", BA3, "يَعْوِي", "howled", "ye", extra=("؛ وَالْبَاءُ بِمَعْنَى «فِي»", "; the ba means «in»", "; bâ «-de» anlamındadır")),
 W("الذِّئْبُ", "dhib", "noun", ["mubtada-khabar", "al-hal-jumla-wa-rabituha"], J(("مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, in raf' by the damma", "Mübteda, damme ile merfû"), Dn("وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْهَاءِ فِي «قَطَعْتُهُ»، وَالرَّابِطُ الضَّمِيرُ فِي «بِهِ»", "the nominal clause is a hal of the هُ in «I crossed it», in the seat of nasb, tied to it by the pronoun in «in it»", "isim cümlesi «قَطَعْتُهُ»daki «hû»dan hâl olarak mahallen mansûb; râbıt «بِهِ»deki zamirdir"))),
 W("يَعْوِي", "awa", "verb", ["mudari-marfu", "thulathi-mujarrad-babs", "naqis-verbs", "mubtada-khabar"], J(MUDR_Y, HID("هُوَ", "it", "hüve", ("الذِّئْبِ", "the wolf", "kurda")), Dn("وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «الذِّئْبُ»؛ الْعُوَاءُ: صَوْتُ الذِّئْبِ وَمَا أَشْبَهَهُ مِنَ السِّبَاعِ", "the clause is the predicate of «the wolf», in the seat of raf'; العُوَاء: the cry of the wolf and beasts like it", "cümle «الذِّئْبُ»ün haberi olarak mahallen merfû; العُوَاء: kurdun ve benzeri yırtıcıların sesi"))),
 T("كَالْخَلِيعِ", "khali-outcast", "noun", ["huruf-jarr", "maful-mutlaq", "hadhf-wa-taqdir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَالْخَلِيعِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: يَعْوِي عُوَاءً كَعُوَاءِ الْخَلِيعِ. الْخَلِيعُ: الَّذِي خَلَعَهُ أَهْلُهُ لِخُبْثِهِ، وَزَعَمَ الْأَئِمَّةُ أَنَّهُ فِي هٰذَا الْبَيْتِ الْمُقَامِرُ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الذِّئْبُ فِي عُوَائِهِ مِنْ فَرْطِ الْجُوعِ، وَالْمُشَبَّهُ بِهِ الْمُقَامِرُ الَّذِي كَثُرَ عِيَالُهُ وَيُطَالِبُونَهُ بِالنَّفَقَةِ وَهُوَ يَصِيحُ بِهِمْ وَيُخَاصِمُهُمْ إِذْ لَا يَجِدُ مَا يُرْضِيهِمْ بِهِ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ.",
   "The kaf is a jarr letter of likening and الْخَلِيعِ is in jarr by the kasra — the phrase hangs on an omitted adjective of an omitted absolute object: «it howls a howling like the outcast's». الخَلِيع: one whom his people have cast off for his wickedness; the masters hold that in this verse it is the gambler. A tashbih mursal mujmal: the thing likened is the wolf howling for sheer hunger; the thing it is likened to is the gambler with a large household that presses him for its keep while he shouts and quarrels with them, having nothing to content them with (al-Zawzanī); the particle is the kaf, and the point of likeness is left unsaid.",
   "Kâf teşbih bildiren cer harfi, الْخَلِيعِ kesre ile mecrûr — câr-mecrûr, mahzûf mef'ûlün mutlakın mahzûf na'tına müteallik: «kovulmuşun uluması gibi bir uluyuşla ulur». الخَلِيع: kötülüğü yüzünden ailesinin kendisinden el çektiği kimse; imamlar bu beyitte onun kumarbaz olduğunu söyler. Teşbih-i mürsel mücmeldir: müşebbeh açlığın şiddetinden uluyan kurt; müşebbehün bih, çoluk çocuğu çok olup onlar nafaka isterken onlara bağırıp çekişen, onları memnun edecek bir şey bulamayan kumarbaz (Zevzenî); edat kâf, vech-i şebeh mahzûftur.", s=[KA, ("الْخَلِيعِ", "khali-outcast", "noun")]),
 W("الْمُعَيَّلِ", "muayyal", "noun", ["naat-sifa", "al-qafiya"], J(NAAT("الْخَلِيعِ", "jarr", en_of="the outcast"), Dn("الْمُعَيَّلُ: الْكَثِيرُ الْعِيَالِ", "المُعَيَّل: one with a large household to feed", "المُعَيَّل: çoluk çocuğu çok olan")), "."),
])
V(None, 50, "I said to it, when it howled: «Our case is that we have little wealth — if you, like me, have never yet come by any.»",
  "Uluyunca ona dedim ki: «Hâlimiz şu: zenginliğimiz azdır — eğer sen de (benim gibi) henüz mal edinmemişsen.»", [
 W("فَقُلْتُ", "qala", "verb", ["hollow-verbs", "al-bariz-al-muttasil"], J(PRE("fa-ist", "قُلْتُ"), lo(MADI_TU)), s=[FA, ("قُلْتُ", "qala", "verb")]),
 PJ("لَهُ", "لَ", "li", "هُ", LAM3, "قُلْتُ", "I said", "e", extra=("؛ وَالضَّمِيرُ لِلذِّئْبِ", "; the pronoun is the wolf", "; zamir kurda döner")),
 T("لَمَّا", "lamma", "part", ["maful-fih"], "ظَرْفُ زَمَانٍ بِمَعْنَى «حِينَ» مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِـ«قُلْتُ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time, «when», built on sukun in the seat of nasb; it hangs on «I said» and is annexed to the clause after it.", "«حِينَ» anlamında zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «قُلْتُ»ya müteallik, sonraki cümleye muzâf."),
 W("عَوَى", "awa", "verb", ["thulathi-mujarrad-babs", "naqis-verbs"], J(("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A past verb built on a fatha estimated on the alif", "Elif üzerinde takdîrî fetha üzere mebnî mâzî"), HID("هُوَ", "it", "hüve", ("الذِّئْبِ", "the wolf", "kurda")), Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «لَمَّا» إِلَيْهَا", "the clause is in the seat of jarr, annexed to لَمَّا", "cümle «لَمَّا»nın muzâfun ileyhi olarak mahallen mecrûr")), ":"),
 T("إِنَّ", "inna", "part", ["inna-wa-akhawatuha"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "The particle of emphasis and nasb.", "Tekit ve nasb harfi."),
 W("شَأْنَنَا", "shan", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], J(("اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ", "The noun of إِنَّ, in nasb by the fatha", "İnne'nin ismi, fetha ile mansûb"), IDF("نَا")), HEMI, [("شَأْنَ", "shan", "noun"), P("نَا")]),
 T("قَلِيلُ", "qalil", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "sifa-mushabbaha"],
   "خَبَرُ إِنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ. قَالَ الزَّوْزَنِيُّ: يُرِيدُ: إِنَّ شَأْنَنَا أَنَّنَا قَلِيلُ الْغِنَى؛ وَمَنْ رَوَى «طَوِيلُ الْغِنَى» فَمَعْنَاهُ: طَوِيلُ طَلَبِ الْغِنَى.",
   "The predicate of إِنَّ, in raf' by the damma, annexed — the clause is what is said, in the seat of nasb. Al-Zawzanī: he means «our case is that we are of little wealth»; those who transmit «طَوِيلُ الْغِنَى» take it as «long in seeking wealth».",
   "İnne'nin haberi, damme ile merfû, muzâf — cümle mekūlü'l-kavl olarak mahallen mansûb. Zevzenî: «hâlimiz, zenginliğimizin az oluşudur» demek ister; «طَوِيلُ الْغِنَى» rivayet edenlere göre mânâ: «zenginlik arayışımız uzundur»."),
 W("الْغِنَى", "ghina", "noun", ["idafa-definiteness", "ism-maqsur-manqus", "idafa-lafziyya"], J(("مُضَافٌ إِلَيْهِ مَجْرُورٌ " + MAQSUR_J, "The second term of the idafa, in jarr by a kasra estimated on the alif", "Muzâfun ileyh, elif üzerinde takdîrî kesre ile mecrûr"), Dn("مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا", "the adjective is annexed to its doer", "sıfat-ı müşebbehenin fâiline izâfeti"))),
 T("إِنْ", "in-shartiyya", "part", ["in-shartiyya"], "حَرْفُ شَرْطٍ جَازِمٌ.", "The conditional particle that puts two verbs in jazm.", "Câzim şart harfi."),
 T("كُنْتَ", "kana", "verb", ["kana-wa-akhawatuha", "in-shartiyya", "hollow-verbs", "hadhf-wa-taqdir"],
   "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهُ — وَجَوَابُ الشَّرْطِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.",
   "A defective past verb built on sukun, in the seat of jazm as the verb of the condition; the ta is its noun, in the seat of raf' — the answer of the condition is left out, shown by what comes before.",
   "Sükûn üzere mebnî nâkıs mâzî, şart fiili olarak mahallen meczûm; tâ onun ismi, mahallen merfû — şartın cevabı mahzûftur, öncesi ona delâlet eder."),
 T("لَمَّا", "lamma", "part", ["lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ بِمَعْنَى «لَمْ»، كَمَا فِي قَوْلِهِ تَعَالَى: «وَلَمَّا يَعْلَمِ اللهُ الَّذِينَ جَاهَدُوا مِنْكُمْ».", "A particle of negation and jazm that turns the verb to the past, in the sense of لَمْ, as in the Qurʾānic «وَلَمَّا يَعْلَمِ اللهُ الَّذِينَ جَاهَدُوا مِنْكُمْ» (9:16) (al-Zawzanī).", "«لَمْ» anlamında nefy, cezm ve kalb harfi; «وَلَمَّا يَعْلَمِ اللهُ الَّذِينَ جَاهَدُوا مِنْكُمْ» (Tevbe 16) âyetindeki gibi (Zevzenî)."),
 T("تَمَوَّلِ", "tamawwala", "verb", ["lam-jazim", "form-v-verbs", "kana-wa-akhawatuha", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمَّا وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + KASR_Q[0] + "، وَأَصْلُهُ «تَتَمَوَّلْ» حُذِفَتْ إِحْدَى تَاءَيْهِ تَخْفِيفًا، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «كُنْتَ»؛ تَمَوَّلَ الرَّجُلُ: صَارَ ذَا مَالٍ.",
   "A present verb in jazm by لَمَّا, its sign the sukun" + KASR_Q[1] + "; it stands for «تَتَمَوَّلْ», one of the two ta's dropped for lightness; its doer is the hidden «you» — the clause is the predicate of «كُنْتَ», in the seat of nasb; تَمَوَّلَ: to come to have wealth.",
   "لَمَّا ile meczûm muzâri, cezm alâmeti sükûn" + KASR_Q[2] + "; aslı «تَتَمَوَّلْ»dür, iki tâ'dan biri hafiflik için düşmüştür; fâili vücûben gizli «ente» — cümle «كُنْتَ»nin haberi olarak mahallen mansûb; تَمَوَّلَ: mal sahibi olmak.", "."),
])
V(None, 51, "Each of us, when he gets a thing, lets it slip from him; and whoever tills as I till and as you till grows lean.",
  "İkimiz de bir şey elde edince onu elden çıkarırız; benim kazancım ve senin kazancın gibi kazanan da zayıf düşer.", [
 T("كِلَانَا", "kila", "noun", ["mubtada-khabar", "al-muthanna", "idafa-definiteness"],
   "مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ نِيَابَةً عَنِ الضَّمَّةِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى، مُضَافٌ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ مِنْ تَمَامِ مَقُولِ الْقَوْلِ فِي الْبَيْتِ قَبْلَهُ، أَوْ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا.",
   "The mubtada, in raf' by the alif in place of the damma — it is treated as a dual; annexed, and نَا is its second term — the nominal clause continues what was said in the verse before, in the seat of nasb; or it opens a new sentence and has no seat.",
   "Mübteda; tesniyeye mülhak olduğu için damme yerine elif ile merfû; muzâf, نَا muzâfun ileyh — isim cümlesi, önceki beyitteki mekūlü'l-kavlin devamı olarak mahallen mansûbdur; ya da müste'nefedir, mahalli yoktur.", s=[("كِلَا", "kila", "noun"), P("نَا")]),
 W("إِذَا", "idha", "part", ["maful-fih", "idha-shartiyya"], J(IDHA, Dn("مُتَعَلِّقٌ بِجَوَابِهِ «أَفَاتَهُ»", "it hangs on its answer, «lets it slip»", "cevabı olan «أَفَاتَهُ»ye müteallik"))),
 T("مَا", "ma-zaida", "part", ["anwa-ma"], MA_Z[0], MA_Z[1], MA_Z[2]),
 W("نَالَ", "nala", "verb", ["hollow-verbs"], J(MADI, HID("هُوَ", "he", "hüve", ("«كِلَانَا»", "«each of us»", "«كِلَانَا»ya")), Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا", "the clause is in the seat of jarr, annexed to إِذَا", "cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr"))),
 W("شَيْئًا", "shay", "noun", ["maful-bihi"], J(MAFR)),
 T("أَفَاتَهُ", "afata", "verb", ["form-iv-verbs", "hollow-verbs", "maful-bihi", "mubtada-khabar"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا، وَ«إِذَا» وَمَا بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُ «كِلَانَا». أَفَاتَهُ: فَوَّتَهُ عَلَى نَفْسِهِ، أَيْ: إِذَا مَلَكَ شَيْئًا أَنْفَقَهُ وَبَذَّرَهُ.",
   "A past verb built on fatha; the هُ is its direct object, in the seat of nasb, and its doer is a hidden «he» — the clause is the answer of إِذَا and has no seat; إِذَا with what follows it is the predicate of «each of us», in the seat of raf'. أَفَاتَهُ: he makes it escape him — when he owns a thing he spends and squanders it (al-Zawzanī).",
   "Fetha üzere mebnî mâzî; «hû» mef'ûlün bih, mahallen mansûb; fâili gizli «hüve» — cümle «إِذَا»nın cevabıdır, mahalli yoktur; «إِذَا» ve sonrası «كِلَانَا»nın haberi olarak mahallen merfû. أَفَاتَهُ: onu elinden kaçırır — bir şeye sahip olunca harcayıp saçar (Zevzenî).", HEMI, [("أَفَاتَ", "afata", "verb"), P("هُ")]),
 T("وَمَنْ", "man", "pron", ["atf-nasaq", "al-majzum-wal-shart-wal-jaza", "mubtada-khabar"],
   "الْوَاوُ عَاطِفَةٌ، وَمَنْ اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَخَبَرُهُ جُمْلَتَا الشَّرْطِ وَالْجَوَابِ؛ وَقِيلَ: جُمْلَةُ الشَّرْطِ وَحْدَهَا، وَقِيلَ: جُمْلَةُ الْجَوَابِ.",
   "The waw conjoins; مَنْ is a conditional noun that puts two verbs in jazm, built on sukun in the seat of raf' as mubtada; its predicate is the two clauses of condition and answer — some say the condition clause alone, and some the answer.",
   "Vâv atıf; مَنْ câzim şart ismi; sükûn üzere mebnî, mübteda olarak mahallen merfû; haberi şart ve cevap cümleleridir; yalnız şart cümlesi, yahut yalnız cevap cümlesi olduğu da söylenmiştir.", s=[WA, ("مَنْ", "man", "pron")]),
 T("يَحْتَرِثْ", "ihtaratha", "verb", ["al-majzum-wal-shart-wal-jaza", "form-viii-verbs", "istiara", "arkan-al-istiara", "istiara-tabaiyya"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «مَنْ» — الِاحْتِرَاثُ وَالْحَرْثُ وَاحِدٌ. قَالَ الزَّوْزَنِيُّ: أَصْلُ الْحَرْثِ إِصْلَاحُ الْأَرْضِ وَإِلْقَاءُ الْبَذْرِ فِيهَا، ثُمَّ يُسْتَعَارُ لِلسَّعْيِ وَالْكَسْبِ، كَقَوْلِهِ تَعَالَى: «مَنْ كَانَ يُرِيدُ حَرْثَ الْآخِرَةِ»، وَهُوَ فِي الْبَيْتِ مُسْتَعَارٌ — فَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: أَصْلِيَّةٌ فِي الْمَصْدَرِ «حَرْثِي»، تَبَعِيَّةٌ فِي الْفِعْلِ «يَحْتَرِثْ».",
   "A present verb in jazm as the verb of the condition, its sign the sukun; its doer is a hidden pronoun returning to «whoever» — الاِحْتِرَاث and الحَرْث are one. Al-Zawzanī: الحَرْث is at root working the soil and casting seed into it; it is then borrowed for striving and earning, as in the Qurʾānic «مَنْ كَانَ يُرِيدُ حَرْثَ الْآخِرَةِ» (42:20); in this verse it is borrowed. So it is an explicit istiʿāra: primary in the masdar «my tilling», and derived (tabaʿiyya) in the verb «tills».",
   "Şart fiili olarak meczûm muzâri, cezm alâmeti sükûn; fâili «مَنْ»e dönen gizli zamir — الاِحْتِرَاث ile الحَرْث birdir. Zevzenî: الحَرْث aslında toprağı işleyip tohum atmaktır; sonra çalışıp kazanmak için istiâre edilir; «مَنْ كَانَ يُرِيدُ حَرْثَ الْآخِرَةِ» (Şûrâ 20) âyetindeki gibi; beyitte de müsteârdır. Demek ki istiâre-i tasrîhiyyedir: «حَرْثِي» masdarında asliyye, «يَحْتَرِثْ» fiilinde tebeiyye."),
 W("حَرْثِي", "harth", "noun", ["maful-bihi", "idafa-definiteness", "ya-al-mutakallim", "masdar", "istiara"], J(("مَفْعُولٌ بِهِ مَنْصُوبٌ ", "The direct object, in nasb by ", "Mef'ûlün bih; "), YA_EST("بِفَتْحَةٍ", "a fatha", "fetha ile mansûb"), Dn("مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ. وَتَفْسِيرُ الزَّوْزَنِيِّ «مَنْ سَعَى سَعْيِي وَسَعْيَكَ» عَلَى أَنَّهُ مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ، وَاسْتَبْعَدَهُ الدُّرَّةُ", "the masdar annexed to its doer. Al-Zawzanī's paraphrase, «whoever strives as I strive and as you strive», takes it as an absolute object that shows the kind; al-Durra calls that reading far-fetched", "masdarın fâiline izâfeti. Zevzenî'nin «benim ve senin çalıştığın gibi çalışan» açıklaması ise onu nev'i bildiren mef'ûlün mutlak sayar; Dürre bunu uzak bulur")), s=[("حَرْثِ", "harth", "noun"), P("ي")]),
 W("وَحَرْثَكَ", "harth", "noun", ["atf-nasaq", "idafa-definiteness", "masdar"], J(PRE("wa", "حَرْثَ"), ATF("حَرْثِي", "my tilling", "nasb"), IDF("كَ")), s=[WA, ("حَرْثَ", "harth", "noun"), P("كَ")]),
 T("يَهْزُلِ", "hazala", "verb", ["al-majzum-wal-shart-wal-jaza", "thulathi-mujarrad-babs", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + KASR_Q[0] + "، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — أَيِ: افْتَقَرَ وَعَاشَ مَهْزُولَ الْعَيْشِ؛ وَيُرْوَى «يُهْزَلِ» بِالْبِنَاءِ لِلْمَجْهُولِ.",
   "A present verb in jazm as the answer of the condition, its sign the sukun" + KASR_Q[1] + "; its doer is a hidden «he» — that is, he grows poor and lives a lean life (al-Zawzanī); it is also transmitted «يُهْزَلِ», in the passive.",
   "Şartın cevabı olarak meczûm muzâri, cezm alâmeti sükûn" + KASR_Q[2] + "; fâili gizli «hüve» — yani fakir düşer, kıt kanaat yaşar (Zevzenî); meçhul sîgasıyla «يُهْزَلِ» de rivayet edilir.", "."),
])
# ==== INSERT 48-51 ABOVE ====
# =====================================================================================================================
# The horse: verses 52–57
# =====================================================================================================================
NAAT_FARAS = ("نَعْتٌ آخَرُ لِلْفَرَسِ الْمَوْصُوفِ فِيمَا قَبْلَهُ مَجْرُورٌ بِالْكَسْرَةِ", "A further adjective of the horse described in the verses before, in jarr by the kasra", "Önceki beyitlerde anlatılan atın bir başka na'tı, kesre ile mecrûr")
V(S4, 52, "Often I ride out early, the birds still in their nests, on a sleek, short-haired horse — a shackle for the wild game — huge of frame;",
  "Çoğu kez, kuşlar daha yuvalarındayken, kısa tüylü, yaban hayvanlarına köstek olan iri yapılı bir atla erkenden çıkarım;", [
 T("وَقَدْ", "qad", "part", ["qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ، وَهُوَ مَعَ الْمُضَارِعِ هُنَا لِلتَّكْثِيرِ — وَبِهِ يَأْخُذُ فِي التَّمَدُّحِ بِالْفُرُوسِيَّةِ.", "The waw opens a new sentence; قَدْ, with the present verb here, means «often» — with it he begins to boast of his horsemanship.", "Vâv istînâfiyye; قَدْ tahkîk harfi, burada muzâri ile teksîr («çoğu kez») bildirir — bununla binicilikle övünmeye başlar.", s=[WA, ("قَدْ", "qad", "part")]),
 T("أَغْتَدِي", "ightada", "verb", ["mudari-marfu", "form-viii-verbs", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — اغْتَدَى وَغَدَا بِمَعْنًى: خَرَجَ غُدْوَةً.", "A present verb in raf' by a damma estimated on the ya (too heavy to voice); its doer is the hidden «I» — اغْتَدَى, like غَدَا: to go out in the early morning.", "Yâ üzerinde ağırlık sebebiyle takdîrî damme ile merfû muzâri; fâili vücûben gizli «ene» — اغْتَدَى, «غَدَا» gibi: sabah erkenden çıkmak."),
 T("وَالطَّيْرُ", "tayr", "noun", ["al-hal-jumla-wa-rabituha", "anwa-al-waw", "mubtada-khabar"], "الْوَاوُ وَاوُ الْحَالِ، وَالطَّيْرُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ طَائِرٍ.", "The waw is the waw of the hal; الطَّيْرُ is the mubtada, in raf' by the damma — the plural of طَائِر.", "Vâv hâliye; الطَّيْرُ mübteda, damme ile merfû — «طَائِر»in cem'i.", s=[WA, ("الطَّيْرُ", "tayr", "noun")]),
 HARF_JARR("فِي", "fi"),
 T("وُكُنَاتِهَا", "wukna", "noun", ["huruf-jarr", "idafa-definiteness", "jam-muannath-salim", "kinaya", "aqsam-al-kinaya"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَإِ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «أَغْتَدِي». جَمْعُ وُكْنَةٍ: مَوْقِعُ الطَّائِرِ؛ وَكَوْنُ الطَّيْرِ فِي وُكُنَاتِهَا كِنَايَةٌ عَنْ صِفَةٍ هِيَ شِدَّةُ التَّبْكِيرِ.",
   "In jarr by the kasra, annexed; هَا is its second term — the phrase hangs on the omitted predicate of the mubtada, and the clause is a hal of the doer of «I ride out», in the seat of nasb. The plural of وُكْنَة, a bird's roost; «the birds still in their roosts» is a kinaya for a quality: how very early he is.",
   "Kesre ile mecrûr, muzâf; هَا muzâfun ileyh — câr-mecrûr mübtedanın mahzûf haberine müteallik; cümle «أَغْتَدِي»nin fâilinden hâl olarak mahallen mansûb. «وُكْنَة»nin (kuşun tünediği yer) cem'i; kuşların yuvalarında olması bir sıfattan — çok erken çıkmaktan — kinâyedir.", HEMI, [("وُكُنَاتِ", "wukna", "noun"), P("هَا")]),
 T("بِمُنْجَرِدٍ", "munjarid", "noun", ["huruf-jarr", "ism-fail", "hadhf-wa-taqdir"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَمُنْجَرِدٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَغْتَدِي»؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: بِفَرَسٍ مُنْجَرِدٍ، وَهُوَ الْمَاضِي فِي السَّيْرِ، وَقِيلَ: الْقَصِيرُ الشَّعْرِ.",
   "The ba is a jarr letter and مُنْجَرِدٍ is in jarr by the kasra — the phrase hangs on «I ride out»; it describes a noun left out: «on a horse that is…» — one that presses on in its going, or, it is said, short-haired.",
   "Bâ cer harfi, مُنْجَرِدٍ kesre ile mecrûr — câr-mecrûr «أَغْتَدِي»ye müteallik; mahzûf bir mevsûfun na'tıdır: «…bir atla» — yürüyüşünde atılgan; «kısa tüylü» de denmiştir.", s=[BI, ("مُنْجَرِدٍ", "munjarid", "noun")]),
 T("قَيْدِ", "qayd", "noun", ["naat-sifa", "idafa-definiteness", "tashbih", "aqsam-al-tashbih"],
   "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَفِيهِ تَشْبِيهٌ بَلِيغٌ حُذِفَتْ أَدَاتُهُ وَوَجْهُهُ: جَعَلَ الْفَرَسَ لِسُرْعَةِ إِدْرَاكِهِ الصَّيْدَ كَالْقَيْدِ لِلْأَوَابِدِ، لِأَنَّهَا لَا يُمْكِنُهَا الْفَوْتُ مِنْهُ كَمَا أَنَّ الْمُقَيَّدَ لَا يَتَمَكَّنُ مِنَ الْهَرَبِ.",
   "A second adjective of the omitted noun, in jarr by the kasra, annexed. A tashbih balīgh, with neither particle nor point of likeness: by the speed with which he overtakes the game, the horse is made as a shackle to the wild beasts — they can no more escape him than a shackled thing can flee (al-Zawzanī).",
   "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr, muzâf. Edatı ve vechi hazfedilmiş teşbih-i belîğ vardır: at, ava çabuk yetişmesi sebebiyle yaban hayvanlarına köstek gibi kılınmıştır; çünkü kösteklenen nasıl kaçamazsa onlar da ondan kurtulamaz (Zevzenî)."),
 T("الْأَوَابِدِ", "abida", "noun", ["idafa-definiteness", "jam-taksir"], MI[0] + " — جَمْعُ آبِدَةٍ: الْوَحْشُ.", MI[1] + " — the plural of آبِدَة: a wild beast.", MI[2] + " — «آبِدَة»nin cem'i: yaban hayvanı."),
 T("هَيْكَلِ", "haykal", "noun", ["naat-sifa", "al-qafiya"], "نَعْتٌ ثَالِثٌ مَجْرُورٌ بِالْكَسْرَةِ" + QAFIYA[0] + " — الْهَيْكَلُ: الْفَرَسُ الْعَظِيمُ الْجِرْمِ.", "A third adjective, in jarr by the kasra" + QAFIYA[1] + " — الهَيْكَل: a horse of huge frame.", "Üçüncü na't, kesre ile mecrûr" + QAFIYA[2] + " — الهَيْكَل: iri gövdeli at.", "،"),
])
V(S4, 53, "ready to charge, ready to flee, coming on and turning back all at once — like a boulder of rock that the torrent has hurled down from on high;",
  "hem saldırmaya hem kaçmaya, hem ileri atılmaya hem geri dönmeye birlikte hazır; selin yüksekten aşağı attığı sert bir kaya parçası gibi;", [
 T("مِكَرٍّ", "mikarr", "noun", ["naat-sifa", "sighat-mubalagha", "tibaq"],
   NAAT_FARAS[0] + " — عَلَى وَزْنِ «مِفْعَلٍ» وَهُوَ يَتَضَمَّنُ الْمُبَالَغَةَ كَأَنَّهُ آلَةٌ لِلْكَرِّ؛ وَبَيْنَهُ وَبَيْنَ «مِفَرٍّ» طِبَاقُ إِيجَابٍ.",
   NAAT_FARAS[1] + " — on the pattern مِفْعَل, which carries intensity, as if he were a tool for charging; with «ready to flee» it makes a tibaq.",
   NAAT_FARAS[2] + " — mübalağa içeren «مِفْعَل» vezninde, sanki saldırının âletidir; «مِفَرٍّ» ile arasında tıbâk-ı îcâb vardır."),
 T("مِفَرٍّ", "mifarr", "noun", ["naat-sifa", "sighat-mubalagha", "tibaq"], NAAT_FARAS[0] + " — «مِفْعَلٌ» مِنْ فَرَّ يَفِرُّ، يُطَابِقُ «مِكَرٍّ».", NAAT_FARAS[1] + " — مِفْعَل from فَرَّ, the contrary of «ready to charge».", NAAT_FARAS[2] + " — «فَرَّ»den «مِفْعَل»; «مِكَرٍّ»in zıddı."),
 T("مُقْبِلٍ", "muqbil", "noun", ["naat-sifa", "ism-fail", "tibaq"], NAAT_FARAS[0] + " — اسْمُ فَاعِلٍ مِنْ «أَقْبَلَ»؛ وَبَيْنَهُ وَبَيْنَ «مُدْبِرٍ» طِبَاقُ إِيجَابٍ.", NAAT_FARAS[1] + " — the ism fa'il of أَقْبَلَ; with «turning back» it makes a tibaq.", NAAT_FARAS[2] + " — «أَقْبَلَ»den ism-i fâil; «مُدْبِرٍ» ile arasında tıbâk-ı îcâb vardır."),
 T("مُدْبِرٍ", "mudbir", "noun", ["naat-sifa", "ism-fail", "tibaq"], NAAT_FARAS[0] + " — اسْمُ فَاعِلٍ مِنْ «أَدْبَرَ»، يُطَابِقُ «مُقْبِلٍ».", NAAT_FARAS[1] + " — the ism fa'il of أَدْبَرَ, the contrary of «coming on».", NAAT_FARAS[2] + " — «أَدْبَرَ»den ism-i fâil; «مُقْبِلٍ»in zıddı."),
 T("مَعًا", "maan", "adv", ["hal"],
   "حَالٌ مِنَ الضَّمَائِرِ الْمُسْتَتِرَةِ فِي الصِّفَاتِ قَبْلَهُ مَنْصُوبٌ بِالْفَتْحَةِ — قَالَ الزَّوْزَنِيُّ: يَعْنِي أَنَّ الْكَرَّ وَالْفَرَّ وَالْإِقْبَالَ وَالْإِدْبَارَ مُجْتَمِعَةٌ فِي قُوَّتِهِ لَا فِي فِعْلِهِ، لِأَنَّ فِيهَا تَضَادًّا.",
   "A hal of the pronouns hidden in the adjectives before it, in nasb by the fatha — al-Zawzanī: charging and fleeing, coming on and turning back are together in his POWER, not in his act, for they are contraries.",
   "Önceki sıfatlardaki gizli zamirlerden hâl, fetha ile mansûb — Zevzenî: saldırma ile kaçma, ileri atılma ile geri dönme onun fiilinde değil KUVVETİNDE bir aradadır; çünkü bunlar birbirinin zıddıdır.", HEMI),
 T("كَجُلْمُودِ", "julmud", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَجُلْمُودِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ آخَرَ لِلْفَرَسِ، وَيَجُوزُ أَنْ يَكُونَ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْفَرَسُ، وَالْمُشَبَّهُ بِهِ جُلْمُودُ صَخْرٍ حَطَّهُ السَّيْلُ، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ سُرْعَةُ الْمَرِّ وَصَلَابَةُ الْخَلْقِ.",
   "The kaf is a jarr letter of likening; جُلْمُودِ is in jarr by the kasra, annexed — the phrase hangs on a further omitted adjective of the horse, or it is the predicate of a mubtada left out. A tashbih mursal mujmal: the thing likened is the horse, the thing he is likened to is a boulder that the torrent hurled down, the particle is the kaf, and the point of likeness is left unsaid — speed in passing and hardness of build (al-Zawzanī).",
   "Kâf teşbih bildiren cer harfi; جُلْمُودِ kesre ile mecrûr, muzâf — câr-mecrûr atın mahzûf bir başka na'tına müteallik; mahzûf bir mübtedanın haberi olması da câizdir. Teşbih-i mürsel mücmeldir: müşebbeh at, müşebbehün bih selin aşağı attığı kaya parçası, edat kâf; vech-i şebeh mahzûftur: geçişteki hız ve yapıdaki sertlik (Zevzenî).", s=[KA, ("جُلْمُودِ", "julmud", "noun")]),
 T("صَخْرٍ", "sakhr-rock", "noun", ["idafa-definiteness"], MI[0] + " — مِنْ إِضَافَةِ بَعْضِ الشَّيْءِ إِلَى كُلِّهِ، أَيْ: جُلْمُودٍ مِنْ صَخْرٍ.", MI[1] + " — the part annexed to its whole: «a boulder of rock».", MI[2] + " — parçanın bütününe izâfeti: «kayadan bir parça»."),
 T("حَطَّهُ", "hatta-down", "verb", ["thulathi-mujarrad-babs", "doubled-verbs", "maful-bihi", "jumla-sifa"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«جُلْمُودِ».", "A past verb built on fatha; the هُ is its direct object, set before the doer — the clause qualifies «a boulder», in the seat of jarr.", "Fetha üzere mebnî mâzî; «hû» öne geçmiş mef'ûlün bih — cümle «جُلْمُودِ»ün na'tı olarak mahallen mecrûr.", s=[("حَطَّ", "hatta-down", "verb"), P("هُ")]),
 T("السَّيْلُ", "sayl", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The doer, in raf' by the damma.", "Fâil, damme ile merfû."),
 HARF_JARR("مِنْ", "min"),
 T("عَلِ", "alu", "noun", ["huruf-jarr", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "al-qafiya"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«حَطَّ»؛ بِمَعْنَى «فَوْقُ»، وَأُعْرِبَ هُنَا وَلَمْ يُبْنَ عَلَى الضَّمِّ لِأَنَّهُ نَكِرَةٌ، أَيْ: مِنْ مَكَانٍ عَالٍ" + QAFIYA[0] + ".",
   "In jarr by the kasra — the phrase hangs on «hurled down». It means «above»; here it is declined, not built on damma, because it is indefinite: «from some high place»" + QAFIYA[1] + ".",
   "Kesre ile mecrûr — câr-mecrûr «حَطَّ»ya müteallik. «Üst» anlamındadır; burada nekre olduğu için damme üzere mebnî değil mu'rebdir: «yüksek bir yerden»" + QAFIYA[2] + ".", "،"),
])
V(S4, 54, "a bay, off the middle of whose back the saddle-felt slips, as the smooth hard rock makes what alights on it slide off;",
  "doru bir at; keçesi sırtının ortasından kayar, tıpkı kaygan sert kayanın üzerine ineni kaydırdığı gibi;", [
 T("كُمَيْتٍ", "kumayt", "noun", ["naat-sifa"], NAAT_FARAS[0] + " — الْكُمَيْتُ مِنَ الْخَيْلِ: مَا لَوْنُهُ بَيْنَ الْأَحْمَرِ وَالْأَسْوَدِ.", NAAT_FARAS[1] + " — a كُمَيْت horse is one whose colour is between red and black.", NAAT_FARAS[2] + " — atlardan كُمَيْت: rengi kırmızı ile siyah arasında olan (doru)."),
 T("يَزِلُّ", "zalla-slip", "verb", ["mudari-marfu", "doubled-verbs", "kinaya", "aqsam-al-kinaya"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْفَرَسِ بَعْدَ وَصْفِهِ، وَيَجُوزُ أَنْ تَكُونَ نَعْتًا لَهُ. وَزَلِيلُ اللِّبْدِ عَنْ مَتْنِهِ كِنَايَةٌ عَنْ صِفَةٍ: انْمِلَاسِ ظَهْرِهِ وَاكْتِنَازِ لَحْمِهِ.",
   "A present verb in raf' by the damma — the clause is a hal of the horse, now that he has been described, or an adjective of him. The felt slipping from his back is a kinaya for a quality: the smoothness of his back and the firmness of his flesh.",
   "Damme ile merfû muzâri — cümle, vasfedildikten sonra attan hâl olarak mahallen mansûb; na't olması da câizdir. Keçenin sırtından kayması bir sıfattan kinâyedir: sırtının pürüzsüzlüğü ve etinin sıkılığı."),
 T("اللِّبْدُ", "libd", "noun", ["fail"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.", "The doer, in raf' by the damma.", "Fâil, damme ile merfû."),
 HARF_JARR("عَنْ", "an"),
 T("حَالِ", "hal-back", "noun", ["huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَزِلُّ»؛ الْحَالُ: مَقْعَدُ الْفَارِسِ مِنْ ظَهْرِ الْفَرَسِ.", "In jarr by the kasra, annexed — the phrase hangs on «slips»; الحَال: the rider's seat on the horse's back.", "Kesre ile mecrûr, muzâf — câr-mecrûr «يَزِلُّ»ye müteallik; الحَال: atın sırtında binicinin oturduğu yer."),
 T("مَتْنِهِ", "matn", "noun", ["idafa-definiteness"], MI[0] + "، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", MI[1] + ", annexed in turn; the هِ is its second term.", MI[2] + ", muzâf; «hî» muzâfun ileyh.", HEMI, [("مَتْنِ", "matn", "noun"), P("هِ")]),
 T("كَمَا", "kama", "part", ["huruf-jarr", "an-masdariyya", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَمَا مَصْدَرِيَّةٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ جَرٍّ بِالْكَافِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: يَزِلُّ زَلِيلًا كَزَلِيلِ الصَّفْوَاءِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ زَلِيلُ اللِّبْدِ عَنْ مَتْنِ الْفَرَسِ، وَالْمُشَبَّهُ بِهِ إِزْلَالُ الصَّخْرَةِ الْمَلْسَاءِ مَا يَنْزِلُ عَلَيْهَا، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الِانْمِلَاسُ.",
   "The kaf is a jarr letter of likening and مَا makes the clause a masdar, which is in the seat of jarr by the kaf — the phrase hangs on an omitted adjective of an omitted absolute object: «it slips with a slipping like that of the smooth rock». A tashbih mursal mujmal: the thing likened is the felt slipping from the horse's back, the thing it is likened to is the smooth rock making what comes down on it slide off, the particle is the kaf, and the point of likeness — smoothness — is left unsaid.",
   "Kâf teşbih bildiren cer harfi, مَا masdariyye; müevvel masdar kâf ile mahallen mecrûr — câr-mecrûr, mahzûf bir mef'ûlün mutlakın mahzûf na'tına müteallik: «düz kayanın kaydırışı gibi bir kayışla kayar». Teşbih-i mürsel mücmeldir: müşebbeh keçenin atın sırtından kayması, müşebbehün bih kaygan kayanın üzerine ineni kaydırması, edat kâf; vech-i şebeh — pürüzsüzlük — mahzûftur.", s=[KA, ("مَا", "ma-masdariyya", "part")]),
 T("زَلَّتِ", "zalla-slip", "verb", ["thulathi-mujarrad-babs", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A past verb built on fatha; the ta marks the feminine and takes a kasra because two still letters meet.", "Fetha üzere mebnî mâzî; tâ te'nîs için, iki sâkin karşılaştığından kesre ile harekelenmiştir."),
 T("الصَّفْوَاءُ", "safwa", "noun", ["fail", "ism-mamdud"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ — الصَّفْوَاءُ: الْحَجَرُ الصُّلْبُ الْأَمْلَسُ.", "The doer, in raf' by the damma — الصَّفْوَاء: hard smooth rock.", "Fâil, damme ile merfû — الصَّفْوَاء: sert, kaygan kaya."),
 T("بِالْمُتَنَزِّلِ", "mutanazzil", "noun", ["huruf-jarr", "ism-fail", "hadhf-wa-taqdir", "al-qafiya"],
   "الْبَاءُ حَرْفُ جَرٍّ لِلتَّعْدِيَةِ، وَالْمُتَنَزِّلِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«زَلَّتْ»؛ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ تَقْدِيرُهُ: بِالْمَطَرِ الْمُتَنَزِّلِ، أَوْ بِالْإِنْسَانِ الْمُتَنَزِّلِ.",
   "The ba is a jarr letter that makes the verb transitive; الْمُتَنَزِّلِ is in jarr by the kasra — the phrase hangs on «slips»; it describes a noun left out: «the rain that comes down», or «the man who comes down».",
   "Bâ ta'diye için cer harfi; الْمُتَنَزِّلِ kesre ile mecrûr — câr-mecrûr «زَلَّتْ»e müteallik; mahzûf bir mevsûfun sıfatıdır: «inen yağmuru» ya da «inen insanı».", "،", [BI, ("الْمُتَنَزِّلِ", "mutanazzil", "noun")]),
])
V(S4, 55, "lean as he is, he seethes; the broken sound of his breath, when his heat boils up in him, is the bubbling of a cauldron;",
  "zayıflığına rağmen coşkundur; içinde harareti kaynadığında göğsündeki kesik kişnemesi bir kazanın fokurdamasıdır sanki;", [
 HARF_JARR("عَلَى", "ala", " بِمَعْنَى «مَعَ»", " — here «for all», «with»", " — burada «-e rağmen, ile birlikte» anlamında"),
 T("الذَّبْلِ", "dhabl", "noun", ["huruf-jarr", "masdar"], "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَيَّاشٍ»؛ الذَّبْلُ وَالذُّبُولُ وَاحِدٌ: ضُمْرُ الْبَطْنِ.", "In jarr by the kasra — the phrase hangs on «seething»; الذَّبْل, like الذُّبُول: leanness of the belly.", "Kesre ile mecrûr — câr-mecrûr «جَيَّاشٍ»e müteallik; الذَّبْل, «الذُّبُول» ile aynıdır: karnın çekikliği."),
 T("جَيَّاشٍ", "jayyash", "noun", ["naat-sifa", "sighat-mubalagha"], NAAT_FARAS[0] + " — صِيغَةُ مُبَالَغَةٍ عَلَى «فَعَّالٍ» مِنْ جَاشَتِ الْقِدْرُ إِذَا غَلَتْ.", NAAT_FARAS[1] + " — an intensive on فَعَّال, from جَاشَت of a pot: it boiled.", NAAT_FARAS[2] + " — «فَعَّال» vezninde mübalağa sîgası; tencerenin kaynaması anlamındaki «جَاشَتْ»ten."),
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ — وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ اهْتِزَامُهُ أَيْ تَكَسُّرُ صَهِيلِهِ فِي صَدْرِهِ، وَالْمُشَبَّهُ بِهِ غَلْيُ الْمِرْجَلِ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الصَّوْتُ الْمُتَتَابِعُ.",
   "The verb-like particle of likening. A tashbih mursal mujmal: the thing likened is his «ihtizām» — his neighing breaking in his chest — the thing it is likened to is the boiling of a cauldron, the particle is كَأَنَّ, and the point of likeness — the sound coming wave on wave — is left unsaid.",
   "Teşbih bildiren fiile benzeyen harf. Teşbih-i mürsel mücmeldir: müşebbeh onun «ihtizâm»ı, yani kişnemesinin göğsünde kırılması; müşebbehün bih kazanın kaynaması, edat كَأَنَّ; vech-i şebeh — ardı ardına gelen ses — mahzûftur."),
 T("اهْتِزَامَهُ", "ihtizam", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar"], "اسْمُ كَأَنَّ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The noun of كَأَنَّ, in nasb by the fatha, annexed; the هُ is its second term.", "كَأَنَّ'nin ismi, fetha ile mansûb, muzâf; «hû» muzâfun ileyh.", HEMI, [("اهْتِزَامَ", "ihtizam", "noun"), P("هُ")]),
 T("إِذَا", "idha", "part", ["maful-fih", "idha-shartiyya"], "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِمَا فِي «كَأَنَّ» مِنْ مَعْنَى التَّشْبِيهِ، وَيَجُوزُ تَعْلِيقُهُ بِـ«غَلْيُ»؛ مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb for time to come, built on sukun in the seat of nasb; it hangs on the sense of likening in كَأَنَّ, or on «boiling», and is annexed to the clause after it.", "Gelecek zaman zarfı, sükûn üzere mebnî, mahallen mansûb; «كَأَنَّ»deki teşbih mânâsına — ya da «غَلْيُ»e — müteallik; sonraki cümleye muzâf."),
 T("جَاشَ", "jasha", "verb", ["thulathi-mujarrad-babs", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.", "A past verb built on fatha — the clause is in the seat of jarr, annexed to إِذَا.", "Fetha üzere mebnî mâzî — cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr."),
 T("فِيهِ", "fi", "prep", ["huruf-jarr"], "فِي حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَاشَ».", "فِي is a jarr letter and the هِ is in the seat of jarr — the phrase hangs on «boils up».", "فِي cer harfi, «hî» mahallen mecrûr — câr-mecrûr «جَاشَ»ye müteallik.", s=[("فِي", "fi", "prep"), P("هِ")]),
 T("حَمْيُهُ", "hamy", "noun", ["fail", "idafa-definiteness", "masdar"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْحَمْيُ: الْحَرَارَةُ.", "The doer, in raf' by the damma, annexed; the هُ is its second term — الحَمْي: heat.", "Fâil, damme ile merfû, muzâf; «hû» muzâfun ileyh — الحَمْي: hararet.", s=[("حَمْيُ", "hamy", "noun"), P("هُ")]),
 T("غَلْيُ", "ghaly", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "masdar", "imal-al-masdar"], "خَبَرُ كَأَنَّ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — مَصْدَرُ غَلَتِ الْقِدْرُ.", "The predicate of كَأَنَّ, in raf' by the damma, annexed — the masdar of غَلَت (a pot boiling).", "كَأَنَّ'nin haberi, damme ile merfû, muzâf — tencerenin kaynaması anlamındaki «غَلَتْ»in masdarı."),
 T("مِرْجَلِ", "mirjal", "noun", ["idafa-definiteness", "imal-al-masdar", "al-qafiya"], MI[0] + QAFIYA[0] + " — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ؛ الْمِرْجَلُ: الْقِدْرُ.", MI[1] + QAFIYA[1] + " — the masdar is annexed to its doer; المِرْجَل: a cooking-pot.", MI[2] + QAFIYA[2] + " — masdarın fâiline izâfeti; المِرْجَل: kazan.", "،"),
])
V(S4, 56, "one that pours out run upon run, when the swimming steeds, flagging, raise the dust on the hard, hoof-beaten ground;",
  "kulaç atar gibi koşan atlar yorgun düşüp çiğnenmiş sert düzlükte toz kaldırdığında bile koşusunu döktükçe döken;", [
 T("مِسَحٍّ", "misahh", "noun", ["naat-sifa", "sighat-mubalagha", "istiara", "istiara-tabaiyya"],
   NAAT_FARAS[0] + " — «مِفْعَلٌ» مِنْ سَحَّ الْمَاءَ إِذَا صَبَّهُ، وَهُوَ يَقْتَضِي الْمُبَالَغَةَ: يَصُبُّ الْجَرْيَ صَبًّا بَعْدَ صَبٍّ؛ وَيَجُوزُ رَفْعُهُ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ، وَنَصْبُهُ عَلَى الْمَدْحِ. وَفِيهِ اسْتِعَارَةٌ تَبَعِيَّةٌ: شُبِّهَ تَتَابُعُ جَرْيِهِ بِسَحِّ الْمَاءِ ثُمَّ اشْتُقَّ مِنْهُ الْوَصْفُ.",
   NAAT_FARAS[1] + " — مِفْعَل from سَحَّ «to pour (water)», a pattern that carries intensity: he pours out his run, gush after gush. It may also be read in raf' (the predicate of a mubtada left out) or in nasb (praise). An istiʿāra carried in the derived word (tabaʿiyya): his run, coming burst on burst, is likened to water poured out, and the adjective is drawn from that.",
   NAAT_FARAS[2] + " — «suyu dökmek» anlamındaki سَحَّ'dan «مِفْعَل»; bu vezin mübalağa bildirir: koşusunu döktükçe döker. Mahzûf mübtedanın haberi olarak ref'i, medh üzere nasbı da câizdir. İstiâre-i tebeiyye vardır: koşusunun ardı ardına gelişi suyun dökülmesine benzetilmiş, sıfat bundan türetilmiştir."),
 T("إِذَا", "idha", "part", ["maful-fih", "idha-shartiyya", "hadhf-wa-taqdir"],
   "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُضَافٌ إِلَى جُمْلَةِ شَرْطِهِ — وَجَوَابُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ «مِسَحٍّ»، أَيْ: إِذَا أَثَرْنَ الْغُبَارَ سَحَّ.",
   "An adverb for time to come that carries the sense of a condition, built on sukun in the seat of nasb and annexed to its condition clause — its answer is left out, and «one that pours» points to it: «when they raise the dust, he pours».",
   "Şart mânâsı taşıyan gelecek zaman zarfı; sükûn üzere mebnî, mahallen mansûb, şart cümlesine muzâf — cevabı mahzûftur, «مِسَحٍّ» ona delâlet eder: «toz kaldırdıklarında o döker»."),
 T("مَا", "ma-zaida", "part", ["anwa-ma"], "زَائِدَةٌ لِلتَّوْكِيدِ لَا عَمَلَ لَهَا.", "The added مَا: emphasis only, it governs nothing.", "Zâid mâ; yalnız tekit içindir, amel etmez."),
 T("السَّابِحَاتُ", "sabiha", "noun", ["fail", "hadhf-wa-taqdir", "jam-muannath-salim", "ism-fail", "istiara", "arkan-al-istiara"],
   "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «أَثَرْنَ» مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا. وَهُوَ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيِ: الْخَيْلُ السَّابِحَاتُ، وَالسَّابِحُ مِنَ الْخَيْلِ: الَّذِي يَمُدُّ يَدَيْهِ فِي عَدْوِهِ. وَفِيهِ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ: قَالَ الزَّوْزَنِيُّ: شُبِّهَ بِالسَّابِحِ فِي الْمَاءِ.",
   "The doer of an omitted verb that «they raise» explains, in raf' by the damma — the clause is in the seat of jarr, annexed to إِذَا. It describes a noun left out, «the horses that swim»: a «swimming» horse is one that stretches out its forelegs as it runs. An explicit istiʿāra — al-Zawzanī: it is likened to one swimming in water.",
   "«أَثَرْنَ»nin tefsir ettiği mahzûf bir fiilin fâili, damme ile merfû — cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr. Mahzûf mevsûfun na'tıdır: «yüzen atlar»; atlardan «sâbih», koşarken ön ayaklarını ileri uzatandır. İstiâre-i tasrîhiyye vardır — Zevzenî: suda yüzene benzetilmiştir."),
 HARF_JARR("عَلَى", "ala", " بِمَعْنَى «مَعَ»", " — here «with», «in spite of»", " — burada «ile birlikte, -e rağmen» anlamında"),
 T("الْوَنَى", "wanan", "noun", ["huruf-jarr", "ism-maqsur-manqus", "masdar"],
   "مَجْرُورٌ " + MAQSUR_J + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«السَّابِحَاتُ» لِأَنَّهُ اسْمُ فَاعِلٍ، أَيْ: فِي حَالِ فُتُورِهَا؛ وَعَلَّقَهُمَا التِّبْرِيزِيُّ بِـ«أَثَرْنَ». الْوَنَى: الْفُتُورُ.",
   "In jarr by a kasra estimated on the alif — the phrase hangs on «the swimmers», an ism fa'il: «as they flag»; al-Tibrīzī hangs it on «they raise». الوَنَى: slackening, weariness.",
   "Elif üzerinde takdîrî kesre ile mecrûr — câr-mecrûr, ism-i fâil olan «السَّابِحَاتُ»a müteallik: «yorgun düştükleri hâlde»; Tebrîzî «أَثَرْنَ»ye bağlar. الوَنَى: gevşeme, yorgunluk.", HEMI),
 T("أَثَرْنَ", "athara", "verb", ["form-iv-verbs", "hollow-verbs", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ تَفْسِيرِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ؛ أَثَارَ الْغُبَارَ: هَيَّجَهُ.",
   "A past verb built on sukun because the women's nun is attached; the nun is the doer, in the seat of raf' — the clause explains the omitted verb and has no seat; أَثَارَ of dust: to stir it up.",
   "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî mâzî; nûn fâil, mahallen merfû — cümle tefsîriyyedir, i'râbdan mahalli yoktur; tozu «أَثَارَ»: kaldırmak."),
 T("الْغُبَارَ", "ghubar", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The direct object, in nasb by the fatha.", "Mef'ûlün bih, fetha ile mansûb."),
 T("بِالْكَدِيدِ", "kadid", "noun", ["huruf-jarr"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَالْكَدِيدِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَثَرْنَ»، وَيَجُوزُ تَعْلِيقُهُمَا بِمَحْذُوفٍ حَالٍ مِنَ «الْغُبَارَ»؛ الْكَدِيدُ: الْأَرْضُ الصُّلْبَةُ الْمُطْمَئِنَّةُ.",
   "The ba is a jarr letter meaning «in»; الْكَدِيدِ is in jarr by the kasra — the phrase hangs on «they raise», or on an omitted hal of «the dust»; الكَدِيد: hard, low-lying ground.",
   "Bâ «-de» anlamında cer harfi; الْكَدِيدِ kesre ile mecrûr — câr-mecrûr «أَثَرْنَ»ye müteallik; «الْغُبَارَ»dan mahzûf hâle bağlanması da câizdir; الكَدِيد: sert, çukurca düz arazi.", s=[BI, ("الْكَدِيدِ", "kadid", "noun")]),
 T("الْمُرَكَّلِ", "murakkal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
   "نَعْتٌ لِـ«الْكَدِيدِ» مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ مِنْ «رَكَّلَ»: الَّذِي يُرْكَلُ بِالْحَوَافِرِ مَرَّةً بَعْدَ أُخْرَى، وَنَائِبُ فَاعِلِهِ ضَمِيرٌ مُسْتَتِرٌ فِيهِ.",
   "An adjective of «the hard ground», in jarr by the kasra — the ism maf'ul of رَكَّلَ: kicked by hooves again and again; its deputy doer is the pronoun hidden in it.",
   "«الْكَدِيدِ»in na'tı, kesre ile mecrûr — «رَكَّلَ»den ism-i mef'ûl: toynaklarla tekrar tekrar tepilmiş; nâib-i fâili içindeki gizli zamirdir.", "،"),
])
V(S4, 57, "he makes the light lad slip from his back, and flings away the clothes of the rough, heavy rider.",
  "Hafif delikanlıyı sırtından kaydırır; sert ve ağır binicinin de elbiselerini savurup atar.", [
 T("يُزِلُّ", "azalla", "verb", ["mudari-marfu", "form-iv-verbs", "doubled-verbs", "jumla-sifa", "kinaya", "aqsam-al-kinaya"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، مِنْ «أَزَلَّ»، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَرَسِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ آخَرُ لَهُ، وَيَجُوزُ أَنْ تَكُونَ حَالًا مِنْهُ؛ وَيُرْوَى «يَزِلُّ الْغُلَامُ» بِفَتْحِ الْيَاءِ وَرَفْعِ الْغُلَامِ. وَإِزْلَالُهُ الْغُلَامَ وَإِلْوَاؤُهُ بِأَثْوَابِ الْعَنِيفِ كِنَايَةٌ عَنْ صِفَةٍ: شِدَّةِ عَدْوِهِ وَفَرْطِ مَرَحِهِ فِي جَرْيِهِ.",
   "A present verb in raf' by the damma, from أَزَلَّ (Form IV); its doer is a hidden pronoun returning to the horse — the clause is a further adjective of him, in the seat of jarr, or a hal. It is also transmitted يَزِلُّ الْغُلَامُ («the lad slips»), with the lad in raf'. His making the lad slip and flinging off the rough man's clothes is a kinaya for a quality: the force of his gallop and his exuberance in running (al-Zawzanī).",
   "Damme ile merfû muzâri, «أَزَلَّ»den (if'âl); fâili ata dönen gizli zamir — cümle onun bir başka na'tı olarak mahallen mecrûr; hâl olması da câizdir. «يَزِلُّ الْغُلَامُ» (delikanlı kayar) şeklinde, «الغلام»ın ref'iyle de rivayet edilir. Delikanlıyı kaydırması ve sert binicinin elbiselerini savurması bir sıfattan kinâyedir: koşusunun şiddeti ve koşarkenki aşırı coşkusu (Zevzenî)."),
 T("الْغُلَامَ", "ghulam", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The direct object, in nasb by the fatha.", "Mef'ûlün bih, fetha ile mansûb."),
 T("الْخِفَّ", "khiff", "noun", ["naat-sifa", "tibaq"],
   "نَعْتٌ لِـ«الْغُلَامَ» مَنْصُوبٌ بِالْفَتْحَةِ — الْخِفُّ: الْخَفِيفُ؛ وَبَيْنَهُ وَبَيْنَ «الْمُثَقَّلِ» طِبَاقُ إِيجَابٍ.",
   "An adjective of «the lad», in nasb by the fatha — الخِفّ: light; with «the heavy» it makes a tibaq.",
   "«الْغُلَامَ»ın na'tı, fetha ile mansûb — الخِفّ: hafif; «الْمُثَقَّلِ» ile arasında tıbâk-ı îcâb vardır."),
 HARF_JARR("عَنْ", "an"),
 T("صَهَوَاتِهِ", "sahwa", "noun", ["huruf-jarr", "idafa-definiteness", "jam-muannath-salim"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُزِلُّ». جَمْعُ صَهْوَةٍ: مَقْعَدُ الْفَارِسِ مِنْ ظَهْرِ الْفَرَسِ؛ وَجَمَعَهَا وَلَيْسَ لَهُ إِلَّا صَهْوَةٌ وَاحِدَةٌ لِأَنَّهُ لَا لَبْسَ فِيهِ، فَإِضَافَتُهَا إِلَى ضَمِيرِ الْوَاحِدِ تُزِيلُ اللَّبْسَ.",
   "In jarr by the kasra, annexed; the هِ is its second term — the phrase hangs on «makes slip». The plural of صَهْوَة, the rider's seat on a horse's back; he uses the plural though a horse has but one, because no confusion can arise: annexing it to a singular pronoun removes it (al-Zawzanī).",
   "Kesre ile mecrûr, muzâf; «hî» muzâfun ileyh — câr-mecrûr «يُزِلُّ»ye müteallik. «صَهْوَة»nin cem'i: atın sırtında binicinin oturduğu yer; atın tek sahvesi olduğu hâlde cemi getirmiştir, çünkü karışıklık olmaz: müfred zamire izâfet karışıklığı giderir (Zevzenî).", HEMI, [("صَهَوَاتِ", "sahwa", "noun"), P("هِ")]),
 T("وَيُلْوِي", "alwa", "verb", ["atf-nasaq", "mudari-marfu", "form-iv-verbs", "naqis-verbs"],
   "الْوَاوُ عَاطِفَةٌ، وَيُلْوِي فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَرَسِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «يُزِلُّ»؛ أَلْوَى بِالشَّيْءِ: رَمَى بِهِ وَذَهَبَ بِهِ.",
   "The waw conjoins; يُلْوِي is a present verb in raf' by a damma estimated on the ya (too heavy to voice); its doer is a hidden pronoun returning to the horse — the clause is conjoined to «makes slip»; أَلْوَى بِالشَّيْءِ: to fling a thing away, to carry it off.",
   "Vâv atıf; يُلْوِي yâ üzerinde ağırlık sebebiyle takdîrî damme ile merfû muzâri; fâili ata dönen gizli zamir — cümle «يُزِلُّ» cümlesine ma'tûf; أَلْوَى بِالشَّيْءِ: bir şeyi fırlatıp atmak, alıp götürmek.", s=[WA, ("يُلْوِي", "alwa", "verb")]),
 T("بِأَثْوَابِ", "thawb", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَأَثْوَابِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُلْوِي»؛ جَمْعُ ثَوْبٍ.",
   "The ba is a jarr letter; أَثْوَابِ is in jarr by the kasra, annexed — the phrase hangs on «flings away»; the plural of ثَوْب.",
   "Bâ cer harfi; أَثْوَابِ kesre ile mecrûr, muzâf — câr-mecrûr «يُلْوِي»ye müteallik; «ثَوْب»un cem'i.", s=[BI, ("أَثْوَابِ", "thawb", "noun")]),
 T("الْعَنِيفِ", "anif", "noun", ["idafa-definiteness", "sifa-mushabbaha", "hadhf-wa-taqdir"],
   MI[0] + " — صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيِ: الرَّجُلِ الْعَنِيفِ، وَهُوَ ضِدُّ الرَّفِيقِ.",
   MI[1] + " — it describes a noun left out, «the rough man»: the opposite of the gentle one.",
   MI[2] + " — mahzûf mevsûfun sıfatı: «sert adam»; yumuşak davrananın zıddı."),
 T("الْمُثَقَّلِ", "muthaqqal", "noun", ["naat-sifa", "ism-maful", "tibaq", "al-qafiya"],
   "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ مِنْ «ثَقَّلَ»: الثَّقِيلُ؛ يُطَابِقُ «الْخِفَّ».",
   "A second adjective of the omitted noun, in jarr by the kasra — the ism maf'ul of ثَقَّلَ: heavy; the contrary of «the light».",
   "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr — «ثَقَّلَ»den ism-i mef'ûl: ağır; «الْخِفَّ»in zıddı.", "."),
])


# =====================================================================================================================
# The horse, continued — and the herd appears: verses 58–63
# =====================================================================================================================
ISM_KAANNA = ("اسْمُ كَأَنَّ مَنْصُوبٌ بِالْفَتْحَةِ", "The noun of كَأَنَّ, in nasb by the fatha", "كَأَنَّ'nin ismi, fetha ile mansûb")
KAANNA_T = ("حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ يُفِيدُ التَّشْبِيهَ", "A verb-like particle of likening", "Teşbih bildiren fiile benzeyen harf")
RAF3 = ("وَيَجُوزُ رَفْعُهُ خَبَرًا لِمُبْتَدَإٍ مَحْذُوفٍ، وَنَصْبُهُ عَلَى الْمَدْحِ", "it may also be read in raf', as the predicate of a mubtada left out, or in nasb, as praise", "mahzûf mübtedanın haberi olarak ref'i, medih üzere nasbı da câizdir")
V(None, 58, "A steady runner, like a boy's whirligig that his two hands, one following the other, have spun tight on a string knotted together.",
  "Koşusunu hiç kesmez; bir çocuğun, ekli bir iple iki elini ardı ardına işleterek sımsıkı çevirdiği fırıldağı gibidir.", [
 T("دَرِيرٍ", "darir", "noun", ["naat-sifa", "sifa-mushabbaha"],
   NAAT_FARAS[0] + "، " + RAF3[0] + " — مِنْ دَرَّ يَدِرُّ؛ فَعِيلٌ بِمَعْنَى الدَّارِّ أَوْ بِمَعْنَى الْمُدِرِّ، أَيْ: يَدِرُّ الْعَدْوَ وَالْجَرْيَ: يُدِيمُهُمَا وَيُوَاصِلُهُمَا.",
   NAAT_FARAS[1] + "; " + RAF3[1] + " — from دَرَّ «to flow»: a فَعِيل in the sense of الدَّارّ or of المُدِرّ — he makes his run flow, keeps it up without a break (al-Zawzanī).",
   NAAT_FARAS[2] + "; " + RAF3[2] + " — «akmak» anlamındaki دَرَّ'den; «الدَّارّ» ya da «المُدِرّ» mânâsında فَعِيل: koşusunu akıtır, kesintisiz sürdürür (Zevzenî)."),
 T("كَخُذْرُوفِ", "khudhruf", "noun", ["huruf-jarr", "idafa-definiteness", "hal", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَخُذْرُوفِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي «دَرِيرٍ». الْخُذْرُوفُ: حَصَاةٌ مَثْقُوبَةٌ يَجْعَلُ الصِّبْيَانُ فِيهَا خَيْطًا فَيُدِيرُهَا الصَّبِيُّ عَلَى رَأْسِهِ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ ذُكِرَ فِيهِ وَصْفُ الْمُشَبَّهِ بِهِ: الْمُشَبَّهُ الْفَرَسُ فِي سُرْعَةِ مَرِّهِ وَشِدَّةِ عَدْوِهِ، وَالْمُشَبَّهُ بِهِ الْخُذْرُوفُ فِي دَوَرَانِهِ إِذَا بُولِغَ فِي فَتْلِ خَيْطِهِ مُوَصَّلًا، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ السُّرْعَةُ.",
   "The kaf is a jarr letter of likening; خُذْرُوفِ is in jarr by the kasra, annexed — the phrase hangs on an omitted hal of the pronoun hidden in «steady runner». الخُذْرُوف: a pierced pebble through which boys pass a string, and which the boy whirls over his head. A tashbih mursal mujmal in which the thing likened to is described: the thing likened is the horse in his swift passing and hard running; the thing he is likened to is the whirligig spinning when its knotted string has been twisted to the utmost (al-Zawzanī); the particle is the kaf, and the point of likeness — speed — is left unsaid.",
   "Kâf teşbih bildiren cer harfi; خُذْرُوفِ kesre ile mecrûr, muzâf — câr-mecrûr «دَرِيرٍ»deki gizli zamirden mahzûf hâle müteallik. الخُذْرُوف: çocukların içinden ip geçirip başının üstünde çevirdiği delikli çakıl taşı. Müşebbehün bihin vasfı zikredilmiş teşbih-i mürsel mücmeldir: müşebbeh, geçişinin hızı ve koşusunun şiddetiyle at; müşebbehün bih, ekli ipi iyice büküldüğünde dönen fırıldak (Zevzenî); edat kâf; vech-i şebeh — sürat — mahzûftur.", s=[KA, ("خُذْرُوفِ", "khudhruf", "noun")]),
 W("الْوَلِيدِ", "walid", "noun", ["idafa-definiteness"], J(MI, Dn("الْوَلِيدُ: الصَّبِيُّ، وَالْجَمْعُ الْوِلْدَانُ", "الوَلِيد: a boy; plural الوِلْدَان", "الوَلِيد: erkek çocuk; cem'i الوِلْدَان"))),
 T("أَمَرَّهُ", "amarra", "verb", ["form-iv-verbs", "doubled-verbs", "maful-bihi", "al-hal-jumla-wa-rabituha"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «خُذْرُوفِ الْوَلِيدِ»، أَوْ فِي مَحَلِّ جَرٍّ نَعْتٌ لَهُ؛ الْإِمْرَارُ: إِحْكَامُ الْفَتْلِ.",
   "A past verb built on fatha; the هُ is its direct object, set before the doer, in the seat of nasb — the clause is a hal of «the boy's whirligig», in the seat of nasb, or an adjective of it, in the seat of jarr; الإِمْرَار: twisting tight.",
   "Fetha üzere mebnî mâzî; «hû» öne geçmiş mef'ûlün bih, mahallen mansûb — cümle «خُذْرُوفِ الْوَلِيدِ»den hâl olarak mahallen mansûb ya da onun na'tı olarak mahallen mecrûr; الإِمْرَار: sımsıkı bükmek.", HEMI, [("أَمَرَّ", "amarra", "verb"), P("هُ")]),
 W("تَتَابُعُ", "tatabu", "noun", ["fail", "idafa-definiteness", "masdar"], J(("فَاعِلُ «أَمَرَّهُ» مَرْفُوعٌ بِالضَّمَّةِ", "The doer of «spun it tight», in raf' by the damma", "«أَمَرَّهُ»nün fâili, damme ile merfû"), MUD)),
 T("كَفَّيْهِ", "kaff-hand", "noun", ["idafa-definiteness", "al-muthanna", "imal-al-masdar"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ.",
   "The second term of the idafa, in jarr by the ya, being a dual whose nun is dropped in annexation; the هِ is its own second term — the masdar is annexed to its doer.",
   "Muzâfun ileyh; tesniye olduğu için yâ ile mecrûr, izâfet sebebiyle nûnu düşmüştür; «hî» muzâfun ileyh — masdarın fâiline izâfeti.", s=[("كَفَّيْ", "kaff-hand", "noun"), P("هِ")]),
 T("بِخَيْطٍ", "khayt", "noun", ["huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَخَيْطٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«تَتَابُعُ».", "The ba is a jarr letter and خَيْطٍ is in jarr by the kasra — the phrase hangs on «following».", "Bâ cer harfi, خَيْطٍ kesre ile mecrûr — câr-mecrûr «تَتَابُعُ»a müteallik.", s=[BI, ("خَيْطٍ", "khayt", "noun")]),
 W("مُوَصَّلِ", "muwassal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(NAAT("خَيْطٍ", "jarr", en_of="a string"), QAFIYA, Dn("أَيْ: قَدِ انْقَطَعَ ثُمَّ وُصِلَ، وَذٰلِكَ أَشَدُّ لِدَوَرَانِهِ لِانْمِلَاسِهِ وَمُرُونِهِ", "that is, one that broke and was knotted together again — and so spins the harder, being worn smooth and supple", "yani kopup yeniden eklenmiş ip; aşınıp yumuşadığı için fırıldağı daha hızlı döndürür")), "."),
])
V(None, 59, "He has the flanks of a gazelle and the shanks of an ostrich, the lope of a wolf and the canter of a fox-cub.",
  "Onda ceylanın böğürleri, devekuşunun bacakları, kurdun koşusu ve tilki yavrusunun sekişi vardır.", [
 T("لَهُ", "li", "prep", ["huruf-jarr", "mubtada-khabar", "taqdim-al-musnad"], "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى الْفَرَسِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ؛ وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ جَرٍّ نَعْتٌ آخَرُ لِلْفَرَسِ، وَيَجُوزُ أَنْ تَكُونَ حَالًا مِنْهُ.", "The lam is a jarr letter and the هُ is in the seat of jarr, returning to the horse — the phrase hangs on an omitted predicate, set first; the nominal clause is a further adjective of the horse, in the seat of jarr, or a hal of him.", "Lâm cer harfi, «hû» mahallen mecrûr, ata döner — câr-mecrûr öne geçmiş mahzûf habere müteallik; isim cümlesi atın bir başka na'tı olarak mahallen mecrûrdur, ondan hâl olması da câizdir.", s=[("لَ", "li", "prep"), P("هُ")]),
 T("أَيْطَلَا", "aytal", "noun", ["mubtada-khabar", "al-muthanna", "idafa-definiteness", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْأَلِفُ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ — الْأَيْطَلُ: الْخَاصِرَةُ. قَالَ الزَّوْزَنِيُّ: شَبَّهَ خَاصِرَتَيْ هٰذَا الْفَرَسِ بِخَاصِرَتَيِ الظَّبْيِ فِي الضُّمْرِ، وَسَاقَيْهِ بِسَاقَيِ النَّعَامَةِ فِي الِانْتِصَابِ وَالطُّولِ، وَعَدْوَهُ بِإِرْخَاءِ الذِّئْبِ، وَتَقْرِيبَهُ بِتَقْرِيبِ وَلَدِ الثَّعْلَبِ، فَجَمَعَ أَرْبَعَةَ تَشْبِيهَاتٍ فِي هٰذَا الْبَيْتِ — وَكُلُّهَا تَشْبِيهٌ بَلِيغٌ حُذِفَتْ مِنْهُ الْأَدَاةُ وَوَجْهُ الشَّبَهِ.",
   "The mubtada, placed last, in raf' by the alif, being a dual whose nun is dropped in annexation — الأَيْطَل: the flank. Al-Zawzanī: he likens this horse's flanks to a gazelle's in leanness, his shanks to an ostrich's in straightness and length, his running to the lope of a wolf, and his canter to that of a fox-cub — four likenesses gathered in one verse. Each is a tashbih balīgh: the particle and the point of likeness are both dropped.",
   "Sona bırakılmış mübteda; tesniye olduğu için elif ile merfû, izâfet sebebiyle nûnu düşmüştür — الأَيْطَل: böğür. Zevzenî: bu atın böğürlerini incelikte ceylanın böğürlerine, bacaklarını diklik ve uzunlukta devekuşunun bacaklarına, koşusunu kurdun koşusuna, sekişini tilki yavrusunun sekişine benzetmiş, bir beyitte dört teşbihi toplamıştır. Her biri teşbih-i belîğdir: edat ve vech-i şebeh hazfedilmiştir."),
 W("ظَبْيٍ", "zaby", "noun", ["idafa-definiteness"], J(MI)),
 W("وَسَاقَا", "saq", "noun", ["atf-nasaq", "al-muthanna", "idafa-definiteness", "tashbih"], J(PRE("wa", "سَاقَا"), ("مَعْطُوفٌ عَلَى «أَيْطَلَا» مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتِ النُّونُ لِلْإِضَافَةِ", "conjoined to «the flanks», in raf' by the alif, a dual whose nun is dropped in annexation", "«أَيْطَلَا»ya ma'tûf; tesniye olduğu için elif ile merfû, nûnu izâfetle düşmüştür")), s=[WA, ("سَاقَا", "saq", "noun")]),
 W("نَعَامَةٍ", "naama", "noun", ["idafa-definiteness"], J(MI), HEMI),
 W("وَإِرْخَاءُ", "irkha", "noun", ["atf-nasaq", "idafa-definiteness", "masdar", "tashbih"], J(PRE("wa", "إِرْخَاءُ"), ATF("أَيْطَلَا", "the flanks", "raf"), MUD, Dn("الْإِرْخَاءُ: ضَرْبٌ مِنْ عَدْوِ الذِّئْبِ يُشْبِهُ خَبَبَ الدَّوَابِّ", "الإِرْخَاء: a gait of the wolf, like the amble of riding-beasts", "الإِرْخَاء: kurdun, bineklerin rahvanına benzeyen bir koşu türü")), s=[WA, ("إِرْخَاءُ", "irkha", "noun")]),
 W("سِرْحَانٍ", "sirhan", "noun", ["idafa-definiteness"], J(MI, Dn("السِّرْحَانُ: الذِّئْبُ", "السِّرْحَان: the wolf", "السِّرْحَان: kurt"))),
 W("وَتَقْرِيبُ", "taqrib", "noun", ["atf-nasaq", "idafa-definiteness", "masdar", "tashbih"], J(PRE("wa", "تَقْرِيبُ"), ATF("أَيْطَلَا", "the flanks", "raf"), MUD, Dn("التَّقْرِيبُ: وَضْعُ الرِّجْلَيْنِ مَوْضِعَ الْيَدَيْنِ فِي الْعَدْوِ", "التَّقْرِيب: setting the hind feet where the forefeet were, in running", "التَّقْرِيب: koşarken arka ayakları ön ayakların yerine basmak")), s=[WA, ("تَقْرِيبُ", "taqrib", "noun")]),
 W("تَتْفُلِ", "tatful", "noun", ["idafa-definiteness", "al-qafiya"], J(MI, QAFIYA, Dn("التَّتْفُلُ: وَلَدُ الثَّعْلَبِ", "التَّتْفُل: the fox's cub", "التَّتْفُل: tilki yavrusu")), "."),
])
V(None, 60, "Big-ribbed; when you look at him from behind, he fills the gap between his legs with a full tail that hangs just above the ground and is not set askew.",
  "Kaburgaları iridir; arkasından baktığında, bacaklarının arasını yere az kalacak kadar inen, bir yana eğik olmayan gür bir kuyrukla kapatmıştır.", [
 T("ضَلِيعٍ", "dali", "noun", ["naat-sifa", "sifa-mushabbaha"], NAAT_FARAS[0] + "، " + RAF3[0] + " — الضَّلِيعُ: الْعَظِيمُ الْأَضْلَاعِ الْمُنْتَفِخُ الْجَنْبَيْنِ.", NAAT_FARAS[1] + "; " + RAF3[1] + " — الضَّلِيع: big in the ribs, full in the sides.", NAAT_FARAS[2] + "; " + RAF3[2] + " — الضَّلِيع: kaburgaları iri, yanları dolgun."),
 W("إِذَا", "idha", "part", ["maful-fih", "idha-shartiyya"], J(IDHA, Dn("مُتَعَلِّقٌ بِجَوَابِهِ «سَدَّ»، وَ«إِذَا» وَمَا بَعْدَهَا نَعْتٌ آخَرُ لِلْفَرَسِ", "it hangs on its answer, «he fills»; إِذَا with what follows is a further description of the horse", "cevabı olan «سَدَّ»ye müteallik; «إِذَا» ve sonrası atın bir başka sıfatıdır"))),
 T("اسْتَدْبَرْتَهُ", "istadbara", "verb", ["form-x-verbs", "al-bariz-al-muttasil", "maful-bihi"],
   MADI_TU[0] + "، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا؛ الِاسْتِدْبَارُ: النَّظَرُ إِلَى دُبُرِ الشَّيْءِ، وَهُوَ مُؤَخَّرُهُ.",
   MADI_TU[1] + "; the هُ is its direct object, in the seat of nasb — the clause is in the seat of jarr, annexed to إِذَا; الاِسْتِدْبَار: to look at the hinder part of a thing.",
   MADI_TU[2] + "; «hû» mef'ûlün bih, mahallen mansûb — cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr; الاِسْتِدْبَار: bir şeyin arka tarafına bakmak.", s=[("اسْتَدْبَرْتَ", "istadbara", "verb"), P("هُ")]),
 W("سَدَّ", "sadda-block", "verb", ["doubled-verbs"], J(MADI, HID("هُوَ", "he", "hüve", ("الْفَرَسِ", "the horse", "ata")), Dn("وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا", "the clause is the answer of إِذَا and has no seat", "cümle «إِذَا»nın cevabıdır, mahalli yoktur"))),
 W("فَرْجَهُ", "farj-gap", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, IDF("هُ"), Dn("الْفَرْجُ: الْفَضَاءُ بَيْنَ الْيَدَيْنِ وَالرِّجْلَيْنِ، وَالْمُرَادُ مَا بَيْنَ رِجْلَيْهِ", "الفَرْج: the open space between the legs — here, between his hind legs", "الفَرْج: bacakların arasındaki açıklık — burada arka bacaklarının arası")), HEMI, [("فَرْجَ", "farj-gap", "noun"), P("هُ")]),
 T("بِضَافٍ", "dafin-full", "noun", ["huruf-jarr", "ism-fail", "ism-maqsur-manqus", "hadhf-wa-taqdir", "ijaz-al-hadhf"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَضَافٍ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«سَدَّ». أَرَادَ: بِذَنَبٍ ضَافٍ، فَحَذَفَ الْمَوْصُوفَ اجْتِزَاءً بِدَلَالَةِ الصِّفَةِ عَلَيْهِ، كَقَوْلِهِمْ: مَرَرْتُ بِكَرِيمٍ، أَيْ: بِإِنْسَانٍ كَرِيمٍ. الضَّفْوُ: السُّبُوغُ وَالتَّمَامُ.",
   "The ba is a jarr letter; ضَافٍ is in jarr by a kasra estimated on the ya that falls before the tanwin — the phrase hangs on «he fills». He means «with a full tail»: the noun is dropped because its adjective is enough to show it, as one says «I passed by a generous [man]» (al-Zawzanī). الضَّفْو: fullness and length.",
   "Bâ cer harfi; ضَافٍ, tenvin sebebiyle düşen yâ üzerinde takdîrî kesre ile mecrûr — câr-mecrûr «سَدَّ»ye müteallik. Maksat «gür bir kuyrukla»dır; sıfat delâlet ettiği için mevsûf hazfedilmiştir; «مَرَرْتُ بِكَرِيمٍ» (yani kerîm bir insana uğradım) denmesi gibi (Zevzenî). الضَّفْو: bolluk ve tamlık.", s=[BI, ("ضَافٍ", "dafin-full", "noun")]),
 W("فُوَيْقَ", "fuwayqa", "noun", ["maful-fih", "idafa-definiteness"], J(("ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ", "An adverb of place, in nasb by the fatha, annexed", "Mekân zarfı, fetha ile mansûb, muzâf"), Dn("مُتَعَلِّقٌ بِـ«ضَافٍ»؛ تَصْغِيرُ «فَوْقَ» وَهُوَ تَصْغِيرُ التَّقْرِيبِ، مِثْلُ قُبَيْلَ وَبُعَيْدَ. وَشَرَطَ كَوْنَهُ فُوَيْقَ الْأَرْضِ لِأَنَّهُ إِذَا بَلَغَهَا وَطِئَهُ بِرِجْلَيْهِ، وَذٰلِكَ عَيْبٌ", "it hangs on «full»; the diminutive of فَوْقَ, a diminutive of nearness, like قُبَيْلَ and بُعَيْدَ. He makes it «just above the ground» because a tail that reaches the ground is trodden on, and that is a fault (al-Zawzanī)", "«ضَافٍ»e müteallik; «فَوْقَ»nın tasgîri, yakınlık bildiren tasgîrdir (قُبَيْلَ, بُعَيْدَ gibi). «Yerin hemen üstünde» şartını koşmuştur; çünkü kuyruk yere değerse at ona basar, bu da kusurdur (Zevzenî)"))),
 W("الْأَرْضِ", "ard", "noun", ["idafa-definiteness"], J(MI)),
 T("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "jumla-sifa"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الذَّنَبِ الْمَحْذُوفِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لَهُ، أَوْ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْهُ.", "A defective past verb built on fatha; its noun is a hidden pronoun returning to the omitted «tail» — the clause is a second adjective of it, in the seat of jarr, or a hal of it, in the seat of nasb.", "Fetha üzere mebnî nâkıs mâzî; ismi mahzûf «kuyruğa» dönen gizli zamir — cümle onun ikinci na'tı olarak mahallen mecrûr ya da ondan hâl olarak mahallen mansûb."),
 T("بِأَعْزَلِ", "azal-tail", "noun", ["kana-wa-akhawatuha", "huruf-jarr", "mamnu-min-sarf", "al-qafiya"],
   "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَأَعْزَلِ خَبَرُ «لَيْسَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ حَرْفِ الْجَرِّ الزَّائِدِ — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ، وَجُرَّ بِالْكَسْرَةِ لِضَرُورَةِ الشِّعْرِ. الْأَعْزَلُ: الَّذِي يَمِيلُ عَظْمُ ذَنَبِهِ إِلَى أَحَدِ الشِّقَّيْنِ.",
   "The ba is an added jarr letter that strengthens the negation; أَعْزَلِ is the predicate of لَيْسَ, in nasb by a fatha that the added letter's vowel keeps from showing — a diptote (an adjective on أَفْعَل), given the kasra here by poetic licence. الأَعْزَل: a horse whose tail-bone leans to one side.",
   "Bâ, nefyi pekiştiren zâid cer harfi; أَعْزَلِ «لَيْسَ»nin haberi; zâid harfin harekesi mahalli meşgul ettiği için takdîrî fetha ile mansûb — vasfiyet ve ef'al vezni sebebiyle gayr-i munsariftir, şiir zarûretiyle kesre almıştır. الأَعْزَل: kuyruk kemiği bir yana eğik olan at.", ".", [BI, ("أَعْزَلِ", "azal-tail", "noun")]),
])
V(None, 61, "When he bears down in his run, it is as though on the two sides of his back there lay a bride's perfume-stone, or a slab on which colocynth is pounded.",
  "Koşuya yüklendiğinde, sırtının iki yanında sanki bir gelinin koku ezdiği taş ya da Ebucehil karpuzu dövülen yassı taş vardır.", [
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + ". وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شَبَّهَ انْمِلَاسَ ظَهْرِهِ وَاكْتِنَازَهُ بِاللَّحْمِ بِالْحَجَرِ الَّذِي تَسْحَقُ الْعَرُوسُ بِهِ أَوْ عَلَيْهِ الطِّيبَ، أَوْ بِالْحَجَرِ الَّذِي يُكْسَرُ عَلَيْهِ الْحَنْظَلُ وَيُسْتَخْرَجُ حَبُّهُ؛ وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الْمَلَاسَةُ وَالصَّلَابَةُ. وَالْجُمْلَةُ مُسْتَأْنَفَةٌ لَا مَحَلَّ لَهَا.",
   KAANNA_T[1] + ". A tashbih mursal mujmal: the smoothness of his back and its firm packing with flesh are likened to the stone with which, or on which, a bride grinds perfume, or to the stone on which colocynth is cracked for its seed (al-Zawzanī); the particle is كَأَنَّ, and the point of likeness — smoothness and hardness — is left unsaid. The sentence is a fresh one and has no seat.",
   KAANNA_T[2] + ". Teşbih-i mürsel mücmeldir: sırtının düzgünlüğü ve etle dolgunluğu, gelinin kendisiyle ya da üzerinde koku ezdiği taşa yahut üzerinde Ebucehil karpuzu kırılıp çekirdeği çıkarılan taşa benzetilmiştir (Zevzenî); edat كَأَنَّ; vech-i şebeh — düzgünlük ve sertlik — mahzûftur. Cümle müste'nefedir, mahalli yoktur."),
 HARF_JARR("عَلَى", "ala"),
 T("الْمَتْنَيْنِ", "matn", "noun", ["huruf-jarr", "al-muthanna", "inna-wa-akhawatuha", "taqdim-al-musnad"],
   "مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَأَنَّ مُقَدَّمٍ عَلَى اسْمِهَا؛ الْمَتْنَانِ: مَا عَنْ يَمِينِ الْفَقَارِ وَشِمَالِهِ.",
   "In jarr by the ya, being a dual — the phrase hangs on the omitted predicate of كَأَنَّ, set before its noun; المَتْنَان: what lies to the right and left of the spine.",
   "Tesniye olduğu için yâ ile mecrûr — câr-mecrûr, كَأَنَّ'nin ismine takdim edilmiş mahzûf haberine müteallik; المَتْنَان: omurganın sağında ve solunda kalan kısımlar."),
 T("مِنْهُ", "min", "prep", ["huruf-jarr", "hal"], "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى الْفَرَسِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ «الْمَتْنَيْنِ»، أَوْ نَعْتٍ لَهُ إِنْ جُعِلَتْ «أَلْ» لِلْجِنْسِ، وَالْحَالُ أَوْلَى.", "مِنْ is a jarr letter and the هُ is in the seat of jarr, returning to the horse — the phrase hangs on an omitted hal of «the two sides of the back» — or on an adjective of it, if the article is taken as generic; the hal is the better reading.", "مِنْ cer harfi, «hû» mahallen mecrûr, ata döner — câr-mecrûr «الْمَتْنَيْنِ»den mahzûf hâle — ya da «أَلْ» cins için sayılırsa onun mahzûf na'tına — müteallik; hâl olması evlâdır.", s=[("مِنْ", "min", "prep"), P("هُ")]),
 T("إِذَا", "idha", "part", ["maful-fih"], "ظَرْفُ زَمَانٍ مُجَرَّدٌ عَنِ الشَّرْطِ، مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ، مُتَعَلِّقٌ بِمَا فِي «كَأَنَّ» مِنْ مَعْنَى الْفِعْلِ، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.", "An adverb of time with no sense of condition, built on sukun in the seat of nasb; it hangs on the verbal sense in كَأَنَّ and is annexed to the clause after it.", "Şart mânâsından soyutlanmış zaman zarfı; sükûn üzere mebnî, mahallen mansûb; «كَأَنَّ»deki fiil mânâsına müteallik, sonraki cümleye muzâf."),
 W("انْتَحَى", "intaha-lean", "verb", ["form-viii-verbs", "naqis-verbs"], J(("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A past verb built on a fatha estimated on the alif", "Elif üzerinde takdîrî fetha üzere mebnî mâzî"), HID("هُوَ", "he", "hüve", ("الْفَرَسِ", "the horse", "ata")), Dn("وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا؛ الِانْتِحَاءُ: الِاعْتِمَادُ وَالْقَصْدُ. وَيُرْوَى: «كَأَنَّ سَرَاتَهُ لَدَى الْبَيْتِ قَائِمًا»", "the clause is in the seat of jarr, annexed to إِذَا; الاِنْتِحَاء: bearing down, making for a thing. The half-verse is also transmitted «كَأَنَّ سَرَاتَهُ لَدَى الْبَيْتِ قَائِمًا» — «as though his back, as he stands by the tent, were…»", "cümle «إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr; الاِنْتِحَاء: yüklenmek, yönelmek. Mısra «كَأَنَّ سَرَاتَهُ لَدَى الْبَيْتِ قَائِمًا» («çadırın yanında dururken sırtı sanki…») şeklinde de rivayet edilir")), HEMI),
 W("مَدَاكَ", "madak", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], J(("اسْمُ كَأَنَّ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ", "The noun of كَأَنَّ, placed last, in nasb by the fatha", "كَأَنَّ'nin sona bırakılmış ismi, fetha ile mansûb"), MUD, Dn("الْمَدَاكُ: الْحَجَرُ الَّذِي يُسْحَقُ بِهِ الطِّيبُ وَغَيْرُهُ، وَالَّذِي يُسْحَقُ عَلَيْهِ أَيْضًا؛ وَالدَّوْكُ: السَّحْقُ", "المَدَاك: the stone with which perfume and the like is ground, and also the one on which it is ground; الدَّوْك: grinding", "المَدَاك: kendisiyle koku ve benzeri ezilen taş; üzerinde ezilen taşa da denir; الدَّوْك: ezmek"))),
 W("عَرُوسٍ", "arus", "noun", ["idafa-definiteness"], J(MI, Dn("وَخَصَّ مَدَاكَ الْعَرُوسِ لِحِدْثَانِ عَهْدِهَا بِالسَّحْقِ لِلطِّيبِ", "he names the bride's stone because she has only just been grinding perfume on it", "gelinin taşını anmıştır, çünkü o, koku ezmeyi daha yeni bırakmıştır"))),
 T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «veya»."),
 W("صَلَايَةَ", "salaya", "noun", ["atf-nasaq", "idafa-definiteness"], J(("مَعْطُوفٌ عَلَى «مَدَاكَ» مَنْصُوبٌ بِالْفَتْحَةِ", "Conjoined to «a perfume-stone», in nasb by the fatha", "«مَدَاكَ»ye ma'tûf, fetha ile mansûb"), MUD, Dn("الصَّلَايَةُ: الْحَجَرُ الْأَمْلَسُ الَّذِي يُسْحَقُ عَلَيْهِ شَيْءٌ كَالْهَبِيدِ، وَهُوَ حَبُّ الْحَنْظَلِ", "الصَّلَايَة: the smooth stone on which a thing such as colocynth seed is pounded", "الصَّلَايَة: üzerinde Ebucehil karpuzu çekirdeği gibi şeylerin dövüldüğü düz taş"))),
 W("حَنْظَلِ", "hanzal", "noun", ["idafa-definiteness", "al-qafiya"], J(MI, QAFIYA), "."),
])
V(None, 62, "The blood of the foremost of the herd upon his throat is like the juice of henna on combed grey hair.",
  "Av sürüsünün öndekilerinin kanı, onun göğsünde, sanki taranmış ak saça sürülmüş kına suyudur.", [
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + ". وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شَبَّهَ الدَّمَ الْجَامِدَ عَلَى نَحْرِهِ مِنْ دِمَاءِ الصَّيْدِ بِمَا جَفَّ مِنْ عُصَارَةِ الْحِنَّاءِ عَلَى شَعْرِ الْأَشْيَبِ؛ وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الْحُمْرَةُ عَلَى الْبَيَاضِ.",
   KAANNA_T[1] + ". A tashbih mursal mujmal: the blood of the game, dried upon his throat, is likened to henna-juice dried on the hair of a grey-headed man (al-Zawzanī); the particle is كَأَنَّ, and the point of likeness — red upon white — is left unsaid.",
   KAANNA_T[2] + ". Teşbih-i mürsel mücmeldir: göğsünde kurumuş av kanı, ak saçlı birinin saçında kurumuş kına suyuna benzetilmiştir (Zevzenî); edat كَأَنَّ; vech-i şebeh — beyaz üzerinde kırmızılık — mahzûftur."),
 W("دِمَاءَ", "dam", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir", "ism-mamdud"], J(ISM_KAANNA, MUD)),
 W("الْهَادِيَاتِ", "hadiya-foremost", "noun", ["idafa-definiteness", "jam-muannath-salim", "ism-fail"], J(MI, Dn("الْهَادِيَاتُ: الْمُتَقَدِّمَاتُ وَالْأَوَائِلُ، أَيْ: أَوَائِلُ الصَّيْدِ وَالْوَحْشِ؛ وَسُمِّيَ الْمُتَقَدِّمُ هَادِيًا لِأَنَّ هَادِيَ الْقَوْمِ يَتَقَدَّمُهُمْ", "الهَادِيَات: those that go in front, the first — the foremost of the game; the one in front is called هَادٍ because a people's guide goes before them", "الهَادِيَات: öne geçenler, ilkler — avın öndekileri; öndekine «هَادٍ» denmesi, kavmin kılavuzunun onların önünde gitmesindendir"))),
 T("بِنَحْرِهِ", "nahr-chest", "noun", ["huruf-jarr", "idafa-definiteness", "hal"], "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «عَلَى»، وَنَحْرِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «دِمَاءَ الْهَادِيَاتِ».", "The ba is a jarr letter meaning «upon»; نَحْرِ is in jarr by the kasra, annexed, and the هِ is its second term — the phrase hangs on an omitted hal of «the blood of the foremost».", "Bâ «üzerinde» anlamında cer harfi; نَحْرِ kesre ile mecrûr, muzâf; «hî» muzâfun ileyh — câr-mecrûr «دِمَاءَ الْهَادِيَاتِ»ten mahzûf hâle müteallik.", HEMI, [BI, ("نَحْرِ", "nahr-chest", "noun"), P("هِ")]),
 W("عُصَارَةُ", "usara", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], J(KHB_KAANNA, MUD, Dn("عُصَارَةُ الشَّيْءِ: مَا خَرَجَ مِنْهُ عِنْدَ عَصْرِهِ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "عُصَارَة of a thing: what comes out of it when it is pressed; the sentence is a fresh one", "bir şeyin عُصَارَة'si: sıkıldığında ondan çıkan su; cümle müste'nefedir"))),
 W("حِنَّاءٍ", "hinna", "noun", ["idafa-definiteness", "ism-mamdud"], J(MI)),
 T("بِشَيْبٍ", "shayb-greyness", "noun", ["huruf-jarr", "naat-sifa"], "الْبَاءُ حَرْفُ جَرٍّ، وَشَيْبٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«عُصَارَةُ حِنَّاءٍ»، أَيْ: خُضِبَ بِهَا شَيْبٌ؛ وَيَجُوزُ تَعْلِيقُهُمَا بِـ«عُصَارَةُ» نَفْسِهَا.", "The ba is a jarr letter and شَيْبٍ is in jarr by the kasra — the phrase hangs on an omitted adjective of «the juice of henna»: henna with which grey hair has been dyed; it may also hang on «juice» itself.", "Bâ cer harfi, شَيْبٍ kesre ile mecrûr — câr-mecrûr «عُصَارَةُ حِنَّاءٍ»in mahzûf na'tına müteallik: kendisiyle ak saç boyanmış kına; doğrudan «عُصَارَةُ»ye bağlanması da câizdir.", s=[BI, ("شَيْبٍ", "shayb-greyness", "noun")]),
 W("مُرَجَّلِ", "murajjal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(NAAT("شَيْبٍ", "jarr", en_of="grey hair"), QAFIYA, Dn("التَّرْجِيلُ: تَسْرِيحُ الشَّعْرِ، وَالْمُرَجَّلُ: الْمُسَرَّحُ بِالْمُشْطِ. قَالَ الزَّوْزَنِيُّ: وَأَتَى بِالْمُرَجَّلِ لِإِقَامَةِ الْقَافِيَةِ", "التَّرْجِيل: combing the hair; المُرَجَّل: combed out. Al-Zawzanī: he brings in «combed» to make the rhyme", "التَّرْجِيل: saçı taramak; المُرَجَّل: tarakla taranmış. Zevzenî: «مُرَجَّل»i kafiyeyi tutturmak için getirmiştir")), "."),
])
V(None, 63, "Then a herd came into our view, whose does were like the maidens of Dawār in long-trailing wraps.",
  "Derken karşımıza bir sürü çıktı; dişileri, uzun etekli örtüler içinde Devâr'ın çevresinde dönen bâkire kızlar gibiydi.", [
 W("فَعَنَّ", "anna-verb", "verb", ["doubled-verbs"], J(PRE("fa-ist", "عَنَّ"), lo(MADI), Dn("عَنَّ: عَرَضَ وَظَهَرَ", "عَنَّ: to come into view, to show itself", "عَنَّ: karşıya çıkmak, görünmek")), s=[FA, ("عَنَّ", "anna-verb", "verb")]),
 PJ("لَنَا", "لَ", "li", "نَا", LAM3, "عَنَّ", "came into view", "ye"),
 W("سِرْبٌ", "sirb", "noun", ["fail"], J(FAILR, Dn("السِّرْبُ: الْقَطِيعُ مِنَ الظِّبَاءِ أَوِ النِّسَاءِ أَوِ الْقَطَا أَوِ الْمَهَا أَوِ الْبَقَرِ أَوِ الْخَيْلِ، وَالْمُرَادُ هُنَا الْقَطِيعُ مِنْ بَقَرِ الْوَحْشِ", "السِّرْب: a herd or flock — of gazelles, women, sand-grouse, oryx, cattle or horses; here, a herd of wild cows", "السِّرْب: ceylan, kadın, bağırtlak, yaban sığırı, sığır ya da at sürüsü; burada yaban sığırı sürüsü"))),
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "jumla-sifa", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + " — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِـ«سِرْبٌ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شَبَّهَ الْمَهَا فِي بَيَاضِ أَلْوَانِهَا بِالْعَذَارَى لِأَنَّهُنَّ مَصُونَاتٌ فِي الْخُدُورِ لَا يُغَيِّرُ أَلْوَانَهُنَّ حَرُّ الشَّمْسِ، وَشَبَّهَ طُولَ أَذْيَالِهَا وَسُبُوغَ شَعْرِهَا بِالْمُلَاءِ الْمُذَيَّلِ، وَشَبَّهَ حُسْنَ مَشْيِهَا بِحُسْنِ تَبَخْتُرِ الْعَذَارَى فِي مَشْيِهِنَّ؛ وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ.",
   KAANNA_T[1] + " — the clause qualifies «a herd», in the seat of raf'. A tashbih mursal mujmal: the wild cows are likened, for their whiteness, to maidens — who are kept in their tents, so that the sun's heat does not change their colour; their long tails and full hair to trailing wraps; and their fine gait to the graceful swaying walk of maidens (al-Zawzanī). The particle is كَأَنَّ; the point of likeness is left unsaid.",
   KAANNA_T[2] + " — cümle «سِرْبٌ»ün na'tı olarak mahallen merfû. Teşbih-i mürsel mücmeldir: yaban sığırları, renklerinin beyazlığında bâkire kızlara benzetilmiştir — çünkü onlar çadırlarında korunur, güneşin sıcağı renklerini değiştirmez; kuyruklarının uzunluğu ve tüylerinin bolluğu uzun etekli örtülere, yürüyüşlerinin güzelliği de kızların salınarak yürüyüşüne benzetilmiştir (Zevzenî). Edat كَأَنَّ; vech-i şebeh mahzûftur."),
 W("نِعَاجَهُ", "naja", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], J(ISM_KAANNA, IDF("هُ"), Dn("النِّعَاجُ: اسْمٌ لِإِنَاثِ الضَّأْنِ وَبَقَرِ الْوَحْشِ، وَالْمُرَادُ هُنَا إِنَاثُ بَقَرِ الْوَحْشِ", "النِّعَاج: the females of sheep and of wild cattle; here, the wild cows", "النِّعَاج: koyunun ve yaban sığırının dişileri; burada yaban inekleri")), HEMI, [("نِعَاجَ", "naja", "noun"), P("هُ")]),
 W("عَذَارَى", "adhra", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir", "ism-maqsur-manqus"], J(("خَبَرُ كَأَنَّ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "The predicate of كَأَنَّ, in raf' by a damma estimated on the alif", "كَأَنَّ'nin haberi, elif üzerinde takdîrî damme ile merfû"), MUD, Dn("جَمْعُ عَذْرَاءَ: الْبِكْرُ الَّتِي لَمْ تُمَسَّ", "the plural of عَذْرَاء, a virgin", "«عَذْرَاء»nın (bâkire) cem'i"))),
 W("دَوَارٍ", "dawar", "propn", ["idafa-definiteness"], J(MI, Dn("دَوَارٌ: حَجَرٌ كَانَ أَهْلُ الْجَاهِلِيَّةِ يَنْصِبُونَهُ وَيَطُوفُونَ حَوْلَهُ", "Dawār: a stone that the people of the Jāhiliyya set up and walked round", "Devâr: Câhiliye ehlinin dikip etrafında döndüğü taş"))),
 HARF_JARR("فِي", "fi"),
 W("مُلَاءٍ", "mulaa", "noun", ["huruf-jarr", "hal", "ism-mamdud"], J(MAJR, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «عَذَارَى دَوَارٍ»؛ الْمُلَاءُ: جَمْعُ مُلَاءَةٍ، وَإِنَّمَا تُسَمَّى مُلَاءَةً إِذَا كَانَتْ لِفْقَيْنِ", "the phrase hangs on an omitted hal of «the maidens of Dawār»; المُلَاء: the plural of مُلَاءَة, a wrap — so called only when it is of two pieces sewn together", "câr-mecrûr «عَذَارَى دَوَارٍ»den mahzûf hâle müteallik; المُلَاء: «مُلَاءَة»nin cem'i; iki parçadan dikilmiş örtüye denir"))),
 W("مُذَيَّلِ", "mudhayyal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(NAAT("مُلَاءٍ", "jarr", en_of="wraps"), QAFIYA, Dn("الْمُذَيَّلُ: الَّذِي أُطِيلَ ذَيْلُهُ وَأُرْخِيَ", "المُذَيَّل: made long in the skirt and let trail", "المُذَيَّل: eteği uzatılıp salıverilmiş")), "."),
])

# =====================================================================================================================
# The hunt: verses 64–69
# =====================================================================================================================
HD = (" وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — ", " By the Talkhīṣ's definition, ", " Telhîs'in tarifine göre ")   # a figure no commentator names, that meets the Talkhīṣ's definition
ZARF_M = ("ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ", "An adverb of place, in nasb by the fatha, annexed", "Mekân zarfı, fetha ile mansûb, muzâf")
V(None, 64, "They turned and fled, like onyx beads set apart on a string, on the neck of a boy who has noble uncles in the clan on his father's side and on his mother's.",
  "Dönüp kaçtılar; aralarına başka taşlar dizilmiş Yemen boncukları gibiydiler — aşirette amcaları da dayıları da soylu bir çocuğun boynunda.", [
 T("فَأَدْبَرْنَ", "adbara", "verb", ["atf-nasaq", "form-iv-verbs", "al-bariz-al-muttasil"],
   "الْفَاءُ عَاطِفَةٌ، وَأَدْبَرْنَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ يَعُودُ عَلَى النِّعَاجِ — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا.",
   "The fa conjoins; أَدْبَرْنَ is a past verb built on sukun because the feminine nun is attached; the nun is the doer, in the seat of raf', and returns to the does — the clause is conjoined to the one before.",
   "Fâ atıf; أَدْبَرْنَ nûn-ı nisveye bitiştiği için sükûn üzere mebnî mâzî; nûn fâil, mahallen merfû, dişi sığırlara döner — cümle öncekine ma'tûf.", s=[FA, ("أَدْبَرْنَ", "adbara", "verb")]),
 T("كَالْجِزْعِ", "jiz-beads", "noun", ["huruf-jarr", "maful-mutlaq", "hadhf-wa-taqdir", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَالْجِزْعِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَفْعُولٍ مُطْلَقٍ مَحْذُوفٍ، أَيْ: أَدْبَرْنَ إِدْبَارًا كَالْجِزْعِ. الْجِزْعُ: الْخَرَزُ الْيَمَانِيُّ. وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ ذُكِرَ فِيهِ وَصْفُ الْمُشَبَّهِ بِهِ: شَبَّهَ بَقَرَ الْوَحْشِ بِالْخَرَزِ الْيَمَانِيِّ لِأَنَّهُ يَسْوَدُّ طَرَفَاهُ وَسَائِرُهُ أَبْيَضُ، وَكَذٰلِكَ بَقَرُ الْوَحْشِ تَسْوَدُّ أَكَارِعُهَا وَخُدُودُهَا وَسَائِرُهَا أَبْيَضُ؛ وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ.",
   "The kaf is a jarr letter of likening and الْجِزْعِ is in jarr by the kasra — the phrase hangs on an omitted adjective of an omitted absolute object: «they turned, a turning like onyx beads». الجِزْع: the Yemeni bead (onyx). A tashbih mursal mujmal in which the thing likened to is described: the wild cows are likened to Yemeni beads because the bead is black at its two ends and white elsewhere, and the wild cows are black in the shanks and the cheeks and white elsewhere (al-Zawzanī); the particle is the kaf, and the point of likeness is left unsaid.",
   "Kâf teşbih bildiren cer harfi, الْجِزْعِ kesre ile mecrûr — câr-mecrûr, mahzûf mef'ûlün mutlakın mahzûf na'tına müteallik: «Yemen boncukları gibi bir dönüşle döndüler». الجِزْع: Yemen boncuğu (oniks). Müşebbehün bihin vasfı zikredilmiş teşbih-i mürsel mücmeldir: yaban sığırları Yemen boncuğuna benzetilmiştir; çünkü boncuğun iki ucu siyah, gerisi beyazdır; yaban sığırlarının da incikleri ve yanakları siyah, gerisi beyazdır (Zevzenî); edat kâf, vech-i şebeh mahzûftur.", s=[KA, ("الْجِزْعِ", "jiz-beads", "noun")]),
 W("الْمُفَصَّلِ", "mufassal", "noun", ["naat-sifa", "ism-maful"], J(NAAT("الْجِزْعِ", "jarr", en_of="onyx beads"), Dn("أَيِ: الَّذِي فُصِلَ بَيْنَهُ بِغَيْرِهِ مِنَ الْجَوَاهِرِ؛ وَشَرَطَ كَوْنَهُ مُفَصَّلًا لِتَفَرُّقِهِنَّ عِنْدَ رُؤْيَتِهِ", "that is, set apart by other gems strung between them; he makes them «set apart» because the cows scattered at the sight of him", "yani aralarına başka mücevherler dizilmiş; «aralıklı» olmasını şart koşmuştur, çünkü sığırlar onu görünce dağılmıştır"))),
 T("بَيْنَهُ", "bayna", "noun", ["maful-fih", "idafa-definiteness", "naib-al-fail"],
   "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ فِي مَوْضِعِ نَائِبِ الْفَاعِلِ لِـ«الْمُفَصَّلِ»، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْجِزْعِ.",
   "An adverb of place, in nasb by the fatha, standing where the deputy doer of «set apart» would stand; annexed, and the هُ is its second term, returning to the beads.",
   "Mekân zarfı, fetha ile mansûb; «الْمُفَصَّلِ»in nâib-i fâili mevkiindedir; muzâf, «hû» muzâfun ileyh, boncuklara döner.", HEMI, [("بَيْنَ", "bayna", "noun"), P("هُ")]),
 T("بِجِيدِ", "jid", "noun", ["huruf-jarr", "idafa-definiteness", "naat-sifa"],
   "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَجِيدِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ ثَانٍ لِـ«الْجِزْعِ»، أَوْ حَالٍ مِنْهُ؛ الْجِيدُ: الْعُنُقُ.",
   "The ba is a jarr letter meaning «on»; جِيدِ is in jarr by the kasra, annexed — the phrase hangs on a second omitted adjective of «the beads», or on a hal of them; الجِيد: the neck.",
   "Bâ «-de» anlamında cer harfi; جِيدِ kesre ile mecrûr, muzâf — câr-mecrûr «الْجِزْعِ»in mahzûf ikinci na'tına ya da ondan hâle müteallik; الجِيد: boyun.", s=[BI, ("جِيدِ", "jid", "noun")]),
 T("مُعَمٍّ", "muamm", "noun", ["idafa-definiteness", "hadhf-wa-taqdir", "ism-maful"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيْ: بِجِيدِ صَبِيٍّ مُعَمٍّ. الْمُعَمُّ: الْكَرِيمُ الْأَعْمَامِ، وَالْمُخْوَلُ: الْكَرِيمُ الْأَخْوَالِ، وَقَدْ أَعَمَّ وَأَخْوَلَ؛ وَهُمَا مِنَ الشَّوَاذِّ لِأَنَّ الْقِيَاسَ مِنْ «أَفْعَلَ» فَهُوَ «مُفْعِلٌ»، وَهٰذَانِ «أَفْعَلَ» فَهُوَ «مُفْعَلٌ». وَشَرَطَ ذٰلِكَ لِأَنَّ جَوَاهِرَ قِلَادَةِ مِثْلِ هٰذَا الصَّبِيِّ أَعْظَمُ مِنْ جَوَاهِرِ قِلَادَةِ غَيْرِهِ.",
   "The second term of the idafa, in jarr by the kasra — it describes a noun left out: «on the neck of a boy with noble uncles». المُعَمّ: one whose paternal uncles are noble; المُخْوَل: one whose maternal uncles are noble, from أَعَمَّ and أَخْوَلَ. Both are irregular: أَفْعَلَ regularly gives مُفْعِل, and these give مُفْعَل. He adds this because the gems on such a boy's necklace are finer than on another's (al-Zawzanī).",
   "Muzâfun ileyh, kesre ile mecrûr — mahzûf mevsûfun na'tıdır: «amcaları soylu bir çocuğun boynunda». المُعَمّ: amcaları soylu olan; المُخْوَل: dayıları soylu olan; «أَعَمَّ» ve «أَخْوَلَ»den. İkisi de şâzdır: kıyas «أَفْعَلَ»den «مُفْعِل»dir, bunlar ise «مُفْعَل» gelmiştir. Bunu şart koşmuştur, çünkü böyle bir çocuğun gerdanlığındaki taşlar başkasınınkinden daha değerlidir (Zevzenî)."),
 HARF_JARR("فِي", "fi"),
 W("الْعَشِيرَةِ", "ashira", "noun", ["huruf-jarr"], J(MAJR, TA("مُعَمٍّ", "with noble uncles", "e"))),
 W("مُخْوَلِ", "mukhwal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ", "A second adjective of the omitted noun, in jarr by the kasra", "Mahzûf mevsûfun ikinci na'tı, kesre ile mecrûr"), QAFIYA, Dn("الْمُخْوَلُ: الْكَرِيمُ الْأَخْوَالِ", "المُخْوَل: one whose maternal uncles are noble", "المُخْوَل: dayıları soylu olan")), "."),
])
V(None, 65, "He brought us up with the foremost of them, while the laggards were still behind him, in a herd that had not yet been scattered.",
  "At bizi sürünün öndekilerine yetiştirdi; geride kalanları ise, henüz dağılmamış bir topluluk hâlinde, onun berisindeydi.", [
 T("فَأَلْحَقَنَا", "alhaqa", "verb", ["atf-nasaq", "form-iv-verbs", "maful-bihi", "kinaya", "aqsam-al-kinaya"],
   "الْفَاءُ عَاطِفَةٌ، وَأَلْحَقَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَرَسِ. قَالَ الزَّوْزَنِيُّ: يُرِيدُ أَنَّهُ يُدْرِكُ أَوَائِلَهَا قَبْلَ تَفَرُّقِ جَمَاعَتِهَا، يَصِفُهُ بِشِدَّةِ عَدْوِهِ — فَالْبَيْتُ كِنَايَةٌ عَنْ صِفَةٍ هِيَ شِدَّةُ الْعَدْوِ.",
   "The fa conjoins; أَلْحَقَ is a past verb built on fatha; نَا is its direct object, in the seat of nasb, and its doer is a hidden pronoun returning to the horse. Al-Zawzanī: he means that the horse overtakes the foremost before the herd has broken up — he describes how hard he runs. So the verse is a kinaya for a quality: the force of his run.",
   "Fâ atıf; أَلْحَقَ fetha üzere mebnî mâzî; نَا mef'ûlün bih, mahallen mansûb; fâili ata dönen gizli zamir. Zevzenî: atın, sürü dağılmadan öndekilere yetiştiğini kasteder; onu koşusunun şiddetiyle vasfeder. Demek ki beyit bir sıfattan kinâyedir: koşunun şiddeti.", s=[FA, ("أَلْحَقَ", "alhaqa", "verb"), P("نَا")]),
 T("بِالْهَادِيَاتِ", "hadiya-foremost", "noun", ["huruf-jarr", "jam-muannath-salim", "tibaq"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَادِيَاتِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَلْحَقَ»؛ الْهَادِيَاتُ: الْأَوَائِلُ الْمُتَقَدِّمَاتُ." + HD[0] + "طِبَاقٌ بَيْنَ «الْهَادِيَاتِ» وَ«جَوَاحِرُهَا»: الْمُتَقَدِّمَاتُ وَالْمُتَخَلِّفَاتُ.",
   "The ba is a jarr letter and الْهَادِيَاتِ is in jarr by the kasra — the phrase hangs on «brought us up»; الهَادِيَات: the first, those in front." + HD[1] + "«الْهَادِيَاتِ» and «جَوَاحِرُهَا» make a tibaq: those in front against those behind.",
   "Bâ cer harfi, الْهَادِيَاتِ kesre ile mecrûr — câr-mecrûr «أَلْحَقَ»ya müteallik; الهَادِيَات: önde gidenler." + HD[2] + "«الْهَادِيَاتِ» ile «جَوَاحِرُهَا» arasında tıbâk vardır: öndekiler ile geride kalanlar.", s=[BI, ("الْهَادِيَاتِ", "hadiya-foremost", "noun")]),
 T("وَدُونَهُ", "duna", "noun", ["anwa-al-waw", "maful-fih", "idafa-definiteness", "mubtada-khabar", "taqdim-al-musnad"],
   "الْوَاوُ وَاوُ الْحَالِ، وَدُونَ ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْفَرَسِ — أَيْ: هِيَ أَقْرَبُ مِنْهُ، قَدْ جَاوَزَهَا.",
   "The waw is the waw of the hal; دُونَ is an adverb of place, in nasb by the fatha, hanging on an omitted predicate set first; annexed, and the هُ is its second term, returning to the horse — that is, they are on the near side of him: he has passed them.",
   "Vâv hâliye; دُونَ mekân zarfı, fetha ile mansûb, öne geçmiş mahzûf habere müteallik; muzâf, «hû» muzâfun ileyh, ata döner — yani onlar ondan beridedir, at onları geçmiştir.", HEMI, [WA, ("دُونَ", "duna", "noun"), P("هُ")]),
 W("جَوَاحِرُهَا", "jahira", "noun", ["mubtada-khabar", "idafa-definiteness", "jam-taksir", "al-hal-jumla-wa-rabituha", "tibaq"], J(("مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, placed last, in raf' by the damma", "Sona bırakılmış mübteda, damme ile merfû"), IDF("هَا"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «أَلْحَقَ»، وَالرَّابِطُ الْوَاوُ وَالضَّمِيرُ؛ الْجَوَاحِرُ: الْمُتَخَلِّفَاتُ، وَقَدْ جَحَرَ أَيْ: تَخَلَّفَ؛ تُطَابِقُ «الْهَادِيَاتِ»", "the clause is a hal of the doer of «brought us up», in the seat of nasb, tied to it by the waw and the pronoun; الجَوَاحِر: those that lag behind, from جَحَرَ «to fall back»; the contrary of «the foremost»", "cümle «أَلْحَقَ»nın fâilinden hâl olarak mahallen mansûb, râbıt vâv ile zamirdir; الجَوَاحِر: geride kalanlar; جَحَرَ «geri kalmak»tan; «الْهَادِيَاتِ»in zıddı")), s=[("جَوَاحِرُ", "jahira", "noun"), P("هَا")]),
 HARF_JARR("فِي", "fi"),
 W("صَرَّةٍ", "sarra-herd", "noun", ["huruf-jarr", "hal"], J(MAJR, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي الظَّرْفِ «دُونَهُ»، وَعِنْدَ سِيبَوَيْهِ مِنْ «جَوَاحِرُهَا»؛ الصَّرَّةُ: الْجَمَاعَةُ، وَالصَّرَّةُ أَيْضًا: الصَّيْحَةُ", "the phrase hangs on an omitted hal of the pronoun hidden in the adverb «behind him» — or, for Sībawayh, of «the laggards»; الصَّرَّة: a company, a herd; it is also a cry", "câr-mecrûr, «دُونَهُ» zarfındaki gizli zamirden — Sîbeveyh'e göre «جَوَاحِرُهَا»dan — mahzûf hâle müteallik; الصَّرَّة: topluluk; «çığlık» anlamına da gelir"))),
 T("لَمْ", "lam-jazima", "part", ["lam-jazim"], LAM_J[0], LAM_J[1], LAM_J[2]),
 T("تُزَيَّلِ", "zayyala", "verb", ["lam-jazim", "form-ii-verbs", "al-majhul-fil-kafiya", "jumla-sifa", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + KASR_Q[0] + "، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى «صَرَّةٍ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لَهَا؛ التَّزْيِيلُ: التَّفْرِيقُ. وَيُرْوَى «تَزَيَّلِ» بِالْبِنَاءِ لِلْفَاعِلِ، أَيْ: تَتَزَيَّلْ.",
   "A passive present verb in jazm by لَمْ, its sign the sukun" + KASR_Q[1] + "; its deputy doer is a hidden pronoun returning to «a herd» — the clause qualifies it, in the seat of jarr; التَّزْيِيل: scattering. It is also transmitted in the active, «تَزَيَّلِ», for تَتَزَيَّلْ.",
   "لَمْ ile meczûm meçhul muzâri, cezm alâmeti sükûn" + KASR_Q[2] + "; nâib-i fâili «صَرَّةٍ»e dönen gizli zamir — cümle onun na'tı olarak mahallen mecrûr; التَّزْيِيل: dağıtmak. Ma'lûm olarak «تَزَيَّلِ» (yani تَتَزَيَّلْ) de rivayet edilir.", "."),
])
V(None, 66, "He ran down a bull and a cow, one after the other in a single heat, and was not so wet with sweat that he might be washed by it.",
  "Bir boğa ile bir ineği ardı ardına, tek koşuda avladı; üstelik yıkanmış gibi olacak kadar terlemedi.", [
 T("فَعَادَى", "ada-hunt", "verb", ["atf-nasaq", "form-iii-verbs", "naqis-verbs", "majaz-aqli"],
   "الْفَاءُ عَاطِفَةٌ، وَعَادَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَرَسِ. الْمُعَادَاةُ وَالْعِدَاءُ: الْمُوَالَاةُ، أَيْ: وَالَى بَيْنَ ثَوْرٍ وَنَعْجَةٍ فِي طَلَقٍ وَاحِدٍ. قَالَ الزَّوْزَنِيُّ: نَسَبَ فِعْلَ الْفَارِسِ إِلَى الْفَرَسِ لِأَنَّهُ حَامِلُهُ وَمُوصِلُهُ إِلَى مَرَامِهِ — فَهُوَ مَجَازٌ عَقْلِيٌّ عَلَاقَتُهُ السَّبَبِيَّةُ.",
   "The fa conjoins; عَادَى is a past verb built on a fatha estimated on the alif; its doer is a hidden pronoun returning to the horse. المُعَادَاة and العِدَاء: taking one after another — he took a bull and a cow in one heat. Al-Zawzanī: he ascribes the rider's act to the horse, because the horse carries him and brings him to what he seeks. So it is a majaz ʿaqlī whose tie is cause.",
   "Fâ atıf; عَادَى elif üzerinde takdîrî fetha üzere mebnî mâzî; fâili ata dönen gizli zamir. المُعَادَاة ve العِدَاء: ardı ardına yapmak — tek koşuda bir boğa ile bir ineği peş peşe avladı. Zevzenî: binicinin fiilini ata nisbet etmiştir, çünkü onu taşıyan ve muradına ulaştıran attır. Demek ki alâkası sebebiyet olan mecâz-ı aklîdir.", s=[FA, ("عَادَى", "ada-hunt", "verb")]),
 T("عِدَاءً", "ida", "noun", ["maful-mutlaq", "masdar", "ism-mamdud", "mulhaq-bil-jinas"],
   "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ." + HD[0] + "مَا يُلْحَقُ بِالْجِنَاسِ بَيْنَ «عَادَى» وَ«عِدَاءً»: يَجْمَعُهُمَا الِاشْتِقَاقُ.",
   "An absolute object, in nasb by the fatha." + HD[1] + "there is what is joined to the jinās between «عَادَى» and «عِدَاءً»: derivation from one root binds them.",
   "Mef'ûlün mutlak, fetha ile mansûb." + HD[2] + "«عَادَى» ile «عِدَاءً» arasında cinâsa mülhak olan iştikak vardır."),
 W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], J(ZARF_M, Dn("مُتَعَلِّقٌ بِـ«عَادَى»، أَوْ بِالْمَصْدَرِ «عِدَاءً»", "it hangs on «ran down», or on the masdar «عِدَاءً»", "«عَادَى»ya ya da «عِدَاءً» masdarına müteallik"))),
 W("ثَوْرٍ", "thawr", "noun", ["idafa-definiteness"], J(MI, Dn("أَيْ: ثَوْرٍ مِنْ بَقَرِ الْوَحْشِ", "that is, a bull of the wild cattle", "yani yaban sığırlarından bir boğa"))),
 W("وَنَعْجَةٍ", "naja", "noun", ["atf-nasaq"], J(PRE("wa", "نَعْجَةٍ"), ATF("ثَوْرٍ", "a bull")), HEMI, [WA, ("نَعْجَةٍ", "naja", "noun")]),
 W("دِرَاكًا", "dirak", "noun", ["maful-mutlaq", "masdar"], J(("مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ لِأَنَّهُ مَصْدَرٌ مُرَادِفٌ لِلْفِعْلِ السَّابِقِ، وَقِيلَ: مَصْدَرٌ وَقَعَ حَالًا", "An absolute object, in nasb by the fatha — a masdar of the same sense as the verb before; it is also read as a masdar standing as a hal", "Mef'ûlün mutlak, fetha ile mansûb — önceki fiille eş anlamlı masdar; hâl yerinde masdar olduğu da söylenmiştir"), Dn("الدِّرَاكُ: الْمُتَابَعَةُ، أَيْ: مُدَارَكَةً", "الدِّرَاك: following close, one upon the other", "الدِّرَاك: peş peşe gelmek"))),
 T("وَلَمْ", "lam-jazima", "part", ["atf-nasaq", "lam-jazim"], "الْوَاوُ عَاطِفَةٌ، وَيَجُوزُ أَنْ تَكُونَ وَاوَ الْحَالِ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The waw conjoins — or it may be the waw of the hal; لَمْ is the particle of negation that puts the verb in jazm and turns it to the past.", "Vâv atıf — hâliye olması da câizdir; لَمْ nefy, cezm ve kalb harfi.", s=[WA, ("لَمْ", "lam-jazima", "part")]),
 W("يَنْضَحْ", "nadaha", "verb", ["lam-jazim", "thulathi-mujarrad-babs"], J(("فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ", "A present verb in jazm by لَمْ, its sign the sukun", "لَمْ ile meczûm muzâri, cezm alâmeti sükûn"), HID("هُوَ", "he", "hüve", ("الْفَرَسِ", "the horse", "ata")), Dn("أَيْ: لَمْ يَعْرَقْ؛ وَيُرْوَى بِالْبِنَاءِ لِلْمَفْعُولِ", "that is, he did not sweat; it is also transmitted in the passive", "yani terlemedi; meçhul olarak da rivayet edilir"))),
 T("بِمَاءٍ", "ma-water", "noun", ["huruf-jarr", "ism-mamdud"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَاءٍ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَنْضَحْ»؛ وَالْمُرَادُ بِالْمَاءِ الْعَرَقُ.", "The ba is a jarr letter and مَاءٍ is in jarr by the kasra — the phrase hangs on «was wet»; by «water» he means sweat.", "Bâ cer harfi, مَاءٍ kesre ile mecrûr — câr-mecrûr «يَنْضَحْ»a müteallik; «su»dan maksat terdir.", s=[BI, ("مَاءٍ", "ma-water", "noun")]),
 T("فَيُغْسَلِ", "ghasala", "verb", ["atf-nasaq", "lam-jazim", "al-majhul-fil-kafiya", "mubalagha-maqbula", "al-qafiya"],
   "الْفَاءُ عَاطِفَةٌ، وَيُغْسَلِ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ عَلَى «يَنْضَحْ» مَجْزُومٌ مِثْلُهُ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + KASR_Q[0] + "، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — أَيْ: لَمْ يَعْرَقْ عَرَقًا مُفْرِطًا يَغْسِلُ جَسَدَهُ، يُرِيدُ أَنَّهُ أَدْرَكَهُمَا وَقَتَلَهُمَا فِي طَلَقٍ وَاحِدٍ دُونَ مُعَانَاةِ مَشَقَّةٍ. وَبِهٰذَا الْبَيْتِ مَثَّلَ التَّلْخِيصُ لِلْمُبَالَغَةِ الْمَقْبُولَةِ الَّتِي تُسَمَّى التَّبْلِيغَ، وَهُوَ أَنْ يَكُونَ الْمُدَّعَى مُمْكِنًا عَقْلًا وَعَادَةً.",
   "The fa conjoins; يُغْسَلِ is a passive present verb conjoined to «was wet» and in jazm like it, its sign the sukun" + KASR_Q[1] + "; its deputy doer is a hidden «he» — that is, he did not sweat so heavily that the sweat washed his body: he overtook and killed the two in one heat without strain (al-Zawzanī). The Talkhīṣ cites this very verse for the acceptable hyperbole called tablīgh: what is claimed is possible both in reason and in custom.",
   "Fâ atıf; يُغْسَلِ «يَنْضَحْ»a ma'tûf, onun gibi meczûm meçhul muzâri, cezm alâmeti sükûn" + KASR_Q[2] + "; nâib-i fâili gizli «hüve» — yani bedenini yıkayacak kadar aşırı terlemedi: ikisine tek koşuda, zahmet çekmeden yetişip öldürdü (Zevzenî). Telhîs, teblîğ denilen makbul mübalağaya bu beyti örnek verir: iddia edilen şey aklen de âdeten de mümkündür.", ".", [FA, ("يُغْسَلِ", "ghasala", "verb")]),
])
V(None, 67, "So the cooks of the meat were of two kinds: some roasting strips laid in rows on the hot stones, some hurrying a stew in the pot.",
  "Et pişirenler iki kısım oldu: kimi taşlara dizilmiş etleri kebap ediyor, kimi de tencerede acele bir yahni pişiriyordu.", [
 T("فَظَلَّ", "zalla-remain", "verb", ["atf-nasaq", "kana-wa-akhawatuha", "doubled-verbs", "kinaya", "aqsam-al-kinaya"],
   "الْفَاءُ عَاطِفَةٌ، وَظَلَّ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ. قَالَ الزَّوْزَنِيُّ: يَقُولُ: كَثُرَ الصَّيْدُ فَأَخْصَبَ الْقَوْمُ فَطَبَخُوا وَاشْتَوَوْا — فَالْبَيْتُ كِنَايَةٌ عَنْ صِفَةٍ هِيَ كَثْرَةُ الصَّيْدِ.",
   "The fa conjoins; ظَلَّ is a defective past verb built on fatha. Al-Zawzanī: he means that the game was plentiful, so the party fared well, and stewed and roasted. So the verse is a kinaya for a quality: the plenty of the kill.",
   "Fâ atıf; ظَلَّ fetha üzere mebnî nâkıs mâzî. Zevzenî: av bol oldu, topluluk bolluğa erdi, hem yahni hem kebap yaptılar, demek ister. Demek ki beyit bir sıfattan kinâyedir: avın bolluğu.", s=[FA, ("ظَلَّ", "zalla-remain", "verb")]),
 W("طُهَاةُ", "tahin", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "jam-taksir", "ism-fail"], J(("اسْمُ «ظَلَّ» مَرْفُوعٌ بِالضَّمَّةِ", "The noun of ظَلَّ, in raf' by the damma", "«ظَلَّ»nin ismi, damme ile merfû"), MUD, Dn("جَمْعُ طَاهٍ كَالْقُضَاةِ جَمْعِ قَاضٍ؛ الطَّهْوُ وَالطَّهْيُ: الْإِنْضَاجُ", "the plural of طَاهٍ, as قُضَاة is of قَاضٍ; الطَّهْو: cooking", "«طَاهٍ»in cem'i (قَاضٍ – قُضَاة gibi); الطَّهْو: pişirmek"))),
 W("اللَّحْمِ", "lahm", "noun", ["idafa-definiteness", "idafa-lafziyya"], J(MI, Dn("مِنْ إِضَافَةِ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ", "the ism fa'il annexed to its object", "ism-i fâilin mef'ûlüne izâfeti"))),
 HARF_JARR("مِنْ", "min", " لِلتَّفْصِيلِ وَالتَّفْسِيرِ، كَقَوْلِهِمْ: هُمْ مِنْ بَيْنِ عَالِمٍ وَزَاهِدٍ، يُرِيدُ أَنَّهُمْ لَا يَعْدُونَ الصِّنْفَيْنِ", " — it sets out the kinds, as one says «they are, between them, scholars and ascetics»: they are these two kinds and no other (al-Zawzanī)", " — tafsil ve tefsir içindir; «onlar âlim ile zâhid arasındadır» denmesi gibi: bu iki sınıfın dışına çıkmazlar (Zevzenî)"),
 W("بَيْنِ", "bayna", "noun", ["huruf-jarr", "idafa-definiteness", "kana-wa-akhawatuha"], J(MAJR, MUD, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «ظَلَّ»", "the phrase hangs on the omitted predicate of ظَلَّ", "câr-mecrûr «ظَلَّ»nin mahzûf haberine müteallik"))),
 W("مُنْضِجٍ", "mundij", "noun", ["idafa-definiteness", "ism-fail", "shurut-amal-ism-al-fail"], J(MI, Dn("اسْمُ فَاعِلٍ مِنْ «أَنْضَجَ»، يَنْصِبُ «صَفِيفَ»؛ وَالْإِنْضَاجُ يَشْتَمِلُ عَلَى طَبْخِ اللَّحْمِ وَشَيِّهِ", "the ism fa'il of أَنْضَجَ; it puts «strips» in nasb; الإِنْضَاج covers both boiling meat and roasting it", "«أَنْضَجَ»den ism-i fâil; «صَفِيفَ»i nasb eder; الإِنْضَاج eti hem haşlamayı hem kızartmayı kapsar")), HEMI),
 W("صَفِيفَ", "safif", "noun", ["maful-bihi", "idafa-definiteness"], J(("مَفْعُولٌ بِهِ لِـ«مُنْضِجٍ» مَنْصُوبٌ بِالْفَتْحَةِ", "The direct object of «one who cooks», in nasb by the fatha", "«مُنْضِجٍ»in mef'ûlün bihi, fetha ile mansûb"), MUD, Dn("الصَّفِيفُ: الْمَصْفُوفُ عَلَى الْحِجَارَةِ لِيَنْضَجَ", "الصَّفِيف: meat laid in rows on the stones to cook", "الصَّفِيف: pişsin diye taşların üzerine dizilmiş et"))),
 W("شِوَاءٍ", "shiwa", "noun", ["idafa-definiteness", "ism-mamdud"], J(MI)),
 T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «veya»."),
 T("قَدِيرٍ", "qadir-stew", "noun", ["atf-nasaq", "hadhf-al-mudaf-wal-mudaf-ilayh"],
   "مَعْطُوفٌ عَلَى «صَفِيفَ»، وَجُرَّ عَلَى تَوَهُّمِ جَرِّ الْمَعْطُوفِ عَلَيْهِ بِالْإِضَافَةِ، كَأَنَّهُ قَالَ: مِنْ بَيْنِ مُنْضِجِ صَفِيفِ شِوَاءٍ أَوْ قَدِيرٍ؛ وَقِيلَ: جُرَّ لِمُجَاوَرَةِ الْمَجْرُورِ؛ وَقِيلَ: التَّقْدِيرُ: أَوْ طَابِخِ قَدِيرٍ، فَحُذِفَ الْمُضَافُ وَبَقِيَ الْمُضَافُ إِلَيْهِ مَجْرُورًا. الْقَدِيرُ: اللَّحْمُ الْمَطْبُوخُ فِي الْقِدْرِ.",
   "Conjoined to «strips», and put in jarr as if the word it is joined to were itself in jarr by annexation — as though he had said مُنْضِجِ صَفِيفِ شِوَاءٍ أَوْ قَدِيرٍ; some say it takes jarr from the word beside it; and some supply «or one who stews a stew», the annexed noun being dropped and its second term left in jarr. القَدِير: meat cooked in the pot.",
   "«صَفِيفَ»e ma'tûf; ma'tûfun aleyhin izâfetle mecrûr olduğu tevehhümüyle cer edilmiştir; sanki «مُنْضِجِ صَفِيفِ شِوَاءٍ أَوْ قَدِيرٍ» demiştir. Mecrûra komşuluk sebebiyle cer edildiği de söylenmiştir; bir görüşe göre de takdiri «ya da yahni pişiren»dir: muzâf hazfedilmiş, muzâfun ileyh mecrûr kalmıştır. القَدِير: tencerede pişirilmiş et."),
 W("مُعَجَّلِ", "muajjal-hasty", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(NAAT("قَدِيرٍ", "jarr", en_of="a stew"), QAFIYA), "."),
])
V(None, 68, "Then evening came upon us, and the eye almost failed before him: whenever it climbed up him, it came down again.",
  "Sonra akşamladık; göz onun karşısında neredeyse âciz kalıyordu: ne zaman onda yukarı çıksa yine aşağı iniyordu.", [
 T("وَرُحْنَا", "raha-become", "verb", ["atf-nasaq", "hollow-verbs", "al-bariz-al-muttasil", "al-fil-al-tamm-wal-naqis"],
   "الْوَاوُ عَاطِفَةٌ، وَرُحْنَا فِعْلٌ مَاضٍ تَامٌّ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا الْفَاعِلِينَ، وَنَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — أَيْ: ثُمَّ أَمْسَيْنَا.",
   "The waw conjoins; رُحْنَا is a complete past verb built on sukun because the نَا of the doers is attached; نَا is the doer, in the seat of raf' — that is, «then evening came upon us».",
   "Vâv atıf; رُحْنَا fâil olan نَا'ya bitiştiği için sükûn üzere mebnî tam mâzî; نَا fâil, mahallen merfû — yani «sonra akşamladık».", s=[WA, ("رُحْنَا", "raha-become", "verb")]),
 W("يَكَادُ", "kada", "verb", ["afal-al-muqaraba", "hollow-verbs", "al-hal-jumla-wa-rabituha"], J(("فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ بِالضَّمَّةِ", "A defective present verb in raf' by the damma", "Damme ile merfû nâkıs muzâri"), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «نَا» فِي «رُحْنَا»، وَالرَّابِطُ مُقَدَّرٌ أَيْ: يَكَادُ الطَّرْفُ مِنَّا", "the clause is a hal of the نَا in «we came home», in the seat of nasb; its tie is understood: «our eye almost…»", "cümle «رُحْنَا»daki نَا'dan hâl olarak mahallen mansûb; râbıt mukadderdir: «gözümüz neredeyse…»"))),
 W("الطَّرْفُ", "tarf", "noun", ["afal-al-muqaraba"], J(("اسْمُ «يَكَادُ» مَرْفُوعٌ بِالضَّمَّةِ", "The noun of يَكَادُ, in raf' by the damma", "«يَكَادُ»nün ismi, damme ile merfû"), Dn("الطَّرْفُ: اسْمٌ لِمَا يَتَحَرَّكُ مِنْ أَشْفَارِ الْعَيْنِ، وَالْمُرَادُ الْعَيْنُ", "الطَّرْف: what moves of the eyelids; the eye is meant", "الطَّرْف: gözün hareket eden kirpik kenarları; maksat gözdür"))),
 W("يَقْصُرُ", "qasara", "verb", ["mudari-marfu", "thulathi-mujarrad-babs", "afal-al-muqaraba"], J(MUDR, HID("هُوَ", "it", "hüve", ("الطَّرْفِ", "the eye", "göze")), Dn("وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «يَكَادُ»؛ الْقُصُورُ: الْعَجْزُ، أَيْ: تَكَادُ عُيُونُنَا تَعْجِزُ عَنْ ضَبْطِ حُسْنِهِ وَاسْتِقْصَاءِ مَحَاسِنِ خَلْقِهِ", "the clause is the predicate of يَكَادُ, in the seat of nasb; القُصُور: falling short — our eyes almost fail to take in his beauty and to search out all the fine points of his build", "cümle «يَكَادُ»nün haberi olarak mahallen mansûb; القُصُور: âciz kalmak — gözlerimiz onun güzelliğini kavramaktan, yapısının bütün güzelliklerini araştırmaktan neredeyse âciz kalır"))),
 W("دُونَهُ", "duna", "noun", ["maful-fih", "idafa-definiteness"], J(("ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ", "An adverb of place, in nasb by the fatha", "Mekân zarfı, fetha ile mansûb"), IDF("هُ"), Dn("مُتَعَلِّقٌ بِـ«يَقْصُرُ»", "it hangs on «fails»", "«يَقْصُرُ»ya müteallik")), HEMI, [("دُونَ", "duna", "noun"), P("هُ")]),
 T("مَتَى", "mata", "part", ["al-majzum-wal-shart-wal-jaza", "maful-fih"], "اسْمُ شَرْطٍ جَازِمٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ، مُتَعَلِّقٌ بِفِعْلِ الشَّرْطِ «تَرَقَّ»؛ وَ«مَتَى» وَمَا بَعْدَهَا كَلَامٌ مُسْتَأْنَفٌ لَا مَحَلَّ لَهُ.", "A conditional noun that puts two verbs in jazm, built on sukun in the seat of nasb as an adverb of time; it hangs on the verb of the condition, «climbs»; مَتَى with what follows it is a fresh sentence and has no seat.", "Câzim şart ismi; sükûn üzere mebnî, zaman zarfı olarak mahallen mansûb; şart fiili «تَرَقَّ»ya müteallik; «مَتَى» ve sonrası müste'nef bir sözdür, mahalli yoktur."),
 T("مَا", "ma-zaida", "part", ["anwa-ma"], MA_Z[0], MA_Z[1], MA_Z[2]),
 T("تَرَقَّ", "taraqqa", "verb", ["al-majzum-wal-shart-wal-jaza", "form-v-verbs", "naqis-verbs", "tibaq"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِعْلُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ، وَالْفَتْحَةُ قَبْلَهُ دَلِيلٌ عَلَيْهِ، وَأَصْلُهُ «تَتَرَقَّ» حُذِفَتْ إِحْدَى تَاءَيْهِ تَخْفِيفًا — التَّرَقِّي وَالِارْتِقَاءُ وَالرُّقِيُّ وَاحِدٌ؛ يُطَابِقُ «تَسَفَّلِ».",
   "A present verb in jazm as the verb of the condition, its sign the dropping of the weak letter, to which the fatha before it points; it stands for «تَتَرَقَّ», one of the two ta's dropped for lightness — التَّرَقِّي, الاِرْتِقَاء and الرُّقِيّ are one: climbing; the contrary of «comes down».",
   "Şart fiili olarak meczûm muzâri; cezm alâmeti illet harfinin hazfidir, önceki fetha ona delâlet eder; aslı «تَتَرَقَّ»dır, iki tâ'dan biri hafiflik için düşmüştür — التَّرَقِّي, الاِرْتِقَاء ve الرُّقِيّ birdir: yükselmek; «تَسَفَّلِ»in zıddı."),
 W("الْعَيْنُ", "ayn-eye", "noun", ["fail"], J(FAILR)),
 PJ("فِيهِ", "فِي", "fi", "هِ", ("فِي", "فِي", "فِي"), "تَرَقَّ", "climbs", "ya", extra=("؛ وَالضَّمِيرُ لِلْفَرَسِ", "; the pronoun is the horse", "; zamir ata döner")),
 T("تَسَفَّلِ", "tasaffala", "verb", ["al-majzum-wal-shart-wal-jaza", "form-v-verbs", "tibaq", "al-qafiya"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ جَوَابُ الشَّرْطِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ" + KASR_Q[0] + "، وَأَصْلُهُ «تَتَسَفَّلْ»، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْعَيْنِ — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ لَا مَحَلَّ لَهَا. أَيْ: مَتَى مَا تَرَقَّتِ الْعَيْنُ فِي أَعَالِي خَلْقِهِ نَظَرَتْ إِلَى قَوَائِمِهِ: مَهْمَا نَظَرَتْ إِلَى أَعَالِيهِ اشْتَهَتِ النَّظَرَ إِلَى أَسَافِلِهِ؛ وَيُرْوَى «تَسَهَّلِ»." + HD[0] + "طِبَاقٌ بَيْنَ الْفِعْلَيْنِ «تَرَقَّ» وَ«تَسَفَّلِ»: الصُّعُودُ وَالنُّزُولُ.",
   "A present verb in jazm as the answer of the condition, its sign the sukun" + KASR_Q[1] + "; it stands for «تَتَسَفَّلْ»; its doer is a hidden pronoun returning to the eye — the clause is the answer of the condition and has no seat. That is: whenever the eye climbs to the upper parts of his build it looks down again to his legs — however much it looks at his upper parts it longs to look at the lower (al-Zawzanī). It is also transmitted «تَسَهَّلِ»." + HD[1] + "the two verbs «تَرَقَّ» and «تَسَفَّلِ» make a tibaq: going up against coming down.",
   "Şartın cevabı olarak meczûm muzâri, cezm alâmeti sükûn" + KASR_Q[2] + "; aslı «تَتَسَفَّلْ»dir; fâili göze dönen gizli zamir — cümle şartın cevabıdır, mahalli yoktur. Yani göz ne zaman onun yapısının üst kısımlarına çıksa yine bacaklarına bakar: üst kısımlarına ne kadar baksa alt kısımlarına bakmayı arzular (Zevzenî). «تَسَهَّلِ» de rivayet edilir." + HD[2] + "«تَرَقَّ» ile «تَسَفَّلِ» fiilleri arasında tıbâk vardır: çıkmak ile inmek.", "."),
])
V(None, 69, "He passed the night with his saddle and his bridle on him; he passed it standing before my eyes, not turned loose.",
  "Geceyi, eyeri ve gemi üzerinde geçirdi; gözümün önünde ayakta, salıverilmeden geceledi.", [
 W("فَبَاتَ", "bata", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], J(PRE("fa", "بَاتَ"), ("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَرَسِ", "a defective past verb built on fatha; its noun is a hidden pronoun returning to the horse", "fetha üzere mebnî nâkıs mâzî; ismi ata dönen gizli zamir")), s=[FA, ("بَاتَ", "bata", "verb")]),
 T("عَلَيْهِ", "ala", "prep", ["huruf-jarr", "mubtada-khabar", "taqdim-al-musnad"], "عَلَى حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.", "عَلَى is a jarr letter and the هِ is in the seat of jarr — the phrase hangs on an omitted predicate, set first.", "عَلَى cer harfi, «hî» mahallen mecrûr — câr-mecrûr öne geçmiş mahzûf habere müteallik.", s=[("عَلَيْ", "ala", "prep"), P("هِ")]),
 W("سَرْجُهُ", "sarj", "noun", ["mubtada-khabar", "idafa-definiteness", "kana-wa-akhawatuha"], J(("مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ", "The mubtada, placed last, in raf' by the damma", "Sona bırakılmış mübteda, damme ile merfû"), IDF("هُ"), Dn("وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «بَاتَ»؛ وَيَجُوزُ أَنْ يَكُونَ «سَرْجُهُ» اسْمَ «بَاتَ» مُؤَخَّرًا وَالْجَارُّ وَالْمَجْرُورُ خَبَرَهُ", "the nominal clause is the predicate of بَاتَ, in the seat of nasb; or «his saddle» is itself the noun of بَاتَ, placed last, and the jarr phrase its predicate", "isim cümlesi «بَاتَ»nin haberi olarak mahallen mansûb; «سَرْجُهُ»nün «بَاتَ»nin sona kalmış ismi, câr-mecrûrun da haberi olması câizdir")), s=[("سَرْجُ", "sarj", "noun"), P("هُ")]),
 W("وَلِجَامُهُ", "lijam", "noun", ["atf-nasaq", "idafa-definiteness"], J(PRE("wa", "لِجَامُ"), ATF("سَرْجُهُ", "his saddle", "raf"), IDF("هُ")), HEMI, [WA, ("لِجَامُ", "lijam", "noun"), P("هُ")]),
 W("وَبَاتَ", "bata", "verb", ["atf-nasaq", "kana-wa-akhawatuha", "hollow-verbs"], J(PRE("wa", "بَاتَ"), ("فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْفَرَسِ", "a defective past verb built on fatha; its noun is a hidden pronoun returning to the horse", "fetha üzere mebnî nâkıs mâzî; ismi ata dönen gizli zamir"), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الَّتِي قَبْلَهَا", "the clause is conjoined to the one before", "cümle öncekine ma'tûf")), s=[WA, ("بَاتَ", "bata", "verb")]),
 T("بِعَيْنِي", "ayn-eye", "noun", ["huruf-jarr", "idafa-definiteness", "ya-al-mutakallim", "kana-wa-akhawatuha"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَعَيْنِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ «بَاتَ»، أَيْ: بَيْنَ يَدَيَّ بِحَيْثُ أَرَاهُ.",
   "The ba is a jarr letter; عَيْنِ is in jarr by a kasra estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term — the phrase hangs on the omitted predicate of بَاتَ: before me, where I could see him.",
   "Bâ cer harfi; عَيْنِ mütekellim yâsından önceki harf üzerinde takdîrî kesre ile mecrûr (mahal, münasebet harekesiyle meşguldür); muzâf, yâ muzâfun ileyh — câr-mecrûr «بَاتَ»nin mahzûf haberine müteallik: önümde, onu görebileceğim yerde.", s=[BI, ("عَيْنِ", "ayn-eye", "noun"), P("ي")]),
 W("قَائِمًا", "qaim", "noun", ["hal", "ism-fail"], J(("حَالٌ مِنَ اسْمِ «بَاتَ» مَنْصُوبٌ بِالْفَتْحَةِ", "A hal of the noun of بَاتَ, in nasb by the fatha", "«بَاتَ»nin isminden hâl, fetha ile mansûb"), Dn("وَيَجُوزُ أَنْ يَكُونَ خَبَرَ «بَاتَ» وَ«بِعَيْنِي» مُتَعَلِّقٌ بِهِ", "or it is the predicate of بَاتَ, with «before my eyes» hanging on it", "«بَاتَ»nin haberi olması, «بِعَيْنِي»nin de ona bağlanması câizdir"))),
 W("غَيْرَ", "ghayr", "noun", ["hal", "idafa-definiteness"], J(("حَالٌ ثَانِيَةٌ مَنْصُوبَةٌ بِالْفَتْحَةِ", "A second hal, in nasb by the fatha", "İkinci hâl, fetha ile mansûb"), MUD)),
 W("مُرْسَلِ", "mursal", "noun", ["idafa-definiteness", "ism-maful", "al-qafiya"], J(MI, QAFIYA, Dn("أَيْ: غَيْرَ مُرْسَلٍ إِلَى الْمَرْعَى، بَلْ بَاتَ مُسْرَجًا مُلْجَمًا", "that is, not sent out to pasture: he spent the night saddled and bridled", "yani otlağa salıverilmemiş; geceyi eyerli ve gemli geçirdi")), "."),
])
# ==== INSERT 58-69 ABOVE ====
# =====================================================================================================================
# The lightning and the rain: verses 70–75
# =====================================================================================================================
V(S5, 70, "My friend, do you see a lightning — I show you its flash — like the flicker of two hands, in a heaped cloud crowned above?",
  "Ey arkadaş! Tepesi taç gibi olmuş yığın yığın bir bulutta, parıltısını sana gösterdiğim, iki elin kımıldayışı gibi (çakan) bir şimşek görüyor musun?", [
 T("أَصَاحِ", "sahib", "noun", ["vocative-munada", "hadhf-wa-taqdir"],
   "الْهَمْزَةُ حَرْفُ نِدَاءٍ لِلْقَرِيبِ، وَصَاحِ مُنَادًى مُرَخَّمُ «صَاحِبٍ» — حُذِفَتْ بَاؤُهُ لِلتَّرْخِيمِ عَلَى غَيْرِ قِيَاسٍ لِأَنَّهُ لَيْسَ بِعَلَمٍ — مَبْنِيٌّ عَلَى الضَّمِّ عَلَى الْحَرْفِ الْمَحْذُوفِ فِي مَحَلِّ نَصْبٍ، عَلَى لُغَةِ مَنْ يَنْتَظِرُ. وَبِهِ يَأْخُذُ فِي وَصْفِ الْبَرْقِ وَالْمَطَرِ بَعْدَ فَرَاغِهِ مِنْ وَصْفِ الْفَرَسِ.",
   "The hamza is the vocative particle for one who is near; صَاحِ is a vocative, صَاحِب cut short (tarkhīm) — its ba dropped, against the rule, since it is no proper name — built on a damma on the dropped letter, in the seat of nasb, in the usage of those who keep the dropped letter in mind. With it he turns from the horse to describe the lightning and the rain.",
   "Hemze, yakın için nidâ harfi; صَاحِ, «صَاحِب»in terhîm edilmiş münâdâsıdır — alem olmadığı için kıyasa aykırı olarak bâ'sı düşmüştür — mahzûf harf üzerinde damme üzere mebnî, mahallen mansûb (düşen harfi bekleyenlerin lügatine göre). Bununla, atı anlatmayı bitirip şimşeği ve yağmuru anlatmaya başlar.", s=[("أَ", "hamza-nida", "part"), ("صَاحِ", "sahib", "noun")]),
 T("تَرَى", "raa", "verb", ["mudari-marfu", "naqis-verbs", "al-istifham", "hadhf-wa-taqdir"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَقَبْلَهُ هَمْزَةُ اسْتِفْهَامٍ مُقَدَّرَةٌ، أَيْ: أَتَرَى.",
   "A present verb in raf' by a damma estimated on the alif; its doer is the hidden «you» — a hamza of question is understood before it: «do you see…?».",
   "Elif üzerinde takdîrî damme ile merfû muzâri; fâili vücûben gizli «ente» — öncesinde mukadder bir istifham hemzesi vardır: «görüyor musun?»."),
 T("بَرْقًا", "barq", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The direct object, in nasb by the fatha.", "Mef'ûlün bih, fetha ile mansûb."),
 T("أُرِيكَ", "ara", "verb", ["mudari-marfu", "form-iv-verbs", "naqis-verbs", "mafulayn", "jumla-sifa"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«بَرْقًا».",
   "A present verb in raf' by a damma estimated on the ya (too heavy to voice); its doer is the hidden «I», and the kaf is the first object, in the seat of nasb — the clause qualifies «a lightning», in the seat of nasb.",
   "Yâ üzerinde ağırlık sebebiyle takdîrî damme ile merfû muzâri; fâili vücûben gizli «ene», kâf birinci mef'ûl, mahallen mansûb — cümle «بَرْقًا»nın na'tı olarak mahallen mansûb.", s=[("أُرِي", "ara", "verb"), P("كَ")]),
 T("وَمِيضَهُ", "wamid", "noun", ["mafulayn", "idafa-definiteness"],
   "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — الْوَمِيضُ: اللَّمَعَانُ.",
   "The second object, in nasb by the fatha, annexed; the هُ is its second term — الوَمِيض: flashing.",
   "İkinci mef'ûl, fetha ile mansûb, muzâf; «hû» muzâfun ileyh — الوَمِيض: parıltı, çakış.", HEMI, [("وَمِيضَ", "wamid", "noun"), P("هُ")]),
 T("كَلَمْعِ", "lam-shine", "noun", ["huruf-jarr", "idafa-definiteness", "masdar", "imal-al-masdar", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "الْكَافُ حَرْفُ جَرٍّ وَتَشْبِيهٍ، وَلَمْعِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِمَصْدَرٍ مَحْذُوفٍ، وَيَجُوزُ تَعْلِيقُهُمَا بِمَحْذُوفٍ حَالٍ مِنْ «وَمِيضَهُ». وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ وَمِيضُ الْبَرْقِ، وَالْمُشَبَّهُ بِهِ لَمْعُ الْيَدَيْنِ أَيْ تَحْرِيكُهُمَا، وَالْأَدَاةُ الْكَافُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ سُرْعَةُ التَّحَرُّكِ.",
   "The kaf is a jarr letter of likening; لَمْعِ is in jarr by the kasra, annexed — the phrase hangs on an omitted adjective of an omitted masdar, or on an omitted hal of «its flash». A tashbih mursal mujmal: the thing likened is the lightning's flash, the thing it is likened to is the «lamʿ» of two hands — their quick movement — the particle is the kaf, and the point of likeness, swift motion, is left unsaid (al-Zawzanī: it moves as they move).",
   "Kâf teşbih bildiren cer harfi; لَمْعِ kesre ile mecrûr, muzâf — câr-mecrûr, mahzûf bir masdarın mahzûf na'tına müteallik; «وَمِيضَهُ»dan mahzûf hâle bağlanması da câizdir. Teşbih-i mürsel mücmeldir: müşebbeh şimşeğin çakışı, müşebbehün bih iki elin «lem'»i, yani hızla hareket ettirilmesi; edat kâf; vech-i şebeh — hareketin hızı — mahzûftur (Zevzenî: onların kımıldayışı gibi kımıldar).", s=[KA, ("لَمْعِ", "lam-shine", "noun")]),
 T("الْيَدَيْنِ", "yad", "noun", ["idafa-definiteness", "al-muthanna", "imal-al-masdar"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ.",
   "The second term of the idafa, in jarr by the ya — a dual; the masdar is annexed to its doer.",
   "Muzâfun ileyh, tesniye olduğu için yâ ile mecrûr — masdarın fâiline izâfeti."),
 HARF_JARR("فِي", "fi"),
 T("حَبِيٍّ", "habiyy", "noun", ["huruf-jarr"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أُرِيكَ». الْحَبِيُّ: السَّحَابُ الْمُتَرَاكِمُ، سُمِّيَ بِذٰلِكَ لِأَنَّهُ حَبَا بَعْضُهُ إِلَى بَعْضٍ.",
   "In jarr by the kasra — the phrase hangs on «I show you». الحَبِيّ: cloud heaped on cloud, so called because part of it crawls up to part.",
   "Kesre ile mecrûr — câr-mecrûr «أُرِيكَ»ye müteallik. الحَبِيّ: yığın yığın bulut; bir kısmı ötekine doğru emeklercesine yığıldığı için bu adı almıştır."),
 T("مُكَلَّلِ", "mukallal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
   "نَعْتٌ لِـ«حَبِيٍّ» مَجْرُورٌ بِالْكَسْرَةِ" + QAFIYA[0] + " — اسْمُ مَفْعُولٍ مِنْ «كَلَّلَ»: جَعَلَهُ مُكَلَّلًا لِأَنَّ أَعْلَاهُ صَارَ كَالْإِكْلِيلِ لِأَسْفَلِهِ؛ وَيُرْوَى «مُكَلِّلِ» بِكَسْرِ اللَّامِ أَيْ: مُتَبَسِّمٍ بِالْبَرْقِ.",
   "An adjective of «a heaped cloud», in jarr by the kasra" + QAFIYA[1] + " — the ism maf'ul of كَلَّلَ «to crown»: its top has become like a crown to what is beneath it. It is also transmitted مُكَلِّل, with a kasra on the lam: «smiling» with lightning.",
   "«حَبِيٍّ»in na'tı, kesre ile mecrûr" + QAFIYA[2] + " — «كَلَّلَ»den (taç giydirmek) ism-i mef'ûl: üstü, altına taç gibi olmuştur. Lâm'ın kesresiyle «مُكَلِّل» de rivayet edilir: şimşekle gülümseyen.", "؟"),
])
V(S5, 71, "Its gleam shines out — or it is as the lamps of a monk who has tipped the oil over the twisted wicks.",
  "Işığı parlıyor; yahut bükülmüş fitillerin üzerine yağı boca etmiş bir rahibin kandilleri gibidir.", [
 T("يُضِيءُ", "adaa-shine", "verb", ["mudari-marfu", "form-iv-verbs", "hollow-verbs", "jumla-sifa"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ آخَرُ لِـ«بَرْقًا»، وَيَجُوزُ أَنْ تَكُونَ حَالًا مِنْهُ أَوْ مُسْتَأْنَفَةً.",
   "A present verb in raf' by the damma — the clause is a further adjective of «a lightning», in the seat of nasb; it may also be a hal of it, or a fresh sentence.",
   "Damme ile merfû muzâri — cümle «بَرْقًا»nın bir başka na'tı olarak mahallen mansûb; ondan hâl ya da müste'nefe olması da câizdir."),
 T("سَنَاهُ", "sanan-light", "noun", ["fail", "ism-maqsur-manqus", "idafa-definiteness"],
   "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — السَّنَا بِالْقَصْرِ: الضَّوْءُ.",
   "The doer, in raf' by a damma estimated on the alif, annexed; the هُ is its second term — السَّنَا, with the short alif: light.",
   "Fâil, elif üzerinde takdîrî damme ile merfû, muzâf; «hû» muzâfun ileyh — kasr ile السَّنَا: ışık.", s=[("سَنَا", "sanan-light", "noun"), P("هُ")]),
 T("أَوْ", "aw", "part", ["atf-nasaq"], "حَرْفُ عَطْفٍ.", "A conjunction: «or».", "Atıf harfi: «veya»."),
 T("مَصَابِيحُ", "misbah", "noun", ["atf-nasaq", "mamnu-min-sarf", "jam-taksir", "idafa-definiteness", "tashbih", "aqsam-al-tashbih"],
   "مَعْطُوفٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — عَطْفٌ عَلَى الضَّمِيرِ الْمُسْتَتِرِ فِي مُتَعَلَّقِ «كَلَمْعِ» فِي الْبَيْتِ قَبْلَهُ؛ وَيُرْوَى بِالْجَرِّ عَطْفًا عَلَى «لَمْعِ الْيَدَيْنِ». جَمْعُ مِصْبَاحٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ. وَفِيهِ تَشْبِيهٌ ثَانٍ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ ضَوْءُ الْبَرْقِ، وَالْمُشَبَّهُ بِهِ مَصَابِيحُ رَاهِبٍ أَمَالَ السَّلِيطَ بِذُبَالِهَا، وَالْأَدَاةُ الْكَافُ الْمُتَقَدِّمَةُ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ قُوَّةُ الْإِضَاءَةِ.",
   "Conjoined, in raf' by the damma, annexed — joined to the pronoun hidden in what «like the flicker» (in the verse before) hangs on; it is also transmitted in jarr, joined to «the flicker of two hands». The plural of مِصْبَاح, on the pattern of the ultimate plural. A second tashbih mursal mujmal: the thing likened is the lightning's light, the thing it is likened to is the lamps of a monk who has poured the oil on their wicks, the particle is the kaf that went before, and the point of likeness — strength of light — is left unsaid (al-Zawzanī: its motion recalls the two hands, its light the monk's lamp).",
   "Ma'tûf, damme ile merfû, muzâf — önceki beyitteki «كَلَمْعِ»nin müteallakındaki gizli zamire atfedilmiştir; «لَمْعِ الْيَدَيْنِ»e atıfla cer ile de rivayet edilir. «مِصْبَاح»ın müntehe'l-cümû' sîgasındaki cem'i. İkinci bir teşbih-i mürsel mücmel vardır: müşebbeh şimşeğin ışığı, müşebbehün bih fitillerine yağı dökmüş rahibin kandilleri, edat önce geçen kâf; vech-i şebeh — aydınlatmanın gücü — mahzûftur (Zevzenî: hareketi iki eli, ışığı rahibin kandilini andırır)."),
 T("رَاهِبٍ", "rahib", "noun", ["idafa-definiteness"], MI[0] + ".", MI[1] + ".", MI[2] + ".", HEMI),
 T("أَمَالَ", "amala-tilt", "verb", ["form-iv-verbs", "hollow-verbs", "jumla-sifa"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى «رَاهِبٍ» — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لَهُ.",
   "A past verb built on fatha; its doer is a hidden pronoun returning to «a monk» — the clause qualifies him, in the seat of jarr.",
   "Fetha üzere mebnî mâzî; fâili «رَاهِبٍ»e dönen gizli zamir — cümle onun na'tı olarak mahallen mecrûr."),
 T("السَّلِيطَ", "salit", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — السَّلِيطُ: الزَّيْتُ.", "The direct object, in nasb by the fatha — السَّلِيط: (lamp-)oil.", "Mef'ûlün bih, fetha ile mansûb — السَّلِيط: (kandil) yağı."),
 T("بِالذُّبَالِ", "dhubal", "noun", ["huruf-jarr"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَالذُّبَالِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَمَالَ»؛ جَمْعُ ذُبَالَةٍ وَهِيَ الْفَتِيلَةُ. قَالَ الزَّوْزَنِيُّ: زَعَمَ أَكْثَرُ النَّاسِ أَنَّهُ مِنَ الْمَقْلُوبِ، وَتَقْدِيرُهُ: أَمَالَ الذُّبَالَ بِالسَّلِيطِ إِذَا صَبَّهُ عَلَيْهِ؛ وَقِيلَ: الْبَاءُ بِمَعْنَى «مَعَ».",
   "The ba is a jarr letter and الذُّبَالِ is in jarr by the kasra — the phrase hangs on «tipped»; the plural of ذُبَالَة, a wick. Al-Zawzanī: most hold that the phrase is turned about (qalb), the sense being «he bent the wicks with the oil», pouring it over them; others take the ba as «with».",
   "Bâ cer harfi, الذُّبَالِ kesre ile mecrûr — câr-mecrûr «أَمَالَ»ye müteallik; «ذُبَالَة»nin (fitil) cem'i. Zevzenî: çoğunluğa göre ifade maklûbdur; takdiri «fitilleri yağla eğdi», yani yağı üzerlerine döktü; «bâ, مَعَ anlamındadır» da denmiştir.", s=[BI, ("الذُّبَالِ", "dhubal", "noun")]),
 T("الْمُفَتَّلِ", "mufattal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
   "نَعْتٌ لِـ«الذُّبَالِ» مَجْرُورٌ بِالْكَسْرَةِ — اسْمُ مَفْعُولٍ مِنْ «فَتَّلَ»: الْمُبْرَمُ.",
   "An adjective of «the wicks», in jarr by the kasra — the ism maf'ul of فَتَّلَ: tightly twisted.",
   "«الذُّبَالِ»in na'tı, kesre ile mecrûr — «فَتَّلَ»den ism-i mef'ûl: sıkıca bükülmüş.", "."),
])
V(S5, 72, "I sat watching it, with my companions, between Ḍārij and al-ʿUdhayb — how far off was what I gazed at!",
  "Arkadaşlarımla birlikte Dâric ile Uzeyb arasında onu gözlemek için oturdum; seyrettiğim şey ne kadar da uzaktı!", [
 T("قَعَدْتُ", "qaada", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَالْجُمْلَةُ مُسْتَأْنَفَةٌ.",
   "A past verb built on sukun because the doer's ta is attached; the ta is the doer, in the seat of raf' — a fresh sentence.",
   "Fâil tâsına bitiştiği için sükûn üzere mebnî mâzî; tâ fâil, mahallen merfû — cümle müste'nefedir."),
 T("لَهُ", "li", "prep", ["huruf-jarr"],
   "اللَّامُ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى الْبَرْقِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«قَعَدْتُ»، أَيْ: لِلنَّظَرِ إِلَيْهِ.",
   "The lam is a jarr letter and the هُ is in the seat of jarr, returning to the lightning — the phrase hangs on «I sat»: to watch it.",
   "Lâm cer harfi, «hû» mahallen mecrûr, şimşeğe döner — câr-mecrûr «قَعَدْتُ»ye müteallik: ona bakmak için.", s=[("لَ", "li", "prep"), P("هُ")]),
 T("وَصُحْبَتِي", "suhba", "noun", ["maful-maah", "anwa-al-waw", "idafa-definiteness", "ya-al-mutakallim"],
   "الْوَاوُ وَاوُ الْمَعِيَّةِ، وَصُحْبَتِي مَفْعُولٌ مَعَهُ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَيَجُوزُ أَنْ تَكُونَ الْوَاوُ لِلْحَالِ وَ«صُحْبَتِي» مُبْتَدَأً خَبَرُهُ الظَّرْفُ. الصُّحْبَةُ هُنَا: الْأَصْحَابُ.",
   "The waw is the waw of accompaniment; صُحْبَتِي is a mafʿūl maʿah, in nasb by a fatha estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term. The waw may also be the waw of the hal, with «my companions» a mubtada whose predicate is the adverb. الصُّحْبَة here: the companions.",
   "Vâv, vâv-ı maiyyet; صُحْبَتِي mef'ûlün maah, mütekellim yâsından önceki harf üzerinde takdîrî fetha ile mansûb; muzâf, yâ muzâfun ileyh. Vâvın hâliye, «صُحْبَتِي»nin de haberi zarf olan mübteda olması câizdir. الصُّحْبَة burada: arkadaşlar.", s=[WA, ("صُحْبَتِ", "suhba", "noun"), P("ي")]),
 T("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"],
   "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِـ«قَعَدْتُ».", "An adverb of place, in nasb by the fatha, annexed — it hangs on «I sat».", "Mekân zarfı, fetha ile mansûb, muzâf — «قَعَدْتُ»ye müteallik."),
 T("ضَارِجٍ", "darij", "propn", ["idafa-definiteness"], MI[0] + " — اسْمُ مَوْضِعٍ.", MI[1] + " — the name of a place.", MI[2] + " — bir yer adı.", HEMI),
 T("وَبَيْنَ", "bayna", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness"],
   "الْوَاوُ عَاطِفَةٌ، وَبَيْنَ مَعْطُوفٌ عَلَى «بَيْنَ» الْأَوَّلِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَأُعِيدَ تَوْكِيدًا.",
   "The waw conjoins; بَيْنَ is conjoined to the first «between», in nasb by the fatha, annexed — it is said again for emphasis.",
   "Vâv atıf; بَيْنَ ilk «بَيْنَ»ye ma'tûf, fetha ile mansûb, muzâf — tekit için tekrar edilmiştir.", s=[WA, ("بَيْنَ", "bayna", "noun")]),
 T("الْعُذَيْبِ", "udhayb", "propn", ["idafa-definiteness"], MI[0] + " — اسْمُ مَوْضِعٍ.", MI[1] + " — the name of a place.", MI[2] + " — bir yer adı."),
 T("بَعْدَ", "baada", "verb", ["thulathi-mujarrad-babs", "khabar-insha"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — قَالَ الزَّوْزَنِيُّ: أَصْلُهُ «بَعُدَ» فَخَفَّفَهُ بِتَسْكِينِ الْعَيْنِ؛ وَالْخَبَرُ يُرَادُ بِهِ التَّعَجُّبُ مِنْ بُعْدِ مَا نَظَرَ إِلَيْهِ. وَقِيلَ: هُوَ ظَرْفٌ، وَيُرْوَى «بُعْدَ» بِضَمِّ الْبَاءِ عَلَى أَنَّهُ مُنَادًى مُضَافٌ أُرِيدَ بِهِ التَّعَجُّبُ.",
   "A past verb built on fatha — al-Zawzanī: it is بَعُدَ «was far», made lighter by stilling its middle letter; the statement is meant as wonder at how far off the thing he watched was. It is also read as an adverb («after»), and it is transmitted بُعْدَ, with a damma on the ba — an annexed vocative used for wonder.",
   "Fetha üzere mebnî mâzî — Zevzenî: aslı «بَعُدَ»dir, ayn'ı sâkin kılınarak hafifletilmiştir; haberden maksat, baktığı şeyin uzaklığına taaccübdür. Zarf olduğu da söylenmiştir; bâ'nın dammesiyle «بُعْدَ» de rivayet edilir: taaccüb kastedilen muzâf münâdâ."),
 T("مَا", "ma-zaida", "part", ["anwa-ma"],
   "زَائِدَةٌ — كَذَا قَالَ الزَّوْزَنِيُّ، وَتَقْدِيرُهُ: بَعُدَ مُتَأَمَّلِي؛ وَقِيلَ: مَوْصُولَةٌ، وَالتَّقْدِيرُ: بَعُدَ مَا هُوَ مُتَأَمَّلِي.",
   "Added — so al-Zawzanī: «far was what I gazed at»; others take it as the relative مَا: «far was that which is the thing I gaze at».",
   "Zâid — Zevzenî böyle der; takdiri: «seyrettiğim şey uzak oldu»; mevsûle olduğu da söylenmiştir: «seyrettiğim şey olan o (bulut) uzak oldu»."),
 T("مُتَأَمَّلِي", "mutaammal", "noun", ["fail", "ism-maful", "idafa-definiteness", "ya-al-mutakallim", "al-qafiya"],
   "فَاعِلُ «بَعُدَ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ " + YA_MUQ + "، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — اسْمُ مَفْعُولٍ مِنْ «تَأَمَّلَ»: الْمَنْظُورُ إِلَيْهِ، وَهُوَ السَّحَابُ الَّذِي كَانَ يَشِيمُ بَرْقَهُ.",
   "The doer of «was far», in raf' by a damma estimated before the speaker's ya, whose kasra holds the place; annexed, and the ya is its second term — the ism maf'ul of تَأَمَّلَ: the thing looked at, the cloud whose lightning he was watching.",
   "«بَعُدَ»nin fâili; mütekellim yâsından önceki harf üzerinde takdîrî damme ile merfû; muzâf, yâ muzâfun ileyh — «تَأَمَّلَ»den ism-i mef'ûl: bakılan şey, yani şimşeğini gözlediği bulut.", "!", [("مُتَأَمَّلِ", "mutaammal", "noun"), P("ي")]),
])
V(S5, 73, "By my reckoning as I watched, the right of its downpour is over Qaṭan, and its left over al-Sitār and then Yadhbul.",
  "Şimşeği gözleyerek kestirdiğime göre, yağmurunun sağ yanı Katan'ın, sol yanı ise Sitâr'ın, sonra Yezbül'ün üzerindeydi.", [
 HARF_JARR("عَلَى", "ala"),
 T("قَطَنٍ", "qatan", "propn", ["huruf-jarr", "taqdim-al-musnad", "kinaya", "aqsam-al-kinaya"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ؛ قَطَنٌ: جَبَلٌ؛ وَيُرْوَى «عَلَا قَطَنًا». وَكَوْنُ أَيْمَنِ صَوْبِهِ عَلَى قَطَنٍ وَأَيْسَرِهِ عَلَى السِّتَارِ وَيَذْبُلَ — وَبَيْنَهَا مَسَافَةٌ بَعِيدَةٌ — كِنَايَةٌ عَنْ صِفَةٍ: عِظَمِ السَّحَابِ وَغَزَارَتِهِ وَعُمُومِ جَوْدِهِ.",
   "In jarr by the kasra — the jarr phrase hangs on an omitted predicate, set first; Qaṭan is a mountain; it is also transmitted عَلَا قَطَنًا («rose over Qaṭan»). That the right of its rain should be over Qaṭan and its left over al-Sitār and Yadhbul — far apart as they are — is a kinaya for a quality: the vastness of the cloud, the abundance of its rain and the reach of its bounty (al-Zawzanī).",
   "Kesre ile mecrûr — câr-mecrûr öne geçmiş mahzûf habere müteallik; Katan bir dağdır; «عَلَا قَطَنًا» (Katan'ın üstüne yükseldi) şeklinde de rivayet edilir. Yağmurunun sağının Katan, solunun — aralarında uzun mesafe bulunan — Sitâr ile Yezbül üzerinde olması bir sıfattan kinâyedir: bulutun büyüklüğü, yağmurunun bolluğu ve cömertliğinin yaygınlığı (Zevzenî)."),
 T("بِالشَّيْمِ", "shaym", "noun", ["huruf-jarr", "masdar", "hal"],
   "الْبَاءُ حَرْفُ جَرٍّ، وَالشَّيْمِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الضَّمِيرِ الْمُسْتَتِرِ فِي الْخَبَرِ. الشَّيْمُ: النَّظَرُ إِلَى الْبَرْقِ مَعَ تَرَقُّبِ الْمَطَرِ؛ أَرَادَ أَنَّهُ يَحْكُمُ بِهِ حَدْسًا وَتَقْدِيرًا لِأَنَّهُ لَا يَرَى السِّتَارَ وَيَذْبُلَ وَقَطَنًا مَعًا.",
   "The ba is a jarr letter and الشَّيْمِ is in jarr by the kasra — the phrase hangs on an omitted hal of the pronoun hidden in the predicate. الشَّيْم: watching the lightning in expectation of rain; he means that he judges by guess and estimate, for he cannot see al-Sitār, Yadhbul and Qaṭan all at once (al-Zawzanī).",
   "Bâ cer harfi, الشَّيْمِ kesre ile mecrûr — câr-mecrûr haberdeki gizli zamirden mahzûf hâle müteallik. الشَّيْم: yağmur bekleyerek şimşeğe bakmak; bununla tahmin ve takdir yoluyla hükmettiğini kastetmiştir, çünkü Sitâr'ı, Yezbül'ü ve Katan'ı birlikte göremez (Zevzenî).", s=[BI, ("الشَّيْمِ", "shaym", "noun")]),
 T("أَيْمَنُ", "ayman", "noun", ["mubtada-khabar", "idafa-definiteness", "ism-tafdil", "tibaq"],
   "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَبَيْنَهُ وَبَيْنَ «أَيْسَرُهُ» طِبَاقُ إِيجَابٍ.",
   "The mubtada, placed last, in raf' by the damma, annexed — with «its left» it makes a tibaq.",
   "Sona bırakılmış mübteda, damme ile merfû, muzâf — «أَيْسَرُهُ» ile arasında tıbâk-ı îcâb vardır."),
 T("صَوْبِهِ", "sawb", "noun", ["idafa-definiteness"],
   MI[0] + "، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى السَّحَابِ — الصَّوْبُ: الْمَطَرُ.",
   MI[1] + ", annexed in turn; the هِ is its second term and returns to the cloud — الصَّوْب: rain.",
   MI[2] + ", muzâf; «hî» muzâfun ileyh, buluta döner — الصَّوْب: yağmur.", HEMI, [("صَوْبِ", "sawb", "noun"), P("هِ")]),
 T("وَأَيْسَرُهُ", "aysar", "noun", ["atf-nasaq", "mubtada-khabar", "idafa-definiteness", "ism-tafdil", "tibaq"],
   "الْوَاوُ عَاطِفَةٌ، وَأَيْسَرُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يُطَابِقُ «أَيْمَنُ».",
   "The waw conjoins; أَيْسَرُ is a mubtada, in raf' by the damma, annexed, and the هُ is its second term — the contrary of «the right».",
   "Vâv atıf; أَيْسَرُ mübteda, damme ile merfû, muzâf; «hû» muzâfun ileyh — «أَيْمَنُ»in zıddı.", s=[WA, ("أَيْسَرُ", "aysar", "noun"), P("هُ")]),
 HARF_JARR("عَلَى", "ala"),
 T("السِّتَارِ", "sitar", "propn", ["huruf-jarr", "mubtada-khabar"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ الْمُبْتَدَإِ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الَّتِي قَبْلَهَا؛ السِّتَارُ: جَبَلٌ.",
   "In jarr by the kasra — the jarr phrase hangs on the omitted predicate of the mubtada, and the clause is conjoined to the one before it; al-Sitār is a mountain.",
   "Kesre ile mecrûr — câr-mecrûr mübtedanın mahzûf haberine müteallik; cümle öncekine ma'tûftur; Sitâr bir dağdır."),
 T("فَيَذْبُلِ", "yadhbul", "propn", ["atf-nasaq", "mamnu-min-sarf", "al-qafiya"],
   "الْفَاءُ عَاطِفَةٌ، وَيَذْبُلِ مَعْطُوفٌ عَلَى «السِّتَارِ» مَجْرُورٌ بِالْكَسْرَةِ لِضَرُورَةِ الشِّعْرِ، وَحَقُّهُ أَنْ يُجَرَّ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَوَزْنِ الْفِعْلِ — يَذْبُلُ: جَبَلٌ.",
   "The fa conjoins; يَذْبُلِ is conjoined to «al-Sitār», in jarr by the kasra as verse allows — it should take the fatha, being a diptote (a proper name on the pattern of a verb); Yadhbul is a mountain.",
   "Fâ atıf; يَذْبُلِ «السِّتَارِ»e ma'tûf, şiir zarûretiyle kesre ile mecrûr; alemiyet ve vezn-i fiil sebebiyle gayr-i munsarif olduğundan aslında fetha ile cer edilirdi — Yezbül bir dağdır.", ".", [FA, ("يَذْبُلِ", "yadhbul", "propn")]),
])
V(S5, 74, "Then it took to pouring its water round Kutayfa, flinging the great kanahbal trees down upon their chins.",
  "Derken Küteyfe'nin çevresine suyunu boşaltmaya koyuldu; ulu kenehbel ağaçlarını çeneleri üstüne (yüzüstü) deviriyordu.", [
 T("فَأَضْحَى", "adha-become", "verb", ["atf-nasaq", "kana-wa-akhawatuha", "form-iv-verbs", "naqis-verbs"],
   "الْفَاءُ عَاطِفَةٌ، وَأَضْحَى فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى السَّحَابِ الْمَفْهُومِ مِمَّا قَبْلَهُ.",
   "The fa conjoins; أَضْحَى is a defective past verb built on a fatha estimated on the alif; its noun is a hidden pronoun returning to the cloud understood from what went before.",
   "Fâ atıf; أَضْحَى elif üzerinde takdîrî fetha üzere mebnî nâkıs mâzî; ismi, öncesinden anlaşılan buluta dönen gizli zamir.", s=[FA, ("أَضْحَى", "adha-become", "verb")]),
 T("يَسُحُّ", "sahha-pour", "verb", ["mudari-marfu", "doubled-verbs", "kana-wa-akhawatuha"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى السَّحَابِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ «أَضْحَى»؛ سَحَّ الْمَاءَ: صَبَّهُ.",
   "A present verb in raf' by the damma; its doer is a hidden pronoun returning to the cloud — the clause is the predicate of أَضْحَى, in the seat of nasb; سَحَّ الْمَاءَ: to pour water out.",
   "Damme ile merfû muzâri; fâili buluta dönen gizli zamir — cümle «أَضْحَى»nın haberi olarak mahallen mansûb; سَحَّ الْمَاءَ: suyu dökmek."),
 T("الْمَاءَ", "ma-water", "noun", ["maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.", "The direct object, in nasb by the fatha.", "Mef'ûlün bih, fetha ile mansûb."),
 T("حَوْلَ", "hawla", "noun", ["maful-fih", "idafa-definiteness"],
   "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — مُتَعَلِّقٌ بِـ«يَسُحُّ».", "An adverb of place, in nasb by the fatha, annexed — it hangs on «pours».", "Mekân zarfı, fetha ile mansûb, muzâf — «يَسُحُّ»ya müteallik."),
 T("كُتَيْفَةٍ", "kutayfa", "propn", ["idafa-definiteness", "mamnu-min-sarf"],
   MI[0] + " — وَنُوِّنَ لِضَرُورَةِ الشِّعْرِ، وَحَقُّهُ الْمَنْعُ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ؛ كُتَيْفَةُ: اسْمُ مَوْضِعٍ.",
   MI[1] + " — it takes tanwin as verse allows, though as a feminine proper name it is a diptote; Kutayfa is the name of a place.",
   MI[2] + " — şiir zarûretiyle tenvinlenmiştir; alemiyet ve te'nîs sebebiyle aslında gayr-i munsariftir; Küteyfe bir yer adıdır.", HEMI),
 T("يَكُبُّ", "kabba", "verb", ["mudari-marfu", "doubled-verbs", "kana-wa-akhawatuha"],
   "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى السَّحَابِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرٌ ثَانٍ لِـ«أَضْحَى»، وَيَجُوزُ أَنْ تَكُونَ مُسْتَأْنَفَةً؛ الْكَبُّ: إِلْقَاءُ الشَّيْءِ عَلَى وَجْهِهِ.",
   "A present verb in raf' by the damma; its doer is a hidden pronoun returning to the cloud — the clause is a second predicate of أَضْحَى, in the seat of nasb, or a fresh sentence; الكَبّ: throwing a thing down on its face.",
   "Damme ile merfû muzâri; fâili buluta dönen gizli zamir — cümle «أَضْحَى»nın ikinci haberi olarak mahallen mansûb; müste'nefe olması da câizdir; الكَبّ: bir şeyi yüzüstü atmak."),
 HARF_JARR("عَلَى", "ala"),
 T("الْأَذْقَانِ", "dhaqan", "noun", ["huruf-jarr", "jam-taksir", "istiara", "arkan-al-istiara", "istiara-makniyya"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يَكُبُّ»؛ جَمْعُ ذَقَنٍ وَهُوَ مُجْتَمَعُ اللَّحْيَيْنِ. قَالَ الزَّوْزَنِيُّ: وَالْأَذْقَانُ مُسْتَعَارٌ فِي الْبَيْتِ لِلشَّجَرِ، وَقَالَ التِّبْرِيزِيُّ: يُرِيدُ بِهَا الرُّؤُوسَ وَأَعَالِيَ الشَّجَرِ — فَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ، وَيَصِحُّ إِجْرَاؤُهَا مَكْنِيَّةً: شُبِّهَ الدَّوْحُ بِقَوْمٍ يُكَبُّونَ عَلَى وُجُوهِهِمْ ثُمَّ حُذِفَ الْمُشَبَّهُ بِهِ وَرُمِزَ إِلَيْهِ بِالْأَذْقَانِ.",
   "In jarr by the kasra — the phrase hangs on «flings down»; the plural of ذَقَن, where the two jawbones meet. Al-Zawzanī: «chins» is borrowed in the verse for the trees; al-Tibrīzī: he means the heads, the tree-tops. So it is an explicit istiʿāra; it may also be read as an istiʿāra by kināya — the great trees likened to men thrown on their faces, the men dropped and hinted at by «chins».",
   "Kesre ile mecrûr — câr-mecrûr «يَكُبُّ»ye müteallik; «ذَقَن»in (iki çene kemiğinin birleştiği yer) cem'i. Zevzenî: beyitte «çeneler» ağaçlar için istiâre edilmiştir; Tebrîzî: bununla ağaçların başlarını, tepelerini kasteder. Demek ki istiâre-i tasrîhiyyedir; mekniyye olarak da yürütülebilir: ulu ağaçlar yüzüstü düşürülen insanlara benzetilmiş, müşebbehün bih hazfedilip «çeneler» ile ona işaret edilmiştir."),
 T("دَوْحَ", "dawh", "noun", ["maful-bihi", "idafa-definiteness"],
   "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — جَمْعُ دَوْحَةٍ وَهِيَ الشَّجَرَةُ الْعَظِيمَةُ.", "The direct object, in nasb by the fatha, annexed — the plural of دَوْحَة, a great tree.", "Mef'ûlün bih, fetha ile mansûb, muzâf — «دَوْحَة»nin (ulu ağaç) cem'i."),
 T("الْكَنَهْبَلِ", "kanahbal", "noun", ["idafa-definiteness", "al-qafiya"],
   MI[0] + " — ضَرْبٌ مِنْ شَجَرِ الْبَادِيَةِ، بِفَتْحِ الْبَاءِ وَضَمِّهَا.", MI[1] + " — a kind of desert tree; its ba is read with fatha or with damma.", MI[2] + " — bir çeşit çöl ağacı; bâ'sı fetha ile de damme ile de okunur.", "."),
])
V(S5, 75, "And some of its spray passed over al-Qanān, and brought the white-footed ibexes down from every haunt there.",
  "Serpintisinden bir kısmı Kanân dağının üzerinden geçti de oradaki ayağı sekili dağ keçilerini her konaklarından aşağı indirdi.", [
 T("وَمَرَّ", "marra", "verb", ["atf-nasaq", "thulathi-mujarrad-babs", "doubled-verbs", "hadhf-wa-taqdir"],
   "الْوَاوُ عَاطِفَةٌ، وَمَرَّ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَفَاعِلُهُ مَحْذُوفٌ دَلَّ عَلَيْهِ «مِنْ نَفَيَانِهِ»، وَالتَّقْدِيرُ: مَرَّ شَيْءٌ مِنْ نَفَيَانِهِ — كَذَا أَعْرَبَهُ الدُّرَّةُ؛ وَقِيلَ: ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى السَّحَابِ. وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى مَا قَبْلَهَا.",
   "The waw conjoins; مَرَّ is a past verb built on fatha. Its doer is left out, shown by «of its spray»: «something of its spray passed» — so al-Durra parses it; others make the doer a hidden pronoun returning to the cloud. The clause is conjoined to what went before.",
   "Vâv atıf; مَرَّ fetha üzere mebnî mâzî. Fâili mahzûftur, «مِنْ نَفَيَانِهِ» ona delâlet eder; takdiri: «serpintisinden bir şey geçti» — Dürre böyle i'râb eder; «fâil buluta dönen gizli zamirdir» de denmiştir. Cümle öncesine ma'tûftur.", s=[WA, ("مَرَّ", "marra", "verb")]),
 HARF_JARR("عَلَى", "ala"),
 T("الْقَنَانِ", "qanan", "propn", ["huruf-jarr"],
   "مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَرَّ»؛ الْقَنَانُ: جَبَلٌ لِبَنِي أَسَدٍ.",
   "In jarr by the kasra — the phrase hangs on «passed»; al-Qanān is a mountain of the Banū Asad.",
   "Kesre ile mecrûr — câr-mecrûr «مَرَّ»ye müteallik; Kanân, Benî Esed'e ait bir dağdır."),
 HARF_JARR("مِنْ", "min", " لِلتَّبْعِيضِ، وَجَعَلَهُ الدُّرَّةُ بَيَانًا لِلْفَاعِلِ الْمَحْذُوفِ", " — «some of»; al-Durra takes it as explaining the omitted doer", " — teb'îz («bir kısmı») içindir; Dürre onu mahzûf fâilin beyânı sayar"),
 T("نَفَيَانِهِ", "nafayan", "noun", ["huruf-jarr", "idafa-definiteness"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ يَعُودُ عَلَى الْغَيْثِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَرَّ». النَّفَيَانُ: مَا يَتَطَايَرُ مِنْ قَطْرِ الْمَطَرِ.",
   "In jarr by the kasra, annexed; the هِ is its second term and returns to the rain — the phrase hangs on «passed». النَّفَيَان: the drops that fly off from falling rain, its spray.",
   "Kesre ile mecrûr, muzâf; «hî» muzâfun ileyh, yağmura döner — câr-mecrûr «مَرَّ»ye müteallik. النَّفَيَان: yağmur damlalarından savrulan serpinti.", HEMI, [("نَفَيَانِ", "nafayan", "noun"), P("هِ")]),
 T("فَأَنْزَلَ", "anzala", "verb", ["atf-nasaq", "form-iv-verbs", "mulhaq-bil-jinas"],
   "الْفَاءُ عَاطِفَةٌ تُفِيدُ السَّبَبِيَّةَ، وَأَنْزَلَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى فَاعِلِ «مَرَّ» — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى الَّتِي قَبْلَهَا. وَبَيْنَهُ وَبَيْنَ «مَنْزِلِ» مَا يُلْحَقُ بِالْجِنَاسِ، لِأَنَّهُمَا يَجْمَعُهُمَا الِاشْتِقَاقُ مِنَ النُّزُولِ.",
   "The fa conjoins, with the sense of cause; أَنْزَلَ is a past verb built on fatha, its hidden doer the same as that of «passed» — the clause is conjoined to the one before it. Between it and «haunt» (مَنْزِل) there is what is joined to the jinās: the two words are bound by derivation from one root, «coming down».",
   "Fâ sebebiyet bildiren atıf; أَنْزَلَ fetha üzere mebnî mâzî, fâili «مَرَّ»nin fâiline dönen gizli zamir — cümle öncekine ma'tûftur. «مَنْزِلِ» ile arasında cinâsa mülhak olan iştikak vardır: iki kelimeyi «nüzûl» kökünden türeme birleştirir.", s=[FA, ("أَنْزَلَ", "anzala", "verb")]),
 T("مِنْهُ", "min", "prep", ["huruf-jarr"],
   "مِنْ حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ يَعُودُ عَلَى الْقَنَانِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَنْزَلَ».",
   "مِنْ is a jarr letter and the هُ is in the seat of jarr, returning to al-Qanān — the phrase hangs on «brought down».",
   "مِنْ cer harfi, «hû» mahallen mecrûr, Kanân'a döner — câr-mecrûr «أَنْزَلَ»ye müteallik.", s=[("مِنْ", "min", "prep"), P("هُ")]),
 T("الْعُصْمَ", "asam", "noun", ["maful-bihi", "jam-taksir", "hadhf-wa-taqdir"],
   "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ أَعْصَمَ، وَهُوَ مِنَ الْأَوْعَالِ مَا فِي إِحْدَى يَدَيْهِ بَيَاضٌ؛ نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيِ: الْأَوْعَالَ الْعُصْمَ.",
   "The direct object, in nasb by the fatha — the plural of أَعْصَم, the ibex with white on one foreleg; it describes a noun left out: «the white-footed ibexes».",
   "Mef'ûlün bih, fetha ile mansûb — «أَعْصَم»in cem'i: ön ayaklarından birinde aklık bulunan dağ keçisi; mahzûf mevsûfun na'tıdır: «sekili dağ keçilerini»."),
 HARF_JARR("مِنْ", "min"),
 T("كُلِّ", "kull", "noun", ["huruf-jarr", "idafa-definiteness"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَنْزَلَ».", "In jarr by the kasra, annexed — the phrase hangs on «brought down».", "Kesre ile mecrûr, muzâf — câr-mecrûr «أَنْزَلَ»ye müteallik."),
 T("مَنْزِلِ", "manzil", "noun", ["idafa-definiteness", "mulhaq-bil-jinas", "al-qafiya"],
   MI[0] + QAFIYA[0] + " — أَيْ: مِنْ كُلِّ مَوْضِعٍ مِنْ هٰذَا الْجَبَلِ؛ وَيُلَاقِي «أَنْزَلَ» فِي الِاشْتِقَاقِ.",
   MI[1] + QAFIYA[1] + " — that is, from every place on that mountain; it meets «brought down» in derivation.",
   MI[2] + QAFIYA[2] + " — yani o dağın her yerinden; iştikakta «أَنْزَلَ» ile buluşur.", "."),
])


# =====================================================================================================================
# The flood: verses 76–81, the close of the poem
# =====================================================================================================================
ZARF_K = lambda en, tr: ("ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُتَعَلِّقٌ بِمَا فِي «كَأَنَّ» مِنْ مَعْنَى الْفِعْلِ", "An adverb of time, in nasb by the fatha; it hangs on the verbal sense in كَأَنَّ", "Zaman zarfı, fetha ile mansûb; «كَأَنَّ»deki fiil mânâsına müteallik")
V(None, 76, "And at Taymāʾ it left not a palm-trunk standing, nor any tower but one built up with stone.",
  "Teymâ'da ise ne bir hurma kütüğü bıraktı ne de taşla yükseltilmiş olandan başka bir köşk.", [
 T("وَتَيْمَاءَ", "tayma", "propn", ["atf-nasaq", "mamnu-min-sarf", "ism-mamdud"],
   "الْوَاوُ عَاطِفَةٌ، وَتَيْمَاءَ مَعْطُوفٌ عَلَى «الْقَنَانِ» فِي الْبَيْتِ قَبْلَهُ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ وَاخْتَارَ الدُّرَّةُ نَصْبَهُ بِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ «لَمْ يَتْرُكْ». تَيْمَاءُ: قَرْيَةٌ عَادِيَّةٌ فِي بِلَادِ الْعَرَبِ.",
   "The waw conjoins; تَيْمَاءَ is conjoined to «al-Qanān» in the verse before, in jarr by the fatha in place of the kasra — a diptote, for its long feminine alif. Al-Durra prefers to read it in nasb, by an omitted verb that «it left not» explains. Taymāʾ: an ancient town in the land of the Arabs.",
   "Vâv atıf; تَيْمَاءَ önceki beyitteki «الْقَنَانِ»a ma'tûf; elif-i memdûde ile müennes olduğu için gayr-i munsarif, kesre yerine fetha ile mecrûr. Dürre, «لَمْ يَتْرُكْ»ün tefsir ettiği mahzûf bir fiille mansûb olmasını tercih eder. Teymâ: Arap diyarında çok eski bir kasaba.", s=[WA, ("تَيْمَاءَ", "tayma", "propn")]),
 T("لَمْ", "lam-jazima", "part", ["lam-jazim"], LAM_J[0], LAM_J[1], LAM_J[2]),
 T("يَتْرُكْ", "taraka", "verb", ["lam-jazim", "thulathi-mujarrad-babs", "hal"],
   "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْغَيْثِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ «تَيْمَاءَ». قَالَ الزَّوْزَنِيُّ: يَعْنِي أَنَّهُ قَلَعَ الْأَشْجَارَ وَهَدَمَ الْأَبْنِيَةَ إِلَّا مَا كَانَ مِنْهَا مَرْفُوعًا بِالْحِجَارَةِ وَالْجِصِّ.",
   "A present verb in jazm by لَمْ, its sign the sukun; its doer is a hidden pronoun returning to the rain — the clause is a hal of «Taymāʾ», in the seat of nasb. Al-Zawzanī: he means that it tore up the trees and threw down the buildings, all but those raised with stone and plaster.",
   "لَمْ ile meczûm muzâri, cezm alâmeti sükûn; fâili yağmura dönen gizli zamir — cümle «تَيْمَاءَ»dan hâl olarak mahallen mansûb. Zevzenî: ağaçları söktüğünü, taş ve kireçle yükseltilmiş olanlar dışında binaları yıktığını kasteder."),
 PJ("بِهَا", "بِ", "bi", "هَا", BA3, "يَتْرُكْ", "left", "e", extra=("؛ وَالْبَاءُ بِمَعْنَى «فِي»", "; the ba means «in»", "; bâ «-de» anlamındadır")),
 W("جِذْعَ", "jidh", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, MUD)),
 W("نَخْلَةٍ", "nakhla", "noun", ["idafa-definiteness"], J(MI), HEMI),
 T("وَلَا", "la-nafiya", "part", ["atf-nasaq", "la-nafiya"], "الْوَاوُ عَاطِفَةٌ، وَلَا زَائِدَةٌ لِتَوْكِيدِ النَّفْيِ.", "The waw conjoins; لَا is added to strengthen the negation.", "Vâv atıf; lâ, nefyi pekiştirmek için zâiddir.", s=[WA, ("لَا", "la-nafiya", "part")]),
 W("أُطُمًا", "utum", "noun", ["atf-nasaq"], J(("مَعْطُوفٌ عَلَى «جِذْعَ» مَنْصُوبٌ بِالْفَتْحَةِ", "Conjoined to «a trunk», in nasb by the fatha", "«جِذْعَ»a ma'tûf, fetha ile mansûb"), Dn("الْأُطُمُ: الْقَصْرُ، وَالْجَمْعُ الْآطَامُ؛ وَيُرْوَى «أُجُمًا» وَهُوَ بِمَعْنَاهُ", "الأُطُم: a tower, a strong house; plural الآطَام; it is also transmitted «أُجُمًا», of the same sense", "الأُطُم: köşk, müstahkem yapı; cem'i الآطَام; aynı anlamda «أُجُمًا» da rivayet edilir"))),
 T("إِلَّا", "illa", "part", ["istithna-mufarragh", "qasr", "turuq-al-qasr"],
   "أَدَاةُ حَصْرٍ. وَفِيهِ — عَلَى حَدِّ التَّلْخِيصِ — قَصْرٌ طَرِيقُهُ النَّفْيُ وَالِاسْتِثْنَاءُ: قَصَرَ مَا تَرَكَهُ السَّيْلُ مِنَ الْآطَامِ عَلَى الْمَشِيدِ بِالْجَنْدَلِ.",
   "The particle of restriction. By the Talkhīṣ's definition, there is a qaṣr by negation and exception: of the towers, what the flood left is confined to those built with stone.",
   "Hasr edatı. Telhîs'in tarifine göre nefy ve istisnâ yoluyla kasr vardır: selin köşklerden bıraktığı, taşla yapılmış olana hasredilmiştir."),
 W("مَشِيدًا", "mashid", "noun", ["mafulayn", "ism-maful"], J(("مَفْعُولٌ بِهِ ثَانٍ لِـ«يَتْرُكْ» مَنْصُوبٌ بِالْفَتْحَةِ، وَقِيلَ: حَالٌ مِنَ الْأُطُمِ", "A second object of «left», in nasb by the fatha; it is also read as a hal of the tower", "«يَتْرُكْ»ün ikinci mef'ûlü, fetha ile mansûb; köşkten hâl olduğu da söylenmiştir"), Dn("اسْمُ مَفْعُولٍ مِنْ «شَادَ يَشِيدُ»؛ الشِّيدُ: الْجِصُّ، وَالشَّيْدُ: الرَّفْعُ وَعُلُوُّ الْبُنْيَانِ", "the ism maf'ul of شَادَ يَشِيدُ; الشِّيد: plaster; الشَّيْد: raising a building high", "«شَادَ يَشِيدُ»den ism-i mef'ûl; الشِّيد: kireç; الشَّيْد: binayı yükseltmek"))),
 T("بِجَنْدَلِ", "jandal", "noun", ["huruf-jarr", "al-qafiya"], "الْبَاءُ حَرْفُ جَرٍّ، وَجَنْدَلِ مَجْرُورٌ بِالْكَسْرَةِ" + QAFIYA[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«مَشِيدًا»؛ الْجَنْدَلُ: الصَّخْرُ، وَالْجَمْعُ الْجَنَادِلُ.", "The ba is a jarr letter and جَنْدَلِ is in jarr by the kasra" + QAFIYA[1] + " — the phrase hangs on «built up»; الجَنْدَل: rock; plural الجَنَادِل.", "Bâ cer harfi, جَنْدَلِ kesre ile mecrûr" + QAFIYA[2] + " — câr-mecrûr «مَشِيدًا»ya müteallik; الجَنْدَل: kaya; cem'i الجَنَادِل.", ".", [BI, ("جَنْدَلِ", "jandal", "noun")]),
])
V(None, 77, "Mount Thabīr, in the first onrush of its downpour, was like a chief among men wrapped in a striped cloak.",
  "Sebîr dağı, sağanağının ilk boşanışında, çizgili bir abaya bürünmüş bir kavim büyüğü gibiydi.", [
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + ". وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ ثَبِيرٌ وَقَدْ غَطَّاهُ الْغُثَاءُ، وَالْمُشَبَّهُ بِهِ سَيِّدُ أُنَاسٍ قَدْ تَلَفَّفَ بِكِسَاءٍ مُخَطَّطٍ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ: شَبَّهَ تَغْطِيَتَهُ بِالْغُثَاءِ بِتَغَطِّي هٰذَا الرَّجُلِ بِالْكِسَاءِ.",
   KAANNA_T[1] + ". A tashbih mursal mujmal: the thing likened is Thabīr, covered with the flood's wrack; the thing it is likened to is a chief of men wrapped in a striped cloak; the particle is كَأَنَّ, and the point of likeness is left unsaid — its covering of wrack is likened to that man's covering of cloak (al-Zawzanī).",
   KAANNA_T[2] + ". Teşbih-i mürsel mücmeldir: müşebbeh, sel köpüğü ve çerçöple örtülmüş Sebîr; müşebbehün bih, çizgili abaya sarınmış bir kavim büyüğü; edat كَأَنَّ; vech-i şebeh mahzûftur: dağın çerçöple örtülmesi o adamın abayla örtünmesine benzetilmiştir (Zevzenî)."),
 W("ثَبِيرًا", "thabir", "propn", ["inna-wa-akhawatuha"], J(ISM_KAANNA, Dn("ثَبِيرٌ: جَبَلٌ بِعَيْنِهِ", "Thabīr is a particular mountain", "Sebîr belirli bir dağdır"))),
 HARF_JARR("فِي", "fi"),
 T("عَرَانِينِ", "irnin", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", "hal", "istiara", "arkan-al-istiara"],
   "مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «ثَبِيرًا». الْعِرْنِينُ: الْأَنْفُ، وَقَالَ جُمْهُورُ الْأَئِمَّةِ: هُوَ مُعْظَمُ الْأَنْفِ. قَالَ الزَّوْزَنِيُّ: اسْتَعَارَ الْعَرَانِينَ لِأَوَائِلِ الْمَطَرِ لِأَنَّ الْأُنُوفَ تَتَقَدَّمُ الْوُجُوهَ — فَهِيَ اسْتِعَارَةٌ تَصْرِيحِيَّةٌ.",
   "In jarr by the kasra, annexed — the phrase hangs on an omitted hal of «Thabīr». العِرْنِين: the nose — most of the masters say, the bulk of the nose. Al-Zawzanī: he borrows «noses» for the first of the rain, because the nose goes before the face. So it is an explicit istiʿāra.",
   "Kesre ile mecrûr, muzâf — câr-mecrûr «ثَبِيرًا»dan mahzûf hâle müteallik. العِرْنِين: burun; imamların çoğuna göre burnun büyük kısmı. Zevzenî: «burunları» yağmurun ilk boşananları için istiâre etmiştir, çünkü burun yüzün önünde gider. Demek ki istiâre-i tasrîhiyyedir."),
 W("وَبْلِهِ", "wabl", "noun", ["idafa-definiteness"], J(MI, IDF("هِ"), Dn("الْوَبْلُ: جَمْعُ وَابِلٍ، وَهُوَ الْمَطَرُ الْغَزِيرُ الْعَظِيمُ الْقَطْرِ، وَهُوَ أَيْضًا مَصْدَرٌ", "الوَبْل: the plural of وَابِل, heavy rain in big drops; it is also a masdar", "الوَبْل: «وَابِل»in (iri taneli, bol yağmur) cem'i; masdar olarak da kullanılır")), HEMI, [("وَبْلِ", "wabl", "noun"), P("هِ")]),
 W("كَبِيرُ", "kabir", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], J(KHB_KAANNA, MUD, Dn("أَيْ: سَيِّدُ أُنَاسٍ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "that is, the chief of a people; the sentence is a fresh one", "yani bir topluluğun efendisi; cümle müste'nefedir"))),
 W("أُنَاسٍ", "unas", "noun", ["idafa-definiteness"], J(MI)),
 HARF_JARR("فِي", "fi"),
 W("بِجَادٍ", "bijad", "noun", ["huruf-jarr"], J(MAJR, TA("مُزَمَّلِ", "wrapped", "e"), Dn("الْبِجَادُ: كِسَاءٌ مُخَطَّطٌ، وَالْجَمْعُ الْبُجُدُ", "البِجَاد: a striped cloak; plural البُجُد", "البِجَاد: çizgili aba; cem'i البُجُد"))),
 T("مُزَمَّلِ", "muzammal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"],
   "نَعْتٌ لِـ«كَبِيرُ» مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْجِوَارِ. قَالَ الزَّوْزَنِيُّ: وَجَرَّ «مُزَمَّلًا» عَلَى جِوَارِ «بِجَادٍ»، وَإِلَّا فَالْقِيَاسُ يَقْتَضِي رَفْعَهُ لِأَنَّهُ وَصْفُ «كَبِيرُ أُنَاسٍ»، وَمِثْلُهُ قَوْلُهُمْ: جُحْرُ ضَبٍّ خَرِبٍ. التَّزْمِيلُ: التَّلْفِيفُ بِالثِّيَابِ.",
   "An adjective of «a chief», in raf' by a damma that the vowel of neighbourhood keeps from showing. Al-Zawzanī: he puts «wrapped» in jarr because it stands next to «a cloak»; by rule it should be in raf', since it describes «a chief of men» — like the Arabs' saying جُحْرُ ضَبٍّ خَرِبٍ. التَّزْمِيل: wrapping in garments.",
   "«كَبِيرُ»ün na'tı; civâr harekesi mahalli meşgul ettiği için takdîrî damme ile merfû. Zevzenî: «مُزَمَّل»i «بِجَادٍ»e komşuluğu sebebiyle cer etmiştir; yoksa kıyas ref'ini gerektirir, çünkü «كَبِيرُ أُنَاسٍ»in vasfıdır; Arapların «جُحْرُ ضَبٍّ خَرِبٍ» sözü de böyledir. التَّزْمِيل: elbiseye sarıp sarmalamak.", "."),
])
V(None, 78, "The peaks of al-Mujaymir's head, that morning, ringed with the torrent and its wrack, were like the whorl of a spindle.",
  "Müceymir tepesinin doruğu, o sabah, selin ve getirdiği çerçöpün içinde bir iğ ağırşağı gibiydi.", [
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + ". وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: شَبَّهَ اسْتِدَارَةَ هٰذِهِ الْأَكَمَةِ بِمَا أَحَاطَ بِهَا مِنَ الْأَغْثَاءِ بِاسْتِدَارَةِ فَلْكَةِ الْمِغْزَلِ، وَإِحَاطَتَهَا بِهَا بِإِحَاطَةِ الْمِغْزَلِ؛ وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ وَهُوَ الِاسْتِدَارَةُ.",
   KAANNA_T[1] + ". A tashbih mursal mujmal: the roundness of this hill, with the wrack that rings it, is likened to the roundness of a spindle's whorl, and the ring about the hill to the spindle's (al-Zawzanī); the particle is كَأَنَّ, and the point of likeness — roundness — is left unsaid.",
   KAANNA_T[2] + ". Teşbih-i mürsel mücmeldir: bu tepenin, çevresini saran çerçöple yuvarlaklığı iğ ağırşağının yuvarlaklığına, çerçöpün onu kuşatması da iğin ağırşağı kuşatmasına benzetilmiştir (Zevzenî); edat كَأَنَّ; vech-i şebeh — yuvarlaklık — mahzûftur."),
 W("ذُرَى", "dhirwa", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir", "ism-maqsur-manqus"], J(("اسْمُ كَأَنَّ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "The noun of كَأَنَّ, in nasb by a fatha estimated on the alif", "كَأَنَّ'nin ismi, elif üzerinde takdîrî fetha ile mansûb"), MUD, Dn("جَمْعُ ذُرْوَةٍ: أَعْلَى الشَّيْءِ", "the plural of ذُرْوَة, the top of a thing", "«ذُرْوَة»nin (bir şeyin en üstü) cem'i"))),
 W("رَأْسِ", "ras", "noun", ["idafa-definiteness"], J(MI, MUD)),
 W("الْمُجَيْمِرِ", "mujaymir", "propn", ["idafa-definiteness"], J(MI, Dn("الْمُجَيْمِرُ: أَكَمَةٌ بِعَيْنِهَا", "al-Mujaymir is a particular hill", "Müceymir belirli bir tepedir"))),
 W("غُدْوَةً", "ghudwa", "noun", ["maful-fih"], J(ZARF_K("", "")), HEMI),
 HARF_JARR("مِنَ", "min", "، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَهُوَ لِلتَّعْلِيلِ، أَيْ: مِمَّا أَحَاطَ بِهَا", ", voweled with fatha before the stilled letter; it gives the cause: «because of what ringed it»", "; iki sâkinin karşılaşması sebebiyle fetha ile harekelenmiştir; ta'lîl içindir: «onu saran şeyden dolayı»"),
 W("السَّيْلِ", "sayl", "noun", ["huruf-jarr", "hal"], J(MAJR, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «فَلْكَةُ مِغْزَلِ»، كَانَ نَعْتًا لَهُ فَلَمَّا تَقَدَّمَ عَلَيْهِ صَارَ حَالًا", "the phrase hangs on an omitted hal of «the whorl of a spindle» — it was its adjective, and set before it becomes a hal", "câr-mecrûr «فَلْكَةُ مِغْزَلِ»den mahzûf hâle müteallik; onun na'tı iken öne geçince hâl olmuştur"))),
 W("وَالْأَغْثَاءِ", "ghutha", "noun", ["atf-nasaq", "jam-taksir", "ism-mamdud"], J(PRE("wa", "الْأَغْثَاءِ"), ATF("السَّيْلِ", "the torrent"), Dn("جَمْعُ غُثَاءٍ: مَا جَاءَ بِهِ السَّيْلُ مِنَ الْحَشِيشِ وَالشَّجَرِ وَالْكَلَإِ وَالتُّرَابِ", "the plural of غُثَاء: what a torrent brings down — grass, wood, herbage and earth", "«غُثَاء»ın cem'i: selin getirdiği ot, ağaç, çayır ve toprak")), s=[WA, ("الْأَغْثَاءِ", "ghutha", "noun")]),
 W("فَلْكَةُ", "falka", "noun", ["inna-wa-akhawatuha", "idafa-definiteness"], J(KHB_KAANNA, MUD, Dn("فَلْكَةُ الْمِغْزَلِ مَفْتُوحَةُ الْفَاءِ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "the whorl of a spindle, with a fatha on the fa; the sentence is a fresh one", "iğ ağırşağı; fâ'nın fethasıyla; cümle müste'nefedir"))),
 W("مِغْزَلِ", "mighzal", "noun", ["idafa-definiteness", "al-qafiya"], J(MI, QAFIYA, Dn("الْمِغْزَلُ بِضَمِّ الْمِيمِ وَفَتْحِهَا وَكَسْرِهَا", "المِغْزَل, a spindle — said with damma, fatha or kasra on the mim", "المِغْزَل: iğ — mîmin dammesi, fethası ve kesresiyle söylenir")), "."),
])
V(None, 79, "It cast its load down on the plain of al-Ghabīṭ, alighting as the Yemeni merchant alights with his laden bales.",
  "Yükünü Gabît ovasına bıraktı; denkleri yüklü Yemenli tacirin konuşu gibi kondu.", [
 W("وَأَلْقَى", "alqa", "verb", ["atf-nasaq", "form-iv-verbs", "naqis-verbs"], J(PRE("wa", "أَلْقَى"), ("فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "a past verb built on a fatha estimated on the alif", "elif üzerinde takdîrî fetha üzere mebnî mâzî"), HID("هُوَ", "it", "hüve", ("الْمَطَرِ", "the rain", "yağmura")), Dn("وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ «مَرَّ» فِي الْبَيْتِ ٧٥", "the clause is conjoined to «it passed» in verse 75", "cümle 75. beyitteki «مَرَّ» cümlesine ma'tûf")), s=[WA, ("أَلْقَى", "alqa", "verb")]),
 T("بِصَحْرَاءِ", "sahra", "noun", ["huruf-jarr", "idafa-definiteness", "ism-mamdud"], "الْبَاءُ حَرْفُ جَرٍّ، وَصَحْرَاءِ مَجْرُورٌ بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَلْقَى».", "The ba is a jarr letter; صَحْرَاءِ is in jarr by the kasra, since it is annexed — the phrase hangs on «cast down».", "Bâ cer harfi; صَحْرَاءِ muzâf olduğu için kesre ile mecrûr — câr-mecrûr «أَلْقَى»ya müteallik.", s=[BI, ("صَحْرَاءِ", "sahra", "noun")]),
 W("الْغَبِيطِ", "ghabit-hill", "propn", ["idafa-definiteness"], J(MI, Dn("الْغَبِيطُ هُنَا: أَكَمَةٌ قَدِ انْخَفَضَ وَسَطُهَا وَارْتَفَعَ طَرَفَاهَا، سُمِّيَتْ غَبِيطًا تَشْبِيهًا بِغَبِيطِ الْبَعِيرِ", "al-Ghabīṭ here: a hill low in the middle and high at both ends, so named for its likeness to a camel's saddle-frame", "Gabît burada: ortası çukur, iki ucu yüksek bir tepe; deve semerine benzetilerek bu adı almıştır"))),
 W("بَعَاعَهُ", "baa-load", "noun", ["maful-bihi", "idafa-definiteness"], J(MAFR, IDF("هُ"), Dn("الْبَعَاعُ: الثِّقْلُ، أَيْ: أَلْقَى هٰذَا الْحَيَا ثِقْلَهُ", "البَعَاع: a load — the rain threw down its burden", "البَعَاع: yük — yağmur yükünü bıraktı")), HEMI, [("بَعَاعَ", "baa-load", "noun"), P("هُ")]),
 T("نُزُولَ", "nuzul", "noun", ["maful-mutlaq", "masdar", "idafa-definiteness", "hadhf-al-mudaf-wal-mudaf-ilayh", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — عَلَى حَذْفِ مُضَافٍ، وَتَقْدِيرُ الْبَيْتِ: وَأَلْقَى ثِقْلَهُ بِصَحْرَاءِ الْغَبِيطِ فَنَزَلَ بِهِ نُزُولًا مِثْلَ نُزُولِ التَّاجِرِ الْيَمَانِيِّ. وَفِيهِ تَشْبِيهٌ بَلِيغٌ حُذِفَتْ مِنْهُ الْأَدَاةُ وَوَجْهُ الشَّبَهِ: شَبَّهَ نُزُولَ هٰذَا الْمَطَرِ بِنُزُولِ التَّاجِرِ، وَشَبَّهَ ضُرُوبَ النَّبَاتِ النَّاشِئَةِ مِنْ هٰذَا الْمَطَرِ بِصُنُوفِ الثِّيَابِ الَّتِي نَشَرَهَا التَّاجِرُ عِنْدَ عَرْضِهَا لِلْبَيْعِ.",
   "An absolute object, in nasb by the fatha, annexed — with an annexed noun left out; the verse in full is: «it threw its load on the plain of al-Ghabīṭ and alighted there with an alighting like that of the Yemeni merchant». A tashbih balīgh, the particle and the point of likeness both dropped: the coming down of this rain is likened to the merchant's alighting, and the many kinds of plants that spring from it to the kinds of cloth he spreads out when he shows them for sale (al-Zawzanī).",
   "Mef'ûlün mutlak, fetha ile mansûb, muzâf — muzâfın hazfiyle; beytin takdiri: «yükünü Gabît ovasına bıraktı ve oraya Yemenli tacirin konuşu gibi bir konuşla kondu». Edatı ve vech-i şebehi hazfedilmiş teşbih-i belîğdir: bu yağmurun inişi tacirin konuşuna, yağmurdan biten türlü bitkiler de tacirin satışa sunarken serdiği türlü kumaşlara benzetilmiştir (Zevzenî)."),
 T("الْيَمَانِي", "yamani", "noun", ["idafa-definiteness", "ism-maqsur-manqus", "ism-mansub", "hadhf-wa-taqdir"],
   "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، مِنْ إِضَافَةِ الْمَصْدَرِ إِلَى فَاعِلِهِ — نَعْتٌ لِمَوْصُوفٍ مَحْذُوفٍ أَيِ: التَّاجِرِ الْيَمَانِي؛ وَهُوَ نِسْبَةٌ إِلَى الْيَمَنِ خُفِّفَتْ يَاؤُهَا وَعُوِّضَ مِنْهَا الْأَلِفُ.",
   "The second term of the idafa, in jarr by a kasra estimated on the ya — the masdar annexed to its doer; it describes a noun left out: «the Yemeni merchant». It is the nisba to al-Yaman with its ya lightened and an alif put in its place.",
   "Muzâfun ileyh, yâ üzerinde takdîrî kesre ile mecrûr — masdarın fâiline izâfeti; mahzûf mevsûfun na'tıdır: «Yemenli tacir». Yemen'e nisbettir; yâsı tahfif edilmiş, yerine elif getirilmiştir."),
 T("ذِي", "dhu", "noun", ["naat-sifa", "five-nouns", "idafa-definiteness"], "نَعْتٌ ثَانٍ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "A second adjective of the omitted noun, in jarr by the ya — one of the five nouns; annexed.", "Mahzûf mevsûfun ikinci na'tı; esmâ-i hamseden olduğu için yâ ile mecrûr; muzâf."),
 W("الْعِيَابِ", "ayba", "noun", ["idafa-definiteness", "jam-taksir"], J(MI, Dn("جَمْعُ عَيْبَةٍ: وِعَاءُ الثِّيَابِ", "the plural of عَيْبَة, a bale or chest for clothes", "«عَيْبَة»nin (elbise denk veya sandığı) cem'i"))),
 W("الْمُحَمَّلِ", "muhammal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(("نَعْتٌ ثَالِثٌ لِلْمَوْصُوفِ الْمَحْذُوفِ مَجْرُورٌ بِالْكَسْرَةِ", "A third adjective of the omitted noun, in jarr by the kasra", "Mahzûf mevsûfun üçüncü na'tı, kesre ile mecrûr"), Dn("أَيْ: صَاحِبِ الْعِيَابِ الْمُحَمَّلِ مِنَ الثِّيَابِ؛ وَيَجُوزُ كَسْرُ مِيمِهِ الثَّانِيَةِ عَلَى أَنَّهُ اسْمُ فَاعِلٍ", "that is, the owner of the bales, laden with cloth; its second mim may also take a kasra, as an ism fa'il", "yani denk sahibi, kumaş yüklü; ikinci mîmin kesresiyle ism-i fâil olması da câizdir")), "."),
])
V(None, 80, "The song-birds of the valleys, that early morning, were as though they had been given a dawn-draught of the finest wine, peppered.",
  "Vadilerin ötücü kuşları, o sabah erkenden, sanki biberli, en hâlis şaraptan sabah içkisi içirilmişlerdi.", [
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + ". وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ الْمَكَاكِيُّ فِي حِدَّةِ أَلْسِنَتِهَا وَتَتَابُعِ أَصْوَاتِهَا وَنَشَاطِهَا فِي تَغْرِيدِهَا، وَالْمُشَبَّهُ بِهِ مَنْ سُقِيَ الْخَمْرَ الْمُفَلْفَلَةَ صَبَاحًا؛ جَعَلَ نَشَاطَ الطَّيْرِ كَالسُّكْرِ، وَتَغْرِيدَهَا بِحِدَّةِ أَلْسِنَتِهَا مِنْ حَذْيِ الشَّرَابِ الْمُفَلْفَلِ إِيَّاهَا؛ وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ.",
   KAANNA_T[1] + ". A tashbih mursal mujmal: the thing likened is the birds, sharp of tongue, their notes following fast, lively in their song; the thing they are likened to is one given peppered wine in the morning — their liveliness is made like drunkenness, and their sharp-tongued trilling like the bite of the peppered drink (al-Zawzanī); the particle is كَأَنَّ, and the point of likeness is left unsaid.",
   KAANNA_T[2] + ". Teşbih-i mürsel mücmeldir: müşebbeh, dillerinin keskinliği, seslerinin ardı ardına gelişi ve ötüşlerindeki canlılıkla kuşlar; müşebbehün bih, sabahleyin biberli şarap içirilmiş kimse — kuşların canlılığı sarhoşluk gibi, keskin dilli ötüşleri de biberli içkinin dili yakması gibi kılınmıştır (Zevzenî); edat كَأَنَّ; vech-i şebeh mahzûftur."),
 W("مَكَاكِيَّ", "mukka", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], J(ISM_KAANNA, MUD, Dn("جَمْعُ مُكَّاءٍ: ضَرْبٌ مِنَ الطَّيْرِ", "the plural of مُكَّاء, a kind of bird", "«مُكَّاء»ın (bir kuş türü) cem'i"))),
 W("الْجِوَاءِ", "jiwa", "noun", ["idafa-definiteness", "ism-mamdud"], J(MI, Dn("الْجِوَاءُ: الْوَادِي، وَالْجَمْعُ أَجْوِيَةٌ", "الجِوَاء: a valley; plural أَجْوِيَة", "الجِوَاء: vadi; cem'i أَجْوِيَة"))),
 W("غُدَيَّةً", "ghudayya", "noun", ["maful-fih"], J(ZARF_K("", ""), Dn("تَصْغِيرُ غُدْوَةٍ أَوْ غَدَاةٍ", "the diminutive of غُدْوَة or غَدَاة", "«غُدْوَة» ya da «غَدَاة»in tasgîri")), HEMI),
 T("صُبِحْنَ", "sabaha", "verb", ["al-majhul-fil-kafiya", "naib-al-fail", "al-bariz-al-muttasil", "inna-wa-akhawatuha", "mafulayn"],
   "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنُونِ النِّسْوَةِ، وَالنُّونُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ، وَهُوَ الْمَفْعُولُ الْأَوَّلُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَأَنَّ؛ الصَّبْحُ: سَقْيُ الصَّبُوحِ.",
   "A passive past verb built on sukun because the feminine nun is attached; the nun is the deputy doer, in the seat of raf' — it is the first object — and the clause is the predicate of كَأَنَّ, in the seat of raf'; الصَّبْح: giving the morning draught.",
   "Nûn-ı nisveye bitiştiği için sükûn üzere mebnî meçhul mâzî; nûn nâib-i fâil, mahallen merfû — birinci mef'ûldür; cümle كَأَنَّ'nin haberi olarak mahallen merfû; الصَّبْح: sabah içkisi içirmek."),
 W("سُلَافًا", "sulaf", "noun", ["mafulayn"], J(("مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ", "A second object, in nasb by the fatha", "İkinci mef'ûlün bih, fetha ile mansûb"), Dn("السُّلَافُ: أَجْوَدُ الْخَمْرِ، وَهُوَ مَا انْعَصَرَ مِنَ الْعِنَبِ مِنْ غَيْرِ عَصْرٍ", "السُّلَاف: the best of wine, what runs from the grapes unpressed", "السُّلَاف: şarabın en iyisi; üzümden sıkılmadan kendiliğinden akan"))),
 HARF_JARR("مِنْ", "min"),
 W("رَحِيقٍ", "rahiq", "noun", ["huruf-jarr", "naat-sifa"], J(MAJR, Dn("وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ نَعْتٍ لِـ«سُلَافًا»؛ الرَّحِيقُ: الْخَمْرُ الصَّافِيَةُ", "the phrase hangs on an omitted adjective of «the finest wine»; الرَّحِيق: clear wine", "câr-mecrûr «سُلَافًا»nın mahzûf na'tına müteallik; الرَّحِيق: duru şarap"))),
 W("مُفَلْفَلِ", "mufalfal", "noun", ["naat-sifa", "ism-maful", "al-qafiya"], J(NAAT("رَحِيقٍ", "jarr", en_of="wine"), QAFIYA, Dn("الْمُفَلْفَلُ: الَّذِي أُلْقِيَ فِيهِ الْفُلْفُلُ", "المُفَلْفَل: with pepper put in it", "المُفَلْفَل: içine biber atılmış")), "."),
])
V(None, 81, "And the wild beasts, drowned in it at evening, at its farthest edges, were like the dug-up roots of the wild onion.",
  "Akşamleyin onun en uzak kıyılarında boğulmuş yırtıcılar ise, sanki sökülmüş yaban soğanı kökleriydi.", [
 T("كَأَنَّ", "kaanna", "part", ["inna-wa-akhawatuha", "tashbih", "arkan-al-tashbih", "aqsam-al-tashbih"],
   KAANNA_T[0] + ". وَفِيهِ تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ: الْمُشَبَّهُ السِّبَاعُ الْغَرْقَى، وَالْمُشَبَّهُ بِهِ أُصُولُ الْبَصَلِ الْبَرِّيِّ، وَالْأَدَاةُ كَأَنَّ، وَوَجْهُ الشَّبَهِ مَحْذُوفٌ: شَبَّهَ تَلَطُّخَهَا بِالطِّينِ وَالْمَاءِ الْكَدِرِ بِأُصُولِ الْبَصَلِ الْبَرِّيِّ لِأَنَّهَا مُتَلَطِّخَةٌ بِالطِّينِ وَالتُّرَابِ.",
   KAANNA_T[1] + ". A tashbih mursal mujmal: the thing likened is the drowned beasts, the thing they are likened to is the roots of the wild onion, the particle is كَأَنَّ, and the point of likeness is left unsaid — smeared with mud and muddy water, they are like those roots, which come up smeared with mud and earth (al-Zawzanī).",
   KAANNA_T[2] + ". Teşbih-i mürsel mücmeldir: müşebbeh boğulmuş yırtıcılar, müşebbehün bih yaban soğanının kökleri, edat كَأَنَّ; vech-i şebeh mahzûftur: çamura ve bulanık suya bulanmış hâlleri, çamura ve toprağa bulanmış olan yaban soğanı köklerine benzetilmiştir (Zevzenî)."),
 W("السِّبَاعَ", "sabu", "noun", ["inna-wa-akhawatuha", "jam-taksir"], J(ISM_KAANNA)),
 PJ("فِيهِ", "فِي", "fi", "هِ", ("فِي", "فِي", "فِي"), "غَرْقَى", "drowned", "ya", extra=("؛ وَالضَّمِيرُ لِلسَّيْلِ", "; the pronoun is the flood", "; zamir sele döner")),
 W("غَرْقَى", "ghariq", "noun", ["hal", "jam-taksir", "ism-maqsur-manqus"], J(("حَالٌ مِنَ «السِّبَاعَ» مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", "A hal of «the beasts», in nasb by a fatha estimated on the alif", "«السِّبَاعَ»dan hâl, elif üzerinde takdîrî fetha ile mansûb"), Dn("جَمْعُ غَرِيقٍ مِثْلُ مَرْضَى وَمَرِيضٍ", "the plural of غَرِيق, as مَرْضَى is of مَرِيض", "«غَرِيق»in cem'i (مَرِيض – مَرْضَى gibi)"))),
 W("عَشِيَّةً", "ashiyya", "noun", ["maful-fih"], J(("ظَرْفُ زَمَانٍ مَنْصُوبٌ بِالْفَتْحَةِ", "An adverb of time, in nasb by the fatha", "Zaman zarfı, fetha ile mansûb"), Dn("مُتَعَلِّقٌ بِـ«غَرْقَى»؛ الْعَشِيَّةُ: مَا بَعْدَ الزَّوَالِ إِلَى طُلُوعِ الْفَجْرِ", "it hangs on «drowned»; العَشِيَّة: from past noon until the break of dawn", "«غَرْقَى»ya müteallik; العَشِيَّة: zevâlden fecrin doğuşuna kadar olan vakit")), HEMI),
 T("بِأَرْجَائِهِ", "raja-side", "noun", ["huruf-jarr", "idafa-definiteness", "jam-taksir", "hal"], "الْبَاءُ حَرْفُ جَرٍّ بِمَعْنَى «فِي»، وَأَرْجَاءِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنْ «أَنَابِيشُ عُنْصُلِ»؛ الْأَرْجَاءُ: النَّوَاحِي، الْوَاحِدُ رَجًا.", "The ba is a jarr letter meaning «in»; أَرْجَاءِ is in jarr by the kasra, annexed, and the هِ is its second term — the phrase hangs on an omitted hal of «roots of wild onion»; الأَرْجَاء: the sides, singular رَجًا.", "Bâ «-de» anlamında cer harfi; أَرْجَاءِ kesre ile mecrûr, muzâf; «hî» muzâfun ileyh — câr-mecrûr «أَنَابِيشُ عُنْصُلِ»den mahzûf hâle müteallik; الأَرْجَاء: kenarlar, tekili رَجًا.", s=[BI, ("أَرْجَاءِ", "raja-side", "noun"), P("هِ")]),
 T("الْقُصْوَى", "quswa", "noun", ["naat-sifa", "ism-tafdil", "ism-maqsur-manqus"],
   "نَعْتٌ لِـ«أَرْجَائِهِ» مَجْرُورٌ " + MAQSUR_J + " — تَأْنِيثُ الْأَقْصَى، وَهُوَ الْأَبْعَدُ؛ وَوُصِفَ الْجَمْعُ بِالْمُفْرَدِ الْمُؤَنَّثِ كَقَوْلِهِ تَعَالَى: «لِنُرِيَكَ مِنْ آيَاتِنَا الْكُبْرَى».",
   "An adjective of «its edges», in jarr by a kasra estimated on the alif — the feminine of الأَقْصَى, «the farthest»; a plural is here described by a feminine singular, as in the Qurʾānic «لِنُرِيَكَ مِنْ آيَاتِنَا الْكُبْرَى» (20:23).",
   "«أَرْجَائِهِ»nin na'tı, elif üzerinde takdîrî kesre ile mecrûr — «en uzak» anlamındaki الأَقْصَى'nın müennesi; cemi burada müfred müennesle vasfedilmiştir; «لِنُرِيَكَ مِنْ آيَاتِنَا الْكُبْرَى» (Tâhâ 23) âyetindeki gibi."),
 W("أَنَابِيشُ", "unbusha", "noun", ["inna-wa-akhawatuha", "idafa-definiteness", "jam-taksir"], J(KHB_KAANNA, MUD, Dn("الْأَنَابِيشُ: أُصُولُ النَّبْتِ، سُمِّيَتْ بِذٰلِكَ لِأَنَّهَا يُنْبَشُ عَنْهَا، وَاحِدَتُهَا أُنْبُوشَةٌ؛ وَالْجُمْلَةُ مُسْتَأْنَفَةٌ", "الأَنَابِيش: the roots of plants, so called because they are dug for; singular أُنْبُوشَة; the sentence is a fresh one", "الأَنَابِيش: bitki kökleri; kazılıp çıkarıldıkları için bu adı almıştır; tekili أُنْبُوشَة; cümle müste'nefedir"))),
 W("عُنْصُلِ", "unsul", "noun", ["idafa-definiteness", "al-qafiya"], J(MI, QAFIYA, Dn("الْعُنْصُلُ: الْبَصَلُ الْبَرِّيُّ", "العُنْصُل: the wild onion", "العُنْصُل: yaban soğanı")), "."),
])
# ==== INSERT 76-81 ABOVE ====
# ==== PACKAGE (verses are inserted ABOVE this line, in poem order) ====

# ---------------------------------------------------------------------------------------------------------------------
# Figures that rest on the Talkhīṣ's OWN DEFINITION (no commentator names them) — the orchestrator's ruling: such a figure
# belongs in the package, and its line says «عَلَى حَدِّ التَّلْخِيصِ». The definitions were re-read in
# research/sources/talkhis-al-miftah-balagha.txt: the ṭibāq (two opposed meanings, of one kind or of two), what is joined
# to the jinās (derivation), the complete jinās (kind, number, shape and order of the letters), radd al-ʿajuz ʿalā al-ṣadr
# in verse (one word at the end of the verse, its partner at the head, middle or end of the first hemistich or at the head
# of the second), the iltifāt, the tajrīd (a man addressing himself), the qaṣr by negation and exception, the majāz ʿaqlī.
# A verse not yet authored is skipped; verses written after this ruling carry the wording in their own lines.
# ---------------------------------------------------------------------------------------------------------------------
HADD = ("عَلَى حَدِّ التَّلْخِيصِ", "by the Talkhīṣ's definition", "Telhîs'in tarifine göre")
def _tk(n, surface, nth=0):
    hits = [t for t in VERSE[n]["tokens"] if t["surface"]["full"] == N(surface)]
    assert len(hits) > nth, (n, surface)
    return hits[nth]
def SUB(n, surface, ar, en, tr, nth=0):
    """reword a claim already in the line: each of ar/en/tr is (old, new)"""
    if n not in VERSE: return
    t = _tk(n, surface, nth)
    for L, (old, new) in (("ar", ar), ("en", en), ("tr", tr)):
        assert t["irab"][L].count(N(old)) == 1, (n, surface, L, old)
        t["irab"][L] = t["irab"][L].replace(N(old), N(new))
def ADD(n, surface, tags, ar, en, tr, nth=0):
    """add a figure to the end of the token's line, and its grammar notes"""
    if n not in VERSE: return
    t = _tk(n, surface, nth)
    for L, x, lead in (("ar", ar, " وَفِيهِ — " + HADD[0] + " — "), ("en", en, " B" + HADD[1][1:] + ", "), ("tr", tr, " " + HADD[2] + " ")):
        assert t["irab"][L].endswith("."), (n, surface, L)
        t["irab"][L] = t["irab"][L] + N(lead + x + ".")
    t["grammar"] = t["grammar"] + [g for g in tags if g not in t["grammar"]]
def TAG(n, surface, tags, nth=0):
    if n not in VERSE: return
    t = _tk(n, surface, nth); t["grammar"] = t["grammar"] + [g for g in tags if g not in t["grammar"]]
def _tib(n, surface):
    SUB(n, surface, ("طِبَاق", "— " + HADD[0] + " — طِبَاق"), (" a tibaq", ", " + HADD[1] + ", a tibaq"), (" tıbâk", ", " + HADD[2] + ", tıbâk"))
def ISHT(n, surface, a, b, nth=0, radd=None):
    """what is joined to the jinās: a and b are bound by derivation; radd = (ar, en, tr) of where the partner of the rhyme-word stands"""
    ar = "مَا يُلْحَقُ بِالْجِنَاسِ بَيْنَ «%s» وَ«%s»: يَجْمَعُهُمَا الِاشْتِقَاقُ" % (a, b)
    en = "there is what is joined to the jinās between «%s» and «%s»: derivation from one root binds them" % (a, b)
    tr = "«%s» ile «%s» arasında cinâsa mülhak olan iştikak vardır" % (a, b)
    tags = ["mulhaq-bil-jinas"]
    if radd:
        ar += "؛ وَرَدُّ الْعَجُزِ عَلَى الصَّدْرِ: «%s» فِي آخِرِ الْبَيْتِ وَ«%s» %s" % (b, a, radd[0])
        en += "; and a radd al-ʿajuz ʿalā al-ṣadr: «%s» ends the verse and «%s» stands %s" % (b, a, radd[1])
        tr += "; ayrıca reddü'l-acüz ale's-sadr vardır: «%s» beytin sonunda, «%s» %s" % (b, a, radd[2])
        tags.append("radd-al-ajuz")
    ADD(n, surface, tags, ar, en, tr, nth)
# -- claims already in the lines, now said on their true basis
for _n, _s in ((2, "جَنُوبٍ"), (36, "مُثَنًّى"), (46, "اللَّيْلُ"), (53, "مِكَرٍّ"), (53, "مُقْبِلٍ"), (57, "الْخِفَّ"), (73, "أَيْمَنُ")): _tib(_n, _s)
_ilt = (("وَفِيهِ الْتِفَاتٌ", "وَفِيهِ — " + HADD[0] + " — الْتِفَاتٌ"), ("there is an iltifāt", "there is, " + HADD[1] + ", an iltifāt"), ("hitaba iltifât vardır", "hitaba, " + HADD[2] + ", iltifât vardır"))
SUB(7, "كَدَأْبِكَ", *_ilt); SUB(42, "هَوَاكِ", *_ilt)
SUB(10, "لَكَ", ("وَالْخِطَابُ لِنَفْسِهِ عَلَى التَّجْرِيدِ", "وَالْخِطَابُ لِنَفْسِهِ، وَهُوَ — " + HADD[0] + " — تَجْرِيدٌ"), ("he is still speaking to himself (tajrīd)", "he is still speaking to himself — " + HADD[1] + ", a tajrīd"), ("hitap, tecrîd yoluyla kendisinedir", "hitap kendisinedir; bu, " + HADD[2] + " tecrîddir"))
SUB(20, "قَاتِلِي", ("مَجَازٌ عَقْلِيٌّ", "— " + HADD[0] + " — مَجَازٌ عَقْلِيٌّ"), ("is a majaz ʿaqlī", "is, " + HADD[1] + ", a majaz ʿaqlī"), ("alâkası sebebiyet olan", HADD[2] + ", alâkası sebebiyet olan"))
SUB(22, "وَمَا", ("طَرِيقُ قَصْرٍ", "— " + HADD[0] + " — طَرِيقُ قَصْرٍ"), ("is a way of restriction", "is, " + HADD[1] + ", a way of restriction"), ("kasr yoludur", HADD[2] + " kasr yoludur"))
SUB(75, "فَأَنْزَلَ", ("وَبَيْنَهُ وَبَيْنَ «مَنْزِلِ» مَا يُلْحَقُ", "وَبَيْنَهُ وَبَيْنَ «مَنْزِلِ» — " + HADD[0] + " — مَا يُلْحَقُ"), ("there is what is joined", "there is, " + HADD[1] + ", what is joined"), ("cinâsa mülhak olan iştikak vardır", HADD[2] + " cinâsa mülhak olan iştikak vardır"))
ADD(75, "مَنْزِلِ", ["radd-al-ajuz"], "رَدُّ الْعَجُزِ عَلَى الصَّدْرِ: «مَنْزِلِ» فِي آخِرِ الْبَيْتِ وَ«أَنْزَلَ» فِي صَدْرِ الْمِصْرَاعِ الثَّانِي، وَهُمَا مُلْحَقَانِ بِالْمُتَجَانِسَيْنِ",
    "there is a radd al-ʿajuz ʿalā al-ṣadr: «مَنْزِلِ» ends the verse and «أَنْزَلَ» stands at the head of the second hemistich, the two being joined to the jinās", "reddü'l-acüz ale's-sadr vardır: «مَنْزِلِ» beytin sonunda, «أَنْزَلَ» ikinci mısraın başındadır; ikisi cinâsa mülhaktır")
# -- figures of sound, and ṭibāqs the words themselves show
ISHT(25, "تَعَرُّضَ", "تَعَرَّضَتْ", "تَعَرُّضَ")
ADD(30, "رَيَّا", ["tibaq"], "طِبَاقٌ بَيْنَ «هَضِيمَ» وَ«رَيَّا»: الضُّمُورُ وَالِامْتِلَاءُ", "«هَضِيمَ» and «رَيَّا» make a tibaq: leanness against fullness", "«هَضِيمَ» ile «رَيَّا» arasında tıbâk vardır: incelik ile dolgunluk")
TAG(30, "هَضِيمَ", ["tibaq"])
ISHT(38, "الضُّحَى", "تُضْحِي", "الضُّحَى")
ADD(40, "الظَّلَامَ", ["tibaq"], "طِبَاقٌ بَيْنَ الْفِعْلِ «تُضِيءُ» وَالِاسْمِ «الظَّلَامَ»: الْإِضَاءَةُ وَالظُّلْمَةُ", "the verb «تُضِيءُ» and the noun «الظَّلَامَ» make a tibaq: light against dark", "«تُضِيءُ» fiili ile «الظَّلَامَ» ismi arasında tıbâk vardır: aydınlık ile karanlık")
TAG(40, "تُضِيءُ", ["tibaq"])
ISHT(42, "بِمُنْسَلِ", "تَسَلَّتْ", "مُنْسَلِ", radd=("فِي صَدْرِ الْمِصْرَاعِ الْأَوَّلِ", "at the head of the first hemistich", "birinci mısraın başındadır"))
ISHT(46, "الْإِصْبَاحُ", "صُبْحٍ", "الْإِصْبَاحُ")
ADD(50, "لَمَّا", ["jinas-tamm"], "جِنَاسٌ تَامٌّ بَيْنَ «لَمَّا» الظَّرْفِيَّةِ فِي صَدْرِ الْبَيْتِ وَ«لَمَّا» الْجَازِمَةِ هُنَا: اتَّفَقَ اللَّفْظَانِ فِي الْحُرُوفِ وَعَدَدِهَا وَهَيْئَتِهَا وَتَرْتِيبِهَا وَاخْتَلَفَ الْمَعْنَى",
    "there is a complete jinās between the لَمَّا of time in the first hemistich and the لَمَّا of jazm here: the two agree in their letters, their number, their vowels and their order, and differ in meaning", "birinci mısradaki zarf olan «لَمَّا» ile buradaki câzim «لَمَّا» arasında cinâs-ı tâm vardır: iki lafız harflerde, sayıda, harekede ve sırada birdir, mânâ ise ayrıdır", nth=1)
ADD(51, "أَفَاتَهُ", ["tibaq"], "طِبَاقٌ بَيْنَ الْفِعْلَيْنِ «نَالَ» وَ«أَفَاتَ»: الظَّفَرُ بِالشَّيْءِ وَتَفْوِيتُهُ", "the two verbs «نَالَ» and «أَفَاتَ» make a tibaq: gaining a thing against letting it go", "«نَالَ» ile «أَفَاتَ» fiilleri arasında tıbâk vardır: bir şeyi elde etmek ile elden kaçırmak")
TAG(51, "نَالَ", ["tibaq"])
ISHT(51, "حَرْثِي", "يَحْتَرِثْ", "حَرْثِي")
ISHT(54, "زَلَّتِ", "يَزِلُّ", "زَلَّتِ")
ISHT(55, "جَاشَ", "جَيَّاشٍ", "جَاشَ")
ISHT(70, "أُرِيكَ", "تَرَى", "أُرِيكَ")
# ==== HADD ABOVE ====
# =====================================================================================================================
# The package: lexicon, paradigms, manifest
# =====================================================================================================================
AR_DIG = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")
def ar_num(n): return str(n).translate(AR_DIG)
TOTAL = 81   # the poem's verses in al-Zawzanī's count
PLAN = [  # (first verse, last verse, the chapter's theme) — every verse of the poem, in al-Zawzanī's order, none skipped
 (1, 6, ("الْوُقُوفُ عَلَى الْأَطْلَالِ", "The halt at the ruins", "Yurt kalıntıları başında duruş")),
 (7, 12, ("ذِكْرَى الْأَيَّامِ الْخَالِيَةِ وَيَوْمُ دَارَةِ جُلْجُلٍ", "Days remembered: the day at Dārat Juljul", "Hatırlanan günler: Dâretü Cülcül günü")),
 (13, 18, ("خِدْرُ عُنَيْزَةَ", "ʿUnayza's howdah", "Uneyze'nin mahfesi")),
 (19, 25, ("عِتَابُ فَاطِمَةَ وَبَيْضَةُ الْخِدْرِ", "The reproach to Fāṭima; the lady of the guarded tent", "Fâtıma'ya sitem; korunan çadırın hanımı")),
 (26, 31, ("الزِّيَارَةُ لَيْلًا", "The visit by night", "Gece ziyareti")),
 (32, 37, ("وَصْفُ الْمَحْبُوبَةِ", "The beloved described", "Sevgilinin tasviri")),
 (38, 43, ("تَمَامُ الْوَصْفِ وَالْقَلْبُ الَّذِي لَا يَسْلُو", "The description completed; the heart that does not forget", "Tasvirin tamamı; unutmayan gönül")),
 (44, 51, ("اللَّيْلُ وَالْوَادِي وَالذِّئْبُ", "The night, the valley and the wolf", "Gece, vadi ve kurt")),
 (52, 57, ("الْفَرَسُ", "The horse", "At")),
 (58, 63, ("تَمَامُ وَصْفِ الْفَرَسِ وَظُهُورُ السِّرْبِ", "The horse, continued; the herd appears", "At tasvirinin devamı; sürünün görünmesi")),
 (64, 69, ("الصَّيْدُ", "The hunt", "Av")),
 (70, 75, ("الْبَرْقُ وَالْمَطَرُ", "The lightning and the rain", "Şimşek ve yağmur")),
 (76, 81, ("السَّيْلُ وَآثَارُهُ", "The flood and what it left", "Sel ve bıraktıkları")),
]
assert [a for a, b, t in PLAN] == [1] + [b + 1 for a, b, t in PLAN[:-1]] and PLAN[-1][1] == TOTAL and all(6 <= b - a + 1 <= 8 for a, b, t in PLAN)
# only what is finished is published: the chapters whose verses are all authored, contiguously from verse 1
DONE = 0
while DONE + 1 in VERSE: DONE += 1
READY = [(a, b, t) for a, b, t in PLAN if b <= DONE]
LAST = READY[-1][1] if READY else 0
CHAPS = [S1] + [[{"id": "s%d" % (i + 1), **VERSE[n]} for i, n in enumerate(range(a, b + 1))] for a, b, t in READY]
TITLES = [{"ar": "خَبَرُ امْرِئِ الْقَيْسِ عِنْدَ ابْنِ قُتَيْبَةَ", "en": "The poet's story, from Ibn Qutayba", "tr": "Şairin haberi — İbn Kuteybe'den"}] + [
    {"ar": "%s (الْأَبْيَاتُ %s–%s)" % (t[0], ar_num(a), ar_num(b)), "en": "%s (verses %d–%d)" % (t[1], a, b), "tr": "%s (%d–%d. beyitler)" % (t[2], a, b)} for a, b, t in READY]
ALL_AUTHORED = S1 + [VERSE[n] for n in sorted(VERSE)]     # every sentence written so far, published or waiting

# ---- the lexicon: every key by lemma identity from the shelf; the entries in NEW_GLOSS are new ---------------------------
PREF = ["talkhis-al-miftah", "al-kafiya", "izhar-al-asrar", "qisas-al-nabiyyin-4", "al-usul-al-munifa", "marah-al-arwah", "tasrif-al-izzi",
        "bad-al-amali", "abu-hanifa-wa-al-safina", "alb-arslan-wa-malazgird", "ibn-khaldun-wa-timur", "fath-al-qustantiniyya"]
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
def find_gloss(k):
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

def G(lemma, pos, en, tr, level, root=None, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
PLACE_OPENING = ("a place named in the opening of the Muʿallaqa", "Muallaka'nın başında anılan bir yer")
NEW_GLOSS = {
 # ---- the khabar ----
 "dammun": G("دَمُّون", "propn", "Dammūn — the place where the news of his father's killing reached Imruʾ al-Qays (a diptote)", "Demmûn — babasının öldürüldüğü haberinin İmruülkays'a ulaştığı yer (gayr-i munsarif)", 6),
 "mashar": G("مَعْشَر", "noun", "a company, a people, a kindred group", "topluluk, cemaat, aynı soydan grup", 4, "ع ش ر"),
 "yamanin": G("يَمَانٍ", "noun", "a Yemeni, of Yemen — the irregular nisba to الْيَمَن (pl. يَمَانُونَ)", "Yemenli — «الْيَمَن»e kıyas dışı nisbet (çoğ. يَمَانُونَ)", 5, "ي م ن"),
 "sahw": G("صَحْو", "noun", "sobriety, being sober (masdar of صَحَا)", "ayıklık, ayılma (صَحَا'nın masdarı)", 5, "ص ح و"),
 "sukr": G("سُكْر", "noun", "drunkenness", "sarhoşluk", 4, "س ك ر"),
 "mashan": G("مَصْحًى", "noun", "sobering up, coming round from drunkenness (a masdar with mim from صَحَا)", "ayılma, sarhoşluktan kendine gelme (صَحَا'dan mîmli masdar)", 6, "ص ح و"),
 "ala-swear": G("آلَى", "verb", "to swear an oath (آلَى يُؤْلِي إِيلَاءً)", "yemin etmek (آلَى يُؤْلِي إِيلَاءً)", 6, "أ ل و", form="IV"),
 "thaara": G("ثَأَرَ", "verb", "to take blood-vengeance — ثَأَرَ بِهِ: for a slain man (ثَأَرَ يَثْأَرُ)", "kan davası gütmek, öç almak — ثَأَرَ بِهِ: öldürülenin öcünü almak (ثَأَرَ يَثْأَرُ)", 6, "ث أ ر", form="I"),
 # ---- the halt at the ruins ----
 "siqt": G("سِقْط", "noun", "the edge of a sand-ridge, where the sand thins out and ends", "kum tepesinin ucu, kumun incelip bittiği yer", 6, "س ق ط"),
 "liwa": G("لِوًى", "noun", "a winding stretch of sand, where the sand bends and twists", "kumun eğrilip büküldüğü yer, kıvrımlı kum şeridi", 6, "ل و ي"),
 "dakhul": G("الدَّخُول", "propn", "al-Dakhūl — " + PLACE_OPENING[0], "Dehûl — " + PLACE_OPENING[1], 6),
 "hawmal": G("حَوْمَل", "propn", "Ḥawmal — " + PLACE_OPENING[0], "Havmel — " + PLACE_OPENING[1], 6),
 "tudih": G("تُوضِح", "propn", "Tūḍiḥ — " + PLACE_OPENING[0] + " (a diptote)", "Tûdıh — " + PLACE_OPENING[1] + " (gayr-i munsarif)", 6),
 "miqrat": G("الْمِقْرَاة", "propn", "al-Miqrāt — " + PLACE_OPENING[0], "Mikrât — " + PLACE_OPENING[1], 6),
 "rasm": G("رَسْم", "noun", "a trace — what clings to the ground of an abandoned camp, such as dung and ashes (pl. رُسُوم, أَرْسُم)", "iz — terk edilmiş konak yerinde toprağa yapışıp kalan ters, kül gibi kalıntı (çoğ. رُسُوم, أَرْسُم)", 5, "ر س م", "رُسُوم"),
 "nasaja": G("نَسَجَ", "verb", "to weave (نَسَجَ يَنْسِجُ)", "dokumak (نَسَجَ يَنْسِجُ)", 4, "ن س ج", form="I"),
 "janub": G("جَنُوب", "noun", "the south wind", "güney rüzgârı", 4, "ج ن ب"),
 "shamal": G("شَمْأَل", "noun", "the north wind — one of the forms of شَمَال", "kuzey rüzgârı — «شَمَال»in lügatlerinden biri", 6, "ش م ل"),
 "baar": G("بَعَر", "noun", "dung, droppings (of camels, sheep, antelopes)", "ters, (deve, koyun, ceylan) pisliği", 5, "ب ع ر"),
 "rim": G("رِئْم", "noun", "a pure-white antelope that lives in the sands (pl. أَرْآم)", "kumlarda yaşayan bembeyaz ceylan (çoğ. أَرْآم)", 6, "ر أ م", "أَرْآم"),
 "habb-grain": G("حَبّ", "noun", "grain, seeds, berries (a collective; one: حَبَّة)", "tane, tohum (cins ismi; teki حَبَّة)", 3, "ح ب ب"),
 "fulful": G("فُلْفُل", "noun", "pepper; حَبُّ فُلْفُلٍ: peppercorns", "karabiber; حَبُّ فُلْفُلٍ: biber taneleri", 5),
 "ghadat": G("غَدَاة", "noun", "the early morning (pl. غَدَوَات)", "sabah vakti, kuşluk (çoğ. غَدَوَات)", 4, "غ د و", "غَدَوَات"),
 "bayn-parting": G("بَيْن", "noun", "parting, separation (masdar of بَانَ)", "ayrılık (بَانَ'nin masdarı)", 5, "ب ي ن"),
 "samura-tree": G("سَمُرَة", "noun", "an acacia — a tree of the ṭalḥ kind (pl. سَمُرَات)", "semure — talh cinsinden bir akasya ağacı (çoğ. سَمُرَات)", 6, "س م ر", "سَمُرَات"),
 "hayy-tribe": G("حَيّ", "noun", "a tribe, a tribal encampment (pl. أَحْيَاء)", "kabile, oba (çoğ. أَحْيَاء)", 4, "ح ي ي", "أَحْيَاء"),
 "naqif": G("نَاقِف", "noun", "one who splits open (a colocynth, to get at its seed) — ism fāʿil of نَقَفَ", "(çekirdeğini çıkarmak için Ebucehil karpuzunu) yaran kişi — نَقَفَ'nin ism-i fâili", 6, "ن ق ف"),
 "hanzal": G("حَنْظَل", "noun", "colocynth, the bitter desert gourd", "Ebucehil karpuzu, acı çöl kabağı", 5, "ح ن ظ ل"),
 "asan": G("أَسًى", "noun", "grief, sorrow (a maqṣūr masdar)", "üzüntü, keder (maksûr masdar)", 5, "أ س و"),
 "tajammala": G("تَجَمَّلَ", "verb", "to bear up with grace, to show fortitude (Form V)", "güzelce sabretmek, metanet göstermek (tefa''ul)", 5, "ج م ل", form="V"),
 "abra": G("عَبْرَة", "noun", "a tear, tears (pl. عَبَرَات)", "gözyaşı (çoğ. عَبَرَات)", 5, "ع ب ر", "عَبَرَات"),
 "muharaq": G("مُهَرَاق", "noun", "poured out, shed — ism mafʿūl of هَرَاقَ, a form of أَرَاقَ", "dökülmüş, akıtılmış — «أَرَاقَ»nın bir lügati olan هَرَاقَ'dan ism-i mef'ûl", 6, "ه ر ق"),
 "daris": G("دَارِس", "noun", "effaced, worn away (ism fāʿil of دَرَسَ)", "silinmiş, izi kalmamış (دَرَسَ'nin ism-i fâili)", 5, "د ر س"),
 "muawwal-reliance": G("مُعَوَّل", "noun", "what one leans on, a support to turn to; also: a place for weeping aloud", "dayanılan, güvenilip sığınılan şey; ayrıca: sesli ağlama yeri", 6, "ع و ل"),
 # ---- the night ----
 "arkha": G("أَرْخَى", "verb", "to let down, to let hang (a curtain, a rein)", "(perdeyi, dizgini) salıvermek, sarkıtmak", 5, "ر خ و", form="IV"),
 "sidl": G("سِدْل", "noun", "a curtain, a veil (pl. سُدُول)", "perde, örtü (çoğ. سُدُول)", 6, "س د ل", "سُدُول"),
 "sulb-back": G("صُلْب", "noun", "the backbone, the spine, the back", "bel kemiği, omurga, bel", 5, "ص ل ب"),
 "ardafa": G("أَرْدَفَ", "verb", "to make follow, to bring up behind (Form IV)", "ardından getirmek, peşine takmak (if'âl)", 5, "ر د ف", form="IV"),
 "kalkal": G("كَلْكَل", "noun", "the chest, the breast (pl. كَلَاكِل)", "göğüs (çoğ. كَلَاكِل)", 6, plural="كَلَاكِل"),
 "injala": G("اِنْجَلَى", "verb", "to clear away, to be lifted (of darkness, of grief) (Form VII)", "açılmak, dağılıp gitmek (karanlık, keder için) (infiâl)", 5, "ج ل و", form="VII"),
 "isbah": G("إِصْبَاح", "noun", "the breaking of morning, morning (masdar of أَصْبَحَ)", "sabah oluşu, sabah (أَصْبَحَ'nin masdarı)", 4, "ص ب ح"),
 "amthal": G("أَمْثَل", "noun", "better, more excellent (an elative; fem. مُثْلَى, pl. أَمَاثِل)", "daha iyi, daha üstün (ism-i tafdîl; müennesi مُثْلَى, çoğ. أَمَاثِل)", 5, "م ث ل"),
 "maras": G("مَرَس", "noun", "a rope (pl. أَمْرَاس)", "ip, halat (çoğ. أَمْرَاس)", 6, "م ر س", "أَمْرَاس"),
 "kattan": G("كَتَّان", "noun", "flax, linen", "keten", 5, "ك ت ن"),
 "jandal": G("جَنْدَل", "noun", "rock, boulders (pl. جَنَادِل)", "kaya, iri taşlar (çoğ. جَنَادِل)", 5, plural="جَنَادِل"),
 # ---- the horse ----
 "ightada": G("اِغْتَدَى", "verb", "to go out in the early morning — the same as غَدَا (Form VIII)", "sabah erkenden çıkmak — غَدَا ile aynı (iftiâl)", 5, "غ د و", form="VIII"),
 "wukna": G("وُكْنَة", "noun", "a bird's roost, where it settles for the night (pl. وُكُنَات)", "kuşun tünediği, gecelediği yer (çoğ. وُكُنَات)", 6, "و ك ن", "وُكُنَات"),
 "munjarid": G("مُنْجَرِد", "noun", "(of a horse) pressing on in his pace; or: short-haired, sleek", "(at için) yürüyüşünde atılgan; yahut: kısa tüylü", 6, "ج ر د"),
 "qayd": G("قَيْد", "noun", "a shackle, a fetter (pl. قُيُود)", "köstek, bukağı (çoğ. قُيُود)", 4, "ق ي د", "قُيُود"),
 "abida": G("آبِدَة", "noun", "a wild beast — pl. أَوَابِد, the wild game (from أَبَدَ «to run wild»)", "yaban hayvanı — çoğ. أَوَابِد, yabanî av hayvanları («yabanîleşmek» anlamındaki أَبَدَ'den)", 6, "أ ب د", "أَوَابِد"),
 "mikarr": G("مِكَرّ", "noun", "quick to wheel and charge — مِفْعَل from كَرَّ, a pattern that carries intensity", "dönüp saldırmaya pek yatkın — كَرَّ'den, mübalağa bildiren «مِفْعَل» vezninde", 6, "ك ر ر"),
 "mifarr": G("مِفَرّ", "noun", "quick to turn and flee — مِفْعَل from فَرَّ, a pattern that carries intensity", "dönüp kaçmaya pek yatkın — فَرَّ'den, mübalağa bildiren «مِفْعَل» vezninde", 6, "ف ر ر"),
 "muqbil": G("مُقْبِل", "noun", "coming on, advancing (ism fāʿil of أَقْبَلَ)", "ileri gelen, yönelen (أَقْبَلَ'nin ism-i fâili)", 4, "ق ب ل"),
 "mudbir": G("مُدْبِر", "noun", "turning back, retreating (ism fāʿil of أَدْبَرَ)", "geri dönen, arkasını dönen (أَدْبَرَ'nin ism-i fâili)", 4, "د ب ر"),
 "julmud": G("جُلْمُود", "noun", "a great hard rock, a boulder (pl. جَلَامِيد)", "büyük, sert kaya (çoğ. جَلَامِيد)", 6, plural="جَلَامِيد"),
 "sakhr-rock": G("صَخْر", "noun", "rock, stone (a collective; one: صَخْرَة; pl. صُخُور)", "kaya, taş (cins ismi; teki صَخْرَة; çoğ. صُخُور)", 3, "ص خ ر", "صُخُور"),
 "hatta-down": G("حَطَّ", "verb", "to throw down from a height, to bring down (حَطَّ يَحُطُّ)", "yukarıdan aşağı atmak, indirmek (حَطَّ يَحُطُّ)", 4, "ح ط ط", form="I"),
 "alu": G("عَلُ", "noun", "above, the top — مِنْ عَلُ: from above; when indefinite it is declined: مِنْ عَلٍ «from some high place»", "üst, yukarı — مِنْ عَلُ: yukarıdan; nekre olunca mu'rebdir: مِنْ عَلٍ «yüksek bir yerden»", 6, "ع ل و"),
 "kumayt": G("كُمَيْت", "noun", "a bay — a horse whose colour is between red and black", "doru — rengi kırmızı ile siyah arasında olan at", 6, "ك م ت"),
 "libd": G("لِبْد", "noun", "felt; the saddle-felt laid on a horse's back", "keçe; atın sırtına konan keçe", 5, "ل ب د"),
 "hal-back": G("حَال", "noun", "the middle of a horse's back, where the rider sits", "atın sırtının ortası, binicinin oturduğu yer", 6, "ح و ل"),
 "safwa": G("صَفْوَاء", "noun", "hard smooth rock (also صَفْوَان, صَفًا)", "sert, kaygan kaya (صَفْوَان, صَفًا da denir)", 6, "ص ف و"),
 "mutanazzil": G("مُتَنَزِّل", "noun", "coming down, alighting (ism fāʿil of تَنَزَّلَ)", "inen, konan (تَنَزَّلَ'nin ism-i fâili)", 5, "ن ز ل"),
 "dhabl": G("ذَبْل", "noun", "leanness, the drawing-in of the belly — the same as ذُبُول", "zayıflık, karnın çekikliği — ذُبُول ile aynı", 6, "ذ ب ل"),
 "jayyash": G("جَيَّاش", "noun", "seething, ever boiling up — an intensive of جَائِش", "coşkun, kaynayıp duran — جَائِش'in mübalağası", 6, "ج ي ش"),
 "ihtizam": G("اِهْتِزَام", "noun", "a broken, rumbling sound — here the horse's neighing breaking in his chest", "kesik kesik gürleyen ses — burada atın göğsünde kırılan kişnemesi", 6, "ه ز م"),
 "hamy": G("حَمْي", "noun", "heat (masdar of حَمِيَ)", "hararet, kızgınlık (حَمِيَ'nin masdarı)", 6, "ح م ي"),
 "ghaly": G("غَلْي", "noun", "boiling (masdar of غَلَى, of a pot)", "kaynama (tencere için غَلَى'nın masdarı)", 5, "غ ل ي"),
 "mirjal": G("مِرْجَل", "noun", "a cauldron, a cooking-pot of copper, iron or the like (pl. مَرَاجِل)", "kazan; bakır, demir ve benzerinden tencere (çoğ. مَرَاجِل)", 6, "ر ج ل", "مَرَاجِل"),
 "misahh": G("مِسَحّ", "noun", "one that pours forth (its run) gush after gush — مِفْعَل from سَحَّ «to pour»", "(koşusunu) döktükçe döken — «dökmek» anlamındaki سَحَّ'dan «مِفْعَل»", 6, "س ح ح"),
 "sabiha": G("سَابِحَة", "noun", "a «swimmer» — a horse that stretches out its forelegs as it runs (pl. سَابِحَات)", "«yüzen» — koşarken ön ayaklarını ileri uzatan at (çoğ. سَابِحَات)", 6, "س ب ح", "سَابِحَات"),
 "wanan": G("وَنًى", "noun", "flagging, weariness (masdar of وَنَى)", "gevşeme, yorgunluk (وَنَى'nın masdarı)", 6, "و ن ي"),
 "ghubar": G("غُبَار", "noun", "dust", "toz", 3, "غ ب ر"),
 "kadid": G("كَدِيد", "noun", "hard, low-lying ground", "sert, çukurca düz arazi", 6, "ك د د"),
 "murakkal": G("مُرَكَّل", "noun", "kicked again and again — ground beaten by hooves (ism mafʿūl of رَكَّلَ)", "tekrar tekrar tepilmiş — toynaklarla çiğnenmiş yer (رَكَّلَ'den ism-i mef'ûl)", 6, "ر ك ل"),
 "azalla": G("أَزَلَّ", "verb", "to make slip, to make slide off (Form IV of زَلَّ)", "kaydırmak, sürçtürmek (زَلَّ'nin if'âli)", 5, "ز ل ل", form="IV"),
 "khiff": G("خِفّ", "noun", "light — the same as خَفِيف", "hafif — خَفِيف ile aynı", 6, "خ ف ف"),
 "sahwa": G("صَهْوَة", "noun", "the rider's seat on a horse's back (pl. صَهَوَات)", "atın sırtında binicinin oturduğu yer (çoğ. صَهَوَات)", 6, "ص ه و", "صَهَوَات"),
 "alwa": G("أَلْوَى", "verb", "أَلْوَى بِالشَّيْءِ: to fling a thing away, to carry it off (Form IV)", "أَلْوَى بِالشَّيْءِ: bir şeyi fırlatıp atmak, alıp götürmek (if'âl)", 6, "ل و ي", form="IV"),
 "anif": G("عَنِيف", "noun", "rough, harsh — the opposite of the gentle; here a rider who is rough with his mount", "sert, kaba — yumuşak davrananın zıddı; burada bineğine sert davranan binici", 5, "ع ن ف"),
 "muthaqqal": G("مُثَقَّل", "noun", "heavy, weighed down (ism mafʿūl of ثَقَّلَ)", "ağır, ağırlaştırılmış (ثَقَّلَ'den ism-i mef'ûl)", 5, "ث ق ل"),
 # ---- the lightning and the rain ----
 "hamza-nida": G("أَ (النِّدَاء)", "part", "the hamza of calling — «O», for one who is near", "nidâ hemzesi — yakındakine «ey»", 5),
 "wamid": G("وَمِيض", "noun", "a flash, the flashing (of lightning)", "parıltı, (şimşeğin) çakışı", 6, "و م ض"),
 "habiyy": G("حَبِيّ", "noun", "a heaped cloud — cloud piled on cloud, as though part of it crawled up to part", "yığın yığın bulut — bir kısmı ötekine doğru emeklemiş gibi üst üste binen bulut", 6, "ح ب و"),
 "mukallal": G("مُكَلَّل", "noun", "crowned — of a cloud whose top is like a crown (إِكْلِيل) to what lies beneath it", "taçlı — tepesi altındakine taç (إِكْلِيل) gibi olmuş bulut", 6, "ك ل ل"),
 "adaa-shine": G("أَضَاءَ", "verb", "to shine, to give light; to light up (Form IV)", "parlamak, ışık vermek; aydınlatmak (if'âl)", 4, "ض و أ", form="IV"),
 "sanan-light": G("سَنًا", "noun", "light, gleam (with the short alif; سَنَاء, with the long, is «loftiness»)", "ışık, parıltı (maksûr; memdûd olan سَنَاء «yücelik» demektir)", 6, "س ن و"),
 "salit": G("سَلِيط", "noun", "oil — lamp-oil; sesame oil is also so called", "yağ — kandil yağı; susam yağına da denir", 6, "س ل ط"),
 "dhubal": G("ذُبَال", "noun", "wicks — the plural of ذُبَالَة", "fitiller — ذُبَالَة'nin cem'i", 6, "ذ ب ل"),
 "mufattal": G("مُفَتَّل", "noun", "tightly twisted (ism mafʿūl of فَتَّلَ)", "sıkıca bükülmüş (فَتَّلَ'den ism-i mef'ûl)", 5, "ف ت ل"),
 "darij": G("ضَارِج", "propn", "Ḍārij — a place", "Dâric — bir yer adı", 6),
 "mutaammal": G("مُتَأَمَّل", "noun", "the thing gazed at, what is watched (ism mafʿūl of تَأَمَّلَ)", "bakılan, seyredilen şey (تَأَمَّلَ'den ism-i mef'ûl)", 6, "أ م ل"),
 "qatan": G("قَطَن", "propn", "Qaṭan — a mountain", "Katan — bir dağ", 6),
 "shaym": G("شَيْم", "noun", "watching the lightning, to see where its rain will fall", "yağmurunun nereye düşeceğini kestirmek için şimşeği gözlemek", 6, "ش ي م"),
 "ayman": G("أَيْمَن", "noun", "the right-hand side, the rightmost part (opposite of أَيْسَر)", "sağ yan, en sağdaki kısım (أَيْسَر'in zıddı)", 5, "ي م ن"),
 "sitar": G("السِّتَار", "propn", "al-Sitār — a mountain", "Sitâr — bir dağ", 6),
 "yadhbul": G("يَذْبُل", "propn", "Yadhbul — a mountain (a diptote: a proper name on the pattern of a verb)", "Yezbül — bir dağ (gayr-i munsarif: fiil vezninde alem)", 6),
 "sahha-pour": G("سَحَّ", "verb", "to pour out (water); to pour down (سَحَّ يَسُحُّ)", "(suyu) dökmek; dökülmek (سَحَّ يَسُحُّ)", 5, "س ح ح", form="I"),
 "kutayfa": G("كُتَيْفَة", "propn", "Kutayfa — a place", "Küteyfe — bir yer adı", 6),
 "kabba": G("كَبَّ", "verb", "to throw (a thing) down on its face (كَبَّ يَكُبُّ)", "(bir şeyi) yüzüstü atmak, devirmek (كَبَّ يَكُبُّ)", 5, "ك ب ب", form="I"),
 "dawh": G("دَوْح", "noun", "great spreading trees — the plural of دَوْحَة", "ulu ağaçlar — دَوْحَة'nin cem'i", 6, "د و ح"),
 "kanahbal": G("كَنَهْبَل", "noun", "kanahbal — a kind of great desert tree (also read كَنَهْبُل)", "kenehbel — bir çeşit ulu çöl ağacı (كَنَهْبُل de okunur)", 6),
 "qanan": G("الْقَنَان", "propn", "al-Qanān — a mountain of the Banū Asad", "Kanân — Benî Esed'e ait bir dağ", 6),
 "nafayan": G("نَفَيَان", "noun", "what flies off — the spray of falling rain", "savrulan şey — yağan yağmurun serpintisi", 6, "ن ف ي"),
 "asam": G("أَعْصَم", "noun", "white-footed — an ibex with white on one foreleg (pl. عُصْم)", "sekili — ön ayaklarından birinde aklık bulunan dağ keçisi (çoğ. عُصْم)", 6, "ع ص م", "عُصْم"),
 # ---- verses 7–12 ----
 "dab": G("دَأْب", "noun", "habit, wont, way (masdar of دَأَبَ: to keep at a thing)", "âdet, hâl, tutum (bir işe devam etmek anlamındaki دَأَبَ'nin masdarı)", 5, "د أ ب"),
 "huwayrith": G("الْحُوَيْرِث", "propn", "al-Ḥuwayrith — in the kunya Umm al-Ḥuwayrith, a woman the poet names", "Huveyris — şairin andığı bir kadının künyesinde: Ümmü'l-Huveyris", 6),
 "jara-neighbour": G("جَارَة", "noun", "a woman neighbour (feminine of جَار)", "kadın komşu (جَار'ın müennesi)", 3, "ج و ر"),
 "rabab": G("الرَّبَاب", "propn", "al-Rabāb — in the kunya Umm al-Rabāb, a woman the poet names", "Rebâb — şairin andığı bir kadının künyesinde: Ümmü'r-Rebâb", 6),
 "masal": G("مَأْسَل", "propn", "Maʾsal — a particular mountain (with a fatha on the sin)", "Me'sel — belirli bir dağ (sîn'in fethasıyla)", 6),
 "tadawwaa": G("تَضَوَّعَ", "verb", "(of a scent) to spread, to be wafted abroad (Form V)", "(koku) yayılmak, etrafa dağılmak (tefa''ul)", 6, "ض و ع", form="V"),
 "nasim": G("نَسِيم", "noun", "a breeze, a gentle breath of wind", "esinti, hafif rüzgâr", 4, "ن س م"),
 "saba-wind": G("الصَّبَا", "noun", "the east wind (a maqṣūr noun)", "sabâ — doğudan esen rüzgâr (maksûr isim)", 5, "ص ب و"),
 "rayya": G("رَيَّا", "noun", "a sweet scent, fragrance", "güzel koku, râyiha", 6, "ر و ي"),
 "qaranful": G("قَرَنْفُل", "noun", "cloves", "karanfil (baharat)", 5),
 "sababa": G("صَبَابَة", "noun", "the tenderness of longing, ardent love", "özlemin inceliği, yanık sevda", 5, "ص ب ب"),
 "nahr-chest": G("نَحْر", "noun", "the top of the breast, where a necklace lies", "göğsün üst kısmı, gerdan", 5, "ن ح ر"),
 "balla": G("بَلَّ", "verb", "to wet, to moisten (بَلَّ يَبُلُّ)", "ıslatmak (بَلَّ يَبُلُّ)", 4, "ب ل ل", form="I"),
 "mihmal": G("مِحْمَل", "noun", "a sword-belt, the strap a sword hangs from (pl. مَحَامِل)", "kılıç kayışı, hamail (çoğ. مَحَامِل)", 6, "ح م ل", "مَحَامِل"),
 "siyy": G("سِيّ", "noun", "the like, the equal — لَا سِيَّمَا: «and none like…», especially", "benzer, denk — لَا سِيَّمَا: «hele…», özellikle", 5, "س و ي"),
 "dara-pool": G("دَارَة", "noun", "a round open place; دَارَةُ جُلْجُلٍ: Dārat Juljul, a particular pool", "yuvarlak açık alan; دَارَةُ جُلْجُلٍ: Dâretü Cülcül, belirli bir gölcük", 6, "د و ر"),
 "juljul": G("جُلْجُل", "propn", "Juljul — in Dārat Juljul, the pool of the poet's famous day", "Cülcül — şairin meşhur gününün geçtiği gölcüğün adında: Dâretü Cülcül", 6),
 "kur": G("كُور", "noun", "a camel's saddle with its gear (pl. أَكْوَار)", "takımlarıyla birlikte deve semeri (çoğ. أَكْوَار)", 6, "ك و ر", "أَكْوَار"),
 "mutahammal": G("مُتَحَمَّل", "noun", "carried, borne off (ism mafʿūl of تَحَمَّلَ)", "yüklenip taşınan (تَحَمَّلَ'den ism-i mef'ûl)", 6, "ح م ل"),
 "irtama": G("اِرْتَمَى", "verb", "to throw to one another; to throw oneself (Form VIII)", "birbirine atmak; atılmak (iftiâl)", 5, "ر م ي", form="VIII"),
 "huddab": G("هُدَّاب", "noun", "a fringe, the loose threads at the edge of a cloth", "saçak, kumaşın kenarından sarkan iplikler", 6, "ه د ب"),
 "dimaqs": G("دِمَقْس", "noun", "silk — or, it is said, white silk in particular", "ibrişim — «özellikle beyazı» da denmiştir", 6),
 # ---- verses 13–18 ----
 "khidr": G("خِدْر", "noun", "a woman's curtained quarters; here: the howdah, her litter on the camel (pl. خُدُور)", "kadının perdeli bölmesi; burada: mahfe, deve üzerindeki hevdec (çoğ. خُدُور)", 5, "خ د ر", "خُدُور"),
 "unayza": G("عُنَيْزَة", "propn", "ʿUnayza — the woman of the howdah; said to be the poet's cousin, or a nickname of Fāṭima (a diptote)", "Uneyze — mahfedeki kadın; şairin amcasının kızı olduğu, yahut Fâtıma'nın lakabı olduğu söylenir (gayr-i munsarif)", 6),
 "wayla": G("وَيْلَة", "noun", "woe, sore torment (pl. وَيْلَات) — لَكَ الْوَيْلَاتُ: «woe to you!»", "vay, şiddetli azap (çoğ. وَيْلَات) — لَكَ الْوَيْلَاتُ: «vay hâline!»", 5, "و ي ل", "وَيْلَات"),
 "murjil": G("مُرْجِل", "noun", "one who makes another go on foot (ism fāʿil of أَرْجَلَ)", "birini yaya bırakan (أَرْجَلَ'nin ism-i fâili)", 6, "ر ج ل"),
 "ghabit": G("غَبِيط", "noun", "a kind of camel-saddle, or of howdah", "bir çeşit deve semeri veya mahfe", 6, "غ ب ط"),
 "zimam": G("زِمَام", "noun", "a camel's rein, its nose-rope", "devenin yuları", 4, "ز م م"),
 "jana": G("جَنًى", "noun", "what is gathered from a tree, fruit ready for plucking", "ağaçtan derilen şey, derilecek meyve", 6, "ج ن ي"),
 "shiqq": G("شِقّ", "noun", "a half, one side of a thing", "yarım, bir şeyin bir yanı", 5, "ش ق ق"),
 "kathib": G("كَثِيب", "noun", "a dune, a great heap of sand (pl. كُثْبَان)", "kum tepesi, büyük kum yığını (çoğ. كُثْبَان)", 5, "ك ث ب", "كُثْبَان"),
 "halfa": G("حَلْفَة", "noun", "an oath, a single swearing", "bir yemin, bir kere yemin etme", 5, "ح ل ف"),
 "tahallala": G("تَحَلَّلَ", "verb", "to free oneself; (in an oath) to make an exception that looses it (Form V)", "çözülmek; (yeminde) onu çözen bir istisna yapmak (tefa''ul)", 6, "ح ل ل", form="V"),
 # ---- verses 19–25 ----
 "mahl": G("مَهْل", "noun", "gentleness, going slowly — مَهْلًا: «gently!»", "yavaşlık, acele etmeme — مَهْلًا: «yavaş ol!»", 4, "م ه ل"),
 "tadallul": G("تَدَلُّل", "noun", "coquetry — presuming on being loved (masdar of تَدَلَّلَ)", "naz — sevildiğine güvenerek nazlanma (تَدَلَّلَ'nin masdarı)", 5, "د ل ل"),
 "sarm": G("صَرْم", "noun", "cutting off, breaking with someone (masdar of صَرَمَ)", "ilişkiyi kesme, terk etme (صَرَمَ'nin masdarı)", 6, "ص ر م"),
 "ajmala": G("أَجْمَلَ", "verb", "to act graciously, to do a thing handsomely (Form IV)", "güzel davranmak, bir işi güzellikle yapmak (if'âl)", 5, "ج م ل", form="IV"),
 "gharra": G("غَرَّ", "verb", "to deceive, to embolden falsely (غَرَّ يَغُرُّ)", "aldatmak, şımartıp cüretlendirmek (غَرَّ يَغُرُّ)", 4, "غ ر ر", form="I"),
 "salla-draw": G("سَلَّ", "verb", "to draw (a thing) gently out of another (سَلَّ يَسُلُّ)", "bir şeyi başka bir şeyin içinden usulca çekip çıkarmak (سَلَّ يَسُلُّ)", 5, "س ل ل", form="I"),
 "nasala": G("نَسَلَ", "verb", "(of feathers, fur, a garment) to fall out, to slip off (نَسَلَ يَنْسُلُ)", "(tüy, yün, elbise) dökülmek, sıyrılıp düşmek (نَسَلَ يَنْسُلُ)", 6, "ن س ل", form="I"),
 "dharafa": G("ذَرَفَ", "verb", "(of tears) to flow; (of an eye) to shed tears (ذَرَفَ يَذْرِفُ)", "(gözyaşı) akmak; (göz) yaş dökmek (ذَرَفَ يَذْرِفُ)", 5, "ذ ر ف", form="I"),
 "ashar-pieces": G("أَعْشَار", "noun", "pieces, fragments (of a broken pot); or tenths, the ten shares of the maysir camel", "parçalar, kırıklar; yahut onda birler — meysir devesinin on payı", 6, "ع ش ر"),
 "muqattal": G("مُقَتَّل", "noun", "utterly subdued, broken in (ism mafʿūl of قَتَّلَ)", "iyice boyun eğdirilmiş (قَتَّلَ'den ism-i mef'ûl)", 6, "ق ت ل"),
 "rama-seek": G("رَامَ", "verb", "to seek, to make for (رَامَ يَرُومُ)", "istemek, kastetmek, ulaşmaya çalışmak (رَامَ يَرُومُ)", 5, "ر و م", form="I"),
 "mujal": G("مُعْجَل", "noun", "hurried, hastened away (ism mafʿūl of أَعْجَلَ)", "acele ettirilmiş (أَعْجَلَ'den ism-i mef'ûl)", 5, "ع ج ل"),
 "haris-guard": G("حَارِس", "noun", "a guard, a watchman (pl. أَحْرَاس, حَرَس)", "bekçi, muhafız (çoğ. أَحْرَاس, حَرَس)", 4, "ح ر س", "أَحْرَاس"),
 "law-masdariyya": G("لَوْ (الْمَصْدَرِيَّة)", "part", "the masdar-making لَوْ — «that», after words of wishing or eagerness", "masdariyye لَوْ — arzu ve hırs bildiren kelimelerden sonra «-mesini»", 5),
 "thiny": G("ثِنْي", "noun", "a fold, a bend, a side (pl. أَثْنَاء)", "kıvrım, büklüm, yan (çoğ. أَثْنَاء)", 6, "ث ن ي", "أَثْنَاء"),
 "wishah": G("وِشَاح", "noun", "a sash set with gems, worn by a woman across the body", "kadının çaprazlama taktığı taşlı kuşak", 6, "و ش ح"),
 # ---- verses 26–31 ----
 "nadda": G("نَضَّى", "verb", "to strip off (clothes) — the intensive of نَضَا (Form II)", "(elbiseyi) sıyırıp çıkarmak — نَضَا'nın mübalağası (tef'îl)", 6, "ن ض و", form="II"),
 "sitr": G("سِتْر", "noun", "a curtain, a screen (pl. سُتُور)", "perde, örtü (çoğ. سُتُور)", 4, "س ت ر", "سُتُور"),
 "libsa": G("لِبْسَة", "noun", "a manner of dress (a noun of manner from لَبِسَ)", "giyiniş biçimi (لَبِسَ'den ism-i hey'et)", 6, "ل ب س"),
 "ghawaya": G("غَوَايَة", "noun", "going astray, folly (masdar of غَوِيَ)", "sapkınlık, azgınlık (غَوِيَ'nin masdarı)", 5, "غ و ي"),
 "dhayl": G("ذَيْل", "noun", "the skirt of a garment, its trailing end (pl. أَذْيَال, ذُيُول)", "etek, elbisenin yerde sürünen ucu (çoğ. أَذْيَال, ذُيُول)", 4, "ذ ي ل", "أَذْيَال"),
 "mirt": G("مِرْط", "noun", "a woman's wrap of silk-wool or of wool (pl. مُرُوط)", "ipekli veya yünlü kadın örtüsü (çoğ. مُرُوط)", 6, "م ر ط", "مُرُوط"),
 "murahhal": G("مُرَحَّل", "noun", "(of cloth) worked with figures like camel-saddles", "(kumaş) deve semerlerine benzer nakışlarla işlenmiş", 6, "ر ح ل"),
 "ajaza-cross": G("أَجَازَ", "verb", "to cross, to pass through (a place) — the same as جَازَ (Form IV)", "(bir yeri) geçmek, aşmak — جَازَ ile aynı (if'âl)", 5, "ج و ز", form="IV"),
 "saha-court": G("سَاحَة", "noun", "an open space among the tents, a courtyard (pl. سَاحَات)", "çadırlar arasındaki meydan, avlu (çoğ. سَاحَات)", 4, "س و ح", "سَاحَات"),
 "intaha-lean": G("اِنْتَحَى", "verb", "to lean on, to bear towards; اِنْتَحَى بِهِ: to turn aside with him (Form VIII)", "yaslanmak, yönelmek; اِنْتَحَى بِهِ: onu bir yana çekmek (iftiâl)", 6, "ن ح و", form="VIII"),
 "khabt-ground": G("خَبْت", "noun", "low, level ground", "alçak, düz arazi", 6, "خ ب ت"),
 "aqanqal": G("عَقَنْقَل", "noun", "sand knotted and banked together", "birbirine girip kümelenmiş kum", 6, "ع ق ل"),
 "hasara-pull": G("هَصَرَ", "verb", "to pull, to draw (a bough, a head) down towards oneself (هَصَرَ يَهْصِرُ)", "(dalı, başı) kendine doğru çekmek (هَصَرَ يَهْصِرُ)", 6, "ه ص ر", form="I"),
 "fawd": G("فَوْد", "noun", "the side of the head (dual فَوْدَانِ)", "başın yanı (tesniyesi فَوْدَانِ)", 6, "ف و د"),
 "tamayala": G("تَمَايَلَ", "verb", "to sway, to lean over (Form VI)", "salınmak, eğilmek (tefâul)", 5, "م ي ل", form="VI"),
 "hadim": G("هَضِيم", "noun", "slender, drawn in — هَضِيمُ الْكَشْحِ: slim-waisted (فَعِيل in the sense of مَفْعُول)", "ince, içe çekik — هَضِيمُ الْكَشْحِ: ince belli (mef'ûl anlamında فَعِيل)", 6, "ه ض م"),
 "mukhalkhal": G("مُخَلْخَل", "noun", "the place of the anklet on the leg", "bacakta halhalın takıldığı yer", 6, "خ ل خ ل"),
 "muhafhaf": G("مُهَفْهَف", "noun", "slim of waist, flat of belly (fem. مُهَفْهَفَة)", "ince belli, karnı çekik (müennesi مُهَفْهَفَة)", 6, "ه ف ه ف"),
 "mufad": G("مُفَاض", "noun", "(of a woman, fem. مُفَاضَة) big-bellied, loose of flesh", "(kadın için, müennesi مُفَاضَة) karnı büyük, eti sarkık", 6, "ف ي ض"),
 "tariba": G("تَرِيبَة", "noun", "the top of the breast, where the necklace lies (pl. تَرَائِب)", "göğsün üstü, gerdanlığın durduğu yer (çoğ. تَرَائِب)", 6, "ت ر ب", "تَرَائِب"),
 "sajanjal": G("سَجَنْجَل", "noun", "a mirror (a Greek word made Arabic)", "ayna (Arapçalaşmış Rumca bir kelime)", 6),
 "kashh": G("كَشْح", "noun", "the flank, between the last rib and the hip; the waist (pl. كُشُوح)", "böğür, son kaburga ile kalça arası; bel (çoğ. كُشُوح)", 6, "ك ش ح", "كُشُوح"),
 # ---- verses 32–37 ----
 "bikr": G("بِكْر", "noun", "the first of its kind, what nothing like it came before; a virgin", "türünün ilki, kendinden önce benzeri gelmemiş olan; bâkire", 5, "ب ك ر"),
 "muqanat": G("مُقَانَاة", "noun", "mingled, blended in colour (fem. ism mafʿūl of قَانَى)", "rengi karıştırılmış (قَانَى'dan müennes ism-i mef'ûl)", 6, "ق ن و"),
 "sufra": G("صُفْرَة", "noun", "yellowness, a yellow tinge", "sarılık, sarı renk", 4, "ص ف ر"),
 "ghadha": G("غَذَا", "verb", "to nourish, to feed (غَذَا يَغْذُو)", "beslemek (غَذَا يَغْذُو)", 5, "غ ذ و", form="I"),
 "namir": G("نَمِير", "noun", "sweet, wholesome water", "tatlı, bedene yarayan su", 6, "ن م ر"),
 "muhallal": G("مُحَلَّل", "noun", "(of water) much alighted at, and so muddied", "(su için) çok konulup bulandırılmış", 6, "ح ل ل"),
 "asil-cheek": G("أَسِيل", "noun", "(of a cheek) long and smooth", "(yanak için) uzun ve düzgün", 6, "أ س ل"),
 "nazira": G("نَاظِرَة", "noun", "an eye that looks, a glancing eye (fem. ism fāʿil of نَظَرَ)", "bakan göz (نَظَرَ'nin müennes ism-i fâili)", 5, "ن ظ ر"),
 "wajra": G("وَجْرَة", "propn", "Wajra — a place known for its wild game (a diptote)", "Vecre — yaban hayvanlarıyla bilinen bir yer (gayr-i munsarif)", 6),
 "mutfil": G("مُطْفِل", "noun", "(a gazelle, a wild cow) that has a young one", "yavrusu olan (ceylan, yaban sığırı)", 6, "ط ف ل"),
 "jid": G("جِيد", "noun", "the neck (pl. أَجْيَاد)", "boyun (çoğ. أَجْيَاد)", 5, "ج ي د", "أَجْيَاد"),
 "nassa": G("نَصَّ", "verb", "to raise, to lift up (نَصَّ يَنُصُّ)", "kaldırmak, yükseltmek (نَصَّ يَنُصُّ)", 5, "ن ص ص", form="I"),
 "far-hair": G("فَرْع", "noun", "a full head of hair (pl. فُرُوع)", "gür ve uzun saç (çoğ. فُرُوع)", 6, "ف ر ع", "فُرُوع"),
 "fahim": G("فَاحِم", "noun", "jet-black (from الفَحْم, charcoal)", "simsiyah, kömür karası (الفَحْم'den)", 5, "ف ح م"),
 "athith": G("أَثِيث", "noun", "thick, abundant (of hair, of plants)", "gür, sık (saç, bitki için)", 6, "أ ث ث"),
 "qinw": G("قِنْو", "noun", "the fruit-stalk of a date-palm with its clusters (pl. قِنْوَان, أَقْنَاء)", "hurma hevengi (çoğ. قِنْوَان, أَقْنَاء)", 6, "ق ن و", "قِنْوَان"),
 "mutaathkil": G("مُتَعَثْكِل", "noun", "hung with clusters, with its bunches out", "salkım salkım olmuş, salkımları çıkmış", 6, "ع ث ك ل"),
 "ghadira": G("غَدِيرَة", "noun", "a lock, a tress of hair (pl. غَدَائِر)", "saç lülesi, zülüf (çoğ. غَدَائِر)", 6, "غ د ر", "غَدَائِر"),
 "mustashzir": G("مُسْتَشْزِر", "noun", "twisted and rising upwards (with a fatha on the zay: raised up)", "bükülüp yukarı yükselmiş (zây'ın fethasıyla: yukarı kaldırılmış)", 6, "ش ز ر"),
 "aqisa": G("عَقِيصَة", "noun", "a gathered, plaited lock of hair (pl. عِقَاص, عَقَائِص)", "toplanıp örülmüş saç tutamı (çoğ. عِقَاص, عَقَائِص)", 6, "ع ق ص", "عِقَاص"),
 "jadil": G("جَدِيل", "noun", "a rein plaited of leather (pl. جُدُل)", "deriden örülmüş yular (çoğ. جُدُل)", 6, "ج د ل"),
 "mukhassar": G("مُخَصَّر", "noun", "narrow in the middle, slim-waisted", "ortası ince, dar belli", 6, "خ ص ر"),
 "unbub": G("أُنْبُوب", "noun", "the length of a reed between two knots (pl. أَنَابِيب)", "kamışın iki boğumu arası (çoğ. أَنَابِيب)", 6, "ن ب ب", "أَنَابِيب"),
 "saqiyy": G("سَقِيّ", "noun", "watered (فَعِيل in the sense of مَسْقِيّ) — of palms, of papyrus", "sulanmış (مَسْقِيّ anlamında فَعِيل) — hurmalık, berdî için", 6, "س ق ي"),
 "mudhallal": G("مُذَلَّل", "noun", "bent low, made easy to reach — of palm-boughs bowed by fruit", "eğdirilmiş, kolay erişilir kılınmış — meyveden eğilmiş hurma dalları için", 6, "ذ ل ل"),
 # ---- verses 38–43 ----
 "fatit": G("فَتِيت", "noun", "crumbs, fine bits got by crumbling (also فُتَات)", "kırıntı, ufalanarak oluşan parçacıklar (فُتَات da denir)", 6, "ف ت ت"),
 "nauum": G("نَؤُوم", "noun", "a heavy sleeper, one who sleeps much (intensive فَعُول; masc. and fem. alike)", "çok uyuyan (mübalağa sîgası فَعُول; müzekker ve müennes aynı)", 6, "ن و م"),
 "intataqa": G("اِنْتَطَقَ", "verb", "to gird oneself, to bind the waist with a girdle (Form VIII)", "kuşak kuşanmak, beline kuşak bağlamak (iftiâl)", 6, "ن ط ق", form="VIII"),
 "ata-reach": G("عَطَا", "verb", "to reach for, to take with the hand (عَطَا يَعْطُو)", "uzanıp almak (عَطَا يَعْطُو)", 6, "ع ط و", form="I"),
 "rakhs": G("رَخْص", "noun", "soft, tender (of fingers, of a body)", "yumuşak, körpe (parmak, beden için)", 6, "ر خ ص"),
 "shathn": G("شَثْن", "noun", "thick and rough (of hands, of fingers)", "kalın ve sert (el, parmak için)", 6, "ش ث ن"),
 "usru": G("أُسْرُوع", "noun", "a small worm of herbs and damp ground, to which fingers are likened (pl. أَسَارِيع; also يُسْرُوع)", "sebzelerde ve nemli yerlerde bulunan kurtçuk; parmaklar ona benzetilir (çoğ. أَسَارِيع; يُسْرُوع da denir)", 6, "س ر ع", "أَسَارِيع"),
 "zaby-place": G("ظَبْي", "propn", "Ẓaby — a particular place (so al-Zawzanī)", "Zaby — belirli bir yer adı (Zevzenî)", 6),
 "miswak": G("مِسْوَاك", "noun", "a toothstick (pl. مَسَاوِيك)", "misvak (çoğ. مَسَاوِيك)", 4, "س و ك", "مَسَاوِيك"),
 "ishil": G("إِسْحِل", "noun", "a tree with thin, straight twigs, used for toothsticks", "dalları ince ve düzgün, misvak yapılan bir ağaç", 6, "س ح ل"),
 "manara": G("مَنَارَة", "noun", "a lamp, a lamp-stand (pl. مَنَاوِر, مَنَائِر); (elsewhere) a minaret, a lighthouse", "kandil, kandillik (çoğ. مَنَاوِر, مَنَائِر); (başka yerde) minare, fener", 5, "ن و ر", "مَنَاوِر"),
 "mumsa": G("مُمْسًى", "noun", "the evening, coming into the evening (a maqṣūr noun, from أَمْسَى)", "akşam vakti, akşama girme (أَمْسَى'dan maksûr isim)", 6, "م س و"),
 "rana": G("رَنَا", "verb", "to gaze long and steadily (رَنَا يَرْنُو إِلَيْهِ)", "uzun uzun, gözünü ayırmadan bakmak (رَنَا يَرْنُو إِلَيْهِ)", 6, "ر ن و", form="I"),
 "isbakarra": G("اِسْبَكَرَّ", "verb", "to stretch out, to grow tall and straight (a quadriliteral on اِفْعَلَلَّ)", "uzayıp serpilmek, boy atmak (اِفْعَلَلَّ vezninde rubâî)", 6, "س ب ك ر"),
 "mijwal": G("مِجْوَل", "noun", "a garment worn by a little girl", "küçük kız çocuğunun giydiği elbise", 6, "ج و ل"),
 "tasalla": G("تَسَلَّى", "verb", "to be consoled, to get over a love or a grief (Form V)", "teselli bulmak, bir sevgiyi ya da üzüntüyü unutmak (tefa''ul)", 5, "س ل و", form="V"),
 "amaya": G("عَمَايَة", "noun", "blindness; error, the folly of passion (pl. عَمَايَات)", "körlük; sapkınlık, sevda gafleti (çoğ. عَمَايَات)", 6, "ع م ي", "عَمَايَات"),
 "munsal": G("مُنْسَلٍ", "noun", "one who gets over a love, consoled (ism fāʿil of اِنْسَلَى)", "sevgisini unutan, teselli bulan (اِنْسَلَى'dan ism-i fâil)", 6, "س ل و"),
 "alwa-contentious": G("أَلْوَى", "noun", "fierce in dispute, stubborn (an adjective on أَفْعَل)", "husumeti şiddetli, çetin (أَفْعَل vezninde sıfat)", 6, "ل و ي"),
 "nasih-sincere": G("نَصِيح", "noun", "a sincere adviser (= نَاصِح)", "içtenlikle öğüt veren (= نَاصِح)", 5, "ن ص ح"),
 "tadhal": G("تَعْذَال", "noun", "blame, reproach (a masdar, like العَذْل)", "kınama, azarlama (العَذْل gibi masdar)", 6, "ع ذ ل"),
 "mutal": G("مُؤْتَلٍ", "noun", "one who falls short, who spares effort (ism fāʿil of اِئْتَلَى)", "kusur eden, çabayı esirgeyen (اِئْتَلَى'dan ism-i fâil)", 6, "أ ل و"),
 # ---- verses 48–51 ----
 "qirba": G("قِرْبَة", "noun", "a water-skin (pl. قِرَب)", "kırba, su tulumu (çoğ. قِرَب)", 5, "ق ر ب", "قِرَب"),
 "isam": G("عِصَام", "noun", "the strap or tie of a water-skin (pl. عُصُم)", "kırbanın bağı, askısı (çoğ. عُصُم)", 6, "ع ص م", "عُصُم"),
 "dhalul": G("ذَلُول", "noun", "tractable, broken in (of a mount; pl. ذُلُل)", "uysal, alıştırılmış (binek için; çoğ. ذُلُل)", 5, "ذ ل ل", "ذُلُل"),
 "murahhal": G("مُرَحَّل", "noun", "saddled again and again (ism mafʿūl of رَحَّلَ)", "defalarca semer vurulmuş (رَحَّلَ'den ism-i mef'ûl)", 6, "ر ح ل"),
 "qafr": G("قَفْر", "noun", "an empty, desolate place (pl. قِفَار)", "boş, ıssız yer (çoğ. قِفَار)", 5, "ق ف ر", "قِفَار"),
 "awa": G("عَوَى", "verb", "to howl (of a wolf, a dog; عَوَى يَعْوِي)", "ulumak (kurt, köpek için; عَوَى يَعْوِي)", 5, "ع و ي", form="I"),
 "khali-outcast": G("خَلِيع", "noun", "one cast off by his people for his wickedness; here, a gambler", "kötülüğü yüzünden ailesinin el çektiği kimse; burada: kumarbaz", 6, "خ ل ع"),
 "muayyal": G("مُعَيَّل", "noun", "one with a large household to feed", "çoluk çocuğu çok olan", 6, "ع ي ل"),
 "tamawwala": G("تَمَوَّلَ", "verb", "to come to have wealth (Form V)", "mal sahibi olmak (tefa''ul)", 5, "م و ل", form="V"),
 "afata": G("أَفَاتَ", "verb", "to make a thing escape, to let it slip (Form IV of فَاتَ)", "elden kaçırmak, yitirmek (فَاتَ'nin if'âli)", 6, "ف و ت", form="IV"),
 "ihtaratha": G("اِحْتَرَثَ", "verb", "to till; to strive and earn (Form VIII, = حَرَثَ)", "ekip biçmek; çalışıp kazanmak (iftiâl, = حَرَثَ)", 6, "ح ر ث", form="VIII"),
 "hazala": G("هَزَلَ", "verb", "to grow lean; to fall into want (هَزَلَ يَهْزُلُ)", "zayıflamak; yoksul düşmek (هَزَلَ يَهْزُلُ)", 6, "ه ز ل", form="I"),
 # ---- verses 58–63 ----
 "darir": G("دَرِير", "noun", "(of a horse) running in a steady, unbroken flow", "(at için) koşusunu kesintisiz sürdüren", 6, "د ر ر"),
 "khudhruf": G("خُذْرُوف", "noun", "a boy's whirligig: a pierced pebble whirled on a string (pl. خَذَارِيف)", "çocuk fırıldağı: ipe geçirilip çevrilen delikli taş (çoğ. خَذَارِيف)", 6, "خ ذ ر ف", "خَذَارِيف"),
 "amarra": G("أَمَرَّ", "verb", "to twist (a rope) tight (Form IV, doubled)", "(ipi) sımsıkı bükmek (if'âl, muzâaf)", 6, "م ر ر", form="IV"),
 "tatabu": G("تَتَابُع", "noun", "following one upon another, succession (masdar of تَتَابَعَ)", "ardı ardına gelme (تَتَابَعَ'nin masdarı)", 4, "ت ب ع"),
 "khayt": G("خَيْط", "noun", "a thread, a string (pl. خُيُوط)", "ip, iplik (çoğ. خُيُوط)", 2, "خ ي ط", "خُيُوط"),
 "muwassal": G("مُوَصَّل", "noun", "joined together, knotted piece to piece (ism mafʿūl of وَصَّلَ)", "birbirine eklenmiş (وَصَّلَ'den ism-i mef'ûl)", 5, "و ص ل"),
 "aytal": G("أَيْطَل", "noun", "the flank (pl. أَيَاطِل; also إِطْل)", "böğür (çoğ. أَيَاطِل; إِطْل da denir)", 6, "أ ط ل", "أَيَاطِل"),
 "naama": G("نَعَامَة", "noun", "an ostrich (pl. نَعَام)", "devekuşu (çoğ. نَعَام)", 4, "ن ع م", "نَعَام"),
 "irkha": G("إِرْخَاء", "noun", "a loping gait of the wolf; (elsewhere) letting down, loosening", "kurdun rahvan gibi koşusu; (başka yerde) salıverme, gevşetme", 6, "ر خ و"),
 "sirhan": G("سِرْحَان", "noun", "a wolf (pl. سَرَاحِين)", "kurt (çoğ. سَرَاحِين)", 6, "س ر ح", "سَرَاحِين"),
 "tatful": G("تَتْفُل", "noun", "a fox-cub", "tilki yavrusu", 6, "ت ف ل"),
 "dali": G("ضَلِيع", "noun", "big in the ribs, full in the sides; sturdy", "kaburgaları iri, yanları dolgun; güçlü", 6, "ض ل ع"),
 "istadbara": G("اِسْتَدْبَرَ", "verb", "to look at from behind; to come at from the rear (Form X)", "arkasından bakmak; arkadan gelmek (istif'âl)", 6, "د ب ر", form="X"),
 "farj-gap": G("فَرْج", "noun", "a gap, an opening; the space between a horse's legs (pl. فُرُوج)", "açıklık, aralık; atın bacakları arası (çoğ. فُرُوج)", 6, "ف ر ج", "فُرُوج"),
 "dafin-full": G("ضَافٍ", "noun", "full, ample, long (of a tail, a garment; manqūṣ)", "bol, gür, uzun (kuyruk, elbise için; menkūs)", 6, "ض ف و"),
 "fuwayqa": G("فُوَيْقَ", "noun", "just above (the diminutive of فَوْقَ)", "hemen üstünde (فَوْقَ'nın tasgîri)", 6, "ف و ق"),
 "azal-tail": G("أَعْزَل", "noun", "(a horse) whose tail-bone leans to one side; (elsewhere) unarmed", "kuyruk kemiği bir yana eğik (at); (başka yerde) silahsız", 6, "ع ز ل"),
 "madak": G("مَدَاك", "noun", "a stone for grinding perfume", "koku ezilen taş", 6, "د و ك"),
 "arus": G("عَرُوس", "noun", "a bride (also a bridegroom; pl. عَرَائِس)", "gelin (damat için de kullanılır; çoğ. عَرَائِس)", 3, "ع ر س", "عَرَائِس"),
 "salaya": G("صَلَايَة", "noun", "a smooth slab for pounding (colocynth seed, perfume)", "üzerinde (Ebucehil karpuzu çekirdeği, koku) dövülen düz taş", 6, "ص ل ي"),
 "hadiya-foremost": G("هَادِيَة", "noun", "one that goes in front, the foremost of a herd (pl. هَادِيَات, هَوَادٍ)", "önde giden, sürünün öndeki hayvanı (çoğ. هَادِيَات, هَوَادٍ)", 6, "ه د ي", "هَادِيَات"),
 "usara": G("عُصَارَة", "noun", "juice, what is pressed out of a thing", "usâre, sıkılarak çıkarılan su", 5, "ع ص ر"),
 "hinna": G("حِنَّاء", "noun", "henna", "kına", 4, "ح ن أ"),
 "murajjal": G("مُرَجَّل", "noun", "combed out (ism mafʿūl of رَجَّلَ)", "taranmış (رَجَّلَ'den ism-i mef'ûl)", 6, "ر ج ل"),
 "sirb": G("سِرْب", "noun", "a herd, a flock (of gazelles, wild cows, birds; pl. أَسْرَاب)", "sürü (ceylan, yaban sığırı, kuş; çoğ. أَسْرَاب)", 5, "س ر ب", "أَسْرَاب"),
 "dawar": G("دَوَار", "propn", "Dawār — a stone the pagan Arabs set up and circled", "Devâr — Câhiliye Araplarının dikip etrafında döndüğü taş", 6),
 "mulaa": G("مُلَاءَة", "noun", "a wrap of two pieces sewn together (pl. مُلَاء)", "iki parçadan dikilmiş örtü, çarşaf (çoğ. مُلَاء)", 6, "م ل أ", "مُلَاء"),
 # ---- verses 64–69 ----
 "adbara": G("أَدْبَرَ", "verb", "to turn back, to turn and flee (Form IV)", "arkasını dönmek, dönüp kaçmak (if'âl)", 3, "د ب ر", form="IV"),
 "jiz-beads": G("جِزْع", "noun", "the Yemeni bead, onyx — black at the ends and white between (also جَزْع)", "Yemen boncuğu, oniks — uçları siyah, ortası beyaz (جَزْع da denir)", 6, "ج ز ع"),
 "muamm": G("مُعَمّ", "noun", "one whose paternal uncles are noble (irregular, from أَعَمَّ)", "amcaları soylu olan (أَعَمَّ'den, şâz)", 6, "ع م م"),
 "mukhwal": G("مُخْوَل", "noun", "one whose maternal uncles are noble (irregular, from أَخْوَلَ)", "dayıları soylu olan (أَخْوَلَ'den, şâz)", 6, "خ و ل"),
 "jahira": G("جَاحِرَة", "noun", "one that lags behind the herd (pl. جَوَاحِر)", "sürünün gerisinde kalan (çoğ. جَوَاحِر)", 6, "ج ح ر", "جَوَاحِر"),
 "sarra-herd": G("صَرَّة", "noun", "a company, a close herd; a cry", "topluluk, sıkışık sürü; çığlık", 6, "ص ر ر"),
 "zayyala": G("زَيَّلَ", "verb", "to scatter, to part asunder (Form II)", "dağıtmak, birbirinden ayırmak (tef'îl)", 6, "ز ي ل", form="II"),
 "tahin": G("طَاهٍ", "noun", "a cook (ism fāʿil of طَهَا; pl. طُهَاة)", "aşçı, et pişiren (طَهَا'dan ism-i fâil; çoğ. طُهَاة)", 6, "ط ه و", "طُهَاة"),
 "mundij": G("مُنْضِج", "noun", "one who cooks (meat) through, by boiling or roasting (ism fāʿil of أَنْضَجَ)", "(eti) haşlayarak ya da kızartarak pişiren (أَنْضَجَ'den ism-i fâil)", 5, "ن ض ج"),
 "safif": G("صَفِيف", "noun", "meat laid in rows on hot stones to roast", "kızarsın diye kızgın taşlara dizilmiş et", 6, "ص ف ف"),
 "shiwa": G("شِوَاء", "noun", "roast meat", "kebap, kızartılmış et", 4, "ش و ي"),
 "qadir-stew": G("قَدِير", "noun", "meat cooked in the pot, a stew (فَعِيل in the sense of مَقْدُور)", "tencerede pişirilmiş et, yahni (مَقْدُور anlamında فَعِيل)", 6, "ق د ر"),
 "muajjal-hasty": G("مُعَجَّل", "noun", "hurried, made ready in haste (ism mafʿūl of عَجَّلَ)", "aceleyle hazırlanmış (عَجَّلَ'den ism-i mef'ûl)", 4, "ع ج ل"),
 "taraqqa": G("تَرَقَّى", "verb", "to climb, to go up step by step (Form V)", "yükselmek, basamak basamak çıkmak (tefa''ul)", 5, "ر ق ي", form="V"),
 "tasaffala": G("تَسَفَّلَ", "verb", "to go down, to sink low (Form V)", "aşağı inmek, alçalmak (tefa''ul)", 5, "س ف ل", form="V"),
 "lijam": G("لِجَام", "noun", "a bridle, a bit (pl. لُجُم)", "gem, dizgin (çoğ. لُجُم)", 3, "ل ج م", "لُجُم"),
 # ---- verses 76–81 ----
 "tayma": G("تَيْمَاء", "propn", "Taymāʾ — an ancient town in the north of Arabia (a diptote)", "Teymâ — Arabistan'ın kuzeyinde çok eski bir kasaba (gayr-i munsarif)", 6),
 "jidh": G("جِذْع", "noun", "the trunk of a palm (pl. جُذُوع, أَجْذَاع)", "hurma kütüğü, gövdesi (çoğ. جُذُوع, أَجْذَاع)", 4, "ج ذ ع", "جُذُوع"),
 "utum": G("أُطُم", "noun", "a tower, a strong high house (pl. آطَام)", "köşk, yüksek müstahkem yapı (çoğ. آطَام)", 6, "أ ط م", "آطَام"),
 "mashid": G("مَشِيد", "noun", "built high; plastered (ism mafʿūl of شَادَ يَشِيدُ)", "yükseltilmiş; kireçle sıvanmış (شَادَ يَشِيدُ'den ism-i mef'ûl)", 5, "ش ي د"),
 "jandal": G("جَنْدَل", "noun", "rock, boulders (pl. جَنَادِل)", "kaya, iri taş (çoğ. جَنَادِل)", 6, "ج ن د ل", "جَنَادِل"),
 "thabir": G("ثَبِير", "propn", "Thabīr — a mountain", "Sebîr — bir dağ", 6),
 "irnin": G("عِرْنِين", "noun", "the nose, its upper part; (borrowed) the first of a thing (pl. عَرَانِين)", "burun, burnun üst kısmı; (istiâre ile) bir şeyin başı (çoğ. عَرَانِين)", 6, "ع ر ن", "عَرَانِين"),
 "bijad": G("بِجَاد", "noun", "a striped cloak (pl. بُجُد)", "çizgili aba (çoğ. بُجُد)", 6, "ب ج د", "بُجُد"),
 "muzammal": G("مُزَمَّل", "noun", "wrapped up in a garment (ism mafʿūl of زَمَّلَ)", "elbiseye sarınmış (زَمَّلَ'den ism-i mef'ûl)", 5, "ز م ل"),
 "dhirwa": G("ذُرْوَة", "noun", "the top, the peak of a thing (pl. ذُرًى)", "doruk, bir şeyin en üstü (çoğ. ذُرًى)", 5, "ذ ر و", "ذُرًى"),
 "mujaymir": G("الْمُجَيْمِر", "propn", "al-Mujaymir — a hill", "Müceymir — bir tepe", 6),
 "ghudwa": G("غُدْوَة", "noun", "the early morning, between dawn and sunrise", "sabahın erken vakti, fecir ile güneşin doğuşu arası", 4, "غ د و"),
 "ghutha": G("غُثَاء", "noun", "the wrack a torrent brings down: scum, grass, wood (pl. أَغْثَاء)", "selin getirdiği çerçöp, köpük, ot (çoğ. أَغْثَاء)", 6, "غ ث و", "أَغْثَاء"),
 "falka": G("فَلْكَة", "noun", "the whorl of a spindle", "iğ ağırşağı", 6, "ف ل ك"),
 "mighzal": G("مِغْزَل", "noun", "a spindle (pl. مَغَازِل)", "iğ (çoğ. مَغَازِل)", 5, "غ ز ل", "مَغَازِل"),
 "ghabit-hill": G("الْغَبِيط", "propn", "al-Ghabīṭ — a hill low in the middle, named after the camel's saddle-frame", "Gabît — ortası çukur bir tepe; deve semerine benzetilerek adlandırılmıştır", 6),
 "baa-load": G("بَعَاع", "noun", "a load, a burden; the weight of rain a cloud lets fall", "yük, ağırlık; bulutun bıraktığı yağmur yükü", 6, "ب ع ع"),
 "yamani": G("يَمَانٍ", "noun", "Yemeni, a man of Yemen (nisba with its yāʾ lightened: الْيَمَانِي)", "Yemenli (yâsı tahfif edilmiş nisbet: الْيَمَانِي)", 5, "ي م ن"),
 "ayba": G("عَيْبَة", "noun", "a bale or chest for clothes (pl. عِيَاب)", "elbise dengi veya sandığı (çoğ. عِيَاب)", 6, "ع ي ب", "عِيَاب"),
 "muhammal": G("مُحَمَّل", "noun", "laden, loaded (ism mafʿūl of حَمَّلَ)", "yüklü, yüklenmiş (حَمَّلَ'den ism-i mef'ûl)", 4, "ح م ل"),
 "mukka": G("مُكَّاء", "noun", "a small song-bird of the open country (pl. مَكَاكِيّ)", "kırda yaşayan küçük ötücü kuş (çoğ. مَكَاكِيّ)", 6, "م ك و", "مَكَاكِيّ"),
 "jiwa": G("جِوَاء", "noun", "a valley, a wide low ground (pl. أَجْوِيَة)", "vadi, geniş çukur arazi (çoğ. أَجْوِيَة)", 6, "ج و و", "أَجْوِيَة"),
 "ghudayya": G("غُدَيَّة", "noun", "the early morning (diminutive of غُدْوَة or غَدَاة)", "sabahın erken vakti (غُدْوَة ya da غَدَاة'in tasgîri)", 6, "غ د و"),
 "sabaha": G("صَبَحَ", "verb", "to give a morning draught to (صَبَحَ يَصْبَحُ)", "sabah içkisi içirmek (صَبَحَ يَصْبَحُ)", 6, "ص ب ح", form="I"),
 "sulaf": G("سُلَاف", "noun", "the finest wine, the first run of the grapes", "en hâlis şarap, üzümün sıkılmadan akan ilk suyu", 6, "س ل ف"),
 "rahiq": G("رَحِيق", "noun", "pure, clear wine", "saf, duru şarap", 5, "ر ح ق"),
 "mufalfal": G("مُفَلْفَل", "noun", "peppered, spiced with pepper", "biberli, biber katılmış", 6, "ف ل ف ل"),
 "ghariq": G("غَرِيق", "noun", "drowned (pl. غَرْقَى)", "boğulmuş (çoğ. غَرْقَى)", 4, "غ ر ق", "غَرْقَى"),
 "raja-side": G("رَجًا", "noun", "a side, an edge (a maqṣūr noun; pl. أَرْجَاء)", "kenar, yan (maksûr isim; çoğ. أَرْجَاء)", 6, "ر ج و", "أَرْجَاء"),
 "quswa": G("قُصْوَى", "noun", "farthest (fem. of أَقْصَى)", "en uzak (أَقْصَى'nın müennesi)", 4, "ق ص و"),
 "unbusha": G("أُنْبُوشَة", "noun", "a root dug up out of the ground (pl. أَنَابِيش)", "topraktan sökülmüş kök (çoğ. أَنَابِيش)", 6, "ن ب ش", "أَنَابِيش"),
 "unsul": G("عُنْصُل", "noun", "the wild onion, squill", "yaban soğanı, ada soğanı", 6, "ع ن ص ل"),
 # ==== NEW GLOSS ENTRIES ABOVE ====
}
# a key is a global claim: a NEW key must not already name something else on the shelf (or in a parallel staged package)
for k in NEW_GLOSS:
    hit = [p for p in PREF if k in _G[p] and _G[p][k].get("lemma") != NEW_GLOSS[k]["lemma"]]
    assert not hit, (k, hit)

def _keys(sentences):
    u = set()
    for s in sentences:
        for t in s["tokens"]:
            u.add(t["lex"])
            for sg2 in t.get("segments", []): u.add(sg2["lex"])
    return u
used, used_all = _keys([s for S in CHAPS for s in S]), _keys(ALL_AUTHORED)
no_entry = [k for k in sorted(used_all) if k not in NEW_GLOSS and find_gloss(k) is None]
assert not no_entry, no_entry
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k)
    if e is None: missing.append(k)
    else: GLOSS[k] = dict(e)
assert not missing, missing
unused_new = [k for k in NEW_GLOSS if k not in used_all]
assert not unused_new, unused_new
# same lemma and key as the shelf, but the gloss shown in THIS poem is the sense its verses use (after al-Zawzanī)
def REGLOSS(k, en, tr):
    assert k in used_all, k
    if k in GLOSS: GLOSS[k] = {**GLOSS[k], "gloss": {"en": en, "tr": tr}}
REGLOSS("afa", "(of a trace) to be wiped out, effaced; (elsewhere) to pardon (عَفَا يَعْفُو)", "(iz için) silinmek, yok olmak; (başka yerde) affetmek (عَفَا يَعْفُو)")
REGLOSS("ajuz", "the hindquarters, the rump (pl. أَعْجَاز); here: the last parts of the night", "sağrı, kıç tarafı (çoğ. أَعْجَاز); burada: gecenin son kısımları")
REGLOSS("asamm", "solid, hard, with no hollow in it (pl. صُمّ); (elsewhere) deaf", "sert, som, içi boş olmayan (çoğ. صُمّ); (başka yerde) sağır")
REGLOSS("haykal", "a horse of huge frame (pl. هَيَاكِل); (elsewhere) a great structure, a temple", "iri gövdeli at (çoğ. هَيَاكِل); (başka yerde) büyük yapı, tapınak")
REGLOSS("maqtal", "killing, being killed (a masdar with mim); also the place of killing", "öldürülme (mîmli masdar); ayrıca öldürülme yeri")
REGLOSS("mashrab", "drinking (a masdar with mim); also a drinking-place", "içme (mîmli masdar); ayrıca içme yeri")
REGLOSS("naa-weigh", "to rise heavily, to heave under a load; here, after al-Zawzanī: نَأَى «to be far» turned about", "ağırlıkla doğrulmak, yük altında davranmak; burada Zevzenî'ye göre: «uzaklaşmak» anlamındaki نَأَى'nın maklûbu")
REGLOSS("tatawala", "to grow long, to stretch on (Form VI)", "uzadıkça uzamak (tefâul)")
REGLOSS("tahammala", "to load up and set off, to depart (Form V); (elsewhere) to bear", "yükünü yükleyip göçmek, yola çıkmak (tefa''ul); (başka yerde) katlanmak")
REGLOSS("tamatta", "to stretch oneself, to stretch out (the back)", "gerinmek, (belini) gerip uzatmak")
REGLOSS("wuquf", "halting, standing — the plural of وَاقِف (as شُهُود of شَاهِد); also the masdar of وَقَفَ", "duranlar — وَاقِف'in cem'i (شَاهِد–شُهُود gibi); ayrıca وَقَفَ'nin masdarı")
REGLOSS("khalil", "a close friend, an intimate (dual خَلِيلَانِ)", "can dostu, yakın arkadaş (tesniyesi خَلِيلَانِ)")
REGLOSS("sahib", "a companion, a friend (pl. أَصْحَاب, صَحْب); صَاحِ: «my friend», cut short in the call", "arkadaş, yoldaş (çoğ. أَصْحَاب, صَحْب); صَاحِ: nidâda kısaltılmış «arkadaşım»")
REGLOSS("aysar", "the left-hand side, the leftmost part (opposite of أَيْمَن); (elsewhere) easier", "sol yan, en soldaki kısım (أَيْمَن'in zıddı); (başka yerde) daha kolay")
REGLOSS("udhayb", "al-ʿUdhayb — a place", "Uzeyb — bir yer adı")
REGLOSS("amala-tilt", "to tilt, to incline (a thing); here: to tip (the oil) on to the wicks (Form IV, hollow)", "eğmek, meylettirmek; burada: (yağı) fitillerin üzerine boca etmek (if'âl, ecvef)")
REGLOSS("suhba", "companions (a collective); (elsewhere) companionship", "arkadaşlar (topluluk ismi); (başka yerde) arkadaşlık")
REGLOSS("lam-shine", "a flash, a gleam; a quick movement — لَمْعُ الْيَدَيْنِ: the flicker of two hands (masdar of لَمَعَ)", "parıltı; hızlı hareket — لَمْعُ الْيَدَيْنِ: iki elin kımıldayışı (لَمَعَ'nın masdarı)")
REGLOSS("qaada", "to sit; قَعَدَ لَهُ: to sit watching for it (قَعَدَ يَقْعُدُ)", "oturmak; قَعَدَ لَهُ: onu gözlemek için oturmak (قَعَدَ يَقْعُدُ)")
REGLOSS("lada", "at, by, beside — the same as عِنْدَ", "yanında, katında — عِنْدَ ile aynı")
REGLOSS("ghulam", "a lad, a youth; here: the young rider", "delikanlı, genç; burada: genç binici")
REGLOSS("misbah", "a lamp (pl. مَصَابِيح)", "kandil, lamba (çoğ. مَصَابِيح)")
REGLOSS("dhaqan", "a chin (pl. أَذْقَان)", "çene (çoğ. أَذْقَان)")
REGLOSS("anzala", "to bring down, to send down (Form IV)", "indirmek (if'âl)")
REGLOSS("najm", "a star (pl. نُجُوم)", "yıldız (çoğ. نُجُوم)")
REGLOSS("hamm", "care, sorrow (pl. هُمُوم)", "keder, tasa (çoğ. هُمُوم)")
REGLOSS("qa", "level ground, a plain (pl. قِيعَان)", "düzlük, düz arazi (çoğ. قِيعَان)")
REGLOSS("arsa-plot", "an open space with no building on it, a courtyard (pl. عَرَصَات)", "üzerinde bina olmayan açık alan, avlu (çoğ. عَرَصَات)")
REGLOSS("thawb", "a garment (pl. أَثْوَاب, ثِيَاب)", "elbise (çoğ. أَثْوَاب, ثِيَاب)")
REGLOSS("matn", "the back (of a horse); (elsewhere) a text", "(atın) sırtı; (başka yerde) metin")
REGLOSS("salih-fit", "good, fine, sound (ism fāʿil of صَلَحَ)", "iyi, güzel, elverişli (صَلَحَ'nin ism-i fâili)")
REGLOSS("adhra", "a maiden, a virgin (pl. عَذَارَى)", "bâkire, genç kız (çoğ. عَذَارَى)")
REGLOSS("aqara", "to hamstring; to slaughter (a camel)", "sinirini kesmek; (deveyi) boğazlamak")
REGLOSS("dam-tear", "tears (pl. دُمُوع)", "gözyaşı (çoğ. دُمُوع)")
REGLOSS("qama", "to rise, to stand up", "kalkmak, ayağa kalkmak")
REGLOSS("muallal", "taken again and again (ism mafʿūl of عَلَّلَ, from عَلَّهُ «to give a second drink»); (elsewhere) explained by a cause", "tekrar tekrar alınan (عَلَّلَ'den ism-i mef'ûl; «ikinci kez su vermek» anlamındaki عَلَّهُ'dan); (başka yerde) illeti gösterilmiş")
REGLOSS("taadhdhara", "to turn stiff and contrary, to make difficulties (Form V); (elsewhere) to be impossible", "sertleşip yan çizmek, zorluk çıkarmak (tefa''ul); (başka yerde) imkânsız olmak")
REGLOSS("insarafa", "to turn (to or from), to go off (Form VII)", "(bir yöne) dönmek, ayrılıp gitmek (infiâl)")
REGLOSS("abada-far", "to put far off, to keep away (Form IV)", "uzaklaştırmak, uzak tutmak (if'âl)")
REGLOSS("mala", "to lean, to incline, to tilt (مَالَ يَمِيلُ — hollow)", "eğilmek, yana yatmak (مَالَ يَمِيلُ — ecvef)")
REGLOSS("imru", "a man — in the name امْرُؤُ الْقَيْسِ, Imruʾ al-Qays (its ra takes the vowel of its hamza: امْرُؤٌ، امْرَأً، امْرِئٍ)", "kişi — امْرُؤُ الْقَيْسِ (İmruülkays) adında (râ'sı hemzesinin harekesine uyar: امْرُؤٌ، امْرَأً، امْرِئٍ)")
REGLOSS("tamima", "an amulet, a charm hung on a child (pl. تَمَائِم)", "muska, çocuğa takılan nazarlık (çoğ. تَمَائِم)")
REGLOSS("saa-bad", "to displease, to grieve (someone); to be bad (hollow; سَاءَ يَسُوءُ)", "(birini) üzmek, hoşuna gitmemek; kötü olmak (ecvef; سَاءَ يَسُوءُ)")
REGLOSS("khalaiq", "a trait of character, a disposition", "huy, haslet")
REGLOSS("bayda-egg", "an egg; بَيْضَةُ خِدْرٍ: a lady kept behind the curtain, likened to an egg", "yumurta; بَيْضَةُ خِدْرٍ: perde ardında korunan, yumurtaya benzetilen hanım")
REGLOSS("taarrada", "to show one's side, to come across (the sky) (Form V); (elsewhere) to waylay", "yanını göstermek, (gökte) enine belirmek (tefa''ul); (başka yerde) yolunu kesmek")
REGLOSS("taarrud", "showing one's side (masdar of تَعَرَّضَ)", "yanını gösterme (تَعَرَّضَ'nin masdarı)")
REGLOSS("mufassal", "(of a sash or necklace) with its beads set apart by gold; (elsewhere) detailed", "(kuşak, gerdanlık için) boncuklarının arası altınla ayrılmış; (başka yerde) ayrıntılı")
REGLOSS("asarra", "to keep secret, to hide; also (an opposite sense) to show (Form IV)", "gizlemek; ayrıca (zıt anlamıyla) açığa vurmak (if'âl)")
REGLOSS("haris", "keen, eager (عَلَى: for, against) (pl. حِرَاص)", "hırslı, istekli (عَلَى ile) (çoğ. حِرَاص)")
REGLOSS("khiba", "a tent of wool or hair (pl. أَخْبِيَة)", "yünden veya kıldan çadır (çoğ. أَخْبِيَة)")
REGLOSS("mutafaddil", "one wearing a single light garment, as for sleep or work; (elsewhere) gracious", "uyku veya iş için tek, hafif giysi giyen; (başka yerde) lütufkâr")
REGLOSS("rayyan", "well-watered; (of a limb) full, plump (fem. رَيَّا)", "suya kanmış; (uzuv için) dolgun (müennesi رَيَّا)")
REGLOSS("hiqf", "a high curving ridge of sand (pl. حِقَاف, أَحْقَاف)", "yüksek, eğri kum sırtı (çoğ. حِقَاف, أَحْقَاف)")
REGLOSS("batn", "a belly; (of land) a hollow with higher ground about it", "karın; (arazi için) çevresi yüksek çukur yer")
REGLOSS("hila", "a means, a way out; a stratagem", "çare, çıkar yol; hile")
REGLOSS("kharaja", "to go out; خَرَجَ بِهِ: to bring (someone) out", "çıkmak; خَرَجَ بِهِ: (birini) çıkarmak")
REGLOSS("jarra", "to drag, to trail (doubled; جَرَّ يَجُرُّ)", "sürüklemek, sürümek (muzâaf; جَرَّ يَجُرُّ)")
REGLOSS("yamin", "an oath; the right hand — يَمِينَ اللهِ: «by God's oath»", "yemin; sağ el — يَمِينَ اللهِ: «Allah'a yemin olsun»")
REGLOSS("muthanna", "doubled back, folded (ism mafʿūl of ثَنَّى); (in grammar) the dual", "katlanmış, bükülmüş (ثَنَّى'dan ism-i mef'ûl); (nahivde) tesniye")
REGLOSS("mursal", "let loose, hanging free (ism mafʿūl of أَرْسَلَ); (elsewhere) one sent", "salıverilmiş, serbest bırakılmış (أَرْسَلَ'den ism-i mef'ûl); (başka yerde) gönderilmiş")
REGLOSS("muattal", "bare of ornament; left idle (ism mafʿūl of عَطَّلَ)", "takısız; boş bırakılmış (عَطَّلَ'den ism-i mef'ûl)")
REGLOSS("fahish", "beyond the praised measure, excessive", "övülen ölçüyü aşan, aşırı")
REGLOSS("latif", "fine, slender; subtle, gentle", "ince, narin; latif")
REGLOSS("ulya", "highest, uppermost (fem. of أَعْلَى; pl. عُلًا)", "en yüksek, en üst (أَعْلَى'nın müennesi; çoğ. عُلًا)")
REGLOSS("dalla-stray", "to stray, to be lost from sight (doubled; ضَلَّ يَضِلُّ)", "yolunu şaşırmak, gözden kaybolmak (muzâaf; ضَلَّ يَضِلُّ)")
REGLOSS("ittaqa", "to guard oneself, to put something between oneself and another; to be wary of (Form VIII)", "sakınmak, araya bir engel koymak; çekinmek (iftiâl)")
REGLOSS("saq", "the shank, the leg", "baldır, bacak")
REGLOSS("tafaddul", "putting on the فُضْلَة, a single garment for work; (elsewhere) grace, favour freely given", "«فُضْلَة» (tek parça iş elbisesi) giymek; (başka yerde) lütuf, tefaddul")
REGLOSS("dir", "a woman's shift (masc.); a coat of mail (fem.; pl. دُرُوع, أَدْرُع)", "kadın gömleği (müzekker); zırh (müennes; çoğ. دُرُوع, أَدْرُع)")
REGLOSS("adha-become", "to come into the forenoon; to become — a sister of kāna", "kuşluk vaktine girmek; olmak — kâne'nin kardeşi")
REGLOSS("halim", "forbearing, mild; a man of sense", "halîm, yumuşak huylu; aklı başında kimse")
REGLOSS("lamma", "when (with a past verb); (before a present verb) not yet — a particle of jazm like لَمْ", "…-ınca, …-dığı zaman (mâzî ile); (muzâriden önce) henüz …-medi — لَمْ gibi cezm harfi")
REGLOSS("harth", "tilth, tillage; (borrowed) striving and earning", "ekin, tarla sürme; (istiâre ile) çalışıp kazanma")
REGLOSS("taqrib", "(of a horse) a canter in which the hind feet land where the forefeet were; bringing near (masdar of قَرَّبَ)", "(at için) arka ayakların ön ayakların yerine bastığı koşu; yaklaştırma (قَرَّبَ'nin masdarı)")
REGLOSS("mudhayyal", "long in the skirt, trailing (ism mafʿūl of ذَيَّلَ); (in badīʿ) a kind of jinās nāqiṣ", "eteği uzun, yerde sürünen (ذَيَّلَ'nin ism-i mef'ûlü); (bedîde) cinâs-ı nâkısın bir türü")
REGLOSS("walid", "a boy, a child (pl. وِلْدَان)", "erkek çocuk (çoğ. وِلْدَان)")
REGLOSS("qasara", "قَصَرَ عَنْهُ: to fall short of a thing, to be unable to reach it; (elsewhere) to shorten (the prayer)", "قَصَرَ عَنْهُ: bir şeye yetişememek, ondan âciz kalmak; (başka yerde) (namazı) kısaltmak")
REGLOSS("alhaqa", "to make one catch up with, to bring up to; to join to, to attach (Form IV)", "yetiştirmek, ulaştırmak; katmak, eklemek (if'âl)")
REGLOSS("duna", "on this side of, short of, below; other than (adverb)", "berisinde, altında, önünde; -den başka (zarf)")
REGLOSS("raha-become", "to go or come back in the evening; to become — a sister of kāna (hollow)", "akşamleyin gitmek ya da dönmek; olmak — kâne'nin kardeşi (ecvef)")
REGLOSS("qaim", "standing; subsisting", "ayakta duran; kâim")
REGLOSS("kabir", "great, big; an elder, a chief", "büyük; yaşlı, bir topluluğun büyüğü")
# ==== REGLOSS ABOVE ====

# ---- paradigms: the shelf's own where the verb is on the shelf; a new verb is built by sarf_gen, or cell for cell on a shelf verb of the same class
MORPH = {"verbs": {}}
def _like(model, pairs, **over):
    """a paradigm on the model of a shelf verb of the same class: the radicals swapped cell for cell, the lexical fields restated"""
    m = json.loads(json.dumps(model, ensure_ascii=False))
    def sw(x):
        if isinstance(x, list): return [sw(c) for c in x]
        for a, b in pairs: x = x.replace(a, "\x00" + b)
        return x.replace("\x00", "")
    out = {k: (sw(v) if k in ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2", "majhulMazi", "majhulMudari") else v) for k, v in m.items()
           if k in ("bab", "wazn", "mazi", "mudari", "amr", "mansub", "majzum", "majzum2", "majhulMazi", "majhulMudari")}
    out.update(over)
    return json.loads(N(json.dumps(out, ensure_ascii=False)))
_marra, _ahabba, _alqa, _ibtala, _inbara, _aata = (find_verb(k) for k in ("marra", "ahabba", "alqa", "ibtala", "inbara", "aataa"))
assert all((_marra, _ahabba, _alqa, _ibtala, _inbara, _aata)) and _aata["mazi"][0] == N("آتَى") and _aata["mudari"][12] == N("أُوتِي")
def _dbl(f, l, masdar, fail, maful):
    """a doubled verb of bāb naṣara, in the shape sarf_gen states مَرَّ (suffix-attach on the contracted and the full stem)"""
    return _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", masdar, fail, _sg.mazi14(f + "َ" + l + "ّ", f + "َ" + l + "َ" + l),
                     _sg.mudari14("َ", f + "ُ" + l + "ّ", f + "ْ" + l + "ُ" + l),
                     [f + "ُ" + l + "َّ", f + "ُ" + l + "َّا", f + "ُ" + l + "ُّوا", f + "ُ" + l + "ِّي", f + "ُ" + l + "َّا", "اُ" + f + "ْ" + l + "ُ" + l + "ْنَ"],
                     "يَ" + f + "ُ" + l + "َّ", "يَ" + f + "ُ" + l + "َّ", "تَ" + f + "ُ" + l + "َّ", maful=maful,
                     note="مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَ" + f + "ُ" + l + "َّ، وَيَجُوزُ لَمْ يَ" + f + "ْ" + l + "ُ" + l + "ْ.")
def _ala(c, masdar, fail, note):
    """Form IV, hamzated first radical and defective (آتَى، آلَى): sarf_gen's defective engine, the first person softened as the shelf writes it (أُوتِي)"""
    e = _sg.derived_naqis(_sg.B4 + " — مَهْمُوزُ الْفَاءِ نَاقِصٌ", _sg.W4, "ُ", "آ" + c + "َ", "ؤْ" + c, "i", "آ" + c, masdar, fail, note=note)
    e["mudari"][12] = N("أُو" + c + "ِي")
    return e
def _cells(e): return {k: e[k] for k in ("mazi", "mudari", "amr", "mansub", "majzum", "majzum2")}
# the two builders are trusted only because they reproduce the shelf's own مَرَّ and آتَى cell for cell
assert _cells(_dbl("م", "ر", "مُرُور", "مَارّ", None)) == _cells(json.loads(N(json.dumps(_marra, ensure_ascii=False)))), "dbl"
assert _cells(_ala("ت", "إِيتَاء", "مُؤْتٍ", "")) == _cells(json.loads(N(json.dumps(_aata, ensure_ascii=False)))), "ala"
NEW_VERBS = {
 "hatta-down": _dbl("ح", "ط", "حَطّ", "حَاطّ", "مَحْطُوط"),
 "sahha-pour": _dbl("س", "ح", "سَحّ", "سَاحّ", "مَسْحُوح"),
 "kabba": _dbl("ك", "ب", "كَبّ", "كَابّ", "مَكْبُوب"),
 "azalla": _like(_ahabba, [("ح", "ز"), ("ب", "ل")], masdar="إِزْلَال", ismFail="مُزِلّ", ismMaful="مُزَلّ", note="مُضَاعَفٌ مِنَ الْإِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُزِلَّ، وَيَجُوزُ لَمْ يُزْلِلْ."),
 "arkha": _like(_alqa, [("ل", "ر"), ("ق", "خ")], masdar="إِرْخَاء", ismFail="مُرْخٍ", ismMaful="مُرْخًى", note="نَاقِصٌ مِنَ الْإِفْعَالِ: يُرْخِي ← لَمْ يُرْخِ."),
 "alwa": _like(_alqa, [("ق", "و")], bab=_sg.B4 + " — لَفِيفٌ مَقْرُونٌ", masdar="إِلْوَاء", ismFail="مُلْوٍ", ismMaful="مُلْوًى", note="لَفِيفٌ مَقْرُونٌ مِنَ الْإِفْعَالِ: يُلْوِي ← لَمْ يُلْوِ."),
 "ala-swear": _ala("ل", "إِيلَاء", "مُؤْلٍ", "آلَى يُؤْلِي إِيلَاءً: حَلَفَ — مِنَ الْإِفْعَالِ، مَهْمُوزُ الْفَاءِ نَاقِصٌ، وَأَصْلُهُ أَأْلَى."),
 "ightada": _like(_ibtala, [("ب", "غ"), ("ل", "د")], bab=_sg.B8 + " — نَاقِصٌ", masdar="اِغْتِدَاء", ismFail="مُغْتَدٍ", note="اِغْتَدَى وَغَدَا بِمَعْنًى: خَرَجَ غُدْوَةً."),
 "injala": _like(_inbara, [("ب", "ج"), ("ر", "ل")], masdar="اِنْجِلَاء", ismFail="مُنْجَلٍ", note="اِنْجَلَى: اِنْكَشَفَ — يُقَالُ: جَلَوْتُهُ فَانْجَلَى."),
 "adaa-shine": _like(_sg.SAMTI["asaa"], [("س", "ض")], masdar="إِضَاءَة", ismFail="مُضِيء", ismMaful="مُضَاء", majhulMazi="أُضِيءَ", majhulMudari="يُضَاءُ", note="أَجْوَفُ مَهْمُوزُ اللَّامِ: يُضِيءُ ← لَمْ يُضِئْ."),
 "ardafa": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَرْدَف", "رْدِف", "أَرْدِف", "إِرْدَاف", "مُرْدِف", "مُرْدَف", "أُرْدِفَ", "يُرْدَفُ"),
 "tajammala": _sg.derived(_sg.B5, _sg.W5, "َ", "تَجَمَّل", "تَجَمَّل", "تَجَمَّل", "تَجَمُّل", "مُتَجَمِّل"),
 "nasaja": _sg.sound1("daraba", "نَسَج", "نْسِج", "اِنْسِج", "نَسْج", "نَاسِج", "مَنْسُوج", "نُسِجَ", "يُنْسَجُ"),
 "thaara": _sg.sound1("fataha", "ثَأَر", "ثْأَر", "اِثْأَر", "ثَأْر", "ثَائِر", cls="مَهْمُوزُ الْعَيْنِ"),
 "tadawwaa": _sg.derived(_sg.B5, _sg.W5, "َ", "تَضَوَّع", "تَضَوَّع", "تَضَوَّع", "تَضَوُّع", "مُتَضَوِّع"),
 "balla": _dbl("ب", "ل", "بَلّ", "بَالّ", "مَبْلُول"),
 "irtama": _like(_ibtala, [("ب", "ر"), ("ل", "م")], bab=_sg.B8 + " — نَاقِصٌ", masdar="اِرْتِمَاء", ismFail="مُرْتَمٍ", note="اِرْتَمَى الْقَوْمُ بِالشَّيْءِ: رَمَى بِهِ بَعْضُهُمْ إِلَى بَعْضٍ."),
 "tahallala": _sg.derived(_sg.B5, _sg.W5, "َ", "تَحَلَّل", "تَحَلَّل", "تَحَلَّل", "تَحَلُّل", "مُتَحَلِّل"),
 "ajmala": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَجْمَل", "جْمِل", "أَجْمِل", "إِجْمَال", "مُجْمِل", "مُجْمَل", "أُجْمِلَ", "يُجْمَلُ"),
 "gharra": _dbl("غ", "ر", "غُرُور", "غَارّ", "مَغْرُور"),
 "salla-draw": _dbl("س", "ل", "سَلّ", "سَالّ", "مَسْلُول"),
 "nasala": _sg.sound1("nasara", "نَسَل", "نْسُل", "اُنْسُل", "نُسُول", "نَاسِل"),
 "dharafa": _sg.sound1("daraba", "ذَرَف", "ذْرِف", "اِذْرِف", "ذَرْف", "ذَارِف"),
 "rama-seek": _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "رَام", "رُم", "رُوم", "رُم", "رُوم", "رُم", "رَوْم", "رَائِم", "مَرُوم", "رِيمَ", "يُرَامُ"),
 "nadda": _sg.derived_naqis(_sg.B2 + " — نَاقِصٌ", _sg.W2, "ُ", "نَضَّ", "نَضّ", "i", "نَضّ", "تَنْضِيَة", "مُنَضٍّ", "مُنَضًّى", "نُضِّيَ", "يُنَضَّى"),
 "ajaza-cross": _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ", _sg.W4, "ُ", "أَجَاز", "أَجَز", "جِيز", "جِز", "أَجِيز", "أَجِز", "إِجَازَة", "مُجِيز", "مُجَاز", "أُجِيزَ", "يُجَازُ", "أَجْوَفُ مِنَ الْإِفْعَالِ: يُجِيزُ ← لَمْ يُجِزْ."),
 "intaha-lean": _like(_ibtala, [("ب", "ن"), ("ل", "ح")], bab=_sg.B8 + " — نَاقِصٌ", masdar="اِنْتِحَاء", ismFail="مُنْتَحٍ", note="اِنْتَحَى: اِعْتَمَدَ وَمَالَ."),
 "hasara-pull": _sg.sound1("daraba", "هَصَر", "هْصِر", "اِهْصِر", "هَصْر", "هَاصِر", "مَهْصُور", "هُصِرَ", "يُهْصَرُ"),
 "tamayala": _sg.derived(_sg.B6, _sg.W6, "َ", "تَمَايَل", "تَمَايَل", "تَمَايَل", "تَمَايُل", "مُتَمَايِل"),
 "ghadha": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "غَذَ", "غْذ", "u", "اُغْذ", "غَذْو", "غَاذٍ", "مَغْذُوّ", "غُذِيَ", "يُغْذَى"),
 "nassa": _dbl("ن", "ص", "نَصّ", "نَاصّ", "مَنْصُوص"),
 "intataqa": _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَطَق", "نْتَطِق", "اِنْتَطِق", "اِنْتِطَاق", "مُنْتَطِق"),
 "ata-reach": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "عَطَ", "عْط", "u", "اُعْط", "عَطْو", "عَاطٍ"),
 "rana": _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "رَنَ", "رْن", "u", "اُرْن", "رُنُوّ", "رَانٍ"),
 "isbakarra": _like(find_verb("iqshaarra"), [("ق", "س"), ("ش", "ب"), ("ع", "ك")], masdar="اِسْبِكْرَار", ismFail="مُسْبَكِرّ"),
 "tasalla": _sg.derived_naqis(_sg.B5 + " — نَاقِصٌ", _sg.W5, "َ", "تَسَلَّ", "تَسَلّ", "a", "تَسَلّ", "تَسَلٍّ", "مُتَسَلٍّ"),
 "awa": _sg.naqis1("daraba", "لَفِيفٌ مَقْرُونٌ", "y", "عَوَ", "عْو", "i", "اِعْو", "عُوَاء", "عَاوٍ"),
 "tamawwala": _sg.derived(_sg.B5, _sg.W5, "َ", "تَمَوَّل", "تَمَوَّل", "تَمَوَّل", "تَمَوُّل", "مُتَمَوِّل"),
 "afata": _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ", _sg.W4, "ُ", "أَفَات", "أَفَت", "فِيت", "فِت", "أَفِيت", "أَفِت", "إِفَاتَة", "مُفِيت", "مُفَات", "أُفِيتَ", "يُفَاتُ", "أَجْوَفُ مِنَ الْإِفْعَالِ: يُفِيتُ ← لَمْ يُفِتْ."),
 "ihtaratha": _sg.derived(_sg.B8, _sg.W8, "َ", "اِحْتَرَث", "حْتَرِث", "اِحْتَرِث", "اِحْتِرَاث", "مُحْتَرِث", "مُحْتَرَث", "اُحْتُرِثَ", "يُحْتَرَثُ"),
 "hazala": _sg.sound1("nasara", "هَزَل", "هْزُل", "اُهْزُل", "هُزَال", "هَازِل", None, "هُزِلَ", "يُهْزَلُ"),
 "amarra": _like(_ahabba, [("ح", "م"), ("ب", "ر")], masdar="إِمْرَار", ismFail="مُمِرّ", ismMaful="مُمَرّ", note="مُضَاعَفٌ مِنَ الْإِفْعَالِ: الْجَزْمُ بِالْفَتْحِ — لَمْ يُمِرَّ، وَيَجُوزُ لَمْ يُمْرِرْ."),
 "istadbara": _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَدْبَر", "سْتَدْبِر", "اِسْتَدْبِر", "اِسْتِدْبَار", "مُسْتَدْبِر", "مُسْتَدْبَر", "اُسْتُدْبِرَ", "يُسْتَدْبَرُ"),
 "adbara": _sg.derived(_sg.B4, _sg.W4, "ُ", "أَدْبَر", "دْبِر", "أَدْبِر", "إِدْبَار", "مُدْبِر"),
 "zayyala": _sg.derived(_sg.B2, _sg.W2, "ُ", "زَيَّل", "زَيِّل", "زَيِّل", "تَزْيِيل", "مُزَيِّل", "مُزَيَّل", "زُيِّلَ", "يُزَيَّلُ"),
 "taraqqa": _sg.derived_naqis(_sg.B5 + " — نَاقِصٌ", _sg.W5, "َ", "تَرَقَّ", "تَرَقّ", "a", "تَرَقّ", "تَرَقٍّ", "مُتَرَقٍّ"),
 "tasaffala": _sg.derived(_sg.B5, _sg.W5, "َ", "تَسَفَّل", "تَسَفَّل", "تَسَفَّل", "تَسَفُّل", "مُتَسَفِّل"),
 "sabaha": _sg.sound1("fataha", "صَبَح", "صْبَح", "اِصْبَح", "صَبْح", "صَابِح", "مَصْبُوح", "صُبِحَ", "يُصْبَحُ"),
 # ==== NEW VERBS ABOVE ====
}
for k in ("ightada", "injala", "irtama", "intaha-lean"):
    NEW_VERBS[k].pop("majhulMazi", None); NEW_VERBS[k].pop("majhulMudari", None)
for k, e in GLOSS.items():
    if e.get("pos") != "verb": continue
    v = NEW_VERBS.get(k) if k in NEW_GLOSS else find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par
assert set(NEW_VERBS) == {k for k, e in NEW_GLOSS.items() if e["pos"] == "verb"}

# ---- the attribution: built from what is published, so that it never claims more than the chapters hold -------------------------
PAGE_OF = {1: 35, 2: 36, 3: 36, 4: 37, 5: 37, 6: 38, 7: 38, 8: 39, 9: 39, 10: 39, 11: 40, 12: 40, 13: 41, 14: 42, 15: 42, 16: 43, 17: 44, 18: 44, 19: 45, 20: 45,
           21: 46, 22: 46, 23: 47, 24: 48, 25: 48, 26: 49, 27: 49, 28: 50, 29: 50, 30: 51, 31: 52, 32: 52, 33: 53, 34: 54, 35: 54, 36: 55, 37: 55, 38: 55, 39: 56,
           40: 57, 41: 57, 42: 58, 43: 58, 44: 59, 45: 59, 46: 60, 47: 60, 48: 61, 49: 62, 50: 62, 51: 63, 52: 63, 53: 64, 54: 65, 55: 65, 56: 65, 57: 66, 58: 67,
           59: 68, 60: 68, 61: 69, 62: 69, 63: 70, 64: 70, 65: 71, 66: 71, 67: 71, 68: 72, 69: 72, 70: 72, 71: 73, 72: 73, 73: 74, 74: 74, 75: 75, 76: 75, 77: 76,
           78: 76, 79: 76, 80: 77, 81: 77}   # the printed page on which al-Zawzanī's edition sets each verse
LAST_PAGE = PAGE_OF.get(LAST + 1, 78)
# slips of the e-text corrected against a witness: (verse, ar, en, tr)
CORR = [
 (45, "الْبَيْتُ ٤٥ «لَمِّا» ← «لَمَّا» وَ«بَكَلْكَلِ» ← «بِكَلْكَلِ» (شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ، وَالتِّبْرِيزِيُّ ص ٣٥)",
  "v. 45 «لَمِّا» → «لَمَّا» and «بَكَلْكَلِ» → «بِكَلْكَلِ» (al-Zawzanī's own commentary; al-Tibrīzī, «شرح القصائد العشر», p. 35)",
  "45. beyit «لَمِّا» → «لَمَّا» ve «بَكَلْكَلِ» → «بِكَلْكَلِ» (Zevzenî'nin kendi şerhi; Tebrîzî, «شرح القصائد العشر», p. 35)"),
 (57, "الْبَيْتُ ٥٧ «على صَهَواتِهِ» ← «عَنْ صَهَوَاتِهِ» (الْوَزْنُ، وَقَوْلُ الزَّوْزَنِيِّ «عَنْ مَقْعَدِهِ»، وَالتِّبْرِيزِيُّ ص ٤١، وَالدُّرَّةُ ١/١٣٠)",
  "v. 57 «على صَهَواتِهِ» → «عَنْ صَهَوَاتِهِ» (the metre; al-Zawzanī's paraphrase «عن مقعده»; al-Tibrīzī p. 41; al-Durra 1/130)",
  "57. beyit «على صَهَواتِهِ» → «عَنْ صَهَوَاتِهِ» (vezin; Zevzenî'nin «عن مقعده» açıklaması; Tebrîzî s. 41; Dürre 1/130)"),
 (70, "الْبَيْتُ ٧٠ «ومَيضَهُ» ← «وَمِيضَهُ» (قَوْلُ الزَّوْزَنِيِّ «الْوَمِيضُ»)",
  "v. 70 «ومَيضَهُ» → «وَمِيضَهُ» (a misplaced fatḥa; al-Zawzanī's gloss «الوميض»)",
  "70. beyit «ومَيضَهُ» → «وَمِيضَهُ» (yeri kaymış fetha; Zevzenî'nin «الوميض» açıklaması)"),
 (72, "الْبَيْتُ ٧٢ «مُتَأَمِّلي» ← «مُتَأَمَّلِي» (قَوْلُ الزَّوْزَنِيِّ «وَهُوَ الْمَنْظُورُ إِلَيْهِ»، وَالتِّبْرِيزِيُّ ص ٥٠)",
  "v. 72 «مُتَأَمِّلي» → «مُتَأَمَّلِي» (al-Zawzanī: «وهو المنظور إليه»; al-Tibrīzī p. 50)",
  "72. beyit «مُتَأَمِّلي» → «مُتَأَمَّلِي» (Zevzenî: «وهو المنظور إليه»; Tebrîzî s. 50)"),
 (75, "الْبَيْتُ ٧٥ «القَنَّانِ» ← «الْقَنَانِ» (التِّبْرِيزِيُّ ص ٥١، وَتَرْجِيحُ الدُّرَّةِ ١/١٥٤)",
  "v. 75 «القَنَّانِ» → «الْقَنَانِ» (al-Tibrīzī p. 51; al-Durra 1/154, who prefers the fatḥa with a single nūn)",
  "75. beyit «القَنَّانِ» → «الْقَنَانِ» (Tebrîzî s. 51; Dürre 1/154, kāf'ın fethası ve nûn'un şeddesiz okunuşunu tercih eder)"),
 (12, "الْبَيْتُ ١٢ «الدَّمَقس» ← «الدِّمَقْسِ» (التِّبْرِيزِيُّ ص ١٦، وَالْمَعَاجِمُ: بِكَسْرِ الدَّالِ)",
  "v. 12 «الدَّمَقس» → «الدِّمَقْسِ» (al-Tibrīzī p. 16; the lexica: with a kasra on the dāl)",
  "12. beyit «الدَّمَقس» → «الدِّمَقْسِ» (Tebrîzî s. 16; sözlükler: dâl'in kesresiyle)"),
 (23, "الْبَيْتُ ٢٣ «مُعَجَّلِ» ← «مُعْجَلِ» (الْوَزْنُ، وَالتِّبْرِيزِيُّ ص ٢٣)",
  "v. 23 «مُعَجَّلِ» → «مُعْجَلِ» (the metre; al-Tibrīzī p. 23)",
  "23. beyit «مُعَجَّلِ» → «مُعْجَلِ» (vezin; Tebrîzî s. 23)"),
 (30, "الْبَيْتُ ٣٠ «رَيًّا الْمُخلخَلِ» ← «رَيَّا الْمُخَلْخَلِ» بِلَا تَنْوِينٍ لِأَنَّهُ مُضَافٌ (التِّبْرِيزِيُّ ص ٢٧)",
  "v. 30 «رَيًّا الْمُخلخَلِ» → «رَيَّا الْمُخَلْخَلِ», without tanwin, the word being annexed (al-Tibrīzī p. 27)",
  "30. beyit «رَيًّا الْمُخلخَلِ» → «رَيَّا الْمُخَلْخَلِ», muzâf olduğu için tenvinsiz (Tebrîzî s. 27)"),
 (31, "الْبَيْتُ ٣١ «بَيْضَاءَ» ← «بَيْضَاءُ» بِالرَّفْعِ كَمَا قَبْلَهَا وَمَا بَعْدَهَا (التِّبْرِيزِيُّ ص ٢٨، وَإِعْرَابُ الدُّرَّةِ ١/٩٢)",
  "v. 31 «بَيْضَاءَ» → «بَيْضَاءُ», in raf' like the words before and after it (al-Tibrīzī p. 28; al-Durra's parse, 1/92)",
  "31. beyit «بَيْضَاءَ» → «بَيْضَاءُ», öncesi ve sonrası gibi ref' ile (Tebrîzî s. 28; Dürre'nin i'râbı, 1/92)"),
 (33, "الْبَيْتُ ٣٣ «بناظرّةٍ» ← «بِنَاظِرَةٍ» بِلَا تَشْدِيدٍ، وَ«مُطْفِلٍ» ← «مُطْفِلِ» بِلَا تَنْوِينٍ لِلْقَافِيَةِ (التِّبْرِيزِيُّ ص ٢٩)",
  "v. 33 «بناظرّةٍ» → «بِنَاظِرَةٍ», without the shadda, and «مُطْفِلٍ» → «مُطْفِلِ», without tanwin at the rhyme (al-Tibrīzī p. 29)",
  "33. beyit «بناظرّةٍ» → «بِنَاظِرَةٍ», şeddesiz; «مُطْفِلٍ» → «مُطْفِلِ», kafiyede tenvinsiz (Tebrîzî s. 29)"),
 (35, "الْبَيْتُ ٣٥ «أثيتٍ» ← «أَثِيثٍ» بِالثَّاءِ (شَرْحُ الزَّوْزَنِيِّ نَفْسُهُ «الْأَثِيثُ: الْكَثِيرُ»، وَالتِّبْرِيزِيُّ ص ٣٠)",
  "v. 35 «أثيتٍ» → «أَثِيثٍ», with a thāʾ (al-Zawzanī's own gloss «الأثيث: الكثير»; al-Tibrīzī p. 30)",
  "35. beyit «أثيتٍ» → «أَثِيثٍ», sâ ile (Zevzenî'nin kendi açıklaması «الأثيث: الكثير»; Tebrîzî s. 30)"),
 (64, "الْبَيْتُ ٦٤ «بِجِيدٍ مُعَمٍّ» ← «بِجِيدِ مُعَمٍّ» بِالْإِضَافَةِ (قَوْلُ الزَّوْزَنِيِّ «فِي عُنُقِ صَبِيٍّ كَرُمَ أَعْمَامُهُ»، وَالتِّبْرِيزِيُّ ص ٤٤، وَالدُّرَّةُ ١/١٤٠)",
  "v. 64 «بِجِيدٍ مُعَمٍّ» → «بِجِيدِ مُعَمٍّ», an annexation (al-Zawzanī's paraphrase «on the neck of a boy whose uncles are noble»; al-Tibrīzī p. 44; al-Durra 1/140)",
  "64. beyit «بِجِيدٍ مُعَمٍّ» → «بِجِيدِ مُعَمٍّ», izâfetle (Zevzenî'nin «amcaları soylu bir çocuğun boynunda» açıklaması; Tebrîzî s. 44; Dürre 1/140)"),
 (36, "الْبَيْتُ ٣٦ «مُثَنَّى» ← «مُثَنًّى» بِالتَّنْوِينِ لِأَنَّهُ نَكِرَةٌ مُنْصَرِفَةٌ عُطِفَ عَلَيْهَا «مُرْسَلِ» (التِّبْرِيزِيُّ ص ٣١)",
  "v. 36 «مُثَنَّى» → «مُثَنًّى», with tanwin — an indefinite, fully declined noun to which «مُرْسَلِ» is conjoined (al-Tibrīzī p. 31)",
  "36. beyit «مُثَنَّى» → «مُثَنًّى», tenvinle — «مُرْسَلِ»in atfedildiği munsarif bir nekredir (Tebrîzî s. 31)"),
 # ==== CORR ABOVE ====
]
# what is left for the scholar: (verse — 0 for the khabar, ar, en, tr)
SCHOLAR = [
 (0, "اسْمُ «دَمُّونَ»", "the vowelling of the place-name «دَمُّون»", "«دَمُّون» yer adının zabtı"),
 (52, "كَافُ «وُكُنَاتِهَا» (ضُمَّتْ، وَهِيَ عِنْدَ التِّبْرِيزِيِّ مَفْتُوحَةٌ)",
  "the kāf of «وُكُنَاتِهَا» in v. 52 (ḍamma chosen — al-Zawzanī's first form; al-Tibrīzī's text has a fatḥa; the metre allows both)",
  "52. beyitteki «وُكُنَاتِهَا»nın kâfı (damme seçildi — Zevzenî'nin ilk zikrettiği şekil; Tebrîzî metninde fethalıdır; vezin ikisine de uyar)"),
 (72, "«بَعْدَ مَا» فِي الْبَيْتِ ٧٢ (وَيُرْوَى «بُعْدَ»)", "«بَعْدَ مَا» in v. 72 (also transmitted «بُعْدَ»)", "72. beyitteki «بَعْدَ مَا» («بُعْدَ» de rivayet edilir)"),
 (74, "بَاءُ «الْكَنَهْبَلِ» (فُتِحَتْ، وَذَكَرَ الزَّوْزَنِيُّ الضَّمَّ وَالْفَتْحَ)", "the bāʾ of «الْكَنَهْبَلِ» in v. 74 (fatḥa chosen; al-Zawzanī allows ḍamma too)", "74. beyitteki «الْكَنَهْبَلِ»in bâ'sı (fetha seçildi; Zevzenî dammeyi de zikreder)"),
 (75, "«مَنْزِلِ» فِي الْبَيْتِ ٧٥ (كُسِرَتْ زَايُهُ كَمَا فِي الطَّبْعَةِ، وَتَفْسِيرُ الزَّوْزَنِيِّ «مَوْضِعُ الْإِنْزَالِ» يُنَاسِبُ «مُنْزَلِ» وَهِيَ رِوَايَةُ التِّبْرِيزِيِّ)، وَتَصْحِيحُ «الْقَنَانِ»",
  "«مَنْزِلِ» in v. 75 (the edition's kasra kept, though al-Zawzanī's gloss «موضع الإنزال» suits «مُنْزَلِ», al-Tibrīzī's reading), and the correction of «الْقَنَانِ»",
  "75. beyitteki «مَنْزِلِ» (baskıdaki kesre korundu; oysa Zevzenî'nin «موضع الإنزال» açıklaması Tebrîzî'nin rivayeti olan «مُنْزَلِ»e uygundur) ve «الْقَنَانِ» düzeltmesi"),
 (32, "ضَادُ «الْبَيَاضِ» فِي الْبَيْتِ ٣٢ (جُرَّتْ عَلَى الْإِضَافَةِ، وَذَكَرَ الزَّوْزَنِيُّ النَّصْبَ وَالْخَفْضَ، وَهِيَ عِنْدَ التِّبْرِيزِيِّ مَرْفُوعَةٌ)",
  "the ḍād of «الْبَيَاضِ» in v. 32 (jarr chosen, by annexation; al-Zawzanī allows nasb and jarr; al-Tibrīzī's text has raf')",
  "32. beyitteki «الْبَيَاضِ»ın dâd'ı (izâfetle cer seçildi; Zevzenî nasb ve cerri zikreder; Tebrîzî metninde merfûdur)"),
 (51, "يَاءُ «يَهْزُلِ» فِي الْبَيْتِ ٥١ (طُبِعَتْ ضَمَّةُ الزَّايِ وَحْدَهَا فَفُتِحَتِ الْيَاءُ؛ وَعِنْدَ التِّبْرِيزِيِّ «يُهْزَلِ» بِالْبِنَاءِ لِلْمَجْهُولِ)",
  "the yāʾ of «يَهْزُلِ» in v. 51 (the edition prints only the ḍamma of the zāy, so the yāʾ is given a fatḥa; al-Tibrīzī has the passive «يُهْزَلِ»)",
  "51. beyitteki «يَهْزُلِ»nin yâ'sı (baskıda yalnız zây'ın dammesi var, bu yüzden yâ fethalı okundu; Tebrîzî'de meçhul «يُهْزَلِ»)"),
 (79, "مِيمُ «الْمُحَمَّلِ» الثَّانِيَةُ فِي الْبَيْتِ ٧٩ (لَمْ تُشْكَلْ فِي الطَّبْعَةِ، فَفُتِحَتْ كَمَا عِنْدَ التِّبْرِيزِيِّ ص ٥٣، وَأَجَازَ الدُّرَّةُ الْكَسْرَ)",
  "the second mīm of «الْمُحَمَّلِ» in v. 79 (bare in the edition; given a fatḥa as in al-Tibrīzī p. 53; al-Durra also allows a kasra)",
  "79. beyitteki «الْمُحَمَّلِ»in ikinci mîmi (baskıda harekesiz; Tebrîzî s. 53'teki gibi fethalı okundu; Dürre kesreyi de câiz görür)"),
 # ==== SCHOLAR ABOVE ====
]
# the verses the Talkhīṣ itself cites (checked against research/sources/talkhis-al-miftah-balagha.txt): (verse, ar, en, tr)
TALKHIS = [
 (1, "الْبَيْتِ ١ لِحُسْنِ الِابْتِدَاءِ", "verse 1 (the fine opening)", "1. beyti (hüsn-i ibtidâ)"),
 (46, "الْبَيْتِ ٤٦ لِخُرُوجِ الْأَمْرِ إِلَى التَّمَنِّي", "verse 46 (the command used for a wish)", "46. beyti (emrin temennî için kullanılması)"),
 (36, "الْبَيْتِ ٣٦ لِتَنَافُرِ الْحُرُوفِ فِي «مُسْتَشْزِرَاتٌ»", "verse 36 (the clash of letters in «مُسْتَشْزِرَاتٌ»)", "36. beyti («مُسْتَشْزِرَاتٌ»taki tenâfür-i hurûf)"),
 (66, "الْبَيْتِ ٦٦ لِلْمُبَالَغَةِ الْمَقْبُولَةِ (التَّبْلِيغِ)", "verse 66 (the acceptable hyperbole called tablīgh)", "66. beyti (teblîğ denilen makbul mübalağa)"),
 # ==== TALKHIS ABOVE ====
]
_corr = sorted((c for c in CORR if c[0] <= LAST), key=lambda c: c[0])
_sch = sorted((c for c in SCHOLAR if c[0] <= LAST), key=lambda c: c[0])
_tal = sorted((c for c in TALKHIS if c[0] <= LAST), key=lambda c: c[0])
_whole = LAST == TOTAL
_runs_ar = "؛ ".join("الْفَصْلُ %s: %s–%s" % (ar_num(i), ar_num(a), ar_num(b)) for i, (a, b, t) in enumerate(READY, 2))
_runs_en = "; ".join("chapter %d: %d–%d" % (i, a, b) for i, (a, b, t) in enumerate(READY, 2))
_runs_tr = "; ".join("%d. bölüm: %d–%d" % (i, a, b) for i, (a, b, t) in enumerate(READY, 2))
ATTR_AR = (
 "نَصٌّ مُتَلَقًّى. الْفَصْلُ الْأَوَّلُ قِطْعَةٌ مُتَّصِلَةٌ بِحُرُوفِهَا مِنْ تَرْجَمَةِ امْرِئِ الْقَيْسِ فِي «الشِّعْرِ وَالشُّعَرَاءِ» لِابْنِ قُتَيْبَةَ (ت ٢٧٦ هـ)، طَبْعَةُ دَارِ الْحَدِيثِ بِالْقَاهِرَةِ ١٤٢٣ هـ، ١/١٠٩: مِنْ «فَبَلَغَهُ مَقْتَلُ أَبِيهِ» إِلَى «حَتَّى يَثْأَرَ بِأَبِيهِ». "
 + ("وَسَائِرُ الْفُصُولِ هِيَ الْمُعَلَّقَةُ كَامِلَةً — %s بَيْتًا — " % ar_num(TOTAL) if _whole else "وَسَائِرُ الْفُصُولِ هِيَ الْمُعَلَّقَةُ مِنْ أَوَّلِهَا إِلَى الْبَيْتِ %s مِنْ %s (وَتَتْلُوهَا بَقِيَّةُ الْأَبْيَاتِ فِي فُصُولٍ لَاحِقَةٍ) — " % (ar_num(LAST), ar_num(TOTAL)))
 + "بِرِوَايَةِ الزَّوْزَنِيِّ (ت ٤٨٦ هـ) فِي «شَرْحِ الْمُعَلَّقَاتِ السَّبْعِ»، طَبْعَةُ دَارِ إِحْيَاءِ التُّرَاثِ الْعَرَبِيِّ ١٤٢٣ هـ / ٢٠٠٢ م، ص ٣٥–%s: نَصُّهُ وَتَرْتِيبُهُ وَعَدُّهُ، لَمْ يُتْرَكْ بَيْتٌ وَلَمْ يُتَخَطَّ مَوْضِعٌ. أَبْيَاتُ الْفُصُولِ: %s. وَالْقَصِيدَةُ مِنَ الطَّوِيلِ. " % (ar_num(LAST_PAGE), _runs_ar)
 + ("وَالْأَبْيَاتُ ٤٨–٥١ قَالَ فِيهَا الزَّوْزَنِيُّ إِنَّ جُمْهُورَ الْأَئِمَّةِ لَمْ يَرْوِهَا فِي هٰذِهِ الْقَصِيدَةِ وَزَعَمُوا أَنَّهَا لِتَأَبَّطَ شَرًّا، وَهِيَ هُنَا كَمَا فِي رِوَايَتِهِ. " if LAST >= 51 else "")
 + "وَشَرْحُ الْبَيْتَيْنِ ٣ وَ٤ فِي هٰذِهِ الطَّبْعَةِ مَكْتُوبٌ عَلَيْهِ «لَيْسَ لِلزَّوْزَنِيِّ». الضَّبْطُ طَبَقَتَانِ: مَا شَكَلَتْهُ الطَّبْعَةُ أُبْقِيَ عَلَى حَالِهِ (مَعَ تَوْحِيدِ الرَّسْمِ)، وَمَا تَرَكَتْهُ بِلَا شَكْلٍ ضَبَطَهُ الْمُحَرِّرُ بِدَلَالَةِ الْوَزْنِ وَالشَّرْحِ؛ وَنَصُّ ابْنِ قُتَيْبَةَ لَيْسَ فِي طَبْعَتِهِ إِلَّا الشَّدَّاتُ، فَسَائِرُ شَكْلِهِ مِنَ الْمُحَرِّرِ، وَيَاؤُهُ الْمُتَطَرِّفَةُ الْمُهْمَلَةُ (فى، ضيّعنى) كُتِبَتْ يَاءً مَنْقُوطَةً، وَالْأَلِفُ الْمَقْصُورَةُ الَّتِي رُسِمَتْ يَاءً فِي طَبْعَةِ الزَّوْزَنِيِّ كُتِبَتْ أَلِفًا مَقْصُورَةً. "
 + ("تَصْحِيحُ سَهْوِ النَّصِّ الْإِلِكْتُرُونِيِّ بِشَاهِدٍ: " + "؛ ".join(c[1] for c in _corr) + ". " if _corr else "")
 + "الْإِعْرَابُ رُوجِعَ كَلِمَةً كَلِمَةً عَلَى «فَتْحِ الْكَبِيرِ الْمُتَعَالِ إِعْرَابِ الْمُعَلَّقَاتِ الْعَشْرِ الطِّوَالِ» لِمُحَمَّد عَلِي طٰهٰ الدُّرَّةِ (مَكْتَبَةُ السَّوَادِيِّ، جُدَّةُ، ط ٢، ١٤٠٩ هـ / ١٩٨٩ م)، وَكُتِبَ بِعِبَارَةِ هٰذَا الْمَشْرُوعِ، وَحَيْثُ ذَكَرَ وَجْهَيْنِ قُدِّمَ الْأَوَّلُ وَأُشِيرَ إِلَى الثَّانِي؛ وَعَدُّهُ لِلْأَبْيَاتِ وَتَرْتِيبُهُ يُخَالِفَانِ الزَّوْزَنِيَّ. وَالْمَعَانِي وَشَرْحُ الْغَرِيبِ وَالتَّرْجَمَةُ عَنِ الزَّوْزَنِيِّ. وَالْوُجُوهُ الْبَلَاغِيَّةُ مُسَمَّاةٌ بِأَبْوَابِ «تَلْخِيصِ الْمِفْتَاحِ» لِلْقَزْوِينِيِّ، وَكُلُّ وَجْهٍ قَائِمٌ عَلَى أَحَدِ أَصْلَيْنِ: أَنْ يُسَمِّيَهُ شَارِحٌ أَوْ يَصِفَهُ، أَوْ أَنْ يَنْطَبِقَ عَلَيْهِ حَدُّ التَّلْخِيصِ نَفْسُهُ، وَحِينَئِذٍ يُقَالُ فِيهِ «عَلَى حَدِّ التَّلْخِيصِ»"
 + ("، وَقَدِ اسْتَشْهَدَ التَّلْخِيصُ نَفْسُهُ بِـ" + " وَبِـ".join(c[1] for c in _tal) if _tal else "") + ". "
 + ("تُرِكَ لِنَظَرِ الْعَالِمِ: " + "؛ ".join(c[1] for c in _sch) + "." if _sch else ""))
ATTR_EN = (
 "A RECEIVED text. Chapter 1 is one contiguous span, verbatim, of the entry on Imruʾ al-Qays in Ibn Qutayba (d. 276 AH), «الشعر والشعراء», the edition al-Maktaba al-Shāmila names Dār al-Ḥadīth, Cairo, 1423 AH, vol. 1 p. 109 — from «فبلغه مقتل أبيه» to «حتّى يثأر بأبيه»; nothing is retold. "
 + ("The other chapters give the Muʿallaqa WHOLE — all %d verses — " % TOTAL if _whole else "The other chapters give the Muʿallaqa from its first verse to verse %d of %d (the remaining verses follow in later chapters) — " % (LAST, TOTAL))
 + "in the recension of al-Zawzanī (d. 486 AH), «شرح المعلقات السبع», Dār Iḥyāʾ al-Turāth al-ʿArabī, 1st ed. 1423 AH / 2002 CE, pp. 35–%d: his text, his order and his NUMBERING; no verse is left out and no run is skipped. The verses of each chapter — %s. The metre is al-ṭawīl. " % (LAST_PAGE, _runs_en)
 + ("Of verses 48–51 al-Zawzanī himself notes that most transmitters do not give them in this poem and ascribe them to Taʾabbaṭa Sharran; they stand here as his recension has them. " if LAST >= 51 else "")
 + "In this edition the commentary on verses 3 and 4 is marked «not al-Zawzanī's». VOWELLING, two layers: the vowels the edition prints are kept, normalised to the shelf's spelling; the letters it leaves bare are vowelled by the editor, as the metre and the commentary require. Ibn Qutayba's page prints only the shaddas — every other vowel in chapter 1 is editorial — and its undotted final yāʾ (فى، ضيّعنى) is written ي; an alif maqṣūra that al-Zawzanī's edition prints as a yāʾ is written ى. "
 + ("SLIPS OF THE E-TEXT corrected against a witness (was → now): " + "; ".join(c[2] for c in _corr) + ". " if _corr else "")
 + "THE IʿRĀB of every verse token was checked against Muḥammad ʿAlī Ṭāhā al-Durra, «فتح الكبير المتعال إعراب المعلقات العشر الطوال» (Maktabat al-Sawādī, Jidda, 2nd ed. 1409 AH / 1989 CE, vol. 1) and written in the shelf's own wording; where he gives two readings the first is given and the second mentioned, and where al-Zawzanī's explanation requires another parse the line says so. His recension counts and orders the verses differently. The meanings, the glosses of the rare words and the translations follow al-Zawzanī; the amatory verses are translated plainly, as he explains them. THE FIGURES are named in the categories of al-Qazwīnī's Talkhīṣ al-Miftāḥ, each on one of two bases: a commentator (al-Zawzanī, al-Tibrīzī, al-Durra) names or describes it, or it meets the Talkhīṣ's own definition exactly — and then its line says «by the Talkhīṣ's definition»"
 + ("; the Talkhīṣ itself cites " + " and ".join(c[2] for c in _tal) if _tal else "") + ". "
 + ("LEFT FOR THE SCHOLAR: " + "; ".join(c[2] for c in _sch) + "." if _sch else ""))
ATTR_TR = (
 "MERVÎ (alınmış) metin. 1. bölüm, İbn Kuteybe'nin (ö. 276 h.) «الشعر والشعراء» adlı eserindeki İmruülkays maddesinden kesintisiz ve harfiyen alınmış tek bir parçadır (el-Mektebetü'ş-Şâmile'nin Dârü'l-Hadîs, Kahire, 1423 h. olarak andığı baskı, 1/109): «فبلغه مقتل أبيه»den «حتّى يثأر بأبيه»e kadar; hiçbir şey yeniden anlatılmamıştır. "
 + ("Diğer bölümler Muallaka'yı BÜTÜNÜYLE — %d beytin tamamını — " % TOTAL if _whole else "Diğer bölümler Muallaka'yı ilk beytinden %d. beytine kadar (toplam %d beyit; kalan beyitler sonraki bölümlerde gelecektir) — " % (LAST, TOTAL))
 + "Zevzenî'nin (ö. 486 h.) rivayetiyle verir («شرح المعلقات السبع», Dâru İhyâi't-Türâsi'l-Arabî, 1. baskı 1423 h. / 2002 m., s. 35–%d): metin, sıra ve beyit NUMARALARI onundur; hiçbir beyit dışarıda bırakılmamış, hiçbir yer atlanmamıştır. Bölümlerin beyitleri — %s. Kasidenin vezni tavîldir. " % (LAST_PAGE, _runs_tr)
 + ("48–51. beyitler hakkında Zevzenî, imamların çoğunun bunları bu kasidede rivayet etmediğini ve Teebbeta Şerran'a nisbet ettiğini bizzat belirtir; burada onun rivayetindeki gibi yer alırlar. " if LAST >= 51 else "")
 + "Bu baskıda 3. ve 4. beyitlerin şerhine «Zevzenî'ye ait değildir» notu düşülmüştür. HAREKELEME iki katmandır: baskının bastığı harekeler korunmuş, yalnızca rafın imlâsına uydurulmuştur; baskının harekesiz bıraktığı harfleri editör, veznin ve şerhin gerektirdiği şekilde harekelemiştir. İbn Kuteybe'nin sayfasında yalnız şeddeler basılıdır — 1. bölümdeki diğer bütün harekeler editöre aittir — ve noktasız son yâ (فى، ضيّعنى) «ي» ile yazılmıştır; Zevzenî baskısında yâ olarak dizilen elif-i maksûre de «ى» ile yazılmıştır. "
 + ("E-METNİN bir şahide dayanılarak düzeltilen SEHİVLERİ (eski → yeni): " + "; ".join(c[3] for c in _corr) + ". " if _corr else "")
 + "İ'RÂB: beyitlerdeki her kelimenin i'râbı Muhammed Ali Tâhâ ed-Dürre'nin «فتح الكبير المتعال إعراب المعلقات العشر الطوال» adlı eseriyle (Mektebetü's-Sevâdî, Cidde, 2. baskı 1409 h. / 1989 m., 1. cilt) karşılaştırılmış ve rafın kendi ifadesiyle yazılmıştır; iki vecih verdiği yerde birincisi esas alınmış, ikincisine işaret edilmiş; Zevzenî'nin açıklamasının başka bir i'râbı gerektirdiği yerde bu, satırda belirtilmiştir. Onun rivayeti beyitleri farklı sayar ve sıralar. Mânâlar, garîb kelimelerin açıklamaları ve çeviriler Zevzenî'ye dayanır; gazel beyitleri onun açıkladığı şekilde, sade bir dille çevrilmiştir. SANATLAR Kazvînî'nin Telhîsü'l-Miftâh'ındaki başlıklarla adlandırılmıştır; her sanat iki esastan birine dayanır: ya bir şârih (Zevzenî, Tebrîzî, Dürre) onu adlandırır yahut tarif eder, ya da Telhîs'in kendi tarifine tam olarak uyar — bu durumda satırda «Telhîs'in tarifine göre» denir"
 + ("; Telhîs'in kendisi " + " ve ".join(c[3] for c in _tal) + " şahit getirir" if _tal else "") + ". "
 + ("ÂLİMİN NAZARINA BIRAKILANLAR: " + "; ".join(c[3] for c in _sch) + "." if _sch else ""))

MANIFEST = {
 "id": SLUG,
 "storyGroup": SLUG,
 "title": {"ar": "مُعَلَّقَةُ امْرِئِ الْقَيْسِ", "en": "The Muʿallaqa of Imruʾ al-Qays", "tr": "İmruülkays'ın Muallakası"},
 "subtitle": {"ar": "خَبَرُ الشَّاعِرِ عِنْدَ ابْنِ قُتَيْبَةَ، ثُمَّ مُعَلَّقَتُهُ بِرِوَايَةِ الزَّوْزَنِيِّ بَيْتًا بَيْتًا، مَعَ الْإِعْرَابِ وَالْبَلَاغَةِ",
              "en": "The poet's story from Ibn Qutayba, then his Muʿallaqa in al-Zawzanī's recension, verse by verse, with full iʿrāb and the figures of balāgha",
              "tr": "Şairin İbn Kuteybe'deki haberi, ardından Zevzenî rivayetiyle Muallakası — beyit beyit, tam i'râb ve belâgat sanatlarıyla"},
 "level": 6,
 "levelName": "Master",
 "version": "0.1.0",
 "published": "2026-11-20",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {"ar": N(ATTR_AR), "en": ATTR_EN, "tr": ATTR_TR, "reviewStatus": "pending-scholarly-review"},
}
import shutil
if (PKG / "chapters").exists(): shutil.rmtree(PKG / "chapters")      # a chapter file from an earlier layout must not survive
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("published: khabar + verses 1–%d of %d (%d chapters); authored and waiting: %s" % (LAST, TOTAL, len(CHAPS), sorted(n for n in VERSE if n > LAST)))
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
