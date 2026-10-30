# -*- coding: utf-8 -*-
"""Author chapter 13 of talkhis-al-miftah — كُلٌّ فِي حَيِّزِ النَّفْيِ: عُمُومُ السَّلْبِ وَسَلْبُ الْعُمُومِ.

The musnad-ilayh bab closes on its most logical chapter: what happens to كُلّ
under negation. Ibn Mālik's rule states it by ORDER — kull fronted over the
negation is ʿumūm al-salb («no one at all»), kull delayed under it is salb
al-ʿumūm («not all — so some did») — and the muṣannif prefers ʿAbd al-Qāhir's
formulation by REACH: if كل falls inside the negation's ḥayyiz (after the
particle, or as maʿmūl of the negated verb), the negation strikes the
TOTALITY and the sentence affirms the part; outside it, the denial covers
every single member.

Al-Mutanabbī carries the first half — مَا كُلُّ مَا يَتَمَنَّى الْمَرْءُ يُدْرِكُهُ
(not ALL a man wishes does he attain — some he does) — and the Prophet's own
answer to Dhū al-Yadayn carries the second: كُلُّ ذَلِكَ لَمْ يَكُنْ, «none of
that happened», kull before the negation, every member denied. The chapter
closes the bab with لَا فِيهَا غَوْلٌ: the subject DELAYED because the maqam
demanded the musnad fronted for qasr — the door to the musnad's own bab.

ATTRIBUTION: every Arabic word is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~1067-1155: Ibn Malik's
pair, al-Mutanabbi's bayt, مَا جَاءَنِي الْقَوْمُ كُلُّهُمْ and لَمْ آخُذْ كُلَّ
الدَّرَاهِمِ, the hadith كُلُّ ذَلِكَ لَمْ يَكُنْ (Bukhari/Muslim, the Dhu
al-Yadayn story), and al-Saffat 37:47. Nothing is composed.

Grammar this chapter is chosen to teach:
  • note 115 `umum-al-salb` — the hayyiz doctrine with its question test,
    Ibn Malik's order-rule and the musannif's three objections named.
  • the engine work the probe forced: the madda as two hamzas (آخُذْ was a
    NOUN and a MUDAF), the jazm-shape test (يَتَمَنَّى read as a jazm), the
    فَعَالِل row (دَرَاهِم answered a weak triliteral), the revived rule 6c
    (naked() had been eating كل and بعض since the rule was written), and
    MaEngine's new salb-al-umum rule (مَا + كُلّ) and list-frame rule 6f.
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

TITLE13 = {"ar": "كُلٌّ فِي حَيِّزِ النَّفْيِ: عُمُومُ السَّلْبِ وَسَلْبُ الْعُمُومِ",
           "en": "Kull under Negation: Denying Every One, or Denying the Totality",
           "tr": "Nefiy Sahasında Küll: Umûmü's-Selb ve Selbü'l-Umûm"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "No man at all stood. — Not all men stood (so some did).",
 "tr": "Hiçbir insan kalkmadı. — İnsanların hepsi kalkmadı (demek ki bâzısı kalktı)."},
 "tokens": [
  tok("كُلُّ","kull","noun",["umum-al-salb","mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — تَقَدَّمَ عَلَى النَّفْيِ فَأَفَادَ عُمُومَ السَّلْبِ عِنْدَ ابْنِ مَالِكٍ.",
      "The mubtada, in raf', a mudaf — and standing BEFORE the negation. Ibn Malik's rule reads the order: kull fronted over the negation is ʿUMUM AL-SALB — the denial reaches every single member, «no man at all stood». Hold this sentence against the next one; the pair differs only in order, and the order is the whole meaning.",
      "Merfû mübtedâ ve muzâf — NEFİYDEN ÖNCE duruyor. İbn Mâlik'in kāidesi sırayı okur: nefyin üzerine öne alınmış kull, UMÛMÜ'S-SELBdir — inkâr her bir ferde ulaşır, «hiçbir insan kalkmadı». Bu cümleyi ardındakiyle yan yana tut; çift yalnız sırada ayrılır ve sıra, mânânın tamamıdır."),
  tok("إِنْسَانٍ","insan","noun",["idafa-definiteness","umum-al-salb"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh, in jarr.",
      "Mecrûr muzâfun ileyh."),
  tok("لَمْ","lam-jazima","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "The letter that negates, puts the mudari' in jazm, and turns its sense to the past.",
      "Nefiy, cezm ve kalb harfi: muzâriyi cezmedip mânâsını mâzîye çevirir."),
  tok("يَقُمْ","qama","verb",["lam-jazim","hollow-verbs","fa-khabar-mubtada"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ خَبَرٌ.",
      "The mudari' in jazm by lam, its sign the sukun — and the hollow middle DROPS for the meeting of two quiescents: يَقُومُ → يَقُمْ. The clause is the khabar of كُلُّ.",
      "«لَمْ» ile meczum muzâri; alâmeti sükûndur — ve ecvefin ortası iki sâkinin buluşmasıyla DÜŞER: يَقُومُ ← يَقُمْ. Cümle, «كُلُّ»nün haberidir.",
      punct="."),
  tok("لَمْ","lam-jazima","part",["lam-jazim","umum-al-salb"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ — وَالْمُسْنَدُ إِلَيْهِ بَعْدَهُ هٰذِهِ الْمَرَّةَ.",
      "The same lam — but this time the subject stands AFTER it, inside the negation's reach, and everything changes.",
      "Aynı lâm — fakat bu sefer özne ONDAN SONRA, nefyin sahası içinde duruyor ve her şey değişir."),
  tok("يَقُمْ","qama","verb",["lam-jazim","hollow-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ.",
      "The same jussive verb.",
      "Aynı meczum fiil."),
  tok("كُلُّ","kull","noun",["umum-al-salb","fail"],
      "فَاعِلٌ مَرْفُوعٌ مُضَافٌ — تَأَخَّرَ عَنِ النَّفْيِ فَأَفَادَ سَلْبَ الْعُمُومِ: نُفِيَ الْمَجْمُوعُ لَا كُلُّ فَرْدٍ.",
      "The fa'il now, still marfu', still mudaf — but DELAYED under the negation: SALB AL-ʿUMUM. What is denied is the totality, not each member — «not all of them stood», and the sentence thereby concedes that some did. One word moved; the logic inverted.",
      "Şimdi fâil; yine merfû, yine muzâf — fakat nefyin altına GECİKMİŞ: SELBÜ'L-UMÛM. Nefyedilen her ferd değil, bütündür — «hepsi kalkmadı», ve cümle böylece bâzısının kalktığını teslim eder. Tek kelime yer değiştirdi; mantık tersine döndü."),
  tok("إِنْسَانٍ","insan","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "The mudaf ilayh, in jarr.",
      "Mecrûr muzâfun ileyh.",
      punct=".")],
 "jumal": [
  J("كُلُّ إِنْسَانٍ لَمْ يَقُمْ",
    "جُمْلَةٌ اسْمِيَّةٌ — الْمُسْنَدُ إِلَيْهِ خَارِجَ حَيِّزِ النَّفْيِ، فَالسَّلْبُ عَامٌّ.",
    "A nominal sentence with the subject OUTSIDE the negation's reach — so the denial is universal.",
    "Özne nefiy sahasının DIŞINDA olan isim cümlesi — öyleyse selb umûmîdir."),
  J("لَمْ يَقُمْ كُلُّ إِنْسَانٍ",
    "جُمْلَةٌ فِعْلِيَّةٌ — كُلٌّ مَعْمُولُ الْفِعْلِ الْمَنْفِيِّ، فَالْمَنْفِيُّ هُوَ الْعُمُومُ.",
    "A verbal sentence with kull as the negated verb's own ma'mul — so what is denied is the totality, and the part survives.",
    "Küll'ün menfî fiilin ma'mûlü olduğu fiil cümlesi — öyleyse nefyedilen bütündür ve parça ayakta kalır.")]})

# ---------------------------------------------------------------- s2 — al-Mutanabbi
S.append({"id": "s2", "translation": {
 "en": "Not all that a man wishes does he attain — the winds blow contrary to what the ships desire.",
 "tr": "Kişi her arzu ettiğine nâil olamaz — rüzgârlar, gemilerin istemediği yönden eser."},
 "tokens": [
  tok("مَا","ma-nafiya","part",["umum-al-salb","ma-la-mushabbaha"],
      "حَرْفُ نَفْيٍ — وَكُلٌّ بَعْدَهُ فِي حَيِّزِهِ، فَالنَّفْيُ مُتَوَجِّهٌ إِلَى الشُّمُولِ خَاصَّةً.",
      "The negation — with كل directly inside its reach, so by ʿAbd al-Qāhir's rule the denial strikes the TOTALITY alone: «not ALL he wishes» — and the bayt's whole consolation lives in what that leaves standing: some of it he does attain.",
      "Nefiy harfi — ve «كل» doğrudan sahası içinde; öyleyse Abdülkāhir'in kāidesince inkâr yalnız BÜTÜNe yönelir: «her istediğini değil» — ve beytin bütün tesellîsi bunun ayakta bıraktığındadır: bâzısına nâil olur."),
  tok("كُلُّ","kull","noun",["umum-al-salb","mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ إِلَى «مَا» الْمَوْصُولَةِ.",
      "The mubtada, in raf' — annexed to the RELATIVE ma that follows: «all THAT a man wishes». Two ma's four words apart, one a letter and one a noun, and the chapter uses the pair on purpose.",
      "Merfû mübtedâ — ardındaki MEVSÛL mâya muzâftır: «kişinin arzu ettiği ŞEYİN hepsi». Dört kelime arayla iki mâ; biri harf, biri isim — bâb çifti bilerek kullanır."),
  tok("مَا","ma-mawsula","pron",["ism-mawsul","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ — وَالْمُضَافُ إِلَيْهِ لَا يَكُونُ إِلَّا اسْمًا.",
      "A relative noun, mabni, in the position of jarr as the mudaf ilayh — and the mudaf-ilayh seat is closed to particles, which settles this ma's class by POSITION alone. (The app's rule for exactly this had been silently dead for كل since it was written: the clitic-peel was eating the kaf. This chapter revived it.)",
      "İsm-i mevsûl; muzâfun ileyh olarak mahallen mecrûr — ve muzâfun ileyh mevkii harflere kapalıdır; bu mânın cinsini tek başına MEVKİ karara bağlar. (Uygulamanın tam bu kāidesi, yazıldığından beri «كل» için sessizce ölüydü: önek soyucusu kâfı yiyordu. Bu bâb onu diriltti.)"),
  tok("يَتَمَنَّى","tamanna","verb",["jumla-sifa","form-v-verbs","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَالْجُمْلَةُ صِلَةٌ، وَالْعَائِدُ مَحْذُوفٌ: يَتَمَنَّاهُ.",
      "A Form V naqis mudari', its damma ESTIMATED on the weak alif — the clause is the sila, and the ʿaid is a DROPPED object: يَتَمَنَّاهُ, «that he wishes [it]». The seat doctrine again, from the object's side.",
      "Form V nâkıs muzâri; dammesi illetli elif üzerinde TAKDÎRÎdir — cümle sıladır ve ÂİD, düşürülmüş mef'ûldür: «يَتَمَنَّاهُ». Mevki doktrini yine — bu kez mef'ûl tarafından."),
  tok("الْمَرْءُ","mar","noun",["fail","anwa-al-lam-al-tarif"],
      "فَاعِلٌ مَرْفُوعٌ، وَ«ال» فِيهِ لِلْجِنْسِ.",
      "The fa'il of «wishes», its article the lam of the genus: man as such.",
      "«Arzu eder»in fâili; harf-i ta'rîfi cins lâmıdır: insan cinsi."),
  tok("يُدْرِكُهُ","adraka","verb",["fa-khabar-mubtada","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ «كُلُّ».",
      "«Does he attain it» — Form IV, the ha its object pointing back at the mubtada's ma — and the clause is the KHABAR of كُلُّ, in raf'. The bayt's grammar closes exactly where its logic does.",
      "«Ona nâil olur» — Form IV; hâ, mübtedânın mâsına dönen mef'ûldür — ve cümle «كُلُّ»nün HABERİ olarak mahallen merfûdur. Beytin nahvi, tam mantığının kapandığı yerde kapanır.",
      segments=[seg("يُدْرِكُ","adraka","verb"), seg("هُ","pron-3ms","pron")],
      punct="•"),
  tok("تَجْرِي","jara","verb",["mudari-marfu","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ.",
      "«Blow» — the damma estimated on the ya as too heavy. The second hemistich is the proverb the first earns.",
      "«Eser» — damme, ağırlık sebebiyle yâ üzerinde takdîrîdir. İkinci mısra, birincinin hak ettiği darb-ı meseldir."),
  tok("الرِّيَاحُ","rih","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — جَمْعُ رِيحٍ.",
      "The fa'il — the plural of رِيح, wind.",
      "Merfû fâil — «رِيح»in cem'i."),
  tok("بِمَا","ma-mawsula","pron",["ism-mawsul","huruf-jarr"],
      "الْبَاءُ حَرْفُ جَرٍّ، وَ«مَا» مَوْصُولَةٌ فِي مَحَلِّ جَرٍّ.",
      "The ba governs, and the ma is a relative in its jarr: «contrary to WHAT the ships desire».",
      "Bâ cerreder; mâ, mecrûr mevkiinde mevsûldür: «gemilerin İSTEMEDİĞİ şeyle».",
      segments=[seg("بِ","bi","prep"), seg("مَا","ma-mawsula","pron")]),
  tok("لَا","la-nafiya","part",["la-nahiya"],
      "حَرْفُ نَفْيٍ دَاخِلٌ عَلَى الصِّلَةِ.",
      "A negation inside the sila — the clause it negates is still the relative's own.",
      "Sılanın içine girmiş nefiy — nefyettiği cümle yine mevsûlündür."),
  tok("تَشْتَهِي","ishtaha","verb",["jumla-sifa","form-viii-verbs","naqis-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ، وَالْعَائِدُ مَحْذُوفٌ: تَشْتَهِيهِ.",
      "A Form VIII naqis, its final ya a RADICAL (ش ه و → تَشْتَهِي) — the app's peel once took exactly this shape's ya for an object pronoun — and the ʿaid is again a dropped object: تَشْتَهِيهِ.",
      "Form VIII nâkıs; son yâsı ASLÎdir (ش ه و ← تَشْتَهِي) — uygulamanın soyucusu tam bu şeklin yâsını bir zamanlar mef'ûl zamiri sanmıştı — ve âid yine düşürülmüş mef'ûldür: «تَشْتَهِيهِ»."),
  tok("السُّفُنُ","safina","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ — جَمْعُ سَفِينَةٍ.",
      "The fa'il — the plural of سَفِينَة, ship.",
      "Merfû fâil — «سَفِينَة»nin cem'i.",
      punct=".")],
 "jumal": [
  J("مَا كُلُّ مَا يَتَمَنَّى الْمَرْءُ يُدْرِكُهُ",
    "كُلٌّ فِي حَيِّزِ النَّفْيِ — سَلْبُ الْعُمُومِ: نُفِيَ الشُّمُولُ وَثَبَتَ الْبَعْضُ.",
    "Kull inside the negation's reach — salb al-umum: the totality denied, the part affirmed. The consolation is grammatical before it is poetic.",
    "Küll nefiy sahasında — selbü'l-umûm: bütün nefyedildi, parça sâbit kaldı. Tesellî, şiirden önce nahvîdir.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "The people did not come to me — not all of them. — I did not take all the dirhams.",
 "tr": "Kavim bana gelmedi — hepsi değil. — Dirhemlerin tamamını almadım."},
 "tokens": [
  tok("مَا","ma-nafiya","part",["ma-la-mushabbaha"],
      "حَرْفُ نَفْيٍ.",
      "The negation.",
      "Nefiy harfi."),
  tok("جَاءَنِي","jaa","verb",["ya-al-mutakallim","fail"],
      "فِعْلٌ مَاضٍ، وَالنُّونُ لِلْوِقَايَةِ وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "The mazi with its nun of protection, the ya the object.",
      "Vikāye nûnu ve mef'ûl yâsıyla mâzî.",
      segments=[seg("جَاءَ","jaa","verb"), seg("نِي","ni-wiqaya","pron")]),
  tok("الْقَوْمُ","qawm","noun",["fail"],
      "فَاعِلٌ مَرْفُوعٌ.",
      "The fa'il, in raf'.",
      "Merfû fâil."),
  tok("كُلُّهُمْ","kull","noun",["umum-al-salb","tawkid"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَرْفُوعٌ — وَقَعَ كُلٌّ فِي حَيِّزِ النَّفْيِ، فَالْمَنْفِيُّ الشُّمُولُ: جَاءَ بَعْضُهُمْ.",
      "The ma'nawi tawkid — and because the whole sentence stands under مَا, this كل falls inside the negation's REACH: what is denied is the totality, «they did not come — ALL of them», and the part survives: some came. Chapter 10 taught this word as emphasis; this chapter teaches what negation does to it.",
      "Ma'nevî te'kîd — ve bütün cümle «مَا»nın altında durduğu için bu «كل», nefyin SAHASI içine düşer: nefyedilen bütündür, «hepsi birden gelmedi», ve parça ayakta kalır: bâzısı geldi. Onuncu bâb bu kelimeyi te'kîd olarak öğretmişti; bu bâb, nefyin ona ne yaptığını öğretir.",
      segments=[seg("كُلُّ","kull","noun"), seg("هُمْ","pron-3mp","pron")],
      punct="."),
  tok("لَمْ","lam-jazima","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ.",
      "The jazm-negation.",
      "Cezmeden nefiy."),
  tok("آخُذْ","akhadha","verb",["lam-jazim","umum-al-salb"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ، وَالْفَاعِلُ «أَنَا» — وَالْمَدَّةُ هَمْزَتَانِ: هَمْزَةُ الْمُتَكَلِّمِ وَفَاءُ الْفِعْلِ.",
      "«I did not take» — jussive, and the MADDA is two hamzas in one letter: the speaker's prefix أَ fused with the root's own hamza (أَ + أْخُذُ = آخُذُ). The app read this word as a noun — and a mudaf! — until the madda was unfolded for matching; the first person of every hamza-initial verb was unreachable from its written form.",
      "«Almadım» — meczum; ve MEDDE tek harfte iki hemzedir: mütekellim öneki «أَ», kökün kendi hemzesiyle kaynaşmıştır (أَ + أْخُذُ = آخُذُ). Medde eşleştirme için açılana dek uygulama bu kelimeyi isim — hem de muzâf! — okuyordu; hemze ile başlayan her fiilin birinci şahsı, yazılı şeklinden ulaşılmazdı."),
  tok("كُلَّ","kull","noun",["umum-al-salb","maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ مُضَافٌ — مَعْمُولُ الْفِعْلِ الْمَنْفِيِّ، فَهُوَ فِي حَيِّزِ النَّفْيِ: أَخَذْتُ بَعْضَهَا.",
      "The object, in nasb, a mudaf — the negated verb's own MA'MUL, so inside the hayyiz: «not all the dirhams did I take» — I took some. Abd al-Qahir's second route into the hayyiz: not after the particle, but governed by the negated verb.",
      "Mansub mef'ûlün bih, muzâf — menfî fiilin kendi MA'MÛLÜ, öyleyse nefiy sahasının içinde: «dirhemlerin tamamını almadım» — bâzısını aldım. Abdülkāhir'in sahaya ikinci yolu: edattan sonra değil, menfî fiilin amel ettiği kelime olarak."),
  tok("الدَّرَاهِمِ","dirham","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ دِرْهَمٍ عَلَى فَعَالِلَ، مِنْ صِيَغِ مُنْتَهَى الْجُمُوعِ.",
      "The mudaf ilayh, in jarr — the plural of دِرْهَم on فَعَالِل, a sighat muntaha al-jumu' (diptote when indefinite; the article restores its kasra here). Its four radicals are د ر ه م — the app's peel table lost the ha to a person-affix strip until this chapter gave the quadriliteral plurals their row.",
      "Mecrûr muzâfun ileyh — «دِرْهَم»in فَعَالِل veznindeki cem'i, sîga-i müntehe'l-cümû'dandır (nekreyken gayr-i munsarif; buradaki harf-i ta'rîf kesrasını geri verir). Dört aslî harfi د ر ه م'dir — uygulamanın soyma tablosu, bu bâb rubâî cem'lere satırını verene dek hâyı bir şahıs-eki soymasına kaptırıyordu.",
      punct=".")]})

# ---------------------------------------------------------------- s4 — the hadith
S.append({"id": "s4", "translation": {
 "en": "«None of that happened.» (The Prophet's answer to Dhu al-Yadayn — kull BEFORE the negation: every member denied.)",
 "tr": "«Bunların hiçbiri olmadı.» (Peygamber Efendimizin Zülyedeyn'e cevabı — küll nefiyden ÖNCE: her bir ferd nefyedilmiştir.)"},
 "tokens": [
  tok("كُلُّ","kull","noun",["umum-al-salb","mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ مُضَافٌ — خَارِجَ حَيِّزِ النَّفْيِ وَلَيْسَ مَعْمُولًا لِلْفِعْلِ الْمَنْفِيِّ، فَأَفَادَ عُمُومَ السَّلْبِ.",
      "The mubtada, a mudaf — OUTSIDE the negation's reach and not the negated verb's ma'mul, so the denial covers every single member: «NONE of that happened». The Prophet ﷺ was asked «did the prayer shorten, or did you forget?» — and the answer denies both at once, each individually. The hadith is the doctrine's cleanest witness, and the books cite it for exactly this.",
      "Merfû mübtedâ, muzâf — nefiy sahasının DIŞINDA ve menfî fiilin ma'mûlü değil; öyleyse inkâr her bir ferdi kaplar: «bunların HİÇBİRİ olmadı». Efendimize ﷺ «namaz mı kısaldı, yoksa unuttunuz mu?» diye sorulmuştu — cevap ikisini birden, her birini ayrı ayrı nefyeder. Hadis, doktrinin en berrak şâhididir ve kitaplar onu tam bunun için zikreder."),
  tok("ذَلِكَ","dhalika","pron",["asma-al-ishara","idafa-definiteness"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "The far demonstrative, mabni, in the position of jarr as the mudaf ilayh — a demonstrative CAN take this seat, where a detached pronoun never could.",
      "Uzak işaret ismi; muzâfun ileyh olarak mahallen mecrûr — işaret ismi bu mevkiye GİREBİLİR; munfasıl zamir asla giremezdi."),
  tok("لَمْ","lam-jazima","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "The jazm-negation.",
      "Cezmeden nefiy."),
  tok("يَكُنْ","kana","verb",["lam-jazim","hollow-verbs","fa-khabar-mubtada"],
      "فِعْلٌ مُضَارِعٌ تَامٌّ مَجْزُومٌ، حُذِفَتْ وَاوُهُ لِالْتِقَاءِ السَّاكِنَيْنِ — وَالْجُمْلَةُ خَبَرٌ.",
      "«Happened» — kana used COMPLETE (tamm), not as the incomplete sister: it means «to occur» and needs no khabar of its own. Jussive, its waw dropped for the two quiescents. The clause is the khabar of كُلُّ.",
      "«Oldu» — kâne burada TAM kullanılmıştır, nâkıs kardeş olarak değil: «vukū bulmak» demektir ve kendi haberine muhtaç değildir. Meczumdur; vâvı iki sâkinin buluşmasıyla düşmüştür. Cümle, «كُلُّ»nün haberidir.",
      punct=".")],
 "jumal": [
  J("كُلُّ ذَلِكَ لَمْ يَكُنْ",
    "الْمُسْنَدُ إِلَيْهِ خَارِجَ حَيِّزِ النَّفْيِ — عُمُومُ السَّلْبِ: نُفِيَ كُلُّ فَرْدٍ.",
    "The subject outside the negation's reach — umum al-salb: each member denied on its own. Both the shortening and the forgetting, severally.",
    "Özne nefiy sahasının dışında — umûmü's-selb: her ferd tek tek nefyedildi. Hem kısalma hem unutma, ayrı ayrı.")]})

# ---------------------------------------------------------------- s5 — the aya
S.append({"id": "s5", "translation": {
 "en": "No intoxication is in it (the drink of Paradise) — the subject delayed, because the maqam fronted the musnad for qasr.",
 "tr": "Onda (cennet şarabında) sersemletme yoktur — müsned kasr için öne alınınca, müsnedün ileyh geciktirilmiştir."},
 "tokens": [
  tok("لَا","la-nafiya","part",["umum-al-salb"],
      "حَرْفُ نَفْيٍ.",
      "The negation — and note it is NOT the genus-denying la of لَا رَجُلَ: the noun does not follow it directly, and غَوْلٌ keeps its tanwin and its raf'.",
      "Nefiy harfi — ve dikkat: «لَا رَجُلَ»nin cinsini nefyeden lâsı DEĞİLDİR; isim onu doğrudan takip etmez ve «غَوْلٌ» tenvînini de ref'ini de korur."),
  tok("فِيهَا","fi","prep",["zarf-mustaqarr-wa-laghw","taqdim-al-musnad-ilayh"],
      "جَارٌّ وَمَجْرُورٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ، مُسْتَقَرٌّ — قُدِّمَ الْمُسْنَدُ لِإِفَادَةِ الْقَصْرِ.",
      "The FRONTED khabar — mustaqarr on an omitted amil — and the fronting is a QASR: in IT, and only in it, is there no intoxication; the wines of this world are thereby indicted. When the maqam fronts the musnad, the musnad ilayh must wait: the bab of the subject closes by handing the pen to the bab of the predicate.",
      "ÖNE ALINMIŞ haber — mahzûf âmil üzere müstakar — ve takdîm bir KASRdır: sersemletme yalnız ONDA yoktur; dünya şarapları böylece töhmet altındadır. Makām müsnedi öne alınca müsnedün ileyh bekler: öznenin bâbı, kalemi yüklemin bâbına devrederek kapanır.",
      segments=[seg("فِي","fi","prep"), seg("هَا","pron-3fs","pron")]),
  tok("غَوْلٌ","ghawl","noun",["mubtada-khabar","tankir-al-musnad-ilayh","taqdim-al-musnad-ilayh"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — أُخِّرَ الْمُسْنَدُ إِلَيْهِ لِأَنَّ الْمَقَامَ اقْتَضَى تَقْدِيمَ الْمُسْنَدِ.",
      "The DELAYED mubtada, indefinite (licensed by the fronted khabar, as chapter 9's bayt taught) — and with it the musnad-ilayh bab ends: every state of the subject has now been walked, and the last state was to stand aside.",
      "GECİKTİRİLMİŞ mübtedâ; nekredir (öne alınmış haberin meşrû kıldığı üzere — dokuzuncu bâbın beytinin öğrettiği gibi) — ve onunla müsnedün ileyh bâbı biter: öznenin her hâli artık yürünmüştür ve son hâl, kenara çekilmekti.",
      punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "mar":      g("مَرْء", "م ر أ", "noun", "a man, a person", "kişi, insan", 4),
 "ghawl":    g("غَوْل", "غ و ل", "noun", "intoxication, what steals the mind", "sersemletme, aklı çalan şey", 5),
 "dirham":   g("دِرْهَم", None, "noun", "dirham (a silver coin)", "dirhem (gümüş sikke)", 2, plural="دَرَاهِم"),
 "tamanna":  g("تَمَنَّى", "م ن ي", "verb", "to wish for, to long for", "temennî etmek, arzulamak", 3, form="V"),
 "ishtaha":  g("اِشْتَهَى", "ش ه و", "verb", "to desire, to crave", "iştahlanmak, arzu etmek", 4, form="VIII"),
 "ma-mawsula": g("مَا (الْمَوْصُولَة)", None, "pron", "that which, what (relative)", "o şey ki (ism-i mevsûl mâ)", 3),
 "pron-3fs": g("ـهَا", None, "pron", "her, its (attached, fem.)", "onu, onun (muttasıl, müennes)", 1),
 "bi":       g("بِ", None, "prep", "with, by, in", "ile, -de", 1),
 # COPIED from other packages, lemma-identical — a lex key is GLOBAL.
 "qama":     g("قَامَ", "ق و م", "verb", "to stand, to rise", "kalkmak, ayağa durmak", 1, form="I"),
 "adraka":   g("أَدْرَكَ", "د ر ك", "verb", "to attain, to reach", "idrâk etmek, nâil olmak", 3, form="IV"),
 "akhadha":  g("أَخَذَ", "أ خ ذ", "verb", "to take", "almak", 1, form="I"),
 "lam-jazima": g("لَمْ", None, "part", "did not (jazm + past sense)", "-medi (cezmedip mâzîye çeviren lem)", 2),
 "rih":      g("رِيح", "ر و ح", "noun", "wind", "rüzgâr", 2, plural="رِيَاح"),
 "safina":   g("سَفِينَة", "س ف ن", "noun", "ship", "gemi", 2, plural="سُفُن"),
}

def build_morph():
    """Copies for qama/adraka/akhadha; two new derived-naqis paradigms.

    تَمَنَّى — Form V naqis (يَتَمَنَّى, the fatha type): masdar تَمَنٍّ is a
    manqus and the mensub-row templates cannot carry it, which the ziyade
    extension handles by refusing row by row.
    اِشْتَهَى — Form VIII naqis (يَشْتَهِي, the kasra type), masdar اِشْتِهَاء.
    """
    out = {}
    for pkg, lex in [("aqaid-ahl-al-sunna", "qama"),
                     ("mukhtasar-al-manar", "adraka"),
                     ("wasiyyat-abi-yusuf-l5", "akhadha")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    out["tamanna"] = _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَمَنَّ", "تَمَنّ", "a", "تَمَنّ",
                                       "تَمَنٍّ (التَّمَنِّي)", "مُتَمَنٍّ",
                                       "مُتَمَنًّى", "تُمُنِّيَ", "يُتَمَنَّى")
    out["ishtaha"] = _sg.derived_naqis(_sg.B8, _sg.W8, "َ", "اِشْتَهَ", "شْتَه", "i", "اِشْتَه",
                                       "اِشْتِهَاء", "مُشْتَهٍ",
                                       "مُشْتَهًى", "اُشْتُهِيَ", "يُشْتَهَى")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/13.json").write_text(
    json.dumps({"chapter": 13, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 13 for c in man["chapters"]):
    man["chapters"].append({"n": 13, "title": TITLE13})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.13.0"
ADD_EN = (" Chapter 13 continues from the same file (lines ~1067-1155), which carries every one of its "
          "examples vowelled: Ibn Malik's pair كُلُّ إِنْسَانٍ لَمْ يَقُمْ / لَمْ يَقُمْ كُلُّ إِنْسَانٍ, al-Mutanabbi's "
          "bayt, مَا جَاءَنِي الْقَوْمُ كُلُّهُمْ and لَمْ آخُذْ كُلَّ الدَّرَاهِمِ, the hadith كُلُّ ذَلِكَ لَمْ يَكُنْ "
          "(the Dhu al-Yadayn narration, Bukhari and Muslim), and al-Saffat 37:47. The hadith and the aya "
          "are received text quoted exactly.")
ADD_TR = (" On üçüncü bâb aynı dosyadan (satır ~1067-1155) devam eder; o satırlar bâbın bütün misallerini "
          "harekeli olarak taşır: İbn Mâlik'in çifti كُلُّ إِنْسَانٍ لَمْ يَقُمْ / لَمْ يَقُمْ كُلُّ إِنْسَانٍ, Mütenebbî'nin "
          "beyti, مَا جَاءَنِي الْقَوْمُ كُلُّهُمْ ile لَمْ آخُذْ كُلَّ الدَّرَاهِمِ, hadîs-i şerîf كُلُّ ذَلِكَ لَمْ يَكُنْ "
          "(Zülyedeyn rivâyeti, Buhârî ve Müslim) ve Sâffât 37:47. Hadis ile âyet, aynen alınmış "
          "mervî metindir.")
if "1067-1155" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch13:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
