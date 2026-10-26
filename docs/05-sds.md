# 05 SDS — LeaveBot（講師參考）

> 上游：`docs/04-sad.md`、`docs/03-srs.md`。欄位及介面供測試案例與兩張主線票引用。

## 資料

| 表／欄位 | 型別與允許值 | 預設／限制 | 來源 FR |
|---|---|---|---|
| `employees.id`, `name` | 整數主鍵、文字 | 兩筆虛構員工；`name` 非空 | FR-02、FR-06 |
| `leaves.id`, `employee_id` | 整數主鍵、外鍵 | `employee_id` 必須存在；開啟 SQLite foreign keys | FR-01、FR-02、FR-06 |
| `leaves.leave_type`, `period` | 文字；`annual/personal/sick`、`full/am/pm` | 不接受其他值 | FR-02、FR-03 |
| `leaves.start_date`, `end_date` | `YYYY-MM-DD` 日期文字 | 結束日不得早於開始日 | FR-02、FR-03 |
| `leaves.reason` | 文字 | 選填，預設空字串；最多 100 個 Unicode 字元 | FR-04 |
| `leaves.days`, `status` | 數值、文字 | 由後端計算天數；新假單固定 `pending`，不接受客戶端指定 | FR-01、FR-03、FR-05 |

## API

| 編號 | 方法／路徑 | 輸入 | 成功結果 | 錯誤碼與結果 | 來源 FR |
|---|---|---|---|---|---|
| API-01 | `GET /api/health` | 無 | 200，`{"status":"ok"}` | 服務無法連線時由前端顯示連線失敗 | 骨架 |
| API-02 | `GET /api/employees` | 無 | 200，`id/name` 清單 | 讀取失敗時不顯示虛構成功 | FR-06 |
| API-03 | `POST /api/leaves` | JSON：`employee_id`、`leave_type`、`start_date`、`end_date`、`period`，選填 `reason` | 201，含 `id`、後端計算 `days` 與 `pending` 的假單 | 欄位、員工或規則錯誤回 422 且不新增資料；`days/status` 等多餘欄位也回 422 | FR-01 至 FR-05 |
| API-04 | `GET /api/leaves?employee_id=<id>` | 員工 ID | 200，該員工假單清單 | 未知員工回 404 | FR-06 |

## 畫面與模組

| 畫面／模組 | 顯示或負責的行為 | 呼叫 API／介面 | 來源 |
|---|---|---|---|
| UI-01 同頁表單與我的假單 | 選員工、填表、送出、顯示錯誤或待審核；重新整理或切員工後重查列表；理由用 `textContent` | API-02、API-03、API-04 | US-01、US-02、NFR-01 |
| `create_app(database_path=None)` | 初始化資料庫及路由；預設路徑從 `LEAVEBOT_DB` 取得，測試注入暫存路徑 | SQLite 接縫 | NFR-02 |
| `rules.leave_days(start,end,period)` | 含起迄日計算週一至週五；合法單日半天為 0.5，非法組合丟出規則錯誤 | API-03 | FR-03 |

每次 SQLite 連線開啟 foreign keys；正常結束 commit，例外 rollback，最後關閉。資料庫意外失敗不應新增假單或向畫面回報成功。
