# Session 2 – Cell Referencing, Named Ranges, Data Entry Rules
### Assignment Solutions

---

## Task 1: Food Delivery Apps — Rating Percentage (Absolute Referencing)

### Setup

| Cell | Content |
|---|---|
| E1 | Maximum Rating → `5` |
| A2:A6 | App Name |
| B2:B6 | Average Rating |
| C2:C6 | Rating Percentage (formula) |

### Sample Data

| App Name (A) | Avg. Rating (B) | Rating % (C) |
|---|---|---|
| Zomato | 4.2 | 84% |
| Swiggy | 4.3 | 86% |
| Uber Eats | 3.9 | 78% |
| Domino's | 4.1 | 82% |
| Foodpanda | 3.7 | 74% |

**Max Rating (E1) = 5**

### Formula (in C2, then dragged down to C6)
```
=B2/$E$1
```
- `B2` is a **relative reference** — it changes automatically to B3, B4, B5, B6 as the formula is copied down, so each row divides its own rating.
- `$E$1` is an **absolute reference** (locked with `$` before both the column and row) — it stays fixed on the Max Rating cell no matter where the formula is copied.

**Steps to lock the reference:** Click on cell E1 while typing the formula, then press **F4** — this automatically inserts the `$` signs (`$E$1`).

Format column C as **Percentage** (Home → Number Format → Percentage, or Ctrl+Shift+%) so 0.84 displays as 84%.

---

## Task 2: IPL Teams — Bonus Calculation (Mixed Referencing)

### Setup

| Cell | Content |
|---|---|
| D1 | Bonus Factor → `1.5` |
| A2:A7 | Team Name |
| B2:B7 | Total Wins |
| C2:C7 | Bonus Points (formula) |

### Sample Data

| Team (A) | Total Wins (B) | Bonus Points (C) |
|---|---|---|
| Chennai Super Kings | 130 | 195 |
| Mumbai Indians | 132 | 198 |
| Kolkata Knight Riders | 108 | 162 |
| Royal Challengers Bengaluru | 108 | 162 |
| Rajasthan Royals | 100 | 150 |
| Sunrisers Hyderabad | 88 | 132 |

**Bonus Factor (D1) = 1.5**

### Formula (in C2, then dragged down to C7)
```
=B2*$D$1
```
Since the Bonus Factor is a single fixed cell (like the Max Rating in Task 1), it is locked the same way with `$D$1`, while `B2` remains relative so each team's own win count is used.

### Why this is called "Mixed Referencing" here
Strictly, **mixed referencing** means locking *only the row* or *only the column* of a reference (e.g., `$B2` locks column B but lets the row change, or `B$2` locks row 2 but lets the column change) — as opposed to a **fully relative** (`B2`) or **fully absolute** (`$B$1`) reference.

**Example demonstrating true mixed referencing** for this same task — if the Bonus Factor were placed in row 1 across multiple bonus columns (say D1 = Bonus Type A, E1 = Bonus Type B) and Wins were always in column B for every row:
```
=$B2*D$1
```
- `$B2` → column B is locked (always pulls Wins), but the row changes as you drag **down**.
- `D$1` → row 1 is locked (always pulls the Bonus Factor), but the column changes as you drag **across** to E1, F1, etc.

This lets **one formula** be dragged both **down and across** and still return correct results — the defining use case of mixed references.

---

## Task 3: Named Range 'TopArtists' and COUNTA

### Step 1: Enter the Data
In A1:A5, enter your 5 favorite artists:

| Cell | Artist |
|---|---|
| A1 | Arijit Singh |
| A2 | Taylor Swift |
| A3 | The Weeknd |
| A4 | A.R. Rahman |
| A5 | Ed Sheeran |

### Step 2: Define the Named Range
1. Select **A1:A5**.
2. Go to the **Name Box** (top-left, next to the formula bar) and type: `TopArtists`
3. Press **Enter**.

*(Alternative method: **Formulas tab → Define Name → Name: TopArtists → Refers to: =Sheet1!$A$1:$A$5 → OK**)*

### Step 3: Count Artists Using the Named Range
In any other cell (e.g., B7):
```
=COUNTA(TopArtists)
```
**Result:** `5`

`COUNTA` counts all non-blank cells within the named range, so it correctly returns 5 for the five artist names.

---

## Task 4: Data Validation — Payment Method Dropdown

**Goal:** Restrict column B so users can only pick from UPI, Credit Card, Debit Card, Wallet, Net Banking.

### Steps
1. Select the range where transactions will be entered, e.g., **B2:B100**.
2. Go to **Data tab → Data Validation → Data Validation…**
3. In the **Settings** tab:
   - **Allow:** List
   - **Source:** `UPI,Credit Card,Debit Card,Wallet,Net Banking`
4. *(Optional but recommended)* Go to the **Input Message** tab → check "Show input message when cell is selected" → add a message like "Select a payment method."
5. *(Optional)* Go to the **Error Alert** tab → check "Show error alert after invalid data is entered" → Style: **Stop** → Error message: "Please select a valid payment method from the dropdown."
6. Click **OK**.

### Result
Every cell in B2:B100 now shows a small dropdown arrow. Clicking it displays:
```
UPI
Credit Card
Debit Card
Wallet
Net Banking
```
Typing anything outside this list triggers the error alert and blocks entry — exactly like the payment-method selector in Paytm.

### Sample Table

| Transaction ID (A) | Payment Method (B) | Amount (C) |
|---|---|---|
| TXN001 | UPI | 499 |
| TXN002 | Credit Card | 1299 |
| TXN003 | Wallet | 250 |
| TXN004 | Net Banking | 3000 |
| TXN005 | Debit Card | 875 |

---

## Task 5: Dynamic Named Range 'RecentMovies' + Validation

**Goal:** As new movie titles are added in column A, the named range should automatically expand — and the dropdown in column C should always reflect the current list.

### Step 1: Enter Initial Data
In A1:A5 (A1 can be a header "Movie Title", data starts A2):

| Cell | Movie |
|---|---|
| A1 | Movie Title *(header)* |
| A2 | Pathaan |
| A3 | Jawan |
| A4 | Animal |
| A5 | Fighter |

### Step 2: Create the Dynamic Named Range
Go to **Formulas → Define Name**:
- **Name:** `RecentMovies`
- **Refers to:**
```
=OFFSET(Sheet1!$A$2,0,0,COUNTA(Sheet1!$A$2:$A$1000)-COUNTA(Sheet1!$A$1)+1,1)
```

A simpler, commonly-taught version (assuming no header row, data starts at A1):
```
=OFFSET(Sheet1!$A$1,0,0,COUNTA(Sheet1!$A:$A),1)
```

**How it works:**
- `OFFSET($A$1,0,0,...)` starts the range at cell A1 (0 rows, 0 columns offset from the anchor).
- `COUNTA($A:$A)` dynamically counts how many non-blank cells exist in column A — this becomes the **height** of the range.
- `,1)` fixes the **width** to 1 column.
- As soon as a new movie is typed into the next empty row in column A, `COUNTA` increases by 1, and the named range automatically grows to include it — no manual editing needed.

### Step 3: Apply Data Validation Using the Dynamic Range
1. Select column C (e.g., **C2:C1000**) where users will rate/select a movie.
2. **Data tab → Data Validation → Allow: List**
3. In **Source**, type:
```
=RecentMovies
```
4. Click **OK**.

### Result
- The dropdown in column C always lists the **current, full set** of movies from column A — including any newly added titles — with no need to redefine the named range or the validation rule.
- This is the key difference from a **static named range** (Task 3's `TopArtists`), which stays locked to A1:A5 even if more artists are added below row 5.

### Sample Table

| Movie Title (A) | | Selected Movie (C) — dropdown from RecentMovies |
|---|---|---|
| Pathaan | | Jawan |
| Jawan | | Animal |
| Animal | | Pathaan |
| Fighter | | Fighter |
| *(new entry, e.g. Stree 2)* | | *(now also appears in dropdown automatically)* |

---
*End of Session 2 Assignment*
