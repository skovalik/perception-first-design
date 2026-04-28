---
name: all
description: Run all three PFD modes (analyze, solve, evaluate) on the same input. Produces three full outputs side-by-side, one per cognitive contract. Use when a question genuinely warrants multiple cognitive contracts, or when you want to see what the question reveals across descriptive, prescriptive, and rated lenses simultaneously.
---

# PFD All: Three-Mode Composite

Run analyze, solve, and evaluate on the same input. Three outputs, three cognitive contracts, side-by-side.

## Input

$ARGUMENTS. The question, problem, or artifact to run through all three modes.

## When to use this vs. the individual modes

A composite run produces non-redundant output because the three modes have genuinely different cognitive contracts:

- **analyze** tells you what would happen.
- **solve** tells you what would have to be true for it to work.
- **evaluate** tells you whether the proposed thing performs against the rubric.

Use `all` when the question warrants multiple views simultaneously: a hypothetical that you also want to see prescribed for, an artifact you want both audited and re-derived from constraints, or a problem space where you want to see what would happen alongside what should be done.

If you only need one view, use the corresponding single-mode command. Three modes is more expensive in tokens and time.

## Process

If no input is provided, ask: "What should I run through all three PFD modes?"

Load the PFD skill: Read `skills/pfd/SKILL.md`.

Run each mode in sequence. Full output for each, not compressed summaries.

### Section 1: Analyze (descriptive)

Execute the Analysis Protocol from `commands/analyze.md`. Full output: 5 layer-cascade consequences with stress-test depth, integrative compounds, trade-offs folded into the relevant consequence.

### Section 2: Solve (prescriptive)

Execute the Derivation Protocol from `commands/solve.md` and SKILL.md. Full output: R1 through R5 requirements, solution that satisfies all five, alternatives, hard-fail noted.

### Section 3: Evaluate (rated)

If the input includes an artifact (URL, screenshot, HTML, copy block), execute the corpus-backed evaluation from `commands/evaluate.md`. Full output: layer-by-layer scoring with citations.

If no artifact is provided, output a one-line skip note:

> **Evaluate skipped.** Evaluate requires an artifact (URL, screenshot, HTML, copy). Attach one to score against the layer rubric.

## Output format

Top-level title: the input question or problem.
Top-level subtitle: "Three lenses, by cognitive contract."

Section headings:
- `## Analyze (descriptive)`
- `## Solve (prescriptive)`
- `## Evaluate (rated)`

No synthesis section in v0.7.0. The three views sit side by side. Where they agree is convergent signal; where they contradict is where the question's actual cognitive contract lives, and that contradiction is the most valuable output of the composite run.

## After execution

Log the run per the SKILL.md Insight Log protocol. Note that this was a three-mode composite. The most valuable runs are usually those where the three modes contradict; those reveal mismatches between question shape and what the user actually needed.
