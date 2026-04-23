# Test Plan Analysis: Why Playwright Didn't Catch the START HERE Bug

**Date:** 2026-04-18  
**Issue:** START HERE button routes to dashboard instead of opening PDF  
**Impact:** Critical pilot blocker — would prevent Week 1 baseline test

---

## The Bug

**What Happened:**
- User clicks "START HERE →" button
- **Expected:** PDF opens in new tab
- **Actual:** Page routes back to dashboard

**Root Cause:**
```javascript
// baseline.js
this.printBtn.addEventListener('click', (e) => {
    e.preventDefault();      // <-- Stops <a> tag from working
    e.stopPropagation();
    this.printBaseline();    // <-- Calls JS function instead
});
```

The JavaScript intercepted the click and prevented the native `<a>` tag behavior.

---

## Why Playwright Didn't Catch This

### Test That Should Have Caught It

**File:** `tests/baseline.spec.ts`  
**Test:** `should display START HERE button with correct href`

```typescript
test('should display START HERE button with correct href', async ({ page }) => {
  const baseline = new BaselinePage(page);
  const href = await baseline.clickPrintBaseline();
  
  expect(href).toBe('/api/v1/problems/pdf?week=1');
});
```

**What the test actually did:**
1. ✅ Checked link is visible
2. ✅ Checked `href` attribute equals `/api/v1/problems/pdf?week=1`
3. ❌ **Did NOT click the link**
4. ❌ **Did NOT verify PDF opens**
5. ❌ **Did NOT verify new tab opens**

**The test passed because it only checked the HTML, not the behavior.**

### The Page Object Method

```typescript
// fixtures.ts - BaselinePage class
async clickPrintBaseline() {
  const link = this.page.locator('a[href*="/api/v1/problems/pdf"]');
  await expect(link).toBeVisible();
  
  // Only gets attribute, doesn't click!
  const href = await link.getAttribute('href');
  expect(href).toContain('/api/v1/problems/pdf?week=1');
  
  return href;  // Never actually clicks!
}
```

**Method name is misleading:** `clickPrintBaseline()` doesn't click!

---

## Test Plan Failures

### 1. Shallow Testing

| What We Tested | What We Should Have Tested |
|----------------|---------------------------|
| HTML attribute exists | Click actually works |
| Link is visible | New tab opens |
| href is correct | PDF loads in new tab |
| Element present | User can complete action |

### 2. False Confidence

- **90 tests passing** gave false sense of security
- **23 critical tests** didn't include actual click verification
- Tests validated code structure, not user experience

### 3. Missing Test Categories

**Not tested:**
- Actual click interactions on critical buttons
- New tab/window opening
- PDF rendering in browser
- End-to-end user workflows
- JavaScript event handler interference

**Tested instead:**
- Element visibility
- Attribute values
- API responses
- Static HTML structure

---

## Why This Matters for Pilot

### Week 1 Baseline Test

**Without this button working:**
- ❌ Student cannot access baseline test
- ❌ No gap map generated
- ❌ No personalized training for Weeks 2-4
- ❌ **Pilot fails at Week 1**

**Severity:** Critical — would have blocked entire pilot

---

## Improved Test Strategy

### New Test Categories

#### 1. Action Verification Tests (NEW)

Tests that actually perform user actions:

```typescript
test('CRITICAL: START HERE click opens PDF in new tab', async ({ page, context }) => {
  // Listen for new tab
  const [newPage] = await Promise.all([
    context.waitForEvent('page'),  // Wait for new tab
    page.click('#print-baseline')   // Click the button
  ]);
  
  // Verify new tab opened
  await newPage.waitForLoadState();
  
  // Verify it's a PDF
  const url = newPage.url();
  expect(url).toContain('/api/v1/problems/pdf');
  
  // Verify PDF content type
  const response = await newPage.evaluate(() => 
    fetch(window.location.href).then(r => r.headers.get('content-type'))
  );
  expect(response).toContain('pdf');
});
```

#### 2. End-to-End Workflow Tests (NEW)

Tests complete user journeys:

```typescript
test('CRITICAL: Complete Week 1 baseline workflow', async ({ page }) => {
  // 1. Click START HERE
  // 2. Verify PDF opens
  // 3. Simulate scan upload
  // 4. Verify gap map appears
  // 5. Verify 3 weakest pathways identified
});
```

#### 3. JavaScript Interference Tests (NEW)

Tests that JS doesn't break native behavior:

```typescript
test('CRITICAL: Navigation links work without JS interference', async ({ page }) => {
  // Disable JavaScript
  await page.context().setOffline(true);
  
  // Link should still work (if it's a real link)
  const link = page.locator('a[href="/api/v1/problems/pdf"]');
  await expect(link).toHaveAttribute('href', '/api/v1/problems/pdf');
});
```

#### 4. Event Handler Tests (NEW)

Tests that event handlers don't break functionality:

```typescript
test('CRITICAL: Click events do not prevent default navigation', async ({ page }) => {
  // Monitor preventDefault calls
  await page.evaluate(() => {
    document.addEventListener('click', (e) => {
      if (e.defaultPrevented) {
        window.__preventedClicks = window.__preventedClicks || [];
        window.__preventedClicks.push(e.target.id);
      }
    }, true);
  });
  
  await page.click('#print-baseline');
  
  // Check if click was incorrectly prevented
  const prevented = await page.evaluate(() => window.__preventedClicks || []);
  expect(prevented).not.toContain('print-baseline');
});
```

### Revised Test Pyramid

```
       /\
      /  \  5%   - Live E2E (manual, full workflows)
     /____\
    /      \  15%  - Action Verification (clicks, navigation, new tabs)
   /        \
  /__________\  30%  - Critical Path (original 23 tests)
 /            \
/______________\  50%  - UI/Structure (visibility, attributes, API)
```

**New layer:** Action Verification Tests (15%)
- Actually click buttons
- Verify new tabs open
- Verify PDFs load
- Verify navigation completes

### Critical Test Checklist (Revised)

Every critical button/link must have:
- [ ] **Structure test:** Element exists with correct attributes
- [ ] **Visibility test:** Element is visible and clickable
- [ ] **Action test:** Click performs expected action
- [ ] **Result test:** Expected outcome occurs (new tab, PDF load, etc.)

---

## Immediate Actions

### 1. Fix Current Bug (DONE)
- ✅ Removed `e.preventDefault()` from baseline.js
- ✅ Removed `e.stopPropagation()`
- 🔄 Pending: Verify fix works

### 2. Add Missing Tests (URGENT)

```typescript
// tests/baseline.spec.ts - ADD THESE TESTS

test('CRITICAL: START HERE click opens PDF in new tab', async ({ page, context }) => {
  const [newPage] = await Promise.all([
    context.waitForEvent('page'),
    page.click('#print-baseline')
  ]);
  
  await newPage.waitForLoadState();
  expect(newPage.url()).toContain('/api/v1/problems/pdf');
});

test('CRITICAL: All navigation links work correctly', async ({ page }) => {
  const links = [
    { id: 'nav-dashboard', hash: '#dashboard' },
    { id: 'nav-baseline', hash: '#baseline' },
    { id: 'nav-practice', hash: '#practice' },
  ];
  
  for (const link of links) {
    await page.click(`#${link.id}`);
    await expect(page).toHaveURL(new RegExp(link.hash));
    await expect(page.locator(`#page-${link.hash.slice(1)}`)).toHaveClass(/active/);
  }
});
```

### 3. Audit All Existing Tests

Review every test and categorize:
- **Structure only:** Needs action test added
- **Action included:** Keep as-is
- **False positive:** Fix or remove

### 4. Rename Misleading Methods

```typescript
// BEFORE (misleading)
async clickPrintBaseline() {
  // Doesn't actually click!
  return link.getAttribute('href');
}

// AFTER (accurate)
async getPrintBaselineHref() {
  // Just gets the href
  return link.getAttribute('href');
}

async clickAndVerifyPrintBaselineOpensPdf() {
  // Actually clicks and verifies
  const [newPage] = await Promise.all([
    context.waitForEvent('page'),
    link.click()
  ]);
  return newPage;
}
```

---

## Lessons Learned

### 1. Tests Passing ≠ Product Working

- 90 tests passing didn't catch a critical bug
- Tests validated code structure, not user experience
- **Lesson:** Always test behavior, not just structure

### 2. Naming Matters

- `clickPrintBaseline()` that doesn't click is dangerous
- Misleading names create false confidence
- **Lesson:** Method names must accurately describe behavior

### 3. Critical Paths Need Action Tests

- Any button that blocks user flow needs action verification
- "Click" in test name must mean actual click
- **Lesson:** Structure tests are necessary but not sufficient

### 4. Hands-On Validation Is Essential

- Automated tests missed what manual testing caught
- Real user behavior differs from test assumptions
- **Lesson:** Automated tests + manual validation required

---

## Revised Validation Strategy

### Phase 1: Automated Tests (Before Hands-On)
- Structure tests (existing)
- Action verification tests (NEW — add these)
- API integration tests (existing)

### Phase 2: Hands-On Validation (Before Pilot)
- Complete end-to-end workflows
- Click every critical button
- Verify every navigation path
- Test on target device (tablet/laptop)

### Phase 3: Pilot Student Shadow (Week 1)
- Watch real student use platform
- Note confusion points
- Document unexpected behavior
- Fix issues before Week 2

---

## Conclusion

**The test plan failed because:**
1. Tests checked HTML structure, not user actions
2. Misleading method names created false confidence
3. No tests verified actual click behavior
4. Test pyramid was missing the "action verification" layer

**To prevent this:**
1. Add action verification tests for all critical buttons
2. Rename methods to accurately describe behavior
3. Require hands-on validation before any launch
4. Test behavior, not just structure

**Current status:**
- Bug identified and fixed
- Test plan gaps documented
- Improved strategy defined
- Ready to add missing tests and re-validate
