# Reef Rush

A match-3 puzzle game with sea creatures, built as an installable progressive web app (PWA). It is one static HTML page with no build step and no dependencies.

- 15 levels on an 8×8 board, each with its own goals and a move limit, and one to three stars per level
- Special pieces:
  - **Wave**: match 4 in a row to clear that row or column
  - **Bubble Bomb**: match in an L or T shape to blast a 3×3 area
  - **Whirlpool**: match 5 in a row to clear every creature of one kind
  - Swap two specials together for a bigger blast
- Obstacles: kelp, nets, sunken crates and pearls that you drop to the seabed
- Boosters (Hammer, Free swap, Shuffle), idle hints, automatic reshuffle and one undo per level
- Synthesised sound effects and music, vibration on Android, and combo callouts
- Progress (unlocked levels, stars, best scores and boosters) is saved in the browser's `localStorage`

## Project layout

```
index.html             the whole game (HTML, CSS and JS)
manifest.webmanifest   app name, colours and icons for installing
sw.js                  service worker: offline play and caching
vercel.json            headers for the service worker and manifest
icons/                 app icon sources (SVG) and rendered PNGs
scripts/render-icons.py  re-renders the PNG icons from the SVGs
```

## Run locally

Service workers need `http://localhost` or HTTPS, so use a local server rather than opening the file directly:

```bash
npx serve .            # or: python3 -m http.server 8000
```

## Deploy on Vercel

1. Import this repository in Vercel (**Add New → Project**).
2. Leave **Framework Preset** as **Other**, with no build command, and leave the output directory empty (the repository root is served).
3. Deploy. Every push to `main` deploys to production.

Or from the terminal: `npx vercel --prod`.

## Install on your phone

- **Android (Chrome):** open the site, then tap **Install app** on the level map, or choose **Add to Home screen** from Chrome's menu.
- **iPhone/iPad (Safari):** open the site, tap **Share**, then **Add to Home Screen**. The **Install app** button on the level map shows these steps.

After the first visit the game works offline.

## Updating

When you change `index.html`, it is fetched from the network first, so players get the new version the next time they open the game online. If you change any of the icons or the manifest, bump `VERSION` in `sw.js` so the cached copies are replaced.
