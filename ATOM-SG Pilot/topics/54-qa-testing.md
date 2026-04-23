---
title: Topic #54 — QA & Testing
description: Persona testing, solvability verification, transfer test measurement, and ramp-up analytics
status: active
owner: QA Bot
last_updated: 2026-04-22 10:30 SGT
---

# Topic #54 — QA & Testing

## Purpose

Test the entire system end-to-end with diverse personas, measure ramp-up, and validate success criteria.

**Critical Requirement (Stage 0 Finding 1):** Separate diagram data from question/solution data to prevent answer leakage to renderer.

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Scope

- **Persona Testing:** Test baseline with Zeth (1 real child) + optionally 2-3 friends
- **Solvability Verification:** Test all 4 reconstructed questions can be solved (NO visible answers)
- **Transfer Test:** 4 new questions (same types, different parameters) to measure ramp-up
- **Ramp-Up Analytics:** Compare baseline vs. transfer performance

## Tasks (Assigned from SOR v4.5)

| ID | Task | Owner | Target | Success Criteria |
|----|------|-------|-----------------|
| D18 | Conduct baseline test with Zeth | QA Bot | 2026-04-24 | Zeth completes baseline, full data recorded, NO visible answers |
| D19 | Verify solvability of 4 questions | QA Bot | 2026-04-24 | All 4 questions passable from reconstruction, verify NO answer leakage |
| D20 | Generate 4 transfer questions | QA Bot | 2026-05-04 | 4 new questions generated (same types, different parameters), preserve `diagram_data:` structure |
| D21 | Conduct transfer test with Zeth | QA Bot | 2026-05-05 | Zeth completes transfer, full data recorded, NO visible answers |
| D22 | Calculate ramp-up metrics | QA Bot | 2026-05-06 | Baseline vs. transfer comparison complete |

## Diagram vs Question Data Separation (Fix 1)

**Critical Requirement from Stage 0:** All tests must verify NO answer leakage to students.

### Solvability Test Verification

For each reconstructed question:
1. **Give reconstruction to solver** — Diagram (from `diagram_data:`) + question text (from `question_text:`)
2. **Verify NO answers visible** — Check that `solution:` and `answer_key:` sections are NOT displayed
3. **Record answer independently** — Solver derives answer from reconstruction only
4. **Compare to answer key** — Validate solvability (match = PASS, mismatch = FAIL)
5. **If fails** — Analyze WHY (missing info? answer leaked? ambiguous diagram?)

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Reporting

- **Progress Updates:** Report daily to this topic only (not directly to Sean)
- **Task Completion:** Report when each D-task completes
- **Test Results:** Report after each test session (accuracy, issues, NO answer leakage, persona feedback)
- **Blocking Issues:** Report immediately if any task blocks

## Success Criteria

- Baseline test with Zeth completed (full data recorded)
- All 4 questions verified solvable (NO visible answers to solver)
- Transfer test completed (4 new questions)
- Ramp-up metrics calculated (recognition improvement, articulation improvement, solving improvement)
- Overall success criteria from SOR v4.5 met
- **NO answer leakage** — Students never see solutions or answers before solving

---

*Updated: 2026-04-22 based on Stage 0 Finding 1*
