# -*- coding: utf-8 -*-
"""Author chapter 19 of aqaid-ahl-al-sunna — the offices of the imam.

Continues chapter 18's «وَلَا بُدَّ لِلْمُسْلِمِينَ مِنْ إِمَامٍ يَقُومُ بِتَنْفِيذِ أَحْكَامِهِمْ»
straight into the matn's enumeration of what he stands up to do. Every item is
a masdar in jarr, joined by waw to «تَنْفِيذِ» — one long chain of ma'tufat
hanging off the ba of «يَقُومُ بِ». The span stops early inside the list; it
skips nothing.

This chapter is also the best showcase the package has for the derived nouns:
الْمُتَغَلِّبَة and الْمُتَلَصِّصَة are ism fa'il on Form V, قُطَّاع is فُعَّال as a
broken plural of قَاطِع, الْمُنَازَعَات is the Form III masdar, and الْوَاقِعَة is a
plain ism fa'il. The IsmTagger reads all of them off the surface.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
sys.path.insert(0, str(ROOT / "tools/authoring"))
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
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
def g(lemma, root, pos, en, tr, level, plural=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
S = []

TITLE19 = {"ar": "وَظَائِفُ الْإِمَامِ", "en": "The Offices of the Imam",
           "tr": "İmâmın Vazîfeleri"}

# Every item of the list wears the same i'rab, so the note that says so is
# written once and reused — a ma'tuf is a ma'tuf whatever it names.
def MATUF(what_ar, what_en, what_tr):
    return ("مَعْطُوفٌ عَلَى «تَنْفِيذِ» مَجْرُورٌ وَهُوَ مُضَافٌ — " + what_ar,
            "Joined to «the carrying-out», in jarr and a mudaf — " + what_en,
            "«تَنْفِيذِ»ye ma'tûf, mecrûr ve muzâf — " + what_tr)

S.append({"id": "s1", "translation": {
 "en": "and establishing their prescribed punishments, and sealing their frontiers, and equipping their armies,",
 "tr": "hadlerini ikāme etmek, sınırlarını kapamak, ordularını techîz etmek,"},
 "tokens": [
  tok("وَإِقَامَةِ","iqama","noun",["atf-nasaq","masdar","form-iv-verbs","idafa-definiteness"],
      *MATUF("مَصْدَرُ «أَقَامَ» عَلَى إِفْعَالٍ، وَأَصْلُهُ إِقْوَامٌ فَنُقِلَتْ حَرَكَةُ الْوَاوِ ثُمَّ قُلِبَتْ أَلِفًا ثُمَّ حُذِفَتْ وَعُوِّضَ عَنْهَا بِالتَّاءِ.",
             "the masdar of أَقَامَ on إِفْعَال. Its origin is إِقْوَام: the waw's vowel moved back, the waw turned alif, the alif was dropped, and the TA at the end stands in its place.",
             "«أَقَامَ»nın İF'ÂL vezninde masdarı. Aslı إِقْوَام'dır: vâvın harekesi nakledildi, vâv elife kalboldu, elif hazfedildi ve yerine sondaki TÂ ıvaz getirildi."),
      segments=[seg("وَ","wa","conj"), seg("إِقَامَةِ","iqama","noun")]),
  tok("حُدُودِهِمْ","hadd","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَ«هِمْ» مُضَافٌ إِلَيْهِ ثَانٍ — وَ«حُدُود» جَمْعُ «حَدٍّ» عَلَى فُعُولٍ.",
      "The mudaf ilayh in jarr, itself a mudaf; «him» is a second mudaf ilayh — «hudud» is the plural of «hadd» on فُعُول.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; «هِمْ» ikinci muzâfun ileyhtir — «حُدُود», «حَدّ»ın FUÛL vezninde cemidir.",
      segments=[seg("حُدُودِ","hadd","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("وَسَدِّ","sadd","noun",["atf-nasaq","masdar","idafa-definiteness"],
      *MATUF("مَصْدَرُ «سَدَّ» الْمُضَاعَفِ.", "the masdar of the doubled verb سَدَّ.",
             "muzâaf «سَدَّ» fiilinin masdarı."),
      segments=[seg("وَ","wa","conj"), seg("سَدِّ","sadd","noun")]),
  tok("ثُغُورِهِمْ","thaghr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَ«هِمْ» مُضَافٌ إِلَيْهِ ثَانٍ — وَ«ثُغُور» جَمْعُ «ثَغْرٍ».",
      "The mudaf ilayh in jarr, itself a mudaf; «him» is a second mudaf ilayh — «thughur» is the plural of «thaghr», a frontier post.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; «هِمْ» ikinci muzâfun ileyhtir — «ثُغُور», serhad demek olan «ثَغْر»ın cemidir.",
      segments=[seg("ثُغُورِ","thaghr","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("وَتَجْهِيزِ","tajhiz","noun",["atf-nasaq","masdar","form-ii-verbs","idafa-definiteness"],
      *MATUF("مَصْدَرُ «جَهَّزَ» عَلَى تَفْعِيلٍ.", "the masdar of جَهَّزَ on تَفْعِيل.",
             "«جَهَّزَ»nin TEF'ÎL vezninde masdarı."),
      segments=[seg("وَ","wa","conj"), seg("تَجْهِيزِ","tajhiz","noun")]),
  tok("جُيُوشِهِمْ","jaysh","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَ«هِمْ» مُضَافٌ إِلَيْهِ ثَانٍ — وَ«جُيُوش» جَمْعُ «جَيْشٍ» عَلَى فُعُولٍ.",
      "The mudaf ilayh in jarr, itself a mudaf; «him» is a second mudaf ilayh — «juyush» is the plural of «jaysh» on فُعُول.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; «هِمْ» ikinci muzâfun ileyhtir — «جُيُوش», «جَيْش»in FUÛL vezninde cemidir.",
      punct="،", segments=[seg("جُيُوشِ","jaysh","noun"), seg("هِمْ","pron-3mp","pron")]),
 ],
 "jumal": [J("وَإِقَامَةِ حُدُودِهِمْ وَسَدِّ ثُغُورِهِمْ وَتَجْهِيزِ جُيُوشِهِمْ",
   "مَعَاطِيفُ عَلَى «تَنْفِيذِ» — لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ لِأَنَّهَا مُفْرَدَاتٌ لَا جُمَلٌ.",
   "A run of ma'tufat on «the carrying-out» — these are single words, not clauses, so the question of a clause's position does not arise.",
   "«تَنْفِيذِ»ye ma'tûflar — bunlar cümle değil müfredlerdir; cümle mahalli sorusu burada sorulmaz.")]})

S.append({"id": "s2", "translation": {
 "en": "and taking their alms, and subduing the usurper, the marauder and the highwayman,",
 "tr": "zekâtlarını almak, mütegallibeyi, mütelassısayı ve yol kesenleri kahretmek,"},
 "tokens": [
  tok("وَأَخْذِ","akhdh","noun",["atf-nasaq","masdar","idafa-definiteness"],
      *MATUF("مَصْدَرُ «أَخَذَ» الْمَهْمُوزِ الْفَاءِ.",
             "the masdar of أَخَذَ, whose first radical is a hamza.",
             "fâ'ı hemzeli «أَخَذَ» fiilinin masdarı."),
      segments=[seg("وَ","wa","conj"), seg("أَخْذِ","akhdh","noun")]),
  tok("صَدَقَاتِهِمْ","sadaqa","noun",["jam-muannath-salim","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ، وَ«هِمْ» مُضَافٌ إِلَيْهِ ثَانٍ — جَمْعُ مُؤَنَّثٍ سَالِمٌ.",
      "The mudaf ilayh in jarr by the KASRA and a mudaf; «him» is a second mudaf ilayh — a sound feminine plural, which takes a kasra in nasb as well as in jarr.",
      "Kesra ile mecrûr muzâfun ileyh ve muzâf; «هِمْ» ikinci muzâfun ileyhtir — cemi müennes sâlim, nasb hâlinde de kesra alır.",
      segments=[seg("صَدَقَاتِ","sadaqa","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("وَقَهْرِ","qahr","noun",["atf-nasaq","masdar","idafa-definiteness"],
      *MATUF("مَصْدَرُ «قَهَرَ».", "the masdar of قَهَرَ.", "«قَهَرَ»nin masdarı."),
      segments=[seg("وَ","wa","conj"), seg("قَهْرِ","qahr","noun")]),
  tok("الْمُتَغَلِّبَةِ","mutaghallib","noun",["ism-fail","form-v-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «تَغَلَّبَ» عَلَى مُتَفَعِّلٍ، وَالتَّاءُ لِلْجَمَاعَةِ.",
      "The mudaf ilayh in jarr — the ism fa'il of تَغَلَّبَ on مُتَفَعِّل; the ta makes it a BODY of such people, not one man.",
      "Mecrûr muzâfun ileyh — «تَغَلَّبَ»nin MÜTEFA''İL vezninde ism-i fâili; tâ, tek kişiyi değil bir ZÜMREyi bildirir."),
  tok("وَالْمُتَلَصِّصَةِ","mutalassis","noun",["atf-nasaq","ism-fail","form-v-verbs"],
      "مَعْطُوفٌ عَلَى «الْمُتَغَلِّبَةِ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «تَلَصَّصَ» عَلَى مُتَفَعِّلٍ.",
      "Joined to «the usurper», in jarr — the ism fa'il of تَلَصَّصَ on مُتَفَعِّل.",
      "«الْمُتَغَلِّبَةِ»ye ma'tûf, mecrûr — «تَلَصَّصَ»nin MÜTEFA''İL vezninde ism-i fâili.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَلَصِّصَةِ","mutalassis","noun")]),
  tok("وَقُطَّاعِ","quttaa","noun",["atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الْمُتَغَلِّبَةِ» مَجْرُورٌ وَهُوَ مُضَافٌ — جَمْعُ «قَاطِعٍ» عَلَى فُعَّالٍ.",
      "Joined to «the usurper», in jarr and a mudaf — the plural of قَاطِع on فُعَّال.",
      "«الْمُتَغَلِّبَةِ»ye ma'tûf, mecrûr ve muzâf — «قَاطِع»in FU''ÂL vezninde cemidir.",
      segments=[seg("وَ","wa","conj"), seg("قُطَّاعِ","quttaa","noun")]),
  tok("الطَّرِيقِ","tariq","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَ«قُطَّاعُ الطَّرِيقِ» عَلَمٌ بِالْغَلَبَةِ عَلَى الْمُحَارِبِينَ.",
      "The mudaf ilayh in jarr — «cutters of the road» has become, by usage, the standing name for brigands.",
      "Mecrûr muzâfun ileyh — «قُطَّاعُ الطَّرِيقِ», kullanım galebesiyle yol kesenlerin husûsî adı olmuştur.", punct="،"),
 ],
 "jumal": [J("وَأَخْذِ صَدَقَاتِهِمْ وَقَهْرِ الْمُتَغَلِّبَةِ وَالْمُتَلَصِّصَةِ وَقُطَّاعِ الطَّرِيقِ",
   "مَعَاطِيفُ عَلَى «تَنْفِيذِ» — مُفْرَدَاتٌ لَا جُمَلٌ.",
   "More ma'tufat on «the carrying-out» — single words, not clauses.",
   "«تَنْفِيذِ»ye ma'tûflar — cümle değil müfredlerdir.")]})

S.append({"id": "s3", "translation": {
 "en": "and holding the Friday prayers and the festivals, and cutting off the disputes that fall out between people.",
 "tr": "cumaları ve bayramları ikāme etmek, kullar arasında vâki olan çekişmeleri kesmek."},
 "tokens": [
  tok("وَإِقَامَةِ","iqama","noun",["atf-nasaq","masdar","form-iv-verbs","idafa-definiteness"],
      *MATUF("وَهُوَ مَصْدَرُ «أَقَامَ» كَمَا مَرَّ.",
             "the masdar of أَقَامَ, as above.", "geçtiği gibi «أَقَامَ»nın masdarı."),
      segments=[seg("وَ","wa","conj"), seg("إِقَامَةِ","iqama","noun")]),
  tok("الْجُمَعِ","jumua","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «جُمُعَةٍ».",
      "The mudaf ilayh in jarr — the plural of «jumu'a», the Friday.",
      "Mecrûr muzâfun ileyh — «جُمُعَة»nin cemidir."),
  tok("وَالْأَعْيَادِ","id","noun",["atf-nasaq"],
      "مَعْطُوفٌ عَلَى «الْجُمَعِ» مَجْرُورٌ — جَمْعُ «عِيدٍ» عَلَى أَفْعَالٍ، وَأَصْلُهُ أَعْوَادٌ فَقُلِبَتِ الْوَاوُ يَاءً لِمُشَاكَلَةِ الْوَاحِدِ.",
      "Joined to «the Fridays», in jarr — the plural of «id» on أَفْعَال. Its origin is أَعْوَاد; the waw turned YA to match the singular عِيد.",
      "«الْجُمَعِ»e ma'tûf, mecrûr — «عِيد»in EF'ÂL vezninde cemi. Aslı أَعْوَاد'dır; tekiline benzesin diye vâv YÂ'ya kalbolmuştur.",
      segments=[seg("وَ","wa","conj"), seg("الْأَعْيَادِ","id","noun")]),
  tok("وَقَطْعِ","qat","noun",["atf-nasaq","masdar","idafa-definiteness"],
      *MATUF("مَصْدَرُ «قَطَعَ».", "the masdar of قَطَعَ.", "«قَطَعَ»nin masdarı."),
      segments=[seg("وَ","wa","conj"), seg("قَطْعِ","qat","noun")]),
  tok("الْمُنَازَعَاتِ","munazaa","noun",["jam-muannath-salim","masdar","form-iii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ «مُنَازَعَةٍ»، وَهِيَ مَصْدَرُ «نَازَعَ» عَلَى مُفَاعَلَةٍ.",
      "The mudaf ilayh in jarr by the kasra — the plural of «munaza'a», the masdar of نَازَعَ on مُفَاعَلَة.",
      "Kesra ile mecrûr muzâfun ileyh — «مُنَازَعَة»nin cemi; o da «نَازَعَ»nin MÜFÂALE vezninde masdarıdır."),
  tok("الْوَاقِعَةِ","waqia","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«الْمُنَازَعَاتِ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «وَقَعَ» عَلَى فَاعِلٍ.",
      "A na't of «the disputes», in jarr — the ism fa'il of وَقَعَ on فَاعِل.",
      "«الْمُنَازَعَاتِ»in na'tı, mecrûr — «وَقَعَ»nin FÂİL vezninde ism-i fâili."),
  tok("بَيْنَ","bayna","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِـ«الْوَاقِعَةِ».",
      "A place-adverb in nasb and a mudaf, attaching to «that fall out».",
      "Mansub mekân zarfı ve muzâf; «الْوَاقِعَةِ»ye taalluk eder."),
  tok("الْعِبَادِ","abd","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — «عِبَاد» جَمْعُ «عَبْدٍ» عَلَى فِعَالٍ.",
      "The mudaf ilayh in jarr — «ibad» is the plural of «abd» on فِعَال.",
      "Mecrûr muzâfun ileyh — «عِبَاد», «عَبْد»in FİÂL vezninde cemidir.", punct="."),
 ],
 "jumal": [J("وَإِقَامَةِ الْجُمَعِ وَالْأَعْيَادِ وَقَطْعِ الْمُنَازَعَاتِ الْوَاقِعَةِ بَيْنَ الْعِبَادِ",
   "مَعَاطِيفُ عَلَى «تَنْفِيذِ» — مُفْرَدَاتٌ لَا جُمَلٌ.",
   "The last of the ma'tufat taken here — single words, not clauses.",
   "Burada alınan son ma'tûflar — cümle değil müfredlerdir.")]})

GLOSS_ADD = {
 "iqama":       g("إِقَامَة", "ق و م", "noun", "establishing, setting up (masdar, Form IV)", "ikāme; ayakta tutma (masdar)", 4),
 "hadd":        g("حَدّ", "ح د د", "noun", "a prescribed punishment; a limit", "had; sınır, ceza", 3, plural="حُدُود"),
 "sadd":        g("سَدّ", "س د د", "noun", "sealing, blocking (masdar)", "sedd; kapama (masdar)", 3),
 "thaghr":      g("ثَغْر", "ث غ ر", "noun", "a frontier post", "serhad; sınır boyu", 4, plural="ثُغُور"),
 "tajhiz":      g("تَجْهِيز", "ج ه ز", "noun", "equipping, outfitting (masdar, Form II)", "techîz; donatma (masdar)", 4),
 "jaysh":       g("جَيْش", "ج ي ش", "noun", "an army", "ordu", 2, plural="جُيُوش"),
 "akhdh":       g("أَخْذ", "أ خ ذ", "noun", "taking (masdar)", "ahz; alma (masdar)", 2),
 "sadaqa":      g("صَدَقَة", "ص د ق", "noun", "alms", "sadaka; zekât", 2, plural="صَدَقَات"),
 "qahr":        g("قَهْر", "ق ه ر", "noun", "subduing, overpowering (masdar)", "kahr; bastırma (masdar)", 3),
 "mutaghallib": g("مُتَغَلِّب", "غ ل ب", "noun", "one who seizes power by force (ism fa'il, Form V)", "mütegallib; zorla hâkim olan", 5),
 "mutalassis":  g("مُتَلَصِّص", "ل ص ص", "noun", "a marauder, one who takes to thieving (ism fa'il, Form V)", "mütelassıs; hırsızlığa yeltenen", 5),
 "quttaa":      g("قُطَّاع", "ق ط ع", "noun", "cutters (plural of قَاطِع); قُطَّاعُ الطَّرِيقِ = highwaymen", "kesenler («قَاطِع»in cemi); قُطَّاعُ الطَّرِيقِ = yol kesenler", 4),
 "jumua":       g("جُمُعَة", "ج م ع", "noun", "Friday; the Friday prayer", "cuma; cuma namazı", 2, plural="جُمَع"),
 "id":          g("عِيد", "ع و د", "noun", "a festival", "bayram", 2, plural="أَعْيَاد"),
 "munazaa":     g("مُنَازَعَة", "ن ز ع", "noun", "a dispute (masdar, Form III)", "münâzaa; çekişme (masdar)", 4),
 "waqia":       g("وَاقِع", "و ق ع", "noun", "falling out, occurring (ism fa'il)", "vâki olan; meydana gelen", 3),
 "bayna":       g("بَيْنَ", "ب ي ن", "noun", "between (adverb of place)", "arasında (mekân zarfı)", 1),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/19.json").write_text(
    json.dumps({"chapter": 19, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 19 for c in man["chapters"]):
    man["chapters"].append({"n": 19, "title": TITLE19})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.17.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch19:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
