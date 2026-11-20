# Google Play store listing: copy and paste

## App details
- **App name** (max 30): `HV Network Driver`
- **Default language:** English (Australia) – en-AU
- **App or game:** App · **Free or paid:** Free
- **Category:** Maps & Navigation
- **Tags:** Navigation, Transportation
- **Contact email:** [your email] · **Website:** [your GitHub Pages URL, optional]
- **Privacy policy URL:** `https://[your-github-username].github.io/[repo-name]/privacy.html`

## Short description (max 80)
```
Check you're on an approved heavy vehicle network, with route & break alerts.
```

## Full description (max 4000)
```
HV Network Driver is a companion app for Australian heavy vehicle drivers. It uses heavy vehicle network maps you download from the NHVR National Network Map to show, live, whether you're on an approved network for your vehicle.

LIVE "ON NETWORK" CHECK
• Load the network for your vehicle, such as B-double, road train, PBS or HML
• A green or red banner shows whether your GPS position is on a loaded network
• Names the road you're on, and beeps or vibrates if you leave the network
• Tap any spot on the map to check it before you drive

ROUTE ALERTS
• Import a route you planned in the NHVR Route Planner (KML or GPX)
• See an "Off route" warning if you're more than 150 m from your planned route

WORKS WITHOUT SIGNAL
• Imported networks and routes are saved on your phone, ready for black spots
• Large, glove-friendly buttons, a night map and a keep-screen-on option

VEHICLE PROFILE
• Check height, width and length against general access limits
• Get advice on which networks to download for your combination and mass scheme

BREAK TIMER (STANDARD HOURS, SOLO)
• Tap Start work and Start rest
• See time left in the 5½, 8, 11 and 24 hour windows, with an alert when a break is due
• A planning aid only. It does not replace your National Driver Work Diary or EWD.

PRIVATE BY DESIGN
• No account, no ads, no tracking
• Your location and files stay on your phone

HOW TO GET NETWORK DATA
1. Open the NHVR National Network Map (maps.nhvr.gov.au)
2. View by Networks, choose your state and network, tap the ? icon, then Download Network
3. Open HV Network Driver > Layers > Import file

IMPORTANT
HV Network Driver is an independent app. It is not made by, endorsed by or affiliated with the National Heavy Vehicle Regulator (NHVR) or any government agency. Network information comes from files you download yourself from the NHVR's public National Network Map: https://maps.nhvr.gov.au
The app only knows about the networks you load. Always follow road signs, gazetted notices, permits and the conditions that apply to your vehicle.
```

## Graphics (in the `store/` folder)
- App icon 512×512: `icon-512.png`
- Feature graphic 1024×500: `feature-graphic-1024x500.png`
- Phone screenshots (1080×1920): `screenshot-2-fatigue.png`, `screenshot-3-vehicle.png`, `screenshot-4-layers.png`
  → **Add 1–2 real screenshots of the map from your phone** (with a network loaded) and put them first. They sell the app.

## App content answers (Policy > App content)
- **Privacy policy:** URL above
- **Ads:** No, my app does not contain ads
- **App access:** All functionality is available without special access
- **Content rating questionnaire:** Category "All other app types" → answer No to everything. Expect a rating of Everyone / PEGI 3.
- **Target audience:** 18 and over
- **News app:** No
- **Government app:** No. The app isn't developed by or for a government (the disclaimer is in the description).
- **Financial features / Health:** None
- **Data safety** (see below)

## Data safety form
Google treats data as "collected" when it is sent off the device. Location in this app is processed only on the device, so the honest answers are:
- **Does your app collect or share any of the required user data types?** → **No**
- **Is all of the user data collected by your app encrypted in transit?** → Yes (all network requests use HTTPS)
- **Account deletion:** not applicable (no accounts)

Note: map tile requests go to the map provider (MapTiler or OpenStreetMap), which sees the device's IP address and the map area being viewed, not GPS coordinates. If you want to be extra cautious, you can declare **Location → Approximate location → Shared → App functionality** instead. Either way, keep the form consistent with `docs/privacy.html`.

## Location permission
The app only uses foreground location (no `ACCESS_BACKGROUND_LOCATION`), so you don't need the background-location declaration or video. The app shows an explanation screen before Android asks for permission.
