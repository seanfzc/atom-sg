# ATOM-SG Pilot - Kanban Board
*Last updated: 2026-04-17 16:20 SGT*

## Sub-Agent Definitions
- **PM Owner:** Zcaethbot (overall coordination, updates Kanban, weekly summaries)
- **Geometry Owner:** GeoBot (geometry problem pack, mapping, rubric support)
- **Rendering Owner:** RenderBot (PDF renders, artifact repo updates)
- **OCR Owner:** OcrBot (OCR pipeline readiness, Tesseract tests)
- **Backend Owner:** BackendBot (backend scaffold, REST API, artifact storage)
- **MVP Owner:** MvpBot (integrated recognition-first loop, cross-thread collision practice)
- **Dashboards Owner:** DashBot (dashboard templates, Dataview renderings)
- **Backups Owner:** BackupBot (Git-backed backups, automated commits)
- **QA/Review Owner:** Sean Foo (rubric mapping, acceptance criteria)

---

## 🔴 TO DO

### Week 2 - Integrated Recognition-First (Launch: 2026-04-26)

| # | Task | Owner | Topic/Thread | Depends On | Notes |
|---|------|-------|-------------|------------|-------|
| T9 | Perform transfer test (Week 5 validation) | QA Team (Sean + Sub-agents) | 07-Backups | Week 2 completion | Final validation of success criteria (≥90% pathway ID, ≥90% articulation, ≥80% solving) |

---

## 🟡 IN PROGRESS

*(No tasks currently in progress)*

---

## ⏸️ ON HOLD - Awaiting Go-Ahead Signal

*(No tasks currently on hold)*

---

## 🟢 DONE

### Coordination & Planning

| # | Task | Owner | Completed | Notes |
|---|------|-------|-----------|-------|
| C0 | Statement of Requirements — **approved** | MvpBot | 2026-04-14 17:57 SGT | SOR v4.1 approved by Sean Foo; all open decisions resolved. |
| C1 | Define artifact repository location | BackendBot | 2026-04-13 00:15 SGT | Location: `ATOM-SG Pilot/05-Backend/artifacts/` with subfolders `renders/`, `ocr/`. |
| C2 | Communicate repo location to RenderBot & MVPBot | Zcaethbot | 2026-04-13 00:15 SGT | Communicated via SubAgentComms.md. |
| C3 | Backend API spec — **approved** | BackendBot | 2026-04-15 06:16 SGT | API spec approved with condition: proportional rendering implementation required (≤5% deviation). |
| C4 | MVP alignment with backend — **completed** | MvpBot | 2026-04-15 06:21 SGT | MVP.md created with complete backend endpoint mapping, user flows, timeline (Weeks 2-5), and technical considerations. |
| C5 | Implement MVP (backend + frontend) | Logistics Bureau | 2026-04-16 07:30 SGT | **COMPLETE.** Backend + frontend implemented, 33 UAT bug fixes applied, final verification passed (22/23 tests). |

### Geometry & Content

| # | Task | Owner | Completed | Notes |
|---|------|-------|-----------|-------|
| T1 | Build baseline problem pack (20-25 geometry items) | GeoBot | 2026-04-13 10:30 SGT | 25 geometry problems created in `02-Geometry/problems/`; mapping plan in `Problem-Pack-Plan.md` |
| T2 | Map items → geometry sub-pathways + equation shadows | GeoBot | 2026-04-13 10:30 SGT | Mapping file `Geometry-Subpathway-Mapping.md` created with sub-pathway and equation shadow mapping |
| T3 | Rubric mapping & acceptance criteria (80%+ accuracy) | Sean Foo | 2026-04-13 13:00 SGT | Rubric mapping finalised with corrections (Zone A Level 2, 100% threshold, G007 tightened). |
| T4 | PDF renders + artifact repo update | RenderBot | 2026-04-13 14:37 SGT | 25 PDF diagrams + metadata stored in artifacts/renders/; manifest & README created. |
| T5 | OCR pipeline readiness (Tesseract tests) | OcrBot | 2026-04-15 08:30 SGT | **COMPLETE.** Tesseract 5.5.2 verified, 88-96% confidence, preprocessing pipeline configured, 70% threshold set. Ready for production. |
| T10 | Generate problem cards 009-028 | RenderBot | 2026-04-17 14:26 SGT | **COMPLETE.** All 28 problem cards (P5-Problem-001.md through P5-Problem-028.md) created in `01-Projects/Baseline/`. Chunked approach successful. |

### Backend Implementation (C5)

| # | Task | Owner | Completed | Notes |
|---|------|-------|-----------|-------|
| T6 | Implement backend core endpoints | BackendBot | 2026-04-15 | **COMPLETE.** All 19 endpoints functional: problems, rubrics, renders, practice-sessions, pathway-radar, milestones, reflections, scans, glossary. |
| T7 | Integrate recognition-first loop (MVP integration) | MvpBot | 2026-04-15 | **COMPLETE.** Forced articulation, triad feedback, pathway type selection, equation shadows all integrated. |
| T8 | Create dashboard for milestone tracking & problem bank | DashBot | 2026-04-16 | **COMPLETE.** Dashboard with progress indicators, milestone requirements, Today's Mission card. |

### UAT Bug Fixes (33 Total)

| Priority | Count | Status | Key Fixes |
|----------|-------|--------|-----------|
| P0 - Critical | 8 | ✅ Complete | Forced articulation validation, gaming detection, proportional rendering, canvas tools, collision detection, glossary, range validation |
| P1 - High | 15 | ✅ Complete | Timer management, feedback truncation, error handling, state management, loading states, confidence tracking |
| P2 - Low | 10 | ✅ Complete | Tooltips, help modal, keyboard shortcuts, auto-save, print optimization, randomization |

### Verification & UX

| # | Task | Owner | Completed | Notes |
|---|------|-------|-----------|-------|
| V1 | Final MVP Verification | Zcaethbot | 2026-04-16 06:55 SGT | **PASSED (22/23).** All critical components functional. 1 warning (CORS headers - non-critical). |
| V2 | Medium-Priority UX Fixes | Zcaethbot | 2026-04-16 07:30 SGT | **COMPLETE.** 11 UX fixes: problem count display, progress indicators, milestone explanations, diagram help buttons, color mismatch notes. |
| V3 | START HERE Button Fix | Zcaethbot | 2026-04-17 13:50 SGT | **DEPLOYED.** Changed from JS button to direct `<a>` tag link. PDF now opens reliably in new tab. |
| V4 | PDF Layout Fix | Zcaethbot | 2026-04-17 13:50 SGT | **DEPLOYED.** Rewrote `generate_week_test_pdf()` with proper 1" margins. Text no longer overflows. |
| T11 | Playwright E2E Test Suite | QA Team | 2026-04-17 16:20 SGT | **COMPLETE.** 90 tests (23 critical + 67 UI). Mock API layer, test pyramid strategy, CI/CD integration. See `05-Backend/playwright-tests/`. |

---

## ⚡ SYSTEM BLOCKER - RESOLVED

| # | Task | Owner | Blocker | Action Needed |
|---|------|-------|---------|---------------|
| S1 | OpenRouter model billing error | Zcaethbot | ✅ **Resolved** | Credit approved, model switched to GLM-4.7. Sub-agents operational. |
| S2 | Subagent timeout (problem generation) | Zcaethbot | ✅ **Resolved** | Chunked approach implemented (≤5 items per batch, explicit timeouts). |

## 🚫 BLOCKED

*(No tasks currently blocked.)*

---

## 📊 Project Summary

### Current Status: **MVP COMPLETE — ALL CONTENT READY**

| Phase | Status | Completion |
|-------|--------|------------|
| Planning (C0-C4) | ✅ Done | 100% |
| Backend (T5-T6) | ✅ Done | 100% |
| Frontend (T7-T8) | ✅ Done | 100% |
| Bug Fixes (33 total) | ✅ Done | 100% |
| Verification | ✅ Done | 96% (22/23 tests) |
| UX Polish | ✅ Done | 100% |
| Content (Problem Cards) | ✅ Done | 100% (28/28 complete) |
| Testing (Playwright) | ✅ Done | 100% (90 tests, 23 critical) |

### Next Milestone
- **Week 2 Pilot Launch:** 2026-04-26
- **Blockers:** None
- **Risks:** None — All deliverables complete
- **Test Coverage:** 90 tests (23 critical pilot tests + 67 UI tests) with mock API layer

---

## How to Read This Board
- Check this file for current status of all tasks across all workstreams.
- Each task maps to a **Topic/Thread** (vault folder) and an **Owner** (sub-agent or Sean).
- PM Owner (Zcaethbot) updates this board after every status change.
- Sean reviews during weekly summaries or on demand.
