---
name: pfd
description: >
  This skill should be used when working on any design, marketing, copywriting, writing, or
  communication task — including: "run PFD", "apply PFD", "use Perception-First Design", "do a
  PFD analysis", "run the derivation protocol"; when designing interfaces, landing pages, emails,
  ads, or visual systems; when writing or reviewing marketing copy, headlines, CTAs, proposals,
  pitches, or presentations; when evaluating conversion problems, bounce rates, engagement, or
  persuasion; when doing brand work, content strategy, or any client communication; or whenever
  cognitive load, first impressions, processing fluency, trust, or decision architecture should
  inform the work.
---

# Perception-First Design (PFD): v0.7.0

**Author:** Stefan Kovalik / Aurochs
**Framework version:** 3.6 (2026-04-20). ~100 citations, international research integration, Methodology Siblings section, Cultural Calibration meta-rule, 7 new layer rules across L0–L4
**Source of truth:** `framework/PERCEPTION-FIRST-DESIGN.md` — when framework layer descriptions change, update this skill's layer summaries to match. Framework is canonical; this skill is derived.
**License:** [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). PFD™ is a trademark of Stefan Kovalik (USPTO serial 99686343). Practice exemption: applying PFD in your work doesn't trigger share-alike. See `LICENSE` and `NOTICE` in the plugin root.
**Path conventions:** All paths in this document are plugin-root-relative. Skill-local paths (`references/...`) resolve from this skill's directory; repo-level paths (`framework/...`, `corpus/...`) resolve from the plugin root.

---

## What PFD Is

A psychology-backed design framework grounded in how human perception actually works. Not "make it pretty" — design for how people perceive, process, and decide.

**The thesis:** Users don't think — until you make them. Attention is OFF by default. The design question isn't "don't waste their attention" — it's "when you activate their attention, what do they think about, how do they feel, and what do they do next?"

Applies to anything that communicates with humans: interfaces, landing pages, emails, ads, copy, presentations, proposals, pitches, product descriptions, documentation. The five layers exist to produce pre-verbal arousal — the viewer's nervous system firing before their analytical mind engages.

---

## The Three Modes

**Mode 1: PFD Evaluation (Checklist)**
Walk an existing design through the 5 layers. Each layer validates or flags. Good for quick audits.

**Mode 2: PFD Derivation (Generative)**
Work bottom-up through the 5 layers. Each layer produces a hard REQUIREMENT. The solution emerges from the accumulated constraints — not from intuition or domain convention.

**Mode 3: PFD Analysis (Descriptive)**
Walk the 5 layers as predictive lenses, not as constraints. Output cascading consequences, trade-offs, and integrative compounds. Good for hypothetical change questions ("what happens if X"), mechanism questions ("why does X work"), and behavioral observations ("users say X but do Y, why"). Produces results, not recommendations. The cognitive contract is descriptive, not prescriptive.

### Mode Detection (Auto)

When the skill activates without an explicit command (e.g., "pfd this", "run PFD on this"), inspect the input and pick the mode:

**Mode 1 — Evaluation**, when the input IS an artifact:
- A URL, web link, or live page
- A screenshot, mockup, image, or PDF
- HTML, CSS, or DOM snippet
- An existing copy block, email, deck, or design to be reviewed
- Phrases: "audit this", "review this", "score this", "what's wrong with...", "evaluate"

**Mode 2 — Derivation**, when the input IS a problem:
- A goal or outcome to design for ("design an onboarding for X")
- A design question ("modal vs inline expansion?")
- A diagnosis request ("we're losing users at checkout — why?")
- Phrases: "should we", "how do we", "what would be the right...", "design a", "solve this"

**Mode 3 — Analysis**, when the input IS a hypothetical, mechanism, or observation:
- A hypothetical change ("what happens if we remove X")
- A mechanism question ("why does this work", "how does this trick work")
- A behavioral observation to explain ("users say X but do Y")
- A counterfactual or thought experiment about an existing system
- Phrases: "what happens if", "why is X working", "what would change", "imagine we replace", "what's the effect of"

**Ambiguous? Ask once:**
> "Three options: evaluate something existing (URL/screenshot), solve a design problem (goal/question), or analyze a mechanism or hypothetical (what-happens-if / why). Which?"

**Edge cases:**
- URL plus hypothetical ("here's the page, what happens if we remove the nav?") routes to Analysis. The hypothetical is the work; the URL is just context.
- Problem plus hypothetical phrasing ("we're considering removing X, what would happen?") routes to Analysis. Hypothetical phrasing dominates.
- URL with no question routes to Evaluation by default.
- The question shape overrides artifact-based routing when a question is in the prompt.

**Forced via command:**
- `/perception-first-design:solve` — always Mode 2 (derive a solution)
- `/perception-first-design:evaluate` — always Mode 1 (audit an artifact)
- `/perception-first-design:analyze` — always Mode 3 (descriptive cascade)
- `/perception-first-design:all` — composite, run all three modes on the same input

---

## The 5-Layer Dependency Stack

Fix bottom-up. Upstream failures block everything downstream.

### Cognitive Load (L0)
> "Can't perceive anything without the bandwidth to do so."

- Working memory: ~3-5 chunks (Cowan, 2001, 2010 — not Miller's "7±2")
- **WM is spent on unconscious processing too** (Hassin et al., 2009): visual noise consumes bandwidth even when unattended
- Extraneous load (poor design) must be eliminated to free bandwidth for intrinsic load (the task)
- When processing exceeds capacity → brain defaults to leaving
- **Constraint type:** Capacity ceiling on simultaneous processing

**In practice:** Reduce choices. Progressive disclosure. Smart defaults. Delete unnecessary fields. Clean background noise that users never consciously notice (inconsistent spacing, off-system colors). Their WM pays the bill regardless.
**Failure signals:** Form abandonment, high bounce on option-heavy pages, "where do I click?"

### Layer 1: First-Impression Architecture
> "Your site has 50 milliseconds."

- Visual appeal judgments form in 50ms (Lindgaard et al., 2006)
- Aesthetic-usability effect: beautiful = perceived as more functional (Kurosu & Kashimura, 1995)
- **5-stage subroutine** (Leder et al., 2004): perception → implicit integration → explicit classification → cognitive mastery → evaluation. Each stage can fail independently.
- **Pre-verbal arousal has two polarities at L1** (Mori, 1970; Pessiglione et al., 2007): uncanny-valley response kills L1 before analysis; subliminal reward cues pass L1 before awareness.
- The first impression IS the activation point — switches attention from OFF to ON
- **Constraint type:** Temporal gate — if it fails, nothing downstream gets evaluated

**In practice:** Hero/opening = thesis statement. Visual quality must match price point. Audit for uncanny-valley triggers (off AI photos, uncanny animation timing, asymmetric faces).
**Failure signals:** High bounce + low time-on-page. "Looks sketchy." Competitors with worse products winning.

### Layer 2: Processing Fluency
> "If it's easy to process, it feels true."

- Easy-to-read fonts judged as more TRUE (Reber & Schwarz, 1999)
- Effect generalizes: truth, confidence, liking, trust (Alter & Oppenheimer, 2009)
- **Subjective felt fluency, not objective measurable fluency** (Forster, Leder & Ansorge, 2013): Lighthouse score and lived fluency are correlated but not identical. L2 lives in the gap.
- Cross-modal sensory coherence: all elements tell the same story (Spence, 2011)
- Consistency > creativity. Inconsistency compounds as trust erosion.
- **Constraint type:** Signal quality — inconsistency degrades truth/trust signal

**In practice:** 2 fonts max. 3-4 colors. Consistent spacing. Consistent voice and tone. Design for felt fluency, not metric-passing.
**Failure signals:** Inconsistent branding across touchpoints. Visual/verbal quality ≠ price point.

### Layer 3: Perception Bias Optimization
> "It's not for you. It's for them."

- Users autopilot decisions, rationalize after (Nisbett & Wilson, 1977; Kahneman, 2011)
- Surveys = System 2 rationalization. Analytics = System 1 behavior. The gap = where problems hide.
- Predictive processing: brain generates predictions; match = autopilot; violation = attention fires (Clark, 2013)
- **Trust is a perceptual output, not an argument output** (Seckler et al., 2015): visual coherence drives trust directly; weak visuals mean users filter every argument through a low-quality prior
- **Constraint type:** Information asymmetry — what users say ≠ what they respond to

**In practice:** Design for what analytics shows, not what surveys say. Test emotional response, not stated preference. Fix visual coherence before rewriting copy when trust data is poor.
**Failure signals:** "Users say they want X but do Y." Internal team preferences ≠ user behavior.

### Layer 4: Decision Architecture
> "Build the trail."

- Structure the environment so the right choice is the easiest choice
- Ethical persuasion: Alignment (user goals = business goals), Sincerity (what you show = what you deliver), Golden Rule (would you be comfortable experiencing this?)
- **Demonstrate, don't describe** (Hertwig & Erev, 2009): decisions from description underweight rare events. Interactive previews, trials, and samples move the decision from description to experience.
- **Match linguistic register to commitment distance** (Trope & Liberman, 2010): near-term actions get concrete language ("buy now"); abstract commitments get high-construal language ("partnership"). Mismatches feel transactional or bloated.
- PFD removes perception barriers to genuine value — does NOT create perception of value where none exists
- **Constraint type:** Behavioral structure — the environment shapes the decision

**"Fewer options" is context-dependent.** Reducing choices reduces paralysis *at decision points* — purchase pages, one-time commitments, unfamiliar options. It does NOT apply in expert tool palettes, browse/reference interfaces, or workspace contexts where option reduction harms productivity. The principle is: simplify decision points, not the entire environment.

**In practice:** CTAs as natural resolution of the experience. Progressive trust-building. No dark patterns. Match option density to context: sparse at conversion points, rich in expert workspaces. For risk/price/uncertainty: demonstrate via interaction, not description.
**Failure signals:** Users complete tasks but feel manipulated. High conversion but low retention. Experts frustrated by hidden/reduced tooling.

---

## The Derivation Protocol

**Rule Zero:** Do NOT propose any solution until all 5 layers are analyzed and requirements accumulated.

### Step 1 — State the Design Problem
What is the user trying to do? What prevents them? What do they experience?
Do NOT describe the problem as missing features or comparisons to other tools.

### Step 2 — Work Each Layer Bottom-Up
For each layer (L0 → L1 → L2 → L3 → L4):
  a. State the constraint (biological/psychological hard limit)
  b. State the violation (how current design fails this constraint)
  c. Derive the REQUIREMENT (what design MUST do — not "should")
  d. Label it R[n]
  e. Include a `**Citations:**` line listing 1-2 strongest supporting works from the framework's research base. Format: `Author (Year) for [reason]` with semicolons between multiple.

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

### Output Closing
End the output with a single italic line:

> *Initial findings. Ralph Loop a requirement, cite further, switch to analyze / evaluate, or ask any follow-up to dig deeper.*

Non-negotiable. Single italic line, no bullet menu.

---

## The Analysis Protocol

**Rule Zero:** Walk the 5 layers as descriptive lenses, not as constraints. Produce results, not recommendations. Do not slip into solve mode.

### Step 1 — Restate the question
State the change, mechanism, or counterfactual being analyzed. Ground it in concrete terms. Avoid restating it as a problem to solve.

### Step 2 — Walk each layer bottom-up as a descriptive lens
For each layer (Cognitive Load → First Impression → Processing Fluency → Perception Bias → Decision Architecture):
  a. State the layer's psychological reality (the constraint)
  b. Trace what the change does to perception or cognition at this layer
  c. Stress-test the consequence against four dimensions (each consequence must surface findings from at least two of these, ideally all four):
    - **User-population variation** (novice, power, accessibility, device, demographics)
    - **Adjacent infrastructure** (extensions, APIs, automation, dependent products, integrations, regulated surfaces)
    - **Precedents** (has a similar change been attempted elsewhere? what was the outcome?)
    - **Time structure** (immediate / short / long: seconds-minutes, days-weeks, months-years)
  d. Output: mechanism prose plus a "What happens:" prediction line that incorporates the stress-test findings.

Produce one consequence per layer. Five layer-cascade consequences are non-negotiable.

### Step 3 — Check for trade-offs
Does the change push the layer in only one direction, or in both? When a layer pushes both directions, fold the trade-off into the consequence as a sub-finding (not as a separate consequence).

Example: phishing risk in a "remove URL bar" analysis is bidirectional. Volume drops; per-incident severity rises. Net depends on which dominates. Do not assert one-way effects when trade-offs exist.

### Step 4 — Check for integrative compounds
What happens when consequences compound across layers? Three patterns to check by default:
  - **Social aggregation** (individual experiences aggregating into collective signals: backlash, viral discussion, regulatory action). Always check when consumer-facing. Surface in temporal waves if the cascade is multi-stage.
  - **Lock-in asymmetry** (substitute behaviors locking in faster than re-introduction reverses them). Always check when behavior change is involved. Recovery is rarely symmetric with disruption.
  - **Ecosystem cascade** (downstream products, derivatives, integrations inheriting the change). Always check when the artifact is platform-level.

Other compounds may emerge through the cascade. Look for them. Tag with `[Cross-layer + Social Aggregation]`, `[Cross-layer]`, or other appropriate cross-cutting label. Letter-label them (A, B, C) to distinguish from the numbered layer cascade.

### Step 5 — Format output
- **Title:** the question
- **Subtitle:** "X layer-cascade consequences, Y integrative compounds." Concrete counts.

Each consequence (numbered or lettered) has four structural elements:
1. **Heading** with abstract analytical title and bracketed layer tag (`## N. [Title] [Layer]` or `## N. [Title] [Layer A × Layer B]`)
2. **Italic concrete subtitle** directly under the heading. Plain-language summary of what the consequence is, no framework jargon. Readers without PFD context understand the consequence from this line alone.
3. **Body** with mechanism prose plus "What happens:" prediction.
4. **Citations** line at end of body. `**Citations:** Author (Year) for [reason]; Author (Year) for [reason].` 1-3 strongest supporting works from the framework's research base. When applied prediction without direct citation: "Applied prediction; no direct framework citation. Closest adjacent: [related citation]."

Subtitle and Citations are both non-negotiable.

- **Layer cascade:** 5 numbered consequences in cascade order, four-element structure above.
- **Integrative compounds:** separate section, letter-labeled (A, B, C, ...), `[Cross-layer ...]` heading tag, same four-element structure.
- **Closing cue:** End the output with a single italic line:
  > *Initial findings. Ralph Loop a consequence, cite further, switch to solve / evaluate, or ask any follow-up to dig deeper.*

  Single line, italic, on its own. Non-negotiable. No menu expansion.

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
| Slipping into solve mode during analysis | Produces recommendations when the question wanted results; descriptive contract violated |
| One-way effects when trade-offs exist | Misses bidirectional layer behavior; phishing-as-uniform-rise example |
| Treating layers as siloed in analysis | Misses integrative compounds (backlash, lock-in asymmetry, ecosystem cascade) |
| Shallow per-consequence depth in analysis | Single sentences read correct but bland; the depth bar is multi-paragraph stress-tested findings |
| Heading without italic concrete subtitle | Abstract titles are not scannable; readers without framework context need the plain-language line to follow the analysis |
| Missing Citations line per consequence or requirement | Output reads as opinion when it should anchor to evidence; framework's research base is its credibility |
| Closing cue expanded into a bullet menu | Loads WM at the most depleted moment of the output; invites survey-driven format creep; closing cue is one italic line, never a list |

---

## After Applying PFD

### Insight Log (MANDATORY — every analysis)

Append an entry to `references/insights-log.md` after every PFD derivation or evaluation:

```markdown
### YYYY-MM-DD — [Brief description of what was analyzed]
**Type:** url | text | image | html | css | copy | directory
**Domain:** [e.g., SaaS landing, ecommerce PDP, email, portfolio, dashboard]
**Key finding:** [The non-obvious thing PFD surfaced — one sentence]
**Layer(s):** [L0/L1/L2/L3/L4]
**Promote?:** yes | maybe | no
**Notes:** [Cross-references, patterns, connections to prior findings]
```

Do this even for routine analyses. The insight is sometimes in what PFD struggled with,
what layer was ambiguous, or what the protocol couldn't handle cleanly.

### Accumulated Learnings — sharded corpus (v0.5+)

Learnings are stored as atom files under `references/learnings/`, organized by primary layer. Lightweight index + on-demand atom reads, never eager monolith load.

**Query sequence:**
1. Read `references/learnings/_index.md` — lightweight, one line per learning (scales to 1000+)
2. Scan the index for atoms relevant to the current task; note their paths
3. Drill into specific atoms via `Read` — only the ones you need
4. For programmatic filtering (e.g., "all L2 learnings tagged fluency"), read `references/learnings/_search.json` instead of the markdown index

**Cheapest first:** index scan → targeted atom read → legacy monolith fallback.

**Do NOT eager-load `accumulated-learnings.md`** — that monolith is the pre-migration fallback for L1–L19 only. Read it when the index points at pre-migration content, or as a last-resort fallback for broad context. After Phase 2 bulk migration, it retires entirely.

**Adding a new learning (when `Promote?: yes` in insights-log):**
1. Create atom file: `references/learnings/{layer}/l<NNN>-<slug>.md` with YAML frontmatter (required: `id`, `title`, `layer`, `date`, `contributor`, `source`; optional: `secondary_layers`, `updated`, `related`, `tags`)
2. Regenerate: `python scripts/gen-pfd-index.py` (run from repo root)
3. Commit atom + regenerated `_index.md` + `_search.json` together
4. If the learning changes scoring behavior, bump patch version in `.claude-plugin/plugin.json`

---

## Reference Files

Load these when relevant:

- **`references/learnings/`** — Sharded accumulated learnings (29 atoms across L0/L1/L2/L3/L4/cross/meta). Query via `_index.md` (human) or `_search.json` (machine). Lazy-loaded.
- **`references/accumulated-learnings.md`** — Pre-shard monolith retained for backward compatibility. Do not eager-load; use the sharded loader above.
- **`references/citation-standards.md`** — Required when presenting PFD publicly or to clients. Distinguishes hard science from practitioner synthesis.
- **`references/mvs-psychology-reference.md`** — Per-layer psychology corpus with primary research citations. Every PFD violation traces to a citation here.
- **`references/pfd-spatial-extension.md`** — Load when applying PFD to canvas tools, spatial interfaces, or layout systems (Figma, Miro, Notion, Cognograph).
- **`references/practitioner-corrections.md`** — Practitioner correction layer. Empty by default; populate with audit corrections to lift evaluation accuracy from LLM-baseline to practitioner-grade.

Full framework: `framework/PERCEPTION-FIRST-DESIGN.md` (~870 lines, ~100 citations).

---

## Corpus-Backed Evaluation (v1)

When performing a PFD evaluation (Mode 1: Checklist or Mode 2: Derivation), load the corpus for deeper analysis:

1. Read `corpus/core/tier2-prompt-template.md` for the evaluation protocol
2. Follow the loading sequence in the template (rubric -> constraints -> corrections -> design system profile -> heuristic rules -> worked examples)
3. Apply the evaluation instructions from the template
4. After evaluation, log findings per the Insight Log protocol below

The corpus provides:
- **Heuristic rules** (`corpus/heuristics/`) — specific detection criteria with psychology citations
- **Design system profiles** (`corpus/design-systems/`) — framework-specific detection and fix prescriptions
- **Worked examples** (`corpus/worked-examples/`) — calibration anchors showing what each score range looks like

(Practitioner corrections are tracked in `references/practitioner-corrections.md` — single source of truth.)

**When to use corpus vs. quick evaluation:**
- Quick PFD scan (no URL, just looking at a design): Use the skill's 5-layer stack directly (no corpus needed)
- Full PFD audit (URL provided, detailed analysis requested): Load the corpus per the template
- PFD derivation (generating a design): Load `references/practitioner-corrections.md` + design system profile for constraint-setting

---

## Version History

- **v0.7.0** (2026-04-28): Mode 3 (Analysis) added. New commands `/perception-first-design:analyze` (descriptive cascade for hypotheticals, mechanism questions, behavioral observations) and `/perception-first-design:all` (composite three-mode runner). Analysis Protocol formalized: 5 layer-cascade consequences with per-consequence stress-testing across four dimensions (user-population variation, adjacent infrastructure, precedents, time structure), plus integrative compounds (social aggregation, lock-in asymmetry, ecosystem cascade) and folded trade-offs. Mode detection extended: bare-skill activation now routes "what happens if X", "why is X working", and similar phrasing to Mode 3. SKILL.md "Two Modes" section renamed "Three Modes." Four anti-patterns added covering analyze-specific failure modes (slipping into solve mode, one-way effects when trade-offs exist, treating layers as siloed in analysis, shallow per-consequence depth). Spec calibrated against the URL-bar/Chrome thought experiment that produced an expert "wow" reaction in the v2.1 era; v0.6.0 solve compressed that question to a verdict, v0.7.0 analyze produces the descriptive cascade the question actually warranted.
- **v0.6.0** (2026-04-27): Marketplace-listing readiness. Plugin manifest at `.claude-plugin/plugin.json` (repo root) with spec-canonical component layout (`skills/`, `commands/`, `scripts/` at root — no nested `skill/` subdirectory). Marketplace catalog at `.claude-plugin/marketplace.json` enables self-hosted distribution alongside official Anthropic submission. Commands renamed: `pfd` → `solve` (Mode 2 derivation), `pfd-audit` → `evaluate` (Mode 1 corpus-backed audit) under `/perception-first-design:` namespace. Mode detection rules added — bare skill activation auto-routes between solve and evaluate based on input shape. 9 new atoms added (l021-l029) from the calibration campaign; `_index.md` regenerated to 29 atoms. `mvs-psychology-reference.md` added to skill references for skill-side quick lookup. License simplified to single CC BY-SA 4.0 with practice exemption (was dual MIT + CC BY-SA). NOTICE file at repo root with trademark terms + permitted/prohibited use examples. `.gitignore` for OS noise + private working files. Path conventions clarified. Corrections live in `references/practitioner-corrections.md` (single source of truth).
- **v0.5.0** (2026-04-21): Sharded learnings architecture. Migrated 20 accumulated learnings from monolithic `accumulated-learnings.md` to atom files under `references/learnings/` organized by primary layer (L0/L1/L2/L3/L4/meta/cross). Generated `_index.md` (human-readable) + `_search.json` (machine-readable) from atom YAML frontmatter via `scripts/gen-pfd-index.py`. SKILL.md loader updated for lazy-load — index-first scan, atoms read on demand. Scales to 1000+ learnings without per-activation cost blowup. Monolithic file retained as pointer for external-link compatibility. Framework v3.6 unchanged.
- **v0.4.0** (2026-04-20): Framework v3.6: international citation expansion. 17 new citations across 6 research traditions (DE/AT/CH, JP, CN, FR, NL/IL/Scandinavia). New Methodology Siblings section (Kansei/Nagamachi, Gestalt/Wertheimer+Metzger, neuroaesthetics/Skov+Nadal+Leder). Cultural Calibration meta-rule: architecture universal, calibration cultural; validate L1 and L3 against target-market users before cross-regional rollout. Seven new layer rules threaded into L0–L4 as active framework rules, not footnotes. Pre-verbal arousal empirical backbone strengthened (Hassin 2013, Pessiglione 2007, Mori 1970). Learning #20 added: International citation expansion. Master doc: 817 → 872 lines.
- **v0.3.9** (2026-04-16): Learning #19 added (Multi-Artifact Engagement Field and Relay-User Mode). Two convergent PFD Ralph Loops on a European enterprise prospect engagement surfaced the same structural gap — PFD's 5-layer stack assumes one artifact + buyer-in-front; B2B engagements are fields of artifacts evaluated by relay users. Candidate for L5 formalization in v0.4 after 2-3 more engagement validations. Related candidate observation (calendrical/timing layer) registered in insights log, not yet promoted.
- **v0.3.8** (2026-04-02): Unified objective statement added to "What PFD Is": pre-verbal arousal as the explicit goal of the 5-layer stack.
- **v0.3.7** (2026-03-16): Canonicalized layer numbering: Foundation (L0) → L1 → L2 → L3 → L4. Fixed off-by-one error (was L2-L5). No framework content changed — numbering alignment only.
- **v0.3.6** (2026-02-26): Learning #16 (near-miss color asymmetry). Framework v3.3: added Bujack et al. 2022 + Brainard 2022 (55 citations). L2 color qualifier (perceptual vs physical space, OKLCH). Design-token linting near-miss severity weighting. Skeptical analysis of "Schrödinger completed" headlines — cite non-additivity finding, not "completed" framing.
- **v0.3.4** (2026-02-25): Synced with framework v3.2 scholarly audit. 53 citations (5 new). Fixed Tractinsky 2006 mischaracterization, Miller 1956 body text, Zak 2015 hedge. WM 3-4→3-5 per Cowan 2010. Citation-standards.md updated with full audit log.
- **v0.3.0** (2026-02-24): Restructured plugin with proper directory layout. Skill description expanded to cover design, marketing, copywriting, writing, and communication. Learnings, citations, and PFD-S moved to references/ for progressive disclosure. `/pfd` command added.
- **v0.2.0** (2026-02-19): 9-expert PFD brainstorm synthesis. Added learnings #9-12: temporal/session continuity, constraints as distributions, visual channel audit, route vs survey knowledge.
- **v0.1.1** (2026-02-19): Added learnings #6-8 from product-level derivation.
- **v0.1** (2026-02-19): Initial proto. Derivation protocol, 5 layers, PFD-S, 5 accumulated learnings.
