# -*- coding: utf-8 -*-
"""Author chapter 12 of aqaid-ahl-al-sunna — the number of the prophets.

Picks the matn up exactly where chapter 11 stopped: their number is reported
in some hadiths, but the better course is not to fix a count when naming
them — for Allah said «of them are some We have told you of, and of them are
some We have not» — and in stating a number one is not safe from letting in
who is not of them or leaving out who is. All of them conveyed and reported
from Allah, truthful and sincere; and the best of the prophets is Muhammad.

Verbatim contiguous span, re-vowelled against the received text. The Qur'anic
verse is quoted as the matn quotes it and is marked as a quotation in its own
i'rab, not silently blended into the author's prose.
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/aqaid-ahl-al-sunna"
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

TITLE12 = {"ar": "عَدَدُ الْأَنْبِيَاءِ وَأَفْضَلُهُمْ",
           "en": "The Number of the Prophets, and the Best of Them",
           "tr": "Nebîlerin Sayısı ve En Faziletlisi"}

S.append({"id": "s1", "translation": {
 "en": "And a statement of their number has been reported in some of the hadiths.",
 "tr": "Sayılarının beyanı bazı hadislerde rivayet edilmiştir."},
 "tokens": [
  tok("وَقَدْ","qad","part",["qad-harf"],
      "الْوَاوُ عَاطِفَةٌ، وَ«قَدْ» حَرْفُ تَحْقِيقٍ مَعَ الْمَاضِي.",
      "Joining waw; «qad» before a past verb affirms it took place.",
      "Atıf vâvı; mâzî ile «قَدْ» tahkîk harfidir.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("رُوِيَ","ruwiya","verb",["naib-al-fail","naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — نَاقِصٌ وَاوِيٌّ، ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ.",
      "A past verb built for the unknown — a naqis verb: its first letter takes a damma, the one before the last a kasra.",
      "Meçhul mâzî fiil — nâkıs; başı ötreli, sonundan önceki harf kesralıdır."),
  tok("بَيَانُ","bayan","noun",["naib-al-fail","idafa-definiteness","form-ii-verbs","masdar"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «بَيَّنَ».",
      "The deputy fa'il, in raf', and a mudaf — the masdar of بَيَّنَ.",
      "Merfû nâibü'l-fâil ve muzâf — «بَيَّنَ»nin masdarı."),
  tok("عَدَدِهِمْ","adad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ ثَانٍ.",
      "The mudaf ilayh in jarr, itself a mudaf; the ha is a second mudaf ilayh.",
      "Mecrûr muzâfun ileyh, kendisi de muzâf; hâ ikinci muzâfun ileyhtir.",
      segments=[seg("عَدَدِ","adad","noun"), seg("هِمْ","pron-3mp","pron")]),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("بَعْضِ","bad","noun",["huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ.",
      "In jarr by the kasra, and a mudaf.",
      "Kesra ile mecrur ve muzâf."),
  tok("الْأَحَادِيثِ","hadith","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ «حَدِيثٍ» عَلَى أَحَادِيثَ، وَظَهَرَتِ الْكَسْرَةُ لِدُخُولِ «الْ».",
      "The mudaf ilayh in jarr — the plural أَحَادِيث, and the kasra SHOWS because the article restores it.",
      "Mecrûr muzâfun ileyh — «حَدِيث»in cem'i; «ال» girdiği için kesra zâhirdir.", punct="،"),
 ],
 "jumal": [J("وَقَدْ رُوِيَ بَيَانُ عَدَدِهِمْ فِي بَعْضِ الْأَحَادِيثِ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir.")]})

S.append({"id": "s2", "translation": {
 "en": "And the better course is that one should not confine himself to a number in naming them.",
 "tr": "Evlâ olan, isimlendirmede bir sayı ile yetinmemektir."},
 "tokens": [
  tok("وَالْأَوْلَى","awla","noun",["mubtada-khabar","ism-tafdil","ism-maqsur-manqus"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«الْأَوْلَى» مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمُ تَفْضِيلٍ مَقْصُورٌ.",
      "Isti'naf waw; «the better» is the mubtada in raf' by a damma ESTIMATED on its alif — a maqsur elative.",
      "İstinâf vâvı; «الْأَوْلَى» elifi üzerinde takdîrî damme ile merfû mübtedâ — maksûr ism-i tafdîldir.",
      segments=[seg("وَ","wa","conj"), seg("الْأَوْلَى","awla","noun")]),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya","inna-am-anna"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ مِنْهُ وَمِمَّا بَعْدَهُ خَبَرُ الْمُبْتَدَإِ.",
      "The SAKIN masdar-making an, which puts the verb in nasb; the masdar read out of it is the khabar.",
      "Nasbeden masdar harfi; ondan ve sonrasından anlaşılan masdar haberdir."),
  tok("لَا","la-nafiya","part",["ma-la-mushabbaha"],
      "نَافِيَةٌ لَا عَمَلَ لَهَا — وَقَعَتْ بَيْنَ «أَنْ» وَمَنْصُوبِهَا فَلَمْ تَمْنَعِ النَّصْبَ.",
      "A plain negator with no government: it sits between «an» and the verb it governs, and does not block the nasb.",
      "Amel etmeyen nefiy harfi: «أَنْ» ile mansûbunun arasına girer, nasbı engellemez."),
  tok("يَقْتَصِرَ","iqtasara","verb",["form-viii-verbs","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ — مِنْ بَابِ الِافْتِعَالِ.",
      "A mudari in nasb by «an», the fatha its sign — Form VIII.",
      "«أَنْ» ile mansub muzâri, alâmeti fetha — iftiâl bâbından."),
  tok("عَلَى","ala","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِالْفِعْلِ.",
      "A jarr letter; the phrase attaches to the verb.",
      "Cer harfi; câr-mecrûr fiile taalluk eder."),
  tok("عَدَدٍ","adad","noun",["huruf-jarr"],
      "مَجْرُورٌ بِالْكَسْرَةِ — نَكِرَةٌ فِي سِيَاقِ النَّفْيِ فَتَعُمُّ.",
      "In jarr by the kasra — an indefinite under a negation, so it covers ANY number.",
      "Kesra ile mecrur — nefiy siyâkında nekiredir, umûm ifade eder."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("التَّسْمِيَةِ","tasmiya","noun",["huruf-jarr","form-ii-verbs","masdar"],
      "مَجْرُورٌ بِالْكَسْرَةِ — مَصْدَرُ «سَمَّى» عَلَى تَفْعِلَةٍ لِكَوْنِهِ نَاقِصًا.",
      "In jarr by the kasra — the masdar of سَمَّى on تَفْعِلَة, the shape a naqis Form II takes.",
      "Kesra ile mecrur — nâkıs olduğu için tef'ile vezninde «سَمَّى» masdarı.", punct="؛"),
 ],
 "jumal": [J("وَالْأَوْلَى أَنْ لَا يَقْتَصِرَ عَلَى عَدَدٍ فِي التَّسْمِيَةِ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ خَبَرُهَا مَصْدَرٌ مُؤَوَّلٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause whose khabar is a masdar read out of «an» — i'rabless.",
   "Haberi müevvel masdar olan istinâfî isim cümlesi — mahalsizdir.")]})

S.append({"id": "s3", "translation": {
 "en": "For Allah the Exalted said: «Of them are some We have told you of, and of them are some We have not told you of.»",
 "tr": "Zira Allah Teâlâ şöyle buyurdu: «Onlardan sana anlattıklarımız da var, sana anlatmadıklarımız da.»"},
 "tokens": [
  tok("فَقَدْ","qad","part",["qad-harf"],
      "الْفَاءُ لِلتَّعْلِيلِ، وَ«قَدْ» لِلتَّحْقِيقِ.",
      "The fa gives the REASON; «qad» affirms.",
      "Fâ ta'lîl içindir; «قَدْ» tahkîk bildirir.",
      segments=[seg("فَ","fa","conj"), seg("قَدْ","qad","part")]),
  tok("قَالَ","qala","verb",["hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ وَاوِيٌّ.",
      "A past verb on fatha — a hollow verb with a waw.",
      "Fetha üzere mebnî mâzî — ecvef-i vâvîdir."),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name, the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "A past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır."),
  tok("مِنْهُمْ","min","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ — وَهَذَا أَوَّلُ الْآيَةِ الْمَحْكِيَّةِ.",
      "A jarr phrase serving as a FRONTED khabar — and here the quoted verse begins.",
      "Öne geçmiş haber olan câr-mecrûr — burada mahkî âyet başlar.",
      segments=[seg("مِنْ","min","prep"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَنْ","man-mawsula","pron",["ism-mawsul"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
      "A relative noun, fixed, in the position of raf' as the delayed mubtada.",
      "İsm-i mevsûl — mebnî, sonraya bırakılmış mübtedâ olarak mahallen merfû."),
  tok("قَصَصْنَا","qassa","verb",["doubled-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِـ«نَا»، وَ«نَا» فَاعِلٌ، وَالْجُمْلَةُ صِلَةٌ — وَفُكَّ الْإِدْغَامُ لِسُكُونِ آخِرِهِ.",
      "A past verb on sukun because «na» joined it; «na» is the fa'il and the clause is the sila — and the doubling is UNDONE because the last letter fell quiescent.",
      "«نَا» bitiştiği için sükûn üzere mebnî mâzî; «نَا» fâil, cümle sıladır — sonu sâkin olduğu için idgam çözülmüştür.",
      segments=[seg("قَصَصْ","qassa","verb"), seg("نَا","pron-1p","pron")]),
  tok("عَلَيْكَ","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«قَصَصْنَا».",
      "A jarr phrase attaching to «We told».",
      "«قَصَصْنَا»ya taalluk eden câr-mecrûr.",
      segments=[seg("عَلَيْ","ala","prep"), seg("كَ","pron-2ms","pron")]),
  tok("وَمِنْهُمْ","min","prep",["huruf-jarr","atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ، وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.",
      "Joining waw; the jarr phrase is again a fronted khabar.",
      "Atıf vâvı; câr-mecrûr yine öne geçmiş haberdir.",
      segments=[seg("وَ","wa","conj"), seg("مِنْ","min","prep"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَنْ","man-mawsula","pron",["ism-mawsul"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
      "A relative noun in the position of raf' as the delayed mubtada.",
      "Sonraya bırakılmış mübtedâ olarak mahallen merfû ism-i mevsûl."),
  tok("لَمْ","lam-jazima","part",["lam-jazim"],
      "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.",
      "A letter of negation, jazm and time-reversal.",
      "Nefiy, cezm ve kalb harfi."),
  tok("نَقْصُصْ","qassa","verb",["lam-jazim","doubled-verbs"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِـ«لَمْ» وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ مُسْتَتِرٌ «نَحْنُ» — وَجَبَ فَكُّ الْإِدْغَامِ لِلْجَزْمِ.",
      "A mudari in jazm by «lam», the sukun its sign, its fa'il hidden «we» — and the doubling MUST be undone, precisely because of the jazm.",
      "«لَمْ» ile meczum muzâri, alâmeti sükûn, fâili müstetir «biz» — cezm sebebiyle idgamın çözülmesi vâcibdir."),
  tok("عَلَيْكَ","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْفِعْلِ، وَبِهِ تَنْتَهِي الْآيَةُ.",
      "A jarr phrase attaching to the verb; with it the verse ends.",
      "Fiile taalluk eden câr-mecrûr; âyet burada biter.",
      segments=[seg("عَلَيْ","ala","prep"), seg("كَ","pron-2ms","pron")], punct="،"),
 ],
 "jumal": [J("فَقَدْ قَالَ اللهُ تَعَالَى",
   "جُمْلَةٌ فِعْلِيَّةٌ تَعْلِيلِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "A verbal clause giving the reason — i'rabless.",
   "Ta'lîl bildiren fiil cümlesi — mahalsizdir."),
  J("مِنْهُمْ مَنْ قَصَصْنَا عَلَيْكَ",
   "جُمْلَةٌ اسْمِيَّةٌ مَحْكِيَّةٌ بِالْقَوْلِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ.",
   "A nominal clause QUOTED by «said» — in the position of nasb as its object.",
   "Kavil ile mahkî isim cümlesi — mef'ûlün bih olarak mahallen mansubdur.")]})

S.append({"id": "s4", "translation": {
 "en": "And in stating a number one is not safe from someone entering among them who is not of them, or someone leaving them who is of them.",
 "tr": "Sayı zikredilirken, onlardan olmayanın aralarına girmesinden yahut onlardan olanın çıkmasından emin olunamaz."},
 "tokens": [
  tok("وَلَا","la-nafiya","part",["ma-la-mushabbaha"],
      "الْوَاوُ عَاطِفَةٌ، وَ«لَا» نَافِيَةٌ.",
      "Joining waw; the لا simply negates.",
      "Atıf vâvı; «لَا» nefiy harfidir.",
      segments=[seg("وَ","wa","conj"), seg("لَا","la-nafiya","part")]),
  tok("يُؤْمَنُ","amina","verb",["naib-al-fail","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ الْمَصْدَرُ الْمُؤَوَّلُ الْآتِي.",
      "A mudari built for the unknown, in raf'; its deputy fa'il is the masdar read out of what follows.",
      "Merfû meçhul muzâri; nâibü'l-fâili sonra gelen müevvel masdardır."),
  tok("فِي","fi","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ.", "A jarr letter.", "Cer harfi."),
  tok("ذِكْرِ","dhikr","noun",["huruf-jarr","idafa-definiteness","masdar"],
      "مَجْرُورٌ بِالْكَسْرَةِ وَهُوَ مُضَافٌ — مَصْدَرُ «ذَكَرَ».",
      "In jarr by the kasra, and a mudaf — the masdar of ذَكَرَ.",
      "Kesra ile mecrur ve muzâf — «ذَكَرَ»nin masdarı."),
  tok("الْعَدَدِ","adad","noun",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "The mudaf ilayh in jarr.", "Mecrûr muzâfun ileyh."),
  tok("أَنْ","an-masdariyya","part",["an-masdariyya","inna-am-anna"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ، وَالْمَصْدَرُ الْمُؤَوَّلُ نَائِبُ فَاعِلٍ لِـ«يُؤْمَنُ».",
      "The masdar-making an; the masdar read out of it is the deputy fa'il of «one is safe».",
      "Nasbeden masdar harfi; müevvel masdar «يُؤْمَنُ»in nâibü'l-fâilidir."),
  tok("يَدْخُلَ","dakhala","verb",["an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِـ«أَنْ» وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.",
      "A mudari in nasb by «an», the fatha its sign.",
      "«أَنْ» ile mansub muzâri, alâmeti fetha."),
  tok("فِيهِمْ","fi","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَدْخُلَ».",
      "A jarr phrase attaching to «enters».",
      "«يَدْخُلَ»ye taalluk eden câr-mecrûr.",
      segments=[seg("فِي","fi","prep"), seg("هِمْ","pron-3mp","pron")]),
  tok("مَنْ","man-mawsula","pron",["ism-mawsul","fail"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ لِـ«يَدْخُلَ».",
      "A relative noun in the position of raf' as the fa'il of «enters».",
      "«يَدْخُلَ»nin fâili olarak mahallen merfû ism-i mevsûl."),
  tok("لَيْسَ","laysa","verb",["kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ جَامِدٌ، وَاسْمُهُ مُسْتَتِرٌ، وَالْجُمْلَةُ صِلَةُ الْمَوْصُولِ.",
      "A frozen defective past verb, its ism hidden; the clause is the sila.",
      "Câmid nâkıs mâzî; ismi müstetir, cümle sıladır."),
  tok("مِنْهُمْ","min","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ خَبَرُ «لَيْسَ» فِي مَحَلِّ نَصْبٍ.",
      "A jarr phrase serving as the khabar of «laysa», in the position of nasb.",
      "«لَيْسَ»nin haberi olan câr-mecrûr — mahallen mansub.",
      segments=[seg("مِنْ","min","prep"), seg("هُمْ","pron-3mp","pron")], punct="،"),
  tok("أَوْ","aw","part",["atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّخْيِيرِ أَوِ التَّنْوِيعِ.",
      "A joining letter offering an alternative.",
      "Tahyîr yahut tenvî' için atıf harfi."),
  tok("يَخْرُجَ","kharaja","verb",["an-masdariyya","atf-nasaq"],
      "مَعْطُوفٌ عَلَى «يَدْخُلَ» مَنْصُوبٌ.",
      "Joined to «enters», in nasb.",
      "«يَدْخُلَ»ye ma'tûf, mansubdur."),
  tok("مِنْهُمْ","min","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«يَخْرُجَ».",
      "A jarr phrase attaching to «leaves».",
      "«يَخْرُجَ»ye taalluk eden câr-mecrûr.",
      segments=[seg("مِنْ","min","prep"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَنْ","man-mawsula","pron",["ism-mawsul","fail"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ رَفْعٍ فَاعِلٌ لِـ«يَخْرُجَ».",
      "A relative noun in the position of raf' as the fa'il of «leaves».",
      "«يَخْرُجَ»nin fâili olarak mahallen merfû ism-i mevsûl."),
  tok("هُوَ","pron-3ms-munfasil","pron",["mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ، وَالْجُمْلَةُ صِلَةٌ.",
      "A detached pronoun, fixed, in the position of raf' as mubtada; the clause is the sila.",
      "Munfasıl zamir — mebnî, mahallen merfû mübtedâ; cümle sıladır."),
  tok("فِيهِمْ","fi","prep",["huruf-jarr","mubtada-khabar"],
      "جَارٌّ وَمَجْرُورٌ خَبَرُ الْمُبْتَدَإِ.",
      "A jarr phrase serving as the khabar.",
      "Mübtedânın haberi olan câr-mecrûr.",
      segments=[seg("فِي","fi","prep"), seg("هِمْ","pron-3mp","pron")], punct="،"),
 ],
 "jumal": [J("وَلَا يُؤْمَنُ فِي ذِكْرِ الْعَدَدِ أَنْ يَدْخُلَ فِيهِمْ مَنْ لَيْسَ مِنْهُمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ — لَا مَحَلَّ لَهَا.",
   "A joined verbal clause — i'rabless.",
   "Ma'tûf fiil cümlesi — mahalsizdir."),
  J("مَنْ هُوَ فِيهِمْ",
   "صِلَةُ الْمَوْصُولِ جُمْلَةٌ اسْمِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "The sila is a nominal clause — i'rabless.",
   "Mevsûlün sılası isim cümlesidir — mahalsizdir.")]})

S.append({"id": "s5", "translation": {
 "en": "And all of them were reporting and conveying from Allah the Exalted, truthful and sincere.",
 "tr": "Hepsi Allah Teâlâ'dan haber veren ve tebliğ eden, doğru sözlü ve nasihat eden kimselerdi."},
 "tokens": [
  tok("وَكُلُّهُمْ","kull","noun",["mubtada-khabar","idafa-definiteness","kana-wa-akhawatuha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«كُلُّ» اسْمُ «كَانُوا» مُقَدَّمٌ — بَلْ هُوَ مُبْتَدَأٌ وَالْجُمْلَةُ بَعْدَهُ خَبَرُهُ.",
      "Isti'naf waw; «all of them» is the mubtada, and the kana-clause after it is its khabar.",
      "İstinâf vâvı; «كُلُّ» mübtedâdır ve sonrasındaki kâne cümlesi haberidir.",
      segments=[seg("وَ","wa","conj"), seg("كُلُّ","kull","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("كَانُوا","kana","verb",["kana-wa-akhawatuha","hollow-verbs","afal-khamsa"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَوَاوُ الْجَمَاعَةِ اسْمُهُ فِي مَحَلِّ رَفْعٍ.",
      "A defective past verb; the waw of the group is its ism, in the position of raf'.",
      "Nâkıs mâzî; vâv-ı cemâat mahallen merfû ismidir.",
      segments=[seg("كَان","kana","verb"), seg("ُوا","pron-3mp","pron")]),
  tok("مُخْبِرِينَ","mukhbir","noun",["kana-wa-akhawatuha","jam-mudhakkar-salim","ism-fail","form-iv-verbs"],
      "خَبَرُ «كَانَ» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ — اسْمُ فَاعِلٍ مِنْ «أَخْبَرَ».",
      "The khabar of «were», in nasb by the YA — the ism fa'il of أَخْبَرَ.",
      "«كَانَ»nin haberi, YÂ ile mansub — «أَخْبَرَ»nin ism-i fâili."),
  tok("مُبَلِّغِينَ","muballigh","noun",["tawkid","jam-mudhakkar-salim","ism-fail","form-ii-verbs"],
      "خَبَرٌ ثَانٍ لِـ«كَانَ» مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنْ «بَلَّغَ».",
      "A SECOND khabar of «were», in nasb by the ya — the ism fa'il of بَلَّغَ.",
      "«كَانَ»nin İKİNCİ haberi, yâ ile mansub — «بَلَّغَ»nin ism-i fâili."),
  tok("عَنِ","an","prep",["huruf-jarr"],
      "حَرْفُ جَرٍّ، وَحُرِّكَتْ نُونُهُ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr letter; its nun took a kasra where two sakins met.",
      "Cer harfi; iki sâkin buluştuğu için nûnu kesralanmıştır."),
  tok("اللهِ","allah","noun",["huruf-jarr"],
      "لَفْظُ الْجَلَالَةِ مَجْرُورٌ.",
      "The majestic name, in jarr.",
      "Lafza-i celâl — mecrurdur."),
  tok("تَعَالَى","taala","verb",["jumla-mutarida","naqis-verbs"],
      "فِعْلٌ مَاضٍ، وَالْجُمْلَةُ مُعْتَرِضَةٌ لِلتَّعْظِيمِ.",
      "A past verb; a parenthetic clause of exaltation.",
      "Mâzî fiil; ta'zîm için mu'terizadır.", punct="،"),
  tok("صَادِقِينَ","sadiq","noun",["hal","jam-mudhakkar-salim","ism-fail"],
      "خَبَرٌ ثَالِثٌ مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنْ «صَدَقَ».",
      "A third khabar, in nasb by the ya — the ism fa'il of صَدَقَ.",
      "Üçüncü haber, yâ ile mansub — «صَدَقَ»nin ism-i fâili."),
  tok("نَاصِحِينَ","nasih","noun",["hal","jam-mudhakkar-salim","ism-fail"],
      "خَبَرٌ رَابِعٌ مَنْصُوبٌ بِالْيَاءِ — اسْمُ فَاعِلٍ مِنْ «نَصَحَ».",
      "A fourth khabar, in nasb by the ya — the ism fa'il of نَصَحَ.",
      "Dördüncü haber, yâ ile mansub — «نَصَحَ»nin ism-i fâili.", punct="."),
 ],
 "jumal": [J("وَكُلُّهُمْ كَانُوا مُخْبِرِينَ مُبَلِّغِينَ عَنِ اللهِ تَعَالَى صَادِقِينَ نَاصِحِينَ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ نَاسِخَةٌ فِي مَحَلِّ رَفْعٍ.",
   "An isti'naf nominal clause whose khabar is a kana-clause, in the position of raf'.",
   "Haberi mahallen merfû nâsih fiil cümlesi olan istinâfî isim cümlesi.")]})

S.append({"id": "s6", "translation": {
 "en": "And the best of the prophets, upon them be peace, is Muhammad, may Allah bless him and grant him peace.",
 "tr": "Nebîlerin — aleyhimüsselâm — en faziletlisi Muhammed sallallâhu aleyhi ve sellemdir."},
 "tokens": [
  tok("وَأَفْضَلُ","afdal","noun",["mubtada-khabar","ism-tafdil","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَ«أَفْضَلُ» مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — اسْمُ تَفْضِيلٍ.",
      "Isti'naf waw; «the best» is the mubtada in raf' and a mudaf — an elative.",
      "İstinâf vâvı; «أَفْضَلُ» merfû mübtedâ ve muzâf — ism-i tafdîldir.",
      segments=[seg("وَ","wa","conj"), seg("أَفْضَلُ","afdal","noun")]),
  tok("الْأَنْبِيَاءِ","nabi","noun",["idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ — ظَهَرَتْ لِدُخُولِ «الْ» عَلَى صِيغَةِ مُنْتَهَى الْجُمُوعِ.",
      "The mudaf ilayh in jarr by the kasra — which SHOWS because the article restores it to a diptote plural shape.",
      "Kesra ile mecrûr muzâfun ileyh — müntehe'l-cumû' vezninde «ال» girdiği için kesra zâhirdir."),
  tok("عَلَيْهِمُ","ala","prep",["huruf-jarr","jumla-mutarida"],
      "جَارٌّ وَمَجْرُورٌ خَبَرٌ مُقَدَّمٌ، وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A jarr phrase as a fronted khabar; the mim took a damma where two sakins met.",
      "Öne geçmiş haber olan câr-mecrûr; iki sâkin buluştuğu için mîm ötrelenmiştir.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هِمُ","pron-3mp","pron")]),
  tok("السَّلَامُ","salam","noun",["mubtada-khabar"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، وَالْجُمْلَةُ دُعَائِيَّةٌ مُعْتَرِضَةٌ.",
      "The delayed mubtada in raf'; the whole is a parenthetic prayer.",
      "Sonraya bırakılmış merfû mübtedâ; cümle mu'teriza duâdır."),
  tok("مُحَمَّدٌ","muhammad","propn",["mubtada-khabar"],
      "خَبَرُ الْمُبْتَدَإِ مَرْفُوعٌ بِالضَّمَّةِ.",
      "The khabar of the mubtada, in raf' by the damma.",
      "Damme ile merfû haber."),
  tok("صَلَّى","salla","verb",["jumla-mutarida","naqis-verbs","form-ii-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ.",
      "A past verb built on a fatha ESTIMATED on its alif.",
      "Elifi üzerinde takdîrî fetha üzere mebnî mâzî."),
  tok("اللهُ","allah","noun",["fail"],
      "لَفْظُ الْجَلَالَةِ فَاعِلٌ مَرْفُوعٌ.",
      "The majestic name, the fa'il in raf'.",
      "Lafza-i celâl — merfû fâildir."),
  tok("عَلَيْهِ","ala","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«صَلَّى».",
      "A jarr phrase attaching to «blessed».",
      "«صَلَّى»ya taalluk eden câr-mecrûr.",
      segments=[seg("عَلَيْ","ala","prep"), seg("هِ","pron-3ms","pron")]),
  tok("وَسَلَّمَ","sallama","verb",["atf-nasaq","form-ii-verbs"],
      "الْوَاوُ عَاطِفَةٌ، وَ«سَلَّمَ» مَعْطُوفٌ عَلَى «صَلَّى»، وَالْفَاعِلُ مُسْتَتِرٌ.",
      "Joining waw; «granted peace» is joined to «blessed», its fa'il hidden.",
      "Atıf vâvı; «سَلَّمَ» «صَلَّى»ya ma'tûftur, fâili müstetirdir.",
      segments=[seg("وَ","wa","conj"), seg("سَلَّمَ","sallama","verb")], punct="."),
 ],
 "jumal": [J("وَأَفْضَلُ الْأَنْبِيَاءِ مُحَمَّدٌ",
   "جُمْلَةٌ اسْمِيَّةٌ اسْتِئْنَافِيَّةٌ — لَا مَحَلَّ لَهَا.",
   "An isti'naf nominal clause — i'rabless.",
   "İstinâfî isim cümlesi — mahalsizdir."),
  J("صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ",
   "جُمْلَةٌ فِعْلِيَّةٌ دُعَائِيَّةٌ مُعْتَرِضَةٌ — لَا مَحَلَّ لَهَا.",
   "A parenthetic verbal clause of prayer — i'rabless.",
   "Mu'teriza duâ cümlesi — mahalsizdir.")]})

GLOSS_ADD = {
 "ruwiya":    g("رُوِيَ", "ر و ي", "verb", "to be reported, narrated", "rivayet edilmek", 3),
 "bayan":     g("بَيَان", "ب ي ن", "noun", "a statement, making clear (masdar)", "beyan; açıklama (masdar)", 3),
 "bad":       g("بَعْض", "ب ع ض", "noun", "some, a part of", "bazı; bir kısmı", 1),
 "hadith":    g("حَدِيث", "ح د ث", "noun", "hadith, report", "hadis", 1, "أَحَادِيث"),
 "awla":      g("الْأَوْلَى", "و ل ي", "noun", "the better course (elative)", "evlâ olan (ism-i tafdîl)", 4),
 "iqtasara":  g("اِقْتَصَرَ", "ق ص ر", "verb", "to confine oneself to", "iktifâ etmek; yetinmek", 4),
 "tasmiya":   g("تَسْمِيَة", "س م و", "noun", "naming (masdar, Form II)", "isimlendirme; tesmiye (masdar)", 4),
 "fa":        g("فَ", None, "conj", "so, for (fa)", "böylece; zira (fâ)", 1),
 "man-mawsula": g("مَنْ (الْمَوْصُولَة)", None, "pron", "the one who (relative)", "kimse; -en kimse (mevsûl)", 2),
 "qassa":     g("قَصَّ", "ق ص ص", "verb", "to relate, narrate", "anlatmak; kıssa etmek", 3),
 "pron-1p":   g("نَا", None, "pron", "we, us (attached)", "biz (muttasıl)", 1),
 "amina":     g("أَمِنَ", "أ م ن", "verb", "to be safe from", "emin olmak", 2),
 "dhikr":     g("ذِكْر", "ذ ك ر", "noun", "mention, stating (masdar)", "zikir; anma (masdar)", 2),
 "aw":        g("أَوْ", None, "part", "or", "yahut; veya", 1),
 "pron-3ms-munfasil": g("هُوَ", None, "pron", "he (detached)", "o (munfasıl)", 1),
 "mukhbir":   g("مُخْبِر", "خ ب ر", "noun", "one who reports", "haber veren; muhbir", 3),
 "muballigh": g("مُبَلِّغ", "ب ل غ", "noun", "one who conveys", "tebliğ eden", 3),
 "sadiq":     g("صَادِق", "ص د ق", "noun", "truthful", "sâdık; doğru sözlü", 2),
 "nasih":     g("نَاصِح", "ن ص ح", "noun", "sincere adviser", "nâsih; öğüt veren", 3),
 "an":        g("عَنْ", None, "prep", "from, about", "-den; hakkında", 1),
 "adad":      g("عَدَد", "ع د د", "noun", "number, count", "sayı; aded", 2),
 "afdal":     g("أَفْضَل", "ف ض ل", "noun", "best, most excellent (elative)", "en faziletli (ism-i tafdîl)", 3),
 "lam-jazima": g("لَمْ", None, "part", "did not (negates, jazm, turns the tense back)", "-medi (nefiy, cezm, kalb)", 2),
 "pron-2ms":  g("كَ", None, "pron", "you (masc. sg., attached)", "sen/senin (muttasıl, eril)", 1),
}

def build_morph():
    aq = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))["verbs"]
    out = {}
    # رُوِيَ — the passive of the naqis رَوَى; the corpus needs only the mabni
    # lil-majhul rows it actually uses, but the paradigm is built in full.
    out["ruwiya"] = _sg.entry("مِنْ بَابِ ضَرَبَ — نَاقِصٌ يَائِيٌّ", "فَعَلَ يَفْعِلُ",
                              "رِوَايَة", "رَاوٍ",
                              _sg.mazi_naqis("رَوَ", "رَوَوْا"),
                              _sg.mudari_naqis("َ", "رْو", "i"), _sg.amr_naqis("اِرْو", "i"),
                              "يَرْوِيَ", "يَرْوِ", "تَرْوِ", "مَرْوِيّ", "رُوِيَ", "يُرْوَى",
                              "نَاقِصٌ: مَجْهُولُهُ رُوِيَ يُرْوَى — ضُمَّ أَوَّلُهُ وَكُسِرَ مَا قَبْلَ آخِرِهِ.")
    out["iqtasara"] = _sg.derived(_sg.B8, _sg.W8, "َ", "اِقْتَصَر", "قْتَصِر", "اِقْتَصِر",
                                  "اِقْتِصَار", "مُقْتَصِر", "مُقْتَصَر")
    out["qassa"] = _sg.idgham(_sg.entry(
        _sg.BABS["nasara"][0] + " — مُضَاعَفٌ", _sg.BABS["nasara"][1], "قَصّ", "قَاصّ",
        _sg.mazi14("قَصّ", "قَصَص"), _sg.mudari14("َ", "قُصّ", "قْصُص"),
        ["قُصَّ", "قُصَّا", "قُصُّوا", "قُصِّي", "قُصَّا", "اُقْصُصْنَ"],
        "يَقُصَّ", "يَقُصَّ", "تَقُصَّ", "مَقْصُوص", "قُصَّ", "يُقَصُّ",
        note="مُضَاعَفٌ: يَجِبُ فَكُّ الْإِدْغَامِ عِنْدَ سُكُونِ الْآخِرِ — لَمْ نَقْصُصْ، قَصَصْنَا."))
    out["amina"] = _sg.sound1("samia", "أَمِن", "أْمَن", "اِئْمَن", "أَمْن", "آمِن",
                              "مَأْمُون", "أُمِنَ", "يُؤْمَنُ",
                              note="مَهْمُوزُ الْفَاءِ: تُكْتَبُ هَمْزَتُهُ عَلَى الْوَاوِ فِي «يُؤْمَنُ».")
    for k in ("kana", "laysa", "dakhala", "kharaja", "qala", "salla", "sallama", "taala"):
        if k in aq: out[k] = aq[k]
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/12.json").write_text(json.dumps({"chapter": 12, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 12 for c in man["chapters"]):
    man["chapters"].append({"n": 12, "title": TITLE12})
man["chapters"].sort(key=lambda c: c["n"]); man["version"] = "0.10.0"
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8")); mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("ch12:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
