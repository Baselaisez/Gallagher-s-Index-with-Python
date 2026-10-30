# -*- coding: utf-8 -*-
"""Author chapter 36 of talkhis-al-miftah — التَّوَسُّطُ بَيْنَ الْكَمَالَيْنِ.

Sahifa 84-85 (lines ~2434-2470): the wasl's second da'i — the jumlas
agree in khabar/insha (in word and sense, or in sense alone) AND share a
jihat jamia, so the waw is due:

  • يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ (an-Nisa 4:142, part) — fi'liyya
    joined to ismiyya; the jiha is the TADAYUF of mukhada'a (deceit is
    between two).
  • إِنَّ الْأَبْرَارَ لَفِي نَعِيمٍ وَإِنَّ الْفُجَّارَ لَفِي جَحِيمٍ
    (al-Infitar 82:13-14) — two ismiyyas; the jiha is TADAD.
  • وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا (al-A'raf 7:31, part) — three
    inshas; one musnad-ilayh, related musnads.
  • the source's own drill pairs: زَيْدٌ شَاعِرٌ وَعَمْرٌو كَاتِبٌ (the
    jiha holds in BOTH musnad and musnad-ilayh — wasl), زَيْدٌ شَاعِرٌ
    وَعَمْرٌو طَوِيلٌ (poet-hood and tallness never meet — the atf is
    WRONG, and the sentence is taught as the counter-example), and
    أَبُو زَيْدٍ يَشْعُرُ وَابْنُهُ يَكْتُبُ (the jiha is the TADAYUF of
    father and son).

ATTRIBUTION: s1-s4 are Qur'anic text quoted exactly in standard imla as
the source prints them (4:142 part; 82:13-14; 7:31 part); s5-s7 are the
source's own drill sentences, verbatim.

Grammar this chapter teaches:
  • note 140 `tawassut-bayna-al-kamalayn` — the second wasl da'i, the
    rule that the jiha must hold in BOTH musnad and musnad-ilayh, and
    Sakkaki's division of the jiha (aqli: ittihad / tamathul / tadayuf;
    wahmi and khayali named — their witnesses arrive with the next
    chapter).
  • new paradigms: خَادَعَ (Form III sound), أَكَلَ (hamza-fa on the
    akhadha road — its amr is the received takhfif كُلْ), أَسْرَفَ
    (Form IV sound); شَرِبَ copied from aqaid after the lemma identity
    check.
"""
import json, pathlib, sys, re
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
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

TITLE36 = {"ar": "التَّوَسُّطُ بَيْنَ الْكَمَالَيْنِ — الْجِهَةُ الْجَامِعَةُ",
           "en": "Between the Two Perfections: the Joining Aspect",
           "tr": "Tevassut Beyne'l-Kemâleyn: Cihet-i Câmia"}

# ------------------- s1 — Nisa 4:142: fi'liyya joined to ismiyya by tadayuf
S.append({"id": "s1", "translation": {
 "en": "They would deceive Allah — and He is their requiter. (fi'liyya joined to ismiyya: the jiha is the tadayuf of deceit, which is always between two.)",
 "tr": "Allah'ı aldatmaya kalkışırlar — O da onların karşılığını verendir. (isim cümlesine bağlanan fiil cümlesi: cihet, hep iki taraf isteyen aldatışın tezâyüfüdür.)"},
 "tokens": [
  tok("يُخَادِعُونَ","khadaa","verb",["tawassut-bayna-al-kamalayn","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ — مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ.",
      "«they would deceive» — a Form III mudari of the five verbs, raf' by the RETAINED nun, the waw its doer.",
      "«aldatmaya kalkışırlar» — beş fiilden III. bâb muzâri; ref'i SABİT NÛN iledir, vâv fâildir."),
  tok("اللهَ","allah","propn",["tawassut-bayna-al-kamalayn"],
      "لَفْظُ الْجَلَالَةِ مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ.",
      "«Allah» — the jalala as the object, mansub.",
      "«Allah'ı» — mef'ûl olarak lafz-ı celâl; mansub."),
  tok("وَهُوَ","huwa","pron",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ — لِلتَّوَسُّطِ بَيْنَ الْكَمَالَيْنِ — وَهُوَ مُبْتَدَأٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ.",
      "«and He» — THE waw of this chapter: the wasl of tawassut. Then the detached pronoun as mubtada, mabni in a raf' position.",
      "«O da» — bu bâbın vâvı: tevassut vaslı. Sonra munfasıl zamir mübtedâ; ref mahallinde mebnî.",
      segments=[seg("وَ","wa","part"), seg("هُوَ","huwa","pron")]),
  tok("خَادِعُهُمْ","khadi","noun",["tawassut-bayna-al-kamalayn","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ، وَهُوَ مُضَافٌ وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — إِضَافَةُ اسْمِ الْفَاعِلِ إِلَى مَفْعُولِهِ.",
      "«their requiter» — the khabar, marfu'; the ism fa'il annexed to its own object. Deceit needs two parties — that mutual need IS the jihat jamia here.",
      "«onları aldatandır» — haber, merfû; kendi mef'ûlüne muzâf ism-i fâil. Aldatış iki taraf ister — buradaki cihet-i câmia tam da o karşılıklı ihtiyaçtır.",
      punct=".", segments=[seg("خَادِعُ","khadi","noun"), seg("هُمْ","pron-3mp","pron")])],
 "jumal": [
  J("يُخَادِعُونَ اللهَ",
    "جُمْلَةٌ فِعْلِيَّةٌ خَبَرِيَّةٌ.",
    "The verbal clause — their attempt.",
    "Fiil cümlesi — onların kalkışması."),
  J("وَهُوَ خَادِعُهُمْ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — الْجِهَةُ الْجَامِعَةُ التَّضَايُفُ فِي الْمُخَادَعَةِ.",
    "The nominal clause, JOINED: both clauses stand in one mukhada'a, and a deceit's two sides need each other to exist — tadayuf, the source's own jiha for this aya.",
    "İsim cümlesi, BAĞLI: iki cümle tek mühâdaada durur ve aldatışın iki tarafı var olmak için birbirine muhtaçtır — tezâyüf; kaynağın bu âyet için verdiği cihet.")]})

# ------------------------------ s2 — Infitar 82:13: the first half of the tibaq
S.append({"id": "s2", "translation": {
 "en": "Indeed the righteous are surely in bliss —",
 "tr": "Şüphesiz iyiler, elbette nimet içindedirler —"},
 "tokens": [
  tok("إِنَّ","inna","part",["tawassut-bayna-al-kamalayn","inna-wa-akhawatuha"],
      "حَرْفٌ نَاسِخٌ يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "«indeed» — the nasikh: nasb on its ism, raf' on its khabar.",
      "«şüphesiz» — nâsih: ismini nasb, haberini raf eder."),
  tok("الْأَبْرَارَ","abrar","noun",["tawassut-bayna-al-kamalayn"],
      "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«the righteous» — inna's ism, mansub by the plain fatha.",
      "«iyiler» — إِنَّ'nin ismi; açık fethayla mansub."),
  tok("لَفِي","fi","part",["tawassut-bayna-al-kamalayn","inna-wa-akhawatuha"],
      "اللَّامُ الْمُزَحْلَقَةُ، وَفِي حَرْفُ جَرٍّ.",
      "«surely in» — the sliding lam of emphasis riding the jarr letter: the khabar arrives as a shibh jumla.",
      "«elbette içinde» — cer harfine binmiş kayan lâm: haber, şibh cümle olarak gelir.",
      segments=[seg("لَ","li","part"), seg("فِي","fi","part")]),
  tok("نَعِيمٍ","naim","noun",["tawassut-bayna-al-kamalayn"],
      "مَجْرُورٌ بِفِي — وَشِبْهُ الْجُمْلَةِ فِي مَحَلِّ رَفْعٍ خَبَرُ إِنَّ.",
      "«bliss» — majrur; the phrase stands in raf' position as inna's khabar.",
      "«nimet» — mecrur; öbek, ref mahallinde إِنَّ'nin haberidir.",
      punct="•")],
 "jumal": [
  J("إِنَّ الْأَبْرَارَ لَفِي نَعِيمٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مُؤَكَّدَةٌ بِإِنَّ وَاللَّامِ.",
    "The first report, doubly emphasized — bliss for the righteous.",
    "İlk haber, çifte te'kîdli — iyilere nimet."),
  J("لَفِي نَعِيمٍ",
    "شِبْهُ جُمْلَةٍ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
    "The jarr phrase doing a khabar's work.",
    "Haber işi gören câr-mecrûr öbeği.")]})

# ------------------------------- s3 — Infitar 82:14: joined across the tadad
S.append({"id": "s3", "translation": {
 "en": "— and indeed the wicked are surely in a blaze. (two ismiyyas joined: the jiha is TADAD — bliss against blaze, righteous against wicked.)",
 "tr": "— ve şüphesiz kötüler, elbette alevli ateş içindedirler. (bağlanmış iki isim cümlesi: cihet TEZÂDDIR — nimete karşı ateş, iyiye karşı kötü.)"},
 "tokens": [
  tok("وَإِنَّ","inna","part",["tawassut-bayna-al-kamalayn","inna-wa-akhawatuha"],
      "الْوَاوُ عَاطِفَةٌ لِلتَّوَسُّطِ بَيْنَ الْكَمَالَيْنِ، وَإِنَّ حَرْفٌ نَاسِخٌ.",
      "«and indeed» — the tawassut waw again, then the nasikh.",
      "«ve şüphesiz» — yine tevassut vâvı, sonra nâsih.",
      segments=[seg("وَ","wa","part"), seg("إِنَّ","inna","part")]),
  tok("الْفُجَّارَ","fujjar","noun",["tawassut-bayna-al-kamalayn"],
      "اسْمُ إِنَّ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«the wicked» — inna's ism, mansub.",
      "«kötüler» — إِنَّ'nin ismi; mansub."),
  tok("لَفِي","fi","part",["tawassut-bayna-al-kamalayn"],
      "اللَّامُ الْمُزَحْلَقَةُ، وَفِي حَرْفُ جَرٍّ.",
      "«surely in» — the same sliding lam: the two halves mirror each other clause for clause.",
      "«elbette içinde» — aynı kayan lâm: iki yarı, cümle cümle birbirini aynalar.",
      segments=[seg("لَ","li","part"), seg("فِي","fi","part")]),
  tok("جَحِيمٍ","jahim","noun",["tawassut-bayna-al-kamalayn"],
      "مَجْرُورٌ بِفِي — وَشِبْهُ الْجُمْلَةِ خَبَرُ إِنَّ. وَالْجِهَةُ الْجَامِعَةُ بَيْنَ الْجُمْلَتَيْنِ التَّضَادُّ.",
      "«a blaze» — majrur, the phrase inna's khabar. Opposites MEET in the mind — that meeting is a jiha, and the waw is due.",
      "«alevli ateş» — mecrur; öbek إِنَّ'nin haberi. Zıtlar zihinde BULUŞUR — o buluşma bir cihettir ve vâv hak olur.",
      punct="•")],
 "jumal": [
  J("وَإِنَّ الْفُجَّارَ لَفِي جَحِيمٍ",
    "جُمْلَةٌ اسْمِيَّةٌ مَعْطُوفَةٌ — الْجِهَةُ الْجَامِعَةُ التَّضَادُّ.",
    "The second report, JOINED to the first: both are khabari, both emphatic, and their subjects and predicates stand in opposition — tadad is a lawful jiha.",
    "İkinci haber, ilkine BAĞLI: ikisi de haberî, ikisi de te'kîdli; özneleri ve yüklemleri karşıtlıkta durur — tezâd meşru bir cihettir."),
  J("لَفِي جَحِيمٍ",
    "شِبْهُ جُمْلَةٍ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
    "The mirrored khabar phrase.",
    "Aynalanmış haber öbeği.")]})

# ------------------------- s4 — A'raf 7:31: three inshas on one musnad-ilayh
S.append({"id": "s4", "translation": {
 "en": "And eat and drink, and do not be wasteful. (three inshas joined: one addressee throughout, and the musnads are next of kin.)",
 "tr": "Yiyin, için; israf da etmeyin. (bağlanmış üç inşâ: baştan sona tek muhatap ve müsnedler birbirine akraba.)"},
 "tokens": [
  tok("وَكُلُوا","akala","verb",["tawassut-bayna-al-kamalayn","imperative-amr"],
      "الْوَاوُ عَاطِفَةٌ، وَكُلُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ — أَمْرُ أَكَلَ بِحَذْفِ الْهَمْزَةِ: كُلْ.",
      "«and eat» — the amr of أَكَلَ with its hamza cut away (كُلْ, one of the received light imperatives), mabni on the dropped nun, the waw its doer.",
      "«ve yiyin» — أَكَلَ'nin hemzesi atılmış emri (كُلْ — mervî hafif emirlerden); nûnun hazfi üzere mebnî, vâv fâil.",
      segments=[seg("وَ","wa","part"), seg("كُلُوا","akala","verb")]),
  tok("وَاشْرَبُوا","shariba","verb",["tawassut-bayna-al-kamalayn","imperative-amr"],
      "الْوَاوُ عَاطِفَةٌ، وَاشْرَبُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ.",
      "«and drink» — a second amr joined to the first: same addressee, neighbouring deed.",
      "«ve için» — ilkine bağlanmış ikinci emir: aynı muhatap, komşu iş.",
      segments=[seg("وَ","wa","part"), seg("اشْرَبُوا","shariba","verb")]),
  tok("وَلَا","la-nahiya","part",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ، وَلَا نَاهِيَةٌ جَازِمَةٌ.",
      "«and do not» — the joining waw with the prohibiting la.",
      "«ve …meyin» — atıf vâvı ile nehiy lâsı.",
      segments=[seg("وَ","wa","part"), seg("لَا","la-nahiya","part")]),
  tok("تُسْرِفُوا","asrafa","verb",["tawassut-bayna-al-kamalayn"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا وَعَلَامَةُ جَزْمِهِ حَذْفُ النُّونِ، وَالْوَاوُ فَاعِلٌ.",
      "«be wasteful» — a Form IV mudari, majzum by the la, its sign the dropped nun. All three clauses are insha in word and sense — agreement, plus one addressee: the wasl is due.",
      "«israf edin» — IV. bâbdan muzâri; lâ ile meczum, alâmeti nûnun hazfi, vâv fâil. Üç cümle de lafzan ve mânen inşâ — ittifak, üstüne tek muhatap: vasl hak olur.",
      punct=".")],
 "jumal": [
  J("كُلُوا … اشْرَبُوا … لَا تُسْرِفُوا",
    "ثَلَاثُ جُمَلٍ إِنْشَائِيَّةٍ مَعْطُوفَةٍ.",
    "Three commands on one thread: the eaters, the drinkers and the would-be wasters are the same people, and the deeds are next of kin.",
    "Tek iplikte üç emir: yiyen, içen ve israfa kalkışacak olan aynı insanlardır; işler de birbirine akrabadır."),
  J("لَا تُسْرِفُوا",
    "جُمْلَةُ نَهْيٍ مَعْطُوفَةٌ عَلَى الْأَمْرَيْنِ.",
    "The prohibition joined onto the two commands — insha with insha.",
    "İki emre bağlanan nehiy — inşâ inşâya.")]})

# ------------------------ s5 — the source's pair: the jiha holds in BOTH seats
S.append({"id": "s5", "translation": {
 "en": "Zayd is a poet and 'Amr is a writer. (Zayd and 'Amr are two of a kind, poetry and writing are neighbours: the jiha holds in both seats, so the waw is right.)",
 "tr": "Zeyd şairdir, Amr da yazardır. (Zeyd ile Amr birbirinin dengi, şiirle yazı komşudur: cihet iki makamda da tutar, vâv yerindedir.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["tawassut-bayna-al-kamalayn"],
      "مُبْتَدَأٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«Zayd» — the mubtada.",
      "«Zeyd» — mübtedâ."),
  tok("شَاعِرٌ","shair","noun",["tawassut-bayna-al-kamalayn","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«a poet» — the khabar.",
      "«şair» — haber."),
  tok("وَعَمْرٌو","amr-alam","propn",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ، وَعَمْرٌو مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ.",
      "«and 'Amr» — the joining waw is LAWFUL here; a second mubtada.",
      "«ve Amr» — buradaki atıf vâvı MEŞRUDUR; ikinci mübtedâ.",
      segments=[seg("وَ","wa","part"), seg("عَمْرٌو","amr-alam","propn")]),
  tok("كَاتِبٌ","katib","noun",["tawassut-bayna-al-kamalayn","ism-fail"],
      "خَبَرٌ مَرْفُوعٌ — وَالْجِهَةُ الْجَامِعَةُ قَائِمَةٌ فِي الْمُسْنَدَيْنِ وَالْمُسْنَدِ إِلَيْهِمَا مَعًا.",
      "«a writer» — the second khabar. Two comparable men, two neighbouring crafts: the jiha stands in the musnads AND the musnad-ilayhs — the books' condition for the wasl.",
      "«yazar» — ikinci haber. İki denk adam, iki komşu zanaat: cihet, müsnedlerde DE müsnedün-ileyhlerde DE durur — kitapların vasl şartı.",
      punct=".")],
 "jumal": [
  J("زَيْدٌ شَاعِرٌ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ.",
    "The first report.",
    "İlk haber."),
  J("وَعَمْرٌو كَاتِبٌ",
    "مَعْطُوفَةٌ — تَمَاثُلُ الْمُسْنَدِ إِلَيْهِمَا وَتَنَاسُبُ الْمُسْنَدَيْنِ.",
    "Joined lawfully: the subjects are two of a kind (tamathul) and the predicates two crafts of one family.",
    "Meşru bağlanış: özneler birbirinin dengi (temâsül), yüklemler tek ailenin iki zanaatı.")]})

# ----------------- s6 — the counter-example: a waw with no jiha to carry it
S.append({"id": "s6", "translation": {
 "en": "«Zayd is a poet and 'Amr is tall.» (the books' counter-example: poet-hood and tallness never meet, so THIS atf is wrong — a waw cannot buy a jiha.)",
 "tr": "«Zeyd şairdir ve Amr uzundur.» (kitapların karşı-örneği: şairlikle uzunluk buluşmaz; BU atıf yanlıştır — vâv, cihet satın alamaz.)"},
 "tokens": [
  tok("زَيْدٌ","zayd","propn",["tawassut-bayna-al-kamalayn"],
      "مُبْتَدَأٌ مَرْفُوعٌ.",
      "«Zayd» — the mubtada, as before.",
      "«Zeyd» — mübtedâ, öncekindeki gibi."),
  tok("شَاعِرٌ","shair","noun",["tawassut-bayna-al-kamalayn"],
      "خَبَرٌ مَرْفُوعٌ.",
      "«a poet» — the khabar, as before.",
      "«şair» — haber, öncekindeki gibi."),
  tok("وَعَمْرٌو","amr-alam","propn",["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ — وَالْعَطْفُ هُنَا غَيْرُ صَحِيحٍ عِنْدَ أَهْلِ الْمَعَانِي.",
      "«and 'Amr» — the same waw, and the ma'ani scholars REJECT it here: the letters are fine, the joining is not.",
      "«ve Amr» — aynı vâv; ve meânî ehli onu BURADA reddeder: harfler yerinde, bağlayış değil.",
      segments=[seg("وَ","wa","part"), seg("عَمْرٌو","amr-alam","propn")]),
  tok("طَوِيلٌ","tawil-long","noun",["tawassut-bayna-al-kamalayn"],
      "خَبَرٌ مَرْفُوعٌ — وَلَا مُنَاسَبَةَ بَيْنَ الشِّعْرِ وَالطُّولِ فَلَا جِهَةَ جَامِعَةَ.",
      "«tall» — grammatical in every letter, and still wrong: Zayd and 'Amr relate, but poetry and tallness do not, and the jiha must hold in BOTH seats.",
      "«uzun» — her harfi gramere uygun, yine de yanlış: Zeyd ile Amr alâkalı, fakat şiirle uzunluk değil; cihet İKİ makamda da tutmalı.",
      punct=".")],
 "jumal": [
  J("زَيْدٌ شَاعِرٌ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ.",
    "The first report — blameless.",
    "İlk haber — kusursuz."),
  J("وَعَمْرٌو طَوِيلٌ",
    "مَعْطُوفَةٌ عَطْفًا غَيْرَ صَحِيحٍ — الْمُسْنَدَانِ لَا يَتَنَاسَبَانِ.",
    "The rejected joining: with related subjects but unrelated predicates the waw hangs on half a jiha, and half a jiha is none.",
    "Reddedilen bağlanış: özneler alâkalı ama yüklemler alâkasızken vâv yarım cihete asılır; yarım cihet, cihet değildir.")]})

# ------------------------ s7 — tadayuf: father and son need each other to be
S.append({"id": "s7", "translation": {
 "en": "Abu Zayd writes poetry and his son writes prose. (the jiha is TADAYUF: no father without a son, no son without a father.)",
 "tr": "Ebû Zeyd şiir söyler, oğlu da yazı yazar. (cihet TEZÂYÜFTÜR: oğulsuz baba, babasız oğul olmaz.)"},
 "tokens": [
  tok("أَبُو","ab","noun",["tawassut-bayna-al-kamalayn","five-nouns"],
      "مِنَ الْأَسْمَاءِ الْخَمْسَةِ: مُبْتَدَأٌ مَرْفُوعٌ بِالْوَاوِ، وَهُوَ مُضَافٌ.",
      "«Abu (father of)» — a five-nouns head: mubtada, its raf' shown by the WAW, and a mudaf.",
      "«Ebû» — beş isimden: mübtedâ; ref'i VÂV iledir ve muzâftır."),
  tok("زَيْدٍ","zayd","propn",["tawassut-bayna-al-kamalayn"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«of Zayd» — the mudaf ilayh.",
      "«Zeyd'in» — muzâfun ileyh."),
  tok("يَشْعُرُ","shaara","verb",["tawassut-bayna-al-kamalayn"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ هُوَ — وَالْجُمْلَةُ خَبَرٌ.",
      "«writes poetry» — the mudari clause standing as the khabar.",
      "«şiir söyler» — haber olarak duran muzâri cümlesi."),
  tok("وَابْنُهُ","ibn",'noun',["tawassut-bayna-al-kamalayn"],
      "الْوَاوُ عَاطِفَةٌ، وَابْنُ مُبْتَدَأٌ ثَانٍ مَرْفُوعٌ بِالضَّمَّةِ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.",
      "«and his son» — the joined second mubtada with its pronoun annexed. Father and son EXIST through each other — the tadayuf that licenses this waw.",
      "«ve oğlu» — bağlanmış ikinci mübtedâ; zamiri muzâfun ileyh. Baba ile oğul birbiri SAYESİNDE vardır — bu vâvı meşru kılan tezâyüf.",
      segments=[seg("وَ","wa","part"), seg("ابْنُ","ibn","noun"), seg("هُ","pron-3ms","pron")]),
  tok("يَكْتُبُ","kataba","verb",["tawassut-bayna-al-kamalayn"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ هُوَ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَإِ الثَّانِي.",
      "«writes» — the second khabar clause; the two crafts are neighbours, so the musnads relate too.",
      "«yazar» — ikinci haber cümlesi; iki zanaat komşudur, müsnedler de böylece alâkalıdır.",
      punct=".")],
 "jumal": [
  J("أَبُو زَيْدٍ يَشْعُرُ",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرُهَا جُمْلَةٌ فِعْلِيَّةٌ.",
    "The father's sentence.",
    "Babanın cümlesi."),
  J("وَابْنُهُ يَكْتُبُ",
    "مَعْطُوفَةٌ — الْجِهَةُ الْجَامِعَةُ تَضَايُفُ الْأُبُوَّةِ وَالْبُنُوَّةِ.",
    "Joined by the tadayuf of fatherhood and sonship: each term is defined by the other, and the mind holds them as one pair.",
    "Babalıkla oğulluğun tezâyüfüyle bağlı: her terim ötekiyle tanımlanır ve zihin ikisini tek çift olarak tutar.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "khadaa": g("خَادَعَ", "خ د ع", "verb", "to try to deceive", "aldatmaya çalışmak", 5, form="III"),
 "khadi": g("خَادِع", "خ د ع", "noun", "deceiver; requiter of deceit (ism fa'il)", "aldatan; aldatışın karşılığını veren (ism-i fâil)", 5),
 "abrar": g("أَبْرَار", "ب ر ر", "noun", "the righteous (plural of بَرّ)", "iyiler (بَرّ'in çoğulu)", 5),
 "fujjar": g("فُجَّار", "ف ج ر", "noun", "the wicked (plural of فَاجِر)", "kötüler, günahkârlar (فَاجِر'in çoğulu)", 5),
 "akala": g("أَكَلَ", "أ ك ل", "verb", "to eat", "yemek", 1, form="I"),
 "asrafa": g("أَسْرَفَ", "س ر ف", "verb", "to be wasteful, exceed the bound", "israf etmek, haddi aşmak", 4, form="IV"),
 "naim": copy_gloss("bad-al-amali", "naim"),
 "jahim": copy_gloss("bad-al-amali", "jahim"),
 "shariba": copy_gloss("aqaid-ahl-al-sunna", "shariba"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/36.json").write_text(
    json.dumps({"chapter": 36, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 36 for c in man["chapters"]):
    man["chapters"].append({"n": 36, "title": TITLE36})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.36.0"
ADD_EN = (" Chapter 36 carries tawassut bayna l-kamalayn (lines ~2434-2470, sahifa 84-85): "
          "s1-s4 are Qur'anic text quoted exactly in standard imla as the source prints them "
          "(an-Nisa 4:142 part, al-Infitar 82:13-14, al-A'raf 7:31 part); s5-s7 are the "
          "source's own drill sentences, verbatim — s6 deliberately preserves the source's "
          "COUNTER-example, taught as a rejected joining.")
ADD_TR = (" Otuz altıncı bâb tevassut beyne'l-kemâleyni taşır (satır ~2434-2470, sahife "
          "84-85): s1-s4, kaynağın bastığı standart imlâ ile aynen alınmış Kur'ân metnidir "
          "(Nisâ 4:142 kısmen, İnfitâr 82:13-14, A'râf 7:31 kısmen); s5-s7 kaynağın kendi "
          "alıştırma cümleleridir, aynen — s6, kaynağın KARŞI-örneğini bilerek korur ve "
          "reddedilmiş bir bağlanış olarak öğretilir.")
if "2434-2470" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "khadaa" not in mo["verbs"]:
    mo["verbs"]["khadaa"] = _sg.derived(
        _sg.B3, _sg.W3, "ُ", "خَادَع", "خَادِع", "خَادِع",
        "مُخَادَعَة", "مُخَادِع", "مُخَادَع", "خُودِعَ", "يُخَادَعُ")
if "akala" not in mo["verbs"]:
    # hamza-fa on the akhadha road: mechanical أَأْكُلُ in the first person
    # (the matching layer unfolds the written آكُلُ), and the received
    # TAKHFIF amr — كُلْ, hamza cut away.
    mo["verbs"]["akala"] = _sg.entry(
        "مِنْ بَابِ نَصَرَ يَنْصُرُ — مَهْمُوزُ الْفَاءِ", "فَعَلَ يَفْعُلُ",
        "أَكْل", "آكِل",
        _sg.mazi14("أَكَل"),
        _sg.mudari14("َ", "أْكُل"),
        ["كُلْ", "كُلَا", "كُلُوا", "كُلِي", "كُلَا", "كُلْنَ"],
        "يَأْكُلَ", "يَأْكُلْ", "تَأْكُلْ",
        "مَأْكُول", "أُكِلَ", "يُؤْكَلُ",
        "مَهْمُوزُ الْفَاءِ: أَمْرُهُ «كُلْ» بِحَذْفِ الْهَمْزَةِ.")
if "asrafa" not in mo["verbs"]:
    mo["verbs"]["asrafa"] = _sg.derived(
        _sg.B4, _sg.W4, "ُ", "أَسْرَف", "سْرِف", "أَسْرِف",
        "إِسْرَاف", "مُسْرِف", "مُسْرَف", "أُسْرِفَ", "يُسْرَفُ")
_amo = json.loads((ROOT / "content/samples/aqaid-ahl-al-sunna/morphology.json")
                  .read_text(encoding="utf-8"))["verbs"]
if "shariba" not in mo["verbs"]:
    mo["verbs"]["shariba"] = _amo["shariba"]
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 140
GR = ROOT / "content/grammar"
NOTE140 = {
 "id": "tawassut-bayna-al-kamalayn",
 "title": {"ar": "التَّوَسُّطُ بَيْنَ الْكَمَالَيْنِ — الْجِهَةُ الْجَامِعَةُ",
           "en": "Between the two perfections: the joining aspect",
           "tr": "Tevassut beyne'l-kemâleyn: cihet-i câmia"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — دواعي الوصل: التوسط بين الكمالين"],
 "question": {
  "en": ["Do the two jumlas agree as khabar or as insha — in word and sense, or in sense alone? That is the first half of the wasl's licence.",
         "Does a jihat jamia bind the musnads AND the musnad-ilayhs together? Half a jiha (زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ) is none.",
         "What kind is the jiha? Sakkaki: aqli (ittihad, tamathul, tadayuf), wahmi, or khayali."],
  "tr": ["İki cümle haberlikte veya inşâlıkta uyuşuyor mu — lafzan ve mânen, yahut yalnız mânen? Vasl ruhsatının ilk yarısı budur.",
         "Cihet-i câmia, müsnedleri VE müsnedün-ileyhleri birlikte bağlıyor mu? Yarım cihet (زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ) cihet değildir.",
         "Cihet ne türden? Sekkâkî: aklî (ittihâd, temâsül, tezâyüf), vehmî veya hayâlî."]},
 "plain": {
  "en": "The wasl's second licence: the jumlas agree in kind (report with report, request with request — in word and sense, or in sense alone) AND share a joining aspect that holds in both the subjects and the predicates. Then the waw is due: يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ.",
  "tr": "Vaslın ikinci ruhsatı: cümleler türce uyuşur (haber habere, talep talebe — lafzan ve mânen, yahut yalnız mânen) VE hem öznelerde hem yüklemlerde tutan bir birleştirici cihet paylaşır. O zaman vâv hak olur: يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ."},
 "explanation": {
  "en": "TAWASSUT BAYNA L-KAMALAYN — neither perfect severance nor perfect union, and so exactly where the waw does its work. Two conditions. (1) AGREEMENT in khabari/inshai standing: both reports (إِنَّ الْأَبْرَارَ لَفِي نَعِيمٍ وَإِنَّ الْفُجَّارَ لَفِي جَحِيمٍ), or both requests (وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا) — and sense outranks word: in al-Baqara 2:83 لَا تَعْبُدُونَ is a report in word, a command in sense, and the three clauses agree in COMMAND alone, which suffices. (2) A JIHAT JAMIA holding in both seats: زَيْدٌ شَاعِرٌ وَعَمْرٌو كَاتِبٌ joins lawfully (comparable men, neighbouring crafts), while زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ is rejected outright — Zayd and 'Amr relate, poetry and tallness do not, and half a jiha is none. Sakkaki divides the jiha: AQLI — ittihad (one term shared: زَيْدٌ يَكْتُبُ وَيَشْعُرُ; and the mukhada'a of 4:142, whose two sides need each other), tamathul (two of a kind — the mind strips the two likes from their persons and the multiplicity falls away), tadayuf (each exists through the other: cause and effect, more and less, father and son — أَبُو زَيْدٍ يَشْعُرُ وَابْنُهُ يَكْتُبُ); WAHMI — resemblances the estimative faculty makes (near-likeness, opposition — the tadad of 82:13-14 — and near-opposition); KHAYALI — a closeness already settled in the imagination by habit and custom. The wahmi witnesses arrive with the next chapter.",
  "tr": "TEVASSUT BEYNE'L-KEMÂLEYN — ne tam kopuş ne tam birleşme; vâvın iş gördüğü yer tam burasıdır. İki şart. (1) Haberlik-inşâlıkta UYUŞMA: ikisi de haber (إِنَّ الْأَبْرَارَ لَفِي نَعِيمٍ وَإِنَّ الْفُجَّارَ لَفِي جَحِيمٍ) veya ikisi de talep (وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا) — ve mânâ lafzı geçer: Bakara 2:83'te لَا تَعْبُدُونَ lafzan haber, mânen emirdir; üç cümle yalnız EMİRLİKTE uyuşur, bu da yeter. (2) İki makamda da tutan CİHET-İ CÂMİA: زَيْدٌ شَاعِرٌ وَعَمْرٌو كَاتِبٌ meşru bağlanır (denk adamlar, komşu zanaatlar); زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ ise düpedüz reddedilir — Zeyd ile Amr alâkalı, şiirle uzunluk değil; yarım cihet cihet değildir. Sekkâkî ciheti böler: AKLÎ — ittihâd (ortak bir terim: زَيْدٌ يَكْتُبُ وَيَشْعُرُ; ve 4:142'nin mühâdaası — iki tarafı birbirine muhtaç), temâsül (birbirinin dengi iki şey — akıl iki dengi şahıslarından soyunca çokluk ortadan kalkar), tezâyüf (her biri ötekiyle var: illet ile ma'lûl, az ile çok, baba ile oğul — أَبُو زَيْدٍ يَشْعُرُ وَابْنُهُ يَكْتُبُ); VEHMÎ — vehmin kurduğu yakınlıklar (temâsül benzeri, tezâd — 82:13-14'ün tezâdı — ve tezâd benzeri); HAYÂLÎ — hayalde örf ve âdetle önceden yerleşmiş yakınlık. Vehmî şahitler gelecek bâbla gelir."},
 "examples": [
  {"ar": "يُخَادِعُونَ اللهَ وَهُوَ خَادِعُهُمْ",
   "en": "fi'liyya joined to ismiyya — the jiha is the tadayuf of deceit (4:142).",
   "tr": "isim cümlesine bağlı fiil cümlesi — cihet, aldatışın tezâyüfü (4:142).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "وَإِنَّ الْفُجَّارَ لَفِي جَحِيمٍ",
   "en": "two mirrored reports joined across TADAD (82:13-14).",
   "tr": "TEZÂD üzerinden bağlanmış iki aynalı haber (82:13-14).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "وَكُلُوا وَاشْرَبُوا وَلَا تُسْرِفُوا",
   "en": "three inshas, one addressee (7:31).",
   "tr": "üç inşâ, tek muhatap (7:31).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ",
   "en": "the counter-example: half a jiha is none.",
   "tr": "karşı-örnek: yarım cihet, cihet değildir.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s6"}],
 "commonMistakes": [
  {"wrong": "«İki doğru cümle her zaman vâvla bağlanabilir»",
   "right": "«Vâv, iki makamda birden tutan bir cihet-i câmia ister»",
   "why": {"en": "Truth is not the licence — RELATION is. Both halves of زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ may be true, and the joining is still rejected: the subjects relate, the predicates do not, and the waw would assert a meeting of topics that never happens. The ma'ani scholar's waw is a claim, and claims need grounds.",
           "tr": "Ruhsat doğruluk değil, ALÂKADIR. زَيْدٌ شَاعِرٌ وَعَمْرٌو طَوِيلٌ'un iki yarısı da doğru olabilir; bağlanış yine reddedilir: özneler alâkalı, yüklemler değil — vâv, hiç gerçekleşmeyen bir konu buluşması iddia ederdi. Meânî âliminin vâvı bir iddiadır ve iddia delil ister."}}],
 "relatedNotes": ["al-fasl-wa-al-wasl", "kamal-al-inqita", "shibh-kamal-al-ittisal",
                  "shibh-kamal-al-inqita", "khabar-fi-mana-al-insha", "atf-nasaq"]}

(GR / "tawassut-bayna-al-kamalayn.json").write_text(
    json.dumps(NOTE140, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch36:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + khadaa/akala/asrafa (+shariba copied); note 140")
