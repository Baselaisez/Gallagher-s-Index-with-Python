# -*- coding: utf-8 -*-
"""The Izhar authoring shim: talkhis_common with its package switched to content/samples/izhar-al-asrar
(DRY_PKG/DRY_GR still override, as for the Talkhis and Kafiya scripts). Everything else — tok/seg/G/find_gloss/
put_morph/write_out — is the shared machinery."""
import os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import talkhis_common as _tc
_tc.PKG = pathlib.Path(os.environ["DRY_PKG"]) if os.environ.get("DRY_PKG") else _tc.ROOT / "content/samples/izhar-al-asrar"
if os.environ.get("DRY_GR"): _tc.GR = pathlib.Path(os.environ["DRY_GR"])
from talkhis_common import *
PKG = _tc.PKG
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr3fs(): return seg("هَا", "pron-3fs", "pron")
def wa(form, lex, pos): return [seg("وَ", "wa", "conj"), seg(form, lex, pos)]
def fa(form, lex, pos): return [seg("فَ", "fa", "conj"), seg(form, lex, pos)]
