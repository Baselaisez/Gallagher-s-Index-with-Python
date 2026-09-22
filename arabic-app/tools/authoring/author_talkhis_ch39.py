# -*- coding: utf-8 -*-
"""Author chapter 39 of talkhis-al-miftah — إِيجَازُ الْحَذْفِ.

Sahifa 94-95 (lines ~2714-2775): ijaz divides into qasr (ch. 38's
crown witness) and HADHF — and the omitted thing is a PART of the
sentence, a WHOLE jumla, or SEVERAL jumlas:

  • omitted MUDAF: وَاسْأَلِ الْقَرْيَةَ (Yusuf 12:82) — the taqdir is
    أَهْلَ الْقَرْيَةِ, and the mudaf-ilayh steps into the mudaf's case.
  • omitted MAWSUF: Suhaym's bayt أَنَا ابْنُ جَلَا وَطَلَّاعُ الثَّنَايَا
    مَتَى أَضَعِ الْعِمَامَةَ تَعْرِفُونِي — the taqdir أَنَا ابْنُ رَجُلٍ
    جَلَا (the source adds: ثَنَايَا is the plural of ثَنِيَّة).
  • omitted SIFA: وَكَانَ وَرَاءَهُمْ مَلِكٌ يَأْخُذُ كُلَّ سَفِينَةٍ
    غَصْبًا (Kahf 18:79) — the taqdir سَفِينَةٍ صَحِيحَةٍ.
  • the TWO WAJHS of hadhf: nothing put in the gap, or a STAND-IN:
    وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ مِنْ قَبْلِكَ (Fatir 35:4),
    where فَقَدْ كُذِّبَتْ… stands where فَلَا تَحْزَنْ وَاصْبِرْ fell.

ATTRIBUTION: s1 is Yusuf 12:82 (part), s4 al-Kahf 18:79 (part), s5
Fatir 35:4 (part) — received Qur'anic text quoted exactly in standard
imla as the source prints them; s2-s3 are Suhaym b. Wathil's bayt as
the source recites it, split at the hemistich (the chapter-19/37
verse-reuse precedent).

Grammar this chapter teaches:
  • note 143 `ijaz-al-hadhf` — the omitted juz' kinds, the omitted
    jumla kinds, the two wajhs, and the dalils of hadhf.
  • five-verbs jazm in the flesh: يُكَذِّبُوكَ and تَعْرِفُونِي (hadhf
    al-nun under a clinging pronoun) — the engine learned to restore
    the raf' nun for matching this wave.
  • the derived majhul-mazi she-cell: كُذِّبَتْ.
  • new paradigm: جَلَا يَجْلُو (naqis wawi, bab nasara).
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

TITLE39 = {"ar": "إِيجَازُ الْحَذْفِ",
           "en": "Brevity by Omission",
           "tr": "Îcâz-ı Hazif"}

# ------------------------- s1 — Yusuf 12:82: the omitted MUDAF
S.append({"id": "s1", "translation": {
 "en": "«And ask the town» (12:82) — that is, ask the town's PEOPLE: the mudaf is omitted, and what it leaned on steps into its case.",
 "tr": "«Köye sor» (12:82) — yani köyün HALKINA sor: muzâf hazfedilmiş, dayandığı kelime onun i'râbına geçmiştir."},
 "tokens": [
  tok("وَاسْأَلِ","saala","verb",["ijaz-al-hadhf","imperative-amr"],
      "الْوَاوُ عَاطِفَةٌ، وَاسْأَلْ فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ أَنْتَ.",
      "«and ask» — the amr, its resting sukun moved to a kasra against the coming hamzat al-wasl.",
      "«ve sor» — emir; sükûnu, gelen vasıl hemzesine karşı kesreye çevrilmiş.",
      segments=[seg("وَ","wa","part"), seg("اسْأَلِ","saala","verb")]),
  tok("الْقَرْيَةَ","qarya","noun",["ijaz-al-hadhf","hadhf-wa-taqdir"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ — وَالتَّقْدِيرُ: وَاسْأَلْ أَهْلَ الْقَرْيَةِ، فَحُذِفَ الْمُضَافُ وَقَامَ هٰذَا مَقَامَهُ فَأَخَذَ نَصْبَهُ.",
      "«the town» — nasb, but not its own: the omitted mudaf أَهْلَ owned this case, and the word left behind inherited it.",
      "«köyü» — nasb, ama kendi malı değil: hazfedilen muzâf أَهْلَ bu i'râbın sahibiydi; geride kalan kelime onu miras aldı.",
      punct=".")],
 "jumal": [
  J("وَاسْأَلِ الْقَرْيَةَ",
    "جُمْلَةٌ فِعْلِيَّةٌ طَلَبِيَّةٌ — شَاهِدُ حَذْفِ الْمُضَافِ.",
    "The mudaf-omission witness: a town cannot answer, so the mind supplies its people — brevity that trusts the hearer.",
    "Muzâf hazfinin şahidi: köy cevap veremez, zihin halkını takdir eder — dinleyene güvenen kısalık."),
  J("الْقَرْيَةَ",
    "قَامَ الْمُضَافُ إِلَيْهِ مَقَامَ الْمُضَافِ الْمَحْذُوفِ وَأَخَذَ إِعْرَابَهُ.",
    "One word wearing another's case: the surest fingerprint that something fell.",
    "Başkasının i'râbını giymiş tek kelime: bir şeyin düştüğünün en sağlam izi.")]})

# ----------- s2 — Suhaym's first hemistich: the omitted MAWSUF
S.append({"id": "s2", "translation": {
 "en": "I am the son of one-who-cleared-the-heights, and the ever-scaler of the passes — that is, the son of A MAN who cleared them: the mawsuf is omitted and its sifa stands alone.",
 "tr": "Ben, zirveleri aşmış birinin oğluyum ve geçitlerin dâimî tırmanıcısıyım — yani aşmış BİR ADAMIN oğlu: mevsuf hazfedilmiş, sıfatı tek başına durur."},
 "tokens": [
  tok("أَنَا","ana","pron",["ijaz-al-hadhf"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ.",
      "«I» — the boast opens on the speaker himself.",
      "«ben» — övünme, konuşanın kendisiyle açılır."),
  tok("ابْنُ","ibn","noun",["ijaz-al-hadhf","idafa-definiteness"],
      "خَبَرٌ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«son of» — the khabar, leaning on what follows.",
      "«oğlu» — haber; sonrakine yaslanan muzâf."),
  tok("جَلَا","jala","verb",["ijaz-al-hadhf","naqis-verbs","jumla-sifa","hadhf-wa-taqdir"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى الْفَتْحِ الْمُقَدَّرِ، وَالْفَاعِلُ هُوَ — وَالْجُمْلَةُ صِفَةٌ لِمَوْصُوفٍ مَحْذُوفٍ، وَالتَّقْدِيرُ: أَنَا ابْنُ رَجُلٍ جَلَا.",
      "«who cleared» — a mazi verb sitting where a noun should: the mawsuf رَجُلٍ fell, and its sifa-clause holds the annexation alone. Ijaz al-hadhf.",
      "«aşmış» — isim duracak yerde bir mâzî fiil: mevsuf رَجُلٍ düşmüş, sıfat cümlesi izâfeti tek başına tutar. Îcâz-ı hazif.",
      punct=None),
  tok("وَطَلَّاعُ","tallaa","noun",["ijaz-al-hadhf","sighat-mubalagha"],
      "الْوَاوُ عَاطِفَةٌ، وَطَلَّاعُ مَعْطُوفٌ عَلَى ابْنُ مَرْفُوعٌ وَهُوَ مُضَافٌ.",
      "«and the ever-scaler of» — فَعَّال, the intensive mould: not one who climbed once, but whose habit is the heights.",
      "«ve dâimî tırmanıcısı» — فَعَّال, mübâlağa kalıbı: bir kez çıkan değil, âdeti zirveler olan.",
      segments=[seg("وَ","wa","part"), seg("طَلَّاعُ","tallaa","noun")]),
  tok("الثَّنَايَا","thanaya","noun",["ijaz-al-hadhf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ — وَهُوَ جَمْعُ ثَنِيَّةٍ.",
      "«the mountain passes» — jarr estimated on the alif; the source itself footnotes: plural of ثَنِيَّة.",
      "«geçitlerin» — cer, elif üzerinde takdîrî; kaynağın kendi notu: ثَنِيَّة'nin cem'i.",
      punct="•")],
 "jumal": [
  J("أَنَا ابْنُ جَلَا وَطَلَّاعُ الثَّنَايَا",
    "جُمْلَةٌ اسْمِيَّةٌ — شَاهِدُ حَذْفِ الْمَوْصُوفِ، وَالتَّقْدِيرُ: ابْنُ رَجُلٍ جَلَا.",
    "The mawsuf-omission witness: Suhaym's boast rides faster for the missing word — fame needs no naming.",
    "Mevsuf hazfinin şahidi: Sühaym'ın övünmesi eksik kelimeyle daha hızlı gider — şöhret ad istemez."),
  J("ابْنُ جَلَا",
    "مُضَافٌ إِلَى جُمْلَةِ الصِّفَةِ بَعْدَ حَذْفِ مَوْصُوفِهَا.",
    "An idafa leaning on a verb-clause: the grammar's scar where the noun was cut away.",
    "Fiil cümlesine yaslanan izâfet: ismin kesildiği yerde gramerin izi.")]})

# ----------- s3 — the second hemistich: shart, jazm, and the wiqaya nun
S.append({"id": "s3", "translation": {
 "en": "Whenever I set down the turban, you know me. (the shart-noun مَتَى gives jazm to both verbs; the five-verbs jawab drops its nun and takes the guarding nun before the speaker's ya.)",
 "tr": "Sarığımı ne zaman koysam beni tanırsınız. (Şart ismi مَتَى iki fiile de cezm verir; ef'âl-i hamseden cevap fiili nûnunu düşürür ve mütekellim yâsından önce vikaye nûnunu alır.)"},
 "tokens": [
  tok("مَتَى","mata","noun",["ijaz-al-hadhf","in-shartiyya","maful-fih"],
      "اسْمُ شَرْطٍ جَازِمٌ مُتَضَمِّنٌ مَعْنَى الظَّرْفِيَّةِ، يَجْزِمُ فِعْلَيْنِ.",
      "«whenever» — the shart-noun of time: it binds two verbs in jazm, condition and answer.",
      "«ne zaman» — zaman bildiren şart ismi: şart ve cevap, iki fiili cezmle bağlar."),
  tok("أَضَعِ","wadaa","verb",["ijaz-al-hadhf","in-shartiyya","mithal-verbs"],
      "فِعْلُ الشَّرْطِ مُضَارِعٌ مَجْزُومٌ بِالسُّكُونِ وَحُرِّكَ بِالْكَسْرِ لِالْتِقَاءِ السَّاكِنَيْنِ، وَالْفَاعِلُ أَنَا — وَالْمِثَالُ الْوَاوِيُّ قَدْ أَسْقَطَ وَاوَهُ فِي الْمُضَارِعِ.",
      "«I set down» — the shart verb, jazm by sukun, moved to a kasra against the coming sakin; the mithal wawi has already dropped its waw (وَضَعَ → أَضَعُ).",
      "«koysam» — şart fiili, sükûnla meczum; gelen sâkine karşı kesreye çevrilmiş. Misâl-i vâvî, muzâride vâvını çoktan düşürmüştür (وَضَعَ → أَضَعُ).",
      punct=None),
  tok("الْعِمَامَةَ","imama","noun",["ijaz-al-hadhf"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ.",
      "«the turban» — the disguise of rank: set it down and the face is proof enough.",
      "«sarığı» — makam örtüsü: koy, yüz yeter delil."),
  tok("تَعْرِفُونِي","arafa","verb",["ijaz-al-hadhf","afal-khamsa","ya-al-mutakallim","in-shartiyya"],
      "جَوَابُ الشَّرْطِ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.",
      "«you know me» — the jawab: a five-verbs form whose raf' nun fell to jazm, then the GUARDING nun stepped in to shield the verb from the speaker's ya.",
      "«beni tanırsınız» — cevap: ef'âl-i hamseden; ref' nûnu cezme düşmüş, sonra fiili mütekellim yâsından koruyan VİKAYE nûnu girmiştir.",
      punct=".", segments=[seg("تَعْرِفُو","arafa","verb"), seg("نِي","ni-wiqaya","pron")])],
 "jumal": [
  J("مَتَى أَضَعِ الْعِمَامَةَ تَعْرِفُونِي",
    "جُمْلَةُ شَرْطٍ وَجَوَابُهُ — وَكِلَا الْفِعْلَيْنِ مَجْزُومٌ بِمَتَى.",
    "One shart-noun, two jazms: the condition by sukun-turned-kasra, the answer by a dropped nun.",
    "Tek şart ismi, iki cezm: şart kesreye dönmüş sükûnla, cevap düşmüş nûnla."),
  J("تَعْرِفُونِي",
    "فِعْلٌ وَفَاعِلٌ وَنُونُ وِقَايَةٍ وَمَفْعُولٌ — أَرْبَعَةُ أَجْزَاءٍ فِي كَلِمَةٍ.",
    "Four grammatical persons folded into one written word — the opposite pole of this chapter's omissions.",
    "Tek yazılı kelimeye katlanmış dört gramer parçası — bu bâbın hazif kutbunun tam karşısı.")]})

# ----------- s4 — Kahf 18:79: the omitted SIFA
S.append({"id": "s4", "translation": {
 "en": "«And beyond them was a king seizing every ship by force» (18:79) — every SOUND ship: the sifa is omitted, and what came before points to it.",
 "tr": "«Onların ilerisinde her gemiyi zorla alan bir kral vardı» (18:79) — her SAĞLAM gemiyi: sıfat hazfedilmiş, öncesi ona delâlet eder."},
 "tokens": [
  tok("وَكَانَ","kana","verb",["ijaz-al-hadhf","kana-wa-akhawatuha"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَ فِعْلٌ مَاضٍ نَاقِصٌ.",
      "«and there was» — kana opens the scene Khidr explains.",
      "«ve vardı» — Hızır'ın açıkladığı sahneyi kâne açar.",
      segments=[seg("وَ","wa","part"), seg("كَانَ","kana","verb")]),
  tok("وَرَاءَهُمْ","waraa","noun",["ijaz-al-hadhf","maful-fih","zarf-mustaqarr-wa-laghw"],
      "وَرَاءَ ظَرْفُ مَكَانٍ مَنْصُوبٌ، خَبَرُ كَانَ مُقَدَّمٌ وَهُوَ مُضَافٌ، وَهُمْ مُضَافٌ إِلَيْهِ — وَمَعْنَاهُ هُنَا أَمَامَهُمْ.",
      "«beyond them» — the place-zarf as kana's fronted khabar; and the source notes the sense: AHEAD of them, on their road.",
      "«ilerisinde» — mekân zarfı, kânenin öne alınmış haberi; kaynak mânâyı da söyler: yollarının İLERİSİNDE.",
      segments=[seg("وَرَاءَ","waraa","noun"), seg("هُمْ","pron-3mp","pron")]),
  tok("مَلِكٌ","malik-king","noun",["ijaz-al-hadhf","kana-wa-akhawatuha"],
      "اسْمُ كَانَ مُؤَخَّرٌ مَرْفُوعٌ.",
      "«a king» — kana's delayed ism (and a different word from مَالِك, «owner»: one vowel apart, a throne apart).",
      "«bir kral» — kânenin ertelenmiş ismi (ve مَالِك «sahip»ten ayrı bir kelime: bir hareke fark, bir taht fark)."),
  tok("يَأْخُذُ","akhadha","verb",["ijaz-al-hadhf","jumla-sifa"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ هُوَ — وَالْجُمْلَةُ صِفَةٌ لِمَلِكٌ.",
      "«seizing» — the verb-clause as sifa of the king.",
      "«alan» — kralın sıfatı olan fiil cümlesi."),
  tok("كُلَّ","kull","noun",["ijaz-al-hadhf"],
      "مَفْعُولٌ بِهِ مَنْصُوبٌ وَهُوَ مُضَافٌ.",
      "«every» — always a mudaf.",
      "«her» — dâima muzâf."),
  tok("سَفِينَةٍ","safina","noun",["ijaz-al-hadhf","hadhf-wa-taqdir","naat-sifa"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ — وَالتَّقْدِيرُ: كُلَّ سَفِينَةٍ صَحِيحَةٍ، فَحُذِفَتِ الصِّفَةُ لِدَلَالَةِ مَا قَبْلَهُ عَلَيْهَا.",
      "«ship» — its omitted sifa is صَحِيحَةٍ, «sound»: that is why Khidr scuttled the boat — a holed ship the king would not take.",
      "«gemi» — hazfedilen sıfatı صَحِيحَةٍ, «sağlam»: Hızır'ın gemiyi delmesi bundandı — delik gemiyi kral almazdı."),
  tok("غَصْبًا","ghasb","noun",["ijaz-al-hadhf","hal","maful-mutlaq"],
      "مَصْدَرٌ مَنْصُوبٌ فِي مَوْضِعِ الْحَالِ — أَيْ غَاصِبًا — وَيَجُوزُ مَفْعُولًا مُطْلَقًا لِبَيَانِ النَّوْعِ.",
      "«by force» — a masdar standing as hal («seizing-wise»), or a maf'ul mutlaq naming the taking's kind: both readings are received.",
      "«zorla» — hâl makamında masdar («gasp ederek»), yahut alışın türünü adlandıran mef'ûl-i mutlak: iki okuma da mervîdir.",
      punct=".")],
 "jumal": [
  J("وَكَانَ وَرَاءَهُمْ مَلِكٌ يَأْخُذُ كُلَّ سَفِينَةٍ غَصْبًا",
    "جُمْلَةُ كَانَ — وَفِيهَا شَاهِدُ حَذْفِ الصِّفَةِ.",
    "The sifa-omission witness: the verse withholds «sound», and Khidr's chisel supplies the commentary.",
    "Sıfat hazfinin şahidi: âyet «sağlam»ı söylemez, Hızır'ın keskisi tefsiri yapar."),
  J("يَأْخُذُ كُلَّ سَفِينَةٍ غَصْبًا",
    "جُمْلَةُ الصِّفَةِ — وَالْمَحْذُوفُ صِفَةُ سَفِينَةٍ: صَحِيحَةٍ.",
    "Inside the sifa-clause, another sifa is missing: omission nested in description.",
    "Sıfat cümlesinin içinde bir sıfat daha eksik: tasvirin içine yuvalanmış hazif.")]})

# ----------- s5 — Fatir 35:4: the STAND-IN wajh of hadhf
S.append({"id": "s5", "translation": {
 "en": "«And if they call you a liar — messengers before you were called liars» (35:4). The omitted jawab is «so do not grieve, and endure»; what is written STANDS IN its place.",
 "tr": "«Seni yalanlarlarsa — senden önceki nice resuller de yalanlandı» (35:4). Hazfedilen cevap «üzülme ve sabret»tir; yazılı olan, onun YERİNE geçmiştir."},
 "tokens": [
  tok("وَإِنْ","in-shart","part",["ijaz-al-hadhf","in-shartiyya"],
      "الْوَاوُ عَاطِفَةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.",
      "«and if» — the shart harf that will bend two verbs.",
      "«ve eğer» — iki fiili bükecek şart harfi.",
      segments=[seg("وَ","wa","part"), seg("إِنْ","in-shart","part")]),
  tok("يُكَذِّبُوكَ","kadhdhaba","verb",["ijaz-al-hadhf","afal-khamsa","in-shartiyya","form-ii-verbs"],
      "فِعْلُ الشَّرْطِ مُضَارِعٌ مَجْزُومٌ بِحَذْفِ النُّونِ مِنَ الْأَفْعَالِ الْخَمْسَةِ، وَالْوَاوُ فَاعِلٌ، وَالْكَافُ مَفْعُولٌ بِهِ.",
      "«they call you a liar» — the five-verbs jazm again: the nun fell, the group's waw stays as fail, the kaf clings as object.",
      "«seni yalanlarlarsa» — yine ef'âl-i hamse cezmi: nûn düşmüş, cemaat vâvı fâil kalmış, kâf mef'ûl olarak yapışmıştır.",
      segments=[seg("يُكَذِّبُو","kadhdhaba","verb"), seg("كَ","pron-2ms","pron")]),
  tok("فَقَدْ","qad","part",["ijaz-al-hadhf","qad-harf"],
      "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَقَدْ حَرْفُ تَحْقِيقٍ — وَالْجُمْلَةُ بَعْدَهَا قَائِمَةٌ مَقَامَ الْجَوَابِ الْمَحْذُوفِ: فَلَا تَحْزَنْ وَاصْبِرْ.",
      "«then indeed» — the fa of the jawab, but the true jawab fell: «do not grieve, endure» — and this clause was set in its place. The second wajh of hadhf.",
      "«gerçekten» — cevap fâsı; ama asıl cevap düşmüştür: «üzülme, sabret» — ve bu cümle onun yerine konmuştur. Hazfin ikinci vechi.",
      segments=[seg("فَ","fa","part"), seg("قَدْ","qad","part")]),
  tok("كُذِّبَتْ","kadhdhaba","verb",["ijaz-al-hadhf","naib-al-fail","form-ii-verbs"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَالتَّاءُ لِلتَّأْنِيثِ.",
      "«were called liars» — the majhul mazi with the ta of tanith: the deniers are not worth naming.",
      "«yalanlandı» — te'nîs tâlı meçhûl mâzî: yalanlayanlar anılmaya değmez.",
      punct=None),
  tok("رُسُلٌ","rusul","noun",["ijaz-al-hadhf","naib-al-fail","tankir-al-musnad-ilayh"],
      "نَائِبُ فَاعِلٍ مَرْفُوعٌ — وَتَنْكِيرُهُ لِلتَّكْثِيرِ.",
      "«messengers» — the deputy-subject, indefinite for MANY: you walk a crowded road.",
      "«resuller» — nâib-i fâil; tenkiri ÇOKLUK içindir: kalabalık bir yolda yürüyorsun.",
      punct=None),
  tok("مِنْ","min","part",["ijaz-al-hadhf"],
      "حَرْفُ جَرٍّ.",
      "«from» —",
      "«-den» —"),
  tok("قَبْلِكَ","qabl","noun",["ijaz-al-hadhf"],
      "مَجْرُورٌ بِمِنْ وَهُوَ مُضَافٌ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«before you» — the consolation's whole geography in one jarr phrase.",
      "«senden önce» — tesellinin bütün coğrafyası tek câr-mecrûrda.",
      punct=".", segments=[seg("قَبْلِ","qabl","noun"), seg("كَ","pron-2ms","pron")])],
 "jumal": [
  J("وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ مِنْ قَبْلِكَ",
    "جُمْلَةُ شَرْطٍ حُذِفَ جَوَابُهَا وَأُقِيمَ غَيْرُهُ مَقَامَهُ.",
    "The stand-in witness: hadhf's second wajh — the gap is not left open but filled with the reason for patience.",
    "Yerine-geçen şahidi: hazfin ikinci vechi — boşluk açık bırakılmaz, sabrın gerekçesiyle doldurulur."),
  J("فَقَدْ كُذِّبَتْ رُسُلٌ مِنْ قَبْلِكَ",
    "قَائِمٌ مَقَامَ الْجَوَابِ — وَالتَّقْدِيرُ: فَلَا تَحْزَنْ وَاصْبِرْ.",
    "What consoles is written; what commands is understood — one clause doing the other's work.",
    "Teselli eden yazılmış; emreden anlaşılmıştır — biri ötekinin işini gören tek cümle.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "qarya": g("قَرْيَة", "ق ر ي", "noun", "town, village", "belde, köy", 2, plural="قُرًى"),
 "jala": g("جَلَا", "ج ل و", "verb", "to clear, make plain; to scale and lay open (heights, matters)", "açmak, aşmak; (zirveleri, işleri) aşıp âşikâr kılmak", 5, form="I"),
 "tallaa": g("طَلَّاع", "ط ل ع", "noun", "one ever scaling (intensive fa''al mould)", "dâima tırmanan (mübâlağa sîgası فَعَّال)", 5),
 "thanaya": g("ثَنِيَّة", "ث ن ي", "noun", "mountain pass, high road", "dağ geçidi, bel", 5, plural="ثَنَايَا"),
 "imama": g("عِمَامَة", "ع م م", "noun", "turban", "sarık, imâme", 3, plural="عَمَائِم"),
 "waraa": g("وَرَاء", "و ر ي", "noun", "behind; beyond (also: ahead, on one's road)", "arka; öte (bazen: ileride, yol üstünde)", 2),
 "malik-king": g("مَلِك", "م ل ك", "noun", "king", "kral, melik", 2, plural="مُلُوك"),
 "mata": copy_gloss("wasiyyat-abi-hanifa-samti", "mata"),
 "ghasb": copy_gloss("kitab-al-buyu", "ghasb"),
 "qabl": copy_gloss("aqaid-ahl-al-sunna", "qabl"),
 "rusul": copy_gloss("aqaid-ahl-al-sunna", "rusul"),
 "wadaa": copy_gloss("mukhtasar-al-manar", "wadaa"),
 "in-shart": copy_gloss("wasiyyat-abi-yusuf-l5", "in-shart"),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/39.json").write_text(
    json.dumps({"chapter": 39, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 39 for c in man["chapters"]):
    man["chapters"].append({"n": 39, "title": TITLE39})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.39.0"
ADD_EN = (" Chapter 39 continues into ijaz al-hadhf (lines ~2714-2775, sahifa 94-95): s1 is "
          "Yusuf 12:82 (part), s4 al-Kahf 18:79 (part) and s5 Fatir 35:4 (part), received "
          "Qur'anic text quoted exactly in standard imla as the source prints them; s2-s3 are "
          "Suhaym b. Wathil's bayt as the source recites it, split at the hemistich per the "
          "package's verse-reuse precedent.")
ADD_TR = (" Otuz dokuzuncu bâb îcâz-ı hazfe girer (satır ~2714-2775, sahife 94-95): s1 Yûsuf "
          "12:82 (kısmen), s4 Kehf 18:79 (kısmen), s5 Fâtır 35:4 (kısmen) — kaynağın bastığı "
          "standart imlâ ile aynen alınmış mervî Kur'ân metni; s2-s3, Sühaym b. Vesîl'in "
          "beytidir — kaynağın okuduğu şekliyle, paketin beyit bölme teâmülünce mısra "
          "başından ikiye ayrılmıştır.")
if "2714-2775" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
if "jala" not in mo["verbs"]:
    # naqis wawi of bab nasara — the عَفَا road: جَلَا يَجْلُو جَلَاءً.
    mo["verbs"]["jala"] = _sg.naqis1(
        "nasara", "نَاقِصٌ وَاوِيٌّ", "w", "جَلَ", "جْل", "u", "اُجْل",
        "جَلَاء", "جَالٍ (الْجَالِي)", "مَجْلُوّ", "جُلِيَ", "يُجْلَى",
        "نَاقِصٌ وَاوِيٌّ: لَمْ يَجْلُ.")
if "wadaa" not in mo["verbs"]:
    src = json.loads((ROOT / "content/samples/mukhtasar-al-manar/morphology.json").read_text(encoding="utf-8"))
    mo["verbs"]["wadaa"] = src["verbs"]["wadaa"]
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- note 143
GR = ROOT / "content/grammar"
NOTE143 = {
 "id": "ijaz-al-hadhf",
 "title": {"ar": "إِيجَازُ الْحَذْفِ",
           "en": "Brevity by omission",
           "tr": "Îcâz-ı hazif"},
 "level": 6, "group": "balagha",
 "classicalSources": ["تلخيص المفتاح — إيجاز الحذف"],
 "question": {
  "en": ["What fell — a PART of the sentence (mudaf, mawsuf, sifa, shart, jawab, or another part), a WHOLE jumla (the caused, the cause, or neither), or SEVERAL jumlas?",
         "Was anything set in the gap? Usually not; but in وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ a stand-in fills the jawab's place — hadhf's second wajh.",
         "What licenses the omission? Reason and the evident purpose (or reason alone, or the idiom's habit) must both point to WHAT fell and THAT it fell."],
  "tr": ["Düşen ne — cümlenin bir CÜZÜ mü (muzâf, mevsuf, sıfat, şart, cevap veya başka bir cüz), bir CÜMLE mi (müsebbeb, sebep veya ikisi de olmayan), yoksa BİRDEN ÇOK cümle mi?",
         "Boşluğa bir şey kondu mu? Çoğu kez hayır; ama وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ'da cevabın yerine bir bedel geçer — hazfin ikinci vechi.",
         "Hazfe ne izin verir? Akıl ile açık maksat (yahut yalnız akıl, yahut örfün âdeti) hem NEYİN düştüğünü hem düştüğünü göstermelidir."]},
 "plain": {
  "en": "Ijaz's second road: omit, and trust the hearer. What falls is a part — a mudaf (وَاسْأَلِ الْقَرْيَةَ = its people), a mawsuf (أَنَا ابْنُ جَلَا = son of A MAN who…), a sifa (كُلَّ سَفِينَةٍ = every SOUND ship), a shart, a jawab — or a whole jumla, or several. The gap stays open, or a stand-in fills it.",
  "tr": "Îcâzın ikinci yolu: hazfet ve dinleyene güven. Düşen şey cümlenin bir cüzüdür — muzâf (وَاسْأَلِ الْقَرْيَةَ = halkına), mevsuf (أَنَا ابْنُ جَلَا = aşmış BİR ADAMIN oğlu), sıfat (كُلَّ سَفِينَةٍ = her SAĞLAM gemi), şart, cevap — yahut bir cümledir, yahut birden çok. Boşluk ya açık bırakılır ya bir bedel doldurur."},
 "explanation": {
  "en": "The OMITTED PART: a mudaf — وَاسْأَلِ الْقَرْيَةَ (12:82), where أَهْلَ fell and الْقَرْيَة stepped into its nasb; a mawsuf — Suhaym's أَنَا ابْنُ جَلَا, i.e. ابْنُ رَجُلٍ جَلَا; a sifa — يَأْخُذُ كُلَّ سَفِينَةٍ غَصْبًا (18:79), i.e. صَحِيحَةٍ, known from what precedes; a shart — لَيْتَ لِي مَالًا أُنْفِقْهُ, i.e. إِنْ أُرْزَقْهُ أُنْفِقْهُ; a jawab — for pure concision (أَعْرَضُوا understood in Ya-Sin 36:45) or for magnifying beyond what description could hold: وَلَوْ تَرَى إِذْ وُقِفُوا عَلَى النَّارِ, i.e. لَرَأَيْتَ أَمْرًا فَظِيعًا; or another part, as the ma'tuf وَمَنْ أَنْفَقَ مِنْ بَعْدِهِ وَقَاتَلَ understood in Hadid 57:10. The OMITTED JUMLA: the caused — لِيُحِقَّ الْحَقَّ (8:8), i.e. فَعَلَ مَا فَعَلَ; the cause — فَانْفَجَرَتْ (2:60), i.e. فَضَرَبَهُ بِهَا (or, equally received, the shart-part with فَإِنْ ضَرَبْتَ بِهَا فَقَدِ انْفَجَرَتْ); or neither, as فَنِعْمَ الْمَاهِدُونَ (51:48) on its two readings (the jumla هُمْ نَحْنُ omitted, or the mubtada نَحْنُ alone). SEVERAL JUMLAS: أَنَا أُنَبِّئُكُمْ بِتَأْوِيلِهِ فَأَرْسِلُونِ يُوسُفُ (12:45-46), where the sending, the arrival, and the address all fell between two words. The TWO WAJHS: nothing set in the gap (all the above), or a STAND-IN set in it — وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ مِنْ قَبْلِكَ (35:4), where the written clause stands where فَلَا تَحْزَنْ وَاصْبِرْ fell. The DALILS: reason proves a hadhf and the evident purpose names it (حُرِّمَتْ عَلَيْكُمُ الْمَيْتَةُ — the eating, not the carcass, is forbidden); or reason alone does both (وَجَاءَ رَبُّكَ — His command came).",
  "tr": "DÜŞEN CÜZ: muzâf — وَاسْأَلِ الْقَرْيَةَ (12:82): أَهْلَ düşmüş, الْقَرْيَة onun nasbına geçmiştir; mevsuf — Sühaym'ın أَنَا ابْنُ جَلَا'sı, yani ابْنُ رَجُلٍ جَلَا; sıfat — يَأْخُذُ كُلَّ سَفِينَةٍ غَصْبًا (18:79), yani صَحِيحَةٍ, öncesinden bilinir; şart — لَيْتَ لِي مَالًا أُنْفِقْهُ, yani إِنْ أُرْزَقْهُ أُنْفِقْهُ; cevap — sırf ihtisar için (Yâsîn 36:45'te أَعْرَضُوا mukadder) yahut tasvire sığmayacağını bildirmek için: وَلَوْ تَرَى إِذْ وُقِفُوا عَلَى النَّارِ, yani لَرَأَيْتَ أَمْرًا فَظِيعًا; yahut başka bir cüz: Hadîd 57:10'da mukadder mâtuf وَمَنْ أَنْفَقَ مِنْ بَعْدِهِ وَقَاتَلَ. DÜŞEN CÜMLE: müsebbeb — لِيُحِقَّ الْحَقَّ (8:8), yani فَعَلَ مَا فَعَلَ; sebep — فَانْفَجَرَتْ (2:60), yani فَضَرَبَهُ بِهَا (yahut, o da mervî: فَإِنْ ضَرَبْتَ بِهَا فَقَدِ انْفَجَرَتْ takdiriyle şart cüzü); yahut ikisi de olmayan: فَنِعْمَ الْمَاهِدُونَ (51:48), iki okuyuşuyla (هُمْ نَحْنُ cümlesi, yahut yalnız نَحْنُ mübtedâsı). BİRDEN ÇOK CÜMLE: أَنَا أُنَبِّئُكُمْ بِتَأْوِيلِهِ فَأَرْسِلُونِ يُوسُفُ (12:45-46): gönderme, varış ve hitap iki kelimenin arasında düşmüştür. İKİ VECİH: boşluğa bir şey konmaz (yukarıdakilerin hepsi) yahut bir BEDEL konur — وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ مِنْ قَبْلِكَ (35:4): yazılı cümle, فَلَا تَحْزَنْ وَاصْبِرْ'ın yerinde durur. DELİLLER: akıl hazfi ispat eder, açık maksat mahzufu tayin eder (حُرِّمَتْ عَلَيْكُمُ الْمَيْتَةُ — haram olan leş değil, yemektir); yahut ikisini de yalnız akıl yapar (وَجَاءَ رَبُّكَ — emri geldi)."},
 "examples": [
  {"ar": "وَاسْأَلِ الْقَرْيَةَ",
   "en": "the omitted mudaf: ask the town's PEOPLE (12:82).",
   "tr": "mahzuf muzâf: köyün HALKINA sor (12:82).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s1"},
  {"ar": "أَنَا ابْنُ جَلَا وَطَلَّاعُ الثَّنَايَا",
   "en": "the omitted mawsuf: son of A MAN who cleared the heights.",
   "tr": "mahzuf mevsuf: aşmış BİR ADAMIN oğlu.",
   "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "يَأْخُذُ كُلَّ سَفِينَةٍ غَصْبًا",
   "en": "the omitted sifa: every SOUND ship (18:79).",
   "tr": "mahzuf sıfat: her SAĞLAM gemi (18:79).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s4"},
  {"ar": "وَإِنْ يُكَذِّبُوكَ فَقَدْ كُذِّبَتْ رُسُلٌ مِنْ قَبْلِكَ",
   "en": "the stand-in wajh: the written clause holds the omitted jawab's place (35:4).",
   "tr": "bedel vechi: yazılı cümle, mahzuf cevabın yerini tutar (35:4).",
   "sourceStory": "talkhis-al-miftah", "sentence": "s5"}],
 "commonMistakes": [
  {"wrong": "«Hazif, mânâdan bir şey eksiltir»",
   "right": "«Hazif, mahzufu delil ayakta tuttuğu sürece mânâyı eksiksiz bırakır»",
   "why": {"en": "Omission is only ijaz while a dalil points to what fell: reason, the evident purpose, or the idiom's habit. Cut a word no evidence can restore and the result is not hadhf but IKHLAL — the rejected shortness of the previous chapter.",
           "tr": "Hazif, ancak bir delil düşeni gösterdikçe îcâzdır: akıl, açık maksat veya örfün âdeti. Hiçbir delilin geri getiremeyeceği kelimeyi kes — çıkan şey hazif değil İHLÂLDİR: önceki bâbın merdut kısalığı."}}],
 "relatedNotes": ["ijaz-itnab-musawat", "hadhf-wa-taqdir", "in-shartiyya", "afal-khamsa",
                  "naib-al-fail", "hadhf-al-maful", "tark-al-musnad"]}

(GR / "ijaz-al-hadhf.json").write_text(
    json.dumps(NOTE143, ensure_ascii=False, indent=1), encoding="utf-8")

print("talkhis ch39:", len(S), "sentences,", sum(len(x["tokens"]) for x in S),
      "tokens; gloss +", len(GLOSS_ADD), "; morph + jala, wadaa; note 143")
