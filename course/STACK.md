# STACK —— 技術棧與邊界（固定，不要讓 agent 換）

> 一天要從需求做到測試通過，**選型的時間省下來給規格和測試**。
> 這一頁是規格，不是程式碼：這個 repo 裡沒有任何預先寫好的程式，`backend/`、套件設定都由你們的 agent 照這一頁生成。
> 生成的結果和這一頁不一樣時，**以這一頁為準**，把差異記進 `docs/LESSONS.md`。
> 想在這些邊界之外做選擇，寫進 `docs/04-sad.md` 的 ADR，並先問講師。

## 固定的部分

| 層 | 用什麼 | 位置 |
|---|---|---|
| 前端 | 純 HTML ＋ 原生 JavaScript ＋ 一份 CSS，**不用任何框架、不用 Node** | `backend/app/static/` |
| 後端 | Python 3.12、FastAPI、標準庫 `sqlite3`、pytest | `backend/` |
| 資料庫 | SQLite 單一檔案 `backend/data/leavebot.db`（不進版控） | — |
| 前後端怎麼接 | FastAPI 把 `static/` 掛在 `/`，API 一律在 `/api` 底下。**同一個來源**，所以不用 CORS | — |

只有一個程式要跑，只需要裝 Python。版本是講師在 2026-10-16 實測過的組合（Python 3.12）。換版本前先問 —— 版本漂移是最常見的卡關原因。

## 紅線

- 不換框架、不加白名單外的套件、不開 CORS。
- 前端一律呼叫相對路徑 `/api/...`，不寫死 `http://127.0.0.1:8000`。
- 驗證一定在後端做。前端可以先擋一次讓使用者體驗好，但**後端不能相信前端**。
- SQL 一律用參數（`?`），不准用字串拼接。

## 骨架怎麼生（D2 單元 11，票 `issues/000-skeleton.md`）

**1. 套件設定 `pyproject.toml`**（根目錄）。讓 agent 生成，必須符合：

| 項目 | 規定 |
|---|---|
| `requires-python` | `>=3.11` |
| `dependencies` | **只有** `fastapi>=0.115`、`uvicorn>=0.30`、`httpx>=0.27`。這就是白名單 |
| 開發用 `[dev]` | `pytest>=8.0` |
| 進階挑戰用 `[ai]` | `anthropic>=1.0`。只有做進階挑戰 C4 才加，基本範圍不需要 |
| pytest | `testpaths = ["backend/tests"]`、`pythonpath = ["backend"]`、`addopts = "--import-mode=importlib"`（不同層級有同名測試檔也不會撞名）、登記 marker `req` |

裝法：

```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"        # Windows：.venv\Scripts\pip install -e ".[dev]"
```

之後一律用 `.venv/bin/python`、`.venv/bin/pytest`、`.venv/bin/uvicorn`（Windows：`.venv\Scripts\…`）—— agent 的 shell 不會自動啟用 venv。

**2. 後端**：讓 agent 依 `docs/05-sds.md` 生成，結構固定成：

```text
backend/
├── app/
│   ├── main.py        ← 一定要有 `app = FastAPI()`；所有路由都在 /api 底下；最後把 static/ 掛在 /
│   ├── static/        ← index.html、app.js、style.css
│   └── …              ← 其他模組依 SDS 拆（例：驗證規則、資料存取）
├── data/              ← SQLite 檔，不進版控
└── tests/
    ├── acceptance/    ← 驗 PRD 的 AC：用 FastAPI 的 TestClient 打 API
    └── unit/          ← 驗規則模組：不碰 HTTP、不碰資料庫
```

掛靜態檔要放在**所有 API 路由之後**，不然 `/` 會把 `/api/...` 吃掉：

```python
app.mount("/", StaticFiles(directory=Path(__file__).parent / "static", html=True), name="static")
```

**3. 啟動**（在 repo 根目錄）：

```bash
.venv/bin/uvicorn app.main:app --app-dir backend --reload
```

瀏覽器開 `http://127.0.0.1:8000/`。port 被佔用就加 `--port 8001`。Ctrl+C 結束。

**4. 驗收骨架**：首頁打開後，用 `fetch("/api/health")` 讀到回應並顯示在畫面上；`.venv/bin/pytest` 全綠（只有一個 health 測試）。**骨架不寫任何請假邏輯。**

## 測試資料與資料庫

- 資料庫檔案的位置從環境變數 `LEAVEBOT_DB` 讀，沒設才用 `backend/data/leavebot.db`。測試一律用暫存資料夾裡的檔案，**不准碰開發用的資料庫**。
- 員工名單（下拉選單用）在啟動時寫入幾筆預設資料，寫法依 SDS。

## 今天是幾號：固定成課程日期

課程情境與公司規章的「今天」都是 **2026-10-12（週一）**。後端任何用到「今天」的地方（不可早於今天、送出期限），**一律從環境變數 `LEAVEBOT_TODAY` 讀**，沒設才用真實日期。

不這樣做的話：彩排時一張 10/23 的假單，過了那天就被「不可早於今天」擋下，demo 走不通。測試也一樣，不准依賴真實時鐘。

## 套件

只能用上面白名單裡的。前端不裝任何東西。要加，先問。

## 不做

登入（員工用下拉選單切換身分）、通知、部署、Docker、ORM、前端框架、前端自動化測試。
這些都是真實系統需要的東西，**但不是這兩天要練的東西**。想做的話寫進 `docs/01-brief.md` 的 non-goal，那也是一種決策。

## 測試

在 repo 根目錄跑 `.venv/bin/pytest`。每個測試標註它實作哪個測試案例、驗哪條需求：

```python
@pytest.mark.req("TC-03", "AC-01.2")
def test_end_date_before_start_date_is_rejected(client): ...
```

每做完一張票，更新 `docs/06-test-plan.md` 的追溯矩陣：哪個 TC 由哪個測試檔驗過。規則見 `templates/TRACEABILITY.md`。

---

## 進階挑戰 C4、C5 才適用：呼叫模型

基本範圍**沒有 LLM**。做進階挑戰「一句話 AI 解析」時才加上這一段的規定。

- **模型一律透過 Anthropic API 呼叫。不准**用 `claude -p`、`codex exec` 這類 agent CLI 當後端 —— 它們帶著執行指令的工具，被注入攻擊時能在你的電腦上動手。API 呼叫沒有工具，最壞只是答錯。
- API key 只放 `.env`（變數 `ANTHROPIC_API_KEY`），不准寫進任何其他檔案。從 `.env` 讀 `ANTHROPIC_API_KEY` 與 `LLM_MODEL`；模型選哪個、為什麼，寫進 SAD 的 ADR。
- 測試**不准呼叫真的模型**。業務程式只依賴一個 `complete(system, user) -> str` 的介面，測試注入假的實作。
- 設逾時上限，數字依 Test Plan（用整份 eval 集量，不要拿一句話量）。
- 模型的輸出**必須通過格式驗證**才能往下走；剩餘天數、撞期、核准一律由程式碼或人決定，不採用模型給的任何數字或狀態。
- SDK 的用法不確定時，請 agent 用 context7 查官方文件，不要憑記憶寫。

### 解析合約（C4 固定，不要改）

```text
POST /api/parse
  request:  {"sentence": "下週三下午看牙醫", "today": "2026-10-12"}
  response: {"requests": [{"start_date", "end_date", "period", "leave_type", "days", …}], "clarify": false}
```

欄位定義見 `fixtures/README.md`。它是**只解析、不存檔**的 API，解析結果要讓員工看過、改過，再走基本範圍的送出 API。
固定它的唯一理由：eval 要用同一份句子集、同一套比對規則（見 `templates/06-test-plan.md` 的「AI 驗收」）幫每一組量準確率。
