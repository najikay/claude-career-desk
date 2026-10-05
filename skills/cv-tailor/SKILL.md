---
name: cv-tailor
description: "Tailor a CV or resume to one job posting without inventing anything: reorder and reword what is already there to match what the posting asks for, using the posting's own terms where the user truly has the thing, and list every change with its reason. Use when the user says \"tailor my CV to this job\", \"adapt my resume for this posting\" or \"optimise my CV for this role\". Needs the CV and the posting. Not for a general CV review (use cv-review)."
---

# CV tailoring

Input: the user's CV and one job posting.

## The rule of this desk
**Nothing is invented.** Only what is on the CV, or what the user says in this conversation, may be stated about them: no added skill, tool, title, employer, date, grade or number. Do not upgrade what the user did or how much of it was theirs: *answered* is not *resolved*, *helped* is not *led*, *built with two teammates* is not *built*, a course is not experience, a listed skill is not use. If a rewrite says more than the original, it is wrong. Where a real detail is missing, write `[add: …]` and ask the user for it.

A keyword from the posting goes in only where the user has exactly that thing. Where they have the nearest thing, name what they have: "ROS 1 (Noetic)" stays "ROS 1 (Noetic)"; it does not become "ROS 2". Dates, job titles, employers and degrees are copied exactly; if one looks out of date (an "expected" date that has passed), keep it and mark it `[confirm: …]`.

## Steps
1. **What the posting wants**: its five most important requirements, in its words.
2. **Where the CV answers each**: the line that shows it, or "nothing on the CV".
3. **Questions**, at most three, where the CV may be underselling the user: "Your skills list has C++. Where did you use it?" If the user wants the draft now, write it, mark the open points `[confirm: …]`, and put the questions after it.
4. **The tailored CV**:
   - put first the section that carries the best evidence for this role (at entry level usually a project or an internship, above unrelated work);
   - within each entry, lead with the lines the posting cares about;
   - reword each line to start with what was done and, only where the CV or the user gives one, end with what came of it. With no outcome given, stop at what was done or write `[add: what came of it]`;
   - use the posting's terms only where they are true of the user;
   - cut what does not serve this application; keep it to one page at entry level unless the user's country or field expects more;
   - plain structure with standard headings, so that applicant-tracking software reads it: no tables, columns or text in images.
5. **The change list**: a table `what changed · why · which requirement it answers`. Everything moved, reworded, cut or left as a placeholder is in it, so the user stays the author.
6. **Not on your CV**: the posting's requirements you could not show, listed plainly, with what the user could do about each. Never papered over.

End with one line: before sending anything, search it for `[`; every bracket is something only the user can fill in.

## Care with personal details
- Never ask for, or suggest adding, age or date of birth, a photo, marital or family status, health or disability, religion or nationality. Where a country's convention expects one of these (a photo in Germany, for example), say that it is the user's choice. Do not press the user to explain a gap in their history; offer neutral wording if they ask.
- Never put the user's CV text, name or contact details into a web search. If the user asks you to look an employer up and you can search, search with the company and role names only, and say where each fact came from.
- Referees' names and contact details stay off the CV.

## Notes
- Unsupported claims ("team player", "hard-working") are cut, or replaced by the line that shows them.
- Give the tailored CV as one block the user can copy, then the change list. Write a file only when the user works in files and asks.
