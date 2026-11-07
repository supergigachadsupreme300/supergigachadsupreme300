import { speciesById } from './fish.js';

const BOUND_MARGIN = 30;

export function updateFishes(fishes, dt, w, h, particles) {
  let eaten = 0;
  const seabedY = h * 0.82;

  for (let i = 0; i < fishes.length; i++) {
    const f = fishes[i];
    const sp = f.species;

    if (f.eating > 0) f.eating = Math.max(0, f.eating - dt);

    // state timer
    f.stateTimer -= dt;
    if (f.stateTimer <= 0) {
      // pick next state with probabilities
      const r = Math.random();
      if (r < 0.45) { f.state = 'wander'; f.stateTimer = 3 + Math.random() * 5; }
      else if (r < 0.65) { f.state = 'idle'; f.stateTimer = 2 + Math.random() * 3; }
      else if (r < 0.78) { f.state = 'rest'; f.stateTimer = 3 + Math.random() * 4; }
      else { f.state = 'seek'; f.stateTimer = 2 + Math.random() * 3; }
      f.wanderTimer = 0;
    }

    // food seeking overrides
    let food = particles.nearestFood(f.x, f.y, 160);
    if (food && (f.state === 'wander' || f.state === 'idle')) {
      f.state = 'seek';
    }

    f.wanderTimer -= dt;
    if (f.wanderTimer <= 0) {
      f.wanderTimer = 2 + Math.random() * 3;
      f.wanderTarget = {
        x: BOUND_MARGIN + Math.random() * (w - BOUND_MARGIN * 2),
        y: 40 + Math.random() * (seabedY - 80)
      };
    }

    let dvx = 0, dvy = 0;
    const targetSpeed = sp.speed;

    if (f.state === 'seek' && food) {
      const dx = food.x - f.x;
      const dy = food.y - f.y;
      const d = Math.hypot(dx, dy) || 1;
      const seekSpeed = sp.speed * 1.4;
      dvx = (dx / d) * seekSpeed;
      dvy = (dy / d) * seekSpeed;
      if (d < 8) {
        particles.removeFood(food);
        particles.spawnSparkle(f.x, f.y);
        f.eating = 0.6;
        eaten++;
        food = null;
        f.state = 'wander';
        f.stateTimer = 2 + Math.random() * 3;
      }
    } else if (f.state === 'idle') {
      // slow drift
      dvx = f.vx * 0.3;
      dvy = f.vy * 0.3 + (Math.random() - 0.5) * 2;
    } else if (f.state === 'rest') {
      // sink gently toward seabed, minimal movement
      const restY = seabedY - 12 - Math.random() * 6;
      dvx = (Math.random() - 0.5) * 3;
      dvy = (restY - f.y) * 0.8;
    } else {
      // wander
      const dx = f.wanderTarget.x - f.x;
      const dy = f.wanderTarget.y - f.y;
      const d = Math.hypot(dx, dy) || 1;
      dvx = (dx / d) * targetSpeed;
      dvy = (dy / d) * targetSpeed;
    }

    // Schooling & separation
    let sx = 0, sy = 0, ax = 0, ay = 0, cx = 0, cy = 0, n = 0;
    for (let j = 0; j < fishes.length; j++) {
      if (i === j) continue;
      const o = fishes[j];
      const dx = o.x - f.x;
      const dy = o.y - f.y;
      const d = Math.hypot(dx, dy);
      if (d < 130 && d > 0) {
        n++;
        if (d < 38) { sx -= dx / d; sy -= dy / d; }
        ax += o.vx; ay += o.vy;
        cx += o.x; cy += o.y;
      }
    }
    if (n > 0) {
      dvx += sx * 45;
      dvy += sy * 45;
      if (sp.schooling) {
        dvx += ((cx / n - f.x) * 0.4);
        dvy += ((cy / n - f.y) * 0.4);
        dvx += (ax / n) * 0.25;
        dvy += (ay / n) * 0.25;
      }
    }

    // Boundary avoidance
    const margin = BOUND_MARGIN;
    if (f.x < margin) dvx += (margin - f.x) * 2.5;
    if (f.x > w - margin) dvx -= (f.x - (w - margin)) * 2.5;
    if (f.y < 40) dvy += (40 - f.y) * 2.5;
    if (f.y > seabedY - 10) dvy -= (f.y - (seabedY - 10)) * 2.5;

    // Steering
    const steer = f.state === 'rest' ? 3 : 6;
    f.vx += (dvx - f.vx) * Math.min(1, dt * steer);
    f.vy += (dvy - f.vy) * Math.min(1, dt * steer);

    // Speed clamp
    const maxSpeed = sp.speed * 1.5;
    const spd = Math.hypot(f.vx, f.vy);
    if (spd > maxSpeed) {
      f.vx = (f.vx / spd) * maxSpeed;
      f.vy = (f.vy / spd) * maxSpeed;
    }
    if (spd < 1 && f.state !== 'rest') {
      f.vx += (Math.random() - 0.5) * 4;
      f.vy += (Math.random() - 0.5) * 4;
    }

    f.x += f.vx * dt;
    f.y += f.vy * dt;
    f.x = Math.max(margin, Math.min(w - margin, f.x));
    f.y = Math.max(30, Math.min(seabedY - 8, f.y));

    const ang = Math.atan2(f.vy, f.vx);
    let diff = ang - f.angle;
    while (diff > Math.PI) diff -= Math.PI * 2;
    while (diff < -Math.PI) diff += Math.PI * 2;
    f.angle += diff * Math.min(1, dt * 8);

    f.animPhase += dt * 3;
  }

  return eaten;
}
