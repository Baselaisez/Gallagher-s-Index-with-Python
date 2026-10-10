# -*- coding: utf-8 -*-
"""Al-Kafiya (Ibn al-Hajib) — chapter 1: the KALIMA and its three kinds (the ism, the fiʿl, the harf), the definitions the matn opens with
(lafz, wadʿ, maʿna), the KALAM and the ISNAD, the two-word minimum, the ism's marks. Source: Ziya Sungur-oglu's Ottoman notebook on the
Kafiya (Turkish معناسى glosses under every definition), lines ~60-135 of the transcription; Molla Jami's questions feed the note.

  COMMENTARY sentences (the notebook's or the teacher's, not the matn): s8 (the كَلْم etymology), s14 (the five non-kalam compounds) — marked C_EN/C_TR.
  The two bayts s9-s10 are ʿAli's, cited by the notebook for the wound of the tongue (hemistich mark * on the first half).
  python3 tools/authoring/author_kafiya_ch1.py
"""
import json, os, sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from kafiya_common import *
import kafiya_common as _kc
import sarf_gen as _sg
PKG = _kc.PKG

K = "al-kalima-wal-kalam"
TITLE = {"ar": "الْكَلِمَةُ وَأَقْسَامُهَا وَالْكَلَامُ", "en": "The word, its three kinds, and the sentence", "tr": "Kelime, üç kısmı ve kelâm"}
S = []
TG = json.loads((PKG / "glossary.json").read_text(encoding="utf-8"))["entries"]
B8 = "الْبَابُ الثَّامِنُ: اِفْتَعَلَ يَفْتَعِلُ"; W8 = "اِفْتَعَلَ يَفْتَعِلُ"

def fi(tag=K, punct=None): return tok("فِي", "fi", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def ala(tag=K): return tok("عَلَى", "ala", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«on».", "«üzerine».")
def aw(tag=K): return tok("أَوْ", "aw", "conj", [tag, "atf-nasaq"], "حَرْفُ عَطْفٍ لِلتَّقْسِيمِ.", "«or».", "«ya da».")
def mina(tag=K, full="مِنَ"): return tok(full, "min", "prep", [tag, "huruf-jarr"], "حَرْفُ جَرٍّ.", "«from».", "«-den».")
def ma_maws(tag, ar, en, tr):
    return tok("مَا", "ma-mawsula", "pron", [tag, "ism-mawsul", "mubtada-khabar"], ar, en, tr)
def mana_j(tags, punct=None):
    return tok("مَعْنًى", "mana", "noun", [K, "huruf-jarr", "ism-maqsur-manqus"] + tags, "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ عَلَى الْأَلِفِ الْمَحْذُوفَةِ لِالْتِقَاءِ السَّاكِنَيْنِ — اسْمٌ مَقْصُورٌ مُنَوَّنٌ.", "«a meaning» — a maqsur noun, its kasra estimated.", "«bir mana» — maksûr isim, kesresi takdîrî.", punct=punct)
def bi_ahad():
    return [tok("بِأَحَدِ", "ahad", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْبَاءُ حَرْفُ جَرٍّ، وَأَحَدِ مَجْرُورٌ، مُضَافٌ.", "«with one of».", "«birine».", segments=[seg("بِ", "bi", "prep"), seg("أَحَدِ", "ahad", "noun")]),
            tok("الْأَزْمِنَةِ", "zaman", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ زَمَانٍ عَلَى أَفْعِلَةٍ.", "«the tenses» — the broken plural of زَمَان.", "«zamanların» — zamân'ın cem-i mükesseri.", segments=None),
            tok("الثَّلَاثَةِ", "thalatha", "noun", [K, "naat-sifa"], "صِفَةٌ لِلْأَزْمِنَةِ مَجْرُورَةٌ.", "«three».", "«üç».")]
def dalla_def(subj_full, subj_lex, subj_en, subj_tr):
    """X مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ — the shared opening of the three definitions."""
    return [tok(subj_full, subj_lex, "noun", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالِاسْمُ بَعْدَهَا مُبْتَدَأٌ مَرْفُوعٌ.", subj_en, subj_tr, segments=[seg("وَ", "wa", "conj"), seg(subj_full[2:], subj_lex, "noun")]),
            ma_maws(K, "اسْمٌ مَوْصُولٌ خَبَرٌ — أَيْ: الَّذِي دَلَّ.", "«that which» — the relative, the khabar.", "«… olan şey» — ism-i mevsûl, haber."),
            tok("دَلَّ", "dalla", "verb", [K, "ism-mawsul", "doubled-verbs"], "مَاضٍ مُضَاعَفٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةُ الْمَوْصُولِ.", "«points» — the relative clause.", "«delâlet eder» — sıla."),
            ala(),
            mana_j([]),
            fi(),
            tok("نَفْسِهِ", "nafs", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: فِي نَفْسِ الْمَعْنَى.", "«in itself».", "«kendi nefsinde».", segments=[seg("نَفْسِ", "nafs", "noun"), pr3msi()])]

# ----------- s1 — the kalima
S.append({"id": "s1", "translation": {
 "en": "The word is an utterance set down for a single meaning.",
 "tr": "Kelime, müfred (tek) bir mana için konulmuş lafızdır."},
 "tokens": [
  tok("الْكَلِمَةُ", "kalima", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the word» — the mubtada.", "«kelime» — mübtedâ."),
  tok("لَفْظٌ", "lafz", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ — الْجِنْسُ فِي الْحَدِّ.", "«an utterance» — the khabar, the genus of the definition.", "«lafız» — haber, tarifin cinsi."),
  tok("وُضِعَ", "wadaa", "verb", [K, "naib-al-fail", "jumla-sifa"], "مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ صِفَةٌ لِلَفْظٍ.", "«set down» — passive; the clause qualifies «utterance».", "«konulmuş» — meçhul; cümle lafz'ın sıfatı."),
  tok("لِمَعْنًى", "mana", "noun", [K, "huruf-jarr", "ism-maqsur-manqus", "naib-al-fail"], "اللَّامُ صِلَةٌ لَا لِلتَّعْلِيلِ، وَمَعْنًى مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — فِي مَعْنَى الْمَفْعُولِ بِهِ.", "«for a meaning» — the lam links the verb to its object, it is not the lam of cause.", "«bir mana için» — lâm ta'lîl değil sıla: fiili mef'ûlüne bağlar.", segments=[seg("لِ", "li", "prep"), seg("مَعْنًى", "mana", "noun")]),
  tok("مُفْرَدٍ", "mufrad", "noun", [K, "naat-sifa", "ism-maful"], "صِفَةٌ لِمَعْنًى مَجْرُورَةٌ — وَقِيلَ: صِفَةٌ لِلَفْظٍ فَتُرْفَعُ.", "«single» — qualifying «meaning»; some read it as qualifying «utterance» and raise it.", "«müfred» — mana'nın sıfatı; lafz'ın sıfatı okuyup ref' edenler de var.", punct="."),
 ]})

# ----------- s2 — the three kinds
S.append({"id": "s2", "translation": {
 "en": "And it is a noun, a verb and a particle.",
 "tr": "Ve o isim, fiil ve harftir."},
 "tokens": [
  tok("وَهِيَ", "hiya", "pron", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَهِيَ مُبْتَدَأٌ — الْكَلِمَةُ.", "«and it» — the mubtada.", "«ve o» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("هِيَ", "hiya", "pron")]),
  tok("اسْمٌ", "ism", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a noun» — the khabar.", "«isim» — haber."),
  tok("وَفِعْلٌ", "fil", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَفِعْلٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a verb».", "«ve fiil».", segments=[seg("وَ", "wa", "conj"), seg("فِعْلٌ", "fil", "noun")]),
  tok("وَحَرْفٌ", "harf", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَحَرْفٌ مَعْطُوفٌ مَرْفُوعٌ.", "«and a particle».", "«ve harf».", segments=[seg("وَ", "wa", "conj"), seg("حَرْفٌ", "harf", "noun")], punct="."),
 ]})

# ----------- s3 — the first division
S.append({"id": "s3", "translation": {
 "en": "Because it either points to a meaning in itself or does not; and the second is the particle.",
 "tr": "Çünkü ya kendi nefsinde bir manaya delâlet eder ya etmez; ikincisi harftir."},
 "tokens": [
  tok("لِأَنَّهَا", "anna", "part", [K, "inna-wa-akhawatuha", "lam-taleel"], "اللَّامُ لِلتَّعْلِيلِ، وَأَنَّ حَرْفُ تَوْكِيدٍ وَنَصْبٍ، وَهَا اسْمُهَا.", "«because it» — the lam of cause over أَنَّ and its noun.", "«çünkü o» — ta'lîl lâmı, enne ve ismi.", segments=[seg("لِ", "lam-taleel", "part"), seg("أَنَّ", "anna", "part"), pr3fs()]),
  tok("إِمَّا", "imma", "part", [K], "حَرْفُ تَفْصِيلٍ — يُقَابِلُهَا أَوْ.", "«either» — answered by «or».", "«ya» — karşılığı «ya da»."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "inna-wa-akhawatuha"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرُ أَنَّ: دَلَالَتُهَا.", "«that» — the masdar is the khabar of أَنَّ.", "«-mesi» — masdar enne'nin haberi."),
  tok("تَدُلَّ", "dalla", "verb", [K, "an-masdariyya", "doubled-verbs"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هِيَ — مُضَاعَفٌ.", "«it points» — a doubled verb.", "«delâlet etmesi» — muzâaf."),
  ala(),
  mana_j([]),
  fi(),
  tok("نَفْسِهَا", "nafs", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَهَا مُضَافٌ إِلَيْهِ.", "«in itself».", "«kendi nefsinde».", segments=[seg("نَفْسِ", "nafs", "noun"), pr3fs()]),
  aw(),
  tok("لَا", "la", "part", [K, "atf-nasaq"], "نَافِيَةٌ — أَيْ: أَوْ لَا تَدُلَّ، حُذِفَ الْمَعْطُوفُ.", "«not» — «or does not», the verb dropped.", "«etmez» — «ya da etmez», fiil hazfedildi.", punct="،"),
  tok("وَالثَّانِي", "thani", "noun", [K, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«and the second» — a manqus mubtada.", "«ikincisi» — mankûs mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الثَّانِي", "thani", "noun")]),
  tok("الْحَرْفُ", "harf", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«the particle».", "«harftir».", punct="."),
 ]})

# ----------- s4 — the second division
S.append({"id": "s4", "translation": {
 "en": "And the first either joins with one of the three tenses or does not: the second is the noun, the first the verb.",
 "tr": "Birincisi de ya üç zamandan birine yakın olur ya olmaz: ikincisi isim, birincisi fiildir."},
 "tokens": [
  tok("وَالْأَوَّلُ", "awwal", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْأَوَّلُ مُبْتَدَأٌ مَرْفُوعٌ.", "«and the first» — the mubtada.", "«birincisi» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْأَوَّلُ", "awwal", "noun")]),
  tok("إِمَّا", "imma", "part", [K], "حَرْفُ تَفْصِيلٍ.", "«either».", "«ya»."),
  tok("أَنْ", "an-masdariyya", "part", [K, "an-masdariyya", "mubtada-khabar"], "حَرْفٌ مَصْدَرِيٌّ — وَالْمَصْدَرُ خَبَرُ الْأَوَّلِ.", "«that» — the masdar is the khabar.", "«-mesi» — masdar haber."),
  tok("يَقْتَرِنَ", "iqtarana", "verb", [K, "an-masdariyya", "form-viii-verbs"], "مُضَارِعٌ مَنْصُوبٌ بِأَنْ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — افْتَعَلَ.", "«it joins» — Form VIII.", "«yakın olması» — iftiâl."),
  *bi_ahad(),
  aw(),
  tok("لَا", "la", "part", [K, "atf-nasaq"], "نَافِيَةٌ — أَيْ: أَوْ لَا يَقْتَرِنَ.", "«not».", "«olmaz».", punct="،"),
  tok("وَالثَّانِي", "thani", "noun", [K, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ عَاطِفَةٌ، وَالثَّانِي مُبْتَدَأٌ — مَنْقُوصٌ.", "«and the second».", "«ikincisi».", segments=[seg("وَ", "wa", "conj"), seg("الثَّانِي", "thani", "noun")]),
  tok("الِاسْمُ", "ism", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«the noun».", "«isimdir».", punct="،"),
  tok("وَالْأَوَّلُ", "awwal", "noun", [K, "mubtada-khabar"], "الْوَاوُ عَاطِفَةٌ، وَالْأَوَّلُ مُبْتَدَأٌ.", "«and the first».", "«birincisi».", segments=[seg("وَ", "wa", "conj"), seg("الْأَوَّلُ", "awwal", "noun")]),
  tok("الْفِعْلُ", "fil", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«the verb».", "«fiildir».", punct="."),
 ]})

# ----------- s5 — the lafz
S.append({"id": "s5", "translation": {
 "en": "The utterance is what a human being pronounces, really or by ruling, whether meaningless or set down, whether single or compound.",
 "tr": "Lafız, ister mühmel ister mevzû olsun, ister müfred ister mürekkeb olsun, insanın hakikaten ya da hükmen telaffuz ettiği şeydir."},
 "tokens": [
  tok("اللَّفْظُ", "lafz", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«the utterance».", "«lafız»."),
  ma_maws(K, "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what» — the relative, the khabar.", "«… şey» — mevsûl, haber."),
  tok("يَتَلَفَّظُ", "talaffaza", "verb", [K, "ism-mawsul", "form-v-verbs"], "مُضَارِعٌ مَرْفُوعٌ — صِلَةُ الْمَوْصُولِ؛ تَفَعَّلَ.", "«pronounces» — Form V, the relative clause.", "«telaffuz eder» — tefa''ul, sıla."),
  tok("بِهِ", "bi", "prep", [K, "huruf-jarr", "ism-mawsul"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — الْعَائِدُ.", "«it» — the returning pronoun.", "«onu» — âid.", segments=[seg("بِ", "bi", "prep"), pr3msi()]),
  tok("الْإِنْسَانُ", "insan", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«a human being» — the doer.", "«insan» — fâil."),
  tok("حَقِيقَةً", "haqiqa", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ — أَوْ مَفْعُولٌ مُطْلَقٌ لِفِعْلٍ مَحْذُوفٍ.", "«really».", "«hakikaten»."),
  aw(),
  tok("حُكْمًا", "hukm", "noun", [K, "hal", "atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ — كَالضَّمِيرِ الْمُسْتَتِرِ فِي اضْرِبْ.", "«or by ruling» — like the hidden pronoun in «strike!».", "«ya da hükmen» — «vur!» daki gizli zamir gibi.", punct="،"),
  tok("مُهْمَلًا", "muhmal", "noun", [K, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ كَانَ مُقَدَّمٌ مَنْصُوبٌ — الْمُهْمَلُ: مَا لَمْ يُوضَعْ لِمَعْنًى، كَدَيْزٍ.", "«meaningless» — the khabar of كَانَ set first; like دَيْز.", "«mühmel» — kâne'nin öne alınmış haberi; deyz gibi."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha", "hollow-verbs"], "فِعْلٌ مَاضٍ نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ: هُوَ — وَالْجُمْلَةُ حَالٌ.", "«be it» — its noun hidden; the clause is a hal.", "«olsun» — ismi gizli; cümle hâl."),
  aw(),
  tok("مَوْضُوعًا", "mawdu", "noun", [K, "atf-nasaq", "ism-maful"], "مَعْطُوفٌ عَلَى مُهْمَلًا مَنْصُوبٌ.", "«or set down».", "«ya da mevzû».", punct="،"),
  tok("مُفْرَدًا", "mufrad", "noun", [K, "kana-wa-akhawatuha", "ism-maful"], "خَبَرُ كَانَ الثَّانِيَةِ مُقَدَّمٌ.", "«single».", "«müfred»."),
  tok("كَانَ", "kana", "verb", [K, "kana-wa-akhawatuha", "hollow-verbs"], "نَاقِصٌ، وَاسْمُهُ مُسْتَتِرٌ.", "«be it».", "«olsun»."),
  aw(),
  tok("مُرَكَّبًا", "murakkab", "noun", [K, "atf-nasaq", "ism-maful"], "مَعْطُوفٌ مَنْصُوبٌ.", "«or compound».", "«ya da mürekkeb».", punct="."),
 ]})

# ----------- s6 — the wadʿ
S.append({"id": "s6", "translation": {
 "en": "And setting-down is the assigning of one thing to another such that, whenever the first thing is uttered or perceived, the second thing is understood from it.",
 "tr": "Vaz', birinci şey kullanıldığı ya da hissedildiği zaman ondan ikinci şeyin anlaşılması cihetiyle bir şeyi bir şeye tahsis etmektir."},
 "tokens": [
  tok("وَالْوَضْعُ", "wad-put", "noun", [K, "mubtada-khabar", "masdar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْوَضْعُ مُبْتَدَأٌ — مَصْدَرُ وَضَعَ.", "«and setting-down» — the masdar of وَضَعَ.", "«vaz'» — vadaa'nın masdarı.", segments=[seg("وَ", "wa", "conj"), seg("الْوَضْعُ", "wad-put", "noun")]),
  tok("تَخْصِيصُ", "takhsis", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ — مَصْدَرُ خَصَّصَ.", "«the assigning» — the khabar, annexed.", "«tahsis» — haber, muzâf."),
  tok("شَيْءٍ", "shay", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«of a thing».", "«bir şeyi»."),
  tok("بِشَيْءٍ", "shay", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«to a thing».", "«bir şeye».", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")]),
  tok("بِحَيْثُ", "haythu", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَحَيْثُ ظَرْفٌ مَبْنِيٌّ عَلَى الضَّمِّ فِي مَحَلِّ جَرٍّ.", "«such that» — حَيْثُ built on damma.", "«… cihetiyle» — haysü damme üzere mebnî.", segments=[seg("بِ", "bi", "prep"), seg("حَيْثُ", "haythu", "noun")]),
  tok("مَتَى", "mata", "part", [K, "in-shartiyya"], "اسْمُ شَرْطٍ ظَرْفُ زَمَانٍ مَبْنِيٌّ — يَجْزِمُ فِعْلَيْنِ.", "«whenever» — a conditional adverb.", "«… zaman» — şart ismi, zarf."),
  tok("أُطْلِقَ", "atlaqa", "verb", [K, "naib-al-fail", "form-iv-verbs", "in-shartiyya"], "مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — فِعْلُ الشَّرْطِ.", "«is uttered» — the condition, passive.", "«kullanılır» — şart fiili, meçhul."),
  aw(),
  tok("أُحِسَّ", "ahassa", "verb", [K, "naib-al-fail", "form-iv-verbs", "doubled-verbs", "atf-nasaq"], "مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ — أَحَسَّ الْمُضَاعَفُ.", "«or is perceived» — Form IV of a doubled root.", "«ya da hissedilir» — muzâaf if'âl."),
  tok("الشَّيْءُ", "shay", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the thing» — the deputy doer.", "«şey» — nâib-i fâil."),
  tok("الْأَوَّلُ", "awwal", "noun", [K, "naat-sifa"], "صِفَةٌ مَرْفُوعَةٌ.", "«first».", "«birinci»."),
  tok("فُهِمَ", "fahima", "verb", [K, "naib-al-fail", "in-shartiyya"], "مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ فِي مَحَلِّ جَزْمٍ — جَوَابُ الشَّرْطِ.", "«is understood» — the answer of the condition.", "«anlaşılır» — cezâ."),
  tok("مِنْهُ", "min", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ.", "«from it».", "«ondan».", segments=[seg("مِنْ", "min", "prep"), pr3ms()]),
  tok("الشَّيْءُ", "shay", "noun", [K, "naib-al-fail"], "نَائِبُ فَاعِلٍ مَرْفُوعٌ.", "«the thing».", "«şey»."),
  tok("الثَّانِي", "thani", "noun", [K, "naat-sifa", "ism-maqsur-manqus"], "صِفَةٌ مَرْفُوعَةٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَنْقُوصٌ.", "«second».", "«ikinci».", punct="."),
 ]})

# ----------- s7 — the maʿna
S.append({"id": "s7", "translation": {
 "en": "And the meaning is what is intended by a thing.",
 "tr": "Mana, bir şeyle kastolunan şeydir."},
 "tokens": [
  tok("وَالْمَعْنَى", "mana", "noun", [K, "mubtada-khabar", "ism-maqsur-manqus"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمَعْنَى مُبْتَدَأٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«and the meaning» — a maqsur mubtada.", "«mana» — maksûr mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْمَعْنَى", "mana", "noun")]),
  ma_maws(K, "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what».", "«… şey»."),
  tok("يُقْصَدُ", "qasada", "verb", [K, "ism-mawsul", "naib-al-fail"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ: هُوَ — صِلَةٌ.", "«is intended» — passive, the relative clause.", "«kastolunur» — meçhul, sıla."),
  tok("بِشَيْءٍ", "shay", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«by a thing».", "«bir şeyle».", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")], punct="."),
 ]})

# ----------- s8 — the etymology (COMMENTARY)
S.append({"id": "s8", "translation": {
 "en": "And it is said: «word» and «speech» are both derived from kalm, which is the wound." + C_EN,
 "tr": "Denildi ki: kelime ve kelâm, yaralama demek olan kelm'den müştaktır." + C_TR},
 "tokens": [
  tok("وَقِيلَ", "qala", "verb", [K, "naib-al-fail"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَقِيلَ مَاضٍ مَبْنِيٌّ لِلْمَجْهُولِ — أَجْوَفُ؛ وَنَائِبُ فَاعِلِهِ الْجُمْلَةُ بَعْدَهُ.", "«and it is said» — the passive of the hollow قَالَ.", "«denildi» — ecvef kâle'nin meçhulü.", segments=[seg("وَ", "wa", "conj"), seg("قِيلَ", "qala", "verb")], punct=":"),
  tok("الْكَلِمَةُ", "kalima", "noun", [K, "mubtada-khabar"], "مُبْتَدَأٌ مَرْفُوعٌ.", "«word».", "«kelime»."),
  tok("وَالْكَلَامُ", "kalam", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْكَلَامُ مَعْطُوفٌ مَرْفُوعٌ.", "«and speech».", "«ve kelâm».", segments=[seg("وَ", "wa", "conj"), seg("الْكَلَامُ", "kalam", "noun")]),
  tok("مُشْتَقَّانِ", "mushtaqq", "noun", [K, "mubtada-khabar", "al-muthanna", "ism-maful", "form-viii-verbs"], "خَبَرٌ مَرْفُوعٌ بِالْأَلِفِ — مُثَنًّى؛ اسْمُ مَفْعُولِ اشْتَقَّ.", "«derived» — dual khabar; the passive participle of Form VIII.", "«müştaktır» — tesniye haber; iştakka'nın ism-i mef'ûlü."),
  mina(),
  tok("الْكَلْمِ", "kalm-wound", "noun", [K, "huruf-jarr", "masdar"], "مَجْرُورٌ — الْكَلْمُ: الْجَرْحُ.", "«kalm».", "«kelm»."),
  tok("وَهُوَ", "huwa", "pron", [K, "mubtada-khabar"], "الْوَاوُ حَالِيَّةٌ، وَهُوَ مُبْتَدَأٌ.", "«which is».", "«o da».", segments=[seg("وَ", "wa", "conj"), seg("هُوَ", "huwa", "pron")]),
  tok("الْجَرْحُ", "jarh", "noun", [K, "mubtada-khabar", "masdar"], "خَبَرٌ مَرْفُوعٌ — مَصْدَرُ جَرَحَ.", "«the wound».", "«yaradır».", punct="."),
 ]})

# ----------- s9-s10 — ʿAli's two bayts (basit)
S.append({"id": "s9", "translation": {
 "en": "The breadth of the open plain, with enemies, is a narrow place; the eye of the needle, with friends, is a field. (ʿAli's bayt as the notebook prints it.)",
 "tr": "Fezanın genişliği düşmanlarla dardır; iğnenin deliği dostlarla beraber meydandır. (Hz. Ali'nin beyti, defterin yazdığı gibi.)"},
 "tokens": [
  tok("رَحْبُ", "rahb", "noun", [K, "mubtada-khabar", "idafa-definiteness", "sifa-mushabbaha"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — رَحْبٌ: وَاسِعٌ؛ وَبِالضَّمِّ: السَّعَةُ.", "«the breadth of» — rahb «wide», ruhb «width».", "«genişliği» — rahb: geniş; ruhb: genişlik."),
  tok("الْفَضَاءِ", "fada-open", "noun", [K, "idafa-definiteness", "ism-mamdud"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَمْدُودٌ.", "«the open plain».", "«fezanın»."),
  mina(),
  tok("الْأَعْدَاءِ", "aduww", "noun", [K, "huruf-jarr", "jam-taksir"], "مَجْرُورٌ — جَمْعُ عَدُوٍّ.", "«enemies» — the plural of عَدُوّ.", "«düşmanlar» — adüvv'ün cem'i."),
  tok("ضَيِّقَةٌ", "dayyiq", "noun", [K, "mubtada-khabar", "sifa-mushabbaha"], "خَبَرٌ مَرْفُوعٌ — أُنِّثَ حَمْلًا عَلَى مَعْنَى الْأَرْضِ، كَمَا يَطْبَعُهُ الدَّفْتَرُ.", "«narrow» — feminine by sense (the land), as the notebook prints it.", "«dardır» — mana (yer) itibariyle müennes, defterin yazdığı gibi.", punct="*"),
  tok("سَمُّ", "samm", "noun", [K, "mubtada-khabar", "idafa-definiteness"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — سَمُّ الْخِيَاطِ: ثَقْبُ الْإِبْرَةِ.", "«the eye of» — the needle's eye.", "«deliği» — iğnenin deliği."),
  tok("الْخِيَاطِ", "khiyat", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — الْخِيَاطُ: الْإِبْرَةُ.", "«the needle».", "«iğnenin»."),
  tok("مَعَ", "maa", "noun", [K, "zarf-mustaqarr-wa-laghw"], "ظَرْفٌ مَنْصُوبٌ، مُضَافٌ.", "«with».", "«… ile beraber»."),
  tok("الْأَحْبَابِ", "habib", "noun", [K, "idafa-definiteness", "jam-taksir"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — جَمْعُ حَبِيبٍ.", "«friends».", "«dostlar»."),
  tok("مَيْدَانٌ", "maydan", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«a field».", "«meydandır».", punct="."),
 ]})
S.append({"id": "s10", "translation": {
 "en": "The wounds of the spear-head have a healing; but what the tongue has wounded does not heal.",
 "tr": "Süngünün yaraları iyileşir; ama dilin açtığı yaralar iyileşmez."},
 "tokens": [
  tok("جِرَاحَاتُ", "jiraha", "noun", [K, "mubtada-khabar", "idafa-definiteness", "jam-muannath-salim"], "مُبْتَدَأٌ مَرْفُوعٌ، مُضَافٌ — جَمْعُ جِرَاحَةٍ بِالْأَلِفِ وَالتَّاءِ.", "«the wounds of» — a sound feminine plural.", "«yaraları» — cem-i müennes sâlim."),
  tok("السِّنَانِ", "sinan", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — السِّنَانُ: نَصْلُ الرُّمْحِ.", "«the spear-head».", "«süngünün»."),
  tok("لَهَا", "li", "prep", [K, "huruf-jarr", "mubtada-khabar", "zarf-mustaqarr-wa-laghw"], "اللَّامُ حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — خَبَرٌ مُقَدَّمٌ لِالْتِيَامٌ، وَالْجُمْلَةُ خَبَرُ جِرَاحَاتُ.", "«have» — the fronted khabar of the inner sentence.", "«… vardır» — mukaddem haber.", segments=[seg("لِ", "li", "prep"), pr3fs()]),
  tok("الْتِيَامٌ", "iltiam", "noun", [K, "mubtada-khabar", "masdar", "form-viii-verbs"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ — مَصْدَرُ الْتَأَمَ، سُهِّلَتْ هَمْزَتُهُ يَاءً.", "«a healing» — the masdar of الْتَأَمَ, its hamza softened.", "«iyileşme» — ilteeme'nin masdarı, hemzesi yumuşatılmış.", punct="*"),
  tok("وَلَا", "la", "part", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«but not».", "«ama … -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part")]),
  tok("يَلْتَامُ", "iltaama", "verb", [K, "form-viii-verbs", "fail"], "مُضَارِعٌ مَرْفُوعٌ — أَصْلُهُ يَلْتَئِمُ، سُهِّلَتِ الْهَمْزَةُ لِلْوَزْنِ.", "«heals» — for يَلْتَئِمُ, the hamza softened for the metre.", "«iyileşir» — aslı yelteimu, hemze vezin için yumuşatıldı."),
  tok("مَا", "ma-mawsula", "pron", [K, "ism-mawsul", "fail"], "اسْمٌ مَوْصُولٌ فَاعِلٌ.", "«what» — the relative, the doer.", "«… şey» — mevsûl, fâil."),
  tok("جَرَحَ", "jaraha", "verb", [K, "ism-mawsul", "fail"], "مَاضٍ — صِلَةُ الْمَوْصُولِ، وَالْعَائِدُ مَحْذُوفٌ: جَرَحَهُ.", "«has wounded» — the relative clause, its returning pronoun dropped.", "«yaraladığı» — sıla, âid hazfedilmiş."),
  tok("اللِّسَانُ", "lisan", "noun", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«the tongue».", "«dil».", punct="."),
 ]})

# ----------- s11 — the kalam
S.append({"id": "s11", "translation": {
 "en": "And speech is what comprises two words by predication.",
 "tr": "Kelâm, isnad ile iki kelimeyi içine alan şeydir."},
 "tokens": [
  tok("وَالْكَلَامُ", "kalam", "noun", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْكَلَامُ مُبْتَدَأٌ.", "«and speech» — the mubtada.", "«kelâm» — mübtedâ.", segments=[seg("وَ", "wa", "conj"), seg("الْكَلَامُ", "kalam", "noun")]),
  ma_maws(K, "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what».", "«… şey»."),
  tok("تَضَمَّنَ", "tadammana", "verb", [K, "ism-mawsul", "form-v-verbs", "maful-bihi"], "مَاضٍ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — صِلَةٌ؛ تَفَعَّلَ.", "«comprises» — Form V.", "«içine alır» — tefa''ul."),
  tok("كَلِمَتَيْنِ", "kalima", "noun", [K, "maful-bihi", "al-muthanna"], "مَفْعُولٌ بِهِ مَنْصُوبٌ بِالْيَاءِ — مُثَنًّى.", "«two words» — a dual object.", "«iki kelimeyi» — tesniye mef'ûl."),
  tok("بِالْإِسْنَادِ", "isnad", "noun", [K, "huruf-jarr", "masdar", "form-iv-verbs"], "الْبَاءُ حَرْفُ جَرٍّ، وَالْإِسْنَادِ مَجْرُورٌ — مَصْدَرُ أَسْنَدَ.", "«by predication».", "«isnad ile».", segments=[seg("بِ", "bi", "prep"), seg("الْإِسْنَادِ", "isnad", "noun")], punct="."),
 ]})

# ----------- s12 — the isnad
S.append({"id": "s12", "translation": {
 "en": "And predication is the relating of one of the two words, really or by ruling, to the other, such that it gives the addressee a complete benefit upon which silence is sound.",
 "tr": "İsnad, muhataba üzerine sükût sahih olan tam bir fayda ifade etmesi cihetiyle, hakikaten ya da hükmen iki kelimeden birini diğerine nispet etmektir."},
 "tokens": [
  tok("وَالْإِسْنَادُ", "isnad", "noun", [K, "mubtada-khabar", "masdar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْإِسْنَادُ مُبْتَدَأٌ.", "«and predication».", "«isnad».", segments=[seg("وَ", "wa", "conj"), seg("الْإِسْنَادُ", "isnad", "noun")]),
  tok("نِسْبَةُ", "nisba", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar"], "خَبَرٌ مَرْفُوعٌ، مُضَافٌ.", "«the relating of» — the khabar.", "«nispet etmek» — haber."),
  tok("إِحْدَى", "ahad", "noun", [K, "idafa-definiteness", "ism-maqsur-manqus"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ، مُضَافٌ — مُؤَنَّثُ أَحَدٍ.", "«one of» — the feminine of أَحَد, maqsur.", "«birini» — ehad'in müennesi, maksûr."),
  tok("الْكَلِمَتَيْنِ", "kalima", "noun", [K, "idafa-definiteness", "al-muthanna"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«the two words».", "«iki kelimeden»."),
  tok("حَقِيقَةً", "haqiqa", "noun", [K, "hal"], "حَالٌ مَنْصُوبٌ.", "«really».", "«hakikaten»."),
  aw(),
  tok("حُكْمًا", "hukm", "noun", [K, "hal", "atf-nasaq"], "مَعْطُوفٌ مَنْصُوبٌ — كَإِسْنَادِ الْجُمْلَةِ.", "«or by ruling».", "«ya da hükmen»."),
  tok("إِلَى", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ — مُتَعَلِّقٌ بِنِسْبَةُ.", "«to».", "«-e»."),
  tok("الْأُخْرَى", "ukhra", "noun", [K, "huruf-jarr", "ism-maqsur-manqus"], "مَجْرُورٌ بِكَسْرَةٍ مُقَدَّرَةٍ — مَقْصُورٌ.", "«the other».", "«diğerine»."),
  tok("بِحَيْثُ", "haythu", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَحَيْثُ مَبْنِيٌّ فِي مَحَلِّ جَرٍّ.", "«such that».", "«… cihetiyle».", segments=[seg("بِ", "bi", "prep"), seg("حَيْثُ", "haythu", "noun")]),
  tok("يُفِيدُ", "afada", "verb", [K, "form-iv-verbs", "hollow-verbs", "maful-bihi"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ: هُوَ — أَفَادَ الْأَجْوَفُ، يَتَعَدَّى إِلَى مَفْعُولَيْنِ.", "«it gives» — hollow Form IV, taking two objects.", "«ifade eder» — ecvef if'âl, iki mef'ûl alır."),
  tok("الْمُخَاطَبَ", "mukhatab", "noun", [K, "maful-bihi", "ism-maful"], "مَفْعُولٌ بِهِ أَوَّلُ مَنْصُوبٌ.", "«the addressee» — the first object.", "«muhataba» — birinci mef'ûl."),
  tok("فَائِدَةً", "faida", "noun", [K, "maful-bihi"], "مَفْعُولٌ بِهِ ثَانٍ مَنْصُوبٌ.", "«a benefit» — the second object.", "«bir fayda» — ikinci mef'ûl."),
  tok("تَامَّةً", "tamm", "noun", [K, "naat-sifa", "ism-fail"], "صِفَةٌ مَنْصُوبَةٌ.", "«complete».", "«tam»."),
  tok("يَصِحُّ", "sahha", "verb", [K, "jumla-sifa", "doubled-verbs", "fail"], "مُضَارِعٌ مَرْفُوعٌ — مُضَاعَفٌ؛ وَالْجُمْلَةُ صِفَةٌ ثَانِيَةٌ لِفَائِدَةً.", "«is sound» — a second qualifying clause.", "«sahih olur» — ikinci sıfat cümlesi."),
  tok("السُّكُوتُ", "sukut", "noun", [K, "fail", "masdar"], "فَاعِلٌ مَرْفُوعٌ.", "«silence» — the doer.", "«sükût» — fâil."),
  tok("عَلَيْهَا", "ala", "prep", [K, "huruf-jarr", "jumla-sifa"], "حَرْفُ جَرٍّ، وَهَا مَجْرُورٌ — الْعَائِدُ إِلَى فَائِدَةً.", "«upon it» — the returning pronoun.", "«onun üzerine» — âid.", segments=[seg("عَلَيْ", "ala", "prep"), pr3fs()], punct="."),
 ]})

# ----------- s13 — the two-word minimum
S.append({"id": "s13", "translation": {
 "en": "And that comes about only in two nouns, as in «Zayd is standing», or in a verb and a noun, as in «Zayd stood».",
 "tr": "Bu da ancak ya «Zeyd ayaktadır» gibi iki isimde, ya da «Zeyd kalktı» gibi bir fiil ve bir isimde olur."},
 "tokens": [
  tok("وَلَا", "la", "part", [K, "istithna-mufarragh"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَلَا نَافِيَةٌ.", "«and not».", "«ve … -mez».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part")]),
  tok("يَتَأَتَّى", "taatta", "verb", [K, "form-v-verbs", "naqis-verbs", "fail"], "مُضَارِعٌ مَرْفُوعٌ بِضَمَّةٍ مُقَدَّرَةٍ — نَاقِصٌ مِنَ التَّفَعُّلِ: تَأَتَّى الْأَمْرُ: تَهَيَّأَ.", "«comes about» — a naqis Form V.", "«hâsıl olur» — nâkıs tefa''ul."),
  tok("ذَلِكَ", "dhalika", "pron", [K, "fail", "asma-al-ishara"], "اسْمُ إِشَارَةٍ فَاعِلٌ — الْإِسْنَادُ.", "«that» — the doer: the predication.", "«bu» — fâil: isnad."),
  tok("إِلَّا", "illa", "part", [K, "istithna-mufarragh"], "أَدَاةُ حَصْرٍ — اسْتِثْنَاءٌ مُفَرَّغٌ.", "«only» — an emptied exception.", "«ancak» — müferrağ istisnâ."),
  fi(),
  tok("اسْمَيْنِ", "ism", "noun", [K, "huruf-jarr", "al-muthanna"], "مَجْرُورٌ بِالْيَاءِ — مُثَنًّى.", "«two nouns».", "«iki isimde»."),
  tok("كَزَيْدٌ", "zayd", "propn", [K, "huruf-jarr", "mubtada-khabar"], "الْكَافُ جَارَّةٌ، وَزَيْدٌ قَائِمٌ جُمْلَةٌ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ — لِذَلِكَ بَقِيَ رَفْعُ زَيْدٌ.", "«as “Zayd» — a quoted sentence after the kaf, so Zayd keeps its damma.", "«“Zeyd» gibi — kâf'tan sonra hikâye edilen cümle, bu yüzden Zeyd merfû kalır.", segments=[seg("كَ", "ka", "prep"), seg("زَيْدٌ", "zayd", "propn")]),
  tok("قَائِمٌ", "qaim", "noun", [K, "mubtada-khabar", "ism-fail"], "خَبَرٌ مَرْفُوعٌ فِي الْجُمْلَةِ الْمَحْكِيَّةِ.", "«standing”».", "«ayaktadır”».", punct="،"),
  aw(),
  fi(),
  tok("فِعْلٍ", "fil", "noun", [K, "huruf-jarr"], "مَجْرُورٌ.", "«a verb».", "«bir fiil»."),
  tok("وَاسْمٍ", "ism", "noun", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَاسْمٍ مَعْطُوفٌ مَجْرُورٌ.", "«and a noun».", "«ve bir isimde».", segments=[seg("وَ", "wa", "conj"), seg("اسْمٍ", "ism", "noun")]),
  tok("كَقَامَ", "qama", "verb", [K, "huruf-jarr", "hollow-verbs", "fail"], "الْكَافُ جَارَّةٌ، وَقَامَ زَيْدٌ جُمْلَةٌ مَحْكِيَّةٌ فِي مَحَلِّ جَرٍّ.", "«as “stood» — a quoted sentence.", "«“kalktı» gibi — hikâye edilen cümle.", segments=[seg("كَ", "ka", "prep"), seg("قَامَ", "qama", "verb")]),
  tok("زَيْدٌ", "zayd", "propn", [K, "fail"], "فَاعِلٌ مَرْفُوعٌ.", "«Zayd”».", "«Zeyd”».", punct="."),
 ]})

# ----------- s14 — the five non-kalam compounds (COMMENTARY)
S.append({"id": "s14", "translation": {
 "en": "And the non-sentence compounds are five: the numeral, as «eleven»; the sound-compound, as «Sibawayh»; the annexation, as «Zayd's servant»; the qualifying, as «Zayd the learned»; and the fused, as «Baalbek»." + C_EN,
 "tr": "Kelâm olmayan mürekkebler beştir: aded terkibi «on bir» gibi; savtî terkib «Sîbeveyh» gibi; izâfî terkib «Zeyd'in kölesi» gibi; tavsîfî terkib «âlim Zeyd» gibi; mezcî terkib «Ba'lebek» gibi." + C_TR},
 "tokens": [
  tok("وَالْمُرَكَّبَاتُ", "murakkab", "noun", [K, "mubtada-khabar", "jam-muannath-salim", "ism-maful"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْمُرَكَّبَاتُ مُبْتَدَأٌ — جَمْعُ مُرَكَّبٍ بِالْأَلِفِ وَالتَّاءِ.", "«and the compounds» — a sound feminine plural.", "«mürekkebler» — cem-i müennes sâlim.", segments=[seg("وَ", "wa", "conj"), seg("الْمُرَكَّبَاتُ", "murakkab", "noun")]),
  tok("غَيْرُ", "ghayr", "noun", [K, "naat-sifa", "idafa-definiteness"], "صِفَةٌ مَرْفُوعَةٌ، مُضَافٌ.", "«non-».", "«… olmayan»."),
  tok("الْكَلَامِيَّةِ", "kalami", "noun", [K, "idafa-definiteness", "ism-mansub"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — نِسْبَةٌ إِلَى الْكَلَامِ.", "«sentence-» — a nisba.", "«kelâmî» — nisbe."),
  tok("خَمْسَةٌ", "khamsa", "noun", [K, "mubtada-khabar"], "خَبَرٌ مَرْفُوعٌ.", "«five».", "«beştir».", punct=":"),
  tok("التَّعْدَادِيُّ", "tadadi", "noun", [K, "mubtada-khabar", "ism-mansub"], "مُبْتَدَأٌ مَرْفُوعٌ — نِسْبَةٌ إِلَى التَّعْدَادِ؛ وَخَبَرُهُ الْجَارُّ بَعْدَهُ.", "«the numeral» — its khabar the kaf-phrase.", "«adedî» — haberi kâf'lı ibare."),
  tok("كَأَحَدَ", "ahada-ashar", "noun", [K, "huruf-jarr", "mubtada-khabar"], "الْكَافُ جَارَّةٌ، وَأَحَدَ عَشَرَ مَبْنِيٌّ عَلَى فَتْحِ الْجُزْأَيْنِ فِي مَحَلِّ جَرٍّ.", "«as “eleven”» — both halves built on fatha.", "«on bir» gibi — iki cüzü fetha üzere mebnî.", segments=[seg("كَ", "ka", "prep"), seg("أَحَدَ", "ahada-ashar", "noun")]),
  tok("عَشَرَ", "ahada-ashar", "noun", [K, "huruf-jarr"], "الْجُزْءُ الثَّانِي مِنَ الْمُرَكَّبِ الْعَدَدِيِّ.", "— the second half.", "— ikinci cüz.", punct="،"),
  tok("وَالصَّوْتِيُّ", "sawti", "noun", [K, "mubtada-khabar", "ism-mansub", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالصَّوْتِيُّ مُبْتَدَأٌ.", "«and the sound-compound».", "«savtî».", segments=[seg("وَ", "wa", "conj"), seg("الصَّوْتِيُّ", "sawti", "noun")]),
  tok("كَسِيبَوَيْهِ", "sibawayh", "propn", [K, "huruf-jarr", "mubtada-khabar"], "الْكَافُ جَارَّةٌ، وَسِيبَوَيْهِ مَبْنِيٌّ عَلَى الْكَسْرِ فِي مَحَلِّ جَرٍّ.", "«as “Sibawayh”» — built on kasra.", "«Sîbeveyh» gibi — kesre üzere mebnî.", segments=[seg("كَ", "ka", "prep"), seg("سِيبَوَيْهِ", "sibawayh", "propn")], punct="،"),
  tok("وَالْإِضَافِيُّ", "idafi", "noun", [K, "mubtada-khabar", "ism-mansub", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْإِضَافِيُّ مُبْتَدَأٌ.", "«and the annexation».", "«izâfî».", segments=[seg("وَ", "wa", "conj"), seg("الْإِضَافِيُّ", "idafi", "noun")]),
  tok("كَغُلَامِ", "ghulam", "noun", [K, "huruf-jarr", "idafa-definiteness"], "الْكَافُ جَارَّةٌ، وَغُلَامِ مَجْرُورٌ، مُضَافٌ.", "«as “the servant of».", "«kölesi» gibi.", segments=[seg("كَ", "ka", "prep"), seg("غُلَامِ", "ghulam", "noun")]),
  tok("زَيْدٍ", "zayd", "propn", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«Zayd”».", "«Zeyd'in».", punct="،"),
  tok("وَالتَّوْصِيفِيُّ", "tawsifi", "noun", [K, "mubtada-khabar", "ism-mansub", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالتَّوْصِيفِيُّ مُبْتَدَأٌ.", "«and the qualifying».", "«tavsîfî».", segments=[seg("وَ", "wa", "conj"), seg("التَّوْصِيفِيُّ", "tawsifi", "noun")]),
  tok("كَزَيْدٍ", "zayd", "propn", [K, "huruf-jarr", "naat-sifa"], "الْكَافُ جَارَّةٌ، وَزَيْدٍ مَجْرُورٌ.", "«as “Zayd».", "«Zeyd» gibi.", segments=[seg("كَ", "ka", "prep"), seg("زَيْدٍ", "zayd", "propn")]),
  tok("الْعَالِمِ", "alim-scholar", "noun", [K, "naat-sifa", "ism-fail"], "صِفَةٌ مَجْرُورَةٌ — اسْمُ فَاعِلِ عَلِمَ.", "«the learned”».", "«âlim»."  , punct="،"),
  tok("وَالْمَزْجِيُّ", "mazji", "noun", [K, "mubtada-khabar", "ism-mansub", "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَالْمَزْجِيُّ مُبْتَدَأٌ — نِسْبَةٌ إِلَى الْمَزْجِ.", "«and the fused».", "«mezcî».", segments=[seg("وَ", "wa", "conj"), seg("الْمَزْجِيُّ", "mazji", "noun")]),
  tok("كَبَعْلَبَكَّ", "baalabakk", "propn", [K, "huruf-jarr", "mamnu-min-sarf"], "الْكَافُ جَارَّةٌ، وَبَعْلَبَكَّ مَجْرُورٌ بِالْفَتْحَةِ — مَمْنُوعٌ مِنَ الصَّرْفِ لِلْعَلَمِيَّةِ وَالتَّرْكِيبِ.", "«as “Baalbek”» — a diptote: proper name plus composition.", "«Ba'lebek» gibi — alemiyet ve terkibden gayr-i munsarif.", segments=[seg("كَ", "ka", "prep"), seg("بَعْلَبَكَّ", "baalabakk", "propn")], punct="."),
 ]})

# ----------- s15-s17 — the three definitions
S.append({"id": "s15", "translation": {
 "en": "The noun is what points to a meaning in itself, not joined with one of the three tenses.",
 "tr": "İsim, üç zamandan birine yakın olmayarak kendi nefsinde bir manaya delâlet eden kelimedir."},
 "tokens": [
  *dalla_def("وَالِاسْمُ", "ism", "«the noun» — the mubtada.", "«isim» — mübtedâ."),
  tok("غَيْرِ", "ghayr", "noun", [K, "naat-sifa", "idafa-definiteness"], "صِفَةٌ لِمَعْنًى مَجْرُورَةٌ، مُضَافٌ.", "«not» — qualifying «meaning».", "«… olmayan» — mana'nın sıfatı."),
  tok("مُقْتَرِنٍ", "muqtarin", "noun", [K, "idafa-definiteness", "ism-fail", "form-viii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — اسْمُ فَاعِلِ اقْتَرَنَ.", "«joined» — the active participle of Form VIII.", "«yakın olan» — iktarane'nin ism-i fâili."),
  *bi_ahad(),
 ]})
S[-1]["tokens"][-1]["punctAfter"] = "."
S.append({"id": "s16", "translation": {
 "en": "The verb is what points to a meaning in itself, joined with one of the three tenses.",
 "tr": "Fiil, üç zamandan birine yakın olarak kendi nefsinde bir manaya delâlet eden kelimedir."},
 "tokens": [
  *dalla_def("وَالْفِعْلُ", "fil", "«the verb» — the mubtada.", "«fiil» — mübtedâ."),
  tok("مُقْتَرِنٍ", "muqtarin", "noun", [K, "naat-sifa", "ism-fail", "form-viii-verbs"], "صِفَةٌ لِمَعْنًى مَجْرُورَةٌ — اسْمُ فَاعِلٍ.", "«joined» — qualifying «meaning».", "«yakın olan» — sıfat."),
  *bi_ahad(),
 ]})
S[-1]["tokens"][-1]["punctAfter"] = "."
S.append({"id": "s17", "translation": {
 "en": "The particle is what points to a meaning in something else.",
 "tr": "Harf, başkasında bir manaya delâlet eden kelimedir."},
 "tokens": [
  *dalla_def("وَالْحَرْفُ", "harf", "«the particle» — the mubtada.", "«harf» — mübtedâ.")[:5],
  fi(),
  tok("غَيْرِهِ", "ghayr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — أَيْ: فِي غَيْرِ الْمَعْنَى.", "«in something else».", "«başkasında».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()], punct="."),
 ]})

# ----------- s18 — the ism's marks
S.append({"id": "s18", "translation": {
 "en": "Among the marks of the noun are the entry of the lam of definition, of the jarr and of the tanwin, and its being predicated-of and annexed.",
 "tr": "İsmin hâssalarından bazısı: tarif lâmının, cerrin ve tenvinin dâhil olması ve müsnedün ileyh ile muzâf olmasıdır."},
 "tokens": [
  tok("وَمِنْ", "min", "prep", [K, "huruf-jarr", "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَمِنْ حَرْفُ جَرٍّ — وَالْجَارُّ خَبَرٌ مُقَدَّمٌ.", "«and among» — the fronted khabar.", "«… -den» — mukaddem haber.", segments=[seg("وَ", "wa", "conj"), seg("مِنْ", "min", "prep")]),
  tok("خَوَاصِّ", "khassa-property", "noun", [K, "huruf-jarr", "idafa-definiteness", "jam-taksir", "mamnu-min-sarf"], "مَجْرُورٌ بِالْكَسْرَةِ لِلْإِضَافَةِ، مُضَافٌ — جَمْعُ خَاصَّةٍ عَلَى فَوَاعِلَ.", "«the marks of» — the plural of خَاصَّة, a diptote softened by annexation.", "«hâssalarından» — hâssa'nın cem'i, izâfetle kesre alır."),
  tok("الِاسْمِ", "ism", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ.", "«the noun».", "«ismin»."),
  tok("دُخُولُ", "dukhul", "noun", [K, "mubtada-khabar", "idafa-definiteness", "masdar"], "مُبْتَدَأٌ مُؤَخَّرٌ مَرْفُوعٌ، مُضَافٌ.", "«the entry of» — the delayed mubtada.", "«dâhil olması» — muahhar mübtedâ."),
  tok("لَامِ", "lam-letter", "noun", [K, "idafa-definiteness"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ، مُضَافٌ.", "«the lam of».", "«lâmının»."),
  tok("التَّعْرِيفِ", "tarif", "noun", [K, "idafa-definiteness", "masdar", "form-ii-verbs"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ — مَصْدَرُ عَرَّفَ.", "«definition».", "«tarif»."),
  tok("وَالْجَرِّ", "jarr", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالْجَرِّ مَعْطُوفٌ عَلَى لَامِ مَجْرُورٌ.", "«and of the jarr».", "«ve cerrin».", segments=[seg("وَ", "wa", "conj"), seg("الْجَرِّ", "jarr", "noun")]),
  tok("وَالتَّنْوِينِ", "tanwin", "noun", [K, "atf-nasaq", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَالتَّنْوِينِ مَعْطُوفٌ مَجْرُورٌ.", "«and of the tanwin».", "«ve tenvinin».", segments=[seg("وَ", "wa", "conj"), seg("التَّنْوِينِ", "tanwin", "noun")], punct="،"),
  tok("وَكَوْنُهُ", "kawn", "noun", [K, "atf-nasaq", "idafa-definiteness", "masdar"], "الْوَاوُ عَاطِفَةٌ، وَكَوْنُ مَعْطُوفٌ عَلَى دُخُولُ مَرْفُوعٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ — مَصْدَرُ كَانَ النَّاقِصَةِ.", "«and its being» — the masdar of the defective كَانَ.", "«ve olması» — nâkıs kâne'nin masdarı.", segments=[seg("وَ", "wa", "conj"), seg("كَوْنُ", "kawn", "noun"), pr3ms()]),
  tok("مُسْنَدًا", "musnad", "noun", [K, "kana-wa-akhawatuha", "ism-maful", "form-iv-verbs"], "خَبَرُ الْمَصْدَرِ كَوْن مَنْصُوبٌ — اسْمُ مَفْعُولِ أَسْنَدَ.", "«predicated» — the khabar of the masdar of كَانَ.", "«müsned» — kevn masdarının haberi."),
  tok("إِلَيْهِ", "ila", "prep", [K, "huruf-jarr"], "حَرْفُ جَرٍّ، وَالْهَاءُ مَجْرُورٌ — مُسْنَدٌ إِلَيْهِ.", "«-of» — the musnad ilayh.", "«ileyh».", segments=[seg("إِلَيْ", "ila", "prep"), pr3msi()]),
  tok("وَمُضَافًا", "mudaf", "noun", [K, "atf-nasaq", "ism-maful"], "الْوَاوُ عَاطِفَةٌ، وَمُضَافًا مَعْطُوفٌ عَلَى مُسْنَدًا مَنْصُوبٌ.", "«and annexed».", "«ve muzâf».", segments=[seg("وَ", "wa", "conj"), seg("مُضَافًا", "mudaf", "noun")], punct="."),
 ]})

# ----------- s19 — the khassa
S.append({"id": "s19", "translation": {
 "en": "And a mark is what is peculiar to a thing and is not found in anything else.",
 "tr": "Hâssa, bir şeye mahsus olup başkasında bulunmayan şeydir."},
 "tokens": [
  tok("وَالْخَاصَّةُ", "khassa-property", "noun", [K, "mubtada-khabar"], "الْوَاوُ لِلِاسْتِئْنَافِ، وَالْخَاصَّةُ مُبْتَدَأٌ.", "«and a mark».", "«hâssa».", segments=[seg("وَ", "wa", "conj"), seg("الْخَاصَّةُ", "khassa-property", "noun")]),
  ma_maws(K, "اسْمٌ مَوْصُولٌ خَبَرٌ.", "«what».", "«… şey»."),
  tok("يَخْتَصُّ", "ikhtassa", "verb", [K, "ism-mawsul", "form-viii-verbs", "doubled-verbs"], "مُضَارِعٌ مَرْفُوعٌ، وَالْفَاعِلُ مُسْتَتِرٌ — صِلَةٌ؛ افْتَعَلَ الْمُضَاعَفُ.", "«is peculiar» — doubled Form VIII.", "«mahsus olur» — muzâaf iftiâl."),
  tok("بِشَيْءٍ", "shay", "noun", [K, "huruf-jarr"], "الْبَاءُ حَرْفُ جَرٍّ، وَشَيْءٍ مَجْرُورٌ.", "«to a thing».", "«bir şeye».", segments=[seg("بِ", "bi", "prep"), seg("شَيْءٍ", "shay", "noun")]),
  tok("وَلَا", "la", "part", [K, "atf-nasaq"], "الْوَاوُ عَاطِفَةٌ، وَلَا نَافِيَةٌ.", "«and not».", "«ve … -maz».", segments=[seg("وَ", "wa", "conj"), seg("لَا", "la", "part")]),
  tok("يُوجَدُ", "wajada", "verb", [K, "naib-al-fail", "atf-nasaq"], "مُضَارِعٌ مَبْنِيٌّ لِلْمَجْهُولِ مَعْطُوفٌ، وَنَائِبُ الْفَاعِلِ مُسْتَتِرٌ — مِثَالٌ وَاوِيٌّ.", "«is found» — the passive of the assimilated وَجَدَ.", "«bulunur» — misâl vecede'nin meçhulü."),
  fi(),
  tok("غَيْرِهِ", "ghayr", "noun", [K, "huruf-jarr", "idafa-definiteness"], "مَجْرُورٌ، وَالْهَاءُ مُضَافٌ إِلَيْهِ.", "«in anything else».", "«başkasında».", segments=[seg("غَيْرِ", "ghayr", "noun"), pr3msi()], punct="."),
 ]})

# ---------------------------------------------------------------- glossary
def need(k, *a, **kw):
    return None if k in TG else G(k, *a, **kw)
CAND = {
 "iqtarana": need("iqtarana", "اقْتَرَنَ", "ق ر ن", "verb", "to be joined with, to go together with (Form VIII; اقْتَرَنَ يَقْتَرِنُ بِـ)", "yakın olmak, birlikte bulunmak (iftiâl; iktarane yaktarinu bi-)", 4),
 "talaffaza": need("talaffaza", "تَلَفَّظَ", "ل ف ظ", "verb", "to pronounce, to utter (Form V; تَلَفَّظَ يَتَلَفَّظُ بِـ)", "telaffuz etmek (tefa''ul; telaffaza yetelaffazu bi-)", 4),
 "muhmal": need("muhmal", "مُهْمَل", "ه م ل", "noun", "meaningless, not set down for any meaning (ism maf'ul of Form IV أَهْمَلَ) — like دَيْز", "mühmel: bir manaya konulmamış (ihmâl'in ism-i mef'ûlü) — deyz gibi", 5),
 "ahassa": need("ahassa", "أَحَسَّ", "ح س س", "verb", "to perceive, to sense (Form IV of a doubled root; أَحَسَّ يُحِسُّ بِـ)", "hissetmek, sezmek (muzâaf if'âl; ehasse yuhissu bi-)", 4),
 "afada": need("afada", "أَفَادَ", "ف ي د", "verb", "to give benefit, to convey (hollow Form IV; أَفَادَ يُفِيدُ — two objects)", "fayda vermek, ifade etmek (ecvef if'âl; efâde yufîdu — iki mef'ûl)", 4),
 "taatta": need("taatta", "تَأَتَّى", "أ ت ي", "verb", "to come about, to be feasible (naqis Form V; تَأَتَّى يَتَأَتَّى)", "hâsıl olmak, mümkün olmak (nâkıs tefa''ul; teettâ yeteettâ)", 5),
 "tanwin": need("tanwin", "تَنْوِين", "ن و ن", "noun", "the tanwin — the doubled vowel-sign that ends an indefinite noun (masdar of Form II نَوَّنَ)", "tenvin — nekre ismin sonundaki çift hareke (tef'îl masdarı)", 3),
 "jaraha": need("jaraha", "جَرَحَ", "ج ر ح", "verb", "to wound (جَرَحَ يَجْرَحُ)", "yaralamak (ceraha yecrahu)", 3),
 "jarh": need("jarh", "جَرْح", "ج ر ح", "noun", "a wound, wounding (masdar of جَرَحَ)", "yara, yaralama (ceraha'nın masdarı)", 3),
 "jiraha": need("jiraha", "جِرَاحَة", "ج ر ح", "noun", "a wound (pl. جِرَاحَات)", "yara (ç. جِرَاحَات)", 4, plural="جِرَاحَات"),
 "kalm-wound": need("kalm-wound", "كَلْم", "ك ل م", "noun", "a wound (the masdar كَلْم from which some derive «kalima» and «kalam»)", "yara (kelm — bazılarına göre kelime ve kelâm bundan müştaktır)", 5),
 "iltaama": need("iltaama", "الْتَأَمَ", "ل أ م", "verb", "to heal over, to close up (Form VIII; الْتَأَمَ يَلْتَئِمُ — softened to يَلْتَامُ in verse)", "kapanmak, iyileşmek (iftiâl; ilteeme yelteimu — şiirde yeltâmu)", 5),
 "iltiam": need("iltiam", "الْتِئَام", "ل أ م", "noun", "a healing-over (masdar of الْتَأَمَ; softened الْتِيَام in verse)", "iyileşme, kapanma (ilteeme masdarı; şiirde iltiyâm)", 5),
 "sinan": need("sinan", "سِنَان", "س ن ن", "noun", "a spear-head (pl. أَسِنَّة)", "süngü, mızrak ucu (ç. أَسِنَّة)", 4, plural="أَسِنَّة"),
 "rahb": need("rahb", "رَحْب", "ر ح ب", "noun", "wide, spacious (a sifa mushabbaha); رُحْب: width", "geniş (sıfat-ı müşebbehe); ruhb: genişlik", 4),
 "fada-open": need("fada-open", "فَضَاء", "ف ض و", "noun", "the open plain, open space (a mamdud noun)", "feza, açık alan (memdûd isim)", 4),
 "dayyiq": need("dayyiq", "ضَيِّق", "ض ي ق", "noun", "narrow (a sifa mushabbaha on فَيْعِل)", "dar (fey'il vezninde sıfat-ı müşebbehe)", 3),
 "samm": need("samm", "سَمّ", "س م م", "noun", "an eye, a hole — سَمُّ الْخِيَاطِ: the eye of the needle (pl. سُمُوم)", "delik — semmü'l-hıyât: iğne deliği (ç. سُمُوم)", 5, plural="سُمُوم"),
 "khiyat": need("khiyat", "خِيَاط", "خ ي ط", "noun", "a needle", "iğne", 4),
 "maydan": need("maydan", "مَيْدَان", "م ي د", "noun", "a field, an open arena (pl. مَيَادِين)", "meydan (ç. مَيَادِين)", 3, plural="مَيَادِين"),
 "mushtaqq": need("mushtaqq", "مُشْتَقّ", "ش ق ق", "noun", "derived (ism maf'ul of Form VIII اشْتَقَّ)", "müştak, türemiş (iştakka'nın ism-i mef'ûlü)", 4),
 "muqtarin": need("muqtarin", "مُقْتَرِن", "ق ر ن", "noun", "joined with, accompanied by (ism fa'il of اقْتَرَنَ)", "yakın olan, birlikte bulunan (iktarane'nin ism-i fâili)", 5),
 "musnad": need("musnad", "مُسْنَد", "س ن د", "noun", "predicated, the predicate; مُسْنَدٌ إِلَيْهِ: the subject predicated of (ism maf'ul of أَسْنَدَ)", "müsned, yüklem; müsnedün ileyh: özne (isnâd'ın ism-i mef'ûlü)", 4),
 "khassa-property": need("khassa-property", "خَاصَّة (الْخَاصِّيَّة)", "خ ص ص", "noun", "a peculiar mark, a distinguishing property (pl. خَوَاصّ)", "hâssa, ayırıcı özellik (ç. خَوَاصّ)", 5, plural="خَوَاصّ"),
 "lam-letter": need("lam-letter", "لَام", "ل و م", "noun", "the letter lam — لَامُ التَّعْرِيفِ: the lam of definition", "lâm harfi — lâmü't-ta'rîf: tarif lâmı", 3),
 "tarif": need("tarif", "تَعْرِيف", "ع ر ف", "noun", "definition, making definite (masdar of Form II عَرَّفَ)", "tarif, belirli kılma (ta'rîf; tef'îl masdarı)", 3),
 "wad-put": need("wad-put", "وَضْع", "و ض ع", "noun", "setting-down, the coining of a word for a meaning (masdar of وَضَعَ)", "vaz', bir lafzın bir mana için konulması (vadaa'nın masdarı)", 4),
 "kalami": need("kalami", "كَلَامِيّ", "ك ل م", "noun", "of speech, sentence- (a nisba to كَلَام)", "kelâmî, kelâma ait (nisbe)", 5),
 "khamsa": need("khamsa", "خَمْسَة", "خ م س", "noun", "five", "beş", 1),
 "tadadi": need("tadadi", "تَعْدَادِيّ", "ع د د", "noun", "numeral (compound) — a nisba to تَعْدَاد", "adedî, sayı terkibine ait (nisbe)", 5),
 "sawti": need("sawti", "صَوْتِيّ", "ص و ت", "noun", "of sound — the sound-compound (a nisba to صَوْت)", "savtî, sese ait (nisbe)", 5),
 "idafi": need("idafi", "إِضَافِيّ", "ض ي ف", "noun", "of annexation — the annexation compound (a nisba to إِضَافَة)", "izâfî, izafete ait (nisbe)", 4),
 "tawsifi": need("tawsifi", "تَوْصِيفِيّ", "و ص ف", "noun", "qualifying — the noun-adjective compound (a nisba to تَوْصِيف)", "tavsîfî, sıfat terkibine ait (nisbe)", 5),
 "mazji": need("mazji", "مَزْجِيّ", "م ز ج", "noun", "fused — the blended compound (a nisba to مَزْج)", "mezcî, karışım terkibine ait (nisbe)", 5),
 "ahada-ashar": need("ahada-ashar", "أَحَدَ عَشَرَ", "أ ح د", "noun", "eleven (both halves built on fatha)", "on bir (iki cüzü fetha üzere mebnî)", 2),
 "sibawayh": need("sibawayh", "سِيبَوَيْهِ", None, "propn", "Sibawayh — the great grammarian (d. c. 796); his name is a Persian sound-compound", "Sîbeveyh — büyük nahivci (ö. yak. 796); adı Farsça bir savtî terkib", 4),
 "baalabakk": need("baalabakk", "بَعْلَبَكّ", None, "propn", "Baalbek — the fused compound example (a diptote)", "Ba'lebek — mezcî terkib örneği (gayr-i munsarif)", 4),
 "alim-scholar": need("alim-scholar", "عَالِم", "ع ل م", "noun", "a learned man, a scholar (ism fa'il of عَلِمَ; pl. عُلَمَاء)", "âlim, bilgin (alime'nin ism-i fâili; ç. عُلَمَاء)", 2, plural="عُلَمَاء"),
}
_used = []
for _s in S:
    for _t in _s["tokens"]:
        _used.append(_t["lex"])
        for _g in (_t.get("segments") or []): _used.append(_g["lex"])
_MISSING = []
for k in sorted(set(_used)):
    if k in TG or k in CAND: continue
    try: CAND[k] = find_gloss(k)
    except KeyError: _MISSING.append(k)
if _MISSING: raise SystemExit("no package owns: " + ", ".join(_MISSING))
GLOSS_ADD = {k: v for k, v in CAND.items() if v}

# ---------------------------------------------------------------- paradigms
mo = json.loads((PKG / "morphology.json").read_text(encoding="utf-8"))
mo["verbs"].pop("iqtarana", None) if not (mo["verbs"].get("iqtarana", {}).get("mazi") or [""]*6)[5].endswith("نَّ") else None   # a stale fakk spelling is replaced
put_morph(mo, "iqtarana", _sg.idgham(_sg.derived(B8, W8, "َ", "اِقْتَرَن", "قْتَرِن", "اِقْتَرِن", "اِقْتِرَان", "مُقْتَرِن", None, None, None, "اقْتَرَنَ الشَّيْءُ بِالشَّيْءِ: صَاحَبَهُ — لَازِمٌ، لَا مَجْهُولَ لَهُ؛ نُونُهُ تُدْغَمُ فِي نُونِ النِّسْوَةِ وَنَا: اِقْتَرَنَّ، اِقْتَرَنَّا.")))
put_morph(mo, "talaffaza", _sg.derived(_sg.B5, _sg.W5, "َ", "تَلَفَّظ", "تَلَفَّظ", "تَلَفَّظ", "تَلَفُّظ", "مُتَلَفِّظ", "مُتَلَفَّظ (بِهِ)", None, None, "تَلَفَّظَ بِالْكَلِمَةِ: نَطَقَ بِهَا — يَتَعَدَّى بِالْبَاءِ."))
_ah = _sg.derived_hollow(_sg.B4 + " — مُضَاعَفٌ", _sg.W4, "ُ", "أَحَسّ", "أَحْسَس", "حِسّ", "حْسِس", "أَحِسّ", "أَحْسِس", "إِحْسَاس", "مُحِسّ", "مُحَسّ (بِهِ)", "أُحِسَّ", "يُحَسُّ", "أَحَسَّ بِالشَّيْءِ يُحِسُّ: شَعَرَ بِهِ — مُضَاعَفٌ مِنَ الْإِفْعَالِ، يُفَكُّ إِدْغَامُهُ عِنْدَ السُّكُونِ: أَحْسَسْتُ، لَمْ يُحْسِسْ أَوْ لَمْ يُحِسَّ.")
_ah["amr"][0] = "أَحِسَّ"; _ah["majzum"] = "يُحِسَّ"; _ah["majzum2"] = "تُحِسَّ"
put_morph(mo, "ahassa", _ah)
put_morph(mo, "afada", _sg.derived_hollow(_sg.B4, _sg.W4, "ُ", "أَفَاد", "أَفَد", "فِيد", "فِد", "أَفِيد", "أَفِد", "إِفَادَة", "مُفِيد", "مُفَاد", "أُفِيدَ", "يُفَادُ", "أَفَادَ يُفِيدُ: أَعْطَى الْفَائِدَةَ — أَجْوَفُ يَائِيٌّ مِنَ الْإِفْعَالِ؛ يَتَعَدَّى إِلَى مَفْعُولَيْنِ: أَفَادَ الْمُخَاطَبَ فَائِدَةً."))
put_morph(mo, "taatta", _sg.derived_naqis(_sg.B5, _sg.W5, "َ", "تَأَتَّ", "تَأَتّ", "a", "تَأَتّ", "تَأَتٍّ (التَّأَتِّي)", "مُتَأَتٍّ (الْمُتَأَتِّي)", None, None, None, "تَأَتَّى الْأَمْرُ يَتَأَتَّى: تَهَيَّأَ وَأَمْكَنَ — نَاقِصٌ يَائِيٌّ مِنَ التَّفَعُّلِ، مَهْمُوزُ الْفَاءِ؛ مَجْزُومُهُ يَتَأَتَّ."))
put_morph(mo, "jaraha", _sg.sound1("fataha", "جَرَح", "جْرَح", "اِجْرَح", "جَرْح", "جَارِح", "مَجْرُوح", "جُرِحَ", "يُجْرَحُ", "جَرَحَ يَجْرَحُ: أَصَابَ بِجُرْحٍ — مِنْ بَابِ فَتَحَ لِأَجْلِ حَرْفِ الْحَلْقِ."))
put_morph(mo, "iltaama", _sg.derived(B8, W8, "َ", "اِلْتَأَم", "لْتَئِم", "اِلْتَئِم", "اِلْتِئَام", "مُلْتَئِم", None, None, None, "الْتَأَمَ الْجُرْحُ يَلْتَئِمُ: انْضَمَّ وَبَرِئَ — مَهْمُوزُ الْعَيْنِ مِنَ الِافْتِعَالِ؛ الشَّاعِرُ يُسَهِّلُ هَمْزَتَهُ: يَلْتَامُ، الْتِيَامٌ."))
for _k, _v in GLOSS_ADD.items():
    if _v.get("pos") == "verb" and _k not in mo["verbs"]:
        _m = find_morph(_k)
        if _m: mo["verbs"][_k] = _m
(PKG / "morphology.json").write_text(json.dumps(mo, ensure_ascii=False, indent=1), encoding="utf-8")
print("kafiya ch1 gloss+morph ok", len(GLOSS_ADD))

# ---------------------------------------------------------------- note
NOTE = {
 "id": K,
 "title": {"ar": "الْكَلِمَةُ وَالْكَلَامُ", "en": "The word and the sentence: the Kafiya's opening definitions", "tr": "Kelime ve kelâm: Kâfiye'nin açılış tarifleri"},
 "level": 5, "group": "nahw",
 "classicalSources": ["الكافية لابن الحاجب — الكلمة لفظ وضع لمعنى مفرد، وهي اسم وفعل وحرف", "الفوائد الضيائية لملا جامي — شرح الكافية: أسئلة الديباجة والكلمة"],
 "question": {
  "en": ["Why does the Kafiya open with no basmala, hamdala or salawat on the page? Molla Jami's first question: the author saw his book as his own and did not want to rank it beside other scholars' books, so he humbled himself and left them out — and since one may bring them by heart and by tongue, leaving them off the page does not mean leaving them out. The obligatory openings are the basmala, the hamdala and the salawat; the permitted ones are the book's name, its discipline, the count of its chapters and the statement of its aim.",
         "What is a KALIMA? An utterance set down for a single meaning: لَفْظٌ وُضِعَ لِمَعْنًى مُفْرَدٍ. «Utterance» is the genus (so a gesture is out); «set down» excludes the meaningless دَيْز; «for a meaning» is the object of the setting-down, its lam a link, not the lam of cause; «single» excludes the compound. The notebook reads مُفْرَدٍ as qualifying the meaning (a meaning whose part points to no part of the utterance: إِنْسَان as the rational animal) and records the other reading that qualifies the utterance and raises it.",
         "Why exactly THREE kinds? The word either points to a meaning in itself or not: if not, it is a particle. If it does, it either joins one of the three tenses or not: if it joins, a verb; if not, a noun. The division is exhaustive, so the three definitions fall out of it: اسْم = مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ غَيْرِ مُقْتَرِنٍ بِأَحَدِ الْأَزْمِنَةِ الثَّلَاثَةِ; فِعْل = the same, مُقْتَرِنٍ; حَرْف = مَا دَلَّ عَلَى مَعْنًى فِي غَيْرِهِ.",
         "What is KALAM? What comprises two words by ISNAD — and isnad is the relating of one word to the other so that the hearer gets a complete benefit on which silence is sound. So kalam needs two nouns (زَيْدٌ قَائِمٌ) or a verb and a noun (قَامَ زَيْدٌ) — never a noun and a particle, never a verb and a particle. Even يَا زَيْدُ is kalam by ruling: the concealed أَدْعُو and its doer أَنَا are the two words. Kalam and jumla are synonyms for some (the Mufassal, the Lubab); for the Mughni's author kalam is narrower — its isnad must be intended for its own sake, so in زَيْدٌ أَبُوهُ قَائِمٌ the inner «his father is standing» is a jumla but not kalam.",
         "What compounds are NOT kalam? Five: the numeral (أَحَدَ عَشَرَ), the sound-compound (سِيبَوَيْهِ), the annexation (غُلَامُ زَيْدٍ), the qualifying (زَيْدٌ الْعَالِمُ) and the fused (بَعْلَبَكَّ). Each is مُرَكَّب but has no isnad on which silence is sound.",
         "What are the noun's MARKS? The entry of the lam of definition (الرَّجُل), of the jarr (بِزَيْدٍ), of the tanwin (رَجُلٌ), and its being predicated-of (زَيْدٌ قَائِمٌ) and annexed (غُلَامُ زَيْدٍ). A khassa is what belongs to a thing and is found in nothing else — so any word that takes one of these is a noun, and the engine uses the same five tests when it decides a row's class.",
         "What does the engine read? The DabtEngine classes every row as ism / fiʿl / ḥarf by exactly the Kafiya's marks (the lam, the jarr, the tanwin, the musnad-ilayh seat, the annexation) and the verb's tense-marks, and the QawaidEngine audits the definitional sentences of this chapter as a mubtada + relative-khabar frame (X مَا دَلَّ…), the passive of وُضِعَ with its استتار, the fronted khabar of مِنْ خَوَاصِّ الِاسْمِ, and the quoted sentence after the kaf (كَزَيْدٌ قَائِمٌ keeps its damma)."],
  "tr": ["Kâfiye sayfada niçin besmele, hamdele ve salvele ile açılmaz? Molla Câmî'nin ilk sorusu: müellif kitabını kendi kitabı sayıp diğer âlimlerin kitapları gibi görmedi, nefsini kırmak için yazmadı — kalben ve lisanen getirmek câiz olduğundan sayfadan düşmesi mutlak terk sayılmaz. Vâcib olanlar besmele, hamdele, salvele; câiz olanlar kitabın adı, fenni, fasıllarının sayısı ve maksadının beyanı.",
         "KELİME nedir? Müfred bir mana için konulmuş lafız: لَفْظٌ وُضِعَ لِمَعْنًى مُفْرَدٍ. «Lafız» cinstir (işaret dışarıda kalır); «konulmuş» mühmel دَيْز'i çıkarır; «bir mana için» vaz'ın mef'ûlüdür, lâmı ta'lîl değil sıla; «müfred» mürekkebi çıkarır. Defter müfred'i mananın sıfatı okur (cüz'ü lafzın cüz'üne delâlet etmeyen mana: hayvân-ı nâtık olan إِنْسَان) ve lafzın sıfatı okuyup ref' eden öbür kıraati de kaydeder.",
         "Niçin tam ÜÇ kısım? Kelime ya kendi nefsinde bir manaya delâlet eder ya etmez: etmezse harf. Ederse ya üç zamandan birine yakın olur ya olmaz: olursa fiil, olmazsa isim. Taksim tamdır, üç tarif ondan çıkar: اسْم = مَا دَلَّ عَلَى مَعْنًى فِي نَفْسِهِ غَيْرِ مُقْتَرِنٍ بِأَحَدِ الْأَزْمِنَةِ الثَّلَاثَةِ; فِعْل = aynı, مُقْتَرِنٍ; حَرْف = مَا دَلَّ عَلَى مَعْنًى فِي غَيْرِهِ.",
         "KELÂM nedir? İSNAD ile iki kelimeyi içine alan; isnad da bir kelimeyi diğerine, muhatab üzerine sükût sahih olan tam bir fayda alacak şekilde nispet etmektir. Bu yüzden kelâm ya iki isimden (زَيْدٌ قَائِمٌ) ya bir fiil ve bir isimden (قَامَ زَيْدٌ) olur — isim ve harften, fiil ve harften asla. يَا زَيْدُ bile hükmen kelâmdır: mukadder أَدْعُو ile fâili أَنَا iki kelimedir. Kelâm ve cümle bazılarına göre (Mufassal, Lübâb) müterâdif; Muğnî sahibine göre kelâm daha hususîdir — isnadı bizzat maksud olmalı; زَيْدٌ أَبُوهُ قَائِمٌ'de içteki «babası ayakta» cümledir, kelâm değildir.",
         "Kelâm OLMAYAN mürekkebler hangileri? Beş: aded terkibi (أَحَدَ عَشَرَ), savtî (سِيبَوَيْهِ), izâfî (غُلَامُ زَيْدٍ), tavsîfî (زَيْدٌ الْعَالِمُ), mezcî (بَعْلَبَكَّ). Her biri mürekkebdir ama üzerine sükût sahih olan bir isnad taşımaz.",
         "İsmin HÂSSALARI nelerdir? Tarif lâmının (الرَّجُل), cerrin (بِزَيْدٍ), tenvinin (رَجُلٌ) dâhil olması; müsnedün ileyh (زَيْدٌ قَائِمٌ) ve muzâf (غُلَامُ زَيْدٍ) olması. Hâssa bir şeye mahsus olup başkasında bulunmayandır — bunlardan birini alan her kelime isimdir; motor bir satırın sınıfına karar verirken aynı beş testi kullanır.",
         "Motor neyi okur? DabtEngine her satırı tam Kâfiye'nin hâssalarıyla (lâm, cer, tenvin, müsnedün ileyh yeri, izâfet) ve fiilin zaman alâmetleriyle isim / fiil / harf diye sınıflar; QawaidEngine bu bâbın tarif cümlelerini mübtedâ + mevsûl-haber çerçevesi (X مَا دَلَّ…), وُضِعَ'nın istitârlı meçhulü, مِنْ خَوَاصِّ الِاسْمِ'in mukaddem haberi ve kâf'tan sonraki hikâye edilen cümle (كَزَيْدٌ قَائِمٌ dammesini korur) olarak denetler."]},
 "plain": {
  "en": "A word is an utterance coined for one meaning; it is a noun, a verb or a particle. A sentence needs two words joined by predication that lets the hearer fall silent, satisfied: two nouns or a verb and a noun.",
  "tr": "Kelime bir mana için konulmuş lafızdır; isim, fiil ya da harftir. Kelâm, muhatabı susturacak bir isnadla bağlanmış iki kelime ister: iki isim ya da bir fiil ve bir isim."},
 "explanation": {
  "en": "الْكَلِمَةُ لَفْظٌ وُضِعَ لِمَعْنًى مُفْرَدٍ، وَهِيَ اسْمٌ وَفِعْلٌ وَحَرْفٌ. Ibn al-Hajib's Kafiya opens where every Arabic grammar opens, but with a logician's economy: one definition of the word, one exhaustive division into three, then the three definitions read off the division. The notebook then supplies the terms the definition leans on — LAFZ (what a human pronounces, really or by ruling, meaningful or not, single or compound), WADʿ (the assigning of one thing to another so that the first, uttered or perceived, brings the second to mind — as the word «pen» is assigned to the writing tool) and MAʿNA (what is intended by a thing). KALAM is what comprises two words by ISNAD, and isnad is defined by its fruit: a complete benefit on which silence is sound. Hence the two-word minimum (زَيْدٌ قَائِمٌ, قَامَ زَيْدٌ), the five compounds that are not kalam, and the noun's five marks. The two bayts of ʿAli are cited for the folk etymology of kalima from كَلْم «wound»: the wounds of the spear heal, the wounds of the tongue do not.",
  "tr": "الْكَلِمَةُ لَفْظٌ وُضِعَ لِمَعْنًى مُفْرَدٍ، وَهِيَ اسْمٌ وَفِعْلٌ وَحَرْفٌ. İbnü'l-Hâcib'in Kâfiye'si her Arapça gramerin başladığı yerden başlar, ama bir mantıkçının tutumluluğuyla: kelimenin tek tarifi, üçe tam bir taksim, sonra taksimden okunan üç tarif. Defter tarifin dayandığı terimleri verir — LAFIZ (insanın hakikaten ya da hükmen telaffuz ettiği; mühmel ya da mevzû, müfred ya da mürekkeb), VAZ' (birinci şey söylendiğinde ya da hissedildiğinde ikinciyi akla getirecek şekilde bir şeyi bir şeye tahsis — «kalem» lafzının yazı aletine tahsisi gibi) ve MANA (bir şeyle kastolunan). KELÂM isnad ile iki kelimeyi içine alandır; isnad da meyvesiyle tarif edilir: üzerine sükût sahih olan tam fayda. Buradan iki kelime asgarîsi (زَيْدٌ قَائِمٌ, قَامَ زَيْدٌ), kelâm olmayan beş terkib ve ismin beş hâssası çıkar. Hz. Ali'nin iki beyti kelimenin كَلْم «yara»dan türediği halk etimolojisi için anılır: süngü yarası iyileşir, dil yarası iyileşmez."},
 "examples": [
  {"ar": "الْكَلِمَةُ لَفْظٌ وُضِعَ لِمَعْنًى مُفْرَدٍ", "en": "The definition of the word — the Kafiya's first sentence.", "tr": "Kelimenin tarifi — Kâfiye'nin ilk cümlesi.", "sourceStory": "al-kafiya", "sentence": "s1"},
  {"ar": "وَالثَّانِي الْحَرْفُ … وَالثَّانِي الِاسْمُ، وَالْأَوَّلُ الْفِعْلُ", "en": "The exhaustive division into three.", "tr": "Üçe tam taksim.", "sourceStory": "al-kafiya", "sentence": "s4"},
  {"ar": "وَالْكَلَامُ مَا تَضَمَّنَ كَلِمَتَيْنِ بِالْإِسْنَادِ", "en": "The definition of kalam.", "tr": "Kelâmın tarifi.", "sourceStory": "al-kafiya", "sentence": "s11"},
  {"ar": "وَلَا يَتَأَتَّى ذَلِكَ إِلَّا فِي اسْمَيْنِ كَزَيْدٌ قَائِمٌ، أَوْ فِي فِعْلٍ وَاسْمٍ كَقَامَ زَيْدٌ", "en": "The two-word minimum, with the quoted sentences after the kaf.", "tr": "İki kelime asgarîsi, kâf'tan sonraki hikâye edilen cümlelerle.", "sourceStory": "al-kafiya", "sentence": "s13"},
  {"ar": "وَمِنْ خَوَاصِّ الِاسْمِ دُخُولُ لَامِ التَّعْرِيفِ وَالْجَرِّ وَالتَّنْوِينِ", "en": "The noun's marks — the fronted khabar.", "tr": "İsmin hâssaları — mukaddem haber.", "sourceStory": "al-kafiya", "sentence": "s18"}],
 "commonMistakes": [
  {"wrong": "«لِمَعْنًى'deki lâm ta'lîl lâmıdır: bir mana uğruna konulmuş»",
   "right": "«لِمَعْنًى مَفْعُولٌ بِهِ — lâm sıla, fiili mef'ûlüne bağlar»",
   "why": {"en": "The notebook's note: the lam is a link, not the lam of cause; the meaning is what the utterance is set down FOR as its object, not the reason it was coined.", "tr": "Defterin notu: lâm ta'lîl değil sıladır; mana lafzın kendisine konulduğu mef'ûldür, konulma sebebi değil."}},
  {"wrong": "«İki kelime yan yana gelince kelâm olur: غُلَامُ زَيْدٍ kelâmdır»",
   "right": "«مَا تَضَمَّنَ كَلِمَتَيْنِ بِالْإِسْنَادِ — isnad şart: غُلَامُ زَيْدٍ izâfî terkibdir, kelâm değil»",
   "why": {"en": "Two words make kalam only through an isnad that gives a complete benefit; the five compounds (numeral, sound, annexation, qualifying, fused) have none.", "tr": "İki kelime ancak tam fayda veren bir isnadla kelâm olur; beş terkib (adedî, savtî, izâfî, tavsîfî, mezcî) bunu taşımaz."}},
  {"wrong": "«كَزَيْدٌ قَائِمٌ'de Zeyd kâf'la mecrûr olmalı: كَزَيْدٍ»",
   "right": "«كَزَيْدٌ قَائِمٌ — cümle hikâye edilir, kâf'tan sonra dammesini korur»",
   "why": {"en": "After the kaf of exemplification a whole sentence is quoted as it stands; it sits in the place of jarr as a unit, so its mubtada keeps the damma.", "tr": "Temsil kâfından sonra bütün cümle olduğu gibi hikâye edilir; bir bütün olarak cer mahallindedir, mübtedâsı dammesini korur."}}],
 "relatedNotes": ["mubtada-khabar", "ism-mawsul", "anwa-al-jumal", "ism-fil", "mana-al-fil", "idafa-definiteness"]}

ADD_EN = (" Chapter 1 (notebook lines ~60-135): the kalima's definition (s1) and its three kinds by the two divisions (s2-s4), the lafz, wadʿ and maʿna "
          "definitions (s5-s7), the كَلْم etymology (s8, commentary) with ʿAli's two bayts (s9-s10), the kalam and the isnad (s11-s12), the two-word minimum "
          "with the quoted كَزَيْدٌ قَائِمٌ (s13), the five non-kalam compounds (s14, commentary), the three definitions (s15-s17), the noun's marks and the "
          "khassa (s18-s19). Commentary sentences are marked in the translations.")
ADD_TR = (" Birinci bâb (defter satırları ~60-135): kelimenin tarifi (s1) ve iki taksimle üç kısmı (s2-s4), lafız, vaz' ve mana tarifleri (s5-s7), "
          "كَلْم iştikakı (s8, şerh) ve Hz. Ali'nin iki beyti (s9-s10), kelâm ve isnad (s11-s12), hikâye edilen كَزَيْدٌ قَائِمٌ ile iki kelime asgarîsi (s13), "
          "kelâm olmayan beş terkib (s14, şerh), üç tarif (s15-s17), ismin hâssaları ve hâssa (s18-s19). Şerh cümleleri tercümelerde işaretlidir.")
write_out(1, S, TITLE, ADD_EN, ADD_TR, "60-135", GLOSS_ADD, notes=(NOTE,),
          related=(("mubtada-khabar", [K]), ("ism-mawsul", [K]), ("anwa-al-jumal", [K])))
report(1, S, GLOSS_ADD, (NOTE,))
