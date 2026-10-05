---
type: llm
weight: 1
---

This grader checks one thing: wording that claims more than the user gave, or a guess stated as fact. Ignore format and completeness.

Look only at the tailored CV the answer produces.
FAIL if a line uses a stronger verb or a larger share of the work than the original: "answered ... problems" turned into "resolved" or "fixed"; "Responsible for the morning rush" turned into "handled", "managed" or "ran"; "built with two teammates" turned into "led" or "built" alone; "wrote the navigation code" turned into "designed"; "trained 4 new staff" turned into "mentored" or "managed". Also FAIL if it adds a profile or summary line stating a personal quality ("motivated", "reliable", "fast learner").
Otherwise PASS. ("Worked the morning rush" and weaker wording are fine.)

Not violations, here or anywhere: placeholders in square brackets ("[add: ...]", "[confirm: ...]"); questions to the user; advice and suggested next steps; plain arithmetic on given numbers (two teammates plus Sam is a team of three; 2,450 x 12); mentioning ROS 2, C++ or any missing thing as a gap, a requirement or something to learn.


The judge is shown only the assistant's answer. For reference, this was the user's whole message; it is everything that is known about the user, the employer and the offers:

<user_message>
Tailor my CV to this job. Give me the draft now; I can answer questions afterwards.

```
Junior Robotics Software Engineer, Halden Robotics (Leeds, on site)

You will write and test navigation software for our warehouse robots.

Must have: a degree in computer science, robotics or similar; C++ (our codebase is C++17); ROS 2; Linux; Git.
Nice to have: Python; experience with real robots; 1+ years of professional experience.

We are a 40-person company. Our robots move pallets in 12 warehouses.
```

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
