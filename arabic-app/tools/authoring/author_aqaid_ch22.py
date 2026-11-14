# -*- coding: utf-8 -*-
"""Author chapter 22 of aqaid-ahl-al-sunna — what the imam need not be, and what he must.

Follows chapter 21. The matn now clears away two conditions people impose on
the imamate and do not belong to it — infallibility, and being the best of his
age — and then states the one that does: that he be of the people of full
authority, knowing in governance.

Grammar this chapter is chosen to teach:
  • أَنْ يَكُونَ twice more, and the second time with the whole masdar joined by
    وَلَا to the first — a ma'tuf that is not a word but a MASDAR.
  • أَفْضَلَ أَهْلِ زَمَانِهِ — a three-member idafa headed by an ism tafdil, and
    every consequence the Idafa engine builds is visible in it at once.
  • يُشْتَرَطُ — mabni li-l-majhul; its na'ib al-fa'il is the masdar itself.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
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
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
def g(lemma, root, pos, en, tr, level, plural=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    return e
S = []

TITLE22 = {"ar": "مَا لَا يُشْتَرَطُ فِي الْإِمَامِ وَمَا يُشْتَرَطُ",
           "en": "What Is Not Required of the Imam, and What Is",
           "tr": "İmâmda Şart Olmayanlar ve Olanlar"}

S.append({"id": "s1", "translation": {
 "en": "And it is not required that he be free from sin,",
 "tr": "İmâmın ma'sûm olması şart değildir,"},
 "tokens": [
  tok("وَلَا","la","part",["atf-nasaq"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "An isti'naf waw and a negating «la» that governs nothing.",
      "İstinâf vâvı ve amel etmeyen nefiy «lâ»sı.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("يُشْتَرَطُ","ishtarata","verb",["naib-al-fail","form-viii-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَنَائِبُ الْفَاعِلِ هُوَ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.",
      "A mudari' built for the PASSIVE, in raf' — and its na'ib al-fa'il is the MASDAR that follows: «his being sinless is not required».",
      "Meçhûl bina edilmiş merfû muzâri — nâib-i fâili, ardından gelen MÜEVVEL MASDARdır: «ma'sûm olması şart değildir»."),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.",
      "The masdar-making particle, putting the verb in nasb; the masdar it makes stands in RAF' as the na'ib al-fa'il.",
      "Nasb eden masdar harfi; te'vîl edilen masdar, nâib-i fâil olarak mahallen MERFÛdur."),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ»، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ».",
      "A naqis mudari' in nasb after «an»; its ism is a hidden «he».",
      "«أَنْ» ile mansub nâkıs muzâri; ismi müstetir «هُوَ» zamîridir."),
  tok("مَعْصُومًا","masum","noun",["ism-maful","kana-wa-akhawatuha"],
      "خَبَرُ «يَكُونَ» مَنْصُوبٌ بِالْفَتْحَةِ — اسْمُ مَفْعُولٍ مِنْ «عَصَمَ» عَلَى مَفْعُولٍ.",
      "The khabar of «yakuna», in nasb by the fatha — the ism maf'ul of عَصَمَ on مَفْعُول.",
      "«يَكُونَ»nin haberi, fetha ile mansub — «عَصَمَ»nin MEF'ÛL vezninde ism-i mef'ûlü.", punct="،"),
 ],
 "jumal": [J("وَلَا يُشْتَرَطُ أَنْ يَكُونَ مَعْصُومًا",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf verbal clause — i'rabless.",
   "İstinâfî fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "nor that he be the best of the people of his age.",
 "tr": "zamanının ehlinin en faziletlisi olması da şart değildir."},
 "tokens": [
  tok("وَلَا","la","part",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ وَ«لَا» لِتَأْكِيدِ النَّفْيِ — وَالْمَعْطُوفُ مَصْدَرٌ لَا مُفْرَدٌ.",
      "A joining waw and a «la» strengthening the negation — and what is joined here is a MASDAR, not a single word.",
      "Atıf vâvı ve nefyi te'kîd eden «lâ» — buradaki ma'tûf bir kelime değil, MASDARdır.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la","part")]),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya","atf-nasaq"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ مَعْطُوفٌ عَلَى الْمَصْدَرِ الْأَوَّلِ فِي مَحَلِّ رَفْعٍ.",
      "The masdar-making particle again; this masdar is joined to the first one and shares its position in raf'.",
      "Yine masdar harfi; bu masdar evvelkine ma'tûftur ve onun ref' mahallini paylaşır."),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ»، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ.",
      "A naqis mudari' in nasb after «an»; its ism is hidden.",
      "«أَنْ» ile mansub nâkıs muzâri; ismi müstetirdir."),
  tok("أَفْضَلَ","afdal","noun",["ism-tafdil","kana-wa-akhawatuha","idafa-definiteness"],
      "خَبَرُ «يَكُونَ» مَنْصُوبٌ بِالْفَتْحَةِ وَهُوَ مُضَافٌ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ، وَإِنَّمَا نُوِّنَ لَوْ لَمْ يُضَفْ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "The khabar of «yakuna», in nasb by the fatha and a MUDAF — an elative on أَفْعَل. Standing alone it would be barred from tanwin; here the idafa is what it wears instead.",
      "«يَكُونَ»nin haberi, fetha ile mansub ve MUZÂFtır — EF'AL vezninde ism-i tafdîl. Tek başına gayr-i munsarif olurdu; burada onun yerine izâfet vardır."),
  tok("أَهْلِ","ahl","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ أَيْضًا — حَلْقَةٌ وُسْطَى تَجْمَعُ الْوَصْفَيْنِ مَعًا.",
      "The mudaf ilayh in jarr, and itself a mudaf — a MIDDLE link, which is both roles at once.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — iki vasfı birden taşıyan ORTA halka."),
  tok("زَمَانِهِ","zaman","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَبِهَا انْغَلَقَتِ السِّلْسِلَةُ.",
      "The mudaf ilayh in jarr, itself a mudaf, and the ha is its mudaf ilayh — with which the chain closes.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; hâ ise onun muzâfun ileyhidir — zincir onunla kapanır.",
      punct=".", segments=[seg("زَمَانِ","zaman","noun"), seg("هِ","pron-3ms","pron")]),
 ],
 "jumal": [J("وَلَا أَنْ يَكُونَ أَفْضَلَ أَهْلِ زَمَانِهِ",
   "الْمَصْدَرُ الْمُؤَوَّلُ مَعْطُوفٌ عَلَى نَائِبِ الْفَاعِلِ — فِي مَحَلِّ رَفْعٍ.",
   "The masdar is joined to the na'ib al-fa'il, and so stands in raf' with it.",
   "Müevvel masdar nâib-i fâile ma'tûftur — mahallen merfûdur.")]})

S.append({"id": "s3", "translation": {
 "en": "And it is required that he be of the people of full authority, knowing in governance.",
 "tr": "Tam velâyet ehlinden ve siyâseti bilen biri olması ise şarttır."},
 "tokens": [
  tok("وَيُشْتَرَطُ","ishtarata","verb",["naib-al-fail","form-viii-verbs","mudari-marfu"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«يُشْتَرَطُ» مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.",
      "An isti'naf waw; «is required» is a passive mudari' in raf'.",
      "İstinâf vâvı; «يُشْتَرَطُ» meçhûl bina edilmiş merfû muzâridir.",
      segments=[seg("وَ","wa","conj"), seg("يُشْتَرَطُ","ishtarata","verb")]),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ.",
      "The masdar-making particle; the masdar stands in raf' as the na'ib al-fa'il.",
      "Nasb eden masdar harfi; masdar, nâib-i fâil olarak mahallen merfûdur."),
  tok("يَكُونَ","kana","verb",["kana-wa-akhawatuha","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِـ«أَنْ»، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ.",
      "A naqis mudari' in nasb after «an»; its ism is hidden.",
      "«أَنْ» ile mansub nâkıs muzâri; ismi müstetirdir."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ «يَكُونَ» — وَكُلُّ جَارٍّ وَمَجْرُورٍ لَا بُدَّ لَهُ مِنْ مُتَعَلَّقٍ.",
      "A jarr letter; the phrase is the khabar of «yakuna» — and EVERY jarr-majrur must attach to something.",
      "Cer harfi; câr-mecrûr «يَكُونَ»nin haberidir — ve her câr-mecrûrun mutlaka bir MÜTEALLAKI olmalıdır."),
  tok("أَهْلِ","ahl","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ.",
      "In jarr after «min», and a mudaf.",
      "«مِنْ» ile mecrûr ve muzâftır."),
  tok("الْوِلَايَةِ","wilaya","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرٌ بِمَعْنَى السُّلْطَةِ وَالتَّدْبِيرِ.",
      "The mudaf ilayh in jarr — a masdar meaning authority and management.",
      "Mecrûr muzâfun ileyh — velâyet, yani yetki ve tedbîr mânâsında masdar."),
  tok("الْكَامِلَةِ","kamil","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«الْوِلَايَةِ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «كَمَلَ»، وَتَبِعَ مَنْعُوتَهُ فِي الْجَرِّ وَالتَّعْرِيفِ وَالتَّأْنِيثِ.",
      "A na't of «the authority», in jarr — the ism fa'il of كَمَلَ, following its noun in case, in definiteness and in gender: a na't matches in four of five.",
      "«الْوِلَايَةِ»nin na'tı, mecrûr — «كَمَلَ»nin ism-i fâili; men'ûtuna cerde, marifelikte ve te'nîste tâbi olmuştur.", punct="."),
 ],
 "jumal": [J("وَيُشْتَرَطُ أَنْ يَكُونَ مِنْ أَهْلِ الْوِلَايَةِ الْكَامِلَةِ",
   "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf verbal clause — i'rabless.",
   "İstinâfî fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "ishtarata": g("اشْتَرَطَ", "ش ر ط", "verb", "to stipulate, require", "şart koşmak", 4),
 "masum":     g("مَعْصُوم", "ع ص م", "noun", "protected from sin (ism maf'ul)", "ma'sûm; günahtan korunmuş", 4),
 "zaman":     g("زَمَان", "ز م ن", "noun", "time, age", "zaman, devir", 2),
 "wilaya":    g("وِلَايَة", "و ل ي", "noun", "authority, guardianship (masdar)", "velâyet; yetki", 4),
 "kamil":     g("كَامِل", "ك م ل", "noun", "complete, full (ism fa'il)", "kâmil; tam", 2),
}

def build_morph():
    out = {}
    # اِشْتَرَطَ is ALREADY in kitab-al-sulh under this very key, and a lex key is
    # global: generating a second paradigm here would have shipped the same
    # verb twice, spelled two ways (اشْتَرَطَ against اِشْتَرَطَ — the hamzat wasl
    # without its kasra). So it is COPIED after a lemma identity check, which
    # is the standing rule for a verb that two packages share.
    src = json.loads((ROOT / "content/samples/kitab-al-sulh/morphology.json")
                     .read_text(encoding="utf-8"))["verbs"]["ishtarata"]
    assert src["mazi"][0].replace("ِ", "") == "اشْتَرَطَ".replace("ِ", ""), \
        "kitab-al-sulh's ishtarata is not the verb this chapter means"
    out["ishtarata"] = src
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/22.json").write_text(
    json.dumps({"chapter": 22, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 22 for c in man["chapters"]):
    man["chapters"].append({"n": 22, "title": TITLE22})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.20.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch22:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
