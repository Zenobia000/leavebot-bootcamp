# 05 SDS — LeaveBot

> 上游：`docs/04-sad.md`、`docs/03-srs.md`。欄位及介面供測試案例與兩張主線票引用。

文件狀態：已確認；負責人／審查者：LeaveBot 小組。

## 目錄

- [資料模型與不變量](#資料模型與不變量)
- [API 契約](#api-契約)
- [UI 與模組契約](#ui-與模組契約)
- [變更與未決](#變更與未決)

## 資料模型與不變量

員工名單供選擇，假單由後端驗證後寫入。`days` 和 `status` 由後端產生，客戶端不能指定。欄位約束如下：

| 表／欄位 | 型別與允許值 | 預設／限制 | 來源 FR |
|---|---|---|---|
| `employees.id`, `name` | 整數主鍵、文字 | 員工名單；`name` 非空 | FR-02、FR-06 |
| `leaves.id`, `employee_id` | 整數主鍵、外鍵 | `employee_id` 必須存在；開啟 SQLite foreign keys | FR-01、FR-02、FR-06 |
| `leaves.leave_type`, `period` | 文字；`annual/personal/sick`、`full/am/pm` | 不接受其他值 | FR-02、FR-03 |
| `leaves.start_date`, `end_date` | `YYYY-MM-DD` 日期文字 | 結束日不得早於開始日 | FR-02、FR-03 |
| `leaves.reason` | 文字 | 選填，預設空字串；最多 100 個 Unicode 字元 | FR-04 |
| `leaves.days`, `status` | 數值、文字 | 由後端計算天數；新假單固定 `pending`，不接受客戶端指定 | FR-01、FR-03、FR-05 |

每次 SQLite 連線開啟 foreign keys；正常結束 commit，例外 rollback，最後關閉。拒絕的輸入不得新增假單；資料庫失敗時不得向畫面回報成功。

## API 契約

### API-01｜`GET /api/health`

骨架連線檢查；無輸入，成功回 200 與 `{"status":"ok"}`。服務不可連線時，前端顯示連線失敗。

### API-02｜`GET /api/employees`（FR-06）

無輸入，成功回 200 與員工 `id/name` 清單，例如 `[{"id":1,"name":"小安"}]`。讀取失敗時前端顯示錯誤。

### API-03｜`POST /api/leaves`（FR-01 至 FR-05）

接受 `employee_id`、`leave_type`、`start_date`、`end_date`、`period`，`reason` 選填。最小 JSON 請求：

```json
{"employee_id":1,"leave_type":"annual","start_date":"2026-10-20","end_date":"2026-10-20","period":"full","reason":""}
```

成功回 201，包含伺服器產生的 `id`、`days: 1`、`status: "pending"` 及原始有效欄位。業務驗證錯誤回 422 與 `{"detail":"可讀訊息"}`，框架解析錯誤可能回結構化 `detail`；前端需提供通用錯誤回饋，假單筆數不變；`days`、`status` 等多餘欄位也拒絕。員工看到的那一句，以 SRS 預期結果表為準。相同有效請求再次送出會新增另一筆，沒有冪等鍵。

### API-04｜`GET /api/leaves?employee_id=<id>`（FR-06）

依員工 ID 回 200 與該員工清單；沒有資料回空陣列，未知員工回 404。本版未定義清單排序契約。

## UI 與模組契約

- UI-01｜同頁表單與我的假單（US-01、US-02、NFR-01）：選員工、填表、送出、顯示錯誤或待審核；重新整理或切員工後重查列表。呼叫 API-02 至 API-04；理由用 `textContent`。
- `create_app(database_path=None)`（NFR-02）：初始化資料庫與路由；預設從 `LEAVEBOT_DB` 取得路徑，測試注入暫存路徑。
- `rules.leave_days(start,end,period)`（FR-03）：含起迄日計算週一至週五；合法單日半天為 0.5，非法組合拋出規則錯誤，由 API-03 處理。

## 變更與未決

從空資料庫初始化，沒有既有資料遷移。本版尚未設計正式使用時的 API 相容性、備份和資料保留；若部署須先補決策。

