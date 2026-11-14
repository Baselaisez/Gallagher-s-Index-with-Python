"""The script layer, re-exported: it lives at ``qissa_core.orthography`` because the
memory store needs it too and must not import the grammar package to get it."""

from ...orthography import (DAMMA, FATHA, KASRA, SHADDA, SHORT, SUKUN, TANWIN, WEAK, Unit, fold, is_sakin,  # noqa: F401
                            is_short, is_weak, join, letters_only, norm_marks, parse, seat, vowel)
