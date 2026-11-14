# -*- coding: utf-8 -*-
"""Author chapter 43 of talkhis-al-miftah — التَّكْمِيلُ وَالتَّتْمِيمُ.

Sahifa 99 (lines ~2870-2890): the sixth and seventh occasions of
itnab, a minimal pair on ONE hinge — does the speech suggest the
OPPOSITE of what is meant?

  • TAKMIL (also called IHTIRAS): in speech that DOES suggest the
    contrary, bring what repels it. Tarafa's rain-prayer فَسَقَى
    دِيَارَكِ غَيْرَ مُفْسِدِهَا • صَوْبُ الرَّبِيعِ وَدِيمَةٌ تَهْمِي
    — mid-speech, «without ruining them» guards the blessing from
    reading as a flood; and Ma'ida 5:54's أَذِلَّةٍ عَلَى
    الْمُؤْمِنِينَ أَعِزَّةٍ عَلَى الْكَافِرِينَ — at speech's end,
    «mighty against the disbelievers» guards humility from reading
    as weakness.
  • TATMIM: in speech that does NOT suggest the contrary, bring a
    FADLA for a point such as mubalagha — وَيُطْعِمُونَ الطَّعَامَ
    عَلَى حُبِّهِ (76:8): with the pronoun read to the food, «despite
    loving it» heaps the giving higher.

ATTRIBUTION: s4 is al-Ma'ida 5:54 (part) and s6 al-Insan 76:8 (part),
received Qur'anic text quoted exactly in standard imla as the source
prints them; s2-s3 are Tarafa b. al-Abd's bayt as the source recites
it, split at the hemistich; s1 and s5 are the musannif's definitions
as the source recites them (the ch38 definitional-frame precedent).

Grammar this chapter teaches:
  • note 147 `takmil-wa-tatmim` — the two definitions verbatim, the
    yuhimu/la-yuhimu hinge, and the seat freedom (mid-speech or end).
  • new paradigms: أَوْهَمَ (IV), دَفَعَ, سَقَى (naqis yai), هَمَى
    (naqis yai); أَطْعَمَ copied from kaffarat.
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
J = lambda text, ar, en, tr: {"text": text, "ar": ar, "en": en, "tr": tr}
def g(lemma, root, pos, en, tr, level, plural=None, form=None):
    e = {"lemma": lemma, "pos": pos, "gloss": {"en": en, "tr": tr}, "level": level}
    if root: e["root"] = root
    if plural: e["plural"] = plural
    if form: e["form"] = form
    return e
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
S = []

TITLE43 = {"ar": "التَّكْمِيلُ وَالتَّتْمِيمُ",
           "en": "Takmil and Tatmim — the Guard and the Topping",
           "tr": "Tekmîl ve Tetmîm — Siper ve Tamamlayış"}

# ----------- s1 — the takmil definition
S.append({"id": "s1", "translation": {
 "en": "TAKMIL — also called ihtiras, «taking guard» — is bringing, in speech that SUGGESTS the contrary of what is meant, that which repels it.",
 "tr": "TEKMÎL — ihtirâs, «sakınma» da denir — maksûdun zıddını AKLA GETİREN sözde, o zıddı def edeni getirmektir."},
 "tokens": [
  tok("التَّكْمِيلُ","takmil","noun",["takmil-wa-tatmim"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "«completion» — the sixth occasion, as mubtada.",
      "«tekmîl» — altıncı sebep; mübtedâ."),
  tok("أَنْ","an-nasiba","part",["takmil-wa-tatmim","an-masdariyya"],
      "مَصْدَرِيَّةٌ نَاصِبَةٌ.",
      "«that» — the masdar-maker: the definition rolls into one noun.",
      "«-mek» — masdariyye: tarif tek isme dürülür."),
  tok("يُؤْتَى","ata","verb",["takmil-wa-tatmim","naib-al-fail"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ — وَالْمَصْدَرُ خَبَرُ الْمُبْتَدَأِ.",
      "«there be brought» — the passive mudari, its nasb estimated on the maqsura.",
      "«getirilmek» — meçhûl muzâri; nasbı maksûre üzerinde takdîrî."),
  tok("فِي","fi","part",["takmil-wa-tatmim"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«içinde» —"),
  tok("كَلَامٍ","kalam","noun",["takmil-wa-tatmim"],
      "مَجْرُورٌ بِفِي.",
      "«speech» —",
      "«bir sözde» —"),
  tok("يُوهِمُ","awhama","verb",["takmil-wa-tatmim","form-iv-verbs","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ صِفَةٌ لِكَلَامٍ — وَهٰذَا الْقَيْدُ هُوَ الْفَرْقُ كُلُّهُ.",
      "«that suggests» — Form IV of وَهْم: makes the hearer imagine. This sifa is the whole hinge between the pair.",
      "«akla getiren» — وَهْم'in IV. bâbı: dinleyene tevehhüm ettirir. Bu sıfat, çiftin bütün menteşesidir."),
  tok("خِلَافَ","khilaf","noun",["takmil-wa-tatmim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«the contrary of» —",
      "«zıddını» —"),
  tok("الْمَقْصُودِ","maqsud","noun",["takmil-wa-tatmim","ism-maful"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«what is meant» —",
      "«maksûdun» —"),
  tok("بِمَا","ma-mawsula","part",["takmil-wa-tatmim","anwa-ma"],
      "الْبَاءُ جَارَّةٌ، وَمَا مَوْصُولَةٌ.",
      "«that which» —",
      "«def edeni» —",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","pron")]),
  tok("يَدْفَعُهُ","dafaa","verb",["takmil-wa-tatmim"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِلَةُ مَا.",
      "«repels it» — the guard-word's whole job in one sila.",
      "«def eder» — siper kelimesinin bütün işi tek sılada.",
      punct=".", segments=[seg("يَدْفَعُ","dafaa","verb"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("التَّكْمِيلُ أَنْ يُؤْتَى فِي كَلَامٍ يُوهِمُ خِلَافَ الْمَقْصُودِ بِمَا يَدْفَعُهُ",
    "جُمْلَةٌ اسْمِيَّةٌ — حَدُّ التَّكْمِيلِ (الِاحْتِرَاسِ).",
    "The definition: where the words could be read against you, post a guard.",
    "Tarif: sözün aleyhine okunabileceği yerde nöbetçi dik."),
  J("يُوهِمُ خِلَافَ الْمَقْصُودِ",
    "قَيْدُ الْبَابِ — بِهِ يَفْتَرِقُ التَّكْمِيلُ عَنِ التَّتْمِيمِ.",
    "Five words that split this chapter's pair.",
    "Bu bâbın çiftini ayıran beş kelime.")]})

# ----------- s2 — Tarafa, first hemistich: the mid-speech guard
S.append({"id": "s2", "translation": {
 "en": "So may they water your dwellings — WITHOUT RUINING THEM —",
 "tr": "Yurtlarını sulasın — ONLARI HARAP ETMEDEN —"},
 "tokens": [
  tok("فَسَقَى","saqa-water","verb",["takmil-wa-tatmim","naqis-verbs"],
      "الْفَاءُ بِحَسَبِ مَا قَبْلَهَا، وَسَقَى فِعْلٌ مَاضٍ — وَالْمُرَادُ الدُّعَاءُ.",
      "«so may … water» — a mazi worn as a prayer.",
      "«sulasın» — duâ kılığında mâzî.",
      segments=[seg("فَ","fa","part"), seg("سَقَى","saqa-water","verb")]),
  tok("دِيَارَكِ","dar","noun",["takmil-wa-tatmim"],
      "مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«your dwellings» — the beloved's abodes, object before its subject.",
      "«yurtlarını» — sevgilinin diyârı; mef'ûl, fâilinden önce.",
      segments=[seg("دِيَارَ","dar","noun"), seg("كِ","pron-2fs","pron")]),
  tok("غَيْرَ","ghayr","noun",["takmil-wa-tatmim","hal"],
      "حَالٌ مِنَ الْفَاعِلِ الْآتِي مَنْصُوبٌ وَهُوَ مُضَافٌ — وَهٰذَا هُوَ الِاحْتِرَاسُ.",
      "«without» — a hal thrown FORWARD of its subject: the guard posted mid-speech, before the rain is even named.",
      "«-meden» — fâilinden ÖNE atılmış hâl: nöbetçi, yağmur daha anılmadan söz ortasına dikilir."),
  tok("مُفْسِدِهَا","mufsid","noun",["takmil-wa-tatmim","ism-fail","form-iv-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَهَا مُضَافٌ إِلَيْهِ.",
      "«ruining them» — for a prayed-for rain can still drown: the contrary the takmil repels.",
      "«harap edici» — duâ edilen yağmur boğabilir de: tekmîlin def ettiği zıt budur.",
      punct="•", segments=[seg("مُفْسِدِ","mufsid","noun"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("فَسَقَى دِيَارَكِ غَيْرَ مُفْسِدِهَا",
    "الدُّعَاءُ وَحَالُهُ الْمُحْتَرِسَةُ — وَالْفَاعِلُ فِي الْعَجُزِ.",
    "The prayer with its guard already up, its subject still to come.",
    "Duâ, nöbetçisi çoktan dikilmiş; fâili henüz yolda."),
  J("غَيْرَ مُفْسِدِهَا",
    "الِاحْتِرَاسُ فِي وَسَطِ الْكَلَامِ.",
    "The takmil mid-speech: blessing, not flood.",
    "Söz ortasında tekmîl: bereket, sel değil.")]})

# ----------- s3 — Tarafa, second hemistich
S.append({"id": "s3", "translation": {
 "en": "— the spring rain, and a steady downpour streaming. (the source's own note: صَوْب is the spring's rain, دِيمَة the long soft rain.)",
 "tr": "— bahar yağmuru ve boşanan dâimî yağmur. (kaynağın kendi notu: صَوْب bahar yağmuru, دِيمَة uzun süren yumuşak yağmurdur.)"},
 "tokens": [
  tok("صَوْبُ","sawb","noun",["takmil-wa-tatmim"],
      "فَاعِلُ سَقَى الْمُؤَخَّرُ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the pouring of» — the delayed subject arrives.",
      "«yağışı» — ertelenmiş fâil gelir."),
  tok("الرَّبِيعِ","rabi","noun",["takmil-wa-tatmim"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the spring» —",
      "«baharın» —"),
  tok("وَدِيمَةٌ","dima","noun",["takmil-wa-tatmim","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَدِيمَةٌ مَعْطُوفٌ عَلَى صَوْبُ مَرْفُوعٌ.",
      "«and a steady rain» — the gentle kind that soaks and never smashes.",
      "«ve dâimî yağmur» — ıslatan ama yıkmayan cinsten.",
      segments=[seg("وَ","wa","part"), seg("دِيمَةٌ","dima","noun")]),
  tok("تَهْمِي","hamaa","verb",["takmil-wa-tatmim","naqis-verbs","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْجُمْلَةُ صِفَةٌ لِدِيمَةٌ.",
      "«streaming» — the naqis mudari of هَمَى, its damma hidden on the ya.",
      "«boşanan» — هَمَى'nın nâkıs muzârisi; dammesi yâda gizli.",
      punct="•")],
 "jumal": [
  J("صَوْبُ الرَّبِيعِ وَدِيمَةٌ تَهْمِي",
    "الْفَاعِلُ وَمَعْطُوفُهُ — عَجُزُ بَيْتِ طَرَفَةَ.",
    "The rains named at last — already sworn harmless.",
    "Nihayet adları konan yağmurlar — zararsızlıkları çoktan yeminli."),
  J("تَهْمِي",
    "صِفَةُ الدِّيمَةِ — الْمُضَارِعُ النَّاقِصُ التَّقْدِيرِيُّ.",
    "One taqdiri verb closing the bayt.",
    "Beyti kapatan tek takdîrî fiil.")]})

# ----------- s4 — Ma'ida 5:54: the takmil at speech's end
S.append({"id": "s4", "translation": {
 "en": "…humble toward the believers, MIGHTY AGAINST THE DISBELIEVERS (5:54). The guard stands at the speech's END: humility must not be read as weakness.",
 "tr": "…müminlere karşı alçak gönüllü, KÂFİRLERE KARŞI İZZETLİ (5:54). Nöbetçi sözün SONUNDA durur: tevazu, zaaf diye okunmasın."},
 "tokens": [
  tok("أَذِلَّةٍ","dhalil","noun",["takmil-wa-tatmim"],
      "صِفَةٌ لِقَوْمٍ فِي الْآيَةِ مَجْرُورَةٌ — جَمْعُ ذَلِيلٍ: هُنَا بِمَعْنَى الرِّفْقِ وَالتَّوَاضُعِ.",
      "«humble» — plural of ذَلِيل, here tenderness, not disgrace.",
      "«alçak gönüllü» — ذَلِيل'in cem'i; burada şefkat, zillet değil."),
  tok("عَلَى","ala","part",["takmil-wa-tatmim"],
      "حَرْفُ جَرٍّ.",
      "«toward» —",
      "«karşı» —"),
  tok("الْمُؤْمِنِينَ","mumin","noun",["takmil-wa-tatmim","jam-mudhakkar-salim"],
      "مَجْرُورٌ بِالْيَاءِ.",
      "«the believers» —",
      "«müminlere» —"),
  tok("أَعِزَّةٍ","aziz","noun",["takmil-wa-tatmim"],
      "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ — جَمْعُ عَزِيزٍ، وَهِيَ التَّكْمِيلُ.",
      "«mighty» — the second sifa IS the takmil: gentleness at home, iron at the gate.",
      "«izzetli» — ikinci sıfat tekmîlin tâ kendisi: içeride yumuşaklık, kapıda demir."),
  tok("عَلَى","ala","part",["takmil-wa-tatmim"],
      "حَرْفُ جَرٍّ.",
      "«against» —",
      "«karşı» —"),
  tok("الْكَافِرِينَ","kafir","noun",["takmil-wa-tatmim","jam-mudhakkar-salim"],
      "مَجْرُورٌ بِالْيَاءِ.",
      "«the disbelievers» —",
      "«kâfirlere» —",
      punct=".")],
 "jumal": [
  J("أَذِلَّةٍ عَلَى الْمُؤْمِنِينَ أَعِزَّةٍ عَلَى الْكَافِرِينَ",
    "صِفَتَانِ مُتَقَابِلَتَانِ — وَالثَّانِيَةُ تَكْمِيلٌ فِي آخِرِ الْكَلَامِ.",
    "The takmil at the end: without it, «humble» could shade into «weak».",
    "Sonda tekmîl: o olmasa «alçak gönüllü», «zayıf»a çalardı."),
  J("أَعِزَّةٍ عَلَى الْكَافِرِينَ",
    "دَفْعُ إِيهَامِ الضَّعْفِ.",
    "Four words repelling one dangerous misreading.",
    "Tek tehlikeli yanlış okumayı def eden dört kelime.")]})

# ----------- s5 — the tatmim definition
S.append({"id": "s5", "translation": {
 "en": "And TATMIM is bringing, in speech that does NOT suggest the contrary, a surplus word (fadla) for a point — such as mubalagha.",
 "tr": "TETMÎM ise, zıddı akla GETİRMEYEN sözde, bir nükte için — mübâlağa gibi — fazla bir kelime (fazla) getirmektir."},
 "tokens": [
  tok("وَالتَّتْمِيمُ","tatmim","noun",["takmil-wa-tatmim"],
      "الْوَاوُ عَاطِفَةٌ، وَالتَّتْمِيمُ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and completion-topping» — the seventh occasion, joined to the sixth.",
      "«ve tetmîm» — altıncıya bağlanan yedinci sebep.",
      segments=[seg("وَ","wa","part"), seg("التَّتْمِيمُ","tatmim","noun")]),
  tok("أَنْ","an-nasiba","part",["takmil-wa-tatmim","an-masdariyya"],
      "مَصْدَرِيَّةٌ نَاصِبَةٌ.",
      "«that» —",
      "«-mek» —"),
  tok("يُؤْتَى","ata","verb",["takmil-wa-tatmim","naib-al-fail"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ بِفَتْحَةٍ مُقَدَّرَةٍ.",
      "«there be brought» —",
      "«getirilmek» —"),
  tok("فِي","fi","part",["takmil-wa-tatmim"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«içinde» —"),
  tok("كَلَامٍ","kalam","noun",["takmil-wa-tatmim"],
      "مَجْرُورٌ بِفِي.",
      "«speech» —",
      "«bir sözde» —"),
  tok("لَا","la-nafiya","part",["takmil-wa-tatmim"],
      "نَافِيَةٌ — وَبِهٰذَا الْحَرْفِ الْوَاحِدِ افْتَرَقَ الْبَابَانِ.",
      "«not» — one letter, and the pair parts ways.",
      "«-meyen» — tek harf, ve çift yol ayrılır."),
  tok("يُوهِمُ","awhama","verb",["takmil-wa-tatmim","form-iv-verbs","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ صِفَةٌ لِكَلَامٍ.",
      "«suggests» —",
      "«akla getiren» —"),
  tok("خِلَافَ","khilaf","noun",["takmil-wa-tatmim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«the contrary of» —",
      "«zıddını» —"),
  tok("الْمَقْصُودِ","maqsud","noun",["takmil-wa-tatmim","ism-maful"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«what is meant» —",
      "«maksûdun» —"),
  tok("بِفَضْلَةٍ","fadla","noun",["takmil-wa-tatmim"],
      "جَارٌّ وَمَجْرُورٌ — وَالْفَضْلَةُ مَا يَتِمُّ الْكَلَامُ بِدُونِهِ.",
      "«a surplus word» — the nahw's own term: what the sentence stands without.",
      "«bir fazla» — nahvin öz terimi: cümlenin onsuz da ayakta durduğu şey.",
      segments=[seg("بِ","bi","part"), seg("فَضْلَةٍ","fadla","noun")]),
  tok("لِنُكْتَةٍ","nukta","noun",["takmil-wa-tatmim"],
      "جَارٌّ وَمَجْرُورٌ — لَا فَضْلَةَ بِلَا نُكْتَةٍ.",
      "«for a point» — no surplus without its earning.",
      "«bir nükte için» — kazançsız fazlalık yok.",
      segments=[seg("لِ","li","part"), seg("نُكْتَةٍ","nukta","noun")]),
  tok("كَالْمُبَالَغَةِ","mubalagha","noun",["takmil-wa-tatmim"],
      "الْكَافُ جَارَّةٌ لِلتَّمْثِيلِ، وَالْمُبَالَغَةُ مَجْرُورَةٌ.",
      "«such as mubalagha» — the worked example follows.",
      "«mübâlağa gibi» — işlenmiş örnek hemen gelir.",
      punct=".", segments=[seg("كَ","ka","part"), seg("الْمُبَالَغَةِ","mubalagha","noun")])],
 "jumal": [
  J("وَالتَّتْمِيمُ أَنْ يُؤْتَى فِي كَلَامٍ لَا يُوهِمُ خِلَافَ الْمَقْصُودِ بِفَضْلَةٍ لِنُكْتَةٍ",
    "حَدُّ التَّتْمِيمِ — يُفَارِقُ التَّكْمِيلَ بِلَا النَّافِيَةِ.",
    "The tatmim definition: the same frame as takmil, parted by one negating la.",
    "Tetmîm tarifi: tekmîlle aynı çerçeve; tek nefiy lâsıyla ayrılır."),
  J("بِفَضْلَةٍ لِنُكْتَةٍ",
    "الْفَضْلَةُ الْمَشْرُوطَةُ بِالنُّكْتَةِ.",
    "Surplus, licensed by its point.",
    "Nüktesiyle ruhsatlı fazlalık.")]})

# ----------- s6 — Insan 76:8: the tatmim witness
S.append({"id": "s6", "translation": {
 "en": "And they feed with food — DESPITE THEIR LOVE OF IT (76:8). Read the pronoun to the food, and عَلَى حُبِّهِ is the tatmim: giving away what you crave outweighs giving your surplus.",
 "tr": "Ve yemeği yedirirler — ONU SEVDİKLERİ HÂLDE (76:8). Zamir yemeğe gönderilirse عَلَى حُبِّهِ tetmîmdir: canının çektiğini vermek, artanı vermekten ağırdır."},
 "tokens": [
  tok("وَيُطْعِمُونَ","atama","verb",["takmil-wa-tatmim","form-iv-verbs","afal-khamsa"],
      "الْوَاوُ عَاطِفَةٌ، وَيُطْعِمُونَ فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«and they feed» — Form IV, the five-verbs raf'.",
      "«ve yedirirler» — IV. bâb; ef'âl-i hamse ref'i.",
      segments=[seg("وَ","wa","part"), seg("يُطْعِمُونَ","atama","verb")]),
  tok("الطَّعَامَ","taam","noun",["takmil-wa-tatmim"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the food» —",
      "«yemeği» —"),
  tok("عَلَى","ala","part",["takmil-wa-tatmim"],
      "حَرْفُ جَرٍّ — بِمَعْنَى مَعَ.",
      "«despite» — the ala of accompaniment.",
      "«rağmen» — maiyet mânâsında alâ."),
  tok("حُبِّهِ","hubb","noun",["takmil-wa-tatmim","hal"],
      "مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ لِلطَّعَامِ عَلَى هٰذَا الْوَجْهِ — وَالْجَارُّ حَالٌ: أَيْ مُحِبِّينَ لَهُ، وَهُوَ التَّتْمِيمُ لِلْمُبَالَغَةِ.",
      "«their love of it» — the jarr phrase as hal: they give while craving. The fadla that heaps the praise higher — tatmim.",
      "«onu severken» — hâl makamındaki câr-mecrûr: canları çekerken verirler. Övgüyü katlayan fazla — tetmîm.",
      punct=".", segments=[seg("حُبِّ","hubb","noun"), seg("هِ","pron-3ms","pron")])],
 "jumal": [
  J("وَيُطْعِمُونَ الطَّعَامَ عَلَى حُبِّهِ",
    "الْفِعْلُ وَمَفْعُولُهُ وَالْحَالُ الْمُتَمِّمَةُ.",
    "The sentence stands without the hal — and the praise stands taller with it.",
    "Cümle hâlsiz de ayakta — övgü onunla daha dik."),
  J("عَلَى حُبِّهِ",
    "الْفَضْلَةُ لِنُكْتَةِ الْمُبَالَغَةِ — شَاهِدُ التَّتْمِيمِ.",
    "The tatmim witness: no contrary lurked; the surplus only heaps.",
    "Tetmîm şahidi: pusuda zıt yoktu; fazla yalnız yığar.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "takmil": g("تَكْمِيل", "ك م ل", "noun", "takmil / ihtiras: the guarding surplus", "tekmîl / ihtirâs: siper fazlası", 6),
 "tatmim": g("تَتْمِيم", "ت م م", "noun", "tatmim: the point-bearing surplus", "tetmîm: nükteli fazla", 6),
 "awhama": g("أَوْهَمَ", "و ه م", "verb", "to make (someone) imagine, suggest falsely", "vehmettirmek, akla getirmek", 5, form="IV"),
 "dafaa": g("دَفَعَ", "د ف ع", "verb", "to repel, push away", "def etmek, itmek", 2, form="I"),
 "fadla": g("فَضْلَة", "ف ض ل", "noun", "surplus element (nahw: what the sentence stands without)", "fazla (nahiv: cümlenin onsuz durduğu öge)", 5),
 "nukta": g("نُكْتَة", "ن ك ت", "noun", "subtle point, earning", "nükte", 4, plural="نُكَت"),
 "mubalagha": g("مُبَالَغَة", "ب ل غ", "noun", "intensification, hyperbole", "mübâlağa", 4),
 "saqa-water": g("سَقَى", "س ق ي", "verb", "to water, give drink", "sulamak, su vermek", 3, form="I"),
 "sawb": g("صَوْب", "ص و ب", "noun", "downpour, the falling of rain", "yağış, boşanan yağmur", 5),
 "rabi": g("رَبِيع", "ر ب ع", "noun", "spring", "bahar, rebî'", 3),
 "dima": g("دِيمَة", "د و م", "noun", "long steady rain", "dâimî yumuşak yağmur", 5, plural="دِيَم"),
 "hamaa": g("هَمَى", "ه م ي", "verb", "to stream, pour down", "boşanmak, akmak", 5, form="I"),
 "dhalil": g("ذَلِيل", "ذ ل ل", "noun", "lowly; (5:54) tender, humble", "zelil; (5:54) yumuşak, alçak gönüllü", 4, plural="أَذِلَّة"),
 "hubb": g("حُبّ", "ح ب ب", "noun", "love; craving", "sevgi; iştah", 2),
 "maqsud": copy_gloss("mukhtasar-al-manar", "maqsud"),
 "aziz": copy_gloss("wasiyyat-abi-hanifa-l4", "aziz"),
 "atama": copy_gloss("kitab-al-kaffarat", "atama"),
 "taam": copy_gloss("wasiyyat-abi-hanifa-samti", "taam"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/43.json").write_text(
    json.dumps({"chapter": 43, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 43 for c in man["chapters"]):
    man["chapters"].append({"n": 43, "title": TITLE43})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.43.0"
ADD_EN = (" Chapter 43 carries takmil and tatmim (lines ~2870-2890, sahifa 99): s4 is "
          "al-Ma'ida 5:54 (part) and s6 al-Insan 76:8 (part), received Qur'anic text quoted "
          "exactly in standard imla as the source prints them; s2-s3 are Tarafa b. al-Abd's "
          "bayt as the source recites it, split at the hemistich; s1 and s5 are the "
          "musannif's definitions as the source recites them, per the package's definitional "
          "frame.")
ADD_TR = (" Kırk üçüncü bâb tekmîl ile tetmîmi taşır (satır ~2870-2890, sahife 99): s4 Mâide "
          "5:54 (kısmen), s6 İnsân 76:8 (kısmen) — kaynağın bastığı standart imlâ ile aynen "
          "alınmış mervî Kur'ân metni; s2-s3, Tarafe b. el-Abd'in beytidir — kaynağın "
          "okuduğu şekliyle, mısra başından bölünmüş; s1 ve s5, musannifin tarifleridir — "
          "paketin tarif çerçevesince.")
if "2870-2890" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "awhama" not in mo["verbs"]:
    # Form IV of a mithal-wawi root: أَوْهَمَ يُوهِمُ (the waw survives).
    mo["verbs"]["awhama"] = _sg.derived(
        _sg.B4, _sg.W4, "ُ", "أَوْهَم", "وهِم", "أَوْهِم",
        "إِيهَام", "مُوهِم", "مُوهَم", "أُوهِمَ", "يُوهَمُ")
if "dafaa" not in mo["verbs"]:
    mo["verbs"]["dafaa"] = _sg.sound1(
        "fataha", "دَفَع", "دْفَع", "اِدْفَع", "دَفْع", "دَافِع",
        "مَدْفُوع", "دُفِعَ", "يُدْفَعُ")
mo["verbs"].pop("saqa", None) if False else None
if "saqa-water" not in mo["verbs"]:
    # naqis yai of bab daraba — the مَضَى road: سَقَى يَسْقِي سَقْيًا.
    mo["verbs"]["saqa-water"] = _sg.naqis1(
        "daraba", "نَاقِصٌ يَائِيٌّ", "y", "سَقَ", "سْق", "i", "اِسْق",
        "سَقْي", "سَاقٍ (السَّاقِي)", "مَسْقِيّ", "سُقِيَ", "يُسْقَى",
        "نَاقِصٌ يَائِيٌّ: لَمْ يَسْقِ.")
if "hamaa" not in mo["verbs"]:
    mo["verbs"]["hamaa"] = _sg.naqis1(
        "daraba", "نَاقِصٌ يَائِيٌّ", "y", "هَمَ", "هْم", "i", "اِهْم",
        "هَمْي", "هَامٍ (الْهَامِي)", None, None, None,
        "نَاقِصٌ يَائِيٌّ لَازِمٌ: لَمْ يَهْمِ.")
if "atama" not in mo["verbs"]:
    src = json.loads((ROOT / "content/samples/kitab-al-kaffarat/morphology.json").read_text(encoding="utf-8"))
    mo["verbs"]["atama"] = src["verbs"]["atama"]
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 147
GR = ROOT / "content/grammar"
NOTE147 = {
 "id": "takmil-wa-tatmim",
 "title": {"ar": "التَّكْمِيلُ وَالتَّتْمِيمُ",
           "en": "Takmil and tatmim — the guard and the topping",
           "tr": "Tekmîl ve tetmîm — siper ve tamamlayış"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإطناب: التكميل والتتميم"],
 "question": {
  "en": ["Could the words be read AGAINST the meaning? Then the surplus that repels the misreading is TAKMIL (ihtiras) — mid-speech (غَيْرَ مُفْسِدِهَا) or at the end (أَعِزَّةٍ عَلَى الْكَافِرِينَ).",
         "No contrary lurks, and the surplus only heightens? That is TATMIM — a fadla for a point such as mubalagha (عَلَى حُبِّهِ).",
         "One hinge parts the pair: يُوهِمُ خِلَافَ الْمَقْصُودِ with or without لَا."],
  "tr": ["Kelimeler mânânın ALEYHİNE okunabilir mi? O yanlış okumayı def eden fazla TEKMÎLDİR (ihtirâs) — söz ortasında (غَيْرَ مُفْسِدِهَا) yahut sonunda (أَعِزَّةٍ عَلَى الْكَافِرِينَ).",
         "Pusuda zıt yok, fazla yalnız yükseltiyor mu? O TETMÎMDİR — mübâlağa gibi bir nükte için fazla (عَلَى حُبِّهِ).",
         "Çifti tek menteşe ayırır: يُوهِمُ خِلَافَ الْمَقْصُودِ — lâ ile yahut lâsız."]},
 "plain": {
  "en": "Two occasions in one minimal pair. TAKMIL (ihtiras): the speech could suggest the contrary — post a guard: rain prayed «WITHOUT RUINING» the dwellings; humility crowned «mighty against the disbelievers» (5:54). TATMIM: no contrary lurks; the surplus earns by a point — «they feed with food DESPITE LOVING IT» (76:8).",
  "tr": "Tek asgarî çiftte iki ıtnâb sebebi. TEKMÎL (ihtirâs): söz zıddı akla getirebilir; nöbetçi dik — Tarafe, sevgilinin yurduna yağmuru «HARAP ETMEDEN» diye duâ eder; 5:54 tevazuyu «kâfirlere karşı izzetli» ile taçlandırır. TETMÎM: pusuda zıt yok; fazla, nüktesiyle kazanır — «yemeği, SEVDİKLERİ HÂLDE yedirirler» (76:8).",},
 "explanation": {
  "en": "TAKMIL — the scholars also say IHTIRAS, «taking guard» — is defined أَنْ يُؤْتَى فِي كَلَامٍ يُوهِمُ خِلَافَ الْمَقْصُودِ بِمَا يَدْفَعُهُ: where the wording could plant the OPPOSITE of what you mean, bring what repels it. Its seat is free. MID-SPEECH: Tarafa's فَسَقَى دِيَارَكِ غَيْرَ مُفْسِدِهَا صَوْبُ الرَّبِيعِ وَدِيمَةٌ تَهْمِي — a prayer for rain could drown what it blesses, so «without ruining them» stands guard before the rains are even named (and the hal even precedes its own subject). AT THE END: أَذِلَّةٍ عَلَى الْمُؤْمِنِينَ أَعِزَّةٍ عَلَى الْكَافِرِينَ (5:54) — tenderness toward believers could read as softness of spine; the second sifa repels it. TATMIM is the same frame behind لَا: أَنْ يُؤْتَى فِي كَلَامٍ لَا يُوهِمُ خِلَافَ الْمَقْصُودِ بِفَضْلَةٍ لِنُكْتَةٍ كَالْمُبَالَغَةِ — no contrary threatens, and the surplus (a FADLA, the nahw's term for what the sentence stands without) earns by a point. وَيُطْعِمُونَ الطَّعَامَ عَلَى حُبِّهِ (76:8): on the reading that sends the pronoun to the FOOD, «despite their love of it» heaps the mubalagha — to give away what you crave is the harder, higher giving. The pair belongs beside ighal and tadhyil in one map of seats: ighal seals the END with any nukta; tadhyil follows with a confirming JUMLA; takmil/tatmim ride ANYWHERE as phrases, parted only by whether a misreading lurked.",
  "tr": "TEKMÎL — âlimler İHTİRÂS, «sakınma» da der — şöyle tarif edilir: أَنْ يُؤْتَى فِي كَلَامٍ يُوهِمُ خِلَافَ الْمَقْصُودِ بِمَا يَدْفَعُهُ — lafız, kastının ZIDDINI ekebilecekse, onu def edeni getir. Oturağı serbesttir. SÖZ ORTASINDA: Tarafe'nin فَسَقَى دِيَارَكِ غَيْرَ مُفْسِدِهَا صَوْبُ الرَّبِيعِ وَدِيمَةٌ تَهْمِي beyti — yağmur duâsı, bereketlediğini boğabilir; «harap etmeden», yağmurlar daha adlanmadan nöbete durur (hâl, fâilinden bile öncedir). SONDA: أَذِلَّةٍ عَلَى الْمُؤْمِنِينَ أَعِزَّةٍ عَلَى الْكَافِرِينَ (5:54) — müminlere yumuşaklık, omurga gevşekliği diye okunabilirdi; ikinci sıfat bunu def eder. TETMÎM, lâ'nın ardındaki aynı çerçevedir: أَنْ يُؤْتَى فِي كَلَامٍ لَا يُوهِمُ خِلَافَ الْمَقْصُودِ بِفَضْلَةٍ لِنُكْتَةٍ كَالْمُبَالَغَةِ — zıt tehdidi yok; fazla (FAZLA: nahvin, cümlenin onsuz durduğu öge terimi) nüktesiyle kazanır. وَيُطْعِمُونَ الطَّعَامَ عَلَى حُبِّهِ (76:8): zamiri YEMEĞE gönderen okuyuşta «onu severken» mübâlağayı yığar — canının çektiğini vermek, vermenin zoru ve yücesidir. Çift, îgāl ve tezyîlle tek oturak haritasına oturur: îgāl SONU herhangi bir nükteyle mühürler; tezyîl, pekiştiren bir CÜMLEYLE izler; tekmîl/tetmîm öbek olarak HER YERE biner — yalnız pusuda yanlış okuma var mıydı, onunla ayrılırlar.",},
 "examples": [
  {"ar": "فَسَقَى دِيَارَكِ غَيْرَ مُفْسِدِهَا",
   "en": "takmil mid-speech: blessing guarded from the flood-reading.",
   "tr": "söz ortasında tekmîl: bereket, sel okumasından korunur.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "أَعِزَّةٍ عَلَى الْكَافِرِينَ",
   "en": "takmil at the end: humility guarded from weakness (5:54).",
   "tr": "sonda tekmîl: tevazu, zaaftan korunur (5:54).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "وَيُطْعِمُونَ الطَّعَامَ عَلَى حُبِّهِ",
   "en": "tatmim: the fadla heaping the mubalagha (76:8).",
   "tr": "tetmîm: mübâlağayı yığan fazla (76:8).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«Tekmîl ile tetmîm aynı şeydir»",
   "right": "«Tekmîl bir yanlış okumayı DEF EDER; tetmîm, zıt tehdidi yokken nükte için EKLER»",
   "why": {"en": "The definitions differ by one لَا. Takmil's surplus is defensive — strike it and the speech can be read against you (rain that ruins, humility that is weakness). Tatmim's surplus is offensive — strike it and nothing misreads, but the praise stands a step lower.",
           "tr": "Tarifler tek lâ ile ayrılır. Tekmîlin fazlası savunmadır — sil, söz aleyhine okunabilir (harap eden yağmur, zaaf sanılan tevazu). Tetmîmin fazlası hücumdur — sil, hiçbir şey yanlış okunmaz; ama övgü bir basamak alçalır."}}],
 "relatedNotes": ["asbab-al-itnab", "ighal", "tadhyil", "hal", "an-masdariyya",
                  "naib-al-fail", "form-iv-verbs"]}

(GR / "takmil-wa-tatmim.json").write_text(
    json.dumps(NOTE147, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch43:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + awhama/dafaa/saqa/hamaa (+atama copied); note 147")
