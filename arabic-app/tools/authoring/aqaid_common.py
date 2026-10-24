# -*- coding: utf-8 -*-
"""The Aqa'id (Nasafi matn) authoring shim: talkhis_common with its package switched to content/samples/aqaid-ahl-al-sunna
(DRY_PKG/DRY_GR override, as for the Talkhis and Kafiya scripts)."""
import os, pathlib, sys
sys.path.insert(0, "/home/user/Gallagher-s-Index-with-Python/arabic-app/tools/authoring")
import talkhis_common as _tc
_tc.PKG = pathlib.Path(os.environ["DRY_PKG"]) if os.environ.get("DRY_PKG") else _tc.ROOT / "content/samples/aqaid-ahl-al-sunna"
if os.environ.get("DRY_GR"): _tc.GR = pathlib.Path(os.environ["DRY_GR"])
from talkhis_common import *
PKG = _tc.PKG
R_EN = " (The matn restored to the received wording where the supplied transcription is unvowelled.)"
R_TR = " (Metin, verilen harekesiz nüshada alınan rivayete göre harekelenmiştir.)"
def pr3ms(): return seg("هُ", "pron-3ms", "pron")
def pr3msi(): return seg("هِ", "pron-3ms", "pron")
def pr3fs(): return seg("هَا", "pron-3fs", "pron")
def pr3mp(): return seg("هُمْ", "pron-3mp", "pron")
def pr3mpi(): return seg("هِمْ", "pron-3mp", "pron")
def pr1p(): return seg("نَا", "pron-1p", "pron")
