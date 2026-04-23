# 12 Persona Frontend Testing Plan for ATOM-SG Pilot

## Overview
Adapt the existing 12 persona backend testing framework for comprehensive frontend testing with Cursor, including full baseline test generation and persona-specific answer patterns.

## Current State Analysis

### Baseline Test Generation (Current)
- **Location:** `main.py:generate_week_test_pdf()`
- **Status:** Placeholder PDF with 1 sample problem
- **Issue:** Not generating full 25-question baseline test

### OCR/Scan Processing (Current)
- **Endpoint:** `POST /api/v1/scans`
- **Status:** Mock implementation with simulated results
- **Flow:** 
  1. User uploads PDF/PNG/JPG
  2. OCR "processes" (simulated 30s)
  3. Returns gap map with weakest pathways

### 12 Personas (Backend)
Already defined in UAT-TEST-PLAN.md:
1. Alex (Perfect Student, 95%+)
2. Brianna (Above Average, 85%, visual learner)
3. Cameron (Average, 75%, disengaged)
4. Dylan (Below Average, 65%, distracted)
5. Eve (Poor, 50%, major struggles)
6. Fay (Disengaged, 40%, random guessing)
7. Grace (Confused, 55%, wrong pathways)
8. Henry (Anxious, 60%, second-guesses)
9. Ivy (Picky, 70%, critical UI issues)
10. Jack (Cheater/Gamer, random pattern detection)
11. Kevin (Visual Learner, 80%, weak abstract articulation)
12. Liam (Reading Struggles, 60%, misinterprets)

---

## Implementation Requirements

### 1. Full Baseline Test PDF Generation

**Need:** Generate actual 25-question baseline test with:
- Geometry problems (G001-G025)
- Answer sheets with bubbles/checkboxes
- Working space for each question
- Proper formatting for OCR recognition

**Files to Modify:**
- `05-Backend/main.py:generate_week_test_pdf()` - Complete rewrite
- `05-Backend/frontend/static/js/baseline.js` - Handle full test upload

### 2. 12 Persona Answer Pattern Generation

**Need:** Create answer patterns for each persona:

```javascript
const PERSONA_ANSWERS = {
  alex: {
    accuracy: 0.95,
    pattern: "correct",
    working: "detailed",
    time: "fast"
  },
  brianna: {
    accuracy: 0.85,
    pattern: "mostly_correct",
    working: "visual_diagrams",
    time: "normal"
  },
  // ... etc for all 12
};
```

**Files to Create:**
- `05-Backend/playwright-tests/personas/12-persona-answers.js`
- `05-Backend/playwright-tests/personas/persona-runner.js`

### 3. OCR Integration for Testing

**Current Flow:**
1. User completes baseline PDF
2. User uploads via `baseline.js`
3. Backend "processes" OCR (mock)
4. Gap map generated

**For Testing:**
- Need to generate persona-specific completed PDFs
- Or simulate OCR results based on persona patterns

### 4. Persona-MVP Interaction Testing

**Test Scenarios per Persona:**

| Persona | Baseline Upload | Daily Practice | Pathway Radar | Transfer Test |
|---------|-----------------|----------------|---------------|---------------|
| Alex | Perfect score | Fast, accurate | High confidence | Pass all |
| Brianna | Good score | Uses hints | Medium confidence | Pass most |
| Cameron | Average | Skips some | Low engagement | Borderline |
| Dylan | Below avg | Distracted | Random clicks | Fail |
| Eve | Poor | Needs help | Very low | Fail |
| Fay | Random | Guessing | Gaming pattern | Fail |
| Grace | Wrong pathways | Confused | Wrong IDs | Fail |
| Henry | Slow, anxious | Second-guesses | Low confidence | Borderline |
| Ivy | Critical | Reports UI issues | Picky | Pass |
| Jack | Gaming detected | Pattern gaming | Speed gaming | Fail |
| Kevin | Visual good | Weak articulation | Good IDs | Pass |
| Liam | Misreads | Wrong interpretations | Confused | Fail |

---

## Implementation Steps

### Phase 1: Full Baseline PDF Generation
1. Create 25-question PDF template
2. Add answer bubbles/checkboxes
3. Add working space per question
4. Ensure OCR-friendly formatting

### Phase 2: Persona Answer Patterns
1. Define answer patterns for all 12 personas
2. Create answer generation logic
3. Build persona runner for Cursor

### Phase 3: OCR Test Integration
1. Generate persona-specific completed PDFs OR
2. Mock OCR results based on persona patterns
3. Test gap map accuracy

### Phase 4: Frontend Persona Testing
1. Test each persona's journey through MVP
2. Verify UI behavior per persona type
3. Test gaming detection for Jack
4. Test help systems for struggling personas

---

## Files to Create/Modify

### New Files
- `05-Backend/playwright-tests/personas/12-persona-answers.js`
- `05-Backend/playwright-tests/personas/persona-runner.js`
- `05-Backend/playwright-tests/tests/12-persona-journey.spec.ts`
- `05-Backend/scripts/generate-baseline-pdf.js`

### Modified Files
- `05-Backend/main.py:generate_week_test_pdf()` - Full 25-question generation
- `05-Backend/frontend/static/js/baseline.js` - Full test handling
- `05-Backend/playwright-tests/playwright.config.ts` - Add persona profiles

---

## Questions for Sean

1. **Baseline PDF:** Should I generate actual 25-question PDFs or simulate OCR results?
2. **Persona Testing:** Do you want automated persona simulation or manual testing guidance?
3. **OCR:** Is OCR integration critical or can we mock it for testing?
4. **Priority:** Which personas are most critical to test first?

---

## Next Steps

1. Get Sean's input on questions above
2. Implement full baseline PDF generation
3. Create 12 persona answer patterns
4. Build persona testing framework
5. Run tests with Cursor
