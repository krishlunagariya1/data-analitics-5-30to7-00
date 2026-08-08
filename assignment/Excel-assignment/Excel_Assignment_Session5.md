# Session 5 – Text Functions (Part 1)
### Assignment Solutions

---

## Task 1: LEFT Function — Extract First 4 Characters from Product Names

### Sample Data (Column A)

| Product Name (A) |
|---|
| iPhone-Apple |
| Galaxy-Samsung |
| Redmi-Xiaomi |
| Pixel-Google |
| Nord-OnePlus |

### Formula (in B2, dragged down)
```
=LEFT(A2,4)
```

### Explanation
`LEFT(text, num_chars)` returns the specified number of characters starting from the **left (beginning)** of the text string. Here, `4` means it always pulls exactly the first 4 characters, regardless of where a hyphen or space appears.

### Result

| Product Name (A) | First 4 Chars (B) |
|---|---|
| iPhone-Apple | iPho |
| Galaxy-Samsung | Gala |
| Redmi-Xiaomi | Redm |
| Pixel-Google | Pixe |
| Nord-OnePlus | Nord |

---

## Task 2: RIGHT Function — Extract State Code (Last 2 Characters)

### Sample Data (Column A)

| Order ID (A) |
|---|
| ODR-2024-GJ |
| ODR-2024-MH |
| ODR-2024-DL |
| ODR-2024-KA |
| ODR-2024-TN |

### Formula (in B2, dragged down)
```
=RIGHT(A2,2)
```

### Explanation
`RIGHT(text, num_chars)` returns the specified number of characters counting from the **right (end)** of the text string. Since every state code here is exactly 2 letters, `2` reliably extracts "GJ", "MH", etc.

### Result

| Order ID (A) | State Code (B) |
|---|---|
| ODR-2024-GJ | GJ |
| ODR-2024-MH | MH |
| ODR-2024-DL | DL |
| ODR-2024-KA | KA |
| ODR-2024-TN | TN |

---

## Task 3: MID + FIND — Extract Username from Email Address

### Sample Data (Column A)

| Email (A) |
|---|
| virat18@gmail.com |
| rohit45@yahoo.com |
| msdhoni7@gmail.com |
| priya.sharma@outlook.com |
| ajay_k@gmail.com |

### Formula (in B2, dragged down)
```
=MID(A2,1,FIND("@",A2)-1)
```

### Explanation, step by step
1. `FIND("@",A2)` locates the **position number** of the "@" symbol within the email string.
   - For `virat18@gmail.com`, "@" is at position 8.
2. `FIND("@",A2)-1` subtracts 1, giving the exact **length of the username** portion (7, since "virat18" has 7 characters).
3. `MID(A2, 1, 7)` then extracts 7 characters starting from position 1 (the very beginning) — which is exactly the username, stopping right before the "@".

**General syntax reminder:** `MID(text, start_num, num_chars)`.

### Result

| Email (A) | Username (B) |
|---|---|
| virat18@gmail.com | virat18 |
| rohit45@yahoo.com | rohit45 |
| msdhoni7@gmail.com | msdhoni7 |
| priya.sharma@outlook.com | priya.sharma |
| ajay_k@gmail.com | ajay_k |

> Note: This formula works correctly regardless of the username's length or the email domain, since it dynamically calculates the cut-off point using `FIND` instead of a fixed number.

---

## Task 4: TEXT Function — Format Cricket Scores as "156 runs"

### Sample Data (Column A)

| Score (A) |
|---|
| 156 |
| 210 |
| 98 |
| 45 |
| 301 |

### Formula (in B2, dragged down)
```
=TEXT(A2,"0")&" runs"
```

### Explanation
- `TEXT(A2,"0")` converts the number in A2 into a **text string** using the format code `"0"`, which displays the number as a plain whole number (no decimals) — this step matters because it lets you safely concatenate a number with text using `&`.
- `&" runs"` appends the literal word " runs" to the end.

*(Alternative without TEXT, using simple concatenation, also works here since these are whole numbers: `=A2&" runs"` — but `TEXT()` is the more robust/expected approach, especially if scores ever include decimals or need specific formatting like thousand separators, e.g. `=TEXT(A2,"#,##0")&" runs"`.)*

### Result

| Score (A) | Formatted (B) |
|---|---|
| 156 | 156 runs |
| 210 | 210 runs |
| 98 | 98 runs |
| 45 | 45 runs |
| 301 | 301 runs |

---

## Task 5: REPT Function — Repeat 'SALE' Without Helper Columns

### Sample Data

| Repeat Count (A) | Result (B) |
|---|---|
| 3 | *(formula)* |
| 5 | *(formula)* |
| 1 | *(formula)* |
| 4 | *(formula)* |
| 2 | *(formula)* |

### Formula (in B2, dragged down) — single formula, no helper column
```
=REPT("SALE",A2)
```

### Explanation
`REPT(text, number_times)` repeats the given text string exactly the number of times specified — directly referencing the count cell (A2) as the `number_times` argument. Because the entire repetition logic lives inside **one** function call, no intermediate/helper column or VBA macro is needed, satisfying the task's constraint.

### Result

| Repeat Count (A) | Result (B) |
|---|---|
| 3 | SALESALESALE |
| 5 | SALESALESALESALESALE |
| 1 | SALE |
| 4 | SALESALESALESALE |
| 2 | SALESALE |

---
*End of Session 5 Assignment*
