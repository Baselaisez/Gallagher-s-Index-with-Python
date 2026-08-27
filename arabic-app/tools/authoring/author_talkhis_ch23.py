# -*- coding: utf-8 -*-
"""Author chapter 23 of talkhis-al-miftah — الْإِنْشَاءُ وَالتَّمَنِّي.

The insha bab opens (sahifa 68-69): speech with no external nisba — no
truth or falsehood can touch it — split into talabi and ghayr-talabi,
and the FIRST of the five talabi kinds walked in full:

  • لَيْتَ is coined for the wish, and the wished-for need not be
    possible — لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا.
  • هَلْ is borrowed for it where the asker despairs — هَلْ لِي مِنْ
    شَفِيعٍ said where no intercessor is known to exist.
  • لَوْ is borrowed for it, and the SURFACE proves the borrowing: in
    لَوْ تَأْتِينِي فَتُحَدِّثَنِي the fa-verb wears NASB by a hidden أَنْ —
    and that nasb never follows a conditional; it follows one of the
    six talab things. The nasb is the dalil (the source's own argument).
  • هَلَّا (and أَلَّا، لَوْلَا، لَوْمَا) before a MADI is TANDIM (reproach
    for what was left undone — هَلَّا أَكْرَمْتَ زَيْدًا) and before a
    MUDARI is TAHDID (urging — هَلَّا تَقُومُ); Sakkaki derives them from
    hal/law + a tamanni-laden zaida ma/la.
  • لَعَلَّ's asl is tarajji; when the hoped thing is REMOTE it is given
    layta's hukm, and the same receipt shows: لَعَلِّي أَحُجُّ فَأَزُورَكَ.

ATTRIBUTION: every sentence is the source's own example quoted verbatim
(research/sources/talkhis-al-miftah-balagha.txt lines ~1945-1990, sahifa
68-69), Ottoman plain-alif normalized to standard orthography (لِى → لِي)
— a recorded normalization, not an edit.

Grammar this chapter teaches:
  • note 125 `insha-wa-tamanni` — the insha definition, the talabi
    split, tamanni's particle and its three borrowed ones, the
    fa-sababiyya dalil, and the tandim/tahdid tense split.
  • engine work: InshaEngine (new — layta frame, law/la'alla proven by
    the hidden-an nasb, tahdid split by tense, hal's wish as a
    shortlist), the tahdid particles as closed-class rows, ShartEngine
    standing down for the borrowed لَوْ and the verb-faced لَوْلَا.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
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

TITLE23 = {"ar": "الْإِنْشَاءُ وَالتَّمَنِّي",
           "en": "Insha, and the Wish",
           "tr": "İnşâ ve Temennî"}

# ------------------------------------------------- s1 — the coined particle
S.append({"id": "s1", "translation": {
 "en": "Would that youth returned one day! (The wished-for need not even be possible — layta is tamanni's own particle, and insha admits no true or false.)",
 "tr": "Keşke gençlik bir gün geri dönse! (Temennî edilenin mümkün olması bile gerekmez — لَيْتَ temennînin asıl edatıdır; inşâya doğru-yanlış işlemez.)"},
 "tokens": [
  tok("لَيْتَ","layta","part",["insha-wa-tamanni","khabar-insha"],
      "حَرْفُ تَمَنٍّ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ — وَالْكَلَامُ إِنْشَائِيٌّ لَا يَحْتَمِلُ الصِّدْقَ وَالْكَذِبَ.",
      "«would that» — the particle COINED for tamanni, an inna-sister in government. And the sentence it opens is INSHA: it sets up a wish rather than reporting a fact, so no one can call it true or false — that impossibility is insha's very definition.",
      "«keşke» — temennî için KONULMUŞ edat; amelce inne'nin kızkardeşi. Açtığı söz İNŞÂdır: bir vâkıayı haber vermez, bir dilek kurar; ona doğru da yanlış da denemez — bu imkânsızlık inşânın ta kendisinin tarifidir."),
  tok("الشَّبَابَ","shabab","noun",["insha-wa-tamanni"],
      "اسْمُ لَيْتَ مَنْصُوبٌ.",
      "«youth» — layta's ism, mansub by the inna-family government.",
      "«gençlik» — لَيْتَ'nin ismi; inne ailesi ameliyle mansub."),
  tok("يَعُودُ","ada-return","verb",["insha-wa-tamanni","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَيْتَ.",
      "«returns» — a marfu' mudari; the verbal clause stands as layta's khabar, in the position of raf'.",
      "«döner» — merfû muzâri; fiil cümlesi لَيْتَ'nin haberi olarak ref' mahallindedir."),
  tok("يَوْمًا","yawm","noun",["insha-wa-tamanni"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ — مَفْعُولٌ فِيهِ.",
      "«one day» — a mansub time-zarf, maf'ul fih.",
      "«bir gün» — mansub zaman zarfı; mef'ûlün fîh.",
      punct=".")],
 "jumal": [
  J("لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا",
    "الْجُمْلَةُ إِنْشَائِيَّةٌ طَلَبِيَّةٌ: لَا نِسْبَةَ لَهَا فِي الْخَارِجِ تُطَابِقُ أَوْ تُخَالِفُ.",
    "INSHA TALABI: the sentence has no external nisba for its words to match or miss — that is why true/false cannot touch it — and it is TALABI because the wanted thing is not in hand at the moment of asking.",
    "İNŞÂ-İ TALEBÎ: cümlenin dışarıda mutabık kalacağı yahut aykırı düşeceği bir nispeti yoktur — doğru/yanlışın ona işlememesi bundandır — ve istenen şey, isteme ânında elde olmadığı için TALEBÎdir."),
  J("لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا",
    "تَمَنِّي الْمُسْتَحِيلِ صَحِيحٌ: لَا يُشْتَرَطُ إِمْكَانُ الْمُتَمَنَّى.",
    "The wish for the IMPOSSIBLE is sound: youth does not return, and is wished for anyway — possibility is no condition of tamanni, which is what separates it from tarajji's hope for the attainable.",
    "MUHÂLİN temennîsi sahihtir: gençlik geri dönmez, yine de temennî edilir — imkân, temennînin şartı değildir; onu ulaşılabilire ümit olan tereccîden ayıran da budur.")]})

# ------------------------------------------------- s2 — hal borrowed
S.append({"id": "s2", "translation": {
 "en": "Have I any intercessor? (Said where none is known to exist: the question form carries the wish — hal borrowed for tamanni.)",
 "tr": "Bana bir şefaatçi var mı? (Şefaatçinin olmadığı bilinen yerde söylenir: soru kalıbı temennî taşır — هَلْ temennî için ödünç alınmıştır.)"},
 "tokens": [
  tok("هَلْ","hal","part",["insha-wa-tamanni"],
      "حَرْفُ اسْتِفْهَامٍ أُشْرِبَ مَعْنَى التَّمَنِّي.",
      "«have…?» — the question particle, here made to drink tamanni's meaning: the asker knows no intercessor exists, so the question is a wish wearing a question's dress. Istifham stays the asl — the despair that turns it lives in the heart, not on the page.",
      "«var mı?» — istifham edatı; burada temennî mânâsı içirilmiştir: soran, şefaatçinin olmadığını bilir; soru, soru elbisesi giymiş bir dilektir. İstifham asıl kalır — onu çeviren ümitsizlik sayfada değil kalptedir."),
  tok("لِي","li","part",["insha-wa-tamanni","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ — خَبَرٌ مُقَدَّمٌ.",
      "«for me» — لِ opened to لَ's shape before the ya; the jarr-phrase as khabar muqaddam, fronted before its indefinite mubtada.",
      "«bana» — câr-mecrûr, haber-i mukaddem; nekre mübtedâsından önce alınmış.",
      segments=[seg("لِ","li","prep"), seg("ي","pron-1s","pron")]),
  tok("مِنْ","min","part",["insha-wa-tamanni","huruf-jarr"],
      "حَرْفُ جَرٍّ زَائِدٌ لِتَأْكِيدِ الْعُمُومِ بَعْدَ الِاسْتِفْهَامِ.",
      "«any» — the ZAIDA min: after a question (as after a negation) it stresses the sweep — «any intercessor at all» — and governs the word's letter, not its place.",
      "«hiçbir» — ZÂİD min: istifhamdan sonra (nefiyden sonraki gibi) kapsamı pekiştirir — «herhangi bir şefaatçi» — kelimenin lafzını cerreder, mahallini değil."),
  tok("شَفِيعٍ","shafi","noun",["insha-wa-tamanni"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا مَرْفُوعٌ مَحَلًّا.",
      "«intercessor» — the deferred mubtada: majrur in LETTER by the zaida min, marfu' in PLACE — the lafzan/mahallan split on one word.",
      "«şefaatçi» — muahhar mübtedâ: zâid min ile LAFZAN mecrur, MAHALLEN merfû — lafız/mahal ayrımı tek kelimede.",
      punct=".")],
 "jumal": [
  J("هَلْ لِي مِنْ شَفِيعٍ",
    "اسْتِفْهَامٌ أُشْرِبَ مَعْنَى التَّمَنِّي — لِتَعَذُّرِ الْمَسْؤُولِ عَنْهُ.",
    "The BORROWED question: where the asked-about thing is known absent, asking after it can only be wishing for it. The form is istifham; the despair converts it — and because the despair is in the heart, the reading is an offered wajh, never a surface verdict.",
    "ÖDÜNÇ soru: sorulan şeyin yokluğu bilindiği yerde onu sormak, ancak onu dilemektir. Kalıp istifhamdır; onu çeviren ümitsizliktir — ve ümitsizlik kalpte olduğundan bu okuyuş sunulan bir vecihtir, asla yüzey hükmü değildir."),
  J("هَلْ لِي مِنْ شَفِيعٍ",
    "«مِنْ» الزَّائِدَةُ تَجُرُّ اللَّفْظَ وَيَبْقَى الْمَحَلُّ رَفْعًا.",
    "The zaida min governs the LETTER and leaves the PLACE alone: shafi' is majrur lafzan, marfu' mahallan as the mubtada — the same two-layer reading every mahalli i'rab trains.",
    "Zâid مِنْ LAFZI cerreder, MAHALLİ bırakır: şefî' lafzan mecrur, mübtedâ olarak mahallen merfûdur — her mahallî i'râbın alıştırdığı iki katmanlı okuyuşun kendisi.")]})

# ------------------------------------------------- s3 — law borrowed, the dalil
S.append({"id": "s3", "translation": {
 "en": "Would that you came to me and talked with me! (The fa-verb's nasb by a hidden an is the PROOF that this law is tamanni — that nasb never follows a conditional.)",
 "tr": "Keşke bana gelsen de benimle konuşsan! (Fâ fiilinin gizli bir en ile nasbı, bu لَوْ'in temennî olduğunun DELİLİdir — o nasb şarttan sonra asla gelmez.)"},
 "tokens": [
  tok("لَوْ","law","part",["insha-wa-tamanni","in-shartiyya"],
      "حَرْفُ تَمَنٍّ — وَالدَّلِيلُ نَصْبُ «فَتُحَدِّثَنِي» بِأَنْ مُضْمَرَةٍ.",
      "«would that» — لَوْ borrowed for the WISH, and the page itself proves the borrowing: the fa-verb two words on wears nasb by a hidden أَنْ, and a mudari's nasb after the fa never follows a conditional — it follows one of the six talab things. The conditional frame stands down.",
      "«keşke» — TEMENNÎ için ödünç alınmış لَوْ; ödüncü sayfanın kendisi ispat eder: iki kelime ilerideki fâ fiili gizli bir أَنْ ile nasb taşır ve fâ'dan sonra muzârinin nasbı şarttan sonra asla gelmez — altı talep şeyinden birinden sonra gelir. Şart çatısı geri çekilir."),
  tok("تَأْتِينِي","ata","verb",["insha-wa-tamanni","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالنُّونُ لِلْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«you come to me» — the wished act, a marfu' mudari (the wish itself does not govern it); the nun is the nun of protection and the speaker's ya its maf'ul bihi.",
      "«bana gelsen» — temennî edilen fiil, merfû muzâri (temennînin kendisi onu amel etmez); nûn vikāye nûnu, mütekellim yâsı mef'ûlün bihtir.",
      segments=[seg("تَأْتِي","ata","verb"), seg("نِي","pron-1s","pron")]),
  tok("فَتُحَدِّثَنِي","haddatha","verb",["insha-wa-tamanni","an-masdariyya"],
      "الْفَاءُ سَبَبِيَّةٌ وَالْمُضَارِعُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ وُجُوبًا.",
      "«and talked with me» — the FA SABABIYYA: what follows is the fruit of what was wished. The mudari after it is MANSUB by an obligatorily hidden أَنْ — the fatha on the tha is the receipt — and that construction follows tamanni and its five talab siblings, never a shart. This one fatha is the whole dalil.",
      "«de benimle konuşsan» — SEBEBİYYE FÂSI: ardındaki, dilenenin meyvesidir. Ondan sonraki muzâri, vücûben gizli bir أَنْ ile MANSUBdur — sâ'daki fetha makbuzdur — ve bu yapı temennî ile beş talep kardeşinden sonra gelir, şarttan sonra asla. Bütün delil bu tek fethadır.",
      segments=[seg("فَ","fa","part"), seg("تُحَدِّثَ","haddatha","verb"), seg("نِي","pron-1s","pron")],
      punct=".")],
 "jumal": [
  J("لَوْ تَأْتِينِي فَتُحَدِّثَنِي",
    "لَوْ لِلتَّمَنِّي — وَالدَّلِيلُ نَصْبُ الْمُضَارِعِ بَعْدَ الْفَاءِ.",
    "LAW FOR THE WISH, argued from the surface: nasb by a hidden an happens after six things — tamanni among them — and never after a shart. Since the fa-verb IS mansub, the law cannot be conditional; the fitting reading left standing is tamanni. The source's own istidlal, complete on three words.",
    "TEMENNÎ لَوْ'i — delili yüzeyden: gizli en ile nasb altı şeyden sonra olur — temennî onlardandır — ve şarttan sonra asla. Fâ fiili mansub OLDUĞUNA göre bu لَوْ şart olamaz; ayakta kalan uygun okuyuş temennîdir. Kaynağın kendi istidlâli, üç kelimede tamam."),
  J("فَتُحَدِّثَنِي",
    "الْفَاءُ السَّبَبِيَّةُ: مَا بَعْدَهَا مُسَبَّبٌ عَمَّا قَبْلَهَا.",
    "The FA SABABIYYA names the causal chain: the talking would flow from the coming. The an + verb melt into a masdar coordinated to a masdar understood from the wish — the classical taqdir behind the fatha.",
    "SEBEBİYYE FÂSI illiyet zincirini adlandırır: konuşma, gelmeden doğacaktır. En + fiil bir masdara erir ve temennîden anlaşılan bir masdara atfedilir — fethanın ardındaki klasik takdir budur.")]})

# ------------------------------------------------- s4 — tandim (madi)
S.append({"id": "s4", "translation": {
 "en": "If only you had honoured Zayd! (halla before a MADI is tandim — making the addressee regret what he left undone.)",
 "tr": "Keşke Zeyd'e ikram etseydin! (Mâzîden önce هَلَّا tendîmdir — muhâtabı yapmadığına pişman etmek.)"},
 "tokens": [
  tok("هَلَّا","halla","part",["insha-wa-tamanni","huruf-tanbih"],
      "حَرْفُ تَنْدِيمٍ — مُرَكَّبٌ عِنْدَ السَّكَّاكِيِّ مِنْ «هَلْ» وَ«لَا» الزَّائِدَةِ الْمُضَمَّنَةِ مَعْنَى التَّمَنِّي.",
      "«if only you had…!» — ONE particle: Sakkaki reads it as hal compounded with a zaida la that drank tamanni's meaning, which is why a madi after it yields TANDIM — reproach for the thing left undone. The peel must never split it into a question-hamza's family.",
      "«keşke …-saydın!» — TEK edat: Sekkâkî onu, temennî mânâsı içirilmiş zâid bir lâ ile birleşmiş هَلْ diye okur; mâzî ardında TENDÎM (yapılmayana sitem) vermesi bundandır. Ayrıştırıcı onu asla soru hemzesi ailesine bölmemelidir."),
  tok("أَكْرَمْتَ","akrama","verb",["insha-wa-tamanni"],
      "فِعْلٌ مَاضٍ — وَمُضِيُّهُ هُوَ الَّذِي جَعَلَ الْحَرْفَ لِلتَّنْدِيمِ.",
      "«you had honoured» — a MADI, and its pastness is the whole switch: what is already past cannot be urged, only regretted, so the particle reads tandim.",
      "«ikram etseydin» — MÂZÎ; ve edatı çeviren düğme onun geçmişliğidir: geçmiş olan artık teşvik edilemez, ancak pişmanlık duyulur — edat bu yüzden tendîm okur."),
  tok("زَيْدًا","zayd","propn",["insha-wa-tamanni"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«Zayd» — the maf'ul bihi, mansub.",
      "«Zeyd'i» — mef'ûlün bih, mansub.",
      punct=".")],
 "jumal": [
  J("هَلَّا أَكْرَمْتَ زَيْدًا",
    "التَّنْدِيمُ: تَوْبِيخُ الْمُخَاطَبِ عَلَى تَرْكِ الْفِعْلِ فِي الْمَاضِي.",
    "TANDIM: the speaker's aim is to make the addressee REGRET the omission — the act lay in his power and he left it. A wish-shaped rebuke, aimed backward.",
    "TENDÎM: konuşanın maksadı, muhâtabı yapmadığına PİŞMAN etmektir — fiil elindeydi ve bıraktı. Geriye dönük, dilek kılığında bir azar."),
  J("هَلَّا أَكْرَمْتَ زَيْدًا",
    "عِنْدَ السَّكَّاكِيِّ: «هَلْ» أَوْ «لَوْ» + «مَا/لَا» زَائِدَةٌ مُضَمَّنَةٌ مَعْنَى التَّمَنِّي.",
    "Sakkaki's derivation covers the whole family at once — هَلَّا، أَلَّا، لَوْلَا، لَوْمَا are hal/law wearing a tamanni-laden extra ma/la, which is why all four give tandim with a madi and tahdid with a mudari.",
    "Sekkâkî'nin türetmesi bütün aileyi birden kapsar — هَلَّا، أَلَّا، لَوْلَا، لَوْمَا, temennî yüklü zâid mâ/lâ giymiş hel/lev'dir; dördünün de mâzî ile tendîm, muzâri ile tahzîz vermesi bundandır.")]})

# ------------------------------------------------- s5 — tahdid (mudari)
S.append({"id": "s5", "translation": {
 "en": "Why don't you stand? (The same particle before a MUDARI is tahdid — urging the act on.)",
 "tr": "Kalksana! (Aynı edat MUZÂRİ önünde tahzîzdir — fiile teşvik.)"},
 "tokens": [
  tok("هَلَّا","halla","part",["insha-wa-tamanni","huruf-tanbih"],
      "حَرْفُ تَحْضِيضٍ — وَالْفَيْصَلُ زَمَنُ الْفِعْلِ بَعْدَهُ.",
      "«why don't you…?» — the SAME particle as s4, and the verb's TENSE is the entire divider: a mudari can still be done, so the particle spurs instead of reproaching.",
      "«…-sana!» — s4'teki edatın AYNISI; bölen, ardındaki fiilin ZAMANIdır: muzâri hâlâ yapılabilir — edat bu yüzden sitem değil teşvik eder."),
  tok("تَقُومُ","qama","verb",["insha-wa-tamanni","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَاسْتِقْبَالُهُ هُوَ الَّذِي جَعَلَ الْحَرْفَ لِلتَّحْضِيضِ.",
      "«you stand» — a marfu' mudari; its openness to the future flips the particle to TAHDID: the act can still happen, so it is urged.",
      "«kalkarsın» — merfû muzâri; istikbâle açıklığı edatı TAHZÎZe çevirir: fiil hâlâ olabilir, öyleyse teşvik edilir.",
      punct=".")],
 "jumal": [
  J("هَلَّا تَقُومُ",
    "التَّحْضِيضُ: طَلَبُ الْفِعْلِ بِحَثٍّ وَإِزْعَاجٍ.",
    "TAHDID: asking for the act with a push — sharper than a plain amr, softer than a threat. The mudari is what licenses it: only the still-possible can be urged.",
    "TAHZÎZ: fiili dürterek istemek — yalın emirden keskin, tehditten yumuşak. Ruhsatı muzâridir: ancak hâlâ mümkün olan teşvik edilir."),
  J("هَلَّا تَقُومُ",
    "زَمَنُ الْفِعْلِ هُوَ الْمُشَاهَدُ الْوَاحِدُ الْفَاصِلُ بَيْنَ التَّنْدِيمِ وَالتَّحْضِيضِ.",
    "One observable splits the pair: s4 and s5 share their particle letter for letter, and only the tense after it decides — madi = tandim, mudari = tahdid. The closed-class method the app has used since مِنْ/مَنْ, here inside balagha itself.",
    "Çifti TEK gözlemlenebilir ayırır: s4 ile s5 edatı harfi harfine paylaşır; karar yalnız ardındaki zamandadır — mâzî = tendîm, muzâri = tahzîz. Uygulamanın مِنْ/مَنْ'den beri kullandığı kapalı-sınıf yöntemi, bu kez belâgatin içinde.")]})

# ------------------------------------------------- s6 — la'alla with layta's hukm
S.append({"id": "s6", "translation": {
 "en": "Would that I could make the pilgrimage and visit you! (la'alla's hope, spoken of a REMOTE thing, is given layta's hukm — and the nasb of the fa-verb is again the receipt.)",
 "tr": "Keşke hac edebilsem de seni ziyaret etsem! (Uzak bir şey için söylenen لَعَلَّ ümidine لَيْتَ hükmü verilir — fâ fiilinin nasbı yine makbuzdur.)"},
 "tokens": [
  tok("لَعَلِّي","laalla","part",["insha-wa-tamanni","khabar-insha"],
      "حَرْفُ تَرَجٍّ أُجْرِيَ مُجْرَى لَيْتَ — وَالْيَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.",
      "«would that I» — la'alla, whose asl is TARAJJI (hope for the attainable); the hajj stands remote from the speaker, so the particle is run layta's course. The clinging ya is its ism in the position of nasb.",
      "«keşke ben» — aslı TERECCÎ (ulaşılabilire ümit) olan لَعَلَّ; hac, konuşana uzak durduğundan edat لَيْتَ mecrâsına akıtılır. Bitişik yâ, nasb mahallinde onun ismidir.",
      segments=[seg("لَعَلَّ","laalla","part"), seg("ي","pron-1s","pron")]),
  tok("أَحُجُّ","hajja","verb",["insha-wa-tamanni","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ لَعَلَّ.",
      "«I make the pilgrimage» — a marfu' mudari (the doubled jim carries its shadda whole); the clause is la'alla's khabar in the position of raf'.",
      "«hac ederim» — merfû muzâri (şeddeli cîm bütün taşınır); cümle, ref' mahallinde لَعَلَّ'nin haberidir."),
  tok("فَأَزُورَكَ","zara","verb",["insha-wa-tamanni","an-masdariyya"],
      "الْفَاءُ سَبَبِيَّةٌ وَالْمُضَارِعُ مَنْصُوبٌ بِأَنْ مُضْمَرَةٍ — وَنَصْبُهُ دَلِيلُ التَّمَنِّي.",
      "«and visit you» — the fa sababiyya again, the mudari mansub by the hidden an, the kaf its maf'ul bihi. The fatha on the ra is the WITNESS that this la'alla got layta's hukm: after a plain tarajji the books do not give the fa this nasb.",
      "«de seni ziyaret edeyim» — yine sebebiyye fâsı; muzâri gizli en ile mansub, kâf mef'ûlün bih. Râ'daki fetha, bu لَعَلَّ'ye لَيْتَ hükmü verildiğinin ŞÂHİDİdir: yalın tereccîden sonra kitaplar fâ'ya bu nasbı vermez.",
      segments=[seg("فَ","fa","part"), seg("أَزُورَ","zara","verb"), seg("كَ","pron-2ms","pron")],
      punct=".")],
 "jumal": [
  J("لَعَلِّي أَحُجُّ فَأَزُورَكَ",
    "لَعَلَّ بِمَنْزِلَةِ لَيْتَ — لِبُعْدِ الْمَرْجُوِّ.",
    "LA'ALLA AT LAYTA'S RANK: hope's particle, aimed at a thing too far for hope, becomes a wish — and the grammar follows the heart, giving the fa-verb the nasb that only the talab six license.",
    "لَيْتَ MENZİLESİNDE لَعَلَّ: ümidin edatı, ümide fazla uzak bir şeye yönelince dilek olur — ve gramer kalbi izler: fâ fiiline yalnız altı talebin ruhsat verdiği nasbı verir."),
  J("لَعَلِّي أَحُجُّ فَأَزُورَكَ",
    "حَدُّ التَّرَجِّي وَالتَّمَنِّي: الْمُمْكِنُ الْقَرِيبُ يُرْجَى، وَالْبَعِيدُ أَوِ الْمُسْتَحِيلُ يُتَمَنَّى.",
    "The tarajji/tamanni border drawn once: the near-possible is HOPED for, the remote or impossible is WISHED for — and the border shows on the page only through the fa-verb's ending, which is why this sentence and s3 close the chapter as a pair.",
    "Tereccî/temennî sınırı bir kez çizilir: yakın-mümkün ÜMİT edilir, uzak yahut muhâl TEMENNÎ edilir — ve sınır sayfada yalnız fâ fiilinin sonunda görünür; bu cümle ile s3'ün bâbı çift olarak kapatması bundandır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # copies — a lex key is GLOBAL: entries copied verbatim from their home package
 "ada-return": copy_gloss("kitab-al-sulh", "ada-return"),
 "zara":       copy_gloss("wasiyyat-abi-hanifa-samti", "zara"),
 "shabab":     copy_gloss("wasiyyat-abi-yusuf-l5", "shabab"),
 "laalla":     copy_gloss("bad-al-amali", "laalla"),
 # NEW this chapter
 "layta": g("لَيْتَ", None, "part", "would that…! (the wish particle, inna's sister)",
            "keşke (temennî edatı; inne'nin kızkardeşi)", 3),
 "halla": g("هَلَّا", None, "part",
            "if only you had…! / why don't you…? (tandim with a madi, tahdid with a mudari)",
            "keşke …-saydın! / …-sana! (mâzî ile tendîm, muzâri ile tahzîz)", 5),
 "shafi": g("شَفِيع", "ش ف ع", "noun", "intercessor", "şefaatçi", 3, plural="شُفَعَاء"),
 "hajja": g("حَجَّ", "ح ج ج", "verb", "to make the pilgrimage", "hac etmek", 2, form="I"),
 "haddatha": g("حَدَّثَ", "ح د ث", "verb", "to talk to, tell, relate", "konuşmak, anlatmak", 2, form="II"),
}

# ---------------------------------------------------------------- morphology
def build_morph():
    out = {}
    sulh = json.loads((ROOT / "content/samples/kitab-al-sulh/morphology.json").read_text(encoding="utf-8"))["verbs"]
    samti = json.loads((ROOT / "content/samples/wasiyyat-abi-hanifa-samti/morphology.json").read_text(encoding="utf-8"))["verbs"]
    out["ada-return"] = sulh["ada-return"]
    out["zara"] = samti["zara"]
    # حَجَّ يَحُجُّ — geminate of bab nasara, on the صَحَّ template: the merge
    # holds while the twin stays vowelled (حَجَّ، يَحُجُّ) and breaks before a
    # sukun-initial ending (حَجَجْتَ); jazm bil-fath with the fakk allowed.
    out["hajja"] = _sg.idgham(_sg.entry(
        _sg.BABS["nasara"][0] + " — مُضَاعَفٌ", _sg.BABS["nasara"][1], "حَجّ", "حَاجّ",
        _sg.mazi14("حَجّ", "حَجَج"), _sg.mudari14("َ", "حُجّ", "حْجُج"),
        ["حُجَّ", "حُجَّا", "حُجُّوا", "حُجِّي", "حُجَّا", "اُحْجُجْنَ"],
        "يَحُجَّ", "يَحُجَّ", "تَحُجَّ",
        note="مُضَاعَفٌ مِنْ بَابِ نَصَرَ: الْجَزْمُ بِالْفَتْحِ وَيَجُوزُ الْفَكُّ — لَمْ يَحُجَّ / لَمْ يَحْجُجْ."))
    out["haddatha"] = _sg.derived("بَابُ التَّفْعِيلِ: فَعَّلَ يُفَعِّلُ", "فَعَّلَ يُفَعِّلُ", "ُ",
        "حَدَّث", "حَدِّث", "حَدِّث", "تَحْدِيث", "مُحَدِّث",
        maful="مُحَدَّث", pmz="حُدِّثَ", pmd="يُحَدَّثُ",
        note="مَجْهُولُ الْمَاضِي: ضَمُّ الْأَوَّلِ وَكَسْرُ مَا قَبْلَ الْآخِرِ — حُدِّثَ.")
    return out

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/23.json").write_text(
    json.dumps({"chapter": 23, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 23 for c in man["chapters"]):
    man["chapters"].append({"n": 23, "title": TITLE23})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.23.0"
ADD_EN = (" Chapter 23 opens the insha bab from the same file (lines ~1945-1990, sahifa 68-69): every "
          "sentence is the source's own worked example quoted verbatim — لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا, "
          "هَلْ لِي مِنْ شَفِيعٍ, لَوْ تَأْتِينِي فَتُحَدِّثَنِي, هَلَّا أَكْرَمْتَ زَيْدًا, هَلَّا تَقُومُ, "
          "لَعَلِّي أَحُجُّ فَأَزُورَكَ — with the Ottoman plain-alif spellings (لِى) normalized to standard "
          "orthography, a recorded normalization.")
ADD_TR = (" Yirmi üçüncü bâb, aynı dosyadan inşâ bâbını açar (satır ~1945-1990, sahife 68-69): her cümle "
          "kaynağın kendi işlenmiş örneğinin aynen alınmışıdır — لَيْتَ الشَّبَابَ يَعُودُ يَوْمًا, هَلْ لِي مِنْ "
          "شَفِيعٍ, لَوْ تَأْتِينِي فَتُحَدِّثَنِي, هَلَّا أَكْرَمْتَ زَيْدًا, هَلَّا تَقُومُ, لَعَلِّي أَحُجُّ فَأَزُورَكَ — "
          "Osmanlı düz-elif imlâsı (لِى) standart imlâya çevrilmiştir; kayıtlı bir normalizasyondur.")
if "1945-1990" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch23:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
