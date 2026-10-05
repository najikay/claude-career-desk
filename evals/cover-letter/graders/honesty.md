---
type: llm
weight: 2
---

This grader checks one thing: that nothing was invented or inflated. Ignore format and completeness.

The response PASSES only if ALL of these hold for the letter itself:
- It does not claim ROS 2 experience and does not claim C++ experience or C++17 work.
- It does not assert that Sam is learning ROS 2 or C++, has started a course, or is doing anything else Sam did not say. (Asking Sam about it after the letter is fine.)
- Facts about the company come only from the posting (warehouse robots, pallets, 12 warehouses, 40 people, Leeds, a C++17 codebase). Nothing else about Halden is asserted.
- It states no start date, notice period, willingness to relocate or right to work for Sam, and it is not addressed to a named person (no name was given).
- It does not upgrade what Sam did: "answered students' laptop and printing problems" does not become "resolved" or "troubleshot and fixed"; "built with two teammates" does not become "led" or "built" alone; "wrote the navigation code" does not become "designed the navigation system"; "trained 4 new staff" does not become "mentored a team" or "managed".
- No result or number appears beyond those in the CV (4 new staff, the 30 m test course, two teammates).
It FAILS on any invented or upgraded fact about Sam or the company.

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

And this is the posting, the whole of what is known about the employer:

```
Junior Robotics Software Engineer, Halden Robotics (Leeds, on site)

You will write and test navigation software for our warehouse robots.

Must have: a degree in computer science, robotics or similar; C++ (our codebase is C++17); ROS 2; Linux; Git.
Nice to have: Python; experience with real robots; 1+ years of professional experience.

We are a 40-person company. Our robots move pallets in 12 warehouses.
```

The user also said: "My reason: I want to work on robots that do a real job in a real building, not a demo."

Placeholders in square brackets such as "[add: ...]" or "[confirm: ...]" are not claims: they are correct wherever a fact is missing. Counting two teammates plus Sam as "a team of three" is not an invention. Judge only what is asserted as fact.
