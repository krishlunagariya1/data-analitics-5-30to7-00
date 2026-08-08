# Session 21 – Case Study Integration + Mini Dashboard Project
## Solved Assignment

**File used:** `capstone_dashboard.xlsx` (attached alongside this document) — a fully working, pre-built workbook covering **all 5 tasks end-to-end**, so you can open it and see the finished pipeline: messy raw data → cleaned data → lookups → summary → dashboard.

**Workbook structure:**

| Sheet | Contents |
|---|---|
| `Dashboard` | The finished mini dashboard: KPI cards, Top 3 Restaurants table, note on adding the live Slicer |
| `RawOrders` | 96 rows of **messy** source data — duplicates, 4 different date text formats mixed together, and blank Delivery Partner cells |
| `Orders_Cleaned` | The cleaned 90-row result: duplicates removed, dates normalized to real dates, blanks filled with "Unassigned," plus VLOOKUP'd Restaurant Name/City and a Day of Week column |
| `RestaurantDetails` | Lookup table — Restaurant ID, Restaurant Name, City, and a helper Order Count column |
| `CitySummary` | City-level totals (Total Orders, Total Delivery Charges) with a bar chart — the manual equivalent of a PivotTable/PivotChart, since those two live inside Excel and can't be scripted into a file |

---

## Task 1 — Clean the Raw Dataset

`RawOrders` intentionally contains three real-world problems:
- **6 duplicate rows** (same Order ID, Restaurant ID, date text, everything — a re-submitted record)
- **Delivery Date stored as mixed text formats** — some rows `05/06/2024`, others `2024-06-05`, others `5-Jun-2024`, others `05.06.2024` — the classic "data from four different exports pasted together" problem
- **Blank Delivery Partner** on some rows (order not yet assigned to a rider)

**Steps to reproduce this cleaning in Excel:**
1. **Remove duplicates:** select the whole table → **Data tab → Remove Duplicates** → tick all columns → OK. (96 rows → 90 rows, 6 removed.)
2. **Fix inconsistent dates:** since Excel stores these as text (not real dates) when formats are mixed, the reliable fix is:
   - Select the Delivery Date column → **Data tab → Text to Columns → Delimited → Finish** (this alone forces Excel to re-interpret each text string using your regional date settings for straightforward formats), **or**
   - For a column with genuinely mixed formats like this one, use **Power Query** (Data → Get Data → From Table/Range → in the Query Editor, set the column type to Date — Power Query is much better than native Excel at parsing multiple date text formats in one pass) → Close & Load back.
   - Confirm success by checking the column is now **right-aligned** (Excel right-aligns real dates, left-aligns text) and a formula like `=YEAR(C2)` returns a number instead of `#VALUE!`.
3. **Fill missing Delivery Partner values:** select the Delivery Partner column → **Home → Find & Select → Go To Special → Blanks** → OK (this selects every empty cell in the column at once) → type `Unassigned` → press **Ctrl+Enter** (fills the same value into every selected cell simultaneously, not just the active one).

Result lands on the `Orders_Cleaned` sheet: 90 rows, real dates, no blank partners.

---

## Task 2 — VLOOKUP/XLOOKUP: Add Restaurant Name from a Separate Table

The `RestaurantDetails` sheet holds Restaurant ID → Restaurant Name → City (per the hint, on its own sheet).

**Formula used (Restaurant Name column, `Orders_Cleaned!G2`):**
```
=VLOOKUP(B2, RestaurantDetails!$A$2:$C$11, 2, FALSE)
```
**Formula used (City column, `Orders_Cleaned!H2`):**
```
=VLOOKUP(B2, RestaurantDetails!$A$2:$C$11, 3, FALSE)
```
- `B2` = this row's Restaurant ID
- `RestaurantDetails!$A$2:$C$11` = the lookup table, **locked with `$`** so it doesn't shift when you copy the formula down
- `2` / `3` = which column to return (Name / City) counting from the left of the lookup range
- `FALSE` = exact match only — critical, since Restaurant IDs won't have an approximate match

**If your Excel version has XLOOKUP**, the equivalent (and more readable) version is:
```
=XLOOKUP(B2, RestaurantDetails!$A$2:$A$11, RestaurantDetails!$B$2:$B$11)
```
XLOOKUP doesn't need a column-index number and defaults to exact match, so it's less error-prone — but VLOOKUP was used in the attached file for broader compatibility.

---

## Task 3 — Extract Day of the Week from Delivery Date

**Formula used (`Orders_Cleaned!I2`):**
```
=TEXT(C2, "dddd")
```
This returns the full weekday name (e.g., "Friday") directly as text. Two alternatives:
- `=TEXT(C2,"ddd")` → abbreviated form ("Fri")
- `=WEEKDAY(C2,2)` → returns a **number** 1–7 (Monday=1...Sunday=7) instead of text — more useful if you later want to sort or group by weekday numerically (e.g., inside a PivotTable's row grouping) rather than display it.

Both only work correctly **after** Task 1's date-cleaning step — if Delivery Date is still text, both formulas return `#VALUE!`, which is a good built-in check that your cleaning actually worked.

---

## Task 4 — City Summary: Total Orders & Delivery Charges (PivotTable + PivotChart)

The `CitySummary` sheet in the attached file shows the target result using formulas (`COUNTIF`/`SUMIF`) plus a bar chart, since a live PivotTable/PivotChart has to be built inside Excel itself. **To build the actual PivotTable/PivotChart as the task asks:**

1. Click inside `Orders_Cleaned` → **Insert tab → PivotChart** (this creates the PivotTable and chart together).
2. In the field list: drag **City** → **Rows/Axis**; drag **Order ID** → **Values** → set to **Count** (this gives Total Orders); drag **Delivery Charges (₹)** → **Values** again → defaults to **Sum** (this gives Total Delivery Charges).
3. You'll now have two value fields side by side per city. Set the chart type to **Clustered Column** (Design tab → Change Chart Type) so both metrics show as paired bars per city.
4. Rename the PivotTable field headers ("Count of Order ID" → "Total Orders", "Sum of Delivery Charges" → "Total Delivery Charges") via **Value Field Settings → Custom Name**.

**Result (matches the formula-based `CitySummary` sheet in the file):**

| City | Total Orders | Total Delivery Charges (₹) |
|---|---|---|
| Mumbai | 24 | ₹1,254.95 |
| Bangalore | 18 | ₹964.96 |
| Pune | 18 | ₹834.28 |
| Delhi | 16 | ₹784.84 |
| Ahmedabad | 14 | ₹598.06 |

*(Numbers will match exactly what your own PivotTable shows if built from the same `Orders_Cleaned` sheet — Mumbai leads on both order volume and total charges.)*

---

## Task 5 — Mini Dashboard: KPIs, Top 3 Restaurants, City Slicer

The `Dashboard` sheet in the attached file already contains:

| Element | How it's built |
|---|---|
| **Total Orders** KPI card | `=COUNTA(Orders_Cleaned!A2:A91)` |
| **Average Delivery Time** KPI card | `=AVERAGE(Orders_Cleaned!F2:F91)` |
| **Total Delivery Charges** KPI card | `=SUM(Orders_Cleaned!E2:E91)` |
| **Top 3 Restaurants by order count** | `RestaurantDetails` sheet gets a helper `Order Count` column: `=COUNTIF(Orders_Cleaned!$B$2:$B$91,A2)`; the Dashboard then pulls the top 3 via `=LARGE(...)` for the count and `=INDEX(...,MATCH(LARGE(...),...))` for the matching restaurant name |

**To add the live Slicer (must be done in Excel — this is the one piece that can't be pre-built in a script):**
1. First build a PivotTable somewhere on the Dashboard (or a hidden helper sheet) summarizing whatever the Top 3 / KPI figures should react to — e.g., a PivotTable with **City** in Filters and **Order ID** (Count) / **Delivery Charges** (Sum) in Values.
2. Click that PivotTable → **PivotTable Analyze tab → Filter → Insert Slicer** → tick **City** → OK.
3. To make the slicer control **multiple** PivotTables/PivotCharts at once (so filtering by city updates every visual on the dashboard together): click the Slicer → **Slicer tab → Report Connections** → tick every PivotTable on the dashboard that should respond to it → OK.
4. If your KPI cards (Total Orders, Avg Delivery Time) are plain formulas rather than PivotTable values, they **won't** respond to a slicer directly — to make everything filter together, convert those formulas to `GETPIVOTDATA()` references pointing at a filtered PivotTable, or rebuild them as PivotTable values instead of raw `COUNTA`/`AVERAGE` formulas over the full range.

**Result:** clicking a city (e.g., "Mumbai") in the slicer filters every connected visual — the PivotChart from Task 4, and any PivotTable-driven KPI — down to Mumbai-only figures simultaneously, which is the interactive "single filter, whole dashboard reacts" behavior the task is asking for.

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | Remove Duplicates, Text to Columns/Power Query for dates, Go To Special → Blanks | Data tab; Home → Find & Select |
| 2 | VLOOKUP / XLOOKUP against a separate lookup sheet | Formula bar |
| 3 | TEXT() or WEEKDAY() on the cleaned date column | Formula bar |
| 4 | PivotTable + PivotChart, City in Rows, Count + Sum in Values | Insert → PivotChart |
| 5 | KPI formulas, INDEX/MATCH/LARGE for Top 3, Slicer + Report Connections | Insert → Slicer; PivotTable/Slicer tabs |
