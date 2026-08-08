# Session 3 – Sorting, Basic & Advanced Filtering
### Assignment Solutions

---

## Sample Dataset Used (Throughout All Tasks)

| Region | Product | Sales |
|---|---|---|
| East | Pizza | 6500 |
| West | Burger | 9200 |
| North | Pasta | 4300 |
| South | Pizza | 7800 |
| East | Burger | 5100 |
| West | Pasta | 8900 |
| North | Pizza | 3200 |
| South | Burger | 6700 |
| East | Pasta | 9500 |
| West | Pizza | 4700 |

*(A blank row has intentionally been left after row 6 and row 9 in the working file to simulate a "raw export" for Task 5.)*

---

## Task 1: Basic Ascending Sort on Sales

### Steps
1. Click any single cell inside the **Sales** column (e.g., C5).
2. Go to **Data tab → Sort A to Z** (the "AZ↓" icon), or **Data → Sort → Column: Sales → Order: Smallest to Largest**.
3. Excel automatically detects the full table range (as long as there are no blank rows breaking it) and sorts every row together, keeping Region/Product aligned with their correct Sales value.

### Result (Sales ascending)

| Region | Product | Sales |
|---|---|---|
| North | Pizza | 3200 |
| North | Pasta | 4300 |
| West | Pizza | 4700 |
| East | Burger | 5100 |
| East | Pizza | 6500 |
| South | Burger | 6700 |
| South | Pizza | 7800 |
| West | Pasta | 8900 |
| West | Burger | 9200 |
| East | Pasta | 9500 |

> **Tip:** Always select a single cell (not just the column) before sorting so Excel's "Expand the selection" prompt keeps entire rows together — sorting only the Sales column in isolation would break the Region/Product pairing.

---

## Task 2: Multi-Level Sort (Region → Product → Sales)

### Steps
1. Select any cell within the data → **Data tab → Sort** (opens the Sort dialog).
2. Ensure **"My data has headers"** is checked.
3. Set the first level:
   - **Sort by:** Region
   - **Order:** A to Z
4. Click **Add Level**, set the second level:
   - **Then by:** Product
   - **Order:** A to Z
5. Click **Add Level** again, set the third level:
   - **Then by:** Sales
   - **Order:** Largest to Smallest
6. Click **OK**.

### Result

| Region | Product | Sales |
|---|---|---|
| East | Burger | 5100 |
| East | Pasta | 9500 |
| East | Pizza | 6500 |
| North | Pasta | 4300 |
| North | Pizza | 3200 |
| South | Burger | 6700 |
| South | Pizza | 7800 |
| West | Burger | 9200 |
| West | Pasta | 8900 |
| West | Pizza | 4700 |

**Explanation:** Excel first groups all rows by Region alphabetically. Within each Region group, rows are further sorted alphabetically by Product. Within any Region+Product combination that has multiple entries, Sales would be arranged largest to smallest (not visible above since each Region-Product pair is unique in this sample, but the rule is applied by Excel regardless).

---

## Task 3: AutoFilter — Show Only 'Pizza' or 'Burger'

### Steps
1. Select the data range (including headers) → **Data tab → Filter** (or Ctrl+Shift+L). Dropdown arrows appear on each header.
2. Click the dropdown arrow on the **Product** header.
3. Uncheck **"Select All"** first, then check only:
   - ☑ Pizza
   - ☑ Burger
   - ☐ Pasta *(leave unchecked)*
4. Click **OK**.

### Result — Filtered View

| Region | Product | Sales |
|---|---|---|
| East | Pizza | 6500 |
| West | Burger | 9200 |
| South | Pizza | 7800 |
| East | Burger | 5100 |
| North | Pizza | 3200 |
| South | Burger | 6700 |
| West | Pizza | 4700 |

All **Pasta** rows are temporarily hidden (not deleted) — exactly like tapping the "Pizza" or "Burger" category chip on Zomato hides all other cuisine cards without removing them from the menu.

---

## Task 4: Advanced Filter — Sales > 8000 AND Region = West

### Step 1: Set Up the Criteria Range
Above (or beside) the main data table, create a small criteria range using the **exact same column headers**:

| Region | Sales |
|---|---|
| West | >8000 |

*(Placed, for example, in cells E1:F2, while the main data table is in A1:C11.)*

Because both conditions are on the **same row**, Excel's Advanced Filter treats them as an **AND** condition (Region = West **AND** Sales > 8000). If they were on separate rows, it would be treated as OR.

### Step 2: Apply Advanced Filter
1. Click any cell inside the main data table.
2. Go to **Data tab → Advanced** (in the Sort & Filter group).
3. In the dialog:
   - **Action:** Choose "Filter the list, in-place" (or "Copy to another location" to keep the original data untouched).
   - **List range:** `$A$1:$C$11` (your full data table).
   - **Criteria range:** `$E$1:$F$2` (the criteria block you built).
   - *(If copying elsewhere)* **Copy to:** e.g., `$H$1`
4. Click **OK**.

### Result

| Region | Product | Sales |
|---|---|---|
| West | Burger | 9200 |
| West | Pasta | 8900 |

Only rows where **Region = West** and **Sales > 8000** remain visible — West/Pizza (4700) is correctly excluded since it fails the Sales condition.

---

## Task 5: Removing Blank Rows Efficiently (Without Manual Deletion)

**Constraint:** No manual one-by-one row deletion — use a built-in Excel feature.

### Method: Go To Special → Blanks → Delete Entire Row

1. Select the entire data range, e.g., **A1:C11** (including any blank rows within it).
2. Press **Ctrl+G** (or **Home tab → Find & Select → Go To Special…**) to open the **Go To Special** dialog.
3. Select **Blanks** → click **OK**.
   - Excel now selects every empty cell within the selected range simultaneously.
4. Go to **Home tab → Delete → Delete Sheet Rows** (or right-click any selected blank cell → **Delete → Entire Row**).
5. All rows containing the selected blank cells are removed in one action, and the remaining data automatically shifts up to close the gaps.

### Alternative Method: Filter-Based Removal
1. Apply **AutoFilter** (Ctrl+Shift+L) on the header row.
2. Click the dropdown on any key column (e.g., Region) → uncheck **"Select All"**, then check only **"Blanks."**
3. This isolates just the blank rows.
4. Select all visible (blank) rows → **Home → Delete → Delete Sheet Rows**.
5. Turn off the filter (Ctrl+Shift+L) to see the cleaned dataset.

### Result
The dataset is now continuous with no gaps — exactly the kind of clean, analysis-ready table needed before building a PivotTable or chart from a Flipkart-style sales report.

| Region | Product | Sales |
|---|---|---|
| East | Pizza | 6500 |
| West | Burger | 9200 |
| North | Pasta | 4300 |
| South | Pizza | 7800 |
| East | Burger | 5100 |
| West | Pasta | 8900 |
| North | Pizza | 3200 |
| South | Burger | 6700 |
| East | Pasta | 9500 |
| West | Pizza | 4700 |

> **Why Go To Special is better than manual deletion:** it works in a single pass regardless of how many blank rows exist or where they are scattered, so it scales to datasets with thousands of rows — something manual row-by-row deletion cannot do efficiently.

---
*End of Session 3 Assignment*
