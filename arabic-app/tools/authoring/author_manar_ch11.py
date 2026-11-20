# -*- coding: utf-8 -*-
"""Author chapter 11 of mukhtasar-al-manar — the GENERAL and its specification.

Chapters 8 to 10 worked the khass from every side. This chapter turns to its
opposite number, states the Hanafi position on what a general wording obliges,
and then takes up the one operation that is ever performed on it: takhsis, the
cutting of a general down to some of what it covers.

ATTRIBUTION: like chapters 2–10, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • يُوجِبُ — the ACTIVE of أَوْجَبَ, and with it the package has now shown the
    same verb in three cells: أَنْ يُوجِبَ (ch4, mansub), مُوجِب (ch8, participle)
    and يُوجِبُ here, marfu'. One paradigm assembled out of three chapters.
  • قِسْمَانِ — a DUAL as a khabar, its NUN standing, set against دَفَّتَيِ in
    chapter 2 where the same nun fell for an idafa.
  • قَصْرُ الْعَامِّ عَلَى بَعْضِ أَفْرَادِهِ — a MASDAR governing exactly as its verb
    would: a mudaf ilayh for its object and a jarr for what the verb takes.
  • مُتَّصِل — the third اِفْتِعَال of a MITHAL in the package (اِتَّفَاق، اِتِّصَال),
    and مُنْفَصِل beside it on اِنْفِعَال: the same root-idea through two babs.
  • لَا يَسْتَقِلُّ — Form X of a DOUBLED root, the twins meeting under اِسْتَفْعَلَ.
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

TITLE11 = {"ar": "الْعَامُّ وَتَخْصِيصُهُ", "en": "The General and Its Specification",
           "tr": "Âmm ve Tahsîsi"}

S.append({"id": "s1", "translation": {
 "en": "Then the general obliges the ruling in all its instances, decisively, with us.",
 "tr": "Âmm, bize göre bütün fertlerinde hükmü kat'î olarak îcâb ettirir."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ مَعَ التَّرَاخِي — وَبِهِ رَجَعَ مِنَ الْخَاصِّ إِلَى قَسِيمِهِ.",
      "A letter of atf giving sequence with an interval — with it the matn turns back from the khass to its opposite number, having worked the one for three chapters.",
      "Terâhî ile tertîb için atıf harfi — metin, üç bâb boyunca çalıştığı hâsstan onun karşılığına döner."),
  tok("الْعَامُّ","amm","noun",["mubtada-khabar","doubled-verbs"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ الْقِسْمُ الثَّانِي مِنْ أَقْسَامِ الْبَابِ الرَّابِعِ، لَمْ يُعْمَلْ فِيهِ حَتَّى الْآنَ.",
      "The mubtada in raf' — the second of the four kinds chapter 4 named, and nothing had been done with it until now. A matn names its terms early and works them one at a time.",
      "Merfû mübtedâ — dördüncü bâbın saydığı dört kısmın ikincisidir ve şimdiye kadar üzerinde çalışılmamıştı. Metin ıstılahlarını erken sayar, sonra tek tek işler."),
  tok("يُوجِبُ","awjaba","verb",["mudari-marfu","form-iv-verbs","mithal-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ — وَهُوَ «أَوْجَبَ» نَفْسُهُ الَّذِي مَرَّ مَنْصُوبًا فِي «أَنْ يُوجِبَ» وَاسْمَ فَاعِلٍ فِي «مُوجِبُهُ». ثَلَاثَةُ أَبْوَابٍ جَمَعَتْ ثَلَاثَ خَانَاتٍ مِنْ صَرْفٍ وَاحِدٍ.",
      "A mudari in raf' by the damma — and it is the very أَوْجَبَ that stood in nasb in أَنْ يُوجِبَ in chapter 4 and as a participle in مُوجِبُهُ in chapter 8. Three chapters have now assembled three cells of one paradigm, and a reader who has met all three has learned the verb from the text rather than from a table.",
      "Damme ile merfû muzâri — dördüncü bâbda «أَنْ يُوجِبَ»de mansub, sekizinci bâbda «مُوجِبُهُ»de ism-i fâil olarak geçen «أَوْجَبَ»in kendisidir. Üç bâb, tek bir çekimin üç hânesini bir araya getirdi; üçüne de rastlayan okuyucu fiili cetvelden değil metinden öğrenmiştir."),
  tok("الْحُكْمَ","hukm","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "The maf'ul bihi, in nasb.", "Mansub mef'ûlün bih."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يُوجِبُ».",
      "A jarr letter attaching to «obliges».",
      "«يُوجِبُ»a taalluk eden cer harfi."),
  tok("جَمِيعِ","jami","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — وَهُوَ الْكَلِمَةُ الَّتِي حُدَّ بِهَا الْعَامُّ فِي الْبَابِ الرَّابِعِ: «مُسْتَغْرِقٌ لِجَمِيعِ مَا يَصْلُحُ لَهُ».",
      "In jarr after «fi» and a mudaf — the same word by which the general was defined in chapter 4: «taking in ALL that it is fit for». The definition and the ruling use one word, and that is not an accident: what a wording covers is what it obliges.",
      "«فِي» ile mecrûr ve muzâf — dördüncü bâbda âmmın tarif edildiği kelimenin aynısı: «مُسْتَغْرِقٌ لِجَمِيعِ مَا يَصْلُحُ لَهُ». Tarif ile hüküm aynı kelimeyi kullanır ve bu tesadüf değildir: lafız neyi kapsıyorsa onu îcâb ettirir."),
  tok("أَفْرَادِهِ","afrad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ ثَانٍ — جَمْعُ «فَرْدٍ».",
      "The mudaf ilayh in jarr and itself a mudaf, with the HA as a second mudaf ilayh — the plural of «fard», an individual instance.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf; HÂ ikinci muzâfun ileyhtir — «فَرْد»in cemidir."),
  tok("قَطْعًا","qat","noun",["maful-mutlaq","masdar"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ — وَهُوَ اللَّفْظُ نَفْسُهُ الَّذِي وُصِفَ بِهِ حُكْمُ الْخَاصِّ فِي الْبَابِ الرَّابِعِ، وَفِيهِ تَمَامُ الْخِلَافِ: الْقَطْعُ فِي الْعَامِّ مَذْهَبُنَا، وَغَيْرُنَا يَرَاهُ ظَنِّيًّا.",
      "A maf'ul mutlaq in nasb — the same word that described the khass's ruling in chapter 4, and the whole disagreement sits in it. That a GENERAL obliges DECISIVELY is the Hanafi position; others hold that a general is only presumptive until nothing specifies it. The matn states its school and does not hide that there is another.",
      "Mansub mef'ûl-ü mutlak — dördüncü bâbda hâssın hükmünü niteleyen kelimenin aynısı ve bütün ihtilâf onun içindedir. Âmmın KAT'Î olarak îcâb etmesi bizim mezhebimizdir; başkaları âmmı, tahsîs edilmedikçe zannî sayar. Metin mezhebini söyler ve başka bir görüş olduğunu gizlemez."),
  tok("عِنْدَنَا","inda","noun",["maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَ«نَا» مُضَافٌ إِلَيْهِ — وَهِيَ الْكَلِمَةُ الَّتِي مَرَّتْ فِي بَابِ الْمُطْلَقِ لِلْغَرَضِ عَيْنِهِ.",
      "An adverb in nasb and a mudaf, with «na» as its mudaf ilayh — the same word that stood in the chapter on the unrestricted, and for the same purpose: to mark a position as this school's own.",
      "Mansub zarf ve muzâf; «نَا» muzâfun ileyhtir — mutlak bâbında aynı maksatla geçen kelimenin aynısı: bir görüşün bu mezhebe ait olduğunu işaretlemek.",
      punct=".", segments=[seg("عِنْدَ","inda","noun"), seg("نَا","pron-1p","pron")]),
 ],
 "jumal": [J("الْعَامُّ يُوجِبُ الْحُكْمَ فِي جَمِيعِ أَفْرَادِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause whose khabar is a verbal clause — i'rabless.",
   "Haberi fiil cümlesi olan isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And specification is the cutting of the general down to some of its instances, by an indication that comes with it.",
 "tr": "Tahsîs, âmmı, kendisiyle beraber gelen bir delille fertlerinin bir kısmına hasretmektir."},
 "tokens": [
  tok("وَالتَّخْصِيصُ","takhsis","noun",["atf-nasaq","mubtada-khabar","masdar","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«التَّخْصِيصُ» مُبْتَدَأٌ مَرْفُوعٌ — مَصْدَرُ «خَصَّصَ» عَلَى تَفْعِيلٍ، وَلَامُهُ صَحِيحَةٌ فَجَاءَ عَلَى أَصْلِ الْوَزْنِ.",
      "A joining waw; «specification» is the mubtada in raf' — the masdar of خَصَّصَ on تَفْعِيل, its lam a sound letter so the pattern stands whole. The third تَفْعِيل in the package after تَقْرِير and تَحْرِيم, against تَعْدِيَة where the weak lam forced the ta marbuta in.",
      "Atıf vâvı; «التَّخْصِيصُ» merfû mübtedâdır — «خَصَّصَ»in TEF'ÎL vezninde masdarı; lâmı sahîh olduğu için vezin tam gelmiştir. Pakette «تَقْرِير» ve «تَحْرِيم»den sonra üçüncü tef'îldir; illetli lâmın tâ-i merbûtayı zorladığı «تَعْدِيَة»in karşısında durur.",
      segments=[seg("وَ","wa","conj"), seg("التَّخْصِيصُ","takhsis","noun")]),
  tok("قَصْرُ","qasr","noun",["mubtada-khabar","masdar","idafa-definiteness","qasr"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «قَصَرَ»، وَهُوَ عَامِلٌ عَمَلَ فِعْلِهِ: أُضِيفَ إِلَى مَفْعُولِهِ ثُمَّ تَعَلَّقَ بِهِ الْجَارُّ بَعْدَهُ.",
      "The khabar in raf' and a mudaf — the masdar of قَصَرَ, and it GOVERNS exactly as its verb would: what follows it in the idafa is its OBJECT in meaning, and the jarr after that hangs on it too. A masdar is a verb with a noun's ending; watch what it takes and the sentence unfolds.",
      "Merfû haber ve muzâf — «قَصَرَ»in masdarı ve fiili gibi AMEL EDER: izâfetle kendisine eklenen, mânâ cihetinden mef'ûlüdür; sonraki câr da ona taalluk eder. Masdar, ismin sonunu taşıyan bir fiildir; ne aldığına bak, cümle açılır."),
  tok("الْعَامِّ","amm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ فِي اللَّفْظِ، مَفْعُولُ الْمَصْدَرِ فِي الْمَعْنَى.",
      "The mudaf ilayh in jarr by its FORM, the masdar's object in MEANING — the same double reading الْحُكْمِ had after تَعْدِيَة in chapter 3.",
      "Lafzan mecrûr muzâfun ileyh, ma'nen masdarın mef'ûlü — üçüncü bâbda «تَعْدِيَة»den sonraki «الْحُكْمِ»in aynı çifte okunuşu."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«قَصْرُ» — وَ«قَصَرَ» لَا يَتِمُّ إِلَّا بِهِ.",
      "A jarr letter attaching to «the cutting» — and قَصَرَ does not complete without it: a thing is always cut down ONTO something.",
      "«قَصْرُ»a taalluk eden cer harfi — «قَصَرَ» onsuz tamam olmaz: bir şey daima bir şeye hasredilir."),
  tok("بَعْضِ","bad","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَلَى» وَهُوَ مُضَافٌ.",
      "In jarr after «ala», and a mudaf.",
      "«عَلَى» ile mecrûr ve muzâf."),
  tok("أَفْرَادِهِ","afrad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — سِلْسِلَةٌ مِنْ أَرْبَعٍ: بَعْضِ ← أَفْرَادِ ← الْهَاءِ.",
      "The mudaf ilayh in jarr and itself a mudaf, with the HA a further one. Counting from قَصْرُ the chain runs four members deep, and every middle link is a mudaf and a mudaf ilayh at once.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf; HÂ da ayrıca muzâfun ileyhtir. «قَصْرُ»dan sayınca zincir dört halkadır ve ortadaki her halka aynı anda hem muzâf hem muzâfun ileyhtir."),
  tok("بِدَلِيلٍ","dalil","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«قَصْرُ» — وَبِهِ يُفَارِقُ التَّخْصِيصُ التَّحَكُّمَ.",
      "A jarr-majrur attaching to «the cutting» — and it is what separates specification from arbitrariness. Chapter 9 shut the same door on the mutlaq with the same word.",
      "«قَصْرُ»a taalluk eden câr-mecrûr — tahsîsi keyfîlikten ayıran kayıttır. Dokuzuncu bâb aynı kapıyı mutlak için aynı kelimeyle kapatmıştı.",
      segments=[seg("بِ","bi","prep"), seg("دَلِيلٍ","dalil","noun")]),
  tok("مُقْتَرِنٍ","muqtarin","noun",["naat-sifa","ism-fail","form-viii-verbs"],
      "نَعْتٌ لِـ«دَلِيلٍ» مَجْرُورٌ — اسْمُ فَاعِلٍ مِنْ «اِقْتَرَنَ» عَلَى مُفْتَعِلٍ، وَجَذْرُهُ «ق ر ن» الَّذِي جَاءَتْ مِنْهُ «الْقَرِينَةُ» فِي بَابَيِ الْأَمْرِ وَالْكِنَايَةِ.",
      "A na't of «an indication», in jarr — the ism fa'il of اِقْتَرَنَ on مُفْتَعِل, from the root ق ر ن that gave قَرِينَة in the chapters on the command and on the veiled. Same root, three chapters, and the sense holds throughout: a thing that comes ALONGSIDE and changes how the words are read.",
      "«دَلِيلٍ»in na'tı, mecrûr — «اِقْتَرَنَ»nin MÜFTEİL vezninde ism-i fâili; kökü «ق ر ن»dir ve emir ile kinâye bâblarındaki «الْقَرِينَة» de ondandır. Aynı kök, üç bâb ve mânâ hep aynı: YANINDA gelip lafzın okunuşunu değiştiren şey.",
      punct="."),
 ],
 "jumal": [J("التَّخْصِيصُ قَصْرُ الْعَامِّ عَلَى بَعْضِ أَفْرَادِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the specifier is of two kinds: connected and separate.",
 "tr": "Muhassıs iki kısımdır: muttasıl ve munfasıl."},
 "tokens": [
  tok("وَالْمُخَصِّصُ","mukhassis","noun",["atf-nasaq","mubtada-khabar","ism-fail","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُخَصِّصُ» مُبْتَدَأٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «خَصَّصَ» عَلَى مُفَعِّلٍ، بِكَسْرِ الصَّادِ الْأُولَى.",
      "A joining waw; «the specifier» is the mubtada in raf' — the ism fa'il of خَصَّصَ on مُفَعِّل, with a KASRA on the doubled letter. Put a fatha there and it becomes مُخَصَّص, the thing specified. The same one-vowel distinction الْمُجْمِل and الْمُجْمَل turned on in chapter 6.",
      "Atıf vâvı; «الْمُخَصِّصُ» merfû mübtedâdır — «خَصَّصَ»in MÜFA''İL vezninde ism-i fâili; şeddeli harf KESRALIdır. Oraya fetha koy, «مُخَصَّص» olur: tahsîs edilen şey. Altıncı bâbdaki «الْمُجْمِل» ile «الْمُجْمَل» arasındaki tek harekelik farkın aynısı.",
      segments=[seg("وَ","wa","conj"), seg("الْمُخَصِّصُ","mukhassis","noun")]),
  tok("قِسْمَانِ","qism","noun",["mubtada-khabar","al-muthanna"],
      "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، وَنُونُهُ ثَابِتَةٌ لِأَنَّهُ غَيْرُ مُضَافٍ — بِخِلَافِ «دَفَّتَيِ الْمُصْحَفِ» فِي الْبَابِ الثَّانِي حَيْثُ سَقَطَتْ لِلْإِضَافَةِ.",
      "The khabar, in raf' by the ALIF because it is a DUAL — and its NUN stands, because nothing is added to it. Set it against دَفَّتَيِ الْمُصْحَفِ in chapter 2, where the same nun fell for an idafa. The nun is present here and absent there for one reason only, and that reason is the whole rule.",
      "ELİF ile merfû haber, zira TESNİYEdir — ve NÛNu durur, çünkü muzâf değildir. İkinci bâbdaki «دَفَّتَيِ الْمُصْحَفِ» ile karşılaştır: orada aynı nûn izâfet için düşmüştü. Nûnun burada bulunup orada bulunmamasının tek bir sebebi vardır ve kaidenin tamamı odur.", punct="："),
  tok("مُتَّصِلٌ","muttasil","noun",["badal","ism-fail","form-viii-verbs","mithal-verbs"],
      "بَدَلُ تَفْصِيلٍ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «اِتَّصَلَ» عَلَى مُفْتَعِلٍ، وَأَصْلُهُ «مُوْتَصِل» مِنْ «و ص ل»: أُبْدِلَتِ الْوَاوُ تَاءً وَأُدْغِمَتْ، كَمَا فِي «اِتِّفَاق» فِي الْبَابِ الثَّالِثِ.",
      "A badal of detail, in raf' — the ism fa'il of اِتَّصَلَ on مُفْتَعِل. Its origin is مُوْتَصِل from و ص ل: the waw was turned into a ta and swallowed by the pattern's ta, exactly as اِتِّفَاق in chapter 3. The doubled ta you see is two letters and neither of them is the root's.",
      "Merfû tafsîl bedeli — «اِتَّصَلَ»nin MÜFTEİL vezninde ism-i fâili. Aslı «و ص ل»den «مُوْتَصِل»dir: vâv tâya kalbedilip veznin tâsına idgâm edilmiştir — üçüncü bâbdaki «اِتِّفَاق» gibi. Gördüğün şeddeli tâ iki harftir ve hiçbiri kökün değildir."),
  tok("وَمُنْفَصِلٌ","munfasil","noun",["atf-nasaq","ism-fail","form-vii-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «اِنْفَصَلَ» عَلَى مُنْفَعِلٍ، وَهُوَ سَلِيمُ الْفَاءِ فَلَمْ يَعْرِضْ لَهُ شَيْءٌ.",
      "Joined, in raf' — the ism fa'il of اِنْفَصَلَ on مُنْفَعِل. Its first radical is a sound letter, so nothing happens to it at all. The pair is the lesson: مُتَّصِل had to be repaired and مُنْفَصِل did not, and the difference is entirely in the first letter of the root.",
      "Ma'tûf, merfû — «اِنْفَصَلَ»nin MÜNFAİL vezninde ism-i fâili; fâsı sahîh olduğu için başına hiçbir şey gelmemiştir. Ders çiftin kendisidir: «مُتَّصِل» tamire muhtaç oldu, «مُنْفَصِل» olmadı; fark tamamen kökün ilk harfindedir.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("مُنْفَصِلٌ","munfasil","noun")]),
 ],
 "jumal": [J("الْمُخَصِّصُ قِسْمَانِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "So the connected is what does not stand on its own, like the exception, the condition and the description.",
 "tr": "Muttasıl, kendi başına müstakil olmayandır: istisnâ, şart ve sıfat gibi."},
 "tokens": [
  tok("فَالْمُتَّصِلُ","muttasil","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الْمُتَّصِلُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the connected» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الْمُتَّصِلُ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الْمُتَّصِلُ","muttasil","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا.",
      "«La» simply denying, and governing nothing.",
      "Amel etmeyen nefy «لَا»sı."),
  tok("يَسْتَقِلُّ","istaqalla","verb",["mudari-marfu","form-x-verbs","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ عَلَى «اِسْتَفْعَلَ» مِنْ «ق ل ل» — مُضَاعَفٌ الْتَقَى مِثْلَاهُ فَأُدْغِمَ الْأَوَّلُ فِي الثَّانِي، وَأَصْلُهُ «يَسْتَقْلِلُ». وَيَنْفَكَّانِ مَتَى جَاءَ سَاكِنٌ: «يَسْتَقْلِلْنَ».",
      "A mudari in raf' on اِسْتَفْعَلَ from ق ل ل — a DOUBLED root whose two identical letters have met and been run together; its origin is يَسْتَقْلِلُ. They come apart again the moment an ending brings a sukun: يَسْتَقْلِلْنَ. That is the whole behaviour of a mudaaf, and it holds in every bab it is put through.",
      "«ق ل ل»den «اِسْتَفْعَلَ» vezninde merfû muzâri — MUZÂAF olup iki misli karşılaşmış ve birincisi ikinciye idgâm edilmiştir; aslı «يَسْتَقْلِلُ»dur. Sâkin bir ek gelir gelmez ayrılırlar: «يَسْتَقْلِلْنَ». Muzâafın bütün davranışı budur ve konulduğu her bâbda aynı kalır."),
  tok("بِنَفْسِهِ","nafs","noun",["huruf-jarr","idafa-definiteness","tawkid"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَسْتَقِلُّ»، وَ«نَفْسِ» مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "A jarr-majrur attaching to «stands», «the very self of» a mudaf and the HA its mudaf ilayh — the same phrase that stood in the definition of the manifest in chapter 5, there restricting and here excluding.",
      "«يَسْتَقِلُّ»a taalluk eden câr-mecrûr; «نَفْسِ» muzâf, HÂ muzâfun ileyhtir — beşinci bâbda zâhirin tarifinde geçen ibarenin aynısı; orada hasrediyordu, burada dışarıda bırakıyor.",
      segments=[seg("بِ","bi","prep"), seg("نَفْسِ","nafs","noun"), seg("هِ","pron-3ms","pron")]),
  tok("كَالِاسْتِثْنَاءِ","istithna-noun","noun",["huruf-jarr","masdar","form-viii-verbs","istithna"],
      "الْكَافُ حَرْفُ جَرٍّ لِلتَّمْثِيلِ، وَ«الِاسْتِثْنَاءِ» مَجْرُورٌ بِهَا — مَصْدَرُ «اِسْتَثْنَى» عَلَى اسْتِفْعَالٍ، وَقَدْ مَرَّ الْمُسْتَثْنَى الْمُفَرَّغُ فِي أَرْبَعَةِ أَبْوَابٍ.",
      "The KAF is a jarr letter here giving an EXAMPLE, not a comparison, and «the exception» is in jarr after it — the masdar of اِسْتَثْنَى on اِسْتِفْعَال. Four chapters have now shown the mufarragh kind; this is the operation itself, named as one of the three specifiers that cannot stand alone.",
      "KÂF burada teşbîh değil TEMSÎL için cer harfidir; «الِاسْتِثْنَاءِ» onunla mecrûrdur — «اِسْتَثْنَى»nin İSTİF'ÂL vezninde masdarı. Dört bâb müferrağ istisnâyı gösterdi; bu, işlemin kendisidir ve tek başına duramayan üç muhassıstan biri olarak sayılır.",
      segments=[seg("كَ","ka","prep"), seg("الِاسْتِثْنَاءِ","istithna-noun","noun")]),
  tok("وَالشَّرْطِ","shart","noun",["atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — وَهُوَ الثَّانِي مِنَ الْمُخَصِّصَاتِ الْمُتَّصِلَةِ.",
      "Joined, in jarr — the second of the connected specifiers: «free a slave IF you can».",
      "Ma'tûf, mecrûr — muttasıl muhassısların ikincisi: «gücün yeterse bir köle âzâd et».",
      segments=[seg("وَ","wa","conj"), seg("الشَّرْطِ","shart","noun")]),
  tok("وَالصِّفَةِ","sifa","noun",["atf-nasaq","naat-sifa"],
      "مَعْطُوفٌ مَجْرُورٌ — وَهِيَ الثَّالِثَةُ، وَبِهَا يَلْتَقِي هَذَا الْبَابُ بِبَابِ الْمُقَيَّدِ: الصِّفَةُ الزَّائِدَةُ هُنَاكَ قَيَّدَتِ الْخَاصَّ، وَهِيَ هُنَا تُخَصِّصُ الْعَامَّ.",
      "Joined, in jarr — the third, and with it this chapter meets the chapter on the restricted. There an added description put a fetter on a khass; here the same kind of description cuts a general down. One device, two offices, and the difference is only in what it is applied to.",
      "Ma'tûf, mecrûr — üçüncüsüdür ve bu bâb onunla mukayyed bâbıyla buluşur. Orada zâid bir sıfat hâssı kayıtlıyordu; burada aynı cinsten bir sıfat âmmı tahsîs eder. Tek vasıta, iki vazife; fark yalnız neye uygulandığındadır.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("الصِّفَةِ","sifa","noun")]),
 ],
 "jumal": [J("الْمُتَّصِلُ مَا لَا يَسْتَقِلُّ بِنَفْسِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("لَا يَسْتَقِلُّ بِنَفْسِهِ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And the separate is what stands on its own, so it comes in a place other than the general's.",
 "tr": "Munfasıl, kendi başına müstakil olandır; bu yüzden âmmın bulunduğu yerden başka bir yerde gelir."},
 "tokens": [
  tok("وَالْمُنْفَصِلُ","munfasil","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُنْفَصِلُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the separate» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُنْفَصِلُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُنْفَصِلُ","munfasil","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("يَسْتَقِلُّ","istaqalla","verb",["mudari-marfu","form-x-verbs","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَهُوَ عَيْنُ فِعْلِ الْحَدِّ السَّابِقِ بِلَا «لَا»: فَالْقِسْمَانِ يُحَدَّانِ بِكَلِمَةٍ وَاحِدَةٍ، أُثْبِتَتْ هُنَا وَنُفِيَتْ هُنَاكَ.",
      "A mudari in raf' — the very verb of the definition before it, minus the «la». The two kinds are defined by ONE word, affirmed here and denied there. A matn that can do that has understood its own division.",
      "Merfû muzâri — bir önceki tarifin fiilinin aynısı, «لَا»sız. İki kısım TEK bir kelimeyle tarif edilir: burada isbât, orada nefy. Bunu yapabilen bir metin kendi taksîmini anlamış demektir."),
  tok("بِنَفْسِهِ","nafs","noun",["huruf-jarr","idafa-definiteness","tawkid"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَسْتَقِلُّ».",
      "A jarr-majrur attaching to «stands».",
      "«يَسْتَقِلُّ»a taalluk eden câr-mecrûr.",
      segments=[seg("بِ","bi","prep"), seg("نَفْسِ","nafs","noun"), seg("هِ","pron-3ms","pron")]),
  tok("فَيَرِدُ","warada","verb",["atf-nasaq","mudari-marfu","mithal-verbs"],
      "الْفَاءُ لِلتَّرْتِيبِ وَالتَّسَبُّبِ، وَ«يَرِدُ» فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — مِثَالٌ سَقَطَتْ وَاوُهُ، وَقَدْ مَرَّ فِي بَابِ الْأَمْرِ.",
      "A fa of sequence AND of cause — «and so» — and «yaridu» a mudari in raf', the mithal whose waw dropped, met before in the chapter on the command. Because it stands on its own, it can come anywhere: that is not a further fact about it but a consequence of the one just stated.",
      "Tertîb ve sebep fâsı — «bu yüzden» — ve «يَرِدُ» merfû muzâri: vâvı düşmüş misâl; emir bâbında geçmişti. Müstakil olduğu için her yerde gelebilir; bu, onun hakkında ayrı bir bilgi değil, az önce söylenenin neticesidir.",
      segments=[seg("فَ","fa","conj"), seg("يَرِدُ","warada","verb")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِـ«يَرِدُ».",
      "A jarr letter attaching to «comes».",
      "«يَرِدُ»a taalluk eden cer harfi."),
  tok("غَيْرِ","ghayr","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — وَقَدْ مَرَّ فِي بَابِ الْمَجَازِ مُضَافًا إِلَى جُمْلَةٍ، وَهُوَ هُنَا مُضَافٌ إِلَى اسْمٍ.",
      "In jarr after «fi» and a mudaf — in the chapter on the figurative it was added to a whole relative clause; here to a plain noun. غَيْر takes whatever it is given and stays indefinite through all of it.",
      "«فِي» ile mecrûr ve muzâf — mecâz bâbında bir mevsûl cümlesine muzâf olmuştu, burada sade bir isme. «غَيْر» kendisine ne verilirse alır ve hepsinde nekre kalır."),
  tok("مَوْضِعِ","mawdi","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — اسْمُ مَكَانٍ مِنْ «وَضَعَ» عَلَى مَفْعِلٍ، وَهُوَ الْفِعْلُ الَّذِي بُنِيَ عَلَيْهِ بَابُ الْأَقْسَامِ كُلُّهُ.",
      "The mudaf ilayh in jarr and itself a mudaf — a PLACE-NOUN from وَضَعَ on مَفْعِل, the very verb chapter 4 built its whole division on. A mithal makes its place-noun on مَفْعِل with a kasra, not مَفْعَل: مَوْضِع، مَوْعِد، مَوْقِف.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — «وَضَعَ»den MEF'İL vezninde İSM-İ MEKÂN; dördüncü bâbın bütün taksîmini üzerine kurduğu fiilin aynısı. Misâl fiil, ism-i mekânını MEF'AL değil kesralı MEF'İL vezninde yapar: مَوْضِع، مَوْعِد، مَوْقِف."),
  tok("الْعَامِّ","amm","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ خُتِمَ الْبَابُ عَلَى مَا فُتِحَ بِهِ.",
      "The mudaf ilayh in jarr — and with it the chapter closes on the word it opened with.",
      "Mecrûr muzâfun ileyh — bâb, açıldığı kelimeyle kapanır.",
      punct="."),
 ],
 "jumal": [J("الْمُنْفَصِلُ مَا يَسْتَقِلُّ بِنَفْسِهِ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("فَيَرِدُ فِي غَيْرِ مَوْضِعِ الْعَامِّ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ عَلَى الصِّلَةِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause joined to the sila — i'rabless.",
   "Sılaya ma'tûf fiil cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "afrad":         g("أَفْرَاد", "ف ر د", "noun", "instances, individuals (plural of فَرْد)", "fertler", 3),
 "takhsis":       g("تَخْصِيص", "خ ص ص", "noun", "specification — cutting a general down (masdar, Form II)", "tahsîs (masdar)", 4),
 "qasr":          g("قَصْر", "ق ص ر", "noun", "confining a thing to something (masdar)", "kasr; bir şeye hasretme (masdar)", 4),
 "muqtarin":      g("مُقْتَرِن", "ق ر ن", "noun", "coming alongside, accompanying (ism fa'il, Form VIII)", "mukārin; beraberinde gelen", 4),
 "mukhassis":     g("مُخَصِّص", "خ ص ص", "noun", "the SPECIFIER — what cuts a general down (ism fa'il)", "muhassıs — âmmı tahsîs eden", 4),
 "qism":          g("قِسْم", "ق س م", "noun", "a kind, a division", "kısım", 2, plural="أَقْسَام"),
 "muttasil":      g("مُتَّصِل", "و ص ل", "noun", "CONNECTED — not standing on its own (ism fa'il, Form VIII)", "muttasıl — kendi başına durmayan", 4),
 "munfasil":      g("مُنْفَصِل", "ف ص ل", "noun", "SEPARATE — standing on its own (ism fa'il, Form VII)", "munfasıl — kendi başına duran", 4),
 "istaqalla":     g("اِسْتَقَلَّ", "ق ل ل", "verb", "to stand on its own, to be independent", "müstakil olmak", 4),
 "istithna-noun": g("اِسْتِثْنَاء", "ث ن ي", "noun", "exception — «except …» (masdar, Form X)", "istisnâ (masdar)", 4),
 "shart":         g("شَرْط", "ش ر ط", "noun", "a condition", "şart", 2, plural="شُرُوط"),
 "sifa":          g("صِفَة", "و ص ف", "noun", "a description, an adjective", "sıfat", 2, plural="صِفَات"),
 "mawdi":         g("مَوْضِع", "و ض ع", "noun", "a place (ism makan of وَضَعَ)", "mevzi; yer (ism-i mekân)", 3, plural="مَوَاضِع"),
 "ka":            g("كَـ", None, "prep", "like, such as (jarr letter)", "gibi (cer harfi)", 1),
}

def build_morph():
    out = {}
    # اِسْتَقَلَّ — Form X of a DOUBLED root. The contracted stem carries the
    # conjugation and the uncontracted one comes back for every person whose
    # ending brings a sukun.
    G, Sh = "سْتَقِلّ", "سْتَقْلِل"
    out["istaqalla"] = _sg.entry(
        "بَابُ الِاسْتِفْعَالِ: اِسْتَفْعَلَ يَسْتَفْعِلُ — مُضَاعَفٌ", "اِسْتَفْعَلَ يَسْتَفْعِلُ",
        "اِسْتِقْلَال", "مُسْتَقِلّ",
        _sg.mazi14("اِسْتَقَلّ", "اِسْتَقْلَل"), _sg.mudari14("َ", G, Sh),
        ["اِ"+G+"َ", "اِ"+G+"َا", "اِ"+G+"ُوا", "اِ"+G+"ِي", "اِ"+G+"َا", "اِ"+Sh+"ْنَ"],
        "يَ"+G+"َ", "يَ"+G+"َ", "تَ"+G+"َ",
        note="مُضَاعَفٌ مِنَ الِاسْتِفْعَالِ: الْجَزْمُ بِالْفَتْحِ، وَيَجُوزُ الْفَكُّ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/11.json").write_text(
    json.dumps({"chapter": 11, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 11 for c in man["chapters"]):
    man["chapters"].append({"n": 11, "title": TITLE11})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.11.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch11:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
