export class Interaction {
  constructor(canvas, game) {
    this.canvas = canvas;
    this.game = game;
    this.logical = { w: 0, h: 0, scale: 4 };
    this.dragging = null;

    canvas.addEventListener('pointerdown', (e) => this.onPointerDown(e));
    canvas.addEventListener('pointermove', (e) => this.onPointerMove(e));
    canvas.addEventListener('pointerup', (e) => this.onPointerUp(e));
    canvas.addEventListener('pointercancel', () => { this.dragging = null; });
  }

  setLogical(w, h, scale) {
    this.logical.w = w;
    this.logical.h = h;
    this.logical.scale = scale;
  }

  toLogical(e) {
    const rect = this.canvas.getBoundingClientRect();
    const x = (e.clientX - rect.left) / this.logical.scale;
    const y = (e.clientY - rect.top) / this.logical.scale;
    return { x, y };
  }

  onPointerDown(e) {
    const { x, y } = this.toLogical(e);
    // Drop food on click
    this.game.dropFood(x, y);
  }

  onPointerMove(e) {
    // reserved for dragging decor
  }

  onPointerUp(e) {
    // reserved
  }
}
