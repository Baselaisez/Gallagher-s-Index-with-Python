"""Author content/samples/mathal-bi-khuffay-hunayn — «رَجَعَ فُلَانٌ مِنْ حَاجَتِهِ بِخُفَّيْ حُنَيْنٍ», the proverbs' shelf (v348-A), Level 4.

RECEIVED TEXT: Abū ʿUbayd's proverb (as «the common people's proverb») and the FIRST of the reports al-Bakrī gives for it — Abū al-Yaqẓān's,
of Ḥunayn who claimed kinship in Quraysh and came back from ʿAbd al-Muṭṭalib rejected — «فصل المقال» (Shamela 1025, p. 366 = printed
1:354). The exact passage: research/sources/mathal-bi-khuffay-hunayn-src.txt. Taken from «اختلف العلماء في هذا الخبر» to «فيلبس خف أبيه»;
the second report (Ḥunayn the singer of al-Ḥīra, robbed of his clothes when drunk) is not taken. No correction. Every vowel is ours.
Run: python3 tools/authoring/author_mathal_bi_khuffay_hunayn.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-bi-khuffay-hunayn"
HN = ("حُنَيْنٍ", "Ḥunayn", "Huneyn")
AM = ("عَبْدِ الْمُطَّلِبِ", "ʿAbd al-Muṭṭalib", "Abdülmuttalib")
def HUNAYN(role, punct=None):
    m = (" — عَلَمٌ مُنْصَرِفٌ", " — a fully declined name", " — munsarif alem")
    if role == "ismk": return ISMK("حُنَيْنٌ", "hunayn", "propn", note_ar=m[0], note_en=m[1], note_tr=m[2], punct=punct)
    if role == "fail": return FAIL("حُنَيْنٌ", "hunayn", "propn", note_ar=m[0], note_en=m[1], note_tr=m[2], punct=punct)
def KHUFFAY(full, enc=None, punct=None, note=("", "", "")):
    """بِخُفَّيْ / بِخُفَّيْهِ: the dual in jarr, its nun dropped for the annexation"""
    stem = "خُفَّيْ"
    encs = ("، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", ", annexed to «his», the pronoun in the seat of jarr", "; «onun» zamirine muzâf, zamir mahallen mecrûr") if enc else ("", "", "")
    segs = [seg("بِ", "bi", "prep"), seg(stem, "khuff", "noun")] + ([seg(enc, PRON[enc], "pron")] if enc else [])
    return tok(full, "bi", "prep", ["huruf-jarr", "al-muthanna", "idafa-definiteness"] + (["al-bariz-al-muttasil"] if enc else []),
        "الْبَاءُ حَرْفُ جَرٍّ لِلْمُصَاحَبَةِ، وَخُفَّيْ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ" + encs[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ: أَيْ مُصْطَحِبًا خُفَّيْهِ" + note[0] + ".",
        "The ba of company, a jarr letter; «two boots» is in jarr by the ya, a dual whose nun drops for the annexation" + encs[1] + " — the phrase hangs on an omitted hal: «having (nothing but) the two boots»" + note[1] + ".",
        "Bâ musâhabe içindir (cer harfi); «iki mest» tesniye olduğu için yâ ile mecrûr, izâfet için nûnu düşmüş, muzâf" + encs[2] + " — câr-mecrûr mahzûf hâle müteallik: «iki mestiyle»" + note[2] + ".", punct=punct, segments=segs)

TITLES = [{"ar": "بِخُفَّيْ حُنَيْنٍ", "en": "With Ḥunayn's Two Boots", "tr": "Huneyn'in Mestleriyle"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "So-and-so came back from his errand with Ḥunayn's two boots.", "tr": "Falan, işinden Huneyn'in mestleriyle döndü (eli boş döndü)."},
 "tokens": [MADI("رَجَعَ", "rajaa", **W(FAIL_BAAD, HEAD_CL)),
  FAIL("فُلَانٌ", "fulan", note_ar=" — كِنَايَةٌ عَنِ اسْمِ الْعَاقِلِ", note_en=" — a stand-in for a person's name", note_tr=" — akıl sahibinin adına kinâye"),
  PREP("مِنْ", "min", " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَجَعَ»", "; the phrase hangs on «came back»", "; câr-mecrûr «döndü»ye müteallik", gloss_tr="«-den»"),
  ENC_NOUN("حَاجَتِهِ", "haja", "هِ", "majr"),
  KHUFFAY("بِخُفَّيْ"), NM("حُنَيْنٍ", "hunayn", MUNSARIF, punct=".")]})
S1.append({"id": "s2", "translation": {"en": "The learned differ about this report.", "tr": "Âlimler bu haber hakkında ihtilâf etmişlerdir."},
 "tokens": [MADI("اخْتَلَفَ", "ikhtalafa", ["form-viii-verbs"], **W(FAIL_BAAD)),
  FAIL("الْعُلَمَاءُ", "alim-scholar", extra=["jam-taksir"], note_ar=" — جَمْعُ عَالِمٍ", note_en=" — the plural of عَالِم", note_tr=" — âlim'in çoğulu"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«اخْتَلَفَ»", "; the phrase hangs on «differ»", "; câr-mecrûr «ihtilâf etti»ye müteallik"),
  ISHARA("هٰذَا", "hadha", "جَرٍّ", "jarr", "mecrûr"), BADAL("الْخَبَرِ", "khabar", "jarr", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "Abū al-Yaqẓān said: Ḥunayn was a man who had laid claim to a place in Quraysh and traced himself to Asad ibn Hāshim.", "tr": "Ebü'l-Yakzân dedi ki: Huneyn, Kureyş'e mensup olduğunu iddia eden ve kendini Esed b. Hâşim'e nispet eden bir adamdı."},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))),
  tok("أَبُو", "ab", "noun", ["fail", "five-nouns", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ.", "The doer (fa'il), in raf' by the waw — one of the five nouns; annexed.", "Fâil, esmâ-i hamseden olduğu için vâv ile merfû; muzâf."),
  NM("الْيَقْظَانِ", "yaqzan", (" — وَأَبُو الْيَقْظَانِ كُنْيَةُ الْأَخْبَارِيِّ عَامِرِ بْنِ حَفْصٍ", " — Abū al-Yaqẓān is the kunya of the reporter ʿĀmir ibn Ḥafṣ", " — Ebü'l-Yakzân, ahbârî Âmir b. Hafs'ın künyesi"), punct=":"),
  NOTE(KANA("كَانَ"), " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekūlü'l-kavl, mahallen mansûb"),
  HUNAYN("ismk"), KHK("رَجُلًا", "rajul"),
  tok("قَدِ", "qad", "part", ["qad-harf"], "حَرْفُ تَحْقِيقٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "قَدْ affirms the past verb after it; it takes kasra where two sukuns meet.", "Kad tahkîk harfi; iki sâkin karşılaştığı için kesre ile harekelenmiştir."),
  MADI_ALIF("ادَّعَى", "iddaa", ["form-viii-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«رَجُلًا»", note_en=" — the clause qualifies «a man», in the seat of nasb", note_tr=" — cümle «adam»ın na'tı, mahallen mansûb"),
  NOTE(FI(), " — وَادَّعَى فِي الْقَوْمِ: انْتَسَبَ إِلَيْهِمْ وَلَيْسَ مِنْهُمْ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«ادَّعَى»", "; ادَّعَى فِي قَوْمٍ: to claim to belong to a people one is not of; the phrase hangs on «laid claim»", "; ادَّعَى فِي قَوْمٍ: bir kavme olmadığı hâlde nispet iddia etmek; câr-mecrûr fiile müteallik"),
  MAJR("قُرَيْشٍ", "quraysh", "propn", note_ar=" — عَلَمٌ عَلَى الْقَبِيلَةِ، مَصْرُوفٌ عَلَى إِرَادَةِ الْحَيِّ", note_en=" — the tribe's name, declined as the name of the clan", note_tr=" — kabile adı, «hay» (boy) kastıyla munsarif", punct="،"),
  MADI_ALIF("وَانْتَمَى", "intama", ["form-viii-verbs"], hidden=True, note_ar=" — وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى «ادَّعَى»", note_en=" — the clause is conjoined to «laid claim»", note_tr=" — cümle «iddia etti»ye ma'tûf"),
  NOTE(ILA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«انْتَمَى»", "; the phrase hangs on «traced himself»", "; câr-mecrûr «nispet etti»ye müteallik"),
  MAJR("أَسَدِ", "asad", "propn", note_ar=NO_TANWIN[0], note_en=NO_TANWIN[1], note_tr=NO_TANWIN[2]), BN("jarr", ("أَسَدِ", "Asad", "Esed")), NM("هَاشِمٍ", "hashim", MUNSARIF, punct=".")]})
S1.append({"id": "s4", "translation": {"en": "He came to ʿAbd al-Muṭṭalib wearing two red boots and said: «Uncle, I am your nephew, the son of Asad ibn Hāshim.»", "tr": "Ayağında iki kırmızı mest olduğu hâlde Abdülmuttalib'e geldi ve: «Amca, ben kardeşin Esed b. Hâşim'in oğluyum» dedi."},
 "tokens": [ISTI(MADI("فَجَاءَ", "jaa", ["hollow-verbs", "mahmuz-verbs"], hidden=True, **W(HID(*HN)))),
  NOTE(ILA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«جَاءَ»", "; the phrase hangs on «came»", "; câr-mecrûr «geldi»ye müteallik"),
  MAJR("عَبْدِ", "abd", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), NM("الْمُطَّلِبِ", "muttalib", (" — وَعَبْدُ الْمُطَّلِبِ جَدُّ النَّبِيِّ ﷺ", " — ʿAbd al-Muṭṭalib is the grandfather of the Prophet ﷺ", " — Abdülmuttalib, Peygamber'in ﷺ dedesi")),
  tok("وَعَلَيْهِ", "ala", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَعَلَى حَرْفُ جَرٍّ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ مُقَدَّمٍ.",
      "The waw of state; عَلَى «on» with «him» — the phrase hangs on an omitted, fronted predicate.", "Vâv hâliyye; alâ cer harfi, «o» zamiri mahallen mecrûr — câr-mecrûr öne alınmış mahzûf habere müteallik.", segments=[seg("وَ", "wa", "conj"), seg("عَلَيْ", "ala", "prep"), seg("هِ", "pron-3ms", "pron")]),
  tok("خُفَّانِ", "khuff", "noun", ["mubtada-khabar", "al-muthanna"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «جَاءَ».", "The mubtada placed after its predicate, in raf' by the alif — a dual; the clause is a hal of the doer of «came», in the seat of nasb.", "Muahhar mübtedâ, tesniye olduğu için elif ile merfû — cümle «geldi»nin fâilinden hâl, mahallen mansûb."),
  tok("أَحْمَرَانِ", "ahmar", "noun", ["naat-sifa", "al-muthanna"], "نَعْتٌ لِـ«خُفَّانِ» مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى — وَالْمُثَنَّى يُنَوَّنُ بِالنُّونِ وَإِنْ كَانَ مُفْرَدُهُ (أَحْمَرُ) مَمْنُوعًا مِنَ الصَّرْفِ.", "An adjective of «two boots», in raf' by the alif — a dual (the dual keeps its nun though the singular أَحْمَر is a diptote).", "«İki mest»in na'tı, tesniye olduğu için elif ile merfû (müfredi أَحْمَر gayr-i munsarif olsa da tesniye nûnunu alır).", punct="،"),
  QALA("وَقَالَ", hidden=True, punct=":"), YA(),
  tok("عَمِّ", "amm-uncle", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness"], "مُنَادًى مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ الْمَحْذُوفَةِ، وَالْكَسْرَةُ دَلِيلٌ عَلَيْهَا، مُضَافٌ، وَالْيَاءُ الْمَحْذُوفَةُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A vocative in nasb by a fatha estimated before the speaker's ya, which is dropped (the kasra points to it); annexed to that ya, in the seat of jarr: «my uncle».", "Münâdâ; düşen mütekellim yâ'sından önce takdîrî fetha ile mansûb (kesre yâ'ya delâlet eder); muzâf, mahzûf yâ muzâfun ileyh: «amcacığım».", punct="،"),
  tok("أَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun built on sukun, in the seat of raf' as the mubtada.", "Munfasıl zamir, sükûn üzere mebnî, mübtedâ olarak mahallen merfû."),
  KHABAR("ابْنُ", "ibn", ["idafa-definiteness"], note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  tok("أَخِيكَ", "akh", "noun", ["idafa-definiteness", "five-nouns", "al-bariz-al-muttasil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The second term of the idafa, in jarr by the ya — one of the five nouns; annexed to «your».", "Muzâfun ileyh, esmâ-i hamseden olduğu için yâ ile mecrûr; «senin» zamirine muzâf.", segments=[seg("أَخِي", "akh", "noun"), seg("كَ", "pron-2ms", "pron")]),
  tok("أَسَدِ", "asad", "propn", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"], "بَدَلٌ مِنْ «أَخِيكَ» مَجْرُورٌ بِالْكَسْرَةِ" + NO_TANWIN[0] + ".", "A badal of «your brother», in jarr" + NO_TANWIN[1] + ".", "«Kardeşin»den bedel, mecrûr" + NO_TANWIN[2] + "."),
  BN("jarr", ("أَسَدِ", "Asad", "Esed")), NM("هَاشِمٍ", "hashim", MUNSARIF, punct=".")]})
S1.append({"id": "s5", "translation": {"en": "ʿAbd al-Muṭṭalib said: «No — by the garments of Hāshim, I do not know in you the traits of Hāshim.»", "tr": "Abdülmuttalib dedi ki: «Hayır! Hâşim'in elbiselerine andolsun, sende Hâşim'in huylarından bir iz göremiyorum.»"},
 "tokens": [ISTI(MADI("فَقَالَ", "qala", ["hollow-verbs", "maful-bihi"], **W(FAIL_BAAD))),
  FAIL("عَبْدُ", "abd", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]), NM("الْمُطَّلِبِ", "muttalib", punct=":"),
  tok("لَا", "la-jawab", "part", [], "حَرْفُ جَوَابٍ لِنَفْيِ مَا ادَّعَاهُ، مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "The answering «no», denying his claim; built on sukun, with no seat.", "«Hayır» cevap harfi, iddiasını reddeder; sükûn üzere mebnî, mahalli yoktur."),
  tok("وَثِيَابِ", "thawb", "noun", ["huruf-al-qasam-fil-kafiya", "huruf-jarr", "idafa-definiteness"], "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَثِيَابِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلِ قَسَمٍ مَحْذُوفٍ تَقْدِيرُهُ: أُقْسِمُ.",
      "The waw of the oath, a jarr letter; «garments» (plural of ثَوْب) is what is sworn by, in jarr, annexed — the phrase hangs on an omitted «I swear».", "Vâv kasem ve cer harfi; «elbiseler» (sevb'in çoğulu) mukseme bih, mecrûr, muzâf — câr-mecrûr mahzûf «yemin ederim» fiiline müteallik.", segments=[seg("وَ", "wa-qasam", "prep"), seg("ثِيَابِ", "thawb", "noun")]),
  NM("هَاشِمٍ", "hashim", MUNSARIF, punct="،"),
  tok("مَا", "ma-nafiya", "part", ["anwa-ma"], "حَرْفُ نَفْيٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا عَمَلَ لَهُ — وَالْجُمْلَةُ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا.", "The negating مَا, built on sukun, governing nothing — the clause answers the oath and has no seat.", "Nefy mâ'sı, sükûn üzere mebnî, amel etmez — cümle kasemin cevabı, mahalli yoktur."),
  MUDARI("أَعْرِفُ", "arafa", who="أَنَا", wujub=True),
  JARR_PRON("فِيكَ", "fi", "فِي", "كَ", " («sende»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَعْرِفُ»", note_en=" — the phrase hangs on «know»", note_tr=" — câr-mecrûr «tanırım»a müteallik"),
  MAFUL("شَمَائِلَ", "shimal", extra=["jam-taksir", "mamnu-min-sarf"], note_ar="، مُضَافٌ — جَمْعُ شِمَالٍ، وَهِيَ الْخَلِيقَةُ، عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ", note_en=", annexed — plural of شِمَال (a trait of character), on the «ultimate plural» pattern", note_tr=", muzâf — şimâl'in (huy, seciye) çoğulu, müntehe'l-cumû' vezninde"),
  NM("هَاشِمٍ", "hashim", MUNSARIF, punct=".")]})
S1.append({"id": "s6", "translation": {"en": "So he went back from him, disappointed, to his people, and they said: «Ḥunayn has come back with his two boots» —", "tr": "Bunun üzerine eli boş olarak onun yanından kavmine döndü; onlar da: «Huneyn mestleriyle döndü» dediler —"},
 "tokens": [ISTI(MADI("فَرَجَعَ", "rajaa", hidden=True, **W(HID(*HN)))),
  JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)", note_ar=" — وَالْهَاءُ لِعَبْدِ الْمُطَّلِبِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَجَعَ»", note_en=" — «him» is ʿAbd al-Muṭṭalib; the phrase hangs on «went back»", note_tr=" — zamir Abdülmuttalib'e döner; câr-mecrûr «döndü»ye müteallik"),
  HAL("خَائِبًا", "khaib", extra=["ism-fail"], note_ar=" — اسْمُ فَاعِلٍ مِنْ خَابَ", note_en=" — the active participle of خَابَ «to fail, be disappointed»", note_tr=" — hâbe'nin ism-i fâili: «eli boş, ümidi kırık»"),
  NOTE(ILA(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَجَعَ»", "; the phrase hangs on «went back»", "; câr-mecrûr «döndü»ye müteallik"),
  ENC_NOUN("قَوْمِهِ", "qawm", "هِ", "majr", punct="،"),
  VERB_WAW("فَقَالُوا", "qala", ["hollow-verbs", "maful-bihi"], punct=":"),
  NOTE(MADI("رَجَعَ", "rajaa", **W(FAIL_BAAD)), " — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ", "; the clause is what is said, in the seat of nasb", "; cümle mekūlü'l-kavl, mahallen mansûb"),
  HUNAYN("fail"), KHUFFAY("بِخُفَّيْهِ", enc="هِ", punct="،")]})
S1.append({"id": "s7", "translation": {"en": "that is, he came back not accepted, so as to wear his father's boot.", "tr": "yani kabul edilmeden döndü de babasının mestini giyemedi."},
 "tokens": [tok("أَيْ", "ay", "part", [], "حَرْفُ تَفْسِيرٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "أَيْ «that is», the particle of explanation, built on sukun, with no seat.", "Ey tefsir harfi, sükûn üzere mebnî, mahalli yoktur.", punct=":"),
  NOTE(MADI("رَجَعَ", "rajaa", hidden=True), " — وَالْجُمْلَةُ تَفْسِيرِيَّةٌ لَا مَحَلَّ لَهَا", "; the clause explains and has no seat", "; cümle tefsîriyye, mahalli yoktur"),
  LAM_JAZM(),
  tok("يُقْبَلْ", "qabila", "verb", ["nawasib-wa-jawazim-al-mudari", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنْ فَاعِلِ «رَجَعَ».",
      "Present verb in the passive, in jazm by لَمْ, its sign the sukun; its deputy doer is the hidden «he» — the clause is a hal of the doer of «came back», in the seat of nasb.", "Meçhul muzâri, lem ile meczûm, alâmeti sükûn; nâib-i fâil gizli «o» — cümle «döndü»nün fâilinden hâl, mahallen mansûb."),
  tok("فَيَلْبَسَ", "labisa", "verb", ["nawasib-wa-jawazim-al-mudari"], "الْفَاءُ فَاءُ السَّبَبِيَّةِ، وَيَلْبَسَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا بَعْدَ فَاءِ السَّبَبِيَّةِ فِي جَوَابِ النَّفْيِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "The fa of consequence; «wear» is a present verb in nasb by an أَنْ that must stay hidden after the fa answering a negation, its sign the fatha; its doer the hidden «he».", "Sebebiyye fâsı; yelbese, nefyin cevabında sebebiyye fâsından sonra vücûben gizli «en» ile mansûb muzâri, alâmeti fetha; fâil gizli «o».", segments=[seg("فَ", "fa", "conj"), seg("يَلْبَسَ", "labisa", "verb")]),
  MAFUL("خُفَّ", "khuff", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  tok("أَبِيهِ", "ab", "noun", ["idafa-definiteness", "five-nouns", "al-bariz-al-muttasil"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "The second term of the idafa, in jarr by the ya — one of the five nouns; annexed to «his».", "Muzâfun ileyh, esmâ-i hamseden olduğu için yâ ile mecrûr; «onun» zamirine muzâf.", punct=".", segments=[seg("أَبِي", "ab", "noun"), seg("هِ", "pron-3ms", "pron")])]})

NEW_GLOSS = {
 "hunayn": NP("حُنَيْن", "Ḥunayn — a man's name, fully declined; in the proverb بِخُفَّيْ حُنَيْنٍ «with Ḥunayn's two boots» — said of one who comes back empty-handed", "Huneyn — erkek ismi, munsarif; بِخُفَّيْ حُنَيْنٍ «Huneyn'in mestleriyle» atasözünde: eli boş dönen için söylenir"),
 "muttalib": NP("الْمُطَّلِب", "al-Muṭṭalib — a man's name; عَبْدُ الْمُطَّلِبِ ʿAbd al-Muṭṭalib (Shayba ibn Hāshim), the grandfather of the Prophet ﷺ", "el-Muttalib — erkek ismi; عَبْدُ الْمُطَّلِبِ Abdülmuttalib (Şeybe b. Hâşim), Peygamber'in ﷺ dedesi"),
 "intama": NV("اِنْتَمَى", "ن م ي", "VIII", "to trace one's descent (إِلَى: to), to claim kinship with (Form VIII, defective)", "(إِلَى: birine) soyunu dayandırmak, mensubiyet iddia etmek (iftiâl bâbı, nâkıs)"),
 "khaib": NN("خَائِب", "خ ي ب", "disappointed, frustrated, empty-handed (the active participle of خَابَ)", "eli boş, ümidi boşa çıkmış (hâbe'nin ism-i fâili)"),
}
GLOSS_HERE = {
 "yaqzan": ("al-Yaqẓān (awake) — here in the kunya Abū al-Yaqẓān of ʿĀmir ibn Ḥafṣ «Suḥaym» (d. 190 AH), the reporter of Arab history and genealogy", "el-Yakzân (uyanık) — burada ahbâr ve ensâb râvîsi Âmir b. Hafs «Suhaym»ın (ö. 190) künyesi Ebü'l-Yakzân'da"),
 "asad": ("Asad (lion) — here the name Asad ibn Hāshim, the brother of ʿAbd al-Muṭṭalib", "Esed (aslan) — burada Abdülmuttalib'in kardeşi Esed b. Hâşim'in adı"),
 "hashim": ("Hāshim — Hāshim ibn ʿAbd Manāf, the father of ʿAbd al-Muṭṭalib and of Asad", "Hâşim — Abdülmuttalib'in ve Esed'in babası Hâşim b. Abdümenâf"),
 "shimal": ("left, the left hand; (a trait of character) pl. شَمَائِل — the traits, the ways of a man", "sol, sol el; (huy, seciye) çoğ. شَمَائِل — kişinin huyları, tavırları"),
}
V = {"intama": SG.derived_naqis(SG.B8 + " — نَاقِصٌ", SG.W8, "َ", "اِنْتَمَ", "نْتَم", "i", "اِنْتَم", "اِنْتِمَاء", "مُنْتَمٍ", None, None, None, "نَاقِصٌ يَائِيٌّ مِنَ الِافْتِعَالِ: انْتَمَى إِلَيْهِ يَنْتَمِي — انْتَسَبَ؛ لَازِمٌ.")}
FOR_HOCA = [
 ("«لَمْ يُقْبَلْ فَيَلْبَسَ خُفَّ أَبِيهِ»: the passive «يُقْبَلْ» and the nasb of «فَيَلْبَسَ» after the fa of consequence (or raf' «فَيَلْبَسُ»); the sense of the gloss is not plain", "«لَمْ يُقْبَلْ فَيَلْبَسَ خُفَّ أَبِيهِ»: meçhul «يُقْبَلْ» ve sebebiyye fâsından sonra «فَيَلْبَسَ»nin nasbı (ya da merfû «فَيَلْبَسُ»); açıklamanın mânâsı açık değil"),
 ("«قُرَيْشٍ» declined (the clan) — the diptote «قُرَيْشَ» (the tribe) is also allowed", "«قُرَيْشٍ» munsarif (hay kastıyla); kabile kastıyla gayr-i munsarif «قُرَيْشَ» de caizdir"),
 ("«لَا وَثِيَابِ هَاشِمٍ»: لَا read as the answering «no» before the oath", "«لَا وَثِيَابِ هَاشِمٍ»: lâ, kasemden önce cevap «hayır» okundu"),
]
MANIFEST = manifest(SLUG, level=4, title=TITLES[0],
    subtitle={"ar": "حُنَيْنٌ عِنْدَ عَبْدِ الْمُطَّلِبِ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "Ḥunayn before ʿAbd al-Muṭṭalib — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Huneyn, Abdülmuttalib'in huzurunda — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="p. 366 (printed 1:354), bāb 11", pages_ar="ص ٣٦٦ (الْمَطْبُوعُ ١: ٣٥٤)، الْبَابُ الْحَادِيَ عَشَرَ",
    span_en="Abū ʿUbayd's proverb as the heading; al-Bakrī's first report, Abū al-Yaqẓān's, whole — from «اختلف العلماء في هذا الخبر» to «فيلبس خف أبيه»; the second report (Ḥunayn the singer, robbed when drunk) is not taken",
    span_tr="Başlıkta Ebû Ubeyd'in atasözü; Bekrî'nin ilk rivâyeti (Ebü'l-Yakzân'ınki) tamamen — «اختلف العلماء في هذا الخبر»den «فيلبس خف أبيه»ye; ikinci rivâyet (sarhoşken soyulan şarkıcı Huneyn) alınmadı",
    span_ar="الْمَثَلُ عُنْوَانًا، ثُمَّ رِوَايَةُ أَبِي الْيَقْظَانِ كُلُّهَا مِنْ «اخْتَلَفَ الْعُلَمَاءُ فِي هٰذَا الْخَبَرِ» إِلَى «فَيَلْبَسَ خُفَّ أَبِيهِ»، وَلَمْ تُؤْخَذِ الرِّوَايَةُ الثَّانِيَةُ",
    hoca=FOR_HOCA)
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, GLOSS_HERE, V_NEW=V)
