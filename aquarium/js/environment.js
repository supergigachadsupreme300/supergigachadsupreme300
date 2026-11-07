import { getAsset } from './assets.js';

export class Environment {
  constructor() {
    this.time = 0;
    this.rays = [];
    for (let i = 0; i < 9; i++) {
      this.rays.push({ x: 0.05 + i * 0.11, width: 0.035 + Math.random() * 0.025, speed: 0.25 + Math.random() * 0.35, phase: Math.random() * Math.PI * 2 });
    }
    this.currents = [];
    for (let i = 0; i < 6; i++) {
      this.currents.push({ y: 0.15 + i * 0.12, speed: 0.4 + Math.random() * 0.6, phase: Math.random() * Math.PI * 2, len: 0.3 + Math.random() * 0.4 });
    }
    // Structured reef composition: left group, right group, center landmark, sparse middle.
    this.plants = [
      // left reef cluster
      { x: 0.06, h: 0.12, phase: 0.2, type: 'kelp' },
      { x: 0.09, h: 0.09, phase: 0.7, type: 'seaweed' },
      { x: 0.12, h: 0.07, phase: 1.1, type: 'plant' },
      // center-left small
      { x: 0.30, h: 0.06, phase: 1.5, type: 'seaweed' },
      // right reef cluster
      { x: 0.78, h: 0.11, phase: 2.0, type: 'kelp' },
      { x: 0.82, h: 0.08, phase: 2.4, type: 'seaweed' },
      { x: 0.86, h: 0.06, phase: 2.8, type: 'plant' },
      // far right
      { x: 0.93, h: 0.05, phase: 3.1, type: 'plant' }
    ];
    this.rocks = [
      { x: 0.10, r: 0.018, phase: 0.3 },
      { x: 0.22, r: 0.014, phase: 0.9 },
      { x: 0.80, r: 0.016, phase: 1.6 }
    ];
    this.coralSpots = [
      // left reef formation (3 corals)
      { x: 0.05, type: 0, phase: 0.1 },
      { x: 0.10, type: 1, phase: 0.6 },
      { x: 0.16, type: 2, phase: 1.1 },
      // right reef formation
      { x: 0.76, type: 3, phase: 1.8 },
      { x: 0.82, type: 0, phase: 2.3 },
      { x: 0.88, type: 1, phase: 2.8 }
    ];
  }

  draw(ctx, w, h, t) {
    this.time = t;
    const seabedY = h * 0.84;

    // 1. Background gradient (rich turquoise -> deep blue)
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, '#4fd3ff');
    grad.addColorStop(0.25, '#29b6f6');
    grad.addColorStop(0.5, '#0288d1');
    grad.addColorStop(0.75, '#01579b');
    grad.addColorStop(1, '#003f6b');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Distant silhouettes (far reefs/rocks)
    ctx.save();
    ctx.globalAlpha = 0.25;
    ctx.fillStyle = '#014a7a';
    for (let i = 0; i < 5; i++) {
      const x = (0.05 + i * 0.2) * w;
      ctx.beginPath();
      ctx.arc(x, seabedY, 30 + (i % 3) * 12, Math.PI, 0);
      ctx.fill();
    }
    ctx.restore();

    // Horizontal currents
    ctx.save();
    ctx.globalAlpha = 0.12;
    ctx.strokeStyle = '#b3e5fc';
    ctx.lineWidth = 1;
    for (const c of this.currents) {
      const y = c.y * h;
      ctx.beginPath();
      for (let x = 0; x < w; x += 4) {
        const yy = y + Math.sin(x * 0.02 + t * c.speed + c.phase) * 3;
        if (x === 0) ctx.moveTo(x, yy);
        else ctx.lineTo(x, yy);
      }
      ctx.stroke();
    }
    ctx.restore();

    // Sunlight rays
    ctx.save();
    for (const r of this.rays) {
      const sway = Math.sin(t * r.speed + r.phase) * 0.025;
      const x = (r.x + sway) * w;
      const rw = r.width * w;
      const rayGrad = ctx.createLinearGradient(x, 0, x + rw * 0.5, h * 0.8);
      rayGrad.addColorStop(0, 'rgba(255,255,220,0.35)');
      rayGrad.addColorStop(0.5, 'rgba(255,255,220,0.12)');
      rayGrad.addColorStop(1, 'rgba(255,255,220,0)');
      ctx.fillStyle = rayGrad;
      ctx.beginPath();
      ctx.moveTo(x - rw * 0.4, 0);
      ctx.lineTo(x + rw * 0.4, 0);
      ctx.lineTo(x + rw * 1.6, h * 0.85);
      ctx.lineTo(x - rw * 1.6, h * 0.85);
      ctx.closePath();
      ctx.fill();
    }
    ctx.restore();

    // Caustics on seabed
    ctx.save();
    ctx.globalAlpha = 0.15;
    for (let i = 0; i < 8; i++) {
      const cx = (0.1 + i * 0.12) * w + Math.sin(t * 0.8 + i) * 10;
      const cy = seabedY - 5 + Math.cos(t * 0.6 + i * 1.3) * 3;
      ctx.fillStyle = '#b3e5fc';
      ctx.beginPath();
      ctx.ellipse(cx, cy, 18, 6, 0, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();

    // Midground coral sprites
    const coralKeys = ['coral_branching','coral_brain','coral_seafan','anemone'];
    for (let i = 0; i < this.coralSpots.length; i++) {
      const c = this.coralSpots[i];
      const key = coralKeys[c.type % coralKeys.length];
      const img = getAsset(key, 0);
      if (img) {
        const scale = 0.35;
        const iw = img.width * scale;
        const ih = img.height * scale;
        ctx.save();
        ctx.globalAlpha = 0.85;
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, c.x * w - iw/2, seabedY - ih + 4, iw, ih);
        ctx.restore();
      } else {
        this.drawCoralFormation(ctx, c.x * w, seabedY, t, c.type, c.phase, 0.7);
      }
    }

    // Midground rocks
    for (const r of this.rocks) {
      const img = getAsset('rock', 0);
      if (img) {
        const s = 0.4;
        ctx.save();
        ctx.globalAlpha = 0.9;
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, r.x * w - img.width*s/2, seabedY - img.height*s + 2, img.width*s, img.height*s);
        ctx.restore();
      } else {
        this.drawRock(ctx, r.x * w, seabedY - 2, r.r * w, t, r.phase, 0.8);
      }
    }

    // Midground plants
    for (const p of this.plants) {
      const key = p.type === 'kelp' ? 'kelp' : 'seaweed';
      const img = getAsset(key, 0);
      if (img) {
        const s = p.type === 'kelp' ? 0.35 : 0.3;
        const sway = Math.sin(t * 1.1 + p.phase) * 3;
        ctx.save();
        ctx.globalAlpha = 0.9;
        ctx.imageSmoothingEnabled = false;
        ctx.drawImage(img, p.x * w - img.width*s/2 + sway, seabedY - img.height*s + 4, img.width*s, img.height*s);
        ctx.restore();
      } else {
        this.drawPlant(ctx, p.x * w, seabedY, p.h * h, t, p.phase, p.type, 0.9);
      }
    }

    // Central landmark: shipwreck (midground)
    const sw = getAsset('shipwreck', 0);
    if (sw) {
      ctx.save();
      ctx.globalAlpha = 0.85;
      ctx.imageSmoothingEnabled = false;
      const s = 0.5;
      ctx.drawImage(sw, w * 0.82 - sw.width * s / 2, seabedY - sw.height * s + 4, sw.width * s, sw.height * s);
      ctx.restore();
    }

    // Seabed
    const sand = ctx.createLinearGradient(0, seabedY, 0, h);
    sand.addColorStop(0, '#f2d68a');
    sand.addColorStop(0.3, '#e6c06a');
    sand.addColorStop(0.7, '#d4a95a');
    sand.addColorStop(1, '#b88a3a');
    ctx.fillStyle = sand;
    ctx.fillRect(0, seabedY, w, h - seabedY);

    // Sand texture (ripples + grains)
    ctx.save();
    ctx.globalAlpha = 0.35;
    for (let i = 0; i < w; i += 6) {
      const y = seabedY + 4 + Math.sin(i * 0.07 + t * 0.4) * 1.5;
      ctx.fillStyle = '#c9a04a';
      ctx.fillRect(i, y, 3, 1);
    }
    // grains
    ctx.fillStyle = '#a07a2a';
    for (let i = 0; i < 80; i++) {
      const gx = (i * 37) % w;
      const gy = seabedY + 2 + (i * 13) % (h - seabedY - 4);
      ctx.fillRect(gx, gy, 1, 1);
    }
    ctx.restore();

    // Foreground small stones/shells near bottom
    ctx.save();
    for (let i = 0; i < 12; i++) {
      const sx = (0.05 + i * 0.08) * w;
      const sy = seabedY + 6 + (i % 3) * 3;
      if (i % 2 === 0) {
        ctx.fillStyle = '#90a4ae';
        ctx.beginPath();
        ctx.ellipse(sx, sy, 4, 2.5, 0, 0, Math.PI * 2);
        ctx.fill();
      } else {
        ctx.fillStyle = '#ffccbc';
        ctx.beginPath();
        ctx.arc(sx, sy, 3, Math.PI, 0);
        ctx.fill();
      }
    }
    ctx.restore();
  }

  drawCoralFormation(ctx, x, baseY, t, type, phase, alpha) {
    ctx.save();
    ctx.globalAlpha = alpha;
    const sway = Math.sin(t * 0.6 + phase) * 2;
    switch (type) {
      case 0: // branching coral
        ctx.strokeStyle = '#ff6f61';
        ctx.lineWidth = 2;
        ctx.lineCap = 'round';
        for (let b = 0; b < 5; b++) {
          ctx.beginPath();
          ctx.moveTo(x, baseY);
          const ang = -Math.PI / 2 + (b - 2) * 0.35 + sway * 0.02;
          const len = 18 + (b % 2) * 8;
          ctx.lineTo(x + Math.cos(ang) * len, baseY + Math.sin(ang) * len);
          ctx.stroke();
          // sub-branches
          ctx.lineWidth = 1;
          ctx.beginPath();
          ctx.moveTo(x + Math.cos(ang) * len * 0.6, baseY + Math.sin(ang) * len * 0.6);
          ctx.lineTo(x + Math.cos(ang) * len * 0.6 + Math.cos(ang + 0.6) * 8, baseY + Math.sin(ang) * len * 0.6 + Math.sin(ang + 0.6) * 8);
          ctx.stroke();
          ctx.lineWidth = 2;
        }
        break;
      case 1: // brain coral
        ctx.fillStyle = '#ff8a65';
        ctx.beginPath();
        ctx.arc(x, baseY - 8, 12, Math.PI, 0);
        ctx.fill();
        ctx.strokeStyle = '#e64a19';
        ctx.lineWidth = 1;
        for (let g = 0; g < 6; g++) {
          ctx.beginPath();
          ctx.arc(x, baseY - 8, 4 + g * 1.5, 0, Math.PI * 2);
          ctx.stroke();
        }
        break;
      case 2: // sea fan
        ctx.strokeStyle = '#ce93d8';
        ctx.lineWidth = 1.5;
        for (let i = 0; i < 7; i++) {
          const a = -Math.PI / 2 + (i - 3) * 0.25;
          ctx.beginPath();
          ctx.moveTo(x, baseY);
          ctx.quadraticCurveTo(x + Math.cos(a) * 12, baseY + Math.sin(a) * 12 - 4, x + Math.cos(a) * 22, baseY + Math.sin(a) * 22);
          ctx.stroke();
        }
        break;
      case 3: // anemone
        ctx.fillStyle = '#f48fb1';
        for (let t2 = 0; t2 < 9; t2++) {
          const a = (t2 / 9) * Math.PI * 2;
          const sway2 = Math.sin(this.time * 1.5 + phase + t2) * 2;
          ctx.beginPath();
          ctx.moveTo(x, baseY);
          ctx.quadraticCurveTo(x + Math.cos(a) * 6 + sway2, baseY - 10, x + Math.cos(a) * 4 + sway2, baseY - 16);
          ctx.lineWidth = 2;
          ctx.strokeStyle = '#f48fb1';
          ctx.stroke();
        }
        break;
    }
    ctx.restore();
  }

  drawRock(ctx, x, baseY, r, t, phase, alpha) {
    ctx.save();
    ctx.globalAlpha = alpha;
    ctx.fillStyle = '#78909c';
    ctx.beginPath();
    ctx.ellipse(x, baseY - r * 0.5, r * 1.3, r, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#90a4ae';
    ctx.beginPath();
    ctx.ellipse(x - r * 0.3, baseY - r * 0.8, r * 0.5, r * 0.35, 0, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#546e7a';
    ctx.beginPath();
    ctx.ellipse(x + r * 0.4, baseY - r * 0.2, r * 0.4, r * 0.25, 0, 0, Math.PI * 2);
    ctx.fill();
    // texture
    ctx.fillStyle = 'rgba(0,0,0,0.15)';
    for (let i = 0; i < 6; i++) {
      ctx.fillRect(x - r + (i * 7) % (r * 2), baseY - r * 0.5 + (i * 3) % (r), 2, 1);
    }
    ctx.restore();
  }

  drawPlant(ctx, x, baseY, height, t, phase, type, alpha = 1) {
    ctx.save();
    ctx.globalAlpha = alpha;
    const segments = 10;
    const segH = height / segments;
    let cx = x, cy = baseY;
    const color = type === 'kelp' ? '#1b5e20' : (type === 'seaweed' ? '#2e7d32' : '#43a047');
    ctx.strokeStyle = color;
    ctx.lineWidth = type === 'kelp' ? 4 : 2.5;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    for (let i = 0; i < segments; i++) {
      const sway = Math.sin(t * 1.1 + phase + i * 0.5) * (1.5 + i * 0.4);
      cx += sway * 0.25;
      cy -= segH;
      ctx.lineTo(cx, cy);
    }
    ctx.stroke();
    if (type === 'kelp') {
      // leaves
      ctx.fillStyle = '#388e3c';
      for (let i = 3; i < segments; i += 2) {
        const ly = baseY - i * segH;
        const lx = x + Math.sin(t * 1.1 + phase + i * 0.5) * (i * 0.4);
        ctx.beginPath();
        ctx.ellipse(lx + 7, ly, 6, 2.5, 0.3, 0, Math.PI * 2);
        ctx.fill();
      }
    } else if (type === 'plant') {
      ctx.fillStyle = '#66bb6a';
      for (let i = 2; i < segments; i += 2) {
        const ly = baseY - i * segH;
        const lx = x + Math.sin(t * 1.1 + phase + i * 0.5) * (i * 0.35);
        ctx.beginPath();
        ctx.ellipse(lx + 5, ly, 4, 2, 0.4, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    ctx.restore();
  }

  drawDecor(ctx, decor, t) {
    for (const d of decor) {
      this.drawDecorItem(ctx, d, t);
    }
  }

  drawDecorItem(ctx, d, t) {
    const x = d.x, y = d.y;
    const drawImg = (key, scale = 0.35, oy = 0) => {
      const img = getAsset(key, 0);
      if (!img) return false;
      ctx.save();
      ctx.imageSmoothingEnabled = false;
      const w = img.width * scale;
      const h = img.height * scale;
      ctx.drawImage(img, x - w / 2, y - h + oy, w, h);
      ctx.restore();
      return true;
    };
    switch (d.type) {
      case 'coral':
        if (!drawImg('coral_branching', 0.9, 8)) this.drawCoralFormation(ctx, x, y + 8, t, 0, x, 1);
        break;
      case 'rock':
        if (!drawImg('rock', 0.9, 4)) this.drawRock(ctx, x, y + 4, 16, t, x, 1);
        break;
      case 'treasure':
        if (!drawImg('treasure', 0.9, 8)) {
          ctx.fillStyle = '#8d6e63'; ctx.fillRect(x - 14, y - 10, 28, 16);
        }
        break;
      case 'shipwreck':
        if (!drawImg('shipwreck', 0.9, 10)) {
          ctx.fillStyle = '#5d4037'; ctx.fillRect(x - 30, y - 6, 60, 12);
        }
        break;
      case 'shell':
        if (!drawImg('shell', 0.9, 4)) {
          ctx.fillStyle = '#ffccbc'; ctx.beginPath(); ctx.arc(x, y, 8, Math.PI, 0); ctx.fill();
        }
        break;
      case 'seaweed':
        if (!drawImg('seaweed', 0.9, 4)) this.drawPlant(ctx, x, y + 4, 40, t, x, 'seaweed', 1);
        break;
      case 'plant':
        if (!drawImg('kelp', 0.7, 4)) this.drawPlant(ctx, x, y + 4, 30, t, x, 'plant', 1);
        break;
    }
  }
}
