import { speciesById } from './fish.js';

const BOUND_MARGIN = 30;

export function updateFishes(fishes, dt, w, h, particles) {
  let eaten = 0;
  const seabedY = h * 0.82;

  // Precompute neighbors for schooling/separation
  for (let i = 0; i < fishes.length; i++) {
    const f = fishes[i];
    const sp = f.species;

    // Eating state timer
    if (f.eating > 0) f.eating = Math.max(0, f.eating - dt);

    // Find nearest food
    let food = particles.nearestFood(f.x, f.y, 140);
    if (food) {
      f.state = 'seek';
    } else if (sp.schooling) {
      f.state = 'school';
    } else {
      f.state = 'wander';
    }

    // Wander target refresh
    f.wanderTimer -= dt;
    if (f.wanderTimer <= 0) {
      f.wanderTimer = 1.5 + Math.random() * 2.5;
      f.wanderTarget = {
        x: BOUND_MARGIN + Math.random() * (w - BOUND_MARGIN * 2),
        y: 40 + Math.random() * (seabedY - 80)
      };
    }

    // Desired velocity
    let dvx = 0, dvy = 0;

    if (f.state === 'seek' && food) {
      const dx = food.x - f.x;
      const dy = food.y - f.y;
      const d = Math.hypot(dx, dy) || 1;
      const seekSpeed = sp.speed * 1.3;
      dvx = (dx / d) * seekSpeed;
      dvy = (dy / d) * seekSpeed;
      // eat if close
      if (d < 8) {
        particles.removeFood(food);
        particles.spawnSparkle(f.x, f.y);
        f.eating = 0.6;
        eaten++;
        food = null;
        f.state = 'wander';
      }
    } else {
      // wander toward target
      const dx = f.wanderTarget.x - f.x;
      const dy = f.wanderTarget.y - f.y;
      const d = Math.hypot(dx, dy) || 1;
      dvx = (dx / d) * sp.speed;
      dvy = (dy / d) * sp.speed;
    }

    // Schooling & separation
    let sx = 0, sy = 0, ax = 0, ay = 0, cx = 0, cy = 0, n = 0;
    for (let j = 0; j < fishes.length; j++) {
      if (i === j) continue;
      const o = fishes[j];
      const dx = o.x - f.x;
      const dy = o.y - f.y;
      const d = Math.hypot(dx, dy);
      if (d < 1 && d > 0) { /* avoid div0 */ }
      if (d < 120 && d > 0) {
        n++;
        // separation
        if (d < 35) {
          sx -= dx / d;
          sy -= dy / d;
        }
        // alignment
        ax += o.vx;
        ay += o.vy;
        // cohesion
        cx += o.x;
        cy += o.y;
      }
    }
    if (n > 0) {
      // apply separation strongly
      dvx += sx * 40;
      dvy += sy * 40;
      // cohesion/alignment only for schooling species
      if (sp.schooling) {
        dvx += ((cx / n - f.x) * 0.5);
        dvy += ((cy / n - f.y) * 0.5);
        dvx += (ax / n) * 0.3;
        dvy += (ay / n) * 0.3;
      }
    }

    // Boundary avoidance
    const margin = BOUND_MARGIN;
    if (f.x < margin) dvx += (margin - f.x) * 2;
    if (f.x > w - margin) dvx -= (f.x - (w - margin)) * 2;
    if (f.y < 40) dvy += (40 - f.y) * 2;
    if (f.y > seabedY - 10) dvy -= (f.y - (seabedY - 10)) * 2;

    // Smooth velocity change (steering)
    const steer = 6;
    f.vx += (dvx - f.vx) * Math.min(1, dt * steer);
    f.vy += (dvy - f.vy) * Math.min(1, dt * steer);

    // Clamp speed
    const spSpeed = sp.speed * 1.6;
    const spd = Math.hypot(f.vx, f.vy);
    if (spd > spSpeed) {
      f.vx = (f.vx / spd) * spSpeed;
      f.vy = (f.vy / spd) * spSpeed;
    }
    if (spd < sp.speed * 0.3) {
      // nudge
      f.vx += (Math.random() - 0.5) * 5;
      f.vy += (Math.random() - 0.5) * 5;
    }

    // Move
    f.x += f.vx * dt;
    f.y += f.vy * dt;

    // Hard clamp
    f.x = Math.max(margin, Math.min(w - margin, f.x));
    f.y = Math.max(30, Math.min(seabedY - 8, f.y));

    // Angle smoothing
    const ang = Math.atan2(f.vy, f.vx);
    // shortest diff
    let diff = ang - f.angle;
    while (diff > Math.PI) diff -= Math.PI * 2;
    while (diff < -Math.PI) diff += Math.PI * 2;
    f.angle += diff * Math.min(1, dt * 8);

    f.animPhase += dt * 3;
  }

  return eaten;
}
