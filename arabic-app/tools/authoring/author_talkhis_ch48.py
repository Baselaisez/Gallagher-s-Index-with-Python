# -*- coding: utf-8 -*-
"""Author chapter 48 of talkhis-al-miftah — أَقْسَامُ وَجْهِ الشَّبَهِ: THE SEVEN KINDS
(sahifa 107-110, lines ~3080-3200): the wajh as one, several or composite,
each sensory or of the mind; the seven kinds counted; the six bayts and the
aya the source hangs on them; the composite wajh drawn from the WHOLE bayt;
and the wajh drawn from opposition by tamlih or tahakkum.

  s1-s6   the divisions and the first two kinds — RESTORED from the source's
          Turkish paraphrase (marked in every translation).
  s7      Abu Qays's bayt وَقَدْ لَاحَ فِي الصُّبْحِ الثُّرَيَّا … — as printed.
  s8      the wajh of s7 — RESTORED (the source paraphrases it in Turkish).
  s9      Bashshar's كَأَنَّ مُثَارَ النَّقْعِ … — as printed (the source writes
          رُؤُسِنَا; the app writes رُؤُوسِنَا, the standard imla).
  s10     Ibn al-Muʿtazz's صَبَّ عَلَيْهِ قَانِصٌ … — as printed, the rhyme sukun on
          غَفَلْ / الْأَشَلْ kept.
  s11     Ibn al-Muʿtazz's وَكَأَنَّ الْبَرْقَ مُصْحَفُ قَارٍ … — as printed.
  s12     al-Mutanabbi's يُقْعِي جُلُوسَ الْبَدَوِيِّ … — as printed (the source
          writes تُجْدَلِْ with a kasra and a sukun together; the app keeps the
          kasra of the rhyme).
  s13     the aya 62:5 مَثَلُ الَّذِينَ حُمِّلُوا التَّوْرَاةَ … — as printed (the
          source writes التَّوْرٰيةَ with the dagger alif; the app writes
          التَّوْرَاةَ).
  s14     its wajh and ends — RESTORED.
  s15-s16 the two bayts لَقَدْ أَطْمَعَتْنِي … / كَمَا أَبْرَقَتْ … — as printed.
  s17     the rule of the whole bayt — RESTORED.
  s18-s21 the three several kinds and the wajh from opposition — RESTORED.
  s22     the two sayings مَا أَشْبَهَهُ بِالْأَسَدِ and هُوَ حَاتِمٌ — as printed
          (the source spells the name خَاتِمٌ; the app writes حَاتِمٌ — Hatim
          al-Ta'i, whom the source's own gloss names).

Every likening carries an AUTHORED `tashbih` frame the TashbihEngine must read
back: the arkan by token index, the kind, the SHAPES — and, new in this
chapter, the spoken wajh's shape as ONE (mufrad), SEVERAL (mutaaddid) or a
PICTURE (murakkab), and the maf'ul-mutlaq frame with no adat (يُقْعِي جُلُوسَ
الْبَدَوِيِّ). The kaf after a category term (فَالْوَاحِدُ الْحِسِّيُّ كَالْحُمْرَةِ) is
authored as NO likening.

Grammar this chapter teaches: note `aqsam-wajh-al-shabah` (group bayan);
the ta'ajjub مَا أَشْبَهَهُ; the maf'ul mutlaq standing for the adat; the
annexed dual with its pronoun (طَرَفَاهُ); the manqus in idafa (مُصْحَفُ قَارٍ)
and with the article (الْمُصْطَلِي); the rhyme sukun; the geminate صَبَّ;
paradigms نَوَّرَ، تَهَاوَى، صَبَّ، غَفَلَ، أَقْعَى، جَدَلَ، حَمَّلَ، أَطْمَعَ، أَعْرَضَ،
تَوَلَّى، أَبْرَقَ، أَقْشَعَ، اِنْتَزَعَ; تَجَلَّى، أَشْبَهَ copied.
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
def frame(mush, adat, bihi, wajh, kind, sm, sb, sw, **extra):
    f = {"mushabbah": mush, "adat": adat, "bihi": bihi, "wajh": wajh, "kind": kind,
         "shape": {"mushabbah": sm, "bihi": sb, "wajh": sw}}
    f.update(extra); return f
S = []
W = "wajh-al-shabah"; Q = "aqsam-wajh-al-shabah"; A = "arkan-al-tashbih"
R_EN = " (Restored: the source carries this step only in Turkish.)"
R_TR = " (Geri yazım: kaynak bu adımı yalnız Türkçe taşır.)"

TITLE48 = {"ar": "أَقْسَامُ وَجْهِ الشَّبَهِ: الْوَاحِدُ وَالْمُرَكَّبُ وَالْمُتَعَدِّدُ، حِسِّيًّا وَعَقْلِيًّا",
           "en": "The Kinds of the Wajh al-Shabah: One, Composite and Several — Sensory and of the Mind",
           "tr": "Vech-i Şebehin Kısımları: Vâhid, Mürekkeb ve Müteaddid — Hissî ve Aklî"}

# ----------- s1 — each kind is sensory or of the mind (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "And each of them is either sensory or of the mind." + R_EN,
 "tr": "Ve bunların her biri ya hissîdir ya aklî." + R_TR},
 "tokens": [
  tok("وَكُلٌّ","kull","noun",[Q,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكُلٌّ مُبْتَدَأٌ مَرْفُوعٌ — وَالتَّنْوِينُ عِوَضٌ عَنِ الْمُضَافِ إِلَيْهِ.",
      "«and each» — the mubtada; its tanwin stands in for a dropped mudaf ilayh (each ONE of them).",
      "«ve her biri» — mübtedâ; tenvini düşen muzâfun ileyhin ivazıdır (onlardan HER BİRİ).",
      segments=[seg("وَ","wa","conj"), seg("كُلٌّ","kull","noun")]),
  tok("مِنْهَا","min","part",[Q,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ صِفَةٌ لِكُلٍّ — وَالْهَاءُ عَائِدٌ إِلَى الْأَقْسَامِ.",
      "«of them» — a jarr-phrase describing كُلّ; the ha points back to the kinds (one, composite, several).",
      "«onlardan» — كُلّ'ü vasfeden câr-mecrûr; hâ, kısımlara döner (vâhid, mürekkeb, müteaddid).",
      segments=[seg("مِنْ","min","part"), seg("هَا","pron-3fs","pron")]),
  tok("إِمَّا","imma","part",[Q,"atf-nasaq"],
      "حَرْفُ تَفْصِيلٍ.",
      "«either» — the particle of division; its partner وَإِمَّا follows.",
      "«ya» — taksim edatı; eşi وَإِمَّا arkasından gelir."),
  tok("حِسِّيٌّ","hissi","noun",[Q,"mubtada-khabar","ism-mansub"],
      "خَبَرٌ مَرْفُوعٌ — اسْمٌ مَنْسُوبٌ إِلَى الْحِسِّ.",
      "«sensory» — the khabar; a nisba to الْحِسّ: perceived by one of the five senses.",
      "«hissî» — haber; الْحِسّ'e nisbet: beş duyudan biriyle idrak edilen."),
  tok("وَإِمَّا","imma","part",[Q,"atf-nasaq"],
      "الْوَاوُ عَاطِفَةٌ وَإِمَّا حَرْفُ تَفْصِيلٍ.",
      "«or» — the waw joins, إِمَّا divides again.",
      "«ya da» — vâv atfeder, إِمَّا yine böler.",
      segments=[seg("وَ","wa","conj"), seg("إِمَّا","imma","part")]),
  tok("عَقْلِيٌّ","aqli","noun",[Q,"atf-nasaq","ism-mansub"],
      "مَعْطُوفٌ عَلَى حِسِّيٌّ مَرْفُوعٌ — اسْمٌ مَنْسُوبٌ إِلَى الْعَقْلِ.",
      "«of the mind» — joined to حِسِّيٌّ; a nisba to الْعَقْل: grasped by reason, not sensed.",
      "«aklî» — حِسِّيٌّ'ye atıf; الْعَقْل'e nisbet: duyuyla değil akılla kavranan.",
      punct=".")]})

# ----------- s2 — the several may be MIXED (RESTORED)
S.append({"id": "s2", "translation": {
 "en": "And the several may be mixed." + R_EN,
 "tr": "Müteaddid olan, muhtelif (karışık) da olabilir." + R_TR},
 "tokens": [
  tok("وَالْمُتَعَدِّدُ","mutaaddid","noun",[Q,"mubtada-khabar","ism-fail"],
      "الْوَاوُ عَاطِفَةٌ، وَالْمُتَعَدِّدُ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and the several» — the mubtada: the wajh that is more than one quality.",
      "«ve müteaddid» — mübtedâ: birden çok vasıf olan vech.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَعَدِّدُ","mutaaddid","noun")]),
  tok("قَدْ","qad","part",[Q,"qad-harf"],
      "حَرْفُ تَقْلِيلٍ — قَدْ مَعَ الْمُضَارِعِ.",
      "«may» — قَدْ with a mudari: sometimes.",
      "«bazen» — muzâriyle قَدْ: taklîl."),
  tok("يَكُونُ","kana","verb",[Q,"kana-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَرْفُوعٌ، وَاسْمُهُ ضَمِيرٌ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ الْمُبْتَدَأِ.",
      "«is» — the defective verb; its ism is hidden (it); the clause is the mubtada's khabar.",
      "«olur» — nâkıs fiil; ismi gizli zamir (o); cümle mübtedânın haberi."),
  tok("مُخْتَلِفًا","mukhtalif","noun",[Q,"kana-wa-akhawatuha","ism-fail"],
      "خَبَرُ يَكُونُ مَنْصُوبٌ — أَيْ: بَعْضُهُ حِسِّيٌّ وَبَعْضُهُ عَقْلِيٌّ.",
      "«mixed» — the khabar of يَكُونُ: some of its qualities sensory, some of the mind.",
      "«muhtelif» — يَكُونُ'nun haberi: vasıflarının kimi hissî, kimi aklî.",
      punct=".")],
 "jumal": [J("قَدْ يَكُونُ مُخْتَلِفًا", "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ خَبَرُ الْمُبْتَدَأِ.",
             "The verbal clause is the khabar of الْمُتَعَدِّدُ.", "Fiil cümlesi الْمُتَعَدِّدُ'nun haberidir.")]})

# ----------- s3 — the seven kinds counted (RESTORED)
S.append({"id": "s3", "translation": {
 "en": "So the wajh al-shabah is of seven kinds: one and sensory, one and of the mind, composite and sensory, composite and of the mind, several and sensory, several and of the mind, several and mixed." + R_EN,
 "tr": "Öyleyse vech-i şebeh yedi kısımdır: vâhid hissî, vâhid aklî, mürekkeb hissî, mürekkeb aklî, müteaddid hissî, müteaddid aklî, müteaddid muhtelif." + R_TR},
 "tokens": [
  tok("فَوَجْهُ","wajh","noun",[Q,"mubtada-khabar","idafa-definiteness"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَوَجْهُ مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«so the face of» — the fa draws the result; the mubtada, a mudaf.",
      "«öyleyse … yüzü» — fâ neticeyi çıkarır; mübtedâ, muzâf.",
      segments=[seg("فَ","fa","conj"), seg("وَجْهُ","wajh","noun")]),
  tok("الشَّبَهِ","shabah","noun",[Q,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness» — the mudaf ilayh.", "«benzerliğin» — muzâfun ileyh."),
  tok("سَبْعَةُ","saba-seven","noun",[Q,"mubtada-khabar","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — الْعَدَدُ مِنْ ثَلَاثَةٍ إِلَى عَشَرَةٍ يُضَافُ إِلَى جَمْعٍ مَجْرُورٍ.",
      "«seven» — the khabar, annexed: the numbers three to ten take a PLURAL mudaf ilayh in jarr.",
      "«yedi» — haber, muzâf: üçten ona kadar sayılar mecrur bir ÇOĞULA muzâf olur."),
  tok("أَقْسَامٍ","aqsam","noun",[Q,"idafa-definiteness","jam-taksir"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ قِسْمٍ عَلَى أَفْعَالٍ.",
      "«kinds» — the counted noun in jarr; the broken plural أَفْعَال of قِسْم.",
      "«kısım» — sayılan isim, mecrur; قِسْم'in أَفْعَال kalıbında kırık çoğulu.",
      punct=":"),
  tok("وَاحِدٌ","wahid","noun",[Q,"badal","mubtada-khabar"],
      "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ، أَيْ: أَحَدُهَا وَاحِدٌ — أَوْ بَدَلُ تَفْصِيلٍ مِنْ سَبْعَةُ.",
      "«one» — opens the list: the khabar of a dropped mubtada (the first of them is ONE), or a detailing badal of سَبْعَةُ.",
      "«vâhid» — listeyi açar: düşmüş bir mübtedânın haberi (ilki TEKTİR), yahut سَبْعَةُ'den tafsil bedeli."),
  tok("حِسِّيٌّ","hissi","noun",[Q,"naat-sifa","ism-mansub"],
      "نَعْتٌ مَرْفُوعٌ.", "«sensory» — its na't.", "«hissî» — sıfatı.", punct="،"),
  tok("وَوَاحِدٌ","wahid","noun",[Q,"atf-nasaq"],
      "مَعْطُوفٌ مَرْفُوعٌ.", "«one» — joined.", "«vâhid» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("وَاحِدٌ","wahid","noun")]),
  tok("عَقْلِيٌّ","aqli","noun",[Q,"naat-sifa","ism-mansub"],
      "نَعْتٌ مَرْفُوعٌ.", "«of the mind» — its na't.", "«aklî» — sıfatı.", punct="،"),
  tok("وَمُرَكَّبٌ","murakkab","noun",[Q,"atf-nasaq","ism-maful"],
      "مَعْطُوفٌ مَرْفُوعٌ — اسْمُ مَفْعُولٍ.", "«composite» — joined; the ism maf'ul of رَكَّبَ.", "«mürekkeb» — atıf; رَكَّبَ'nin ism-i mef'ûlü.",
      segments=[seg("وَ","wa","conj"), seg("مُرَكَّبٌ","murakkab","noun")]),
  tok("حِسِّيٌّ","hissi","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«sensory» — na't.", "«hissî» — sıfat.", punct="،"),
  tok("وَمُرَكَّبٌ","murakkab","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«composite» — joined.", "«mürekkeb» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("مُرَكَّبٌ","murakkab","noun")]),
  tok("عَقْلِيٌّ","aqli","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«of the mind» — na't.", "«aklî» — sıfat.", punct="،"),
  tok("وَمُتَعَدِّدٌ","mutaaddid","noun",[Q,"atf-nasaq","ism-fail"], "مَعْطُوفٌ مَرْفُوعٌ.", "«several» — joined.", "«müteaddid» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("مُتَعَدِّدٌ","mutaaddid","noun")]),
  tok("حِسِّيٌّ","hissi","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«sensory» — na't.", "«hissî» — sıfat.", punct="،"),
  tok("وَمُتَعَدِّدٌ","mutaaddid","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«several» — joined.", "«müteaddid» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("مُتَعَدِّدٌ","mutaaddid","noun")]),
  tok("عَقْلِيٌّ","aqli","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«of the mind» — na't.", "«aklî» — sıfat.", punct="،"),
  tok("وَمُتَعَدِّدٌ","mutaaddid","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَرْفُوعٌ.", "«several» — joined.", "«müteaddid» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("مُتَعَدِّدٌ","mutaaddid","noun")]),
  tok("مُخْتَلِفٌ","mukhtalif","noun",[Q,"naat-sifa","ism-fail"],
      "نَعْتٌ مَرْفُوعٌ — بَعْضُهُ حِسِّيٌّ وَبَعْضُهُ عَقْلِيٌّ.",
      "«mixed» — the na't of the seventh: part sensory, part of the mind.",
      "«muhtelif» — yedincinin sıfatı: kısmen hissî, kısmen aklî.",
      punct=".")]})

# ----------- s4 — the sensory only between sensory ends; the mental wider (RESTORED)
S.append({"id": "s4", "translation": {
 "en": "The sensory wajh occurs only between two sensory ends, and the mental one is more general." + R_EN,
 "tr": "Hissî vech ancak iki hissî taraf arasında bulunur; aklî olan ise daha umumîdir." + R_TR},
 "tokens": [
  tok("وَالْحِسِّيُّ","hissi","noun",[Q,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْحِسِّيُّ مُبْتَدَأٌ مَرْفُوعٌ — أَيْ: وَجْهُ الشَّبَهِ الْحِسِّيُّ.",
      "«and the sensory» — the mubtada: the sensory WAJH, the noun understood.",
      "«ve hissî» — mübtedâ: hissî VECH, isim mukadder.",
      segments=[seg("وَ","wa","conj"), seg("الْحِسِّيُّ","hissi","noun")]),
  tok("لَا","la-nafiya","part",[Q,"istithna-mufarragh"],
      "حَرْفُ نَفْيٍ.", "«not» — the negation that إِلَّا will empty.", "«değil» — إِلَّا'nın boşaltacağı nefiy."),
  tok("يَكُونُ","kana","verb",[Q,"kana-wa-akhawatuha"],
      "فِعْلٌ مُضَارِعٌ تَامٌّ مَرْفُوعٌ بِمَعْنَى يُوجَدُ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.",
      "«occurs» — كَانَ COMPLETE (= is found), its fa'il hidden; the clause is the khabar.",
      "«bulunur» — TAM كَانَ (= var olur), fâili gizli; cümle haberdir."),
  tok("إِلَّا","illa","part",[Q,"istithna-mufarragh"],
      "أَدَاةُ حَصْرٍ — الِاسْتِثْنَاءُ مُفَرَّغٌ.",
      "«except» — the emptied exception: the verb reaches only what follows.",
      "«ancak» — müferrağ istisnâ: fiil yalnız sonrakine ulaşır."),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الْحِسِّيَّيْنِ","hissi","noun",[Q,"al-muthanna","huruf-jarr","ism-mansub"],
      "اسْمٌ مَجْرُورٌ بِالْيَاءِ لِأَنَّهُ مُثَنًّى — أَيِ: الطَّرَفَيْنِ الْحِسِّيَّيْنِ.",
      "«the two sensory ones» — a DUAL in jarr by its ya: the two sensory ENDS. Note the nisba's doubled ya before the dual ending.",
      "«iki hissî» — yâ ile mecrur TESNİYE: iki hissî TARAF. Tesniye ekinden önce nisbet yâsının şeddesine dikkat.",
      punct="،"),
  tok("وَالْعَقْلِيُّ","aqli","noun",[Q,"mubtada-khabar"],
      "الْوَاوُ عَاطِفَةٌ، وَالْعَقْلِيُّ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«and the mental» — a second mubtada.", "«aklî ise» — ikinci mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْعَقْلِيُّ","aqli","noun")]),
  tok("أَعَمُّ","aamm","noun",[Q,"mubtada-khabar","ism-tafdil","mamnu-min-sarf"],
      "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ عَلَى أَفْعَلَ، مَمْنُوعٌ مِنَ الصَّرْفِ: لَا تَنْوِينَ.",
      "«more general» — the khabar; an أَفْعَل of comparison, a diptote: no tanwin. It may stand between a sensory end and a mental one.",
      "«daha umumî» — haber; tafdil أَفْعَل'i, gayr-i munsarif: tenvinsiz. Hissî bir tarafla aklî bir taraf arasında da bulunabilir.",
      punct=".")]})

# ----------- s5 — the one and sensory: examples (RESTORED) — the kaf of «for instance»
S.append({"id": "s5", "translation": {
 "en": "The one-and-sensory: for instance redness, hiddenness, sweetness of scent, pleasure and softness." + R_EN,
 "tr": "Vâhid hissî: meselâ kızıllık, gizlilik, kokunun güzelliği, lezzet ve yumuşaklık." + R_TR},
 "tokens": [
  tok("فَالْوَاحِدُ","wahid","noun",[Q,"mubtada-khabar"],
      "الْفَاءُ لِلتَّفْصِيلِ، وَالْوَاحِدُ مُبْتَدَأٌ مَرْفُوعٌ.",
      "«the one» — the mubtada: the first of the seven.", "«vâhid» — mübtedâ: yedinin ilki.",
      segments=[seg("فَ","fa","conj"), seg("الْوَاحِدُ","wahid","noun")]),
  tok("الْحِسِّيُّ","hissi","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«sensory» — its na't.", "«hissî» — sıfatı."),
  tok("كَالْحُمْرَةِ","humra","noun",[Q,"huruf-jarr","tashbih"],
      "الْكَافُ جَارَّةٌ وَالْحُمْرَةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. وَهٰذِهِ كَافُ التَّمْثِيلِ: تُعْطِي مِثَالًا وَلَا تُشَبِّهُ.",
      "«like redness» — the kaf-phrase is the khabar; and this is the kaf of EXEMPLIFICATION — a category term stands before it, so the engine reads no likening here.",
      "«kızıllık gibi» — kâf tamlaması haberdir; bu ÖRNEK kâfıdır — önünde bir kısım adı durur; motor burada teşbih okumaz.",
      segments=[seg("كَ","ka","part"), seg("الْحُمْرَةِ","humra","noun")]),
  tok("وَالْخَفَاءِ","khafaa","noun",[Q,"atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ.", "«and hiddenness» — joined in jarr.", "«ve gizlilik» — mecrur atıf.",
      segments=[seg("وَ","wa","conj"), seg("الْخَفَاءِ","khafaa","noun")]),
  tok("وَطِيبِ","tib","noun",[Q,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ مَجْرُورٌ وَهُوَ مُضَافٌ.", "«and sweetness of» — joined, a mudaf.", "«ve güzelliği» — atıf, muzâf.",
      segments=[seg("وَ","wa","conj"), seg("طِيبِ","tib","noun")]),
  tok("الرَّائِحَةِ","raiha","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«scent» — the mudaf ilayh.", "«kokunun» — muzâfun ileyh."),
  tok("وَاللَّذَّةِ","ladhdha","noun",[Q,"atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«and pleasure» — joined.", "«ve lezzet» — atıf.",
      segments=[seg("وَ","wa","conj"), seg("اللَّذَّةِ","ladhdha","noun")]),
  tok("وَاللِّينِ","lin","noun",[Q,"atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — الْأَمْثِلَةُ الْخَمْسَةُ لِلْحَوَاسِّ الْخَمْسِ.",
      "«and softness» — joined: five examples for the five senses (sight, sight, smell, taste, touch).",
      "«ve yumuşaklık» — atıf: beş duyu için beş örnek (görme, görme, koklama, tatma, dokunma).",
      segments=[seg("وَ","wa","conj"), seg("اللِّينِ","lin","noun")], punct=".")]})

# ----------- s6 — the one and mental: the masdar frames, the wajh spoken BEFORE (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "The one-and-mental: for instance boldness, in likening the brave man to the lion; and guidance, in likening knowledge to light." + R_EN,
 "tr": "Vâhid aklî: meselâ cesur adamı arslana benzetmede cür'et; ve ilmi nura benzetmede hidâyet." + R_TR},
 "tashbih": frame([5, 6], 4, [7], [2], "mursal-mufassal", "mufrad", "mufrad", "mufrad"),
 "tokens": [
  tok("وَالْوَاحِدُ","wahid","noun",[Q,"mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْوَاحِدُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the one» — the mubtada.", "«ve vâhid» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْوَاحِدُ","wahid","noun")]),
  tok("الْعَقْلِيُّ","aqli","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«mental» — its na't.", "«aklî» — sıfatı."),
  tok("كَالْجُرْأَةِ","jura","noun",[Q,W,A,"huruf-jarr"],
      "الْكَافُ لِلتَّمْثِيلِ، وَالْجُرْأَةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. وَهِيَ وَجْهُ الشَّبَهِ فِي التَّشْبِيهِ الْآتِي.",
      "«for instance boldness» — the kaf of example, the phrase the khabar; and the word is the WAJH of the likening the masdar تَشْبِيهِ carries next — spoken before it.",
      "«meselâ cür'et» — örnek kâfı, tamlama haber; kelime, arkadan gelen تَشْبِيهِ masdarının taşıdığı benzetmenin VECHİdir — ondan önce söylenmiş.",
      segments=[seg("كَ","ka","part"), seg("الْجُرْأَةِ","jura","noun")]),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("تَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "اسْمٌ مَجْرُورٌ وَهُوَ مُضَافٌ — مَصْدَرٌ يَعْمَلُ عَمَلَ فِعْلِهِ: أُضِيفَ إِلَى مَفْعُولِهِ، وَالْبَاءُ تَجُرُّ الْمُشَبَّهَ بِهِ.",
      "«the likening of» — the masdar governs like its verb: annexed to its object (the mushabbah), the بِ marks the bihi. The masdar is the ADAT of this frame.",
      "«benzetmesinde» — masdar fiili gibi amel eder: mef'ûlüne (müşebbehe) muzâf, بِ müşebbehün bihi gösterir. Masdar bu çerçevenin EDATIdır."),
  tok("الرَّجُلِ","rajul","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«the man» — the mudaf ilayh: the MUSHABBAH.", "«adamı» — muzâfun ileyh: MÜŞEBBEH."),
  tok("الشُّجَاعِ","shujaa","noun",[Q,"naat-sifa","sifa-mushabbaha"], "نَعْتٌ مَجْرُورٌ — صِفَةٌ مُشَبَّهَةٌ.", "«brave» — its na't, a sifa mushabbaha.", "«cesur» — sıfatı, sıfat-ı müşebbehe."),
  tok("بِالْأَسَدِ","asad","noun",[Q,A,"huruf-jarr"],
      "الْبَاءُ جَارَّةٌ وَالْأَسَدِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.",
      "«to the lion» — the بِ-phrase: the MUSHABBAH BIHI. Both ends sensory, the wajh (boldness) of the mind.",
      "«arslana» — بِ tamlaması: MÜŞEBBEHÜN BİH. İki taraf hissî, vech (cür'et) aklî.",
      segments=[seg("بِ","bi","part"), seg("الْأَسَدِ","asad","noun")], punct="،"),
  tok("وَالْهِدَايَةِ","hidaya","noun",[Q,W,"atf-nasaq"],
      "مَعْطُوفٌ عَلَى الْجُرْأَةِ مَجْرُورٌ — وَهِيَ وَجْهُ الشَّبَهِ فِي التَّشْبِيهِ الثَّانِي.",
      "«and guidance» — joined to الْجُرْأَةِ; the WAJH of the second likening, again spoken before its masdar.",
      "«ve hidâyet» — الْجُرْأَةِ'ye atıf; ikinci benzetmenin VECHİ, yine masdarından önce.",
      segments=[seg("وَ","wa","conj"), seg("الْهِدَايَةِ","hidaya","noun")]),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("تَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — مَصْدَرٌ عَامِلٌ.", "«the likening of» — the second masdar-adat.", "«benzetmesinde» — ikinci masdar-edat."),
  tok("الْعِلْمِ","ilm","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«knowledge» — the mushabbah (of the mind).", "«ilmi» — müşebbeh (aklî)."),
  tok("بِالنُّورِ","nur","noun",[Q,A,"huruf-jarr"],
      "الْبَاءُ جَارَّةٌ وَالنُّورِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.",
      "«to light» — the bihi (sensory): a mental mushabbah, a sensory bihi, a mental wajh — the mental wajh is the wider.",
      "«nura» — müşebbehün bih (hissî): aklî müşebbeh, hissî bih, aklî vech — aklî vech daha geniştir.",
      segments=[seg("بِ","bi","part"), seg("النُّورِ","nur","noun")], punct=".")]})

# ----------- s7 — Abu Qays's bayt (as printed)
S.append({"id": "s7", "translation": {
 "en": "«And the Pleiades have shown in the dawn, as you see, like a cluster of white grapes when it has blossomed.»",
 "tr": "«Ve Süreyya, gördüğün gibi, sabahta belirdi — çiçek açtığında bir beyaz üzüm salkımı gibi.»"},
 "tashbih": frame([4], 7, [7, 8], [], "mursal-mujmal", "mufrad", "mufrad", None),
 "tokens": [
  tok("وَقَدْ","qad","part",[Q,"qad-harf"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ حَرْفُ تَحْقِيقٍ.", "«and indeed» — قَدْ before a mazi: certainty.", "«ve gerçekten» — mâzîden önce قَدْ: tahkik.",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("لَاحَ","laha-verb","verb",[Q,"hollow-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — أَجْوَفُ وَاوِيٌّ.",
      "«has shown» — a hollow mazi (لَوَحَ → لَاحَ); its fa'il comes after the jarr-phrase.",
      "«belirdi» — ecvef mâzî (لَوَحَ → لَاحَ); fâili câr-mecrûrdan sonra gelir."),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("الصُّبْحِ","subh","noun",[Q,"huruf-jarr"], "اسْمٌ مَجْرُورٌ مُتَعَلِّقٌ بِلَاحَ.", "«the dawn» — attached to the verb.", "«sabah» — fiile müteallik."),
  tok("الثُّرَيَّا","thurayya","noun",[Q,A,"fail","ism-maqsur-manqus"],
      "فَاعِلٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِلتَّعَذُّرِ — اسْمٌ مَقْصُورٌ. وَهُوَ الْمُشَبَّهُ.",
      "«the Pleiades» — the fa'il, a maqsur: its damma is only supposed on the alif. The MUSHABBAH, a single sensory thing.",
      "«Süreyya» — fâil, maksûr: dammesi elifte takdîrîdir. MÜŞEBBEH, tek bir hissî şey."),
  tok("كَمَا","kama","part",[Q,"an-masdariyya"],
      "الْكَافُ جَارَّةٌ وَمَا مَصْدَرِيَّةٌ — جُمْلَةٌ مُعْتَرِضَةٌ: كَرُؤْيَتِكَ.",
      "«as you see» — a parenthesis (كَرُؤْيَتِكَ) the likening steps over: this كَمَا is no adat.",
      "«gördüğün gibi» — benzetmenin üstünden atladığı bir ara cümle (كَرُؤْيَتِكَ): bu كَمَا edat değildir.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("تَرَى","raa","verb",[Q,"naqis-verbs","jumla-mutarida"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ، وَالْفَاعِلُ أَنْتَ — وَالْجُمْلَةُ صِلَةُ مَا.",
      "«you see» — a naqis mudari, its damma supposed on the alif; the clause is the sila of مَا.",
      "«görürsün» — nâkıs muzâri, dammesi elifte takdîrî; cümle مَا'nın sılası."),
  tok("كَعُنْقُودِ","unqud","noun",[Q,A,"huruf-jarr","hal","idafa-definiteness","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ جَارَّةٌ، وَعُنْقُودِ مَجْرُورٌ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الثُّرَيَّا. وَهُوَ الْمُشَبَّهُ بِهِ.",
      "«like a cluster of» — the kaf of LIKENING (the adat), the phrase a hal of the Pleiades: the MUSHABBAH BIHI, a single sensory thing.",
      "«bir salkımı gibi» — BENZETME kâfı (edat), tamlama Süreyya'dan hâl: MÜŞEBBEHÜN BİH, tek bir hissî şey.",
      segments=[seg("كَ","ka","part"), seg("عُنْقُودِ","unqud","noun")]),
  tok("مُلَّاحِيَّةٍ","mullahiyya","noun",[Q,"idafa-definiteness","ism-mansub"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عِنَبٌ أَبْيَضُ طَوِيلُ الْحَبِّ.",
      "«white grapes» — the mudaf ilayh: a long-berried white grape.",
      "«beyaz üzüm» — muzâfun ileyh: uzun taneli beyaz bir üzüm."),
  tok("حِينَ","hin","noun",[Q,"maful-fih"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِلَاحَ، وَهُوَ مُضَافٌ إِلَى الْجُمْلَةِ.",
      "«when» — a zarf of time on لَاحَ, annexed to the clause after it.",
      "«-diğinde» — لَاحَ'ya bağlı zaman zarfı, ardındaki cümleye muzâf."),
  tok("نَوَّرَا","nawwara","verb",[Q,"form-ii-verbs","idafa-definiteness"],
      "فِعْلٌ مَاضٍ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ (الْعُنْقُودُ)، وَالْأَلِفُ لِلْإِطْلَاقِ — وَالْجُمْلَةُ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.",
      "«it has blossomed» — Form II; the fa'il hidden (the cluster); the final alif is the rhyme's alif of itlaq, not the dual. The clause is the mudaf ilayh of حِينَ.",
      "«çiçek açtı» — II. bâb; fâil gizli (salkım); son elif tesniye değil kafiyenin ıtlak elifidir. Cümle حِينَ'nin muzâfun ileyhidir.",
      punct=".")],
 "jumal": [J("كَمَا تَرَى", "جُمْلَةٌ مُعْتَرِضَةٌ بَيْنَ الْمُشَبَّهِ وَالْمُشَبَّهِ بِهِ لَا مَحَلَّ لَهَا.",
             "A parenthesis between the two ends: the engine steps over it and joins الثُّرَيَّا to كَعُنْقُودِ.",
             "İki taraf arasında ara cümle: motor üstünden atlar, الثُّرَيَّا'yı كَعُنْقُودِ'ye bağlar.")]})

# ----------- s8 — the wajh of s7: a hay'a (RESTORED)
S.append({"id": "s8", "translation": {
 "en": "The wajh al-shabah in it is the configuration arising from the nearness of small, white, round shapes." + R_EN,
 "tr": "Ondaki vech-i şebeh, küçük, beyaz, yuvarlak suretlerin birbirine yaklaşmasından hâsıl olan hey'ettir." + R_TR},
 "tokens": [
  tok("فَوَجْهُ","wajh","noun",[Q,W,"mubtada-khabar","idafa-definiteness"], "الْفَاءُ لِلتَّفْرِيعِ، وَوَجْهُ مُبْتَدَأٌ مُضَافٌ.", "«so the face of» — the mubtada.", "«işte … yüzü» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("وَجْهُ","wajh","noun")]),
  tok("الشَّبَهِ","shabah","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness».", "«benzerliğin»."),
  tok("فِيهِ","fi","part",[Q,"huruf-jarr"], "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِمَحْذُوفٍ حَالٌ — وَالْهَاءُ لِلْبَيْتِ.", "«in it» — in the bayt.", "«onda» — beyitte.",
      segments=[seg("فِي","fi","part"), seg("هِ","pron-3ms","pron")]),
  tok("الْهَيْئَةُ","haya-shape","noun",[Q,W,"mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ — الْهَيْئَةُ: صُورَةٌ مُرَكَّبَةٌ مِنْ عِدَّةِ أُمُورٍ.",
      "«the configuration» — the khabar: a HAY'A, one picture built of several things — the mark of a COMPOSITE wajh.",
      "«hey'et» — haber: HEY'ET, birkaç şeyden kurulu tek tablo — MÜREKKEB vechin alâmeti."),
  tok("الْحَاصِلَةُ","hasil","noun",[Q,"naat-sifa","ism-fail"], "نَعْتٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ.", "«arising» — its na't.", "«hâsıl olan» — sıfatı."),
  tok("مِنْ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("تَقَارُبِ","taqarub","noun",[Q,"huruf-jarr","idafa-definiteness","masdar","form-vi-verbs"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — مَصْدَرُ تَقَارَبَ.", "«the nearness of» — the masdar of Form VI.", "«yaklaşmasından» — VI. bâbın masdarı."),
  tok("الصُّوَرِ","sura","noun",[Q,"idafa-definiteness","jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ صُورَةٍ.", "«the shapes» — the broken plural of صُورَة.", "«suretlerin» — صُورَة'nin kırık çoğulu."),
  tok("الصِّغَارِ","saghir","noun",[Q,"naat-sifa","jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ صَغِيرٍ.", "«small» — na't; plural of صَغِير.", "«küçük» — sıfat; صَغِير'in çoğulu."),
  tok("الْبِيضِ","bid-white","noun",[Q,"naat-sifa","jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ أَبْيَضَ.", "«white» — na't; plural of أَبْيَض.", "«beyaz» — sıfat; أَبْيَض'ın çoğulu."),
  tok("الْمُسْتَدِيرَةِ","mustadir","noun",[Q,"naat-sifa","ism-fail","form-x-verbs"],
      "نَعْتٌ مَجْرُورٌ — اسْمُ فَاعِلٍ مِنَ اسْتَدَارَ.",
      "«round» — na't; the ism fa'il of Form X (feminine singular for a plural of things). Three qualities into ONE picture: composite and sensory, the two ends single.",
      "«yuvarlak» — sıfat; X. bâbın ism-i fâili (eşya çoğulu için müennes tekil). Üç vasıf TEK tabloda: mürekkeb hissî, iki taraf tek.",
      punct=".")]})

# ----------- s9 — Bashshar's bayt (as printed; رُؤُسِنَا → رُؤُوسِنَا)
S.append({"id": "s9", "translation": {
 "en": "«As if the raised dust above our heads, and our swords, were a night whose stars come tumbling down.»",
 "tr": "«Sanki başlarımızın üstünde kalkan toz, kılıçlarımızla birlikte, yıldızları dökülüp duran bir gecedir.»"},
 "tashbih": frame([1, 2, 3, 4, 5], 0, [6, 7, 8], [], "mursal-mujmal", "murakkab", "murakkab", None),
 "tokens": [
  tok("كَأَنَّ","ka-anna","part",[Q,A,"inna-wa-akhawatuha","tashbih"],
      "حَرْفُ تَشْبِيهٍ وَنَصْبٍ مِنْ أَخَوَاتِ إِنَّ — أَدَاةُ التَّشْبِيهِ.",
      "«as if» — the sister of إِنَّ that likens: its ism is the mushabbah, its khabar the bihi.",
      "«sanki» — benzeten إِنَّ kardeşi: ismi müşebbeh, haberi müşebbehün bih."),
  tok("مُثَارَ","muthar","noun",[Q,A,"inna-wa-akhawatuha","ism-maful","idafa-definiteness"],
      "اسْمُ كَأَنَّ مَنْصُوبٌ وَهُوَ مُضَافٌ — اسْمُ مَفْعُولٍ مِنْ أَثَارَ.",
      "«the raised (dust)» — the ism of كَأَنَّ, annexed; the ism maf'ul of أَثَارَ. The MUSHABBAH begins here.",
      "«kaldırılan (toz)» — كَأَنَّ'nin ismi, muzâf; أَثَارَ'nin ism-i mef'ûlü. MÜŞEBBEH burada başlar."),
  tok("النَّقْعِ","naq","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — النَّقْعُ: الْغُبَارُ.", "«the dust» — the mudaf ilayh.", "«tozun» — muzâfun ileyh."),
  tok("فَوْقَ","fawqa","noun",[Q,"maful-fih","idafa-definiteness"],
      "ظَرْفُ مَكَانٍ مَنْصُوبٌ مُتَعَلِّقٌ بِمُثَارَ، وَهُوَ مُضَافٌ.",
      "«above» — a zarf of place hanging on مُثَارَ: the RESTRICTION that makes the mushabbah a picture.",
      "«üstünde» — مُثَارَ'ya bağlı mekân zarfı: müşebbehi tabloya çeviren KAYIT."),
  tok("رُؤُوسِنَا","ras","noun",[Q,"idafa-definiteness","jam-taksir"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَهُوَ مُضَافٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ رَأْسٍ.",
      "«our heads» — the mudaf ilayh, itself annexed to نَا; the broken plural فُعُول of رَأْس (the source writes رُؤُسِنَا).",
      "«başlarımızın» — muzâfun ileyh, kendisi de نَا'ya muzâf; رَأْس'in فُعُول çoğulu (kaynak رُؤُسِنَا yazar).",
      segments=[seg("رُؤُوسِ","ras","noun"), seg("نَا","pron-1p","pron")]),
  tok("وَأَسْيَافَنَا","sayf","noun",[Q,A,"atf-nasaq","inna-wa-akhawatuha","jam-taksir"],
      "مَعْطُوفٌ عَلَى اسْمِ كَأَنَّ مَنْصُوبٌ، وَنَا مُضَافٌ إِلَيْهِ — جَمْعُ سَيْفٍ عَلَى أَفْعَالٍ.",
      "«and our swords» — joined to the ISM of كَأَنَّ in nasb (never to its khabar): dust and swords together are ONE picture — the composite mushabbah.",
      "«ve kılıçlarımız» — كَأَنَّ'nin İSMİNE nasb ile atıf (haberine asla): toz ve kılıçlar birlikte TEK tablodur — mürekkeb müşebbeh.",
      segments=[seg("وَ","wa","conj"), seg("أَسْيَافَ","sayf","noun"), seg("نَا","pron-1p","pron")]),
  tok("لَيْلٌ","layl","noun",[Q,A,"inna-wa-akhawatuha"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ — الْمُشَبَّهُ بِهِ.",
      "«a night» — the khabar of كَأَنَّ: the MUSHABBAH BIHI, described by the clause that follows.",
      "«bir gece» — كَأَنَّ'nin haberi: MÜŞEBBEHÜN BİH, ardındaki cümleyle vasıflanmış."),
  tok("تَهَاوَى","tahawa","verb",[Q,"jumla-sifa","form-vi-verbs","naqis-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى فَتْحٍ مُقَدَّرٍ عَلَى الْأَلِفِ — وَالْجُمْلَةُ فِي مَحَلِّ رَفْعٍ نَعْتٌ لِلَيْلٌ.",
      "«come tumbling» — Form VI, naqis; the clause is a na't of the indefinite لَيْلٌ — what makes the bihi a picture.",
      "«dökülür» — VI. bâb, nâkıs; cümle nekre لَيْلٌ'ün sıfatı — bihi tabloya çeviren budur."),
  tok("كَوَاكِبُهُ","kawkab","noun",[Q,"fail","jam-taksir","mamnu-min-sarf"],
      "فَاعِلٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ عَائِدٌ إِلَى لَيْلٌ — جَمْعُ كَوْكَبٍ عَلَى فَوَاعِلَ، صِيغَةُ مُنْتَهَى الْجُمُوعِ.",
      "«its stars» — the fa'il; the ha is the returning pronoun that ties the clause to لَيْلٌ. فَوَاعِل: a plural of the heaviest shape, barred from tanwin — the idafa gives it its vowel.",
      "«yıldızları» — fâil; hâ, cümleyi لَيْلٌ'e bağlayan âiddir. فَوَاعِل: en ağır çoğul kalıbı, tenvinsiz — izâfet harekesini verir.",
      segments=[seg("كَوَاكِبُ","kawkab","noun"), seg("هُ","pron-3ms","pron")], punct=".")],
 "jumal": [J("تَهَاوَى كَوَاكِبُهُ", "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ رَفْعٍ نَعْتٌ.",
             "The describing clause: both ends composite and sensory — the wajh a hay'a of long bright bodies falling scattered around something dark.",
             "Vasıf cümlesi: iki taraf da mürekkeb hissî — vech, karanlık bir şeyin etrafına dağınık düşen uzun parlak cisimlerin hey'eti.")]})

# ----------- s10 — Ibn al-Muʿtazz: the sun a mirror in a palsied hand (as printed)
S.append({"id": "s10", "translation": {
 "en": "«A hunter loosed (his dog) upon it when it grew heedless — while the sun was like a mirror in the hand of the palsied.»",
 "tr": "«Avcı, o gaflete düşünce (köpeğini) üzerine saldı — güneş, titrek elli birinin elindeki ayna gibiyken.»"},
 "tashbih": frame([5], 6, [6, 7, 8, 9], [], "mursal-mujmal", "mufrad", "muqayyad", None),
 "tokens": [
  tok("صَبَّ","sabba","verb",[Q,"doubled-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ — مُضَاعَفٌ، وَمَفْعُولُهُ مَحْذُوفٌ (كَلْبَهُ).",
      "«loosed» — a geminate mazi (صَبَبَ → صَبَّ); its object, the dog, is dropped.",
      "«saldı» — muzâaf mâzî (صَبَبَ → صَبَّ); mef'ûlü (köpeği) düşmüş."),
  tok("عَلَيْهِ","ala","part",[Q,"huruf-jarr"],
      "جَارٌّ وَمَجْرُورٌ مُتَعَلِّقٌ بِصَبَّ — وَالْهَاءُ لِلثَّوْرِ الْوَحْشِيِّ.",
      "«upon it» — the wild bull of the earlier lines.", "«üzerine» — önceki beyitlerin yaban öküzü.",
      segments=[seg("عَلَيْ","ala","part"), seg("هِ","pron-3ms","pron")]),
  tok("قَانِصٌ","qanis","noun",[Q,"fail","ism-fail"], "فَاعِلٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ قَنَصَ.", "«a hunter» — the fa'il.", "«bir avcı» — fâil."),
  tok("لَمَّا","lamma","part",[Q,"maful-fih"],
      "ظَرْفٌ بِمَعْنَى حِينَ مُتَعَلِّقٌ بِصَبَّ.", "«when» — the لَمَّا of time.", "«-ince» — zaman لَمَّا'sı."),
  tok("غَفَلْ","ghafala","verb",[Q,"thulathi-mujarrad-babs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ، سُكِّنَ لِلْقَافِيَةِ، وَالْفَاعِلُ مُسْتَتِرٌ.",
      "«grew heedless» — a mazi whose fatha the rhyme turned to sukun (غَفَلَ → غَفَلْ); the fa'il hidden (the bull).",
      "«gaflete düştü» — fethasını kafiyenin sükûna çevirdiği mâzî (غَفَلَ → غَفَلْ); fâil gizli (öküz)."),
  tok("وَالشَّمْسُ","shams","noun",[Q,A,"hal","mubtada-khabar","anwa-al-waw"],
      "الْوَاوُ لِلْحَالِ، وَالشَّمْسُ مُبْتَدَأٌ مَرْفُوعٌ — الْمُشَبَّهُ.",
      "«while the sun» — the waw of HAL opens a nominal clause; the mubtada is the MUSHABBAH, a single sensory thing.",
      "«güneş … iken» — HÂL vâvı bir isim cümlesi açar; mübtedâ MÜŞEBBEHtir, tek bir hissî şey.",
      segments=[seg("وَ","wa","conj"), seg("الشَّمْسُ","shams","noun")]),
  tok("كَالْمِرْآةِ","mirat","noun",[Q,A,"huruf-jarr","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ، وَالْمِرْآةِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. وَهُوَ الْمُشَبَّهُ بِهِ.",
      "«like the mirror» — the kaf-adat; the phrase is the khabar: the MUSHABBAH BIHI (مِرْآة: the ism ala of رَأَى).",
      "«ayna gibi» — kâf-edat; tamlama haber: MÜŞEBBEHÜN BİH (مِرْآة: رَأَى'nın ism-i âleti).",
      segments=[seg("كَ","ka","part"), seg("الْمِرْآةِ","mirat","noun")]),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("كَفِّ","kaff","noun",[Q,A,"huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ، مُتَعَلِّقٌ بِمَحْذُوفٍ نَعْتٌ لِلْمِرْآةِ — قَيْدٌ عَلَى الْمُشَبَّهِ بِهِ.",
      "«the hand of» — a jarr-phrase RESTRICTING the mirror: a mirror in a shaking hand, so the bihi is muqayyad and the wajh a moving picture.",
      "«elinde» — aynayı KAYITLAYAN câr-mecrûr: titrek eldeki ayna; bih mukayyed, vech hareketli bir tablo."),
  tok("الْأَشَلْ","ashall","noun",[Q,"idafa-definiteness","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ سُكِّنَتْ لِلْقَافِيَةِ — أَفْعَلُ الْعَيْبِ.",
      "«the palsied» — the mudaf ilayh, its kasra silenced by the rhyme; an أَفْعَل of defect (a diptote, given its kasra by the article).",
      "«titrek ellinin» — muzâfun ileyh, kesrası kafiye için sükûn; kusur أَفْعَل'i (gayr-i munsarif, kesrasını harf-i tariften alır).",
      punct=".")],
 "jumal": [J("وَالشَّمْسُ كَالْمِرْآةِ فِي كَفِّ الْأَشَلْ", "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ نَصْبٍ حَالٌ.",
             "The hal-clause holds the whole likening: the wajh is a hay'a — a round bright body whose light trembles and runs — composite and sensory, the two ends single.",
             "Hâl cümlesi bütün benzetmeyi taşır: vech bir hey'ettir — ışığı titreyip akan yuvarlak parlak cisim — mürekkeb hissî, iki taraf tek.")]})

# ----------- s11 — Ibn al-Muʿtazz: the lightning a reader's mushaf (as printed)
S.append({"id": "s11", "translation": {
 "en": "«And as if the lightning were the mushaf of a reciter — now closing, now opening.»",
 "tr": "«Ve sanki şimşek, bir okuyucunun mushafıdır — bir kapanır, bir açılır.»"},
 "tashbih": frame([1], 0, [2, 3], [4, 5, 6], "mursal-mufassal", "mufrad", "mufrad", "murakkab"),
 "tokens": [
  tok("وَكَأَنَّ","ka-anna","part",[Q,A,"inna-wa-akhawatuha","tashbih"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَأَنَّ حَرْفُ تَشْبِيهٍ وَنَصْبٍ.", "«and as if» — the adat.", "«ve sanki» — edat.",
      segments=[seg("وَ","wa","conj"), seg("كَأَنَّ","ka-anna","part")]),
  tok("الْبَرْقَ","barq","noun",[Q,A,"inna-wa-akhawatuha"], "اسْمُ كَأَنَّ مَنْصُوبٌ — الْمُشَبَّهُ.", "«the lightning» — the ism: the MUSHABBAH.", "«şimşek» — ism: MÜŞEBBEH."),
  tok("مُصْحَفُ","mushaf","noun",[Q,A,"inna-wa-akhawatuha","idafa-definiteness"],
      "خَبَرُ كَأَنَّ مَرْفُوعٌ وَهُوَ مُضَافٌ — الْمُشَبَّهُ بِهِ.",
      "«the mushaf of» — the khabar, annexed: the MUSHABBAH BIHI.", "«mushafı» — haber, muzâf: MÜŞEBBEHÜN BİH."),
  tok("قَارٍ","qari","noun",[Q,"idafa-definiteness","ism-maqsur-manqus","ism-fail"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ الْمَحْذُوفَةِ — أَصْلُهُ قَارِئٌ: قُلِبَتِ الْهَمْزَةُ يَاءً لِكَسْرِ مَا قَبْلَهَا ثُمَّ حُذِفَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.",
      "«a reciter» — the mudaf ilayh; a MANQUS: originally قَارِئ, the hamza turned ya after the kasra, then the ya dropped before the tanwin — the kasra is only supposed.",
      "«bir okuyucunun» — muzâfun ileyh; MANKÛS: aslı قَارِئ, hemze kesradan sonra yâya döndü, sonra yâ tenvin önünde düştü — kesra takdîrîdir."),
  tok("فَانْطِبَاقًا","intibaq","noun",[Q,W,"maful-mutlaq","masdar","form-vii-verbs"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَانْطِبَاقًا مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ: يَنْطَبِقُ انْطِبَاقًا — أَوْ حَالٌ: مُنْطَبِقًا.",
      "«closing» — a masdar in nasb for a dropped verb (it closes A CLOSING), or a hal; the WAJH begins: the picture of alternate motion.",
      "«kapanarak» — düşmüş bir fiilin mef'ûl-i mutlakı (KAPANIŞLA kapanır), yahut hâl; VECH başlar: sırayla hareket tablosu.",
      segments=[seg("فَ","fa","conj"), seg("انْطِبَاقًا","intibaq","noun")]),
  tok("مَرَّةً","marra-once","noun",[Q,W,"maful-fih"],
      "ظَرْفُ زَمَانٍ مَنْصُوبٌ — مَرَّةً … وَمَرَّةً: التَّنَاوُبُ.",
      "«now (one time)» — a zarf of time: the alternation «now … now» is what makes the wajh a hay'a of MOTION.",
      "«bir (kez)» — zaman zarfı: «bir … bir» nöbetleşmesi, vechi HAREKET hey'eti yapan budur."),
  tok("وَانْفِتَاحًا","infitah","noun",[Q,W,"atf-nasaq","masdar","form-vii-verbs"],
      "مَعْطُوفٌ عَلَى انْطِبَاقًا مَنْصُوبٌ — وَالتَّقْدِيرُ: مَرَّةً وَانْفِتَاحًا مَرَّةً.",
      "«and opening» — joined to the first masdar (another مَرَّةً understood). Closing-then-opening: ONE picture, composite and sensory, drawn from motion.",
      "«ve açılarak» — ilk masdara atıf (ikinci bir مَرَّةً mukadder). Kapanıp açılma: hareketten çıkan TEK tablo, mürekkeb hissî.",
      segments=[seg("وَ","wa","conj"), seg("انْفِتَاحًا","infitah","noun")], punct=".")]})

# ----------- s12 — al-Mutanabbi's dog: the maf'ul mutlaq stands for the adat (as printed)
S.append({"id": "s12", "translation": {
 "en": "«It squats (as) the sitting of the bedouin warming at the fire, on four firm-twisted (legs) that were never twisted.»",
 "tr": "«Ateşte ısınan bedevînin oturuşu gibi çömelir — hiç bükülmemiş, sımsıkı örülü dört (ayak) üstünde.»"},
 "tashbih": {"mushabbah": [], "adat": None, "bihi": [2, 3], "wajh": [], "kind": "muakkad-mujmal",
             "shape": {"mushabbah": None, "bihi": "mufrad", "wajh": None}},
 "tokens": [
  tok("يُقْعِي","aqa","verb",[Q,A,"form-iv-verbs","naqis-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ لِلثِّقَلِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ (الْكَلْبُ) — وَهُوَ الْمُشَبَّهُ.",
      "«it squats» — Form IV naqis (أَقْعَى: to sit on the haunches); the hidden fa'il, the dog, is the MUSHABBAH.",
      "«çömelir» — IV. bâb nâkıs (أَقْعَى: kıç üstü oturmak); gizli fâil, köpek, MÜŞEBBEHtir."),
  tok("جُلُوسَ","julus","noun",[Q,A,"maful-mutlaq","masdar","idafa-definiteness","tashbih"],
      "مَفْعُولٌ مُطْلَقٌ مَنْصُوبٌ مُبَيِّنٌ لِلنَّوْعِ، وَهُوَ مُضَافٌ — وَالتَّقْدِيرُ: يُقْعِي إِقْعَاءً مِثْلَ جُلُوسِ الْبَدَوِيِّ: حُذِفَتِ الْأَدَاةُ وَقَامَ الْمَصْدَرُ مَقَامَهَا.",
      "«(as) the sitting of» — a maf'ul mutlaq naming the kind; the adat (مِثْلَ) is DROPPED and the masdar stands in its place: a muakkad tashbih with no adat in sight.",
      "«oturuşu (gibi)» — nev'i bildiren mef'ûl-i mutlak; edat (مِثْلَ) DÜŞMÜŞ, masdar yerine geçmiştir: ortada edat olmayan müekked teşbih."),
  tok("الْبَدَوِيِّ","badawi","noun",[Q,A,"idafa-definiteness","ism-mansub"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمٌ مَنْسُوبٌ إِلَى الْبَدْوِ. وَهُوَ الْمُشَبَّهُ بِهِ.",
      "«the bedouin» — the mudaf ilayh, a nisba to الْبَدْو: the MUSHABBAH BIHI.",
      "«bedevînin» — muzâfun ileyh, الْبَدْو'e nisbet: MÜŞEBBEHÜN BİH."),
  tok("الْمُصْطَلِي","mustali","noun",[Q,"naat-sifa","ism-fail","ism-maqsur-manqus","form-viii-verbs"],
      "نَعْتٌ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْيَاءِ — اسْمُ فَاعِلٍ مِنَ اصْطَلَى، مَنْقُوصٌ: الْأَلِفُ وَاللَّامُ تُبْقِيَانِ يَاءَهُ.",
      "«warming at the fire» — its na't, a manqus with the article: the ya stays and the kasra is supposed on it.",
      "«ateşte ısınan» — sıfatı, harf-i tarifli mankûs: yâ kalır, kesra üstünde takdîrîdir."),
  tok("بِأَرْبَعٍ","arba","noun",[Q,"huruf-jarr"],
      "الْبَاءُ جَارَّةٌ وَأَرْبَعٍ مَجْرُورٌ مُتَعَلِّقٌ بِيُقْعِي — أَيْ: بِأَرْبَعِ قَوَائِمَ؛ الْعَدَدُ بِلَا تَاءٍ لِأَنَّ الْمَعْدُودَ مُؤَنَّثٌ.",
      "«on four» — the counted noun (legs) dropped; the number has NO ta because the counted is feminine (قَائِمَة).",
      "«dört (ayak) üstünde» — sayılan (ayaklar) düşmüş; sayı tâsızdır, çünkü sayılan müennestir (قَائِمَة).",
      segments=[seg("بِ","bi","part"), seg("أَرْبَعٍ","arba","noun")]),
  tok("مَجْدُولَةٍ","majdul","noun",[Q,"naat-sifa","ism-maful"],
      "نَعْتٌ مَجْرُورٌ — اسْمُ مَفْعُولٍ مِنْ جَدَلَ: مَفْتُولَةٍ مُحْكَمَةٍ.",
      "«firm-twisted» — na't; the ism maf'ul of جَدَلَ (to twist a rope tight).",
      "«sımsıkı örülü» — sıfat; جَدَلَ'nin ism-i mef'ûlü (ipi sıkı bükmek)."),
  tok("لَمْ","lam-jazima","part",[Q,"lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not» — the jazm-lam.", "«-medi» — cezm lâmı."),
  tok("تُجْدَلِ","jadala-braid","verb",[Q,"lam-jazim","naib-al-fail","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَجْزُومٌ بِلَمْ وَعَلَامَةُ جَزْمِهِ السُّكُونُ، حُرِّكَ بِالْكَسْرِ لِلْقَافِيَةِ؛ نَائِبُ الْفَاعِلِ مُسْتَتِرٌ — وَالْجُمْلَةُ نَعْتٌ ثَانٍ.",
      "«that were never twisted» — a majhul mudari in jazm; the sukun took a kasra for the rhyme (تُجْدَلْ → تُجْدَلِ); the clause is a second na't: legs so firm they seem twisted, yet no hand twisted them.",
      "«hiç bükülmemiş» — meczum meçhul muzâri; sükûn kafiye için kesra aldı (تُجْدَلْ → تُجْدَلِ); cümle ikinci sıfat: sanki örülmüş gibi sağlam, oysa kimse örmemiş.",
      punct=".")],
 "jumal": [J("لَمْ تُجْدَلِ", "جُمْلَةٌ فِعْلِيَّةٌ فِي مَحَلِّ جَرٍّ نَعْتٌ.",
             "The wajh: the hay'a of every limb in its place at rest — composite, sensory, and a picture of STILLNESS this time.",
             "Vech: her uzvun yerinde durduğu sükûn hey'eti — mürekkeb, hissî ve bu kez SÜKÛN tablosu.")]})

# ----------- s13 — the aya 62:5 (as printed; التَّوْرٰيةَ → التَّوْرَاةَ)
S.append({"id": "s13", "translation": {
 "en": "«The likeness of those who were made to carry the Torah, then did not carry it, is as the likeness of a donkey carrying volumes.» (62:5)",
 "tr": "«Kendilerine Tevrat yükletilip de sonra onu taşımayanların durumu, kitaplar taşıyan eşeğin durumu gibidir.» (62:5)"},
 "tashbih": frame([0, 1, 2, 3, 4, 5, 6], 7, [7, 8, 9, 10], [], "mursal-mujmal", "murakkab", "murakkab", None),
 "tokens": [
  tok("مَثَلُ","mathal","noun",[Q,A,"mubtada-khabar","idafa-definiteness"],
      "مُبْتَدَأٌ مَرْفُوعٌ وَهُوَ مُضَافٌ — الْمَثَلُ: الْحَالُ الْعَجِيبَةُ.",
      "«the likeness of» — the mubtada, annexed: the STATE of those people is the mushabbah, a whole picture.",
      "«durumu» — mübtedâ, muzâf: o kimselerin HÂLİ müşebbehtir, bütün bir tablo."),
  tok("الَّذِينَ","alladhina","pron",[Q,"ism-mawsul","idafa-definiteness"],
      "اسْمٌ مَوْصُولٌ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ مُضَافٌ إِلَيْهِ.", "«those who» — the relative, the mudaf ilayh.", "«… kimselerin» — ism-i mevsûl, muzâfun ileyh."),
  tok("حُمِّلُوا","hammala","verb",[Q,"naib-al-fail","form-ii-verbs","jumla-sifa"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالْوَاوُ نَائِبُ فَاعِلٍ — وَالْجُمْلَةُ صِلَةٌ.",
      "«were made to carry» — Form II majhul (حَمَّلَ takes two objects; the first became the deputy, the second stays in nasb); the sila begins.",
      "«yükletildiler» — II. bâb meçhul (حَمَّلَ iki mef'ûl alır; ilki nâib oldu, ikincisi nasbda kalır); sıla başlar."),
  tok("التَّوْرَاةَ","tawrat","noun",[Q,"maful-bihi","mafulayn"],
      "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ — وَالْمَصْدَرُ يَكْتُبُهَا التَّوْرٰيةَ.",
      "«the Torah» — the SECOND object, kept in nasb after the passive (the source writes التَّوْرٰيةَ).",
      "«Tevrat'ı» — meçhulden sonra nasbda kalan İKİNCİ mef'ûl (kaynak التَّوْرٰيةَ yazar)."),
  tok("ثُمَّ","thumma","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرَاخِي.", "«then» — the atf of delay.", "«sonra» — terâhî atfı."),
  tok("لَمْ","lam-jazima","part",[Q,"lam-jazim"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-medi»."),
  tok("يَحْمِلُوهَا","hamala","verb",[Q,"lam-jazim","afal-khamsa"],
      "فِعْلٌ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ لِأَنَّهُ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ — مَعْطُوفٌ عَلَى الصِّلَةِ.",
      "«did not carry it» — one of the five verbs, jazm by the dropped nun; the waw its fa'il, the ha its object. The mushabbah ends here: a composite, MENTAL picture.",
      "«onu taşımadılar» — ef'âl-i hamseden, cezmi nûnun düşmesiyle; vâv fâil, hâ mef'ûl. Müşebbeh burada biter: mürekkeb, AKLÎ bir tablo.",
      segments=[seg("يَحْمِلُو","hamala","verb"), seg("هَا","pron-3fs","pron")]),
  tok("كَمَثَلِ","mathal","noun",[Q,A,"huruf-jarr","idafa-definiteness","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ جَارَّةٌ، وَمَثَلِ مَجْرُورٌ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. الْأَدَاةُ وَبِدَايَةُ الْمُشَبَّهِ بِهِ.",
      "«is as the likeness of» — the kaf-adat; the phrase is the khabar and opens the bihi.",
      "«durumu gibidir» — kâf-edat; tamlama haber, bihi açar.",
      segments=[seg("كَ","ka","part"), seg("مَثَلِ","mathal","noun")]),
  tok("الْحِمَارِ","himar","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the donkey» — the mudaf ilayh.", "«eşeğin» — muzâfun ileyh."),
  tok("يَحْمِلُ","hamala","verb",[Q,"hal","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ فِي مَحَلِّ نَصْبٍ حَالٌ مِنَ الْحِمَارِ.",
      "«carrying» — a hal-clause on the definite donkey: the bihi too is a composite picture.",
      "«taşıyan» — marife eşekten hâl cümlesi: bih de mürekkeb bir tablodur."),
  tok("أَسْفَارًا","sifr","noun",[Q,"maful-bihi","jam-taksir"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — جَمْعُ سِفْرٍ عَلَى أَفْعَالٍ: الْكُتُبُ الْكِبَارُ.",
      "«volumes» — the object; أَفْعَال plural of سِفْر, a great book. The wajh: bearing the burden of a most useful thing while denied its benefit — composite and mental.",
      "«kitaplar» — mef'ûl; سِفْر'in أَفْعَال çoğulu, büyük kitap. Vech: çok faydalı bir şeyin yükünü çekip faydasından mahrum kalmak — mürekkeb aklî.",
      punct=".")]})

# ----------- s14 — the wajh and the ends of the aya (RESTORED)
S.append({"id": "s14", "translation": {
 "en": "So its wajh al-shabah is composite and of the mind, and its two ends are composite and of the mind." + R_EN,
 "tr": "Vech-i şebehi mürekkeb aklîdir; iki tarafı da mürekkeb aklîdir." + R_TR},
 "tokens": [
  tok("فَوَجْهُ","wajh","noun",[Q,"mubtada-khabar","idafa-definiteness"], "الْفَاءُ لِلتَّفْرِيعِ، وَوَجْهُ مُبْتَدَأٌ مُضَافٌ.", "«so the face of» — the mubtada.", "«işte … yüzü» — mübtedâ.",
      segments=[seg("فَ","fa","conj"), seg("وَجْهُ","wajh","noun")]),
  tok("الشَّبَهِ","shabah","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness».", "«benzerliğin»."),
  tok("مُرَكَّبٌ","murakkab","noun",[Q,"mubtada-khabar","ism-maful"], "خَبَرٌ مَرْفُوعٌ.", "«composite» — the khabar.", "«mürekkeb» — haber."),
  tok("عَقْلِيٌّ","aqli","noun",[Q,"naat-sifa","ism-mansub"], "نَعْتٌ مَرْفُوعٌ.", "«of the mind» — its na't.", "«aklî» — sıfatı.", punct="،"),
  tok("وَطَرَفَاهُ","taraf","noun",[Q,"al-muthanna","mubtada-khabar","idafa-definiteness"],
      "الْوَاوُ عَاطِفَةٌ، وَطَرَفَا مُبْتَدَأٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«and its two ends» — a DUAL mubtada in raf' by its alif; the nun dropped for the idafa, the ha the mudaf ilayh — one word, two offices.",
      "«ve iki tarafı» — elifle merfû TESNİYE mübtedâ; nûnu izâfet için düşmüş, hâ muzâfun ileyh — bir kelime, iki vazife.",
      segments=[seg("وَ","wa","conj"), seg("طَرَفَا","taraf","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مُرَكَّبَانِ","murakkab","noun",[Q,"al-muthanna","mubtada-khabar"],
      "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ لِأَنَّهُ مُثَنًّى.", "«composite» — the dual khabar, raf' by the alif.", "«mürekkeb» — tesniye haber, ref'i elifle."),
  tok("عَقْلِيَّانِ","aqli","noun",[Q,"al-muthanna","naat-sifa","ism-mansub"],
      "نَعْتٌ مَرْفُوعٌ بِالْأَلِفِ — الْيَاءُ الْمُشَدَّدَةُ لِلنِّسْبَةِ ثُمَّ أَلِفُ الْمُثَنَّى.",
      "«of the mind» — the dual na't: the nisba's doubled ya, then the dual's alif and nun.",
      "«aklî» — tesniye sıfat: önce nisbetin şeddeli yâsı, sonra tesniyenin elif-nûnu.",
      punct=".")]})

# ----------- s15 — the first bayt of the pair (as printed)
S.append({"id": "s15", "translation": {
 "en": "«She made me hope for union with a smile; then when we asked, she turned her face and turned her back.»",
 "tr": "«Bir tebessümle beni vuslata umutlandırdı; sonra istediğimizde yüz çevirdi ve arkasını döndü.»"},
 "tokens": [
  tok("لَقَدْ","qad","part",[Q,"qad-harf","lam-taleel"],
      "اللَّامُ لِلتَّوْكِيدِ (لَامُ الِابْتِدَاءِ أَوْ جَوَابُ قَسَمٍ مُقَدَّرٍ)، وَقَدْ حَرْفُ تَحْقِيقٍ.",
      "«indeed» — the lam of emphasis (or of a supposed oath) and قَدْ of certainty before the mazi.",
      "«gerçekten» — te'kid lâmı (yahut mukadder bir kasemin cevabı) ve mâzîden önce tahkik قَدْ'ı.",
      segments=[seg("لَ","lam-ibtida","part"), seg("قَدْ","qad","part")]),
  tok("أَطْمَعَتْنِي","atmaa","verb",[Q,"form-iv-verbs","ya-al-mutakallim","maful-bihi"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ، وَالْفَاعِلُ مُسْتَتِرٌ (هِيَ).",
      "«she made me hope» — Form IV; the ta of the feminine, the nun of guarding, the speaker's ya as object; the fa'il hidden (she — the beloved).",
      "«beni umutlandırdı» — IV. bâb; te'nis tâsı, vikaye nûnu, mütekellim yâsı mef'ûl; fâil gizli (o — sevgili).",
      segments=[seg("أَطْمَعَتْ","atmaa","verb"), seg("نِي","pron-1s","pron")]),
  tok("بِالْوِصَالِ","wisal","noun",[Q,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَالْوِصَالِ مَجْرُورٌ مُتَعَلِّقٌ بِأَطْمَعَ.", "«for union» — the thing hoped for.", "«vuslata» — umulan şey.",
      segments=[seg("بِ","bi","part"), seg("الْوِصَالِ","wisal","noun")]),
  tok("تَبَسُّمًا","tabassum","noun",[Q,"hal","masdar","form-v-verbs"],
      "مَصْدَرٌ مَنْصُوبٌ فِي مَوْضِعِ الْحَالِ: مُتَبَسِّمَةً — أَوْ مَفْعُولٌ لِأَجْلِهِ.",
      "«with a smile» — a masdar as HAL (= smiling), or the maf'ul li-ajlih (out of a smile).",
      "«tebessümle» — HÂL yerinde masdar (= gülümseyerek), yahut mef'ûl-i li-eclih."),
  tok("فَلَمَّا","lamma","part",[Q,"maful-fih"],
      "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ فِيهِ مَعْنَى الشَّرْطِ.",
      "«then when» — لَمَّا of time with a shade of condition; its answer is أَعْرَضَتْ.",
      "«sonra … -ınca» — şart mânâlı zaman لَمَّا'sı; cevabı أَعْرَضَتْ.",
      segments=[seg("فَ","fa","conj"), seg("لَمَّا","lamma","part")]),
  tok("سَأَلْنَا","saala","verb",[Q,"fail"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا، وَنَا فَاعِلٌ — لَا مَفْعُولٌ: سَأَلْنَا نَحْنُ.",
      "«we asked» — the mazi on sukun before نَا the FA'IL (we asked), not سَأَلَنَا «he asked us»: the sukun on the lam decides it.",
      "«istedik» — نَا FÂİLİ önünde sükûnlu mâzî (biz istedik), سَأَلَنَا «bizden istedi» değil: lâmdaki sükûn belirler.",
      segments=[seg("سَأَلْ","saala","verb"), seg("نَا","pron-1p","pron")]),
  tok("أَعْرَضَتْ","arada-away","verb",[Q,"form-iv-verbs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — جَوَابُ لَمَّا.",
      "«she turned away» — Form IV; the answer of لَمَّا.", "«yüz çevirdi» — IV. bâb; لَمَّا'nın cevabı."),
  tok("وَتَوَلَّتْ","tawalla","verb",[Q,"form-v-verbs","naqis-verbs","atf-nasaq"],
      "مَعْطُوفٌ — فِعْلٌ مَاضٍ نَاقِصٌ حُذِفَتْ أَلِفُهُ لِتَاءِ التَّأْنِيثِ: تَوَلَّى → تَوَلَّتْ.",
      "«and turned her back» — Form V naqis: the alif drops before the feminine ta (تَوَلَّى → تَوَلَّتْ). The MUSHABBAH of the pair is this whole state; the adat and bihi come in the next bayt.",
      "«ve arkasını döndü» — V. bâb nâkıs: te'nis tâsı önünde elif düşer (تَوَلَّى → تَوَلَّتْ). Çiftin MÜŞEBBEHİ bu hâlin bütünüdür; edat ve bih sonraki beyitte.",
      segments=[seg("وَ","wa","conj"), seg("تَوَلَّتْ","tawalla","verb")], punct=".")]})

# ----------- s16 — the second bayt: كَمَا carries the likening across the pair (as printed)
S.append({"id": "s16", "translation": {
 "en": "«— as a cloud flashed lightning to a thirsty folk; then when they saw it, it broke up and cleared away.»",
 "tr": "«— tıpkı bir bulutun susuz bir kavme şimşek çakması gibi; sonra onu görünce dağılıp açıldı.»"},
 "tokens": [
  tok("كَمَا","kama","part",[Q,A,"an-masdariyya","tashbih"],
      "الْكَافُ لِلتَّشْبِيهِ وَمَا مَصْدَرِيَّةٌ — أَيْ: كَإِبْرَاقِ غَمَامَةٍ. أَدَاةُ التَّشْبِيهِ الَّذِي مُشَبَّهُهُ الْبَيْتُ السَّابِقُ كُلُّهُ.",
      "«as» — the kaf of likening over a masdar-مَا (= like a cloud's flashing): the ADAT whose mushabbah is the WHOLE previous bayt and whose bihi is this whole bayt. The engine reads one sentence at a time, so the frame is not authored here.",
      "«gibi» — masdariye مَا üzerine benzetme kâfı (= bir bulutun şimşek çakması gibi): müşebbehi ÖNCEKİ beytin bütünü, bihi bu beytin bütünü olan EDAT. Motor cümleyi tek tek okur; çerçeve burada yazılmamıştır.",
      segments=[seg("كَ","ka","part"), seg("مَا","ma-masdariyya","part")]),
  tok("أَبْرَقَتْ","abraqa","verb",[Q,"form-iv-verbs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ — وَالْجُمْلَةُ صِلَةُ مَا الْمَصْدَرِيَّةِ.",
      "«flashed lightning» — Form IV; the sila of the masdar-مَا; its fa'il waits at the end of the hemistich.",
      "«şimşek çaktı» — IV. bâb; masdariye مَا'nın sılası; fâili mısra sonunda bekler."),
  tok("قَوْمًا","qawm","noun",[Q,"maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«a folk» — the object, before the fa'il.", "«bir kavme» — fâilden önce mef'ûl."),
  tok("عِطَاشًا","atshan","noun",[Q,"naat-sifa","jam-taksir"],
      "نَعْتٌ مَنْصُوبٌ — جَمْعُ عَطْشَانَ عَلَى فِعَالٍ.", "«thirsty» — na't; the فِعَال plural of عَطْشَان.", "«susuz» — sıfat; عَطْشَان'ın فِعَال çoğulu."),
  tok("غَمَامَةٌ","ghamama","noun",[Q,"fail"], "فَاعِلٌ مَرْفُوعٌ مُؤَخَّرٌ.", "«a cloud» — the fa'il, delayed.", "«bir bulut» — te'hir edilmiş fâil."),
  tok("فَلَمَّا","lamma","part",[Q,"maful-fih"], "الْفَاءُ عَاطِفَةٌ، وَلَمَّا ظَرْفٌ بِمَعْنَى حِينَ.", "«then when».", "«sonra … -ınca».",
      segments=[seg("فَ","fa","conj"), seg("لَمَّا","lamma","part")]),
  tok("رَأَوْهَا","raa","verb",[Q,"naqis-verbs","maful-bihi"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الضَّمِّ الْمُقَدَّرِ، حُذِفَتْ لَامُهُ لِوَاوِ الْجَمَاعَةِ، وَالْوَاوُ فَاعِلٌ، وَالْهَاءُ مَفْعُولٌ بِهِ.",
      "«they saw it» — رَأَى with the group's waw: the weak lam drops (رَأَى + وا → رَأَوْا), the ha is the object (the cloud).",
      "«onu gördüler» — cemaat vâvıyla رَأَى: illetli lâm düşer (رَأَى + وا → رَأَوْا), hâ mef'ûl (bulut).",
      segments=[seg("رَأَوْ","raa","verb"), seg("هَا","pron-3fs","pron")]),
  tok("أَقْشَعَتْ","aqshaa","verb",[Q,"form-iv-verbs"],
      "فِعْلٌ مَاضٍ، وَالتَّاءُ لِلتَّأْنِيثِ، وَالْفَاعِلُ مُسْتَتِرٌ — جَوَابُ لَمَّا.",
      "«it broke up» — Form IV (the cloud dispersed); the answer of لَمَّا.", "«dağıldı» — IV. bâb (bulut dağıldı); لَمَّا'nın cevabı."),
  tok("وَتَجَلَّتْ","tajalla","verb",[Q,"form-v-verbs","naqis-verbs","atf-nasaq"],
      "مَعْطُوفٌ — فِعْلٌ مَاضٍ نَاقِصٌ حُذِفَتْ أَلِفُهُ لِتَاءِ التَّأْنِيثِ.",
      "«and cleared away» — Form V naqis, its alif dropped before the ta. The wajh: a hopeful BEGINNING joined to a depriving END — and only the whole bayt yields it.",
      "«ve açılıp gitti» — V. bâb nâkıs, elifi tâ önünde düşmüş. Vech: umut veren BAŞLANGICIN mahrum bırakan SONA bitişmesi — ve onu ancak beytin bütünü verir.",
      segments=[seg("وَ","wa","conj"), seg("تَجَلَّتْ","tajalla","verb")], punct=".")]})

# ----------- s17 — the rule of the whole bayt (RESTORED)
S.append({"id": "s17", "translation": {
 "en": "The error is that the wajh al-shabah be drawn from the first hemistich alone; what is required is to draw it from the whole bayt." + R_EN,
 "tr": "Hata, vech-i şebehin yalnız ilk mısradan çıkarılmasıdır; vâcib olan, onu beytin bütününden çıkarmaktır." + R_TR},
 "tokens": [
  tok("وَالْخَطَأُ","khata","noun",[Q,"mubtada-khabar"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَالْخَطَأُ مُبْتَدَأٌ مَرْفُوعٌ.", "«the error» — the mubtada.", "«hata» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْخَطَأُ","khata","noun")]),
  tok("أَنْ","an-masdariyya","part",[Q,"an-masdariyya"],
      "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ: الْخَطَأُ انْتِزَاعُهُ.",
      "«that» — the masdar-أَنْ; the clause it turns into a masdar is the khabar (the error is ITS BEING DRAWN…).",
      "«-ması» — masdariye أَنْ; masdara çevirdiği cümle haberdir (hata, ÇIKARILMASIdır…)."),
  tok("يُنْتَزَعَ","intazaa","verb",[Q,"naib-al-fail","form-viii-verbs","an-masdariyya"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be drawn» — Form VIII majhul, nasb by أَنْ.", "«çıkarılsın» — VIII. bâb meçhul, أَنْ ile mansub."),
  tok("وَجْهُ","wajh","noun",[Q,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ وَهُوَ مُضَافٌ.", "«the face of» — the deputy fa'il.", "«yüzü» — nâib-i fâil."),
  tok("الشَّبَهِ","shabah","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness».", "«benzerliğin»."),
  tok("مِنَ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ، حُرِّكَ بِالْفَتْحِ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«from» — its nun takes a fatha before the article.", "«-den» — nûnu harf-i tarif önünde fetha alır."),
  tok("الْمِصْرَاعِ","misra","noun",[Q,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the hemistich» — one half of the bayt.", "«mısra» — beytin yarısı."),
  tok("الْأَوَّلِ","awwal","noun",[Q,"naat-sifa"], "نَعْتٌ مَجْرُورٌ.", "«the first» — na't.", "«ilk» — sıfat."),
  tok("وَحْدَهُ","wahda","noun",[Q,"hal"],
      "حَالٌ مَنْصُوبٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — وَحْدَهُ لَا يَكُونُ إِلَّا حَالًا: مُنْفَرِدًا.",
      "«alone» — always a HAL (= by itself), annexed to its pronoun; the case-writer knows the word for what it is.",
      "«tek başına» — daima HÂL (= yalnız olarak), zamirine muzâf; hareke yazıcısı kelimeyi tanır.",
      segments=[seg("وَحْدَ","wahda","noun"), seg("هُ","pron-3ms","pron")], punct="،"),
  tok("وَالْوَاجِبُ","wajib","noun",[Q,"mubtada-khabar","ism-fail"],
      "الْوَاوُ عَاطِفَةٌ، وَالْوَاجِبُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and what is required» — a second mubtada.", "«vâcib olan» — ikinci mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْوَاجِبُ","wajib","noun")]),
  tok("انْتِزَاعُهُ","intiza","noun",[Q,"mubtada-khabar","masdar","form-viii-verbs"],
      "خَبَرٌ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ انْتَزَعَ مُضَافٌ إِلَى مَفْعُولِهِ.",
      "«to draw it» — the khabar; the masdar of Form VIII annexed to its object.",
      "«onu çıkarmak» — haber; VIII. bâbın masdarı mef'ûlüne muzâf.",
      segments=[seg("انْتِزَاعُ","intiza","noun"), seg("هُ","pron-3ms","pron")]),
  tok("مِنَ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("الْبَيْتِ","bayt","noun",[Q,"huruf-jarr"], "اسْمٌ مَجْرُورٌ.", "«the bayt» — the verse-line.", "«beyit»."),
  tok("كُلِّهِ","kull","noun",[Q,"tawkid"],
      "تَوْكِيدٌ مَعْنَوِيٌّ مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.",
      "«the whole of it» — the tawkid of totality, matching the bayt in jarr.",
      "«bütünü» — mânevî te'kid, beyte cerde uyar.",
      segments=[seg("كُلِّ","kull","noun"), seg("هِ","pron-3ms","pron")], punct=".")]})

# ----------- s18 — the several and sensory (RESTORED)
S.append({"id": "s18", "translation": {
 "en": "The several-and-sensory: for instance colour, taste and scent, in likening one fruit to another." + R_EN,
 "tr": "Müteaddid hissî: meselâ bir meyveyi diğerine benzetmede renk, tat ve koku." + R_TR},
 "tashbih": frame([7], 6, [8], [2, 3, 4], "mursal-mufassal", "mufrad", "mufrad", "mutaaddid"),
 "tokens": [
  tok("وَالْمُتَعَدِّدُ","mutaaddid","noun",[Q,"mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْمُتَعَدِّدُ مُبْتَدَأٌ.", "«the several» — the mubtada.", "«müteaddid» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَعَدِّدُ","mutaaddid","noun")]),
  tok("الْحِسِّيُّ","hissi","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«sensory» — na't.", "«hissî» — sıfat."),
  tok("كَاللَّوْنِ","lawn","noun",[Q,W,"huruf-jarr"],
      "الْكَافُ لِلتَّمْثِيلِ، وَاللَّوْنِ مَجْرُورٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ. وَهُوَ أَوَّلُ الْوَجْهِ الْمُتَعَدِّدِ.",
      "«for instance colour» — the kaf of example; the first of a SEVERAL wajh, spoken before the masdar.",
      "«meselâ renk» — örnek kâfı; MÜTEADDİD vechin ilki, masdardan önce söylenmiş.",
      segments=[seg("كَ","ka","part"), seg("اللَّوْنِ","lawn","noun")]),
  tok("وَالطَّعْمِ","tam-taste","noun",[Q,W,"atf-nasaq"], "مَعْطُوفٌ مَجْرُورٌ.", "«and taste» — joined: the second quality.", "«ve tat» — atıf: ikinci vasıf.",
      segments=[seg("وَ","wa","conj"), seg("الطَّعْمِ","tam-taste","noun")]),
  tok("وَالرَّائِحَةِ","raiha","noun",[Q,W,"atf-nasaq"],
      "مَعْطُوفٌ مَجْرُورٌ — ثَلَاثُ صِفَاتٍ كُلُّهَا حِسِّيَّةٌ، وَلَا هَيْئَةَ.",
      "«and scent» — joined: three qualities, each sensory and each on its own — SEVERAL, not a picture.",
      "«ve koku» — atıf: üç vasıf, her biri hissî ve her biri kendi başına — MÜTEADDİD, tablo değil.",
      segments=[seg("وَ","wa","conj"), seg("الرَّائِحَةِ","raiha","noun")]),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("تَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — مَصْدَرٌ عَامِلٌ، الْأَدَاةُ.", "«the likening of» — the masdar-adat.", "«benzetmesinde» — masdar-edat."),
  tok("فَاكِهَةٍ","fakiha","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«a fruit» — the mushabbah.", "«bir meyveyi» — müşebbeh."),
  tok("بِأُخْرَى","ukhra","noun",[Q,A,"huruf-jarr","ism-maqsur-manqus","mamnu-min-sarf"],
      "الْبَاءُ جَارَّةٌ وَأُخْرَى مَجْرُورٌ بِفَتْحَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ مَقْصُورٌ — الْمُشَبَّهُ بِهِ.",
      "«to another» — the bihi; أُخْرَى is a maqsur diptote (the feminine of آخَر): its jarr is a supposed fatha.",
      "«diğerine» — bih; أُخْرَى maksûr ve gayr-i munsarif (آخَر'in müennesi): cerri takdîrî fethadır.",
      segments=[seg("بِ","bi","part"), seg("أُخْرَى","ukhra","noun")], punct=".")]})

# ----------- s19 — the several and mental (RESTORED)
S.append({"id": "s19", "translation": {
 "en": "The several-and-mental: for instance keenness of sight, perfect wariness and the hiding of mating, in likening a bird to the raven." + R_EN,
 "tr": "Müteaddid aklî: meselâ bir kuşu kargaya benzetmede bakışın keskinliği, tam ihtiyat ve çiftleşmeyi gizlemek." + R_TR},
 "tashbih": frame([10], 9, [11], [2, 3, 4, 5, 6, 7], "mursal-mufassal", "mufrad", "mufrad", "mutaaddid"),
 "tokens": [
  tok("وَالْمُتَعَدِّدُ","mutaaddid","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the several» — the mubtada.", "«müteaddid» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُتَعَدِّدُ","mutaaddid","noun")]),
  tok("الْعَقْلِيُّ","aqli","noun",[Q,"naat-sifa"], "نَعْتٌ مَرْفُوعٌ.", "«mental» — na't.", "«aklî» — sıfat."),
  tok("كَحِدَّةِ","hidda","noun",[Q,W,"huruf-jarr","idafa-definiteness"],
      "الْكَافُ لِلتَّمْثِيلِ، وَحِدَّةِ مَجْرُورٌ مُضَافٌ — أَوَّلُ الْوَجْهِ.",
      "«for instance keenness of» — the kaf of example; the first quality, an idafa.", "«meselâ keskinliği» — örnek kâfı; ilk vasıf, izâfet.",
      segments=[seg("كَ","ka","part"), seg("حِدَّةِ","hidda","noun")]),
  tok("النَّظَرِ","nazar","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«sight».", "«bakışın»."),
  tok("وَكَمَالِ","kamal","noun",[Q,W,"atf-nasaq","idafa-definiteness"], "مَعْطُوفٌ مَجْرُورٌ مُضَافٌ.", "«and perfection of» — the second.", "«ve tamlığı» — ikincisi.",
      segments=[seg("وَ","wa","conj"), seg("كَمَالِ","kamal","noun")]),
  tok("الْحَذَرِ","hadhar","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«wariness».", "«ihtiyatın»."),
  tok("وَإِخْفَاءِ","ikhfa","noun",[Q,W,"atf-nasaq","idafa-definiteness","masdar","form-iv-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ مُضَافٌ — مَصْدَرُ أَخْفَى.", "«and the hiding of» — the third; the masdar of Form IV.", "«ve gizlemesi» — üçüncüsü; IV. bâbın masdarı.",
      segments=[seg("وَ","wa","conj"), seg("إِخْفَاءِ","ikhfa","noun")]),
  tok("السِّفَادِ","sifad","noun",[Q,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ثَلَاثُ صِفَاتٍ كُلُّهَا عَقْلِيَّةٌ.",
      "«mating» — three qualities, each of the mind (the raven is said to hide its mating).",
      "«çiftleşmeyi» — üç vasıf, hepsi aklî (karganın çiftleşmesini gizlediği söylenir)."),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("تَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"], "اسْمٌ مَجْرُورٌ مُضَافٌ — الْأَدَاةُ.", "«the likening of» — the adat.", "«benzetmesinde» — edat."),
  tok("طَائِرٍ","tair","noun",[Q,A,"idafa-definiteness","ism-fail"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«a bird» — the mushabbah.", "«bir kuşu» — müşebbeh."),
  tok("بِالْغُرَابِ","ghurab","noun",[Q,A,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَالْغُرَابِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to the raven» — the bihi.", "«kargaya» — bih.",
      segments=[seg("بِ","bi","part"), seg("الْغُرَابِ","ghurab","noun")], punct=".")]})

# ----------- s20 — the several and mixed (RESTORED)
S.append({"id": "s20", "translation": {
 "en": "The mixed: for instance beauty of face and eminence of standing, in likening a person to the sun." + R_EN,
 "tr": "Muhtelif: meselâ bir insanı güneşe benzetmede yüz güzelliği ve şanın yüceliği." + R_TR},
 "tashbih": frame([7], 6, [8], [1, 2, 3, 4], "mursal-mufassal", "mufrad", "mufrad", "mutaaddid"),
 "tokens": [
  tok("وَالْمُخْتَلِفُ","mukhtalif","noun",[Q,"mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the mixed» — the mubtada.", "«muhtelif» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْمُخْتَلِفُ","mukhtalif","noun")]),
  tok("كَحُسْنِ","husn","noun",[Q,W,"huruf-jarr","idafa-definiteness"],
      "الْكَافُ لِلتَّمْثِيلِ، وَحُسْنِ مَجْرُورٌ مُضَافٌ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.",
      "«for instance beauty of» — the kaf of example; the phrase is the khabar of الْمُخْتَلِفُ, so the joined noun after it rides the same kaf.",
      "«meselâ güzelliği» — örnek kâfı; tamlama الْمُخْتَلِفُ'un haberidir, ardındaki atıf aynı kâfa biner.",
      segments=[seg("كَ","ka","part"), seg("حُسْنِ","husn","noun")]),
  tok("الطَّلْعَةِ","tala","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — حِسِّيٌّ.", "«the face» — sensory.", "«yüzün» — hissî."),
  tok("وَنَبَاهَةِ","nabaha","noun",[Q,W,"atf-nasaq","idafa-definiteness"],
      "مَعْطُوفٌ عَلَى حُسْنِ مَجْرُورٌ مُضَافٌ — لَا خَبَرٌ ثَانٍ.",
      "«and eminence of» — joined to حُسْنِ in jarr, not a new khabar.", "«ve yüceliği» — حُسْنِ'e cerde atıf, yeni haber değil.",
      segments=[seg("وَ","wa","conj"), seg("نَبَاهَةِ","nabaha","noun")]),
  tok("الشَّأْنِ","shan","noun",[Q,"idafa-definiteness"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — عَقْلِيٌّ: فَالْوَجْهُ مُخْتَلِفٌ.",
      "«standing» — of the mind: one quality sensed, one thought — the wajh is MIXED.",
      "«şanın» — aklî: bir vasıf duyulan, biri düşünülen — vech MUHTELİFtir."),
  tok("فِي","fi","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de»."),
  tok("تَشْبِيهِ","tashbih","noun",[Q,A,"huruf-jarr","idafa-definiteness","imal-al-masdar"], "اسْمٌ مَجْرُورٌ مُضَافٌ — الْأَدَاةُ.", "«the likening of» — the adat.", "«benzetmesinde» — edat."),
  tok("إِنْسَانٍ","insan","noun",[Q,A,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْمُشَبَّهُ.", "«a person» — the mushabbah.", "«bir insanı» — müşebbeh."),
  tok("بِالشَّمْسِ","shams","noun",[Q,A,"huruf-jarr"], "الْبَاءُ جَارَّةٌ وَالشَّمْسِ مَجْرُورٌ — الْمُشَبَّهُ بِهِ.", "«to the sun» — the bihi.", "«güneşe» — bih.",
      segments=[seg("بِ","bi","part"), seg("الشَّمْسِ","shams","noun")], punct=".")]})

# ----------- s21 — the wajh drawn from OPPOSITION (RESTORED)
S.append({"id": "s21", "translation": {
 "en": "And the wajh al-shabah may be drawn from opposition itself, and then brought down to the rank of proportion by way of pleasantry or mockery." + R_EN,
 "tr": "Vech-i şebeh bazen tezâdın kendisinden çıkarılır; sonra temlîh yahut tehekküm yoluyla tenâsüb mertebesine indirilir." + R_TR},
 "tokens": [
  tok("وَقَدْ","qad","part",[Q,"qad-harf"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَقَدْ لِلتَّقْلِيلِ مَعَ الْمُضَارِعِ.", "«and sometimes».", "«ve bazen».",
      segments=[seg("وَ","wa","conj"), seg("قَدْ","qad","part")]),
  tok("يُنْتَزَعُ","intazaa","verb",[Q,"naib-al-fail","form-viii-verbs","mudari-marfu"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ.", "«is drawn» — Form VIII majhul.", "«çıkarılır» — VIII. bâb meçhul."),
  tok("وَجْهُ","wajh","noun",[Q,"naib-al-fail","idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ مُضَافٌ.", "«the face of» — the deputy fa'il.", "«yüzü» — nâib-i fâil."),
  tok("الشَّبَهِ","shabah","noun",[Q,"idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the likeness».", "«benzerliğin»."),
  tok("مِنْ","min","part",[Q,"huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("نَفْسِ","nafs","noun",[Q,"huruf-jarr","idafa-definiteness"],
      "اسْمٌ مَجْرُورٌ مُضَافٌ — نَفْسِ هُنَا لِلتَّوْكِيدِ الْمَعْنَوِيِّ مُقَدَّمَةً: التَّضَادِّ نَفْسِهِ.",
      "«the very» — نَفْس put before its noun: opposition ITSELF (the emphasis word turned mudaf).",
      "«bizzat» — isminin önüne alınmış نَفْس: tezâdın KENDİSİ (te'kid kelimesi muzâf olmuş)."),
  tok("التَّضَادِّ","tadadd","noun",[Q,"idafa-definiteness","masdar","form-vi-verbs","doubled-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَضَادَّ، مُضَاعَفٌ.",
      "«opposition» — the masdar of Form VI, geminate (تَضَادَدَ → تَضَادَّ).", "«tezâd» — VI. bâbın masdarı, muzâaf (تَضَادَدَ → تَضَادَّ).",
      punct="،"),
  tok("ثُمَّ","thumma","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّرْتِيبِ.", "«then».", "«sonra»."),
  tok("يُنَزَّلُ","nazzala","verb",[Q,"naib-al-fail","form-ii-verbs"],
      "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ (الْوَجْهُ).",
      "«is brought down» — Form II majhul; the deputy hidden (the wajh).", "«indirilir» — II. bâb meçhul; nâib gizli (vech)."),
  tok("مَنْزِلَةَ","manzila","noun",[Q,"maful-mutlaq","idafa-definiteness"],
      "مَنْصُوبٌ عَلَى الْمَصْدَرِيَّةِ — مَفْعُولٌ مُطْلَقٌ مِنْ غَيْرِ لَفْظِ الْفِعْلِ، وَهُوَ مُضَافٌ: يُنَزَّلُ تَنْزِيلَ الْمَنْزِلَةِ.",
      "«to the rank of» — in nasb on the seat of the masdar (a maf'ul mutlaq of kindred meaning), annexed. NOT a likeness: the engine refuses the maf'ul-mutlaq frame when the mudaf ilayh is itself a masdar.",
      "«mertebesine» — masdar mevkiinde mansub (mânâca yakın mef'ûl-i mutlak), muzâf. Benzetme DEĞİL: muzâfun ileyh de masdar olunca motor mef'ûl-i mutlak çerçevesini reddeder."),
  tok("التَّنَاسُبِ","tanasub","noun",[Q,"idafa-definiteness","masdar","form-vi-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ تَنَاسَبَ.", "«proportion» — the masdar of Form VI.", "«tenâsüb» — VI. bâbın masdarı."),
  tok("بِوَاسِطَةِ","wasita","noun",[Q,"huruf-jarr","idafa-definiteness"],
      "الْبَاءُ جَارَّةٌ وَوَاسِطَةِ مَجْرُورٌ مُضَافٌ.", "«by way of» — the means.", "«vasıtasıyla» — vesile.",
      segments=[seg("بِ","bi","part"), seg("وَاسِطَةِ","wasita","noun")]),
  tok("تَمْلِيحٍ","tamlih","noun",[Q,"idafa-definiteness","masdar","form-ii-verbs"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ مَلَّحَ: جَعْلُ الْكَلَامِ مَلِيحًا.", "«pleasantry» — the masdar of Form II: making the speech charming.", "«temlîh» — II. bâbın masdarı: sözü hoşlaştırma."),
  tok("أَوْ","aw","conj",[Q,"atf-nasaq"], "حَرْفُ عَطْفٍ.", "«or».", "«yahut»."),
  tok("تَهَكُّمٍ","tahakkum","noun",[Q,"atf-nasaq","masdar","form-v-verbs"],
      "مَعْطُوفٌ مَجْرُورٌ — مَصْدَرُ تَهَكَّمَ: السُّخْرِيَةُ.", "«mockery» — the masdar of Form V: saying the opposite to deride.", "«tehekküm» — V. bâbın masdarı: alay için tersini söylemek.",
      punct=".")]})

# ----------- s22 — the two sayings (as printed; خَاتِمٌ → حَاتِمٌ)
S.append({"id": "s22", "translation": {
 "en": "So it is said of the coward: «How like the lion he is!» — and of the miser: «He is Hatim.» (The frame of the sayings is restored; the sayings are as printed.)",
 "tr": "Korkağa «Arslana ne kadar da benziyor!», cimriye «O Hâtim'dir» denir. (Çerçeve cümlesi geri yazımdır; sözler basıldığı gibidir.)"},
 "tashbih": {"mushabbah": [], "adat": 3, "bihi": [4], "wajh": [], "kind": "mursal-mujmal",
             "shape": {"mushabbah": None, "bihi": "mufrad", "wajh": None}},
 "tokens": [
  tok("فَيُقَالُ","qala","verb",[Q,"naib-al-fail","hollow-verbs"],
      "الْفَاءُ لِلتَّفْرِيعِ، وَيُقَالُ فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَرْفُوعٌ — وَنَائِبُ الْفَاعِلِ الْجُمْلَةُ الْمَقُولَةُ.",
      "«so it is said» — the hollow majhul (قِيلَ / يُقَالُ); the quoted sentence is its deputy.",
      "«denir» — ecvef meçhul (قِيلَ / يُقَالُ); nakledilen cümle nâibidir.",
      segments=[seg("فَ","fa","conj"), seg("يُقَالُ","qala","verb")]),
  tok("لِلْجَبَانِ","jaban","noun",[Q,"huruf-jarr"],
      "اللَّامُ جَارَّةٌ وَالْجَبَانِ مَجْرُورٌ مُتَعَلِّقٌ بِيُقَالُ.", "«of the coward» — to whom it is said.", "«korkağa» — kime dendiği.",
      segments=[seg("لِ","li","part"), seg("الْجَبَانِ","jaban","noun")], punct=":"),
  tok("مَا","ma-taajjubiyya","pron",[Q,A,"mubtada-khabar"],
      "مَا التَّعَجُّبِيَّةُ: نَكِرَةٌ تَامَّةٌ بِمَعْنَى شَيْءٍ، مَبْنِيَّةٌ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«how…!» — the مَا of WONDER: an indefinite meaning «something», the mubtada; the verb after it is its khabar.",
      "«ne kadar…!» — TAACCÜB مَا'sı: «bir şey» mânâsında nekre, mübtedâ; ardındaki fiil haberidir."),
  tok("أَشْبَهَهُ","ashbaha","verb",[Q,A,"form-iv-verbs","maful-bihi","tashbih"],
      "فِعْلُ التَّعَجُّبِ مَاضٍ جَامِدٌ، وَالْفَاعِلُ مُسْتَتِرٌ يَعُودُ إِلَى مَا، وَالْهَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرُ مَا. وَالْفِعْلُ أَدَاةُ التَّشْبِيهِ، وَالْهَاءُ الْمُشَبَّهُ.",
      "«…like him» — the frozen verb of wonder (Form IV of شَبَهَ); its hidden fa'il returns to مَا, the ha is its object. The VERB is the adat, the pronoun the mushabbah (the coward).",
      "«…benzetti» — donmuş taaccüb fiili (شَبَهَ'nin IV. bâbı); gizli fâili مَا'ya döner, hâ mef'ûlü. FİİL edat, zamir müşebbeh (korkak).",
      segments=[seg("أَشْبَهَ","ashbaha","verb"), seg("هُ","pron-3ms","pron")]),
  tok("بِالْأَسَدِ","asad","noun",[Q,A,"huruf-jarr"],
      "الْبَاءُ جَارَّةٌ وَالْأَسَدِ مَجْرُورٌ مُتَعَلِّقٌ بِأَشْبَهَ — الْمُشَبَّهُ بِهِ: تَهَكُّمٌ، فَالْوَجْهُ التَّضَادُّ.",
      "«to the lion» — the bihi. The likening is MOCKERY: coward and lion share only their opposition, brought down to proportion.",
      "«arslana» — bih. Benzetme TEHEKKÜMdür: korkakla arslan yalnız tezâdda ortaktır; tenâsüb mertebesine indirilmiş.",
      segments=[seg("بِ","bi","part"), seg("الْأَسَدِ","asad","noun")], punct="،"),
  tok("وَلِلْبَخِيلِ","bakhil","noun",[Q,"atf-nasaq","huruf-jarr"],
      "الْوَاوُ عَاطِفَةٌ، وَاللَّامُ جَارَّةٌ وَالْبَخِيلِ مَجْرُورٌ — مَعْطُوفٌ عَلَى لِلْجَبَانِ.",
      "«and of the miser».", "«ve cimriye».",
      segments=[seg("وَ","wa","conj"), seg("لِ","li","part"), seg("الْبَخِيلِ","bakhil","noun")], punct=":"),
  tok("هُوَ","huwa","pron",[Q,A,"mubtada-khabar"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ — الْمُشَبَّهُ.",
      "«he» — the mubtada: the MUSHABBAH (the miser).", "«o» — mübtedâ: MÜŞEBBEH (cimri)."),
  tok("حَاتِمٌ","hatim","noun",[Q,A,"mubtada-khabar","tashbih"],
      "خَبَرٌ مَرْفُوعٌ — حَاتِمٌ الطَّائِيُّ، عَلَمُ الْجُودِ؛ تَشْبِيهٌ بَلِيغٌ عَلَى التَّهَكُّمِ. (يَكْتُبُهُ الْمَصْدَرُ خَاتِمٌ.)",
      "«Hatim» — the khabar: Hatim al-Ta'i, generosity's proverb, with no adat — a BALIGH likening by mockery (the source spells the name خَاتِمٌ).",
      "«Hâtim» — haber: cömertliğin darb-ı meseli Hâtim-i Tâî, edatsız — tehekkümle BELÎĞ teşbih (kaynak adı خَاتِمٌ yazar).",
      punct=".")],
 "jumal": [J("مَا أَشْبَهَهُ بِالْأَسَدِ", "جُمْلَةٌ اسْمِيَّةٌ فِي مَحَلِّ رَفْعٍ نَائِبُ فَاعِلٍ لِيُقَالُ.",
             "The quoted sentence is the deputy fa'il of يُقَالُ; the wonder-verb inside it is the engine's adat, its pronoun the mushabbah.",
             "Nakledilen cümle يُقَالُ'nun nâib-i fâilidir; içindeki taaccüb fiili motorun edatı, zamiri müşebbehtir."),
           J("هُوَ حَاتِمٌ", "جُمْلَةٌ اسْمِيَّةٌ مَقُولَةٌ — تَشْبِيهٌ بَلِيغٌ.",
             "A second likening in the same sentence, read after the first is closed: the two are MAFRUQ, each end with its own bihi.",
             "Aynı cümlede ikinci benzetme, ilki kapandıktan sonra okunur: ikisi MEFRÛKtur, her tarafın kendi bihi.")]})

# ---------------------------------------------------------------- glossary
def find_gloss(key):
    for p in sorted((ROOT / "content/samples").iterdir()):
        gp = p / "glossary.json"
        if gp.exists():
            d = json.loads(gp.read_text(encoding="utf-8"))["entries"]
            if key in d: return d[key]
    raise KeyError(key)
GLOSS_ADD = {
 "saba-seven": g("سَبْعَة", "س ب ع", "noun", "seven (with the ta before a masculine counted noun)", "yedi (müzekker sayılan önünde tâ ile)", 2),
 "aamm": g("أَعَمّ", "ع م م", "noun", "more general (ism tafdil of عَامّ; diptote)", "daha umumî (عَامّ'ın ism-i tafdili; gayr-i munsarif)", 4),
 "humra": g("حُمْرَة", "ح م ر", "noun", "redness", "kızıllık", 3),
 "raiha": g("رَائِحَة", "ر و ح", "noun", "scent, smell", "koku", 2, plural="رَوَائِح"),
 "ladhdha": g("لَذَّة", "ل ذ ذ", "noun", "pleasure, delight", "lezzet", 3, plural="لَذَّات"),
 "lin": g("لِين", "ل ي ن", "noun", "softness", "yumuşaklık", 3),
 "jura": g("جُرْأَة", "ج ر أ", "noun", "boldness, daring", "cür'et, cesaret", 4),
 "hidaya": g("هِدَايَة", "ه د ي", "noun", "guidance", "hidâyet", 2),
 "subh": g("صُبْح", "ص ب ح", "noun", "dawn, morning", "sabah", 1),
 "thurayya": g("الثُّرَيَّا", "ث ر و", "propn", "the Pleiades (maqsur; a proper noun)", "Süreyya, Ülker yıldızı (maksûr; alem)", 5),
 "unqud": g("عُنْقُود", "ع ن ق د", "noun", "a cluster (of grapes)", "salkım", 4, plural="عَنَاقِيد"),
 "mullahiyya": g("مُلَّاحِيَّة", "م ل ح", "noun", "a white long-berried grape (nisba)", "beyaz uzun taneli bir üzüm (nisbet)", 6),
 "taqarub": g("تَقَارُب", "ق ر ب", "noun", "nearness to one another (masdar of تَقَارَبَ)", "birbirine yaklaşma (تَقَارَبَ'nin masdarı)", 4),
 "mustadir": g("مُسْتَدِير", "د و ر", "noun", "round, circular (ism fa'il of اسْتَدَارَ)", "yuvarlak, dairevî (اسْتَدَارَ'nin ism-i fâili)", 4),
 "muthar": g("مُثَار", "ث و ر", "noun", "raised, stirred up (ism maf'ul of أَثَارَ)", "kaldırılan, kaldırılmış (أَثَارَ'nin ism-i mef'ûlü)", 5),
 "naq": g("نَقْع", "ن ق ع", "noun", "dust (raised by hooves)", "toz (nal tozu)", 5),
 "sayf": g("سَيْف", "س ي ف", "noun", "sword", "kılıç", 1, plural="أَسْيَاف"),
 "kawkab": g("كَوْكَب", "ك و ك ب", "noun", "star, planet", "yıldız, gezegen", 2, plural="كَوَاكِب"),
 "qanis": g("قَانِص", "ق ن ص", "noun", "hunter (ism fa'il of قَنَصَ)", "avcı (قَنَصَ'nin ism-i fâili)", 4),
 "mirat": g("مِرْآة", "ر أ ي", "noun", "mirror (ism ala: مِرْأَاة → مِرْآة)", "ayna (ism-i âlet: مِرْأَاة → مِرْآة)", 3, plural="مَرَايَا"),
 "ashall": g("أَشَلّ", "ش ل ل", "noun", "palsied, with a withered or shaking hand (an أَفْعَل of defect; diptote)", "eli tutmaz, titrek elli (kusur أَفْعَل'i; gayr-i munsarif)", 5),
 "barq": g("بَرْق", "ب ر ق", "noun", "lightning", "şimşek", 2, plural="بُرُوق"),
 "qari": g("قَارٍ (الْقَارِي)", "ق ر أ", "noun", "a reciter, reader (manqus; from قَارِئ)", "okuyucu, kāri (mankûs; aslı قَارِئ)", 4),
 "intibaq": g("انْطِبَاق", "ط ب ق", "noun", "closing shut (masdar of انْطَبَقَ)", "kapanma (انْطَبَقَ'nin masdarı)", 5),
 "marra-once": g("مَرَّة", "م ر ر", "noun", "a time, once; مَرَّةً … وَمَرَّةً: now … now", "kez, defa; مَرَّةً … وَمَرَّةً: bir … bir", 2, plural="مَرَّات"),
 "infitah": g("انْفِتَاح", "ف ت ح", "noun", "opening up (masdar of انْفَتَحَ)", "açılma (انْفَتَحَ'nin masdarı)", 4),
 "julus": g("جُلُوس", "ج ل س", "noun", "sitting; the manner of sitting (masdar of جَلَسَ)", "oturuş, oturma (جَلَسَ'nin masdarı)", 2),
 "badawi": g("بَدَوِيّ", "ب د و", "noun", "bedouin (nisba to الْبَدْو)", "bedevî (الْبَدْو'e nisbet)", 3),
 "mustali": g("مُصْطَلٍ (الْمُصْطَلِي)", "ص ل ي", "noun", "one warming himself at a fire (ism fa'il of اصْطَلَى; manqus)", "ateşte ısınan (اصْطَلَى'nın ism-i fâili; mankûs)", 6),
 "arba": g("أَرْبَع", "ر ب ع", "noun", "four (without the ta: before a feminine counted noun)", "dört (tâsız: müennes sayılan önünde)", 2),
 "majdul": g("مَجْدُول", "ج د ل", "noun", "tightly twisted, firmly braided (ism maf'ul of جَدَلَ)", "sıkı bükülmüş, örülü (جَدَلَ'nin ism-i mef'ûlü)", 5),
 "mathal": g("مَثَل", "م ث ل", "noun", "likeness; a state or condition (as in the Qur'anic مَثَلُ الَّذِينَ)", "misal, durum, hâl (Kur'ân'daki مَثَلُ الَّذِينَ gibi)", 3, plural="أَمْثَال"),
 "tawrat": g("التَّوْرَاة", None, "noun", "the Torah", "Tevrat", 3),
 "himar": g("حِمَار", "ح م ر", "noun", "donkey", "eşek", 1, plural="حُمُر"),
 "sifr": g("سِفْر", "س ف ر", "noun", "a great book, a volume", "büyük kitap, cilt", 4, plural="أَسْفَار"),
 "taraf": g("طَرَف", "ط ر ف", "noun", "end, side; one of the two ends of a tashbih", "taraf, uç; teşbihin iki tarafından biri", 3, plural="أَطْرَاف"),
 "tabassum": g("تَبَسُّم", "ب س م", "noun", "smiling (masdar of تَبَسَّمَ)", "tebessüm (تَبَسَّمَ'nin masdarı)", 3),
 "atshan": g("عَطْشَان", "ع ط ش", "noun", "thirsty (diptote)", "susuz (gayr-i munsarif)", 3, plural="عِطَاش"),
 "ghamama": g("غَمَامَة", "غ م م", "noun", "a cloud", "bulut", 3, plural="غَمَام"),
 "khata": g("خَطَأ", "خ ط أ", "noun", "error, mistake", "hata", 2, plural="أَخْطَاء"),
 "misra": g("مِصْرَاع", "ص ر ع", "noun", "hemistich, half of a bayt", "mısra, beytin yarısı", 4, plural="مَصَارِيع"),
 "wahda": g("وَحْد", "و ح د", "noun", "alone, by itself (always a hal: وَحْدَهُ)", "tek başına (daima hâl: وَحْدَهُ)", 3),
 "intiza": g("انْتِزَاع", "ن ز ع", "noun", "drawing out, extracting (masdar of انْتَزَعَ)", "çıkarma, çekip alma (انْتَزَعَ'nin masdarı)", 5),
 "lawn": g("لَوْن", "ل و ن", "noun", "colour", "renk", 1, plural="أَلْوَان"),
 "tam-taste": g("طَعْم", "ط ع م", "noun", "taste, flavour", "tat", 2, plural="طُعُوم"),
 "fakiha": g("فَاكِهَة", "ف ك ه", "noun", "fruit", "meyve", 1, plural="فَوَاكِه"),
 "hidda": g("حِدَّة", "ح د د", "noun", "keenness, sharpness", "keskinlik", 4),
 "hadhar": g("حَذَر", "ح ذ ر", "noun", "wariness, caution", "ihtiyat, sakınma", 3),
 "ikhfa": g("إِخْفَاء", "خ ف ي", "noun", "hiding, concealing (masdar of أَخْفَى)", "gizleme (أَخْفَى'nın masdarı)", 4),
 "sifad": g("سِفَاد", "س ف د", "noun", "mating (of animals)", "çiftleşme (hayvanlarda)", 6),
 "tair": g("طَائِر", "ط ي ر", "noun", "bird (ism fa'il of طَارَ)", "kuş (طَارَ'nın ism-i fâili)", 2, plural="طُيُور"),
 "ghurab": g("غُرَاب", "غ ر ب", "noun", "raven, crow", "karga", 2, plural="غِرْبَان"),
 "tala": g("طَلْعَة", "ط ل ع", "noun", "face, aspect, appearance", "yüz, görünüş", 4),
 "nabaha": g("نَبَاهَة", "ن ب ه", "noun", "eminence, distinction", "yücelik, şöhret", 5),
 "shan": g("شَأْن", "ش أ ن", "noun", "standing, matter, affair", "şan, iş, durum", 3, plural="شُؤُون"),
 "tadadd": g("تَضَادّ", "ض د د", "noun", "opposition, contrariety (masdar of تَضَادَّ)", "tezâd (تَضَادَّ'nin masdarı)", 4),
 "tanasub": g("تَنَاسُب", "ن س ب", "noun", "proportion, fitting together (masdar of تَنَاسَبَ)", "tenâsüb, uygunluk (تَنَاسَبَ'nin masdarı)", 4),
 "wasita": g("وَاسِطَة", "و س ط", "noun", "means, medium; بِوَاسِطَةِ: by way of", "vasıta; بِوَاسِطَةِ: yoluyla", 3),
 "tamlih": g("تَمْلِيح", "م ل ح", "noun", "pleasantry — making speech charming (masdar of مَلَّحَ)", "temlîh — sözü hoşlaştırma (مَلَّحَ'nin masdarı)", 6),
 "tahakkum": g("تَهَكُّم", "ه ك م", "noun", "mockery — saying the opposite to deride (masdar of تَهَكَّمَ)", "tehekküm — alay için tersini söyleme (تَهَكَّمَ'nin masdarı)", 6),
 "jaban": g("جَبَان", "ج ب ن", "noun", "coward", "korkak", 3, plural="جُبَنَاء"),
 "hatim": g("حَاتِم", "ح ت م", "propn", "Hatim (al-Ta'i), the proverb of generosity", "Hâtim (-i Tâî), cömertliğin darb-ı meseli", 4),
 "ma-taajjubiyya": g("مَا (التَّعَجُّبِيَّة)", None, "pron", "the ma of wonder: مَا أَحْسَنَهُ «how fine he is!»", "taaccüb mâ'sı: مَا أَحْسَنَهُ «ne güzeldir!»", 4),
 "nawwara": g("نَوَّرَ", "ن و ر", "verb", "to blossom; to light up (Form II)", "çiçek açmak; aydınlatmak (II. bâb)", 3, form="II"),
 "tahawa": g("تَهَاوَى", "ه و ي", "verb", "to fall one after another, tumble down (Form VI)", "birbiri ardınca düşmek (VI. bâb)", 5, form="VI"),
 "sabba": g("صَبَّ", "ص ب ب", "verb", "to pour; صَبَّ عَلَيْهِ: to loose (a dog) upon (geminate)", "dökmek; صَبَّ عَلَيْهِ: (köpeği) üzerine salmak (muzâaf)", 3, form="I"),
 "ghafala": g("غَفَلَ", "غ ف ل", "verb", "to be heedless, unaware", "gaflete düşmek, farkında olmamak", 3, form="I"),
 "aqa": g("أَقْعَى", "ق ع و", "verb", "to squat on the haunches (of a dog) (Form IV)", "kıç üstü oturmak, çömelmek (köpek) (IV. bâb)", 6, form="IV"),
 "jadala-braid": g("جَدَلَ", "ج د ل", "verb", "to twist (a rope) tight, to braid", "(ipi) sıkı bükmek, örmek", 4, form="I"),
 "hammala": g("حَمَّلَ", "ح م ل", "verb", "to make someone carry, to load (Form II; two objects)", "yüklemek, taşıtmak (II. bâb; iki mef'ûl)", 3, form="II"),
 "atmaa": g("أَطْمَعَ", "ط م ع", "verb", "to make someone hope, to tempt (Form IV)", "umutlandırmak, tamah ettirmek (IV. bâb)", 4, form="IV"),
 "arada-away": g("أَعْرَضَ", "ع ر ض", "verb", "to turn away (Form IV)", "yüz çevirmek (IV. bâb)", 3, form="IV"),
 "tawalla": g("تَوَلَّى", "و ل ي", "verb", "to turn one's back, go away (Form V)", "arkasını dönmek, gitmek (V. bâb)", 3, form="V"),
 "abraqa": g("أَبْرَقَ", "ب ر ق", "verb", "to flash lightning (Form IV)", "şimşek çakmak (IV. bâb)", 4, form="IV"),
 "aqshaa": g("أَقْشَعَ", "ق ش ع", "verb", "to break up, disperse (of clouds) (Form IV)", "dağılmak (bulut) (IV. bâb)", 6, form="IV"),
 "intazaa": g("انْتَزَعَ", "ن ز ع", "verb", "to draw out, extract (Form VIII)", "çıkarmak, çekip almak (VIII. bâb)", 4, form="VIII"),
 "tajalla": find_gloss("tajalla"),
 "ashbaha": find_gloss("ashbaha"),
 "khafaa": find_gloss("khafaa"),
 "tib": find_gloss("tib"),
 "saghir": find_gloss("saghir"),
 "fawqa": find_gloss("fawqa"),
 "layl": find_gloss("layl"),
 "kaff": find_gloss("kaff"),
 "mushaf": find_gloss("mushaf"),
 "wisal": find_gloss("wisal"),
 "wajib": find_gloss("wajib"),
 "kamal": find_gloss("kamal"),
 "bakhil": find_gloss("bakhil"),
 "aqsam": find_gloss("aqsam"),
}
if "plural" not in GLOSS_ADD["saghir"]: GLOSS_ADD["saghir"] = dict(GLOSS_ADD["saghir"], plural="صِغَار")

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/48.json").write_text(
    json.dumps({"chapter": 48, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 48 for c in man["chapters"]):
    man["chapters"].append({"n": 48, "title": TITLE48})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.48.0"
ADD_EN = (" Chapter 48 (lines ~3080-3200, sahifa 107-110) carries the seven kinds of the wajh: the six bayts "
          "s7, s9, s10, s11, s12, s15-s16 and the aya s13 (62:5) are Arabic as the source prints it, and so are "
          "the two sayings inside s22; the source writes رُؤُسِنَا (s9), التَّوْرٰيةَ with the dagger alif (s13), "
          "تُجْدَلِْ with a kasra and a sukun together (s12) and the name خَاتِمٌ (s22) — the app writes "
          "رُؤُوسِنَا، التَّوْرَاةَ، تُجْدَلِ، حَاتِمٌ (the source's own gloss names Hatim al-Ta'i), the four divergences "
          "recorded here; the rhyme sukuns غَفَلْ / الْأَشَلْ are kept as printed. s1-s6, s8, s14, s17-s21 and the "
          "frame of s22 are RESTORATIONS, not quotations: the source carries those steps only in Ottoman-Turkish "
          "paraphrase, and the Arabic restores the matn's wording (وَكُلٌّ مِنْهَا إِمَّا حِسِّيٌّ وَإِمَّا عَقْلِيٌّ؛ "
          "فَوَجْهُ الشَّبَهِ سَبْعَةُ أَقْسَامٍ…؛ الْهَيْئَةُ الْحَاصِلَةُ مِنْ تَقَارُبِ الصُّوَرِ…؛ وَالْخَطَأُ أَنْ يُنْتَزَعَ…؛ "
          "وَقَدْ يُنْتَزَعُ وَجْهُ الشَّبَهِ مِنْ نَفْسِ التَّضَادِّ…) in the musannif's register; each is marked "
          "«restored» in its translation. Every likening carries an authored `tashbih` frame — arkan, kind, the "
          "shapes of the ends and of the spoken wajh (one / several / a picture) — the engine is tested against; "
          "the kaf after a category term (فَالْوَاحِدُ الْحِسِّيُّ كَالْحُمْرَةِ) is authored as NO likening, and the "
          "likening that spans the pair s15-s16 by كَمَا is described, not framed.")
ADD_TR = (" Kırk sekizinci bâb (satır ~3080-3200, sahife 107-110) vechin yedi kısmını taşır: s7, s9, s10, s11, "
          "s12, s15-s16 beyitleri ile s13 âyeti (62:5) kaynağın bastığı Arapçadır, s22'nin içindeki iki söz de "
          "öyle; kaynak رُؤُسِنَا (s9), hançer elifle التَّوْرٰيةَ (s13), kesra ile sükûnu birlikte تُجْدَلِْ (s12) ve "
          "adı خَاتِمٌ (s22) yazar — uygulama رُؤُوسِنَا، التَّوْرَاةَ، تُجْدَلِ، حَاتِمٌ yazar (kaynağın kendi açıklaması "
          "Hâtim-i Tâî'yi adlandırır); dört fark burada kayıtlıdır; kafiye sükûnları غَفَلْ / الْأَشَلْ basıldığı gibi "
          "korunmuştur. s1-s6, s8, s14, s17-s21 ve s22'nin çerçeve cümlesi ALINTI DEĞİL GERİ YAZIMDIR: kaynak o "
          "adımları yalnız Osmanlıca-Türkçe açıklamayla taşır; Arapça, matnın ifadesini musannifin üslûbunda geri "
          "yazar; her biri tercümesinde «geri yazılmıştır» diye işaretlidir. Her benzetme, motorun sınandığı "
          "müellif eliyle yazılmış bir `tashbih` çerçevesi taşır — rükünler, nev', tarafların ve söylenen vechin "
          "şekli (tek / müteaddid / tablo); kısım adından sonraki kâf (فَالْوَاحِدُ الْحِسِّيُّ كَالْحُمْرَةِ) benzetme "
          "DEĞİL diye yazılmış, s15-s16 çiftini كَمَا ile bağlayan benzetme ise çerçevelenmeden anlatılmıştır.")
if "3080-3200" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))
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
def put(key, e):
    if key not in V: V[key] = e
put("nawwara", _sg.derived(_sg.B2, _sg.W2, "ُ", "نَوَّر", "نَوِّر", "نَوِّر", "تَنْوِير", "مُنَوِّر", "مُنَوَّر", "نُوِّرَ", "يُنَوَّرُ"))
put("tahawa", _sg.derived_naqis(_sg.B6, _sg.W6, "َ", "تَهَاوَ", "تَهَاو", "a", "تَهَاو", "تَهَاوٍ (التَّهَاوِي)", "مُتَهَاوٍ (الْمُتَهَاوِي)",
                                None, None, None, "نَاقِصٌ مِنْ بَابِ التَّفَاعُلِ: تَهَاوَى، تَهَاوَتْ، تَهَاوَوْا — الْأَلِفُ تَسْقُطُ لِتَاءِ التَّأْنِيثِ وَوَاوِ الْجَمَاعَةِ."))
put("sabba", _sg.entry("مِنْ بَابِ نَصَرَ يَنْصُرُ — مُضَاعَفٌ", "فَعَلَ يَفْعُلُ", "صَبّ", "صَابّ",
                       _sg.mazi14("صَبّ", "صَبَب"), _sg.mudari14("َ", "صُبّ", "صْبُب"),
                       ["صُبَّ", "صُبَّا", "صُبُّوا", "صُبِّي", "صُبَّا", "اُصْبُبْنَ"],
                       "يَصُبَّ", "يَصُبَّ", "تَصُبَّ", "مَصْبُوب", "صُبَّ", "يُصَبُّ",
                       "مُضَاعَفٌ: الْإِدْغَامُ حَيْثُ تَحَرَّكَ الثَّانِي (صَبَّ، يَصُبُّ)، وَالْفَكُّ حَيْثُ سَكَنَ (صَبَبْتُ، يَصْبُبْنَ)؛ الْجَزْمُ بِالْفَتْحِ: لَمْ يَصُبَّ."))
put("ghafala", _sg.sound1("nasara", "غَفَل", "غْفُل", "اُغْفُل", "غَفْلَة", "غَافِل", None, None, None,
                          "فِي الشِّعْرِ يُسَكَّنُ آخِرُهُ لِلْقَافِيَةِ: لَمَّا غَفَلْ."))
put("aqa", _sg.derived_naqis(_sg.B4, _sg.W4, "ُ", "أَقْعَ", "قْع", "i", "أَقْع", "إِقْعَاء", "مُقْعٍ (الْمُقْعِي)"))
put("jadala-braid", _sg.sound1("daraba", "جَدَل", "جْدِل", "اِجْدِل", "جَدْل", "جَادِل", "مَجْدُول", "جُدِلَ", "يُجْدَلُ",
                               "فِي الشِّعْرِ يُحَرَّكُ الْمَجْزُومُ بِالْكَسْرِ لِلْقَافِيَةِ: لَمْ تُجْدَلِ."))
put("hammala", _sg.derived(_sg.B2, _sg.W2, "ُ", "حَمَّل", "حَمِّل", "حَمِّل", "تَحْمِيل", "مُحَمِّل", "مُحَمَّل", "حُمِّلَ", "يُحَمَّلُ",
                           "يَتَعَدَّى إِلَى مَفْعُولَيْنِ: حَمَّلَهُ التَّوْرَاةَ — فَإِذَا بُنِيَ لِلْمَجْهُولِ نَابَ الْأَوَّلُ وَبَقِيَ الثَّانِي مَنْصُوبًا."))
put("atmaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَطْمَع", "طْمِع", "أَطْمِع", "إِطْمَاع", "مُطْمِع", "مُطْمَع", "أُطْمِعَ", "يُطْمَعُ"))
put("arada-away", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَعْرَض", "عْرِض", "أَعْرِض", "إِعْرَاض", "مُعْرِض", "مُعْرَض", "أُعْرِضَ", "يُعْرَضُ"))
put("tawalla", _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَوَلَّ", "تَوَلّ", "a", "تَوَلّ", "تَوَلٍّ (التَّوَلِّي)", "مُتَوَلٍّ (الْمُتَوَلِّي)"))
put("abraqa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَبْرَق", "بْرِق", "أَبْرِق", "إِبْرَاق", "مُبْرِق"))
put("aqshaa", _sg.derived(_sg.B4, _sg.W4, "ُ", "أَقْشَع", "قْشِع", "أَقْشِع", "إِقْشَاع", "مُقْشِع"))
put("intazaa", _sg.derived(_sg.B8, _sg.W8, "َ", "اِنْتَزَع", "نْتَزِع", "اِنْتَزِع", "اِنْتِزَاع", "مُنْتَزِع", "مُنْتَزَع", "اُنْتُزِعَ", "يُنْتَزَعُ"))
put("tajalla", copy_morph("aqaid-ahl-al-sunna", "tajalla"))
put("ashbaha", copy_morph("aqaid-ahl-al-sunna", "ashbaha"))
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- the note
GR = ROOT / "content/grammar"
NOTE = {
 "id": "aqsam-wajh-al-shabah",
 "title": {"ar": "أَقْسَامُ وَجْهِ الشَّبَهِ — الْوَاحِدُ وَالْمُرَكَّبُ وَالْمُتَعَدِّدُ",
           "en": "The kinds of the wajh al-shabah — one, composite, several",
           "tr": "Vech-i şebehin kısımları — vâhid, mürekkeb, müteaddid"},
 "level": 6, "group": "bayan",
 "classicalSources": ["تلخيص المفتاح — أقسام وجه الشبه"],
 "question": {
  "en": ["Is the wajh ONE quality (redness), SEVERAL qualities each on its own (colour, taste and scent), or one PICTURE drawn from several things (a night whose stars tumble)?",
         "Is it sensed or thought? A sensory wajh lives only between two sensory ends; a mental wajh may join any two.",
         "Where is the wajh drawn from — the first hemistich, or the WHOLE bayt? And can two opposites share a wajh at all?"],
  "tr": ["Vech TEK bir vasıf mı (kızıllık), her biri kendi başına BİRKAÇ vasıf mı (renk, tat, koku), yoksa birkaç şeyden çıkan tek bir TABLO mu (yıldızları dökülen gece)?",
         "Duyulan mı, düşünülen mi? Hissî vech yalnız iki hissî taraf arasında yaşar; aklî vech her iki tarafı da birleştirebilir.",
         "Vech nereden çıkarılır — ilk mısradan mı, beytin BÜTÜNÜNDEN mi? Ve iki zıt hiç vech paylaşabilir mi?"]},
 "plain": {
  "en": "Seven kinds: one, composite or several — each sensory or mental, the several possibly mixed. The engine reads a spoken wajh's SHAPE from its syntax: one noun is one; nouns joined by و are several; an idafa, a clause or an alternation (now… now…) is a picture. Sensed-or-thought it leaves to the reader.",
  "tr": "Telhîs yedi kısım sayar: vâhid, mürekkeb yahut müteaddid — her biri hissî veya aklî; müteaddid muhtelif de olabilir. Motor söylenen vechin ŞEKLİNİ söz diziminden okur: tek isim tektir; و ile bağlı isimler müteaddiddir; izâfet, cümle yahut nöbetleşme (bir… bir…) tablodur. Hissî mi aklî mi sorusunu okuyucuya bırakır."},
 "explanation": {
  "en": "The wajh is either ONE (وَاحِد), a COMPOSITE (مُرَكَّب) — a hay'a, one picture built of several things — or SEVERAL (مُتَعَدِّد), several qualities each counting on its own; and each is sensory (حِسِّيّ) or of the mind (عَقْلِيّ), the several possibly MIXED (مُخْتَلِف): seven kinds. The sensory wajh occurs only between two sensory ends, since what cannot be sensed has no sensed quality; the mental is wider. ONE-SENSORY: redness, hiddenness, sweetness of scent, pleasure, softness — one for each sense. ONE-MENTAL: boldness in likening the brave man to the lion; guidance in likening knowledge to light. COMPOSITE-SENSORY, the two ends single: Abu Qays's وَقَدْ لَاحَ فِي الصُّبْحِ الثُّرَيَّا كَمَا تَرَى كَعُنْقُودِ مُلَّاحِيَّةٍ حِينَ نَوَّرَا — the wajh is the hay'a of small, white, round shapes drawn close. Both ends composite: Bashshar's كَأَنَّ مُثَارَ النَّقْعِ فَوْقَ رُؤُوسِنَا وَأَسْيَافَنَا لَيْلٌ تَهَاوَى كَوَاكِبُهُ — long bright bodies falling scattered around something dark. A wajh drawn from MOTION: Ibn al-Muʿtazz's sun وَالشَّمْسُ كَالْمِرْآةِ فِي كَفِّ الْأَشَلْ (a bright disc whose light trembles and runs) and his lightning وَكَأَنَّ الْبَرْقَ مُصْحَفُ قَارٍ فَانْطِبَاقًا مَرَّةً وَانْفِتَاحًا (motion in different directions — a mill-wheel or an arrow, moving one way, gives no composite); and one drawn from STILLNESS: al-Mutanabbi's dog يُقْعِي جُلُوسَ الْبَدَوِيِّ الْمُصْطَلِي بِأَرْبَعٍ مَجْدُولَةٍ لَمْ تُجْدَلِ, every limb in its place. COMPOSITE-MENTAL: مَثَلُ الَّذِينَ حُمِّلُوا التَّوْرَاةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ الْحِمَارِ يَحْمِلُ أَسْفَارًا — bearing the burden of a most useful thing while denied its benefit; both ends composite and mental. The composite wajh is drawn from the WHOLE: in لَقَدْ أَطْمَعَتْنِي بِالْوِصَالِ تَبَسُّمًا / فَلَمَّا سَأَلْنَا أَعْرَضَتْ وَتَوَلَّتْ — كَمَا أَبْرَقَتْ قَوْمًا عِطَاشًا غَمَامَةٌ / فَلَمَّا رَأَوْهَا أَقْشَعَتْ وَتَجَلَّتْ the wajh is a hopeful beginning joined to a depriving end, and taking it from the first hemistich alone is the error. SEVERAL-SENSORY: colour, taste and scent in likening one fruit to another; SEVERAL-MENTAL: keenness of sight, perfect wariness and hidden mating in likening a bird to the raven; MIXED: beauty of face (sensed) and eminence of standing (thought) in likening a person to the sun. Lastly the wajh may be drawn from OPPOSITION itself and brought down to the rank of proportion by pleasantry (تَمْلِيح) or mockery (تَهَكُّم): of the coward مَا أَشْبَهَهُ بِالْأَسَدِ, of the miser هُوَ حَاتِمٌ. WHAT THE ENGINE CLAIMS: the shape of a SPOKEN wajh — one noun is مُفْرَد; nouns joined by وَ are مُتَعَدِّد (كَاللَّوْنِ وَالطَّعْمِ وَالرَّائِحَةِ); an idafa (كَإِزَالَةِ الْحِجَابِ), a clause, or an alternation with مَرَّةً / تَارَةً is مُرَكَّب — and the shape of each END (a noun with a describing clause or a joined pair under one restriction is a picture). It reads the kaf after a category term (فَالْوَاحِدُ الْحِسِّيُّ كَالْحُمْرَةِ) as «for instance», the aside كَمَا تَرَى as no adat, and the maf'ul mutlaq of likeness (يُقْعِي جُلُوسَ الْبَدَوِيِّ) as a frame with its adat dropped. Sensed-or-thought, and the wajh of an UNSPOKEN (mujmal) likening, it offers as a shortlist: those are knowledge of the two things, not of the sentence.",
  "tr": "Vech ya TEKTİR (وَاحِد), ya MÜREKKEBdir (مُرَكَّب) — hey'et: birkaç şeyden kurulu tek tablo — ya MÜTEADDİDdir (مُتَعَدِّد): her biri kendi başına sayılan birkaç vasıf; her biri de hissî (حِسِّيّ) yahut aklîdir (عَقْلِيّ), müteaddid MUHTELİF (مُخْتَلِف) de olabilir: yedi kısım. Hissî vech yalnız iki hissî taraf arasında bulunur, çünkü duyulamayanın duyulan vasfı olmaz; aklî daha geniştir. VÂHİD-HİSSÎ: kızıllık, gizlilik, koku güzelliği, lezzet, yumuşaklık — her duyuya bir örnek. VÂHİD-AKLÎ: cesur adamı arslana benzetmede cür'et; ilmi nura benzetmede hidâyet. MÜREKKEB-HİSSÎ, iki taraf tek: Ebû Kays'ın وَقَدْ لَاحَ فِي الصُّبْحِ الثُّرَيَّا كَمَا تَرَى كَعُنْقُودِ مُلَّاحِيَّةٍ حِينَ نَوَّرَا beyti — vech, küçük beyaz yuvarlak suretlerin birbirine yaklaşma hey'eti. İki taraf mürekkeb: Beşşâr'ın كَأَنَّ مُثَارَ النَّقْعِ فَوْقَ رُؤُوسِنَا وَأَسْيَافَنَا لَيْلٌ تَهَاوَى كَوَاكِبُهُ beyti — karanlık bir şeyin etrafına dağınık düşen uzun parlak cisimler. HAREKETten çıkan vech: İbnü'l-Mu'tez'in güneşi وَالشَّمْسُ كَالْمِرْآةِ فِي كَفِّ الْأَشَلْ (ışığı titreyip akan parlak yuvarlak) ve şimşeği وَكَأَنَّ الْبَرْقَ مُصْحَفُ قَارٍ فَانْطِبَاقًا مَرَّةً وَانْفِتَاحًا (farklı yönlere hareket — tek yöne giden değirmen taşı yahut ok terkib vermez); SÜKÛNdan çıkan: Mütenebbî'nin köpeği يُقْعِي جُلُوسَ الْبَدَوِيِّ الْمُصْطَلِي بِأَرْبَعٍ مَجْدُولَةٍ لَمْ تُجْدَلِ, her uzuv yerinde. MÜREKKEB-AKLÎ: مَثَلُ الَّذِينَ حُمِّلُوا التَّوْرَاةَ ثُمَّ لَمْ يَحْمِلُوهَا كَمَثَلِ الْحِمَارِ يَحْمِلُ أَسْفَارًا — çok faydalı bir şeyin yükünü çekip faydasından mahrum kalmak; iki taraf da mürekkeb aklî. Mürekkeb vech BÜTÜNDEN çıkarılır: لَقَدْ أَطْمَعَتْنِي بِالْوِصَالِ تَبَسُّمًا / فَلَمَّا سَأَلْنَا أَعْرَضَتْ وَتَوَلَّتْ — كَمَا أَبْرَقَتْ قَوْمًا عِطَاشًا غَمَامَةٌ / فَلَمَّا رَأَوْهَا أَقْشَعَتْ وَتَجَلَّتْ beyitlerinde vech, umut veren başlangıcın mahrum bırakan sona bitişmesidir; onu yalnız ilk mısradan almak hatadır. MÜTEADDİD-HİSSÎ: bir meyveyi diğerine benzetmede renk, tat, koku; MÜTEADDİD-AKLÎ: kuşu kargaya benzetmede bakış keskinliği, tam ihtiyat, çiftleşmeyi gizleme; MUHTELİF: insanı güneşe benzetmede yüz güzelliği (hissî) ve şan yüceliği (aklî). Nihayet vech TEZÂDIN kendisinden çıkarılıp temlîh (تَمْلِيح) yahut tehekküm (تَهَكُّم) ile tenâsüb mertebesine indirilebilir: korkağa مَا أَشْبَهَهُ بِالْأَسَدِ, cimriye هُوَ حَاتِمٌ. MOTORUN İDDİASI: SÖYLENEN vechin şekli — tek isim مُفْرَد; وَ ile bağlı isimler مُتَعَدِّد (كَاللَّوْنِ وَالطَّعْمِ وَالرَّائِحَةِ); izâfet (كَإِزَالَةِ الْحِجَابِ), cümle yahut مَرَّةً / تَارَةً ile nöbetleşme مُرَكَّب — ve her TARAFIN şekli (vasıf cümleli isim yahut tek kayıt altındaki atıf çifti tablodur). Kısım adından sonraki kâfı (فَالْوَاحِدُ الْحِسِّيُّ كَالْحُمْرَةِ) «meselâ» diye, كَمَا تَرَى ara cümlesini edat değil diye, benzetme mef'ûl-i mutlakını (يُقْعِي جُلُوسَ الْبَدَوِيِّ) edatı düşmüş çerçeve diye okur. Hissî mi aklî mi sorusunu ve SÖYLENMEMİŞ (mücmel) vechi kısa liste olarak sunar: onlar cümlenin değil iki şeyin bilgisidir."},
 "examples": [
  {"ar": "وَقَدْ لَاحَ فِي الصُّبْحِ الثُّرَيَّا كَمَا تَرَى كَعُنْقُودِ مُلَّاحِيَّةٍ حِينَ نَوَّرَا", "en": "composite-sensory wajh, single ends; the aside كَمَا تَرَى stepped over.", "tr": "mürekkeb hissî vech, tek taraflar; كَمَا تَرَى ara cümlesi atlanır.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "كَأَنَّ مُثَارَ النَّقْعِ فَوْقَ رُؤُوسِنَا وَأَسْيَافَنَا لَيْلٌ تَهَاوَى كَوَاكِبُهُ", "en": "both ends composite: a joined pair under one restriction, a noun with its clause.", "tr": "iki taraf mürekkeb: tek kayıt altında atıf çifti, cümleli isim.", "sourceStory": "talkhis-al-miftah", "sentence": "s9"},
  {"ar": "يُقْعِي جُلُوسَ الْبَدَوِيِّ الْمُصْطَلِي", "en": "the adat dropped, the maf'ul mutlaq in its place.", "tr": "edat düşmüş, mef'ûl-i mutlak yerinde.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"},
  {"ar": "كَاللَّوْنِ وَالطَّعْمِ وَالرَّائِحَةِ فِي تَشْبِيهِ فَاكِهَةٍ بِأُخْرَى", "en": "a SEVERAL wajh, spoken before its masdar.", "tr": "MÜTEADDİD vech, masdarından önce söylenmiş.", "sourceStory": "talkhis-al-miftah", "sentence": "s18"},
  {"ar": "مَا أَشْبَهَهُ بِالْأَسَدِ … هُوَ حَاتِمٌ", "en": "the wajh from opposition: mockery; two likenings in one line, mafruq.", "tr": "tezâddan vech: tehekküm; bir satırda iki benzetme, mefrûk.", "sourceStory": "talkhis-al-miftah", "sentence": "s22"}],
 "commonMistakes": [
  {"wrong": "«فَالْوَاحِدُ الْحِسِّيُّ كَالْحُمْرَةِ bir teşbihtir: vâhid hissî kızıllığa benzetilmiştir»",
   "right": "«Kâf burada örnek kâfıdır: vâhid hissî vechin misali kızıllıktır»",
   "why": {"en": "A category term of the art before the kaf names a division and gives its instance. The engine refuses a likening after الْوَاحِدُ، الْمُرَكَّبُ، الْمُتَعَدِّدُ، الْمُخْتَلِفُ and their kin.", "tr": "Kâftan önceki kısım adı bir bölüm adlandırır ve örneğini verir. Motor الْوَاحِدُ، الْمُرَكَّبُ، الْمُتَعَدِّدُ، الْمُخْتَلِفُ ve benzerlerinden sonra benzetme okumaz."}},
  {"wrong": "«لَقَدْ أَطْمَعَتْنِي بِالْوِصَالِ تَبَسُّمًا mısraında vech: tebessümle umutlandırmak»",
   "right": "«Vech beytin bütününden çıkarılır: umut veren başlangıcın mahrum bırakan sona bitişmesi»",
   "why": {"en": "A composite wajh is a picture; cutting it at the hemistich leaves half a picture, and the Talkhis calls that the error.", "tr": "Mürekkeb vech bir tablodur; mısrada kesmek yarım tablo bırakır ve Telhîs buna hata der."}},
  {"wrong": "«كَاللَّوْنِ وَالطَّعْمِ وَالرَّائِحَةِ: mürekkeb vech»",
   "right": "«Müteaddid vech: üç vasıf, her biri kendi başına; mürekkeb tek bir hey'ettir»",
   "why": {"en": "Joined by وَ, the qualities stay separate — several. A picture needs the things to be held in ONE hay'a: an idafa, a clause, an alternation.", "tr": "وَ ile bağlı vasıflar ayrı kalır — müteaddid. Tablo, şeylerin TEK hey'ette tutulmasını ister: izâfet, cümle, nöbetleşme."}}],
 "relatedNotes": ["wajh-al-shabah", "arkan-al-tashbih", "tashbih", "ilm-al-bayan", "maful-mutlaq", "inna-wa-akhawatuha", "jumla-sifa", "ism-maqsur-manqus", "al-muthanna", "jam-taksir", "doubled-verbs", "naqis-verbs"]}
(GR / "aqsam-wajh-al-shabah.json").write_text(json.dumps(NOTE, ensure_ascii=False, indent=1), encoding="utf-8")
w = json.loads((GR / "wajh-al-shabah.json").read_text(encoding="utf-8"))
if "aqsam-wajh-al-shabah" not in w["relatedNotes"]:
    w["relatedNotes"].insert(1, "aqsam-wajh-al-shabah")
    (GR / "wajh-al-shabah.json").write_text(json.dumps(w, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch48:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + 13 built, 2 copied; note aqsam-wajh-al-shabah;",
      "frames:", sum(1 for x in S if x.get("tashbih")))
