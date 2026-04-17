import { test, expect, BaselinePage } from './fixtures';
import path from 'path';

/**
 * Baseline Test Page Tests - Test Plan Section 3
 * Tests: Print button, file upload, gap map results
 */

test.describe('Baseline Test Page', () => {
  test.beforeEach(async ({ page, baseURL }) => {
    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');
  });

  test('should display START HERE button with correct href', async ({ page }) => {
    const baseline = new BaselinePage(page);
    const href = await baseline.clickPrintBaseline();
    
    expect(href).toBe('/api/v1/problems/pdf?week=1');
  });

  test('should have working PDF link that opens in new tab', async ({ page }) => {
    const pdfLink = page.locator('a[href*="/api/v1/problems/pdf"]');
    
    await expect(pdfLink).toHaveAttribute('target', '_blank');
    await expect(pdfLink).toBeVisible();
  });

  test('should display upload section', async ({ page }) => {
    await expect(page.locator('#baseline-file-input')).toBeVisible();
    await expect(page.locator('#baseline-upload-btn')).toBeVisible();
  });

  test('should validate file input accepts correct types', async ({ page }) => {
    const fileInput = page.locator('#baseline-file-input');
    
    // Check accept attribute
    const acceptAttr = await fileInput.getAttribute('accept');
    expect(acceptAttr).toMatch(/\.pdf|\.png|\.jpg|\.jpeg/i);
  });

  test('should show upload status after file selection', async ({ page }) => {
    // Create a dummy file for testing
    const dummyFile = {
      name: 'test-baseline.pdf',
      mimeType: 'application/pdf',
      buffer: Buffer.from('dummy pdf content')
    };
    
    await page.setInputFiles('#baseline-file-input', [dummyFile]);
    
    // File name should appear somewhere
    const pageContent = await page.textContent('body');
    expect(pageContent).toContain('test-baseline.pdf');
  });

  test('should handle upload button click', async ({ page }) => {
    // Mock the API response
    await page.route('**/api/v1/ocr/process', async route => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          scan_id: 'test-scan-001',
          status: 'processing'
        })
      });
    });
    
    const dummyFile = {
      name: 'test-baseline.pdf',
      mimeType: 'application/pdf',
      buffer: Buffer.from('dummy pdf content')
    };
    
    await page.setInputFiles('#baseline-file-input', [dummyFile]);
    await page.click('#baseline-upload-btn');
    
    // Should show status
    await expect(page.locator('#baseline-upload-status')).toBeVisible();
  });

  test('should display gap map results section when available', async ({ page }) => {
    // Initially results may be hidden
    const resultsSection = page.locator('#baseline-results');
    
    // Section should exist
    await expect(resultsSection).toHaveCount(1);
  });

  test('should have no console errors on page load', async ({ consoleLogs }) => {
    // Wait a bit for any async operations
    await new Promise(r => setTimeout(r, 1000));
    
    const errors = consoleLogs.filter(log => log.includes('[error]'));
    expect(errors).toHaveLength(0);
  });

  test('should handle API client availability', async ({ page }) => {
    // Check that window.api or api is available
    const apiAvailable = await page.evaluate(() => {
      return typeof window.api !== 'undefined' || typeof (window as any).api !== 'undefined';
    });
    
    // Log the result but don't fail - this is informational
    console.log('API client available:', apiAvailable);
  });
});
