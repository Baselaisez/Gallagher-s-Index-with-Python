# -*- coding: utf-8 -*-
"""The Qiṣaṣ al-Nabiyyīn PART TWO authoring shim: qisas_common's helpers with the package switched to
content/samples/qisas-al-nabiyyin-2, bootstrapped when it does not exist yet. The text is Nadwī's second part
(the ship of Nūḥ; the storm — Hūd and ʿĀd; the she-camel of Thamūd — Ṣāliḥ), transcribed page by page from the
Karachi scan (Majlis Nashriyāt-i Islām) the project owner supplied. RIGHTS: in copyright — a study build, as for Part One."""
import json, os, pathlib, sys
_HERE = pathlib.Path(__file__).resolve().parent
_REPO = pathlib.Path("/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
sys.path.insert(0, str(_HERE))
if not (_HERE / "talkhis_common.py").exists(): sys.path.insert(0, str(_REPO))   # a scratch copy of this shim still finds the shared modules in the repo
import talkhis_common as _tc
import qisas_common as _q1      # the shared helpers (and Part One's bootstrap, harmless)
_tc.PKG = pathlib.Path(os.environ["DRY_PKG"]) if os.environ.get("DRY_PKG") else _tc.ROOT / "content/samples/qisas-al-nabiyyin-2"
if os.environ.get("DRY_GR"): _tc.GR = pathlib.Path(os.environ["DRY_GR"])
from qisas_common import *
PKG = _tc.PKG

MANIFEST2 = {
 "id": "qisas-al-nabiyyin-2",
 "storyGroup": "qisas-al-nabiyyin",
 "title": {"ar": "قِصَصُ النَّبِيِّينَ — الْجُزْءُ الثَّانِي", "en": "Stories of the Prophets — Part Two", "tr": "Peygamber Kıssaları — İkinci Cüz"},
 "subtitle": {"ar": "سَفِينَةُ نُوحٍ، وَالْعَاصِفَةُ (هُودٌ وَعَادٌ)، وَنَاقَةُ ثَمُودَ (صَالِحٌ) — عَلَيْهِمُ السَّلَامُ — بِقَلَمِ أَبِي الْحَسَنِ النَّدْوِيِّ",
              "en": "The ship of Nūḥ; the storm (Hūd and ʿĀd); the she-camel of Thamūd (Ṣāliḥ) — the second part of Nadwī's stories for children",
              "tr": "Nûh'un gemisi; fırtına (Hûd ve Âd); Semûd'un devesi (Sâlih) — Nedvî'nin çocuklar için kıssalarının ikinci cüzü"},
 "level": 1, "levelName": "Newbie", "access": "premium", "published": "2026-10-07", "version": "0.1.0",
 "chapters": [],
 "attribution": {
  "ar": "قِصَصُ النَّبِيِّينَ لِلْأَطْفَالِ، الْجُزْءُ الثَّانِي، لِأَبِي الْحَسَنِ عَلِيٍّ الْحَسَنِيِّ النَّدْوِيِّ (ت 1420هـ/1999م). النَّصُّ مَنْقُولٌ صَفْحَةً صَفْحَةً مِنْ طَبْعَةِ كَرَاتْشِي (مَجْلِسُ نَشْرِيَّاتِ إِسْلَام)، بِضَبْطِهَا. الْحُقُوقُ مَحْفُوظَةٌ لِأَصْحَابِهَا؛ لَا يُنْشَرُ هٰذَا النَّصُّ إِلَّا بِإِذْنِهِمْ.",
  "en": "Qiṣaṣ al-Nabiyyīn li-l-aṭfāl, Part Two, by Abū al-Ḥasan ʿAlī al-Ḥasanī al-Nadwī (d. 1999). The Arabic is transcribed page by page, with its printed vowelling, from the Karachi edition (Majlis Nashriyāt-i Islām) the project owner supplied; the section numbers and titles are the book's; Qur'anic verses as the print quotes them. RIGHTS: the work is in copyright and this package is a study build — it must not be distributed without the rights holder's permission. The i'rab, the glossary and the translations are the app's own.",
  "tr": "Kısasü'n-Nebiyyîn li'l-etfâl, İkinci Cüz, Ebü'l-Hasen Ali el-Hasenî en-Nedvî (ö. 1999). Arapça metin, proje sahibinin verdiği Karaçi baskısından (Meclis-i Neşriyât-ı İslâm) sayfa sayfa, basılı harekesiyle aktarılmıştır; bölüm numaraları ve başlıkları kitabındır; âyetler baskının aktardığı gibidir. HAKLAR: eser telif altındadır ve bu paket bir çalışma sürümüdür — hak sahibinin izni olmadan dağıtılamaz. İ'râb, sözlük ve çeviriler uygulamanındır.",
  "reviewStatus": "pending-scholarly-review"
 }
}
def bootstrap2():
    (PKG / "chapters").mkdir(parents=True, exist_ok=True)
    if not (PKG / "manifest.json").exists(): (PKG / "manifest.json").write_text(json.dumps(MANIFEST2, ensure_ascii=False, indent=1), encoding="utf-8")
    if not (PKG / "glossary.json").exists(): (PKG / "glossary.json").write_text(json.dumps({"entries": {}}, ensure_ascii=False, indent=1), encoding="utf-8")
    if not (PKG / "morphology.json").exists(): (PKG / "morphology.json").write_text(json.dumps({"verbs": {}}, ensure_ascii=False, indent=1), encoding="utf-8")
def _reheader2():
    """Part One's bootstrap (imported above) may have written ITS manifest into a DRY_PKG first: keep the chapters and the version, take every other field from MANIFEST2."""
    m = json.loads((PKG / "manifest.json").read_text(encoding="utf-8"))
    if m.get("id") != MANIFEST2["id"]:
        keep = {"chapters": m.get("chapters", []), "version": m.get("version", MANIFEST2["version"])}
        m = dict(MANIFEST2); m.update(keep)
        (PKG / "manifest.json").write_text(json.dumps(m, ensure_ascii=False, indent=1), encoding="utf-8")
bootstrap2(); _reheader2()
def fi(punct=None): return tok("فِي", "fi", "prep", ["huruf-jarr"], "حَرْفُ جَرٍّ.", "«in».", "«-de».", punct=punct)
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr2mp(): return seg("كُمْ", "pron-2mp", "pron")
def pr3fs_(): return seg("هَا", "pron-3fs", "pron")
