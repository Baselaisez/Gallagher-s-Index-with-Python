// Learning curve for SarfTagger. The rules can generate unlimited data, so the
// only question worth asking is where more of it stops paying. Every point is
// scored the same way the shipped model is: held out BY ROOT.
const { chromium } = require('playwright-core');
const { pathToFileURL } = require('url'); const path = require('path');
(async () => {
  const b = await chromium.launch({ executablePath: process.env.CHROMIUM_PATH });
  const p = await b.newPage(); await p.goto(pathToFileURL(path.resolve('prototype/reader.html')).href);
  console.log(JSON.stringify(await p.evaluate(() => {
    const EXTRA = ["حكم","عبد","سجد","غفر","صبر","شكر","ذكر","حفظ","قرأ","بلغ",
                   "صدق","عدل","رزق","لبس","طرق","كسب","ملك","نفع","صنع","جمع",
                   "سال","عاد","زار","طاف","صام","نال","هدي","بني","سعي","نهي",
                   "وضع","وقع","وهب","يسر","شد","حل","ظن","عض","رد","صف"];
    const ALL = [...SarfTagger.ROOTS, ...EXTRA];
    const out = { sizes: [] };
    for (const n of [10, 20, 30, 45, 60, 70]) {
      const roots = ALL.slice(0, n);
      const save = SarfTagger.ROOTS;
      SarfTagger.ROOTS = roots; SarfTagger._rows = null; SarfTagger._model = null; SarfTagger._eval = null;
      const t0 = performance.now();
      let e = null;
      try { e = SarfTagger.evalUnseen(); } catch (err) { e = { err: String(err) }; }
      const ms = performance.now() - t0;
      out.sizes.push({ roots: n, examples: e.examples,
                       top1: Math.round(e.top1*1000)/10, top2: Math.round(e.top2*1000)/10,
                       form: Math.round(e.form*1000)/10, ms: Math.round(ms) });
      SarfTagger.ROOTS = save; SarfTagger._rows = null; SarfTagger._model = null; SarfTagger._eval = null;
    }
    return out;
  }), null, 1));
  await b.close();
})();
