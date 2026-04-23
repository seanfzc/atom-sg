import { test, expect } from './fixtures';

/**
 * P0/P1 Fix Verification Tests
 * Tests: All critical bug fixes from P0-1 through P1-1
 */

test.describe('P0/P1 Critical Fixes', () => {
  test.describe('P0-1: Articulation Validation Enhancement', () => {
    test.beforeEach(async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
      await page.click('#start-session');
      await page.waitForTimeout(500);
    });

    test('should require minimum 50 characters in equation shadow', async ({ page }) => {
      await page.selectOption('#pathway-type', 'arithmetic');
      await page.fill('#equation-shadow', 'Too short');
      await page.click('#confirm-articulation');
      
      // Should show validation error
      await expect(page.locator('#articulation-error')).toBeVisible();
      await expect(page.locator('#articulation-error')).toContainText(/50|minimum/i);
    });

    test('should accept valid equation shadow length', async ({ page }) => {
      await page.selectOption('#pathway-type', 'arithmetic');
      await page.fill('#equation-shadow', 
        'This is a detailed explanation of my thinking process with sufficient length');
      
      // Character counter should show >= 50
      const counterText = await page.locator('#char-count').textContent();
      const count = parseInt(counterText || '0');
      expect(count).toBeGreaterThanOrEqual(50);
    });
  });

  test.describe('P0-2: Gaming Detection Language Fix', () => {
    test('should show supportive break message instead of consequences', async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
      
      // Mock gaming detection
      await page.route('**/api/v1/practice/submit', async route => {
        await route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify({
            gaming_detected: true,
            message: "Let's Take a Short Break 🌟",
            cooldown_seconds: 30
          })
        });
      });
      
      await page.click('#start-session');
      await page.waitForTimeout(500);
      
      await page.selectOption('#pathway-type', 'arithmetic');
      await page.fill('#equation-shadow', 
        'This is a detailed explanation of my thinking process with sufficient length');
      await page.click('#confirm-articulation');
      await page.fill('#student-answer', '4');
      await page.click('#submit-answer');
      
      // Should NOT contain "consequences"
      const pageContent = await page.textContent('body');
      expect(pageContent.toLowerCase()).not.toContain('consequences');
      expect(pageContent.toLowerCase()).toContain('break');
    });
  });

  test.describe('P0-3: I\'m Stuck Button', () => {
    test.beforeEach(async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
    });

    test('should display floating Need Help button', async ({ page }) => {
      const stuckButton = page.locator('#stuckButton');
      await expect(stuckButton).toBeVisible();
      await expect(stuckButton).toContainText(/need help|stuck/i);
    });

    test('should open help modal with 3 options', async ({ page }) => {
      await page.click('#stuckButton');
      
      await expect(page.locator('#help-modal')).toBeVisible();
      await expect(page.locator('#hint-btn')).toBeVisible();
      await expect(page.locator('#glossary-btn')).toBeVisible();
      await expect(page.locator('#example-btn')).toBeVisible();
    });

    test('should fetch hint from API', async ({ page }) => {
      await page.route('**/api/v1/problems/*/hint', async route => {
        await route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify({ hint: 'Try breaking it into smaller steps' })
        });
      });
      
      await page.click('#stuckButton');
      await page.click('#hint-btn');
      
      await expect(page.locator('#hint-content')).toContainText('smaller steps');
    });
  });

  test.describe('P0-4: Terminology Definitions', () => {
    test('should display tooltips on articulation form', async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
      await page.click('#start-session');
      await page.waitForTimeout(500);
      
      // Look for tooltip icons
      const tooltipIcons = page.locator('.tooltip-icon, [data-tooltip]');
      await expect(tooltipIcons.first()).toBeVisible();
    });
  });

  test.describe('P0-5: Vocabulary Support (Glossary)', () => {
    test('should have floating glossary button', async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
      
      await expect(page.locator('#glossaryButton')).toBeVisible();
    });

    test('should open glossary with Ctrl+B', async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
      
      await page.keyboard.press('Control+b');
      await expect(page.locator('#glossary-modal')).toBeVisible();
    });
  });

  test.describe('P0-6: Visual-Text Mismatches', () => {
    test('should have accessible render files', async ({ page, baseURL }) => {
      // Test a few known geometry renders
      const renderIds = ['G001-angle-diagram-v1', 'G017-cuboid-v1'];
      
      for (const renderId of renderIds) {
        const response = await page.request.get(`${baseURL}/renders/${renderId}.svg`);
        
        if (response.status() === 200) {
          const content = await response.text();
          // Should be valid SVG
          expect(content).toContain('<svg');
          expect(content).toContain('</svg>');
        }
      }
    });
  });

  test.describe('P0-7: Step-by-Step Scaffolding', () => {
    test('should show step guidance for wrong answers', async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#practice`);
      await page.waitForLoadState('networkidle');
      
      await page.route('**/api/v1/practice/submit', async route => {
        await route.fulfill({
          status: 200,
          contentType: 'application/json',
          body: JSON.stringify({
            pathway_correct: true,
            articulation_level: 2,
            solution_correct: false,
            steps: [
              'Step 1: Read the problem carefully',
              'Step 2: Identify what you need to find',
              'Step 3: Choose the right operation'
            ]
          })
        });
      });
      
      await page.click('#start-session');
      await page.waitForTimeout(500);
      
      await page.selectOption('#pathway-type', 'arithmetic');
      await page.fill('#equation-shadow', 
        'This is a detailed explanation of my thinking process with sufficient length');
      await page.click('#confirm-articulation');
      await page.fill('#student-answer', 'wrong');
      await page.click('#submit-answer');
      
      // Step guidance should appear
      await expect(page.locator('#step-guidance')).toBeVisible();
      await expect(page.getByText('Step 1')).toBeVisible();
    });
  });

  test.describe('P1-1: Gamification', () => {
    test.beforeEach(async ({ page, baseURL }) => {
      await page.goto(`${baseURL}/#dashboard`);
      await page.waitForLoadState('networkidle');
    });

    test('should display streak counter', async ({ page }) => {
      await expect(page.locator('#streak-days')).toBeVisible();
    });

    test('should display total days practiced', async ({ page }) => {
      await expect(page.locator('#total-days')).toBeVisible();
    });

    test('should display achievements section', async ({ page }) => {
      const achievementsSection = page.locator('#achievements-list, #no-achievements');
      await expect(achievementsSection).toBeVisible();
    });
  });
});
