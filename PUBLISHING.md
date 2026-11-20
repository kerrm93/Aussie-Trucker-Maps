# Getting HV Network Driver onto Google Play

You don't need Android Studio for this. GitHub builds the Play upload file (`.aab`) for you in the cloud. Plan on about an hour of setup, then **at least 14 days** of closed testing if you have a new personal developer account.

---

## Step 0 – Choose your app ID (do this first, it's permanent)

The app ID is currently `au.hvnetworkdriver.app`. Once you publish, you can never change it. Use something you own, e.g. `au.com.smithtransport.hvdriver`.

Change it in **two** places:
1. `capacitor.config.json` → `"appId"`
2. `android/app/build.gradle` → the `applicationId "..."` line. Leave `namespace` as it is.

## Step 1 – Google Play developer account
1. Sign up at https://play.google.com/console (US$25 one-off fee, plus ID verification).
2. **Personal or organisation?**
   - *Personal*: quick to set up, but you must run a **closed test with at least 12 testers for 14 days in a row** before you can publish to everyone.
   - *Organisation*: needs an ABN-registered business and a D-U-N-S number (free, but takes a while). Organisation accounts skip the 12-tester rule.

## Step 2 – Map background key (needed before public release)
OpenStreetMap's own servers don't allow distributed apps to use their map images without permission. Use a map provider instead:
1. Create an account at https://cloud.maptiler.com and copy your API key.
2. Check the plan terms. Free plans have usage limits and may not cover commercial use.
3. Add the key as a GitHub secret called `MAPTILER_KEY` (Step 3). The build inserts it automatically.

Without a key, the app falls back to OpenStreetMap. That's fine for your own testing, but not for a public release.

## Step 3 – Put the project on GitHub
1. Create a free account at https://github.com and a **new repository** (private is fine).
2. Upload this whole folder. The easiest way is **GitHub Desktop** (https://desktop.github.com): *Add local repository* → *Publish*. The web uploader only takes 100 files at a time, and this project has more than that.
   - Do **not** upload the `upload-key-PRIVATE` folder.
3. In the repo: **Settings → Secrets and variables → Actions → New repository secret**. Add the 4 secrets listed in `upload-key-PRIVATE/GITHUB-SECRETS.txt`, plus `MAPTILER_KEY`.

## Step 4 – Build the app
1. In the repo, open the **Actions** tab → **Build Android app** → **Run workflow**.
2. After about 5–8 minutes, open the finished run and download the artifact zip under **Artifacts**. It contains:
   - `app-release.aab` → the file you upload to Google Play
   - `app-release.apk` → install this straight onto your own Android phone to try it (allow "Install unknown apps" when asked)
3. Test on the phone: import a real `.gpkg` from the National Network Map, drive a short loop and check the banner and off-route alert.

Every run gets a higher version number automatically, so you can upload each new build as an update.

## Step 5 – Privacy policy page
Google needs a public web address for your privacy policy.
1. Open `docs/privacy.html` and replace `[YOUR NAME OR BUSINESS]`, `[YOUR EMAIL]` and the map provider name.
2. Publish it:
   - **Public repo**: Settings → Pages → Deploy from branch → `main` / `/docs`. Your URL will be `https://USERNAME.github.io/REPO/privacy.html`
   - **Private repo**: drag the `docs` folder onto https://app.netlify.com/drop (free), or paste the text into a Google Sites page.

## Step 6 – Create the app in Play Console
1. **Create app** → name `HV Network Driver`, English (Australia), App, Free. Accept the declarations.
2. **Policy → App content**: fill everything in using `STORE_LISTING.md` (privacy policy, ads = no, target audience 18+, content rating, data safety, government app = no).
3. **Grow → Store presence → Main store listing**: paste the text from `STORE_LISTING.md` and upload the images from `store/`. Add 1–2 real map screenshots from your phone.
4. **Test and release → Closed testing** → create a track → **Create new release** → upload `app-release.aab`. Accept Play App Signing when asked (recommended).
5. **Testers**: add at least 12 Google accounts, e.g. a Google Group of drivers you know. Send them the opt-in link. They must install from Play and **stay opted in for 14 days**. Ask them to actually use it, because Google asks about this.
6. After 14 days: **Dashboard → Apply for production**. Answer the questions about your testing honestly and in detail.
7. Once approved: **Production → Create new release** → upload the latest `.aab` → choose **Australia** (or more countries) → roll out. The first review usually takes a few days.

## Updating the app later
1. Edit `web-src/app.html` (the whole app is in this one file).
2. Push to GitHub and run the workflow again (or push a tag like `v1.0.1`).
3. Upload the new `.aab` to Play.

To try changes in a browser first: `npm install`, then `python3 web-src/build.py`, then open `www/index.html` from any https or localhost web server.

## Using Android Studio instead (optional)
`npm install` → `npm run sync` → `npm run open`. Copy `upload.jks` into the `android/` folder and create `android/keystore.properties` with:
```
storeFile=../upload.jks
storePassword=...
keyAlias=upload
keyPassword=...
```
Then **Build → Generate Signed App Bundle**, or run `./gradlew bundleRelease` in `android/`.

## Checklist before you hit "publish"
- [ ] App ID changed to your own (Step 0)
- [ ] MapTiler key added (Step 2)
- [ ] Privacy policy placeholders filled in and page live (Step 5)
- [ ] Tested the APK on a real phone with real NHVR files
- [ ] Store listing keeps the "not affiliated with the NHVR" wording. Google rejects apps that look like official government apps.
- [ ] `upload-key-PRIVATE` backed up somewhere safe and NOT in GitHub
