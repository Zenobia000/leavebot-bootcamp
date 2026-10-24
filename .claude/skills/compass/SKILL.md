---
name: compass
description: 問這個情況該用哪個技能、走哪條流程。上課用的 11 個技能的路由器。
disable-model-invocation: true
---

# Compass

This repo ships eleven skills for a two-day course: D1 learns the tools in `playground/`, D2 writes the specs and builds one leave-request feature from zero. Tell the user where they are now, which skill fits, and what file it should leave behind.

**Respond in the session's language.** Check which of `docs/01-brief.md` … `docs/06-test-plan.md`, `diagrams/`, `docs/LESSONS.md` and `issues/` already exist before answering — the next step is the first thing that is missing. The repo starts empty on purpose: everything outside `course/` and the config files is something the user builds.

## D1 — tools and a throwaway demo

Everything on D1 goes in `playground/` (git-ignored, not bound by `course/STACK.md`). A rough idea gets sharpened with **`/grilling`**, written up with `course/templates/02-prd.md`, and drawn with **`/archify`**.

## D2 morning — the spec chain

| Step | Skill | Leaves behind (format) |
| --- | --- | --- |
| 1. Why build it: pain, goals, non-goals, done criteria | — fill the template | `docs/01-brief.md` (`course/templates/01-brief.md`) |
| 2. Surface the gaps in the company rules | **`/grilling`** | answered questions, open ones listed |
| 3. For whom, what: persona, user flow, story, BDD | **`/grilling`** (same session) | `docs/02-prd.md` (`course/templates/02-prd.md`) |
| 4. What the system must do: FR, NFR, each with its source | — fill the template with the agent | `docs/03-srs.md` |
| 5. The workflow as a picture | **`/archify`** (no Node: Mermaid) | `diagrams/` |
| 6. How it fits together and how each piece works | **`/to-architecture`** | `docs/04-sad.md`, `docs/05-sds.md` |

## D2 afternoon — tests first, then the build

| Step | Skill | Done when |
| --- | --- | --- |
| 7. How it will be verified: 6–12 test cases, traceability matrix | — fill the template with the agent | `docs/06-test-plan.md`; every AC / FR has a TC |
| 8. Split the work; project rules | **`/to-tickets`**, **`/writing-for-agents`** | `issues/000-skeleton.md`, `issues/001-submit-leave.md`; the 本專案 half of `AGENTS.md`; `docs/LESSONS.md` |
| 9. Skeleton per `course/STACK.md` | — | the page at `http://127.0.0.1:8000/` shows `/api/health`; `.venv/bin/pytest` green |
| 10. The leave-request slice | **`/tdd`** | the ticket's test cases go red, then green, each test marked `@pytest.mark.req(...)` |
| A test goes red and the cause is not obvious | **`/diagnosing-bugs`** | a reproducing test, one hypothesis at a time, then the fix |
| A requirement changes | — | spec first, then TC, then test, then code; full regression green |
| End of the slice | — | ask the agent to click through the PRD user flow with the **playwright** MCP |
| Before committing the slice | **`/code-review`** | a review a human accepts or rejects line by line |
| Another teammate or tool takes over | **`/handoff`** | a file the next session starts from |
| A rule that must never be broken | **`/writing-hooks`** | a hook in `.claude/hooks/`, registered in both tools |

Finish with the traceability matrix: no AC / FR / NFR without a TC, no TC without a test file, three rows spot-checked by a human. Advanced challenges C1–C5 (`course/LEAVEBOT.md`) come after, one ticket each.

`/compass`, `/to-architecture`, `/to-tickets` and `/handoff` are **user-triggered**: the user types them, and they are deliberately absent from your own list of skills. Do not warn that they are missing — check `.claude/skills/<name>/SKILL.md` if in doubt.

An open question at any step goes back to **`/grilling`**, never to a guessed default.

## Context hygiene

- Steps 2–3 stay in **one session**. The PRD needs the interview verbatim, not a summary.
- Between cards and tickets, **`/clear`**. Everything the next step needs is in `docs/`, `docs/LESSONS.md` and the ticket.
- A session getting long mid-step: finish the step, then `/compact` with an instruction (`/compact next we build ticket 001`).

## Built-in commands, not skills

`/clear`, `/compact` and `/init` belong to Claude Code itself — and do not run `/init` here, it would overwrite the project's agent rules. In Codex, skills are called with `$name` (`$grilling`), and its own review command is `/review`.

## When the output disagrees with the handout

That is expected — models hallucinate. Align in this order: the spec (`docs/`, `course/STACK.md`), then the measures (tests, the traceability matrix), then the instructor. Record the drift in `docs/LESSONS.md`. A team that falls behind switches to the instructor's checkpoint branch (`cp1-requirements` … `cp5-delivered`) rather than pushing on.

## Where the boundaries live

`AGENTS.md` holds the rules (factory half on top, project half below); `course/STACK.md` fixes the stack; `.claude/hooks/` blocks dangerous git commands whatever the agent decides; `.mcp.json` adds context7 (current docs) and playwright (a browser); `course/HARNESS.md` explains which file does what.
