# Option A: Fix Properly — Execution Plan

**Decision:** Complete test infrastructure overhaul before launch  
**New Target Launch Date:** 2026-05-03 (1 week delay)  
**Owner:** Zcaethbot (execution), Sean (validation checkpoints)

---

## Phase 1: Immediate Fixes (Today — 2026-04-18)

### 1.1 Verify START HERE Fix (15 min)
- [ ] Sean hard-refreshes and tests START HERE button
- [ ] Confirm PDF opens in new tab
- [ ] If still broken → emergency debug session

### 1.2 Add Missing Action Tests (2 hours)
Create `tests/action-verification.spec.ts`:

```typescript
// Critical button/link action tests
// These actually CLICK and verify outcomes

test('CRITICAL: START HERE opens PDF in new tab', async ({ page, context }) => {
  const [newPage] = await Promise.all([
    context.waitForEvent('page'),
    page.click('#print-baseline')
  ]);
  await newPage.waitForLoadState();
  expect(newPage.url()).toContain('/api/v1/problems/pdf');
});

test('CRITICAL: All nav links route correctly', async ({ page }) => {
  const navItems = ['dashboard', 'baseline', 'practice', 'radar'];
  for (const item of navItems) {
    await page.click(`#nav-${item}`);
    await expect(page).toHaveURL(new RegExp(`#${item}`));
    await expect(page.locator(`#page-${item}`)).toHaveClass(/active/);
  }
});

test('CRITICAL: Practice start button loads problem', async ({ page }) => {
  await page.click('#start-practice');
  await expect(page.locator('#problem-container')).toBeVisible();
  await expect(page.locator('#pathway-type-select')).toBeVisible();
});

test('CRITICAL: Submit answer shows feedback', async ({ page }) => {
  // Complete articulation
  await page.selectOption('#pathway-type', 'cross-thread');
  await page.fill('#equation-shadow', 'test articulation');
  await page.fill('#answer', '42');
  
  // Submit
  await page.click('#submit-answer');
  
  // Verify feedback appears
  await expect(page.locator('#triad-feedback')).toBeVisible();
});
```

### 1.3 Rename Misleading Methods (30 min)
Update `fixtures.ts`:
- `clickPrintBaseline()` → `getPrintBaselineHref()` + `clickAndVerifyPrintBaselineOpensPdf()`
- Audit all page object methods for misleading names

---

## Phase 2: Test Audit (Tomorrow — 2026-04-19)

### 2.1 Categorize All 90 Tests (3 hours)

Create spreadsheet/categories:

| Test File | Test Name | Category | Action Needed |
|-----------|-----------|----------|---------------|
| baseline.spec.ts | should display START HERE button | Structure only | Add action test |
| critical-pilot.spec.ts | TEST 1.1: Valid JSON | API/Mock | Keep |
| ... | ... | ... | ... |

**Categories:**
- **Structure only** — checks HTML/attributes (NEEDS action test added)
- **Action included** — actually clicks/interacts (KEEP)
- **API/Mock** — tests backend integration (KEEP)
- **False positive** — misleading name or insufficient (FIX/REMOVE)

### 2.2 Identify Critical Gaps (1 hour)

Every critical user flow must have action test:

| Flow | Current Coverage | Gap |
|------|-----------------|-----|
| Week 1: Start → PDF → Upload → Gap map | Structure only | Missing action tests |
| Week 2: Radar → Practice → Feedback | Partial | Missing feedback verification |
| Navigation: All menu items | Structure only | Missing click tests |
| Canvas: Draw → Save | Structure only | Missing interaction tests |

---

## Phase 3: Add Action Tests (2026-04-20 to 2026-04-21)

### 3.1 Critical Path Action Tests (4 hours)

Add to `tests/critical-actions.spec.ts`:

```typescript
// Week 1 Baseline Flow
test('CRITICAL: Complete Week 1 baseline workflow', async ({ page, context }) => {
  // 1. Click START HERE
  const [pdfPage] = await Promise.all([
    context.waitForEvent('page'),
    page.click('#print-baseline')
  ]);
  
  // 2. Verify PDF loaded
  await pdfPage.waitForLoadState();
  expect(pdfPage.url()).toContain('/api/v1/problems/pdf');
  
  // 3. Simulate upload
  await page.setInputFiles('#baseline-file', 'test-scan.pdf');
  await page.click('#baseline-upload-btn');
  
  // 4. Verify gap map appears
  await expect(page.locator('#gap-map')).toBeVisible();
  await expect(page.locator('.weak-pathway')).toHaveCount(3);
});

// Week 2 Daily Practice Flow
test('CRITICAL: Complete daily practice session', async ({ page }) => {
  // 1. Start radar
  await page.click('#start-radar');
  await expect(page.locator('#radar-question')).toBeVisible();
  
  // 2. Answer 3 radar questions
  for (let i = 0; i < 3; i++) {
    await page.click('.answer-option:first-child');
    await page.click('#submit-radar-answer');
  }
  
  // 3. Start practice
  await page.click('#start-practice');
  
  // 4. Complete forced articulation
  await page.selectOption('#pathway-type', 'cross-thread');
  await page.fill('#equation-shadow', 'test');
  
  // 5. Solve and submit
  await page.fill('#answer', '42');
  await page.click('#submit-answer');
  
  // 6. Verify feedback
  await expect(page.locator('#triad-feedback')).toBeVisible();
});
```

### 3.2 Navigation Action Tests (2 hours)

```typescript
// tests/navigation-actions.spec.ts
test('CRITICAL: All navigation links work', async ({ page }) => {
  const pages = [
    { nav: 'nav-dashboard', page: 'page-dashboard', url: /#dashboard/ },
    { nav: 'nav-baseline', page: 'page-baseline', url: /#baseline/ },
    { nav: 'nav-practice', page: 'page-practice', url: /#practice/ },
    { nav: 'nav-radar', page: 'page-radar', url: /#radar/ },
  ];
  
  for (const p of pages) {
    await page.click(`#${p.nav}`);
    await expect(page).toHaveURL(p.url);
    await expect(page.locator(`#${p.page}`)).toHaveClass(/active/);
    
    // Verify page content loaded
    const content = await page.locator(`#${p.page}`).textContent();
    expect(content.length).toBeGreaterThan(100);
  }
});
```

### 3.3 Canvas Interaction Tests (2 hours)

```typescript
// tests/canvas-actions.spec.ts
test('CRITICAL: Canvas drawing works', async ({ page }) => {
  await page.goto('/#practice');
  await page.click('#start-practice');
  
  // Draw on canvas
  const canvas = page.locator('#annotation-canvas');
  const box = await canvas.boundingBox();
  
  await page.mouse.move(box.x + 50, box.y + 50);
  await page.mouse.down();
  await page.mouse.move(box.x + 100, box.y + 100);
  await page.mouse.up();
  
  // Verify drawing registered
  const hasDrawing = await page.evaluate(() => {
    const canvas = document.querySelector('#annotation-canvas');
    const ctx = canvas.getContext('2d');
    const pixel = ctx.getImageData(75, 75, 1, 1).data;
    return pixel[3] > 0; // Alpha channel
  });
  
  expect(hasDrawing).toBe(true);
});
```

---

## Phase 4: Validation & Documentation (2026-04-22)

### 4.1 Run Complete Test Suite (2 hours)

```bash
# Run all tests
npm run test

# Verify new action tests pass
npm run test:critical-actions

# Generate coverage report
npm run test:coverage
```

**Target:** 100% critical action tests pass

### 4.2 Update Documentation (1 hour)

- Update `TEST_STRATEGY.md` with action verification layer
- Document new test categories
- Create "Adding New Tests" guide

### 4.3 Hands-On Validation Checklist (1 hour)

Even with better tests, still do hands-on:

| Checkpoint | Owner | Time |
|------------|-------|------|
| Click every button on dashboard | Sean | 10 min |
| Complete Week 1 flow end-to-end | Sean | 15 min |
| Complete Week 2 practice session | Sean | 15 min |
| Test on target device (tablet) | Sean | 10 min |

---

## Phase 5: Go/No-Go Decision (2026-04-22 Evening)

### Criteria for GO

| Criterion | Target | Verification |
|-----------|--------|--------------|
| All action tests pass | 100% | Test report |
| No console errors | 0 | Hands-on check |
| All critical flows work | 100% | Hands-on check |
| Sean signs off | Yes | Explicit confirmation |

### If GO
- Launch 2026-05-03
- Monitor closely Week 1
- Daily check-ins

### If NO-GO
- Identify remaining blockers
- Fix and re-validate
- New target: 2026-05-10

---

## Resource Requirements

| Resource | Hours | Owner |
|----------|-------|-------|
| Add action tests | 10 | Zcaethbot |
| Test audit | 4 | Zcaethbot |
| Run/fix tests | 4 | Zcaethbot |
| Hands-on validation | 1 | Sean |
| Documentation | 2 | Zcaethbot |
| **Total** | **21 hours** | |

---

## Daily Checkpoints

| Date | Checkpoint | Deliverable |
|------|-----------|-------------|
| 4/18 EOD | START HERE fixed, action tests added | Test file committed |
| 4/19 EOD | Test audit complete, gaps identified | Audit report |
| 4/20 EOD | Critical action tests added | Tests passing |
| 4/21 EOD | All action tests complete | Full suite passing |
| 4/22 EOD | **GO/NO-GO Decision** | Launch decision |

---

## Success Metrics

| Metric | Before | After | Target |
|--------|--------|-------|--------|
| Tests that actually click | 0 | 20+ | 100% of critical buttons |
| Test coverage (critical paths) | ~30% | >90% | >90% |
| Hands-on surprises | 1 (major) | 0 | 0 |
| Confidence level | Low | High | High |

---

**Start: Now**  
**End: 2026-04-22 (GO/NO-GO)**  
**Launch (if GO): 2026-05-03**
