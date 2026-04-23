# ATOM-SG Pilot - Version Control

**Current Version:** 2.0.0  
**Last Updated:** 2026-04-19  
**Status:** Framework Revision Complete

---

## Version History

### v2.0.0 (2026-04-19) - Framework Revision
**Major Changes:**
- Comprehensive gap analysis completed
- 4 new geometry pathways added (G5-G8)
- New Data Interpretation pathway formalized (DI1-DI3)
- Visual Reconstruction Specification format created
- 12 persona coverage analysis completed
- Training programme gaps identified
- Backend/frontend gaps documented

**New Documentation:**
- `ATOM-SG_FRAMEWORK_REVISION_v2.md`
- `Visual-Reconstruction-Spec.md`
- `COMPREHENSIVE_GAP_ANALYSIS.md`

**Breaking Changes:**
- Problem taxonomy expanded (14 pathways vs 5)
- Rendering requirements increased
- Persona-aware system required

### v1.1.0 (2026-04-16) - MVP Completion
- MVP final verification passed
- 20 word problems created (WP001-WP020)
- 25 geometry problems created (G001-G025)
- Playwright E2E tests implemented
- CI/CD with Telegram notifications

### v1.0.0 (2026-04-12) - Pilot Launch
- Initial framework with 5 pathways
- Basic geometry taxonomy
- Backend MVP
- Frontend MVP

---

## Documentation Index

### Core Framework
| Document | Version | Location | Purpose |
|----------|---------|----------|---------|
| Framework Revision | v2.0 | `00-Templates/ATOM-SG_FRAMEWORK_REVISION_v2.md` | Complete taxonomy |
| Visual Reconstruction | v1.0 | `00-Templates/Visual-Reconstruction-Spec.md` | Diagram standards |
| Gap Analysis | v1.0 | `00-Templates/COMPREHENSIVE_GAP_ANALYSIS.md` | System gaps |
| Model Usage Policy | v1.0 | `MODEL_USAGE_POLICY.md` | GLM selection rules |

### Templates
| Template | Version | Purpose |
|----------|---------|---------|
| Problem Card | v1.0 | Problem creation |
| Rubric | v1.0 | Assessment criteria |
| Baseline Spec | v1.0 | Test specification |
| Render Note | v1.0 | Render documentation |

### Project Tracking
| Document | Location | Purpose |
|----------|----------|---------|
| Kanban | `01-Projects/KANBAN.md` | Task tracking |
| SubAgent Comms | `01-Projects/SubAgentComms.md` | Coordination |
| P0-6 Tracking | `01-Projects/P0-6_TRACKING_COMPLETED.md` | Issue tracking |

---

## Consistency Checklist

When updating documentation, ensure:

- [ ] VERSION.md updated with new version number
- [ ] All cross-references updated
- [ ] Git commit with descriptive message
- [ ] README.md index updated if needed
- [ ] Related templates checked for consistency
- [ ] Breaking changes documented

---

## Quick Reference

### Pathway Taxonomy (v2.0)
```
Word Problems (5 + 1 NEW):
  1. Constant-Total Adjustment
  2. Part-Whole with Comparison
  3. Before-After Change
  4. Supposition
  5. Cross-Thread Collision
  6. Data Interpretation (NEW)

Geometry (4 + 4 NEW):
  G1: Angle Reasoning
  G2: Area & Perimeter
  G3: Volume & 3D
  G4: Properties & Classification
  G5: Composite Overlap (NEW)
  G6: Grid Construction (NEW)
  G7: 3D Visualization (NEW)
  G8: Angle Chasing (NEW)

Data Interpretation (NEW - 3 total):
  DI1: Line Graph
  DI2: Bar Graph
  DI3: Pie Chart
```

### 12 Personas
```
1. Alex (Perfect, 95%+)
2. Brianna (Visual, 85%)
3. Cameron (Disengaged, 75%)
4. Dylan (Distracted, 65%)
5. Eve (Struggling, 50%)
6. Fay (Random, 40%)
7. Grace (Confused, 55%)
8. Henry (Anxious, 60%)
9. Ivy (Critical, 70%)
10. Jack (Gamer, variable)
11. Kevin (Visual/Weak Articulation, 80%)
12. Liam (Reading Struggles, 60%)
```

---

## Next Version Planning

### v2.1.0 (Planned)
- [ ] Implement persona classification system
- [ ] Create adaptive problem selection
- [ ] Build interactive model canvas
- [ ] Add gaming detection (Jack)
- [ ] Implement anxiety-reducing UI (Henry)

### v2.2.0 (Planned)
- [ ] Spaced repetition system
- [ ] Parent/teacher dashboards
- [ ] Social features
- [ ] Mobile optimization

---

## Contact

For questions about versioning or documentation consistency:
- Check this VERSION.md first
- Review related documents in 00-Templates/
- Update SubAgentComms.md with coordination needs
