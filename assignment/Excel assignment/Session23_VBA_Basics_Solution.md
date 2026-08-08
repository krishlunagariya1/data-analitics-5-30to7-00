# Session 23 – VBA Programming (Basics)
## Solved Assignment

**Opening the VBA Editor (needed before every task below):**
1. **Developer tab → Visual Basic** (or press **Alt+F11**).
2. In the Project Explorer pane (left side), right-click your workbook → **Insert → Module**. This creates **Module1**.
3. Type each subroutine below directly into Module1's code pane.
4. To run any macro: click anywhere inside its `Sub`/`End Sub` block → press **F5**, or go back to Excel and use **Developer → Macros → [name] → Run**.
5. Remember to save as **.xlsm** (Excel Macro-Enabled Workbook) — a plain `.xlsx` will silently drop all this code on save.

---

## Task 1 — MsgBox Welcome Macro

```vba
Sub ShowWelcomeMessage()
    MsgBox "Welcome to VBA Programming!"
End Sub
```

**What it does:** `MsgBox` is VBA's built-in function for popping up a simple dialog box with a text string and an OK button. Running this sub displays exactly that message.

---

## Task 2 — Declare Variables (String, Integer, Boolean) and Display Them

```vba
Sub ShowUserDetails()
    Dim userName As String
    Dim orderCount As Integer
    Dim isPremiumUser As Boolean

    userName = "Rahul Patel"
    orderCount = 12
    isPremiumUser = True

    MsgBox "Name: " & userName & vbNewLine & _
           "Order Count: " & orderCount & vbNewLine & _
           "Premium User: " & isPremiumUser
End Sub
```

**Key points:**
- `Dim` declares a variable and its data type — `String` for text, `Integer` for whole numbers, `Boolean` for True/False.
- `&` concatenates text and variables together into one string for the message box.
- `vbNewLine` is a built-in VBA constant that inserts a line break, so all three values appear on separate lines instead of one run-on sentence.
- The underscore `_` at the end of a line is VBA's line-continuation character, letting one logical statement span multiple lines of code for readability.

---

## Task 3 — Conditional Cell Coloring Based on Value

```vba
Sub ColorCellByValue()
    If ActiveSheet.Range("A1").Value > 100 Then
        ActiveSheet.Range("A1").Interior.Color = RGB(0, 176, 80)   ' green
    Else
        ActiveSheet.Range("A1").Interior.Color = RGB(255, 0, 0)    ' red
    End If
End Sub
```

**Key points:**
- `ActiveSheet.Range("A1").Value` reads whatever is currently in cell A1 of the sheet you're viewing.
- `If...Then...Else...End If` is VBA's conditional structure — exactly like Excel's `IF()` formula, but written as code that performs an *action* (coloring a cell) rather than returning a value.
- `.Interior.Color` sets a cell's background fill color. `RGB(0,176,80)` and `RGB(255,0,0)` are standard green/red — you can substitute any RGB triplet for a different shade.
- Test it by typing `150` into A1 and running the macro (turns green), then `50` and running again (turns red).

---

## Task 4 — For Loop: Set A1:A10 to Their Row Numbers

```vba
Sub FillRowNumbers()
    Dim i As Integer

    For i = 1 To 10
        ActiveSheet.Cells(i, 1).Value = i
    Next i
End Sub
```

**Key points:**
- `Dim i As Integer` declares a loop counter variable.
- `For i = 1 To 10 ... Next i` repeats the code between them once for each value of `i` from 1 through 10.
- `Cells(i, 1)` refers to row `i`, column `1` (i.e., column A) — using `Cells(row, column)` instead of `Range("A1")` is exactly what makes it easy to loop, since the row number is just the variable `i`.
- After running: A1=1, A2=2, A3=3, ... A10=10.

---

## Task 5 — For Each Loop: Bold + Size 14 Font on A1:D1 Across All Sheets

```vba
Sub FormatHeaderAllSheets()
    Dim ws As Worksheet

    For Each ws In Worksheets
        ws.Range("A1:D1").Font.Bold = True
        ws.Range("A1:D1").Font.Size = 14
    Next ws
End Sub
```

**Key points:**
- `Dim ws As Worksheet` declares a variable that represents "one worksheet at a time."
- `For Each ws In Worksheets ... Next ws` loops through **every sheet in the workbook**, one at a time, without needing to know how many sheets exist or their names in advance — `Worksheets` is the built-in collection of all sheet objects in the active workbook.
- Inside the loop, `ws` stands in for "whichever sheet we're currently on," so `ws.Range("A1:D1")` always refers to that range on the current sheet in the loop, not a fixed single sheet.
- `.Font.Bold = True` and `.Font.Size = 14` are the two formatting properties applied — this matches the session's demo theme of "updating all sheets with unified formatting" using a single macro run.

---

## Summary Table

| Task | VBA Concept Used | Key Statement |
|---|---|---|
| 1 | MsgBox | `MsgBox "text"` |
| 2 | Variables & data types | `Dim x As String/Integer/Boolean` |
| 3 | If...Then...Else | `If Range("A1").Value > 100 Then ... Else ... End If` |
| 4 | For loop + Cells property | `For i = 1 To 10 : Cells(i,1).Value = i : Next i` |
| 5 | For Each loop + Worksheets collection | `For Each ws In Worksheets ... Next ws` |
