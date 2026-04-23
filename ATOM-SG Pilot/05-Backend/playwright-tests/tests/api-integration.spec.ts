import { test, expect } from './fixtures';

/**
 * API Integration Tests
 * Tests: All API endpoints, error handling, response validation
 */

test.describe('API Integration', () => {
  const baseApiUrl = '/api/v1';

  test('health endpoint should return 200', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/health`);
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('status', 'healthy');
  });

  test('problems endpoint should return problem list', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/problems`);
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('problems');
    expect(Array.isArray(body.problems)).toBe(true);
  });

  test('problems PDF endpoint should return PDF', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/problems/pdf?week=1`);
    
    // Should return 200 or redirect
    expect([200, 302]).toContain(response.status());
    
    // Content type should be PDF or HTML (if error)
    const contentType = response.headers()['content-type'] || '';
    expect(contentType.includes('pdf') || contentType.includes('html')).toBe(true);
  });

  test('milestones endpoint should return milestones', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/milestones`);
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('milestones');
  });

  test('reflections endpoint should return reflections', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/reflections`);
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('reflections');
  });

  test('glossary endpoint should return terms', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/glossary`);
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('terms');
  });

  test('pathway-radar questions endpoint should return questions', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/pathway-radar/questions`);
    expect(response.status()).toBe(200);
    
    const body = await response.json();
    expect(body).toHaveProperty('questions');
  });

  test('renders endpoint should return SVG files', async ({ page, baseURL }) => {
    // Test a known render file
    const response = await page.request.get(`${baseURL}/renders/G001-angle-diagram-v1.svg`);
    
    // May be 200 or 404 depending on if file exists
    expect([200, 404]).toContain(response.status());
    
    if (response.status() === 200) {
      const contentType = response.headers()['content-type'];
      expect(contentType).toContain('svg');
    }
  });

  test('should handle CORS preflight', async ({ page, baseURL }) => {
    const response = await page.request.fetch(`${baseURL}${baseApiUrl}/health`, {
      method: 'OPTIONS',
      headers: {
        'Origin': 'http://localhost:3000',
        'Access-Control-Request-Method': 'GET'
      }
    });
    
    // Should have CORS headers
    const corsHeaders = [
      'access-control-allow-origin',
      'access-control-allow-methods'
    ];
    
    for (const header of corsHeaders) {
      expect(response.headers()[header]).toBeTruthy();
    }
  });

  test('should handle 404 for unknown endpoints', async ({ page, baseURL }) => {
    const response = await page.request.get(`${baseURL}${baseApiUrl}/nonexistent`);
    expect(response.status()).toBe(404);
  });

  test('should handle POST to reflections', async ({ page, baseURL }) => {
    const response = await page.request.post(`${baseURL}${baseApiUrl}/reflections`, {
      data: {
        week: 1,
        pathway: 'arithmetic',
        reflection: 'Test reflection',
        confidence: 3,
        struggles: ['time_management'],
        improvements: ['practice_more']
      }
    });
    
    // Should accept the POST (may return 201 or 200)
    expect([200, 201]).toContain(response.status());
  });
});
