"""Rule induction with a promotion gate — the learning layer's first citizen.

A Form I maṣdar is recited, not computed; but the books also state
TENDENCIES («فَعَلَ المتعدّي على فَعْلٍ غالبًا …»).  This module does what
the books did: it looks at every Form I verb the corpus recites, proposes
«if these features, then this shape» for every small set of features, and
PROMOTES a proposal only through a gate — enough verbs behind it, a high
enough share of them, and a real gain over the simpler proposal it refines.

What is promoted is written as data (``content/rules/masdar_tendencies.json``)
with its support and confidence, marked «induced»: a tendency a teacher may
show, never a law the builder may apply.  Nothing here is a black box: the
whole model is the list of promoted rules, read top to bottom.
"""

from __future__ import annotations

import itertools
from dataclasses import dataclass
from typing import Dict, FrozenSet, Iterable, List, Mapping, Optional, Sequence, Tuple

from ..core_grammar.sarf.analyzer import alternatives
from ..core_grammar.sarf.orthography import FATHA, KASRA, DAMMA, Unit, fold, join, parse, vowel
from ..core_grammar.sarf.root import Root
from ..memory_store.lexicon import Lexicon, VerbEntry

_VOWEL_NAME = {FATHA: "a", KASRA: "i", DAMMA: "u"}
Condition = FrozenSet[Tuple[str, str]]


def _fits(letter: str, radical: str) -> bool:
    return letter == radical or (radical in "وي" and letter in "وياىء") or (radical == "ء" and letter in "اء")


def shape_of(form: str, root: Root) -> Optional[str]:
    """The wazn of a recited form: its radicals written back as ف ع ل.

    قَوْل of ق و ل → فَعْل ;  دُخُول of د خ ل → فُعُول ;  بَقَاء of ب ق ي → فَعَال ;  None where a
    radical is missing (عِدَة of و ع د).  The first two radicals are the first letters that
    fit; the lām is the LAST letter that fits, the radical itself before a stand-in."""
    units = parse(fold(form))
    f, a, l = root.radicals
    i_f = next((i for i, u in enumerate(units) if _fits(u.c, f)), -1)
    i_a = next((i for i, u in enumerate(units) if i > i_f >= 0 and _fits(u.c, a)), -1)
    if i_a < 0:
        return None
    tail = [i for i, u in enumerate(units) if i > i_a and _fits(u.c, l)]
    exact = [i for i in tail if units[i].c == l]
    if not tail:
        return None
    i_l = (exact or tail)[-1]
    out = [Unit("فعل"[(i_f, i_a, i_l).index(i)] if i in (i_f, i_a, i_l) else u.c, u.m) for i, u in enumerate(units)]
    out[-1].m = "".join(ch for ch in out[-1].m if ch == "\u0651")   # the case ending is not the shape's
    if out[-1].c == "ل" and out[-1].m and len(out) >= 2 and vowel(out[-2].m) == DAMMA:
        out[-1:] = [Unit("و", ""), Unit("ل", "")]                     # عُلُوّ is فُعُول with its two wāws merged
    return join(out)


def features(verb: VerbEntry) -> Optional[Dict[str, str]]:
    """What the gate may condition on: the two recited vowels, transitivity, the root's class."""
    words = fold(verb.wazn or "").split()
    if len(words) < 2:
        return None
    mazi, mudari = parse(words[0]), parse(words[1])
    if len(mazi) < 3 or len(mudari) < 4:
        return None
    a, u = _VOWEL_NAME.get(vowel(mazi[1].m)), _VOWEL_NAME.get(vowel(mudari[2].m))
    if not a or not u:
        return None
    return {"mazi": a, "mudari": u, "transitive": "yes" if verb.ism_maful else "no",
            "class": Root.of(verb.root).classes()[0].split("-")[0]}


@dataclass(frozen=True)
class Example:
    lex: str
    feats: Mapping[str, str]
    shape: str


@dataclass(frozen=True)
class Tendency:
    """One promoted proposal."""

    condition: Condition
    shape: str
    support: int
    hits: int
    kind: str = "majority"

    @property
    def confidence(self) -> float:
        return self.hits / self.support

    def covers(self, feats: Mapping[str, str]) -> bool:
        return all(feats.get(k) == v for k, v in self.condition)

    def as_json(self) -> Dict[str, object]:
        return {"if": dict(sorted(self.condition)), "then": self.shape, "support": self.support,
                "confidence": round(self.confidence, 3), "kind": self.kind}


@dataclass(frozen=True)
class PromotionGate:
    """The questions every proposal must answer.

    A MAJORITY rule: enough verbs, most of them agreeing, and a real gain over the
    promoted rule it refines.  A PLURALITY rule (the commonest shape, though under
    half — «فَعِلَ اللازم على فَعَلٍ غالبًا») passes only when that shape is far
    commoner here than it is overall (its lift), and it is labelled as such."""

    min_support: int = 12
    min_confidence: float = 0.6
    min_gain: float = 0.08     # over the best promoted rule it refines
    min_plurality: float = 0.33
    min_lift: float = 2.5
    plurality_support: int = 24

    def kind(self, proposal: Tendency, base_rate: float) -> Optional[str]:
        if proposal.support >= self.min_support and proposal.confidence >= self.min_confidence:
            return "majority"
        if (proposal.support >= self.plurality_support and proposal.confidence >= self.min_plurality
                and base_rate > 0 and proposal.confidence / base_rate >= self.min_lift):
            return "plurality"
        return None

    def admits(self, proposal: Tendency, parents: Sequence[Tendency], base_rate: float = 1.0) -> bool:
        if self.kind(proposal, base_rate) is None:
            return False
        refined = [p for p in parents if p.condition < proposal.condition]
        return all(proposal.confidence >= p.confidence + self.min_gain or proposal.shape != p.shape for p in refined)


class MasdarInducer:
    """Proposes, gates and applies the tendencies of the Form I maṣdar."""

    FEATURES = ("mazi", "mudari", "transitive", "class")

    def __init__(self, gate: Optional[PromotionGate] = None) -> None:
        self.gate = gate or PromotionGate()
        self.rules: List[Tendency] = []
        self.default: str = ""

    @staticmethod
    def examples(lexicon: Lexicon) -> List[Example]:
        out: List[Example] = []
        for v in sorted(lexicon, key=lambda e: e.lex):
            if v.bab != 1 or not v.masdar:
                continue
            feats = features(v)
            forms = alternatives(v.masdar)
            shape = shape_of(forms[0], Root.of(v.root)) if forms else None
            if feats and shape:
                out.append(Example(v.lex, feats, shape))
        return out

    @staticmethod
    def _majority(shapes: Iterable[str]) -> Tuple[str, int, int]:
        count: Dict[str, int] = {}
        total = 0
        for s in shapes:
            count[s] = count.get(s, 0) + 1
            total += 1
        best = max(sorted(count), key=lambda s: count[s])
        return best, count[best], total

    def fit(self, examples: Sequence[Example]) -> "MasdarInducer":
        self.rules = []
        if not examples:
            return self
        self.default = self._majority(e.shape for e in examples)[0]
        base: Dict[str, float] = {}
        for e in examples:
            base[e.shape] = base.get(e.shape, 0.0) + 1.0 / len(examples)
        for size in (1, 2, 3):
            for names in itertools.combinations(self.FEATURES, size):
                groups: Dict[Condition, List[str]] = {}
                for e in examples:
                    groups.setdefault(frozenset((n, e.feats[n]) for n in names), []).append(e.shape)
                for cond in sorted(groups, key=lambda c: sorted(c)):
                    shape, hits, total = self._majority(groups[cond])
                    proposal = Tendency(cond, shape, total, hits)
                    kind = self.gate.kind(proposal, base[shape])
                    if kind and self.gate.admits(proposal, self.rules, base[shape]):
                        self.rules.append(Tendency(cond, shape, total, hits, kind))
        # the most specific, then the surest, is asked first
        self.rules.sort(key=lambda r: (-len(r.condition), -r.confidence, -r.support, sorted(r.condition)))
        return self

    def predict(self, feats: Mapping[str, str]) -> Tuple[str, Optional[Tendency]]:
        for r in self.rules:
            if r.covers(feats):
                return r.shape, r
        return self.default, None

    def cross_validate(self, examples: Sequence[Example], folds: int = 5) -> Dict[str, float]:
        """Held-out accuracy of the promoted list against always saying the commonest shape."""
        hit = base = 0
        for k in range(folds):
            train = [e for i, e in enumerate(examples) if i % folds != k]
            test = [e for i, e in enumerate(examples) if i % folds == k]
            model = MasdarInducer(self.gate).fit(train)
            hit += sum(1 for e in test if model.predict(e.feats)[0] == e.shape)
            base += sum(1 for e in test if model.default == e.shape)
        n = len(examples) or 1
        return {"accuracy": round(hit / n, 4), "baseline": round(base / n, 4)}

    def as_json(self, examples: Sequence[Example]) -> Dict[str, object]:
        cv = self.cross_validate(examples)
        return {"version": 1, "status": "induced",
                "note": "Tendencies of the Form I maṣdar, induced from the verbs the corpus recites and promoted "
                        "through a gate (support, confidence, gain over the rule refined). A teacher may show them; "
                        "the builder never applies them — a Form I maṣdar is recited.",
                "trained_on": len(examples),
                "gate": {"min_support": self.gate.min_support, "min_confidence": self.gate.min_confidence,
                         "min_gain": self.gate.min_gain, "min_plurality": self.gate.min_plurality,
                         "min_lift": self.gate.min_lift, "plurality_support": self.gate.plurality_support},
                "default": self.default, "cv_accuracy": cv["accuracy"], "cv_baseline": cv["baseline"],
                "rules": [r.as_json() for r in self.rules]}
