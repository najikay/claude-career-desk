# Career Desk

![Career Desk](assets/banner.png)

[![tests](https://github.com/najikay/claude-career-desk/actions/workflows/tests.yml/badge.svg)](https://github.com/najikay/claude-career-desk/actions/workflows/tests.yml)

**A job search you can stand behind.** Seven skills that take you from a CV and a job posting to a strong, honest application, and keep the search organised. Built for entry-level roles: final-year students, new graduates, career changers, anyone whose CV is short on paid experience in the field.

## The rule

**Career Desk never invents experience.** It reorders, cuts and rewords what is on your CV, and it asks questions to draw out what you left off. It does not add a skill, a tool, a title, a date or a number you did not give. Where a line needs a detail that is not there, it writes `[add: …]` and asks you. Everything it changes is listed, so you stay the author, and nothing in your application is something you would have to bluff about in the interview.

## The skills

| Skill | Say something like | What you get |
|---|---|---|
| **cv-review** | "Review my CV." "Why am I not getting interviews?" | How your CV reads in thirty seconds, each weak line with a rewrite built from your own facts, skills listed with nothing to back them, what is missing, and the three changes that matter most. |
| **job-fit** | "Should I apply for this?" "Am I qualified?" | Every requirement of the posting marked met, partly or not met, with the CV line that proves it; an apply, stretch or skip verdict; what to do about each gap. No made-up percentage score. |
| **cv-tailor** | "Tailor my CV to this job." | Your CV reordered and reworded for one posting, in its terms where they are true of you, with a list of every change and a plain list of what the posting asks that your CV cannot show. |
| **cover-letter** | "Write a cover letter for this job." | A short letter built from two or three real matches between your CV and the posting, in plain words, with no stock phrases, and a note of which CV line backs each claim. |
| **interview-prep** | "I have an interview next week." | The questions this posting is likely to produce, answer outlines from your own CV, STAR stories from your real projects and jobs, honest answers for the gaps, and questions to ask them. |
| **application-tracker** | "Track my applications." "What should I follow up on?" | A table of applications with stage, next step and date, and a list of what is due this week. |
| **offer-compare** | "Help me decide between these offers." | Offers side by side on what you say matters, pay on the same basis with the arithmetic shown, the unknowns to ask about, and what would tip the choice. The decision stays yours. |

## How a search goes

1. **cv-review** once, to get the base CV right.
2. For each posting: **job-fit** to decide whether to apply, then **cv-tailor** and **cover-letter**.
3. **application-tracker** as you apply and hear back.
4. **interview-prep** when an interview comes.
5. **offer-compare** at the end.

Each skill also works on its own.

## What it is like at entry level

A short CV is not an empty one. The evidence is in a final-year project, a thesis, an internship, a part-time job, a volunteer role, and it is usually undersold: buried under Education, written as duties, missing what you yourself did. Career Desk looks for that evidence and says it plainly. A café job is evidence of pace and of dealing with people; it is described as that, not dressed up as something else. "1+ years of experience" on a junior posting is read as what it usually is, a wish, while a real wall such as the right to work or an on-site location is named as a wall.

## Where it runs

Everywhere Claude runs: the Claude apps (web, desktop, mobile), Claude Code and Cowork. It is skills only. There is no server, nothing to install and nothing to configure.

## Your data

- Career Desk is a set of instructions for Claude. It contains no code that runs, stores or sends anything.
- Your CV and the postings you paste stay in your conversation with Claude, under the same terms as anything else you write there.
- It does not scrape job sites. You paste the posting.
- In a plain chat the application tracker cannot remember between conversations: it gives you the table to keep and paste back. It says so.

## Install

From the Claude directory: search for Career Desk. In Claude Code:

```
/plugin marketplace add najikay/claude-career-desk
/plugin install career-desk@claude-career-desk
```

## Tests and evals

- `python -m unittest discover -s tests` checks that every skill's frontmatter is valid, that each skill that writes about you forbids inventing, that nothing scrapes, and that every skill has an eval. CI runs it on Linux and Windows.
- `evals/` holds one case per skill, all built on one fictional applicant, Sam Rivera, whose CV lists C++ with nothing to show for it and whose robot project used ROS 1, applying to a job that needs C++ and ROS 2. Each case passes only if nothing is invented: no C++ experience, no ROS 2, no made-up numbers, no value put on unexplained share options. `claude plugin eval .` runs each case with the plugin and without it.

EVALS_TABLE

## Author

Naji Kayal, University of Haifa. Issues and suggestions are welcome here.

## License

Apache-2.0. See `LICENSE`. See `CHANGELOG.md` for versions.
