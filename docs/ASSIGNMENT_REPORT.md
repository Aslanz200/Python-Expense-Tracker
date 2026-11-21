# Assignment #05 — Evidence-Based Audit Report

## Project and baseline
- Repository: https://github.com/Aslanz200/Python-Expense-Tracker
- Baseline branch: `main`
- Baseline commit: `d9ec7bb343c7f516cff339e679928ce8e4d42146` (verify against local `git rev-parse HEAD`)
- Working branch: `assignment-05-audit`
- Entry point: `Simple_Expense_Tracker.py`
- Architecture: single-file Tkinter desktop GUI; expense data held in memory; JSON export.
- Repository files: `Simple_Expense_Tracker.py`, `README.md`, `LICENSE`, `Simple Expense Tracker.pyproj`, `Simple Expense Tracker.sln`.
- Dependencies: Python standard library (`tkinter`, `json`, `datetime`); no dependency manifest or automated test suite observed in repository.

## Task 1 — Baseline and context
### Acceptance criteria (proposed; validate manually)
1. User can enter a monthly budget.
2. User can add a valid expense with date, category and amount.
3. Total expenses and remaining budget are updated correctly.
4. User can add a new category.
5. User can export current data to JSON.

### Baseline commands and results
| Command/check | Actual result | Evidence |
| --- | --- | --- |
| `python3 --version` | Pending local execution | Terminal output |
| `python3 -m py_compile Simple_Expense_Tracker.py` | Pending local execution | Terminal output |
| `python3 Simple_Expense_Tracker.py` | GUI launched successfully on macOS (user-provided screenshot, 2026-11-21); exact command/terminal output not supplied | Screenshot `Screenshot 2026-11-21 at 18.20.43.png` supplied in chat |
| Add budget 1000, expense 100; verify remaining 900 | PASS (visual): budget $1000.00, Food expense $100.00 dated 2026-11-21, total $100.00, remaining $900.00 | User-provided screenshot, 2026-11-21 |
| Automated tests | No test files found in repository; no test run claimed | Repository inspection |

### Candidate weaknesses (source review; not yet runtime verified)
- `add_expense()` stores date strings without parsing or validation.
- `add_expense()` converts amounts with `float()` but does not reject negative, zero or non-finite values.
- `README.md` documents `python expense_tracker.py`, but the tracked entry point is `Simple_Expense_Tracker.py`.
- UI, calculations and JSON persistence are tightly coupled in `ExpenseTrackerApp`.
- No automated tests are included.

### Observed facts vs assumptions
Repository files and code are observed through GitHub. Basic GUI launch and one expense calculation are visually verified from a user-provided screenshot. Exact terminal command output, syntax compilation, category addition and JSON export remain **unverified**.

## Task 2 — Agent instructions
Pending: create `AGENTS.md` with project map, safe commands, prohibited actions and review gates.

## Task 3 — Pattern decision
Pending: evaluate whether extracting validation/business rules is justified; at most one focused refactor.

## Task 4 — Read-only AI risk review
Pending: 5+ findings in 3+ categories; independently classify confirmed/plausible/unsupported.

## Task 5 — Risk register
Pending: `docs/RISK_REGISTER.md`; score likelihood × impact and prioritize two confirmed risks.

## Task 6 — Agent readiness
Pending: assess documentation, setup, reproducibility, tests, logging, security and agent boundaries; assign level 1–3.

## Task 7 — Mitigation and verification
Pending: two minimal mitigations for confirmed risks, targeted tests, before/after evidence and residual risk.

## Task 8 — Background agent safeguards
Pending: hypothetical isolated branch/worktree task with allowed files/commands, time limit, prohibited operations, artifacts, human review and rollback.

## Task 9 — Release decision
Pending: GO / CONDITIONAL / NO-GO with evidence.

## Task 10 — AI reflection
Pending: 200–300 words after work and verification.

## Evidence policy
Do not invent executions, pass counts, screenshots or verification. Record AI proposals separately from personally checked findings. Preserve baseline and final commit references.

### Reproduced defect — R01 (2026-11-21)
- Source: user-provided macOS GUI screenshot `Screenshot 2026-11-21 at 18.23.14.png` in assignment conversation.
- Input sequence: monthly budget $1000; Food expense $100; second Food expense -$500, both dated 2026-11-21.
- Observed: total expenses **-$400.00**; remaining budget **$1400.00**.
- Classification: **confirmed correctness defect** for an expense-only application. The code accepts a negative `float` without a positive-value check. Refunds would need explicit separate handling if supported.
- Risk scoring (initial): likelihood 3/3, impact 2/3, score **6/9**; provisional until full risk review.
- Proposed fix (not implemented): reject amounts <= 0 and non-finite amounts; add automated tests.
- Evidence limitations: screenshot verifies GUI state; no terminal output or automated test result is claimed.
