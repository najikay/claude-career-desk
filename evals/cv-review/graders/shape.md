---
type: llm
weight: 1
---

This grader checks that the response has the parts the skill promises. Do not judge honesty here.

The response PASSES if it has ALL of these parts:
- An opening on how the CV reads to a recruiter in a quick skim, saying that the robot project is the strongest item for robotics roles and is undersold or buried inside Education.
- Line-by-line findings that quote the CV's own lines, each with a problem and a rewrite. "Responsible for the morning rush" is flagged as a duty rather than a result. "team player" and "hard-working" are flagged as claims with no evidence.
- Skills with no evidence are called out (C++ at least), and "ROS" is noted as needing its version (ROS 1 Noetic in the project).
- Three changes that matter most, in order.
