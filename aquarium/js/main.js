import { Game } from './game.js';

const game = new Game();
game.start();

// Auto-save on page hide
window.addEventListener('pagehide', () => game.save());
window.addEventListener('beforeunload', () => game.save());
