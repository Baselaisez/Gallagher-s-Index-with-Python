# -*- coding: utf-8 -*-
"""Author chapter 32 of talkhis-al-miftah — كَمَالُ الِاتِّصَالِ (the martaba ladder).

Sahifa 79-82 (lines ~2297-2345): the second da'i of the fasl — KAMAL
AL-ITTISAL: the second jumla stands from the first as its TAWKID, its
BADAL, or its ATF BAYAN, and the source measures each jumla-grade
against a MUFRAD rank it recites outright:

  لَا رَيْبَ فِيهِ   from ذَلِكَ الْكِتَابُ  = the rank of نَفْسُهُ   (tawkid ma'nawi)
  هُدًى لِلْمُتَّقِينَ from ذَلِكَ الْكِتَابُ  = the rank of the 2nd زَيْدٌ (tawkid lafzi)
  the badal-ba'd aya (26:132-133)        = the rank of وَجْهُهُ
  the badal-ishtimal bayt                = the rank of حُسْنُهَا
  the atf-bayan aya (20:120)             = the rank of عُمَرُ

This chapter authors al-Baqara 2:2 (quoted exactly) and the FIVE mufrad
rank-fixtures the source itself recites — the ladder the next chapters'
ayat hang on. The 26:132-133 / 20:120 ayat and the badal bayt come in
the NEXT slice; note 136 cites them meanwhile as the book's own examples.

ATTRIBUTION: s1 is received Qur'anic text quoted exactly (al-Baqara 2:2,
standard imla as the source prints it); s2-s6 are the source's own
recited rank-fixtures verbatim (جَاءَنِي زَيْدٌ نَفْسُهُ، جَاءَنِي زَيْدٌ
زَيْدٌ، أَعْجَبَنِي زَيْدٌ وَجْهُهُ، أَعْجَبَنِي الدَّارُ حُسْنُهَا،
أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ), Ottoman orthography normalized to
standard — recorded normalizations.

Grammar this chapter teaches:
  • note 136 `kamal-al-ittisal` — the three grades with their mufrad
    ranks; anchors the aya and the fixtures.
  • the fixtures finally give atf-bayan its canonical anchor (أَبُو
    حَفْصٍ عُمَرُ) and put the five nouns, the diptote عُمَرُ, the
    genus-la and both tawkids in one chapter of real text.
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

TITLE32 = {"ar": "كَمَالُ الِاتِّصَالِ",
           "en": "Kamal al-Ittisal: the Martaba Ladder",
           "tr": "Kemâl-i İttisâl: Mertebe Merdiveni"}

# ------------------------------------- s1 — al-Baqara 2:2, the worked fasl
S.append({"id": "s1", "translation": {
 "en": "That is the Book — no doubt at all in it — a guidance for the godfearing. (al-Baqara 2:2: three jumlas, and not one atf letter between them.)",
 "tr": "İşte o Kitap — onda hiçbir şüphe yok — müttakîler için bir hidayettir. (Bakara 2:2: üç cümle ve aralarında tek bir atıf harfi yok.)"},
 "tokens": [
  tok("ذَلِكَ","dhalika","pron",["kamal-al-ittisal","asma-al-ishara"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«that» — the demonstrative, mabni, in the position of raf': the mubtada. The FAR pointer honours the Book's rank.",
      "«işte o» — işaret ismi; mebnî, mahallen merfû: mübtedâ. UZAK işareti, Kitâb'ın rütbesini yüceltir."),
  tok("الْكِتَابُ","kitab","noun",["kamal-al-ittisal"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«the Book» — the khabar, marfu': that is THE Book, the complete one — and such praise invites the doubter's whisper the next jumla will crush.",
      "«Kitap» — haber; merfû: işte O Kitap, kâmil olan — ve böyle bir övgü, bir sonraki cümlenin ezeceği şüphe fısıltısını davet eder."),
  tok("لَا","la-nafiya-lil-jins","part",["kamal-al-ittisal","la-nafiya-lil-jins"],
      "لَا النَّافِيَةُ لِلْجِنْسِ تَعْمَلُ عَمَلَ إِنَّ.",
      "«no … at all» — the genus-denying la, governing as inna does.",
      "«hiçbir … yok» — cinsi nefyeden lâ; إِنَّ gibi amel eder."),
  tok("رَيْبَ","rayb","noun",["kamal-al-ittisal","la-nafiya-lil-jins"],
      "اسْمُ لَا مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.",
      "«doubt» — la's ism, mabni on the fatha in the position of nasb: the whole genus of doubt is denied at once.",
      "«şüphe» — lâ'nın ismi; fetha üzere mebnî, mahallen mansub: şüphenin bütün cinsi bir anda nefyedilir."),
  tok("فِيهِ","fi","part",["kamal-al-ittisal"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ لَا.",
      "«in it» — the jarr phrase hanging on an omitted amil: la's khabar.",
      "«onda» — mahzûf âmile taalluk eden câr-mecrûr: lâ'nın haberi.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("هُدًى","huda","noun",["kamal-al-ittisal"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ تَقْدِيرُهُ هُوَ، مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ.",
      "«a guidance» — the khabar of an omitted mubtada (it is: هُوَ هُدًى), its damma estimated on the maqsur ending the tanwin rides.",
      "«bir hidayet» — mahzûf mübtedânın haberi (takdiri: هُوَ هُدًى); dammesi, tenvinin bindiği maksûr son üzerinde takdîrîdir."),
  tok("لِلْمُتَّقِينَ","muttaqi","noun",["kamal-al-ittisal"],
      "اللَّامُ حَرْفُ جَرٍّ، وَالْمُتَّقِينَ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، مُتَعَلِّقٌ بِهُدًى.",
      "«for the godfearing» — the lam of jarr; the sound plural declines by its YA; the phrase hangs on «guidance».",
      "«müttakîler için» — cer lâmı; cem'-i müzekker sâlim YÂ ile i'rablanır; öbek «hidayet»e taalluk eder.",
      punct=".", segments=[seg("لِ","li","part"), seg("الْمُتَّقِينَ","muttaqi","noun")])],
 "jumal": [
  J("ذَلِكَ الْكِتَابُ",
    "جُمْلَةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The first jumla: the praise that opens the Book.",
    "İlk cümle: Kitâb'ı açan övgü."),
  J("لَا رَيْبَ فِيهِ",
    "فُصِلَتْ لِكَمَالِ الِاتِّصَالِ — بِمَنْزِلَةِ التَّوْكِيدِ الْمَعْنَوِيِّ، مَرْتَبَةُ نَفْسِهِ فِي جَاءَنِي زَيْدٌ نَفْسُهُ.",
    "Cut loose by KAMAL AL-ITTISAL: it stands from the first jumla as a TAWKID MA'NAWI — the rank of نَفْسُهُ in «Zayd himself came» — crushing the suspicion that such praise was thrown out carelessly. What is one with you takes no joining letter.",
    "KEMÂL-İ İTTİSÂL ile ayrılmış: ilk cümleden TE'KÎD-İ MANEVÎ makamındadır — «Zeyd bizzat geldi»deki نَفْسُهُ mertebesi — övgünün rastgele atılmış söz olduğu vehmini ezer. Seninle BİR olan, bağlama harfi almaz."),
  J("هُدًى لِلْمُتَّقِينَ",
    "فُصِلَتْ لِكَمَالِ الِاتِّصَالِ — بِمَنْزِلَةِ التَّوْكِيدِ اللَّفْظِيِّ، مَرْتَبَةُ زَيْدٍ الثَّانِي فِي جَاءَنِي زَيْدٌ زَيْدٌ.",
    "Cut loose again: «that complete Book» MEANS «guidance beyond measure», so this jumla restates the first in other letters — a TAWKID LAFZI, the rank of the second زَيْدٌ — and again no waw may stand between a thing and itself.",
    "Yine ayrı: «o kâmil Kitap» zaten «ölçüye sığmaz hidayet» DEMEKTİR; bu cümle ilkini başka harflerle tekrar eder — TE'KÎD-İ LAFZÎ, ikinci زَيْدٌ mertebesi — ve bir şeyle kendisi arasında yine hiçbir vâv duramaz.")]})

# ------------------------------------- s2 — the tawkid-ma'nawi rank fixture
S.append({"id": "s2", "translation": {
 "en": "Zayd himself came to me. (the mufrad ruler: نَفْسُهُ measures the rank لَا رَيْبَ فِيهِ holds among jumlas.)",
 "tr": "Zeyd bana bizzat geldi. (müfred cetvel: نَفْسُهُ, cümleler içinde لَا رَيْبَ فِيهِ'nin tuttuğu mertebeyi ölçer.)"},
 "tokens": [
  tok("جَاءَنِي","jaa","verb",["kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«came to me» — a mazi on the fatha; the guarding nun shields it from the speaker's ya, the maf'ul.",
      "«bana geldi» — fetha üzere mebnî mâzî; vikaye nûnu onu mütekellim yâsından korur; yâ mef'ûldür.",
      segments=[seg("جَاءَ","jaa","verb"), seg("نِي","pron-1s","pron")]),
  tok("زَيْدٌ","zayd","propn",["kamal-al-ittisal"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the fa'il, marfu'.",
      "«Zeyd» — fâil; merfû."),
  tok("نَفْسُهُ","nafs","noun",["kamal-al-ittisal","tawkid"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ تَبَعًا لِزَيْدٍ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«himself» — the TAWKID MA'NAWI, marfu' in pursuit of Zayd; the pronoun is its mudaf ilayh. It kills the guess that someone came on his behalf.",
      "«bizzat» — TE'KÎD-İ MANEVÎ; Zeyd'e tâbi olarak merfû; zamir muzâfun ileyhtir. Onun adına başkasının geldiği tahminini öldürür.",
      punct=".", segments=[seg("نَفْسُ","nafs","noun"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("جَاءَنِي زَيْدٌ نَفْسُهُ",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "A verbal sentence, no mahall — the ruler recited for measuring, not for its news.",
    "Fiil cümlesi, mahalsiz — haberi için değil, ölçmek için okunan cetvel."),
  J("نَفْسُهُ",
    "مَرْتَبَةُ التَّوْكِيدِ الْمَعْنَوِيِّ — وَبِهَا تُوزَنُ جُمْلَةُ لَا رَيْبَ فِيهِ.",
    "THE RANK: what نَفْسُهُ is to Zayd, the whole jumla لَا رَيْبَ فِيهِ is to ذَلِكَ الْكِتَابُ — the source's own scale for the fasl.",
    "MERTEBE: نَفْسُهُ Zeyd'e ne ise, لَا رَيْبَ فِيهِ cümlesi bütünüyle ذَلِكَ الْكِتَابُ'a odur — kaynağın fasl için kendi terazisi.")]})

# ------------------------------------- s3 — the tawkid-lafzi rank fixture
S.append({"id": "s3", "translation": {
 "en": "Zayd — Zayd came to me. (the second ruler: the repeated زَيْدٌ measures the rank of هُدًى لِلْمُتَّقِينَ.)",
 "tr": "Zeyd — Zeyd geldi bana. (ikinci cetvel: tekrarlanan زَيْدٌ, هُدًى لِلْمُتَّقِينَ'in mertebesini ölçer.)"},
 "tokens": [
  tok("جَاءَنِي","jaa","verb",["kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«came to me» — the same mazi with its guarding nun.",
      "«bana geldi» — vikaye nûnuyla aynı mâzî.",
      segments=[seg("جَاءَ","jaa","verb"), seg("نِي","pron-1s","pron")]),
  tok("زَيْدٌ","zayd","propn",["kamal-al-ittisal"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the fa'il, marfu'.",
      "«Zeyd» — fâil; merfû."),
  tok("زَيْدٌ","zayd","propn",["kamal-al-ittisal","tawkid"],
      "تَوْكِيدٌ لَفْظِيٌّ مَرْفُوعٌ تَبَعًا لِلْأَوَّلِ.",
      "«Zayd» — the TAWKID LAFZI: the very word said again, marfu' in pursuit of the first. Nothing new arrives; the arrival itself is pressed home.",
      "«Zeyd» — TE'KÎD-İ LAFZÎ: kelimenin kendisi yeniden söylenir; ilkine tâbi olarak merfû. Yeni bir şey gelmez; gelişin kendisi perçinlenir.",
      punct=".")],
 "jumal": [
  J("جَاءَنِي زَيْدٌ زَيْدٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The second ruler, recited whole.",
    "Bütünüyle okunan ikinci cetvel."),
  J("زَيْدٌ",
    "مَرْتَبَةُ التَّوْكِيدِ اللَّفْظِيِّ — وَبِهَا تُوزَنُ جُمْلَةُ هُدًى لِلْمُتَّقِينَ.",
    "THE RANK: what the second زَيْدٌ is to the first, هُدًى لِلْمُتَّقِينَ is to ذَلِكَ الْكِتَابُ — the same meaning walking in new letters.",
    "MERTEBE: ikinci زَيْدٌ ilkine ne ise, هُدًى لِلْمُتَّقِينَ de ذَلِكَ الْكِتَابُ'a odur — aynı mânânın yeni harflerle yürüyüşü.")]})

# ------------------------------------- s4 — the badal-ba'd rank fixture
S.append({"id": "s4", "translation": {
 "en": "Zayd pleased me — his face. (the third ruler: وَجْهُهُ, a part for the whole — the badal ba'd rank the next slice's aya will hang on.)",
 "tr": "Zeyd hoşuma gitti — yüzü. (üçüncü cetvel: وَجْهُهُ, bütünün yerine parça — bir sonraki dilimin âyetinin asılacağı bedel-i ba'z mertebesi.)"},
 "tokens": [
  tok("أَعْجَبَنِي","aajaba","verb",["kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«pleased me» — the Form IV mazi with the guarding nun; the speaker's ya is the object.",
      "«hoşuma gitti» — vikaye nûnlu IV. bâb mâzîsi; mütekellim yâsı mef'ûldür.",
      segments=[seg("أَعْجَبَ","aajaba","verb"), seg("نِي","pron-1s","pron")]),
  tok("زَيْدٌ","zayd","propn",["kamal-al-ittisal"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — the fa'il, marfu'.",
      "«Zeyd» — fâil; merfû."),
  tok("وَجْهُهُ","wajh","noun",["kamal-al-ittisal","badal"],
      "بَدَلُ بَعْضٍ مِنْ كُلٍّ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ رَابِطٌ.",
      "«his face» — BADAL BA'D MIN KULL: the part swapped in for the whole, marfu' in Zayd's case; the pronoun is the tether back to him. What pleased was not all of Zayd but this of him.",
      "«yüzü» — BEDEL-İ BA'Z: bütünün yerine geçen parça; Zeyd'in i'rabında merfû; zamir, ona bağlayan iptir. Hoşa giden Zeyd'in tamamı değil, ondan bu parçadır.",
      punct=".", segments=[seg("وَجْهُ","wajh","noun"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("أَعْجَبَنِي زَيْدٌ وَجْهُهُ",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The third ruler.",
    "Üçüncü cetvel."),
  J("وَجْهُهُ",
    "مَرْتَبَةُ بَدَلِ الْبَعْضِ — وَبِهَا تُوزَنُ جُمْلَةُ التَّفْصِيلِ بَعْدَ الْإِجْمَالِ.",
    "THE RANK: a second jumla that details PART of what the first said whole (the ni'am aya, 26:132-133, in the next slice) stands from it as وَجْهُهُ stands from Zayd.",
    "MERTEBE: ilkinin toptan söylediğinin BİR KISMINI ayrıntılayan ikinci cümle (bir sonraki dilimdeki nimetler âyeti, 26:132-133), ondan وَجْهُهُ'nun Zeyd'den durduğu yerde durur.")]})

# ------------------------------------- s5 — the badal-ishtimal rank fixture
S.append({"id": "s5", "translation": {
 "en": "The house pleased me — its beauty. (the fourth ruler: حُسْنُهَا, a quality the whole contains — the badal ishtimal rank.)",
 "tr": "Ev hoşuma gitti — güzelliği. (dördüncü cetvel: حُسْنُهَا, bütünün kapsadığı bir nitelik — bedel-i iştimâl mertebesi.)"},
 "tokens": [
  tok("أَعْجَبَنِي","aajaba","verb",["kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«pleased me» — the same Form IV mazi.",
      "«hoşuma gitti» — aynı IV. bâb mâzîsi.",
      segments=[seg("أَعْجَبَ","aajaba","verb"), seg("نِي","pron-1s","pron")]),
  tok("الدَّارُ","dar","noun",["kamal-al-ittisal"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«the house» — the fa'il, marfu'.",
      "«ev» — fâil; merfû."),
  tok("حُسْنُهَا","husn","noun",["kamal-al-ittisal","badal"],
      "بَدَلُ اشْتِمَالٍ مَرْفُوعٌ، وَالْهَا مُضَافٌ إِلَيْهِ رَابِطٌ.",
      "«its beauty» — BADAL ISHTIMAL: not a physical part but a quality the house CONTAINS, marfu' in its case with the pronoun tether. A part you could cut off is ba'd; a beauty you cannot is ishtimal.",
      "«güzelliği» — BEDEL-İ İŞTİMÂL: fizikî bir parça değil, evin KAPSADIĞI bir nitelik; onun i'rabında merfû, zamir ipiyle. Kesip ayırabildiğin parça ba'zdır; ayıramadığın güzellik iştimâldir.",
      punct=".", segments=[seg("حُسْنُ","husn","noun"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("أَعْجَبَنِي الدَّارُ حُسْنُهَا",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The fourth ruler.",
    "Dördüncü cetvel."),
  J("حُسْنُهَا",
    "مَرْتَبَةُ بَدَلِ الِاشْتِمَالِ — وَبِهَا يُوزَنُ الْإِيضَاحُ الَّذِي لَيْسَ بَعْضًا وَلَا عَيْنًا.",
    "THE RANK: a second jumla that unfolds what the first CONTAINED without being a part of it (the bayt of ارْحَلْ, next slice) stands as حُسْنُهَا stands from the house.",
    "MERTEBE: ilkinin KAPSADIĞINI, parçası olmadan açan ikinci cümle (bir sonraki dilimdeki ارْحَلْ beyti), evden حُسْنُهَا'nın durduğu yerde durur.")]})

# ------------------------------------- s6 — the atf-bayan rank fixture
S.append({"id": "s6", "translation": {
 "en": "Abu Hafs — Umar — swore by Allah. (the fifth ruler: عُمَرُ unveils who the kunya named — the atf bayan rank.)",
 "tr": "Ebû Hafs — Ömer — Allah'a yemin etti. (beşinci cetvel: عُمَرُ, künyenin kimi adlandırdığını açar — atf-ı beyân mertebesi.)"},
 "tokens": [
  tok("أَقْسَمَ","aqsama","verb",["kamal-al-ittisal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«swore» — a Form IV mazi on the fatha.",
      "«yemin etti» — fetha üzere mebnî IV. bâb mâzîsi."),
  tok("بِاللهِ","allah","propn",["kamal-al-ittisal"],
      "الْبَاءُ حَرْفُ جَرٍّ لِلْقَسَمِ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ، مُتَعَلِّقٌ بِأَقْسَمَ.",
      "«by Allah» — the ba of the oath; the Name in jarr, the phrase hanging on the verb.",
      "«Allah'a» — kasem bâsı; lafza-i celâl mecrûr; öbek fiile taalluk eder.",
      segments=[seg("بِ","bi","part"), seg("اللهِ","allah","propn")]),
  tok("أَبُو","ab","noun",["kamal-al-ittisal","five-nouns"],
      "فَاعِلٌ مَرْفُوعٌ بِالْوَاوِ لِأَنَّهُ مِنَ الْأَسْمَاءِ الْخَمْسَةِ وَهُوَ مُضَافٌ.",
      "«the father of» — the fa'il, marfu' by its WAW: one of the five nouns, annexed as they must be.",
      "«babası» — fâil; VÂVLA merfû: beş isimden biridir ve olmaları gerektiği gibi muzâftır."),
  tok("حَفْصٍ","hafs","propn",["kamal-al-ittisal"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.",
      "«Hafs» — the mudaf ilayh, majrur: the kunya is complete, and still a veil.",
      "«Hafs'ın» — muzâfun ileyh; mecrûr: künye tamamdır ve hâlâ bir örtüdür."),
  tok("عُمَرُ","umar","propn",["kamal-al-ittisal","atf-bayan","mamnu-min-sarf"],
      "عَطْفُ بَيَانٍ مَرْفُوعٌ بِالضَّمَّةِ بِلَا تَنْوِينٍ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعَدْلِ.",
      "«Umar» — the ATF BAYAN: the plain name unveiling whom the kunya wrapped, marfu' with NO tanwin — barred from full declension by name-hood plus the deflected pattern فُعَل.",
      "«Ömer» — ATF-I BEYÂN: künyenin sardığını açan asıl ad; TENVİNSİZ merfû — alemlik ve udûl (فُعَل kalıbı) sebebiyle gayr-i munsarif.",
      punct=".")],
 "jumal": [
  J("أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The fifth ruler — the books' own atf-bayan verse-line.",
    "Beşinci cetvel — kitapların kendi atf-ı beyân mısraı."),
  J("عُمَرُ",
    "مَرْتَبَةُ عَطْفِ الْبَيَانِ — وَبِهَا تُوزَنُ الْجُمْلَةُ الَّتِي تَكْشِفُ إِبْهَامَ الْأُولَى.",
    "THE RANK: a second jumla that lifts the first one's obscurity (قَالَ يَا آدَمُ after فَوَسْوَسَ — 20:120, next slice) stands as عُمَرُ stands from أَبُو حَفْصٍ.",
    "MERTEBE: ilkinin kapalılığını kaldıran ikinci cümle (فَوَسْوَسَ'den sonra قَالَ يَا آدَمُ — 20:120, sonraki dilim), أَبُو حَفْصٍ'dan عُمَرُ'in durduğu yerde durur.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "aajaba": g("أَعْجَبَ", "ع ج ب", "verb", "to please, delight", "hoşuna gitmek, beğendirmek", 4, form="IV"),
 "aqsama": g("أَقْسَمَ", "ق س م", "verb", "to swear (an oath)", "yemin etmek", 4, form="IV"),
 "hafs": g("حَفْص", None, "propn", "Hafs (a man's name; Abu Hafs is Umar's kunya)", "Hafs (erkek adı; Ebû Hafs, Ömer'in künyesidir)", 5),
 "umar": copy_gloss("aqaid-ahl-al-sunna", "umar"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/32.json").write_text(
    json.dumps({"chapter": 32, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 32 for c in man["chapters"]):
    man["chapters"].append({"n": 32, "title": TITLE32})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.32.0"
ADD_EN = (" Chapter 32 carries kamal al-ittisal's martaba ladder (lines ~2297-2345, sahifa "
          "79-82): s1 is received Qur'anic text quoted exactly — al-Baqara 2:2 in standard "
          "imla; s2-s6 are the source's own recited mufrad rank-fixtures verbatim, Ottoman "
          "orthography normalized to standard — recorded normalizations, no wording changed.")
ADD_TR = (" Otuz ikinci bâb, kemâl-i ittisâlin mertebe merdivenini taşır (satır ~2297-2345, "
          "sahife 79-82): s1 aynen alınmış mervî Kur'ân metnidir — Bakara 2:2, standart imlâ "
          "ile; s2-s6, kaynağın kendi okuduğu müfred mertebe cetvellerinin aynen alınmışıdır; "
          "Osmanlı imlâsı standart imlâya çevrildi — kayıtlı normalizasyonlardır, hiçbir ifade "
          "değiştirilmedi.")
if "2297-2345" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "aajaba" not in mo["verbs"]:
    mo["verbs"]["aajaba"] = _sg.derived(
        _sg.B4, _sg.W4, "ُ", "أَعْجَب", "عْجِب", "أَعْجِب",
        "إِعْجَاب", "مُعْجِب", "مُعْجَب", "أُعْجِبَ", "يُعْجَبُ")
if "aqsama" not in mo["verbs"]:
    mo["verbs"]["aqsama"] = _sg.derived(
        _sg.B4, _sg.W4, "ُ", "أَقْسَم", "قْسِم", "أَقْسِم",
        "إِقْسَام", "مُقْسِم", None, "أُقْسِمَ", "يُقْسَمُ")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 136
GR = ROOT / "content/grammar"
NOTE136 = {
 "id": "kamal-al-ittisal",
 "title": {"ar": "كَمَالُ الِاتِّصَالِ", "en": "Kamal al-ittisal: the martaba ladder", "tr": "Kemâl-i ittisâl: mertebe merdiveni"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — دواعي الفصل: كمال الاتصال"],
 "question": {
  "en": ["Does the second jumla only press the first home — لَا رَيْبَ فِيهِ? The tawkid rank: fasl.",
         "Does it re-deliver the first more fully — the detailed ni'am after the summary? The badal rank: fasl.",
         "Does it lift the first one's obscurity — قَالَ يَا آدَمُ after the whisper? The atf-bayan rank: fasl."],
  "tr": ["İkinci cümle ilkini yalnızca perçinliyor mu — لَا رَيْبَ فِيهِ? Te'kîd mertebesi: fasl.",
         "İlkini daha dolu mu yeniden veriyor — özetten sonra ayrıntılı nimetler? Bedel mertebesi: fasl.",
         "İlkinin kapalılığını mı kaldırıyor — vesveseden sonra قَالَ يَا آدَمُ? Atf-ı beyân mertebesi: fasl."]},
 "plain": {
  "en": "When the second jumla is ONE with the first — its tawkid, its badal, or its atf bayan — no joining letter may stand between them: that is kamal al-ittisal, and fasl is obligatory. The source measures each grade with a mufrad ruler: نَفْسُهُ, the repeated زَيْدٌ, وَجْهُهُ, حُسْنُهَا, and عُمَرُ after أَبُو حَفْصٍ.",
  "tr": "İkinci cümle ilkiyle BİR ise — te'kîdi, bedeli veya atf-ı beyânı ise — aralarına bağlama harfi giremez: kemâl-i ittisâl budur ve fasl vâciptir. Kaynak her dereceyi bir müfred cetvelle ölçer: نَفْسُهُ, tekrarlanan زَيْدٌ, وَجْهُهُ, حُسْنُهَا ve أَبُو حَفْصٍ'tan sonra عُمَرُ."},
 "explanation": {
  "en": "KAMAL AL-ITTISAL is the second da'i of the fasl: the two jumlas are so united that joining them would be joining a thing to itself. Its grades are the tawabi' lifted to clauses, each with the mufrad rank the source recites: (1) TAWKID — in al-Baqara 2:2 the praise ذَلِكَ الْكِتَابُ invites the whisper that such words were thrown out carelessly, and لَا رَيْبَ فِيهِ crushes it at the rank of نَفْسُهُ; then هُدًى لِلْمُتَّقِينَ restates the praise in new letters at the rank of the second زَيْدٌ, since «that complete Book» already MEANS «guidance beyond measure». (2) BADAL — where the first jumla did not fully deliver the intent, the second re-delivers it: in part (26:132-133, أَمَدَّكُمْ بِمَا تَعْلَمُونَ ... بِأَنْعَامٍ وَبَنِينَ — the rank of وَجْهُهُ), or by what it contains (the poet's اِرْحَلْ لَا تُقِيمَنَّ عِنْدَنَا — the rank of حُسْنُهَا). (3) ATF BAYAN — where the first jumla is obscure, the second unveils it: after فَوَسْوَسَ إِلَيْهِ الشَّيْطَانُ the aya says قَالَ يَا آدَمُ (20:120) — the rank of عُمَرُ after أَبُو حَفْصٍ. In every grade the atf is LEFT, and the leaving is the eloquence.",
  "tr": "KEMÂL-İ İTTİSÂL, faslın ikinci dâîsidir: iki cümle o kadar birdir ki, bağlamak bir şeyi kendine bağlamak olurdu. Dereceleri, cümlelere yükseltilmiş tevâbi'dir; her biri kaynağın okuduğu müfred cetvelle ölçülür: (1) TE'KÎD — Bakara 2:2'de ذَلِكَ الْكِتَابُ övgüsü, bu sözlerin rastgele atıldığı vehmini davet eder; لَا رَيْبَ فِيهِ onu نَفْسُهُ mertebesinde ezer; sonra هُدًى لِلْمُتَّقِينَ, övgüyü yeni harflerle ikinci زَيْدٌ mertebesinde tekrar eder — çünkü «o kâmil Kitap» zaten «ölçüsüz hidayet» demektir. (2) BEDEL — ilk cümle maksadı tam vermemişse ikincisi yeniden verir: kısmen (26:132-133, أَمَدَّكُمْ بِمَا تَعْلَمُونَ ... بِأَنْعَامٍ وَبَنِينَ — وَجْهُهُ mertebesi) veya kapsadığıyla (şairin اِرْحَلْ لَا تُقِيمَنَّ عِنْدَنَا'sı — حُسْنُهَا mertebesi). (3) ATF-I BEYÂN — ilk cümle kapalıysa ikincisi açar: فَوَسْوَسَ إِلَيْهِ الشَّيْطَانُ'dan sonra âyet قَالَ يَا آدَمُ der (20:120) — أَبُو حَفْصٍ'tan sonra عُمَرُ mertebesi. Her derecede atıf TERK edilir ve terk, belâgatin kendisidir."},
 "examples": [
  {"ar": "ذَلِكَ الْكِتَابُ لَا رَيْبَ فِيهِ هُدًى لِلْمُتَّقِينَ",
   "en": "al-Baqara 2:2 — three jumlas held apart: the two tawkid ranks in one aya.",
   "tr": "Bakara 2:2 — ayrı tutulan üç cümle: tek âyette iki te'kîd mertebesi.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "جَاءَنِي زَيْدٌ نَفْسُهُ",
   "en": "«Zayd himself came» — the mufrad ruler for the tawkid-ma'nawi grade.",
   "tr": "«Zeyd bizzat geldi» — te'kîd-i manevî derecesinin müfred cetveli.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "أَقْسَمَ بِاللهِ أَبُو حَفْصٍ عُمَرُ",
   "en": "«Abu Hafs — Umar — swore by Allah» — the atf-bayan ruler.",
   "tr": "«Ebû Hafs — Ömer — Allah'a yemin etti» — atf-ı beyân cetveli.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«لَا رَيْبَ فِيهِ ile هُدًى لِلْمُتَّقِينَ aynı mertebede te'kîddir»",
   "right": "«İlki manevî (نَفْسُهُ), ikincisi lafzî (زَيْدٌ زَيْدٌ) mertebesindedir»",
   "why": {"en": "The first jumla denies a suspicion the praise raised — that is نَفْسُهُ's work, killing the wrong guess. The second SAYS THE PRAISE AGAIN in other words — that is the repeated زَيْدٌ's work. One aya, two different tawkids, and the source names each rank.",
           "tr": "İlk cümle, övgünün doğurduğu vehmi nefyeder — bu نَفْسُهُ'nun işidir: yanlış tahmini öldürmek. İkincisi övgüyü BAŞKA KELİMELERLE YENİDEN SÖYLER — bu da tekrarlanan زَيْدٌ'un işidir. Tek âyet, iki ayrı te'kîd; kaynak her mertebeyi adlandırır."}}],
 "relatedNotes": ["al-fasl-wa-al-wasl", "tawkid", "badal", "atf-bayan",
                  "la-nafiya-lil-jins", "mamnu-min-sarf", "five-nouns"]}

(GR / "kamal-al-ittisal.json").write_text(
    json.dumps(NOTE136, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch32:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + aajaba, aqsama; note 136")
