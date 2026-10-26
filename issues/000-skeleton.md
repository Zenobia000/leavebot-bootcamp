# 000 建立可啟動的表單骨架

## 成果與範圍

依 `course/01-上課/04-STACK.md` 建立 `pyproject.toml`、FastAPI、HTML／CSS／原生 JavaScript 首頁及 `GET /api/health`。首頁顯示 health 狀態；不加入請假業務邏輯。

## 完成時可檢查

- 使用專案 `.venv` 安裝並啟動後，瀏覽器打開首頁可看到 health 成功。
- `GET /api/health` 回傳 200 與連線狀態；health 測試通過，完整 pytest 結果已回報。
- 停止後能重新啟動；不含測試資料庫或秘密於版控。

## 讀取與驗收

讀 `docs/04-sad.md` 的系統邊界、`docs/05-sds.md` 的 API-01，以及 STACK 的骨架要求。依 STACK 的虛擬環境指令啟動與執行 `.venv/bin/python -m pytest`（Windows：`.venv\Scripts\python.exe -m pytest`），再人工核對首頁。骨架健康檢查不是業務 TC；TC-01 至 TC-09 留給 001。

## 依賴與大小

阻塞依賴：無；設計文件是輸入，不是另一張票。預估一個課堂短時段，完成後由人驗收才開始 001。
