# -*- coding: utf-8 -*-
"""Author chapter 6 of talkhis-al-miftah — الْقَرِينَةُ فِي الْمَجَازِ الْعَقْلِيِّ.

Chapter 5 defined the intellectual figure and ended on بِتَأَوُّلٍ — «by an
interpretation». This chapter is that word unpacked. A majaz is not made by the
speaker's private intention: something must SHOW that he did not mean the
ascription literally, and the books call that something the QARINA. Without it
the sentence is not a figure but an error, and the whole apparatus of ʿilm
al-maʿani would collapse into a licence to say anything.

The commentary sorts the qarina exactly as the rest of the fann is sorted —
by what is on the page and what is in the mind:

  • LAFZIYYA — a WORD elsewhere in the speech gives it away. Abu al-Najm's
    ascription of the greying to «the pull of the nights» is settled by the very
    next line, which names Allah's word to the sun as what wore the hair away.
  • MAʿNAWIYYA — nothing on the page; the ascription is simply IMPOSSIBLE, and
    impossible in one of two grades: عَقْلًا, which no state of the world could
    make true (a love does not carry a man), and عَادَةً, which a state of the
    world could make true but never does (one commander does not rout an army
    by himself).

And then a gradient, which is the subtlest thing in the chapter: knowing the
literal truth behind a figure is ZAHIR when the verb is rarely hung on a
figurative doer, and KHAFI when it is hung there so often that the ear has
stopped noticing. فَمَا رَبِحَتْ تِجَارَتُهُمْ is obvious; سَرَّتْنِي رُؤْيَتُكَ is not,
and every language has a stock of these.

ATTRIBUTION: every Arabic word here is VERBATIM from
research/sources/talkhis-al-miftah-balagha.txt, lines ~600-621, which gives all
six examples vowelled — the Ghafir verse, the two impossibility examples with
the literal sentence of the first, Abu al-Najm's line, the Baqara verse, and
Abu Nuwas's hemistich. The paired sentences JUXTAPOSE two of the source's own
phrases with a dash between them, as in chapter 5; no connective is composed
and no Arabic word here is ours.

Grammar this chapter is chosen to teach:
  • يَاءُ الْمُتَكَلِّمِ, four times over — بِي، لِي، نَفْسِي، سَرَّتْنِي. A noun annexed
    to it estimates its whole i'rab, because the place is already occupied by
    the kasra of suitability; and a VERB reaching it needs نُونُ الْوِقَايَةِ first,
    or the verb's own ending would be pulled into a kasra it cannot take.
  • ابْنِ — the imperative of a naqis: the jazm sign is the DELETION of the weak
    letter, and there is nothing left on the page to point at. Chapter 5 gave
    بَنَى in the madi; this is the same paradigm two cells away.
  • يَا هَامَانُ — a munada that is a single proper name: mabni on the damma it
    would have had, in the POSITION of nasb. The engine has known this since the
    Nida engine was built and has never had a vocative in real text to show it
    on.
  • حُسْنًا and نَظَرًا — two tamyiz in one hemistich, both indefinite, both in
    nasb, and neither one an object. The pair is the shortest cure available for
    reading every mansub nakira as a maf'ul.
  • قِيلُ اللهِ لِلشَّمْسِ — a masdar annexed to its FAʿIL with a jarr phrase hanging
    on it. Chapter 5 had the masdar annexed to its object; this is the other
    shape, in a line of poetry.
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

TITLE6 = {"ar": "الْقَرِينَةُ فِي الْمَجَازِ الْعَقْلِيِّ",
          "en": "The Signal That Makes a Figure a Figure",
          "tr": "Mecâz-ı Aklîde Karîne"}

# ---------------------------------------------------------------- s1
S.append({"id": "s1", "translation": {
 "en": "«Haman, build me a tower.»",
 "tr": "«Ey Hâmân, bana bir kule yap.»"},
 "tokens": [
  tok("يَا","ya","part",["vocative-munada"],
      "حَرْفُ نِدَاءٍ لِلْبَعِيدِ، وَيُنَادَى بِهِ الْقَرِيبُ تَنْزِيلًا.",
      "A vocative letter, properly for calling someone FAR — and using it for someone near is itself a tanzil, the very device chapter 4 was about. Fir'awn is speaking to a minister standing in front of him.",
      "Uzağı çağırmak için nidâ harfi — ve yakındakine onunla seslenmek, dördüncü bâbın konusu olan TENZÎLin ta kendisidir. Fir'avn, önünde duran bir vezire hitap ediyor."),
  tok("هَامَانُ","haman","propn",["vocative-munada","mamnu-min-sarf"],
      "مُنَادًى عَلَمٌ مُفْرَدٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ — وَهُوَ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
      "A munada that is a single proper name: MABNI on the damma, standing in the POSITION of nasb. Both halves matter — the damma is what you write, and the nasb is what it is, because a munada is the object of an unspoken «I call». And the name is barred from tanwin twice over, being foreign and a proper name at once.",
      "Müfred alem münâdâ: damme üzere MEBNÎ, mahallen MANSUB. İki yarı da mühimdir — yazdığınız şey dammedir, olduğu şey nasbdır; zira münâdâ, söylenmemiş bir «çağırıyorum» fiilinin mef'ûlüdür. İsim ayrıca hem alem hem a'cemî olduğu için iki sebeple gayr-i munsariftir."),
  tok("ابْنِ","bana","verb",["imperative-amr","naqis-verbs","majaz-aqli"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ حَرْفِ الْعِلَّةِ، وَفَاعِلُهُ مُسْتَتِرٌ تَقْدِيرُهُ «أَنْتَ» — وَهَمْزَتُهُ هَمْزَةُ وَصْلٍ سَقَطَتْ فِي الدَّرْجِ. وَالْإِسْنَادُ مَجَازٌ عَقْلِيٌّ: الْبَانِي الْفَعَلَةُ، وَهَامَانُ السَّبَبُ الْآمِرُ.",
      "An imperative, MABNI ON THE DELETION of its weak letter — the ya of يَبْنِي is simply gone, and its absence IS the sign, so there is nothing on the page to point at. Its doer is concealed as «you», and the alif at the front is a hamzat wasl that drops in connected speech. And the ascription is an intellectual figure: the builders are the workmen, and Haman is the commanding CAUSE. The chapter is showing at once that a figure can live inside a COMMAND — an insha, which admits of no true or false at all.",
      "Emir fiili; İLLET HARFİNİN HAZFİ üzere mebnîdir — «يَبْنِي»nin yâsı düşmüştür ve onun yokluğu alâmetin kendisidir; öyleyse sayfada gösterilecek bir şey yoktur. Fâili müstetir «أَنْتَ»dir; baştaki elif ise vasılda düşen hemze-i vasldır. İsnâd da mecâz-ı aklîdir: binâ edenler işçilerdir, Hâmân ise emreden SEBEPtir. Bâb, aynı anda şunu da gösteriyor: mecâz bir EMRİN içinde de yaşayabilir — ve emir inşâdır, doğruluk yahut yalanlık kabul etmez."),
  tok("لِي","li","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw","ya-al-mutakallim"],
      "اللَّامُ حَرْفُ جَرٍّ، وَالْيَاءُ يَاءُ الْمُتَكَلِّمِ ضَمِيرٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ مُتَعَلِّقٌ بِـ«ابْنِ»، فَهُوَ ظَرْفٌ لَغْوٌ.",
      "The lam is a jarr letter and the ya is the SPEAKER'S YA, a pronoun mabni in the position of jarr — the phrase attaching to «build», so it is LAGHW. The ya of the speaker is the one pronoun that never wears a vowel of its own; it takes the whole word's ending with it.",
      "Lâm cer harfi, yâ ise MÜTEKELLİM YÂSIdır — mahallen mecrûr mebnî zamir; câr-mecrûr «ابْنِ»ye taalluk eder, öyleyse LAĞVdır. Mütekellim yâsı, kendine ait bir hareke taşımayan tek zamirdir; kelimenin bütün sonunu kendisiyle birlikte götürür.",
      segments=[seg("لِ","li","prep"), seg("ي","pron-1s","pron")]),
  tok("صَرْحًا","sarh","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — نَكِرَةٌ، وَالتَّنْوِينُ لِلتَّعْظِيمِ فِي مِثْلِ هَذَا الْمَقَامِ.",
      "The object in nasb — indefinite, and in a mouth like this one the tanwin carries GRANDEUR rather than mere indefiniteness: «a tower — and what a tower». Compare it with the two tanwins at the end of this chapter, which are tamyiz and not objects at all: three indefinites in nasb, three different offices.",
      "Mansub mef'ûlün bih — nekre; ve böyle bir ağızda tenvîn, sadece belirsizlik değil TA'ZÎM taşır: «bir kule — hem de ne kule». Bunu, bu bâbın sonundaki iki tenvînle karşılaştırın: onlar temyîzdir, mef'ûl değil. Üç mansub nekre, üç ayrı vazife.",
      punct="."),
 ],
 "jumal": [J("ابْنِ لِي صَرْحًا",
   "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence of INSHA — a command — with no position in i'rab.",
   "İNŞÂÎ fiil cümlesi — emir; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s2
S.append({"id": "s2", "translation": {
 "en": "«Your love brought me to you» — my own self brought me to you, because of my love for you.",
 "tr": "«Sana olan sevgin beni sana getirdi» — beni sana getiren kendi nefsimdir, sevgin sebebiyle."},
 "tokens": [
  tok("مَحَبَّتُكَ","mahabba","noun",["mubtada-khabar","idafa-definiteness","masdar","form-iv-verbs"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — مَصْدَرُ «أَحَبَّ» عَلَى مَفْعَلَة.",
      "The mubtada in raf', a mudaf with the kaf annexed to it — the masdar of أَحَبَّ on مَفْعَلَة. A masdar as the subject of a verb of motion is already half the figure: an act cannot walk.",
      "Merfû mübtedâ ve muzâf; kâf muzâfun ileyhtir — «أَحَبَّ»nin MEF'ALE vezninde masdarı. Bir hareket fiilinin öznesi olarak masdar, mecâzın yarısıdır zaten: bir iş yürüyemez."),
  tok("جَاءَتْ","jaa","verb",["fail","majaz-aqli","qarinat-al-majaz"],
      "فِعْلٌ مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ، وَفَاعِلُهُ مُسْتَتِرٌ يَعُودُ عَلَى «الْمَحَبَّةِ» — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
      "A mazi with the ta of the feminine, its fa'il concealed and pointing back at «your love» — the clause standing in the position of raf' as the khabar. And here is the QARINA, and it is nothing written: a love cannot literally carry a man anywhere. The impossibility is عَقْلًا, and no state of the world could make the sentence true as it stands.",
      "Mâzî fiil; tâ müennesliktir, fâili müstetir olup «الْمَحَبَّة»ye râcidir — cümle, haber olarak mahallen merfûdur. İşte KARÎNE burada ve yazılı bir şey değil: bir sevgi, bir adamı hakîkaten taşıyamaz. İmkânsızlık AKLENdir; âlemin hiçbir hâli bu cümleyi olduğu gibi doğru kılamaz."),
  tok("بِي","bi","prep",["huruf-jarr","zarf-mustaqarr-wa-laghw","ya-al-mutakallim"],
      "الْبَاءُ لِلتَّعْدِيَةِ، وَالْيَاءُ ضَمِيرٌ فِي مَحَلِّ جَرٍّ — مُتَعَلِّقٌ بِـ«جَاءَتْ»، لَغْوٌ. وَالْمَعْنَى: أَحْضَرَتْنِي.",
      "The ba is the ba of TRANSITIVITY and the ya is a pronoun in the position of jarr — attaching to «came», laghw. جَاءَ بِهِ means «he brought it»: the letter is what turns an intransitive verb into a transitive one, and Arabic prefers that to a second verb.",
      "Bâ, TA'DİYE bâsıdır; yâ mahallen mecrûr zamirdir — «جَاءَتْ»ya taalluk eder, lağvdır. «جَاءَ بِهِ» «onu getirdi» demektir: harf, lâzım bir fiili müteaddî kılar; Arapça bunu ikinci bir fiile tercih eder.",
      segments=[seg("بِ","bi","prep"), seg("ي","pron-1s","pron")]),
  tok("إِلَيْكَ","ila","prep",["huruf-jarr"],
      "«إِلَى» حَرْفُ جَرٍّ وَالْكَافُ فِي مَحَلِّ جَرٍّ — وَقُلِبَتْ أَلِفُهَا يَاءً لِاتِّصَالِ الضَّمِيرِ.",
      "«ila» is a jarr letter and the kaf is in the position of jarr — and its alif maqsura has turned into a YA because a pronoun clung to it. عَلَى and إِلَى and حَتَّى all do this, and no other jarr letter does.",
      "«إِلَى» cer harfidir, kâf mahallen mecrûrdur — zamir bitiştiği için elif-i maksûresi YÂYA kalbolmuştur. «عَلَى», «إِلَى» ve «حَتَّى» bunu yapar; başka hiçbir cer harfi yapmaz.",
      segments=[seg("إِلَى","ila","prep"), seg("كَ","pron-2ms","pron")],
      punct="—"),
  tok("جَاءَتْ","jaa","verb",["fail"],
      "فِعْلٌ مَاضٍ وَالتَّاءُ لِلتَّأْنِيثِ — وَهُوَ الْفِعْلُ نَفْسُهُ، وَقَدْ تَغَيَّرَ فَاعِلُهُ وَحْدَهُ.",
      "The same mazi verb over again — and NOTHING in it has changed. Only the doer has moved, and that is the whole difference between the figure and the truth underneath it.",
      "Aynı mâzî fiil, yeniden — ve içinde hiçbir şey değişmedi. Yalnız fâil yer değiştirdi; mecâz ile altındaki hakîkat arasındaki bütün fark budur."),
  tok("بِي","bi","prep",["huruf-jarr","ya-al-mutakallim"],
      "الْبَاءُ لِلتَّعْدِيَةِ وَالْيَاءُ فِي مَحَلِّ جَرٍّ.",
      "The ba of transitivity, the ya in the position of jarr.",
      "Ta'diye bâsı; yâ mahallen mecrûr.",
      segments=[seg("بِ","bi","prep"), seg("ي","pron-1s","pron")]),
  tok("نَفْسِي","nafs","noun",["fail","idafa-definiteness","ya-al-mutakallim"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، مَنَعَ مِنْ ظُهُورِهَا اشْتِغَالُ الْمَحَلِّ بِحَرَكَةِ الْمُنَاسَبَةِ — وَهُوَ مُضَافٌ وَالْيَاءُ مُضَافٌ إِلَيْهِ.",
      "The fa'il in raf' by a damma ESTIMATED on the letter before the speaker's ya, kept from appearing because the place is already taken by the KASRA OF SUITABILITY — the kasra that has to be there so the ya can stand. It is a mudaf and the ya is what it is annexed to. Every noun that takes this ya loses its case-vowel the same way, in all three cases: كِتَابِي is raf', nasb and jarr and looks identical in each.",
      "Merfû fâil; ref' alâmeti, mütekellim yâsından önceki harfte MUKADDER dammedir — görünmesine engel, mahallin MÜNÂSEBET HAREKESİYLE meşgul olmasıdır; yâ ayakta durabilsin diye orada bulunması zorunlu olan kesra. Kelime muzâftır, yâ muzâfun ileyhtir. Bu yâyı alan her isim, üç i'râbın hepsinde harekesini aynı şekilde kaybeder: «كِتَابِي» ref'de de nasbda da cerde de aynı görünür."),
  tok("إِلَيْكَ","ila","prep",["huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِـ«جَاءَتْ».",
      "A jarr and majrur attaching to «came».",
      "«جَاءَتْ»ya taalluk eden câr-mecrûr.",
      segments=[seg("إِلَى","ila","prep"), seg("كَ","pron-2ms","pron")]),
  tok("بِسَبَبِ","sabab","noun",["huruf-jarr","idafa-definiteness"],
      "الْبَاءُ حَرْفُ جَرٍّ وَ«سَبَبِ» مَجْرُورٌ وَهُوَ مُضَافٌ.",
      "The ba is a jarr letter and «cause» is majrur and a mudaf. The literal sentence has to SPELL OUT the causal link in three extra words; the figure got it for nothing by hanging the verb on the cause itself. That economy is the reason anyone speaks in figures at all.",
      "Bâ cer harfi, «سَبَبِ» mecrûr ve muzâftır. Hakîkî cümle, sebep bağını üç fazla kelimeyle AÇIKÇA söylemek zorundadır; mecâz ise fiili doğrudan sebebe asarak bunu bedava elde etmişti. İnsanların mecâzla konuşmasının sebebi bu tasarruftur.",
      segments=[seg("بِ","bi","prep"), seg("سَبَبِ","sabab","noun")]),
  tok("مَحَبَّتِكَ","mahabba","noun",["idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — وَقَدْ كَانَ مُبْتَدَأً فِي الْمَجَازِ فَصَارَ مَجْرُورًا هُنَا.",
      "The mudaf ilayh in jarr, itself a mudaf with the kaf annexed — and it was the MUBTADA of the figure. Raised there, put down here: the same demotion the fifth chapter showed in نَهْرٌ جَارٍ / جَرَى مَاءُ النَّهْرِ, and it happens in every one of these pairs without exception.",
      "Mecrûr muzâfun ileyh; kendisi de muzâftır, kâf muzâfun ileyhtir — ve mecâzda MÜBTEDÂ idi. Orada yükseltilmiş, burada indirilmiştir: beşinci bâbın «نَهْرٌ جَارٍ / جَرَى مَاءُ النَّهْرِ»de gösterdiği indirmenin aynısı; ve bu çiftlerin istisnasız hepsinde olur.",
      punct="."),
 ],
 "jumal": [J("جَاءَتْ بِي إِلَيْكَ",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَإِ.",
   "A verbal sentence in the position of raf' as the khabar.",
   "Haber olarak mahallen merfû fiil cümlesi.")]})

# ---------------------------------------------------------------- s3
S.append({"id": "s3", "translation": {
 "en": "«The commander routed the army.» «What wore it away was Allah's word to the sun: rise!»",
 "tr": "«Emîr orduyu bozguna uğrattı.» «Onu, Allah'ın güneşe ‹doğ› demesi fânî kıldı.»"},
 "tokens": [
  tok("هَزَمَ","hazama","verb",["fail","maful-bihi","majaz-aqli","qarinat-al-majaz"],
      "فِعْلٌ مَاضٍ مِنْ بَابِ ضَرَبَ يَضْرِبُ.",
      "A mazi verb of the bab daraba. And the qarina here is of the SECOND grade: a single commander routing a whole army is not impossible in itself — a mind can picture it — but it does not HAPPEN, and that customary impossibility is enough to settle the reading. عَادَةً, not عَقْلًا, and the books keep the two apart because the strength of the signal differs.",
      "Darabe bâbından mâzî fiil. Karîne burada İKİNCİ derecedendir: tek bir emîrin bütün bir orduyu bozguna uğratması zâtında imkânsız değildir — akıl bunu tasavvur eder — fakat OLMAZ; ve bu âdet üzere imkânsızlık okuyuşu belirlemeye yeter. AKLEN değil ÂDETEN; kitaplar ikisini ayrı tutar, çünkü karînenin kuvveti farklıdır."),
  tok("الْأَمِيرُ","amir","noun",["fail","sifa-mushabbaha"],
      "فَاعِلٌ مَرْفُوعٌ — وَهُوَ السَّبَبُ الْآمِرُ لَا الْمُبَاشِرُ.",
      "The fa'il in raf' — and he is the commanding CAUSE, not the one who did it with his hands. The same mulabis as بَنَى الْأَمِيرُ الْمَدِينَةَ one chapter back, and the same word.",
      "Merfû fâil — emreden SEBEPtir, bizzat yapan değil. Bir önceki bâbdaki «بَنَى الْأَمِيرُ الْمَدِينَةَ» ile aynı mülâbes, hem de aynı kelime."),
  tok("الْجُنْدَ","jund","noun",["maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — اسْمُ جَمْعٍ.",
      "The object in nasb — a collective noun: one word, many men, and the singular verb agrees with the WORD.",
      "Mansub mef'ûlün bih — ism-i cem'dir: tek kelime, çok adam; ve müfred fiil KELİMEYE mutâbakat eder.",
      punct="."),
  tok("أَفْنَاهُ","afna","verb",["fail","maful-bihi","form-iv-verbs","naqis-verbs"],
      "فِعْلٌ مَاضٍ مِنَ الْإِفْعَالِ نَاقِصٌ، مَبْنِيٌّ عَلَى فَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْهَاءُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ — وَأَلِفُهُ الْمَقْصُورَةُ كُتِبَتْ أَلِفًا مَمْدُودَةً لِاتِّصَالِ الضَّمِيرِ.",
      "A mazi of Form IV and DEFECTIVE, mabni on a fatha estimated on the alif, with the ha as its object in the position of nasb — and notice the SPELLING: أَفْنَى ends in an alif maqsura, but the moment a pronoun clings to it the alif is written full. The app's own paradigm lookup had to be taught this, because a stored أَفْنَى never matches a written أَفْنَاهُ otherwise.",
      "İF'ÂL bâbından NÂKIS mâzî; elif üzerinde mukadder fetha ile mebnîdir, hâ ise mahallen mansub mef'ûlün bihtir — ve YAZILIŞA dikkat: «أَفْنَى» elif-i maksûre ile biter, fakat bir zamir bitişir bitişmez elif uzun yazılır. Uygulamanın çekim araması bunu öğrenmek zorunda kaldı; aksi hâlde kayıtlı «أَفْنَى», yazılı «أَفْنَاهُ» ile hiç eşleşmez."),
  tok("قِيلُ","qil","noun",["fail","masdar","imal-al-masdar","idafa-definiteness","qarinat-al-majaz"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — مَصْدَرُ «قَالَ» عَلَى فِعْلٍ، عَامِلٌ عَمَلَ فِعْلِهِ.",
      "The fa'il in raf' and a mudaf — a masdar of قَالَ on the pattern فِيل, GOVERNING as its verb does. Chapter 5 had a masdar annexed to its object; this one is annexed to its DOER, and the jarr phrase after it is the masdar's own complement. And here the qarina is LAFZIYYA: the line before this one hung the greying on «the pull of the nights», and this line names what really did it. A word on the page settles it, and nothing has to be reasoned out.",
      "Merfû fâil ve muzâf — «قَالَ»nin FÎL vezninde masdarı; fiili gibi AMEL EDER. Beşinci bâbda masdar mef'ûlüne izâfe edilmişti; bu ise FÂİLİNE izâfedir ve ardındaki câr-mecrûr masdarın kendi mütemmimidir. Karîne burada LAFZİYYEdir: bir önceki mısra ağarmayı «gecelerin çekişi»ne asmıştı, bu mısra ise gerçekte kimin yaptığını söyler. Sayfadaki bir kelime meseleyi bitirir; hiçbir şeyin akılla çıkarılmasına gerek kalmaz."),
  tok("اللهِ","allah","propn",["idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَهُوَ فَاعِلُ الْمَصْدَرِ فِي الْمَعْنَى.",
      "The mudaf ilayh in jarr — and the DOER of the masdar in meaning. The lam is thickened here and thinned after a kasra, which is the one word in the language whose lam behaves so.",
      "Mecrûr muzâfun ileyh — ve mânen masdarın FÂİLİdir. Lâfza-i celâlin lâmı burada ince okunur (kesradan sonra); lâmı bu şekilde davranan tek kelimedir."),
  tok("لِلشَّمْسِ","shams","noun",["huruf-jarr","zarf-mustaqarr-wa-laghw"],
      "اللَّامُ حَرْفُ جَرٍّ وَ«الشَّمْسِ» مَجْرُورٌ، وَأَلِفُ «أَلْ» مَحْذُوفَةٌ خَطًّا — مُتَعَلِّقٌ بِـ«قِيلُ»، لَغْوٌ.",
      "The lam is a jarr letter and «the sun» is majrur, the article's alif dropped in writing — the phrase attaching to «the word of», which is a masdar, so it is LAGHW. A jarr phrase hanging on a MASDAR is the case that makes the mustaqarr/laghw rule worth stating: the governor need not be a verb, only something carrying a verb's meaning.",
      "Lâm cer harfi, «الشَّمْسِ» mecrûr; «أَلْ»in elifi yazıda düşmüştür — terkîb, bir masdar olan «قِيلُ»ye taalluk eder, öyleyse LAĞVdır. Câr-mecrûrun bir MASDARA asılması, müstakar/lağv kāidesini söylemeye değer kılan hâldir: âmilin fiil olması gerekmez, fiilin mânâsını taşıması yeter.",
      segments=[seg("لِ","li","prep"), seg("الشَّمْسِ","shams","noun")]),
  tok("اطْلُعِي","talaa","verb",["imperative-amr","khabar-insha"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَيَاءُ الْمُخَاطَبَةِ فَاعِلٌ فِي مَحَلِّ رَفْعٍ — وَالْجُمْلَةُ مَقُولُ الْقَوْلِ.",
      "An imperative MABNI ON THE DELETION OF THE NUN, and the ya of the feminine addressee is its FA'IL, in the position of raf' — the clause being what the «word» consisted of. Set it beside ابْنِ at the head of this chapter: one imperative is built on a deleted LETTER OF WEAKNESS and one on a deleted NUN, and the difference is only whether the verb had five-verb endings to lose.",
      "NÛNUN HAZFİ üzere mebnî emir fiili; muhâtaba yâsı ise mahallen merfû FÂİLİdir — cümle, «قِيل»in mekūlüdür. Bu bâbın başındaki «ابْنِ» ile yan yana koyun: emirlerden biri düşmüş bir İLLET HARFİ üzerine, öteki düşmüş bir NÛN üzerine mebnîdir; fark yalnızca fiilin kaybedecek ef'âl-i hamse sonu olup olmamasıdır.",
      punct="."),
 ],
 "jumal": [J("هَزَمَ الْأَمِيرُ الْجُنْدَ",
   "جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, with no position in i'rab.",
   "Fiil cümlesi; i'râbdan mahalli yoktur."),
  J("اطْلُعِي",
   "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ مَقُولُ الْقَوْلِ.",
   "A verbal sentence of insha — what the «word» consisted of.",
   "«قِيل»in mekūlü olan inşâî fiil cümlesi.")]})

# ---------------------------------------------------------------- s4
S.append({"id": "s4", "translation": {
 "en": "«So their trade did not profit.» «Seeing you gladdened me.»",
 "tr": "«Ticaretleri kâr etmedi.» «Seni görmek beni sevindirdi.»"},
 "tokens": [
  tok("فَمَا","ma-nafiya","part",["anwa-ma"],
      "الْفَاءُ عَاطِفَةٌ، وَ«مَا» نَافِيَةٌ لَا عَمَلَ لَهَا — دَخَلَتْ عَلَى الْفِعْلِ فَتَعَيَّنَ النَّفْيُ.",
      "The fa is a joining letter and «ma» is a NEGATION that governs nothing — a verb follows it directly, which settles the reading: the relative and the masdar-making readings both need something else in place. One of the twelve faces, chosen by the plainest signal there is.",
      "Fâ atıf harfi, «مَا» ise amel etmeyen NEFİY mâsıdır — doğrudan fiile dâhil olmuştur, bu da okuyuşu tayin eder: mevsûl ve masdariyye okumalarının her ikisi de başka şeyler ister. On iki vecihten biri, mevcut en sade işaretle seçilmiştir.",
      segments=[seg("فَ","fa","conj"), seg("مَا","ma-nafiya","part")]),
  tok("رَبِحَتْ","rabiha","verb",["fail","majaz-aqli","qarinat-al-majaz"],
      "فِعْلٌ مَاضٍ مِنْ بَابِ سَمِعَ يَسْمَعُ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْإِسْنَادُ مَجَازٌ عَقْلِيٌّ: الرَّابِحُ التَّاجِرُ لَا التِّجَارَةُ.",
      "A mazi of the bab samia, its ta the feminine — and the ascription is an intellectual figure: the one who profits is the MERCHANT, not the trade. This is the ZAHIR end of the gradient: رَبِحَ is so rarely hung on a figurative doer that nobody has to be told, and the literal sense is available at once.",
      "Semia bâbından mâzî; tâ müennesliktir — ve isnâd mecâz-ı aklîdir: kâr eden TÜCCARdır, ticaret değil. Bu, derecelenmenin ZÂHİR ucudur: «رَبِحَ» mecâzî fâile o kadar seyrek asılır ki kimseye söylemeye gerek kalmaz; hakîkî mânâ derhâl hazırdır."),
  tok("تِجَارَتُهُمْ","tijara","noun",["fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ وَالْهَاءُ وَالْمِيمُ مُضَافٌ إِلَيْهِ.",
      "The fa'il in raf', a mudaf with the joined pronoun annexed to it.",
      "Merfû fâil ve muzâf; muttasıl zamir muzâfun ileyhtir.",
      punct="."),
  tok("سَرَّتْنِي","sarra","verb",["maful-bihi","doubled-verbs","majaz-aqli","ya-al-mutakallim"],
      "فِعْلٌ مَاضٍ مُضَاعَفٌ مِنْ بَابِ نَصَرَ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالنُّونُ نُونُ الْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.",
      "A DOUBLED mazi of the bab nasara, its ta the feminine, then نُونُ الْوِقَايَةِ — the PROTECTING nun — and then the speaker's ya as the object, in the position of nasb. The nun is there for one reason: the speaker's ya demands a kasra before it, and a verb's ending may not be pulled into a kasra, so a nun is put in to take the blow. Nothing else in the language does this job, and it appears only before this one pronoun.",
      "Nasara bâbından MUZÂAF mâzî; tâ müenneslik, nûn ise NÛNU'L-VİKĀYE — KORUYUCU nûn — ve yâ, mahallen mansub mef'ûlün bihtir. Nûnun tek bir sebebi var: mütekellim yâsı kendisinden önce kesra ister; fiilin sonu ise kesraya çekilemez, bu yüzden darbeyi almak üzere bir nûn konur. Dilde bu işi başka hiçbir şey görmez ve yalnız bu tek zamirin önünde belirir."),
  tok("رُؤْيَتُكَ","ruya","noun",["fail","masdar","idafa-definiteness","qarinat-al-majaz"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ — مَصْدَرُ «رَأَى». وَهَذَا هُوَ الطَّرَفُ الْخَفِيُّ: إِسْنَادُ السُّرُورِ إِلَى الرُّؤْيَةِ كَثِيرٌ حَتَّى خَفِيَتْ حَقِيقَتُهُ.",
      "The fa'il in raf', a mudaf with the kaf annexed — the masdar of رَأَى. And this is the KHAFI end of the gradient: hanging gladness on a SEEING is so common that the literal sense has gone quiet, and a reader has to stop and remember that a seeing does nothing and that he gladdened himself by it. Both sentences here are majaz of the same kind; only the ear's habit differs, and the books measure a figure by that habit rather than by its logic.",
      "Merfû fâil ve muzâf; kâf muzâfun ileyhtir — «رَأَى»nın masdarı. Ve bu, derecelenmenin HAFÎ ucudur: sevinci bir GÖRMEYE asmak o kadar yaygındır ki hakîkî mânâ susmuştur; okuyucunun durup, bir görmenin hiçbir şey yapmadığını ve kendisinin onunla sevindiğini hatırlaması gerekir. Buradaki iki cümle de aynı nevi mecâzdır; farklı olan yalnızca kulağın alışkanlığıdır — ve kitaplar bir mecâzı mantığıyla değil, bu alışkanlıkla ölçer.",
      punct="."),
 ],
 "jumal": [J("فَمَا رَبِحَتْ تِجَارَتُهُمْ",
   "جُمْلَةٌ فِعْلِيَّةٌ مَعْطُوفَةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A joined verbal sentence, with no position in i'rab.",
   "Ma'tûf fiil cümlesi; i'râbdan mahalli yoktur.")]})

# ---------------------------------------------------------------- s5
S.append({"id": "s5", "translation": {
 "en": "His face increases you in beauty, the more you increase it in looking.",
 "tr": "Ona bakışını artırdıkça, onun yüzü sana güzellik artırır."},
 "tokens": [
  tok("يَزِيدُكَ","zada","verb",["maful-bihi","mudari-marfu","hollow-verbs","majaz-aqli"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — أَجْوَفُ يَائِيٌّ مِنْ بَابِ ضَرَبَ، وَالْكَافُ مَفْعُولٌ بِهِ فِي مَحَلِّ نَصْبٍ.",
      "A mudari' in raf' — a HOLLOW verb whose middle radical is a ya, of the bab daraba — and the kaf is its object, in the position of nasb. The doer comes after the object here, which Arabic allows freely and which puts the surprise at the end of the line.",
      "Merfû muzâri fiil — darabe bâbından AJVEF YÂÎ; kâf ise mahallen mansub mef'ûlün bihtir. Fâil burada mef'ûlden sonra geliyor; Arapça buna serbestçe izin verir ve sürprizi mısraın sonuna koyar."),
  tok("وَجْهُهُ","wajh","noun",["fail","idafa-definiteness","majaz-aqli","qarinat-al-majaz"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْإِسْنَادُ مَجَازٌ عَقْلِيٌّ خَفِيٌّ.",
      "The fa'il in raf', a mudaf with the ha annexed — and the ascription is an intellectual figure of the HIDDEN kind. A face increases nobody in anything; the looker's own looking does. زَادَ is hung on figurative doers so constantly that the line reads as plain speech, which is exactly what Abu Nuwas wanted.",
      "Merfû fâil ve muzâf; hâ muzâfun ileyhtir — ve isnâd, HAFÎ nevinden mecâz-ı aklîdir. Bir yüz kimseye bir şey artırmaz; artıran, bakanın kendi bakışıdır. «زَادَ» mecâzî fâillere o kadar sürekli asılır ki mısra sıradan bir söz gibi okunur — Ebû Nüvâs'ın istediği de tam budur."),
  tok("حُسْنًا","husn","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ — نَكِرَةٌ، يُفَسِّرُ الْجِهَةَ الَّتِي وَقَعَتْ فِيهَا الزِّيَادَةُ.",
      "A TAMYIZ in nasb — indefinite, telling you in WHAT RESPECT the increase happened. It is not the object: the object is the kaf attached to the verb. A mansub indefinite after a full sentence answers «in what way?», and that is the whole of the tamyiz.",
      "Mansub TEMYÎZ — nekre; artışın HANGİ CİHETTE olduğunu açıklar. Mef'ûl değildir: mef'ûl, fiile bitişik kâftır. Tam bir cümleden sonra gelen mansub nekre «ne bakımdan?» sorusuna cevap verir; temyîzin tamamı da budur."),
  tok("إِذَا","idha","part",["idha-shartiyya"],
      "ظَرْفٌ لِمَا يُسْتَقْبَلُ مِنَ الزَّمَانِ، خَافِضٌ لِشَرْطِهِ مُتَعَلِّقٌ بِجَوَابِهِ.",
      "A zarf for future time, annexing the condition to itself and hanging on the answer. It is a NOUN, not a letter, and it does not govern jazm — the first thing every madrasah student is corrected on.",
      "Gelecek zaman için zarftır; şartını kendisine izâfe eder ve cevabına taalluk eder. İSİMdir, harf değil; ve cezmetmez — her medrese talebesinin ilk düzeltildiği şey budur."),
  tok("مَا","ma-zaida","part",["anwa-ma"],
      "زَائِدَةٌ لِلتَّوْكِيدِ، لَا عَمَلَ لَهَا وَلَا تُغَيِّرُ مِنْ مَعْنَى الشَّرْطِ شَيْئًا.",
      "ZA'IDA — added for emphasis. It governs nothing and takes nothing away: إِذَا مَا means what إِذَا means, only more firmly. Read as a negation it would turn the whole protasis inside out, and «extra ma after a conditional» is precisely the rule that stops that happening. This is the twelfth face, and the one a reader is most likely to misread.",
      "Te'kîd için ZÂİDdir. Amel etmez ve hiçbir şeyi eksiltmez: «إِذَا مَا», «إِذَا»nın söylediğini söyler, yalnız daha kuvvetle. Nefiy diye okunsa şartın tamamı tersine dönerdi; «şart edatından sonra gelen mâ zâiddir» kāidesinin varlık sebebi tam olarak budur. On ikinci vecih budur ve okuyucunun en çok yanılacağı vecihtir."),
  tok("زِدْتَهُ","zada","verb",["fail","maful-bihi","hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — وَحُذِفَتْ عَيْنُهُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "A mazi MABNI ON THE SUKUN because the doer's ta has joined it, the ta is the fa'il and the ha is the object — and the hollow verb's middle letter has DROPPED, because the sukun of the ta met the ya and two quiescents cannot stand. زَادَ becomes زِدْتَ, and the kasra left behind is the only trace of the vanished ya. This is the single most characteristic thing a hollow verb does, and the same verb stands four words earlier with its ya intact.",
      "Fâil tâsına bitiştiği için SÜKÛN üzere mebnî mâzî; tâ fâil, hâ mef'ûlün bihtir — ve ecvef fiilin ayn harfi DÜŞMÜŞTÜR, zira tânın sükûnu yâ ile buluşmuş, iki sâkin yan yana duramamıştır. «زَادَ» «زِدْتَ» olur ve geride kalan kesra, kaybolan yânın tek izidir. Bir ecvef fiilin yaptığı en karakteristik şey budur; ve aynı fiil, dört kelime önce yâsı yerinde duruyordu."),
  tok("نَظَرًا","nazar","noun",["tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ — وَهُوَ الثَّانِي فِي الْبَيْتِ، وَالْبَيْتُ كُلُّهُ زِيَادَةٌ فِي زِيَادَةٍ.",
      "The SECOND tamyiz in one hemistich, in nasb — and the line is an increase inside an increase: you increase your looking, the face increases your sense of its beauty, and the two tamyiz name the respect of each. Two indefinites in nasb, neither an object, and between them they teach the case better than a definition would.",
      "Tek mısrada İKİNCİ mansub temyîz — ve mısra, artış içinde artıştır: sen bakışını artırırsın, yüz sana güzellik artırır; iki temyîz de her birinin cihetini adlandırır. İki mansub nekre, ikisi de mef'ûl değil; ve ikisi birden bu bâbı bir tariften daha iyi öğretir.",
      punct="."),
 ],
 "jumal": [J("زِدْتَهُ نَظَرًا",
   "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ بِإِضَافَةِ «إِذَا» إِلَيْهَا.",
   "A verbal sentence in the position of jarr, as what «idha» is annexed to.",
   "«إِذَا»nın kendisine izâfe edilmesiyle mahallen mecrûr fiil cümlesi."),
  J("يَزِيدُكَ وَجْهُهُ حُسْنًا",
   "جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
   "A verbal sentence, with no position in i'rab.",
   "Fiil cümlesi; i'râbdan mahalli yoktur.")]})

GLOSS_ADD = {
 "haman":   g("هَامَان", None, "propn", "Haman (Pharaoh's minister)", "Hâmân (Fir'avn'ın veziri)", 3),
 "sarh":    g("صَرْح", "ص ر ح", "noun", "a lofty tower, a palace", "kule, yüksek köşk", 4, plural="صُرُوح"),
 "mahabba": g("مَحَبَّة", "ح ب ب", "noun", "love (masdar of أَحَبَّ)", "sevgi, muhabbet (أَحَبَّ masdarı)", 2),
 "hazama":  g("هَزَمَ", "ه ز م", "verb", "to rout, to put to flight", "bozguna uğratmak, hezimete uğratmak", 3, form="I"),
 "jund":    g("جُنْد", "ج ن د", "noun", "army, troops (a collective)", "ordu, asker (ism-i cem')", 3, plural="جُنُود"),
 "afna":    g("أَفْنَى", "ف ن ي", "verb", "to wear away, to make perish", "fânî kılmak, yok etmek", 4, form="IV"),
 "qil":     g("قِيل", "ق و ل", "noun", "a saying, the act of saying (masdar of قَالَ)", "söyleme, kavl (قَالَ masdarı)", 4),
 "shams":   g("شَمْس", "ش م س", "noun", "the sun", "güneş", 1, plural="شُمُوس"),
 "talaa":   g("طَلَعَ", "ط ل ع", "verb", "to rise (of a heavenly body)", "doğmak (gök cismi)", 2, form="I"),
 "rabiha":  g("رَبِحَ", "ر ب ح", "verb", "to profit, to gain", "kâr etmek, kazanmak", 2, form="I"),
 "tijara":  g("تِجَارَة", "ت ج ر", "noun", "trade, commerce", "ticaret", 2),
 "sarra":   g("سَرَّ", "س ر ر", "verb", "to gladden, to please", "sevindirmek", 3, form="I"),
 "zada":    g("زَادَ", "ز ي د", "verb", "to increase (something, in something)", "artırmak, ziyâde etmek", 2, form="I"),
 "nazar":   g("نَظَر", "ن ظ ر", "noun", "a look, looking", "bakış, nazar", 2),
 "ma-nafiya": g("مَا (النَّافِيَة)", None, "part", "not (the negating ma)", "değil, -medi (nefiy mâsı)", 2),
 "ma-zaida":  g("مَا (الزَّائِدَة)", None, "part", "extra ma — emphasis only, governs nothing", "zâid mâ — yalnız te'kîd, amel etmez", 4),
 # COPIED from other packages, lemma-identical — a lex key is global.
 "ya":      g("يَا", None, "part", "O — the vocative letter", "ey (nidâ harfi)", 1),
 "jaa":     g("جَاءَ", "ج ي أ", "verb", "to come", "gelmek", 1, form="I"),
 "bi":      g("بِ", None, "prep", "with, by; (with جَاءَ) to bring", "ile; (جَاءَ ile) getirmek", 1),
 "nafs":    g("نَفْس", "ن ف س", "noun", "self, soul", "nefis, kendi", 2, plural="نُفُوس"),
 "sabab":   g("سَبَب", "س ب ب", "noun", "cause, reason", "sebep", 2, plural="أَسْبَاب"),
 "ruya":    g("رُؤْيَة", "ر أ ي", "noun", "seeing, sight (masdar of رَأَى)", "görme, rü'yet (رَأَى masdarı)", 3),
 "allah":   g("اللَّه", None, "propn", "Allah", "Allah", 0),
 "pron-1s":  g("ـي", None, "pron", "my; me (attached pronoun — the speaker's ya)", "benim; beni (bitişik zamir — mütekellim yâsı)", 1),
 "pron-2ms": g("كَ", None, "pron", "you (masc. sg., attached)", "sen/senin (muttasıl, eril)", 1),
 "husn":     g("حُسْن", "ح س ن", "noun", "beauty, goodness", "güzellik, hüsün", 2),
}

def build_morph():
    out = {}
    for pkg, lex in [("wasiyyat-abi-yusuf-l5", "jaa")]:
        m = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))
        out[lex] = m["verbs"][lex]
    # هَزَمَ — Form I sound, bab daraba.
    out["hazama"] = _sg.sound1("daraba", "هَزَم", "هْزِم", "اِهْزِم", "هَزِيمَة", "هَازِم",
                               "مَهْزُوم", "هُزِمَ", "يُهْزَمُ")
    # طَلَعَ — Form I sound, bab nasara. Its feminine imperative is the word the
    # poet puts in the mouth of the command: اُطْلُعِي.
    out["talaa"] = _sg.sound1("nasara", "طَلَع", "طْلُع", "اُطْلُع", "طُلُوع", "طَالِع")
    # رَبِحَ — Form I sound, bab samia.
    out["rabiha"] = _sg.sound1("samia", "رَبِح", "رْبَح", "اِرْبَح", "رِبْح", "رَابِح")
    # زَادَ — Form I AJWAF YA'I, bab daraba. زِدْتَ is the cell the last sentence
    # turns on: the ya drops before the doer's ta.
    out["zada"] = _sg.hollow1("daraba", "أَجْوَفُ يَائِيٌّ", "زَاد", "زِد", "زِيد", "زِد",
                              "زِيد", "زِد", "زِيَادَة", "زَائِد", "مَزِيد",
                              "زِيدَ", "يُزَادُ", _sg.HOLLOW_NOTE.format(ex="زِدْتَ"))
    # أَفْنَى — Form IV NAQIS. Written أَفْنَاهُ the moment a pronoun clings to it.
    out["afna"] = _sg.derived_naqis(_sg.B4 + " — نَاقِصٌ", _sg.W4, "ُ", "أَفْنَ", "فْن", "i", "أَفْن",
                                    "إِفْنَاء", "مُفْنٍ", "مُفْنًى", "أُفْنِيَ", "يُفْنَى",
                                    "نَاقِصٌ مِنَ الْإِفْعَالِ: يُفْنِي ← لَمْ يُفْنِ.")
    # سَرَّ — Form I MUDAAF, bab nasara. Spelled out cell by cell like مَرَّ and
    # ضَمَّ before it: the fakk appears exactly where a sukun would have met the
    # doubled letter, and nowhere else.
    out["sarra"] = _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ",
                             "سُرُور", "سَارّ", _sg.mazi14("سَرّ", "سَرَر"),
                             _sg.mudari14("َ", "سُرّ", "سْرُر"),
                             ["سُرَّ", "سُرَّا", "سُرُّوا", "سُرِّي", "سُرَّا", "اُسْرُرْنَ"],
                             "يَسُرَّ", "يَسُرَّ", "تَسُرَّ", "مَسْرُور", "سُرَّ", "يُسَرُّ",
                             "مُضَاعَفٌ: الْجَزْمُ بِالْفَتْحِ — لَمْ يَسُرَّ، وَيَجُوزُ لَمْ يَسْرُرْ.")
    return out

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/6.json").write_text(
    json.dumps({"chapter": 6, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 6 for c in man["chapters"]):
    man["chapters"].append({"n": 6, "title": TITLE6})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.6.0"
ADD_EN = (" Chapter 6 is built the same way from the same file (lines ~600-621), which gives all "
          "six of its examples in vowelled Arabic: the Ghafir verse, the two impossibility "
          "examples with the literal sentence of the first, Abu al-Najm's line, the Baqara verse "
          "and Abu Nuwas's hemistich.")
ADD_TR = (" Altıncı bâb da aynı dosyadan (satır ~600-621) aynı usûlle kurulmuştur; o satırlar altı "
          "misalin hepsini harekeli Arapça olarak verir: Ğâfir âyeti, iki imkânsızlık misali ve "
          "birincisinin hakîkî cümlesi, Ebü'n-Necm'in mısraı, Bakara âyeti ve Ebû Nüvâs'ın mısraı.")
if "Ghafir" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].update(build_morph())
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch6:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
