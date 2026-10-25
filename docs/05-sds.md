# 05 SDS — API與資料
| API | 用途 | 回應／錯誤 | 來源 |
|---|---|---|---|
| API-01 GET /api/health | 骨架 | 200 ok | 骨架 |
| API-02 GET /api/employees | 員工選單 | 200 id/name列表 | FR-02 |
| API-03 POST /api/leaves | 送出employee_id/leave_type/start_date/end_date/period/reason | 201假單；422驗證錯誤 | FR-01至05 |
| API-04 GET /api/leaves?employee_id=1 | 個人假單 | 200列表；404未知員工 | FR-06 |
employees(id整數主鍵,name文字)；leaves(id主鍵,employee_id外鍵,leave_type,start_date,end_date,period,reason,days實數,status固定pending)。
假別annual/personal/sick；時段full/am/pm。每次連線開foreign_keys，contextmanager確保關閉。
create_app(database_path=None)先讀LEAVEBOT_DB，測試傳tmp_path。rules.leave_days(start,end,period)為公開計算接縫。
UI-01同頁表單與我的假單，用相對/api、textContent呈現資料；送出期間鎖按鈕，切員工重新查列表。
