# Changelog

## Plugin v0.6.0 (2026-04-27): Marketplace Listing Readiness

**Marketplace packaging**
- Plugin manifest moved from `skill/plugin.json` to `.claude-plugin/plugin.json` at repo root, per current Claude Code spec.
- Repo restructured to spec-canonical layout: `skills/`, `commands/`, `scripts/` at repo root. Eliminates the prior nested `skill/skills/` redundancy and obviates plugin.json path overrides.
- `.claude-plugin/marketplace.json` added at repo root — single-plugin entry with `source: "./"`. Enables self-hosted distribution: `/plugin marketplace add skovalik/perception-first-design && /plugin install perception-first-design@perception-first-design`.
- Plugin install via marketplace pulls the entire repo, so the `evaluate` command's `corpus/` and `framework/` references resolve correctly in the cached plugin directory.
- `NOTICE` file at repo root with consolidated trademark + dual-license terms. `LICENSE-CONTENT` (CC BY-SA 4.0) moved from `skill/` to repo root for visibility alongside `LICENSE` (MIT).

**Commands renamed** (breaking change for existing users)
- `pfd` → `solve` (Mode 2: derivation). Invocation: `/perception-first-design:solve "design problem here"`.
- `pfd-audit` → `evaluate` (Mode 1: corpus-backed audit). Invocation: `/perception-first-design:evaluate https://example.com`.
- Reasoning: cleaner namespacing under `/perception-first-design:`. Verbs describe what the command does.

**Mode detection (auto-routing)**
- SKILL.md now includes Mode Detection rules. Bare invocations (e.g., "PFD this design") inspect input shape and auto-route to Mode 1 (artifact → evaluate) or Mode 2 (problem → solve). Ambiguous cases prompt for disambiguation. Replaces the prior "always prefer Mode 2" rule.

**Content additions**
- 9 new atoms from the calibration campaign: l021 (L4 ethics fusion), l022 (L4 symmetry threshold), l023 (falsifiability triad), l024 (AA-constrained token ladder), l025 (cascade-credit), l026 (aesthetic stability as trust producer), l027 (internal acknowledgment signals), l028 (held-decision compounding), l029 (port-don't-install motion audit). Index regenerated to 29 atoms.
- 4 existing atoms updated with calibration-campaign tags: l010 (constraints are distributions), l011 (visual channel audit), l016 (near-miss color asymmetry), l017 (iterative regression is visibility).
- `mvs-psychology-reference.md` added to `skills/pfd/references/` for skill-side quick lookup (was corpus-only at `corpus/core/psychology/`).
- `gen-pfd-index.py` script committed under `scripts/` for atom index regeneration.

**Hygiene**
- `.gitignore` added: protects `CLAUDE.local.md`, `.claude/`, OS noise, Python caches, `*-private*` patterns.
- Path-conventions clarifier added to SKILL.md header (skill-relative vs plugin-root-relative paths).
- Fixed SKILL.md private path leak: `Aurochs/docs/PERCEPTION-FIRST-DESIGN-FRAMEWORK.md` → `framework/PERCEPTION-FIRST-DESIGN.md`.
- Fixed dangling `corpus/core/corrections/` reference in SKILL.md — corrections now live exclusively at `references/practitioner-corrections.md` (single source of truth).
- Author field updated: `Stefan Kovalik` (was `Stefan Kovalik / Aurochs`), with `email: admin@aurochs.agency` added for marketplace contact.

## Framework v3.6 + Skill v0.5.0 (2026-04-21)

### Framework v3.6 (2026-04-20): International Citation Expansion

**Added**
- Methodology Siblings section naming parallel traditions PFD inherits from and stands alongside:
  - Kansei Engineering (Nagamachi 1995): Japanese affective engineering methodology
  - Gestalt psychology (Wertheimer 1923; Metzger 1936): German perceptual organization tradition
  - Neuroaesthetics (Skov & Nadal 2020; Leder et al. 2004): European neural substrate of aesthetic response
- Cultural Calibration meta-rule promoted from footnote to working rule. Western-centric perception science assumptions get flagged when artifact audience is non-Western; calibration priors applied explicitly rather than silently.
- 7 new layer rules threaded across L0-L4:
  - L0: Hassin (2013) implicit working memory costs; Pessiglione (2007) subliminal reward processing
  - L1: Mori (1970) uncanny valley as L1 failure mode
  - L2: Forster (2013) conceptual fluency distinct from perceptual fluency
  - L3: Seckler (2015) trust as conjoint perceptual judgment; Hertwig (2009) description-experience gap
  - L4: Trope & Liberman (2010) construal-level theory for decision architecture
- Citation count: 82 to ~100

### Skill v0.5.0 (2026-04-21): Sharded Learnings Architecture

**Added**
- 20 learnings migrated from monolithic `accumulated-learnings.md` to atom files under `references/learnings/` organized by primary layer: `L0/`, `L1/`, `L2/`, `L3/`, `L4/`, `meta/`, `cross/`.
- `_index.md` and `_search.json` generated from YAML frontmatter across all atoms. Enables index-first scan without loading bodies.
- SKILL.md loader rewritten for lazy-load: scan index first, read individual atoms on demand. Scales to 1000+ learnings without per-activation cost blowup.
- Monolithic `accumulated-learnings.md` retained as a pointer/stub for backward compatibility with external links.

**License**
- Dual-licensed: **MIT** (code, scripts, loaders) + **CC BY-SA 4.0** (framework text, learnings, corpus content).
- Practice exemption explicit in `LICENSE-CONTENT`: applying PFD in practice (running analyses, generating recommendations, delivering client work) does not create a derivative work and is not subject to share-alike. Only redistributions or modifications of the framework text trigger ShareAlike.

## v3.5 (2026-04-02)

### Added
- Pre-verbal arousal formalized as the unified objective of the 5-layer stack
- "What the stack produces" block in The Framework section
- 5 new citations: Damasio (1994), LeDoux (1996), Lavie (1995), Servajean (2024), Joffily & Coricelli (2013)
- Prediction error cascade logic grounding the dependency stack order

### Changed
- Citation count: 77 → 82
- Version header updated to 3.5

## v3.4 (2026-03-04)

- 77 citations: 55 perception science + 22 ADHD cognitive neuroscience
- Predictive processing backbone (Clark 2013, Friston 2010)
- Ontic occlusion and open questions section
- ADHD curb-cut framing and dual-foundation bibliography
- Open-source release under CC BY-SA 4.0
- Evaluation corpus: 26 heuristic rules, 7 worked examples, 3 design system profiles
- Claude Code skill with `/pfd` and `/pfd-audit` commands

## v3.3 (2026-02-26)

- Bujack et al. (2022) non-Riemannian color perception citation
- Citation standards document with evidence tier system
- Processing fluency color infrastructure (Learning #16)
- Near-miss color deviation principle
- Brainard (2022) commentary integration

## v3.2 (2026-02-25)

- Audit corrections: Tractinsky 2006 recharacterized (replication, not critique)
- Miller 1956 body text corrected (rhetorical observation, not working memory limit)
- McGurk & MacDonald 1976: "override" corrected to "integrate with, producing fused percepts"
- Zak 2015 hedge strengthened (intranasal oxytocin field has ~90% false positive rate)
- Narrative persuasion evidence redirected to Green & Brock 2000, van Laer et al. 2014

## v3.0 (2026-02-01)

- 55 citations, fully verified
- 5-layer dependency stack formalized (Foundation, L1, L2, L3, L4)
- Derivation protocol (6-step generative process)
- Rule Zero: no solutions before all layers analyzed
- Accumulated learnings system
- PFD-S spatial extension (v0.1)
