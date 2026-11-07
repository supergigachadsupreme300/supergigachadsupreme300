export const SPECIES = [
  { id: 'turtle', name: 'Sea Turtle', price: 500, rarity: 'legendary', speed: 14, size: 1.6, color: '#2e7d32', accent: '#a5d6a7', schooling: false, desc: 'Gentle ocean wanderer' },
  { id: 'koi', name: 'Koi', price: 30, rarity: 'common', speed: 28, size: 1.0, color: '#ff8a65', accent: '#fff', schooling: false, desc: 'Calm pond fish' },
  { id: 'clownfish', name: 'Clownfish', price: 40, rarity: 'common', speed: 34, size: 0.85, color: '#ff7043', accent: '#ffffff', schooling: true, desc: 'Orange with white bands' },
  { id: 'bluetang', name: 'Blue Tang', price: 60, rarity: 'uncommon', speed: 36, size: 0.95, color: '#2979ff', accent: '#ffeb3b', schooling: true, desc: 'Bright blue reef fish' },
  { id: 'goldfish', name: 'Goldfish', price: 25, rarity: 'common', speed: 26, size: 0.9, color: '#ffca28', accent: '#ff8f00', schooling: false, desc: 'Classic golden swimmer' },
  { id: 'tropical', name: 'Tropical', price: 80, rarity: 'rare', speed: 40, size: 1.05, color: '#00e676', accent: '#ff4081', schooling: false, desc: 'Striped exotic' },
  { id: 'exotic', name: 'Exotic', price: 150, rarity: 'legendary', speed: 44, size: 1.2, color: '#e040fb', accent: '#00e5ff', schooling: false, desc: 'Rare magical fish' }
];

export function speciesById(id) {
  return SPECIES.find(s => s.id === id);
}

export class Fish {
  constructor(speciesId, x, y) {
    const sp = speciesById(speciesId);
    this.species = sp;
    this.id = speciesId;
    this.x = x;
    this.y = y;
    this.vx = (Math.random() - 0.5) * sp.speed;
    this.vy = (Math.random() - 0.5) * sp.speed * 0.6;
    this.angle = Math.atan2(this.vy, this.vx);
    this.targetAngle = this.angle;
    this.speed = sp.speed;
    this.size = sp.size;
    this.animPhase = Math.random() * Math.PI * 2;
    this.state = 'wander';
    this.wanderTimer = 0;
    this.wanderTarget = { x, y };
    this.eating = 0; // timer
    this.scaleX = 1;
  }

  draw(ctx, t) {
    const sp = this.species;
    const size = 10 * this.size; // pixel units base
    const dir = this.vx >= 0 ? 1 : -1;
    const wag = Math.sin(t * 8 + this.animPhase) * 0.35;

    if (this.id === 'turtle') {
      ctx.save();
      ctx.translate(this.x, this.y);
      ctx.scale(dir, 1);
      // shell
      ctx.fillStyle = '#388e3c';
      ctx.beginPath();
      ctx.ellipse(0, 0, size * 1.1, size * 0.7, 0, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#2e7d32';
      ctx.beginPath();
      ctx.ellipse(0, 0, size * 0.9, size * 0.55, 0, 0, Math.PI * 2);
      ctx.fill();
      // pattern
      ctx.strokeStyle = '#1b5e20';
      ctx.lineWidth = 1;
      for (let i = -2; i <= 2; i++) {
        ctx.beginPath();
        ctx.moveTo(i * 4, -size * 0.5);
        ctx.lineTo(i * 4, size * 0.5);
        ctx.stroke();
      }
      // head
      ctx.fillStyle = '#66bb6a';
      ctx.beginPath();
      ctx.arc(size * 0.9, -size * 0.1, size * 0.35, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = '#000';
      ctx.beginPath();
      ctx.arc(size * 1.05, -size * 0.15, 1.5, 0, Math.PI * 2);
      ctx.fill();
      // flippers
      ctx.fillStyle = '#43a047';
      ctx.beginPath();
      ctx.ellipse(-size * 0.4, -size * 0.7, 5, 3, -0.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.ellipse(-size * 0.4, size * 0.7, 5, 3, 0.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.ellipse(size * 0.4, -size * 0.7, 5, 3, 0.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.beginPath();
      ctx.ellipse(size * 0.4, size * 0.7, 5, 3, -0.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();
      return;
    }

    ctx.save();
    ctx.translate(this.x, this.y);
    ctx.scale(dir, 1);

    // tail
    ctx.fillStyle = sp.accent;
    ctx.beginPath();
    const tailWag = wag * 6;
    ctx.moveTo(-size * 0.9, 0);
    ctx.lineTo(-size * 1.5, -size * 0.5 + tailWag);
    ctx.lineTo(-size * 1.5, size * 0.5 + tailWag);
    ctx.closePath();
    ctx.fill();

    // body
    ctx.fillStyle = sp.color;
    ctx.beginPath();
    ctx.ellipse(0, 0, size, size * 0.55, 0, 0, Math.PI * 2);
    ctx.fill();

    // belly highlight
    ctx.fillStyle = 'rgba(255,255,255,0.25)';
    ctx.beginPath();
    ctx.ellipse(0, size * 0.15, size * 0.7, size * 0.25, 0, 0, Math.PI * 2);
    ctx.fill();

    // stripes depending on species
    if (this.id === 'clownfish') {
      ctx.fillStyle = '#ffffff';
      ctx.fillRect(-size * 0.3, -size * 0.5, 3, size);
      ctx.fillRect(size * 0.2, -size * 0.5, 3, size);
    } else if (this.id === 'tropical') {
      ctx.fillStyle = sp.accent;
      for (let s = -1; s <= 1; s++) {
        ctx.fillRect(s * size * 0.35, -size * 0.4, 2, size * 0.8);
      }
    } else if (this.id === 'exotic') {
      ctx.fillStyle = sp.accent;
      ctx.beginPath();
      ctx.arc(0, 0, size * 0.4, 0, Math.PI * 2);
      ctx.fill();
      ctx.fillStyle = sp.color;
      ctx.beginPath();
      ctx.arc(0, 0, size * 0.2, 0, Math.PI * 2);
      ctx.fill();
    } else if (this.id === 'bluetang') {
      ctx.fillStyle = sp.accent;
      ctx.fillRect(size * 0.1, -size * 0.15, 4, 4);
    }

    // dorsal fin
    ctx.fillStyle = sp.accent;
    ctx.beginPath();
    ctx.moveTo(-size * 0.2, -size * 0.5);
    ctx.lineTo(0, -size * 0.9);
    ctx.lineTo(size * 0.3, -size * 0.5);
    ctx.closePath();
    ctx.fill();

    // eye
    ctx.fillStyle = '#fff';
    ctx.beginPath();
    ctx.arc(size * 0.45, -size * 0.1, 3, 0, Math.PI * 2);
    ctx.fill();
    ctx.fillStyle = '#000';
    ctx.beginPath();
    ctx.arc(size * 0.5, -size * 0.1, 1.5, 0, Math.PI * 2);
    ctx.fill();

    // mouth
    ctx.strokeStyle = '#000';
    ctx.lineWidth = 1;
    ctx.beginPath();
    ctx.arc(size * 0.85, 0, 1.5, -0.6, 0.6);
    ctx.stroke();

    // eating effect
    if (this.eating > 0) {
      ctx.fillStyle = 'rgba(255,255,255,0.6)';
      ctx.beginPath();
      ctx.arc(size * 0.9, 0, 2 + (0.5 - this.eating) * 4, 0, Math.PI * 2);
      ctx.fill();
    }

    ctx.restore();
  }
}
