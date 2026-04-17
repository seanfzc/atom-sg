---
dashboard: milestones
title: Milestones Dashboard
description: Overview of project milestones with status, due dates, and progress.
---

```dataview
TABLE name, due, status, progress
FROM "ATOM-SG Pilot"
WHERE type = "milestone"
SORT due ASC
```

## Columns Description
- **name**: Milestone title (e.g., Week 2 – Integrated Intervention)
- **due**: Due date (YYYY-MM-DD)
- **status**: One of: planned, in-progress, completed, blocked
- **progress**: Optional percentage (0-100) or progress bar

## How to Add Milestones
1. Create a new note in the appropriate folder (e.g., `01-Projects/Milestone-Week1.md`)
2. Include the following frontmatter:

```yaml
---
type: milestone
id: Milestone-Week1
name: Week 1 – Baseline
due: 2026-04-19
status: planned
progress: 0
---
```

3. The dashboard will automatically include the milestone.

## Current Summary
```dataviewjs
const milestones = dv.pages('"ATOM-SG Pilot"').filter(p => p.type === "milestone");
const total = milestones.length;
const completed = milestones.filter(m => m.status === "completed").length;
const inProgress = milestones.filter(m => m.status === "in-progress").length;
const overdue = milestones.filter(m => m.due && new Date(m.due) < new Date() && m.status !== "completed").length;

dv.header(3, "Summary");
dv.list([
	`Total milestones: ${total}`,
	`Completed: ${completed}`,
	`In progress: ${inProgress}`,
	`Overdue: ${overdue}`
]);
```