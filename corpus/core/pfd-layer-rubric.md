# PFD Layer Rubric — Evaluation Reference

## Scoring Guide

Each layer scores 0-100. Use the FULL range. A score of 20 is appropriate for sites with severe violations. A score of 90+ requires exceptional execution with zero significant violations and specific evidence cited.

| Range | Meaning |
|-------|---------|
| 90-100 | Exceptional — zero Critical, zero Major violations. Specific strengths cited. |
| 70-89 | Good — minor issues only. Core layer requirements satisfied. |
| 50-69 | Mediocre — some Major violations. Core intent partially achieved. |
| 30-49 | Poor — Critical violations present. Layer requirements mostly unmet. |
| 10-29 | Severe — fundamental failures. Layer requirements not addressed. |
| 0-9 | Absent — no evidence of this layer being considered. |

---

## Foundation (L0): Cognitive Load Reduction

**Constraint:** Working memory holds 3-5 chunks simultaneously (Cowan 2010). Every interactive element, content block, and navigation choice competes for attentional slots. Extraneous cognitive load — load imposed by poor design rather than inherent task complexity — must be eliminated before any upper-layer evaluation is meaningful.

**Evaluates:** Interactive element count, progressive disclosure structure, form field complexity, navigation depth and clarity, reading level and content chunking, responsive design implementation, typographic system coherence.

**Failure signals:**
- More than 50 interactive elements on a single view
- More than 7 visible form fields without progressive disclosure or step indicators
- More than 7 top-level navigation items
- No responsive viewport meta tag or broken mobile rendering
- More than 3 distinct font families
- Content exceeding 2000 words with no structural disclosure (headers, tabs, accordions)

**Scores BELOW 30 when:** No responsive design (missing viewport meta or broken mobile layout), OR more than 80 interactive elements on a single view, OR more than 5 distinct font families, OR no progressive disclosure on content exceeding 2000 words. Any of these conditions indicates the Foundation layer was not addressed.

**Scores ABOVE 80 when:** Clear progressive disclosure with manageable element counts per view state. Smart defaults reduce required decisions. Responsive design adapts content density to viewport. Typographic system limited to 2 families (display + body) with optional monospace. Form fields grouped into logical steps with progress indicators when exceeding 4 fields. Navigation prioritized to 5-7 top-level items with secondary paths in footer or overflow menus.

---

## Layer 1: First-Impression Architecture

**Constraint:** Visual appeal judgments form in 50ms with high test-retest reliability (Lindgaard 2006). If this gate fails, users never evaluate L2-L4 — they leave. The aesthetic-usability effect (Kurosu & Kashimura 1995) means visual quality at L1 creates a halo that colors all subsequent perception. Trust signals must be prominent to register (Fogg 2003 Prominence-Interpretation Theory).

**Evaluates:** Hero/opening section clarity and focus, CTA visibility above the fold, trust signal presence and prominence (testimonials, logos, certifications, contact info), visual quality match to price point and brand positioning, image quality and relevance, overall professional impression.

**Failure signals:**
- No identifiable hero section or opening message
- No CTA visible above the fold
- Broken, placeholder, or low-resolution images
- Visual quality mismatch with stated positioning (e.g., premium pricing with stock-template design)
- Missing trust signals on pages where conversion is expected
- Design quality that triggers spam/scam pattern matching

**Scores BELOW 30 when:** No identifiable hero or opening message, no CTA visible without scrolling, broken or placeholder images present, OR the design quality triggers defensive pattern-matching (spam, scam, abandoned site). These are L1 gate failures — users will not proceed to evaluate the rest of the site.

**Scores ABOVE 80 when:** Clear hero with a focused, single-proposition message. Prominent CTA above the fold with specific action language. Trust signals present and visually integrated (not afterthought badges). Visual quality matches or exceeds the brand's stated positioning. Images are high-quality, relevant, and sized appropriately. The 50ms impression communicates competence and relevance.

---

## Layer 2: Processing Fluency

**Constraint:** Easy-to-process information feels more true, more trustworthy, more likeable — and this effect operates below conscious awareness (Reber & Schwarz 1999). Fluency effects are strongest when users are unaware of the source (Alter & Oppenheimer 2009), making design consistency a subconscious trust mechanism. Gestalt grouping principles (Wertheimer 1923) govern how users perceive visual relationships. Near-miss color deviations cost more than large departures due to non-linear perceptual sensitivity (Bujack et al. 2022; PFD Learning #16).

**Evaluates:** Typography consistency (families, weights, sizes, line heights across components), color system coherence (palette adherence, token consistency, near-miss deviations), spacing rhythm (consistent scale, alignment to grid), layout grid consistency (max-widths, gutters, breakpoint behavior), visual language uniformity (border radii, shadow depths, button styles, icon treatment), component pattern consistency across pages.

**Failure signals:**
- More than 3 font families in use
- More than 6 distinct color families (not counting neutral grays)
- Inconsistent spacing between similar elements (no detectable spacing scale)
- Multiple competing max-widths with no clear container system
- Inconsistent button styles, border radii, or shadow depths across components
- Near-miss color deviations (colors within 5% of a design token but not matching)

**Scores BELOW 30 when:** More than 5 font families, more than 8 distinct color families, no consistent spacing system detectable, or multiple competing visual languages on the same page (e.g., one section looks like a different site). These indicate no coherent design system was applied.

**Scores ABOVE 80 when:** 1-2 font families used systematically (display + body). Color palette derives from a coherent system with consistent token usage. Spacing follows a detectable scale (4px, 8px, or similar base unit). Unified visual language across all components — border radii, shadows, button treatments, and icon styles are consistent. The design feels like one mind designed it, even across different page types.

---

## Layer 3: Perception Bias Optimization

**Constraint:** Users make autopilot decisions using System 1 heuristics and rationalize them after the fact (Kahneman 2011). Loss aversion makes losses hurt approximately 2x more than equivalent gains feel good (Kahneman & Tversky 1979). The brain constantly predicts the next input — convention violations are prediction errors that consume cognitive resources (Clark 2013 predictive processing). Design must work with actual decision behavior, not stated preferences.

**Evaluates:** Social proof deployment (presence, placement, credibility), framing effectiveness (loss/gain, urgency/scarcity authenticity), copy-design alignment (verbal message matches visual impression), construal level matching (abstract vs. concrete language matches page intent), persuasion principle detection (Cialdini's 6: reciprocity, commitment, social proof, authority, liking, scarcity), convention adherence vs. intentional deviation.

**Failure signals:**
- No social proof on conversion-critical pages (pricing, checkout, signup)
- Urgency tactics without substance (fake countdown timers, "only 2 left" on digital products)
- Copy that contradicts the visual impression (claiming simplicity while the design is cluttered)
- Abstract claims on pages requiring concrete decisions (vague value props on pricing pages)
- Experiential self-contradiction — the site's lived experience disproves its own thesis (Learning #15)

**Scores BELOW 30 when:** Zero social proof anywhere on the site, manipulative urgency signals with no genuine basis, OR the site's copy fundamentally misaligns with what the design communicates. The visitor's System 1 reads conflict between what is said and what is shown, producing distrust.

**Scores ABOVE 80 when:** Social proof is present, relevant, and credibly placed near decision points. Framing is honest — urgency is real, scarcity is genuine. Copy reinforces what the design communicates (a clean design backs up a simplicity claim). Construal level matches page intent — concrete specifics on pricing/action pages, broader vision on about/mission pages. Persuasion principles are deployed ethically. No experiential self-contradiction.

---

## Layer 4: Decision Architecture

**Constraint:** Structure the environment so the right choice is the easiest choice (Thaler & Sunstein 2008). Users follow information scent — navigation cues and link labels must predict what comes next (Pirolli & Card 1999). CTA detectability among visual noise follows Signal Detection Theory — high d-prime means the signal (CTA) stands out clearly from noise (competing elements) (Green & Swets 1966). Ethical constraint: the "right choice" must align with user goals, not only business goals.

**Evaluates:** CTA clarity and specificity (action labels, visual weight, placement), navigation trail coherence (breadcrumbs, back paths, wayfinding), funnel progression logic (each step leads naturally to the next), exit intent management (what happens when users try to leave), information scent strength (do link labels predict their destinations), ethical compliance (Alignment, Sincerity, Golden Rule tests from PFD Learning #14).

**Failure signals:**
- No clear primary CTA on conversion pages
- Generic CTA labels ("Click Here," "Submit," "Learn More" without context)
- No breadcrumbs or back-navigation on pages 3+ levels deep
- Excessive outbound links on conversion-critical pages (leaking attention)
- User cannot determine the next step from the current view
- Dark patterns (hidden costs, forced continuity, roach motel navigation)

**Scores BELOW 30 when:** No identifiable decision path exists — CTAs are absent, hidden behind scroll, or visually indistinguishable from surrounding elements. The user literally cannot determine what action the page wants them to take. Or: dark patterns are present (hidden costs, forced defaults, deceptive button labeling).

**Scores ABOVE 80 when:** Clear primary CTA presented as the natural resolution of the page's proposition. Specific action labels that describe the outcome ("Start free trial" not "Submit"). Clear navigation trail with breadcrumbs on deep pages. Information scent is strong — every link label predicts its destination. The decision path feels effortless, not coerced. Ethical tests pass: user goals align with business goals (Alignment), what is shown matches what is delivered (Sincerity), the designer would be comfortable experiencing this as a user (Golden Rule).
