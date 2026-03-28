# Perception-First Design

A 5-layer web design methodology grounded in cognitive psychology.
77 peer-reviewed citations. 15 years applied. Open framework.

Created by Stefan Kovalik / [Aurochs](https://aurochs.agency)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## The Thesis

**Users don't think, until you make them.**

The brain runs on prediction. When reality matches expectation, processing is automatic and unconscious (Clark 2013, Friston 2010). When reality violates expectation, conscious attention fires.

Most design advice stops at "don't waste their limited attention." The real problem is that effortful attention is dormant by default, and you have to design the activation.

Krug's *Don't Make Me Think* covered the foundation layer deliberately and well. This framework starts there and builds the other four: five layers, each grounded in peer-reviewed cognitive science, each dependent on the one below it.

## The Five Layers

| Layer | Constraint | Key Citation |
|---|---|---|
| The Foundation (L0) | Working memory: 3-5 chunks | Cowan 2001, 2010 |
| First Impression (L1) | 50ms visual verdict | Lindgaard et al. 2006 |
| Processing Fluency (L2) | Easy to process = feels true | Reber & Schwarz 1999 |
| Perception Bias (L3) | Users autopilot, rationalize after | Nisbett & Wilson 1977 |
| Decision Architecture (L4) | Structure shapes choice | Thaler & Sunstein 2008 |

Fix bottom-up. Upstream failures block everything downstream.

Full framework: [framework/PERCEPTION-FIRST-DESIGN.md](framework/PERCEPTION-FIRST-DESIGN.md)

## ADHD and the Curb-Cut Effect

I designed this framework with autism and ADHD as diagnostic instruments. The cognitive constraints I design around are constraints every user has. Mine are just louder.

A page that overloads an ADHD user's working memory is overloading everyone's; the ADHD user just notices first. Same principle as curb cuts: built for the constrained case, better for everyone.

Full write-up: [framework/ADHD-CURB-CUT.md](framework/ADHD-CURB-CUT.md)

## Quick Start: The 5-Minute Perception Audit

Five tests you can run on any website right now:

1. **Squint test.** Blur your eyes. Can you still see the visual hierarchy?
2. **5-second test.** Show someone for 5 seconds. What do they remember?
3. **Path count.** How many clicks to the primary action?
4. **Consistency check.** Same fonts, colors, spacing everywhere?
5. **The gut check.** Would you buy from this site? The feeling arrives before the reason.

## Use PFD in Claude Code

```bash
# Clone the repo
git clone https://github.com/skovalik/perception-first-design.git

# Point Claude Code at the skill directory
# (add to your project's .claude/ or install as a skill)

# Audit a live site
/pfd-audit https://example.com

# Run PFD on a design decision
/pfd "Should we use a modal or inline expansion for the pricing FAQ?"

# Run PFD on a strategy question
/pfd "We're losing mobile users at checkout. What's failing?"

# Load PFD as the lens for an iterative work session
# (works with persona loops, subagent workflows, or any structured session)
/pfd "Run the derivation protocol on our onboarding flow"
```

**Mode 1: Evaluation.** Walk an existing design through the 5 layers. Each layer validates or flags. Works on URLs, screenshots, mockups, or HTML files.

**Mode 2: Derivation.** Work bottom-up through the 5 layers on any design problem, decision, or question. Each layer produces a hard requirement. The solution emerges from accumulated constraints, not intuition. This is the mode that generates answers you wouldn't have reached by instinct.

### PFD in Ralph Loops

I built a system called Ralph Loop: iterative convergence sessions where five analytical lenses (methodology, sales, operations, technical architecture, UX research) each evaluate the same problem independently. PFD's 5 layers cut across all of them as the shared quality gate.

Each lens scores independently. One checks cognitive load and scannability. Another checks if the methodology is sound. Another asks if it sells. Another asks if it ships sustainably. PFD keeps all five grounded in how people actually process information. The loop continues until all five converge (typically 95+/100 average across 3-4 iterations). That convergence is the signal that something is ready.

PFD is not a one-shot audit in this context. It's the methodology running in the background across every iteration. Layout choices, copy direction, pricing structure, onboarding flows, navigation architecture. The skill loads the framework. The corpus loads the rules. The derivation protocol runs when the question is "what should this be?" instead of "what's wrong with this?"

Ralph Loop + PFD is how I built the Aurochs site, the product workspace plans, and the PFD corpus itself. The methodology evaluated the methodology.

## The Evaluation Corpus

The `corpus/` directory contains 26 heuristic rules across 5 layers, 7 worked examples at different score ranges, and 3 design system profiles (Tailwind, WordPress, Shopify). Same engine that powers [Forge](https://forge.aurochs.agency).

> The framework is open. The calibration is earned.
>
> This repo contains the evaluation engine. Forge adds the correction layer, accumulated learnings, and 15 years of practitioner calibration.

**What you'll need to build yourself:** The corpus gives you the instrument. Accurate scoring requires a correction layer: your own before/after pairs from running evaluations, reviewing the output, and recording where the system got it wrong. Without corrections, LLM-driven heuristic evaluation has roughly an 80% false-positive rate (Baymard Institute finding). With even a dozen corrections loaded as few-shot examples, accuracy improves dramatically. Run `/pfd-audit`, review the output critically, save your corrections. That's how the calibration builds.

## The Generative Protocol

PFD is not just an audit tool. Mode 2 is a generative process for deriving design decisions from cognitive constraints.

Six steps: state the problem, work each layer bottom-up (constraint, violation, requirement), accumulate R1-R5, derive what satisfies all five simultaneously. Rule Zero: do not propose any solution until all 5 layers are analyzed. Each layer constrains what's possible, and by L4 the right answer is the only one that survived all five filters.

This applies to any design decision: layout choices, copy direction, pricing page structure, onboarding flows, navigation architecture, brand positioning. If humans perceive it, PFD has something to say about it.

Full protocol: [framework/PERCEPTION-FIRST-DESIGN.md](framework/PERCEPTION-FIRST-DESIGN.md)

## Evidence Standards

PFD distinguishes claim types:

- **Established science:** Cowan 2001, Lindgaard 2006, Reber & Schwarz 1999
- **Theoretical frameworks:** Clark 2013, Friston 2010
- **Strong practitioner synthesis:** The 5-layer dependency stack
- **Convergent inference:** ADHD-AI collaboration patterns

Full standards: [skill/skills/pfd/references/citation-standards.md](skill/skills/pfd/references/citation-standards.md)

## Case Studies

**Simply Smart Home.** Revenue tripled. I repositioned "digital photo frames" as smart home decor. That perception shift opened Disney licensing, Costco pallet placement, and Walmart shelf space.

**iO Theater.** Online ticket sales went from 50% to 75%. Same shows, same theater, same audiences. Different perception of the buying experience.

**Vacuum Sealers Unlimited.** Revenue 4x over ten years. No redesign. Incremental optimization, compounding trust. I put enough lipstick on the pig to persuade people on the fence.

## The Book

*Make Me Think: Perception-First Design for the Post-Usability Era* by Stefan Kovalik. 12 chapters at [aurochs.agency/writing/make-me-think/](https://aurochs.agency/writing/make-me-think/). The framework is the reference; the book is the story.

## Cognitive Constraint Design

The meta-framework bridging PFD with other domains. Cognitive constraints are design material, not obstacles to work around. PFD applies this to interfaces. The same principle applies to ADHD-AI workflows, spatial tools, and voice models.

## Citation

```
Kovalik, S. (2024-2026). Perception-First Design: A cognitive psychology
framework for web design. Version 3.4. CC BY-SA 4.0.
https://github.com/skovalik/perception-first-design
```

Machine-readable format: [CITATION.cff](CITATION.cff)

## License

CC BY-SA 4.0. Use, adapt, and build on PFD for any purpose, including commercial, as long as you credit the source and share adaptations under the same license.

"Perception-First Design" is a trademark (Serial 99686343). The methodology is open; the name requires attribution.

## Forge

[Forge](https://forge.aurochs.agency) is the automated PFD evaluation tool. It scans URLs and mockups across all five cognitive layers, produces scored audits with actionable fixes, and applies the correction layer from 15 years of practitioner calibration. Free tier available.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Key rule: every claim needs a citation or must be labeled "practitioner observation."

## About

Stefan Kovalik. BA Psychology, UC Santa Barbara. 15 years design and development. Autism and ADHD as diagnostic instruments, not disclaimers.

[aurochs.agency](https://aurochs.agency) / [LinkedIn](https://linkedin.com/in/kovalik/) / [Bluesky](https://bsky.app/profile/stefankovalik.bsky.social)
