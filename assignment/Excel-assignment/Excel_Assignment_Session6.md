# Session 6 – Text Functions (Part 2: Cleaning Functions)
### Assignment Solutions

---

## Task 1: TRIM Function — Clean Extra Spaces from User Names

### Sample Data (Column A)
*(Note: leading/trailing/multiple spaces are shown using visible markers for clarity — in Excel these would just be actual space characters.)*

| User Name (A) |
|---|
| ` anjali mehta ` |
| ` RAVI PATEL` |
| ` Priya Singh ` |
| `sneha  gupta` *(double space between words)* |
| ` Karan  Mehra ` |

### Formula (in B2, dragged down)
```
=TRIM(A2)
```

### Explanation
`TRIM()` removes all **leading and trailing spaces**, and also collapses any **multiple spaces between words** down to a single space — it does not affect the case or content of the text itself.

### Result

| User Name (A) | Trimmed (B) |
|---|---|
| ` anjali mehta ` | anjali mehta |
| ` RAVI PATEL` | RAVI PATEL |
| ` Priya Singh ` | Priya Singh |
| `sneha  gupta` | sneha gupta |
| ` Karan  Mehra ` | Karan Mehra |

---

## Task 2: CLEAN Function — Remove Non-Printable Characters

### Sample Data (Column A)
*(Cells contain hidden non-printable characters such as line breaks (CHAR(10)) or control characters — represented below with `[LF]` to show where they occur.)*

| WhatsApp Group Name (A) |
|---|
| `Family[LF]Group` |
| `Office🔧Team[LF]` |
| `College Friends[LF][LF]` |
| `Weekend[LF]Trip Plan` |
| `Cricket🏏Squad[LF]` |

### Formula (in B2, dragged down)
```
=CLEAN(A2)
```

### Explanation
`CLEAN()` removes all **non-printable characters** — things like line breaks, tabs, and other control codes (ASCII codes 0–31) that often get pulled in from exports, PDFs, or copy-pasted chat data — but it does **not** remove printable special characters like emojis or symbols, nor does it remove regular spaces (that's TRIM's job).

### Result

| WhatsApp Group Name (A) | Cleaned (B) |
|---|---|
| `Family[LF]Group` | Family Group *(joined, no visible break)* |
| `Office🔧Team[LF]` | Office🔧Team |
| `College Friends[LF][LF]` | College Friends |
| `Weekend[LF]Trip Plan` | Weekend Trip Plan |
| `Cricket🏏Squad[LF]` | Cricket🏏Squad |

> **Tip:** If a group name still looks messy after CLEAN (e.g., emojis remain), that's expected — CLEAN only strips non-printable codes, not visible emoji characters. Combine with TRIM if extra spaces also appear after the line breaks are removed: `=TRIM(CLEAN(A2))`.

---

## Task 3: SUBSTITUTE Function — Replace Underscores with Spaces

### Sample Data (Column A)

| Song Title (A) |
|---|
| Shape_of_You |
| Blinding_Lights |
| Levitating_Remix |
| Kesariya_Reprise |
| Save_Your_Tears |

### Formula (in B2, dragged down)
```
=SUBSTITUTE(A2,"_"," ")
```

### Explanation
`SUBSTITUTE(text, old_text, new_text)` finds every occurrence of `old_text` ("_") inside the string and replaces it with `new_text` (" "). Since no `instance_num` argument is given, **all** occurrences are replaced, not just the first one — exactly what's needed here since titles like "Save_Your_Tears" have two underscores.

### Result

| Song Title (A) | Cleaned Title (B) |
|---|---|
| Shape_of_You | Shape of You |
| Blinding_Lights | Blinding Lights |
| Levitating_Remix | Levitating Remix |
| Kesariya_Reprise | Kesariya Reprise |
| Save_Your_Tears | Save Your Tears |

---

## Task 4: Nested TRIM + CLEAN + PROPER — Fully Formatted Influencer Names

### Sample Data (Column A)
*(Mixed case, extra spaces, and possibly stray non-printable characters from copy-pasting off Instagram — `[LF]` marks a hidden line break where present.)*

| Influencer Name (A) |
|---|
| `vIshAl PATEL` |
| ` aNkuR  SHAH ` |
| `riYA[LF]mehta ` |
| ` KARAN   desai` |
| `sNEha PateL ` |

### Formula (in B2, dragged down) — single nested formula
```
=PROPER(TRIM(CLEAN(A2)))
```

### Explanation of the Nesting (evaluated inside-out)
1. **`CLEAN(A2)`** runs first — strips out any non-printable characters (line breaks, control codes) from the raw text.
2. **`TRIM(...)`** wraps around that result — removes leading/trailing spaces and collapses double spaces between words.
3. **`PROPER(...)`** wraps around the whole thing — capitalizes the first letter of each word and lowercases the rest, regardless of how the original text was cased.

This single formula performs all three cleaning steps in one go, exactly as the hint suggests.

### Result

| Influencer Name (A) | Cleaned & Formatted (B) |
|---|---|
| `vIshAl PATEL` | Vishal Patel |
| ` aNkuR  SHAH ` | Ankur Shah |
| `riYA[LF]mehta ` | Riya Mehta |
| ` KARAN   desai` | Karan Desai |
| `sNEha PateL ` | Sneha Patel |

---

## Task 5: UPPER / LOWER / PROPER — Flipkart Product Names Side by Side

### Sample Data (Column A) — all uppercase

| Product Name (A) |
|---|
| WIRELESS BLUETOOTH HEADPHONES |
| STAINLESS STEEL WATER BOTTLE |
| MEN'S RUNNING SHOES |
| SMART LED TV 43 INCH |
| KITCHEN NON-STICK COOKWARE SET |

### Formulas

| Column | Formula |
|---|---|
| **B (Lowercase)** | `=LOWER(A2)` |
| **C (Proper Case)** | `=PROPER(A2)` |

*(UPPER isn't needed as a formula here since column A is already the uppercase source — but for completeness, if starting from mixed case, the uppercase formula would be `=UPPER(A2)`.)*

### Result — All Three Versions Side by Side

| Original / UPPER (A) | Lowercase (B) = LOWER(A2) | Proper Case (C) = PROPER(A2) |
|---|---|---|
| WIRELESS BLUETOOTH HEADPHONES | wireless bluetooth headphones | Wireless Bluetooth Headphones |
| STAINLESS STEEL WATER BOTTLE | stainless steel water bottle | Stainless Steel Water Bottle |
| MEN'S RUNNING SHOES | men's running shoes | Men'S Running Shoes |
| SMART LED TV 43 INCH | smart led tv 43 inch | Smart Led Tv 43 Inch |
| KITCHEN NON-STICK COOKWARE SET | kitchen non-stick cookware set | Kitchen Non-Stick Cookware Set |

> **Important observation about PROPER:** Excel's `PROPER()` capitalizes the letter following *any* non-letter character — including apostrophes and hyphens. That's why "MEN'S" becomes "Men'S" (capital S after the apostrophe) and "TV" becomes "Tv" (since PROPER doesn't recognize acronyms). For product listings where this matters, a manual correction or a `SUBSTITUTE`-based workaround is typically applied afterward — but the plain `PROPER()` function is what the task calls for.

---
*End of Session 6 Assignment*
