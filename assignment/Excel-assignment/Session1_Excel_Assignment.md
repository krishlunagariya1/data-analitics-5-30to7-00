# Session 1 – Excel Interface, Layout & Data Types
### Assignment Solutions

---

## Task 1: Exploring the Excel Ribbon and Quick Access Toolbar

### Ribbon Tabs (3 tabs and their purpose)

| Tab | Purpose |
|---|---|
| **Home** | Contains the most frequently used commands — font formatting (bold, italic, font size/color), cell alignment, number formatting, styles (conditional formatting, cell styles), and basic editing tools (Sort & Filter, Find & Select). |
| **Insert** | Used to add objects into a worksheet such as Tables, PivotTables, Charts, Illustrations (images, icons, shapes), Sparklines, Hyperlinks, and Text Boxes/Headers-Footers. |
| **Data** | Used for working with external and internal data — Get & Transform Data (Power Query), Sort & Filter, Data Validation, Text to Columns, Remove Duplicates, and What-If Analysis. |
| **Formulas** *(bonus)* | Provides access to the Function Library, Name Manager, and formula auditing tools (Trace Precedents/Dependents), and lets you switch calculation options. |

### Quick Access Toolbar (2 tools)

| Tool | Purpose |
|---|---|
| **Save (Ctrl+S)** | Quickly saves the current workbook without navigating to the File tab. |
| **Undo / Redo (Ctrl+Z / Ctrl+Y)** | Reverts or reapplies the last action performed — very useful when correcting data entry mistakes. |

> The Quick Access Toolbar (top-left, above or below the ribbon) can be customized to add more one-click tools like Print Preview or New File.

---

## Task 2: Creating 'MyPlaylist.xlsx' with Two Worksheets

**Steps:**
1. Open Excel → **File → New → Blank Workbook**.
2. Save it immediately as **MyPlaylist.xlsx** (File → Save As → choose location → filename "MyPlaylist" → Save as type: Excel Workbook (*.xlsx)).
3. Rename **Sheet1** to **Songs** (double-click the sheet tab → type "Songs").
4. Right-click the sheet tab area → **Insert → Worksheet** → rename it **Artists**.

### Sheet: Songs

| Song Title | Artist | Duration (min) | Release Date | Genre |
|---|---|---|---|---|
| Blinding Lights | The Weeknd | 3.20 | 29-11-2019 | Pop |
| Shape of You | Ed Sheeran | 3.53 | 06-01-2017 | Pop |
| Bohemian Rhapsody | Queen | 5.55 | 31-10-1975 | Rock |
| Levitating | Dua Lipa | 3.23 | 01-10-2020 | Pop |
| Kal Ho Naa Ho | Sonu Nigam | 5.22 | 28-11-2003 | Bollywood |

### Sheet: Artists

| Artist Name | Country | Debut Year | Genre | Monthly Listeners (millions) |
|---|---|---|---|---|
| The Weeknd | Canada | 2010 | 15-09-2010 → *(see note)* | 95 |
| Ed Sheeran | UK | 2011 | Pop | 82 |
| Queen | UK | 1970 | Rock | 45 |
| Dua Lipa | UK | 2015 | Pop | 78 |
| Sonu Nigam | India | 1991 | Bollywood | 20 |

> Note: This sample data intentionally mixes **Text** (Song Title, Artist, Genre), **Numbers** (Duration, Monthly Listeners, Debut Year), and **Dates** (Release Date) to satisfy the "mix of data types" requirement.

---

## Task 3: A1 vs R1C1 Referencing – Summing Song Duration

Assume Duration values are in **B2:B6** of the Songs sheet, with the total in **B7**.

### Step 1 — A1 Style (default mode)
```
=SUM(B2:B6)
```
This is the standard, human-readable style where columns are letters (A, B, C…) and rows are numbers (1, 2, 3…).

### Step 2 — Enable R1C1 Mode
Go to: **File → Options → Formulas → Formula section → check "R1C1 reference style" → OK**

### Step 3 — R1C1 Style
Once enabled, the same formula in cell B7 automatically displays as:
```
=SUM(R[-5]C:R[-1]C)
```
**Explanation:**
- `R` = Row, `C` = Column.
- `R[-5]C` means "5 rows above, same column" → refers to B2.
- `R[-1]C` means "1 row above, same column" → refers to B6.
- Column headers change from letters (A, B, C) to numbers (1, 2, 3), and row references become relative offsets `[ ]` from the active cell instead of fixed row numbers.

### Observation
- **A1 mode** is easier to read and is Excel's default — great for everyday use.
- **R1C1 mode** shows the *relative position* of cells from the formula's location, which is useful for auditing formulas across large sheets or understanding relative references in VBA macros.
- Switching modes does **not** change what the formula calculates — only how the reference is *displayed*.

---

## Task 4: GST Calculator — Absolute vs Relative References

### Setup

| Cell | Content |
|---|---|
| B1 | GST Rate → `0.18` (18%) |
| A2:A6 | Item Price (e.g., 500, 1200, 750, 2000, 300) |
| C2:C6 | GST Amount (formula) |

### Using Relative Reference (B1 without $)
In C2:
```
=A2*B1
```
When copied down to C3, C4… Excel auto-adjusts **both** references:
```
C3 → =A3*B2   ❌ (wrong — GST rate cell shifted too, but B2 is empty!)
```
**Problem:** Since B1 (GST rate) must stay fixed for every row, a relative reference breaks as soon as you copy the formula down — it starts pointing to the wrong (empty) cell.

### Using Absolute Reference ($B$1)
In C2:
```
=A2*$B$1
```
When copied down:
```
C3 → =A3*$B$1
C4 → =A4*$B$1
C5 → =A5*$B$1
```
**Result:** A2 (relative) still updates correctly for each row, but $B$1 (absolute) stays locked to the GST rate cell no matter where the formula is copied.

### Sample Output Table

| Item Price (A) | GST Rate (B1 = 0.18) | GST Amount (C) = A*$B$1 |
|---|---|---|
| 500 | | 90 |
| 1200 | | 216 |
| 750 | | 135 |
| 2000 | | 360 |
| 300 | | 54 |

**Key takeaway:**
- **Relative reference (`A1`)** changes automatically when a formula is copied to another cell.
- **Absolute reference (`$A$1`)** stays fixed/locked regardless of where the formula is copied — done by pressing **F4** after selecting the cell reference, or manually typing `$` before the column and row.

---

## Task 5: Fixing Incorrect Data Types in a Raw Dataset

**Dataset used:** Sample Amazon/Flipkart order history export (CSV) — columns: Order ID, Order Date, Product, Category, Price, Quantity, Delivery Status.

### Step 1: Import and Inspect
Open the CSV/XLSX file in Excel. Select each column and check the alignment:
- **Text** → left-aligned by default
- **Numbers/Dates** → right-aligned by default

This alignment check quickly reveals type mismatches.

### Three Columns with Incorrect Data Types Found

| Column | Issue | Evidence |
|---|---|---|
| **Order Date** | Stored as Text (left-aligned), values like `"12/03/2024"` as a text string | `ISNUMBER()` returns FALSE; date filters/sort don't work correctly |
| **Price** | Stored as Text — contains currency symbol `"₹1,299"` or leading apostrophe | Cannot use SUM()/AVERAGE() — formula returns 0 or #VALUE! |
| **Order ID** | Numbers stored as Text (imported from a system that zero-padded IDs, e.g., `"00123"`) | Left-aligned; sorting gives text order (1, 10, 100…) instead of numeric order |

### Correction Steps

**1. Fixing Order Date (Text → Date):**
- Select column → **Data tab → Text to Columns → Delimited → Next → Next**
- In Step 3, under "Column data format," select **Date** and choose the correct format (DMY/MDY) → **Finish**
- Excel converts the text strings into true date serial numbers (now right-aligned).
- Alternative: use formula `=DATEVALUE(A2)` in a helper column, then paste values back.

**2. Fixing Price (Text → Number):**
- Use **Find & Replace** (Ctrl+H) to remove the currency symbol (₹) and commas.
- Select the column → **Data → Text to Columns → Finish** (this forces Excel to re-evaluate the cell as a number), OR
- Use a helper column: `=VALUE(SUBSTITUTE(SUBSTITUTE(A2,"₹",""),",",""))`
- Copy the helper column → Paste Special → Values back into the original column.

**3. Fixing Order ID (Text → Number, where numeric sorting is needed):**
- Select the range → click the small **yellow warning icon** (Error Checking) that appears → choose **"Convert to Number."**
- Or: select an empty cell, enter `1`, copy it, select the Order ID column → **Paste Special → Multiply** (this forces text-numbers to become real numbers instantly).

### Verifying the Fix
- Use `=ISNUMBER(cell)` or `=ISTEXT(cell)` in a helper column to confirm the correction.
- Reapply **Sort** and confirm dates sort chronologically and prices sort numerically (not alphabetically).
- Use **Format Cells (Ctrl+1)** to apply proper formatting: `dd-mm-yyyy` for dates, `₹#,##0.00` (Currency) for price, and `General/Number` for Order ID.

### Summary of Tools Used
| Tool | Used For |
|---|---|
| Text to Columns | Bulk-converting text dates/numbers to proper data types |
| Format Cells (Ctrl+1) | Applying correct display formatting after conversion |
| VALUE() / DATEVALUE() | Formula-based conversion for stubborn text entries |
| Paste Special → Multiply | Quick trick to convert text-numbers to true numbers |
| ISNUMBER() / ISTEXT() | Verifying that the data type correction worked |

---
*End of Session 1 Assignment*
