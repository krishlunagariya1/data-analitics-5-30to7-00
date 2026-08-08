# Session 16 – Data Cleaning Tools & Error Handling
## Solved Assignment

**Dataset used:** `data_cleaning_practice.xlsx` (attached alongside this file) — a 3-sheet workbook:

| Sheet | Contents |
|---|---|
| `Orders` | 30 online orders — Order ID, Customer Name, Zomato-style Address, Amount (5 rows are intentional duplicates for Task 1) |
| `Contacts` | 10 customers with Email and Phone Number (for Tasks 3 & 4) |
| `PlayerStats` | 10 IPL players with Runs, Balls, Innings, and **formulas** for Strike Rate / Average — 2 players are set up to intentionally break with `#DIV/0!` and `#VALUE!` (for Task 5) |

---

## Task 1 — Remove Duplicates from the Orders List

The `Orders` sheet has 30 rows, 5 of which are exact duplicate order records (same customer, address, and amount re-entered under a new Order ID — a common real-world "customer re-submitted the order" glitch).

**Steps:**
1. Select any cell inside the `Orders` table.
2. **Data tab → Data Tools group → Remove Duplicates.**
3. In the dialog, **untick "Order ID"** (since every row has a unique ID, that column would never register a duplicate) — keep **Customer Name, Address, Order Amount** ticked.
4. Click **OK**. Excel reports how many duplicate rows it removed (5 in this dataset) and how many unique records remain (25).

**Why untick Order ID:** Remove Duplicates compares *all ticked columns together* — if you leave a truly-unique column ticked, nothing will ever look like a duplicate. The lesson here is to duplicate-check on the business-meaning columns, not the auto-generated ID.

---

## Task 2 — Text to Columns: Split the Address

Example address in the dataset: `Flat 12B, Sunrise Apartments, SG Highway, Ahmedabad`

**Steps:**
1. Select the **Address** column (click the column header).
2. **Data tab → Data Tools → Text to Columns.**
3. Choose **Delimited** → Next.
4. Tick **Comma** as the delimiter (the address fields are comma-separated, not space-separated — spaces appear *inside* fields like "Sunrise Apartments", so Comma is the correct choice per the hint).
5. Preview shows 4 clean columns forming automatically → Next → Finish.
6. Rename the resulting headers to: **Flat/House No.** | **Building Name** | **Street** | **City**.

**Result:**

| Flat/House No. | Building Name | Street | City |
|---|---|---|---|
| Flat 12B | Sunrise Apartments | SG Highway | Ahmedabad |
| House 4 | Vrindavan Society | CG Road | Ahmedabad |
| Flat 302 | Skyline Towers | MG Road | Mumbai |

> Tip: since Text to Columns overwrites the columns to its right, insert 3 blank columns after Address first, or run it with the destination cell pointed at a blank area.

---

## Task 3 — Flash Fill: Extract Username from Email

On the `Contacts` sheet, Email is e.g. `rahul.patel99@gmail.com` and you want `rahul.patel99` in a new column.

**Steps:**
1. Insert a new column next to Email, header it **Username**.
2. In the first data row, manually type the expected result: `rahul.patel99` (everything before the `@`).
3. Click the next cell down → **Data tab → Data Tools → Flash Fill** (or just press **Ctrl+E**).
4. Excel detects the pattern ("take the text before @") from your one example and auto-fills the rest of the column instantly.
5. Spot-check a few rows — Flash Fill is pattern-based, not formula-based, so if any email has an unusual format it may fill incorrectly and need a manual fix.

**Result:**

| Email | Username |
|---|---|
| rahul.patel99@gmail.com | rahul.patel99 |
| priya.shah22@yahoo.com | priya.shah22 |
| aman_verma07@gmail.com | aman_verma07 |

---

## Task 4 — Find & Replace with Wildcards: Phone Numbers Starting '98' → '99'

On the `Contacts` sheet, numbers like `9876543210` should become `9976543210` — i.e., replace the number's **first two digits only** if they are `98`, leaving the remaining 8 digits untouched.

**Steps:**
1. Select the **Phone Number** column.
2. **Home tab → Find & Select → Replace** (or **Ctrl+H**).
3. Click **Options >>** to reveal advanced settings, and make sure **"Match entire cell contents"** is ticked (so it doesn't accidentally match `98` anywhere mid-string, e.g. inside a different number).
4. In **Find what**, type: `98????????` (that's `98` followed by 8 question marks — each `?` is a wildcard matching exactly one character, so this pattern matches any 10-digit number starting with 98).
5. Excel's Find & Replace wildcards don't support "keep the matched wildcard characters" the way regex back-references do — so instead:
   - **Better approach used here:** Find what: `98*` with "Match entire cell contents" ON, Replace with: `99` — this only works if you're fully replacing, which isn't right for preserving the last 8 digits.
   - **Correct approach:** Since Find & Replace can't capture-and-reuse wildcard characters, do this with a **helper formula** instead, then paste values back:
     ```
     =IF(LEFT(A2,2)="98","99"&RIGHT(A2,8),A2)
     ```
   - Fill this down the Phone Number list, then **Copy → Paste Special → Values** back over the original column.
6. *(If your instructor specifically wants the native wildcard dialog for this task: use Find `98??????` with "Match entire cell" ON and Replace `99??????` — some Excel versions do preserve `?` positions literally in the Replace field for single-character wildcards; test on one cell first before running on the full column, since behavior here varies by Excel version.)*

**Result:**

| Before | After |
|---|---|
| 9876543210 | 9976543210 |
| 9812345678 | 9912345678 |
| 9945612378 | 9945612378 *(unchanged — didn't start with 98)* |

---

## Task 5 — Error Checking Ribbon Tools: Fix #DIV/0! and #VALUE! in IPL Player Stats

The `PlayerStats` sheet has **Strike Rate** (`=Runs/Balls*100`) and **Average** (`=Runs/Innings`) as live formulas. Two players are broken on purpose:
- **Jasprit Bumrah** — Balls Faced = 0 and Innings = 0 → both formulas throw **`#DIV/0!`**
- **Hardik Pandya** — Runs Scored entered as text `"N/A"` → both formulas throw **`#VALUE!`**
- **Ravindra Jadeja** — Balls Faced entered as text `"unknown"` → Strike Rate throws **`#VALUE!`**

**Steps:**
1. **Formulas tab → Formula Auditing → Error Checking.** Excel steps through every error cell one at a time, showing which formula and offering "Show Calculation Steps," "Trace Error," etc.
2. Alternatively, click the small **green triangle + warning icon** that appears in any error cell for the same options via a right-click-style dropdown.
3. **Fix the `#DIV/0!` errors (Jasprit Bumrah):** wrap the formulas in `IFERROR`, or better, `IF` to handle the zero explicitly:
   ```
   =IF(C2=0,"—",(B2/C2)*100)      ' Strike Rate
   =IF(D2=0,"—",B2/D2)            ' Average
   ```
   This shows a dash instead of an error when a player has 0 balls faced / 0 innings (e.g., an injured player who didn't bat).
4. **Fix the `#VALUE!` errors (Hardik Pandya, Ravindra Jadeja):** the root cause is text sitting in a numeric column. Correct it at the source — retype `Runs Scored` for Hardik Pandya as a number, and `Balls Faced` for Ravindra Jadeja as a number — then the formulas recalculate cleanly on their own. (Wrapping in `IFERROR` alone would *hide* the problem without fixing the underlying bad data — always fix the source value first, and only use `IFERROR`/`IF` for genuinely valid edge cases like a 0 denominator.)
5. Re-run **Error Checking** after the fixes — it should report "no errors found," confirming every formula now returns a valid result.

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | Remove Duplicates | Data → Data Tools → Remove Duplicates |
| 2 | Text to Columns (comma-delimited) | Data → Data Tools → Text to Columns |
| 3 | Flash Fill | Data → Data Tools → Flash Fill (Ctrl+E) |
| 4 | Find & Replace with wildcards / helper formula | Home → Find & Select → Replace (Ctrl+H) |
| 5 | Error Checking + IFERROR/IF + fixing source data | Formulas → Formula Auditing → Error Checking |
