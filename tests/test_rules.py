"""The promises every Career Desk skill makes, checked in the text so an edit cannot drop one quietly."""

import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS = sorted((ROOT / "skills").glob("*/SKILL.md"))


class Rules(unittest.TestCase):
    def test_skills_that_write_about_the_user_forbid_inventing(self):
        for name in ("cv-review", "cv-tailor", "cover-letter", "interview-prep", "job-fit"):
            text = (ROOT / "skills" / name / "SKILL.md").read_text(encoding="utf-8").lower()
            self.assertTrue(re.search(r"never|nothing is added|no added|do not", text), name)
            self.assertTrue("invent" in text or "added" in text or "supply" in text, f"{name}: say that nothing is invented")

    def test_no_skill_scrapes_or_needs_a_tool(self):
        for f in SKILLS:
            text = f.read_text(encoding="utf-8").lower()
            for word in ("scrape", "crawl", "mcp", "api key"):
                self.assertNotIn(word, text, f"{f}: {word}")

    def test_every_skill_has_an_eval_and_the_manifests_agree(self):
        for f in SKILLS:
            case = ROOT / "evals" / f.parent.name
            self.assertTrue((case / "prompt.md").is_file() and (case / "graders" / "criteria.md").is_file(), f.parent.name)
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["version"], market["plugins"][0]["version"])
        self.assertEqual(plugin["name"], market["plugins"][0]["name"])
        self.assertTrue((ROOT / plugin["icon"]).is_file())
        self.assertIn(f"## {plugin['version']}", (ROOT / "CHANGELOG.md").read_text(encoding="utf-8"))

    def test_the_readme_lists_every_skill(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for f in SKILLS:
            self.assertIn(f"**{f.parent.name}**", readme, f.parent.name)


if __name__ == "__main__":
    unittest.main()
