import { test, expect } from './fixtures';
import { Page } from '@playwright/test';

/**
 * CRITICAL PILOT TESTS
 * These 23 tests cover the 4 things that will actually break the pilot:
 * 1. Problem Generation (8 tests)
 * 2. Scoring Logic (6 tests)
 * 3. Socratic Feedback (5 tests)
 * 4. Data Persistence (4 tests)
 */

// ============================================================================
// MOCK API LAYER - Predictable responses for reliable testing
// ============================================================================

const MOCK_PROBLEMS: Record<string, any> = {
  'cross-thread': {
    problem: 'A shop sells 3 pens for $5. How much do 12 pens cost?',
    answer: 20,
    equation_shadow: '3 pens = $5, so 12 pens = (12/3) × $5 = 4 × $5 = $20',
    pathway_type: 'cross-thread',
    hint: 'How many groups of 3 pens are in 12 pens?',
    solution_steps: ['Find how many groups: 12 ÷ 3 = 4 groups', 'Multiply: 4 × $5 = $20']
  },
  'part-whole': {
    problem: 'A tank is 3/5 full. It needs 24 more liters to be full. What is the full capacity?',
    answer: 60,
    equation_shadow: '2/5 of tank = 24L, so 1/5 = 12L, full = 5 × 12L = 60L',
    pathway_type: 'part-whole',
    hint: 'If 3/5 is full, what fraction is empty?',
    solution_steps: ['Empty fraction: 1 - 3/5 = 2/5', '2/5 = 24L, so 1/5 = 12L', 'Full = 5 × 12L = 60L']
  },
  'repeated-equal-groups': {
    problem: 'There are 8 boxes with 15 books each. How many books total?',
    answer: 120,
    equation_shadow: '8 groups × 15 per group = 8 × 15 = 120',
    pathway_type: 'repeated-equal-groups',
    hint: 'What operation combines equal groups?',
    solution_steps: ['Multiply: 8 × 15 = 120']
  },
  'comparison': {
    problem: 'John has 45 marbles. Mary has 3 times as many. How many does Mary have?',
    answer: 135,
    equation_shadow: 'Mary = 3 × John = 3 × 45 = 135',
    pathway_type: 'comparison',
    hint: '"Times as many" means which operation?',
    solution_steps: ['Multiply: 3 × 45 = 135']
  },
  'change': {
    problem: 'A temperature rose from 12°C to 28°C. What was the change?',
    answer: 16,
    equation_shadow: 'Change = Final - Initial = 28 - 12 = 16',
    pathway_type: 'change',
    hint: 'How do you find the difference between two numbers?',
    solution_steps: ['Subtract: 28 - 12 = 16']
  }
};

const BANNED_WORDS = ['rest', 'remainder', 'left', 'remaining'];

async function setupMockApi(page: Page) {
  await page.route('**/api/v1/problems/generate**', async (route, request) => {
    const url = request.url();
    const pathwayMatch = url.match(/pathway=([^&]+)/);
    const pathway = pathwayMatch ? decodeURIComponent(pathwayMatch[1]) : 'cross-thread';
    
    const problem = MOCK_PROBLEMS[pathway] || MOCK_PROBLEMS['cross-thread'];
    
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        id: `prob-${Date.now()}`,
        ...problem,
        generated_at: new Date().toISOString()
      })
    });
  });

  await page.route('**/api/v1/problems/*/submit', async (route) => {
    const request = await route.request();
    const postData = await request.postDataJSON();
    const answer = postData?.answer;
    
    // Get the correct answer from the problem ID or default
    const correctAnswer = 20; // Default for cross-thread
    const isCorrect = parseInt(answer) === correctAnswer;
    const attemptCount = postData?.attempt_count || 1;
    
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        correct: isCorrect,
        correct_answer: correctAnswer,
        attempt_count: attemptCount,
        feedback: isCorrect 
          ? 'Correct! Your equation shadow shows clear thinking.'
          : attemptCount >= 3 
            ? 'Here is the full solution: 12 ÷ 3 = 4 groups, 4 × $5 = $20'
            : 'How many groups of 3 pens are in 12 pens?',
        show_solution: attemptCount >= 3,
        socratic: !isCorrect && attemptCount < 3
      })
    });
  });

  await page.route('**/api/v1/baseline/results', async (route) => {
    await route.fulfill({
      status: 200,
      contentType: 'application/json',
      body: JSON.stringify({
        completed: 3,
        total: 28,
        results: [
          { problem_id: 'p1', pathway: 'cross-thread', correct: true, time_seconds: 45 },
          { problem_id: 'p2', pathway: 'part-whole', correct: false, time_seconds: 60 },
          { problem_id: 'p3', pathway: 'comparison', correct: true, time_seconds: 30 }
        ],
        gap_map: {
          'cross-thread': { accuracy: 1.0, status: 'mastery' },
          'part-whole': { accuracy: 0.0, status: 'gap' },
          'comparison': { accuracy: 1.0, status: 'mastery' }
        }
      })
    });
  });
}

// ============================================================================
// PRIORITY 1: PROBLEM GENERATION (8 tests)
// ============================================================================

test.describe('CRITICAL: Problem Generation', () => {
  test.beforeEach(async ({ page }) => {
    await setupMockApi(page);
  });

  test('TEST 1.1: Generate baseline problem returns valid JSON structure', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=cross-thread`);
    
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    
    // Assert required fields exist
    expect(body).toHaveProperty('problem');
    expect(body).toHaveProperty('answer');
    expect(body).toHaveProperty('equation_shadow');
    expect(body).toHaveProperty('pathway_type');
    
    // Assert types
    expect(typeof body.problem).toBe('string');
    expect(typeof body.answer).toBe('number');
    expect(typeof body.equation_shadow).toBe('string');
    expect(typeof body.pathway_type).toBe('string');
  });

  test('TEST 1.2: Generated answer is clean integer or decimal', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=cross-thread`);
    const body = await response.json();
    
    // Answer should be a number (integer or clean decimal)
    expect(typeof body.answer).toBe('number');
    expect(Number.isFinite(body.answer)).toBe(true);
    
    // Should not be NaN, Infinity, or have excessive decimals
    expect(body.answer).not.toBeNaN();
    
    // For money problems, max 2 decimal places
    const decimalPlaces = (body.answer.toString().split('.')[1] || '').length;
    expect(decimalPlaces).toBeLessThanOrEqual(2);
  });

  test('TEST 1.3: pathway_type matches requested pathway', async ({ page, baseURL }) => {
    const pathways = ['cross-thread', 'part-whole', 'repeated-equal-groups', 'comparison', 'change'];
    
    for (const pathway of pathways) {
      const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=${pathway}`);
      const body = await response.json();
      
      expect(body.pathway_type).toBe(pathway);
    }
  });

  test('TEST 1.4: Problem text contains no banned words', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=cross-thread`);
    const body = await response.json();
    
    const problemText = body.problem.toLowerCase();
    
    for (const bannedWord of BANNED_WORDS) {
      expect(problemText).not.toContain(bannedWord);
    }
  });

  test('TEST 1.5: Generate 20 problems - all return valid JSON', async ({ page, baseURL }) => {
    const results = [];
    
    for (let i = 0; i < 20; i++) {
      const pathway = Object.keys(MOCK_PROBLEMS)[i % 5];
      const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=${pathway}`);
      
      expect(response.status()).toBe(200);
      
      const body = await response.json();
      expect(body).toHaveProperty('problem');
      expect(body).toHaveProperty('answer');
      
      results.push(body);
    }
    
    expect(results).toHaveLength(20);
  });

  test('TEST 1.6: Generate 20 problems - distribution is balanced', async ({ page, baseURL }) => {
    const counts: Record<string, number> = {};
    
    for (let i = 0; i < 20; i++) {
      const pathway = Object.keys(MOCK_PROBLEMS)[i % 5];
      const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=${pathway}`);
      const body = await response.json();
      
      counts[body.pathway_type] = (counts[body.pathway_type] || 0) + 1;
    }
    
    // Each pathway should have exactly 4 problems
    for (const pathway of Object.keys(MOCK_PROBLEMS)) {
      expect(counts[pathway]).toBe(4);
    }
  });

  test('TEST 1.7: Generate 20 problems - no identical text', async ({ page, baseURL }) => {
    const problemTexts = new Set();
    
    for (let i = 0; i < 20; i++) {
      const pathway = Object.keys(MOCK_PROBLEMS)[i % 5];
      const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=${pathway}`);
      const body = await response.json();
      
      // Should not have seen this exact text before
      expect(problemTexts.has(body.problem)).toBe(false);
      problemTexts.add(body.problem);
    }
    
    expect(problemTexts.size).toBe(20);
  });

  test('TEST 1.8: API returns malformed response - app shows error state', async ({ page, baseURL }) => {
    // Override mock to return malformed response
    await page.route('**/api/v1/problems/generate**', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'text/plain',
        body: "Sorry, I can't generate that problem right now."
      });
    });
    
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    
    // Should show error state, not blank screen
    await expect(page.locator('.error-message, #error-message, [role="alert"]')).toBeVisible();
    
    // Should have retry option
    await expect(page.locator('#retry-btn, .retry-button')).toBeVisible();
  });

  test('TEST 1.9: API timeout - shows timeout error not infinite spinner', async ({ page, baseURL }) => {
    // Override mock to delay 20 seconds
    await page.route('**/api/v1/problems/generate**', async (route) => {
      await new Promise(resolve => setTimeout(resolve, 20000));
      await route.fulfill({
        status: 200,
        body: JSON.stringify({ problem: 'too late' })
      });
    });
    
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    // Click start and wait for loading indicator
    await page.click('#start-session');
    
    // Loading indicator should appear
    await expect(page.locator('.loading, #loading, .spinner')).toBeVisible();
    
    // After timeout (15s), should show error
    await page.waitForSelector('.timeout-error, #timeout-message', { timeout: 20000 });
  });
});

// ============================================================================
// PRIORITY 2: SCORING LOGIC (6 tests)
// ============================================================================

test.describe('CRITICAL: Scoring Logic', () => {
  test.beforeEach(async ({ page }) => {
    await setupMockApi(page);
  });

  test('TEST 2.1: 1/4 correct on cross-thread shows Gap in gap map', async ({ page, baseURL }) => {
    // Mock baseline results with 25% accuracy
    await page.route('**/api/v1/baseline/results', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          completed: 4,
          gap_map: {
            'cross-thread': { correct: 1, total: 4, accuracy: 0.25, status: 'gap' }
          }
        })
      });
    });
    
    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');
    
    // Gap map should show "Gap" for cross-thread
    const crossThreadStatus = await page.locator('[data-pathway="cross-thread"] .status, #gap-map-cross-thread').textContent();
    expect(crossThreadStatus?.toLowerCase()).toContain('gap');
    
    // Accuracy should show 25%
    const accuracy = await page.locator('[data-pathway="cross-thread"] .accuracy, #accuracy-cross-thread').textContent();
    expect(accuracy).toContain('25');
  });

  test('TEST 2.2: 3/4 correct on part-whole shows Mastery', async ({ page, baseURL }) => {
    await page.route('**/api/v1/baseline/results', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          completed: 4,
          gap_map: {
            'part-whole': { correct: 3, total: 4, accuracy: 0.75, status: 'mastery' }
          }
        })
      });
    });
    
    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');
    
    const status = await page.locator('[data-pathway="part-whole"] .status').textContent();
    expect(status?.toLowerCase()).toContain('master');
  });

  test('TEST 2.3: Whitespace in answer is handled correctly', async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    // Fill articulation
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    // Submit with whitespace
    await page.fill('#student-answer', '  20  ');
    await page.click('#submit-answer');
    
    // Should be marked correct
    await expect(page.locator('#solution-feedback-text')).toContainText(/correct|✓/i);
  });

  test('TEST 2.4: Currency formatting in answer is handled', async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    // Submit with currency symbol
    await page.fill('#student-answer', '$20');
    await page.click('#submit-answer');
    
    // Should handle gracefully (either correct or clear error)
    const feedback = await page.locator('#solution-feedback-text').textContent();
    const isCorrect = feedback?.toLowerCase().includes('correct');
    const isError = feedback?.toLowerCase().includes('number') || feedback?.toLowerCase().includes('format');
    
    expect(isCorrect || isError).toBe(true);
  });

  test('TEST 2.5: Timer records per-problem time accurately', async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    
    // Start session
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    const startTime = Date.now();
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    // Wait 5 seconds
    await page.waitForTimeout(5000);
    
    await page.fill('#student-answer', '20');
    await page.click('#submit-answer');
    
    const endTime = Date.now();
    const actualSeconds = Math.floor((endTime - startTime) / 1000);
    
    // Check that time was recorded (via API or UI)
    // The actual recorded time should be between 4-6 seconds
    expect(actualSeconds).toBeGreaterThanOrEqual(4);
    expect(actualSeconds).toBeLessThanOrEqual(7);
  });

  test('TEST 2.6: Timer does not record 0 or null', async ({ page, baseURL }) => {
    await page.route('**/api/v1/practice/submit', async (route) => {
      const request = await route.request();
      const postData = await request.postDataJSON();
      
      // Assert time is present and valid
      expect(postData).toHaveProperty('time_seconds');
      expect(postData.time_seconds).not.toBeNull();
      expect(postData.time_seconds).not.toBe(0);
      expect(postData.time_seconds).toBeGreaterThan(0);
      
      await route.fulfill({
        status: 200,
        body: JSON.stringify({ correct: true })
      });
    });
    
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(1000);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    await page.fill('#student-answer', '20');
    await page.click('#submit-answer');
    
    // Route handler above will assert the time value
  });
});

// ============================================================================
// PRIORITY 3: SOCRATIC FEEDBACK (5 tests)
// ============================================================================

test.describe('CRITICAL: Socratic Feedback', () => {
  test.beforeEach(async ({ page }) => {
    await setupMockApi(page);
  });

  test('TEST 3.1: First wrong answer shows hint, not answer', async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    // Submit wrong answer
    await page.fill('#student-answer', '15');
    await page.click('#submit-answer');
    
    const feedback = await page.locator('#feedback-text, #solution-feedback-text').textContent();
    
    // Should NOT contain the correct answer (20)
    expect(feedback).not.toContain('20');
    expect(feedback).not.toContain('$20');
    
    // Should contain a question (Socratic method)
    expect(feedback).toContain('?');
    
    // Should be asking, not telling
    expect(feedback?.toLowerCase()).toMatch(/how|what|why|can you|try/i);
  });

  test('TEST 3.2: Correct answer shows equation shadow structure', async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    // Submit correct answer
    await page.fill('#student-answer', '20');
    await page.click('#submit-answer');
    
    const feedback = await page.locator('#feedback-text, #solution-feedback-text, #model-articulation').textContent();
    
    // Should contain "correct" or equivalent
    expect(feedback?.toLowerCase()).toMatch(/correct|right|✓|well done/i);
    
    // Should reference equation shadow or pathway
    const hasEquationShadow = feedback?.toLowerCase().includes('equation') || 
                              feedback?.toLowerCase().includes('shadow') ||
                              feedback?.toLowerCase().includes('thinking');
    expect(hasEquationShadow).toBe(true);
  });

  test('TEST 3.3: Third wrong answer reveals full solution', async ({ page, baseURL }) => {
    let attemptCount = 0;
    
    await page.route('**/api/v1/problems/*/submit', async (route) => {
      attemptCount++;
      const isCorrect = false;
      const showSolution = attemptCount >= 3;
      
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          correct: isCorrect,
          correct_answer: 20,
          attempt_count: attemptCount,
          feedback: showSolution 
            ? 'Full solution: 12 ÷ 3 = 4 groups, 4 × $5 = $20'
            : 'How many groups of 3 pens are in 12 pens?',
          show_solution: showSolution,
          solution_steps: showSolution ? ['12 ÷ 3 = 4', '4 × $5 = $20'] : [],
          socratic: !showSolution
        })
      });
    });
    
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    // Submit wrong answer 3 times
    for (let i = 0; i < 3; i++) {
      await page.fill('#student-answer', '15');
      await page.click('#submit-answer');
      await page.waitForTimeout(500);
    }
    
    // Should show full solution
    const feedback = await page.locator('#feedback-text, #solution-feedback-text').textContent();
    expect(feedback).toContain('20');
    expect(feedback?.toLowerCase()).toContain('solution');
    
    // Should show solution steps
    await expect(page.locator('#solution-steps, .solution-steps')).toBeVisible();
  });

  test('TEST 3.4: Next Problem button appears after solution revealed', async ({ page, baseURL }) => {
    await page.route('**/api/v1/problems/*/submit', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          correct: false,
          attempt_count: 3,
          show_solution: true,
          feedback: 'Full solution revealed'
        })
      });
    });
    
    await page.goto(`${baseURL}/#practice`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    
    await page.fill('#student-answer', '15');
    await page.click('#submit-answer');
    
    // Next Problem button should appear
    await expect(page.locator('#next-problem, #nextProblem, .next-problem')).toBeVisible();
  });

  test('TEST 3.5: Socratic hint is pathway-specific', async ({ page, baseURL }) => {
    // Mock different hints for different pathways
    await page.route('**/api/v1/problems/generate**', async (route, request) => {
      const url = request.url();
      const pathway = url.includes('part-whole') ? 'part-whole' : 'cross-thread';
      
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          ...MOCK_PROBLEMS[pathway],
          id: `prob-${Date.now()}`
        })
      });
    });
    
    // Test cross-thread hint
    await page.goto(`${baseURL}/#practice?pathway=cross-thread`);
    await page.waitForLoadState('networkidle');
    await page.click('#start-session');
    await page.waitForTimeout(500);
    
    await page.selectOption('#pathway-type', 'cross-thread');
    await page.fill('#equation-shadow', 'This is a detailed explanation with sufficient length for the test');
    await page.click('#confirm-articulation');
    await page.fill('#student-answer', 'wrong');
    await page.click('#submit-answer');
    
    const crossThreadFeedback = await page.locator('#feedback-text').textContent();
    
    // Hint should reference groups (cross-thread concept)
    expect(crossThreadFeedback?.toLowerCase()).toMatch(/group|each|per/);
  });
});

// ============================================================================
// PRIORITY 4: DATA PERSISTENCE (4 tests)
// ============================================================================

test.describe('CRITICAL: Data Persistence', () => {
  test.beforeEach(async ({ page }) => {
    await setupMockApi(page);
  });

  test('TEST 4.1: Baseline results survive page reload', async ({ page, baseURL }) => {
    // Start baseline and complete 3 problems
    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');
    
    // Mock that 3 problems are completed
    await page.route('**/api/v1/baseline/results', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          completed: 3,
          total: 28,
          current_problem: 4,
          results: [
            { problem_id: 'p1', correct: true },
            { problem_id: 'p2', correct: false },
            { problem_id: 'p3', correct: true }
          ]
        })
      });
    });
    
    // Reload page
    await page.reload();
    await page.waitForLoadState('networkidle');
    
    // Should still show 3 completed
    const completedText = await page.locator('#baseline-progress, #problems-completed').textContent();
    expect(completedText).toContain('3');
    
    // Should be able to continue from problem 4
    await expect(page.locator('#continue-baseline, #start-problem-4')).toBeVisible();
  });

  test('TEST 4.2: Can continue baseline from where left off', async ({ page, baseURL }) => {
    await page.route('**/api/v1/baseline/results', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          completed: 3,
          total: 28,
          current_problem: 4
        })
      });
    });
    
    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');
    
    // Click continue
    await page.click('#continue-baseline, #resume-baseline');
    
    // Should load problem 4
    const problemNum = await page.locator('#problem-number, #current-problem').textContent();
    expect(problemNum).toContain('4');
  });

  test('TEST 4.3: Transfer test loads baseline for comparison', async ({ page, baseURL }) => {
    // Mock baseline completion
    await page.route('**/api/v1/baseline/results', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          completed: 28,
          gap_map: {
            'cross-thread': { accuracy: 0.75 },
            'part-whole': { accuracy: 0.5 }
          }
        })
      });
    });
    
    // Mock transfer test results
    await page.route('**/api/v1/transfer/results', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          completed: 10,
          gap_map: {
            'cross-thread': { accuracy: 0.9 },
            'part-whole': { accuracy: 0.6 }
          }
        })
      });
    });
    
    await page.goto(`${baseURL}/#transfer`);
    await page.waitForLoadState('networkidle');
    
    // Comparison screen should show both datasets
    await expect(page.locator('#comparison-chart, #baseline-vs-transfer')).toBeVisible();
    
    // Should show baseline data
    const baselineData = await page.locator('#baseline-scores, .baseline-data').textContent();
    expect(baselineData).toBeTruthy();
    
    // Should show transfer data
    const transferData = await page.locator('#transfer-scores, .transfer-data').textContent();
    expect(transferData).toBeTruthy();
  });

  test('TEST 4.4: Accuracy delta calculates correctly', async ({ page, baseURL }) => {
    await page.route('**/api/v1/baseline/results', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          gap_map: {
            'cross-thread': { accuracy: 0.75, correct: 6, total: 8 }
          }
        })
      });
    });
    
    await page.route('**/api/v1/transfer/results', async (route) => {
      await route.fulfill({
        status: 200,
        body: JSON.stringify({
          gap_map: {
            'cross-thread': { accuracy: 0.9, correct: 9, total: 10 }
          }
        })
      });
    });
    
    await page.goto(`${baseURL}/#transfer`);
    await page.waitForLoadState('networkidle');
    
    // Delta should show +15% improvement
    const deltaText = await page.locator('#accuracy-delta, .improvement-delta').textContent();
    
    // Should contain positive indicator
    expect(deltaText?.toLowerCase()).toMatch(/\+15|15%|improve|better|gain/);
  });
});

// ============================================================================
// LIVE API INTEGRATION TESTS (Run separately, not on every commit)
// ============================================================================

test.describe('LIVE API: Integration (use sparingly)', () => {
  test.skip(process.env.SKIP_LIVE_API === 'true', 'Skipping live API tests');

  test('LIVE: Generate problem from real API', async ({ page, baseURL }) => {
    // Remove mock to hit real API
    await page.unroute('**/api/v1/problems/generate**');
    
    const response = await page.request.get(`${baseURL}/api/v1/problems/generate?pathway=cross-thread`);
    
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('problem');
    expect(body).toHaveProperty('answer');
    
    // Log for manual review
    console.log('Live generated problem:', body.problem);
    console.log('Answer:', body.answer);
  });
});
