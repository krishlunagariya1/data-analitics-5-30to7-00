# Session 14 – Pivot Tables (Part 2: Advanced Features)
## Assignment Solution

**Dataset used:** `Food_Delivery_Orders_Sample.xlsx` (attached alongside this file)
A synthetic food-delivery dataset covering **Jan 2024 – Dec 2025**, 650 orders, with columns:

| Order ID | Order Date | City | Restaurant | Payment Mode | Order Amount (INR) |
|---|---|---|---|---|---|

Cities: Ahmedabad, Mumbai, Delhi, Bangalore, Rajkot
Restaurants: Burger King, Domino's Pizza, McDonald's, KFC, Pizza Hut, and a few local names

Use this in place of a live Zomato/Swiggy export — those platforms don't publish a public downloadable order-level dataset, so a realistic stand-in with the same structure (dates, amounts, city, restaurant) is used instead. All the steps below work identically on a real export if you get one later.

---

## Task 1 — Pivot Table grouped by Month and by Year

1. Select any cell inside the `Orders` table → **Insert → PivotTable** → New Worksheet.
2. Build the pivot:
   - **Rows:** `Order Date`
   - **Values:** `Order Amount (INR)` → set to **Sum**
3. Excel auto-groups dates into **Years** and **Months** the moment you drop a date field into Rows (Excel 2016+ does this automatically; in older versions right-click a date → **Group** → tick **Months** and **Years**).
4. Result: a two-level row hierarchy —
   ```
   2024
     Jan  ₹...
     Feb  ₹...
     ...
   2025
     Jan  ₹...
     ...
   ```
   This gives total sales by Month *within* each Year in one view.

---

## Task 2 — Group by Quarter, show latest year's quarterly trend

1. Right-click any date cell inside the Pivot Table row area → **Group…**
2. In the Grouping dialog, under **By**, select only **Quarters** (and keep **Years** selected if you want year+quarter together) → click **OK**.
3. To isolate the latest year (2025):
   - Click the filter arrow on the `Order Date`/Year field → uncheck 2024, keep only **2025**.
4. Result — quarterly sales trend for 2025:

   | Quarter | Total Sales (₹) |
   |---|---|
   | Qtr1 | ~₹XX,XXX |
   | Qtr2 | ~₹XX,XXX |
   | Qtr3 | ~₹XX,XXX |
   | Qtr4 | ~₹XX,XXX |

   (Exact values populate once you build the pivot on the real workbook — Qtr4 is typically highest due to the Nov–Dec festive/holiday order bump built into the sample data.)

---

## Task 3 — Calculated Field: Average Order Value per Month

1. Click inside the Pivot Table → **PivotTable Analyze** tab → **Fields, Items & Sets → Calculated Field…**
2. Name: `Avg Order Value`
3. Formula:
   ```
   = 'Order Amount (INR)' / COUNT('Order ID')
   ```
   (This divides total order value by the count of orders — Excel calculated fields always aggregate as SUM internally, so `SUM(Amount)/COUNT(OrderID)` correctly yields the average per group.)
4. Click **Add → OK**. `Avg Order Value` now appears as a new field in the Values area, automatically broken out by Month (and Year), since the row grouping from Task 1 already exists.
5. Format the new field as currency (right-click a value → **Number Format → Currency**).

---

## Task 4 — Slicer for City / Restaurant

1. Click inside the Pivot Table → **PivotTable Analyze → Insert Slicer**.
2. Tick **City** (or **Restaurant**, or both) → **OK**.
3. A floating slicer box appears with clickable buttons for each city (Ahmedabad, Mumbai, Delhi, Bangalore, Rajkot) / each restaurant (Burger King, Domino's Pizza, McDonald's, KFC, Pizza Hut...).
4. Click **"Ahmedabad"** (or **"Burger King"**) on the slicer — the entire pivot (monthly/quarterly totals, average order value) instantly recalculates to show only that city's/restaurant's numbers.
5. Hold **Ctrl** while clicking to select multiple cities/restaurants at once; click the "clear filter" icon on the slicer to reset.

---

## Task 5 — Drill-down on a Quarterly Total

1. In the Pivot Table (Task 2's quarterly view), find e.g. the **Qtr4 2025** total cell.
2. **Double-click** that cell.

**What happens (per the constraint):**
- Excel automatically inserts a **brand-new worksheet** (named something like `Sheet5` or auto-numbered) **placed immediately to the left of the Pivot Table sheet**.
- That new sheet contains a **static, flat table** — not a pivot — listing **every individual source row (order)** that was summed into that Qtr4-2025 total: their `Order ID`, `Order Date`, `City`, `Restaurant`, `Payment Mode`, and `Order Amount (INR)`, exactly as they appear in the original `Orders` table, filtered down to just that quarter.
- This extracted list is a **one-time snapshot** — it does not update if the source data or the pivot changes, and it isn't linked back to the Pivot Table (deleting it doesn't affect the pivot). It's meant purely for ad-hoc inspection of "what's behind this number," e.g., verifying which specific orders drove Qtr4's total.

---

### Quick recap of where to click for each feature

| Feature | Location |
|---|---|
| Group dates | Right-click date in pivot → Group |
| Calculated Field | PivotTable Analyze → Fields, Items & Sets |
| Slicer | PivotTable Analyze → Insert Slicer |
| Drill-down | Double-click any value cell in the pivot |
