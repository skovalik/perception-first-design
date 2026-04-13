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

82 peer-reviewed citations. 15 years applied. Open framework.

Created by Stefan Kovalik / [Aurochs](https://aurochs.agency)

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC_BY--SA_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

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

You see that the hero is fine but Foundation is broken: too many
competing elements burning working memory before visitors even
reach the headline. You see that L2 is leaking trust through
inconsistent spacing the designer didn't notice but the viewer's
nervous system did.

You stop guessing. You fix L0 first because Lavie (1995) proved
that lower-level processing demands eliminate higher-level
processing capacity. Then L1. Then L2. Each fix compounds upward
through the stack because each layer resolving its prediction
errors builds toward the thing every decision actually runs on:

**Pre-verbal arousal.** The viewer's nervous system fires before
their analytical mind engages. They feel the outcome before they
evaluate the offer.

Damasio (1994) showed the body generating emotional signals that
bias decisions before conscious deliberation. LeDoux (1996)
mapped the pathway: emotional response in 12ms, conscious
evaluation in 200-300ms. The feeling arrives first. Always.

Design becomes a lens of empathy to solve with. Not a set of
business objects to align with the user.

The business objectives and the human objectives share the same
framework because the framework IS how people perceive. The
stakeholder can still disagree, but now they're disagreeing with
cognitive psychology, not with someone's taste.

**Simply Smart Home.** Revenue tripled. I repositioned "digital
photo frames" as smart home decor. That perception shift opened
Disney licensing, Costco pallet placement, and Walmart shelf
space.

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
| **Foundation (L0)** | Working memory: 3-5 chunks | Visitor leaves before processing anything. Bandwidth consumed by noise. |
| **First Impression (L1)** | 50ms visual verdict | Attention never activates. Everything downstream multiplies by zero. |
| **Processing Fluency (L2)** | Easy to process = feels true | Trust erodes subconsciously. The visitor can't explain why they don't believe you. |
| **Perception Bias (L3)** | Users autopilot, rationalize after | You're designing for what users SAY instead of what they DO. The gap is where conversions die. |
| **Decision Architecture (L4)** | Structure shapes choice | The trail is broken. Interested visitors can't find the path to action. |

Full framework (700+ lines, 82 citations):
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

Automated design thinking. The PFD skill runs the full
derivation protocol on anything humans perceive: interfaces,
landing pages, emails, ads, pitches, onboarding flows,
documentation.

```bash
# Audit a live site, full 5-layer perception analysis
/pfd-audit https://example.com

# Derive a design solution from cognitive constraints
/pfd "Should we use a modal or inline expansion for the pricing FAQ?"

# Diagnose a conversion problem
/pfd "We're losing mobile users at checkout. What's failing?"

# Run the full derivation protocol on any design problem
/pfd "Run the derivation protocol on our onboarding flow"
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
framework/           The complete PFD framework (v3.5, 82 citations)
  PERCEPTION-FIRST-DESIGN.md
  ADHD-CURB-CUT.md   ADHD and autism as diagnostic instruments, not disclaimers

corpus/              The evaluation engine
  core/              Rubric, constraints, psychology reference, output schema
  heuristics/        26 rules across 5 layers with psychology citations
  design-systems/    Tailwind, WordPress, Shopify detection profiles
  worked-examples/   7 calibrated examples from terrible (18/100) to excellent (92/100)

skill/               Claude Code skill + commands
  skills/pfd/        The PFD skill (derivation protocol, layer summaries)
  commands/          /pfd and /pfd-audit commands
```

> The framework is open. The calibration is earned.
>
> This repo contains the full evaluation engine.
> [Forge](https://forge.aurochs.agency) adds the correction layer
> and 15 years of practitioner calibration. You build your own
> correction layer by running evaluations, reviewing the output
> critically, and recording where the system got it wrong. A dozen
> corrections transforms accuracy from LLM-baseline to
> practitioner-grade.
>
> Templates are included in `skill/skills/pfd/references/`:
> `insights-log.md`, `accumulated-learnings.md`, and
> `practitioner-corrections.md` ship empty, yours to populate. The
> skill's Insight Log protocol shows the format.

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
Kovalik, S. (2024-2026). Perception-First Design: A cognitive
psychology framework for web design. Version 3.5. CC BY-SA 4.0.
https://github.com/skovalik/perception-first-design
```

Machine-readable: [CITATION.cff](CITATION.cff)

## License

CC BY-SA 4.0. Use, adapt, and build on PFD for any purpose,
including commercial, as long as you credit the source and share
adaptations under the same license.

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
