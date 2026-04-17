import { test, expect } from './fixtures';

/**
 * Glossary Tests - Test Plan Section 8
 * Tests: Glossary modal, search, keyboard shortcut (P0-5)
 */

test.describe('Glossary', () => {
  test.beforeEach(async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
  });

  test('should open glossary modal from floating button', async ({ page }) => {
    await page.click('#glossaryButton');
    
    await expect(page.locator('#glossary-modal')).toBeVisible();
    await expect(page.locator('#glossary-content')).toBeVisible();
  });

  test('should open glossary modal from help modal', async ({ page }) => {
    // Open help modal first
    await page.click('#stuckButton');
    await expect(page.locator('#help-modal')).toBeVisible();
    
    // Click glossary button in help modal
    await page.click('#glossary-btn');
    
    // Glossary modal should appear
    await expect(page.locator('#glossary-modal')).toBeVisible();
  });

  test('should have search functionality', async ({ page }) => {
    await page.click('#glossaryButton');
    await expect(page.locator('#glossary-modal')).toBeVisible();
    
    // Search input should exist
    const searchInput = page.locator('#glossary-search');
    await expect(searchInput).toBeVisible();
    
    // Type a search term
    await searchInput.fill('pathway');
    await page.waitForTimeout(500); // Wait for debounce
    
    // Results should update
    await expect(page.locator('#glossary-content')).toBeVisible();
  });

  test('should close glossary modal', async ({ page }) => {
    await page.click('#glossaryButton');
    await expect(page.locator('#glossary-modal')).toBeVisible();
    
    // Click close button
    await page.click('#close-glossary');
    
    // Modal should be hidden
    await expect(page.locator('#glossary-modal')).toBeHidden();
  });

  test('should open glossary with Ctrl+B keyboard shortcut', async ({ page }) => {
    // Press Ctrl+B
    await page.keyboard.press('Control+b');
    
    // Glossary modal should appear
    await expect(page.locator('#glossary-modal')).toBeVisible();
  });

  test('should fetch glossary terms from API', async ({ page }) => {
    // Monitor API calls
    const apiCalls: string[] = [];
    page.on('request', request => {
      if (request.url().includes('/api/v1/glossary')) {
        apiCalls.push(request.url());
      }
    });
    
    await page.click('#glossaryButton');
    await page.waitForTimeout(1000);
    
    // Should have called glossary API
    expect(apiCalls.some(url => url.includes('/glossary'))).toBeTruthy();
  });

  test('should display glossary terms with definitions', async ({ page }) => {
    // Mock glossary API
    await page.route('**/api/v1/glossary', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          terms: [
            { term: 'Pathway', definition: 'A problem-solving approach' },
            { term: 'Equation Shadow', definition: 'Written representation of thinking' }
          ]
        })
      });
    });
    
    await page.click('#glossaryButton');
    await page.waitForTimeout(500);
    
    // Terms should be displayed
    await expect(page.getByText('Pathway')).toBeVisible();
    await expect(page.getByText('A problem-solving approach')).toBeVisible();
  });
});
