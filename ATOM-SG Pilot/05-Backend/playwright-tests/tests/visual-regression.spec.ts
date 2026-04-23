import { test, expect } from '@playwright/test';

/**
 * Visual Regression Tests
 * Screenshots key pages and compares against baseline
 * Run: npx playwright test tests/visual-regression.spec.ts --update-snapshots
 */

const BASE_URL = process.env.BASE_URL || 'http://192.168.2.6';

// Pages to screenshot
test.describe('Visual Regression - Key Pages', () => {
  
  test('Dashboard page visual check', async ({ page }) => {
    await page.goto(`${BASE_URL}/#dashboard`);
    await page.waitForLoadState('networkidle');
    
    // Wait for content to load
    await page.waitForSelector('#page-dashboard', { state: 'visible' });
    
    // Screenshot the full page
    await expect(page).toHaveScreenshot('dashboard.png', {
      fullPage: true,
      threshold: 0.2  // 20% pixel difference allowed
    });
  });

  test('Baseline page visual check', async ({ page }) => {
    await page.goto(`${BASE_URL}/#baseline`);
    await page.waitForLoadState('networkidle');
    
    await page.waitForSelector('#page-baseline', { state: 'visible' });
    
    await expect(page).toHaveScreenshot('baseline.png', {
      fullPage: true,
      threshold: 0.2
    });
  });

  test('Practice page visual check', async ({ page }) => {
    await page.goto(`${BASE_URL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    await page.waitForSelector('#page-practice', { state: 'visible' });
    
    await expect(page).toHaveScreenshot('practice.png', {
      fullPage: true,
      threshold: 0.2
    });
  });

  test('Navigation bar visual check', async ({ page }) => {
    await page.goto(`${BASE_URL}/#dashboard`);
    await page.waitForLoadState('networkidle');
    
    // Screenshot just the nav bar
    const nav = page.locator('nav, .navbar, #navigation');
    await expect(nav).toHaveScreenshot('navigation.png', {
      threshold: 0.1
    });
  });

  test('Problem card visual check', async ({ page }) => {
    await page.goto(`${BASE_URL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    // Start a session to show problem card
    await page.click('#start-session');
    await page.waitForTimeout(1000);
    
    // Screenshot problem display area
    const problemCard = page.locator('#problem-display, .problem-card, [data-testid="problem"]').first();
    if (await problemCard.isVisible().catch(() => false)) {
      await expect(problemCard).toHaveScreenshot('problem-card.png', {
        threshold: 0.2
      });
    }
  });

  test('Modal dialogs visual check', async ({ page }) => {
    await page.goto(`${BASE_URL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    // Open help modal
    await page.click('#stuckButton');
    await page.waitForTimeout(500);
    
    const modal = page.locator('.modal, [role="dialog"]').first();
    if (await modal.isVisible().catch(() => false)) {
      await expect(modal).toHaveScreenshot('help-modal.png', {
        threshold: 0.2
      });
    }
  });

  test('Mobile viewport - Dashboard', async ({ page }) => {
    // Set mobile viewport
    await page.setViewportSize({ width: 375, height: 667 });
    
    await page.goto(`${BASE_URL}/#dashboard`);
    await page.waitForLoadState('networkidle');
    
    await expect(page).toHaveScreenshot('dashboard-mobile.png', {
      fullPage: true,
      threshold: 0.2
    });
  });

  test('Mobile viewport - Practice', async ({ page }) => {
    await page.setViewportSize({ width: 375, height: 667 });
    
    await page.goto(`${BASE_URL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    await expect(page).toHaveScreenshot('practice-mobile.png', {
      fullPage: true,
      threshold: 0.2
    });
  });
});

// Component-specific visual tests
test.describe('Visual Regression - Components', () => {
  
  test('Button states', async ({ page }) => {
    await page.goto(`${BASE_URL}/#dashboard`);
    await page.waitForLoadState('networkidle');
    
    // Primary button
    const primaryBtn = page.locator('button.btn-primary, .btn-primary').first();
    if (await primaryBtn.isVisible().catch(() => false)) {
      await expect(primaryBtn).toHaveScreenshot('button-primary.png');
    }
    
    // Secondary button
    const secondaryBtn = page.locator('button.btn-secondary, .btn-secondary').first();
    if (await secondaryBtn.isVisible().catch(() => false)) {
      await expect(secondaryBtn).toHaveScreenshot('button-secondary.png');
    }
  });

  test('Form inputs', async ({ page }) => {
    await page.goto(`${BASE_URL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    // Text input
    const input = page.locator('input[type="text"], input[type="number"]').first();
    if (await input.isVisible().catch(() => false)) {
      await expect(input).toHaveScreenshot('input-text.png');
    }
    
    // Select dropdown
    const select = page.locator('select').first();
    if (await select.isVisible().catch(() => false)) {
      await expect(select).toHaveScreenshot('input-select.png');
    }
  });

  test('Error states', async ({ page }) => {
    await page.goto(`${BASE_URL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    // Trigger an error (submit empty form)
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Look for error message
    const error = page.locator('.error, .alert-danger, [role="alert"]').first();
    if (await error.isVisible().catch(() => false)) {
      await expect(error).toHaveScreenshot('error-message.png');
    }
  });
});

// Update baselines script helper
test.describe('Visual Regression - Update Baselines', () => {
  test.skip(process.env.UPDATE_SNAPSHOTS !== 'true', 'Only run when updating baselines');
  
  test('Update all baselines', async ({ page }) => {
    // This test only runs when UPDATE_SNAPSHOTS=true
    // It will regenerate all baseline screenshots
    await page.goto(`${BASE_URL}/#dashboard`);
    await page.waitForLoadState('networkidle');
    await expect(page).toHaveScreenshot('dashboard.png');
  });
});
