# Session 8 – Logical Functions
### Assignment Solutions

---

## Task 1: IF Function — 'High Value' vs 'Regular' Orders

### Sample Data (Food Delivery Orders)

| Order ID (A) | Total Amount (B) | Order Category (C) |
|---|---|---|
| FD01 | 650 | *(formula)* |
| FD02 | 320 | *(formula)* |
| FD03 | 500 | *(formula)* |
| FD04 | 899 | *(formula)* |
| FD05 | 275 | *(formula)* |

### Formula (in C2, dragged down)
```
=IF(B2>=500,"High Value","Regular")
```

### Explanation
`IF(logical_test, value_if_true, value_if_false)` checks whether the Total Amount is **greater than or equal to** ₹500. If TRUE, it returns "High Value"; otherwise it returns "Regular." The `>=` operator ensures an order of exactly ₹500 is correctly counted as High Value (not excluded).

### Result

| Order ID | Total Amount | Order Category |
|---|---|---|
| FD01 | 650 | High Value |
| FD02 | 320 | Regular |
| FD03 | 500 | High Value |
| FD04 | 899 | High Value |
| FD05 | 275 | Regular |

---

## Task 2: Nested IF — Cricket Player Rating

### Sample Data

| Player Name (A) | Total Runs (B) | Rating (C) |
|---|---|---|
| Virat | 1250 | *(formula)* |
| Rohit | 850 | *(formula)* |
| Shubman | 550 | *(formula)* |
| Rinku | 320 | *(formula)* |
| Suryakumar | 980 | *(formula)* |

### Formula (in C2, dragged down)
```
=IF(B2>=1000,"Star",IF(B2>=700,"Pro",IF(B2>=400,"Rising","Newbie")))
```

### Explanation — How the Nesting Works
Excel evaluates this **outside-in, top condition first**:
1. **First IF:** Is Runs ≥ 1000? → If TRUE, return **"Star"** immediately (no further checks happen).
2. If FALSE, Excel moves to the **second IF** (nested inside the `value_if_false` of the first): Is Runs ≥ 700? → If TRUE, return **"Pro"**.
3. If FALSE, Excel moves to the **third IF**: Is Runs ≥ 400? → If TRUE, return **"Rising"**.
4. If all three conditions are FALSE (Runs < 400), the final `value_if_false` returns **"Newbie"**.

**Key rule for nested IFs with ranges:** always test the **highest threshold first**, working downward. If you tested `>=400` first, a player with 1250 runs would incorrectly stop at "Rising" since 1250 does satisfy ≥400 — the higher thresholds would never get a chance to be checked.

### Result

| Player Name | Total Runs | Rating |
|---|---|---|
| Virat | 1250 | Star |
| Rohit | 850 | Pro |
| Shubman | 550 | Rising |
| Rinku | 320 | Newbie |
| Suryakumar | 980 | Pro |

> **Alternative (cleaner) approach using IFS** — covered later in this same session:
> `=IFS(B2>=1000,"Star",B2>=700,"Pro",B2>=400,"Rising",TRUE,"Newbie")`
> This avoids deep nesting and is easier to read for more than 2–3 tiers.

---

## Task 3: AND + IF — Flipkart 'Eligible' Orders

**Condition:** Mark as "Eligible" only if Payment Method = "Prepaid" **AND** Status = "Delivered."

### Sample Data

| Order ID (A) | Payment Method (B) | Status (C) | Eligible? (D) |
|---|---|---|---|
| FK01 | Prepaid | Delivered | *(formula)* |
| FK02 | Cash on Delivery | Delivered | *(formula)* |
| FK03 | Prepaid | Pending | *(formula)* |
| FK04 | Prepaid | Delivered | *(formula)* |
| FK05 | Cash on Delivery | Cancelled | *(formula)* |

### Formula (in D2, dragged down)
```
=IF(AND(B2="Prepaid",C2="Delivered"),"Eligible","Not Eligible")
```

### Explanation
`AND(condition1, condition2, ...)` returns **TRUE only if every condition inside it is TRUE**. Here, both the payment method must exactly match "Prepaid" **and** the status must exactly match "Delivered" for the row to qualify. If even one condition fails, `AND` returns FALSE, and the `IF` returns "Not Eligible."

### Result

| Order ID | Payment Method | Status | Eligible? |
|---|---|---|---|
| FK01 | Prepaid | Delivered | Eligible |
| FK02 | Cash on Delivery | Delivered | Not Eligible |
| FK03 | Prepaid | Pending | Not Eligible |
| FK04 | Prepaid | Delivered | Eligible |
| FK05 | Cash on Delivery | Cancelled | Not Eligible |

---

## Task 4: OR + IF — Playlist 'Quick Access' Songs

**Condition:** Mark as "Quick Access" if the song is downloaded **OR** favorited (or both).

### Sample Data

| Song Name (A) | Artist (B) | isDownloaded (C) | isFavorite (D) | Access Tag (E) |
|---|---|---|---|---|
| Blinding Lights | The Weeknd | TRUE | FALSE | *(formula)* |
| Kesariya | Arijit Singh | FALSE | TRUE | *(formula)* |
| Levitating | Dua Lipa | FALSE | FALSE | *(formula)* |
| Apna Bana Le | Arijit Singh | TRUE | TRUE | *(formula)* |
| Paint The Town Red | Doja Cat | FALSE | FALSE | *(formula)* |

### Formula (in E2, dragged down)
```
=IF(OR(C2=TRUE,D2=TRUE),"Quick Access","Standard")
```
*(Since C2 and D2 are already TRUE/FALSE Boolean values, this can also be simplified to `=IF(OR(C2,D2),"Quick Access","Standard")`.)*

### Explanation
`OR(condition1, condition2, ...)` returns **TRUE if at least one condition is TRUE** — unlike `AND`, it doesn't require all of them to be true. So a song only needs to be downloaded, only favorited, or both, to qualify.

### Result

| Song Name | isDownloaded | isFavorite | Access Tag |
|---|---|---|---|
| Blinding Lights | TRUE | FALSE | Quick Access |
| Kesariya | FALSE | TRUE | Quick Access |
| Levitating | FALSE | FALSE | Standard |
| Apna Bana Le | TRUE | TRUE | Quick Access |
| Paint The Town Red | FALSE | FALSE | Standard |

---

## Task 5: XOR + IF — Flagging 'Suspicious' Zomato Orders

**Condition:** Flag as "Suspicious" only if **exactly one** of the two is true — New Address **or** Cash Payment — but not both, and not neither.

### Sample Data

| Order ID (A) | New Address? (B) | Cash Payment? (C) | Flag (D) |
|---|---|---|---|
| ZM01 | TRUE | FALSE | *(formula)* |
| ZM02 | TRUE | TRUE | *(formula)* |
| ZM03 | FALSE | FALSE | *(formula)* |
| ZM04 | FALSE | TRUE | *(formula)* |
| ZM05 | TRUE | FALSE | *(formula)* |

### Formula (in D2, dragged down)
```
=IF(XOR(B2=TRUE,C2=TRUE),"Suspicious","Normal")
```
*(Simplified since B2/C2 are Boolean: `=IF(XOR(B2,C2),"Suspicious","Normal")`.)*

### Explanation
`XOR(condition1, condition2)` returns:
- **TRUE** if **exactly one** of the two conditions is true (one TRUE, one FALSE — either combination).
- **FALSE** if both conditions are true, **or** if both are false.

This is different from `OR`, which would also return TRUE when *both* conditions are true — `XOR` specifically excludes that "both true" case, matching the "one or the other, not both" logic needed to catch a genuinely unusual pattern (e.g., a regular customer suddenly using a new address is worth flagging, but a new customer paying cash from a new address for the first time is arguably normal, not suspicious).

### Result

| Order ID | New Address? | Cash Payment? | Flag |
|---|---|---|---|
| ZM01 | TRUE | FALSE | Suspicious |
| ZM02 | TRUE | TRUE | Normal |
| ZM03 | FALSE | FALSE | Normal |
| ZM04 | FALSE | TRUE | Suspicious |
| ZM05 | TRUE | FALSE | Suspicious |

**Row-by-row logic check:**
- **ZM01:** New Address (T) + Cash (F) → exactly one TRUE → **Suspicious** ✔
- **ZM02:** New Address (T) + Cash (T) → both TRUE → **Normal** (not flagged, since XOR excludes "both true")
- **ZM03:** New Address (F) + Cash (F) → neither TRUE → **Normal**
- **ZM04:** New Address (F) + Cash (T) → exactly one TRUE → **Suspicious** ✔
- **ZM05:** New Address (T) + Cash (F) → exactly one TRUE → **Suspicious** ✔

---
*End of Session 8 Assignment*
