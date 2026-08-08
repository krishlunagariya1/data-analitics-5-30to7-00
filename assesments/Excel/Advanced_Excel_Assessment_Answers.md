# Advanced Excel for Analytics — Worked Notes
**Assessment theme:** Business Problem Framing & KPI Identification
**Reference dataset:** `RawData` tab in `Excel_KPI_Reference_Workbook.xlsx` (5,314-row OnlineRetail-style transaction table, Oct–Dec 2025) + `Revenue Forecast` tab (24 months of synthetic history for the forecasting task)
**UI assumed below:** Excel Desktop 365/2021 for Windows. Mac/Excel Online differences are flagged inline.

---

## Sample dataset

| Column | Type | Notes |
|---|---|---|
| InvoiceNo | Text | ~2% start with `C` = cancelled/returned order (negative Quantity) |
| StockCode | Text | 40 products |
| Description | Text | ~2% blank on purpose (for the profiling task) |
| Quantity | Integer | negative for cancellations |
| InvoiceDate | Date/time | Oct 1 – Dec 24, 2025, weighted toward business-hour + evening peaks |
| UnitPrice | Currency | fixed per product |
| CustomerID | Integer | ~8.5% blank on purpose |
| Country | Text | UK-majority, 10 other countries |

Helper columns already added in the table (`LineRevenue`, `Hour`, `IsFirstLineOfInvoice`) so you can build PivotTables straight from it.

---

## Section A — Concept Application (short answers)

1. **Before opening the dataset:** frame the business question first — write down exactly what "flat revenue despite increased traffic" means numerically (e.g., conversion rate = orders/visits) so you know which columns/joins you actually need, instead of exploring blindly.
2. **KPI vs. metric:** a KPI is tied to a specific business objective, has a target/benchmark, is tracked over a defined time period, and someone is accountable for moving it. A metric is just any measured number — not every metric is a KPI.
3. **AOV** = Descriptive KPI (answers "what is happening?" — average £ per order). **Customer Repeat Rate** = Diagnostic KPI (answers "why is it happening?" — is revenue driven by new or returning customers?).
4. **Excel** is justified for ad-hoc, formula-transparent, single-user analysis you need to hand-audit (e.g., this KPI workbook). **Power BI** is justified when the model needs to refresh automatically from a live source and be shared as an interactive dashboard across a team.
5. **"Number of Customers" is Descriptive, not Diagnostic** — it tells you *how many* but not *why* revenue moved. A Diagnostic KPI has to explain a driver (e.g., repeat rate, AOV shift, churn by segment); customer count alone doesn't isolate a cause.
6. **Raw columns aren't KPIs** because they're unaggregated and have no business meaning on their own (UnitPrice is just a price, not a performance signal). To turn it into a KPI you must aggregate (sum/average), attach a time dimension, and relate it to a business objective — e.g., UnitPrice → AOV → tracked monthly against a target.

---

## Section B — Practical Tasks

### B1. Power Query data profiling (missing CustomerID / Description)

**Concept:** Power Query's Column Quality and Column Distribution views quantify data completeness before you trust any KPI built on that column.

**Steps (Windows):**
1. Select any cell in your data → **Data → From Table/Range** (or `Data → Get Data → From File → From Workbook` if importing fresh).
2. In the Power Query Editor: **View → Column quality** and **View → Column distribution**.
3. Click each header's quality bar for a % Valid / % Error / % Empty breakdown.
4. Right-click `CustomerID` → **Transform → Column Profile** for the exact missing count, or add a step: select the column → **Home → Remove Rows → Remove Blank Rows** on a duplicated query if you want to quantify impact by comparing row counts before/after.
5. Close & Load, or keep exploring — don't apply the blank-row removal to your real query unless you intend to drop those rows.

**Reference numbers** (already computed with formulas on the `Data Profiling` tab so you can check your Power Query result against them): **CustomerID: 449/5,314 missing (8.4%)**, **Description: 95/5,314 missing (1.8%)**.

**Version note:** Column Quality/Distribution bars require Excel 2016+ with Power Query (built in from 2016 onward); Excel Online's Power Query support is limited — do this step in desktop Excel.

---

### B2. Multi-layered PivotTable — AOV & Revenue per Minute by hour

**Concept:** A PivotTable with a numeric field bucketed by hour lets you spot peak-traffic-but-low-conversion windows — the actual business question in the brief.

**Steps (Windows):**
1. Click inside the `OnlineRetail` table on `RawData` → **Insert → PivotTable → New Worksheet**.
2. Drag **InvoiceDate** to **Rows** — right-click the resulting date group → **Group** → tick only **Hours** (untick Months/Years) to bucket by hour of day.
3. Drag **LineRevenue** to **Values** → set to **Sum**, rename "Sum of LineRevenue" to "Revenue".
4. Drag **InvoiceNo** to **Values** a second time → **Value Field Settings → Summarize by → Distinct Count** (Excel 2013+; on older versions use `IsFirstLineOfInvoice` summed instead, exactly as the reference tab does).
5. Add a **calculated field**: **PivotTable Analyze → Fields, Items & Sets → Calculated Field** → Name `AOV`, Formula `=LineRevenue/InvoiceNo` (or `/IsFirstLineOfInvoice`).
6. Add a second calculated field `RevenuePerMinute` = `LineRevenue/60`.
7. **Insert → PivotChart** (clustered column) from the same PivotTable to visualize revenue-per-minute by hour.

**Reference numbers:** see the `AOV and Revenue per Hour` tab — hours 12–14 and 17–19 show the highest revenue/minute; overall AOV ≈ **£274**.

**Version note:** Distinct Count as a summary option needs Excel 2013+ *and* the table to be added to the Data Model (tick "Add this data to the Data Model" when inserting the PivotTable). If you're on an older build, use the `IsFirstLineOfInvoice` helper-column trick instead — it works everywhere.

---

### B3. Dynamic Pareto Chart (80/20)

**Concept:** Ranks products by revenue and overlays cumulative % so you can see visually which ~20% of SKUs drive ~80% of revenue — and which long-tail items may be diluting margin (through discounting, returns, or holding cost) without contributing much revenue.

**Steps (Windows):**
1. Build a PivotTable: Rows = `StockCode`/`Description`, Values = Sum of `LineRevenue`.
2. Right-click any value → **Sort → Sort Largest to Smallest**.
3. Add a helper column next to the Pivot output (or in a normal range) for cumulative % : `=SUM($B$2:B2)/SUM($B$2:$B$41)` filled down, formatted as %.
4. Select the revenue column + cumulative % column → **Insert → Chart → Histogram → Pareto** (Excel 2016+ has a one-click **Pareto** chart type under Histogram) *or* build it manually as a combo chart: **Insert → Combo Chart → Clustered Column – Line on Secondary Axis**, with cumulative % as the line series on the secondary axis, scaled 0–100%.
5. Add a horizontal reference line at 80% on the secondary axis (a constant helper column plotted as a line) to mark the cutoff visually.

**Reference:** the `Pareto - Top Products` tab already has this built as a real Excel combo chart (bars = revenue, line = cumulative %) with a conditional-format flag marking which products fall in the top 20% by count. In this sample, ~8 of 40 products (20%) already account for over half of total revenue — you'll see the curve bend sharply after the first 5–6 SKUs (cakestands, buntings, memoboard).

**Version note:** the built-in **Histogram → Pareto** chart type requires Excel 2016+; earlier versions must use the manual combo-chart method in step 4, which works in every version including Excel Online.

---

### B4. Time-series forecast — next quarter revenue (Analysis ToolPak)

**Concept:** Fits a trend/regression line to historical monthly revenue (capturing seasonality) and projects it forward, then flags months where actuals deviated significantly from the fitted trend — a proxy for unexplained shocks (promotions, stockouts, seasonality misses).

**Steps (Windows):**
1. Enable the add-in once: **File → Options → Add-ins → Manage: Excel Add-ins → Go… → tick Analysis ToolPak → OK.**
2. With monthly revenue history laid out as two columns (Month index, Revenue): **Data → Data Analysis → Regression** (for a trend line + R², significance stats) or **Data → Data Analysis → Exponential Smoothing** (for a smoothed series that adapts to recent seasonality, damping factor ≈ 0.2–0.3 is a reasonable start).
3. For Regression: Input Y Range = Revenue, Input X Range = Month index, tick **Line Fit Plot** and **Residuals** — residuals more than ~2 standard deviations from 0 are your "significant variances."
4. To project forward, extend the X range to include 3 future month indices before running Regression, or simply drag-fill the trendline's equation (`y = mx + b`, read `m` and `b` off the Regression output) for months 25–27.

**Reference tab (`Revenue Forecast`)** does the equivalent with the `TREND()` worksheet function (same least-squares logic as ToolPak's Regression, but live and recalculating) — it flags any month where actual vs. trend variance exceeds ±10% in red, and projects three months forward. In this sample: **Jan–Mar next-quarter forecast ≈ £68.9k / £70.3k / £71.5k**, with Nov–Dec showing the largest positive variances (holiday seasonality the straight-line trend under-predicts — worth calling out explicitly in your write-up as a limitation of a purely linear model).

**Version note:** Analysis ToolPak ships with Excel Desktop (Windows and Mac) but is **not available in Excel Online**; on Mac, the menu path is **Data → Analysis Tools**, and the Exponential Smoothing tool's UI is slightly different (fewer options) than Windows. `TREND()`/`FORECAST.LINEAR()` work everywhere, including Online, and are the honest fallback if you don't have ToolPak enabled.

---

## Section C — Mini Project scaffold

- **Cleaned Data Model:** load `RawData` into Power Query, apply the profiling/cleanup from B1 (don't blindly drop blank-CustomerID rows — flag them as "Guest" instead so you don't lose revenue history).
- **Descriptive KPI Dashboard:** AOV, Revenue/Minute by hour, and the Pareto chart from B2/B3 are your descriptive core.
- **Monthly Cohort Analysis:** group by `CustomerID` (excluding blanks) × month of first purchase, then track repeat purchase rate per cohort per subsequent month.
- **Diagnostic Report on Churn Drivers:** cross the cohort table against `Country` and AOV to see whether churn concentrates in specific geographies or low-AOV segments — that's the Diagnostic layer the brief is asking for.

---

## What's built vs. what you build yourself

| Built for you in the workbook | You build in Excel UI (steps above) |
|---|---|
| Sample dataset + helper columns | Actual Power Query profiling steps |
| Formula-driven KPI summaries (stand-ins for PivotTables) | Real interactive PivotTable/PivotChart |
| Pareto combo chart | Slicers/Timeline on your PivotTable |
| `TREND()` forecast | Analysis ToolPak Regression/Smoothing dialog |

Interactive PivotTables, Power Query queries, and ToolPak dialogs are Excel-UI-driven objects that can't be reliably generated by a script and reopened cleanly across Excel versions — so the workbook gives you formula-equivalent numbers to check your own PivotTable/ToolPak output against, rather than fake pivot objects that might not survive being opened.
