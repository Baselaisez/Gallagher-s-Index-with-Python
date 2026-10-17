# -*- coding: utf-8 -*-
"""Author chapter 17 of talkhis-al-miftah — لَوْ، وَحِكَايَةُ الْحَالِ: الزَّمَنُ عَلَى خِلَافِ وَقْتِهِ.

The shart bab closes on لَوْ — the conditional of IMTINA': the shart
certainly did not happen, so the jawab did not either, and BOTH clauses
come as mazi by rule (لَوْ جِئْتَنِي لَأَكْرَمْتُكَ). Then the muṣannif turns the
rule over and teaches its most beautiful violations — the tense used
AGAINST its time, each with a nukta:

  • لَوْ + MUDARI (Hujurat 7) — continuity in the past: had he obeyed you
    time after time…
  • MUDARI where an ism fail was expected (Baqara 15) — the mocking
    renews, again and again.
  • لَوْ + MUDARI (An'am 27) — the scene MADE PRESENT (حِكَايَةُ الْحَالِ):
    the speaker whose word cannot miss shows the future as if you stood
    watching it.
  • MUDARI between two mazis (Fatir 9) — أَرْسَلَ … فَتُثِيرُ: the wondrous
    image of the winds driving the clouds is set playing before the eyes.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1483-1510 (sahifa
52): the matn's frame لَوْ جِئْتَنِي لَأَكْرَمْتُكَ, al-Hujurat 49:7, al-Baqara
2:15, al-An'am 6:27 and Fatir 35:9. The ayat are received text quoted
exactly; the Ottoman print's plain-alif spellings are restored to standard
orthography, a spelling normalization only.

Grammar this chapter is chosen to teach:
  • note 119 `hikayat-al-hal` — law's imtina', and the four licensed
    tense-shifts with their nukat.
  • the ShartEngine (new this version): the conditional frame as an exact
    engine — adat, shart, jawab and its lam/fa, with the tense-nukta named
    where the surface runs against the adat's asl.
  • the engine work the probe forced: إِذْ joining the closed classes as a
    zarf, the derived majhul stepping back over the mazi's group-waw
    (وُقِفُوا), and عَنِتُّمْ's idgham cells stored so لَعَنِتُّمْ reaches its
    paradigm through the jawab's lam.
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

TITLE17 = {"ar": "لَوْ، وَحِكَايَةُ الْحَالِ: الزَّمَنُ عَلَى خِلَافِ وَقْتِهِ",
           "en": "Law, and Hikayat al-Hal: the Tense Against Its Time",
           "tr": "Lev ve Hikâyetü'l-Hâl: Vaktine Aykırı Zaman"}

# ---------------------------------------------------------------- s1 — the matn's frame
S.append({"id": "s1", "translation": {
 "en": "Had you come to me, I would have honored you. (The matn's frame for لَوْ: the coming did NOT happen, so neither did the honoring — both clauses mazi, and the jawab wears its lam.)",
 "tr": "Bana gelmiş olsaydın, sana ikram ederdim. (Metnin لَوْ kalıbı: geliş OLMADI, ikram da olmadı — iki cümle de mâzî; cevap lâmını giyer.)"},
 "tokens": [
  tok("لَوْ","law","part",["in-shartiyya","hikayat-al-hal"],
      "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ — يُقَيِّدُ حُصُولَ الْجَزَاءِ فِي الْمَاضِي بِشَرْطٍ قَطْعِيِّ الِانْتِفَاءِ.",
      "لَوْ — the third conditional, and the strangest: IMTINA' LI-IMTINA', «refusal for refusal». Where إِنْ doubts and إِذَا expects, لَوْ states two certainties at once: the shart certainly did NOT happen, and therefore neither did the jawab. It ties the jazā to its shart in the PAST — which is why, by rule, both clauses come as mazi.",
      "لَوْ — üçüncü şart edatı ve en tuhafı: İMTİNÂ Lİ-İMTİNÂ, «olmadığı için olmadı». إِنْ şüphelenir, إِذَا bekler; لَوْ ise iki kesinliği birden söyler: şart kesinlikle OLMADI, dolayısıyla cevap da olmadı. Cezâyı şartına GEÇMİŞTE bağlar — kāide gereği iki cümlenin de mâzî gelmesi bundandır."),
  tok("جِئْتَنِي","jaa","verb",["ya-al-mutakallim","hikayat-al-hal"],
      "فِعْلُ الشَّرْطِ، مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«had you COME to me» — the shart verb, a mazi as the rule demands; the ta is the doer, and the protective nun shields the verb's ending from the speaker's ya.",
      "«bana GELSEYDİN» — şart fiili; kāidenin istediği gibi mâzî. Tâ fâildir; vikāye nûnu, fiilin sonunu mütekellim yâsından korur.",
      segments=[seg("جِئْ","jaa","verb"), seg("تَ","pron-2ms","pron"), seg("نِ","ni-wiqaya","part"), seg("ي","pron-1s","pron")]),
  tok("لَأَكْرَمْتُكَ","akrama","verb",["form-iv-verbs","hikayat-al-hal"],
      "اللَّامُ وَاقِعَةٌ فِي جَوَابِ لَوْ، وَالْفِعْلُ مَاضٍ، وَالتَّاءُ فَاعِلٌ وَالْكَافُ مَفْعُولٌ بِهِ.",
      "«I would have HONORED you» — the jawab, opening on the lam that لَوْ loves (لَامُ جَوَابِ لَوْ), a Form IV mazi with the speaker's ta as doer and your kaf as object. Both halves of the frame now stand: unreal past against unreal past, the lam marking where the answer begins.",
      "«sana İKRAM EDERDİM» — cevap; لَوْ'in sevdiği lâmla açılır (لَامُ جَوَابِ لَوْ). IV. bâbdan mâzî; konuşanın tâsı fâil, senin kâfın mef'ûl. Kalıbın iki yakası artık tamam: gerçekleşmemiş geçmişe karşı gerçekleşmemiş geçmiş; lâm, cevabın başladığı yeri işaretler.",
      segments=[seg("لَ","lam-jawab","part"), seg("أَكْرَمْ","akrama","verb"), seg("تُ","pron-1s","pron"), seg("كَ","pron-2ms","pron")],
      punct=".")],
 "jumal": [
  J("لَوْ جِئْتَنِي لَأَكْرَمْتُكَ",
    "لَوْ حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ — الشَّرْطُ وَالْجَزَاءُ مَاضِيَانِ عَلَى الْأَصْلِ، وَاللَّامُ فِي الْجَوَابِ.",
    "The asl of لَوْ complete: unreal shart, unreal jawab, both mazi, the lam on the answer.",
    "لَوْ'in aslı tamam: gerçekleşmemiş şart, gerçekleşmemiş cevap, ikisi de mâzî; lâm cevabın üzerinde.")]})

# ---------------------------------------------------------------- s2 — Hujurat 7
S.append({"id": "s2", "translation": {
 "en": "Had he obeyed you in much of the affair, you would surely have come to grief. (al-Hujurat 49:7 — a MUDARI after لَوْ: the obeying is pictured continuing, time after time, in the past.)",
 "tr": "Eğer o, birçok işte size uysaydı, sıkıntıya düşerdiniz. (Hucurât 49:7 — لَوْ'den sonra MUZÂRİ: itaat, geçmişte zaman zaman sürüp gider diye resmedilir.)"},
 "tokens": [
  tok("لَوْ","law","part",["in-shartiyya","hikayat-al-hal"],
      "حَرْفُ امْتِنَاعٍ لِامْتِنَاعٍ.",
      "The law of unreality again — but watch what follows it this time.",
      "Yine imtinâ لَوْ'i — fakat bu kez ardından gelene bak."),
  tok("يُطِيعُكُمْ","ataa","verb",["form-iv-verbs","hikayat-al-hal","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ — عَلَى خِلَافِ الْأَصْلِ بَعْدَ لَوْ — وَ«كُمْ» مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى النَّبِيِّ ﷺ.",
      "«had he OBEYED you» — a MUDARI where لَوْ's rule demands a mazi, and the violation is the teaching: the present tense pictures the obeying as CONTINUING, renewed with every opinion of yours he might have followed — «had he kept obeying you, time after time». Say أَطَاعَكُمْ and one act is denied; the mudari denies a habit.",
      "«size UYSAYDI» — لَوْ'in kāidesi mâzî isterken MUZÂRİ; ve ihlâl, dersin kendisidir: şimdiki kip, itaati SÜREN bir şey olarak resmeder — uyacağı her görüşünüzle yenilenen: «size uya uya gitseydi». أَطَاعَكُمْ de: tek bir iş nefyedilir; muzâri bir âdeti nefyeder.",
      segments=[seg("يُطِيعُ","ataa","verb"), seg("كُمْ","pron-2mp","pron")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«in…» — hanging on the obeying.",
      "«…-de» — itaate bağlanır."),
  tok("كَثِيرٍ","kathir","noun",["huruf-jarr"],
      "اسْمٌ مَجْرُورٌ.",
      "«much» — in jarr under fi.",
      "«birçok» — fî altında mecrûr."),
  tok("مِنَ","min","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ — حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«of» — its nun taking a helping fatha before the article's resting alif.",
      "«…-den» — nûnu, harf-i tarifin sâkin elifinden önce yardımcı fetha alır."),
  tok("الْأَمْرِ","amr","noun",["huruf-jarr"],
      "اسْمٌ مَجْرُورٌ.",
      "«the affair» — closing the phrase: in much of the affair.",
      "«işin» — ibareyi kapatır: işin birçoğunda."),
  tok("لَعَنِتُّمْ","anita","verb",["hikayat-al-hal","doubled-verbs"],
      "اللَّامُ فِي جَوَابِ لَوْ، وَ«عَنِتُّمْ» مَاضٍ مِنْ عَنِتَ — أُدْغِمَتْ تَاءُ الْفِعْلِ فِي تَاءِ الْفَاعِلِ — وَالتَّاءُ فَاعِلٌ.",
      "«you would have COME TO GRIEF» — the jawab with its lam, and a small sarf jewel: عَنِتَ ends in a ta, the subject suffix begins with one, and the two run together under a shadda — عَنِتْتُمْ spoken as عَنِتُّمْ. The shadda on the ta is the receipt of the meeting. And note the frame: the SHART broke the rule (mudari), the JAWAB keeps it (mazi) — each tense chosen for its own message.",
      "«SIKINTIYA DÜŞERDİNİZ» — lâmıyla cevap; ve küçük bir sarf mücevheri: عَنِتَ tâ ile biter, fâil eki tâ ile başlar ve ikisi şedde altında birleşir — عَنِتْتُمْ, söylenişte عَنِتُّمْ. Tâdaki şedde, buluşmanın makbuzudur. Ve çatıya dikkat: ŞART kuralı bozdu (muzâri), CEVAP korudu (mâzî) — her kip kendi mesajı için seçilmiş.",
      segments=[seg("لَ","lam-jawab","part"), seg("عَنِتُّمْ","anita","verb")],
      punct=".")],
 "jumal": [
  J("لَوْ يُطِيعُكُمْ فِي كَثِيرٍ مِنَ الْأَمْرِ لَعَنِتُّمْ",
    "مُضَارِعٌ بَعْدَ لَوْ — لِإِفَادَةِ الِاسْتِمْرَارِ فِي الزَّمَنِ الْمَاضِي وَقْتًا بَعْدَ وَقْتٍ.",
    "A mudari after law: the denied obeying is pictured as a CONTINUING habit in the past — the first licensed tense-shift.",
    "Lev'den sonra muzâri: nefyedilen itaat, geçmişte SÜREN bir âdet olarak resmedilir — ruhsatlı ilk zaman kayması.")]})

# ---------------------------------------------------------------- s3 — Baqara 15
S.append({"id": "s3", "translation": {
 "en": "Allah mocks them. (al-Baqara 2:15 — a MUDARI where an ism fail was expected: the requital renews, time after time.)",
 "tr": "Allah onlarla istihzâ eder. (Bakara 2:15 — ism-i fâil beklenen yerde MUZÂRİ: karşılık, zaman zaman yenilenir.)"},
 "tokens": [
  tok("اللَّهُ","allah","propn",["mubtada-khabar"],
      "لَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.",
      "The Name as mubtada.",
      "Lafza-i celâl, mübtedâ."),
  tok("يَسْتَهْزِئُ","istahzaa","verb",["form-x-verbs","hikayat-al-hal","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْجُمْلَةُ خَبَرٌ — وَجَاءَ الْمُضَارِعُ مَوْضِعَ اسْمِ الْفَاعِلِ لِإِفَادَةِ التَّجَدُّدِ وَقْتًا بَعْدَ وَقْتٍ.",
      "«MOCKS them» — Form X of the hamza-final ه ز أ, and the tense is the teaching: the aya answers the mockers' noun-sentence (إِنَّمَا نَحْنُ مُسْتَهْزِئُونَ — a settled trait) not with the matching ism fail مُسْتَهْزِئٌ but with a MUDARI: His requital is not a standing attribute but a renewing act, arriving again and again, time after time. Chapter 16's doctrine wielded as rhetoric.",
      "«İSTİHZÂ EDER» — hemze-i lâm'lı ه ز أ kökünün X. bâbı; ve kip, dersin kendisidir: âyet, alaycıların isim cümlesine (إِنَّمَا نَحْنُ مُسْتَهْزِئُونَ — yerleşik bir vasıf) denk ism-i fâil مُسْتَهْزِئٌ ile değil, MUZÂRİ ile cevap verir: O'nun karşılığı duran bir sıfat değil, zaman zaman yeniden gelen bir iştir. 16. bâbın kāidesi, belâgat olarak kuşanılmış.",
      segments=[seg("يَسْتَهْزِئُ","istahzaa","verb")]),
  tok("بِهِمْ","bi","part",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْفِعْلِ.",
      "«them» — the mockery's target under the ba.",
      "«onlarla» — istihzânın hedefi, bâ altında.",
      segments=[seg("بِ","bi","prep"), seg("هِمْ","pron-3mp","pron")],
      punct=".")],
 "jumal": [
  J("اللَّهُ يَسْتَهْزِئُ بِهِمْ",
    "مُضَارِعٌ مَوْضِعَ اسْمِ الْفَاعِلِ — لِتَجَدُّدِ الْجَزَاءِ وَقْتًا بَعْدَ وَقْتٍ.",
    "A mudari standing where the ism fail was expected: the requital RENEWS — the mockers' settled trait is answered with an ever-arriving act.",
    "İsm-i fâil beklenen yerde muzâri: karşılık YENİLENİR — alaycıların yerleşik vasfına, tekrar tekrar gelen bir işle cevap verilir.")]})

# ---------------------------------------------------------------- s4 — An'am 27
S.append({"id": "s4", "translation": {
 "en": "And could you but see when they are made to stand before the Fire… (al-An'am 6:27 — the mudari after لَوْ shows the future as PRESENT: the scene is set playing before the eyes.)",
 "tr": "Ateşin başında durduruldukları zaman bir görsen… (En'âm 6:27 — لَوْ'den sonraki muzâri istikbâli ŞİMDİ gibi gösterir: sahne, gözlerin önünde oynatılır.)"},
 "tokens": [
  tok("وَلَوْ","law","part",["in-shartiyya","hikayat-al-hal"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«لَوْ» شَرْطِيَّةٌ — وَجَوَابُهَا مَحْذُوفٌ: لَرَأَيْتَ أَمْرًا عَظِيمًا.",
      "«and COULD you but…» — law again, and this time its JAWAB is omitted: «you would have seen a tremendous thing» — left unsaid because no words would carry it. The omission is itself the rhetoric: the hearer's imagination completes what the tongue declines to bound.",
      "«bir GÖRSEN…» — yine lev; ve bu kez CEVABI hazfedilmiş: «muazzam bir şey görürdün» — hiçbir söz taşıyamayacağı için söylenmemiş. Hazfin kendisi belâgattir: dilin sınırlamaktan kaçındığını, dinleyenin muhayyilesi tamamlar.",
      segments=[seg("وَ","wa","part"), seg("لَوْ","law","part")]),
  tok("تَرَى","raa","verb",["naqis-verbs","hikayat-al-hal"],
      "فِعْلٌ مُضَارِعٌ — بَعْدَ لَوْ — تُقَدَّرُ ضَمَّتُهُ عَلَى الْأَلِفِ، وَالْفَاعِلُ أَنْتَ.",
      "«you SEE» — a mudari after law, and the boldest of the shifts: the standing-before-the-Fire has not happened, yet the Speaker — whose word cannot miss — sets it before you in the present tense, as a scene ALREADY PLAYING. The books call this حِكَايَةُ الْحَالِ: narrating a state as if you stood inside it.",
      "«GÖRÜRSÜN» — lev'den sonra muzâri; kaymaların en cüretlisi: ateşin önünde durduruluş henüz olmamıştır; fakat sözü şaşmaz olan Konuşan, onu sana şimdiki kipte, OYNAMAKTA OLAN bir sahne gibi koyar. Kitaplar buna حِكَايَةُ الْحَالِ der: bir hâli, içinde duruyormuşsun gibi anlatmak.",
      segments=[seg("تَرَى","raa","verb")]),
  tok("إِذْ","idh","noun",["maful-fih","hikayat-al-hal"],
      "ظَرْفٌ لِمَا مَضَى مِنَ الزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ — وَهُنَا لِلْمُسْتَقْبَلِ تَنْزِيلًا لَهُ مَنْزِلَةَ الْمَاضِي.",
      "«WHEN…» — إِذْ, the zarf of PAST time, a mabni noun mudaf to the whole clause after it. And it deepens the shift: a past-time adverb pointing at a future scene — because for the One who speaks, the future is as settled as the past. Tense and time pull apart, deliberately, twice in three words.",
      "«…-DIĞI ZAMAN» — إِذْ: GEÇMİŞ zaman zarfı; ardındaki cümlenin tamamına muzâf, mebnî bir isim. Ve kaymayı derinleştirir: geçmiş zarfı, gelecek bir sahneyi gösteriyor — çünkü Konuşan için istikbâl, mâzî kadar kesindir. Kip ile zaman, üç kelimede iki kez, kasıtla ayrışır."),
  tok("وُقِفُوا","waqafa","verb",["naib-al-fail","hikayat-al-hal"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ.",
      "«they are MADE TO STAND» — the passive of وَقَفَ: they do not stand, they are stood; the group's waw is the deputy doer. The agent unnamed, the standing absolute.",
      "«DURDURULDUKLARI» — وَقَفَ'nin meçhûlü: durmazlar, durdurulurlar; cemâat vâvı nâib-i fâildir. Fâil anılmaz; duruş mutlaktır.",
      segments=[seg("وُقِفُوا","waqafa","verb")]),
  tok("عَلَى","ala","part",["huruf-jarr"],
      "حَرْفُ جَرٍّ.",
      "«before / at» — the jarr letter of the standing.",
      "«başında» — duruşun cer harfi."),
  tok("النَّارِ","nar","noun",["huruf-jarr"],
      "اسْمٌ مَجْرُورٌ.",
      "«the Fire» — and the aya breaks off, its jawab still unsaid.",
      "«ateşin» — ve âyet, cevabı hâlâ söylenmemiş, yarıda durur.",
      punct="…")],
 "jumal": [
  J("وَلَوْ تَرَى إِذْ وُقِفُوا عَلَى النَّارِ",
    "مُضَارِعٌ بَعْدَ لَوْ وَظَرْفُ الْمَاضِي لِلْمُسْتَقْبَلِ — حِكَايَةُ الْحَالِ، وَالْجَوَابُ مَحْذُوفٌ تَهْوِيلًا.",
    "The future shown as present (the speaker cannot miss) with a past-time zarf pointing forward — hikayat al-hal — and the jawab omitted because no words would bound it.",
    "İstikbâl şimdi gibi gösterilir (Konuşan şaşmaz), geçmiş zarfı ileriyi gösterir — hikâyetü'l-hâl — ve cevap, hiçbir sözün sınırlayamayacağı için hazfedilmiştir.")]})

# ---------------------------------------------------------------- s5 — Fatir 9
S.append({"id": "s5", "translation": {
 "en": "He sent the winds, and they STIR up a cloud… (Fatir 35:9 — a mudari set between two mazis: the wondrous image is made present before the eyes.)",
 "tr": "Rüzgârları gönderdi; onlar bulutu KALDIRIR… (Fâtır 35:9 — iki mâzî arasında muzâri: eşsiz manzara gözlerin önüne getirilir.)"},
 "tokens": [
  tok("أَرْسَلَ","arsala","verb",["form-iv-verbs","fail"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ عَلَى اللَّهِ.",
      "«He SENT» — a plain mazi: the sending is reported as done.",
      "«GÖNDERDİ» — düz mâzî: gönderiş, olmuş bitmiş diye bildirilir."),
  tok("الرِّيَاحَ","rih","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the winds» — the object, plural of رِيح.",
      "«rüzgârları» — mef'ûl; رِيح'in çoğulu."),
  tok("فَتُثِيرُ","athara","verb",["form-iv-verbs","hikayat-al-hal","hollow-verbs"],
      "الْفَاءُ عَاطِفَةٌ، وَالْفِعْلُ مُضَارِعٌ — عَلَى خِلَافِ مُقْتَضَى الظَّاهِرِ، إِذِ الْفِعْلَانِ حَوْلَهُ مَاضِيَانِ — لِاسْتِحْضَارِ الصُّورَةِ الْعَجِيبَةِ.",
      "«and they STIR up» — the aya's jewel. Both verbs around it are mazi (أَرْسَلَ before, فَسُقْنَاهُ after), so the surface demanded فَأَثَارَتْ. Instead a MUDARI: the winds driving the cloud is the one image in the sequence that displays the Power, so it alone is lifted out of past time and SET PLAYING — اسْتِحْضَارُ الصُّورَةِ, the picture made present. Form IV of the hollow ث و ر: أَثَارَ → تُثِيرُ.",
      "«KALDIRIR» — âyetin mücevheri. Çevresindeki iki fiil de mâzî (önce أَرْسَلَ, sonra فَسُقْنَاهُ); zâhir فَأَثَارَتْ isterdi. Yerine MUZÂRİ: rüzgârların bulutu sürmesi, dizideki Kudreti gösteren tek manzaradır; bu yüzden yalnız o, geçmiş zamandan çıkarılıp OYNATILIR — اسْتِحْضَارُ الصُّورَةِ: resmin şimdiye getirilişi. Ecvef ث و ر'un IV. bâbı: أَثَارَ → تُثِيرُ.",
      segments=[seg("فَ","fa","part"), seg("تُثِيرُ","athara","verb")]),
  tok("سَحَابًا","sahab","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«a cloud» — indefinite: any cloud, every cloud; the wonder is the mechanism, not one instance.",
      "«bir bulut» — nekre: herhangi bir bulut, her bulut; hayret tek olayda değil, düzenektedir.",
      punct="…")],
 "jumal": [
  J("أَرْسَلَ الرِّيَاحَ فَتُثِيرُ سَحَابًا",
    "مُضَارِعٌ بَيْنَ مَاضِيَيْنِ — لِاسْتِحْضَارِ الصُّورَةِ الدَّالَّةِ عَلَى الْقُدْرَةِ.",
    "A mudari set between two mazis: of the whole sequence, only the image that displays the Power is lifted into the present.",
    "İki mâzî arasında muzâri: bütün dizide yalnız Kudreti gösteren manzara şimdiye kaldırılır.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # NEW this chapter
 "anita":     g("عَنِتَ", "ع ن ت", "verb", "to fall into hardship, come to grief", "sıkıntıya düşmek, zora girmek", 5, form="I"),
 "istahzaa":  g("اِسْتَهْزَأَ", "ه ز أ", "verb", "to mock, ridicule", "istihzâ etmek, alay etmek", 4, form="X"),
 "athara":    g("أَثَارَ", "ث و ر", "verb", "to stir up, raise (dust, clouds)", "kaldırmak, harekete geçirmek (toz, bulut)", 4, form="IV"),
 "sahab":     g("سَحَاب", "س ح ب", "noun", "cloud(s)", "bulut", 3, plural="سُحُب"),
 "idh":       g("إِذْ", None, "noun", "when (a mabni zarf for past time — a noun, like عِنْد)", "…-dığı zaman (geçmiş için mebnî zarf — عِنْد gibi bir isim)", 3),
 "pron-2mp":  g("ـكُمْ", None, "pron", "you (pl.) / your (attached)", "sizi, sizin (muttasıl)", 1),
 "lam-jawab": g("لَ (لَامُ الْجَوَابِ)", None, "part", "the lam opening the jawab of law (and the oath)", "lev'in (ve kasemin) cevabını açan lâm", 4),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "law":       g("لَوْ", None, "part", "if (unreal — imtina' li-imtina')", "eğer …-seydi (imtinâ لَوْ'i)", 3),
 "kathir":    g("كَثِير", "ك ث ر", "noun", "much, many", "çok, birçok", 1),
 "nar":       g("نَار", "ن و ر", "noun", "fire; the Fire", "ateş; cehennem ateşi", 1, plural="نِيرَان"),
 "akrama":    g("أَكْرَمَ", "ك ر م", "verb", "to honor, treat generously", "ikram etmek", 2, form="IV"),
 "ataa":      g("أَطَاعَ", "ط و ع", "verb", "to obey", "itaat etmek", 2, form="IV"),
 "raa":       g("رَأَى", "ر أ ي", "verb", "to see", "görmek", 1, form="I"),
 "waqafa":    g("وَقَفَ", "و ق ف", "verb", "to stand; to halt", "durmak; durdurmak", 2, form="I"),
 "arsala":    g("أَرْسَلَ", "ر س ل", "verb", "to send", "göndermek", 2, form="IV"),
 "min":       g("مِنْ", None, "part", "from, of", "-den, -dan", 1),
}

def build_morph():
    """Copies for akrama/ataa/raa/waqafa/arsala; three new paradigms.

    عَنِتَ — bab سَمِعَ, lam = ta: the subject suffixes' ta meets it and the
    idgham writes عَنِتُّمْ (the sarf jewel Hujurat 7 stands on).
    اِسْتَهْزَأَ — Form X, hamza-final; the mechanical seat spelling follows
    the قَرَأُوا precedent already in the corpus.
    أَثَارَ — Form IV of the hollow ث و ر, on the أَشَارَ model.
    """
    out = {}
    for pkg, lex in [("wasiyyat-abi-hanifa-samti", "akrama"),
                     ("min-muqaddimat-al-maqsud", "ataa"),
                     ("wasiyyat-abi-yusuf-l5", "raa"),
                     ("ashab-al-fil", "waqafa"),
                     ("ashab-al-fil", "arsala")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    out["anita"] = _sg.idgham(_sg.sound1("samia", "عَنِت", "عْنَت", "اِعْنَت", "عَنَت", "عَانِت"))
    out["istahzaa"] = _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَهْزَأ", "سْتَهْزِئ", "اِسْتَهْزِئ",
                                  "اِسْتِهْزَاء", "مُسْتَهْزِئ", maful="مُسْتَهْزَأ",
                                  pmz="اُسْتُهْزِئَ", pmd="يُسْتَهْزَأُ")
    out["athara"] = _sg.derived_hollow(_sg.B4 + " — أَجْوَفُ وَاوِيٌّ", _sg.W4, "ُ",
                                       "أَثَار", "أَثَر", "ثِير", "ثِر", "أَثِير", "أَثِر",
                                       "إِثَارَة", "مُثِير", maful="مُثَار",
                                       pmz="أُثِيرَ", pmd="يُثَارُ",
                                       note="أَجْوَفُ وَاوِيٌّ مِنَ الْإِفْعَالِ عَلَى مِثَالِ أَشَارَ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/17.json").write_text(
    json.dumps({"chapter": 17, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 17 for c in man["chapters"]):
    man["chapters"].append({"n": 17, "title": TITLE17})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.17.0"
ADD_EN = (" Chapter 17 continues from the same file (lines ~1483-1510, sahifa 52): the matn's frame "
          "لَوْ جِئْتَنِي لَأَكْرَمْتُكَ, al-Hujurat 49:7, al-Baqara 2:15, al-An'am 6:27 and Fatir 35:9. The ayat "
          "are received text quoted exactly; the Ottoman print's plain-alif spellings are restored to "
          "standard orthography, a spelling normalization only.")
ADD_TR = (" On yedinci bâb aynı dosyadan (satır ~1483-1510, sahife 52) devam eder: metnin kalıbı "
          "لَوْ جِئْتَنِي لَأَكْرَمْتُكَ, Hucurât 49:7, Bakara 2:15, En'âm 6:27 ve Fâtır 35:9. Âyetler aynen alınmış "
          "mervî metindir; Osmanlı baskısının düz elifli imlâsı standart imlâya çevrilmiştir — yalnız bir "
          "imlâ normalizasyonudur.")
if "1483-1510" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch17:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
