# TranVanQuy777

## Pixel Aquarium Simulator 🐠

A cozy, interactive pixel-art aquarium driven by your lifetime GitHub contributions.

<!-- AQUARIUM:START -->
**Lifetime contributions:** 1767  
**Ecosystem level:** 5 - Thriving Ecosystem
<!-- AQUARIUM:END -->

![Aquarium preview](aquarium/aquarium-preview.gif)

**[▶ Play the Aquarium](https://supergigachadsupreme300.github.io/supergigachadsupreme300/)**

### Features
- Colorful tropical fish with natural swimming AI
- Feeding, earning coins, and a pixel-art shop
- Decorations: coral, rocks, treasure, shipwrecks, shells, seaweed
- Upgrades: capacity and auto-feeder
- Contribution-driven ecosystem growth (lifetime GitHub contributions)
- Persistent progress via LocalStorage
- Responsive for desktop and mobile

### How to run locally
Serve the repository root with any static server, then open `aquarium/index.html`.

```bash
python -m http.server 8000
# open http://localhost:8000/
```

### Deployment (GitHub Pages)
1. Push this repository to GitHub.
2. Go to **Settings → Pages**.
3. Source: **Deploy from a branch**, branch `main`, folder `/ (root)`.
4. Save. The game will be available at `https://<user>.github.io/<repo>/`.

### GitHub Secrets (for contribution sync)
Configure these in **Settings → Secrets and variables → Actions**:
- `AQUARIUM_GITHUB_TOKEN` — a PAT with `read:user` (and access to contributions).
- `AQUARIUM_GITHUB_USERNAME` — the GitHub username to track.

The `aquarium-sync` workflow runs daily and on manual dispatch, updating `aquarium/aquarium-state.json` and this README.
