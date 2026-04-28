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
- **Layer cascade:** 5 numbered consequences in cascade order, layer-tagged headings, mechanism prose plus "What happens:" prediction.
- **Integrative compounds:** separate section, letter-labeled (A, B, C, ...), each with `[Cross-layer ...]` tag, mechanism plus "What happens:" prediction.

## Anti-patterns specific to analyze

- **Slipping into solve mode.** Analyze produces predictions, not recommendations. If you find yourself writing "you should" or "the fix is" or "the right approach", stop and re-read the question. The user asked what would happen, not what to do.
- **Treating layers as siloed.** Layer effects compound. Always run Step 4 even if the per-layer cascade feels complete. Backlash, lock-in asymmetry, and ecosystem cascade are not optional checks.
- **One-way effects when trade-offs exist.** "Phishing went UP" was wrong; "phishing TRADED OFF" was right. Check Step 3 ruthlessly, especially on Decision Architecture and Perception Bias consequences.
- **Shallow per-consequence depth.** A single sentence per consequence is insufficient. Each consequence must surface stress-tested findings across at least two of the four Step 2 dimensions.
- **Skipping cross-cutting tags.** Cross-cutting consequences (Layer A × Layer B) are real and must be tagged when they emerge. Phishing as a finding lives at Decision Architecture × Perception Bias; the social backlash compound lives across all five layers.

## After analysis

Log the run per the SKILL.md Insight Log protocol. Mark layer involvement, capture non-obvious findings (especially integrative compounds and bidirectional trade-offs), note `Promote? yes` if the analysis surfaces a candidate learning that generalizes beyond this specific question.
