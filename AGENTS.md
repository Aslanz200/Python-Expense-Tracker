# AI Agent Instructions — Python Expense Tracker

## Purpose and architecture
This repository contains a small Tkinter desktop expense tracker and budget planner. The entry point is `Simple_Expense_Tracker.py`. The `ExpenseTrackerApp` class owns the GUI, in-memory expense/category lists, budget calculations, and JSON export. There is no server, production deployment, or external dependency manifest.

## Setup and safe commands
- Use Python 3 with Tkinter available and a graphical display for GUI checks.
- Static syntax check: `python3 -m py_compile Simple_Expense_Tracker.py`.
- Launch manually: `python3 Simple_Expense_Tracker.py` (GUI required).
- Run tests only when present: `python3 -m unittest discover -s tests -v`.
- Inspect changes with `git diff` and `git status`.
- If a command cannot run in the environment, record that limitation instead of claiming success.

## Coding conventions
- Keep changes minimal and readable, with descriptive Python names.
- Preserve the existing UI and valid expense workflows.
- Validate untrusted inputs before mutating expense state.
- Prefer standard-library functionality; avoid new dependencies unless separately approved.
- Add focused tests for behavioral fixes and document before/after evidence.

## Boundaries and permissions
- Read repository files and propose diffs freely.
- Make edits only within the dedicated assignment branch and approved files.
- Do not access, print, upload, or commit secrets, tokens, personal financial records, or private user data.
- Do not deploy to production, alter GitHub repository settings, delete history, force-push, or execute destructive commands.
- Do not install or upgrade dependencies without explicit human review.
- Do not modify unrelated files or perform large refactors without approval.
- Treat AI-generated findings as hypotheses until supported by code inspection or reproducible tests.

## Verification and review gates
- Preserve the baseline commit and original evidence before edits.
- Every code change requires a human-reviewed diff and relevant tests.
- Report exact commands, actual outputs, failures, skipped checks, and residual risks.
- Human approval is required before merging, releasing, or deploying.
- If a test fails, stop and investigate; revert the focused change if necessary rather than concealing failure.

## Background agent policy
Any hypothetical asynchronous agent must work in an isolated branch/worktree with explicit allowed files, commands, and time limit; it must return a diff, test logs, change summary, and risk notes for human approval. No autonomous merge or deployment.
