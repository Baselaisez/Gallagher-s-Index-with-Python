# -*- coding: utf-8 -*-
"""Train the FIGURE PREDICTOR: which badiʿ figure(s) a sentence carries, from the surface features the reader's
FigurePredictor.feats() computes (tools/ml/figure_feats.js dumps them). One-vs-rest logistic regression per kind with L2,
plain gradient descent, numpy-free. Graded HELD-OUT BY CHAPTER (leave-one-chapter-out over every chapter that carries
authored frames): top-3 hit rate (the authored kind is among the model's three best), micro precision/recall at 0.5.
The model is a shortlist beside the engine's exact reading — evidence, never a rule.

  python3 tools/ml/train_figures.py [content/models/figure_feats.json]  → content/models/figure_model.json
"""
import json, math, pathlib, random, sys
ROOT = pathlib.Path(__file__).resolve().parent.parent.parent
SRC = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "content/models/figure_feats.json"

def train(rows, kinds, epochs=300, lr=0.2, l2=0.002):
    W = {k: {} for k in kinds}; n = len(rows)
    for ep in range(epochs):
        grad = {k: {} for k in kinds}
        for r in rows:
            f = r["feats"]; labs = set(r["labels"])
            for k in kinds:
                z = sum(W[k].get(a, 0.0) * v for a, v in f.items())
                pz = 1.0 / (1.0 + math.exp(-max(-30, min(30, z)))); y = 1.0 if k in labs else 0.0
                for a, v in f.items(): grad[k][a] = grad[k].get(a, 0.0) + (pz - y) * v
        for k in kinds:
            for a, g in grad[k].items(): W[k][a] = W[k].get(a, 0.0) - lr * (g / n + l2 * W[k].get(a, 0.0))
    return W

def predict(W, kinds, f):
    out = {}
    for k in kinds:
        z = sum(W[k].get(a, 0.0) * v for a, v in f.items()); out[k] = 1.0 / (1.0 + math.exp(-max(-30, min(30, z))))
    return out

def main():
    d = json.loads(SRC.read_text(encoding="utf-8")); kinds = d["kinds"]; rows = d["rows"]
    pos = [r for r in rows if r["labels"]]; neg = [r for r in rows if not r["labels"]]
    random.seed(11); random.shuffle(neg); neg = neg[: max(len(pos) * 3, 60)]
    data = pos + neg
    chapters = sorted({(r["story"], r["ch"]) for r in pos})
    hit3 = 0; n3 = 0; tp = fp = fn = 0
    for chk in chapters:
        test = [r for r in data if (r["story"], r["ch"]) == chk and r["labels"]]
        tr = [r for r in data if (r["story"], r["ch"]) != chk]
        W = train(tr, kinds)
        for r in test:
            pr = predict(W, kinds, r["feats"]); top3 = sorted(pr, key=pr.get, reverse=True)[:3]
            n3 += 1; hit3 += 1 if any(k in top3 for k in r["labels"]) else 0
            for k in kinds:
                y = k in r["labels"]; yh = pr[k] >= 0.5
                tp += 1 if (y and yh) else 0; fp += 1 if (yh and not y) else 0; fn += 1 if (y and not yh) else 0
    prec = tp / (tp + fp) if tp + fp else 0.0; rec = tp / (tp + fn) if tp + fn else 0.0
    f1 = 2 * prec * rec / (prec + rec) if prec + rec else 0.0
    W = train(data, kinds)
    counts = {k: sum(1 for r in pos if k in r["labels"]) for k in kinds}
    model = {"kinds": kinds, "features": sorted({a for k in kinds for a in W[k]}),
             "weights": {k: {a: round(v, 4) for a, v in W[k].items() if abs(v) > 1e-4} for k in kinds},
             "trainedOn": len(data), "positives": len(pos), "negatives": len(neg), "counts": counts,
             "heldOut": {"byChapter": len(chapters), "n": n3, "top3": round(100 * hit3 / n3, 1) if n3 else 0.0, "precision": round(100 * prec, 1), "recall": round(100 * rec, 1), "f1": round(100 * f1, 1)},
             "note": "one-vs-rest logistic regression over surface features; held out by chapter; a shortlist, never a rule"}
    (ROOT / "content/models/figure_model.json").write_text(json.dumps(model, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"figure model: {len(pos)} labelled sentences (+{len(neg)} without a figure), {len(chapters)} chapters held out in turn: top-3 {model['heldOut']['top3']}%, P {model['heldOut']['precision']}% R {model['heldOut']['recall']}% F1 {model['heldOut']['f1']}%")
    print("counts", {k: v for k, v in counts.items() if v})

if __name__ == "__main__": main()
