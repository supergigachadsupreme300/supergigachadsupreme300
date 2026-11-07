const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const { spawnSync } = require('child_process');

(async () => {
  const browser = await chromium.launch({ args: ['--no-sandbox'] });
  const page = await browser.newPage({ viewport: { width: 900, height: 560 } });
  await page.goto('http://localhost:8765/aquarium/', { waitUntil: 'networkidle' });
  await page.waitForTimeout(2500);

  const framesDir = path.join(process.cwd(), 'frames');
  fs.mkdirSync(framesDir, { recursive: true });
  const total = 30;
  for (let i = 0; i < total; i++) {
    await page.screenshot({ path: path.join(framesDir, `frame-${String(i).padStart(3, '0')}.png`) });
    await page.waitForTimeout(100);
  }
  await browser.close();

  const out = path.join(process.cwd(), 'aquarium', 'aquarium-preview.gif');
  const r = spawnSync('ffmpeg', [
    '-y', '-framerate', '10',
    '-i', path.join(framesDir, 'frame-%03d.png'),
    '-vf', 'scale=480:-1:flags=lanczos,split[s0][s1];[s0]palettegen=max_colors=128[p];[s1][p]paletteuse=dither=bayer',
    '-loop', '0', out
  ], { stdio: 'inherit' });

  fs.rmSync(framesDir, { recursive: true, force: true });

  if (r.status !== 0) {
    console.error('ffmpeg failed with code', r.status);
    process.exit(1);
  }
  console.log('GIF written to', out);
})().catch(err => {
  console.error(err);
  process.exit(1);
});
