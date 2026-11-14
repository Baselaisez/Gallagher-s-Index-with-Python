# -*- coding: utf-8 -*-
"""Author chapter 7 of talkhis-al-miftah — أَحْوَالُ الْمُسْنَدِ إِلَيْهِ: الْحَذْفُ وَالذِّكْر.

Six chapters have been about the SENTENCE — what a report claims, who it is
built for, whether the ascription is literal. From here the Talkhis turns to
the PARTS, and it begins where the parts begin: the musnad ilayh, the thing
spoken about. Its first two states are the barest possible pair — say it, or
leave it out — and the whole art is in the REASON.

The commentary lists ten motives for dropping it and nine for keeping it, and
the pairs that matter are the ones that share a device and differ in intent:

  • مُقَرِّرٌ لِلشَّرَائِعِ … — the name left out to keep the TONGUE FROM IT, out of
    reverence: everyone knows who confirms the Law.
  • مُوَسْوِسٌ سَاعٍ فِي الْفَسَادِ … — the same omission, to keep the tongue from a
    name one does not care to say.

Same syntax, opposite motive, four lines apart. And on the DHIKR side the same
mirror runs again: الْحَبِيبُ حَاضِرٌ names him for the pleasure of naming him,
السَّارِقُ اللَّئِيمُ حَاضِرٌ names him to shame him.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~665-712, which gives all
of this chapter's examples in vowelled Arabic — the poet's bayt, the moon and
the crescent, the two four-word portraits with their fa of consequence, the
Baqara verse and the Taha verse, and the three حَاضِرٌ sentences. Where two of
the source's phrases stand side by side they are juxtaposed with a full stop
between them, as in chapters 5 and 6; nothing is composed.

Grammar this chapter is chosen to teach:
  • الْمُبْتَدَأُ الْمَحْذُوف — five times, and each time the taqdir is DIFFERENT and
    is named. عَلِيلٌ is the khabar of an unwritten أَنَا; الْهِلَالُ of an unwritten
    هَذَا; مُقَرِّرٌ of an unwritten مُحَمَّدٌ. A chapter about omission is the right
    place for the nahw of omission.
  • THE PARTICIPLES OF THE DERIVED FORMS, in one line: مُقَرِّرٌ (II), مُوضِحٌ (IV,
    and a mithal — the waw stands because a damma is in front of it), مُسْتَفَادٌ
    (X, hollow), مُوَسْوِسٌ (from a QUADRILITERAL), الْمُفْلِحُونَ (IV, sound plural).
    The root finder could read none of these until this chapter demanded it.
  • عَصَايَ — a maqsur meeting the speaker's ya, which is the one exception note
    103 names: the alif stands and the ya takes a fatha.
  • هُدًى — a maqsur wearing tanwin, majrur by a kasra nothing writes; and the
    phrase it stands in is a MUSTAQARR khabar, which is note 102 in real text.
  • شَرَائِع and دَلَائِل — two صِيَغُ مُنْتَهَى الْجُمُوعِ, barred from tanwin, and both
    wearing the article, which restores their kasra.
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

TITLE7 = {"ar": "أَحْوَالُ الْمُسْنَدِ إِلَيْهِ: الْحَذْفُ وَالذِّكْر",
          "en": "The States of the Subject: Leaving It Out, and Saying It",
          "tr": "Müsnedün İleyhin Hâlleri: Hazf ve Zikr"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "He said to me: how are you? I said: ill — a sleeplessness that never ends, and a long grief.",
 "tr": "Bana «nasılsın» dedi; «hastayım» dedim — bitmeyen bir uykusuzluk ve uzun bir hüzün."},
 "tokens": [
  tok("قَالَ","qala","verb",["fail"],
      "فِعْلٌ مَاضٍ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» يَعُودُ عَلَى الصَّاحِبِ.",
      "A mazi verb, its fa'il concealed as «he» — the friend, who is nowhere named. The line opens by leaving somebody out, which is the chapter's whole subject.",
      "Mâzî fiil; fâili müstetir «هُوَ»dur — hiçbir yerde adı geçmeyen arkadaş. Mısra, birini zikretmeyerek başlıyor; bâbın bütün mevzuu da budur."),
  tok("لِي","li","prep",["huruf-jarr","ya-al-mutakallim","zarf-mustaqarr-wa-laghw"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْيَاءُ يَاءُ الْمُتَكَلِّمِ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِـ«قَالَ»، لَغْوٌ.",
      "The lam is a jarr letter and the ya is the speaker's, in the position of jarr — attaching to «said», so it is LAGHW. Two chapters ago this word was being read as a verb, because لِي is also, letter for letter, the feminine imperative of وَلِيَ.",
      "Lâm cer harfi, yâ mütekellim yâsıdır, mahallen mecrûr — «قَالَ»ya taalluk eder, LAĞVdır. İki bâb önce bu kelime fiil okunuyordu; zira «لِي», harf harf, «وَلِيَ»nin müennes emri de olur.",
      segments=[seg("لِ","li","prep"), seg("ي","pron-1s","pron")]),
  tok("كَيْفَ","kayfa","noun",["mubtada-khabar"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.",
      "An interrogative NOUN, mabni on the fatha, standing in the position of raf' as a FRONTED khabar. It is a noun, not a letter — the question-words that ask about a state or a place are asma, and only هَلْ and the hamza are huruf.",
      "Mebnî istifham İSMİ, fetha üzere; mahallen merfû MUKADDEM haberdir. Harf değil isimdir — hâli yahut yeri soran istifham kelimeleri isimdir; yalnız «هَلْ» ile hemze harftir."),
  tok("أَنْتَ","anta","pron",["mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "A detached pronoun, mabni, in the position of raf' as the DELAYED mubtada — and the whole clause is what was said. The khabar came first because a question word must open its question; word order here is forced, not chosen.",
      "Munfasıl zamir, mahallen merfû MUAHHAR mübtedâ — ve cümlenin tamamı mekūlü'l-kavldir. Haber öne geçti, zira istifham kelimesi sorusunun başında bulunmak zorundadır; buradaki tertîb tercih değil, mecburiyettir."),
  tok("قُلْتُ","qala","verb",["fail","hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ — وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A mazi MABNI ON THE SUKUN because the doer's ta joined it, and the ta is the fa'il — and the hollow verb's waw has DROPPED, because the ta's sukun met it. قَالَ becomes قُلْتُ, and the damma left behind is the only trace of the vanished waw.",
      "Fâil tâsına bitiştiği için SÜKÛN üzere mebnî mâzî; tâ fâildir — ve ecvefin vâvı DÜŞMÜŞTÜR, zira tânın sükûnu onunla buluşmuştur. «قَالَ» «قُلْتُ» olur; geride kalan damme, kaybolan vâvın tek izidir."),
  tok("عَلِيلٌ","alil","noun",["mubtada-khabar","hadhf-wa-taqdir","ahwal-al-musnad-ilayh","sifa-mushabbaha"],
      "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «أَنَا» — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ. وَحُذِفَ الْمُسْنَدُ إِلَيْهِ لِلِاحْتِرَازِ عَنِ الْعَبَثِ، إِذْ حَالُ الْمُخَاطَبِ ظَاهِرَةٌ، وَلِلتَّنْبِيهِ عَلَى أَنَّ الدَّلِيلَ الْعَقْلِيَّ أَقْوَى مِنَ اللَّفْظِيِّ.",
      "The khabar of an OMITTED mubtada, estimated as «I» — a sifa mushabbaha on فَعِيل. And the reason the subject is dropped is the chapter's first motive twice over: saying «I» would be idle, since the questioner is looking straight at him; and dropping it points at the stronger of the two proofs — the one the mind supplies rather than the one the words do. A sick man does not say «I am ill»; he says «ill».",
      "MAHZÛF bir mübtedânın haberi; takdîri «أَنَا»dır — FA'ÎL vezninde sıfat-ı müşebbehe. Müsnedün ileyhin hazfi, bâbın ilk iki sebebini birden taşır: «ben» demek ABESten kaçınılması gereken bir fazlalık olurdu, zira soran adam ona bakmaktadır; ve hazf, iki delîlin daha kuvvetlisine — lafzın değil, aklın verdiğine — dikkat çeker. Hasta adam «ben hastayım» demez, «hastayım» der.",
      punct="•"),
  tok("سَهَرٌ","sahar","noun",["mubtada-khabar","hadhf-wa-taqdir"],
      "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، أَيْ: عِلَّتِي سَهَرٌ — وَيَجُوزُ أَنْ يَكُونَ مُبْتَدَأً خَبَرُهُ مَحْذُوفٌ، أَيْ: بِي سَهَرٌ. وَالسَّطْحُ لَا يُرَجِّحُ.",
      "The khabar of an omitted mubtada — «my ailment is a sleeplessness» — OR a mubtada whose khabar is omitted — «in me is a sleeplessness». The surface does not settle which, and saying so is the honest answer: what is certain is that a half of this sentence is unwritten, and the reader supplies it from the line before.",
      "Mahzûf bir mübtedânın haberi — «hastalığım bir uykusuzluktur» — YAHUT haberi mahzûf bir mübtedâ — «bende bir uykusuzluk var». Yüzey ikisini ayırmaz; bunu söylemek dürüst cevaptır. Kesin olan şudur: bu cümlenin bir yarısı yazılmamıştır ve okuyucu onu bir önceki mısradan tamamlar."),
  tok("دَائِمٌ","daim","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«سَهَرٌ» مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «دَامَ» الْأَجْوَفِ: أَصْلُهُ «دَاوِمٌ»، قُلِبَتِ الْعَيْنُ هَمْزَةً.",
      "A na't of «sleeplessness», in raf' — the ism fa'il of the HOLLOW verb دَامَ: its origin is دَاوِمٌ, and the middle radical turned into a HAMZA after the alif of فَاعِل. The same step that gave صَائِمٌ two chapters ago, on a different root.",
      "«سَهَرٌ»un merfû na'tı — AJVEF «دَامَ»nin ism-i fâili: aslı «دَاوِمٌ»dur, ayn harfi fâil elifinden sonra HEMZEYE kalbolmuştur. İki bâb önce «صَائِمٌ»i veren adımın aynısı, başka bir kök üzerinde."),
  tok("وَحُزْنٌ","huzn","noun",["atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«حُزْنٌ» مَعْطُوفٌ عَلَى «سَهَرٌ» مَرْفُوعٌ.",
      "A joining waw, and «grief» is joined to «sleeplessness», in raf'. Two indefinites in a row, each with its own description, and no verb anywhere in the hemistich — the whole second half of the line is nouns.",
      "Atıf vâvı; «حُزْنٌ», «سَهَرٌ»a ma'tûf ve merfûdur. Peş peşe iki nekre, her biri kendi sıfatıyla; mısraın ikinci yarısında hiç fiil yok — tamamı isimdir.",
      segments=[seg("وَ","wa","conj"), seg("حُزْنٌ","huzn","noun")]),
  tok("طَوِيلٌ","tawil-long","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«حُزْنٌ» مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ، كَـ«عَلِيلٍ» فِي الشَّطْرِ الْأَوَّلِ.",
      "A na't of «grief», in raf' — a sifa mushabbaha on فَعِيل, the same scale as «ill» in the first hemistich. The bayt is built out of one pattern used three times, which is what makes it stick.",
      "«حُزْنٌ»un merfû na'tı — FA'ÎL vezninde sıfat-ı müşebbehe; ilk mısradaki «عَلِيلٍ» ile aynı vezin. Beyit, üç defa kullanılan tek bir kalıptan kurulmuştur; akılda kalmasının sebebi budur.",
      punct="."),
 ],
 "jumal": [J("كَيْفَ أَنْتَ",
   "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
   "A nominal sentence in the position of nasb as what was said.",
   "Mekūlü'l-kavl olarak mahallen mansub isim cümlesi."),
  J("عَلِيلٌ",
   "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ، وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
   "The khabar of an omitted mubtada; the clause is in the position of nasb as what was said.",
   "Mahzûf mübtedânın haberi; cümle, mekūlü'l-kavl olarak mahallen mansubdur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "Its light is drawn from the sun. — It is the crescent, by God!",
 "tr": "Onun ışığı güneşten alınmıştır. — Hilâldir, vallahi!"},
 "tokens": [
  tok("نُورُهُ","nur","noun",["mubtada-khabar","idafa-definiteness","ahwal-al-musnad-ilayh"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْهَاءُ تَعُودُ عَلَى مَحْذُوفٍ تَقْدِيرُهُ «الْقَمَرُ».",
      "The mubtada in raf', a mudaf with the ha annexed to it — and that ha points back at a word that is NOT ON THE PAGE: «the moon». A pronoun without a written antecedent is the sharpest form of this chapter's device, because the hearer must supply the subject before he can even resolve the pronoun. The motive the book gives is to TEST HIS ATTENTION.",
      "Merfû mübtedâ, muzâf; hâ muzâfun ileyhtir — ve o hâ, SAYFADA OLMAYAN bir kelimeye râcidir: «الْقَمَرُ». Yazılı mercii bulunmayan zamir, bu bâbın en keskin şeklidir; zira muhâtab, zamiri çözebilmek için önce özneyi kendisi koymak zorundadır. Kitabın verdiği sebep de şudur: DİKKATİNİ ÖLÇMEK."),
  tok("مُسْتَفَادٌ","mustafad","noun",["mubtada-khabar","ism-maful","form-x-verbs","hollow-verbs"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنَ «اسْتَفَادَ» عَلَى مُسْتَفْعَلٍ، وَهُوَ أَجْوَفُ: أَصْلُهُ «مُسْتَفْوَدٌ»، نُقِلَتْ حَرَكَةُ الْوَاوِ إِلَى الْفَاءِ ثُمَّ قُلِبَتْ أَلِفًا.",
      "The khabar in raf' — the ism maf'ul of Form X اسْتَفَادَ on مُسْتَفْعَل, and the verb is HOLLOW: its origin is مُسْتَفْوَدٌ, the waw's vowel moved back onto the letter before it and the waw itself became an alif. The app's root finder could not read this word at all until this chapter; the participles of the derived forms had no row in its table.",
      "Merfû haber — ONUNCU bâbdan «اسْتَفَادَ»nin MÜSTEF'AL vezninde ism-i mef'ûlü; fiil AJVEFtir: aslı «مُسْتَفْوَدٌ»dur, vâvın harekesi önceki harfe nakledilmiş, vâv da elife kalbolmuştur. Uygulamanın kök bulucusu bu kelimeyi bu bâba kadar hiç okuyamıyordu; mezîd bâbların vasıfları tablosunda hiç satır bulmuyordu."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ — وَنُونُهُ سَاكِنَةٌ فِي الْأَصْلِ، فُتِحَتْ لِالْتِقَاءِ السَّاكِنَيْنِ مَعَ لَامِ التَّعْرِيفِ.",
      "A jarr letter of ORIGIN — and its nun is quiescent by rule, opened with a FATHA here only because the article's silent lam follows it. Not a kasra, as the repair usually is: مِنْ takes a fatha, and that irregularity is itself a stored fact rather than a derived one.",
      "İbtidâ-i gāye için cer harfi — nûnu aslen sâkindir; buradaki FETHA yalnızca ardından gelen lâm-ı ta'rîf sebebiyledir. Ve tamîrin âdeti olan kesra değil: «مِنْ» fetha alır; bu istisnâ türetilen değil, bilinen bir bilgidir."),
  tok("الشَّمْسِ","shams","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«مِنْ» — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«مُسْتَفَادٌ»، فَهُوَ لَغْوٌ.",
      "Majrur by «min» — and the phrase attaches to «drawn», an ism maf'ul, so it is LAGHW. A participle governing a jarr phrase is exactly the case note 102 exists for: the governor need not be a verb, only something carrying a verb's meaning.",
      "«مِنْ» ile mecrûr — ve câr-mecrûr, bir ism-i mef'ûl olan «مُسْتَفَادٌ»a taalluk eder; öyleyse LAĞVdır. Câr-mecrûru bir vasfın amel etmesi, 102 numaralı notun varlık sebebidir: âmilin fiil olması gerekmez, fiilin mânâsını taşıması yeter.",
      punct="."),
  tok("الْهِلَالُ","hilal","noun",["mubtada-khabar","hadhf-wa-taqdir","ahwal-al-musnad-ilayh"],
      "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «هَذَا» — وَحُذِفَ لِضِيقِ الْمَقَامِ.",
      "The khabar of an omitted mubtada, estimated as «this» — and it was dropped because THERE WAS NO TIME. A man who catches sight of the new moon has a second in which to say so; «this is the crescent» is one word longer than the moment allows. The chapter's tenth motive is the plainest of them and the least literary.",
      "Takdîri «هَذَا» olan mahzûf bir mübtedânın haberi — ve VAKİT DAR olduğu için hazfedilmiştir. Hilâli gören adamın söylemeye bir saniyesi vardır; «bu hilâldir» demek, ânın müsaade ettiğinden bir kelime uzundur. Bâbın onuncu sebebi, en sade ve en az edebî olanıdır."),
  tok("وَاللهِ","allah","propn",["huruf-jarr"],
      "الْوَاوُ وَاوُ الْقَسَمِ حَرْفُ جَرٍّ، وَلَفْظُ الْجَلَالَةِ مَجْرُورٌ بِهَا — وَجَوَابُ الْقَسَمِ مَحْذُوفٌ دَلَّ عَلَيْهِ مَا قَبْلَهُ.",
      "The waw is the waw of an OATH — a jarr letter — and the name of God is majrur by it; the oath's answer is omitted, and what came before it stands in for that too. Two omissions in three words, and the sentence still says everything it means.",
      "Vâv, KASEM vâvıdır — cer harfidir — ve lafza-i celâl onunla mecrûrdur; kasemin cevabı mahzûftur, öncesi ona delâlet eder. Üç kelimede iki hazf; ve cümle yine kastettiği her şeyi söylüyor.",
      segments=[seg("وَ","wa","prep"), seg("اللهِ","allah","propn")],
      punct="."),
 ],
 "jumal": [J("نُورُهُ مُسْتَفَادٌ مِنَ الشَّمْسِ",
   "جُمْلَةٌ اسْمِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, with no position in i'rab.",
   "İsim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "One who confirms the Laws, who makes the proofs plain — so following him is obligatory. — A whisperer, hurrying to corruption — so opposing him is obligatory.",
 "tr": "Şerîatleri takrîr eden, delîlleri açıklayan — öyleyse ona ittibâ vâcibdir. — Vesvese veren, fesada koşan — öyleyse ona muhâlefet vâcibdir."},
 "tokens": [
  tok("مُقَرِّرٌ","muqarrir","noun",["mubtada-khabar","hadhf-wa-taqdir","ahwal-al-musnad-ilayh","ism-fail","form-ii-verbs"],
      "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «مُحَمَّدٌ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ» — اسْمُ فَاعِلٍ مِنْ «قَرَّرَ» عَلَى مُفَعِّلٍ. وَحُذِفَ الْمُسْنَدُ إِلَيْهِ صِيَانَةً لِلِّسَانِ عَنْ ذِكْرِهِ إِلَّا عَلَى وَجْهِهِ.",
      "The khabar of an omitted mubtada, estimated as «Muhammad, God bless him and grant him peace» — an ism fa'il of Form II. And the motive is REVERENCE: the tongue is kept from the name, not because the hearer would not know it but because he certainly will. The omission is a kind of respect, and it works only where the description could belong to nobody else.",
      "Takdîri «مُحَمَّدٌ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ» olan mahzûf bir mübtedânın haberi — «قَرَّرَ»nin MUFA'İL vezninde ism-i fâili. Sebep TA'ZÎMdir: dil, ismi anmaktan korunur; muhâtab bilmeyeceği için değil, mutlaka bileceği için. Hazf bir nevi hürmettir ve ancak vasıf başkasına âit olamayacak yerde işler."),
  tok("لِلشَّرَائِعِ","sharia","noun",["huruf-jarr","mamnu-min-sarf","zarf-mustaqarr-wa-laghw"],
      "اللَّامُ حَرْفُ جَرٍّ وَ«الشَّرَائِعِ» مَجْرُورٌ بِالْكَسْرَةِ، مُتَعَلِّقٌ بِـ«مُقَرِّرٌ»، لَغْوٌ — وَهُوَ عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ فَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ، وَإِنَّمَا جُرَّ بِالْكَسْرَةِ لِدُخُولِ «أَلْ» عَلَيْهِ.",
      "The lam is a jarr letter and «the Laws» is majrur BY A KASRA, attaching to «confirms», laghw — and the word stands on صِيغَةُ مُنْتَهَى الْجُمُوعِ, so it is barred from tanwin and would take a FATHA in jarr. It takes the kasra here only because the article has entered upon it: the article restores what the ban took away, and that is the rule most often forgotten.",
      "Lâm cer harfi, «الشَّرَائِعِ» KESRA ile mecrûr; «مُقَرِّرٌ»a taalluk eder, lağvdır — ve kelime SIYGA-İ MÜNTEHE'L-CUMÛ' üzeredir, gayr-i munsariftir, cerde FETHA alması gerekirdi. Buradaki kesranın tek sebebi «أَلْ»in dâhil olmasıdır: harf-i ta'rîf, men'in aldığını geri verir; en çok unutulan kāide de budur.",
      segments=[seg("لِ","li","prep"), seg("الشَّرَائِعِ","sharia","noun")]),
  tok("مُوضِحٌ","mudih","noun",["mubtada-khabar","ism-fail","form-iv-verbs","mithal-verbs"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «أَوْضَحَ» عَلَى مُفْعِلٍ، وَهُوَ مِثَالٌ وَاوِيٌّ: وَقَعَتِ الْوَاوُ سَاكِنَةً بَعْدَ ضَمَّةٍ فَصَارَتْ حَرْفَ مَدٍّ وَلَمْ تُكْتَبْ عَلَيْهَا سُكُونٌ.",
      "A SECOND khabar in raf' — the ism fa'il of Form IV أَوْضَحَ, and the root's first letter is a WAW. A quiescent waw standing after a damma is already a letter of prolongation, so no sukun is written on it: مُوضِح, not مُوْضِح. That is the same rule Mukhtasar al-Manar's أَنْ يُوجِبَ forced into the conjugator, met here in a participle.",
      "İkinci merfû haber — «أَوْضَحَ»nin MUF'İL vezninde ism-i fâili; kök MİSÂL vâvîdir. Dammeden sonra sâkin gelen vâv zaten bir med harfidir, üzerine sükûn yazılmaz: «مُوضِح», «مُوْضِح» değil. Muhtasaru'l-Menâr'ın «أَنْ يُوجِبَ»inin çekim motoruna kabul ettirdiği kāidenin aynısı, burada bir vasıfta karşımıza çıkıyor."),
  tok("لِلدَّلَائِلِ","dalil","noun",["huruf-jarr","mamnu-min-sarf","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِاللَّامِ بِالْكَسْرَةِ لِدُخُولِ «أَلْ»، مُتَعَلِّقٌ بِـ«مُوضِحٌ» — وَهُوَ أَيْضًا صِيغَةُ مُنْتَهَى الْجُمُوعِ.",
      "Majrur by the lam with a kasra, again because the article is on it, attaching to «makes plain» — and it too is a صِيغَةُ مُنْتَهَى الْجُمُوعِ. Two of them in one line, both restored to their kasra by the same article: the pair proves the rule better than either would alone.",
      "Lâm ile ve yine «أَلْ» sebebiyle kesra alarak mecrûr; «مُوضِحٌ»a taalluk eder — ve bu da bir SIYGA-İ MÜNTEHE'L-CUMÛ'dur. Tek satırda iki tane; ikisi de kesrasını aynı harf-i ta'rîfle geri almış: çift, kāideyi tek başına her birinden daha iyi ispat eder.",
      segments=[seg("لِ","li","prep"), seg("الدَّلَائِلِ","dalil","noun")]),
  tok("فَيَجِبُ","wajaba","verb",["mudari-marfu","mithal-verbs"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَ«يَجِبُ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ وَاوِيٌّ حُذِفَتْ وَاوُهُ فِي الْمُضَارِعِ.",
      "The fa is of CONSEQUENCE, and «is obligatory» is a mudari' in raf' — a mithal whose waw is deleted in the present, because it stood between a ya and a kasra. The fa is what turns two descriptions into an argument: because he is this, that follows.",
      "Fâ TEFRÎ' içindir; «يَجِبُ» merfû muzâri fiildir — vâvı, yâ ile kesra arasında kaldığı için muzâride düşen bir misâl. İki vasfı bir DELÎLE çeviren şey fâdır: madem öyledir, öyleyse şu lâzım gelir.",
      segments=[seg("فَ","fa","conj"), seg("يَجِبُ","wajaba","verb")]),
  tok("اتِّبَاعُهُ","ittiba","noun",["fail","masdar","form-viii-verbs","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ «اتَّبَعَ» عَلَى الِافْتِعَالِ، وَفَاؤُهُ تَاءٌ فَأُدْغِمَتْ فِي تَاءِ الِافْتِعَالِ.",
      "The fa'il in raf', a mudaf with the ha annexed — the Form VIII masdar of اتَّبَعَ, whose FIRST RADICAL IS A TA, so it runs together with the ta of the pattern itself. اِتْتِبَاع becomes اِتِّبَاع: the shadda you see is two different tas, one from the root and one from the scale.",
      "Merfû fâil, muzâf; hâ muzâfun ileyhtir — «اتَّبَعَ»nin İFTİÂL vezninde masdarı; kökün FÂSI TÂdır, iftiâlin tâsına idgâm olmuştur. «اِتْتِبَاع» «اِتِّبَاع» olur: gördüğünüz şedde, biri kökten biri vezinden gelen iki ayrı tâdır.",
      punct="."),
  tok("مُوَسْوِسٌ","muwaswis","noun",["mubtada-khabar","hadhf-wa-taqdir","ahwal-al-musnad-ilayh","ism-fail","rubai-babs"],
      "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ تَقْدِيرُهُ «الشَّيْطَانُ» — اسْمُ فَاعِلٍ مِنْ «وَسْوَسَ» الرُّبَاعِيِّ عَلَى مُفَعْلِلٍ. وَحُذِفَ الْمُسْنَدُ إِلَيْهِ صِيَانَةً لِلِّسَانِ عَنْهُ.",
      "The khabar of an omitted mubtada, estimated as «the Devil» — the ism fa'il of the QUADRILITERAL وَسْوَسَ on مُفَعْلِل. And here is the mirror: the previous sentence dropped a name out of reverence, this one drops a name out of distaste. **The same device, the opposite motive**, and the books put them side by side precisely so the device cannot be mistaken for the motive.",
      "Takdîri «الشَّيْطَانُ» olan mahzûf bir mübtedânın haberi — RUBÂÎ «وَسْوَسَ»nin MUFA'LİL vezninde ism-i fâili. Ve işte ayna: bir önceki cümle bir ismi hürmetten dolayı düşürdü, bu cümle bir ismi tiksintiden dolayı düşürüyor. **Aynı vasıta, zıt maksat**; kitaplar ikisini tam da vasıtanın maksatla karıştırılmaması için yan yana koyar."),
  tok("سَاعٍ","sai","noun",["mubtada-khabar","ism-fail","ism-maqsur-manqus","naqis-verbs"],
      "خَبَرٌ ثَانٍ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — اسْمٌ مَنْقُوصٌ نَكِرَةٌ، اسْمُ فَاعِلٍ مِنْ «سَعَى».",
      "A second khabar in raf' by a damma estimated on a DELETED ya — an indefinite manqus, the ism fa'il of سَعَى. This is the fourth manqus the Talkhis has shown in five chapters, and by now the reader has met the class in every state it has.",
      "Merfû ikinci haber; ref' alâmeti, HAZFEDİLMİŞ yâ üzerinde mukadder dammedir — nekre menkūs, «سَعَى»nin ism-i fâili. Telhîs'in beş bâbda gösterdiği dördüncü menkūs; okuyucu artık bu sınıfı bütün hâlleriyle görmüş oldu."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ الْمَجَازِيَّةِ.",
      "A jarr letter, here of a FIGURATIVE containment: corruption is not a place, and hurrying «in» it is the language's ordinary way of naming a direction of effort. Two chapters ago that would have been called a majaz.",
      "Zarfiyyet için cer harfi; buradaki zarfiyyet MECÂZÎdir: fesad bir mekân değildir, onun «içinde» koşmak, dilin bir gayret yönünü adlandırma yoludur. İki bâb önce buna mecâz denirdi."),
  tok("الْفَسَادِ","fasad","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«فِي» — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«سَاعٍ»، لَغْوٌ.",
      "Majrur by «fi» — the phrase attaching to «hurrying», laghw. A manqus governs like any other participle; its deleted ya takes nothing away from what it can do.",
      "«فِي» ile mecrûr — câr-mecrûr «سَاعٍ»ye taalluk eder, lağvdır. Menkūs da her vasıf gibi amel eder; düşen yâsı, yapabileceğinden hiçbir şey eksiltmez."),
  tok("فَتَجِبُ","wajaba","verb",["mudari-marfu","mithal-verbs"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَ«تَجِبُ» مُضَارِعٌ مَرْفُوعٌ — وَالتَّاءُ لِلتَّأْنِيثِ لِأَنَّ فَاعِلَهُ «مُخَالَفَتُهُ».",
      "The fa of consequence again, and the verb takes a TA because its doer is feminine — «opposing him» ends in a ta marbuta. Set it beside فَيَجِبُ five words back: identical sentence, identical fa, and the verb's prefix changes for one reason only, which is the gender of a word that has not arrived yet.",
      "Yine tefrî' fâsı; ve fiil TÂ alır, zira fâili müennestir — «مُخَالَفَتُهُ» tâ-i merbûta ile biter. Beş kelime önceki «فَيَجِبُ» ile yan yana koyun: aynı cümle, aynı fâ; ve fiilin öneki tek bir sebeple değişiyor — henüz gelmemiş bir kelimenin cinsiyeti.",
      segments=[seg("فَ","fa","conj"), seg("تَجِبُ","wajaba","verb")]),
  tok("مُخَالَفَتُهُ","mukhalafa","noun",["fail","masdar","form-iii-verbs","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ «خَالَفَ» عَلَى مُفَاعَلَةٍ.",
      "The fa'il in raf', a mudaf with the ha annexed — the Form III masdar of خَالَفَ. And the ha is the only word in the second portrait that points at the one being described; the name itself never appears at all.",
      "Merfû fâil, muzâf; hâ muzâfun ileyhtir — «خَالَفَ»nin MUFÂALE vezninde masdarı. Ve hâ, ikinci portrede tarif edilene işaret eden tek kelimedir; ismin kendisi hiç geçmez.",
      punct="."),
 ],
 "jumal": [J("فَيَجِبُ اتِّبَاعُهُ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ بِالْفَاءِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence joined by the fa, with no position in i'rab.",
   "Fâ ile ma'tûf fiil cümlesi; i'râbdan mahalli yoktur."),
  J("مُوَسْوِسٌ سَاعٍ فِي الْفَسَادِ",
   "خَبَرَانِ لِمُبْتَدَإٍ مَحْذُوفٍ، وَالْجُمْلَةُ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "Two khabars of an omitted mubtada; the sentence has no position in i'rab.",
   "Mahzûf bir mübtedânın iki haberi; cümlenin i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "Those are upon guidance from their Lord, and those are the ones who prosper.",
 "tr": "İşte onlar Rablerinden bir hidâyet üzeredir ve işte onlar kurtuluşa erenlerdir."},
 "tokens": [
  tok("أُولَئِكَ","ulaika","pron",["mubtada-khabar","ahwal-al-musnad-ilayh"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "A demonstrative, mabni, in the position of raf' as the mubtada. It is MENTIONED rather than replaced by a pronoun, and the reason is the fourth motive on the dhikr side: extra clarity and reinforcement. A pronoun would have been shorter and would have carried less weight.",
      "İsm-i işaret, mahallen merfû mübtedâ. Zamirle değiştirilmeyip ZİKREDİLMİŞTİR; sebebi de zikir tarafının dördüncü maddesidir: ziyâde îzâh ve takrîr. Zamir daha kısa olurdu ve daha az ağırlık taşırdı."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلِاسْتِعْلَاءِ — وَهُوَ هُنَا مَجَازِيٌّ: الْهُدَى لَيْسَ سَطْحًا يُعْلَى عَلَيْهِ.",
      "A jarr letter of BEING UPON — figuratively here, since guidance is not a surface anyone stands on. The letter is chosen because standing on something is the posture of one who is settled and secure, which is the whole claim of the verse.",
      "İsti'lâ için cer harfi — burada MECÂZÎdir: hidâyet, üzerine çıkılan bir yüzey değildir. Harf, bir şeyin üzerinde durmanın yerleşmiş ve emîn olanın hâli olması sebebiyle seçilmiştir; âyetin bütün iddiası da budur."),
  tok("هُدًى","huda","noun",["huruf-jarr","ism-maqsur-manqus","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«عَلَى» بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ نَكِرَةٌ، وَتَنْوِينُهُ ظَاهِرٌ قَبْلَ الْأَلِفِ. وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرٍ، فَهُوَ ظَرْفٌ مُسْتَقَرٌّ.",
      "Majrur by «ala» with a kasra ESTIMATED on the alif, which cannot bear one — an indefinite maqsur, and its tanwin is written BEFORE the alif, which is the one place a tanwin ever goes that is not the very end. And the phrase is the KHABAR: nothing in the sentence can govern it, so its amil is estimated and the phrase is MUSTAQARR.",
      "«عَلَى» ile, elif hareke kabul etmediği için MUKADDER kesra ile mecrûr — nekre ism-i maksûr; tenvîni eliften ÖNCE yazılır ki bu, tenvînin en sona gelmediği tek yerdir. Ve terkîb HABERdir: cümlede onu amel edecek bir şey yok, âmili takdîr edilir, öyleyse MÜSTAKARdır."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ — وَنُونُهُ سَاكِنَةٌ هُنَا لِأَنَّ مَا بَعْدَهَا مُتَحَرِّكٌ.",
      "A jarr letter of origin — and its nun keeps its sukun here, because the word after it begins with a vowelled letter. Compare the مِنَ of the second sentence: one word, two spellings, and the difference is entirely in what stands next to it.",
      "İbtidâ-i gāye için cer harfi — ve nûnu burada sükûnunu korur, zira ardındaki kelime harekeli başlar. İkinci cümledeki «مِنَ» ile karşılaştırın: tek kelime, iki yazılış; fark tamamen yanında durandadır."),
  tok("رَبِّهِمْ","rabb","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ صِفَةٌ لِـ«هُدًى».",
      "Majrur by «min», a mudaf with the pronoun annexed to it — and the phrase describes «guidance». A jarr phrase falling as a SIFA is another of the four positions only a mustaqarr can hold: the guidance is qualified as being from Him, and the qualification is two letters and a noun.",
      "«مِنْ» ile mecrûr, muzâf; zamir muzâfun ileyhtir — ve câr-mecrûr «هُدًى»nın sıfatıdır. SIFAT olarak düşen câr-mecrûr, yalnız müstakarın tutabileceği dört mevkiden biridir: hidâyet, O'ndan olmakla vasfedilir; vasıf da iki harf ile bir isimdir."),
  tok("وَأُولَئِكَ","ulaika","pron",["atf-nasaq","mubtada-khabar","ahwal-al-musnad-ilayh"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أُولَئِكَ» مُبْتَدَأٌ ثَانٍ فِي مَحَلِّ رَفْعٍ — أُعِيدَ الِاسْمُ وَلَمْ يُؤْتَ بِضَمِيرٍ، زِيَادَةً فِي الْإِيضَاحِ وَالتَّقْرِيرِ.",
      "A joining waw, and «those» is a SECOND mubtada in the position of raf' — the noun is REPEATED where a pronoun would have done, and the repetition is the point. Saying it twice fixes it; and a sentence that has just described a class is exactly the place where a reader's attention needs fixing.",
      "Atıf vâvı; «أُولَئِكَ» mahallen merfû İKİNCİ mübtedâdır — zamir yerine isim TEKRARLANMIŞTIR ve tekrar maksadın kendisidir. İki defa söylemek onu perçinler; ve bir sınıfı henüz tarif etmiş bir cümle, tam da okuyucunun dikkatinin perçinlenmesi gereken yerdir.",
      segments=[seg("وَ","wa","conj"), seg("أُولَئِكَ","ulaika","pron")]),
  tok("هُمُ","hum","pron",["damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ — يُفِيدُ الْحَصْرَ وَالتَّوْكِيدَ، وَضُمَّتْ مِيمُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A pronoun of SEPARATION, with no position in i'rab: it does not fill a slot, it announces that what follows is a khabar and not an adjective — and it carries restriction with it. «Those are the prosperers» becomes «those, they are the prosperers, and no others». Its mim takes a damma for the meeting of two quiescents.",
      "FASIL zamiri; i'râbdan mahalli yoktur — bir mevkiyi doldurmaz, ardındakinin sıfat değil HABER olduğunu ilân eder ve beraberinde hasr getirir. «İşte onlar felâh bulanlardır» ifadesi, «işte onlar, felâh bulanlar ancak onlardır»a döner. Mîmi, iki sâkinin buluşması sebebiyle damme alır."),
  tok("الْمُفْلِحُونَ","muflih","noun",["mubtada-khabar","jam-mudhakkar-salim","ism-fail","form-iv-verbs"],
      "خَبَرٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الْوَاوُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ — اسْمُ فَاعِلٍ مِنْ «أَفْلَحَ» عَلَى مُفْعِلٍ.",
      "The khabar in raf', its sign the WAW because it is a sound masculine plural — the ism fa'il of Form IV أَفْلَحَ. Three participles of three different derived forms stand in this chapter, and until it was written the app's root finder could read none of them: مُقَرِّرٌ, مُوضِحٌ and this one all came back empty.",
      "Merfû haber; ref' alâmeti, cem'-i müzekker-i sâlim olduğu için VÂVdır — «أَفْلَحَ»nin MUF'İL vezninde ism-i fâili. Bu bâbda üç ayrı mezîd bâbın üç vasfı duruyor; ve bâb yazılana kadar uygulamanın kök bulucusu hiçbirini okuyamıyordu: «مُقَرِّرٌ», «مُوضِحٌ» ve bu, üçü de boş dönüyordu.",
      punct="."),
 ],
 "jumal": [J("أُولَئِكَ عَلَى هُدًى مِنْ رَبِّهِمْ",
   "جُمْلَةٌ اسْمِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, with no position in i'rab.",
   "İsim cümlesi; i'râbdan mahalli yoktur."),
  J("وَأُولَئِكَ هُمُ الْمُفْلِحُونَ",
   "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined nominal sentence, with no position in i'rab.",
   "Ma'tûf isim cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "«It is my staff.» — The beloved is here. — The base thief is here.",
 "tr": "«O benim asâmdır.» — Sevgili hazırdır. — Alçak hırsız hazırdır."},
 "tokens": [
  tok("هِيَ","hiya","pron",["mubtada-khabar","ahwal-al-musnad-ilayh"],
      "ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَذُكِرَ وَكَانَ يَسَعُهُ الْحَذْفُ، لِأَنَّ الْمَقَامَ مَقَامُ إِطَالَةٍ: الْمُخَاطَبُ يُحِبُّ أَنْ يَسْمَعَ.",
      "A detached pronoun in the position of raf' as the mubtada — and it is SAID where it could have been dropped. Musa was asked what was in his right hand and could have answered «a staff»; he answers «it is my staff», and then goes on for two more clauses. The motive the books give is the loveliest in the chapter: the speech is lengthened because the One being addressed is one the speaker wants to keep speaking to.",
      "Munfasıl zamir, mahallen merfû mübtedâ — ve hazfedilebilecekken ZİKREDİLMİŞTİR. Mûsâ'ya sağ elindekinin ne olduğu soruldu; «asâ» diyebilirdi, «o benim asâmdır» der ve iki cümle daha devam eder. Kitapların verdiği sebep, bâbın en güzelidir: söz uzatılmıştır, çünkü muhâtab, mütekellimin konuşmayı sürdürmek istediği zâttır."),
  tok("عَصَايَ","asa-staff","noun",["mubtada-khabar","ism-maqsur-manqus","ya-al-mutakallim","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَهُوَ مُضَافٌ وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَالْمَقْصُورُ تَثْبُتُ أَلِفُهُ مَعَ يَاءِ الْمُتَكَلِّمِ وَتُفْتَحُ الْيَاءُ.",
      "The khabar in raf' by a damma estimated on the alif, a mudaf with the ya annexed to it — and here is the exception the speaker's-ya note names: a MAQSUR keeps its alif and the ya takes a FATHA. Everywhere else this ya forces a kasra onto the letter in front of it and swallows the case-vowel; an alif cannot take a kasra, so the collision is resolved the other way round.",
      "Merfû haber; ref' alâmeti elif üzerinde mukadder dammedir; muzâftır, yâ muzâfun ileyhtir — ve işte mütekellim yâsı notunun andığı istisnâ: MAKSÛRun elifi sâbit kalır, yâ FETHA alır. Başka her yerde bu yâ, önündeki harfe kesra dayatır ve i'râb harekesini yutar; elif kesra alamadığı için çatışma ters yönden çözülür.",
      punct="."),
  tok("الْحَبِيبُ","habib","noun",["mubtada-khabar","ahwal-al-musnad-ilayh","sifa-mushabbaha"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَذُكِرَ تَلَذُّذًا بِذِكْرِهِ.",
      "The mubtada in raf' — and it is said for the PLEASURE of saying it. A pronoun would have carried the same information; the name carries something the information does not. This is the motive that most obviously cannot be reduced to communication, which is why the books keep it.",
      "Merfû mübtedâ — ve anmanın LEZZETİ için anılmıştır. Zamir aynı haberi taşırdı; isim, haberin taşımadığı bir şey taşır. Bu, iletişime en açık şekilde indirgenemeyen sebeptir; kitapların onu muhafaza etmesinin sebebi de budur."),
  tok("حَاضِرٌ","hadir","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ عَلَى فَاعِلٍ.",
      "The khabar in raf' — an ism fa'il on فَاعِل.",
      "Merfû haber — FÂİL vezninde ism-i fâil.",
      punct="."),
  tok("السَّارِقُ","sariq","noun",["mubtada-khabar","ahwal-al-musnad-ilayh","ism-fail"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَذُكِرَ إِظْهَارًا لِلْإِهَانَةِ.",
      "The mubtada in raf' — and it is said in order to SHAME him. The sentence is built exactly like the one before it, word for word in shape, and the two motives are opposite. That is the chapter in one pair: the syntax carries no intention at all, and everything a reader hears is carried by the choice of word inside it.",
      "Merfû mübtedâ — ve İHÂNETİ göstermek için anılmıştır. Cümle, bir öncekiyle şekil bakımından kelimesi kelimesine aynı kurulmuştur ve iki maksat birbirinin zıddıdır. Bâb, tek bir çiftte şudur: terkîb hiçbir niyet taşımaz; okuyucunun işittiği her şeyi, içindeki kelime seçimi taşır."),
  tok("اللَّئِيمُ","laim","noun",["naat-sifa","sifa-mushabbaha"],
      "نَعْتٌ لِـ«السَّارِقُ» مَرْفُوعٌ — صِفَةٌ مُشَبَّهَةٌ عَلَى فَعِيلٍ.",
      "A na't of «the thief», in raf' — a sifa mushabbaha on فَعِيل, the fourth in this chapter after عَلِيلٌ, طَوِيلٌ and الْحَبِيبُ. One scale, four words, and every one of them a settled quality rather than an act.",
      "«السَّارِقُ»un merfû na'tı — FA'ÎL vezninde sıfat-ı müşebbehe; «عَلِيلٌ», «طَوِيلٌ» ve «الْحَبِيبُ»den sonra bu bâbdaki dördüncüsü. Tek vezin, dört kelime; ve her biri bir fiil değil, yerleşmiş bir vasıf."),
  tok("حَاضِرٌ","hadir","noun",["mubtada-khabar","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — وَهُوَ الْخَبَرُ نَفْسُهُ الَّذِي فِي الْجُمْلَةِ قَبْلَهَا، وَلَمْ يَتَغَيَّرْ شَيْءٌ إِلَّا الْمُسْنَدَ إِلَيْهِ.",
      "The khabar in raf' — the SAME khabar as the sentence before it, unchanged. Nothing moved but the musnad ilayh, and the chapter ends by proving its own thesis: the states of the subject are where the meaning of a plain sentence is decided.",
      "Merfû haber — bir önceki cümledeki haberin AYNISI, hiç değişmemiş. Müsnedün ileyhten başka hiçbir şey yer değiştirmedi; ve bâb, kendi iddiasını ispat ederek biter: sade bir cümlenin mânâsı, müsnedün ileyhin hâllerinde kararlaştırılır.",
      punct="."),
 ],
 "jumal": [J("هِيَ عَصَايَ",
   "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ مَقُولُ الْقَوْلِ.",
   "A nominal sentence in the position of nasb as what was said.",
   "Mekūlü'l-kavl olarak mahallen mansub isim cümlesi."),
  J("السَّارِقُ اللَّئِيمُ حَاضِرٌ",
   "جُمْلَةٌ اسْمِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A nominal sentence, with no position in i'rab.",
   "İsim cümlesi; i'râbdan mahalli yoktur.")]})

GLOSS_ADD = {
 "kayfa":     g("كَيْفَ", None, "noun", "how? (an interrogative NOUN, not a letter)", "nasıl? (istifham İSMİ, harf değil)", 2),
 "alil":      g("عَلِيل", "ع ل ل", "noun", "ill, ailing (sifa mushabbaha)", "hasta (sıfat-ı müşebbehe)", 3),
 "sahar":     g("سَهَر", "س ه ر", "noun", "sleeplessness, wakefulness at night", "uykusuzluk, gece uyanıklığı", 4),
 "daim":      g("دَائِم", "د و م", "noun", "lasting, unceasing (ism fa'il of a hollow verb)", "dâim, sürekli (ecvefden ism-i fâil)", 3),
 "huzn":      g("حُزْن", "ح ز ن", "noun", "grief, sorrow", "hüzün, keder", 2, plural="أَحْزَان"),
 "tawil-long": g("طَوِيل", "ط و ل", "noun", "long (sifa mushabbaha)", "uzun (sıfat-ı müşebbehe)", 2),
 "mustafad":  g("مُسْتَفَاد", "ف ي د", "noun", "drawn from, derived (ism maf'ul, Form X)", "istifade edilmiş (ism-i mef'ûl, istif'âl)", 5),
 "istafada":  g("اسْتَفَادَ", "ف ي د", "verb", "to draw benefit from, to derive", "istifade etmek, elde etmek", 4, form="X"),
 "muqarrir":  g("مُقَرِّر", "ق ر ر", "noun", "one who confirms and establishes (ism fa'il, Form II)", "takrîr eden, yerleştiren (ism-i fâil, tef'îl)", 5),
 "sharia":    g("شَرِيعَة", "ش ر ع", "noun", "a revealed Law", "şerîat", 3, plural="شَرَائِع"),
 "mudih":     g("مُوضِح", "و ض ح", "noun", "one who makes plain (ism fa'il, Form IV of a mithal)", "açıklayan (ism-i fâil, if'âl — misâl kökten)", 5),
 "ittiba":    g("اتِّبَاع", "ت ب ع", "noun", "following, adherence (masdar, Form VIII)", "ittibâ, uyma (masdar, iftiâl)", 4),
 "muwaswis":  g("مُوَسْوِس", "و س و س", "noun", "one who whispers evil (ism fa'il of a quadriliteral)", "vesvese veren (rubâîden ism-i fâil)", 5),
 "sai":       g("سَاعٍ (السَّاعِي)", "س ع ي", "noun", "one who hurries or strives (ism fa'il, manqus)", "koşan, sa'y eden (ism-i fâil, menkūs)", 4),
 "ulaika":    g("أُولَئِكَ", None, "pron", "those (plural demonstrative)", "işte onlar (cemi ism-i işaret)", 2),
 "huda":      g("هُدًى", "ه د ي", "noun", "guidance (a maqsur noun)", "hidâyet (ism-i maksûr)", 3),
 "muflih":    g("مُفْلِح", "ف ل ح", "noun", "one who prospers, who attains (ism fa'il, Form IV)", "felâh bulan, kurtuluşa eren (ism-i fâil, if'âl)", 4),
 "aflaha":    g("أَفْلَحَ", "ف ل ح", "verb", "to prosper, to attain what is sought", "felâh bulmak, kurtuluşa ermek", 4, form="IV"),
 "asa-staff": g("عَصًا", "ع ص و", "noun", "a staff, a stick (a maqsur noun)", "asâ, değnek (ism-i maksûr)", 3, plural="عِصِيّ"),
 "habib":     g("حَبِيب", "ح ب ب", "noun", "a beloved one (sifa mushabbaha)", "sevgili, habîb (sıfat-ı müşebbehe)", 2),
 "sariq":     g("سَارِق", "س ر ق", "noun", "a thief (ism fa'il)", "hırsız (ism-i fâil)", 2),
 "hadir":     g("حَاضِر", "ح ض ر", "noun", "present, here (ism fa'il)", "hazır, mevcut (ism-i fâil)", 2),
 # COPIED from other packages, lemma-identical — a lex key is global.
 "qala":      g("قَالَ", "ق و ل", "verb", "to say", "demek, söylemek", 1, form="I"),
 "anta":      g("أَنْتَ", None, "pron", "you (masc. sg., detached)", "sen (munfasıl, eril)", 1),
 "min":       g("مِنْ", None, "prep", "from, of", "-den, -dan", 1),
 "ala":       g("عَلَى", None, "prep", "upon, over", "üzerine, üzere", 1),
 "nur":       g("نُور", "ن و ر", "noun", "light", "nur, ışık", 2, plural="أَنْوَار"),
 "hilal":     g("هِلَال", "ه ل ل", "noun", "the new moon, a crescent", "hilâl, yeni ay", 3),
 "dalil":     g("دَلَائِل", "د ل ل", "noun", "proofs, indications", "deliller", 3),
 "fasad":     g("فَسَاد", "ف س د", "noun", "corruption, spoiling", "fesad, bozgunculuk", 3),
 "laim":      g("لَئِيم", "ل أ م", "noun", "base, ignoble", "alçak, aşağılık", 4),
 "rabb":      g("رَبّ", "ر ب ب", "noun", "Lord, master", "Rab", 1, plural="أَرْبَاب"),
 "hum":       g("هُمْ", None, "pron", "they (masc. pl.)", "onlar (eril)", 1),
}

def build_morph():
    out = {}
    for pkg, lex in [("wasiyyat-abi-yusuf-l5", "qala")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    # اسْتَفَادَ — Form X AJWAF. Its ism maf'ul مُسْتَفَاد is s2's khabar, and the
    # melt is the same one the reader's sarfDerive applies to IV/VII/VIII/X.
    out["istafada"] = _sg.derived_hollow(_sg.B10 + " — أَجْوَفُ يَائِيٌّ", _sg.W10, "َ",
                                         "اِسْتَفَاد", "اِسْتَفَد", "سْتَفِيد", "سْتَفِد",
                                         "اِسْتَفِيد", "اِسْتَفِد",
                                         "اِسْتِفَادَة", "مُسْتَفِيد", maful="مُسْتَفَاد",
                                         pmz="اُسْتُفِيدَ", pmd="يُسْتَفَادُ",
                                         note="أَجْوَفُ مِنَ الِاسْتِفْعَالِ: يَسْتَفْوِدُ ← نُقِلَتِ الْحَرَكَةُ ثُمَّ قُلِبَتِ الْوَاوُ أَلِفًا فِي الْمَاضِي وَيَاءً فِي الْمُضَارِعِ.")
    # أَفْلَحَ — Form IV sound; مُفْلِح is the Baqara verse's khabar.
    out["aflaha"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْلَح", "فْلِح", "أَفْلِح",
                                "إِفْلَاح", "مُفْلِح")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/7.json").write_text(
    json.dumps({"chapter": 7, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 7 for c in man["chapters"]):
    man["chapters"].append({"n": 7, "title": TITLE7})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.7.0"
ADD_EN = (" Chapter 7 is built the same way from the same file (lines ~665-712), which carries every "
          "one of its examples in vowelled Arabic: the poet's bayt, the moon and the crescent, the "
          "two four-word portraits with their fa of consequence, al-Baqara 2:5, Taha 20:18, and the "
          "three حَاضِرٌ sentences.")
ADD_TR = (" Yedinci bâb da aynı dosyadan (satır ~665-712) aynı usûlle kurulmuştur; o satırlar bâbın "
          "bütün misallerini harekeli Arapça olarak taşır: şairin beyti, ay ile hilâl, tefrî' fâsını "
          "taşıyan dört kelimelik iki portre, Bakara 2:5, Tâhâ 20:18 ve üç «حَاضِرٌ» cümlesi.")
if "2:5" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch7:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
