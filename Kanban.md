---
kanban-plugin: basic
---

## DONE
- [x] **T1** Build baseline problem pack (20–25 geometry items)<br>Owner: GeoBot • Topic: 02-Geometry
- [x] **T2** Map items → geometry sub‑pathways + equation shadows<br>Owner: GeoBot • Topic: 02-Geometry • Depends: T1
- [x] **T3** Rubric mapping & acceptance criteria (100% accuracy)<br>Owner: Sean Foo • Topic: 02-Geometry • Depends: T1, T2
- [x] **C1** Define artifact repository location (local path / URL)<br>Owner: BackendBot • Topic: 05-Backend
- [x] **C2** Communicate repo location to RenderBot & MVPBot<br>Owner: Zcaethbot • Topic: PM • Depends: C1
- [x] **C3** Draft backend API spec (OpenAPI or simple Markdown) — Approved by Sean ✅<br>Owner: BackendBot • Topic: 05-Backend
- [x] **C4** Align MVP milestones with backend readiness ✅<br>Owner: MVPBot • Topic: 01-Projects/MVP.md • Depends: C3
- [x] **T4** PDF renders + artifact repo update ✅<br>Owner: RenderBot • Topic: 03-Rendering • Depends: T1, C1
- [x] **T5** OCR pipeline readiness (Tesseract tests) ✅<br>Owner: OcrBot • Topic: 04-OCR
- [x] **C5** MVP implementation (backend + frontend) ✅<br>Owner: LogisticsBureau • Topic: 05-Backend • Depends: C3
- [x] **UAT** UAT executed with 12 student personas (92% accuracy) ✅<br>Owner: TestPlan-Developer • Topic: 01-Projects/UAT-TEST-PLAN.md • Depends: C5
- [x] **PRE-LAUNCH FIXES** Gaming detection (P0) + P1/P2 fixes ✅<br>Owner: Pre-Launch Fixes Engineer • Depends: UAT
- [x] **UX TESTING** 11-year-old perspective (25 issues found) ✅<br>Owner: UX Testing (11YO) • 25 issues categorized
- [x] **ISSUES REPORT** All 25 issues categorized by type & priority ✅
- [x] **PRINT/SCAN DECISION** Accepted for MVP (Issue #2.2) ✅
- [x] **P0‑7 GAMING LANGUAGE** Supportive language implemented (backend + frontend) ✅<br>Owner: Zcaethbot • Issue #2.7 — Most critical UX fix
- [x] **MVP FINAL VERIFICATION** 23 tests, 22 passed, 0 failed ✅<br>Owner: Zcaethbot • Verification script executed 2026-04-16
- [x] **CRITICAL UX FIXES** Gaming language + canvas UI + articulation + dashboard labels ✅<br>Owner: Zcaethbot • 8 MUST-fix issues implemented (see UX_FIXES_VERIFICATION_REPORT.md)
- [x] **DEPLOYMENT ARTIFACTS** Docker + installer + backup + monitoring scripts ✅<br>Owner: Zcaethbot • Deployment artifacts created 2026‑04‑16
- [x] **MEDIUM-PRIORITY UX FIXES** All 11 medium‑priority issues addressed (problem count, progress indicators, milestones clarity, diagram help, bar model notes) ✅<br>Owner: Zcaethbot • All medium‑priority items from UI‑UX‑ISSUES‑CATEGORIZED.md implemented
- [ ] **HANDS‑ON REVIEW** User testing of MVP with all UX improvements ⏳<br>Owner: Sean Foo • Testing gaming detection, canvas tools, simplified labels, "I'm Stuck" button, etc.
- [x] **INFRASTRUCTURE COMPLETION** Health monitoring, firewall, backup/restore, deployment automation ✅<br>Owner: Zcaethbot • Created 4 scripts: health_check.sh, setup_firewall.sh, restore_backup.sh, updated DEPLOYMENT.md

## TO DO

## BLOCKED



%% kanban:settings
```
{"kanban-plugin":"basic","list-collapse":[false,false,false,false]}
```
%%
