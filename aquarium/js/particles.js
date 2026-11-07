export class ParticleSystem {
  constructor() {
    this.bubbles = [];
    this.food = []; // {x,y,vy,life}
    this.sparkles = [];
    this.bubbleTimer = 0;
  }

  update(dt, w, h) {
    // ambient bubbles
    this.bubbleTimer += dt;
    if (this.bubbleTimer > 0.4) {
      this.bubbleTimer = 0;
      this.bubbles.push({
        x: Math.random() * w,
        y: h * 0.82,
        r: 1 + Math.random() * 2.5,
        vy: -20 - Math.random() * 30,
        vx: (Math.random() - 0.5) * 6,
        life: 4 + Math.random() * 3
      });
    }

    for (let i = this.bubbles.length - 1; i >= 0; i--) {
      const b = this.bubbles[i];
      b.x += b.vx * dt;
      b.y += b.vy * dt;
      b.life -= dt;
      b.vy *= 0.995;
      if (b.life <= 0 || b.y < 0) this.bubbles.splice(i, 1);
    }

    // food
    for (let i = this.food.length - 1; i >= 0; i--) {
      const f = this.food[i];
      f.vy += 40 * dt; // gravity-ish sinking (pixels/s^2)
      if (f.vy > 60) f.vy = 60;
      f.y += f.vy * dt;
      f.x += Math.sin(f.y * 0.05) * 2 * dt;
      f.life -= dt;
      // bottom stop
      if (f.y > h * 0.82) { f.y = h * 0.82; f.vy = 0; }
      if (f.life <= 0) this.food.splice(i, 1);
    }

    // sparkles
    for (let i = this.sparkles.length - 1; i >= 0; i--) {
      const s = this.sparkles[i];
      s.x += s.vx * dt;
      s.y += s.vy * dt;
      s.life -= dt;
      s.vy += 60 * dt;
      if (s.life <= 0) this.sparkles.splice(i, 1);
    }
  }

  spawnFood(x, y) {
    this.food.push({ x, y, vy: 0, life: 12, size: 3 + Math.random() * 2 });
  }

  spawnSparkle(x, y) {
    for (let i = 0; i < 6; i++) {
      this.sparkles.push({
        x, y,
        vx: (Math.random() - 0.5) * 60,
        vy: -30 - Math.random() * 40,
        life: 0.6 + Math.random() * 0.4,
        color: Math.random() < 0.5 ? '#ffd54f' : '#fff'
      });
    }
  }

  draw(ctx) {
    // bubbles
    ctx.save();
    ctx.strokeStyle = 'rgba(255,255,255,0.5)';
    ctx.lineWidth = 1;
    for (const b of this.bubbles) {
      ctx.globalAlpha = Math.min(1, b.life);
      ctx.beginPath();
      ctx.arc(b.x, b.y, b.r, 0, Math.PI * 2);
      ctx.stroke();
      // highlight
      ctx.fillStyle = 'rgba(255,255,255,0.3)';
      ctx.beginPath();
      ctx.arc(b.x - b.r * 0.3, b.y - b.r * 0.3, b.r * 0.4, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();

    // food
    ctx.save();
    for (const f of this.food) {
      ctx.fillStyle = '#8d6e63';
      ctx.beginPath();
      ctx.arc(f.x, f.y, f.size, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#a1887f';
      ctx.beginPath();
      ctx.arc(f.x - 1, f.y - 1, f.size * 0.5, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.restore();

    // sparkles
    ctx.save();
    for (const s of this.sparkles) {
      ctx.globalAlpha = Math.max(0, s.life * 2);
      ctx.fillStyle = s.color;
      ctx.fillRect(s.x, s.y, 2, 2);
    }
    ctx.restore();
  }

  // helper to find nearest food to a point
  nearestFood(x, y, radius) {
    let best = null, bestD = radius;
    for (const f of this.food) {
      const d = Math.hypot(f.x - x, f.y - y);
      if (d < bestD) { bestD = d; best = f; }
    }
    return best;
  }

  removeFood(f) {
    const i = this.food.indexOf(f);
    if (i >= 0) this.food.splice(i, 1);
  }
}
