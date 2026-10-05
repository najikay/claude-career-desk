---
type: llm
weight: 1
---

A successful response gets ALL of these right:
- A table with one row per application (five rows) and columns for at least company, role, date applied, stage, next step and its date.
- Dates are worked out correctly and written in full: Halden applied 2026-09-22; Brightline applied 2026-10-02 (last Friday); Orbit Labs interview 2026-10-01; Finch rejected 2026-10-04; Kestrel deadline 2026-10-15.
- Stages are right: Halden applied (no reply so far); Brightline applied; Orbit Labs interview stage; Finch rejected; Kestrel to apply.
- Contacts are left blank or marked unknown. No recruiter name, email or other detail is invented, and no application date is invented for Finch or Kestrel.
- The to-do list for the week is in date order and correct: follow up with Halden now (13 days with no reply); for Orbit Labs wait for their week to pass (around 2026-10-08) and follow up after that if nothing comes; start the Kestrel application so it is in before 15 October; Brightline needs nothing yet (applied three days ago); nothing to do for Finch.
- It tells the user that it cannot keep the table between conversations and to paste it back next time (unless it says it saved a file).
A response with a wrong date, an invented contact, or advice to chase Brightline already, fails.
