# Changelog

All notable changes to the ATOM-SG Pilot project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [2.0.0] - 2026-04-19

### Added
- **Comprehensive Gap Analysis** documenting system-wide gaps across:
  - Training/intervention programme (differentiated instruction, metacognitive training, transfer practice)
  - Backend system (persona-aware data model, adaptive algorithms, gaming detection)
  - Frontend system (interactive canvas, accessibility, anxiety-reducing UI)
  - 12 persona coverage analysis with detailed gap assessment
- **Visual Reconstruction Specification** format for exam-quality diagram creation
- **4 New Geometry Pathways**:
  - G5: Composite Overlap (overlapping shapes, shaded regions)
  - G6: Grid Construction (square grid, construction tasks)
  - G7: 3D Visualization (isometric solids, orthographic projections)
  - G8: Angle Chasing (multi-shape composites, reflex angles)
- **New Data Interpretation Pathway** (formal pathway with 3 sub-types):
  - DI1: Line Graph (rate of change, reverse percentage)
  - DI2: Bar Graph (comparison, average calculations)
  - DI3: Pie Chart (sectors, ratio conversion)
- **VERSION.md** for version control and consistency tracking
- **INDEX.md** as master navigation document

### Changed
- **Framework Taxonomy** expanded from 5 to 14 total pathways
- **Rendering Requirements** significantly increased for exam-quality visuals
- **Problem Complexity** standards raised to Cross-Thread Collision level
- **Documentation Structure** reorganized with consistent templates

### Deprecated
- Simple v1.x taxonomy (retained for backward reference)
- Basic matplotlib-only rendering approach

### Known Issues
- Current baseline test covers only ~40% of exam content
- 11 of 12 personas have significant support gaps
- No persona classification system implemented
- No adaptive problem selection implemented
- Interactive model canvas not implemented

---

## [1.1.0] - 2026-04-16

### Added
- MVP final verification completed (22/23 tests passing)
- 20 word problems created (WP001-WP020) covering Before-After, Part-Whole, Cross-Thread
- 25 geometry problems created (G001-G025) with nano-node mapping
- Playwright E2E test suite with 8 test categories
- CI/CD pipeline with GitHub Actions
- Telegram notifications for test results
- Self-hosted runner configuration for MacBook Neo
- Docker deployment configuration
- Backup and health check automation

### Changed
- Backend API finalized with 15+ endpoints
- Frontend UI with P0/P1/P2 fixes implemented
- Problem database populated with 45 total problems

### Fixed
- P0-1: Pathway type validation in practice submissions
- P0-2: Gaming detection algorithm
- P0-3: Vocabulary gap detection and glossary
- P0-4: Step-by-step scaffolding
- P0-5: Progress persistence
- P0-6: Visual-text mismatch detection
- P0-7: Common mistake patterns

---

## [1.0.0] - 2026-04-12

### Added
- Initial ATOM-SG Pilot framework
- 5 core word problem pathways:
  - Constant-Total Adjustment
  - Part-Whole with Comparison
  - Before-After Change
  - Supposition
  - Cross-Thread Collision
- 4 basic geometry pathways (G1-G4)
- FastAPI backend with basic endpoints
- Vanilla JavaScript frontend
- Problem card templates
- Rubric templates
- Forced articulation system
- Triad feedback mechanism
- Pathway Radar warm-up

### Infrastructure
- Project folder structure established
- Git repository initialized
- Basic CI workflow
- Documentation templates

---

## [Unreleased]

### Planned for v2.1.0
- [ ] Persona classification system
- [ ] Adaptive problem selection algorithm
- [ ] Interactive model canvas (Fabric.js/Konva.js)
- [ ] Gaming detection for Jack persona
- [ ] Anxiety-reducing UI mode for Henry persona
- [ ] Text-to-speech integration for Liam persona

### Planned for v2.2.0
- [ ] Spaced repetition system
- [ ] Parent/teacher dashboards
- [ ] Social features (peer discussion)
- [ ] Mobile PWA
- [ ] Advanced analytics

---

## Versioning Notes

### Major Version (X.0.0)
- Breaking changes to taxonomy or API
- New pathway categories
- Architecture changes

### Minor Version (x.Y.0)
- New features (problems, renderers, personas)
- Non-breaking enhancements
- Documentation improvements

### Patch Version (x.y.Z)
- Bug fixes
- Minor corrections
- Template updates

---

## How to Update This Changelog

1. Add new version section at top
2. Categorize changes (Added, Changed, Deprecated, Removed, Fixed, Security)
3. Reference Git commits where applicable
4. Update VERSION.md with new version number
5. Update INDEX.md if structure changes
