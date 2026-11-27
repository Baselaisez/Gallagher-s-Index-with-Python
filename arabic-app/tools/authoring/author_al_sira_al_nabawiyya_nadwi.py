"""Author content/samples/al-sira-al-nabawiyya-nadwi — al-Nadwī's «السيرة النبوية» as ONE story in parts (v359-S), Level 5.

RECEIVED TEXT: Abū al-Ḥasan ʿAlī al-Ḥasanī al-Nadwī, al-Sīra al-Nabawiyya (Dār Ibn Kathīr, 12th ed. 2004; Shamela 9914). The whole
e-text: research/sources/al-sira-al-nabawiyya-nadwi-src.txt (tools/authoring/sira_src.py). Each chapter is a module
tools/authoring/sira_ch<N>.py (N = its ledger number in sira_common.CHAPTER_IDS: 1–100 reserved for the preface and Faṣl 1, 101 on
= the Prophet's life in the book's order). A later wave APPENDS a module and a ledger line; it never renumbers.
Run: python3 tools/authoring/author_al_sira_al_nabawiyya_nadwi.py
"""
import importlib, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from sira_common import *

CHAPS, METAS, NEW = [], [], {}
for n, heading, page in CHAPTER_IDS:
    m = importlib.import_module("sira_ch%d" % n)
    assert m.N_ == n, (m.__name__, m.N_)
    CHAPS.append((n, m.S)); METAS.append(dict(m.META, n=n, title=m.TITLE))
    for k, e in getattr(m, "NEW", {}).items():
        assert k not in NEW or NEW[k] == e, ("one key, one entry", k); NEW[k] = e
HOCA = [h for n, *_ in CHAPTER_IDS for h in getattr(importlib.import_module("sira_ch%d" % n), "HOCA", [])]
LEFT = [x for n, *_ in CHAPTER_IDS for x in getattr(importlib.import_module("sira_ch%d" % n), "LEFT", [])]
GH = {}
for n, *_ in CHAPTER_IDS:
    for k, v in getattr(importlib.import_module("sira_ch%d" % n), "GLOSS_HERE", {}).items():
        assert k not in GH or GH[k] == v, ("one key, one gloss in the package", k); GH[k] = v
VN = {}
for n, *_ in CHAPTER_IDS:
    VN.update(getattr(importlib.import_module("sira_ch%d" % n), "V", {}))
finish(CHAPS, METAS, NEW, manifest(METAS, hoca=HOCA, left=LEFT), GLOSS_HERE=GH, V_NEW=VN)
