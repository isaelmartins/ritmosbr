const CACHE_NAME = 'ritmosbr-v1';
const ASSETS = [
  './indexmestre.html',
  './audio_assets.js',
  './manifest.json',
  './ritmosbr_app_icon_1776021093801.png'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(ASSETS))
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => response || fetch(event.request))
  );
});
