// SPDX-FileCopyrightText: 2024-2026 Sebastien Rousseau
// SPDX-License-Identifier: Apache-2.0 OR MIT
// Service Worker for Frontmatter Gen (https://frontmatter-gen.com)
const CACHE_NAME = 'fmg-docs-v0.0.1';
const OFFLINE_URL = '/offline/index.html';

const PRECACHE_ASSETS = [
  '/',
  '/index.html',
  '/offline/index.html',
  '/404/index.html',
  '/manifest.json'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME).then((cache) => cache.addAll(PRECACHE_ASSETS))
  );
  self.skipWaiting();
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys
          .filter((key) => key !== CACHE_NAME)
          .map((key) => caches.delete(key))
      )
    )
  );
  self.clients.claim();
});

self.addEventListener('fetch', (event) => {
  if (event.request.mode === 'navigate') {
    event.respondWith(
      fetch(event.request).catch(() => caches.match(OFFLINE_URL))
    );
    return;
  }

  event.respondWith(
    caches.match(event.request).then((cachedResponse) => {
      return (
        cachedResponse ||
        fetch(event.request).catch(() => {
          if (event.request.destination === 'document') {
            return caches.match(OFFLINE_URL);
          }
        })
      );
    })
  );
});
