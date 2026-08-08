# Advanced Excel For Analytics — Assessment Answers

**Theme:** Business Problem Framing & KPI Identification
**Dataset:** [Kaggle – Online Retail Dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data)
**Total Time:** 3 Hours

---

## Section A: Concept Application

### 1. What is the first step an analyst should take before opening a dataset to investigate flat revenue despite increased traffic?

Before opening the dataset, the analyst should **frame the business problem** — not touch the data yet. This means:

- Restating the problem as a clear, answerable question: *"Why has revenue stayed flat while traffic has grown?"*
- Forming a set of **hypotheses** to test (e.g., lower conversion rate, falling AOV, higher return/cancellation rate, discount-heavy traffic, seasonality mismatch, poor product mix).
- Identifying **what metrics/KPIs** would prove or disprove each hypothesis (Conversion Rate, AOV, Repeat Rate, Revenue per Visitor, etc.).
- Deciding the **time grain and scope** needed (daily/hourly, by region, by product) to test those hypotheses.

Only after this framing should the analyst open the dataset — otherwise they risk "data diving" (looking for patterns with no direction), which wastes time and can lead to spurious conclusions.

---

### 2. What specific characteristics distinguish a "Key Performance Indicator" (KPI) from a standard business metric?

| Characteristic | Standard Metric | KPI |
|---|---|---|
| **Definition** | Any measurable number (raw or calculated) | A metric tied directly to a strategic business objective |
| **Actionability** | May or may not lead to a decision | Must be actionable — tells you what to *do* |
| **Target/Benchmark** | Usually none | Has a target, threshold, or benchmark to compare against |
| **Ownership** | Not necessarily owned by anyone | Usually owned by a team/role accountable for it |
| **Trend relevance** | May be static or one-off | Tracked over time to show performance direction |

In short: **all KPIs are metrics, but not all metrics are KPIs.** A metric becomes a KPI only when it is (a) aligned to a specific goal, (b) measurable consistently over time, and (c) actionable — i.e., a change in it should trigger a business decision.

*Example:* "Total number of website clicks" is a metric. "Conversion Rate (%)" is a KPI, because it's tied to the revenue objective, has an implicit target, and directly informs action (e.g., improve checkout flow).

---

### 3. Classify Average Order Value (AOV) and Customer Repeat Rate as either Descriptive or Diagnostic KPIs and state the questions they answer.

| KPI | Classification | Question it Answers |
|---|---|---|
| **Average Order Value (AOV)** | **Descriptive KPI** | *"What is happening?"* — On average, how much is a customer spending per order right now? |
| **Customer Repeat Rate** | **Diagnostic KPI** | *"Why is it happening?"* — Is flat/declining revenue caused by failure to retain customers, or by weaker spending per order? |

**Reasoning:**
- **AOV** summarizes a current state (a snapshot of average transaction size) — it describes *what* is happening without explaining cause. That makes it Descriptive.
- **Customer Repeat Rate** helps explain the *cause* behind a revenue trend — e.g., if repeat rate is falling while traffic rises, it diagnoses that the problem is **retention**, not acquisition. This root-cause capability makes it Diagnostic.

*(Note: in practice AOV can also be used diagnostically — e.g., comparing AOV of new vs. repeat customers — but in its plain form as "average spend per order," it is fundamentally descriptive.)*

---

### 4. Provide one justified reason to choose Excel and one reason to choose Power BI for analyzing Monthly Revenue.

**Choose Excel when:**
- You need **flexible, ad-hoc, cell-level analysis** — e.g., manually adjusting formulas, building a one-off Pareto chart, or doing what-if forecasting with the Analysis ToolPak. Excel is faster for a single analyst doing exploratory, iterative work on a dataset that fits in memory and doesn't need to be shared live with a large audience.

**Choose Power BI when:**
- You need a **live, shareable, auto-refreshing dashboard** for stakeholders — e.g., monthly revenue needs to update automatically as new data lands, be sliced interactively by region/product by non-technical viewers, and be distributed across the organization via the Power BI Service. Power BI's data model (DAX) also scales better to large/relational datasets than a single Excel workbook.

---

### 5. Is "Number of Customers" a valid Diagnostic KPI for revenue trends? Justify by comparing Descriptive vs. Diagnostic logic.

**No — "Number of Customers" is a Descriptive KPI, not a Diagnostic one.**

- **Descriptive logic** answers *"what is the current state?"* — Number of Customers simply counts how many unique buyers existed in a period. It tells you volume, nothing more.
- **Diagnostic logic** answers *"why did the trend happen?"* — it requires a **comparison, ratio, or segmentation** that isolates a cause. Diagnostic KPIs relate two variables (e.g., Repeat Rate = Repeat Customers ÷ Total Customers, or Revenue per Customer = Revenue ÷ Customers).

"Number of Customers" on its own cannot explain *why* revenue is flat. For example, customer count could be rising (more traffic converting to buyers) while revenue stays flat — the raw count would look "healthy" and mask the real problem, which might be falling AOV or high churn among the *existing* customer base.

To make it diagnostic, it would need to be **decomposed**, e.g.:
- New vs. Returning Customer split
- Revenue per Customer trend
- Customer count segmented by cohort/region

Only in these transformed, comparative forms does it start explaining causes — as a raw count, it stays Descriptive.

---

### 6. Why is treating raw data columns (like UnitPrice) as KPIs incorrect, and what transformation steps are required to create a meaningful KPI?

**Why it's incorrect:**
A raw column like `UnitPrice` is just a **data field** captured per transaction line — it has no business meaning on its own. A KPI must be:
1. **Aggregated** over a meaningful dimension (time, customer, product, region)
2. **Aligned to a business objective** (revenue, retention, efficiency)
3. **Comparable** across periods or benchmarks

`UnitPrice` alone tells you the price of one line item in one row — it says nothing about overall performance, trend, or health of the business. Using it directly as a "KPI" would be like reporting a single employee's hourly wage as "Company Productivity."

**Transformation steps required:**

| Step | Action | Example |
|---|---|---|
| 1. **Clean** | Remove/handle nulls, negative quantities (returns), duplicate rows | Filter out `Quantity < 0` or blank `CustomerID` |
| 2. **Derive** | Create a calculated field | `Revenue = UnitPrice × Quantity` |
| 3. **Aggregate** | Roll up to a business dimension (day/month/customer/product) | `SUMIFS(Revenue, Date, month)` → Monthly Revenue |
| 4. **Normalize/Ratio** (if diagnostic) | Divide by a denominator to make it comparable | `AOV = Total Revenue ÷ Number of Orders` |
| 5. **Benchmark** | Compare to target, prior period, or peer segment | MoM % change, YoY growth |

Only after these steps does a raw column like `UnitPrice` become part of a real KPI, such as **Average Order Value** or **Monthly Revenue**.

---

## Section B: Practical Task

> **Note:** These tasks require hands-on work directly inside the downloaded `OnlineRetail` dataset (Kaggle link above) in Excel/Power Query. Below is the exact step-by-step methodology, formulas, and configuration to execute each task in Excel. Since I can't access the internet or your local files in this session, follow these steps against your own downloaded copy of the dataset — the logic and formulas are ready to apply directly.

### 1. Power Query Data Profiling — Missing Values in `CustomerID` and `Description`

**Steps:**
1. `Data` → `Get Data` → `From File` → `From Text/CSV` → load `OnlineRetail.csv/xlsx` into Power Query Editor.
2. In the Power Query Editor ribbon, go to `View` → check **Column Quality**, **Column Distribution**, and **Column Profile** (also set "Column profiling based on entire dataset" at the bottom, not just top 1000 rows).
3. This instantly shows, for each column, the % **Valid**, **Error**, and **Empty**.
4. For `CustomerID` and `Description`, note the **Empty %** shown in the Column Quality bar.
5. To quantify impact numerically, add a Custom Column:
   ```
   = if [CustomerID] = null then "Missing" else "Present"
   ```
   Then `Group By` this new column to get exact counts.
6. **Quantifying KPI impact:** Any row with a missing `CustomerID` cannot be attributed to a customer — so it must be **excluded** from customer-level KPIs (Repeat Rate, CLV, Cohort Analysis) even though it may still count toward raw revenue. Typically ~25% of rows in this dataset have missing `CustomerID` — meaning roughly a quarter of transactions are invisible to any customer-based diagnostic KPI, which is a material data-quality risk to flag.
7. Missing `Description` mainly affects product-level KPIs (Pareto analysis, top-product reporting) — filter or flag these before product-level aggregation to avoid skewing the 80/20 analysis.
8. Load a **Data Quality Summary table** back into Excel: Column | Total Rows | Missing Count | Missing % | KPI(s) Impacted.

---

### 2. Multi-layered PivotTable — AOV and Revenue per Minute (Peak-Traffic, Low-Conversion Hours)

**Prep (Power Query / helper columns):**
- `Order Value = SUM of (UnitPrice × Quantity)` grouped by `InvoiceNo`
- `Hour = HOUR([InvoiceDate])`, `Minute-of-day bucket = HOUR([InvoiceDate])&":"&TEXT(MINUTE([InvoiceDate])-MOD(MINUTE([InvoiceDate]),5),"00")` (5-minute buckets recommended, since exact-minute granularity is usually too sparse)

**PivotTable Layer 1 — AOV by Hour:**
- Rows: `Hour`
- Values:
  - `Sum of Revenue`
  - `Distinct Count of InvoiceNo` (add InvoiceNo to the Data Model and use `DISTINCTCOUNT`, or use a helper column with `COUNTIF`)
  - Calculated field: `AOV = Sum of Revenue ÷ Distinct Count of InvoiceNo`

**PivotTable Layer 2 — Revenue per Minute:**
- Rows: `Hour` → `Minute Bucket` (drill-down layer)
- Values: `Sum of Revenue`, then a calculated field `Revenue per Minute = Sum of Revenue ÷ 5` (since each bucket spans 5 minutes)

**Pinpointing peak-traffic/low-conversion hours:**
- Add a third value: `Distinct Count of InvoiceNo` (traffic proxy) alongside `AOV`.
- Sort/filter hours where **transaction count is high** but **AOV or Revenue-per-Minute is comparatively low** — these are your "high traffic, low conversion value" windows.
- Visualize with a combo PivotChart: bar = Order Count, line = AOV, on the same hourly axis, to visually spot the divergence.

---

### 3. Dynamic Pareto Chart (80/20 Rule) — Top vs. Bottom Product Contribution

**Steps:**
1. Build a PivotTable: Rows = `Description` (or `StockCode`), Values = `Sum of Revenue`.
2. Sort the Pivot **descending by Revenue**.
3. Add helper columns next to the Pivot output (or in a linked table):
   - `Cumulative Revenue = running SUM() of Revenue down the sorted list`
   - `Cumulative % = Cumulative Revenue ÷ Total Revenue`
   - `Product Rank % = Row Number ÷ Total Product Count`
4. Select the Product + Revenue range → `Insert` → `Chart` → **Histogram group** → **Pareto** (Excel's built-in Pareto chart type auto-sorts descending and plots the cumulative % line — available in Excel 2016+).
5. To make it **dynamic** (auto-updates as data refreshes):
   - Convert the source range to an **Excel Table** (`Ctrl+T`) or feed it from the Power Query output.
   - Use `SORT()` and `SUM()`/`SCAN()`-style dynamic array formulas (or a helper Pivot) so cumulative % recalculates automatically.
   - Base the chart on the Table/Pivot range so it expands automatically with new data.
6. **Reading the result:** Mark the point where the cumulative % line crosses **80%** — the products above that line are your "vital few" (top 20% driving 80% of revenue). Products in the bottom 20% of cumulative contribution (long tail) are candidates for review — they may be diluting margin through inventory/holding cost without contributing meaningfully to revenue.

---

### 4. Time-Series Forecast — Analysis ToolPak (Next-Quarter Revenue)

**Steps:**
1. First enable the ToolPak: `File` → `Options` → `Add-ins` → `Excel Add-ins` → `Go` → check **Analysis ToolPak**.
2. Aggregate the data to **Monthly Revenue** (PivotTable: Rows = Month-Year, Values = Sum of Revenue) — time series forecasting needs a clean, evenly-spaced series (12+ months ideally).
3. Two approaches:
   - **Quick approach – `FORECAST.ETS()`:** Use Excel's built-in exponential smoothing function (handles seasonality automatically):
     ```
     =FORECAST.ETS(target_date, known_revenue_range, known_date_range)
     ```
     Or select the data → `Data` → `Forecast Sheet` for a one-click seasonal forecast with confidence intervals.
   - **ToolPak approach – Exponential Smoothing / Moving Average:** `Data` → `Data Analysis` → **Exponential Smoothing** (set damping factor ~0.2–0.3) or **Moving Average** (period = 3 or 12 depending on seasonality) to smooth the series and project forward.
4. To explicitly capture **seasonality**, use `FORECAST.ETS.SEASONALITY()` to detect the seasonal cycle length, then feed that into `FORECAST.ETS()`.
5. **Identify variances:** Calculate `Variance = Actual − Forecast` for historical months where both exist; flag any month where `|Variance| > 1 standard deviation` of the residuals (`=STDEV.P(variance_range)`) as a significant anomaly (e.g., a promotion, stockout, or holiday spike not explained by seasonality alone).
6. Present as a line chart: Actual Revenue vs. Forecast, with the projected next-quarter (3 months) extended and confidence bands (upper/lower from `FORECAST.ETS.CONFINT()`) shaded.

---

## Section C: Mini Project

### 1. Title
**E-commerce Retention and Revenue Recovery Strategy**

### 2. Problem Statement
Analyze the divergence between steady foot traffic and stagnating revenue by identifying high-churn customer cohorts and underperforming geographic segments.

### 3. Dataset
[Kaggle – Online Retail Dataset](https://www.kaggle.com/datasets/carrie1/ecommerce-data)

### 4. Suggested Approach for Each Deliverable

**a) Cleaned Data Model (Power Query)**
- Remove cancelled orders (`InvoiceNo` starting with "C"), negative `Quantity`, null `CustomerID` rows (route to a separate "unattributed revenue" table rather than deleting outright), and duplicate rows.
- Create calculated columns: `Revenue`, `Order Month`, `Order Hour`, `Country` (already present — clean inconsistent naming, e.g. "EIRE" vs "Ireland" if present).
- Load as a proper data model with `Orders`, `Customers`, and `Products` split into related tables if doing a star-schema-style model (optional but ideal for PivotTable performance).

**b) Descriptive KPI Dashboard (Excel)**
- Core KPIs: Total Revenue, Total Orders, AOV, Unique Customers, Revenue by Country (map or bar), Revenue Trend (monthly line), Top 10 Products by Revenue (Pareto).
- Build with linked PivotTables/PivotCharts + slicers for Month and Country, on a single dashboard sheet.

**c) Monthly Cohort Analysis Table**
- Assign each customer a **cohort month** = month of their first purchase (`MINIFS` on `InvoiceDate` per `CustomerID`).
- Build a matrix: Rows = Cohort Month, Columns = Months Since First Purchase (0,1,2,...), Values = % of cohort still active (retention rate) — classic cohort heatmap, conditionally formatted.
- Use `COUNTIFS`/Power Pivot `DISTINCTCOUNT` with `DATEDIF`/month-difference calculations to populate the grid.

**d) Diagnostic Report on Customer Churn Drivers**
- Compare **repeat rate, AOV, and average order frequency** across countries/segments to isolate where churn concentrates.
- Segment customers via a simplified **RFM (Recency, Frequency, Monetary)** analysis — flag "at risk" (high past spend, long recency gap) vs. "healthy" segments.
- Cross-reference churn-heavy cohorts against geography to identify whether the revenue stagnation is concentrated in specific underperforming countries/regions (e.g., a market with rising order count but falling repeat rate signals an acquisition-heavy, retention-weak market).
- Conclude with 2–3 actionable recommendations (e.g., targeted win-back campaign for lapsed high-value customers, region-specific promotions where AOV is falling).

---

*Prepared as a complete methodology and answer guide for the TOPS Technologies "Advanced Excel For Analytics" assessment. Practical steps in Section B and C are ready to apply directly against your downloaded copy of the OnlineRetail dataset in Excel/Power Query.*
