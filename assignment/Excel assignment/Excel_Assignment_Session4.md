# Session 4 – Advanced Filtering & Custom Views
### Assignment Solutions

---

## Task 1: Food Delivery Orders — Advanced Filter (Amount > 800 AND City = 'Ahmedabad')

### Sample Dataset (15 orders) — placed in A1:D16

| Order ID | Restaurant Name | Amount | City |
|---|---|---|---|
| FD001 | Domino's | 650 | Ahmedabad |
| FD002 | Pizza Hut | 920 | Surat |
| FD003 | McDonald's | 480 | Ahmedabad |
| FD004 | Behrouz Biryani | 1100 | Ahmedabad |
| FD005 | Burger King | 750 | Vadodara |
| FD006 | KFC | 890 | Ahmedabad |
| FD007 | Wow Momo | 610 | Rajkot |
| FD008 | Subway | 430 | Ahmedabad |
| FD009 | Faasos | 950 | Ahmedabad |
| FD010 | Barbeque Nation | 1650 | Surat |
| FD011 | Haldiram's | 700 | Ahmedabad |
| FD012 | Chai Point | 320 | Vadodara |
| FD013 | Rajwadu | 1200 | Ahmedabad |
| FD014 | Sankalp | 880 | Rajkot |
| FD015 | Mirch Masala | 995 | Ahmedabad |

### Step 1: Build the Criteria Range
Place this above or beside the table (e.g., F1:G2), using the **exact same header spelling** as the data:

| Amount | City |
|---|---|
| >800 | Ahmedabad |

Both conditions sit on the **same row**, so Excel applies **AND** logic.

### Step 2: Apply Advanced Filter
1. Click inside the data table.
2. **Data tab → Advanced** (Sort & Filter group).
3. **Action:** Filter the list, in-place.
4. **List range:** `$A$1:$D$16`
5. **Criteria range:** `$F$1:$G$2`
6. Click **OK**.

### Result

| Order ID | Restaurant Name | Amount | City |
|---|---|---|---|
| FD004 | Behrouz Biryani | 1100 | Ahmedabad |
| FD006 | KFC | 890 | Ahmedabad |
| FD009 | Faasos | 950 | Ahmedabad |
| FD013 | Rajwadu | 1200 | Ahmedabad |
| FD015 | Mirch Masala | 995 | Ahmedabad |

Only Ahmedabad orders with an Amount strictly greater than 800 remain visible; everything else (wrong city, or Ahmedabad but ≤ 800) is hidden.

---

## Task 2: Online Shopping Transactions — Advanced Filter (Payment Method = 'UPI' OR Status = 'Delivered')

### Sample Dataset (20 transactions) — placed in A1:E21

| Order No | Product | Price | Payment Method | Status |
|---|---|---|---|---|
| OT001 | Headphones | 1499 | UPI | Delivered |
| OT002 | Backpack | 899 | Credit Card | Pending |
| OT003 | Smartwatch | 2999 | Wallet | Delivered |
| OT004 | Shoes | 1899 | UPI | Cancelled |
| OT005 | Laptop Stand | 799 | Net Banking | Pending |
| OT006 | Bluetooth Speaker | 1299 | Debit Card | Delivered |
| OT007 | Phone Case | 299 | UPI | Delivered |
| OT008 | Table Lamp | 599 | Wallet | Pending |
| OT009 | Keyboard | 1199 | UPI | Pending |
| OT010 | Office Chair | 4999 | Credit Card | Delivered |
| OT011 | Water Bottle | 349 | Net Banking | Cancelled |
| OT012 | Sunglasses | 699 | UPI | Pending |
| OT013 | Wallet (item) | 499 | Debit Card | Delivered |
| OT014 | Notebook Set | 249 | UPI | Delivered |
| OT015 | Gaming Mouse | 999 | Credit Card | Pending |
| OT016 | Yoga Mat | 799 | Wallet | Delivered |
| OT017 | Router | 1599 | UPI | Cancelled |
| OT018 | Desk Organizer | 449 | Net Banking | Delivered |
| OT019 | Earbuds | 1999 | UPI | Pending |
| OT020 | Study Lamp | 649 | Debit Card | Cancelled |

### Step 1: Build the Criteria Range (OR logic)
Place this beside the table (e.g., G1:H3):

| Payment Method | Status |
|---|---|
| UPI | |
| | Delivered |

**Key rule:** Placing conditions on **different rows** makes Excel evaluate them as **OR** — a row qualifies if it matches *either* condition. Leave the opposite cell blank in each row (a blank criteria cell means "no restriction" for that column).

### Step 2: Apply Advanced Filter
1. Click inside the data table.
2. **Data tab → Advanced**.
3. **List range:** `$A$1:$E$21`
4. **Criteria range:** `$G$1:$H$3`
5. **Action:** Filter the list, in-place → **OK**.

### Result (rows where Payment Method = UPI **or** Status = Delivered)

| Order No | Product | Price | Payment Method | Status |
|---|---|---|---|---|
| OT001 | Headphones | 1499 | UPI | Delivered |
| OT003 | Smartwatch | 2999 | Wallet | Delivered |
| OT004 | Shoes | 1899 | UPI | Cancelled |
| OT006 | Bluetooth Speaker | 1299 | Debit Card | Delivered |
| OT007 | Phone Case | 299 | UPI | Delivered |
| OT009 | Keyboard | 1199 | UPI | Pending |
| OT010 | Office Chair | 4999 | Credit Card | Delivered |
| OT012 | Sunglasses | 699 | UPI | Pending |
| OT013 | Wallet (item) | 499 | Debit Card | Delivered |
| OT014 | Notebook Set | 249 | UPI | Delivered |
| OT016 | Yoga Mat | 799 | Wallet | Delivered |
| OT017 | Router | 1599 | UPI | Cancelled |
| OT018 | Desk Organizer | 449 | Net Banking | Delivered |
| OT019 | Earbuds | 1999 | UPI | Pending |

Only rows that are **neither UPI nor Delivered** (e.g., OT002, OT005, OT008, OT011, OT015, OT020) are hidden.

---

## Task 3: Movie Bookings — Copy Filtered Results to a New Location

### Sample Dataset (12 bookings) — placed in A1:E13

| Booking ID | Movie Name | Region | Seats Booked | Total Amount |
|---|---|---|---|---|
| MB01 | Pathaan | West | 4 | 1200 |
| MB02 | Jawan | South | 2 | 600 |
| MB03 | Animal | West | 6 | 1800 |
| MB04 | Fighter | North | 3 | 750 |
| MB05 | Stree 2 | West | 5 | 1500 |
| MB06 | Kalki 2898 AD | East | 2 | 700 |
| MB07 | Salaar | West | 3 | 900 |
| MB08 | Rocky Aur Rani | South | 4 | 1000 |
| MB09 | Gadar 2 | West | 7 | 2100 |
| MB10 | Dunki | North | 2 | 500 |
| MB11 | Tiger 3 | West | 2 | 600 |
| MB12 | 12th Fail | East | 3 | 850 |

### Step 1: Build the Criteria Range (AND logic, same row)
Place beside the table (e.g., G1:H2):

| Region | Total Amount |
|---|---|
| West | >1000 |

### Step 2: Apply Advanced Filter with "Copy to another location"
1. Click inside the data table.
2. **Data tab → Advanced**.
3. **Action:** Select **"Copy to another location"** (this is what preserves the original data untouched).
4. **List range:** `$A$1:$E$13`
5. **Criteria range:** `$G$1:$H$2`
6. **Copy to:** click an empty cell far enough away, e.g., `$A$16` (below the original table with spacing) or `$G$5`.
7. Click **OK**.

### Result — Copied Output (original 12 rows remain fully visible/unfiltered)

| Booking ID | Movie Name | Region | Seats Booked | Total Amount |
|---|---|---|---|---|
| MB01 | Pathaan | West | 4 | 1200 |
| MB03 | Animal | West | 6 | 1800 |
| MB05 | Stree 2 | West | 5 | 1500 |
| MB09 | Gadar 2 | West | 7 | 2100 |

**Why this matters:** Unlike "Filter the list, in-place" (which hides rows in the same table), "Copy to another location" creates a **separate, clean extract** — ideal when you need to share or export just the qualifying records (e.g., West-region bookings above ₹1000) while keeping the master booking sheet intact for other reports.

---

## Task 4: Instagram Influencer Campaigns — Custom Views

### Sample Dataset (10 campaigns) — placed in A1:E11

| Campaign ID | Influencer Name | Followers | Engagement Rate | Platform |
|---|---|---|---|---|
| CMP01 | Priya Fashion | 250000 | 6.2% | Instagram |
| CMP02 | TechWithRahul | 480000 | 4.1% | YouTube |
| CMP03 | FoodieAnjali | 120000 | 7.8% | Instagram |
| CMP04 | GamerVikram | 650000 | 3.5% | YouTube |
| CMP05 | TravelWithMeera | 90000 | 8.9% | Instagram |
| CMP06 | FitnessRohan | 310000 | 5.5% | YouTube |
| CMP07 | BeautyByRiya | 180000 | 6.7% | Instagram |
| CMP08 | ComedyKaran | 720000 | 2.9% | YouTube |
| CMP09 | DanceWithNeha | 95000 | 9.4% | Instagram |
| CMP10 | VlogWithArjun | 410000 | 4.8% | YouTube |

### Step 1: Set the Base (Unfiltered) View First
Before creating any custom view, save the **current, unfiltered state** as a baseline so you can always return to it:
1. **View tab → Custom Views → Add…**
2. Name it `All Campaigns` → OK.

### Step 2: Create Custom View 1 — "High Engagement" (Engagement Rate > 5%)
1. Apply **AutoFilter** (Ctrl+Shift+L) on the header row.
2. Click the dropdown on **Engagement Rate → Number Filters → Greater Than… → 5% → OK.**
   *(Rows CMP01, CMP03, CMP05, CMP06, CMP07, CMP09 remain visible.)*
3. **View tab → Custom Views → Add…**
4. Name it: `High Engagement (>5%)` → check "Filter settings" (should be checked by default) → **OK**.

### Step 3: Create Custom View 2 — "YouTube Only"
1. First, clear the previous filter: **Data tab → Clear** (or reopen the Engagement Rate dropdown → Clear Filter).
2. Click the dropdown on **Platform → uncheck "Select All" → check only "YouTube" → OK.**
   *(Rows CMP02, CMP04, CMP06, CMP08, CMP10 remain visible.)*
3. **View tab → Custom Views → Add…**
4. Name it: `YouTube Campaigns` → **OK**.

### Step 4: Switching Between Views
Go to **View tab → Custom Views**, select any saved view from the list (`All Campaigns`, `High Engagement (>5%)`, or `YouTube Campaigns`), and click **Show**. Excel instantly re-applies that exact filter state without you having to manually reset filters each time.

### View Outputs

**"High Engagement (>5%)" view:**

| Campaign ID | Influencer Name | Followers | Engagement Rate | Platform |
|---|---|---|---|---|
| CMP01 | Priya Fashion | 250000 | 6.2% | Instagram |
| CMP03 | FoodieAnjali | 120000 | 7.8% | Instagram |
| CMP05 | TravelWithMeera | 90000 | 8.9% | Instagram |
| CMP06 | FitnessRohan | 310000 | 5.5% | YouTube |
| CMP07 | BeautyByRiya | 180000 | 6.7% | Instagram |
| CMP09 | DanceWithNeha | 95000 | 9.4% | Instagram |

**"YouTube Campaigns" view:**

| Campaign ID | Influencer Name | Followers | Engagement Rate | Platform |
|---|---|---|---|---|
| CMP02 | TechWithRahul | 480000 | 4.1% | YouTube |
| CMP04 | GamerVikram | 650000 | 3.5% | YouTube |
| CMP06 | FitnessRohan | 310000 | 5.5% | YouTube |
| CMP08 | ComedyKaran | 720000 | 2.9% | YouTube |
| CMP10 | VlogWithArjun | 410000 | 4.8% | YouTube |

> **Note:** Custom Views also remember column widths, hidden columns/rows, and print settings at the time they were saved — making them a fast way to switch between different "report angles" on the same sheet without duplicating data or rebuilding filters each time.

---
*End of Session 4 Assignment*
