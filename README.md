# HV Network Driver

An Android app for Australian truck drivers that works with the NHVR National Network Map and Route Planner data.

- **`PUBLISHING.md`** – step-by-step guide to getting it on Google Play
- **`STORE_LISTING.md`** – store text, data safety and content answers, ready to copy and paste
- `web-src/app.html` – the app itself (map, network check, vehicle, fatigue timer)
- `web-src/build.py` – packs the app into `www/index.html` (Leaflet, proj4 and sql.js are built in so it works offline)
- `android/` – native Android project (Capacitor 8, targets Android 16 / API 36)
- `.github/workflows/android.yml` – cloud build that produces a signed `.aab` and `.apk`
- `store/` – icon, feature graphic and screenshots for the Play listing
- `docs/privacy.html` – privacy policy page
- `assets/` – source images for the launcher icon and splash screen (regenerate with `npx @capacitor/assets generate --android`)

Not affiliated with the National Heavy Vehicle Regulator.
