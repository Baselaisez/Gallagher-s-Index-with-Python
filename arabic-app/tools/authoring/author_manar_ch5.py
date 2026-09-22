# -*- coding: utf-8 -*-
"""Author chapter 5 of mukhtasar-al-manar — the four degrees of CLARITY.

Chapter 4 divided the wording by what it was set down FOR. This chapter divides
it by how plainly the meaning shows, and the four are a LADDER, not a list:
each is defined as the one before it plus one more degree of clearness. زَاهِر،
نَصّ، مُفَسَّر، مُحْكَم — and the matn says so with the same verb four times,
اِزْدَادَ وُضُوحًا, so that the reader cannot miss that the four are one thing
measured, not four separate things.

ATTRIBUTION: like chapters 2–4, set from the RECEIVED matn of the Hanafi usul
tradition, not from the owner's supplied page. Every sentence here is matn.

Grammar this chapter is chosen to teach:
  • وُضُوحًا four times — TAMYIZ, and the kind the books call تَمْيِيزُ النِّسْبَةِ:
    the sentence is vague about WHAT increased and the mansub noun settles it.
    Four occurrences in five sentences is a drill, not an example.
  • اِزْدَادَ — Form VIII of ز ي د, where two rules fire at once: the ta of
    اِفْتِعَال becomes د after the zay, and the hollow root melts to an alif.
  • بِحَيْثُ — حَيْثُ, mabni on the damma, and a mudaf to a whole SENTENCE. One
    of the very few words that takes a clause for its mudaf ilayh.
  • اِنْسَدَّ — Form VII of a doubled root, where the twins meet and run together.
  • مِنْ غَيْرِ تَأَمُّلٍ — غَيْر as a mudaf, and the phrase that does the real work
    in the definition of the zahir.
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

TITLE5 = {"ar": "مَرَاتِبُ الْوُضُوح", "en": "The Degrees of Clarity",
          "tr": "Vuzûhun Mertebeleri"}

# a phrase the chapter repeats four times, so its i'rab is written once
TAMYIZ = ("تَمْيِيزٌ مَنْصُوبٌ — وَهُوَ تَمْيِيزُ نِسْبَةٍ: الْجُمْلَةُ مُبْهَمَةٌ فِيمَا ازْدَادَ، فَجَاءَ لِيُبَيِّنَهُ.",
 "A TAMYIZ in nasb — and of the kind called تَمْيِيزُ النِّسْبَةِ: the clause leaves it vague WHAT increased, and this mansub noun settles it. Ask «increased in what?» and the answer is the tamyiz.",
 "Mansub TEMYÎZ — hem de TEMYÎZ-İ NİSBET nev'inden: cümle NEyin arttığı hususunda mübhemdir, bu mansub isim onu tayin eder. «Ne bakımından arttı?» diye sor; cevap temyîzdir.")

S.append({"id": "s1", "translation": {
 "en": "Then the wording, taken by the clearness of its meaning, is four: the manifest, the explicit, the expounded and the firm.",
 "tr": "Lafız, mânâsının vuzûhu itibarıyla dörttür: zâhir, nass, müfesser ve muhkem."},
 "tokens": [
  tok("ثُمَّ","thumma","conj",["atf-nasaq"],
      "حَرْفُ عَطْفٍ يُفِيدُ التَّرْتِيبَ مَعَ التَّرَاخِي — انْتَقَلَ بِهِ مِنْ تَقْسِيمِ اللَّفْظِ بِوَضْعِهِ إِلَى تَقْسِيمِهِ بِوُضُوحِهِ.",
      "A letter of atf giving sequence with an interval — with it the matn steps from dividing the wording by what it was SET DOWN for to dividing it by how plainly it SHOWS.",
      "Terâhî ile tertîb bildiren atıf harfi — metin onunla lafzı vaz'ına göre taksîmden, vuzûhuna göre taksîme geçer."),
  tok("اللَّفْظُ","lafz","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ عَيْنُ الْمُبْتَدَإِ فِي أَوَّلِ الْبَابِ السَّابِقِ، وَالتَّقْسِيمُ غَيْرُهُ.",
      "The mubtada in raf' — the very same mubtada the chapter before opened with. The word being divided has not changed; the RULER being held against it has.",
      "Merfû mübtedâ — bir önceki bâbın açılışındaki mübtedânın aynısıdır. Taksim edilen şey değişmedi; ona tutulan ölçü değişti."),
  tok("بِاعْتِبَارِ","itibar","noun",["huruf-jarr","idafa-definiteness","masdar","form-viii-verbs"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٍ، وَ«اعْتِبَارِ» مُضَافٌ — مَصْدَرُ «اِعْتَبَرَ» عَلَى افْتِعَالٍ.",
      "A jarr-majrur hanging on an omitted word that stands as a hal, and «taken by» is a mudaf — the masdar of اِعْتَبَرَ on اِفْتِعَال. It is the word that announces a change of criterion, and every division in the book is introduced by it.",
      "Mahzûf bir hâle taalluk eden câr-mecrûr; «اعْتِبَارِ» muzâftır — «اِعْتَبَرَ»nin İFTİÂL vezninde masdarı. Ölçü değişikliğini haber veren kelimedir; kitaptaki her taksim onunla girer.",
      segments=[seg("بِ","bi","prep"), seg("اعْتِبَارِ","itibar","noun")]),
  tok("وُضُوحِ","wuduh","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ «وَضَحَ».",
      "The mudaf ilayh in jarr, and itself a mudaf — the masdar of وَضَحَ.",
      "Mecrûr muzâfun ileyh ve kendisi de muzâf — «وَضَحَ»nin masdarı."),
  tok("الْمَعْنَى","mana","noun",["idafa-definiteness","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — وَهُوَ مَقْصُورٌ عُرِّفَ بِـ«أَلْ» فَلَمْ يُنَوَّنْ.",
      "The mudaf ilayh, in jarr by a kasra ESTIMATED on the alif, which cannot carry one. It is the same maqsur the chapter before showed indefinite as مَعْنًى — here made definite by ال, so the tanwin is gone and nothing at all is written on the end.",
      "Elif üzerinde teazzür sebebiyle TAKDÎRÎ kesra ile mecrûr muzâfun ileyh. Bir önceki bâbda مَعْنًى olarak nekre görünen maksûrun aynısıdır; burada «أَلْ» ile marife olduğu için tenvîn gitmiş, sona hiçbir şey yazılmamıştır."),
  tok("أَرْبَعَةٌ","arbaa","noun",["mubtada-khabar","tamyiz"],
      "خَبَرٌ مَرْفُوعٌ مُنَوَّنٌ — وَهُوَ هُنَا غَيْرُ مُضَافٍ، بِخِلَافِ «أَرْبَعَةُ أَقْسَامٍ» فِي الْبَابِ السَّابِقِ.",
      "The khabar in raf', with its tanwin — NOT a mudaf here, unlike أَرْبَعَةُ أَقْسَامٍ in the chapter before. The tanwin is the whole difference, and it is worth pausing on: the same numeral, the same office, and one letter telling you whether a noun follows it.",
      "Tenvînli merfû haber — bir önceki bâbdaki «أَرْبَعَةُ أَقْسَامٍ»in aksine burada MUZÂF DEĞİLDİR. Bütün fark tenvîndedir ve durup düşünmeye değer: aynı sayı, aynı vazife; ardından bir isim gelip gelmediğini tek bir harf söylüyor.", punct="："),
  tok("ظَاهِرٌ","zahir","noun",["badal","ism-fail"],
      "بَدَلُ تَفْصِيلٍ مِنْ «أَرْبَعَةٌ» مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ «ظَهَرَ».",
      "A badal of detail from «four», in raf' — the ism fa'il of ظَهَرَ.",
      "«أَرْبَعَةٌ»den merfû tafsîl bedeli — «ظَهَرَ»nin ism-i fâili."),
  tok("وَنَصٌّ","nass","noun",["atf-nasaq","doubled-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — مَصْدَرُ «نَصَّ» بِمَعْنَى الْمَفْعُولِ: الْمَنْصُوصُ عَلَيْهِ.",
      "Joined, in raf' — the masdar of نَصَّ used in the sense of the passive participle: the thing spoken out plainly.",
      "Ma'tûf, merfû — «نَصَّ»nin mef'ûl mânâsında masdarı: açıkça bildirilen şey.",
      segments=[seg("وَ","wa","conj"), seg("نَصٌّ","nass","noun")]),
  tok("وَمُفَسَّرٌ","mufassar","noun",["atf-nasaq","ism-maful","form-ii-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «فَسَّرَ» عَلَى مُفَعَّلٍ.",
      "Joined, in raf' — the ism maf'ul of فَسَّرَ on مُفَعَّل.",
      "Ma'tûf, merfû — «فَسَّرَ»nin MÜFA''AL vezninde ism-i mef'ûlü.",
      segments=[seg("وَ","wa","conj"), seg("مُفَسَّرٌ","mufassar","noun")]),
  tok("وَمُحْكَمٌ","muhkam","noun",["atf-nasaq","ism-maful","form-iv-verbs"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «أَحْكَمَ» عَلَى مُفْعَلٍ، وَبِهِ تَمَّتِ الْمَرَاتِبُ أَرْبَعًا.",
      "Joined, in raf' — the ism maf'ul of أَحْكَمَ on مُفْعَل, and with it the four degrees are complete.",
      "Ma'tûf, merfû — «أَحْكَمَ»nin MUF'AL vezninde ism-i mef'ûlü; mertebeler bununla dörde tamamlanır.",
      punct=".", segments=[seg("وَ","wa","conj"), seg("مُحْكَمٌ","muhkam","noun")]),
 ],
 "jumal": [J("اللَّفْظُ … أَرْبَعَةٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "So the manifest is that whose intended sense shows by the very hearing of it, with no reflection.",
 "tr": "Zâhir, murâdı sırf işitmekle, hiç düşünmeye gerek kalmadan ortaya çıkandır."},
 "tokens": [
  tok("فَالظَّاهِرُ","zahir","noun",["mubtada-khabar","atf-nasaq"],
      "الْفَاءُ عَاطِفَةٌ لِلتَّفْصِيلِ، وَ«الظَّاهِرُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A fa joining for detail; «the manifest» is the mubtada in raf'.",
      "Tafsîl için âtıfa fâ; «الظَّاهِرُ» merfû mübtedâdır.",
      segments=[seg("فَ","fa","conj"), seg("الظَّاهِرُ","zahir","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَهُوَ الْحَدُّ فِي كُلِّ الْأَقْسَامِ الْأَرْبَعَةِ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar — and it opens the definition of all four kinds alike.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur — dört kısmın tarifi de onunla açılır."),
  tok("ظَهَرَ","zahara","verb",["fail","jumla-sifa"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا — وَفَاعِلُهُ مَذْكُورٌ بَعْدَهُ، بِخِلَافِ الصِّلَاتِ السَّابِقَةِ.",
      "A past verb; the clause is the sila of the relative and has no position in i'rab. Its fa'il is NAMED after it, unlike the silas of the chapter before, where the fa'il was a hidden pronoun going back to «ma».",
      "Mâzî fiil; cümle ism-i mevsûlün sılasıdır ve mahalsizdir. Fâili — önceki bâbın sılalarının aksine — açıkça zikredilmiştir; orada fâil «مَا»ya râci müstetir zamîrdi."),
  tok("الْمُرَادُ","murad","noun",["fail","ism-maful","form-iv-verbs"],
      "فَاعِلٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ «أَرَادَ»، وَهُوَ أَجْوَفُ فَجَاءَ عَلَى «مُفَال» بَعْدَ الْإِعْلَالِ.",
      "The fa'il in raf' — the ism maf'ul of أَرَادَ. The root is hollow, so the shape comes out مُفَال after the i'lal has run, not *مُرْوَد.",
      "Merfû fâil — «أَرَادَ»nin ism-i mef'ûlü. Kök ecvef olduğu için i'lâlden sonra *مُرْوَد değil «مُفَال» şeklinde gelmiştir."),
  tok("مِنْهُ","min","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ظَهَرَ»، وَالْهَاءُ عَائِدَةٌ عَلَى «مَا» — وَبِهَذَا الْعَائِدِ ارْتَبَطَتِ الصِّلَةُ بِمَوْصُولِهَا.",
      "A jarr-majrur attaching to «shows», and the HA goes back to «that which». This returning pronoun is what ties the sila to its relative — a sila without one is not a sila.",
      "«ظَهَرَ»ye taalluk eden câr-mecrûr; HÂ «مَا»ya râcidir. Sılayı mevsûlüne bağlayan âid zamîr budur — âidsiz sıla, sıla olmaz.",
      segments=[seg("مِنْ","min","prep"), seg("هُ","pron-3ms","pron")]),
  tok("بِنَفْسِ","nafs","noun",["huruf-jarr","idafa-definiteness","tawkid"],
      "الْبَاءُ لِلسَّبَبِيَّةِ، وَ«نَفْسِ» مَجْرُورٌ بِهَا وَهُوَ مُضَافٌ — وَأُتِيَ بِهَا لِلْحَصْرِ: بِالسَّمَاعِ وَحْدَهُ.",
      "The BA of cause, and «the very» in jarr after it and a mudaf. It is brought for restriction: by the hearing ALONE, with nothing else added.",
      "Sebebiyye bâsı; «نَفْسِ» onunla mecrûr ve muzâftır. Hasr için getirilmiştir: yalnızca işitmekle, başka hiçbir şey katılmadan.",
      segments=[seg("بِ","bi","prep"), seg("نَفْسِ","nafs","noun")]),
  tok("السَّمَاعِ","samaa","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «سَمِعَ».",
      "The mudaf ilayh in jarr — the masdar of سَمِعَ.",
      "Mecrûr muzâfun ileyh — «سَمِعَ»nin masdarı."),
  tok("مِنْ","min","prep",["huruf-jarr","hal"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنَ «الْمُرَادُ».",
      "A jarr letter; the phrase is a hal from «the intended sense».",
      "Cer harfi; câr-mecrûr «الْمُرَادُ»dan hâldir."),
  tok("غَيْرِ","ghayr","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِـ«مِنْ» وَهُوَ مُضَافٌ — وَ«غَيْر» لَا تَتَعَرَّفُ بِالْإِضَافَةِ لِأَنَّهَا شَدِيدَةُ الْإِبْهَامِ.",
      "In jarr after «min», and a mudaf — and «ghayr» never becomes definite by its idafa, however definite the noun after it, because it is too vague in itself to be pinned down.",
      "«مِنْ» ile mecrûr ve muzâf — «غَيْر», kendisinden sonraki isim ne kadar marife olursa olsun izâfetle marife olmaz; zira kendisi şiddetli ibhâm taşır."),
  tok("تَأَمُّلٍ","taammul","noun",["idafa-definiteness","masdar","form-v-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «تَأَمَّلَ» عَلَى تَفَعُّلٍ، وَبِهَذَا الْقَيْدِ فَارَقَ الظَّاهِرُ مَا يَحْتَاجُ إِلَى نَظَرٍ.",
      "The mudaf ilayh in jarr — the masdar of تَأَمَّلَ on تَفَعُّل, and this is the clause that separates the manifest from anything needing thought to reach.",
      "Mecrûr muzâfun ileyh — «تَأَمَّلَ»nin TEFA''UL vezninde masdarı; zâhiri, ulaşmak için düşünmeye muhtaç olandan ayıran kayıt budur.",
      punct="."),
 ],
 "jumal": [J("الظَّاهِرُ مَا ظَهَرَ الْمُرَادُ مِنْهُ",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir."),
  J("ظَهَرَ الْمُرَادُ مِنْهُ",
   "جُمْلَةٌ فِعْلِيَّةٌ صِلَةُ الْمَوْصُولِ — لَا مَحَلَّ لَهَا.",
   "A verbal clause, the sila of the relative — i'rabless.",
   "İsm-i mevsûlün sılası olan fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "And the explicit is that which has grown clearer than the manifest by a sense coming from the speaker.",
 "tr": "Nass, mütekellimden gelen bir mânâ ile zâhirden daha vâzıh hâle gelendir."},
 "tokens": [
  tok("وَالنَّصُّ","nass","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«النَّصُّ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the explicit» is the mubtada in raf'.",
      "Atıf vâvı; «النَّصُّ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("النَّصُّ","nass","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ازْدَادَ","izdada","verb",["fail","jumla-sifa","form-viii-verbs","hollow-verbs"],
      "فِعْلٌ مَاضٍ، فَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ عَائِدٌ عَلَى «مَا» — وَالْجُمْلَةُ صِلَةٌ. وَهُوَ مِنْ «ز ي د» عَلَى افْتِعَالٍ: أُبْدِلَتْ تَاؤُهُ دَالًا لِوُقُوعِهَا بَعْدَ الزَّايِ، ثُمَّ أُعِلَّ أَجْوَفُهُ فَصَارَ «ازْدَادَ».",
      "A past verb with a hidden pronoun for its fa'il going back to «that which»; the clause is the sila. It is ز ي د run through اِفْتِعَال, and TWO rules fire in it: the ta of the pattern turns into a DAL after a zay — اِزْتَادَ becomes اِزْدَادَ — and then the hollow middle melts into an alif. Note that the dal does NOT swallow the zay: they are different letters, so both stand. Where the two do come out the same, as in اِطَّلَعَ and اِدَّعَى, they run together.",
      "Mâzî fiil; fâili «مَا»ya râci müstetir zamîrdir, cümle sıladır. «ز ي د» kökünün İFTİÂL vezni olup içinde İKİ kaide birden işler: vezindeki tâ, zâdan sonra geldiği için DÂLa kalbedilir — اِزْتَادَ, اِزْدَادَ olur — sonra ecvefi i'lâl edilip orta harf elife dönüşür. Dikkat: dâl, zâyı yutmaz; iki ayrı harftir, ikisi de durur. İkisi aynı çıktığında ise — اِطَّلَعَ، اِدَّعَى gibi — birbirine idgâm edilir."),
  tok("وُضُوحًا","wuduh","noun",["tamyiz","masdar"], *TAMYIZ),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ازْدَادَ» — وَ«عَلَى» هُنَا لِلْمُفَاضَلَةِ.",
      "A jarr-majrur attaching to «has grown» — and «ala» here marks the thing surpassed.",
      "«ازْدَادَ»ya taalluk eden câr-mecrûr — buradaki «عَلَى» üstünlük (mufâdale) içindir."),
  tok("الظَّاهِرِ","zahir","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» — وَبِذِكْرِهِ صَارَ الْحَدُّ سُلَّمًا: كُلُّ مَرْتَبَةٍ هِيَ الَّتِي قَبْلَهَا وَزِيَادَةٌ.",
      "In jarr after «ala» — and by naming it the definition becomes a LADDER: each degree is the one before it plus something. The four are not four separate things but one thing measured.",
      "«عَلَى» ile mecrûr — onun zikriyle tarif bir MERDİVENE dönüşür: her mertebe, kendinden öncekinin üstüne bir ziyâdedir. Dört ayrı şey değil, ölçülen tek bir şeydir."),
  tok("بِمَعْنًى","mana","noun",["huruf-jarr","ism-maqsur-manqus"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ازْدَادَ»، وَ«مَعْنًى» مَقْصُورٌ نَكِرَةٌ جُرَّ بِكَسْرَةٍ مُقَدَّرَةٍ وَكُتِبَ تَنْوِينُهُ فَتْحَةً عَلَى الْأَلِفِ.",
      "A jarr-majrur attaching to «has grown», and «a sense» is an indefinite maqsur: its jarr is a kasra that cannot be written, and its tanwin is written as a fathatan on the alif, exactly as it was in the chapter before.",
      "«ازْدَادَ»ya taalluk eden câr-mecrûr; «مَعْنًى» nekre maksûrdur: ceri takdîrî kesradır ve tenvîni, bir önceki bâbdaki gibi, elif üzerine fethatan olarak yazılır.",
      segments=[seg("بِ","bi","prep"), seg("مَعْنًى","mana","noun")]),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِابْتِدَاءِ الْغَايَةِ — وَفُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter for the start of the span — its nun takes a fatha because two sukuns met.",
      "İbtidâ-i gāye için cer harfi — iki sâkin karşılaştığı için nûnu fetha almıştır."),
  tok("الْمُتَكَلِّمِ","mutakallim","noun",["huruf-jarr","ism-fail","form-v-verbs"],
      "مَجْرُورٌ بِـ«مِنْ» — اسْمُ فَاعِلٍ مِنْ «تَكَلَّمَ»، وَبِهِ خَرَجَ مَا زَادَ وُضُوحُهُ بِقَرِينَةٍ مِنْ خَارِجٍ.",
      "In jarr after «min» — the ism fa'il of تَكَلَّمَ, and by it whatever grew clearer from an OUTSIDE indication is shut out. The extra clearness of a nass must come from the speaker himself.",
      "«مِنْ» ile mecrûr — «تَكَلَّمَ»nin ism-i fâili; onunla, vuzûhu HARİCÎ bir karîneyle artan şey dışarıda kalır. Nassın fazla vuzûhu mütekellimin kendisinden gelmelidir.",
      punct="."),
 ],
 "jumal": [J("النَّصُّ مَا ازْدَادَ وُضُوحًا",
   "جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A nominal clause — i'rabless.",
   "İsim cümlesi — mahalsizdir.")]})

S.append({"id": "s4", "translation": {
 "en": "And the expounded is that which has grown clearer than the explicit, so that the door of interpretation is shut.",
 "tr": "Müfesser, nasstan daha vâzıh hâle gelip te'vîl kapısı kapanandır."},
 "tokens": [
  tok("وَالْمُفَسَّرُ","mufassar","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُفَسَّرُ» مُبْتَدَأٌ مَرْفُوعٌ.",
      "A joining waw; «the expounded» is the mubtada in raf'.",
      "Atıf vâvı; «الْمُفَسَّرُ» merfû mübtedâdır.",
      segments=[seg("وَ","wa","conj"), seg("الْمُفَسَّرُ","mufassar","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ازْدَادَ","izdada","verb",["fail","jumla-sifa","form-viii-verbs","hollow-verbs"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — وَتَكْرَارُ الْفِعْلِ نَفْسِهِ فِي الْحُدُودِ الثَّلَاثَةِ مَقْصُودٌ.",
      "A past verb; the clause is the sila. The SAME verb in all three remaining definitions is deliberate: it is what makes the four a ladder rather than a list.",
      "Mâzî fiil; cümle sıladır. Kalan üç tarifte de AYNI fiilin tekrarı kasıtlıdır: dördü bir liste değil bir merdiven yapan şey budur."),
  tok("وُضُوحًا","wuduh","noun",["tamyiz","masdar"], *TAMYIZ),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ازْدَادَ» لِلْمُفَاضَلَةِ.",
      "A jarr-majrur attaching to «has grown», marking the thing surpassed.",
      "«ازْدَادَ»ya taalluk eden, mufâdale bildiren câr-mecrûr."),
  tok("النَّصِّ","nass","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» — وَالْمَرْتَبَةُ الْمَقِيسُ عَلَيْهَا هِيَ الَّتِي سَبَقَتْ لَا الْأُولَى.",
      "In jarr after «ala» — and the rung being measured against is the one just before, not the first. The ladder is climbed one step at a time.",
      "«عَلَى» ile mecrûr — ölçü alınan mertebe, birincisi değil hemen öncekidir. Merdiven basamak basamak çıkılır."),
  tok("بِحَيْثُ","hayth","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«حَيْثُ» ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ، وَهُوَ مُضَافٌ إِلَى جُمْلَةٍ.",
      "The BA is a jarr letter, and «haythu» is an adverb FIXED on the damma, in the position of jarr — and it is a mudaf to a whole SENTENCE. Most nouns take a noun for their mudaf ilayh; haythu takes a clause, and is one of the very few words that does.",
      "BÂ cer harfidir; «حَيْثُ» damme üzere MEBNÎ zarftır, mahallen mecrûrdur ve bir CÜMLEye muzâftır. Çoğu ismin muzâfun ileyhi isimdir; «حَيْثُ» ise cümleye muzâf olur ve bunu yapan pek az kelimeden biridir.",
      segments=[seg("بِ","bi","prep"), seg("حَيْثُ","hayth","noun")]),
  tok("انْسَدَّ","insadda","verb",["fail","doubled-verbs","form-vii-verbs"],
      "فِعْلٌ مَاضٍ مِنْ «اِنْفَعَلَ» — مُضَاعَفٌ الْتَقَى فِيهِ الْمِثْلَانِ فَأُدْغِمَ الْأَوَّلُ فِي الثَّانِي، وَأَصْلُهُ «انْسَدَدَ». وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «حَيْثُ» إِلَيْهَا.",
      "A past verb on اِنْفَعَلَ — a DOUBLED root whose two identical letters have met and been run together; its origin is انْسَدَدَ, and the uncontracted form comes back the moment a sukun-bearing ending follows (انْسَدَدْتُ). The clause is in the position of jarr, because haythu is added to it.",
      "«اِنْفَعَلَ» vezninde mâzî fiil — MUZÂAF olup iki misli karşılaşmış ve birincisi ikinciye idgâm edilmiştir; aslı «انْسَدَدَ»dir ve sâkin bir ek gelir gelmez fek hâli geri döner (انْسَدَدْتُ). Cümle, «حَيْثُ» ona muzâf olduğu için mahallen mecrûrdur."),
  tok("بَابُ","bab","noun",["fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَاسْتِعَارَةُ «الْبَابِ» لِلتَّأْوِيلِ مَقْصُودَةٌ: مَا انْسَدَّ لَا يُدْخَلُ مِنْهُ.",
      "The fa'il in raf', and a mudaf. Calling interpretation a DOOR is a deliberate figure: a door that is shut is not a door you may still knock at.",
      "Merfû fâil ve muzâf. Te'vîle «kapı» denmesi kasıtlı bir istiâredir: kapanan kapıdan girilmez.",),
  tok("التَّأْوِيلِ","tawil","noun",["idafa-definiteness","masdar","form-ii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ «أَوَّلَ» عَلَى تَفْعِيلٍ، وَهُوَ صَرْفُ اللَّفْظِ عَنْ ظَاهِرِهِ بِدَلِيلٍ.",
      "The mudaf ilayh in jarr — the masdar of أَوَّلَ on تَفْعِيل: turning a wording away from its plain sense on the strength of an indication. It is the same root that gave الْمُؤَوَّل in the chapter before.",
      "Mecrûr muzâfun ileyh — «أَوَّلَ»nin TEF'ÎL vezninde masdarı: bir delile dayanarak lafzı zâhirinden çevirmek. Bir önceki bâbdaki «الْمُؤَوَّل»in kökünün aynısıdır.",
      punct="."),
 ],
 "jumal": [J("انْسَدَّ بَابُ التَّأْوِيلِ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ لِـ«حَيْثُ».",
   "A verbal clause in the position of jarr, the mudaf ilayh of «haythu».",
   "«حَيْثُ»un muzâfun ileyhi olarak mahallen mecrûr fiil cümlesi.")]})

S.append({"id": "s5", "translation": {
 "en": "And the firm is that which has grown clearer than the expounded, so that it does not admit abrogation.",
 "tr": "Muhkem, müfesserden daha vâzıh hâle gelip nesih ihtimâli taşımayandır."},
 "tokens": [
  tok("وَالْمُحْكَمُ","muhkam","noun",["atf-nasaq","mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْمُحْكَمُ» مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ آخِرُ الْمَرَاتِبِ.",
      "A joining waw; «the firm» is the mubtada in raf' — the last of the degrees.",
      "Atıf vâvı; «الْمُحْكَمُ» merfû mübtedâdır — mertebelerin sonuncusudur.",
      segments=[seg("وَ","wa","conj"), seg("الْمُحْكَمُ","muhkam","noun")]),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A relative noun, fixed in form, in the position of raf' as the khabar.",
      "Mebnî ism-i mevsûl; haber olarak mahallen merfûdur."),
  tok("ازْدَادَ","izdada","verb",["fail","jumla-sifa","form-viii-verbs","hollow-verbs"],
      "فِعْلٌ مَاضٍ وَالْجُمْلَةُ صِلَةٌ — وَهَذِهِ الْمَرَّةُ الثَّالِثَةُ، وَبِهَا تَمَّ السُّلَّمُ.",
      "A past verb; the clause is the sila — the third time, and with it the ladder is complete.",
      "Mâzî fiil; cümle sıladır — üçüncü defadır ve merdiven bununla tamamlanır."),
  tok("وُضُوحًا","wuduh","noun",["tamyiz","masdar"], *TAMYIZ),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«ازْدَادَ» لِلْمُفَاضَلَةِ.",
      "A jarr-majrur attaching to «has grown», marking the thing surpassed.",
      "«ازْدَادَ»ya taalluk eden, mufâdale bildiren câr-mecrûr."),
  tok("الْمُفَسَّرِ","mufassar","noun",["huruf-jarr"],
      "مَجْرُورٌ بِـ«عَلَى» — وَهُوَ الدَّرَجَةُ الَّتِي تَلِيهِ مِنْ أَسْفَلَ.",
      "In jarr after «ala» — the rung immediately below.",
      "«عَلَى» ile mecrûr — hemen altındaki basamaktır."),
  tok("بِحَيْثُ","hayth","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«حَيْثُ» ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ مُضَافٌ إِلَى الْجُمْلَةِ بَعْدَهُ.",
      "The BA is a jarr letter, and «haythu» an adverb fixed on the damma, added to the clause after it.",
      "BÂ cer harfi; «حَيْثُ» damme üzere mebnî zarftır, sonrasındaki cümleye muzâftır.",
      segments=[seg("بِ","bi","prep"), seg("حَيْثُ","hayth","noun")]),
  # Deliberately NOT tagged la-nafiya-lil-jins: that lا governs NOUNS and puts
  # them in nasb, and opening its note here would teach the wrong thing about
  # the word on the page. A general note is better than a wrong one.
  tok("لَا","la-nafiya","part",["mudari-marfu"],
      "«لَا» نَافِيَةٌ لَا عَمَلَ لَهَا فِي الْفِعْلِ — تَنْفِي وَلَا تُغَيِّرُ إِعْرَابَ مَا بَعْدَهَا.",
      "«La» here simply DENIES and governs nothing: the verb after it keeps the raf' it would have had anyway. It is neither the la that puts a mudari into jazm nor the one that denies a whole genus.",
      "Buradaki «لَا» yalnızca NEFYEDER, amel etmez: sonrasındaki fiil zaten alacağı ref'i korur. Ne muzâriyi cezm eden lâdır ne de cinsi nefyeden."),
  tok("يَحْتَمِلُ","ihtamala","verb",["mudari-marfu","form-viii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ، فَاعِلُهُ ضَمِيرٌ مُسْتَتِرٌ — عَلَى افْتِعَالٍ مِنْ «ح م ل»، وَتَاؤُهُ سَالِمَةٌ لِأَنَّ الْحَاءَ لَيْسَتْ مِنْ حُرُوفِ الْإِبْدَالِ.",
      "A mudari in raf' by the damma, with a hidden pronoun for its fa'il — ح م ل on اِفْتِعَال, and its TA stands unchanged, because the ha is not one of the letters that force the ibdal. Set it beside اِزْدَادَ in the same chapter and the rule shows itself: the ta changes only after certain letters, and stays put after all the rest.",
      "Damme ile merfû muzâri, fâili müstetir zamîr — «ح م ل» kökünün İFTİÂL vezni; TÂsı olduğu gibi kalmıştır, zira HÂ ibdâl harflerinden değildir. Aynı bâbdaki «اِزْدَادَ» ile yan yana koy, kaide kendini göstersin: tâ yalnız belli harflerden sonra değişir, kalan bütün harflerden sonra yerinde durur."),
  tok("النَّسْخَ","naskh","noun",["maful-bihi","masdar"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — مَصْدَرُ «نَسَخَ»: رَفْعُ الْحُكْمِ الشَّرْعِيِّ بِدَلِيلٍ شَرْعِيٍّ مُتَأَخِّرٍ.",
      "The maf'ul bihi in nasb — the masdar of نَسَخَ: the lifting of a legal ruling by a later legal indication. Not admitting it is the highest degree of clearness a wording can reach, and that is why the ladder ends here.",
      "Mansub mef'ûlün bih — «نَسَخَ»nin masdarı: şer'î bir hükmün, sonraki şer'î bir delille kaldırılması. Bunu kabul etmemek, bir lafzın ulaşabileceği en yüksek vuzûh derecesidir; merdivenin burada bitmesinin sebebi budur.",
      punct="."),
 ],
 "jumal": [J("لَا يَحْتَمِلُ النَّسْخَ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ لِـ«حَيْثُ».",
   "A verbal clause in the position of jarr, the mudaf ilayh of «haythu».",
   "«حَيْثُ»un muzâfun ileyhi olarak mahallen mecrûr fiil cümlesi.")]})

GLOSS_ADD = {
 "itibar":     g("اعْتِبَار", "ع ب ر", "noun", "consideration; the criterion a thing is taken by", "itibar; bir şeyin ele alınış ölçüsü", 4),
 "wuduh":      g("وُضُوح", "و ض ح", "noun", "clearness, plainness (masdar)", "vuzûh, açıklık (masdar)", 3),
 "zahir":      g("ظَاهِر", "ظ ه ر", "noun", "the MANIFEST — clear by the hearing alone", "zâhir — sırf işitmekle açık olan", 3),
 "nass":       g("نَصّ", "ن ص ص", "noun", "the EXPLICIT — clearer still, by the speaker's own sense", "nass — mütekellimin mânâsıyla daha da açık olan", 4),
 "mufassar":   g("مُفَسَّر", "ف س ر", "noun", "the EXPOUNDED — clear past interpreting", "müfesser — te'vîle kapalı derecede açık olan", 5),
 "muhkam":     g("مُحْكَم", "ح ك م", "noun", "the FIRM — clear past abrogating", "muhkem — nesih ihtimâli olmayacak kadar açık olan", 5),
 "zahara":     g("ظَهَرَ", "ظ ه ر", "verb", "to appear, to show plainly", "ortaya çıkmak, zâhir olmak", 2),
 "murad":      g("مُرَاد", "ر و د", "noun", "the intended sense (ism maf'ul of أَرَادَ)", "murâd; kastedilen mânâ", 3),
 "samaa":      g("سَمَاع", "س م ع", "noun", "hearing, the act of listening (masdar)", "semâ; işitme (masdar)", 3),
 "taammul":    g("تَأَمُّل", "أ م ل", "noun", "reflection, thinking a thing over (masdar, Form V)", "teemmül; düşünüp taşınma (masdar)", 4),
 "izdada":     g("اِزْدَادَ", "ز ي د", "verb", "to increase, to grow greater", "artmak, ziyâdeleşmek", 4),
 "mutakallim": g("مُتَكَلِّم", "ك ل م", "noun", "the speaker (ism fa'il, Form V)", "mütekellim; konuşan", 3),
 "hayth":      g("حَيْثُ", None, "noun", "in such a way that … (an adverb added to a whole clause)", "öyle ki … (cümleye muzâf olan zarf)", 4),
 "insadda":    g("اِنْسَدَّ", "س د د", "verb", "to be shut, to be closed off", "kapanmak, tıkanmak", 4),
 "bab":        g("بَاب", "ب و ب", "noun", "a door; a chapter", "kapı; bâb", 1, plural="أَبْوَاب"),
 "tawil":      g("تَأْوِيل", "أ و ل", "noun", "interpretation — turning a wording from its plain sense (masdar, Form II)", "te'vîl; lafzı zâhirinden çevirme (masdar)", 5),
 "la-nafiya":  g("لَا (النَّافِيَة)", None, "part", "not (plain denial; governs nothing)", "…değil (sade nefy; amel etmez)", 2),
 "ihtamala":   g("اِحْتَمَلَ", "ح م ل", "verb", "to admit of, to bear (a possibility)", "ihtimâl taşımak, kaldırmak", 4),
 "naskh":      g("نَسْخ", "ن س خ", "noun", "abrogation — the lifting of a ruling by a later one (masdar)", "nesih; hükmün sonraki bir delille kaldırılması", 5),
}

def build_morph():
    """Two verbs COPIED after a lemma-identity check, two built here.

    Copying is the rule wherever the library already carries the verb: a lex key
    is global, and two packages disagreeing about one paradigm is a defect that
    surfaces somewhere else entirely. Generation is for what nothing has yet.
    """
    out = {}
    for lex, src in (("zahara", "aqaid-ahl-al-sunna"), ("izdada", "wasiyyat-abi-hanifa-samti")):
        s = json.loads((ROOT / "content/samples" / src / "morphology.json").read_text(encoding="utf-8"))
        g_ = json.loads((ROOT / "content/samples" / src / "glossary.json").read_text(encoding="utf-8"))
        assert g_["entries"][lex]["lemma"] == GLOSS_ADD[lex]["lemma"], \
            f"{lex}: {src} has {g_['entries'][lex]['lemma']}, we say {GLOSS_ADD[lex]['lemma']}"
        out[lex] = s["verbs"][lex]
    # اِحْتَمَلَ — Form VIII, fully sound: the ha forces no ibdal, so the ta stands.
    out["ihtamala"] = _sg.derived("بَابُ الِافْتِعَالِ: اِفْتَعَلَ يَفْتَعِلُ", "اِفْتَعَلَ يَفْتَعِلُ", "َ",
                                  "اِحْتَمَل", "حْتَمِل", "اِحْتَمِل", "اِحْتِمَال", "مُحْتَمِل",
                                  maful="مُحْتَمَل")
    # اِنْسَدَّ — Form VII of a DOUBLED root. The twins meet and run together; the
    # uncontracted stem survives for every person whose ending brings a sukun,
    # which is exactly where the two dals are pulled apart again.
    G, Sh = "نْسَدّ", "نْسَدِد"
    out["insadda"] = _sg.entry(
        "بَابُ الِانْفِعَالِ: اِنْفَعَلَ يَنْفَعِلُ — مُضَاعَفٌ", "اِنْفَعَلَ يَنْفَعِلُ",
        "اِنْسِدَاد", "مُنْسَدّ",
        _sg.mazi14("اِنْسَدّ", "اِنْسَدَد"), _sg.mudari14("َ", G, Sh),
        ["اِ"+G+"َ", "اِ"+G+"َا", "اِ"+G+"ُوا", "اِ"+G+"ِي", "اِ"+G+"َا", "اِ"+Sh+"ْنَ"],
        "يَ"+G+"َ", "يَ"+G+"َ", "تَ"+G+"َ",
        note="مُضَاعَفٌ مِنَ الِانْفِعَالِ: الْجَزْمُ بِالْفَتْحِ، وَيَجُوزُ الْفَكُّ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/5.json").write_text(
    json.dumps({"chapter": 5, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 5 for c in man["chapters"]):
    man["chapters"].append({"n": 5, "title": TITLE5})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.5.0"
man["subtitle"] = {"ar": "تعريفات أصول الفقه، ثم الأدلة الأربعة، ثم أقسام اللفظ وضعًا ووضوحًا",
                   "en": "The opening definitions, the four sources, then the wording divided twice over — by what it was set down for and by how plainly it shows",
                   "tr": "Açılış tarifleri, dört delil, sonra lafzın iki kere taksîmi — vaz'ına göre ve vuzûhuna göre"}
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("manar ch5:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
