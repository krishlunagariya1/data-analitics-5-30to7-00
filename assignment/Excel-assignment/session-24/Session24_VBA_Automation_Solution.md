# Session 24 – VBA Automation Project + Case Study
## Solved Assignment

**File used:** `vba_project_data.xlsx` (attached alongside this document) — a 4-sheet workbook set up as the case study base:

| Sheet | Contents | Used for |
|---|---|---|
| `IPL_Matches` | 15 unformatted match records (plain headers, default column widths, no borders) | Task 1 |
| `Spotify_Playlist` | 10 tracks with **3 duplicate rows** and **extra leading/trailing spaces** in Track Name & Artist | Task 2 |
| `Flipkart_Sales` | 40 sales records (Order ID, Category, City, Amount) — pivot-ready | Task 3 |
| `Dashboard` | Placeholder dashboard sheet (build your PivotTable/PivotChart here, then this is what Tasks 3 & 4 act on) | Tasks 3 & 4 |

**Setup first:** open the file, **Alt+F11** to open the VBA Editor, **Insert → Module** (repeat for a fresh module per task if you like, or keep them all in Module1), paste each macro below, then **File → Save As → Excel Macro-Enabled Workbook (.xlsm)** so the code survives saving.

---

## Task 1 — Format IPL Match Data (Bold Headers, AutoFit, Borders)

Recorded via **Developer → Record Macro** while performing: select row 1 → Bold → select the whole table → AutoFit Column Width → apply All Borders. The recorder generates VBA equivalent to:

```vba
Sub FormatIPLMatchSheet()
    Dim ws As Worksheet
    Dim lastRow As Long, lastCol As Long

    Set ws = Sheets("IPL_Matches")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row
    lastCol = ws.Cells(1, ws.Columns.Count).End(xlToLeft).Column

    ' Bold header row
    ws.Range(ws.Cells(1, 1), ws.Cells(1, lastCol)).Font.Bold = True

    ' Autofit all used columns
    ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol)).Columns.AutoFit

    ' Add borders around the whole table
    With ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, lastCol)).Borders
        .LineStyle = xlContinuous
        .Weight = xlThin
    End With
End Sub
```

**Key points:** `End(xlUp)` / `End(xlToLeft)` dynamically find the last used row/column, so the macro works even if match data grows beyond 15 rows — this is the difference between a macro that only works on today's exact data and one that's genuinely reusable, which is what "automation" means in this session's context.

---

## Task 2 — CleanPlaylistData: Remove Duplicates + Trim Extra Spaces

```vba
Sub CleanPlaylistData()
    Dim ws As Worksheet
    Dim lastRow As Long, i As Long

    Set ws = Sheets("Spotify_Playlist")
    lastRow = ws.Cells(ws.Rows.Count, 1).End(xlUp).Row

    ' Trim extra spaces from Track Name (col A) and Artist (col B), skipping the header row
    For i = 2 To lastRow
        ws.Cells(i, 1).Value = Trim(ws.Cells(i, 1).Value)
        ws.Cells(i, 2).Value = Trim(ws.Cells(i, 2).Value)
    Next i

    ' Remove duplicate rows based on Track Name + Artist (columns 1 and 2)
    ws.Range(ws.Cells(1, 1), ws.Cells(lastRow, 3)).RemoveDuplicates Columns:=Array(1, 2), Header:=xlYes
End Sub
```

**Key points:**
- `Trim()` strips leading/trailing spaces from a string — it does **not** collapse repeated spaces in the middle of text, so this specifically fixes the padded values like `"  Blinding Lights "` → `"Blinding Lights"`.
- Trimming happens **before** `RemoveDuplicates`, on purpose: `"Blinding Lights "` and `"Blinding Lights"` look identical to a human but are different strings to Excel, so untrimmed duplicates could slip past the duplicate check entirely.
- `.RemoveDuplicates Columns:=Array(1, 2), Header:=xlYes` is VBA's direct equivalent of the Data tab's Remove Duplicates button — `Array(1,2)` says "treat rows as duplicates only if both Track Name and Artist match."

---

## Task 3 — Button on Flipkart Sheet to Refresh Pivots & Update Charts

**Step 1 — write the macro:**
```vba
Sub RefreshFlipkartDashboard()
    Dim pt As PivotTable
    Dim ws As Worksheet

    On Error Resume Next
    For Each ws In ThisWorkbook.Worksheets
        For Each pt In ws.PivotTables
            pt.RefreshTable
        Next pt
    Next ws
    On Error GoTo 0

    ' Refresh any Power Query connections too, if present
    ThisWorkbook.RefreshAll

    MsgBox "Dashboard refreshed!"
End Sub
```

**Step 2 — add a clickable button on the sheet:**
1. Go to the `Flipkart_Sales` sheet (or `Dashboard`, wherever your PivotTable/PivotChart actually lives).
2. **Developer tab → Insert → Form Controls → Button (Form Control)** (the first rectangle icon under Form Controls, not ActiveX).
3. Click-drag on the sheet to draw the button. The **Assign Macro** dialog pops up automatically — select `RefreshFlipkartDashboard` → **OK**.
4. Right-click the button → **Edit Text** → rename it, e.g., "🔄 Refresh Dashboard."
5. Click anywhere off the button to deselect, then click it once to test — it should refresh every PivotTable in the workbook and show the confirmation message.

**Why `ThisWorkbook.Worksheets` + `ws.PivotTables` (nested loop) instead of just refreshing one PivotTable directly:** a real dashboard often has more than one PivotTable feeding different charts — this pattern refreshes *all* of them across *every* sheet in one click, which is exactly the "update the dashboard charts" requirement, since PivotCharts redraw automatically whenever their underlying PivotTable refreshes.

---

## Task 4 — Export Dashboard Sheet as PDF, With Error Handling

```vba
Sub ExportDashboardToPDF()
    Dim desktopPath As String
    Dim fullPath As String

    On Error Resume Next

    desktopPath = Environ("USERPROFILE") & "\Desktop\"
    fullPath = desktopPath & "Zomato_Sales_Dashboard.pdf"

    Sheets("Dashboard").ExportAsFixedFormat _
        Type:=xlTypePDF, _
        Filename:=fullPath, _
        Quality:=xlQualityStandard, _
        IncludeDocProperties:=True, _
        IgnorePrintAreas:=False, _
        OpenAfterPublish:=False

    If Err.Number <> 0 Then
        MsgBox "Export failed: " & Err.Description, vbCritical
        Err.Clear
    Else
        MsgBox "Dashboard exported successfully to: " & fullPath, vbInformation
    End If

    On Error GoTo 0
End Sub
```

**Key points (per the hint):**
- `On Error Resume Next` tells VBA to keep running instead of crashing on the export line if something goes wrong (e.g., Desktop path doesn't exist, file is open elsewhere and locked, no write permission).
- Immediately after the export attempt, `If Err.Number <> 0 Then` checks whether an error actually happened — this is the "check if the export was successful" the hint asks for; `Err.Number` is 0 when no error occurred.
- `Environ("USERPROFILE") & "\Desktop\"` dynamically resolves to *your* Desktop path rather than a hardcoded `C:\Users\SomeoneElse\Desktop\`, so the macro works on any machine it's run on.
- `Err.Clear` resets the error state after handling it, and `On Error GoTo 0` at the end turns error-resuming back off — good practice so any *later* code in a larger project doesn't silently swallow unrelated errors.

---

## Task 5 — AI-Assisted Macro: Refresh Power Query + Confirmation Message

**Prompt used** (paste-ready, as the task asks you to document):
> "Write a VBA macro in Excel that refreshes all Power Query connections in the current workbook, waits for the refresh to complete, and then shows a message box saying 'Data refreshed successfully!'"

**Resulting code:**
```vba
Sub RefreshPowerQueryData()
    Dim qt As WorkbookConnection

    On Error Resume Next
    For Each qt In ThisWorkbook.Connections
        qt.Refresh
    Next qt
    On Error GoTo 0

    ' Ensure all queries finish before continuing (avoids showing the message too early)
    ThisWorkbook.RefreshAll
    Application.CalculateUntilAsyncQueriesDone

    MsgBox "Data refreshed successfully!"
End Sub
```

**Key points:**
- `ThisWorkbook.Connections` is the collection of every external data connection (including Power Query connections) in the workbook — looping through it refreshes each one individually.
- `Application.CalculateUntilAsyncQueriesDone` is the important safeguard here: Power Query refreshes can run **asynchronously** (in the background), so without this line, VBA might show "Data refreshed successfully!" *before* the refresh has actually finished — this line makes VBA wait until every async query is genuinely done first.
- This mirrors the session's demo goal directly: refresh Power Query → refresh Pivots (Task 3's macro) → apply formatting (Task 1's macro) → export PDF (Task 4's macro) is the full automation chain the case study is building toward, one task at a time.

---

## Summary Table

| Task | VBA Concept Used | Key Statement |
|---|---|---|
| 1 | Recorded macro, dynamic range with `End(xlUp)`/`End(xlToLeft)` | `.Font.Bold`, `.Columns.AutoFit`, `.Borders` |
| 2 | `Trim()`, `RemoveDuplicates` | `ws.Cells(i,1).Value = Trim(...)`; `.RemoveDuplicates Columns:=Array(1,2)` |
| 3 | Form Control Button, nested `For Each`, `PivotTable.RefreshTable` | Developer → Insert → Button (Form Control) |
| 4 | `ExportAsFixedFormat`, `On Error Resume Next`, `Err.Number` | `Sheets(...).ExportAsFixedFormat Type:=xlTypePDF` |
| 5 | AI-assisted code, `WorkbookConnection.Refresh`, async-safe wait | `Application.CalculateUntilAsyncQueriesDone` |
