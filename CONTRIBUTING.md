# Contributing to Perception-First Design

PFD is a living methodology. I built it over 15 years of applied design practice, and it keeps getting sharper. Contributions that improve the framework, expand the corpus, or extend the skill are welcome.

## What I accept

**Framework corrections.** You found a citation error, an overclaim, or a gap. These are the most valuable contributions. PFD's credibility depends on honest sourcing.

**New heuristic rules.** Detection rules for the evaluation corpus. Every rule must include a psychology citation explaining the mechanism. "Best practices say so" is not a mechanism.

**Design system profiles.** Bootstrap, Material UI, shadcn, Svelte, Astro, whatever you work with. Follow the format in `corpus/design-systems/web-frameworks/`.

**Worked examples.** PFD evaluations at any score range. The more diverse the examples, the better the calibration. Follow the format in `corpus/worked-examples/web/`.

**Skill bug reports.** Something broken in the Claude Code plugin? Open an issue.

**Translations.** The framework is English-only. Translations under CC BY-SA 4.0 are welcome. Attribution to the original is required.

## Quality standards

Every claim must trace to a published citation or be explicitly labeled "practitioner observation." This is not optional. PFD distinguishes between established science, theoretical frameworks, and practitioner synthesis (see `skills/pfd/references/citation-standards.md`). Your contribution should do the same.

New heuristic rules must follow the YAML schema in `corpus/heuristics/universal/`. Worked examples must follow the format in `corpus/worked-examples/web/`. If you're unsure about format, open an issue first.

## What I do not accept

Changes to the 5-layer dependency order. That is the core architecture. If you think the ordering is wrong, write it up as a framework correction with evidence and I will evaluate it.

Claims that cite "best practices" without a psychology mechanism. PFD is grounded in cognitive science. "Everyone does it this way" is not a reason.

Promotional content for tools or services.

Changes to the ethical framework's three tests: Alignment, Sincerity, Golden Rule. Those are load-bearing.

## How contributions work

This project is dual-licensed. By submitting a pull request you agree that:

- Contributions to `commands/`, `scripts/`, and `.claude-plugin/` (code, loaders, scripts) are licensed under **MIT**.
- Contributions to `framework/`, `corpus/`, and `skills/pfd/references/learnings/` (text, learnings, corpus content, documentation) are licensed under **CC BY-SA 4.0**.

Your name gets added to CONTRIBUTORS.md.

Learning submissions go through the issue template and I curate them. Accepted learnings land as atom files under `skills/pfd/references/learnings/{layer}/l<NNN>-<slug>.md` with YAML frontmatter; see existing atoms for the shape. Not everything gets promoted, but everything gets read.

## Code of Conduct

This project follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be decent.
