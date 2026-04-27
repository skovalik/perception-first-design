---
id: l022
title: "L4 Symmetry Threshold"
layer: L4
secondary_layers: [meta]
date: 2026-04-24
contributor: Stefan Kovalik
related: [l021, l014, l016]
tags:
  - l4-symmetry-threshold
  - cancel-clicks-ratio
  - path-symmetry
  - numeric-hard-fail
  - regulator-validated
  - cancel-flow
source: >
  PFD Calibration & Showcase Campaign — n=25 Fortune-500 calibration testing
  (2026-04 sweep) using `templates/scoring-rubric.md` v1.0. This learning
  derives from the 5-cancel-flow sub-cluster (eps 06 Adobe, 07 Amazon Prime,
  13 LinkedIn Premium, 24 Disney+, 25 Netflix) per
  `essays/02-five-cancel-flows/comparison-table.md`. Regulator citations —
  FTC v. Vonage Holdings Corp. (2022, $100M consent order); FTC v. Amazon
  (2025, $2.5B consent order); EU DSA Art. 25(1)(c).
---

# Learning 22: L4 Symmetry Threshold — Cancel-Clicks Ratio as Numeric Hard-Fail Trigger

**Insight:** Calibration testing across the n=25 PFD Calibration & Showcase Campaign — specifically the 5-cancel-flow sub-cluster — surfaced the first numeric, regulator-validated L4 hard-fail trigger PFD has named: the cancel-clicks-to-signup-clicks ratio. Per the campaign-canonical comparison table, ratios across the cluster were Adobe ~5×, Amazon 6×, LinkedIn 8×, Disney+ 5–8×, and Netflix ~2× — and every regulator-actioned target in the cluster sits above the 2× line. Two FTC consent orders independently codified the floor: FTC v. Vonage Holdings Corp. (2022, $100M) and FTC v. Amazon (2025, $2.5B) both require cancellation paths that are "at least as simple as" the corresponding signup paths, which is the regulator-verbatim form of ratio ≤ 1×. EU DSA Art. 25(1)(c) carries the same standard, prohibiting "procedures for terminating a service that are more difficult than subscribing." That convergence — two regulators across two jurisdictions, one numeric standard, n=25 calibration validation at the cluster — gives PFD its first L4 instrument with a hard threshold instead of a heuristic verdict. The promoted spec is two-tier: **≤ 1× = regulator-safe** (the hard floor; failure crosses the enforcement-risk line per FTC consent-order standard), **1×–2× = PFD-flagged warning zone** (legally defensible but architecturally suspect; Netflix sits at ~2× and is the cluster's only ethics-passer but not its ideal), and **> 2× = hard fail** (architecturally extractive; the band where 4 of 5 cluster members sit and where 100% of cluster members with regulator action live). The threshold is necessary-but-not-sufficient for enforcement: every regulator-actioned cluster member has ratio > 2×, but Disney+ at 5–8× is currently un-actioned (BBB 1,200+ complaints + Trustpilot 1.3/5 signal hot, no FTC or EU action as of 2026-04-22). The implication for practitioners is sharp: ratio > 2× is a *necessary* condition for being in the regulator-action set across this cluster, but the cluster also shows that being at high ratio without action exists — so the threshold is a hard floor for *architecture*, not a guaranteed predictor of *enforcement*. As design spec, the threshold is binding (you should not ship > 2× regardless of whether your category has been actioned yet); as legal-risk diagnostic, it is a risk indicator that compounds with public-complaint signal (BBB volume, Trustpilot rating, app-store review velocity) but does not by itself guarantee enforcement timing. The threshold is auditable from public surface alone — count clicks on the signup path, count clicks on the documented cancel path (vendor help docs are sufficient if the live cancel surface is bot-blocked), divide. No internal data access required, no surveys, no A/B tests. This operationalizes Learning #21 (L4-Ethics Fusion) by giving the fusion a measurable instrument: where #21 names the *claim* that ethics and decision architecture resolve to the same diagnostic, #22 is the *number* that resolves it. Expected to generalize to other decision-reversal surfaces (downgrade, opt-out, refund, account closure, unsubscribe) and to multi-step transactions where path-symmetry is contested (refund vs purchase, unenroll vs enroll, leave-team vs join-team) on mechanism continuity (the FTC "at least as simple as" standard is surface-agnostic) — validation pending. The campaign's calibration sample tested cancel flows specifically; the threshold's authority on those surfaces is empirical, while its authority on other decision-reversal surfaces is currently predicted by mechanism rather than measured.
