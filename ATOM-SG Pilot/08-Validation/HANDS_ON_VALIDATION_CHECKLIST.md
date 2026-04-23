# Hands-On Validation Checklist

**Objective:** Validate MVP works for real users before pilot launch  
**Target:** Complete by 2026-04-22 (4 days buffer before original launch date)  
**Owner:** Sean Foo  
**Support:** Zcaethbot (monitoring, fixes if issues found)

---

## Pre-Validation Setup (5 minutes)

- [ ] Open browser to: http://192.168.2.6/
- [ ] Open browser DevTools (F12) → Console tab
- [ ] Clear browser cache (Cmd+Shift+R for hard refresh)
- [ ] Confirm no red error messages in console on load

---

## Phase 1: Week 1 Baseline Flow (15 minutes)

### 1.1 START HERE Button
- [ ] Click "START HERE →" button
- [ ] **Expected:** PDF opens in new tab (not redirect to dashboard)
- [ ] **Verify:** PDF shows Week 1 baseline test with proper margins (text not cut off)
- [ ] Download/save PDF or print to PDF

### 1.2 Simulate Student Completion
- [ ] Open saved PDF
- [ ] Verify 40 questions present (20 word problems + 12 geometry + 8 data interpretation)
- [ ] Check that questions have clear space for handwritten working
- [ ] Note any formatting issues

### 1.3 Scan Upload (Simulated)
- [ ] Return to main app
- [ ] Navigate to "Baseline Test" section
- [ ] Click "Upload Scan" (or simulate with test image)
- [ ] **Expected:** Upload accepts image/PDF
- [ ] **Verify:** Gap map generates showing 3 weakest pathways

**Stop if:** PDF doesn't open, questions missing, or upload fails. Report issue immediately.

---

## Phase 2: Week 2 Daily Practice (20 minutes)

### 2.1 Dashboard Overview
- [ ] Navigate to Dashboard
- [ ] **Verify:** Today's Mission card visible
- [ ] **Verify:** Progress stats showing (0% or baseline results)
- [ ] **Verify:** Milestones section with locked/unlocked states

### 2.2 Pathway Radar (5-min warm-up)
- [ ] Click "Start Pathway Radar"
- [ ] **Verify:** 10 mixed questions load
- [ ] Answer 2-3 questions (can be random/incorrect)
- [ ] **Verify:** Timer visible and counting
- [ ] **Verify:** Progress indicator (e.g., "Question 3 of 10")
- [ ] Submit radar
- [ ] **Verify:** Results summary shows accuracy %

### 2.3 Practice Problem — Full Loop
- [ ] Click "Start Practice" or "Today's Mission"
- [ ] **Verify:** Problem loads with diagram

#### Forced Articulation (CRITICAL)
- [ ] **Verify:** "Pathway Type" dropdown/field visible BEFORE solve
- [ ] Select a pathway type (e.g., "Before-After Change")
- [ ] **Verify:** "Equation Shadow" text area visible
- [ ] Type articulation (e.g., "Initial amount, then change, find final")
- [ ] **Verify:** Cannot proceed to solving until both fields completed

#### Solving
- [ ] Enter answer in answer field
- [ ] Submit answer

#### Triad Feedback (CRITICAL)
- [ ] **Verify:** Feedback appears (green/yellow/red)
- [ ] **Verify:** Feedback includes:
  - Correct/incorrect indication
  - Equation shadow comparison
  - Socratic hint (if wrong)
- [ ] If wrong: Click "Try Again" and verify new attempt allowed
- [ ] After 3 wrong: **Verify** solution revealed with "Next Problem" button

### 2.4 Canvas Annotation
- [ ] Start new practice problem
- [ ] Click canvas area
- [ ] **Verify:** Can draw on diagram
- [ ] Test color palette (if visible)
- [ ] Test undo button
- [ ] Test text annotation (if available)

**Stop if:** Forced articulation doesn't work, feedback missing, or canvas broken. Report issue.

---

## Phase 3: Progress Persistence (10 minutes)

### 3.1 Data Survival
- [ ] Complete 2-3 practice problems
- [ ] Note current problem number (e.g., "Problem 3 of 10")
- [ ] **Reload page** (Cmd+R)
- [ ] **Verify:** Returns to same problem
- [ ] **Verify:** Previous answers saved

### 3.2 Session Recovery
- [ ] Complete 1 more problem
- [ ] Close browser tab
- [ ] Reopen http://192.168.2.6/
- [ ] **Verify:** Progress retained

**Stop if:** Data lost on reload. Critical bug — must fix before pilot.

---

## Phase 4: Glossary & Help (5 minutes)

### 4.1 Glossary Access
- [ ] Click "Glossary" button (or press Ctrl+B)
- [ ] **Verify:** Modal opens with terms
- [ ] Search for "equation shadow"
- [ ] **Verify:** Definition appears
- [ ] Close glossary

### 4.2 Tooltips
- [ ] Hover over technical term (e.g., "pathway type")
- [ ] **Verify:** Tooltip appears with explanation

### 4.3 Help Modal
- [ ] Click "Help" or "?" button
- [ ] **Verify:** Instructions visible

---

## Phase 5: Mobile/Tablet Check (10 minutes)

### 5.1 Responsive Design
- [ ] Open http://192.168.2.6/ on mobile or resize browser to mobile width
- [ ] **Verify:** Layout adapts (no horizontal scrolling)
- [ ] **Verify:** Navigation accessible via hamburger menu

### 5.2 Touch Interactions
- [ ] Start practice problem
- [ ] **Verify:** Canvas drawing works with touch/mouse
- [ ] **Verify:** Buttons large enough to tap

**Note:** If no mobile device available, use browser DevTools → Device Toolbar → iPhone 12 preset

---

## Issue Reporting Template

If anything fails, document:

```
**Phase:** (e.g., 2.3 Practice Problem)
**Step:** (e.g., Forced Articulation)
**Expected:** (what should happen)
**Actual:** (what actually happened)
**Severity:** (Blocker / High / Medium / Low)
**Screenshot:** (attach if possible)
**Console Errors:** (copy from DevTools console)
```

---

## Go/No-Go Criteria

### LAUNCH BLOCKERS (must all pass)
- [ ] PDF opens correctly from START HERE
- [ ] Forced articulation works (can't skip)
- [ ] Triad feedback appears with correct structure
- [ ] Progress survives page reload
- [ ] No console errors on any page

### HIGH PRIORITY (should all pass)
- [ ] Canvas annotation functional
- [ ] Glossary accessible
- [ ] Mobile layout usable
- [ ] Pathway radar completes successfully

### MEDIUM PRIORITY (nice to have)
- [ ] Animations smooth
- [ ] Print styling correct
- [ ] Keyboard shortcuts work

---

## Timeline

| Date | Activity |
|------|----------|
| 2026-04-18 (today) | Complete Phases 1-2 (30 min) |
| 2026-04-19 | Complete Phases 3-5 (20 min) |
| 2026-04-20 | Buffer day for fixes if issues found |
| 2026-04-21 | Re-validation if needed |
| 2026-04-22 | **GO/NO-GO Decision** |

**Original launch date (2026-04-26):** 4 days buffer for fixes if needed

---

## Support

**If issues found:**
1. Document using template above
2. Send to Zcaethbot
3. Priority fixes within 24 hours
4. Re-test after fix deployed

**Questions during validation:**
- Check console for errors first
- Hard refresh (Cmd+Shift+R) if weird behavior
- Ask Zcaethbot for clarification on expected behavior
