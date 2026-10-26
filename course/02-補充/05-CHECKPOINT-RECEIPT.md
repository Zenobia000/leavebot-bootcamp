# cp3-tests：測試起點

骨架已建立；第一個業務測試保留紅燈，供下一階段逐項完成表單功能。六份規格與兩張主線票沿用 cp2 的已確認版本。

## 可接續內容

從 [卡 H](../01-上課/prompts/08-H.md) 第二段接續。先確認 TC-01 的失敗原因，再實作 `POST /api/leaves`；其餘 TC 尚未實作。

## 實際驗證

2026-10-27 於 Windows／Python 3.12.9 執行 `.venv\Scripts\python.exe -m pytest -q`：1 passed、1 failed。唯一失敗為 `backend/tests/acceptance/test_leaves.py::test_submit_valid_leave_is_pending`：預期 201，實際 405，因 POST 端點尚未實作。這是本快照預期的紅燈；TC-02 至 TC-09 與瀏覽器流程尚未驗證。
