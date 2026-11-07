// Pixel-art sprite data and rendering helpers.
// Sprites are stored as arrays of strings (rows) where each char maps to a palette entry.
// '.' is always transparent.

export function drawSprite(ctx, rows, palette, x, y, scale = 1, flipX = false) {
  if (!rows) return;
  const h = rows.length;
  const w = rows.reduce((m, r) => Math.max(m, r.length), 0);
  for (let ry = 0; ry < h; ry++) {
    const row = rows[ry] || '';
    for (let rx = 0; rx < row.length; rx++) {
      const ch = row[rx];
      if (ch === '.' || ch === ' ') continue;
      const color = palette[ch];
      if (!color) continue;
      const px = flipX ? (w - 1 - rx) : rx;
      ctx.fillStyle = color;
      ctx.fillRect(x + px * scale, y + ry * scale, scale, scale);
    }
  }
}

export function spriteSize(rows) {
  const h = rows.length;
  const w = rows.reduce((m, r) => Math.max(m, r.length), 0);
  return { w, h };
}

// ---- Palettes ----
export const P = {
  clown: { O: '#ff7043', W: '#ffffff', B: '#1a1a1a', Y: '#ffca28', D: '#bf360c' },
  angel: { B: '#f8bbd0', W: '#ffffff', D: '#c2185b', Y: '#ffeb3b', K: '#1a1a1a', L: '#fce4ec' },
  butter: { Y: '#ffeb3b', B: '#1a237e', W: '#ffffff', O: '#ff8f00', K: '#1a1a1a' },
  tang: { B: '#2979ff', Y: '#ffeb3b', K: '#1a1a1a', D: '#0d47a1', W: '#ffffff' },
  koi: { O: '#ff8a65', W: '#ffffff', K: '#1a1a1a', R: '#d84315', Y: '#ffca28' },
  puffer: { Y: '#fff59d', W: '#ffffff', K: '#1a1a1a', G: '#9e9d24', P: '#f48fb1', D: '#5d4037' },
  tropical: { G: '#00e676', P: '#ff4081', W: '#ffffff', K: '#1a1a1a', D: '#00897b' },
  small: { C: '#4dd0e1', Y: '#ffee58', K: '#1a1a1a', W: '#ffffff' },
  turtle: { G: '#2e7d32', L: '#66bb6a', D: '#1b5e20', K: '#1a1a1a', Y: '#fff176' }
};

// ---- Fish sprites (2 frames each: tail left / tail right) ----
// Frame width ~26, height ~12

export const FISH = {
  clownfish: {
    palette: P.clown,
    frames: [
      [
        "..........................",
        ".......OOOOO..............",
        ".....OOOOOOOOO............",
        "....OOOOOOOOOOO...........",
        "...OOOOOOOOOOOOO..........",
        "..OOOOOOOOOOOOOOO.........",
        "..OOOOOOOOOOOOOOO.........",
        "..OOOOOOOOOOOOOOO.........",
        "...OOOOOOOOOOOOO..........",
        "....OOOOOOOOOOO...........",
        ".....OOOOOOOOO............",
        ".......OOOOO.............."
      ],
      [
        "..........................",
        ".......OOOOO..............",
        ".....OOOOOOOOO............",
        "....OOOOOOOOOOO...........",
        "...OOOOOOOOOOOOO..........",
        "..OOOOOOOOOOOOOOO.........",
        "..OOOOOOOOOOOOOOO.........",
        "..OOOOOOOOOOOOOOO.........",
        "...OOOOOOOOOOOOO..........",
        "....OOOOOOOOOOO...........",
        ".....OOOOOOOOO............",
        ".......OOOOO.............."
      ]
    ],
    // stripes overlay drawn separately
    stripes: true
  }
};

// Because hand-crafting many frames is huge, we instead build detailed fish
// procedurally with a richer multi-part renderer (see fish.js). The sprite
// system above is used for small decorative elements and coral.

export const CORAL_SPRITES = {};
export const PLANT_SPRITES = {};
export const DECOR_SPRITES = {};
