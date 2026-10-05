---
type: llm
weight: 2
---

This grader checks one thing: invented facts. Ignore style, format and completeness.

FAIL if the answer does any of these: gets the arithmetic wrong (Offer B is 2,450 x 12 = 29,400 a year; with the 1,500 bonus the first-year total is 30,900; Offer A is 31,000); puts a cash value on the share options or adds them to a pay total; estimates tax or take-home pay; states a fact about Halden Robotics or Orbit Labs that the user did not give (its mentoring, team, culture, seniority, funding).
Otherwise PASS. (Saying which offer pays more, and calling an assumption an assumption, is fine.)

Not violations, here or anywhere: placeholders in square brackets ("[add: ...]", "[confirm: ...]"); questions to the user; advice and suggested next steps; plain arithmetic on given numbers (two teammates plus Sam is a team of three; 2,450 x 12); mentioning ROS 2, C++ or any missing thing as a gap, a requirement or something to learn.


The judge is shown only the assistant's answer. For reference, this was the user's whole message; it is everything that is known about the user, the employer and the offers:

<user_message>
I have two offers and need to pick one. What matters most to me is learning from senior engineers; pay comes second.

Offer A, Halden Robotics: 31,000 pounds a year, on site in Leeds, 25 days of holiday, "share options" (no details given), start in November.

Offer B, Orbit Labs: 2,450 pounds a month, fully remote, a 1,500 pound signing bonus, 28 days of holiday, six-month probation.
</user_message>
