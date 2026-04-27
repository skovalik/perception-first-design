# Perception-First Design

**People decide in 50 milliseconds. Now your design process can too.**

Everyone has an opinion about design. They use these products
daily, so the opinion feels earned. But opinions aren't
diagnosis. This is.

---

**A 5-layer diagnostic framework grounded in cognitive
psychology. Tells you which perceptual layer is failing, in what
order to fix it, and why the fix works. Before anyone touches a
pixel.**

~100 peer-reviewed citations. 15 years applied. Open framework.

Created by Stefan Kovalik / [Aurochs](https://aurochs.agency)

[![License: MIT](https://img.shields.io/badge/Code-MIT-blue.svg)](skill/LICENSE)
[![License: CC BY-SA 4.0](https://img.shields.io/badge/Framework-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

---

## What Changes When You Have This

The stakeholder says make the logo bigger. The VP doesn't like
blue. The founder's wife thinks the hero needs a video.

The designer is either pushing pixels to someone else's vision
or burning half their time persuading stakeholders why a bad
instinct is bad. The person on the other end of the screen, how
they actually perceive and decide in 50 milliseconds, is nowhere
in the conversation.

PFD changes the conversation from opinions to diagnosis.

You look at a page and you see the layers. Not the colors, not
the layout, not the copy. The perceptual gates between a human
and a decision.

The hero is fine but L0 is broken: too many competing elements
burning working memory before visitors reach the headline. L2 is
leaking trust through inconsistent spacing the viewer's nervous
system notices before the designer does.

You stop guessing. You fix L0 first because Lavie (1995) proved
that lower-level processing demands eliminate higher-level
processing capacity. Then L1. Then L2.

Each fix compounds upward through the stack, toward the thing
every decision actually runs on: **pre-verbal arousal.** The
viewer's nervous system fires before their analytical mind
engages. They feel the outcome before they evaluate the offer.

Damasio (1994) showed the body generating emotional signals that
bias decisions before conscious deliberation. LeDoux (1996)
mapped the pathway: 12ms emotional response, 200-300ms conscious
evaluation. The feeling arrives first. Always.

Design becomes a lens of empathy to solve with, not a set of
business objects to align with the user. The stakeholder can
still disagree, but now they're disagreeing with cognitive
psychology instead of someone's taste.

**Simply Smart Home.** Revenue tripled after I repositioned
"digital photo frames" as smart home decor. That perception shift
opened Disney licensing, Costco pallet placement, and Walmart
shelf space.

**iO Theater.** Online ticket sales went from 50% to 75%. Same
shows, same theater, same audiences. Different perception of the
buying experience.

**Vacuum Sealers Unlimited.** Revenue 4x over ten years. No
redesign. Incremental optimization, compounding trust.

Same products. Different perception.

---

### The Ralph Loop

LLMs miss things. Not sometimes. Every time. A single pass
through any problem is probabilistically incomplete, the same
way a 3D renderer's first pass produces a noisy image. The
fix is the same too: run it again. Each pass catches what the
last one missed.

The [Ralph Loop](https://github.com/frankbria/ralph-claude-code)
applies this to PFD. Run a design, plan, pitch, or system
through the 5 layers. Loop until exit conditions fire and
completion signals hold up under evaluation. Brute force
repetition against your own instructions, compounding toward
an asymptote.

Round 1 catches the obvious layer violations. Round 2 catches
what only surfaces after the obvious ones are fixed. By round
3, the conversation isn't about opinions. It's about which
perceptual layer the remaining issues live on and what the
science says to do about them.

Match depth to stakes. Quick design decision: 1 pass. Feature
spec: 5. Landing page or pitch deck: 10. Systems architecture
or deep research: 50. I've run 100+ on things that needed it.
Each pass costs more and returns less, so you stop when
confidence stops climbing.

---

## The Five Layers

Fix bottom-up. Upstream failures block everything downstream.

| Layer | Gate | What Breaks If It Fails |
|---|---|---|
| **Cognitive Load (L0)** | Working memory: 3-5 chunks | Visitor leaves before processing anything. Bandwidth consumed by noise. |
| **First Impression (L1)** | 50ms visual verdict | Attention never activates. Everything downstream multiplies by zero. |
| **Processing Fluency (L2)** | Easy to process = feels true | Trust erodes subconsciously. The visitor can't explain why they don't believe you. |
| **Perception Bias (L3)** | Users autopilot, rationalize after | You're designing for what users SAY instead of what they DO. The gap is where conversions die. |
| **Decision Architecture (L4)** | Structure shapes choice | The trail is broken. Interested visitors can't find the path to action. |

Full framework (700+ lines, ~100 citations):
[framework/PERCEPTION-FIRST-DESIGN.md](framework/PERCEPTION-FIRST-DESIGN.md)

---

## Try It

### For Practitioners

Clone the repo. Read the framework. The five layers are a
diagnostic instrument: walk any design, email, pitch, or
onboarding flow through them bottom-up. You'll see what's
broken and why, grounded in the same prediction error logic the
brain runs on.

```bash
git clone https://github.com/skovalik/perception-first-design.git
```

### In Claude Code

Automated design thinking. The PFD skill runs on anything humans
perceive: interfaces, landing pages, emails, ads, pitches,
onboarding flows, documentation.

**Install via your own marketplace** (no review required):

```bash
/plugin marketplace add skovalik/perception-first-design
/plugin install perception-first-design@perception-first-design
```

**Or via the official Anthropic marketplace** (when listed):

```bash
/plugin install perception-first-design@claude-plugins-official
```

After install, use the skill in three ways:

```bash
# Bare invocation — auto-detects mode from input
"PFD this landing page: https://example.com"     # → evaluate (URL = artifact)
"Run PFD on our onboarding flow design problem"  # → solve (problem = derivation)

# Force Mode 2 (solve) — derives a solution from cognitive constraints
/perception-first-design:solve "Should we use a modal or inline expansion for the pricing FAQ?"
/perception-first-design:solve "We're losing mobile users at checkout. What's failing?"

# Force Mode 1 (evaluate) — corpus-backed audit of an existing artifact
/perception-first-design:evaluate https://example.com
```

**Mode 1: Evaluation.** Walk an existing design through the 5
layers. Each layer validates or flags. Works on URLs,
screenshots, mockups, HTML files, copy, emails, pitches.
Anything humans perceive.

**Mode 2: Derivation.** Work bottom-up through the 5 layers.
Each layer produces a hard requirement. The solution emerges from
accumulated constraints, not intuition, not competitive copying,
not what the HiPPO wants. This is the mode that generates
answers you wouldn't have reached by instinct.

Rule Zero: do not propose any solution until all 5 layers are
analyzed. The right answer is the only one that survives all
five filters.

---

## What's in the Repo

```
.claude-plugin/      Plugin manifest + marketplace catalog
  plugin.json        Metadata (name, version, license, keywords, path overrides)
  marketplace.json   Self-hosted marketplace entry pointing at this repo

framework/           The complete PFD framework (v3.6, ~100 citations)
  PERCEPTION-FIRST-DESIGN.md
  ADHD-CURB-CUT.md   ADHD and autism as diagnostic instruments, not disclaimers

corpus/              The evaluation engine
  core/              Rubric, constraints, psychology reference, output schema
  heuristics/        26 rules across 5 layers with psychology citations
  design-systems/    Tailwind, WordPress, Shopify detection profiles
  worked-examples/   7 calibrated examples from terrible (18/100) to excellent (92/100)

skill/               Claude Code skill + commands
  skills/pfd/        The PFD skill (derivation protocol, layer summaries)
  skills/pfd/references/learnings/   29 curated learnings sharded by primary layer
  commands/          /perception-first-design:solve and :evaluate commands
  scripts/           gen-pfd-index.py (regenerate _index + _search from atoms)
```

> The framework is open. The calibration is earned.
>
> This repo ships 29 curated learnings as atom files under
> `skill/skills/pfd/references/learnings/`, organized by perceptual
> layer (`L0/`, `L1/`, `L2/`, `L3/`, `L4/`, `meta/`, `cross/`) with
> a generated `_index.md` and `_search.json` for lazy-load.
>
> Contribute a learning via pull request or the
> [Learning Submission issue template](.github/ISSUE_TEMPLATE/learning-submission.md).

---

## ADHD and the Curb-Cut Effect

I designed this framework with autism and ADHD as diagnostic
instruments. The cognitive constraints I design around are
constraints every user has. Mine are just louder.

A page that overloads an ADHD user's working memory is
overloading everyone's. The ADHD user just notices first. Same
principle as curb cuts: built for the constrained case, better
for everyone.

Full write-up:
[framework/ADHD-CURB-CUT.md](framework/ADHD-CURB-CUT.md)

---

## The Book

*Make Me Think: Perception-First Design for the Post-Usability
Era* by Stefan Kovalik. 12 chapters at
[aurochs.agency/writing/make-me-think/](https://aurochs.agency/writing/make-me-think/).
The framework is the reference; the book is the story.

---

## Citation

```
Kovalik, S. (2025-2026). Perception-First Design: A cognitive
psychology framework for design. Version 3.6. CC BY-SA 4.0.
https://github.com/skovalik/perception-first-design
```

Machine-readable: [CITATION.cff](CITATION.cff)

## License

Dual license. Framework text, learnings, corpus content, and
documentation: **CC BY-SA 4.0**. Skill code, loaders, and scripts
under `skill/`: **MIT**. See
[skill/LICENSE](skill/LICENSE) (MIT) and
[skill/LICENSE-CONTENT](skill/LICENSE-CONTENT) (CC BY-SA 4.0).

Practice exemption: applying PFD in practice (running analyses,
producing recommendations, delivering client work) does not
create a derivative work. Only redistributions or modifications
of the framework text trigger ShareAlike.

"Perception-First Design" is a trademark (Serial 99686343). The
methodology is open; the name requires attribution.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Key rule: every claim
needs a citation or must be labeled "practitioner observation."

## About

Stefan Kovalik. BA Psychology, UC Santa Barbara. 15 years design
and development. Autism and ADHD as diagnostic instruments, not
disclaimers.

[aurochs.agency](https://aurochs.agency) /
[LinkedIn](https://linkedin.com/in/kovalik/) /
[Bluesky](https://bsky.app/profile/stefankovalik.bsky.social)
