// voice_espeak.mjs — v349 build-time helper for tools/voice_app.py: eSpeak NG (compiled to WebAssembly, npm `espeak-ng`)
// renders a batch of phoneme strings to WAV files. Nothing of it ships: the app carries only the audio it wrote.
//   node tools/voice_espeak.mjs JOBS.json       JOBS = [{ "out": "/abs/path.wav", "input": "[[…]] …" }, …]
// The module is found as ESPEAK_NG_MODULE (a path to dist/espeak-ng.js), else `espeak-ng` from NODE_PATH / node_modules
// (`npm i --no-save espeak-ng@1.0.2`). Licence: eSpeak NG is GPL-3.0-or-later — it is run here as a tool; its output
// (the audio) is not a covered work (GPLv3 §2), and the app never links or ships the engine.
import fs from "fs";
import path from "path";
import { createRequire } from "module";
import { pathToFileURL } from "url";

const require = createRequire(import.meta.url);
let modPath = process.env.ESPEAK_NG_MODULE;
if (!modPath) {
  const roots = (process.env.NODE_PATH || "").split(path.delimiter).filter(Boolean).concat([path.resolve("node_modules")]);
  for (const r of roots) { const p = path.join(r, "espeak-ng", "dist", "espeak-ng.js"); if (fs.existsSync(p)) { modPath = p; break; } }
  if (!modPath) { try { modPath = require.resolve("espeak-ng/dist/espeak-ng.js"); } catch (e) {} }
}
if (!modPath || !fs.existsSync(modPath)) { console.error("espeak-ng (npm) not found: npm i --no-save espeak-ng@1.0.2, or set ESPEAK_NG_MODULE"); process.exit(2); }
const ESpeakNg = (await import(pathToFileURL(modPath).href)).default;
const wasm = await WebAssembly.compile(fs.readFileSync(path.join(path.dirname(modPath), "espeak-ng.wasm")));
const jobs = JSON.parse(fs.readFileSync(process.argv[2], "utf8"));
let n = 0;
for (const j of jobs) {
  const e = await ESpeakNg({ arguments: ["-v", "ar", "-s", "150", "-w", "/o.wav", j.input],
    instantiateWasm: (imports, ok) => { WebAssembly.instantiate(wasm, imports).then(i => ok(i)); return {}; },
    print: () => {}, printErr: () => {} });
  fs.writeFileSync(j.out, e.FS.readFile("/o.wav"));
  n++;
}
console.log(JSON.stringify({ rendered: n, module: path.basename(path.dirname(path.dirname(modPath))) }));
