# Dashboards

Dashboard templates for Milestones, Risks, and Problem Bank using Dataview.

## Available Dashboards

1. **Milestones Dashboard** (`Milestones-Dashboard.md`)
   - Overview of project milestones with status, due dates, and progress.
   - Assumes milestone notes with `type: milestone` in frontmatter.

2. **Risks Dashboard** (`Risks-Dashboard.md`)
   - Track project risks with severity, impact, and mitigation status.
   - Assumes risk notes with `type: risk` in frontmatter.

3. **Problem Bank Dashboard** (`Problem-Bank-Dashboard.md`)
   - Counts of problems by pathway, difficulty, and geometry vs non‑geometry.
   - Assumes problem cards with `type: problem` and fields `pathwayType`, `difficulty`.
   - Geometry vs non‑geometry is determined by `pathwayType` prefix `geometry_`.

## Templates

Corresponding templates are available in `../00-Templates/`:
- `Milestone-Template.md`
- `Risk-Template.md`
- `Problem-Card.md` (updated)

## Usage

1. Ensure the [Dataview plugin](https://github.com/blacksmithgu/obsidian-dataview) is installed in Obsidian.
2. Create notes using the templates, filling in the frontmatter fields.
3. Open the dashboard files to see automatically updated tables and summaries.

## Customization

Edit the Dataview queries in each dashboard to adjust grouping, sorting, or add new metrics.

## Notes
- All queries assume notes are located within the `ATOM‑SG Pilot` vault folder.
- If you move notes, update the `FROM` clause in the queries.
- For best results, keep frontmatter fields consistent.

