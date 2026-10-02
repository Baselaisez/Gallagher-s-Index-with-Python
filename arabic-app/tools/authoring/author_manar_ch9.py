# -*- coding: utf-8 -*-
"""Author chapter 9 of mukhtasar-al-manar — the UNRESTRICTED and the RESTRICTED.

Chapter 8 took the two forms that carry the rulings. This one takes the two
STATES a khass wording can be in — bare, or carrying a description over and
above what it names — and closes on the Hanafi rule about carrying one onto
the other, which is one of the school's best-known positions.

ATTRIBUTION: like chapters 2–8, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • يَنْقَسِمُ إِلَى — Form VII, and the verb whose preposition is part of its
    meaning: قَسَمَ divides a thing, اِنْقَسَمَ is the thing dividing of itself.
  • زَائِدٍ — the ism fa'il of زَادَ, an AJWAF YAI whose melted middle comes back
    as a HAMZA in the participle: زَيَد → زَائِد. Chapters 5 and 6 used the same
    root through اِزْدَادَ; this is the third face of ز ي د in the package.
  • لَا … إِلَّا بِدَلِيلٍ — the THIRD istithna mufarragh in four chapters, and by
    now the reader should see the shape before reading the words.
  • إِذَا … حُمِلَ — a conditional whose jawab is a majhul past, and the whole
    two-clause sentence is what the school's position actually says.
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

TITLE9 = {"ar": "الْمُطْلَقُ وَالْمُقَيَّد", "en": "The Unrestricted and the Restricted",
          "tr": "Mutlak ve Mukayyed"}

S.append({"id": "s1", "translation": {
 "en": "Then the specific divides into unrestricted and restricted.",
 "tr": "Hâss, mutlak ve mukayyed olmak üzere ikiye ayrılır."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي.",
      "A letter of atf giving sequence with an interval.",
      "Terâhî ile tertîb için atıf harfi."),
  tok("الْخَاصُّ","khass","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — وَهُوَ الْخَاصُّ الَّذِي حُدَّ فِي الْبَابِ الرَّابِعِ، عَادَ الْآنَ لِيُقَسَّمَ.",
      "The fa'il in raf' — the very khass that was defined in chapter 4, come back now to be divided. A term is defined once and then worked; that is how a matn is built.",
      "Merfû fâil — dördüncü bâbda tarif edilen hâssın kendisidir; şimdi taksîm edilmek üzere geri dönmüştür. Bir ıstılah bir kere tarif edilir, sonra üzerinde çalışılır; metin böyle kurulur."),
  tok("يَنْقَسِمُ","inqasama","verb",["mudari-marfu","form-vii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ عَلَى «اِنْفَعَلَ» — وَهُوَ مُطَاوِعُ «قَسَمَ»: ذَاكَ يَقْسِمُ غَيْرَهُ، وَهَذَا يَنْقَسِمُ بِنَفْسِهِ.",
      "A mudari in raf' on اِنْفَعَلَ — the MUTAWA'A of قَسَمَ: that verb divides something else, this one is the thing dividing of itself. Form VII is the whole difference, and the matn chose it deliberately: the division is in the wording's own nature, not something a jurist does to it.",
      "«اِنْفَعَلَ» vezninde merfû muzâri — «قَسَمَ»in MUTÂVAATI: o, başkasını böler; bu, kendiliğinden bölünür. Bütün fark yedinci bâbdır ve metin onu kasten seçmiştir: taksîm, lafzın kendi tabiatındadır, müctehidin ona yaptığı bir şey değil."),
  tok("إِلَى","ila","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ — وَهُوَ مِنْ تَمَامِ الْفِعْلِ: «اِنْقَسَمَ» لَا يَسْتَغْنِي عَنْهُ.",
      "A jarr letter — and it belongs to the verb's meaning: اِنْقَسَمَ does not stand without it. A verb whose preposition is part of it is learned WITH the preposition, never apart from it.",
      "Cer harfi — fiilin mânâsının tamamındandır: «اِنْقَسَمَ» onsuz olmaz. Harf-i cerri mânâsının parçası olan fiil, harfiyle birlikte öğrenilir, ayrı değil."),
  tok("مُطْلَقٍ","mutlaq","noun",["huruf-jarr","ism-maful","form-iv-verbs"],
      "مَجْرُورٌ بِـ«إِلَى» — اسْمُ مَفْعُولٍ مِنْ «أَطْلَقَ» عَلَى مُفْعَلٍ، وَقَدْ مَرَّ مَصْدَرُهُ «الْإِطْلَاقُ» فِي بَابِ الْأَمْرِ.",
      "In jarr after «ila» — the ism maf'ul of أَطْلَقَ on مُفْعَل, whose masdar الْإِطْلَاق stood in the chapter on the command. The pair is worth holding together: there the word named a STATE a command could be in, here it names a wording that is in it.",
      "«إِلَى» ile mecrûr — «أَطْلَقَ»nin MUF'AL vezninde ism-i mef'ûlü; masdarı «الْإِطْلَاق» emir bâbında geçmişti. İkisini bir arada tut: orada kelime emrin bulunabileceği bir HÂLİ adlandırıyordu, burada o hâlde bulunan lafzı."),
  tok("وَمُقَيَّدٍ","muqayyad","noun",["atf-nasaq","ism-maful","form-ii-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ «قَيَّدَ» عَلَى مُفَعَّلٍ.",
      "Joined, in jarr — the ism maf'ul of قَيَّدَ on مُفَعَّل: the wording that has had a fetter put on it.",
      "Ma'tûf, mecrûr — «قَيَّدَ»nin MÜFA''AL vezninde ism-i mef'ûlü: kendisine kayıt vurulmuş lafız.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("مُقَيَّدٍ","muqayyad","noun")]),
 ],
 "jumal": [J("الْخَاصُّ يَنْقَسِمُ إِلَى مُطْلَقٍ وَمُقَيَّدٍ",
   "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause whose khabar is a verbal clause — i'rabless.",
   "Haberi fiil cümlesi olan isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the unrestricted is what takes in one instance, not one in particular.",
 "tr": "Mutlak, muayyen olmayan bir ferdi kapsayandır."},
 "tokens": [
  tok("فَالْمُطْلَقُ","mutlaq","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْمُطْلَقُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the unrestricted» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الْمُطْلَقُ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْمُطْلَقُ","mutlaq","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَهُوَ الْقَالَبُ الَّذِي بُنِيَتْ عَلَيْهِ حُدُودُ هَذَا الْكِتَابِ كُلُّهَا.",
      "A relative noun, fixed in form, in the position of raf' as the khabar — and it is the mould every definition in this book is cast in. A definite noun, a مَا, and a clause: read that shape once and the rest of the matn reads itself.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur — bu kitaptaki bütün tariflerin döküldüğü kalıptır. Marife bir isim, bir مَا ve bir cümle: bu şekli bir kere oku, metnin geri kalanı kendini okutur."),
  tok("تَنَاوَلَ","tanawala","verb",["fail","jumla-sifa","form-vi-verbs"],
      "فِعْلٌ مَاضٍ عَلَى «تَفَاعَلَ»، وَالْجُمْلَةُ صِلَةٌ — وَبَابُ التَّفَاعُلِ هُنَا لِلْأَخْذِ وَالشُّمُولِ لَا لِلْمُشَارَكَةِ.",
      "A past verb on تَفَاعَلَ; the clause is the sila. Form VI is the form of MUTUALITY as a rule — but not here: تَنَاوَلَ means to reach out and take in, and the pattern has drifted from its own headline meaning. A wazn tells you where to look for a sense, not what the sense is.",
      "«تَفَاعَلَ» vezninde mâzî fiil; cümle sıladır. Tefâul bâbı kural olarak MÜŞÂREKET içindir — burada değil: «تَنَاوَلَ» uzanıp kapsamak demektir; kalıp kendi başlık mânâsından kaymıştır. Vezin, mânâyı nerede arayacağını söyler; mânânın kendisini değil."),
  tok("وَاحِدًا","wahid","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "The maf'ul bihi, in nasb.",
      "Mansub mef'ûlün bih."),
  tok("لَا","la-nafiya","part",["atf-nasaq"],
      "«لَا» نَافِيَةٌ — وَهِيَ هُنَا مَعَ مَا بَعْدَهَا نَعْتٌ لِـ«وَاحِدًا».",
      "«La» denying, and with what follows it stands as a NA'T of «one instance» — an adjectival phrase built out of a negation.",
      "Nefy «لَا»sı — sonrasıyla birlikte «وَاحِدًا»ın na'tıdır: nefiyden kurulmuş bir sıfat ibaresi."),
  tok("بِعَيْنِهِ","ayn","noun",["huruf-jarr","idafa-definiteness","naat-sifa"],
      "جَارٌّ وَمَجْرُورٌ، وَ«عَيْنِ» مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْمَعْنَى: فَرْدٌ مِنَ الْجِنْسِ غَيْرُ مُعَيَّنٍ، فَأَيُّ رَقَبَةٍ أَجْزَأَتْ.",
      "A jarr-majrur, «the very self of» a mudaf and the HA its mudaf ilayh. The sense: ONE of the kind, but no one of them in particular — so any instance discharges the duty. «Free a slave» is unrestricted; any slave will do.",
      "Câr-mecrûr; «عَيْنِ» muzâf, HÂ muzâfun ileyhtir. Mânâ: cinsten bir fert, fakat hiçbiri muayyen değil — dolayısıyla hangisi olursa yeterlidir. «Bir köle âzâd et» mutlaktır; hangi köle olursa olsun.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("عَيْنِ","ayn","noun"), seg("هِ","pron-3ms","pron")]),
 ],
 "jumal": [J("الْمُطْلَقُ مَا تَنَاوَلَ وَاحِدًا",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the restricted is what takes in something described by a description over and above the bare reality.",
 "tr": "Mukayyed, aslî hakikatin üzerine bir vasıfla vasıflanmış olanı kapsayandır."},
 "tokens": [
  tok("وَالْمُقَيَّدُ","muqayyad","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُقَيَّدُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the restricted» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُقَيَّدُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُقَيَّدُ","muqayyad","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("تَنَاوَلَ","tanawala","verb",["fail","jumla-sifa","form-vi-verbs"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — وَأُعِيدَ بِعَيْنِهِ، فَالْفَرْقُ بَيْنَ الْحَدَّيْنِ فِي الْمَفْعُولِ لَا فِي الْفِعْلِ.",
      "A past verb; the clause is the sila. The verb is repeated word for word, so the difference between the two definitions lies wholly in the OBJECT: there وَاحِدًا, here مَوْصُوفًا.",
      "Mâzî fiil; cümle sıladır. Fiil aynen tekrarlanmıştır; iki tarif arasındaki fark tamamen MEF'ÛLdedir: orada «وَاحِدًا», burada «مَوْصُوفًا»."),
  tok("مَوْصُوفًا","mawsuf","noun",["maful-bihi","ism-maful"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ «وَصَفَ»، وَهُوَ مِثَالٌ وَاوِيٌّ بَقِيَتْ وَاوُهُ فِي اسْمِ الْمَفْعُولِ لِسُكُونِ مَا قَبْلَهَا.",
      "The maf'ul bihi in nasb — the ism maf'ul of وَصَفَ. The verb is a MITHAL, and its waw drops in the mudari (يَصِفُ); in the participle it stands, because there is no kasra behind it to push it out. The same letter, present in one cell and gone from another, and the reason is entirely local.",
      "Mansub mef'ûlün bih — «وَصَفَ»nin ism-i mef'ûlü. Fiil MİSÂLdir ve vâvı muzâride düşer (يَصِفُ); ism-i mef'ûlde ise durur, zira arkasında onu iten bir kesra yoktur. Aynı harf, bir hânede var bir hânede yok; sebep tamamen yerel."),
  tok("بِوَصْفٍ","wasf","noun",["huruf-jarr","masdar"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«مَوْصُوفًا» — مَصْدَرُ «وَصَفَ»، وَاسْمُ الْمَفْعُولِ عَامِلٌ فَتَعَلَّقَ بِهِ.",
      "A jarr-majrur attaching to «described» — the masdar of وَصَفَ. A participle governs like its verb, which is why the phrase hangs on it rather than on anything further back.",
      "«مَوْصُوفًا»a taalluk eden câr-mecrûr — «وَصَفَ»nin masdarı. İsm-i mef'ûl fiili gibi amel eder; ibarenin daha geriye değil ona asılmasının sebebi budur.",
      segments=[seg("بِ","bi","prep"), seg("وَصْفٍ","wasf","noun")]),
  tok("زَائِدٍ","zaid","noun",["naat-sifa","ism-fail","hollow-verbs"],
      "نَعْتٌ لِـ«وَصْفٍ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «زَادَ»، وَهُوَ أَجْوَفُ يَائِيٌّ: قُلِبَتْ عَيْنُهُ هَمْزَةً فِي اسْمِ الْفَاعِلِ، «زَايِد» ← «زَائِد»، كَـ«قَائِل» وَ«بَائِع».",
      "A na't of «a description», in jarr — the ism fa'il of زَادَ, an AJWAF YAI. Its middle radical turns into a HAMZA in the participle: زَايِد becomes زَائِد, exactly as قَالَ gives قَائِل and بَاعَ gives بَائِع. This is the third face of ز ي د in this package — اِزْدَادَ carried the ibdal of the ta, and here the same root shows the i'lal of the ayn.",
      "«وَصْفٍ»in na'tı, mecrûr — «زَادَ»nin ism-i fâili; ECVEF-İ YÂÎdir. Ayn harfi ism-i fâilde HEMZEye kalbolur: «زَايِد» iken «زَائِد» olur — قَالَ'dan قَائِل, بَاعَ'dan بَائِع gibi. Bu, pakette ز ي د kökünün üçüncü yüzüdür: «اِزْدَادَ» tânın ibdâlini taşıyordu, burada aynı kök aynın i'lâlini gösteriyor."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«زَائِدٍ».",
      "A jarr letter attaching to «over and above».",
      "«زَائِدٍ»e taalluk eden cer harfi."),
  tok("أَصْلِ","asl","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ — وَ«الْأَصْلُ» هُوَ الْكَلِمَةُ الَّتِي فُتِحَ بِهَا الْكِتَابُ.",
      "In jarr after «ala» and a mudaf — and «asl» is the very word the book opened with, in chapter 1. Nine chapters later it is still doing work.",
      "«عَلَى» ile mecrûr ve muzâf — «الْأَصْل», kitabın birinci bâbda açıldığı kelimenin kendisidir. Dokuz bâb sonra hâlâ iş görüyor."),
  tok("الْحَقِيقَةِ","haqiqa","noun",["idafa-definiteness","haqiqa-majaz"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالْحَقِيقَةُ مَا اسْتُعْمِلَ فِيمَا وُضِعَ لَهُ، وَالْمُرَادُ هُنَا الْمَاهِيَّةُ الْمُجَرَّدَةُ قَبْلَ كُلِّ وَصْفٍ.",
      "The mudaf ilayh in jarr — and haqiqa is a wording used for what it was set down for. Here what is meant is the bare NATURE of the thing before any description is added: «a slave» is the reality, «a believing slave» is the reality plus a fetter.",
      "Mecrûr muzâfun ileyh — hakikat, vaz' edildiği mânâda kullanılan lafızdır. Burada kastedilen, her vasıftan önceki çıplak MÂHİYETtir: «köle» hakikattir, «mümin köle» hakikat artı bir kayıttır.",
      punct="."),
 ],
 "jumal": [J("الْمُقَيَّدُ مَا تَنَاوَلَ مَوْصُوفًا بِوَصْفٍ زَائِدٍ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And the unrestricted is not carried onto the restricted with us, except by an indication.",
 "tr": "Bize göre mutlak, bir delil olmadıkça mukayyede hamledilmez."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["atf-nasaq","mudari-marfu"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "A joining waw, and «la» simply denying, governing nothing.",
      "Atıf vâvı; «لَا» amel etmeyen nefy harfidir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُحْمَلُ","hamala","verb",["naib-al-fail","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — مِنْ «ح م ل»، وَهُوَ الْجَذْرُ الَّذِي جَاءَ مِنْهُ «يَحْتَمِلُ» فِي بَابِ الْمُحْكَمِ عَلَى افْتِعَالٍ.",
      "A mudari built for the unnamed doer, in raf' — from ح م ل, the root that gave يَحْتَمِلُ on اِفْتِعَال in the chapter on the muhkam. Two babs of one root in one book, and the nakil drill will now show both.",
      "Meçhûl sîgasında merfû muzâri — «ح م ل» kökünden; muhkem bâbındaki «يَحْتَمِلُ» de İFTİÂL vezninde aynı köktendi. Bir kitapta tek kökün iki bâbı; nakil cetveli artık ikisini de gösterir."),
  tok("الْمُطْلَقُ","mutlaq","noun",["naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "The naib al-fa'il, in raf'.", "Merfû nâib-i fâil."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يُحْمَلُ» — وَهُوَ مِنْ تَمَامِ مَعْنَاهُ: الْحَمْلُ يَكُونُ «عَلَى» شَيْءٍ.",
      "A jarr letter attaching to «is carried» — and part of its meaning: a thing is carried ONTO something.",
      "«يُحْمَلُ»a taalluk eden cer harfi — mânâsının tamamındandır: hamil, bir şeyin «üzerine» olur."),
  tok("الْمُقَيَّدِ","muqayyad","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى».", "In jarr after «ala».", "«عَلَى» ile mecrûr."),
  tok("عِنْدَنَا","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ — وَهِيَ الْكَلِمَةُ الَّتِي يُعْلِنُ بِهَا الْمَتْنُ مَذْهَبَهُ: هَذَا قَوْلُ الْحَنَفِيَّةِ، وَغَيْرُهُمْ عَلَى خِلَافِهِ.",
      "An adverb in nasb and a mudaf, with «na» as its mudaf ilayh — and this is the word by which the matn declares WHOSE position it is stating. «With us» means the Hanafis; others hold otherwise, and the matn does not pretend the question is settled for everyone.",
      "Mansub zarf ve muzâf; «نَا» muzâfun ileyhtir — metnin hangi mezhebi söylediğini ilân ettiği kelimedir. «Bize göre» Hanefîler demektir; başkaları aksini söyler ve metin, meselenin herkesçe kapandığını iddia etmez.",
      segments=[seg("عِنْدَ","inda","noun"), seg("نَا","pron-1p","pron")]),
  tok("إِلَّا","illa","part",["istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ، وَالِاسْتِثْنَاءُ مُفَرَّغٌ — وَهَذَا الثَّالِثُ فِي أَرْبَعَةِ أَبْوَابٍ.",
      "The particle of exception, the exception MUFARRAGH — the third in four chapters. By now the shape should be recognised before the words are read: a negation, an إِلَّا, and no mustathna minhu named.",
      "İstisnâ edatı; istisnâ MÜFERRAĞdır — dört bâbda üçüncüsü. Artık şekil, kelimeler okunmadan tanınmalıdır: bir nefy, bir «إِلَّا» ve zikredilmemiş bir müstesnâ minh."),
  tok("بِدَلِيلٍ","dalil","noun",["istithna-mufarragh","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يُحْمَلُ» — وَهُوَ الْمُسْتَثْنَى الْمُفَرَّغُ، وَ«دَلِيلٌ» هُوَ الْكَلِمَةُ الَّتِي جُمِعَتْ فِي أَوَّلِ الْكِتَابِ: الْأَدِلَّةُ أَرْبَعَةٌ.",
      "A jarr-majrur attaching to «is carried» — the emptied exception itself. And «dalil» is the word chapter 2 pluralised in its opening line: الْأَدِلَّةُ أَرْبَعَةٌ. The book has come round to its own first term.",
      "«يُحْمَلُ»a taalluk eden câr-mecrûr — müferrağ müstesnânın kendisi. «دَلِيل», ikinci bâbın açılış satırında cemilenen kelimedir: الْأَدِلَّةُ أَرْبَعَةٌ. Kitap kendi ilk ıstılahına dönmüştür.",
      punct=".", segments=[seg("بِ","bi","prep"), seg("دَلِيلٍ","dalil","noun")]),
 ],
 "jumal": [J("لَا يُحْمَلُ الْمُطْلَقُ عَلَى الْمُقَيَّدِ إِلَّا بِدَلِيلٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "So when the indication is established, the unrestricted is carried onto the restricted.",
 "tr": "Delil sâbit olduğunda mutlak, mukayyede hamledilir."},
 "tokens": [
  tok("فَإِذَا","idha","part",["idha-shartiyya"],
      "الْفَاءُ فَصِيحَةٌ، وَ«إِذَا» ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ، مُضَمَّنٌ مَعْنَى الشَّرْطِ.",
      "A «telling» fa, and «idha» an adverb of TIME TO COME carrying the sense of a condition — it is not a pure particle but a zarf with a condition folded into it, which is why the books put it apart from إِنْ.",
      "Fasîha fâsı; «إِذَا» gelecek zaman zarfı olup şart mânâsını tazammun eder — sırf harf değil, içine şart katılmış bir zarftır; kitapların onu «إِنْ»den ayrı tutmasının sebebi budur.",
      segments=[seg("فَ","fa","conj"), seg("إِذَا","idha","part")]),
  tok("ثَبَتَ","thabata","verb",["fail","idha-shartiyya"],
      "فِعْلٌ مَاضٍ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهِ، وَهُوَ فِعْلُ الشَّرْطِ — وَ«إِذَا» تُضَافُ إِلَى جُمْلَتِهَا كَمَا أُضِيفَتْ «حَيْثُ» فِي بَابِ الْمُفَسَّرِ.",
      "A past verb, in the position of JARR because «idha» is added to it — it is the condition-verb. «Idha» takes its clause for a mudaf ilayh exactly as حَيْثُ did in the chapter on the mufassar. Two words in one book that are added to whole sentences.",
      "Mâzî fiil; «إِذَا» ona muzâf olduğu için mahallen mecrûrdur ve şartın fiilidir. «إِذَا» cümlesine muzâf olur — müfesser bâbındaki «حَيْثُ» gibi. Bir kitapta cümleye muzâf olan iki kelime."),
  tok("الدَّلِيلُ","dalil","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.", "The fa'il, in raf'.", "Merfû fâil."),
  tok("حُمِلَ","hamala","verb",["naib-al-fail","idha-shartiyya"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ جَوَابُ «إِذَا» لَا مَحَلَّ لَهَا — وَجَوَابُ «إِذَا» لَا يَقْتَرِنُ بِالْفَاءِ إِذَا كَانَ فِعْلًا مَاضِيًا.",
      "A past verb built for the unnamed doer, and the clause is «idha»'s ANSWER — i'rabless. Note that no fa joins it: the answer of a condition takes a fa only when it could not otherwise stand as an answer, and a plain past verb can.",
      "Meçhûl sîgasında mâzî fiil; cümle «إِذَا»nın CEVÂBIdır ve mahalsizdir. Başına fâ gelmediğine dikkat: şartın cevâbı, ancak kendi başına cevap olamayacağı hâllerde fâ alır; sade mâzî fiil olabilir."),
  tok("الْمُطْلَقُ","mutlaq","noun",["naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "The naib al-fa'il, in raf'.", "Merfû nâib-i fâil."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«حُمِلَ».",
      "A jarr letter attaching to «is carried».",
      "«حُمِلَ»ye taalluk eden cer harfi."),
  tok("الْمُقَيَّدِ","muqayyad","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» — وَبِهِ خُتِمَ الْبَابُ عَلَى مَا فُتِحَ بِهِ: قِسْمَانِ، ثُمَّ الْحُكْمُ فِي لِقَائِهِمَا.",
      "In jarr after «ala» — and the chapter closes on what it opened with: two kinds, and then the ruling for what happens when they meet.",
      "«عَلَى» ile mecrûr — bâb, açıldığı şeyle kapanır: iki kısım, sonra karşılaştıklarında geçerli hüküm.",
      punct="."),
 ],
 "jumal": [J("إِذَا ثَبَتَ الدَّلِيلُ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ لِـ«إِذَا».",
   "A verbal clause in the position of jarr, the mudaf ilayh of «idha».",
   "«إِذَا»nın muzâfun ileyhi olarak mahallen mecrûr fiil cümlesi."),
  J("حُمِلَ الْمُطْلَقُ عَلَى الْمُقَيَّدِ",
   "جُمْلَةٌ فِعْلِيَّةٌ جَوَابُ الشَّرْطِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the answer of the condition — i'rabless.",
   "Şartın cevâbı olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "mutlaq":    g("مُطْلَق", "ط ل ق", "noun", "the UNRESTRICTED — takes in one instance, no one in particular", "mutlak — muayyen olmayan bir ferdi kapsayan", 4),
 "muqayyad":  g("مُقَيَّد", "ق ي د", "noun", "the RESTRICTED — takes in what carries an added description", "mukayyed — fazla bir vasıf taşıyanı kapsayan", 4),
 "inqasama":  g("اِنْقَسَمَ", "ق س م", "verb", "to divide into, to fall into kinds", "ayrılmak, kısımlara bölünmek", 3),
 "tanawala":  g("تَنَاوَلَ", "ن و ل", "verb", "to reach out and take in, to cover", "kapsamak, şümûlüne almak", 4),
 "ayn":       g("عَيْن", "ع ي ن", "noun", "the very self of a thing; an eye", "ayn; bir şeyin kendisi", 2, plural="أَعْيَان"),
 "mawsuf":    g("مَوْصُوف", "و ص ف", "noun", "described, qualified (ism maf'ul)", "mevsûf; vasıflanmış", 3),
 "wasf":      g("وَصْف", "و ص ف", "noun", "a description, a quality (masdar)", "vasıf (masdar)", 3, plural="أَوْصَاف"),
 "zaid":      g("زَائِد", "ز ي د", "noun", "added, over and above (ism fa'il)", "zâid; fazladan olan", 3),
 "haqiqa":    g("حَقِيقَة", "ح ق ق", "noun", "the reality — a wording used for what it was set down for", "hakikat — vaz' edildiği mânâda kullanılan", 4),
 "hamala":    g("حَمَلَ", "ح م ل", "verb", "to carry; to construe one wording by another", "yüklemek; bir lafzı ötekine hamletmek", 3),
 "dalil":     g("دَلِيل", "د ل ل", "noun", "an indication, a proof", "delil", 2, plural="أَدِلَّة"),
 "idha":      g("إِذَا", None, "part", "when (an adverb of time to come, with a condition folded in)", "…-dığı zaman (şart mânâlı gelecek zaman zarfı)", 2),
}

def build_morph():
    out = {}
    # اِنْقَسَمَ — Form VII, sound.
    out["inqasama"] = _sg.derived("بَابُ الِانْفِعَالِ: اِنْفَعَلَ يَنْفَعِلُ", "اِنْفَعَلَ يَنْفَعِلُ", "َ",
                                  "اِنْقَسَم", "نْقَسِم", "اِنْقَسِم", "اِنْقِسَام", "مُنْقَسِم",
                                  note="مُطَاوِعُ «قَسَمَ» — وَالِانْفِعَالُ بَابُ الْمُطَاوَعَةِ.")
    # تَنَاوَلَ — Form VI. The middle radical is a waw but Form VI keeps it sound:
    # the alif of تَفَاعَلَ stands before it, so nothing pushes it out.
    out["tanawala"] = _sg.derived("بَابُ التَّفَاعُلِ: تَفَاعَلَ يَتَفَاعَلُ", "تَفَاعَلَ يَتَفَاعَلُ", "َ",
                                  "تَنَاوَل", "تَنَاوَل", "تَنَاوَل", "تَنَاوُل", "مُتَنَاوِل",
                                  maful="مُتَنَاوَل",
                                  note="بَقِيَتِ الْوَاوُ صَحِيحَةً لِسُكُونِ مَا قَبْلَهَا أَلِفًا.")
    # حَمَلَ — sound, bab daraba. The passive is the chapter's own lesson.
    out["hamala"] = _sg.sound1("daraba", "حَمَل", "حْمِل", "اِحْمِل", "حَمْل", "حَامِل",
                               maful="مَحْمُول", pmz="حُمِلَ", pmd="يُحْمَلُ",
                               note="مِنْ بَابِ ضَرَبَ — وَمِنْ جَذْرِهِ «اِحْتَمَلَ» عَلَى افْتِعَالٍ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/9.json").write_text(
    json.dumps({"chapter": 9, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 9 for c in man["chapters"]):
    man["chapters"].append({"n": 9, "title": TITLE9})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.9.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch9:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
