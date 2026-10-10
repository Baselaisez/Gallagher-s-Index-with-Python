# -*- coding: utf-8 -*-
"""Talkhis al-Miftah — chapter 70: RADD AL-ʿAJUZ ʿALA AL-SADR — in prose (the two words repeated, in jinas, or attached to the jinas:
one at the head of the fiqra, the other at its close) and in verse (one word closes the bayt, the other stands at the head of the first
misraʿ, in its middle, at its end, or at the head of the second). Source lines ~4476-4510 (sahifa 154-156).

  RESTORED (the source carries the step only in Turkish): s1 and s6 (the two definitions), and the SIX BAYTS s7-s12: the source gives
  each bayt in Turkish paraphrase with only the repeated words in Arabic (سَرِيعٌ، عَرَارِ، مُغْرَمًا، قَلِيل، دَعَانِي، بَوَاتِرُ/بُتْرٌ); the
  Arabic here is the received text the Talkhis cites, marked «Restored» sentence by sentence. The prose examples (s2 33:37, s3 the
  saying, s4 71:10, s5 26:168) are the source's printed Arabic.

  python3 tools/authoring/author_talkhis_ch70.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
from talkhis_common import *
import talkhis_common as _tc
import sarf_gen as _sg
if os.environ.get("DRY_PKG"):
    _tc.PKG = pathlib.Path(os.environ["DRY_PKG"]); _tc.GR = pathlib.Path(os.environ["DRY_GR"])
PKG = _tc.PKG

R = "radd-al-ajuz"
TITLE = {"ar": "رَدُّ الْعَجُزِ عَلَى الصَّدْرِ — فِي النَّثْرِ وَفِي النَّظْمِ", "en": "Radd al-ʿajuz ʿala al-sadr — in prose and in verse", "tr": "Reddü'l-acüz ale's-sadr — nesirde ve nazımda"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
RB_EN = " (Restored: the source gives the bayt only in Turkish with the repeated words in Arabic; this is the received text the Talkhis cites.)"
RB_TR = " (Geri yazım: kaynak beyti yalnız Türkçe, tekrarlanan kelimeleri Arapça verir; bu, Telhîs'in andığı alınan metindir.)"

def ix(sen, word, nth=1):
    n = 0
    for i, t in enumerate(sen["tokens"]):
        if t["surface"]["full"] == word:
            n += 1
            if n == nth: return i
    raise KeyError(word)
def fi(tag): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».")
def aw_x(tag, word, lex, ar, en, tr, segs=None):
    aw = "أَوِ" if word.startswith("ال") else "أَوْ"   # iltiqa' al-sakinayn: the waw takes a kasra before the article's sakin lam
    return [tok(aw, "aw", "conj", [tag, "atf-nasaq"], "حَرْفُ عَطْفٍ" + ("، وَكُسِرَتِ الْوَاوُ لِالْتِقَاءِ السَّاكِنَيْنِ." if aw == "أَوِ" else "."), "«or»." + (" The waw takes a kasra before the article's sakin lam (two sakins meeting)." if aw == "أَوِ" else ""), "«ya»." + (" İki sâkin karşılaştığı için vav kesre alır." if aw == "أَوِ" else "")), tok(word, lex, "noun", [tag, "atf-nasaq", "idafa-definiteness"], ar, en, tr, segments=segs)]

# ----------- s1 — the definition, in prose (RESTORED)
S.append({"id": "s1", "translation": {
 "en": "RADD AL-ʿAJUZ ʿALA AL-SADR — «bringing the close back upon the head» — is, in PROSE, that one of two words REPEATED, or in JINAS, or ATTACHED to it, be set at the HEAD of the fiqra and the other at its CLOSE." + R_EN,
 "tr": "REDDÜ'L-ACÜZ ALE'S-SADR — «sonu başa döndürmek» — NESİRDE, TEKRARLANAN yahut CİNASLI yahut cinâsa İLHAK edilmiş iki kelimeden birinin fıkranın BAŞINA, öbürünün SONUNA konmasıdır." + R_TR},
 "tokens": [
  tok("رَدُّ","radd","noun",[R, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ رَدَّ.", "«the bringing back of» — the mubtada, annexed.", "«döndürme» — mübtedâ, muzâf."),
  tok("الْعَجُزِ","ajuz","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْعَجُزُ: آخِرُ الْبَيْتِ أَوِ الْفِقْرَةِ.", "«the close» — the last word of the line.", "«acüz» — satırın son kelimesi."),
  tok("عَلَى","ala","prep",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«upon».", "«üzerine»."),
  tok("الصَّدْرِ","sadr","noun",[R, "huruf-jarr"], "مَجْرُورٌ — الصَّدْرُ: أَوَّلُ الْبَيْتِ أَوِ الْفِقْرَةِ.", "«the head» — the first word of the line.", "«sadr» — satırın ilk kelimesi.", punct=":"),
  tok("هُوَ","huwa","pron",[R, "mubtada-khabar"], "مُبْتَدَأٌ ثَانٍ — أَوْ ضَمِيرُ فَصْلٍ.", "«it is» — a second mubtada (or the pronoun of separation).", "«o» — ikinci mübtedâ (yahut fasıl zamiri)."),
  fi(R),
  tok("النَّثْرِ","nathr","noun",[R, "huruf-jarr"], "مَجْرُورٌ — النَّثْرُ: الْكَلَامُ غَيْرُ الْمَوْزُونِ.", "«prose» — unmetred speech.", "«nesir» — vezinsiz söz."),
  tok("أَنْ","an-masdariyya","part",[R, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ خَبَرٌ.", "«that» — the clause is the khabar.", "«-ması» — cümle haber."),
  tok("يُجْعَلَ","jaala","verb",[R, "an-masdariyya", "naib-al-fail"], "فِعْلٌ مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَنْصُوبٌ بِأَنْ.", "«be set» — the passive, mansub by an.", "«konsun» — meçhul; en ile mansûb."),
  tok("أَحَدُ","ahad","noun",[R, "naib-al-fail", "idafa-definiteness"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ، مُضَافٌ.", "«one of» — the deputy, annexed.", "«biri» — nâib, muzâf."),
  tok("اللَّفْظَيْنِ","lafz","noun",[R, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«the two words».", "«iki lafzın»."),
  tok("الْمُكَرَّرَيْنِ","mukarrar","noun",[R, "al-muthanna", "ism-maful"], "نَعْتٌ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«repeated» — the na't, a dual.", "«tekrarlanan» — na't, tesniye."),
 ] + aw_x(R, "الْمُتَجَانِسَيْنِ", "mutajanis", "مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى: اللَّذَيْنِ بَيْنَهُمَا جِنَاسٌ.", "«or in jinas» — joined.", "«yahut cinaslı» — atıf.")
   + aw_x(R, "الْمُلْحَقَيْنِ", "mulhaq", "مَعْطُوفٌ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى: بِالِاشْتِقَاقِ أَوْ شِبْهِهِ.", "«or attached» — by derivation or its look-alike.", "«yahut ilhak edilmiş» — iştikak yahut benzeriyle.") + [
  tok("بِهِمَا","bi","prep",[R, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — أَيْ بِالْمُتَجَانِسَيْنِ.", "«to them» — to the two in jinas.", "«o ikisine» — cinaslı ikisine.",
      segments=[seg("بِ","bi","prep"), seg("هِمَا","pron-3d","pron")]),
  fi(R),
  tok("أَوَّلِ","awwal","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — مُتَعَلِّقٌ بِيُجْعَلَ.", "«the head of».", "«başında»."),
  tok("الْفِقْرَةِ","fiqra","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْفِقْرَةُ: الْجُمْلَةُ مِنَ النَّثْرِ.", "«the fiqra» — the prose clause.", "«fıkra» — nesir cümlesi."),
  tok("وَالْآخَرُ","akhar","noun",[R, "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْآخَرُ مُبْتَدَأٌ.", "«and the other» — the mubtada.", "«ve öbürü» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْآخَرُ","akhar","noun")]),
  tok("فِي","fi","prep",[R, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«at» — the khabar.", "«-de» — haber."),
  tok("آخِرِهَا","akhir","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its close».", "«sonunda».",
      segments=[seg("آخِرِ","akhir","noun"), seg("هَا","pron-3fs","pron")]),
 ]})

# ----------- s2 — 33:37: you fear the people
S.append({"id": "s2", "translation": {
 "en": "«And you FEAR (takhsha) the people, while Allah has more right that you should FEAR HIM (takhshahu)» (33:37) — the same verb opens and closes: the repeated word.",
 "tr": "«İnsanlardan KORKUYORSUN (tahşâ), hâlbuki Allah, kendisinden KORKMANA (tahşâhu) daha lâyıktır» (Ahzâb 37) — aynı fiil açar ve kapar: tekrarlanan kelime."},
 "tokens": [
  tok("وَتَخْشَى","khashiya","verb",[R, "naqis-verbs", "mudari-marfu"], "الْوَاوُ عَاطِفَةٌ، وَتَخْشَى فِعْلٌ مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — نَاقِصٌ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«and you fear» — the naqis verb; its doer concealed.", "«ve korkuyorsun» — nâkıs fiil; fâili gizli.",
      segments=[seg("وَ","wa","conj"), seg("تَخْشَى","khashiya","verb")]),
  tok("النَّاسَ","nas","noun",[R, "maful-bihi"], "مَفْعُولٌ بِهِ مَنْصُوبٌ.", "«the people» — the object.", "«insanlardan» — mef'ul."),
  tok("وَاللهُ","allah","noun",[R, "mubtada-khabar", "hal"], "الْوَاوُ لِلْحَالِ، وَاللهُ مُبْتَدَأٌ مَرْفُوعٌ.", "«while Allah» — the mubtada of a hal clause.", "«hâlbuki Allah» — hâl cümlesinin mübtedâsı.",
      segments=[seg("وَ","wa","conj"), seg("اللهُ","allah","noun")]),
  tok("أَحَقُّ","ahaqq","noun",[R, "mubtada-khabar", "ism-tafdil"], "خَبَرٌ مَرْفُوعٌ — اسْمُ تَفْضِيلٍ.", "«has more right» — the khabar, an afʿal of comparison.", "«daha lâyık» — haber, ism-i tafdil."),
  tok("أَنْ","an-masdariyya","part",[R, "an-masdariyya"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مَجْرُورٌ بِبَاءٍ مُقَدَّرَةٍ: أَحَقُّ بِأَنْ تَخْشَاهُ.", "«that» — the clause hangs on the tafdil (with a dropped ba).", "«-mana» — cümle tafdile bağlı (bâ gizli)."),
  tok("تَخْشَاهُ","khashiya","verb",[R, "an-masdariyya", "naqis-verbs", "maful-bihi"], "فِعْلٌ مُضَارِعٌ مَنْصُوبٌ بِفَتْحَةٍ مُقَدَّرَةٍ، وَالْهَاءُ مَفْعُولٌ بِهِ.", "«you should fear Him» — mansub; the ha its object.", "«O'ndan korkman» — mansûb; hâ mef'ulü.",
      segments=[seg("تَخْشَى","khashiya","verb"), seg("هُ","pron-3ms","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "tikrar", "pair": [ix(S[-1], "وَتَخْشَى"), ix(S[-1], "تَخْشَاهُ")]}]

# ----------- s3 — the one who asks the base man
S.append({"id": "s3", "translation": {
 "en": "«The one who ASKS (sa'il) the base man turns back with his tear FLOWING (sa'il)» — the two in jinas open and close the fiqra.",
 "tr": "«Alçaktan İSTEYEN (sâil) gözyaşı AKARAK (sâil) döner» — cinaslı ikisi fıkrayı açar ve kapar."},
 "tokens": [
  tok("سَائِلُ","sail","noun",[R, "mubtada-khabar", "idafa-definiteness", "ism-fail"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — اسْمُ فَاعِلٍ مِنْ سَأَلَ.", "«the one who asks» — the mubtada; from sa'ala.", "«isteyen» — mübtedâ; seele'den."),
  tok("اللَّئِيمِ","laim","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the base man».", "«alçağın»."),
  tok("يَرْجِعُ","rajaa","verb",[R, "mubtada-khabar", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرٌ.", "«turns back» — the khabar.", "«döner» — haber."),
  tok("وَدَمْعُهُ","dam-tear","noun",[R, "hal", "mubtada-khabar", "idafa-definiteness"], "الْوَاوُ لِلْحَالِ، وَدَمْعُهُ مُبْتَدَأٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«with his tear» — the mubtada of a hal clause.", "«gözyaşı» — hâl cümlesinin mübtedâsı.",
      segments=[seg("وَ","wa","conj"), seg("دَمْعُ","dam-tear","noun"), seg("هُ","pron-3ms","pron")]),
  tok("سَائِلٌ","sail-flowing","noun",[R, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ — اسْمُ فَاعِلٍ مِنْ سَالَ: جَرَى.", "«flowing» — the khabar; from sala «to flow».", "«akan» — haber; sâle «akmak»tan."),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "jinas", "pair": [ix(S[-1], "سَائِلُ"), ix(S[-1], "سَائِلٌ")]},
                 {"kind": "jinas", "sub": "tamm", "kind2": "mumathil", "pair": [ix(S[-1], "سَائِلُ"), ix(S[-1], "سَائِلٌ")]}]

# ----------- s4 — 71:10: ask forgiveness … Forgiving
S.append({"id": "s4", "translation": {
 "en": "«ASK FORGIVENESS (istaghfiru) of your Lord; He is ever FORGIVING (ghaffar)» (71:10) — one root, غ ف ر: the two attached to the jinas open and close.",
 "tr": "«Rabbinizden MAĞFİRET DİLEYİN (istağfirû); O çok BAĞIŞLAYICIDIR (gaffâr)» (Nûh 10) — tek kök, غ ف ر: cinâsa ilhak edilen ikisi açar ve kapar."},
 "tokens": [
  tok("اسْتَغْفِرُوا","istaghfara","verb",[R, "fail"], "فِعْلُ أَمْرٍ مَبْنِيٌّ عَلَى حَذْفِ النُّونِ، وَالْوَاوُ فَاعِلٌ.", "«ask forgiveness» — the plural command; the waw is the doer.", "«mağfiret dileyin» — çoğul emir; vâv fâil."),
  tok("رَبَّكُمْ","rabb","noun",[R, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ.", "«your Lord» — the object.", "«Rabbinizden» — mef'ul.",
      segments=[seg("رَبَّ","rabb","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("إِنَّهُ","inna","part",[R, "inna-wa-akhawatuha"], "إِنَّ حَرْفُ تَوْكِيدٍ نَاسِخٌ، وَالْهَاءُ اسْمُهَا — وَالْجُمْلَةُ تَعْلِيلٌ.", "«He is» — inna with its ism; the clause gives the reason.", "«çünkü O» — inne ve ismi; cümle talil.",
      segments=[seg("إِنَّ","inna","part"), seg("هُ","pron-3ms","pron")]),
  tok("كَانَ","kana","verb",[R, "kana-wa-akhawatuha", "inna-wa-akhawatuha"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ — وَالْجُمْلَةُ خَبَرُ إِنَّ.", "«was ever» — kana; the clause is inna's khabar.", "«-dır» — kâne; cümle innenin haberi."),
  tok("غَفَّارًا","ghaffar","noun",[R, "kana-wa-akhawatuha"], "خَبَرُ كَانَ مَنْصُوبٌ — صِيغَةُ مُبَالَغَةٍ عَلَى فَعَّالٍ.", "«Forgiving» — kana's khabar; the intensive faʿʿal.", "«çok bağışlayıcı» — kânenin haberi; fa'âl vezninde mübalağa."),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "mulhaq", "pair": [ix(S[-1], "اسْتَغْفِرُوا"), ix(S[-1], "غَفَّارًا")]},
                 {"kind": "jinas", "sub": "ishtiqaq", "pair": [ix(S[-1], "اسْتَغْفِرُوا"), ix(S[-1], "غَفَّارًا")]}]

# ----------- s5 — 26:168 once more: the look-alike attached
S.append({"id": "s5", "translation": {
 "en": "«He SAID (qala): I am, of your deed, among those who DETEST (al-qalin)» (26:168) — قَالَ opens, الْقَالِينَ closes: the look-alike of derivation, attached.",
 "tr": "«DEDİ (kâle): Ben sizin işinizden NEFRET EDENLERDENİM (el-kâlîn)» (Şuarâ 168) — قَالَ açar, الْقَالِينَ kapar: ilhak edilen şibh-i iştikak."},
 "tokens": [
  tok("قَالَ","qala","verb",[R, "hollow-verbs"], "فِعْلٌ مَاضٍ أَجْوَفُ، وَالْفَاعِلُ مُسْتَتِرٌ.", "«he said».", "«dedi»."),
  tok("إِنِّي","inna","part",[R, "inna-wa-akhawatuha"], "إِنَّ وَاسْمُهَا: يَاءُ الْمُتَكَلِّمِ.", "«I am» — inna with the speaker's ya.", "«ben» — inne ve mütekellim yâsı.",
      segments=[seg("إِنَّ","inna","part"), seg("ي","pron-1s","pron")]),
  tok("لِعَمَلِكُمْ","amal-work","noun",[R, "huruf-jarr", "idafa-definiteness"], "جَارٌّ وَمَجْرُورٌ مُضَافٌ — مُتَعَلِّقٌ بِالْقَالِينَ.", "«of your deed».", "«işinizden».",
      segments=[seg("لِ","li","prep"), seg("عَمَلِ","amal-work","noun"), seg("كُمْ","pron-2mp","pron")]),
  tok("مِنَ","min","part",[R, "huruf-jarr", "inna-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ إِنَّ.", "«among» — inna's khabar.", "«-den» — innenin haberi."),
  tok("الْقَالِينَ","qalin","noun",[R, "huruf-jarr", "jam-mudhakkar-salim", "ism-fail"], "مَجْرُورٌ بِالْيَاءِ — جَمْعُ مُذَكَّرٍ سَالِمٌ مِنْ قَالٍ.", "«those who detest».", "«nefret edenler»."),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "mulhaq", "pair": [ix(S[-1], "قَالَ"), ix(S[-1], "الْقَالِينَ")]}]

# ----------- s6 — in verse (RESTORED)
S.append({"id": "s6", "translation": {
 "en": "And in VERSE, that one of the two be at the CLOSE of the bayt and the other at the HEAD of the first misraʿ, or in its MIDDLE, or at its END, or at the HEAD of the second." + R_EN,
 "tr": "NAZIMDA ise ikisinden birinin beytin SONUNDA, öbürünün birinci mısraın BAŞINDA, yahut ORTASINDA, yahut SONUNDA, yahut ikincinin BAŞINDA olmasıdır." + R_TR},
 "tokens": [
  tok("وَفِي","fi","prep",[R, "huruf-jarr", "mubtada-khabar", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِي حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ مُقَدَّمٌ.", "«and in» — the fronted khabar.", "«ve -de» — öne alınmış haber.",
      segments=[seg("وَ","wa","conj"), seg("فِي","fi","prep")]),
  tok("النَّظْمِ","nazm","noun",[R, "huruf-jarr"], "مَجْرُورٌ — النَّظْمُ: الشِّعْرُ.", "«verse».", "«nazım»."),
  tok("أَنْ","an-masdariyya","part",[R, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ نَاصِبٌ — وَالْمَصْدَرُ الْمُؤَوَّلُ مُبْتَدَأٌ مُؤَخَّرٌ.", "«that» — the clause is the delayed mubtada.", "«-ması» — cümle sona bırakılmış mübtedâ."),
  tok("يَكُونَ","kana","verb",[R, "kana-wa-akhawatuha", "an-masdariyya", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَنْصُوبٌ بِأَنْ.", "«be» — kana, mansub.", "«olsun» — kâne, mansûb."),
  tok("أَحَدُهُمَا","ahad","noun",[R, "kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَكُونَ مَرْفُوعٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«one of the two» — kana's ism.", "«ikisinden biri» — kânenin ismi.",
      segments=[seg("أَحَدُ","ahad","noun"), seg("هُمَا","pron-3d","pron")]),
  tok("فِي","fi","prep",[R, "huruf-jarr", "kana-wa-akhawatuha"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرُ يَكُونَ.", "«at» — kana's khabar.", "«-de» — kânenin haberi."),
  tok("آخِرِ","akhir","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the close of».", "«sonunda»."),
  tok("الْبَيْتِ","bayt","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the bayt».", "«beytin»."),
  tok("وَالْآخَرُ","akhar","noun",[R, "atf-nasaq", "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْآخَرُ مُبْتَدَأٌ.", "«and the other» — the mubtada.", "«ve öbürü» — mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("الْآخَرُ","akhar","noun")]),
  tok("فِي","fi","prep",[R, "huruf-jarr", "mubtada-khabar"], "حَرْفُ جَرٍّ — وَالْجَارُّ وَالْمَجْرُورُ خَبَرٌ.", "«at» — the khabar.", "«-de» — haber."),
  tok("صَدْرِ","sadr","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the head of».", "«başında»."),
  tok("الْمِصْرَاعِ","misra","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the misraʿ» — the hemistich.", "«mısraın»."),
  tok("الْأَوَّلِ","awwal","noun",[R, "idafa-definiteness"], "نَعْتٌ مَجْرُورٌ.", "«first».", "«birinci»."),
 ] + aw_x(R, "حَشْوِهِ", "hashw", "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ؛ الْحَشْوُ: وَسَطُ الْمِصْرَاعِ.", "«or its middle» — the hashw, the filling.", "«yahut ortasında» — haşv, dolgu.", [seg("حَشْوِ","hashw","noun"), seg("هِ","pron-3ms","pron")])
   + aw_x(R, "آخِرِهِ", "akhir", "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«or its end».", "«yahut sonunda».", [seg("آخِرِ","akhir","noun"), seg("هِ","pron-3ms","pron")])
   + aw_x(R, "صَدْرِ", "sadr", "مَعْطُوفٌ مَجْرُورٌ، مُضَافٌ.", "«or the head of».", "«yahut başında».") + [
  tok("الثَّانِي","thani","noun",[R, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَنْقُوصٌ: الْمِصْرَاعِ الثَّانِي.", "«the second» — the second misraʿ.", "«ikincinin» — ikinci mısraın."),
 ]})

# ----------- s7 — swift to strike a cousin, not swift to bounty (head of the first misraʿ)
S.append({"id": "s7", "translation": {
 "en": "«SWIFT (sariʿ) to strike his cousin's face — and to the caller of bounty not SWIFT (bi-sariʿ).» — the repeated word at the head of the first misraʿ." + RB_EN,
 "tr": "«Amcaoğlunun yüzüne vurmakta ÇEVİK (serî'), cömertliğe çağırana ise ÇEVİK değil (bi-serî').» — tekrarlanan kelime birinci mısraın başında." + RB_TR},
 "tokens": [
  tok("سَرِيعٌ","sari","noun",[R, "mubtada-khabar"], "خَبَرٌ لِمُبْتَدَأٍ مَحْذُوفٍ: هُوَ سَرِيعٌ.", "«swift» — the khabar of a dropped «he is».", "«çevik» — düşmüş «o» mübtedâsının haberi."),
  tok("إِلَى","ila","prep",[R, "huruf-jarr"], "حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِسَرِيعٍ.", "«to».", "«-e»."),
  tok("ابْنِ","ibn","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ.", "«the son of».", "«oğluna»."),
  tok("الْعَمِّ","amm-uncle","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — ابْنُ الْعَمِّ: الْقَرِيبُ.", "«the paternal uncle» — the cousin: his kin.", "«amcanın» — amcaoğlu: yakını."),
  tok("يَلْطِمُ","latama","verb",[R, "hal", "mudari-marfu"], "فِعْلٌ مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — وَالْجُمْلَةُ حَالٌ.", "«striking» — the clause is a hal.", "«vurarak» — cümle hâl."),
  tok("وَجْهَهُ","wajh","noun",[R, "maful-bihi", "idafa-definiteness"], "مَفْعُولٌ بِهِ مَنْصُوبٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«his face».", "«yüzüne».",
      segments=[seg("وَجْهَ","wajh","noun"), seg("هُ","pron-3ms","pron")], punct="*"),
  tok("وَلَيْسَ","laysa","verb",[R, "kana-wa-akhawatuha", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَيْسَ فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ.", "«and he is not» — laysa with its ism concealed.", "«ve değil» — leyse, ismi gizli.",
      segments=[seg("وَ","wa","conj"), seg("لَيْسَ","laysa","verb")]),
  tok("إِلَى","ila","prep",[R, "huruf-jarr"], "حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِسَرِيعٍ الْآتِي.", "«to».", "«-e»."),
  tok("دَاعِي","dai","noun",[R, "huruf-jarr", "idafa-definiteness", "ism-maqsur-manqus", "ism-fail"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مَنْقُوصٌ ثَبَتَتْ يَاؤُهُ لِلْإِضَافَةِ.", "«the caller of» — the manqus keeps its ya in the idafa.", "«çağıranına» — manqûs, izafette yâsı durur."),
  tok("النَّدَى","nada-bounty","noun",[R, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ: الْكَرَمُ.", "«bounty» — a maqsur.", "«cömertlik» — maksûr."),
  tok("بِسَرِيعِ","sari","noun",[R, "kana-wa-akhawatuha", "huruf-jarr"], "الْبَاءُ زَائِدَةٌ فِي خَبَرِ لَيْسَ، وَسَرِيعِ مَجْرُورٌ لَفْظًا مَنْصُوبٌ مَحَلًّا — وَكُسِرَ لِلرَّوِيِّ بِلَا تَنْوِينٍ.", "«swift» — laysa's khabar under the extra ba; the rhyme's kasra without tanwin.", "«çevik» — zâid bâ ile leysenin haberi; revî kesresi tenvinsiz.",
      segments=[seg("بِ","bi","prep"), seg("سَرِيعِ","sari","noun")]),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "tikrar", "at": "sadr-awwal", "pair": [ix(S[-1], "سَرِيعٌ"), ix(S[-1], "بِسَرِيعِ")]}]

# ----------- s8 — the ʿarar of Najd (the middle of the first misraʿ)
S.append({"id": "s8", "translation": {
 "en": "«Take your fill of the scent of the ʿARAR of Najd — for after this evening there is no ʿARAR.» — the repeated word in the middle of the first misraʿ." + RB_EN,
 "tr": "«Necd'in ARÂR çiçeğinin kokusundan nasibini al — bu akşamdan sonra ARÂR yok.» — tekrarlanan kelime birinci mısraın ortasında." + RB_TR},
 "tokens": [
  tok("تَمَتَّعْ","tamattaa","verb",[R, "fail"], "فِعْلُ أَمْرٍ مِنْ تَمَتَّعَ، وَالْفَاعِلُ مُسْتَتِرٌ: أَنْتَ.", "«take your fill» — the command of Form V.", "«nasibini al» — V. bâbdan emir."),
  tok("مِنْ","min","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«of».", "«-den»."),
  tok("شَمِيمِ","shamim","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — الشَّمِيمُ: الرَّائِحَةُ.", "«the scent of».", "«kokusundan»."),
  tok("عَرَارِ","arar","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ — الْعَرَارُ: نَبْتٌ طَيِّبُ الرِّيحِ.", "«the ʿarar of» — a sweet-smelling plant.", "«arâr» — güzel kokulu bir ot."),
  tok("نَجْدٍ","najd","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نَجْدٌ: الْبِلَادُ الْعَالِيَةُ.", "«Najd» — the highland.", "«Necd» — yüksek yurt.", punct="*"),
  tok("فَمَا","ma-nafiya","part",[R, "anwa-ma"], "الْفَاءُ لِلتَّعْلِيلِ، وَمَا نَافِيَةٌ.", "«for … not».", "«çünkü … yok».",
      segments=[seg("فَ","fa","conj"), seg("مَا","ma-nafiya","part")]),
  tok("بَعْدَ","bada","noun",[R, "maful-fih", "idafa-definiteness", "mubtada-khabar"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ — خَبَرٌ مُقَدَّمٌ.", "«after» — the fronted khabar.", "«sonra» — öne alınmış haber."),
  tok("الْعَشِيَّةِ","ashiyya","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْعَشِيَّةُ: آخِرُ النَّهَارِ.", "«this evening».", "«bu akşam»."),
  tok("مِنْ","min","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ زَائِدٌ.", "«(any)» — an extra min.", "«hiç» — zâid min."),
  tok("عَرَارِ","arar","noun",[R, "mubtada-khabar", "huruf-jarr"], "مُبْتَدَأٌ مُؤَخَّرٌ مَجْرُورٌ لَفْظًا بِمِنِ الزَّائِدَةِ مَرْفُوعٌ مَحَلًّا — وَكُسِرَ لِلرَّوِيِّ.", "«ʿarar» — the delayed mubtada under the extra min; the rhyme's kasra.", "«arâr» — zâid min altında sona bırakılmış mübtedâ; revî kesresi."),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "tikrar", "at": "hashw-awwal", "pair": [ix(S[-1], "عَرَارِ", 1), ix(S[-1], "عَرَارِ", 2)]}]

# ----------- s9 — enamoured of the white-breasted, enamoured of white blades (the end of the first misraʿ)
S.append({"id": "s9", "translation": {
 "en": "«Whoever is ENAMOURED (mughraman) of the fair full-breasted girls — I am still ENAMOURED (mughrama) of the white cutting blades.» — the repeated word at the end of the first misraʿ." + RB_EN,
 "tr": "«Kim beyaz tenli, göğsü dolgun kızlara TUTKUNSA (muğramen) — ben hâlâ beyaz keskin kılıçlara TUTKUNUM (muğramâ).» — tekrarlanan kelime birinci mısraın sonunda." + RB_TR},
 "tokens": [
  tok("وَمَنْ","man-shart","pron",[R, "mubtada-khabar", "in-shartiyya"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَمَنِ اسْمُ شَرْطٍ جَازِمٌ مُبْتَدَأٌ.", "«whoever» — the conditional man, the mubtada.", "«kim» — şart ismi men, mübtedâ.",
      segments=[seg("وَ","wa","conj"), seg("مَنْ","man-shart","pron")]),
  tok("كَانَ","kana","verb",[R, "kana-wa-akhawatuha", "in-shartiyya"], "فِعْلٌ مَاضٍ نَاقِصٌ — فِعْلُ الشَّرْطِ، وَاسْمُهُ مُسْتَتِرٌ.", "«is» — kana, the shart verb.", "«ise» — kâne, şart fiili."),
  tok("بِالْبِيضِ","bid-white","noun",[R, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْبِيضِ مَجْرُورٌ — مُتَعَلِّقٌ بِمُغْرَمًا: النِّسَاءُ الْبِيضُ.", "«of the fair» — hangs on «enamoured»: the fair women.", "«beyaz tenlilere» — «tutkun»a bağlı: beyaz kadınlar.",
      segments=[seg("بِ","bi","prep"), seg("الْبِيضِ","bid-white","noun")]),
  tok("الْكَوَاعِبِ","kaib","noun",[R, "jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ كَاعِبٍ: الْجَارِيَةُ نَهَدَ ثَدْيُهَا.", "«full-breasted» — the na't, the plural of kaʿib.", "«göğsü dolgun» — na't, kâib'in cemi."),
  tok("مُغْرَمًا","mughram","noun",[R, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ كَانَ مَنْصُوبٌ — اسْمُ مَفْعُولٍ مِنْ أُغْرِمَ بِهِ: أُولِعَ.", "«enamoured» — kana's khabar.", "«tutkun» — kânenin haberi.", punct="*"),
  tok("فَمَا","ma-nafiya","part",[R, "in-shartiyya", "anwa-ma"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَمَا نَافِيَةٌ.", "«then … not» — the fa of the jawab.", "«… -medim» — cevap fâsı.",
      segments=[seg("فَ","fa","conj"), seg("مَا","ma-nafiya","part")]),
  tok("زِلْتُ","zala","verb",[R, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ أَخَوَاتِ كَانَ، وَالتَّاءُ اسْمُهُ — مَا زِلْتُ: لَمْ أَزَلْ.", "«I am still» — ma zala, a sister of kana.", "«hâlâ» — mâ zâle, kânenin kız kardeşi."),
  tok("بِالْبِيضِ","bid-white","noun",[R, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْبِيضِ مَجْرُورٌ — السُّيُوفُ الْبِيضُ.", "«of the white» — the white blades.", "«beyazlara» — beyaz kılıçlar.",
      segments=[seg("بِ","bi","prep"), seg("الْبِيضِ","bid-white","noun")]),
  tok("الْقَوَاضِبِ","qadib","noun",[R, "jam-taksir"], "نَعْتٌ مَجْرُورٌ — جَمْعُ قَاضِبٍ: السَّيْفُ الْقَاطِعُ.", "«cutting» — the na't, the plural of qadib.", "«keskin» — na't, kâdıb'ın cemi."),
  tok("مُغْرَمَا","mughram","noun",[R, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ زِلْتُ مَنْصُوبٌ — وَأَلِفُ الْإِطْلَاقِ لِلرَّوِيِّ بَدَلَ التَّنْوِينِ.", "«enamoured» — zala's khabar; the rhyme's alif for the tanwin.", "«tutkun» — zâlenin haberi; tenvin yerine ıtlak elifi."),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "tikrar", "at": "arud", "pair": [ix(S[-1], "مُغْرَمًا"), ix(S[-1], "مُغْرَمَا")]}]

# ----------- s10 — a little of an hour (the head of the second misraʿ)
S.append({"id": "s10", "translation": {
 "en": "«And though it be no more than the halting of an hour, a LITTLE (qalilan) — yet its LITTLE (qaliluha) is of profit to me.» — the repeated word at the head of the second misraʿ." + RB_EN,
 "tr": "«Bir saatlik konaklamadan, AZDAN (kalîlen) başkası olmasa da — onun AZI (kalîluhâ) bana yeter.» — tekrarlanan kelime ikinci mısraın başında." + RB_TR},
 "tokens": [
  tok("وَإِنْ","in-shartiyya","part",[R, "in-shartiyya", "atf-nasaq"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَإِنْ حَرْفُ شَرْطٍ جَازِمٌ.", "«and though».", "«ve … de».",
      segments=[seg("وَ","wa","conj"), seg("إِنْ","in-shartiyya","part")]),
  tok("لَمْ","lam-jazima","part",[R, "in-shartiyya"], "حَرْفُ نَفْيٍ وَجَزْمٍ وَقَلْبٍ.", "«not».", "«-medi»."),
  tok("يَكُنْ","kana","verb",[R, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مُضَارِعٌ نَاقِصٌ مَجْزُومٌ — فِعْلُ الشَّرْطِ.", "«it be» — kana majzum, the shart verb.", "«olmasa» — meczûm kâne, şart fiili."),
  tok("إِلَّا","illa","part",[R, "istithna"], "أَدَاةُ حَصْرٍ.", "«no more than» — the illa of restriction.", "«-den başka» — hasr edatı."),
  tok("مُعَرَّجُ","muarraj","noun",[R, "kana-wa-akhawatuha", "idafa-definiteness"], "اسْمُ يَكُنْ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ — التَّعْرِيجُ: الْوُقُوفُ وَالْإِقَامَةُ.", "«the halting of» — kana's delayed ism.", "«konaklama» — kânenin sona bırakılmış ismi."),
  tok("سَاعَةٍ","saa-hour","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«an hour».", "«bir saatlik».", punct="*"),
  tok("قَلِيلًا","qalil","noun",[R, "kana-wa-akhawatuha"], "خَبَرُ يَكُنْ مَنْصُوبٌ — مُقَدَّمٌ عَلَى الِاسْمِ فِي الرُّتْبَةِ.", "«a little» — kana's khabar.", "«az» — kânenin haberi."),
  tok("فَإِنِّي","inna","part",[R, "in-shartiyya", "inna-wa-akhawatuha"], "الْفَاءُ وَاقِعَةٌ فِي جَوَابِ الشَّرْطِ، وَإِنَّ وَاسْمُهَا يَاءُ الْمُتَكَلِّمِ.", "«then I» — the fa of the jawab; inna with the speaker's ya.", "«bana» — cevap fâsı; inne ve mütekellim yâsı.",
      segments=[seg("فَ","fa","conj"), seg("إِنَّ","inna","part"), seg("ي","pron-1s","pron")]),
  tok("نَافِعٌ","nafi","noun",[R, "inna-wa-akhawatuha", "ism-fail"], "خَبَرُ إِنَّ مَرْفُوعٌ — اسْمُ فَاعِلٍ يَعْمَلُ عَمَلَ فِعْلِهِ.", "«of profit» — inna's khabar; a participle that governs.", "«yararlı» — innenin haberi; amel eden ism-i fâil."),
  tok("لِي","li","prep",[R, "huruf-jarr"], "جَارٌّ وَمَجْرُورٌ — مُتَعَلِّقٌ بِنَافِعٍ.", "«to me».", "«bana».",
      segments=[seg("لِ","li","prep"), seg("ي","pron-1s","pron")]),
  tok("قَلِيلُهَا","qalil","noun",[R, "fail", "idafa-definiteness"], "فَاعِلٌ لِنَافِعٍ مَرْفُوعٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«its little» — the doer of the participle.", "«onun azı» — ism-i fâilin fâili.",
      segments=[seg("قَلِيلُ","qalil","noun"), seg("هَا","pron-3fs","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "tikrar", "at": "sadr-thani", "pair": [ix(S[-1], "قَلِيلًا"), ix(S[-1], "قَلِيلُهَا")]}]

# ----------- s11 — al-Arrajani: «leave me, you two» … «called me» (jinas, head of the first misraʿ)
S.append({"id": "s11", "translation": {
 "en": "«LEAVE ME (daʿani), you two, from your blame, out of folly — for the caller of longing CALLED ME (daʿani) before you.» — the two in jinas: one at the close, one at the head of the first misraʿ." + RB_EN,
 "tr": "«İkiniz BENİ BIRAKIN (deânî) kınamanızdan, akılsızlıktan — çünkü özlem çağırıcısı sizden önce BENİ ÇAĞIRDI (deânî).» — cinaslı ikisi: biri sonda, biri birinci mısraın başında." + RB_TR},
 "tokens": [
  tok("دَعَانِي","da-leave","verb",[R, "maful-bihi", "fail"], "فِعْلُ أَمْرٍ لِلْمُثَنَّى مِنْ وَدَعَ (دَعْ): دَعَا، وَالْأَلِفُ فَاعِلٌ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ.", "«leave me, you two» — the dual command with the guarding nun and «me».", "«ikiniz beni bırakın» — tesniye emir, vikaye nûnu ve «beni».",
      segments=[seg("دَعَا","da-leave","verb"), seg("نِي","pron-1s","pron")]),
  tok("مِنْ","min","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("مَلَامِكُمَا","malam","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ؛ الْمَلَامُ: اللَّوْمُ.", "«your blame» — the reproach of you two.", "«ikinizin kınaması».",
      segments=[seg("مَلَامِ","malam","noun"), seg("كُمَا","pron-2d","pron")]),
  tok("سَفَاهًا","safah","noun",[R, "maful-lah"], "مَفْعُولٌ لِأَجْلِهِ مَنْصُوبٌ — أَوْ مَفْعُولٌ مُطْلَقٌ: أَيْ مَلَامًا سَفَاهًا.", "«out of folly» — the object of reason (or an absolute object).", "«akılsızlıktan» — mef'ûlün leh (yahut mutlak).", punct="*"),
  tok("فَدَاعِي","dai","noun",[R, "mubtada-khabar", "idafa-definiteness", "ism-maqsur-manqus", "ism-fail"], "الْفَاءُ لِلتَّعْلِيلِ، وَدَاعِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ، مُضَافٌ — مَنْقُوصٌ.", "«for the caller of» — the mubtada, a manqus.", "«çünkü çağırıcısı» — mübtedâ, manqûs.",
      segments=[seg("فَ","fa","conj"), seg("دَاعِي","dai","noun")]),
  tok("الشَّوْقِ","shawq","noun",[R, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«longing».", "«özlemin»."),
  tok("قَبْلَكُمَا","qabla","noun",[R, "maful-fih", "idafa-definiteness"], "ظَرْفُ زَمَانٍ مَنْصُوبٌ، مُضَافٌ — وَالضَّمِيرُ مُضَافٌ إِلَيْهِ.", "«before you two».", "«sizden önce».",
      segments=[seg("قَبْلَ","qabla","noun"), seg("كُمَا","pron-2d","pron")]),
  tok("دَعَانِي","daa","verb",[R, "mubtada-khabar", "naqis-verbs", "maful-bihi"], "فِعْلٌ مَاضٍ نَاقِصٌ مِنْ دَعَا، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ، وَالنُّونُ لِلْوِقَايَةِ، وَالْيَاءُ مَفْعُولٌ بِهِ — وَالْجُمْلَةُ خَبَرٌ.", "«called me» — the naqis mazi of daʿa; the khabar.", "«beni çağırdı» — deâ'nın nâkıs mâzîsi; haber.",
      segments=[seg("دَعَا","daa","verb"), seg("نِي","pron-1s","pron")]),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "jinas", "at": "sadr-awwal", "pair": [ix(S[-1], "دَعَانِي", 1), ix(S[-1], "دَعَانِي", 2)]},
                 {"kind": "jinas", "sub": "tamm", "kind2": "mumathil", "pair": [ix(S[-1], "دَعَانِي", 1), ix(S[-1], "دَعَانِي", 2)]}]

# ----------- s12 — Abu Tammam: the cutting blades, now blunted (mulhaq, head of the second misraʿ)
S.append({"id": "s12", "translation": {
 "en": "«The white CUTTING blades (bawatir) were cutting in the fray — and now, after him, they are BLUNT (butr).» — one root, ب ت ر: the two attached to the jinas, one at the close and one at the head of the second misraʿ." + RB_EN,
 "tr": "«Beyaz KESKİN kılıçlar (bevâtir) savaşta keskindi — ondan sonra şimdi KÖRDÜR (bütr).» — tek kök, ب ت ر: cinâsa ilhak edilen ikisi, biri sonda, biri ikinci mısraın başında." + RB_TR},
 "tokens": [
  tok("وَكَانَتِ","kana","verb",[R, "kana-wa-akhawatuha"], "الْوَاوُ اسْتِئْنَافِيَّةٌ، وَكَانَتْ فِعْلٌ مَاضٍ نَاقِصٌ، وَالتَّاءُ لِلتَّأْنِيثِ كُسِرَتْ لِالْتِقَاءِ السَّاكِنَيْنِ.", "«and they were» — kana feminine, the ta with the wasl kasra.", "«ve idi» — müennes kâne, tâ vasıl kesresiyle.",
      segments=[seg("وَ","wa","conj"), seg("كَانَتِ","kana","verb")]),
  tok("الْبِيضُ","bid-white","noun",[R, "kana-wa-akhawatuha"], "اسْمُ كَانَ مَرْفُوعٌ — السُّيُوفُ.", "«the white ones» — kana's ism: the swords.", "«beyazlar» — kânenin ismi: kılıçlar."),
  tok("الْبَوَاتِرُ","batir","noun",[R, "jam-taksir", "ism-fail"], "نَعْتٌ مَرْفُوعٌ — جَمْعُ بَاتِرٍ: الْقَاطِعُ.", "«cutting» — the na't, the plural of batir.", "«keskin» — na't, bâtir'in cemi."),
  fi(R),
  tok("الْوَغَى","wagha","noun",[R, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ: الْحَرْبُ.", "«the fray» — a maqsur: war.", "«savaşta» — maksûr: harp.", punct="*"),
  tok("بَوَاتِرَ","batir","noun",[R, "kana-wa-akhawatuha", "mamnu-min-sarf", "jam-taksir"], "خَبَرُ كَانَ مَنْصُوبٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ (صِيغَةُ مُنْتَهَى الْجُمُوعِ).", "«cutting» — kana's khabar, a diptote plural.", "«keskin» — kânenin haberi, gayr-i munsarif cemi."),
  tok("فَهْيَ","hiya","pron",[R, "mubtada-khabar"], "الْفَاءُ عَاطِفَةٌ، وَهْيَ مُبْتَدَأٌ — سُكِّنَتْ هَاؤُهَا لِلْوَزْنِ.", "«and now they» — the mubtada; its ha made quiescent for the metre.", "«şimdi onlar» — mübtedâ; hâsı vezin için sâkin.",
      segments=[seg("فَ","fa","conj"), seg("هْيَ","hiya","pron")]),
  tok("الْآنَ","al-an","noun",[R, "maful-fih"], "ظَرْفُ زَمَانٍ مَبْنِيٌّ عَلَى الْفَتْحِ.", "«now» — the zarf built on the fatha.", "«şimdi» — fetha üzere mebnî zarf."),
  tok("مِنْ","min","part",[R, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den»."),
  tok("بَعْدِهِ","bada","noun",[R, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، مُضَافٌ — وَالْهَاءُ مُضَافٌ إِلَيْهِ: مِنْ بَعْدِ مَوْتِهِ.", "«after him» — after his death.", "«ondan sonra» — ölümünden sonra.",
      segments=[seg("بَعْدِ","bada","noun"), seg("هِ","pron-3ms","pron")]),
  tok("بُتْرُ","abtar","noun",[R, "mubtada-khabar", "jam-taksir"], "خَبَرٌ مَرْفُوعٌ — جَمْعُ أَبْتَرَ: الْمَقْطُوعُ، الْكَلِيلُ؛ وَحُذِفَ تَنْوِينُهُ لِلرَّوِيِّ.", "«blunt» — the khabar, the plural of abtar; its tanwin dropped for the rhyme.", "«kör» — haber, ebter'in cemi; tenvini revî için düşmüş."),
 ]})
S[-1]["badi"] = [{"kind": "radd-ajuz", "kind2": "mulhaq", "at": "sadr-thani", "pair": [ix(S[-1], "بَوَاتِرَ"), ix(S[-1], "بُتْرُ")]},
                 {"kind": "jinas", "sub": "ishtiqaq", "pair": [ix(S[-1], "بَوَاتِرَ"), ix(S[-1], "بُتْرُ")]}]

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "nathr": need("nathr", "نَثْر", "ن ث ر", "noun", "prose — unmetred speech (masdar of نَثَرَ: to scatter)", "nesir — vezinsiz söz (نَثَرَ: saçmak'ın masdarı)", 4),
 "ahaqq": need("ahaqq", "أَحَقّ", "ح ق ق", "noun", "having more right, worthier (ism tafdil of حَقِيق)", "daha lâyık, daha haklı (حَقِيق'in ism-i tafdili)", 3),
 "sail-flowing": need("sail-flowing", "سَائِل", "س ي ل", "noun", "flowing, running (ism fa'il of سَالَ «to flow» — not of سَأَلَ «to ask»)", "akan (سَالَ «akmak»ın ism-i fâili — سَأَلَ «istemek»in değil)", 4),
 "istaghfara": need("istaghfara", "اِسْتَغْفَرَ", "غ ف ر", "verb", "to ask forgiveness (Form X; اِسْتَغْفَرَ يَسْتَغْفِرُ)", "mağfiret dilemek (X. bâb; اِسْتَغْفَرَ يَسْتَغْفِرُ)", 2, form="X"),
 "ghaffar": need("ghaffar", "غَفَّار", "غ ف ر", "noun", "ever-forgiving (the intensive فَعَّال)", "çok bağışlayıcı (فَعَّال vezninde mübalağa)", 2),
 "hashw": need("hashw", "حَشْو", "ح ش و", "noun", "the filling — the middle of a misraʿ between its head and its close; padding", "haşv — mısraın başı ile sonu arasındaki orta; dolgu", 4),
 "sari": need("sari", "سَرِيع", "س ر ع", "noun", "swift, quick (a sifa mushabbaha)", "çevik, hızlı (sıfat-ı müşebbehe)", 2),
 "amm-uncle": need("amm-uncle", "عَمّ", "ع م م", "noun", "paternal uncle; ابْنُ الْعَمِّ: the cousin, one's kin", "amca; ابْنُ الْعَمِّ: amcaoğlu, akraba", 2, plural="أَعْمَام"),
 "latama": need("latama", "لَطَمَ", "ل ط م", "verb", "to slap, to strike the face (لَطَمَ يَلْطِمُ)", "tokat vurmak, yüze vurmak (لَطَمَ يَلْطِمُ)", 4),
 "dai": need("dai", "دَاعٍ (الدَّاعِي)", "د ع و", "noun", "a caller, one who calls or summons (ism fa'il of دَعَا — a manqus)", "çağıran, davet eden (دَعَا'nın ism-i fâili — manqûs)", 3),
 "tamattaa": need("tamattaa", "تَمَتَّعَ", "م ت ع", "verb", "to enjoy, to take one's fill of (Form V; تَمَتَّعَ بِـ)", "faydalanmak, nasibini almak (V. bâb; تَمَتَّعَ بِـ)", 3, form="V"),
 "shamim": need("shamim", "شَمِيم", "ش م م", "noun", "scent, fragrance", "koku, rayiha", 5),
 "arar": need("arar", "عَرَار", "ع ر ر", "noun", "the ʿarar — a sweet-smelling yellow flower of Najd", "arâr — Necd'in güzel kokulu sarı çiçeği", 5),
 "najd": need("najd", "نَجْد", None, "noun", "Najd — the highland of Arabia", "Necd — Arabistan'ın yüksek yurdu", 4),
 "ashiyya": need("ashiyya", "عَشِيَّة", "ع ش و", "noun", "the evening, the close of the day", "akşam, günün sonu", 3),
 "man-shart": need("man-shart", "مَنْ (الشَّرْطِيَّة)", None, "pron", "whoever (the conditional man — jazm on two verbs)", "her kim (şart edatı men — iki fiili cezm eder)", 3),
 "kaib": need("kaib", "كَاعِب", "ك ع ب", "noun", "a girl whose breasts have rounded (pl. كَوَاعِب)", "göğsü dolgunlaşmış genç kız (ç. كَوَاعِب)", 5, plural="كَوَاعِب"),
 "mughram": need("mughram", "مُغْرَم", "غ ر م", "noun", "enamoured, infatuated (ism maf'ul of أُغْرِمَ بِـ)", "tutkun, vurgun (أُغْرِمَ بِـ'nin ism-i mef'ûlü)", 4),
 "zala": need("zala", "زَالَ", "ز ي ل", "verb", "to cease (مَا زَالَ: to be still, to continue — a sister of كَانَ)", "kesilmek (مَا زَالَ: hâlâ olmak, sürmek — كَانَ'nin kız kardeşi)", 3),
 "qadib": need("qadib", "قَاضِب", "ق ض ب", "noun", "cutting, a cutting sword (pl. قَوَاضِب)", "keskin, keskin kılıç (ç. قَوَاضِب)", 5, plural="قَوَاضِب"),
 "muarraj": need("muarraj", "مُعَرَّج", "ع ر ج", "noun", "a halting, a stopping-place on the way (a mimi masdar of عَرَّجَ)", "konaklama, yolda duraklama (عَرَّجَ'nin mîmî masdarı)", 5),
 "nafi": need("nafi", "نَافِع", "ن ف ع", "noun", "beneficial, of profit (ism fa'il of نَفَعَ)", "yararlı, faydalı (نَفَعَ'nin ism-i fâili)", 2),
 "malam": need("malam", "مَلَام", "ل و م", "noun", "blame, reproach (a masdar of لَامَ)", "kınama, levm (لَامَ'nin masdarı)", 3),
 "safah": need("safah", "سَفَاه", "س ف ه", "noun", "folly, foolishness", "akılsızlık, sefahet", 4),
 "shawq": need("shawq", "شَوْق", "ش و ق", "noun", "longing, yearning", "özlem, şevk", 3),
 "batir": need("batir", "بَاتِر", "ب ت ر", "noun", "cutting, sharp (ism fa'il of بَتَرَ; pl. بَوَاتِر)", "keskin, kesen (بَتَرَ'nin ism-i fâili; ç. بَوَاتِر)", 5, plural="بَوَاتِر"),
 "al-an": need("al-an", "الْآنَ", "ء و ن", "noun", "now (a zarf built on the fatha)", "şimdi (fetha üzere mebnî zarf)", 2),
 "abtar": need("abtar", "أَبْتَر", "ب ت ر", "noun", "cut off, blunted, tailless (pl. بُتْر)", "kesik, kör, kuyruksuz (ç. بُتْر)", 4, plural="بُتْر"),
}
for k in ("radd", "ajuz", "ala", "sadr", "huwa", "fi", "an-masdariyya", "jaala", "ahad", "lafz", "mukarrar", "mutajanis", "mulhaq", "bi", "awwal", "fiqra", "akhar", "akhir", "khashiya",
          "nas", "allah", "sail", "laim", "rajaa", "dam-tear", "rabb", "inna", "kana", "qala", "amal-work", "min", "qalin", "nazm", "bayt", "misra", "thani", "ila", "ibn", "wajh", "laysa",
          "nada-bounty", "ma-nafiya", "bada", "bid-white", "saa-hour", "qalil", "li", "da-leave", "daa", "qabla", "wagha", "hiya", "in-shartiyya", "lam-jazima", "illa", "aw", "wa", "fa",
          "pron-3d", "pron-3fs", "pron-3ms", "pron-2mp", "pron-1s", "pron-2d"):
    if k not in TG: CAND[k] = find_gloss(k)
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
put_morph(mo, "istaghfara", _sg.derived(_sg.B10, _sg.W10, "َ", "اِسْتَغْفَر", "سْتَغْفِر", "اِسْتَغْفِر", "اِسْتِغْفَار", "مُسْتَغْفِر", "مُسْتَغْفَر", "اُسْتُغْفِرَ", "يُسْتَغْفَرُ"))
put_morph(mo, "latama", _sg.sound1("daraba", "لَطَم", "لْطِم", "اِلْطِم", "لَطْم", "لَاطِم", "مَلْطُوم", "لُطِمَ", "يُلْطَمُ"))
put_morph(mo, "tamattaa", _sg.derived(_sg.B5, _sg.W5, "َ", "تَمَتَّع", "تَمَتَّع", "تَمَتَّع", "تَمَتُّع", "مُتَمَتِّع", "مُتَمَتَّع", "تُمُتِّعَ", "يُتَمَتَّعُ"))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")

# ---------------------------------------------------------------- notes
NOTE_R = {
 "id": "radd-al-ajuz",
 "title": {"ar": "رَدُّ الْعَجُزِ عَلَى الصَّدْرِ — فِي النَّثْرِ وَفِي النَّظْمِ، وَمَوَاضِعُهُ الْخَمْسَةُ", "en": "Radd al-ʿajuz ʿala al-sadr — in prose and verse, and its five seats", "tr": "Reddü'l-acüz ale's-sadr — nesirde ve nazımda, beş yeri"},
 "level": 6, "group": "badi",
 "classicalSources": ["تلخيص المفتاح — رد العجز على الصدر: هو في النثر أن يجعل أحد اللفظين المكررين أو المتجانسين أو الملحقين بهما في أول الفقرة والآخر في آخرها، نحو: وتخشى الناس والله أحق أن تخشاه؛ سائل اللئيم يرجع ودمعه سائل؛ استغفروا ربكم إنه كان غفارا؛ قال إني لعملكم من القالين. وفي النظم أن يكون أحدهما في آخر البيت والآخر في صدر المصراع الأول أو حشوه أو آخره أو صدر الثاني."],
 "question": {
  "en": ["Does the word that CLOSES the line already stand near its HEAD? That is RADD AL-ʿAJUZ ʿALA AL-SADR — «the close brought back upon the head». The two words may be the SAME (تَخْشَى … تَخْشَاهُ, 33:37), in JINAS (سَائِلُ the asker … سَائِلٌ the flowing), or ATTACHED to the jinas by derivation (اسْتَغْفِرُوا … غَفَّارًا, 71:10) or its look-alike (قَالَ … الْقَالِينَ, 26:168).",
         "In PROSE the seats are two: the head of the fiqra and its close. In VERSE the close is fixed — the last word of the bayt — and the partner takes one of FOUR seats: the head of the first misraʿ (سَرِيعٌ … بِسَرِيعِ; دَعَانِي … دَعَانِي), its middle, the hashw (عَرَارِ … عَرَارِ), its end, the ʿarud (مُغْرَمًا … مُغْرَمَا), or the head of the second misraʿ (قَلِيلًا … قَلِيلُهَا; بَوَاتِرَ … بُتْرُ).",
         "What does the engine read? The last word of the line against every earlier word: the same key, a jinas pair or a shared root names the kind; the partner's seat is measured against the misraʿ break the corpus marks with *. Repeats that are mere grammar (a preposition, a pronoun) are refused."],
  "tr": ["Satırı KAPATAN kelime, BAŞINA yakın bir yerde zaten duruyor mu? Bu REDDÜ'L-ACÜZ ALE'S-SADR'dır — «sonun başa döndürülmesi». İki kelime AYNI olabilir (تَخْشَى … تَخْشَاهُ, Ahzâb 37), CİNASLI (سَائِلُ isteyen … سَائِلٌ akan), yahut iştikakla (اسْتَغْفِرُوا … غَفَّارًا, Nûh 10) veya benzeriyle (قَالَ … الْقَالِينَ, Şuarâ 168) cinâsa İLHAK edilmiş.",
         "NESİRDE yer ikidir: fıkranın başı ve sonu. NAZIMDA son sabittir — beytin son kelimesi — eş DÖRT yerden birini alır: birinci mısraın başı (سَرِيعٌ … بِسَرِيعِ; دَعَانِي … دَعَانِي), ortası, haşv (عَرَارِ … عَرَارِ), sonu, arûz (مُغْرَمًا … مُغْرَمَا), yahut ikinci mısraın başı (قَلِيلًا … قَلِيلُهَا; بَوَاتِرَ … بُتْرُ).",
         "Motor neyi okur? Satırın son kelimesini önceki her kelimeyle: aynı anahtar, cinas çifti yahut ortak kök kısmı adlandırır; eşin yeri, külliyatın * ile işaretlediği mısra kırılmasına göre ölçülür. Yalnız gramer olan tekrarlar (harf-i cer, zamir) reddedilir."]},
 "plain": {
  "en": "The last word of the line is brought back near its head — repeated, in jinas, or attached. Prose: head and close of the fiqra. Verse: the close of the bayt, and the partner at the head, middle or end of the first misraʿ or the head of the second.",
  "tr": "Satırın son kelimesi başına yakın bir yere döndürülür — tekrar, cinas yahut ilhak ile. Nesir: fıkranın başı ve sonu. Nazım: beytin sonu; eş birinci mısraın başında, ortasında, sonunda yahut ikincinin başında."},
 "explanation": {
  "en": "رَدُّ الْعَجُزِ عَلَى الصَّدْرِ: فِي النَّثْرِ أَنْ يُجْعَلَ أَحَدُ اللَّفْظَيْنِ الْمُكَرَّرَيْنِ أَوِ الْمُتَجَانِسَيْنِ أَوِ الْمُلْحَقَيْنِ بِهِمَا فِي أَوَّلِ الْفِقْرَةِ وَالْآخَرُ فِي آخِرِهَا — three kinds of pair, two seats. وَفِي النَّظْمِ أَنْ يَكُونَ أَحَدُهُمَا فِي آخِرِ الْبَيْتِ وَالْآخَرُ فِي صَدْرِ الْمِصْرَاعِ الْأَوَّلِ أَوْ حَشْوِهِ أَوْ آخِرِهِ أَوْ صَدْرِ الثَّانِي — the same three kinds, four seats for the partner. The six bayts the Talkhis cites are given by the source in Turkish with only the paired words in Arabic; the reader restores the received text and says so.",
  "tr": "رَدُّ الْعَجُزِ عَلَى الصَّدْرِ: فِي النَّثْرِ أَنْ يُجْعَلَ أَحَدُ اللَّفْظَيْنِ الْمُكَرَّرَيْنِ أَوِ الْمُتَجَانِسَيْنِ أَوِ الْمُلْحَقَيْنِ بِهِمَا فِي أَوَّلِ الْفِقْرَةِ وَالْآخَرُ فِي آخِرِهَا — üç çift türü, iki yer. وَفِي النَّظْمِ أَنْ يَكُونَ أَحَدُهُمَا فِي آخِرِ الْبَيْتِ وَالْآخَرُ فِي صَدْرِ الْمِصْرَاعِ الْأَوَّلِ أَوْ حَشْوِهِ أَوْ آخِرِهِ أَوْ صَدْرِ الثَّانِي — aynı üç tür, eş için dört yer. Telhîs'in andığı altı beyti kaynak yalnız Türkçe, eşleşen kelimeleri Arapça verir; okuyucu alınan metni geri yazar ve bunu söyler."},
 "examples": [
  {"ar": "وَتَخْشَى النَّاسَ وَاللهُ أَحَقُّ أَنْ تَخْشَاهُ", "en": "33:37 — prose, the repeated word.", "tr": "Ahzâb 37 — nesir, tekrarlanan kelime.", "sourceStory": "talkhis-al-miftah", "sentence": "s2"},
  {"ar": "سَائِلُ اللَّئِيمِ يَرْجِعُ وَدَمْعُهُ سَائِلٌ", "en": "prose, the two in jinas.", "tr": "nesir, cinaslı ikisi.", "sourceStory": "talkhis-al-miftah", "sentence": "s3"},
  {"ar": "سَرِيعٌ إِلَى ابْنِ الْعَمِّ يَلْطِمُ وَجْهَهُ * وَلَيْسَ إِلَى دَاعِي النَّدَى بِسَرِيعِ", "en": "verse — the head of the first misraʿ.", "tr": "nazım — birinci mısraın başı.", "sourceStory": "talkhis-al-miftah", "sentence": "s7"},
  {"ar": "وَكَانَتِ الْبِيضُ الْبَوَاتِرُ فِي الْوَغَى * بَوَاتِرَ فَهْيَ الْآنَ مِنْ بَعْدِهِ بُتْرُ", "en": "Abu Tammam — the head of the second misraʿ, attached by derivation.", "tr": "Ebû Temmâm — ikinci mısraın başı, iştikakla ilhak.", "sourceStory": "talkhis-al-miftah", "sentence": "s12"}],
 "commonMistakes": [
  {"wrong": "«Beyitte aynı kelime iki kere geçti: reddü'l-acüz vardır»",
   "right": "«Şart, birinin beytin SONUNDA olmasıdır; öbürü dört yerden birinde — ortada iki tekrar sanat değildir»",
   "why": {"en": "The figure is named for the close (ʿajuz) brought back upon the head; the seat is the rule.", "tr": "Sanat adını başa döndürülen SON'dan (acüz) alır; yer kuraldır."}}],
 "relatedNotes": ["jinas", "jinas-tamm", "mulhaq-bil-jinas", "saj", "ilm-al-badi"]}

ADD_EN = (" Chapter 70 (lines ~4476-4510, sahifa 154-156) is radd al-ʿajuz ʿala al-sadr: in prose the repeated word (33:37 s2), the two in jinas "
          "(s3), the two attached (71:10 s4; 26:168 s5); in verse the four seats of the partner — the head of the first misraʿ (s7; al-Arrajani "
          "s11), its middle (s8), its end (s9), the head of the second (Dhu l-Rumma s10; Abu Tammam s12). The two definitions (s1, s6) are RESTORED "
          "from the received matn. The SIX BAYTS (s7-s12) are RESTORED too: the source gives each only in Turkish paraphrase with the paired words "
          "in Arabic (سَرِيعٌ، عَرَارِ، مُغْرَمًا، قَلِيل، دَعَانِي، بَوَاتِرُ/بُتْرٌ), and the Arabic printed here is the received text the Talkhis cites, "
          "each marked «Restored» in its translation. The `badi` frames of kind `radd-ajuz` carry `kind2` (tikrar, jinas, mulhaq), the `pair` and, "
          "in verse, the partner's seat `at` (sadr-awwal, hashw-awwal, arud, sadr-thani); the jinas and ishtiqaq pairs are framed beside them.")
ADD_TR = (" Yetmişinci bâb (satır ~4476-4510, sahife 154-156) reddü'l-acüz ale's-sadr'dır: nesirde tekrarlanan kelime (Ahzâb 37 s2), cinaslı "
          "ikisi (s3), ilhak edilen ikisi (Nûh 10 s4; Şuarâ 168 s5); nazımda eşin dört yeri — birinci mısraın başı (s7; Errecânî s11), ortası (s8), "
          "sonu (s9), ikincinin başı (Zürrumme s10; Ebû Temmâm s12). İki tarif (s1, s6) alınan metinden GERİ YAZILMIŞTIR. ALTI BEYİT (s7-s12) de "
          "geri yazılmıştır: kaynak her birini yalnız Türkçe, eşleşen kelimeleri Arapça verir (سَرِيعٌ، عَرَارِ، مُغْرَمًا، قَلِيل، دَعَانِي، بَوَاتِرُ/بُتْرٌ); "
          "buradaki Arapça, Telhîs'in andığı alınan metindir ve her biri tercümesinde «geri yazılmıştır» diye işaretlidir. `radd-ajuz` cinsinden "
          "`badi` çerçeveleri `kind2` (tekrar, cinas, mülhak), `pair` ve nazımda eşin yeri `at` (sadr-ı evvel, haşv-i evvel, arûz, sadr-ı sânî) "
          "taşır; cinas ve iştikak çiftleri yanlarında çerçevelenir.")
write_out(70, S, TITLE, ADD_EN, ADD_TR, "4476-4510", GLOSS_ADD, notes=(NOTE_R,),
          related=(("jinas", ["radd-al-ajuz"]), ("mulhaq-bil-jinas", ["radd-al-ajuz"]), ("saj", ["radd-al-ajuz"]), ("ilm-al-badi", ["radd-al-ajuz"])))
report(70, S, GLOSS_ADD, (NOTE_R,))
