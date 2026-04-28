---
name: evaluate
description: Evaluate an artifact (URL, HTML, screenshot, copy) with Perception-First Design. Mode 1 corpus-backed evaluation that loads heuristic rules, design system profiles, worked examples, and the psychology corpus to produce a layered scoring with citations.
---

# PFD Evaluate — Corpus-Backed Evaluation

Run a full Perception-First Design evaluation using the PFD corpus.

## Input

$ARGUMENTS — URL, HTML, screenshot, or description of the artifact to evaluate

## Process

1. Load the PFD skill: Read `skills/pfd/SKILL.md`
2. Load the Tier 2 evaluation template: Read `corpus/core/tier2-prompt-template.md`
3. Follow the template's loading sequence IN ORDER:
   - Slot [2]: Read `corpus/core/pfd-layer-rubric.md`
   - Slot [3]: Read `corpus/core/constitutional-constraints.md`
   - Slot [4]: Read `corpus/core/psychology/mvs-psychology-reference.md`
   - Slot [5]: Read `skills/pfd/references/learnings/_index.md` (sharded learnings index — drill into atoms via `skills/pfd/references/learnings/{layer}/l<NNN>-*.md` as relevant)
   - Slot [6]: Read `corpus/core/anti-patterns.md`
   - Slot [7]: Read all 5 anchor examples from `corpus/worked-examples/web/example-*.md`
   - Slot [8]: Read `skills/pfd/references/practitioner-corrections.md` (empty by default; populate as you use PFD, or contribute back via GitHub Issues)
   - Slot [9]: Read `corpus/core/output-schema.md`
4. If a URL is provided, fetch the page and examine the HTML/CSS
5. Detect the design system — read the matching profile from `corpus/design-systems/web-frameworks/`
6. Read all heuristic rule files from `corpus/heuristics/universal/`
7. Execute the evaluation per the template instructions (Slots [10]-[12])
8. After evaluation, **rebuild the top 3 fixes as HTML**:
   - Create a single HTML file demonstrating the corrected sections
   - Use the detected design system's actual tokens, components, and visual language (Tailwind classes, WordPress theme patterns, Shopify Dawn vars — whatever was detected)
   - Include inline comments explaining which PFD layer each fix addresses and why
   - Show ONLY the fixed sections, not the entire page — focused diffs
   - If the site uses a framework with a CDN (Tailwind, Bootstrap), include the CDN link so the HTML renders correctly when opened in a browser
   - Save to `corpus/validation/mvs-results/[site-name]-fixes.html`
   - This is the "what it would look like" artifact — compare original vs rebuilt to validate whether the fixes actually improve the design
9. After evaluation + rebuild, log findings per the SKILL.md Insight Log protocol.

End the output with a single italic line:

> *Initial findings. Ralph Loop a layer score, cite further, switch to solve / analyze, or ask any follow-up to dig deeper.*

Non-negotiable. Single italic line, no bullet menu.
