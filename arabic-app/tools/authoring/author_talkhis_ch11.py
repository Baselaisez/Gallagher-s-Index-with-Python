# -*- coding: utf-8 -*-
"""Author chapter 11 of talkhis-al-miftah — تَقْدِيمُ الْمُسْنَدِ إِلَيْهِ وَضَمِيرُ الْفَصْلِ.

The chapter that closes the musnad-ilayh bab. Everything before it chose the
WORD — say it or drop it, definite this way or that, dressed with which tabi'.
This one chooses the PLACE: why does the subject come first, and what happens
when it comes first after a negation?

Fronting is the ASL — the subject's mention matters more — and the book counts
the reasons a speaker leans on it: to plant the khabar in a hearer already
made curious (Abū al-ʿAlāʾ's bayt keeps mankind's bewilderment waiting a whole
hemistich for its resolution); to HASTEN JOY (سَعْدٌ فِي دَارِكَ — the lucky name
first); to hasten grief (السَّفَّاحُ فِي دَارِ صَدِيقِكَ — the shedder of blood
first); to say the subject never leaves the mind (اللَّهُ إِلَهُنَا وَمُحَمَّدٌ
نَبِيُّنَا); and for the sheer pleasure of saying it (حَبِيبِي يَجِيءُ).

Then ضَمِيرُ الْفَصْلِ — زَيْدٌ هُوَ الْقَائِمُ — a pronoun with NO position in
i'rab, standing between mubtada and khabar to say the next word is the khabar
and not an adjective, and to CONFINE the khabar to the subject.

And last, عَبْدُ الْقَاهِرِ's rule: when the fronted subject FOLLOWS the negation
(مَا أَنَا قُلْتُ هَذَا), the fronting means takhsis — «it was not I who said
it» — and CONCEDES that someone did. That is why مَا أَنَا قُلْتُ هَذَا وَلَا
غَيْرِي is ruled a contradiction. Without the negation (أَنَا سَعَيْتُ فِي
حَاجَتِكَ) the takhsis answers a hearer who credited the wrong man, and THERE
the confirmation لَا غَيْرِي is legitimate — the mirror pair is the lesson.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~935-990, which carries
all of it in vowelled Arabic: Abū al-ʿAlāʾ's bayt, the four prose examples,
زَيْدٌ هُوَ الْقَائِمُ, and ʿAbd al-Qāhir's مَا أَنَا قُلْتُ هَذَا with
أَنَا سَعَيْتُ فِي حَاجَتِكَ لَا غَيْرِي. Nothing is composed.

Grammar this chapter is chosen to teach:
  • the fasl pronoun as a STRUCTURE the analyzer now recognises — a detached
    pronoun between a noun and an ال-definite, offered as a shortlist.
  • the ʿAbd al-Qāhir frame as a MaEngine rule — مَا + detached pronoun +
    verb promotes the negation and names the takhsis.
  • حَارَتِ — a hollow māḍī behind the fem-ta, which the peel table read as
    فَاعِل with the suffix standing in as a radical.
  • السَّفَّاحُ on فَعَّال — the intensive read off the shadda the skeleton lost.
  • إِلَهُنَا/نَبِيُّنَا — the sign at the SEAM, not on the pronoun's own letters.
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

TITLE11 = {"ar": "تَقْدِيمُ الْمُسْنَدِ إِلَيْهِ وَضَمِيرُ الْفَصْلِ",
           "en": "Fronting the Subject, and the Pronoun of Separation",
           "tr": "Müsnedün İleyhin Takdîmi ve Zamîr-i Fasl"}

# ---------------------------------------------------------------- s1
# Abū al-ʿAlāʾ — fronting to plant the khabar in a hearer made curious.
S.append({"id": "s1", "translation": {
 "en": "And the one over whom mankind stands bewildered — is a living thing brought forth from lifeless matter.",
 "tr": "İnsanların hakkında hayrete düştüğü şey — cansız maddeden meydana getirilmiş bir canlıdır."},
 "tokens": [
  tok("وَالَّذِي","alladhi","pron",["taqdim-al-musnad-ilayh","ism-mawsul","mubtada-khabar"],
      "الْوَاوُ بِحَسَبِ مَا قَبْلَهَا، وَ«الَّذِي» اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — قُدِّمَ لِتَشْوِيقِ السَّامِعِ إِلَى الْخَبَرِ.",
      "The waw reads by what precedes it, and «the one who» is a relative, mabni, in the position of raf' as the mubtada — FRONTED to make the hearer crave the khabar. The whole first hemistich is spent describing a wonder without naming it; by the time the answer arrives the hearer has been made to want it. That is تَشْوِيق, and it is the second of the book's reasons for putting the subject first.",
      "Vâv, öncesine göre okunur; «الَّذِي» ise mebnî ism-i mevsûl olup mübtedâ olarak mahallen merfûdur — sâmi'i habere TEŞVÎK için ÖNE ALINMIŞTIR. Birinci mısraın tamamı, bir acâibi adlandırmadan tavsifle geçer; cevap geldiğinde muhâtab onu ister hâle getirilmiştir. Bu TEŞVÎKtir ve kitabın takdîm sebeplerinin ikincisidir.",
      segments=[seg("وَ","wa","conj"), seg("الَّذِي","alladhi","pron")]),
  tok("حَارَتِ","hara","verb",["jumla-sifa","hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ سَاكِنَةٌ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا.",
      "A hollow mazi, mabni on the fatha; the ta is the ta of femininity, itself sakin and broken to a kasra for the meeting of two quiescents with the article after it. The clause is the sila and has no position. The app's peel table used to read this word as فَاعِل with the suffix standing in as a THIRD RADICAL (« ح ر ت») — a final ta on this skeleton is a suffix, and the middle radical is the turned weak letter.",
      "Ecvef mâzî; fetha üzere mebnîdir. Tâ, te'nîs tâsıdır; kendisi sâkin iken ardındaki harf-i ta'rîfle iki sâkin buluştuğu için kesre almıştır. Cümle sıladır, mahalli yoktur. Uygulamanın soyma tablosu bu kelimeyi, ek üçüncü aslî harf sayılarak («ح ر ت») FÂİL vezninde okuyordu — bu iskelette son tâ ektir ve orta aslî harf, dönüşmüş illet harfidir.",
      segments=[seg("حَارَ","hara","verb"), seg("تِ","ta-tanith","part")]),
  tok("الْبَرِيَّةُ","bariyya","noun",["fail","anwa-al-lam-al-tarif"],
      "فَاعِلٌ مَرْفُوعٌ، وَ«ال» فِيهِ لِلِاسْتِغْرَاقِ الْعُرْفِيِّ — أَيِ النَّاسُ كَافَّةً.",
      "The fa'il, in raf' — «the created», mankind entire, its article the customary istighraq of chapter 9. All creation wonders; the totality is what makes the coming answer heavy.",
      "Merfû fâil — «yaratılmışlar», yani insanların tamamı; harf-i ta'rîfi, dokuzuncu bâbın örfî istiğrâkıdır. Bütün halk hayrettedir; gelecek cevâbı ağırlaştıran da bu bütünlüktür."),
  tok("فِيهِ","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«حَارَتْ»، لَغْوٌ — وَالْهَاءُ عَائِدُ الصِّلَةِ.",
      "A jarr and its majrur attaching to «stands bewildered» — laghw, its governor written. And the ha is the ʿAID of the sila, pointing back at the relative: the thread that makes the clause a sila at all.",
      "Câr-mecrûr, «حَارَتْ»a taalluk eder — lağvdır, âmili yazılıdır. Hâ ise sılanın ÂİDİdir, mevsûle döner: cümleyi sıla yapan ip odur.",
      segments=[seg("فِي","fi","prep"), seg("هِ","pron-3ms","pron")],
      punct="•"),
  tok("حَيَوَانٌ","hayawan","noun",["mubtada-khabar","tankir-al-musnad-ilayh"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ — نَكِرَةٌ لِلتَّعْظِيمِ وَالتَّنْوِيعِ: أَيُّ حَيَوَانٍ!",
      "The khabar, in raf' — and indefinite for magnification: WHAT a living thing! The hemistich boundary falls exactly between subject and predicate, so the verse form itself performs the delay the fronting was chosen for.",
      "Merfû haber — ve ta'zîm için nekredir: ne canlı ama! Mısra sınırı tam özne ile yüklem arasına düşer; böylece nazım şekli, takdîmin seçildiği geciktirmeyi bizzat icrâ eder."),
  tok("مُسْتَحْدَثٌ","mustahdath","noun",["naat-sifa","ism-maful","form-x-verbs"],
      "نَعْتٌ لِـ«حَيَوَانٌ» مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنِ اسْتَحْدَثَ عَلَى مُسْتَفْعَل.",
      "A na't of «a living thing», in raf' — the ism maf'ul of Form X اِسْتَحْدَثَ on مُسْتَفْعَل: brought newly into being. One fatha separates it from the ism fa'il مُسْتَحْدِث, and the fatha is the whole theology: the creature is made, not maker.",
      "«حَيَوَانٌ»un merfû na'tı — Form X «اِسْتَحْدَثَ»nin مُسْتَفْعَل veznindeki ism-i mef'ûlü: yeniden var edilmiş. Onu ism-i fâil «مُسْتَحْدِث»ten tek fetha ayırır ve o fetha bütün akîdedir: mahlûk yapandır değil, yapılandır."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ.",
      "A jarr letter of origin — out of.",
      "İbtidâ-i gāye için cer harfi — -den."),
  tok("جَمَادٍ","jamad","noun",["huruf-jarr","tankir-al-musnad-ilayh"],
      "مَجْرُورٌ بِـ«مِنْ»، مُتَعَلِّقٌ بِـ«مُسْتَحْدَثٌ» — نَكِرَةٌ لِلنَّوْعِيَّةِ.",
      "Majrur by «min», attaching to «brought forth» — the participle governing exactly as its verb would. Indefinite for KIND: from lifeless matter as such. The line is about resurrection — life made new from decayed bones — and says so without one theological term.",
      "«مِنْ» ile mecrûr, «مُسْتَحْدَثٌ»a taalluk eder — vasıf, tıpkı fiili gibi amel ediyor. NEV'İYYET için nekredir: cansız maddeden, cins olarak. Beyit yeniden diriliş hakkındadır — çürümüş kemiklerden yeniden hayat — ve bunu tek bir kelâm terimi kullanmadan söyler.",
      punct=".")],
 "jumal": [
  J("حَارَتِ الْبَرِيَّةُ فِيهِ",
    "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A verbal clause as the sila of the relative — no position in i'rab, and sealed: nothing inside it attaches to anything outside.",
    "Mevsûlün sılası olan fiil cümlesi — i'râbdan mahalli yoktur ve mühürlüdür: içindeki hiçbir şey dışarıya taalluk etmez.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "Saʿd is at your house. — The Shedder-of-Blood is at your friend's house.",
 "tr": "Sa'd senin evindedir. — Seffâh (kan dökücü) arkadaşının evindedir."},
 "tokens": [
  tok("سَعْدٌ","sad-name","propn",["taqdim-al-musnad-ilayh","mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — قُدِّمَ لِتَعْجِيلِ الْمَسَرَّةِ، إِذْ كَانَ اسْمُهُ مِمَّا يُتَيَمَّنُ بِهِ.",
      "The mubtada, in raf' — fronted to HASTEN THE JOY. The name means good fortune, and the speaker puts the lucky word first so the gladness arrives before the sentence does. Nothing in the grammar requires the order; the kindness does.",
      "Merfû mübtedâ — SEVİNCİ ACELE ETTİRMEK için öne alınmıştır. İsim, uğur demektir; mütekellim uğurlu kelimeyi öne koyar ki sevinç cümleden önce varsın. Sıralamayı gerektiren nahiv değildir; incelik gerektirir."),
  tok("فِي","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfi."),
  tok("دَارِكَ","dar","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ وَالْكَافُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرٌ، مُسْتَقَرٌّ.",
      "Majrur by «fi», a mudaf with the kaf annexed — the phrase standing in the position of raf' as the khabar, MUSTAQARR on an omitted amil.",
      "«فِي» ile mecrûr; muzâftır ve kâf muzâfun ileyhtir — câr-mecrûr, haber olarak mahallen merfûdur; mahzûf âmil üzere MÜSTAKARdır.",
      segments=[seg("دَارِ","dar","noun"), seg("كَ","pron-2ms","pron")],
      punct="."),
  tok("السَّفَّاحُ","saffah","noun",["taqdim-al-musnad-ilayh","sighat-mubalagha","anwa-al-lam-al-tarif"],
      "مُبْتَدَأٌ مَرْفُوعٌ — عَلَى فَعَّالٍ لِلْمُبَالَغَةِ، وَقُدِّمَ لِتَعْجِيلِ الْمَسَاءَةِ.",
      "The mubtada, in raf' — on فَعَّال, the intensive: not one who has shed blood but one who SHEDS it, by habit. Fronted to hasten the GRIEF: the dreadful word first, so the hearer braces before he learns where. The mirror of the sentence before it, and the same word order doing opposite work — which is this whole science in one pair. The app's scale-reader now says فَعَّال here: the shadda that decides it is on the vowelled word, though the bare skeleton loses it.",
      "Merfû mübtedâ — mübâlağa vezni فَعَّال üzere: kan dökmüş biri değil, âdet edinip DÖKEN. ÜZÜNTÜYÜ ACELE ETTİRMEK için öne alınmıştır: korkunç kelime önce gelir ki muhâtab nerede olduğunu öğrenmeden kendini toplasın. Önceki cümlenin aynası — ve aynı söz dizimi zıt işi görüyor; bu ilmin tamamı bu çifttedir. Uygulamanın vezin okuyucusu burada artık فَعَّال der: karâr veren şedde harekeli kelimededir, çıplak iskelet onu kaybeder.",
      punct=None),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfi."),
  tok("دَارِ","dar","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ.",
      "Majrur by «fi» and a mudaf — the chain runs on into the next word.",
      "«فِي» ile mecrûr ve muzâf — zincir sonraki kelimeye uzanır."),
  tok("صَدِيقِكَ","sadiq","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ أَيْضًا، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "The mudaf ilayh, in jarr — and itself a mudaf, the kaf annexed to it: a two-link chain, دَارِ صَدِيقِ كَ, each member majrur by the one before.",
      "Mecrûr muzâfun ileyh — ve kendisi de muzâftır; kâf ona muzâfun ileyhtir: iki halkalı zincir, her halka öncekiyle mecrûr.",
      segments=[seg("صَدِيقِ","sadiq","noun"), seg("كَ","pron-2ms","pron")],
      punct=".")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "Allah is our God, and Muhammad is our Prophet. — My beloved is coming.",
 "tr": "Allah ilâhımızdır, Muhammed peygamberimizdir. — Sevgilim geliyor."},
 "tokens": [
  tok("اللَّهُ","allah","propn",["taqdim-al-musnad-ilayh","mubtada-khabar"],
      "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ — قُدِّمَ لِلدَّلَالَةِ عَلَى أَنَّهُ لَا يَغِيبُ عَنِ الْخَاطِرِ.",
      "The lafz al-jalala as mubtada, in raf' — fronted to say the subject NEVER LEAVES THE MIND. This is the fifth reason: some names stand first because for the speaker they are always already present, and the word order is a confession of that.",
      "Lafza-i celâl mübtedâ, merfû — öznenin HATIRDAN HİÇ ÇIKMADIĞINI göstermek için öne alınmıştır. Bu beşinci sebeptir: bâzı isimler hep önce gelir, çünkü mütekellim için zâten hep hazırdırlar; söz dizimi bunun ikrârıdır."),
  tok("إِلَهُنَا","ilah","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ ظَاهِرَةٍ عَلَى الْهَاءِ، وَهُوَ مُضَافٌ وَ«نَا» مُضَافٌ إِلَيْهِ.",
      "The khabar, in raf' by a damma WRITTEN PLAINLY on the ha — the sign sits at the seam, on the letter the pronoun hangs from, and the pronoun's own alif is not the word's ending. The app used to read this word as a maqsur for exactly that confusion. A mudaf, with «na» its mudaf ilayh.",
      "Merfû haber; damme, hâ üzerinde AÇIKÇA yazılıdır — alâmet eklem yerindedir, zamirin asıldığı harftedir; zamirin kendi elifi kelimenin sonu değildir. Uygulama tam bu karışıklıkla bu kelimeyi maksûr okuyordu. Muzâftır, «نَا» muzâfun ileyhtir.",
      segments=[seg("إِلَهُ","ilah","noun"), seg("نَا","pron-1p","pron")],
      punct="."),
  tok("وَمُحَمَّدٌ","muhammad","propn",["atf-nasaq","taqdim-al-musnad-ilayh"],
      "الْوَاوُ عَاطِفَةٌ، وَ«مُحَمَّدٌ» مُبْتَدَأٌ مَرْفُوعٌ — جُمْلَةٌ مَعْطُوفَةٌ عَلَى جُمْلَةٍ.",
      "The waw joins clause to clause, and «Muhammad» is a second mubtada, in raf' — the same fronting for the same reason, and the parallel structure is itself part of the sentence's confession: both names stand first because both are always present.",
      "Vâv cümleyi cümleye atfeder; «مُحَمَّدٌ» ikinci mübtedâdır, merfûdur — aynı sebeple aynı takdîm. Paralel yapı da cümlenin ikrârındandır: iki isim de öne gelir, çünkü ikisi de hep hazırdır.",
      segments=[seg("وَ","wa","conj"), seg("مُحَمَّدٌ","muhammad","propn")]),
  tok("نَبِيُّنَا","nabi","noun",["mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ ظَاهِرَةٍ عَلَى الْيَاءِ الْمُشَدَّدَةِ، مُضَافٌ وَ«نَا» مُضَافٌ إِلَيْهِ.",
      "The khabar, in raf' by a damma on the doubled ya — again at the seam. نَبِيّ ends in a REAL doubled ya (ن ب ي with the nisba-like shadda), so the vowel is written, not estimated: a doubled ya is no manqus.",
      "Merfû haber; damme, şeddeli yâ üzerindedir — yine eklem yerinde. «نَبِيّ» GERÇEK bir şeddeli yâ ile biter (ن ب ي); öyleyse hareke yazılır, takdîr edilmez: şeddeli yâ, menkūs değildir.",
      segments=[seg("نَبِيُّ","nabi","noun"), seg("نَا","pron-1p","pron")],
      punct="."),
  tok("حَبِيبِي","habib","noun",["taqdim-al-musnad-ilayh","mubtada-khabar","ya-al-mutakallim"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا كَسْرَةُ الْمُنَاسَبَةِ، مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ — قُدِّمَ لِلتَّلَذُّذِ بِذِكْرِهِ.",
      "The mubtada, its raf' ESTIMATED behind the kasra the speaker's ya demands, annexed to that ya — and fronted for the PLEASURE OF SAYING IT. The sixth reason, and the most human: the speaker puts the word first because holding it back is a cost. No rule of syntax knows anything about that; only this science asks the question that finds it.",
      "Mübtedâ; ref'i, mütekellim yâsının istediği münâsebet kesresi ardında TAKDÎRÎdir; o yâya muzâftır — ve ANMANIN LEZZETİ için öne alınmıştır. Altıncı sebep, ve en insânîsi: mütekellim kelimeyi öne koyar, çünkü geciktirmek ona pahalıdır. Hiçbir nahiv kāidesi bundan haberdar değildir; bunu bulan soruyu yalnız bu ilim sorar.",
      segments=[seg("حَبِيب","habib","noun"), seg("ي","pron-1s","pron")]),
  tok("يَجِيءُ","jaa","verb",["fa-khabar-mubtada","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَفَاعِلُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A mudari' in raf' with a concealed fa'il — the clause standing as the khabar. The verb held to the end is the same delay as the bayt's, in miniature.",
      "Merfû muzâri; fâili müstetirdir — cümle, haber olarak mahallen merfûdur. Sona saklanan fiil, beytteki geciktirmenin küçüğüdür.",
      punct=".")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "Zayd — he, and no other — is the one standing.",
 "tr": "Ayakta duran, Zeyd'dir — o, başkası değil."},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["mubtada-khabar","damir-fasl"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "The mubtada, in raf'.",
      "Merfû mübtedâ."),
  tok("هُوَ","huwa","pron",["damir-fasl","qasr"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — يُؤْذِنُ بِأَنَّ مَا بَعْدَهُ خَبَرٌ لَا نَعْتٌ، وَيُفِيدُ قَصْرَ الْمُسْنَدِ عَلَى الْمُسْنَدِ إِلَيْهِ.",
      "The PRONOUN OF SEPARATION — and it has NO position in i'rab: not mubtada, not khabar, a word standing wholly outside the sentence's case structure. It does two things at once: announces that الْقَائِمُ is the KHABAR and not an adjective (زَيْدٌ الْقَائِمُ would be «the standing Zayd», still waiting for its news), and CONFINES the standing to Zayd — he and no one else. The analyzer now offers exactly this shortlist for a pronoun in this seat.",
      "ZAMÎR-İ FASL — ve İ'RÂBDAN MAHALLİ YOKTUR: ne mübtedâdır ne haber; cümlenin hâl yapısının büsbütün dışında duran bir kelimedir. Bir anda iki iş görür: «الْقَائِمُ»un sıfat değil HABER olduğunu bildirir («زَيْدٌ الْقَائِمُ», «ayaktaki Zeyd» demek olur ve haberini beklerdi) ve ayakta durmayı Zeyd'e KASREDER — o, başkası değil. Analizör, bu mevkideki zamir için artık tam bu kısa listeyi sunar."),
  tok("الْقَائِمُ","qaim","noun",["damir-fasl","mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنَ الْأَجْوَفِ: قَاوِمٌ صَارَ قَائِمًا، وَالْهَمْزَةُ إِعْلَالُ الْوَاوِ.",
      "The khabar, in raf' — the ism fa'il of a hollow root: قَاوِم became قَائِم, and the hamza IS the i'lal of the waw. The app's root finder used to keep that seat as a radical and answer «ق ئ م»; the seat is the scar the turned letter left, and the root is ق و م.",
      "Merfû haber — ecvef kökün ism-i fâili: «قَاوِم», «قَائِم» oldu ve hemze, vâvın i'lâlidir. Uygulamanın kök bulucusu o mesnedi aslî harf sayıp «ق ئ م» diyordu; mesned, dönüşen harfin izidir ve kök ق و م'dur.",
      punct=".")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "It was not I who said this. — I — and no other — laboured in your need.",
 "tr": "Bunu söyleyen ben değilim. — Senin işinde çalışan benim — başkası değil."},
 "tokens": [
  tok("مَا","ma-nafiya","part",["taqdim-al-musnad-ilayh","ma-la-mushabbaha"],
      "حَرْفُ نَفْيٍ لَا عَمَلَ لَهُ هُنَا.",
      "A letter of negation, governing nothing here — what is special in this sentence is not the ma but what the WORD ORDER does to it.",
      "Nefiy harfi; burada amel etmez — bu cümlede husûsî olan mâ değil, SÖZ DİZİMİnin ona yaptığıdır."),
  tok("أَنَا","ana","pron",["taqdim-al-musnad-ilayh","mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَتَقْدِيمُهُ بَعْدَ النَّفْيِ يُفِيدُ التَّخْصِيصَ عِنْدَ عَبْدِ الْقَاهِرِ.",
      "A detached pronoun, mabni, in the position of raf' as the mubtada — and its FRONTING DIRECTLY AFTER THE NEGATION is ʿAbd al-Qāhir's rule: the denial confines the act to the subject. «It was not I who said it» does not deny the saying — it CONCEDES the saying and removes only the speaker. That is why adding «and no one else» here would contradict the frame itself, and the books rule it invalid.",
      "Munfasıl zamir; mebnîdir, mübtedâ olarak mahallen merfûdur — ve NEFİYDEN HEMEN SONRA ÖNE ALINMASI, Abdülkāhir'in kāidesidir: nefiy, fiili özneye tahsîs eder. «Bunu söyleyen ben değilim», söylemeyi inkâr etmez — söylemeyi KABUL eder ve yalnız söyleyeni çıkarır. Buraya «başkası da değil» eklemenin kalıbın kendisiyle çelişmesinin ve kitapların bunu geçersiz saymasının sebebi budur."),
  tok("قُلْتُ","qala","verb",["fail","fa-khabar-mubtada"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A mazi, mabni on the sukun for the doer's ta, and the ta is the fa'il — the clause standing in raf' as the khabar of the pronoun.",
      "Mâzî; fâil tâsına bitiştiği için sükûn üzere mebnîdir ve tâ fâildir — cümle, zamirin haberi olarak mahallen merfûdur.",
      segments=[seg("قُلْ","qala","verb"), seg("تُ","pron-1s","pron")]),
  tok("هَذَا","hadha","pron",["maful-bihi","asma-al-ishara"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
      "A demonstrative, mabni, in the position of nasb as the object.",
      "İşaret ismi; mebnîdir, mef'ûlün bih olarak mahallen mansubdur.",
      punct="."),
  tok("أَنَا","ana","pron",["taqdim-al-musnad-ilayh","mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — تَقَدَّمَ بِلَا نَفْيٍ قَبْلَهُ، فَالتَّخْصِيصُ هُنَا لِرَدِّ الْمُخَاطَبِ.",
      "The same pronoun, fronted — but NO negation stands before it, and that changes everything. Here the takhsis answers a hearer who credited the wrong man, or thought others shared the work: «I laboured in your need» — I, whatever you supposed.",
      "Aynı zamir, yine önde — fakat öncesinde nefiy YOKTUR ve bu her şeyi değiştirir. Buradaki tahsîs, işi yanlış adama mâl eden yahut başkalarının da ortak olduğunu sanan muhâtaba cevaptır: «senin işinde çalışan benim» — sen kime yorarsan yor."),
  tok("سَعَيْتُ","saa-verb","verb",["fail","fa-khabar-mubtada","naqis-verbs"],
      "فِعْلٌ مَاضٍ نَاقِصٌ يَائِيٌّ مَبْنِيٌّ عَلَى السُّكُونِ، وَالتَّاءُ فَاعِلٌ — وَالْجُمْلَةُ خَبَرٌ.",
      "A defective mazi (س ع ي — the ya comes back before the doer's ta: سَعَى but سَعَيْتُ), mabni, its ta the fa'il — the clause the khabar.",
      "Nâkıs mâzî (س ع ي — yâ, fâil tâsından önce geri gelir: «سَعَى» fakat «سَعَيْتُ»); mebnîdir, tâ fâildir — cümle haberdir.",
      segments=[seg("سَعَيْ","saa-verb","verb"), seg("تُ","pron-1s","pron")]),
  tok("فِي","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«سَعَيْتُ»، لَغْوٌ.",
      "A jarr letter; the phrase attaches to «laboured» — laghw, the governor written.",
      "Cer harfi; câr-mecrûr «سَعَيْتُ»ya taalluk eder — lağvdır, âmili yazılıdır."),
  tok("حَاجَتِكَ","haja","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» بِكَسْرَةٍ ظَاهِرَةٍ عَلَى التَّاءِ، مُضَافٌ وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "Majrur by «fi», the kasra written plainly on the ta — at the seam again, before the pronoun — a mudaf with the kaf annexed.",
      "«فِي» ile mecrûr; kesre, tâ üzerinde açıkça yazılıdır — yine eklem yerinde, zamirden önce — muzâftır ve kâf muzâfun ileyhtir.",
      segments=[seg("حَاجَتِ","haja","noun"), seg("كَ","pron-2ms","pron")]),
  tok("لَا","la-atifa","conj",["atf-nasaq","taqdim-al-musnad-ilayh"],
      "حَرْفُ عَطْفٍ.",
      "The joining la — and its very legitimacy here is the lesson: after the affirmative frame the takhsis MAY be confirmed, where after مَا أَنَا it could not be.",
      "Âtıfa lâ — ve tam buradaki meşrûiyeti dersin kendisidir: müsbet kalıptan sonra tahsîs te'kîd EDİLEBİLİR; «مَا أَنَا»dan sonra edilemezdi."),
  tok("غَيْرِي","ghayr","noun",["atf-nasaq","ya-al-mutakallim"],
      "مَعْطُوفٌ مَجْرُورٌ لَفْظًا عَلَى الْمَعْنَى — مُضَافٌ إِلَى يَاءِ الْمُتَكَلِّمِ.",
      "«Other than I» — annexed to the speaker's ya. The pair closes the chapter on the mirror it opened: the same three words that were a contradiction after the negation are its lawful confirmation here, and the only thing that moved was the word order.",
      "«Benden başkası» — mütekellim yâsına muzâftır. Çift, bâbı açıldığı aynayla kapatır: nefiyden sonra tenâkuz olan üç kelime, burada tahsîsin meşrû te'kîdidir — ve kımıldayan tek şey söz dizimidir.",
      punct=".")],
 "jumal": [
  J("مَا أَنَا قُلْتُ هَذَا",
    "جُمْلَةٌ اسْمِيَّةٌ مَنْفِيَّةٌ، وَتَقْدِيمُ الْمُسْنَدِ إِلَيْهِ بَعْدَ النَّفْيِ لِلتَّخْصِيصِ.",
    "A negated nominal sentence — and the subject's fronting straight after the negation is what makes it a takhsis: the act is conceded, only the doer is removed.",
    "Menfî bir isim cümlesi — müsnedün ileyhin nefiyden hemen sonra takdîmi onu tahsîs yapar: fiil kabul edilir, yalnız fâil çıkarılır."),
  J("قُلْتُ هَذَا",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
    "A verbal clause in the position of raf' as the khabar of the pronoun.",
    "Zamirin haberi olarak mahallen merfû fiil cümlesi.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "hara":       g("حَارَ", "ح ي ر", "verb", "to be bewildered, at a loss", "hayrete düşmek, şaşırmak", 4, form="I"),
 "bariyya":    g("بَرِيَّة", "ب ر أ", "noun", "the created, mankind", "yaratılmışlar, halk", 4),
 "hayawan":    g("حَيَوَان", "ح ي ي", "noun", "a living thing; animal", "canlı; hayvan", 2),
 "mustahdath": g("مُسْتَحْدَث", "ح د ث", "noun", "brought newly into being (ism maf'ul of Form X)", "yeniden var edilmiş (Form X ism-i mef'ûlü)", 5),
 "sad-name":   g("سَعْد", "س ع د", "propn", "Sa'd (a man's name; means good fortune)", "Sa'd (bir erkek adı; uğur, saadet demektir)", 2),
 "saffah":     g("سَفَّاح", "س ف ح", "noun", "shedder of blood (an intensive on فَعَّال)", "kan dökücü (فَعَّال vezninde mübâlağa)", 5),
 "saa-verb":   g("سَعَى", "س ع ي", "verb", "to strive, to labour for", "çalışmak, koşuşturmak", 2, form="I"),
 "ta-tanith":  g("تْ (تَاءُ التَّأْنِيثِ)", None, "part", "the ta of femininity (on a verb)", "te'nîs tâsı (fiilde)", 2),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "muhammad":   g("مُحَمَّد", None, "propn", "Muhammad", "Muhammed", 0),
 "nabi":       g("نَبِيّ", "ن ب أ", "noun", "prophet", "peygamber, nebî", 1, plural="أَنْبِيَاء"),
 "qaim":       g("قَائِم", "ق و م", "noun", "standing (ism fa'il)", "ayakta duran, kāim (ism-i fâil)", 2),
 "ana":        g("أَنَا", None, "pron", "I (detached)", "ben (munfasıl)", 1),
 "haja":       g("حَاجَة", "ح و ج", "noun", "need, affair", "ihtiyaç, iş", 2, plural="حَاجَات"),
 "jamad":      g("جَمَاد", "ج م د", "noun", "lifeless matter, the inanimate", "cansız madde, cemâdât", 3),
}

def build_morph():
    """Two new paradigms, both forced by the chapter's own tokens.

    سَعَى — naqis ya'i of bab فَتَحَ (سَعَى يَسْعَى): the rama-type mazi (alif
    third person, ya before the doer's ta) with the fatha-type mudari. Without
    it سَعَيْتُ was corpus-unknown and the analyzer read أَنَا سَعَيْتُ as an idafa.

    حَارَ — ajwaf ya'i of bab سَمِعَ (حَيِرَ ← حَارَ يَحَارُ, like خَافَ يَخَافُ):
    long stem حَار before vowels, short حِر before sukun-initial endings (the
    kasra remembering the ya), mudari يَحَارُ / يَحَرْنَ. Passive and maf'ul are
    OMITTED — rare for this verb and not worth a guess.
    """
    out = {}
    out["saa-verb"] = _sg.naqis1("fataha", "نَاقِصٌ يَائِيٌّ", "y", "سَعَ", "سْعَ", "a", "اِسْعَ",
                                 "سَعْي", "سَاعٍ", "مَسْعِيّ", "سُعِيَ", "يُسْعَى")
    out["hara"] = _sg.hollow1("samia", "أَجْوَفُ يَائِيٌّ", "حَار", "حِر", "حَار", "حَر",
                              "حَار", "حَر", "حَيْرَة", "حَائِر",
                              note="أَجْوَفُ مِنْ بَابِ سَمِعَ كَخَافَ يَخَافُ: حَارَ يَحَارُ، وَالْقَصِيرُ بِالْكَسْرِ — حِرْتُ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/11.json").write_text(
    json.dumps({"chapter": 11, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 11 for c in man["chapters"]):
    man["chapters"].append({"n": 11, "title": TITLE11})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.11.0"
ADD_EN = (" Chapter 11 continues from the same file (lines ~935-990), which carries every one of its "
          "examples vowelled: Abu al-'Ala's bayt (وَالَّذِي حَارَتِ الْبَرِيَّةُ فِيهِ حَيَوَانٌ مُسْتَحْدَثٌ مِنْ جَمَادٍ), "
          "سَعْدٌ فِي دَارِكَ with its grief-mirror, اللَّهُ إِلَهُنَا وَمُحَمَّدٌ نَبِيُّنَا, حَبِيبِي يَجِيءُ, "
          "زَيْدٌ هُوَ الْقَائِمُ, and Abd al-Qahir's مَا أَنَا قُلْتُ هَذَا with أَنَا سَعَيْتُ فِي حَاجَتِكَ لَا غَيْرِي.")
ADD_TR = (" On birinci bâb aynı dosyadan (satır ~935-990) devam eder; o satırlar bâbın bütün misallerini "
          "harekeli olarak taşır: Ebü'l-Alâ'nın beyti (وَالَّذِي حَارَتِ الْبَرِيَّةُ فِيهِ حَيَوَانٌ مُسْتَحْدَثٌ مِنْ جَمَادٍ), "
          "hüzün-aynasıyla سَعْدٌ فِي دَارِكَ, اللَّهُ إِلَهُنَا وَمُحَمَّدٌ نَبِيُّنَا, حَبِيبِي يَجِيءُ, "
          "زَيْدٌ هُوَ الْقَائِمُ ve Abdülkāhir'in مَا أَنَا قُلْتُ هَذَا'sı ile أَنَا سَعَيْتُ فِي حَاجَتِكَ لَا غَيْرِي.")
if "935-990" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch11:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
