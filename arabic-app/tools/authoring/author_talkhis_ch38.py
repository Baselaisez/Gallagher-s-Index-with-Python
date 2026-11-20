# -*- coding: utf-8 -*-
"""Author chapter 38 of talkhis-al-miftah — الْإِيجَازُ وَالْإِطْنَابُ وَالْمُسَاوَاةُ.

Sahifa 91-93 (lines ~2640-2700): the maani's next bab opens — the three
ACCEPTED roads of saying what is meant, by the musannif's own tahqiq
(Sakkaki ties ijaz and itnab to the middling speaker's customary
expression and calls them relative; the musannif answers that
relativity does not bar definition):

  • الْإِيجَازُ: تَأْدِيَةُ أَصْلِ الْمُرَادِ بِلَفْظٍ نَاقِصٍ عَنْهُ
    وَافٍ بِأَدَاءِ الْمُرَادِ — «وَافٍ» guards against IKHLAL (the
    too-short speech that fails the meaning).
  • الْإِطْنَابُ: … بِلَفْظٍ زَائِدٍ عَلَيْهِ لِفَائِدَةٍ —
    «لِفَائِدَةٍ» guards against TATWIL and HASHW.
  • الْمُسَاوَاةُ: … بِلَفْظٍ مُسَاوٍ لَهُ.
  Witnesses: musawat in وَلَا يَحِيقُ الْمَكْرُ السَّيِّئُ إِلَّا
  بِأَهْلِهِ (Fatir 35:43 — riding a mufarragh qasr), and ijaz al-qasr
  in وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ (al-Baqara 2:179), whose seven
  superiorities over the Arabs' own أَلْقَتْلُ أَنْفَى لِلْقَتْلِ the
  note recounts.

ATTRIBUTION: s4 is Fatir 35:43 (part) and s5 al-Baqara 2:179 (part),
received Qur'anic text quoted exactly in standard imla as the source
prints them; s1-s3 are the musannif's definitions as the source recites
them, each opened with its term as mubtada (the definitional frame this
package has used since chapter 1).

Grammar this chapter teaches:
  • note 142 `ijaz-itnab-musawat` — the three accepted and three
    rejected roads, the Sakkaki/musannif khilaf, and 2:179's
    superiorities.
  • وَافٍ in real text: the indefinite manqus whose ya is dropped and
    whose tanwin is the IWAD (the مَعَانٍ doctrine at last anchored in
    a story).
  • new paradigm: حَاقَ يَحِيقُ (hollow ya, lazim).
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

TITLE38 = {"ar": "الْإِيجَازُ وَالْإِطْنَابُ وَالْمُسَاوَاةُ",
           "en": "Brevity, Amplification, and the Even Measure",
           "tr": "Îcâz, Itnâb ve Müsâvât"}

# ----------------------------- s1 — the ijaz definition, with its two guards
S.append({"id": "s1", "translation": {
 "en": "IJAZ is conveying the intended meaning's core by wording LESS than it — yet sufficient to deliver it. («sufficient» bars ikhlal: brevity that starves the meaning is no virtue.)",
 "tr": "ÎCÂZ, murâdın aslını ondan DAHA AZ — fakat murâdı edâya YETER — bir lafızla getirmektir. («yeter» kaydı ihlâli dışarır: mânâyı aç bırakan kısalık fazilet değildir.)"},
 "tokens": [
  tok("الْإِيجَازُ","ijaz","noun",["ijaz-itnab-musawat"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«brevity» — the bab's first term, as mubtada.",
      "«îcâz» — bâbın ilk terimi; mübtedâ."),
  tok("تَأْدِيَةُ","tadiya-ada","noun",["ijaz-itnab-musawat"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«conveying» — the khabar, a mudaf: the masdar of أَدَّى.",
      "«getirmek» — haber; muzâf: أَدَّى'nın masdarı."),
  tok("أَصْلِ","asl","noun",["ijaz-itnab-musawat","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the core of» — the chain's middle link.",
      "«aslını» — zincirin orta halkası."),
  tok("الْمُرَادِ","murad","noun",["ijaz-itnab-musawat"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the intended» — the chain closes.",
      "«murâdın» — zincir kapanır."),
  tok("بِلَفْظٍ","lafz","noun",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِتَأْدِيَةُ.",
      "«by wording» — the instrument, hanging on the masdar.",
      "«bir lafızla» — masdara taalluk eden vasıta.",
      segments=[seg("بِ","bi","part"), seg("لَفْظٍ","lafz","noun")]),
  tok("نَاقِصٍ","naqis","noun",["ijaz-itnab-musawat","ism-fail"],
      "صِفَةٌ أُولَى لِلَفْظٍ مَجْرُورَةٌ.",
      "«less» — the first sifa on the wording: fewer words than the meaning's own measure.",
      "«daha az» — lafzın ilk sıfatı: mânânın kendi ölçüsünden az söz."),
  tok("عَنْهُ","an","part",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِنَاقِصٍ.",
      "«than it» — less THAN the meaning's measure.",
      "«ondan» — mânânın ölçüsünden az.",
      segments=[seg("عَنْ","an","part"), seg("هُ","pron-3ms","pron")]),
  tok("وَافٍ","wafin","noun",["ijaz-itnab-musawat","ism-maqsur-manqus"],
      "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ، وَالتَّنْوِينُ عِوَضٌ عَنْهَا.",
      "«sufficient» — the second sifa, and the INDEFINITE MANQUS in the flesh: its ya is dropped, its kasra estimated on the absent letter, and the tanwin standing in the gap is the tanwin of COMPENSATION.",
      "«yeter» — ikinci sıfat ve NEKRE MANKUS bizzat: yâsı düşmüş, kesresi yok harf üzerinde takdîrî, boşluktaki tenvin İVAZ tenvinidir."),
  tok("بِأَدَاءِ","adaa","noun",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِوَافٍ، وَهُوَ مُضَافٌ.",
      "«to the delivery of» — hanging on «sufficient»: sufficient FOR delivering.",
      "«edâsına» — «yeter»e taalluk eder: edâya yeter.",
      segments=[seg("بِ","bi","part"), seg("أَدَاءِ","adaa","noun")]),
  tok("الْمُرَادِ","murad","noun",["ijaz-itnab-musawat"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the meaning» — what must still arrive whole.",
      "«murâdın» — yine de bütün varması gereken şey.",
      punct=".")],
 "jumal": [
  J("الْإِيجَازُ تَأْدِيَةُ أَصْلِ الْمُرَادِ بِلَفْظٍ نَاقِصٍ عَنْهُ وَافٍ بِأَدَاءِ الْمُرَادِ",
    "جُمْلَةٌ اسْمِيَّةٌ — حَدُّ الْإِيجَازِ عِنْدَ الْمُصَنِّفِ.",
    "The musannif's definition — offered where Sakkaki declined to define, holding ijaz merely relative to the middling speaker's custom.",
    "Musannifin tarifi — Sekkâkî'nin tarif etmekten kaçındığı yerde: o, îcâzı orta konuşanın örfüne nispetle görmüştü."),
  J("نَاقِصٍ عَنْهُ وَافٍ بِأَدَاءِ الْمُرَادِ",
    "صِفَتَانِ مُتَعَاقِبَتَانِ — الثَّانِيَةُ احْتِرَازٌ عَنِ الْإِخْلَالِ.",
    "Two sifas in file: LESS, yet SUFFICIENT — the second word is the guard, for brevity that fails the meaning (ikhlal) is rejected outright.",
    "Sıralı iki sıfat: AZ, fakat YETER — ikinci kelime kayıttır; mânâyı karşılamayan kısalık (ihlâl) düpedüz merduttur.")]})

# --------------------------------------------- s2 — the itnab definition
S.append({"id": "s2", "translation": {
 "en": "And ITNAB is conveying the intended meaning's core by wording MORE than it — for a benefit. («for a benefit» bars tatwil and hashw: padding is not amplification.)",
 "tr": "ITNÂB ise murâdın aslını ondan DAHA ÇOK bir lafızla — bir FAYDA İÇİN — getirmektir. («fayda için» kaydı tatvîli ve haşvi dışarır: dolgu, ıtnâb değildir.)"},
 "tokens": [
  tok("وَالْإِطْنَابُ","itnab","noun",["ijaz-itnab-musawat"],
      "الْوَاوُ عَاطِفَةٌ، وَالْإِطْنَابُ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and amplification» — the second term, joined to the first (one bab, one fabric).",
      "«ve ıtnâb» — ilkine bağlanmış ikinci terim (tek bâb, tek kumaş).",
      segments=[seg("وَ","wa","part"), seg("الْإِطْنَابُ","itnab","noun")]),
  tok("تَأْدِيَةُ","tadiya-ada","noun",["ijaz-itnab-musawat"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«conveying» — the same khabar frame.",
      "«getirmek» — aynı haber çerçevesi."),
  tok("أَصْلِ","asl","noun",["ijaz-itnab-musawat"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the core of» —",
      "«aslını» —"),
  tok("الْمُرَادِ","murad","noun",["ijaz-itnab-musawat"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the intended» —",
      "«murâdın» —"),
  tok("بِلَفْظٍ","lafz","noun",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِتَأْدِيَةُ.",
      "«by wording» —",
      "«bir lafızla» —",
      segments=[seg("بِ","bi","part"), seg("لَفْظٍ","lafz","noun")]),
  tok("زَائِدٍ","zaid","noun",["ijaz-itnab-musawat","ism-fail"],
      "صِفَةٌ مَجْرُورَةٌ.",
      "«more» — the mirror of نَاقِصٍ.",
      "«daha çok» — نَاقِصٍ'in aynadaki karşılığı."),
  tok("عَلَيْهِ","ala","part",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِزَائِدٍ.",
      "«than it» — more THAN the meaning's measure.",
      "«onun üzerine» — mânânın ölçüsünden çok.",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")]),
  tok("لِفَائِدَةٍ","faida","noun",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِزَائِدٍ — وَهُوَ الِاحْتِرَازُ عَنِ التَّطْوِيلِ وَالْحَشْوِ.",
      "«for a benefit» — the definition's guard: excess WITHOUT benefit is tatwil (the surplus word unfixable) or hashw (the surplus word nameable), and both are rejected.",
      "«bir fayda için» — tarifin kaydı: faydasız fazlalık ya tatvîldir (fazla söz belirsiz) ya haşivdir (fazla söz belirli) ve ikisi de merduttur.",
      punct=".", segments=[seg("لِ","li","part"), seg("فَائِدَةٍ","faida","noun")])],
 "jumal": [
  J("وَالْإِطْنَابُ تَأْدِيَةُ أَصْلِ الْمُرَادِ بِلَفْظٍ زَائِدٍ عَلَيْهِ لِفَائِدَةٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — حَدُّ الْإِطْنَابِ.",
    "The itnab definition, joined: the two terms share one frame word for word, and only نَاقِص/زَائِد and the guards differ — the bab teaches by minimal pair.",
    "Itnâb tarifi, bağlı: iki terim kelime kelime tek çerçeveyi paylaşır; yalnız نَاقِص/زَائِد ile kayıtlar değişir — bâb, asgarî çiftle öğretir."),
  J("لِفَائِدَةٍ",
    "الِاحْتِرَازُ الَّذِي يُخْرِجُ التَّطْوِيلَ وَالْحَشْوَ.",
    "One prepositional phrase carrying the whole boundary between eloquent fullness and padding.",
    "Belâgatli doluluk ile dolgu arasındaki bütün sınırı taşıyan tek câr-mecrûr.")]})

# ------------------------------------------ s3 — the musawat definition
S.append({"id": "s3", "translation": {
 "en": "And MUSAWAT is conveying the intended meaning's core by wording EQUAL to it.",
 "tr": "MÜSÂVÂT ise murâdın aslını kendisine EŞİT bir lafızla getirmektir."},
 "tokens": [
  tok("وَالْمُسَاوَاةُ","musawat","noun",["ijaz-itnab-musawat"],
      "الْوَاوُ عَاطِفَةٌ، وَالْمُسَاوَاةُ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and the even measure» — the third term, masdar of Form III.",
      "«ve müsâvât» — üçüncü terim; III. bâbın masdarı.",
      segments=[seg("وَ","wa","part"), seg("الْمُسَاوَاةُ","musawat","noun")]),
  tok("تَأْدِيَةُ","tadiya-ada","noun",["ijaz-itnab-musawat"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«conveying» — the frame a third time.",
      "«getirmek» — çerçeve üçüncü kez."),
  tok("أَصْلِ","asl","noun",["ijaz-itnab-musawat"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "«the core of» —",
      "«aslını» —"),
  tok("الْمُرَادِ","murad","noun",["ijaz-itnab-musawat"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the intended» —",
      "«murâdın» —"),
  tok("بِلَفْظٍ","lafz","noun",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِتَأْدِيَةُ.",
      "«by wording» —",
      "«bir lafızla» —",
      segments=[seg("بِ","bi","part"), seg("لَفْظٍ","lafz","noun")]),
  tok("مُسَاوٍ","musawin","noun",["ijaz-itnab-musawat","ism-maqsur-manqus","ism-fail"],
      "صِفَةٌ مَجْرُورَةٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ، وَالتَّنْوِينُ عِوَضٌ.",
      "«equal» — a second indefinite manqus in one chapter: the ism fa'il of سَاوَى with its ya dropped and the compensation tanwin in its place.",
      "«eşit» — bir bâbda ikinci nekre mankus: سَاوَى'nın ism-i fâili; yâsı düşmüş, yerinde ivaz tenvini."),
  tok("لَهُ","li","part",["ijaz-itnab-musawat"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمُسَاوٍ.",
      "«to it» — equal TO the meaning's own measure.",
      "«ona» — mânânın kendi ölçüsüne eşit.",
      punct=".", segments=[seg("لَ","li","part"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("وَالْمُسَاوَاةُ تَأْدِيَةُ أَصْلِ الْمُرَادِ بِلَفْظٍ مُسَاوٍ لَهُ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — حَدُّ الْمُسَاوَاةِ.",
    "The even measure: neither guard is needed, for equality can neither starve the meaning nor pad it.",
    "Müsâvât: hiçbir kayda gerek yok; eşitlik mânâyı ne aç bırakabilir ne şişirebilir."),
  J("بِلَفْظٍ مُسَاوٍ لَهُ",
    "الْجَارُّ وَصِفَتُهُ — مِيزَانُ الْبَابِ كُلِّهِ.",
    "The measuring phrase the whole bab weighs against.",
    "Bütün bâbın kendisiyle tartıldığı ölçü öbeği.")]})

# ------------------- s4 — Fatir 35:43: musawat, riding a mufarragh qasr
S.append({"id": "s4", "translation": {
 "en": "And evil scheming besets none but its own people. (the MUSAWAT witness: wording and meaning weigh even — and the sentence rides a mufarragh qasr.)",
 "tr": "Kötü tuzak, ancak sahibinin başına iner. (MÜSÂVÂT şahidi: lafızla mânâ denk tartılır — ve cümle, müferrağ kasr üzerinde durur.)"},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["ijaz-itnab-musawat","qasr"],
      "الْوَاوُ عَاطِفَةٌ عَلَى مَا قَبْلَهَا فِي الْآيَاتِ، وَلَا نَافِيَةٌ — أَوَّلُ طَرَفَيِ الْقَصْرِ.",
      "«and not» — the waw joins the ayat's train; the la opens the qasr's first arm.",
      "«ve …maz» — vâv, âyet zincirine bağlar; lâ, kasrın ilk kolunu açar.",
      segments=[seg("وَ","wa","part"), seg("لَا","la-nafiya","part")]),
  tok("يَحِيقُ","haqa","verb",["ijaz-itnab-musawat","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«besets» — the hollow mudari of حَاقَ.",
      "«iner, kuşatır» — حَاقَ'ın ecvef muzârisi."),
  tok("الْمَكْرُ","makr","noun",["ijaz-itnab-musawat"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«the scheming» — the doer.",
      "«tuzak» — fâil."),
  tok("السَّيِّئُ","sayyi","noun",["ijaz-itnab-musawat"],
      "صِفَةٌ لِلْمَكْرُ مَرْفُوعَةٌ.",
      "«evil» — its sifa.",
      "«kötü» — sıfatı."),
  tok("إِلَّا","illa","part",["ijaz-itnab-musawat","qasr"],
      "أَدَاةُ حَصْرٍ — قَصْرٌ مُفَرَّغٌ.",
      "«except» — the qasr's second arm: what precedes is emptied for what follows.",
      "«ancak» — kasrın ikinci kolu: öncesi, sonrası için boşaltılmıştır."),
  tok("بِأَهْلِهِ","ahl","noun",["ijaz-itnab-musawat","qasr"],
      "الْبَاءُ جَارَّةٌ، وَأَهْلِ مَجْرُورٌ بِهَا وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَبَيْنَ اللَّفْظِ وَالْمَعْنَى مُسَاوَاةٌ.",
      "«but its own people» — the jarr phrase the qasr saves the verb for. Nothing here could be cut, nothing added: the source's own musawat witness.",
      "«ancak sahibine» — kasrın fiili kendisine sakladığı câr-mecrûr. Buradan bir şey kesilemez, bir şey eklenemez: kaynağın müsâvât şahidi.",
      punct=".", segments=[seg("بِ","bi","part"), seg("أَهْلِ","ahl","noun"), seg("هِ","pron-3ms","pron")])],
 "jumal": [
  J("وَلَا يَحِيقُ الْمَكْرُ السَّيِّئُ إِلَّا بِأَهْلِهِ",
    "جُمْلَةٌ فِعْلِيَّةٌ مَنْفِيَّةٌ بِقَصْرٍ مُفَرَّغٍ — وَهِيَ شَاهِدُ الْمُسَاوَاةِ.",
    "The musawat witness: read it slower or faster and nothing spills — word and meaning sit level.",
    "Müsâvât şahidi: yavaş da okusan hızlı da, hiçbir şey taşmaz — söz ile mânâ terazide dengededir."),
  J("إِلَّا بِأَهْلِهِ",
    "أُسْلُوبُ الْقَصْرِ: النَّفْيُ وَالِاسْتِثْنَاءُ.",
    "The qasr pair from chapter 21, met again in open text.",
    "21. bâbın kasr çifti, açık metinde yeniden.")]})

# --------------- s5 — Baqara 2:179: ijaz al-qasr, the bab's crown witness
S.append({"id": "s5", "translation": {
 "en": "And for you, in just retribution, is LIFE. (IJAZ AL-QASR: eleven letters that outweigh the Arabs' proudest maxim — the note counts the seven superiorities.)",
 "tr": "Kısasta sizin için HAYAT vardır. (ÎCÂZ-I KASR: Arapların en gururlu vecizesini geride bırakan on bir harf — not, yedi üstünlüğü sayar.)"},
 "tokens": [
  tok("وَلَكُمْ","li","part",["ijaz-itnab-musawat","taqdim-al-musnad"],
      "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ جَارَّةٌ وَالضَّمِيرُ مَجْرُورٌ — شِبْهُ الْجُمْلَةِ خَبَرٌ مُقَدَّمٌ وُجُوبًا.",
      "«and for you» — the jarr phrase fronted as khabar, OBLIGATORILY: the coming mubtada is indefinite.",
      "«ve sizin için» — haber olarak öne alınmış câr-mecrûr, hem de VÂCİBEN: gelecek mübtedâ nekredir.",
      segments=[seg("وَ","wa","part"), seg("لَ","li","part"), seg("كُمْ","pron-2mp","pron")]),
  tok("فِي","fi","part",["ijaz-itnab-musawat"],
      "حَرْفُ جَرٍّ.",
      "«in» —",
      "«içinde» —"),
  tok("الْقِصَاصِ","qisas","noun",["ijaz-itnab-musawat"],
      "مَجْرُورٌ بِفِي مُتَعَلِّقٌ بِالْخَبَرِ الْمُقَدَّمِ.",
      "«just retribution» — the majrur: the very thing that looks like death.",
      "«kısasta» — mecrur: ölüm gibi görünen şeyin tam kendisi."),
  tok("حَيَاةٌ","hayat","noun",["ijaz-itnab-musawat","tankir-al-musnad-ilayh"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَتَنْكِيرُهُ لِلتَّعْظِيمِ وَالنَّوْعِيَّةِ.",
      "«LIFE» — the delayed mubtada, and its tanwin does double work: a life of great worth, and a KIND of life (the would-be killer spared, the would-be victim spared). Meaning heaped on eleven letters: ijaz al-qasr.",
      "«HAYAT» — ertelenmiş mübtedâ; tenvini çift iş görür: büyük bir hayat ve bir TÜR hayat (vazgeçen kātil de kurtulur, hedefi de). On bir harfe yığılmış mânâ: îcâz-ı kasr.",
      punct=".")],
 "jumal": [
  J("وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ قُدِّمَ خَبَرُهَا — شَاهِدُ إِيجَازِ الْقَصْرِ.",
    "The bab's crown witness: much meaning, easy wording, and NOTHING omitted — brevity with no hadhf at all.",
    "Bâbın baş şahidi: çok mânâ, kolay lafız ve HİÇBİR şey hazfedilmemiş — hazifsiz kısalık."),
  J("حَيَاةٌ",
    "مُبْتَدَأٌ مُؤَخَّرٌ نُكِّرَ لِلتَّعْظِيمِ.",
    "One indefinite word carrying awe, kind, and the whole argument against the blood-feud.",
    "Tek nekre kelime: tazimi, türü ve kan davasına karşı bütün delili taşır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "ijaz": g("إِيجَاز", "و ج ز", "noun", "brevity, concision (saying it in less)", "îcâz, az sözle söyleme", 6),
 "itnab": g("إِطْنَاب", "ط ن ب", "noun", "amplification (saying it in more, for a benefit)", "ıtnâb, fayda için sözü genişletme", 6),
 "musawat": g("مُسَاوَاة", "س و ي", "noun", "the even measure (wording equal to the meaning)", "müsâvât, sözün mânâya denkliği", 6),
 "tadiya-ada": g("تَأْدِيَة", "أ د ي", "noun", "conveying, delivering (masdar of أَدَّى)", "edâ etme, yerine getirme (أَدَّى'nın masdarı)", 5),
 "adaa": g("أَدَاء", "أ د ي", "noun", "delivery, performance", "edâ, yerine getirme", 4),
 "naqis": g("نَاقِص", "ن ق ص", "noun", "lacking, less (ism fa'il)", "eksik, daha az (ism-i fâil)", 4),
 "wafin": g("وَافٍ", "و ف ي", "noun", "sufficient, fulfilling (indefinite manqus)", "yeter, yerine getiren (nekre mankus)", 5),
 "faida": g("فَائِدَة", "ف ي د", "noun", "benefit, gain", "fayda", 3, plural="فَوَائِد"),
 "musawin": g("مُسَاوٍ", "س و ي", "noun", "equal (ism fa'il of سَاوَى, indefinite manqus)", "eşit (سَاوَى'nın ism-i fâili; nekre mankus)", 5),
 "haqa": g("حَاقَ", "ح ي ق", "verb", "to beset, close in on (with بِ)", "kuşatmak, başına inmek (بِ ile)", 5, form="I"),
 "makr": g("مَكْر", "م ك ر", "noun", "scheming, plotting", "tuzak, hile", 4),
 "sayyi": g("سَيِّئ", "س و أ", "noun", "evil, bad", "kötü", 3),
 "qisas": g("قِصَاص", "ق ص ص", "noun", "just retribution (like for like)", "kısas", 4),
 "zaid": copy_gloss("mukhtasar-al-manar", "zaid"),
 "ahl": copy_gloss("wasiyyat-abi-hanifa-samti", "ahl"),
 "hayat": copy_gloss("mukhtasar-al-manar", "hayat"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/38.json").write_text(
    json.dumps({"chapter": 38, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 38 for c in man["chapters"]):
    man["chapters"].append({"n": 38, "title": TITLE38})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.38.0"
ADD_EN = (" Chapter 38 opens the ijaz/itnab/musawat bab (lines ~2640-2700, sahifa 91-93): s4 "
          "is Fatir 35:43 (part) and s5 al-Baqara 2:179 (part), received Qur'anic text quoted "
          "exactly in standard imla as the source prints them; s1-s3 are the musannif's "
          "definitions as the source recites them, each opened with its term as mubtada — the "
          "definitional frame this package has used since chapter 1.")
ADD_TR = (" Otuz sekizinci bâb îcâz/ıtnâb/müsâvât bâbını açar (satır ~2640-2700, sahife "
          "91-93): s4 Fâtır 35:43 (kısmen), s5 Bakara 2:179 (kısmen) — kaynağın bastığı "
          "standart imlâ ile aynen alınmış mervî Kur'ân metni; s1-s3, musannifin tarifleridir "
          "— kaynağın okuduğu şekliyle, her biri terimi mübtedâ yapılarak: bu paketin 1. "
          "bâbdan beri kullandığı tarif çerçevesi.")
if "2640-2700" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "haqa" not in mo["verbs"]:
    # hollow ya of bab daraba, lazim (governs through بِ) — the هَامَ road.
    mo["verbs"]["haqa"] = _sg.hollow1(
        "daraba", "أَجْوَفُ يَائِيٌّ", "حَاق", "حِق", "حِيق", "حِق", "حِيق", "حِق",
        "حَيْق", "حَائِق", None, None, None,
        "أَجْوَفُ يَائِيٌّ لَازِمٌ — يَتَعَدَّى بِالْبَاءِ: حَاقَ بِهِ.")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 142
GR = ROOT / "content/grammar"
NOTE142 = {
 "id": "ijaz-itnab-musawat",
 "title": {"ar": "الْإِيجَازُ وَالْإِطْنَابُ وَالْمُسَاوَاةُ",
           "en": "Brevity, amplification, and the even measure",
           "tr": "Îcâz, ıtnâb ve müsâvât"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — الإيجاز والإطناب والمساواة"],
 "question": {
  "en": ["Is the wording LESS than the meaning's measure yet still delivers it? Ijaz. More, for a benefit? Itnab. Even? Musawat.",
         "Does the shortness STARVE the meaning? Then it is ikhlal — rejected, not ijaz.",
         "Is the surplus word without benefit? Unnameable, it is tatwil; nameable, it is hashw — both rejected."],
  "tr": ["Lafız, mânânın ölçüsünden AZ ama yine de onu getiriyor mu? Îcâz. Fayda için ÇOK mu? Itnâb. Denk mi? Müsâvât.",
         "Kısalık mânâyı AÇ mı bırakıyor? O ihlâldir — merduttur, îcâz değildir.",
         "Fazla söz faydasız mı? Belirsizse tatvîl, belirliyse haşivdir — ikisi de merduttur."]},
 "plain": {
  "en": "Three accepted roads to saying what you mean: less wording that still delivers (ijaz), more for a benefit (itnab), and wording equal to the meaning (musawat) — the crown witness is وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ, eleven letters that outweigh the Arabs' proudest maxim. Three rejected: ikhlal, tatwil, hashw.",
  "tr": "Meramı söylemenin makbul üç yolu: yine de yerine getiren az söz (îcâz), fayda için çok söz (ıtnâb) ve mânâya denk söz (müsâvât) — baş şahit وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ: Arapların en gururlu vecizesini geçen on bir harf. Merdut üç yol: ihlâl, tatvîl, haşiv."},
 "explanation": {
  "en": "SAKKAKI declines to define ijaz and itnab outright — they are RELATIVE, he says, to the customary expression of the middling speakers (those who parse correctly but earn no praise or blame for eloquence); musawat is matching that custom. The MUSANNIF answers that relativity does not bar definition, and defines all three against the meaning's own measure: ijaz falls short of it yet SUFFICES (وَافٍ excludes IKHLAL — as in the bayt وَالْعَيْشُ خَيْرٌ فِي ظِلَالِ النُّوكِ, where the wording fails the intended «comfortable ignorance beats toilsome wisdom»); itnab exceeds it FOR A BENEFIT (لِفَائِدَةٍ excludes TATWIL — the surplus word unfixable, as مَيْنًا after كَذِبًا — and HASHW, the surplus word nameable: mufsid when it spoils, as النَّدَى in Abu al-Tayyib's line, or harmless, as قَبْلَهُ after الْأَمْسِ); musawat equals it, as in وَلَا يَحِيقُ الْمَكْرُ السَّيِّئُ إِلَّا بِأَهْلِهِ (35:43). IJAZ divides into qasr (no omission — density itself) and hadhf (omission). The qasr masterpiece is وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ (2:179) against the Arabs' أَلْقَتْلُ أَنْفَى لِلْقَتْلِ: fewer letters (eleven against fourteen), the SOUGHT thing (life) named outright, the tanwin of حَيَاةٌ carrying awe and kind at once, full generality, no repetition of قتل, no omitted word to reconstruct, and the tibaq of retribution-and-life gathered in one clause. The hadhf kinds — an omitted mudaf (وَاسْأَلِ الْقَرْيَةَ), an omitted mawsuf, whole omitted jumlas — are the next chapter's slice.",
  "tr": "SEKKÂKÎ, îcâz ile ıtnâbı doğrudan tarif etmez — bunlar, der, orta konuşanların (i'râbı doğru kuran ama belâgatle övülüp yerilmeyenlerin) örfündeki ifadeye GÖREDİR; müsâvât o örfe denk düşmektir. MUSANNIF, göreliliğin tarife engel olmadığını söyler ve üçünü mânânın kendi ölçüsüne göre tarif eder: îcâz ondan eksik kalır ama YETER (وَافٍ kaydı İHLÂLİ dışarır — وَالْعَيْشُ خَيْرٌ فِي ظِلَالِ النُّوكِ beytindeki gibi: lafız, «rahat cehalet, zahmetli akıldan yeğdir» murâdını karşılayamaz); ıtnâb, BİR FAYDA İÇİN aşar (لِفَائِدَةٍ kaydı TATVÎLİ — fazla söz belirsiz: كَذِبًا'dan sonra مَيْنًا — ve HAŞVİ dışarır: fazla söz belirli; bozuyorsa müfsid, Ebu't-Tayyib'in mısraındaki النَّدَى gibi; bozmuyorsa zararsız, الْأَمْسِ'den sonra قَبْلَهُ gibi); müsâvât ona denktir: وَلَا يَحِيقُ الْمَكْرُ السَّيِّئُ إِلَّا بِأَهْلِهِ (35:43). ÎCÂZ ikiye ayrılır: kasr (hazifsiz — yoğunluğun kendisi) ve hazif. Kasr şaheseri, Arapların أَلْقَتْلُ أَنْفَى لِلْقَتْلِ sözüne karşı وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ'dır (2:179): daha az harf (on dörde karşı on bir), İSTENEN şeyin (hayatın) açıkça adlanması, حَيَاةٌ tenvininin tazimle türü birden taşıması, tam umumîlik, قتل tekrarının yokluğu, takdir edilecek mahzufun yokluğu ve kısasla hayatı tek cümlede toplayan tıbâk. Hazif türleri — mahzuf muzâf (وَاسْأَلِ الْقَرْيَةَ), mahzuf mevsuf, mahzuf cümleler — gelecek bâbın dilimidir.",},
 "examples": [
  {"ar": "بِلَفْظٍ نَاقِصٍ عَنْهُ وَافٍ بِأَدَاءِ الْمُرَادِ",
   "en": "the ijaz definition — with the guard that bars ikhlal.",
   "tr": "îcâz tarifi — ihlâli dışaran kayıtla.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "وَلَا يَحِيقُ الْمَكْرُ السَّيِّئُ إِلَّا بِأَهْلِهِ",
   "en": "musawat: nothing to cut, nothing to add (35:43).",
   "tr": "müsâvât: kesilecek de eklenecek de yok (35:43).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "وَلَكُمْ فِي الْقِصَاصِ حَيَاةٌ",
   "en": "ijaz al-qasr: the eleven letters that beat the maxim (2:179).",
   "tr": "îcâz-ı kasr: vecizeyi geçen on bir harf (2:179).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«Kısa söz her zaman belâgatlidir»",
   "right": "«Mânâyı karşılamayan kısalık İHLÂLDİR ve merduttur»",
   "why": {"en": "The bab accepts SIX roads' worth of names and only three of the roads: brevity is praised only while وَافٍ holds — the wording must still DELIVER. The Harith b. Hilliza line is the standing warning: the poet meant «ease in folly beats toil with wits», and the words as they stand cannot carry it.",
           "tr": "Bâb altı yolun adını sayar, yalnız üçünü kabul eder: kısalık ancak وَافٍ kaydı durdukça övülür — lafız yine de TESLİM etmelidir. Hâris b. Hillize mısraı duran uyarıdır: şair «ahmaklıkta rahat, akılla zahmetten yeğdir» demek istedi; söz, olduğu hâliyle bunu taşıyamaz."}}],
 "relatedNotes": ["qasr", "hadhf-wa-taqdir", "tankir-al-musnad-ilayh", "ism-maqsur-manqus",
                  "taqdim-al-musnad"]}

(GR / "ijaz-itnab-musawat.json").write_text(
    json.dumps(NOTE142, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch38:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + haqa; note 142")
