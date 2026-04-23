# ATOM-SG Pilot Vault

**Version:** 2.0.0  
**Status:** Framework Revision Complete  
**Last Updated:** 2026-04-19

This is the comprehensive vault for the ATOM-SG Pilot - a Recognition-First Integrated Training System for P6 Mathematics.

---

## 🚀 Quick Start

### New to the project?
1. Read **[INDEX.md](INDEX.md)** - Master navigation and documentation map
2. Check **[VERSION.md](00-Templates/VERSION.md)** - Current version and changelog
3. Review **[MODEL_USAGE_POLICY.md](MODEL_USAGE_POLICY.md)** - GLM selection rules for sub-agents

### Looking for specific information?
| Need | Go To |
|------|-------|
| Complete framework taxonomy | [Framework Revision v2.0](00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md) |
| System gaps & recommendations | [Comprehensive Gap Analysis](00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md) |
| Diagram standards | [Visual Reconstruction Spec](00-Templates/Visual-Reconstruction-Spec.md) |
| Task tracking | [Kanban](01-Projects/KANBAN.md) |
| API documentation | [API.md](05-Backend/API.md) |
| Deployment guide | [DEPLOYMENT.md](05-Backend/DEPLOYMENT.md) |

---

## 📋 Project Overview

ATOM-SG is an adaptive training system for Singapore PSLE P6 Mathematics, featuring:

- **14 Pathway Taxonomy** (5 word problem + 8 geometry + 1 data interpretation)
- **12 Learner Personas** with differentiated support
- **Forced Articulation** - explain before solving
- **Triad Feedback** - pathway + articulation + solution
- **Exam-Quality Visuals** - grid construction, 3D, composite overlap

---

## 📁 Folder Structure

```
ATOM-SG Pilot/
├── 00-Templates/          # Templates and specifications
│   ├── VERSION.md         # Version control
│   ├── CHANGELOG.md       # Change history
│   ├── ATOM-SG_FRAMEWORK_REVISION_v2.md  # Complete taxonomy
│   ├── Visual-Reconstruction-Spec.md     # Diagram standards
│   ├── COMPREHENSIVE_GAP_ANALYSIS.md     # System gaps
│   └── [other templates]
├── 01-Projects/           # Project management
│   ├── KANBAN.md          # Task tracking
│   ├── SubAgentComms.md   # Coordination
│   └── [project docs]
├── 02-Geometry/           # Geometry problems (G001-G025)
├── 03-WordProblems/       # Word problems (WP001-WP020)
├── 04-OCR/                # OCR pipeline
├── 05-Backend/            # FastAPI + Frontend
├── 06-Dashboards/         # Monitoring
└── 07-Backups/            # Backup procedures
```

---

## 🎯 Current Status (v2.0.0)

### What's New
- ✅ Comprehensive gap analysis completed
- ✅ 4 new geometry pathways defined (G5-G8)
- ✅ Data Interpretation pathway formalized
- ✅ 12 persona coverage analysis
- ✅ Visual Reconstruction Specification

### Critical Gaps Identified
- ⚠️ Current baseline covers only ~40% of exam content
- ⚠️ 11 of 12 personas have significant support gaps
- ⚠️ No persona classification system
- ⚠️ No adaptive problem selection
- ⚠️ No interactive model canvas

See [Comprehensive Gap Analysis](00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md) for details.

---

## 📊 Framework Taxonomy (v2.0)

### Word Problem Pathways
1. **Constant-Total Adjustment**
2. **Part-Whole with Comparison**
3. **Before-After Change**
4. **Supposition**
5. **Cross-Thread Collision** (exam standard complexity)
6. **Data Interpretation** (NEW)

### Geometry Pathways
1. **G1:** Angle Reasoning
2. **G2:** Area & Perimeter
3. **G3:** Volume & 3D
4. **G4:** Properties & Classification
5. **G5:** Composite Overlap (NEW)
6. **G6:** Grid Construction (NEW)
7. **G7:** 3D Visualization (NEW)
8. **G8:** Angle Chasing (NEW)

### Data Interpretation Pathways (NEW)
1. **DI1:** Line Graph
2. **DI2:** Bar Graph
3. **DI3:** Pie Chart

---

## 👥 12 Persona Profiles

| Persona | Accuracy | Key Characteristic | Support Needed |
|---------|----------|-------------------|----------------|
| Alex | 95%+ | Perfect student | Challenge problems |
| Brianna | 85% | Visual learner | Interactive canvas |
| Cameron | 75% | Disengaged | Narrative mode |
| Dylan | 65% | Distracted | Focus mode |
| Eve | 50% | Struggling | Intensive scaffolding |
| Fay | 40% | Random guesser | Anti-gaming |
| Grace | 55% | Confused pathways | Pathway training |
| Henry | 60% | Anxious | Anxiety-reducing UI |
| Ivy | 70% | Critical UI-focused | Feedback mechanisms |
| Jack | Variable | Gamer | Gaming detection |
| Kevin | 80% | Visual/weak articulation | Visual articulation |
| Liam | 60% | Reading struggles | TTS, simplified text |

---

## 🔧 Sub-Agent Guidelines

### Before Starting Work
1. **Check MODEL_USAGE_POLICY.md** - Select appropriate GLM model
2. **Review Kanban** - Understand current priorities
3. **Read relevant templates** in 00-Templates/

### While Working
1. **Follow templates** for consistency
2. **Update SubAgentComms.md** with progress
3. **Reference INDEX.md** for navigation

### After Completing
1. **Update VERSION.md** if making significant changes
2. **Update CHANGELOG.md** with changes
3. **Commit to Git** with descriptive message

---

## 📝 Documentation Standards

### Creating New Problems
Use templates in `00-Templates/`:
- [Problem-Card.md](00-Templates/Problem-Card.md) - Problem structure
- [Visual-Reconstruction-Spec.md](00-Templates/Visual-Reconstruction-Spec.md) - Diagram specs
- [Rubric.md](00-Templates/Rubric.md) - Assessment criteria

### Code Changes
- Backend: Follow [API.md](05-Backend/API.md)
- Frontend: Check existing modules in `05-Backend/frontend/static/js/`
- Tests: Add to `05-Backend/playwright-tests/`

### Documentation Updates
- Major changes: Update VERSION.md and CHANGELOG.md
- New features: Add to INDEX.md
- Breaking changes: Document in framework revision

---

## 🔄 Git Workflow

```bash
# Pull latest changes
git pull origin main

# Make your changes
# ... edit files ...

# Stage and commit
git add -A
git commit -m "Descriptive message about changes"

# Push to remote
git push origin main
```

Note: GitHub has branch protection. Direct push may require bypass for maintainers.

---

## 📞 Support & Coordination

| Need | Contact Method |
|------|---------------|
| Daily updates | SubAgentComms.md |
| Task questions | Kanban.md comments |
| Version info | VERSION.md |
| Navigation | INDEX.md (this file) |
| Framework questions | Framework Revision v2.0 |

---

## 📚 Key Documents Reference

### Essential Reading
- [INDEX.md](INDEX.md) - Start here for navigation
- [VERSION.md](00-Templates/VERSION.md) - Version info
- [CHANGELOG.md](00-Templates/CHANGELOG.md) - Change history
- [MODEL_USAGE_POLICY.md](MODEL_USAGE_POLICY.md) - GLM rules

### Framework & Analysis
- [ATOM-SG_FRAMEWORK_REVISION_v2.md](00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md) - Complete taxonomy
- [COMPREHENSIVE_GAP_ANALYSIS.md](00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md) - System gaps
- [Visual-Reconstruction-Spec.md](00-Templates/Visual-Reconstruction-Spec.md) - Diagram standards

### Project Management
- [Kanban](01-Projects/KANBAN.md) - Task tracking
- [SubAgentComms](01-Projects/SubAgentComms.md) - Coordination

### Technical
- [API.md](05-Backend/API.md) - API specification
- [DEPLOYMENT.md](05-Backend/DEPLOYMENT.md) - Deployment guide

---

## 🎯 Next Priorities (v2.1.0)

Based on gap analysis:

1. **Persona Classification System** - Classify students into 12 personas
2. **Adaptive Problem Selection** - Persona-aware problem routing
3. **Interactive Model Canvas** - Visual learning support
4. **Gaming Detection** - Jack persona protection
5. **Anxiety-Reducing UI** - Henry persona support

See [Comprehensive Gap Analysis](00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md) for full roadmap.

---

## 📜 License & Attribution

ATOM-SG Pilot - Recognition-First Integrated Training System  
Created for Singapore PSLE P6 Mathematics preparation.

---

*Last updated: 2026-04-19 | Version 2.0.0*

*For latest updates, check [CHANGELOG.md](00-Templates/CHANGELOG.md)*
