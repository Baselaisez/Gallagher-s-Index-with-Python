"""Author content/samples/al-asad-wa-al-far — «الْأَسَدُ وَالْفَأْرُ», the twenty-ninth ORIGINAL story, the ninth at Level 1 (wave 128).

ORIGINAL graded Arabic: the fable of the lion and the mouse (Aesop) retold for beginners — a mouse wakes a sleeping lion, begs
for mercy and promises to repay him; the lion laughs and lets him go; days later the lion is caught in a hunter's net and the
mouse gnaws the rope through. Fourteen sentences in four chapters; one entry new to the lexicon (شَبَكَة).
Regenerate with: python3 tools/authoring/author_asad_far.py
"""
import json, os, pathlib, sys
ROOT = pathlib.Path(__file__).resolve().parents[2] if (pathlib.Path(__file__).resolve().parents[2] / "content").exists() \
    else pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app")
OUT_ROOT = pathlib.Path(os.environ.get("QISSA_PKG_ROOT", str(ROOT / "content/samples")))
PKG = OUT_ROOT / "al-asad-wa-al-far"
(PKG / "chapters").mkdir(parents=True, exist_ok=True)
sys.path.insert(0, str(ROOT / "tools/authoring"))
from story_kit import *

PRON.update({"كَ": "pron-2ms", "ي": "pron-1s", "نِي": "pron-1s"}); PRON_AR.update({"كَ": "الْكَافُ", "ي": "الْيَاءُ", "نِي": "الْيَاءُ"})
MAQUL = ("، وَمَقُولُ الْقَوْلِ مَفْعُولٌ بِهِ", "; what is said is its object", "; mekûlü'l-kavl mef'ûlün bihtir")
QALA_H = lambda full, punct=None: MADI(full, "qala", ["hollow-verbs", "maful-bihi"], hidden=True, punct=punct, note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2])
MUDAF_NOTE = ("، مُضَافٌ", ", annexed", ", muzâf")
WIQ = ("، وَالنُّونُ لِلْوِقَايَةِ", "; the nun guards the verb's ending", "; nûn vikâye içindir")
MALIKA_MUNADA = lambda punct=None: tok("مَلِكَ", "malik-king", "noun", ["vocative-munada", "idafa-definiteness"],
    "مُنَادًى مُضَافٌ مَنْصُوبٌ بِالْفَتْحَةِ، مُضَافٌ.", "The called noun (munada): annexed, so it is in nasb; the first term of the idafa.", "Muzâf münâdâ, mansûb; muzâf.", punct=punct)
FA_ANA = lambda: tok("فَأَنَا", "ana", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"],
    "الْفَاءُ لِلتَّعْلِيلِ، وَأَنَا ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "The fa gives the reason; أَنَا «I» is a detached pronoun, built on sukun, in the seat of raf' as the mubtada.",
    "Fâ ta'lîl içindir; ene «ben» — munfasıl zamir, sükûn üzere mebnî, mahallen merfû mübtedâ.", segments=[seg("فَ", "fa", "conj"), seg("أَنَا", "ana", "pron")])
KH2 = lambda full, lex, punct=None: tok(full, lex, "noun", ["mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ.", "A second predicate, in raf'.", "İkinci haber, merfû.", punct=punct)
ANTA_MUB = lambda: tok("أَنْتَ", "anta", "pron", ["mubtada-khabar", "al-mabni-wal-mudmar"], "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.", "A detached pronoun «you», built on fatha, in the seat of raf' as the mubtada.", "Munfasıl zamir «sen», fetha üzere mebnî, mahallen merfû mübtedâ.")
JIDDAN = lambda punct=None: tok("جِدًّا", "jiddan", "noun", ["maful-mutlaq"], "نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ مَنْصُوبٌ بِالْفَتْحَةِ.", "«very» — stands in for the absolute object, in nasb.", "«çok» — mef'ûl-i mutlaktan nâib, mansûb.", punct=punct)
KAYFA = lambda: tok("كَيْفَ", "kayfa", "noun", ["al-istifham", "hal"], "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ حَالٌ.", "The interrogative noun «how?», built on fatha, in the seat of nasb as a hal.", "İstifham ismi «nasıl?», fetha üzere mebnî, hâl olarak mahallen mansûb.")
SADIQI_MUNADA = lambda punct=None: tok("صَدِيقِي", "sadiq-friend", "noun", ["vocative-munada", "ya-al-mutakallim", "idafa-definiteness", "al-bariz-al-muttasil"],
    "مُنَادًى مُضَافٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِالْحَرَكَةِ الْمُنَاسِبَةِ، وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
    "The called noun, annexed to the speaker's ya: in nasb by a fatha that cannot show, because the letter before the ya must carry the kasra; the ya is the second term of the idafa, in the seat of jarr.",
    "Mütekellim yâ'sına muzâf münâdâ: mansûb, fethası takdîrîdir (yâ'dan önceki harf kesre taşır); yâ muzâfun ileyh, mahallen mecrûr.", punct=punct, segments=[seg("صَدِيق", "sadiq-friend", "noun"), seg("ي", "pron-1s", "pron")])
WA_LAKINNAKA = lambda: tok("وَلٰكِنَّكَ", "lakinna", "part", ["inna-wa-akhawatuha", "kaanna-lakinna-layta-laalla-fil-kafiya", "al-bariz-al-muttasil"],
    WA_AR + "لٰكِنَّ حَرْفُ اسْتِدْرَاكٍ وَنَصْبٍ مُشَبَّهٌ بِالْفِعْلِ، وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ اسْمُهَا.", "The waw conjoins; لٰكِنَّ «but» corrects what went before and works like إِنَّ; the attached ka is its noun, in the seat of nasb.",
    "«ve» + lâkinne «fakat» — istidrâk ve nasb harfi, fiile benzer; bitişik kâf ismidir, mahallen mansûb.", segments=[seg("وَ", "wa", "conj"), seg("لٰكِنَّ", "lakinna", "part"), seg("كَ", "pron-2ms", "pron")])
FAL_DARS = lambda punct=None: tok("فَالدَّرْسُ", "dars", "noun", ["mubtada-khabar", "hadhf-wa-taqdir"],
    "الْفَاءُ لِلِاسْتِئْنَافِ، وَالدَّرْسُ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ، وَخَبَرُهُ مَحْذُوفٌ تَقْدِيرُهُ: هُوَ هٰذَا، وَالْجُمْلَةُ بَعْدَهُ تَفْسِيرٌ لَهُ.", "The fa opens a new clause; «the lesson» is the mubtada, in raf'; its predicate is understood («is this»), and the sentence after it spells it out.",
    "Fâ isti'nâf içindir; «ders» mübtedâ, merfû; haberi mahzûf («şudur»), sonraki cümle onu açıklar.", punct=punct, segments=[seg("فَ", "fa", "conj"), seg("الدَّرْسُ", "dars", "noun")])
FA_QAD = lambda: tok("فَقَدْ", "qad", "part", ["qad-harf"], "الْفَاءُ لِلتَّعْلِيلِ، وَقَدْ حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "The fa gives the reason; قَدْ before a present verb means «may, sometimes».", "Fâ ta'lîl içindir; muzâri önünde kad «bazen, -ebilir» (taklîl).", segments=[seg("فَ", "fa", "conj"), seg("قَدْ", "qad", "part")])
YAWMAN = lambda punct=None: ZARF("يَوْمًا", "yawm", kind="زَمَانٍ", kind_en="time", kind_tr="zaman", mudaf=False, punct=punct)
JAWAB = (" — وَالْجُمْلَةُ جَوَابُ الشَّرْطِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ", "; the clause is the answer of the condition and has no seat of its own", "; cümle şartın cevabıdır, i'râbdan mahalli yoktur")
KH_LAKINNA = (" — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لٰكِنَّ", "; the clause fills the seat of raf' as the predicate of لٰكِنَّ", "; cümle lâkinne'nin haberi olarak mahallen merfû")

TITLES = [{"ar": "الْأَسَدُ النَّائِمُ", "en": "The sleeping lion", "tr": "Uyuyan aslan"},
          {"ar": "الرَّحْمَةُ", "en": "Mercy", "tr": "Merhamet"},
          {"ar": "الشَّبَكَةُ", "en": "The net", "tr": "Ağ"},
          {"ar": "الدَّرْسُ", "en": "The lesson", "tr": "Ders"}]
S1 = []
S1.append({"id": "s1", "translation": {"en": "A big lion was asleep under a tree in the forest.", "tr": "Büyük bir aslan ormanda bir ağacın altında uyuyordu."},
 "tokens": [KANA("كَانَ"), ISMK("أَسَدٌ", "asad"), NAAT("كَبِيرٌ", "kabir", "raf"), KHK("نَائِمًا", "naim-sleeper", extra=["ism-fail"]), ZARF("تَحْتَ", "tahta"), MUDAF_ILAYH("شَجَرَةٍ", "shajara"), FI(), MAJR("الْغَابَةِ", "ghaba-forest", punct=".")]})
S1.append({"id": "s2", "translation": {"en": "A little mouse came and walked on the lion's head.", "tr": "Küçük bir fare geldi ve aslanın başının üstünde yürüdü."},
 "tokens": [MADI("فَجَاءَ", "jaa", ["hollow-verbs"]), FAIL("فَأْرٌ", "far-mouse"), NAAT("صَغِيرٌ", "saghir", "raf"), MADI_ALIF("وَمَشَى", "masha", hidden=True), ALA(), MAJR("رَأْسِ", "ras", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("الْأَسَدِ", "asad", punct=".")]})
S1.append({"id": "s3", "translation": {"en": "The lion rose from his sleep and seized the mouse with his paw.", "tr": "Aslan uykusundan kalktı ve fareyi eliyle yakaladı."},
 "tokens": [MADI("فَقَامَ", "qama", ["hollow-verbs"]), FAIL("الْأَسَدُ", "asad"), MIN(), ENC_NOUN("نَوْمِهِ", "nawm", "هِ", "majr"), MADI("وَأَمْسَكَ", "amsaka", ["form-iv-verbs"], hidden=True), MAFUL("الْفَأْرَ", "far-mouse"), BI_NOUN("بِيَدِهِ", "yad", "يَدِهِ", enc="هِ", punct=".")]})
S2 = []
S2.append({"id": "s1", "translation": {"en": "The mouse was afraid and said: «O king of the forest, have mercy on me, for I am small and weak.»", "tr": "Fare korktu ve dedi: «Ey ormanın kralı, bana merhamet et; çünkü ben küçük ve zayıfım.»"},
 "tokens": [MADI("خَافَ", "khafa", ["hollow-verbs"]), FAIL("الْفَأْرُ", "far-mouse"), QALA_H("وَقَالَ", punct=":"), YA(), MALIKA_MUNADA(), MUDAF_ILAYH("الْغَابَةِ", "ghaba-forest", punct="،"),
  AMR("ارْحَمْنِي", "rahima", enc="ي", wiqaya=True, punct="،"), FA_ANA(), KHABAR("صَغِيرٌ", "saghir"), KH2("ضَعِيفٌ", "daif", punct=".")]})
S2.append({"id": "s2", "translation": {"en": "«And if you let me go, I will serve you one day.»", "tr": "«Beni bırakırsan, bir gün sana hizmet ederim.»"},
 "tokens": [IN_SHART("وَإِنْ"), MADI_T("تَرَكْتَنِي", "taraka", who="anta", enc="نِي", shart=True, note_ar=WIQ[0], note_en=WIQ[1], note_tr=WIQ[2], punct="،"),
  MADI_T("خَدَمْتُكَ", "khadama-serve", who="ana", enc="كَ", extra=["al-majzum-wal-shart-wal-jaza"], note_ar=JAWAB[0], note_en=JAWAB[1], note_tr=JAWAB[2]), YAWMAN(punct=".")]})
S2.append({"id": "s3", "translation": {"en": "The lion laughed and said: «You are very small — how could you serve me?»", "tr": "Aslan güldü ve dedi: «Sen çok küçüksün; bana nasıl hizmet edersin?»"},
 "tokens": [MADI("ضَحِكَ", "dahika"), FAIL("الْأَسَدُ", "asad"), QALA_H("وَقَالَ", punct=":"), ANTA_MUB(), KHABAR("صَغِيرٌ", "saghir"), JIDDAN(punct="،"), KAYFA(),
  WIQAYA_V("تَخْدُمُنِي", "khadama-serve", "تَخْدُمُ", "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ", "present verb in raf'", "merfû muzâri", hidden="أَنْتَ", wujub=True, punct="؟")]})
S2.append({"id": "s4", "translation": {"en": "Then he let it go and slept.", "tr": "Sonra onu bıraktı ve uyudu."},
 "tokens": [THUMMA(), ENC_MADI("تَرَكَهُ", "taraka", "هُ", hidden=True), MADI("وَنَامَ", "nama", ["hollow-verbs"], hidden=True, punct=".")]})
S3 = []
S3.append({"id": "s1", "translation": {"en": "After some days the lion fell into a hunter's net.", "tr": "Birkaç gün sonra aslan bir avcının ağına düştü."},
 "tokens": [ZARF("بَعْدَ", "bada", kind="زَمَانٍ", kind_en="time", kind_tr="zaman"), MUDAF_ILAYH("أَيَّامٍ", "yawm", extra=["jam-taksir"], note_ar=" — جَمْعُ يَوْمٍ", note_en=" — the plural of «day»", note_tr=" — «gün»ün çoğulu"),
  MADI("وَقَعَ", "waqaa", ["mithal-verbs"]), FAIL("الْأَسَدُ", "asad"), FI(), MAJR("شَبَكَةِ", "shabaka", note_ar=MUDAF_NOTE[0], note_en=MUDAF_NOTE[1], note_tr=MUDAF_NOTE[2]), MUDAF_ILAYH("صَيَّادٍ", "sayyad", punct=".")]})
S3.append({"id": "s2", "translation": {"en": "The lion roared with a mighty voice.", "tr": "Aslan şiddetli bir sesle kükredi."},
 "tokens": [MADI("فَصَاحَ", "saha-shout", ["hollow-verbs"]), FAIL("الْأَسَدُ", "asad"), BI_NOUN("بِصَوْتٍ", "sawt", "صَوْتٍ"), NAAT("شَدِيدٍ", "shadid", "jarr", punct=".")]})
S3.append({"id": "s3", "translation": {"en": "The mouse heard his voice and came quickly.", "tr": "Fare onun sesini duydu ve hızla geldi."},
 "tokens": [MADI("سَمِعَ", "samia"), FAIL("الْفَأْرُ", "far-mouse"), ENC_NOUN("صَوْتَهُ", "sawt", "هُ", "maful", punct="،"), MADI("فَجَاءَ", "jaa", ["hollow-verbs"], hidden=True), HAL("سَرِيعًا", "sari", ["sifa-mushabbaha"], punct=".")]})
S3.append({"id": "s4", "translation": {"en": "The mouse cut the rope with its mouth, and the lion came out of the net.", "tr": "Fare ipi ağzıyla kesti ve aslan ağdan çıktı."},
 "tokens": [MADI("قَطَعَ", "qataa"), FAIL("الْفَأْرُ", "far-mouse"), MAFUL("الْحَبْلَ", "habl"), BI_NOUN("بِفَمِهِ", "fam", "فَمِهِ", enc="هِ", punct="،"), MADI("فَخَرَجَ", "kharaja"), FAIL("الْأَسَدُ", "asad"), MINA(), MAJR("الشَّبَكَةِ", "shabaka", punct=".")]})
S4 = []
S4.append({"id": "s1", "translation": {"en": "The lion said: «I thank you, my little friend!»", "tr": "Aslan dedi: «Teşekkür ederim, küçük dostum!»"},
 "tokens": [MADI("قَالَ", "qala", ["hollow-verbs", "maful-bihi"], note_ar=MAQUL[0], note_en=MAQUL[1], note_tr=MAQUL[2]), FAIL("الْأَسَدُ", "asad", punct=":"),
  MUDARI("أَشْكُرُكَ", "shakara", who="أَنَا", enc="كَ", wujub=True), YA(), SADIQI_MUNADA(), NAAT("الصَّغِيرَ", "saghir", "nasb", note_ar=" — نَعْتُ الْمُنَادَى الْمُضَافِ يَتْبَعُهُ فِي النَّصْبِ", note_en=" — the adjective follows the annexed munada in nasb", note_tr=" — muzâf münâdânın sıfatı nasbda ona uyar", punct="!")]})
S4.append({"id": "s2", "translation": {"en": "«You are small, but you have helped me.»", "tr": "«Sen küçüksün, ama bana fayda verdin.»"},
 "tokens": [ANTA_MUB(), KHABAR("صَغِيرٌ", "saghir", punct="،"), WA_LAKINNAKA(), MADI_T("نَفَعْتَنِي", "nafaa", who="anta", enc="نِي", note_ar=WIQ[0] + KH_LAKINNA[0], note_en=WIQ[1] + KH_LAKINNA[1], note_tr=WIQ[2] + KH_LAKINNA[2], punct=".")]})
S4.append({"id": "s3", "translation": {"en": "The lesson: do not laugh at the weak, for one day he may help you.", "tr": "Ders: zayıfa gülme; çünkü bir gün sana faydası dokunabilir."},
 "tokens": [FAL_DARS(punct=":"), LA_NAHIYA(), JAZM_V("تَضْحَكْ", "dahika", by="لَا النَّاهِيَةِ", by_en="the prohibitive لَا", by_tr="nehiy lâ'sı", hidden="أَنْتَ"), MINA(), MAJR("الضَّعِيفِ", "daif", punct="،"),
  FA_QAD(), MUDARI("يَنْفَعُكَ", "nafaa", who="هُوَ", enc="كَ"), YAWMAN(punct=".")]})
CHAPS = [S1, S2, S3, S4]
PREF = ["qisas-al-nabiyyin-1", "al-kafiya", "al-asad-wa-al-arnab", "al-ghurab-wa-al-thalab", "juha-wa-al-himar", "luqman-wa-ibnuh", "jurayj-al-abid", "al-rahma-bil-hayawan", "musa-wa-firawn", "izhar-al-asrar", "talkhis-al-miftah", "aqaid-ahl-al-sunna"]
def _pkg_dir(p): return (OUT_ROOT / p) if (OUT_ROOT / p / "glossary.json").exists() else (ROOT / "content/samples" / p)
PREF = [p for p in PREF if _pkg_dir(p).joinpath("glossary.json").exists()]
PREF += sorted(d.name for d in (ROOT / "content/samples").iterdir() if (d / "glossary.json").exists() and d.name not in PREF)
_G = {p: json.loads((_pkg_dir(p) / "glossary.json").read_text(encoding="utf-8"))["entries"] for p in PREF}
_M = {p: json.loads((_pkg_dir(p) / "morphology.json").read_text(encoding="utf-8")).get("verbs", {}) for p in PREF if (_pkg_dir(p) / "morphology.json").exists()}
def find_gloss(k):
    for p in PREF:
        if k in _G[p]: return _G[p][k]
    return None
def find_verb(k):
    for p in PREF:
        if k in _M.get(p, {}): return _M[p][k]
    return None
NEW_GLOSS = {
 "shabaka": {"lemma": "شَبَكَة", "root": "ش ب ك", "pos": "noun", "plural": "شِبَاك", "gloss": {"en": "a net", "tr": "ağ"}, "level": 1},
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
    v = find_verb(k)
    if v: MORPH["verbs"][k] = v
no_par = [k for k, e in GLOSS.items() if e.get("pos") == "verb" and k not in MORPH["verbs"]]
assert not no_par, no_par
LEVEL_NAME = json.loads((ROOT / "content/samples/musa-wa-firawn/manifest.json").read_text(encoding="utf-8")).get("levelName", "Beginner")
MANIFEST = {
 "id": "al-asad-wa-al-far", "storyGroup": "al-asad-wa-al-far",
 "title": {"ar": "الْأَسَدُ وَالْفَأْرُ", "en": "The Lion and the Mouse", "tr": "Aslan ile Fare"},
 "subtitle": {"ar": "فَأْرٌ صَغِيرٌ أَنْقَذَ أَسَدًا كَبِيرًا مِنَ الشَّبَكَةِ — حِكَايَةٌ لِلْمُسْتَوَى الْأَوَّلِ", "en": "A little mouse frees a great lion from the net — a fable for Level 1", "tr": "Küçük bir fare büyük bir aslanı ağdan kurtarır — 1. seviye için bir fabl"},
 "level": 1, "levelName": LEVEL_NAME, "version": "0.1.0", "published": "2026-11-09", "access": "free",
 "chapters": [{"n": i + 1, "title": t} for i, t in enumerate(TITLES)],
 "attribution": {
  "ar": "إِعَادَةُ صِيَاغَةٍ أَصْلِيَّةٌ مُبَسَّطَةٌ (الْمُسْتَوَى الْأَوَّلُ) لِحِكَايَةِ الْأَسَدِ وَالْفَأْرِ الْمَشْهُورَةِ (إِيسُوب)، بِأُسْلُوبِ كِتَابِ الْقِرَاءَةِ الْمُدَرَّجَةِ. لَمْ يُنْقَلْ نَصٌّ مِنْ أَيِّ مَصْدَرٍ.",
  "en": "ORIGINAL Level-1 graded Arabic: the well-known fable of the lion and the mouse (Aesop) retold for beginners in the wording of a graded reader. No text is quoted from any source.",
  "tr": "ÖZGÜN 1. seviye kolaylaştırılmış Arapça: meşhur aslan ile fare fablı (Ezop), kolaylaştırılmış okuyucu üslûbuyla yeni başlayanlar için yeniden anlatılmıştır. Hiçbir kaynaktan metin aktarılmamıştır.",
  "reviewStatus": "pending-scholarly-review"},
}
(PKG / "manifest.json").write_text(json.dumps(MANIFEST, ensure_ascii=False, indent=1), encoding="utf-8")
for i, S in enumerate(CHAPS, 1):
    (PKG / f"chapters/{i}.json").write_text(json.dumps({"chapter": i, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "glossary.json").write_text(json.dumps({"entries": GLOSS}, ensure_ascii=False, indent=1), encoding="utf-8")
(PKG / "morphology.json").write_text(json.dumps(MORPH, ensure_ascii=False, indent=1), encoding="utf-8")
ALL = [s for S in CHAPS for s in S]
print("sentences:", len(ALL), "tokens:", sum(len(s["tokens"]) for s in ALL), "gloss:", len(GLOSS), "verbs:", len(MORPH["verbs"]), "->", PKG)
