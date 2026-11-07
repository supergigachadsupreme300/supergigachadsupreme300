import { loadSave, saveSave } from './saveManager.js';
import { Economy } from './economy.js';
import { Environment } from './environment.js';
import { ParticleSystem } from './particles.js';
import { Fish } from './fish.js';
import { updateFishes } from './fishAI.js';
import { Renderer } from './renderer.js';
import { Interaction } from './interaction.js';
import { Shop } from './shop.js';
import { AquariumGrowthEngine } from './aquariumGrowthEngine.js';

export class Game {
  constructor() {
    const params = new URLSearchParams(window.location.search);
    this.previewMode = params.get('preview') === '1' || window.location.hash === '#preview';
    this.canvas = document.getElementById('game-canvas');
    this.container = document.getElementById('game-container');
    this.ctx = this.canvas.getContext('2d');

    this.state = loadSave();
    this.economy = new Economy(this.state.coins);
    document.getElementById('coin-value').textContent = this.economy.get();
    this.economy.onChange((c) => {
      this.state.coins = c;
      document.getElementById('coin-value').textContent = c;
    });

    this.environment = new Environment();
    this.particles = new ParticleSystem();
    this.renderer = new Renderer(this.canvas);
    this.interaction = new Interaction(this.canvas, this);
    this.shop = new Shop(this);

    // Restore simulation state if available
    if (this.state.simState && Array.isArray(this.state.simState.fish)) {
      this.fishes = this.state.simState.fish.map(s => {
        const f = new Fish(s.id, s.x, s.y);
        f.vx = s.vx || 0; f.vy = s.vy || 0;
        f.origin = s.origin || 'player';
        f.animPhase = s.animPhase || Math.random() * Math.PI * 2;
        return f;
      });
      // Offline progression (capped at 8 hours)
      const elapsed = Math.min(8 * 3600, (Date.now() - (this.state.lastSave || Date.now())) / 1000);
      if (elapsed > 0) {
        const w = 320, h = 180; // approximate; will clamp later in update
        for (const f of this.fishes) {
          f.x += f.vx * elapsed * 0.5;
          f.y += f.vy * elapsed * 0.5;
        }
      }
    } else {
      this.fishes = this.state.fish.map((id, idx) => {
        const f = new Fish(id, 60 + (idx % 5) * 40, 60 + Math.floor(idx / 5) * 40);
        f.origin = 'player';
        return f;
      });
    }

    this.growthEngine = new AquariumGrowthEngine();
    this.growthProgression = null;
    this.growthEngine.init().then((prog) => {
      this.growthProgression = prog;
      this.growthEngine.apply(this);
      // update UI level display if present
      const lvl = document.getElementById('level-value');
      if (lvl && prog) lvl.textContent = prog.level + ' - ' + prog.levelName;
      const contrib = document.getElementById('contrib-value');
      if (contrib && prog) contrib.textContent = prog.lifetimeContributions;
    }).catch(e => console.warn('Growth init failed', e));

    // Auto place saved decor
    this.state.decor.forEach(d => { /* already has x,y */ });

    this.logicalW = 0;
    this.logicalH = 0;
    this.scale = 4;
    this.lastTime = 0;
    this.running = true;
    this.autoFeedTimer = 0;
    this.toastTimer = 0;
    this.simTime = 0;
    this.eventTimer = 25 + Math.random() * 20;
    this.turtleActive = false;
    this.tempRemovals = [];

    this.resize();
    window.addEventListener('resize', () => this.resize());
    document.addEventListener('visibilitychange', () => {
      if (document.hidden) this.running = false; else { this.running = true; this.lastTime = performance.now(); }
    });

    // UI wiring
    document.getElementById('shop-btn').addEventListener('click', () => this.openShop());
    document.getElementById('shop-close').addEventListener('click', () => this.closeShop());
    document.getElementById('feed-btn').addEventListener('click', () => this.feedButton());
    document.getElementById('save-btn').addEventListener('click', () => this.save());

    if (this.previewMode) {
      const hide = (id) => { const el = document.getElementById(id); if (el) el.style.display = 'none'; };
      hide('coin-counter');
      hide('shop-btn');
      hide('bottom-bar');
      hide('shop-modal');
      hide('toast');
    }

    this.shop.render();
  }

  resize() {
    const rect = this.container.getBoundingClientRect();
    this.scale = window.innerWidth < 600 ? 3 : 4;
    const w = Math.max(240, Math.floor(rect.width / this.scale));
    const h = Math.max(160, Math.floor(rect.height / this.scale));
    this.logicalW = w;
    this.logicalH = h;
    this.canvas.width = w;
    this.canvas.height = h;
    this.canvas.style.width = rect.width + 'px';
    this.canvas.style.height = rect.height + 'px';
    this.ctx.imageSmoothingEnabled = false;
    this.interaction.setLogical(w, h, this.scale);
  }

  start() {
    this.lastTime = performance.now();
    const loop = (now) => {
      const dt = Math.min(0.05, (now - this.lastTime) / 1000);
      this.lastTime = now;
      if (this.running) {
        this.update(dt);
        this.render(performance.now() / 1000);
      }
      requestAnimationFrame(loop);
    };
    requestAnimationFrame(loop);
  }

  update(dt) {
    const w = this.logicalW, h = this.logicalH;
    this.simTime += dt;
    this.particles.update(dt, w, h);
    const eaten = updateFishes(this.fishes, dt, w, h, this.particles);
    if (eaten > 0) {
      this.economy.add(eaten * 3);
      this.showToast('Fish fed! +' + (eaten * 3) + ' coins', false);
    }

    // Temp entity removal
    for (let i = this.tempRemovals.length - 1; i >= 0; i--) {
      const t = this.tempRemovals[i];
      if (this.simTime >= t.at) {
        if (t.kind === 'fish') {
          const idx = this.fishes.indexOf(t.obj);
          if (idx >= 0) this.fishes.splice(idx, 1);
          if (t.obj && t.obj.id === 'turtle') this.turtleActive = false;
        } else if (t.kind === 'decor') {
          const idx = this.state.decor.indexOf(t.obj);
          if (idx >= 0) this.state.decor.splice(idx, 1);
        }
        this.tempRemovals.splice(i, 1);
      }
    }

    // Dynamic events
    this.eventTimer -= dt;
    if (this.eventTimer <= 0) {
      this.eventTimer = 35 + Math.random() * 35;
      this.triggerEvent(w, h);
    }

    // auto feeder
    if (this.state.upgrades.autoFeed) {
      this.autoFeedTimer += dt;
      if (this.autoFeedTimer > 4) {
        this.autoFeedTimer = 0;
        this.particles.spawnFood(w * (0.2 + Math.random() * 0.6), 20);
      }
    }

    // toast timer
    if (this.toastTimer > 0) {
      this.toastTimer -= dt;
      if (this.toastTimer <= 0) {
        document.getElementById('toast').classList.add('hidden');
      }
    }
  }

  render(t) {
    this.renderer.draw(this, t);
  }

  dropFood(x, y) {
    // Inspect fish if clicked near one
    for (const f of this.fishes) {
      if (Math.hypot(f.x - x, f.y - y) < 18) {
        this.showToast(f.species.name + ' — ' + f.state, false);
        return;
      }
    }
    if (!this.economy.spend(1)) {
      this.showToast('Not enough coins to feed!', true);
      return;
    }
    this.particles.spawnFood(x, y);
  }

  feedButton() {
    // drop a few food pellets at top
    if (!this.economy.spend(1)) {
      this.showToast('Not enough coins to feed!', true);
      return;
    }
    const w = this.logicalW;
    for (let i = 0; i < 3; i++) {
      this.particles.spawnFood(w * (0.2 + Math.random() * 0.6), 10 + i * 4);
    }
  }

  addFish(id) {
    const w = this.logicalW, h = this.logicalH;
    const f = new Fish(id, 40 + Math.random() * (w - 80), 40 + Math.random() * (h * 0.5));
    f.origin = 'player';
    this.fishes.push(f);
    this.state.fish.push(id);
  }

  addDecor(id) {
    const w = this.logicalW, h = this.logicalH;
    const seabedY = h * 0.82;
    const d = { type: id, x: 60 + Math.random() * (w - 120), y: seabedY - 4 + Math.random() * 8, origin: 'player' };
    this.state.decor.push(d);
  }

  triggerEvent(w, h) {
    const seabedY = h * 0.82;
    const r = Math.random();
    if (r < 0.28) {
      // Turtle visit
      if (!this.turtleActive) {
        const f = new Fish('turtle', -50, 40 + Math.random() * (seabedY - 80));
        f.origin = 'growth'; f._temp = true; f.vx = 18 + Math.random() * 10; f.vy = (Math.random() - 0.5) * 4;
        this.fishes.push(f);
        this.tempRemovals.push({ kind: 'fish', obj: f, at: this.simTime + 20 + Math.random() * 10 });
        this.turtleActive = true;
        this.showToast('A sea turtle is visiting!', false);
      }
    } else if (r < 0.52) {
      // School of small fish passes through
      const y = 30 + Math.random() * (seabedY - 60);
      const dir = Math.random() < 0.5 ? 1 : -1;
      const startX = dir > 0 ? -30 : w + 30;
      for (let i = 0; i < 5; i++) {
        const f = new Fish('smallreef', startX + (dir > 0 ? -i * 18 : i * 18), y + (i - 2) * 7);
        f.origin = 'growth'; f._temp = true;
        f.vx = dir * (45 + Math.random() * 15); f.vy = (Math.random() - 0.5) * 3;
        this.fishes.push(f);
        this.tempRemovals.push({ kind: 'fish', obj: f, at: this.simTime + 18 + Math.random() * 6 });
      }
    } else if (r < 0.72) {
      // Small shells scatter on seabed
      for (let i = 0; i < 3; i++) {
        const d = { type: 'shell', x: 40 + Math.random() * (w - 80), y: seabedY - 2, origin: 'growth', _temp: true };
        this.state.decor.push(d);
        this.tempRemovals.push({ kind: 'decor', obj: d, at: this.simTime + 20 + Math.random() * 8 });
      }
    } else if (r < 0.88) {
      // Fish gather: spawn food cluster
      for (let i = 0; i < 5; i++) {
        this.particles.spawnFood(w * (0.35 + Math.random() * 0.3), 15 + i * 4);
      }
    } else {
      // Rare fish swim-by (exotic) if level high enough
      if (this.growthProgression && this.growthProgression.level >= 4) {
        const dir = Math.random() < 0.5 ? 1 : -1;
        const f = new Fish('exotic', dir > 0 ? -40 : w + 40, 40 + Math.random() * (seabedY - 80));
        f.origin = 'growth'; f._temp = true;
        f.vx = dir * (35 + Math.random() * 10);
        this.fishes.push(f);
        this.tempRemovals.push({ kind: 'fish', obj: f, at: this.simTime + 22 + Math.random() * 8 });
        this.showToast('A rare fish passes by!', false);
      }
    }
  }

  openShop() {
    document.getElementById('shop-modal').classList.remove('hidden');
    this.shop.render();
  }

  closeShop() {
    document.getElementById('shop-modal').classList.add('hidden');
  }

  showToast(msg, isError) {
    const t = document.getElementById('toast');
    t.textContent = msg;
    t.classList.remove('hidden', 'success');
    if (!isError) t.classList.add('success');
    this.toastTimer = 2.2;
  }

  save() {
    this.state.coins = this.economy.get();
    this.state.fish = this.fishes.filter(f => f.origin === 'player').map(f => f.id);
    this.state.decor = this.state.decor.filter(d => d.origin === 'player');
    this.state.lastSave = Date.now();
    this.state.simState = {
      fish: this.fishes.map(f => ({
        id: f.id, x: f.x, y: f.y, vx: f.vx, vy: f.vy,
        origin: f.origin, animPhase: f.animPhase
      }))
    };
    saveSave(this.state);
    this.showToast('Game saved!', false);
  }
}
