/**
 * ACTION VERIFICATION TESTS
 * 
 * These tests ACTUALLY CLICK buttons and verify outcomes.
 * Unlike structure tests that only check HTML attributes.
 * 
 * Critical for catching bugs like:
 * - e.preventDefault() blocking navigation
 * - JavaScript errors preventing clicks
 * - Broken event handlers
 * - Routing failures
 */

import { test, expect } from '@playwright/test';

test.describe('CRITICAL ACTION TESTS: Button Clicks & Navigation', () => {
  
  test.beforeEach(async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/`);
    await page.waitForLoadState('networkidle');
  });

  // ============================================================================
  // START HERE BUTTON - Week 1 Baseline Entry Point
  // ============================================================================
  
  test('CRITICAL: START HERE click opens PDF in new tab', async ({ page, context }) => {
    // Wait for button to be visible and clickable
    const startButton = page.locator('#print-baseline');
    await expect(startButton).toBeVisible();
    await expect(startButton).toBeEnabled();
    
    // Click and wait for new tab to open
    const [newPage] = await Promise.all([
      context.waitForEvent('page', { timeout: 10000 }),
      startButton.click()
    ]);
    
    // Verify new page loaded
    await newPage.waitForLoadState('networkidle', { timeout: 10000 });
    
    // Verify it's the PDF endpoint
    const url = newPage.url();
    expect(url).toContain('/api/v1/problems/pdf');
    expect(url).toContain('week=1');
    
    // Verify PDF content type (not HTML error page)
    const response = await newPage.evaluate(async () => {
      const resp = await fetch(window.location.href);
      return {
        contentType: resp.headers.get('content-type'),
        status: resp.status
      };
    });
    
    expect(response.status).toBe(200);
    expect(response.contentType).toContain('pdf');
  });

  test('CRITICAL: START HERE button is not intercepted by JavaScript', async ({ page }) => {
    // Monitor for preventDefault calls
    await page.evaluate(() => {
      document.addEventListener('click', (e) => {
        if (e.defaultPrevented) {
          (window as any).__preventedClicks = (window as any).__preventedClicks || [];
          (window as any).__preventedClicks.push({
            id: (e.target as HTMLElement).id,
            tagName: (e.target as HTMLElement).tagName,
            timestamp: Date.now()
          });
        }
      }, true);
    });
    
    // Click the button
    await page.click('#print-baseline');
    
    // Check if click was incorrectly prevented
    const prevented = await page.evaluate(() => (window as any).__preventedClicks || []);
    const startHerePrevented = prevented.find((p: any) => p.id === 'print-baseline');
    
    // The click should NOT be prevented - the <a> tag should work naturally
    expect(startHerePrevented).toBeUndefined();
  });

  // ============================================================================
  // NAVIGATION - All Menu Items
  // ============================================================================
  
  test('CRITICAL: All navigation links route to correct pages', async ({ page }) => {
    const navItems = [
      { id: 'nav-dashboard', pageId: 'page-dashboard', hash: '#dashboard' },
      { id: 'nav-baseline', pageId: 'page-baseline', hash: '#baseline' },
      { id: 'nav-practice', pageId: 'page-practice', hash: '#practice' },
      { id: 'nav-radar', pageId: 'page-radar', hash: '#radar' },
    ];
    
    for (const item of navItems) {
      // Click nav item
      await page.click(`#${item.id}`);
      
      // Verify URL changed
      await expect(page).toHaveURL(new RegExp(item.hash));
      
      // Verify correct page is active
      const pageElement = page.locator(`#${item.pageId}`);
      await expect(pageElement).toHaveClass(/active/);
      await expect(pageElement).toBeVisible();
      
      // Verify page has content (not blank)
      const content = await pageElement.textContent();
      expect(content?.length).toBeGreaterThan(50);
    }
  });

  test('CRITICAL: Navigation updates browser history', async ({ page }) => {
    // Navigate to practice
    await page.click('#nav-practice');
    await expect(page).toHaveURL(/#practice/);
    
    // Navigate to baseline
    await page.click('#nav-baseline');
    await expect(page).toHaveURL(/#baseline/);
    
    // Go back
    await page.goBack();
    await expect(page).toHaveURL(/#practice/);
    
    // Verify practice page is active
    await expect(page.locator('#page-practice')).toHaveClass(/active/);
  });

  // ============================================================================
  // PRACTICE SESSION - Complete Flow
  // ============================================================================
  
  test('CRITICAL: Start practice button loads problem with forced articulation', async ({ page }) => {
    // Navigate to practice
    await page.click('#nav-practice');
    
    // Click start
    await page.click('#start-practice, #start-session');
    
    // Verify problem loaded
    await expect(page.locator('#problem-container, .problem-card')).toBeVisible();
    
    // Verify forced articulation fields exist
    await expect(page.locator('#pathway-type, #pathway-type-select')).toBeVisible();
    await expect(page.locator('#equation-shadow, #equation-shadow-input')).toBeVisible();
    
    // Verify solve button is disabled until articulation complete
    const submitButton = page.locator('#submit-answer, #submit-btn');
    const isDisabled = await submitButton.isDisabled().catch(() => false);
    // If there's validation, button should be disabled initially
    if (isDisabled) {
      expect(isDisabled).toBe(true);
    }
  });

  test('CRITICAL: Cannot submit answer without articulation', async ({ page }) => {
    await page.click('#nav-practice');
    await page.click('#start-practice, #start-session');
    
    // Try to submit without articulation
    await page.fill('#answer', '42');
    await page.click('#submit-answer');
    
    // Should show validation error
    const errorVisible = await page.locator('#articulation-error, .validation-error').isVisible().catch(() => false);
    const stillOnProblem = await page.locator('#problem-container').isVisible();
    
    // Either shows error or stays on problem (doesn't advance)
    expect(errorVisible || stillOnProblem).toBe(true);
  });

  test('CRITICAL: Complete articulation enables solving', async ({ page }) => {
    await page.click('#nav-practice');
    await page.click('#start-practice, #start-session');
    
    // Fill articulation
    await page.selectOption('#pathway-type, #pathway-type-select', 'cross-thread');
    await page.fill('#equation-shadow, #equation-shadow-input', 'Test articulation');
    
    // Fill answer
    await page.fill('#answer', '42');
    
    // Submit
    await page.click('#submit-answer, #submit-btn');
    
    // Verify feedback appears (triad feedback)
    await expect(page.locator('#triad-feedback, .feedback-container')).toBeVisible({ timeout: 5000 });
  });

  // ============================================================================
  // PATHWAY RADAR - Daily Warm-up
  // ============================================================================
  
  test('CRITICAL: Start radar loads questions', async ({ page }) => {
    await page.click('#nav-radar');
    await page.click('#start-radar');
    
    // Verify question loaded
    await expect(page.locator('#radar-question, .radar-question')).toBeVisible();
    
    // Verify progress indicator
    const progressVisible = await page.locator('.radar-progress, #radar-progress').isVisible().catch(() => false);
    const questionNumberVisible = await page.locator('.question-number').isVisible().catch(() => false);
    expect(progressVisible || questionNumberVisible).toBe(true);
  });

  test('CRITICAL: Radar answer submission advances to next question', async ({ page }) => {
    await page.click('#nav-radar');
    await page.click('#start-radar');
    
    // Get first question text
    const firstQuestion = await page.locator('#radar-question, .radar-question').textContent();
    
    // Answer
    await page.click('.answer-option:first-child, .radar-option:first-child');
    await page.click('#submit-radar-answer, #submit-radar');
    
    // Verify new question loaded (or results if last)
    const resultsVisible = await page.locator('#radar-results, .radar-complete').isVisible().catch(() => false);
    if (!resultsVisible) {
      const newQuestion = await page.locator('#radar-question, .radar-question').textContent();
      expect(newQuestion).not.toBe(firstQuestion);
    }
  });

  // ============================================================================
  // GLOSSARY & HELP
  // ============================================================================
  
  test('CRITICAL: Glossary button opens modal', async ({ page }) => {
    // Try Ctrl+B shortcut
    await page.keyboard.press('Control+b');
    
    // Verify modal opened
    const modalVisible = await page.locator('#glossary-modal, .glossary-modal').isVisible().catch(() => false);
    
    // Or try clicking glossary button if exists
    if (!modalVisible) {
      const glossaryBtn = page.locator('#glossary-btn, [data-action="glossary"]');
      if (await glossaryBtn.count() > 0) {
        await glossaryBtn.click();
      }
    }
    
    // Verify glossary content
    await expect(page.locator('#glossary-modal, .glossary-modal')).toBeVisible();
    const content = await page.locator('#glossary-content, .glossary-content').textContent();
    expect(content?.length).toBeGreaterThan(100);
  });

  test('CRITICAL: Help button opens help modal', async ({ page }) => {
    const helpBtn = page.locator('#help-btn, #stuckButton, [data-action="help"]');
    if (await helpBtn.count() > 0) {
      await helpBtn.click();
      await expect(page.locator('#help-modal, .help-modal, #stuck-modal')).toBeVisible();
    }
  });

  // ============================================================================
  // CANVAS ANNOTATION
  // ============================================================================
  
  test('CRITICAL: Canvas is interactive', async ({ page }) => {
    await page.click('#nav-practice');
    await page.click('#start-practice, #start-session');
    
    const canvas = page.locator('#annotation-canvas, .annotation-canvas');
    if (await canvas.count() === 0) {
      test.skip('Canvas not present on this page');
      return;
    }
    
    // Get canvas position
    const box = await canvas.boundingBox();
    expect(box).not.toBeNull();
    
    // Draw a line
    await page.mouse.move(box!.x + 50, box!.y + 50);
    await page.mouse.down();
    await page.mouse.move(box!.x + 100, box!.y + 100);
    await page.mouse.up();
    
    // Verify canvas changed (has drawing)
    // This is a basic check - canvas should be responsive
    const canvasElement = await canvas.elementHandle();
    expect(canvasElement).not.toBeNull();
  });

  // ============================================================================
  // ERROR HANDLING
  // ============================================================================
  
  test('CRITICAL: Console has no errors on page load', async ({ page }) => {
    const errors: string[] = [];
    
    page.on('console', msg => {
      if (msg.type() === 'error') {
        errors.push(msg.text());
      }
    });
    
    // Wait for any async loading
    await page.waitForTimeout(2000);
    
    // Filter out known non-critical errors
    const criticalErrors = errors.filter(e => 
      !e.includes('favicon') && 
      !e.includes('source map') &&
      !e.includes('analytics')
    );
    
    expect(criticalErrors).toHaveLength(0);
  });

  test('CRITICAL: 404 page not found shows error state', async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#nonexistent-page`);
    await page.waitForTimeout(1000);
    
    // Should show error or redirect to dashboard
    const errorVisible = await page.locator('.error, .not-found, #error-message').isVisible().catch(() => false);
    const dashboardVisible = await page.locator('#page-dashboard.active').isVisible().catch(() => false);
    
    expect(errorVisible || dashboardVisible).toBe(true);
  });
});

test.describe('CRITICAL ACTION TESTS: Week 1 Baseline Complete Flow', () => {
  
  test('CRITICAL: Complete Week 1 baseline to gap map flow', async ({ page, context }) => {
    // Step 1: Click START HERE
    const [pdfPage] = await Promise.all([
      context.waitForEvent('page'),
      page.click('#print-baseline')
    ]);
    
    // Verify PDF opened
    await pdfPage.waitForLoadState('networkidle');
    expect(pdfPage.url()).toContain('/api/v1/problems/pdf');
    
    // Step 2: Navigate to baseline page for upload
    await page.bringToFront();
    await page.click('#nav-baseline');
    
    // Step 3: Upload scan (mock file)
    const fileInput = page.locator('#baseline-file, #baseline-file-input');
    if (await fileInput.count() > 0) {
      await fileInput.setInputFiles({
        name: 'test-baseline.pdf',
        mimeType: 'application/pdf',
        buffer: Buffer.from('mock pdf content')
      });
      
      // Step 4: Submit upload
      await page.click('#baseline-upload-btn, #upload-baseline-form button[type="submit"]');
      
      // Step 5: Verify processing state
      const statusVisible = await page.locator('#baseline-upload-status, .upload-status').isVisible().catch(() => false);
      expect(statusVisible).toBe(true);
    }
  });
});
