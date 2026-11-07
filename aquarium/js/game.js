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

    this.fishes = this.state.fish.map((id, idx) => {
      const f = new Fish(id, 60 + (idx % 5) * 40, 60 + Math.floor(idx / 5) * 40);
      f.origin = 'player';
      return f;
    });

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
    this.particles.update(dt, w, h);
    const eaten = updateFishes(this.fishes, dt, w, h, this.particles);
    if (eaten > 0) {
      this.economy.add(eaten * 3);
      this.showToast('Fish fed! +' + (eaten * 3) + ' coins', false);
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
    // Persist only player-owned entities; growth baseline is regenerated.
    this.state.fish = this.fishes.filter(f => f.origin === 'player').map(f => f.id);
    this.state.decor = this.state.decor.filter(d => d.origin === 'player');
    saveSave(this.state);
    this.showToast('Game saved!', false);
  }
}
