const CACHE = 'carnet-capvert-20261030-203239';
const PREFIX = 'carnet-capvert-';

const CORE = [
  './',
  './index.html',
];

// Photos des fiches : ajouter ici './nom-du-fichier.jpg' une fois deposees sur GitHub.
const IMAGES = [
  './airbnb.jpg',
  './angulo.jpg',
  './area-docas.jpg',
  './atlantic.jpg',
  './barracuda.jpg',
  './bikini-beach-club.jpg',
  './buddy-bar.jpg',
  './catamaran.jpg',
  './chez-pastis.jpg',
  './espargos.jpg',
  './gata-fish.jpg',
  './il-gobbo.jpg',
  './ile-de-sal.jpg',
  './marea.jpg',
  './ocean-cafe.jpg',
  './oeil-bleu.jpg',
  './ola-brasil.jpg',
  './palm-beach.jpg',
  './papaya.jpg',
  './pedra-de-lume.jpg',
  './plan-sal.jpg',
  './ponta-preta.jpg',
  './ponton-santa-maria.jpg',
  './shark-bay.jpg',
  './white-party.jpg',
];

self.addEventListener('message', e => {
  if (e.data === 'skipWaiting') self.skipWaiting();
});

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache =>
      cache.addAll(CORE).then(() =>
        Promise.all(IMAGES.map(url => cache.add(url).catch(() => null)))
      )
    )
  );
  self.skipWaiting();
});

// Ne purge que les anciennes versions DE CE CARNET : les autres carnets
// heberges sur le meme compte GitHub (meme domaine) gardent leur cache.
self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(keys =>
      Promise.all(keys.filter(k => k.indexOf(PREFIX) === 0 && k !== CACHE).map(k => caches.delete(k)))
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', e => {
  const req = e.request;
  if (req.method !== 'GET') return;

  const url = new URL(req.url);
  const isImage = /\.(jpg|jpeg|png|webp|gif|svg)$/i.test(url.pathname);

  if (isImage) {
    // Images : cache-first (elles ne changent pas, rapide + hors-ligne)
    e.respondWith(
      caches.match(req).then(cached =>
        cached || fetch(req).then(resp => {
          if (resp && resp.status === 200 && resp.type === 'basic') {
            const clone = resp.clone();
            caches.open(CACHE).then(cache => cache.put(req, clone));
          }
          return resp;
        }).catch(() => cached)
      )
    );
    return;
  }

  // HTML / code / reste : NETWORK-FIRST
  // => a chaque ouverture en ligne, on recupere la derniere version GitHub.
  // Hors-ligne : on sert la derniere version mise en cache.
  e.respondWith(
    fetch(req).then(resp => {
      if (resp && resp.status === 200 && resp.type === 'basic') {
        const clone = resp.clone();
        caches.open(CACHE).then(cache => cache.put(req, clone));
      }
      return resp;
    }).catch(() =>
      caches.match(req).then(cached => cached || caches.match('./index.html'))
    )
  );
});
