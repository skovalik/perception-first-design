
# Perception-First Design (PFD) — v0.3.8

**Author:** Stefan Kovalik / Aurochs
**Framework version:** 3.5 (2026-04-02) — 82 citations, pre-verbal arousal as unified objective, predictive processing backbone
**Source of truth:** `framework/PERCEPTION-FIRST-DESIGN.md` — when framework layer descriptions change, update this skill's layer summaries to match. Framework is canonical; this skill is derived.

---

## What PFD Is

A psychology-backed design framework grounded in how human perception actually works. Not "make it pretty" — design for how people perceive, process, and decide.

**The thesis:** Users don't think — until you make them. Attention is OFF by default. The design question isn't "don't waste their attention" — it's "when you activate their attention, what do they think about, how do they feel, and what do they do next?"

Applies to anything that communicates with humans: interfaces, landing pages, emails, ads, copy, presentations, proposals, pitches, product descriptions, documentation. The five layers exist to produce pre-verbal arousal — the viewer's nervous system firing before their analytical mind engages.

---

## The Two Modes

**Mode 1: PFD Evaluation (Checklist)**
Walk an existing design through the 5 layers. Each layer validates or flags. Good for quick audits.

**Mode 2: PFD Derivation (Generative)**
Work bottom-up through the 5 layers. Each layer produces a hard REQUIREMENT. The solution emerges from the accumulated constraints — not from intuition or domain convention.

**Always prefer Mode 2 unless the user explicitly asks for a quick audit.**

---

## The 5-Layer Dependency Stack

Fix bottom-up. Upstream failures block everything downstream.

### Foundation (L0): Cognitive Load Reduction
> "Can't perceive anything without the bandwidth to do so."

- Working memory: ~3-5 chunks (Cowan, 2001, 2010 — not Miller's "7±2")
- Extraneous load (poor design) must be eliminated to free bandwidth for intrinsic load (the task)
- When processing exceeds capacity → brain defaults to leaving
- **Constraint type:** Capacity ceiling on simultaneous processing

**In practice:** Reduce choices. Progressive disclosure. Smart defaults. Delete unnecessary fields.
**Failure signals:** Form abandonment, high bounce on option-heavy pages, "where do I click?"

### Layer 1: First-Impression Architecture
> "Your site has 50 milliseconds."

- Visual appeal judgments form in 50ms (Lindgaard et al., 2006)
- Aesthetic-usability effect: beautiful = perceived as more functional (Kurosu & Kashimura, 1995)
- The first impression IS the activation point — switches attention from OFF to ON
- **Constraint type:** Temporal gate — if it fails, nothing downstream gets evaluated

**In practice:** Hero/opening = thesis statement. Visual quality must match price point.
**Failure signals:** High bounce + low time-on-page. "Looks sketchy." Competitors with worse products winning.

### Layer 2: Processing Fluency
> "If it's easy to process, it feels true."

- Easy-to-read fonts judged as more TRUE (Reber & Schwarz, 1999)
- Effect generalizes: truth, confidence, liking, trust (Alter & Oppenheimer, 2009)
- Cross-modal sensory coherence: all elements tell the same story (Spence, 2011)
- Consistency > creativity. Inconsistency compounds as trust erosion.
- **Constraint type:** Signal quality — inconsistency degrades truth/trust signal

**In practice:** 2 fonts max. 3-4 colors. Consistent spacing. Consistent voice and tone.
**Failure signals:** Inconsistent branding across touchpoints. Visual/verbal quality ≠ price point.

### Layer 3: Perception Bias Optimization
> "It's not for you. It's for them."

- Users autopilot decisions, rationalize after (Nisbett & Wilson, 1977; Kahneman, 2011)
- Surveys = System 2 rationalization. Analytics = System 1 behavior. The gap = where problems hide.
- Predictive processing: brain generates predictions; match = autopilot; violation = attention fires (Clark, 2013)
- **Constraint type:** Information asymmetry — what users say ≠ what they respond to

**In practice:** Design for what analytics shows, not what surveys say. Test emotional response, not stated preference.
**Failure signals:** "Users say they want X but do Y." Internal team preferences ≠ user behavior.

### Layer 4: Decision Architecture
> "Build the trail."

- Structure the environment so the right choice is the easiest choice
- Ethical persuasion: Alignment (user goals = business goals), Sincerity (what you show = what you deliver), Golden Rule (would you be comfortable experiencing this?)
- PFD removes perception barriers to genuine value — does NOT create perception of value where none exists
- **Constraint type:** Behavioral structure — the environment shapes the decision

**"Fewer options" is context-dependent.** Reducing choices reduces paralysis *at decision points* — purchase pages, one-time commitments, unfamiliar options. It does NOT apply in expert tool palettes, browse/reference interfaces, or workspace contexts where option reduction harms productivity. The principle is: simplify decision points, not the entire environment.

**In practice:** CTAs as natural resolution of the experience. Progressive trust-building. No dark patterns. Match option density to context: sparse at conversion points, rich in expert workspaces.
**Failure signals:** Users complete tasks but feel manipulated. High conversion but low retention. Experts frustrated by hidden/reduced tooling.

---

## The Derivation Protocol

**Rule Zero:** Do NOT propose any solution until all 5 layers are analyzed and requirements accumulated.

### Step 1 — State the Design Problem
What is the user trying to do? What prevents them? What do they experience?
Do NOT describe the problem as missing features or comparisons to other tools.

### Step 2 — Work Each Layer Bottom-Up
For each layer (Foundation → L1 → L2 → L3 → L4):
  a. State the constraint (biological/psychological hard limit)
  b. State the violation (how current design fails this constraint)
  c. Derive the REQUIREMENT (what design MUST do — not "should")
  d. Label it R[n]

### Step 3 — Accumulate Requirements
List R1-R5. All non-negotiable. Solution must satisfy ALL simultaneously.
Lower-layer requirements win conflicts.

### Step 4 — Derive the Solution
What satisfies R1 AND R2 AND R3 AND R4 AND R5?
If no single intervention covers all five, what minimal set does?

### Step 5 — Test Against Proposals (if any)
Check existing proposals against full requirement set. Note failures.

### Step 6 — Identify the Gap
Requirements that no proposal satisfies = where the non-obvious solution lives.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails |
|---|---|
| Solution-first ("we need a sidebar") | Contaminates requirement space |
| Competitive copying ("Miro does X") | Domain-driven, not perception-driven |
| Engineering-first ("what's fastest?") | Optimizes effort, not perception |
| Checklist mode (evaluating post-hoc) | Refines but doesn't generate |
| Skipping layers | Dependency stack violation |
| Soft requirements ("should" not "must") | Lets solutions slide past gaps |

---

## After Applying PFD

---

## Reference Files

Load these when relevant:

- **`references/citation-standards.md`** — Required when presenting PFD publicly or to clients. Distinguishes hard science from practitioner synthesis.
- **`references/pfd-spatial-extension.md`** — Load when applying PFD to canvas tools, spatial interfaces, or layout systems (Cognograph, Figma, Miro, Notion).

Full framework: `framework/PERCEPTION-FIRST-DESIGN.md` (700+ lines, 82 citations)

---

## Corpus-Backed Evaluation (v1)

When performing a PFD evaluation (Mode 1: Checklist or Mode 2: Derivation), load the corpus for deeper analysis:

1. Read `corpus/core/tier2-prompt-template.md` for the evaluation protocol
2. Follow the loading sequence in the template (rubric -> constraints -> design system profile -> heuristic rules -> worked examples)
3. Apply the evaluation instructions from the template
4. After evaluation, document findings for future reference

The corpus provides:
- **Heuristic rules** (`corpus/heuristics/`) — specific detection criteria with psychology citations
- **Design system profiles** (`corpus/design-systems/`) — framework-specific detection and fix prescriptions
- **Worked examples** (`corpus/worked-examples/`) — calibration anchors showing what each score range looks like

**When to use corpus vs. quick evaluation:**
- Quick PFD scan (no URL, just looking at a design): Use the skill's 5-layer stack directly (no corpus needed)
- Full PFD audit (URL provided, detailed analysis requested): Load the corpus per the template
- PFD derivation (generating a design): Load design system profile for constraint-setting

---

## Version History

- **v0.3.8** (2026-04-02): Unified objective statement added to "What PFD Is": pre-verbal arousal as the explicit goal of the 5-layer stack.
- **v0.3.7** (2026-03-16): Canonicalized layer numbering: Foundation (L0) → L1 → L2 → L3 → L4. Fixed off-by-one error (was L2-L5). No framework content changed — numbering alignment only.
- **v0.3.6** (2026-02-26): Learning #16 (near-miss color asymmetry). Framework v3.3: added Bujack et al. 2022 + Brainard 2022 (55 citations). L2 color qualifier (perceptual vs physical space, OKLCH). Design-token linting near-miss severity weighting. Skeptical analysis of "Schrödinger completed" headlines — cite non-additivity finding, not "completed" framing.
- **v0.3.4** (2026-02-25): Synced with framework v3.2 scholarly audit. 53 citations (5 new). Fixed Tractinsky 2006 mischaracterization, Miller 1956 body text, Zak 2015 hedge. WM 3-4→3-5 per Cowan 2010. Citation-standards.md updated with full audit log.
- **v0.3.0** (2026-02-24): Restructured plugin with proper directory layout. Skill description expanded to cover design, marketing, copywriting, writing, and communication. Learnings, citations, and PFD-S moved to references/ for progressive disclosure. `/pfd` command added.
- **v0.2.0** (2026-02-19): 9-expert PFD brainstorm synthesis. Added learnings #9-12: temporal/session continuity, constraints as distributions, visual channel audit, route vs survey knowledge.
- **v0.1.1** (2026-02-19): Added learnings #6-8 from product-level derivation.
- **v0.1** (2026-02-19): Initial proto. Derivation protocol, 5 layers, PFD-S, 5 accumulated learnings.
