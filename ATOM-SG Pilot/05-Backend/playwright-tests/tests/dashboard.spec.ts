import { test, expect, DashboardPage } from './fixtures';

/**
 * Dashboard Tests - Test Plan Section 2
 * Tests: Statistics display, milestones, gamification
 */

test.describe('Dashboard', () => {
  test.beforeEach(async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#dashboard`);
    await page.waitForLoadState('networkidle');
  });

  test('should display Today\'s Mission card', async ({ page }) => {
    await expect(page.getByText(/Week \d+, Day \d+/)).toBeVisible();
    await expect(page.getByText(/Today's Mission/)).toBeVisible();
  });

  test('should display task items with time estimates', async ({ page }) => {
    // Look for time estimates (e.g., "5 min", "15 min", "10 min")
    const timePattern = /\d+\s*min/;
    const pageContent = await page.textContent('body');
    expect(pageContent).toMatch(timePattern);
  });

  test('should display statistics cards', async ({ page }) => {
    const dashboard = new DashboardPage(page);
    const stats = await dashboard.getStatistics();
    
    // Verify statistics elements exist
    await expect(page.locator('#total-problems')).toBeVisible();
    await expect(page.locator('#avg-score')).toBeVisible();
    await expect(page.locator('#id-accuracy')).toBeVisible();
    await expect(page.locator('#articulation-level')).toBeVisible();
  });

  test('should load milestones from API', async ({ page, waitForApiResponse }) => {
    // Wait for milestones API call
    const milestonesData = await waitForApiResponse('/milestones');
    
    // Verify milestones section is populated
    await expect(page.locator('#milestones-list')).toBeVisible();
  });

  test('should display gamification section (P1-1)', async ({ page }) => {
    const dashboard = new DashboardPage(page);
    await dashboard.expectGamificationVisible();
    
    // Check for streak and total days
    const streakText = await page.locator('#streak-days').textContent();
    const totalDaysText = await page.locator('#total-days').textContent();
    
    expect(streakText).toBeTruthy();
    expect(totalDaysText).toBeTruthy();
  });

  test('should display achievements list or no achievements message', async ({ page }) => {
    const achievementsList = page.locator('#achievements-list');
    const noAchievements = page.locator('#no-achievements');
    
    // One of these should be visible
    await expect(achievementsList.or(noAchievements)).toBeVisible();
  });

  test('should fetch dashboard data on load', async ({ page }) => {
    // Monitor API calls
    const apiCalls: string[] = [];
    page.on('request', request => {
      if (request.url().includes('/api/v1/')) {
        apiCalls.push(request.url());
      }
    });
    
    await page.reload();
    await page.waitForLoadState('networkidle');
    
    // Should call milestones and reflections endpoints
    expect(apiCalls.some(url => url.includes('/milestones'))).toBeTruthy();
    expect(apiCalls.some(url => url.includes('/reflections'))).toBeTruthy();
  });

  test('should handle API errors gracefully', async ({ page }) => {
    // Intercept and fail the milestones API
    await page.route('**/api/v1/milestones', route => {
      route.fulfill({
        status: 500,
        body: JSON.stringify({ error: 'Server error' })
      });
    });
    
    await page.reload();
    await page.waitForTimeout(2000);
    
    // Dashboard should still be visible even if API fails
    await expect(page.locator('#page-dashboard')).toBeVisible();
  });
});
