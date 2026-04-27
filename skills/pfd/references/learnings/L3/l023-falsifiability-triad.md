---
id: l023
title: "Falsifiability Triad"
layer: L3
secondary_layers: [L2, L4]
date: 2026-04-24
contributor: Stefan Kovalik
related: [l015, l016, l021, l022]
tags:
  - falsifiability-triad
  - honest-claim
  - l3-positive-shape
  - perception-bias-replacement
  - sincerity-test
  - verifiable-copy
source: >
  PFD Calibration & Showcase Campaign — n=25 Fortune-500 calibration testing
  (2026-04 sweep) using `templates/scoring-rubric.md` v1.0. Originates from
  Expedia ep 05 dark-pattern-map (verbatim "Candidate learning for promotion
  to `references/learnings/l3/`" — placement honored on 2026-04-25 re-shard);
  verified across 7+ episodes spanning cancel flows (eps 06 Adobe, 24 Disney+,
  25 Netflix), OTA (eps 05 Expedia, 22 Booking), B2B pricing (ep 23 Salesforce),
  and ticketing (ep 02 Ticketmaster, ep 17 StubHub).
---

# Learning 23: Falsifiability Triad — The Three-Property Test for Honest L3 Claims

**Insight:** Calibration testing across the n=25 PFD Calibration & Showcase Campaign surfaced a recurring fix pattern at the L3 layer that the originating audit document (Expedia ep 05's `dark-pattern-map.md`) explicitly proposed for promotion to `references/learnings/l3/`: across the campaign's PFD-aligned alternatives to perception-bias claims — covering scarcity, urgency, social proof, anchoring, retention copy, and post-state framing — every alternative satisfied a three-property test. Falsifiability (the user can catch the system lying), specificity (a verifiable referent), and user-controllability (the system commits to a verifiable mechanism) together form a recurring positive shape for honest L3 claims across the campaign cluster, distinct from Learning #15's negative shape ("don't contradict yourself"). The triad is not asserted as the only possible honest shape — alternative honest forms may exist outside the campaign's tested surfaces — but it is the recurring shape across every PFD-aligned alternative the campaign produced. The campaign evidence is dense: Booking ep 22's fix replaced "Only 1 left!" with "3 rooms in this rate class · allocation refreshed 2:14 PM" — falsifiable (the user can refresh and check), specific (named rate class, timestamped), user-controllable (commits to a refresh interval the user can verify). Disney+ ep 24's fix replaced "you will lose Marvel, Star Wars..." (loss-framed retention copy) with "Access ends Tue May 6, 2026. No further charges." — falsifiable (the user can attempt access on May 7), specific (date-literal, dollar-literal), user-controllable (commits to a calendar boundary). Salesforce ep 23's pricing fix added "most teams of 10–500 reps land here" beside the mid-tier — falsifiable (verifiable via lead-qualification data), specific (named role + range), user-controllable in the weak sense (the buyer can self-categorize against the range). Netflix ep 25's "paused for 10 months with full data preservation" replaces the "closed" framing — specific (named retention period), user-controllable (the user can return within the window and verify). Where the triad is fully satisfied (Disney+, Booking), the L3 claim flips from perception-bias to honest-claim cleanly. Where 2 of 3 are satisfied (Netflix, Salesforce), the claim is partial — defensible but not fully audit-proof. Where 0–1 are satisfied, the claim is a perception-bias artifact regardless of how reasonable it sounds. The graded application is the practical use: 3-of-3 = honest claim; 2-of-3 = partial honest claim; 0–1 = perception-bias claim. The positional value of this learning in the framework is that it gives PFD its first explicit *positive-shape* design rule for L3 — until now, the framework has named L3 violations (#15 self-contradiction, #16 near-miss color) but not the positive standard a compliant L3 claim should hit. The triad fills that gap. Expected to apply to other urgency/scarcity/social-proof surfaces beyond the campaign's tested set (e-commerce, SaaS, OTA, ticketing, lead-form pricing, retention copy, post-state framing — anywhere the design must communicate a fact about the world where the user has no direct access to the underlying mechanism), with the scope caveat from above intact: the triad is the campaign's recurring shape, not asserted as the only possible honest shape, and the extension to surfaces outside the calibration sample is predicted by mechanism rather than verified by measurement. Practical heuristic: "if it can't be falsified, it can't be honest." Cross-refs the L4 Symmetry Threshold (#22) as a sibling: where #22 is a numeric L4 primitive, the Falsifiability Triad is a verbal L3 primitive — both turn ethical claims into auditable specs.
