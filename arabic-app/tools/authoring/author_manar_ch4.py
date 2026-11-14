# -*- coding: utf-8 -*-
"""Author chapter 4 of mukhtasar-al-manar — the four divisions of the LAFZ.

With the four sources named and defined, the matn turns to the first of them,
the Book, and asks the question the whole science turns on: what KINDS of
wording does a text contain, and what does each kind oblige? The Hanafi answer
is the fourfold division by wadʿ — khass, ʿamm, mushtarak, muʾawwal — and this
chapter sets it out with the definition of each.

ATTRIBUTION: like chapters 2–3, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn;
nothing in this chapter is original.

Grammar this chapter is chosen to teach, and it is the richest chapter in the
package by a distance:

  • أَرْبَعَةُ أَقْسَامٍ — the number from three to ten is a MUDAF and what it
    counts is a PLURAL MAJRUR. Chapter 2 showed the same numeral as a khabar
    (الْأَدِلَّةُ أَرْبَعَةٌ); here it governs. Same word, two offices.
  • لِمَعْنًى beside لِمَعَانٍ — the MAQSUR and the MANQUS in one chapter, one in
    the singular and one in its own plural. And مَعَانٍ is the hard case: a
    مُنْتَهَى الْجُمُوعِ, so barred from tanwin, yet written with one, because a
    manqus drops its ya in raf' and jarr and a tanwin of COMPENSATION takes the
    dropped letter's place.
  • وُضِعَ — the majhul of a MITHAL verb. The waw that fell out of يَضَعُ comes
    back in يُوضَعُ, which is the cleanest proof available that the drop was
    caused by the kasra and not by the waw being weak.
  • أَنْ يُوجِبَ — أَنْ الْمَصْدَرِيَّةُ and the mudari in nasb, the whole making a
    masdar muawwal that serves as a khabar.
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

TITLE4 = {"ar": "أَقْسَامُ اللَّفْظِ", "en": "The Divisions of the Wording",
          "tr": "Lafzın Kısımları"}

S.append({"id": "s1", "translation": {
 "en": "Then the wording is of four kinds: the specific, the general, the shared and the interpreted.",
 "tr": "Lafız dört kısımdır: hâss, âmm, müşterek ve müevvel."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ مَعَ التَّرَاخِي — انْتَقَلَ بِهِ مِنْ ذِكْرِ الْأَدِلَّةِ إِلَى تَقْسِيمِ أَلْفَاظِ أَوَّلِهَا.",
      "A letter of atf giving sequence with an interval — with it the matn steps from naming the sources to dividing the wording of the first of them.",
      "Terâhî ile tertîb bildiren atıf harfi — metin onunla delilleri saymaktan, birincisinin lafızlarını taksîme geçer."),
  tok("اللَّفْظُ","lafz","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ — وَالْمُرَادُ بِهِ اللَّفْظُ الْمَوْضُوعُ لِمَعْنًى، لَا مُطْلَقُ الصَّوْتِ.",
      "The mubtada in raf' by the damma — and what is meant is the wording SET DOWN for a meaning, not mere sound.",
      "Damme ile merfû mübtedâ — kastedilen, bir mânâ için vaz' edilmiş lafızdır; mutlak ses değil."),
  tok("أَرْبَعَةُ","arbaa","noun",["mubtada-khabar","idafa-definiteness","tamyiz"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَالْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى مَعْدُودِهِ، وَلَحِقَتْهُ التَّاءُ لِأَنَّ مَعْدُودَهُ مُذَكَّرٌ.",
      "The khabar in raf', and a MUDAF — from three to ten the number is joined to what it counts by an IDAFA, not by a mansub tamyiz. Note the contrast with chapter 2: there أَرْبَعَةٌ stood alone as a khabar and wore a tanwin; here it governs a noun and loses it. Same word, two offices.",
      "Merfû haber ve MUZÂF — üçten ona kadar sayı, ma'dûduna mansub temyîzle değil İZÂFETLE bağlanır. İkinci bölümle karşılaştır: orada أَرْبَعَةٌ tek başına haberdi ve tenvîn taşıyordu; burada bir isme muzâf olup tenvînini kaybetti. Aynı kelime, iki ayrı vazife."),
  tok("أَقْسَامٍ","aqsam","noun",["idafa-definiteness","tamyiz"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «قِسْمٍ»، وَهُوَ الْمُمَيِّزُ فِي الْمَعْنَى: مَيَّزَ الْعَدَدَ الْمُبْهَمَ.",
      "The mudaf ilayh in jarr — the plural of «qism», and in meaning the DISTINGUISHER: it says what the bare number is a number OF.",
      "Mecrûr muzâfun ileyh — «قِسْم»in cemidir ve mânâ cihetinden mümeyyizdir: mübhem sayının neyin sayısı olduğunu ayırır.", punct="："),
  tok("خَاصٌّ","khass","noun",["badal"],
      "بَدَلٌ مِنْ «أَرْبَعَةُ» مَرْفُوعٌ — بَدَلُ تَفْصِيلٍ. وَهُوَ اسْمُ فَاعِلٍ مِنْ «خَصَّ» أُدْغِمَ مِثْلَاهُ.",
      "A badal of «four», in raf' — a badal of DETAIL. It is the ism fa'il of خَصَّ, its two identical letters run together.",
      "«أَرْبَعَةُ»den merfû bedel — tafsîl bedeli. «خَصَّ»nin ism-i fâilidir, iki misli idgâm edilmiştir."),
  tok("وَعَامٌّ","amm","noun",["atf-nasaq","doubled-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «عَمَّ»، وَأَصْلُهُ «عَامِمٌ» فَأُدْغِمَ.",
      "Joined, in raf' — the ism fa'il of عَمَّ; its origin is عَامِمٌ, and the two mims were run together.",
      "Ma'tûf, merfû — «عَمَّ»nin ism-i fâili; aslı «عَامِمٌ»dur, iki mîm idgâm edilmiştir.",
      segments=[seg("وَ","wa","conj"), seg("عَامٌّ","amm","noun")]),
  tok("وَمُشْتَرَكٌ","mushtarak","noun",["atf-nasaq","ism-maful","form-viii-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «اِشْتَرَكَ» عَلَى مُفْتَعَلٍ.",
      "Joined, in raf' — the ism maf'ul of اِشْتَرَكَ on مُفْتَعَل.",
      "Ma'tûf, merfû — «اِشْتَرَكَ»nin MÜFTEAL vezninde ism-i mef'ûlü.",
      segments=[seg("وَ","wa","conj"), seg("مُشْتَرَكٌ","mushtarak","noun")]),
  tok("وَمُؤَوَّلٌ","muawwal","noun",["atf-nasaq","ism-maful","form-ii-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «أَوَّلَ» عَلَى مُفَعَّلٍ، وَبِهِ تَمَّتِ الْأَقْسَامُ أَرْبَعَةً.",
      "Joined, in raf' — the ism maf'ul of أَوَّلَ on مُفَعَّل, and with it the four kinds are complete.",
      "Ma'tûf, merfû — «أَوَّلَ»nin MÜFA''AL vezninde ism-i mef'ûlü; kısımlar bununla dörde tamamlanır.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("مُؤَوَّلٌ","muawwal","noun")]),
 ],
 "jumal": [J("اللَّفْظُ أَرْبَعَةُ أَقْسَامٍ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "The specific is what was set down for a single meaning, on its own.",
 "tr": "Hâss, tek bir mânâ için tek başına vaz' edilmiş olandır."},
 "tokens": [
  tok("فَالْخَاصُّ","khass","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ فَصِيحَةٌ أَوْ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْخَاصُّ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A «telling» fa, or one joining for detail, and «the specific» is the mubtada in raf'.",
      "Fasîha yahut tafsîl için âtıfa olan fâ; «الْخَاصُّ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْخَاصُّ","khass","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("وُضِعَ","wadaa","verb",["naib-al-fail","mithal-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ لَا مَحَلَّ لَهَا. وَهُوَ مِثَالٌ وَاوِيٌّ: سَقَطَتْ وَاوُهُ فِي «يَضَعُ» لِوُقُوعِهَا بَيْنَ يَاءٍ وَكَسْرَةٍ فِي الْأَصْلِ، وَعَادَتْ فِي الْمَجْهُولِ «يُوضَعُ».",
      "A past verb built for the UNNAMED DOER; the naib al-fa'il is a hidden pronoun going back to «what», and the clause is the sila — i'rabless. It is a MITHAL WAWI: its waw fell out of يَضَعُ, and it comes BACK in the passive يُوضَعُ. That return is the cleanest proof available that the waw was dropped by its surroundings, not because a waw is weak in itself.",
      "Meçhûl sîgasında mâzî fiil; nâib-i fâil «مَا»ya râci müstetir zamîrdir, cümle de sıladır ve mahalsizdir. Bu bir MİSÂL-İ VÂVÎdir: vâvı «يَضَعُ»de düşmüş, meçhûl «يُوضَعُ»de GERİ DÖNMÜŞTÜR. Bu dönüş, vâvın kendisi zayıf olduğu için değil çevresi sebebiyle düştüğünün en açık delilidir."),
  tok("لِمَعْنًى","mana","noun",["huruf-jarr","ism-maqsur-manqus"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«وُضِعَ» — وَ«مَعْنًى» اسْمٌ مَقْصُورٌ، جُرَّ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَتَنْوِينُهُ مَكْتُوبٌ عَلَى الْأَلِفِ نَفْسِهَا.",
      "A jarr-majrur attaching to «was set down» — and «a meaning» is a MAQSUR noun: its jarr is a kasra that cannot be written, so it is UNDERSTOOD, and the tanwin sits on the alif itself.",
      "«وُضِعَ»ye taalluk eden câr-mecrûr — «مَعْنًى» MAKSÛR isimdir; ceri elif üzerinde takdîrî kesradır ve tenvîni elifin üstüne yazılır.",
      segments=[seg("لِ","li","prep"), seg("مَعْنًى","mana","noun")]),
  tok("وَاحِدٍ","wahid","noun",["naat-sifa"],
      "نَعْتٌ لِـ«مَعْنًى» مَجْرُورٌ بِالْكَسْرَةِ — وَظَهَرَتْ عَلَيْهِ لِأَنَّهُ صَحِيحُ الْآخِرِ، بِخِلَافِ مَنْعُوتِهِ.",
      "A na't of «a meaning», in jarr by the kasra — and the kasra SHOWS on it, because it ends in a sound letter, unlike the word it describes. The pair is worth staring at: the same case, written on one and understood on the other.",
      "«مَعْنًى»in na'tı, kesra ile mecrûr — sahîhu'l-âhir olduğu için kesra ZÂHİRdir; men'ûtunun aksine. Çifte dikkat et: aynı i'râb, birinde yazılı, ötekinde takdîrî."),
  tok("عَلَى","ala","prep",["huruf-jarr","hal"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنَ الضَّمِيرِ فِي «وُضِعَ».",
      "A jarr letter; the phrase is a HAL from the pronoun inside «was set down».",
      "Cer harfi; câr-mecrûr «وُضِعَ»deki zamîrden hâldir."),
  tok("الِانْفِرَادِ","infirad","noun",["huruf-jarr","masdar","form-vii-verbs"],
      "مَجْرُورٌ بِـ«عَلَى» — مَصْدَرُ «اِنْفَرَدَ» عَلَى اِنْفِعَالٍ، وَبِهِ خَرَجَ الْمُشْتَرَكُ: فَإِنَّهُ مَوْضُوعٌ لِمَعَانٍ لَا لِمَعْنًى وَاحِدٍ عَلَى حِدَةٍ.",
      "In jarr after «ala» — the masdar of اِنْفَرَدَ on اِنْفِعَال, and by it the SHARED word is shut out: it is set down for meanings, not for one meaning standing alone.",
      "«عَلَى» ile mecrûr — «اِنْفَرَدَ»nin İNFİÂL vezninde masdarı; onunla müşterek dışarıda kalır: o, tek başına bir mânâ için değil, birçok mânâ için vaz' edilmiştir.",
      punct="."),
 ],
 "jumal": [J("الْخَاصُّ مَا وُضِعَ لِمَعْنًى وَاحِدٍ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("وُضِعَ لِمَعْنًى وَاحِدٍ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And its ruling is that it obliges the judgement decisively.",
 "tr": "Hükmü, hükmü kat'î olarak îcâb etmesidir."},
 "tokens": [
  tok("وَحُكْمُهُ","hukm","noun",["atf-nasaq","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَ«حُكْمُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ فِي مَحَلِّ جَرٍّ.",
      "A joining waw; «ruling» is the mubtada in raf' and a mudaf, and the HA is the mudaf ilayh, in the position of jarr.",
      "Atıf vâvı; «حُكْمُ» merfû mübtedâ ve muzâf, HÂ ise mahallen mecrûr muzâfun ileyhtir.",
      segments=[seg("وَ","wa","conj"), seg("حُكْمُ","hukm","noun"), seg("هُ","pron-3ms","pron")]),
  tok("أَنْ","an-nasiba","part",["an-masdariyya","mudari-marfu"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — يَسْبِكُ مَا بَعْدَهُ مَصْدَرًا، وَيَنْصِبُ الْمُضَارِعَ.",
      "A MASDAR-MAKING letter that puts the mudari into nasb — it melts the clause after it down into a masdar.",
      "Masdariyye ve nâsıbe harfi — sonrasını masdara döker ve muzârii nasb eder."),
  tok("يُوجِبَ","awjaba","verb",["an-masdariyya","form-iv-verbs","mithal-verbs"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «الْخَاصِّ» — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرُ «حُكْمُهُ».",
      "A mudari in nasb after «an», its mark the fatha, with a hidden pronoun going back to «the specific» for its fa'il — and the MASDAR MUAWWAL («its obliging») is the khabar of «its ruling».",
      "«أَنْ» ile mansub muzâri; nasb alâmeti fethadır, fâili «الْخَاصِّ»a râci müstetir zamîrdir — masdar-ı müevvel («îcâb etmesi») «حُكْمُهُ»nün haberidir."),
  tok("الْحُكْمَ","hukm","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.",
      "The maf'ul bihi, in nasb by the fatha.",
      "Fetha ile mansub mef'ûlün bih."),
  tok("قَطْعًا","qat","noun",["maful-mutlaq","masdar","hal"],
      "مَفْعُولٌ مُطْلَقٌ مُبَيِّنٌ لِلنَّوْعِ مَنْصُوبٌ، وَقِيلَ حَالٌ بِمَعْنَى «قَاطِعًا» — وَالْمَعْنَى وَاحِدٌ: لَا احْتِمَالَ فِيهِ.",
      "A MAF'UL MUTLAQ in nasb, telling the KIND of the obliging; some read it instead as a hal, «cutting off doubt». The two readings meet in one sense: there is no other possibility left open. This is the whole point of the khass — it does not admit an alternative.",
      "Nev'i beyân eden mansub MEF'ÛL-Ü MUTLAK; bir görüşe göre «kesin olarak» mânâsında hâldir — mânâ birdir: başka ihtimal bırakmaz. Hâssın bütün mühim tarafı budur: başka bir ihtimale yer vermez.",
      punct="."),
 ],
 "jumal": [J("حُكْمُهُ أَنْ يُوجِبَ الْحُكْمَ",
   "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا مَصْدَرٌ مُؤَوَّلٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause whose khabar is a masdar muawwal — i'rabless.",
   "Haberi masdar-ı müevvel olan isim cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And the general is a wording that takes in everything it is fit for.",
 "tr": "Âmm, kendisine elverişli olan her şeyi kuşatan lafızdır."},
 "tokens": [
  tok("وَالْعَامُّ","amm","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْعَامُّ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the general» is the mubtada in raf'.",
      "Atıf vâvı; «الْعَامُّ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْعَامُّ","amm","noun")]),
  tok("لَفْظٌ","lafz","noun",["mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَجَاءَ نَكِرَةً لِأَنَّ الْمَقْصُودَ الْجِنْسُ لَا لَفْظٌ بِعَيْنِهِ.",
      "The khabar in raf', with a tanwin — and it comes INDEFINITE because what is meant is the kind, not one particular word.",
      "Tenvînli merfû haber — maksûd cins olduğu için nekre gelmiştir, muayyen bir lafız değil."),
  tok("مُسْتَغْرِقٌ","mustaghriq","noun",["naat-sifa","ism-fail","form-x-verbs"],
      "نَعْتٌ لِـ«لَفْظٌ» مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «اِسْتَغْرَقَ» عَلَى مُسْتَفْعِلٍ، وَهُوَ عَامِلٌ عَمَلَ فِعْلِهِ فَتَعَلَّقَ بِهِ الْجَارُّ بَعْدَهُ.",
      "A na't of «a wording», in raf' — the ism fa'il of اِسْتَغْرَقَ on مُسْتَفْعِل, and it GOVERNS like its verb, which is why the jarr after it attaches to it.",
      "«لَفْظٌ»un na'tı, merfû — «اِسْتَغْرَقَ»nin MÜSTEF'İL vezninde ism-i fâili; fiili gibi amel eder, bu yüzden sonraki câr ona taalluk eder."),
  tok("لِجَمِيعِ","jami","noun",["huruf-jarr","idafa-definiteness"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«مُسْتَغْرِقٌ»، وَ«جَمِيعِ» مُضَافٌ.",
      "A jarr-majrur attaching to «taking in», and «all of» is a mudaf.",
      "«مُسْتَغْرِقٌ»a taalluk eden câr-mecrûr; «جَمِيعِ» muzâftır.",
      segments=[seg("لِ","li","prep"), seg("جَمِيعِ","jami","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "A relative noun, fixed in form, in the position of jarr as the mudaf ilayh.",
      "Mebnî ism-i mevsûl; muzâfun ileyh olarak mahallen mecrûrdur."),
  tok("يَصْلُحُ","salaha-mujarrad","verb",["mudari-marfu","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ، لَا مَحَلَّ لَهَا.",
      "A mudari in raf' by the damma, with a hidden pronoun for its fa'il — and the clause is the sila of the relative, i'rabless.",
      "Damme ile merfû muzâri, fâili müstetir zamîr — cümle ism-i mevsûlün sılasıdır, mahalsizdir."),
  tok("لَهُ","li","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَصْلُحُ» — وَعَلَيْهِ مَدَارُ الْحَدِّ: مَا لَا يَصْلُحُ لَهُ اللَّفْظُ لَا يَدْخُلُ تَحْتَهُ.",
      "A jarr-majrur attaching to «is fit» — and the whole definition turns on it: what the wording is NOT fit for does not fall under it.",
      "«يَصْلُحُ»a taalluk eden câr-mecrûr — tarifin medârı odur: lafzın elverişli olmadığı şey onun altına girmez.",
      punct=".", segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
 ],
 "jumal": [J("الْعَامُّ لَفْظٌ مُسْتَغْرِقٌ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the shared is what was set down for differing meanings.",
 "tr": "Müşterek, birbirinden farklı mânâlar için vaz' edilmiş olandır."},
 "tokens": [
  tok("وَالْمُشْتَرَكُ","mushtarak","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُشْتَرَكُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the shared» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُشْتَرَكُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُشْتَرَكُ","mushtarak","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("وُضِعَ","wadaa","verb",["naib-al-fail","mithal-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْجُمْلَةُ صِلَةٌ — وَتَكْرَارُ اللَّفْظِ مَعَ تَغْيِيرِ الْمُتَعَلَّقِ هُوَ مَوْضِعُ الْفَرْقِ بَيْنَ الْحَدَّيْنِ.",
      "A past verb built for the unnamed doer; the clause is the sila. The definition repeats word for word what was said of the khass and changes ONE thing — what follows the lam. That one change is the whole difference.",
      "Meçhûl mâzî fiil; cümle sıladır. Tarif, hâss için söyleneni harfi harfine tekrar eder ve TEK bir şeyi değiştirir: lâmdan sonrasını. Bütün fark o tek değişikliktedir."),
  tok("لِمَعَانٍ","mana","noun",["huruf-jarr","ism-maqsur-manqus","mamnu-min-sarf"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«وُضِعَ» — وَ«مَعَانٍ» جَمْعُ «مَعْنًى» عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ فَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ، لَكِنَّهُ مَنْقُوصٌ حُذِفَتْ يَاؤُهُ فِي الرَّفْعِ وَالْجَرِّ وَعُوِّضَ عَنْهَا بِالتَّنْوِينِ.",
      "A jarr-majrur attaching to «was set down» — and «meanings» is the hard case in this chapter. It is a MUNTAHA AL-JUMU', so it is BARRED FROM TANWIN; and yet a tanwin is written on it. Both are true: being a MANQUS, it drops its ya in raf' and in jarr, and the tanwin standing there is a tanwin of COMPENSATION for the dropped letter, not the tanwin of the indefinite. Put it in nasb and both facts show at once: رَأَيْتُ مَعَانِيَ — the ya returns, and the fatha comes bare.",
      "«وُضِعَ»ye taalluk eden câr-mecrûr — «مَعَانٍ» bu bölümün en çetin kelimesidir. Sîga-i müntehe'l-cumû'dandır, dolayısıyla GAYR-İ MUNSARİFtir; buna rağmen üzerinde tenvîn yazılır. İkisi de doğrudur: MENKŪS olduğu için ref' ve cerde yâsı düşer ve oradaki tenvîn, nekrelik tenvîni değil, düşen harfin yerini tutan İVAZ tenvînidir. Nasb hâline koy, ikisi birden görünsün: رَأَيْتُ مَعَانِيَ — yâ döner, fetha da tenvînsiz gelir.",
      segments=[seg("لِ","li","prep"), seg("مَعَانٍ","mana","noun")]),
  tok("مُخْتَلِفَةٍ","mukhtalif","noun",["naat-sifa","ism-fail","form-viii-verbs"],
      "نَعْتٌ لِـ«مَعَانٍ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «اِخْتَلَفَ»، وَبِهِ خَرَجَ الْمُتَوَاطِئُ الَّذِي مَعَانِيهِ نَوْعٌ وَاحِدٌ.",
      "A na't of «meanings», in jarr — the ism fa'il of اِخْتَلَفَ, and by it the merely general word is shut out, whose meanings are all of one kind.",
      "«مَعَانٍ»in na'tı, mecrûr — «اِخْتَلَفَ»nin ism-i fâili; onunla mânâları tek nevi olan mütevâtı' lafız dışarıda kalır.",
      punct="."),
 ],
 "jumal": [J("الْمُشْتَرَكُ مَا وُضِعَ لِمَعَانٍ مُخْتَلِفَةٍ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s6", "translation": {
 "en": "And the interpreted is that one of whose faces has been given the stronger weight by preponderant judgement.",
 "tr": "Müevvel, vecihlerinden biri gālib re'y ile tercîh edilmiş olandır."},
 "tokens": [
  tok("وَالْمُؤَوَّلُ","muawwal","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُؤَوَّلُ» مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ الرَّابِعُ وَالْأَخِيرُ.",
      "A joining waw; «the interpreted» is the mubtada in raf' — the fourth and last.",
      "Atıf vâvı; «الْمُؤَوَّلُ» merfû mübtedâdır — dördüncü ve sonuncudur.",
      segments=[seg("وَ","wa","conj"), seg("الْمُؤَوَّلُ","muawwal","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("تَرَجَّحَ","tarajjaha","verb",["form-v-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَعْلُومِ عَلَى تَفَعَّلَ، وَهُوَ مُطَاوِعُ «رَجَّحَ» — وَالْجُمْلَةُ صِلَةٌ. وَالْمُطَاوَعَةُ هُنَا مَقْصُودَةٌ: الرُّجْحَانُ وَاقِعٌ بِفِعْلِ الْمُجْتَهِدِ، وَاللَّفْظُ يَقْبَلُهُ.",
      "A past verb on تَفَعَّلَ, the MUTAWA'A of رَجَّحَ — «to be given the stronger weight» — and the clause is the sila. The Form V is chosen on purpose: the weighing is done BY the mujtahid, and the wording is what RECEIVES it. A muawwal is not a word that weighs itself.",
      "TEFA''ALE vezninde ma'lûm mâzî fiil; «رَجَّحَ»in mutâvaatıdır — cümle sıladır. Beşinci bâbın seçilmesi kasıtlıdır: tercîhi yapan müctehiddir, lafız ise onu kabul edendir. Müevvel, kendi kendini tercîh eden bir lafız değildir."),
  tok("بَعْضُ","bad","noun",["fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "The fa'il in raf', and a mudaf.",
      "Merfû fâil ve muzâf."),
  tok("وُجُوهِهِ","wujuh","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ ثَانٍ — فَهَذِهِ إِضَافَةٌ ذَاتُ ثَلَاثَةِ أَرْكَانٍ. وَ«الْوُجُوهُ» جَمْعُ «وَجْهٍ»: الْمَعَانِي الَّتِي يَحْتَمِلُهَا اللَّفْظُ.",
      "The mudaf ilayh in jarr, and itself a mudaf, with the HA as a second mudaf ilayh — a chain of THREE. «Faces» is the plural of wajh: the meanings a wording will bear.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf; HÂ ikinci muzâfun ileyhtir — ÜÇ rükünlü bir izâfet. «الْوُجُوه», «وَجْه»in cemidir: lafzın ihtimâl verdiği mânâlar.",
      segments=[seg("وُجُوهِ","wujuh","noun"), seg("هِ","pron-3ms","pron")]),
  tok("بِغَالِبِ","ghalib","noun",["huruf-jarr","idafa-definiteness","ism-fail"],
      "الْبَاءُ لِلسَّبَبِيَّةِ أَوْ لِلِاسْتِعَانَةِ، وَ«غَالِبِ» مَجْرُورٌ بِهَا وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ مِنْ «غَلَبَ».",
      "The BA of cause or of instrument, and «the preponderant» in jarr after it and a mudaf — the ism fa'il of غَلَبَ.",
      "Sebebiyye yahut istiâne bâsı; «غَالِبِ» onunla mecrûr ve muzâftır — «غَلَبَ»nin ism-i fâili.",
      segments=[seg("بِ","bi","prep"), seg("غَالِبِ","ghalib","noun")]),
  tok("الرَّأْيِ","ray","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ فَارَقَ الْمُؤَوَّلُ الْمُفَسَّرَ: هَذَا ثَبَتَ بِالنَّصِّ الْقَاطِعِ، وَذَاكَ بِغَالِبِ الظَّنِّ، فَاحْتَمَلَ الْخَطَأَ.",
      "The mudaf ilayh in jarr — and with it the muawwal parts company with the mufassar: the one is settled by a decisive text, the other by preponderant judgement, and so it remains open to error. That admission is deliberate, and it is why the muawwal is the weakest of the four.",
      "Mecrûr muzâfun ileyh — müevvel, müfesserden bununla ayrılır: biri kat'î nassla, öteki gālib zanla sâbittir ve bu yüzden hataya ihtimâllidir. Bu itiraf kasıtlıdır; müevvelin dördün en zayıfı olmasının sebebi de budur.",
      punct="."),
 ],
 "jumal": [J("الْمُؤَوَّلُ مَا تَرَجَّحَ بَعْضُ وُجُوهِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("تَرَجَّحَ بَعْضُ وُجُوهِهِ بِغَالِبِ الرَّأْيِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "lafz":        g("لَفْظ", "ل ف ظ", "noun", "utterance, wording", "lafız, söz", 3, plural="أَلْفَاظ"),
 "aqsam":       g("أَقْسَام", "ق س م", "noun", "kinds, divisions (plural of قِسْم)", "kısımlar", 2),
 "khass":       g("خَاصّ", "خ ص ص", "noun", "the SPECIFIC — set down for one meaning alone", "hâss — tek mânâ için vaz' edilen", 4),
 "amm":         g("عَامّ", "ع م م", "noun", "the GENERAL — taking in all it is fit for", "âmm — elverişli olduğu her şeyi kuşatan", 4),
 "mushtarak":   g("مُشْتَرَك", "ش ر ك", "noun", "the SHARED — set down for differing meanings", "müşterek — farklı mânâlar için vaz' edilen", 4),
 "muawwal":     g("مُؤَوَّل", "أ و ل", "noun", "the INTERPRETED — one face preferred by judgement", "müevvel — bir vechi re'yle tercîh edilen", 5),
 "wadaa":       g("وَضَعَ", "و ض ع", "verb", "to set down, to assign (a word to a meaning)", "vaz' etmek", 3),
 # kept letter-for-letter identical to the entry aqaid and kitab-al-sulh carry —
 # `lex` is a GLOBAL key, and two packages disagreeing about one is a defect
 # that surfaces two engines away.
 "mana":        g("مَعْنًى", "ع ن ي", "noun", "meaning", "mana", 3, plural="مَعَانٍ"),
 "wahid":       g("وَاحِد", "و ح د", "noun", "one", "bir; vâhid", 1),
 "infirad":     g("اِنْفِرَاد", "ف ر د", "noun", "standing alone (masdar, Form VII)", "infirâd; tek başına olma (masdar)", 4),
 "an-nasiba":   g("أَنْ", None, "part", "that (masdar-making, puts the mudari in nasb)", "ki (masdariyye, muzâriyi nasb eder)", 2),
 "awjaba":      g("أَوْجَبَ", "و ج ب", "verb", "to oblige, to make binding", "îcâb etmek, gerektirmek", 4),
 "qat":         g("قَطْع", "ق ط ع", "noun", "cutting off; decisiveness (masdar)", "kat'; kesinlik (masdar)", 3),
 "mustaghriq":  g("مُسْتَغْرِق", "غ ر ق", "noun", "taking in the whole of (ism fa'il, Form X)", "istiğrâk eden; kuşatan", 5),
 "jami":        g("جَمِيع", "ج م ع", "noun", "all of, the whole of", "hepsi, tamamı", 2),
 "salaha-mujarrad": g("صَلَحَ", "ص ل ح", "verb", "to be fit for, to be suitable", "elverişli olmak", 3),
 "mukhtalif":   g("مُخْتَلِف", "خ ل ف", "noun", "differing (ism fa'il, Form VIII)", "muhtelif, farklı", 3),
 "tarajjaha":   g("تَرَجَّحَ", "ر ج ح", "verb", "to be given the stronger weight", "tercîh edilmek, ağır basmak", 5),
 "bad":         g("بَعْض", "ب ع ض", "noun", "some, one of", "bazı, biri", 1),
 "wujuh":       g("وُجُوه", "و ج ه", "noun", "faces; the readings a wording bears (plural of وَجْه)", "vecihler; lafzın ihtimâlleri", 3),
 "ghalib":      g("غَالِب", "غ ل ب", "noun", "preponderant, prevailing (ism fa'il)", "gālib, ağır basan", 3),
 "ray":         g("رَأْي", "ر أ ي", "noun", "judgement, considered opinion", "re'y, görüş", 3, plural="آرَاء"),
}

def build_morph():
    out = {}
    # وَضَعَ — MITHAL WAWI, bab fataha (the ʿayn is a throat letter). The waw is
    # not written in the mudari at all: the stem handed to the generator is
    # ضَع, not وضَع. The passive is stored because the chapter turns on it —
    # يُوضَعُ shows the waw coming back.
    out["wadaa"] = _sg.sound1("fataha", "وَضَع", "ضَع", "ضَع", "وَضْع", "وَاضِع",
                              maful="مَوْضُوع", pmz="وُضِعَ", pmd="يُوضَعُ",
                              cls="مِثَالٌ وَاوِيٌّ",
                              note="سَقَطَتِ الْوَاوُ فِي الْمُضَارِعِ، وَعَادَتْ فِي الْمَجْهُولِ «يُوضَعُ».")
    # صَلَحَ يَصْلُحُ — sound, bab nasara. Keyed away from kitab-al-sulh's صَالَحَ,
    # which already owns the plain `salaha` key across the library.
    out["salaha-mujarrad"] = _sg.sound1("nasara", "صَلَح", "صْلُح", "اُصْلُح", "صَلَاح", "صَالِح",
                                        note="وَفِيهِ لُغَةٌ أُخْرَى: صَلُحَ يَصْلُحُ مِنْ بَابِ كَرُمَ.")
    # أَوْجَبَ — Form IV of a mithal. The waw is kept and lengthened: يُوجِبُ.
    out["awjaba"] = _sg.derived("مِنْ بَابِ الْإِفْعَالِ", "أَفْعَلَ يُفْعِلُ", "ُ",
                                "أَوْجَب", "وجِب", "أَوْجِب", "إِيجَاب", "مُوجِب",
                                maful="مُوجَب", pmz="أُوجِبَ", pmd="يُوجَبُ",
                                note="مِثَالٌ وَاوِيٌّ: بَقِيَتِ الْوَاوُ مَدًّا فِي «يُوجِبُ»، وَقُلِبَتْ فِي الْمَصْدَرِ «إِيجَاب».")
    # تَرَجَّحَ — Form V, the mutawa'a of رَجَّحَ.
    out["tarajjaha"] = _sg.derived("مِنْ بَابِ التَّفَعُّلِ", "تَفَعَّلَ يَتَفَعَّلُ", "َ",
                                   "تَرَجَّح", "تَرَجَّح", "تَرَجَّح", "تَرَجُّح", "مُتَرَجِّح",
                                   note="مُطَاوِعُ «رَجَّحَ» — وَالتَّفَعُّلُ بَابُ الْمُطَاوَعَةِ لِلتَّفْعِيلِ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/4.json").write_text(
    json.dumps({"chapter": 4, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 4 for c in man["chapters"]):
    man["chapters"].append({"n": 4, "title": TITLE4})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.4.0"
man["title"] = {"ar": "مُخْتَصَرُ الْمَنَار: التَّعْرِيفَاتُ وَالْأَدِلَّةُ وَأَقْسَامُ اللَّفْظ",
                "en": "Mukhtasar al-Manar: The Definitions, the Sources and the Divisions of the Wording",
                "tr": "Muhtasaru'l-Menâr: Tarifler, Deliller ve Lafzın Kısımları"}
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة الأربعة، ثم تقسيم اللفظ إلى خاص وعام ومشترك ومؤول",
                   "en": "The opening definitions, the four sources, then the wording divided into specific, general, shared and interpreted",
                   "tr": "Açılış tarifleri, dört delil, sonra lafzın hâss, âmm, müşterek ve müevvele taksîmi"}
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch4:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
