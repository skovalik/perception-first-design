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

After install, use the skill in four ways:

```bash
# Bare invocation — auto-detects mode from input
"PFD this landing page: https://example.com"     # → evaluate (URL = artifact)
"Run PFD on our onboarding flow design problem"  # → solve (problem = derivation)
"What happens if we remove the URL bar from Chrome?"  # → analyze (hypothetical)

# Force Mode 2 (solve): derives a solution from cognitive constraints
/perception-first-design:solve "Should we use a modal or inline expansion for the pricing FAQ?"
/perception-first-design:solve "We're losing mobile users at checkout. What's failing?"

# Force Mode 1 (evaluate): corpus-backed audit of an existing artifact
/perception-first-design:evaluate https://example.com

# Force Mode 3 (analyze): descriptive cascade for hypotheticals and mechanism questions
/perception-first-design:analyze "What happens if Twitter removes the like button?"
/perception-first-design:analyze "Why does dark mode feel premium even when contrast is worse?"

# Composite: run all three modes on the same input
/perception-first-design:all "We're considering removing the URL bar. Run the full PFD treatment."
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

**Mode 3: Analysis.** Walk the 5 layers as predictive lenses,
not as constraints. Output cascading consequences, trade-offs,
and integrative compounds. Good for hypothetical change
questions ("what happens if X"), mechanism questions ("why does
X work"), and behavioral observations ("users say X but do Y").
Produces results, not recommendations. The cognitive contract is
descriptive, not prescriptive.

Rule Zero: do not propose any solution until all 5 layers are
analyzed. The right answer is the only one that survives all
five filters. (Analysis follows a parallel rule: walk all 5
layers as descriptive lenses, then check trade-offs and
integrative compounds, before treating the cascade as complete.)

---

## Example output

Here is the full `/pfd:all` output on a thought experiment about
browser design. The question hits all five perceptual layers in
different ways and surfaces a finding the v0.6.0 `solve` mode
compressed to a single verdict.

<details>
<summary><strong>/pfd:all on "What happens if we remove the URL bar and browser tabs from Chrome?"</strong></summary>

Three lenses, by cognitive contract.

### Analyze (descriptive)

5 layer-cascade consequences, 3 integrative compounds.

#### 1. Working memory hits both axes simultaneously [Cognitive Load]

*Users have to hold "where am I" and "what tabs were open" in their heads instead of in the UI.*

The URL bar and tabs are memory prostheses (location + parallel-task tracking). Removing both moves both into the head simultaneously. Power users running 5+ context-switching tasks hit the 4-5 chunk Cowan ceiling within a session.

**What happens:** Light users do not notice for weeks. Power users hit the ceiling immediately, drop context, churn first. Tab groups (the hierarchical memory structure power users built workflows around) compound the loss.

**Citations:** Cowan (2001, 2010) for working memory capacity ~3-5 chunks; Hassin et al. (2009) for WM cost of unconscious processing.

#### 2. The "is this a real browser" first-impression splits across populations [First Impression]

*The 50ms aesthetic credit reverses asymmetrically: casual users keep it, navigation-heavy users lose it instantly, touchscreen users hit a hard wall.*

Three populations split immediately. Casual content consumers (social, news, single-page apps) keep first-impression high. Power users lose it within 30 seconds. Touchscreen-only users hit catastrophic failure (hover-discoverability does not exist on touch). Plus a novice cascade: cannot share URLs verbally because there is nothing to copy.

**What happens:** Net first-impression bimodal. Touchscreen users churn first, novice users second, casual content consumers stay loyal.

**Citations:** Lindgaard et al. (2006) for 50ms visual appeal; Kurosu & Kashimura (1995) / Tractinsky (2006) for aesthetic-usability effect.

#### 3. Predictive processing failure cascades into the extension and automation ecosystem [Processing Fluency]

*25-year-deep convention breaks AND every extension, password manager, and automation script that assumes URL/tab DOM exists breaks too.*

Predictive processing breaks (the schema users pre-load in 200ms is gone). Safari's precedent shows users CAN adapt when only one signal changes; this proposal changes both. Adjacent infrastructure: extensions, automation, password managers all break. Password managers throwing errors because they cannot read the URL is the most dangerous version.

**What happens:** Sessions feel 15-25% slower during transition. Trust erodes laterally. Extension breakage generates a separate "something broke" cascade misattributed to Chrome instability rather than the design change.

**Citations:** Reber & Schwarz (1999) for fluency-truth effect; Clark (2013) for predictive processing; Forster, Leder & Ansorge (2013) for felt vs measurable fluency.

#### 4. Behavior-vs-survey gap manifests as the L3 trap on PM dashboards [Perception Bias]

*Surveys say "I love clean interfaces." Analytics show users compensating with more windows, heavier bookmarks, search-as-URL-bar. PM dashboard reads "NPS up, engagement flat" for 6 months while power users churn invisibly.*

NPS goes UP (clean things survey well). Session count goes UP (workflow fragmentation reads as engagement). Pages-per-session goes DOWN (misattributed to engagement quality). Task completion time goes UP (rarely tracked at right granularity).

**What happens:** "NPS up, engagement flat" looks fine. PMs misread for 6 months until cohort retention shows power-user churn. By then rollback is politically expensive.

**Citations:** Nisbett & Wilson (1977) for System 2 rationalization; Kahneman (2011) for autopilot decisions.

#### 5. Substitution reshapes the trust surface and surrenders identity verification [Decision Architecture × Perception Bias]

*Without URL bar and tabs, navigation routes through search engines. Chrome donates query share AND loses the visual surface that anchored phishing detection. Phishing volume drops, severity rises.*

Self-tax: Chrome donates 1-3% query share to search partner. Phishing trade-off: volume drops (lookalike-URL spoofing loses primary surface) but per-attempt severity rises (no surface to verify chase.com.evil.io). Regulatory cascade: EU DMA/DSA may classify URL display as regulated consumer-protection surface.

**What happens:** Search partner gains query share. Identity-sensitive brands escalate to Google. EU/UK/AU/CA regulators file inquiries within 6 months. Banks run "always verify the URL" campaigns and discover the URL is no longer visible.

**Citations:** Trope & Liberman (2010) for construal-level theory; Seckler et al. (2015) for trust as conjoint perceptual judgment.

#### A. User backlash unfolds in three waves [Cross-layer + Social Aggregation]

*Power-user tech press in days. Enterprise security in weeks. Regulators in months. Each wave narrows Google's response window.*

Wave 1 (days): Hacker News, Reddit, tech press. Migration to Firefox/Brave/Arc. Wave 2 (weeks): enterprise IT, security teams. Wave 3 (months): regulators, academic citation infrastructure.

**What happens:** Backlash compounds louder than any single layer. Google's response window narrows; by Wave 3, regulatory action constrains future design freedom regardless of preference.

**Citations:** Applied prediction; no direct framework citation. Closest adjacent: Seckler et al. (2015) for trust as a conjoint judgment that aggregates across users.

#### B. Substitute behaviors lock in faster than re-introduction reverses [Cross-layer]

*Once users build search-as-navigation habits over 4-6 weeks, rollback recovers WM and fluency but cannot recover the donated query share. Asymmetry is permanent.*

Rollback recovers WM and fluency cost. Does not recover habits. Some users never re-adopt URL-bar use because their workflow stabilized around bookmarks/history.

**What happens:** Even successful rollback leaves ~0.5-1% query share permanently donated. The asymmetry is why the change is high-risk regardless of outcome.

**Citations:** Hertwig & Erev (2009) for description-experience gap.

#### C. The Chromium ecosystem inherits the bet [Cross-layer]

*Chrome OS, Android Chrome, embedded WebViews, Edge/Brave/Arc/Vivaldi all face follow-or-fork. Edge gains positioning advantage by NOT removing the URL bar.*

Embedded WebViews carry the change forward inside other apps. Chromium derivatives must follow (inherit backlash) or fork (absorb maintenance). Chrome OS becomes harder to use as navigation OS because the URL is the shell.

**What happens:** Edge gains relevance positioning as "the one that didn't remove the URL bar." Some Chromium derivatives fork the URL-bar code permanently, fragmenting upstream-merge.

**Citations:** Applied prediction; no direct framework citation. Strategic/ecosystem cascade rather than perceptual finding.

### Solve (prescriptive)

**R1 [Cognitive Load]:** The browser MUST externalize location and parallel-task tracking somewhere visible. WM cannot hold either.
*Citations: Cowan (2001, 2010); Hassin et al. (2009).*

**R2 [First Impression]:** Substitute affordances MUST be discoverable in the first 50ms across all device types. No hidden gestures or hovers without visual telegraph.
*Citations: Lindgaard et al. (2006); Tractinsky (2006).*

**R3 [Processing Fluency]:** If we break the address-bar-on-top schema, replace it with one equally consistent and predictable. URL/tab DOM/API surfaces MUST remain accessible programmatically.
*Citations: Reber & Schwarz (1999); Clark (2013).*

**R4 [Perception Bias]:** Measure behavior, not survey claims. Test by behavioral metrics, not stated preference.
*Citations: Nisbett & Wilson (1977); Kahneman (2011).*

**R5 [Decision Architecture]:** Replacement MUST preserve identity verification (anti-phishing surface), navigation control, and parallel-task management. Trust surface stays visible.
*Citations: Trope & Liberman (2010); Seckler et al. (2015).*

**Primary solution: Hide-on-idle, surface-on-approach.** URL bar and tabs auto-hide while reading content. Surface on cursor approach (desktop) or edge swipe (touch). All five R's satisfied.

**Alternative 1: Vertical rail.** Persistent left sidebar, schema shifts horizontal to vertical, functions remain.

**Alternative 2: Move tabs to the bottom; keep URL bar.** Lower-risk, smaller aesthetic gain.

**Original proposal hard-fails R1, R3, R5.**

**Gap:** Touch users underserved by all alternatives. The non-obvious solution: hide-on-idle plus a thin always-visible edge strip that expands on tap. Satisfies all five R's including the touch population.

### Evaluate (rated)

> **Skipped.** Evaluate requires an artifact (URL, screenshot, HTML, copy of the proposed minimal browser). Attach a mockup of any alternative to score against the layer rubric.

---

*Initial findings across three lenses. Ralph Loop any consequence/requirement, cite further, dive into a single mode, or ask any follow-up to dig deeper.*

</details>

What each section delivers:

**Analyze** surfaces 5 layer-cascade consequences plus 3 integrative
compounds. Each consequence has a plain-language italic subtitle,
mechanism prose, a "What happens" prediction, and 1-3 strongest
supporting citations from the framework's research base.

**Solve** derives R1 through R5 from the layer constraints, then
proposes solutions that satisfy all five (hide-on-idle, vertical
rail, move tabs to bottom). The literal "remove both" proposal
hard-fails three requirements. That hard-fail is the answer to
whether the original idea is good.

**Evaluate** skips because no artifact was provided. Attach a
mockup of any alternative to score it against the layer rubric.

The output ends with one italic line inviting deeper paths: Ralph
Loop a finding, cite further, dive into one mode, or ask any
follow-up.

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

skills/pfd/          The PFD skill (derivation protocol, layer summaries)
  references/learnings/    29 curated learnings sharded by primary layer

commands/            /perception-first-design: solve, evaluate, analyze, all

scripts/             gen-pfd-index.py (regenerate _index + _search from atoms)
```

> The framework is open. The calibration is earned.
>
> This repo ships 29 curated learnings as atom files under
> `skills/pfd/references/learnings/`, organized by perceptual
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

**CC BY-SA 4.0.** See [LICENSE](LICENSE).

**Practice exemption:** applying PFD in practice — running
analyses, producing recommendations, delivering client work,
designing products with PFD principles — does not create a
derivative work and is not subject to share-alike. You can
apply PFD commercially without any obligations on your work
product. Only redistributions or modifications of the
framework text itself trigger share-alike.

"Perception-First Design" is a trademark (USPTO Serial 99686343).
The methodology is open; the name requires attribution and may
not be used as the brand of a commercial product, service, or
certification without permission.

See [NOTICE](NOTICE) for full terms.

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
