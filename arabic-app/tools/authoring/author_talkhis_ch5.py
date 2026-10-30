# -*- coding: utf-8 -*-
"""Author chapter 5 of talkhis-al-miftah — الْحَقِيقَةُ الْعَقْلِيَّةُ وَالْمَجَازُ الْعَقْلِيُّ.

Chapter 4 closed by announcing that predication is of two kinds. This chapter
defines both, and the definitions are the two most quoted lines in the whole
first fann. What makes them worth an app rather than a page is that the
DIFFERENCE between them is one word — «مَا هُوَ لَهُ» against «مُلَابَسٍ لَهُ غَيْرِ
مَا هُوَ لَهُ» — and everything else in the two sentences is identical, down to
the أَوْ مَعْنَاهُ. A reader who can see which half changed has understood the
chapter; a reader who cannot has read the same sentence twice.

Then the examples, and they are not decoration: each one names a different
MULĀBIS — the thing the act was hung on instead of its true owner. The
commentary lists six (mafʿūl, fāʿil, maṣdar, zamān, makān, sabab) and this
chapter carries all six, each beside the plain sentence that says the same
thing literally.

ATTRIBUTION: every Arabic word here is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~514-548 and ~589-599,
which quotes the matn's two definitions vowelled and then gives each example
with its ḥaqīqa spelled out in Arabic. The example sentences below JUXTAPOSE
two of the source's own phrases with a dash between them — the figure, then
the literal sentence underneath it. No Arabic word in this chapter is composed,
and no connective has been invented to join them.

ONE DIVERGENCE, recorded in the manifest: the supplied commentary vowels the
definition's key word مُلَابَسٍ (ism mafʿūl) and repeats that vowelling in its own
question-and-answer about the term. Printed editions of the Talkhīṣ are widely
vowelled مُلَابِسٍ (ism fāʿil). The two differ by one ḥaraka and hardly at all in
sense — «a thing associated with it» against «a thing having association with
it» — and the paradigm the app now ships for لَابَسَ shows both cells side by
side, which is the honest way to leave a divergence a reader can see.

Grammar this chapter is chosen to teach:
  • لَهُ TWICE, in two different states, in two consecutive sentences. In s1 it
    is the khabar of a ṣila and its ʿāmil is ESTIMATED — ظَرْفٌ مُسْتَقَرٌّ. In s2
    the identical two letters attach to «مُلَابَسٍ», an ism mafʿūl standing right
    beside them — ظَرْفٌ لَغْوٌ. Same word, same sentence-shape, opposite state,
    and the engine now names which is which.
  • THE MANQŪṢ COMPLETED. Chapter 3 had خَالِي الذِّهْنِ in jarr (kasra estimated,
    yāʾ standing because it is annexed). Chapter 4 had it in rafʿ (ḍamma
    estimated). This chapter has الْوَادِيَ in naṣb — fatḥa WRITTEN on the yāʾ —
    and جَارٍ indefinite, where the yāʾ is deleted outright and the tanwīn sits
    on a kasra. Four states of one noun class across three chapters.
  • صَائِم — the ism fāʿil of an ajwaf: صَاوِم with the ʿayn turned HAMZA. The
    iʿlāl engine derives it, and نَهَارُهُ صَائِمٌ is the sentence that makes the
    derivation worth having.
  • أَفْعَمَ, whose ROOT IS ف ع م — so the verb and the mīzān that measures it are
    spelled with the same three letters. There is no better single word for
    showing that a wazn is a MOULD and not a spelling.
  • يَجْعَلُ الْوِلْدَانَ شِيبًا — a verb of two objects, for the third chapter
    running, and this time in the Qurʾān.
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
S = []

TITLE5 = {"ar": "الْحَقِيقَةُ الْعَقْلِيَّةُ وَالْمَجَازُ الْعَقْلِيُّ",
          "en": "The Intellectual Truth and the Intellectual Figure",
          "tr": "Hakîkat-i Akliyye ve Mecâz-ı Aklî"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "And it is attributing the act, or the meaning of the act, to the one it belongs to in the speaker's own view, outwardly.",
 "tr": "O da, fiili yahut fiilin mânâsını, zâhirde ve mütekellimin kendi kanaatinde, kime âitse ona isnâd etmektir."},
 "tokens": [
  tok("وَهِيَ","hiya","pron",["mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«هِيَ» ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — يَعُودُ عَلَى «الْحَقِيقَةِ الْعَقْلِيَّةِ» الْمَذْكُورَةِ فِي آخِرِ الْبَابِ السَّابِقِ.",
      "A joining waw, and «hiya» is a detached pronoun, mabni, in the position of raf' as the mubtada — pointing back at «the intellectual truth» named in the last line of the previous chapter. The definition is not introduced; it is CONTINUED, and the feminine pronoun is the whole of the join.",
      "Atıf vâvı; «هِيَ» munfasıl zamirdir, mahallen merfû mübtedâdır — bir önceki bâbın son satırında anılan «الْحَقِيقَةُ الْعَقْلِيَّةُ»ye râcidir. Tarif takdîm edilmiyor, SÜRDÜRÜLÜYOR; ve bağın tamamı bu müennes zamirdir.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("إِسْنَادُ","isnad","noun",["mubtada-khabar","masdar","imal-al-masdar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ عَمَلَ فِعْلِهِ، فَـ«الْفِعْلِ» مَفْعُولُهُ فِي الْمَعْنَى وَإِنْ كَانَ مَجْرُورًا فِي اللَّفْظِ.",
      "The khabar in raf' and a mudaf — a masdar GOVERNING as its verb does, so «the act» is its object in meaning even though it is majrur in form. The definition of a science is a masdar because a science defines ACTS, and the eleventh chapter of the Manar defined ijtihad the same way.",
      "Merfû haber ve muzâf — fiili gibi AMEL EDEN masdar; öyleyse «الْفِعْلِ» lafzan mecrûr olsa da mânen onun mef'ûlüdür. Bir ilmin tarifi masdarla yapılır, çünkü ilim FİİLLERİ tarif eder; Menâr'ın ictihâd tarifi de aynı yoldan gitmişti."),
  tok("الْفِعْلِ","fil","noun",["idafa-definiteness","imal-al-masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ الْمَفْعُولُ فِي الْمَعْنَى.",
      "The mudaf ilayh in jarr — and the object in meaning.",
      "Mecrûr muzâfun ileyh — mânen mef'ûldür."),
  tok("أَوْ","aw","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّنْوِيعِ — لَا لِلشَّكِّ، بَلْ لِتَوْسِيعِ الْمَحْدُودِ.",
      "A letter of atf giving a VARIETY, not a doubt: it widens what is being defined rather than hesitating between two things.",
      "Tenvî için atıf harfi — şek için değil; tarif edilen şeyi GENİŞLETMEK içindir."),
  tok("مَعْنَاهُ","mana","noun",["atf-nasaq","ism-maqsur-manqus","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى «الْفِعْلِ» مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ، وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ. وَمَعْنَى الْفِعْلِ: الْمَصْدَرُ وَاسْمُ الْفَاعِلِ وَاسْمُ الْمَفْعُولِ وَالصِّفَةُ الْمُشَبَّهَةُ وَاسْمُ التَّفْضِيلِ وَالظَّرْفُ الْمُسْتَقَرُّ.",
      "Joined to «the act», in jarr by a kasra ESTIMATED on the alif because the alif cannot take one — a maqsur noun — and it is a mudaf with the ha annexed to it. And «the meaning of the act» is the commentary's own list: a masdar, an ism fa'il, an ism maf'ul, a sifa mushabbaha, an ism tafdil and a settled zarf. That list is exactly what this app's ta'alluq engine asks for when it looks for something to hang a jarr phrase on — six items, named by a book of the seventh century.",
      "«الْفِعْلِ»e ma'tûf; elif hareke kabul etmediği için MUKADDER kesra ile mecrûrdur — ism-i maksûr; ayrıca muzâftır, hâ muzâfun ileyhtir. «Fiilin mânâsı»ndan murad, şerhin kendi saydığı altı şeydir: masdar, ism-i fâil, ism-i mef'ûl, sıfat-ı müşebbehe, ism-i tafdîl ve zarf-ı müstakar. Bu liste, uygulamanın taalluk motorunun bir câr-mecrûru asacak şey ararken sorduğu şeyin ta kendisidir — yedinci asırdan bir kitabın saydığı altı madde."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«إِسْنَادُ».",
      "A jarr letter — the phrase attaching to «attributing».",
      "Cer harfi — câr-mecrûr «إِسْنَادُ»ya taalluk eder."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","anwa-ma"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ بِـ«إِلَى».",
      "A relative noun, mabni, in the position of jarr after «ila». It is the sixth of the twelve faces of ma, and here nothing else is possible: a harf cannot be governed by a jarr letter.",
      "İsm-i mevsûl; «إِلَى» ile mahallen mecrûrdur. Mânın on iki vechinden altıncısıdır ve burada başka ihtimal yoktur: cer harfi bir harfi cer edemez."),
  tok("هُوَ","huwa","pron",["mubtada-khabar","jumla-sifa"],
      "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A detached pronoun in the position of raf' as the mubtada — and the clause is the sila of the relative, with no position in i'rab.",
      "Munfasıl zamir, mahallen merfû mübtedâ — cümle ism-i mevsûlün sılasıdır, mahalli yoktur."),
  tok("لَهُ","li","prep",["huruf-jarr","mubtada-khabar","zarf-mustaqarr-wa-laghw"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْهَاءُ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ، فَهُوَ ظَرْفٌ مُسْتَقَرٌّ.",
      "The lam is a jarr letter and the ha is in the position of jarr — and the phrase attaches to an OMITTED khabar, which makes it MUSTAQARR. The estimated «kaʾin» carries a doer inside it, and that is why two letters and a pronoun can be a whole predicate. Watch this word: the next sentence has the identical two letters in the opposite state.",
      "Lâm cer harfi, hâ mahallen mecrûr — ve câr-mecrûr MAHZÛF bir habere taalluk eder; öyleyse ZARF-I MÜSTAKARdır. Takdîr edilen «kâin» içinde bir fâil taşır; iki harf ile bir zamirin bütün bir haber olabilmesinin sebebi budur. Bu kelimeye dikkat: bir sonraki cümlede aynı iki harf, tam zıt hâlde gelecek.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("عِنْدَ","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ، مُتَعَلِّقٌ بِالْخَبَرِ الْمَحْذُوفِ — أَيْ: ثَابِتٌ لَهُ عِنْدَ الْمُتَكَلِّمِ.",
      "A zarf of place in nasb and a mudaf, attaching to the omitted khabar — «established as his, IN THE SPEAKER'S VIEW». عِنْدَ is a noun, not a letter, and this app peels عِنْدَهُ into two the same way it peels مَعَهُ. Where this word is placed decides the whole definition: the truth of an attribution is measured against what the SPEAKER believes, not against the world, which is why a mistaken man still speaks a ḥaqiqa and a liar does not.",
      "Mansub mekân zarfı ve muzâf; mahzûf habere taalluk eder — «MÜTEKELLİM İNDİNDE ona sâbit olan». «عِنْدَ» harf değil isimdir; uygulama «عِنْدَهُ»yu da «مَعَهُ» gibi ikiye ayırır. Bu kelimenin yeri bütün tarifi belirler: bir isnâdın hakîkîliği âleme göre değil, MÜTEKELLİMİN inancına göre ölçülür; yanılan adamın sözü yine hakîkat-i akliyye olur, yalancınınki olmaz."),
  tok("الْمُتَكَلِّمِ","mutakallim","noun",["idafa-definiteness","ism-fail","form-v-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «تَكَلَّمَ» عَلَى مُتَفَعِّلٍ.",
      "The mudaf ilayh in jarr — the ism fa'il of تَكَلَّمَ on مُتَفَعِّل. The one DOING the speaking, named by the pattern rather than by a separate word.",
      "Mecrûr muzâfun ileyh — «تَكَلَّمَ»nin MÜTEFA'İL vezninde ism-i fâili. Konuşma işini YAPAN; ayrı bir kelimeyle değil, vezinle adlandırılmıştır."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfi."),
  tok("الظَّاهِرِ","zahir","noun",["huruf-jarr","ism-fail","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«فِي» — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«إِسْنَادُ»، فَهُوَ ظَرْفٌ لَغْوٌ، بِخِلَافِ «لَهُ» الَّذِي تَقَدَّمَ. وَبِهَذَا الْقَيْدِ يَخْرُجُ قَوْلُ الْجَاهِلِ وَالْكَاذِبِ.",
      "Majrur by «fi» — and the phrase attaches to «attributing», which makes it LAGHW, unlike the «lahu» four words back. Two jarr phrases in one sentence, one hanging on a written governor and one on an estimated one, and the books have a name for each. And the restriction «outwardly» is doing real work: it lets in the man who believes what he says and is wrong, and keeps out the man who says it without believing it.",
      "«فِي» ile mecrûr — ve câr-mecrûr «إِسْنَادُ»ya taalluk eder; öyleyse ZARF-I LAĞVdır — dört kelime önceki «لَهُ»nun aksine. Tek cümlede iki câr-mecrûr: biri yazılı âmile, öteki takdîrî âmile asılı; ve kitapların her biri için bir adı var. «Zâhirde» kaydı da boş durmuyor: inandığını söyleyip yanılanı içeri alır, inanmadığını söyleyeni dışarıda bırakır.",
      punct="."),
 ],
 "jumal": [J("هُوَ لَهُ",
   "جُمْلَةٌ اسْمِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan isim cümlesi — mahalsizdir."),
  J("وَهِيَ إِسْنَادُ الْفِعْلِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "And it is attributing the act, or the meaning of the act, to something associated with it OTHER than the one it belongs to, by an interpretation.",
 "tr": "O da, fiili yahut fiilin mânâsını, bir te'vîl ile, kendisine âit olandan BAŞKA fakat onunla alâkalı bir şeye isnâd etmektir."},
 "tokens": [
  tok("وَهُوَ","huwa","pron",["mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«هُوَ» مُبْتَدَأٌ — يَعُودُ عَلَى «الْمَجَازِ الْعَقْلِيِّ». وَالتَّعْرِيفَانِ تَوْأَمَانِ فِي اللَّفْظِ، وَالْفَرْقُ كُلُّهُ فِيمَا بَعْدَ «إِلَى».",
      "A joining waw, and «huwa» is the mubtada, pointing back at «the intellectual figure». The two definitions are twins in wording — same masdar, same object, same أَوْ مَعْنَاهُ — and the entire difference between truth and figure sits after «ila». A reader who can name which half changed has read the chapter.",
      "Atıf vâvı; «هُوَ» mübtedâdır — «الْمَجَازُ الْعَقْلِيُّ»ye râcidir. İki tarif lafızda ikizdir — aynı masdar, aynı mef'ûl, aynı «أَوْ مَعْنَاهُ» — ve hakîkat ile mecâz arasındaki bütün fark «إِلَى»dan sonrasındadır. Hangi yarının değiştiğini söyleyebilen, bâbı okumuş demektir.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("إِسْنَادُ","isnad","noun",["mubtada-khabar","masdar","imal-al-masdar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرٌ عَامِلٌ كَالَّذِي قَبْلَهُ.",
      "The khabar in raf' and a mudaf — a governing masdar, exactly as in the sentence before.",
      "Merfû haber ve muzâf — bir öncekiyle aynı: âmil masdar."),
  tok("الْفِعْلِ","fil","noun",["idafa-definiteness","imal-al-masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh in jarr.",
      "Mecrûr muzâfun ileyh."),
  tok("أَوْ","aw","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّنْوِيعِ.",
      "A letter of atf giving a variety.",
      "Tenvî için atıf harfi."),
  tok("مَعْنَاهُ","mana","noun",["atf-nasaq","ism-maqsur-manqus","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَهُوَ مُضَافٌ.",
      "Joined, in jarr by an estimated kasra on the alif, and a mudaf. Because the two definitions repeat this word, the majaz reaches the participles too: عِيشَةٌ رَاضِيَةٌ has no verb in it at all.",
      "Ma'tûf; elif üzerinde mukadder kesra ile mecrûr ve muzâf. İki tarif bu kelimeyi tekrarladığı için mecâz ism-i fâile de ulaşır: «عِيشَةٌ رَاضِيَةٌ»de hiç fiil yoktur."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«إِسْنَادُ».",
      "A jarr letter attaching to «attributing».",
      "«إِسْنَادُ»ya taalluk eden cer harfi."),
  tok("مُلَابَسٍ","mulabas","noun",["huruf-jarr","ism-maful","form-iii-verbs"],
      "مَجْرُورٌ بِـ«إِلَى» — اسْمُ مَفْعُولٍ مِنْ «لَابَسَ» عَلَى مُفَاعَلٍ، أَيْ: شَيْءٌ بَيْنَهُ وَبَيْنَ الْفِعْلِ مُلَابَسَةٌ. وَالنُّسْخَةُ الْمَطْبُوعَةُ تَضْبِطُهُ «مُلَابِسٍ» بِالْكَسْرِ عَلَى اسْمِ الْفَاعِلِ، وَالْمَعْنَى وَاحِدٌ.",
      "Majrur by «ila» — the ism maf'ul of لَابَسَ on مُفَاعَل: a thing that has a CONNECTION with the act. The source this package is built from vowels it with a fatha; printed editions commonly write مُلَابِسٍ with a kasra, the ism fa'il. One haraka apart and hardly any sense apart — «a thing associated with it» against «a thing having association with it» — and the paradigm this app ships for لَابَسَ shows the two cells one line apart, which is the only honest way to leave a divergence a reader can check.",
      "«إِلَى» ile mecrûr — «لَابَسَ»nin MUFÂAL vezninde ism-i mef'ûlü: fiil ile arasında MÜLÂBESE bulunan şey. Bu paketin dayandığı kaynak onu fethalı harekeler; matbû nüshalar çoğunlukla kesralı «مُلَابِسٍ» (ism-i fâil) yazar. Aralarında bir hareke, mânâca hemen hiç fark yok — «onunla alâkalı olan şey» ile «onunla alâkası bulunan şey» — ve uygulamanın «لَابَسَ» için taşıdığı çekim, iki hâneyi bir satır arayla gösterir; bir nüsha ihtilâfını okuyucunun görebileceği şekilde bırakmanın dürüst yolu budur."),
  tok("لَهُ","li","prep",["huruf-jarr","naat-sifa","zarf-mustaqarr-wa-laghw"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْهَاءُ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِـ«مُلَابَسٍ»، فَهُوَ ظَرْفٌ لَغْوٌ.",
      "The lam is a jarr letter and the ha is in the position of jarr — attaching to «mulabas», the word standing immediately before it, which makes it LAGHW. In the previous sentence the very same two letters were MUSTAQARR because nothing there could govern them. The difference is not in the word; it is in what is standing next to it, and this is the clearest pair the library contains.",
      "Lâm cer harfi, hâ mahallen mecrûr — hemen önündeki «مُلَابَسٍ»e taalluk eder; öyleyse ZARF-I LAĞVdır. Bir önceki cümlede tıpatıp aynı iki harf MÜSTAKARdı, çünkü orada onları amel edecek bir şey yoktu. Fark kelimede değil, yanında duranda; ve kütüphanenin sahip olduğu en berrak çift budur."),
  tok("غَيْرِ","ghayr","noun",["naat-sifa","idafa-definiteness"],
      "نَعْتٌ لِـ«مُلَابَسٍ» مَجْرُورٌ وَهُوَ مُضَافٌ — وَ«غَيْرُ» لَا تَتَعَرَّفُ بِالْإِضَافَةِ، فَصَحَّ نَعْتُ النَّكِرَةِ بِهَا.",
      "A na't of «mulabas», in jarr and a mudaf — and «ghayr» is one of the nouns that stay INDEFINITE however they are annexed, which is exactly why it may describe an indefinite. That is a rule the app's iḍāfa engine knows and most readers meet here for the first time.",
      "«مُلَابَسٍ»in na'tı, mecrûr ve muzâf — «غَيْر» izâfetle marife OLMAYAN isimlerdendir; nekreye sıfat olabilmesinin sebebi tam budur. Bu, uygulamanın izâfet motorunun bildiği, okuyucunun çoğu kez ilk defa burada karşılaştığı bir kāidedir."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","anwa-ma","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْمُضَافُ إِلَيْهِ لَا يَكُونُ إِلَّا اسْمًا.",
      "A relative noun in the position of jarr as the mudaf ilayh — and the mudaf ilayh seat is closed to the particles. Whatever else this ma might be elsewhere, standing after «ghayr» it can only be a noun, and the app's ma engine settles it on exactly that ground.",
      "Mahallen mecrûr muzâfun ileyh olan ism-i mevsûl — muzâfun ileyh isimden başkası olamaz. Bu mâ başka yerde ne olursa olsun, «غَيْرِ»den sonra ancak isim olur; uygulamanın mâ motoru da meseleyi tam bu delille bitirir."),
  tok("هُوَ","huwa","pron",["mubtada-khabar","jumla-sifa"],
      "مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "The mubtada — and the clause is the sila of the relative.",
      "Mübtedâ — cümle ism-i mevsûlün sılasıdır."),
  tok("لَهُ","li","prep",["huruf-jarr","mubtada-khabar","zarf-mustaqarr-wa-laghw"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ — ظَرْفٌ مُسْتَقَرٌّ. فَفِي هَذِهِ الْجُمْلَةِ «لَهُ» مَرَّتَيْنِ: الْأُولَى لَغْوٌ وَالثَّانِيَةُ مُسْتَقَرٌّ.",
      "A jarr and majrur attaching to an omitted khabar — MUSTAQARR. So this one sentence carries «lahu» twice: the first laghw, the second mustaqarr. Identical letters, identical order, opposite state — and nothing but the neighbouring word decides it.",
      "Mahzûf habere taalluk eden câr-mecrûr — ZARF-I MÜSTAKAR. Bu tek cümlede «لَهُ» iki defa geçiyor: birincisi lağv, ikincisi müstakar. Harfleri aynı, sırası aynı, hâli zıt — ve karar veren şey yalnızca yanındaki kelime.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("بِتَأَوُّلٍ","taawwul","noun",["huruf-jarr","masdar","form-v-verbs"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«تَأَوُّلٍ» مَجْرُورٌ — مَصْدَرُ «تَأَوَّلَ» عَلَى التَّفَعُّلِ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«إِسْنَادُ»، لَغْوٌ. وَهَذَا الْقَيْدُ يُخْرِجُ كَلَامَ الْجَاهِلِ: مَنْ نَسَبَ الْإِنْبَاتَ إِلَى الرَّبِيعِ مُعْتَقِدًا فَلَيْسَ مَجَازًا، بَلْ خَطَأٌ.",
      "The ba is a jarr letter and «an interpretation» is majrur — the Form V masdar of تَأَوَّلَ — the phrase attaching to «attributing», laghw. And this single restriction is what keeps the definition honest: a man who ascribes the growing to the SPRING and believes it has not made a figure, he has made a mistake. A majaz requires that the speaker know better, and that something in the situation shows he knows better.",
      "Bâ cer harfi, «تَأَوُّلٍ» mecrûr — «تَأَوَّلَ»nin TEFA'UL vezninde masdarı; câr-mecrûr «إِسْنَادُ»ya taalluk eder, lağvdır. Ve tarifi dürüst tutan şey bu tek kayıttır: bitirmeyi BAHARA nisbet edip buna inanan kimse mecâz yapmış olmaz, HATA etmiş olur. Mecâz, mütekellimin işin aslını bilmesini ve bunu gösteren bir karînenin bulunmasını ister.",
      segments=[seg("بِ","bi","prep"), seg("تَأَوُّلٍ","taawwul","noun")],
      punct="."),
 ],
 "jumal": [J("هُوَ لَهُ",
   "جُمْلَةٌ اسْمِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan isim cümlesi — mahalsizdir."),
  J("وَهُوَ إِسْنَادُ الْفِعْلِ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "«A pleased life» — the man was pleased with his life. «A filled torrent» — the torrent filled the valley.",
 "tr": "«Râzı olan hayat» — adam hayatından râzı oldu. «Doldurulmuş sel» — sel vadiyi doldurdu."},
 "tokens": [
  tok("عِيشَةٌ","isha","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَسَوَّغَ الِابْتِدَاءَ بِالنَّكِرَةِ كَوْنُهَا مَوْصُوفَةً.",
      "The mubtada in raf' — and what licenses beginning with an indefinite is that it is DESCRIBED. An indefinite may not open a sentence bare, but an indefinite with a sifa may, and this two-word phrase is the standard example of the rule.",
      "Merfû mübtedâ — nekre ile ibtidâyı câiz kılan şey, onun MEVSÛF olmasıdır. Nekre çıplak hâlde cümleye başlayamaz, sıfatlı olarak başlayabilir; bu iki kelimelik terkîb de kāidenin meşhur misalidir."),
  tok("رَاضِيَةٌ","radi","noun",["mubtada-khabar","ism-fail","naqis-verbs","majaz-aqli"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «رَضِيَ» النَّاقِصِ، وَالتَّاءُ لِلتَّأْنِيثِ. وَالْإِسْنَادُ مَجَازٌ عَقْلِيٌّ: أُسْنِدَ الْمَبْنِيُّ لِلْفَاعِلِ إِلَى الْمَفْعُولِ بِهِ، فَالْعِيشَةُ مَرْضِيَّةٌ لَا رَاضِيَةٌ.",
      "The khabar in raf' — the ism fa'il of the defective verb رَضِيَ, with the ta of the feminine. And the attribution is an INTELLECTUAL FIGURE: an active participle has been hung on the OBJECT. A life does not do any being-pleased; it is what somebody is pleased WITH. Every word here is literal — عِيشَة means a life and رَاضِيَة means pleased — and what has moved is the attribution alone. That is the whole difference between this majaz and the kind that moves a word.",
      "Merfû haber — NÂKIS «رَضِيَ»nin ism-i fâili; tâ müennesliktir. İsnâd ise MECÂZ-I AKLÎdir: mebnî lil-fâil olan bir vasıf, MEF'ÛLE isnâd edilmiştir. Hayat râzı olmaz; kendisinden râzı olunandır. Buradaki her kelime hakîkîdir — «عِيشَة» hayat, «رَاضِيَة» râzı demektir — yer değiştiren yalnız isnâddır. Bu mecâzı, kelimeyi yerinden oynatan mecâzdan ayıran şey tam budur.",
      punct="—"),
  tok("رَضِيَ","radiya","verb",["fail","naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — نَاقِصٌ يَائِيٌّ.",
      "A mazi verb, mabni on the fatha — a defective verb whose lam is a ya. This is the sentence underneath the figure: same meaning, ordinary attribution, and four words instead of two.",
      "Fetha üzere mebnî mâzî fiil — nâkıs yâî. Mecâzın altındaki cümle budur: aynı mânâ, sıradan isnâd; iki kelime yerine dört kelime."),
  tok("الرَّجُلُ","rajul","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — وَهُوَ الرَّاضِي حَقِيقَةً، وَقَدْ كَانَ غَائِبًا عَنِ الْمَجَازِ رَأْسًا.",
      "The fa'il in raf' — and HE is the one really doing the being-pleased. Notice that he was absent from the figure altogether: «a pleased life» has nobody in it, and restoring him is what the literal sentence is for.",
      "Merfû fâil — hakîkatte râzı olan odur; ve mecâzda hiç yoktu: «râzı olan hayat» ifadesinde kimse yok. Hakîkî cümlenin işi, onu geri getirmektir."),
  tok("عِيشَتَهُ","isha","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَهُوَ الَّذِي حَمَلَ الْوَصْفَ فِي الْمَجَازِ.",
      "The object in nasb, a mudaf with the ha annexed — and it is the very word that carried the description in the figure. The word that was the SUBJECT of the figure is the OBJECT of the truth; that swap is the mechanism.",
      "Mansub mef'ûlün bih, muzâf; hâ muzâfun ileyhtir — ve mecâzda vasfı taşıyan kelimenin ta kendisi. Mecâzda ÖZNE olan, hakîkatte MEF'ÛLdür; mekanizma bu yer değiştirmedir.",
      punct="."),
  tok("سَيْلٌ","sayl","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ مَوْصُوفَةٌ كَالْأُولَى.",
      "The mubtada in raf' — a described indefinite, like the first one.",
      "Merfû mübtedâ — birincisi gibi mevsûf nekre."),
  tok("مُفْعَمٌ","mufam","noun",["mubtada-khabar","ism-maful","form-iv-verbs","majaz-aqli"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «أَفْعَمَ» عَلَى مُفْعَلٍ، وَجَذْرُهُ «ف ع م». وَالْإِسْنَادُ مَجَازٌ عَقْلِيٌّ عَلَى الْعَكْسِ مِنَ الْأَوَّلِ: أُسْنِدَ الْمَبْنِيُّ لِلْمَفْعُولِ إِلَى الْفَاعِلِ، فَالسَّيْلُ مُفْعِمٌ لَا مُفْعَمٌ.",
      "The khabar in raf' — the ism maf'ul of أَفْعَمَ on مُفْعَل, and its ROOT IS ف ع م. Say the two aloud: the verb and the scale that measures it are spelled with the same three letters, which is the shortest proof available that a wazn is a MOULD and not a spelling. And the figure runs the OTHER WAY from the first: here a PASSIVE participle has been hung on the doer. A torrent does no being-filled; it fills. Two examples, one on each side of the boundary — that is why the books always give them as a pair.",
      "Merfû haber — «أَفْعَمَ»nin MUF'AL vezninde ism-i mef'ûlü; ve KÖKÜ «ف ع م»dir. İkisini yüksek sesle söyleyin: fiil ile onu ölçen vezin aynı üç harfle yazılıyor; bir veznin YAZILIŞ değil KALIP olduğunun en kısa ispatı budur. İsnâd da birincinin TERSİ yönde mecâz-ı aklîdir: burada MEF'ÛL vasfı FÂİLE isnâd edilmiştir. Sel doldurulmaz, doldurur. Sınırın iki yanından birer misal — kitapların bu ikisini hep birlikte vermesinin sebebi budur."),
  tok("أَفْعَمَ","afama","verb",["fail","maful-bihi","form-iv-verbs"],
      "فِعْلٌ مَاضٍ عَلَى أَفْعَلَ — وَوَزْنُهُ وَحُرُوفُهُ سَوَاءٌ لِأَنَّ جَذْرَهُ «ف ع م».",
      "A mazi verb on أَفْعَلَ — and its scale and its letters coincide, because its root is ف ع م. The app's mizan engine still derives the scale from the root rather than reading it off the page, which is the only reason it does not report a coincidence as a discovery.",
      "أَفْعَلَ vezninde mâzî fiil — kökü «ف ع م» olduğu için vezni ile harfleri çakışır. Uygulamanın mîzân motoru vezni yine de sayfadan okumaz, kökten türetir; bir tesadüfü keşif diye bildirmemesinin tek sebebi budur.",
      punct=None),
  tok("السَّيْلُ","sayl","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — وَهُوَ الْمُفْعِمُ حَقِيقَةً.",
      "The fa'il in raf' — and it is the FILLER in reality, which is precisely the participle the figure refused to use.",
      "Merfû fâil — ve hakîkatte DOLDURAN odur; mecâzın kullanmaktan kaçındığı ism-i fâil de tam budur."),
  tok("الْوَادِيَ","waadi","noun",["maful-bihi","ism-maqsur-manqus"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ الظَّاهِرَةُ عَلَى الْيَاءِ — اسْمٌ مَنْقُوصٌ مُعَرَّفٌ بِأَلْ، فَثَبَتَتْ يَاؤُهُ.",
      "The object in nasb, its sign the fatha WRITTEN on the ya — a manqus made definite by the article, so the ya stands. Three chapters have now shown this noun class in every state it has: خَالِي الذِّهْنِ in jarr with the kasra estimated, the same phrase in raf' with the damma estimated, and here the fatha alone, actually written. The rule is that a manqus writes only its fatha, and the library now demonstrates it rather than asserting it.",
      "Mansub mef'ûlün bih; nasb alâmeti yâ üzerine YAZILMIŞ fethadır — elif-lâm ile marife menkūs olduğundan yâsı sâbit kalmıştır. Üç bâb, bu isim sınıfını bütün hâlleriyle gösterdi: cerde «خَالِي الذِّهْنِ», kesrası mukadder; aynı terkîb ref'de, dammesi mukadder; ve burada yalnız fetha, hem de yazılı olarak. Kāide, menkūsun yalnız fethasını yazdığıdır; kütüphane artık bunu iddia etmiyor, gösteriyor.",
      punct="."),
 ],
 "jumal": [J("رَضِيَ الرَّجُلُ عِيشَتَهُ",
   "جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, with no position in i'rab.",
   "Fiil cümlesi; i'râbdan mahalli yoktur."),
  J("أَفْعَمَ السَّيْلُ الْوَادِيَ",
   "جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, with no position in i'rab.",
   "Fiil cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "«Poetry that composes.» «His daytime is fasting.» «A running river» — the river's water ran.",
 "tr": "«Şiir söyleyen şiir.» «Gündüzü oruçludur.» «Akan nehir» — nehrin suyu aktı."},
 "tokens": [
  tok("شِعْرٌ","shir","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "The mubtada in raf'.",
      "Merfû mübtedâ."),
  tok("شَاعِرٌ","shair","noun",["mubtada-khabar","ism-fail","majaz-aqli"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ، وَالْإِسْنَادُ إِلَى الْمَصْدَرِ: حَقِيقَتُهُ «شَعَرَ الرَّجُلُ شِعْرَهُ».",
      "The khabar in raf' — an ism fa'il, and the attribution is to the MASDAR. Poetry does not compose; a man composes poetry. This is the third mulabis of the six, and notice that the figure is only two words long: the shorter it is, the more of the sentence the hearer has to supply.",
      "Merfû haber — ism-i fâil; ve isnâd MASDARA yapılmıştır: hakîkati «شَعَرَ الرَّجُلُ شِعْرَهُ»dur. Şiir şiir söylemez; adam şiir söyler. Altı mülâbesin üçüncüsü budur; ve mecâzın yalnız iki kelime olduğuna dikkat: ne kadar kısaysa, muhâtabın tamamlaması gereken o kadar çoktur.",
      punct="."),
  tok("نَهَارُهُ","nahar","noun",["mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "The mubtada in raf', a mudaf with the ha annexed to it. The pronoun is what makes it definite, and the sentence needs a definite mubtada because no sifa is coming to license an indefinite one.",
      "Merfû mübtedâ, muzâf; hâ muzâfun ileyhtir. Onu marife yapan şey zamirdir; ve bu cümlenin marife mübtedâya ihtiyacı var, zira nekreyi câiz kılacak bir sıfat gelmiyor."),
  tok("صَائِمٌ","saim","noun",["mubtada-khabar","ism-fail","hollow-verbs","majaz-aqli"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «صَامَ» الْأَجْوَفِ: أَصْلُهُ «صَاوِمٌ»، قُلِبَتِ الْعَيْنُ هَمْزَةً لِوُقُوعِهَا بَعْدَ أَلِفِ فَاعِلٍ. وَالْإِسْنَادُ إِلَى الزَّمَانِ، وَحَقِيقَتُهُ «صَامَ الرَّجُلُ نَهَارَهُ».",
      "The khabar in raf' — the ism fa'il of the HOLLOW verb صَامَ. Its origin is صَاوِمٌ: the middle radical fell after the alif of فَاعِل and turned into a HAMZA, which is the same step that gives قَائِل and بَائِع. And the attribution is to the TIME: a daytime does not fast, a man fasts during it. Fourth mulabis, and it is the one that most often passes unnoticed, because English says «a busy morning» without blinking.",
      "Merfû haber — AJVEF «صَامَ»nin ism-i fâili: aslı «صَاوِمٌ»dur; ayn harfi, fâil kalıbının elifinden sonra düştüğü için HEMZEYE kalbolmuştur — «قَائِل» ve «بَائِع»i veren adımın aynısı. İsnâd ise ZAMANA yapılmıştır: gündüz oruç tutmaz, adam gündüzünde oruç tutar. Dördüncü mülâbes budur ve çoğu zaman fark edilmeden geçen odur; zira Türkçe de «yoğun bir sabah» der ve kimse şaşırmaz.",
      punct="."),
  tok("نَهْرٌ","nahr","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — نَكِرَةٌ مَوْصُوفَةٌ.",
      "The mubtada in raf' — a described indefinite.",
      "Merfû mübtedâ — mevsûf nekre."),
  tok("جَارٍ","jari","noun",["mubtada-khabar","ism-fail","ism-maqsur-manqus","naqis-verbs","majaz-aqli"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمٌ مَنْقُوصٌ نَكِرَةٌ، حُذِفَتْ يَاؤُهُ وَعُوِّضَ عَنْهَا التَّنْوِينُ. وَالْإِسْنَادُ إِلَى الْمَكَانِ: حَقِيقَتُهُ «جَرَى مَاءُ النَّهْرِ».",
      "The khabar in raf' by a damma estimated on a ya that IS NOT THERE — an indefinite manqus: the ya is deleted and the tanwin stands in its place. Set it beside الْوَادِيَ one sentence back and the class is complete: definite and in nasb, the ya and its fatha are both written; indefinite and in raf', the ya is gone and only a tanwin marks the spot. And the attribution is to the PLACE — a river does not run, its water runs in it.",
      "Merfû haber; ref' alâmeti, OLMAYAN bir yâ üzerinde takdîr edilen dammedir — nekre menkūs: yâsı hazfedilmiş, yerine tenvîn getirilmiştir. Bir cümle önceki «الْوَادِيَ» ile yan yana koyun, sınıf tamamlanır: marife ve mansub iken yâ da fethası da yazılı; nekre ve merfû iken yâ yok, yerinde yalnız bir tenvîn. İsnâd ise MEKÂNA yapılmıştır — nehir akmaz, suyu onun içinde akar.",
      punct="—"),
  tok("جَرَى","jara","verb",["fail","naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — نَاقِصٌ يَائِيٌّ.",
      "A mazi verb, mabni on a fatha ESTIMATED on the alif because the alif cannot bear one — a defective verb whose lam is a ya. Its participle is the جَارٍ two words back: the reader has just seen the finished noun and now sees the verb it came from.",
      "Elif hareke kabul etmediği için üzerinde MUKADDER fetha ile mebnî mâzî fiil — nâkıs yâî. İsm-i fâili, iki kelime önceki «جَارٍ»dir: okuyucu önce bitmiş ismi gördü, şimdi geldiği fiili görüyor."),
  tok("مَاءُ","ma-water","noun",["fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَهُوَ الْجَارِي حَقِيقَةً.",
      "The fa'il in raf' and a mudaf — and it is the thing that really runs.",
      "Merfû fâil ve muzâf — hakîkatte akan odur."),
  tok("النَّهْرِ","nahr","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْمَكَانُ الَّذِي كَانَ مُبْتَدَأً فِي الْمَجَازِ صَارَ مُضَافًا إِلَيْهِ فِي الْحَقِيقَةِ.",
      "The mudaf ilayh in jarr — and the PLACE that was the subject of the figure has become a mudaf ilayh in the truth. In every one of these pairs the word that was raised in the figure is demoted in the literal sentence: that demotion is the figure, stated backwards.",
      "Mecrûr muzâfun ileyh — ve mecâzda mübtedâ olan MEKÂN, hakîkatte muzâfun ileyh olmuştur. Bu çiftlerin hepsinde, mecâzda yükseltilen kelime hakîkî cümlede indirilir: mecâzın kendisi, tersinden söylenmiş bu indirmedir.",
      punct="."),
 ],
 "jumal": [J("جَرَى مَاءُ النَّهْرِ",
   "جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, with no position in i'rab.",
   "Fiil cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "«The commander built the city.» «And the earth brought forth its burdens.» «A day that makes children grey-haired.»",
 "tr": "«Emîr şehri binâ etti.» «Ve yer ağırlıklarını çıkardı.» «Çocukları ak saçlı kılan bir gün.»"},
 "tokens": [
  tok("بَنَى","bana","verb",["fail","maful-bihi","naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — نَاقِصٌ يَائِيٌّ.",
      "A mazi verb, mabni on an estimated fatha — a defective verb whose lam is a ya. Second one in two sentences, and both write an alif where the ya belongs.",
      "Mukadder fetha üzere mebnî mâzî fiil — nâkıs yâî. İki cümlede ikincisi; ve ikisi de yânın yerine elif yazıyor."),
  tok("الْأَمِيرُ","amir","noun",["fail","sifa-mushabbaha"],
      "فَاعِلٌ مَرْفُوعٌ — وَالْإِسْنَادُ إِلَيْهِ مَجَازٌ عَقْلِيٌّ، إِذِ الْبَانِي هُمُ الْفَعَلَةُ بِأَمْرِهِ، فَهُوَ السَّبَبُ لَا الْفَاعِلُ.",
      "The fa'il in raf' — and attributing the building to HIM is an intellectual figure: the builders are the workmen, and he is the CAUSE, not the doer. This is the sixth and last mulabis, and it is the one that runs through ordinary speech unremarked in every language: «the government built a road». The figure is invisible precisely because it is so useful.",
      "Merfû fâil — ve binâyı ONA isnâd etmek mecâz-ı aklîdir: binâ edenler, emriyle çalışan işçilerdir; o SEBEPtir, fâil değil. Altı mülâbesin sonuncusu budur ve her dilde sıradan konuşmanın içinden fark edilmeden geçen odur: «devlet yol yaptı». Mecâz, tam da çok işe yaradığı için görünmez."),
  tok("الْمَدِينَةَ","madina","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "The object in nasb.",
      "Mansub mef'ûlün bih.",
      punct="."),
  tok("وَأَخْرَجَتِ","akhraja","verb",["fail","maful-bihi","form-iv-verbs"],
      "الْوَاوُ حَسَبَ مَا قَبْلَهَا، وَ«أَخْرَجَتْ» فِعْلٌ مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ السَّاكِنَةُ، كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ مَعَ لَامِ التَّعْرِيفِ.",
      "The waw as its context takes it, and «brought forth» is a mazi verb whose ta is the QUIESCENT ta of the feminine — vowelled with a kasra here only because the definite article's sukun follows it and two quiescents cannot meet. The kasra is not i'rab and not sarf; it is a repair, and the app's harakat auditor is built to tell the three apart.",
      "Vâv, öncesine göredir; «أَخْرَجَتْ» mâzî fiildir ve tâsı SÂKİN te'nîs tâsıdır — buradaki kesra yalnızca ardından gelen lâm-ı ta'rîfin sükûnu sebebiyledir; iki sâkin yan yana gelmez. Bu kesra ne i'râb ne sarftır, bir TAMİRdir; uygulamanın hareke denetçisi de bu üçünü ayırmak için yapılmıştır.",
      segments=[seg("وَ","wa","conj"), seg("أَخْرَجَتِ","akhraja","verb")]),
  tok("الْأَرْضُ","ard","noun",["fail","majaz-aqli"],
      "فَاعِلٌ مَرْفُوعٌ — وَالْإِسْنَادُ إِلَى الْمَكَانِ، إِذِ الْمُخْرِجُ هُوَ اللهُ تَعَالَى.",
      "The fa'il in raf' — and the attribution is to the PLACE, since the One who brings forth is Allah. The Qur'an is full of this figure, and naming it is not a hedge about the verse: it is the classical way of saying that the earth is where the bringing-forth happens, not the one who does it.",
      "Merfû fâil — ve isnâd MEKÂNA yapılmıştır; zira çıkaran Allah Teâlâ'dır. Kur'ân-ı Kerîm bu mecâzla doludur; ve onu adlandırmak âyet hakkında bir ihtiyat değildir: yerin, çıkarma işinin FÂİLİ değil MAHALLİ olduğunu söylemenin klasik yoludur."),
  tok("أَثْقَالَهَا","thiql","noun",["maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — جَمْعُ تَكْسِيرٍ لِـ«ثِقْلٍ» عَلَى أَفْعَالٍ.",
      "The object in nasb, a mudaf with the ha annexed — a broken plural of ثِقْل on أَفْعَال.",
      "Mansub mef'ûlün bih, muzâf; hâ muzâfun ileyhtir — «ثِقْل»in AF'ÂL vezninde cem'-i teksîri.",
      punct="."),
  tok("يَوْمًا","yawm","noun",["maful-fih","jumla-sifa"],
      "مَفْعُولٌ فِيهِ ظَرْفُ زَمَانٍ مَنْصُوبٌ — نَكِرَةٌ، وَالْجُمْلَةُ بَعْدَهُ فِي مَحَلِّ نَصْبٍ نَعْتٌ لَهُ.",
      "An adverbial object, a zarf of TIME in nasb — indefinite, and the clause after it stands in the position of nasb as its na't. A sentence describing an indefinite is a sifa; the same sentence after a definite would be a hal. One rule, and the tanwin decides which side of it you are on.",
      "Mansub zaman zarfı — nekre; ve ardındaki cümle onun na'tı olarak mahallen mansubdur. Nekreyi vasfeden cümle sıfattır; aynı cümle marifeden sonra gelse hâl olurdu. Tek kāide; ve hangi tarafında olduğunuza tenvîn karar verir."),
  tok("يَجْعَلُ","jaala","verb",["mafulayn","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَهُوَ مِنْ أَفْعَالِ التَّصْيِيرِ، يَنْصِبُ مَفْعُولَيْنِ.",
      "A mudari' verb in raf', its fa'il concealed as «he» — and it is one of the verbs of MAKING-INTO, which take two objects. The fourth chapter in a row to hand the reader a doubly transitive verb, and the first to do it in the Qur'an.",
      "Merfû muzâri fiil; fâili müstetir «هُوَ» — ve TASYÎR fiillerindendir, iki mef'ûl nasbeder. Okuyucuya iki mef'ûllü fiil veren üst üste dördüncü bâb; ve bunu Kur'ân'da yapan ilki."),
  tok("الْوِلْدَانَ","walid","noun",["mafulayn","maful-bihi"],
      "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ — جَمْعُ «وَلِيدٍ».",
      "The FIRST object in nasb — the plural of وَلِيد, a newborn.",
      "Mansub BİRİNCİ mef'ûlün bih — «وَلِيد»in cem'i."),
  tok("شِيبًا","shayb","noun",["mafulayn","maful-bihi"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — جَمْعُ «أَشْيَبَ». وَالْإِسْنَادُ إِلَى الزَّمَانِ كَـ«نَهَارُهُ صَائِمٌ»، فَالْيَوْمُ ظَرْفُ الْفِعْلِ لَا فَاعِلُهُ.",
      "The SECOND object in nasb — the plural of أَشْيَب, grey-haired. And the attribution is to the TIME, exactly as in «his daytime is fasting» two sentences back: a day is WHEN the greying happens, not what does it. The chapter ends by putting the plainest example of the doctrine and its Qur'anic parallel four lines apart, which is what a matn is for.",
      "Mansub İKİNCİ mef'ûlün bih — «أَشْيَب»in cem'i. İsnâd ise, iki cümle önceki «نَهَارُهُ صَائِمٌ» gibi ZAMANA yapılmıştır: gün, ağarmanın FÂİLİ değil VAKTİdir. Bâb, doktrinin en sade misali ile Kur'ânî nazîresini dört satır arayla koyarak biter; bir metnin işi de budur.",
      punct="."),
 ],
 "jumal": [J("بَنَى الْأَمِيرُ الْمَدِينَةَ",
   "جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, with no position in i'rab.",
   "Fiil cümlesi; i'râbdan mahalli yoktur."),
  J("يَجْعَلُ الْوِلْدَانَ شِيبًا",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ نَصْبٍ نَعْتٌ لِـ«يَوْمًا».",
   "A verbal sentence in the position of nasb as the na't of «a day».",
   "«يَوْمًا»ya na't olarak mahallen mansub fiil cümlesi.")]})

GLOSS_ADD = {
 "hiya":     g("هِيَ", None, "pron", "she, it (feminine detached pronoun)", "o (müennes munfasıl zamir)", 1),
 "huwa":     g("هُوَ", None, "pron", "he, it (detached pronoun)", "o (munfasıl zamir)", 1),
 "fil":      g("فِعْل", "ف ع ل", "noun", "act, deed; a verb", "fiil; iş", 1, plural="أَفْعَال"),
 "aw":       g("أَوْ", None, "conj", "or (here: giving a variety, not a doubt)", "veya (burada: tenvî için, şek için değil)", 1),
 "mana":     g("مَعْنًى", "ع ن ي", "noun", "meaning (a maqsur noun)", "mânâ (ism-i maksûr)", 2, plural="مَعَانٍ"),
 "ila":      g("إِلَى", None, "prep", "to, towards", "-e, -a doğru", 1),
 "ma-mawsula": g("مَا (المَوْصُولَة)", None, "pron", "that which, what (relative)", "o şey ki (ism-i mevsûl)", 2),
 "li":       g("لِ", None, "prep", "for, belonging to", "için, -e âit", 1),
 "inda":     g("عِنْد", None, "noun", "with, in the view of (a zarf — a noun, not a letter)", "yanında, indinde (zarf — harf değil, isim)", 2),
 "fi":       g("فِي", None, "prep", "in", "-de, içinde", 1),
 "zahir":    g("ظَاهِر", "ظ ه ر", "noun", "outward, apparent (ism fa'il)", "zâhir, dıştan görünen (ism-i fâil)", 3),
 "mulabas":  g("مُلَابَس", "ل ب س", "noun", "a thing associated with another (ism maf'ul, Form III)", "mülâbes; bir şeyle alâkalı olan (ism-i mef'ûl, mufâale)", 5),
 "taawwul":  g("تَأَوُّل", "أ و ل", "noun", "an interpretation, a construing (masdar, Form V)", "te'vîl, yorumlama (masdar, tefa'ul)", 5),
 "isha":     g("عِيشَة", "ع ي ش", "noun", "a life, a way of living", "hayat, yaşayış", 3),
 "radi":     g("رَاضٍ (الرَّاضِي)", "ر ض و", "noun", "pleased, content (ism fa'il of a defective verb)", "râzı olan (nâkıstan ism-i fâil)", 4),
 "sayl":     g("سَيْل", "س ي ل", "noun", "a torrent, a flood", "sel", 3, plural="سُيُول"),
 "mufam":    g("مُفْعَم", "ف ع م", "noun", "filled up (ism maf'ul of أَفْعَمَ)", "doldurulmuş (أَفْعَمَ'den ism-i mef'ûl)", 5),
 "afama":    g("أَفْعَمَ", "ف ع م", "verb", "to fill something to the brim", "ağzına kadar doldurmak", 5, form="IV"),
 "waadi":    g("وَادِي (وَادٍ)", "و د ي", "noun", "a valley, a watercourse (manqus)", "vadi (menkūs)", 3, plural="أَوْدِيَة"),
 "shir":     g("شِعْر", "ش ع ر", "noun", "poetry", "şiir", 2, plural="أَشْعَار"),
 "shair":    g("شَاعِر", "ش ع ر", "noun", "a poet; composing poetry (ism fa'il)", "şair; şiir söyleyen (ism-i fâil)", 2),
 "nahar":    g("نَهَار", "ن ه ر", "noun", "daytime", "gündüz", 2),
 "saim":     g("صَائِم", "ص و م", "noun", "fasting (ism fa'il of a hollow verb)", "oruçlu (ecvefden ism-i fâil)", 3),
 "saama":    g("صَامَ", "ص و م", "verb", "to fast", "oruç tutmak", 2, form="I"),
 "nahr":     g("نَهْر", "ن ه ر", "noun", "a river", "nehir", 2, plural="أَنْهَار"),
 "jari":     g("جَارٍ (الْجَارِي)", "ج ر ي", "noun", "running, flowing (ism fa'il, manqus)", "akan, câri (ism-i fâil, menkūs)", 3),
 "bana":     g("بَنَى", "ب ن ي", "verb", "to build", "binâ etmek, yapmak", 2, form="I"),
 "amir":     g("أَمِير", "أ م ر", "noun", "a commander, a prince", "emîr, kumandan", 2, plural="أُمَرَاء"),
 "thiql":    g("ثِقْل", "ث ق ل", "noun", "a burden, a weight", "yük, ağırlık", 4, plural="أَثْقَال"),
 "walid":    g("وَلِيد", "و ل د", "noun", "a newborn, a child", "yeni doğmuş çocuk", 3, plural="وِلْدَان"),
 "shayb":    g("أَشْيَب", "ش ي ب", "noun", "grey-haired", "ak saçlı", 4, plural="شِيب"),
 "labasa":   g("لَابَسَ", "ل ب س", "verb", "to be closely connected with", "bir şeyle iç içe olmak, mülâbeset etmek", 5, form="III"),
 # COPIED from other packages, lemma-identical — a lex key is global. The gloss
 # is package-local, so مَاء is glossed as water here rather than as the «water
 # of the face» the Samti wasiyya needed.
 "radiya":   g("رَضِيَ", "ر ض ي", "verb", "to be content with, accept", "razı olmak", 2, form="I"),
 "rajul":    g("رَجُل", "ر ج ل", "noun", "man", "adam, er", 1, plural="رِجَال"),
 "jara":     g("جَرَى", "ج ر ي", "verb", "to flow, run its course", "akmak, cereyan etmek", 3, form="I"),
 "ma-water": g("مَاء", "م و ه", "noun", "water", "su", 2, plural="مِيَاه"),
 "madina":   g("مَدِينَة", "م د ن", "noun", "city", "şehir", 1, plural="مُدُن"),
 "ard":      g("أَرْض", "أ ر ض", "noun", "land, earth", "arazi, yer", 1, plural="أَرَاضٍ"),
 "yawm":     g("يَوْم", "ي و م", "noun", "day", "gün", 1, plural="أَيَّام"),
 "jaala":    g("جَعَلَ", "ج ع ل", "verb", "to make, set", "kılmak, yapmak", 2, form="I"),
 # …and the two verbs shipped for their PARADIGMS rather than for a token: the
 # cells مُلَابِس / مُلَابَس are the nusha divergence this chapter records, and
 # صَامَ is where صَائِم comes from.
 "taawwala": g("تَأَوَّلَ", "أ و ل", "verb", "to construe, to interpret", "te'vîl etmek, yorumlamak", 5, form="V"),
}

def build_morph():
    out = {}
    # COPIED after a lemma-identity assert — a lex key is global.
    for pkg, lex in [("wasiyyat-abi-hanifa-samti", "radiya"),
                     ("wasiyyat-abi-hanifa-samti", "jara"),
                     ("wasiyyat-abi-hanifa-samti", "akhraja"),
                     ("wasiyyat-abi-hanifa-samti", "jaala")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    # صَامَ — Form I AJWAF WAWI, bab nasara. Its ism fa'il صَائِم is the point of
    # s4: the ayn falls after the alif of فَاعِل and turns hamza.
    out["saama"] = _sg.hollow1("nasara", "أَجْوَفُ وَاوِيٌّ", "صَام", "صُم", "صُوم", "صُم",
                               "صُوم", "صُم", "صَوْم", "صَائِم",
                               note=_sg.HOLLOW_NOTE.format(ex="صُمْتَ"))
    # بَنَى — Form I NAQIS YA'I, bab daraba, with its passive.
    out["bana"] = _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "بَنَ", "بْن", "i", "اِبْن",
                             "بِنَاء", "بَانٍ (الْبَانِي)", "مَبْنِيّ",
                             "بُنِيَ", "يُبْنَى", _sg.NAQIS_Y_NOTE)
    # أَفْعَمَ — Form IV sound, and its ROOT IS ف ع م, so the paradigm and the
    # mizan that measures it are spelled alike. Kept because that coincidence
    # is the shortest available proof that a wazn is a mould, not a spelling.
    out["afama"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْعَم", "فْعِم", "أَفْعِم",
                               "إِفْعَام", "مُفْعِم", maful="مُفْعَم",
                               pmz="أُفْعِمَ", pmd="يُفْعَمُ",
                               note="جَذْرُهُ «ف ع م»، فَوَافَقَ لَفْظُهُ وَزْنَهُ — وَالْوَزْنُ قَالَبٌ لَا هِجَاءٌ.")
    # لَابَسَ — Form III sound. Shipped for ONE reason: the chapter's key word is
    # its participle, and the two candidate readings of the matn are مُلَابِس and
    # مُلَابَس — two cells of this very paradigm, one line apart.
    out["labasa"] = _sg.derived(_sg.B3, _sg.W3, "ُ", "لَابَس", "لَابِس", "لَابِس",
                                "مُلَابَسَة", "مُلَابِس", maful="مُلَابَس",
                                pmz="لُوبِسَ", pmd="يُلَابَسُ")
    # تَأَوَّلَ — Form V. Its fa is a HAMZA, so the reader's conjugator refuses the
    # root and the audit skips it; seat orthography is not derivable.
    out["taawwala"] = _sg.derived(_sg.B5, _sg.W5, "َ", "تَأَوَّل", "تَأَوَّل", "تَأَوَّل",
                                  "تَأَوُّل", "مُتَأَوِّل", maful="مُتَأَوَّل")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/5.json").write_text(
    json.dumps({"chapter": 5, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 5 for c in man["chapters"]):
    man["chapters"].append({"n": 5, "title": TITLE5})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.5.0"
DIV_EN = (" Chapter 5's Arabic is likewise VERBATIM from that file (its two matn definitions, "
          "vowelled, and the six examples each with the literal sentence the commentary gives "
          "beneath it); the example sentences juxtapose two of the source's own phrases with a "
          "dash between them, and no connective has been composed to join them. ONE DIVERGENCE "
          "is recorded here rather than hidden: the source vowels the definition's key word "
          "مُلَابَسٍ (ism maf'ul) and repeats that vowelling in its own question about the term, "
          "while printed editions of the Talkhis commonly write مُلَابِسٍ (ism fa'il). The reading "
          "shown is the source's; the paradigm shipped for لَابَسَ carries both cells.")
DIV_TR = (" Beşinci bâbın Arapçası da aynı dosyadan AYNEN alınmıştır (matnin iki tarifi harekeli "
          "olarak ve altı misalin her biri, şerhin altına koyduğu hakîkî cümlesiyle birlikte); "
          "misal cümleleri, kaynağın kendi iki ibaresini aralarına bir çizgi koyarak yan yana "
          "getirir ve onları birleştirmek için hiçbir bağlaç telif edilmemiştir. BİR NÜSHA "
          "İHTİLÂFI gizlenmeyip buraya kaydedilmiştir: kaynak, tarifin anahtar kelimesini "
          "مُلَابَسٍ (ism-i mef'ûl) diye harekeler ve terim hakkındaki kendi suâlinde de aynı "
          "harekeyi tekrarlar; matbû Telhîs nüshaları ise çoğunlukla مُلَابِسٍ (ism-i fâil) yazar. "
          "Gösterilen okuyuş kaynağınkidir; «لَابَسَ» için taşınan çekim iki hâneyi de içerir.")
if "مُلَابَسٍ" not in man["attribution"]["en"]:
    man["attribution"]["en"] += DIV_EN
    man["attribution"]["tr"] += DIV_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch5:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
