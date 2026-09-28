# -*- coding: utf-8 -*-
"""Train the BAB MODEL: predict the Form-I bab (nasara / daraba / fataha / samia / karuma / hasiba) of a
sound-or-weak triliteral root from its three radicals — learned from every Form-I paradigm the packages
store. A multinomial logistic regression over one-hot radical features (letter × position, the weak-letter
and hamza flags, the guttural-second/third flags that pull to fataha, the geminate flag), trained with
plain gradient descent in numpy-free Python; 5-fold cross-validation reports the held-out accuracy the
Learning lab shows. The model is EVIDENCE for the Sarf lab when the corpus is silent — never a rule.

  python3 tools/ml/train_bab.py            → content/models/bab_model.json  (weights + held-out report)
"""
import json, math, pathlib, random, re, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
DIA = re.compile("[ً-ْٰ]")
LETTERS = list("ءابتثجحخدذرزسشصضطظعغفقكلمنهويى")
GUTT = set("ءهعحغخ")
BABS = ["nasara", "daraba", "fataha", "samia", "karuma", "hasiba"]
WAZN_BAB = {"فَعَلَ يَفْعُلُ": "nasara", "فَعَلَ يَفْعِلُ": "daraba", "فَعَلَ يَفْعَلُ": "fataha", "فَعِلَ يَفْعَلُ": "samia", "فَعُلَ يَفْعُلُ": "karuma", "فَعِلَ يَفْعِلُ": "hasiba"}

def bare(s): return DIA.sub("", s or "").replace("ـ", "")

def load():
    rows = []
    for gp in sorted((ROOT / "content/samples").glob("*/glossary.json")):
        pkg = gp.parent
        mp = pkg / "morphology.json"
        if not mp.exists(): continue
        gl = json.loads(gp.read_text(encoding="utf-8"))["entries"]
        mo = json.loads(mp.read_text(encoding="utf-8"))["verbs"]
        for lex, e in mo.items():
            w = e.get("wazn", "")
            bab = next((b for k, b in WAZN_BAB.items() if w.startswith(k)), None)
            if not bab: continue
            g = gl.get(lex) or {}
            root = (g.get("root") or "").split()
            if len(root) != 3: continue
            rows.append((tuple(root), bab, lex, e.get("mazi", [""])[0]))
    # one vote per root: the same root in two packages is one datum
    seen = {}; out = []
    for r in rows:
        if r[0] in seen: continue
        seen[r[0]] = 1; out.append(r)
    return out

def feats(root):
    f = {"bias": 1.0}
    r1, r2, r3 = root
    for i, c in enumerate((r1, r2, r3)):
        f[f"L{i}:{c}"] = 1.0
    if r2 in GUTT: f["gutt2"] = 1.0
    if r3 in GUTT: f["gutt3"] = 1.0
    if r1 in "وي": f["weak1"] = 1.0
    if r2 in "وي": f["weak2"] = 1.0
    if r3 in "وي": f["weak3"] = 1.0
    if r1 == "ء": f["hamza1"] = 1.0
    if r3 == "ء": f["hamza3"] = 1.0
    if r2 == r3: f["gem"] = 1.0
    if r2 == "و": f["w2"] = 1.0
    if r2 == "ي": f["y2"] = 1.0
    if r3 == "و": f["w3"] = 1.0
    if r3 == "ي": f["y3"] = 1.0
    return f

def train(data, epochs=400, lr=0.15, l2=0.003):
    W = {b: {} for b in BABS}
    n = len(data)
    for ep in range(epochs):
        grad = {b: {} for b in BABS}
        for root, bab in data:
            f = feats(root)
            scores = {b: sum(W[b].get(k, 0.0) * v for k, v in f.items()) for b in BABS}
            m = max(scores.values()); ex = {b: math.exp(scores[b] - m) for b in BABS}; z = sum(ex.values())
            for b in BABS:
                p = ex[b] / z; y = 1.0 if b == bab else 0.0
                for k, v in f.items(): grad[b][k] = grad[b].get(k, 0.0) + (p - y) * v
        for b in BABS:
            for k, gv in grad[b].items():
                W[b][k] = W[b].get(k, 0.0) - lr * (gv / n + l2 * W[b].get(k, 0.0))
    return W

def predict(W, root):
    f = feats(root)
    scores = {b: sum(W[b].get(k, 0.0) * v for k, v in f.items()) for b in BABS}
    m = max(scores.values()); ex = {b: math.exp(scores[b] - m) for b in BABS}; z = sum(ex.values())
    return {b: ex[b] / z for b in BABS}

def main():
    data = load()
    random.seed(7); random.shuffle(data)
    pairs = [(r[0], r[1]) for r in data]
    K = 5; folds = [pairs[i::K] for i in range(K)]
    hit = 0; n = 0; conf = {b: {c: 0 for c in BABS} for b in BABS}; top2 = 0
    for k in range(K):
        test = folds[k]; tr = [p for j in range(K) if j != k for p in folds[j]]
        W = train(tr)
        for root, bab in test:
            pr = predict(W, root); best = max(pr, key=pr.get); n += 1
            if best == bab: hit += 1
            if bab in sorted(pr, key=pr.get, reverse=True)[:2]: top2 += 1
            conf[bab][best] += 1
    counts = {b: sum(1 for _, x in pairs if x == b) for b in BABS}
    majority = max(counts.values()) / len(pairs)
    W = train(pairs)
    model = {"babs": BABS, "features": sorted({k for b in BABS for k in W[b]}), "weights": {b: {k: round(v, 4) for k, v in W[b].items() if abs(v) > 1e-4} for b in BABS},
             "trainedOn": len(pairs), "counts": counts, "heldOut": {"folds": K, "n": n, "acc": round(100 * hit / n, 1), "top2": round(100 * top2 / n, 1), "majority": round(100 * majority, 1), "confusion": conf},
             "note": "multinomial logistic regression over radical one-hots; 5-fold held-out; evidence, not a rule"}
    (ROOT / "content/models/bab_model.json").write_text(json.dumps(model, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"bab model: {len(pairs)} roots, held-out acc {model['heldOut']['acc']}% (top-2 {model['heldOut']['top2']}%, majority {model['heldOut']['majority']}%)")
    print("counts", counts)
    for b in BABS: print(" ", b, conf[b])

if __name__ == "__main__": main()
