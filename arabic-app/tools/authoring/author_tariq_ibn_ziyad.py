"""Author content/samples/tariq-ibn-ziyad — «طَارِقُ بْنُ زِيَادٍ وَعُبُورُ الْبَحْرِ», an ORIGINAL historical story at Level 5.

ORIGINAL graded Arabic: the crossing into al-Andalus in 92 AH / 711 CE. Mūsā ibn Nuṣayr, the governor of the Maghrib,
sends his commander Ṭāriq ibn Ziyād across the strait with an army of Berbers and Arabs; they land by the mountain that
took his name (Jabal Ṭāriq, Gibraltar); the Visigothic king Ludhrīq (Roderic) marches against them and is routed; the
cities open, Ṭāriq reaches the capital; in 93 Mūsā crosses with a second army, conquers other cities and joins him. The
event is told by Ibn ʿAbd al-Ḥakam (Futūḥ Miṣr wa-l-Maghrib), Ibn ʿIdhārī (al-Bayān al-Mughrib) and al-Maqqarī (Nafḥ
al-Ṭīb); it is RETOLD FREELY — no sentence is a quotation from them, no āya or ḥadīth is quoted, no words are put in a
historical person's mouth. Left out as legend or as disputed: the burning of the ships, the speech «الْبَحْرُ مِنْ
وَرَائِكُمْ», every army size, Count Julian, the battle site, Roderic's fate, the name of the capital (طُلَيْطُلَة /
طُلَيْطِلَة: the vowelling is disputed) and the province name إِفْرِيقِيَّة (the doubling of its yāʾ is disputed).

Five chapters, twenty-eight sentences, in a Level-5 register: maf'ūl muṭlaq (قِتَالًا شَدِيدًا، صَبْرًا عَظِيمًا), maf'ūl lahu
(خَوْفًا عَلَى مُلْكِهِ), tamyīz after the elative (أَقَلُّ عَدَدًا), the emptied istithnāʾ (لَمْ يَكُنْ … إِلَّا مَضِيقٌ), relative and
ṣifa clauses with a resumptive pronoun (الَّذِي نَزَلُوا عِنْدَهُ، بَابًا دَخَلَ مِنْهُ، رَجُلًا اسْمُهُ …), لَمَّا (twice), حَتَّى + the
subjunctive (حَتَّى يَلْحَقَ), wāw al-ḥāl (وَالْمُسْلِمُونَ أَقَلُّ …، وَقَدْ خَرَجَ …), the passive (سُمِّيَ، هُزِمَ، فُتِحَتْ، تُسَمَّى،
بُنِيَتْ، يُعْرَفُ), كَانَ with a fronted predicate, لَمْ يَكُنْ، لَمْ يَزَلْ، مَا زَالَ، صَارَ, أَمَّا … فَـ, the numbers 92 and 93 with
سَنَة, the dual, and the tawkīd نَفْسِهَا. Written on the authoring kit (story_kit.py); glosses and paradigms are copied by
lemma identity from the shelf; the new entries are listed in NEW_GLOSS (no new verb).  Regenerate with:
QISSA_PKG_ROOT=<dir> python3 tools/authoring/author_tariq_ibn_ziyad.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/qissa-main/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
SLUG = "tariq-ibn-ziyad"
PKG = OUT_ROOT / SLUG
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

PRON.update({"هُ": "pron-3ms", "هِ": "pron-3ms", "هَا": "pron-3fs", "هُمْ": "pron-3mp", "هِمْ": "pron-3mp", "هُمُ": "pron-3mp"})
PRON_AR.update({"هُ": "الْهَاءُ", "هِ": "الْهَاءُ", "هَا": "هَا", "هُمْ": "هُمْ", "هِمْ": "هُمْ", "هُمُ": "هُمْ"})

N = lambda s: unicodedata.normalize("NFC", s)
def PH(t, lex, span=2):
    """the name-phrase sits on the FIRST token of its span (CLAUDE.md «Idioms/phrases»): every word keeps its own iʿrāb"""
    t["phrase"] = {"lex": lex, "span": span}
    return t

# ---- the house notes this story leans on ------------------------------------------------------------------------
MUD = ("، مُضَافٌ", ", annexed", ", muzâf")
JAWAB_LAMMA = (" — وَالْجُمْلَةُ جَوَابُ لَمَّا لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of لَمَّا and has no seat of its own", "; cümle lemmâ'nın cevabıdır, i'râbdan mahalli yoktur")
KH_KANA_J = ("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", "; the jarr phrase is the predicate of كَانَ, in the seat of nasb", "; câr-mecrûr kâne'nin haberi, mahallen mansûb")
SALIM_W = "بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ"
SALIM_W_EN, SALIM_W_TR = " — by the waw, a sound masculine plural", " — cem-i müzekker sâlim olduğu için vâv ile"
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
DHALIKA_TAIL = ("، وَاللَّامُ لِلْبُعْدِ، وَالْكَافُ لِلْخِطَابِ", "; its lam marks distance and its kaf addresses the listener", "; lâm uzaklık, kâf hitap içindir")
MUQ_A = "بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ"
DIPT_A = ("، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", " — the vowel is estimated on the alif; a foreign proper name, barred from tanwin", " — hareke elif üzerinde takdîrîdir; yabancı özel isim, gayr-i munsarif")
MUNSARIF = (" — عَلَمٌ عَرَبِيٌّ مَصْرُوفٌ", " — an Arabic proper name that keeps its tanwin", " — munsarif Arapça özel isim")
ANDALUS_N = (" — عَلَمٌ أَعْجَمِيٌّ دَخَلَتْهُ أَلْ فَجُرَّ بِالْكَسْرَةِ", " — a foreign name that carries the article, so it takes the kasra", " — başına el- gelmiş yabancı isim; bu yüzden kesre ile mecrûr")
LUDH_N = ("بِلَا تَنْوِينٍ، عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ", " without tanwin — a foreign proper name, barred from tanwin", " tenvinsiz — yabancı özel isim, gayr-i munsarif")

def DHALIKA_SEAT(seat_ar, seat_en, seat_tr, punct=None, extra=None):
    return tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"] + (extra or []),
        "ذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ " + seat_ar + DHALIKA_TAIL[0] + ".",
        "A demonstrative, built on sukun, in the seat of " + seat_en + DHALIKA_TAIL[1] + ".",
        "İşaret ismi, sükûn üzere mebnî, mahallen " + seat_tr + DHALIKA_TAIL[2] + ".", punct=punct)
def MUTLAQ_NAW(full, lex, punct=None):
    """قِتَالًا شَدِيدًا: the verb's own masdar, described — so it states the KIND of the act"""
    return tok(full, lex, "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "masdar"],
        "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرُ الْفِعْلِ قَبْلَهُ، مُبَيِّنٌ لِلنَّوْعِ لِأَنَّهُ مَوْصُوفٌ.",
        "The absolute object (maf'ul mutlaq), in nasb — the verb's own masdar; because it carries an adjective it states the KIND of the act.",
        "Mef'ûlün mutlak, mansûb — fiilin kendi masdarı; sıfatlandığı için fiilin nev'ini beyan eder.", punct=punct)
def IBN(of_ar, of_en, of_tr, punct=None):
    """بْنُ between two names: a na't of the first name, annexed to the second; its alif is dropped in writing"""
    return tok("بْنُ", "ibn-bn", "noun", ["naat-sifa", "idafa-definiteness"],
        "نَعْتٌ لِ" + of_ar + " مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — وَحُذِفَتْ أَلِفُهُ خَطًّا لِوُقُوعِهِ بَيْنَ عَلَمَيْنِ.",
        "An adjective (na't) of «" + of_en + "», in raf' and annexed — its alif is dropped in writing because it stands between two names.",
        "«" + of_tr + "»in na'tı, merfû, muzâf — iki alem arasında geldiği için elifi yazıda düşer.", punct=punct)
def MUSA_ISMK(punct=None):
    return PH(ISMK("مُوسَى", "musa", "propn", ["ism-maqsur-manqus", "mamnu-min-sarf"], DIPT_A[0], DIPT_A[1], DIPT_A[2], sign=MUQ_A, muakhkhar=True, punct=punct), "musa-ibn-nusayr", 3)
def MUSA_F(phrase=True, punct=None):
    t = FAIL("مُوسَى", "musa", "propn", ["ism-maqsur-manqus", "mamnu-min-sarf"], DIPT_A[0], DIPT_A[1], DIPT_A[2], sign=MUQ_A, punct=punct)
    return PH(t, "musa-ibn-nusayr", 3) if phrase else t
NUSAYR_MI = lambda punct=None: MUDAF_ILAYH("نُصَيْرٍ", "nusayr", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2], punct=punct)
TARIQ_F = lambda punct=None: FAIL("طَارِقٌ", "tariq-name", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2], punct=punct)
TARIQ_MI = lambda punct=None: MUDAF_ILAYH("طَارِقٍ", "tariq-name", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2], punct=punct)
ANDALUS_J = lambda punct=None: MAJR("الْأَنْدَلُسِ", "andalus", "propn", note_ar=ANDALUS_N[0], note_en=ANDALUS_N[1], note_tr=ANDALUS_N[2], punct=punct)
ANDALUS_MI = lambda punct=None: MUDAF_ILAYH("الْأَنْدَلُسِ", "andalus", "propn", note_ar=ANDALUS_N[0], note_en=ANDALUS_N[1], note_tr=ANDALUS_N[2], punct=punct)
MUSLIMUN_F = lambda punct=None: FAIL("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign=SALIM_W, note_en=SALIM_W_EN, note_tr=SALIM_W_TR, punct=punct)
MINA_BAYAN = lambda note=("", "", ""), kind=("لِبَيَانِ الْجِنْسِ", "naming the kind («of»)", "cins beyânı için"): tok("مِنَ", "min", "prep", ["huruf-jarr"],
    "حَرْفُ جَرٍّ " + kind[0] + "، وَحُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ" + note[0] + ".",
    "A jarr letter " + kind[1] + ", voweled with fatha before the following ال" + note[1] + ".",
    "«-den» — " + kind[2] + " cer harfi; iki sâkin karşılaştığı için fetha ile harekelendi" + note[2] + ".")
TABID = ("لِلتَّبْعِيضِ", "of part («a part of»)", "teb'îz (bir kısım) için")
def ALLADHI_R(of_ar, of_en, of_tr):
    """الَّذِي as a na't of a noun in raf'"""
    return tok("الَّذِي", "alladhi", "pron", ["ism-mawsul", "naat-sifa"],
        "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِ" + of_ar + ".",
        "A relative pronoun built on sukun, in the seat of raf' as a na't of «" + of_en + "».",
        "İsm-i mevsûl, sükûn üzere mebnî, «" + of_tr + "»in na'tı olarak mahallen merfû.")
def INDAHU_AID(punct=None):
    """عِنْدَهُ whose pronoun is the resumptive of a relative clause"""
    return tok("عِنْدَهُ", "inda", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "ism-mawsul"],
        "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَهِيَ الْعَائِدُ الَّذِي يَرْبِطُ الصِّلَةَ بِالْمَوْصُولِ.",
        "An adverb of place «by», in nasb and annexed to «it» (the seat of jarr) — that pronoun is the resumptive that ties the ṣila to the relative.",
        "Mekân zarfı «yanında», mansûb, muzâf; «hû» zamiri mahallen mecrûr muzâfun ileyh — sılayı mevsûle bağlayan âid zamirdir.",
        punct=punct, segments=[seg("عِنْدَ", "inda", "noun"), seg("هُ", "pron-3ms", "pron")])
TISIN = lambda: ATF("وَتِسْعِينَ", "tisun", case="jarr", extra=["jam-mudhakkar-salim", "asma-al-adad-fil-kafiya"], sign="مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ",
    note_en=" — in jarr by the ya, as it declines like a sound masculine plural", note_tr=" — cem-i müzekker sâlime mülhak olduğu için yâ ile mecrûr")

# ---- Chapter 1 — الْأَمِيرُ وَقَائِدُهُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "The Muslims had conquered most of the lands of the Maghrib, and their governor over them was Mūsā ibn Nuṣayr.",
                                       "tr": "Müslümanlar Mağrib topraklarının çoğunu fethetmişlerdi; oradaki emîrleri de Mûsâ b. Nusayr idi."},
 "tokens": [KANA("كَانَ"),
  ISMK("الْمُسْلِمُونَ", "muslim", extra=["jam-mudhakkar-salim"], sign=SALIM_W, note_en=SALIM_W_EN, note_tr=SALIM_W_TR),
  tok("قَدْ", "qad", "part", ["qad-harf"], "قَدْ حَرْفُ تَحْقِيقٍ — وَكَانَ مَعَ قَدْ وَالْمَاضِي يَدُلُّ عَلَى مَاضٍ سَبَقَ مَاضِيًا.",
      "قَدْ affirms the past verb after it — كَانَ with قَدْ and a past verb tells of a past before the past («had conquered»).",
      "Kad tahkîk harfi — kâne, kad ve mâzî ile birlikte geçmişten önceki geçmişi bildirir («fethetmişlerdi»)."),
  VERB_WAW("فَتَحُوا", "fataha", note_ar=KH_KANA_CL[0], note_en=KH_KANA_CL[1], note_tr=KH_KANA_CL[2]),
  MAFUL("أَكْثَرَ", "akthar", extra=["ism-tafdil", "idafa-definiteness"], note_ar=MUD[0] + " — اسْمُ تَفْضِيلٍ", note_en=MUD[1] + " — an elative, «most of»", note_tr=MUD[2] + " — ism-i tafdîl, «çoğu»"),
  MUDAF_ILAYH("بِلَادِ", "bilad", extra=["jam-taksir"], note_ar=MUD[0], note_en=", itself annexed", note_tr=", kendisi de muzâf"),
  MUDAF_ILAYH("الْمَغْرِبِ", "maghrib", punct="،"),
  KANA("وَكَانَ"),
  tok("أَمِيرَهُمْ", "amir", "noun", ["kana-wa-akhawatuha", "idafa-definiteness", "al-bariz-al-muttasil"],
      "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The FRONTED predicate of كَانَ, in nasb, annexed to «their» (the seat of jarr) — its fatha shows it is the predicate, though it comes first.",
      "Kâne'nin öne alınmış haberi, mansûb; «onların» zamirine muzâf, zamir mahallen mecrûr — öne geçse de fethası onun haber olduğunu gösterir.",
      segments=[seg("أَمِيرَ", "amir", "noun"), seg("هُمْ", "pron-3mp", "pron")]),
  JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («onun üzerine»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِأَمِيرَ", note_en="; the phrase hangs on «governor»", note_tr="; câr-mecrûr «emîr»e müteallık"),
  MUSA_ISMK(),
  IBN("مُوسَى", "Mūsā", "Mûsâ"),
  NUSAYR_MI(punct=".")]})
S1.append({"id": "s2", "translation": {"en": "And Ṭāriq ibn Ziyād was one of his commanders.", "tr": "Târık b. Ziyâd da onun kumandanlarından biriydi."},
 "tokens": [KANA("وَكَانَ"),
  PH(ISMK("طَارِقُ", "tariq-name", "propn", note_ar=" — عَلَمٌ مَصْرُوفٌ، وَحُذِفَ تَنْوِينُهُ لِأَنَّهُ وُصِفَ بِابْنٍ مُضَافٍ إِلَى عَلَمٍ",
      note_en=" — a name that keeps its tanwin elsewhere, but drops it here because «son of» + a name describes it", note_tr=" — munsarif isim; alem'e muzâf «ibn» ile vasıflandığı için tenvini düştü"), "tariq-ibn-ziyad", 3),
  IBN("طَارِقٍ", "Ṭāriq", "Târık"),
  MUDAF_ILAYH("زِيَادٍ", "ziyad-name", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2]),
  KHK("قَائِدًا", "qaid-leader"),
  MIN(role=("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِقَائِدٍ", "; the phrase hangs on an omitted na't of «a commander»", "; câr-mecrûr «kumandan»ın mahzûf na'tına müteallık")),
  ENC_NOUN("قَادَتِهِ", "qaid-leader", "هِ", "majr", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِقَائِدٍ", note_en=" — the broken plural of «commander»", note_tr=" — kâidin cem-i teksîri", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "Beyond the sea lay wide lands called al-Andalus.", "tr": "Denizin ötesinde Endülüs denilen geniş bir ülke vardı."},
 "tokens": [KANA("وَكَانَتْ", fem=True),
  tok("وَرَاءَ", "waraa", "noun", ["maful-fih", "idafa-definiteness", "kana-wa-akhawatuha"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ مُقَدَّمٌ.",
      "An adverb of place «beyond», in nasb and annexed — the phrase is the FRONTED predicate of كَانَ, in the seat of nasb.",
      "Mekân zarfı «ötesinde», mansûb, muzâf — şibh-i cümle, kâne'nin öne alınmış haberi, mahallen mansûb."),
  MUDAF_ILAYH("الْبَحْرِ", "bahr"),
  ISMK("بِلَادٌ", "bilad", extra=["jam-taksir"], muakhkhar=True, note_ar=" — جَمْعُ بَلَدٍ", note_en=" — the plural of «country»", note_tr=" — beledin cemi"),
  NAAT("وَاسِعَةٌ", "wasi-wide", "raf", ["ism-fail"], note_ar=" — جَمْعُ مَا لَا يَعْقِلُ يُوصَفُ بِالْمُفْرَدِ الْمُؤَنَّثِ", note_en=" — a plural of things is described by a feminine singular", note_tr=" — akılsız varlıkların cemi müfred müennesle vasıflanır"),
  tok("تُسَمَّى", "samma", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs", "naqis-verbs", "mafulayn", "jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ يَعُودُ عَلَى بِلَادٍ، وَهُوَ الْعَائِدُ الرَّابِطُ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِبِلَادٍ.",
      "Present verb in the passive, in raf' by a damma estimated on the alif; its deputy doer is the hidden «it» (the lands), the resumptive pronoun — the clause is a second na't of «lands», in the seat of raf'.",
      "Meçhul muzâri, elif üzerinde takdîrî damme ile merfû; nâib-i fâil «ülke»ye dönen gizli zamir «o» — bağlayıcı âid zamirdir; cümle «ülke»nin ikinci na'tı, mahallen merfû."),
  tok("الْأَنْدَلُسَ", "andalus", "propn", ["maful-bihi", "mafulayn"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — سَمَّى يَنْصِبُ مَفْعُولَيْنِ، فَلَمَّا بُنِيَ لِلْمَجْهُولِ نَابَ الْأَوَّلُ عَنِ الْفَاعِلِ وَبَقِيَ الثَّانِي مَنْصُوبًا.",
      "The second object, in nasb — سَمَّى takes two objects; in the passive the first becomes the deputy doer and the second stays in nasb.",
      "İkinci mef'ûlün bih, mansûb — sammâ iki mef'ûl alır; meçhul olunca birincisi nâib-i fâil olur, ikincisi mansûb kalır.", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "Its king at that time was a man named Ludhrīq (Roderic).", "tr": "O vakit oranın kralı, adı Lüzrîk (Rodrigo) olan bir adamdı."},
 "tokens": [KANA("وَكَانَ"),
  ENC_NOUN("مَلِكُهَا", "malik-king", "هَا", "ismk"),
  FI(),
  DHALIKA_SEAT("جَرٍّ", "jarr", "mecrûr"),
  tok("الْوَقْتِ", "waqt", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ بِالْكَسْرَةِ.",
      "A badal of the demonstrative, in jarr like it.", "İşaret isminden bedel, mecrûr."),
  KHK("رَجُلًا", "rajul"),
  ENC_NOUN("اسْمُهُ", "ism-name", "هُ", "mubtada", extra=["jumla-sifa"], note_ar=" — وَالْهَاءُ الْعَائِدُ الَّذِي يَرْبِطُ جُمْلَةَ النَّعْتِ بِرَجُلٍ", note_en="; «his» is the resumptive pronoun that ties the na't clause to «a man»", note_tr="; «hû» na't cümlesini «adam»a bağlayan âid zamirdir"),
  tok("لُذْرِيقُ", "ludhriq", "propn", ["mubtada-khabar", "mamnu-min-sarf", "jumla-sifa"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ " + LUDH_N[0] + " — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِرَجُلٍ.",
      "The predicate (khabar), in raf'" + LUDH_N[1] + " — the nominal clause is a na't of «a man», in the seat of nasb.",
      "Haber, merfû," + LUDH_N[2] + " — isim cümlesi «adam»ın na'tı, mahallen mansûb.", punct=".")]})
S1.append({"id": "s5", "translation": {"en": "Between it and the Maghrib there lay nothing but a strait of the sea.", "tr": "Onunla Mağrib arasında denizden bir boğazdan başka bir şey yoktu."},
 "tokens": [WA_LAM(),
  tok("يَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ: يَكُونْ) — يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
      "The defective present verb in jazm by لَمْ, its sign the sukun; the waw of يَكُونْ dropped because two sukuns met — it raises its noun and puts its predicate in nasb.",
      "Lem ile meczûm nâkıs muzâri, alâmeti sükûn; iki sâkin buluştuğu için yekûn'un vâvı düştü — ismini ref, haberini nasb eder."),
  tok("بَيْنَهَا", "bayna", "noun", ["maful-fih", "idafa-definiteness", "al-bariz-al-muttasil", "kana-wa-akhawatuha"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ نَصْبٍ خَبَرُ يَكُنْ مُقَدَّمٌ.",
      "An adverb of place «between», in nasb and annexed to «it» (the seat of jarr) — the phrase is the FRONTED predicate of يَكُنْ, in the seat of nasb.",
      "Mekân zarfı «arasında», mansûb, «o» zamirine muzâf — şibh-i cümle, yekün'ün öne alınmış haberi, mahallen mansûb.",
      segments=[seg("بَيْنَ", "bayna", "noun"), seg("هَا", "pron-3fs", "pron")]),
  ATF("وَبَيْنَ", "bayna", case="nasb", extra=["maful-fih", "idafa-definiteness"], note_ar=MUD[0] + " — وَتُكَرَّرُ بَيْنَ مَعَ الضَّمِيرِ", note_en=", annexed — بَيْنَ is repeated when its first term is a pronoun", note_tr=", muzâf — ilk terimi zamir olunca beyne tekrarlanır"),
  MUDAF_ILAYH("الْمَغْرِبِ", "maghrib"),
  ILLA(),
  tok("مَضِيقٌ", "madiq", "noun", ["kana-wa-akhawatuha", "istithna-mufarragh"],
      "اسْمُ يَكُنْ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالِاسْتِثْنَاءُ مُفَرَّغٌ، فَأَخَذَ إِعْرَابَهُ مِنْ مَوْقِعِهِ.",
      "The noun of يَكُنْ, placed after its predicate, in raf' — the exception is emptied, so it takes the case of its own seat.",
      "Yekün'ün ismi (haberinden sonraya bırakılmış), merfû — istisnâ müferrağdır; i'râbını kendi mevkiinden alır."),
  MINA_BAYAN(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِمَضِيقٍ", "; the phrase hangs on an omitted na't of «a strait»", "; câr-mecrûr «boğaz»ın mahzûf na'tına müteallık"), kind=TABID),
  MAJR("الْبَحْرِ", "bahr", punct=".")]})

# ---- Chapter 2 — عُبُورُ الْمَضِيقِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "In the year ninety-two of the Hijra, Mūsā sent Ṭāriq to al-Andalus with an army of Berbers and Arabs.",
                                       "tr": "Hicretin doksan ikinci yılında Mûsâ, Târık'ı Berberîler ve Araplardan oluşan bir orduyla Endülüs'e gönderdi."},
 "tokens": [FI(),
  MAJR("سَنَةِ", "sana", note_ar=MUD[0] + " إِلَى الْعَدَدِ بَعْدَهُ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِأَرْسَلَ", note_en=" — annexed to the number after it; the phrase hangs on «sent»", note_tr=", sonraki sayıya muzâf — câr-mecrûr «gönderdi»ye müteallık"),
  MUDAF_ILAYH("اثْنَتَيْنِ", "ithnatan", extra=["al-muthanna", "asma-al-adad-fil-kafiya"], sign="بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِالْمُثَنَّى",
      note_ar=" — وَجَاءَ مُؤَنَّثًا لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ: الْوَاحِدُ وَالِاثْنَانِ يُوَافِقَانِ الْمَعْدُودَ",
      note_en=" — by the ya, as it declines like a dual; feminine because the thing counted, «year», is feminine: one and two agree with what they count",
      note_tr=" — tesniyeye mülhak olduğu için yâ ile; ma'dûd «sene» müennes olduğu için müennes geldi: bir ve iki ma'dûda uyar"),
  TISIN(),
  LI_AL("لِلْهِجْرَةِ", "hijra", "الْهِجْرَةِ", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنْ سَنَةٍ، أَيْ: مَحْسُوبَةً مِنَ الْهِجْرَةِ",
      note_en=" — the phrase hangs on an omitted hal: the year as counted from the Hijra, «AH»", note_tr=" — câr-mecrûr mahzûf bir hâle müteallık: hicretten sayılan yıl, «hicrî»"),
  MADI("أَرْسَلَ", "arsala", ["form-iv-verbs"]),
  MUSA_F(phrase=False),
  MAFUL("طَارِقًا", "tariq-name", "propn", note_ar=MUNSARIF[0], note_en=MUNSARIF[1], note_tr=MUNSARIF[2]),
  ILA(),
  ANDALUS_J(),
  PREP("فِي", "fi", "، بِمَعْنَى «مَعَ» (لِلْمُصَاحَبَةِ)", " — here «with, at the head of» (accompaniment)", " (musâhabet: «ile»)", gloss_tr="«-de»"),
  MAJR("جَيْشٍ", "jaysh", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ مِنْ طَارِقٍ", note_en=" — the phrase hangs on an omitted hal of «Ṭāriq»", note_tr=" — câr-mecrûr «Târık»tan mahzûf bir hâle müteallık"),
  MINA_BAYAN(("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِجَيْشٍ", "; the phrase hangs on an omitted na't of «an army»", "; câr-mecrûr «ordu»nun mahzûf na'tına müteallık")),
  MAJR("الْبَرْبَرِ", "barbar"),
  ATF("وَالْعَرَبِ", "arab", case="jarr", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "Most of his soldiers were Berbers.", "tr": "Askerlerinin çoğu Berberîlerdendi."},
 "tokens": [KANA("وَكَانَ"),
  ISMK("أَكْثَرُ", "akthar", extra=["ism-tafdil", "idafa-definiteness"], note_ar=MUD[0] + " — اسْمُ تَفْضِيلٍ", note_en=MUD[1] + " — an elative, «most of»", note_tr=MUD[2] + " — ism-i tafdîl, «çoğu»"),
  ENC_NOUN("جُنُودِهِ", "jund", "هِ", "mudaf", extra=["jam-taksir"], note_ar=" — جَمْعُ جُنْدٍ", note_en=" — the plural of «troops»", note_tr=" — cündün cemi"),
  MINA(),
  MAJR("الْبَرْبَرِ", "barbar", note_ar=KH_KANA_J[0], note_en=KH_KANA_J[1], note_tr=KH_KANA_J[2], punct=".")]})
S2.append({"id": "s3", "translation": {"en": "So Ṭāriq crossed the strait with his army, in ships.", "tr": "Târık ordusuyla birlikte gemilerle boğazı geçti."},
 "tokens": [MADI("فَعَبَرَ", "abara", ["maful-bihi"]),
  TARIQ_F(),
  BI_NOUN("بِجَيْشِهِ", "jaysh", "جَيْشِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of accompaniment, «with»", note_tr=" — bâ musâhabet içindir, «ile»"),
  MAFUL("الْمَضِيقَ", "madiq"),
  FI(),
  MAJR("السُّفُنِ", "safina", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِسَفِينَةٍ", note_en=" — the broken plural of «ship»", note_tr=" — sefînenin cem-i teksîri", punct=".")]})
S2.append({"id": "s4", "translation": {"en": "And the Muslims landed by a mountain on the coast of al-Andalus.", "tr": "Müslümanlar Endülüs sahilinde bir dağın yanına indiler."},
 "tokens": [MADI("وَنَزَلَ", "nazala"),
  MUSLIMUN_F(),
  INDA(),
  MUDAF_ILAYH("جَبَلٍ", "jabal"),
  ALA(),
  MAJR("سَاحِلِ", "sahil", note_ar=MUD[0] + " — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِجَبَلٍ", note_en=", annexed — the phrase hangs on an omitted na't of «a mountain»", note_tr=", muzâf — câr-mecrûr «dağ»ın mahzûf na'tına müteallık"),
  ANDALUS_MI(punct=".")]})
S2.append({"id": "s5", "translation": {"en": "So the mountain by which they landed was named Jabal Ṭāriq, «Ṭāriq's Mountain».",
                                       "tr": "Bu yüzden yanına indikleri dağa Cebel-i Târık («Târık Dağı») adı verildi."},
 "tokens": [tok("فَسُمِّيَ", "samma", "verb", ["naib-al-fail", "al-majhul-fil-kafiya", "form-ii-verbs", "naqis-verbs", "mafulayn"],
      FA_AR + "سُمِّيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَبْنِيٌّ عَلَى الْفَتْحِ — وَسَمَّى يَنْصِبُ مَفْعُولَيْنِ، فَلَمَّا بُنِيَ لِلْمَجْهُولِ رُفِعَ أَوَّلُهُمَا نَائِبًا عَنِ الْفَاعِلِ وَبَقِيَ الثَّانِي مَنْصُوبًا.",
      "The fa conjoins; «was named» is a past verb in the passive, built on fatha — سَمَّى takes two objects, and in the passive the first is raised as deputy doer while the second stays in nasb.",
      "«bunun üzerine» + meçhul mâzî, fetha üzere mebnî — sammâ iki mef'ûl alır; meçhul olunca birincisi nâib-i fâil olarak merfû olur, ikincisi mansûb kalır.",
      segments=[seg("فَ", "fa", "conj"), seg("سُمِّيَ", "samma", "verb")]),
  NAIB("الْجَبَلُ", "jabal"),
  ALLADHI_R("لْجَبَلِ", "the mountain", "dağ"),
  VERB_WAW("نَزَلُوا", "nazala", extra=["ism-mawsul"], note_ar=SILA[0], note_en=SILA[1], note_tr=SILA[2]),
  INDAHU_AID(),
  PH(tok("جَبَلَ", "jabal", "noun", ["maful-bihi", "mafulayn", "idafa-definiteness"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.",
      "The second object, in nasb, annexed.", "İkinci mef'ûlün bih, mansûb, muzâf."), "jabal-tariq", 2),
  TARIQ_MI(punct=".")]})

# ---- Chapter 3 — لِقَاءُ الْجَيْشَيْنِ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "When the news of them reached Ludhrīq, he gathered his troops and marched against them, fearing for his kingdom.",
                                       "tr": "Onların haberi Lüzrîk'e ulaşınca, mülkü için korkarak askerlerini topladı ve onlara doğru yürüdü."},
 "tokens": [LAMMA2("وَلَمَّا"),
  MADI("بَلَغَ", "balagha", note_ar="، وَالْفَاعِلُ «خَبَرُهُمْ» مُؤَخَّرٌ عَنِ الْمَفْعُولِ" + LAMMA_CL[0], note_en="; its doer «their news» comes after the object" + LAMMA_CL[1], note_tr="; fâili «haberleri» mef'ûlden sonra gelir" + LAMMA_CL[2]),
  tok("لُذْرِيقَ", "ludhriq", "propn", ["maful-bihi", "mamnu-min-sarf"],
      "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِالْفَتْحَةِ " + LUDH_N[0] + ".",
      "The direct object, placed before the doer, in nasb" + LUDH_N[1] + ".",
      "Mef'ûlün bih, fâilden önce gelmiş, mansûb," + LUDH_N[2] + "."),
  ENC_NOUN("خَبَرُهُمْ", "khabar", "هُمْ", "fail", note_ar=" — مُؤَخَّرٌ", note_en=" — placed after the object", note_tr=" — mef'ûlden sonraya bırakılmış", punct="،"),
  MADI("جَمَعَ", "jamaa-gather", ["maful-bihi"], hidden=True, note_ar=JAWAB_LAMMA[0], note_en=JAWAB_LAMMA[1], note_tr=JAWAB_LAMMA[2]),
  ENC_NOUN("جُنُودَهُ", "jund", "هُ", "maful", extra=["jam-taksir"]),
  MADI("وَسَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  JARR_PRON("إِلَيْهِمْ", "ila", "إِلَيْ", "هِمْ", " («onlara»)"),
  tok("خَوْفًا", "khawf", "noun", ["maful-lah", "al-maful-fih-wal-maful-lah", "masdar"],
      "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، وَيُشَارِكُهُ فِي الْوَقْتِ وَالْفَاعِلِ.",
      "The object of purpose (maf'ul li-ajlih), in nasb — a masdar of the heart that gives the reason for the act, sharing its time and its doer: «out of fear».",
      "Mef'ûlün lieclih, mansûb — fiilin sebebini bildiren kalbî masdar; zamanı ve fâili fiille ortaktır: «korkusundan»."),
  PREP("عَلَى", "ala", "، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِالْمَصْدَرِ «خَوْفًا»", " «for»; the phrase hangs on the masdar «fear»", "; câr-mecrûr «korku» masdarına müteallık", gloss_tr="«için»"),
  ENC_NOUN("مُلْكِهِ", "mulk", "هِ", "majr", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "He meant to drive them out of his land.", "tr": "Onları ülkesinden çıkarmak istedi."},
 "tokens": [MADI("وَأَرَادَ", "arada", ["hollow-verbs", "form-iv-verbs"], hidden=True),
  AN_MAFUL(),
  MANSUB_AN("يُخْرِجَهُمْ", "akhraja", ["form-iv-verbs"], enc="هُمْ"),
  MIN(),
  ENC_NOUN("بِلَادِهِ", "bilad", "هِ", "majr", extra=["jam-taksir"], punct=".")]})
S3.append({"id": "s3", "translation": {"en": "The two armies met, the Muslims being fewer in number than their enemy.", "tr": "İki ordu karşılaştı; Müslümanlar ise sayıca düşmanlarından azdı."},
 "tokens": [tok("فَالْتَقَى", "iltaqa", "verb", ["form-viii-verbs", "naqis-verbs"],
      FA_AR + "الْتَقَى فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ بَعْدَهُ.",
      "The fa conjoins; «met» is a past verb (Form VIII) built on a fatha estimated on the alif; its doer follows.",
      "«bunun üzerine» + iltekâ (ifti'âl): elif üzerindeki takdîrî fetha ile mebnî mâzî; fâili sonra gelir.",
      segments=[seg("فَ", "fa", "conj"), seg("الْتَقَى", "iltaqa", "verb")]),
  FAIL("الْجَيْشَانِ", "jaysh", extra=["al-muthanna"], sign="بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَالنُّونُ عِوَضٌ عَنِ التَّنْوِينِ فِي الْمُفْرَدِ",
      note_en=" — by the alif, being a dual; the nun stands for the tanwin of the singular", note_tr=" — tesniye olduğu için elif ile; nûn müfreddeki tenvinin bedelidir", punct="،"),
  tok("وَالْمُسْلِمُونَ", "muslim", "noun", ["mubtada-khabar", "al-hal-jumla-wa-rabituha", "jam-mudhakkar-salim"],
      "الْوَاوُ حَالِيَّةٌ، وَالْمُسْلِمُونَ مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw of the hal; «the Muslims» is the mubtada, in raf' by the waw (a sound masculine plural) — the nominal clause fills the seat of nasb as a hal.",
      "Hâl vâvı; «Müslümanlar» mübtedâ, cem-i müzekker sâlim olduğu için vâv ile merfû — isim cümlesi hâl olarak mahallen mansûb.",
      segments=[seg("وَ", "wa", "conj"), seg("الْمُسْلِمُونَ", "muslim", "noun")]),
  tok("أَقَلُّ", "aqall", "noun", ["mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ — اسْمُ تَفْضِيلٍ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ (أَصْلُهُ: أَقْلَلُ، فَأُدْغِمَتِ اللَّامُ فِي اللَّامِ).",
      "The predicate (khabar), in raf' without tanwin — an elative, barred from tanwin as an adjective on the أَفْعَل pattern (from أَقْلَلُ, the two lams merged).",
      "Haber, tenvinsiz merfû — vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif ism-i tafdîl (aslı akleli; iki lâm idgâm edildi)."),
  tok("عَدَدًا", "adad", "noun", ["tamyiz", "al-tamyiz-wa-ahkamuh"],
      "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ — يُبَيِّنُ الْجِهَةَ الَّتِي فِيهَا الْقِلَّةُ بَعْدَ اسْمِ التَّفْضِيلِ.",
      "A specifier (tamyiz), in nasb — after the elative it names the respect in which they were fewer: «in number».",
      "Temyîz, mansûb — ism-i tafdîlden sonra azlığın hangi yönden olduğunu belirtir: «sayıca»."),
  MIN(role=("، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِأَقَلَّ", "; the phrase hangs on «fewer» («than»)", "; câr-mecrûr «daha az»a müteallık («-den»)")),
  ENC_NOUN("عَدُوِّهِمْ", "aduww", "هِمْ", "majr", note_ar=" — وَالْعَدُوُّ يَقَعُ عَلَى الْوَاحِدِ وَالْجَمَاعَةِ", note_en=" — عَدُوّ may stand for one enemy or a whole host", note_tr=" — adüv tek düşman için de topluluk için de kullanılır", punct=".")]})
S3.append({"id": "s4", "translation": {"en": "The Muslims fought fiercely and held firm with great endurance.", "tr": "Müslümanlar şiddetle savaştılar ve büyük bir sabır gösterdiler."},
 "tokens": [MADI("فَقَاتَلَ", "qatala-fight", ["form-iii-verbs"]),
  MUSLIMUN_F(),
  MUTLAQ_NAW("قِتَالًا", "qital"),
  NAAT("شَدِيدًا", "shadid", "nasb", punct="،"),
  VERB_WAW("وَصَبَرُوا", "sabara"),
  MUTLAQ_NAW("صَبْرًا", "sabr"),
  NAAT("عَظِيمًا", "azim", "nasb", punct=".")]})
S3.append({"id": "s5", "translation": {"en": "Then God gave them victory: Ludhrīq was routed and his army scattered.", "tr": "Sonra Allah onlara zafer verdi; Lüzrîk bozguna uğradı ve ordusu dağıldı."},
 "tokens": [THUMMA(),
  ENC_MADI("نَصَرَهُمُ", "nasara", "هُمُ", note_ar=" — وَحُرِّكَتِ الْمِيمُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ بَعْدَهُ", note_en="; the mim is voweled with damma before the following ال, and the doer follows", note_tr="; mîm iki sâkin karşılaştığı için damme ile harekelendi; fâili sonra gelir"),
  ALLAH_F(punct="،"),
  MAJHUL("فَهُزِمَ", "hazama"),
  tok("لُذْرِيقُ", "ludhriq", "propn", ["naib-al-fail", "mamnu-min-sarf"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِالضَّمَّةِ " + LUDH_N[0] + ".",
      "The deputy doer (na'ib al-fa'il), in raf'" + LUDH_N[1] + ".",
      "Nâib-i fâil, merfû," + LUDH_N[2] + "."),
  MADI("وَتَفَرَّقَ", "tafarraqa", ["form-v-verbs"]),
  ENC_NOUN("جَيْشُهُ", "jaysh", "هُ", "fail", punct=".")]})
S3.append({"id": "s6", "translation": {"en": "That was in the same year.", "tr": "Bu da aynı yıl oldu."},
 "tokens": [KANA("وَكَانَ"),
  DHALIKA_SEAT("رَفْعٍ اسْمُ كَانَ", "raf' as the noun of كَانَ", "merfû — kâne'nin ismi", extra=["kana-wa-akhawatuha"]),
  FI(),
  MAJR("السَّنَةِ", "sana", note_ar=KH_KANA_J[0], note_en=KH_KANA_J[1], note_tr=KH_KANA_J[2]),
  tok("نَفْسِهَا", "nafs", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — يُؤَكِّدُ السَّنَةَ، وَيَعُودُ عَلَيْهَا الضَّمِيرُ.",
      "A tawkid of meaning «itself, the same», in jarr like the word it strengthens; annexed to «it», which returns to «the year» (the seat of jarr).",
      "Ma'nevî te'kîd «kendisi, aynı», pekiştirdiği kelime gibi mecrûr; «senenin» zamirine muzâf, zamir mahallen mecrûr.", punct=".",
      segments=[seg("نَفْسِ", "nafs", "noun"), seg("هَا", "pron-3fs", "pron")])]})
S3.append({"id": "s7", "translation": {"en": "This victory was a gate through which the Muslims entered the lands of al-Andalus.", "tr": "Bu zafer, Müslümanların Endülüs topraklarına girdiği bir kapı oldu."},
 "tokens": [KANA("وَكَانَ"),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "kana-wa-akhawatuha"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.",
      "A demonstrative, built on sukun, in the seat of raf' as the noun of كَانَ.", "İşaret ismi, sükûn üzere mebnî; kâne'nin ismi olarak mahallen merfû."),
  tok("النَّصْرُ", "nasr", "noun", ["badal", "asma-al-ishara"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَرْفُوعٌ بِالضَّمَّةِ.", "A badal of the demonstrative, in raf' like it.", "İşaret isminden bedel, merfû."),
  KHK("بَابًا", "bab"),
  MADI("دَخَلَ", "dakhala", ["jumla-sifa"], note_ar="، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِبَابٍ", note_en="; its doer follows — the clause is a na't of «a gate», in the seat of nasb", note_tr="; fâili sonra gelir — cümle «kapı»nın na'tı, mahallen mansûb"),
  JARR_PRON("مِنْهُ", "min", "مِنْ", "هُ", " («ondan»)", extra=["jumla-sifa"], note_ar=" — وَالْهَاءُ الْعَائِدُ الَّذِي يَرْبِطُ جُمْلَةَ النَّعْتِ بِبَابٍ", note_en="; «it» is the resumptive pronoun that ties the na't clause to «a gate»", note_tr="; «hû» na't cümlesini «kapı»ya bağlayan âid zamirdir"),
  MUSLIMUN_F(),
  ILA(),
  MAJR("بِلَادِ", "bilad", extra=["jam-taksir"], note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  ANDALUS_MI(punct=".")]})

# ---- Chapter 4 — فَتْحُ الْمُدُنِ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "Then Ṭāriq marched with his army through the land, and many cities were opened to him.", "tr": "Sonra Târık ordusuyla ülkenin içlerine yürüdü ve birçok şehir ona açıldı."},
 "tokens": [THUMMA(),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"]),
  TARIQ_F(),
  BI_NOUN("بِجَيْشِهِ", "jaysh", "جَيْشِهِ", enc="هِ", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of accompaniment, «with»", note_tr=" — bâ musâhabet içindir, «ile»"),
  FI(),
  MAJR("الْبِلَادِ", "bilad", extra=["jam-taksir"], punct="،"),
  MAJHUL("فَفُتِحَتْ", "fataha", fem=True),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"),
  NAIB("مُدُنٌ", "madina", extra=["jam-taksir"], note_ar=" — جَمْعُ تَكْسِيرٍ لِمَدِينَةٍ، فَأُنِّثَ فِعْلُهُ", note_en=" — a broken plural of «city», so its verb is feminine", note_tr=" — medînenin cem-i teksîri; bu yüzden fiili müennes geldi"),
  NAAT("كَثِيرَةٌ", "kathir", "raf", punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He kept on marching until he reached the capital of Ludhrīq's kingdom.", "tr": "Lüzrîk'in krallığının başşehrine ulaşıncaya kadar yürümeyi sürdürdü."},
 "tokens": [WA_LAM(),
  tok("يَزَلْ", "zala", "verb", ["kana-wa-akhawatuha", "nawasib-wa-jawazim-al-mudari", "hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتِ الْأَلِفُ لِالْتِقَاءِ السَّاكِنَيْنِ (أَصْلُهُ: يَزَالْ)، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ.",
      "A defective present verb, a sister of كَانَ, in jazm by لَمْ, its sign the sukun; its alif dropped where two quiescents met (from يَزَالْ); its noun is the hidden «he» — with the negation it means «kept on».",
      "Kâne'nin kardeşlerinden nâkıs muzâri, lem ile meczûm, alâmeti sükûn; iki sâkin karşılaşınca elifi düştü (aslı yezâl); ismi gizli zamir «o» — nefiyle birlikte devamlılık bildirir."),
  MUDARI("يَسِيرُ", "sara-travel", ["hollow-verbs", "kana-wa-akhawatuha"], note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ يَزَلْ", note_en=" — the clause is the predicate of يَزَلْ, in the seat of nasb", note_tr=" — cümle yezel'in haberi, mahallen mansûb"),
  HATTA_IBT(),
  MADI("بَلَغَ", "balagha", hidden=True),
  MAFUL("عَاصِمَةَ", "asima", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  MUDAF_ILAYH("مُلْكِ", "mulk", note_ar=MUD[0], note_en=", itself annexed", note_tr=", kendisi de muzâf"),
  tok("لُذْرِيقَ", "ludhriq", "propn", ["idafa-definiteness", "mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ، لِأَنَّهُ عَلَمٌ أَعْجَمِيٌّ مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "The second term of the idafa, in jarr — its sign the fatha standing in for the kasra, because it is a foreign proper name barred from tanwin.",
      "Muzâfun ileyh, mecrûr — yabancı özel isim olarak gayr-i munsarif olduğu için kesre yerine fetha ile.", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "He entered it, most of its people having already left it.", "tr": "Halkının çoğu oradan çıkmış olduğu hâlde oraya girdi."},
 "tokens": [ENC_MADI("فَدَخَلَهَا", "dakhala", "هَا", hidden=True),
  WA_QAD(),
  MADI("خَرَجَ", "kharaja", note_ar="، وَالْفَاعِلُ بَعْدَهُ", note_en="; its doer follows", note_tr="; fâili sonra gelir"),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («oradan»)"),
  FAIL("أَكْثَرُ", "akthar", extra=["ism-tafdil", "idafa-definiteness"], note_ar=MUD[0] + " — اسْمُ تَفْضِيلٍ", note_en=MUD[1] + " — an elative, «most of»", note_tr=MUD[2] + " — ism-i tafdîl, «çoğu»"),
  ENC_NOUN("أَهْلِهَا", "ahl", "هَا", "mudaf", punct=".")]})
S4.append({"id": "s4", "translation": {"en": "In the year ninety-three, Mūsā ibn Nuṣayr crossed the sea with another army.", "tr": "Doksan üç yılında Mûsâ b. Nusayr başka bir orduyla denizi geçti."},
 "tokens": [tok("وَفِي", "fi", "prep", ["huruf-jarr"], WA_AR + "فِي حَرْفُ جَرٍّ.", "The waw conjoins; فِي is a jarr letter «in».", "«ve» + fî «-de»: cer harfi.",
      segments=[seg("وَ", "wa", "conj"), seg("فِي", "fi", "prep")]),
  MAJR("سَنَةِ", "sana", note_ar=MUD[0] + " إِلَى الْعَدَدِ بَعْدَهُ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِعَبَرَ", note_en=" — annexed to the number after it; the phrase hangs on «crossed»", note_tr=", sonraki sayıya muzâf — câr-mecrûr «geçti»ye müteallık"),
  MUDAF_ILAYH("ثَلَاثٍ", "thalath", extra=["asma-al-adad-fil-kafiya"],
      note_ar=" — وَحُذِفَتْ مِنْهُ التَّاءُ لِأَنَّ الْمَعْدُودَ «سَنَة» مُؤَنَّثٌ: الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى تِسْعَةٍ يُخَالِفُ مَعْدُودَهُ",
      note_en=" — without the ta, because the thing counted, «year», is feminine: three to nine take the opposite gender of what they count",
      note_tr=" — ma'dûd «sene» müennes olduğu için tâsız: üçten dokuza kadar sayılar ma'dûduna cinsçe zıt gelir"),
  TISIN(),
  MADI("عَبَرَ", "abara", ["maful-bihi"]),
  MUSA_F(),
  IBN("مُوسَى", "Mūsā", "Mûsâ"),
  NUSAYR_MI(),
  MAFUL("الْبَحْرَ", "bahr"),
  BI_NOUN("بِجَيْشٍ", "jaysh", "جَيْشٍ", note_ar=" — وَالْبَاءُ لِلْمُصَاحَبَةِ", note_en=" — the ba of accompaniment, «with»", note_tr=" — bâ musâhabet içindir, «ile»"),
  tok("آخَرَ", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf"],
      "نَعْتٌ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ، لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ أَفْعَلَ.",
      "An adjective in jarr, its sign the fatha standing in for the kasra — آخَر «another» is barred from tanwin as an adjective on the أَفْعَل pattern.",
      "Na't, mecrûr; kesre yerine fetha ile — âhar vasfiyet ve ef'al vezni sebebiyle gayr-i munsarif.", punct=".")]})
S4.append({"id": "s5", "translation": {"en": "He conquered other cities, then marched on so as to join Ṭāriq.", "tr": "Başka şehirler fethetti, sonra Târık'a yetişmek için yürüdü."},
 "tokens": [MADI("فَفَتَحَ", "fataha", ["maful-bihi"], hidden=True),
  MAFUL("مُدُنًا", "madina", extra=["jam-taksir"]),
  tok("أُخْرَى", "akhar", "noun", ["naat-sifa", "mamnu-min-sarf", "ism-maqsur-manqus"],
      "نَعْتٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مُؤَنَّثُ آخَرَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَقْصُورَةِ؛ وَجَمْعُ مَا لَا يَعْقِلُ يُوصَفُ بِالْمُفْرَدِ الْمُؤَنَّثِ.",
      "An adjective in nasb by a fatha estimated on the alif — the feminine of آخَر «another», barred from tanwin by its shortened feminine alif; a plural of things is described by a feminine singular.",
      "Na't, elif üzerinde takdîrî fetha ile mansûb — âharın müennesi; maksûr te'nîs elifi sebebiyle gayr-i munsarif; akılsız varlıkların cemi müfred müennesle vasıflanır.", punct="،"),
  THUMMA(),
  MADI("سَارَ", "sara-travel", ["hollow-verbs"], hidden=True),
  tok("حَتَّى", "hatta", "prep", ["huruf-jarr", "nawasib-wa-jawazim-al-mudari", "ila-hatta-fi-wal-ba-fil-kafiya"],
      "حَرْفُ جَرٍّ بِمَعْنَى «كَيْ» لِلتَّعْلِيلِ، وَالْفِعْلُ بَعْدَهُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا، وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِحَتَّى.",
      "حَتَّى here means «so that» (purpose): a jarr letter after which an unspoken أَنْ must put the verb in nasb; the masdar so built is in jarr by حَتَّى.",
      "Hattâ burada «-sin diye» (ta'lîl) anlamında cer harfi; sonraki fiil vücûben gizli en ile mansûb, müevvel masdar hattâ ile mecrûr."),
  tok("يَلْحَقَ", "lahiqa", "verb", ["nawasib-wa-jawazim-al-mudari"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ حَتَّى وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "Present verb in nasb by the unspoken أَنْ after حَتَّى, its sign the fatha; the doer is a hidden pronoun «he».",
      "Hattâ'dan sonra gizli en ile mansûb muzâri, alâmeti fetha; fâil gizli zamir «o»."),
  BI_NOUN("بِطَارِقٍ", "tariq-name", "طَارِقٍ", pos="propn", note_ar=" — عَلَمٌ مَصْرُوفٌ؛ وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِيَلْحَقَ", note_en=" — a name that keeps its tanwin; the phrase hangs on «join»", note_tr=" — munsarif isim; câr-mecrûr «yetişsin»e müteallık", punct=".")]})
S4.append({"id": "s6", "translation": {"en": "When the two met, the two armies became a single army.", "tr": "İkisi buluşunca iki ordu tek bir ordu oldu."},
 "tokens": [LAMMA2("فَلَمَّا"),
  tok("الْتَقَيَا", "iltaqa", "verb", ["form-viii-verbs", "naqis-verbs", "al-muthanna", "fail", "al-bariz-al-muttasil"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَأَلِفُ الِاثْنَيْنِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ — وَرُدَّتْ أَلِفُ الْفِعْلِ إِلَى أَصْلِهَا الْيَاءِ (الْتَقَى ← الْتَقَيَا)" + LAMMA_CL[0] + ".",
      "Past verb (Form VIII) built on fatha; the alif of the two is its doer, in the seat of raf' — the verb's own alif returns to its original ya (الْتَقَى → الْتَقَيَا)" + LAMMA_CL[1] + ".",
      "İftiâl bâbından, fetha üzere mebnî mâzî; tesniye elifi fâil, mahallen merfû — fiilin elifi aslı olan yâ'ya döndü (iltekâ → iltekayâ)" + LAMMA_CL[2] + ".",
      segments=[seg("الْتَقَيَ", "iltaqa", "verb"), seg("ا", "pron-3d", "pron")], punct="،"),
  tok("صَارَ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
      "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ" + JAWAB_LAMMA[0] + ".",
      "صَارَ «became» is one of كَانَ's sisters: it raises its noun and puts its predicate in nasb" + JAWAB_LAMMA[1] + ".",
      "«oldu» — kâne'nin kardeşlerinden nâkıs fiil; ismini ref, haberini nasb eder" + JAWAB_LAMMA[2] + "."),
  tok("الْجَيْشَانِ", "jaysh", "noun", ["kana-wa-akhawatuha", "al-muthanna"], "اسْمُ صَارَ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.",
      "The noun of صَارَ, in raf' by the alif, being a dual.", "Sâra'nın ismi, tesniye olduğu için elif ile merfû."),
  tok("جَيْشًا", "jaysh", "noun", ["kana-wa-akhawatuha"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ.", "The predicate of صَارَ, in nasb.", "Sâra'nın haberi, mansûb."),
  NAAT("وَاحِدًا", "wahid", "nasb", punct=".")]})
S4.append({"id": "s7", "translation": {"en": "Together they conquered most of the lands of al-Andalus.", "tr": "İkisi birlikte Endülüs topraklarının çoğunu fethetti."},
 "tokens": [DUAL_MADI("وَفَتَحَا", "fataha", ["maful-bihi"]),
  HAL("مَعًا", "maan", note_ar="، وَصَاحِبُهُ أَلِفُ الِاثْنَيْنِ", note_en=" — its owner is the alif of the two: both at once", note_tr=" — sahibi tesniye elifidir: ikisi birlikte"),
  MAFUL("أَكْثَرَ", "akthar", extra=["ism-tafdil", "idafa-definiteness"], note_ar=MUD[0] + " — اسْمُ تَفْضِيلٍ", note_en=MUD[1] + " — an elative, «most of»", note_tr=MUD[2] + " — ism-i tafdîl, «çoğu»"),
  MUDAF_ILAYH("بِلَادِ", "bilad", extra=["jam-taksir"], note_ar=MUD[0], note_en=", itself annexed", note_tr=", kendisi de muzâf"),
  ANDALUS_MI(punct=".")]})

# ---- Chapter 5 — بَعْدَ الْفَتْحِ ----
S5 = []
S5.append({"id": "s1", "translation": {"en": "Islam remained in al-Andalus for many centuries.", "tr": "İslâm, Endülüs'te uzun asırlar boyunca kaldı."},
 "tokens": [MADI("وَبَقِيَ", "baqiya"),
  FAIL("الْإِسْلَامُ", "islam"),
  FI(),
  ANDALUS_J(),
  ZARF("قُرُونًا", "qarn", mudaf=False, extra=["jam-taksir"], note_ar=" — جَمْعُ قَرْنٍ", note_en=" — the plural of «age, century»", note_tr=" — karnın cemi", **ZAMAN),
  NAAT("كَثِيرَةً", "kathir", "nasb", punct=".")]})
S5.append({"id": "s2", "translation": {"en": "Mosques were built in it, and scholars grew many there.", "tr": "Orada camiler yapıldı ve âlimler çoğaldı."},
 "tokens": [MAJHUL("وَبُنِيَتْ", "bana", ["naqis-verbs"], fem=True),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («orada»)"),
  NAIB("الْمَسَاجِدُ", "masjid", extra=["jam-taksir", "mamnu-min-sarf"], note_ar=" — جَمْعُ مَسْجِدٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ، وَهُوَ جَمْعُ تَكْسِيرٍ فَأُنِّثَ فِعْلُهُ", note_en=" — the plural of «mosque» on the furthest-plural pattern; a broken plural, so its verb is feminine", note_tr=" — mescidin müntehe'l-cumû' vezninde cemi; cem-i teksîr olduğu için fiili müennes geldi", punct="،"),
  MADI("وَكَثُرَ", "kathura"),
  JARR_PRON("فِيهَا", "fi", "فِي", "هَا", " («orada»)"),
  FAIL("الْعُلَمَاءُ", "alim-scholar", extra=["jam-taksir"], note_ar=" — جَمْعُ عَالِمٍ", note_en=" — the plural of «scholar»", note_tr=" — âlimin cemi", punct=".")]})
S5.append({"id": "s3", "translation": {"en": "As for the mountain by which Ṭāriq landed, it is known by his name to this day.", "tr": "Târık'ın yanına indiği dağa gelince, o bugüne kadar onun adıyla bilinmektedir."},
 "tokens": [tok("وَأَمَّا", "amma-tafsil", "part", ["amma-tafsiliyya"],
      WA_ISTINAF[0] + "أَمَّا حَرْفُ شَرْطٍ وَتَفْصِيلٍ وَتَوْكِيدٍ، وَجَوَابُهُ يَقْتَرِنُ بِالْفَاءِ.",
      WA_ISTINAF[1] + "أَمَّا «as for» is the particle of condition and detailing; its answer is opened by the fa.",
      WA_ISTINAF[2] + "emmâ «-e gelince»: şart, tafsîl ve te'kîd harfi; cevabı fâ ile başlar.",
      segments=[seg("وَ", "wa", "conj"), seg("أَمَّا", "amma-tafsil", "part")]),
  MUBTADA("الْجَبَلُ", "jabal"),
  ALLADHI_R("لْجَبَلِ", "the mountain", "dağ"),
  MADI("نَزَلَ", "nazala", ["ism-mawsul"], note_ar="، وَالْفَاعِلُ بَعْدَهُ" + SILA[0], note_en="; its doer follows" + SILA[1], note_tr="; fâili sonra gelir" + SILA[2]),
  INDAHU_AID(),
  TARIQ_F(punct="،"),
  tok("فَمَا", "ma-nafiya", "part", ["amma-tafsiliyya", "la-nafiya"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ أَمَّا، وَمَا حَرْفُ نَفْيٍ.",
      "The fa opens the answer of أَمَّا; مَا negates the verb after it.",
      "Fâ, emmâ'nın cevabına girmiştir; mâ nefiy harfi.",
      segments=[seg("فَ", "fa", "conj"), seg("مَا", "ma-nafiya", "part")]),
  tok("زَالَ", "zala", "verb", ["kana-wa-akhawatuha", "hollow-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى الْجَبَلِ — وَمَعَ النَّفْيِ يُفِيدُ الِاسْتِمْرَارَ؛ وَجُمْلَةُ «مَا زَالَ» وَمَا بَعْدَهَا فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "زَالَ is a defective past verb, a sister of كَانَ, built on fatha; its noun is the hidden «it» (the mountain) — after a negation it means «never ceased»; «مَا زَالَ» with what follows is the predicate of the mubtada, in the seat of raf'.",
      "Zâle: kâne'nin kardeşlerinden, fetha üzere mebnî nâkıs mâzî; ismi dağa dönen gizli zamir «o» — nefiyle devamlılık bildirir; «mâ zâle» ve sonrası mübtedânın haberi, mahallen merfû."),
  tok("يُعْرَفُ", "arafa", "verb", ["naib-al-fail", "mudari-marfu", "kana-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ بِالضَّمَّةِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ زَالَ.",
      "Present verb in the passive, in raf'; its deputy doer is the hidden «it» — the clause is the predicate of زَالَ, in the seat of nasb.",
      "Meçhul muzâri, merfû; nâib-i fâil gizli zamir «o» — cümle zâle'nin haberi, mahallen mansûb."),
  BI_NOUN("بِاسْمِهِ", "ism-name", "اسْمِهِ", enc="هِ", note_ar=" — وَالْهَاءُ تَعُودُ عَلَى طَارِقٍ", note_en=" — «his» returns to Ṭāriq", note_tr=" — «hî» Târık'a döner"),
  ILA(),
  MAJR("الْيَوْمِ", "yawm", punct=".")]})
S5.append({"id": "s4", "translation": {"en": "And thus a new era began in the history of al-Andalus.", "tr": "Böylece Endülüs tarihinde yeni bir devir başladı."},
 "tokens": [tok("وَهٰكَذَا", "hakadha", "pron", ["asma-al-ishara", "maful-fih"],
      WA_AR + "هَا لِلتَّنْبِيهِ، وَالْكَافُ لِلتَّشْبِيهِ، وَذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ — وَالْمَجْمُوعُ فِي مَحَلِّ نَصْبٍ صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ: بَدَأَ بَدْءًا هٰكَذَا.",
      "The waw conjoins; «thus»: the hā of alerting, the kāf of likeness and the demonstrative, together in the seat of nasb as the description of an omitted verbal noun («began in this way»).",
      "«ve» + «işte böyle»: tenbih hâ'sı, teşbih kâfı ve işaret ismi; bütünü hazfedilmiş masdarın sıfatı olarak mahallen mansûb («böylece başladı»).",
      segments=[seg("وَ", "wa", "conj"), seg("هٰكَذَا", "hakadha", "pron")]),
  MADI("بَدَأَ", "badaa", note_ar="، وَالْفَاعِلُ «عَهْدٌ» بَعْدَ الْجَارِّ وَالْمَجْرُورِ", note_en="; its doer «an era» comes after the jarr phrase", note_tr="; fâili «devir» câr-mecrûrdan sonra gelir"),
  FI(),
  MAJR("تَارِيخِ", "tarikh", note_ar=MUD[0], note_en=MUD[1], note_tr=MUD[2]),
  ANDALUS_MI(),
  FAIL("عَهْدٌ", "ahd", note_ar=" — مُؤَخَّرٌ عَنِ الْجَارِّ وَالْمَجْرُورِ", note_en=" — placed after the jarr phrase", note_tr=" — câr-mecrûrdan sonraya bırakılmış"),
  NAAT("جَدِيدٌ", "jadid", "raf", punct=".")]})

CHAPTERS = [
 ("ch1", {"ar": "الْأَمِيرُ وَقَائِدُهُ", "en": "The Governor and His Commander", "tr": "Vali ve Kumandanı"}, S1),
 ("ch2", {"ar": "عُبُورُ الْمَضِيقِ", "en": "Crossing the Strait", "tr": "Boğazın Geçilişi"}, S2),
 ("ch3", {"ar": "لِقَاءُ الْجَيْشَيْنِ", "en": "The Two Armies Meet", "tr": "İki Ordunun Karşılaşması"}, S3),
 ("ch4", {"ar": "فَتْحُ الْمُدُنِ", "en": "The Cities Open", "tr": "Şehirlerin Fethi"}, S4),
 ("ch5", {"ar": "بَعْدَ الْفَتْحِ", "en": "After the Conquest", "tr": "Fetihten Sonra"}, S5),
]
TITLES = [c[1] for c in CHAPTERS]
CHAPS = [c[2] for c in CHAPTERS]
DERIVED = {"form-ii-verbs", "form-iii-verbs", "form-iv-verbs", "form-v-verbs", "form-viii-verbs", "form-x-verbs"}
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            g = t.get("grammar", [])
            if DERIVED & set(g): g = [x for x in g if x != "thulathi-mujarrad-babs"]
            t["grammar"] = list(dict.fromkeys(g))

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule); the new entries are listed below
SAMPLES = ROOT / "content/samples"
PREF = ["fath-al-qustantiniyya", "salah-al-din-wa-al-quds", "umar-wa-al-qidr", "abu-hanifa-wa-al-safina", "qisas-al-nabiyyin-4", "qisas-al-nabiyyin-2",
        "qisas-al-nabiyyin-1", "dhu-al-qarnayn-wa-al-sadd", "musa-wa-firawn", "ashab-al-ghar", "al-amana-wa-al-khashaba", "juha-wa-al-himar",
        "wasiyyat-abi-yusuf-l5", "al-usul-al-munifa", "al-kafiya", "talkhis-al-miftah"]
PREF = [p for p in PREF if (SAMPLES / p / "glossary.json").exists()]
PREF += sorted(d.name for d in SAMPLES.iterdir() if (d / "glossary.json").exists() and d.name not in PREF and d.name != SLUG)
# keys that two packages gloss differently are pinned to the package whose sense this story uses
FORCE = {"qarn": "mukhtasar-al-manar",          # «an age, a generation» — not the horn of the Golden Horn
         "ism-name": "qisas-al-nabiyyin-1", "sultan": "wasiyyat-abi-yusuf-l5", "muslim": "qisas-al-nabiyyin-4",
         "lam-jazima": "dhu-al-qarnayn-wa-al-sadd", "arada": "wasiyyat-abi-hanifa", "masjid": "abu-hanifa-wa-al-safina",
         "akhraja": "adam-wa-iblis", "nasara": "wasiyyat-abi-hanifa-samti"}   # نَصَرَهُ اللهُ: «to support, give victory»
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

def PHRASE(lemma, lvl, g_en, g_tr, l_en, l_tr, n_en, n_tr):
    return {"lemma": lemma, "pos": "phrase", "level": lvl, "gloss": {"en": g_en, "tr": g_tr}, "literal": {"en": l_en, "tr": l_tr}, "note": {"en": n_en, "tr": n_tr}}
NEW_GLOSS = {
 # two name-words already on the shelf under the SAME lemma for other men: the key is reused, the gloss names this story's man
 "tariq-name": {"lemma": "طَارِق", "root": "ط ر ق", "pos": "propn", "gloss": {"en": "Ṭāriq — a man's name; here Ṭāriq ibn Ziyād, the commander who crossed into al-Andalus in 92 / 711", "tr": "Târık — erkek adı; burada 92 / 711'de Endülüs'e geçen kumandan Târık b. Ziyâd"}, "level": 5},
 "musa": {"lemma": "مُوسَى", "pos": "propn", "gloss": {"en": "Mūsā — a man's name (a diptote, its vowels estimated on the alif); here Mūsā ibn Nuṣayr, the Umayyad governor of the Maghrib", "tr": "Mûsâ — erkek adı (gayr-i munsarif, harekeleri elif üzerinde takdîrî); burada Emevîlerin Mağrib valisi Mûsâ b. Nusayr"}, "level": 5},
 "ziyad-name": {"lemma": "زِيَاد", "root": "ز ي د", "pos": "propn", "gloss": {"en": "Ziyād — a man's name; here the father of Ṭāriq ibn Ziyād", "tr": "Ziyâd — erkek adı; burada Târık b. Ziyâd'ın babası"}, "level": 5},
 "nusayr": {"lemma": "نُصَيْر", "root": "ن ص ر", "pos": "propn", "gloss": {"en": "Nuṣayr — a man's name (the diminutive pattern فُعَيْل); here the father of Mūsā ibn Nuṣayr", "tr": "Nusayr — erkek adı (fuayl tasğîr vezni); burada Mûsâ b. Nusayr'ın babası"}, "level": 5},
 "ludhriq": {"lemma": "لُذْرِيق", "pos": "propn", "gloss": {"en": "Ludhrīq — Roderic, the last Visigothic king of Hispania (a foreign name: a diptote)", "tr": "Lüzrîk — Rodrigo, Hispanya'nın son Vizigot kralı (yabancı isim: gayr-i munsarif)"}, "level": 5},
 "andalus": {"lemma": "الْأَنْدَلُس", "pos": "propn", "gloss": {"en": "al-Andalus — the Muslims' name for the Iberian Peninsula (a foreign name that always carries the article)", "tr": "Endülüs — Müslümanların İber Yarımadası'na verdiği ad (daima harf-i tarifle gelen yabancı isim)"}, "level": 5},
 "barbar": {"lemma": "الْبَرْبَر", "pos": "noun", "gloss": {"en": "the Berbers — the native peoples of North Africa (a collective noun)", "tr": "Berberîler — Kuzey Afrika'nın yerli kavimleri (ism-i cem')"}, "level": 5},
 "hijra": {"lemma": "هِجْرَة", "root": "ه ج ر", "pos": "noun", "gloss": {"en": "emigration; الْهِجْرَةُ: the Prophet's emigration to Medina, from which the Islamic years are counted (لِلْهِجْرَةِ: AH)", "tr": "hicret, göç; el-hicre: Peygamberimizin Medine'ye hicreti, hicrî yılların başlangıcı (li'l-hicre: hicrî)"}, "level": 4},
 "tariq-ibn-ziyad": PHRASE("طَارِقُ بْنُ زِيَادٍ", 5, "Ṭāriq ibn Ziyād (d. after 95 / 714), the commander who led the Muslim crossing into al-Andalus", "Târık b. Ziyâd (ö. 95 / 714'ten sonra), Endülüs'e geçişi yöneten kumandan",
    "literally «Ṭāriq, son of Ziyād»", "lafzen «Ziyâd'ın oğlu Târık»",
    "A name with its nasab: بْنُ is a na't of the first name, annexed to the father's name; it loses its alif in writing and the first name loses its tanwin. طَارِقُ and بْنُ take the case of their seat; زِيَادٍ is always in jarr.",
    "Nesebiyle birlikte bir isimdir: بْنُ ilk ismin na'tıdır ve babanın adına muzâftır; yazıda elifi, ilk isim de tenvini düşer. طَارِقُ ve بْنُ yerlerinin i'râbını alır; زِيَادٍ daima mecrûrdur."),
 "musa-ibn-nusayr": PHRASE("مُوسَى بْنُ نُصَيْرٍ", 5, "Mūsā ibn Nuṣayr, the Umayyad governor of the Maghrib who sent Ṭāriq and followed him into al-Andalus", "Mûsâ b. Nusayr, Târık'ı gönderen ve ardından Endülüs'e geçen Emevî Mağrib valisi",
    "literally «Mūsā, son of Nuṣayr»", "lafzen «Nusayr'ın oğlu Mûsâ»",
    "A name with its nasab: مُوسَى shows no case (it is estimated on the alif), بْنُ is its na't and carries the case, نُصَيْرٍ is always in jarr.",
    "Nesebiyle birlikte bir isimdir: مُوسَى i'râbı göstermez (elif üzerinde takdîrîdir), بْنُ onun na'tıdır ve i'râbı taşır, نُصَيْرٍ daima mecrûrdur."),
 "jabal-tariq": PHRASE("جَبَلُ طَارِقٍ", 5, "Jabal Ṭāriq — Gibraltar, the rock at the southern tip of Spain, named after Ṭāriq ibn Ziyād", "Cebel-i Târık — Cebelitarık, İspanya'nın güney ucundaki kayalık; adını Târık b. Ziyâd'dan alır",
    "literally «Ṭāriq's mountain»", "lafzen «Târık'ın dağı»",
    "An idafa that became a place-name; the English «Gibraltar» comes from it. جَبَلُ takes the case of its seat; طَارِقٍ is always in jarr.",
    "Yer adı olmuş bir izâfet; «Gibraltar / Cebelitarık» adı buradan gelir. جَبَلُ yerinin i'râbını alır; طَارِقٍ daima mecrûrdur."),
}
NEW_VERBS = {}
# a key is a global claim: a NEW key must not already be on the shelf with another lemma
for k in NEW_GLOSS:
    for p in PREF:
        if k in _G[p] and _G[p][k].get("lemma") != NEW_GLOSS[k].get("lemma"): raise SystemExit(f"new key {k!r} already exists in {p} with lemma {_G[p][k].get('lemma')!r}")

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
 "title": {"ar": "طَارِقُ بْنُ زِيَادٍ وَعُبُورُ الْبَحْرِ", "en": "Ṭāriq ibn Ziyād and the Crossing", "tr": "Târık b. Ziyâd ve Boğazın Geçilişi"},
 "subtitle": {"ar": "قَائِدٌ يَعْبُرُ الْمَضِيقَ، وَجَبَلٌ يَحْمِلُ اسْمَهُ، وَبِلَادٌ تُفْتَحُ لِلْمُسْلِمِينَ — قِصَّةٌ لِلْمُسْتَوَى الْخَامِسِ",
              "en": "A commander crosses the strait, a mountain takes his name, and a land opens to the Muslims — a story for the fifth level",
              "tr": "Boğazı geçen bir kumandan, adını taşıyan bir dağ ve Müslümanlara açılan bir ülke — beşinci seviye için bir hikâye"},
 "level": 5,
 "levelName": "Advanced",
 "version": "0.1.0",
 "published": "2026-11-19",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "قِصَّةٌ تَارِيخِيَّةٌ أَصْلِيَّةٌ (الْمُسْتَوَى الْخَامِسُ) تَرْوِي عُبُورَ طَارِقِ بْنِ زِيَادٍ إِلَى الْأَنْدَلُسِ سَنَةَ ٩٢ هـ / ٧١١ م، أُلِّفَتْ بِأُسْلُوبِ الْقَارِئِ الْمُتَدَرِّجِ عَلَى مَا اتَّفَقَتْ عَلَيْهِ الْمَصَادِرُ، وَمِنْهَا: «فُتُوحُ مِصْرَ وَالْمَغْرِبِ»، وَ«الْبَيَانُ الْمُغْرِبُ»، وَ«نَفْحُ الطِّيبِ». لَيْسَتْ فِيهَا جُمْلَةٌ هِيَ نَصُّ مَصْدَرٍ، وَلَا آيَةٌ وَلَا حَدِيثٌ؛ وَتُرِكَتِ الْأَعْدَادُ وَالْأَخْبَارُ الْمُخْتَلَفُ فِيهَا، كَإِحْرَاقِ السُّفُنِ وَالْخُطْبَةِ الْمَنْسُوبَةِ إِلَى طَارِقٍ. كُلُّ إِعْرَابٍ فِيهَا اجْتِهَادُ الْمُؤَلِّفِ، وَهِيَ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "ORIGINAL Level-5 graded Arabic: a historical narrative of Ṭāriq ibn Ziyād's crossing into al-Andalus in 92 AH / 711 CE, composed for this reader from the well-attested core of the event as the classical historians tell it — Ibn ʿAbd al-Ḥakam (Futūḥ Miṣr wa-l-Maghrib), Ibn ʿIdhārī (al-Bayān al-Mughrib) and al-Maqqarī (Nafḥ al-Ṭīb). No sentence is a quotation from any source and no verse or hadith is quoted. Legends and disputed reports are left out: the burning of the ships, the speech attributed to Ṭāriq («the sea is behind you»), every army size, the battle site and Roderic's fate. Every i'rab line is the author's own analysis, pending scholarly review.",
  "tr": "ÖZGÜN 5. seviye kolaylaştırılmış Arapça: Târık b. Ziyâd'ın 92 / 711 yılında Endülüs'e geçişinin, klasik tarihçilerin — İbn Abdülhakem (Fütûhu Mısr ve'l-Mağrib), İbn İzârî (el-Beyânü'l-Muğrib) ve Makkarî (Nefhu't-Tîb) — anlattığı sağlam çekirdeğe dayanılarak bu okuyucu için yazılmış tarihî anlatısı. Hiçbir cümle herhangi bir kaynaktan alıntı değildir; âyet ya da hadis aktarılmamıştır. Efsaneler ve ihtilaflı rivayetler dışarıda bırakılmıştır: gemilerin yakılması, Târık'a nisbet edilen hutbe («deniz arkanızda»), ordu sayıları, savaşın yeri ve Rodrigo'nun akıbeti. Her i'râb satırı yazarın kendi tahlilidir ve ilmî incelemeyi beklemektedir.",
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
