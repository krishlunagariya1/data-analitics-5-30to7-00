# Session 13 – Pivot Tables (Part 1: Basics)
### Assignment Solutions

---

## Sample Dataset Used (Throughout All Tasks)

A food delivery order dataset with 50+ rows and columns: **Order ID, Restaurant, City, Delivery Partner, Amount**. A representative sample is shown below (the full working dataset would extend to 50+ rows following the same pattern):

| Order ID | Restaurant | City | Delivery Partner | Amount |
|---|---|---|---|---|
| FD001 | Domino's | Ahmedabad | Ravi Patel | 650 |
| FD002 | Behrouz Biryani | Surat | Amit Shah | 890 |
| FD003 | KFC | Ahmedabad | Kiran Joshi | 540 |
| FD004 | Domino's | Vadodara | Ravi Patel | 720 |
| FD005 | Faasos | Ahmedabad | Amit Shah | 480 |
| FD006 | Behrouz Biryani | Rajkot | Kiran Joshi | 1100 |
| FD007 | KFC | Surat | Ravi Patel | 610 |
| FD008 | Domino's | Ahmedabad | Kiran Joshi | 980 |
| FD009 | Faasos | Vadodara | Amit Shah | 390 |
| FD010 | Behrouz Biryani | Ahmedabad | Ravi Patel | 1250 |
| ... | ... | ... | ... | ... |
| FD050 | KFC | Rajkot | Amit Shah | 700 |

*(Data continues to 50+ rows, spanning cities: Ahmedabad, Surat, Vadodara, Rajkot; restaurants: Domino's, Behrouz Biryani, KFC, Faasos; and delivery partners: Ravi Patel, Amit Shah, Kiran Joshi.)*

---

## Task 1: Pivot Table — Total Amount by City

### Steps
1. Click any cell inside the dataset.
2. Go to **Insert tab → PivotTable → "From Table/Range"**.
3. Confirm the data range is correctly detected (e.g., `A1:E51`) and choose **"New Worksheet"** as the destination → **OK**.
4. In the **PivotTable Fields** pane on the right:
   - Drag **City** into the **Rows** area.
   - Drag **Amount** into the **Values** area (it will automatically default to **Sum of Amount**).

### Result (Pivot Table Output)

| City (Rows) | Sum of Amount |
|---|---|
| Ahmedabad | 18,450 |
| Surat | 12,300 |
| Vadodara | 9,870 |
| Rajkot | 8,600 |
| **Grand Total** | **49,220** |

*(Values shown are illustrative totals consistent with a 50+ row dataset — exact figures depend on your actual downloaded data.)*

---

## Task 2: Pivot Table — Restaurant (Rows) × City (Columns), Sum of Amount

### Steps
1. Using the same Pivot Table (or a fresh one from the same data source):
   - Drag **Restaurant** into the **Rows** area.
   - Drag **City** into the **Columns** area.
   - Keep **Amount** in the **Values** area (Sum of Amount).

### Result (Cross-Tabulated Pivot Table)

| Restaurant (Rows) | Ahmedabad | Surat | Vadodara | Rajkot | Grand Total |
|---|---|---|---|---|---|
| Domino's | 5,200 | 2,900 | 3,100 | 1,800 | 13,000 |
| Behrouz Biryani | 6,100 | 3,400 | 2,200 | 4,500 | 16,200 |
| KFC | 3,800 | 4,100 | 2,700 | 2,100 | 12,700 |
| Faasos | 3,350 | 1,900 | 1,870 | 200 | 7,320 |
| **Grand Total** | **18,450** | **12,300** | **9,870** | **8,600** | **49,220** |

**Explanation:** Placing a field in **Rows** creates one row per unique value (each Restaurant), while placing a field in **Columns** creates one column per unique value (each City). The intersection cell shows the **Sum of Amount** for that specific Restaurant + City combination — this is exactly how a Pivot Table performs a two-dimensional cross-tabulation without writing any formulas manually.

---

## Task 3: Change Values from SUM of Amount to COUNT of Orders by Delivery Partner

### Steps
1. Remove the current field layout: drag **Restaurant** and **City** back out of the Rows/Columns areas (or start a fresh Pivot Table on a new sheet).
2. Drag **Delivery Partner** into the **Rows** area.
3. Drag **Order ID** (or **Amount** — any field works for counting) into the **Values** area.
4. By default, a text/ID field defaults to **Count**, but if it shows "Sum," click the dropdown arrow next to the field in the Values area → **Value Field Settings… → Summarize value field by: Count → OK**.

### Result

| Delivery Partner (Rows) | Count of Order ID |
|---|---|
| Ravi Patel | 18 |
| Amit Shah | 16 |
| Kiran Joshi | 17 |
| **Grand Total** | **51** |

**Explanation:** Switching the summarization type from **Sum** to **Count** changes what the Pivot Table calculates for each group — instead of adding up the Amount values, it now simply counts how many order rows fall under each Delivery Partner, which directly answers "how many orders did each partner deliver?"

---

## Task 4: Add a City Filter to the Pivot Table

### Steps
1. On the Pivot Table (using either the Task 1 or Task 3 layout), drag **City** into the **Filters** area of the PivotTable Fields pane.
2. A filter dropdown cell (labeled "City") now appears above the Pivot Table on the worksheet.
3. Click the dropdown arrow next to it → select **Ahmedabad** → **OK** (uncheck "Select All" first if multiple selections are shown, or simply pick the single city from the list).

### Result — Before Filter (All Cities, using Task 3's layout)

| Delivery Partner (Rows) | Count of Order ID |
|---|---|
| Ravi Patel | 18 |
| Amit Shah | 16 |
| Kiran Joshi | 17 |
| **Grand Total** | **51** |

### Result — After Filtering to City = Ahmedabad

| City: | Ahmedabad |
|---|---|
| **Delivery Partner (Rows)** | **Count of Order ID** |
| Ravi Patel | 7 |
| Amit Shah | 6 |
| Kiran Joshi | 5 |
| **Grand Total** | **18** |

### Observation
Once the filter is applied, the Pivot Table **instantly recalculates** every value in the Rows/Values area to reflect only the rows where City = "Ahmedabad" — the Grand Total drops from 51 (all cities) down to 18 (Ahmedabad only), and each Delivery Partner's individual count also shrinks to match only their Ahmedabad deliveries. This demonstrates the core power of Pivot Table filters: the same table structure can be re-analyzed for any subset of the data in seconds, without rebuilding the table or writing new formulas.

> **Tip:** For a more visual/interactive way to filter (especially useful when switching between multiple cities frequently), you can also insert a **Slicer** (PivotTable Analyze tab → Insert Slicer → City) instead of using the plain Filters-area dropdown — Slicers show all city buttons at once and highlight the currently selected one.

---
*End of Session 13 Assignment*
