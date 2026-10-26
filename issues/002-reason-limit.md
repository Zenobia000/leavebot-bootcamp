# 002 將理由長度上限從 200 改為 100

## 成果與範圍

卡 J 由人確認的需求變更。沿用 `docs/02-prd.md` 的 AC-01.4、`docs/03-srs.md` 的 FR-04；同步更新 `docs/01-brief.md` 的決策、`docs/05-sds.md` 的欄位限制、前端提示與後端驗證。其他請假規則不變。

## 完成時可檢查

- 新增 TC-10：101 個 Unicode 字元理由回 422 且不存檔；先確認舊上限會讓測試紅燈，再改程式轉綠。
- 保留 TC-05 的 201 字元拒絕案例；不刪除或放寬既有測試。
- UI 的輸入上限與文字提示為 100；完整 pytest 通過，瀏覽器操作確認提示及拒絕結果。
- `docs/06-test-plan.md` 的追溯表與 `docs/DELIVERY.md` 記錄實際證據及未驗證項。

## 讀取與驗收

讀 `docs/02-prd.md`、`docs/03-srs.md`、`docs/05-sds.md`、`docs/06-test-plan.md`。以專案虛擬環境執行 `.venv/bin/python -m pytest`（Windows：`.venv\Scripts\python.exe -m pytest`），再操作理由邊界；不要以文件敘述代替實際測試輸出。

## 依賴與大小

阻塞依賴：001 的表單主線與測試已完成。這是單一欄位規則的短時段變更；若發現其他欄位也受影響，先回報再擴大範圍。
