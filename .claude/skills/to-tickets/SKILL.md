---
name: to-tickets
description: 把規格切成 D2 的票：骨架一張、新增請假的垂直切片一張，進階挑戰另開。寫進 issues/，每張都引用它要讓哪些 TC 變綠。
disable-model-invocation: true
---

# To Tickets

Split the build into tickets an agent can pick up cold in a fresh session. Material: `docs/01-brief.md` … `docs/06-test-plan.md`, `course/STACK.md`, `course/LEAVEBOT.md`.

## The tickets

| Ticket | Scope |
| --- | --- |
| `issues/000-skeleton.md` | exactly the skeleton section of `course/STACK.md`: `pyproject.toml`, `backend/app/main.py` with `GET /api/health`, `backend/app/static/` mounted at `/` whose page shows the health response, one passing health test. No business logic |
| `issues/001-submit-leave.md` | the vertical slice of the basic scope in `course/LEAVEBOT.md`: form → backend validation → saved as pending → "my requests" list shows it. **Every basic-scope TC lands here** |
| `issues/1NN-<challenge>.md` | one per advanced challenge C1–C5 (`course/LEAVEBOT.md`), **only when the user asks for it** |

Every ticket after the skeleton is a **vertical slice**: something observably works when it is done, front to back. Never "the database layer" or "the API layer".

## Ticket shape

```markdown
# <001: verb the outcome>

## Test cases this ticket turns green
TC-01, TC-04 — copied from docs/06-test-plan.md with the requirement each verifies.

## Done when
- those test cases pass, each test marked @pytest.mark.req("TC-xx", ...)
- a command someone else can run (pytest selection, curl, or a click path on http://127.0.0.1:8000/)
- the traceability matrix in docs/06-test-plan.md shows these TCs with their test files

## Context
The sections of docs/05-sds.md this touches (API IDs, screens, modules). Point, do not restate.

## Blocked by
000 — or "nothing".

## Notes
Traps, decided-against alternatives, the seam to test at.
```

## Rules

- **Every TC in the test plan lands in exactly one ticket.** List any that land nowhere — they are either missing scope or belong in "不測什麼".
- **No ticket decides what the spec left open.** Put the question in Notes and flag it to the user.
- **Show the full set before writing files.** Sizing is easier to judge as a list.

## Finish

Report the paths and say: build `000` straight from `course/STACK.md`, then `001` with `/tdd`, **`/clear`ing context between tickets**; each ticket ends with the traceability matrix and `docs/LESSONS.md` updated.
