import { test, expect, PracticePage } from './fixtures';

/**
 * Daily Practice Page Tests - Test Plan Section 4
 * Tests: Session controls, articulation, canvas, help modal, triad feedback
 */

test.describe('Daily Practice Page', () => {
  test.beforeEach(async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
  });

  test('should display floating help buttons (P0-3)', async ({ page }) => {
    await expect(page.locator('#stuckButton')).toBeVisible();
    await expect(page.locator('#glossaryButton')).toBeVisible();
  });

  test('should display practice control buttons', async ({ page }) => {
    await expect(page.locator('#start-warmup')).toBeVisible();
    await expect(page.locator('#start-session')).toBeVisible();
  });

  test('should start practice session and load problem', async ({ page }) => {
    const practice = new PracticePage(page);
    
    // Mock the API response for problem
    await page.route('**/api/v1/problems/*', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          id: 'test-problem-001',
          title: 'Test Problem',
          text: 'What is 2 + 2?',
          pathway: 'arithmetic',
          difficulty: 'easy'
        })
      });
    });
    
    await practice.startSession();
    
    // Session should be visible
    await expect(page.locator('#session-pathway')).toBeVisible();
    await expect(page.locator('#session-progress')).toBeVisible();
  });

  test('should display pathway type dropdown with 5 options', async ({ page }) => {
    // Start session first
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    const dropdown = page.locator('#pathway-type');
    await expect(dropdown).toBeVisible();
    
    // Check for 5 pathway options
    const options = await dropdown.locator('option').count();
    expect(options).toBeGreaterThanOrEqual(5);
  });

  test('should validate articulation form - empty pathway type', async ({ page }) => {
    const practice = new PracticePage(page);
    
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Try to submit without selecting pathway
    await page.fill('#equation-shadow', 'This is a valid equation shadow with more than fifty characters in it');
    await page.click('#confirm-articulation');
    
    // Should show error
    await practice.expectArticulationValidationError();
  });

  test('should validate articulation form - short equation shadow (P0-1)', async ({ page }) => {
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Select pathway but use short equation shadow
    await page.selectOption('#pathway-type', 'arithmetic');
    await page.fill('#equation-shadow', 'short'); // Less than 50 chars
    await page.click('#confirm-articulation');
    
    // Should show error about minimum length
    await expect(page.locator('#articulation-error')).toContainText(/50|minimum|characters/i);
  });

  test('should update character counter as user types', async ({ page }) => {
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    const counter = page.locator('#char-count');
    await expect(counter).toBeVisible();
    
    // Type some text
    await page.fill('#equation-shadow', 'Test text');
    
    // Counter should update
    const countText = await counter.textContent();
    expect(countText).toContain('9');
  });

  test('should open help modal when Need Help clicked (P0-3)', async ({ page }) => {
    const practice = new PracticePage(page);
    await practice.openHelpModal();
    
    // Check modal content
    await expect(page.locator('#hint-btn')).toBeVisible();
    await expect(page.locator('#glossary-btn')).toBeVisible();
    await expect(page.locator('#example-btn')).toBeVisible();
  });

  test('should display canvas tools', async ({ page }) => {
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Canvas should be visible
    await expect(page.locator('#practice-canvas')).toBeVisible();
    
    // Tool buttons should exist
    const tools = ['#pen-tool', '#line-tool', '#text-tool', '#eraser-tool', '#clear-canvas'];
    for (const tool of tools) {
      await expect(page.locator(tool)).toHaveCount(1);
    }
  });

  test('should display triad feedback after submission', async ({ page }) => {
    // Mock the submission response
    await page.route('**/api/v1/practice/submit', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          pathway_correct: true,
          articulation_level: 2,
          solution_correct: true,
          model_articulation: 'This is the model explanation',
          steps: ['Step 1', 'Step 2', 'Step 3']
        })
      });
    });
    
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Fill and submit
    await page.selectOption('#pathway-type', 'arithmetic');
    await page.fill('#equation-shadow', 'This is a detailed equation shadow explanation with sufficient length');
    await page.click('#confirm-articulation');
    
    await page.fill('#student-answer', '4');
    await page.click('#submit-answer');
    
    // Feedback should appear
    await expect(page.locator('#pathway-feedback-text')).toBeVisible();
    await expect(page.locator('#articulation-level-val')).toBeVisible();
    await expect(page.locator('#solution-feedback-text')).toBeVisible();
  });

  test('should show step-by-step guidance for wrong answers (P0-7)', async ({ page }) => {
    // Mock wrong answer response
    await page.route('**/api/v1/practice/submit', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          pathway_correct: true,
          articulation_level: 2,
          solution_correct: false,
          model_articulation: 'The correct answer is 4',
          steps: [
            'Identify the numbers involved',
            'Apply the operation',
            'Check your work'
          ]
        })
      });
    });
    
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'arithmetic');
    await page.fill('#equation-shadow', 'This is a detailed equation shadow explanation with sufficient length');
    await page.click('#confirm-articulation');
    
    await page.fill('#student-answer', '5'); // Wrong answer
    await page.click('#submit-answer');
    
    // Step-by-step guidance should appear
    await expect(page.locator('#step-guidance')).toBeVisible();
  });

  test('should show gaming detection message (P0-2)', async ({ page }) => {
    // Mock gaming detection response
    await page.route('**/api/v1/practice/submit', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          gaming_detected: true,
          message: "Let's Take a Short Break",
          cooldown_seconds: 30
        })
      });
    });
    
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Submit quickly (simulate gaming)
    await page.selectOption('#pathway-type', 'arithmetic');
    await page.fill('#equation-shadow', 'This is a detailed equation shadow explanation with sufficient length');
    await page.click('#confirm-articulation');
    await page.fill('#student-answer', '4');
    await page.click('#submit-answer');
    
    // Gaming message should appear with supportive tone
    await expect(page.locator('#gaming-message')).toContainText(/short break|take a break/i);
  });
});
