const CACHE_NAME = 'ritmosbr-v1.0.3'; // FORCE UPDATE 1.0.3 // Mudei a versão para forçar atualização
const assets = [
  '/',
  '/index.html',
  '/manifest.json',
  '/sw.js',
  '/audio_assets.js',
  '/logotipo_ritmosbr.png'
];

self.addEventListener('install', event => {
  self.skipWaiting(); // Força a nova versão a assumir o controle na hora
  event.waitUntil(
    caches.open(CACHE_NAME).then(cache => cache.addAll(assets))
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => Promise.all(
      keys.filter(key => key !== CACHE_NAME).map(key => caches.delete(key))
    ))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => response || fetch(event.request))
  );
});
