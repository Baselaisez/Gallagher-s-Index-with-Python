# -*- coding: utf-8 -*-
"""Author chapter 29 of talkhis-al-miftah — بَابُ النَّهْيِ وَجَوَابُ الطَّلَبِ وَالنِّدَاءُ.

Sahifa 76-77 (lines ~2186-2215): three babs in one chapter, exactly as the
source runs them together.

  • النَّهْي: the request of LEAVING the deed, on isti'la; its one harf is
    the jazming لَا (لَا تَفْعَلْ). Like the amr it can leave its asl —
    tahdid to the disobedient slave: لَا تَمْتَثِلْ أَمْرِي.
  • جَوَابُ الطَّلَبِ: after tamanni, istifham, amr and nahy the books
    permit an IMPLIED shart — لَيْتَ لِي مَالًا أُنْفِقْهُ، أَيْنَ بَيْتُكَ
    أَزُرْكَ، أَكْرِمْنِي أُكْرِمْكَ، لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ — the
    ard (from istifham) joins them: أَلَا تَنْزِلُ تُصِبْ خَيْرًا. Elsewhere
    only with a QARINA: فَاللَّهُ هُوَ الْوَلِيُّ (al-Shura 42:9), the fa
    standing for إِنْ أَرَادُوا أَوْلِيَاءَ.
  • النِّدَاء: a talab kind; its sigha leaves the call for IGHRA
    (يَا مَظْلُومُ) and IKHTISAS (أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ).

ATTRIBUTION: فَاللَّهُ هُوَ الْوَلِيُّ is received Qur'anic text quoted
exactly (al-Shura 42:9); every other sentence is the source's own worked
example verbatim (lines ~2186-2215, sahifa 76-77), Ottoman plain-alif
normalized to standard orthography — a recorded normalization.

Grammar this chapter teaches:
  • note 131 `al-nahy-wa-wujuhuh` — the nahy's definition, its one harf,
    the isti'la shart, the tahdid face, kaff vs tark.
  • note 132 `jawab-al-talab` — the doors of the implied shart and the
    qarina rule; the engine names the jawab on the row.
  • note 133 `ighra-wa-ikhtisas` — the nida sigha beyond the call.
  • engine work: لَا النَّاهِيَة named by the next word's jazm dress; the
    JAWAB AL-TALAB post-pass; the layta deferred-ism repair; the ayyuha
    closed-class row; InshaEngine's ardTalab frame.
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
def copy_verb(pkg, key):
    d = json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))["verbs"]
    return d[key]
S = []

TITLE29 = {"ar": "بَابُ النَّهْيِ وَجَوَابُ الطَّلَبِ وَالنِّدَاءُ",
           "en": "The Nahy, the Answer of the Request, and the Call",
           "tr": "Nehiy Bâbı, Talebin Cevabı ve Nidâ"}

# ------------------------------------------- s1 — the nahy, worn for tahdid
S.append({"id": "s1", "translation": {
 "en": "Disobey my order! (said to the defiant slave — the NAHY worn for THREAT: «and you will see».)",
 "tr": "Emrimi tutma! (isyan eden köleye — TEHDİT için giyilmiş NEHİY: «tutmazsan görürsün».)"},
 "tokens": [
  tok("لَا","la-nahiya","part",["al-nahy-wa-wujuhuh"],
      "لَا النَّاهِيَةُ الْجَازِمَةُ — حَرْفُ النَّهْيِ الْوَحِيدُ.",
      "«do not» — the PROHIBITING la, the nahy's one and only harf, and a jazim: the sukun on the verb after it is its government.",
      "«-ma» — NEHYEDEN lâ; nehyin tek harfi ve bir câzim: ardındaki fiilin sükûnu onun amelidir."),
  tok("تَمْتَثِلْ","imtathala","verb",["al-nahy-wa-wujuhuh"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنْتَ.",
      "«you comply» — a mudari jazmed by the prohibiting la, the sukun its sign; the doer is the concealed «you». The shape is a plain nahy — the RANK makes it a threat: a master who says «disobey me!» promises the consequence.",
      "«uyarsın» — nehyeden lâ ile meczum muzâri; alâmeti sükûn, fâili gizli «sen». Kalıp düz bir nehiydir — onu tehdide çeviren RÜTBEdir: «emrimi tutma!» diyen efendi, âkıbeti vaat ediyor."),
  tok("أَمْرِي","amr","noun",["al-nahy-wa-wujuhuh"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى مَا قَبْلَ يَاءِ الْمُتَكَلِّمِ، وَالْيَاءُ مُضَافٌ إِلَيْهِ.",
      "«my order» — the object, mansub by a fatha ESTIMATED on the letter before the speaker's ya; the ya is the mudaf ilayh.",
      "«emrimi» — mef'ûl; fetha, mütekellim yâsından önceki harf üzerinde TAKDÎRÎdir; yâ, muzâfun ileyhtir.",
      punct="!", segments=[seg("أَمْرِ","amr","noun"), seg("ي","pron-1s","pron")])],
 "jumal": [
  J("لَا تَمْتَثِلْ أَمْرِي",
    "جُمْلَةٌ إِنْشَائِيَّةٌ — نَهْيٌ خَرَجَ إِلَى التَّهْدِيدِ — لَا مَحَلَّ لَهَا.",
    "An insha clause with no mahall: the nahy's letters, the threat's meaning.",
    "Mahalli olmayan inşâ cümlesi: harfleri nehiy, mânâsı tehdit."),
  J("لَا تَمْتَثِلْ أَمْرِي",
    "وَجْهُ التَّهْدِيدِ — نَهْيٌ لَا يُرَادُ بِهِ الْكَفُّ.",
    "THE TAHDID WAJH: a prohibition whose leaving is not wanted at all — the master wants obedience, and dresses the warning as its opposite.",
    "TEHDİT VECHİ: terki hiç istenmeyen bir nehiy — efendi itaat ister ve uyarıyı zıddının kılığına sokar.")]})

# ------------------------------- s2 — the tamanni door of the implied shart
S.append({"id": "s2", "translation": {
 "en": "Would that I had wealth I would spend! (the first door: after the WISH, a bare majzum answers an unwritten «if».)",
 "tr": "Keşke malım olsa da infak etsem! (ilk kapı: TEMENNÎDEN sonra yalın bir meczum, yazılmamış bir «eğer»e cevap verir.)"},
 "tokens": [
  tok("لَيْتَ","layta","part",["jawab-al-talab","insha-wa-tamanni"],
      "حَرْفُ تَمَنٍّ مِنْ أَخَوَاتِ إِنَّ — يَنْصِبُ الِاسْمَ وَيَرْفَعُ الْخَبَرَ.",
      "«would that» — the coined wish particle, of inna's sisters: nasb on its ism, raf' on its khabar.",
      "«keşke» — temennî için konulmuş harf, inne kardeşlerinden: ismini nasb, haberini ref eder."),
  tok("لِي","li","part",["jawab-al-talab"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ خَبَرُ لَيْتَ مُقَدَّمٌ.",
      "«to me» — a jarr phrase hanging on an omitted amil: layta's KHABAR, brought forward.",
      "«bana» — mahzûf bir âmile taalluk eden câr-mecrûr: لَيْتَ'nin ÖNE ALINMIŞ haberi.",
      segments=[seg("لِ","li","part"), seg("ي","pron-1s","pron")]),
  tok("مَالًا","mal","noun",["jawab-al-talab","inna-wa-akhawatuha"],
      "اسْمُ لَيْتَ مُؤَخَّرٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«wealth» — layta's ISM, deferred, mansub by the plain fatha: the jarr phrase before it stood in as the khabar, so the noun that follows is the ism.",
      "«mal» — لَيْتَ'nin ERTELENMİŞ İSMİ; açık fethayla mansub: önündeki câr-mecrûr haber olarak durdu, ardından gelen isim İSİMDİR."),
  tok("أُنْفِقْهُ","anfaqa","verb",["jawab-al-talab"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ التَّمَنِّي بِشَرْطٍ مُقَدَّرٍ (إِنْ يَكُنْ لِي مَالٌ أُنْفِقْهُ)، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْهَاءُ مَفْعُولٌ بِهِ.",
      "«I would spend it» — a mudari MAJZUM in the wish's answer, by an ESTIMATED shart: «if I have wealth, I spend it». No written jazim stands anywhere; the sukun is the hidden shart's receipt. The ha is its object.",
      "«infak ederim onu» — temennînin cevabında, TAKDİR EDİLEN bir şartla MECZUM muzâri: «malım olursa infak ederim». Ortada yazılı hiçbir câzim yok; sükûn, gizli şartın makbuzudur. Hâ, mef'ûlüdür.",
      punct="!", segments=[seg("أُنْفِقْ","anfaqa","verb"), seg("هُ","pron-3ms","pron")])],
 "jumal": [
  J("لَيْتَ لِي مَالًا",
    "جُمْلَةُ التَّمَنِّي — إِنْشَاءٌ لَا مَحَلَّ لَهُ، وَالْخَبَرُ مُقَدَّمٌ.",
    "The wish clause: insha with no mahall — and its khabar walks in front of its ism.",
    "Temennî cümlesi: mahalsiz inşâ — haberi, isminin önünde yürüyor."),
  J("أُنْفِقْهُ",
    "جَوَابُ الطَّلَبِ — مَجْزُومٌ بِشَرْطٍ مُقَدَّرٍ.",
    "THE ANSWER OF THE REQUEST: the books estimate «if…» and the jazm on the page is that hidden clause's receipt — the first of the four doors.",
    "TALEBİN CEVABI: kitaplar «eğer…» takdir eder; sayfadaki cezm o gizli cümlenin makbuzudur — dört kapının ilki.")]})

# ------------------------------ s3 — the istifham door
S.append({"id": "s3", "translation": {
 "en": "Where is your house, that I may visit you? (the second door: after the QUESTION.)",
 "tr": "Evin nerede, ziyaret edeyim seni? (ikinci kapı: SORUDAN sonra.)"},
 "tokens": [
  tok("أَيْنَ","ayna","noun",["jawab-al-talab","adawat-al-tasawwur"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ.",
      "«where» — an interrogative NOUN, mabni on the fatha, in the position of raf': the khabar, fronted (question words own the sentence head).",
      "«nerede» — soru İSMİ; fetha üzere mebnî, mahallen merfû: öne alınmış haber (soru kelimeleri cümle başını mülk edinir)."),
  tok("بَيْتُكَ","bayt","noun",["jawab-al-talab"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«your house» — the mubtada, deferred, marfu' by the damma; the kaf is the mudaf ilayh.",
      "«evin» — ertelenmiş mübtedâ; dammeyle merfû; kâf, muzâfun ileyhtir.",
      segments=[seg("بَيْتُ","bayt","noun"), seg("كَ","pron-2ms","pron")]),
  tok("أَزُرْكَ","zara","verb",["jawab-al-talab"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الِاسْتِفْهَامِ بِشَرْطٍ مُقَدَّرٍ (إِنْ تُعَرِّفْنِيهِ أَزُرْكَ)، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْكَافُ مَفْعُولٌ بِهِ.",
      "«I would visit you» — majzum in the question's answer, by the estimated «if you tell me where, I visit you»; the sukun is the sign, the kaf the object. (زَارَ is hollow: the waw already fell to the jazm's sukun — أَزُورُ → أَزُرْ.)",
      "«ziyaret edeyim seni» — sorunun cevabında meczum; takdir: «tarif edersen ziyaret ederim». Alâmeti sükûn, kâf mef'ûl. (زَارَ ecveftir: vâv, cezmin sükûnuna zaten düştü — أَزُورُ → أَزُرْ.)",
      punct="؟", segments=[seg("أَزُرْ","zara","verb"), seg("كَ","pron-2ms","pron")])],
 "jumal": [
  J("أَيْنَ بَيْتُكَ",
    "جُمْلَةٌ اسْمِيَّةٌ اسْتِفْهَامِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The question clause — nominal, no mahall: khabar fronted, mubtada deferred.",
    "Soru cümlesi — isim cümlesi, mahalsiz: haber önde, mübtedâ ertelenmiş."),
  J("أَزُرْكَ",
    "جَوَابُ الطَّلَبِ الثَّانِي — الِاسْتِفْهَامُ بَابٌ لِلشَّرْطِ الْمُقَدَّرِ.",
    "The second door: a real question carries a hidden bargain — «tell me, and I will come» — and the jazm records it.",
    "İkinci kapı: gerçek bir soru gizli bir pazarlık taşır — «söyle, geleyim» — ve cezm bunu kaydeder.")]})

# ------------------------------ s4 — the amr door
S.append({"id": "s4", "translation": {
 "en": "Honour me, and I will honour you. (the third door: after the AMR.)",
 "tr": "Bana ikram et, sana ikram edeyim. (üçüncü kapı: EMİRDEN sonra.)"},
 "tokens": [
  tok("أَكْرِمْنِي","akrama","verb",["jawab-al-talab","imperative-amr"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ.",
      "«honour me» — the amr, mabni on the sukun; the nun is the GUARDING nun and the ya the speaker-object; the doer is the concealed «you».",
      "«bana ikram et» — emir; sükûn üzere mebnî. Nûn, VİKAYE nûnu; yâ, mütekellim mef'ûlü; fâil gizli «sen»dir.",
      segments=[seg("أَكْرِمْ","akrama","verb"), seg("نِي","pron-1s","pron")]),
  tok("أُكْرِمْكَ","akrama","verb",["jawab-al-talab"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الْأَمْرِ بِشَرْطٍ مُقَدَّرٍ (إِنْ تُكْرِمْنِي أُكْرِمْكَ)، وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْكَافُ مَفْعُولٌ بِهِ.",
      "«I will honour you» — majzum in the amr's answer: «if you honour me, I honour you». The two verbs are one root wearing the bargain's two halves; the sukun is the estimated shart's receipt.",
      "«sana ikram edeyim» — emrin cevabında meczum: «bana ikram edersen sana ikram ederim». İki fiil, pazarlığın iki yarısını giymiş tek köktür; sükûn, takdîr edilen şartın makbuzudur.",
      punct=".", segments=[seg("أُكْرِمْ","akrama","verb"), seg("كَ","pron-2ms","pron")])],
 "jumal": [
  J("أَكْرِمْنِي",
    "جُمْلَةُ الطَّلَبِ — أَمْرٌ لَا مَحَلَّ لَهُ.",
    "The request half: an amr clause, no mahall.",
    "Talep yarısı: emir cümlesi, mahalsiz."),
  J("أُكْرِمْكَ",
    "جَوَابُ الطَّلَبِ الثَّالِثُ — فِي تَقْدِيرِ شَرْطٍ وَجَوَابِهِ.",
    "The third door: the amr and its answer construe as a full conditional — request above, reward below, one implied «if» between them.",
    "Üçüncü kapı: emir ve cevabı tam bir şart cümlesi gibi kurulur — üstte talep, altta karşılık, arada takdîrî bir «eğer».")]})

# ------------------------------ s5 — the nahy door
S.append({"id": "s5", "translation": {
 "en": "Do not revile, and it will be better for you. (the fourth door: after the NAHY.)",
 "tr": "Sövme, senin için hayırlı olur. (dördüncü kapı: NEHİYDEN sonra.)"},
 "tokens": [
  tok("لَا","la-nahiya","part",["jawab-al-talab","al-nahy-wa-wujuhuh"],
      "لَا النَّاهِيَةُ الْجَازِمَةُ.",
      "«do not» — the prohibiting, jazming la.",
      "«-ma» — nehyeden, cezmeden lâ."),
  tok("تَشْتِمْ","shatama","verb",["jawab-al-talab","al-nahy-wa-wujuhuh"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِلَا النَّاهِيَةِ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ.",
      "«you revile» — jazmed by the prohibiting la, its doer the concealed «you»: a true nahy this time, wanting the leaving itself.",
      "«söversin» — nehyeden lâ ile meczum; fâili gizli «sen»: bu kez terkin kendisi istenen gerçek bir nehiy."),
  tok("يَكُنْ","kana","verb",["jawab-al-talab","kana-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ فِي جَوَابِ النَّهْيِ بِشَرْطٍ مُقَدَّرٍ (إِنْ لَا تَشْتِمْ يَكُنْ)، وَاسْمُهَا ضَمِيرٌ مُسْتَتِرٌ يَعُودُ عَلَى التَّرْكِ.",
      "«it will be» — the defective kana, MAJZUM in the nahy's answer: «if you do not revile, it will be». Its ism is concealed, returning to the LEAVING itself; the hollow waw already fell to the sukun (يَكُونُ → يَكُنْ).",
      "«olur» — nâkıs kâne; nehyin cevabında MECZUM: «sövmezsen olur». İsmi gizlidir, TERKİN kendisine döner; ecvef vâvı sükûna zaten düştü (يَكُونُ → يَكُنْ).",
      segments=None),
  tok("خَيْرًا","khayr","noun",["jawab-al-talab","kana-wa-akhawatuha"],
      "خَبَرُ يَكُنْ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«better» — yakun's khabar, mansub by the plain fatha.",
      "«hayırlı» — يَكُنْ'un haberi; açık fethayla mansub."),
  tok("لَكَ","li","part",["jawab-al-talab"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِخَيْرًا.",
      "«for you» — the jarr phrase, hanging on «better».",
      "«senin için» — câr-mecrûr; «hayırlı»ya taalluk eder.",
      punct=".", segments=[seg("لَ","li","part"), seg("كَ","pron-2ms","pron")])],
 "jumal": [
  J("لَا تَشْتِمْ",
    "جُمْلَةُ النَّهْيِ — إِنْشَاءٌ لَا مَحَلَّ لَهُ.",
    "The nahy clause: insha, no mahall — and this one means its own leaving.",
    "Nehiy cümlesi: inşâ, mahalsiz — ve bu kez terkin kendisi kastediliyor."),
  J("يَكُنْ خَيْرًا لَكَ",
    "جَوَابُ الطَّلَبِ الرَّابِعُ — النَّهْيُ بَابٌ لِلشَّرْطِ الْمُقَدَّرِ أَيْضًا.",
    "The fourth door: even a prohibition opens the hidden «if» — «if you leave it, it will be better».",
    "Dördüncü kapı: bir nehiy bile gizli «eğer»i açar — «terk edersen hayırlı olur».")]})

# ------------------------------ s6 — the 'ard, from the istifham
S.append({"id": "s6", "translation": {
 "en": "Won't you dismount? You would meet with good. (the ARD — asking with gentleness, born of the question.)",
 "tr": "İnmez misin? Hayra erersin. (ARZ — tatlılıkla istemek; sorudan doğmuştur.)"},
 "tokens": [
  tok("أَلَا","ala-ard","part",["jawab-al-talab","khuruj-al-istifham"],
      "أَلَا لِلْعَرْضِ — الْهَمْزَةُ وَ«لَا» صَارَتَا أَدَاةَ طَلَبٍ بِلِينٍ.",
      "«won't you» — ALA of the OFFER: the hamza over la, become one tool of gentle asking. The receipt that this is no plain negation-question stands two words on: the bare majzum.",
      "«-mez misin» — ARZ edatı أَلَا: hemze ile lâ, tatlı isteyişin tek edatı olmuş. Bunun düz bir nefiy sorusu olmadığının makbuzu iki kelime ötededir: yalın meczum."),
  tok("تَنْزِلُ","nazala","verb",["jawab-al-talab"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ.",
      "«you dismount» — marfu' by the plain damma (the ala governs nothing); its doer the concealed «you».",
      "«inersin» — açık dammeyle merfû (أَلَا amel etmez); fâili gizli «sen»."),
  tok("تُصِبْ","asaba","verb",["jawab-al-talab"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ فِي جَوَابِ الْعَرْضِ بِشَرْطٍ مُقَدَّرٍ (إِنْ تَنْزِلْ تُصِبْ)، وَعَلَامَةُ جَزْمِهِ السُّكُونُ.",
      "«you would meet» — majzum in the offer's answer: «if you dismount, you meet with good»; the hollow ya already fell to the sukun (تُصِيبُ → تُصِبْ).",
      "«erersin» — arzın cevabında meczum: «inersen hayra erersin»; ecvef yâsı sükûna zaten düştü (تُصِيبُ → تُصِبْ)."),
  tok("خَيْرًا","khayr","noun",["jawab-al-talab"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«good» — the object, mansub by the plain fatha.",
      "«hayra» — mef'ûl; açık fethayla mansub.",
      punct=".")],
 "jumal": [
  J("أَلَا تَنْزِلُ",
    "جُمْلَةُ الْعَرْضِ — اسْتِفْهَامٌ خَرَجَ إِلَى الطَّلَبِ بِلِينٍ.",
    "The offer clause: a question's letters, a gentle request's meaning — the ard is the istifham's own child.",
    "Arz cümlesi: harfleri soru, mânâsı tatlı istek — arz, istifhâmın öz çocuğudur."),
  J("تُصِبْ خَيْرًا",
    "جَوَابُ الطَّلَبِ — وَالْجَزْمُ هُوَ الْقَرِينَةُ عَلَى الْعَرْضِ.",
    "The answer again — and this time the jazm is also the PROOF: only a request, never a plain negation, earns an answer in jazm.",
    "Yine cevap — ve bu kez cezm aynı zamanda İSPATTIR: cezimli cevabı yalnız talep kazanır, düz nefiy asla.")]})

# ------------------------------ s7 — the qarina-only case (al-Shura 42:9)
S.append({"id": "s7", "translation": {
 "en": "So Allah — He is the true Friend. (al-Shura 42:9: outside the doors, the shart is estimated only with a QARINA — here the fa.)",
 "tr": "İşte Allah — asıl Dost O'dur. (Şûrâ 42:9: kapıların dışında şart ancak KARÎNE ile takdir edilir — burada fâ.)"},
 "tokens": [
  tok("فَاللَّهُ","allah","propn",["jawab-al-talab"],
      "الْفَاءُ قَرِينَةُ الشَّرْطِ الْمُقَدَّرِ (إِنْ أَرَادُوا أَوْلِيَاءَ)، وَلَفْظُ الْجَلَالَةِ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«so Allah» — the FA is the qarina of the estimated shart: «if they want protectors, then Allah…». The Name is the mubtada, marfu'.",
      "«işte Allah» — FÂ, takdîr edilen şartın karînesidir: «dost isterlerse, işte Allah…». Lafza-i celâl mübtedâdır, merfû.",
      segments=[seg("فَ","fa","part"), seg("اللَّهُ","allah","propn")]),
  tok("هُوَ","huwa","pron",["jawab-al-talab","damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ مِنَ الْإِعْرَابِ.",
      "«He» — the pronoun of SEPARATION, no mahall: it walls the khabar off from being read as a sifa, and restricts — the Friend is He, none else.",
      "«O» — FASIL zamiri, mahalli yok: haberi sıfat okunmaktan ayırır ve kasreder — Dost yalnız O'dur."),
  tok("الْوَلِيُّ","wali","noun",["jawab-al-talab"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«the Friend» — the khabar, marfu' by the plain damma.",
      "«Dost» — haber; açık dammeyle merfû.",
      punct=".")],
 "jumal": [
  J("فَاللَّهُ هُوَ الْوَلِيُّ",
    "جُمْلَةٌ اسْمِيَّةٌ — جَوَابُ شَرْطٍ مُقَدَّرٍ دَلَّتْ عَلَيْهِ الْفَاءُ.",
    "A nominal clause standing as the answer of an estimated shart — and the FA on its brow is the evidence the books demand.",
    "Takdîr edilen bir şartın cevabı olarak duran isim cümlesi — alnındaki FÂ, kitapların istediği delildir."),
  J("هُوَ الْوَلِيُّ",
    "ضَمِيرُ الْفَصْلِ — تَوْكِيدٌ وَقَصْرٌ.",
    "The separating pronoun: emphasis and restriction in one word — outside the four doors, only such a qarina licenses the hidden shart.",
    "Fasıl zamiri: tek kelimede tekit ve kasr — dört kapının dışında gizli şarta ancak böyle bir karîne izin verir.")]})

# ------------------------------ s8 — the nida for IGHRA
S.append({"id": "s8", "translation": {
 "en": "O wronged one! (the call's sigha worn for IGHRA — urging the hearer to his own cause.)",
 "tr": "Ey mazlum! (nidâ sîgası İĞRÂ için giyilmiş — muhatabı kendi davasına teşvik.)"},
 "tokens": [
  tok("يَا","ya","part",["ighra-wa-ikhtisas","vocative-munada"],
      "حَرْفُ نِدَاءٍ.",
      "«O» — the calling particle.",
      "«ey» — nidâ harfi."),
  tok("مَظْلُومُ","mazlum","noun",["ighra-wa-ikhtisas","vocative-munada"],
      "مُنَادَى نَكِرَةٌ مَقْصُودَةٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.",
      "«wronged one» — the munada, an intended indefinite, mabni on the damm in the position of nasb. The call is real in letter, IGHRA in aim: it spurs the wronged man to speak up for his own right.",
      "«mazlum» — münâdâ; nekre-i maksûde, zamme üzere mebnî, mahallen mansub. Nidâ lafızda gerçek, maksatta İĞRÂdır: mazlumu kendi hakkını aramaya teşvik eder.",
      punct="!")],
 "jumal": [
  J("يَا مَظْلُومُ",
    "جُمْلَةُ نِدَاءٍ — إِنْشَاءٌ لَا مَحَلَّ لَهُ.",
    "A call clause: insha, no mahall.",
    "Nidâ cümlesi: inşâ, mahalsiz."),
  J("يَا مَظْلُومُ",
    "وَجْهُ الْإِغْرَاءِ — نِدَاءٌ يُرَادُ بِهِ التَّشْوِيقُ.",
    "THE IGHRA WAJH: the caller does not summon — he stirs: «you are wronged; act!»",
    "İĞRÂ VECHİ: çağıran davet etmiyor — kışkırtıyor: «mazlumsun; davran!»")]})

# ------------------------------ s9 — the nida sigha for IKHTISAS
S.append({"id": "s9", "translation": {
 "en": "I — of all men — do such-and-such. (the IKHTISAS: the call's shape with no call in it.)",
 "tr": "Ben — erler içinde — şunu şunu yaparım. (İHTİSAS: içinde nidâ olmayan nidâ kalıbı.)"},
 "tokens": [
  tok("أَنَا","ana","pron",["ighra-wa-ikhtisas"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«I» — the detached pronoun, mabni, in the position of raf': the mubtada.",
      "«ben» — munfasıl zamir; mebnî, mahallen merfû: mübtedâ."),
  tok("أَفْعَلُ","faala","verb",["ighra-wa-ikhtisas"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ، وَالْجُمْلَةُ خَبَرٌ.",
      "«I do» — a marfu' mudari, its doer concealed; the clause is the khabar.",
      "«yaparım» — merfû muzâri; fâili gizli; cümle haberdir."),
  tok("كَذَا","kadha","pron",["ighra-wa-ikhtisas"],
      "كِنَايَةٌ عَنِ الْمَفْعُولِ — مَبْنِيٌّ فِي مَحَلِّ نَصْبٍ.",
      "«such-and-such» — a kinaya standing in for the object, mabni, in the position of nasb.",
      "«şunu şunu» — mef'ûlün yerini tutan kinâye; mebnî, mahallen mansub."),
  tok("أَيُّهَا","ayyuha","noun",["ighra-wa-ikhtisas"],
      "«أَيُّ» مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ عَلَى الِاخْتِصَاصِ بِفِعْلٍ مُقَدَّرٍ (أَخُصُّ)، وَ«هَا» لِلتَّنْبِيهِ.",
      "«of all» — AYY, mabni on the damm, in the position of NASB on the ikhtisas: an estimated «I single out» governs it. The ha only alerts. No one is being called.",
      "«içinde» — EYY; zamme üzere mebnî, İHTİSAS üzere mahallen mansub: takdîrî bir «tahsis ederim» onu amel eder. Hâ yalnız tenbihtir. Kimse çağrılmıyor.",
      segments=[seg("أَيُّ","ayyuha","noun"), seg("هَا","ha-tanbih","part")]),
  tok("الرَّجُلُ","rajul","noun",["ighra-wa-ikhtisas"],
      "صِفَةٌ لِأَيٍّ مَرْفُوعَةٌ لَفْظًا تَبَعًا لِلَفْظِ الضَّمِّ.",
      "«men» — the sifa of ayy, marfu' in LETTER, following the damm the bina wears — the classical i'rab of the ikhtisas frame.",
      "«erler» — أَيّ'in sıfatı; LAFZAN merfû, mebnînin taşıdığı zammeye tâbi — ihtisas kalıbının klasik i'râbı.",
      punct=".")],
 "jumal": [
  J("أَنَا أَفْعَلُ كَذَا",
    "جُمْلَةٌ اسْمِيَّةٌ خَبَرِيَّةٌ.",
    "The frame sentence: a plain nominal report.",
    "Çerçeve cümle: düz bir isim cümlesi."),
  J("أَيُّهَا الرَّجُلُ",
    "وَجْهُ الِاخْتِصَاصِ — صِيغَةُ النِّدَاءِ بِلَا نِدَاءٍ.",
    "THE IKHTISAS WAJH: the call's dress with no calling in it — «I, and among men precisely I, do this». The speaker singles himself out.",
    "İHTİSAS VECHİ: içinde çağrı olmayan nidâ kılığı — «ben, erler içinde tam da ben, bunu yaparım». Konuşan kendini tahsis ediyor.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "la-nahiya": copy_gloss("wasiyyat-abi-yusuf-l5", "la-nahiya"),
 "imtathala": g("اِمْتَثَلَ", "م ث ل", "verb", "to comply, obey (an order)", "uymak, (emri) tutmak", 5, form="VIII"),
 "anfaqa": g("أَنْفَقَ", "ن ف ق", "verb", "to spend (wealth)", "infak etmek, harcamak", 3, form="IV"),
 "nazala": g("نَزَلَ", "ن ز ل", "verb", "to descend, dismount", "inmek", 2, form="I"),
 "khayr": copy_gloss("wasiyyat-abi-hanifa", "khayr"),
 "shatama": copy_gloss("wasiyyat-abi-hanifa-samti", "shatama"),
 "akrama": copy_gloss("wasiyyat-abi-hanifa-samti", "akrama"),
 "kana": copy_gloss("kitab-al-sulh", "kana"),
 "faala": copy_gloss("mukhtasar-al-manar", "faala"),
 "mal": copy_gloss("kitab-al-sulh", "mal"),
 "wali": copy_gloss("aqaid-ahl-al-sunna", "wali"),
 "mazlum": copy_gloss("aqaid-ahl-al-sunna", "mazlum"),
 "kadha": copy_gloss("wasiyyat-abi-hanifa-samti", "kadha"),
 "rajul": copy_gloss("wasiyyat-abi-hanifa-samti", "rajul"),
 "ayyuha": copy_gloss("jumal-al-tadrib", "ayyuha"),
 "ala-ard": g("أَلَا (لِلْعَرْضِ)", None, "part", "won't you…? (the gentle offer, born of the question)",
              "-mez misin? (sorudan doğan tatlı isteyiş: arz)", 5),
 "ha-tanbih": g("هَا (التَّنْبِيه)", None, "part", "the alerting ha (as in أَيُّهَا)",
                "tenbih hâsı (أَيُّهَا'daki gibi)", 4),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/29.json").write_text(
    json.dumps({"chapter": 29, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 29 for c in man["chapters"]):
    man["chapters"].append({"n": 29, "title": TITLE29})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.29.0"
ADD_EN = (" Chapter 29 carries the nahy, the jawab al-talab and the nida's departures (lines "
          "~2186-2215, sahifa 76-77): فَاللَّهُ هُوَ الْوَلِيُّ is received Qur'anic text quoted "
          "exactly — al-Shura 42:9; every other sentence is the source's own worked example "
          "verbatim, Ottoman plain-alif normalized to standard orthography — a recorded "
          "normalization. One divergence: the source vowels لَا تَشْتُمْ on bab nasara; the "
          "corpus's received paradigm recites شَتَمَ يَشْتِمُ on bab daraba (both are attested), "
          "and the chapter follows the corpus — recorded here.")
ADD_TR = (" Yirmi dokuzuncu bâb nehyi, cevâbü't-talebi ve nidânın çıkışlarını taşır (satır "
          "~2186-2215, sahife 76-77): فَاللَّهُ هُوَ الْوَلِيُّ aynen alınmış mervî Kur'ân "
          "metnidir — Şûrâ 42:9; diğer bütün cümleler kaynağın kendi işlenmiş örneklerinin aynen "
          "alınmışıdır; Osmanlı düz-elif imlâsı standart imlâya çevrilmiştir — kayıtlı bir "
          "normalizasyondur. Bir ayrılık: kaynak لَا تَشْتُمْ'u nasara bâbıyla harekeler; "
          "külliyatın mervî çekimi شَتَمَ يَشْتِمُ ile daraba bâbını okur (ikisi de menkuldür) "
          "ve bâb, külliyata tâbi kılındı — burada kayıtlıdır.")
if "2186-2215" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "imtathala" not in mo["verbs"]:
    mo["verbs"]["imtathala"] = _sg.derived(
        _sg.B8, _sg.W8, "َ", "اِمْتَثَل", "مْتَثِل", "اِمْتَثِل",
        "اِمْتِثَال", "مُمْتَثِل", "مُمْتَثَل", "اُمْتُثِلَ", "يُمْتَثَلُ")
if "anfaqa" not in mo["verbs"]:
    mo["verbs"]["anfaqa"] = _sg.derived(
        _sg.B4, _sg.W4, "ُ", "أَنْفَق", "نْفِق", "أَنْفِق",
        "إِنْفَاق", "مُنْفِق", "مُنْفَق", "أُنْفِقَ", "يُنْفَقُ")
if "nazala" not in mo["verbs"]:
    mo["verbs"]["nazala"] = _sg.sound1(
        "daraba", "نَزَل", "نْزِل", "اِنْزِل", "نُزُول", "نَازِل",
        None, "نُزِلَ", "يُنْزَلُ")
for key, pkg in [("shatama", "wasiyyat-abi-hanifa-samti"), ("akrama", "wasiyyat-abi-hanifa-samti"),
                 ("kana", "kitab-al-sulh"), ("faala", "mukhtasar-al-manar")]:
    if key not in mo["verbs"]:
        mo["verbs"][key] = copy_verb(pkg, key)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
GR = ROOT / "content/grammar"
NOTE131 = {
 "id": "al-nahy-wa-wujuhuh",
 "title": {"ar": "النَّهْيُ وَوُجُوهُهُ", "en": "The nahy and its departures", "tr": "Nehiy ve vecihleri"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح (الخطيب القزويني) — باب الإنشاء: النهي"],
 "question": {
  "en": ["Is the LEAVING of the deed demanded from above? Then the sigha keeps its name: nahy.",
         "Does the speaker actually want the deed done — «disobey me!» to the defiant? TAHDID."],
  "tr": ["Fiilin TERKİ yukarıdan mı isteniyor? O hâlde sîga adını korur: nehiy.",
         "Konuşan fiilin yapılmasını mı istiyor aslında — âsiye «emrimi tutma!» gibi? TEHDİT."]},
 "plain": {
  "en": "The nahy is the amr's mirror: demanding that a deed be LEFT, from above. It owns exactly one harf — the jazming لا — and like the amr it can leave its post: said to the defiant, «disobey my order!» threatens rather than forbids.",
  "tr": "Nehiy, emrin aynasıdır: fiilin TERKİNİN yukarıdan istenmesidir. Tek harfi vardır — cezmeden lâ — ve emir gibi o da yerinden çıkabilir: âsiye söylenen «emrimi tutma!» yasaklamaz, tehdit eder."},
 "explanation": {
  "en": "النَّهْيُ: طَلَبُ التَّرْكِ عَلَى وَجْهِ الِاسْتِعْلَاءِ — the request of leaving the deed, from above; isti'la conditions it exactly as it conditions the amr. Its one harf is the PROHIBITING لا, a jazim: لَا تَفْعَلْ. The books split what is asked into KAFF — that the addressee not begin — and TARK — that he abandon what he began. And like the amr the sigha can leave its post: to the slave who defies his master, لَا تَمْتَثِلْ أَمْرِي («disobey my order!») is a THREAT — the leaving is not wanted at all; the consequence is promised through its opposite.",
  "tr": "النَّهْيُ: fiilin terkinin isti'lâ yoluyla istenmesidir — isti'lâ onu, emri şart koştuğu gibi şart koşar. Tek harfi, NEHYEDEN lâ'dır ve câzimdir: لَا تَفْعَلْ. Kitaplar isteneni ikiye ayırır: KEFF — muhatabın hiç başlamaması — ve TERK — başladığını bırakması. Ve emir gibi bu sîga da yerinden çıkar: efendisine isyan eden köleye لَا تَمْتَثِلْ أَمْرِي («emrimi tutma!») bir TEHDİTTİR — terk hiç istenmiyor; âkıbet, zıddı üzerinden vaat ediliyor."},
 "examples": [
  {"ar": "لَا تَمْتَثِلْ أَمْرِي",
   "en": "«Disobey my order!» — the nahy worn for threat.",
   "tr": "«Emrimi tutma!» — tehdit için giyilmiş nehiy.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ",
   "en": "«Do not revile, and it will be better for you» — a true nahy, with the answer of the request after it.",
   "tr": "«Sövme, senin için hayırlı olur» — gerçek bir nehiy; ardında talebin cevabı.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«لَا تَعْلَمُ ile لَا تَعْلَمْ aynıdır»",
   "right": "«Damma nefiydir (bilmiyorsun), sükûn nehiydir (bilme!)»",
   "why": {"en": "One la, two faces, one letter of difference: the negating la governs nothing and the mudari keeps its damma; the prohibiting la is a JAZIM and the sukun is its government. Read the verb's ending before naming the la.",
           "tr": "Tek lâ, iki yüz, tek harf fark: nefiy lâ'sı amel etmez, muzâri dammesini korur; nehiy lâ'sı CÂZİMDİR ve sükûn onun amelidir. Lâ'yı adlandırmadan önce fiilin sonunu oku."}}],
 "relatedNotes": ["al-amr-wa-wujuhuh", "jawab-al-talab", "khuruj-al-istifham"]}

NOTE132 = {
 "id": "jawab-al-talab",
 "title": {"ar": "جَوَابُ الطَّلَبِ", "en": "The answer of the request", "tr": "Talebin cevabı (cevâbü't-taleb)"},
 "level": 6, "group": "nahw", "mamul": "majzum",
 "classicalSources": ["تلخيص المفتاح — تقدير الشرط بعد التمني والاستفهام والأمر والنهي",
                      "شروح التلخيص — قرينة الفاء في جواب الشرط المقدر"],
 "question": {
  "en": ["Is a mudari MAJZUM with no written jazim anywhere before it?",
         "Does a request stand earlier — a wish, a question, an amr, a nahy, an offer?"],
  "tr": ["Önünde hiçbir yazılı câzim yokken muzâri MECZUM mu?",
         "Daha önce bir talep mi duruyor — temennî, soru, emir, nehiy, arz?"]},
 "plain": {
  "en": "After a request — a wish, a question, a command, a prohibition, a gentle offer — a bare majzum verb answers an UNWRITTEN «if»: أَكْرِمْنِي أُكْرِمْكَ construes as «if you honour me, I honour you». Elsewhere the hidden shart needs a visible clue, like the fa of فَاللَّهُ هُوَ الْوَلِيُّ.",
  "tr": "Bir talepten sonra — temennî, soru, emir, nehiy, arz — yalın bir meczum fiil, YAZILMAMIŞ bir «eğer»e cevap verir: أَكْرِمْنِي أُكْرِمْكَ, «bana ikram edersen sana ikram ederim» diye kurulur. Başka yerde gizli şart görünür bir ipucu ister; فَاللَّهُ هُوَ الْوَلِيُّ'deki fâ gibi."},
 "explanation": {
  "en": "The books permit estimating a shart after exactly these doors: TAMANNI (لَيْتَ لِي مَالًا أُنْفِقْهُ — «if I have wealth, I spend it»), ISTIFHAM (أَيْنَ بَيْتُكَ أَزُرْكَ), AMR (أَكْرِمْنِي أُكْرِمْكَ), NAHY (لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ) — and the ARD, the gentle offer born of the question (أَلَا تَنْزِلُ تُصِبْ خَيْرًا). The jazm on the answering verb is the hidden shart's only trace on the page: no written jazim governs it. OUTSIDE these doors the estimation is licit only where a QARINA stands — in فَاللَّهُ هُوَ الْوَلِيُّ (al-Shura 42:9) the fa points back to an estimated إِنْ أَرَادُوا أَوْلِيَاءَ.",
  "tr": "Kitaplar şart takdirine tam şu kapılardan izin verir: TEMENNÎ (لَيْتَ لِي مَالًا أُنْفِقْهُ — «malım olursa infak ederim»), İSTİFHAM (أَيْنَ بَيْتُكَ أَزُرْكَ), EMİR (أَكْرِمْنِي أُكْرِمْكَ), NEHİY (لَا تَشْتِمْ يَكُنْ خَيْرًا لَكَ) — ve sorudan doğan tatlı isteyiş ARZ (أَلَا تَنْزِلُ تُصِبْ خَيْرًا). Cevap fiilinin cezmi, gizli şartın sayfadaki tek izidir: onu yazılı hiçbir câzim amel etmez. Bu kapıların DIŞINDA takdir ancak KARÎNE ile câizdir — فَاللَّهُ هُوَ الْوَلِيُّ'de (Şûrâ 42:9) fâ, takdîr edilen إِنْ أَرَادُوا أَوْلِيَاءَ'ya işaret eder."},
 "examples": [
  {"ar": "أَكْرِمْنِي أُكْرِمْكَ",
   "en": "«Honour me, and I will honour you» — the amr door: one implied «if» between two verbs of one root.",
   "tr": "«Bana ikram et, sana ikram edeyim» — emir kapısı: tek kökün iki fiili arasında takdîrî bir «eğer».",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "لَيْتَ لِي مَالًا أُنْفِقْهُ",
   "en": "«Would that I had wealth I would spend» — the tamanni door.",
   "tr": "«Keşke malım olsa da infak etsem» — temennî kapısı.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "فَاللَّهُ هُوَ الْوَلِيُّ",
   "en": "«So Allah is the true Friend» (42:9) — outside the doors, the fa is the required qarina.",
   "tr": "«İşte asıl Dost Allah'tır» (42:9) — kapıların dışında fâ, gereken karînedir.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«أُكْرِمْكَ'nin cezmi emirden gelir»",
   "right": "«Cezm, takdîr edilen şarttan gelir — emir yalnız kapıyı açar»",
   "why": {"en": "An amr governs nothing after itself; the jazim of the answering verb is the ESTIMATED إِنْ. Naming the amr as the governor invents a jazim the books never list.",
           "tr": "Emir kendinden sonrasını amel etmez; cevap fiilinin câzimi TAKDÎR EDİLEN إِنْ'dir. Emri âmil saymak, kitapların hiç saymadığı bir câzim uydurmaktır."}}],
 "relatedNotes": ["al-amr-wa-wujuhuh", "al-nahy-wa-wujuhuh", "insha-wa-tamanni", "jazm-al-mudari"]}

NOTE133 = {
 "id": "ighra-wa-ikhtisas",
 "title": {"ar": "الْإِغْرَاءُ وَالِاخْتِصَاصُ", "en": "Ighra and ikhtisas: the call beyond calling", "tr": "İğrâ ve ihtisas: çağrının ötesinde nidâ"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — النداء وخروجه عن أصله"],
 "question": {
  "en": ["Is anyone actually being summoned? If yes, the call keeps its name: nida.",
         "Does the «call» spur the hearer to his own cause — يَا مَظْلُومُ? IGHRA.",
         "Does the sigha stand mid-sentence with no calling at all — أَيُّهَا الرَّجُلُ? IKHTISAS."],
  "tr": ["Gerçekten biri mi çağrılıyor? Evetse çağrı adını korur: nidâ.",
         "«Çağrı» muhatabı kendi davasına mı kışkırtıyor — يَا مَظْلُومُ? İĞRÂ.",
         "Sîga, cümle ortasında hiç çağrısız mı duruyor — أَيُّهَا الرَّجُلُ? İHTİSAS."]},
 "plain": {
  "en": "The call's sigha can serve without calling. يَا مَظْلُومُ summons no one — it spurs the wronged man to act (IGHRA). And in أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ nobody is addressed at all: the speaker singles HIMSELF out among men (IKHTISAS), and أَيّ stands mabni on the damm in the position of nasb.",
  "tr": "Nidâ sîgası çağırmadan da iş görür. يَا مَظْلُومُ kimseyi davet etmez — mazlumu davranmaya kışkırtır (İĞRÂ). أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ'de ise hiç kimseye seslenilmez: konuşan, erler içinde KENDİNİ tahsis eder (İHTİSAS); أَيّ zamme üzere mebnî, mahallen mansubdur."},
 "explanation": {
  "en": "النِّدَاءُ is itself a talab kind: the demand that the addressed one TURN, by a harf standing (in letter or estimation) for أَدْعُو. Its sigha leaves that post two ways. IGHRA: the call's letters aimed at incitement — يَا مَظْلُومُ said to one complaining of wrong urges him to his own defence. IKHTISAS: the call's dress with no call in it — أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ, «I, precisely among men, do this»; the classical i'rab reads أَيّ as mabni on the damm in the POSITION OF NASB, governed by an estimated أَخُصُّ («I single out»), with the ال-noun after it following the damm in letter.",
  "tr": "NİDÂ da bir talep türüdür: çağrılanın, (lafzen veya takdiren) أَدْعُو yerinde duran bir harfle YÖNELMESİNİN istenmesidir. Sîgası bu görevden iki yolla çıkar. İĞRÂ: teşvike yönelmiş çağrı harfleri — zulümden yakınana söylenen يَا مَظْلُومُ, onu kendi savunmasına iter. İHTİSAS: içinde çağrı olmayan nidâ kılığı — أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ, «erler içinde tam da ben bunu yaparım»; klasik i'râb أَيّ'i zamme üzere mebnî, MAHALLEN MANSUB okur — takdîrî bir أَخُصُّ («tahsis ederim») onu amel eder; ardındaki ال'lı isim lafzen zamme'ye tâbidir."},
 "examples": [
  {"ar": "يَا مَظْلُومُ",
   "en": "«O wronged one!» — ighra: the call that incites.",
   "tr": "«Ey mazlum!» — iğrâ: kışkırtan çağrı.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s8"},
  {"ar": "أَنَا أَفْعَلُ كَذَا أَيُّهَا الرَّجُلُ",
   "en": "«I — of all men — do such-and-such» — ikhtisas: the call's shape, the self singled out.",
   "tr": "«Ben — erler içinde — şunu şunu yaparım» — ihtisas: nidâ kalıbı, tahsis edilen benlik.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s9"}],
 "commonMistakes": [
  {"wrong": "«أَيُّهَا الرَّجُلُ'de رَجُل çağrılan kişidir»",
   "right": "«Kimse çağrılmıyor — konuşan kendini erler içinde tahsis ediyor»",
   "why": {"en": "In the ikhtisas there is no addressee at all: the frame sentence is about the SPEAKER, and the nida-shaped phrase narrows him among a class. Reading it as a call misses the whole wajh.",
           "tr": "İhtisasta muhatap hiç yoktur: çerçeve cümle KONUŞAN hakkındadır; nidâ kılıklı öbek onu bir sınıf içinde daraltır. Bunu çağrı okumak vechin tamamını kaçırmaktır."}}],
 "relatedNotes": ["vocative-munada", "al-amr-wa-wujuhuh", "khuruj-al-istifham"]}

for note in (NOTE131, NOTE132, NOTE133):
    (GR / f"{note['id']}.json").write_text(json.dumps(note, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch29:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + imtathala, anfaqa, nazala, copies; notes 131-133")
