from __future__ import annotations

import contextlib
import importlib.util
import io
import sys
import tempfile
import unittest
import unittest.mock
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = REPO_ROOT / "scripts" / "update_summary.py"


def load_module():
    spec = importlib.util.spec_from_file_location("update_summary", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("failed to load update_summary.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class UpdateSummaryScriptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.module = load_module()

    def test_readme_text_bullet_is_normalized_and_missing_link_is_added(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            folder = Path(tmpdir)
            readme_path = folder / "README.md"
            (folder / "q1.md").write_text("## 질문\n\n> 질문 A?", encoding="utf-8")
            (folder / "q2.md").write_text("## 질문\n\n> 질문 B?", encoding="utf-8")
            readme_path.write_text(
                "# Topic\n\n## 질문 목록\n\n- 질문 A?\n",
                encoding="utf-8",
            )

            updated, changes = self.module.update_readme_question_list(readme_path, readme_path.read_text(encoding="utf-8"))

            self.assertIn("- [질문 A?](q1.md)", updated)
            self.assertIn("- [질문 B?](q2.md)", updated)
            self.assertIn("normalize text bullet to link: 질문 A?", changes)
            self.assertIn("add missing link: q2.md", changes)

    def test_readme_duplicate_links_are_deduplicated(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            folder = Path(tmpdir)
            readme_path = folder / "README.md"
            (folder / "q1.md").write_text("## 질문\n\n> 질문 A?", encoding="utf-8")
            readme_path.write_text(
                "# Topic\n\n## 질문 목록\n\n- [질문 A?](q1.md)\n- [질문 A?](q1.md)\n",
                encoding="utf-8",
            )

            updated, changes = self.module.update_readme_question_list(readme_path, readme_path.read_text(encoding="utf-8"))

            self.assertEqual(updated.count("(q1.md)"), 1)
            self.assertIn("remove duplicate link: q1.md", changes)

    def test_check_mode_prints_detailed_file_changes(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            repo = Path(tmpdir)
            summary_path = repo / "SUMMARY.md"
            topic = repo / "topic"
            topic.mkdir(parents=True)

            summary_path.write_text("# Table of contents\n\n* [Topic](topic/README.md)\n", encoding="utf-8")
            (topic / "q1.md").write_text("## 질문\n\n> 질문 A?", encoding="utf-8")
            (topic / "q2.md").write_text("## 질문\n\n> 질문 B?", encoding="utf-8")
            (topic / "README.md").write_text("# Topic\n\n## 질문 목록\n\n- 질문 A?\n", encoding="utf-8")

            old_root = self.module.REPO_ROOT
            old_summary = self.module.SUMMARY_PATH
            try:
                self.module.REPO_ROOT = repo
                self.module.SUMMARY_PATH = summary_path

                stdout = io.StringIO()
                with contextlib.redirect_stdout(stdout):
                    with unittest.mock.patch.object(sys, "argv", ["update_summary.py", "--check"]):
                        exit_code = self.module.main()

                output = stdout.getvalue()
                self.assertEqual(exit_code, 1)
                self.assertIn("- SUMMARY.md", output)
                self.assertIn("- topic/README.md", output)
                self.assertIn("normalize text bullet to link: 질문 A?", output)
                self.assertIn("add missing link: q2.md", output)
            finally:
                self.module.REPO_ROOT = old_root
                self.module.SUMMARY_PATH = old_summary


if __name__ == "__main__":
    unittest.main()
