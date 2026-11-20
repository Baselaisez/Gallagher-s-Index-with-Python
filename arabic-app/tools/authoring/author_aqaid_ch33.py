# -*- coding: utf-8 -*-
"""aqaid-ahl-al-sunna — chapter 33: the vision of God — the hearing-proof that obliges it, and how He is seen: not by facing, by a ray
or by a distance. Source: matn line 35 (ورد الدليل السمعي … وبين الله تعالى); ورؤية الله تعالى جائزة and فيرى لا في مكان ولا على جهة
are chapter 6 s3-s4, which s2 of this chapter continues.  DRY_PKG=<copy> DRY_GR=<copy> python3 author_aqaid_ch33.py"""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from aq63 import *

TITLE = {"ar": "دَلِيلُ الرُّؤْيَةِ وَكَيْفِيَّتُهَا", "en": "The Proof of the Vision, and Its Manner", "tr": "Rü'yetin Delili ve Keyfiyeti"}
S = []
S.append({"id": "s1", "translation": {
 "en": "The hearing-proof has come, making obligatory the believers' seeing of God the Exalted in the abode of the Hereafter.",
 "tr": "Mü'minlerin âhiret yurdunda Allah Teâlâ'yı görmesini vâcip kılan sem'î delil vârid olmuştur."},
 "tokens": [
  MAZI("وَرَدَ", "warada", "«has come» — a report has arrived.", "«vârid olmuştur» — bir nas gelmiştir.", "وَالْفَاعِلُ «الدَّلِيلُ»", tags=["fail", "mithal-verbs"]),
  FAIL("الدَّلِيلُ", "dalil-proof", "«the proof».", "«delil»."),
  NAT("السَّمْعِيُّ", "samiyya", "«of hearing» — a proof from revelation (what is heard), as against a proof of reason.", "«sem'î» — nakle (işitilene) dayanan delil; aklî delilin karşıtı.", "الدَّلِيلُ", "raf", tags=["ism-mansub"]),
  FUSED("بِإِيجَابِ", "بِ", "ijab", "«making obligatory» — the masdar of Form IV, annexed to its object.", "«vâcip kılmakla» — if'âl masdarı, mef'ûlüne muzâf.", "«وَرَدَ»", mudaf=True, inner="إِيجَابِ", tags=["masdar", "form-iv-verbs", "imal-al-masdar"]),
  MUDI("رُؤْيَةِ", "ruya", "«the seeing of» — a masdar annexed to its doer and governing its object: رُؤْيَةُ الْمُؤْمِنِينَ اللهَ.", "«görmesi» — fâiline muzâf, mef'ûlünü nasbeden masdar: رُؤْيَةُ الْمُؤْمِنِينَ اللهَ.", mudaf=True, tags=["masdar", "imal-al-masdar"]),
  W("الْمُؤْمِنِينَ", "mumin", "noun", ["idafa-definiteness", "jam-mudhakkar-salim", "imal-al-masdar"], "مُضَافٌ إِلَيْهِ مَجْرُورٌ وَعَلَامَةُ جَرِّهِ الْيَاءُ لِأَنَّهُ جَمْعُ مُذَكَّرٍ سَالِمٌ، وَهُوَ فَاعِلُ الْمَصْدَرِ فِي الْمَعْنَى.", "«the believers» — a sound plural in jarr by its yāʾ; the masdar's doer.", "«mü'minlerin» — yâ ile mecrûr cem'-i müzekker sâlim; masdarın fâili."),
  W("اللهَ", "allah", "propn", ["maful-bihi", "imal-al-masdar"], "مَفْعُولٌ بِهِ لِلْمَصْدَرِ «رُؤْيَةِ» مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ.", "«God» — the masdar's object in naṣb.", "«Allah'ı» — masdarın mansûb mef'ûlü."),
  TAALA(),
  PREP("فِي", "fi", "«in».", "«-de»."),
  MAJ("دَارِ", "dar", "«the abode of».", "«yurdunda».", "فِي", "«رُؤْيَةِ»", mudaf=True),
  MUDI("الْآخِرَةِ", "akhira", "«the Hereafter».", "«âhiret».", punct=".")]})
S.append({"id": "s2", "translation": {
 "en": "— (in no direction) of facing, nor of a ray's contact, nor of a distance's being fixed between the seer and God the Exalted.",
 "tr": "— (hiçbir cihette değil:) ne karşı karşıya olma, ne bir ışının teması, ne de gören ile Allah Teâlâ arasında bir mesafenin sübûtu."},
 "tokens": [
  PREP("مِنْ", "min", "«of» — explaining the «direction» denied in chapter 6: not in a place, not in any direction …", "«… -den» — altıncı bâbda nefyedilen «cihet»i açıklar: mekânda değil, hiçbir cihette değil …", extra=" — بَيَانٌ لِلْجِهَةِ الْمَنْفِيَّةِ فِي قَوْلِهِ: وَلَا عَلَى جِهَةٍ (الْبَابُ السَّادِسُ)"),
  MAJ("مُقَابَلَةٍ", "muqabala", "«facing» — the seer opposite the seen.", "«mukabele» — görenin görülenin karşısında olması.", "مِنْ", "مَحْذُوفٍ صِفَةٌ لِـ«جِهَةٍ»", tags=["masdar", "form-iii-verbs"]),
  WALA(),
  W("اتِّصَالِ", "ittisal", "noun", ["atf-nasaq", "idafa-definiteness", "masdar", "form-viii-verbs"], "مَعْطُوفٌ عَلَى «مُقَابَلَةٍ» تَابِعٌ لَهُ فِي الْجَرِّ، وَهُوَ مُضَافٌ.", "«the contact of» — the masdar of Form VIII from وصل (the wāw becomes tāʾ and merges).", "«teması» — وصل'den iftiâl masdarı (vâv tâ olup idgam edilir)."),
  MUDI("شُعَاعٍ", "shuaa", "«a ray» — the ray the optics of the day said left the eye.", "«bir ışının» — dönemin optiğinin gözden çıktığını söylediği ışın."),
  WALA(),
  W("ثُبُوتِ", "thubut", "noun", ["atf-nasaq", "idafa-definiteness", "masdar"], "مَعْطُوفٌ عَلَى «مُقَابَلَةٍ» تَابِعٌ لَهُ فِي الْجَرِّ، وَهُوَ مُضَافٌ.", "«the being-fixed of».", "«sübûtu»."),
  MUDI("مَسَافَةٍ", "masafa", "«a distance».", "«bir mesafenin»."),
  W("بَيْنَ", "bayna", "noun", ["maful-fih", "idafa-definiteness"], "ظَرْفُ مَكَانٍ مَنْصُوبٌ وَعَلَامَةُ نَصْبِهِ الْفَتْحَةُ مُتَعَلِّقٌ بِـ«ثُبُوتِ»، وَهُوَ مُضَافٌ.", "«between» — a ẓarf hanging on the masdar ثُبُوتِ.", "«arasında» — masdar ثُبُوتِ'ye müteallık zarf."),
  MUDI("الرَّائِي", "rai-seer", "«the seer» — a definite manqūṣ: the kasra is estimated on the yāʾ.", "«gören» — marife mankûs: kesre yâ üzerinde takdirîdir.", tags=["ism-fail", "ism-maqsur-manqus"], extra=" الْمُقَدَّرَةُ عَلَى الْيَاءِ لِلثِّقَلِ"),
  W("وَبَيْنَ", "bayna", "noun", ["atf-nasaq", "maful-fih", "idafa-definiteness"], "الْوَاوُ عَاطِفَةٌ، وَ«بَيْنَ» مَعْطُوفٌ عَلَى «بَيْنَ» الْأُولَى مَنْصُوبٌ، وَهُوَ مُضَافٌ — وَتَكْرَارُ «بَيْنَ» جَائِزٌ مَعَ الظَّاهِرِ.", "«and between» — بَيْنَ is repeated, which Arabic allows before a full noun.", "«ve … arasında» — بَيْنَ tekrarlanır; zâhir isimle bu câizdir.", segments=[seg("وَ", "wa", "conj"), seg("بَيْنَ", "bayna", "noun")]),
  MUDI("اللهِ", "allah", "«God».", "«Allah».", pos="propn"),
  TAALA(punct=".")]})

CAND = {
 "dalil-proof": need("dalil-proof", "دَلِيل", "د ل ل", "noun", "a proof, an indication", "delil", 3, plural="دَلَائِل / أَدِلَّة"),
 "shuaa": need("shuaa", "شُعَاع", "ش ع ع", "noun", "a ray (of light)", "ışın, şua", 4),
 "rai-seer": need("rai-seer", "الرَّائِي", "ر أ ي", "noun", "the seer, the one who sees (ism fāʿil of رَأَى)", "gören (رَأَى'nın ism-i fâili)", 4),
}
ADD_EN = (" Chapter 33 (matn line 35): the hearing-proof obliging the believers' vision of God in the Hereafter, and the manner of the vision —"
          " no facing, no ray, no distance; s2 continues chapter 6's فَيُرَى لَا فِي مَكَانٍ وَلَا عَلَى جِهَةٍ.")
ADD_TR = (" Otuz üçüncü bâb (matn satırı 35): mü'minlerin âhirette Allah'ı görmesini vâcip kılan sem'î delil ve rü'yetin keyfiyeti —"
          " mukabele, ışın, mesafe yok; s2, altıncı bâbın فَيُرَى لَا فِي مَكَانٍ وَلَا عَلَى جِهَةٍ cümlesini sürdürür.")
finish(33, S, TITLE, CAND, ADD_EN, ADD_TR, "Chapter 33 (matn line 35)")
