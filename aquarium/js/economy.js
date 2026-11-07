export class Economy {
  constructor(startCoins = 50) {
    this.coins = startCoins;
    this.listeners = [];
  }
  get() { return this.coins; }
  set(v) { this.coins = Math.max(0, Math.floor(v)); this._emit(); }
  add(n) { this.coins = Math.max(0, this.coins + Math.floor(n)); this._emit(); }
  spend(n) {
    n = Math.floor(n);
    if (n <= 0) return true;
    if (this.coins < n) return false;
    this.coins -= n;
    this._emit();
    return true;
  }
  canAfford(n) { return this.coins >= Math.floor(n); }
  onChange(fn) { this.listeners.push(fn); }
  _emit() { this.listeners.forEach(fn => fn(this.coins)); }
}
