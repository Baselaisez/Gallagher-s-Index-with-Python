// Leave-one-story-out cross-validation for IrabModel. The in-app score is a
// RESUBSTITUTION number — the model graded on the very corpus it memorised.
// This prints the held-out number instead, which is the only one that says
// anything about a sentence the app has not seen.
//
// Since v146 the validator lives INSIDE IrabModel (crossVal uses the same
// rows()/fit()/rank() as the shipped predict), so this harness is a thin
// runner: it cannot drift from the estimator, because it has no estimator
// of its own. Earlier versions carried a private naive-Bayes copy here and
// were one algorithm change away from grading the wrong model.
//   NODE_PATH=... CHROMIUM_PATH=... node tools/cv_eval.js
const { chromium } = require('playwright-core');
const { pathToFileURL } = require('url'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage();
  await p.goto(pathToFileURL(path.resolve('prototype/reader.html')).href);
  console.log(JSON.stringify(await p.evaluate(() => {
    const cv = IrabModel.crossVal();
    const acc = IrabModel.accuracy();
    return {
      folds: cv.folds, n: cv.n,
      heldout: { top1: Math.round(cv.top1 * 1000) / 10, top2: Math.round(cv.top2 * 1000) / 10 },
      resubstitution: { top1: Math.round(acc.top1 * 1000) / 10, top2: Math.round(acc.top2 * 1000) / 10 },
    };
  }), null, 1));
  await b.close();
})();
