# Session 17 – Power Query (Basics)
## Solved Assignment

**Files used:**
- `trending_movies.csv` — the raw source file (28 movies, columns: Title, Genre, Release Year, IMDb Rating). 5 rows have a **blank IMDb Rating**, and every Genre is stored as **comma-separated multi-genre text** (e.g., `Action, Thriller`) — these are the two problems you're asked to clean up.
- `cleaned_movies_preview.xlsx` — what your final result should look like after all 5 tasks (23 rows, first-genre-only, correct data types) so you can check your own output against it.

---

## Task 1 — Import the CSV via Power Query, Load to a New Worksheet

**Steps:**
1. **Data tab → Get Data → From File → From Text/CSV.**
2. Browse to and select `trending_movies.csv` → **Import**.
3. A preview window opens showing the raw data with correct headers detected (Title, Genre, Release Year, IMDb Rating). Instead of clicking **Load** directly, click **Transform Data** — this opens the **Power Query Editor**, which you need for Tasks 2–4.
4. *(If you just wanted a straight import with no cleaning, "Load" would dump it into a new worksheet immediately — but this assignment needs the Editor, so always route through Transform Data.)*

---

## Task 2 — Remove Rows Where IMDb Rating Is Blank

Inside the **Power Query Editor**:

1. Click the **filter arrow** on the **IMDb Rating** column header.
2. Untick **(blank)** in the value list (Power Query shows blanks/nulls as a selectable option in the filter dropdown) → **OK**.
   - Alternative: right-click the IMDb Rating column header → **Remove Empty** (a one-click equivalent).
3. This step appears in the **Applied Steps** pane on the right as something like `Filtered Rows`. The row count drops from 28 to 23 (5 blank-rating rows removed).

---

## Task 3 — Change Data Types: Release Year → Whole Number, IMDb Rating → Decimal Number

**Steps:**
1. Click the small **data-type icon** to the left of the **Release Year** column header (it currently shows `ABC123` = "Any"/text-ish, or already a number depending on CSV auto-detection).
2. From the dropdown, pick **Whole Number**.
3. Repeat for **IMDb Rating** → pick **Decimal Number**.
4. Each change adds a `Changed Type` step to Applied Steps. If Power Query already auto-detected these types on import (it often does for clean numeric CSVs), you'll see an existing `Changed Type` step — just edit it (click the gear icon) to confirm Release Year is Whole Number and IMDb Rating is Decimal Number rather than adding a duplicate step.

---

## Task 4 — Keep Only the First Genre from the Comma-Separated Genre Column

Example: `Action, Thriller` → should become just `Action`.

**Steps:**
1. Select the **Genre** column.
2. **Home tab → Split Column → By Delimiter** (or **Transform tab → Split Column → By Delimiter**).
3. Delimiter: choose **Comma** (select from the dropdown, or "Custom" and type `,`).
4. Under **Split**, choose **"At the leftmost delimiter"** — this is the key setting: it splits the text into exactly 2 columns (first genre / everything else) instead of splitting at every comma into many ragged columns.
5. Click **OK**. Power Query creates two columns: `Genre.1` (e.g., `Action`) and `Genre.2` (e.g., ` Thriller`, ` Drama`).
6. **Delete `Genre.2`** (right-click its header → Remove), and **rename `Genre.1` back to `Genre`** (double-click the header).
7. This whole operation shows as a `Split Column by Delimiter` step (plus your manual rename/removal) in Applied Steps.

**Result:** `Action, Thriller` → `Action`; `Crime, Drama, Action` → `Crime`; single-genre rows like a hypothetical `Drama` stay unchanged (no comma = nothing to split).

---

## Task 5 — Load Cleaned Data Back to Excel & Verify

**Steps:**
1. In the Power Query Editor, click **Home tab → Close & Load** (or **Close & Load To…** if you want to choose "New Worksheet" explicitly, rather than the default which also creates a new sheet with a Table).
2. Excel creates a new worksheet with a live **Table** connected to your query — this is your cleaned dataset.
3. **Verify against `cleaned_movies_preview.xlsx`:**
   - Row count should be **23** (28 originals − 5 blank-rating rows).
   - **Genre** column shows only single genres (no commas remaining).
   - **Release Year** is right-aligned and whole numbers (no decimals).
   - **IMDb Rating** is right-aligned and shows one decimal place, no blanks.
4. To re-run this entire pipeline on a fresh/updated CSV later, just **right-click the query in the Queries & Connections pane → Refresh** — every Applied Step (filter blanks, change types, split column) replays automatically on the new data. This is the core benefit of Power Query over doing all this manually: it's a reusable, replayable recipe, not a one-time cleanup.

---

## Applied Steps Summary (what your Power Query Editor should show, top to bottom)

| Step | What it does |
|---|---|
| Source | Loads `trending_movies.csv` |
| Promoted Headers | Uses first row as column names |
| Changed Type | Auto-detected initial types |
| Filtered Rows | Removes rows where IMDb Rating is blank |
| Changed Type (edited) | Release Year → Whole Number, IMDb Rating → Decimal Number |
| Split Column by Delimiter | Splits Genre at the first comma |
| Removed Columns | Drops the leftover `Genre.2` column |
| Renamed Columns | `Genre.1` → `Genre` |

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | Get Data From Text/CSV → Transform Data | Data → Get Data → From File → From Text/CSV |
| 2 | Filter out blanks | Column filter dropdown → untick (blank), or Remove Empty |
| 3 | Change Data Type | Click type icon in column header |
| 4 | Split Column by Delimiter (leftmost) | Home/Transform → Split Column → By Delimiter |
| 5 | Close & Load, then Refresh to re-run | Home → Close & Load |
