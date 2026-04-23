---
title: Topic #53 — Intervention (Data Manipulation Focus)
description: 10 days of teaching sessions focused on pathway types, shadow equations, geometry, and linguistic equivalents
status: active
owner: Pedagogy Bot
last_updated: 2026-04-22 10:30 SGT
---

# Topic #53 — Intervention

## Purpose

Conduct 10 days of teaching sessions focused on pathway types, shadow equations, geometry, and linguistic equivalents, using deconstructed YAML data.

**Critical Requirement (Stage 0 Finding 1):** Separate diagram data from question/solution data to prevent answer leakage to renderer.

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Scope

- **Input:** 4 baseline questions (from Topic #52) with `diagram_data:` separated from `question:`/`solution:`/`answer_key:`
- **Focus:** Data manipulation, downsizing to nano-nodes, accurate visuals, teaching content
- **Duration:** 10 days (Weeks 2-4 from SOR v4.5)
- **Session Structure:** 5-minute pathway radar warm-up + daily practice sessions

## Tasks (Assigned from SOR v4.5)

| ID | Task | Owner | Target | Success Criteria |
|----|------|-------|-----------------|
| D12 | Create pathway recognition curriculum | Pedagogy Bot | 2026-05-01 | Daily warm-up questions for weakest pathways, using `diagram_data:` only |
| D13 | Create Socratic feedback templates | Pedagogy Bot | 2026-05-01 | Triad feedback logic for each pathway type, NO answer leakage |
| D14 | Create articulation rubric (3-level) | Pedagogy Bot | 2026-05-01 | Level 0-3 criteria for each articulation |
| D15 | Create nano-node breakdown exercises | Pedagogy Bot | 2026-05-01 | Downsize complex problems to nano-nodes, preserve `diagram_data:` structure |
| D16 | Create geometry learning equivalents | Pedagogy Bot | 2026-05-01 | Visual + linguistic scaffolding for geometry concepts |
| D17 | Conduct teaching sessions (10 days) | Pedagogy Bot | 2026-05-01 to 2026-05-10 | Daily sessions, track improvement, verify NO answer leakage |

## Diagram vs Question Data Separation (Fix 1)

**Critical Requirement from Stage 0:** All teaching materials must respect the separation.

### Teaching System Display

When showing questions to students during intervention:
1. **Display diagram ONLY** — Rendered from `diagram_data:` section
2. **Display question text separately** — Read from `question_text:` section
3. **NEVER display solutions** — Do NOT show `solution:` or `answer_key:` sections
4. **Force articulation FIRST** — Student identifies pathway, explains structure, THEN solves
5. **Hide all answers** — No answer visible until after submission

**Reference:** `../00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md`

## Reporting

- **Progress Updates:** Report daily to this topic only (not directly to Sean)
- **Task Completion:** Report when each D-task completes
- **Teaching Session Results:** Report after each session (accuracy, improvement, issues, NO answer leakage)
- **Blocking Issues:** Report immediately if any task blocks

## Success Criteria

- Daily teaching sessions completed (10 days)
- Pathway recognition accuracy improves by ≥80% on trained pathways
- Articulation quality reaches Level 2+ on ≥80% of problems
- Solving accuracy improves by ≥70% on trained pathways
- Geometry learning equivalents taught and understood
- All feedback considered helpful by ≥90% of students
- **NO answer leakage** — Students never see solutions or answers before solving

---

*Updated: 2026-04-22 based on Stage 0 Finding 1*
