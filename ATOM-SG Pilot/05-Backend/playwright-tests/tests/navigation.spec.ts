import { test, expect, NavigationPage } from './fixtures';

/**
 * Navigation Tests - Test Plan Section 1
 * Tests: Navigation bar, page routing, active states
 */

test.describe('Navigation', () => {
  test.beforeEach(async ({ page, baseURL }) => {
    await page.goto(baseURL!);
    // Wait for app to initialize
    await page.waitForLoadState('networkidle');
  });

  test('should display navigation bar with all links', async ({ page }) => {
    const navLinks = ['Dashboard', 'Baseline Test', 'Daily Practice', 'Pathway Radar', 'Transfer Test', 'Reflections'];
    
    for (const linkText of navLinks) {
      await expect(page.getByText(linkText, { exact: false })).toBeVisible();
    }
  });

  test('should navigate to Dashboard page', async ({ page }) => {
    const nav = new NavigationPage(page);
    await nav.navigateTo('dashboard');
    await nav.expectPageActive('dashboard');
    
    // Verify URL hash
    await expect(page).toHaveURL(/#dashboard/);
  });

  test('should navigate to Baseline page', async ({ page }) => {
    const nav = new NavigationPage(page);
    await nav.navigateTo('baseline');
    await nav.expectPageActive('baseline');
    
    await expect(page).toHaveURL(/#baseline/);
    await expect(page.locator('#print-baseline, a[href*="/api/v1/problems/pdf"]')).toBeVisible();
  });

  test('should navigate to Practice page', async ({ page }) => {
    const nav = new NavigationPage(page);
    await nav.navigateTo('practice');
    await nav.expectPageActive('practice');
    
    await expect(page).toHaveURL(/#practice/);
    await expect(page.locator('#start-session')).toBeVisible();
  });

  test('should navigate to Pathway Radar page', async ({ page }) => {
    const nav = new NavigationPage(page);
    await nav.navigateTo('radar');
    await nav.expectPageActive('radar');
    
    await expect(page).toHaveURL(/#radar/);
  });

  test('should highlight active navigation link', async ({ page }) => {
    const nav = new NavigationPage(page);
    
    // Navigate to baseline
    await nav.navigateTo('baseline');
    
    // Check that baseline nav link has active class
    const baselineNav = page.locator('#nav-baseline');
    await expect(baselineNav).toHaveClass(/active/);
    
    // Navigate to practice
    await nav.navigateTo('practice');
    
    // Check that practice nav link is now active
    const practiceNav = page.locator('#nav-practice');
    await expect(practiceNav).toHaveClass(/active/);
    
    // Baseline should no longer be active
    await expect(baselineNav).not.toHaveClass(/active/);
  });

  test('should hide other pages when showing active page', async ({ page }) => {
    const nav = new NavigationPage(page);
    
    await nav.navigateTo('baseline');
    
    // Baseline page should be visible
    await expect(page.locator('#page-baseline')).toBeVisible();
    
    // Other pages should be hidden
    await expect(page.locator('#page-dashboard')).toBeHidden();
    await expect(page.locator('#page-practice')).toBeHidden();
  });

  test('should handle direct URL with hash', async ({ page, baseURL }) => {
    // Navigate directly to #baseline
    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');
    
    const nav = new NavigationPage(page);
    await nav.expectPageActive('baseline');
  });
});
