"""Author content/samples/mathal-arafatni-nasaaha-allah — «عَرَفَتْنِي نَسَأَهَا اللهُ», the proverbs' shelf (v348-A), Level 4.

RECEIVED TEXT: Abū ʿUbayd's entry «ومن الدعاء قولهم: عرفتني نسأها الله» as al-Bakrī's «فصل المقال» carries it (Shamela 1025, p. 90 =
printed 1:78): the proverb, its gloss and the two origins he gives — the man whose lost mare knew his voice, and Bayhas «Naʿāma» whose
wife knew him by night. The exact passage: research/sources/mathal-arafatni-nasaaha-allah-src.txt. Taken whole, from the proverb to
«فقال: عرفتني، نسأها الله»; al-Bakrī's commentary after it is not taken. No correction; orthography only: «ايدي» is written «أَيْدِي»,
and the stray colon of «امرأته: بليل» is not carried over. Every vowel is ours.
Run: python3 tools/authoring/author_mathal_arafatni_nasaaha_allah.py
"""
import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from amthal_common import *

SLUG = "mathal-arafatni-nasaaha-allah"
def ARAFATNI(note=("", "", ""), punct=None):
    return tok("عَرَفَتْنِي", "arafa", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim"],
        "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ" + note[0] + ".",
        "Past verb built on fatha; the ta marks the feminine, its doer the hidden «she»; the nun guards the verb and the ya «me» is its object, in the seat of nasb" + note[1] + ".",
        "Fetha üzere mebnî mâzî; tâ te'nîs, fâil gizli «o» (dişil); nûn vikâye, yâ mef'ûlün bih, mahallen mansûb" + note[2] + ".", punct=punct,
        segments=[seg("عَرَفَتْ", "arafa", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
def NASAAHA(punct=None):
    return [tok("نَسَأَهَا", "nasaa", "verb", ["thulathi-mujarrad-babs", "al-bariz-al-muttasil", "maful-bihi", "mahmuz-verbs"],
        "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ خَبَرِيَّةٌ لَفْظًا دُعَائِيَّةٌ مَعْنًى لَا مَحَلَّ لَهَا.",
        "Past verb built on fatha; «her» is its object in the seat of nasb, and its doer follows — a statement in form, a prayer in meaning, with no seat.",
        "Fetha üzere mebnî mâzî; «hâ» mef'ûlün bih, mahallen mansûb; fâili sonra gelir — lafzen haber, mânen dua cümlesi, mahalli yoktur.",
        segments=[seg("نَسَأَ", "nasaa", "verb"), seg("هَا", "pron-3fs", "pron")]), ALLAH_F(punct=punct)]

TITLES = [{"ar": "عَرَفَتْنِي نَسَأَهَا اللهُ", "en": "She Knew Me — God Lengthen Her Days", "tr": "Beni Tanıdı — Allah Ömrünü Uzatsın"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "She knew me — may God lengthen her days!", "tr": "Beni tanıdı — Allah ömrünü uzatsın!"},
 "tokens": [ARAFATNI(HEAD_CL), *NASAAHA(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "That is: may God put off her appointed end, and make her life long.", "tr": "Yani: Allah ecelini geciktirsin, ömrünü uzun etsin."},
 "tokens": [tok("أَيْ", "ay", "part", [], "حَرْفُ تَفْسِيرٍ مَبْنِيٌّ عَلَى السُّكُونِ لَا مَحَلَّ لَهُ.", "أَيْ «that is», the particle of explanation, built on sukun, with no seat.", "Ey tefsir harfi, sükûn üzere mebnî, mahalli yoktur.", punct=":"),
  MADI("أَخَّرَ", "akhkhara", ["form-ii-verbs"], **W(FAIL_BAAD, (" — وَالْجُمْلَةُ تَفْسِيرِيَّةٌ دُعَائِيَّةٌ", "; an explaining clause, a prayer", "; tefsîriyye cümle, dua"))), ALLAH_F(),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أَخَّرَ»", "; the phrase hangs on «put off»", "; câr-mecrûr «geciktirdi»ye müteallik"),
  ENC_NOUN("أَجَلِهَا", "ajal", "هَا", "majr", punct="،"),
  MADI("وَأَطَالَ", "atala", ["form-iv-verbs", "hollow-verbs"], hidden=True, note_ar=" — وَالْفَاعِلُ ضَمِيرٌ يَعُودُ عَلَى اللهِ", note_en=" — the doer is a pronoun referring to God", note_tr=" — fâil Allah'a dönen zamir"),
  ENC_NOUN("عُمْرَهَا", "umr", "هَا", "maful", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "He said: Its origin was that a man had a mare, and she was taken from him;", "tr": "Dedi ki: Aslı şudur: Bir adamın bir kısrağı vardı; elinden alındı;"},
 "tokens": [SAYQ("قَالَ", ("الْأَصْمَعِيُّ", "al-Aṣmaʿī", "Asmaî")),
  ISTI(KANA("وَكَانَ")), ENC_NOUN("أَصْلُهُ", "asl", "هُ", "ismk", note_ar=" — وَالْهَاءُ لِلْمَثَلِ", note_en=" — «its» is the proverb's", note_tr=" — zamir atasözüne döner"),
  tok("أَنَّ", "anna", "part", ["inna-wa-akhawatuha", "mawadi-fath-anna"], "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِنْ مَعْمُولَيْهِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.", "أَنَّ «that» — with its noun and predicate it makes a masdar in the seat of nasb, the predicate of كَانَ.", "Enne — ismi ve haberiyle kurduğu müevvel masdar kâne'nin haberi, mahallen mansûb."),
  tok("رَجُلًا", "rajul", "noun", ["inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The noun of أَنَّ, in nasb.", "Enne'nin ismi, mansûb."),
  tok("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ أَنَّ.", "The defective past verb, the ta marking the feminine (its noun «mare» is feminine) — the clause is the predicate of أَنَّ.", "Nâkıs mâzî, tâ te'nîs (ismi «kısrak» müennes) — cümle enne'nin haberi, mahallen merfû."),
  NOTE(LAHU("لَهُ", "pron-3ms", " («onun»)"), "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرِ كَانَ الْمُقَدَّمِ", "; the phrase hangs on the omitted, fronted predicate of كَانَ", "; câr-mecrûr kâne'nin öne alınmış mahzûf haberine müteallik"),
  ISMK("فَرَسٌ", "faras", muakhkhar=True, note_ar=" — وَالْفَرَسُ يَقَعُ عَلَى الذَّكَرِ وَالْأُنْثَى، وَهِيَ هُنَا أُنْثَى", note_en=" — فَرَس serves for horse and mare alike; here a mare", note_tr=" — feres erkek ve dişi için kullanılır; burada kısrak", punct="،"),
  tok("فَأُخِذَتْ", "akhadha", "verb", ["naib-al-fail", "mahmuz-verbs"], "الْفَاءُ عَاطِفَةٌ، وَأُخِذَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ (الْفَرَسُ).", "The fa conjoins; «was taken» is a past verb in the passive, built on fatha; the ta marks the feminine and the deputy doer is the hidden «she» (the mare).", "«bunun üzerine» + meçhul mâzî, fetha üzere mebnî; tâ te'nîs; nâib-i fâil gizli «o» (kısrak).", segments=[seg("فَ", "fa", "conj"), seg("أُخِذَتْ", "akhadha", "verb")]),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«أُخِذَتْ»", note_en=" — the phrase hangs on «was taken»", note_tr=" — câr-mecrûr «alındı»ya müteallik", punct="؛")]})
S1.append({"id": "s4", "translation": {"en": "then afterwards he saw her in the hands of some people; she knew him and whinnied when she heard his voice,", "tr": "sonra onu bir topluluğun elinde gördü; kısrak onu tanıdı ve sesini işitince kişnedi;"},
 "tokens": [THUMMA(), ENC_MADI("رَآهَا", "raa", "هَا", ["mahmuz-verbs", "naqis-verbs"], alif=True, hidden=True, note_ar=" — يَعُودُ عَلَى الرَّجُلِ", note_en=" (the man)", note_tr=" (adam)"),
  ZARF("بَعْدَ", "bada", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«رَآهَا»", note_en="; it hangs on «saw her»", note_tr="; «gördü»ye müteallik"),
  ISHARA("ذٰلِكَ", "dhalika", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr"),
  NOTE(FI(), " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ حَالٍ مِنَ الْهَاءِ فِي «رَآهَا»", "; the phrase hangs on an omitted hal of «her»", "; câr-mecrûr «onu»dan mahzûf hâle müteallik"),
  MAJR("أَيْدِي", "yad", extra=["jam-taksir", "ism-maqsur-manqus"], sign="بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ", note_ar="، مُضَافٌ — جَمْعُ يَدٍ", note_en=" — the kasra is estimated on the ya; annexed — the plural of يَد", note_tr=" — kesre yâ üzerinde takdîrî; muzâf — yed'in çoğulu"),
  MUDAF_ILAYH("قَوْمٍ", "qawm", punct="،"),
  tok("فَعَرَفَتْهُ", "arafa", "verb", ["al-bariz-al-muttasil", "maful-bihi"], "الْفَاءُ عَاطِفَةٌ، وَعَرَفَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ (الْفَرَسُ)، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "The fa conjoins; «knew» is a past verb built on fatha, the ta marking the feminine, its doer the hidden «she» (the mare), and «him» its object.", "«bunun üzerine» + fetha üzere mebnî mâzî; tâ te'nîs, fâil gizli «o» (kısrak), zamir mef'ûlün bih.", segments=[seg("فَ", "fa", "conj"), seg("عَرَفَتْ", "arafa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  MADI("فَحَمْحَمَتْ", "hamhama", ["rubai-babs"], fem=True, hidden=True, note_ar=" — وَحَمْحَمَ الْفَرَسُ: صَوَّتَ يَطْلُبُ الْعَلَفَ أَوْ صَاحِبَهُ", note_en=" — حَمْحَمَ: (of a horse) to whinny for its fodder or its master", note_tr=" — hamhame: atın yem veya sahibi için kişnemesi"),
  ZARF("حِينَ", "hin", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«حَمْحَمَتْ»، مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ", note_en="; it hangs on «whinnied» and is annexed to the clause after it", note_tr="; «kişnedi»ye müteallik, sonraki cümleye muzâf"),
  MADI("سَمِعَتْ", "samia", fem=True, hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «حِينَ» إِلَيْهَا", note_en=" — the clause is in the seat of jarr, annexed to «when»", note_tr=" — cümle «hîne»ye muzâfun ileyh, mahallen mecrûr"),
  ENC_NOUN("كَلَامَهُ", "kalam", "هُ", "maful", punct="،")]})
S1.append({"id": "s5", "translation": {"en": "and at that he said these words.", "tr": "bunun üzerine adam bu sözü söyledi."},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True)),
  ZARF("عِنْدَ", "inda", **ZAMAN, note_ar=" — مُتَعَلِّقٌ بِـ«قَالَ»", note_en="; it hangs on «said»", note_tr="; «dedi»ye müteallik"),
  ISHARA("ذٰلِكَ", "dhalika", "جَرٍّ مُضَافٌ إِلَيْهِ", "jarr as the second term of the idafa", "muzâfun ileyh — mecrûr"),
  ISHARA("هٰذِهِ", "hadhihi", "نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the direct object", "mef'ûlün bih — mansûb", built_ar="الْكَسْرِ", built_en="kasra", built_tr="kesre"),
  BADAL("الْمَقَالَةَ", "maqala", "nasb", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "Then he said: Someone other than al-Aṣmaʿī said: This proverb is Bayhas's, who is known as Naʿāma (the Ostrich); he was long in the legs.", "tr": "Sonra dedi ki: Asmaî'den başkası şöyle dedi: Bu atasözü «Neâme» (Devekuşu) diye bilinen Beyhes'indir; bacakları uzundu."},
 "tokens": [THUMMA(), MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=":", note_ar=" — يَعُودُ عَلَى أَبِي عُبَيْدٍ", note_en=" (Abū ʿUbayd)", note_tr=" (Ebû Ubeyd)"),
  QALA("وَقَالَ"), FAIL("غَيْرُ", "ghayr", note_ar=MUDAF[0], note_en=MUDAF[1], note_tr=MUDAF[2]),
  NM("الْأَصْمَعِيِّ", "asmai", (" — عَبْدُ الْمَلِكِ بْنُ قُرَيْبٍ، إِمَامُ اللُّغَةِ الْبَصْرِيُّ", " — ʿAbd al-Malik ibn Qurayb, the Basran master of the language", " — Basralı lugat imamı Abdülmelik b. Kureyb"), punct=":"),
  ISHARA("هٰذَا", "hadha", "رَفْعٍ مُبْتَدَأٌ", "raf' as the mubtada", "mübtedâ — merfû"), BADAL("الْمَثَلُ", "mathal", "raf"),
  tok("لِبَيْهَسٍ", "li", "prep", ["huruf-jarr"], "اللَّامُ حَرْفُ جَرٍّ لِلنِّسْبَةِ، وَبَيْهَسٍ مَجْرُورٌ بِالْكَسْرَةِ — عَلَمٌ مُنْصَرِفٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِمَحْذُوفٍ خَبَرٍ.", "The lam of belonging, a jarr letter; Bayhas, a fully declined name, is in jarr — the phrase hangs on an omitted predicate.", "Aidiyet lâmı (cer harfi); Beyhes (munsarif alem) mecrûr — câr-mecrûr mahzûf habere müteallik.", segments=[seg("لِ", "li", "prep"), seg("بَيْهَسٍ", "bayhas", "propn")]),
  tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ نَعْتٌ لِـ«بَيْهَسٍ».", "A relative built on sukun, in the seat of jarr as an adjective of «Bayhas».", "İsm-i mevsûl, sükûn üzere mebnî, «Beyhes»in na'tı olarak mahallen mecrûr."),
  tok("يُعْرَفُ", "arafa", "verb", ["naib-al-fail", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.", "Present verb in the passive, in raf'; its deputy doer the hidden «he» — the clause is the ṣila.", "Meçhul muzâri, merfû; nâib-i fâil gizli «o» — cümle sıla."),
  tok("بِنَعَامَةَ", "bi", "prep", ["huruf-jarr", "mamnu-min-sarf"], "الْبَاءُ حَرْفُ جَرٍّ، وَنَعَامَةَ مَجْرُورٌ بِالْفَتْحَةِ نِيَابَةً عَنِ الْكَسْرَةِ — لَقَبٌ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّأْنِيثِ اللَّفْظِيِّ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«يُعْرَفُ».", "The ba is a jarr letter; Naʿāma is in jarr by a fatha standing in for the kasra — a byname with the feminine ending, barred from tanwin; the phrase hangs on «is known».", "Bâ cer harfi; Neâme kesre yerine fetha ile mecrûr — lafzî müennes lakap, gayr-i munsarif; câr-mecrûr «bilinir»e müteallik.", punct="،", segments=[seg("بِ", "bi", "prep"), seg("نَعَامَةَ", "naama-laqab", "propn")]),
  ISTI(KANA("وَكَانَ")), KHK("طَوِيلَ", "tawil-long", note_ar=MUDAF[0] + " — مِنْ إِضَافَةِ الصِّفَةِ الْمُشَبَّهَةِ إِلَى فَاعِلِهَا فِي الْمَعْنَى", note_en=MUDAF[1] + " — the adjective annexed to what it describes", note_tr=MUDAF[2] + " — sıfat-ı müşebbehenin mânâca fâiline izâfeti"),
  MUDAF_ILAYH("الرِّجْلَيْنِ", "rijl", extra=["al-muthanna"], sign="بِالْيَاءِ لِأَنَّهُ مُثَنًّى", note_en=" — by the ya, a dual", note_tr=" — tesniye olduğu için yâ ile", punct=".")]})
S1.append({"id": "s7", "translation": {"en": "His wife saw him by night and said: «An ostrich, by God!»", "tr": "Karısı onu gece gördü ve: «Vallahi bir devekuşu!» dedi."},
 "tokens": [tok("فَرَأَتْهُ", "raa", "verb", ["al-bariz-al-muttasil", "maful-bihi", "mahmuz-verbs", "naqis-verbs"], "الْفَاءُ عَاطِفَةٌ، وَرَأَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ.",
      "The fa conjoins; «saw» is a past verb built on a fatha estimated on the alif, dropped before the ta of the feminine; «him» is its object; its doer follows.", "«bunun üzerine» + re'â, iki sâkin yüzünden düşen elif üzerinde takdîrî fetha ile mebnî mâzî; tâ te'nîs; zamir mef'ûlün bih; fâili sonra gelir.", segments=[seg("فَ", "fa", "conj"), seg("رَأَتْ", "raa", "verb"), seg("هُ", "pron-3ms", "pron")]),
  ENC_NOUN("امْرَأَتُهُ", "imraa", "هُ", "fail"),
  BI_NOUN("بِلَيْلٍ", "layl", "لَيْلٍ", note_ar=" — وَالْبَاءُ بِمَعْنَى «فِي»، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِـ«رَأَتْهُ»", note_en=" — the ba means «in»; the phrase hangs on «saw him»", note_tr=" — bâ «fî» anlamında; câr-mecrûr «gördü»ye müteallik"),
  QALAT("فَقَالَتْ", punct=":"),
  tok("نَعَامَةٌ", "naama", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"], "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ: هٰذِهِ نَعَامَةٌ، مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.", "The predicate of an omitted mubtada («this is an ostrich»), in raf' — the sentence is what is said.", "Mahzûf mübtedânın haberi («bu bir devekuşu»), merfû — cümle mekūlü'l-kavl."),
  tok("وَاللهِ", "allah", "propn", ["huruf-al-qasam-fil-kafiya", "huruf-jarr", "jumla-mutarida"], "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مُقْسَمٌ بِهِ مَجْرُورٌ بِالْكَسْرَةِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقَانِ بِفِعْلِ قَسَمٍ مَحْذُوفٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّوْكِيدِ.", "The waw of the oath, a jarr letter; the Name of Majesty is what is sworn by, in jarr — the phrase hangs on an omitted «I swear»; a parenthetical oath of emphasis.", "Kasem vâvı (cer harfi); lafza-i celâl mukseme bih, mecrûr — mahzûf kasem fiiline müteallik; te'kîd için i'tirâziyye.", punct="!", segments=[seg("وَ", "wa-qasam", "prep"), seg("اللهِ", "allah", "propn")])]})
S1.append({"id": "s8", "translation": {"en": "And he said: «She knew me — may God lengthen her days!»", "tr": "O da dedi ki: «Beni tanıdı — Allah ömrünü uzatsın!»"},
 "tokens": [ISTI(QALA("فَقَالَ", hidden=True, punct=":")), ARAFATNI(MAQUL, punct="،"), *NASAAHA(punct=".")]})

NEW_GLOSS = {
 "nasaa": NV("نَسَأَ", "ن س أ", "I", "to put off, to postpone — نَسَأَهُ اللهُ (or نَسَأَ اللهُ فِي أَجَلِهِ): may God lengthen his days", "geciktirmek, ertelemek — نَسَأَهُ اللهُ: Allah ömrünü uzatsın"),
 "atala": NV("أَطَالَ", "ط و ل", "IV", "to lengthen, to make long (Form IV, hollow)", "uzatmak (if'âl bâbı, ecvef)"),
 "hamhama": NV("حَمْحَمَ", "ح م ح م", "QI", "(of a horse) to whinny, to neigh softly for fodder or for its master (quadriliteral)", "(at) kişnemek, yem veya sahibi için hafifçe kişnemek (rubâî)"),
 "bayhas": NP("بَيْهَس", "Bayhas — a man of Fazāra known as «Naʿāma», of whom many sayings are told; fully declined", "Beyhes — Fezâre'den, «Neâme» lakabıyla bilinen, pek çok sözü nakledilen adam; munsarif"),
 "naama-laqab": NP("نَعَامَة", "Naʿāma (the Ostrich) — the byname of Bayhas, for his long legs; a diptote as a name", "Neâme (Devekuşu) — Beyhes'in uzun bacakları yüzünden lakabı; alem olarak gayr-i munsarif"),
}
V = {"nasaa": SG.sound1("fataha", "نَسَأ", "نْسَأ", "اِنْسَأ", "نَسْء", "نَاسِئ", "مَنْسُوء", "نُسِئَ", "يُنْسَأُ", "مَهْمُوزُ اللَّامِ: نَسَأَ يَنْسَأُ — أَخَّرَ.", cls="مَهْمُوزُ اللَّامِ"),
     "atala": SG.derived_hollow(SG.B4 + " — أَجْوَفُ وَاوِيٌّ", SG.W4, "ُ", "أَطَال", "أَطَل", "طِيل", "طِل", "أَطِيل", "أَطِل", "إِطَالَة", "مُطِيل", "مُطَال", "أُطِيلَ", "يُطَالُ"),
     "hamhama": SG.derived("الرُّبَاعِيُّ الْمُجَرَّدُ: فَعْلَلَ يُفَعْلِلُ", "فَعْلَلَ", "ُ", "حَمْحَم", "حَمْحِم", "حَمْحِم", "حَمْحَمَة", "مُحَمْحِم", None, None, None, "رُبَاعِيٌّ مُجَرَّدٌ لَازِمٌ: حَمْحَمَ يُحَمْحِمُ حَمْحَمَةً.")}
FOR_HOCA = [
 ("«قَالَ: وَكَانَ أَصْلُهُ»: the speaker read as al-Aṣmaʿī (named in «وقال غير الأصمعي»)", "«قَالَ: وَكَانَ أَصْلُهُ»: konuşan Asmaî okundu («وقال غير الأصمعي»den)"),
 ("«بِنَعَامَةَ» as a diptote byname; «نَعَامَةٌ وَاللهِ» the common noun, the predicate of an omitted «هٰذِهِ»", "«بِنَعَامَةَ» gayr-i munsarif lakap; «نَعَامَةٌ وَاللهِ» cins isim, mahzûf «هٰذِهِ»nin haberi"),
 ("«بِلَيْلٍ»: the print's «امرأته: بليل» read without its colon", "«بِلَيْلٍ»: baskıdaki «امرأته: بليل» iki noktasız okundu"),
]
MANIFEST = manifest(SLUG, level=4, title=TITLES[0],
    subtitle={"ar": "الْفَرَسُ الَّتِي عَرَفَتْ صَاحِبَهَا، وَبَيْهَسٌ نَعَامَةُ — مِنْ «فَصْلِ الْمَقَالِ» لِلْبَكْرِيِّ، نَصٌّ مَنْقُولٌ بِلَفْظِهِ",
              "en": "The mare that knew her master, and Bayhas «the Ostrich» — from al-Bakrī's Faṣl al-maqāl, the received text, word for word",
              "tr": "Sahibini tanıyan kısrak ve «Devekuşu» Beyhes — Bekrî'nin Faslü'l-makāl'inden, lafzıyla"},
    pages="p. 90 (printed 1:78), bāb 1", pages_ar="ص ٩٠ (الْمَطْبُوعُ ١: ٧٨)، الْبَابُ الْأَوَّلُ",
    span_en="Abū ʿUbayd's entry whole: the proverb, his gloss, and the two origins he reports, to «فقال: عرفتني، نسأها الله» (al-Bakrī's commentary after it is not taken)",
    span_tr="Ebû Ubeyd'in maddesi tamamen: atasözü, açıklaması ve naklettiği iki menşe, «فقال: عرفتني، نسأها الله»ya kadar (ardındaki Bekrî şerhi alınmadı)",
    span_ar="مَادَّةُ أَبِي عُبَيْدٍ كُلُّهَا: الْمَثَلُ وَتَفْسِيرُهُ وَأَصْلَاهُ إِلَى «فَقَالَ: عَرَفَتْنِي، نَسَأَهَا اللهُ»",
    extra_en="Orthography only: «ايدي» is written «أَيْدِي». ", extra_tr="Yalnız imlâ: «ايدي», «أَيْدِي» yazıldı. ", extra_ar="وَكُتِبَتْ «ايدي» «أَيْدِي». ",
    hoca=FOR_HOCA)
finish(SLUG, TITLES, [S1], NEW_GLOSS, MANIFEST, V_NEW=V)
