# Session 10 – Modern Lookup Functions (XLOOKUP)
### Assignment Solutions

---

## Task 1: XLOOKUP — Fetch Product Name by Product ID

### Sample Data (Main Product Table — A1:D11)

| Product ID (A) | Name (B) | Category (C) | Price (D) |
|---|---|---|---|
| P101 | Wireless Earbuds | Electronics | 1499 |
| P102 | Smartwatch | Electronics | 2999 |
| P103 | Bluetooth Speaker | Electronics | 1299 |
| P104 | Power Bank | Electronics | 899 |
| P105 | Laptop Bag | Accessories | 799 |
| P106 | Gaming Mouse | Electronics | 999 |
| P107 | LED Desk Lamp | Home | 649 |
| P108 | Phone Cover | Accessories | 249 |
| P109 | Fitness Band | Electronics | 1799 |
| P110 | Wired Headphones | Electronics | 449 |

### Search Table (Column F — Product IDs to look up)

| Product ID (F) | Product Name (G) |
|---|---|
| P103 | *(formula)* |
| P107 | *(formula)* |
| P110 | *(formula)* |

### Formula (in G2, dragged down)
```
=XLOOKUP(F2,$A$2:$A$11,$B$2:$B$11)
```

### Explanation
`XLOOKUP(lookup_value, lookup_array, return_array, [if_not_found], [match_mode], [search_mode])`:
- `F2` — the Product ID to search for.
- `$A$2:$A$11` — the column to search within (locked with `$` so it doesn't shift when dragged down).
- `$B$2:$B$11` — the column to pull the result from.

Unlike VLOOKUP, XLOOKUP takes the lookup array and return array as **two separate ranges** — it doesn't need a column index number, and the return column can be anywhere (even to the left of the lookup column).

### Result

| Product ID (F) | Product Name (G) |
|---|---|
| P103 | Bluetooth Speaker |
| P107 | LED Desk Lamp |
| P110 | Wired Headphones |

---

## Task 2: XLOOKUP Reverse Search — Last Order Amount by Restaurant (Bottom-Up)

### Sample Data (Zomato Orders — A1:D9, in chronological order)

| Order ID (A) | Restaurant Name (B) | Order Date (C) | Amount (D) |
|---|---|---|---|
| ZO01 | Domino's | 01-07-2026 | 650 |
| ZO02 | Behrouz Biryani | 03-07-2026 | 890 |
| ZO03 | Domino's | 10-07-2026 | 720 |
| ZO04 | KFC | 15-07-2026 | 540 |
| ZO05 | Behrouz Biryani | 20-07-2026 | 1100 |
| ZO06 | Domino's | 25-07-2026 | 980 |
| ZO07 | KFC | 29-07-2026 | 610 |
| ZO08 | Behrouz Biryani | 05-08-2026 | 1250 |

### Search Setup

| Cell | Content |
|---|---|
| F1 | Restaurant to Search → `Domino's` |
| F2 | Last Order Amount → formula |

### Formula (in F2)
```
=XLOOKUP(F1,B2:B9,D2:D9,"Not Found",0,-1)
```

### Explanation of the Arguments
- `F1` — restaurant name to search for.
- `B2:B9` — the lookup array (Restaurant Name).
- `D2:D9` — the return array (Amount).
- `"Not Found"` — the `if_not_found` default value.
- `0` — `match_mode` = exact match.
- **`-1`** — `search_mode` = **"search last to first"** — this is the key setting. It tells XLOOKUP to scan the array **starting from the bottom row and moving upward**, so the **first match it encounters is the most recent (last) order** for that restaurant, not the earliest one.

### Result
For **F1 = "Domino's"**, XLOOKUP scans from row 9 upward and finds the Domino's entry at row 6 first (Amount = 980) before it would ever reach row 3 or row 1 — so:
**F2 = 980** *(the most recent Domino's order, not the first one placed)*

> **Why this matters:** With a normal top-to-bottom search (`search_mode = 1`, the default), the same formula would instead return **650** — the *first* Domino's order in the list — which is the wrong answer for "last order." Setting `search_mode = -1` is exactly how XLOOKUP performs the "reverse lookup" demonstrated in the trainer's demo (finding an employee's *last* bonus).

---

## Task 3: XLOOKUP with Default Value — Spotify Playlist by Genre

### Sample Data (Playlists — A1:D6)

| Playlist Name (A) | Genre (B) | Created By (C) | Number of Songs (D) |
|---|---|---|---|
| Chill Vibes | Lo-fi | Spotify | 45 |
| Desi Hits | Bollywood | User | 60 |
| Rock Legends | Rock | Spotify | 38 |
| Workout Beats | EDM | User | 52 |
| Sunday Mornings | Jazz | Spotify | 30 |

### Search Setup

| Cell | Content |
|---|---|
| F1 | Genre to Search → e.g., `Rock` or `Pop` |
| F2 | Playlist Result → formula |

### Formula (in F2)
```
=XLOOKUP(F1,B2:B6,A2:A6,"No playlist available")
```

### Explanation
The **fourth argument** (`if_not_found`) is where XLOOKUP's built-in error handling shines — if `F1` doesn't match any value in the Genre column, XLOOKUP directly returns the custom text `"No playlist available"` instead of throwing an `#N/A` error. No need for a separate `IFERROR()` wrapper, unlike VLOOKUP.

### Sample Results

| F1 (Search) | F2 (Result) |
|---|---|
| Rock | Rock Legends |
| Jazz | Sunday Mornings |
| Pop | No playlist available |
| Hip-Hop | No playlist available |

---

## Task 4: XLOOKUP Error Handling — IRCTC Booking Status

### Sample Data (Bookings — A1:D6)

| Booking ID (A) | Passenger Name (B) | Train Number (C) | Status (D) |
|---|---|---|---|
| BK1001 | Rahul Sharma | 12951 | Confirmed |
| BK1002 | Anjali Mehta | 12301 | Waitlisted |
| BK1003 | Suresh Kumar | 12626 | Confirmed |
| BK1004 | Priya Nair | 22691 | RAC |
| BK1005 | Vikram Joshi | 12009 | Cancelled |

### Step 1: Basic Formula (Without Error Handling)
```
=XLOOKUP(F1,A2:A6,D2:D6)
```
If **F1 = "BK1099"** (a Booking ID that doesn't exist in the table), this formula returns Excel's default error:
```
#N/A
```
This happens because XLOOKUP's optional `if_not_found` argument was left out entirely, so it falls back to the standard lookup error.

### Step 2: Corrected Formula with Custom Error Message
```
=XLOOKUP(F1,A2:A6,D2:D6,"Booking Not Found")
```

### Result Comparison

| Search Value (F1) | Formula Without `if_not_found` | Formula With `if_not_found` |
|---|---|---|
| BK1003 | Confirmed | Confirmed |
| BK1099 *(invalid ID)* | `#N/A` | Booking Not Found |

**Explanation:** Adding `"Booking Not Found"` as the fourth argument tells XLOOKUP exactly what to display when no match exists, rather than surfacing a raw Excel error — much cleaner for anyone viewing the sheet, and it also prevents the `#N/A` from breaking any other formulas (like SUM or COUNTIF) that might reference this result cell.

---

## Task 5: AI-Assisted XLOOKUP — Myntra Delivery Date by Order ID

### Sample Prompt Used (as instructed)
> "Write an XLOOKUP formula to find the delivery date for an order by Order ID in Excel."

### Typical AI-Generated Formula Response
```
=XLOOKUP([Order ID to search], [Order ID range], [Delivery Date range])
```
Applied to a concrete sheet layout, this becomes:
```
=XLOOKUP(F1, A2:A6, D2:D6)
```

### Sample Data (Myntra Orders — A1:D6)

| Order ID (A) | Product (B) | Order Date (C) | Delivery Date (D) |
|---|---|---|---|
| MY501 | Kurta Set | 01-08-2026 | 06-08-2026 |
| MY502 | Sneakers | 02-08-2026 | 07-08-2026 |
| MY503 | Handbag | 03-08-2026 | 09-08-2026 |
| MY504 | Denim Jacket | 04-08-2026 | 10-08-2026 |
| MY505 | Sunglasses | 05-08-2026 | 08-08-2026 |

### Formula Tested (in G1, with F1 as the search cell)
```
=XLOOKUP(F1,A2:A6,D2:D6,"Order ID not found")
```
*(A default-value argument was added on top of the AI's base suggestion, applying the error-handling technique from Task 4 to make the formula more robust.)*

### Test Results

| F1 (Search Order ID) | G1 (Delivery Date Result) |
|---|---|
| MY503 | 09-08-2026 |
| MY501 | 06-08-2026 |
| MY999 *(invalid)* | Order ID not found |

**Verification:** The AI-suggested formula worked correctly once populated with the actual sheet's cell references (F1, A2:A6, D2:D6) — confirming that a generic XLOOKUP structure from an AI tool can be directly adapted to a real dataset by simply substituting in the correct ranges. Adding the fourth `if_not_found` argument (learned in Task 4) further improved on the AI's base answer by making the formula error-proof.

---
*End of Session 10 Assignment*
