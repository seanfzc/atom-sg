import { test as base, expect, Page } from '@playwright/test';

/**
 * Custom fixtures for ATOM-SG MVP tests
 */
export type TestFixtures = {
  /** Navigate to a specific page */
  gotoPage: (pageName: string) => Promise<void>;
  
  /** Wait for API response */
  waitForApiResponse: (urlPattern: string) => Promise<any>;
  
  /** Check if element has error state */
  hasErrorState: (selector: string) => Promise<boolean>;
  
  /** Get console logs */
  consoleLogs: string[];
  
  /** Clear console logs */
  clearConsoleLogs: () => void;
};

export const test = base.extend<TestFixtures>({
  // Initialize console logs array
  consoleLogs: async ({ page }, use) => {
    const logs: string[] = [];
    page.on('console', msg => {
      const text = `[${msg.type()}] ${msg.text()}`;
      logs.push(text);
      if (msg.type() === 'error') {
        console.error('Browser console error:', text);
      }
    });
    await use(logs);
  },
  
  // Clear console logs helper
  clearConsoleLogs: async ({ consoleLogs }, use) => {
    await use(() => {
      consoleLogs.length = 0;
    });
  },
  
  // Navigate to page helper
  gotoPage: async ({ page, baseURL }, use) => {
    await use(async (pageName: string) => {
      const url = `${baseURL}/#${pageName}`;
      await page.goto(url);
      // Wait for page to be active
      await page.waitForSelector(`#page-${pageName}.active, #page-${pageName}:not(.hidden)`, 
        { state: 'visible', timeout: 5000 });
    });
  },
  
  // Wait for API response helper
  waitForApiResponse: async ({ page }, use) => {
    await use(async (urlPattern: string) => {
      const response = await page.waitForResponse(
        response => response.url().includes(urlPattern) && response.status() === 200,
        { timeout: 10000 }
      );
      return await response.json().catch(() => null);
    });
  },
  
  // Check error state helper
  hasErrorState: async ({ page }, use) => {
    await use(async (selector: string) => {
      const element = await page.locator(selector);
      const hasErrorClass = await element.evaluate(el => 
        el.classList.contains('error') || 
        el.classList.contains('is-invalid') ||
        el.getAttribute('aria-invalid') === 'true'
      );
      return hasErrorClass;
    });
  },
});

export { expect };

/**
 * Page object models for common operations
 */
export class NavigationPage {
  constructor(private page: Page) {}
  
  async navigateTo(pageName: string) {
    const linkMap: Record<string, string> = {
      'dashboard': 'nav-dashboard',
      'baseline': 'nav-baseline',
      'practice': 'nav-practice',
      'radar': 'nav-radar',
      'transfer': 'nav-transfer',
      'reflections': 'nav-reflections',
    };
    
    const navId = linkMap[pageName];
    if (navId) {
      await this.page.click(`#${navId}`);
      await this.page.waitForURL(`**/#${pageName}`);
    }
  }
  
  async expectPageActive(pageName: string) {
    const pageElement = this.page.locator(`#page-${pageName}`);
    await expect(pageElement).toHaveClass(/active/);
  }
}

export class DashboardPage {
  constructor(private page: Page) {}
  
  async getStatistics() {
    return {
      problems: await this.page.locator('#total-problems').textContent(),
      score: await this.page.locator('#avg-score').textContent(),
      accuracy: await this.page.locator('#id-accuracy').textContent(),
      articulation: await this.page.locator('#articulation-level').textContent(),
    };
  }
  
  async expectGamificationVisible() {
    await expect(this.page.locator('#streak-days')).toBeVisible();
    await expect(this.page.locator('#total-days')).toBeVisible();
  }
}

export class PracticePage {
  constructor(private page: Page) {}
  
  async startSession() {
    await this.page.click('#start-session');
    await this.page.waitForSelector('#session-pathway', { state: 'visible' });
  }
  
  async fillArticulation(pathwayType: string, equationShadow: string) {
    await this.page.selectOption('#pathway-type', pathwayType);
    await this.page.fill('#equation-shadow', equationShadow);
  }
  
  async expectArticulationValidationError() {
    await expect(this.page.locator('#articulation-error')).toBeVisible();
  }
  
  async openHelpModal() {
    await this.page.click('#stuckButton');
    await expect(this.page.locator('#help-modal')).toBeVisible();
  }
}

export class BaselinePage {
  constructor(private page: Page) {}
  
  async clickPrintBaseline() {
    // The button is now an anchor tag
    const link = this.page.locator('a[href*="/api/v1/problems/pdf"]');
    await expect(link).toBeVisible();
    
    // Check href attribute
    const href = await link.getAttribute('href');
    expect(href).toContain('/api/v1/problems/pdf?week=1');
    
    return href;
  }
  
  async uploadFile(filePath: string) {
    await this.page.setInputFiles('#baseline-file', filePath);
    await this.page.click('#upload-baseline-form button[type="submit"]');
  }
}
