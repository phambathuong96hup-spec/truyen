// Service Worker for AI Chinese Web Novel Reader (PWA)
const CACHE_NAME = "novel-ai-cache-v9";
const STATIC_ASSETS = [
  "/manifest.json",
  "/static/icons/icon.svg"
];

self.addEventListener("install", (event) => {
  self.skipWaiting();
});

self.addEventListener("activate", (event) => {
  event.waitUntil(
    caches.keys().then((keys) => {
      return Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) {
            return caches.delete(key);
          }
        })
      );
    }).then(() => self.clients.claim())
  );
});

// Network-First strategy: Always fetch freshest files from server when online
self.addEventListener("fetch", (event) => {
  // Never cache API or stream endpoints
  if (event.request.url.includes("/api/")) {
    return;
  }

  // Always bypass cache for HTML, JS, CSS to ensure immediate updates
  const url = new URL(event.request.url);
  if (url.pathname === "/" || url.pathname.endsWith(".html") || url.pathname.endsWith(".js") || url.pathname.endsWith(".css")) {
    event.respondWith(
      fetch(event.request, { cache: "no-store" })
        .then((response) => {
          return response;
        })
        .catch(() => caches.match(event.request))
    );
    return;
  }

  event.respondWith(
    fetch(event.request)
      .then((networkResponse) => {
        if (networkResponse && networkResponse.status === 200 && event.request.method === "GET") {
          const responseToCache = networkResponse.clone();
          caches.open(CACHE_NAME).then((cache) => cache.put(event.request, responseToCache));
        }
        return networkResponse;
      })
      .catch(() => caches.match(event.request))
  );
});
