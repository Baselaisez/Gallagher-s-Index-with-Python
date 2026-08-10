# -*- coding: utf-8 -*-
"""Author chapter 3 of mukhtasar-al-manar — the remaining two sources, ijma' and qiyas.

Chapter 2 named the four and defined the first two. This chapter closes the list
with the two RATIONAL sources, and the matn keeps the same shape it set up:
وَأَمَّا … فَهُوَ, once each.

ATTRIBUTION: the two definitions here are the received formulas of the Hanafi
usul tradition, carried in the same words by every edition; they are NOT from
the owner's supplied page, which stops at page 1. The closing sentence (s3) is
an ORIGINAL bridge written for this reader, not matn, and is marked as such in
the manifest attribution in both languages.

Grammar this chapter is chosen to teach:
  • الْمُجْتَهِدِينَ as mudaf ilayh — a SOUND MASCULINE PLURAL losing its nun to
    the idafa, the same rule chapter 2 showed on a dual. Two shapes, one law.
  • اِتِّفَاق — the Form VIII masdar whose ta is not original: و ف ق gave
    اِوْتِفَاق, and the waw was swallowed into the ta. The I'lal Lab's case.
  • تَعْدِيَة — a Form II masdar of a NAQIS verb: تَفْعِيل cannot stand on a weak
    lam, so the ta marbuta comes in to make good the loss.
  • عَلَيْهَا مَدَارُ الْأَحْكَامِ — a shibh-jumla khabar put BEFORE its mubtada,
    inside a sila. Fronting is the point: it is what makes the clause say
    "on THESE, and on nothing else."
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/mukhtasar-al-manar"
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

TITLE3 = {"ar": "الْإِجْمَاعُ وَالْقِيَاس", "en": "Consensus and Analogy", "tr": "İcmâ ve Kıyâs"}

S.append({"id": "s1", "translation": {
 "en": "And as for consensus, it is the agreement of the mujtahids of Muhammad's community, in one age, upon a legal ruling.",
 "tr": "İcmâ'a gelince, o, Muhammed ümmetinin müctehidlerinin bir asırda şer'î bir hüküm üzerinde ittifâk etmesidir."},
 "tokens": [
  tok("وَأَمَّا","amma","part",["atf-nasaq","amma-tafsiliyya"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَمَّا» تَفْصِيلِيَّةٌ — وَهَذَا الْبَنْدُ الثَّالِثُ مِنَ التَّعْدَادِ.",
      "A joining waw and the detailing «amma» — this is the third item of the enumeration.",
      "Atıf vâvı ve tafsîl «emmâ»sı — sayımın üçüncü maddesidir.",
      segments=[seg("وَ","wa","conj"), seg("أَمَّا","amma","part")]),
  tok("الْإِجْمَاعُ","ijma","noun",["mubtada-khabar","amma-tafsiliyya"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ الْفَاصِلُ بَيْنَ «أَمَّا» وَفَائِهَا.",
      "The mubtada in raf', and the thing standing between «amma» and its fa.",
      "Merfû mübtedâ; «أَمَّا» ile fâsı arasındaki fâsıldır."),
  tok("فَهُوَ","huwa","pron",["amma-tafsiliyya","damir-fasl"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ«هُوَ» مُبْتَدَأٌ ثَانٍ، وَالْجُمْلَةُ خَبَرُ الْأَوَّلِ.",
      "The FA of «amma»'s answer, and «huwa» a second mubtada; the clause is the khabar of the first.",
      "«أَمَّا»nın cevabındaki fâ; «هُوَ» ikinci mübtedâ, cümle de birincinin haberidir.",
      segments=[seg("فَ","fa","conj"), seg("هُوَ","huwa","pron")]),
  tok("اِتِّفَاقُ","ittifaq","noun",["mubtada-khabar","masdar","form-viii-verbs","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «اِتَّفَقَ» عَلَى اِفْتِعَالٍ، وَأَصْلُهُ «اِوْتِفَاقٌ» مِنْ «و ف ق»، فَأُبْدِلَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ.",
      "The khabar in raf', and a mudaf — the masdar of اِتَّفَقَ on اِفْتِعَال. Its origin is اِوْتِفَاق from و ف ق: the WAW was turned into a ta and swallowed into the ta of the pattern. The doubled ta you see is two letters, only one of them original.",
      "Merfû haber ve muzâf — «اِتَّفَقَ»nin İFTİÂL vezninde masdarı. Aslı «و ف ق»tan «اِوْتِفَاق»tır; VÂV tâya kalbedilip vezindeki tâya idgâm edilmiştir. Gördüğün şeddeli tâ iki harftir, biri aslî değildir."),
  tok("الْمُجْتَهِدِينَ","mujtahid","noun",["idafa-definiteness","jam-mudhakkar-salim","ism-fail","form-viii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَحُذِفَتْ نُونُهُ لِلْإِضَافَةِ — كَمَا حُذِفَتْ نُونُ الْمُثَنَّى قَبْلُ.",
      "The mudaf ilayh, in jarr by the YA because it is a SOUND MASCULINE PLURAL — and its NUN has fallen for the idafa, exactly as the dual's nun fell in the chapter before. One law, two shapes.",
      "Mecrûr muzâfun ileyh; CEM'-İ MÜZEKKER-İ SÂLİM olduğu için YÂ ile mecrûrdur ve NÛNu izâfet sebebiyle düşmüştür — önceki bölümde tesniyenin nûnu nasıl düştüyse öyle. Tek kural, iki şekil."),
  tok("مِنْ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلتَّبْعِيضِ، وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنَ «الْمُجْتَهِدِينَ».",
      "A jarr letter of PART-OF; the phrase is a hal from «the mujtahids».",
      "Teb'îz için cer harfi; câr-mecrûr «الْمُجْتَهِدِينَ»den hâldir."),
  tok("أُمَّةِ","umma","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ.",
      "In jarr after «min», and itself a mudaf.",
      "«مِنْ» ile mecrûr ve kendisi de muzâf."),
  tok("مُحَمَّدٍ","muhammad","noun",["idafa-definiteness","ism-maful","form-ii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَمٌ مَنْقُولٌ مِنِ اسْمِ مَفْعُولِ «حَمَّدَ»: الْمَحْمُودُ مَرَّةً بَعْدَ مَرَّةٍ.",
      "The mudaf ilayh in jarr — a proper name carried over from the ism maf'ul of حَمَّدَ: the one praised again and again.",
      "Mecrûr muzâfun ileyh — «حَمَّدَ»nin ism-i mef'ûlünden nakledilmiş alemdir: tekrar tekrar hamdedilen."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ، مُتَعَلِّقٌ بِـ«اِتِّفَاقُ».",
      "A jarr letter of containment, attaching to «the agreement».",
      "Zarfiyye için cer harfi; «اِتِّفَاقُ»a taalluk eder."),
  tok("عَصْرٍ","asr","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي» — وَتَنْكِيرُهُ مَقْصُودٌ: أَيُّ عَصْرٍ كَانَ، لَا الْعَصْرُ الْأَوَّلُ وَحْدَهُ.",
      "In jarr after «fi» — and it is left INDEFINITE on purpose: any one age, not the first age alone.",
      "«فِي» ile mecrûr — nekre bırakılması kasıtlıdır: herhangi bir asır, yalnız ilk asır değil."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلِاسْتِعْلَاءِ الْمَعْنَوِيِّ، مُتَعَلِّقٌ بِـ«اِتِّفَاقُ» — وَهُوَ الَّذِي يُبَيِّنُ عَلَامَ وَقَعَ الِاتِّفَاقُ.",
      "A jarr letter of resting-upon in the figurative sense, attaching to «the agreement» — this is the word that says WHAT they agreed on.",
      "Ma'nevî isti'lâ için cer harfi; «اِتِّفَاقُ»a taalluk eder — ittifâkın NE ÜZERİNE olduğunu bildiren kelimedir."),
  tok("حُكْمٍ","hukm","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى».", "In jarr after «ala».", "«عَلَى» ile mecrûr."),
  tok("شَرْعِيٍّ","shari","noun",["naat-sifa"],
      "نَعْتٌ لِـ«حُكْمٍ» مَجْرُورٌ — اسْمٌ مَنْسُوبٌ بِيَاءِ النِّسْبَةِ، وَبِهِ خَرَجَ الْحُكْمُ الْعَقْلِيُّ وَالْحِسِّيُّ.",
      "A na't of «a ruling», in jarr — a NISBA noun made with the ya of relation, and by it the rational and the sensory ruling are shut out.",
      "«حُكْمٍ»in na'tı, mecrûr — nisbet yâsıyla yapılmış mensûb isimdir; onunla aklî ve hissî hüküm dışarıda kalır.",
      punct="."),
 ],
 "jumal": [J("الْإِجْمَاعُ هُوَ اِتِّفَاقُ الْمُجْتَهِدِينَ",
   "جُمْلَةٌ اسْمِيَّةٌ وَقَعَتْ جَوَابًا لِـ«أَمَّا» — لَا مَحَلَّ لَهَا.",
   "A nominal clause standing as «amma»'s answer — i'rabless.",
   "«أَمَّا»nın cevabı olarak düşen isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And as for analogy, it is the carrying of the ruling from the root case to the branch case by a cause that gathers the two.",
 "tr": "Kıyâs'a gelince, o, hükmü, iki tarafı toplayan bir illetle asıldan fer'e taşımaktır."},
 "tokens": [
  tok("وَأَمَّا","amma","part",["atf-nasaq","amma-tafsiliyya"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَمَّا» تَفْصِيلِيَّةٌ — وَهَذَا الْبَنْدُ الرَّابِعُ وَالْأَخِيرُ.",
      "A joining waw and the detailing «amma» — the fourth and last item.",
      "Atıf vâvı ve tafsîl «emmâ»sı — dördüncü ve son maddedir.",
      segments=[seg("وَ","wa","conj"), seg("أَمَّا","amma","part")]),
  tok("الْقِيَاسُ","qiyas","noun",["mubtada-khabar","amma-tafsiliyya"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَهُوَ الْفَاصِلُ.", "The mubtada in raf', and the separator.",
      "Merfû mübtedâ ve fâsıl."),
  tok("فَهُوَ","huwa","pron",["amma-tafsiliyya","damir-fasl"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ «أَمَّا»، وَ«هُوَ» مُبْتَدَأٌ ثَانٍ.",
      "The FA of «amma»'s answer, and «huwa» a second mubtada.",
      "«أَمَّا»nın cevabındaki fâ; «هُوَ» ikinci mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("هُوَ","huwa","pron")]),
  tok("تَعْدِيَةُ","tadiya","noun",["mubtada-khabar","masdar","form-ii-verbs","naqis-verbs","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «عَدَّى» عَلَى تَفْعِيلٍ، وَلَمَّا كَانَ لَامُهُ مُعْتَلًّا لَمْ يَسْتَقِمْ «تَعْدِيلٌ»، فَعُوِّضَ عَنِ الْيَاءِ بِالتَّاءِ الْمَرْبُوطَةِ.",
      "The khabar in raf', and a mudaf — the masdar of عَدَّى on تَفْعِيل. Because its LAM is weak, تَفْعِيل could not stand, so the TA MARBUTA came in to make good what the weak letter cost. Every Form II naqis masdar is built this way: تَزْكِيَة، تَسْمِيَة، تَعْدِيَة.",
      "Merfû haber ve muzâf — «عَدَّى»nin TEF'ÎL vezninde masdarı. Lâmı illetli olduğu için «تَعْدِيل» düzgün olmadı; yâdan bedel olarak TÂ-İ MERBÛTA getirildi. Nâkıs olan her tef'îl masdarı böyledir: تَزْكِيَة، تَسْمِيَة، تَعْدِيَة."),
  tok("الْحُكْمِ","hukm","noun",["idafa-definiteness","maful-bihi"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ فِي اللَّفْظِ، وَهُوَ مَفْعُولُ الْمَصْدَرِ فِي الْمَعْنَى: الْمُعَدَّى هُوَ الْحُكْمُ.",
      "The mudaf ilayh in jarr by its FORM, but the masdar's OBJECT in meaning: the thing carried across is the ruling.",
      "Lafzan mecrûr muzâfun ileyh; ma'nen masdarın mef'ûlüdür: taşınan şey hükümdür."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ، مُتَعَلِّقٌ بِـ«تَعْدِيَةُ» — وَفُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter for the START of the span, attaching to «the carrying» — its nun takes a fatha because two sukuns met.",
      "İbtidâ-i gāye için cer harfi; «تَعْدِيَةُ»ye taalluk eder — iki sâkin karşılaştığı için nûnu fetha almıştır."),
  tok("الْأَصْلِ","asl","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ» — وَهُوَ الْمَقِيسُ عَلَيْهِ الَّذِي وَرَدَ فِيهِ النَّصُّ.",
      "In jarr after «min» — the case measured AGAINST, the one the text actually spoke about.",
      "«مِنْ» ile mecrûr — hakkında nass vârid olan, kendisine kıyas edilen taraftır."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِانْتِهَاءِ الْغَايَةِ، مُتَعَلِّقٌ بِـ«تَعْدِيَةُ» — وَبِهِ تَمَّتِ الْغَايَتَانِ.",
      "A jarr letter for the END of the span, attaching to «the carrying» — with it both ends of the span are set.",
      "İntihâ-i gāye için cer harfi; «تَعْدِيَةُ»ye taalluk eder — iki gāye onunla tamamlanır."),
  tok("الْفَرْعِ","far","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«إِلَى» — وَهُوَ الْمَقِيسُ الَّذِي سَكَتَ عَنْهُ النَّصُّ.",
      "In jarr after «ila» — the case measured, the one the text was silent about.",
      "«إِلَى» ile mecrûr — nassın sükût ettiği, kıyas edilen taraftır."),
  tok("بِعِلَّةٍ","illa","noun",["huruf-jarr"],
      "الْبَاءُ لِلسَّبَبِيَّةِ، وَالْمَجْرُورُ بِهَا «عِلَّةٍ» — وَهِيَ الْوَصْفُ الَّذِي عُلِّقَ بِهِ الْحُكْمُ.",
      "The BA of causation, and «a cause» in jarr after it — the property the ruling was hung upon.",
      "Sebebiyye bâsı ve onunla mecrûr «عِلَّةٍ» — hükmün kendisine bağlandığı vasıftır.",
      segments=[seg("بِ","bi","prep"), seg("عِلَّةٍ","illa","noun")]),
  tok("جَامِعَةٍ","jamia","noun",["naat-sifa","ism-fail"],
      "نَعْتٌ لِـ«عِلَّةٍ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «جَمَعَ»، وَبِهِ خَرَجَتِ الْعِلَّةُ الْقَاصِرَةُ الَّتِي لَا تَتَعَدَّى أَصْلَهَا.",
      "A na't of «a cause», in jarr — the ism fa'il of جَمَعَ, and by it the CONFINED cause is shut out: a cause that never reaches past its own case cannot carry a ruling anywhere.",
      "«عِلَّةٍ»in na'tı, mecrûr — «جَمَعَ»nin ism-i fâili; onunla kāsır illet dışarıda kalır: kendi aslını aşamayan illet hiçbir yere hüküm taşıyamaz.",
      punct="."),
 ],
 "jumal": [J("الْقِيَاسُ هُوَ تَعْدِيَةُ الْحُكْمِ",
   "جُمْلَةٌ اسْمِيَّةٌ وَقَعَتْ جَوَابًا لِـ«أَمَّا» — لَا مَحَلَّ لَهَا.",
   "A nominal clause standing as «amma»'s answer — i'rabless.",
   "«أَمَّا»nın cevabı olarak düşen isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "So these are the four principles upon which the rulings turn.",
 "tr": "İşte hükümlerin medârı olan dört asıl bunlardır."},
 "tokens": [
  tok("فَهَذِهِ","hadhihi","pron",["mubtada-khabar","huruf-tanbih"],
      "الْفَاءُ فَصِيحَةٌ، وَ«هَذِهِ» اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالْهَاءُ فِيهِ لِلتَّنْبِيهِ.",
      "A «telling» fa — the one that answers a condition the words leave unsaid — and «hadhihi» a demonstrative, fixed in form, in the position of raf' as mubtada. The HA in front of it is the ha of drawing attention.",
      "Fasîha fâsı — söylenmemiş bir şartın cevâbını getiren fâ — ve «هَذِهِ» mebnî ism-i işârettir, mübtedâ olarak mahallen merfûdur. Başındaki HÂ tenbîh hâsıdır.",
      segments=[seg("فَ","fa","conj"), seg("هَذِهِ","hadhihi","pron")]),
  tok("هِيَ","hiya","pron",["damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ — جِيءَ بِهِ لِيُعْلَمَ أَنَّ مَا بَعْدَهُ خَبَرٌ لَا نَعْتٌ، وَلِيُفِيدَ الْقَصْرَ: هَذِهِ الْأَرْبَعَةُ لَا غَيْرُ.",
      "A PRONOUN OF SEPARATION, with no position in i'rab. It is brought for two reasons: so the reader knows what follows is the KHABAR and not another adjective, and to give restriction — these four and no others.",
      "Mahalli olmayan FASIL ZAMÎRİ. İki sebeple getirilir: sonrasının na't değil HABER olduğu bilinsin diye ve kasr ifâde etsin diye — bu dört, başkası değil."),
  tok("الْأُصُولُ","usul","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ — جَمْعُ «أَصْلٍ».",
      "The khabar in raf' by the damma — the plural of «asl».",
      "Damme ile merfû haber — «أَصْل»in cemidir."),
  tok("الْأَرْبَعَةُ","arbaa","noun",["naat-sifa"],
      "نَعْتٌ مَرْفُوعٌ — وَلَحِقَتْهُ التَّاءُ لِأَنَّ مَعْدُودَهُ «أُصُولٌ» مُذَكَّرٌ، كَمَا مَرَّ فِي أَوَّلِ الْبَابِ.",
      "A na't in raf' — and it wears the TA because what it counts, «principles», is masculine, exactly as at the head of this section.",
      "Merfû na't — ma'dûdu olan «أُصُول» müzekker olduğu için TÂ almıştır; bâbın başında geçtiği gibi."),
  tok("الَّتِي","allati","pron",["ism-mawsul","jumla-sifa"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ نَعْتٌ ثَانٍ لِـ«الْأُصُولُ» — وَجَاءَ بِصِيغَةِ الْمُفْرَدَةِ الْمُؤَنَّثَةِ لِأَنَّ جَمْعَ غَيْرِ الْعَاقِلِ يُعَامَلُ مُعَامَلَتَهَا.",
      "A relative noun, fixed in form, in the position of raf' as a SECOND na't of «the principles» — and it comes in the feminine singular shape because a plural of non-rational things is treated as one feminine thing.",
      "Mebnî ism-i mevsûl; «الْأُصُولُ»un ikinci na'tı olarak mahallen merfûdur — gayr-i âkil cemi müfred müennes muâmelesi gördüğü için müfred müennes sîgasıyla gelmiştir."),
  tok("عَلَيْهَا","ala","prep",["huruf-jarr","mubtada-khabar"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — وَتَقْدِيمُهُ هُوَ الَّذِي أَفَادَ الِاخْتِصَاصَ: عَلَيْهَا وَحْدَهَا.",
      "A jarr-majrur standing as the khabar, and standing FIRST. The fronting is the whole point: it is what makes the clause say «on these, and on nothing else.»",
      "Mukaddem haber olan câr-mecrûr. İhtisâsı sağlayan şey bu takdîmdir: yalnız onların üzerine.",
      segments=[seg("عَلَى","ala","prep"), seg("هَا","pron-3fs","pron")]),
  tok("مَدَارُ","madar","noun",["mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — اسْمُ مَكَانٍ مِنْ «دَارَ»: الْمَوْضِعُ الَّذِي يُدَارُ عَلَيْهِ.",
      "The mubtada, in raf' and coming LAST, and a mudaf — a place-noun from دَارَ: the point a thing turns about.",
      "Muahhar merfû mübtedâ ve muzâf — «دَارَ»dan ism-i mekân: üzerinde dönülen yer."),
  tok("الْأَحْكَامِ","ahkam","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ خُتِمَ الْبَابُ عَلَى مَا فُتِحَ بِهِ: أَرْبَعَةٌ، وَأَحْكَامٌ تَدُورُ عَلَيْهَا.",
      "The mudaf ilayh in jarr — and with it the section closes on what it opened with: four, and rulings that turn upon them.",
      "Mecrûr muzâfun ileyh — bâb, açıldığı şeyle kapanır: dört asıl ve onların üzerinde dönen hükümler.",
      punct="."),
 ],
 "jumal": [J("عَلَيْهَا مَدَارُ الْأَحْكَامِ",
   "جُمْلَةٌ اسْمِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A nominal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan isim cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "ittifaq":  g("اِتِّفَاق", "و ف ق", "noun", "agreement, concurrence (masdar, Form VIII)", "ittifâk (masdar)", 4),
 "mujtahid": g("مُجْتَهِد", "ج ه د", "noun", "a mujtahid — one qualified to derive rulings", "müctehid", 4,
               plural="مُجْتَهِدُونَ"),
 "umma":     g("أُمَّة", "أ م م", "noun", "community, nation", "ümmet", 2, plural="أُمَم"),
 "muhammad": g("مُحَمَّد", "ح م د", "noun", "Muhammad (the Prophet)", "Muhammed", 1),
 "fi":       g("فِي", None, "prep", "in, within (jarr letter)", "-de, içinde (cer harfi)", 1),
 "asr":      g("عَصْر", "ع ص ر", "noun", "an age, a generation", "asır, çağ", 2, plural="أَعْصَار"),
 "hukm":     g("حُكْم", "ح ك م", "noun", "a ruling, a judgement", "hüküm", 2, plural="أَحْكَام"),
 "shari":    g("شَرْعِيّ", "ش ر ع", "noun", "legal, of the Shari'a (nisba)", "şer'î (nisbet)", 3),
 "tadiya":   g("تَعْدِيَة", "ع د و", "noun", "carrying across, transfer (masdar, Form II)", "ta'diye; taşıma (masdar)", 5),
 "far":      g("فَرْع", "ف ر ع", "noun", "branch case — the one being measured", "fer'; kıyas edilen taraf", 3,
               plural="فُرُوع"),
 "illa":     g("عِلَّة", "ع ل ل", "noun", "cause, the property a ruling hangs on", "illet", 3, plural="عِلَل"),
 "jamia":    g("جَامِعَة", "ج م ع", "noun", "gathering, joining two things (ism fa'il, fem.)", "câmia; iki tarafı toplayan", 3),
 "hadhihi":  g("هَذِهِ", None, "pron", "this (feminine)", "bu (müennes)", 1),
 "hiya":     g("هِيَ", None, "pron", "she, it (detached)", "o (müennes, munfasıl)", 1),
 "allati":   g("الَّتِي", None, "pron", "which, that (fem. relative)", "ki o (müennes ism-i mevsûl)", 1),
 "madar":    g("مَدَار", "د و ر", "noun", "the pivot, what a thing turns upon", "medâr; üzerinde dönülen nokta", 4),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/3.json").write_text(
    json.dumps({"chapter": 3, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 3 for c in man["chapters"]):
    man["chapters"].append({"n": 3, "title": TITLE3})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.3.0"
# The closing sentence is ours, not the matn's. Say so, in every language the
# reader can switch to — an unmarked original inside a quoted text is the one
# thing this package must never ship.
ORIG = {
 "en": ("In chapter 3 the definitions of consensus and analogy are the received formulas of the "
        "tradition; the closing sentence («So these are the four principles upon which the rulings "
        "turn») is ORIGINAL — written for this reader as a bridge, and not part of the matn."),
 "tr": ("Üçüncü bölümde icmâ ve kıyâs tarifleri geleneğin meşhûr ibâreleridir; kapanış cümlesi "
        "(«İşte hükümlerin medârı olan dört asıl bunlardır») ise ORİJİNALdir — matnın parçası "
        "değil, bu okuyucu için yazılmış bir geçiş cümlesidir."),
 "ar": ("وَتَعْرِيفَا الْإِجْمَاعِ وَالْقِيَاسِ فِي الْبَابِ الثَّالِثِ هُمَا الْمُتَدَاوَلَانِ عِنْدَ أَهْلِ الْفَنِّ، "
        "وَأَمَّا الْجُمْلَةُ الْخَاتِمَةُ فَمِنْ إِنْشَائِنَا لَا مِنَ الْمَتْنِ، وُضِعَتْ لِلتَّخَلُّصِ لَا غَيْرُ."),
}
for lang, txt in ORIG.items():
    cur = man["attribution"].get(lang, "").strip()
    if txt not in cur:
        man["attribution"][lang] = (cur + " " + txt).strip()
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch3:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
