# -*- coding: utf-8 -*-
"""Author chapter 19 of talkhis-al-miftah — تَأْخِيرُ الْمُسْنَدِ وَتَقْدِيمُهُ.

The last of the musnad's states: its postponement (the asl — the musnad
ilayh's mention matters more) and its FRONTING, with the four named
reasons the matn gives for taqdim. As in ch18, the Belagat layer ships as
NAMED jumal rows, not prose:

  • التَّخْصِيصُ وَالْقَصْرُ — لَا فِيهَا غَوْلٌ (Saffat 37:47): the zarf fronted
    to confine — only THERE is no ghawl. And the mirror teaches more than
    the rule: in لَا رَيْبَ فِيهِ (Baqara 2:2) the zarf is NOT fronted,
    because fronting would have implied doubt stands in the other Books.
  • التَّنْبِيهُ أَنَّهُ خَبَرٌ لَا صِفَةٌ — Hassan b. Thabit's لَهُ هِمَمٌ لَا
    مُنْتَهَى لِكِبَارِهَا: front the khabar and no reader can mistake it for
    a sifa, since a sifa never precedes its mawsuf.
  • التَّفَاؤُلُ — سَعِدَتْ بِغُرَّةِ وَجْهِكَ الْأَيَّامُ: the auspicious verb
    brought forward as a good omen.
  • التَّشْوِيقُ إِلَى الْمُسْنَدِ إِلَيْهِ — Muhammad b. Wuhayb's bayt: the
    fronted ثَلَاثَةٌ withholds its subject a whole hemistich, and the
    reveal (شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ) is the payoff.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1545-1566 (sahifa
54-55): Saffat 37:47 and Baqara 2:2 (received text quoted exactly),
Hassan b. Thabit's hemistich, the سَعِدَتْ frame, and Muhammad b. Wuhayb's
bayt in praise of al-Mu'tasim (Abu Ishaq). The Ottoman print's plain-alif
spellings (اِسْحَق) are restored to standard orthography (إِسْحَاق) — a
spelling normalization only.

Grammar this chapter is chosen to teach:
  • note 121 `taqdim-al-musnad` — the four taqdim wujuh + the ta'khir asl
    + the la-order doctrine (fronting past لَا breaks its work).
  • TaqdimEngine (new): the khabar-muqaddam frame and the la-jins frame,
    read exactly off the surface; the semantic wujuh stay a shortlist.
  • engine work the probe forced: the ta-ta'nith bina (سَعِدَتْ was
    «jazm by the sukun»), the propn-first corpus guard (إِسْحَاقَ was an
    إِفْعَال masdar), the clitic-provenance glossary override (وَجْهِكَ
    answered ج ه ك), and the combined clitic+pronoun strip in the noun
    lexicon (لِكِبَارِهَا).
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
def copy_gloss(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/glossary.json").read_text(encoding="utf-8"))["entries"]
    return d[key]
S = []

TITLE19 = {"ar": "تَأْخِيرُ الْمُسْنَدِ وَتَقْدِيمُهُ",
           "en": "The Musnad Postponed and Fronted",
           "tr": "Müsnedin Tehiri ve Takdimi"}

# ---------------------------------------------------------------- s1 — Saffat 47
S.append({"id": "s1", "translation": {
 "en": "No intoxication is in it. (al-Saffat 37:47 — the zarf FRONTED past the la to confine: only in the drink of Paradise is there no ghawl.)",
 "tr": "Onda sersemletme yoktur. (Sâffât 37:47 — zarf, lâ'nın önüne alınmış: yalnız cennet içeceğinde ğavl yoktur — kasr için.)"},
 "tokens": [
  tok("لَا","la-nafiya","part",["taqdim-al-musnad"],
      "نَافِيَةٌ مُلْغَاةٌ — بَطَلَ عَمَلُهَا لِتَقَدُّمِ خَبَرِهَا عَلَيْهَا.",
      "«no» — and here a la whose WORK IS BROKEN: la of the genus governs only when its ism follows it directly, and the fronted khabar has come between. The noun will arrive in RAF' — compare s2, where nothing intervenes and the la builds its ism on the fath.",
      "«yok» — ve burada AMELİ BOZULMUŞ bir lâ: cins lâ'sı ancak ismi hemen ardından gelirse amel eder; öne alınan haber araya girmiştir. İsim REF' ile gelecek — s2 ile karşılaştır: orada araya bir şey girmez ve lâ, ismini fetha üzere bina eder."),
  tok("فِيهَا","fi","part",["taqdim-al-musnad","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ — شِبْهُ جُمْلَةٍ خَبَرٌ مُقَدَّمٌ.",
      "«in it» — the jarr-phrase standing as KHABAR MUQADDAM, and the fronting is the aya's rhetoric: said of the drink of Paradise, «in IT is no ghawl» confines the ghawl-lessness to it — the drinks of this world keep theirs. Fronting the musnad restricts the musnad ilayh to it.",
      "«onda» — HABER-İ MUKADDEM duran câr-mecrûr; ve takdim, âyetin belâgatidir: cennet içeceği için söylenen «ONDA ğavl yok», ğavlsizliği ona hasreder — dünya içecekleri ğavllerini korur. Müsnedi öne almak, müsnedün ileyhi ona kasretmektir.",
      segments=[seg("فِي","fi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("غَوْلٌ","ghawl","noun",["taqdim-al-musnad","mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — وَرَفْعُهُ شَاهِدُ إِلْغَاءِ «لَا».",
      "«ghawl» (the wine's sting: intoxication, headache, harm) — the MUBTADA MU'AKHKHAR, and its visible DAMMA is the receipt of the whole doctrine: had the la still governed, this noun would stand on a bare fatha. The raf' proves the fronting broke the la's work. And a nakira mubtada is licensed exactly here — the fronted jarr-khabar is what permits it.",
      "«ğavl» (içkinin sancısı: sersemletme, baş ağrısı, zarar) — MUAHHAR MÜBTEDÂ; ve görünen DAMMESİ bütün doktrinin makbuzudur: lâ hâlâ amel etseydi bu isim yalın fetha üzre dururdu. Ref', takdimin lâ'nın amelini bozduğunun delilidir. Nekre mübtedâya da tam burada cevaz verilir — öne alınmış câr-mecrûr haber, onun ruhsatıdır.",
      punct=".")],
 "jumal": [
  J("لَا فِيهَا غَوْلٌ",
    "الْوَجْهُ الْأَوَّلُ لِلتَّقْدِيمِ: التَّخْصِيصُ — قَصْرُ الْمُسْنَدِ إِلَيْهِ عَلَى الْمُسْنَدِ.",
    "TAQDIM WAJH 1 — TAKHSIS: fronting فِيهَا confines: no-ghawl-ness belongs to the drink of Paradise ALONE. The order is the meaning: say غَوْلٌ first and the confinement evaporates.",
    "TAKDİM 1. VECİH — TAHSİS: فِيهَا'nın öne alınması hasreder: ğavlsizlik YALNIZ cennet içeceğinindir. Sıra mânânın kendisidir: önce غَوْلٌ de, hasr buharlaşır."),
  J("لَا فِيهَا غَوْلٌ",
    "وَإِلْغَاءُ «لَا»: إِذَا تَقَدَّمَ الْخَبَرُ عَلَيْهَا بَطَلَ عَمَلُهَا وَرُفِعَ الِاسْمُ.",
    "And the nahw under the balagha: la of the genus works only on a noun that follows it DIRECTLY. The fronted khabar voids it — غَوْلٌ takes raf', where s2's رَيْبَ stands on the fath. One doctrine, two ayat, opposite orders.",
    "Ve belâgatin altındaki nahiv: cins lâ'sı ancak HEMEN ardından gelen isimde amel eder. Öne alınan haber onu iptal eder — غَوْلٌ ref' alır; s2'nin رَيْبَ'i ise fetha üzre durur. Tek doktrin, iki âyet, zıt sıralar.")]})

# ---------------------------------------------------------------- s2 — Baqara 2
S.append({"id": "s2", "translation": {
 "en": "There is no doubt in it. (al-Baqara 2:2 — and here the zarf is NOT fronted: «لَا فِيهِ رَيْبٌ» would have implied the doubt stands in the other Books instead.)",
 "tr": "Onda hiçbir şüphe yoktur. (Bakara 2:2 — burada zarf öne ALINMAMIŞTIR: «لَا فِيهِ رَيْبٌ» denseydi şüphenin öteki Kitaplarda bulunduğu îmâ edilirdi.)"},
 "tokens": [
  tok("لَا","la-nafiya-lil-jins","part",["taqdim-al-musnad"],
      "نَافِيَةٌ لِلْجِنْسِ تَعْمَلُ عَمَلَ «إِنَّ» — اسْمُهَا بَعْدَهَا مُبَاشَرَةً.",
      "«no … at all» — la of the GENUS, in full working order this time: its ism follows it with nothing between, so it builds that ism on the fath and denies the whole genus of doubt.",
      "«hiçbir … yok» — CİNS lâ'sı; bu kez ameli tam: ismi araya hiçbir şey girmeden gelir, o ismi fetha üzere bina eder ve şüphe cinsinin tamamını nefyeder."),
  tok("رَيْبَ","rayb","noun",["taqdim-al-musnad"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ.",
      "«doubt» — the ism of la, MABNI ON THE FATH, no tanwin: the visible opposite of s1's غَوْلٌ. Set the two ayat side by side and the whole chapter is in their endings — fatha where the la works, damma where the fronting broke it.",
      "«şüphe» — lâ'nın ismi; FETHA ÜZERE MEBNÎ, tenvinsiz: s1'deki غَوْلٌ'un gözle görülür zıddı. İki âyeti yan yana koy; bütün bâb, sonlarındadır — lâ amel ederken fetha, takdim ameli bozunca damme."),
  tok("فِيهِ","fi","part",["taqdim-al-musnad","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ — خَبَرُ «لَا» غَيْرُ مُقَدَّمٍ.",
      "«in it» — the khabar, left in its place. And the LEAVING is the balagha: front it (لَا فِيهِ رَيْبٌ) and the takhsis of s1 fires — «no doubt in THIS book» — quietly seating the doubt in the other revealed Books. The Qur'an refuses the implication by refusing the fronting. A wajh can be the reason NOT to do a thing.",
      "«onda» — haber, yerinde bırakılmış. Ve BIRAKILIŞ belâgatin kendisidir: öne al (لَا فِيهِ رَيْبٌ) ve s1'in tahsisi ateşlenir — «şüphe yalnız BU kitapta yok» — şüpheyi sessizce öteki indirilmiş Kitaplara oturtur. Kur'ân, îmâyı takdimi reddederek reddeder. Bir vecih, bir şeyi YAPMAMANIN da gerekçesi olabilir.",
      segments=[seg("فِي","fi","prep"), seg("هِ","pron-3ms","pron")],
      punct=".")],
 "jumal": [
  J("لَا رَيْبَ فِيهِ",
    "لَا النَّافِيَةُ لِلْجِنْسِ عَامِلَةٌ: اسْمُهَا مَبْنِيٌّ عَلَى الْفَتْحِ وَخَبَرُهَا شِبْهُ جُمْلَةٍ.",
    "The la-jins frame entire: ism on the fath directly after, the jarr-phrase khabar behind it. This is the ORDER the genus-denial requires — and the frame the TaqdimEngine reads exactly.",
    "Cins-lâ çatısı bütün hâliyle: hemen ardından fetha üzre ismi, arkasında şibh cümle haberi. Cins nefyinin İSTEDİĞİ sıra budur — Takdim motorunun da harfiyen okuduğu çatı."),
  J("لَا رَيْبَ فِيهِ",
    "الْوَجْهُ مِنْ تَرْكِ التَّقْدِيمِ: لِئَلَّا يُوهِمَ ثُبُوتَ الرَّيْبِ فِي سَائِرِ كُتُبِ اللهِ.",
    "The wajh of WITHHELD fronting: لَا فِيهِ رَيْبٌ would confine doubt-lessness to this Book and imply the doubt lives in the others. The musannif teaches taqdim by the one place revelation declined it.",
    "TERK EDİLEN takdimin vechi: لَا فِيهِ رَيْبٌ, şüphesizliği bu Kitab'a hasreder ve şüphenin ötekilerde bulunduğunu îmâ ederdi. Musannif takdimi, vahyin ondan kaçındığı yerle öğretir.")]})

# ---------------------------------------------------------------- s3 — Hassan
S.append({"id": "s3", "translation": {
 "en": "His are aspirations whose great ones have no limit. (Hassan b. Thabit, of the Prophet ﷺ — the khabar fronted so no one reads it as a sifa.)",
 "tr": "Onundur öyle himmetler ki büyüklerinin sınırı yoktur. (Hassân b. Sâbit, Peygamber ﷺ hakkında — haber öne alınmış ki kimse onu sıfat okumasın.)"},
 "tokens": [
  tok("لَهُ","li","part",["taqdim-al-musnad","huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ — خَبَرٌ مُقَدَّمٌ وُجُوبًا.",
      "«his» — لِ opened to لَ before the pronoun; the jarr-phrase as KHABAR MUQADDAM, and here the nahw compels what the balagha chose: the coming mubtada is a NAKIRA, and a nakira may open no sentence — the fronted khabar is its licence.",
      "«onundur» — zamirden önce لِ, لَ'ye açılır; câr-mecrûr HABER-İ MUKADDEM; ve burada nahiv, belâgatin seçtiğini zorunlu kılar: gelecek mübtedâ NEKREdir ve nekre cümle açamaz — öne alınmış haber onun ruhsatıdır.",
      segments=[seg("لَ","li","prep"), seg("هُ","pron-3ms","pron")]),
  tok("هِمَمٌ","himma","noun",["taqdim-al-musnad","mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — نَكِرَةٌ سَوَّغَهَا تَقَدُّمُ الْخَبَرِ.",
      "«aspirations» — the mubtada mu'akhkhar, indefinite and lawful only because the khabar came first. And the ORDER teaches the second wajh: had the poet begun هِمَمٌ لَهُ…, the لَهُ could be read as a sifa of himam. Fronted, it can only be the khabar — a sifa never precedes its mawsuf.",
      "«himmetler» — muahhar mübtedâ; nekredir ve ancak haberin öne geçmesiyle meşrûdur. SIRA ikinci vechi de öğretir: şair هِمَمٌ لَهُ… diye başlasaydı لَهُ, himmetlerin sıfatı okunabilirdi. Öne alınınca yalnız haber olabilir — sıfat, mevsûfundan önce gelmez."),
  tok("لَا","la-nafiya-lil-jins","part",[],
      "نَافِيَةٌ لِلْجِنْسِ — وَالْجُمْلَةُ صِفَةٌ لِهِمَمٌ.",
      "«no … at all» — a second la-jins opens the SIFA clause of himam: aspirations such that their great ones have no limit at all.",
      "«hiçbir … yok» — ikinci bir cins lâ'sı, himmetlerin SIFAT cümlesini açar: öyle himmetler ki büyüklerinin hiçbir sınırı yoktur."),
  tok("مُنْتَهَى","muntaha","noun",["ism-maqsur-manqus"],
      "اسْمُ «لَا» مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ.",
      "«limit, utmost point» — the ism of la, and a maqsur: the fath it is built on is ESTIMATED on the alif that can carry nothing. Form VIII's derived noun (مُنْتَهًى from اِنْتَهَى, root ن ه ي — the nun is the RADICAL and the ta the form's infix, the trap the peel rules fall into without the lexicon).",
      "«son, nihayet» — lâ'nın ismi; ve maksûr: üzerine bina edildiği fetha, hiçbir hareke taşıyamayan elifte TAKDÎR edilir. VIII. bâbın türemiş ismi (اِنْتَهَى'dan مُنْتَهًى; kök ن ه ي — nûn ASIL harftir, tâ bâbın ekidir: sözlük olmadan soyucu kuralların düştüğü tuzak)."),
  tok("لِكِبَارِهَا","kabir","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ خَبَرُ «لَا» — وَ«هَا» مُضَافٌ إِلَيْهِ.",
      "«for its great ones» — لِ + كِبَار (the broken plural of كَبِير) + هَا pointing back at the himam: the jarr-phrase is the la's khabar. Three dresses on one word — clitic, plural, pronoun — and the lexicon must see through all three at once.",
      "«büyükleri için» — لِ + كِبَار (كَبِير'in kırık çoğulu) + himmetlere dönen هَا: câr-mecrûr, lâ'nın haberidir. Tek kelimede üç kıyafet — klitik, çoğul, zamir — ve sözlük üçünü birden delip görmelidir.",
      segments=[seg("لِ","li","prep"), seg("كِبَارِ","kabir","noun"), seg("هَا","pron-3fs","pron")],
      punct=".")],
 "jumal": [
  J("لَهُ هِمَمٌ لَا مُنْتَهَى لِكِبَارِهَا",
    "الْوَجْهُ الثَّانِي لِلتَّقْدِيمِ: التَّنْبِيهُ مِنْ أَوَّلِ الْأَمْرِ أَنَّهُ خَبَرٌ لَا صِفَةٌ.",
    "TAQDIM WAJH 2 — TANBIH: fronted, لَهُ declares itself the khabar from the first word; a sifa cannot stand before its mawsuf. The hearer is never allowed to build the wrong parse.",
    "TAKDİM 2. VECİH — TENBİH: öne alınan لَهُ, ilk kelimeden haber olduğunu ilân eder; sıfat mevsûfunun önünde duramaz. Dinleyenin yanlış kurgu kurmasına hiç izin verilmez."),
  J("لَهُ هِمَمٌ لَا مُنْتَهَى لِكِبَارِهَا",
    "وَالنَّحْوُ تَحْتَهُ: مُبْتَدَأٌ نَكِرَةٌ لَا يَجُوزُ الِابْتِدَاءُ بِهِ إِلَّا مَعَ تَقَدُّمِ الْخَبَرِ.",
    "And the nahw beneath the choice: هِمَمٌ is a nakira, and a nakira mubtada is licensed only under a fronted jarr-khabar — the TAQDIM WAJIB rule. Balagha chose what grammar was about to compel.",
    "Ve seçimin altındaki nahiv: هِمَمٌ nekredir ve nekre mübtedâya ancak öne alınmış câr haber altında cevaz vardır — TAKDÎM-İ VÂCİB kuralı. Belâgat, gramerin zaten zorunlu kılacağını seçmiştir.")]})

# ---------------------------------------------------------------- s4 — tafa'ul
S.append({"id": "s4", "translation": {
 "en": "The days became happy through the radiance of your face. (The auspicious verb fronted — TAFA'UL, the good omen said first.)",
 "tr": "Yüzünün parlaklığıyla günler mesut oldu. (Uğurlu fiil öne alınmış — TEFE'ÜL: hayırlı söz önce söylenir.)"},
 "tokens": [
  tok("سَعِدَتْ","saida","verb",["taqdim-al-musnad"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، وَالتَّاءُ لِلتَّأْنِيثِ — قُدِّمَ لِلتَّفَاؤُلِ.",
      "«became happy» — a madi built on the fatha, the quiet ta marking its subject feminine — a BINA, not jazm: jazm belongs to the mudari and no governor stands here. Fronted for TAFA'UL: begin with سَعِدَ and the omen of happiness falls on the whole utterance before anything else is heard.",
      "«mesut oldu» — fetha üzere mebnî mâzî; sâkin tâ, öznesinin müenneslik alâmeti — bu BİNÂdır, cezm değil: cezm muzâriye âittir ve burada câzim yoktur. TEFE'ÜL için öne alınmıştır: söze سَعِدَ ile başla; saâdet uğuru, daha başka bir şey duyulmadan sözün tamamına düşer."),
  tok("بِغُرَّةِ","ghurra","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«سَعِدَتْ».",
      "«through the radiance» — غُرَّة is the white blaze on a horse's forehead, borrowed for the shining of a noble face; بِ of means, hanging on the verb.",
      "«parlaklığıyla» — غُرَّة, atın alnındaki akıtmadır; asil yüzün parlayışı için ödünç alınmış. Vâsıta بِ'si; fiile bağlanır.",
      segments=[seg("بِ","bi","prep"), seg("غُرَّةِ","ghurra","noun")]),
  tok("وَجْهِكَ","wajh","noun",["tarif-bil-idafa"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ ثَانٍ.",
      "«of your face» — the idafa chain: ghurra → face → you, each link majrur by the one before.",
      "«yüzünün» — izâfet zinciri: gurre → yüz → sen; her halka bir öncekiyle mecrûr.",
      segments=[seg("وَجْهِ","wajh","noun"), seg("كَ","pron-2ms","pron")]),
  tok("الْأَيَّامُ","yawm","noun",["taqdim-al-musnad"],
      "فَاعِلٌ مُؤَخَّرٌ مَرْفُوعٌ.",
      "«the days» — the fa'il, held to the END: the verse keeps the omen first and its doer last, so the fronting of the musnad and the postponing of the musnad ilayh are one gesture.",
      "«günler» — fâil; SONA saklanmış: beyit uğuru önde, fâili sonda tutar — müsnedin takdimi ile müsnedün ileyhin tehiri tek harekettir.",
      punct=".")],
 "jumal": [
  J("سَعِدَتْ بِغُرَّةِ وَجْهِكَ الْأَيَّامُ",
    "الْوَجْهُ الثَّالِثُ لِلتَّقْدِيمِ: التَّفَاؤُلُ — يُفْتَتَحُ الْكَلَامُ بِمَا يُتَيَمَّنُ بِهِ.",
    "TAQDIM WAJH 3 — TAFA'UL: open with the auspicious word. سَعِدَتْ first is a blessing pronounced before it is predicated; the same sentence verb-last would inform without omening.",
    "TAKDİM 3. VECİH — TEFE'ÜL: söze uğurlu kelimeyle başla. Önce سَعِدَتْ demek, yüklem olmadan önce telaffuz edilmiş bir duadır; aynı cümle fiil sonda olsa bildirir ama uğurlamaz."),
  J("سَعِدَتْ بِغُرَّةِ وَجْهِكَ الْأَيَّامُ",
    "وَتَأْخِيرُ الْفَاعِلِ إِلَى آخِرِ الْبَيْتِ مِنْ تَمَامِ الْوَجْهِ.",
    "And the fa'il's postponement completes the wajh: the days arrive last, after the omen and its cause — front and back of the sentence chosen together, the ta'khir asl of this bab serving the taqdim.",
    "Fâilin beytin sonuna tehiri vechi tamamlar: günler en sona, uğurdan ve sebebinden sonra gelir — cümlenin önü ve arkası birlikte seçilmiştir; bâbın tehir aslı, takdime hizmet eder.")]})

# ---------------------------------------------------------------- s5 — the bayt (tashwiq)
S.append({"id": "s5", "translation": {
 "en": "Three things — through their beauty the world shines: the forenoon sun, Abu Ishaq, and the moon. (Muhammad b. Wuhayb praising al-Mu'tasim — the fronted musnad withholds its subject a whole hemistich: TASHWIQ.)",
 "tr": "Üç şey — güzellikleriyle dünya aydınlanır: kuşluk güneşi, Ebû İshâk ve ay. (Muhammed b. Vüheyb, Mu'tasım'ı methediyor — öne alınan müsned, öznesini bir mısra boyunca saklar: TEŞVÎK.)"},
 "tokens": [
  tok("ثَلَاثَةٌ","thalatha","noun",["taqdim-al-musnad","mubtada-khabar"],
      "خَبَرٌ مُقَدَّمٌ مَرْفُوعٌ — قُدِّمَ لِلتَّشْوِيقِ إِلَى الْمُسْنَدِ إِلَيْهِ.",
      "«three» — the MUSNAD, fronted; and the fronting is a delay-fuse: the hearer is told there are three world-brightening things and must wait a whole hemistich to learn WHICH three. TASHWIQ — the longing the order itself manufactures.",
      "«üç» — MÜSNED, öne alınmış; ve takdim bir gecikme fitilidir: dinleyene dünyayı aydınlatan üç şey olduğu söylenir ve HANGİ üç olduğunu öğrenmek için tam bir mısra bekler. TEŞVÎK — sıranın bizzat ürettiği iştiyak."),
  tok("تُشْرِقُ","ashraqa","verb",["mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ صِفَةٌ لِثَلَاثَةٌ.",
      "«shines» — Form IV of ش ر ق (its damma prefix the receipt), and the clause is a SIFA of the three: three-such-that-the-world-shines-by-their-beauty.",
      "«aydınlanır» — ش ر ق'ın IV. bâbı (damme öneki makbuzudur); cümle, üçün SIFATIdır: öyle üç ki güzellikleriyle dünya aydınlanır."),
  tok("الدُّنْيَا","dunya","noun",["ism-maqsur-manqus"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«the world» — the fa'il, its damma estimated on the maqsur alif.",
      "«dünya» — fâil; dammesi maksûr elif üzerinde takdîr edilir."),
  tok("بِبَهْجَتِهَا","bahja","noun",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ، وَ«هَا» عَائِدَةٌ عَلَى الثَّلَاثَةِ.",
      "«by their beauty» — the ha pointing back at the three; the sifa-clause is stitched to its mawsuf by this pronoun.",
      "«güzellikleriyle» — هَا, üçe döner; sıfat cümlesi mevsûfuna bu zamirle dikilir.",
      segments=[seg("بِ","bi","prep"), seg("بَهْجَتِ","bahja","noun"), seg("هَا","pron-3fs","pron")],
      punct="•"),
  tok("شَمْسُ","shams","noun",["taqdim-al-musnad","mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the sun» — the MUBTADA MU'AKHKHAR at last: the reveal the whole first hemistich was built to delay. A mudaf, its tanwin surrendered to the coming idafa.",
      "«güneş» — nihayet MUAHHAR MÜBTEDÂ: ilk mısraın geciktirmek için kurulduğu açılış. Muzâf; tenvinini gelecek izâfete teslim etmiş."),
  tok("الضُّحَى","duha","noun",["tarif-bil-idafa","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ.",
      "«of the forenoon» — mudaf ilayh, its kasra estimated on the maqsur alif: the sun at its clearest hour.",
      "«kuşluğun» — muzâfun ileyh; kesresi maksûr elifte takdîr edilir: güneşin en berrak saati."),
  tok("وَأَبُو","ab","noun",["five-nouns","anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«أَبُو» مَعْطُوفٌ مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ.",
      "«and Abu» — joined to the sun by the waw, and one of the FIVE NOUNS: its raf' is the letter waw itself. The caliph al-Mu'tasim, by his kunya, set between two heavenly lights.",
      "«ve Ebû» — vâvla güneşe atfedilmiş; ve BEŞ İSİMden: ref'i bizzat vâv harfidir. Halife Mu'tasım, künyesiyle, iki gök ışığının arasına oturtulmuş.",
      segments=[seg("وَ","wa","part"), seg("أَبُو","ab","noun")]),
  tok("إِسْحَاقَ","ishaq","propn",["mamnu-min-sarf","tarif-bil-idafa"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
      "«Ishaq» — the mudaf ilayh, and its jarr shows as a FATHA: barred from tanwin for being a name AND foreign (the prophet Isaac's name, Hebrew before it was Arabic). An ajami alam has no Arabic root to dig — the honest answer is the refusal.",
      "«İshâk» — muzâfun ileyh; cerri FETHA ile görünür: hem alem hem YABANCI olduğundan tenvinden men edilmiştir (İshâk peygamberin adı; Arapçadan önce İbrânîce). Acemî alemin kazılacak Arapça kökü yoktur — dürüst cevap, imtinâdır."),
  tok("وَالْقَمَرُ","qamar","noun",["anwa-al-waw"],
      "الْوَاوُ عَاطِفَةٌ، وَ«الْقَمَرُ» مَعْطُوفٌ مَرْفُوعٌ.",
      "«and the moon» — the third of the three, closing the list the fronted ثَلَاثَةٌ promised: sun, caliph, moon — the mamduh seated between the two lights.",
      "«ve ay» — üçün üçüncüsü; öne alınmış ثَلَاثَةٌ'ün vaat ettiği listeyi kapatır: güneş, halife, ay — memdûh iki ışığın arasında.",
      segments=[seg("وَ","wa","part"), seg("الْقَمَرُ","qamar","noun")],
      punct=".")],
 "jumal": [
  J("ثَلَاثَةٌ تُشْرِقُ الدُّنْيَا بِبَهْجَتِهَا شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ",
    "الْوَجْهُ الرَّابِعُ لِلتَّقْدِيمِ: التَّشْوِيقُ إِلَى الْمُسْنَدِ إِلَيْهِ — يُذْكَرُ الْمُسْنَدُ أَوَّلًا وَيُؤَخَّرُ الْمُسْنَدُ إِلَيْهِ إِلَى آخِرِ الْبَيْتِ.",
    "TAQDIM WAJH 4 — TASHWIQ: the musnad first (ثَلَاثَةٌ), the musnad ilayh held to the last breath of the bayt. The hemistich between them is the suspense; the three names are the payoff — and the praised one stands SECOND, framed by sun and moon.",
    "TAKDİM 4. VECİH — TEŞVÎK: müsned önce (ثَلَاثَةٌ), müsnedün ileyh beytin son nefesine saklanır. Aradaki mısra gerilimdir; üç isim ödüldür — ve memdûh, güneşle ayın çerçevelediği İKİNCİ sırada durur."),
  J("شَمْسُ الضُّحَى وَأَبُو إِسْحَاقَ وَالْقَمَرُ",
    "وَتَأْخِيرُ الْمُسْنَدِ أَصْلٌ حَيْثُ كَانَ ذِكْرُ الْمُسْنَدِ إِلَيْهِ أَهَمَّ — وَهُنَا عُكِسَ لِنُكْتَةٍ.",
    "And the bab's other half, the TA'KHIR ASL: the musnad ordinarily comes second because the musnad ilayh's mention matters more. This bayt reverses the asl for a named nukta — which is the whole doctrine of the chapter: departures are licensed by their wujuh, never free.",
    "Ve bâbın öteki yarısı, TEHİR ASLI: müsned normalde ikinci gelir; çünkü müsnedün ileyhin zikri daha mühimdir. Bu beyit aslı, adı konmuş bir nükte için tersine çevirir — bâbın bütün doktrini de budur: sapmalara vecihleri ruhsat verir, asla serbest değildirler.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # copies — a lex key is GLOBAL: entries copied verbatim from their home package
 "himma":    copy_gloss("wasiyyat-abi-hanifa-samti", "himma"),
 "kabir":    copy_gloss("ashab-al-fil", "kabir"),
 "thalatha": copy_gloss("kitab-al-sulh", "thalatha"),
 "dunya":    copy_gloss("bad-al-amali", "dunya"),
 "saida":    copy_gloss("aqaid-ahl-al-sunna", "saida"),
 # NEW this chapter
 "muntaha":  g("مُنْتَهًى", "ن ه ي", "noun", "limit, utmost point (Form VIII derived noun of اِنْتَهَى)",
               "son, nihayet (اِنْتَهَى'nın VIII. bâb türemiş ismi)", 4, form="VIII"),
 "ghurra":   g("غُرَّة", "غ ر ر", "noun", "blaze, radiance (the white on a horse's forehead; a face's shining)",
               "gurre; akıtma, parlaklık (atın alnındaki aklık; yüzün parlayışı)", 4, plural="غُرَر"),
 "ashraqa":  g("أَشْرَقَ", "ش ر ق", "verb", "to shine, to rise radiant (Form IV)",
               "parlamak, ışımak (IV. bâb)", 3, form="IV"),
 "bahja":    g("بَهْجَة", "ب ه ج", "noun", "beauty, splendour, delight", "güzellik, revnak, sevinç", 3),
 "duha":     g("ضُحًى", "ض ح و", "noun", "forenoon, mid-morning brightness", "kuşluk vakti", 3),
 "qamar":    g("قَمَر", "ق م ر", "noun", "moon", "ay", 1, plural="أَقْمَار"),
 "ishaq":    g("إِسْحَاق", None, "propn", "Ishaq (the prophet Isaac; Abu Ishaq is al-Mu'tasim's kunya)",
               "İshâk (İshâk peygamber; Ebû İshâk, Mu'tasım'ın künyesidir)", 3),
}

def build_morph():
    """أَشْرَقَ — Form IV sound of ش ر ق; and سَعِدَ copied from its home package."""
    out = {}
    m = json.loads((ROOT / "content/samples/aqaid-ahl-al-sunna/morphology.json").read_text(encoding="utf-8"))
    out["saida"] = m["verbs"]["saida"]
    out["ashraqa"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَشْرَق", "شْرِق", "أَشْرِق",
                                 "إِشْرَاق", "مُشْرِق", maful="مُشْرَق",
                                 pmz="أُشْرِقَ", pmd="يُشْرَقُ")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/19.json").write_text(
    json.dumps({"chapter": 19, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 19 for c in man["chapters"]):
    man["chapters"].append({"n": 19, "title": TITLE19})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.19.0"
ADD_EN = (" Chapter 19 continues from the same file (lines ~1545-1566, sahifa 54-55): al-Saffat 37:47 and "
          "al-Baqara 2:2 (received text quoted exactly), Hassan b. Thabit's hemistich لَهُ هِمَمٌ لَا مُنْتَهَى لِكِبَارِهَا, "
          "the سَعِدَتْ بِغُرَّةِ وَجْهِكَ الْأَيَّامُ frame, and Muhammad b. Wuhayb's bayt in praise of al-Mu'tasim. The "
          "Ottoman print's plain-alif spellings (اِسْحَق) are restored to standard orthography (إِسْحَاق) — a spelling "
          "normalization only.")
ADD_TR = (" On dokuzuncu bâb aynı dosyadan (satır ~1545-1566, sahife 54-55) devam eder: Sâffât 37:47 ile Bakara 2:2 "
          "(aynen alınmış mervî metin), Hassân b. Sâbit'in لَهُ هِمَمٌ لَا مُنْتَهَى لِكِبَارِهَا mısraı, سَعِدَتْ بِغُرَّةِ "
          "وَجْهِكَ الْأَيَّامُ kalıbı ve Muhammed b. Vüheyb'in Mu'tasım methindeki beyti. Osmanlı baskısının düz elifli "
          "imlâsı (اِسْحَق) standart imlâya (إِسْحَاق) çevrilmiştir — yalnız bir imlâ normalizasyonudur.")
if "1545-1566" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch19:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
