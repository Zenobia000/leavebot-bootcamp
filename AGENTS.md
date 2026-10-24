# LeaveBot —— agent 工作規則

> Claude Code 透過 `CLAUDE.md`（只有一行 `@AGENTS.md`）讀這一份；Codex 直接讀。每個設定檔各管什麼，見 `course/HARNESS.md`。
> **上半段是原廠規則**，課程給的，不要改。**下半段是本專案**，你們在 D2 拆票時寫，之後一路長大。

---

# 原廠規則

## 這個 repo 一開始是空地

除了 `course/` 和設定檔，什麼程式都沒有。`docs/`、`diagrams/`、`issues/`、`backend/`、`pyproject.toml` 都由你依規格生成。

| 檔案 | 回答 |
|---|---|
| `course/LEAVEBOT.md` | 題目、公司規章（課堂假設，不是勞動法規）、MVP 範圍 |
| `course/STACK.md` | 固定的技術棧、套件白名單、紅線、骨架怎麼生、進階挑戰的模型規定 |
| `course/templates/` | 六份規格模板、追溯規則、經驗紀錄模板 |
| `course/examples/it-asset/` | 另一個題目寫好的六份文件，看深度用，**不要照抄** |
| `course/fixtures/` | 進階挑戰 C4 的 eval 句子 |
| `docs/01-brief.md` … `docs/06-test-plan.md` | 這個專案的規格。`06` 最後有追溯矩陣 |
| `docs/LESSONS.md` | 這個專案的經驗：偏差、誤解、踩過的坑 |
| `diagrams/` | 流程圖、架構圖（Archify 或 Mermaid） |
| `issues/` | D2 的票：`000-skeleton`、`001-submit-leave`，進階挑戰另開 |
| `playground/` | D1 的練習區，不進版控。**不受 `course/STACK.md` 限制，也不用寫測試** |

## 規格和你的產出不一致時

1. **以規格為準**（`docs/`、`course/STACK.md`），不要自己決定哪邊對，也不要為了讓產出成立去改規格。
2. 規格沒寫到、或兩份文件互相衝突：**停下來問**。
3. 發現了偏差就記進 `docs/LESSONS.md` 的「偏差紀錄」：講義／規格說什麼、你實際做了什麼、怎麼對齊。

## 每張票結束前

- 跑過 `.venv/bin/pytest` 並貼出結果，才能說「完成」。
- 更新 `docs/06-test-plan.md` 的追溯矩陣：這張票的 TC 由哪個測試檔驗過。
- 這張票裡有任何偏差、誤解或踩坑，補進 `docs/LESSONS.md`。

一律用 `.venv/bin/python`、`.venv/bin/pytest`（Windows：`.venv\Scripts\python`）。你的 shell 不會自動啟用 venv，很多機器上也沒有 `python` 這個指令。

## 紅線

- **照 `course/STACK.md`。** 不換框架、不加白名單外的套件、不開 CORS、不在前端寫死後端位址。要例外，先問。
- 驗證一定在後端做；SQL 一律用參數，不准字串拼接。
- 測試不准碰開發用的資料庫，也不准依賴真實時鐘（「今天」從 `LEAVEBOT_TODAY` 讀）。
- 每個測試標註它實作的 TC 與驗的需求：`@pytest.mark.req("TC-03", "AC-01.1")`。
- 不准修改或刪除測試來讓測試通過。
- API key 只放 `.env`，不准寫進任何其他檔案。
- 套件（FastAPI、Anthropic SDK）的寫法不確定時，用 context7 查文件，不要憑記憶寫。

### 進階挑戰 C4、C5 起才適用

- **模型只透過 Anthropic API 呼叫**，不准拿 `claude -p`、`codex exec` 這類 agent CLI 當後端。
- 測試**不准呼叫真的模型**，一律注入假的實作。
- 剩餘天數、撞期檢查、核准，**一律由程式碼或人決定**，不採用模型給的任何數字或狀態。
- 模型的輸出必須通過格式驗證才能存進資料庫。

---

# 本專案

> D2 拆票時填（至少一條）。範本在 `course/templates/agent-rules/`。只寫**這個專案**才有的規則，每一條都要能檢查。
> `docs/LESSONS.md` 裡同一類問題出現第二次，就升級成這裡的一條規則。

＜例：天數一律由 `leave_days()` 計算，API 不接受前端傳來的天數（SDS 的模組段）＞
