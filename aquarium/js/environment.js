export class Environment {
  constructor() {
    this.time = 0;
    this.rays = [];
    for (let i = 0; i < 7; i++) {
      this.rays.push({ x: 0.1 + i * 0.13, width: 0.04 + Math.random() * 0.03, speed: 0.3 + Math.random() * 0.4, phase: Math.random() * Math.PI * 2 });
    }
    this.plants = [];
    for (let i = 0; i < 14; i++) {
      this.plants.push({ x: i * 0.07 + 0.02, h: 0.06 + Math.random() * 0.12, phase: Math.random() * Math.PI * 2, type: Math.random() < 0.5 ? 'seaweed' : 'plant' });
    }
  }

  draw(ctx, w, h, t) {
    this.time = t;
    // Water gradient
    const grad = ctx.createLinearGradient(0, 0, 0, h);
    grad.addColorStop(0, '#3ec6ff');
    grad.addColorStop(0.35, '#1a9fe0');
    grad.addColorStop(0.7, '#0d6fa8');
    grad.addColorStop(1, '#084a7a');
    ctx.fillStyle = grad;
    ctx.fillRect(0, 0, w, h);

    // Sunlight rays
    ctx.save();
    ctx.globalAlpha = 0.18;
    for (const r of this.rays) {
      const sway = Math.sin(t * r.speed + r.phase) * 0.02;
      const x = (r.x + sway) * w;
      const rw = r.width * w;
      const rayGrad = ctx.createLinearGradient(x, 0, x, h * 0.75);
      rayGrad.addColorStop(0, 'rgba(255,255,200,0.9)');
      rayGrad.addColorStop(1, 'rgba(255,255,200,0)');
      ctx.fillStyle = rayGrad;
      ctx.beginPath();
      ctx.moveTo(x - rw * 0.3, 0);
      ctx.lineTo(x + rw * 0.3, 0);
      ctx.lineTo(x + rw * 1.2, h * 0.75);
      ctx.lineTo(x - rw * 1.2, h * 0.75);
      ctx.closePath();
      ctx.fill();
    }
    ctx.restore();

    // Background coral silhouettes (depth layer)
    this.drawBackgroundCoral(ctx, w, h, t);

    // Seabed
    const seabedY = h * 0.82;
    // sand gradient
    const sand = ctx.createLinearGradient(0, seabedY, 0, h);
    sand.addColorStop(0, '#e8c97a');
    sand.addColorStop(0.5, '#d4a95a');
    sand.addColorStop(1, '#b88a3a');
    ctx.fillStyle = sand;
    ctx.fillRect(0, seabedY, w, h - seabedY);

    // sand ripples
    ctx.strokeStyle = 'rgba(160,120,50,0.35)';
    ctx.lineWidth = 1;
    for (let i = 0; i < w; i += 12) {
      const y = seabedY + 6 + Math.sin(i * 0.05 + t * 0.5) * 2;
      ctx.beginPath();
      ctx.moveTo(i, y);
      ctx.lineTo(i + 6, y);
      ctx.stroke();
    }

    // Plants on seabed
    for (const p of this.plants) {
      const px = p.x * w;
      const baseY = seabedY;
      this.drawPlant(ctx, px, baseY, p.h * h, t, p.phase, p.type);
    }
  }

  drawBackgroundCoral(ctx, w, h, t) {
    ctx.save();
    ctx.globalAlpha = 0.35;
    // far coral blobs
    const cols = ['#ff7a9e', '#ff9f6b', '#c77dff'];
    for (let i = 0; i < 5; i++) {
      const x = (0.1 + i * 0.19) * w;
      const y = h * 0.78;
      ctx.fillStyle = cols[i % cols.length];
      ctx.beginPath();
      ctx.arc(x, y, 18 + (i % 3) * 6, Math.PI, 0);
      ctx.fill();
      // bumps
      for (let b = 0; b < 4; b++) {
        ctx.beginPath();
        ctx.arc(x - 12 + b * 8, y - 6 - (b % 2) * 4, 6, 0, Math.PI * 2);
        ctx.fill();
      }
    }
    ctx.restore();
  }

  drawPlant(ctx, x, baseY, height, t, phase, type) {
    const segments = 8;
    const segH = height / segments;
    let cx = x;
    let cy = baseY;
    ctx.strokeStyle = type === 'seaweed' ? '#2e9e5b' : '#4caf50';
    ctx.lineWidth = 3;
    ctx.lineCap = 'round';
    ctx.beginPath();
    ctx.moveTo(cx, cy);
    for (let i = 0; i < segments; i++) {
      const sway = Math.sin(t * 1.2 + phase + i * 0.6) * (2 + i * 0.5);
      cx += sway * 0.3;
      cy -= segH;
      ctx.lineTo(cx, cy);
    }
    ctx.stroke();
    // leaves
    if (type === 'plant') {
      ctx.fillStyle = '#66bb6a';
      for (let i = 2; i < segments; i += 2) {
        const ly = baseY - i * segH;
        const lx = x + Math.sin(t * 1.2 + phase + i * 0.6) * (i * 0.6);
        ctx.beginPath();
        ctx.ellipse(lx + 6, ly, 5, 2, 0.4, 0, Math.PI * 2);
        ctx.fill();
      }
    }
  }

  drawDecor(ctx, decor, t) {
    for (const d of decor) {
      this.drawDecorItem(ctx, d, t);
    }
  }

  drawDecorItem(ctx, d, t) {
    const x = d.x, y = d.y;
    switch (d.type) {
      case 'coral':
        ctx.fillStyle = '#ff6f61';
        ctx.beginPath();
        ctx.arc(x, y, 14, Math.PI, 0);
        ctx.fill();
        ctx.fillStyle = '#ff8a80';
        for (let b = 0; b < 5; b++) {
          ctx.beginPath();
          ctx.arc(x - 10 + b * 5, y - 4 - (b % 2) * 5, 4, 0, Math.PI * 2);
          ctx.fill();
        }
        break;
      case 'rock':
        ctx.fillStyle = '#78909c';
        ctx.beginPath();
        ctx.ellipse(x, y, 16, 10, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.fillStyle = '#90a4ae';
        ctx.beginPath();
        ctx.ellipse(x - 4, y - 3, 6, 4, 0, 0, Math.PI * 2);
        ctx.fill();
        break;
      case 'treasure':
        // chest
        ctx.fillStyle = '#8d6e63';
        ctx.fillRect(x - 14, y - 10, 28, 16);
        ctx.fillStyle = '#ffd54f';
        ctx.fillRect(x - 14, y - 12, 28, 4);
        ctx.fillStyle = '#ffca28';
        ctx.fillRect(x - 3, y - 4, 6, 6);
        // coins
        ctx.fillStyle = '#ffd54f';
        for (let c = 0; c < 3; c++) {
          ctx.beginPath();
          ctx.arc(x - 8 + c * 8, y - 16 + Math.sin(t*2+c)*2, 3, 0, Math.PI*2);
          ctx.fill();
        }
        break;
      case 'shipwreck':
        ctx.fillStyle = '#5d4037';
        ctx.fillRect(x - 30, y - 6, 60, 12);
        ctx.fillRect(x - 6, y - 30, 12, 30);
        ctx.fillStyle = '#8d6e63';
        ctx.fillRect(x - 30, y - 8, 60, 4);
        break;
      case 'shell':
        ctx.fillStyle = '#ffccbc';
        ctx.beginPath();
        ctx.arc(x, y, 8, Math.PI, 0);
        ctx.fill();
        ctx.strokeStyle = '#ff8a65';
        ctx.lineWidth = 1;
        for (let s = 0; s < 4; s++) {
          ctx.beginPath();
          ctx.moveTo(x, y);
          ctx.lineTo(x - 6 + s * 4, y - 6);
          ctx.stroke();
        }
        break;
      case 'seaweed':
        this.drawPlant(ctx, x, y, 40, t, x, 'seaweed');
        break;
      case 'plant':
        this.drawPlant(ctx, x, y, 30, t, x, 'plant');
        break;
    }
  }
}
