import { expect, test } from '@playwright/test';

const ROUTES = [
  { hash: '#baseline', linkText: 'Baseline Test' },
  { hash: '#practice', linkText: 'Daily Practice' },
  { hash: '#pathway-radar', linkText: 'Pathway Radar' },
  { hash: '#transfer', linkText: 'Transfer Test' },
  { hash: '#reflections', linkText: 'Reflections' },
] as const;

test.describe('Console smoke checks', () => {
  test('navigates key routes without console errors', async ({ page, baseURL }) => {
    const consoleErrors: string[] = [];

    page.on('console', (msg) => {
      if (msg.type() !== 'error') {
        return;
      }

      const location = msg.location();
      const at = location.url
        ? ` @ ${location.url}:${location.lineNumber}:${location.columnNumber}`
        : '';
      consoleErrors.push(`[console.error] ${msg.text()}${at}`);
    });

    page.on('pageerror', (err) => {
      consoleErrors.push(`[pageerror] ${err.message}`);
    });

    await page.goto(`${baseURL}/#baseline`);
    await page.waitForLoadState('networkidle');

    for (const route of ROUTES) {
      await page.getByRole('link', { name: route.linkText }).click();
      await expect(page).toHaveURL(new RegExp(`${route.hash}$`));
      await page.waitForTimeout(250);
    }

    if (page.url().endsWith('#reflections')) {
      const submitReflectionButton = page.getByRole('button', { name: 'Submit Reflection' });
      if (await submitReflectionButton.isVisible()) {
        await submitReflectionButton.click();
      }
    }

    expect(
      consoleErrors,
      `Console errors found:\n${consoleErrors.join('\n')}`
    ).toEqual([]);
  });
});
