export class Renderer {
  constructor(canvas) {
    this.canvas = canvas;
    this.ctx = canvas.getContext('2d');
  }

  clear(w, h) {
    this.ctx.clearRect(0, 0, w, h);
  }

  draw(game, t) {
    const ctx = this.ctx;
    const w = game.logicalW;
    const h = game.logicalH;
    game.environment.draw(ctx, w, h, t);
    game.environment.drawDecor(ctx, game.state.decor, t);
    // fish
    for (const f of game.fishes) {
      f.draw(ctx, t);
    }
    game.particles.draw(ctx);
  }
}
