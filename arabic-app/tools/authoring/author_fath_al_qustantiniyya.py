"""Author content/samples/fath-al-qustantiniyya — «فَتْحُ الْقُسْطَنْطِينِيَّةِ», an ORIGINAL historical story at Level 5.

ORIGINAL graded Arabic: the conquest of Constantinople in 1453 (857 AH) by the young Ottoman Sultan Meḥmed II, after it
the Conqueror (الْفَاتِحُ) — the fortress on the Bosphorus (Rumeli Hisarı), the great cannons against the land walls, the
chain across the Golden Horn, the ships hauled overland on greased planks in one night, the siege of fifty-three days, the
entry on Tuesday (29 May) 1453, the safety granted to the people and the city made the capital. Only the well-attested core
of the event is told; disputed numbers and anecdotes are left out, and no āya or ḥadīth is quoted or paraphrased. No
sentence is a quotation from any source. Five chapters, twenty-nine sentences, in a Level-5 register: maf'ūl muṭlaq,
maf'ūl lahu, ḥāl and wāw al-ḥāl, tamyīz with numbers, لَمَّا، حَتَّى + subjunctive, the passive, relative and ṣifa clauses
with a resumptive pronoun, the istithnāʾ mufarragh, diptotes in every seat. Written on the authoring kit (story_kit.py);
glosses and paradigms are copied by lemma identity from the shelf, and the new entries are listed in NEW_GLOSS / NEW_VERBS
(two new verbs: حَاصَرَ, Form III, and هَجَمَ, Form I of bāb naṣara).  Regenerate with:
python3 tools/authoring/author_fath_al_qustantiniyya.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "fath-al-qustantiniyya"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

PRON.update({"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp"})
PRON_AR.update({"هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "هَا": "هَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُمُ": "هُمْ"})

# ---- the house notes this story leans on ------------------------------------------------------------------------
MUD = ("، مُضَافٌ", ", annexed", ", muzâf")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
KH_KANA_J = ("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the jarr phrase is the predicate of كَانَ, in the seat of nasb", "; câr-mecrûr kâne'nin haberi, mahallen mansûb")
SALIM_W = "بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ"
SALIM_W_EN, SALIM_W_TR = " — by the waw, a sound masculine plural", " — cem-i müzekker sâlim olduğu için vâv ile"
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
DHALIKA_TAIL = ("، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ", "; its lam marks distance and its kaf addresses the listener", "; lâm uzaklık, kâf hitap içindir")

def KANAT(punct=None):
    """كَانَتِ at the head of the story: the ta of the feminine voweled with kasra before the article"""
    return tok("كَانَتِ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَحُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
        "كَانَ is the defective past verb: it raises its noun and puts its predicate in nasb; the ta marks the feminine and is voweled with kasra before the following ال.",
        "«idi» — nâkıs mâzî fiil kâne: ismini ref, haberini nasb eder; tâ te'nîs içindir, iki sâkin karşılaştığı için kesre ile harekelendi.", punct=punct)
def KANAT_HID(full="وَكَانَتْ"):
    """وَكَانَتْ whose noun is the hidden «she»"""
    return tok(full, "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
        WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْمَدِينَةِ.",
        "The waw conjoins; كَانَ is the defective past verb, the ta marks the feminine, and its noun is the hidden pronoun «she» — the city.",
        "«ve» + nâkıs mâzî fiil kâne; tâ te'nîs içindir, ismi şehre dönen gizli zamir «o».",
        segments=[seg("وَ", "wa", "conj"), seg("كَانَتْ", "kana", "verb")])
def DHALIKA_SEAT(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "ذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + DHALIKA_TAIL[0] + ".",
        "A demonstrative, built on sukun, in the seat of " + seat_en + DHALIKA_TAIL[1] + ".",
        "İşaret ismi, sükûn üzere mebnî, mahallen " + seat_tr + DHALIKA_TAIL[2] + ".", punct=punct)
def MUTLAQ_NAW(full, lex, punct=None):
    """ضَرْبًا شَدِيدًا: the verb's own masdar, described — so it states the KIND of the act"""
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ الْفِعْلِ قَبْلَهُ، مُبَيِّنٌ لِلنَّوْعِ لِأَنَّهُ مَوْصُوفٌ.",
        "The absolute object (maf'ul mutlaq), in nasb — the verb's own masdar; because it carries an adjective it states the KIND of the act.",
        "Mef'ûlün mutlak, mansûb — fiilin kendi masdarı; sıfatlandığı için fiilin nev'ini beyan eder.", punct=punct)
def UTHMANIYYUN_F(punct=None):
    return FAIL("الْعُثْمَانِيُّونَ", "uthmani", extra=["jam-mudhakkar-salim", "ism-mansub"], sign=SALIM_W, note_en=SALIM_W_EN, note_tr=SALIM_W_TR, punct=punct)
def QARN_J(full="الْقَرْنِ", mi=False, punct=None):
    return MUDAF_ILAYH(full, "qarn", punct=punct) if mi else MAJR(full, "qarn", punct=punct)
DHAHABI_J = lambda punct=None: NAAT("الذَّهَبِيِّ", "dhahabi", "jarr", ["ism-mansub"], note_ar=" — اسْمٌ مَنْسُوبٌ إِلَى الذَّهَبِ", note_en=" — a nisba adjective, «golden»", note_tr=" — zehebe nisbet edilmiş isim, «altın»", punct=punct)

# ---- Chapter 1 — أَمَلٌ قَدِيمٌ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Constantinople was the capital of the Byzantines, and it was a well-fortified city which the sea surrounded on three sides.",
                                       "tr": "Kostantiniyye Rumların başşehriydi; denizin üç yönden kuşattığı müstahkem bir şehirdi."},
 "tokens": [KANAT(),
  ISMK("الْقُسْطَنْطِينِيَّةُ", "qustantiniyya", "propn"),
  KHK("عَاصِمَةَ", "asima", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  MUDAF_ILAYH("الرُّومِ", "rum", "propn", punct="،"),
  KANAT_HID(),
  KHK("مَدِينَةً", "madina"),
  NAAT("حَصِينَةً", "hasin", "nasb", ["sifa-mushabbaha"]),
  tok("يُحِيطُ", "ahata", "verb", ["mudari-marfu", "form-iv-verbs", "hollow-verbs", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِمَدِينَةٍ.",
      "Present verb in raf'; its doer follows — the clause is a second na't of «a city», in the seat of nasb.",
      "Merfû muzâri; fâili sonra gelir — cümle «şehir»in ikinci na'tı olarak mahallen mansûb."),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onu»)", extra=["jumla-sifa"], note_ar=" — وَهَا الْعَائِدُ الَّذِي يَرْبِطُ جُمْلَةَ النَّعْتِ بِمَدِينَةٍ", note_en="; «it» is the returning pronoun that ties the na't clause to «a city»", note_tr="; «hâ», na't cümlesini «şehir»e bağlayan âid zamirdir"),
  FAIL("الْبَحْرُ", "bahr"),
  MIN(),
  tok("ثَلَاثِ", "thalath", "noun", ["huruf-jarr", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
      "مَجْرُورٌ بِمِنْ وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ — وَحُذِفَتْ مِنْهُ التَّاءُ لِأَنَّ مَعْدُودَهُ «جِهَة» مُؤَنَّثٌ: الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُخَالِفُ مَعْدُودَهُ.",
      "In jarr after مِنْ and annexed — it drops the ta because its counted noun «side» is feminine: the numbers three to ten take the opposite gender of what they count.",
      "Min ile mecrûr, muzâf — ma'dûdu «cihet» müennes olduğu için tâsız gelmiştir: üçten ona kadar sayılar ma'dûduna cinsçe zıt olur."),
  tok("جِهَاتٍ", "jiha", "noun", ["idafa-definiteness", "jam-muannath-salim", "asma-al-adad-fil-kafiya"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ، وَهُوَ تَمْيِيزُ الْعَدَدِ: جَمْعٌ مَجْرُورٌ بِالْإِضَافَةِ.",
      "The second term of the idafa, in jarr — a sound feminine plural, the specifier of the number: a plural in jarr by the annexation.",
      "Muzâfun ileyh, mecrûr — cem-i müennes sâlim; sayının temyîzi: izâfetle mecrûr cemi.", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "Its high walls protected it on the side of the land.", "tr": "Kara tarafından onu yüksek surları koruyordu."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  ENC_NOUN("أَسْوَارُهَا", "sur-wall", "هَا", "ismk", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِسُورٍ", note_en=" — the broken plural of «wall»", note_tr=" — sûrun cem-i teksîri"),
  NAAT("الْعَالِيَةُ", "alin-high", "raf", ["ism-fail"]),
  MUDARI("تَحْمِيهَا", "hama-protect", who="هِيَ", enc="هَا", naqis="ي", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  MIN(),
  MAJR("جِهَةِ", "jiha", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  MUDAF_ILAYH("الْبَرِّ", "barr-land", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "The Muslims had hoped to conquer it for a long time.", "tr": "Müslümanlar uzun zamandan beri onu fethetmeyi umuyorlardı."},
 "tokens": [KANA("وَكَانَ"),
  ISMK("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign=SALIM_W, note_en=SALIM_W_EN, note_tr=SALIM_W_TR),
  MUDARI5_KH("يَرْجُونَ", "raja", ["naqis-verbs"], note_ar=" (أَصْلُهُ يَرْجُوُونَ: حُذِفَتْ لَامُ الْفِعْلِ لِالْتِقَاءِ السَّاكِنَيْنِ)", note_en=" (from يَرْجُوُونَ: the verb's last radical dropped where two quiescents met)", note_tr=" (aslı yercuvûne: iki sâkin karşılaşınca lâmü'l-fiil düştü)"),
  ENC_NOUN("فَتْحَهَا", "fath", "هَا", "maful", extra=["masdar"], note_ar=" — مَصْدَرٌ مُضَافٌ إِلَى مَفْعُولِهِ", note_en=" — a masdar annexed to its own object («to conquer IT»)", note_tr=" — mef'ûlüne muzâf masdar («onu fethetmek»)"),
  PREP("مُنْذُ", "mundhu", gloss_tr="«-den beri»"),
  MAJR("زَمَنٍ", "zaman-period"),
  NAAT("بَعِيدٍ", "baid", "jarr", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "Their armies had besieged it before, but they could not take it.", "tr": "Orduları daha önce onu kuşatmış, fakat fethetmeye güç yetirememişlerdi."},
 "tokens": [tok("وَقَدْ", "qad", "part", ["qad-harf"], WA_AR + "قَدْ حَرْفُ تَحْقِيقٍ.", "The waw conjoins; قَدْ affirms the past verb after it.", "«ve» + kad: tahkîk harfi.",
      segments=[seg("وَ", "wa", "conj"), seg("قَدْ", "qad", "part")]),
  ENC_MADI("حَاصَرَتْهَا", "hasara", "هَا", ["form-iii-verbs"], fem=True),
  ENC_NOUN("جُيُوشُهُمْ", "jaysh", "هُمْ", "fail", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ، فَجَازَ تَأْنِيثُ فِعْلِهِ", note_en=" — a broken plural, so its verb may take the feminine", note_tr=" — cem-i teksîr; bu yüzden fiilinin müennes gelmesi caizdir"),
  MIN(),
  tok("قَبْلُ", "qablu", "noun", ["maful-fih", "al-ghayat-wa-baqiyyat-al-zuruf-al-mabniyya", "huruf-jarr"],
      "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ بِمِنْ — قُطِعَ عَنِ الْإِضَافَةِ لَفْظًا وَنُوِيَ مَعْنَاهَا (أَيْ: مِنْ قَبْلِ ذٰلِكَ).",
      "An adverb of time built on damma, in the seat of jarr after مِنْ — cut off from its annexation in wording while its sense is kept («before that»).",
      "Zaman zarfı, damme üzere mebnî, min ile mahallen mecrûr — lafzen izâfetten kesilmiş, mânâsı niyet edilmiştir («ondan önce»).", punct="،"),
  tok("فَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], FA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "The fa conjoins; لَمْ negates, governs jazm and turns the present to the past.", "«bunun üzerine» + lem: nefiy, cezm ve kalb harfi.",
      segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  JAZM_V("تَقْدِرْ", "qadara-able", hidden="هِيَ", note_ar=" يَعُودُ عَلَى الْجُيُوشِ", note_en=" — the armies", note_tr=" — ordular"),
  ALA(),
  ENC_NOUN("فَتْحِهَا", "fath", "هَا", "majr", extra=["masdar"], punct=".")]})
S1.append({"id": "s5", "translation": {"en": "When Mehmed II became sultan while still a young man, he resolved most firmly to conquer it.",
                                       "tr": "II. Mehmed henüz genç iken sultan olunca, onu fethetmeye sağlam bir azimle karar verdi."},
 "tokens": [LAMMA2("فَلَمَّا"),
  tok("صَارَ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
      "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + LAMMA_CL[0] + ".",
      "صَارَ «became» is one of كَانَ's sisters: it raises its noun and puts its predicate in nasb" + LAMMA_CL[1] + ".",
      "«oldu» — kâne'nin kardeşlerinden nâkıs fiil; ismini ref, haberini nasb eder" + LAMMA_CL[2] + "."),
  tok("مُحَمَّدٌ", "muhammad", "propn", ["kana-wa-akhawatuha"], "اسْمُ صَارَ مَرْفُوعٌ بِالضَّمَّةِ.", "The noun of صَارَ, in raf'.", "Sâra'nın ismi, merfû."),
  tok("الثَّانِي", "thani", "noun", ["naat-sifa", "ism-maqsur-manqus"],
      "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.",
      "An adjective agreeing with the name, in raf' by a damma estimated on the ya (too heavy to pronounce) — a manqūṣ noun.",
      "Na't, merfû; damme ağırlık sebebiyle yâ üzerinde takdîrîdir — menkûs isim."),
  tok("سُلْطَانًا", "sultan", "noun", ["kana-wa-akhawatuha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of صَارَ, in nasb.", "Sâra'nın haberi, mansûb."),
  WA_HUWA_HAL(),
  KHABAR("شَابٌّ", "shabb", punct="،"),
  MADI("عَزَمَ", "azama", hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  ALA(),
  ENC_NOUN("فَتْحِهَا", "fath", "هَا", "majr", extra=["masdar"]),
  MUTLAQ_NAW("عَزْمًا", "azm-resolve"),
  NAAT("شَدِيدًا", "shadid", "nasb", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "So he prepared for it a mighty army and many ships.", "tr": "Bunun için büyük bir ordu ve birçok gemi hazırladı."},
 "tokens": [MADI("فَأَعَدَّ", "aadda", ["form-iv-verbs", "doubled-verbs"], hidden=True),
  tok("لِذٰلِكَ", "li", "prep", ["huruf-jarr", "asma-al-ishara"],
      "اللَّامُ حَرْفُ جَرٍّ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ" + DHALIKA_TAIL[0] + ".",
      "The lam is a jarr letter; the demonstrative after it is built on sukun in the seat of jarr" + DHALIKA_TAIL[1] + ".",
      "Lâm cer harfi; işaret ismi sükûn üzere mebnî, mahallen mecrûr" + DHALIKA_TAIL[2] + ".",
      segments=[seg("لِ", "li", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  MAFUL("جَيْشًا", "jaysh"),
  NAAT("عَظِيمًا", "azim", "nasb"),
  ATF("وَسُفُنًا", "safina", case="nasb", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِسَفِينَةٍ", note_en=" — the broken plural of «ship»", note_tr=" — sefînenin cem-i teksîri"),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct=".")]})

# ---- Chapter 2 — قَلْعَةُ رُومَلِي ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "The Sultan wanted to hold the Bosphorus strait, so that no ship would pass through it except by his leave.",
                                       "tr": "Sultan Boğaz'a hâkim olmak istedi; öyle ki onun izni olmadan oradan hiçbir gemi geçmesin."},
 "tokens": [MADI("وَأَرَادَ", "arada", ["hollow-verbs", "form-iv-verbs"]),
  FAIL("السُّلْطَانُ", "sultan"),
  AN_MAFUL(),
  MANSUB_AN("يَمْلِكَ", "malaka"),
  MAFUL("مَضِيقَ", "madiq", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  MUDAF_ILAYH("الْبُوسْفُورِ", "busfur", "propn", note_ar=" — اسْمٌ أَعْجَمِيٌّ دَخَلَتْهُ أَلْ فَجُرَّ بِالْكَسْرَةِ", note_en=" — a foreign name that carries the article, so it takes the kasra", note_tr=" — başına el- gelmiş yabancı isim; bu yüzden kesre ile mecrûr", punct="،"),
  tok("فَلَا", "la-nafiya", "part", ["la-nafiya"], FA_AR + "لَا نَافِيَةٌ لَا عَمَلَ لَهَا.", "The fa conjoins; لَا negates and governs nothing.", "«bunun üzerine» + nefiy lâ'sı; amel etmez.",
      segments=[seg("فَ", "fa", "conj"), seg("لَا", "la-nafiya", "part")]),
  tok("تَمُرَّ", "marra", "verb", ["nawasib-wa-jawazim-al-mudari", "atf-nasaq", "doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَعْطُوفٌ عَلَى «يَمْلِكَ» مَنْصُوبٌ مِثْلَهُ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ بَعْدَهُ.",
      "Present verb conjoined to «hold» and in nasb like it, its sign the fatha; its doer follows.",
      "«Hâkim olmak» fiiline ma'tûf muzâri; onun gibi mansûb, alâmeti fetha; fâili sonra gelir."),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («orada»)"),
  FAIL("سَفِينَةٌ", "safina"),
  ILLA(),
  BI_NOUN("بِإِذْنِهِ", "idhn", "إِذْنِهِ", enc="هِ", extra=["hal", "istithna-mufarragh"], note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنْ سَفِينَةٍ", note_en=" — the jarr phrase hangs on an omitted hal: «[passing only] with his leave»", note_tr=" — câr-mecrûr mahzûf bir hâle müteallık: «onun izniyle olarak»", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "So he built a mighty fortress at its narrowest point.", "tr": "Bunun üzerine Boğaz'ın en dar yerine büyük bir kale yaptı."},
 "tokens": [MADI_ALIF("فَبَنَى", "bana", hidden=True),
  MAFUL("قَلْعَةً", "qala-fortress"),
  NAAT("عَظِيمَةً", "azim", "nasb"),
  FI(),
  tok("أَضْيَقِ", "adyaq", "noun", ["huruf-jarr", "ism-tafdil", "mamnu-min-sarf", "idafa-definiteness"],
      "مَجْرُورٌ بِفِي وَعَلَامَةُ جَرِّهِ الْكَسْرَةُ، مُضَافٌ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ، فَلَمَّا أُضِيفَ جُرَّ بِالْكَسْرَةِ.",
      "In jarr after فِي and annexed — an elative, barred from tanwin as an adjective on the verb's pattern; annexed, it takes the plain kasra.",
      "Fî ile mecrûr, muzâf — vasfiyet ve fiil vezni sebebiyle gayr-i munsarif ism-i tafdîl; muzâf olunca kesre ile mecrûr olur."),
  MUDAF_ILAYH("مَوْضِعٍ", "mawdi", note_ar=" — وَهُوَ نَكِرَةٌ، فَاسْمُ التَّفْضِيلِ الْمُضَافُ إِلَيْهَا يَبْقَى مُفْرَدًا مُذَكَّرًا", note_en=" — indefinite, so the elative annexed to it stays singular and masculine", note_tr=" — nekre; ona muzâf ism-i tafdîl müfred ve müzekker kalır"),
  MINHU(punct=".")]})
S2.append({"id": "s3", "translation": {"en": "Its building was finished within a few months, the workers labouring on it night and day.",
                                       "tr": "İşçiler gece gündüz onun üzerinde çalışırken inşası birkaç ayda tamamlandı."},
 "tokens": [MADI("وَتَمَّ", "tamma", ["doubled-verbs"]),
  ENC_NOUN("بِنَاؤُهَا", "bina", "هَا", "fail", extra=["masdar"]),
  FI(),
  MAJR("أَشْهُرٍ", "shahr", extra=["jam-taksir"], note_ar=" — جَمْعُ قِلَّةٍ لِشَهْرٍ", note_en=" — a plural of paucity of «month»", note_tr=" — şehrin cem-i kıllesi"),
  NAAT("قَلِيلَةٍ", "qalil", "jarr", punct="،"),
  tok("وَالْعُمَّالُ", "amil-worker", "noun", ["mubtada-khabar", "al-hal-jumla-wa-rabituha", "jam-taksir"],
      "الْوَاوُ حَالِيَّةٌ، وَالْعُمَّالُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw of the hal; «the workers» is the mubtada, in raf' — the nominal clause fills the seat of nasb as a hal.",
      "Hâl vâvı; «işçiler» mübtedâ, merfû — isim cümlesi hâl olarak mahallen mansûb.",
      segments=[seg("وَ", "wa", "conj"), seg("الْعُمَّالُ", "amil-worker", "noun")]),
  MUDARI5("يَعْمَلُونَ", "amila", role_ar=KH_CL[0], role_en=KH_CL[1], role_tr=KH_CL[2]),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («onda»)"),
  ZARF("لَيْلًا", "layl", mudaf=False, **ZAMAN),
  ATF("وَنَهَارًا", "nahar", case="nasb", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "Facing it stood another fortress, which one of his forefathers had built.", "tr": "Karşısında, atalarından birinin yaptırdığı başka bir kale vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  tok("أَمَامَهَا", "amama", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "kana-wa-akhawatuha"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.",
      "An adverb of place «in front of», in nasb and annexed to «it» (the seat of jarr) — the phrase is the FRONTED predicate of كَانَ, in the seat of nasb.",
      "Mekân zarfı «önünde», mansûb, «o» zamirine muzâf — şibh-i cümle, kâne'nin öne alınmış haberi, mahallen mansûb.",
      segments=[seg("أَمَامَ", "amama", "noun"), seg("هَا", "pron-3fs", "pron")]),
  ISMK("قَلْعَةٌ", "qala-fortress", muakhkhar=True),
  tok("أُخْرَى", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf", "ism-maqsur-manqus"],
      "نَعْتٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مُؤَنَّثُ آخَرَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَقْصُورَةِ.",
      "An adjective in raf' by a damma estimated on the alif — the feminine of آخَر «another», barred from tanwin by its shortened feminine alif.",
      "Na't, elif üzerinde takdîrî damme ile merfû — âharın müennesi; maksûr te'nîs elifi sebebiyle gayr-i munsarif."),
  ENC_MADI("بَنَاهَا", "bana", "هَا", ["naqis-verbs", "jumla-sifa"], alif=True,
      note_ar=" — وَالْفَاعِلُ بَعْدَهُ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِقَلْعَةٍ، وَهَا الْعَائِدُ الرَّابِطُ", note_en="; its doer follows — the clause is a second na't of «a fortress», in the seat of raf', and «it» is the returning pronoun that ties it", note_tr="; fâili sonra gelir — cümle «kale»nin ikinci na'tı, mahallen merfû; «hâ» onu bağlayan âid zamirdir"),
  FAIL("أَحَدُ", "ahad", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  ENC_NOUN("آبَائِهِ", "ab", "هِ", "mudaf", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِأَبٍ", note_en=" — the broken plural of «father»: forefathers", note_tr=" — ebin cem-i teksîri: atalar", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "Thus the Ottomans held the strait from both its sides.", "tr": "Böylece Osmanlılar Boğaz'a iki yakasından hâkim oldular."},
 "tokens": [MADI("فَمَلَكَ", "malaka"),
  UTHMANIYYUN_F(),
  MAFUL("الْمَضِيقَ", "madiq"),
  MIN(),
  tok("جِهَتَيْهِ", "jiha", "noun", ["huruf-jarr", "al-muthanna", "idafa-definiteness", "al-bariz-al-muttasil"],
      "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "In jarr by the ya, being a dual; its nun drops for the annexation, and the attached «its» is the second term, in the seat of jarr.",
      "Tesniye olduğu için yâ ile mecrûr; izâfet sebebiyle nûnu düştü; muzâf, bitişik zamir muzâfun ileyh — mahallen mecrûr.", punct=".",
      segments=[seg("جِهَتَيْ", "jiha", "noun"), seg("هِ", "pron-3ms", "pron")])]})

# ---- Chapter 3 — الْمَدَافِعُ وَالسِّلْسِلَةُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "Then the Sultan marched with his army to the city and besieged it by land and sea.", "tr": "Sonra Sultan ordusuyla şehre yürüdü ve onu karadan ve denizden kuşattı."},
 "tokens": [THUMMA(),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"]),
  FAIL("السُّلْطَانُ", "sultan"),
  BI_NOUN("بِجَيْشِهِ", "jaysh", "جَيْشِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of accompaniment, «with»", note_tr=" — bâ musâhabet içindir, «ile»"),
  ILA(),
  MAJR("الْمَدِينَةِ", "madina", punct="،"),
  ENC_MADI("فَحَاصَرَهَا", "hasara", "هَا", ["form-iii-verbs"], hidden=True),
  MINA(),
  MAJR("الْبَرِّ", "barr-land"),
  ATF("وَالْبَحْرِ", "bahr", case="jarr", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "He had with him huge cannons whose like people had never seen.", "tr": "Yanında, insanların benzerini görmediği büyük toplar vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  tok("مَعَهُ", "maa", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "kana-wa-akhawatuha"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.",
      "An adverb «with», in nasb and annexed to «him» (the seat of jarr) — the phrase is the FRONTED predicate of كَانَ, in the seat of nasb.",
      "«Yanında, beraber» — zarf, mansûb, «o» zamirine muzâf — şibh-i cümle, kâne'nin öne alınmış haberi, mahallen mansûb.",
      segments=[seg("مَعَ", "maa", "noun"), seg("هُ", "pron-3ms", "pron")]),
  ISMK("مَدَافِعُ", "midfa", extra=["mamnu-min-sarf", "jam-taksir"], muakhkhar=True,
       note_ar=" بِلَا تَنْوِينٍ — جَمْعُ مِدْفَعٍ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَنَّهُ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ (مَفَاعِل)", note_en=" without tanwin — the plural of «cannon», a diptote on the furthest-plural pattern مَفَاعِل", note_tr=" tenvinsiz — midfa'ın cemi; müntehe'l-cumû' sîgasında (mefâil) olduğu için gayr-i munsarif"),
  NAAT("عَظِيمَةٌ", "azim", "raf", note_ar=" — جَمْعُ مَا لَا يَعْقِلُ يُوصَفُ بِالْمُفْرَدِ الْمُؤَنَّثِ", note_en=" — a plural of things is described by a feminine singular", note_tr=" — akılsız varlıkların cemi müfred müennesle vasıflanır"),
  LAM_JAZM(),
  tok("يَرَ", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "naqis-verbs", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (يَرَى ← لَمْ يَرَ)، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِمَدَافِعَ.",
      "Present verb in jazm after لَمْ, its sign the dropped weak letter (يَرَى → لَمْ يَرَ); its doer follows — the clause is a second na't of «cannons», in the seat of raf'.",
      "Lem ile meczûm muzâri; alâmeti illet harfinin hazfi (yerâ → lem yera); fâili sonra gelir — cümle «toplar»ın ikinci na'tı, mahallen merfû."),
  FAIL("النَّاسُ", "nas"),
  ENC_NOUN("مِثْلَهَا", "mithl", "هَا", "maful", extra=["jumla-sifa"], note_ar=" — وَهَا الْعَائِدُ الَّذِي يَرْبِطُ جُمْلَةَ النَّعْتِ بِمَدَافِعَ", note_en="; «their» is the returning pronoun that ties the na't clause to «cannons»", note_tr="; «hâ» na't cümlesini «toplar»a bağlayan âid zamirdir", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "The cannons pounded the walls fiercely for many days.", "tr": "Toplar surları günlerce şiddetle dövdü."},
 "tokens": [MADI("فَضَرَبَتِ", "daraba", fem=True, kasra=True),
  FAIL("الْمَدَافِعُ", "midfa", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِغَيْرِ الْعَاقِلِ، فَأُنِّثَ فِعْلُهُ", note_en=" — a broken plural of things, so its verb is feminine", note_tr=" — akılsız varlıkların cem-i teksîri; bu yüzden fiili müennes geldi"),
  MAFUL("الْأَسْوَارَ", "sur-wall", extra=["jam-taksir"]),
  MUTLAQ_NAW("ضَرْبًا", "darb"),
  NAAT("شَدِيدًا", "shadid", "nasb"),
  ZARF("أَيَّامًا", "yawm", mudaf=False, extra=["jam-taksir"], **ZAMAN),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "And by night the Byzantines would repair what the cannons had demolished by day.", "tr": "Rumlar da topların gündüz yıktığını gece onarırlardı."},
 "tokens": [KANA("وَكَانَ"),
  ISMK("الرُّومُ", "rum", "propn"),
  MUDARI5_KH("يُصْلِحُونَ", "aslaha", ["form-iv-verbs"]),
  BI_NOUN("بِاللَّيْلِ", "layl", "اللَّيْلِ", note_ar=" — وَالْبَاءُ بِمَعْنَى فِي (لِلظَّرْفِيَّةِ)", note_en=" — the ba here means «in» (of time)", note_tr=" — bâ burada «-de» anlamındadır (zarfiyet)"),
  MAWSUL_MAF("مَا", "ma-mawsula", built="السُّكُونِ", built_en="sukun", built_tr="sükûn"),
  ENC_MADI("هَدَمَتْهُ", "hadama", "هُ", fem=True,
      note_ar=" — وَالْفَاعِلُ بَعْدَهُ، وَالْهَاءُ الْعَائِدُ عَلَى مَا" + SILA[0], note_en="; its doer follows, and «it» is the pronoun returning to مَا" + SILA[1], note_tr="; fâili sonra gelir, «hû» mâ'ya dönen âid zamirdir" + SILA[2]),
  FAIL("الْمَدَافِعُ", "midfa", extra=["jam-taksir"]),
  BI_NOUN("بِالنَّهَارِ", "nahar", "النَّهَارِ", note_ar=" — وَالْبَاءُ لِلظَّرْفِيَّةِ", note_en=" — the ba of time, «by day»", note_tr=" — zarfiyet bâ'sı, «gündüz»", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "And the entrance of the Golden Horn was closed with a huge chain of iron.", "tr": "Haliç'in girişi de demirden büyük bir zincirle kapatıldı."},
 "tokens": [MAJHUL("وَأُغْلِقَ", "aghlaqa", ["form-iv-verbs"]),
  NAIB("مَدْخَلُ", "madkhal", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  QARN_J(mi=True),
  NAAT("الذَّهَبِيِّ", "dhahabi", "jarr", ["ism-mansub"], note_ar=" — اسْمٌ مَنْسُوبٌ إِلَى الذَّهَبِ؛ وَالْقَرْنُ الذَّهَبِيُّ: الْخَلِيجُ الَّذِي تَقَعُ عَلَيْهِ الْمَدِينَةُ", note_en=" — a nisba adjective, «golden»; the Golden Horn is the inlet on which the city stands", note_tr=" — zehebe nisbet edilmiş isim, «altın»; el-Karnu'z-zehebî (Haliç) şehrin kıyısındaki körfezdir"),
  BI_NOUN("بِسِلْسِلَةٍ", "silsila", "سِلْسِلَةٍ"),
  NAAT("ضَخْمَةٍ", "dakhm", "jarr", ["sifa-mushabbaha"]),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter naming the material («of iron»), voweled with fatha before the following ال.", "«-den» — cins beyânı için cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("الْحَدِيدِ", "hadid", punct=".")]})
S3.append({"id": "s6", "translation": {"en": "So the Ottoman ships could not enter it.", "tr": "Bu yüzden Osmanlı gemileri oraya giremedi."},
 "tokens": [tok("فَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], FA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "The fa conjoins; لَمْ negates, governs jazm and turns the present to the past.", "«bunun üzerine» + lem: nefiy, cezm ve kalb harfi.",
      segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")]),
  tok("تَسْتَطِعِ", "istataa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim", "form-x-verbs", "hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَحُذِفَتْ يَاؤُهُ (تَسْتَطِيعُ ← لَمْ تَسْتَطِعْ) لِالْتِقَاءِ السَّاكِنَيْنِ؛ وَالْفَاعِلُ بَعْدَهُ.",
      "Present verb in jazm after لَمْ, its sign the sukun — voweled with kasra before the following ال; its long ya dropped where two quiescents met (تَسْتَطِيعُ → لَمْ تَسْتَطِعْ); its doer follows.",
      "Lem ile meczûm muzâri, alâmeti sükûn — iki sâkin karşılaştığı için kesre ile harekelendi; yâ'sı da iki sâkin karşılaşınca düştü (testetîu → lem testetı'); fâili sonra gelir."),
  FAIL("السُّفُنُ", "safina", extra=["jam-taksir"]),
  NAAT("الْعُثْمَانِيَّةُ", "uthmani", "raf", ["ism-mansub"]),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِتَسْتَطِعْ", "; the clause it builds is the object of «could»", "; kurduğu müevvel masdar «güç yetirdi»nin mef'ûlüdür"),
  MANSUB_AN("تَدْخُلَهُ", "dakhala", who="هِيَ", enc="هُ", punct=".")]})

# ---- Chapter 4 — السُّفُنُ عَلَى الْبَرِّ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "When the Sultan saw this, he thought of another way by which to bring his ships in.", "tr": "Sultan bunu görünce, gemilerini içeri sokabileceği başka bir yol düşündü."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI_ALIF("رَأَى", "raa", note_ar="، وَالْفَاعِلُ بَعْدَهُ" + LAMMA_CL[0], note_en="; its doer follows" + LAMMA_CL[1], note_tr="; fâili sonra gelir" + LAMMA_CL[2]),
  FAIL("السُّلْطَانُ", "sultan"),
  DHALIKA_SEAT("نَصْبٍ مَفْعُولٌ بِهِ", "nasb as the object", "mansûb mef'ûlün bih", punct="،", extra=["maful-bihi"]),
  MADI("فَكَّرَ", "fakkara", ["form-ii-verbs"], hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  FI(),
  MAJR("طَرِيقٍ", "tariq"),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"],
      "نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ، لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ.",
      "An adjective in jarr, its sign the fatha standing in for the kasra — آخَر «another» is barred from tanwin as an adjective on the أَفْعَل pattern.",
      "Na't, mecrûr; kesre yerine fetha ile — âhar vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif."),
  MUDARI("يُدْخِلُ", "adkhala", ["form-iv-verbs", "jumla-sifa"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ ثَانٍ لِطَرِيقٍ", note_en=" — the clause is a second na't of «a way», in the seat of jarr", note_tr=" — cümle «yol»un ikinci na'tı, mahallen mecrûr"),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)", extra=["jumla-sifa"], note_ar=" — وَالْهَاءُ الْعَائِدُ عَلَى طَرِيقٍ، تَرْبِطُ جُمْلَةَ النَّعْتِ بِهِ", note_en="; «it» returns to «a way» and ties the na't clause to it", note_tr="; «hî» «yol»a döner ve na't cümlesini ona bağlar"),
  ENC_NOUN("سُفُنَهُ", "safina", "هُ", "maful", extra=["jam-taksir"], punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He gave orders for planks of wood, and they were laid out over the land, and oil and fat were put on them.",
                                       "tr": "Tahtadan kalaslar için emir verdi; kalaslar karaya döşendi ve üzerlerine yağ ve iç yağı sürüldü."},
 "tokens": [MADI("فَأَمَرَ", "amara-command", hidden=True),
  BI_NOUN("بِأَلْوَاحٍ", "lawh-board", "أَلْوَاحٍ", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِلَوْحٍ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِأَمَرَ", note_en=" — the broken plural of «plank»; the phrase hangs on «ordered»", note_tr=" — levhin cem-i teksîri; câr-mecrûr «emretti»ye müteallık"),
  tok("مِنَ", "min", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ لِبَيَانِ الْجِنْسِ، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "A jarr letter naming the material («of wood»), voweled with fatha before the following ال.", "«-den» — cins beyânı için cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi."),
  MAJR("الْخَشَبِ", "khashab"),
  tok("فَمُدَّتْ", "madda", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "doubled-verbs"],
      FA_AR + "مُدَّ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْأَلْوَاحِ — أَصْلُهُ مُدِدَتْ، فَسُكِّنَتِ الدَّالُ الْأُولَى وَأُدْغِمَتْ فِي الثَّانِيَةِ.",
      "The fa conjoins; «were laid» is a past verb in the passive, built on fatha, the ta marking the feminine; its deputy doer is the hidden «they» (the planks) — from مُدِدَتْ, the first dal made quiescent and merged into the second.",
      "«bunun üzerine» + meçhul mâzî, fetha üzere mebnî; tâ te'nîs içindir; nâib-i fâil kalaslara dönen gizli zamir «o» — aslı mudidet: birinci dâl sâkin kılınıp ikinciye idgâm edildi.",
      segments=[seg("فَ", "fa", "conj"), seg("مُدَّتْ", "madda", "verb")]),
  ALA(),
  MAJR("الْبَرِّ", "barr-land", punct="،"),
  MAJHUL("وَوُضِعَ", "wadaa", ["mithal-verbs"]),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («üzerine»)"),
  NAIB("الزَّيْتُ", "zayt"),
  ATF("وَالشَّحْمُ", "shahm", case="raf", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "Then in a single night the soldiers dragged the ships over them, so as to set them down in the Golden Horn behind the chain.",
                                       "tr": "Sonra askerler, onları zincirin gerisinde Haliç'e indirmek için gemileri tek bir gecede kalasların üzerinden çektiler."},
 "tokens": [THUMMA(),
  MADI("جَرَّ", "jarra", ["doubled-verbs"]),
  FAIL("الْجُنُودُ", "jund", extra=["jam-taksir"]),
  MAFUL("السُّفُنَ", "safina", extra=["jam-taksir"]),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («üzerinde»)"),
  FI(),
  MAJR("لَيْلَةٍ", "layla"),
  NAAT("وَاحِدَةٍ", "wahid", "jarr", punct="،"),
  tok("حَتَّى", "hatta", "prep", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari", "ila-hatta-fi-wal-ba-fil-kafiya"],
      "حَرْفُ جَرٍّ بِمَعْنَى «كَيْ» لِلتَّعْلِيلِ، وَالْفِعْلُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
      "حَتَّى here means «so that» (purpose): a jarr letter after which an unspoken أَنْ must put the verb in nasb; the masdar so built is in jarr by حَتَّى.",
      "Hattâ burada «-sin diye» (ta'lîl) anlamında cer harfi; sonraki fiil vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr."),
  tok("يُنْزِلُوهَا", "anzala", "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "form-iv-verbs", "al-bariz-al-muttasil", "maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "Present verb in nasb by the unspoken أَنْ after حَتَّى, its sign the dropped nun (one of the five verbs); the waw is its doer, in the seat of raf', and «them» its object, in the seat of nasb.",
      "Hattâ'dan sonra gizli en ile mansûb muzâri; ef'âl-i hamseden olduğu için alâmeti nûnun hazfi; vâv fâil, mahallen merfû; «onları» mef'ûlün bih, mahallen mansûb.",
      segments=[seg("يُنْزِلُو", "anzala", "verb"), seg("هَا", "pron-3fs", "pron")]),
  FI(),
  QARN_J(),
  DHAHABI_J(),
  ZARF("وَرَاءَ", "wara"),
  MUDAF_ILAYH("السِّلْسِلَةِ", "silsila", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "When morning came, the Byzantines saw the Ottoman ships in the Golden Horn and were seized with great fear.",
                                       "tr": "Sabah olunca Rumlar Osmanlı gemilerini Haliç'te gördüler ve büyük bir korkuya kapıldılar."},
 "tokens": [LAMMA2("فَلَمَّا"),
  tok("أَصْبَحَ", "asbaha", "verb", ["al-fil-al-tamm-wal-naqis", "form-iv-verbs", "kana-wa-akhawatuha"],
      "أَصْبَحَ هُنَا فِعْلٌ تَامٌّ بِمَعْنَى «دَخَلَ فِي الصَّبَاحِ»، مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ بَعْدَهُ" + LAMMA_CL[0] + ".",
      "أَصْبَحَ used here as a complete verb, «entered the morning»: a past verb built on fatha, its doer following" + LAMMA_CL[1] + ".",
      "Asbaha burada tam fiil («sabaha erdi»); fetha üzere mebnî mâzî, fâili sonra gelir" + LAMMA_CL[2] + "."),
  FAIL("الرُّومُ", "rum", "propn"),
  RAAW("رَأَوُا", note=("، وَحُرِّكَتِ الْوَاوُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ" + JAWAB_LAMMA[0], "; the waw is voweled with damma before the following ال" + JAWAB_LAMMA[1], "; vâv iki sâkin karşılaştığı için damme ile harekelendi" + JAWAB_LAMMA[2])),
  MAFUL("السُّفُنَ", "safina", extra=["jam-taksir"]),
  NAAT("الْعُثْمَانِيَّةَ", "uthmani", "nasb", ["ism-mansub"]),
  FI(),
  QARN_J(),
  DHAHABI_J(punct="،"),
  VERB_WAW("فَخَافُوا", "khafa", ["hollow-verbs"]),
  MUTLAQ_NAW("خَوْفًا", "khawf"),
  NAAT("عَظِيمًا", "azim", "nasb", punct=".")]})

# ---- Chapter 5 — الْفَتْحُ ----
S5 = []
S5.append({"id": "s1", "translation": {"en": "The length of the siege was fifty-three days.", "tr": "Kuşatmanın süresi elli üç gün oldu."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  ISMK("مُدَّةُ", "mudda", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  MUDAF_ILAYH("الْحِصَارِ", "hisar", extra=["masdar"]),
  KHK("ثَلَاثَةً", "thalatha", extra=["asma-al-adad-fil-kafiya"],
      note_ar=" — وَثَبَتَتْ فِيهِ التَّاءُ لِأَنَّ مَعْدُودَهُ «يَوْم» مُذَكَّرٌ: الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى تِسْعَةٍ يُخَالِفُ مَعْدُودَهُ، وَلَوْ عُطِفَ عَلَيْهِ عَقْدٌ",
      note_en=" — it keeps its ta because its counted noun «day» is masculine: three to nine take the opposite gender, even with a ten-number conjoined to them",
      note_tr=" — ma'dûdu «gün» müzekker olduğu için tâ'sı sâbittir: üçten dokuza kadar sayılar, üzerlerine onluk ma'tûf olsa da ma'dûda zıt gelir"),
  ATF("وَخَمْسِينَ", "khamsun", case="nasb", extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
      note_en=" — in nasb by the ya, as it declines like a sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mansûb"),
  tok("يَوْمًا", "yawm", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh", "asma-al-adad-fil-kafiya"],
      "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — تَمْيِيزُ الْعَدَدِ الْمَعْطُوفِ (مِنْ أَحَدٍ وَعِشْرِينَ إِلَى تِسْعَةٍ وَتِسْعِينَ) مُفْرَدٌ مَنْصُوبٌ.",
      "A specifier (tamyiz), in nasb — the counted noun after a conjoined number (twenty-one to ninety-nine) is a singular in nasb.",
      "Temyîz, mansûb — ma'tûf sayının (yirmi birden doksan dokuza kadar) temyîzi müfred ve mansûbdur.", punct=".")]})
S5.append({"id": "s2", "translation": {"en": "Then the Sultan ordered his soldiers to attack before dawn, and they assaulted the walls from land and sea together.",
                                       "tr": "Sonra Sultan askerlerine şafaktan önce hücum emri verdi; onlar da karadan ve denizden birlikte surlara hücum ettiler."},
 "tokens": [THUMMA(),
  MADI("أَمَرَ", "amara-command"),
  FAIL("السُّلْطَانُ", "sultan"),
  ENC_NOUN("جُنُودَهُ", "jund", "هُ", "maful", extra=["jam-taksir"]),
  BI_NOUN("بِالْهُجُومِ", "hujum", "الْهُجُومِ", extra=["masdar"]),
  ZARF("قَبْلَ", "qabla", **ZAMAN),
  MUDAF_ILAYH("الْفَجْرِ", "fajr", punct="،"),
  VERB_WAW("فَهَجَمُوا", "hajama"),
  ALA(),
  MAJR("الْأَسْوَارِ", "sur-wall", extra=["jam-taksir"]),
  MINA(),
  MAJR("الْبَرِّ", "barr-land"),
  ATF("وَالْبَحْرِ", "bahr", case="jarr"),
  HAL("مَعًا", "maan", punct=".", note_ar="، وَصَاحِبُهُ وَاوُ الْجَمَاعَةِ", note_en=" — its owner is the waw of the group: the soldiers, all at once", note_tr=" — sahibi cemaat vâvıdır: askerler, hep birlikte")]})
S5.append({"id": "s3", "translation": {"en": "The Byzantines fought them fiercely; then the Ottomans entered the city in the morning.", "tr": "Rumlar onlarla şiddetle çarpıştı; sonra Osmanlılar sabahleyin şehre girdi."},
 "tokens": [ENC_MADI("فَقَاتَلَهُمُ", "qatala-fight", "هُمُ", ["form-iii-verbs"],
      note_ar=" — وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ بَعْدَهُ", note_en="; the mim is voweled with damma before the following ال, and the doer follows", note_tr="; mîm iki sâkin karşılaştığı için damme ile harekelendi; fâili sonra gelir"),
  FAIL("الرُّومُ", "rum", "propn"),
  MUTLAQ_NAW("قِتَالًا", "qital"),
  NAAT("شَدِيدًا", "shadid", "nasb", punct="،"),
  THUMMA(),
  MADI("دَخَلَ", "dakhala"),
  UTHMANIYYUN_F(),
  MAFUL("الْمَدِينَةَ", "madina"),
  FI(),
  MAJR("الصَّبَاحِ", "sabah", punct=".")]})
S5.append({"id": "s4", "translation": {"en": "That was on Tuesday, in the year 1453 of the Christian era.", "tr": "Bu, salı günü, milâdî 1453 yılında oldu."},
 "tokens": [KANA("وَكَانَ"),
  DHALIKA_SEAT("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi", extra=["kana-wa-akhawatuha"]),
  FI(),
  MAJR("يَوْمِ", "yawm", note_ar=MUD[0] + KH_KANA_J[0], note_en=MUD[1] + KH_KANA_J[1], note_tr=MUD[2] + KH_KANA_J[2]),
  MUDAF_ILAYH("الثُّلَاثَاءِ", "thulatha", punct="،"),
  ZARF("سَنَةَ", "sana", note_ar=" إِلَى الْعَدَدِ بَعْدَهُ", note_en=" to the number after it", note_tr=" — sonraki sayıya", **ZAMAN),
  MUDAF_ILAYH("ثَلَاثٍ", "thalath", extra=["asma-al-adad-fil-kafiya"],
      note_ar=" — وَحُذِفَتْ مِنْهُ التَّاءُ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ", note_en=" — without the ta, because the thing counted, «year», is feminine", note_tr=" — ma'dûd «sene» müennes olduğu için tâsız"),
  ATF("وَخَمْسِينَ", "khamsun", case="jarr", extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
      note_en=" — in jarr by the ya, as it declines like a sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr"),
  tok("وَأَرْبَعِمِائَةٍ", "arbaumia", "noun", ["atf-nasaq", "asma-al-adad-fil-kafiya", "idafa-definiteness"],
      WA_AR + "«أَرْبَعِ» مَعْطُوفٌ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَ«مِائَةٍ» مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — وَحُذِفَتِ التَّاءُ مِنْ أَرْبَعٍ لِأَنَّ الْمِائَةَ مُؤَنَّثَةٌ، وَيُكْتَبُ الْجُزْآنِ كَلِمَةً وَاحِدَةً.",
      "The waw conjoins; «four» is conjoined in jarr and annexed, and «hundred» is the second term in jarr — four drops its ta because مِائَة is feminine, and the two parts are written as one word.",
      "«ve» + «erba'» ma'tûf, mecrûr, muzâf; «mie» muzâfun ileyh, mecrûr — mie müennes olduğu için erba' tâsızdır; iki parça tek kelime yazılır.",
      segments=[seg("وَ", "wa", "conj"), seg("أَرْبَعِمِائَةٍ", "arbaumia", "noun")]),
  ATF("وَأَلْفٍ", "alf", case="jarr", extra=["asma-al-adad-fil-kafiya"]),
  LI_AL("لِلْمِيلَادِ", "milad", "الْمِيلَادِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنْ سَنَةَ، أَيْ: مَحْسُوبَةً مِنَ الْمِيلَادِ",
      note_en=" — the phrase hangs on an omitted hal: the year as counted from the Nativity, «AD»", note_tr=" — câr-mecrûr mahzûf bir hâle müteallık: mîlâddan sayılan yıl, «milâdî»", punct=".")]})
S5.append({"id": "s5", "translation": {"en": "When the Sultan entered the city, he granted its people safety out of mercy for them, and left them to their religion.",
                                       "tr": "Sultan şehre girince, onlara olan merhametinden dolayı halkına eman verdi ve onları dinleri üzere bıraktı."},
 "tokens": [LAMMA2("فَلَمَّا"),
  MADI("دَخَلَ", "dakhala", note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]),
  FAIL("السُّلْطَانُ", "sultan"),
  MAFUL("الْمَدِينَةَ", "madina", punct="،"),
  tok("أَعْطَى", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "mafulayn"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ، وَهُوَ يَنْصِبُ مَفْعُولَيْنِ" + JAWAB_LAMMA[0] + ".",
      "Past verb built on a fatha estimated on the alif; its doer «he» is hidden, and it takes two objects" + JAWAB_LAMMA[1] + ".",
      "Elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil gizli zamir «o»; iki mef'ûl alır" + JAWAB_LAMMA[2] + "."),
  ENC_NOUN("أَهْلَهَا", "ahl", "هَا", "maful", extra=["mafulayn"], note_ar=" — وَهُوَ الْمَفْعُولُ الْأَوَّلُ", note_en=" — the first object", note_tr=" — birinci mef'ûl"),
  tok("الْأَمَانَ", "aman", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb.", "İkinci mef'ûlün bih, mansûb."),
  tok("رَحْمَةً", "rahma", "noun", ["maful-lah", "al-maful-fih-wal-maful-lah", "masdar"],
      "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، وَيُشَارِكُهُ فِي الْوَقْتِ وَالْفَاعِلِ.",
      "The object of purpose (maf'ul li-ajlih), in nasb — a masdar of the heart that gives the reason for the act, sharing its time and its doer: «out of mercy».",
      "Mef'ûlün lieclih, mansûb — fiilin sebebini bildiren kalbî masdar; zamanı ve fâili fiille ortaktır: «merhametinden dolayı»."),
  JARR_PRON("بِهِمْ", "bi", "بِ", "هِمْ", " («onlara»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِرَحْمَةً", note_en="; the phrase hangs on «mercy»", note_tr="; câr-mecrûr «merhamet»e müteallık", punct="،"),
  ENC_MADI("وَتَرَكَهُمْ", "taraka", "هُمْ", hidden=True),
  ALA(),
  ENC_NOUN("دِينِهِمْ", "din", "هِمْ", "majr", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنَ الضَّمِيرِ هُمْ", note_en="; the phrase hangs on an omitted hal of «them»: «[remaining] upon their religion»", note_tr="; câr-mecrûr «onları» zamirinden mahzûf bir hâle müteallık", punct=".")]})
S5.append({"id": "s6", "translation": {"en": "He made it the capital of his state, and it remained the capital of the Ottomans for a long time.", "tr": "Onu devletinin başşehri yaptı; şehir uzun zaman Osmanlıların başşehri olarak kaldı."},
 "tokens": [ENC_MADI("وَجَعَلَهَا", "jaala", "هَا", ["mafulayn"], hidden=True, note_ar=" — وَهُوَ الْمَفْعُولُ الْأَوَّلُ، فَجَعَلَ هُنَا بِمَعْنَى صَيَّرَ يَنْصِبُ مَفْعُولَيْنِ", note_en=" — the first object: جَعَلَ here means «to make into» and takes two objects", note_tr=" — birinci mef'ûl; ca'ale burada «kılmak» anlamında iki mef'ûl alır"),
  tok("عَاصِمَةً", "asima", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ.", "The second object, in nasb.", "İkinci mef'ûlün bih, mansûb."),
  LI_ENC("لِدَوْلَتِهِ", "dawla", "دَوْلَتِ", "هِ", punct="،"),
  tok("فَظَلَّتْ", "zalla-remain", "verb", ["kana-wa-akhawatuha", "doubled-verbs"],
      FA_AR + "ظَلَّ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى الْمَدِينَةِ.",
      "The fa conjoins; ظَلَّ «remained» is one of كَانَ's sisters, built on fatha, the ta marking the feminine; its noun is the hidden «she» — the city.",
      "«bunun üzerine» + zalle «kaldı»: kâne'nin kardeşlerinden nâkıs mâzî, fetha üzere mebnî; tâ te'nîs içindir; ismi şehre dönen gizli zamir «o».",
      segments=[seg("فَ", "fa", "conj"), seg("ظَلَّتْ", "zalla-remain", "verb")]),
  tok("عَاصِمَةً", "asima", "noun", ["kana-wa-akhawatuha"], "خَبَرُ ظَلَّ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of ظَلَّ, in nasb.", "Zalle'nin haberi, mansûb."),
  tok("لِلْعُثْمَانِيِّينَ", "li", "prep", ["huruf-jarr", "jam-mudhakkar-salim", "ism-mansub"],
      "اللَّامُ حَرْفُ جَرٍّ، وَالْعُثْمَانِيِّينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ.",
      "The lam is a jarr letter; «the Ottomans» after it is in jarr by the ya, a sound masculine plural.",
      "Lâm cer harfi; «Osmanlılar» cem-i müzekker sâlim olduğu için yâ ile mecrûr.",
      segments=[seg("لِ", "li", "prep"), seg("الْعُثْمَانِيِّينَ", "uthmani", "noun")]),
  ZARF("زَمَنًا", "zaman-period", mudaf=False, **ZAMAN),
  NAAT("طَوِيلًا", "tawil-long", "nasb", punct=".")]})
S5.append({"id": "s7", "translation": {"en": "After this conquest Sultan Mehmed was named al-Fātiḥ, the Conqueror.", "tr": "Bu fetihten sonra Sultan Mehmed'e «Fâtih» adı verildi."},
 "tokens": [tok("وَسُمِّيَ", "samma", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs", "naqis-verbs", "mafulayn"],
      WA_AR + "سُمِّيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — وَسَمَّى يَنْصِبُ مَفْعُولَيْنِ، فَلَمَّا بُنِيَ لِلْمَجْهُولِ رُفِعَ أَوَّلُهُمَا نَائِبًا عَنِ الْفَاعِلِ وَبَقِيَ الثَّانِي مَنْصُوبًا.",
      "The waw conjoins; «was named» is a past verb in the passive, built on fatha — سَمَّى takes two objects, and in the passive the first is raised as deputy doer while the second stays in nasb.",
      "«ve» + meçhul mâzî, fetha üzere mebnî — sammâ iki mef'ûl alır; meçhul olunca birincisi nâib-i fâil olarak merfû olur, ikincisi mansûb kalır.",
      segments=[seg("وَ", "wa", "conj"), seg("سُمِّيَ", "samma", "verb")]),
  NAIB("السُّلْطَانُ", "sultan"),
  tok("مُحَمَّدٌ", "muhammad", "propn", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"], "بَدَلٌ مِنَ السُّلْطَانِ مَرْفُوعٌ بِالضَّمَّةِ.", "A badal of «the Sultan», in raf' like it.", "«Sultan»dan bedel, onun gibi merfû."),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A demonstrative, built on sukun, in the seat of jarr as the second term of the idafa.", "İşaret ismi, sükûn üzere mebnî; muzâfun ileyh olarak mahallen mecrûr."),
  BADAL("الْفَتْحِ", "fath", "jarr", extra=["masdar"]),
  tok("الْفَاتِحَ", "fatih-conqueror", "noun", ["maful-bihi", "mafulayn", "ism-fail"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ فَاعِلٍ مِنْ فَتَحَ صَارَ لَقَبًا.",
      "The second object, in nasb — the active participle of فَتَحَ, become a title: «the Conqueror».", "İkinci mef'ûlün bih, mansûb — fetaha'nın ism-i fâili, lakap olmuştur: «Fâtih».", punct=".")]})
S5.append({"id": "s8", "translation": {"en": "And by this the Muslims attained what they had hoped for over a long time.", "tr": "Böylece Müslümanlar uzun zamandır umdukları şeye kavuştular."},
 "tokens": [tok("وَبِذٰلِكَ", "bi", "prep", ["huruf-jarr", "asma-al-ishara"],
      WA_AR + "الْبَاءُ حَرْفُ جَرٍّ لِلسَّبَبِيَّةِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ" + DHALIKA_TAIL[0] + "؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِنَالَ.",
      "The waw conjoins; the ba is a jarr letter of cause («by this»), and the demonstrative after it is built on sukun in the seat of jarr" + DHALIKA_TAIL[1] + "; the phrase hangs on «attained».",
      "«ve» + sebebiyet bâ'sı cer harfi; işaret ismi sükûn üzere mebnî, mahallen mecrûr" + DHALIKA_TAIL[2] + "; câr-mecrûr «nâil oldu»ya müteallık.",
      segments=[seg("وَ", "wa", "conj"), seg("بِ", "bi", "prep"), seg("ذٰلِكَ", "dhalika", "pron")]),
  MADI("نَالَ", "nala", ["hollow-verbs"]),
  FAIL("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign=SALIM_W, note_en=SALIM_W_EN, note_tr=SALIM_W_TR),
  MAWSUL_MAF("مَا", "ma-mawsula", built="السُّكُونِ", built_en="sukun", built_tr="sükûn"),
  KANU("كَانُوا"),
  tok("يَرْجُونَهُ", "raja", "verb", ["afal-khamsa", "mudari-marfu", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "kana-wa-akhawatuha", "ism-mawsul"],
      "فِعْلٌ مُضَارِعٌ مِنَ الْأَفْعَالِ الْخَمْسَةِ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَهِيَ الْعَائِدُ عَلَى مَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ، وَجُمْلَةُ كَانُوا وَمَا بَعْدَهَا صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
      "One of the five verbs, in raf' by the kept nun; the waw is its doer, in the seat of raf', and «it» its object, in the seat of nasb — the pronoun returning to مَا. The clause is the predicate of كَانُوا, and كَانُوا with what follows is the relative's ṣila, with no seat of its own.",
      "Ef'âl-i hamseden muzâri, nûnun sübûtuyla merfû; vâv fâil, mahallen merfû; «hû» mef'ûlün bih, mahallen mansûb — mâ'ya dönen âid zamir. Cümle kâne'nin haberi, mahallen mansûb; «kânû» ve sonrası sıla cümlesidir, i'râbdan mahalli yoktur.",
      segments=[seg("يَرْجُونَ", "raja", "verb"), seg("هُ", "pron-3ms", "pron")]),
  ZARF("زَمَنًا", "zaman-period", mudaf=False, **ZAMAN),
  NAAT("طَوِيلًا", "tawil-long", "nasb", punct=".")]})

CHAPTERS = [
 ("ch1", {"ar": "أَمَلٌ قَدِيمٌ", "en": "An Old Hope", "tr": "Eski Bir Ümit"}, S1),
 ("ch2", {"ar": "قَلْعَةُ رُومَلِي", "en": "The Fortress of Rumeli (Rumeli Hisarı)", "tr": "Rumeli Hisarı"}, S2),
 ("ch3", {"ar": "الْمَدَافِعُ وَالسِّلْسِلَةُ", "en": "The Cannons and the Chain", "tr": "Toplar ve Zincir"}, S3),
 ("ch4", {"ar": "السُّفُنُ عَلَى الْبَرِّ", "en": "Ships over Land", "tr": "Karadan Yürüyen Gemiler"}, S4),
 ("ch5", {"ar": "الْفَتْحُ", "en": "The Conquest", "tr": "Fetih"}, S5),
]
TITLES = [c[1] for c in CHAPTERS]
CHAPS = [c[2] for c in CHAPTERS]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-x-verbs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            g = t.get("grammar", [])
            if DERIVED & set(g): g = [x for x in g if x != "thulathi-mujarrad-babs"]
            t["grammar"] = list(dict.fromkeys(g))

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule); the new entries are listed below
SAMPLES = ROOT / "content/samples"
PREF = ["qisas-al-nabiyyin-4", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-1", "dhu-al-qarnayn-wa-al-sadd", "musa-wa-firawn", "ashab-al-ghar",
        "al-amana-wa-al-khashaba", "juha-wa-al-himar", "wasiyyat-abi-yusuf-l5", "al-usul-al-munifa", "al-kafiya", "talkhis-al-miftah"]
PREF = [p for p in PREF if (SAMPLES / p / "glossary.json").exists()]
PREF += sorted(d.name for d in SAMPLES.iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != PKG.name)
# keys that two packages gloss differently are pinned to the package whose sense this story uses
FORCE = {"sultan": "wasiyyat-abi-yusuf-l5", "darb": "al-kafiya", "muslim": "qisas-al-nabiyyin-4", "lam-jazima": "dhu-al-qarnayn-wa-al-sadd",
         "ma-mawsula": "al-asad-wa-al-arnab", "aman": "bad-al-amali", "hasin": "marah-al-arwah", "barr-land": "qisas-al-nabiyyin-2",
         "shahm": "umar-wa-al-qidr"}   # شَحْم «fat, suet» — first minted by «عُمَرُ وَالْقِدْرُ»; reused by lemma identity
_G = {p: json.loads((SAMPLES / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((SAMPLES / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) if (SAMPLES / p / "morphology.json").exists() else {} for p in PREF}
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
 "qustantiniyya": {"lemma": "الْقُسْطَنْطِينِيَّة", "pos": "propn", "gloss": {"en": "Constantinople — the city named after Constantine, Istanbul", "tr": "Kostantiniyye — Konstantin'e nisbetle anılan şehir, İstanbul"}, "level": 5},
 "busfur": {"lemma": "الْبُوسْفُور", "pos": "propn", "gloss": {"en": "the Bosphorus (a foreign name, written with the article)", "tr": "Bosfor, İstanbul Boğazı (başına el- gelen yabancı isim)"}, "level": 5},
 "asima": {"lemma": "عَاصِمَة", "root": "ع ص م", "pos": "noun", "plural": "عَوَاصِم", "gloss": {"en": "a capital city", "tr": "başşehir, başkent"}, "level": 4},
 "sur-wall": {"lemma": "سُور", "root": "س و ر", "pos": "noun", "plural": "أَسْوَار", "gloss": {"en": "a city wall, a rampart", "tr": "sur, kale duvarı"}, "level": 4},
 "qala-fortress": {"lemma": "قَلْعَة", "root": "ق ل ع", "pos": "noun", "plural": "قِلَاع", "gloss": {"en": "a fortress, a castle", "tr": "kale, hisar"}, "level": 4},
 "madiq": {"lemma": "مَضِيق", "root": "ض ي ق", "pos": "noun", "plural": "مَضَايِق", "gloss": {"en": "a strait, a narrow passage", "tr": "boğaz, dar geçit"}, "level": 5},
 "adyaq": {"lemma": "أَضْيَق", "root": "ض ي ق", "pos": "noun", "gloss": {"en": "narrower, narrowest (the elative of ضَيِّق; a diptote)", "tr": "daha dar, en dar (ضَيِّق'in ism-i tafdîli; gayr-i munsarif)"}, "level": 5},
 "amil-worker": {"lemma": "عَامِل", "root": "ع م ل", "pos": "noun", "plural": "عُمَّال", "gloss": {"en": "a worker, a labourer (pl. عُمَّال)", "tr": "işçi, amele (ç. عُمَّال)"}, "level": 4},
 "midfa": {"lemma": "مِدْفَع", "root": "د ف ع", "pos": "noun", "plural": "مَدَافِع", "gloss": {"en": "a cannon (a noun of instrument on مِفْعَل; its plural مَدَافِعُ is a diptote)", "tr": "top (mif'al vezninde ism-i âlet; çoğulu مَدَافِعُ gayr-i munsarif)"}, "level": 5},
 "silsila": {"lemma": "سِلْسِلَة", "root": "س ل س ل", "pos": "noun", "plural": "سَلَاسِل", "gloss": {"en": "a chain", "tr": "zincir"}, "level": 4},
 "dakhm": {"lemma": "ضَخْم", "root": "ض خ م", "pos": "noun", "gloss": {"en": "huge, massive", "tr": "iri, kocaman"}, "level": 5},
 "dhahabi": {"lemma": "ذَهَبِيّ", "root": "ذ ه ب", "pos": "noun", "gloss": {"en": "golden (the nisba of ذَهَب); الْقَرْنُ الذَّهَبِيُّ: the Golden Horn", "tr": "altın, altından (ذَهَب'e nisbe); el-Karnu'z-zehebî: Haliç"}, "level": 5},
 "uthmani": {"lemma": "عُثْمَانِيّ", "root": "ع ث م", "pos": "noun", "plural": "عُثْمَانِيُّونَ", "gloss": {"en": "Ottoman (the nisba of ʿUthmān, the dynasty's founder)", "tr": "Osmanlı (hanedanın kurucusu Osman'a nisbe)"}, "level": 5},
 "lawh-board": {"lemma": "لَوْح", "root": "ل و ح", "pos": "noun", "plural": "أَلْوَاح", "gloss": {"en": "a board, a plank (of wood)", "tr": "levha, tahta, kalas"}, "level": 4},
 "hisar": {"lemma": "حِصَار", "root": "ح ص ر", "pos": "noun", "gloss": {"en": "a siege (a masdar of حَاصَرَ)", "tr": "kuşatma, muhasara (حَاصَرَ'nin masdarı)"}, "level": 5},
 "hasara": {"lemma": "حَاصَرَ", "root": "ح ص ر", "pos": "verb", "form": "III", "gloss": {"en": "to besiege (Form III)", "tr": "kuşatmak, muhasara etmek (müfâale)"}, "level": 5},
 "hajama": {"lemma": "هَجَمَ", "root": "ه ج م", "pos": "verb", "gloss": {"en": "to attack, to assault (هَجَمَ عَلَى; bāb naṣara)", "tr": "hücum etmek, saldırmak (هَجَمَ عَلَى; nasara bâbı)"}, "level": 5},
 "hujum": {"lemma": "هُجُوم", "root": "ه ج م", "pos": "noun", "gloss": {"en": "an attack, an assault (the masdar of هَجَمَ)", "tr": "hücum, saldırı (هَجَمَ'nin masdarı)"}, "level": 5},
 "azm-resolve": {"lemma": "عَزْم", "root": "ع ز م", "pos": "noun", "gloss": {"en": "resolve, firm determination (the masdar of عَزَمَ)", "tr": "azim, kesin karar (عَزَمَ'nin masdarı)"}, "level": 4},
 "thulatha": {"lemma": "الثُّلَاثَاء", "root": "ث ل ث", "pos": "noun", "gloss": {"en": "Tuesday (يَوْمُ الثُّلَاثَاءِ)", "tr": "salı (günü)"}, "level": 4},
 "arbaumia": {"lemma": "أَرْبَعُمِائَة", "root": "ر ب ع", "pos": "noun", "gloss": {"en": "four hundred", "tr": "dört yüz"}, "level": 4},
 "milad": {"lemma": "مِيلَاد", "root": "و ل د", "pos": "noun", "gloss": {"en": "birth, nativity; لِلْمِيلَادِ: of the Christian era (AD)", "tr": "doğum; li'l-mîlâd: milâdî"}, "level": 5},
 "fatih-conqueror": {"lemma": "فَاتِح", "root": "ف ت ح", "pos": "noun", "gloss": {"en": "a conqueror (the active participle of فَتَحَ); الْفَاتِحُ: the title of Sultan Mehmed II", "tr": "fetheden, fâtih (فَتَحَ'nin ism-i fâili); el-Fâtih: Sultan II. Mehmed'in lakabı"}, "level": 5},
}
NEW_VERBS = {
 "hasara": _sg.derived(_sg.B3, _sg.W3, "ُ", "حَاصَر", "حَاصِر", "حَاصِر", "حِصَار / مُحَاصَرَة", "مُحَاصِر", "مُحَاصَر", "حُوصِرَ", "يُحَاصَرُ",
                       "حَاصَرَ الْعَدُوَّ يُحَاصِرُهُ حِصَارًا وَمُحَاصَرَةً: أَحَاطَ بِهِ وَمَنَعَهُ مِنَ الْخُرُوجِ."),
 "hajama": _sg.sound1("nasara", "هَجَم", "هْجُم", "اُهْجُم", "هُجُوم", "هَاجِم",
                      note="هَجَمَ عَلَيْهِ يَهْجُمُ هُجُومًا مِنْ بَابِ نَصَرَ: انْقَضَّ عَلَيْهِ؛ لَازِمٌ يَتَعَدَّى بِعَلَى، فَلَا يُبْنَى مِنْهُ مَجْهُولٌ إِلَّا مَعَ الْجَارِّ."),
}
# a key minted by a sibling story released in the same wave: used only if that package is not on the shelf yet (same entry)
SHELF_FALLBACK = {"shahm": {"lemma": "شَحْم", "root": "ش ح م", "pos": "noun", "plural": "شُحُوم", "gloss": {"en": "fat, suet", "tr": "iç yağı, yağ"}, "level": 4}}
# a key is a global claim: a NEW key must not already be on the shelf with another sense
for k in NEW_GLOSS:
    for p in PREF:
        # (v324) a sibling story of the same wave may mint the same word: the same LEMMA under the same key is one word
        if k in _G[p] and _G[p][k].get("lemma") != NEW_GLOSS[k].get("lemma"): raise SystemExit(f"new key {k!r} already exists in {p}")

used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
GLOSS, missing = {}, []
for k in sorted(used):
    e = NEW_GLOSS.get(k) or find_gloss(k) or SHELF_FALLBACK.get(k)
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
 "id": "fath-al-qustantiniyya",
 "storyGroup": "fath-al-qustantiniyya",
 "title": {"ar": "فَتْحُ الْقُسْطَنْطِينِيَّةِ", "en": "The Conquest of Constantinople", "tr": "İstanbul'un Fethi"},
 "subtitle": {"ar": "السُّلْطَانُ الشَّابُّ مُحَمَّدٌ الْفَاتِحُ: قَلْعَةٌ عَلَى الْبُوسْفُورِ، وَمَدَافِعُ تَضْرِبُ الْأَسْوَارَ، وَسُفُنٌ تَسِيرُ عَلَى الْبَرِّ — قِصَّةٌ لِلْمُسْتَوَى الْخَامِسِ",
              "en": "The young Sultan Mehmed the Conqueror: a fortress on the Bosphorus, cannons pounding the walls, and ships that travel over land — a story for the fifth level",
              "tr": "Genç Sultan Fâtih Mehmed: Boğaz'da bir hisar, surları döven toplar ve karadan yürüyen gemiler — beşinci seviye için bir hikâye"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "قِصَّةٌ تَارِيخِيَّةٌ أَصْلِيَّةٌ (الْمُسْتَوَى الْخَامِسُ) تَرْوِي فَتْحَ الْقُسْطَنْطِينِيَّةِ سَنَةَ ٨٥٧ هـ / ١٤٥٣ م، أُلِّفَتْ بِأُسْلُوبِ الْقَارِئِ الْمُتَدَرِّجِ عَلَى مَا اتَّفَقَتْ عَلَيْهِ الْمَصَادِرُ الْعُثْمَانِيَّةُ وَالْبِيزَنْطِيَّةُ. لَيْسَتْ فِيهَا جُمْلَةٌ هِيَ نَصُّ مَصْدَرٍ، وَلَا آيَةٌ وَلَا حَدِيثٌ؛ وَتُرِكَتِ الْأَعْدَادُ وَالْأَخْبَارُ الْمُخْتَلَفُ فِيهَا. كُلُّ إِعْرَابٍ فِيهَا اجْتِهَادُ الْمُؤَلِّفِ، وَهِيَ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "ORIGINAL Level-5 graded Arabic: a historical narrative of the conquest of Constantinople in 857 AH / 1453 CE, composed for this reader from the well-attested core of the event as the Ottoman and Byzantine chronicles tell it (among them Âşıkpaşazâde, Tursun Bey, Doukas, Kritoboulos and Sphrantzes). No sentence is a quotation from any source, no verse or hadith is quoted, and disputed numbers and anecdotes are left out. Every i'rab line is the author's own analysis, pending scholarly review.",
  "tr": "ÖZGÜN 5. seviye kolaylaştırılmış Arapça: 857 / 1453 yılındaki İstanbul fethinin, Osmanlı ve Bizans kroniklerinin (Âşıkpaşazâde, Tursun Bey, Dukas, Kritovulos ve Sfrancis gibi) ittifakla anlattığı sağlam çekirdeğe dayanılarak bu okuyucu için yazılmış tarihî anlatısı. Hiçbir cümle herhangi bir kaynaktan alıntı değildir; âyet ya da hadis aktarılmamış, ihtilaflı sayı ve rivayetler dışarıda bırakılmıştır. Her i'râb satırı yazarın kendi tahlilidir ve ilmî incelemeyi beklemektedir.",
  "reviewStatus": "pending-scholarly-review",
 },
}

(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]),
      "new:", sorted(k for k in GLOSS if k in NEW_GLOSS), "->", PKG)
