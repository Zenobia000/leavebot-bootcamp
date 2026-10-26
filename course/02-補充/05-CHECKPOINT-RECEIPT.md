# cp5-delivered：講師交付參考快照

本快照承接 cp4 的表單主線，卡 J 將理由上限由 200 改為 100；Brief、PRD AC-01.4、SRS FR-04、SDS、TC-10、前後端與 UI 已對齊。歷史變更見 `issues/002-reason-limit.md`。

## 可接續內容

從 [卡 K](../01-上課/prompts/11-K.md) 做交付審查，或於課後對照六份文件、三張票與測試。這是講師參考解法，不要求學員逐字產出相同內容。

## 自動化證據

本次整理後在 Windows Python 3.12.9 的專案 `.venv` 執行 `.venv\Scripts\python.exe -m pytest -q`：**21 passed、1 warning**。TC-10 覆蓋 100 字成功與 101 字拒絕；後者在舊上限時曾預期紅燈，改為 100 後轉綠。原始紅→綠輸出保存在 `docs/DELIVERY.md`，其中絕對路徑是彩排時的環境資訊。

## 瀏覽器證據與界限

先前對同一份未改動的程式以 Playwright Chromium 操作成功送出、反向日期拒絕不存檔、重新整理、切換員工、TC-09 理由純文字呈現、100 字 UI 與 390px 排版。紀錄在 [browser-check.json](../../docs/evidence/browser-check.json) 與兩張截圖。未驗證其他作業系統、其他 Agent 的完整課堂耗時或真人操作。
