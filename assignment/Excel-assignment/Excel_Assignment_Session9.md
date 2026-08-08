# Session 9 – Lookup Functions (Part 1)
### Assignment Solutions

---

## Task 1: VLOOKUP — Find Flipkart Product Price by Name

### Sample Data (Product Table — A1:B11)

| Product Name (A) | Price (B) |
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

### Search Setup

| Cell | Content |
|---|---|
| D1 | Search Product → (user types a product name here, e.g., `Smartwatch`) |
| D2 | Price Result → formula |

### Formula (in D2)
```
=VLOOKUP(D1,A2:B11,2,FALSE)
```

### Explanation
`VLOOKUP(lookup_value, table_array, col_index_num, [range_lookup])`:
- `D1` — the product name typed by the user.
- `A2:B11` — the table range to search within (lookup column must be the **first** column of this range).
- `2` — return the value from the **2nd column** of the range (Price).
- `FALSE` — forces an **exact match**; if the name isn't found exactly as typed, it returns `#N/A` instead of guessing.

### Sample Result
If **D1 = "Smartwatch"**, then **D2 = 2999**.
If **D1 = "Power Bank"**, then **D2 = 899**.

---

## Task 2: HLOOKUP — Zomato Dish Ratings (Horizontal Layout)

### Sample Data (Menu Table — laid out horizontally, A1:H2)

| | A | B | C | D | E | F | G | H |
|---|---|---|---|---|---|---|---|---|
| **Row 1 (Dish)** | Paneer Tikka | Butter Chicken | Veg Biryani | Masala Dosa | Chole Bhature | Fish Curry | Paneer Roll | Dal Makhani |
| **Row 2 (Rating)** | 4.5 | 4.7 | 4.3 | 4.6 | 4.2 | 4.4 | 4.1 | 4.8 |

### Search Setup

| Cell | Content |
|---|---|
| A4 | Search Dish → (e.g., `Butter Chicken`) |
| A5 | Rating Result → formula |

### Formula (in A5)
```
=HLOOKUP(A4,A1:H2,2,FALSE)
```

### Explanation
`HLOOKUP(lookup_value, table_array, row_index_num, [range_lookup])` works exactly like VLOOKUP but searches **across a row** instead of down a column:
- `A4` — the dish name to search for.
- `A1:H2` — the table, where the lookup values sit in the **first row**.
- `2` — return the value from the **2nd row** of the range (Rating).
- `FALSE` — exact match only.

### Sample Result
If **A4 = "Butter Chicken"**, then **A5 = 4.7**.
If **A4 = "Dal Makhani"**, then **A5 = 4.8**.

---

## Task 3: VLOOKUP with Approximate Match (range_lookup = TRUE)

### Sample Data (Instagram Users Table — A1:B13)

| Username (A) | Mobile Number (B) |
|---|---|
| ananya_r | 9876543210 |
| dev.patel | 9123456780 |
| isha_verma | 9988776655 |
| karan_shah | 9765432109 |
| meera_j | 9654321098 |
| nikhil.k | 9543210987 |
| priya_sharma | 9432109876 |
| rohan_mehta | 9321098765 |
| sneha_r | 9210987654 |
| tanvi_desai | 9109876543 |
| vikram_singh | 9098765432 |
| zara_khan | 8987654321 |

> **Important pre-requisite for approximate match:** For `TRUE` (approximate match) to behave meaningfully, the lookup column **must be sorted in ascending order** — which the usernames above already are, alphabetically.

### Formula
```
=VLOOKUP(D1,A2:B13,2,TRUE)
```

### Experiment: Searching for a Name Not Exactly in the List

**Test 1 — Misspelled name:** D1 = `"karan_shaah"` (extra "a")
- **Result:** Instead of an error, VLOOKUP returns the mobile number for **`karan_shah`** — **9765432109** — even though the spelling doesn't match exactly.

**Test 2 — Partial/non-existent name:** D1 = `"priya_s"`
- **Result:** VLOOKUP returns the number for **`priya_sharma`** — **9432109876** — because it's the closest match that is **less than or equal to** the search term in sort order.

### Explanation — What's Actually Happening
When `range_lookup = TRUE`, VLOOKUP does **not** look for an exact text match at all. Instead, it scans the sorted lookup column and returns the value associated with the **largest entry that is less than or equal to** the search term (based on alphabetical/numeric sort order) — it silently accepts a "closest match" rather than throwing `#N/A`.

**This is risky for text data like usernames**, because:
- A typo or partial name will still return *a* result — with no warning that it isn't a true match.
- If the list isn't properly sorted, results become unpredictable and can return completely wrong data.
- Approximate match is really designed for **numeric range lookups** (e.g., tax slabs, grading bands like `IF(Marks>=90,"A"...)` equivalents), not for looking up unique text identifiers like usernames or names.

**Best practice:** For text/exact-identifier lookups (names, IDs, usernames), **always use `FALSE`** for range_lookup so Excel returns a clear `#N/A` error when no exact match exists — this is far safer than silently returning the wrong person's data.

---

## Task 4: Demonstrating VLOOKUP's Leftmost-Column Limitation

### Step 1: Modify the Product Table from Task 1
Insert a new **'Discount'** column **before** 'Product Name', so the table now looks like:

| Discount (A) | Product Name (B) | Price (C) |
|---|---|---|
| 10% | Wireless Earbuds | 1499 |
| 15% | Smartwatch | 2999 |
| 5% | Bluetooth Speaker | 1299 |
| 20% | Power Bank | 899 |
| 10% | Laptop Bag | 799 |
| 5% | Gaming Mouse | 999 |
| 15% | LED Desk Lamp | 649 |
| 10% | Phone Cover | 249 |
| 20% | Fitness Band | 1799 |
| 5% | Wired Headphones | 449 |

### Step 2: Attempt the Same VLOOKUP Formula
```
=VLOOKUP(D1,A2:C11,3,FALSE)
```
*(Adjusted column index to `3` since Price is now the 3rd column — but note this is exactly the problem being demonstrated.)*

### What Goes Wrong
VLOOKUP **always searches for the lookup_value only in the first (leftmost) column** of the given range — here, column A (Discount) — **not** column B (Product Name), regardless of which column index you specify for the return value.

- If D1 contains a **product name** (e.g., "Smartwatch") but VLOOKUP is scanning column A (Discount values like "10%", "15%"), it will **never find a match**, because product names don't exist in column A at all.
- **Result:** `#N/A` error — every single time — no matter what valid product name is typed in D1.

### Why This Happens (VLOOKUP's Core Limitation)
> **VLOOKUP can only look up values that appear in the leftmost column of its table_array, and can only return values from columns to the right of it. It cannot look leftward.**

This is precisely why adding the Discount column *before* Product Name broke the formula — the function has no way to search column B while starting its scan from column A.

### How to Fix It (Two Standard Solutions)

**Option A — Rearrange columns:** Move 'Product Name' back to be the leftmost column, with 'Discount' placed after it.

**Option B — Use INDEX+MATCH instead** *(the modern, more flexible alternative — not limited by column order)*:
```
=INDEX(C2:C11,MATCH(D1,B2:B11,0))
```
This looks up the product name in column B (regardless of its position) and returns the corresponding value from column C, working equally well whether Discount is to the left or right of Product Name.

*(Note: INDEX+MATCH and XLOOKUP are typically covered as VLOOKUP's replacement in a later session — mentioned here only to illustrate the fix for this specific limitation.)*

---
*End of Session 9 Assignment*
