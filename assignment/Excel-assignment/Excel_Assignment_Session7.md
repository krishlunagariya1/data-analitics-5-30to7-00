# Session 7 – Date & Time Functions
### Assignment Solutions

---

## Task 1: TODAY() and NOW() — Current Date and Time

### Formulas

| Cell | Formula | Purpose |
|---|---|---|
| A1 | `=TODAY()` | Returns the current **date** only (e.g., 08-08-2026) |
| A2 | `=NOW()` | Returns the current **date and time** together (e.g., 08-08-2026 14:35) |

### Sample Result

| Cell | Formula | Displayed Value |
|---|---|---|
| A1 | `=TODAY()` | 08-08-2026 |
| A2 | `=NOW()` | 08-08-2026 14:35:07 |

### Explanation
- `TODAY()` takes **no arguments** and returns just the date, formatted according to your system's regional date settings.
- `NOW()` also takes no arguments but returns both the date **and** the current time as a combined serial value (date + time-as-a-fraction-of-a-day).
- Both functions are **volatile** — they automatically recalculate and refresh every time the workbook recalculates (e.g., on opening the file or pressing F9), so they always show the current moment, not a fixed snapshot.

> **Tip:** If NOW() only shows a date, select the cell → **Format Cells (Ctrl+1) → Custom → `dd-mm-yyyy hh:mm:ss`** to reveal the time portion.

---

## Task 2: YEAR(), MONTH(), DAY() — Extracting Parts of a Birthday

### Sample Data (Column A)

| Friend Name (A) | Birthday (B) |
|---|---|
| Aarav | 15-03-1999 |
| Diya | 22-07-2000 |
| Kabir | 05-11-1998 |
| Meera | 30-01-2001 |
| Rohan | 18-09-1999 |

### Formulas (in C2, D2, E2 — dragged down)

| Column | Formula | Extracts |
|---|---|---|
| C (Year) | `=YEAR(B2)` | The 4-digit year |
| D (Month) | `=MONTH(B2)` | The month number (1–12) |
| E (Day) | `=DAY(B2)` | The day of the month (1–31) |

### Result

| Friend Name | Birthday (B) | Year (C) | Month (D) | Day (E) |
|---|---|---|---|---|
| Aarav | 15-03-1999 | 1999 | 3 | 15 |
| Diya | 22-07-2000 | 2000 | 7 | 22 |
| Kabir | 05-11-1998 | 1998 | 11 | 5 |
| Meera | 30-01-2001 | 2001 | 1 | 30 |
| Rohan | 18-09-1999 | 1999 | 9 | 18 |

> **Bonus – Employee Age:** Since the trainer coverage mentions calculating age, this can be done the same way with:
> `=DATEDIF(B2,TODAY(),"y")` → returns the completed number of years between the birthday and today, i.e., current age.

---

## Task 3: NETWORKDAYS — Working Days Between Match Date and Today

### Sample Data (Column A) — IPL match dates for the current season

| Match Date (A) | Working Days Until Today (B) |
|---|---|
| 22-03-2026 | *(formula)* |
| 05-04-2026 | *(formula)* |
| 19-04-2026 | *(formula)* |
| 03-05-2026 | *(formula)* |
| 17-05-2026 | *(formula)* |

### Formula (in B2, dragged down)
```
=NETWORKDAYS(A2,TODAY())
```

### Explanation
`NETWORKDAYS(start_date, end_date, [holidays])` counts the number of **working days** (Monday–Friday) between two dates, automatically **excluding Saturdays and Sundays**. The optional third argument (a list of holiday dates) is skipped here, per the task's instruction to ignore holidays.

### Sample Result *(assuming "today" = 08-08-2026)*

| Match Date (A) | Working Days Until Today (B) |
|---|---|
| 22-03-2026 | 100 |
| 05-04-2026 | 90 |
| 19-04-2026 | 79 |
| 03-05-2026 | 69 |
| 17-05-2026 | 58 |

> **Note:** If a match date happens to be after today (a future match), NETWORKDAYS still calculates correctly but will return a value based on start-to-end order — if start_date > end_date, the result is returned as a **negative number**, indicating the count runs backward. Swap the arguments to `=NETWORKDAYS(TODAY(),A2)` if you specifically want a positive count for future matches.

---

## Task 4: DATEDIF — Days Taken for Flipkart Delivery

### Sample Data

| Order Date (A) | Delivery Date (B) | Days Taken (C) |
|---|---|---|
| 01-08-2026 | 05-08-2026 | *(formula)* |
| 03-08-2026 | 04-08-2026 | *(formula)* |
| 10-07-2026 | 16-07-2026 | *(formula)* |
| 22-07-2026 | 29-07-2026 | *(formula)* |
| 28-07-2026 | 03-08-2026 | *(formula)* |

### Formula (in C2, dragged down)
```
=DATEDIF(A2,B2,"d")
```

### Explanation
`DATEDIF(start_date, end_date, unit)` calculates the difference between two dates. The `"d"` unit returns the difference in **complete days** — exactly the delivery duration needed here.

### Result

| Order Date (A) | Delivery Date (B) | Days Taken (C) |
|---|---|---|
| 01-08-2026 | 05-08-2026 | 4 |
| 03-08-2026 | 04-08-2026 | 1 |
| 10-07-2026 | 16-07-2026 | 6 |
| 22-07-2026 | 29-07-2026 | 7 |
| 28-07-2026 | 03-08-2026 | 6 |

> **Note:** For simple day-count differences like this, `=B2-A2` (plain subtraction) would give the same numeric result, since both dates are stored as date serial numbers. `DATEDIF` becomes essential for the more complex year/month calculations shown in Task 5, which is why it's the function taught here.

---

## Task 5: EOMONTH + DATEDIF — Months Since Spotify Signup

### Setup

| Cell | Content |
|---|---|
| A1 | Spotify Signup Date → `12-02-2022` |
| A2 | Last day of current month → `=EOMONTH(TODAY(),0)` |
| A3 | Total months since signup → `=DATEDIF(A1,A2,"m")` |

### Step 1: Find the Last Day of the Current Month
```
=EOMONTH(TODAY(),0)
```
`EOMONTH(start_date, months)` returns the last day of the month that is `months` away from `start_date`. Using `0` means "the current month," so this returns the last calendar date of the month `TODAY()` falls in (e.g., 31-08-2026 if today is in August).

### Step 2: Calculate Total Months Since Signup
```
=DATEDIF(A1,A2,"m")
```
The `"m"` unit tells `DATEDIF` to return the number of **complete months** between the signup date (A1) and the end-of-month reference date (A2) — rather than just complete years or days.

### Sample Result *(assuming today = 08-08-2026, signup = 12-02-2022)*

| Cell | Formula | Value |
|---|---|---|
| A1 | Signup Date | 12-02-2022 |
| A2 | `=EOMONTH(TODAY(),0)` | 31-08-2026 |
| A3 | `=DATEDIF(A1,A2,"m")` | 54 |

**Interpretation:** You have been using Spotify for **54 complete months** as of the end of the current month.

> **Why use EOMONTH instead of just TODAY() directly?** Anchoring to the *end* of the current month (rather than today's exact date) gives a cleaner, more standard "as of this month" figure — useful for monthly subscription/usage reports where partial-month precision isn't needed, and it avoids the count changing every single day within the same month.

---
*End of Session 7 Assignment*
