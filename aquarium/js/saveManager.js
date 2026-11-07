const KEY = 'pixelAquariumSave_v1';

const DEFAULTS = {
  coins: 50,
  fish: [], // array of species ids
  decor: [], // array of {type, x, y}
  upgrades: { capacity: 6, autoFeed: false },
  settings: { sound: true }
};

export function loadSave() {
  try {
    const raw = localStorage.getItem(KEY);
    if (!raw) return structuredClone(DEFAULTS);
    const parsed = JSON.parse(raw);
    return {
      coins: typeof parsed.coins === 'number' ? parsed.coins : DEFAULTS.coins,
      fish: Array.isArray(parsed.fish) ? parsed.fish : [],
      decor: Array.isArray(parsed.decor) ? parsed.decor : [],
      upgrades: Object.assign({}, DEFAULTS.upgrades, parsed.upgrades || {}),
      settings: Object.assign({}, DEFAULTS.settings, parsed.settings || {})
    };
  } catch (e) {
    console.warn('Save load failed, using defaults', e);
    return structuredClone(DEFAULTS);
  }
}

export function saveSave(data) {
  try {
    localStorage.setItem(KEY, JSON.stringify(data));
    return true;
  } catch (e) {
    console.warn('Save failed', e);
    return false;
  }
}

export { DEFAULTS };
