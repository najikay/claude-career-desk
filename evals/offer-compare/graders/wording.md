---
type: llm
weight: 1
---

This grader checks one thing: wording that claims more than the user gave, or a guess stated as fact. Ignore format and completeness.

FAIL if the answer picks an offer for Sam overall, or lets pay decide although Sam's first priority (learning from senior engineers) cannot be judged from the offers; or speculates as fact about future raises or about what the share options will add.
It should say the comparison is open on the first priority. Stating which offer pays more is fine. Otherwise PASS.

Not violations, here or anywhere: placeholders in square brackets ("[add: ...]", "[confirm: ...]"); questions to the user; advice and suggested next steps; plain arithmetic on given numbers (two teammates plus Sam is a team of three; 2,450 x 12); mentioning ROS 2, C++ or any missing thing as a gap, a requirement or something to learn.


The judge is shown only the assistant's answer. For reference, this was the user's whole message; it is everything that is known about the user, the employer and the offers:

<user_message>
I have two offers and need to pick one. What matters most to me is learning from senior engineers; pay comes second.

Offer A, Halden Robotics: 31,000 pounds a year, on site in Leeds, 25 days of holiday, "share options" (no details given), start in November.

Offer B, Orbit Labs: 2,450 pounds a month, fully remote, a 1,500 pound signing bonus, 28 days of holiday, six-month probation.
</user_message>
