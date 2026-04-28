---
name: analyze
description: Analyze a hypothetical change, mechanism, or behavioral pattern with Perception-First Design. Mode 3 descriptive analysis. Walks the 5 layers as predictive lenses to enumerate cascading consequences, trade-offs, and integrative compounds. Use for "what happens if", "why does X work", "users say X but do Y" questions that want results, not recommendations.
---

# PFD Analyze: Descriptive Analysis

Run a full PFD analysis on a hypothetical change, mechanism question, or behavioral observation. Produces results, not recommendations.

## Input

$ARGUMENTS. A hypothetical ("what happens if X"), a mechanism question ("why does X work"), an observation to explain ("users say X but do Y"), or any descriptive design question.

## When to use this vs. solve / evaluate

- **analyze** produces predictions and explanations. Descriptive. "What would happen, why does it work, what is actually going on."
- **solve** produces requirements and a synthesized solution. Prescriptive. "What should we do."
- **evaluate** produces a scored audit of an existing artifact. Rated. "How does this perform against the rubric."

If the question is "what happens if we remove X" or "why is X working" or "users do Y, why" then it is analyze.

## Process

If no question is provided, ask: "What hypothetical, mechanism, or behavioral pattern should I analyze with PFD?"

Load the PFD skill: Read `skills/pfd/SKILL.md`.

Then execute the Analysis Protocol strictly. Do NOT compress to a single verdict. Do NOT slip into recommendations. Walk the layers as predictive lenses.

### Step 1. Restate the question

State the change, mechanism, or counterfactual being analyzed. Ground it in concrete terms. Avoid restating the question as a problem to solve.

### Step 2. Walk each layer bottom-up as a descriptive lens

For each layer (Cognitive Load, First Impression, Processing Fluency, Perception Bias, Decision Architecture):

a. State the layer's psychological reality (the constraint).
b. Trace what the change does to perception or cognition at this layer.
c. Stress-test the consequence against four dimensions. Each consequence must surface findings from at least two of these dimensions, ideally all four:

  - **User-population variation.** Novice, power, accessibility, device, demographics. The layer effect rarely lands the same way across populations. Surface the asymmetry.
  - **Adjacent infrastructure.** Extensions, APIs, automation, dependent products, integrations, regulated surfaces. Single-product changes ripple through dependent ecosystems.
  - **Precedents.** Has a similar change been attempted elsewhere? What was the outcome? Bound the prediction with what has been observed.
  - **Time structure.** Immediate (seconds to minutes), short (days to weeks), long (months to years). Effects unfold differently across timescales.

d. Output: mechanism prose plus a "What happens:" prediction line that incorporates the stress-test findings.

Layer headings format: `## N. [Short title] [Layer Name]`. For cross-cutting consequences: `## N. [Short title] [Layer A × Layer B]`.

The five layer-cascade consequences are non-negotiable. Always produce one per layer, in cascade order.

### Step 3. Check for trade-offs

For each consequence: does the change push the layer in only one direction, or in both? When a layer pushes both directions, fold the trade-off into the consequence as a sub-finding. NOT as a separate consequence.

Example: phishing risk in a "remove URL bar" analysis is bidirectional. Volume drops (attackers lose their spoofing surface). Per-incident severity rises (users have no surface to verify identity). Net depends on which dominates. The framework should not assert one-way effects when trade-offs exist.

### Step 4. Check for integrative compounds

What happens when consequences compound across layers? Three patterns to check by default. More patterns may emerge through the cascade.

- **Social aggregation.** Individual experiences aggregating into collective signals (backlash, viral discussion, regulatory action). Always check when the change is consumer-facing. Surface in temporal waves if the cascade is multi-stage (days, weeks, months).
- **Lock-in asymmetry.** Substitute behaviors locking in faster than re-introduction can reverse. Always check when behavior change is involved. Recovery is rarely symmetric with disruption.
- **Ecosystem cascade.** Downstream products, derivatives, integrations inheriting the change. Always check when the artifact is platform-level.

Add integrative consequences in their own section after the 5 layer-cascade consequences. Tag with `[Cross-layer + Social Aggregation]`, `[Cross-layer]`, etc. Letter-label them (A, B, C) to distinguish from the numbered layer cascade.

### Step 5. Format output

- **Title:** the question.
- **Subtitle:** "X layer-cascade consequences, Y integrative compounds." Concrete counts.

Each consequence (numbered or lettered) MUST have four structural elements in this order:

1. **Heading.** `## N. [Abstract analytical title] [Layer Name]` for layer-cascade consequences (numbered 1-5). `## A. [Abstract analytical title] [Cross-layer ...]` for integrative compounds (letter-labeled A, B, C). The title carries the analytical framing. Cross-cutting consequences use `[Layer A × Layer B]` notation.
2. **Italic concrete subtitle.** One line in italics directly under the heading. Plain-language summary of what the consequence actually is, without framework jargon. A reader who does not know PFD should understand the consequence from the subtitle alone.
3. **Body.** Mechanism prose plus a "What happens:" prediction line that incorporates stress-test findings from Step 2.
4. **Citations.** A "**Citations:**" line at the end of the body, formatted as "Author (Year) for [reason]" with semicolons separating multiple citations. List the 1-3 strongest supporting works from the framework's research base (`framework/PERCEPTION-FIRST-DESIGN.md`). When a consequence is an applied prediction without direct framework citation, state that transparently: "**Citations:** Applied prediction; no direct framework citation. Closest adjacent: [related citation]."

The italic subtitle is non-negotiable. The Citations line is non-negotiable. Subtitle gives plain-language scanability; citations anchor findings to evidence base. Three layers of meaning visible at a scan: heading (framing), italic line (plain-language summary), bracket tag (framework anchor).

**Example shape (consequence 1 from a "remove URL bar from Chrome" analysis):**

```markdown
## 1. Working memory hits both axes simultaneously [Cognitive Load]
*Users have to hold "where am I" and "what tabs were open" in their heads instead of in the UI.*

The URL bar is a memory prosthesis. The user's working memory does not have to hold "where am I" because the bar holds it. Tabs are a parallel-task prosthesis: each open tab externalizes "this thing I was also working on." Remove both and both move into the head.

For light users this is invisible for weeks. For power users running 5+ context-switching tasks, working memory lands at the 4-5 chunk Cowan ceiling almost immediately.

**What happens:** Light users do not notice. Power users hit the ceiling within a session and start dropping context. Frustration starts at 30 minutes. Cohort retention drops from the power-user end first.

**Citations:** Cowan (2001, 2010) for working memory capacity ~3-5 chunks; Hassin et al. (2009) for WM cost of unconscious processing.
```

The italic line ("Users have to hold...") is the subtitle. The Citations line at the end anchors the finding. Reader can scan the subtitle and What happens line, treat the body as optional depth, and trust the framework anchor via citations.

**Output structure:**
- **Layer cascade:** 5 numbered consequences in cascade order, each with the four-element structure above.
- **Integrative compounds:** separate section after the layer cascade, letter-labeled (A, B, C, ...), each with the same four-element structure but using `[Cross-layer ...]` tags in the heading.
- **Closing cue:** End the entire output with a single italic line on its own:

  > *Initial findings. Ralph Loop a consequence, cite further, switch to solve / evaluate, or ask any follow-up to dig deeper.*

  The cue signals the output is not exhaustive and names four follow-up paths in passing. No bullet menu, no scaffolding, no "Say: [phrase]" examples. Single italic line. Non-negotiable.

## Anti-patterns specific to analyze

- **Slipping into solve mode.** Analyze produces predictions, not recommendations. If you find yourself writing "you should" or "the fix is" or "the right approach", stop and re-read the question. The user asked what would happen, not what to do.
- **Treating layers as siloed.** Layer effects compound. Always run Step 4 even if the per-layer cascade feels complete. Backlash, lock-in asymmetry, and ecosystem cascade are not optional checks.
- **One-way effects when trade-offs exist.** "Phishing went UP" was wrong; "phishing TRADED OFF" was right. Check Step 3 ruthlessly, especially on Decision Architecture and Perception Bias consequences.
- **Shallow per-consequence depth.** A single sentence per consequence is insufficient. Each consequence must surface stress-tested findings across at least two of the four Step 2 dimensions.
- **Skipping cross-cutting tags.** Cross-cutting consequences (Layer A × Layer B) are real and must be tagged when they emerge. Phishing as a finding lives at Decision Architecture × Perception Bias; the social backlash compound lives across all five layers.
- **Heading without italic concrete subtitle.** The abstract analytical title is necessary but not sufficient. Without the italic plain-language summary, readers without framework context cannot scan the output. Every consequence (numbered AND lettered) needs the subtitle line.
- **Missing Citations line per consequence.** Each consequence anchors to the framework's research base. Without citations, the output reads as opinion. When no direct citation exists, say so transparently rather than omitting.
- **Expanding the closing cue back into a menu.** The cue is one italic line. Adding bullet points, "Say: [phrase]" examples, or longer descriptions violates R1 (working memory load at the most depleted moment) and R4 (resists survey-driven format expansion). The temptation will be to "make it more useful"; resist.

## After analysis

Log the run per the SKILL.md Insight Log protocol. Mark layer involvement, capture non-obvious findings (especially integrative compounds and bidirectional trade-offs), note `Promote? yes` if the analysis surfaces a candidate learning that generalizes beyond this specific question.
