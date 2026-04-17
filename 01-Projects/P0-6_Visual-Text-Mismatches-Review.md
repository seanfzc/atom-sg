# TICKET: P0-6 - Visual-Text Mismatches Review

**Ticket ID:** P0-6
**Priority:** 🔴 CRITICAL (Must Launch With)
**Created:** 2026-04-15 16:30 GMT+8
**Assigned to:** Manual Review Team
**Estimated Time:** 5 hours
**Status:** 📝 Ready to Start

---

## 📋 Executive Summary

This ticket implements systematic review of all 25 geometry problems (G001-G025) to identify and fix visual-text inconsistencies found by Ivy in the focused UX test deep dive. Ivy found 12+ issues where diagrams don't match question text, causing confusion for visual learners like Brianna and undermining system credibility.

**Why Critical:**
- Visual learners (Brianna, Ivy, Kevin) rely on diagrams for understanding
- When diagrams contradict question text, students lose trust
- Leads to wrong answers, disengagement, and "I don't know which one is correct"

**User Decision:** Start review after code fixes complete (Phase 1 done).

---

## 🎯 Objectives

1. **Systematic review** of all 25 geometry problem files
2. **Identify visual-text inconsistencies** including:
   - Shape/quantity mismatches (e.g., "¾-circle" text vs quarter-circle diagram)
   - Proportion errors (angles/sides not visually proportional)
   - Missing labels (unlabeled sides, arrows without quantities)
   - Contradictory information (diagram shows X but text says Y)
3. **Document all issues** with severity ratings (P0, P1, P2)
4. **Propose fixes** (diagram update OR text correction)
5. **Create issue tracking** for implementation

---

## 📁 Problem Files to Review

**Location:** `ATOM-SG Pilot/02-Geometry/problems/`
**Total Problems:** 25 (G001-G025)

**Problem Distribution by Subpathway:**
- G1 (Angles): G001, G007, G008, G013, G017, G021
- G2 (Area & Perimeter): G002, G010, G014, G018, G022
- G3 (Volume & 3D): G003, G009, G016, G023
- G4 (Properties & Classification): G004, G011, G012, G019, G024, G025

---

## 🔍 Review Checklist Per Problem

For each problem, check:

### A. Shape Consistency
- [ ] Diagram shape matches question description
  - Example: Question says "circle" → Diagram is circular (not rectangular)
  - Example: Question says "triangle" → Diagram is triangular (3 sides)

### B. Quantity Consistency
- [ ] All measurements in question appear in diagram
  - Example: "length 6 cm" → Diagram shows side labeled "6 cm"
  - Example: "angles: 45°, 60°, 75°" → Diagram shows all 3 angles labeled
- [ ] No extra measurements in diagram not mentioned in question
- [ ] No missing measurements mentioned in question

### C. Proportional Accuracy
- [ ] Angles visually proportional to their values
  - Example: 70° angle appears larger than 60° angle (not 180 - actual)
  - Example: 120° angle appears larger than 30° angle (not 150 - actual)
- [ ] Side lengths visually proportional to their ratios
  - Example: In 3:4:5 triangle, side ratio 3:4 is visible (not 3:5:1)

### D. Label Clarity
- [ ] All geometric elements are labeled (sides, angles, vertices)
  - Example: In triangle with vertices A, B, C → all labeled
  - Example: In rectangle → length, breadth, height labeled
- [ ] Labels are readable and not obscured
- [ ] Font size is appropriate for 11-year-olds

### E. Before-After Arrows (if applicable)
- [ ] Arrows show what changed (e.g., "sold 30", "gave away 15")
- [ ] Arrow direction is clear (from X to Y, or remaining)
- [ ] Arrows don't conflict with question description
- [ ] Quantities on arrows match question text

### F. Bar Models (if applicable)
- [ ] Bar segments are clearly labeled (e.g., "1/2", "3/4")
- [ ] Total is clearly shown
- [ ] Fractions are visually represented (larger segment = larger fraction)
- [ ] Colors are consistent with question (if colors mentioned)

### G. Text-Diagram Correspondence
- [ ] Question text describes diagram accurately
- [ ] No contradictions between text and diagram
- [ ] Diagram doesn't show elements not mentioned in question
- [ ] Diagram shows elements that contradict question text

### H. Rendering Quality
- [ ] Lines are crisp and clear (not blurry or pixelated)
- [ ] Colors have good contrast
- [ ] Font is legible
- [ ] Diagram fits within problem card layout

---

## 🚨 Common Issues to Look For

### Issue 1: Shape Mismatch
**Example from UX test:** Text says "¾-circle" but diagram shows quarter-circle (90°)
**Impact:** Brianna is confused - "Which one is correct? I can't trust this."
**Severity:** 🔴 P0
**Check:** Question says "circle", "semicircle", "sector" → Verify diagram shape matches
**Fix:** Update diagram OR correct question text to match

---

### Issue 2: Angle Proportion Error
**Example from UX test:** Angle labeled 70° appears larger than 60° angle
**Impact:** Students who rely on visual estimation get wrong answers
**Severity:** 🔴 P0
**Check:** If question lists multiple angles (e.g., 45°, 70°, 75°) → Verify proportional rendering
**Fix:** Add `ensureProportional: True` flag to diagram metadata; force rendering to match actual angle ratios

---

### Issue 3: Unlabeled Sides
**Example from UX test:** "Joined along 5 cm side" - which side is 5 cm?
**Impact:** Students have to guess, often guess wrong
**Severity:** 🔴 P0
**Check:** If question mentions "side", "length", "width" → Verify diagram has corresponding label
**Fix:** Add explicit labels to all sides mentioned in question

---

### Issue 4: Before-After Arrow Without Labels
**Example from UX test:** "Sold 3/5" then "sold 1/4 of remainder" - arrows don't show quantities
**Impact:** Students can't track what changed each step
**Severity:** 🔴 P0
**Check:** If problem is "before-after-change" → Verify arrows have labels
**Fix:** Add arrow labels showing quantities (e.g., "sold 18", "remaining 12")

---

### Issue 5: Fraction Representation Error
**Example from UX test:** "3/4 of whole" - is diagram showing 3/4 visually?
**Impact:** Visual learners expect segments to match fractions
**Severity:** 🟡 P1
**Check:** If question mentions fractions → Verify segment proportions in bar model
**Fix:** Use proportional rendering; add fraction labels to bar segments

---

### Issue 6: Text Contradiction
**Example from UX test:** Question says "find total" but diagram shows separate parts
**Impact:** Students don't know which interpretation is correct
**Severity:** 🔴 P0
**Check:** Compare question text with diagram structure
**Fix:** Align text and diagram; add explanatory note if necessary

---

### Issue 7: Missing Measurements in Diagram
**Example from UX test:** Question says "length 6 cm" but diagram shows unlabeled side
**Impact:** Students can't identify which side is 6 cm
**Severity:** 🔴 P0
**Check:** Verify all measurements from question appear in diagram
**Fix:** Add missing labels to diagram rendering

---

## 📊 Review Process

### Phase 1: Initial Scan (30 min)
1. Read all 25 problem files
2. Extract question text, subpathway, diagram descriptions
3. Identify problem type (angles, area, volume, properties)
4. Create spreadsheet template for tracking issues

### Phase 2: Detailed Review (3 hours)
1. Open each problem file
2. Apply review checklist (A-H above)
3. Check diagram rendering (if PDF renders exist in `05-Backend/artifacts/renders/`)
4. Identify inconsistencies
5. Classify severity (P0, P1, P2)
6. Document issue in tracking spreadsheet

### Phase 3: Issue Prioritization (30 min)
1. Categorize issues by type (shape, quantity, proportion, labels, arrows, etc.)
2. Count issues per category
3. Identify top 3-5 issues affecting most students
4. Classify critical issues (P0) vs nice-to-have (P1/P2)
5. Create prioritized issue list

### Phase 4: Report Generation (1 hour)
1. Create `VISUAL-TEXT-MISMATCHES-REPORT.md` with:
   - Executive summary
   - Top 10 issues with severity
   - Full issue list (all problems affected)
   - Recommended fixes per issue
   - Severity distribution chart

### Phase 5: Fix Recommendations (optional, separate task)

1. Create separate ticket for implementing fixes
2. Assign priority based on severity
3. Estimate implementation time (2-10 hours depending on issues found)

---

## 📝 Tracking Spreadsheet Template

**Columns:**
| Problem ID | Subpathway | Issue Type | Severity | Description | Text Correction | Diagram Update | Priority |

**Issue Types:**
- Shape Mismatch
- Quantity Consistency
- Proportional Error
- Label Clarity
- Before-After Arrows
- Bar Model Error
- Text Contradiction
- Missing Measurements

**Severity Codes:**
- 🔴 P0 - Blocks learning, causes disengagement
- 🟡 P1 - Annoying but workable
- 🟢 P2 - Minor, can defer

---

## 🎯 Quick Wins (30 min - Can Start Immediately)

If review finds **obvious high-impact issues**, these can be fixed during review:

1. **Add explicit side labels** to geometry problems (P0)
   - Example: Add "5 cm" label to joined side in composite shapes
   - Impact: Students can immediately identify which measurement is which

2. **Fix obvious proportion errors** (P0)
   - Example: "¾-circle" text shows as quarter-circle diagram → Change to ¾-circle (270°)
   - Time: 15 min per fix

3. **Add arrow labels** for before-after problems (P0)
   - Example: Add "sold 18", "remaining 12" labels to arrows
   - Time: 10 min per fix

**Total quick wins time:** 1 hour

---

## 📈 Success Criteria

This review is **COMPLETE** when:

1. ✅ All 25 problems reviewed against 9-item checklist
2. ✅ Visual-text inconsistencies documented in tracking spreadsheet
3. ✅ Issues categorized and prioritized (P0/P1/P2)
4. ✅ Report generated (`VISUAL-TEXT-MISMATCHES-REPORT.md`)
5. ✅ Quick wins identified (if applicable)
6. ✅ Recommendations provided for P0 issues
7. ✅ P1 and P2 issues catalogued for future fixes

---

## 📋 Files Involved

**Review:**
- `ATOM-SG Pilot/02-Geometry/problems/G001.md` through `G025.md` (25 files)
- `ATOM-SG Pilot/05-Backend/artifacts/renders/` (diagram PDFs, for reference if needed)

**Output:**
- `VISUAL-TEXT-MISMATCHES-REPORT.md` (final report)
- `P0-6_TRACKING_SPREADSHEET.xlsx` (if Excel available) or CSV

**Related:**
- `FOCUSED_UX_TEST_DEEP_DIVE.md` (reference for issues found by Ivy)
- `P0_P1_IMPLEMENTATION_PLAN.md` (master implementation plan)

---

## 🚀 Next Steps (After Review Complete)

1. **Review generated report** - Verify findings make sense
2. **Prioritize P0 fixes** - Create separate implementation tickets
3. **Implement quick wins** - If high-impact low-effort fixes found
4. **Schedule P1/P2 fixes** - For post-launch improvements
5. **Monitor feedback** - After deployment, watch for visual-text issues reported by students

---

## 📝 Notes

- **Domain expertise required:** P6 geometry problems need domain knowledge to identify subtle inconsistencies
- **Reviewer independence:** Should be reviewed by someone familiar with P6 math syllabus
- **Time estimate:** 5 hours assumes careful review; may take longer if many issues found
- **Quick wins:** Can be implemented during review process for immediate impact

---

**Last Updated:** 2026-04-15 16:32 GMT+8
**Status:** 📝 Ready to Start
**Ready for user approval to begin review process.**
