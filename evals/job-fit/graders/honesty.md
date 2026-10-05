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
- No fact about Sam or about Halden Robotics appears that is not in the CV or the posting, and no outcome is predicted ("you will get an interview").
It FAILS if C++ or ROS 2 is marked fully met, or a percentage score is given.
