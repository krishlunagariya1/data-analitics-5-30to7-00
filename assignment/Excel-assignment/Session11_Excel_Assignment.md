# Session 11 – Advanced Lookup: INDEX-MATCH & MATCH-MATCH
### Assignment Solutions

---

## Task 1: INDEX + MATCH — IPL Score for 'Gujarat Titans' on '2024-04-15'

### Sample Data (Teams as Rows, Match Dates as Columns — A1:E6)

| Team (A) | 2024-04-05 (B) | 2024-04-10 (C) | 2024-04-15 (D) | 2024-04-20 (E) |
|---|---|---|---|---|
| Mumbai Indians | 178 | 165 | 190 | 172 |
| Chennai Super Kings | 210 | 188 | 175 | 195 |
| Gujarat Titans | 165 | 200 | 182 | 210 |
| Royal Challengers Bengaluru | 195 | 170 | 205 | 188 |
| Kolkata Knight Riders | 180 | 192 | 168 | 175 |

### Search Setup

| Cell | Content |
|---|---|
| G1 | Team → `Gujarat Titans` |
| G2 | Match Date → `2024-04-15` |
| G3 | Score Result → formula |

### Formula (in G3)
```
=INDEX(B2:E6,MATCH(G1,A2:A6,0),MATCH(G2,B1:E1,0))
```

### Explanation — How the Two MATCH Calls Work Together
- `INDEX(array, row_num, column_num)` returns the value at the intersection of a specific row and column within a range.
- **First MATCH** — `MATCH(G1,A2:A6,0)` — searches for "Gujarat Titans" down column A and returns its **row position** within that range (row 3, since Gujarat Titans is the 3rd team listed).
- **Second MATCH** — `MATCH(G2,B1:E1,0)` — searches for "2024-04-15" across row 1 (the date headers) and returns its **column position** within that range (column 3, since 15-Apr is the 3rd date column).
- `INDEX(B2:E6, 3, 3)` then returns the value sitting at the 3rd row, 3rd column of the data block — the intersection of Gujarat Titans and 15-Apr.

### Result
**G3 = 182** (Gujarat Titans' score on 2024-04-15)

---

## Task 2: INDEX + MATCH-MATCH — iPhone 15 Price in Ahmedabad

### Sample Data (Products as Rows, Cities as Columns — A1:E6)

| Product (A) | Mumbai (B) | Delhi (C) | Ahmedabad (D) | Bengaluru (E) |
|---|---|---|---|---|
| iPhone 15 | 79999 | 80499 | 79499 | 80999 |
| Galaxy S24 | 74999 | 75499 | 74499 | 75999 |
| OnePlus 12 | 64999 | 65499 | 64499 | 65999 |
| Pixel 8 | 69999 | 70499 | 69499 | 70999 |
| Redmi Note 13 | 21999 | 22499 | 21499 | 22999 |

### Search Setup

| Cell | Content |
|---|---|
| G1 | Product → `iPhone 15` |
| G2 | City → `Ahmedabad` |
| G3 | Price Result → formula |

### Formula (in G3)
```
=INDEX(B2:E6,MATCH(G1,A2:A6,0),MATCH(G2,B1:E1,0))
```

### Explanation
Same two-way lookup pattern as Task 1:
- `MATCH(G1,A2:A6,0)` finds that "iPhone 15" is in **row 1** of the product list.
- `MATCH(G2,B1:E1,0)` finds that "Ahmedabad" is in **column 3** of the city headers.
- `INDEX(B2:E6,1,3)` returns the value at that exact intersection.

### Result
**G3 = 79499** (iPhone 15's price in Ahmedabad)

---

## Task 3: Two-Way Lookup — 'Kesariya' Plays in 'March'

### Sample Data (Songs as Rows, Months as Columns — A1:E6)

| Song Name (A) | January (B) | February (C) | March (D) | April (E) |
|---|---|---|---|---|
| Kesariya | 120 | 145 | 210 | 180 |
| Apna Bana Le | 95 | 110 | 130 | 105 |
| Tum Hi Ho | 200 | 190 | 175 | 160 |
| Chaiyya Chaiyya | 60 | 75 | 90 | 70 |
| Zara Zara | 140 | 130 | 150 | 125 |

### Search Setup

| Cell | Content |
|---|---|
| G1 | Song Name → `Kesariya` |
| G2 | Month → `March` |
| G3 | Play Count Result → formula |

### Formula (in G3)
```
=INDEX(B2:E6,MATCH(G1,A2:A6,0),MATCH(G2,B1:E1,0))
```

### Explanation (as per the hint — MATCH provides both coordinates for INDEX)
- `MATCH(G1,A2:A6,0)` → finds "Kesariya" is in **row 1** of the song list.
- `MATCH(G2,B1:E1,0)` → finds "March" is in **column 3** of the month headers.
- `INDEX(B2:E6,1,3)` → returns the value at row 1, column 3 of the data block.

### Result
**G3 = 210** (Kesariya was played 210 times in March)

---

## Task 4: Fixing VLOOKUP's Column-Order Failure — Zomato Sales (Burger Hub, Friday)

### The Problem with VLOOKUP Here

### Sample Data (Restaurants as Rows, Weekdays as Columns — A1:G6)

| Restaurant (A) | Monday (B) | Tuesday (C) | Wednesday (D) | Thursday (E) | Friday (F) | Saturday (G) |
|---|---|---|---|---|---|---|
| Domino's | 12000 | 11500 | 13000 | 14500 | 18000 | 21000 |
| Burger Hub | 9500 | 9800 | 10200 | 11000 | 15500 | 17800 |
| Pizza Corner | 8700 | 8900 | 9100 | 9600 | 13200 | 15900 |
| Wow Momo | 6200 | 6500 | 6800 | 7100 | 9900 | 11500 |
| Behrouz Biryani | 15000 | 14200 | 15800 | 16900 | 21000 | 24500 |

**Why VLOOKUP fails here:** A formula like `=VLOOKUP(G1,A2:G6,6,FALSE)` hard-codes column index `6` assuming Friday is always the 6th column. If someone later **rearranges the weekday columns** (e.g., reorders them, inserts a "Sunday" column, or moves "Friday" earlier for a different regional report layout), the column index number no longer points to Friday — it silently pulls sales from whatever column now sits in position 6, giving a **wrong number without any error message**. VLOOKUP has no awareness of which column header it's actually returning from; it only counts positions.

### Fixed Formula Using INDEX + MATCH

### Search Setup

| Cell | Content |
|---|---|
| I1 | Restaurant → `Burger Hub` |
| I2 | Weekday → `Friday` |
| I3 | Sales Result → formula |

### Formula (in I3)
```
=INDEX(B2:G6,MATCH(I1,A2:A6,0),MATCH(I2,B1:G1,0))
```

### Explanation — Why This Fixes the Limitation
Instead of a fixed column **number**, this formula uses `MATCH(I2,B1:G1,0)` to **dynamically find** wherever "Friday" currently sits among the weekday headers. If the columns are later reordered — say Friday moves from position 6 to position 2 — `MATCH` automatically returns the new correct position (2) instead of the old one, so `INDEX` always pulls from the right column **regardless of how the table is rearranged**. The formula becomes self-correcting because it looks up the *header text*, not a hard-coded position.

### Result
**I3 = 15500** (Burger Hub's Friday sales)

### Summary Comparison

| Aspect | VLOOKUP (column index) | INDEX + MATCH (dynamic) |
|---|---|---|
| Column reference | Fixed number (e.g., `6`) | Found dynamically via header name |
| Breaks if columns reordered? | **Yes** — silently returns wrong data | **No** — automatically re-locates the correct column |
| Can look left of lookup column? | No | Yes |
| Best used for | Simple, static, single-direction tables | Tables that change structure, or need two-way (row+column) lookups |

---
*End of Session 11 Assignment*
