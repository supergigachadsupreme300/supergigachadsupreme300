const fs = require('fs');
const path = require('path');

const TOKEN = process.env.AQUARIUM_GITHUB_TOKEN;
const USERNAME = process.env.AQUARIUM_GITHUB_USERNAME;

if (!TOKEN) { console.error('Missing AQUARIUM_GITHUB_TOKEN'); process.exit(1); }
if (!USERNAME) { console.error('Missing AQUARIUM_GITHUB_USERNAME'); process.exit(1); }

const ROOT = process.cwd();
const STATE_PATH = path.join(ROOT, 'aquarium', 'aquarium-state.json');
const CONFIG_PATH = path.join(ROOT, 'aquarium', 'growth-config.json');
const README_PATH = path.join(ROOT, 'README.md');

async function gql(query, variables) {
  const res = await fetch('https://api.github.com/graphql', {
    method: 'POST',
    headers: {
      'Authorization': `bearer ${TOKEN}`,
      'Content-Type': 'application/json',
      'User-Agent': 'aquarium-sync'
    },
    body: JSON.stringify({ query, variables })
  });
  if (!res.ok) {
    const txt = await res.text();
    throw new Error(`GraphQL HTTP ${res.status}: ${txt}`);
  }
  const json = await res.json();
  if (json.errors) {
    throw new Error('GraphQL errors: ' + JSON.stringify(json.errors));
  }
  return json.data;
}

async function main() {
  // 1. Get user createdAt
  const userQuery = `
    query($login: String!) {
      user(login: $login) {
        createdAt
        login
      }
    }
  `;
  const userData = await gql(userQuery, { login: USERNAME });
  if (!userData || !userData.user) throw new Error('User not found: ' + USERNAME);
  const createdAt = new Date(userData.user.createdAt);
  const login = userData.user.login;

  const now = new Date();
  const startYear = createdAt.getFullYear();
  const endYear = now.getFullYear();

  // 2. Loop years
  const yearlyBreakdown = {};
  let lifetime = 0;
  for (let y = startYear; y <= endYear; y++) {
    const from = `${y}-01-01T00:00:00Z`;
    const toYear = y === endYear ? now : new Date(y, 11, 31, 23, 59, 59);
    const to = toYear.toISOString();
    const q = `
      query($login: String!, $from: DateTime!, $to: DateTime!) {
        user(login: $login) {
          contributionsCollection(from: $from, to: $to) {
            contributionCalendar {
              totalContributions
            }
          }
        }
      }
    `;
    const data = await gql(q, { login: USERNAME, from, to });
    const total = data.user.contributionsCollection.contributionCalendar.totalContributions || 0;
    yearlyBreakdown[String(y)] = total;
    lifetime += total;
    // small delay to be nice
    await new Promise(r => setTimeout(r, 200));
  }

  // 3. Load config for level
  let config = null;
  try { config = JSON.parse(fs.readFileSync(CONFIG_PATH, 'utf8')); } catch (e) { config = { levels: [{ min: 0, level: 1, name: 'Seedling Tank' }] }; }
  const levels = config.levels || [{ min: 0, level: 1, name: 'Seedling Tank' }];
  let chosen = levels[0];
  for (const l of levels) {
    if (lifetime >= l.min) chosen = l;
    else break;
  }

  // 4. Write state
  const state = {
    username: login,
    generatedAt: new Date().toISOString(),
    lifetimeContributions: lifetime,
    yearlyBreakdown,
    level: chosen.level,
    levelName: chosen.name
  };
  fs.mkdirSync(path.dirname(STATE_PATH), { recursive: true });
  fs.writeFileSync(STATE_PATH, JSON.stringify(state, null, 2) + '\n');

  // 5. Update README markers
  try {
    let readme = fs.readFileSync(README_PATH, 'utf8');
    const startMarker = '<!-- AQUARIUM:START -->';
    const endMarker = '<!-- AQUARIUM:END -->';
    const block = `${startMarker}\n**Lifetime contributions:** ${lifetime}  \n**Ecosystem level:** ${chosen.level} - ${chosen.name}\n${endMarker}`;
    if (readme.includes(startMarker) && readme.includes(endMarker)) {
      const re = new RegExp(startMarker + '[\\s\\S]*?' + endMarker, 'm');
      readme = readme.replace(re, block);
    } else {
      readme = block + '\n\n' + readme;
    }
    fs.writeFileSync(README_PATH, readme);
  } catch (e) {
    console.warn('README update failed', e);
  }

  console.log('Lifetime contributions:', lifetime);
  console.log('Level:', chosen.level, chosen.name);
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
