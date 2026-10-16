#!/usr/bin/env bash
# 一個指令同時起 backend（FastAPI）與 frontend（Next.js）。Ctrl+C 兩個一起停。
#
#   bash scripts/dev.sh
#   FRONTEND_PORT=3100 BACKEND_PORT=8100 bash scripts/dev.sh   # port 被佔用時換一組
#
# 前端用 next.config.ts 的 rewrites 把 /api/* 轉給 backend（見 STACK.md），
# 所以瀏覽器只連前端，不用處理 CORS。backend 位址由這支腳本用 BACKEND_URL 傳過去。

set -uo pipefail
cd "$(git rev-parse --show-toplevel)" || exit 1

FRONTEND_PORT=${FRONTEND_PORT:-3000}
BACKEND_PORT=${BACKEND_PORT:-8000}
export BACKEND_URL="http://127.0.0.1:${BACKEND_PORT}"

fail() { printf '✗ %s\n' "$1" >&2; exit 1; }

[ -f backend/app/main.py ] || fail "找不到 backend/app/main.py。還沒做 I0 骨架？照 STACK.md 的「I0」讓 agent 生成。"
[ -f frontend/package.json ] || fail "找不到 frontend/package.json。還沒做 I0 骨架？照 STACK.md 的「I0」建立 frontend。"
[ -x .venv/bin/uvicorn ] || fail "找不到 .venv/bin/uvicorn。先在 repo 根目錄照 README 建 .venv 並 pip install -e \".[dev]\"。"
[ -d frontend/node_modules ] || fail "frontend/node_modules 不存在。先跑：(cd frontend && npm install)"

port_busy() {
  if command -v ss >/dev/null 2>&1; then ss -ltn | grep -q ":$1 "
  elif command -v lsof >/dev/null 2>&1; then lsof -iTCP:"$1" -sTCP:LISTEN >/dev/null 2>&1
  else return 1; fi
}
port_busy "$BACKEND_PORT" && fail "port $BACKEND_PORT 已被佔用。換一個：BACKEND_PORT=8100 bash scripts/dev.sh"
port_busy "$FRONTEND_PORT" && fail "port $FRONTEND_PORT 已被佔用。換一個：FRONTEND_PORT=3100 bash scripts/dev.sh"

pids=()
cleanup() { for p in "${pids[@]}"; do kill "$p" 2>/dev/null; done; }
trap cleanup EXIT INT TERM

ROOT=$PWD
(cd backend && exec "$ROOT/.venv/bin/uvicorn" app.main:app --reload --port "$BACKEND_PORT") &
pids+=($!)
(cd frontend && exec npx next dev -p "$FRONTEND_PORT") &
pids+=($!)

printf '\n前端  http://localhost:%s\n後端  %s（API 文件：%s/docs）\nCtrl+C 結束\n\n' "$FRONTEND_PORT" "$BACKEND_URL" "$BACKEND_URL"
wait -n
