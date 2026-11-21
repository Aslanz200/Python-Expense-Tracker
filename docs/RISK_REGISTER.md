# Risk Register — Assignment #05

Assessment date: 2026-11-21. Scale: likelihood 1 (low)–3 (high), impact 1 (low)–3 (high); score = likelihood × impact. Scores are reasoned estimates, not measured incident frequencies.

| ID | Category | Cause → event → consequence | Affected component | Status and evidence | L | I | Score | Mitigation | Owner | Verification plan | Residual risk |
|---|---|---|---|---|---:|---:|---:|---|---|---|---|
| R01 | Correctness | Unchecked amount → negative expense accepted → misleading budget | `add_expense` | **Confirmed**: GUI screenshot 2026-11-21 18:23:14; budget 1000, expenses 100 and -500, total -400, remaining 1400; source uses `float()` without positivity check | 3 | 2 | 6 | Reject non-positive/non-finite amounts | Student | Negative/zero/nan/inf automated tests and GUI retest | Pending fix and verification |
| R02 | Correctness | Unparsed date string → impossible date accepted → inaccurate records | `add_expense` | **Confirmed**: GUI screenshot 2026-11-21 18:27:51 shows 2026-99-99 entered as Food $50; code stores raw string | 3 | 2 | 6 | Strict ISO calendar-date validation | Student | Invalid/valid/leap-date automated tests and GUI retest | Pending fix and verification |
| R03 | Maintainability | GUI and validation/calculation coupled → difficult isolated testing and future regressions | `ExpenseTrackerApp` | **Confirmed structural observation**: one class contains UI construction, input parsing, calculations and export; consequence risk is an assessment, not a demonstrated failure | 2 | 2 | 4 | Extract small validation functions; avoid broad redesign | Student | Review diff and run regression tests | Coupling beyond validation remains |
| R04 | Agent operations | No existing automated tests → AI changes may escape regression detection | Repository | **Confirmed**: repository inspection found no `tests/` files in baseline | 3 | 2 | 6 | Add targeted `unittest` coverage and document commands | Student | Run `unittest discover` and record totals | GUI interactions still require manual testing |
| R05 | Reproducibility | README names wrong script → documented launch fails → setup confusion | `README.md` | **Confirmed**: README says `expense_tracker.py`; tracked file is `Simple_Expense_Tracker.py` | 3 | 1 | 3 | Correct README command | Student | Compare README against tracked entry point; launch manually | Tkinter availability varies by platform |
| R06 | Security/data integrity | JSON save has no exception handler → failed write may crash or leave partial file | `save_data` | **Plausible/unverified**: `open(...,'w')` and `json.dump` without local `OSError` handling; no reproduced failure | 2 | 2 | 4 | Consider error handling and atomic save in later scope | Student | Reproduce permission/disk errors in safe sandbox | Not tested; remains open |
| R07 | Dependency | Third-party dependency vulnerability | Imports | **Unsupported**: baseline source imports only standard-library modules, no third-party manifest found | 1 | 1 | 1 | No dependency claim without evidence | Student | Review import inventory | Standard-library/environment issues still possible |

## Prioritization
Top two **confirmed user-facing correctness defects** selected for code mitigation: **R01 and R02** (both score 6). R04 also scores 6 but is addressed by the tests accompanying these two mitigations. R05 can be corrected as a documentation improvement.

## Verification and limitations
The GUI screenshots were provided during the assignment and have not yet been committed to GitHub. No automated test pass/fail claims should be made until execution output is captured. Update residual scores after verification.
