---
name: application-tracker
description: "Keep a job search organised: a table of applications with company, role, date applied, stage, next step and its date, contact and notes, updated as the user reports news, with what is due and which applications need a follow-up, and a short follow-up message when asked. Use when the user says \"track my applications\", \"I applied to...\", \"I heard back\", \"I got an interview\" or \"what should I follow up on?\". Not for finding job postings, and not for preparing for an interview (use interview-prep)."
---

# Application tracker

## The table
`company · role · applied · stage · next step · due · contact · notes`

- **Stage** is one of: `to apply` · `applied` · `assessment` · `screening` · `interview` · `offer` · `accepted` · `declined` · `rejected` · `withdrawn` · `no reply`.
- **Dates** are written in full (2026-10-05). Work them out from today's date; if you do not know today's date, ask. A date the user did not give stays blank. Dates of events (an interview, a rejection) go in the notes.
- **Contact**, and anything else the user did not tell you, stays blank. Never fill a name, an email address or a date from a guess.

## Keeping it
- **In a chat with no files and no memory**: you cannot keep the table between conversations. Give the whole table back, as one block, every time it changes, and tell the user to paste it in when they return. Say this once, plainly.
- **Working in files**: keep it in `applications.md` (or the file the user names), and only when the user asks for a file.
- When the user pastes an earlier table, continue from it; do not rebuild it from memory.

## When the user reports news
Update the row or add one, then show the table and the list below. Do not ask for details they did not offer; leave the cell blank.

## What needs doing
After every update, list what is **due in the next two weeks**, this week first, in date order. These are rules of thumb; say so once:
- applied, no reply after 7 to 10 days: a short follow-up is reasonable. Before that, nothing is due;
- after an interview: if they gave a date for their answer, follow up the day after it passes; if they gave none, after 5 to 7 working days. A thank-you note within a day is customary in some countries (the US, for example) and optional elsewhere;
- applied and silent for about four weeks: mark `no reply`, keep the row, move on;
- `to apply` with a deadline: the deadline is the due date, and the application wants a day or two before it;
- after a rejection: nothing is due. Asking for feedback is optional and worth it mainly after an interview.

End with one line of counts by stage. Report, do not judge: a rejection is recorded, not commented on.

## A follow-up message, when asked
Three or four lines, built only from what is in the table: the role, the date applied or interviewed, a plain question about the timeline. No name unless the user gave one ("Hello,"), nothing about the user that they did not say, no pressure.
