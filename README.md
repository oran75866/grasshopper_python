# Grasshopper GhPython 工具集

GHPython scripts for Grasshopper / Rhino 8 (Python 3.9 RhinoCode Runtime).

本 repo 收錄用於 Grasshopper 開發的 GhPython 工具腳本，依功能分類整理，可直接貼入 Python 3 Script 元件使用。

## Environment

- Rhino 8 (SR6+)
- Grasshopper (built-in)
- Python 3.9 — RhinoCode Runtime
- RhinoCommon API 8.6

---

## 資料夾結構

| 資料夾 | 說明 |
|--------|------|
| `data_tree/` | DataTree 操作工具（分支、路徑、重組等）|
| `geometry/` | 幾何運算工具（曲線、曲面、點雲等）|
| `list_tools/` | List 資料處理工具（排序、篩選、分群等）|
| `io/` | 資料輸入輸出工具（CSV、JSON、文字等）|

---

## Scripts

### `group_curves_by_shape.py` — Group Curves by Shape

將具有樓層資料結構的曲線，依照形狀重新分組，同時保留樓層結構。

**使用情境**

當你有一棟建築的各樓層輪廓線（已依樓高分好 branch），想將相同形狀的輪廓線歸為同一群組時使用。

**判斷邏輯**

以曲線長度中點（Curve Middle Point）的 XY 座標作為形狀識別依據。在建築平面的應用情境下，相同形狀的輪廓線在各樓層的 XY 位置相同，僅 Z 值（樓高）不同，因此只比較 XY 即可正確識別形狀。

**Inputs**

| 名稱 | 型態 | 說明 |
|------|------|------|
| `x` | DataTree (Curve) | 依樓層組織的曲線資料樹，path = 樓層索引 |
| `tol` | float | 座標比對容差，預設 `1.0`（模型單位）|

**Outputs**

| 名稱 | 型態 | 說明 |
|------|------|------|
| `a` | DataTree (Curve) | 重新分組後的曲線，path = `{shape_id; floor_idx}` |

**資料結構示意**

輸入（依樓層）：
```
{0}  →  (空)
{1}  →  [輪廓A, 輪廓B]
{2}  →  [輪廓A, 輪廓B]
...
{9}  →  [輪廓A, 輪廓B]
{10} →  (空)
```

輸出（依形狀 × 樓層）：
```
{0; 1}  →  輪廓A @ 樓層1
{0; 2}  →  輪廓A @ 樓層2
...
{1; 1}  →  輪廓B @ 樓層1
{1; 2}  →  輪廓B @ 樓層2
...
```

**參數調整**

- `tol` 調大：容許更大的座標誤差，適合模型座標非整數的情況
- `tol` 調小：更嚴格的形狀比對，避免不同形狀被誤判為同一群
