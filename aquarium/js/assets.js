const BASE = 'assets/sprites/';

const FILES = {
  clownfish: ['clownfish_0.png','clownfish_1.png'],
  bluetang: ['bluetang_0.png','bluetang_1.png'],
  angelfish: ['angelfish_0.png','angelfish_1.png'],
  butterflyfish: ['butterflyfish_0.png','butterflyfish_1.png'],
  pufferfish: ['pufferfish_0.png','pufferfish_1.png'],
  lionfish: ['lionfish_0.png','lionfish_1.png'],
  koi: ['koi_0.png','koi_1.png'],
  smallreef: ['smallreef_0.png','smallreef_1.png'],
  turtle: ['turtle_0.png','turtle_1.png'],
  goldfish: ['goldfish_0.png','goldfish_1.png'],
  tropical: ['tropical_0.png','tropical_1.png'],
  exotic: ['exotic_0.png','exotic_1.png'],
  lionfish: ['lionfish_0.png','lionfish_1.png'],
  coral_branching: ['coral_branching.png'],
  coral_brain: ['coral_brain.png'],
  coral_seafan: ['coral_seafan.png'],
  anemone: ['anemone.png'],
  seaweed: ['seaweed.png'],
  kelp: ['kelp.png'],
  rock: ['rock.png'],
  shell: ['shell.png'],
  treasure: ['treasure.png'],
  shipwreck: ['shipwreck.png']
};

export const ASSETS = {};

export function loadImage(src) {
  return new Promise((resolve, reject) => {
    const img = new Image();
    img.onload = () => resolve(img);
    img.onerror = () => reject(new Error('Failed to load ' + src));
    img.src = BASE + src;
  });
}

export async function loadAssets() {
  const tasks = [];
  for (const key of Object.keys(FILES)) {
    ASSETS[key] = [];
    for (const f of FILES[key]) {
      tasks.push(loadImage(f).then(img => { ASSETS[key].push(img); }));
    }
  }
  await Promise.all(tasks);
  return ASSETS;
}

export function getAsset(key, frame = 0) {
  const arr = ASSETS[key];
  if (!arr || arr.length === 0) return null;
  return arr[frame % arr.length];
}
