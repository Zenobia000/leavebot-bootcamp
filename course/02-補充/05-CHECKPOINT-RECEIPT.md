# cp4-working-feature：講師參考快照

本快照沿用依模板整理的六份文件與兩張主線票；表單、後端驗證、SQLite 與我的假單已接通。自動化測試通過，瀏覽器操作驗收仍待核對。

## 可接續內容
表單主線與自動化測試綠；從 [卡 I](../01-上課/prompts/09-I.md)、[卡 J](../01-上課/prompts/10-J.md) 接續，或先由人操作驗收。

## 實際證據
```text
...................                                                      [100%]
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\python_workspace\github\ai-vibe-coding-beginner\tmp\leavebot-rehearsal\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
19 passed, 1 warning in 0.63s
```

本次整理後以 Windows Python 3.12.9 的專案 `.venv` 重跑 `.venv\Scripts\python.exe -m pytest -q`：**20 passed、1 warning**。新增 TC-05 的 200 字成功邊界，保留 201 字拒絕；測試結果只證明自動化案例。TC-09 的瀏覽器純文字操作與其他平台的課堂耗時尚未驗證。
