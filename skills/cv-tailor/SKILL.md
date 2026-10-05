---
name: cv-tailor
description: "Tailor a CV or resume to one job posting without inventing anything: reorder and reword what is already there to match what the posting asks for, using the posting's own terms where the user truly has the thing, and list every change with its reason. Use when the user says \"tailor my CV to this job\", \"adapt my resume for this posting\" or \"optimise my CV for this role\". Needs the CV and the posting. Not for a general CV review (use cv-review)."
---

# CV tailoring

Input: the user's CV and one job posting.

## The one rule
**Only what is on the CV, or what the user tells you in this conversation, may appear in the tailored CV.** No added skill, tool, title, employer, date, grade or number. A keyword from the posting goes in only where the user has exactly that thing. Where they have the nearest thing, name what they have: "ROS 1 (Noetic)" stays "ROS 1 (Noetic)", it does not become "ROS 2". Dates, job titles, employers and degrees are copied exactly.

## Steps
1. **What the posting wants**: its five most important requirements, in its words.
2. **Where the CV answers each**: the line that shows it, or "nothing on the CV".
3. **Ask before you write**, at most three questions, where the CV may be underselling the user: "Your skills list has C++. Where did you use it?" If the user wants the draft now, write it and mark the open points `[confirm: …]`.
4. **The tailored CV**:
   - put first the section that carries the best evidence for this role (at entry level usually a project or an internship, above unrelated work);
   - within each entry, lead with the lines the posting cares about;
   - reword each line to start with what was done and end with what came of it, in the posting's terms where they are true;
   - cut what does not serve this application; keep it to one page at entry level unless the user's country or field expects more;
   - plain structure with standard headings, so that applicant-tracking software reads it: no tables, columns or text in images.
5. **The change list**: a table `what changed · why · which requirement it answers`. Everything moved, reworded, cut or left as a placeholder is in it, so the user stays the author.
6. **Not on your CV**: the posting's requirements you could not show, listed plainly, with what the user could do about each. Never papered over.

## Notes
- Unsupported claims ("team player", "hard-working") are cut, or replaced by the line that shows them.
- Give the tailored CV as one block the user can copy, then the change list. Write a file only when the user works in files and asks.
