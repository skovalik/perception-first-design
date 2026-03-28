# PFD Constitutional Constraints

These rules are MANDATORY. They override the LLM's judgment. They are enforced both in the prompt and in post-processing validation.

## Dependency Stack Caps (Hard Enforcement)

Lower layers are load-bearing. If they fail, upper layers cannot be fully trusted — they are built on a broken foundation. These caps are non-negotiable.

- If Foundation score < 40: L1 capped at 50, L2 capped at 45, L3 capped at 40, L4 capped at 35
- If L1 score < 40: L2 capped at 50, L3 capped at 45, L4 capped at 40
- Any layer with a Critical-severity violation: that layer capped at 30
- Score of 90+ requires: zero Critical violations, zero Major violations, AND specific evidence cited for each strength claim

When a cap is applied, note it in the Dependency Notes section. State the original uncapped score alongside the capped score so the practitioner can see how much the dependency constraint affected the evaluation.

## Anti-Leniency Rules

- Scores MUST use the full 0-100 range. A score of 20 is appropriate for sites with severe violations. A score of 50 is mediocre, not bad. A score of 75 is genuinely good.
- Do NOT cluster all scores in the 60-80 range. If Foundation is strong (>70) but L4 is weak (<40), that spread is expected and correct. PFD's dependency stack naturally produces score spread.
- If all 5 layer scores are within 15 points of each other, re-examine — uniform scores are a red flag for lazy evaluation. Different layers measure different things; uniform quality across all 5 is rare.
- Calibrate against the anchor examples loaded in Slot [7]. If you are scoring a site similarly to the "good" anchor example, your scores should be in the 65-75 range, not 80+. If you are scoring similarly to the "mediocre" anchor, you should be in the 45-55 range.

## Overall Score Calculation

Weighted average with Foundation weighted 1.5x (because Foundation failures cascade to all upper layers):

```
Overall = (Foundation * 1.5 + L1 + L2 + L3 + L4) / 5.5
```

Round to the nearest integer. Apply this formula AFTER dependency caps have been enforced.

## Citation Rules

- Only cite studies from the psychology reference material loaded in this evaluation context
- Every WHY explanation in a violation must trace to a specific citation — study name, finding, and relevance to this specific violation
- If you cannot find a citation in the loaded reference material for a claim, state "practitioner observation" — do NOT fabricate a study name, author, or date
- Do not cite studies you know about but that are not in the loaded corpus — consistency with the reference material is more important than comprehensiveness

## Deviation Handling

- Do NOT flag intentional design deviations as violations when clear intent signals are present
- Intent signals include: consistent application of the deviation across the site, deviation matches a recognized design movement (brutalism, anti-design, maximalism), deviation serves a documented brand purpose
- Examples of intentional deviations: brutalism on a fashion or creative agency site, dense color palettes in expert data tools, minimal typography on portfolios, deliberately asymmetric layouts on editorial sites
- Classify each deviation as one of: **intentional** (clear intent signals), **accidental** (inconsistent application, no pattern), or **unclear** (flag for practitioner review)
- Intentional deviations are noted but not scored as violations. Accidental deviations are scored normally. Unclear deviations are flagged with a recommendation to verify intent.

## Ethics Gate

PFD removes perception barriers to genuine value. It does NOT create perception of value where none exists. This distinction is the ethical boundary of the entire framework.

- **Alignment test:** Do user goals and business goals converge? If the design optimizes for business outcomes at the expense of user outcomes, it fails Alignment.
- **Sincerity test:** Does what the user sees match what they will receive? If the design creates expectations that the product or service cannot fulfill, it fails Sincerity.
- **Golden Rule test:** Would you, as a designer, be comfortable experiencing this design as a user? If not, it fails the Golden Rule.
- **Fluency trap detection:** If L2 scores high (polished, fluent, visually cohesive) but the site contains unverifiable claims, misleading imagery, or hidden costs, flag as a potential fluency trap. Beautiful design making false promises is MORE dangerous than ugly design making false promises — because fluency increases believability (Reber & Schwarz 1999).
