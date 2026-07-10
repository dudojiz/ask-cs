# Rules

- Commit per each query session. Commit messages must follow type(scope): subject, for example `docs(android): why-anr-occur`
- Before opening a PR, run the `humanizer` skill once (rewrite mode) on the docs added or changed in that PR to strip AI-writing tells. Apply the 기술 문서 criteria — clarity first, remove filler/보일러플레이트, no 숨결 주입. Humanize the PR description the same way: plain prose, no emoji footers, no "Generated with …" lines, no over-structured bold bullet lists.
  - Skill: `/Users/ksh/fruit-matjip-workspace/scripter-ai/.claude/skills/humanizer/` (SKILL.md + patterns-ko/en/common.md)