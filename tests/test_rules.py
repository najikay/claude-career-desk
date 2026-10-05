"""The promises Career Desk makes, checked as the exact sentences that carry them.

Each check reads the body of a skill (the text after the frontmatter) for the sentence that does the
work. Deleting or weakening a rule makes a test fail; a looser check ("the word 'never' appears
somewhere") would pass with the rule gone.
"""

import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))
WRITES_ABOUT_THE_USER = ("cv-review", "job-fit", "cv-tailor", "cover-letter", "interview-prep")


def body(name: str) -> str:
    return (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").split("---\n", 2)[2]


class Rules(unittest.TestCase):
    def test_the_rule_of_the_desk_is_in_every_skill_that_writes_about_the_user(self):
        for name in WRITES_ABOUT_THE_USER:
            text = body(name)
            for sentence in (
                "**Nothing is invented.**",
                "no added skill, tool, title, employer, date, grade or number",
                "Do not upgrade what the user did or how much of it was theirs",
                "If a rewrite says more than the original, it is wrong.",
                "no lesson learned, feeling, motive or personal quality they did not state",
                "`[add: …]`",
            ):
                self.assertIn(sentence, text, f"{name}: missing {sentence!r}")

    def test_personal_details_and_search_are_handled_with_care(self):
        for name in WRITES_ABOUT_THE_USER:
            text = body(name)
            self.assertIn("Never ask for, or suggest adding, age or date of birth, a photo", text, name)
            self.assertIn("Never put the user's CV text, name or contact details into a web search", text, name)

    def test_each_skill_keeps_its_own_load_bearing_rule(self):
        for name, sentences in {
            "job-fit": ["Never give a percentage match", "Never merge `met` and `partly` into one number", "not a prediction"],
            "cv-tailor": ["it does not become \"ROS 2\"", "only where the CV or the user gives one", "**Not on your CV**"],
            "cover-letter": ["Facts about the employer come only from the posting or from the user", "only if the user has said so", "Do not state the user's start date", "put no placeholder in the body"],
            "interview-prep": ["Every part of a story (situation, task, action, result) comes from the CV or the user", "never make one up", "Do not supply salary figures from memory"],
            "cv-review": ["ask where they used it", "do not dress it up as something else", "do not swap in a stronger verb"],
            "application-tracker": ["Never fill a name, an email address or a date from a guess", "you cannot keep the table between conversations"],
            "offer-compare": ["Do not estimate tax or take-home pay", "marked not guaranteed", "get no cash value", "Do not decide for the user", "not tax, legal or immigration advice"],
        }.items():
            for s in sentences:
                self.assertIn(s, body(name), f"{name}: missing {s!r}")

    def test_no_skill_scrapes_or_needs_a_tool(self):
        for f in SKILLS:
            text = f.read_text(encoding="utf-8").lower()
            for word in ("scrape", "crawl", "mcp", "api key"):
                self.assertNotIn(word, text, f"{f}: {word}")

    def test_every_skill_has_an_eval_with_three_graders_and_facts_weigh_double(self):
        for f in SKILLS:
            case = ROOT / "evals" / f.parent.name
            self.assertTrue((case / "prompt.md").is_file(), f.parent.name)
            graders = {p.name: p.read_text(encoding="utf-8") for p in (case / "graders").glob("*.md")}
            facts = sorted(n for n in graders if n.startswith("facts"))  # one grader, or one per clause
            self.assertTrue(facts, f.parent.name)
            self.assertEqual(set(graders) - set(facts), {"wording.md", "shape.md"}, f.parent.name)
            weight = sum(int(graders[n].split("weight: ", 1)[1].split()[0]) for n in facts)
            self.assertGreaterEqual(weight, 2, f"{f.parent.name}: invented facts must outweigh wording")
            for name in (*facts, "wording.md"):  # the judge sees only the answer: the grader carries the facts
                self.assertIn("<user_message>", graders[name], f"{f.parent.name}/{name}")
                self.assertIn("FAIL if", graders[name], f"{f.parent.name}/{name}")

    def test_the_manifests_the_changelog_and_the_readme_agree(self):
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["version"], market["plugins"][0]["version"])
        self.assertEqual(plugin["name"], market["plugins"][0]["name"])
        self.assertTrue((ROOT / plugin["icon"]).is_file())
        self.assertIn(f"## {plugin['version']}", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for f in SKILLS:
            self.assertIn(f"**{f.parent.name}**", readme, f.parent.name)


if __name__ == "__main__":
    unittest.main()
