#!/usr/bin/env node
/**
 * Auto-Fix Runner: Find and fix broken interactions automatically
 * 
 * This script:
 * 1. Runs action verification tests
 * 2. Captures failures with detailed diagnostics
 * 3. Attempts automated fixes for common issues
 * 4. Re-runs tests to verify fixes
 */

const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const CONFIG = {
  testDir: './tests',
  resultsDir: './test-results',
  frontendDir: '../frontend/static/js',
  maxRetries: 3,
  fixesApplied: []
};

// Common issues and their auto-fixes
const AUTO_FIXES = {
  // Issue: e.preventDefault() blocking anchor tags
  'preventDefault-blocking-link': {
    pattern: /addEventListener\(['"]click['"],\s*\([^)]*\)\s*=>\s*\{[\s\S]*?e\.preventDefault\(\)[\s\S]*?\}\s*\);/,
    filePattern: /\.js$/,
    fix: (content, match) => {
      // Comment out or remove e.preventDefault() for anchor tags
      return content.replace(
        /(addEventListener\(['"]click['"],\s*\([^)]*\)\s*=>\s*\{[\s\S]*?)(e\.preventDefault\(\);)([\s\S]*?\}\s*\);)/,
        '$1// $2 // REMOVED: was blocking native anchor tag behavior$3'
      );
    },
    description: 'Removed e.preventDefault() that was blocking anchor tag navigation'
  },

  // Issue: Missing target="_blank" on external links
  'missing-target-blank': {
    pattern: /<a\s+[^>]*href=["'][^"']*pdf[^"']*["'][^>]*>(?!.*target=)/i,
    filePattern: /\.(html|jsx|tsx|vue)$/,
    fix: (content) => {
      return content.replace(
        /(<a\s+[^>]*href=["'][^"']*pdf[^"']*["'])([^>]*)>/gi,
        '$1 target="_blank"$2>'
      );
    },
    description: 'Added target="_blank" to PDF links'
  },

  // Issue: Broken event handler (null element)
  'null-element-handler': {
    pattern: /getElementById\(['"]([^'"]+)['"]\)\s*\.addEventListener/,
    filePattern: /\.js$/,
    check: (content, match) => {
      const elementId = match[1];
      // Check if element exists in HTML
      const htmlFiles = findHtmlFiles();
      let found = false;
      for (const htmlFile of htmlFiles) {
        const html = fs.readFileSync(htmlFile, 'utf8');
        if (html.includes(`id="${elementId}"`)) {
          found = true;
          break;
        }
      }
      return !found;
    },
    fix: (content, match) => {
      const elementId = match[1];
      // Wrap in null check
      return content.replace(
        new RegExp(`(const|let|var)\\s+\\w+\\s*=\\s*document\\.getElementById\\(['"]${elementId}['"]\\);?`),
        `const ${match[0].split('=')[0].trim().split(' ')[1]} = document.getElementById('${elementId}');\n  if (!${match[0].split('=')[0].trim().split(' ')[1]}) {\n    console.error('Element #${elementId} not found');\n    return;\n  }`
      );
    },
    description: 'Added null check for missing DOM element'
  },

  // Issue: Hardcoded API URLs that should be relative
  'hardcoded-api-url': {
    pattern: /['"]http:\/\/localhost:\d+\/api\/v1\/[^'"]+['"]/,
    filePattern: /\.js$/,
    fix: (content) => {
      return content.replace(
        /['"]http:\/\/localhost:\d+(\/api\/v1\/[^'"]+)['"]/g,
        '"$1"'
      );
    },
    description: 'Converted hardcoded localhost URLs to relative paths'
  }
};

function findHtmlFiles() {
  const htmlFiles = [];
  const frontendDir = path.resolve(CONFIG.frontendDir, '..');
  
  function scanDir(dir) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory() && !item.includes('node_modules')) {
        scanDir(fullPath);
      } else if (item.endsWith('.html')) {
        htmlFiles.push(fullPath);
      }
    }
  }
  
  scanDir(frontendDir);
  return htmlFiles;
}

function runTests(testPattern = 'action-verification') {
  console.log(`\n🧪 Running tests: ${testPattern}`);
  
  try {
    const output = execSync(
      `npx playwright test ${testPattern} --reporter=json`,
      { 
        cwd: path.resolve(__dirname),
        encoding: 'utf8',
        timeout: 120000
      }
    );
    
    return { success: true, output };
  } catch (error) {
    // Tests failed - parse the error output
    return { 
      success: false, 
      output: error.stdout || error.message,
      error: error
    };
  }
}

function parseFailures(testOutput) {
  const failures = [];
  
  try {
    const results = JSON.parse(testOutput);
    
    for (const suite of results.suites || []) {
      for (const spec of suite.specs || []) {
        for (const test of spec.tests || []) {
          for (const result of test.results || []) {
            if (result.status !== 'passed') {
              failures.push({
                test: spec.title,
                error: result.error?.message || 'Unknown error',
                location: `${spec.file}:${result.line || 0}`,
                snippet: result.error?.snippet || ''
              });
            }
          }
        }
      }
    }
  } catch (e) {
    // Try regex parsing if JSON fails
    const failureRegex = /(\d+ failed)/g;
    const match = testOutput.match(failureRegex);
    if (match) {
      console.log('Found failures:', match[0]);
    }
  }
  
  return failures;
}

function diagnoseFailure(failure) {
  const diagnostics = [];
  
  // Check for common error patterns
  if (failure.error.includes('timeout')) {
    diagnostics.push('Element not found or not clickable - may be hidden or missing');
  }
  
  if (failure.error.includes('preventDefault')) {
    diagnostics.push('JavaScript is preventing default behavior - check event handlers');
  }
  
  if (failure.error.includes('new tab') || failure.error.includes('page')) {
    diagnostics.push('Navigation or new tab opening failed - check target="_blank" or window.open');
  }
  
  if (failure.test.includes('articulation') && failure.error.includes('visible')) {
    diagnostics.push('Forced articulation fields not appearing - check conditional rendering');
  }
  
  if (failure.error.includes('undefined') || failure.error.includes('null')) {
    diagnostics.push('Null reference error - element may not exist in DOM');
  }
  
  return diagnostics;
}

function scanForIssues() {
  console.log('\n🔍 Scanning for common issues...');
  
  const issues = [];
  const jsFiles = [];
  
  // Find all JS files
  function scanJsFiles(dir) {
    const items = fs.readdirSync(dir);
    for (const item of items) {
      const fullPath = path.join(dir, item);
      const stat = fs.statSync(fullPath);
      if (stat.isDirectory() && !item.includes('node_modules')) {
        scanJsFiles(fullPath);
      } else if (item.endsWith('.js')) {
        jsFiles.push(fullPath);
      }
    }
  }
  
  scanJsFiles(path.resolve(CONFIG.frontendDir));
  
  // Check each file for issues
  for (const file of jsFiles) {
    const content = fs.readFileSync(file, 'utf8');
    
    for (const [issueType, issueConfig] of Object.entries(AUTO_FIXES)) {
      if (!file.match(issueConfig.filePattern)) continue;
      
      const match = content.match(issueConfig.pattern);
      if (match) {
        // Additional check if defined
        if (issueConfig.check && !issueConfig.check(content, match)) {
          continue;
        }
        
        issues.push({
          type: issueType,
          file: file,
          description: issueConfig.description,
          canAutoFix: !!issueConfig.fix,
          match: match[0].substring(0, 100) + '...'
        });
      }
    }
  }
  
  return issues;
}

function applyFix(issue) {
  const fixConfig = AUTO_FIXES[issue.type];
  if (!fixConfig || !fixConfig.fix) {
    return false;
  }
  
  try {
    const content = fs.readFileSync(issue.file, 'utf8');
    const match = content.match(fixConfig.pattern);
    
    if (!match) return false;
    
    const fixedContent = fixConfig.fix(content, match);
    
    // Backup original
    const backupPath = issue.file + '.backup-' + Date.now();
    fs.writeFileSync(backupPath, content);
    
    // Apply fix
    fs.writeFileSync(issue.file, fixedContent);
    
    CONFIG.fixesApplied.push({
      type: issue.type,
      file: issue.file,
      description: fixConfig.description,
      backup: backupPath
    });
    
    return true;
  } catch (error) {
    console.error(`Failed to apply fix to ${issue.file}:`, error.message);
    return false;
  }
}

function generateReport(testResults, failures, issues) {
  const report = {
    timestamp: new Date().toISOString(),
    summary: {
      testsRun: testResults.success ? 'passed' : 'failed',
      failures: failures.length,
      issuesFound: issues.length,
      fixesApplied: CONFIG.fixesApplied.length
    },
    failures: failures.map(f => ({
      test: f.test,
      error: f.error,
      diagnostics: diagnoseFailure(f)
    })),
    issues: issues,
    fixes: CONFIG.fixesApplied,
    nextSteps: []
  };
  
  // Generate next steps
  if (failures.length > 0) {
    report.nextSteps.push('Review test failures and apply manual fixes');
  }
  if (issues.length > CONFIG.fixesApplied.length) {
    report.nextSteps.push(`${issues.length - CONFIG.fixesApplied.length} issues require manual review`);
  }
  if (CONFIG.fixesApplied.length > 0) {
    report.nextSteps.push('Re-run tests to verify auto-fixes worked');
  }
  
  return report;
}

async function main() {
  console.log('╔════════════════════════════════════════════════════════╗');
  console.log('║     Auto-Fix Runner: Test & Fix Interactions         ║');
  console.log('╚════════════════════════════════════════════════════════╝');
  
  // Step 1: Run initial tests
  console.log('\n📋 Step 1: Running initial test suite...');
  const testResults = runTests('action-verification');
  
  if (testResults.success) {
    console.log('✅ All tests passed! No fixes needed.');
    return;
  }
  
  console.log('❌ Tests failed. Analyzing...');
  
  // Step 2: Parse failures
  const failures = parseFailures(testResults.output);
  console.log(`\n📊 Found ${failures.length} test failures:`);
  failures.forEach((f, i) => {
    console.log(`  ${i + 1}. ${f.test}`);
    console.log(`     Error: ${f.error.substring(0, 100)}...`);
  });
  
  // Step 3: Scan for issues
  const issues = scanForIssues();
  console.log(`\n🔍 Found ${issues.length} potential issues in code:`);
  issues.forEach((issue, i) => {
    console.log(`  ${i + 1}. [${issue.type}] ${path.basename(issue.file)}`);
    console.log(`     ${issue.description}`);
    console.log(`     Auto-fixable: ${issue.canAutoFix ? 'YES' : 'NO'}`);
  });
  
  // Step 4: Apply auto-fixes
  console.log('\n🔧 Step 4: Applying auto-fixes...');
  let fixesApplied = 0;
  
  for (const issue of issues) {
    if (issue.canAutoFix) {
      console.log(`  Fixing ${issue.type} in ${path.basename(issue.file)}...`);
      if (applyFix(issue)) {
        fixesApplied++;
        console.log('    ✅ Fixed');
      } else {
        console.log('    ❌ Fix failed');
      }
    }
  }
  
  console.log(`\n📈 Applied ${fixesApplied} auto-fixes`);
  
  // Step 5: Re-run tests if fixes applied
  if (fixesApplied > 0) {
    console.log('\n🔄 Step 5: Re-running tests to verify fixes...');
    const retryResults = runTests('action-verification');
    
    if (retryResults.success) {
      console.log('✅ All tests now passing!');
    } else {
      const remainingFailures = parseFailures(retryResults.output);
      console.log(`❌ Still ${remainingFailures.length} failures remaining`);
      console.log('   These require manual investigation');
    }
  }
  
  // Step 6: Generate report
  console.log('\n📄 Step 6: Generating report...');
  const report = generateReport(testResults, failures, issues);
  
  const reportPath = path.join(CONFIG.resultsDir, 'auto-fix-report.json');
  fs.writeFileSync(reportPath, JSON.stringify(report, null, 2));
  
  console.log(`\n📁 Report saved to: ${reportPath}`);
  
  // Print summary
  console.log('\n╔════════════════════════════════════════════════════════╗');
  console.log('║                      SUMMARY                           ║');
  console.log('╠════════════════════════════════════════════════════════╣');
  console.log(`║  Test Results:     ${report.summary.testsRun.padEnd(26)} ║`);
  console.log(`║  Failures Found:   ${String(report.summary.failures).padEnd(26)} ║`);
  console.log(`║  Issues Scanned:   ${String(report.summary.issuesFound).padEnd(26)} ║`);
  console.log(`║  Fixes Applied:    ${String(report.summary.fixesApplied).padEnd(26)} ║`);
  console.log('╚════════════════════════════════════════════════════════╝');
  
  if (report.nextSteps.length > 0) {
    console.log('\n📋 Next Steps:');
    report.nextSteps.forEach((step, i) => {
      console.log(`  ${i + 1}. ${step}`);
    });
  }
}

// Run if called directly
if (require.main === module) {
  main().catch(console.error);
}

module.exports = { runTests, scanForIssues, applyFix, AUTO_FIXES };
