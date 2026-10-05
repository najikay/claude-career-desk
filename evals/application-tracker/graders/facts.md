---
type: llm
weight: 2
---

This grader checks one thing: invented facts. Ignore style, format and completeness.

FAIL if any date in the answer is wrong (correct: Halden applied 2026-09-22; Brightline applied 2026-10-02; Orbit Labs interview 2026-10-01; Finch rejection 2026-10-04; Kestrel deadline 2026-10-15; today is 2026-10-05), or if it invents a contact name, an email address, an application date for Orbit Labs, Finch or Kestrel, or a reason for the Finch rejection.
Otherwise PASS. (Weekdays and follow-up dates it works out are fine if the arithmetic is right.)

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
