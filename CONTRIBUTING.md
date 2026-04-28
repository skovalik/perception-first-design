# Contributing to Perception-First Design

PFD is a living methodology. I built it over 15 years of applied design practice, and it keeps getting sharper. Contributions that improve the framework, expand the corpus, or extend the skill are welcome.

## Channels

Different intents route to different places.

**Issues** for bugs, framework corrections (citation errors, overclaims, gaps), learning submissions (use the issue template), translation proposals, and discussion of in-progress PRs.

**Discussions** for show-and-tell of analyses you've run, Q&A on layer ambiguity or calibration questions, and feature ideas before they're formal requests. The richest contributions for the community right now are practitioners sharing real PFD analyses in show-and-tell.

**Pull requests** for anything in "What I accept" below that's ready to merge.

If you're not sure which channel fits, default to Discussions. I'd rather have the conversation in the right shape than the right place.

## What I accept

**Framework corrections.** You found a citation error, an overclaim, or a gap. These are the most valuable contributions. PFD's credibility depends on honest sourcing.

**New heuristic rules.** Detection rules for the evaluation corpus. Every rule must include a psychology citation explaining the mechanism. "Best practices say so" is not a mechanism.

**Design system profiles.** Bootstrap, Material UI, shadcn, Svelte, Astro, whatever you work with. Follow the format in `corpus/design-systems/web-frameworks/`.

**Worked examples.** Both evaluate (rated audits) and analyze (descriptive cascades) examples welcome. The more diverse the examples, the better the calibration. For evaluate examples, follow the format in `corpus/worked-examples/web/`. For analyze examples, follow the four-element consequence structure (heading, italic concrete subtitle, body with "What happens:" prediction, citations) per `commands/analyze.md`. The canonical path for analyze worked examples is still being decided; for now share them in Discussions show-and-tell while the format settles.

**PFD analyses you've run.** Share in Discussions show-and-tell. Diverse analyses sharpen calibration. If an analysis surfaces a new pattern that should become accumulated knowledge, it can be promoted to a learning atom via the issue template.

**Skill bug reports.** Something broken in the Claude Code plugin? Open an issue. Quick clarifying questions can go in Discussions Q&A first.

**Translations.** The framework is English-only. Translations under CC BY-SA 4.0 are welcome. Attribution to the original is required.

## Quality standards

Every claim must trace to a published citation, or be explicitly labeled as either a practitioner observation (something seen repeatedly in practice) or an applied prediction (something the framework supports without a direct citation, with the closest adjacent citation noted). This is not optional. PFD distinguishes between established science, theoretical frameworks, and practitioner synthesis (see `skills/pfd/references/citation-standards.md`). Your contribution should do the same.

For analyze contributions specifically, each consequence and integrative compound includes a Citations line per the format in `commands/analyze.md`. Applied predictions are tagged transparently rather than fabricated.

For evaluate contributions, follow the rubric and citation expectations in the corpus. New heuristic rules must follow the YAML schema in `corpus/heuristics/universal/`. Worked examples must follow the format in `corpus/worked-examples/web/`. If you're unsure about format, open an issue first.

## Voice

The repository uses voice-scrubbed punctuation: no em-dashes, plain language, first-person "I" rather than corporate "we". Match the existing voice when contributing framework text or atom content. The existing files are the reference; if your contribution looks stylistically like the surrounding work, you're calibrated correctly.

## What I do not accept

Changes to the 5-layer dependency order. That is the core architecture. If you think the ordering is wrong, write it up as a framework correction with evidence and I will evaluate it.

Claims that cite "best practices" without a psychology mechanism. PFD is grounded in cognitive science. "Everyone does it this way" is not a reason.

Promotional content for tools or services.

Changes to the ethical framework's three tests: Alignment, Sincerity, Golden Rule. Those are load-bearing.

## How contributions work

This project is licensed under **CC BY-SA 4.0**. By submitting a pull request you agree that your contribution (text, code, scripts, learnings, atom content, anything) is licensed under CC BY-SA 4.0.

The license includes a practice exemption: applying PFD methodology in your work (consulting, design work, training, building products with PFD principles) does not create a derivative and is not subject to share-alike. See `NOTICE` for the full terms. Share-alike attaches only when you adapt, rewrite, translate, or redistribute the framework text itself.

Your name gets added to CONTRIBUTORS.md.

Learning submissions go through the issue template and I curate them. Accepted learnings land as atom files under `skills/pfd/references/learnings/{layer}/l<NNN>-<slug>.md` with YAML frontmatter; see existing atoms for the shape. Not everything gets promoted, but everything gets read.

## Code of Conduct

This project follows the [Contributor Covenant v2.1](https://www.contributor-covenant.org/version/2/1/code_of_conduct/). Be decent.
