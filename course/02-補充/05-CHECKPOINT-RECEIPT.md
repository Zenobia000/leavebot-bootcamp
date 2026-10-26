# cp5-delivered：交付快照

本快照承接 cp4 的表單主線。卡 J 將理由上限由 200 字改為 100 字，Brief、PRD AC-01.4、SRS FR-04、SDS、TC-10、前後端與 UI 已對齊。變更紀錄見 `issues/002-reason-limit.md`。

## 接續方式

從 [卡 K](../01-上課/prompts/11-K.md) 做交付審查，也可對照六份文件、疊代票與測試證據。

## 驗證結果

在 Windows Python 3.12.9 的專案 `.venv` 執行 `.venv\Scripts\python.exe -m pytest -q`：21 passed、1 warning。TC-10 驗證 100 字成功與 101 字拒絕。測試執行紀錄見 `docs/DELIVERY.md`。

Playwright Chromium 曾驗證成功送出、反向日期拒絕且不存檔、重新整理、切換員工、TC-09 理由純文字呈現、100 字 UI 與 390px 排版。紀錄見 [browser-check.json](../../docs/evidence/browser-check.json) 與截圖。其他作業系統與真人操作尚未驗證。
