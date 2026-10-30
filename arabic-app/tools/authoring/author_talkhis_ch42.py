# -*- coding: utf-8 -*-
"""Author chapter 42 of talkhis-al-miftah — التَّذْيِيلُ.

Sahifa 98-99 (lines ~2855-2870): the fifth occasion of itnab —
TADHYIL («adding a train»): following a jumla with another jumla that
contains its meaning, for emphasis. Two darbs:

  • NOT brought to proverb-hood (needs its neighbour): ذٰلِكَ
    جَزَيْنَاهُمْ بِمَا كَفَرُوا وَهَلْ نُجَازِي إِلَّا الْكَفُورَ
    (Saba 34:17, as the source prints the qira'a: نُجَازِي … الْكَفُورَ).
  • Brought to proverb-hood (stands alone): وَقُلْ جَاءَ الْحَقُّ
    وَزَهَقَ الْبَاطِلُ إِنَّ الْبَاطِلَ كَانَ زَهُوقًا (al-Isra 17:81).
  • And the tadhyil confirms the MANTUQ (what the wording says) or the
    MAFHUM (what is understood from it): the poet Ziyad's bayt
    وَلَسْتَ بِمُسْتَبْقٍ أَخًا لَا تَلُمُّهُ • عَلَى شَعَثٍ أَيُّ
    الرِّجَالِ الْمُهَذَّبُ — the seat's question confirms the
    hemistich's UNDERSTOOD sense: no friend is kept without pardon,
    for who among men is flawless?

ATTRIBUTION: s1-s2 are Saba 34:17 (part) and s3-s4 al-Isra 17:81
(part), received Qur'anic text quoted exactly in standard imla as the
source prints it (34:17's نُجَازِي…الْكَفُورَ follows the source's
printed qira'a); s5-s6 are the poet Ziyad's bayt as the source
recites it, split at the hemistich per the package's precedent.

Grammar this chapter teaches:
  • note 146 `tadhyil` — the definition verbatim, the two darbs, and
    the mantuq/mafhum split.
  • new paradigms: جَازَى (III naqis), كَفَرَ, زَهَقَ, لَمَّ (geminate).
  • لَيْسَ + the zaida ba on its khabar (بِمُسْتَبْقٍ — jarr in
    wording, nasb in place); the declining أَيُّ as mubtada.
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

TITLE42 = {"ar": "التَّذْيِيلُ",
           "en": "Tadhyil — the Confirming Train",
           "tr": "Tezyîl — Pekiştiren Kuyruk"}

# ----------- s1 — Saba 34:17a: the sentence the train will follow
S.append({"id": "s1", "translation": {
 "en": "Thus We repaid them for their disbelief — (34:17)",
 "tr": "İşte onları, küfürleri sebebiyle böyle cezalandırdık — (34:17)"},
 "tokens": [
  tok("ذٰلِكَ","dhalika","pron",["tadhyil","asma-al-ishara"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ — مَفْعُولٌ ثَانٍ مُقَدَّمٌ، وَقِيلَ مَفْعُولٌ مُطْلَقٌ: جَزَيْنَاهُمْ ذٰلِكَ الْجَزَاءَ.",
      "«thus» — the demonstrative fronted: THAT repayment, no other.",
      "«işte böyle» — öne alınmış işaret: O cezayı, başkasını değil."),
  tok("جَزَيْنَاهُمْ","jaza","verb",["tadhyil"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ، وَهُمْ مَفْعُولٌ أَوَّلُ.",
      "«We repaid them» — the naqis mazi with both its pronouns aboard.",
      "«onları cezalandırdık» — iki zamirini de taşıyan nâkıs mâzî.",
      segments=[seg("جَزَيْنَا","jaza","verb"), seg("هُمْ","pron-3mp","pron")]),
  tok("بِمَا","ma-mawsula","part",["tadhyil","anwa-ma"],
      "الْبَاءُ لِلسَّبَبِيَّةِ، وَمَا مَصْدَرِيَّةٌ.",
      "«for that» — the ba of cause over the masdar-maker ma.",
      "«sebebiyle» — sebep bâsı, masdariyye mâ üzerinde.",
      segments=[seg("بِ","bi","part"), seg("مَا","ma-mawsula","part")]),
  tok("كَفَرُوا","kafara","verb",["tadhyil"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ لِاتِّصَالِهِ بِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِالْبَاءِ: أَيْ بِكُفْرِهِمْ.",
      "«they disbelieved» — rolled up with ma into «their disbelief», the cause under the ba.",
      "«küfrettiler» — mâ ile dürülüp «küfürleri» olur: bânın altındaki sebep.",
      punct=".")],
 "jumal": [
  J("ذٰلِكَ جَزَيْنَاهُمْ بِمَا كَفَرُوا",
    "الْجُمْلَةُ الْأُولَى — وَسَيَتْبَعُهَا ذَيْلُهَا.",
    "The sentence a train is about to follow.",
    "Kuyruğunun izleyeceği cümle."),
  J("بِمَا كَفَرُوا",
    "الْبَاءُ السَّبَبِيَّةُ وَالْمَصْدَرُ الْمُؤَوَّلُ.",
    "Cause folded into two words.",
    "İki kelimeye dürülmüş sebep.")]})

# ----------- s2 — Saba 34:17b: darb 1 — the train that needs its neighbour
S.append({"id": "s2", "translation": {
 "en": "— and do We repay but the ingrate? The train (tadhyil) restates the sentence before it, but leans on it: the FIRST darb, not brought to proverb-hood.",
 "tr": "— biz nankörden başkasını mı cezalandırırız? Kuyruk (tezyîl) önceki cümleyi yeniden söyler, ama ona yaslanır: darb-ı mesel hâline getirilmemiş BİRİNCİ darb."},
 "tokens": [
  tok("وَهَلْ","hal-istifham","part",["tadhyil","khuruj-al-istifham"],
      "الْوَاوُ عَاطِفَةٌ، وَهَلْ حَرْفُ اسْتِفْهَامٍ خَرَجَ إِلَى النَّفْيِ.",
      "«and do…?» — a question worn as denial: We do NOT repay but…",
      "«ve … mı?» — nefiy kılığında soru: cezalandırmayız, ancak…",
      segments=[seg("وَ","wa","part"), seg("هَلْ","hal-istifham","part")]),
  tok("نُجَازِي","jazaa","verb",["tadhyil","form-iii-verbs","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْفَاعِلُ نَحْنُ.",
      "«do We repay» — Form III's naqis mudari, its damma estimated on the ya (the printed qira'a).",
      "«cezalandırır mıyız» — III. bâbın nâkıs muzârisi; dammesi yâ üzerinde takdîrî (basılı kıraat)."),
  tok("إِلَّا","illa","part",["tadhyil","istithna-mufarragh","qasr"],
      "أَدَاةُ حَصْرٍ — اسْتِثْنَاءٌ مُفَرَّغٌ.",
      "«but» — the emptied exception: only the ingrate.",
      "«ancak» — müferrağ istisnâ: yalnız nankör."),
  tok("الْكَفُورَ","kafur","noun",["tadhyil","sighat-mubalagha"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — فَعُولٌ لِلْمُبَالَغَةِ: الْمُوغِلُ فِي الْكُفْرَانِ.",
      "«the ingrate» — the فَعُول intensive: not one lapse, a habit of denial.",
      "«nankörü» — فَعُول mübâlağası: bir kere değil, huy edinilmiş nankörlük.",
      punct=".")],
 "jumal": [
  J("وَهَلْ نُجَازِي إِلَّا الْكَفُورَ",
    "التَّذْيِيلُ — ضَرْبٌ لَمْ يُجْعَلْ مَثَلًا: لَا يَسْتَقِلُّ عَمَّا قَبْلَهُ.",
    "The first darb: read alone, «do We repay but the ingrate?» still asks — repay WHAT? The train needs its engine.",
    "Birinci darb: tek başına okunsa «nankörden başkasını mı cezalandırırız?» yine sorar — NEYLE ceza? Kuyruk, lokomotifini ister."),
  J("إِلَّا الْكَفُورَ",
    "الْقَصْرُ فِي ذَيْلِ الْآيَةِ.",
    "The qasr pair inside the train.",
    "Kuyruğun içindeki kasr çifti.")]})

# ----------- s3 — Isra 17:81a
S.append({"id": "s3", "translation": {
 "en": "And say: truth has come, and falsehood has perished — (17:81)",
 "tr": "De ki: Hak geldi, bâtıl yok oldu — (17:81)"},
 "tokens": [
  tok("وَقُلْ","qala","verb",["tadhyil","imperative-amr","hollow-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَقُلْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ — حُذِفَتْ عَيْنُهُ الْأَجْوَفِيَّةُ، وَالْفَاعِلُ أَنْتَ.",
      "«and say» — the hollow amr, its middle letter gone.",
      "«ve de ki» — ecvef emri; orta harfi düşmüş.",
      segments=[seg("وَ","wa","part"), seg("قُلْ","qala","verb")]),
  tok("جَاءَ","jaa","verb",["tadhyil"],
      "فِعْلٌ مَاضٍ.",
      "«has come» —",
      "«geldi» —"),
  tok("الْحَقُّ","haqq","noun",["tadhyil"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«truth» —",
      "«hak» —"),
  tok("وَزَهَقَ","zahaqa","verb",["tadhyil"],
      "الْوَاوُ عَاطِفَةٌ، وَزَهَقَ فِعْلٌ مَاضٍ.",
      "«and has perished» — breathed its last, like a departing soul.",
      "«ve yok oldu» — can çıkar gibi çıktı.",
      segments=[seg("وَ","wa","part"), seg("زَهَقَ","zahaqa","verb")]),
  tok("الْبَاطِلُ","batil","noun",["tadhyil"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "«falsehood» —",
      "«bâtıl» —",
      punct=".")],
 "jumal": [
  J("جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ",
    "جُمْلَتَانِ مُتَعَاطِفَتَانِ — إِعْلَانُ مَكَّةَ يَوْمَ الْفَتْحِ.",
    "The proclamation recited at the smashing of the idols.",
    "Putlar devrilirken okunan ilan."),
  J("وَقُلْ",
    "الْأَمْرُ بِالْإِعْلَانِ.",
    "Truth is not only to happen; it is to be SAID.",
    "Hak yalnız olmaz; SÖYLENİR de.")]})

# ----------- s4 — Isra 17:81b: darb 2 — the train made a proverb
S.append({"id": "s4", "translation": {
 "en": "— truly falsehood was ever perishing (17:81). The SECOND darb: a train coined into a proverb — cut it loose and it still speaks.",
 "tr": "— şüphesiz bâtıl her zaman yok olucudur (17:81). İKİNCİ darb: darb-ı mesel hâline getirilmiş kuyruk — koparın, yine konuşur."},
 "tokens": [
  tok("إِنَّ","inna","part",["tadhyil","inna-wa-akhawatuha"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ.",
      "«truly» —",
      "«şüphesiz» —"),
  tok("الْبَاطِلَ","batil","noun",["tadhyil"],
      "اسْمُ إِنَّ مَنْصُوبٌ.",
      "«falsehood» —",
      "«bâtıl» —"),
  tok("كَانَ","kana","verb",["tadhyil","kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهَا هُوَ — وَكَانَ هُنَا لِلدَّوَامِ.",
      "«was ever» — kana of standing habit: always was, always will be.",
      "«her zaman» — devam kânesi: hep öyleydi, hep öyle olacak."),
  tok("زَهُوقًا","zahuq","noun",["tadhyil","sighat-mubalagha","kana-wa-akhawatuha"],
      "خَبَرُ كَانَ مَنْصُوبٌ — فَعُولٌ لِلْمُبَالَغَةِ: شَأْنُهُ الزُّهُوقُ.",
      "«ever-perishing» — the فَعُول mould again: perishing is falsehood's very nature.",
      "«yok olucu» — yine فَعُول kalıbı: yok olmak, bâtılın tabiatıdır.",
      punct=".")],
 "jumal": [
  J("إِنَّ الْبَاطِلَ كَانَ زَهُوقًا",
    "التَّذْيِيلُ الْجَارِي مَجْرَى الْمَثَلِ — يَسْتَقِلُّ بِنَفْسِهِ.",
    "The second darb: lift it out of the aya and it is a complete proverb, quotable at any grave of any falsehood.",
    "İkinci darb: âyetten çıkarın, başlı başına bir meseldir — her bâtılın her mezarında okunur."),
  J("زَهُوقًا",
    "صِيغَةُ الْمُبَالَغَةِ فِي مَقْعَدِ الْخَبَرِ.",
    "One intensive word carrying the whole verdict.",
    "Bütün hükmü taşıyan tek mübâlağa kalıbı.")]})

# ----------- s5 — Ziyad's bayt, first hemistich
S.append({"id": "s5", "translation": {
 "en": "You will keep no brother whose disarray you never gather —",
 "tr": "Dağınıklığını toparlamadığın hiçbir kardeşi tutamazsın —"},
 "tokens": [
  tok("وَلَسْتَ","laysa","verb",["tadhyil","kana-wa-akhawatuha"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَلَيْسَ فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ، وَالتَّاءُ اسْمُهَا.",
      "«you are not» — the jamid laysa with its ta as ism.",
      "«değilsin» — câmid leyse; tâsı ismidir.",
      segments=[seg("وَ","wa","part"), seg("لَسْتَ","laysa","verb")]),
  tok("بِمُسْتَبْقٍ","mustabqin","noun",["tadhyil","ism-maqsur-manqus","form-x-verbs","ism-fail"],
      "الْبَاءُ زَائِدَةٌ لِلتَّوْكِيدِ، وَمُسْتَبْقٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — مَنْقُوصٌ مِنِ اسْتَبْقَى.",
      "«keeping» — laysa's khabar under the EXTRA ba: jarr in wording, nasb in place; the Form X manqus.",
      "«tutucu» — ZÂİD bâ altında leysenin haberi: lafzan mecrur, mahallen mensub; X. bâbın mankusu."),
  tok("أَخًا","akh","noun",["tadhyil","five-nouns"],
      "مَفْعُولٌ بِهِ لِمُسْتَبْقٍ مَنْصُوبٌ — وَهُوَ هُنَا مُفْرَدٌ مُنَوَّنٌ لَا مِنَ الْأَسْمَاءِ الْخَمْسَةِ.",
      "«a brother» — the ism fa'il governs its object; and أَخ here is bare and tanwined, off the five-nouns rail.",
      "«bir kardeşi» — ism-i fâil mef'ûlünü amel eder; أَخ burada yalın ve tenvinli, beş isim rayının dışında."),
  tok("لَا","la-nafiya","part",["tadhyil"],
      "نَافِيَةٌ.",
      "«never» —",
      "«-madığın» —"),
  tok("تَلُمُّهُ","lamma-verb","verb",["tadhyil","doubled-verbs","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ أَنْتَ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ صِفَةٌ لِأَخًا: لَا تَلُمُّ شَعَثَهُ.",
      "«you gather» — the geminate لَمَّ: to gather what scattered — a friend's faults forgiven, his disarray set right.",
      "«toparlarsın» — muzâaf لَمَّ: dağılanı derlemek — dostun kusurunu bağışlamak, dağınığını düzeltmek.",
      punct="•", segments=[seg("تَلُمُّ","lamma-verb","verb"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("وَلَسْتَ بِمُسْتَبْقٍ أَخًا لَا تَلُمُّهُ",
    "لَيْسَ وَخَبَرُهَا الْمَجْرُورُ بِالْبَاءِ الزَّائِدَةِ — صَدْرُ الْبَيْتِ.",
    "The claim: keep no friend you will not pardon.",
    "Dava: bağışlamayacağın dostu tutamazsın."),
  J("بِمُسْتَبْقٍ",
    "الْبَاءُ الزَّائِدَةُ عَلَى خَبَرِ لَيْسَ — جَرٌّ فِي اللَّفْظِ وَنَصْبٌ فِي الْمَحَلِّ.",
    "The classic zaida ba: two i'rabs on one word, both true.",
    "Klasik zâid bâ: tek kelimede iki i'râb, ikisi de doğru.")]})

# ----------- s6 — the second hemistich: the mafhum-confirming tadhyil
S.append({"id": "s6", "translation": {
 "en": "— over some disarray: WHICH of men is flawless? (the tadhyil confirming the UNDERSTOOD sense: pardon, for perfection is nowhere.)",
 "tr": "— bir dağınıklık yüzünden: insanların HANGİSİ kusursuz ki? (MEFHÛMU pekiştiren tezyîl: bağışla, çünkü kusursuzluk hiçbir yerde yok.)"},
 "tokens": [
  tok("عَلَى","ala","part",["tadhyil"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِتَلُمُّ.",
      "«over» —",
      "«yüzünden» —"),
  tok("شَعَثٍ","shaath","noun",["tadhyil"],
      "مَجْرُورٌ بِعَلَى — التَّفَرُّقُ وَالِاخْتِلَالُ.",
      "«disarray» — the scattering every friendship must forgive.",
      "«dağınıklık» — her dostluğun bağışlaması gereken dağılma."),
  tok("أَيُّ","ayy","pron",["tadhyil","khuruj-al-istifham"],
      "اسْمُ اسْتِفْهَامٍ مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ وَهُوَ مُضَافٌ — الْمُعْرَبُ الْوَحِيدُ مِنْ بَابِهِ، وَالِاسْتِفْهَامُ إِنْكَارِيٌّ.",
      "«which» — the one interrogative that DECLINES, here as mubtada; and the question denies: none is.",
      "«hangisi» — soru isimlerinin tek MU'REBİ; mübtedâ. Ve soru inkârîdir: hiçbiri değil."),
  tok("الرِّجَالِ","rajul","noun",["tadhyil"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«of men» —",
      "«insanların» —"),
  tok("الْمُهَذَّبُ","muhadhdhab","noun",["tadhyil","ism-maful","form-ii-verbs"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ هَذَّبَ. وَالْجُمْلَةُ تَذْيِيلٌ يُقَرِّرُ مَفْهُومَ الصَّدْرِ.",
      "«the flawless one» — the ism maf'ul of هَذَّبَ; and the whole question is the train, confirming what the first hemistich left UNDERSTOOD.",
      "«kusursuz» — هَذَّبَ'nin ism-i mef'ûlü; ve bütün soru kuyruktur: ilk mısraın ANLAŞILANINI pekiştirir.",
      punct="•")],
 "jumal": [
  J("أَيُّ الرِّجَالِ الْمُهَذَّبُ",
    "التَّذْيِيلُ الْمُقَرِّرُ لِلْمَفْهُومِ — جَارٍ مَجْرَى الْمَثَلِ.",
    "The mafhum-confirming train — itself coined into a proverb the Arabs still quote.",
    "Mefhûmu pekiştiren kuyruk — kendisi de Arapların hâlâ andığı bir mesel olmuştur."),
  J("أَيُّ",
    "الْمُعْرَبُ الْوَحِيدُ بَيْنَ أَسْمَاءِ الِاسْتِفْهَامِ.",
    "Chapter 26's declining ayy, earning its damma in verse.",
    "26. bâbın mu'reb أَيّ'ı, dammesini şiirde kazanır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "jazaa": g("جَازَى", "ج ز ي", "verb", "to repay, requite", "cezalandırmak, karşılığını vermek", 4, form="III"),
 "kafara": g("كَفَرَ", "ك ف ر", "verb", "to disbelieve; to be ungrateful", "küfretmek, inkâr etmek; nankörlük etmek", 2, form="I"),
 "kafur": g("كَفُور", "ك ف ر", "noun", "deeply ungrateful, ingrate (intensive فَعُول)", "çok nankör (mübâlağa فَعُول)", 4),
 "zahaqa": g("زَهَقَ", "ز ه ق", "verb", "to perish, vanish (of a soul: to depart)", "yok olmak, zâil olmak (can: çıkmak)", 4, form="I"),
 "zahuq": g("زَهُوق", "ز ه ق", "noun", "ever-perishing (intensive فَعُول)", "her zaman yok olucu (mübâlağa فَعُول)", 4),
 "mustabqin": g("مُسْتَبْقٍ", "ب ق ي", "noun", "one who keeps, retains (ism fa'il of اِسْتَبْقَى, manqus)", "tutan, alıkoyan (اِسْتَبْقَى'nın ism-i fâili; mankus)", 5),
 "lamma-verb": g("لَمَّ", "ل م م", "verb", "to gather up (scattered things; a friend's faults)", "toparlamak, derlemek (dağınığı; dostun kusurunu)", 4, form="I"),
 "shaath": g("شَعَث", "ش ع ث", "noun", "disarray, dishevelment", "dağınıklık, perişanlık", 5),
 "muhadhdhab": g("مُهَذَّب", "ه ذ ب", "noun", "refined, flawless (ism maf'ul of هَذَّبَ)", "kusursuz, arınmış (هَذَّبَ'nin ism-i mef'ûlü)", 4),
 "haqq": copy_gloss("wasiyyat-abi-hanifa-samti", "haqq"),
 "batil": g("بَاطِل", "ب ط ل", "noun", "falsehood, the void", "bâtıl", 2),
 "jaza": copy_gloss("bad-al-amali", "jaza"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/42.json").write_text(
    json.dumps({"chapter": 42, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 42 for c in man["chapters"]):
    man["chapters"].append({"n": 42, "title": TITLE42})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.42.0"
ADD_EN = (" Chapter 42 carries tadhyil (lines ~2855-2870, sahifa 98-99): s1-s2 are Saba 34:17 "
          "(part; the printed qira'a نُجَازِي…الْكَفُورَ followed exactly) and s3-s4 al-Isra "
          "17:81 (part), received Qur'anic text quoted exactly in standard imla as the source "
          "prints them; s5-s6 are the poet Ziyad's bayt as the source recites it, split at "
          "the hemistich per the package's precedent.")
ADD_TR = (" Kırk ikinci bâb tezyîli taşır (satır ~2855-2870, sahife 98-99): s1-s2 Sebe' 34:17 "
          "(kısmen; basılı kıraat نُجَازِي…الْكَفُورَ aynen izlenmiştir), s3-s4 İsrâ 17:81 "
          "(kısmen) — kaynağın bastığı standart imlâ ile aynen alınmış mervî Kur'ân metni; "
          "s5-s6, şair Ziyâd'ın beytidir — kaynağın okuduğu şekliyle, paketin teâmülünce "
          "mısra başından bölünmüştür.")
if "2855-2870" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "jaza" not in mo["verbs"]:
    src = json.loads((ROOT / "content/samples/bad-al-amali/morphology.json").read_text(encoding="utf-8"))
    mo["verbs"]["jaza"] = src["verbs"]["jaza"]
if "jazaa" not in mo["verbs"]:
    # Form III naqis on the وَالَى road: جَازَى يُجَازِي مُجَازَاةً.
    mo["verbs"]["jazaa"] = _sg.derived_naqis(
        _sg.B3, _sg.W3, "ُ", "جَازَ", "جَاز", "i", "جَاز",
        "مُجَازَاة", "مُجَازٍ", "مُجَازًى", "جُوزِيَ", "يُجَازَى")
if "kafara" not in mo["verbs"]:
    mo["verbs"]["kafara"] = _sg.sound1(
        "nasara", "كَفَر", "كْفُر", "اُكْفُر", "كُفْر", "كَافِر",
        "مَكْفُور", "كُفِرَ", "يُكْفَرُ")
if "zahaqa" not in mo["verbs"]:
    mo["verbs"]["zahaqa"] = _sg.sound1(
        "fataha", "زَهَق", "زْهَق", "اِزْهَق", "زُهُوق", "زَاهِق")
if "lamma-verb" not in mo["verbs"]:
    # Form I geminate of bab nasara on the ظَنَّ road — sound lam, so only
    # the seams contract; idgham() is the standing convention.
    mo["verbs"]["lamma-verb"] = _sg.idgham(_sg.entry(
        "مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
        "لَمّ", "لَامّ",
        _sg.mazi14("لَمّ", "لَمَم"),
        _sg.mudari14("َ", "لُمّ", "لْمُم"),
        ["لُمَّ", "لُمَّا", "لُمُّوا", "لُمِّي", "لُمَّا", "اُلْمُمْنَ"],
        "يَلُمَّ", "يَلُمَّ", "تَلُمَّ",
        "مَلْمُوم", "لُمَّ", "يُلَمُّ",
        "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَلُمَّ، وَيَجُوزُ لَمْ يَلْمُمْ."))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 146
GR = ROOT / "content/grammar"
NOTE146 = {
 "id": "tadhyil",
 "title": {"ar": "التَّذْيِيلُ",
           "en": "Tadhyil — the confirming train",
           "tr": "Tezyîl — pekiştiren kuyruk"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإطناب: التذييل"],
 "question": {
  "en": ["Does a second jumla follow the first, CONTAINING its meaning, for emphasis? That is tadhyil: تَعْقِيبُ الْجُمْلَةِ بِجُمْلَةٍ تَشْتَمِلُ عَلَى مَعْنَاهَا لِلتَّوْكِيدِ.",
         "Can the train stand alone as a proverb? Then it is the second darb (إِنَّ الْبَاطِلَ كَانَ زَهُوقًا); if it leans on its neighbour, the first (وَهَلْ نُجَازِي إِلَّا الْكَفُورَ).",
         "What does it confirm — the MANTUQ (what the wording says) or the MAFHUM (what is understood)? The bayt's أَيُّ الرِّجَالِ الْمُهَذَّبُ confirms the understood."],
  "tr": ["İlk cümleyi, mânâsını İÇEREN ikinci bir cümle te'kid için mi izliyor? Tezyîl budur: تَعْقِيبُ الْجُمْلَةِ بِجُمْلَةٍ تَشْتَمِلُ عَلَى مَعْنَاهَا لِلتَّوْكِيدِ.",
         "Kuyruk tek başına mesel olabiliyor mu? İkinci darbdır (إِنَّ الْبَاطِلَ كَانَ زَهُوقًا); komşusuna yaslanıyorsa birincidir (وَهَلْ نُجَازِي إِلَّا الْكَفُورَ).",
         "Neyi pekiştirir — MANTÛKU (lafzın dediğini) mu, MEFHÛMU (anlaşılanı) mu? Beytin أَيُّ الرِّجَالِ الْمُهَذَّبُ'u anlaşılanı pekiştirir."]},
 "plain": {
  "en": "The fifth occasion of itnab: follow the sentence with a train carrying the same meaning again, for emphasis. Two darbs: a train coined into a proverb stands alone (17:81); one not so coined leans on its engine (34:17). And the train confirms either the wording or the understood sense.",
  "tr": "Itnâbın beşinci sebebi: cümleyi, aynı mânâyı yeniden taşıyan bir kuyrukla izle — te'kid için. İki darb: mesel hâline gelen kuyruk tek başına durur (17:81'in «bâtıl hep yok olucudur»u); gelmeyen, lokomotifine yaslanır (34:17'nin «nankörden başkasını mı cezalandırırız?»ı). Ve kuyruk ya lafzı ya anlaşılanı pekiştirir."},
 "explanation": {
  "en": "TADHYIL is defined as تَعْقِيبُ الْجُمْلَةِ بِجُمْلَةٍ تَشْتَمِلُ عَلَى مَعْنَاهَا لِلتَّوْكِيدِ — following a jumla with a jumla that embraces its meaning, to confirm it. Its DARBS are two. (1) NOT brought to proverb-hood: ذٰلِكَ جَزَيْنَاهُمْ بِمَا كَفَرُوا وَهَلْ نُجَازِي إِلَّا الْكَفُورَ (34:17, in the source's printed qira'a) — the rhetorical question re-says the repayment, but torn from its neighbour it dangles: repay what? (2) BROUGHT to proverb-hood, standing alone: وَقُلْ جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ إِنَّ الْبَاطِلَ كَانَ زَهُوقًا (17:81) — the sealing jumla is a coin struck once and spent everywhere. Further, the tadhyil confirms the MANTUQ — the wording's own statement — or the MAFHUM, what the wording leaves understood: in Ziyad's bayt وَلَسْتَ بِمُسْتَبْقٍ أَخًا لَا تَلُمُّهُ عَلَى شَعَثٍ أَيُّ الرِّجَالِ الْمُهَذَّبُ, the seat's question («which of men is flawless?») does not restate the words but grounds their UNDERSTOOD claim: pardon your friend's disarray, for a flawless friend exists nowhere. Tadhyil differs from IGHAL by seat and scope: ighal is any point-bearing seal (even a phrase) at the END; tadhyil is a whole JUMLA, and its point is always TA'KID.",
  "tr": "TEZYÎL şöyle tarif edilir: تَعْقِيبُ الْجُمْلَةِ بِجُمْلَةٍ تَشْتَمِلُ عَلَى مَعْنَاهَا لِلتَّوْكِيدِ — cümleyi, mânâsını kuşatan bir cümleyle izlemek, pekiştirmek için. DARBLARI ikidir. (1) Mesel hâline GETİRİLMEMİŞ: ذٰلِكَ جَزَيْنَاهُمْ بِمَا كَفَرُوا وَهَلْ نُجَازِي إِلَّا الْكَفُورَ (34:17, kaynağın basılı kıraatiyle) — inkârî soru cezayı yeniden söyler; ama komşusundan koparılsa asılı kalır: neyle ceza? (2) Mesel hâline GETİRİLMİŞ, tek başına duran: وَقُلْ جَاءَ الْحَقُّ وَزَهَقَ الْبَاطِلُ إِنَّ الْبَاطِلَ كَانَ زَهُوقًا (17:81) — mühür cümlesi bir kez basılıp her yerde harcanan sikkedir. Ayrıca tezyîl ya MANTÛKU — lafzın kendi dediğini — ya MEFHÛMU pekiştirir: Ziyâd'ın وَلَسْتَ بِمُسْتَبْقٍ أَخًا لَا تَلُمُّهُ عَلَى شَعَثٍ أَيُّ الرِّجَالِ الْمُهَذَّبُ beytinde oturaktaki soru («insanların hangisi kusursuz?») kelimeleri yinelemez; ANLAŞILAN davayı temellendirir: dostunun dağınığını bağışla, çünkü kusursuz dost hiçbir yerde yok. Tezyîl, ÎGĀLDEN oturak ve kapsamca ayrılır: îgāl sondaki her nükteli mühürdür (bir öbek bile olur); tezyîl bütün bir CÜMLEDİR ve nüktesi dâima TE'KİDDİR.",},
 "examples": [
  {"ar": "وَهَلْ نُجَازِي إِلَّا الْكَفُورَ",
   "en": "darb 1 — the train that leans on its neighbour (34:17).",
   "tr": "1. darb — komşusuna yaslanan kuyruk (34:17).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "إِنَّ الْبَاطِلَ كَانَ زَهُوقًا",
   "en": "darb 2 — the train coined into a proverb (17:81).",
   "tr": "2. darb — mesel olmuş kuyruk (17:81).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "أَيُّ الرِّجَالِ الْمُهَذَّبُ",
   "en": "the mafhum-confirming tadhyil, in Ziyad's bayt.",
   "tr": "mefhûmu pekiştiren tezyîl, Ziyâd'ın beytinde.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«Tezyîl ile îgāl aynı şeydir — ikisi de sona gelen fazlalıktır»",
   "right": "«Îgāl sondaki her nükteli mühürdür; tezyîl bütün bir cümledir ve nüktesi dâima te'kiddir»",
   "why": {"en": "Both live near the seat of the speech, but ighal's licence is ANY nukta (mubalagha, tahqiq, urging) and a mere phrase can carry it; tadhyil's licence is confirmation alone, and nothing short of a full jumla — one that could even be minted into a proverb — counts.",
           "tr": "İkisi de sözün oturağına yakın yaşar; ama îgālin ruhsatı HERHANGİ bir nüktedir (mübâlağa, tahkîk, teşvik) ve bir öbek bile taşır; tezyîlin ruhsatı yalnız te'kiddir ve tam bir cümleden azı — hattâ mesel diye basılabilecek bir cümleden azı — sayılmaz."}}],
 "relatedNotes": ["asbab-al-itnab", "ighal", "khuruj-al-istifham", "istithna-mufarragh",
                  "sighat-mubalagha", "kana-wa-akhawatuha", "ism-maqsur-manqus"]}

(GR / "tadhyil.json").write_text(
    json.dumps(NOTE146, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch42:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + jazaa/kafara/zahaqa/lamma (+jaza copied); note 146")
