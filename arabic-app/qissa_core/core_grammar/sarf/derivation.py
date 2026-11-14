"""BUILD: a root on a wazn — the origin form, each rule that fires, the surface."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional, Tuple

from .orthography import DAMMA, SHADDA, Unit, is_sakin, is_weak, join, parse, vowel
from .root import Root
from .rules import NOUN, SHARED, Context, PhonologicalRule
from .wazn import Wazn

_MASK = {"و": "", "ي": ""}
_UNMASK = {v: k for k, v in _MASK.items()}


def _unmask(text: str) -> str:
    return "".join(_UNMASK.get(ch, ch) for ch in text)


@dataclass(frozen=True)
class Step:
    """One firing of one rule."""

    rule: str
    before: str
    after: str


@dataclass(frozen=True)
class Derivation:
    """The whole road from origin to surface."""

    root: Root
    wazn: Wazn
    tpl: str                 # the template used (an override's, where one applied)
    asl: str                 # what the plain template gives
    out: str                 # the surface, hamzas unseated
    steps: Tuple[Step, ...] = field(default_factory=tuple)
    full: Optional[str] = None   # the unreduced form of a manqūṣ (دَاعِيٌ)

    @property
    def rule_ids(self) -> List[str]:
        return [s.rule for s in self.steps]


class Deriver:
    """Runs the two rule groups over a filled template, with a memo."""

    def __init__(self) -> None:
        self._memo: Dict[Tuple[str, str], Derivation] = {}

    @staticmethod
    def _shared_for(root: Root, wazn: Wazn) -> List[PhonologicalRule]:
        hold_ayn = wazn.sound_ayn or root.is_lafif
        rules: List[PhonologicalRule] = []
        for r in SHARED:
            if r.id == "naql" and hold_ayn:
                continue
            if r.id == "hamz-fail" and not (wazn.id == "fail-1" and not root.is_lafif):
                continue
            rules.append(r)
        return rules

    @staticmethod
    def _run_shared(cur: str, rules: List[PhonologicalRule], ctx: Context) -> Tuple[str, List[Step]]:
        """First rule that fires wins; repeat until none does (twelve rounds at most)."""
        u = parse(cur)
        ctx.pending = None
        steps: List[Step] = []
        for _ in range(12):
            fired: Optional[Step] = None
            for rule in rules:
                before = join(u)
                if rule.apply(u, ctx):
                    fired = Step(rule.id, before, join(u))
                    break
            if fired is None or fired.before == fired.after:
                break
            steps.append(fired)
        ctx.pending = None
        return join(u), steps

    def derive(self, root: Root, wazn: Wazn) -> Derivation:
        key = (root.key, wazn.id)
        hit = self._memo.get(key)
        if hit is not None:
            return hit
        tpl, why = wazn.template_for(root)
        asl = join(Wazn.fill(wazn.tpl, root))
        units = Wazn.fill(tpl, root)
        hold_ayn = root.is_lafif or wazn.sound_ayn
        # a weak letter the rules must not touch rides through under a mask: a doubled one,
        # a vowelled first radical, and the ʿayn of a lafīf or of a sound-ʿayn shape
        for x in units:
            if is_weak(x.c) and (SHADDA in x.m or (x.r == 0 and not is_sakin(x))
                                 or (hold_ayn and x.r == 1 and not is_sakin(x))):
                x.c = _MASK[x.c]
        cur = join(units)
        steps: List[Step] = []
        ctx = Context(root=root, wazn=wazn)
        if why:
            steps.append(Step("qiyas-" + why, asl, _unmask(cur)))

        def noun_rules(pre: bool) -> bool:
            nonlocal cur
            fired = False
            for rule in NOUN:
                if rule.pre != pre:
                    continue
                u = parse(cur)
                if not rule.apply(u, ctx):
                    continue
                after = join(u)
                if after == cur:
                    continue
                steps.append(Step(rule.id, _unmask(cur), _unmask(after)))
                cur, fired = after, True
            return fired

        if not why:
            noun_rules(True)
        # a silent yāʾ as FIRST radical after a ḍamma turns into wāw (مُيْقِن → مُوقِن)
        u = parse(cur)
        f = next((i for i, x in enumerate(Wazn.fill(tpl, root)) if x.r == 0), -1)
        if 0 < f < len(u) and u[f].c == "ي" and is_sakin(u[f]) and vowel(u[f - 1].m) == DAMMA:
            u[f].c = "و"
            after = join(u)
            steps.append(Step("qalb-ya-damma", _unmask(cur), _unmask(after)))
            cur = after
        shared = self._shared_for(root, wazn)
        for _ in range(4):
            out, fired = self._run_shared(cur, shared, ctx)
            moved = bool(fired)
            for s in fired:
                steps.append(Step(s.rule, _unmask(s.before), _unmask(s.after)))
            cur = out
            if noun_rules(False):
                moved = True
            if not moved:
                break
        cur = _unmask(cur)
        full = next((s.before for s in steps if s.rule == "hadhf-manqus"), None)
        result = Derivation(root=root, wazn=wazn, tpl=tpl, asl=asl, out=cur, steps=tuple(steps), full=full)
        self._memo[key] = result
        return result
