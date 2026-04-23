# ATOM-SG MVP Playwright E2E Tests

Comprehensive end-to-end testing suite for the ATOM-SG MVP frontend using Playwright.

## Quick Start

```bash
# Navigate to test directory
cd /ATOM-SG\ Pilot/05-Backend/playwright-tests

# Install dependencies
npm install

# Install Playwright browsers
npm run install:browsers

# Run CRITICAL tests first (the 24 tests that matter most)
npm run test:critical

# Run all tests
npm test

# Run with UI mode for debugging
npm run test:ui

# Run specific browser
npm run test:chromium
npm run test:firefox
npm run test:webkit

# Run visual regression tests
npm run test:visual

# Update visual baselines
npm run test:visual:update
```

## Test Structure

```
playwright-tests/
├── playwright.config.ts      # Playwright configuration
├── package.json              # Dependencies
├── .env.example              # Environment template
├── setup.sh                  # One-command setup
├── README.md                 # This file
└── tests/
    ├── fixtures.ts           # Custom fixtures and page objects
    ├── critical-pilot.spec.ts   # ⭐ CRITICAL: 23 tests that will break the pilot
    ├── navigation.spec.ts    # Navigation bar tests
    ├── dashboard.spec.ts     # Dashboard page tests
    ├── baseline.spec.ts      # Baseline test page tests
    ├── practice.spec.ts      # Daily practice page tests
    ├── glossary.spec.ts      # Glossary modal tests
    ├── api-integration.spec.ts  # API endpoint tests
    └── p0-p1-fixes.spec.ts   # Critical bug fix verification
```

## Test Coverage

### ⭐ CRITICAL PILOT TESTS (23 tests) - **RUN THESE FIRST**

**File:** `tests/critical-pilot.spec.ts`

These tests validate the 4 things that will actually break the pilot:

| Priority | Area | Tests | What It Validates |
|----------|------|-------|-------------------|
| **P1** | Problem Generation | 8 | JSON validity, answer format, pathway matching, banned words, distribution balance, no duplicates, error handling, timeouts |
| **P2** | Scoring Logic | 6 | Gap map accuracy, mastery detection, whitespace handling, currency formatting, timer accuracy, null prevention |
| **P3** | Socratic Feedback | 5 | Hint vs answer, correct feedback, 3-strike solution reveal, Next Problem button, pathway-specific hints |
| **P4** | Data Persistence | 4 | Baseline survive reload, continue from problem 4, transfer comparison, accuracy delta calculation |

**Why these matter:** The existing 67 UI tests tell you the app *renders*. These 23 tests tell you the app *works*.

### UI/Functional Tests (67 tests)

| Area | Tests | Key Features |
|------|-------|--------------|
| **Navigation** | 6 | All nav links, active states, URL hashes |
| **Dashboard** | 7 | Stats, milestones, gamification, API errors |
| **Baseline** | 8 | PDF link, upload, gap map, console monitoring |
| **Practice** | 12 | Canvas, articulation, help modal, triad feedback |
| **Glossary** | 7 | Modal, search, Ctrl+B shortcut |
| **API** | 12 | All endpoints, CORS, error handling |
| **P0/P1 Fixes** | 15+ | All 8 critical fixes verified |

**Total: 90 tests**

## Mock API Layer

To avoid flaky tests and burned API credits, we use a **Mock API Layer** that returns predictable responses:

```typescript
// In critical-pilot.spec.ts
const MOCK_PROBLEMS = {
  'cross-thread': {
    problem: 'A shop sells 3 pens for $5...',
    answer: 20,
    equation_shadow: '3 pens = $5, so 12 pens = ...',
    pathway_type: 'cross-thread',
    hint: 'How many groups of 3 pens are in 12 pens?'
  },
  // ... 4 more pathways
};
```

### Why Mock?
- ✅ **Predictable**: Same response every test run
- ✅ **Fast**: No network latency
- ✅ **Cheap**: No API credits burned
- ✅ **Reliable**: No flakiness from LLM variations

### When to Use Live API?
Only for the separate "Live API Integration" suite:

```bash
# Run live API tests (use sparingly!)
SKIP_LIVE_API=false npm run test
```

## Configuration

### Environment Variables

Copy `.env.example` to `.env` and customize:

```bash
# Target MVP URL
BASE_URL=http://192.168.2.6

# Mock API Mode (default: true)
MOCK_API=true

# Skip Live API Tests (default: true - recommended for CI)
SKIP_LIVE_API=true

# CI Mode
CI=false
```

### Playwright Config

- **Browsers**: Chromium, Firefox, WebKit
- **Mobile**: Pixel 5, iPhone 12
- **Retries**: 2 on CI, 0 locally
- **Workers**: 1 on CI, auto locally
- **Screenshots**: On failure
- **Video**: On first retry
- **Trace**: On first retry

## Running Tests

### Critical Tests Only (Recommended for CI)
```bash
npm run test:critical
```

### Critical Tests with UI
```bash
npm run test:critical:ui
```

### All Tests with Mock API
```bash
npm run test:mock
```

### Live API Tests (Manual Only)
```bash
npm run test:live
```

### Debug Mode
```bash
npm run test:debug
```

### View Report
```bash
npm run report
```

## Critical Test Details

### P1: Problem Generation (8 tests)

| Test | Assertion |
|------|-----------|
| 1.1 | Response has problem, answer, equation_shadow, pathway_type fields |
| 1.2 | Answer is clean integer or decimal (≤2 places) |
| 1.3 | pathway_type matches requested pathway |
| 1.4 | No banned words ("rest", "remainder", "left") in problem text |
| 1.5 | 20 sequential requests all return valid JSON |
| 1.6 | Distribution is balanced (4 per pathway type) |
| 1.7 | No two problems have identical text |
| 1.8 | Malformed API response shows error state, not blank screen |
| 1.9 | API timeout shows error, not infinite spinner |

### P2: Scoring Logic (6 tests)

| Test | Assertion |
|------|-----------|
| 2.1 | 1/4 correct shows "Gap" in gap map with 25% accuracy |
| 2.2 | 3/4 correct shows "Mastery" in gap map |
| 2.3 | Whitespace in answer (" 42 ") is handled correctly |
| 2.4 | Currency formatting ("$42") is handled correctly |
| 2.5 | Timer records per-problem time accurately (4-6s for 5s wait) |
| 2.6 | Timer never records 0 or null |

### P3: Socratic Feedback (5 tests)

| Test | Assertion |
|------|-----------|
| 3.1 | First wrong answer shows hint with question mark, not answer |
| 3.2 | Correct answer shows "correct" and equation shadow |
| 3.3 | Third wrong answer reveals full solution |
| 3.4 | "Next Problem" button appears after solution revealed |
| 3.5 | Socratic hint is pathway-specific |

### P4: Data Persistence (4 tests)

| Test | Assertion |
|------|-----------|
| 4.1 | Baseline results survive page reload (3 completed → still 3) |
| 4.2 | Can continue baseline from problem 4 after reload |
| 4.3 | Transfer test loads baseline for comparison |
| 4.4 | Accuracy delta calculates correctly (+15% shown) |

## CI/CD Integration

### GitHub Actions (Automated)

Tests run automatically on every PR and push to main:

```yaml
# .github/workflows/playwright-tests.yml
name: Playwright Tests
on:
  push:
    branches: [main, master]
  pull_request:
    branches: [main, master]

jobs:
  critical-tests:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '20'
      - run: cd 05-Backend/playwright-tests && npm ci
      - run: cd 05-Backend/playwright-tests && npx playwright install chromium
      - run: cd 05-Backend/playwright-tests && npm run test:critical
```

### Telegram Notifications

Get instant alerts when tests fail:

1. **Setup Bot:** Message [@BotFather](https://t.me/botfather) to create a bot
2. **Get Chat ID:** Add bot to your group, message [@userinfobot](https://t.me/userinfobot) to get the ID
3. **Add Secrets:** Go to GitHub Repository Settings → Secrets → Add:
   - `TELEGRAM_BOT_TOKEN` - Your bot's API token
   - `TELEGRAM_CHAT_ID` - Your group's chat ID (e.g., `-1003889017461`)

See [GITHUB_SECRETS_SETUP.md](../../.github/GITHUB_SECRETS_SETUP.md) for detailed instructions.

### Test Schedule

| Trigger | Tests Run | Time |
|---------|-----------|------|
| Every PR | Critical (24 tests) | ~30s |
| Push to main | Critical + Full suite | ~5min |
| Nightly | All tests + Live API | ~10min |

## Writing New Critical Tests

```typescript
import { test, expect } from './fixtures';

test.describe('CRITICAL: Feature Name', () => {
  test.beforeEach(async ({ page }) => {
    // Set up mock API
    await page.route('**/api/v1/endpoint', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({ predictable: 'response' })
      });
    });
  });

  test('TEST X.Y: Descriptive test name', async ({ page, baseURL }) => {
    // Arrange
    await page.goto(`${baseURL}/#page`);
    
    // Act
    await page.click('#button');
    
    // Assert - be specific about what matters
    await expect(page.locator('#result')).toContainText('expected');
  });
});
```

## Troubleshooting

### Tests failing due to network issues
- Check `BASE_URL` is correct
- Ensure target server is running
- Use `MOCK_API=true` to bypass network

### Element not found
- Increase timeout: `{ timeout: 10000 }`
- Check selector exists in DOM
- Wait for network idle: `await page.waitForLoadState('networkidle')`

### Mock API not working
- Ensure route is set before navigation
- Check URL pattern matches: `**/api/v1/**`
- Verify mock is in `test.beforeEach`

## Visual Regression Testing

Detect unintended UI changes automatically:

```bash
# Run visual regression tests
npm run test:visual

# Update baseline screenshots (after intentional UI changes)
npm run test:visual:update
```

### What Gets Tested

- Full page screenshots (Dashboard, Baseline, Practice)
- Mobile viewport screenshots
- Component screenshots (buttons, forms, modals)
- Error state screenshots

### How It Works

1. First run creates baseline screenshots in `__screenshots__/`
2. Subsequent runs compare new screenshots against baseline
3. Any pixel difference > 20% fails the test
4. CI uploads diffs for review

### Updating Baselines

After intentional UI changes:

```bash
# Update all baselines
UPDATE_SNAPSHOTS=true npm run test:visual

# Or use the npm script
npm run test:visual:update
```

## Maintenance

### Adding New Critical Tests
1. Add to `tests/critical-pilot.spec.ts`
2. Use mock API for predictability
3. Follow naming: `TEST X.Y: Description`
4. Update README table

### Updating Mocks
- Edit `MOCK_PROBLEMS` in `critical-pilot.spec.ts`
- Ensure all 5 pathways have mock data
- Keep responses realistic but predictable

### Visual Test Maintenance
- Baselines stored in `__screenshots__/`
- Review diffs in CI artifacts when tests fail
- Update baselines only for intentional UI changes

## Links

- [Playwright Docs](https://playwright.dev/)
- [Test Plan](../MVP_FRONTEND_FUNCTIONAL_TEST_PLAN.md)
- [P0/P1 Tracking](../../P0-6_TRACKING_COMPLETED.md)
# Smoke test trigger - Sun Apr 19 02:08:57 +08 2026
