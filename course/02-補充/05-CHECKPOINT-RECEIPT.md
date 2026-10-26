# cp3-tests：講師參考快照

本快照沿用已整理的六份規格與兩張主線票。骨架已建立；第一個業務測試刻意保留紅燈，供課堂逐個行為完成 TDD。

## 可接續內容
骨架 health 應為綠燈，TC-01 因 `POST /api/leaves` 尚未實作而預期回 405。從 [卡 H](../01-上課/prompts/08-H.md) 的第二段接續，先確認紅燈原因再實作。

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

以上為原始彩排證據。本次整理後以 Windows Python 3.12.9 的專案 `.venv` 重跑 `.venv\Scripts\python.exe -m pytest -q`：**1 passed、1 failed**；唯一失敗是 TC-01 的 `POST /api/leaves` 回 405，符合本快照預期紅燈。不代表 TC-02 至 TC-09 或瀏覽器流程已驗證。
