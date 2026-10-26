# 交付參考

依 `course/01-上課/04-STACK.md` 安裝、啟動與測試。預設網址 `http://127.0.0.1:8000/`；測試資料庫獨立，不含應用程式內 LLM 或登入。下方紅→綠與套件清單是原始彩排紀錄，其中絕對路徑屬當時環境，執行指令以目前 STACK 為準。

卡 J 先新增「101 字必須拒絕」的測試。上限還是 200 時，這條是紅的，下面貼的就是那次紀錄。接著程式改成 100 字，前後端和畫面上的字數提示都改了。這份快照的上限是 100。收據寫的完整結果是 21 passed、1 warning。下面綠燈原文是 20 passed，那是還沒加上「100 字可以登記」之前的一次執行，和 21 不是同一次。瀏覽器證據沿用先前的 Chromium 彩排，見 `docs/evidence/browser-check.json`。
## 需求變更的實際紅燈
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

```
## 改成 100 字之後、補上成功邊界之前的綠燈
```text
....................                                                     [100%]
============================== warnings summary ===============================
.venv\Lib\site-packages\fastapi\testclient.py:1
  D:\python_workspace\github\ai-vibe-coding-beginner\tmp\leavebot-rehearsal\.venv\Lib\site-packages\fastapi\testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
    from starlette.testclient import TestClient as TestClient  # noqa

-- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
20 passed, 1 warning in 0.46s

```
## 實測套件
```json
[{"name": "annotated-doc", "version": "0.0.5"}, {"name": "annotated-types", "version": "0.8.0"}, {"name": "anyio", "version": "4.15.1"}, {"name": "certifi", "version": "2026.10.23"}, {"name": "click", "version": "8.5.0"}, {"name": "colorama", "version": "0.4.6"}, {"name": "fastapi", "version": "0.162.0"}, {"name": "h11", "version": "0.16.0"}, {"name": "httpcore", "version": "1.0.9"}, {"name": "httpx", "version": "0.28.1"}, {"name": "idna", "version": "3.20"}, {"name": "iniconfig", "version": "2.3.1"}, {"name": "leavebot-classroom", "version": "0.1.0", "editable_project_location": "D:\\python_workspace\\github\\ai-vibe-coding-beginner\\tmp\\leavebot-rehearsal"}, {"name": "opentelemetry-api", "version": "1.45.1"}, {"name": "packaging", "version": "26.3"}, {"name": "pip", "version": "24.3.1"}, {"name": "pluggy", "version": "1.7.0"}, {"name": "pydantic", "version": "2.14.1"}, {"name": "pydantic_core", "version": "2.50.1"}, {"name": "Pygments", "version": "2.21.0"}, {"name": "pytest", "version": "9.1.1"}, {"name": "starlette", "version": "1.10.0"}, {"name": "typing_extensions", "version": "4.16.0"}, {"name": "typing-inspection", "version": "0.4.4"}, {"name": "uvicorn", "version": "0.54.0"}]

```
瀏覽器自動操作已完成：成功送出、反向日期拒絕且未新增、重新整理、切換員工、理由HTML以純文字呈現、100字UI與390px排版。證據見 docs/evidence/browser-check.json 與兩張截圖；這不是其他平台或真人操作的驗證。不同OS及不同Agent的完整課堂耗時未量測。
