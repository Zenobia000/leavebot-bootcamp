# 06 Test Plan — LeaveBot（講師參考）

> 案例的預期值依 `docs/02-prd.md`、`docs/03-srs.md` 與講師教學決策，不從實作函式反推。本快照已完成 TC-01 至 TC-08 的自動化驗證；TC-09 仍待瀏覽器或人工操作。

## 案例

| TC | 需求 | 層級 | 輸入／情境 | 預期結果 | 人工確認 |
|---|---|---|---|---|---|
| TC-01 | AC-01.1、FR-01 | acceptance | 員工 1、`annual`、2026-10-20 整天 | 201；`pending`、1 天；可在員工 1 列表看到 | 依規格核定 |
| TC-02 | AC-01.2、FR-02 | acceptance | 缺少假別 | 422；假單筆數不變 | 依規格核定 |
| TC-03 | AC-01.2、FR-02 | acceptance | 結束日早於開始日 | 422；不存檔 | 依規格核定 |
| TC-04 | AC-01.3、FR-03 | unit | 週五到週一整天、單日工作日上午／下午、跨日半天、全週末 | 前兩類分別為 2 天及 0.5 天；後兩類拒絕 | 依工作日規則核定 |
| TC-05 | AC-01.4、FR-04 | acceptance | 理由 201 個 Unicode 字元 | 422；不存檔 | 依 200 字上限核定 |
| TC-06 | AC-01.5、FR-05 | acceptance | 請求自行帶入 `approved` 或 `days=99` | 422；不存檔 | 依後端決定規則核定 |
| TC-07 | AC-02.1、FR-06、NFR-02 | acceptance | 員工 1 送出後查員工 2，重開 app 再查員工 1；測試使用暫存 DB | 員工 2 為空；員工 1 紀錄持久；開發 DB 不受測試影響 | 依隔離要求核定 |
| TC-08 | AC-01.2、FR-02 | acceptance | 未知員工、非法假別／時段或無效日期 | 422；不存檔 | 依規格核定 |
| TC-09 | NFR-01 | 人工操作 | 理由含 HTML 標記 | 畫面顯示文字，不解析成 HTML | 依安全呈現要求核定 |

## 人工操作

從首頁選員工 1，送出合法假單，核對待審核與天數；重新整理後仍可見。送出反向日期，確認錯誤且列表未新增。切到員工 2，確認看不到員工 1 的假單。以含 HTML 標記的理由送出，確認以純文字顯示。執行時記錄瀏覽器及實際結果；無瀏覽器工具時由人操作。

## 退出條件

- [x] 相關自動化測試實際執行且通過：19 passed（2026-10-27，Windows Python 3.12.9）
- [ ] 成功、拒絕、重新整理與換員工流程經人工或瀏覽器操作核對
- [x] 每條 AC／FR／NFR 已安排 TC；尚未執行者不標通過

## 追溯表（票完成後更新證據）

| 需求 | TC | 測試檔／人工證據 | 狀態 |
|---|---|---|---|
| AC-01.1、FR-01 | TC-01 | `backend/tests/acceptance/test_leaves.py` | 通過 |
| AC-01.2、FR-02 | TC-02、TC-03、TC-08 | `backend/tests/acceptance/test_leaves.py` | 通過 |
| AC-01.3、FR-03 | TC-04 | `backend/tests/unit/test_rules.py` | 通過 |
| AC-01.4、FR-04 | TC-05 | `backend/tests/acceptance/test_leaves.py` | 通過 |
| AC-01.5、FR-05 | TC-06 | `backend/tests/acceptance/test_leaves.py` | 通過 |
| AC-02.1、FR-06 | TC-07 | `backend/tests/acceptance/test_leaves.py` | 通過 |
| NFR-01 | TC-09 | 待人工操作 | 未執行 |
| NFR-02 | TC-07 | `backend/tests/acceptance/test_leaves.py` 使用 `tmp_path` 注入資料庫 | 通過 |

## C4/C5 選用：AI 評測

基本主線不使用模型，不跑 LLM eval。挑戰票啟動後才依 `course/02-補充/fixtures/README.md` 另定 fixture、比較方式、門檻與注入案例。
