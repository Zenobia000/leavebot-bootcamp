# cp3-tests：講師參考快照

課程版本2026.10-unified-1；教材基底 `d10995bb6b4e06519fea443d367912f517ce82b7`。建立時間 2026-10-25T08:30:23.965495+00:00。
這是一組講師明確選定的決策與參考實作，不代表所有Agent都能在同樣時間產出。

## 可接續內容
骨架綠、第一個業務測試預期紅；接卡H逐個綠燈

## 實際證據
```text
.                                                                        [100%]
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\python_workspace\github\ai-vibe-coding-beginner\tmp\leavebot-rehearsal\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
1 passed, 1 warning in 0.35s

EXPECTED RED:
.F                                                                       [100%]
================================== FAILURES ===================================
_____________________ test_submit_valid_leave_is_pending ______________________

client = <starlette.testclient.TestClient object at 0x000001AF731C15E0>

    @pytest.mark.req('TC-01','AC-01.1','FR-01')
    def test_submit_valid_leave_is_pending(client):
        r=client.post('/api/leaves',json=valid())
>       assert r.status_code==201
E       assert 405 == 201
E        +  where 405 = <Response [405 Method Not Allowed]>.status_code

backend\tests\acceptance\test_leaves.py:13: AssertionError
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\python_workspace\github\ai-vibe-coding-beginner\tmp\leavebot-rehearsal\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED backend/tests/acceptance/test_leaves.py::test_submit_valid_leave_is_pending
1 failed, 1 passed, 1 warning in 0.32s
```

測試在本機Python3.12的隔離venv執行；原始結果只證明所列案例，不代表已做所有平台／Agent的互動彩排。查閱課程CHECKPOINTS後再接續。
