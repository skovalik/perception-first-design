---
name: pfd-audit
description: Run a full PFD corpus-backed evaluation on a URL or HTML. Loads the complete heuristic rules, design system profiles, and psychology corpus for a deep perception analysis.
---

# PFD Audit — Corpus-Backed Evaluation

Run a full Perception-First Design evaluation using the PFD corpus.

## Input

$ARGUMENTS — URL or description of the design to evaluate

## Process

1. Load the PFD skill: Read `skill/skills/pfd/SKILL.md`
2. Load the Tier 2 evaluation template: Read `corpus/core/tier2-prompt-template.md`
3. Follow the template's loading sequence IN ORDER:
   - Slot [2]: Read `corpus/core/pfd-layer-rubric.md`
   - Slot [3]: Read `corpus/core/constitutional-constraints.md`
   - Slot [4]: Read `corpus/core/psychology/mvs-psychology-reference.md`
   - Slot [5]: Read `skill/skills/pfd/references/accumulated-learnings.md` (empty by default; populate as you use PFD, or contribute back via GitHub Issues)
   - Slot [6]: Read `corpus/core/anti-patterns.md`
   - Slot [7]: Read all 5 anchor examples from `corpus/worked-examples/web/example-*.md`
   - Slot [8]: Read `skill/skills/pfd/references/practitioner-corrections.md` (empty by default; populate as you use PFD, or contribute back via GitHub Issues)
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
9. After evaluation + rebuild, document findings for future reference
