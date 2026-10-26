# 001 送出並查看自己的請假單

## 成果與範圍

完成一條可操作的主線：選員工 → 填表 → 後端驗證與工作日計算 → SQLite 存為 `pending` → 我的假單。實作 `docs/05-sds.md` 的 API-02 至 API-04、UI-01 與 `rules.leave_days`；依 `docs/02-prd.md` 和 `docs/03-srs.md` 處理拒絕與資料隔離。

## 完成時可檢查

- `docs/06-test-plan.md` 的 TC-01 至 TC-08 逐個依 TDD 紅燈、綠燈；第一個業務紅燈先停下供人確認。
- TC-09 由瀏覽器或人工核對理由只以純文字呈現；沒有操作證據時保持未驗證。
- 成功送出顯示待審核與天數；拒絕輸入不存檔；重新整理及切換員工後列表正確。
- 完整 pytest 結果已回報，追溯表填入實際測試檔與狀態；實際偏差記入 `docs/LESSONS.md`。

## 讀取與驗收

讀 `docs/02-prd.md` 至 `docs/06-test-plan.md`、`course/01-上課/04-STACK.md`。以專案虛擬環境執行 `.venv/bin/python -m pytest`（Windows：`.venv\Scripts\python.exe -m pytest`），再操作成功、拒絕、刷新與換員工流程。不得改測試條件來讓結果通過。

## 依賴與大小

阻塞依賴：000 的可啟動骨架已由人驗收。這是一張完整縱向切片；若超出課堂時段，先報告卡住的接縫，不默默刪除驗收條件。
