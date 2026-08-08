# Session 19 – Excel Dashboard Design
## Solved Assignment

**File used:** `food_delivery_dashboard.xlsx` (attached alongside this document) — a working, pre-built dashboard covering **all 5 tasks**, so you can open it directly and see the finished result, then use the steps below to reproduce or extend it.

**Workbook structure:**

| Sheet | Contents |
|---|---|
| `Dashboard` | The finished wireframe: Header → KPI Cards → Trends (Donut + Waterfall charts) → Insights |
| `OrdersData` | Raw source data — 113 orders across Jan–Jun, columns: Order ID, Cuisine, Order Amount (₹), Month |
| `Summary` | Helper calculations feeding the charts: cuisine totals (for the Donut) and monthly totals + waterfall helper columns (Base / Increase / Decrease) |

Color palette used: **Spotify-inspired** — near-black background (`#191414`), Spotify green (`#1DB954`) and light green (`#1ED760`) for accents/positive values, white text for readability, gray for secondary labels, and red (`#E63946`) reserved only for the waterfall's decrease bars.

---

## Task 1 — Dashboard Wireframe: Header → KPIs → Trends → Insights

**Steps:**
1. Pick one sheet to be the dashboard canvas (`Dashboard` here) and fill its whole visible area with a **solid dark fill** (Home → Fill Color) — this is what makes it read as an "app dashboard" instead of a plain spreadsheet.
2. **Header band** (rows 1–3): merge a wide range (e.g., `A1:P2`) → type the report title in large bold white text; merge a second thin row below for a subtitle in smaller gray italic text.
3. **Section labels**: before each section (KPIs, Trends, Insights), merge a full-width row and type the section name in bold accent-color text (green here) — this visually divides the wireframe into its four zones exactly like the brief asks.
4. **KPI zone**: reserve a fixed row band (rows 6–9 in this file) split into equal-width card blocks — covered fully in Task 2.
5. **Trends zone**: reserve a large row band below the KPIs for the charts (Task 3 & 4).
6. **Insights zone**: reserve a few rows at the bottom for plain-text bullet takeaways (Task 5 area, populated at the end).
7. Use **View tab → Gridlines (untick)** on the Dashboard sheet so it doesn't look like a spreadsheet — this single toggle does more for "dashboard feel" than almost anything else.

---

## Task 2 — KPI Cards: Min, Max, Average Order Value

Built directly in the `Dashboard` sheet, columns A–P, rows 6–9, as **4 equal-width cards**:

| Card | Formula | Format |
|---|---|---|
| Min Order Value | `=MIN(OrdersData!C2:C113)` | White text, ₹ currency |
| Max Order Value | `=MAX(OrdersData!C2:C113)` | Green text, ₹ currency |
| Average Order Value | `=AVERAGE(OrdersData!C2:C113)` | Light-green text, ₹ currency |
| Total Orders | `=COUNTA(OrdersData!A2:A113)` | White text, whole number |

**Steps to build one card:**
1. Merge a block of cells (e.g., `A6:D7`) for the **label** row — type "MIN ORDER VALUE," bold, gray, centered.
2. Merge the block below it (`A8:D9`) for the **value** — enter the formula, set font size ~20pt bold, colored per the accent above, number format `"₹"#,##0.00`.
3. Fill both merged blocks with a slightly lighter "card" gray (`#282828`) so each KPI reads as a distinct card floating on the dark dashboard background — not just numbers sitting on the same flat background as everything else.
4. Repeat for all 4 KPIs, spacing them into equal-width columns (here: A–D, E–H, I–L, M–P) so they land perfectly evenly across the row — this also sets up Task 5's alignment requirement.

---

## Task 3 — Donut Chart: Cuisine Type Proportions

**Steps:**
1. On the `Summary` sheet, build a small helper table: **Cuisine** | **Total Orders (Count)**, with `=COUNTIF(OrdersData!B:B, "Indian")` (etc.) for each cuisine — this is what the chart actually reads from, rather than pointing a chart straight at 113 raw rows.
2. Select that helper table → **Insert tab → Insert Pie or Doughnut Chart → Doughnut**.
3. **Chart Design tab → Add Chart Element → Data Labels → More Options → tick "Percentage,"** untick "Value" — this shows each slice's share (%) rather than a raw count, which reads better on a dashboard.
4. **Format Data Series → Doughnut Hole Size**: increase to ~65–70% for a slimmer modern ring (the default is a thick, dated-looking donut).
5. Recolor each slice manually (right-click a slice → Format Data Point → Fill) to sit within your chosen palette — e.g., shades of green from dark to light for the top cuisines, with gray for the smallest slice, keeping the whole chart inside the same color family as the KPI cards instead of Excel's default rainbow.
6. Remove the chart border and set its background to "No Fill" so it blends into the dark dashboard instead of sitting in a white box.

---

## Task 4 — Waterfall Chart: Month-on-Month Change in Total Orders

Excel does have a native **Waterfall** chart type (Insert → Insert Waterfall or Stock Chart → Waterfall) — the steps below cover both: the native way, and the classic manual method actually used in the attached file (useful because the native Waterfall chart type isn't available in every Excel version/edition, and the manual version gives you more control over color rules).

**Native method (if available in your Excel):**
1. Build a simple table: **Month** | **Total Orders** (one row per month).
2. Select it → **Insert tab → Insert Waterfall, Funnel, Stock, Surface, or Radar Chart → Waterfall**.
3. Right-click any bar you want treated as a **subtotal** (e.g., the final month) → **Set as Total** — Excel then auto-colors increases/decreases/totals in three distinct default colors, which you can restyle via Format Data Point.

**Manual method (used in the attached file, works in every Excel version):**
1. Build 4 helper columns per month on the `Summary` sheet:
   - **Change** = this month's total − previous month's total
   - **Base (invisible)** = `IF(Change>=0, previous month's total, this month's total)` — this is the "floating" part of each bar that stays invisible
   - **Increase** = `IF(Change>=0, Change, 0)`
   - **Decrease** = `IF(Change<0, -Change, 0)`
2. Select **Month, Base, Increase, Decrease** → **Insert → Stacked Column Chart**.
3. Click the **Base** series → **Format Data Series → Fill → No Fill** and **Border → No Line** — this makes the base segment invisible, so each remaining bar appears to "float" at the right height, exactly mimicking a true waterfall.
4. Color the **Increase** series green and the **Decrease** series red (Format Data Series → Fill → Solid Fill) so growth and decline are visually obvious at a glance, per the task's color-coding requirement.

**Result:** a chart where each month's bar visually starts where the previous month left off — rising (green) in growth months, falling (red) in decline months — the defining look of a waterfall chart.

---

## Task 5 — Alignment, Spacing & Consistent Color Palette

**Steps applied across the whole dashboard:**
1. **Equal-width KPI cards:** all 4 KPI cards span exactly 4 columns each (A–D, E–H, I–L, M–P) with identical row heights (rows 6–9) — select all 4 blocks together and use **Home → Align → Distribute Horizontally** to guarantee even gaps if you nudge any card manually.
2. **Chart alignment:** with both charts selected (Ctrl+click each chart border), use **Shape Format tab → Align → Align Top** so the Donut and Waterfall charts start at exactly the same row, and **Align → Distribute Horizontally** so their side gap matches the KPI card gaps above them.
3. **Consistent palette:** every element on the dashboard pulls from one 5-color set only — dark background, two greens (primary accent + highlight), white (primary text), gray (secondary text/labels), plus a single red reserved *only* for "decrease" data — never use red decoratively elsewhere, so its meaning as "negative" stays unambiguous. This is the core of color theory for dashboards: a small, purposeful palette where color always communicates something, rather than a wide palette chosen for variety.
4. **Whitespace:** leave at least 1 blank row between sections (Header/KPIs/Trends/Insights) and don't let charts or cards touch the sheet edges — the merged section-label rows in Task 1 naturally create this breathing room.
5. **Typography hierarchy:** one font family throughout (Arial) with only 3 sizes used deliberately — large bold for the title, medium bold for KPI values and chart titles, small for labels/insights — rather than a random mix of sizes, which is what makes a wireframe look "designed" rather than "typed."

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | Wireframe via merged cells + fill color + section rows | Home → Fill Color; View → Gridlines |
| 2 | KPI cards via MIN/MAX/AVERAGE formulas + card fills | Formula bar; Home → Fill Color, Font |
| 3 | Doughnut Chart on COUNTIF helper table | Insert → Pie or Doughnut Chart |
| 4 | Waterfall (native or Base/Increase/Decrease stacked-bar trick) | Insert → Waterfall, or Insert → Stacked Column |
| 5 | Align & Distribute, single consistent palette | Shape Format → Align → Align/Distribute |
