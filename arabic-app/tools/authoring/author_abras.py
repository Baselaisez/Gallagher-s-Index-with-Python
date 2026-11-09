"""Author content/samples/al-abras-wa-al-aqra-wa-al-ama — «الْأَبْرَصُ وَالْأَقْرَعُ وَالْأَعْمَى», the twenty-second ORIGINAL story and the second at Level 3 (wave 115).

ORIGINAL graded Arabic: three men of the Children of Israel — a leper, a bald man and a blind man — healed and enriched, then
visited again by the angel in a poor man's form; two deny the blessing and one gives thanks. The narrative is preserved in the
ḥadīth collections (al-Bukhārī and Muslim) and is RETOLD FREELY here in a graded reader's wording: no sentence is the text of a
ḥadīth and none may be cited as one. Four chapters, twenty-two sentences (261 tokens — the angel «comes to» each man with إِلَى, so the engine reads the object of جَاءَ without guessing). Written on the authoring kit (story_kit.py); three
entries are new (أَقْرَع، شَعْر، أُولَى), none of them verbs.  Regenerate with:
python3 tools/authoring/author_abras.py
"""
import json, os, pathlib, re, sys, unicodedata

ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "al-abras-wa-al-aqra-wa-al-ama"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *      # the shared helper library (wave 113) — tools/authoring/story_kit.py
from story_kit import _pre   # the clitic peel (a private name, so the star import leaves it behind)
import sarf_gen as _sg

# ============ «الْأَبْرَصُ وَالْأَقْرَعُ وَالْأَعْمَى» — the twenty-second ORIGINAL story, the second at Level 3 (wave 115) ============
PRON.update({"نَا": "pron-1p", "ي": "pron-1s", "نِي": "pron-1s", "كَ": "pron-2ms", "كُمْ": "pron-2mp", "هِمَا": "pron-3d"})
PRON_AR.update({"نَا": "نَا", "ي": "الْيَاءُ", "نِي": "الْيَاءُ", "كَ": "الْكَافُ", "كُمْ": "كُمْ", "هِمَا": "هُمَا"})
ZAMAN = dict(kind="زَمَانٍ", kind_en="time", kind_tr="zaman")
AFAL_SIFA = ("، وَهُوَ صِفَةٌ عَلَى أَفْعَلَ مَمْنُوعَةٌ مِنَ الصَّرْفِ لِلْوَصْفِيَّةِ وَوَزْنِ الْفِعْلِ", " — an adjective on أَفْعَل, barred from tanwin as an adjective of the verb's own pattern", " — ef'al vezninde sıfat; vasfiyet ve fiil vezni sebebiyle gayr-ı munsarif")

def YA_NOUN(full, lex, role_ar, role_en, role_tr, extra=None, punct=None):
    """بَصَرِي، بَلَدِي، آبَائِي: a noun annexed to the speaker's yāʾ — its own ending is ESTIMATED on the letter before the yāʾ"""
    return tok(full, lex, "noun", (extra or []) + ["ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil", "al-taqdiri-al-thani-wal-thalith-al-mudaf-ila-al-ya-wal-mahki"],
        role_ar + " مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْكَسْرَةِ الْمُنَاسِبَةِ لِلْيَاءِ، مُضَافٌ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
        role_en + " estimated on the letter before the speaker's ya, which the kasra that suits the ya occupies; annexed to that ya, the second term of the idafa in the seat of jarr.",
        role_tr + " mütekellim yâ'sından önceki harf üzerinde takdîrî — yâ'ya uygun kesre o yeri işgal eder; muzâf, yâ muzâfun ileyh, mahallen mecrûr.",
        punct=punct, segments=[seg(full[:-1], lex, "noun"), seg("ي", "pron-1s", "pron")])
ILAYYA = lambda punct=None: tok("إِلَيَّ", "ila", "prep", ["huruf-jarr", "al-bariz-al-muttasil", "ya-al-mutakallim"],
    "حَرْفُ جَرٍّ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ، وَقُلِبَتْ أَلِفُ إِلَى يَاءً وَأُدْغِمَتْ فِي يَاءِ الضَّمِيرِ.",
    "A jarr letter; the speaker's ya fills the seat of jarr — the alif of إِلَى turns to ya and merges with the pronoun's ya.",
    "Cer harfi; mütekellim yâ'sı mahallen mecrûr — ilâ'nın elifi yâ'ya dönüp zamirin yâ'sına idgâm edildi.", punct=punct, segments=[seg("إِلَى", "ila", "prep"), seg("يَ", "pron-1s", "pron")])
AL_DIPT = ('، وَظَهَرَتِ الْكَسْرَةُ لِدُخُولِ ال عَلَى الْمَمْنُوعِ مِنَ الصَّرْفِ', ' — the kasra shows because the article lifts the bar on the diptote', ' — gayr-i munsarife harf-i tarif gelince kesre zâhir olur')   # (wave 118) the diptote under the article takes its kasra
MALAK_F = lambda punct=None: FAIL("الْمَلَكُ", "malak", punct=punct)
JAA_H = lambda full="جَاءَ": MADI(full, "jaa", ["hollow-verbs"], hidden=True)
MASAHAHU = lambda punct=None: ENC_MADI("فَمَسَحَهُ", "masaha", "هُ", hidden=True, punct=punct)
FAQAD = lambda: tok("فَقَدْ", "qad", "part", ["qad-harf"], FA_AR + "قَدْ حَرْفُ تَحْقِيقٍ.", "The fa conjoins (and gives the reason); قَدْ affirms the past.", "Fâ atıf (sebep bildirir); kad tahkîk harfi.", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")])
KARIHANI = lambda: tok("كَرِهَنِي", "kariha", "verb", ["al-bariz-al-muttasil", "maful-bihi", "ya-al-mutakallim"],
    "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ.",
    "Past verb built on fatha; the nun guards it and the speaker's ya is the object «me», fronted before the doer.", "Fetha üzere mebnî mâzî; nûn vikâye, mütekellim yâ'sı öne alınmış mef'ûlün bih «beni»; fâil sonra gelir.",
    segments=[seg("كَرِهَ", "kariha", "verb"), seg("نِ", "nun-wiqaya", "part"), seg("ي", "pron-1s", "pron")])
def AATAHU(full, note=("", "", "")):
    """وَأَعْطَاهُ / فَأَعْطَاهُ: the gift verb with its first object attached (the second follows)"""
    p, stem, sg, ar0, en0, tr0 = _pre(full)
    return tok(full, "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"],
        ar0 + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْهَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ" + note[0] + " — أَعْطَى يَتَعَدَّى إِلَى مَفْعُولَيْنِ.",
        en0 + "past verb built on a fatha estimated on the alif; the attached «him» is its FIRST object" + note[1] + " — «to give» takes two objects.",
        tr0 + "elif üzerindeki takdîrî fetha ile mebnî mâzî; bitişik «ona» birinci mef'ûlün bih" + note[2] + " — a'tâ iki mef'ûl alır.",
        segments=[s for s in [sg, seg("أَعْطَا", "aata", "verb"), seg("هُ", "pron-3ms", "pron")] if s])
HID = ("، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ", "; the doer «he» is hidden", "; fâil gizli «o»")
MAF2 = lambda full, lex, extra=None, punct=None, note_ar="", note_en="", note_tr="": tok(full, lex, "noun", ["maful-bihi", "mafulayn"] + (extra or []),
    "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ بِالْفَتْحَةِ" + note_ar + ".", "The second direct object, in nasb" + note_en + ".", "İkinci mef'ûlün bih, mansûb" + note_tr + ".", punct=punct)
HAMIL_N = lambda punct=None: NAAT("حَامِلًا", "hamil", "nasb", punct=punct, note_ar=" — صِفَةٌ تَخْتَصُّ بِالْمُؤَنَّثِ فَلَا تَلْحَقُهَا التَّاءُ", note_en=" — an adjective only a female can bear, so it takes no feminine ta", note_tr=" — yalnız dişiye mahsus sıfat olduğu için te'nîs tâ'sı almaz")
KH_MAHDHUF = lambda full, lex, taqdir_ar, taqdir_en, taqdir_tr, extra=None: tok(full, lex, "noun", ["mubtada-khabar", "hadhf-wa-taqdir"] + (extra or []),
    "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ بِالضَّمَّةِ، تَقْدِيرُهُ: " + taqdir_ar + ".", "The predicate of an omitted mubtada, in raf' — «" + taqdir_en + "».", "Hazfedilmiş mübtedânın haberi, merfû — «" + taqdir_tr + "».")
MITHLA = lambda: tok("مِثْلَ", "mithl", "noun", ["maful-mutlaq", "al-mansubat-al-maful-al-mutlaq", "idafa-definiteness"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ — صِفَةٌ لِمَصْدَرٍ مَحْذُوفٍ.",
    "Standing in for the absolute object, in nasb and annexed — an adjective of an omitted masdar («a saying like that»).", "Mef'ûlün mutlakın nâibi, mansûb, muzâf — hazfedilen masdarın sıfatı.")
DHALIKA_MI = lambda punct=None: tok("ذٰلِكَ", "dhalika", "pron", ["asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "A demonstrative built on fatha, in the seat of jarr as the second term.", "İşaret ismi, fetha üzere mebnî, muzâfun ileyh olarak mahallen mecrûr.", punct=punct)
MA_MI = lambda: tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "idafa-definiteness"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ.", "A relative pronoun in the seat of jarr as the second term; the clause after it is its clause.", "İsm-i mevsûl, muzâfun ileyh olarak mahallen mecrûr; sonraki cümle sılasıdır.")
MA_MAF = lambda note=("", "", ""): tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "maful-bihi"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ" + note[0] + ".",
    "A relative pronoun built on sukun, the object in the seat of nasb; the clause after it is its clause" + note[1] + ".", "İsm-i mevsûl, sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb; sonraki cümle sılasıdır" + note[2] + ".")
RAJUL_KH = lambda: KH_MAHDHUF("رَجُلٌ", "rajul", "أَنَا رَجُلٌ", "[I am] a man", "[ben] bir adam[ım]")
ASALUKA = lambda: tok("أَسْأَلُكَ", "saala", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"],
    "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
    "Present verb in raf'; the doer «I» must stay hidden, and the attached «you» is its first object, in the seat of nasb.", "Merfû muzâri; fâil «ben» vücûben müstetir; bitişik kâf birinci mef'ûlün bih, mahallen mansûb.",
    segments=[seg("أَسْأَلُ", "saala", "verb"), seg("كَ", "pron-2ms", "pron")])
BILLADHI = lambda: tok("بِالَّذِي", "alladhi", "pron", ["huruf-jarr", "ism-mawsul", "huruf-al-qasam-fil-kafiya"],
    "الْبَاءُ حَرْفُ قَسَمٍ وَجَرٍّ، وَالَّذِي اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَالْجُمْلَةُ بَعْدَهُ صِلَتُهُ — أَسْأَلُكَ بِاللهِ الَّذِي.",
    "The ba of oath and jarr; «He who» is a relative pronoun in the seat of jarr and the clause after it is its clause — «I ask you by God, who…».", "Kasem ve cer bâ'sı; «o ki» ism-i mevsûl, mahallen mecrûr; sonraki cümle sılasıdır — «sana … Allah adına soruyorum».",
    segments=[seg("بِ", "bi", "prep"), seg("الَّذِي", "alladhi", "pron")])
ABLUGHU = lambda full, what: MUDARI(full, "balagha", who="أَنَا", wujub=True, note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِ" + what, note_en="; the clause qualifies the indefinite noun before it, in the seat of nasb", note_tr="; cümle önceki nekre ismin sıfatı, mahallen mansûb")
BALADI = lambda punct=None: YA_NOUN("بَلَدِي", "balad", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ", "The direct object, in nasb by a fatha", "Mef'ûlün bih, fetha ile mansûb;", extra=["maful-bihi"], punct=punct)
KUNTU_SH = lambda: tok("كُنْتَ", "kana", "verb", ["kana-wa-akhawatuha", "al-majzum-wal-shart-wal-jaza", "al-bariz-al-muttasil", "hollow-verbs"],
    "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ؛ وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
    "كَانَ as the verb of the condition, built on sukun before the ta (its middle letter dropped where two quiescents met), in the seat of jazm; the ta «you» is its noun, in the seat of raf'.",
    "Şart fiili olarak kâne; tâ bitiştiği için sükûn üzere mebnî (iki sâkin karşılaşınca aynı düştü), mahallen meczûm; tâ «sen» ismi, mahallen merfû.")
KADHIBAN = lambda: tok("كَاذِبًا", "kadhib-liar", "noun", ["kana-wa-akhawatuha", "ism-fail"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — وَهُوَ اسْمُ فَاعِلٍ مِنْ كَذَبَ.", "The predicate of كَانَ, in nasb — the active participle of «to lie».", "Kâne'nin haberi, mansûb — kezebe'nin ism-i fâili.")
FASAYYARAKA = lambda: tok("فَصَيَّرَكَ", "sayyara", "verb", ["al-fa-fi-jawab-al-shart", "form-ii-verbs", "al-bariz-al-muttasil", "maful-bihi", "al-majzum-wal-shart-wal-jaza"],
    "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَصَيَّرَ فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ بِمَعْنَى الدُّعَاءِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
    "The fa introduces the answer of the condition; «may He turn you» is a past verb with the force of a prayer, the attached «you» its object and the doer after it — the clause fills the seat of jazm as the answer.",
    "Fâ şartın cevabına gelmiştir; «seni çevirsin» duâ anlamında mâzî, bitişik kâf mef'ûlün bih, fâil sonra gelir — cümle şartın cevabı olarak mahallen meczûm.",
    segments=[seg("فَ", "fa", "conj"), seg("صَيَّرَ", "sayyara", "verb"), seg("كَ", "pron-2ms", "pron")])
MA_KUNTA = lambda punct=None: [tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "huruf-jarr"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ بِإِلَى، وَجُمْلَةُ كُنْتَ صِلَتُهُ.", "A relative pronoun in the seat of jarr after إِلَى; «you were» is its clause.", "İsm-i mevsûl, ilâ ile mahallen mecrûr; «idin» sılasıdır."),
    tok("كُنْتَ", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs", "hadhf-wa-taqdir"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ اسْمُهَا، وَخَبَرُهَا مَحْذُوفٌ تَقْدِيرُهُ: عَلَيْهِ — إِلَى مَا كُنْتَ عَلَيْهِ.", "كَانَ with the ta as its noun; its predicate is omitted — «to what you were [in]».", "Kâne; tâ ismi, haberi hazfedilmiş — «üzerinde bulunduğun hale».", punct=punct)]
MISKIN_GHARIB = lambda punct=None: [RAJUL_KH(), NAAT("مِسْكِينٌ", "miskin", "raf"), NAAT("غَرِيبٌ", "gharib", "raf", punct=punct, note_ar=" ثَانٍ", note_en=" (a second one)", note_tr=" (ikinci)")]

# ---- Chapter 1 — الْمَلَكُ يَسْأَلُ ----
S1 = []
S1.append({"id": "s1", "translation": {"en": "Among the Children of Israel there were three men: a leper, a bald man and a blind man; and God wished to see what they would do with His blessing.", "tr": "İsrailoğulları arasında üç adam vardı: bir alacalı, bir kel ve bir kör. Allah, nimetiyle ne yapacaklarını görmek diledi."},
 "tokens": [KANA("كَانَ"), FI((KH_MUQ[0], KH_MUQ[1], KH_MUQ[2])),
  tok("بَنِي", "banu", "noun", ["huruf-jarr", "jam-mudhakkar-salim", "idafa-definiteness"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، مُضَافٌ.",
      "In jarr by the ya — a plural attached to the sound masculine plural in its declension, its nun dropped for the annexation; annexed.", "Yâ ile mecrûr — cem-i müzekker sâlime mülhak, nûnu izâfet için düşmüş; muzâf."),
  ISRAIL_MI(),
  tok("ثَلَاثَةُ", "thalatha", "noun", ["kana-wa-akhawatuha", "asma-al-adad-fil-kafiya", "idafa-definiteness"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — عَدَدٌ مِنَ الثَّلَاثَةِ إِلَى الْعَشَرَةِ يُضَافُ إِلَى جَمْعٍ وَيُخَالِفُ مَعْدُودَهُ فِي التَّأْنِيثِ.",
      "The noun of كَانَ, placed after its predicate, in raf' and annexed — a number from three to ten is annexed to a plural and takes the opposite gender of its counted noun.", "Kâne'nin ismi (haberinden sonra), merfû, muzâf — üçten ona kadar sayılar cemiye muzâf olur ve ma'dûduna cinsçe zıt gelir."),
  tok("رِجَالٍ", "rajul", "noun", ["idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ تَكْسِيرٍ لِرَجُلٍ.", "The second term of the idafa, in jarr — the broken plural of «man».", "Muzâfun ileyh, mecrûr — racülün cem-i teksîri.", punct=":"),
  tok("أَبْرَصُ", "abras", "noun", ["badal", "al-badal-wa-aqsamuh-wa-atf-al-bayan", "mamnu-min-sarf"], "بَدَلُ تَفْصِيلٍ مِنْ ثَلَاثَةٍ مَرْفُوعٌ بِالضَّمَّةِ" + AFAL_SIFA[0] + ".", "A badal spelling out «three», in raf'" + AFAL_SIFA[1] + ".", "«Üç»ü açan tafsîl bedeli, merfû" + AFAL_SIFA[2] + "."),
  ATF("وَأَقْرَعُ", "aqra", "noun", "raf", ["mamnu-min-sarf"], note_ar=AFAL_SIFA[0], note_en=AFAL_SIFA[1], note_tr=AFAL_SIFA[2]),
  ATF("وَأَعْمَى", "ama-blind", "noun", "raf", ["mamnu-min-sarf", "ism-maqsur-manqus"], sign="مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ", note_ar=AFAL_SIFA[0], note_en=" (the damma is estimated on the alif)" + AFAL_SIFA[1], note_tr=" (damme elif üzerinde takdîrî)" + AFAL_SIFA[2], punct="،"),
  MADI("فَأَرَادَ", "arada", ["form-iv-verbs", "hollow-verbs"]), ALLAH_F(),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِأَرَادَ", "; the clause it builds is the object of «wished»", "; kurduğu müevvel masdar «diledi»nin mef'ûlüdür"),
  tok("يَرَى", "raa", "verb", ["nawasib-wa-jawazim-al-mudari", "naqis-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ وَعَلَامَةُ نَصْبِهِ فَتْحَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "Present verb in nasb after أَنْ, its sign a fatha estimated on the alif; the doer «He» is hidden.", "En ile mansûb muzâri, alâmeti elif üzerindeki takdîrî fetha; fâil gizli «O»."),
  MA_MAF((" — وَالْعَائِدُ مَحْذُوفٌ: مَا يَفْعَلُونَهُ", "; the returning pronoun is omitted («what they do [with it]»)", "; âid zamir hazfedilmiş")),
  MUDARI5("يَفْعَلُونَ", "faala", role_ar=" — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", role_en="; the clause is the relative's clause and has no seat of i'rab", role_tr="; cümle mevsûlün sılası, i'râbdan mahalli yok"),
  BI_NOUN("بِنِعْمَتِهِ", "nima", "نِعْمَتِهِ", enc="هِ", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "So He sent an angel to them. He came to the leper and said to him: What is the thing you love most?", "tr": "Onlara bir melek gönderdi. Melek alacalıya geldi ve ona dedi ki: En çok neyi istersin?"},
 "tokens": [MADI("فَأَرْسَلَ", "arsala", ["form-iv-verbs"], hidden=True), ILAYHIM(), MAFUL("مَلَكًا", "malak", punct="،"), JAA_H("فَجَاءَ"), ILA(), MAJR("الْأَبْرَصِ", "abras", extra=["mamnu-min-sarf"], note_ar=AL_DIPT[0], note_en=AL_DIPT[1], note_tr=AL_DIPT[2]), QALA("وَقَالَ", hidden=True), JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)", punct=":"),
  tok("أَيُّ", "ayy", "pron", ["al-istifham", "mubtada-khabar", "idafa-definiteness"], "اسْمُ اسْتِفْهَامٍ مُعْرَبٌ، مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، مُضَافٌ — أَيٌّ وَحْدَهَا بَيْنَ أَسْمَاءِ الِاسْتِفْهَامِ تُعْرَبُ، لِلُزُومِهَا الْإِضَافَةَ.",
      "The one declinable interrogative noun — it never leaves the idafa, so it never lost its i'rab — here the mubtada, in raf' and annexed.", "İstifhâm isimleri içinde yalnız eyy mu'rebdir — izâfetten ayrılmadığı için i'râbını kaybetmemiştir; burada mübtedâ, merfû, muzâf."),
  MUDAF_ILAYH("شَيْءٍ", "shay"),
  tok("أَحَبُّ", "ahabb", "noun", ["mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ.", "The predicate, in raf' — an elative on أَفْعَل.", "Haber, merfû — ef'al vezninde ism-i tafdîl."),
  JARR_PRON("إِلَيْكَ", "ila", "إِلَيْ", "كَ", " («sana»)", punct="؟")]})
S1.append({"id": "s3", "translation": {"en": "He said: A fine colour and fine skin, for people have come to loathe me.", "tr": "Dedi ki: Güzel bir renk ve güzel bir ten; çünkü insanlar benden iğrenir oldu."},
 "tokens": [QALA("قَالَ", hidden=True, punct=":"), KH_MAHDHUF("لَوْنٌ", "lawn", "أَحَبُّ شَيْءٍ إِلَيَّ لَوْنٌ حَسَنٌ", "[the dearest thing to me is] a fine colour", "[bana en sevimli şey] güzel bir renk[tir]"),
  NAAT("حَسَنٌ", "hasan-adj", "raf"), ATF("وَجِلْدٌ", "jild", "noun", "raf"), NAAT("حَسَنٌ", "hasan-adj", "raf", punct="،"), FAQAD(), KARIHANI(), FAIL("النَّاسُ", "nas", punct=".")]})
S1.append({"id": "s4", "translation": {"en": "The angel wiped him, and what had been upon him went away, and he gave him a pregnant she-camel.", "tr": "Melek onu sıvazladı; üzerindeki hastalık gitti ve ona gebe bir deve verdi."},
 "tokens": [ENC_MADI("فَمَسَحَهُ", "masaha", "هُ"), MALAK_F(punct="،"), MADI("فَذَهَبَ", "dhahaba"), JARR_PRON("عَنْهُ", "an", "عَنْ", "هُ", " («ondan»)"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ فَاعِلٌ، وَجُمْلَةُ كَانَ بِهِ صِلَتُهُ.", "A relative pronoun, the doer in the seat of raf'; «was upon him» is its clause.", "İsm-i mevsûl, fâil olarak mahallen merfû; «onda idi» sılasıdır."),
  tok("كَانَ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ، وَاسْمُهَا مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ يَعُودُ عَلَى مَا.", "كَانَ built on fatha; its noun is a hidden «it» referring back to مَا.", "Fetha üzere mebnî nâkıs kâne; ismi gizli «o», mâ'ya râci."),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onda»)", punct="،", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ كَانَ", note_en="; the phrase is the predicate of كَانَ, in the seat of nasb", note_tr="; câr-mecrûr kâne'nin haberi, mahallen mansûb"),
  AATAHU("وَأَعْطَاهُ", HID), MAF2("نَاقَةً", "naqa"), HAMIL_N(punct=".")]})
S1.append({"id": "s5", "translation": {"en": "Then he came to the bald man and asked him the same; he said: Fine hair, for people have come to loathe me.", "tr": "Sonra kele geldi ve ona da aynısını sordu. O dedi ki: Güzel saç; çünkü insanlar benden iğrenir oldu."},
 "tokens": [THUMMA(), JAA_H(), ILA(), MAJR("الْأَقْرَعِ", "aqra", extra=["mamnu-min-sarf"], note_ar=AL_DIPT[0], note_en=AL_DIPT[1], note_tr=AL_DIPT[2]), ENC_MADI("فَسَأَلَهُ", "saala", "هُ", hidden=True), MITHLA(), DHALIKA_MI(punct="،"), QALA("فَقَالَ", hidden=True, punct=":"),
  KH_MAHDHUF("شَعْرٌ", "shaar", "أَحَبُّ شَيْءٍ إِلَيَّ شَعْرٌ حَسَنٌ", "[the dearest thing to me is] fine hair", "[bana en sevimli şey] güzel saç[tır]"), NAAT("حَسَنٌ", "hasan-adj", "raf", punct="،"), FAQAD(), KARIHANI(), FAIL("النَّاسُ", "nas", punct=".")]})
S1.append({"id": "s6", "translation": {"en": "He wiped him, and God gave him fine hair and a pregnant cow.", "tr": "Onu sıvazladı; Allah ona güzel saç ve gebe bir inek verdi."},
 "tokens": [MASAHAHU(punct="،"), AATAHU("فَأَعْطَاهُ", ("، وَالْفَاعِلُ بَعْدَهُ", "; the doer follows", "; fâil sonra gelir")), ALLAH_F(), MAF2("شَعْرًا", "shaar"), NAAT("حَسَنًا", "hasan-adj", "nasb"), ATF("وَبَقَرَةً", "baqara", "noun", "nasb"), HAMIL_N(punct=".")]})
S1.append({"id": "s7", "translation": {"en": "Then he came to the blind man, who said: I would love God to restore my sight to me, so that I may see people with it.", "tr": "Sonra köre geldi; o dedi ki: Allah'ın gözümü bana geri vermesini isterim ki onunla insanları göreyim."},
 "tokens": [THUMMA(), JAA_H(), ILA(), tok("الْأَعْمَى", "ama-blind", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ كَسْرَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "In jarr after إِلَى, its sign a kasra estimated on the alif.", "İlâ ile mecrûr; alâmeti elif üzerindeki takdîrî kesre."),
  QALA("فَقَالَ", hidden=True, punct=":"), MUDARI("أُحِبُّ", "ahabba", ["form-iv-verbs", "doubled-verbs"], who="أَنَا", wujub=True),
  AN(" — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولٌ بِهِ لِأُحِبُّ", "; the clause it builds is the object of «I would love»", "; kurduğu müevvel masdar «isterim»in mef'ûlüdür"),
  MANSUB_AN("يَرُدَّ", "radda", ["doubled-verbs"], hidden=False), ALLAH_F(), ILAYYA(),
  YA_NOUN("بَصَرِي", "basar", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ", "The direct object, in nasb by a fatha", "Mef'ûlün bih, fetha ile mansûb;", extra=["maful-bihi"]),
  tok("فَأُبْصِرَ", "absara", "verb", ["form-iv-verbs", "nawasib-wa-jawazim-al-mudari", "atf-nasaq"], FA_AR + "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِالْعَطْفِ عَلَى يَرُدَّ، وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا.",
      "The fa conjoins; «that I may see» is in nasb by conjunction to «restore», its sign the fatha; the doer «I» must stay hidden.", "Fâ atıf; «göreyim» yerudde'ye atıfla mansûb, alâmeti fetha; fâil «ben» vücûben müstetir.", segments=[seg("فَ", "fa", "conj"), seg("أُبْصِرَ", "absara", "verb")]),
  JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)"), MAFUL("النَّاسَ", "nas", punct=".")]})
S1.append({"id": "s8", "translation": {"en": "He wiped him, and God restored his sight to him, and he gave him a pregnant ewe.", "tr": "Onu sıvazladı; Allah gözünü ona geri verdi ve ona gebe bir koyun verdi."},
 "tokens": [MASAHAHU(punct="،"), MADI("فَرَدَّ", "radda", ["doubled-verbs"]), ALLAH_F(), ILAYHI(), ENC_NOUN("بَصَرَهُ", "basar", "هُ", "maful", punct="،"), AATAHU("وَأَعْطَاهُ", HID), MAF2("شَاةً", "shat"), HAMIL_N(punct=".")]})

# ---- Chapter 2 — النِّعْمَةُ ----
S2 = []
S2.append({"id": "s1", "translation": {"en": "The camel, the cow and the ewe gave birth, and they multiplied until this one had a valley full of camels, this one a valley of cattle, and this one a valley of sheep.", "tr": "Deve, inek ve koyun doğurdu; çoğaldılar, öyle ki birinin bir vadi dolusu devesi, birinin bir vadi dolusu sığırı, birinin de bir vadi dolusu koyunu oldu."},
 "tokens": [MADI("فَوَلَدَتِ", "walada", ["mithal-verbs"], fem=True, kasra=True), FAIL("النَّاقَةُ", "naqa"), ATF("وَالْبَقَرَةُ", "baqara"), ATF("وَالشَّاةُ", "shat", punct="،"),
  MADI("وَكَثُرَتْ", "kathura", fem=True, hidden=True), HATTA_IBT(), KANA("كَانَ"),
  tok("لِهٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara"], "اللَّامُ حَرْفُ جَرٍّ، وَهٰذَا اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ كَانَ مُقَدَّمٌ.",
      "The lam is a jarr letter and the demonstrative after it fills the seat of jarr — the phrase is the fronted predicate of كَانَ.", "Lâm cer harfi, işaret ismi mahallen mecrûr — câr-mecrûr kâne'nin öne alınmış haberi.", segments=[seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("وَادٍ", "wadi-valley", "noun", ["kana-wa-akhawatuha", "ism-maqsur-manqus"], "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ لِلثِّقَلِ — مَنْقُوصٌ نَكِرَةٌ حُذِفَتْ يَاؤُهُ وَعُوِّضَ عَنْهَا التَّنْوِينُ.",
      "The noun of كَانَ, placed after its predicate, in raf' by a damma estimated on the dropped ya — an indefinite manqus whose ya has gone, the tanwin standing in for it.", "Kâne'nin ismi (haberinden sonra); düşen yâ üzerindeki takdîrî damme ile merfû — nekre menkûs, yâ'sı düşmüş, tenvîn onun yerine geçmiş."),
  MINA(), MAJR("الْإِبِلِ", "ibil", punct="،"),
  tok("وَلِهٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara", "mubtada-khabar"], WA_AR + "اللَّامُ حَرْفُ جَرٍّ، وَهٰذَا فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ، وَالْجُمْلَةُ مَعْطُوفَةٌ عَلَى جُمْلَةِ كَانَ.",
      "The waw conjoins the clause to the one before; the lam is a jarr letter and the demonstrative fills the seat of jarr — the phrase is a fronted predicate.", "Vâv cümleyi öncekine atfeder; lâm cer harfi, işaret ismi mahallen mecrûr — câr-mecrûr öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("وَادٍ", "wadi-valley", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ نَكِرَةٌ.", "A mubtada placed after its predicate, in raf' by a damma estimated on the dropped ya — an indefinite manqus.", "Sona bırakılmış mübtedâ; düşen yâ üzerindeki takdîrî damme ile merfû — nekre menkûs."),
  MINA(), MAJR("الْبَقَرِ", "baqar", punct="،"),
  tok("وَلِهٰذَا", "hadha", "pron", ["huruf-jarr", "asma-al-ishara", "mubtada-khabar"], WA_AR + "اللَّامُ حَرْفُ جَرٍّ، وَهٰذَا فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "The waw conjoins; the lam is a jarr letter and the demonstrative fills the seat of jarr — a fronted predicate.", "Vâv atıf; lâm cer harfi, işaret ismi mahallen mecrûr — öne alınmış haber.", segments=[seg("وَ", "wa", "conj"), seg("لِ", "li", "prep"), seg("هٰذَا", "hadha", "pron")]),
  tok("وَادٍ", "wadi-valley", "noun", ["mubtada-khabar", "ism-maqsur-manqus"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — مَنْقُوصٌ نَكِرَةٌ.", "A mubtada placed after its predicate, in raf' by a damma estimated on the dropped ya — an indefinite manqus.", "Sona bırakılmış mübtedâ; düşen yâ üzerindeki takdîrî damme ile merfû — nekre menkûs."),
  MINA(), MAJR("الْغَنَمِ", "ghanam", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "Years passed, and the angel came back to them in the form of a poor man, to see what they would do with what God had given them.", "tr": "Yıllar geçti; melek, Allah'ın kendilerine verdikleriyle ne yaptıklarını görmek için yoksul bir adam sûretinde yanlarına döndü."},
 "tokens": [tok("وَمَضَتْ", "mada", "verb", ["naqis-verbs"], WA_ISTINAF[0] + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالتَّاءُ لِلتَّأْنِيثِ.",
      WA_ISTINAF[1] + "past verb built on a fatha estimated on the alif, which dropped before the feminine ta (two quiescents).", WA_ISTINAF[2] + "te'nîs tâ'sı önünde (iki sâkin) düşen elif üzerindeki takdîrî fetha ile mebnî mâzî.", segments=[seg("وَ", "wa", "conj"), seg("مَضَتْ", "mada", "verb")]),
  FAIL("سَنَوَاتٌ", "sana", extra=["jam-muannath-salim"], punct="،", note_ar=" — جَمْعُ مُؤَنَّثٍ سَالِمٌ لِسَنَةٍ", note_en=" — the sound feminine plural of «year»", note_tr=" — senenin cem-i müennes sâlimi"),
  MADI("فَرَجَعَ", "rajaa"), MALAK_F(), ILAYHIM(), FI(), MAJR("صُورَةِ", "sura", note_ar="، مُضَافٌ", note_en="; annexed", note_tr="; muzâf"), MUDAF_ILAYH("رَجُلٍ", "rajul"), NAAT("فَقِيرٍ", "faqir", "jarr"),
  tok("لِيَنْظُرَ", "nazara", "verb", ["lam-taleel", "nawasib-wa-jawazim-al-mudari"], "اللَّامُ لِلتَّعْلِيلِ، وَيَنْظُرَ فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ بَعْدَ اللَّامِ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ.",
      "The lam of purpose; «that he might see» is in nasb by a hidden أَنْ after the lam, its sign the fatha; the doer «he» is hidden.", "Ta'lîl lâmı; «görsün diye» lâmdan sonra gizli en ile mansûb, alâmeti fetha; fâil gizli «o».", segments=[seg("لِ", "lam-taleel", "part"), seg("يَنْظُرَ", "nazara", "verb")]),
  tok("مَاذَا", "madha", "pron", ["al-istifham", "maful-bihi", "mawadi-irab-al-jumla"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ لِيَفْعَلُونَ — وَجُمْلَةُ الِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ مَفْعُولُ يَنْظُرَ الْمُعَلَّقِ عَنْهَا.",
      "An interrogative built on sukun, the fronted object of «they do», in the seat of nasb — the whole question is what «see» looks at, in the seat of nasb (the verb is suspended by it).", "İstifhâm ismi, sükûn üzere mebnî, «yaparlar»ın öne alınmış mef'ûlü — soru cümlesi, kendisiyle ta'lîk edilen «görsün»ün mef'ûlü olarak mahallen mansûb."),
  MUDARI5("يَفْعَلُونَ", "faala"),
  tok("بِمَا", "bi", "prep", ["huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَمَا اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ جَرٍّ، وَجُمْلَةُ أَعْطَاهُمُ صِلَتُهُ.", "The ba is a jarr letter; مَا is a relative pronoun in the seat of jarr, and «gave them» is its clause.", "Bâ cer harfi; mâ ism-i mevsûl, mahallen mecrûr; «onlara verdi» sılasıdır.", segments=[seg("بِ", "bi", "prep"), seg("مَا", "ma-mawsula", "pron")]),
  tok("أَعْطَاهُمُ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَهُمْ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ، وَحُرِّكَتْ مِيمُهُ بِالضَّمِّ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْمَفْعُولُ الثَّانِي الْعَائِدُ الْمَحْذُوفُ، وَالْفَاعِلُ بَعْدَهُ.",
      "Past verb built on an estimated fatha; the attached «them» is its first object (its mim voweled before the following ال), the second object is the omitted returning pronoun, and the doer follows.", "Takdîrî fetha ile mebnî mâzî; bitişik «onlara» birinci mef'ûl (mîmi, sonraki el önünde harekelendi), ikinci mef'ûl hazfedilen âid; fâil sonra gelir.", segments=[seg("أَعْطَا", "aata", "verb"), seg("هُمُ", "pron-3mp", "pron")]),
  ALLAH_F(punct=".")]})

# ---- Chapter 3 — الْجُحُودُ ----
S3 = []
S3.append({"id": "s1", "translation": {"en": "He came to the leper in his former form and said to him: A poor stranger, with nothing to carry him to his town.", "tr": "Alacalıya eski sûretinde geldi ve ona dedi ki: Yoksul bir garibim; memleketime ulaşacak hiçbir şeyim yok."},
 "tokens": [JAA_H("فَجَاءَ"), ILA(), MAJR("الْأَبْرَصِ", "abras", extra=["mamnu-min-sarf"], note_ar=AL_DIPT[0], note_en=AL_DIPT[1], note_tr=AL_DIPT[2]), FI(), ENC_NOUN("صُورَتِهِ", "sura", "هِ", "majr"),
  tok("الْأُولَى", "ula-first", "noun", ["naat-sifa", "ism-maqsur-manqus"], "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — مُؤَنَّثُ أَوَّلَ.", "An adjective in jarr by a kasra estimated on the alif — the feminine of «first».", "Na't; elif üzerindeki takdîrî kesre ile mecrûr — evvel'in müennesi."),
  QALA("وَقَالَ", hidden=True), JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)", punct=":"), *MISKIN_GHARIB(),
  tok("لَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-afal-al-naqisa-fil-kafiya", "jumla-sifa"], "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ لِلنَّفْيِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَالِثٌ لِرَجُلٍ.", "The frozen defective verb of negation — its clause is a third adjective of «a man», in the seat of raf'.", "Nefiy bildiren câmid nâkıs fiil — cümlesi «adam»ın üçüncü sıfatı, mahallen merfû."),
  JARR_PRON("لَهُ", "li", "لَ", "هُ", " («onun»)", note_ar=" — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ خَبَرُ لَيْسَ مُقَدَّمٌ", note_en="; the phrase is the fronted predicate of لَيْسَ", note_tr="; câr-mecrûr leyse'nin öne alınmış haberi"),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "kana-wa-akhawatuha"], "اسْمٌ مَوْصُولٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ اسْمُ لَيْسَ مُؤَخَّرٌ، وَجُمْلَةُ يَبْلُغُ صِلَتُهُ.", "A relative pronoun, the noun of لَيْسَ placed after its predicate, in the seat of raf'; «reaches» is its clause.", "İsm-i mevsûl, leyse'nin sona bırakılmış ismi, mahallen merfû; «ulaşır» sılasıdır."),
  MUDARI("يَبْلُغُ", "balagha", who="هُوَ"), JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)", note_ar=" — وَالْهَاءُ هِيَ الْعَائِدُ", note_en="; this ha is the returning pronoun", note_tr="; bu hâ âid zamirdir"), ENC_NOUN("بَلَدَهُ", "balad", "هُ", "maful", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "I ask you, by Him who gave you the fine colour and the wealth, for a camel on which I may reach my town.", "tr": "Sana güzel rengi ve malı veren Allah adına senden, memleketime ulaşacağım bir deve istiyorum."},
 "tokens": [ASALUKA(), BILLADHI(),
  tok("أَعْطَاكَ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ: هُوَ وَهُوَ الْعَائِدُ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.",
      "Past verb built on an estimated fatha; the hidden doer «He» is the returning pronoun, and the attached «you» is the first object.", "Takdîrî fetha ile mebnî mâzî; gizli fâil «O» âid zamirdir; bitişik kâf birinci mef'ûlün bih.", segments=[seg("أَعْطَا", "aata", "verb"), seg("كَ", "pron-2ms", "pron")]),
  MAF2("اللَّوْنَ", "lawn"), NAAT("الْحَسَنَ", "hasan-adj", "nasb"), ATF("وَالْمَالَ", "mal", "noun", "nasb"),
  MAF2("بَعِيرًا", "bair", note_ar=" لِأَسْأَلُكَ", note_en=" of «I ask you»", note_tr=" («senden istiyorum»un)"), ABLUGHU("أَبْلُغُ", "بَعِيرًا"), JARR_PRON("بِهِ", "bi", "بِ", "هِ", " («onunla»)"), BALADI(punct=".")]})
S3.append({"id": "s3", "translation": {"en": "He said: The claims on me are many, and I have nothing to give you.", "tr": "Dedi ki: Üzerimdeki haklar çok; sana verecek bir şeyim yok."},
 "tokens": [QALA("فَقَالَ", hidden=True, punct=":"),
  tok("الْحُقُوقُ", "haqq", "noun", ["mubtada-khabar", "jam-taksir"], "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ تَكْسِيرٍ لِحَقٍّ.", "The mubtada, in raf' — the broken plural of «a right, a claim».", "Mübtedâ, merfû — hakkın cem-i teksîri."),
  KHABAR("كَثِيرَةٌ", "kathir", punct="،"),
  tok("وَلَيْسَ", "laysa", "verb", ["kana-wa-akhawatuha", "al-afal-al-naqisa-fil-kafiya"], WA_AR + "لَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ لِلنَّفْيِ.", "The waw conjoins; لَيْسَ is the frozen defective verb of negation.", "«ve» + leyse: nefiy bildiren câmid nâkıs fiil.", segments=[seg("وَ", "wa", "conj"), seg("لَيْسَ", "laysa", "verb")]),
  tok("عِنْدِي", "inda", "noun", ["maful-fih", "kana-wa-akhawatuha", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مُضَافٌ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَالظَّرْفُ فِي مَحَلِّ نَصْبٍ خَبَرُ لَيْسَ مُقَدَّمٌ.",
      "An adverb of place in nasb by an estimated fatha before the speaker's ya, annexed to it — the fronted predicate of لَيْسَ.", "Mekân zarfı, mütekellim yâ'sından önce takdîrî fetha ile mansûb, muzâf — leyse'nin öne alınmış haberi.", segments=[seg("عِنْدِ", "inda", "noun"), seg("ي", "pron-1s", "pron")]),
  tok("مَا", "ma-mawsula", "pron", ["ism-mawsul", "kana-wa-akhawatuha"], "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ اسْمُ لَيْسَ مُؤَخَّرٌ، وَجُمْلَةُ أُعْطِيكَ صِلَتُهُ، وَالْعَائِدُ مَحْذُوفٌ.", "A relative pronoun, the noun of لَيْسَ placed after its predicate; «I give you» is its clause, the returning pronoun omitted.", "İsm-i mevsûl, leyse'nin sona bırakılmış ismi; «sana veririm» sılası, âid hazfedilmiş."),
  tok("أُعْطِيكَ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ مَفْعُولٌ بِهِ أَوَّلُ فِي مَحَلِّ نَصْبٍ، وَالثَّانِي الْعَائِدُ الْمَحْذُوفُ.",
      "Present verb in raf' by a damma estimated on the ya; the doer «I» must stay hidden, the attached «you» is the first object and the omitted returning pronoun the second.", "Yâ üzerinde takdîrî damme ile merfû muzâri; fâil «ben» vücûben müstetir; kâf birinci mef'ûl, hazfedilen âid ikincisi.", punct=".", segments=[seg("أُعْطِي", "aata", "verb"), seg("كَ", "pron-2ms", "pron")])]})
S3.append({"id": "s4", "translation": {"en": "The angel said to him: I think I know you!", "tr": "Melek ona dedi ki: Seni tanır gibiyim!"},
 "tokens": [QALA("فَقَالَ"), JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"), MALAK_F(punct=":"),
  tok("كَأَنِّي", "ka-anna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya", "al-bariz-al-muttasil", "ya-al-mutakallim"], "كَأَنَّ حَرْفٌ مُشَبَّهٌ بِالْفِعْلِ لِلتَّشْبِيهِ، وَيَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ اسْمُهَا، وَحُذِفَتْ نُونُ الْوِقَايَةِ تَخْفِيفًا — وَالْجُمْلَةُ بَعْدَهَا خَبَرُهَا.",
      "كَأَنَّ «as if» with the speaker's ya as its noun, in the seat of nasb (the guarding nun dropped for lightness); the clause after it is its predicate.", "Keenne; mütekellim yâ'sı ismi, mahallen mansûb (vikâye nûnu hafiflik için düşmüş); sonraki cümle haberi.", segments=[seg("كَأَنَّ", "ka-anna", "part"), seg("ي", "pron-1s", "pron")]),
  tok("أَعْرِفُكَ", "arafa", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ كَأَنَّ.",
      "Present verb in raf'; the doer «I» must stay hidden and the attached «you» is its object — the clause is the predicate of كَأَنَّ, in the seat of raf'.", "Merfû muzâri; fâil «ben» vücûben müstetir, kâf mef'ûlün bih — cümle keenne'nin haberi, mahallen merfû.", punct="!", segments=[seg("أَعْرِفُ", "arafa", "verb"), seg("كَ", "pron-2ms", "pron")])]})
S3.append({"id": "s5", "translation": {"en": "Were you not a poor leper whom people loathed, and God gave to you?", "tr": "Sen, insanların iğrendiği yoksul bir alacalı değil miydin? Sonra Allah sana verdi."},
 "tokens": [tok("أَلَمْ", "lam-jazima", "part", ["al-istifham", "nawasib-wa-jawazim-al-mudari", "lam-jazim"], "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ، وَلَمْ حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "The hamza asks a question that expects assent; لَمْ negates, governs jazm and turns the present to the past.", "Hemze takrîrî istifhâm içindir; lem nefiy, cezm ve kalb harfi.", segments=[seg("أَ", "a-istifham", "part"), seg("لَمْ", "lam-jazima", "part")]),
  tok("تَكُنْ", "kana", "verb", ["kana-wa-akhawatuha", "hollow-verbs", "nawasib-wa-jawazim-al-mudari"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ (الْوَاوُ) لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهَا مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنْتَ.",
      "The present of كَانَ in jazm after لَمْ, its sign the sukun; its middle waw dropped where two quiescents met, and its noun «you» must stay hidden.", "Kâne'nin muzârii, lem ile meczûm, alâmeti sükûn; iki sâkin karşılaşınca aynı (vâv) düştü; ismi «sen» vücûben müstetir."),
  tok("أَبْرَصَ", "abras", "noun", ["kana-wa-akhawatuha", "mamnu-min-sarf"], "خَبَرُ تَكُنْ مَنْصُوبٌ بِالْفَتْحَةِ" + AFAL_SIFA[0] + ".", "The predicate of «were you», in nasb" + AFAL_SIFA[1] + ".", "Tekün'ün haberi, mansûb" + AFAL_SIFA[2] + "."),
  NAAT("فَقِيرًا", "faqir", "nasb"),
  tok("يَكْرَهُكَ", "kariha", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "jumla-sifa"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ مُقَدَّمٌ، وَالْفَاعِلُ بَعْدَهُ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ ثَانٍ لِأَبْرَصَ.",
      "Present verb in raf'; the attached «you» is its fronted object and the doer follows — the clause is a second adjective of «leper», in the seat of nasb.", "Merfû muzâri; bitişik kâf öne alınmış mef'ûlün bih, fâil sonra gelir — cümle «alacalı»nın ikinci sıfatı, mahallen mansûb.", segments=[seg("يَكْرَهُ", "kariha", "verb"), seg("كَ", "pron-2ms", "pron")]),
  FAIL("النَّاسُ", "nas", punct="،"),
  tok("فَأَعْطَاكَ", "aata", "verb", ["form-iv-verbs", "naqis-verbs", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], FA_AR + "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ، وَالْكَافُ مَفْعُولٌ بِهِ أَوَّلُ فِي مَحَلِّ نَصْبٍ، وَالْمَفْعُولُ الثَّانِي مَحْذُوفٌ: الْمَالَ، وَالْفَاعِلُ بَعْدَهُ.",
      "The fa conjoins; past verb built on an estimated fatha, the attached «you» its first object, the second (the wealth) omitted, the doer after it.", "Fâ atıf; takdîrî fetha ile mebnî mâzî, kâf birinci mef'ûl, ikincisi (mal) hazfedilmiş, fâil sonra gelir.", segments=[seg("فَ", "fa", "conj"), seg("أَعْطَا", "aata", "verb"), seg("كَ", "pron-2ms", "pron")]),
  ALLAH_F(punct="؟")]})
S3.append({"id": "s6", "translation": {"en": "He said: I only inherited this wealth from my fathers.", "tr": "Dedi ki: Ben bu malı yalnızca babalarımdan miras aldım."},
 "tokens": [QALA("فَقَالَ", hidden=True, punct=":"),
  tok("إِنَّمَا", "innama", "part", ["innama-kaffa", "inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ كُفَّ عَنِ الْعَمَلِ بِمَا الْكَافَّةِ، وَأَفَادَ التَّرْكِيبُ الْحَصْرَ.", "إِنَّ restrained by مَا: it no longer governs, and the pair means «only».", "Kâffe mâ ile amelden alıkonmuş inne; terkip hasr («yalnızca») ifade eder."),
  MADI_T("وَرِثْتُ", "waritha", who="ana", extra=["mithal-verbs"]),
  tok("هٰذَا", "hadha", "pron", ["asma-al-ishara", "maful-bihi"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.", "A demonstrative built on sukun, the object in the seat of nasb.", "İşaret ismi, sükûn üzere mebnî, mef'ûlün bih olarak mahallen mansûb."),
  BADAL("الْمَالَ", "mal", "nasb"), PREP("عَنْ", "an", gloss_tr="«-den»"),
  YA_NOUN("آبَائِي", "ab", "مَجْرُورٌ بِكَسْرَةٍ", "In jarr after the letter, by a kasra", "Cer harfiyle mecrûr, kesre", extra=["huruf-jarr", "jam-taksir"], punct=".")]})
S3.append({"id": "s7", "translation": {"en": "The angel said: If you are lying, may God turn you back to what you were.", "tr": "Melek dedi ki: Eğer yalan söylüyorsan, Allah seni eski haline çevirsin."},
 "tokens": [QALA("فَقَالَ"), MALAK_F(punct=":"), IN_SHART("إِنْ"), KUNTU_SH(), KADHIBAN(), FASAYYARAKA(), ALLAH_F(), ILA(), *MA_KUNTA(punct=".")]})
S3.append({"id": "s8", "translation": {"en": "Then he came to the bald man and said the same to him, and he answered as the first had answered; so the angel said to him what he had said to the leper.", "tr": "Sonra kele geldi ve ona da aynısını söyledi; o da birincinin verdiği cevabı verdi. Melek ona alacalıya söylediğini söyledi."},
 "tokens": [THUMMA(), JAA_H(), ILA(), MAJR("الْأَقْرَعِ", "aqra", extra=["mamnu-min-sarf"], note_ar=AL_DIPT[0], note_en=AL_DIPT[1], note_tr=AL_DIPT[2]), QALA("فَقَالَ", hidden=True), JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"), MITHLA(), DHALIKA_MI(punct="،"),
  MADI("فَرَدَّ", "radda", ["doubled-verbs"], hidden=True), ALAYHI(), MITHLA(), MA_MI(), MADI("رَدَّ", "radda", ["doubled-verbs"]), FAIL("الْأَوَّلُ", "awwal", punct="،"),
  QALA("فَقَالَ"), JARR_PRON("لَهُ", "li", "لَ", "هُ", " («ona»)"), MALAK_F(), MITHLA(), MA_MI(), MADI("قَالَ", "qala", ["hollow-verbs"], hidden=True),
  LI_AL("لِلْأَبْرَصِ", "abras", "الْأَبْرَصِ", extra=["mamnu-min-sarf"], punct=".", note_ar=" — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ، لٰكِنَّهُ جُرَّ بِالْكَسْرَةِ لِدُخُولِ ال عَلَيْهِ", note_en=" — a diptote, yet it takes the ordinary kasra once it wears the article", note_tr=" — gayr-ı munsariftir, fakat el aldığı için kesre ile mecrûr olur")]})

# ---- Chapter 4 — الشُّكْرُ ----
S4 = []
S4.append({"id": "s1", "translation": {"en": "Then he came to the blind man and said: A poor stranger; I ask you, by Him who restored your sight to you, for a sheep on which I may reach my town.", "tr": "Sonra köre geldi ve dedi ki: Yoksul bir garibim; gözünü sana geri veren Allah adına senden, memleketime ulaşacağım bir koyun istiyorum."},
 "tokens": [THUMMA(), JAA_H(), ILA(), tok("الْأَعْمَى", "ama-blind", "noun", ["huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِإِلَى وَعَلَامَةُ جَرِّهِ كَسْرَةٌ مُقَدَّرَةٌ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.", "In jarr after إِلَى, its sign a kasra estimated on the alif.", "İlâ ile mecrûr; alâmeti elif üzerindeki takdîrî kesre."),
  QALA("فَقَالَ", hidden=True, punct=":"), *MISKIN_GHARIB(punct="،"), ASALUKA(), BILLADHI(),
  MADI("رَدَّ", "radda", ["doubled-verbs"], hidden=True, note_ar=" وَهُوَ الْعَائِدُ — وَالْجُمْلَةُ صِلَةُ الَّذِي", note_en=", and it is the returning pronoun — the clause is the relative's clause", note_tr=" ve o âid zamirdir — cümle ellezî'nin sılası"),
  JARR_PRON("عَلَيْكَ", "ala", "عَلَيْ", "كَ", " («sana»)"), ENC_NOUN("بَصَرَكَ", "basar", "كَ", "maful"),
  MAF2("شَاةً", "shat", note_ar=" لِأَسْأَلُكَ", note_en=" of «I ask you»", note_tr=" («senden istiyorum»un)"), ABLUGHU("أَبْلُغُ", "شَاةً"), JARR_PRON("بِهَا", "bi", "بِ", "هَا", " («onunla»)"), BALADI(punct=".")]})
S4.append({"id": "s2", "translation": {"en": "He said: I was blind, and God restored my sight to me; so take what you will and leave what you will.", "tr": "Dedi ki: Ben kördüm; Allah gözümü bana geri verdi. Dilediğini al, dilediğini bırak."},
 "tokens": [QALA("فَقَالَ", hidden=True, punct=":"), QAD(),
  tok("كُنْتُ", "kana", "verb", ["kana-wa-akhawatuha", "al-bariz-al-muttasil", "hollow-verbs"], "كَانَ فِعْلٌ مَاضٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ رَفْعٍ اسْمُهَا، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "كَانَ built on sukun before the ta of the doer (its middle letter dropped where two quiescents met); the ta «I» is its noun, in the seat of raf'.", "Fâil tâ'sı bitiştiği için sükûn üzere mebnî kâne (iki sâkin karşılaşınca aynı düştü); tâ «ben» ismi, mahallen merfû."),
  tok("أَعْمَى", "ama-blind", "noun", ["kana-wa-akhawatuha", "mamnu-min-sarf", "ism-maqsur-manqus"], "خَبَرُ كَانَ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ" + AFAL_SIFA[0] + "، فَلَا تَنْوِينَ.", "The predicate of كَانَ, in nasb by a fatha estimated on the alif" + AFAL_SIFA[1] + ", so it wears no tanwin.", "Kâne'nin haberi; elif üzerindeki takdîrî fetha ile mansûb" + AFAL_SIFA[2] + "; tenvîn almaz."),
  MADI("فَرَدَّ", "radda", ["doubled-verbs"]), ALLAH_F(), ILAYYA(), YA_NOUN("بَصَرِي", "basar", "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ", "The direct object, in nasb by a fatha", "Mef'ûlün bih, fetha ile mansûb;", extra=["maful-bihi"], punct="،"),
  AMR("فَخُذْ", "akhadha", note_ar=" — وَحُذِفَتْ هَمْزَةُ أَخَذَ فِي الْأَمْرِ تَخْفِيفًا", note_en=" — the hamza of أَخَذَ drops in the imperative", note_tr=" — ehaze'nin hemzesi emirde düşer"),
  MA_MAF((" — وَالْعَائِدُ مَحْذُوفٌ", "; the returning pronoun is omitted", "; âid hazfedilmiş")),
  tok("شِئْتَ", "shaa", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — أَجْوَفُ يَائِيٌّ حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ وَكُسِرَ أَوَّلُهُ دَلَالَةً عَلَى الْيَاءِ.",
      "Past verb built on sukun before the ta of the doer, the ta its doer — a ya-hollow verb whose middle letter dropped where two quiescents met, the kasra on its first letter pointing to the lost ya.", "Fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî, tâ fâil — yâ'lı ecvef; iki sâkin karşılaşınca aynı düştü, ilk harfin kesresi düşen yâ'ya delâlet eder."),
  AMR("وَاتْرُكْ", "taraka"), MA_MAF((" — وَالْعَائِدُ مَحْذُوفٌ", "; the returning pronoun is omitted", "; âid hazfedilmiş")),
  tok("شِئْتَ", "shaa", "verb", ["hollow-verbs", "al-bariz-al-muttasil", "fail"], "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ مَا.", "Past verb built on sukun before the ta of the doer, the ta its doer — the clause is مَا's clause.", "Fâil tâ'sı bitiştiği için sükûn üzere mebnî mâzî, tâ fâil — cümle mâ'nın sılası.", punct=".")]})
S4.append({"id": "s3", "translation": {"en": "By God, today I will not refuse you anything you take for God's sake.", "tr": "Vallahi bugün, Allah için aldığın hiçbir şeyi senden esirgemem."},
 "tokens": [tok("فَوَاللهِ", "allah", "propn", ["huruf-al-qasam-fil-kafiya", "huruf-jarr"], FA_AR + "الْوَاوُ حَرْفُ قَسَمٍ وَجَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ — وَجُمْلَةُ لَا أَمْنَعُكَ جَوَابُ الْقَسَمِ لَا مَحَلَّ لَهَا.",
      "The fa conjoins; the waw of oath is a jarr letter and the Name of Majesty is in jarr — «I will not refuse you» is the oath's answer, with no seat of i'rab.", "Fâ atıf; kasem vâvı cer harfi, lafza-i celâl mecrûr — «esirgemem» kasemin cevabı, i'râbdan mahalli yok.",
      segments=[seg("فَ", "fa", "conj"), seg("وَ", "wa-qasam", "part"), seg("اللهِ", "allah", "propn")]),
  LA_NAFIYA(),
  tok("أَمْنَعُكَ", "manaa", "verb", ["mudari-marfu", "al-bariz-al-muttasil", "maful-bihi", "mafulayn"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ مُسْتَتِرٌ وُجُوبًا تَقْدِيرُهُ: أَنَا، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ أَوَّلُ.", "Present verb in raf'; the doer «I» must stay hidden, and the attached «you» is the first object.", "Merfû muzâri; fâil «ben» vücûben müstetir; bitişik kâf birinci mef'ûlün bih.", segments=[seg("أَمْنَعُ", "manaa", "verb"), seg("كَ", "pron-2ms", "pron")]),
  ZARF("الْيَوْمَ", "yawm", mudaf=False, **ZAMAN), MAF2("شَيْئًا", "shay"),
  MADI_T("أَخَذْتَهُ", "akhadha", who="anta", enc="هُ", note_ar=" — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِشَيْئًا", note_en="; the clause qualifies «anything», in the seat of nasb", note_tr="; cümle «bir şey»in sıfatı, mahallen mansûb"),
  tok("لِلّٰهِ", "allah", "propn", ["huruf-jarr", "lam-taleel"], "اللَّامُ حَرْفُ جَرٍّ لِلتَّعْلِيلِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِالْكَسْرَةِ، وَحُذِفَتْ أَلِفُ الْوَصْلِ فِي الرَّسْمِ.", "The lam of purpose is a jarr letter; the Name of Majesty is in jarr, and the article's alif is swallowed in the spelling.", "Ta'lîl lâmı cer harfi; lafza-i celâl mecrûr, vasl elifi yazıda düşmüştür.", punct=".", segments=[seg("لِ", "li", "prep"), seg("اللّٰهِ", "allah", "propn")])]})
S4.append({"id": "s4", "translation": {"en": "The angel said: Keep your wealth; this was only a trial for you all. God is pleased with you and angry with your two companions.", "tr": "Melek dedi ki: Malını tut; bu sizin için ancak bir imtihandı. Allah senden razı oldu, iki arkadaşına ise gazap etti."},
 "tokens": [QALA("فَقَالَ"), MALAK_F(punct=":"), AMR("أَمْسِكْ", "amsaka", ["form-iv-verbs"]), ENC_NOUN("مَالَكَ", "mal", "كَ", "maful", punct="،"),
  tok("فَإِنَّمَا", "innama", "part", ["innama-kaffa", "inna-wa-akhawatuha"], FA_AR + "إِنَّمَا: إِنَّ الْمَكْفُوفَةُ بِمَا الْكَافَّةِ، تُفِيدُ الْحَصْرَ.", "The fa conjoins; إِنَّمَا is إِنَّ restrained by مَا, meaning «only».", "Fâ atıf; innemâ: kâffe mâ ile amelden alıkonmuş inne, hasr ifade eder.", segments=[seg("فَ", "fa", "conj"), seg("إِنَّمَا", "innama", "part")]),
  KANA("كَانَتْ", fem=True),
  tok("هٰذِهِ", "hadhihi", "pron", ["asma-al-ishara", "kana-wa-akhawatuha"], "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ اسْمُ كَانَ.", "A demonstrative built on kasra, the noun of كَانَ in the seat of raf'.", "İşaret ismi, kesre üzere mebnî, kâne'nin ismi olarak mahallen merfû."),
  KHK("فِتْنَةً", "fitna"), JARR_PRON("لَكُمْ", "li", "لَ", "كُمْ", " («sizin için»)", punct="،"), FAQAD(),
  MADI("رَضِيَ", "radiya", ["naqis-verbs"], note_ar=" — ظَهَرَتِ الْفَتْحَةُ عَلَى الْيَاءِ", note_en=" — the fatha is written on the ya", note_tr=" — fetha yâ üzerinde zâhir"),
  ALLAH_F(), JARR_PRON("عَنْكَ", "an", "عَنْ", "كَ", " («senden»)"), MADI("وَغَضِبَ", "ghadiba", hidden=True), ALA(),
  tok("صَاحِبَيْكَ", "sahib", "noun", ["huruf-jarr", "al-muthanna", "idafa-definiteness", "al-bariz-al-muttasil"], "مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "In jarr by the ya of the dual, its nun dropped for the annexation; the attached «your» is the second term, in the seat of jarr.", "Tesniye yâ'sıyla mecrûr, nûnu izâfet için düşmüş; bitişik kâf muzâfun ileyh, mahallen mecrûr.", punct=".", segments=[seg("صَاحِبَيْ", "sahib", "noun"), seg("كَ", "pron-2ms", "pron")])]})

CHAPTERS = [
 ("ch1", {"ar": "الْمَلَكُ يَسْأَلُ", "en": "The Angel Asks", "tr": "Melek Soruyor"}, S1),
 ("ch2", {"ar": "النِّعْمَةُ", "en": "The Blessing", "tr": "Nimet"}, S2),
 ("ch3", {"ar": "الْجُحُودُ", "en": "Denial", "tr": "Nankörlük"}, S3),
 ("ch4", {"ar": "الشُّكْرُ", "en": "Gratitude", "tr": "Şükür"}, S4),
]
TITLES = [c[1] for c in CHAPTERS]
CHAPS = [c[2] for c in CHAPTERS]

PREF = ["ashab-al-ghar", "juha-wa-al-himar", "al-asad-wa-al-arnab", "habil-wa-qabil", "adam-wa-iblis", "shuayb-wa-ahl-madyan", "zakariyya-wa-yahya", "ayyub-wa-al-sabr",
        "dhu-al-qarnayn-wa-al-sadd", "luqman-wa-ibnuh", "qarun-wa-kunuzuh", "ashab-al-kahf", "dawud-wa-jalut", "hud-wa-aad", "sulayman-wa-al-hudhud",
        "salih-wa-al-naqa", "nuh-wa-al-safina", "musa-fi-madyan", "musa-wal-khadir", "musa-wa-bani-israil", "musa-wa-firawn", "yunus-wa-al-hut", "ashab-al-fil",
        "qisas-al-nabiyyin-1", "qisas-al-nabiyyin-2", "qisas-al-nabiyyin-4", "jumal-al-tadrib", "wasiyyat-abi-hanifa-L2", "talkhis-al-miftah", "al-kafiya",
        "izhar-al-asrar", "aqaid-ahl-al-sunna", "wasiyyat-abi-hanifa-samti", "wasiyyat-abi-yusuf-L5", "kitab-al-waqf", "mukhtasar-al-manar", "kitab-al-sulh",
        "kitab-al-buyu", "kitab-al-kaffarat", "bad-al-amali", "min-muqaddimat-al-maqsud"]
PREF = [p for p in PREF if (OUT_ROOT / p / "glossary.json").exists() or (ROOT / "content/samples" / p / "glossary.json").exists()]
# …and every other package on the shelf after them, so a key that lives only in one text is still found (the lemma-identity rule)
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
FORCE = {"ma-mawsula": "al-asad-wa-al-arnab", "lam-taleel": "al-kafiya", "nun-wiqaya": "al-asad-wa-al-arnab", "ka-anna": None, "hasan-adj": None, "kadhib-liar": None,
         "wadi-valley": None, "ama-blind": None, "a-istifham": None, "wa-qasam": None}
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF}
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
 "aqra": {"lemma": "أَقْرَع", "root": "ق ر ع", "pos": "noun", "gloss": {"en": "bald (an أَفْعَل adjective of defect; feminine قَرْعَاء; a diptote)", "tr": "kel (kusur bildiren ef'al sıfatı; müennesi kar'â'; gayr-ı munsarif)"}, "level": 3},
 "shaar": {"lemma": "شَعْر", "root": "ش ع ر", "pos": "noun", "plural": "شُعُور", "gloss": {"en": "hair", "tr": "saç, kıl"}, "level": 3},
 "ula-first": {"lemma": "أُولَى", "root": "أ و ل", "pos": "noun", "gloss": {"en": "first, former (the feminine of أَوَّل; maqṣūr)", "tr": "ilk, önceki (evvel'in müennesi; maksûr)"}, "level": 3},
}
NEW_VERBS = {}
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
 "id": "al-abras-wa-al-aqra-wa-al-ama",
 "storyGroup": "al-abras-wa-al-aqra-wa-al-ama",
 "title": {"ar": "الْأَبْرَصُ وَالْأَقْرَعُ وَالْأَعْمَى", "en": "The Leper, the Bald Man and the Blind Man", "tr": "Alacalı, Kel ve Kör"},
 "subtitle": {"ar": "ثَلَاثَةٌ أَنْعَمَ اللهُ عَلَيْهِمْ ثُمَّ جَاءَهُمْ مَلَكٌ فِي صُورَةِ فَقِيرٍ: مَنْ شَكَرَ وَمَنْ جَحَدَ — قِصَّةٌ لِلْمُسْتَوَى الثَّالِثِ",
              "en": "Three men God blessed, then an angel came to them as a poor man: who gave thanks and who denied — a story for the third level",
              "tr": "Allah'ın nimet verdiği üç adam; sonra bir melek yoksul kılığında gelir: kim şükretti, kim inkâr etti — üçüncü seviye için bir hikâye"},
 "level": 3,
 "levelName": LEVEL_NAME,
 "version": "0.1.0",
 "published": "2026-11-08",
 "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الثَّالِثُ) لِخَبَرِ الْأَبْرَصِ وَالْأَقْرَعِ وَالْأَعْمَى مِنْ بَنِي إِسْرَائِيلَ الَّذِي رَوَتْهُ كُتُبُ الْحَدِيثِ (الْبُخَارِيُّ وَمُسْلِمٌ)، أُلِّفَتْ بِأُسْلُوبِ الْقَارِئِ الْمُتَدَرِّجِ؛ لَيْسَ فِيهَا جُمْلَةٌ هِيَ نَصُّ حَدِيثٍ، وَلَا يَصِحُّ الِاسْتِشْهَادُ بِشَيْءٍ مِنْهَا عَلَى أَنَّهُ حَدِيثٌ. كُلُّ إِعْرَابٍ فِيهَا اجْتِهَادُ الْمُؤَلِّفِ، وَهِيَ بِانْتِظَارِ الْمُرَاجَعَةِ الْعِلْمِيَّةِ.",
  "en": "ORIGINAL Level-3 graded Arabic: the narrative of the leper, the bald man and the blind man among the Children of Israel, preserved in the hadith collections (al-Bukhari, Muslim), RETOLD FREELY in the wording of a graded reader. No sentence here is the text of a hadith and none may be cited as one; every i'rab line is the author's own analysis, pending scholarly review.",
  "tr": "ÖZGÜN 3. seviye kolaylaştırılmış Arapça: hadis kitaplarında (Buhârî, Müslim) nakledilen İsrailoğulları'ndan alacalı, kel ve kör kıssası, kolaylaştırılmış okuyucu üslûbuyla SERBESTÇE yeniden anlatılmıştır. Buradaki hiçbir cümle bir hadisin metni değildir ve hadis olarak aktarılamaz; her i'râb satırı yazarın kendi tahlilidir ve ilmî incelemeyi beklemektedir.",
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
