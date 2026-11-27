# -*- coding: utf-8 -*-
"""Author chapter 26 of talkhis-al-miftah — أَدَوَاتُ التَّصَوُّرِ.

The istifham bab's remaining tasawwur particles (sahifa 72-73):

  • أَيّ asks what SEPARATES one of two partners in a shared matter —
    أَيُّ الْفَرِيقَيْنِ خَيْرٌ مَقَامًا — and it is the ONE interrogative noun
    that DECLINES (it never leaves the idafa).
  • كَمْ asks the NUMBER, its tamyiz riding behind مِنْ in the aya —
    سَلْ بَنِي إِسْرَائِيلَ كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ.
  • كَيْفَ the STATE, أَيْنَ the PLACE, مَتَى the TIME — each a mabni noun
    reading its i'rab off its position.
  • أَيَّانَ the FUTURE, kept for GREAT things — يَسْأَلُ أَيَّانَ يَوْمُ
    الْقِيَامَةِ (al-Qiyama 75:6).
  • أَنَّى wears two faces: كَيْفَ before a verb (فَأْتُوا حَرْثَكُمْ أَنَّى
    شِئْتُمْ — taught in the note), مِنْ أَيْنَ before a nominal — يَا
    مَرْيَمُ أَنَّى لَكِ هَذَا (Al 'Imran 3:37).

ATTRIBUTION: the ayat are received Qur'anic text quoted exactly — the
source's surah citations for two of them are corrected against the mushaf
and the corrections are recorded in the manifest attribution (see below).
كَيْفَ أَنْتَ، أَيْنَ زَيْدٌ، مَتَى جِئْتَ are the source's own worked
examples verbatim (research/sources/talkhis-al-miftah-balagha.txt lines
~2086-2110, sahifa 72-73), Ottoman plain-alif normalized to standard
orthography — a recorded normalization.

Grammar this chapter teaches:
  • note 128 `adawat-al-tasawwur` — the seven adawat and their matlubs,
    ayy's i'rab, kam's tamyiz, ayyan's tafkhim, anna's two faces.
  • engine work: the conditional nouns filed as NOUNS (ISM_KINDS), the
    istifham-face router (fewer than two verbs after the adat = question),
    CaseEngine's mu'rab-أي exception, the light-imperative table (سَلْ →
    اِسْأَلْ at the matching layer), exact-beats-loose across the corpus
    walk, and the shadda/sukun repair in the mabni-ending guard.
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
S = []

TITLE26 = {"ar": "أَدَوَاتُ التَّصَوُّرِ: أَيٌّ وَكَمْ وَكَيْفَ وَأَيْنَ وَمَتَى",
           "en": "The Tasawwur Particles: Ayy, Kam, Kayfa, Ayna, Mata",
           "tr": "Tasavvur Edatları: Eyy, Kem, Keyfe, Eyne, Metâ"}

# ------------------------------------------------- s1 — Maryam 19:73, ayy
S.append({"id": "s1", "translation": {
 "en": "Which of the two camps is better in station? (Maryam 19:73 — ayy asks what separates two partners in a shared matter.)",
 "tr": "İki zümreden hangisi makamca daha hayırlıdır? (Meryem 19:73 — eyy, ortak bir işte iki ortağı ayıranı sorar.)"},
 "tokens": [
  tok("أَيُّ","ayy","pron",["adawat-al-tasawwur","al-istifham"],
      "اسْمُ اسْتِفْهَامٍ مُعْرَبٌ — وَهُوَ الْوَحِيدُ الْمُعْرَبُ بَيْنَ أَخَوَاتِهِ لِمُلَازَمَتِهِ الْإِضَافَةَ — مُبْتَدَأٌ مَرْفُوعٌ وَعَلَامَةُ رَفْعِهِ الضَّمَّةُ الظَّاهِرَةُ، وَهُوَ مُضَافٌ.",
      "«which» — the interrogative أَيّ, and the ONE that DECLINES: it never leaves the idafa, so it never lost its i'rab — here mubtada, marfu' by a plainly written damma, and mudaf. Its ask is the ta'yin: what separates one of two partners in a matter both share.",
      "«hangisi» — istifham أَيّ'i ve MU'REB olan teki: izâfetten hiç ayrılmaz, i'râbını da hiç yitirmemiştir — burada mübtedâ, açık dammeyle merfû ve muzâf. Sorusu tayindir: ikisini de kapsayan bir işte iki ortaktan birini ayıran nedir."),
  tok("الْفَرِيقَيْنِ","fariq","noun",["adawat-al-tasawwur","al-muthanna"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ مُثَنًّى.",
      "«of the two camps» — mudaf ilayh, majrur by the YA of the dual. The dual is no accident: أَيّ's ask needs a shared pool of exactly-known members to divide.",
      "«iki zümrenin» — muzâfun ileyh; tesniye YÂSIyla mecrur. Tesniye tesadüf değildir: أَيّ'in sorusu, bölecek üyeleri belli bir ortak havuz ister."),
  tok("خَيْرٌ","khayr","noun",["adawat-al-tasawwur"],
      "خَبَرٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ — وَأَصْلُهُ أَفْعَلُ تَفْضِيلٍ حُذِفَتْ هَمْزَتُهُ.",
      "«better» — the khabar, marfu' by the plain damma; at bottom an ism tafdil whose hamza the language wore away (أَخْيَر → خَيْر).",
      "«daha hayırlı» — haber, açık dammeyle merfû; aslında hemzesi aşınmış bir ism-i tafdîl (أَخْيَر → خَيْر)."),
  tok("مَقَامًا","maqam","noun",["adawat-al-tasawwur","tamyiz"],
      "تَمْيِيزٌ مَنْصُوبٌ بِالْفَتْحَةِ الظَّاهِرَةِ — مَيَّزَ جِهَةَ الْخَيْرِيَّةِ.",
      "«in station» — tamyiz, mansub by the plain fatha: it names the RESPECT in which the two camps are weighed. The aya is the disbelievers' boast — and the question-machine works even in a boasting mouth.",
      "«makamca» — temyiz, açık fethayla mansub: iki zümrenin HANGİ CİHETTEN tartıldığını adlandırır. Âyet kâfirlerin övünmesidir — soru makinesi övünen ağızda bile işler.",
      punct="؟")],
 "jumal": [
  J("أَيُّ الْفَرِيقَيْنِ خَيْرٌ مَقَامًا",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The question-sentence itself: nominal, insha'i, opening its discourse — no mahall. The istifham noun OWNS the sentence's head (the sadara right), which is why every question in this chapter fronts its adat.",
    "Soru cümlesinin kendisi: isim cümlesi, inşâî, söze başlıyor — mahalli yok. İstifham ismi cümlenin başını MÜLK edinir (sadâret hakkı); bu bâbdaki her sorunun edatını öne almasının sebebi budur."),
  J("أَيُّ الْفَرِيقَيْنِ",
    "أَيٌّ مُعْرَبَةٌ لِمُلَازَمَةِ الْإِضَافَةِ — إِعْرَابُهَا هُوَ الدَّرْسُ.",
    "THE WAJH: among the interrogative nouns — all mabni — أَيّ alone declines, and the reason is doctrine in one line: it never leaves the idafa, so the idafa's anchor kept its ending alive. One damma carries the whole lesson.",
    "VECİH: hepsi mebnî olan soru isimleri içinde yalnız أَيّ i'râb alır; sebebi tek satırlık doktrindir: izâfetten hiç ayrılmaz, izâfet çıpası da sonunu diri tutmuştur. Bütün dersi tek damme taşır.")]})

# ------------------------------------------------- s2 — Baqara 2:211, kam
S.append({"id": "s2", "translation": {
 "en": "Ask the Children of Israel how many a clear sign We gave them. (al-Baqara 2:211 — kam asks the number, its counted kind behind min.)",
 "tr": "İsrâiloğullarına sor: onlara nice açık âyet verdik. (Bakara 2:211 — kem sayıyı sorar; sayılan türü min arkasındadır.)"},
 "tokens": [
  tok("سَلْ","saala","verb",["adawat-al-tasawwur"],
      "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى السُّكُونِ، حُذِفَتْ هَمْزَتُهُ تَخْفِيفًا — أَصْلُهُ اِسْأَلْ — وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ أَنْتَ.",
      "«ask!» — the amr of سَأَلَ, mabni on the sukun, its 'ayn-hamza dropped by the received takhfif (the full اِسْأَلْ is equally sound; sentence-initially the Qur'an prefers the light form). The doer is the concealed «you».",
      "«sor!» — سَأَلَ'nin emri, sükûn üzere mebnî; ayn-hemzesi mervî tahfifle düşmüş (tam اِسْأَلْ de sahihtir; cümle başında Kur'ân hafif şekli yeğler). Fâil gizli «sen»dir."),
  tok("بَنِي","banu","noun",["adawat-al-tasawwur"],
      "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْيَاءُ لِأَنَّهُ مُلْحَقٌ بِجَمْعِ الْمُذَكَّرِ السَّالِمِ، حُذِفَتْ نُونُهُ لِلْإِضَافَةِ، وَهُوَ مُضَافٌ.",
      "«the Children of» — first object, mansub by the YA (it is attached to the sound masculine plural's i'rab), its nun dropped for the idafa, and itself mudaf.",
      "«oğullarına» — birinci mef'ûl; cem-i müzekker sâlime mülhak olduğundan YÂ ile mansub; nûnu izâfet için düşmüş ve kendisi muzâf."),
  tok("إِسْرَائِيلَ","israil","propn",["adawat-al-tasawwur","mamnu-min-sarf"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْفَتْحَةُ نِيَابَةً عَنِ الْكَسْرَةِ لِأَنَّهُ مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالْعُجْمَةِ.",
      "«Israel» — mudaf ilayh, majrur by a FATHA standing in for the kasra: a proper name of foreign origin is barred from tanwin and bends its jarr to the fatha.",
      "«İsrâil» — muzâfun ileyh; kesra yerine geçen FETHA ile mecrur: alemiyet ve ucme sebebiyle gayr-i munsariftir, cerri fethaya döner."),
  tok("كَمْ","kam","pron",["adawat-al-tasawwur","tamyiz"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ ثَانٍ مُقَدَّمٌ لِآتَيْنَا — وَلَهُ الصَّدَارَةُ.",
      "«how many» — the interrogative كَمْ, mabni on the sukun, standing in NASB position as the fronted second object of آتَيْنَا: the question word claims the sentence's head (sadara), so the object walks to the front.",
      "«kaç / nice» — istifham كَمْ'i; sükûn üzere mebnî, آتَيْنَا'nın öne alınmış ikinci mef'ûlü olarak nasb mevkiinde: soru kelimesi cümle başını ister (sadâret), mef'ûl de başa yürür."),
  tok("آتَيْنَاهُمْ","aataa","verb",["adawat-al-tasawwur"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِنَا الْفَاعِلِينَ، وَ«نَا» فَاعِلٌ، وَ«هُمْ» مَفْعُولٌ بِهِ أَوَّلُ.",
      "«We gave them» — the madi of آتَى (Form IV: to GRANT, taking two objects), mabni on the sukun for the attached doers' نَا; «هُمْ» is its first object, and كَمْ before it the second.",
      "«onlara verdik» — آتَى'nın mâzîsi (IV. bâb: BAĞIŞLAMAK; iki mef'ûl alır); fâil نَا'sına bitiştiği için sükûn üzere mebnî; «هُمْ» birinci mef'ûlü, öndeki كَمْ ikincisidir.",
      segments=[seg("آتَيْنَا","aataa","verb"), seg("هُمْ","hum","pron")]),
  tok("مِنْ","min","part",["adawat-al-tasawwur","huruf-jarr"],
      "حَرْفُ جَرٍّ — يُبَيِّنُ تَمْيِيزَ كَمْ الْمُبْهَمَةِ.",
      "«of» — the jarr letter that carries كَمْ's tamyiz: the number was asked bare, and مِنْ opens the phrase that names WHAT was counted.",
      "«-den» — كَمْ'in temyizini taşıyan cer harfi: sayı çıplak soruldu; NEYİN sayıldığını adlandıran öbeği مِنْ açar."),
  tok("آيَةٍ","aya","noun",["adawat-al-tasawwur","tamyiz"],
      "تَمْيِيزُ كَمْ مَجْرُورٌ بِمِنْ لَفْظًا — وَجَرُّهُ بِمِنْ ظَاهِرَةً هُوَ الْفَاشِي فِي التَّنْزِيلِ.",
      "«sign» — كَمْ's tamyiz, majrur by the explicit مِنْ; with the letter written out this jarr is the Qur'an's favoured shape. Absent the مِنْ, the asker's tamyiz would stand MANSUB — and that case-split is what tells the asking كَمْ from the telling one.",
      "«âyet» — كَمْ'in temyizi; açık مِنْ ile mecrur; harf yazılınca bu cer Kur'ân'ın yeğlediği kalıptır. مِنْ olmasaydı soranın temyizi MANSUB dururdu — ve o hâl ayrımı, soran كَمْ'i söyleyenden ayıran şeydir."),
  tok("بَيِّنَةٍ","bayyina","noun",["adawat-al-tasawwur"],
      "نَعْتٌ لِآيَةٍ مَجْرُورٌ مِثْلُهَا بِالْكَسْرَةِ الظَّاهِرَةِ.",
      "«clear» — na't to آيَةٍ, majrur like it by the plain kasra.",
      "«açık» — آيَةٍ'e na't; onun gibi açık kesrayla mecrur.",
      punct="؟")],
 "jumal": [
  J("سَلْ بَنِي إِسْرَائِيلَ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The command-frame: verbal, insha'i, no mahall. Its verb سَلْ then does something rare — it stops governing what it most wants (its second object) the moment a question begins.",
    "Emir çerçevesi: fiil cümlesi, inşâî, mahalli yok. Fiili سَلْ sonra nadir bir şey yapar — soru başlar başlamaz en çok istediğini (ikinci mef'ûlünü) yönetmeyi bırakır."),
  J("كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ",
    "جُمْلَةُ الِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ سَدَّتْ مَسَدَّ الْمَفْعُولِ الثَّانِي لِسَلْ — عُلِّقَ الْفِعْلُ لِصَدَارَةِ الِاسْتِفْهَامِ.",
    "THE TA'LIQ: the whole question-clause stands in nasb position filling سَلْ's second-object seat — the verb is SUSPENDED (mu'allaq) because the istifham owns its sentence's head and no outside governor may reach past it. The question is handed over whole, never word by word.",
    "TA'LÎK: soru cümlesinin tamamı, سَلْ'in ikinci mef'ûl koltuğunu doldurarak nasb mevkiinde durur — fiil ASKIYA alınmıştır (muallak); çünkü istifham kendi cümlesinin başına sahiptir ve dış âmil onu aşıp içeri uzanamaz. Soru bütün olarak teslim edilir, asla kelime kelime değil."),
  J("كَمْ … مِنْ آيَةٍ",
    "كَمْ: سُؤَالُ الْعَدَدِ — وَتَمْيِيزُهَا بِمِنْ.",
    "THE WAJH: kam = the number-ask, and its counted kind rides behind مِنْ. The twin kam KHABARIYYA tells («many a sign») instead of asking — and where مِنْ is absent, the tamyiz's case splits them: the asker's mansub, the teller's majrur.",
    "VECİH: kem = sayı sorusu; sayılan türü مِنْ arkasında gider. İkizi haberiyye كَمْ sormaz, SÖYLER («nice âyet») — ve مِنْ yoksa ikisini temyizin hâli ayırır: soranınki mansub, söyleyeninki mecrur.")]})

# ------------------------------------------------- s3 — kayfa
S.append({"id": "s3", "translation": {
 "en": "How are you? (kayfa asks the STATE — a hal-word answers, never a yes.)",
 "tr": "Nasılsın? (keyfe HÂLİ sorar — bir hâl kelimesi cevaplar, asla evet değil.)"},
 "tokens": [
  tok("كَيْفَ","kayfa","pron",["adawat-al-tasawwur","al-istifham"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ خَبَرٌ مُقَدَّمٌ — يُسْأَلُ بِهِ عَنِ الْحَالِ.",
      "«how» — a mabni interrogative NOUN on the fatha, standing in RAF' position as fronted khabar: the state is asked, and the answer must be a state-word (صَالِحٌ، مَرِيضٌ), never yes.",
      "«nasıl» — fetha üzere mebnî bir soru İSMİ; mukaddem haber olarak REF mevkiinde: hâl sorulur ve cevap bir hâl kelimesi olmalıdır (iyiyim, hastayım), asla evet değil."),
  tok("أَنْتَ","anta","pron",["adawat-al-tasawwur"],
      "ضَمِيرٌ مُنْفَصِلٌ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
      "«you» — the detached pronoun, deferred mubtada in raf' position; the question word took the head-seat its sadara demands.",
      "«sen» — munfasıl zamir; muahhar mübtedâ olarak ref mevkiinde; baş koltuğu, sadâretin istediği gibi soru kelimesi aldı.",
      punct="؟")],
 "jumal": [
  J("كَيْفَ أَنْتَ",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ — وَتَقْدِيمُ الْخَبَرِ وَاجِبٌ لِصَدَارَةِ الِاسْتِفْهَامِ.",
    "The smallest complete question in the bab: khabar + mubtada, and the fronting is WAJIB — an istifham noun may not stand anywhere but first. The taqdim chapter's rule, met here as a hard constraint rather than a choice.",
    "Bâbın en küçük tam sorusu: haber + mübtedâ; ve takdim VÂCİBdir — istifham ismi baştan başka yerde duramaz. Takdim bâbının kuralı, burada tercih değil kesin kayıt olarak karşılanır."),
  J("كَيْفَ أَنْتَ",
    "كَيْفَ: سُؤَالُ الْحَالِ — وَجَوَابُهُ حَالٌ لَا «نَعَمْ».",
    "THE WAJH: kayfa = the state-ask. Its answer-shape is its diagnosis — a hal-word where ayna takes a place, mata a time, man a name. The tasawwur adawat divide the world of answers between them.",
    "VECİH: keyfe = hâl sorusu. Cevap kalıbı teşhisidir — bir hâl kelimesi; eyne yer, metâ zaman, men ad alır. Tasavvur edatları cevaplar dünyasını aralarında bölüşür.")]})

# ------------------------------------------------- s4 — ayna
S.append({"id": "s4", "translation": {
 "en": "Where is Zayd? (ayna asks the PLACE — a mabni noun in nasb position on the zarfiyya.)",
 "tr": "Zeyd nerede? (eyne YERİ sorar — zarfiyye üzere nasb mevkiinde mebnî bir isim.)"},
 "tokens": [
  tok("أَيْنَ","ayna","pron",["adawat-al-tasawwur","al-istifham"],
      "اسْمُ اسْتِفْهَامٍ لِلْمَكَانِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ — خَبَرٌ مُقَدَّمٌ.",
      "«where» — the place-ask, mabni on the fatha, in NASB position on the zarfiyya, standing as fronted khabar. The same written word jazms two verbs as a conditional noun — the FRAME, not the word, decides the face.",
      "«nerede» — mekân sorusu; fetha üzere mebnî, zarfiyye üzere NASB mevkiinde, mukaddem haber. Aynı yazılı kelime şart ismi olarak iki fiili cezmeder — yüzü kelime değil, ÇERÇEVE belirler."),
  tok("زَيْدٌ","zayd","propn",["adawat-al-tasawwur"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ.",
      "«Zayd» — deferred mubtada, marfu' by the plain damma, waiting for a PLACE as his answer.",
      "«Zeyd» — muahhar mübtedâ; açık dammeyle merfû; cevap olarak bir YER bekler.",
      punct="؟")],
 "jumal": [
  J("أَيْنَ زَيْدٌ",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ — لَا فِعْلَ فِيهَا أَصْلًا فَلَا شَرْطَ.",
    "No verb stands anywhere in the sentence — so the conditional reading is not weak, it is IMPOSSIBLE: a jazim with nothing to jazm. The question is what remains, and the engine-room rule is the chapter's: count the verbs before naming the face.",
    "Cümlede hiçbir yerde fiil yok — öyleyse şart okuması zayıf değil, İMKÂNSIZdır: cezmedecek şeyi olmayan bir câzim. Kalan sorudur; makine dairesinin kuralı bâbın kuralıdır: yüzü adlandırmadan önce fiilleri say."),
  J("أَيْنَ زَيْدٌ",
    "أَيْنَ: سُؤَالُ الْمَكَانِ — وَهِيَ مِنْ أَخَوَاتِ مَتَى فِي الشَّرْطِ أَيْضًا.",
    "THE WAJH: ayna = the place-ask — and the same noun serves among the jawazim. One word, two offices, and its case-position (nasb on the zarfiyya) holds in both.",
    "VECİH: eyne = mekân sorusu — ve aynı isim cevâzim arasında da hizmet eder. Tek kelime, iki vazife; hâl mevkii (zarfiyye üzere nasb) ikisinde de geçerlidir.")]})

# ------------------------------------------------- s5 — mata
S.append({"id": "s5", "translation": {
 "en": "When did you come? (mata asks the TIME — one verb and the sentence ends: a question, not a condition.)",
 "tr": "Ne zaman geldin? (metâ ZAMANI sorar — tek fiille cümle biter: şart değil, soru.)"},
 "tokens": [
  tok("مَتَى","mata-istifham","pron",["adawat-al-tasawwur","al-istifham"],
      "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ مَبْنِيٌّ عَلَى السُّكُونِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ الزَّمَانِيَّةِ — مُتَعَلِّقٌ بِجِئْتَ.",
      "«when» — the time-ask, mabni on the sukun, in nasb position on the temporal zarfiyya, attached to جِئْتَ. Write a second, jazmed verb after it and the SAME word becomes a conditional noun — the frame decides.",
      "«ne zaman» — zaman sorusu; sükûn üzere mebnî, zaman zarfiyyesi üzere nasb mevkiinde, جِئْتَ'ye müteallik. Ardına cezimli ikinci bir fiil yazın, AYNI kelime şart ismi olur — çerçeve karar verir."),
  tok("جِئْتَ","jaa","verb",["adawat-al-tasawwur"],
      "فِعْلٌ مَاضٍ مَبْنِيٌّ عَلَى السُّكُونِ لِاتِّصَالِهِ بِتَاءِ الْفَاعِلِ، وَالتَّاءُ فَاعِلٌ.",
      "«you came» — the madi of جَاءَ, mabni on the sukun for the doer's ta; the ta is the fa'il. One verb, and the sentence closes — which is exactly what rules the condition out.",
      "«geldin» — جَاءَ'nin mâzîsi; fâil tâsına bitiştiği için sükûn üzere mebnî; tâ fâildir. Tek fiil ve cümle kapanır — şartı dışlayan tam da budur.",
      punct="؟")],
 "jumal": [
  J("مَتَى جِئْتَ",
    "جُمْلَةٌ فِعْلِيَّةٌ إِنْشَائِيَّةٌ — فِعْلٌ وَاحِدٌ فَلَا جَوَابَ يُنْتَظَرُ.",
    "One verb, no jawab in sight: the conditional مَتَى needs two clauses to bind and finds one. The minimal pair is the teaching — مَتَى جِئْتَ asks; مَتَى جِئْتَنِي أَكْرَمْتُكَ conditions.",
    "Tek fiil, görünürde cevap yok: şart مَتَى'sı bağlayacak iki cümle ister, bir tane bulur. Asgarî çift dersin kendisidir — مَتَى جِئْتَ sorar; مَتَى جِئْتَنِي أَكْرَمْتُكَ şart koşar."),
  J("مَتَى جِئْتَ",
    "مَتَى: سُؤَالُ الزَّمَانِ الْمُطْلَقِ — مَاضِيهِ وَمُسْتَقْبَلِهِ.",
    "THE WAJH: mata = the time-ask, indifferent to past or future — where its rare sister أَيَّانَ (next sentence) is kept for the future alone, and for great things.",
    "VECİH: metâ = mutlak zaman sorusu — geçmişine de geleceğine de kayıtsız; nadir kız kardeşi أَيَّانَ (sonraki cümle) ise yalnız geleceğe ve büyük şeylere saklanır.")]})

# ------------------------------------------------- s6 — Qiyama 75:6, ayyan
S.append({"id": "s6", "translation": {
 "en": "He asks: when is the Day of Rising? (al-Qiyama 75:6 — ayyan, the future-ask kept for great things.)",
 "tr": "Sorar: kıyâmet günü ne zaman? (Kıyâme 75:6 — eyyâne: büyük şeylere saklanan istikbâl sorusu.)"},
 "tokens": [
  tok("يَسْأَلُ","saala","verb",["adawat-al-tasawwur"],
      "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِالضَّمَّةِ الظَّاهِرَةِ، وَالْفَاعِلُ ضَمِيرٌ مُسْتَتِرٌ تَقْدِيرُهُ هُوَ — وَعُلِّقَ عَنِ الْجُمْلَةِ بَعْدَهُ لِصَدَارَةِ الِاسْتِفْهَامِ.",
      "«he asks» — the mudari of سَأَلَ, marfu' by the plain damma, its doer the concealed «he» (the denier of the Rising); and it is SUSPENDED from the clause after it — the istifham's sadara shields its sentence from outside government.",
      "«sorar» — سَأَلَ'nin muzârisi; açık dammeyle merfû; fâili gizli «o» (kıyâmeti inkâr eden); ve ardındaki cümleden ASKIYA alınmıştır — istifhamın sadâreti, cümlesini dış âmilden korur."),
  tok("أَيَّانَ","ayyan","pron",["adawat-al-tasawwur","al-istifham"],
      "اسْمُ اسْتِفْهَامٍ لِلزَّمَانِ الْمُسْتَقْبَلِ مَبْنِيٌّ عَلَى الْفَتْحِ فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ — خَبَرٌ مُقَدَّمٌ، وَلَا يُسْأَلُ بِهِ إِلَّا عَنِ الْمُعَظَّمَاتِ.",
      "«when» — the FUTURE-ask, mabni on the fatha, nasb position on the zarfiyya, fronted khabar. The books keep it for GREAT things — the rarity of the word is part of the awe.",
      "«ne zaman» — İSTİKBÂL sorusu; fetha üzere mebnî, zarfiyye üzere nasb mevkiinde, mukaddem haber. Kitaplar onu BÜYÜK şeylere saklar — kelimenin nadirliği heybetin parçasıdır."),
  tok("يَوْمُ","yawm","noun",["adawat-al-tasawwur"],
      "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ بِالضَّمَّةِ وَهُوَ مُضَافٌ.",
      "«the Day» — deferred mubtada, marfu' by the damma, and mudaf.",
      "«günü» — muahhar mübtedâ; dammeyle merfû ve muzâf."),
  tok("الْقِيَامَةِ","qiyama","noun",["adawat-al-tasawwur"],
      "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْكَسْرَةِ الظَّاهِرَةِ.",
      "«of the Rising» — mudaf ilayh, majrur by the plain kasra.",
      "«kıyâmetin» — muzâfun ileyh; açık kesrayla mecrur.",
      punct="؟")],
 "jumal": [
  J("يَسْأَلُ",
    "جُمْلَةٌ فِعْلِيَّةٌ ابْتِدَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The report-frame: someone asks. What he asks arrives as a WHOLE clause — see the next row — because a question cannot be handed over in pieces.",
    "Haber çerçevesi: biri soruyor. NE sorduğu BÜTÜN bir cümle olarak gelir — sonraki satıra bakın — çünkü soru parça parça teslim edilemez."),
  J("أَيَّانَ يَوْمُ الْقِيَامَةِ",
    "جُمْلَةُ الِاسْتِفْهَامِ فِي مَحَلِّ نَصْبٍ مَفْعُولٌ بِهِ لِيَسْأَلُ — بِالتَّعْلِيقِ.",
    "The question-clause stands whole in nasb position as يَسْأَلُ's object, by TA'LIQ: the asking verb reports the question, it does not govern inside it. Same machine as سَلْ … كَمْ, one sentence over.",
    "Soru cümlesi, TA'LÎK yoluyla يَسْأَلُ'nün mef'ûlü olarak bütün hâlinde nasb mevkiinde durur: soran fiil soruyu nakleder, içine amel etmez. سَلْ … كَمْ ile aynı makine, bir cümle ötede."),
  J("أَيَّانَ يَوْمُ الْقِيَامَةِ",
    "أَيَّانَ فِي مَوْضِعِ التَّفْخِيمِ — لِلْمُعَظَّمَاتِ.",
    "THE WAJH: tafkhim by particle-choice. The scoffer's own mouth is made to ask with the awe-word — أَيَّانَ, never a plain مَتَى — and the choice of adat carries the Day's weight before the answer comes.",
    "VECİH: edat seçimiyle tafhîm. Alaycının kendi ağzına heybet kelimesiyle sorduruluyor — أَيَّانَ; düz bir مَتَى değil — ve edat seçimi, cevap gelmeden Günün ağırlığını taşıyor.")]})

# ------------------------------------------------- s7 — Al 'Imran 3:37, anna
S.append({"id": "s7", "translation": {
 "en": "O Maryam, whence is this for you? (Al 'Imran 3:37 — anna in its min-ayna face: the SOURCE is asked.)",
 "tr": "Ey Meryem, bu sana nereden? (Âl-i İmrân 3:37 — enna, min-eyne yüzünde: KAYNAK sorulur.)"},
 "tokens": [
  tok("يَا","ya","part",["adawat-al-tasawwur","vocative-munada"],
      "حَرْفُ نِدَاءٍ.",
      "«O» — the vocative letter; Zakariyya calls before he asks.",
      "«ey» — nidâ harfi; Zekeriyyâ sormadan önce sesleniyor."),
  tok("مَرْيَمُ","maryam","propn",["adawat-al-tasawwur","vocative-munada"],
      "مُنَادَى مُفْرَدٌ عَلَمٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ نَصْبٍ.",
      "«Maryam» — a single proper-name munada, BUILT on the damma in nasb position: the call's classic shape, the damma worn as bina, never as raf'.",
      "«Meryem» — müfred alem münâdâ; nasb mevkiinde damme üzere MEBNÎ: nidânın klasik kalıbı; damme ref değil bina olarak taşınır."),
  tok("أَنَّى","anna-istifham","pron",["adawat-al-tasawwur","al-istifham"],
      "اسْمُ اسْتِفْهَامٍ مَبْنِيٌّ عَلَى السُّكُونِ — بِمَعْنَى مِنْ أَيْنَ هُنَا — فِي مَحَلِّ نَصْبٍ عَلَى الظَّرْفِيَّةِ، خَبَرٌ مُقَدَّمٌ.",
      "«whence» — the interrogative أَنَّى, mabni, here in its مِنْ أَيْنَ face (before a nominal, the SOURCE is asked); in nasb position on the zarfiyya as fronted khabar. Before a verb it reads as كَيْفَ instead — أَنَّى شِئْتُمْ, «in whatever manner».",
      "«nereden» — istifham أَنَّى'sı; mebnî; burada مِنْ أَيْنَ yüzünde (isim cümlesi önünde KAYNAK sorulur); zarfiyye üzere nasb mevkiinde mukaddem haber. Fiil önünde ise كَيْفَ okunur — أَنَّى شِئْتُمْ, «dilediğiniz şekilde»."),
  tok("لَكِ","li","part",["adawat-al-tasawwur"],
      "اللَّامُ حَرْفُ جَرٍّ وَالْكَافُ ضَمِيرٌ مُتَّصِلٌ فِي مَحَلِّ جَرٍّ — وَشِبْهُ الْجُمْلَةِ حَالٌ مِنَ الْإِشَارَةِ.",
      "«for you» — the jarr lam with the attached feminine kaf in jarr position; the phrase stands as hal of the pointed-at provision.",
      "«sana» — cer lâmı ile dişil muttasıl kâf, cer mevkiinde; öbek, işaret edilen rızkın hâli olarak durur.",
      segments=[seg("لَ","li","part"), seg("كِ","pron-2fs","pron")]),
  tok("هَذَا","hadha","pron",["adawat-al-tasawwur"],
      "اسْمُ إِشَارَةٍ مَبْنِيٌّ فِي مَحَلِّ رَفْعٍ مُبْتَدَأٌ مُؤَخَّرٌ.",
      "«this» — the demonstrative as deferred mubtada in raf' position: the out-of-season provision itself, pointed at.",
      "«bu» — muahhar mübtedâ olarak ref mevkiinde işaret ismi: mevsimsiz rızkın kendisi, işaret edilerek.",
      punct="؟")],
 "jumal": [
  J("يَا مَرْيَمُ",
    "جُمْلَةُ النِّدَاءِ إِنْشَائِيَّةٌ لَا مَحَلَّ لَهَا.",
    "The call-clause: insha'i, no mahall — and its munada wears the bina-damma the case-audit lists among the endings that only LOOK like i'rab.",
    "Nidâ cümlesi: inşâî, mahalli yok — ve münâdâsı, hâl denetiminin «i'râba yalnız BENZEYEN sonlar» listesindeki bina dammesini taşır."),
  J("أَنَّى لَكِ هَذَا",
    "جُمْلَةٌ اسْمِيَّةٌ إِنْشَائِيَّةٌ — وَلَا فِعْلَ فِيهَا فَتَعَيَّنَ مَعْنَى مِنْ أَيْنَ.",
    "No verb anywhere in the clause — so the كَيْفَ face has nothing to attach to and the مِنْ أَيْنَ face is SETTLED by structure: the same verb-counting that split متى's condition from its question splits أَنَّى's two meanings.",
    "Cümlede hiçbir yerde fiil yok — كَيْفَ yüzünün tutunacak şeyi kalmaz ve مِنْ أَيْنَ yüzü YAPIYLA kesinleşir: metâ'nın şartını sorusundan ayıran fiil sayımı, أَنَّى'nın iki mânâsını da ayırır."),
  J("أَنَّى لَكِ هَذَا",
    "أَنَّى تَعْدِلُ كَيْفَ تَارَةً وَمِنْ أَيْنَ أُخْرَى.",
    "THE WAJH: one particle, two equivalences — the books say «sometimes» in both directions, and the aya-pair carries them: أَنَّى شِئْتُمْ (= however), أَنَّى لَكِ هَذَا (= from where). Maryam's answer names a SOURCE — هُوَ مِنْ عِنْدِ اللَّهِ — proving which face was asked.",
    "VECİH: tek edat, iki denklik — kitaplar iki yönde de «bazen» der ve âyet çifti ikisini de taşır: أَنَّى شِئْتُمْ (= nasıl dilersen), أَنَّى لَكِ هَذَا (= nereden). Meryem'in cevabı bir KAYNAK adlandırır — هُوَ مِنْ عِنْدِ اللَّهِ — hangi yüzün sorulduğunun ispatı.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 "ayy": g("أَيّ", None, "pron", "which? (the one DECLINING interrogative noun — it never leaves the idafa)",
          "hangi? (i'râb alan tek soru ismi — izâfetten hiç ayrılmaz)", 4),
 "kam": g("كَمْ", None, "pron", "how many? (interrogative; its khabari twin means «many a»)",
          "kaç? (istifham; haberiyye ikizi «nice» demektir)", 3),
 "ayyan": g("أَيَّانَ", None, "pron", "when? (of the future, kept for great things)",
            "ne zaman? (istikbâl için; büyük şeylere saklanır)", 5),
 "anna-istifham": g("أَنَّى", None, "pron", "how? / from where? (context decides between the two)",
                    "nasıl? / nereden? (ikisini bağlam ayırır)", 5),
 "mata-istifham": g("مَتَى", None, "pron", "when? (interrogative; the same word also serves as a conditional noun)",
                    "ne zaman? (istifham; aynı kelime şart ismi olarak da hizmet eder)", 2),
 "fariq": g("فَرِيق", "ف ر ق", "noun", "party, camp, group", "zümre, fırka, taraf", 4),
 "banu": g("بَنُونَ", "ب ن ي", "noun", "sons, children (declines by letters, attached to the sound plural; بَنُو in idafa)",
           "oğullar (harflerle i'râb alır, cem-i sâlime mülhak; izâfette بَنُو)", 3),
 "israil": g("إِسْرَائِيل", None, "propn", "Israel (Ya'qub); barred from tanwin for name and foreignness",
             "İsrâil (Ya'kūb); alemiyet ve ucme sebebiyle gayr-i munsarif", 4),
 "maryam": g("مَرْيَم", None, "propn", "Maryam, mother of 'Isa; barred from tanwin",
             "Meryem, Îsâ'nın annesi; gayr-i munsarif", 3),
 "aya": g("آيَة", "أ ي ي", "noun", "sign; verse of the Qur'an", "âyet; alâmet, nişâne", 2, plural="آيَات"),
 "aataa": g("آتَى", "أ ت ي", "verb", "to give, to grant (Form IV; takes two objects)",
            "vermek, bağışlamak (IV. bâb; iki mef'ûl alır)", 4, form="IV"),
 "maqam": copy_gloss("kitab-al-buyu", "maqam"),
 "bayyina": copy_gloss("aqaid-ahl-al-sunna", "bayyina"),
 "ayna": copy_gloss("jumal-al-tadrib", "ayna"),
 "qiyama": copy_gloss("bad-al-amali", "qiyama"),
}

# ---------------------------------------------------------------- morphology
# آتَى — Form IV of أ ت ي: mahmuz al-fa AND naqis ya'i at once. The conjugator
# refuses hamzated roots, so every cell is hand-stored, mirrored on the
# corpus's own أَعْطَى (bad-al-amali `aata`) shape: same bab, same endings, the
# hamza rules layered on top — the madda of آتَيْنَا is أَ + أْ written as one
# letter, and the first person أُوتِي turns its second hamza to waw after the
# damma (the آمَنَ → أُومِنُ rule).
AATAA = {
 "bab": "الْبَابُ الرَّابِعُ: أَفْعَلَ يُفْعِلُ إِفْعَالًا — مَهْمُوزُ الْفَاءِ نَاقِصٌ",
 "wazn": "أَفْعَلَ يُفْعِلُ",
 "masdar": "إِيتَاء",
 "ismFail": "مُؤْتٍ",
 "ismMaful": "مُؤْتًى",
 "mazi": ["آتَى","آتَيَا","آتَوْا","آتَتْ","آتَتَا","آتَيْنَ",
          "آتَيْتَ","آتَيْتُمَا","آتَيْتُمْ","آتَيْتِ","آتَيْتُمَا","آتَيْتُنَّ",
          "آتَيْتُ","آتَيْنَا"],
 "mudari": ["يُؤْتِي","يُؤْتِيَانِ","يُؤْتُونَ","تُؤْتِي","تُؤْتِيَانِ","يُؤْتِينَ",
            "تُؤْتِي","تُؤْتِيَانِ","تُؤْتُونَ","تُؤْتِينَ","تُؤْتِيَانِ","تُؤْتِينَ",
            "أُوتِي","نُؤْتِي"],
 "amr": ["آتِ","آتِيَا","آتُوا","آتِي","آتِيَا","آتِينَ"],
 "mansub": "يُؤْتِيَ",
 "majzum": "يُؤْتِ",
 "majzum2": "تُؤْتِ",
 "majhulMazi": "أُوتِيَ",
 "majhulMudari": "يُؤْتَى",
 "note": ("مَهْمُوزُ الْفَاءِ نَاقِصٌ مِنَ الْإِفْعَالِ: آتَى يُؤْتِي إِيتَاءً — يَنْصِبُ مَفْعُولَيْنِ. "
          "أَلِفُ آتَى مَدَّةٌ: هَمْزَتَانِ فِي حَرْفٍ وَاحِدٍ (أَأْتَى)؛ وَفِي الْمُتَكَلِّمِ أُوتِي "
          "قُلِبَتِ الثَّانِيَةُ وَاوًا بَعْدَ الضَّمَّةِ كَأُومِنُ."),
}

# ---------------------------------------------------------------- write out
man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/26.json").write_text(
    json.dumps({"chapter": 26, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 26 for c in man["chapters"]):
    man["chapters"].append({"n": 26, "title": TITLE26})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.26.0"
ADD_EN = (" Chapter 26 carries the tasawwur adawat from the same file (lines ~2086-2110, sahifa 72-73): "
          "أَيُّ الْفَرِيقَيْنِ خَيْرٌ مَقَامًا, سَلْ بَنِي إِسْرَائِيلَ كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ, "
          "يَسْأَلُ أَيَّانَ يَوْمُ الْقِيَامَةِ and يَا مَرْيَمُ أَنَّى لَكِ هَذَا are received Qur'anic text "
          "quoted exactly — Maryam 19:73, al-Baqara 2:211, al-Qiyama 75:6 and Al 'Imran 3:37; the source's "
          "surah citations for the first two (Taha 73 and Taha 67) are corrected against the mushaf, a "
          "recorded divergence. كَيْفَ أَنْتَ, أَيْنَ زَيْدٌ and مَتَى جِئْتَ are the source's own worked "
          "examples verbatim, Ottoman plain-alif normalized to standard orthography — a recorded "
          "normalization.")
ADD_TR = (" Yirmi altıncı bâb, tasavvur edatlarını aynı dosyadan taşır (satır ~2086-2110, sahife 72-73): "
          "أَيُّ الْفَرِيقَيْنِ خَيْرٌ مَقَامًا, سَلْ بَنِي إِسْرَائِيلَ كَمْ آتَيْنَاهُمْ مِنْ آيَةٍ بَيِّنَةٍ, "
          "يَسْأَلُ أَيَّانَ يَوْمُ الْقِيَامَةِ ve يَا مَرْيَمُ أَنَّى لَكِ هَذَا aynen alınmış mervî Kur'ân "
          "metnidir — Meryem 19:73, Bakara 2:211, Kıyâme 75:6 ve Âl-i İmrân 3:37; kaynağın ilk ikisi için "
          "verdiği sûre atıfları (Tâhâ 73 ve Tâhâ 67) mushafa göre düzeltilmiştir — kayıtlı bir farklılıktır. "
          "كَيْفَ أَنْتَ, أَيْنَ زَيْدٌ ve مَتَى جِئْتَ kaynağın kendi işlenmiş örneklerinin aynen alınmışıdır; "
          "Osmanlı düz-elif imlâsı standart imlâya çevrilmiştir — kayıtlı bir normalizasyondur.")
if "2086-2110" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"]["aataa"] = AATAA
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch26:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD), "; morph + aataa")
