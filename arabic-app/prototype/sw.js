/**
 * Offline for Qissa.
 *
 * The whole app — shell, stories, grammar, glossaries — is one HTML file, so
 * "works offline" is a very short list: that file, the manifest, and the icons.
 * There is no API to fall back to and no runtime data to stale.
 *
 * Bump CACHE whenever reader.html is rebuilt. The old cache is deleted on
 * activate, so a stale build cannot outlive a deploy — which matters here more
 * than usual, because the content is baked into the file rather than fetched.
 */
const CACHE = 'qissa-v101';
const ASSETS = [
  './reader.html',
  './manifest.webmanifest',
  './icons/icon-192.png',
  './icons/icon-512.png',
  './icons/icon-maskable-512.png',
  './icons/apple-touch-icon.png',
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(CACHE)
      // addAll is atomic: one 404 and nothing is cached, which is the behaviour
      // we want — a half-cached app is worse than none.
      .then(c => c.addAll(ASSETS))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(keys.filter(k => k !== CACHE).map(k => caches.delete(k))))
      .then(() => self.clients.claim())
  );
});

// Network first, cache as the fallback. The reverse would be faster but would
// serve yesterday's stories after a deploy; a reader who is online should get
// the current text, and one who is not should still get the app.
self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    fetch(req)
      .then(res => {
        if (res && res.ok) {
          const copy = res.clone();
          caches.open(CACHE).then(c => c.put(req, copy));
        }
        return res;
      })
      .catch(() => caches.match(req).then(hit => hit || caches.match('./reader.html')))
  );
});
