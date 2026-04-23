# ATOM-SG Pilot - Project Overview

**Project:** ATOM-SG Pilot - P6 Mathematics Training System
**Version:** 2.1.0 (SOR v4.5 with Fix 1 applied)
**Last Updated:** 2026-04-22

---

## Quick Navigation

### 📚 Always Load (All Stages)

| Stage | Always Load | Purpose |
|-------|-------------|---------|
| Stage 0 (Smoke Test) | `docs/04-renderer-rules.md` | What renderer draws vs hides (diagram vs question separation) |
| Stage 1 (Deconstruction) | `00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md` | Diagram vs question data structure |
| Stage 1 (Deconstruction) | `00-Templates/MATH_DIAGRAM_RENDERING_INSTRUCTION.md` | 4-gates rendering approach |
| Stage 1 (Deconstruction) | `00-Templates/PARAMETRIC_VISUAL_RENDERING_GUIDE.md` | Label placement and collision rules |
| All Stages | `00-Templates/MATH_DIAGRAM_AUDIT_INSTRUCTION.md` | Tester audit protocols |
| All Stages | `00-Templates/MATH_VISUAL_AUDIT_REVIEWER.md` | Reviewer system instruction |
| Stage 2 (Baseline) | `topics/52-baseline-generation.md` | 4-question PDF generation |
| Stage 3 (Baseline Test) | `topics/54-qa-testing.md` | Persona testing, solvability verification |
| Stage 4 (Intervention) | `topics/53-intervention.md` | 10-day teaching sessions |
| Stage 5 (Transfer) | `topics/54-qa-testing.md` | Transfer test, ramp-up analytics |

### 📊 Current Status
| Document | Purpose | Last Updated |
|----------|---------|--------------|
| [Statement-Of-Requirements-v4.5.md](01-Projects/Statement-Of-Requirements-v4.5.md) | SOR v4.5 (28 days, 4 questions, solvability metric) | 2026-04-22 |
| [KANBAN.md](01-Projects/KANBAN.md) | Task tracking (T1-T5, C1-C4) | Daily |
| [CoordinationLog.md](01-Projects/CoordinationLog.md) | Cross-agent coordination | Daily |
| [Stage1-Deconstruction/](Stage1-Deconstruction/) | YAML files (Q7, Q9, Q10, Q13) | 2026-04-22 |

---

## Documentation Structure

### docs/
Renderer rules and guidelines.

| File | Version | Purpose |
|------|---------|---------|
| [04-renderer-rules.md](docs/04-renderer-rules.md) | 1.0 | What to draw vs hide (Stage 0 Finding 1 fix) |

### 00-Templates/
Templates and specifications for consistent content creation.

| File | Version | Purpose |
|------|---------|---------|
| [VERSION.md](00-Templates/VERSION.md) | 2.1.0 | Version history |
| [ATOM-SG_FRAMEWORK_REVISION_v2.md](00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md) | 2.0 | Complete framework |
| [YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md](00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md) | 1.0 | Diagram vs question data separation (Stage 0 Finding 1) |
| [MATH_DIAGRAM_RENDERING_INSTRUCTION.md](00-Templates/MATH_DIAGRAM_RENDERING_INSTRUCTION.md) | 1.0 | 4-gates rendering approach + diagram vs question separation |
| [PARAMETRIC_VISUAL_RENDERING_GUIDE.md](00-Templates/PARAMETRIC_VISUAL_RENDERING_GUIDE.md) | 1.0 | Label placement and collision rules |
| [MATH_DIAGRAM_AUDIT_INSTRUCTION.md](00-Templates/MATH_DIAGRAM_AUDIT_INSTRUCTION.md) | 1.0 | Tester audit protocols |
| [MATH_VISUAL_AUDIT_REVIEWER.md](00-Templates/MATH_VISUAL_AUDIT_REVIEWER.md) | 1.0 | Reviewer system instruction |
| [Baseline-Spec.md](00-Templates/Baseline-Spec.md) | 1.0 | Test specs |
| [Problem-Card.md](00-Templates/Problem-Card.md) | 1.0 | Problem template |
| [Rubric.md](00-Templates/Rubric.md) | 1.0 | Assessment template |
| [Milestone-Template.md](00-Templates/Milestone-Template.md) | 1.0 | Milestone template |

### 01-Projects/
Project management and coordination.

| File | Purpose |
|------|---------|
| [Statement-Of-Requirements-v4.5.md](01-Projects/Statement-Of-Requirements-v4.5.md) | SOR v4.5 with Fix 1 applied |
| [KANBAN.md](01-Projects/KANBAN.md) | Task tracking |
| [CoordinationLog.md](01-Projects/CoordinationLog.md) | Cross-agent coordination |

### topics/
Topic-based coordination for focused sub-agent workstreams.

| File | Purpose |
|------|---------|
| [51-deconstruction-pipeline.md](topics/51-deconstruction-pipeline.md) | Stage 1: Vision LLM 3-layer → YAML (with diagram vs question separation) |
| [52-baseline-generation.md](topics/52-baseline-generation.md) | Stage 2: 4-question PDF generation (with diagram vs question separation) |
| [53-intervention.md](topics/53-intervention.md) | Stage 4: 10-day teaching sessions (with diagram vs question separation) |
| [54-qa-testing.md](topics/54-qa-testing.md) | Stage 3-5: Persona testing, solvability, transfer (with diagram vs question separation) |

---

## Framework Taxonomy (v2.0 - Updated for v4.5)

### Word Problem Pathways
1. **Constant-Total Adjustment** - Problems with fixed totals
2. **Part-Whole with Comparison** - Ratio + difference problems
3. **Before-After Change** - Sequential state changes
4. **Supposition** - Assumption-based problems
5. **Cross-Thread Collision** - Multi-concept fusion (exam standard)
6. **Data Interpretation** (NEW in v4.5) - Graphs, charts, reverse calc

### Geometry Pathways
1. **G1: Angle Reasoning** - Protractor, properties
2. **G2: Area & Perimeter** - Rectilinear figures
3. **G3: Volume & 3D** - Cuboids, nets
4. **G4: Properties & Classification** - Shapes
5. **G5: Composite Overlap** - Overlapping shapes
6. **G6: Grid Construction** - Grid-based tasks
7. **G7: 3D Visualization** - Isometric solids
8. **G8: Angle Chasing** - Multi-shape angles

---

## Workflow

### For Sub-Agents
1. Check [MODEL_USAGE_POLICY.md](MODEL_USAGE_POLICY.md) for GLM selection (NOTE: This file is in the main repo, not yet created in Pilot)
2. Review [Kanban](01-Projects/KANBAN.md) for current tasks
3. Update [SubAgentComms](01-Projects/SubAgentComms.md) with progress
4. Follow templates in [00-Templates/](00-Templates/) and [docs/](docs/)
5. Follow topics [51-deconstruction-pipeline.md](topics/51-deconstruction-pipeline.md) - [54-qa-testing.md](topics/54-qa-testing.md)

### For Developers
1. Check [VERSION.md](00-Templates/VERSION.md) for current version
2. Review [API.md](05-Backend/API.md) for endpoints
3. Follow [DEPLOYMENT.md](05-Backend/DEPLOYMENT.md) for deployment
4. Update documentation when making changes
5. Apply diagram vs question separation (Fix 1) to all rendering work

### For PM
1. Monitor [Kanban](01-Projects/KANBAN.md)
2. Review [SubAgentComms](01-Projects/SubAgentComms.md)
3. Review [CoordinationLog.md](01-Projects/CoordinationLog.md)
4. Check topics [51-54](topics/) for sub-agent updates
5. Apply [docs/04-renderer-rules.md](docs/04-renderer-rules.md) to rendering pipeline

---

## Git Workflow

```bash
# Before starting work
git pull origin main

# After making changes
git add -A
git commit -m "Descriptive message"
git push origin main
```

Note: GitHub has branch protection rules. Direct push to main may require bypass.

---

## Contact & Coordination

- **Daily updates:** CoordinationLog.md
- **Task tracking:** KANBAN.md
- **Version info:** VERSION.md
- **Master index:** [INDEX.md](INDEX.md)
- **Topic coordination:** topics/ (51-deconstruction-pipeline.md, 52-baseline-generation.md, 53-intervention.md, 54-qa-testing.md)

---

## Recent Changes (v2.1.0 - SOR v4.5 + Fix 1)

### Added (2026-04-22)
- `docs/04-renderer-rules.md` — Renderer rules for what to draw vs hide
- `00-Templates/YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md` — Diagram vs question data separation schema
- `topics/51-deconstruction-pipeline.md` — Updated with separation requirement
- `topics/52-baseline-generation.md` — Updated with separation requirement
- `topics/53-intervention.md` — Updated with separation requirement
- `topics/54-qa-testing.md` — Updated with separation requirement
- `01-Projects/Statement-Of-Requirements-v4.5.md` — Added Stage 0 Finding 1 to Decision Log

### Modified (2026-04-22)
- `00-Templates/MATH_DIAGRAM_RENDERING_INSTRUCTION.md` — Updated with diagram vs question separation requirement
- `00-overview.md` — Created with "Always Load" table including renderer rules
- `INDEX.md` — Referenced in 00-overview.md

---

## Key Decisions (v4.5)

### Fix 1: Diagram vs Question Data Separation
- **Decision:** Separate `diagram_data:` (visual elements) from `question:`/`solution:`/`answer_key:` (text, solutions, answers)
- **Reason:** Prevents answer leakage to renderer — students don't see solutions before solving
- **Implementation:** `YAML_SCHEMA_DIAGRAM_QUESTION_SEPARATION.md` schema enforces separation
- **Impact:** All stages (1-5) must respect this separation

---

## Contact & Coordination

- **Daily updates:** CoordinationLog.md
- **Task tracking:** KANBAN.md
- **Topic coordination:** topics/ (51-deconstruction-pipeline.md, 52-baseline-generation.md, 53-intervention.md, 54-qa-testing.md)
- **Version info:** VERSION.md
- **Master index:** [INDEX.md](INDEX.md)

---

*This overview is automatically updated when VERSION.md or key documentation changes.*
