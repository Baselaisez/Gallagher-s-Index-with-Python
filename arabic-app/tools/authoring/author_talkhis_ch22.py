# -*- coding: utf-8 -*-
"""Author chapter 22 of talkhis-al-miftah — طُرُقُ الْقَصْرِ وَالْفَرْقُ بَيْنَهَا.

The qasr bab continues: the routes compared, and the ADDRESSEE doctrine
that decides between the two great ones —

  • نَفْيٌ + اسْتِثْنَاءٌ is for the hukm the addressee DENIES; إِنَّمَا for
    the hukm he knows and accepts.
  • …and each may DEMOTE: وَمَا مُحَمَّدٌ إِلَّا رَسُولٌ (Al Imran 3:144) sets
    the companions' magnifying of the Prophet's death at the RANK of
    denial (qasr ifrad); إِنْ أَنْتُمْ إِلَّا بَشَرٌ مِثْلُنَا (Ibrahim 14:10)
    answers the deniers with qasr qalb — and its إِنْ is the NEGATING in,
    a new closed-class face the engines learned this chapter.
  • إِنَّمَا نَحْنُ مُصْلِحُونَ (Baqara 2:11): the munafiqs claim their claim
    is obvious — the unknown demoted to the rank of the known — and the
    reply أَلَا إِنَّهُمْ هُمُ الْمُفْسِدُونَ (2:12) stacks its tawkid: the
    alerting أَلَا, إِنَّ, the damir al-fasl, the article.
  • إِنَّمَا هُوَ أَخُوكَ: innama's asl — said to one who KNOWS, to move him.

ATTRIBUTION: every Arabic word is VERBATIM received text quoted exactly —
Al Imran 3:144, Ibrahim 14:10, al-Baqara 2:11 and 2:12 (Qur'anic text),
and the books' own إِنَّمَا هُوَ أَخُوكَ frame — following
research/sources/talkhis-al-miftah-balagha.txt lines ~1880-1935 (sahifa
66-67), which cites each for the doctrine taught on it.

Grammar this chapter is chosen to teach:
  • note 124 `turuq-al-qasr` — the four routes, their four differences,
    the addressee doctrine with tanzil both ways, and the Sakkaki /
    Abd al-Qahir khilaf on لا-atf beside innama.
  • engine work: the NEGATING سukun-إن (illa-later discriminator; the
    shart frame stands down), أَلَا التنبيه before إِنَّ (one particle, not
    hamza+la), the five-nouns host under its pronoun (أَخُوكَ), and
    QasrEngine reading the إِنْ…إِلَّا frame.
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
S = []

TITLE22 = {"ar": "طُرُقُ الْقَصْرِ وَالْفَرْقُ بَيْنَهَا",
           "en": "The Routes of Qasr, Compared",
           "tr": "Kasr Yolları ve Aralarındaki Farklar"}

# ---------------------------------------------------------------- s1 — Al Imran 144
S.append({"id": "s1", "translation": {
 "en": "And Muhammad is only a messenger. (Al Imran 3:144 — nafy+istithna is for what the hearer DENIES; the companions' magnifying of his death was set at denial's rank, and the qasr is ifrad.)",
 "tr": "Muhammed ancak bir resuldür. (Âl-i İmrân 3:144 — nefiy+istisnâ, dinleyenin İNKÂR ettiği içindir; sahâbenin vefatını büyütmesi inkâr menzilesine indirildi ve kasr ifraddır.)"},
 "tokens": [
  tok("وَمَا","ma-nafiya","part",["turuq-al-qasr","anwa-ma"],
      "الْوَاوُ اسْتِئْنَافِيَّةٌ وَ«مَا» نَافِيَةٌ — وَ«إِلَّا» بَعْدَهَا عَلَامَةُ الْقَصْرِ.",
      "«and not» — the frame's negation, its illa standing two words on. The route chosen is the TELL: nafy+istithna is kept for a hukm the addressee denies or does not know.",
      "«ve değildir» — çatının nefyi; illâsı iki kelime ileride. Seçilen yol İPUCUdur: nefiy+istisnâ, muhatabın inkâr ettiği yahut bilmediği hüküm için saklanır.",
      segments=[seg("وَ","wa","part"), seg("مَا","ma-nafiya","part")]),
  tok("مُحَمَّدٌ","muhammad","propn",["turuq-al-qasr"],
      "مُبْتَدَأٌ مَرْفُوعٌ — وَهُوَ الْمَقْصُورُ.",
      "«Muhammad» ﷺ — the maqsur: the bearer, about to be confined to his messengerhood.",
      "«Muhammed» ﷺ — maksûr: sahibi; risâletine hasredilmek üzere."),
  tok("إِلَّا","illa","part",["turuq-al-qasr"],
      "أَدَاةُ الِاسْتِثْنَاءِ الْمُفَرَّغِ.",
      "«only» — the mufarragh exception.",
      "«ancak» — müferrağ istisnâ."),
  tok("رَسُولٌ","rasul","noun",["turuq-al-qasr","aqsam-al-qasr"],
      "خَبَرٌ مَرْفُوعٌ — الْمَقْصُورُ عَلَيْهِ: قَصْرُ إِفْرَادٍ بِتَنْزِيلِ الْمَعْلُومِ مَنْزِلَةَ الْمُنْكَرِ.",
      "«a messenger» — the maqsur alayh. Every companion KNEW he was a messenger — so why the denial-route? Because their magnifying of his death was SET AT the rank of denying it: he is a messenger ONLY, not exempt from passing as the messengers before him passed. Qasr IFRAD, cutting «messenger AND deathless» down to the first — and the route itself carries the rebuke.",
      "«bir resul» — maksûrun aleyh. Her sahâbî onun resul olduğunu BİLİYORDU — öyleyse inkâr yolu niçin? Çünkü vefatını büyütmeleri, onu İNKÂR menzilesine indirildi: o YALNIZ resuldür; kendinden önceki resuller gibi geçip gitmekten müstesnâ değildir. İFRAD kasrı — «resul VE ölümsüz»ü ilkine budar — ve azarı yolun kendisi taşır.",
      punct=".")],
 "jumal": [
  J("وَمَا مُحَمَّدٌ إِلَّا رَسُولٌ",
    "الْفَرْقُ الرَّابِعُ: النَّفْيُ وَالِاسْتِثْنَاءُ لِحُكْمٍ يُنْكِرُهُ الْمُخَاطَبُ — وَهُنَا نُزِّلَ الْمَعْلُومُ مَنْزِلَةَ الْمُنْكَرِ.",
    "DIFFERENCE 4 between the routes: nafy+istithna is for what the hearer denies. Here nobody denied — so the aya DEMOTES the known to denial's rank: grief so great it acted like denial is answered as denial. The tanzil doctrine, on the frame's own choice of route.",
    "Yollar arasındaki 4. FARK: nefiy+istisnâ, dinleyenin inkâr ettiği içindir. Burada kimse inkâr etmiyordu — âyet bilineni inkâr menzilesine İNDİRİR: inkâr gibi davranan büyük üzüntüye inkâr gibi cevap verilir. Tenzîl doktrini, çatının yol seçiminin bizzat üstünde."),
  J("وَمَا مُحَمَّدٌ إِلَّا رَسُولٌ",
    "وَهُوَ قَصْرُ إِفْرَادٍ: قُطِعَتْ شَرِكَةُ «رَسُولٌ وَبَاقٍ لَا يَمُوتُ».",
    "And it is IFRAD: the companions' state held two claims in partnership — messenger, and one who stays. The qasr prunes the second. Ch21's addressee taxonomy, now working on revelation's own text.",
    "Ve İFRADdır: sahâbenin hâli iki iddiayı ortak tutuyordu — resul, ve kalıcı. Kasr ikincisini budar. 21. bâbın muhatap taksimi, şimdi vahyin kendi metninde iş başında.")]})

# ---------------------------------------------------------------- s2 — Ibrahim 10
S.append({"id": "s2", "translation": {
 "en": "You are only human beings like us. (Ibrahim 14:10 — the deniers to the prophets: qasr QALB by the deniers' own creed; and the إِنْ here is the NEGATING in, working exactly as ما.)",
 "tr": "Siz ancak bizim gibi birer beşersiniz. (İbrâhîm 14:10 — inkârcılar peygamberlere: inkârcıların kendi inancına göre KALB kasrı; buradaki إِنْ, tıpkı mâ gibi çalışan NEFİY in'idir.)"},
 "tokens": [
  tok("إِنْ","in-nafiya","part",["turuq-al-qasr","in-shartiyya"],
      "نَافِيَةٌ بِمَعْنَى «مَا» — وَعَلَامَتُهَا «إِلَّا» بَعْدَهَا، وَلَا شَرْطَ هُنَا.",
      "«not» — and the nun wears sukun, which usually says CONDITIONAL. The tell is the إِلَّا standing later: إِنْ…إِلَّا is a negation frame exactly like مَا…إِلَّا, and the shart reading falls away — a conditional demands its verb, and this in opens on a pronoun and closes on an exception.",
      "«değil» — nûn sükûnlu; bu çoğu kez ŞART demektir. İpucu ilerideki إِلَّا'dır: إِنْ…إِلَّا, tıpkı مَا…إِلَّا gibi bir nefiy çatısıdır ve şart okuyuşu düşer — şart fiilini ister; bu in ise zamirle açılıp istisnâ ile kapanır."),
  tok("أَنْتُمْ","antum","pron",["turuq-al-qasr"],
      "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ — وَهُوَ الْمَقْصُورُ.",
      "«you» — the detached pronoun as mubtada, and the maqsur: the prophets themselves, about to be confined (in their deniers' mouths) to bare humanity.",
      "«siz» — munfasıl zamir, mübtedâ ve maksûr: peygamberlerin kendileri; (inkârcıların ağzında) çıplak beşerliğe hasredilmek üzere."),
  tok("إِلَّا","illa","part",["turuq-al-qasr"],
      "أَدَاةُ الِاسْتِثْنَاءِ الْمُفَرَّغِ.",
      "«only» — the exception closing the in-frame.",
      "«ancak» — in çatısını kapatan istisnâ."),
  tok("بَشَرٌ","bashar","noun",["turuq-al-qasr","aqsam-al-qasr"],
      "خَبَرٌ مَرْفُوعٌ — الْمَقْصُورُ عَلَيْهِ: قَصْرُ قَلْبٍ عَلَى اعْتِقَادِ الْكَافِرِينَ.",
      "«human beings» — the maqsur alayh, and by the deniers' own creed this is QALB: the prophets pressed their claim, the deniers held its opposite (a prophet cannot be a mere man), and the sentence flips — «you are ONLY men». The prophets' reply in the next aya (إِنْ نَحْنُ إِلَّا بَشَرٌ مِثْلُكُمْ) concedes the frame to silence the foe — مُجَارَاةُ الْخَصْمِ, not a denial of their own mission.",
      "«birer beşer» — maksûrun aleyh; ve inkârcıların kendi inancına göre bu KALBdir: peygamberler dâvâlarında ısrar etti, inkârcılar tersini tuttu (peygamber sıradan insan olamaz) ve cümle çevirir — «siz YALNIZ insansınız». Peygamberlerin sonraki âyetteki cevabı (إِنْ نَحْنُ إِلَّا بَشَرٌ مِثْلُكُمْ) hasmı susturmak için çatıyı teslim alır — مُجَارَاةُ الْخَصْمِ; kendi risâletlerinin inkârı değil."),
  tok("مِثْلُنَا","mithl","noun",["turuq-al-qasr","tarif-bil-idafa"],
      "صِفَةٌ لِـ«بَشَرٌ» مَرْفُوعَةٌ، وَ«نَا» مُضَافٌ إِلَيْهِ.",
      "«like us» — the sifa sealing the demotion: not merely human, but human OUR way — nothing above us.",
      "«bizim gibi» — indirmeyi mühürleyen sıfat: yalnız insan değil, BİZİM gibi insan — bizden üstün değil.",
      segments=[seg("مِثْلُ","mithl","noun"), seg("نَا","pron-1p","pron")],
      punct=".")],
 "jumal": [
  J("إِنْ أَنْتُمْ إِلَّا بَشَرٌ مِثْلُنَا",
    "إِنِ النَّافِيَةُ — أُخْتُ «مَا» فِي هَذَا الْبَابِ: نَفْيٌ وَاسْتِثْنَاءٌ بِأَدَاةٍ ثَالِثَةٍ.",
    "The NEGATING in — ma's sister in this bab: the same nafy+istithna route through a third particle. One spelling, three faces (conditional, negation, the light mukhaffafa) — and the illa is the surface observable that picks this one.",
    "NEFİY in'i — bu bâbda mâ'nın kız kardeşi: aynı nefiy+istisnâ yolu, üçüncü bir edatla. Tek imlâ, üç yüz (şart, nefiy, muhaffefe) — ve bunu seçen yüzey işareti illâdır."),
  J("إِنْ أَنْتُمْ إِلَّا بَشَرٌ مِثْلُنَا",
    "قَصْرُ قَلْبٍ عَلَى مُعْتَقَدِ الْمُخَاطَبِ — وَجَوَابُ الْأَنْبِيَاءِ مِنْ بَابِ مُجَارَاةِ الْخَصْمِ.",
    "QALB against the prophets' pressed claim — and when the prophets answer in the SAME frame, it is not concession of prophethood but مُجَارَاةُ الْخَصْمِ: adopting the foe's idiom where silencing him is the aim. The books read the pair together; so do we.",
    "Peygamberlerin ısrarlı dâvâsına karşı KALB — ve peygamberler AYNI çatıyla cevap verince bu, nübüvvetten vazgeçiş değil مُجَارَاةُ الْخَصْمِ'dır: hasmı susturmak istenen yerde onun dilini kuşanmak. Kitaplar çifti birlikte okur; biz de öyle.")]})

# ---------------------------------------------------------------- s3 — Baqara 11
S.append({"id": "s3", "translation": {
 "en": "We are only reformers. (al-Baqara 2:11 — the munafiqs choose إِنَّمَا: they CLAIM their goodness is obvious, demoting the unknown to the rank of the known.)",
 "tr": "Biz ancak ıslah edicileriz. (Bakara 2:11 — münafıklar إِنَّمَا'yı seçer: iyiliklerinin apaçık olduğunu İDDİA ederler; meçhulü malum menzilesine indirirler.)"},
 "tokens": [
  tok("إِنَّمَا","innama","part",["turuq-al-qasr","innama-kaffa"],
      "كَافَّةٌ وَمَكْفُوفَةٌ — طَرِيقُ قَصْرٍ لِحُكْمٍ يَدَّعِي الْمُتَكَلِّمُ ظُهُورَهُ.",
      "«only» — inna with the restraining ma: the second great route, and its asl is the OPPOSITE of the illa-frame's — innama is for a hukm the hearer knows and does not deny. The munafiqs know their claim is NOT known; they use innama anyway, CLAIMING obviousness — the unknown demoted to the known's rank. The route itself is their bluff.",
      "«ancak» — kâffe mâ'lı inne: ikinci büyük yol; ve aslı, illâ çatısının TERSİdir — innemâ, dinleyenin bilip inkâr etmediği hüküm içindir. Münafıklar iddialarının bilinMEdiğini bilirler; yine de innemâ kullanır, apaçıklık İDDİA ederler — meçhul, malumun menzilesine indirilmiş. Yolun kendisi onların blöfüdür."),
  tok("نَحْنُ","nahnu","pron",["turuq-al-qasr"],
      "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.",
      "«we» — the detached pronoun as mubtada.",
      "«biz» — munfasıl zamir, mübtedâ."),
  tok("مُصْلِحُونَ","muslih","noun",["turuq-al-qasr","ism-fail","jam-mudhakkar-salim"],
      "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — وَالْقَصْرُ ادِّعَائِيٌّ.",
      "«reformers» — Form IV's ism fail in the sound plural, raf' by its waw: مُصْلِح, one who sets things right. The qasr says «reformers and nothing else» — and the next aya will flip every word of it.",
      "«ıslah ediciler» — IV. bâbın ism-i fâili, cem'-i sâlim; ref'i vâvladır: مُصْلِح, düzelten. Kasr «ıslahçıyız, başka bir şey değil» der — ve sonraki âyet her kelimesini çevirecek.",
      punct=".")],
 "jumal": [
  J("إِنَّمَا نَحْنُ مُصْلِحُونَ",
    "أَصْلُ «إِنَّمَا»: حُكْمٌ يَعْلَمُهُ الْمُخَاطَبُ وَلَا يُنْكِرُهُ — وَهُنَا نُزِّلَ الْمَجْهُولُ مَنْزِلَةَ الْمَعْلُومِ ادِّعَاءً.",
    "Innama's asl: the known, undenied hukm (إِنَّمَا هُوَ أَخُوكَ — said to one who knows, to move him to mercy). The munafiqs invert it by CLAIM: they speak as if their virtue were common knowledge. The tanzil doctrine again — mirror-image of s1's.",
    "İnnemâ'nın aslı: bilinen, inkâr edilmeyen hüküm (إِنَّمَا هُوَ أَخُوكَ — bilene, merhamete sevk için söylenir). Münafıklar bunu İDDİA ile tersine çevirir: faziletleri herkesçe biliniyormuş gibi konuşurlar. Yine tenzîl doktrini — s1'inkinin ayna görüntüsü."),
  J("إِنَّمَا نَحْنُ مُصْلِحُونَ",
    "وَمِنْ فُرُوقِ الطُّرُقِ: «لَا» الْعَاطِفَةُ تُجَامِعُ إِنَّمَا وَالتَّقْدِيمَ، لَا النَّفْيَ وَالِاسْتِثْنَاءَ.",
    "And difference 3 between the routes: the atf-la may follow innama and the fronting (إِنَّمَا أَنَا تَمِيمِيٌّ لَا قَيْسِيٌّ) but never the illa-frame — مَا زَيْدٌ إِلَّا قَائِمٌ لَا قَاعِدٌ is refused, for the atf-la demands a sentence not already negated. Sakkaki adds a condition, Abd al-Qahir softens it to «not beautiful» — and the books judge his view nearer the truth.",
    "Ve yolların 3. farkı: atıf lâ'sı innemâ ve takdimle birleşir (إِنَّمَا أَنَا تَمِيمِيٌّ لَا قَيْسِيٌّ), illâ çatısıyla asla — مَا زَيْدٌ إِلَّا قَائِمٌ لَا قَاعِدٌ reddedilir; çünkü atıf lâ'sı, önceden nefyedilmemiş bir cümle ister. Sekkâkî bir şart ekler; Abdülkāhir «şart değil, güzel olmaz»a yumuşatır — ve kitaplar onun görüşünü hakikate daha yakın bulur.")]})

# ---------------------------------------------------------------- s4 — Baqara 12
S.append({"id": "s4", "translation": {
 "en": "Truly, it is they who are the corrupters. (al-Baqara 2:12 — the reply stacks its emphases: the alerting أَلَا, then إِنَّ, then the damir al-fasl, then the article — because a claimed-obvious lie needs a fortified refutation.)",
 "tr": "Gözünü aç: onlar bozguncuların ta kendileridir. (Bakara 2:12 — cevap te'kidlerini yığar: tenbih أَلَا'sı, sonra إِنَّ, sonra fasıl zamiri, sonra harf-i tarif — çünkü apaçıklık iddia eden yalana tahkim edilmiş bir reddiye gerekir.)"},
 "tokens": [
  tok("أَلَا","ala-tanbih","part",["turuq-al-qasr","huruf-tanbih"],
      "أَدَاةُ تَنْبِيهٍ وَاسْتِفْتَاحٍ — تَسْبِقُ «إِنَّ» وَلَا تَعْمَلُ شَيْئًا.",
      "«truly, mark it» — the ALERTING ala, one particle: it precedes إِنَّ, wakes the hearer, and governs nothing. Not the question-hamza plus a negation — the inna-table lists it beside إِنَّ itself, and here it is the first stone of the reply's fortification.",
      "«gözünü aç» — TENBİH أَلَا'sı, tek edat: إِنَّ'den önce gelir, dinleyeni uyandırır, hiçbir şeyi amel etmez. Soru hemzesi + nefiy değil — inne tablosu onu bizzat إِنَّ'nin yanında sayar; burada reddiyenin tahkimatının ilk taşıdır."),
  tok("إِنَّهُمْ","inna","part",["turuq-al-qasr","inna-am-anna"],
      "«إِنَّ» لِلتَّوْكِيدِ وَ«هُمْ» اسْمُهَا فِي مَحَلِّ نَصْبٍ.",
      "«truly they» — inna with its clinging ism: the second emphasis in the stack.",
      "«muhakkak onlar» — inne ve yapışık ismi: yığındaki ikinci te'kid.",
      segments=[seg("إِنَّ","inna","part"), seg("هُمْ","pron-3mp","pron")]),
  tok("هُمُ","hum","pron",["turuq-al-qasr","damir-fasl"],
      "ضَمِيرُ فَصْلٍ لَا مَحَلَّ لَهُ — يُفِيدُ التَّوْكِيدَ وَالْقَصْرَ.",
      "«they and none other» — the DAMIR AL-FASL, standing between ism and khabar with no seat of its own: it welds the two, excludes a third, and adds its own shade of qasr. Third emphasis. (Its wasl-damma before the article: هُمُ الْـ.)",
      "«onların ta kendileri» — FASIL ZAMİRİ; isimle haber arasında kendi mahalli olmadan durur: ikisini kaynatır, üçüncüyü dışlar, kendi kasr gölgesini katar. Üçüncü te'kid. (Harf-i tariften önce vasıl dammesi: هُمُ الْـ.)"),
  tok("الْمُفْسِدُونَ","mufsid","noun",["turuq-al-qasr","ism-fail","jam-mudhakkar-salim","anwa-al-lam-al-tarif"],
      "خَبَرُ «إِنَّ» مَرْفُوعٌ بِالْوَاوِ — مُعَرَّفٌ بِلَامِ الْجِنْسِ: رَابِعُ التَّوْكِيدَاتِ.",
      "«THE corrupters» — Form IV's ism fail again (مُفْسِد, the exact inverse of s3's مُصْلِح), and the article is the FOURTH emphasis: the jins-lam confines corrupting to them, ch18's qasr device closing the ring. Four fortifications on one sentence — measured against the size of the lie they answer.",
      "«BOZGUNCULAR» — yine IV. bâbın ism-i fâili (مُفْسِد; s3'ün مُصْلِح'inin tam tersi) ve harf-i tarif DÖRDÜNCÜ te'kiddir: cins lâmı bozgunculuğu onlara hasreder — 18. bâbın kasr aygıtı halkayı kapatır. Tek cümlede dört tahkimat — cevapladığı yalanın boyuna göre ölçülmüş.",
      punct=".")],
 "jumal": [
  J("أَلَا إِنَّهُمْ هُمُ الْمُفْسِدُونَ",
    "رَدٌّ مُؤَكَّدٌ بِأَرْبَعٍ: أَلَا، وَإِنَّ، وَضَمِيرُ الْفَصْلِ، وَلَامُ الْجِنْسِ.",
    "A refutation fortified four ways — the alerting ala, inna, the damir al-fasl, the jins-lam — because the claim it answers was dressed as the obvious. The strength of a denial is calibrated to the hearer's entrenchment: the inkari maqam doctrine, working at full stretch.",
    "Dört yolla tahkim edilmiş reddiye — tenbih أَلَا'sı, إِنَّ, fasıl zamiri, cins lâmı — çünkü cevapladığı iddia apaçıklık kıyafeti giymişti. İnkârın gücü, dinleyenin direncine göre ayarlanır: inkârî makam doktrini, son haddinde iş başında."),
  J("أَلَا إِنَّهُمْ هُمُ الْمُفْسِدُونَ",
    "وَضَمِيرُ الْفَصْلِ نَفْسُهُ طَرِيقُ قَصْرٍ خَامِسٌ عِنْدَ قَوْمٍ.",
    "And the damir al-fasl is itself counted a fifth qasr-route by some — it welds subject to predicate and shuts the door on any third party. The routes' list, like most of the books' lists, has a disputed tail; we teach the four and name the fifth.",
    "Ve fasıl zamiri, kimilerince beşinci bir kasr yolu sayılır — özneyi yükleme kaynatır, üçüncü şahsa kapıyı kapatır. Yolların listesinin, kitapların çoğu listesi gibi, ihtilaflı bir kuyruğu vardır; biz dördü öğretir, beşinciyi adlandırırız.")]})

# ---------------------------------------------------------------- s5 — innama's asl
S.append({"id": "s5", "translation": {
 "en": "He is only your brother. (Innama's home ground: said to one who KNOWS and does not deny — to move him to act on what he knows.)",
 "tr": "O ancak senin kardeşindir. (İnnemâ'nın kendi zemini: BİLEN ve inkâr etmeyene söylenir — bildiğinin gereğini yapmaya sevk için.)"},
 "tokens": [
  tok("إِنَّمَا","innama","part",["turuq-al-qasr","innama-kaffa"],
      "كَافَّةٌ وَمَكْفُوفَةٌ — عَلَى أَصْلِهَا هُنَا: لِحُكْمٍ مَعْلُومٍ غَيْرِ مُنْكَرٍ.",
      "«only» — innama on its own home ground at last: the hearer knows this man is his brother and denies nothing. The qasr is not teaching him a fact; it is pressing the fact he owns into his conduct — be merciful to him.",
      "«ancak» — innemâ nihayet kendi zemininde: dinleyen bu adamın kardeşi olduğunu bilir ve hiçbir şeyi inkâr etmez. Kasr ona bir vakıa öğretmiyor; sahibi olduğu vakıayı davranışına bastırıyor — ona merhametli ol."),
  tok("هُوَ","huwa","pron",["turuq-al-qasr"],
      "ضَمِيرٌ مُنْفَصِلٌ مُبْتَدَأٌ.",
      "«he» — the detached pronoun as mubtada.",
      "«o» — munfasıl zamir, mübtedâ."),
  tok("أَخُوكَ","akh","noun",["turuq-al-qasr","five-nouns"],
      "خَبَرٌ مَرْفُوعٌ بِالْوَاوِ — مِنَ الْأَسْمَاءِ الْخَمْسَةِ، وَالْكَافُ مُضَافٌ إِلَيْهِ.",
      "«your brother» — one of the FIVE NOUNS, its raf' shown by the waw itself, the kaf its required mudaf ilayh. The sentence every reader can parse by now — and the bab's quiet close: which route you choose tells the hearer what you think he believes.",
      "«senin kardeşin» — BEŞ İSİMden; ref'i bizzat vâvla görünür, kâf şart koşulan muzâfun ileyhidir. Artık her okurun çözebileceği cümle — ve bâbın sessiz kapanışı: seçtiğin yol, dinleyene neye inandığını düşündüğünü söyler.",
      punct=".")],
 "jumal": [
  J("إِنَّمَا هُوَ أَخُوكَ",
    "أَصْلُ إِنَّمَا: تَذْكِيرُ الْعَالِمِ لِيَعْمَلَ بِعِلْمِهِ — لَا إِعْلَامُ الْجَاهِلِ.",
    "Innama's asl in one line: reminding the knower so he acts on his knowledge — not informing the ignorant. Set beside s1 the symmetry completes: the illa-frame for the denier (real or demoted), innama for the acknowledger (real or claimed).",
    "İnnemâ'nın aslı tek satırda: bilene hatırlatmak ki bildiğiyle amel etsin — bilmeyene bildirmek değil. s1'in yanına koy; bakışım tamamlanır: illâ çatısı inkârcıya (gerçek yahut indirilmiş), innemâ ikrarcıya (gerçek yahut iddia edilmiş)."),
  J("إِنَّمَا هُوَ أَخُوكَ",
    "وَمَزِيَّةُ إِنَّمَا عَلَى الْعَطْفِ: يُفْهَمُ مِنْهَا الْحُكْمَانِ مَعًا.",
    "And innama's edge over the atf-route: both rulings — the affirmation and the exclusion — are heard AT ONCE in one particle, where the atf spells them out in two clauses. Its finest use, the books add, is ta'rid: saying one thing to intend another — the door the next chapters open.",
    "Ve innemânın atıf yoluna üstünlüğü: iki hüküm — isbat ve dışlama — tek edatta AYNI ANDA işitilir; atıf ise ikisini iki cümlede açar. En güzel kullanımı, diye ekler kitaplar, ta'rizdir: bir şeyi söyleyip başkasını murad etmek — sonraki bâbların açacağı kapı.")]})

# ---------------------------------------------------------------- glossary
GLOSS_ADD = {
 # copies — a lex key is GLOBAL: entries copied verbatim from their home package
 "rasul":  copy_gloss("aqaid-ahl-al-sunna", "rasul"),
 "bashar": copy_gloss("aqaid-ahl-al-sunna", "bashar"),
 "innama": copy_gloss("kitab-al-sulh", "innama"),
 # NEW this chapter
 "in-nafiya": g("إِنْ (النَّافِيَة)", None, "part",
                "the negating in — «not», working like ما; its tell is the إِلَّا after it",
                "nefiy in'i — «değil», mâ gibi çalışır; ipucu ardındaki إِلَّا'dır", 5),
 "antum":  g("أَنْتُمْ", None, "pron", "you (masc. plural, detached)", "siz (eril çoğul, munfasıl)", 2),
 "ala-tanbih": g("أَلَا (التَّنْبِيه)", None, "part",
                 "the alerting ala — precedes إِنَّ, wakes the hearer, governs nothing",
                 "tenbih أَلَا'sı — إِنَّ'den önce gelir, dinleyeni uyandırır, amel etmez", 5),
 "muslih": g("مُصْلِح", "ص ل ح", "noun", "reformer, one who sets right (ism fail of أَصْلَحَ)",
             "ıslah edici (أَصْلَحَ'nın ism-i fâili)", 3, plural="مُصْلِحُونَ", form="IV"),
 "mufsid": g("مُفْسِد", "ف س د", "noun", "corrupter (ism fail of أَفْسَدَ)",
             "bozguncu, ifsad edici (أَفْسَدَ'nın ism-i fâili)", 3, plural="مُفْسِدُونَ", form="IV"),
}

man = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
(PKG / "chapters/22.json").write_text(
    json.dumps({"chapter": 22, "sentences": S}, ensure_ascii=False, indent=1), encoding="utf-8")
if not any(c["n"] == 22 for c in man["chapters"]):
    man["chapters"].append({"n": 22, "title": TITLE22})
man["chapters"].sort(key=lambda c: c["n"])
man["version"] = "0.22.0"
ADD_EN = (" Chapter 22 compares the qasr routes from the same file (lines ~1880-1935, sahifa 66-67): "
          "Al Imran 3:144, Ibrahim 14:10, al-Baqara 2:11 and 2:12 — received Qur'anic text quoted "
          "exactly, each cited by the source for the doctrine taught on it — and the books' own frame "
          "إِنَّمَا هُوَ أَخُوكَ. The Farazdaq bayt and the تَمِيمِيٌّ أَنَا frames are carried in the note "
          "and jumal rows, not as tokens.")
ADD_TR = (" Yirmi ikinci bâb, kasr yollarını aynı dosyadan karşılaştırır (satır ~1880-1935, sahife "
          "66-67): Âl-i İmrân 3:144, İbrâhîm 14:10, Bakara 2:11 ve 2:12 — aynen alınmış mervî Kur'ân "
          "metni; her biri üzerinde öğretilen doktrin için kaynağın kendisince zikredilir — ve kitapların "
          "kendi kalıbı إِنَّمَا هُوَ أَخُوكَ. Ferezdak beyti ile تَمِيمِيٌّ أَنَا kalıpları token olarak değil, "
          "not ve cümle satırlarında taşınır.")
if "1880-1935" not in man["attribution"]["en"]:
    man["attribution"]["en"] += ADD_EN
    man["attribution"]["tr"] += ADD_TR
(PKG / "manifest.json").write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
gl = json.loads((PKG / "glossary.json").read_text(encoding="utf-8")); gl["entries"].update(GLOSS_ADD)
(PKG / "glossary.json").write_text(json.dumps(gl, ensure_ascii=False, indent=1), encoding="utf-8")
print("talkhis ch22:", len(S), "sentences,", sum(len(x["tokens"]) for x in S), "tokens; gloss +", len(GLOSS_ADD))
