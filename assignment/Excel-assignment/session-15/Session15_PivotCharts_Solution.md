# Session 15 – PivotCharts + Slicers + Timelines
## Solved Assignment

**Dataset used:** `ipl_matches.xlsx` (attached alongside this file)
A synthetic IPL-style dataset covering **5 seasons (2021–2025)**, 300 matches, 600 rows (one row per team per match, so each match appears twice — once from each team's perspective, which is what makes "matches played per team" and "wins per team" a simple count).

| Column | Description |
|---|---|
| Match ID | Unique match number (shared by both rows of a match) |
| Season | IPL year (2021–2025) |
| Match Date | Date the match was played |
| Venue | Stadium the match was played at |
| Team | The team this row is about |
| Opponent | The team they played against |
| Result | `Won` / `Lost` for the `Team` column |

> Note: IPL data isn't available as an official "download" button anywhere — this dataset was generated to mirror the exact structure (Match Date, Team, Venue, Result) that real ball-by-ball / match-summary IPL datasets (e.g., the ones on Kaggle) use, so the steps below transfer directly to a real file too.

---

## Task 1 — PivotChart: Total Matches Played by Each Team

**Steps:**
1. Select any cell in the `Matches` table → **Insert → PivotChart** (this creates the PivotTable *and* chart together).
2. In the field list:
   - Drag **Team** → **Axis (Categories)**
   - Drag **Match ID** → **Values** → set to **Count** (right-click the field in Values → Value Field Settings → **Count**, not Sum, since Match ID is a number)
3. Excel defaults to a clustered column chart — that's fine for "total matches played," or switch to a bar chart via **PivotChart Design → Change Chart Type → Bar**.

**Result:** one bar per team, height = number of matches played (should be roughly equal across teams since it's a round-robin-style schedule — a good sanity check that your Count formula is right).

---

## Task 2 — Slicer on Venue

**Steps:**
1. Click the PivotChart → **PivotChart Analyze tab → Filter → Insert Slicer**.
2. Tick **Venue** → **OK**.
3. Click any stadium in the slicer (e.g., **"Eden Gardens, Kolkata"**) — the chart instantly recalculates to show only matches played at that venue, letting you compare which teams play most/win most at a given ground.
4. Ctrl-click to select multiple venues at once; click the eraser/funnel icon on the slicer to clear the filter.

---

## Task 3 — Timeline Slicer on Match Date

**Steps:**
1. Click the PivotChart → **PivotChart Analyze tab → Filter → Insert Timeline**.
2. Tick **Match Date** → **OK**.
3. A horizontal Timeline control appears, defaulting to **Months**. Click the level dropdown in its corner and switch to **Years** to browse season-by-season, or keep **Months** to zoom into a specific stretch of a season.
4. Drag the timeline's selection handles to a range (e.g., just March–May 2023) — the chart updates to show only that window's matches.

*(Timeline ≠ Slicer: a Timeline is purpose-built for date fields — it gives you a draggable range instead of a checkbox list, which is what "across different IPL seasons or months" calls for.)*

---

## Task 4 — Interactive Dashboard: Bar Chart + Line Chart, Linked to the Same Slicer & Timeline

**Steps:**
1. **Build Chart 1 (Bar — Total Wins by Team):**
   - Insert → PivotChart → new PivotTable.
   - **Team** → Axis, **Result** → Filter (set to only `Won`), **Match ID** → Values (Count).
   - Chart type: **Clustered Bar**.
2. **Build Chart 2 (Line — Matches Played Over Time):**
   - Insert another PivotChart → new PivotTable.
   - **Match Date** → Axis (right-click → Group → **Months** and **Years**), **Match ID** → Values (Count).
   - Chart type: **Line**.
3. **Link both charts to one Venue slicer:**
   - Click the Venue slicer (from Task 2) → **Slicer tab → Report Connections** (Excel) / **Filter Connections** (Google Sheets doesn't support this — needs desktop Excel).
   - Tick **both** PivotTables (the one behind Chart 1 and the one behind Chart 2) → **OK**.
4. **Link both charts to the same Timeline:**
   - Click the Timeline (from Task 3) → **Timeline tab → Report Connections** → tick both PivotTables → **OK**.
5. Arrange both charts on one sheet next to the Venue slicer and Timeline — this is your dashboard. Now clicking a venue in the slicer, or dragging the timeline range, **updates both charts simultaneously**, exactly like an executive dashboard filtering region + date across multiple visuals at once.

---

## Task 5 — Wins per Team per Year, Highlighting the Top Performer Each Year

**Steps:**
1. Insert → PivotChart → new PivotTable.
2. **Season** → Axis (Rows), **Team** → Legend (Columns), **Match ID** → Values (Count), then filter **Result = Won** (drag Result to Filters, select only "Won").
3. Chart type: **Clustered Column**, with Season on the X-axis and one colored bar-cluster per team.
4. **Highlight the top team per year** — two ways:
   - **Chart-formatting approach:** click into the underlying PivotTable, then for each Season row use **Conditional Formatting → Top 1 value** on the wins numbers → pick a bold fill color (e.g., gold). This highlight carries visually into the chart's data labels/table if you show the PivotTable alongside the chart.
   - **Value Filter approach (per the hint):** on the **Team** field, apply **Value Filters → Top 10 → Top 1 → by Sum/Count of Match ID**, evaluated *within each Season* — this trims each year's cluster down to just the winning team's bar, or use it on a second, simplified chart that shows only "Season → Top Team" at a glance.
5. Optionally add **Data Labels** (Chart Design → Add Chart Element → Data Labels) so the winning team's bar shows its win-count directly on the chart, and manually set that one series' fill color to a standout color (e.g., IPL trophy gold) while leaving the rest gray — this is the most reliable way to visually distinguish "the top performer" since native PivotChart conditional formatting on individual bars is limited.

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | PivotChart, Count of matches by Team | Insert → PivotChart |
| 2 | Slicer on Venue | PivotChart Analyze → Insert Slicer |
| 3 | Timeline on Match Date | PivotChart Analyze → Insert Timeline |
| 4 | Report Connections (linking one slicer/timeline to 2 charts) | Slicer/Timeline tab → Report Connections |
| 5 | Value Filters (Top 1) + manual highlight color | PivotTable Fields → Value Filters; Format Data Series |
