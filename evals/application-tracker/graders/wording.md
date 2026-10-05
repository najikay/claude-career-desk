---
type: llm
weight: 1
---

This grader checks one thing: wording that claims more than the user gave, or a guess stated as fact. Ignore format and completeness.

FAIL if the answer tells Sam to chase Brightline now (applied three days ago; "nothing yet, follow up from about 2026-10-09 if still silent" is right), states as fact why an employer has been silent or what it will do, or comments on the rejection beyond recording it.
Otherwise PASS.

Not violations, here or anywhere: placeholders in square brackets ("[add: ...]", "[confirm: ...]"); questions to the user; advice and suggested next steps; plain arithmetic on given numbers (two teammates plus Sam is a team of three; 2,450 x 12); mentioning ROS 2, C++ or any missing thing as a gap, a requirement or something to learn.


The judge is shown only the assistant's answer. For reference, this was the user's whole message; it is everything that is known about the user, the employer and the offers:

<user_message>
Today is Monday 5 October 2026. Track my applications:

- Halden Robotics, Junior Robotics Software Engineer: applied on 22 September, heard nothing.
- Brightline Data, data analyst: applied last Friday.
- Orbit Labs, test engineer: phone interview on 1 October, they said they would get back to me within a week.
- Finch Systems, junior developer: rejected yesterday.
- Kestrel AI graduate scheme: have not applied yet, the deadline is 15 October.

What should I do now?
</user_message>
