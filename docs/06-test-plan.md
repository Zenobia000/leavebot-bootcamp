# 06 Test Plan — 代表案例
| TC | 需求 | 情境 | 預期 |
|---|---|---|---|
| TC-01 | AC-01.1 FR-01 | 合法一天 | 201 pending 1天 |
| TC-02 | AC-01.2 FR-02 | 缺假別 | 422且筆數不變 |
| TC-03 | AC-01.2 FR-02 | 反向日期 | 422且不存檔 |
| TC-04 | AC-01.3 FR-03 | 跨週末、單日半天、非法半天、全週末 | 天數正確或拒絕 |
| TC-05 | AC-01.4 FR-04 | 201字理由 | 拒絕且不存檔 |
| TC-06 | AC-01.5 FR-05 | 自帶approved或days | 拒絕且不存檔 |
| TC-07 | AC-02.1 FR-06 | 切員工、重開app | 持久且資料隔離 |
| TC-08 | AC-01.2 FR-02 | 非法員工／假別／時段 | 拒絕且不存檔 |
| TC-09 | NFR-01 | 理由有HTML字串 | 當文字顯示 |
退出：pytest綠；瀏覽器成功、拒絕、刷新與換員工有證據。不跑LLM eval。
追溯：TC01/02/03/05/06/07/08 → backend/tests/acceptance/test_leaves.py；TC04 → backend/tests/unit/test_rules.py。上述已執行綠；TC09瀏覽器純文字驗收待操作，不標通過。
