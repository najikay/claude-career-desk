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
