---
id: l024
title: "AA-Constrained Token Ladder"
layer: L2
secondary_layers: [meta]
date: 2026-04-24
contributor: Stefan Kovalik
related: [l011, l013, l016]
tags:
  - aa-constrained-token-ladder
  - wcag-aa
  - design-system-tokens
  - contrast-discipline
  - by-construction
  - brand-color-variants
source: >
  PFD Calibration & Showcase Campaign — n=25 Fortune-500 calibration testing
  (2026-04 sweep). Distribution-level finding from `qa/CONTRAST-FIXES.md` —
  axe-core contrast audit (WCAG 2.1 AA) across 26 full-rebuild pages, 576
  violations → 0 via three-axis fix sweep. Mid-grey token fix recurred in
  12+ of 25 episodes; tiny-font fix in ~8; brand-color-on-tint fix in ~5
  (eps 06 Adobe, 07 Amazon Prime, 11 Reddit explicit).
---

# Learning 24: AA-Constrained Token Ladder — Design Systems Should Pass WCAG AA by Construction, Not by Audit

**Insight:** Calibration testing across the n=25 PFD Calibration & Showcase Campaign produced the strongest distribution-level mechanism finding of the sweep: 576 WCAG 2.1 AA contrast violations across 26 full-rebuild pages collapsed to 0 via a three-axis token-ladder fix pattern that recurred uniformly enough to surface a system-construction discipline PFD has not previously named. The dominant axis was a single token family — `--ink-4` / `--fg-quiet` / equivalent mid-grey tokens in the `#6b7380` neighborhood — sitting at the WCAG cliff edge across 12+ of 25 episodes. On light backgrounds these tokens fail AA's 4.5:1 normal-text threshold ~70% of the time; the canonical fix was `#6b7380 → #4e5668` for day mode and `#484f58 → #7a8494` for dark-default pages. The second axis was tiny font tokens (9–11px) recurring in ~8 episodes, requiring a 12px floor combined with explicit color overrides instead of opacity inheritance. The third axis was brand colors on tinted backgrounds (~5 episodes — Adobe red `#FA0F00 → #D40000`, Amazon Prime blue `#00A8E1 → #0077a3`, Reddit orange `#FF4500 → #c73500`), requiring AA-compliant variants of the brand color that preserve color-family identity at 10–30% lightness adjustment. Across all three axes, the fix repeated mechanically enough to indicate the failure is systemic rather than per-designer or per-page — a plausible inference, not yet formally verified, is that vendor-built design systems emit "subtle" or "tertiary" tokens without a documented (token × declared-background) AA contract at construction time, leaving the contrast outcome to per-page audit rather than to construction-time guarantee. This sharpens Learning #11 (Visual Channel Audit) by giving channel-violation findings a systemic root cause — channel violations don't come from designer error, they come from token defaults chosen for aesthetic subtlety rather than mathematical contrast constraint. Distinct from Learning #16 (Near-Miss Color Asymmetry), which names the cost asymmetry of color *choice*; #24 names the construction discipline of color *tokens*. The promoted spec is two-tier — **AA = hard floor** (no shipped token may produce text below 4.5:1 normal / 3:1 large on its declared backgrounds; brand colors that violate this ship as AA-compliant variants, not as-shipped brand colors), and **AAA = aspirational ceiling** for accessibility-critical surfaces (medical, financial, government, educational — 7:1 normal / 4.5:1 large). Brand-allowance is handled by variant — the design system ships `--brand-primary` as the AA-compliant version, with the original as `--brand-primary-display` reserved for surfaces with no text. The token ladder must compose multiplicatively — every (token × declared-background) pair has a documented contrast figure ≥ AA, computed at construction time rather than discovered at audit time. Practical implementation: ship the design system with a contrast-test artifact that runs axe-core or equivalent against every (token, background) pair on every commit; the artifact is cheap to build (a single HTML page enumerating combinations) and turns the AA-by-construction claim from a wish into a CI gate. Generalizes beyond PFD audit work into design-system construction itself — any agency, in-house team, or vendor shipping a token system should adopt the AA-constrained ladder as the construction discipline, with AAA reserved for context-sensitive surfaces. The campaign's evidence is the strongest empirical case in the corpus for this discipline — 26 pages spanning ecommerce, SaaS, fintech, media, marketplaces, and B2B with the majority of vendor-built design systems in the calibration sample (12 of 25 episodes had the mid-grey token violation explicitly; the broader three-axis pattern affected the majority of the sample) requiring the same three-axis fix, indicating that mainstream design systems frequently ship without an AA-by-construction contract on their token ladders, and that AA-by-construction is the cheapest correction available because it pre-empts every audit cycle the per-designer/per-page workflow would otherwise burn.
