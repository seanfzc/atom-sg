---
title: Topic #52 — Baseline Generation
description: Generate 4-question baseline test PDF with exam-quality visuals from internal YAML
status: active
owner: Logistics Bot
last_updated: 2026-04-22 10:30 SGT
---

# Topic #52 — Baseline Generation

## Purpose

Generate a printable 4-question baseline test PDF from internal YAML output with exam-quality visuals.

**Critical Requirement (Stage 0 Finding 1):** Separate diagram data from question/solution data to prevent answer leakage to renderer.

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Scope

- **Input:** 4 YAML files (from Topic #51) with `diagram_data:` separated from `question:`/`solution:`/`answer_key:`
- **Output:** Single 4-question baseline test PDF
- **Rendering:** Exam-quality visuals from YAML `diagram_data:` section ONLY
- **Question text:** Added from separate `question_text:` input (NOT from `diagram_data:`)

## Tasks (Assigned from SOR v4.5)

| ID | Task | Owner | Target | Success Criteria |
|----|------|-------|-----------------|
| D7 | Apply rendering gates to 4 YAMLs | Logistics Bot | 2026-04-24 | All gates pass, YAML validated, `diagram_data:` structure verified |
| D8 | Apply label rules to 4 YAMLs | Logistics Bot | 2026-04-24 | All labels positioned correctly, no overlaps, only from `diagram_data:` |
| D9 | Apply geometry rules (isometric 3D, composite overlap) | Logistics Bot | 2026-04-24 | Visuals exam-quality, NO answer leakage |
| D10 | Generate 4-question PDF with inline visuals | Logistics Bot | 2026-04-25 | PDF printable, no overflow, exam-quality, diagram + question text (no solutions) |
| D11 | Verify rendering quality (solvability test) | Integrity Bot | 2026-04-25 | All 4 questions solvable from reconstruction, NO visible answers |

## Diagram vs Question Data Separation (Fix 1)

**Critical Requirement from Stage 0:** Renderer MUST separate visual elements from question/solution elements.

### Renderer Responsibilities

1. **Only read `diagram_data:` section** — Ignore `question:`, `solution:`, `answer_key:` sections
2. **Validate diagram structure** — Check all required fields present
3. **Render visual elements ONLY** — No question text, no solutions, no answers from `diagram_data:`
4. **Add question text separately** — Read `question_text:` from YAML, add to PDF separately
5. **Test solvability** — Given diagram + question text (NOT from `diagram_data:`), can student solve?

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Reporting

- **Progress Updates:** Report daily to this topic only (not directly to Sean)
- **Task Completion:** Report when each D-task completes
- **Blocking Issues:** Report immediately if any task blocks

## Success Criteria

- 4-question baseline test PDF generated
- All visuals exam-quality (pixel-precise, labeled correctly)
- PDF printable (no overflow, proper margins)
- **NO solutions or answers visible** on any page
- All 4 questions pass solvability test (student can solve using diagram + question text)

---

*Updated: 2026-04-22 based on Stage 0 Finding 1*
