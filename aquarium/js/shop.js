import { SPECIES, APPROVED_SPECIES } from './fish.js';

const DECOR_ITEMS = [
  { id: 'coral', name: 'Coral', price: 40, desc: 'Colorful reef coral' },
  { id: 'rock', name: 'Rock', price: 20, desc: 'Smooth stone' },
  // treasure removed per user request
  { id: 'shipwreck', name: 'Shipwreck', price: 200, desc: 'Old wooden wreck' },
  { id: 'shell', name: 'Shell', price: 15, desc: 'Pretty seashell' },
  { id: 'seaweed', name: 'Seaweed', price: 10, desc: 'Green kelp' },
  { id: 'plant', name: 'Plant', price: 15, desc: 'Aquatic plant' }
];

const UPGRADE_ITEMS = [
  { id: 'capacity', name: 'Capacity +2', price: 100, desc: 'Hold more fish' },
  { id: 'autoFeed', name: 'Auto-Feeder', price: 250, desc: 'Drops food periodically' }
];

export class Shop {
  constructor(game) {
    this.game = game;
    this.tab = 'fish';
    this.content = document.getElementById('shop-content');
    this.tabs = document.querySelectorAll('.tab-btn');
    this.tabs.forEach(btn => {
      btn.addEventListener('click', () => {
        this.tabs.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        this.tab = btn.dataset.tab;
        this.render();
      });
    });
  }

  render() {
    this.content.innerHTML = '';
    if (this.tab === 'fish') {
      for (const sp of SPECIES.filter(s => APPROVED_SPECIES.includes(s.id))) {
        this.content.appendChild(this.makeItem(sp.name, sp.price, sp.desc, () => this.buyFish(sp.id), sp.rarity));
      }
    } else if (this.tab === 'decor') {
      for (const d of DECOR_ITEMS) {
        this.content.appendChild(this.makeItem(d.name, d.price, d.desc, () => this.buyDecor(d.id)));
      }
    } else {
      for (const u of UPGRADE_ITEMS) {
        const owned = (u.id === 'autoFeed') ? this.game.state.upgrades.autoFeed : false;
        const label = owned ? 'OWNED' : u.name;
        this.content.appendChild(this.makeItem(label, u.price, u.desc, () => this.buyUpgrade(u.id), null, owned));
      }
    }
  }

  makeItem(name, price, desc, onBuy, rarity, disabled = false) {
    const div = document.createElement('div');
    div.className = 'shop-item';
    div.innerHTML = `
      <div class="item-name">${name}${rarity ? ' [' + rarity + ']' : ''}</div>
      <div class="item-desc">${desc}</div>
      <div class="item-price">${price} coins</div>
      <button class="pixel-btn small" ${disabled ? 'disabled' : ''}>BUY</button>
    `;
    const btn = div.querySelector('button');
    btn.addEventListener('click', onBuy);
    if (disabled) btn.disabled = true;
    return div;
  }

  buyFish(id) {
    const sp = SPECIES.find(s => s.id === id);
    if (!sp) return;
    if (this.game.state.fish.length >= this.game.state.upgrades.capacity) {
      this.game.showToast('Aquarium full! Upgrade capacity.', true);
      return;
    }
    if (!this.game.economy.spend(sp.price)) {
      this.game.showToast('Not enough coins!', true);
      return;
    }
    this.game.addFish(id);
    this.game.showToast('Added ' + sp.name + '!', false);
  }

  buyDecor(id) {
    const item = DECOR_ITEMS.find(d => d.id === id);
    if (!item) return;
    if (!this.game.economy.spend(item.price)) {
      this.game.showToast('Not enough coins!', true);
      return;
    }
    this.game.addDecor(id);
    this.game.showToast('Placed ' + item.name + '!', false);
  }

  buyUpgrade(id) {
    if (id === 'capacity') {
      const price = 100;
      if (!this.game.economy.spend(price)) { this.game.showToast('Not enough coins!', true); return; }
      this.game.state.upgrades.capacity += 2;
      this.game.showToast('Capacity increased!', false);
    } else if (id === 'autoFeed') {
      if (this.game.state.upgrades.autoFeed) { this.game.showToast('Already owned.', true); return; }
      const price = 250;
      if (!this.game.economy.spend(price)) { this.game.showToast('Not enough coins!', true); return; }
      this.game.state.upgrades.autoFeed = true;
      this.game.showToast('Auto-Feeder enabled!', false);
    }
    this.render();
  }
}
