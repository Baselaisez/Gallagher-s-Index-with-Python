# -*- coding: utf-8 -*-
"""Author chapter 6 of mukhtasar-al-manar — the four degrees of OBSCURITY.

Chapter 5 climbed: zahir, nass, mufassar, muhkam, each clearer than the last.
This chapter descends the other side of the same staircase — khafi, mushkil,
mujmal, mutashabih — and the matn signals the symmetry by using the very same
verb in the very same frame, اِزْدَادَ خَفَاءً where it said اِزْدَادَ وُضُوحًا. The
two chapters are one table, and reading them apart is reading them wrong.

ATTRIBUTION: like chapters 2–5, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • خَفَاءً beside chapter 5's وُضُوحًا — the same tamyiz slot filled by a MAMDUD
    noun, and the mamdud is the point: خَفَاءً takes its tanwin because its hamza
    is the root's own ya turned into one (خ ف ي), while صَحْرَاءُ, which ends in
    the same three letters, is barred from tanwin because ITS hamza is the alif
    of feminisation. Only the root tells them apart.
  • لَا يُنَالُ … إِلَّا بِالطَّلَبِ — ISTITHNA MUFARRAGH: a negative sentence, an
    إِلَّا, and no mustathna minhu at all, so what follows إِلَّا simply takes the
    i'rab the sentence had waiting for it.
  • الْمُجْمَل beside الْمُجْمِل in one sentence — ism maf'ul and ism fa'il of the
    same Form IV verb, differing by a single vowel, and the whole definition
    turns on which is which.
  • رَجَاءُ مَعْرِفَةِ مُرَادِهِ — an idafa chain four members long.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/mukhtasar-al-manar"
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

TITLE6 = {"ar": "مَرَاتِبُ الْخَفَاء", "en": "The Degrees of Obscurity",
          "tr": "Hafânın Mertebeleri"}

# The tamyiz of the descending ladder, written once and used three times — the
# mirror of chapter 5's وُضُوحًا, and the reason both chapters must be read together.
TAMYIZ = ("تَمْيِيزٌ مَنْصُوبٌ — تَمْيِيزُ نِسْبَةٍ، كَـ«وُضُوحًا» فِي الْبَابِ السَّابِقِ سَوَاءً بِسَوَاءٍ. وَ«خَفَاء» مَمْدُودٌ هَمْزَتُهُ مُنْقَلِبَةٌ عَنْ يَاءٍ أَصْلِيَّةٍ، فَهُوَ مُنْصَرِفٌ يُنَوَّنُ.",
 "A TAMYIZ in nasb, of the nisba kind — the exact counterpart of وُضُوحًا in the chapter before. And note what it is: a MAMDUD noun that KEEPS its tanwin, because its hamza is the root's own ya (خ ف ي) turned into one. صَحْرَاءُ ends in the same three letters and is barred from tanwin, because its hamza is the alif of feminisation. Nothing on the page distinguishes them; only the root does.",
 "Nisbet nev'inden mansub TEMYÎZ — bir önceki bâbdaki «وُضُوحًا»ın tam karşılığı. Neye dikkat etmeli: bu MEMDÛD bir isimdir ve tenvînini KORUR, zira hemzesi kökün kendi yâsından (خ ف ي) dönüşmüştür. صَحْرَاءُ aynı üç harfle biter ve tenvînden men edilmiştir; zira onun hemzesi te'nîs elifidir. Sayfada ikisini ayıran hiçbir şey yoktur; yalnız kök ayırır.")

S.append({"id": "s1", "translation": {
 "en": "And facing them are four: the hidden, the difficult, the summary and the ambiguous.",
 "tr": "Bunların karşısında da dört vardır: hafî, müşkil, mücmel ve müteşâbih."},
 "tokens": [
  tok("وَفِي","fi","prep",["huruf-jarr","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«فِي» حَرْفُ جَرٍّ وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "A joining waw, and «fi» a jarr letter whose phrase stands as the khabar, placed FIRST.",
      "Atıf vâvı; «فِي» cer harfidir ve câr-mecrûr mukaddem haberdir.",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","prep")]),
  tok("مُقَابَلَتِهَا","muqabala","noun",["huruf-jarr","idafa-definiteness","masdar","form-iii-verbs"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ عَائِدٌ عَلَى مَرَاتِبِ الْوُضُوحِ — مَصْدَرُ «قَابَلَ» عَلَى مُفَاعَلَةٍ.",
      "In jarr after «fi» and a mudaf, with the HA as its mudaf ilayh going back to the degrees of clearness — the masdar of قَابَلَ on مُفَاعَلَة. The word announces that what follows is not a new list but the OTHER SIDE of the one just given.",
      "«فِي» ile mecrûr ve muzâf; HÂ, vuzûh mertebelerine râci muzâfun ileyhtir — «قَابَلَ»nin MÜFÂALE vezninde masdarı. Kelime, geleceğin yeni bir liste değil, az önce verilenin ÖTEKİ YÜZÜ olduğunu haber verir.",
      segments=[seg("مُقَابَلَتِ","muqabala","noun"), seg("هَا","pron-3fs","pron")]),
  tok("أَرْبَعَةٌ","arbaa","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَسَاغَ الِابْتِدَاءُ بِالنَّكِرَةِ لِتَقَدُّمِ الْخَبَرِ عَلَيْهَا.",
      "The mubtada, in raf' and coming LAST. An indefinite noun may not normally start a sentence — and here it does not: the khabar came first, and that is precisely the licence.",
      "Muahhar merfû mübtedâ — nekre ile ibtidâ normalde câiz değildir; burada da olmamıştır: haber öne geçmiştir, ruhsatın sebebi tam da budur.", punct="："),
  tok("خَفِيٌّ","khafi","noun",["badal","sifa-mushabbaha"],
      "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ مِنْ «خَفِيَ».",
      "A badal of detail, in raf' — a sifa mushabbaha on فَعِيل from خَفِيَ.",
      "Merfû tafsîl bedeli — «خَفِيَ»den FAÎL vezninde sıfat-ı müşebbehe."),
  tok("وَمُشْكِلٌ","mushkil","noun",["atf-nasaq","ism-fail","form-iv-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «أَشْكَلَ»، أَيْ دَخَلَ فِي أَشْكَالِهِ فَالْتَبَسَ بِهَا.",
      "Joined, in raf' — the ism fa'il of أَشْكَلَ: literally the thing that has got in among its own look-alikes and cannot be picked out from them.",
      "Ma'tûf, merfû — «أَشْكَلَ»nin ism-i fâili: kendi benzerlerinin arasına karışıp onlardan ayırt edilemez hâle gelen şey.",
      segments=[seg("وَ","wa","conj"), seg("مُشْكِلٌ","mushkil","noun")]),
  tok("وَمُجْمَلٌ","mujmal","noun",["atf-nasaq","ism-maful","form-iv-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «أَجْمَلَ» عَلَى مُفْعَلٍ.",
      "Joined, in raf' — the ism maf'ul of أَجْمَلَ on مُفْعَل: the thing left summed up rather than spelled out.",
      "Ma'tûf, merfû — «أَجْمَلَ»nin MUF'AL vezninde ism-i mef'ûlü: açılmadan toplu bırakılan şey.",
      segments=[seg("وَ","wa","conj"), seg("مُجْمَلٌ","mujmal","noun")]),
  tok("وَمُتَشَابِهٌ","mutashabih","noun",["atf-nasaq","ism-fail","form-vi-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «تَشَابَهَ» عَلَى مُتَفَاعِلٍ، وَبَابُ التَّفَاعُلِ لِلْمُشَارَكَةِ: أَشْبَهَ بَعْضُهُ بَعْضًا حَتَّى لَمْ يُتَمَيَّزْ.",
      "Joined, in raf' — the ism fa'il of تَشَابَهَ on مُتَفَاعِل, and Form VI is the form of MUTUALITY: the parts have come to resemble one another until none can be told from the rest.",
      "Ma'tûf, merfû — «تَشَابَهَ»nin MÜTEFÂİL vezninde ism-i fâili; TEFÂUL bâbı MÜŞÂREKET içindir: parçalar birbirine benzemiş, hiçbiri ötekinden ayırt edilemez olmuştur.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("مُتَشَابِهٌ","mutashabih","noun")]),
 ],
 "jumal": [J("وَفِي مُقَابَلَتِهَا أَرْبَعَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا مُقَدَّمٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause with its khabar fronted — i'rabless.",
   "Haberi mukaddem isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the hidden is that whose intended sense is hidden by something incidental, not by the wording itself.",
 "tr": "Hafî, murâdı ârızî bir sebeple gizlenen — sîganın kendisinden değil — lafızdır."},
 "tokens": [
  tok("فَالْخَفِيُّ","khafi","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْخَفِيُّ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the hidden» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الْخَفِيُّ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْخَفِيُّ","khafi","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("خَفِيَ","khafiya","verb",["fail","jumla-sifa","naqis-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ، وَالْجُمْلَةُ صِلَةٌ — وَظَهَرَتِ الْيَاءُ فِي الْمَاضِي لِأَنَّهَا مُتَحَرِّكَةٌ، وَتُحْذَفُ فِي «خَفُوا».",
      "A past verb, a NAQIS YAI of the sami'a bab; the clause is the sila. Its ya stands on the page here because it carries a vowel, and it falls out the moment an ending would leave it sitting on a sukun: خَفُوا.",
      "Semi'a bâbından NÂKIS-İ YÂÎ mâzî fiil; cümle sıladır. Yâsı burada harekeli olduğu için yazıda durur; sâkin kalacağı bir ek geldiğinde düşer: خَفُوا."),
  tok("مُرَادُهُ","murad","noun",["fail","idafa-definiteness","ism-maful"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ وَهِيَ الْعَائِدُ عَلَى «مَا».",
      "The fa'il in raf' and a mudaf, with the HA as its mudaf ilayh — and that HA is the pronoun that ties the sila back to «that which».",
      "Merfû fâil ve muzâf; HÂ muzâfun ileyhtir ve sılayı «مَا»ya bağlayan âid zamîrdir.",
      segments=[seg("مُرَادُ","murad","noun"), seg("هُ","pron-3ms","pron")]),
  tok("بِعَارِضٍ","arid","noun",["huruf-jarr","ism-fail"],
      "الْبَاءُ لِلسَّبَبِيَّةِ، وَ«عَارِضٍ» مَجْرُورٌ بِهَا — اسْمُ فَاعِلٍ مِنْ «عَرَضَ»: مَا طَرَأَ مِنْ خَارِجٍ.",
      "The BA of cause, and «something incidental» in jarr after it — the ism fa'il of عَرَضَ: whatever has come upon the word from outside.",
      "Sebebiyye bâsı; «عَارِضٍ» onunla mecrûrdur — «عَرَضَ»nin ism-i fâili: kelimeye dışarıdan ârız olan şey.",
      segments=[seg("بِ","bi","prep"), seg("عَارِضٍ","arid","noun")]),
  tok("لَا","la-nafiya","part",["atf-nasaq"],
      "«لَا» عَاطِفَةٌ نَافِيَةٌ — تَنْفِي عَنِ الثَّانِي مَا أُثْبِتَ لِلْأَوَّلِ، وَهِيَ هُنَا الَّتِي تَحْمِلُ الْحَدَّ كُلَّهُ.",
      "«La» joining and denying: it takes back from the second what was granted to the first. It is the small word that carries the whole definition — the obscurity must come from OUTSIDE, or the word is not a khafi at all.",
      "Nefyeden âtıfa «لَا» — birinciye verileni ikinciden alır. Bütün tarifi taşıyan küçük kelimedir: kapalılık DIŞARIDAN gelmelidir, yoksa kelime hafî olmaz."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى «بِعَارِضٍ» فِي الْمَعْنَى.",
      "A jarr letter; in meaning the phrase is joined to «by something incidental».",
      "Cer harfi; câr-mecrûr mânâ cihetinden «بِعَارِضٍ»e ma'tûftur."),
  tok("نَفْسِ","nafs","noun",["huruf-jarr","idafa-definiteness","tawkid"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ — أُتِيَ بِـ«نَفْسِ» لِنَفْيِ الِاحْتِمَالِ: لَا مِنَ الصِّيغَةِ ذَاتِهَا.",
      "In jarr after «min» and a mudaf — «the very» is brought to close a door: not from the wording ITSELF, whatever else may be true of it.",
      "«مِنْ» ile mecrûr ve muzâf — «نَفْسِ», bir ihtimâli kapatmak için getirilmiştir: sîganın KENDİSİNDEN değil."),
  tok("الصِّيغَةِ","sigha","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهَذَا الْقَيْدِ فَارَقَ الْخَفِيُّ الْمُجْمَلَ: خَفَاءُ ذَاكَ مِنَ اللَّفْظِ، وَخَفَاءُ هَذَا مِنْ عَارِضٍ.",
      "The mudaf ilayh in jarr — and this clause is what separates the hidden from the summary: the summary is obscure BY ITS WORDING, the hidden only by what has happened to it.",
      "Mecrûr muzâfun ileyh — hafîyi mücmelden ayıran kayıt budur: mücmelin kapalılığı LAFZINDANDIR, hafînin kapalılığı ise başına gelen bir ârızdandır.",
      punct="."),
 ],
 "jumal": [J("الْخَفِيُّ مَا خَفِيَ مُرَادُهُ بِعَارِضٍ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("خَفِيَ مُرَادُهُ بِعَارِضٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the difficult is that which has grown more obscure, so that the intended sense is not reached except by searching.",
 "tr": "Müşkil, kapalılığı artıp murâda ancak araştırmayla ulaşılabilendir."},
 "tokens": [
  tok("وَالْمُشْكِلُ","mushkil","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُشْكِلُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the difficult» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُشْكِلُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُشْكِلُ","mushkil","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ازْدَادَ","izdada","verb",["fail","jumla-sifa","form-viii-verbs","hollow-verbs"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — وَهُوَ عَيْنُ الْفِعْلِ الَّذِي بُنِيَتْ عَلَيْهِ مَرَاتِبُ الْوُضُوحِ، وَإِنَّمَا تَغَيَّرَ تَمْيِيزُهُ.",
      "A past verb; the clause is the sila. It is the SAME verb the degrees of clearness were built on — only the tamyiz after it has changed. The two chapters are one table read from its two ends.",
      "Mâzî fiil; cümle sıladır. Vuzûh mertebelerinin üzerine kurulduğu fiilin AYNISIDIR; değişen yalnız ardındaki temyîzdir. İki bâb, iki ucundan okunan tek bir cetveldir."),
  tok("خَفَاءً","khafaa","noun",["tamyiz","masdar","ism-mamdud"], *TAMYIZ),
  tok("بِحَيْثُ","hayth","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«حَيْثُ» ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
      "The BA is a jarr letter, and «haythu» an adverb fixed on the damma, added to the clause after it.",
      "BÂ cer harfi; «حَيْثُ» damme üzere mebnî zarftır, sonrasındaki cümleye muzâftır.",
      segments=[seg("بِ","bi","prep"), seg("حَيْثُ","hayth","noun")]),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا — وَهِيَ شَرْطُ الِاسْتِثْنَاءِ الْمُفَرَّغِ الْآتِي بَعْدَهَا.",
      "«La» simply denying, and governing nothing — but it is the CONDITION for what comes next: the mufarragh exception only works after a negation.",
      "Amel etmeyen nefy «لَا»sı — fakat sonrasının ŞARTIdır: müferrağ istisnâ ancak nefyden sonra olur."),
  tok("يُنَالُ","nala","verb",["naib-al-fail","hollow-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَهُوَ أَجْوَفُ، عَيْنُهُ أَلِفٌ فِي «نَالَ» وَبَقِيَتْ أَلِفًا فِي مَجْهُولِ الْمُضَارِعِ.",
      "A mudari built for the unnamed doer, in raf' — a HOLLOW verb: نَالَ يَنَالُ, and in the passive the middle stays an alif, يُنَالُ.",
      "Meçhûl sîgasında merfû muzâri — ECVEF fiildir: نَالَ يَنَالُ; muzârinin meçhûlünde de orta harf elif olarak kalır: يُنَالُ."),
  tok("الْمُرَادُ","murad","noun",["naib-al-fail","ism-maful"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ.",
      "The naib al-fa'il, in raf'.",
      "Merfû nâib-i fâil."),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ: تَقَدَّمَهُ نَفْيٌ وَلَمْ يُذْكَرِ الْمُسْتَثْنَى مِنْهُ، فَتَفَرَّغَ الْعَامِلُ لِمَا بَعْدَهَا.",
      "The particle of exception — and the exception is MUFARRAGH, «emptied»: a negation came before it and no mustathna minhu was ever named, so the governor is left FREE to reach past إِلَّا and give what follows the i'rab it was holding. إِلَّا itself governs nothing here; it only removes the denial.",
      "İstisnâ edatı — istisnâ MÜFERRAĞdır, yani «boşaltılmış»: önünde nefy vardır ve müstesnâ minh zikredilmemiştir; böylece âmil, «إِلَّا»yı aşıp sonrasına elinde tuttuğu i'râbı vermekte SERBEST kalır. «إِلَّا» burada amel etmez; yalnız nefyi kaldırır."),
  tok("بِالطَّلَبِ","talab","noun",["istithna-mufarragh","huruf-jarr","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُنَالُ» — وَهُوَ الْمُسْتَثْنَى الْمُفَرَّغُ: أَخَذَ إِعْرَابَهُ مِنْ عَامِلِهِ لَا مِنْ «إِلَّا».",
      "A jarr-majrur attaching to «is reached» — and this is the emptied exception itself. Take إِلَّا away and the sentence still parses: «الْمُرَادُ يُنَالُ بِالطَّلَبِ». That is the test for a mufarragh, and it is the only exception whose i'rab comes from the governor rather than from إِلَّا.",
      "«يُنَالُ»a taalluk eden câr-mecrûr — müferrağ müstesnânın kendisidir. «إِلَّا»yı kaldır, cümle yine çözülür: «الْمُرَادُ يُنَالُ بِالطَّلَبِ». Müferrağın ölçüsü budur; i'râbını «إِلَّا»dan değil âmilinden alan tek istisnâ nev'idir.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("الطَّلَبِ","talab","noun")]),
 ],
 "jumal": [J("لَا يُنَالُ الْمُرَادُ إِلَّا بِالطَّلَبِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ لِـ«حَيْثُ».",
   "A verbal clause in the position of jarr, the mudaf ilayh of «haythu».",
   "«حَيْثُ»un muzâfun ileyhi olarak mahallen mecrûr fiil cümlesi.")]})

S.append({"id": "s4", "translation": {
 "en": "And the summary is that which has grown more obscure, so that it is not grasped except by an explanation from the one who summarised.",
 "tr": "Mücmel, kapalılığı artıp ancak icmâl edenin beyânıyla anlaşılabilendir."},
 "tokens": [
  tok("وَالْمُجْمَلُ","mujmal","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُجْمَلُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the summary» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُجْمَلُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُجْمَلُ","mujmal","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ازْدَادَ","izdada","verb",["fail","jumla-sifa","form-viii-verbs","hollow-verbs"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — الْمَرَّةُ الثَّانِيَةُ فِي النُّزُولِ.",
      "A past verb; the clause is the sila — the second step down.",
      "Mâzî fiil; cümle sıladır — inişteki ikinci basamak."),
  tok("خَفَاءً","khafaa","noun",["tamyiz","masdar","ism-mamdud"], *TAMYIZ),
  tok("بِحَيْثُ","hayth","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«حَيْثُ» مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
      "The BA is a jarr letter, and «haythu» is added to the clause after it.",
      "BÂ cer harfi; «حَيْثُ» sonrasındaki cümleye muzâftır.",
      segments=[seg("بِ","bi","prep"), seg("حَيْثُ","hayth","noun")]),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "«La» simply denying, and governing nothing.",
      "Amel etmeyen nefy «لَا»sı."),
  tok("يُدْرَكُ","adraka","verb",["naib-al-fail","form-iv-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ مِنْ «أَدْرَكَ»، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «مَا».",
      "A mudari built for the unnamed doer, in raf', from أَدْرَكَ — and its naib al-fa'il is a hidden pronoun going back to «that which». Note that the mudari of Form IV drops the hamza: أَدْرَكَ gives يُدْرِكُ, never *يُؤَدْرِكُ.",
      "«أَدْرَكَ»den meçhûl sîgasında merfû muzâri; nâib-i fâili «مَا»ya râci müstetir zamîrdir. Dikkat: İF'ÂL bâbının muzârisinde hemze düşer — «أَدْرَكَ»den «يُدْرِكُ» olur, *«يُؤَدْرِكُ» değil."),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ كَمَا سَبَقَ.",
      "The particle of exception, the exception again mufarragh as before.",
      "İstisnâ edatı; istisnâ yine önceki gibi müferrağdır."),
  tok("بِبَيَانٍ","bayan","noun",["istithna-mufarragh","huruf-jarr","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُدْرَكُ» — مَصْدَرُ «بَيَّنَ» عَلَى فَعَال.",
      "A jarr-majrur attaching to «is grasped» — the masdar of بَيَّنَ.",
      "«يُدْرَكُ»a taalluk eden câr-mecrûr — «بَيَّنَ»nin masdarı.",
      segments=[seg("بِ","bi","prep"), seg("بَيَانٍ","bayan","noun")]),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ — وَفُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter for the start of the span — its nun takes a fatha because two sukuns met.",
      "İbtidâ-i gāye için cer harfi — iki sâkin karşılaştığı için nûnu fetha almıştır."),
  tok("الْمُجْمِلِ","mujmil","noun",["huruf-jarr","ism-fail","form-iv-verbs"],
      "مَجْرُورٌ بِـ«مِنْ» — اسْمُ فَاعِلٍ مِنْ «أَجْمَلَ»، وَبَيْنَهُ وَبَيْنَ «الْمُجْمَلِ» فِي أَوَّلِ الْجُمْلَةِ حَرَكَةٌ وَاحِدَةٌ: كَسْرَةُ الْمِيمِ تَجْعَلُهُ الْفَاعِلَ، وَفَتْحُهَا يَجْعَلُهُ الْمَفْعُولَ.",
      "In jarr after «min» — the ism fa'il of أَجْمَلَ. Between it and الْمُجْمَل at the head of this very sentence there stands ONE vowel: a kasra on the mim makes it the one who summarised, a fatha makes it the thing summarised. The whole definition turns on that vowel, and a text without vowels leaves the reader to supply it.",
      "«مِنْ» ile mecrûr — «أَجْمَلَ»nin ism-i fâili. Aynı cümlenin başındaki «الْمُجْمَلِ» ile arasında TEK bir hareke vardır: mîmin kesrası onu icmâl EDEN, fethası ise icmâl EDİLEN yapar. Bütün tarif o harekeye bağlıdır; harekesiz bir metinde okuyucu onu kendi takdîr etmek zorundadır.",
      punct="."),
 ],
 "jumal": [J("لَا يُدْرَكُ إِلَّا بِبَيَانٍ مِنَ الْمُجْمِلِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ لِـ«حَيْثُ».",
   "A verbal clause in the position of jarr, the mudaf ilayh of «haythu».",
   "«حَيْثُ»un muzâfun ileyhi olarak mahallen mecrûr fiil cümlesi.")]})

S.append({"id": "s5", "translation": {
 "en": "And the ambiguous is that whose hope of knowing its intended sense has been cut off.",
 "tr": "Müteşâbih, murâdını bilme ümidi kesilmiş olandır."},
 "tokens": [
  tok("وَالْمُتَشَابِهُ","mutashabih","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُتَشَابِهُ» مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ آخِرُ الدَّرَجَاتِ نُزُولًا.",
      "A joining waw; «the ambiguous» is the mubtada in raf' — the bottom of the descent.",
      "Atıf vâvı; «الْمُتَشَابِهُ» merfû mübtedâdır — inişin en alt basamağıdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَشَابِهُ","mutashabih","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("انْقَطَعَ","inqataa","verb",["fail","jumla-sifa","form-vii-verbs"],
      "فِعْلٌ مَاضٍ عَلَى «اِنْفَعَلَ»، وَهُوَ مُطَاوِعُ «قَطَعَ» — وَالْجُمْلَةُ صِلَةٌ. وَلَمْ يَقُلْ «مَا لَا يُعْلَمُ»، بَلْ قَطَعَ الرَّجَاءَ نَفْسَهُ: فَالطَّلَبُ هُنَا لَا يُجْدِي، بِخِلَافِ الْمُشْكِلِ.",
      "A past verb on اِنْفَعَلَ, the mutawa'a of قَطَعَ; the clause is the sila. The matn does not say «what is not known» — it says the HOPE itself has been cut. Searching helped with the mushkil; here it does not, and the difference is deliberate.",
      "«اِنْفَعَلَ» vezninde mâzî fiil, «قَطَعَ»in mutâvaatı; cümle sıladır. Metin «bilinmeyen şey» demiyor, ÜMİDİN kendisinin kesildiğini söylüyor. Müşkilde araştırmak fayda veriyordu; burada vermez ve bu fark kasıtlıdır."),
  tok("رَجَاءُ","rajaa","noun",["fail","idafa-definiteness","masdar","ism-mamdud"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «رَجَا»، وَهُوَ مَمْدُودٌ هَمْزَتُهُ عَنْ وَاوٍ فَهُوَ مُنْصَرِفٌ.",
      "The fa'il in raf' and a mudaf — the masdar of رَجَا, and a mamdud whose hamza comes from a waw, so it too keeps its tanwin when indefinite. It heads a chain of four.",
      "Merfû fâil ve muzâf — «رَجَا»nın masdarı; hemzesi vâvdan dönüşen memdûddur, dolayısıyla nekre iken tenvînini korur. Dört rükünlü bir izâfetin başıdır."),
  tok("مَعْرِفَةِ","marifa","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — الْحَلْقَةُ الثَّانِيَةُ.",
      "The mudaf ilayh in jarr, and itself a mudaf — the second link.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — ikinci halka."),
  tok("مُرَادِهِ","murad","noun",["idafa-definiteness","ism-maful"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — فَالسِّلْسِلَةُ أَرْبَعُ حَلَقَاتٍ: رَجَاءُ ← مَعْرِفَةِ ← مُرَادِ ← الْهَاءِ، وَكُلُّ وَاحِدَةٍ فِي الْوَسَطِ مُضَافٌ وَمُضَافٌ إِلَيْهِ مَعًا.",
      "The mudaf ilayh in jarr and itself a mudaf, with the HA as a further mudaf ilayh — so the chain runs FOUR links deep: رَجَاءُ ← مَعْرِفَةِ ← مُرَادِ ← the HA. Every link in the middle is a mudaf and a mudaf ilayh at the same time, and only the last is not itself a mudaf.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf; HÂ da ayrıca muzâfun ileyhtir — zincir DÖRT halkadır: رَجَاءُ ← مَعْرِفَةِ ← مُرَادِ ← HÂ. Ortadaki her halka aynı anda hem muzâf hem muzâfun ileyhtir; yalnız sonuncusu muzâf değildir.",
      punct=".", segments=[seg("مُرَادِ","murad","noun"), seg("هِ","pron-3ms","pron")]),
 ],
 "jumal": [J("انْقَطَعَ رَجَاءُ مَعْرِفَةِ مُرَادِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "muqabala":   g("مُقَابَلَة", "ق ب ل", "noun", "facing, standing opposite (masdar, Form III)", "mukābele; karşı karşıya olma (masdar)", 4),
 "khafi":      g("خَفِيّ", "خ ف ي", "noun", "the HIDDEN — obscured by something outside the wording", "hafî — lafzın dışından bir sebeple kapalı olan", 4),
 "mushkil":    g("مُشْكِل", "ش ك ل", "noun", "the DIFFICULT — reached only by searching", "müşkil — ancak araştırmayla ulaşılan", 4),
 "mujmal":     g("مُجْمَل", "ج م ل", "noun", "the SUMMARY — grasped only by the speaker's explanation", "mücmel — ancak mütekellimin beyânıyla anlaşılan", 4),
 "mutashabih": g("مُتَشَابِه", "ش ب ه", "noun", "the AMBIGUOUS — its meaning past hoping for", "müteşâbih — mânâsı umulmaz olan", 5),
 "khafiya":    g("خَفِيَ", "خ ف ي", "verb", "to be hidden, to be concealed", "gizli kalmak, kapalı olmak", 3),
 "khafaa":     g("خَفَاء", "خ ف ي", "noun", "obscurity, hiddenness (masdar)", "hafâ; kapalılık (masdar)", 4),
 "arid":       g("عَارِض", "ع ر ض", "noun", "something incidental, a passing cause (ism fa'il)", "ârız; dışarıdan gelen sebep", 4),
 "sigha":      g("صِيغَة", "ص و غ", "noun", "the wording, the form a thing is cast in", "sîga; kalıp", 3, plural="صِيَغ"),
 "la-nafiya":  g("لَا (النَّافِيَة)", None, "part", "not (plain denial; governs nothing)", "…değil (sade nefy; amel etmez)", 2),
 "nala":       g("نَالَ", "ن ي ل", "verb", "to reach, to attain", "ulaşmak, elde etmek", 3),
 "illa":       g("إِلَّا", None, "part", "except, but", "ancak, …-den başka", 3),
 "talab":      g("طَلَب", "ط ل ب", "noun", "seeking, searching for (masdar)", "talep; arayış (masdar)", 2),
 "adraka":     g("أَدْرَكَ", "د ر ك", "verb", "to grasp, to catch up with", "idrak etmek, yetişmek", 3),
 "bayan":      g("بَيَان", "ب ي ن", "noun", "an explanation, a making-plain (masdar)", "beyân; açıklama (masdar)", 3),
 "mujmil":     g("مُجْمِل", "ج م ل", "noun", "the one who left it summed up (ism fa'il)", "mücmil; icmâl eden", 5),
 "inqataa":    g("اِنْقَطَعَ", "ق ط ع", "verb", "to be cut off, to come to an end", "kesilmek, son bulmak", 3),
 "rajaa":      g("رَجَاء", "ر ج و", "noun", "hope, expectation (masdar)", "recâ; ümit (masdar)", 3),
}

def build_morph():
    """Copy where the library already carries the verb; generate only what is new."""
    out = {}
    for lex, src in (("nala", "bad-al-amali"), ("inqataa", "kitab-al-sulh")):
        s = json.loads((ROOT / "content/samples" / src / "morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / "content/samples" / src / "glossary.json").read_text(encoding="utf-8"))
        assert g_["entries"][lex]["lemma"] == GLOSS_ADD[lex]["lemma"], \
            f"{lex}: {src} has {g_['entries'][lex]['lemma']}, we say {GLOSS_ADD[lex]['lemma']}"
        out[lex] = s["verbs"][lex]
    # خَفِيَ — NAQIS YAI of the sami'a bab. The ya stands where it carries a
    # vowel and falls where an ending would leave it on a sukun.
    # `naqis1` builds the رَمَى / دَعَا mazi, whose third radical is an alif. The
    # sami'a bab is the OTHER naqis mazi — بَقِيَ، رَضِيَ، خَفِيَ — where the ya
    # stands and carries a kasra, and only the third-person plural contracts.
    # sarf_gen keeps a separate maker for it, and using the wrong one shipped
    # *خَفِى / *خَفِتْ before the regeneration gate caught it.
    out["khafiya"] = _sg.entry(
        "مِنْ بَابِ سَمِعَ يَسْمَعُ — نَاقِصٌ يَائِيٌّ", "فَعِلَ يَفْعَلُ",
        "خَفَاء", "خَافٍ (الْخَافِي)",
        _sg.mazi_naqis_kasra("خَفِ", "خَفُوا"),
        _sg.mudari_naqis("َ", "خْف", "a"),
        _sg.amr_naqis("اِخْف", "a"),
        "يَخْفَى", "يَخْفَ", "تَخْفَ",
        note="نَاقِصٌ يَائِيٌّ مِنْ بَابِ سَمِعَ: خَفِيَ يَخْفَى، وَالْجَزْمُ بِحَذْفِ الْأَلِفِ — لَمْ يَخْفَ.")
    # أَدْرَكَ — Form IV, sound. The hamza of the mazi drops in the mudari.
    out["adraka"] = _sg.derived("بَابُ الْإِفْعَالِ: أَفْعَلَ يُفْعِلُ", "أَفْعَلَ يُفْعِلُ", "ُ",
                                "أَدْرَك", "دْرِك", "أَدْرِك", "إِدْرَاك", "مُدْرِك",
                                maful="مُدْرَك", pmz="أُدْرِكَ", pmd="يُدْرَكُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/6.json").write_text(
    json.dumps({"chapter": 6, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 6 for c in man["chapters"]):
    man["chapters"].append({"n": 6, "title": TITLE6})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.6.0"
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة الأربعة، ثم أقسام اللفظ وضعًا ووضوحًا وخفاءً",
                   "en": "The opening definitions, the four sources, then the wording divided by what it was set down for, by how plainly it shows, and by how far it hides",
                   "tr": "Açılış tarifleri, dört delil, sonra lafzın vaz'ına, vuzûhuna ve hafâsına göre taksîmi"}
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch6:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
