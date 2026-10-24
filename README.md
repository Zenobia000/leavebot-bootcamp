# LeaveBot —— SDD × AI Coding Agent 實戰營上課 repo

> **這是一片空地。** D1 你們在這裡學會駕馭 Claude Code；D2 從需求開始寫規格，再讓 agent 照規格把請假功能從 0 長出來。
> 題目：員工填一張請假單，系統照規則檢查、存起來、顯示狀態。做完的組可以挑戰「一句話請假」的 AI 解析。
> 講義在課程網站（講師會給網址）。

```text
leavebot-bootcamp/
├── README.md  AGENTS.md  CLAUDE.md   ← 你在這裡；AGENTS.md 是 agent 的規則
├── course/                           ← 課程給的：題目、技術棧、模板、範例、eval 句子
└── .claude/ .mcp.json                ← agent 的設定，打開工具就生效，不用動（.agents/ .codex/ 給 Codex 用）
```

你們會長出來的：`docs/`（六份規格＋經驗紀錄）、`diagrams/`（流程圖）、`issues/`（票）、`backend/`、`pyproject.toml`。
D1 的練習放在 `playground/`，不進版控。

## 課前（開課前一週做完）

1. **拿到 repo**：每組 fork，**取消勾選「Copy the `main` branch only」**（不然拿不到講師的 checkpoint 分支），再 clone 自己的那一份。
2. **裝工具**：Git、Python 3.12、Claude Code；Node 18 以上（只給畫圖的 Archify 用，沒裝也能完成主線）。細節照講義的「課前準備」。
3. **讀題目**：[`course/LEAVEBOT.md`](./course/LEAVEBOT.md)。
4. **確認接上了**：在 repo 根目錄打開 `claude`，打 `/compass`，看得到技能表就完成。第一次開會問要不要啟用專案的 MCP，選同意。

**一律在 repo 根目錄啟動 agent**。在子目錄啟動，護欄不會生效。

選用：
- **Anthropic API key**：只有進階挑戰 C4、C5（一句話 AI 解析）需要。
- **用 Codex 的人**：Windows 先跑 `git config --global core.symlinks true` 再 clone，否則 Codex 找不到技能。講義以 Claude Code 示範。

## 卡住了：切到 checkpoint 分支

講師彩排時把 D2 從頭做過一次，每個檢查點留了一個分支。落後超過 15 分鐘就切過去接著做，原本的進度留在原分支：

```bash
git remote add upstream https://github.com/Zenobia000/leavebot-bootcamp.git   # 只要做一次
git fetch upstream
git switch -c rescue-cp2 upstream/cp2-design
```

| 分支 | 時間 | 切過去之後做什麼 |
|---|---|---|
| `cp1-requirements` | 10:30 | 寫 SRS |
| `cp2-design` | 12:30 | 寫 Test Plan |
| `cp3-tests` | 14:15 | 做新增請假的切片 |
| `cp4-working-feature` | 15:00 | 除錯與需求變更 |
| `cp5-delivered` | 17:00 | 參考：完整交付長什麼樣 |
| `advanced-ai-parse` | — | 參考：進階挑戰 C4、C5 |

切過去是讓你們接著做，不是對答案。

## 想知道更多

| 想知道 | 看 |
|---|---|
| agent 的設定檔各管什麼、11 個技能、2 個 MCP | [`course/HARNESS.md`](./course/HARNESS.md) |
| 技術棧、紅線、骨架怎麼生 | [`course/STACK.md`](./course/STACK.md) |
| 六份規格怎麼寫 | [`course/templates/`](./course/templates/) |

課程結束後想要完整的工具鏈（38 個技能），用模板 repo [`agent-skills-starter`](https://github.com/Zenobia000/agent-skills-starter) 開新專案。

技能與 guard hooks 衍生自 [luca-skills](https://github.com/Luca0x5755/luca-skills)（MIT），Archify 取自 [tt-a1i/archify](https://github.com/tt-a1i/archify)（MIT），聲明見 [`.claude/THIRD-PARTY-NOTICES.md`](./.claude/THIRD-PARTY-NOTICES.md)。
