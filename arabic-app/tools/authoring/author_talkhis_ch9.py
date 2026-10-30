# -*- coding: utf-8 -*-
"""Author chapter 9 of talkhis-al-miftah — تَعْرِيفُ الْمُسْنَدِ إِلَيْهِ بِاللَّامِ وَبِالْإِضَافَةِ، وَتَنْكِيرُهُ.

Chapter 8 took two of the six doors to definiteness. This one takes the other
two that carry any weight — the ARTICLE and the IDAFA — and then turns the whole
question round and asks why a subject would be left INDEFINITE at all.

The article is the richest of the four, because أل is not one letter with one
job. It is عَهْدٌ خَارِجِيّ when the thing has already been mentioned, plainly or
by allusion, or is standing there in front of both speakers; عَهْدٌ ذِهْنِيّ when
it has been mentioned nowhere and both minds still know which one is meant
(«go into the market» — which market? the one you would go to); لَامُ الْجِنْس
when the genus itself is the subject; and اسْتِغْرَاق when every individual of
that genus is meant — really every one (عَالِمُ الْغَيْبِ وَالشَّهَادَةِ) or every one
as people ordinarily count them (جَمَعَ الْأَمِيرُ الصَّاغَةَ: every goldsmith in his
own country, not every goldsmith alive).

The iḍāfa is the SHORTEST road to the hearer's mind, and it also carries rank:
عَبْدِي magnifies the annexed-to, عَبْدُ الْخَلِيفَةِ magnifies the annexed, and
وَلَدُ الْحَجَّامِ belittles it — the same construction doing opposite work.

And تَنْكِير is not the absence of a reason. It is ifrād, nawʿiyya, taʿẓīm,
taḥqīr, takthīr, taqlīl — and Abū al-Simṭ's line puts two of them on ONE WORD,
which is why it closes the chapter.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~805-870, which carries
all of it in vowelled Arabic: الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ, اُدْخُلِ السُّوقَ,
al-ʿAsr 103:2, al-Hashr 59:22, جَمَعَ الْأَمِيرُ الصَّاغَةَ, the لَا رَجُلَ / لَا رِجَالَ
pair, the three iḍāfa examples, and Abū al-Simṭ's bayt. Paired examples are
juxtaposed with a full stop between them, as in chapters 5 to 8; nothing is
composed.

Grammar this chapter is chosen to teach:
  • أل FOUR TIMES with four different jobs in five sentences — and the app can
    show the difference nowhere except in the iʿrab, because the letter is
    identical every time. That is the point of the chapter.
  • خَيْرٌ — an ism tafḍīl that has LOST its hamza (أَخْيَر → خَيْر), so a reader
    meets a comparative wearing no comparative shape at all.
  • اُدْخُلِ — the amr on a WASL hamza, mabni on the sukun, its sukun broken to a
    kasra for the meeting of two quiescents with the article that follows.
  • لَفِي — a lam that is NOT a jarr clitic. A jarr letter never governs another
    particle, so this is لَامُ الِابْتِدَاءِ slid onto the khabar (الْمُزَحْلَقَة). The
    analyzer used to call it a jarr clitic over في; this chapter is the fixture
    for the fix.
  • لَا رَجُلَ against لَا رِجَالَ — the singular's istighrāq begins at ONE and the
    plural's at THREE, which is why only the second is deniable when two men
    are in the house.
  • الصَّاغَة — a broken plural whose root is hollow (ص و غ), and whose article
    the root finder was eating as a radical (ل ص غ) until this chapter.
  • حَاجِبٌ twice in one bayt: one tanwin for taʿẓīm and one for taḥqīr, and only
    the MAQAM tells them apart. Nothing on the page does.
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

TITLE9 = {"ar": "تَعْرِيفُ الْمُسْنَدِ إِلَيْهِ بِاللَّامِ وَبِالْإِضَافَةِ، وَتَنْكِيرُهُ",
          "en": "Making the Subject Definite: by the Article and by Annexation — and Leaving it Indefinite",
          "tr": "Müsnedün İleyhin Lâm ve İzâfetle Ma'rife Kılınması — ve Nekre Bırakılması"}

# ---------------------------------------------------------------- s1
# THREE lams, three jobs, one letter. جِنْس، عَهْد ذِهْنِيّ، اِسْتِغْرَاق.
S.append({"id": "s1", "translation": {
 "en": "The male is better than the female. — Go into the market. — Truly the human being is in loss.",
 "tr": "Erkek (cinsi) kadın (cinsin)den daha hayırlıdır. — Çarşıya gir. — Muhakkak ki insan hüsrandadır."},
 "tokens": [
  tok("الرَّجُلُ","rajul","noun",["anwa-al-lam-al-tarif","mubtada-khabar","tarif-al-musnad-ilayh"],
      "مُبْتَدَأٌ مَرْفُوعٌ، وَ«ال» فِيهِ لَامُ الْجِنْسِ — أُشِيرَ بِهَا إِلَى نَفْسِ الْحَقِيقَةِ لَا إِلَى فَرْدٍ مِنْهَا.",
      "The mubtada, in raf' — and its «al» is THE LAM OF THE GENUS: it points at the reality itself, not at any individual wearing it. The sentence is not about a man; it is about manhood. That is why it does not contradict the plain fact that some women are better than some men — the claim was never about individuals at all.",
      "Merfû mübtedâ — ve içindeki «ال», CİNS LÂMIdır: bir ferde değil, hakîkatin kendisine işaret eder. Cümle bir adam hakkında değil, erkeklik hakkındadır. Bâzı kadınların bâzı erkeklerden hayırlı olması hakîkatine aykırı düşmemesinin sebebi de budur — iddia zâten hiçbir ferd hakkında değildi."),
  tok("خَيْرٌ","khayr","noun",["mubtada-khabar","ism-tafdil"],
      "خَبَرٌ مَرْفُوعٌ — وَهُوَ اسْمُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ (أَخْيَرُ ← خَيْرٌ)، وَلِذَلِكَ لَا يَظْهَرُ عَلَيْهِ وَزْنُ أَفْعَلَ.",
      "The khabar, in raf' — and it is an ISM TAFDIL whose hamza has been dropped: أَخْيَرُ became خَيْرٌ. So a comparative arrives wearing none of the shape a comparative is recognised by, and only شَرّ does the same. A reader who looks for أَفْعَل here finds nothing and concludes wrongly that no comparison is being made — the «مِنْ» after it is the proof that one is.",
      "Merfû haber — ve hemzesi düşürülmüş bir İSM-İ TAFDÎLdir: «أَخْيَرُ» iken «خَيْرٌ» olmuştur. Böylece bir üstünlük ismi, tanındığı vezni hiç taşımadan gelir; aynısını yalnız «شَرّ» yapar. Burada «أَفْعَل» arayan okuyucu hiçbir şey bulamaz ve yanlışlıkla mukāyese yok sanır — ardındaki «مِنْ» ise mukāyesenin ispatıdır."),
  tok("مِنَ","min","prep",["huruf-jarr","ism-tafdil"],
      "حَرْفُ جَرٍّ، وَهُوَ الدَّاخِلُ عَلَى الْمُفَضَّلِ عَلَيْهِ، فُتِحَتْ نُونُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter — the one that enters on the thing surpassed, which is what turns any noun into an explicit comparison. Its nun is opened with a fatha for the meeting of two quiescents with the article ahead of it.",
      "Cer harfi — kendisinden üstün tutulanın (müfaddalun aleyh) başına gelen harftir; herhangi bir ismi açık bir mukāyeseye çeviren de odur. Nûnu, önündeki harf-i ta'rîfle iki sâkin buluştuğu için fetha almıştır."),
  tok("الْمَرْأَةِ","imraa","noun",["anwa-al-lam-al-tarif","huruf-jarr"],
      "مَجْرُورٌ بِـ«مِنْ»، وَ«ال» فِيهِ لَامُ الْجِنْسِ أَيْضًا — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«خَيْرٌ».",
      "Majrur by «min», and its «al» is the lam of the genus as well — womanhood answering manhood. The phrase attaches to «better», which is a noun with a verb's force: an ism tafdil governs a jarr the way a verb governs its own.",
      "«مِنْ» ile mecrûr; içindeki «ال» de cins lâmıdır — erkekliğe kadınlık cevap verir. Câr-mecrûr «خَيْرٌ»a taalluk eder: ism-i tafdîl, fiil kuvvetini taşıyan bir isimdir ve fiilin kendi mecrûrunu aldığı gibi alır.",
      punct="."),
  tok("اُدْخُلِ","dakhala","verb",["imperative-amr","anwa-al-lam-al-tarif"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «أَنْتَ». وَهَمْزَتُهُ هَمْزَةُ وَصْلٍ.",
      "An imperative, MABNI on the sukun — and the sukun has been broken to a kasra because the article after it opens on a silent letter and two quiescents will not stand. Its hamza is a hamza of WASL, written اُ and not أُ: it is not part of the word, it is a step to reach the sakin first letter. There is no jazm here and no jazim; the sukun is the bina of the amr.",
      "Emir fiili; SÜKÛN üzere mebnîdir — ve sükûn, ardından gelen harf-i ta'rîf sâkin bir harfle başladığı ve iki sâkin bir araya gelemeyeceği için kesraya çevrilmiştir. Hemzesi VASL hemzesidir; «أُ» değil «اُ» yazılır: kelimenin parçası değil, sâkin ilk harfe ulaşmak için basamaktır. Burada ne cezm vardır ne câzim; sükûn, emrin binâsıdır."),
  tok("السُّوقَ","suq","noun",["anwa-al-lam-al-tarif","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَ«ال» فِيهِ لِلْعَهْدِ الذِّهْنِيِّ — لَا سُوقَ بِعَيْنِهِ جَرَى ذِكْرُهُ، وَلٰكِنَّهُ مَعْلُومٌ فِي الذِّهْنِ بِحَسَبِ الْحَاجَةِ. وَالْمُعَرَّفُ بِهِ كَالنَّكِرَةِ فِي الْمَعْنَى.",
      "The object, in nasb — and its «al» is the article of MENTAL acquaintance. No particular market has been named, and neither speaker could point at one; both nonetheless know which is meant, from the errand. This is the one face of أل that leaves the word INDEFINITE IN MEANING, which is why it may take an indefinite adjective after it — a thing no other definite noun may do.",
      "Mansub mef'ûlün bih — ve içindeki «ال», AHD-İ ZİHNÎ lâmıdır. Muayyen bir çarşının adı geçmemiştir, iki taraf da birini gösteremez; buna rağmen ikisi de yapılacak işe göre hangisi olduğunu bilir. «ال»ın, kelimeyi MÂNÂCA NEKRE bırakan tek yüzü budur — ardından nekre bir sıfat alabilmesinin sebebi de budur; başka hiçbir marife bunu yapamaz.",
      punct="."),
  tok("إِنَّ","inna","part",["inna-wa-akhawatuha"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ، يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ، وَكُسِرَتْ هَمْزَتُهُ لِوُقُوعِهَا فِي الِابْتِدَاءِ.",
      "A letter of emphasis and nasb: it puts its noun in nasb and its khabar in raf'. Its hamza is KASRA'd because the clause stands at the head of the speech — the Qatr al-Nada rule the app teaches under «inna or anna».",
      "Te'kîd ve nasb harfi: ismini nasb, haberini ref' eder. Hemzesi, cümle kelâmın başında bulunduğu için KESRAlıdır — uygulamanın «inne mi enne mi» başlığı altında öğrettiği Katru'n-Nedâ kāidesi."),
  tok("الْإِنْسَانَ","insan","noun",["anwa-al-lam-al-tarif","inna-wa-akhawatuha"],
      "اسْمُ «إِنَّ» مَنْصُوبٌ، وَ«ال» فِيهِ لِلِاسْتِغْرَاقِ — أَيْ كُلُّ إِنْسَانٍ.",
      "The ism of «inna», in nasb — and its «al» is the article of ISTIGHRAQ: every human being, one by one. The lam of the genus and the lam of istighraq are the same letter, and the difference is that the first speaks of the reality and the second of every individual in it. Here the exception that follows (إِلَّا الَّذِينَ آمَنُوا) is itself the proof: you cannot except an individual from a reality, only from a totality.",
      "Mansub «إِنَّ» ismi — ve içindeki «ال» İSTİĞRÂK içindir: her bir insan, tek tek. Cins lâmı ile istiğrâk lâmı aynı harftir; fark, birincisinin hakîkatten, ikincisinin ise ondaki her ferdden bahsetmesidir. Burada ardından gelen istisnâ (إِلَّا الَّذِينَ آمَنُوا) bunun delilidir: bir hakîkatten ferd istisnâ edilmez, ancak bir bütünden edilir."),
  tok("لَفِي","fi","prep",["zarf-mustaqarr-wa-laghw","huruf-jarr"],
      "اللَّامُ لَامُ الِابْتِدَاءِ الْمُزَحْلَقَةُ، وَ«فِي» حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرُ «إِنَّ»، مُتَعَلِّقٌ بِمَحْذُوفٍ، فَهُوَ ظَرْفٌ مُسْتَقَرٌّ.",
      "The lam is the LAM OF IBTIDA, slid forward onto the khabar — الْمُزَحْلَقَة, «the one that was pushed along», because its place was the head of the sentence and إِنَّ took that place, so the two emphases would have collided. It is NOT a jarr clitic: a jarr letter never governs another particle, and في is a particle. The phrase is the khabar of إِنَّ, hanging on an omitted amil, so it is MUSTAQARR — which is exactly what lets a bare jarr phrase serve as a predicate.",
      "Lâm, habere kaydırılmış LÂMÜ'L-İBTİDÂdır — «el-müzahlaka», yani «kaydırılan»; zira yeri cümlenin başıydı, o yeri «إِنَّ» aldı ve iki te'kîd çarpışacaktı. Bir cer öneki DEĞİLDİR: cer harfi başka bir harfi cerretmez, «فِي» ise harftir. Câr-mecrûr «إِنَّ»nin haberidir ve mahzûf bir âmile taalluk eder; bu yüzden MÜSTAKARRdır — çıplak bir câr-mecrûrun haber olabilmesinin sebebi de tam budur.",
      segments=[seg("لَ","lam-ibtida","part"), seg("فِي","fi","prep")]),
  tok("خُسْرٍ","khusr","noun",["huruf-jarr","tankir-al-musnad-ilayh"],
      "مَجْرُورٌ بِـ«فِي» — نَكِرَةٌ لِلتَّعْظِيمِ، أَيْ فِي خُسْرٍ عَظِيمٍ.",
      "Majrur by «fi» — and INDEFINITE for magnification: in a loss whose extent is not stated, and therefore not bounded. Naming it would have measured it. This is the same device the next chapter's حَاجِبٌ uses, met here first on a word that is not the subject.",
      "«فِي» ile mecrûr — ve TA'ZÎM için nekredir: miktarı söylenmemiş, dolayısıyla sınırlanmamış bir hüsranda. Adlandırmak onu ölçerdi. Bu, aynı bâbın sonundaki «حَاجِبٌ»un kullandığı hîlenin ta kendisidir; burada ilk defa, özne olmayan bir kelimede karşılaşılır.",
      punct=".")],
 "jumal": [
  J("الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ",
    "جُمْلَةٌ اسْمِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A nominal sentence standing at the head of the speech — no position in i'rab.",
    "Kelâmın başında duran ibtidâî isim cümlesi — i'râbdan mahalli yoktur."),
  J("اُدْخُلِ السُّوقَ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ طَلَبِيَّةٌ لَا مَحَلَّ لَهَا.",
    "A verbal sentence, and an INSHA of the demanding kind — a command is neither true nor false, so it is outside the khabar/inshaʾ split's first half. No position in i'rab.",
    "Fiil cümlesi ve TALEBÎ bir İNŞÂ — emir ne doğrudur ne yanlış, bu yüzden haber/inşâ taksîminin ilk yarısının dışındadır. İ'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "Knower of the unseen and the witnessed. — The commander gathered the goldsmiths.",
 "tr": "Gaybı ve şehâdeti bilen. — Emîr kuyumcuları topladı."},
 "tokens": [
  tok("عَالِمُ","alim","noun",["ism-fail","idafa-definiteness"],
      "خَبَرٌ لِمُبْتَدَإٍ مَحْذُوفٍ مَرْفُوعٌ، وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ عَلَى فَاعِلٍ، وَعَمَلُهُ عَمَلُ فِعْلِهِ.",
      "The khabar of an omitted mubtada, in raf', and a mudaf — an ism fa'il on فَاعِل, governing what its own verb would govern. It has no tanwin because it is annexed, not because it is definite by itself.",
      "Mahzûf bir mübtedânın merfû haberi ve muzâf — FÂİL vezninde ism-i fâildir ve kendi fiilinin amelini yapar. Tenvîni yoktur; çünkü muzâftır, kendiliğinden marife olduğu için değil."),
  tok("الْغَيْبِ","ghayb","noun",["anwa-al-lam-al-tarif","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَ«ال» فِيهِ لِلِاسْتِغْرَاقِ الْحَقِيقِيِّ — أَيْ كُلُّ غَيْبٍ بِحَسَبِ اللُّغَةِ.",
      "The mudaf ilayh, in jarr — and its «al» is REAL istighraq: every single thing the word covers by the language's own reckoning, with nothing left outside. When the knower is Allah, no other reading is possible, and that is what makes this the textbook example of the kind.",
      "Mecrûr muzâfun ileyh — ve içindeki «ال» HAKÎKÎ istiğrâktır: lügatin kendi ölçüsüyle kelimenin kapsadığı her bir ferd, dışarıda hiçbir şey kalmaksızın. Bilen Allah Teâlâ olunca başka bir okuyuş mümkün değildir; bu nevin ders kitabı misali olmasının sebebi de budur."),
  tok("وَالشَّهَادَةِ","shahada","noun",["atf-nasaq","anwa-al-lam-al-tarif"],
      "مَعْطُوفٌ عَلَى «الْغَيْبِ» مَجْرُورٌ، وَ«ال» فِيهِ لِلِاسْتِغْرَاقِ الْحَقِيقِيِّ كَذَلِكَ.",
      "Joined to «the unseen» and majrur like it, with the same real istighraq. The two words together are a merism: what is hidden and what is seen is everything there is, said as two halves so that the totality is felt rather than asserted.",
      "«الْغَيْبِ»e ma'tûf ve onun gibi mecrûr; «ال»ı da aynı şekilde hakîkî istiğrâk içindir. İki kelime birlikte bir tayy-i cihettir: gizli olan ile görünen, var olanın tamamıdır ve bütünlük iddia edilmek yerine iki yarım hâlinde hissettirilir.",
      segments=[seg("وَ","wa","conj"), seg("الشَّهَادَةِ","shahada","noun")],
      punct="."),
  tok("جَمَعَ","jamaa","verb",["fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "A mazi verb, mabni on the fatha. The sentence is verbal, and the two before it were nominal — the chapter alternates on purpose, because the question it asks (why THIS definiteness?) is indifferent to which kind of sentence the word sits in.",
      "Fetha üzere mebnî mâzî fiil. Bu cümle fiiliyye, öncekiler ismiyyedir — bâb bilerek dönüşümlüdür; zira sorduğu soru (niçin BU ma'rifelik?) kelimenin hangi cins cümlede durduğuna bakmaz."),
  tok("الْأَمِيرُ","amir","noun",["fail","anwa-al-lam-al-tarif"],
      "فَاعِلٌ مَرْفُوعٌ، وَ«ال» فِيهِ لِلْعَهْدِ الْخَارِجِيِّ — أَمِيرٌ بِعَيْنِهِ مَعْلُومٌ لِلْمُتَكَلِّمِ وَالسَّامِعِ.",
      "The fa'il, in raf' — and its «al» is the article of EXTERNAL acquaintance: one particular commander, known to speaker and hearer alike, whether by having been named already, by allusion, or by simply being the commander they both live under.",
      "Merfû fâil — ve içindeki «ال», AHD-İ HÂRİCÎ lâmıdır: muayyen bir emîr; ister daha önce açıkça zikredilmiş, ister kinâye ile geçmiş, isterse yalnızca ikisinin de altında yaşadığı emîr olsun, mütekellim ile sâmi'in ikisince de mâlumdur."),
  tok("الصَّاغَةَ","saigh","noun",["anwa-al-lam-al-tarif","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ، وَ«ال» فِيهِ لِلِاسْتِغْرَاقِ الْعُرْفِيِّ — أَيْ كُلُّ صَائِغٍ فِي مَمْلَكَتِهِ لَا فِي الدُّنْيَا.",
      "The object, in nasb — and its «al» is CUSTOMARY istighraq: every goldsmith in the commander's own country, not every goldsmith alive. Nothing in the letters says so; the reach of a totality is set by what people ordinarily mean, and a commander's reach ends at his border. Note also that الصَّاغَة is a broken plural of صَائِغ with a HOLLOW root (ص و غ) — the waw does not stand in the word, and the app's root finder says so rather than inventing a letter.",
      "Mansub mef'ûlün bih — ve içindeki «ال» ÖRFÎ istiğrâktır: dünyadaki her kuyumcu değil, emîrin kendi memleketindeki her kuyumcu. Harfler bunu söylemez; bir bütünün erimini insanların âdeten kastettiği şey belirler ve bir emîrin erimi sınırında biter. Ayrıca «الصَّاغَة», kökü ECVEF (ص و غ) olan «صَائِغ»in cem-i mükesseridir — vâv kelimede durmaz ve uygulamanın kök bulucusu harf uydurmak yerine bunu söyler.",
      punct=".")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "There is no man at all in the house. — There are no men at all in the house.",
 "tr": "Evde hiçbir adam yoktur. — Evde hiç adamlar yoktur."},
 "tokens": [
  tok("لَا","la-nafiya-lil-jins","part",["la-nafiya-lil-jins"],
      "لَا النَّافِيَةُ لِلْجِنْسِ، تَعْمَلُ عَمَلَ «إِنَّ»: تَنْصِبُ الِاسْمَ وَتَرْفَعُ الْخَبَرَ.",
      "The LA that denies the whole genus, working as «inna» works: nasb on its noun, raf' on its khabar. It is called the la of ISTIGHRAQ for that reason — it is the negative twin of the article this chapter has been walking.",
      "Cinsini nefyeden LÂ; «إِنَّ» gibi amel eder: ismini nasb, haberini ref' eder. Ona İSTİĞRÂK lâsı denmesinin sebebi budur — bu bâbın yürüdüğü harf-i ta'rîfin menfî ikizidir."),
  tok("رَجُلَ","rajul","noun",["la-nafiya-lil-jins","anwa-al-lam-al-tarif"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ — وَاسْتِغْرَاقُ الْمُفْرَدِ يَبْدَأُ مِنَ الْوَاحِدِ، فَلَا يَصِحُّ هٰذَا وَفِي الدَّارِ رَجُلٌ وَاحِدٌ.",
      "The ism of «la», MABNI on the fatha in the position of nasb — and the singular's istighraq begins at ONE. So this sentence is false the moment a single man is in the house. Note also that the la strips the word of its own oneness before entering on it: «لَا رَجُلَ» does not say «not one man», it says «nobody at all», and the word means «every individual», not «the individuals taken together». That is why there is no contradiction in a SINGULAR wearing a totality.",
      "Mahallen mansub, fetha üzere MEBNÎ «لَا» ismi — ve müfredin istiğrâkı BİRden başlar. O hâlde evde tek bir adam bulunduğu anda bu cümle yalan olur. Şuna da dikkat: lâ, kelimenin üzerine ancak ondan VAHDET mânâsı soyulduktan sonra girer; «لَا رَجُلَ» «bir adam değil» demez, «hiç kimse yok» der; ve kelime «ferdlerin tamamı» değil, «her bir ferd» mânâsınadır. Bir MÜFREDin bütünlük taşımasında tenâkuz bulunmamasının sebebi budur."),
  tok("فِي","fi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "A jarr letter of containment.",
      "Zarfiyyet için cer harfi."),
  tok("الدَّارِ","dar","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«فِي» — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرُ «لَا»، مُتَعَلِّقٌ بِمَحْذُوفٍ، فَهُوَ مُسْتَقَرٌّ.",
      "Majrur by «fi» — the phrase standing in the position of raf' as the khabar of «la», hanging on an omitted amil, so it is MUSTAQARR.",
      "«فِي» ile mecrûr — câr-mecrûr, «لَا»nın haberi olarak mahallen merfûdur; mahzûf bir âmile taalluk eder, dolayısıyla MÜSTAKARRdır.",
      punct="."),
  tok("لَا","la-nafiya-lil-jins","part",["la-nafiya-lil-jins"],
      "لَا النَّافِيَةُ لِلْجِنْسِ.",
      "The la that denies the genus, again — the same word, and the difference that follows is entirely in the noun.",
      "Yine cinsini nefyeden LÂ — aynı kelime; ardından gelen fark tamamen isimdedir."),
  tok("رِجَالَ","rajul","noun",["la-nafiya-lil-jins"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ، وَهُوَ جَمْعُ تَكْسِيرٍ — وَاسْتِغْرَاقُ الْجَمْعِ يَبْدَأُ مِنَ الثَّلَاثَةِ.",
      "The ism of «la», mabni on the fatha, and a BROKEN PLURAL — and the plural's istighraq begins at THREE. So with one or two men in the house this sentence is still true while the one before it is false. That difference is the proof the book gives that the singular's istighraq is the wider of the two, and it is a proof you can check by walking into a room.",
      "Fetha üzere mebnî, mahallen mansub «لَا» ismi ve bir CEM-İ MÜKESSER — ve cem'in istiğrâkı ÜÇten başlar. O hâlde evde bir yahut iki adam varken bu cümle hâlâ doğru, öncekiyse yalandır. Kitabın, müfredin istiğrâkının daha şümullü olduğuna getirdiği delil budur — ve bir odaya girerek denetlenebilecek bir delildir."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "A jarr letter.",
      "Cer harfi."),
  tok("الدَّارِ","dar","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "مَجْرُورٌ بِـ«فِي» — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ رَفْعٍ خَبَرُ «لَا»، مُسْتَقَرٌّ.",
      "Majrur by «fi» — the phrase in the position of raf' as the khabar of «la», mustaqarr.",
      "«فِي» ile mecrûr — câr-mecrûr, «لَا»nın haberi olarak mahallen merfûdur; müstakarrdır.",
      punct=".")],
 "jumal": [
  J("لَا رَجُلَ فِي الدَّارِ",
    "جُمْلَةٌ اسْمِيَّةٌ مَنْفِيَّةٌ بِلَا النَّافِيَةِ لِلْجِنْسِ، لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A nominal sentence negated by the la of genus-denial — no position in i'rab.",
    "Cinsini nefyeden lâ ile menfî isim cümlesi — i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "My slave came. — The caliph's slave rode. — The cupper's son is present.",
 "tr": "Kölem geldi. — Halîfenin kölesi bindi. — Hacamatçının oğlu hazırdır."},
 "tokens": [
  tok("عَبْدِي","abd","noun",["tarif-bil-idafa","idafa-definiteness","ya-al-mutakallim"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ، وَهُوَ مُضَافٌ وَالْيَاءُ مُضَافٌ إِلَيْهِ — وَالْإِضَافَةُ هُنَا تَتَضَمَّنُ تَعْظِيمَ الْمُضَافِ إِلَيْهِ، وَهُوَ الْمُتَكَلِّمُ.",
      "The mubtada, in raf' by an ESTIMATED damma: the place is already occupied by the kasra the speaker's ya demands, so the case-vowel cannot appear. It is a mudaf and the ya is its mudaf ilayh — and the annexation carries MAGNIFICATION of the annexed-to, which here is the speaker himself. «My slave came» is a way of saying something about me. Annexing to the speaker or the addressee is also the SHORTEST road to the hearer's mind, which is the first reason the book gives for choosing the idafa at all.",
      "Merfû mübtedâ; refi TAKDÎRÎ bir zamme iledir, zira mahal, mütekellim yâsının gerektirdiği münâsebet kesresiyle meşguldür. Muzâftır, yâ ise muzâfun ileyhtir — ve izâfet burada MUZÂFUN İLEYHin, yani mütekellimin ta'zîmini tazammun eder. «Kölem geldi» demek, benim hakkımda bir şey söylemektir. Mütekellime yahut muhâtaba izâfe, aynı zamanda sâmi'in zihnine giden EN KISA yoldur; kitabın izâfeti seçmek için verdiği ilk sebep de budur.",
      segments=[seg("عَبْدِ","abd","noun"), seg("ي","pron-1s","pron")]),
  tok("حَضَرَ","hadara","verb",["fa-khabar-mubtada"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» — وَالْجُمْلَةُ الْفِعْلِيَّةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "A mazi verb, its fa'il concealed as «he» — and the whole verbal clause stands in the position of raf' as the khabar of the mubtada. A verbal sentence inside a nominal one: this is one of the seven clauses that DO have a position in i'rab.",
      "Mâzî fiil; fâili müstetir «هُوَ»dur — ve bütün fiil cümlesi, mübtedânın haberi olarak mahallen merfûdur. İsim cümlesi içinde bir fiil cümlesi: bu, i'râbdan mahalli OLAN yedi cümleden biridir.",
      punct="."),
  tok("عَبْدُ","abd","noun",["tarif-bil-idafa","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَالْإِضَافَةُ هُنَا تَتَضَمَّنُ تَعْظِيمَ الْمُضَافِ نَفْسِهِ.",
      "The mubtada, in raf' and a mudaf — and here the annexation magnifies the MUDAF itself. The same construction as the sentence before it, doing the opposite work: there the honour fell on the owner, here on the slave, because of who the owner is.",
      "Merfû mübtedâ ve muzâf — ve izâfet burada MUZÂFIN kendisini ta'zîm eder. Bir önceki cümleyle aynı terkîb, zıt işi görüyor: orada şeref sâhibe düşmüştü, burada köleye — sâhibin kim olduğu sebebiyle."),
  tok("الْخَلِيفَةِ","khalifa","noun",["idafa-definiteness","tarif-bil-idafa"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَبِهِ عُرِّفَ الْمُضَافُ، إِذْ لَا يَجْتَمِعُ الْأَلِفُ وَاللَّامُ وَالْإِضَافَةُ.",
      "The mudaf ilayh, in jarr — and it is what made the mudaf definite, since a noun cannot wear both the article and an annexation. Notice the direction of the transfer: definiteness travels FROM the second word TO the first, and so does rank.",
      "Mecrûr muzâfun ileyh — ve muzâfı ma'rife kılan odur; zira bir isimde harf-i ta'rîf ile izâfet birleşmez. Aktarımın yönüne dikkat: ma'rifelik İKİNCİ kelimeden BİRİNCİye geçer, mertebe de öyle."),
  tok("رَكِبَ","rakiba","verb",["fa-khabar-mubtada"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "A mazi verb with a concealed fa'il — the clause standing in the position of raf' as the khabar.",
      "Fâili müstetir mâzî fiil — cümle, haber olarak mahallen merfûdur.",
      punct="."),
  tok("وَلَدُ","walad","noun",["tarif-bil-idafa","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — وَالْإِضَافَةُ هُنَا تَتَضَمَّنُ تَحْقِيرَ الْمُضَافِ.",
      "The mubtada, in raf' and a mudaf — and here the annexation BELITTLES the mudaf. Nothing has changed in the grammar between this sentence and the one before it; what changed is who the second word is. That is the whole claim of the section: an idafa hands its own standing to the word in front of it, upward or downward.",
      "Merfû mübtedâ ve muzâf — ve izâfet burada muzâfı TAHKÎR eder. Bu cümle ile önceki arasında nahiv bakımından hiçbir şey değişmemiştir; değişen, ikinci kelimenin kim olduğudur. Bâbın bütün iddiası da budur: izâfet, kendi mertebesini önündeki kelimeye devreder — yukarı yahut aşağı."),
  tok("الْحَجَّامِ","hajjam","noun",["idafa-definiteness","tarif-bil-idafa"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَلَى وَزْنِ فَعَّالٍ لِلْحِرْفَةِ.",
      "The mudaf ilayh, in jarr — on فَعَّال, the scale of TRADES (خَبَّاز a baker, نَجَّار a carpenter, حَجَّام a cupper). The scale is the same one used for intensives, and only the meaning separates them.",
      "Mecrûr muzâfun ileyh — ZANAAT vezni olan «فَعَّال» üzere (خَبَّاز fırıncı, نَجَّار marangoz, حَجَّام hacamatçı). Vezin, mübâlağa için kullanılanın aynısıdır; ikisini yalnız mânâ ayırır."),
  tok("حَاضِرٌ","hadir","noun",["mubtada-khabar","ism-fail"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ — اسْمُ فَاعِلٍ.",
      "The khabar of the mubtada, in raf' — an ism fa'il. The third sentence returns to a single-word predicate, so that the reader's whole attention falls where the chapter wants it: on the two words of the subject.",
      "Merfû haber — ism-i fâil. Üçüncü cümle tek kelimelik yükleme döner; böylece okuyucunun bütün dikkati bâbın istediği yere, öznenin iki kelimesine düşer.",
      punct=".")]})

# ---------------------------------------------------------------- s5
# أبو السمط's bayt — the SAME word twice, one tanwin for ta'zim and one for tahqir.
S.append({"id": "s5", "translation": {
 "en": "He has a mighty barrier in every affair that would disgrace him — and against one who seeks his bounty he has no barrier at all, not the smallest.",
 "tr": "Onu lekeleyecek her işte, onun için büyük bir engel vardır — fakat ihsan isteyene karşı, en küçük bir engeli bile yoktur."},
 "tokens": [
  tok("لَهُ","li","prep",["zarf-mustaqarr-wa-laghw","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ، مُتَعَلِّقٌ بِمَحْذُوفٍ، فَهُوَ مُسْتَقَرٌّ.",
      "A jarr and its majrur, standing in the position of raf' as a FRONTED khabar, hanging on an omitted amil — mustaqarr. The predicate comes first because the subject is indefinite, and an indefinite may not open a sentence: fronting the khabar is what licenses the indefinite subject that follows.",
      "Câr ve mecrûr; ÖNE ALINMIŞ haber olarak mahallen merfû, mahzûf bir âmile taalluk eder — müstakarrdır. Yüklem öne geçmiştir, çünkü özne nekredir ve nekre cümleye başlayamaz: haberi öne almak, ardından gelen nekre özneyi câiz kılan şeydir.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("حَاجِبٌ","hajib","noun",["tankir-al-musnad-ilayh","mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — نَكِرَةٌ لِلتَّعْظِيمِ، أَيْ حَاجِبٌ عَظِيمٌ.",
      "The DELAYED mubtada, in raf' — and indefinite for MAGNIFICATION: a mighty barrier. Nothing in the word says «mighty»; the maqam does. He is being praised, and what stands between him and disgrace must therefore be great.",
      "GERİYE BIRAKILMIŞ merfû mübtedâ — ve TA'ZÎM için nekredir: büyük bir engel. Kelimede «büyük» diyen hiçbir şey yoktur; bunu makām söyler. Övülen bir kimsedir ve onunla ayıp arasında duran şey, o hâlde büyük olmalıdır."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلظَّرْفِيَّةِ.",
      "A jarr letter of containment.",
      "Zarfiyyet için cer harfi."),
  tok("كُلِّ","kull","noun",["idafa-definiteness","huruf-jarr"],
      "مَجْرُورٌ بِـ«فِي» وَهُوَ مُضَافٌ — وَ«كُلٌّ» مِمَّا يَلْزَمُ الْإِضَافَةَ، فَمَا بَعْدَهُ لَا يَكُونُ إِلَّا اسْمًا.",
      "Majrur by «fi» and a mudaf — and «kull» is one of the nouns that MUST be annexed, so whatever stands after it can only be a noun. The app uses that as a rule: after كُلّ, بَعْض, جَمِيع, غَيْر, مِثْل, the class of the next word is settled by position and no context can put a particle in that seat.",
      "«فِي» ile mecrûr ve muzâf — ve «كُلّ», izâfeti LÂZIM olan isimlerdendir; bu yüzden ardından gelen ancak isim olabilir. Uygulama bunu bir kāide olarak kullanır: «كُلّ، بَعْض، جَمِيع، غَيْر، مِثْل»den sonra, sonraki kelimenin cinsi mevkice belirlenir ve hiçbir bağlam o mevkiye bir harf koyamaz."),
  tok("أَمْرٍ","amr","noun",["idafa-definiteness","tankir-al-musnad-ilayh"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَكِرَةٌ، وَالتَّنْكِيرُ هُنَا لِلْإِبْهَامِ وَالتَّعْمِيمِ مَعَ «كُلٍّ».",
      "The mudaf ilayh, in jarr — indefinite, and the indefiniteness here is for GENERALISING: كُلِّ أَمْرٍ takes in whatever affair may arise, named or unnamed. An idafa to a definite would have narrowed it to affairs already known.",
      "Mecrûr muzâfun ileyh — nekredir ve buradaki nekrelik, «كُلّ» ile birlikte TA'MÎM içindir: «كُلِّ أَمْرٍ», adı konmuş konmamış her işi kapsar. Marifeye izâfet, onu ancak bilinen işlere daraltırdı."),
  tok("يَشِينُهُ","shana","verb",["jumla-sifa","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ تَقْدِيرُهُ «هُوَ» يَعُودُ عَلَى «أَمْرٍ»، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«أَمْرٍ».",
      "A mudari' in raf'; its fa'il is concealed as «it», pointing back at «affair», and the ha is its object — the clause standing in the position of JARR as an adjective of «affair». A clause describing an indefinite is a sifa; describing a definite it would be a hal. The word is spelled with a ya that is a RADICAL (ش ي ن), not a sign of anything.",
      "Merfû muzâri fiil; fâili «أَمْرٍ»a râci müstetir «هُوَ», hâ ise mef'ûlün bihtir — cümle, «أَمْرٍ»in sıfatı olarak mahallen MECRÛRdur. Nekreyi niteleyen cümle sıfat, marifeyi niteleyen hâl olurdu. Kelimedeki yâ ASLÎdir (ش ي ن), bir alâmet değildir.",
      segments=[seg("يَشِينُ","shana","verb"), seg("هُ","pron-3ms","pron")],
      punct="•"),
  tok("وَلَيْسَ","laysa","verb",["kana-wa-akhawatuha","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَيْسَ» فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ يَرْفَعُ الِاسْمَ وَيَنْصِبُ الْخَبَرَ.",
      "The waw joins, and «laysa» is an incomplete JAMID verb — raf' on its noun, nasb on its khabar. Jamid means the paradigm genuinely stops: fourteen mazi cells and nothing else, no mudari', no imperative, no masdar. Its absence is doctrine, not an omission in the data.",
      "Vâv âtıfadır; «لَيْسَ» ise nâkıs ve CÂMİD bir mâzî fiildir: ismini ref', haberini nasb eder. Câmid, çekimin gerçekten durması demektir: on dört mâzî hânesi ve başka hiçbir şey — ne muzâri, ne emir, ne masdar. Yokluğu bir eksiklik değil, bir hükümdür.",
      segments=[seg("وَ","wa","conj"), seg("لَيْسَ","laysa","verb")]),
  tok("لَهُ","li","prep",["zarf-mustaqarr-wa-laghw"],
      "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ نَصْبٍ خَبَرُ «لَيْسَ» مُقَدَّمٌ، مُسْتَقَرٌّ.",
      "A jarr and its majrur, in the position of NASB as the fronted khabar of «laysa» — mustaqarr. The same two letters as the opening of the line, and a different case, because a different governor is over them.",
      "Câr ve mecrûr; «لَيْسَ»nin öne alınmış haberi olarak mahallen MANSUB — müstakarrdır. Mısraın başındaki iki harfin aynısı, fakat başka bir hâl; zira üzerlerinde başka bir âmil vardır.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("عَنْ","an","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ لِلْمُجَاوَزَةِ.",
      "A jarr letter of moving away — «keeping off from».",
      "Mücâveze için cer harfi — «-den uzak tutmak»."),
  tok("طَالِبِ","talib","noun",["ism-fail","idafa-definiteness"],
      "مَجْرُورٌ بِـ«عَنْ» وَهُوَ مُضَافٌ — اسْمُ فَاعِلٍ عَامِلٌ عَمَلَ فِعْلِهِ، فَنَصَبَ… بَلْ أَضَافَ إِلَى مَفْعُولِهِ، وَهِيَ الْإِضَافَةُ اللَّفْظِيَّةُ.",
      "Majrur by «an» and a mudaf — an ism fa'il annexed to its OWN OBJECT. That is the idafa lafziyya: it gives the first word no definiteness at all, only lightness, which is why طَالِبِ الْعُرْفِ stays indefinite in meaning and can be the object of a general statement.",
      "«عَنْ» ile mecrûr ve muzâf — KENDİ MEF'ÛLÜne izâfe edilmiş bir ism-i fâil. Bu, izâfet-i lafziyyedir: birinci kelimeye hiç ma'rifelik vermez, yalnız hafiflik verir; «طَالِبِ الْعُرْفِ»in mânâca nekre kalmasının ve umûmî bir hükmün konusu olabilmesinin sebebi de budur."),
  tok("الْعُرْفِ","urf","noun",["idafa-lafziyya","anwa-al-lam-al-tarif"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَهُوَ فِي الْأَصْلِ مَفْعُولُ «طَالِب» — وَ«ال» فِيهِ لِلْجِنْسِ.",
      "The mudaf ilayh, in jarr — and in origin the OBJECT of «seeker». Its «al» is the lam of the genus: kindness as such, not a particular favour. The chapter's four faces of the article are all now on the page, and this is the fourth appearance of the same two letters doing a fourth job.",
      "Mecrûr muzâfun ileyh — ve aslında «طَالِب»in MEF'ÛLÜdür. «ال»ı cins lâmıdır: muayyen bir ihsan değil, ihsanın kendisi. Bâbın harf-i ta'rîfe âit dört yüzü artık sayfadadır; bu da aynı iki harfin dördüncü işi görüşüdür."),
  tok("حَاجِبٌ","hajib","noun",["tankir-al-musnad-ilayh","kana-wa-akhawatuha"],
      "اسْمُ «لَيْسَ» مُؤَخَّرٌ مَرْفُوعٌ — نَكِرَةٌ لِلتَّحْقِيرِ، أَيْ وَلَا حَاجِبٌ حَقِيرٌ.",
      "The delayed ISM of «laysa», in raf' — and indefinite for BELITTLING: not even the slightest doorkeeper. The same word, the same tanwin, the same line — and the opposite reading, because the first sits in praise of a defence and the second in denial of an obstacle. The maqam decides, and only the maqam. This is the chapter's proof that indefiniteness is a choice with reasons, exactly as definiteness is.",
      "«لَيْسَ»nin geriye bırakılmış merfû İSMİ — ve TAHKÎR için nekredir: en küçük bir engel bile değil. Aynı kelime, aynı tenvîn, aynı beyit — ve zıt bir okuyuş; zira birincisi bir korumanın methinde, ikincisi bir engelin nefyinde durur. Karârı makām verir, yalnız makām. Bâbın, nekreliğin de tıpkı ma'rifelik gibi sebepleri olan bir tercih olduğuna dâir delili budur.",
      punct=".")],
 "jumal": [
  J("لَهُ حَاجِبٌ فِي كُلِّ أَمْرٍ يَشِينُهُ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا مُقَدَّمٌ وَمُبْتَدَؤُهَا مُؤَخَّرٌ نَكِرَةٌ، لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "A nominal sentence with a fronted khabar and a delayed indefinite mubtada — no position in i'rab. Fronting is what makes the indefinite subject lawful.",
    "Haberi öne alınmış, mübtedâsı geriye bırakılmış nekre bir isim cümlesi — i'râbdan mahalli yoktur. Nekre özneyi câiz kılan, takdîmdir."),
  J("يَشِينُهُ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ صِفَةٌ لِـ«أَمْرٍ».",
    "A verbal clause in the position of jarr, an adjective of «affair» — one of the seven clauses that DO carry a position.",
    "«أَمْرٍ»in sıfatı olarak mahallen mecrûr fiil cümlesi — mahalli OLAN yedi cümleden biri."),
  J("وَلَيْسَ لَهُ عَنْ طَالِبِ الْعُرْفِ حَاجِبٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ نَاقِصَةٌ مَعْطُوفَةٌ عَلَى الْجُمْلَةِ الْأُولَى، لَا مَحَلَّ لَهَا.",
    "An incomplete verbal sentence joined to the first — no position in i'rab. Joined clause to clause, so the two readings of حَاجِبٌ are held in one breath.",
    "Birinci cümleye ma'tûf nâkıs fiil cümlesi — i'râbdan mahalli yoktur. Cümle cümleye atfedilmiştir; böylece «حَاجِبٌ»un iki okuyuşu tek nefeste tutulur.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "imraa":     g("اِمْرَأَة", "م ر أ", "noun", "woman", "kadın", 1, plural="نِسَاء"),
 "suq":       g("سُوق", "س و ق", "noun", "market", "çarşı, pazar", 2, plural="أَسْوَاق"),
 "khusr":     g("خُسْر", "خ س ر", "noun", "loss, ruin", "hüsran, ziyan", 3),
 "ghayb":     g("غَيْب", "غ ي ب", "noun", "the unseen", "gayb, görünmeyen", 3),
 "saigh":     g("صَائِغ", "ص و غ", "noun", "goldsmith", "kuyumcu, sâiğ", 4, plural="صَاغَة"),
 "khalifa":   g("خَلِيفَة", "خ ل ف", "noun", "caliph, successor", "halîfe", 2, plural="خُلَفَاء"),
 "hajjam":    g("حَجَّام", "ح ج م", "noun", "cupper, bloodletter (a lowly trade)", "hacamatçı (aşağı görülen bir zanaat)", 4),
 "hajib":     g("حَاجِب", "ح ج ب", "noun", "doorkeeper, chamberlain; a barrier", "kapıcı, hâcib; engel, perde", 3, plural="حُجَّاب"),
 "urf":       g("عُرْف", "ع ر ف", "noun", "kindness, bounty; what is customarily known as good", "ihsan, iyilik; örfen ma'rûf olan", 4),
 "hadara":    g("حَضَرَ", "ح ض ر", "verb", "to be present, to come", "hazır olmak, gelmek", 2, form="I"),
 "lam-ibtida": g("لَ (لَامُ الِابْتِدَاءِ)", None, "part", "the lam of ibtida — emphasis, slid onto the khabar after inna", "lâmü'l-ibtidâ — te'kîd lâmı; inne'den sonra habere kayar (müzahlaka)", 4),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "khayr":     g("خَيْر", "خ ي ر", "noun", "good; better (an ism tafdil with its hamza dropped)", "hayır; daha hayırlı (hemzesi düşmüş ism-i tafdîl)", 1),
 "dar":       g("دَار", "د و ر", "noun", "house, abode", "ev, yurt", 1, plural="دِيَار"),
 "abd":       g("عَبْد", "ع ب د", "noun", "slave, servant", "kul, köle", 1, plural="عِبَاد"),
 "walad":     g("وَلَد", "و ل د", "noun", "child, son", "çocuk, oğul", 1, plural="أَوْلَاد"),
 "shahada":   g("شَهَادَة", "ش ه د", "noun", "witnessing; what is seen", "şehâdet; görünen âlem", 2),
 "kull":      g("كُلّ", "ك ل ل", "noun", "every, all (always a mudaf)", "her, bütün (dâima muzâf)", 1),
 "amr":       g("أَمْر", "أ م ر", "noun", "affair, matter, command", "iş, emir", 1, plural="أُمُور"),
 "inna":      g("إِنَّ", None, "part", "truly, indeed (nasb on its noun, raf' on its khabar)", "muhakkak ki (ismini nasb, haberini ref' eder)", 1),
 "laysa":     g("لَيْسَ", None, "verb", "is not (a jamid, incomplete verb)", "değildir (câmid, nâkıs fiil)", 2, form="I"),
 "dakhala":   g("دَخَلَ", "د خ ل", "verb", "to enter, to go in", "girmek", 1, form="I"),
 "jamaa":     g("جَمَعَ", "ج م ع", "verb", "to gather, to bring together", "toplamak", 1, form="I"),
 "rakiba":    g("رَكِبَ", "ر ك ب", "verb", "to ride, to mount", "binmek", 1, form="I"),
 "shana":     g("شَانَ", "ش ي ن", "verb", "to disgrace, to mar", "lekelemek, ayıplı kılmak", 4, form="I"),
}

def build_morph():
    """Every verb this chapter uses, with its paradigm.

    Five of the six are copied lemma-identical out of packages that already
    carry them — a lex key is global, so the paradigm must be the same object
    wherever the key appears. حَضَرَ is new and is built by the generator.
    """
    out = {}
    for pkg, lex in [("mukhtasar-al-manar", "dakhala"),
                     ("wasiyyat-abi-yusuf-l5", "jamaa"),
                     ("wasiyyat-abi-hanifa-samti", "rakiba"),
                     ("wasiyyat-abi-hanifa-samti", "shana"),
                     ("wasiyyat-abi-yusuf-l5", "laysa")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    # حَضَرَ — Form I sound, bab نَصَرَ.
    out["hadara"] = _sg.sound1("nasara", "حَضَر", "حْضُر", "اُحْضُر", "حُضُور", "حَاضِر",
                               "مَحْضُور", "حُضِرَ", "يُحْضَرُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/9.json").write_text(
    json.dumps({"chapter": 9, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 9 for c in man["chapters"]):
    man["chapters"].append({"n": 9, "title": TITLE9})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.9.0"
ADD_EN = (" Chapter 9 continues from the same file (lines ~805-870), which carries every one of its "
          "examples vowelled: الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ, اُدْخُلِ السُّوقَ, al-'Asr 103:2, al-Hashr 59:22, "
          "جَمَعَ الْأَمِيرُ الصَّاغَةَ, the لَا رَجُلَ / لَا رِجَالَ pair, the three idafa examples "
          "(عَبْدِي حَضَرَ، عَبْدُ الْخَلِيفَةِ رَكِبَ، وَلَدُ الْحَجَّامِ حَاضِرٌ) and Abu al-Simt's bayt.")
ADD_TR = (" Dokuzuncu bâb aynı dosyadan (satır ~805-870) devam eder; o satırlar bâbın bütün "
          "misallerini harekeli olarak taşır: الرَّجُلُ خَيْرٌ مِنَ الْمَرْأَةِ, اُدْخُلِ السُّوقَ, Asr 103:2, Haşr 59:22, "
          "جَمَعَ الْأَمِيرُ الصَّاغَةَ, لَا رَجُلَ / لَا رِجَالَ çifti, üç izâfet misali "
          "(عَبْدِي حَضَرَ، عَبْدُ الْخَلِيفَةِ رَكِبَ، وَلَدُ الْحَجَّامِ حَاضِرٌ) ve Ebü's-Simt'in beyti.")
if "103:2" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch9:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
