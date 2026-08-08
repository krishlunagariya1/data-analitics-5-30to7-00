# Session 18 – Power Query (Merging & Appending)
## Solved Assignment

**Files used (all attached alongside this document):**

| File | Used for | Columns |
|---|---|---|
| `restaurants.csv` | Task 1 | RestaurantID, Name, City |
| `orders.csv` | Tasks 1 & 4 | OrderID, RestaurantID, OrderAmount *(2 rows reference a RestaurantID that doesn't exist in `restaurants.csv`, and 1 row has a blank OrderAmount — built in on purpose so Task 4's null-cleanup has something real to fix)* |
| `orders_last_month.csv` | Task 2 | OrderID, UserID, Amount, Date (June 2025) |
| `orders_this_month.csv` | Task 2 | OrderID, UserID, Amount, Date (July 2025) |
| `flipkart_products.csv` | Task 3 | ProductID, Name, Category, Price *(no Discount column)* |
| `myntra_products.csv` | Task 3 | ProductID, Name, Category, Price, Discount |

---

## Task 1 — Merge Restaurants + Orders on RestaurantID

**Steps:**
1. **Data tab → Get Data → From File → From Text/CSV** → import `restaurants.csv` → **Transform Data** (opens Power Query Editor, query named `restaurants`).
2. Repeat: **Get Data → From Text/CSV** → import `orders.csv` → **Transform Data** (query named `orders`).
3. With the `orders` query selected, go to **Home tab → Combine → Merge Queries** (this is the JOIN equivalent).
4. In the Merge dialog:
   - Top table: `orders`, click the **RestaurantID** column to select it as the join key.
   - Bottom table dropdown: choose `restaurants`, click its **RestaurantID** column too.
   - **Join Kind: Left Outer** (keeps every order, even ones whose restaurant doesn't match — this matters for Task 4).
5. Click **OK**. A new column appears containing a nested table icon — click the **expand icon (⇄)** on that column's header, untick RestaurantID (already have it) and City if you don't need it yet, keep **Name** → **OK**.
6. Rename the expanded `Name` column to **Restaurant Name**.

**Result:** every order row now shows its restaurant's name directly next to the OrderAmount — e.g. OrderID 9001 → "Burger King", OrderID 9006 → "Pizza Hut". OrderIDs 9005 and 9009 (which reference RestaurantIDs 108/109 that don't exist in `restaurants.csv`) will show **null** in Restaurant Name — that's expected and exactly what Task 4 asks you to clean up.

---

## Task 2 — Append Last Month's Orders + This Month's Orders

**Steps:**
1. Import both `orders_last_month.csv` and `orders_this_month.csv` as separate queries (same **Get Data → From Text/CSV → Transform Data** flow as above).
2. With either query selected → **Home tab → Combine → Append Queries** (choose **"Append Queries as New"** so you keep the two originals intact and get a clean third combined query — better practice than overwriting one of them).
3. In the dialog: **Primary table** = `orders_last_month`, **Table to append** = `orders_this_month` → **OK**.
4. Since both source tables have **identical column names and order** (OrderID, UserID, Amount, Date), Power Query stacks them directly with no mismatch handling needed.
5. Rename the new combined query to **`AllOrders`**.

**Result:** `AllOrders` contains all 10 rows (5 from June + 5 from July), one continuous list — this is a stacking operation (rows added), unlike Merge which adds columns.

---

## Task 3 — Append Flipkart + Myntra Products (Mismatched Columns)

`FlipkartProducts` has **4 columns** (no Discount); `MyntraProducts` has **5 columns** (includes Discount).

**Steps:**
1. Import `flipkart_products.csv` and `myntra_products.csv` as two separate queries.
2. Select one → **Home → Combine → Append Queries as New** → Primary = `flipkart_products`, Append = `myntra_products` → **OK**.
3. Power Query **automatically aligns columns by name** (ProductID→ProductID, Name→Name, Category→Category, Price→Price) and, per the hint, **creates a Discount column with `null` for every Flipkart row**, since Flipkart's source data never had that column.
4. **Check for nulls:** select the **Discount** column → the filter dropdown or the column quality indicators (View tab → Column Quality) will show the 4 Flipkart rows as null/empty, while the 4 Myntra rows show their real discount %.
5. This confirms **no data was lost** — every row from both platforms is present, and the schema mismatch (Flipkart missing a column Myntra has) was resolved by nulling it out rather than dropping rows or erroring.

**Result table shape:**

| ProductID | Name | Category | Price | Discount |
|---|---|---|---|---|
| F001 | Running Shoes | Footwear | 1999 | **null** |
| F002 | Cotton T-Shirt | Apparel | 499 | **null** |
| M001 | Denim Jacket | Apparel | 2999 | 20% |
| M002 | Sneakers | Footwear | 2499 | 15% |

*(You could optionally follow up with Task 4's technique to replace these Discount nulls with `"0%"` or `"No Discount"` — same Replace Values approach, just applied to this table instead.)*

---

## Task 4 — Clean Nulls in the Merged Table (Task 1's output)

In the merged `orders` table from Task 1, two problems exist:
- **Restaurant Name** is null for OrderIDs 9005 and 9009 (RestaurantID didn't match any restaurant).
- **OrderAmount** is null/blank for OrderID 9010 (missing in the source data).

**Steps — Restaurant Name nulls → "Unknown":**
1. Right-click the **Restaurant Name** column header → **Replace Values**.
2. **Value To Find:** leave blank, but check "null" handling — Power Query's Replace Values dialog doesn't directly type "null" as text; instead:
   - Right-click column → **Replace Errors** is for error values, not nulls, so for nulls use: select the column → **Transform tab → Replace Values**, Value to Find = `null` (Power Query does accept typing `null` in this box, matching actual null cells) → Replace With = `Unknown` → **OK**.
   - Alternative, more reliable method: **Transform tab → Fill → Down/Up** does NOT apply here (that's for filling repeated headers); for nulls specifically, the cleanest approach is to add a **Conditional Column** or use the formula bar directly on the step:
     ```
     = Table.ReplaceValue(PreviousStepName, null, "Unknown", Replacer.ReplaceValue, {"Restaurant Name"})
     ```
     Power Query generates exactly this M code automatically when you use the Replace Values dialog on that column with "null" typed into Value To Find — you don't need to write it by hand, just know this is what's happening under the hood.

**Steps — OrderAmount nulls → 0:**
1. Select the **OrderAmount** column → **Transform tab → Replace Values**.
2. Value To Find: `null` → Replace With: `0` → **OK**.
3. Make sure OrderAmount's data type is still **Whole Number/Decimal Number** after this (Replace Values can sometimes need a follow-up **Changed Type** step if the column reverted to Any/Text).

**Result after cleanup:**

| OrderID | RestaurantID | Restaurant Name | OrderAmount |
|---|---|---|---|
| 9005 | 108 | **Unknown** | 299 |
| 9009 | 109 | **Unknown** | 675 |
| 9010 | 101 | Burger King | **0** |

4. Finish with **Home tab → Close & Load** to push the fully merged, appended, and null-cleaned table into a new Excel worksheet.

---

## Summary Table

| Task | Feature Used | Key Location in Ribbon |
|---|---|---|
| 1 | Merge Queries (Left Outer Join) on RestaurantID | Home → Combine → Merge Queries |
| 2 | Append Queries (identical schema) | Home → Combine → Append Queries |
| 3 | Append Queries (mismatched schema → auto-null) | Home → Combine → Append Queries; check Column Quality |
| 4 | Replace Values (null → "Unknown" / 0) | Transform tab → Replace Values |
