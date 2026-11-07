import { Game } from './game.js';
import { loadAssets } from './assets.js';

const params = new URLSearchParams(window.location.search);
const preview = params.get('preview') === '1' || window.location.hash === '#preview';
if (preview) document.body.classList.add('preview-mode');

loadAssets().then(() => {
  const game = new Game();
  game.previewMode = preview;
  game.start();
}).catch(err => {
  console.error('Asset load failed', err);
  const game = new Game();
  game.previewMode = preview;
  game.start();
});

// Auto-save on page hide
window.addEventListener('pagehide', () => game.save());
window.addEventListener('beforeunload', () => game.save());
