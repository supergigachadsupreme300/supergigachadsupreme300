export const SPECIES = [
  { id: 'turtle', name: 'Sea Turtle', price: 500, rarity: 'legendary', speed: 14, size: 1.6, color: '#2e7d32', accent: '#a5d6a7', schooling: false, desc: 'Gentle ocean wanderer', pattern: 'turtle' },
  { id: 'koi', name: 'Koi', price: 30, rarity: 'common', speed: 28, size: 1.0, color: '#ff8a65', accent: '#fff', schooling: false, desc: 'Calm pond fish', pattern: 'koi' },
  { id: 'clownfish', name: 'Clownfish', price: 40, rarity: 'common', speed: 34, size: 0.85, color: '#ff7043', accent: '#ffffff', schooling: true, desc: 'Orange with white bands', pattern: 'bands' },
  { id: 'bluetang', name: 'Blue Tang', price: 60, rarity: 'uncommon', speed: 36, size: 0.95, color: '#2979ff', accent: '#ffeb3b', schooling: true, desc: 'Bright blue reef fish', pattern: 'solid' },
  { id: 'goldfish', name: 'Goldfish', price: 25, rarity: 'common', speed: 26, size: 0.9, color: '#ffca28', accent: '#ff8f00', schooling: false, desc: 'Classic golden swimmer', pattern: 'solid' },
  { id: 'tropical', name: 'Tropical', price: 80, rarity: 'rare', speed: 40, size: 1.05, color: '#00e676', accent: '#ff4081', schooling: false, desc: 'Striped exotic', pattern: 'stripes' },
  { id: 'exotic', name: 'Exotic', price: 150, rarity: 'legendary', speed: 44, size: 1.2, color: '#e040fb', accent: '#00e5ff', schooling: false, desc: 'Rare magical fish', pattern: 'spots' },
  { id: 'angelfish', name: 'Angelfish', price: 90, rarity: 'rare', speed: 30, size: 1.15, color: '#f8bbd0', accent: '#c2185b', schooling: false, desc: 'Elegant tall fish', pattern: 'angel' },
  { id: 'butterflyfish', name: 'Butterflyfish', price: 70, rarity: 'uncommon', speed: 32, size: 0.9, color: '#ffeb3b', accent: '#1a237e', schooling: true, desc: 'Yellow with eye spot', pattern: 'butterfly' },
  { id: 'pufferfish', name: 'Pufferfish', price: 110, rarity: 'rare', speed: 20, size: 1.0, color: '#fff59d', accent: '#f48fb1', schooling: false, desc: 'Round spiky fish', pattern: 'puffer' },
  { id: 'lionfish', name: 'Lionfish', price: 130, rarity: 'rare', speed: 24, size: 1.1, color: '#e53935', accent: '#ffca28', schooling: false, desc: 'Striped with fan fins', pattern: 'lion' },
  { id: 'smallreef', name: 'Small Reef Fish', price: 15, rarity: 'common', speed: 42, size: 0.6, color: '#4dd0e1', accent: '#ffee58', schooling: true, desc: 'Tiny blue fish', pattern: 'solid' },
  { id: 'royalgramma', name: 'Royal Gramma', price: 85, rarity: 'rare', speed: 30, size: 0.9, color: '#7b1fa2', accent: '#ffca28', schooling: false, desc: 'Purple and yellow', pattern: 'solid' },
  { id: 'moorishidol', name: 'Moorish Idol', price: 120, rarity: 'rare', speed: 28, size: 1.0, color: '#ffffff', accent: '#ffc107', schooling: false, desc: 'Black, white and gold', pattern: 'solid' }
];

import { getAsset } from './assets.js';

export function speciesById(id) {
  return SPECIES.find(s => s.id === id);
}

export class Fish {
  constructor(speciesId, x, y) {
    const sp = speciesById(speciesId);
    this.species = sp;
    this.id = speciesId;
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * sp.speed;
    this.vy = (Math.random() - 0.5) * sp.speed * 0.6;
    this.angle = Math.atan2(this.vy, this.vx);
    this.targetAngle = this.angle;
    this.speed = sp.speed;
    this.size = sp.size;
    this.animPhase = Math.random() * Math.PI * 2;
    this.state = 'wander';
    this.wanderTimer = 0;
    this.wanderTarget = { x, y };
    this.eating = 0;
    this.origin = 'player';
    this.finPhase = Math.random() * Math.PI * 2;
  }

  draw(ctx, t) {
    const sp = this.species;
    // Sprite-based rendering (PNG assets)
    const assetKey = this.id === 'bluetang' ? 'bluetang' : this.id;
    const frames = (window.__ASSETS__ && window.__ASSETS__[assetKey]) ? window.__ASSETS__[assetKey].length : 0;
    // Use module-level ASSETS via dynamic import is not sync; instead read from global set by game.
    const img = (typeof getAsset === 'function') ? getAsset(assetKey, Math.floor(t * 4 + this.animPhase) % 2) : null;
    if (img) {
      const dir = this.vx >= 0 ? 1 : -1;
      const scale = 0.4;
      const w = img.width * scale;
      const h = img.height * scale;
      ctx.save();
      ctx.translate(Math.round(this.x), Math.round(this.y));
      if (dir < 0) ctx.scale(-1, 1);
      ctx.imageSmoothingEnabled = false;
      ctx.drawImage(img, -w / 2, -h / 2, w, h);
      ctx.restore();
      return;
    }
    const size = 12 * this.size; // base pixel size (fallback procedural)
    const dir = this.vx >= 0 ? 1 : -1;
    const wag = Math.sin(t * 9 + this.animPhase) * 0.4;
    const finWag = Math.sin(t * 6 + this.finPhase) * 0.25;

    // Turtle special-case (keep detailed)
    if (this.id === 'turtle') {
      this.drawTurtle(ctx, t, size, dir, wag);
      return;
    }

    // Pufferfish special-case
    if (this.id === 'pufferfish') {
      this.drawPuffer(ctx, t, size, dir, wag);
      return;
    }

    // Angelfish special-case (tall body)
    if (this.id === 'angelfish') {
      this.drawAngel(ctx, t, size, dir, wag);
      return;
    }

    ctx.save();
    ctx.translate(Math.round(this.x), Math.round(this.y));
    ctx.scale(dir, 1);

    // Tail (animated)
    const tailWag = wag * 6;
    ctx.fillStyle = sp.accent;
    ctx.beginPath();
    ctx.moveTo(-size * 0.85, 0);
    ctx.lineTo(-size * 1.55, -size * 0.55 + tailWag);
    ctx.lineTo(-size * 1.4, tailWag * 0.3);
    ctx.lineTo(-size * 1.55, size * 0.55 + tailWag);
    ctx.closePath();
    ctx.fill();
    // tail outline
    ctx.strokeStyle = 'rgba(0,0,0,0.35)';
    ctx.lineWidth = 1;
    ctx.stroke();

    // Body base
    const bodyW = size;
    const bodyH = size * 0.5;
    // shadow/depth gradient via layered ellipses
    ctx.fillStyle = shade(sp.color, -0.15);
    ctx.beginPath();
    ctx.ellipse(0, bodyH * 0.15, bodyW * 0.95, bodyH * 0.9, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = sp.color;
    ctx.beginPath();
    ctx.ellipse(0, 0, bodyW, bodyH, 0, 0, Math.PI * 2);
    ctx.fill();
    // highlight
    ctx.fillStyle = 'rgba(255,255,255,0.22)';
    ctx.beginPath();
    ctx.ellipse(-bodyW * 0.15, -bodyH * 0.25, bodyW * 0.55, bodyH * 0.3, -0.3, 0, Math.PI * 2);
    ctx.fill();

    // Dorsal fin
    ctx.fillStyle = sp.accent;
    ctx.beginPath();
    ctx.moveTo(-size * 0.3, -bodyH);
    ctx.lineTo(size * 0.05, -bodyH - size * 0.45 + finWag * 2);
    ctx.lineTo(size * 0.4, -bodyH);
    ctx.closePath();
    ctx.fill();
    ctx.strokeStyle = 'rgba(0,0,0,0.3)';
    ctx.stroke();

    // Pectoral fin
    ctx.fillStyle = shade(sp.accent, -0.1);
    ctx.beginPath();
    ctx.ellipse(size * 0.15, bodyH * 0.35, size * 0.22, bodyH * 0.25, 0.6 + finWag, 0, Math.PI * 2);
    ctx.fill();

    // Patterns
    this.drawPattern(ctx, sp, size, bodyW, bodyH, t);

    // Eye
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(size * 0.5, -size * 0.08, 3.2, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#1a1a1a';
    ctx.beginPath();
    ctx.arc(size * 0.55, -size * 0.08, 1.7, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(size * 0.6, -size * 0.15, 0.7, 0, Math.PI * 2);
    ctx.fill();

    // Mouth
    ctx.strokeStyle = 'rgba(0,0,0,0.5)';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(size * 0.88, 0.5, 1.6, -0.5, 0.5);
    ctx.stroke();

    // Scales texture
    ctx.fillStyle = 'rgba(0,0,0,0.08)';
    for (let sx = -bodyW * 0.6; sx < bodyW * 0.7; sx += 4) {
      for (let sy = -bodyH * 0.5; sy < bodyH * 0.5; sy += 3) {
        if (Math.hypot(sx, sy) < bodyW * 0.85) {
          ctx.fillRect(sx, sy, 1, 1);
        }
      }
    }

    if (this.eating > 0) {
      ctx.fillStyle = 'rgba(255,255,255,0.7)';
      ctx.beginPath();
      ctx.arc(size * 0.95, 0, 2 + (0.5 - this.eating) * 5, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.restore();
  }

  drawPattern(ctx, sp, size, bw, bh, t) {
    const p = sp.pattern;
    if (p === 'bands') {
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(-size * 0.35, -bh * 0.9, 3, bh * 1.8);
      ctx.fillRect(size * 0.15, -bh * 0.9, 3, bh * 1.8);
      ctx.fillStyle = sp.accent;
      ctx.fillRect(-size * 0.35, -bh * 0.9, 1, bh * 1.8);
    } else if (p === 'stripes') {
      ctx.fillStyle = sp.accent;
      for (let s = -1; s <= 1; s++) {
        ctx.fillRect(s * size * 0.3, -bh * 0.7, 2, bh * 1.4);
      }
    } else if (p === 'spots') {
      ctx.fillStyle = sp.accent;
      for (let s = 0; s < 5; s++) {
        ctx.beginPath();
        ctx.arc(-size * 0.3 + s * size * 0.25, (s % 2 === 0 ? -2 : 2), 2.5, 0, Math.PI * 2);
        ctx.fill();
      }
    } else if (p === 'koi') {
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.ellipse(-size * 0.2, 0, size * 0.35, bh * 0.6, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = sp.accent;
      ctx.beginPath();
      ctx.ellipse(size * 0.35, -1, size * 0.2, bh * 0.4, 0, 0, Math.PI * 2);
      ctx.fill();
    } else if (p === 'solid') {
      // subtle lateral line
      ctx.strokeStyle = 'rgba(255,255,255,0.25)';
      ctx.lineWidth = 1;
      ctx.beginPath();
      ctx.moveTo(-size * 0.7, 0);
      ctx.lineTo(size * 0.8, 0);
      ctx.stroke();
    } else if (p === 'angel') {
      // vertical stripes
      ctx.fillStyle = sp.accent;
      ctx.fillRect(-size * 0.25, -bh * 1.6, 2, bh * 3.2);
      ctx.fillRect(size * 0.2, -bh * 1.6, 2, bh * 3.2);
    } else if (p === 'butterfly') {
      // eye spot on body
      ctx.fillStyle = sp.accent;
      ctx.beginPath();
      ctx.arc(-size * 0.1, 0, 4, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#1a1a1a';
      ctx.beginPath();
      ctx.arc(-size * 0.1, 0, 1.5, 0, Math.PI * 2);
      ctx.fill();
      // vertical bars
      ctx.fillStyle = sp.accent;
      ctx.fillRect(size * 0.3, -bh * 0.9, 2, bh * 1.8);
    }
  }

  drawTurtle(ctx, t, size, dir, wag) {
    ctx.save();
    ctx.translate(Math.round(this.x), Math.round(this.y));
    ctx.scale(dir, 1);
    // shell
    ctx.fillStyle = '#388e3c';
    ctx.beginPath();
    ctx.ellipse(0, 0, size * 1.15, size * 0.72, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#2e7d32';
    ctx.beginPath();
    ctx.ellipse(0, 0, size * 0.95, size * 0.58, 0, 0, Math.PI * 2);
    ctx.fill();
    // shell pattern (scutes)
    ctx.strokeStyle = '#1b5e20';
    ctx.lineWidth = 1;
    for (let i = -2; i <= 2; i++) {
      ctx.beginPath();
      ctx.moveTo(i * 4, -size * 0.55);
      ctx.lineTo(i * 4, size * 0.55);
      ctx.stroke();
    }
    ctx.beginPath();
    ctx.moveTo(-size * 0.9, 0);
    ctx.lineTo(size * 0.9, 0);
    ctx.stroke();
    // head
    ctx.fillStyle = '#66bb6a';
    ctx.beginPath();
    ctx.arc(size * 0.95, -size * 0.05, size * 0.32, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#1a1a1a';
    ctx.beginPath();
    ctx.arc(size * 1.08, -size * 0.1, 1.4, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(size * 1.12, -size * 0.15, 0.5, 0, Math.PI * 2);
    ctx.fill();
    // flippers
    const fw = wag * 0.5;
    ctx.fillStyle = '#43a047';
    ctx.beginPath();
    ctx.ellipse(-size * 0.45, -size * 0.72, 6, 3, -0.5 + fw, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.ellipse(-size * 0.45, size * 0.72, 6, 3, 0.5 - fw, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.ellipse(size * 0.4, -size * 0.72, 5, 3, 0.5 - fw, 0, Math.PI * 2);
    ctx.fill();
    ctx.beginPath();
    ctx.ellipse(size * 0.4, size * 0.72, 5, 3, -0.5 + fw, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  drawPuffer(ctx, t, size, dir, wag) {
    ctx.save();
    ctx.translate(Math.round(this.x), Math.round(this.y));
    ctx.scale(dir, 1);
    const r = size * 0.85;
    // body (round)
    ctx.fillStyle = shade('#fff59d', -0.1);
    ctx.beginPath();
    ctx.arc(0, 0, r + 1, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#fff59d';
    ctx.beginPath();
    ctx.arc(0, 0, r, 0, Math.PI * 2);
    ctx.fill();
    // highlight
    ctx.fillStyle = 'rgba(255,255,255,0.3)';
    ctx.beginPath();
    ctx.arc(-r * 0.25, -r * 0.25, r * 0.45, 0, Math.PI * 2);
    ctx.fill();
    // spots
    ctx.fillStyle = '#f48fb1';
    for (let i = 0; i < 8; i++) {
      const a = (i / 8) * Math.PI * 2;
      ctx.beginPath();
      ctx.arc(Math.cos(a) * r * 0.55, Math.sin(a) * r * 0.55, 2, 0, Math.PI * 2);
      ctx.fill();
    }
    // spikes
    ctx.strokeStyle = '#5d4037';
    ctx.lineWidth = 1;
    for (let i = 0; i < 12; i++) {
      const a = (i / 12) * Math.PI * 2;
      ctx.beginPath();
      ctx.moveTo(Math.cos(a) * r, Math.sin(a) * r);
      ctx.lineTo(Math.cos(a) * (r + 3), Math.sin(a) * (r + 3));
      ctx.stroke();
    }
    // tail
    ctx.fillStyle = '#f48fb1';
    ctx.beginPath();
    ctx.moveTo(-r, 0);
    ctx.lineTo(-r - 6, -4 + wag * 3);
    ctx.lineTo(-r - 6, 4 + wag * 3);
    ctx.closePath();
    ctx.fill();
    // eye
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(r * 0.35, -r * 0.15, 4, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#1a1a1a';
    ctx.beginPath();
    ctx.arc(r * 0.4, -r * 0.15, 2, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(r * 0.45, -r * 0.22, 0.8, 0, Math.PI * 2);
    ctx.fill();
    // mouth
    ctx.fillStyle = '#5d4037';
    ctx.beginPath();
    ctx.arc(r * 0.85, 0.5, 1.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }

  drawAngel(ctx, t, size, dir, wag) {
    ctx.save();
    ctx.translate(Math.round(this.x), Math.round(this.y));
    ctx.scale(dir, 1);
    const bh = size * 0.9;
    const bw = size * 0.6;
    // tail
    ctx.fillStyle = '#c2185b';
    ctx.beginPath();
    ctx.moveTo(-bw, 0);
    ctx.lineTo(-bw - 7, -4 + wag * 3);
    ctx.lineTo(-bw - 7, 4 + wag * 3);
    ctx.closePath();
    ctx.fill();
    // body (tall)
    ctx.fillStyle = shade('#f8bbd0', -0.1);
    ctx.beginPath();
    ctx.ellipse(0, 0, bw, bh, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#f8bbd0';
    ctx.beginPath();
    ctx.ellipse(0, 0, bw * 0.85, bh * 0.85, 0, 0, Math.PI * 2);
    ctx.fill();
    // highlight
    ctx.fillStyle = 'rgba(255,255,255,0.25)';
    ctx.beginPath();
    ctx.ellipse(-bw * 0.2, -bh * 0.3, bw * 0.4, bh * 0.3, -0.3, 0, Math.PI * 2);
    ctx.fill();
    // stripes
    ctx.fillStyle = '#c2185b';
    ctx.fillRect(-1, -bh, 2, bh * 2);
    // long dorsal fin
    ctx.fillStyle = '#c2185b';
    ctx.beginPath();
    ctx.moveTo(-bw * 0.6, -bh);
    ctx.lineTo(0, -bh - size * 0.7);
    ctx.lineTo(bw * 0.6, -bh);
    ctx.closePath();
    ctx.fill();
    // anal fin
    ctx.beginPath();
    ctx.moveTo(-bw * 0.6, bh);
    ctx.lineTo(0, bh + size * 0.5);
    ctx.lineTo(bw * 0.6, bh);
    ctx.closePath();
    ctx.fill();
    // eye
    ctx.fillStyle = '#ffffff';
    ctx.beginPath();
    ctx.arc(bw * 0.35, -bh * 0.2, 2.5, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#1a1a1a';
    ctx.beginPath();
    ctx.arc(bw * 0.4, -bh * 0.2, 1.3, 0, Math.PI * 2);
    ctx.fill();
    ctx.restore();
  }
}

function shade(hex, amt) {
  // amt: -1..1
  const c = hex.replace('#', '');
  const num = parseInt(c, 16);
  let r = (num >> 16) & 255;
  let g = (num >> 8) & 255;
  let b = num & 255;
  r = Math.max(0, Math.min(255, r + amt * 255));
  g = Math.max(0, Math.min(255, g + amt * 255));
  b = Math.max(0, Math.min(255, b + amt * 255));
  return `rgb(${r|0},${g|0},${b|0})`;
}
