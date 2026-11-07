// Detailed pixel-art sprite data.
// Each sprite: array of strings (rows). '.' = transparent.
// Render with drawSprite() (nearest-neighbor, crisp).

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
  return { w: rows.reduce((m, r) => Math.max(m, r.length), 0), h: rows.length };
}

// ---------- Palettes ----------
export const PAL = {
  clown: { O:'#ff6f3c', D:'#d84315', W:'#ffffff', K:'#1a1a1a', Y:'#ffc107', L:'#ffab91' },
  tang:  { B:'#1e88e5', D:'#0d47a1', Y:'#ffeb3b', K:'#1a1a1a', W:'#ffffff', L:'#64b5f6' },
  angel: { P:'#f48fb1', D:'#c2185b', Y:'#ffeb3b', K:'#1a1a1a', W:'#ffffff', L:'#f8bbd0' },
  butter:{ Y:'#ffeb3b', D:'#f9a825', B:'#1a237e', K:'#1a1a1a', W:'#ffffff', O:'#ff8f00' },
  puffer:{ Y:'#fff59d', D:'#c0ca33', P:'#f48fb1', K:'#1a1a1a', W:'#ffffff', G:'#795548' },
  koi:   { O:'#ff8a65', D:'#d84315', W:'#ffffff', K:'#1a1a1a', R:'#bf360c', Y:'#ffca28' },
  lion:  { R:'#e53935', D:'#b71c1c', W:'#ffffff', K:'#1a1a1a', Y:'#ffca28', O:'#ff7043' },
  small: { C:'#26c6da', D:'#00838f', Y:'#ffee58', K:'#1a1a1a', W:'#ffffff' },
  turtle:{ G:'#2e7d32', L:'#66bb6a', D:'#1b5e20', K:'#1a1a1a', Y:'#fff176' }
};

// ---------- Fish sprites (facing right; tail on left) ----------
// Each is an array of 2 frames.

export const FISH_SPRITES = {
  clownfish: {
    palette: PAL.clown,
    frames: [
      // frame 0 - tail mid
      [
        "......................",
        ".....KKKK.............",
        "....KOOOOK............",
        "...KOOOOOOK...........",
        "..KOOOOOOOOK..........",
        ".KOOOOOOOOOOK.........",
        "KOOOOOOOOOOOOK........",
        "KWWWOOOOOOOOOOK.......",
        "KWWWOOOOOOOOOOK.......",
        "KWWWOOOOOOOOOOK.......",
        "KOOOOOOOOOOOOK........",
        ".KOOOOOOOOOOK.........",
        "..KOOOOOOOOK..........",
        "...KOOOOOOK...........",
        "....KOOOOK............",
        ".....KKKK............."
      ],
      // frame 1 - tail up
      [
        ".....KKKK.............",
        "....KOOOOK............",
        "...KOOOOOOK...........",
        "..KOOOOOOOOK..........",
        ".KOOOOOOOOOOK.........",
        "KOOOOOOOOOOOOK........",
        "KWWWOOOOOOOOOOK.......",
        "KWWWOOOOOOOOOOK.......",
        "KWWWOOOOOOOOOOK.......",
        "KOOOOOOOOOOOOK........",
        ".KOOOOOOOOOOK.........",
        "..KOOOOOOOOK..........",
        "...KOOOOOOK...........",
        "....KOOOOK............",
        ".....KKKK.............",
        "......................"
      ]
    ]
  },

  bluetang: {
    palette: PAL.tang,
    frames: [
      [
        "......................",
        ".....KKKK.............",
        "....KBBB BK...........",
        "...KBBBBBBK...........",
        "..KBBBBBBBBK..........",
        ".KBBBBBBBBBBK.........",
        "KBBBBBBBBBBBBK........",
        "KBBBBBBBBBBBBBK.......",
        "KBBBBBBBBBBBBBK.......",
        "KBBBBBBBBBBBBK........",
        ".KBBBBBBBBBBK.........",
        "..KBBBBBBBBK..........",
        "...KBBBBBBK...........",
        "....KBBB BK...........",
        ".....KKKK.............",
        "......................"
      ],
      [
        ".....KKKK.............",
        "....KBBB BK...........",
        "...KBBBBBBK...........",
        "..KBBBBBBBBK..........",
        ".KBBBBBBBBBBK.........",
        "KBBBBBBBBBBBBK........",
        "KBBBBBBBBBBBBBK.......",
        "KBBBBBBBBBBBBBK.......",
        "KBBBBBBBBBBBBK........",
        ".KBBBBBBBBBBK.........",
        "..KBBBBBBBBK..........",
        "...KBBBBBBK...........",
        "....KBBB BK...........",
        ".....KKKK.............",
        "......................",
        "......................"
      ]
    ]
  }
};

// Note: additional species sprites to be added.
// For now, missing species fall back to a generic detailed fish renderer in fish.js.
export default FISH_SPRITES;
