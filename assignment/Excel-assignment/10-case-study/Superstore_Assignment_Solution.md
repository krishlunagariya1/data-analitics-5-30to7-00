# Case Study 10: Retail Store Sales Dashboard & Analysis — Solution

**File delivered:** `Superstore_Dashboard.xlsx`
**Dataset note:** No file was uploaded to this chat, and the real Kaggle `SampleSuperstore.csv` couldn't be downloaded (no internet access here), so the workbook uses a realistic sample dataset built with the exact same columns and typical Superstore patterns (Furniture running thin/negative margins under heavy discounting, Technology carrying the best margins, etc.). **Upload your real `SampleSuperstore.csv` and I'll re-run every step against your actual data.** Everything below is written so it applies to your file unchanged — only the numbers will shift.

---

## Task 1 — Clean the data (Filter + Remove Duplicates)

**Sheet:** `RawData_Cleaned`

Steps performed (and what to do yourself in Excel):
1. Select the full data range → **Data tab → Filter** (also applied automatically here as an Excel Table, which includes filter dropdowns on every column).
2. **Data tab → Remove Duplicates** → check *all* columns → OK.

**Important nuance:** the task says "so each Order ID appears only once," but in the real Superstore dataset one `Order ID` legitimately contains several rows — one per product purchased in that order. Deleting rows just to force one row per Order ID would delete real sales lines and understate totals. The correct cleaning action is to remove **exact duplicate rows** (every column identical), which is what "Remove Duplicates" does when all columns are selected. In this sample: **390 rows → 375 rows (15 exact duplicates removed)**. A note documenting this is written directly under the table in the sheet.

---

## Task 2 — Pivot Table: Sales & Profit by Region

**Sheet:** `Region_Summary`

Built as a live summary table using `SUMIFS`/`COUNTIFS` against `RawData_Cleaned` (recalculates automatically if you edit the raw data) — functionally identical to a PivotTable's output. If your instructor wants a **native** Excel PivotTable object too: select the table on `RawData_Cleaned` → **Insert → PivotTable** → Rows: `Region`, Values: `Sum of Sales`, `Sum of Profit`.

Result in the sample data:

| Region | Total Sales | Total Profit | Orders | Margin |
|---|---|---|---|---|
| Central | $84,888.59 | $2,782.65 | 98 | 3.3% |
| East | $129,349.90 | $6,944.33 | 93 | 5.4% |
| South | $72,473.36 | –$604.81 | 110 | –0.8% |
| **West** | **$101,193.07** | **$7,023.98** | 74 | **6.9%** |

The row with the highest profit (**West**) is highlighted green via conditional formatting, and the region name is also pulled out automatically with an `INDEX/MATCH` formula beneath the table.

---

## Task 3 — Conditional Formatting: Discount > 20% AND Profit < 0

**Sheet:** `RawData_Cleaned`

A formula-based conditional formatting rule is applied across the whole data range:

```
=AND($<Discount column>2>0.2, $<Profit column>2<0)
```

Matching rows are filled red with dark-red text — these are the high-discount, loss-making orders worth investigating (over-discounting on low-margin categories like Tables and Bookcases is the usual driver).

To reproduce manually: select the data range → **Home → Conditional Formatting → New Rule → Use a formula** → enter the formula above → set a red fill.

---

## Task 4 — Dashboard

**Sheet:** `Dashboard` (first tab)

Contains:
- **KPI cards:** Total Sales, Total Profit, Total Orders (unique Order IDs), Overall Profit Margin — all live `SUM`/`SUMPRODUCT` formulas, no hardcoded numbers.
- **Bar chart — Sales by Category** (built as a Pivot Chart-equivalent, sourced from the `Category_SubCategory` summary sheet).
- **Bar chart — Profit by Region**, placed alongside for extra context on the profitable-regions question from Task 2.

Sample totals: **Total Sales $387,904.92 · Total Profit $16,146.15 · 260 Orders · 4.2% overall margin.**

---

## Task 5 — Top 5 Most Profitable Sub-Categories

**Sheet:** `Top5_Profitable_SubCategories`

Ranked with `LARGE` + `INDEX/MATCH` against the sub-category profit table (equivalent to using Quick Analysis → Charts → sorted Top N), with a clustered column chart alongside.

| Rank | Sub-Category | Total Profit |
|---|---|---|
| 1 | Copiers | $18,908.82 |
| 2 | Phones | $4,286.27 |
| 3 | Furnishings | $1,733.88 |
| 4 | Appliances | $1,700.84 |
| 5 | Storage | $909.02 |

**Findings (also recorded as a cell comment on the sheet):** Technology sub-categories dominate profitability — Copiers alone contribute more profit than the next three sub-categories combined, reflecting strong margins and low average discounting. Furniture sub-categories such as Tables and Bookcases don't make the top 5; across the dataset they're frequently discounted above 20%, which is exactly the pattern flagged in Task 3 and erodes or reverses their profit. **Recommendation:** cap discounts on low-margin Furniture items and prioritize inventory/marketing spend toward Technology sub-categories.

---

## Workbook structure

| Sheet | Purpose |
|---|---|
| `Dashboard` | KPIs + charts (Task 4) |
| `RawData_Cleaned` | Cleaned, filterable, conditionally formatted data (Tasks 1 & 3) |
| `Region_Summary` | Pivot-style Region analysis (Task 2) |
| `Category_SubCategory` | Helper summary feeding the dashboard & Top-5 sheet |
| `Top5_Profitable_SubCategories` | Ranked Top 5 + chart + findings (Task 5) |

All figures are formulas (`SUMIFS`, `COUNTIFS`, `LARGE`, `INDEX/MATCH`), so changing any value in `RawData_Cleaned` automatically ripples through every sheet and chart.
