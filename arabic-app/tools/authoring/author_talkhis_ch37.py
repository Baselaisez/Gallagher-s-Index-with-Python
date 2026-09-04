# -*- coding: utf-8 -*-
"""Author chapter 37 of talkhis-al-miftah — الْجِهَةُ الْوَهْمِيَّةُ وَالْخَيَالِيَّةُ.

Sahifa 85-86 (lines ~2470-2492): Sakkaki's remaining two kinds of the
jihat jamia, and the wasl-beautifiers that close the bab:

  • WAHMI — the estimative faculty builds the closeness:
    - shibh tamathul: the wahm presents white and yellow as likes, so
      Muhammad b. Wuhayb's madh of the caliph al-Mu'tasim gathers three
      things beautifully: ثَلَاثَةٌ تُشْرِقُ الدُّنْيَا بِبَهْجَتِهَا •
      شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ (the bayt stands
      WHOLE in chapter 19, where the fronted-musnad bab read it; this
      chapter splits it at the hemistich because the LIST is the lesson
      — the recorded-reuse precedent).
    - tadad: اَبُو جَهْلٍ كَافِرٌ وَابْنُهُ مُؤْمِنٌ — belief against
      unbelief in the musnads, father and son in the musnad-ilayhs.
    - shibh tadad: اَلسَّمَاءُ مَرْفُوعَةٌ وَالْاَرْضُ مُنْحَطَّةٌ — the
      wahm lowers tadad and its semblance to the RANK of tadayuf: a
      thing is found quickest in the heart beside its opposite.
  • KHAYALI — a closeness already settled in the imagination by 'urf
    and 'ada (taught in the note; it varies by custom, so the source
    gives it no fixed witness).
  • The WASL-BEAUTIFIERS: agreement in ismiyya/fi'liyya (and in
    mazi/mudari) beautifies the joining — UNLESS a mani': in
    قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ the mismatch is DELIBERATE, huduth
    meant of the one and thubut of the other.

ATTRIBUTION: s1-s2 are Muhammad b. Wuhayb's bayt exactly as the source
cites it (also standing whole in chapter 19 — a recorded reuse; the
source's Ottoman إِسْحَق is written إِسْحَاق as chapter 19 already
prints it — recorded normalization); s3-s5 are the source's own worked
examples, verbatim.

Grammar this chapter teaches:
  • note 140 gains its three WAHMI witnesses (AR-keyed dedupe — the
    ch33 lesson: sentence ids restart every chapter).
  • note 141 `muhassin-al-wasl` — the beautifiers and their mani':
    likeness of FORM serves the joining only while the MEANING wants
    the forms alike.
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

TITLE37 = {"ar": "الْجِهَةُ الْوَهْمِيَّةُ وَالْخَيَالِيَّةُ — وَمُحَسِّنَاتُ الْوَصْلِ",
           "en": "The Estimative and Imaginal Aspects — and the Wasl's Beautifiers",
           "tr": "Vehmî ve Hayâlî Cihet — ve Vaslın Güzelleştiricileri"}

# ------------------- s1 — the Wuhayb bayt, first hemistich: three that shine
S.append({"id": "s1", "translation": {
 "en": "Three there are by whose splendour the world is lit —",
 "tr": "Üç şey vardır ki dünya onların güzelliğiyle aydınlanır —"},
 "tokens": [
  tok("ثَلَاثَةٌ","thalatha","noun",["tawassut-bayna-al-kamalayn","taqdim-al-musnad"],
      "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ — قُدِّمَ لِلتَّشْوِيقِ إِلَى الْمُسْنَدِ إِلَيْهِ.",
      "«three» — the fronted khabar (chapter 19 read this very bayt for that fronting); the delay makes the hearer wait for WHICH three.",
      "«üç» — öne alınmış haber (19. bâb bu beyti tam bu takdîm için okumuştu); erteleme, dinleyeni HANGİ üç diye bekletir."),
  tok("تُشْرِقُ","ashraqa","verb",["tawassut-bayna-al-kamalayn"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِفَةٌ لِثَلَاثَةٌ.",
      "«is lit» — the Form IV mudari; the clause is a sifa on the three.",
      "«aydınlanır» — IV. bâbdan muzâri; cümle, üçün sıfatıdır."),
  tok("الدُّنْيَا","dunya","noun",["tawassut-bayna-al-kamalayn","ism-maqsur-manqus"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«the world» — the doer, its damma estimated on the maqsur alif.",
      "«dünya» — fâil; dammesi maksûr elif üzerinde takdîrî."),
  tok("بِبَهْجَتِهَا","bahja","noun",["tawassut-bayna-al-kamalayn"],
      "جَارٌّ وَمَجْرُورٌ، وَ«هَا» عَائِدَةٌ عَلَى الثَّلَاثَةِ.",
      "«by their splendour» — the jarr phrase; the «ha» points back at the three.",
      "«güzellikleriyle» — câr-mecrûr; «هَا» üçe döner.",
      punct="•", segments=[seg("بِ","bi","part"), seg("بَهْجَتِ","bahja","noun"), seg("هَا","pron-3fs","pron")])],
 "jumal": [
  J("ثَلَاثَةٌ تُشْرِقُ الدُّنْيَا بِبَهْجَتِهَا",
    "جُمْلَةٌ اسْمِيَّةٌ قُدِّمَ خَبَرُهَا — وَجُمْلَةُ الصِّفَةِ فِي مَحَلِّ رَفْعٍ.",
    "The promise: three things, held back for one hemistich — the fronting chapter 19 taught, now serving the wahmi list to come.",
    "Vaad: bir mısra boyunca bekletilen üç şey — 19. bâbın öğrettiği takdîm, şimdi gelecek vehmî listeye hizmet ediyor."),
  J("تُشْرِقُ الدُّنْيَا بِبَهْجَتِهَا",
    "جُمْلَةٌ فِعْلِيَّةٌ صِفَةٌ لِثَلَاثَةٌ.",
    "The sifa clause that lets a nakira stand as mubtada-material.",
    "Nekireyi mübtedâlığa yaklaştıran sıfat cümlesi.")]})

# --------- s2 — the second hemistich: the LIST the wahm gathers as likes
S.append({"id": "s2", "translation": {
 "en": "— the morning sun, Abu Ishaq, and the moon. (SHIBH TAMATHUL: the wahm presents caliph and luminaries as likes, so gathering them under one waw is beautiful.)",
 "tr": "— kuşluk güneşi, Ebû İshâk ve ay. (ŞİBH-İ TEMÂSÜL: vehim, halifeyle iki ışık kaynağını birbirinin dengi gibi gösterir; onları tek vâv altında toplamak bu yüzden güzeldir.)"},
 "tokens": [
  tok("شَمْسُ","shams","noun",["tawassut-bayna-al-kamalayn"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the sun» — the delayed mubtada arrives at last, a mudaf.",
      "«güneşi» — ertelenmiş mübtedâ nihayet gelir; muzâftır."),
  tok("الضُّحَى","duha","noun",["tawassut-bayna-al-kamalayn","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.",
      "«of the morning» — the mudaf ilayh, its kasra estimated on the maqsur alif.",
      "«kuşluğun» — muzâfun ileyh; kesresi maksûr elif üzerinde takdîrî."),
  tok("وَأَبُو","ab","noun",["tawassut-bayna-al-kamalayn","five-nouns"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَبُو» مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ.",
      "«and Abu» — joined; a five-nouns head showing its raf' by the WAW. The caliph stands BETWEEN the two luminaries — the wahm's likeness, written into the word order.",
      "«ve Ebû» — atfedilmiş; ref'ini VÂV ile gösteren beş isimden. Halife iki ışığın ARASINDA durur — vehmin temâsülü, kelime dizimine yazılmış.",
      segments=[seg("وَ","wa","part"), seg("أَبُو","ab","noun")]),
  tok("إِسْحَاقَ","ishaq","propn",["tawassut-bayna-al-kamalayn","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
      "«Ishaq» — the mudaf ilayh in jarr by a FATHA: barred from tanwin as a foreign proper name (al-Mu'tasim's kunya).",
      "«İshâk'ın» — fetha ile mecrur muzâfun ileyh: yabancı özel ad olarak tenvinden men'li (Mu'tasım'ın künyesi)."),
  tok("وَالْقَمَرُ","qamar","noun",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْقَمَرُ» مَعْطُوفٌ مَرْفُوعٌ — وَالْجِهَةُ الْجَامِعَةُ شِبْهُ التَّمَاثُلِ عِنْدَ الْوَهْمِ.",
      "«and the moon» — the third of the three, joined: sun, caliph and moon share no aqli bond, but the WAHM shows them as one kind of shining thing, and that estimative likeness licenses the waws.",
      "«ve ay» — üçün üçüncüsü, atfedilmiş: güneş, halife ve ay aklî bağ taşımaz; ama VEHİM üçünü tek tür parlayan şey gibi gösterir ve o vehmî benzerlik vâvları meşru kılar.",
      punct="•", segments=[seg("وَ","wa","part"), seg("الْقَمَرُ","qamar","noun")])],
 "jumal": [
  J("شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ",
    "الْمُبْتَدَأُ الْمُؤَخَّرُ وَمَعْطُوفَاهُ — الْجِهَةُ الْجَامِعَةُ وَهْمِيَّةٌ: شِبْهُ التَّمَاثُلِ.",
    "The list itself is the lesson: three unlikes the wahm gathers as likes — which is exactly why the madh works.",
    "Listenin kendisi derstir: vehmin denk diye topladığı üç farklı şey — methin işlemesi tam bundandır."),
  J("وَأَبُو إِسْحَاقَ",
    "مَعْطُوفٌ بَيْنَ الشَّمْسِ وَالْقَمَرِ.",
    "The caliph seated between sun and moon — praise by position alone.",
    "Güneşle ay arasına oturtulmuş halife — yalnız konumla övgü.")]})

# ------------------------ s3 — tadad: belief and unbelief in one household
S.append({"id": "s3", "translation": {
 "en": "Abu Jahl is an unbeliever, and his son ('Ikrima) is a believer. (TADAD in the musnads, tadayuf in the musnad-ilayhs — opposites meet in the mind, so the waw is due.)",
 "tr": "Ebû Cehil kâfirdir, oğlu (İkrime) ise mümindir. (müsnedlerde TEZÂD, müsnedün-ileyhlerde tezâyüf — zıtlar zihinde buluşur, vâv hak olur.)"},
 "tokens": [
  tok("أَبُو","ab","noun",["tawassut-bayna-al-kamalayn","five-nouns"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ وَهُوَ مُضَافٌ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ.",
      "«Abu (father of)» — the five-nouns mubtada, raf' by the waw, a mudaf.",
      "«Ebû» — beş isimden mübtedâ; ref'i vâv iledir, muzâftır."),
  tok("جَهْلٍ","jahl","noun",["tawassut-bayna-al-kamalayn"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْكُنْيَةُ ذَمٌّ: أَبُو الْجَهْلِ نَفْسِهِ.",
      "«of Jahl» — the mudaf ilayh; a kunya that condemns: father of ignorance itself.",
      "«Cehl'in» — muzâfun ileyh; kınayan bir künye: cehaletin babası."),
  tok("كَافِرٌ","kafir","noun",["tawassut-bayna-al-kamalayn","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«an unbeliever» — the first khabar.",
      "«kâfir» — ilk haber."),
  tok("وَابْنُهُ","ibn","noun",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ، وَابْنُ مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
      "«and his son» — the joined second mubtada ('Ikrima, who embraced Islam after the conquest), the pronoun annexed.",
      "«ve oğlu» — bağlanmış ikinci mübtedâ (fetihten sonra Müslüman olan İkrime); zamir muzâfun ileyh.",
      segments=[seg("وَ","wa","part"), seg("ابْنُ","ibn","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مُؤْمِنٌ","mumin","noun",["tawassut-bayna-al-kamalayn","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — وَالْجِهَةُ الْجَامِعَةُ التَّضَادُّ بَيْنَ الْمُسْنَدَيْنِ مَعَ تَضَايُفِ الْمُسْنَدِ إِلَيْهِمَا.",
      "«a believer» — the second khabar. Kufr against iman in the predicates, father against son in the subjects: BOTH seats hold their jiha, and the waw stands firm.",
      "«mümin» — ikinci haber. Yüklemlerde küfre karşı iman, öznelerde babaya karşı oğul: İKİ makam da cihetini tutar ve vâv sapasağlam durur.",
      punct=".")],
 "jumal": [
  J("أَبُو جَهْلٍ كَافِرٌ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ.",
    "The father's sentence.",
    "Babanın cümlesi."),
  J("وَابْنُهُ مُؤْمِنٌ",
    "مَعْطُوفَةٌ — تَضَادُّ الْمُسْنَدَيْنِ وَتَضَايُفُ الْمُسْنَدِ إِلَيْهِمَا.",
    "Joined across the starkest tadad the sira offers — and the mind holds the pair as one household.",
    "Siyerin sunduğu en keskin tezâd üzerinden bağlı — ve zihin, çifti tek hane olarak tutar.")]})

# -------------------- s4 — shibh tadad: heaven raised and earth laid low
S.append({"id": "s4", "translation": {
 "en": "The heaven is raised high and the earth is laid low. (SHIBH TADAD: not true opposites — but the wahm lowers opposition and its semblance to the rank of tadayuf, and a thing is found quickest beside its counterpart.)",
 "tr": "Gök yükseltilmiştir, yer ise alçaktır. (ŞİBH-İ TEZÂD: gerçek zıtlar değil — fakat vehim, zıddı ve benzerini tezâyüf mertebesine indirir; bir şey en çabuk karşılığının yanında bulunur.)"},
 "tokens": [
  tok("السَّمَاءُ","sama","noun",["tawassut-bayna-al-kamalayn"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«the heaven» — the first mubtada.",
      "«gök» — ilk mübtedâ."),
  tok("مَرْفُوعَةٌ","marfua","noun",["tawassut-bayna-al-kamalayn","ism-maful"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ رَفَعَ.",
      "«raised» — the khabar, an ism maf'ul: raised BY its Maker.",
      "«yükseltilmiş» — haber; ism-i mef'ûl: Yaratanı tarafından yükseltilmiş."),
  tok("وَالْأَرْضُ","ard","noun",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ، وَالْأَرْضُ مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.",
      "«and the earth» — the joined second mubtada.",
      "«ve yer» — bağlanmış ikinci mübtedâ.",
      segments=[seg("وَ","wa","part"), seg("الْأَرْضُ","ard","noun")]),
  tok("مُنْحَطَّةٌ","munhatta","noun",["tawassut-bayna-al-kamalayn","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ انْحَطَّ، وَالْجِهَةُ شِبْهُ التَّضَادِّ عِنْدَ الْوَهْمِ.",
      "«laid low» — the second khabar (Form VII participle of a geminate). Heaven and earth are not black-and-white opposites — the wahm merely SEATS them so, and that estimative opposition is jiha enough.",
      "«alçalmış» — ikinci haber (muzâaf VII. bâbın ism-i fâili). Gökle yer siyah-beyaz gibi gerçek zıt değildir — vehim onları öyle OTURTUR ve o vehmî zıtlık cihet olarak yeter.",
      punct=".")],
 "jumal": [
  J("السَّمَاءُ مَرْفُوعَةٌ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ.",
    "The height.",
    "Yükseklik."),
  J("وَالْأَرْضُ مُنْحَطَّةٌ",
    "مَعْطُوفَةٌ — شِبْهُ التَّضَادِّ يَنْزِلُ مَنْزِلَةَ التَّضَايُفِ.",
    "Joined by the semblance: you recall a thing fastest beside its counterpart — the wahm's own arithmetic, and the source says exactly that.",
    "Benzerlikle bağlı: bir şeyi en hızlı karşılığının yanında hatırlarsın — vehmin kendi hesabı; kaynak tam bunu söyler.")]})

# ------------- s5 — the beautifier and its mani': deliberate form-mismatch
S.append({"id": "s5", "translation": {
 "en": "Zayd stood up — and 'Amr is seated. (the beautifier: matching ismiyya to ismiyya adorns a wasl. HERE the mismatch is deliberate: an EVENT is meant of Zayd, a STATE of 'Amr.)",
 "tr": "Zeyd kalktı — Amr ise oturmaktadır. (güzelleştirici: isim cümlesini isim cümlesine denk getirmek vaslı süsler. BURADA uyumsuzluk kasıtlıdır: Zeyd'den HUDÛS, Amr'dan SÜBUT kastedilir.)"},
 "tokens": [
  tok("قَامَ","qama","verb",["muhassin-al-wasl"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — وَاخْتِيرَ الْفِعْلُ لِإِفَادَةِ الْحُدُوثِ.",
      "«stood up» — a mazi, CHOSEN as a verb because a verb says something HAPPENED.",
      "«kalktı» — mâzî; fiil SEÇİLMİŞTİR, çünkü fiil bir şeyin OLDUĞUNU söyler."),
  tok("زَيْدٌ","zayd","propn",["muhassin-al-wasl"],
      "فَاعِلٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«Zayd» — the doer of the event.",
      "«Zeyd» — hâdisenin fâili."),
  tok("وَعَمْرٌو","amr-alam","propn",["muhassin-al-wasl"],
      "الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and 'Amr» — joined, but as a MUBTADA: the second half goes nominal on purpose.",
      "«ve Amr» — bağlanmış, fakat MÜBTEDÂ olarak: ikinci yarı bilerek isim cümlesine geçer.",
      segments=[seg("وَ","wa","part"), seg("عَمْرٌو","amr-alam","propn")]),
  tok("قَاعِدٌ","qaid","noun",["muhassin-al-wasl","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ يُفِيدُ الثُّبُوتَ، فَالْمُخَالَفَةُ مَقْصُودَةٌ.",
      "«seated» — an ism fa'il, because a noun says something IS. Matching the shapes would have beautified the wasl; here the speaker WANTS event against state, and the mani' outranks the ornament.",
      "«oturmaktadır» — ism-i fâil, çünkü isim bir şeyin ÖYLE OLDUĞUNU söyler. Şekilleri denkleştirmek vaslı süslerdi; burada konuşan hâdiseye karşı sübut İSTER ve mâni', süsten önce gelir.",
      punct=".")],
 "jumal": [
  J("قَامَ زَيْدٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ — لِلْحُدُوثِ.",
    "The verbal half: something happened.",
    "Fiil yarısı: bir şey oldu."),
  J("وَعَمْرٌو قَاعِدٌ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — خُولِفَ الشَّكْلُ لِأَنَّ الْمَعْنَى أَرَادَ الثُّبُوتَ.",
    "The nominal half, joined: the forms disagree because the MEANINGS do — the beautifier yields to the intent.",
    "İsim yarısı, bağlı: şekiller ayrışır çünkü MÂNÂLAR ayrışır — güzelleştirici, kasta boyun eğer.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "jahl": copy_gloss("bad-al-amali", "jahl"),
 "kafir": copy_gloss("aqaid-ahl-al-sunna", "kafir"),
 "mumin": copy_gloss("aqaid-ahl-al-sunna", "mumin"),
 "sama": copy_gloss("aqaid-ahl-al-sunna", "sama"),
 "marfua": g("مَرْفُوعَة", "ر ف ع", "noun", "raised, lifted high (ism maf'ul)", "yükseltilmiş (ism-i mef'ûl)", 4),
 "munhatta": g("مُنْحَطَّة", "ح ط ط", "noun", "laid low, sunk down (Form VII ism fa'il)", "alçalmış, alçak duran (VII. bâb ism-i fâili)", 5),
 "qaid": g("قَاعِد", "ق ع د", "noun", "seated, sitting (ism fa'il)", "oturan, oturmakta (ism-i fâil)", 3),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/37.json").write_text(
    json.dumps({"chapter": 37, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 37 for c in man["chapters"]):
    man["chapters"].append({"n": 37, "title": TITLE37})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.37.0"
ADD_EN = (" Chapter 37 carries the wahmi and khayali jiha with the wasl-beautifiers (lines "
          "~2470-2492, sahifa 85-86): s1-s2 are Muhammad b. Wuhayb's bayt exactly as the "
          "source cites it — the bayt also stands whole in chapter 19, where the "
          "fronted-musnad bab read it (a recorded reuse), and the source's Ottoman إِسْحَق is "
          "written إِسْحَاق as chapter 19 already prints it; s3-s5 are the source's own "
          "worked examples, verbatim.")
ADD_TR = (" Otuz yedinci bâb vehmî ve hayâlî ciheti, vasl güzelleştiricileriyle taşır (satır "
          "~2470-2492, sahife 85-86): s1-s2 Muhammed b. Vüheyb'in beytidir — kaynağın iktibas "
          "ettiği şekliyle aynen; beyit, takdîm bâbının okuduğu 19. bâbda bütün hâliyle de "
          "durur (kayıtlı yeniden kullanım) ve kaynağın Osmanlı imlâlı إِسْحَق'ı, 19. bâbın "
          "bastığı gibi إِسْحَاق yazılmıştır; s3-s5 kaynağın kendi işlenmiş misalleridir, "
          "aynen.")
if "2470-2492" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------- note 140: the wahmi witnesses (AR-keyed dedupe)
GR = ROOT / "content/grammar"
n140p = GR / "tawassut-bayna-al-kamalayn.json"
n140 = json.loads(n140p.read_text(encoding="utf-8"))
have = {(e.get("sourceStory"), e.get("sentence"), e.get("ar")) for e in n140.get("examples", [])}
for ex in [
  {"ar": "شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ",
   "en": "WAHMI, shibh tamathul: the caliph gathered between two luminaries.",
   "tr": "VEHMÎ, şibh-i temâsül: iki ışık arasına toplanmış halife.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "أَبُو جَهْلٍ كَافِرٌ وَابْنُهُ مُؤْمِنٌ",
   "en": "WAHMI, tadad: belief against unbelief in one household.",
   "tr": "VEHMÎ, tezâd: tek hanede imana karşı küfür.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "السَّمَاءُ مَرْفُوعَةٌ وَالْأَرْضُ مُنْحَطَّةٌ",
   "en": "WAHMI, shibh tadad: heaven and earth seated as opposites.",
   "tr": "VEHMÎ, şibh-i tezâd: zıt diye oturtulmuş gökle yer.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"}]:
    if (ex["sourceStory"], ex["sentence"], ex["ar"]) not in have:
        n140["examples"].append(ex)
n140p.write_text(json.dumps(n140, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 141
NOTE141 = {
 "id": "muhassin-al-wasl",
 "title": {"ar": "مُحَسِّنَاتُ الْوَصْلِ — وَمَانِعُهَا",
           "en": "The wasl's beautifiers — and what overrules them",
           "tr": "Vaslın güzelleştiricileri — ve onları geçen mâni'"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — تحسين الوصل"],
 "question": {
  "en": ["Are the two joined jumlas alike in kind — ismiyya with ismiyya, fi'liyya with fi'liyya, mazi with mazi? The likeness ADORNS the wasl.",
         "Does the meaning WANT them unlike — an event beside a state (قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ)? Then the mani' overrules the ornament."],
  "tr": ["Bağlanan iki cümle türce denk mi — isim isimle, fiil fiille, mâzî mâzîyle? Denklik vaslı SÜSLER.",
         "Mânâ onları farklı mı İSTİYOR — hâdise yanında sübut (قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ)? O zaman mâni', süsü geçer."]},
 "plain": {
  "en": "Once a wasl is licensed, likeness of FORM beautifies it: nominal beside nominal, verbal beside verbal, past beside past. But the ornament yields to intent — in قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ the mismatch is deliberate: an event is asserted of Zayd, a standing state of 'Amr.",
  "tr": "Vasl bir kez meşru olunca ŞEKİL denkliği onu güzelleştirir: isim yanında isim, fiil yanında fiil, mâzî yanında mâzî. Fakat süs kasta boyun eğer — قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ'da uyumsuzluk kasıtlıdır: Zeyd'den bir hâdise, Amr'dan duran bir hâl bildirilir."},
 "explanation": {
  "en": "THE BEAUTIFIERS: the two jumlas agreeing in ismiyya and fi'liyya, and — within the verbal — in mazi and mudari, is among what makes a wasl handsome; the ear hears one fabric. THE MANI': a likeness of form is only wanted while the MEANINGS are alike. In قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ the first half is verbal because HUDUTH (an event: he stood) is meant, the second nominal because THUBUT (a state: he is seated) is meant — matching the shapes would have flattened that very distinction, so the mismatch is the eloquence. Likewise زَيْدٌ قَامَ وَعَمْرٌو يَقْعُدُ keeps a mazi beside a mudari because a completed act is meant of the one and an ongoing one of the other. The ma'ani scholar needs the jihat jamia MORE than anyone — Sakkaki's own closing remark — and the khayali kind most of all, because it stands on nothing firmer than 'urf and 'ada: what custom has seated together in the imagination joins smoothly there and nowhere else.",
  "tr": "GÜZELLEŞTİRİCİLER: iki cümlenin isimlik-fiillikte, fiil cümlesi içinde de mâzî-muzârilikte uyuşması vaslı güzelleştirenlerdendir; kulak tek kumaş işitir. MÂNİ': şekil denkliği ancak MÂNÂLAR denkken istenir. قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ'da ilk yarı fiildir çünkü HUDÛS (bir hâdise: kalktı) kastedilir; ikincisi isimdir çünkü SÜBUT (bir hâl: oturmaktadır) kastedilir — şekilleri denkleştirmek tam o farkı silerdi; uyumsuzluk belâgatin kendisidir. Aynı şekilde زَيْدٌ قَامَ وَعَمْرٌو يَقْعُدُ, birinden bitmiş, ötekinden süren iş kastedildiği için mâzîyi muzâri yanında tutar. Meânî âliminin cihet-i câmiaya herkesten çok ihtiyacı vardır — Sekkâkî'nin kendi kapanış sözü — en çok da hayâlîsine; çünkü o, örf ve âdetten daha sağlam bir şeye dayanmaz: âdetin hayalde yan yana oturttuğu, orada pürüzsüz bağlanır, başka yerde bağlanmaz.",},
 "examples": [
  {"ar": "قَامَ زَيْدٌ وَعَمْرٌو قَاعِدٌ",
   "en": "the mani' at work: event of Zayd, state of 'Amr — the forms part on purpose.",
   "tr": "iş başındaki mâni': Zeyd'den hâdise, Amr'dan hâl — şekiller bilerek ayrışır.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«Bağlanan cümleler her zaman aynı türden olmalıdır»",
   "right": "«Denklik süstür, kural değil — mânâ farklı isterse şekil de farklılaşır»",
   "why": {"en": "Reading the beautifier as a rule would condemn the Qur'an's own يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ — fi'liyya joined to ismiyya, and perfectly: their deceit is an EVENT they keep attempting, His requital a standing STATE. The mismatch carries the theology.",
           "tr": "Güzelleştiriciyi kural okumak, Kur'ân'ın kendi يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ'unu mahkûm ederdi — isim cümlesine bağlanmış fiil cümlesi, hem de kusursuzca: onların aldatışı tekrarlanan bir HÂDİSE, O'nun karşılığı duran bir HÂLDİR. Uyumsuzluk, akideyi taşır."}}],
 "relatedNotes": ["al-fasl-wa-al-wasl", "tawassut-bayna-al-kamalayn", "mubtada-khabar", "anwa-al-jumal"]}

(GR / "muhassin-al-wasl.json").write_text(
    json.dumps(NOTE141, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch37:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; note 140 + 3 wahmi witnesses; note 141")
