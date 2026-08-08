# Session 22 – Introduction to Macros & Recording Automations
## Solved Assignment

**Files used (attached alongside this document):**
- `food_orders_10.xlsx` — 10 food delivery orders (Order ID, Restaurant, Amount, Status), for Task 2
- `instagram_followers.xlsx` — an Instagram-style follower list in column A, deliberately containing **4 blank rows** and **unsorted names** (several starting with "A"), for Tasks 4 & 5

> **Important note on this session specifically:** macros are recorded by *your actions inside Excel* — the macro recorder watches clicks and keystrokes in real time and writes VBA behind the scenes. That recording process genuinely cannot be pre-built into a file; there's no "run the recorder for you" step outside of Excel itself. What's below is the exact, faithful sequence of clicks to perform for each task so your recording captures precisely the right macro — and the two datasets above are ready to open and record against directly.

---

## Task 1 — Enable Developer Tab + Record "Name in A1, Bold"

**Enable the Developer tab (one-time setup):**
1. **File → Options → Customize Ribbon.**
2. In the right-hand list, tick **Developer** → **OK**. The Developer tab now appears in the ribbon.

**Record the macro:**
1. Open a new blank workbook.
2. **Developer tab → Record Macro.**
3. In the dialog: Macro name: `EnterMyName` (no spaces allowed in macro names) → Shortcut key: optional → Store macro in: **This Workbook** → **OK**. Recording has now started.
4. Click cell **A1** → type your name → press **Enter**.
5. Click **A1** again → press **Ctrl+B** (or Home tab → Bold) to bold it.
6. **Developer tab → Stop Recording.**

Your name now sits bold in A1, and every step (select A1, type value, select A1, apply bold) has been captured into a VBA sub named `EnterMyName`.

---

## Task 2 — Record a Macro: Format Header Row + Auto-Fit Column Widths

Open `food_orders_10.xlsx` for this one.

**Steps:**
1. **Developer tab → Record Macro** → name it `FormatOrdersHeader` → Store in: This Workbook → **OK**.
2. Select the header row (row 1, columns A:D — click and drag across **A1:D1**, or click the row-1 number on the left to select the whole row).
3. **Home tab → Fill Color** → pick a background color (e.g., light blue or green).
4. While still selected, optionally also apply **bold** (Home → Bold) so the header stands out further — not required by the task but a common pairing.
5. Now select the whole used range or all four columns (click column headers **A** through **D**, holding Shift/drag across them).
6. **Home tab → Format → AutoFit Column Width** (in the Cells group) — this is the "auto-adjusts all column widths" step; alternatively double-click the boundary between any two column headers, but doing it via the Format menu records more reliably as one clean step.
7. **Developer tab → Stop Recording.**

Result: header row colored, columns sized to fit their widest content — and the whole sequence is now replayable on any similarly-shaped order sheet via **Developer → Macros → FormatOrdersHeader → Run**.

---

## Task 3 — Save as .xlsm and Verify the Macro Survives Close/Reopen

**Steps:**
1. **File → Save As.**
2. In the "Save as type" dropdown, choose **Excel Macro-Enabled Workbook (*.xlsm)** — a plain `.xlsx` **silently discards all macros on save**, which is the single most common mistake at this stage.
3. Give it a name (e.g., `food_orders_macros.xlsm`) → **Save**. Excel may show a compatibility warning about macros — that's expected and fine, since you deliberately chose the `.xlsm` format to keep them.
4. **Close the file completely**, then reopen it.
5. On reopen, Excel shows a **yellow "SECURITY WARNING – Macros have been disabled"** bar below the ribbon (this is Excel protecting you from unknown macro-laden files by default). Click **Enable Content** on that bar to allow the macros in this specific file to run.
6. **Developer tab → Macros** → select `FormatOrdersHeader` (or `EnterMyName`) → **Run** → confirm it executes correctly, applying the same header color/column-width formatting again.

**Verification checklist:**
- File extension shows `.xlsm` in the title bar / File Explorer, not `.xlsx`.
- The macro appears in the **Developer → Macros** list after reopening.
- Running it a second time reproduces the same visible result (color + auto-fit) without errors.

---

## Task 4 — Record a Macro: Delete Blank Rows, Then Sort Alphabetically

Open `instagram_followers.xlsx` for this one — column A has 20 rows with 4 intentional blanks scattered through an unsorted name list.

**Steps:**
1. **Developer tab → Record Macro** → name it `CleanSortFollowers` → **OK**.
2. Select the full name range, e.g. **A2:A20** (or select the whole column A by clicking its header if you're comfortable operating on the full column).
3. **Home tab → Find & Select → Go To Special → Blanks → OK** — this selects only the empty cells within your selection.
4. **Right-click any selected blank cell → Delete → "Shift cells up"** → **OK**. All blank rows collapse out and the list shifts up to close the gaps.
5. Now select the (now shorter, gap-free) name list again — e.g., **A2:A16**.
6. **Data tab → Sort A to Z** (the AZ↓ button) — for a single column this is a one-click alphabetical sort; if prompted about "expand the selection," choose to sort only the selected column since there's nothing else beside it.
7. **Developer tab → Stop Recording.**

Result: no blank rows remain, and every name is alphabetically ordered (Aditi Joshi, Aisha Khan, Alok Bhatt, Amit Verma, Anjali Desai, Ananya Sharma, Arjun Nair, ... down to Yash Thakkar).

---

## Task 5 — Edit the Macro: Highlight Names Starting With "A" in Yellow

**Constraint respected:** everything below uses only the macro recorder and Excel's built-in menus — no VBA is typed or hand-edited. "Editing the macro" here means **recording a second pass and appending it**, or **re-recording the whole sequence with the extra step included** — both are valid, purely recorder-driven ways to "edit" a macro without touching code.

**Steps (recording the additional highlight step):**
1. **Developer tab → Record Macro** → name it `HighlightAFollowers` (a new macro that adds to what Task 4 built — you can later run both in sequence, or re-record Task 4 end-to-end with this step folded in).
2. Select the cleaned, sorted name range (e.g., **A2:A16**, following on from Task 4's result).
3. **Home tab → Conditional Formatting → New Rule.**
4. Choose **"Format only cells that contain."**
5. Set the rule to: **Cell Value → begins with → A** (type `A` in the value box — tick "match case" only if you specifically want capital-A only, which is appropriate here since names are capitalized).
6. Click **Format…** → **Fill tab** → choose **yellow** → **OK** → **OK** to confirm the rule.
7. **Developer tab → Stop Recording.**

**Result:** every follower name beginning with "A" (Aditi Joshi, Aisha Khan, Alok Bhatt, Amit Verma, Anjali Desai, Ananya Sharma, Arjun Nair) is now highlighted yellow, and this was achieved entirely by clicking through **Home → Conditional Formatting → New Rule** while the recorder was running — never by opening the VBA editor.

**To combine Tasks 4 and 5 into one single macro** (optional, but tidy): **Developer tab → Macros** → select `CleanSortFollowers` → **Run**, immediately followed by running `HighlightAFollowers` → then record one final short macro (`Record Macro` → run nothing but immediately `Stop Recording` isn't useful) — practically, the clean way to merge two recorder-made macros without hand-editing VBA is to just **re-record the entire sequence once, start to finish** (delete blanks → sort → apply conditional formatting) under one macro name, e.g. `CleanSortHighlightFollowers`, so it's a single click to reproduce all of Task 4 + Task 5 together.

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | Developer tab + Record Macro (name entry, bold) | File → Options → Customize Ribbon; Developer → Record Macro |
| 2 | Record Macro (fill color, AutoFit column width) | Home → Fill Color; Home → Format → AutoFit Column Width |
| 3 | Save As .xlsm; Enable Content on reopen | File → Save As → Excel Macro-Enabled Workbook |
| 4 | Record Macro (Go To Special → Blanks, Delete, Sort A→Z) | Home → Find & Select → Go To Special; Data → Sort |
| 5 | Record Macro (Conditional Formatting rule) | Home → Conditional Formatting → New Rule |
