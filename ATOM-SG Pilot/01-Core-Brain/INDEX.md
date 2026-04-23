# ATOM-SG Pilot - Master Index

**Project:** ATOM-SG Pilot - P6 Mathematics Training System  
**Version:** 2.0.0  
**Last Updated:** 2026-04-19  

---

## Quick Navigation

### 🎯 Start Here
| Document | Purpose | Audience |
|----------|---------|----------|
| [README.md](README.md) | Project overview | Everyone |
| [VERSION.md](00-Templates/VERSION.md) | Version history | Developers |
| [MODEL_USAGE_POLICY.md](MODEL_USAGE_POLICY.md) | GLM selection rules | Sub-agents |
| [00-overview.md](00-overview.md) | Project overview, always load table | Everyone |

### 📊 Current Status
| Document | Purpose | Last Updated |
|----------|---------|--------------|
| [Framework Revision v2.0](00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md) | Complete taxonomy | 2026-04-19 |
| [Visual Reconstruction Spec](00-Templates/Visual-Reconstruction-Spec.md) | Diagram standards | 2026-04-19 |
| [Comprehensive Gap Analysis](00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md) | System gaps | 2026-04-19 |
| [Kanban](01-Projects/KANBAN.md) | Task tracking | Daily |
| [SubAgent Comms](01-Projects/SubAgentComms.md) | Coordination | Daily |

---

## Documentation Structure

### 00-Templates/
Templates and specifications for consistent content creation.

| File | Version | Purpose |
|------|---------|---------|
| [VERSION.md](00-Templates/VERSION.md) | 2.0.0 | Version control |
| [ATOM-SG_FRAMEWORK_REVISION_v2.md](00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md) | 2.0 | Complete framework |
| [Visual-Reconstruction-Spec.md](00-Templates/Visual-Reconstruction-Spec.md) | 1.0 | Diagram specs |
| [COMPREHENSIVE_GAP_ANALYSIS.md](00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md) | 1.0 | Gap analysis |
| [EXAM_RECONSTRUCTION_STANDARDS.md](00-Templates/EXAM_RECONSTRUCTION_STANDARDS.md) | 2.0 | Quality standards |
| [Baseline-Spec.md](00-Templates/Baseline-Spec.md) | 1.0 | Test specs |
| [Problem-Card.md](00-Templates/Problem-Card.md) | 1.0 | Problem template |
| [Rubric.md](00-Templates/Rubric.md) | 1.0 | Assessment template |
| [Render-Note.md](00-Templates/Render-Note.md) | 1.0 | Render docs |
| [Milestone-Template.md](00-Templates/Milestone-Template.md) | 1.0 | Milestone template |
| [Risk-Template.md](00-Templates/Risk-Template.md) | 1.0 | Risk template |

### 01-Projects/
Project management and coordination.

| File | Purpose |
|------|---------|
| [KANBAN.md](01-Projects/KANBAN.md) | Task tracking (T1-T5, C1-C4) |
| [SubAgentComms.md](01-Projects/SubAgentComms.md) | Cross-agent coordination |
| [Baseline.md](01-Projects/Baseline.md) | Baseline test planning |
| [P0-6_TRACKING_COMPLETED.md](01-Projects/P0-6_TRACKING_COMPLETED.md) | Issue tracking |
| [P0_P1_IMPLEMENTATION_PLAN.md](01-Projects/P0_P1_IMPLEMENTATION_PLAN.md) | Implementation plan |
| [LESSON_LEARNED_WordProblems_Missing.md](01-Projects/LESSON_LEARNED_WordProblems_Missing.md) | Lessons learned |

### 02-Geometry/
Geometry problems and taxonomy.

| File | Purpose |
|------|---------|
| [Problem-Pack-Plan.md](02-Geometry/Problem-Pack-Plan.md) | 25-item geometry plan |
| [Geometry-Rubrics.md](02-Geometry/Geometry-Rubrics.md) | Assessment rubrics |
| [Geometry-Subpathway-Mapping.md](02-Geometry/Geometry-Subpathway-Mapping.md) | Sub-pathway mapping |
| [Geometry-Rubric-Mapping.md](02-Geometry/Geometry-Rubric-Mapping.md) | Rubric mapping |
| [problems/G001.md](02-Geometry/problems/G001.md) - G025.md | Individual problems |

### 03-WordProblems/
Word problems (Before-After, Part-Whole, Cross-Thread).

| File | Purpose |
|------|---------|
| [README.md](03-WordProblems/README.md) | WP documentation |
| [problems/WP001.md](03-WordProblems/problems/WP001.md) - WP020.md | Individual problems |

### 04-OCR/
OCR pipeline documentation.

| File | Purpose |
|------|---------|
| [README.md](04-OCR/README.md) | OCR documentation |

### 05-Backend/
Backend API and frontend.

| File | Purpose |
|------|---------|
| [README.md](05-Backend/README.md) | Backend docs |
| [API.md](05-Backend/API.md) | API specification |
| [DEPLOYMENT.md](05-Backend/DEPLOYMENT.md) | Deployment guide |
| [main.py](05-Backend/main.py) | FastAPI application |
| [frontend/index.html](05-Backend/frontend/index.html) | Frontend entry |
| [frontend/static/js/](05-Backend/frontend/static/js/) | JavaScript modules |
| [playwright-tests/](05-Backend/playwright-tests/) | E2E tests |

### 06-Dashboards/
Monitoring and dashboards.

| File | Purpose |
|------|---------|
| [README.md](06-Dashboards/README.md) | Dashboard docs |
| [Problem-Bank-Dashboard.md](06-Dashboards/Problem-Bank-Dashboard.md) | Problem status |
| [Milestones-Dashboard.md](06-Dashboards/Milestones-Dashboard.md) | Milestone tracking |
| [Risks-Dashboard.md](06-Dashboards/Risks-Dashboard.md) | Risk tracking |

### 07-Backups/
Backup and recovery.

| File | Purpose |
|------|---------|
| [README.md](07-Backups/README.md) | Backup procedures |

---

## Framework Taxonomy (v2.0)

### Word Problem Pathways
1. **Constant-Total Adjustment** - Problems with fixed totals
2. **Part-Whole with Comparison** - Ratio + difference problems
3. **Before-After Change** - Sequential state changes
4. **Supposition** - Assumption-based problems
5. **Cross-Thread Collision** - Multi-concept fusion (exam standard)
6. **Data Interpretation** (NEW) - Graphs, charts, reverse calc

### Geometry Pathways
1. **G1: Angle Reasoning** - Protractor, properties
2. **G2: Area & Perimeter** - Rectilinear figures
3. **G3: Volume & 3D** - Cuboids, nets
4. **G4: Properties & Classification** - Shapes
5. **G5: Composite Overlap** (NEW) - Overlapping shapes
6. **G6: Grid Construction** (NEW) - Grid-based tasks
7. **G7: 3D Visualization** (NEW) - Isometric solids
8. **G8: Angle Chasing** (NEW) - Multi-shape angles

### Data Interpretation Pathways (NEW)
1. **DI1: Line Graph** - Rate of change, reverse calc
2. **DI2: Bar Graph** - Comparison, average
3. **DI3: Pie Chart** - Sectors, ratios

---

## 12 Persona Profiles

| ID | Persona | Accuracy | Key Need |
|----|---------|----------|----------|
| 1 | Alex | 95%+ | Challenge/extension |
| 2 | Brianna | 85% | Visual scaffolding |
| 3 | Cameron | 75% | Engagement/motivation |
| 4 | Dylan | 65% | Focus/attention |
| 5 | Eve | 50% | Intensive help |
| 6 | Fay | 40% | Anti-gaming/engagement |
| 7 | Grace | 55% | Pathway training |
| 8 | Henry | 60% | Anxiety support |
| 9 | Ivy | 70% | UI feedback |
| 10 | Jack | Variable | Gaming detection |
| 11 | Kevin | 80% | Visual articulation |
| 12 | Liam | 60% | Reading support |

---

## Recent Changes (v2.0)

### Added
- Comprehensive gap analysis (training, backend, frontend, personas)
- Visual Reconstruction Specification format
- 4 new geometry pathways (G5-G8)
- Data Interpretation pathway (DI1-DI3)
- 12 persona coverage analysis
- VERSION.md for version control
- INDEX.md (this file)

### Modified
- Framework taxonomy expanded (5 → 14 pathways)
- Rendering requirements increased
- Persona-aware system requirements added

### Deprecated
- v1.x simple taxonomy (retained for reference)

---

## Workflow

### For Sub-Agents
1. Check [MODEL_USAGE_POLICY.md](MODEL_USAGE_POLICY.md) for GLM selection
2. Review [Kanban](01-Projects/KANBAN.md) for current tasks
3. Update [SubAgentComms](01-Projects/SubAgentComms.md) with progress
4. Follow templates in [00-Templates/](00-Templates/)

### For Developers
1. Check [VERSION.md](00-Templates/VERSION.md) for current version
2. Review [API.md](05-Backend/API.md) for endpoints
3. Follow [DEPLOYMENT.md](05-Backend/DEPLOYMENT.md) for deployment
4. Update documentation when making changes

### For PM
1. Monitor [Kanban](01-Projects/KANBAN.md)
2. Review [SubAgentComms](01-Projects/SubAgentComms.md)
3. Check [Milestones-Dashboard](06-Dashboards/Milestones-Dashboard.md)
4. Track risks in [Risks-Dashboard](06-Dashboards/Risks-Dashboard.md)

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

- **Daily updates:** SubAgentComms.md
- **Task tracking:** KANBAN.md
- **Version info:** VERSION.md
- **Master index:** This file (INDEX.md)

---

*This index is automatically updated when VERSION.md changes.*
