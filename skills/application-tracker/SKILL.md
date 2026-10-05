---
name: application-tracker
description: "Keep a job search organised: a table of applications with company, role, date applied, stage, next step and its date, contact and notes, updated as the user reports news, with what is due this week and which applications need a follow-up. Use when the user says \"track my applications\", \"I applied to...\", \"update my job tracker\" or \"what should I follow up on?\". Not for finding job postings."
---

# Application tracker

## The table
`company · role · applied · stage · next step · due · contact · notes`

- **Stage** is one of: `to apply` · `applied` · `screening` · `interview` · `offer` · `rejected` · `withdrawn` · `no reply`.
- **Dates** are written in full (2026-10-05). Work them out from today's date; if you do not know today's date, ask. A date the user did not give stays blank.
- **Contact** and anything else the user did not tell you stays blank. Never fill a name, an email or a date from a guess.

## Keeping it
- **In a chat with no files and no memory**: you cannot keep the table between conversations. Give the whole table back, as one block, every time it changes, and tell the user to paste it in when they return. Say this once, plainly.
- **Working in files**: keep it in `applications.md` (or the file the user names) and update it there.
- When the user pastes an earlier table, continue from it; do not rebuild it from memory.

## When the user reports news
Update the row or add one, then show the table and the list below. Do not ask for details they did not offer; leave the cell blank.

## What needs doing
After every update, list **due this week** in date order, using these rules of thumb and saying they are rules of thumb:
- applied, no reply after 7 to 10 days: a short follow-up is reasonable;
- after an interview: a thank-you note within a day; if they gave a date for their answer, follow up the day after it passes; if they gave none, after 5 to 7 working days;
- applied and silent for about four weeks: mark `no reply`, keep it, move on;
- `to apply` with a deadline: the deadline is the due date, and the application wants a day or two before it.

End with one line of counts by stage. Report, do not judge: a rejection is recorded, not commented on.
