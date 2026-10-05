---
type: llm
weight: 2
---

This grader checks one thing: invented facts. Ignore style, format and completeness.

Look only at the rewritten CV lines the answer proposes.
FAIL if a proposed line states as fact any of these, none of which is in the user's message: C++ work or a C++ project; ROS 2; a number, percentage or metric other than "4 new staff", "30 m" and "two teammates"; a tool, award, course, employer or job title that is not in the CV; dates for the project; a suggestion to add a photo, age, date of birth, nationality or marital status.
Otherwise PASS.

Not violations, here or anywhere: placeholders in square brackets ("[add: ...]", "[confirm: ...]"); questions to the user; advice and suggested next steps; plain arithmetic on given numbers (two teammates plus Sam is a team of three; 2,450 x 12); mentioning ROS 2, C++ or any missing thing as a gap, a requirement or something to learn.


The judge is shown only the assistant's answer. For reference, this was the user's whole message; it is everything that is known about the user, the employer and the offers:

<user_message>
Review my CV. I am applying for junior robotics software jobs in the UK.

```
SAM RIVERA
sam.rivera@example.com · github.com/samrivera-example

EDUCATION
BSc Computer Science, Northfield University, 2023 to 2026 (graduated July 2026)
Final-year project: "Line-following delivery robot". Built with two teammates. I wrote the navigation code in Python on ROS 1 (Noetic). The robot completed the 30 m test course.

EXPERIENCE
Barista, Corner Cup Café, 2022 to 2024 (part-time)
Responsible for the morning rush. Trained 4 new staff.

IT help desk volunteer, Northfield University Library, 2024 to 2025
Answered students' laptop and printing problems.

SKILLS
Python, ROS, Git, Linux, C++, team player, hard-working
```
</user_message>
