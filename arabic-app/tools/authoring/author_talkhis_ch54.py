# -*- coding: utf-8 -*-
"""Author chapter 54 of talkhis-al-miftah — الِاسْتِعَارَةُ بِالْكِنَايَةِ
وَالتَّخْيِيلِيَّةُ، وَحُسْنُ الِاسْتِعَارَةِ (sahifa 129-133, lines ~3740-3900): the
likening hidden in the mind with only the mushabbah spoken (the MAKNIYYA) and
the thing of the bihi's attributed to it (the TAKHYILIYYA); Sakkaki's division
and the two replies; the conditions of a good istiʿara (the jamiʿ plain, no
scent of the likening in the wording) and the compound built on the hadith of
the hundred camels.

  RESTORED (the source carries the step only in Turkish): s1-s3, s5, s7, s9-s10,
          s12-s18, and the frames of the examples.
  As printed: the bayts of Abu Dhuʾayb al-Hudhali (s4), of s6, of Zuhayr (s8);
          the hadiths of s11 and s19.

Every makniyya carries TWO authored frames: the `makniyya` on the spoken
mushabbah (with the tarshih words by index) and the `takhyiliyya` on the
attributed thing; the tashbihs of the musannif's own explanations (شَبَّهَ …
بِـ… فِي…) carry tashbih frames.
"""

import json, pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
PKG = ROOT / "content/samples/talkhis-al-miftah"
sys.path.insert(0, str(ROOT / "tools/authoring"))
import sarf_gen as _sg
DIA = re.compile("[ً-ٰ]")
def bare(s): return DIA.sub("", s)
def tok(full, lex, pos, grammar, ar, en, tr, punct=None, segments=None):
    t = {"surface": {"full": full, "smart": full, "bare": bare(full)}, "lex": lex, "pos": pos}
    if grammar: t["grammar"] = grammar
    t["irab"] = {"ar": ar, "en": en, "tr": tr}
    if segments: t["segments"] = segments
    if punct: t["punctAfter"] = punct
    return t
def seg(form, lex, pos): return {"form": form, "lex": lex, "pos": pos}
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
def find_gloss(key):
    for p in sorted((ROOT / "content/samples").iterdir()):
        gp = p / "glossary.json"
        if gp.exists():
            d = json.loads(gp.read_text(encoding="utf-8"))["entries"]
            if key in d: return d[key]
    raise KeyError(key)
def _has_gloss(key):
    try: find_gloss(key); return True
    except KeyError: return False
def find_morph(key):
    for p in sorted((ROOT / "content/samples").iterdir()):
        gp = p / "morphology.json"
        if gp.exists():
            d = json.loads(gp.read_text(encoding="utf-8"))["verbs"]
            if key in d: return d[key]
    raise KeyError(key)
def mj(word, kind, alaqa=None, haqiqa=None, murad=None, qarina=None, istiara=None):
    f = {"word": word, "kind": kind}
    if alaqa: f["alaqa"] = alaqa
    if haqiqa: f["haqiqa"] = haqiqa
    if murad: f["murad"] = murad
    if qarina is not None: f["qarina"] = qarina
    if istiara: f["istiara"] = istiara
    return f
def ist(lafz, ends=None, jami=None, hissi=None, seat=None, mulaim=None, minhu=None, lahu=None):
    d = {"lafz": lafz}
    if ends: d["ends"] = ends
    if jami: d["jami"] = jami
    if hissi: d["hissi"] = hissi
    if seat: d["qarinaSeat"] = seat
    if mulaim: d["mulaim"] = mulaim
    if minhu: d["mulaimMinhu"] = minhu
    if lahu: d["mulaimLahu"] = lahu
    return d
S = []
M = "istiara-makniyya"; H = "husn-al-istiara"; K = "majaz-murakkab"; T = "istiara-tabaiyya"; R = "tarshih-wa-tajrid"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"
TITLE54 = {"ar": "الِاسْتِعَارَةُ بِالْكِنَايَةِ وَالتَّخْيِيلِيَّةُ، وَمَذْهَبُ السَّكَّاكِيِّ، وَحُسْنُ الِاسْتِعَارَةِ",
           "en": "The Istiʿara by Kinaya and the Takhyiliyya, Sakkaki's View, and the Beauty of the Istiʿara",
           "tr": "Kinâye Yoluyla İstiâre ve Tahyîliyye, Sekkâkî'nin Görüşü, ve İstiârenin Güzelliği"}
def kaq(full="كَقَوْلِهِ", who="pron-3ms", punct=":", tag=M):
    pr = {"pron-3ms": "هِ", "pron-3mp": "هِمْ", "pron-2ms": "كَ"}[who]
    return tok(full, "qawl", "noun", [tag, "huruf-jarr", "idafa-definiteness"],
               "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
               "«as in his/your saying» — the kaf of «for instance», a wall: no likening.", "«sözü gibi» — «meselâ» kâfı, duvar: benzetme değil.",
               segments=[seg("كَ", "ka", "part"), seg("قَوْلِ", "qawl", "noun"), seg(pr, who, "pron")], punct=punct)
def kawa(full="وَكَقَوْلِهِ", who="pron-3ms", tag=M):
    t = kaq(full, who, ":", tag); t["segments"].insert(0, seg("وَ", "wa", "conj")); return t
SAW = tok("ﷺ", "salla-allahu", "part", [M], "جُمْلَةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ.", "«peace be upon him» — a parenthetical prayer.", "«sallallâhu aleyhi ve sellem» — mu'terize dua.", punct=":")

# ----------- s1 — the likening hidden in the mind (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "The likening may be HIDDEN in the mind, so that none of its arkan is spoken except the MUSHABBAH." + R_EN,
 "tr": "Benzetme nefiste GİZLENEBİLİR; öyle ki rükünlerinden MÜŞEBBEH dışında hiçbiri açıkça söylenmez." + R_TR},
 "tokens": [
  tok("قَدْ","qad","part",[M, "qad-harf"], "حَرْفُ تَقْلِيلٍ مَعَ الْمُضَارِعِ.", "«sometimes» — qad with a mudari'.", "«bazen» — muzâri ile kad."),
  tok("يُضْمَرُ","admara","verb",[M, "naib-al-fail", "form-iv-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«is hidden» — the passive mudari' of Form IV.", "«gizlenir» — IV. bâbın meçhûl muzârii."),
  tok("التَّشْبِيهُ","tashbih","noun",[M, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the likening» — the deputy doer.", "«benzetme» — nâib-i fâil."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("النَّفْسِ","nafs","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the mind».", "«nefis, zihin»."),
  tok("فَلَا","la-nafiya","part",[M, "atf-nasaq"], "الْفَاءُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«so … not».", "«böylece … -mez».",
      segments=[seg("فَ","fa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُصَرَّحُ","sarraha","verb",[M, "naib-al-fail", "form-ii-verbs", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ الْجَارُّ وَالْمَجْرُورُ بَعْدَهُ.", "«is spoken openly» — the passive; the jarr-majrur after it deputises.", "«açıkça söylenir» — meçhûl; sonraki câr-mecrûr nâib-i fâil."),
  tok("بِشَيْءٍ","shay","noun",[M, "huruf-jarr", "naib-al-fail"], "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعِ نَائِبِ الْفَاعِلِ.", "«of anything» — in the place of raf' as the deputy doer.", "«bir şey» — nâib-i fâil olarak ref mahallinde.",
      segments=[seg("بِ","bi","part"), seg("شَيْءٍ","shay","noun")]),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.", "«of» — partitive.", "«-den» — teb'îz."),
  tok("أَرْكَانِهِ","rukn","noun",[M, "huruf-jarr", "idafa-definiteness", "jam-taksir"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ رُكْنٍ.", "«its arkan» — plural of رُكْن.", "«rükünlerinden» — رُكْن'ün çoğulu.",
      segments=[seg("أَرْكَانِ","rukn","noun"), seg("هِ","pron-3ms","pron")]),
  tok("سِوَى","siwa","noun",[M, "istithna"], "أَدَاةُ اسْتِثْنَاءٍ — اسْمٌ مَنْصُوبٌ عَلَى الِاسْتِثْنَاءِ بِفَتْحَةٍ مُقَدَّرَةٍ، مُضَافٌ.", "«except» — the noun of exception, a mudaf.", "«dışında» — istisnâ ismi, muzâf."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[M, "istithna", "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الرُّكْنُ الْوَحِيدُ الْمَذْكُورُ.", "«the mushabbah» — mudaf ilayh; the one rukn spoken.", "«müşebbeh» — muzâfun ileyh; söylenen tek rükün.", punct=".")]})

# ----------- s2 — how it is signalled (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And it is signalled by AFFIRMING for the mushabbah a thing that belongs PROPERLY to the mushabbah bihi." + R_EN,
 "tr": "Ona, müşebbeh için müşebbehün bihe HAS bir şeyin İSBAT EDİLMESİYLE delâlet edilir." + R_TR},
 "tokens": [
  tok("وَيُدَلُّ","dalla","verb",[M, "naib-al-fail", "doubled-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيُدَلُّ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ — مُضَاعَفٌ.", "«and it is signalled» — the passive of the doubled دَلَّ.", "«ve delâlet edilir» — muzâaf دَلَّ'nin meçhûlü.",
      segments=[seg("وَ","wa","conj"), seg("يُدَلُّ","dalla","verb")]),
  tok("عَلَيْهِ","ala","part",[M, "huruf-jarr", "naib-al-fail"], "جَارٌّ وَمَجْرُورٌ نَائِبُ فَاعِلٍ.", "«to it» — the deputy doer.", "«ona» — nâib-i fâil.",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")]),
  tok("بِأَنْ","an-masdariyya","part",[M, "huruf-jarr", "an-masdariyya"], "الْبَاءُ جَارَّةٌ، وَأَنْ مَصْدَرِيَّةٌ نَاصِبَةٌ.", "«by that» — the ba over the masdar-making أَنْ.", "«… ile» — masdar yapan أَنْ üzerinde bâ.",
      segments=[seg("بِ","bi","part"), seg("أَنْ","an-masdariyya","part")]),
  tok("يُثْبَتَ","athbata","verb",[M, "an-masdariyya", "naib-al-fail", "form-iv-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، مَبْنِيٌّ لِلْمَجْهُولِ.", "«is affirmed» — nasb by أَنْ; passive.", "«isbat edilir» — أَنْ ile mansûb; meçhûl."),
  tok("لِلْمُشَبَّهِ","mushabbah","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for the mushabbah».", "«müşebbeh için».",
      segments=[seg("لِ","li","part"), seg("الْمُشَبَّهِ","mushabbah","noun")]),
  tok("أَمْرٌ","amr","noun",[M, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a thing» — the deputy doer.", "«bir şey» — nâib-i fâil."),
  tok("مُخْتَصٌّ","mukhtass","noun",[M, "naat-sifa", "ism-fail", "form-viii-verbs", "doubled-verbs"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلِ اخْتَصَّ.", "«proper to» — a na't; ism fa'il of the doubled Form VIII.", "«has olan» — na't; muzâaf VIII. bâbın ism-i fâili."),
  tok("بِالْمُشَبَّهِ","mushabbah","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«to the mushabbah».", "«müşebbeh».",
      segments=[seg("بِ","bi","part"), seg("الْمُشَبَّهِ","mushabbah","noun")]),
  tok("بِهِ","bi","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — تَمَامُ اسْمِ الْمُشَبَّهِ بِهِ.", "«bihi» — completing «mushabbah bihi».", "«bih» — müşebbehün bih adının tamamı.",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s3 — the two names (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "So the likening is called an ISTIʿARA BY KINAYA, or one KEPT HIDDEN; and the affirming of that thing, an istiʿara TAKHYILIYYA." + R_EN,
 "tr": "Böylece benzetmeye KİNÂYE YOLUYLA İSTİÂRE yahut KENDİSİNDEN KİNÂYE EDİLEN istiâre; o şeyin isbatına ise TAHYÎLİYYE istiâre denir." + R_TR},
 "tokens": [
  tok("فَيُسَمَّى","samma","verb",[M, "naib-al-fail", "form-ii-verbs", "mafulayn", "naqis-verbs"], "الْفَاءُ لِلتَّفْرِيعِ، وَيُسَمَّى فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.", "«so it is called» — the passive of the naqis Form II.", "«böylece … denir» — nâkıs II. bâbın meçhûlü.",
      segments=[seg("فَ","fa","conj"), seg("يُسَمَّى","samma","verb")]),
  tok("التَّشْبِيهُ","tashbih","noun",[M, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the likening» — the deputy doer.", "«benzetme» — nâib-i fâil."),
  tok("اسْتِعَارَةً","istiara","noun",[M, "mafulayn"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ.", "«an istiʿara» — the second object.", "«istiâre» — ikinci mef'ûl."),
  tok("بِالْكِنَايَةِ","kinaya","noun",[M, "huruf-jarr", "naat-sifa"], "جَارٌّ وَمَجْرُورٌ نَعْتٌ — بِالْكِنَايَةِ: لِأَنَّ الْمُشَبَّهَ بِهِ مَكْنِيٌّ عَنْهُ.", "«by kinaya» — a na't: the bihi is only hinted at.", "«kinâye yoluyla» — na't: bih yalnız ima edilmiştir.",
      segments=[seg("بِ","bi","part"), seg("الْكِنَايَةِ","kinaya","noun")]),
  tok("أَوْ","aw","conj",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("مَكْنِيًّا","makni","noun",[M, "atf-nasaq", "ism-maful", "naqis-verbs"], "مَعْطُوفٌ مَنْصُوبٌ — اسْمُ مَفْعُولِ كَنَى.", "«kept hidden» — joined; ism maf'ul of the naqis كَنَى.", "«kinâye edilen» — matuf; nâkıs كَنَى'nın ism-i mef'ûlü."),
  tok("عَنْهَا","an","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — عَنِ الِاسْتِعَارَةِ.", "«from it».", "«ondan».",
      segments=[seg("عَنْ","an","part"), seg("هَا","pron-3fs","pron")], punct="،"),
  tok("وَإِثْبَاتُ","ithbat","noun",[M, "mubtada-khabar", "idafa-definiteness", "masdar", "form-iv-verbs"], "الْوَاوُ عَاطِفَةٌ، وَإِثْبَاتُ مُبْتَدَأٌ مُضَافٌ — مَصْدَرُ أَثْبَتَ.", "«and the affirming of» — the mubtada, a mudaf; the masdar of Form IV.", "«ve isbatı» — mübtedâ, muzâf; IV. bâbın masdarı.",
      segments=[seg("وَ","wa","conj"), seg("إِثْبَاتُ","ithbat","noun")]),
  tok("ذَلِكَ","dhalika","pron",[M, "asma-al-ishara", "idafa-definiteness"], "اسْمُ إِشَارَةٍ مُضَافٌ إِلَيْهِ.", "«that» — the demonstrative, mudaf ilayh.", "«o» — işaret ismi, muzâfun ileyh."),
  tok("الْأَمْرِ","amr","noun",[M, "badal"], "بَدَلٌ مِنِ اسْمِ الْإِشَارَةِ مَجْرُورٌ.", "«thing» — badal of the demonstrative.", "«şeyin» — işaret isminin bedeli."),
  tok("اسْتِعَارَةً","istiara","noun",[M, "mubtada-khabar", "mafulayn"], "مَفْعُولٌ ثَانٍ لِفِعْلٍ مَحْذُوفٍ (يُسَمَّى) مَنْصُوبٌ — وَالْجُمْلَةُ خَبَرٌ.", "«an istiʿara» — the second object of a dropped «is called»; the clause is the khabar.", "«istiâre» — hazfedilmiş «denir»in ikinci mef'ûlü; cümle haber."),
  tok("تَخْيِيلِيَّةً","takhyiliyya","noun",[M, "naat-sifa", "ism-mansub"], "نَعْتٌ مَنْصُوبٌ — مَنْسُوبٌ إِلَى التَّخْيِيلِ.", "«takhyiliyya» — a na't; nisba to التَّخْيِيل.", "«tahyîliyye» — na't; tahyîle nisbet.", punct=".")]})

# ----------- s4 — Abu Dhuʾayb's bayt (as printed)
S.append({"id": "s4", "translation": {
 "en": "As in the Hudhali's saying: «And when DEATH has fastened its CLAWS, • you find every amulet of no avail».",
 "tr": "Hüzelî'nin şu sözü gibi: «ÖLÜM PENÇELERİNİ geçirdi mi, • her muskayı faydasız bulursun»."},
 "majaz": [mj(3, "makniyya", "mushabaha", {"en": "death", "tr": "ölüm"}, {"en": "a beast of prey — the bihi kept hidden, the likening in the mind", "tr": "yırtıcı hayvan — gizli tutulan bih, benzetme zihinde"},
              istiara=ist("makniyya", minhu=[4])),
           mj(5, "takhyiliyya", "mushabaha", {"en": "its claws", "tr": "pençeleri"}, {"en": "the means by which death seizes — a thing of the beast's, imagined for death", "tr": "ölümün yakalama vasıtası — yırtıcıya ait bir şey, ölüm için tahayyül edilmiş"},
              istiara=ist("takhyiliyya"))],
 "tokens": [
  tok("كَقَوْلِ","qawl","noun",[M, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ.", "«as in the saying of» — the kaf of «for instance», a wall.", "«sözü gibi» — «meselâ» kâfı, duvar.",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")]),
  tok("الْهُذَلِيِّ","hudhali","noun",[M, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — أَبُو ذُؤَيْبٍ الْهُذَلِيُّ.", "«the Hudhali» — Abu Dhuʾayb; mudaf ilayh.", "«Hüzelî» — Ebû Züeyb; muzâfun ileyh.", punct=":"),
  tok("وَإِذَا","idha","part",[M, "idha-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِذَا ظَرْفٌ مُتَضَمِّنٌ مَعْنَى الشَّرْطِ.", "«and when» — idha of the shart.", "«ve … -diğinde» — şart mânâlı izâ.",
      segments=[seg("وَ","wa","conj"), seg("إِذَا","idha","part")]),
  tok("الْمَنِيَّةُ","maniyya","noun",[M, "idha-shartiyya", "fail"], "فَاعِلٌ لِفِعْلٍ مَحْذُوفٍ يُفَسِّرُهُ الْمَذْكُورُ (إِذَا أَنْشَبَتِ الْمَنِيَّةُ) — الْمُشَبَّهُ الْمَذْكُورُ: اسْتِعَارَةٌ بِالْكِنَايَةِ، شُبِّهَتْ بِالسَّبُعِ وَطُوِيَ ذِكْرُهُ.",
      "«death» — the fa'il of a dropped verb the spoken one explains. The MUSHABBAH spoken alone: an istiʿara BY KINAYA — death likened to a beast of prey whose name is folded away.",
      "«ölüm» — söylenen fiilin açıkladığı hazfedilmiş fiilin fâili. Yalnız MÜŞEBBEH söylenmiş: KİNÂYE YOLUYLA istiâre — ölüm, adı dürülmüş yırtıcıya benzetilmiş."),
  tok("أَنْشَبَتْ","anshaba","verb",[M, "idha-shartiyya", "form-iv-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ مِنَ الرَّابِعِ، وَالتَّاءُ لِلتَّأْنِيثِ — تَرْشِيحٌ: الْإِنْشَابُ مِنْ لَوَازِمِ السَّبُعِ.", "«has fastened» — Form IV; a TARSHIH: fastening claws belongs to the beast.", "«geçirdi» — IV. bâb; TERŞÎH: pençe geçirmek yırtıcıya aittir.",
      segments=[seg("أَنْشَبَ","anshaba","verb"), seg("تْ","ta-tanith","part")]),
  tok("أَظْفَارَهَا","zufr","noun",[M, "maful-bihi", "idafa-definiteness", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَهَا مُضَافٌ إِلَيْهِ — الِاسْتِعَارَةُ التَّخْيِيلِيَّةُ: أُثْبِتَ لِلْمَنِيَّةِ مَا يَخْتَصُّ بِالسَّبُعِ.",
      "«its claws» — the object; the TAKHYILIYYA: a thing proper to the beast is affirmed for death.",
      "«pençelerini» — mef'ûl; TAHYÎLİYYE: yırtıcıya has olan, ölüm için isbat edilmiş.",
      segments=[seg("أَظْفَارَ","zufr","noun"), seg("هَا","pron-3fs","pron")], punct="•"),
  tok("أَلْفَيْتَ","alfa","verb",[M, "idha-shartiyya", "mafulayn", "form-iv-verbs", "naqis-verbs"], "فِعْلٌ مَاضٍ مِنَ الرَّابِعِ، وَالتَّاءُ فَاعِلٌ — جَوَابُ إِذَا؛ مِنْ أَفْعَالِ الْقُلُوبِ يَنْصِبُ مَفْعُولَيْنِ.", "«you find» — Form IV naqis; the jawab of إِذَا; a heart-verb with two objects.", "«bulursun» — IV. bâb nâkıs; izânın cevabı; iki mef'ûllü kalp fiili.",
      segments=[seg("أَلْفَيْ","alfa","verb"), seg("تَ","pron-2ms","pron")]),
  tok("كُلَّ","kull","noun",[M, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ، مُضَافٌ.", "«every» — the first object, a mudaf.", "«her» — birinci mef'ûl, muzâf."),
  tok("تَمِيمَةٍ","tamima","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«amulet» — mudaf ilayh.", "«muska» — muzâfun ileyh."),
  tok("لَا","la-nafiya","part",[M, "mafulayn"], "حَرْفُ نَفْيٍ.", "«not».", "«-mez»."),
  tok("تَنْفَعُ","nafaa","verb",[M, "mafulayn", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ مَفْعُولٌ ثَانٍ.", "«avails» — the clause is the second object.", "«fayda verir» — cümle ikinci mef'ûl.", punct=".")]})

# ----------- s5 — the musannif's explanation (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "He likened death to a beast of prey in the snatching of lives, and affirmed for it the CLAWS, by which the beast's preying is complete." + R_EN,
 "tr": "Ölümü, canları kapmakta yırtıcıya benzetmiş ve ona, yırtıcının parçalamasının kemâlinin kendisiyle olduğu PENÇELERİ isbat etmiştir." + R_TR},
 "tashbih": {"kind": "mursal-mufassal", "mushabbah": [1], "bihi": [2], "adat": 0, "wajh": [3, 4, 5]},
 "tokens": [
  tok("شَبَّهَ","shabbaha","verb",[M, "form-ii-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ (الشَّاعِرُ) — أَدَاةُ التَّشْبِيهِ فِعْلٌ.", "«he likened» — the doer hidden (the poet); the adat is a verb.", "«benzetti» — fâil gizli (şair); edat fiildir."),
  tok("الْمَنِيَّةَ","maniyya","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُشَبَّهُ.", "«death» — the object; the mushabbah.", "«ölümü» — mef'ûl; müşebbeh."),
  tok("بِالسَّبُعِ","sabu","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to the beast of prey» — the bihi.", "«yırtıcıya» — bih.",
      segments=[seg("بِ","bi","part"), seg("السَّبُعِ","sabu","noun")]),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ — يَجُرُّ وَجْهَ الشَّبَهِ.", "«in» — governs the wajh.", "«-de» — vechi cer eder."),
  tok("اغْتِيَالِ","ightiyal","noun",[M, "huruf-jarr", "idafa-definiteness", "form-viii-verbs", "masdar"], "مَجْرُورٌ، مُضَافٌ — وَجْهُ الشَّبَهِ؛ مَصْدَرُ اغْتَالَ.", "«the snatching of» — the wajh; the masdar of Form VIII.", "«kapmak» — vech; VIII. bâbın masdarı."),
  tok("النُّفُوسِ","nafs","noun",[M, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ نَفْسٍ.", "«lives» — mudaf ilayh; plural of نَفْس.", "«canları» — muzâfun ileyh; نَفْس'in çoğulu.", punct="،"),
  tok("وَأَثْبَتَ","athbata","verb",[M, "atf-nasaq", "form-iv-verbs", "maful-bihi"], "مَعْطُوفٌ — فِعْلٌ مَاضٍ مِنَ الرَّابِعِ.", "«and affirmed» — joined; Form IV.", "«ve isbat etti» — matuf; IV. bâb.",
      segments=[seg("وَ","wa","conj"), seg("أَثْبَتَ","athbata","verb")]),
  tok("لَهَا","li","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — لِلْمَنِيَّةِ.", "«for it» — for death.", "«ona» — ölüme.",
      segments=[seg("لَ","li","part"), seg("هَا","pron-3fs","pron")]),
  tok("الْأَظْفَارَ","zufr","noun",[M, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the claws» — the object.", "«pençeleri» — mef'ûl."),
  tok("الَّتِي","allati","pron",[M, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ لِلْأَظْفَارِ.", "«by which» — the relative as a na't.", "«… olan» — na't olarak mevsûl."),
  tok("بِهَا","bi","part",[M, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — صِلَةٌ.", "«by them» — the khabar brought forward; the sila.", "«onlarla» — öne alınmış haber; sıla.",
      segments=[seg("بِ","bi","part"), seg("هَا","pron-3fs","pron")]),
  tok("كَمَالُ","kamal","noun",[M, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the completeness of» — the mubtada, held back; a mudaf.", "«kemâli» — geriye bırakılmış mübtedâ; muzâf."),
  tok("افْتِرَاسِهِ","iftiras","noun",[M, "idafa-definiteness", "form-viii-verbs", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ افْتَرَسَ.", "«its preying» — mudaf ilayh with its pronoun; the masdar of Form VIII.", "«parçalamasının» — muzâfun ileyh ve zamiri; VIII. bâbın masdarı.",
      segments=[seg("افْتِرَاسِ","iftiras","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s6 — the bayt of the tongue of the state (as printed)
S.append({"id": "s6", "translation": {
 "en": "And as in his saying: «Though I speak in thanks for your kindness, eloquent, • the TONGUE of my STATE is more eloquent in complaint».",
 "tr": "Ve şairin şu sözü gibi: «İyiliğine şükürle, açık açık konuşsam da, • HÂLİMİN DİLİ şikâyette daha konuşkandır»."},
 "majaz": [mj(7, "makniyya", "mushabaha", {"en": "my state", "tr": "hâlim"}, {"en": "a speaking person — the bihi hidden", "tr": "konuşan bir insan — bih gizli"},
              istiara=ist("makniyya", minhu=[9])),
           mj(6, "takhyiliyya", "mushabaha", {"en": "the tongue of", "tr": "dili"}, {"en": "the state's means of indicating — a speaker's organ imagined for it", "tr": "hâlin delâlet vasıtası — konuşana ait uzuv, hâl için tahayyül edilmiş"},
              istiara=ist("takhyiliyya"))],
 "tokens": [
  kawa("وَكَقَوْلِهِ"),
  tok("وَلَئِنْ","in-shartiyya","part",[M, "in-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ مُوَطِّئَةٌ لِلْقَسَمِ، وَإِنْ شَرْطِيَّةٌ.", "«and even if» — the lam preparing an oath over the shart's إِنْ.", "«ve … -sam da» — şartın إِنْ'i üzerinde kasem lâmı.",
      segments=[seg("وَ","wa","conj"), seg("لَ","lam-qasam","part"), seg("إِنْ","in-shartiyya","part")]),
  tok("نَطَقْتُ","nataqa","verb",[M, "in-shartiyya", "fail"], "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ.", "«I speak» — the verb of the shart; the ta the doer.", "«konuşsam» — şart fiili; tâ fâil.",
      segments=[seg("نَطَقْ","nataqa","verb"), seg("تُ","pron-1s","pron")]),
  tok("بِشُكْرِ","shukr","noun",[M, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«in thanks for» — a mudaf.", "«şükrüyle» — muzâf.",
      segments=[seg("بِ","bi","part"), seg("شُكْرِ","shukr","noun")]),
  tok("بِرِّكَ","birr","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.", "«your kindness» — mudaf ilayh with its pronoun.", "«iyiliğinin» — muzâfun ileyh ve zamiri.",
      segments=[seg("بِرِّ","birr","noun"), seg("كَ","pron-2ms","pron")]),
  tok("مُفْصِحًا","mufsih","noun",[M, "hal", "ism-fail", "form-iv-verbs"], "حَالٌ مَنْصُوبٌ — اسْمُ فَاعِلِ أَفْصَحَ.", "«eloquently» — a hal; ism fa'il of Form IV.", "«açıkça» — hâl; IV. bâbın ism-i fâili.", punct="•"),
  tok("فَلِسَانُ","lisan","noun",[M, "in-shartiyya", "mubtada-khabar", "idafa-definiteness"], "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَلِسَانُ مُبْتَدَأٌ مُضَافٌ — الِاسْتِعَارَةُ التَّخْيِيلِيَّةُ: أُثْبِتَ لِلْحَالِ مَا يَخْتَصُّ بِالْمُتَكَلِّمِ.",
      "«then the tongue of» — the fa binding the jawab; the mubtada, a mudaf. The TAKHYILIYYA: a thing of the speaker's is affirmed for the state.",
      "«dili» — cevabı bağlayan fâ; mübtedâ, muzâf. TAHYÎLİYYE: konuşana has olan, hâl için isbat edilmiş.",
      segments=[seg("فَ","fa","conj"), seg("لِسَانُ","lisan","noun")]),
  tok("حَالِي","hal","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، وَالْيَاءُ مُضَافٌ إِلَيْهِ — الْمُشَبَّهُ الْمَذْكُورُ: اسْتِعَارَةٌ بِالْكِنَايَةِ، شُبِّهَتِ الْحَالُ بِإِنْسَانٍ مُتَكَلِّمٍ.",
      "«my state» — mudaf ilayh with the speaker's ya. The MUSHABBAH spoken: an istiʿara BY KINAYA — the state likened to a speaking person.",
      "«hâlimin» — mütekellim yâsıyla muzâfun ileyh. Söylenen MÜŞEBBEH: KİNÂYE YOLUYLA istiâre — hâl, konuşan bir insana benzetilmiş.",
      segments=[seg("حَالِ","hal","noun"), seg("ي","pron-1s","pron")]),
  tok("بِالشِّكَايَةِ","shikaya","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَنْطَقُ.", "«in complaint» — hangs on «more eloquent».", "«şikâyette» — «daha konuşkan»a bağlı.",
      segments=[seg("بِ","bi","part"), seg("الشِّكَايَةِ","shikaya","noun")]),
  tok("أَنْطَقُ","antaq","noun",[M, "mubtada-khabar", "ism-tafdil", "mamnu-min-sarf"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ؛ تَرْشِيحٌ: النُّطْقُ مِنْ لَوَازِمِ الْمُتَكَلِّمِ.", "«more eloquent» — the khabar; an ism tafdil. A TARSHIH: speaking belongs to the speaker.", "«daha konuşkan» — haber; ism-i tafdîl. TERŞÎH: konuşmak konuşana aittir.", punct=".")]})

# ----------- s7 — the explanation (RESTORED)
S.append({"id": "s7", "translation": {
 "en": "He likened the state to a speaking human in indicating, and affirmed for it the TONGUE, on which indicating stands." + R_EN,
 "tr": "Hâli, delâlette konuşan bir insana benzetmiş ve ona, delâletin kıvamı kendisiyle olan DİLİ isbat etmiştir." + R_TR},
 "tashbih": {"kind": "mursal-mufassal", "mushabbah": [1], "bihi": [2, 3], "adat": 0, "wajh": [4, 5]},
 "tokens": [
  tok("شَبَّهَ","shabbaha","verb",[M, "form-ii-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — أَدَاةُ التَّشْبِيهِ.", "«he likened» — the adat is the verb.", "«benzetti» — edat fiildir."),
  tok("الْحَالَ","hal","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُشَبَّهُ.", "«the state» — the mushabbah.", "«hâli» — müşebbeh."),
  tok("بِإِنْسَانٍ","insan","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to a human» — the bihi.", "«insana» — bih.",
      segments=[seg("بِ","bi","part"), seg("إِنْسَانٍ","insan","noun")]),
  tok("مُتَكَلِّمٍ","mutakallim","noun",[M, "naat-sifa", "ism-fail", "form-v-verbs"], "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلِ تَكَلَّمَ.", "«speaking» — a na't; ism fa'il of Form V.", "«konuşan» — na't; V. bâbın ism-i fâili."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ — يَجُرُّ وَجْهَ الشَّبَهِ.", "«in» — governs the wajh.", "«-de» — vechi cer eder."),
  tok("الدَّلَالَةِ","dalala","noun",[M, "huruf-jarr"], "مَجْرُورٌ — وَجْهُ الشَّبَهِ.", "«indicating» — the wajh.", "«delâlet» — vech.", punct="،"),
  tok("وَأَثْبَتَ","athbata","verb",[M, "atf-nasaq", "form-iv-verbs", "maful-bihi"], "مَعْطُوفٌ — فِعْلٌ مَاضٍ.", "«and affirmed» — joined.", "«ve isbat etti» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("أَثْبَتَ","athbata","verb")]),
  tok("لَهَا","li","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — لِلْحَالِ.", "«for it» — for the state.", "«ona» — hâle.",
      segments=[seg("لَ","li","part"), seg("هَا","pron-3fs","pron")]),
  tok("اللِّسَانَ","lisan","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the tongue» — the object.", "«dili» — mef'ûl."),
  tok("الَّذِي","alladhi","pron",[M, "ism-mawsul", "naat-sifa"], "اسْمٌ مَوْصُولٌ نَعْتٌ.", "«on which» — the relative as a na't.", "«… olan» — na't olarak mevsûl."),
  tok("بِهِ","bi","part",[M, "huruf-jarr", "mubtada-khabar"], "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — صِلَةٌ.", "«on it» — the khabar brought forward; the sila.", "«onunla» — öne alınmış haber; sıla.",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("قِوَامُ","qiwam","noun",[M, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the standing of» — the mubtada, held back; a mudaf.", "«kıvamı» — geriye bırakılmış mübtedâ; muzâf."),
  tok("الدَّلَالَةِ","dalala","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«indicating» — mudaf ilayh.", "«delâletin» — muzâfun ileyh.", punct=".")]})

# ----------- s8 — Zuhayr's bayt (as printed)
S.append({"id": "s8", "translation": {
 "en": "And as in Zuhayr's saying: «The heart has sobered from Salma and its folly has ceased, • and the HORSES of YOUTH and its riding-camels have been UNSADDLED».",
 "tr": "Ve Züheyr'in şu sözü gibi: «Kalp Selmâ'dan ayıldı, boş sevdası dindi, • GENÇLİĞİN ATLARI ve develeri EYERSİZ BIRAKILDI»."},
 "majaz": [mj(10, "makniyya", "mushabaha", {"en": "youth", "tr": "gençlik, sabâ"}, {"en": "a road one travels, as the pilgrimage — the bihi hidden", "tr": "hac gibi yol alınan bir yön — bih gizli"},
              istiara=ist("makniyya", minhu=[8])),
           mj(9, "takhyiliyya", "mushabaha", {"en": "the horses of", "tr": "atları"}, {"en": "the mounts of the journey, imagined for youth — or, read as the soul's powers, a tahqiqiyya", "tr": "yolculuğun binekleri, gençlik için tahayyül edilmiş — yahut nefsin kuvvetleri okunursa tahkîkiyye"},
              istiara=ist("takhyiliyya")),
           mj(11, "takhyiliyya", "mushabaha", {"en": "and its riding-camels", "tr": "ve develeri"}, {"en": "the mounts of the journey, imagined for youth", "tr": "yolculuğun binekleri, gençlik için tahayyül edilmiş"},
              istiara=ist("takhyiliyya"))],
 "tokens": [
  tok("وَكَقَوْلِ","qawl","noun",[M, "huruf-jarr", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَالْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ قَوْلِ مَجْرُورٌ مُضَافٌ.", "«and as in the saying of» — the kaf of «for instance», a wall.", "«ve … sözü gibi» — «meselâ» kâfı, duvar.",
      segments=[seg("وَ","wa","conj"), seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun")]),
  tok("زُهَيْرٍ","zuhayr","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zuhayr» — mudaf ilayh.", "«Züheyr» — muzâfun ileyh.", punct=":"),
  tok("صَحَا","saha","verb",[M, "naqis-verbs", "fail"], "فِعْلٌ مَاضٍ نَاقِصٌ وَاوِيٌّ (صَحَا يَصْحُو).", "«has sobered» — the naqis-waw mazi.", "«ayıldı» — nâkıs-vâvî mâzî."),
  tok("الْقَلْبُ","qalb","noun",[M, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the heart» — the fa'il.", "«kalp» — fâil."),
  tok("عَنْ","an","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("سَلْمَى","salma","noun",[M, "huruf-jarr", "mamnu-min-sarf", "ism-maqsur-manqus"], "مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ — عَلَمٌ مَقْصُورٌ مَمْنُوعٌ مِنَ الصَّرْفِ.", "«Salma» — a maqsur proper name, a diptote.", "«Selmâ» — maksûr alem, gayr-i munsarif."),
  tok("وَأَقْصَرَ","aqsara","verb",[M, "atf-nasaq", "form-iv-verbs", "fail"], "مَعْطُوفٌ — فِعْلٌ مَاضٍ مِنَ الرَّابِعِ: كَفَّ.", "«and has ceased» — joined; Form IV: desisted.", "«ve dindi» — matuf; IV. bâb: vazgeçti.",
      segments=[seg("وَ","wa","conj"), seg("أَقْصَرَ","aqsara","verb")]),
  tok("بَاطِلُهُ","batil","noun",[M, "fail", "idafa-definiteness", "ism-fail"], "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its folly» — the fa'il with its pronoun.", "«boş sevdası» — fâil ve zamiri.",
      segments=[seg("بَاطِلُ","batil","noun"), seg("هُ","pron-3ms","pron")], punct="•"),
  tok("وَعُرِّيَ","arra","verb",[M, "atf-nasaq", "naib-al-fail", "form-ii-verbs", "naqis-verbs"], "الْوَاوُ عَاطِفَةٌ، وَعُرِّيَ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مِنَ النَّاقِصِ عَرَّى — تَرْشِيحٌ: التَّعْرِيَةُ مِنْ لَوَازِمِ الدَّوَابِّ.",
      "«and have been unsaddled» — the passive of the naqis Form II; a TARSHIH: unsaddling belongs to mounts.",
      "«ve eyersiz bırakıldı» — nâkıs II. bâbın meçhûlü; TERŞÎH: eyer çözmek bineklere aittir.",
      segments=[seg("وَ","wa","conj"), seg("عُرِّيَ","arra","verb")]),
  tok("أَفْرَاسُ","faras","noun",[M, "naib-al-fail", "idafa-definiteness", "jam-taksir"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ — جَمْعُ فَرَسٍ؛ الِاسْتِعَارَةُ التَّخْيِيلِيَّةُ.", "«the horses of» — the deputy doer, a mudaf; plural of فَرَس. The TAKHYILIYYA.", "«atları» — nâib-i fâil, muzâf; فَرَس'in çoğulu. TAHYÎLİYYE."),
  tok("الصِّبَا","siba","noun",[M, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — الْمُشَبَّهُ الْمَذْكُورُ: اسْتِعَارَةٌ بِالْكِنَايَةِ.", "«youth» — mudaf ilayh; a maqsur. The MUSHABBAH spoken: an istiʿara BY KINAYA.", "«gençliğin» — muzâfun ileyh; maksûr. Söylenen MÜŞEBBEH: KİNÂYE YOLUYLA istiâre."),
  tok("وَرَوَاحِلُهُ","rahila","noun",[M, "atf-nasaq", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مَعْطُوفٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ رَاحِلَةٍ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ؛ تَخْيِيلِيَّةٌ ثَانِيَةٌ.", "«and its riding-camels» — joined; plural of رَاحِلَة on the muntaha pattern. A second takhyiliyya.", "«ve develeri» — matuf; رَاحِلَة'nin müntehâ kalıbında çoğulu. İkinci tahyîliyye.",
      segments=[seg("وَ","wa","conj"), seg("رَوَاحِلُ","rahila","noun"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s9 — the explanation (RESTORED)
S.append({"id": "s9", "translation": {
 "en": "He likened youth to one of the directions of travel, as the pilgrimage, and affirmed for it the horses and the riding-camels." + R_EN,
 "tr": "Gençliği, hac gibi, yol alınan yönlerden birine benzetmiş ve ona atları ve develeri isbat etmiştir." + R_TR},
 "tashbih": {"kind": "mursal-mujmal", "mushabbah": [1], "bihi": [2], "adat": 0, "wajh": []},
 "tokens": [
  tok("شَبَّهَ","shabbaha","verb",[M, "form-ii-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ — أَدَاةُ التَّشْبِيهِ.", "«he likened» — the adat is the verb.", "«benzetti» — edat fiildir."),
  tok("الصِّبَا","siba","noun",[M, "maful-bihi", "ism-maqsur-manqus"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ — الْمُشَبَّهُ.", "«youth» — the object; the mushabbah.", "«gençliği» — mef'ûl; müşebbeh."),
  tok("بِجِهَةٍ","jiha","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to a direction» — the bihi.", "«bir yöne» — bih.",
      segments=[seg("بِ","bi","part"), seg("جِهَةٍ","jiha","noun")]),
  tok("مِنْ","min","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ لِلتَّبْعِيضِ.", "«of» — partitive.", "«-den» — teb'îz."),
  tok("جِهَاتِ","jiha","noun",[M, "huruf-jarr", "idafa-definiteness", "jam-muannath-salim"], "مَجْرُورٌ، مُضَافٌ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.", "«the directions of» — a mudaf; sound feminine plural.", "«yönlerinden» — muzâf; cem-i müennes sâlim."),
  tok("السَّيْرِ","sayr","noun",[M, "idafa-definiteness", "masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«travel» — mudaf ilayh.", "«yol almanın» — muzâfun ileyh."),
  tok("كَالْحَجِّ","hajj","noun",[M, "huruf-jarr"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ، لَا تَشْبِيهَ؛ الْحَجِّ مَجْرُورٌ.", "«as the pilgrimage» — the kaf of «for instance», a wall: no likening.", "«hac gibi» — «meselâ» kâfı, duvar: benzetme değil.",
      segments=[seg("كَ","ka","part"), seg("الْحَجِّ","hajj","noun")], punct="،"),
  tok("وَأَثْبَتَ","athbata","verb",[M, "atf-nasaq", "form-iv-verbs", "maful-bihi"], "مَعْطُوفٌ — فِعْلٌ مَاضٍ.", "«and affirmed» — joined.", "«ve isbat etti» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("أَثْبَتَ","athbata","verb")]),
  tok("لَهُ","li","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — لِلصِّبَا.", "«for it» — for youth.", "«ona» — gençliğe.",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")]),
  tok("الْأَفْرَاسَ","faras","noun",[M, "maful-bihi", "jam-taksir"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the horses» — the object.", "«atları» — mef'ûl."),
  tok("وَالرَّوَاحِلَ","rahila","noun",[M, "atf-nasaq", "jam-taksir", "mamnu-min-sarf"], "مَعْطُوفٌ مَنْصُوبٌ.", "«and the riding-camels» — joined.", "«ve develeri» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("الرَّوَاحِلَ","rahila","noun")], punct=".")]})

# ----------- s10 — the other reading: tahqiqiyya (RESTORED)
S.append({"id": "s10", "translation": {
 "en": "And it may be that by the two are meant the POWERS the soul obtains — so that the istiʿara is a TAHQIQIYYA." + R_EN,
 "tr": "İkisiyle nefsin elde ettiği KUVVETLERİN kastedilmesi de muhtemeldir — o zaman istiâre TAHKÎKİYYE olur." + R_TR},
 "tokens": [
  tok("وَيَحْتَمِلُ","ihtamala","verb",[M, "form-viii-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيَحْتَمِلُ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — فَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.", "«and it may be» — Form VIII; its doer is the أَنْ clause.", "«ve muhtemeldir» — VIII. bâb; fâili أَنْ cümlesi.",
      segments=[seg("وَ","wa","conj"), seg("يَحْتَمِلُ","ihtamala","verb")]),
  tok("أَنْ","an-masdariyya","part",[M, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that».", "«-mesi»."),
  tok("يُرَادَ","arada","verb",[M, "an-masdariyya", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ مِنَ الرَّابِعِ.", "«is meant» — nasb, passive; the hollow Form IV.", "«kastedilir» — mansûb, meçhûl; ecvef IV. bâb."),
  tok("بِهِمَا","bi","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — بِالْأَفْرَاسِ وَالرَّوَاحِلِ.", "«by the two» — the horses and the camels.", "«ikisiyle» — atlar ve develer.",
      segments=[seg("بِ","bi","part"), seg("هِمَا","pron-3md","pron")]),
  tok("الْقُوَى","quwwa","noun",[M, "naib-al-fail", "jam-taksir", "ism-maqsur-manqus"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — جَمْعُ قُوَّةٍ.", "«the powers» — the deputy doer; plural of قُوَّة.", "«kuvvetler» — nâib-i fâil; قُوَّة'nin çoğulu."),
  tok("الْحَاصِلَةُ","hasil","noun",[M, "naat-sifa", "ism-fail"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلِ حَصَلَ.", "«obtained» — a na't; ism fa'il.", "«hâsıl olan» — na't; ism-i fâil."),
  tok("لِلنَّفْسِ","nafs","noun",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«by the soul».", "«nefse».",
      segments=[seg("لِ","li","part"), seg("النَّفْسِ","nafs","noun")], punct="،"),
  tok("فَتَكُونَ","kana","verb",[M, "an-masdariyya", "kana-wa-akhawatuha"], "الْفَاءُ لِلسَّبَبِيَّةِ، وَتَكُونَ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ — نَاقِصٌ.", "«so that … is» — the fa of consequence with a hidden أَنْ; kana.", "«o zaman … olur» — sebep fâsı, gizli أَنْ; kâne.",
      segments=[seg("فَ","fa","conj"), seg("تَكُونَ","kana","verb")]),
  tok("الِاسْتِعَارَةُ","istiara","noun",[M, "kana-wa-akhawatuha"], "اسْمُ تَكُونَ مَرْفُوعٌ.", "«the istiʿara» — the ism of kana.", "«istiâre» — kânenin ismi."),
  tok("تَحْقِيقِيَّةً","tahqiqiyya","noun",[M, "kana-wa-akhawatuha", "ism-mansub"], "خَبَرُ تَكُونَ مَنْصُوبٌ.", "«a tahqiqiyya» — the khabar of kana.", "«tahkîkiyye» — kânenin haberi.", punct=".")]})

# ----------- s11 — the hadith (as printed)
S.append({"id": "s11", "translation": {
 "en": "He ﷺ said: «Be in this world as if you were a stranger, or one crossing a road».",
 "tr": "O ﷺ buyurdu: «Dünyada bir garip yahut bir yolcu gibi ol»."},
 "tashbih": {"kind": "mursal-mujmal", "mushabbah": [], "bihi": [6, 7, 8, 9], "adat": 5, "wajh": []},
 "tokens": [
  tok("قَالَ","qala","verb",[M, "hollow-verbs", "fail"], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«he said» — the hollow mazi.", "«buyurdu» — ecvef mâzî."),
  SAW,
  tok("كُنْ","kana","verb",[M, "imperative-amr", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلُ أَمْرٍ نَاقِصٌ مَبْنِيٌّ عَلَى السُّكُونِ، حُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ، وَاسْمُهُ مُسْتَتِرٌ (أَنْتَ).", "«be» — the amr of kana; its middle radical dropped before the sukun; its ism hidden.", "«ol» — kânenin emri; ayn'ı iki sâkin buluşunca düşmüş; ismi gizli."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الدُّنْيَا","dunya","noun",[M, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.", "«this world» — a maqsur.", "«dünya» — maksûr."),
  tok("كَأَنَّكَ","kaanna","part",[M, "inna-wa-akhawatuha", "kana-wa-akhawatuha", "arkan-al-tashbih"], "حَرْفُ تَشْبِيهٍ وَنَصْبٍ، وَالْكَافُ اسْمُهَا — الْمُشَبَّهُ؛ وَالْجُمْلَةُ خَبَرُ كُنْ.", "«as if you» — the adat with its ism, the mushabbah; the clause is the khabar of «be».", "«sanki sen» — edat ve ismi, müşebbeh; cümle «ol»un haberi.",
      segments=[seg("كَأَنَّ","kaanna","part"), seg("كَ","pron-2ms","pron")]),
  tok("غَرِيبٌ","gharib","noun",[M, "inna-wa-akhawatuha"], "خَبَرُ كَأَنَّ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ.", "«a stranger» — the khabar of كَأَنَّ; the bihi.", "«garip» — كَأَنَّ'nin haberi; bih."),
  tok("أَوْ","aw","conj",[M, "atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("عَابِرُ","abir","noun",[M, "atf-nasaq", "ism-fail", "idafa-definiteness"], "مَعْطُوفٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ فَاعِلِ عَبَرَ.", "«one crossing» — joined; a mudaf; ism fa'il.", "«geçen» — matuf; muzâf; ism-i fâil."),
  tok("سَبِيلٍ","sabil","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a road» — mudaf ilayh.", "«yol» — muzâfun ileyh.", punct=".")]})

# ----------- s12 — Sakkaki's division (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "And with Sakkaki the istiʿara is DECLARED (musarraha) or HIDDEN (makniyya); and the declared is tahqiqiyya or takhyiliyya." + R_EN,
 "tr": "Sekkâkî'ye göre istiâre MUSARRAHA yahut MEKNİYYEdir; musarraha da tahkîkiyye yahut tahyîliyyedir." + R_TR},
 "tokens": [
  tok("وَعِنْدَ","inda","noun",[M, "maful-fih", "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَعِنْدَ ظَرْفٌ خَبَرٌ مُقَدَّمٌ، مُضَافٌ.", "«and with» — the zarf as khabar, brought forward; a mudaf.", "«ve … -ye göre» — öne alınmış haber zarfı; muzâf.",
      segments=[seg("وَ","wa","conj"), seg("عِنْدَ","inda","noun")]),
  tok("السَّكَّاكِيِّ","sakkaki","noun",[M, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — صَاحِبُ الْمِفْتَاحِ.", "«Sakkaki» — mudaf ilayh; the author of the Miftah.", "«Sekkâkî» — muzâfun ileyh; Miftâh'ın sahibi."),
  tok("الِاسْتِعَارَةُ","istiara","noun",[M, "mubtada-khabar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ.", "«the istiʿara» — the mubtada, held back.", "«istiâre» — geriye bırakılmış mübtedâ."),
  tok("مُصَرَّحَةٌ","musarraha","noun",[M, "mubtada-khabar", "ism-maful", "form-ii-verbs"], "خَبَرٌ ثَانٍ مَرْفُوعٌ (أَوْ حَالٌ) — اسْمُ مَفْعُولِ صَرَّحَ.", "«declared» — a second khabar; ism maf'ul of Form II.", "«musarraha» — ikinci haber; II. bâbın ism-i mef'ûlü."),
  tok("وَمَكْنِيَّةٌ","makniyya","noun",[M, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ.", "«or hidden» — joined.", "«yahut mekniyye» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("مَكْنِيَّةٌ","makniyya","noun")], punct="،"),
  tok("وَالْمُصَرَّحَةُ","musarraha","noun",[M, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْمُصَرَّحَةُ مُبْتَدَأٌ.", "«and the declared» — the mubtada.", "«musarraha» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُصَرَّحَةُ","musarraha","noun")]),
  tok("تَحْقِيقِيَّةٌ","tahqiqiyya","noun",[M, "mubtada-khabar", "ism-mansub"], "خَبَرٌ مَرْفُوعٌ.", "«tahqiqiyya» — the khabar.", "«tahkîkiyye» — haber."),
  tok("وَتَخْيِيلِيَّةٌ","takhyiliyya","noun",[M, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ مَرْفُوعٌ.", "«or takhyiliyya» — joined.", "«yahut tahyîliyye» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("تَخْيِيلِيَّةٌ","takhyiliyya","noun")], punct=".")]})

# ----------- s13 — the tamthil (RESTORED)
S.append({"id": "s13", "translation": {
 "en": "And he made the tamthil a kind of the tahqiqiyya; and it was answered that the tamthil REQUIRES COMPOSITION." + R_EN,
 "tr": "Temsili tahkîkiyyeden saymıştır; buna, temsilin TERKİBİ GEREKTİRDİĞİ ile cevap verilmiştir." + R_TR},
 "tokens": [
  tok("وَجَعَلَ","jaala","verb",[M, "mafulayn", "fail"], "الْوَاوُ عَاطِفَةٌ، وَجَعَلَ فِعْلٌ مَاضٍ يَنْصِبُ مَفْعُولَيْنِ، وَالْفَاعِلُ مُسْتَتِرٌ (السَّكَّاكِيُّ).", "«and he made» — a two-object verb; the doer hidden.", "«ve saydı» — iki mef'ûllü fiil; fâil gizli.",
      segments=[seg("وَ","wa","conj"), seg("جَعَلَ","jaala","verb")]),
  tok("التَّمْثِيلَ","tamthil","noun",[M, "mafulayn"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ.", "«the tamthil» — the first object.", "«temsili» — birinci mef'ûl."),
  tok("مِنَ","min","part",[M, "huruf-jarr", "mafulayn"], "حَرْفُ جَرٍّ حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ — الْجَارُّ وَالْمَجْرُورُ مَفْعُولٌ ثَانٍ.", "«of» — the jarr phrase as the second object.", "«-den» — câr-mecrûr ikinci mef'ûl."),
  tok("التَّحْقِيقِيَّةِ","tahqiqiyya","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the tahqiqiyya».", "«tahkîkiyye».", punct="،"),
  tok("وَرُدَّ","radda","verb",[M, "naib-al-fail", "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرُدَّ فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — مُضَاعَفٌ؛ نَائِبُ الْفَاعِلِ مُسْتَتِرٌ.", "«and it was answered» — the passive of the doubled رَدَّ.", "«ve cevap verildi» — muzâaf رَدَّ'nin meçhûlü.",
      segments=[seg("وَ","wa","conj"), seg("رُدَّ","radda","verb")]),
  tok("بِأَنَّ","anna","part",[M, "huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.", "«by that» — the ba over أَنَّ.", "«… ile» — أَنَّ üzerinde bâ.",
      segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part")]),
  tok("التَّمْثِيلَ","tamthil","noun",[M, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the tamthil» — the ism of أَنَّ.", "«temsil» — أَنَّ'nin ismi."),
  tok("يَسْتَلْزِمُ","istalzama","verb",[M, "inna-wa-akhawatuha", "form-x-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مِنَ الْعَاشِرِ، وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«requires» — Form X; the clause is the khabar of أَنَّ.", "«gerektirir» — X. bâb; cümle أَنَّ'nin haberi."),
  tok("التَّرْكِيبَ","tarkib","noun",[M, "maful-bihi", "masdar"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَصْدَرُ رَكَّبَ.", "«composition» — the object; the masdar of Form II.", "«terkibi» — mef'ûl; II. bâbın masdarı.", punct=".")]})

# ----------- s14 — his takhyiliyya (RESTORED)
S.append({"id": "s14", "translation": {
 "en": "And he explained the takhyiliyya as that whose meaning has NO REALITY, neither by sense nor by reason — like the word «claws» in the Hudhali's saying." + R_EN,
 "tr": "Tahyîliyyeyi, mânâsının ne hissen ne aklen bir GERÇEKLİĞİ olmayan diye açıklamıştır — Hüzelî'nin sözündeki «pençeler» lafzı gibi." + R_TR},
 "tokens": [
  tok("وَفَسَّرَ","fassara","verb",[M, "form-ii-verbs", "maful-bihi"], "الْوَاوُ عَاطِفَةٌ، وَفَسَّرَ فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«and he explained» — Form II.", "«ve açıkladı» — II. bâb.",
      segments=[seg("وَ","wa","conj"), seg("فَسَّرَ","fassara","verb")]),
  tok("التَّخْيِيلِيَّةَ","takhyiliyya","noun",[M, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the takhyiliyya» — the object.", "«tahyîliyyeyi» — mef'ûl."),
  tok("بِمَا","ma-mawsula","pron",[M, "huruf-jarr", "ism-mawsul"], "الْبَاءُ جَارَّةٌ، وَمَا مَوْصُولٌ.", "«as that which».", "«… olan diye».",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("لَا","la-nafiya-lil-jins","part",[M, "la-nafiya-lil-jins", "ism-mawsul"], "لَا النَّافِيَةُ لِلْجِنْسِ — وَالْجُمْلَةُ صِلَةٌ.", "«no» — the la that denies the genus; the sila.", "«hiç … yok» — cinsi nefyeden lâ; sıla."),
  tok("تَحَقُّقَ","tahaqquq","noun",[M, "la-nafiya-lil-jins", "masdar", "form-v-verbs"], "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ — مَصْدَرُ تَحَقَّقَ.", "«reality» — the ism of لَا, built on fatha; the masdar of Form V.", "«gerçeklik» — lânın ismi, fetha üzere mebnî; V. bâbın masdarı."),
  tok("لِمَعْنَاهُ","mana","noun",[M, "huruf-jarr", "la-nafiya-lil-jins", "idafa-definiteness", "ism-maqsur-manqus"], "الْجَارُّ وَالْمَجْرُورُ خَبَرُ لَا، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«for its meaning» — the khabar of لَا.", "«mânâsının» — lânın haberi.",
      segments=[seg("لِ","li","part"), seg("مَعْنَا","mana","noun"), seg("هُ","pron-3ms","pron")]),
  tok("حِسًّا","hiss","noun",[M, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ (أَوْ مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ).", "«by sense» — a tamyiz.", "«hissen» — temyiz."),
  tok("وَلَا","la-nafiya","part",[M, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا لِتَأْكِيدِ النَّفْيِ.", "«nor».", "«ne de».",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("عَقْلًا","aql","noun",[M, "atf-nasaq", "tamyiz"], "مَعْطُوفٌ مَنْصُوبٌ.", "«by reason» — joined.", "«aklen» — matuf.", punct="،"),
  tok("كَلَفْظِ","lafz","noun",[M, "huruf-jarr", "idafa-definiteness"], "الْكَافُ لِلتَّمْثِيلِ — جِدَارٌ؛ لَفْظِ مَجْرُورٌ مُضَافٌ.", "«like the word» — the kaf of «for instance», a wall.", "«lafzı gibi» — «meselâ» kâfı, duvar.",
      segments=[seg("كَ","ka","part"), seg("لَفْظِ","lafz","noun")]),
  tok("الْأَظْفَارِ","zufr","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«claws» — mudaf ilayh.", "«pençeler» — muzâfun ileyh."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("قَوْلِ","qawl","noun",[M, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the saying of» — a mudaf.", "«sözünde» — muzâf."),
  tok("الْهُذَلِيِّ","hudhali","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the Hudhali» — mudaf ilayh.", "«Hüzelî» — muzâfun ileyh.", punct=".")]})

# ----------- s15 — his makniyya, and the reply (RESTORED)
S.append({"id": "s15", "translation": {
 "en": "And he made the word of the mushabbah, in the makniyya, USED FOR the mushabbah bihi — the clue being the annexing of the claws; and it was answered that the word is used in WHAT IT WAS COINED FOR." + R_EN,
 "tr": "Mekniyyede müşebbehin lafzını, pençelerin izâfeti karînesiyle müşebbehün bih İÇİN KULLANILMIŞ saymıştır; buna, lafzın KONULDUĞU MÂNÂDA kullanıldığı ile cevap verilmiştir." + R_TR},
 "tokens": [
  tok("وَجَعَلَ","jaala","verb",[M, "mafulayn"], "الْوَاوُ عَاطِفَةٌ، وَجَعَلَ فِعْلٌ مَاضٍ يَنْصِبُ مَفْعُولَيْنِ.", "«and he made» — a two-object verb.", "«ve saydı» — iki mef'ûllü fiil.",
      segments=[seg("وَ","wa","conj"), seg("جَعَلَ","jaala","verb")]),
  tok("لَفْظَ","lafz","noun",[M, "mafulayn", "idafa-definiteness"], "مَفْعُولٌ أَوَّلُ مَنْصُوبٌ، مُضَافٌ.", "«the word of» — the first object, a mudaf.", "«lafzını» — birinci mef'ûl, muzâf."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the mushabbah» — mudaf ilayh.", "«müşebbehin» — muzâfun ileyh."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْمَكْنِيَّةِ","makniyya","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the makniyya».", "«mekniyye»."),
  tok("مُسْتَعْمَلًا","mustamal","noun",[M, "mafulayn", "ism-maful", "form-x-verbs"], "مَفْعُولٌ ثَانٍ مَنْصُوبٌ — اسْمُ مَفْعُولٍ.", "«used» — the second object; ism maf'ul.", "«kullanılmış» — ikinci mef'ûl; ism-i mef'ûl."),
  tok("فِي","fi","part",[M, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«for».", "«-de»."),
  tok("الْمُشَبَّهِ","mushabbah","noun",[M, "huruf-jarr"], "مَجْرُورٌ.", "«the mushabbah».", "«müşebbeh»."),
  tok("بِهِ","bi","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — تَمَامُ الِاسْمِ.", "«bihi».", "«bih».",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("بِقَرِينَةِ","qarina","noun",[M, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ، مُضَافٌ.", "«by the clue of» — a mudaf.", "«karînesiyle» — muzâf.",
      segments=[seg("بِ","bi","part"), seg("قَرِينَةِ","qarina","noun")]),
  tok("إِضَافَةِ","idafa","noun",[M, "idafa-definiteness", "masdar", "form-iv-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — مَصْدَرُ أَضَافَ.", "«the annexing of» — mudaf ilayh, itself a mudaf; the masdar of Form IV.", "«izâfetinin» — muzâfun ileyh, kendisi muzâf; IV. bâbın masdarı."),
  tok("الْأَظْفَارِ","zufr","noun",[M, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the claws» — mudaf ilayh.", "«pençelerin» — muzâfun ileyh.", punct="،"),
  tok("وَرُدَّ","radda","verb",[M, "naib-al-fail", "doubled-verbs"], "الْوَاوُ عَاطِفَةٌ، وَرُدَّ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and it was answered» — the passive.", "«ve cevap verildi» — meçhûl.",
      segments=[seg("وَ","wa","conj"), seg("رُدَّ","radda","verb")]),
  tok("بِأَنَّ","anna","part",[M, "huruf-jarr", "inna-wa-akhawatuha"], "الْبَاءُ جَارَّةٌ، وَأَنَّ نَاصِبَةٌ.", "«by that».", "«… ile».",
      segments=[seg("بِ","bi","part"), seg("أَنَّ","anna","part")]),
  tok("اللَّفْظَ","lafz","noun",[M, "inna-wa-akhawatuha"], "اسْمُ أَنَّ مَنْصُوبٌ.", "«the word» — the ism of أَنَّ.", "«lafız» — أَنَّ'nin ismi."),
  tok("مُسْتَعْمَلٌ","mustamal","noun",[M, "inna-wa-akhawatuha", "ism-maful"], "خَبَرُ أَنَّ مَرْفُوعٌ.", "«is used» — the khabar of أَنَّ.", "«kullanılmıştır» — أَنَّ'nin haberi."),
  tok("فِيمَا","ma-mawsula","pron",[M, "huruf-jarr", "ism-mawsul"], "فِي جَارَّةٌ، وَمَا مَوْصُولٌ.", "«in what».", "«… şeyde».",
      segments=[seg("فِي","fi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("وُضِعَ","wadaa","verb",[M, "naib-al-fail", "ism-mawsul", "mithal-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — صِلَةٌ؛ مِثَالٌ وَاوِيٌّ.", "«it was coined» — the passive; the sila; a mithal-waw.", "«konulmuş» — meçhûl; sıla; misâl-i vâvî."),
  tok("لَهُ","li","part",[M, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«for».", "«… için».",
      segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")], punct=".")]})

# ----------- s16 — the beauty of the istiʿara (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "And the BEAUTY of the tahqiqiyya and the tamthiliyya lies in observing the aspects of a good likening, and in that no SCENT of the likening be smelt from it in the wording." + R_EN,
 "tr": "Tahkîkiyye ile temsîliyyenin GÜZELLİĞİ, güzel benzetmenin cihetlerine riayet etmekte ve lafızda ondan benzetme KOKUSU alınmamasındadır." + R_TR},
 "tokens": [
  tok("وَحُسْنُ","husn","noun",[H, "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَحُسْنُ مُبْتَدَأٌ مُضَافٌ.", "«and the beauty of» — the mubtada, a mudaf.", "«güzelliği» — mübtedâ, muzâf.",
      segments=[seg("وَ","wa","conj"), seg("حُسْنُ","husn","noun")]),
  tok("التَّحْقِيقِيَّةِ","tahqiqiyya","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the tahqiqiyya» — mudaf ilayh.", "«tahkîkiyyenin» — muzâfun ileyh."),
  tok("وَالتَّمْثِيلِيَّةِ","tamthiliyya","noun",[H, "atf-nasaq", "ism-mansub"], "مَعْطُوفٌ مَجْرُورٌ.", "«and the tamthiliyya» — joined.", "«ve temsîliyyenin» — matuf.",
      segments=[seg("وَ","wa","conj"), seg("التَّمْثِيلِيَّةِ","tamthiliyya","noun")]),
  tok("بِرِعَايَةِ","riaya","noun",[H, "huruf-jarr", "mubtada-khabar", "idafa-definiteness", "masdar"], "الْجَارُّ وَالْمَجْرُورُ خَبَرٌ؛ رِعَايَةِ مُضَافٌ — مَصْدَرُ رَاعَى.", "«in observing» — the khabar; a mudaf; the masdar of Form III.", "«riayet etmekte» — haber; muzâf; III. bâbın masdarı.",
      segments=[seg("بِ","bi","part"), seg("رِعَايَةِ","riaya","noun")]),
  tok("جِهَاتِ","jiha","noun",[H, "idafa-definiteness", "jam-muannath-salim"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the aspects of» — mudaf ilayh, itself a mudaf.", "«cihetlerine» — muzâfun ileyh, kendisi muzâf."),
  tok("حُسْنِ","husn","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the goodness of» — mudaf ilayh, a mudaf.", "«güzelliğinin» — muzâfun ileyh, muzâf."),
  tok("التَّشْبِيهِ","tashbih","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likening» — mudaf ilayh.", "«benzetmenin» — muzâfun ileyh.", punct="،"),
  tok("وَأَنْ","an-masdariyya","part",[H, "atf-nasaq", "an-masdariyya"], "الْوَاوُ عَاطِفَةٌ، وَأَنْ مَصْدَرِيَّةٌ — الْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى رِعَايَةِ.", "«and that» — the أَنْ clause joined to «observing».", "«ve … -maması» — أَنْ cümlesi «riayet»e matuf.",
      segments=[seg("وَ","wa","conj"), seg("أَنْ","an-masdariyya","part")]),
  tok("لَا","la-nafiya","part",[H, "an-masdariyya"], "حَرْفُ نَفْيٍ.", "«not».", "«-ma»."),
  tok("يُشَمَّ","shamma","verb",[H, "an-masdariyya", "naib-al-fail", "doubled-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِأَنْ، مَبْنِيٌّ لِلْمَجْهُولِ — مُضَاعَفٌ.", "«be smelt» — nasb by أَنْ; the passive of the doubled شَمَّ.", "«koklanması» — أَنْ ile mansûb; muzâaf شَمَّ'nin meçhûlü."),
  tok("مِنْهَا","min","part",[H, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — مِنَ الِاسْتِعَارَةِ.", "«from it» — from the istiʿara.", "«ondan» — istiâreden.",
      segments=[seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("رَائِحَةُ","raiha","noun",[H, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ — وَفِيهِ اسْتِعَارَةٌ بِالْكِنَايَةِ: التَّشْبِيهُ شُبِّهَ بِذِي رَائِحَةٍ.", "«the scent of» — the deputy doer, a mudaf; itself an istiʿara by kinaya: the likening likened to a scented thing.", "«kokusu» — nâib-i fâil, muzâf; kendisi kinâye yoluyla istiâre: benzetme kokulu bir şeye benzetilmiş."),
  tok("التَّشْبِيهِ","tashbih","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likening» — mudaf ilayh.", "«benzetmenin» — muzâfun ileyh."),
  tok("لَفْظًا","lafz","noun",[H, "tamyiz"], "تَمْيِيزٌ مَنْصُوبٌ — مِنْ جِهَةِ اللَّفْظِ.", "«in wording» — a tamyiz.", "«lafız bakımından» — temyiz.", punct=".")]})

# ----------- s17 — the plain jamiʿ (RESTORED)
S.append({"id": "s17", "translation": {
 "en": "And in the asliyya the PLAINNESS of the jamiʿ is required, lest it become like a RIDDLE: were one to say «I saw a lion» and mean a man of foul breath, it would not be good." + R_EN,
 "tr": "Asliyyede, BİLMECE gibi olmasın diye câmiin AÇIK olması şart koşulur: «bir arslan gördüm» deyip ağzı kokan bir adam kastedilse güzel olmazdı." + R_TR},
 "tashbih": {"kind": "mursal-mujmal", "mushabbah": [], "bihi": [7], "adat": 7, "wajh": []},
 "majaz": [mj(11, "istiara", "mushabaha", {"en": "a lion", "tr": "bir arslan"}, {"en": "a man of FOUL BREATH — the jamiʿ (lions are foul-breathed) is hidden, so the istiʿara is a riddle: the book's own example of what NOT to do", "tr": "AĞZI KOKAN bir adam — câmi (arslanın ağzı kokar) gizli, istiâre bilmeceye döner: kitabın yapılmaması gerekene örneği"},
             istiara=ist("asliyya", hissi=["hissi", "hissi", "hissi"], mulaim="mutlaqa"))],
 "tokens": [
  tok("وَيُشْتَرَطُ","ishtarata","verb",[H, "naib-al-fail", "form-viii-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَيُشْتَرَطُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ.", "«and it is required» — the passive of Form VIII.", "«ve şart koşulur» — VIII. bâbın meçhûlü.",
      segments=[seg("وَ","wa","conj"), seg("يُشْتَرَطُ","ishtarata","verb")]),
  tok("فِي","fi","part",[H, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْأَصْلِيَّةِ","asliyya","noun",[H, "huruf-jarr"], "مَجْرُورٌ.", "«the asliyya».", "«asliyye»."),
  tok("ظُهُورُ","zuhur","noun",[H, "naib-al-fail", "idafa-definiteness", "masdar"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«the plainness of» — the deputy doer, a mudaf.", "«açıklığı» — nâib-i fâil, muzâf."),
  tok("الْجَامِعِ","jami-link","noun",[H, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the jamiʿ» — mudaf ilayh.", "«câmiin» — muzâfun ileyh."),
  tok("لِئَلَّا","li","part",[H, "lam-taleel", "an-masdariyya"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنْ نَاصِبَةٌ، وَلَا نَافِيَةٌ — كُتِبَتْ مُتَّصِلَةً.", "«lest» — the lam of cause, أَنْ and لَا written as one.", "«… olmasın diye» — ta'lil lâmı, أَنْ ve لَا bitişik.",
      segments=[seg("لِ","li","part"), seg("أَنْ","an-masdariyya","part"), seg("لَا","la-nafiya","part")]),
  tok("تَصِيرَ","sara","verb",[H, "an-masdariyya", "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ — مِنْ أَخَوَاتِ كَانَ، وَاسْمُهُ مُسْتَتِرٌ (هِيَ): الْمُشَبَّهُ.", "«it become» — nasb; a sister of kana, its ism hidden: the mushabbah.", "«olmasın» — mansûb; kânenin kardeşi, ismi gizli: müşebbeh."),
  tok("كَاللُّغْزِ","lughz","noun",[H, "huruf-jarr", "kana-wa-akhawatuha", "arkan-al-tashbih"], "جَارٌّ وَمَجْرُورٌ — الْكَافُ لِلتَّشْبِيهِ، أَدَاةٌ حَقِيقِيَّةٌ هُنَا؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ تَصِيرَ.", "«like a riddle» — a REAL likening kaf here; the khabar of «become».", "«bilmece gibi» — burada GERÇEK teşbih kâfı; «olmasın»ın haberi.",
      segments=[seg("كَ","ka","part"), seg("اللُّغْزِ","lughz","noun")], punct="،"),
  tok("فَلَوْ","law","part",[H, "atf-nasaq"], "الْفَاءُ لِلتَّفْرِيعِ، وَلَوْ حَرْفُ شَرْطٍ غَيْرُ جَازِمٍ.", "«so were» — law, the shart that does not jazm.", "«öyle ki … -se» — cezm etmeyen şart harfi lev.",
      segments=[seg("فَ","fa","conj"), seg("لَوْ","law","part")]),
  tok("قِيلَ","qala","verb",[H, "naib-al-fail", "hollow-verbs"], "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ: قُلْتُ، قِيلَ.", "«it were said» — the passive of the hollow قَالَ.", "«dense» — ecvef قَالَ'nin meçhûlü."),
  tok("رَأَيْتُ","raa","verb",[H, "naib-al-fail", "maful-bihi", "naqis-verbs"], "الْجُمْلَةُ الْمَحْكِيَّةُ نَائِبُ فَاعِلٍ.", "«‹I saw›» — the quoted clause is the deputy doer.", "«‹gördüm›» — hikâye edilen cümle nâib-i fâil.",
      segments=[seg("رَأَيْ","raa","verb"), seg("تُ","pron-1s","pron")]),
  tok("أَسَدًا","asad","noun",[H, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a lion» — the object.", "«bir arslan» — mef'ûl."),
  tok("وَأُرِيدَ","arada","verb",[H, "atf-nasaq", "naib-al-fail", "form-iv-verbs", "hollow-verbs"], "مَعْطُوفٌ عَلَى قِيلَ — مَبْنِيٌّ لِلْمَجْهُولِ.", "«and were meant» — joined to «it were said»; passive.", "«ve kastedilse» — «dense»ye matuf; meçhûl.",
      segments=[seg("وَ","wa","conj"), seg("أُرِيدَ","arada","verb")]),
  tok("رَجُلٌ","rajul","noun",[H, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«a man» — the deputy doer.", "«bir adam» — nâib-i fâil."),
  tok("أَبْخَرُ","abkhar","noun",[H, "naat-sifa", "mamnu-min-sarf"], "نَعْتٌ مَرْفُوعٌ — أَفْعَلُ الْوَصْفِ، مَمْنُوعٌ مِنَ الصَّرْفِ.", "«of foul breath» — a na't; the أَفْعَل of quality, a diptote.", "«ağzı kokan» — na't; vasıf أَفْعَل'i, gayr-i munsarif."),
  tok("لَمْ","lam-jazima","part",[H, "lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ — جَوَابُ لَوْ.", "«not» — the jawab of law.", "«-mazdı» — levin cevabı."),
  tok("يَحْسُنْ","hasuna","verb",[H, "lam-jazim"], "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ.", "«be good» — jazm by لَمْ.", "«güzel olmazdı» — لَمْ ile meczûm.", punct=".")]})

# ----------- s18 — the hundred camels (RESTORED frame + the received saying)
S.append({"id": "s18", "translation": {
 "en": "And as in your saying: «I saw a hundred camels, in which you find no one fit to ride» — while you mean PEOPLE." + R_EN,
 "tr": "Ve şu sözün gibi: «İçlerinde binilecek bir tane bulamadığın yüz deve gördüm» — kastın ise İNSANLARdır." + R_TR},
 "majaz": mj(2, "murakkab", "tamthil", {"en": "a hundred camels with not one fit to ride — the picture of a herd", "tr": "içinde bir tane binilecek olmayan yüz deve — sürünün resmi"}, {"en": "people: many, and hardly one of worth — the whole picture lent to their state", "tr": "insanlar: çok, ama işe yarar bir tanesi zor — resmin bütünü hâllerine ödünç"},
             istiara=ist("murakkab")),
 "tokens": [
  kawa("وَكَقَوْلِكَ", "pron-2ms", K),
  tok("رَأَيْتُ","raa","verb",[K, "maful-bihi", "naqis-verbs"], "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ.", "«I saw».", "«gördüm».",
      segments=[seg("رَأَيْ","raa","verb"), seg("تُ","pron-1s","pron")]),
  tok("إِبِلًا","ibil","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْمُ جَمْعٍ؛ رَأْسُ الصُّورَةِ الْمُسْتَعَارَةِ.", "«camels» — the object; a collective. The head of the lent picture.", "«develer» — mef'ûl; cins ismi. Ödünç resmin başı."),
  tok("مِائَةً","mia","noun",[K, "naat-sifa"], "نَعْتٌ مَنْصُوبٌ (أَوْ بَدَلٌ) — الْعَدَدُ بَعْدَ الْمَعْدُودِ.", "«a hundred» — a na't (or badal); the number after its noun.", "«yüz» — na't (yahut bedel); sayı ma'dûdundan sonra."),
  tok("لَا","la-nafiya","part",[K, "jumla-sifa"], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.", "«not» — the clause a second na't.", "«-ma» — cümle ikinci na't."),
  tok("تَجِدُ","wajada","verb",[K, "jumla-sifa", "mithal-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ وَاوِيٌّ، حُذِفَتْ وَاوُهُ.", "«you find» — the mithal-waw, its waw dropped.", "«bulursun» — misâl-i vâvî, vâvı düşmüş."),
  tok("فِيهَا","fi","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«in them».", "«içlerinde».",
      segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("رَاحِلَةً","rahila","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — النَّاقَةُ الصَّالِحَةُ لِلرُّكُوبِ.", "«a riding-camel» — the object: the one fit to be ridden.", "«binilecek deve» — mef'ûl: binmeye elverişli olan.", punct="،"),
  tok("وَأَنْتَ","anta","pron",[K, "hal", "mubtada-khabar"], "الْوَاوُ لِلْحَالِ، وَأَنْتَ مُبْتَدَأٌ.", "«while you» — the waw of the hal; the mubtada.", "«sen ise» — hâl vâvı; mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("أَنْتَ","anta","pron")]),
  tok("تُرِيدُ","arada","verb",[K, "mubtada-khabar", "form-iv-verbs", "hollow-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ، وَالْجُمْلَةُ خَبَرٌ.", "«mean» — the clause is the khabar.", "«kastediyorsun» — cümle haber."),
  tok("النَّاسَ","nas","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ — الْمُرَادُ.", "«people» — the object; the thing meant.", "«insanları» — mef'ûl; kastedilen.", punct=".")]})

# ----------- s19 — the hadith it is drawn from (as printed)
S.append({"id": "s19", "translation": {
 "en": "And it is drawn from his ﷺ saying: «People are like a hundred camels: you find among them hardly one fit to ride».",
 "tr": "Bu, onun ﷺ şu sözünden alınmıştır: «İnsanlar yüz deve gibidir: içlerinde binilecek bir tane bulamazsın»."},
 "tashbih": {"kind": "mursal-mujmal", "mushabbah": [5], "bihi": [6, 7, 8, 9, 10, 11], "adat": 6, "wajh": []},
 "tokens": [
  tok("وَهُوَ","huwa","pron",[K, "mubtada-khabar"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("مُقْتَبَسٌ","muqtabas","noun",[K, "mubtada-khabar", "ism-maful", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولِ اقْتَبَسَ.", "«drawn» — the khabar; ism maf'ul of Form VIII.", "«alınmış» — haber; VIII. bâbın ism-i mef'ûlü."),
  tok("مِنْ","min","part",[K, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("قَوْلِهِ","qawl","noun",[K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his saying».", "«sözünden».",
      segments=[seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")]),
  SAW,
  tok("النَّاسُ","nas","noun",[K, "mubtada-khabar", "arkan-al-tashbih"], "مُبْتَدَأٌ مَرْفُوعٌ — الْمُشَبَّهُ.", "«people» — the mubtada; the mushabbah.", "«insanlar» — mübtedâ; müşebbeh."),
  tok("كَإِبِلٍ","ibil","noun",[K, "huruf-jarr", "mubtada-khabar", "arkan-al-tashbih"], "الْكَافُ لِلتَّشْبِيهِ — أَدَاةٌ؛ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ: الْمُشَبَّهُ بِهِ.", "«like camels» — the likening kaf; the khabar: the bihi.", "«develer gibi» — teşbih kâfı; haber: bih.",
      segments=[seg("كَ","ka","part"), seg("إِبِلٍ","ibil","noun")]),
  tok("مِائَةٍ","mia","noun",[K, "naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«a hundred» — a na't.", "«yüz» — na't."),
  tok("لَا","la-nafiya","part",[K, "jumla-sifa"], "حَرْفُ نَفْيٍ — وَالْجُمْلَةُ نَعْتٌ.", "«not» — the clause a na't.", "«-ma» — cümle na't."),
  tok("تَجِدُ","wajada","verb",[K, "jumla-sifa", "mithal-verbs"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ.", "«you find».", "«bulursun»."),
  tok("فِيهَا","fi","part",[K, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ.", "«among them».", "«içlerinde».",
      segments=[seg("فِي","fi","part"), seg("هَا","pron-3fs","pron")]),
  tok("رَاحِلَةً","rahila","noun",[K, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«one fit to ride» — the object.", "«binilecek bir tane» — mef'ûl.", punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "admara": g("أَضْمَرَ", "ض م ر", "verb", "to hide in the mind, keep unspoken (Form IV)", "içinde gizlemek, söylememek (IV. bâb)", 4, form="IV"),
 "sarraha": g("صَرَّحَ", "ص ر ح", "verb", "to declare openly (Form II)", "açıkça söylemek (II. bâb)", 4, form="II"),
 "athbata": g("أَثْبَتَ", "ث ب ت", "verb", "to affirm, establish (Form IV)", "isbat etmek (IV. bâb)", 3, form="IV"),
 "ithbat": g("إِثْبَات", "ث ب ت", "noun", "affirming (masdar of أَثْبَتَ)", "isbat (أَثْبَتَ'nin masdarı)", 3),
 "mukhtass": g("مُخْتَصّ", "خ ص ص", "noun", "proper to, peculiar to (ism faʿil of اِخْتَصَّ)", "has, mahsus (اِخْتَصَّ'nin ism-i fâili)", 5),
 "makni": g("مَكْنِيّ", "ك ن ي", "noun", "hinted at, kept hidden (ism mafʿul of كَنَى)", "kinâye edilen, gizli tutulan (كَنَى'nın ism-i mef'ûlü)", 6),
 "makniyya": g("مَكْنِيَّة", "ك ن ي", "noun", "makniyya — the istiʿara with the bihi hidden and only the mushabbah spoken", "mekniyye — bihi gizli, yalnız müşebbehi söylenen istiâre", 6),
 "takhyiliyya": g("تَخْيِيلِيَّة", "خ ي ل", "noun", "takhyiliyya — the affirming, for the mushabbah, of a thing proper to the hidden bihi", "tahyîliyye — gizli bihe has bir şeyin müşebbeh için isbatı", 6),
 "musarraha": g("مُصَرَّحَة", "ص ر ح", "noun", "musarraha — Sakkaki's declared istiʿara, the bihi's word spoken", "musarraha — Sekkâkî'nin açık istiâresi, bihin lafzı söylenmiş", 6),
 "tahqiqiyya": find_gloss("tahqiqiyya") if _has_gloss("tahqiqiyya") else g("تَحْقِيقِيَّة", "ح ق ق", "noun", "tahqiqiyya — the istiʿara whose meaning is realised by sense or by reason", "tahkîkiyye — mânâsı hissen yahut aklen gerçekleşen istiâre", 6),
 "tamthiliyya": g("تَمْثِيلِيَّة", "م ث ل", "noun", "tamthiliyya — the compound istiʿara of a picture", "temsîliyye — bir resmin mürekkeb istiâresi", 6),
 "hudhali": g("الْهُذَلِيّ", "ه ذ ل", "noun", "the Hudhali — Abu Dhuʾayb, poet of Hudhayl", "Hüzelî — Ebû Züeyb, Hüzeyl kabilesinin şairi", 6),
 "maniyya": g("مَنِيَّة", "م ن ي", "noun", "death, the appointed end", "ölüm, ecel", 4, plural="مَنَايَا"),
 "anshaba": g("أَنْشَبَ", "ن ش ب", "verb", "to fasten, sink in (claws) (Form IV)", "(pençe) geçirmek, saplamak (IV. bâb)", 5, form="IV"),
 "alfa": g("أَلْفَى", "ل ف و", "verb", "to find (a thing so) (Form IV, naqis; two objects)", "bulmak (IV. bâb, nâkıs; iki mef'ûl)", 5, form="IV"),
 "tamima": g("تَمِيمَة", "ت م م", "noun", "amulet", "muska, nazarlık", 5, plural="تَمَائِم"),
 "sabu": g("سَبُع", "س ب ع", "noun", "beast of prey", "yırtıcı hayvan", 4, plural="سِبَاع"),
 "ightiyal": g("اِغْتِيَال", "غ و ل", "noun", "snatching away, killing unawares (masdar of اِغْتَالَ)", "ansızın kapıp götürme, öldürme (اِغْتَالَ'nin masdarı)", 6),
 "kamal": g("كَمَال", "ك م ل", "noun", "completeness, perfection", "kemâl", 3),
 "iftiras": g("اِفْتِرَاس", "ف ر س", "noun", "preying, tearing prey (masdar of اِفْتَرَسَ)", "parçalama, avlama (اِفْتَرَسَ'nin masdarı)", 5),
 "shukr": g("شُكْر", "ش ك ر", "noun", "thanks", "şükür", 2),
 "birr": find_gloss("birr"),
 "mufsih": g("مُفْصِح", "ف ص ح", "noun", "speaking clearly, eloquent (ism faʿil of أَفْصَحَ)", "açıkça söyleyen (أَفْصَحَ'nin ism-i fâili)", 5),
 "lisan": find_gloss("lisan") if _has_gloss("lisan") else g("لِسَان", "ل س ن", "noun", "tongue", "dil", 2, plural="أَلْسِنَة"),
 "shikaya": g("شِكَايَة", "ش ك و", "noun", "complaint", "şikâyet", 3),
 "antaq": g("أَنْطَقُ", "ن ط ق", "noun", "more eloquent, more speaking (ism tafdil)", "daha konuşkan, daha beliğ (ism-i tafdîl)", 5),
 "insan": find_gloss("insan") if _has_gloss("insan") else g("إِنْسَان", "أ ن س", "noun", "human being", "insan", 1, plural="نَاس"),
 "mutakallim": find_gloss("mutakallim") if _has_gloss("mutakallim") else g("مُتَكَلِّم", "ك ل م", "noun", "speaker (ism faʿil of تَكَلَّمَ)", "konuşan (تَكَلَّمَ'nin ism-i fâili)", 3),
 "qiwam": g("قِوَام", "ق و م", "noun", "what a thing stands on, its support", "kıvam, dayanak", 5),
 "saha": g("صَحَا", "ص ح و", "verb", "to sober up, come to (naqis-waw: صَحَا يَصْحُو)", "ayılmak, kendine gelmek (nâkıs-vâvî: صَحَا يَصْحُو)", 5, form="I"),
 "salma": g("سَلْمَى", None, "noun", "Salma (a woman's name)", "Selmâ (kadın adı)", 4),
 "aqsara": g("أَقْصَرَ", "ق ص ر", "verb", "to cease, desist (Form IV)", "vazgeçmek, dinmek (IV. bâb)", 5, form="IV"),
 "batil": find_gloss("batil") if _has_gloss("batil") else g("بَاطِل", "ب ط ل", "noun", "vain thing, folly; falsehood", "bâtıl, boş şey", 3),
 "arra": g("عَرَّى", "ع ر ي", "verb", "to strip, unsaddle (Form II, naqis)", "soymak, eyerini almak (II. bâb, nâkıs)", 5, form="II"),
 "siba": g("صِبًا (الصِّبَا)", "ص ب و", "noun", "youth; youthful passion", "gençlik; gençlik sevdası, sabâ", 5),
 "rahila": g("رَاحِلَة", "ر ح ل", "noun", "riding-camel, a beast fit to ride", "binek devesi, binilecek hayvan", 5, plural="رَوَاحِل"),
 "jiha": find_gloss("jiha"),
 "sayr": g("سَيْر", "س ي ر", "noun", "travel, journeying (masdar of سَارَ)", "yol alma, seyir (سَارَ'nin masdarı)", 3),
 "hajj": g("حَجّ", "ح ج ج", "noun", "the pilgrimage", "hac", 2),
 "ihtamala": find_gloss("ihtamala") if _has_gloss("ihtamala") else g("اِحْتَمَلَ", "ح م ل", "verb", "to admit of, be possible; to bear (Form VIII)", "muhtemel olmak; taşımak (VIII. bâb)", 4, form="VIII"),
 "arada": find_gloss("arada") if _has_gloss("arada") else g("أَرَادَ", "ر و د", "verb", "to want, mean (Form IV, hollow)", "istemek, kastetmek (IV. bâb, ecvef)", 2, form="IV"),
 "quwwa": find_gloss("quwwa") if _has_gloss("quwwa") else g("قُوَّة", "ق و ي", "noun", "power, faculty", "kuvvet", 2, plural="قُوًى"),
 "hasil": g("حَاصِل", "ح ص ل", "noun", "obtained, resulting (ism faʿil of حَصَلَ)", "hâsıl olan (حَصَلَ'nin ism-i fâili)", 4),
 "kaanna": find_gloss("kaanna") if _has_gloss("kaanna") else g("كَأَنَّ", None, "part", "as if — the particle of likening among inna's sisters", "sanki — innenin kardeşlerinden teşbih harfi", 2),
 "gharib": find_gloss("gharib") if _has_gloss("gharib") else g("غَرِيب", "غ ر ب", "noun", "stranger; strange, rare", "garip, yabancı; nadir", 3, plural="غُرَبَاء"),
 "abir": g("عَابِر", "ع ب ر", "noun", "one crossing, passing (ism faʿil of عَبَرَ)", "geçen, yolcu (عَبَرَ'nin ism-i fâili)", 4),
 "sabil": find_gloss("sabil") if _has_gloss("sabil") else g("سَبِيل", "س ب ل", "noun", "road, way", "yol", 2, plural="سُبُل"),
 "sakkaki": g("السَّكَّاكِيّ", None, "noun", "al-Sakkaki (d. 626/1229), author of the Miftah al-ʿUlum", "Sekkâkî (ö. 626/1229), Miftâhu'l-ulûm'un müellifi", 6),
 "jaala": find_gloss("jaala") if _has_gloss("jaala") else g("جَعَلَ", "ج ع ل", "verb", "to make (a thing so), reckon as (two objects)", "kılmak, saymak (iki mef'ûl)", 2, form="I"),
 "radda": g("رَدَّ", "ر د د", "verb", "to answer, refute; to return (doubled: رَدَّ يَرُدُّ)", "cevap vermek, reddetmek; geri çevirmek (muzâaf: رَدَّ يَرُدُّ)", 3, form="I"),
 "istalzama": g("اِسْتَلْزَمَ", "ل ز م", "verb", "to require, entail (Form X)", "gerektirmek (X. bâb)", 5, form="X"),
 "tarkib": g("تَرْكِيب", "ر ك ب", "noun", "composition, compounding (masdar of رَكَّبَ)", "terkip (رَكَّبَ'nin masdarı)", 4),
 "fassara": g("فَسَّرَ", "ف س ر", "verb", "to explain, interpret (Form II)", "tefsir etmek, açıklamak (II. bâb)", 3, form="II"),
 "tahaqquq": g("تَحَقُّق", "ح ق ق", "noun", "being real, realisation (masdar of تَحَقَّقَ)", "gerçekleşme, tahakkuk (تَحَقَّقَ'nin masdarı)", 5),
 "hiss": find_gloss("hiss") if _has_gloss("hiss") else g("حِسّ", "ح س س", "noun", "sense, sensation", "his, duyu", 3),
 "aql": find_gloss("aql") if _has_gloss("aql") else g("عَقْل", "ع ق ل", "noun", "reason, intellect", "akıl", 2),
 "idafa": g("إِضَافَة", "ض ي ف", "noun", "annexing, the idafa (masdar of أَضَافَ)", "izâfet (أَضَافَ'nin masdarı)", 3),
 "wadaa": find_gloss("wadaa") if _has_gloss("wadaa") else g("وَضَعَ", "و ض ع", "verb", "to put, coin (a word) (mithal-waw)", "koymak, (kelime) vaz' etmek (misâl-i vâvî)", 3, form="I"),
 "husn": find_gloss("husn") if _has_gloss("husn") else g("حُسْن", "ح س ن", "noun", "beauty, goodness", "güzellik, hüsün", 2),
 "riaya": g("رِعَايَة", "ر ع ي", "noun", "observing, heeding (masdar of رَاعَى)", "riayet, gözetme (رَاعَى'nın masdarı)", 4),
 "shamma": g("شَمَّ", "ش م م", "verb", "to smell (doubled: شَمَّ يَشُمُّ)", "koklamak (muzâaf: شَمَّ يَشُمُّ)", 4, form="I"),
 "raiha": g("رَائِحَة", "ر و ح", "noun", "scent, smell", "koku, râyiha", 3, plural="رَوَائِح"),
 "ishtarata": find_gloss("ishtarata"),
 "zuhur": find_gloss("zuhur") if _has_gloss("zuhur") else g("ظُهُور", "ظ ه ر", "noun", "plainness, appearing (masdar of ظَهَرَ)", "açıklık, zuhur (ظَهَرَ'nin masdarı)", 3),
 "lughz": g("لُغْز", "ل غ ز", "noun", "riddle", "bilmece, lugaz", 5, plural="أَلْغَاز"),
 "law": find_gloss("law") if _has_gloss("law") else g("لَوْ", None, "part", "if, were it that — the shart of the impossible", "eğer, -se (imkânsızın şartı)", 2),
 "sara": find_gloss("sara"),
 "abkhar": g("أَبْخَرُ", "ب خ ر", "noun", "of foul breath (أَفْعَل of quality)", "ağzı kokan (vasıf أَفْعَل'i)", 6),
 "hasuna": find_gloss("hasuna") if _has_gloss("hasuna") else g("حَسُنَ", "ح س ن", "verb", "to be good, fine (حَسُنَ يَحْسُنُ)", "güzel olmak (حَسُنَ يَحْسُنُ)", 3, form="I"),
 "ibil": g("إِبِل", "أ ب ل", "noun", "camels (a collective)", "develer (cins ismi)", 3),
 "mia": g("مِائَة", "م أ ي", "noun", "a hundred", "yüz", 2),
 "wajada": find_gloss("wajada"),
 "anta": find_gloss("anta") if _has_gloss("anta") else g("أَنْتَ", None, "pron", "you (masc. sing.)", "sen", 1),
 "muqtabas": g("مُقْتَبَس", "ق ب س", "noun", "drawn, borrowed (ism mafʿul of اِقْتَبَسَ)", "iktibas edilmiş, alınmış (اِقْتَبَسَ'nin ism-i mef'ûlü)", 5),
 "nas": find_gloss("nas") if _has_gloss("nas") else g("نَاس", "ن و س", "noun", "people", "insanlar", 1),
 "asliyya": find_gloss("asliyya"), "faras": find_gloss("faras"), "jami-link": find_gloss("jami-link"), "nataqa": find_gloss("nataqa"),
 "pron-3md": find_gloss("pron-3md"), "zuhayr": find_gloss("zuhayr"), "salla-allahu": find_gloss("salla-allahu"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/54.json").write_text(
    json.dumps({"chapter": 54, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 54 for c in man["chapters"]):
    man["chapters"].append({"n": 54, "title": TITLE54})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.54.0"
ADD_EN = (" Chapter 54 (lines ~3740-3900, sahifa 129-133) carries the istiʿara by kinaya and the takhyiliyya, Sakkaki's "
          "division with the two replies, and the beauty of the istiʿara: the bayt of Abu Dhuʾayb al-Hudhali (s4), the "
          "bayt of the tongue of the state (s6), Zuhayr's bayt (s8), the hadith كُنْ فِي الدُّنْيَا كَأَنَّكَ غَرِيبٌ (s11) "
          "and the hadith of the hundred camels (s19) are Arabic as the source prints it, inside restored frames. s1-s3, "
          "s5, s7, s9-s10, s12-s18 and the frames of the examples are RESTORATIONS, not quotations: the source carries "
          "those steps only in Ottoman-Turkish paraphrase, and the Arabic restores the matn's wording in the musannif's "
          "register; each is marked «restored» in its translation. Every makniyya carries two authored frames — the "
          "`makniyya` on the spoken mushabbah, with the tarshih words by index, and the `takhyiliyya` on the attributed "
          "thing; the musannif's own شَبَّهَ … بِـ… explanations carry tashbih frames; s18 is a `murakkab` frame.")
ADD_TR = (" Elli dördüncü bâb (satır ~3740-3900, sahife 129-133) kinâye yoluyla istiâre ile tahyîliyyeyi, Sekkâkî'nin "
          "taksimini ve iki cevabı, ve istiârenin güzelliğini taşır: Ebû Züeyb el-Hüzelî'nin beyti (s4), hâlin dili beyti "
          "(s6), Züheyr'in beyti (s8), كُنْ فِي الدُّنْيَا كَأَنَّكَ غَرِيبٌ hadisi (s11) ve yüz deve hadisi (s19), geri "
          "yazılmış çerçeveler içinde kaynağın bastığı Arapçadır. s1-s3, s5, s7, s9-s10, s12-s18 ile örneklerin "
          "çerçeveleri ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, "
          "matnın ifadesini musannifin üslûbunda geri yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. "
          "Her mekniyye iki müellif çerçevesi taşır — söylenen müşebbeh üzerinde terşîh kelimeleri indeksli `makniyya` "
          "ve isbat edilen şey üzerinde `takhyiliyya`; musannifin kendi شَبَّهَ … بِـ… açıklamaları teşbih çerçevesi "
          "taşır; s18 bir `murakkab` çerçevesidir.")
if "3740-3900" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
other = {}
for p in (ROOT / "content/samples").iterdir():
    if p.name == PKG.name or not (p / "glossary.json").exists(): continue
    for k, v in json.loads((p / "glossary.json").read_text(encoding="utf-8"))["entries"].items():
        other.setdefault(k, set()).add(bare(v["lemma"]).split(" ")[0])
for k, v in GLOSS_ADD.items():
    if k in gl["entries"]:
        assert bare(gl["entries"][k]["lemma"]).replace("ال", "", 1) == bare(v["lemma"]).replace("ال", "", 1), f"key {k} already means {gl['entries'][k]['lemma']}"
        continue
    if k in other:
        assert bare(v["lemma"]).split(" ")[0] in other[k], f"key {k} means something else elsewhere: {other[k]}"
    gl["entries"][k] = v
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
V = mo["verbs"]
def put(key, e):
    if key not in V: V[key] = e
def doubled(bab, yv, m, mm, d, dd, amr, masdar, fail, maful=None, pmz=None, pmd=None, note=None):
    b = _sg.BABS[bab]
    return _sg.idgham(_sg.entry(b[0] + " — مُضَاعَفٌ", b[1], masdar, fail, _sg.mazi14(m, mm), _sg.mudari14(yv, d, dd), amr,
                                "يَ" + d + "َ", "يَ" + d + "َ", "تَ" + d + "َ", maful, pmz, pmd, note))
put("admara", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَضْمَر", "ضْمِر", "أَضْمِر", "إِضْمَار", "مُضْمِر", "مُضْمَر", "أُضْمِرَ", "يُضْمَرُ",
                          "فِي الْمَتْنِ مَبْنِيٌّ لِلْمَجْهُولِ: يُضْمَرُ التَّشْبِيهُ."))
put("sarraha", _sg.derived(_sg.B2, _sg.W2, "ُ", "صَرَّح", "صَرِّح", "صَرِّح", "تَصْرِيح", "مُصَرِّح", "مُصَرَّح", "صُرِّحَ", "يُصَرَّحُ"))
put("athbata", _sg.idgham(_sg.derived(_sg.B4, _sg.W4, "ُ", "أَثْبَت", "ثْبِت", "أَثْبِت", "إِثْبَات", "مُثْبِت", "مُثْبَت", "أُثْبِتَ", "يُثْبَتُ")))
put("anshaba", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَنْشَب", "نْشِب", "أَنْشِب", "إِنْشَاب", "مُنْشِب", "مُنْشَب", "أُنْشِبَ", "يُنْشَبُ",
                           "أَنْشَبَ الْمَخَالِبَ: عَلَّقَهَا وَأَثْبَتَهَا."))
put("alfa", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَلْفَ", "لْف", "i", "أَلْف", "إِلْفَاء", "مُلْفٍ (الْمُلْفِي)", "مُلْفًى", "أُلْفِيَ", "يُلْفَى",
                              "نَاقِصٌ عَلَى أَفْعَلَ: أَلْفَى يُلْفِي — أَلْفَيْتَ؛ مِنْ أَفْعَالِ الْقُلُوبِ."))
put("aqsara", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْصَر", "قْصِر", "أَقْصِر", "إِقْصَار", "مُقْصِر", None, None, None,
                          "لَازِمٌ: أَقْصَرَ عَنِ الشَّيْءِ — كَفَّ."))
put("arra", _sg.derived_naqis(_sg.B2, _sg.W2, "ُ", "عَرَّ", "عَرّ", "i", "عَرّ", "تَعْرِيَة", "مُعَرٍّ (الْمُعَرِّي)", "مُعَرًّى", "عُرِّيَ", "يُعَرَّى",
                              "نَاقِصٌ عَلَى فَعَّلَ: عَرَّى يُعَرِّي؛ الْمَجْهُولُ عُرِّيَ — كُسِرَ مَا قَبْلَ الْيَاءِ."))
put("fassara", _sg.derived(_sg.B2, _sg.W2, "ُ", "فَسَّر", "فَسِّر", "فَسِّر", "تَفْسِير", "مُفَسِّر", "مُفَسَّر", "فُسِّرَ", "يُفَسَّرُ"))
put("istalzama", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَلْزَم", "سْتَلْزِم", "اِسْتَلْزِم", "اِسْتِلْزَام", "مُسْتَلْزِم", "مُسْتَلْزَم", "اُسْتُلْزِمَ", "يُسْتَلْزَمُ"))
put("radda", doubled("nasara", "َ", "رَدّ", "رَدَد", "رُدّ", "رْدُد", ["رُدَّ", "رُدَّا", "رُدُّوا", "رُدِّي", "رُدَّا", "اُرْدُدْنَ"], "رَدّ", "رَادّ", "مَرْدُود", "رُدَّ", "يُرَدُّ",
                     "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: رَدَّ يَرُدُّ؛ الْمَجْهُولُ رُدَّ بِضَمِّ الْأَوَّلِ."))
put("shamma", doubled("nasara", "َ", "شَمّ", "شَمَم", "شُمّ", "شْمُم", ["شُمَّ", "شُمَّا", "شُمُّوا", "شُمِّي", "شُمَّا", "اُشْمُمْنَ"], "شَمّ", "شَامّ", "مَشْمُوم", "شُمَّ", "يُشَمُّ",
                      "مُضَاعَفٌ مِنْ بَابِ نَصَرَ: شَمَّ يَشُمُّ (وَيُقَالُ شَمِمَ يَشَمُّ)؛ الْمَجْهُولُ يُشَمُّ."))
put("saha", _sg.naqis1("nasara", "نَاقِصٌ وَاوِيٌّ", "w", "صَحَ", "صْح", "u", "اُصْح", "صَحْو", "صَاحٍ (الصَّاحِي)", None, None, None,
                       "نَاقِصٌ وَاوِيٌّ مِنْ بَابِ نَصَرَ: صَحَا يَصْحُو — صَحَا الْقَلْبُ."))
for k in ("ishtarata", "sara", "wajada", "nataqa"):
    put(k, find_morph(k))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the notes
GR = ROOT / "content/grammar"
NOTE_M = {
 "id": "istiara-makniyya",
 "title": {"ar": "الِاسْتِعَارَةُ بِالْكِنَايَةِ وَالتَّخْيِيلِيَّةُ — وَمَذْهَبُ السَّكَّاكِيِّ", "en": "The istiʿara by kinaya and the takhyiliyya — and Sakkaki's view", "tr": "Kinâye yoluyla istiâre ve tahyîliyye — ve Sekkâkî'nin görüşü"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — الاستعارة بالكناية والتخييلية"],
 "question": {
  "en": ["Is the BIHI's name spoken at all? In أَنْشَبَتِ الْمَنِيَّةُ أَظْفَارَهَا no beast is named: the likening (death to a beast of prey) is HIDDEN in the mind, only the mushabbah is spoken. That is the istiʿara BY KINAYA (the makniyya).",
         "How do we know a likening is there? By a THING PROPER TO THE BIHI being affirmed for the mushabbah — the claws. That affirming is the TAKHYILIYYA: an image lent to death, with no reality by sense or by reason.",
         "Where does Sakkaki differ? He calls the spoken mushabbah's word (الْمَنِيَّة) an istiʿara for the bihi, the annexed claws its clue — and the Talkhis answers: the word is used in what it was coined for; it is death that is meant."],
  "tr": ["BİHİN adı hiç söylenmiş mi? أَنْشَبَتِ الْمَنِيَّةُ أَظْفَارَهَا'da yırtıcı anılmaz: benzetme (ölümün yırtıcıya) zihinde GİZLİDİR, yalnız müşebbeh söylenir. KİNÂYE YOLUYLA istiâre (mekniyye) budur.",
         "Benzetmenin orada olduğunu nereden biliriz? BİHE HAS BİR ŞEYİN müşebbeh için isbatından — pençeler. O isbat TAHYÎLİYYEdir: ölüme ödünç verilmiş, hissen ve aklen gerçekliği olmayan bir hayal.",
         "Sekkâkî nerede ayrılır? Söylenen müşebbehin lafzını (الْمَنِيَّة) bih için istiâre, izâfe edilen pençeleri karînesi sayar — Telhîs cevap verir: lafız konulduğu mânâdadır; kastedilen ölümdür."]},
 "plain": {
  "en": "The likening stays in the mind and only the mushabbah is spoken, with a thing of the hidden bihi affirmed for it (death's claws, the state's tongue): that likening is an istiʿara BY KINAYA, the affirmed thing a TAKHYILIYYA. The engine finds the pair: a mark of a living thing annexed to an abstract one.",
  "tr": "Benzetme zihinde tutulup yalnız müşebbeh söylenince ve gizli bihe has bir şey onun için isbat edilince (ölümün pençeleri, hâlin dili, gençliğin atları) benzetme KİNÂYE YOLUYLA istiâre, isbat edilen şey TAHYÎLİYYEdir. Motor çifti bulur: soyut bir şeye izâfe edilmiş uzuv yahut âlet, ve gizli bihe uyan bir fiil."},
 "explanation": {
  "en": "The likening may be HIDDEN IN THE MIND (يُضْمَرُ التَّشْبِيهُ فِي النَّفْسِ), so that none of its arkan is spoken except the MUSHABBAH; and it is signalled by affirming for the mushabbah a thing that belongs properly to the MUSHABBAH BIHI. The likening so hidden is called an ISTIʿARA BY KINAYA (بِالْكِنَايَةِ) or one KEPT HIDDEN (مَكْنِيٌّ عَنْهَا), and the affirming of that thing an istiʿara TAKHYILIYYA. Abu Dhuʾayb's وَإِذَا الْمَنِيَّةُ أَنْشَبَتْ أَظْفَارَهَا • أَلْفَيْتَ كُلَّ تَمِيمَةٍ لَا تَنْفَعُ: he likened death to a beast of prey in snatching lives and affirmed for it the CLAWS, by which the beast's preying is complete — الْمَنِيَّة the makniyya, أَظْفَارَهَا the takhyiliyya, and أَنْشَبَتْ, which belongs to the beast, a TARSHIH. The tongue of the state — فَلِسَانُ حَالِي بِالشِّكَايَةِ أَنْطَقُ: the state likened to a speaking person, the TONGUE affirmed for it. Zuhayr's صَحَا الْقَلْبُ عَنْ سَلْمَى … وَعُرِّيَ أَفْرَاسُ الصِّبَا وَرَوَاحِلُهُ: youth likened to a direction of travel, as the pilgrimage, the HORSES and RIDING-CAMELS affirmed for it — though the two may be meant as the soul's powers, and then the istiʿara is a TAHQIQIYYA. SAKKAKI divides the istiʿara into MUSARRAHA (declared) and MAKNIYYA, and the declared into tahqiqiyya and takhyiliyya; he counts the tamthil among the tahqiqiyya (answered: the tamthil requires composition, and the istiʿara here is of the single word); he explains the takhyiliyya as what has no reality by sense or reason, like the word «claws»; and he makes the spoken mushabbah's word (الْمَنِيَّة) an istiʿara used for the bihi, with the annexed claws as its clue — answered: the word is used in what it was coined for, since death, not a beast, is what the speaker means. WHAT THE ENGINE CLAIMS: a makniyya CANDIDATE where a body part or an instrument of a living thing (claws, tongue, hand, wing, horses) is annexed to an abstract or lifeless noun, or predicated of it, and the verb around it suits the hidden bihi (fastening, speaking, unsaddling); it names the spoken mushabbah, the affirmed thing, and the tarshih words. It grades that reading against the authored pair of frames, and it does not name the hidden bihi itself — that is the musannif's explanation, carried on the murad.",
  "tr": "Benzetme ZİHİNDE GİZLENEBİLİR (يُضْمَرُ التَّشْبِيهُ فِي النَّفْسِ); öyle ki rükünlerinden MÜŞEBBEH dışında hiçbiri söylenmez; buna, müşebbeh için MÜŞEBBEHÜN BİHe has bir şeyin isbatıyla delâlet edilir. Böyle gizlenen benzetmeye KİNÂYE YOLUYLA (بِالْكِنَايَةِ) yahut KENDİSİNDEN KİNÂYE EDİLEN (مَكْنِيٌّ عَنْهَا) istiâre; o şeyin isbatına TAHYÎLİYYE istiâre denir. Ebû Züeyb'in وَإِذَا الْمَنِيَّةُ أَنْشَبَتْ أَظْفَارَهَا • أَلْفَيْتَ كُلَّ تَمِيمَةٍ لَا تَنْفَعُ beyti: ölümü canları kapmakta yırtıcıya benzetmiş, ona yırtıcının parçalamasının kemâlinin kendisiyle olduğu PENÇELERİ isbat etmiştir — الْمَنِيَّة mekniyye, أَظْفَارَهَا tahyîliyye, yırtıcıya ait أَنْشَبَتْ ise TERŞÎH. Hâlin dili — فَلِسَانُ حَالِي بِالشِّكَايَةِ أَنْطَقُ: hâl konuşan bir insana benzetilmiş, DİL ona isbat edilmiş. Züheyr'in صَحَا الْقَلْبُ عَنْ سَلْمَى … وَعُرِّيَ أَفْرَاسُ الصِّبَا وَرَوَاحِلُهُ beyti: gençlik hac gibi yol alınan bir yöne benzetilmiş, ATLAR ve DEVELER ona isbat edilmiş — gerçi ikisiyle nefsin kuvvetleri kastedilebilir; o zaman istiâre TAHKÎKİYYEdir. SEKKÂKÎ istiâreyi MUSARRAHA (açık) ve MEKNİYYE diye, musarrahayı da tahkîkiyye ve tahyîliyye diye böler; temsili tahkîkiyyeden sayar (cevap: temsil terkibi gerektirir, buradaki istiâre müfred kelimenindir); tahyîliyyeyi hissen ve aklen gerçekliği olmayan diye açıklar, «pençeler» lafzı gibi; söylenen müşebbehin lafzını (الْمَنِيَّة) bih için kullanılmış istiâre, izâfe edilen pençeleri karînesi sayar — cevap: lafız konulduğu mânâda kullanılmıştır; konuşanın kastı yırtıcı değil ölümdür. MOTORUN İDDİASI: canlı bir şeyin uzvu yahut âleti (pençe, dil, el, kanat, atlar) soyut yahut cansız bir isme izâfe edilmiş yahut ona yüklenmişse ve çevresindeki fiil gizli bihe uyuyorsa (geçirmek, konuşmak, eyer çözmek) bir mekniyye ADAYI; söylenen müşebbehi, isbat edilen şeyi ve terşîh kelimelerini adlandırır. Bu okumayı müellifin çift çerçevesine karşı sınar; gizli bihin kendisini adlandırmaz — o, murâdda taşınan musannif açıklamasıdır."},
 "examples": [
  {"ar": "وَإِذَا الْمَنِيَّةُ أَنْشَبَتْ أَظْفَارَهَا", "en": "death the makniyya; its claws the takhyiliyya; fastening the tarshih.", "tr": "ölüm mekniyye; pençeleri tahyîliyye; geçirmek terşîh.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "فَلِسَانُ حَالِي بِالشِّكَايَةِ أَنْطَقُ", "en": "the state the makniyya; the tongue the takhyiliyya.", "tr": "hâl mekniyye; dil tahyîliyye.", "sourceStory": "talkhis-al-miftah", "sentence": "s6"},
  {"ar": "وَعُرِّيَ أَفْرَاسُ الصِّبَا وَرَوَاحِلُهُ", "en": "youth the makniyya; horses and camels the takhyiliyya — or a tahqiqiyya.", "tr": "gençlik mekniyye; atlar ve develer tahyîliyye — yahut tahkîkiyye.", "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "شَبَّهَ الْمَنِيَّةَ بِالسَّبُعِ فِي اغْتِيَالِ النُّفُوسِ", "en": "the hidden likening, spelled out by the musannif.", "tr": "gizli benzetme, musannifin açıklamasıyla.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«أَظْفَارَ الْمَنِيَّةِ: pençeler, ölümün sebepleri için mürsel mecazdır»",
   "right": "«Tahyîliyyedir: pençeler, gizli yırtıcıya has bir şey olarak ölüme isbat edilmiştir; benzetme zihindedir»",
   "why": {"en": "There is no tie of cause or part here; there is a hidden likening. The claws are lent from the beast's picture, not moved by a relation.", "tr": "Burada sebep yahut cüz bağı yok; gizli bir benzetme var. Pençeler bir alâka ile kaymamış, yırtıcının resminden ödünç alınmıştır."}},
  {"wrong": "«الْمَنِيَّةُ kelimesi yırtıcı için istiâredir (Sekkâkî)»",
   "right": "«الْمَنِيَّةُ konulduğu mânâdadır — kastedilen ölümdür; istiâre lafızda değil, gizli benzetmededir»",
   "why": {"en": "The Talkhis's answer: a word used in its own meaning is no majaz. What is borrowed is the picture (the claws), not the name of death.", "tr": "Telhîs'in cevabı: kendi mânâsında kullanılan kelime mecaz değildir. Ödünç alınan, ölümün adı değil resimdir (pençeler)."}}],
 "relatedNotes": ["istiara", "arkan-al-istiara", "aqsam-al-istiara", "istiara-tabaiyya", "tarshih-wa-tajrid", "husn-al-istiara", "kinaya", "tashbih"]}
NOTE_H = {
 "id": "husn-al-istiara",
 "title": {"ar": "حُسْنُ الِاسْتِعَارَةِ — ظُهُورُ الْجَامِعِ وَخَفَاءُ التَّشْبِيهِ", "en": "The beauty of the istiʿara — the jamiʿ plain, the likening unseen", "tr": "İstiârenin güzelliği — câmi açık, benzetme görünmez"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — حسن الاستعارة"],
 "question": {
  "en": ["Does the istiʿara keep the CONDITIONS of a good likening? The tahqiqiyya and the tamthiliyya are good when the aspects of a good tashbih are observed.",
         "Can the likening be SMELT in the wording? A good istiʿara lets no scent of it show: it names the lion and never says «like».",
         "Is the JAMIʿ PLAIN? In the asliyya it must be, lest the istiʿara become a riddle — «I saw a lion» meaning a man of foul breath (as lions are) is not good; «a hundred camels without one fit to ride», meaning people, is drawn from the Prophet's ﷺ likening and is."],
  "tr": ["İstiâre güzel benzetmenin ŞARTLARINI koruyor mu? Tahkîkiyye ile temsîliyye, güzel teşbihin cihetlerine riayet edilince güzeldir.",
         "Benzetmenin KOKUSU lafızdan alınıyor mu? Güzel istiâre onun kokusunu göstermez: arslanı adlandırır, «gibi» demez.",
         "CÂMİ AÇIK mı? Asliyyede açık olmalı; yoksa istiâre bilmeceye döner — ağzı kokan (arslanlar gibi) bir adamı kastederek «bir arslan gördüm» güzel değildir; insanları kastederek «içinde binilecek bir tane olmayan yüz deve» Peygamber'in ﷺ benzetmesinden alınmıştır ve güzeldir."]},
 "plain": {
  "en": "A good istiʿara observes what makes a good likening, lets no scent of the likening show in its wording, and — in the asliyya — keeps its jamiʿ plain, or it becomes a riddle. The engine checks the surface: no adat, no wajh spoken, and a jamiʿ the stock likenesses know.",
  "tr": "Güzel istiâre, güzel benzetmeyi güzel yapana riayet eder, lafzında benzetmenin kokusunu göstermez ve — asliyyede — câmiini açık tutar; yoksa bilmeceye döner. Motor yüzeyi sınar: edat yok, vech söylenmemiş, yerleşik benzetmelerin bildiği bir câmi."},
 "explanation": {
  "en": "The BEAUTY of the tahqiqiyya and the tamthiliyya lies in OBSERVING THE ASPECTS OF A GOOD TASHBIH — the wajh well chosen, the ends fit — and in that NO SCENT OF THE LIKENING BE SMELT from the istiʿara in its wording: it must not say «like», nor name the wajh, nor let the mushabbah stand beside the bihi; the lion must simply be a lion. And in the ASLIYYA the PLAINNESS OF THE JAMIʿ is required, lest the istiʿara become like a RIDDLE (اللُّغْز): were one to say رَأَيْتُ أَسَدًا and mean a man of foul breath — lions being foul-breathed — it would not be good, for no hearer reaches that jamiʿ. Against it stands the compound رَأَيْتُ إِبِلًا مِائَةً لَا تَجِدُ فِيهَا رَاحِلَةً said of people: the jamiʿ — many, and hardly one of worth — is plain, and the picture is drawn from the Prophet's ﷺ own likening النَّاسُ كَإِبِلٍ مِائَةٍ لَا تَجِدُ فِيهَا رَاحِلَةً, where the kaf makes it a tashbih, not an istiʿara. WHAT THE ENGINE CLAIMS: for every istiʿara frame it reports the three surface tests — no adat in the sentence, no wajh spoken, the mushabbah not named beside the bihi — and for an asliyya whether the lent noun is one whose jamiʿ the stock likenesses carry (lion → bravery, sea → generosity, moon → beauty); a lent noun outside them is marked «jamiʿ not plain: riddle?». It does not judge the poet's taste beyond those tests.",
  "tr": "Tahkîkiyye ile temsîliyyenin GÜZELLİĞİ, GÜZEL TEŞBİHİN CİHETLERİNE RİAYETte — vech iyi seçilmiş, taraflar uygun — ve istiâreden lafzında BENZETMENİN KOKUSUNUN ALINMAMASINDAdır: «gibi» dememeli, vechi adlandırmamalı, müşebbehi bihin yanında bırakmamalı; arslan sadece arslan olmalı. ASLİYYEde CÂMİİN AÇIKLIĞI şarttır; yoksa istiâre BİLMECEye (اللُّغْز) döner: ağzı kokan bir adamı kastederek رَأَيْتُ أَسَدًا dense — arslanların ağzı kokar — güzel olmazdı; hiçbir dinleyici o câmie ulaşmaz. Karşısında insanlar için söylenen mürekkeb رَأَيْتُ إِبِلًا مِائَةً لَا تَجِدُ فِيهَا رَاحِلَةً durur: câmi — çok, ama işe yarar bir tanesi zor — açıktır ve resim Peygamber'in ﷺ kendi benzetmesi النَّاسُ كَإِبِلٍ مِائَةٍ لَا تَجِدُ فِيهَا رَاحِلَةً'den alınmıştır; orada kâf onu istiâre değil teşbih yapar. MOTORUN İDDİASI: her istiâre çerçevesi için üç yüzey sınamasını bildirir — cümlede edat yok, vech söylenmemiş, müşebbeh bihin yanında adlandırılmamış — ve asliyye için ödünç ismin câmiini yerleşik benzetmelerin taşıyıp taşımadığını (arslan → cesaret, deniz → cömertlik, ay → güzellik); dışında kalan ödünç isim «câmi açık değil: bilmece mi?» diye işaretlenir. Bu sınamaların ötesinde şairin zevkine hükmetmez."},
 "examples": [
  {"ar": "وَأَنْ لَا يُشَمَّ مِنْهَا رَائِحَةُ التَّشْبِيهِ لَفْظًا", "en": "no scent of the likening in the wording.", "tr": "lafızda benzetme kokusu yok.", "sourceStory": "talkhis-al-miftah", "sentence": "s16"},
  {"ar": "فَلَوْ قِيلَ رَأَيْتُ أَسَدًا وَأُرِيدَ رَجُلٌ أَبْخَرُ لَمْ يَحْسُنْ", "en": "a hidden jamiʿ makes a riddle.", "tr": "gizli câmi bilmece yapar.", "sourceStory": "talkhis-al-miftah", "sentence": "s17"},
  {"ar": "النَّاسُ كَإِبِلٍ مِائَةٍ لَا تَجِدُ فِيهَا رَاحِلَةً", "en": "the received likening the compound is drawn from — a tashbih, by its kaf.", "tr": "mürekkebin alındığı yerleşik benzetme — kâfıyla teşbih.", "sourceStory": "talkhis-al-miftah", "sentence": "s19"}],
 "commonMistakes": [
  {"wrong": "«رَأَيْتُ أَسَدًا ile ağzı kokan adam kastedilebilir: arslanın ağzı da kokar»",
   "right": "«Câmi açık değil: dinleyen cesareti anlar, kokuyu değil — istiâre bilmeceye döner, güzel olmaz»",
   "why": {"en": "The jamiʿ must be the trait the hearer reaches first. A true but hidden shared trait makes a riddle, not an istiʿara.", "tr": "Câmi, dinleyenin ilk ulaştığı vasıf olmalı. Doğru fakat gizli bir ortak vasıf istiâre değil bilmece yapar."}},
  {"wrong": "«النَّاسُ كَإِبِلٍ مِائَةٍ bir istiâre-i temsîliyyedir»",
   "right": "«Kâf söylenmiştir: teşbihtir; temsîliyye, kâfsız رَأَيْتُ إِبِلًا مِائَةً'dir»",
   "why": {"en": "One spoken adat is enough to keep a likening a tashbih. The istiʿara is the same picture with the adat and the mushabbah dropped.", "tr": "Tek bir söylenmiş edat benzetmeyi teşbih olarak tutmaya yeter. İstiâre, edatı ve müşebbehi düşmüş aynı resimdir."}}],
 "relatedNotes": ["istiara-makniyya", "istiara", "aqsam-al-istiara", "tarshih-wa-tajrid", "majaz-murakkab", "tashbih", "wajh-al-shabah", "aqsam-al-tashbih"]}
for n in (NOTE_M, NOTE_H):
    (GR / f"{n['id']}.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")
for nid, add in (("istiara", ["istiara-makniyya", "husn-al-istiara"]), ("arkan-al-istiara", ["istiara-makniyya"]),
                 ("tarshih-wa-tajrid", ["istiara-makniyya", "husn-al-istiara"]), ("majaz-murakkab", ["husn-al-istiara"]), ("kinaya", ["istiara-makniyya"])):
    fp = GR / f"{nid}.json"
    if not fp.exists(): continue
    w = json.loads(fp.read_text(encoding="utf-8"))
    ch = False
    for a in add:
        if a not in w.get("relatedNotes", []): w.setdefault("relatedNotes", []).append(a); ch = True
    if ch: fp.write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch54:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; notes istiara-makniyya, husn-al-istiara;",
      "majaz frames:", sum(len(x["majaz"]) if isinstance(x.get("majaz"), list) else (1 if x.get("majaz") else 0) for x in S),
      "tashbih frames:", sum(1 for x in S if x.get("tashbih")))
