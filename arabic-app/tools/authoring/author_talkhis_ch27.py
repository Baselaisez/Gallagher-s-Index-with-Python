# -*- coding: utf-8 -*-
"""Author chapter 27 of talkhis-al-miftah — خُرُوجُ الِاسْتِفْهَامِ عَنْ أَصْلِهِ.

The question leaving its asl (sahifa 73-74): the source's ten wujuh, the
seven that fit real text carried as sentences, the rest in note 129.

  • istibta' — كَمْ دَعَوْتُكَ: the asker knows the count, so the «question»
    is reproach at slowness.
  • ta'ajjub — مَا لِيَ لَا أَرَى الْهُدْهُدَ (al-Naml 27:20): the مَا لِـ frame.
  • tanbih on straying — فَأَيْنَ تَذْهَبُونَ (al-Takwir 81:26).
  • inkar — أَغَيْرَ اللَّهِ تَدْعُونَ (al-An'am 6:40): the fronted object IS
    the denial's address.
  • taqrir by nafy-of-nafy — أَلَيْسَ اللَّهُ بِكَافٍ عَبْدَهُ (al-Zumar 39:36),
    with the zaida ba in laysa's khabar.
  • tahqir — مَنْ هَذَا. • istib'ad — أَنَّى لَهُمُ الذِّكْرَى (al-Dukhan 44:13).

ATTRIBUTION: the five ayat are received Qur'anic text quoted exactly;
كَمْ دَعَوْتُكَ and مَنْ هَذَا are the source's own worked examples verbatim
(research/sources/talkhis-al-miftah-balagha.txt lines ~2110-2150, sahifa
73-74), Ottoman plain-alif normalized to standard orthography — a
recorded normalization.

Grammar this chapter teaches:
  • note 129 `khuruj-al-istifham` — the ten wujuh with their receipts.
  • engine work: hamzaNafy (nafy-of-nafy = taqrir), kamIstibta (first-person
    madi after kam), the مَا لِـ frame (MaEngine 8c + maLiTaajjub), the
    widened hamzaMaful (a fronted MUDAF's plain fatha, the verb past the
    idafa chain), CaseEngine's laysa-mabni guard, the majhul singular's
    group's-waw plural, and the doer-in-the-cell expectation (a 1st/2nd
    person verb's fa'il is its own pronoun — expect the maf'ul).
"""
import json, pathlib, re, sys
ROOT = pathlib.Path('/home/user/Gallagher-s-Index-with-Python/arabic-app')
PKG = ROOT / "content/samples/talkhis-al-miftah"
sys.path.insert(0, str(ROOT / "tools/authoring"))
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

TITLE27 = {"ar": "خُرُوجُ الِاسْتِفْهَامِ عَنْ أَصْلِهِ",
           "en": "The Question Leaving Its Origin",
           "tr": "İstifhâmın Aslından Çıkışı"}

# ------------------------------------------------- s1 — istibta'
S.append({"id": "s1", "translation": {
 "en": "How often have I called you! (The asker knows the count — the question decays to ISTIBTA': reproach at the other's slowness.)",
 "tr": "Kaç kere çağırdım seni! (Soran sayıyı bilir — soru İSTİBTÂ'a düşer: karşı tarafın ağırdan almasına sitem.)"},
 "tokens": [
  tok("كَمْ","kam","pron",["khuruj-al-istifham","adawat-al-tasawwur"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ نَائِبٌ عَنِ الْمَفْعُولِ الْمُطْلَقِ — أَيْ كَمْ دَعْوَةٍ — وَالِاسْتِفْهَامُ خَارِجٌ إِلَى الِاسْتِبْطَاءِ.",
      "«how often» — كَمْ, mabni, in NASB position deputizing for the maf'ul mutlaq (how many a CALLING). And the question is no question: the caller knows the count, so the frame decays to istibta' — «all this calling, and still you are slow».",
      "«kaç kere» — كَمْ; mebnî; mef'ûl-i mutlaktan nâip olarak NASB mevkiinde (kaç ÇAĞIRIŞ). Ve soru, soru değildir: çağıran sayıyı bilir; kalıp istibtâ'a düşer — «bunca çağırdım, hâlâ ağırdan alıyorsun»."),
  tok("دَعَوْتُكَ","daa","verb",["khuruj-al-istifham"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.",
      "«I called you» — the madi of دَعَا, mabni on the sukun for the doer's ta; the ta is the fa'il and the kaf the object. A FIRST-PERSON madi after كَمْ is the engine's receipt for the istibta' reading.",
      "«çağırdım seni» — دَعَا'nın mâzîsi; fâil tâsına bitiştiği için sükûn üzere mebnî; tâ fâil, kâf mef'ûldür. كَمْ'den sonra BİRİNCİ ŞAHIS mâzî, makinenin istibtâ okuyuşu için makbuzudur.",
      punct="!",
      segments=[seg("دَعَوْتُ","daa","verb"), seg("كَ","pron-2ms","pron")])],
 "jumal": [
  J("كَمْ دَعَوْتُكَ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا — وَالطَّلَبُ فِيهَا صُورِيٌّ.",
    "The clause is insha'i and owns no mahall — and its «request» is a shell: nothing is really asked. The istifham machinery runs, but the answer-slot is already filled by the asker's own knowledge.",
    "Cümle inşâîdir, mahalli yok — ve «talebi» kabuktan ibarettir: gerçekte bir şey sorulmaz. İstifham makinesi çalışır; fakat cevap yuvası, soranın kendi bilgisiyle çoktan doludur."),
  J("كَمْ دَعَوْتُكَ",
    "الْوَجْهُ: الِاسْتِبْطَاءُ — سُؤَالُ الْمَرْءِ عَنْ فِعْلِ نَفْسِهِ لَا يَكُونُ حَقِيقِيًّا.",
    "THE WAJH: istibta'. The mechanical receipt is the person: a man cannot genuinely ask the count of his own past deed, so the first-person madi hands the reading over — reproach at slowness, «رَغْمًا: for all my calling, you did not answer».",
    "VECİH: istibtâ. Mekanik makbuz şahıstır: insan kendi geçmiş fiilinin sayısını gerçekten soramaz; birinci şahıs mâzî okuyuşu teslim eder — ağırdan almaya sitem: «bunca davetime rağmen icâbet etmedin».")]})

# ------------------------------------------------- s2 — ta'ajjub, Naml 27:20
S.append({"id": "s2", "translation": {
 "en": "What is it to me that I do not see the hoopoe? (al-Naml 27:20 — the ma-li frame: wonder wearing a question.)",
 "tr": "Bana ne oluyor ki hüdhüdü göremiyorum? (Neml 27:20 — mâ-li kalıbı: soru kılığında hayret.)"},
 "tokens": [
  tok("مَا","ma-istifham","pron",["khuruj-al-istifham","anwa-ma"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالِاسْتِفْهَامُ لِلتَّعَجُّبِ.",
      "«what» — the interrogative ma as mubtada; and the question is WONDER: Sulayman marvels at the state, he does not request news. The مَا لِـ frame is the receipt.",
      "«ne» — mübtedâ olarak istifham mâsı; ve soru HAYRETtir: Süleyman hâle şaşar, havadis istemez. مَا لِـ kalıbı makbuzdur."),
  tok("لِيَ","li","part",["khuruj-al-istifham"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْيَاءُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ خَبَرٌ.",
      "«to me» — the jarr lam with the speaker's ya in jarr position; the phrase is the khabar. مَا لِيَ، مَا لَكَ، مَا لَهُمْ — one frame, declined through the persons.",
      "«bana» — cer lâmı ile mütekellim yâsı, cer mevkiinde; öbek haberdir. مَا لِيَ، مَا لَكَ، مَا لَهُمْ — tek kalıp, şahıslara çekilmiş.",
      segments=[seg("لِ","li","part"), seg("يَ","pron-1s","pron")]),
  tok("لَا","la","part",["khuruj-al-istifham"],
      "حَرْفُ نَفْيٍ.",
      "«not» — the negation opening the hal-clause: the state marvelled at is itself negative.",
      "«değil/-me» — hâl cümlesini açan nefiy harfi: şaşılan hâlin kendisi menfîdir."),
  tok("أَرَى","raa","verb",["khuruj-al-istifham"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الْمُقَدَّرَةُ عَلَى الْأَلِفِ لِلتَّعَذُّرِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنَا — وَالْجُمْلَةُ حَالٌ.",
      "«I (do not) see» — the mudari of رَأَى, its raf' a damma ESTIMATED on the alif (ta'adhdhur); the doer is the concealed «I», and the clause stands as hal. Its own doer being in the cell, the noun after it can only be the object.",
      "«görmüyorum» — رَأَى'nın muzârisi; ref'i elif üzerinde TAKDÎRÎ dammedir (taazzür); fâili gizli «ben»dir ve cümle hâl olarak durur. Fâili kendi hanesinde olunca, ardındaki isim ancak mef'ûl olabilir."),
  tok("الْهُدْهُدَ","hudhud","noun",["khuruj-al-istifham"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ.",
      "«the hoopoe» — the object, mansub by the plain fatha: the missing bird the whole marvel turns on.",
      "«hüdhüdü» — mef'ûlün bih; açık fethayla mansub: bütün hayretin döndüğü kayıp kuş.",
      punct="؟")],
 "jumal": [
  J("مَا لِيَ",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ ابْتِدَائِيَّةٌ — مُبْتَدَأٌ وَخَبَرُهُ شِبْهُ جُمْلَةٍ.",
    "The frame-clause: an asking mubtada with a bare jarr-phrase khabar. The negation cannot be this ma — the phrase gives it nothing to deny — so the question owns the head by structure, not by taste.",
    "Kalıp cümlesi: soran mübtedâ + yalın câr-mecrûr haber. Nefiy bu mâ olamaz — öbek ona inkâr edecek şey vermez — soru başa zevkle değil YAPIyla sahiptir."),
  J("لَا أَرَى الْهُدْهُدَ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ نَصْبٍ حَالٌ.",
    "The negated seeing stands as HAL in nasb position: «what is to me, BEING one who does not see the hoopoe?» — the state is the thing marvelled at.",
    "Menfî görme, nasb mevkiinde HÂL olarak durur: «hüdhüdü GÖRMEZ hâlde bana ne oluyor?» — şaşılan şey hâlin kendisidir."),
  J("مَا لِيَ لَا أَرَى الْهُدْهُدَ",
    "الْوَجْهُ: التَّعَجُّبُ.",
    "THE WAJH: ta'ajjub. The aya's asker rules the birds — the absence should be impossible, and the question-shape carries the impossibility better than any exclamation would.",
    "VECİH: taaccüp. Âyetin soranı kuşlara hükmeder — yokluk imkânsız olmalıydı; soru kalıbı imkânsızlığı her nidâdan iyi taşır.")]})

# ------------------------------------------------- s3 — tanbih, Takwir 81:26
S.append({"id": "s3", "translation": {
 "en": "So where are you going? (al-Takwir 81:26 — not geography: a waking-cry at straying.)",
 "tr": "Peki nereye gidiyorsunuz? (Tekvîr 81:26 — coğrafya değil: sapıklığa karşı bir uyandırma nidâsı.)"},
 "tokens": [
  tok("فَأَيْنَ","ayna","pron",["khuruj-al-istifham","adawat-al-tasawwur"],
      "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَأَيْنَ اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ مُتَعَلِّقٌ بِتَذْهَبُونَ — وَالِاسْتِفْهَامُ لِلتَّنْبِيهِ عَلَى الضَّلَالِ.",
      "«so where» — the resuming fa, then أَيْنَ in its nasb position on the zarfiyya. No place is really asked: the aya shakes the strayer awake — TANBIH on the straying — by making him look for his own road and find none.",
      "«peki nereye» — isti'nâf fâsı, sonra zarfiyye üzere nasb mevkiinde أَيْنَ. Gerçekte yer sorulmaz: âyet sapanı sarsıp uyandırır — dalâlet üzerine TENBÎH — ona kendi yolunu aratıp bulamamasıyla.",
      segments=[seg("فَ","fa","part"), seg("أَيْنَ","ayna","pron")]),
  tok("تَذْهَبُونَ","dhahaba","verb",["khuruj-al-istifham"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ.",
      "«you are going» — a five-verbs mudari, marfu' by the RETAINED nun, its waw the doer.",
      "«gidiyorsunuz» — ef'âl-i hamseden bir muzâri; SABİT nunla merfû; vâvı fâildir.",
      punct="؟")],
 "jumal": [
  J("فَأَيْنَ تَذْهَبُونَ",
    "جُمْلَةٌ فِعْلِيَّةٌ اسْتِئْنَافِيَّةٌ لَا مَحَلَّ لَهَا.",
    "A resumed verbal clause, no mahall — the fa turns from the description of the Qur'an to the men walking away from it.",
    "İsti'nâfla açılmış fiil cümlesi, mahalli yok — fâ, Kur'ân'ın vasfından ondan uzaklaşan adamlara döner."),
  J("فَأَيْنَ تَذْهَبُونَ",
    "الْوَجْهُ: التَّنْبِيهُ عَلَى الضَّلَالِ.",
    "THE WAJH: tanbih on straying. The question presupposes a road worth naming and dares the hearer to name his — the failure to answer IS the awakening.",
    "VECİH: dalâlet üzerine tenbîh. Soru, adlandırmaya değer bir yol varsayar ve dinleyene kendi yolunu adlandırmayı teklif eder — cevap verememenin kendisi uyanıştır.")]})

# ------------------------------------------------- s4 — inkar, An'am 6:40
S.append({"id": "s4", "translation": {
 "en": "Is it other than Allah you would call? (al-An'am 6:40 — the fronted object is the denial's address: INKAR.)",
 "tr": "Allah'tan başkasına mı yalvarırsınız? (En'âm 6:40 — öne alınmış mef'ûl, inkârın adresidir: İNKÂR.)"},
 "tokens": [
  tok("أَغَيْرَ","ghayr","noun",["khuruj-al-istifham","al-istifham"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ الْإِنْكَارِيِّ، وَغَيْرَ مَفْعُولٌ بِهِ مُقَدَّمٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ وَهُوَ مُضَافٌ — وَتَقْدِيمُهُ هُوَ مَوْضِعُ الْإِنْكَارِ.",
      "«is it OTHER than…» — the hamza of denial, and غَيْرَ the FRONTED object, mansub by a plain fatha (the idafa took its tanwin), itself mudaf. What follows the hamza is what is asked — and here what is denied: not the calling, but its ADDRESS.",
      "«BAŞKASINA mı…» — inkâr hemzesi ve غَيْرَ, ÖNE ALINMIŞ mef'ûl; açık fethayla mansub (tenvinini izâfet aldı), kendisi muzâf. Hemzeyi izleyen, sorulandır — burada inkâr edilendir: yalvarma değil, ADRESİ."),
  tok("اللَّهِ","allah","propn",["khuruj-al-istifham"],
      "لَفْظُ الْجَلَالَةِ مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ.",
      "«than Allah» — the Name as mudaf ilayh, majrur by the kasra.",
      "«Allah'tan» — muzâfun ileyh olarak lafza-i celâl; kesrayla mecrur."),
  tok("تَدْعُونَ","daa","verb",["khuruj-al-istifham"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَمَفْعُولُهُ مُقَدَّمٌ عَلَيْهِ.",
      "«you would call» — the five-verbs mudari of دَعَا, marfu' by the retained nun, the waw its doer — and its object stands two words BEFORE it, past the Name it annexes.",
      "«yalvarırsınız» — دَعَا'nın ef'âl-i hamse muzârisi; sabit nunla merfû; vâvı fâil — ve mef'ûlü, muzâf olduğu İsmi aşıp iki kelime ÖNÜNDE durur.",
      punct="؟")],
 "jumal": [
  J("أَغَيْرَ اللَّهِ تَدْعُونَ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ — قُدِّمَ الْمَفْعُولُ لِإِفَادَةِ الِاخْتِصَاصِ بِالْإِنْكَارِ.",
    "A verbal clause with its object thrown to the front: the fronting narrows the denial to the ADDRESS — «calling is fine; calling OTHER THAN HIM is what cannot stand». Taqdim doctrine and istifham doctrine in one machine.",
    "Mef'ûlü öne fırlatılmış fiil cümlesi: takdim, inkârı ADRESe daraltır — «yalvarmak tamam; O'NDAN BAŞKASINA yalvarmak, duramayacak olandır». Takdim doktrini ile istifham doktrini tek makinede."),
  J("أَغَيْرَ اللَّهِ تَدْعُونَ",
    "الْوَجْهُ: الْإِنْكَارُ الْإِبْطَالِيُّ — مَا بَعْدَ الْهَمْزَةِ غَيْرُ وَاقِعٍ وَمُدَّعِيهِ كَاذِبٌ.",
    "THE WAJH: inkar ibtali — what stands after the hamza is claimed NOT TO HAPPEN rightly at all; the question-shape makes the hearer himself condemn it.",
    "VECİH: inkâr-ı ibtâlî — hemzeden sonraki şeyin hakça hiç OLMADIĞI savunulur; soru kalıbı, dinleyene onu bizzat mahkûm ettirir.")]})

# ------------------------------------------------- s5 — taqrir, Zumar 39:36
S.append({"id": "s5", "translation": {
 "en": "Is Allah not sufficient for His servant? (al-Zumar 39:36 — two negatives birth an affirmation: TAQRIR.)",
 "tr": "Allah kuluna yetmez mi? (Zümer 39:36 — iki menfîden bir müsbet doğar: TAKRÎR.)"},
 "tokens": [
  tok("أَلَيْسَ","laysa","verb",["khuruj-al-istifham","al-istifham"],
      "الْهَمْزَةُ لِلِاسْتِفْهَامِ التَّقْرِيرِيِّ — نَفْيُ النَّفْيِ إِثْبَاتٌ — وَلَيْسَ فِعْلٌ مَاضٍ جَامِدٌ نَاقِصٌ مَبْنِيٌّ عَلَى الْفَتْحِ.",
      "«is it not…» — the hamza riding the NEGATION: two negatives birth an affirmation, so the question extracts a yes stronger than any statement. لَيْسَ itself is the jamid nasikh, a mazi mabni on the fatha.",
      "«değil mi…» — NEFYİN üzerine binen hemze: iki menfîden bir müsbet doğar; soru, her düz cümleden güçlü bir evet çıkarır. لَيْسَ ise câmid nâsihtir; fetha üzere mebnî bir mâzî."),
  tok("اللَّهُ","allah","propn",["khuruj-al-istifham"],
      "لَفْظُ الْجَلَالَةِ اسْمُ لَيْسَ مَرْفُوعٌ بِالضَّمَّةِ.",
      "«Allah» — laysa's ism, marfu' by the damma.",
      "«Allah» — لَيْسَ'nin ismi; dammeyle merfû."),
  tok("بِكَافٍ","kafin","noun",["khuruj-al-istifham","huruf-jarr"],
      "الْبَاءُ حَرْفُ جَرٍّ زَائِدٌ لِتَوْكِيدِ النَّفْيِ، وَكَافٍ خَبَرُ لَيْسَ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — اسْمُ فَاعِلٍ مَنْقُوصٌ مِنْ كَفَى، وَتَنْوِينُهُ عِوَضٌ عَنِ الْيَاءِ الْمَحْذُوفَةِ.",
      "«sufficient» — laysa's khabar wearing the ZAIDA BA: majrur in letter, mansub in place, the extra letter fastening the negation the hamza will then overturn. And the word is a manqus ism fa'il of كَفَى — its tanwin the 'iwad for the dropped ya.",
      "«kâfî» — ZÂİDE BÂ giymiş لَيْسَ haberi: lafzan mecrur, mahallen mansub; fazla harf, hemzenin sonra devireceği nefyi perçinler. Kelime ise كَفَى'nın menkūs ism-i fâilidir — tenvini, düşen yânın ivazıdır.",
      segments=[seg("بِ","bi","part"), seg("كَافٍ","kafin","noun")]),
  tok("عَبْدَهُ","abd","noun",["khuruj-al-istifham"],
      "مَفْعُولٌ بِهِ لِاسْمِ الْفَاعِلِ كَافٍ مَنْصُوبٌ بِالْفَتْحَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — اسْمُ الْفَاعِلِ يَعْمَلُ عَمَلَ فِعْلِهِ.",
      "«His servant» — the OBJECT of the participle كَافٍ (an ism fa'il governs like its verb), mansub by the fatha, the ha its mudaf ilayh.",
      "«kulunu» — ism-i fâil كَافٍ'nin MEF'ÛLÜ (ism-i fâil, fiili gibi amel eder); fethayla mansub; hâ muzâfun ileyhtir.",
      punct="؟")],
 "jumal": [
  J("أَلَيْسَ اللَّهُ بِكَافٍ عَبْدَهُ",
    "جُمْلَةٌ إِنْشَائِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا — وَالتَّقْرِيرُ حَمْلُ الْمُخَاطَبِ عَلَى الْإِقْرَارِ.",
    "The taqrir machine whole: laysa denies, the ba rivets the denial, the hamza overturns both — and the hearer is carried to CONCEDE the sufficiency in his own voice. The strongest yes in the language is manufactured from two no's.",
    "Takrîr makinesi bütün hâlinde: لَيْسَ inkâr eder, bâ inkârı perçinler, hemze ikisini birden devirir — ve dinleyen, yeterliği KENDİ sesiyle teslime taşınır. Dilin en güçlü evet'i iki hayırdan imal edilir."),
  J("بِكَافٍ",
    "الْبَاءُ الزَّائِدَةُ فِي خَبَرِ لَيْسَ — تَوْكِيدٌ لَا تَعَلُّقَ لَهَا.",
    "THE ZAIDA BA: it governs a real jarr yet attaches to nothing — added purely to press the negation. Drop it and the sentence stands (أَلَيْسَ اللَّهُ كَافِيًا); keep it and the denial-to-be-overturned is louder.",
    "ZÂİDE BÂ: gerçek bir cer yapar ama hiçbir şeye taalluk etmez — sırf nefyi bastırmak için eklenmiştir. Atın, cümle ayakta kalır (أَلَيْسَ اللَّهُ كَافِيًا); tutun, devrilecek inkâr daha gür olur.")]})

# ------------------------------------------------- s6 — tahqir
S.append({"id": "s6", "translation": {
 "en": "Who is THIS? (Said of one present and known — the question belittles: TAHQIR.)",
 "tr": "Kim BU? (Orada olan ve bilinen biri için — soru küçümser: TAHKÎR.)"},
 "tokens": [
  tok("مَنْ","man-istifham","pron",["khuruj-al-istifham"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — وَالِاسْتِفْهَامُ لِلتَّحْقِيرِ.",
      "«who» — the person-ask as mubtada; but the speaker SEES the man and knows him. A question with its answer standing in the room is no question — it belittles.",
      "«kim» — mübtedâ olarak kişi sorusu; fakat konuşan adamı GÖRÜR ve bilir. Cevabı odada dikilen soru, soru değildir — küçümser."),
  tok("هَذَا","hadha","pron",["khuruj-al-istifham"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "«this one» — the demonstrative as khabar: the pointing finger does the belittling, reducing a named man to a «this».",
      "«bu» — haber olarak işaret ismi: küçümsemeyi işaret parmağı yapar; adı olan adamı bir «bu»ya indirger.",
      punct="؟")],
 "jumal": [
  J("مَنْ هَذَا",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "Two mabni words, a complete sentence — the smallest clause in the chapter carries the sharpest edge.",
    "İki mebnî kelime, tam bir cümle — bâbın en küçük cümlesi en keskin ağzı taşır."),
  J("مَنْ هَذَا",
    "الْوَجْهُ: التَّحْقِيرُ — وَبِعَكْسِهِ التَّهْوِيلُ: مَنْ فِرْعَوْنُ.",
    "THE WAJH: tahqir — and its mirror is TAHWIL: in Ibn 'Abbas's reading مَنْ فِرْعَوْنُ, the same shape aggrandizes the named terror. One frame, and the context alone decides whether it shrinks or enlarges.",
    "VECİH: tahkîr — aynası TEHVÎLdir: İbn Abbâs kıraatindeki مَنْ فِرْعَوْنُ, aynı kalıpla adlandırılmış dehşeti büyütür. Tek kalıp; küçültme mi büyütme mi olduğuna yalnız bağlam karar verir.")]})

# ------------------------------------------------- s7 — istib'ad, Dukhan 44:13
S.append({"id": "s7", "translation": {
 "en": "Whence, for them, the remembering? (al-Dukhan 44:13 — the reminder came and was refused: ISTIB'AD, the thing placed beyond reach.)",
 "tr": "Nereden olacak onlara öğüt almak? (Duhân 44:13 — hatırlatıcı geldi ve reddedildi: İSTİB'ÂD; şey erişilmezliğe konur.)"},
 "tokens": [
  tok("أَنَّى","anna-istifham","pron",["khuruj-al-istifham","adawat-al-tasawwur"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ — بِمَعْنَى مِنْ أَيْنَ — فِي مَحَلِّ نَصْبٍ، خَبَرٌ مُقَدَّمٌ، وَالِاسْتِفْهَامُ لِلِاسْتِبْعَادِ.",
      "«whence» — أَنَّى in its min-ayna face (a nominal follows), fronted khabar — and the ask is ISTIB'AD: no source is sought; the remembering is declared to have none left.",
      "«nereden» — min-eyne yüzünde أَنَّى (ardında isim cümlesi), mukaddem haber — ve soru İSTİB'ÂDdır: kaynak aranmaz; öğüt almanın kaynağı kalmadığı ilân edilir."),
  tok("لَهُمُ","li","part",["khuruj-al-istifham"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْهَاءُ وَالْمِيمُ ضَمِيرٌ فِي مَحَلِّ جَرٍّ — وَضُمَّتِ الْمِيمُ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«for them» — the jarr lam with the plural pronoun; the mim takes a damma where its sukun met the article's silent alif — the iltiqa repair, worn on a pronoun.",
      "«onlara» — cer lâmı ile çoğul zamiri; mîm, sükûnu harf-i tarifin sessiz elifiyle karşılaşınca damme aldı — iltikā tamiri, bir zamirin üstünde.",
      segments=[seg("لَ","li","part"), seg("هُمُ","hum","pron")]),
  tok("الذِّكْرَى","dhikra","noun",["khuruj-al-istifham"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ الْمُقَدَّرَةِ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ.",
      "«the remembering» — deferred mubtada, its damma ESTIMATED on the maqsur alif (ta'adhdhur). The aya continues: a clear Messenger had already come — and they turned away.",
      "«öğüt almak» — muahhar mübtedâ; dammesi maksûr elif üzerinde TAKDÎRÎdir (taazzür). Âyet devam eder: apaçık bir Peygamber zaten gelmişti — ve yüz çevirdiler.",
      punct="؟")],
 "jumal": [
  J("أَنَّى لَهُمُ الذِّكْرَى",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The structural face is ch26's أَنَّى لَكِ هَذَا exactly — nominal, verbless, min-ayna. The RHETORIC flips it: Maryam's question had an answer (من عند الله); this one is asked because none is left.",
    "Yapısal yüz, tam olarak 26. bâbın أَنَّى لَكِ هَذَا'sıdır — isim cümlesi, fiilsiz, min-eyne. RETORİK onu ters çevirir: Meryem'in sorusunun cevabı vardı (من عند الله); bu, hiç kalmadığı için sorulur."),
  J("أَنَّى لَهُمُ الذِّكْرَى",
    "الْوَجْهُ: الِاسْتِبْعَادُ — وَقَدْ جَاءَهُمْ رَسُولٌ مُبِينٌ ثُمَّ تَوَلَّوْا عَنْهُ.",
    "THE WAJH: istib'ad. The aya's own next clause is the proof — the clear Messenger CAME and they turned away; asking «whence now?» places the remembering beyond their reach forever.",
    "VECİH: istib'âd. Âyetin kendi devam cümlesi delildir — apaçık Peygamber GELDİ ve yüz çevirdiler; «şimdi nereden?» diye sormak, öğüt almayı erişimlerinin ebediyen ötesine koyar.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "hudhud": g("هُدْهُد", None, "noun", "hoopoe (Sulayman's messenger-bird)", "hüdhüd (Süleyman'ın haberci kuşu)", 4, plural="هَدَاهِد"),
 "dhikra": g("ذِكْرَى", "ذ ك ر", "noun", "remembrance, taking heed (a maqsur noun)", "öğüt alma, hatırlayış (maksûr isim)", 4),
 "kafin": g("كَافٍ", "ك ف ي", "noun", "sufficient (ism fa'il of كَفَى, manqus — its tanwin replaces the dropped ya)",
            "kâfî, yeter (كَفَى'nın ism-i fâili, menkūs — tenvini düşen yânın ivazıdır)", 4),
 "pron-2fs": g("كِ", None, "pron", "you (fem. sg., attached)", "sen (dişil, bitişik zamir)", 1),
 "la": copy_gloss("aqaid-ahl-al-sunna", "la"),
 "dhahaba": copy_gloss("wasiyyat-abi-hanifa", "dhahaba"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/27.json").write_text(
    json.dumps({"chapter": 27, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 27 for c in man["chapters"]):
    man["chapters"].append({"n": 27, "title": TITLE27})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.27.0"
ADD_EN = (" Chapter 27 carries the question's departures from its asl (lines ~2110-2150, sahifa 73-74): "
          "مَا لِيَ لَا أَرَى الْهُدْهُدَ, فَأَيْنَ تَذْهَبُونَ, أَغَيْرَ اللَّهِ تَدْعُونَ, أَلَيْسَ اللَّهُ "
          "بِكَافٍ عَبْدَهُ and أَنَّى لَهُمُ الذِّكْرَى are received Qur'anic text quoted exactly — al-Naml "
          "27:20, al-Takwir 81:26, al-An'am 6:40, al-Zumar 39:36 and al-Dukhan 44:13; كَمْ دَعَوْتُكَ and "
          "مَنْ هَذَا are the source's own worked examples verbatim, Ottoman plain-alif normalized to "
          "standard orthography — a recorded normalization.")
ADD_TR = (" Yirmi yedinci bâb, sorunun aslından çıkışlarını taşır (satır ~2110-2150, sahife 73-74): "
          "مَا لِيَ لَا أَرَى الْهُدْهُدَ, فَأَيْنَ تَذْهَبُونَ, أَغَيْرَ اللَّهِ تَدْعُونَ, أَلَيْسَ اللَّهُ "
          "بِكَافٍ عَبْدَهُ ve أَنَّى لَهُمُ الذِّكْرَى aynen alınmış mervî Kur'ân metnidir — Neml 27:20, "
          "Tekvîr 81:26, En'âm 6:40, Zümer 39:36 ve Duhân 44:13; كَمْ دَعَوْتُكَ ile مَنْ هَذَا kaynağın "
          "kendi işlenmiş örneklerinin aynen alınmışıdır; Osmanlı düz-elif imlâsı standart imlâya "
          "çevrilmiştir — kayıtlı bir normalizasyondur.")
if "2110-2150" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "dhahaba" not in mo["verbs"]:
    mo["verbs"]["dhahaba"] = copy_verb("wasiyyat-abi-hanifa", "dhahaba")
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch27:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD), "; morph + dhahaba(copy)")
