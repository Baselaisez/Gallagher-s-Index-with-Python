"""Author content/samples/ashab-al-ghar — «أَصْحَابُ الْغَارِ», the twenty-first ORIGINAL story and the first original text at Level 3 (wave 113).

ORIGINAL graded Arabic: the three travellers shut in a cave by a fallen rock, each calling on God by the best deed he did for
His sake alone — a narrative preserved in the ḥadīth collections (al-Bukhārī and Muslim), RETOLD FREELY in the wording of a
graded reader. No sentence here is the text of a ḥadīth and none may be cited as one. Four chapters, twenty-five sentences.
Every token carries its trilingual iʿrāb; paradigms and glosses are copied by lemma identity from the shared lexicon; three
entries are new (غَار، أَجِير، حَلَبَ — the verb with a generated paradigm of bāb نَصَرَ).  Regenerate with:
python3 tools/authoring/author_ghar.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "ashab-al-ghar"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

# ============ «أَصْحَابُ الْغَارِ» — the twenty-first ORIGINAL story, the first at Level 3 (wave 113) ============
# every surface and every iʿrāb line is NFC-normalised on the way in (the corpus stores fatḥa before shadda)
PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "هِمَا": "pron-3d"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "هِمَا": "هُمَا"})

LAMMA_CL = (" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", "; the clause fills the seat of jarr, annexed to لَمَّا", "; cümle lemmâ'ya muzâfun ileyh olarak mahallen mecrûr")
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")

ALLAHUMMA = lambda punct=None: tok("اللّٰهُمَّ", "allahumma", "propn", ["vocative-munada", "al-mabni-ghayr-al-lazim-tawabi-al-munada-wa-huruf-al-nida-wa-ism-la-wal-mudari-bil-nun"],
    "مُنَادًى مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ، وَالْمِيمُ الْمُشَدَّدَةُ عِوَضٌ عَنْ حَرْفِ النِّدَاءِ الْمَحْذُوفِ.",
    "The vocative «O God»: built on damma in the seat of nasb; the doubled mim at the end stands in for the dropped vocative particle.",
    "Münâdâ, damme üzere mebnî, mahallen mansûb; sondaki şeddeli mîm hazfedilen nidâ harfinin yerine geçer.", punct=punct)
INNAHU_SHAN = lambda: tok("إِنَّهُ", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "mawadi-al-munfasil-wa-damir-al-fasl-wal-shan"],
    "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَالْهَاءُ ضَمِيرُ الشَّأْنِ فِي مَحَلِّ نَصْبٍ اسْمُهَا — وَالْجُمْلَةُ بَعْدَهُ تُفَسِّرُهُ، فِي مَحَلِّ رَفْعٍ خَبَرُهَا.",
    "إِنَّ with the pronoun of the matter (ḍamīr al-shaʾn) as its noun, in the seat of nasb — the whole sentence that follows explains it and is the predicate.",
    "İnne; hâ şe'n zamiri, ismi olarak mahallen mansûb — sonraki cümle onu açıklar, haber olarak mahallen merfû.",
    segments=[seg("إِنَّ", "inna", "part"), seg("هُ", "pron-3ms", "pron")])
IN_SH = lambda: IN_SHART("إِنْ")
KUNTU = lambda: tok("كُنْتُ", "kana", "verb", ["kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil", "hollow-verbs"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ؛ وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    "كَانَ as the verb of the condition: built on sukun before the ta of the doer (its middle letter dropped where two quiescents met), in the seat of jazm; the ta is its noun, in the seat of raf'.",
    "Şart fiili olarak kâne: fâil tâ'sı bitiştiği için sükûn üzere mebnî (iki sâkin karşılaşınca aynı düştü), mahallen meczûm; tâ, kâne'nin ismi — mahallen merfû.")
FAALTU_KH = lambda: tok("فَعَلْتُ", "faala", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "fail"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
    "Past verb built on sukun before the ta of the doer, the ta its doer — the clause is the predicate of كَانَ, in the seat of nasb.",
    "Fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî, tâ fâil — cümle kâne'nin haberi, mahallen mansûb.")
DHALIKA_MAF = lambda: tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "maful-bihi"],
    "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَاللَّامُ لِلْبُعْدِ وَالْكَافُ لِلْخِطَابِ.",
    "A demonstrative built on fatha, the object in the seat of nasb; its lam marks distance and its kaf addresses the listener.",
    "İşaret ismi, fetha üzere mebnî, mef'ûlün bih olarak mahallen mansûb; lâm uzaklık, kâf hitap içindir.")
LI_WAJHIKA = lambda: tok("لِوَجْهِكَ", "li", "prep", ["huruf-jarr", "lam-taleel", "idafa-definiteness", "al-bariz-al-muttasil", "maful-lah"],
    "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَوَجْهِ مَجْرُورٌ بِالْكَسْرَةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«فَعَلْتُ»، وَفِيهِ مَعْنَى الْمَفْعُولِ لِأَجْلِهِ.",
    "The lam is a jarr letter of purpose; «face» is in jarr and annexed to the attached «Your», in the seat of jarr — the phrase hangs on «I did» and carries the sense of a maf'ul li-ajlih: for Your sake alone.",
    "Ta'lîl lâmı cer harfi; «vech» mecrûr ve muzâf, bitişik kâf zamiri muzâfun ileyh — câr-mecrûr «yaptım»a müteallık, mef'ûlün lieclih anlamı taşır: sırf Senin rızân için.",
    segments=[seg("لِ", "li", "prep"), seg("وَجْهِ", "wajh", "noun"), seg("كَ", "pron-2ms", "pron")])
FAFTAH = lambda: tok("فَافْتَحْ", "fataha", "verb", ["al-fa-fi-jawab-al-shart", "imperative-amr", "al-fail-al-mudmar-al-mustatir-wujuban", "al-majzum-wal-shart-wal-jaza"],
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَافْتَحْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، وَهِيَ دُعَاءٌ.",
    "The fa introduces the answer of the condition; «open» is an imperative built on sukun with the doer «You» necessarily hidden — the clause fills the seat of jazm as the answer, and it is a supplication.",
    "Fâ şartın cevabına gelmiştir; «aç» sükûn üzere mebnî emir, fâili vücûben müstetir «Sen» — cümle şartın cevabı olarak mahallen meczûm; bir duâdır.",
    segments=[seg("فَ", "fa", "conj"), seg("افْتَحْ", "fataha", "verb")])
LANA = lambda punct=None: JARR_PRON("لَنَا", "li", "لَ", "نَا", " («bize»)", punct=punct)
HADHIHI_J = lambda: tok("هٰذِهِ", "hadhihi", "pron", ["asma-al-ishara"], "اسْمُ إِشَارَةٍ لِلْمُفْرَدَةِ الْمُؤَنَّثَةِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ.",
    "The feminine singular demonstrative, built on kasra, in the seat of jarr.", "Müfred müennes işaret ismi, kesre üzere mebnî, mahallen mecrûr.")
SAKHRA_BADAL_J = lambda punct=None: BADAL("الصَّخْرَةِ", "sakhra", "jarr", punct=punct)
FALAM = lambda: tok("فَلَمْ", "lam-jazima", "part", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], FA_AR + "لَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
    "The fa conjoins; لَمْ negates, governs jazm and turns the present to the past.", "«bunun üzerine» + lem: nefiy, cezm ve kalb harfi.",
    segments=[seg("فَ", "fa", "conj"), seg("لَمْ", "lam-jazima", "part")])
YAQDIRU = lambda punct=None: tok("يَقْدِرُوا", "qadara", "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil", "lam-jazim"],
    "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ، وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَالْأَلِفُ فَارِقَةٌ.",
    "Present verb in jazm after لَمْ, its sign the dropped nun of the five verbs; the waw is the doer, in the seat of raf', and the final alif only marks the plural in writing.",
    "Lem ile meczûm muzâri; alâmeti ef'âl-i hamseden olduğu için nûnun düşmesi; vâv fâil, mahallen merfû; elif fârikadır.", punct=punct)
TAHARRAKAT = lambda: MADI("فَتَحَرَّكَتِ", "taharraka", ["form-v-verbs"], fem=True, hidden=False, kasra=True)
SAKHRA_F = lambda punct=None: FAIL("الصَّخْرَةُ", "sakhra", punct=punct)
ILAYYA = lambda punct=None: tok("إِلَيَّ", "ila", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"],
    "حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَقُلِبَتْ أَلِفُ إِلَى يَاءً وَأُدْغِمَتْ فِي يَاءِ الضَّمِيرِ.",
    "A jarr letter; the speaker's ya fills the seat of jarr — the alif of إِلَى turns to ya and merges with the pronoun's ya.",
    "Cer harfi; mütekellim yâ'sı mahallen mecrûr — ilâ'nın elifi yâ'ya dönüp zamirin yâ'sına idgâm edildi.", punct=punct,
    segments=[seg("إِلَى", "ila", "prep"), seg("يَ", "pron-1s", "pron")])
def YA_NOUN(full, lex, role_ar, role_en, role_tr, extra=None, punct=None):
    """أَهْلِي، يَدِي، أَجْرِي، عِنْدِي: a noun annexed to the speaker's yāʾ — its own ending is ESTIMATED on the letter before the yāʾ"""
    return tok(full, lex, "noun", extra + ["ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil", "al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"],
        role_ar + " مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        role_en + " estimated on the letter before the speaker's ya, which the kasra that suits the ya occupies; annexed to that ya, the second term of the idafa in the seat of jarr.",
        role_tr + " mütekellim yâ'sından önceki harf üzerinde takdîrî — yâ'ya uygun kesre o yeri işgal eder; muzâf, yâ muzâfun ileyh, mahallen mecrûr.",
        punct=punct, segments=[seg(full[:-1], lex, "noun"), seg("ي", "pron-1s", "pron")])
NUN_WIQ_VERB = lambda full, lex, extra, ar_head, en_head, tr_head, punct=None, stem=None: tok(full, lex, "verb", extra + ["al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim"],
    ar_head + "، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
    en_head + "; the nun guards the verb's ending and the speaker's ya is the object «me», in the seat of nasb.",
    tr_head + "; nûn vikâye içindir, mütekellim yâ'sı mef'ûlün bih «beni» — mahallen mansûb.", punct=punct,
    segments=[s for s in [(seg("فَ", "fa", "conj") if full.startswith("فَ") else None), seg(stem, lex, "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")] if s])

# ---- Chapter 1 — الْغَارُ وَالصَّخْرَةُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Three men set out on a journey, and when evening came upon them a heavy rain fell on them.", "tr": "Üç adam bir yolculuğa çıktı; akşam olunca üzerlerine şiddetli bir yağmur indi."},
 "tokens": [MADI("خَرَجَ", "kharaja"),
  tok("ثَلَاثَةُ", "thalatha", "noun", ["fail", "asma-al-adad-fil-kafiya", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — عَدَدٌ مِنَ الثَّلَاثَةِ إِلَى الْعَشَرَةِ يُضَافُ إِلَى جَمْعٍ، وَيُخَالِفُ مَعْدُودَهُ فِي التَّذْكِيرِ وَالتَّأْنِيثِ.",
      "The doer, in raf', annexed — a number from three to ten is annexed to a plural and takes the opposite gender of its counted noun.", "Fâil, merfû, muzâf — üçten ona kadar sayılar cemiye muzâf olur ve ma'dûduna cinsçe zıt gelir."),
  tok("رِجَالٍ", "rajul", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تَكْسِيرٍ لِرَجُلٍ، وَهُوَ مَعْدُودُ الْعَدَدِ.",
      "The second term of the idafa, in jarr — the broken plural of «man», the counted noun of the number.", "Muzâfun ileyh, mecrûr — racülün cem-i teksîri, sayının ma'dûdu."),
  FI(), MAJR("سَفَرٍ", "safar", punct="،"), LAMMA2("فَلَمَّا"),
  tok("أَمْسَوْا", "amsa", "verb", ["kana-wa-akhawatuha", "al-fil-al-tamm-wal-naqis", "naqis-verbs", "al-bariz-al-muttasil", "fail"],
      "أَمْسَى هُنَا فِعْلٌ تَامٌّ بِمَعْنَى «دَخَلُوا فِي الْمَسَاءِ»، مَبْنِيٌّ عَلَى ضَمٍّ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ" + LAMMA_CL[0] + ".",
      "أَمْسَى used here as a complete verb, «they reached evening»: built on a damma estimated on the dropped alif, the waw its doer" + LAMMA_CL[1] + ".",
      "Emsâ burada tam fiil («akşama erdiler»); düşen elif üzerindeki takdîrî damme ile mebnî, vâv fâil" + LAMMA_CL[2] + ".",
      segments=[seg("أَمْسَوْ", "amsa", "verb"), seg("ا", "pron-3mp", "pron")]),
  MADI("نَزَلَ", "nazala"), JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onların üzerine»)"), FAIL("مَطَرٌ", "matar"), NAAT("شَدِيدٌ", "shadid", "raf", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "So they entered a cave in a mountain to spend the night in it until morning.", "tr": "Bunun üzerine sabaha kadar içinde gecelemek için bir dağdaki mağaraya girdiler."},
 "tokens": [VERB_WAW("فَدَخَلُوا", "dakhala"), MAFUL("غَارًا", "ghar"), FI(), MAJR("جَبَلٍ", "jabal"),
  tok("لِيَبِيتُوا", "bata", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "afal-khamsa", "hollow-verbs", "al-bariz-al-muttasil"],
      "اللَّامُ لَامُ التَّعْلِيلِ، وَيَبِيتُوا فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "The lam of purpose; «that they might spend the night» is a present verb put in nasb by a hidden أَنْ after the lam, its sign the dropped nun of the five verbs; the waw is the doer.",
      "Ta'lîl lâmı; «gecelesinler diye» muzâri, lâmdan sonra gizli en ile mansûb, alâmeti ef'âl-i hamseden olduğu için nûnun düşmesi; vâv fâil.",
      segments=[seg("لِ", "lam-taleel", "part"), seg("يَبِيتُوا", "bata", "verb")]),
  JARR_PRON("فِيهِ", "fi", "فِي", "هِ", " («onda»)"),
  tok("حَتَّى", "hatta", "prep", ["huruf-jarr", "ila-hatta-fi-wal-ba-fil-kafiya"], "حَرْفُ جَرٍّ لِلْغَايَةِ.", "A jarr letter marking the end point («until»).", "Gâye bildiren cer harfi («-e kadar»)."),
  MAJR("الصَّبَاحِ", "sabah", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "Then a huge rock fell from the mountain and blocked the mouth of the cave against them.", "tr": "Derken dağdan kocaman bir kaya düştü ve mağaranın ağzını üzerlerine kapattı."},
 "tokens": [MADI("فَسَقَطَتْ", "saqata", fem=True), FAIL("صَخْرَةٌ", "sakhra"), NAAT("عَظِيمَةٌ", "azim", "raf"), MINA(), MAJR("الْجَبَلِ", "jabal", punct="،"),
  MADI("فَسَدَّتْ", "sadda-block", ["doubled-verbs"], fem=True, hidden=True), JARR_PRON("عَلَيْهِمْ", "ala", "عَلَيْ", "هِمْ", " («onlara karşı»)"),
  MAFUL("بَابَ", "bab", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"), MUDAF_ILAYH("الْغَارِ", "ghar", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "They rose to push it away but could not, and they knew there was no way out for them except by God's mercy.", "tr": "Onu itmek için kalktılar, fakat buna güçleri yetmedi; anladılar ki Allah'ın rahmetinden başka onlara bir çıkış yoktur."},
 "tokens": [VERB_WAW("فَقَامُوا", "qama", ["hollow-verbs"]), JARR_PRON("إِلَيْهَا", "ila", "إِلَيْ", "هَا", " («ona»)"),
  tok("لِيَدْفَعُوهَا", "dafaa", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari", "afal-khamsa", "al-bariz-al-muttasil", "maful-bihi"],
      "اللَّامُ لِلتَّعْلِيلِ، وَيَدْفَعُوا مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ، وَعَلَامَةُ نَصْبِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "The lam of purpose; «that they might push» is in nasb by a hidden أَنْ, its sign the dropped nun; the waw is the doer and «it» the object, in the seat of nasb.",
      "Ta'lîl lâmı; «itsinler diye» gizli en ile mansûb, alâmeti nûnun düşmesi; vâv fâil, «onu» mef'ûlün bih — mahallen mansûb.", punct="،",
      segments=[seg("لِ", "lam-taleel", "part"), seg("يَدْفَعُو", "dafaa", "verb"), seg("هَا", "pron-3fs", "pron")]),
  FALAM(), YAQDIRU(), ALA(),
  tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ.", "A demonstrative built on fatha, in the seat of jarr.", "İşaret ismi, fetha üzere mebnî, mahallen mecrûr.", punct="،"),
  VERB_WAW("وَعَلِمُوا", "alima"),
  ANNAHU((" — وَالْهَاءُ ضَمِيرُ الشَّأْنِ، وَالْجُمْلَةُ بَعْدَهُ خَبَرُهَا، وَالْمَصْدَرُ الْمُؤَوَّلُ سَدَّ مَسَدَّ مَفْعُولَيْ عَلِمَ", "; here the ha is the pronoun of the matter, the sentence after it the predicate, and the whole clause stands in for both objects of «knew»", "; hâ burada şe'n zamiri, sonraki cümle haberi; müevvel masdar «bildiler»in iki mef'ûlü yerine geçer")),
  tok("لَا", "la-nafiya-lil-jins", "part", ["la-nafiya-lil-jins", "ma-la-laysa-wa-la-al-jins"], "لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ إِنَّ.", "The لَا that denies the whole kind, governing like إِنَّ.", "Cinsi nefyeden lâ; inne gibi amel eder."),
  tok("مَخْرَجَ", "makhraj", "noun", ["la-nafiya-lil-jins"], "اسْمُ لَا النَّافِيَةِ لِلْجِنْسِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَخَبَرُهَا مَحْذُوفٌ.", "The noun of the kind-denying لَا, built on fatha in the seat of nasb; its predicate is omitted.", "Cinsi nefyeden lâ'nın ismi; fetha üzere mebnî, mahallen mansûb; haberi hazfedilmiştir."),
  JARR_PRON("لَهُمْ", "li", "لَ", "هُمْ", " («onlar için»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِخَبَرِ لَا الْمَحْذُوفِ", note_en="; the phrase hangs on the omitted predicate of لَا", note_tr="; câr-mecrûr lâ'nın hazfedilen haberine müteallık"),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ بَعْدَ النَّفْيِ، وَمَا بَعْدَهَا يَأْخُذُ إِعْرَابَهُ مِنْ مَوْقِعِهِ.", "The particle of an emptied exception after a negation; what follows takes the case its own position demands.", "Nefiyden sonra müferrağ istisnâ edatı; sonrası i'râbını kendi mevkiinden alır."),
  BI_NOUN("بِرَحْمَةِ", "rahma", "رَحْمَةِ", extra=["idafa-definiteness"], note_ar="، مُضَافٌ", note_en="; annexed", note_tr="; muzâf"), ALLAH_MI(punct=".")]})
S1.append({"id": "s5", "translation": {"en": "One of them said: Nothing will save you from this rock but sincerity, so let each of us call on his Lord by the best deed he did for His sake.", "tr": "İçlerinden biri dedi ki: Sizi bu kayadan ancak samimiyet kurtarır; öyleyse her birimiz, sırf O'nun rızâsı için yaptığı en güzel amelle Rabbine dua etsin."},
 "tokens": [QALA("فَقَالَ"), ENC_NOUN("أَحَدُهُمْ", "ahad", "هُمْ", "fail", punct=":"), LA_NAFIYA(),
  tok("يُنَجِّيكُمْ", "najja", "verb", ["mudari-marfu", "form-ii-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَكُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُؤَخَّرٌ بَعْدَ إِلَّا.",
      "Present verb in raf' by a damma estimated on the ya; «you» is its object in the seat of nasb, and its doer comes after إِلَّا.",
      "Yâ üzerinde takdîrî damme ile merfû muzâri; «sizi» mef'ûlün bih, mahallen mansûb; fâili illâ'dan sonra gelir.",
      segments=[seg("يُنَجِّي", "najja", "verb"), seg("كُمْ", "pron-2mp", "pron")]),
  MIN(), HADHIHI_J(), SAKHRA_BADAL_J(),
  tok("إِلَّا", "illa", "part", ["istithna-mufarragh", "istithna"], "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ — وَمَا بَعْدَهَا فَاعِلُ يُنَجِّي.", "The particle of the emptied exception — what follows it is the doer of «saves».", "Müferrağ istisnâ edatı — sonrası «kurtarır»ın fâilidir."),
  FAIL("الصِّدْقُ", "sidq", punct="،", note_ar=" — جَاءَ بَعْدَ إِلَّا فِي اسْتِثْنَاءٍ مُفَرَّغٍ، فَأَخَذَ إِعْرَابَ مَوْقِعِهِ", note_en=" — it stands after إِلَّا in an emptied exception and takes the case of its position", note_tr=" — müferrağ istisnâda illâ'dan sonra gelip mevkiinin i'râbını aldı"),
  tok("فَلْيَدْعُ", "daa", "verb", ["lam-amr", "nawasib-wa-jawazim-al-mudari", "naqis-verbs", "jawazim-al-mudari-wal-amr-fil-kafiya"],
      FA_AR + "اللَّامُ لَامُ الْأَمْرِ، سُكِّنَتْ بَعْدَ الْفَاءِ، وَيَدْعُ فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَامِ الْأَمْرِ، وَعَلَامَةُ جَزْمِهِ حَذْفُ حَرْفِ الْعِلَّةِ (الْوَاوِ).",
      "The fa conjoins; the lam of command (made quiescent after the fa) governs jazm on «let … call», whose sign is the dropped weak letter, the waw.",
      "Fâ atıf; emir lâmı (fâdan sonra sâkin kılınmış) «dua etsin»i cezmeder; alâmeti illet harfinin (vâvın) düşmesi.",
      segments=[seg("فَ", "fa", "conj"), seg("لْ", "lam-amr", "part"), seg("يَدْعُ", "daa", "verb")]),
  tok("كُلُّ", "kull", "noun", ["fail", "idafa-definiteness"], "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The doer, in raf', annexed.", "Fâil, merfû, muzâf."),
  MUDAF_ILAYH("وَاحِدٍ", "wahid"),
  JARR_PRON("مِنَّا", "min", "مِنْ", "نَا", " («bizden»)", note_ar=" — وَأُدْغِمَتْ نُونُ مِنْ فِي نُونِ الضَّمِيرِ", note_en="; the nun of مِنْ merges into the pronoun's nun", note_tr="; min'in nûnu zamirin nûnuna idgâm edildi"),
  ENC_NOUN("رَبَّهُ", "rabb", "هُ", "maful"),
  BI_NOUN("بِأَحْسَنِ", "ahsan", "أَحْسَنِ", extra=["ism-tafdil", "idafa-definiteness"], note_ar="، مُضَافٌ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ، أُضِيفَ فَجُرَّ بِالْكَسْرَةِ", note_en="; annexed — an elative on أَفْعَل that, being annexed, takes the ordinary kasra", note_tr="; muzâf — ef'al vezninde ism-i tafdîl; muzâf olduğu için kesre ile mecrûr"),
  MUDAF_ILAYH("عَمَلٍ", "amal-deed"),
  ENC_MADI("عَمِلَهُ", "amila", "هُ", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ نَعْتٌ لِعَمَلٍ", note_en="; the clause qualifies «a deed», in the seat of jarr", note_tr="; cümle «amel»in sıfatı, mahallen mecrûr"),
  LI_ENC("لِوَجْهِهِ", "wajh", "وَجْهِ", "هِ", punct=".")]})

# ---- Chapter 2 — بِرُّ الْوَالِدَيْنِ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "The first said: O God, I had two aged parents, and I never gave anyone milk before them, neither family nor child.", "tr": "Birincisi dedi ki: Allah'ım, benim yaşlı iki ana-babam vardı; onlardan önce ne aileme ne çocuğuma, hiç kimseye süt içirmezdim."},
 "tokens": [QALA("فَقَالَ"), FAIL("الْأَوَّلُ", "awwal", punct=":"), ALLAHUMMA(), INNAHU_SHAN(), KANA("كَانَ"),
  JARR_PRON("لِي", "li", "لِ", "ي", " («benim»)", note_ar=KH_MUQ[0], note_en=KH_MUQ[1], note_tr=KH_MUQ[2]),
  tok("أَبَوَانِ", "ab", "noun", ["kana-wa-akhawatuha", "al-muthanna"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَرُدَّتْ لَامُ الْكَلِمَةِ (الْوَاوُ) فِي التَّثْنِيَةِ.",
      "The noun of كَانَ, placed after its predicate, in raf' by the alif of the dual — the root's waw returns in the dual (أَبَوَانِ).", "Kâne'nin ismi (haberinden sonra), tesniye olduğu için elifle merfû — tesniyede kelimenin lâmı (vâv) geri gelir."),
  tok("شَيْخَانِ", "shaykh", "noun", ["naat-sifa", "al-muthanna"], "نَعْتٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "An adjective agreeing with its noun, in raf' by the alif of the dual.", "Na't; tesniye olduğu için elifle merfû."),
  tok("كَبِيرَانِ", "kabir", "noun", ["naat-sifa", "al-muthanna"], "نَعْتٌ ثَانٍ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "A second adjective, in raf' by the alif of the dual.", "İkinci na't; tesniye olduğu için elifle merfû.", punct="،"),
  tok("وَكُنْتُ", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs"],
      WA_AR + "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "The waw conjoins; كَانَ built on sukun before the ta of the doer (its middle letter dropped where two quiescents met); the ta is its noun, in the seat of raf'.",
      "«ve» + kâne: fâil tâ'sı bitiştiği için sükûn üzere mebnî (iki sâkin karşılaşınca aynı düştü); tâ ismi, mahallen merfû.", segments=[seg("وَ", "wa", "conj"), seg("كُنْتُ", "kana", "verb")]),
  LA_NAFIYA(),
  tok("أَسْقِي", "saqa-water", "verb", ["mudari-marfu", "naqis-verbs", "kana-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ.",
      "Present verb in raf' by a damma estimated on the ya; the doer «I» must stay hidden — the clause is the predicate of كَانَ, in the seat of nasb.",
      "Yâ üzerinde takdîrî damme ile merfû muzâri; fâil «ben» vücûben müstetir — cümle kâne'nin haberi, mahallen mansûb."),
  MAFUL("أَحَدًا", "ahad", note_ar=" — الْمَفْعُولُ الْأَوَّلُ", note_en=" — the first of two objects", note_tr=" — birinci mef'ûl"),
  ZARF("قَبْلَهُمَا", "qabla", extra=["al-bariz-al-muttasil"], note_ar="، وَهُمَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ", note_en="; the attached dual pronoun is the second term, in the seat of jarr", note_tr="; bitişik tesniye zamiri muzâfun ileyh, mahallen mecrûr", segments=[seg("قَبْلَ", "qabla", "noun"), seg("هُمَا", "pron-3d", "pron")], **ZAMAN),
  tok("لَبَنًا", "laban", "noun", ["maful-bihi", "mafulayn"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ — سَقَى يَتَعَدَّى إِلَى مَفْعُولَيْنِ.", "A second direct object, in nasb — «to give to drink» takes two objects.", "İkinci mef'ûlün bih, mansûb — sekâ iki mef'ûl alır.", punct="،"),
  tok("لَا", "la-nafiya", "part", ["la-nafiya"], "لَا نَافِيَةٌ مُؤَكِّدَةٌ لِلنَّفْيِ قَبْلَهَا، لَا عَمَلَ لَهَا.", "لَا repeating and strengthening the negation before it; it governs nothing.", "Önceki nefyi pekiştiren lâ; amel etmez."),
  tok("أَهْلًا", "ahl", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan"], "بَدَلٌ مِنْ «أَحَدًا» مَنْصُوبٌ بِالْفَتْحَةِ — بَدَلُ تَفْصِيلٍ.", "A badal of «anyone», in nasb — a badal that spells out the parts.", "«Hiç kimse»den bedel, mansûb — tafsîl bedeli."),
  WA_LA_NAFIYA(),
  tok("وَلَدًا", "walad", "noun", ["atf-nasaq"], "مَعْطُوفٌ عَلَى أَهْلًا مَنْصُوبٌ بِالْفَتْحَةِ — وَالْوَاوُ هُنَا أَصْلِيَّةٌ مِنَ الْكَلِمَةِ، وَحَرْفُ الْعَطْفِ هُوَ وَاوُ «وَلَا».",
      "Conjoined to «family», in nasb — this word's own waw is a root letter; the conjunction is the waw of «and not».", "«Ehl»e ma'tûf, mansûb — buradaki vâv kelimenin aslındandır; atıf harfi «ve lâ»nın vâvıdır.", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "One day I went far away with the sheep and did not return until the two of them had fallen asleep.", "tr": "Bir gün koyunlarla uzak bir yere gittim ve ikisi uyuyuncaya kadar dönmedim."},
 "tokens": [MADI_T("فَذَهَبْتُ", "dhahaba", who="ana"), ZARF("يَوْمًا", "yawm", mudaf=False, **ZAMAN), BI_NOUN("بِالْغَنَمِ", "ghanam", "الْغَنَمِ"), ILA(), MAJR("مَكَانٍ", "makan"), NAAT("بَعِيدٍ", "baid", "jarr", punct="،"),
  FALAM(),
  tok("أَرْجِعْ", "rajaa", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.",
      "Present verb in jazm after لَمْ, its sign the sukun; the doer «I» must stay hidden.", "Lem ile meczûm muzâri, alâmeti sükûn; fâil «ben» vücûben müstetir."),
  HATTA_IBT(), DUAL_MADI("نَامَا", "nama", ["hollow-verbs"], punct=".")]})
S2.append({"id": "s3", "translation": {"en": "I milked their milk for them and found them asleep; I hated to break their sleep, and I hated to give my family and my child to drink before them.", "tr": "Onlar için sütlerini sağdım, fakat ikisini uyur buldum; uykularını bölmek istemedim, ailemle çocuğuma onlardan önce içirmeyi de istemedim."},
 "tokens": [MADI_T("فَحَلَبْتُ", "halaba", who="ana"), JARR_PRON("لَهُمَا", "li", "لَ", "هُمَا", " («o ikisi için»)"), ENC_NOUN("لَبَنَهُمَا", "laban", "هُمَا", "maful", punct="،"),
  MADI_T("فَوَجَدْتُهُمَا", "wajada", who="ana", enc="هُمَا"),
  tok("نَائِمَيْنِ", "naaim", "noun", ["hal", "al-muthanna", "ism-fail"], "حَالٌ مَنْصُوبٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — وَهُوَ اسْمُ فَاعِلٍ مِنْ نَامَ.", "The hal, in nasb by the ya of the dual — the active participle of «to sleep».", "Hâl, tesniye olduğu için yâ ile mansûb — nâme'nin ism-i fâili.", punct="،"),
  MADI_T("فَكَرِهْتُ", "kariha", who="ana"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِكَرِهْتُ", "; the clause it builds is the object of «I hated»", "; kurduğu müevvel masdar «istemedim»in mef'ûlüdür"),
  MANSUB_AN("أَقْطَعَ", "qataa", who="أَنَا", wujub=True), JARR_PRON("عَلَيْهِمَا", "ala", "عَلَيْ", "هِمَا", " («o ikisinin»)"), ENC_NOUN("نَوْمَهُمَا", "nawm", "هُمَا", "maful", punct="،"),
  MADI_T("وَكَرِهْتُ", "kariha", who="ana"),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِكَرِهْتُ", "; the clause it builds is the object of «I hated»", "; kurduğu müevvel masdar «istemedim»in mef'ûlüdür"),
  MANSUB_AN("أَسْقِيَ", "saqa-water", ["naqis-verbs"], who="أَنَا", wujub=True, note_ar=" — وَظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ لِخِفَّتِهَا", note_en=" — the fatha is written on the ya, which is light enough to carry it", note_tr=" — fetha hafif olduğu için yâ üzerinde yazılır"),
  YA_NOUN("أَهْلِي", "ahl", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ", "The direct object, in nasb by a fatha", "Mef'ûlün bih, fetha ile mansûb;", extra=["maful-bihi"]),
  tok("وَوَلَدِي", "walad", "noun", ["atf-nasaq", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"],
      WA_AR + "وَلَدِي مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The waw conjoins; «my child» follows in nasb by a fatha estimated before the speaker's ya, to which it is annexed.", "«ve» + veledî: ma'tûf, yâdan önceki harf üzerinde takdîrî fetha ile mansûb; muzâf, yâ muzâfun ileyh.",
      segments=[seg("وَ", "wa", "conj"), seg("وَلَدِ", "walad", "noun"), seg("ي", "pron-1s", "pron")]),
  ZARF("قَبْلَهُمَا", "qabla", extra=["al-bariz-al-muttasil"], note_ar="، وَهُمَا مُضَافٌ إِلَيْهِ", note_en="; the dual pronoun is its second term", note_tr="; tesniye zamiri muzâfun ileyh", segments=[seg("قَبْلَ", "qabla", "noun"), seg("هُمَا", "pron-3d", "pron")], punct=".", **ZAMAN)]})
S2.append({"id": "s4", "translation": {"en": "So I stayed standing with the vessel in my hand until dawn broke, while the children cried from hunger at my feet.", "tr": "Böylece kap elimde, tan ağarıncaya kadar ayakta bekledim; çocuklar ise ayaklarımın dibinde açlıktan ağlıyordu."},
 "tokens": [tok("فَبَقِيتُ", "baqiya", "verb", ["naqis-verbs", "al-bariz-al-muttasil", "fail"],
      FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ، تَثْبُتُ يَاؤُهُ قَبْلَ التَّاءِ.",
      "The fa conjoins; past verb built on sukun before the ta of the doer, the ta its doer — a ya-final verb of the bab سَمِعَ, whose ya stays before the ta.", "Fâ atıf; fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî, tâ fâil — semia bâbından yâ'lı nâkıs, yâ'sı tâ'dan önce sâbit kalır.",
      segments=[seg("فَ", "fa", "conj"), seg("بَقِيتُ", "baqiya", "verb")]),
  HAL("قَائِمًا", "qaim", ["ism-fail"]),
  tok("وَالْإِنَاءُ", "inaa", "noun", ["al-hal-jumla-wa-rabituha", "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَالْإِنَاءُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ الِاسْمِيَّةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw opens a hal clause; «the vessel» is its mubtada, in raf' — the nominal clause is a hal, in the seat of nasb.", "Hâl vâvı; «kap» mübtedâ, merfû — isim cümlesi hâl olarak mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("الْإِنَاءُ", "inaa", "noun")]),
  FI(("، وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", " — the phrase is the predicate, in the seat of raf'", " — câr-mecrûr haber, mahallen merfû")),
  YA_NOUN("يَدِي", "yad", "مَجْرُورٌ بِكَسْرَةٍ", "In jarr after the letter, by a kasra", "Cer harfiyle mecrûr, kesre", extra=["huruf-jarr"]),
  HATTA_IBT(), MADI("طَلَعَ", "talaa"), FAIL("الْفَجْرُ", "fajr", punct="،"),
  tok("وَالْأَطْفَالُ", "atfal", "noun", ["al-hal-jumla-wa-rabituha", "mubtada-khabar", "jam-taksir"], "الْوَاوُ حَالِيَّةٌ، وَالْأَطْفَالُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw opens a hal clause; «the children» is its mubtada, in raf' — the clause is a hal, in the seat of nasb.", "Hâl vâvı; «çocuklar» mübtedâ, merfû — cümle hâl, mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("الْأَطْفَالُ", "atfal", "noun")]),
  MUDARI5("يَبْكُونَ", "baka", ["naqis-verbs"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ", role_en="; the clause is the predicate, in the seat of raf'", role_tr="; cümle haber, mahallen merfû"),
  MINA(), MAJR("الْجُوعِ", "ju"), INDA(),
  tok("قَدَمَيَّ", "qadam", "noun", ["idafa-definiteness", "al-muthanna", "ya-al-mutakallim", "al-bariz-al-muttasil"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَأُدْغِمَتْ يَاءُ الْمُثَنَّى فِي يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The second term of the idafa, in jarr by the ya of the dual; its nun dropped for the annexation and the dual's ya merged into the speaker's ya, itself the second term of a further idafa, in the seat of jarr.",
      "Muzâfun ileyh; tesniye yâ'sıyla mecrûr; nûnu izâfet için düştü, tesniye yâ'sı mütekellim yâ'sına idgâm edildi; yâ muzâfun ileyh, mahallen mecrûr.", punct=".")]})
S2.append({"id": "s5", "translation": {"en": "When the two of them awoke they drank their milk.", "tr": "İkisi uyanınca sütlerini içtiler."},
 "tokens": [LAMMA2("فَلَمَّا"), DUAL_MADI("نَهَضَا", "nahada", note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), DUAL_MADI("شَرِبَا", "shariba"), ENC_NOUN("لَبَنَهُمَا", "laban", "هُمَا", "maful", punct=".")]})
S2.append({"id": "s6", "translation": {"en": "O God, if I did that for Your sake alone, then open a way for us out of this rock.", "tr": "Allah'ım, eğer bunu sırf Senin rızân için yaptıysam, bize bu kayadan bir yol aç."},
 "tokens": [ALLAHUMMA(punct="،"), IN_SH(), KUNTU(), FAALTU_KH(), DHALIKA_MAF(), LI_WAJHIKA(), FAFTAH(), LANA(), MIN(), HADHIHI_J(), SAKHRA_BADAL_J(punct=".")]})
S2.append({"id": "s7", "translation": {"en": "The rock moved a little, but they could not get out.", "tr": "Kaya biraz kımıldadı, fakat çıkmaya güçleri yetmedi."},
 "tokens": [TAHARRAKAT(), SAKHRA_F(),
  tok("قَلِيلًا", "qalil", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ: تَحَرُّكًا قَلِيلًا.",
      "Standing in for the absolute object, in nasb — an adjective of an omitted masdar: «a little moving».", "Mef'ûlün mutlakın nâibi, mansûb — hazfedilen masdarın sıfatı: «az bir hareket».", punct="،"),
  INNA_ENC("وَلَكِنَّهُمْ", "هُمْ", " («fakat onlar»)"), LAM_JAZM(), YAQDIRU(), ALA(), MAJR("الْخُرُوجِ", "khuruj", punct=".")]})

# ---- Chapter 3 — تَرْكُ الْحَرَامِ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "The second said: O God, I had a cousin who was the dearest of people to me; I asked of her a forbidden thing, and she refused.", "tr": "İkincisi dedi ki: Allah'ım, bir amca kızım vardı; insanların bana en sevgilisiydi. Ondan haram bir şey istedim, o ise reddetti."},
 "tokens": [QALA("وَقَالَ"),
  tok("الثَّانِي", "thani", "noun", ["fail", "ism-maqsur-manqus"], "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ — اسْمٌ مَنْقُوصٌ.", "The doer, in raf' by a damma estimated on the ya — a manqus noun.", "Fâil; yâ üzerinde takdîrî damme ile merfû — ism-i menkûs.", punct=":"),
  ALLAHUMMA(), INNAHU_SHAN(), KANA("كَانَتْ", fem=True),
  JARR_PRON("لِي", "li", "لِ", "ي", " («benim»)", note_ar=KH_MUQ[0], note_en=KH_MUQ[1], note_tr=KH_MUQ[2]),
  tok("بِنْتُ", "bint", "noun", ["kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ.", "The noun of كَانَ, placed after its predicate, in raf'; annexed.", "Kâne'nin ismi (haberinden sonra), merfû; muzâf."),
  MUDAF_ILAYH("عَمٍّ", "amm-uncle"),
  tok("كَانَتْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "jumla-sifa"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِبِنْتِ عَمٍّ.",
      "كَانَ built on fatha with the feminine ta; its noun is a hidden «she» — the clause qualifies «a cousin», in the seat of raf'.", "Fetha üzere mebnî nâkıs kâne, tâ te'nîs; ismi gizli «o» — cümle «amca kızı»nın sıfatı, mahallen merfû."),
  tok("أَحَبَّ", "ahabb", "noun", ["kana-wa-akhawatuha", "ism-tafdil", "mamnu-min-sarf", "idafa-definiteness"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ.",
      "The predicate of كَانَ, in nasb; annexed — an elative on أَفْعَل («the dearest of»).", "Kâne'nin haberi, mansûb; muzâf — ef'al vezninde ism-i tafdîl («en sevgilisi»)."),
  MUDAF_ILAYH("النَّاسِ", "nas"), ILAYYA(punct="،"),
  MADI_T("فَطَلَبْتُ", "talaba", who="ana"), JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)"), MAFUL("أَمْرًا", "amr"), NAAT("حَرَامًا", "haram-fiqh", "nasb"),
  tok("فَأَبَتْ", "aba", "verb", ["naqis-verbs"], FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.",
      "The fa conjoins; past verb built on a fatha estimated on the alif, which dropped before the feminine ta (two quiescents); the doer «she» is hidden.", "Fâ atıf; te'nîs tâ'sı önünde (iki sâkin) düşen elif üzerindeki takdîrî fetha ile mebnî mâzî; fâil gizli «o».",
      punct=".", segments=[seg("فَ", "fa", "conj"), seg("أَبَتْ", "aba", "verb")])]})
S3.append({"id": "s2", "translation": {"en": "Then after some years she came to me, hunger having pressed her hard, and I gave her a hundred dinars on condition that she do what I wanted.", "tr": "Sonra yıllar geçince bana geldi; açlık ona iyice bastırmıştı. İstediğimi yapması şartıyla ona yüz dinar verdim."},
 "tokens": [THUMMA(),
  NUN_WIQ_VERB("جَاءَتْنِي", "jaa", ["hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ", "Past verb built on fatha with the feminine ta; the doer «she» is hidden", "Fetha üzere mebnî mâzî, tâ te'nîs; fâil gizli «o»", stem="جَاءَتْ"),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  tok("سَنَوَاتٍ", "sana", "noun", ["idafa-definiteness", "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ لِسَنَةٍ، رُدَّتْ فِيهِ لَامُهَا الْمَحْذُوفَةُ (الْوَاوُ).",
      "The second term, in jarr — the sound feminine plural of «year», in which its lost third radical (the waw) returns.", "Muzâfun ileyh, mecrûr — senenin cem-i müennes sâlimi; düşmüş lâmı (vâv) geri gelir."),
  WA_QAD(),
  tok("اشْتَدَّ", "ishtadda", "verb", ["form-viii-verbs", "doubled-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مُضَاعَفٌ عَلَى افْتَعَلَ، أُدْغِمَتْ لَامُهُ فِي عَيْنِهِ.", "Past verb built on fatha — a doubled root on اِفْتَعَلَ, its last two radicals merged.", "Fetha üzere mebnî mâzî — iftiale vezninde muzâaf; lâmı aynına idgâm edilmiş."),
  JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («ona»)"), FAIL("الْجُوعُ", "ju", punct="،"),
  MADI_T("فَأَعْطَيْتُهَا", "aata", who="ana", enc="هَا", extra=["naqis-verbs", "form-iv-verbs", "mafulayn"]),
  tok("مِائَةَ", "mia", "noun", ["maful-bihi", "mafulayn", "asma-al-adad-fil-kafiya", "idafa-definiteness"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — الْمِائَةُ تُضَافُ إِلَى مُفْرَدٍ مَجْرُورٍ.",
      "The second object, in nasb, annexed — «a hundred» is annexed to a singular in jarr.", "İkinci mef'ûlün bih, mansûb, muzâf — yüz, müfred mecrûra muzâf olur."),
  MUDAF_ILAYH("دِينَارٍ", "dinar", note_ar=" — مَعْدُودُ الْمِائَةِ مُفْرَدٌ مَجْرُورٌ", note_en=" — the counted noun of «hundred», a singular in jarr", note_tr=" — yüzün ma'dûdu, müfred mecrûr"),
  ALA(), AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِعَلَى: عَلَى فِعْلِهَا", "; the clause it builds is in jarr after عَلَى: «on condition of her doing»", "; müevvel masdar alâ ile mecrûr: «yapması şartıyla»"),
  MANSUB_AN("تَفْعَلَ", "faala", who="هِيَ"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "anwa-ma"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَجُمْلَةُ أُرِيدُ صِلَتُهُ، وَالْعَائِدُ مَحْذُوفٌ: مَا أُرِيدُهُ.",
      "A relative pronoun built on sukun, in the seat of nasb as the object; «I want» is its clause and the returning pronoun is omitted («what I want [it]»).", "İsm-i mevsûl, sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb; «istiyorum» sılası, âid zamir hazfedilmiş."),
  MUDARI("أُرِيدُ", "arada", ["form-iv-verbs", "hollow-verbs"], who="أَنَا", wujub=True, punct=".")]})
S3.append({"id": "s3", "translation": {"en": "When I had her in my power she said: Fear God, and do not take what is not yours by right.", "tr": "Ona güç yetirdiğimde dedi ki: Allah'tan kork, hakkın olmayan şeyi alma."},
 "tokens": [LAMMA2("فَلَمَّا"), MADI_T("قَدَرْتُ", "qadara", who="ana", note_ar=LAMMA_CL[0], note_en=LAMMA_CL[1], note_tr=LAMMA_CL[2]), JARR_PRON("عَلَيْهَا", "ala", "عَلَيْ", "هَا", " («ona»)"),
  QALAT("قَالَتْ", punct=":"),
  tok("اتَّقِ", "ittaqa", "verb", ["imperative-amr", "form-viii-verbs", "naqis-verbs", "al-fail-al-mudmar-al-mustatir-wujuban"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ (الْيَاءِ)، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ — مِنِ اتَّقَى عَلَى افْتَعَلَ، وَأَصْلُهُ اِوْتَقَى.",
      "An imperative built on the dropped weak letter (the ya); the doer «you» must stay hidden — from اِتَّقَى on اِفْتَعَلَ, whose waw turned into the ta.", "İllet harfinin (yâ) düşmesi üzere mebnî emir; fâil «sen» vücûben müstetir — iftiale vezninde ittekâ; aslı ivtekâ."),
  ALLAH_MAF(punct="،"), WA_LA_NAHIYA(),
  tok("تَأْخُذْ", "akhadha", "verb", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.",
      "Present verb in jazm after the prohibitive لَا, its sign the sukun; the doer «you» must stay hidden.", "Nehiy lâ'sı ile meczûm muzâri, alâmeti sükûn; fâil «sen» vücûben müstetir."),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَجُمْلَةُ لَيْسَ صِلَتُهُ.", "A relative pronoun, in the seat of nasb as the object; the clause of لَيْسَ is its clause.", "İsm-i mevsûl, mef'ûlün bih olarak mahallen mansûb; leyse cümlesi sılasıdır."),
  tok("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-afal-al-naqisa-fil-kafiya"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ لِلنَّفْيِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى مَا.", "The frozen defective verb of negation; its noun is a hidden «it» referring back to مَا.", "Nefiy bildiren câmid nâkıs fiil; ismi gizli «o», mâ'ya râci."),
  JARR_PRON("لَكَ", "li", "لَ", "كَ", " («senin»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ لَيْسَ", note_en="; the phrase is the predicate of لَيْسَ, in the seat of nasb", note_tr="; câr-mecrûr leyse'nin haberi, mahallen mansûb"),
  BI_NOUN("بِحَقٍّ", "haqq", "حَقٍّ", punct=".", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِخَبَرِ لَيْسَ", note_en=" — hanging on the predicate of لَيْسَ", note_tr=" — leyse'nin haberine müteallık")]})
S3.append({"id": "s4", "translation": {"en": "So I rose and left her, and I left her the gold, though she was the dearest of people to me.", "tr": "Bunun üzerine kalkıp ondan uzaklaştım ve altını ona bıraktım; oysa o, insanların bana en sevgilisiydi."},
 "tokens": [tok("فَقُمْتُ", "qama", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail"],
      FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — أَجْوَفُ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ وَضُمَّ أَوَّلُهُ دَلَالَةً عَلَى الْوَاوِ.",
      "The fa conjoins; past verb built on sukun before the ta of the doer — a hollow verb whose middle letter dropped where two quiescents met, the damma on its first letter pointing to the lost waw.",
      "Fâ atıf; fâil tâ'sı bitiştiği için sükûn üzere mebnî — ecvef; iki sâkin karşılaşınca aynı düştü, ilk harfin dammesi düşen vâva delâlet eder.", segments=[seg("فَ", "fa", "conj"), seg("قُمْتُ", "qama", "verb")]),
  JARR_PRON("عَنْهَا", "an", "عَنْ", "هَا", " («ondan»)"), MADI_T("وَتَرَكْتُ", "taraka", who="ana"), JARR_PRON("لَهَا", "li", "لَ", "هَا", " («ona»)"), MAFUL("الذَّهَبَ", "dhahab-gold", punct="،"),
  tok("وَهِيَ", "hiya", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar", "al-hal-jumla-wa-rabituha"], "الْوَاوُ حَالِيَّةٌ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ.",
      "The waw opens a hal clause; «she» is a detached pronoun built on fatha, the mubtada in the seat of raf' — the clause is a hal, in the seat of nasb.", "Hâl vâvı; «o» munfasıl zamir, fetha üzere mebnî, mübtedâ — cümle hâl, mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")]),
  tok("أَحَبُّ", "ahabb", "noun", ["mubtada-khabar", "ism-tafdil", "idafa-definiteness"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — اسْمُ تَفْضِيلٍ.", "The predicate, in raf'; annexed — an elative.", "Haber, merfû; muzâf — ism-i tafdîl."),
  MUDAF_ILAYH("النَّاسِ", "nas"), ILAYYA(punct=".")]})
S3.append({"id": "s5", "translation": {"en": "O God, if I did that out of fear of You, then open a way for us.", "tr": "Allah'ım, eğer bunu Senden korktuğum için yaptıysam, bize bir yol aç."},
 "tokens": [ALLAHUMMA(punct="،"), IN_SH(), KUNTU(), FAALTU_KH(), DHALIKA_MAF(),
  tok("خَوْفًا", "khawf", "noun", ["maful-lah", "al-maful-fih-wal-maful-lah"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ بِالْفَتْحَةِ — مَصْدَرٌ قَلْبِيٌّ يُبَيِّنُ عِلَّةَ الْفِعْلِ، مُشَارِكٌ لَهُ فِي الْوَقْتِ وَالْفَاعِلِ.",
      "The maf'ul li-ajlih (object of cause), in nasb — a masdar of the heart giving the reason for the act, sharing its time and its doer.", "Mef'ûlün lieclih, mansûb — fiilin sebebini bildiren kalbî masdar; fiille zamanda ve fâilde ortak."),
  JARR_PRON("مِنْكَ", "min", "مِنْ", "كَ", " («Senden»)"), FAFTAH(), LANA(punct=".")]})
S3.append({"id": "s6", "translation": {"en": "The rock moved once more, but they were not able to get out.", "tr": "Kaya bir kez daha kımıldadı, fakat çıkmaya güçleri yetmedi."},
 "tokens": [TAHARRAKAT(), SAKHRA_F(),
  tok("مَرَّةً", "marra-once", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq"], "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ بِالْفَتْحَةِ لِبَيَانِ الْعَدَدِ.", "An absolute object counting the occurrence, in nasb.", "Sayı bildiren mef'ûlün mutlak, mansûb."),
  tok("أُخْرَى", "ukhra", "noun", ["naat-sifa", "ism-maqsur-manqus", "mamnu-min-sarf"], "نَعْتٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مُؤَنَّثُ آخَرَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ.",
      "An adjective in nasb by a fatha estimated on the alif — the feminine of آخَر, barred from tanwin by its feminine alif.", "Na't; elif üzerinde takdîrî fetha ile mansûb — âhar'ın müennesi, te'nîs elifi yüzünden gayr-ı munsarif.", punct="،"),
  INNA_ENC("وَلَكِنَّهُمْ", "هُمْ", " («fakat onlar»)"), LAM_JAZM(),
  tok("يَسْتَطِيعُوا", "istataa", "verb", ["nawasib-wa-jawazim-al-mudari", "afal-khamsa", "form-x-verbs", "hollow-verbs", "al-bariz-al-muttasil"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ.",
      "Present verb in jazm after لَمْ, its sign the dropped nun; the waw is the doer, in the seat of raf'.", "Lem ile meczûm muzâri, alâmeti nûnun düşmesi; vâv fâil, mahallen merfû."),
  MAFUL("الْخُرُوجَ", "khuruj", punct=".")]})

# ---- Chapter 4 — الْأَمَانَةُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "The third said: O God, I had hired men working for me, and I paid them their wages — all but one man, who left his wage and went away.", "tr": "Üçüncüsü dedi ki: Allah'ım, benim için çalışan ücretli işçilerim vardı; ücretlerini verdim. Yalnız bir adam ücretini bırakıp gitti."},
 "tokens": [QALA("وَقَالَ"), FAIL("الثَّالِثُ", "thalith", punct=":"), ALLAHUMMA(), INNAHU_SHAN(), KANA("كَانَ"),
  YA_NOUN("عِنْدِي", "inda", "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ", "An adverb of place, in nasb by a fatha", "Mekân zarfı, fetha ile mansûb;", extra=["maful-fih", "kana-wa-akhawatuha"]),
  tok("أُجَرَاءُ", "ajir", "noun", ["kana-wa-akhawatuha", "jam-taksir", "mamnu-min-sarf", "ism-mamdud"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ لِأَجِيرٍ عَلَى فُعَلَاءَ، مَمْنُوعٌ مِنَ الصَّرْفِ لِأَلِفِ التَّأْنِيثِ الْمَمْدُودَةِ؛ وَالظَّرْفُ قَبْلَهُ خَبَرُهَا الْمُقَدَّمُ.",
      "The noun of كَانَ, placed after its predicate, in raf' — the broken plural of «hired man» on فُعَلَاء, barred from tanwin by its lengthened feminine alif; the adverb before it is the fronted predicate.",
      "Kâne'nin ismi (haberinden sonra), merfû — ecîrin fuâlâ' vezninde cem-i teksîri; memdûd te'nîs elifi yüzünden gayr-ı munsarif; önceki zarf öne alınmış haberidir."),
  MUDARI5("يَعْمَلُونَ", "amila", role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِأُجَرَاءَ", role_en="; the clause qualifies «hired men», in the seat of raf'", role_tr="; cümle «ücretliler»in sıfatı, mahallen merfû"),
  JARR_PRON("لِي", "li", "لِ", "ي", " («benim için»)", punct="،"),
  MADI_T("فَأَعْطَيْتُهُمْ", "aata", who="ana", enc="هُمْ", extra=["naqis-verbs", "form-iv-verbs", "mafulayn"]),
  ENC_NOUN("أَجْرَهُمْ", "ajr", "هُمْ", "maful", note_ar=" — وَهُوَ الْمَفْعُولُ الثَّانِي", note_en=" — the second object", note_tr=" — ikinci mef'ûl"),
  tok("إِلَّا", "illa", "part", ["istithna", "al-mustathna-wa-nawah-wa-nasbuh"], "أَدَاةُ اسْتِثْنَاءٍ، وَالْكَلَامُ تَامٌّ مُوجَبٌ فَيَجِبُ نَصْبُ الْمُسْتَثْنَى.", "The particle of exception; the sentence is complete and affirmative, so the excepted noun must take nasb.", "İstisnâ edatı; cümle tam ve müsbet olduğu için müstesnâ mansûb olur."),
  tok("رَجُلًا", "rajul", "noun", ["istithna", "al-mustathna-wa-nawah-wa-nasbuh"], "مُسْتَثْنًى بِإِلَّا مَنْصُوبٌ بِالْفَتْحَةِ.", "The excepted noun after إِلَّا, in nasb.", "İllâ ile müstesnâ, mansûb."),
  NAAT("وَاحِدًا", "wahid", "nasb"),
  MADI("تَرَكَ", "taraka", hidden=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِرَجُلٍ", note_en="; the clause qualifies «a man», in the seat of nasb", note_tr="; cümle «adam»ın sıfatı, mahallen mansûb"),
  ENC_NOUN("أَجْرَهُ", "ajr", "هُ", "maful"), MADI("وَذَهَبَ", "dhahaba", hidden=True, punct=".")]})
S4.append({"id": "s2", "translation": {"en": "With his wage I bought sheep, and they multiplied until they became great wealth of camels, cattle and sheep.", "tr": "Onun ücretiyle koyun aldım; çoğaldılar, nihayet develerden, sığırlardan ve koyunlardan oluşan büyük bir mal oldular."},
 "tokens": [MADI_T("فَاشْتَرَيْتُ", "ishtara", who="ana", extra=["form-viii-verbs", "naqis-verbs"]), BI_NOUN("بِأَجْرِهِ", "ajr", "أَجْرِهِ", enc="هِ"), MAFUL("غَنَمًا", "ghanam", punct="،"),
  MADI("فَكَثُرَتْ", "kathura", fem=True, hidden=True), HATTA_IBT(),
  tok("صَارَتْ", "sara", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "صَارَ فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هِيَ.",
      "صَارَ «became», one of كَانَ's sisters, built on fatha with the feminine ta; its noun is a hidden «they (the sheep)».", "Kâne'nin kardeşlerinden sâre «oldu»; fetha üzere mebnî, tâ te'nîs; ismi gizli «o (koyunlar)»."),
  tok("أَمْوَالًا", "mal", "noun", ["kana-wa-akhawatuha", "jam-taksir"], "خَبَرُ صَارَ مَنْصُوبٌ بِالْفَتْحَةِ — جَمْعُ تَكْسِيرٍ لِمَالٍ.", "The predicate of صَارَ, in nasb — the broken plural of «property».", "Sâre'nin haberi, mansûb — mâlin cem-i teksîri."),
  NAAT("كَثِيرَةً", "kathir", "nasb"), MINA(), MAJR("الْإِبِلِ", "ibil"), ATF("وَالْبَقَرِ", "baqar", "noun", "jarr"), ATF("وَالْغَنَمِ", "ghanam", "noun", "jarr", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "After some years he came to me and said: O servant of God, give me my wage.", "tr": "Yıllar sonra bana geldi ve dedi ki: Ey Allah'ın kulu, ücretimi ver."},
 "tokens": [NUN_WIQ_VERB("فَجَاءَنِي", "jaa", ["hollow-verbs"], FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", "The fa conjoins; past verb built on fatha, the doer «he» hidden", "Fâ atıf; fetha üzere mebnî mâzî, fâil gizli «o»", stem="جَاءَ"),
  ZARF("بَعْدَ", "bada", **ZAMAN),
  tok("سِنِينَ", "sana", "noun", ["idafa-definiteness", "al-jam-al-salim-fil-kafiya", "jam-mudhakkar-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ.", "The second term, in jarr by the ya — a plural attached to the sound masculine plural in its declension.", "Muzâfun ileyh, yâ ile mecrûr — cem-i müzekker sâlime mülhak."),
  QALA("وَقَالَ", hidden=True, punct=":"), YA(),
  tok("عَبْدَ", "abd", "noun", ["vocative-munada", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "A vocative in annexation, in nasb.", "Muzâf münâdâ, mansûb."), ALLAH_MI(punct="،"),
  AMR("أَعْطِنِي", "aata", ["form-iv-verbs", "naqis-verbs"], enc="نِي", wiqaya=True, built="حَذْفِ حَرْفِ الْعِلَّةِ (الْيَاءِ)", built_en="the dropped weak letter (the ya)", built_tr="illet harfinin (yâ) düşmesi"),
  YA_NOUN("أَجْرِي", "ajr", "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِفَتْحَةٍ", "The second object, in nasb by a fatha", "İkinci mef'ûlün bih, fetha ile mansûb;", extra=["maful-bihi", "mafulayn"], punct=".")]})
S4.append({"id": "s4", "translation": {"en": "I said to him: All that you see of this wealth is your wage, so take it, all of it.", "tr": "Ona dedim ki: Bu mallardan gördüğün her şey senin ücretindir; al, hepsini al."},
 "tokens": [tok("فَقُلْتُ", "qala", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
      FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَمَقُولُ الْقَوْلِ بَعْدَ النُّقْطَتَيْنِ مَفْعُولٌ بِهِ.",
      "The fa conjoins; past verb built on sukun before the ta of the doer (its middle letter dropped where two quiescents met); what is said follows the colon as the object.", "Fâ atıf; fâil tâ'sı bitiştiği için sükûn üzere mebnî (iki sâkin karşılaşınca aynı düştü); mekûlü'l-kavl iki noktadan sonra mef'ûlün bihtir.",
      segments=[seg("فَ", "fa", "conj"), seg("قُلْتُ", "qala", "verb")]),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)", punct=":"),
  MUBTADA("كُلُّ", "kull", note_ar="، مُضَافٌ", note_en=", annexed", note_tr=", muzâf"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَجُمْلَةُ تَرَى صِلَتُهُ، وَالْعَائِدُ مَحْذُوفٌ.",
      "A relative pronoun, in the seat of jarr as the second term of the idafa; «you see» is its clause, the returning pronoun omitted.", "İsm-i mevsûl; muzâfun ileyh olarak mahallen mecrûr; «görüyorsun» sılası, âid hazfedilmiş."),
  MUDARI("تَرَى", "raa", ["naqis-verbs"], who="أَنْتَ", naqis="ا", wujub=True), MIN(), HADHIHI_J(), BADAL("الْأَمْوَالِ", "mal", "jarr", extra=["jam-taksir"]),
  tok("أَجْرُكَ", "ajr", "noun", ["mubtada-khabar", "idafa-definiteness", "al-bariz-al-muttasil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The predicate, in raf'; annexed to the attached «your», which fills the seat of jarr.", "Haber, merfû; muzâf, bitişik kâf zamiri muzâfun ileyh — mahallen mecrûr.", punct="،", segments=[seg("أَجْرُ", "ajr", "noun"), seg("كَ", "pron-2ms", "pron")]),
  AMR("فَخُذْهَا", "akhadha", enc="هَا", note_ar=" — وَحُذِفَتْ هَمْزَةُ أَخَذَ فِي الْأَمْرِ تَخْفِيفًا", note_en=" — the hamza of أَخَذَ drops in the imperative", note_tr=" — ehaze'nin hemzesi emirde düşer"),
  tok("كُلَّهَا", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"], "تَوْكِيدٌ مَعْنَوِيٌّ لِلضَّمِيرِ «هَا» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A tawkid of meaning strengthening the pronoun «it», in nasb; annexed to the attached pronoun, which is the second term.", "«Onu» zamirini pekiştiren ma'nevî te'kîd, mansûb; muzâf, bitişik zamir muzâfun ileyh.", punct=".", segments=[seg("كُلَّ", "kull", "noun"), seg("هَا", "pron-3fs", "pron")])]})
S4.append({"id": "s5", "translation": {"en": "He said: O servant of God, do not mock me!", "tr": "Dedi ki: Ey Allah'ın kulu, benimle alay etme!"},
 "tokens": [QALA("فَقَالَ", hidden=True, punct=":"), YA(),
  tok("عَبْدَ", "abd", "noun", ["vocative-munada", "idafa-definiteness"], "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ.", "A vocative in annexation, in nasb.", "Muzâf münâdâ, mansûb."), ALLAH_MI(punct="،"),
  LA_NAHIYA(),
  tok("تَسْخَرْ", "sakhira", "verb", ["nawasib-wa-jawazim-al-mudari", "la-nahiya"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.",
      "Present verb in jazm after the prohibitive لَا, its sign the sukun; the doer «you» must stay hidden.", "Nehiy lâ'sı ile meczûm muzâri, alâmeti sükûn; fâil «sen» vücûben müstetir."),
  tok("مِنِّي", "min", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"], "مِنْ حَرْفُ جَرٍّ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ، وَأُدْغِمَتْ نُونُ مِنْ فِي نُونِ الْوِقَايَةِ.",
      "The jarr letter مِنْ; the nun guards it and the speaker's ya fills the seat of jarr — the nun of مِنْ merges into the guarding nun.", "Min cer harfi; nûn vikâye, mütekellim yâ'sı mahallen mecrûr — min'in nûnu vikâye nûnuna idgâm edildi.", punct="!",
      segments=[seg("مِنْ", "min", "prep"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])]})
S4.append({"id": "s6", "translation": {"en": "I said: I am not mocking you. So he took it all and drove it off, and left nothing of it behind.", "tr": "Dedim ki: Seninle alay etmiyorum. Bunun üzerine hepsini aldı ve sürüp götürdü; ondan hiçbir şey bırakmadı."},
 "tokens": [tok("فَقُلْتُ", "qala", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail", "maful-bihi"],
      FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَمَقُولُ الْقَوْلِ بَعْدَ النُّقْطَتَيْنِ.",
      "The fa conjoins; past verb built on sukun before the ta of the doer; what is said follows the colon.", "Fâ atıf; fâil tâ'sı bitiştiği için sükûn üzere mebnî; mekûlü'l-kavl iki noktadan sonra gelir.", punct=":",
      segments=[seg("فَ", "fa", "conj"), seg("قُلْتُ", "qala", "verb")]),
  tok("إِنِّي", "inna", "part", ["inna-wa-akhawatuha", "al-bariz-al-muttasil", "ya-al-mutakallim"], "إِنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا، وَحُذِفَتْ نُونُ الْوِقَايَةِ تَخْفِيفًا — وَالْجُمْلَةُ بَعْدَهَا خَبَرُهَا.",
      "إِنَّ with the speaker's ya as its noun, in the seat of nasb (the guarding nun is dropped for lightness); the clause after it is its predicate.", "İnne; mütekellim yâ'sı ismi, mahallen mansûb (vikâye nûnu hafiflik için düşmüş); sonraki cümle haberi.",
      segments=[seg("إِنَّ", "inna", "part"), seg("ي", "pron-1s", "pron")]),
  LA_NAFIYA(),
  MUDARI("أَسْخَرُ", "sakhira", who="أَنَا", wujub=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ", note_en="; the clause is the predicate of إِنَّ, in the seat of raf'", note_tr="; cümle inne'nin haberi, mahallen merfû"),
  JARR_PRON("مِنْكَ", "min", "مِنْ", "كَ", " («seninle»)", punct="."),
  ENC_MADI("فَأَخَذَهَا", "akhadha", "هَا", hidden=True),
  tok("كُلَّهَا", "kull", "noun", ["tawkid", "al-tawkid-al-lafzi-wal-manawi", "idafa-definiteness", "al-bariz-al-muttasil"], "تَوْكِيدٌ مَعْنَوِيٌّ لِلْمَفْعُولِ «هَا» مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.",
      "A tawkid of meaning strengthening the object «it», in nasb; annexed to the attached pronoun.", "Mef'ûl «onu» zamirini pekiştiren ma'nevî te'kîd, mansûb; muzâf, zamir muzâfun ileyh.", segments=[seg("كُلَّ", "kull", "noun"), seg("هَا", "pron-3fs", "pron")]),
  ENC_MADI("وَسَاقَهَا", "saqa", "هَا", hidden=True, extra=["hollow-verbs"], punct="،"), WA_LAM(),
  tok("يَتْرُكْ", "taraka", "verb", ["nawasib-wa-jawazim-al-mudari", "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Present verb in jazm after لَمْ, its sign the sukun; the doer «he» is hidden.", "Lem ile meczûm muzâri, alâmeti sükûn; fâil gizli «o»."),
  JARR_PRON("مِنْهَا", "min", "مِنْ", "هَا", " («ondan»)"), MAFUL("شَيْئًا", "shay", punct=".")]})
S4.append({"id": "s7", "translation": {"en": "O God, if I did that for Your sake alone, then open for us what remains.", "tr": "Allah'ım, eğer bunu sırf Senin rızân için yaptıysam, kalanı da bize aç."},
 "tokens": [ALLAHUMMA(punct="،"), IN_SH(), KUNTU(), FAALTU_KH(), DHALIKA_MAF(), LI_WAJHIKA(), FAFTAH(), LANA(),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَجُمْلَةُ بَقِيَ صِلَتُهُ، وَالْعَائِدُ هُوَ الْفَاعِلُ الْمُسْتَتِرُ.",
      "A relative pronoun, the object in the seat of nasb; «remains» is its clause, and the returning pronoun is its hidden doer.", "İsm-i mevsûl, mef'ûlün bih — mahallen mansûb; «kaldı» sılası, âid gizli fâildir."),
  tok("بَقِيَ", "baqiya", "verb", ["naqis-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الظَّاهِرِ عَلَى الْيَاءِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.", "Past verb built on a fatha written on the ya; the doer «it» is hidden.", "Yâ üzerinde zâhir fetha ile mebnî mâzî; fâil gizli «o».", punct=".")]})
S4.append({"id": "s8", "translation": {"en": "The rock moved and fell away from the mouth of the cave, and they walked out of it.", "tr": "Kaya kımıldadı ve mağaranın ağzından düştü; onlar da yürüyerek oradan çıktılar."},
 "tokens": [TAHARRAKAT(), SAKHRA_F(), MADI("وَسَقَطَتْ", "saqata", fem=True, hidden=True), PREP("عَنْ", "an", gloss_tr="«-den»"),
  MAJR("بَابِ", "bab", note_ar="، مُضَافٌ", note_en="; annexed", note_tr="; muzâf"), MUDAF_ILAYH("الْغَارِ", "ghar", punct="،"),
  VERB_WAW("فَخَرَجُوا", "kharaja"), MINHU(),
  MUDARI5("يَمْشُونَ", "masha", ["naqis-verbs"], role_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ", role_en="; the clause is a hal, in the seat of nasb", role_tr="; cümle hâl, mahallen mansûb", punct=".")]})

CHAPTERS = [
 ("ch1", {"ar": "الْغَارُ وَالصَّخْرَةُ", "en": "The Cave and the Rock", "tr": "Mağara ve Kaya"}, S1),
 ("ch2", {"ar": "بِرُّ الْوَالِدَيْنِ", "en": "Kindness to Parents", "tr": "Ana-Babaya İyilik"}, S2),
 ("ch3", {"ar": "تَرْكُ الْحَرَامِ", "en": "Leaving the Forbidden", "tr": "Haramı Terk"}, S3),
 ("ch4", {"ar": "الْأَمَانَةُ", "en": "Trustworthiness", "tr": "Emanet"}, S4),
]
TITLES = [c[1] for c in CHAPTERS]
CHAPS = [c[2] for c in CHAPTERS]

# ---- the glossary: copied from the packages that own each key (the lemma-identity rule); three entries are new
PREF = ["juha-wa-al-himar", "al-asad-wa-al-arnab", "habil-wa-qabil", "adam-wa-iblis", "shuayb-wa-ahl-madyan", "zakariyya-wa-yahya", "ayyub-wa-al-sabr",
        "dhu-al-qarnayn-wa-al-sadd", "luqman-wa-ibnuh", "qarun-wa-kunuzuh", "ashab-al-kahf", "dawud-wa-jalut", "hud-wa-aad", "sulayman-wa-al-hudhud",
        "salih-wa-al-naqa", "nuh-wa-al-safina", "musa-fi-madyan", "musa-wal-khadir", "musa-wa-bani-israil", "musa-wa-firawn", "yunus-wa-al-hut", "ashab-al-fil",
        "qisas-al-nabiyyin-1", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "jumal-al-tadrib", "wasiyyat-abi-hanifa-L2", "talkhis-al-miftah", "al-kafiya",
        "izhar-al-asrar", "aqaid-ahl-al-sunna", "wasiyyat-abi-hanifa-samti", "wasiyyat-abi-yusuf-L5", "kitab-al-waqf", "mukhtasar-al-manar", "kitab-al-sulh",
        "kitab-al-buyu", "kitab-al-kaffarat", "bad-al-amali", "min-muqaddimat-al-maqsud"]
PREF = [p for p in PREF if (ROOT / "content/samples" / p / "glossary.json").exists()]
# …and every other package on the shelf after them, so a key that lives only in one text is still found (the lemma-identity rule)
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
# keys that two packages spell alike but mean differently are pinned to the package whose sense this story uses
FORCE = {"qadara": "dhu-al-qarnayn-wa-al-sadd", "bada": "al-kafiya", "dhahab-gold": "izhar-al-asrar", "haram-fiqh": None, "la-nafiya-lil-jins": "al-kafiya",
         "ma-mawsula": "al-asad-wa-al-arnab", "lam-amr": "al-kafiya", "lam-taleel": "al-kafiya", "nun-wiqaya": "al-asad-wa-al-arnab", "allahumma": "qisas-al-nabiyyin-4",
         "amm-uncle": None, "amal-deed": None, "saqa-water": None, "marra-once": None, "sadda-block": None, "pron-1s": None, "pron-1p": None, "pron-2mp": None}
_G = {p: json.loads((ROOT / "content/samples" / p / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((ROOT / "content/samples" / p / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF}
def find_gloss(k):
    if FORCE.get(k) and k in _G[FORCE[k]]: return _G[FORCE[k]][k]
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    if FORCE.get(k) and k in _M[FORCE[k]]: return _M[FORCE[k]][k]
    for p in PREF:
        if k in _M[p]: return _M[p][k]
    return None

NEW_GLOSS = {
 "ghar": {"lemma": "غَار", "root": "غ و ر", "pos": "noun", "plural": "غِيرَان", "gloss": {"en": "cave", "tr": "mağara"}, "level": 3},
 "ajir": {"lemma": "أَجِير", "root": "أ ج ر", "pos": "noun", "plural": "أُجَرَاء", "gloss": {"en": "a hired man, labourer (فَعِيل; the plural فُعَلَاء is a diptote)", "tr": "ücretli, işçi, ecîr (faîl; çoğulu fuâlâ' gayr-ı munsariftir)"}, "level": 3},
 "halaba": {"lemma": "حَلَبَ", "root": "ح ل ب", "pos": "verb", "gloss": {"en": "to milk (an animal)", "tr": "(hayvanı) sağmak"}, "level": 3},
}
NEW_VERBS = {
 "halaba": _sg.sound1("nasara", "حَلَب", "حْلُب", "اُحْلُب", "حَلْب", "حَالِب", maful="مَحْلُوب", pmz="حُلِبَ", pmd="يُحْلَبُ", note="حَلَبَ يَحْلُبُ حَلْبًا مِنْ بَابِ نَصَرَ: اسْتَخْرَجَ اللَّبَنَ مِنَ الضَّرْعِ."),
}
used = set()
for S in CHAPS:
    for s in S:
        for t in s["tokens"]:
            used.add(t["lex"])
            for sg2 in t.get("segments", []): used.add(sg2["lex"])
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

LEVEL_NAME = json.loads((ROOT / "content/samples/qisas-al-nabiyyin-4/manifest.json").read_text(encoding="utf-8")).get("levelName", "Intermediate")
MANIFEST = {
 "id": "ashab-al-ghar",
 "storyGroup": "ashab-al-ghar",
 "title": {"ar": "أَصْحَابُ الْغَارِ", "en": "The Men in the Cave", "tr": "Mağaradakiler"},
 "subtitle": {"ar": "ثَلَاثَةُ رِجَالٍ سَدَّتْ عَلَيْهِمْ صَخْرَةٌ بَابَ الْغَارِ، فَدَعَا كُلُّ وَاحِدٍ بِأَحْسَنِ عَمَلٍ عَمِلَهُ لِوَجْهِ اللهِ — قِصَّةٌ لِلْمُسْتَوَى الثَّالِثِ",
              "en": "Three men shut in a cave by a rock, each calling on God by the best deed he did for His sake alone — a story for the third level",
              "tr": "Bir kayanın mağarada kapattığı üç adam; her biri sırf Allah rızâsı için yaptığı en güzel amelle dua eder — üçüncü seviye için bir hikâye"},
 "level": 3,
 "levelName": LEVEL_NAME,
 "version": "0.1.0",
 "published": "2026-11-08",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّالِثُ) لِخَبَرِ أَصْحَابِ الْغَارِ الَّذِي رَوَتْهُ كُتُبُ الْحَدِيثِ (الْبُخَارِيُّ وَمُسْلِمٌ)، أُلِّفَتْ بِأُسْلُوبِ الْقَارِئِ الْمُتَدَرِّجِ؛ لَيْسَ فِيهَا جُمْلَةٌ هِيَ نَصُّ حَدِيثٍ، وَلَا يَصِحُّ الِاسْتِشْهَادُ بِشَيْءٍ مِنْهَا عَلَى أَنَّهُ حَدِيثٌ. كُلُّ إِعْرَابٍ فِيهَا اجْتِهَادُ الْمُؤَلِّفِ، وَهِيَ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "ORIGINAL Level-3 graded Arabic: the narrative of the three men in the cave, preserved in the hadith collections (al-Bukhari, Muslim), RETOLD FREELY in the wording of a graded reader. No sentence here is the text of a hadith and none may be cited as one; every i'rab line is the author's own analysis, pending scholarly review.",
  "tr": "ÖZGÜN 3. seviye kolaylaştırılmış Arapça: hadis kitaplarında (Buhârî, Müslim) nakledilen mağaradaki üç adam kıssası, kolaylaştırılmış okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Buradaki hiçbir cümle bir hadisin metni değildir ve hadis olarak aktarılamaz; her i'râb satırı yazarın kendi tahlilidir ve ilmî incelemeyi beklemektedir.",
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
