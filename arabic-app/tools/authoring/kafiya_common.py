# -*- coding: utf-8 -*-
"""The Kafiya authoring shim: talkhis_common with its package switched to content/samples/al-kafiya
(DRY_PKG/DRY_GR still override, as for the Talkhis scripts). Everything else — tok/seg/G/find_gloss/
put_morph/write_out — is the shared machinery."""
import os, pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import talkhis_common as _tc
_tc.PKG = pathlib.Path(os.environ["DRY_PKG"]) if os.environ.get("DRY_PKG") else _tc.ROOT / "content/samples/al-kafiya"
if os.environ.get("DRY_GR"): _tc.GR = pathlib.Path(os.environ["DRY_GR"])
from talkhis_common import *
PKG = _tc.PKG
C_EN = " (Commentary: the notebook carries this sentence as the teacher's or Molla Jami's explanation, not as the matn.)"
C_TR = " (Şerh: defter bu cümleyi matn olarak değil, hocanın ya da Molla Câmî'nin açıklaması olarak taşır.)"
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr3fs(): return seg("هَا", "pron-3fs", "pron")
def wa(form, lex, pos): return [seg("وَ", "wa", "conj"), seg(form, lex, pos)]
