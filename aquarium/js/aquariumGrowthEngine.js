import { Fish } from './fish.js';

const STATE_URL = 'aquarium-state.json';
const CONFIG_URL = 'growth-config.json';
const CACHE_KEY = 'aquariumStateCache_v1';

export class AquariumGrowthEngine {
  constructor() {
    this.config = null;
    this.state = null; // contribution state
    this.progression = null;
    this.ready = false;
  }

  async init() {
    await this.loadConfig();
    await this.loadState();
    this.computeProgression();
    this.ready = true;
    return this.progression;
  }

  async loadConfig() {
    try {
      const res = await fetch(CONFIG_URL, { cache: 'no-store' });
      if (!res.ok) throw new Error('config fetch ' + res.status);
      this.config = await res.json();
    } catch (e) {
      console.warn('Growth config load failed, using defaults', e);
      this.config = this.defaultConfig();
    }
  }

  defaultConfig() {
    return {
      version: 1,
      levels: [{ min: 0, level: 1, name: 'Seedling Tank' }],
      progression: { fishRate: 0.06, maxBaselineFish: 36, coralRate: 0.025, maxCoral: 14, plantRate: 0.035, maxPlant: 18, decorRate: 0.015, maxDecor: 10 },
      milestones: [],
      speciesPool: ['koi', 'goldfish']
    };
  }

  async loadState() {
    // Try network first
    try {
      const res = await fetch(STATE_URL, { cache: 'no-store' });
      if (!res.ok) throw new Error('state fetch ' + res.status);
      const data = await res.json();
      if (!data || typeof data.lifetimeContributions !== 'number') throw new Error('invalid state');
      this.state = data;
      try { localStorage.setItem(CACHE_KEY, JSON.stringify(data)); } catch (e) {}
      return;
    } catch (e) {
      console.warn('Aquarium state load failed, trying cache', e);
    }
    // Fallback cache
    try {
      const cached = localStorage.getItem(CACHE_KEY);
      if (cached) {
        const data = JSON.parse(cached);
        if (data && typeof data.lifetimeContributions === 'number') {
          this.state = data;
          return;
        }
      }
    } catch (e) {}
    // Safe default: zero contributions (but mark as fallback, not real)
    this.state = {
      lifetimeContributions: 0,
      yearlyBreakdown: {},
      username: 'unknown',
      generatedAt: null,
      fallback: true
    };
  }

  getLevel(contribs) {
    const levels = (this.config && this.config.levels) || [{ min: 0, level: 1, name: 'Seedling Tank' }];
    let chosen = levels[0];
    for (const l of levels) {
      if (contribs >= l.min) chosen = l;
      else break;
    }
    return chosen;
  }

  computeProgression() {
    const cfg = this.config || this.defaultConfig();
    const p = cfg.progression;
    const contribs = (this.state && typeof this.state.lifetimeContributions === 'number') ? this.state.lifetimeContributions : 0;

    const level = this.getLevel(contribs);
    const unlockedMilestones = (cfg.milestones || []).filter(m => contribs >= m.contributions);
    const unlockedSpecies = new Set(cfg.speciesPool || ['koi', 'goldfish']);
    for (const m of unlockedMilestones) {
      if (m.type === 'species') unlockedSpecies.add(m.unlock);
    }
    const unlockedStructures = unlockedMilestones.filter(m => m.type === 'structure').map(m => m.unlock);

    const clamp = (v, max) => Math.max(0, Math.min(max, v));
    const baselineFish = clamp(Math.floor(contribs * (p.fishRate || 0.06)), p.maxBaselineFish || 36);
    const coralCount = clamp(Math.floor(contribs * (p.coralRate || 0.025)), p.maxCoral || 14);
    const plantCount = clamp(Math.floor(contribs * (p.plantRate || 0.035)), p.maxPlant || 18);
    const decorCount = clamp(Math.floor(contribs * (p.decorRate || 0.015)), p.maxDecor || 10);

    this.progression = {
      lifetimeContributions: contribs,
      yearlyBreakdown: (this.state && this.state.yearlyBreakdown) || {},
      username: (this.state && this.state.username) || 'unknown',
      fallback: !!(this.state && this.state.fallback),
      level: level.level,
      levelName: level.name,
      unlockedSpecies: [...unlockedSpecies],
      unlockedStructures,
      unlockedMilestones: unlockedMilestones.map(m => m.unlock),
      targets: {
        baselineFish,
        coralCount,
        plantCount,
        decorCount
      }
    };
    return this.progression;
  }

  // Apply baseline ecosystem to game without overwriting player state
  apply(game) {
    if (!this.progression) return;
    const prog = this.progression;
    const w = game.logicalW, h = game.logicalH;
    const seabedY = h * 0.82;

    // Baseline fish: ensure count of growth-origin fish reaches target
    const growthFish = game.fishes.filter(f => f.origin === 'growth');
    const needFish = prog.targets.baselineFish - growthFish.length;
    if (needFish > 0) {
      const pool = prog.unlockedSpecies.length ? prog.unlockedSpecies : ['koi', 'goldfish'];
      for (let i = 0; i < needFish; i++) {
        const species = pool[Math.floor(Math.random() * pool.length)];
        const f = new Fish(species, 40 + Math.random() * (w - 80), 40 + Math.random() * (h * 0.5));
        f.origin = 'growth';
        game.fishes.push(f);
      }
    }

    // Baseline decor: coral, seaweed/plant, structures
    const growthDecor = game.state.decor.filter(d => d.origin === 'growth');
    // desired types list
    const desired = [];
    for (let i = 0; i < prog.targets.coralCount; i++) desired.push('coral');
    for (let i = 0; i < prog.targets.plantCount; i++) desired.push(Math.random() < 0.5 ? 'seaweed' : 'plant');
    for (let i = 0; i < prog.targets.decorCount; i++) desired.push('rock');
    for (const s of prog.unlockedStructures) desired.push(s);

    // Add missing decor up to desired count, by type counts
    const countByType = {};
    for (const d of growthDecor) countByType[d.type] = (countByType[d.type] || 0) + 1;
    const desiredCountByType = {};
    for (const t of desired) desiredCountByType[t] = (desiredCountByType[t] || 0) + 1;

    for (const type of Object.keys(desiredCountByType)) {
      const have = countByType[type] || 0;
      const want = desiredCountByType[type];
      const add = Math.max(0, want - have);
      for (let i = 0; i < add; i++) {
        const d = { type, x: 40 + Math.random() * (w - 80), y: seabedY - 4 + Math.random() * 8, origin: 'growth' };
        game.state.decor.push(d);
      }
    }
  }
}

export default AquariumGrowthEngine;
