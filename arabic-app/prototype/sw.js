/**
 * Offline for Qissa.
 *
 * The whole app — shell, stories, grammar, glossaries — is one HTML file (or, in the hosted and Android builds, one page
 * plus a few data/*.js files), so "works offline" is a very short list: those files, the manifest, and the icons. There is
 * no API to fall back to and no runtime data to stale.
 *
 * Bump CACHE whenever reader.html is rebuilt (tools/release.py does). The old cache is deleted on activate, so a stale
 * build cannot outlive a deploy — which matters here more than usual, because the content is baked into the file.
 *
 * (wave 127) CACHE FIRST, refreshed in the background. The reader used to be network-first: every online visit
 * re-downloaded 37 MB before anything painted, and a slow connection meant a slow app. Now a cached copy answers at once
 * and the network copy, when it arrives, is stored for the NEXT launch; a new deploy is therefore one launch late, which
 * the CACHE bump turns into a clean install. A reader who has nothing cached still gets the network.
 */
const CACHE = 'qissa-v355';
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

// Cache first; the network refreshes the cache in the background for the next launch.
self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET' || new URL(req.url).origin !== self.location.origin) return;
  event.respondWith(
    caches.open(CACHE).then(c => c.match(req).then(hit => {
      const refresh = fetch(req).then(res => {
        if (res && res.ok) c.put(req, res.clone());
        return res;
      });
      if (hit) { refresh.catch(() => {}); return hit; }          // served from the cache; the refresh is for next time
      return refresh.catch(() => c.match('./reader.html'));      // nothing cached yet: the network, or the shell
    }))
  );
});
