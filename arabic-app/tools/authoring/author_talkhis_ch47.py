# -*- coding: utf-8 -*-
"""Author chapter 47 of talkhis-al-miftah — وَجْهُ الشَّبَهِ (sahifa 105-106,
lines ~3028-3080): the definition of the wajh, its tahqiq/takhyil, the
نُجُوم/سُنَن bayt and the two hadiths the source hangs on it, the
النَّحْوُ كَالْمِلْحِ saying with its khilaf on the wajh, and the divisions
of the wajh (inside/outside the two essences; hissi, ʿaqli, idafi; one,
several, composite).

  s1      the matn's definition, Arabic as the source prints it:
          وَجْهُ الشَّبَهِ مَا يَشْتَرِكَانِ فِيهِ تَحْقِيقًا أَوْ تَخْيِيلًا.
  s2-s3   فَالْأَوَّلُ كَمَا مَرَّ / وَالثَّانِي كَقَوْلِهِ — RESTORED (the source
          gives the two branches only in Turkish).
  s4      Abu l-Qasim's bayt as the source recites it, split at the hemistich:
          وَكَأَنَّ النُّجُومَ بَيْنَ دُجَاهَا • سُنَنٌ لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ
  s5-s6   the nukta — RESTORED from the source's Turkish: the wajh is the
          hay'a of bright white things around a dark black one, and it is in
          the mushabbah bihi only by takhyil.
  s7-s9   the hadith the source cites from Ruh al-Bayan, as printed, split
          at its clauses (إِنْ أَرَدْتُمْ … فَادْرُسُوا الْقُرْآنَ فَإِنَّهُ …).
  s10     أَتَيْتُكُمْ بِالْحَنِيفِيَّةِ الْبَيْضَاءِ — as printed.
  s11     شَاهَدْتُ سَوَادَ الْكُفْرِ مِنْ جَبِينِ فُلَانٍ — as printed.
  s12-s14 the reasoning — RESTORED: bid'a as walking in darkness, so it was
          likened to darkness; and by reversal the sunna to light.
  s15     النَّحْوُ فِي الْكَلَامِ كَالْمِلْحِ فِي الطَّعَامِ — as printed.
  s16-s18 the khilaf on its wajh — RESTORED from the source's Turkish
          (little reforms / much spoils is corrupt; the wajh is: its
          presence reforms, its absence spoils).
  s19-s22 the divisions of the wajh — the matn, restored where the source
          carries only the Turkish (marked so).

Every likening carries an AUTHORED `tashbih` frame — the arkan by token
index, the kind, and the SHAPES (mufrad / muqayyad / murakkab) of the two
ends and of the spoken wajh — which TashbihEngine must read back.

Grammar this chapter teaches: note 152 `wajh-al-shabah` (group bayan); the
five verbs with the dual alif (يَشْتَرِكَانِ); the masdar as hal (تَحْقِيقًا);
the shart with a fa-jawab (إِنْ أَرَدْتُمْ … فَادْرُسُوا); the diptote mudaf
ilayh (أَشْيَاءَ); the nisba sifas; the atf with أَوْ; paradigms اِشْتَرَكَ,
شَاهَدَ, شَبَّهَ, أَصْلَحَ, أَفْسَدَ, مَشَى; أَرَادَ, دَرَسَ, لَاحَ, لَزِمَ copied.
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
def copy_morph(pkg, key):
    return json.loads((ROOT / f"content/samples/{pkg}/morphology.json").read_text(encoding="utf-8"))["verbs"][key]
S = []
W = "wajh-al-shabah"; A = "arkan-al-tashbih"

TITLE47 = {"ar": "وَجْهُ الشَّبَهِ: تَعْرِيفُهُ وَتَحْقِيقُهُ وَتَخْيِيلُهُ وَأَقْسَامُهُ",
           "en": "The Wajh al-Shabah: its Definition, its Tahqiq and Takhyil, and its Divisions",
           "tr": "Vech-i Şebeh: Tarifi, Tahkîki ve Tahyîli, Kısımları"}

# ----------- s1 — the definition (matn, as printed)
S.append({"id": "s1", "translation": {
 "en": "The wajh al-shabah is what the two share in — really, or by imagination.",
 "tr": "Vech-i şebeh, ikisinin kendisinde ortak olduğu şeydir — gerçekten, yahut hayal yoluyla."},
 "tokens": [
  tok("وَجْهُ","wajh","noun",[W,"mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the face of» — the mubtada, a mudaf: the term being defined.",
      "«yüzü» — mübtedâ, muzâf: tarif edilen terim."),
  tok("الشَّبَهِ","shabah","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«the likeness» — the mudaf ilayh: وَجْهُ الشَّبَهِ, the face the likeness turns to us.",
      "«benzerliğin» — muzâfun ileyh: وَجْهُ الشَّبَهِ, benzerliğin bize dönük yüzü."),
  tok("مَا","ma-mawsula","pron",[W,"ism-mawsul","mubtada-khabar"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ خَبَرٌ.",
      "«that which» — the relative, the khabar; its clause follows.",
      "«… şey» — ism-i mevsûl, haber; sılası ardından gelir."),
  tok("يَشْتَرِكَانِ","ishtaraka","verb",[W,"afal-khamsa","al-muthanna","form-viii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِثُبُوتِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَأَلِفُ الِاثْنَيْنِ فَاعِلٌ — وَالْجُمْلَةُ صِلَةُ مَا.",
      "«the two share» — one of the five verbs, raf' by the RETAINED nun; the dual alif is its fa'il (the two ends); the clause is the sila.",
      "«ikisi ortaktır» — ef'âl-i hamseden, ref'i nûnun sübûtuyla; tesniye elifi fâil (iki taraf); cümle sıladır."),
  tok("فِيهِ","fi","part",[W,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِيَشْتَرِكَانِ — وَالْهَاءُ الْعَائِدُ إِلَى مَا.",
      "«in it» — attached to the verb; the ha is the ʿaid pointing back to مَا.",
      "«onda» — fiile müteallik; hâ, مَا'ya dönen âiddir.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("تَحْقِيقًا","tahqiq","noun",[W,"hal","masdar"],
      "حَالٌ مَنْصُوبٌ — مَصْدَرٌ وَاقِعٌ مَوْقِعَ الْحَالِ، أَيْ: مُحَقَّقًا.",
      "«in truth» — a masdar standing as HAL (= مُحَقَّقًا): the shared meaning really there.",
      "«tahkîken» — hâl yerinde masdar (= مُحَقَّقًا): ortak mânâ gerçekten orada."),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ لِلتَّقْسِيمِ.",
      "«or» — the atf of division.",
      "«yahut» — taksim atfı."),
  tok("تَخْيِيلًا","takhyil","noun",[W,"hal","masdar","atf-nasaq"],
      "مَعْطُوفٌ عَلَى تَحْقِيقًا مَنْصُوبٌ — أَيْ: مُتَخَيَّلًا.",
      "«or by imagination» — joined to the first hal (= مُتَخَيَّلًا): the meaning imagined into the other end.",
      "«yahut tahyîlen» — ilk hâle atıf (= مُتَخَيَّلًا): mânâ öteki tarafa hayal edilmiş.",
      punct=".")],
 "jumal": [
  J("يَشْتَرِكَانِ فِيهِ",
    "جُمْلَةٌ صِلَةُ الْمَوْصُولِ لَا مَحَلَّ لَهَا مِنَ الْإِعْرَابِ.",
    "The sila: no seat in i'rab. The dual alif inside it is the two ends — the definition names them without naming them.",
    "Sıla: i'râbdan mahalli yok. İçindeki tesniye elifi iki taraftır — tarif onları adlandırmadan adlandırır.")]})

# ----------- s2 — the first branch (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "The first is as has passed. (Restored: the source gives the two branches only in Turkish.)",
 "tr": "İlki, geçtiği gibidir. (Geri yazım: kaynak iki kolu yalnız Türkçe verir.)"},
 "tokens": [
  tok("فَالْأَوَّلُ","awwal","noun",[W,"mubtada-khabar"],
      "الْفَاءُ اسْتِئْنَافِيَّةٌ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«the first» (the tahqiqi) — the mubtada.",
      "«ilki» (tahkîkî) — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("الْأَوَّلُ","awwal","noun")]),
  tok("كَمَا","kama","part",[W,"huruf-jarr","an-masdariyya"],
      "الْكَافُ جَارَّةٌ وَمَا مَصْدَرِيَّةٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "«as» — the kaf of jarr over a masdar-ma; the phrase is the khabar.",
      "«gibi» — masdariye mâ üzerine cer kâfı; tamlama haberdir.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("مَرَّ","marra","verb",[W,"jumla-sifa"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ — وَالْجُمْلَةُ صِلَةُ مَا الْمَصْدَرِيَّةِ.",
      "«has passed» — the examples of the last chapter, where the shared meaning was real.",
      "«geçti» — geçen bâbın örnekleri; orada ortak mânâ gerçekti.",
      punct=".")]})

# ----------- s3 — the second branch (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "And the second is as in his saying: (Restored.)",
 "tr": "İkincisi ise onun şu sözündeki gibidir: (Geri yazım.)"},
 "tokens": [
  tok("وَالثَّانِي","thani","noun",[W,"mubtada-khabar","ism-maqsur-manqus"],
      "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ.",
      "«the second» (the takhyili) — a manqus mubtada, its damma estimated on the ya.",
      "«ikincisi» (tahyîlî) — menkūs mübtedâ, dammesi yâ üzerinde takdîrî.",
      segments=[seg("وَ","wa","conj"), seg("الثَّانِي","thani","noun")]),
  tok("كَقَوْلِهِ","qawl","noun",[W,"huruf-jarr","idafa-definiteness"],
      "الْكَافُ جَارَّةٌ وَقَوْلِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. وَهٰذِهِ كَافُ التَّمْثِيلِ لَا كَافُ التَّشْبِيهِ.",
      "«as in his saying» — the kaf that INTRODUCES AN EXAMPLE, not the kaf of likening: the engine refuses to read a tashbih here.",
      "«sözündeki gibi» — ÖRNEK GETİREN kâf, benzetme kâfı değil: motor burada teşbih okumayı reddeder.",
      punct=":",
      segments=[seg("كَ","ka","part"), seg("قَوْلِ","qawl","noun"), seg("هِ","pron-3ms","pron")])]})

# ----------- s4 — the bayt (as printed), split at the hemistich
S.append({"id": "s4", "translation": {
 "en": "«And it is as if the stars, amid its darkness, • were sunnas among which an innovation has shown.»",
 "tr": "«Sanki yıldızlar, gecenin karanlıkları arasında, • aralarında bir bid'at belirmiş sünnetlerdir.»"},
 "tashbih": {"mushabbah": [1, 2, 3], "adat": 0, "bihi": [4, 5, 6, 7], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": "muqayyad", "bihi": "murakkab", "wajh": None}},
 "tokens": [
  tok("وَكَأَنَّ","ka-anna","part",[W,A,"inna-wa-akhawatuha","tashbih"],
      "الْوَاوُ لِلِاسْتِئْنَافِ، وَكَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ — أَدَاةُ التَّشْبِيهِ.",
      "«and it is as if» — كَأَنَّ, the adat: inna's sister that carries the likening.",
      "«sanki» — كَأَنَّ, edat: benzetmeyi taşıyan inne kardeşi.",
      segments=[seg("وَ","wa","conj"), seg("كَأَنَّ","ka-anna","part")]),
  tok("النُّجُومَ","najm","noun",[W,A,"inna-wa-akhawatuha","jam-taksir"],
      "اسْمُ كَأَنَّ مَنْصُوبٌ — الْمُشَبَّهُ.",
      "«the stars» — the ism of كَأَنَّ: the MUSHABBAH.",
      "«yıldızlar» — كَأَنَّ'nin ismi: MÜŞEBBEH."),
  tok("بَيْنَ","bayna","noun",[W,"maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ — حَالٌ مِنَ النُّجُومِ، وَبِهِ صَارَ الْمُشَبَّهُ مُقَيَّدًا.",
      "«amid» — a zarf annexed to the next word, a hal of the stars: the RESTRICTION that makes the mushabbah muqayyad.",
      "«arasında» — sonraki kelimeye muzâf zarf, yıldızların hâli: müşebbehi mukayyed yapan KAYIT."),
  tok("دُجَاهَا","duja","noun",[W,"idafa-definiteness","ism-maqsur-manqus"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — عَائِدٌ إِلَى اللَّيْلَةِ.",
      "«its darkness» — a maqsur mudaf ilayh; the ha points to the night.",
      "«onun karanlığı» — maksûr muzâfun ileyh; hâ geceye râci'.",
      punct="•",
      segments=[seg("دُجَا","duja","noun"), seg("هَا","pron-3fs","pron")]),
  tok("سُنَنٌ","sunna","noun",[W,A,"inna-wa-akhawatuha","jam-taksir"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ، وَالْجُمْلَةُ بَعْدَهُ صِفَتُهُ.",
      "«sunnas» — the khabar of كَأَنَّ: the MUSHABBAH BIHI, and the clause after it is its sifa.",
      "«sünnetler» — كَأَنَّ'nin haberi: MÜŞEBBEHÜN BİH; ardındaki cümle sıfatıdır."),
  tok("لَاحَ","laha-verb","verb",[W,"jumla-sifa","hollow-verbs"],
      "فِعْلٌ مَاضٍ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِسُنَنٍ؛ وَبِهَا صَارَ الْمُشَبَّهُ بِهِ مُرَكَّبًا.",
      "«has shown» — the clause is the sifa of سُنَنٌ; with it the mushabbah bihi becomes MURAKKAB, a whole picture.",
      "«belirdi» — cümle سُنَنٌ'in sıfatı; onunla müşebbehün bih MÜREKKEB, bir bütün tablo olur."),
  tok("بَيْنَهُنَّ","bayna","noun",[W,"maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ مُتَعَلِّقٌ بِلَاحَ وَهُوَ مُضَافٌ، وَالضَّمِيرُ مُضَافٌ إِلَيْهِ — عَائِدٌ إِلَى سُنَنٍ.",
      "«among them» — the zarf; its pronoun is the ʿaid that ties the clause to سُنَنٌ.",
      "«aralarında» — zarf; zamiri, cümleyi سُنَنٌ'e bağlayan âiddir.",
      segments=[seg("بَيْنَ","bayna","noun"), seg("هُنَّ","pron-3fp","pron")]),
  tok("ابْتِدَاعٌ","ibtida","noun",[W,"fail","masdar","form-viii-verbs"],
      "فَاعِلٌ مَرْفُوعٌ — مَصْدَرُ ابْتَدَعَ.",
      "«an innovation» — the fa'il of لَاحَ: a Form VIII masdar.",
      "«bir bid'at» — لَاحَ'nın fâili: VIII. bâb masdarı.",
      punct=".")],
 "jumal": [
  J("لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ صِفَةٌ لِسُنَنٍ — وَبِهَا الْمُشَبَّهُ بِهِ مُرَكَّبٌ.",
    "The sifa clause on an indefinite khabar: the mushabbah bihi is not «sunnas» but «sunnas with an innovation showing among them» — a composite picture.",
    "Nekre habere sıfat cümlesi: müşebbehün bih «sünnetler» değil, «aralarında bir bid'at beliren sünnetler»dir — birleşik bir tablo."),
  J("النُّجُومَ بَيْنَ دُجَاهَا",
    "اسْمُ كَأَنَّ مَعَ ظَرْفٍ حَالٍ مِنْهُ — مُشَبَّهٌ مُقَيَّدٌ.",
    "The mushabbah is the stars AMID THE DARK: a single thing with a restriction — muqayyad.",
    "Müşebbeh, KARANLIK İÇİNDEKİ yıldızlardır: kayıtlı tek şey — mukayyed.")]})

# ----------- s5 — the wajh of the bayt (RESTORED)
S.append({"id": "s5", "translation": {
 "en": "The wajh al-shabah in it is the picture that arises from bright white things appearing on the sides of a dark black thing. (Restored from the source's note.)",
 "tr": "Ondaki vech-i şebeh, siyah karanlık bir şeyin etrafında beyaz parlak bir takım şeylerin belirmesinden meydana gelen hey'ettir. (Kaynağın notundan geri yazım.)"},
 "tokens": [
  tok("وَجْهُ","wajh","noun",[W,"mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَوَجْهُ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the wajh of» — the mubtada.", "«vechi» — mübtedâ."),
  tok("الشَّبَهِ","shabah","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness» —", "«benzerliğin» —"),
  tok("فِيهِ","fi","part",[W,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ — أَيْ: فِي هٰذَا الْبَيْتِ.",
      "«in it» — in this bayt.", "«onda» — bu beyitte.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْهَيْئَةُ","haya-shape","noun",[W,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ — الْهَيْئَةُ: الصُّورَةُ الْمُرَكَّبَةُ، وَهِيَ وَجْهُ الشَّبَهِ الْمُرَكَّبُ.",
      "«the picture» — the khabar: a HAY'A, a composite picture — the composite wajh in one word.",
      "«hey'et» — haber: HEY'ET, birleşik bir tablo — mürekkeb vech tek kelimede."),
  tok("الْحَاصِلَةُ","hasil","noun",[W,"naat-sifa","ism-fail"],
      "صِفَةٌ مَرْفُوعَةٌ — اسْمُ فَاعِلٍ مِنْ حَصَلَ.",
      "«that arises» — a na't, the ism fa'il.", "«hâsıl olan» — sıfat, ism-i fâil."),
  tok("مِنْ","min","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«from» —", "«-den» —"),
  tok("حُصُولِ","husul","noun",[W,"masdar","idafa-definiteness"],
      "مَجْرُورٌ بِمِنْ وَهُوَ مُضَافٌ — مَصْدَرٌ.",
      "«the appearing of» — a masdar, mudaf.", "«husûlünden» — masdar, muzâf."),
  tok("أَشْيَاءَ","shay","noun",[W,"mamnu-min-sarf","idafa-definiteness","jam-taksir"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ.",
      "«things» — the mudaf ilayh, a DIPTOTE: its jarr is a fatha standing in for the kasra.",
      "«şeylerin» — muzâfun ileyh, GAYR-İ MUNSARİF: cerri kesra yerine fethadır."),
  tok("مُشْرِقَةٍ","mushriq","noun",[W,"naat-sifa","ism-fail"],
      "صِفَةٌ مَجْرُورَةٌ — اسْمُ فَاعِلٍ مِنْ أَشْرَقَ.",
      "«bright» — the first na't of the things.", "«parlak» — şeylerin ilk sıfatı."),
  tok("بِيضٍ","bid-white","noun",[W,"naat-sifa","jam-taksir"],
      "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ — جَمْعُ أَبْيَضَ.",
      "«white» — the second na't: the plural of أَبْيَض.", "«beyaz» — ikinci sıfat: أَبْيَض'ın cem'i."),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«on» —", "«-de» —"),
  tok("جَوَانِبِ","janib","noun",[W,"idafa-definiteness","jam-taksir","mamnu-min-sarf"],
      "مَجْرُورٌ بِفِي بِالْكَسْرَةِ لِأَنَّهُ مُضَافٌ — وَهُوَ صِيغَةُ مُنْتَهَى الْجُمُوعِ، لَكِنَّ الْإِضَافَةَ تَرُدُّ إِلَيْهِ الْكَسْرَةَ.",
      "«the sides of» — a sighat muntaha al-jumu' that would refuse the kasra — but the IDAFA gives it back.",
      "«yanlarında» — kesrayı reddedecek bir müntehe'l-cumû' kalıbı — fakat İZÂFET kesrayı geri verir."),
  tok("شَيْءٍ","shay","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«a thing» —", "«bir şeyin» —"),
  tok("مُظْلِمٍ","muzlim","noun",[W,"naat-sifa","ism-fail"],
      "صِفَةٌ مَجْرُورَةٌ — اسْمُ فَاعِلٍ مِنْ أَظْلَمَ.",
      "«dark» — na't.", "«karanlık» — sıfat."),
  tok("أَسْوَدَ","aswad","noun",[W,"naat-sifa","mamnu-min-sarf"],
      "صِفَةٌ ثَانِيَةٌ مَجْرُورَةٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — أَفْعَلُ الْأَلْوَانِ.",
      "«black» — the colour-أَفْعَل, a diptote: jarr by a fatha.",
      "«siyah» — renk أَفْعَل'i, gayr-i munsarif: cerri fethayla.",
      punct=".")]})

# ----------- s6 — it is there only by takhyil (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And it does not exist in the mushabbah bihi except by way of imagination. (Restored.)",
 "tr": "O, müşebbehün bihte hayal yolundan başka bir yolla mevcut değildir. (Geri yazım.)"},
 "tokens": [
  tok("وَهِيَ","hiya","pron",[W,"mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَهِيَ ضَمِيرٌ مُنْفَصِلٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — عَائِدٌ إِلَى الْهَيْئَةِ.",
      "«and it» — the hay'a.", "«o» — hey'et.",
      segments=[seg("وَ","wa","conj"), seg("هِيَ","hiya","pron")]),
  tok("غَيْرُ","ghayr","noun",[W,"mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«not» — غَيْر as khabar, annexed to what it negates.", "«değil» — غَيْر haber, nefyettiğine muzâf."),
  tok("مَوْجُودَةٍ","mawjud","noun",[W,"idafa-definiteness","ism-maful"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ مَفْعُولٍ.",
      "«existing» — the mudaf ilayh.", "«mevcut» — muzâfun ileyh."),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("الْمُشَبَّهِ","mushabbah","noun",[W,A,"ism-maful"],
      "مَجْرُورٌ بِفِي.", "«the likened» —", "«müşebbeh» —"),
  tok("بِهِ","bi","part",[W,A,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِالْمُشَبَّهِ — الْمُشَبَّهُ بِهِ: الِاسْمُ الْمُرَكَّبُ لِلطَّرَفِ الثَّانِي.",
      "«-to» — الْمُشَبَّهُ بِهِ, the compound name of the second end.",
      "«bih» — الْمُشَبَّهُ بِهِ, ikinci tarafın bileşik adı.",
      segments=[seg("بِ","bi","part"), seg("هِ","pron-3ms","pron")]),
  tok("إِلَّا","illa","part",[W,"istithna-mufarragh"],
      "أَدَاةُ اسْتِثْنَاءٍ مُفَرَّغٍ.",
      "«except» — an emptied exception: what follows takes the case its seat demands.",
      "«ancak» — müferrağ istisnâ: sonrası, mevkiinin istediği hâli alır."),
  tok("عَلَى","ala","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«by» —", "«üzere» —"),
  tok("طَرِيقِ","tariq","noun",[W,"idafa-definiteness"],
      "مَجْرُورٌ بِعَلَى وَهُوَ مُضَافٌ — مُتَعَلِّقٌ بِمَوْجُودَةٍ.",
      "«the way of» —", "«yolu» —"),
  tok("التَّخْيِيلِ","takhyil","noun",[W,"idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ خَيَّلَ.",
      "«imagination» — Form II's masdar: the wajh is takhyili.",
      "«tahyîl» — II. bâb masdarı: vech tahyîlîdir.",
      punct=".")]})

# ----------- s7-s9 — the hadith (as printed), split at its clauses
S.append({"id": "s7", "translation": {
 "en": "«If you desire the life of the blessed, the death of the martyrs, and salvation on the Day of Gathering,",
 "tr": "«Saîdlerin hayatını, şehidlerin ölümünü, haşir gününde kurtuluşu isterseniz,"},
 "tokens": [
  tok("إِنْ","in-shartiyya","part",[W,"in-shartiyya"],
      "حَرْفُ شَرْطٍ جَازِمٌ.",
      "«if» — the conditional; its jawab comes with a fa two sentences on.",
      "«eğer» — şart edatı; cevabı iki cümle sonra fâ ile gelir."),
  tok("أَرَدْتُمْ","arada","verb",[W,"in-shartiyya","hollow-verbs"],
      "فِعْلٌ مَاضٍ فِي مَحَلِّ جَزْمٍ فِعْلُ الشَّرْطِ، وَالتَّاءُ فَاعِلٌ — أَجْوَفُ: أَصْلُهُ أَرْوَدْتُمْ.",
      "«you desire» — the shart verb, a mazi in the seat of jazm; hollow: the waw fell.",
      "«isterseniz» — şart fiili, cezm mahallinde mâzî; ecvef: vâv düşmüş."),
  tok("عَيْشَ","aysh","noun",[W,"maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«the life of» — the first object.", "«hayatını» — ilk mef'ûl."),
  tok("السُّعَدَاءِ","said","noun",[W,"idafa-definiteness","jam-taksir"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ سَعِيدٍ.",
      "«the blessed» — the plural of سَعِيد.", "«saîdlerin» — سَعِيد'in cem'i."),
  tok("وَمَوْتَ","mawt","noun",[W,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى عَيْشَ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«and the death of» — joined to the object.", "«ve ölümünü» — mef'ûle atıf.",
      segments=[seg("وَ","wa","conj"), seg("مَوْتَ","mawt","noun")]),
  tok("الشُّهَدَاءِ","shahid-martyr","noun",[W,"idafa-definiteness","jam-taksir"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ شَهِيدٍ.",
      "«the martyrs» —", "«şehidlerin» —"),
  tok("وَالنَّجَاةَ","najat","noun",[W,"atf-nasaq"],
      "مَعْطُوفٌ مَنْصُوبٌ.",
      "«and salvation» — the third object.", "«ve kurtuluşu» — üçüncü mef'ûl.",
      segments=[seg("وَ","wa","conj"), seg("النَّجَاةَ","najat","noun")]),
  tok("يَوْمَ","yawm","noun",[W,"maful-fih","idafa-definiteness"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«on the day of» — a zarf.", "«gününde» — zarf."),
  tok("الْحَشْرِ","hashr","noun",[W,"idafa-definiteness","masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.",
      "«gathering» —", "«haşir» —",
      punct="،")],
 "jumal": [
  J("إِنْ أَرَدْتُمْ",
    "فِعْلُ الشَّرْطِ مَاضٍ فِي مَحَلِّ جَزْمٍ؛ جَوَابُهُ فَادْرُسُوا بَعْدَ سِتَّةِ مَفَاعِيلَ.",
    "The shart opens here and its jawab (فَادْرُسُوا) waits behind six objects — the sentence is cut for reading, not for grammar.",
    "Şart burada açılır, cevabı (فَادْرُسُوا) altı mef'ûlün ardında bekler — cümle okumak için bölündü, gramer için değil.")]})

S.append({"id": "s8", "translation": {
 "en": "and shade on the Day of Scorching Heat, and guidance on the Day of Error — then study the Qur'an,",
 "tr": "kavurucu sıcak gününde gölgeyi, dalâlet gününde hidâyeti — o halde Kur'ân'ı ders edinin,"},
 "tokens": [
  tok("وَالظِّلَّ","zill","noun",[W,"atf-nasaq"],
      "مَعْطُوفٌ عَلَى عَيْشَ فِي الْجُمْلَةِ قَبْلَهَا مَنْصُوبٌ.",
      "«and shade» — joined to the objects of the sentence before.",
      "«ve gölgeyi» — önceki cümlenin mef'ûllerine atıf.",
      segments=[seg("وَ","wa","conj"), seg("الظِّلَّ","zill","noun")]),
  tok("يَوْمَ","yawm","noun",[W,"maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ.", "«on the day of» —", "«gününde» —"),
  tok("الْحَرُورِ","harur","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«scorching heat» —", "«kavurucu sıcak» —"),
  tok("وَالْهُدَى","huda","noun",[W,"atf-nasaq","ism-maqsur-manqus"],
      "مَعْطُوفٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ.",
      "«and guidance» — a maqsur: its fatha estimated.", "«ve hidâyeti» — maksûr: fethası takdîrî.",
      segments=[seg("وَ","wa","conj"), seg("الْهُدَى","huda","noun")]),
  tok("يَوْمَ","yawm","noun",[W,"maful-fih","idafa-definiteness"],
      "ظَرْفٌ مَنْصُوبٌ وَهُوَ مُضَافٌ.", "«on the day of» —", "«gününde» —"),
  tok("الضَّلَالَةِ","dalalah-error","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«error» —", "«dalâlet» —"),
  tok("فَادْرُسُوا","darasa","verb",[W,"in-shartiyya","imperative-amr","fa-khabar-mubtada"],
      "الْفَاءُ رَابِطَةٌ لِجَوَابِ الشَّرْطِ، وَادْرُسُوا فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ — وَالْجُمْلَةُ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ.",
      "«then study» — the fa binds the JAWAB (an imperative cannot be majzum, so the fa is required); the group's waw is the fa'il.",
      "«o hâlde ders edinin» — fâ CEVABI bağlar (emir meczûm olamaz, fâ zorunlu); cemâat vâvı fâildir.",
      segments=[seg("فَ","fa","conj"), seg("ادْرُسُوا","darasa","verb")]),
  tok("الْقُرْآنَ","quran","noun",[W,"maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the Qur'an» — the object.", "«Kur'ân'ı» — mef'ûl.",
      punct="،")],
 "jumal": [
  J("فَادْرُسُوا الْقُرْآنَ",
    "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَزْمٍ جَوَابُ الشَّرْطِ، مَقْرُونَةٌ بِالْفَاءِ لِأَنَّهَا طَلَبِيَّةٌ.",
    "The jawab: an imperative clause, so it is bound by the fa — one of the seven places the fa is obligatory.",
    "Cevap: emir cümlesi, o yüzden fâ ile bağlanmıştır — fânın vâcib olduğu yedi yerden biri.")]})

S.append({"id": "s9", "translation": {
 "en": "for it is the speech of the Merciful, a refuge from Satan, and a weight in the Balance.» (As the source cites it from Ruh al-Bayan.)",
 "tr": "çünkü o Rahmân'ın kelâmı, şeytandan bir sığınak ve mizanda bir ağırlıktır.» (Kaynağın Rûhu'l-Beyân'dan naklettiği gibi.)"},
 "tokens": [
  tok("فَإِنَّهُ","inna","part",[W,"inna-wa-akhawatuha","lam-taleel"],
      "الْفَاءُ لِلتَّعْلِيلِ، وَإِنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَالْهَاءُ اسْمُهَا فِي مَحَلِّ نَصْبٍ.",
      "«for it» — the fa of reason; the pronoun is inna's ism.",
      "«çünkü o» — ta'lil fâsı; zamir innenin ismi.",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part"), seg("هُ","pron-3ms","pron")]),
  tok("كَلَامُ","kalam","noun",[W,"inna-wa-akhawatuha","idafa-definiteness"],
      "خَبَرُ إِنَّ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«the speech of» — the first khabar.", "«kelâmı» — ilk haber."),
  tok("الرَّحْمٰنِ","rahman","propn",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — يُكْتَبُ بِالْأَلِفِ الْخَنْجَرِيَّةِ.",
      "«the Merciful» — written with the dagger alif, as the source prints.",
      "«Rahmân'ın» — kaynağın bastığı gibi hançer elifle."),
  tok("وَحِرْزٌ","hirz","noun",[W,"atf-nasaq"],
      "مَعْطُوفٌ عَلَى كَلَامُ مَرْفُوعٌ.",
      "«and a refuge» — the second khabar, joined.", "«ve bir sığınak» — ikinci haber, atıfla.",
      segments=[seg("وَ","wa","conj"), seg("حِرْزٌ","hirz","noun")]),
  tok("مِنَ","min","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ — حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«from» — its nun takes a fatha before the article.", "«-den» — nûnu harf-i tariften önce fetha alır."),
  tok("الشَّيْطَانِ","shaytan","noun",[W,"huruf-jarr"],
      "مَجْرُورٌ بِمِنْ.", "«Satan» —", "«şeytan» —"),
  tok("وَرُجْحَانٌ","rujhan","noun",[W,"atf-nasaq","masdar"],
      "مَعْطُوفٌ مَرْفُوعٌ.",
      "«and a weight» — the third khabar.", "«ve bir ağırlık» — üçüncü haber.",
      segments=[seg("وَ","wa","conj"), seg("رُجْحَانٌ","rujhan","noun")]),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("الْمِيزَانِ","mizan","noun",[W,"huruf-jarr","mithal-verbs"],
      "مَجْرُورٌ بِفِي — اسْمُ آلَةٍ عَلَى مِفْعَالٍ، أَصْلُهُ مِوْزَان: قُلِبَتِ الْوَاوُ يَاءً لِسُكُونِهَا بَعْدَ كَسْرَةٍ.",
      "«the Balance» — مِفْعَال from و ز ن: the waw turned ya after the kasra (مِوْزَان → مِيزَان).",
      "«mizan» — و ز ن'den مِفْعَال: vâv kesradan sonra yâ oldu (مِوْزَان → مِيزَان).",
      punct=".")],
 "jumal": [
  J("فَإِنَّهُ كَلَامُ الرَّحْمٰنِ",
    "جُمْلَةٌ اسْمِيَّةٌ مُؤَكَّدَةٌ بِإِنَّ لَا مَحَلَّ لَهَا — تَعْلِيلِيَّةٌ.",
    "The reason for the command, three khabars on one inna: speech, refuge, weight.",
    "Emrin illeti, bir innede üç haber: kelâm, sığınak, ağırlık.")]})

# ----------- s10 — the hanifiyya hadith (as printed)
S.append({"id": "s10", "translation": {
 "en": "«I have brought you the white, upright religion.»",
 "tr": "«Size beyaz Hanîfliği getirdim.»"},
 "tokens": [
  tok("أَتَيْتُكُمْ","ata","verb",[W,"maful-bihi"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ — نَاقِصٌ: أَتَى.",
      "«I have brought you» — a naqis verb wearing its doer and its object.",
      "«size getirdim» — fâilini ve mef'ûlünü taşıyan nâkıs fiil.",
      segments=[seg("أَتَيْتُ","ata","verb"), seg("كُمْ","pron-2mp","pron")]),
  tok("بِالْحَنِيفِيَّةِ","hanifiyya","noun",[W,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِأَتَيْتُ — أَتَى بِهِ: جَاءَ بِهِ.",
      "«the hanifiyya» — the upright faith; أَتَى بِ = brought.",
      "«Hanîfliği» — dosdoğru din; أَتَى بِ = getirdi.",
      segments=[seg("بِ","bi","part"), seg("الْحَنِيفِيَّةِ","hanifiyya","noun")]),
  tok("الْبَيْضَاءِ","bayda","noun",[W,"naat-sifa","mamnu-min-sarf"],
      "صِفَةٌ مَجْرُورَةٌ بِالْكَسْرَةِ — فَعْلَاءُ الْأَلْوَانِ مَمْنُوعَةٌ مِنَ الصَّرْفِ، لَكِنَّ ال تَرُدُّ الْكَسْرَةَ. وَالْبَيَاضُ هُنَا تَخْيِيلٌ: السُّنَّةُ تُتَخَيَّلُ نُورًا.",
      "«white» — the colour فَعْلَاء, a diptote given its kasra back by the article. The WHITENESS is the takhyil: the sunna imagined as light.",
      "«beyaz» — renk فَعْلَاء'sı, gayr-i munsarif; harf-i tarif kesrayı geri verir. BEYAZLIK tahyîldir: sünnet nur olarak tahayyül edilir.",
      punct=".")]})

# ----------- s11 — the darkness of unbelief (as printed)
S.append({"id": "s11", "translation": {
 "en": "«I saw the blackness of unbelief on so-and-so's brow.»",
 "tr": "«Küfrün karalığını falancanın alnında gördüm.»"},
 "tokens": [
  tok("شَاهَدْتُ","shahada-verb","verb",[W,"form-iii-verbs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ فَاعِلٌ — بَابُ الْمُفَاعَلَةِ.",
      "«I saw» — Form III.", "«gördüm» — III. bâb."),
  tok("سَوَادَ","sawad","noun",[W,"maful-bihi","idafa-definiteness"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ — وَالسَّوَادُ تَخْيِيلٌ: الْكُفْرُ يُتَخَيَّلُ ظُلْمَةً.",
      "«the blackness of» — the object; the BLACKNESS is imagined into unbelief.",
      "«karalığını» — mef'ûl; KARALIK küfre hayal edilmiştir."),
  tok("الْكُفْرِ","kufr","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«unbelief» —", "«küfrün» —"),
  tok("مِنْ","min","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«on» —", "«-de» —"),
  tok("جَبِينِ","jabin","noun",[W,"huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِمِنْ وَهُوَ مُضَافٌ.", "«the brow of» —", "«alnında» —"),
  tok("فُلَانٍ","fulan","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«so-and-so» —", "«falancanın» —",
      punct=".")]})

# ----------- s12-s14 — the reasoning (RESTORED)
S.append({"id": "s12", "translation": {
 "en": "When innovation, and everything that is ignorance, makes its owner like one who walks in darkness — (Restored from the source's Turkish.)",
 "tr": "Bid'at ve cehâlet olan her şey, sahibini karanlıkta yürüyen kimse gibi kıldığında — (Kaynağın Türkçesinden geri yazım.)"},
 "tokens": [
  tok("لَمَّا","lamma","part",[W,"maful-fih"],
      "لَمَّا حِينِيَّةٌ — ظَرْفٌ بِمَعْنَى حِينَ، يَلِيهَا الْمَاضِي.",
      "«when» — the لَمَّا of time, followed by a mazi.", "«-dığında» — zaman لَمَّا'sı, ardında mâzî."),
  tok("كَانَتِ","kana","verb",[W,"kana-wa-akhawatuha"],
      "فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ حُرِّكَتْ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«was» — kana; its ta takes a kasra before the article.", "«idi» — kâne; tâsı harf-i tariften önce kesra alır."),
  tok("الْبِدْعَةُ","bida","noun",[W,"kana-wa-akhawatuha"],
      "اسْمُ كَانَ مَرْفُوعٌ.", "«innovation» — kana's ism.", "«bid'at» — kânenin ismi."),
  tok("وَكُلُّ","kull","noun",[W,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى الْبِدْعَةُ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«and every» — joined to the ism, annexed to مَا.", "«ve her» — isme atıf, مَا'ya muzâf.",
      segments=[seg("وَ","wa","conj"), seg("كُلُّ","kull","noun")]),
  tok("مَا","ma-mawsula","pron",[W,"ism-mawsul","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«that which» — the relative in the mudaf-ilayh seat.", "«… şey» — muzâfun ileyh mahallinde mevsûl."),
  tok("هُوَ","huwa","pron",[W,"mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةٌ.",
      "«it is» — the sila's mubtada.", "«o» — sılanın mübtedâsı."),
  tok("جَهْلٌ","jahl","noun",[W,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.", "«ignorance» — its khabar.", "«cehâlet» — haberi."),
  tok("يَجْعَلُ","jaala","verb",[W,"kana-wa-akhawatuha","mafulayn"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ كَانَ فِي مَحَلِّ نَصْبٍ. يَنْصِبُ مَفْعُولَيْنِ.",
      "«makes» — the clause is kana's khabar; جَعَلَ takes TWO objects.",
      "«kılar» — cümle kânenin haberi; جَعَلَ İKİ mef'ûl alır."),
  tok("صَاحِبَهُ","sahib","noun",[W,"mafulayn","idafa-definiteness"],
      "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«its owner» — the first object.", "«sahibini» — ilk mef'ûl.",
      segments=[seg("صَاحِبَ","sahib","noun"), seg("هُ","pron-3ms","pron")]),
  tok("كَمَنْ","man-mawsul","pron",[W,"mafulayn","huruf-jarr","ism-mawsul"],
      "الْكَافُ جَارَّةٌ، وَمَنْ مَوْصُولٌ فِي مَحَلِّ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ ثَانٍ.",
      "«like one who» — the second object, a jarr-phrase in the seat of nasb.",
      "«… kimse gibi» — ikinci mef'ûl, nasb mahallinde câr-mecrûr.",
      segments=[seg("كَ","ka","part"), seg("مَنْ","man-mawsul","pron")]),
  tok("يَمْشِي","masha","verb",[W,"ism-mawsul","ism-maqsur-manqus"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — وَالْجُمْلَةُ صِلَةُ مَنْ.",
      "«walks» — a naqis mudari: raf' estimated on the ya; the sila of مَنْ.",
      "«yürür» — nâkıs muzâri: ref'i yâ üzerinde takdîrî; مَنْ'in sılası."),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("الظُّلْمَةِ","zulma","noun",[W,"huruf-jarr"],
      "مَجْرُورٌ بِفِي.", "«the darkness» —", "«karanlık» —",
      punct="،")]})

S.append({"id": "s13", "translation": {
 "en": "it was likened to darkness. (Restored.)",
 "tr": "karanlığa benzetildi. (Geri yazım.)"},
 "tashbih": {"mushabbah": [], "adat": 0, "bihi": [1], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": None, "bihi": "mufrad", "wajh": None}},
 "tokens": [
  tok("شُبِّهَتْ","shabbaha","verb",[W,A,"naib-al-fail","form-ii-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — الْبِدْعَةُ: الْمُشَبَّهُ.",
      "«it was likened» — the passive of شَبَّهَ; its hidden deputy (the bid'a) is the MUSHABBAH.",
      "«benzetildi» — شَبَّهَ'nin meçhûlü; gizli nâibi (bid'at) MÜŞEBBEHtir."),
  tok("بِالظُّلْمَةِ","zulma","noun",[W,A,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِشُبِّهَتْ — الْمُشَبَّهُ بِهِ.",
      "«to darkness» — the بِ-phrase of شَبَّهَ carries the MUSHABBAH BIHI.",
      "«karanlığa» — شَبَّهَ'nin بِ'li tamlaması MÜŞEBBEHÜN BİHi taşır.",
      punct=".",
      segments=[seg("بِ","bi","part"), seg("الظُّلْمَةِ","zulma","noun")])],
 "jumal": [
  J("شُبِّهَتْ بِالظُّلْمَةِ",
    "جَوَابُ لَمَّا — جُمْلَةٌ فِعْلِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The jawab of لَمَّا: the whole reasoning lands on one passive verb.",
    "لَمَّا'nın cevabı: bütün istidlâl tek bir meçhûl fiile iner.")]})

S.append({"id": "s14", "translation": {
 "en": "And by reversal it followed that the sunna, and everything that is knowledge, be likened to light. (Restored.)",
 "tr": "Aksi yoldan da sünnetin ve ilim olan her şeyin nura benzetilmesi lâzım geldi. (Geri yazım.)"},
 "tashbih": {"mushabbah": [4, 5, 6, 7, 8], "adat": 3, "bihi": [9], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": "murakkab", "bihi": "mufrad", "wajh": None}},
 "tokens": [
  tok("وَبِالْعَكْسِ","aks","noun",[W,"huruf-jarr"],
      "الْوَاوُ عَاطِفَةٌ، وَالْبَاءُ جَارَّةٌ، وَالْعَكْسِ مَجْرُورٌ — حَالٌ.",
      "«and by reversal» —", "«aksi yoldan» —",
      segments=[seg("وَ","wa","conj"), seg("بِ","bi","part"), seg("الْعَكْسِ","aks","noun")]),
  tok("لَزِمَ","lazima","verb",[W,"an-masdariyya"],
      "فِعْلٌ مَاضٍ، وَفَاعِلُهُ الْمَصْدَرُ الْمُؤَوَّلُ بَعْدَهُ.",
      "«it followed» — its fa'il is the أَنْ-clause read as a masdar.", "«lâzım geldi» — fâili, masdara çevrilen أَنْ cümlesi."),
  tok("أَنْ","an-masdariyya","part",[W,"an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ.", "«that» —", "«-mesi» —"),
  tok("تُشَبَّهَ","shabbaha","verb",[W,A,"an-masdariyya","naib-al-fail","form-ii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.",
      "«be likened» — the passive mudari, mansub by أَنْ: the verb of likening as adat.",
      "«benzetilmesi» — meçhûl muzâri, أَنْ ile mansub: edat olan benzetme fiili."),
  tok("السُّنَّةُ","sunna","noun",[W,A,"naib-al-fail"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ — الْمُشَبَّهُ.",
      "«the sunna» — the deputy doer: the MUSHABBAH.", "«sünnet» — nâib-i fâil: MÜŞEBBEH."),
  tok("وَكُلُّ","kull","noun",[W,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى السُّنَّةُ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«and every» —", "«ve her» —",
      segments=[seg("وَ","wa","conj"), seg("كُلُّ","kull","noun")]),
  tok("مَا","ma-mawsula","pron",[W,"ism-mawsul","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«that which» —", "«… şey» —"),
  tok("هُوَ","huwa","pron",[W,"mubtada-khabar"],
      "مُبْتَدَأٌ — وَالْجُمْلَةُ صِلَةٌ.", "«it is» —", "«o» —"),
  tok("عِلْمٌ","ilm","noun",[W,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ.", "«knowledge» —", "«ilim» —"),
  tok("بِالنُّورِ","nur","noun",[W,A,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِتُشَبَّهَ — الْمُشَبَّهُ بِهِ.",
      "«to light» — the MUSHABBAH BIHI on the verb's بِ.", "«nura» — fiilin بِ'sindeki MÜŞEBBEHÜN BİH.",
      punct=".",
      segments=[seg("بِ","bi","part"), seg("النُّورِ","nur","noun")])]})

# ----------- s15 — the saying (as printed)
S.append({"id": "s15", "translation": {
 "en": "Grammar in speech is like salt in food.",
 "tr": "Kelâmda nahiv, yemekte tuz gibidir."},
 "tashbih": {"mushabbah": [0, 1, 2], "adat": 3, "bihi": [3, 4, 5], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": "muqayyad", "bihi": "muqayyad", "wajh": None}},
 "tokens": [
  tok("النَّحْوُ","nahw","noun",[W,A,"mubtada-khabar"],
      "مُبْتَدَأٌ مَرْفُوعٌ — الْمُشَبَّهُ.",
      "«grammar» — the mubtada: the MUSHABBAH.", "«nahiv» — mübtedâ: MÜŞEBBEH."),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("الْكَلَامِ","kalam","noun",[W,"huruf-jarr"],
      "مَجْرُورٌ بِفِي — وَالْجَارُّ وَالْمَجْرُورُ حَالٌ مِنَ النَّحْوِ، فَالْمُشَبَّهُ مُقَيَّدٌ.",
      "«speech» — the restriction on the mushabbah: not grammar, but grammar-in-speech.",
      "«kelâm» — müşebbehin kaydı: nahiv değil, kelâmdaki nahiv."),
  tok("كَالْمِلْحِ","milh","noun",[W,A,"huruf-jarr","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ جَارَّةٌ، وَالْمِلْحِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ؛ الْمُشَبَّهُ بِهِ.",
      "«like salt» — the kaf of likening: the MUSHABBAH BIHI.", "«tuz gibi» — benzetme kâfı: MÜŞEBBEHÜN BİH.",
      segments=[seg("كَ","ka","part"), seg("الْمِلْحِ","milh","noun")]),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("الطَّعَامِ","taam","noun",[W,"huruf-jarr"],
      "مَجْرُورٌ بِفِي — حَالٌ مِنَ الْمِلْحِ، فَالْمُشَبَّهُ بِهِ مُقَيَّدٌ أَيْضًا.",
      "«food» — the restriction on the other end: salt-in-food.", "«yemek» — öteki tarafın kaydı: yemekteki tuz.",
      punct=".")],
 "jumal": [
  J("النَّحْوُ فِي الْكَلَامِ كَالْمِلْحِ فِي الطَّعَامِ",
    "جُمْلَةٌ اسْمِيَّةٌ — تَشْبِيهٌ مُرْسَلٌ مُجْمَلٌ، طَرَفَاهُ مُقَيَّدَانِ.",
    "Both ends are restricted by a jarr-phrase; the adat is spoken, the wajh is not — and WHAT the wajh is, is the khilaf that follows.",
    "İki taraf da câr-mecrûrla kayıtlı; edat söylenmiş, vech söylenmemiş — vechin NE olduğu ise ardından gelen ihtilâftır.")]})

# ----------- s16-s18 — the khilaf (RESTORED)
S.append({"id": "s16", "translation": {
 "en": "Hence the corruption of making the wajh al-shabah in it «that a little of it reforms and much of it spoils» is plain. (Restored.)",
 "tr": "Bundan dolayı ondaki vech-i şebehi «azı ıslah eder, çoğu ifsad eder» diye koymanın fesâdı ortaya çıktı. (Geri yazım.)"},
 "tokens": [
  tok("وَلِهٰذَا","hadha","pron",[W,"huruf-jarr","lam-taleel"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَاللَّامُ لِلتَّعْلِيلِ جَارَّةٌ، وَهٰذَا فِي مَحَلِّ جَرٍّ.",
      "«hence» — the lam of reason over the demonstrative.", "«bundan dolayı» — işaret ismi üstünde ta'lil lâmı.",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","part"), seg("هٰذَا","hadha","pron")]),
  tok("ظَهَرَ","zahara","verb",[W,"fail"],
      "فِعْلٌ مَاضٍ.", "«is plain» — became manifest.", "«ortaya çıktı» —"),
  tok("فَسَادُ","fasad","noun",[W,"fail","idafa-definiteness"],
      "فَاعِلٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.", "«the corruption of» — the fa'il.", "«fesâdı» — fâil."),
  tok("جَعْلِ","jal-making","noun",[W,"idafa-definiteness","masdar","imal-al-masdar"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ جَعَلَ عَامِلٌ عَمَلَ فِعْلِهِ: يَنْصِبُ مَفْعُولَيْنِ.",
      "«making» — a masdar working like its verb: it takes two objects (the wajh, and the clause).",
      "«koymanın» — fiili gibi amel eden masdar: iki mef'ûl alır (vech ve cümle)."),
  tok("وَجْهِ","wajh","noun",[W,"imal-al-masdar","idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَفْعُولُ الْمَصْدَرِ الْأَوَّلُ فِي الْمَعْنَى، وَهُوَ مُضَافٌ.",
      "«the wajh of» — the masdar's first object, in the mudaf-ilayh seat.", "«vechini» — masdarın ilk mef'ûlü, muzâfun ileyh mahallinde."),
  tok("الشَّبَهِ","shabah","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness» —", "«benzerliğin» —"),
  tok("فِيهِ","fi","part",[W,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ — أَيْ: فِي هٰذَا الْقَوْلِ.",
      "«in it» — in this saying.", "«onda» — bu sözde.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("أَنَّ","anna","part",[W,"inna-wa-akhawatuha","imal-al-masdar"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَفْعُولُ الْمَصْدَرِ الثَّانِي.",
      "«that» — its clause is the masdar's second object: what the wajh was made to be.",
      "«… olduğunu» — cümlesi masdarın ikinci mef'ûlü: vech ne yapıldıysa o."),
  tok("قَلِيلَهُ","qalil","noun",[W,"inna-wa-akhawatuha","idafa-definiteness"],
      "اسْمُ أَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«a little of it» — anna's ism.", "«azı» — ennenin ismi.",
      segments=[seg("قَلِيلَ","qalil","noun"), seg("هُ","pron-3ms","pron")]),
  tok("يُصْلِحُ","aslaha","verb",[W,"inna-wa-akhawatuha","form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.",
      "«reforms» — the khabar clause.", "«ıslah eder» — haber cümlesi."),
  tok("وَكَثِيرَهُ","kathir","noun",[W,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى اسْمِ أَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«and much of it» — joined to the ism, in nasb.", "«çoğu» — isme atıf, mansub.",
      segments=[seg("وَ","wa","conj"), seg("كَثِيرَ","kathir","noun"), seg("هُ","pron-3ms","pron")]),
  tok("يُفْسِدُ","afsada","verb",[W,"form-iv-verbs"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — خَبَرُ الْمَعْطُوفِ.",
      "«spoils» — the second khabar.", "«ifsad eder» — ikinci haber.",
      punct=".")]})

S.append({"id": "s17", "translation": {
 "en": "— because grammar admits neither littleness nor muchness, unlike salt. (Restored.)",
 "tr": "— çünkü nahiv, tuzun aksine, azlığı ve çokluğu kabul etmez. (Geri yazım.)"},
 "tokens": [
  tok("لِأَنَّ","anna","part",[W,"lam-taleel","inna-wa-akhawatuha"],
      "اللَّامُ لِلتَّعْلِيلِ جَارَّةٌ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ.",
      "«because» —", "«çünkü» —",
      segments=[seg("لِ","li","part"), seg("أَنَّ","anna","part")]),
  tok("النَّحْوَ","nahw","noun",[W,"inna-wa-akhawatuha"],
      "اسْمُ أَنَّ مَنْصُوبٌ.", "«grammar» — anna's ism.", "«nahiv» — ennenin ismi."),
  tok("لَا","la","part",[W,"inna-wa-akhawatuha"],
      "حَرْفُ نَفْيٍ.", "«not» —", "«-mez» —"),
  tok("يَحْتَمِلُ","ihtamala","verb",[W,"form-viii-verbs","inna-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ — وَالْجُمْلَةُ خَبَرُ أَنَّ.", "«admits» —", "«kabul eder» —"),
  tok("الْقِلَّةَ","qilla","noun",[W,"maful-bihi"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«littleness» —", "«azlığı» —"),
  tok("وَالْكَثْرَةَ","kathra","noun",[W,"atf-nasaq"],
      "مَعْطُوفٌ مَنْصُوبٌ.", "«and muchness» —", "«ve çokluğu» —",
      segments=[seg("وَ","wa","conj"), seg("الْكَثْرَةَ","kathra","noun")]),
  tok("بِخِلَافِ","khilaf","noun",[W,"huruf-jarr","idafa-definiteness"],
      "الْبَاءُ جَارَّةٌ، وَخِلَافِ مَجْرُورٌ وَهُوَ مُضَافٌ — حَالٌ.",
      "«unlike» —", "«aksine» —",
      segments=[seg("بِ","bi","part"), seg("خِلَافِ","khilaf","noun")]),
  tok("الْمِلْحِ","milh","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«salt» —", "«tuzun» —",
      punct=".")]})

S.append({"id": "s18", "translation": {
 "en": "Rather the wajh al-shabah is that its presence is soundness and its absence is corruption. (Restored.)",
 "tr": "Vech-i şebeh şudur ki: onun bulunması salâh, bulunmaması fesâddır. (Geri yazım.)"},
 "tokens": [
  tok("بَلْ","bal","part",[W,"atf-nasaq"],
      "حَرْفُ إِضْرَابٍ — يُبْطِلُ مَا قَبْلَهُ وَيُثْبِتُ مَا بَعْدَهُ.",
      "«rather» — the idrab: cancels the first reading, sets the true one.",
      "«bilakis» — idrâb: ilk okuyuşu kaldırır, doğrusunu koyar."),
  tok("وَجْهُ","wajh","noun",[W,"mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.", "«the wajh of» —", "«vechi» —"),
  tok("الشَّبَهِ","shabah","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness» —", "«benzerliğin» —"),
  tok("أَنَّ","anna","part",[W,"inna-wa-akhawatuha","mubtada-khabar"],
      "حَرْفُ تَوْكِيدٍ وَنَصْبٍ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.",
      "«that» — the أَنَّ-clause, read as a masdar, is the khabar.", "«… olmasıdır» — masdara çevrilen أَنَّ cümlesi haberdir."),
  tok("وُجُودَهُ","wujud","noun",[W,"inna-wa-akhawatuha","idafa-definiteness","masdar"],
      "اسْمُ أَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«its presence» — anna's ism.", "«bulunması» — ennenin ismi.",
      segments=[seg("وُجُودَ","wujud","noun"), seg("هُ","pron-3ms","pron")]),
  tok("صَلَاحٌ","salah","noun",[W,"inna-wa-akhawatuha"],
      "خَبَرُ أَنَّ مَرْفُوعٌ.", "«soundness» — anna's khabar.", "«salâh» — ennenin haberi."),
  tok("وَعَدَمَهُ","adam","noun",[W,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى اسْمِ أَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«and its absence» — a second ism by atf, still in nasb.", "«ve bulunmaması» — atıfla ikinci isim, yine mansub.",
      segments=[seg("وَ","wa","conj"), seg("عَدَمَ","adam","noun"), seg("هُ","pron-3ms","pron")]),
  tok("فَسَادٌ","fasad","noun",[W,"atf-nasaq"],
      "خَبَرٌ لِلْمَعْطُوفِ مَرْفُوعٌ.", "«corruption» — its khabar.", "«fesâd» — haberi.",
      punct=".")],
 "jumal": [
  J("أَنَّ وُجُودَهُ صَلَاحٌ وَعَدَمَهُ فَسَادٌ",
    "مَصْدَرٌ مُؤَوَّلٌ فِي مَحَلِّ رَفْعٍ خَبَرٌ — وَجْهُ الشَّبَهِ هُنَا وَاحِدٌ لَا مُرَكَّبٌ: صِفَةٌ إِضَافِيَّةٌ.",
    "The wajh named: presence-reforms / absence-spoils — ONE relational quality, not a picture.",
    "Vech adlandırıldı: bulunması ıslah / bulunmaması ifsad — resim değil, TEK bir izâfî vasıf.")]})

# ----------- s19-s22 — the divisions of the wajh (matn)
S.append({"id": "s19", "translation": {
 "en": "And it is either not outside the essence of the two — as in likening a garment to another in its species, its genus or its differentia —",
 "tr": "O ya ikisinin mâhiyetinin dışında değildir — bir elbiseyi nev'inde, cinsinde yahut faslında başka bir elbiseye benzetmekte olduğu gibi —"},
 "tashbih": {"mushabbah": [9], "adat": 8, "bihi": [10], "wajh": [11, 12, 13, 14, 15, 16], "kind": "mursal-mufassal",
             "shape": {"mushabbah": "mufrad", "bihi": "mufrad", "wajh": "mufrad"}},
 "tokens": [
  tok("وَهُوَ","huwa","pron",[W,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَهُوَ مُبْتَدَأٌ — عَائِدٌ إِلَى وَجْهِ الشَّبَهِ.",
      "«and it» — the wajh.", "«o» — vech.",
      segments=[seg("وَ","wa","conj"), seg("هُوَ","huwa","pron")]),
  tok("إِمَّا","imma","part",[W,"atf-nasaq"],
      "حَرْفُ تَفْصِيلٍ — لَا بُدَّ لَهُ مِنْ ثَانٍ: أَوْ خَارِجٌ.",
      "«either» — إِمَّا never stands alone: its answer is أَوْ خَارِجٌ two sentences on.",
      "«ya» — إِمَّا tek başına durmaz: cevabı iki cümle sonra أَوْ خَارِجٌ'dur."),
  tok("غَيْرُ","ghayr","noun",[W,"mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.", "«not» — the khabar.", "«değil» — haber."),
  tok("خَارِجٍ","kharij","noun",[W,"idafa-definiteness","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلٍ.", "«outside» —", "«dışında» —"),
  tok("عَنْ","an","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ مُتَعَلِّقٌ بِخَارِجٍ.", "«of» —", "«-den» —"),
  tok("حَقِيقَتِهِمَا","haqiqa","noun",[W,"huruf-jarr","idafa-definiteness","al-muthanna"],
      "مَجْرُورٌ بِعَنْ وَهُوَ مُضَافٌ، وَضَمِيرُ الْمُثَنَّى مُضَافٌ إِلَيْهِ — الطَّرَفَانِ.",
      "«the essence of the two» — the dual pronoun is the two ends.", "«ikisinin mâhiyeti» — tesniye zamiri iki taraftır.",
      segments=[seg("حَقِيقَتِ","haqiqa","noun"), seg("هِمَا","pron-3d","pron")]),
  tok("كَمَا","kama","part",[W,"huruf-jarr"],
      "الْكَافُ جَارَّةٌ وَمَا كَافَّةٌ — كَافُ التَّمْثِيلِ: يُمَثِّلُ لِلْقِسْمِ، وَالْجَارُّ وَالْمَجْرُورُ بَعْدَهَا حَالٌ.",
      "«as» — the kaf of EXAMPLE, not of likening; the tashbih in this sentence lives in the masdar after it.",
      "«… gibi» — benzetme değil ÖRNEK kâfı; bu cümledeki teşbih ardındaki masdardadır.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-kaffa","part")]),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("تَشْبِيهِ","tashbih","noun",[W,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ — مَصْدَرٌ يَعْمَلُ عَمَلَ فِعْلِهِ: مُضَافُهُ إِلَيْهِ مَفْعُولُهُ، وَالْبَاءُ بَعْدَهُ صِلَتُهُ. هُوَ الْأَدَاةُ هُنَا.",
      "«the likening of» — the masdar تَشْبِيه as ADAT: what it annexes is the mushabbah, its بِ-phrase the mushabbah bihi.",
      "«benzetmek» — EDAT olan تَشْبِيه masdarı: muzâfun ileyhi müşebbeh, بِ'li tamlaması müşebbehün bih."),
  tok("ثَوْبٍ","thawb","noun",[W,A,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَفْعُولُ الْمَصْدَرِ فِي الْمَعْنَى: الْمُشَبَّهُ.",
      "«a garment» — the MUSHABBAH.", "«bir elbiseyi» — MÜŞEBBEH."),
  tok("بِآخَرَ","akhar","noun",[W,A,"huruf-jarr","mamnu-min-sarf"],
      "الْبَاءُ جَارَّةٌ، وَآخَرَ مَجْرُورٌ بِالْفَتْحَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ — الْمُشَبَّهُ بِهِ.",
      "«to another» — the MUSHABBAH BIHI; آخَر is a diptote, its jarr a fatha.",
      "«bir başkasına» — MÜŞEBBEHÜN BİH; آخَر gayr-i munsarif, cerri fetha.",
      segments=[seg("بِ","bi","part"), seg("آخَرَ","akhar","noun")]),
  tok("فِي","fi","part",[W,A,"huruf-jarr"],
      "حَرْفُ جَرٍّ — وَمَا بَعْدَهُ وَجْهُ الشَّبَهِ.",
      "«in» — the فِي that names the WAJH.", "«-de» — VECHİ adlandıran فِي."),
  tok("نَوْعِهِ","naw","noun",[W,A,"huruf-jarr","idafa-definiteness"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ — وَجْهُ الشَّبَهِ الْأَوَّلُ: مِنْ حَقِيقَتِهِمَا.",
      "«its species» — the wajh: a meaning INSIDE the two essences.", "«nev'inde» — vech: iki mâhiyetin İÇİNDEN bir mânâ.",
      segments=[seg("نَوْعِ","naw","noun"), seg("هِ","pron-3ms","pron")]),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«yahut» —"),
  tok("جِنْسِهِ","jins","noun",[W,A,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ وَهُوَ مُضَافٌ.", "«its genus» —", "«cinsinde» —",
      segments=[seg("جِنْسِ","jins","noun"), seg("هِ","pron-3ms","pron")]),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«yahut» —"),
  tok("فَصْلِهِ","fasl","noun",[W,A,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ وَهُوَ مُضَافٌ — وَالْعَطْفُ بِأَوْ: وَجْهٌ وَاحِدٌ مِنْ ثَلَاثَةٍ لَا ثَلَاثَةٌ مَعًا.",
      "«its differentia» — joined by أَوْ: ONE wajh out of three, not three at once — so the wajh stays single.",
      "«faslında» — أَوْ ile atıf: üçten BİR vech, üçü birden değil — vech tek kalır.",
      punct="،",
      segments=[seg("فَصْلِ","fasl","noun"), seg("هِ","pron-3ms","pron")])]})

S.append({"id": "s20", "translation": {
 "en": "or outside them: a real quality, sensed — like the bodily qualities — or of the mind — like the qualities of the soul —",
 "tr": "yahut ikisinin dışındadır: hakikî bir vasıf, hissî — cismânî keyfiyetler gibi — yahut aklî — nefsânî keyfiyetler gibi —"},
 "tokens": [
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ — جَوَابُ إِمَّا.", "«or» — the answer of إِمَّا.", "«yahut» — إِمَّا'nın cevabı."),
  tok("خَارِجٌ","kharij","noun",[W,"atf-nasaq","ism-fail"],
      "مَعْطُوفٌ عَلَى غَيْرُ مَرْفُوعٌ.", "«outside» —", "«dışında» —"),
  tok("عَنْهُمَا","an","part",[W,"huruf-jarr","al-muthanna"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِخَارِجٍ.", "«them» — the two ends.", "«ikisinin» — iki taraf.",
      punct=":",
      segments=[seg("عَنْ","an","part"), seg("هُمَا","pron-3d","pron")]),
  tok("صِفَةٌ","sifa","noun",[W,"mubtada-khabar"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُوَ صِفَةٌ — أَوْ بَدَلٌ مِنْ خَارِجٌ.",
      "«a quality» — «it is a quality», or a badal of «outside».", "«bir vasıf» — «o bir vasıftır», yahut «dışında»dan bedel."),
  tok("حَقِيقِيَّةٌ","haqiqi","noun",[W,"naat-sifa","ism-mansub"],
      "صِفَةٌ مَرْفُوعَةٌ — نِسْبَةٌ إِلَى الْحَقِيقَةِ.", "«real» — a nisba na't.", "«hakikî» — nisbet sıfatı."),
  tok("حِسِّيَّةٌ","hissi","noun",[W,"naat-sifa","ism-mansub"],
      "صِفَةٌ ثَانِيَةٌ مَرْفُوعَةٌ — نِسْبَةٌ إِلَى الْحِسِّ.", "«sensed» — the second na't.", "«hissî» — ikinci sıfat."),
  tok("كَالْكَيْفِيَّاتِ","kayfiyya","noun",[W,"huruf-jarr","jam-muannath-salim"],
      "الْكَافُ لِلتَّمْثِيلِ جَارَّةٌ، وَالْكَيْفِيَّاتِ مَجْرُورٌ بِالْكَسْرَةِ — جَمْعُ مُؤَنَّثٍ سَالِمٌ. لَيْسَتْ كَافَ تَشْبِيهٍ.",
      "«like the qualities» — the kaf of EXAMPLE over a sound feminine plural; no likening is made here.",
      "«keyfiyetler gibi» — cem-i müennes-i sâlim üstünde ÖRNEK kâfı; burada benzetme yapılmıyor.",
      segments=[seg("كَ","ka","part"), seg("الْكَيْفِيَّاتِ","kayfiyya","noun")]),
  tok("الْجِسْمَانِيَّةِ","jismani","noun",[W,"naat-sifa","ism-mansub"],
      "صِفَةٌ مَجْرُورَةٌ — نِسْبَةٌ إِلَى الْجِسْمِ بِزِيَادَةِ الْأَلِفِ وَالنُّونِ.",
      "«bodily» — a nisba with the added alif-nun (جِسْم → جِسْمَانِيّ).", "«cismânî» — elif-nûn ekli nisbet (جِسْم → جِسْمَانِيّ)."),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«yahut» —"),
  tok("عَقْلِيَّةٌ","aqli","noun",[W,"atf-nasaq","ism-mansub"],
      "مَعْطُوفٌ عَلَى حِسِّيَّةٌ مَرْفُوعٌ.", "«of the mind» —", "«aklî» —"),
  tok("كَالْكَيْفِيَّاتِ","kayfiyya","noun",[W,"huruf-jarr","jam-muannath-salim"],
      "كَافُ التَّمْثِيلِ وَمَجْرُورُهَا.", "«like the qualities» —", "«keyfiyetler gibi» —",
      segments=[seg("كَ","ka","part"), seg("الْكَيْفِيَّاتِ","kayfiyya","noun")]),
  tok("النَّفْسَانِيَّةِ","nafsani","noun",[W,"naat-sifa","ism-mansub"],
      "صِفَةٌ مَجْرُورَةٌ — نِسْبَةٌ إِلَى النَّفْسِ بِالْأَلِفِ وَالنُّونِ.",
      "«of the soul» —", "«nefsânî» —",
      punct="،")]})

S.append({"id": "s21", "translation": {
 "en": "or relational — like the removing of the veil, in likening the proof to the sun.",
 "tr": "yahut izâfî — hücceti güneşe benzetmekte perdeyi kaldırmak gibi."},
 "tashbih": {"mushabbah": [6], "adat": 5, "bihi": [7], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": "mufrad", "bihi": "mufrad", "wajh": None}},
 "tokens": [
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«yahut» —"),
  tok("إِضَافِيَّةٌ","idafi","noun",[W,"atf-nasaq","ism-mansub"],
      "مَعْطُوفٌ عَلَى حَقِيقِيَّةٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى الْإِضَافَةِ: صِفَةٌ لَا تُعْقَلُ إِلَّا بِالْقِيَاسِ إِلَى غَيْرِهَا.",
      "«relational» — a quality understood only by relation to something else.",
      "«izâfî» — ancak başkasına nisbetle anlaşılan vasıf."),
  tok("كَإِزَالَةِ","izala","noun",[W,"huruf-jarr","idafa-definiteness","masdar"],
      "كَافُ التَّمْثِيلِ جَارَّةٌ، وَإِزَالَةِ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرُ أَزَالَ.",
      "«like the removing of» — the kaf of example again; the masdar of أَزَالَ.",
      "«kaldırmak gibi» — yine örnek kâfı; أَزَالَ'nin masdarı.",
      segments=[seg("كَ","ka","part"), seg("إِزَالَةِ","izala","noun")]),
  tok("الْحِجَابِ","hijab","noun",[W,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the veil» —", "«perdeyi» —"),
  tok("فِي","fi","part",[W,"huruf-jarr"],
      "حَرْفُ جَرٍّ.", "«in» —", "«-de» —"),
  tok("تَشْبِيهِ","tashbih","noun",[W,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "مَجْرُورٌ بِفِي وَهُوَ مُضَافٌ — الْمَصْدَرُ الْعَامِلُ: أَدَاةُ التَّشْبِيهِ.",
      "«the likening of» — the working masdar, the ADAT.", "«benzetmek» — amel eden masdar, EDAT."),
  tok("الْحُجَّةِ","hujja","noun",[W,A,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«the proof» — the MUSHABBAH.", "«hücceti» — MÜŞEBBEH."),
  tok("بِالشَّمْسِ","shams","noun",[W,A,"huruf-jarr"],
      "الْبَاءُ جَارَّةٌ، وَالشَّمْسِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ؛ وَالْوَجْهُ إِزَالَةُ الْحِجَابِ: صِفَةٌ إِضَافِيَّةٌ.",
      "«to the sun» — the MUSHABBAH BIHI; the wajh (removing the veil) is relational: neither the proof nor the sun IS a removing.",
      "«güneşe» — MÜŞEBBEHÜN BİH; vech (perdeyi kaldırmak) izâfîdir: ne hüccet ne güneş bir kaldırmadır.",
      punct=".",
      segments=[seg("بِ","bi","part"), seg("الشَّمْسِ","shams","noun")])]})

S.append({"id": "s22", "translation": {
 "en": "And also: it is either one, or as good as one, or several, or composite.",
 "tr": "Ve yine: o ya birdir, ya bir hükmündedir, ya müteaddiddir, ya mürekkebdir."},
 "tokens": [
  tok("وَأَيْضًا","aydan","noun",[W,"maful-mutlaq"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَأَيْضًا مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: آضَ يَئِيضُ أَيْضًا — أَيْ: رَجَعَ.",
      "«and also» — a masdar as maf'ul mutlaq of a dropped verb (آضَ = returned): «returning to the matter…».",
      "«ve yine» — hazfedilmiş fiilin mef'ûl-i mutlakı olan masdar (آضَ = döndü): «konuya dönersek…».",
      segments=[seg("وَ","wa","conj"), seg("أَيْضًا","aydan","noun")]),
  tok("إِمَّا","imma","part",[W,"atf-nasaq"],
      "حَرْفُ تَفْصِيلٍ.", "«either» —", "«ya» —"),
  tok("وَاحِدٌ","wahid","noun",[W,"mubtada-khabar"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُوَ وَاحِدٌ.", "«one» — «it is one».", "«bir» — «o birdir»."),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«ya» —"),
  tok("بِمَنْزِلَتِهِ","manzila","noun",[W,"huruf-jarr","idafa-definiteness"],
      "الْبَاءُ جَارَّةٌ، وَمَنْزِلَتِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَالْجَارُّ وَالْمَجْرُورُ مَعْطُوفٌ عَلَى وَاحِدٌ.",
      "«or as good as one» — several meanings that count as one.", "«ya bir hükmünde» — bir sayılan birkaç mânâ.",
      segments=[seg("بِ","bi","part"), seg("مَنْزِلَتِ","manzila","noun"), seg("هِ","pron-3ms","pron")]),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«ya» —"),
  tok("مُتَعَدِّدٌ","mutaaddid","noun",[W,"atf-nasaq","ism-fail"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ تَعَدَّدَ.", "«several» —", "«müteaddid» —"),
  tok("أَوْ","aw","conj",[W,"atf-nasaq"],
      "حَرْفُ عَطْفٍ.", "«or» —", "«ya» —"),
  tok("مُرَكَّبٌ","murakkab","noun",[W,"atf-nasaq","ism-maful"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ مِنْ رَكَّبَ: الْهَيْئَةُ الَّتِي رَأَيْنَاهَا فِي بَيْتِ النُّجُومِ.",
      "«composite» — the ism maf'ul of رَكَّبَ: the hay'a we met in the bayt of the stars.",
      "«mürekkeb» — رَكَّبَ'nin ism-i mef'ûlü: yıldızlar beytinde gördüğümüz hey'et.",
      punct=".")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "tahqiq": g("تَحْقِيق", "ح ق ق", "noun", "verification, reality (masdar of حَقَّقَ); tahqiqan: really", "tahkîk, gerçeklik (حَقَّقَ'nin masdarı); tahkîkan: gerçekten", 5),
 "takhyil": g("تَخْيِيل", "خ ي ل", "noun", "imagination, imagining (masdar of خَيَّلَ)", "tahyîl, hayal ettirme (خَيَّلَ'nin masdarı)", 5),
 "najm": g("نَجْم", "ن ج م", "noun", "star", "yıldız", 1, plural="نُجُوم"),
 "duja": g("دُجًى", "د ج و", "noun", "darkness of night (maqsur)", "gece karanlığı (maksûr)", 5),
 "ibtida": g("ابْتِدَاع", "ب د ع", "noun", "innovating, an innovation (masdar of ابْتَدَعَ)", "bid'at çıkarma (ابْتَدَعَ'nin masdarı)", 5),
 "haya-shape": g("هَيْئَة", "ه ي أ", "noun", "shape, configuration; a composite picture (hay'a)", "hey'et, şekil; birleşik tablo", 4, plural="هَيْئَات"),
 "hasil": g("حَاصِل", "ح ص ل", "noun", "arising, resulting (ism fa'il of حَصَلَ)", "hâsıl olan (حَصَلَ'nin ism-i fâili)", 3),
 "husul": g("حُصُول", "ح ص ل", "noun", "arising, coming about (masdar)", "husûl, meydana gelme (masdar)", 4),
 "mushriq": g("مُشْرِق", "ش ر ق", "noun", "shining, bright (ism fa'il of أَشْرَقَ)", "parlak, ışıldayan (أَشْرَقَ'nin ism-i fâili)", 4),
 "bid-white": g("بِيض", "ب ي ض", "noun", "white (adjective; pl. of أَبْيَض — the damma turned kasra for the ya)", "beyazlar (أَبْيَض'ın cem'i; yâ için damme kesraya döndü)", 4),
 "muzlim": g("مُظْلِم", "ظ ل م", "noun", "dark (ism fa'il of أَظْلَمَ)", "karanlık (أَظْلَمَ'nin ism-i fâili)", 3),
 "aswad": g("أَسْوَد", "س و د", "noun", "black (adjective; the colour-أَفْعَل; diptote)", "siyah (renk أَفْعَل'i; gayr-i munsarif)", 2),
 "aysh": g("عَيْش", "ع ي ش", "noun", "life, living", "yaşayış, hayat", 2),
 "shahid-martyr": g("شَهِيد", "ش ه د", "noun", "martyr; witness", "şehid; şahit", 2, plural="شُهَدَاء"),
 "hashr": g("حَشْر", "ح ش ر", "noun", "the Gathering (of the resurrection); masdar of حَشَرَ", "haşir; حَشَرَ'nin masdarı", 3),
 "zill": g("ظِلّ", "ظ ل ل", "noun", "shade, shadow", "gölge", 2, plural="ظِلَال"),
 "harur": g("حَرُور", "ح ر ر", "noun", "scorching heat, hot wind", "kavurucu sıcak, sam yeli", 5),
 "dalalah-error": g("ضَلَالَة", "ض ل ل", "noun", "error, going astray", "dalâlet, sapıklık", 3),
 "hirz": g("حِرْز", "ح ر ز", "noun", "refuge, safeguard, amulet", "sığınak, koruyucu", 4),
 "mizan": g("مِيزَان", "و ز ن", "noun", "balance, scales (ism ala: مِوْزَان → مِيزَان)", "mizan, terazi (ism-i âlet: مِوْزَان → مِيزَان)", 3, plural="مَوَازِين"),
 "hanifiyya": g("حَنِيفِيَّة", "ح ن ف", "noun", "the hanifiyya — the upright faith of Ibrahim (nisba)", "Hanîflik — İbrahim'in dosdoğru dini (nisbet)", 5),
 "bayda": g("بَيْضَاء", "ب ي ض", "noun", "white (adjective; feminine of أَبْيَض; diptote)", "beyaz (أَبْيَض'ın müennesi; gayr-i munsarif)", 3),
 "sawad": g("سَوَاد", "س و د", "noun", "blackness", "karalık, siyahlık", 3),
 "jabin": g("جَبِين", "ج ب ن", "noun", "brow, forehead", "alın", 3),
 "bida": g("بِدْعَة", "ب د ع", "noun", "innovation (in religion), bid'a", "bid'at", 3, plural="بِدَع"),
 "zulma": g("ظُلْمَة", "ظ ل م", "noun", "darkness", "karanlık", 2, plural="ظُلُمَات"),
 "aks": g("عَكْس", "ع ك س", "noun", "reverse, opposite; bi-l-aks: conversely", "aks, tersi; bi'l-aks: aksine", 3),
 "milh": g("مِلْح", "م ل ح", "noun", "salt", "tuz", 1),
 "jal-making": g("جَعْل", "ج ع ل", "noun", "making, setting (masdar of جَعَلَ)", "kılma, koyma (جَعَلَ'nin masdarı)", 3),
 "haqiqi": g("حَقِيقِيّ", "ح ق ق", "noun", "real, actual (nisba)", "hakikî (nisbet)", 3),
 "hissi": g("حِسِّيّ", "ح س س", "noun", "sensory, of the senses (nisba)", "hissî, duyuya ait (nisbet)", 4),
 "kayfiyya": g("كَيْفِيَّة", "ك ي ف", "noun", "quality, how-ness (nisba to كَيْفَ)", "keyfiyet, nitelik (كَيْفَ'ye nisbet)", 4, plural="كَيْفِيَّات"),
 "jismani": g("جِسْمَانِيّ", "ج س م", "noun", "bodily (nisba with alif-nun)", "cismânî (elif-nûnlu nisbet)", 4),
 "nafsani": g("نَفْسَانِيّ", "ن ف س", "noun", "of the soul, psychic (nisba with alif-nun)", "nefsânî (elif-nûnlu nisbet)", 4),
 "idafi": g("إِضَافِيّ", "ض ي ف", "noun", "relational, relative (nisba to إِضَافَة)", "izâfî, nisbî (إِضَافَة'ye nisbet)", 4),
 "izala": g("إِزَالَة", "ز و ل", "noun", "removing (masdar of أَزَالَ)", "izâle, kaldırma (أَزَالَ'nin masdarı)", 4),
 "hijab": g("حِجَاب", "ح ج ب", "noun", "veil, screen", "perde, hicab", 3, plural="حُجُب"),
 "aydan": g("أَيْضًا", "أ ي ض", "noun", "also, likewise (a masdar as maf'ul mutlaq)", "yine, dahi (mef'ûl-i mutlak olan masdar)", 2),
 "mutaaddid": g("مُتَعَدِّد", "ع د د", "noun", "several, multiple (ism fa'il of تَعَدَّدَ)", "müteaddid, birden çok (تَعَدَّدَ'nin ism-i fâili)", 4),
 "murakkab": g("مُرَكَّب", "ر ك ب", "noun", "composite, compound (ism maf'ul of رَكَّبَ)", "mürekkeb, birleşik (رَكَّبَ'nin ism-i mef'ûlü)", 4),
 "ma-masdariyya": g("مَا (الْمَصْدَرِيَّة)", None, "part", "ma that turns its clause into a masdar", "cümlesini masdara çeviren mâ", 4),
 "ma-kaffa": g("مَا (الْكَافَّة)", None, "part", "the ma that stops a governor from governing (كَمَا)", "âmili amelden alıkoyan mâ (كَمَا)", 4),
 "man-mawsul": g("مَنْ (الْمَوْصُولَة)", None, "pron", "who, the one who (relative)", "… olan kimse (mevsûl)", 3),
 "ishtaraka": g("اِشْتَرَكَ", "ش ر ك", "verb", "to share, take part in (Form VIII)", "ortak olmak, iştirak etmek (VIII. bâb)", 4, form="VIII"),
 "shahada-verb": g("شَاهَدَ", "ش ه د", "verb", "to witness, see (Form III)", "müşâhede etmek, görmek (III. bâb)", 3, form="III"),
 "shabbaha": g("شَبَّهَ", "ش ب ه", "verb", "to liken (Form II); شَبَّهَ X بِY", "benzetmek (II. bâb); شَبَّهَ X بِY", 3, form="II"),
 "aslaha": g("أَصْلَحَ", "ص ل ح", "verb", "to reform, put right (Form IV)", "ıslah etmek, düzeltmek (IV. bâb)", 3, form="IV"),
 "afsada": g("أَفْسَدَ", "ف س د", "verb", "to spoil, corrupt (Form IV)", "ifsad etmek, bozmak (IV. bâb)", 3, form="IV"),
 "masha": g("مَشَى", "م ش ي", "verb", "to walk", "yürümek", 1, form="I"),
 "awwal": copy_gloss("aqaid-ahl-al-sunna", "awwal"),
 "thani": copy_gloss("mukhtasar-al-manar", "thani"),
 "sunna": copy_gloss("mukhtasar-al-manar", "sunna"),
 "said": copy_gloss("aqaid-ahl-al-sunna", "said"),
 "mawt": copy_gloss("bad-al-amali", "mawt"),
 "najat": copy_gloss("aqaid-ahl-al-sunna", "najat"),
 "quran": copy_gloss("mukhtasar-al-manar", "quran"),
 "rujhan": copy_gloss("bad-al-amali", "rujhan"),
 "kufr": copy_gloss("aqaid-ahl-al-sunna", "kufr"),
 "sahib": copy_gloss("wasiyyat-abi-hanifa-samti", "sahib"),
 "nahw": copy_gloss("bad-al-amali", "nahw"),
 "qalil": copy_gloss("aqaid-ahl-al-sunna", "qalil"),
 "wujud": copy_gloss("aqaid-ahl-al-sunna", "wujud"),
 "salah": copy_gloss("wasiyyat-abi-hanifa-samti", "salah"),
 "adam": copy_gloss("aqaid-ahl-al-sunna", "adam"),
 "naw": copy_gloss("kitab-al-sulh", "naw"),
 "jins": copy_gloss("kitab-al-sulh", "jins"),
 "sifa": copy_gloss("mukhtasar-al-manar", "sifa"),
 "hujja": copy_gloss("mukhtasar-al-manar", "hujja"),
 "bal": copy_gloss("kitab-al-waqf", "bal"),
 "lamma": copy_gloss("wasiyyat-abi-hanifa-samti", "lamma"),
 "kama": copy_gloss("wasiyyat-abi-hanifa-samti", "kama"),
 "rahman": copy_gloss("wasiyyat-abi-hanifa-samti", "rahman"),
 "arada": copy_gloss("aqaid-ahl-al-sunna", "arada"),
 "darasa": copy_gloss("jumal-al-tadrib", "darasa"),
 "laha-verb": copy_gloss("bad-al-amali", "laha-verb"),
 "lazima": copy_gloss("mukhtasar-al-manar", "lazima"),
 "in-shartiyya": copy_gloss("aqaid-ahl-al-sunna", "in-shartiyya") if "in-shartiyya" in json.loads((ROOT / "content/samples/aqaid-ahl-al-sunna/glossary.json").read_text(encoding="utf-8"))["entries"] else g("إِنْ (الشَّرْطِيَّة)", None, "part", "if (conditional)", "eğer (şart)", 3),
 "an-masdariyya": copy_gloss("mukhtasar-al-manar", "an-masdariyya") if "an-masdariyya" in json.loads((ROOT / "content/samples/mukhtasar-al-manar/glossary.json").read_text(encoding="utf-8"))["entries"] else g("أَنْ (الْمَصْدَرِيَّة)", None, "part", "that (turns its verb into a masdar)", "-mesi (fiili masdara çevirir)", 3),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/47.json").write_text(
    json.dumps({"chapter": 47, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 47 for c in man["chapters"]):
    man["chapters"].append({"n": 47, "title": TITLE47})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.47.0"
ADD_EN = (" Chapter 47 (lines ~3028-3080, sahifa 105-106) carries the wajh al-shabah: s1 the definition, "
          "s4 Abu l-Qasim's bayt (split at the hemistich), s7-s9 the hadith the source cites from Ruh "
          "al-Bayan (vol. 7 p. 346) split at its clauses, s10-s11 the two sayings, s15 the النَّحْوُ "
          "كَالْمِلْحِ saying, and s19-s22 the divisions of the wajh are Arabic as the source prints it "
          "(the source writes اْلقُرْاٰنَ and الرَّحْمٰنِ with the dagger alif; the app keeps الرَّحْمٰنِ "
          "and writes الْقُرْآنَ in the standard imla — the one divergence). s2-s3, s5-s6, s12-s14 and "
          "s16-s18 are RESTORATIONS, not quotations: the source carries those steps only in "
          "Ottoman-Turkish paraphrase, and the Arabic restores the matn's own wording (فَالْأَوَّلُ كَمَا "
          "مَرَّ، وَالثَّانِي كَقَوْلِهِ؛ الْهَيْئَةُ الْحَاصِلَةُ…؛ لَمَّا كَانَتِ الْبِدْعَةُ…؛ ظَهَرَ فَسَادُ جَعْلِ "
          "وَجْهِ الشَّبَهِ…؛ بَلْ وَجْهُ الشَّبَهِ أَنَّ وُجُودَهُ صَلَاحٌ وَعَدَمَهُ فَسَادٌ) in the musannif's "
          "register; each is marked «restored» in its translation. Every likening carries an authored "
          "`tashbih` frame — arkan, kind and the shapes of its ends — the engine is tested against; the "
          "kaf of exemplification (كَقَوْلِهِ، كَمَا، كَالْكَيْفِيَّاتِ) is authored as NO likening.")
ADD_TR = (" Kırk yedinci bâb (satır ~3028-3080, sahife 105-106) vech-i şebehi taşır: s1 tarif, s4 Ebü'l-"
          "Kāsım'ın beyti (mısra başından bölünmüş), s7-s9 kaynağın Rûhu'l-Beyân'dan (c. 7, s. 346) "
          "naklettiği hadis cümlelerinden bölünmüş, s10-s11 iki söz, s15 النَّحْوُ كَالْمِلْحِ sözü ve "
          "s19-s22 vechin kısımları kaynağın bastığı Arapçadır (kaynak اْلقُرْاٰنَ ve الرَّحْمٰنِ'i hançer "
          "elifle yazar; uygulama الرَّحْمٰنِ'i korur, الْقُرْآنَ'ı standart imlâyla yazar — tek fark). "
          "s2-s3, s5-s6, s12-s14 ve s16-s18 ALINTI DEĞİL GERİ YAZIMDIR: kaynak o adımları yalnız "
          "Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın kendi ifadesini musannifin üslûbunda geri "
          "yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Her benzetme, motorun "
          "sınandığı müellif eliyle yazılmış bir `tashbih` çerçevesi taşır — rükünler, nev' ve tarafların "
          "şekilleri; örnek kâfı (كَقَوْلِهِ، كَمَا، كَالْكَيْفِيَّاتِ) benzetme DEĞİL diye yazılmıştır.")
if "3028-3080" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
# the key rule: never OVERWRITE an entry the package already owns, and never mint a key
# another package owns under a different word
other = {}
for p in (ROOT / "content/samples").iterdir():
    if p.name == PKG.name or not (p / "glossary.json").exists(): continue
    for k, v in json.loads((p / "glossary.json").read_text(encoding="utf-8"))["entries"].items():
        other.setdefault(k, set()).add(bare(v["lemma"]).split(" ")[0])
for k, v in GLOSS_ADD.items():
    if k in gl["entries"]:
        assert bare(gl["entries"][k]["lemma"]) == bare(v["lemma"]), f"key {k} already means {gl['entries'][k]['lemma']}"
        continue
    if k in other:
        assert bare(v["lemma"]).split(" ")[0] in other[k], f"key {k} means something else elsewhere: {other[k]}"
    gl["entries"][k] = v
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- morphology
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
V = mo["verbs"]
if "ishtaraka" not in V:
    V["ishtaraka"] = _sg.derived(_sg.B8, _sg.W8, "َ", "اِشْتَرَك", "شْتَرِك", "اِشْتَرِك",
                                 "اِشْتِرَاك", "مُشْتَرِك", "مُشْتَرَك", "اُشْتُرِكَ", "يُشْتَرَكُ")
if "shahada-verb" not in V:
    V["shahada-verb"] = _sg.derived(_sg.B3, _sg.W3, "ُ", "شَاهَد", "شَاهِد", "شَاهِد",
                                    "مُشَاهَدَة", "مُشَاهِد", "مُشَاهَد", "شُوهِدَ", "يُشَاهَدُ")
if "shabbaha" not in V:
    V["shabbaha"] = _sg.derived(_sg.B2, _sg.W2, "ُ", "شَبَّه", "شَبِّه", "شَبِّه",
                                "تَشْبِيه", "مُشَبِّه", "مُشَبَّه", "شُبِّهَ", "يُشَبَّهُ")
if "aslaha" not in V:
    V["aslaha"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَصْلَح", "صْلِح", "أَصْلِح",
                              "إِصْلَاح", "مُصْلِح", "مُصْلَح", "أُصْلِحَ", "يُصْلَحُ")
if "afsada" not in V:
    V["afsada"] = _sg.derived(_sg.B4, _sg.W4, "ُ", "أَفْسَد", "فْسِد", "أَفْسِد",
                              "إِفْسَاد", "مُفْسِد", "مُفْسَد", "أُفْسِدَ", "يُفْسَدُ")
if "masha" not in V:
    V["masha"] = _sg.naqis1("daraba", "نَاقِصٌ يَائِيٌّ", "y", "مَشَ", "مْش", "i", "اِمْش",
                            "مَشْي", "مَاشٍ (الْمَاشِي)", None, None, None,
                            "نَاقِصٌ يَائِيٌّ لَازِمٌ: لَمْ يَمْشِ.")
for key, pkg in (("arada", "aqaid-ahl-al-sunna"), ("darasa", "jumal-al-tadrib"),
                 ("laha-verb", "bad-al-amali"), ("lazima", "mukhtasar-al-manar")):
    if key not in V: V[key] = copy_morph(pkg, key)
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 152
GR = ROOT / "content/grammar"
NOTE152 = {
 "id": "wajh-al-shabah",
 "title": {"ar": "وَجْهُ الشَّبَهِ — تَحْقِيقُهُ وَتَخْيِيلُهُ وَأَقْسَامُهُ",
           "en": "The wajh al-shabah — real or imagined, and its divisions",
           "tr": "Vech-i şebeh — tahkîkî mi tahyîlî mi, ve kısımları"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — وجه الشبه"],
 "question": {
  "en": ["What do the two ends SHARE? That is the wajh — and it may be truly in both (tahqiqi) or put into the second by imagination alone (takhyili).",
         "Is the shared meaning part of what the two things ARE (a garment like a garment), or a quality outside them — sensed, of the mind, or relational?",
         "Is it ONE meaning, several, or a whole PICTURE (a hay'a) drawn from several? Only the last makes the tashbih murakkab."],
  "tr": ["İki taraf NEYİ paylaşıyor? O vechtir — ikisinde gerçekten bulunabilir (tahkîkî) yahut ikincisine yalnız hayalle konmuş olabilir (tahyîlî).",
         "Ortak mânâ, iki şeyin NE OLDUĞUNUN bir parçası mı (elbise gibi elbise), yoksa dışlarında bir vasıf mı — hissî, aklî, izâfî?",
         "TEK bir mânâ mı, birkaç mı, yoksa birkaçından çıkan bütün bir TABLO mu (hey'et)? Yalnız sonuncusu teşbihi mürekkeb yapar."]},
 "plain": {
  "en": "The wajh is what the two ends share. It can be real in both (a cheek and a rose are both red) or only imagined into the second (stars amid the dark as sunnas among bid'as). It may be one quality, several, or a whole picture; the engine reads its shape from the syntax and leaves real-or-imagined to the reader.",
  "tr": "Vech, iki tarafın paylaştığı şeydir. İkisinde de gerçek olabilir (yanak da gül de kızıldır) yahut yalnız ikincisine hayal edilmiş (karanlıktaki yıldızlar, bid'atler arasındaki sünnetler). Bir vasıf, birkaç vasıf yahut bir tablo olabilir; motor şeklini söz diziminden okur, gerçek mi hayal mi sorusunu okuyucuya bırakır."},
 "explanation": {
  "en": "The matn: وَجْهُ الشَّبَهِ مَا يَشْتَرِكَانِ فِيهِ تَحْقِيقًا أَوْ تَخْيِيلًا — «what the two share in, really or by imagination». TAHQIQI is the case already met (خَدُّهُ كَالْوَرْدِ: redness is in the cheek and in the rose). TAKHYILI is Abu l-Qasim's bayt: وَكَأَنَّ النُّجُومَ بَيْنَ دُجَاهَا سُنَنٌ لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ — the wajh is the HAY'A of bright white things scattered around a dark black thing, and that picture is not IN sunnas-among-bid'as except by imagination: because bid'a and every ignorance make their owner like one walking in darkness, bid'a was first likened to darkness; by reversal sunna and every knowledge to light — whence أَتَيْتُكُمْ بِالْحَنِيفِيَّةِ الْبَيْضَاءِ and شَاهَدْتُ سَوَادَ الْكُفْرِ مِنْ جَبِينِ فُلَانٍ — and only then could stars-among-dark be sunnas-among-bid'as, like white hairs in black, or flowers in green grass. The wajh must be SHARED by both ends: hence the corruption of reading النَّحْوُ فِي الْكَلَامِ كَالْمِلْحِ فِي الطَّعَامِ as «a little reforms, much spoils» — grammar admits neither little nor much; the wajh is «its presence is soundness and its absence corruption». DIVISIONS: the wajh is either NOT OUTSIDE the two essences (a garment likened to another in species, genus or differentia) or OUTSIDE them — a real quality that is sensed (colours, shapes, sizes; sounds strong and weak; tastes, smells; heat, cold, hardness, softness…) or of the mind (intelligence, knowledge, anger, forbearance…) — or a RELATIONAL quality (the removing of a veil, in likening the proof to the sun). And again: ONE, or as good as one, or SEVERAL, or COMPOSITE. The engine (TashbihEngine) claims what the syntax settles — whether each end is mufrad, muqayyad (with a jarr-phrase or zarf on it: النَّحْوُ فِي الْكَلَامِ) or murakkab (a noun with the clause that describes it: سُنَنٌ لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ), and whether a spoken wajh is one thing or a hay'a — and offers tahqiq/takhyil and the inside/outside/relational sorting as a shortlist, because those are knowledge of the two THINGS, not of the sentence.",
  "tr": "Matn: وَجْهُ الشَّبَهِ مَا يَشْتَرِكَانِ فِيهِ تَحْقِيقًا أَوْ تَخْيِيلًا — «ikisinin, gerçekten yahut hayal yoluyla, kendisinde ortak olduğu şey». TAHKÎKÎ, zaten görülen hâldir (خَدُّهُ كَالْوَرْدِ: kızıllık yanakta da gülde de vardır). TAHYÎLÎ, Ebü'l-Kāsım'ın beytidir: وَكَأَنَّ النُّجُومَ بَيْنَ دُجَاهَا سُنَنٌ لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ — vech, siyah karanlık bir şeyin etrafına saçılmış beyaz parlak şeylerin HEY'ETİdir ve bu tablo bid'atler-arası-sünnetlerde hayalden başka yolla YOKTUR: bid'at ve her cehâlet sahibini karanlıkta yürüyen gibi kıldığından bid'at önce karanlığa benzetildi; aksi yolla sünnet ve her ilim nura — أَتَيْتُكُمْ بِالْحَنِيفِيَّةِ الْبَيْضَاءِ ve شَاهَدْتُ سَوَادَ الْكُفْرِ مِنْ جَبِينِ فُلَانٍ buradandır — ancak ondan sonra karanlıktaki yıldızlar bid'atler arasındaki sünnetler olabildi; siyah saçtaki ak teller, yeşil çimendeki çiçekler gibi. Vech iki tarafta ORTAK olmalıdır: bu yüzden النَّحْوُ فِي الْكَلَامِ كَالْمِلْحِ فِي الطَّعَامِ'ı «azı ıslah, çoğu ifsad» diye okumak fâsittir — nahiv az-çok kabul etmez; vech «bulunması salâh, bulunmaması fesâd»tır. KISIMLAR: vech ya iki mâhiyetin DIŞINDA DEĞİLDİR (bir elbisenin nev'inde, cinsinde, faslında başka elbiseye benzetilmesi) ya DIŞINDADIR — hissî hakikî bir vasıf (renkler, şekiller, ölçüler; kuvvetli ve zayıf sesler; tatlar, kokular; sıcaklık, soğukluk, sertlik, yumuşaklık…) yahut aklî (zekâ, ilim, gazap, hilm…) — yahut İZÂFÎ bir vasıftır (hüccetin güneşe benzetilmesinde perdeyi kaldırmak). Ve yine: TEK, yahut bir hükmünde, yahut MÜTEADDİD, yahut MÜREKKEB. Motor (TashbihEngine) söz diziminin kestiğini iddia eder — her tarafın müfred mi, mukayyed mi (üstünde câr-mecrûr yahut zarf: النَّحْوُ فِي الْكَلَامِ), mürekkeb mi (kendisini vasfeden cümleyle isim: سُنَنٌ لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ) olduğunu ve söylenen vechin tek şey mi hey'et mi olduğunu — tahkîk/tahyîl ile iç/dış/izâfî tasnifini ise kısa liste olarak sunar; çünkü onlar cümlenin değil iki ŞEYİN bilgisidir."},
 "examples": [
  {"ar": "وَجْهُ الشَّبَهِ مَا يَشْتَرِكَانِ فِيهِ تَحْقِيقًا أَوْ تَخْيِيلًا",
   "en": "the definition.", "tr": "tarif.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "وَكَأَنَّ النُّجُومَ بَيْنَ دُجَاهَا سُنَنٌ لَاحَ بَيْنَهُنَّ ابْتِدَاعٌ",
   "en": "takhyili: a composite bihi, a muqayyad mushabbah.", "tr": "tahyîlî: mürekkeb bih, mukayyed müşebbeh.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "النَّحْوُ فِي الْكَلَامِ كَالْمِلْحِ فِي الطَّعَامِ",
   "en": "both ends muqayyad; the wajh shared, or the tashbih fails.", "tr": "iki taraf mukayyed; vech ortak olmalı, yoksa teşbih düşer.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s15"},
  {"ar": "كَإِزَالَةِ الْحِجَابِ فِي تَشْبِيهِ الْحُجَّةِ بِالشَّمْسِ",
   "en": "a relational wajh; the masdar تَشْبِيه as adat.", "tr": "izâfî vech; edat olan تَشْبِيه masdarı.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s21"}],
 "commonMistakes": [
  {"wrong": "«Kelâmda nahiv yemekteki tuz gibidir: azı ıslah, çoğu ifsad eder»",
   "right": "«Vech: nahvin bulunması salâh, bulunmaması fesâddır»",
   "why": {"en": "The wajh must be in BOTH ends. Salt can be too little or too much; grammar cannot — so a wajh built on quantity is not shared, and a tashbih whose wajh is not shared is no tashbih.",
           "tr": "Vech İKİ tarafta olmalıdır. Tuz az da çok da olabilir; nahiv olamaz — nicelik üstüne kurulan vech ortak değildir ve vechi ortak olmayan teşbih teşbih değildir."}},
  {"wrong": "«كَإِزَالَةِ الْحِجَابِ bir teşbihtir: izâfî vasıf perdeyi kaldırmaya benzetilmiştir»",
   "right": "«Bu kâf örnek kâfıdır (كَافُ التَّمْثِيلِ); cümledeki teşbih تَشْبِيهِ الْحُجَّةِ بِالشَّمْسِ masdarındadır»",
   "why": {"en": "Two kafs, one letter: the kaf that likens and the kaf that says «for instance». In a list of categories (أَوْ إِضَافِيَّةٌ كَ…) the kaf gives an example; the engine refuses a likening there and reads the masdar instead.",
           "tr": "İki kâf, tek harf: benzeten kâf ile «meselâ» diyen kâf. Kısımlar listesinde (أَوْ إِضَافِيَّةٌ كَ…) kâf örnek verir; motor orada benzetmeyi reddeder ve masdarı okur."}}],
 "relatedNotes": ["arkan-al-tashbih", "ilm-al-bayan", "tashbih", "istiara", "inna-wa-akhawatuha", "jumla-sifa", "afal-khamsa", "mamnu-min-sarf", "imal-al-masdar", "in-shartiyya"]}
(GR / "wajh-al-shabah.json").write_text(json.dumps(NOTE152, ensure_ascii=False, indent=1), encoding="utf-8")
NOTE153 = {
 "id": "jam-taksir",
 "title": {"ar": "جَمْعُ التَّكْسِيرِ", "en": "The broken plural", "tr": "Cem-i teksîr (kırık çoğul)"},
 "level": 3, "group": "sarf",
 "classicalSources": ["الكافية — الجمع", "البناء"],
 "question": {
  "en": ["Does the plural keep the singular's letters whole and add ـُونَ / ـَات — or does it BREAK the singular's shape (نَجْم → نُجُوم، سُنَّة → سُنَن، شَيْء → أَشْيَاء)?",
         "Which pattern did it break into? The patterns are heard from the Arabs (samaʿi), not derived — the app stores each plural on its glossary entry.",
         "Does the broken plural decline like a singular (نُجُومٌ، نُجُومًا، نُجُومٍ), or is it a صِيغَةُ مُنْتَهَى الْجُمُوعِ (جَوَانِب، مَسَاجِد) barred from tanwin?"],
  "tr": ["Çoğul, tekilin harflerini bütün bırakıp ـُونَ / ـَات mı ekler — yoksa tekilin şeklini KIRAR mı (نَجْم → نُجُوم، سُنَّة → سُنَن، شَيْء → أَشْيَاء)?",
         "Hangi kalıba kırıldı? Kalıplar Araptan işitilir (semâî), türetilmez — uygulama her çoğulu sözlük maddesinde saklar.",
         "Kırık çoğul tekil gibi mi çekilir (نُجُومٌ، نُجُومًا، نُجُومٍ), yoksa tenvin almayan bir صِيغَةُ مُنْتَهَى الْجُمُوعِ mü (جَوَانِب، مَسَاجِد)?"]},
 "plain": {
  "en": "A sound plural adds an ending and leaves the word whole; a BROKEN plural changes the word's inner shape. Which broken pattern a noun takes is heard, not derived, so the app stores it — and the plural then declines like any singular, unless it is one of the heaviest patterns, which refuse tanwin.",
  "tr": "Sâlim çoğul bir ek koyar, kelimeyi bütün bırakır; KIRIK çoğul kelimenin iç şeklini değiştirir. Bir ismin hangi kırık kalıbı aldığı işitilir, türetilmez; uygulama onu saklar — çoğul sonra her tekil gibi çekilir; en ağır kalıplar hariç, onlar tenvin almaz."},
 "explanation": {
  "en": "The sound plurals (جَمْعُ الْمُذَكَّرِ السَّالِمُ, جَمْعُ الْمُؤَنَّثِ السَّالِمُ) keep the singular intact and add an ending. جَمْعُ التَّكْسِيرِ breaks the singular: by changing vowels only (أَسَد → أُسْد), by adding letters (نَجْم → نُجُوم، شَيْء → أَشْيَاء), by dropping them (سُنَّة → سُنَن، شَهِيد → شُهَدَاء changes both), or all at once. The patterns are many — فُعُول، أَفْعَال، فُعَل، فُعَلَاء، فَوَاعِل، مَفَاعِل — and which one a given noun takes is SAMAʿI: the books list them, the dictionaries record them, and no rule predicts نُجُوم rather than أَنْجُم from نَجْم alone. That is why the app stores every plural on its glossary entry instead of deriving it. In iʿrab a broken plural is treated as a SINGULAR word: it takes the three vowels and the tanwin (نُجُومٌ، سُنَنًا، أَشْيَاءَ → the last is a diptote, see below). Two families refuse tanwin: صِيغَةُ مُنْتَهَى الْجُمُوعِ — a plural on فَوَاعِل / مَفَاعِل / أَفَاعِيل (جَوَانِب، مَسَاجِد، مَفَاتِيح) — and the فُعَلَاء / أَفْعِلَاء plurals ending in the alif of femininity (سُعَدَاء، شُهَدَاء); and أَشْيَاء, alone of its shape, is barred too. A diptote plural in the mudaf-ilayh seat shows a fatha for its jarr (حُصُولِ أَشْيَاءَ) — but the ARTICLE or an IDAFA gives the kasra back (فِي جَوَانِبِ شَيْءٍ، السُّعَدَاءِ). Agreement: a broken plural of non-rational things is treated as feminine singular (نُجُومٌ لَامِعَةٌ), which is the doctrine the analyzer's agreement rules follow.",
  "tr": "Sâlim çoğullar (جَمْعُ الْمُذَكَّرِ السَّالِمُ, جَمْعُ الْمُؤَنَّثِ السَّالِمُ) tekili bozmadan bir ek koyar. جَمْعُ التَّكْسِيرِ tekili kırar: yalnız harekeyi değiştirerek (أَسَد → أُسْد), harf ekleyerek (نَجْم → نُجُوم، شَيْء → أَشْيَاء), harf düşürerek (سُنَّة → سُنَن; شَهِيد → شُهَدَاء ikisini birden) yahut hepsini birden. Kalıplar çoktur — فُعُول، أَفْعَال، فُعَل، فُعَلَاء، فَوَاعِل، مَفَاعِل — ve bir ismin hangisini aldığı SEMÂÎDİR: kitaplar sayar, sözlükler kaydeder; نَجْم'den tek başına نُجُوم'u değil أَنْجُم'u hiçbir kural kestiremez. Bu yüzden uygulama her çoğulu türetmek yerine sözlük maddesinde saklar. İ'râbda kırık çoğul TEKİL bir kelime gibi işlem görür: üç harekeyi ve tenvini alır (نُجُومٌ، سُنَنًا؛ أَشْيَاءَ ise gayr-i munsariftir, aşağıda). İki aile tenvin almaz: صِيغَةُ مُنْتَهَى الْجُمُوعِ — فَوَاعِل / مَفَاعِل / أَفَاعِيل üzerine çoğul (جَوَانِب، مَسَاجِد، مَفَاتِيح) — ve te'nis elifiyle biten فُعَلَاء / أَفْعِلَاء çoğulları (سُعَدَاء، شُهَدَاء); أَشْيَاء da kendi şeklinde tek başına yasaklıdır. Muzâfun ileyh mevkiinde gayr-i munsarif çoğul cerrini fethayla gösterir (حُصُولِ أَشْيَاءَ) — fakat HARF-İ TARİF yahut İZÂFET kesrayı geri verir (فِي جَوَانِبِ شَيْءٍ، السُّعَدَاءِ). Uyum: akılsızların kırık çoğulu müennes tekil sayılır (نُجُومٌ لَامِعَةٌ); tahlilcinin uyum kuralları bu doktrini izler."},
 "examples": [
  {"ar": "وَكَأَنَّ النُّجُومَ بَيْنَ دُجَاهَا سُنَنٌ", "en": "فُعُول and فُعَل: two broken plurals in one hemistich.", "tr": "فُعُول ve فُعَل: bir mısrada iki kırık çoğul.", "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "مِنْ حُصُولِ أَشْيَاءَ مُشْرِقَةٍ بِيضٍ فِي جَوَانِبِ شَيْءٍ", "en": "أَشْيَاءَ a diptote in jarr by fatha; جَوَانِبِ given its kasra back by the idafa.", "tr": "أَشْيَاءَ fethayla mecrur gayr-i munsarif; جَوَانِبِ izâfetle kesrasını geri almış.", "sourceStory": "talkhis-al-miftah", "sentence": "s5"},
  {"ar": "عَيْشَ السُّعَدَاءِ وَمَوْتَ الشُّهَدَاءِ", "en": "فُعَلَاء with the alif of femininity — the article restores the kasra.", "tr": "Te'nis elifli فُعَلَاء — harf-i tarif kesrayı geri verir.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"}],
 "commonMistakes": [
  {"wrong": "«نَجْم'ün çoğulu نَجْمُونَ'dur»",
   "right": "«نَجْم'ün çoğulu نُجُوم'dur — kırık çoğul; sâlim çoğul yalnız akıllı müzekkerin sıfatları ve alemleri içindir»",
   "why": {"en": "The sound masculine plural is for rational males (participles, adjectives, names); a thing-noun breaks. The pattern it breaks into is heard, and the glossary stores it.", "tr": "Cem-i müzekker-i sâlim akıllı müzekkerler içindir (ism-i fâiller, sıfatlar, alemler); eşya isimleri kırılır. Kırıldığı kalıp işitilir, sözlük onu saklar."}}],
 "relatedNotes": ["jam-mudhakkar-salim", "jam-muannath-salim", "mamnu-min-sarf", "al-muthanna", "idafa-definiteness"]}
NOTE154 = {
 "id": "ism-mansub",
 "title": {"ar": "الِاسْمُ الْمَنْسُوبُ — يَاءُ النِّسْبَةِ", "en": "The nisba — the noun of relation", "tr": "İsm-i mensûb — nisbet yâsı"},
 "level": 3, "group": "sarf",
 "classicalSources": ["الكافية — النسبة", "البناء"],
 "question": {
  "en": ["Does the word end in a DOUBLED YA with a kasra before it (حَقِيقِيّ، حِسِّيّ، عَقْلِيّ)? Then it is a noun made to RELATE to what stands before the ya.",
         "What fell before the ya was added — a ta marbuta (حَقِيقَة → حَقِيقِيّ), a maqsur alif (دُنْيَا → دُنْيَوِيّ), a mamdud hamza (سَمَاء → سَمَاوِيّ)?",
         "Did an alif and nun ride in (جِسْم → جِسْمَانِيّ، نَفْس → نَفْسَانِيّ، رَبّ → رَبَّانِيّ)? That is the nisba of intensity, heard on a few words."],
  "tr": ["Kelime, önünde kesra olan ŞEDDELİ bir YÂ ile mi bitiyor (حَقِيقِيّ، حِسِّيّ، عَقْلِيّ)? Öyleyse yâdan öncekine NİSBET edilmiş bir isimdir.",
         "Yâ eklenmeden önce ne düştü — tâ-i merbûta (حَقِيقَة → حَقِيقِيّ), maksûr elifi (دُنْيَا → دُنْيَوِيّ), memdûd hemzesi (سَمَاء → سَمَاوِيّ)?",
         "Araya elif-nûn mu girdi (جِسْم → جِسْمَانِيّ، نَفْس → نَفْسَانِيّ، رَبّ → رَبَّانِيّ)? O, birkaç kelimede işitilen mübâlağa nisbetidir."]},
 "plain": {
  "en": "Add a doubled ya (with a kasra before it) to a noun and you get a word that means «belonging to it, of it»: حَقِيقَة → حَقِيقِيّ. The ta drops first; a final alif or hamza turns waw; a few words take an extra alif-nun. It declines like any adjective and agrees like one.",
  "tr": "Bir isme (önünde kesra olan) şeddeli bir yâ ekleyin: «ona ait, ondan» demek olan bir kelime çıkar: حَقِيقَة → حَقِيقِيّ. Önce tâ düşer; sondaki elif yahut hemze vâva döner; birkaç kelime fazladan elif-nûn alır. Her sıfat gibi çekilir ve uyar."},
 "explanation": {
  "en": "The nisba (النَّسَب) is a derivation of the Bina: a noun is made to RELATE to another by a doubled ya with a kasra before it — مِصْر → مِصْرِيّ، عَقْل → عَقْلِيّ، حِسّ → حِسِّيّ. Rules the books give and the Ism lab computes: (1) a ta marbuta is dropped first (مَكَّة → مَكِّيّ، حَقِيقَة → حَقِيقِيّ، كَيْفِيَّة is itself a nisba-noun built on كَيْفَ); (2) a maqsur's alif and a mamdud's hamza turn WAW (دُنْيَا → دُنْيَوِيّ، سَمَاء → سَمَاوِيّ); (3) a handful are heard, not derived — مَدِينَة → مَدَنِيّ، قُرَيْش → قُرَشِيّ — and the engine keeps them in a table that answers before any rule; (4) the alif-nun nisba (جِسْمَانِيّ، نَفْسَانِيّ، رُوحَانِيّ، رَبَّانِيّ) adds intensity and is likewise heard. The nisba is an ADJECTIVE: it takes the feminine ta (حَقِيقِيَّة، حِسِّيَّة), the sound plurals (حِسِّيُّونَ، كَيْفِيَّات), and full iʿrab — in the Talkhis's list صِفَةٌ حَقِيقِيَّةٌ حِسِّيَّةٌ the nisbas are na'ts in raf' after their head. Read backwards, the doubled ya is a receipt: a word ending ِيّ is never a verb cell and never the speaker's ya — the analyzer refuses both readings on it.",
  "tr": "Nisbet (النَّسَب) Binâ'nın bir türetmesidir: bir isim, önünde kesra olan şeddeli bir yâ ile başka bir şeye NİSBET edilir — مِصْر → مِصْرِيّ، عَقْل → عَقْلِيّ، حِسّ → حِسِّيّ. Kitapların verdiği ve Nisbe lâboratuvarının hesapladığı kurallar: (1) tâ-i merbûta önce düşer (مَكَّة → مَكِّيّ، حَقِيقَة → حَقِيقِيّ; كَيْفِيَّة kendisi كَيْفَ üstüne kurulmuş nisbet ismidir); (2) maksûrun elifi ve memdûdun hemzesi VÂVA döner (دُنْيَا → دُنْيَوِيّ، سَمَاء → سَمَاوِيّ); (3) birkaçı türetilmez, işitilir — مَدِينَة → مَدَنِيّ، قُرَيْش → قُرَشِيّ — motor onları her kuraldan önce cevap veren bir tabloda tutar; (4) elif-nûnlu nisbet (جِسْمَانِيّ، نَفْسَانِيّ، رُوحَانِيّ، رَبَّانِيّ) mübâlağa katar ve yine işitilir. Nisbet bir SIFATTIR: müennes tâsını alır (حَقِيقِيَّة، حِسِّيَّة), sâlim çoğulları alır (حِسِّيُّونَ، كَيْفِيَّات) ve tam i'râb alır — Telhîs'in listesinde صِفَةٌ حَقِيقِيَّةٌ حِسِّيَّةٌ nisbetler mevsûfundan sonra merfû sıfatlardır. Tersinden okununca şeddeli yâ bir makbuzdur: ِيّ ile biten kelime ne fiil hanesidir ne mütekellim yâsı taşır — tahlilci ikisini de reddeder."},
 "examples": [
  {"ar": "صِفَةٌ حَقِيقِيَّةٌ حِسِّيَّةٌ كَالْكَيْفِيَّاتِ الْجِسْمَانِيَّةِ أَوْ عَقْلِيَّةٌ", "en": "five nisbas in one line: the ta dropped, the alif-nun kind, the feminine and the sound plural.", "tr": "bir satırda beş nisbet: düşen tâ, elif-nûnlu tür, müennes ve sâlim çoğul.", "sourceStory": "talkhis-al-miftah", "sentence": "s20"},
  {"ar": "أَوْ إِضَافِيَّةٌ", "en": "a nisba to إِضَافَة: the ta of the base dropped, the ta of the feminine added after the ya.", "tr": "إِضَافَة'ye nisbet: kökün tâsı düşmüş, yâdan sonra müennes tâsı gelmiş.", "sourceStory": "talkhis-al-miftah", "sentence": "s21"}],
 "commonMistakes": [
  {"wrong": "«حَقِيقَتِيّ»",
   "right": "«حَقِيقِيّ — tâ-i merbûta nisbetten önce düşer»",
   "why": {"en": "The ta marbuta is an ending, not part of the stem: it goes before the ya is added. مَكِّيّ, not مَكَّتِيّ.", "tr": "Tâ-i merbûta sondur, gövdeden değildir: yâ eklenmeden düşer. مَكِّيّ, مَكَّتِيّ değil."}}],
 "relatedNotes": ["naat-sifa", "jam-muannath-salim", "jam-mudhakkar-salim", "sifa-mushabbaha", "ism-maqsur-manqus", "ism-mamdud"]}
for n in (NOTE153, NOTE154):
    (GR / f"{n['id']}.json").write_text(json.dumps(n, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch47:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + ishtaraka/shahada-verb/shabbaha/aslaha/afsada/masha (+arada/darasa/laha-verb/lazima copied); note 152;",
      "frames:", sum(1 for x in S if x.get("tashbih")))
