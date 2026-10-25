# cp4-working-feature：講師參考快照

課程版本2026.10-unified-1；教材基底 `d10995bb6b4e06519fea443d367912f517ce82b7`。建立時間 2026-10-25T08:30:25.151388+00:00。
這是一組講師明確選定的決策與參考實作，不代表所有Agent都能在同樣時間產出。

## 可接續內容
表單主線與自動化測試綠；接卡I/J或人工驗收

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

測試在本機Python3.12的隔離venv執行；原始結果只證明所列案例，不代表已做所有平台／Agent的互動彩排。查閱課程CHECKPOINTS後再接續。
