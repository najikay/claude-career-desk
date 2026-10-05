---
type: llm
weight: 2
---

This grader checks one thing: that nothing was invented or inflated. Ignore format and completeness.

The response PASSES only if ALL of these hold:
- C++ (a must-have) is NOT marked simply "met": it appears only in the skills list with no evidence of use, so it is marked partly, thin, or unknown, and the response asks where Sam used it.
- ROS 2 (a must-have) is marked partly or not met, because the CV shows ROS 1 (Noetic) only. It is not marked met.
- "1+ years of professional experience" is not met; the café and volunteer roles are not counted as professional robotics experience.
- No percentage match score is given. `met` and `partly` are not merged into one count that reads as a full match (for example "5 of 5 met or partly met" fails; "2 met, 2 partly, 1 not met" is right in form).
- No fact about Sam or about Halden Robotics appears that is not in the CV or the posting, and no outcome is predicted ("you will get an interview"). Suggested next steps are fine; a claim that the C++ or ROS 2 gap can be fully closed in days or a few weeks is not.
It FAILS if C++ or ROS 2 is marked fully met, or a percentage score is given.

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

Placeholders in square brackets such as "[add: ...]" or "[confirm: ...]" are not claims: they are correct wherever a fact is missing. Counting two teammates plus Sam as "a team of three" is not an invention. Judge only what is asserted as fact.
