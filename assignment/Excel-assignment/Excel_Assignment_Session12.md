# Session 12 – Conditional Formatting
### Assignment Solutions

---

## Task 1: Highlight Duplicate Song Names in Yellow

### Sample Data (20 rows, Column A = Song Name, Column B = Artist)

| Song Name (A) | Artist (B) |
|---|---|
| Kesariya | Arijit Singh |
| Blinding Lights | The Weeknd |
| Apna Bana Le | Arijit Singh |
| Levitating | Dua Lipa |
| Kesariya | Arijit Singh *(duplicate — remix version logged again)* |
| Shape of You | Ed Sheeran |
| Tum Hi Ho | Arijit Singh |
| Paint The Town Red | Doja Cat |
| Save Your Tears | The Weeknd |
| Chaiyya Chaiyya | Sukhwinder Singh |
| Blinding Lights | The Weeknd *(duplicate)* |
| Zara Zara | Bombay Jayashri |
| As It Was | Harry Styles |
| Perfect | Ed Sheeran |
| Tum Hi Ho | Arijit Singh *(duplicate)* |
| Flowers | Miley Cyrus |
| Vampire | Olivia Rodrigo |
| Anti-Hero | Taylor Swift |
| Chaiyya Chaiyya | Sukhwinder Singh *(duplicate)* |
| Espresso | Sabrina Carpenter |

### Steps
1. Select the range **A2:A21** (Song Name column only — not Artist, since we're checking duplicates by song title).
2. Go to **Home tab → Conditional Formatting → Highlight Cells Rules → Duplicate Values…**
3. In the dialog, keep it set to **"Duplicate"** (as opposed to "Unique").
4. Choose a formatting style — select **"Yellow Fill with Dark Yellow Text"** from the dropdown (or click **Custom Format** to pick your own yellow fill).
5. Click **OK**.

### Result
Every occurrence of **Kesariya**, **Blinding Lights**, **Tum Hi Ho**, and **Chaiyya Chaiyya** (all rows where the song name appears more than once) is automatically highlighted in yellow — including the *first* occurrence, since Excel's Duplicate Values rule flags **all** instances of a repeated value, not just the second one onward.

---

## Task 2: Color Scale for Flipkart Product Prices

### Sample Data (Column A = Product, Column B = Price)

| Product (A) | Price (B) |
|---|---|
| Wireless Earbuds | 1499 |
| Smartwatch | 2999 |
| Bluetooth Speaker | 1299 |
| Power Bank | 899 |
| Laptop Bag | 799 |
| Gaming Mouse | 999 |
| LED Desk Lamp | 649 |
| Phone Cover | 249 |
| Fitness Band | 1799 |
| Wired Headphones | 449 |

### Steps
1. Select the price range **B2:B11**.
2. Go to **Home tab → Conditional Formatting → Color Scales**.
3. Choose the **"Green – Yellow – Red Color Scale"** option (or hover to find the specific 3-color scale showing green on top, red on bottom — some Excel versions list it as "Green-White-Red" or a custom-built one).
4. If the direction is reversed (red = highest instead of green = highest), click **Conditional Formatting → Manage Rules → Edit Rule**, and under "Format Style," swap the **Minimum** color to Red and **Maximum** color to Green.

### Result
- **Smartwatch (2999)** — the highest price — shades **dark green**.
- **Phone Cover (249)** — the lowest price — shades **red**.
- All other prices fall on a smooth gradient between the two, based on where their value sits relative to the min/max of the selected range.

> **How it works internally:** Excel calculates each cell's price as a percentile position between the selected range's minimum and maximum, then blends the two end colors proportionally — no manual thresholds needed, unlike Icon Sets or standard color rules.

---

## Task 3: Traffic Light Icon Set for Zomato Order Ratings

### Sample Data (15 orders)

| Order (A) | Rating (B) |
|---|---|
| Order 1 | 4.5 |
| Order 2 | 2.8 |
| Order 3 | 3.2 |
| Order 4 | 5.0 |
| Order 5 | 1.9 |
| Order 6 | 4.0 |
| Order 7 | 3.5 |
| Order 8 | 2.5 |
| Order 9 | 4.8 |
| Order 10 | 3.0 |
| Order 11 | 2.2 |
| Order 12 | 4.2 |
| Order 13 | 3.8 |
| Order 14 | 1.5 |
| Order 15 | 4.6 |

### Steps
1. Select the Rating range **B2:B16**.
2. Go to **Home tab → Conditional Formatting → Icon Sets → 3 Traffic Lights (Unrimmed or Rimmed)**.
3. By default, Excel divides icons into thirds automatically — to match the task's exact thresholds, click **Conditional Formatting → Manage Rules → Edit Rule**, and set custom values:
   - 🟢 **Green icon:** when value is **≥ 4** (Type: Number, Value: 4, Operator: `>=`)
   - 🟡 **Yellow icon:** when value is **≥ 3** and **< 4** (Excel auto-fills this as the "else" band between your green and red thresholds)
   - 🔴 **Red icon:** when value is **< 3** (this becomes the default lowest band)
4. Click **OK**.

### Result

| Order | Rating | Icon |
|---|---|---|
| Order 1 | 4.5 | 🟢 |
| Order 2 | 2.8 | 🔴 |
| Order 3 | 3.2 | 🟡 |
| Order 4 | 5.0 | 🟢 |
| Order 5 | 1.9 | 🔴 |
| Order 6 | 4.0 | 🟢 |
| Order 7 | 3.5 | 🟡 |
| Order 8 | 2.5 | 🔴 |
| Order 9 | 4.8 | 🟢 |
| Order 10 | 3.0 | 🟡 |
| Order 11 | 2.2 | 🔴 |
| Order 12 | 4.2 | 🟢 |
| Order 13 | 3.8 | 🟡 |
| Order 14 | 1.5 | 🔴 |
| Order 15 | 4.6 | 🟢 |

---

## Task 4: Highlight Top 3 and Bottom 3 IPL Run-Scorers

### Sample Data (Column A = Player, Column B = Total Runs)

| Player (A) | Total Runs (B) |
|---|---|
| Virat Kohli | 1250 |
| Rohit Sharma | 980 |
| Shubman Gill | 1100 |
| Rinku Singh | 420 |
| Suryakumar Yadav | 890 |
| KL Rahul | 1050 |
| Ravindra Jadeja | 380 |
| Hardik Pandya | 650 |
| Jos Buttler | 1180 |
| Yashasvi Jaiswal | 310 |

### Step 1: Highlight Top 3 in Blue
1. Select **B2:B11**.
2. **Home tab → Conditional Formatting → Top/Bottom Rules → Top 10 Items…**
3. Change the number from 10 to **3**.
4. Set the format to a **custom Blue Fill** (click the dropdown → Custom Format → choose blue fill color) → **OK**.

### Step 2: Highlight Bottom 3 in Orange
1. Select **B2:B11** again (same range — a second rule stacks on top of the first).
2. **Home tab → Conditional Formatting → Top/Bottom Rules → Bottom 10 Items…**
3. Change the number from 10 to **3**.
4. Set the format to a **custom Orange Fill** → **OK**.

### Result

| Player | Total Runs | Highlight |
|---|---|---|
| Virat Kohli | 1250 | 🔵 Blue (Top 3) |
| Rohit Sharma | 980 | — |
| Shubman Gill | 1100 | 🔵 Blue (Top 3) |
| Rinku Singh | 420 | 🟠 Orange (Bottom 3) |
| Suryakumar Yadav | 890 | — |
| KL Rahul | 1050 | — |
| Ravindra Jadeja | 380 | 🟠 Orange (Bottom 3) |
| Hardik Pandya | 650 | — |
| Jos Buttler | 1180 | 🔵 Blue (Top 3) |
| Yashasvi Jaiswal | 310 | 🟠 Orange (Bottom 3) |

> **Note:** Both rules can coexist on the same range simultaneously without conflict, since "Top 3" and "Bottom 3" values don't overlap (assuming more than 6 total rows) — Excel evaluates each Conditional Formatting rule independently and applies whichever one's condition a cell satisfies.

---

## Task 5: Expenses vs Target — Green (Under) / Red (Over)

**Constraint followed:** This uses **expenses vs. target** (not the trainer's revenue example) — and note the color logic is intentionally the *opposite* meaning of a typical revenue rule: here, **green = good = spent LESS than target**, and **red = bad = spent MORE than target** (whereas for revenue, higher is usually the "good"/green outcome). This is exactly why the same green/red concept needs a different formula depending on context.

### Sample Data

| App/Service (A) | Monthly Expense (B) | Target Budget (C) |
|---|---|---|
| Swiggy | 2400 | 2000 |
| Myntra | 1500 | 2500 |
| Paytm (Bills) | 3200 | 3000 |
| Zomato | 1800 | 2000 |
| Amazon | 4500 | 4000 |
| Netflix + Spotify | 800 | 1000 |

### Steps
1. Select the **Monthly Expense** range, **B2:B7**.
2. **Home tab → Conditional Formatting → New Rule…**
3. Choose **"Use a formula to determine which cells to format."**
4. **Rule 1 — Green (Under Target):**
```
=B2<C2
```
   Set format → Fill color: **Green**.
5. Click **New Rule** again for **Rule 2 — Red (Over Target):**
```
=B2>C2
```
   Set format → Fill color: **Red**.
6. Click **OK** on both, then **Apply**.

### Explanation
Unlike the built-in "greater than / less than" quick rules (which only compare a cell to a **fixed number**), this uses a **formula-based rule** to compare each expense cell **dynamically to its own row's target** in column C — this is essential here since every app has a *different* target budget, not one single threshold for the whole list.

### Result

| App/Service | Monthly Expense | Target Budget | Color |
|---|---|---|---|
| Swiggy | 2400 | 2000 | 🔴 Red (over budget) |
| Myntra | 1500 | 2500 | 🟢 Green (under budget) |
| Paytm (Bills) | 3200 | 3000 | 🔴 Red (over budget) |
| Zomato | 1800 | 2000 | 🟢 Green (under budget) |
| Amazon | 4500 | 4000 | 🔴 Red (over budget) |
| Netflix + Spotify | 800 | 1000 | 🟢 Green (under budget) |

---
*End of Session 12 Assignment*
