---
id: l011
title: "Visual Channel Utilization Audit"
layer: L1
secondary_layers: [L2]
date: 2026-02-19
updated: 2026-04-25
contributor: Stefan Kovalik
tags:
  - visual-channels
  - bertin
  - pre-attentive
  - audit
  - diagnostic-tool
  - density-instrumentation
source: Cartographic + data visualization persona lenses in 9-persona brainstorm; 2026-04-25 update from PFD Calibration & Showcase Campaign instrumentation patterns.
---

# Learning 11: Visual Channel Utilization Audit

**Insight:** Bertin's 7 visual variables (position, size, value/lightness, texture, color, orientation, shape) provide a systematic audit checklist. Most UIs use 2-3. The derivation protocol should include a channel audit after R1-R5: "How many visual channels does this design use? Which channels are available but unused?" Under-utilization of channels means information that COULD be signaled pre-attentively is instead hidden behind interaction. This is a direct R2 diagnostic tool.

**2026-04-25 update — Repetition / Density Instrumentation Extension (PFD Calibration & Showcase Campaign):** Running channel audits across the n=25 sweep surfaced a counting-based instrumentation extension that operationalizes channel-violation findings into legally-defensible numeric metrics rather than heuristic verdicts. Specifically: counting becomes the cleanest measurement methodology PFD has — "Remind Me Later" × 4 in Amazon Prime cancel flow (ep 07, mere-exposure asymmetry per Zajonc 1968), four named dark patterns in one DoorDash checkout (ep 12, pattern-density at chokepoints), 14 IKEA brand-vocabulary elements scored present/absent on web (ep 10, channel-allocation gap), 8 widgets at equal weight on AWS Console Home (ep 08, iso-styling/equality-as-obstruction), 5+ reserved-meaning colors per Booking card (ep 22, color-saturation collapse), 18 of 25 missing responsive hamburgers (campaign-wide, master-template gap). Each is a channel-audit observation re-cast as a count, and the count is the diagnosis. The promoted instrumentation principle: density and repetition are L0/L3/L4 instruments, not just narrative color; a channel-audit finding stated as "X used N times where N > threshold" or "Y elements present Z absent across 14-element brand inventory" is more legally defensible than a heuristic verdict, more legible to non-designer stakeholders, and more reproducible across auditors. Practical extension to the audit protocol: after running the standard channel audit (R1-R5), produce a numeric instrumentation pass — for each channel-violation finding, can it be stated as a count? If yes, prefer the count framing. Connects to Learning #16 (near-miss color asymmetry — the per-card color-saturation collapse threshold ~3 reserved roles is a count-based instrumentation of the same underlying mechanism) and to Learning #22 (L4 Symmetry Threshold — cancel-clicks ratio is a count-instrumented L4 verdict). The campaign's evidence is 6+ episodes where counting was the load-bearing diagnostic; generalize on additional client work before treating density/repetition as the primary instrumentation mode rather than as supplement.
