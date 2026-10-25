# cp5-delivered：講師參考快照

課程版本2026.10-unified-1；教材基底 `d10995bb6b4e06519fea443d367912f517ce82b7`。建立時間 2026-10-25T08:30:27.650133+00:00。
這是一組講師明確選定的決策與參考實作，不代表所有Agent都能在同樣時間產出。

## 可接續內容
需求變更紅→綠與交付參考；瀏覽器證據後補

## 實際證據
```text
.............F......                                                     [100%]
================================== FAILURES ===================================
__________________________ test_new_reason_limit_100 __________________________

client = <starlette.testclient.TestClient object at 0x0000027E45BB36E0>

    @pytest.mark.req('TC-10','AC-01.4','FR-04')
    def test_new_reason_limit_100(client):
>       assert client.post('/api/leaves',json=valid(reason='�r'*101)).status_code==422
E       AssertionError: assert 201 == 422
E        +  where 201 = <Response [201 Created]>.status_code
E        +    where <Response [201 Created]> = post('/api/leaves', json={'employee_id': 1, 'leave_type': 'annual', 'start_date': '2026-10-20', 'end_date': '2026-10-20', ...})
E        +      where post = <starlette.testclient.TestClient object at 0x0000027E45BB36E0>.post
E        +      and   {'employee_id': 1, 'leave_type': 'annual', 'start_date': '2026-10-20', 'end_date': '2026-10-20', ...} = valid(reason=('�r' * 101))

backend\tests\acceptance\test_leaves.py:54: AssertionError
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\python_workspace\github\ai-vibe-coding-beginner\tmp\leavebot-rehearsal\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
=========================== short test summary info ===========================
FAILED backend/tests/acceptance/test_leaves.py::test_new_reason_limit_100 - A...
1 failed, 19 passed, 1 warning in 0.53s

GREEN:
....................                                                     [100%]
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\python_workspace\github\ai-vibe-coding-beginner\tmp\leavebot-rehearsal\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
20 passed, 1 warning in 0.46s
```

測試在本機Python3.12的隔離venv執行；原始結果只證明所列案例，不代表已做所有平台／Agent的互動彩排。查閱課程CHECKPOINTS後再接續。
