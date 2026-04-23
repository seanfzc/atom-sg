# ATOM-SG MVP Test Strategy

## The Problem

**67 UI tests** tell you the app *renders*.  
**23 critical tests** tell you the app *works*.

For pilot success, we need both—but the critical tests are non-negotiable.

## Test Pyramid

```
       /\
      /  \  4 tests  - Live API Integration (manual only)
     /____\
    /      \  23 tests - Critical Pilot Tests (every commit)
   /        \
  /__________\  67 tests - UI/Functional Tests (render validation)
```

## Execution Strategy

### 1. Developer Workflow (Local)

```bash
# Before every commit - run critical tests
npm run test:critical

# Before PR - run all tests with mocks
npm run test:mock

# Debug failing test
npm run test:critical:ui
```

**Time:** ~2 minutes for critical, ~5 minutes for all

### 2. CI/CD Workflow (Automated)

```yaml
# On every PR
- Run: npm run test:critical
- Browsers: Chromium only (fastest)
- Workers: 4 (parallel)
- Time: ~1 minute

# On merge to main
- Run: npm run test:mock (all tests)
- Browsers: Chromium, Firefox, WebKit
- Workers: 2
- Time: ~5 minutes

# Nightly (optional)
- Run: npm run test:live (with real API)
- Browsers: Chromium
- Workers: 1
- Time: ~10 minutes + API latency
```

### 3. Pre-Pilot Checklist

```bash
# Run everything before pilot launch
npm run test:critical      # Must pass: 23/23
npm run test:mock          # Should pass: 90/90
npm run test:live          # Validate: API works end-to-end
```

## Critical Test Breakdown

### P1: Problem Generation (8 tests)
**Risk if failing:** Pilot starts with broken problems  
**Test time:** ~30 seconds

| # | Test | Failure Mode |
|---|------|--------------|
| 1.1 | Valid JSON structure | App crashes on parse error |
| 1.2 | Clean answer format | Students enter "undefined" as answer |
| 1.3 | Pathway matching | Wrong pathway taught |
| 1.4 | No banned words | P6 students confused by P3 vocabulary |
| 1.5 | 20 valid responses | Silent failures mid-baseline |
| 1.6 | Balanced distribution | Some pathways never tested |
| 1.7 | No duplicates | Student sees same problem twice |
| 1.8 | Error handling | Blank screen instead of error message |
| 1.9 | Timeout handling | Infinite spinner, frustrated user |

### P2: Scoring Logic (6 tests)
**Risk if failing:** Wrong gap analysis, wrong pathway assignments  
**Test time:** ~20 seconds

| # | Test | Failure Mode |
|---|------|--------------|
| 2.1 | Gap detection at 25% | Student marked "mastery" when they failed |
| 2.2 | Mastery at 75% | Student stuck in gap remediation |
| 2.3 | Whitespace handling | " 42 " marked wrong |
| 2.4 | Currency handling | "$42" marked wrong |
| 2.5 | Timer accuracy | Analytics show 0s for all problems |
| 2.6 | No null times | Database has NULL time_seconds |

### P3: Socratic Feedback (5 tests)
**Risk if failing:** Students learn nothing from mistakes  
**Test time:** ~15 seconds

| # | Test | Failure Mode |
|---|------|--------------|
| 3.1 | Hint not answer | Answer revealed immediately, no learning |
| 3.2 | Correct feedback | Student doesn't know they got it right |
| 3.3 | 3-strike solution | Student stuck forever on hard problem |
| 3.4 | Next Problem button | Can't progress after solution |
| 3.5 | Pathway-specific hints | Generic hints don't help |

### P4: Data Persistence (4 tests)
**Risk if failing:** Lost progress, angry parents  
**Test time:** ~10 seconds

| # | Test | Failure Mode |
|---|------|--------------|
| 4.1 | Survives reload | Student loses 30 minutes of work |
| 4.2 | Continue from N | Must restart entire baseline |
| 4.3 | Transfer comparison | Can't show improvement |
| 4.4 | Delta calculation | Wrong improvement metrics |

## Mock API Design

### Why Mocks Are Safe Here

The critical tests validate **system behavior**, not **LLM quality**:

| Test Type | Validates | Needs Real API? |
|-----------|-----------|-----------------|
| JSON structure | System parses response correctly | ❌ No |
| Answer format | System handles numbers | ❌ No |
| Pathway matching | System routes correctly | ❌ No |
| Scoring logic | System calculates accuracy | ❌ No |
| Socratic flow | System shows right feedback at right time | ❌ No |
| Data persistence | System saves/loads correctly | ❌ No |
| **Problem quality** | LLM generates good math problems | ✅ Yes |
| **Hint quality** | Socratic hints are pedagogically sound | ✅ Yes |

**Separation of concerns:**
- Critical tests → System works with *any* valid response
- Live API tests → LLM generates *good* responses

### Mock Data Structure

```typescript
const MOCK_PROBLEMS = {
  'cross-thread': {
    problem: string,        // The question text
    answer: number,         // Numeric answer
    equation_shadow: string, // Model articulation
    pathway_type: string,   // Must match request
    hint: string,          // Socratic hint
    solution_steps: string[] // Full solution
  }
  // ... 4 more pathways
};
```

### Extending Mocks

To add new test scenarios:

```typescript
// In critical-pilot.spec.ts
const MOCK_EDGE_CASES = {
  'decimal-answer': {
    problem: 'Cost of 2.5 kg at $4/kg',
    answer: 10.00,  // Tests decimal handling
    // ...
  },
  'large-number': {
    problem: 'Distance problem',
    answer: 10000,  // Tests large number display
    // ...
  }
};
```

## Failure Response Playbook

### Critical Test Fails in CI

```
1. Block deployment
2. Developer investigates locally:
   npm run test:critical:ui
3. Fix issue or update mock if API changed
4. Re-run critical tests
5. Merge only when 23/23 pass
```

### UI Test Fails in CI

```
1. Check if critical tests pass
2. If critical pass, UI failure is non-blocking
3. Log issue for next sprint
4. Deploy if pilot timeline requires
```

### Live API Test Fails

```
1. Expected—LLM responses vary
2. Run 3 times to confirm pattern
3. If consistently failing:
   - Check API credits
   - Check API schema changes
   - Update mocks if schema changed
4. Never block deployment on flaky live tests
```

## Metrics to Track

| Metric | Target | Alert If |
|--------|--------|----------|
| Critical test pass rate | 100% | < 100% |
| Critical test duration | < 2 min | > 3 min |
| UI test pass rate | > 95% | < 90% |
| Live API test pass rate | > 70% | < 50% |
| Flaky test count | 0 | > 2 |

## Test Maintenance

### Weekly
- [ ] Review any critical test failures
- [ ] Update mocks if API schema changed
- [ ] Check test duration trends

### Monthly
- [ ] Review live API test stability
- [ ] Add new critical tests for new features
- [ ] Remove/update obsolete tests

### Pre-Pilot
- [ ] Run full suite: critical + UI + live
- [ ] Validate all 90 tests pass
- [ ] Document any known issues
- [ ] Create runbook for test failures

## Summary

| What | Count | When to Run | Time |
|------|-------|-------------|------|
| Critical tests | 23 | Every commit | ~1 min |
| UI tests | 67 | Pre-merge | ~4 min |
| Live API tests | 4 | Nightly/manual | ~10 min |
| **Total** | **94** | **Full suite weekly** | **~15 min** |

**Remember:** The 23 critical tests are your safety net. If they pass, the pilot won't fail catastrophically. Everything else is optimization.
