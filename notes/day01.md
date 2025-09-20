\# Day 1 — Fast Employability Track

\*\*Date:\*\* 2025-09-19



\## Goal

Set up Python, venv, Git, and push first commit to GitHub.



\## Steps performed (exact commands used)

\- `python --version` → Python 3.13.6

\- `git --version` → git version 2.50.1.windows.1

\- `python -m venv venv`

\- `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned` (ran as Admin)

\- `.\\venv\\Scripts\\Activate.ps1`

\- Created `day01\_setup.py` and ran: `python day01\_setup.py`



\## Issues \& Fixes

\- PowerShell blocked scripts. Resolved with `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

\- File `day01\_setup.py` missing at first — created via Notepad and re-ran.



\## Output snapshot

Paste the outputs you saw (copy-paste):

Hello, World! — Day 1 setup

Python executable: C:...

Python version: 3.13.6 (...)





\## Notes / Learnings

\- Keep a clean repo structure from day-one.

\- Use Conventional Commit messages for clarity.





