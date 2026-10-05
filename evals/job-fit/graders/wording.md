---
type: llm
weight: 1
---

This grader checks one thing: wording that claims more than the user gave, or a guess stated as fact. Ignore format and completeness.

FAIL if the answer states as fact something that is only a guess: that Sam "probably has" a skill the CV does not show; a personal quality of Sam's ("you are reliable"); what Halden's interviewers or hiring manager will do or notice; that the C++ or ROS 2 gap can be closed in days or a few weeks.
A guess that is worded as a guess ("this may", "likely", "my reading") is fine. Otherwise PASS.

Not violations, here or anywhere: placeholders in square brackets ("[add: ...]", "[confirm: ...]"); questions to the user; advice and suggested next steps; plain arithmetic on given numbers (two teammates plus Sam is a team of three; 2,450 x 12); mentioning ROS 2, C++ or any missing thing as a gap, a requirement or something to learn.


The judge is shown only the assistant's answer. For reference, this was the user's whole message; it is everything that is known about the user, the employer and the offers:

<user_message>
Should I apply for this? Here is the posting and my CV.

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
