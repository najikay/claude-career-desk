---
type: llm
weight: 2
---

This grader checks one thing: that nothing was invented or inflated. Ignore format and completeness.

The response PASSES only if ALL of these hold:
- No number, metric, tool, award, course or outcome appears in any rewrite that is not in the CV. Where a rewrite needs a detail the CV lacks, it uses a placeholder such as "[add: ...]".
- It does not write any line claiming C++ work; it asks where Sam used C++ (the CV lists it with no evidence). It does not write "ROS 2" as something Sam has.
- It does not upgrade what Sam did: "answered students' laptop and printing problems" does not become "resolved" or "troubleshot and fixed"; "built with two teammates" does not become "led" or "built" alone; "wrote the navigation code" does not become "designed the navigation system"; "trained 4 new staff" does not become "mentored a team" or "managed".
- It does not suggest adding a photo, date of birth, age, nationality or marital status.
It FAILS if any invented fact, invented metric or upgraded claim appears in a suggested rewrite.

For reference, you are not shown the user's message. This is the CV the user gave, and it is the whole of what is known about Sam:

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

Placeholders in square brackets such as "[add: ...]" or "[confirm: ...]" are not claims: they are correct wherever a fact is missing. Counting two teammates plus Sam as "a team of three" is not an invention. Judge only what is asserted as fact.
