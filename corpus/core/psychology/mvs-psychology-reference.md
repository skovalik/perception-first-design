# PFD Psychology Reference — MVS Condensed

This is the condensed psychology corpus for MVS evaluation. Each layer lists its primary research citations with key findings and PFD implications. Full per-layer deep docs are built in subsequent slices (B, A, C). Every violation WHY in a PFD evaluation must trace to a citation in this file. If a claim cannot be traced here, state "practitioner observation" — do not fabricate citations.

---

## Foundation (L0): Cognitive Load

The Foundation layer eliminates extraneous cognitive load — the processing cost imposed by poor design rather than inherent task complexity. Every unnecessary element, every extra decision, every competing visual signal consumes working memory capacity that should be available for the user's actual goal.

### Cowan 2010 — Working Memory Capacity

- **Citation:** Cowan, N. (2010). The Magical Mystery Four: How Is Working Memory Capacity Limited, and Why? *Current Directions in Psychological Science*, 19(1), 51-57. https://doi.org/10.1177/0963721409359277
- **Key finding:** Working memory holds approximately 4 +/- 1 chunks in healthy young adults. This is a revision of Miller's (1956) "7 +/- 2" — Miller's estimate conflated short-term memory with working memory and included rehearsed items. The true capacity for simultaneously active, unrehearsed chunks is closer to 3-5.
- **PFD implication:** Interactive elements on a page each demand a working memory slot to evaluate affordance, relevance, and action cost. Interfaces with more than approximately 50 interactive elements exceed session-level scanning capacity (users cannot evaluate all choices and either satisfice or abandon). Above-fold content should present no more than 4-5 distinct content blocks simultaneously. Forms should expose no more than 4-7 fields per visible step.

### Sweller 1988 — Cognitive Load Theory

- **Citation:** Sweller, J. (1988). Cognitive Load During Problem Solving: Effects on Learning. *Cognitive Science*, 12(2), 257-285. https://doi.org/10.1207/s15516709cog1202_4
- **Key finding:** Cognitive load has three types: intrinsic load (inherent complexity of the task or content), extraneous load (load imposed by poor instructional design or presentation), and germane load (load devoted to constructing and automating schemas). Learning and performance degrade when extraneous load is high, because it competes with intrinsic and germane load for the same limited working memory capacity.
- **PFD implication:** PFD's Foundation layer targets extraneous load elimination. Undifferentiated content walls (2000+ words without headers, tabs, or accordions) maximize extraneous load by forcing users to maintain a mental map of position, progress, and relevance without external scaffolding. Progressive disclosure — section headers, tabbed interfaces, accordion patterns — converts extraneous load into structure that supports scanning and selective reading.

### Hick 1952 — Choice Reaction Time

- **Citation:** Hick, W. E. (1952). On the Rate of Gain of Information. *Quarterly Journal of Experimental Psychology*, 4(1), 11-26. https://doi.org/10.1080/17470215208416600
- **Key finding:** Choice reaction time increases logarithmically with the number of alternatives: T = b * log2(n + 1). Doubling the number of options adds roughly a constant time increment to the decision. The relationship holds for equally probable choices; real-world navigation with user intent produces faster selection but the logarithmic cost remains as a floor.
- **PFD implication:** Navigation items, form field options, and CTA choices all impose Hick's Law costs. More than 7 top-level navigation items produces perceptible hesitation and scanning behavior rather than direct target-seeking. The prescription is to reduce the visible choice set to the minimum required for the current task state — secondary options belong behind progressive disclosure (dropdowns, overflow menus, footer navigation).

---

## Layer 1: First-Impression Architecture

Layer 1 governs the 50ms gate. If the first visual impression fails — signaling low quality, irrelevance, or untrustworthiness — users leave before evaluating any other layer. L1 is the gate; everything downstream depends on it.

### Lindgaard 2006 — 50ms First Impressions

- **Citation:** Lindgaard, G., Fernandes, G., Dudek, C., & Brown, J. (2006). Attention Web Designers: You Have 50 Milliseconds to Make a Good First Impression! *Behaviour & Information Technology*, 25(2), 115-126. https://doi.org/10.1080/01449290500330448
- **Key finding:** Visual appeal judgments of web pages form in as little as 50 milliseconds with high test-retest reliability. Participants shown web pages for 50ms produced visual appeal ratings that strongly correlated with ratings from a 500ms exposure. First impressions are rapid, consistent, and persistent.
- **PFD implication:** The 50ms window defines the L1 gate. In 50ms, users process: overall color scheme, visual density, layout structure, and image quality. They do NOT process: text content, navigation labels, or detailed typography. L1 evaluation checks whether the elements that register in 50ms (hero layout, color, image quality, visual weight distribution) communicate competence and relevance. If the 50ms impression signals "spam," "outdated," or "irrelevant," the user exits before reaching any other layer.

### Tractinsky 2006 — First Impression Consistency

- **Citation:** Tractinsky, N., Cokhavi, A., Kirschenbaum, M., & Sharfi, T. (2006). Evaluating the Consistency of Immediate Aesthetic Perceptions of Web Pages. *International Journal of Human-Computer Studies*, 64(11), 1071-1083. https://doi.org/10.1016/j.ijhcs.2006.06.009
- **Key finding:** Confirmed Lindgaard's 50ms finding using a different experimental methodology. Immediate aesthetic perceptions were highly consistent across repeated measurements and across participants. First impressions are not random noise — they reflect genuine, rapid perceptual evaluation.
- **PFD implication:** The consistency of first impressions means L1 failures are not edge cases. If the 50ms impression is negative, it is negative for the majority of users, consistently. L1 is not a "some users might not like it" issue — it is a systematic gate that blocks all subsequent evaluation for most visitors.

### Kurosu & Kashimura 1995 — Aesthetic-Usability Effect

- **Citation:** Kurosu, M. & Kashimura, K. (1995). Apparent Usability vs. Inherent Usability: Experimental Analysis on the Determinants of the Apparent Usability. *CHI '95 Conference Companion on Human Factors in Computing Systems*, 292-293. https://doi.org/10.1145/223355.223680
- **Key finding:** Visually appealing interfaces are perceived as more usable regardless of actual usability. Users rate attractive layouts as easier to use even when task performance is identical. This is the aesthetic-usability effect: beauty creates a halo that colors all subsequent evaluation.
- **PFD implication:** Visual quality at L1 is not cosmetic — it directly affects how users perceive usability, trustworthiness, and credibility at every subsequent layer. A site with strong L1 (visually polished) gets the benefit of the doubt on L2-L4 minor issues. A site with weak L1 has every subsequent issue amplified by the negative halo. This is why L1 is a gate, not just a layer.

### Fogg 2003 — Prominence-Interpretation Theory

- **Citation:** Fogg, B. J. (2003). Prominence-Interpretation Theory: Explaining How People Assess Credibility Online. *CHI '03 Extended Abstracts on Human Factors in Computing Systems*, 722-723. https://doi.org/10.1145/765891.765951
- **Key finding:** Users assess credibility through a two-step process: (1) they notice an element (prominence), and (2) they make a judgment about it (interpretation). If an element is not prominent, it cannot influence credibility assessment — even if it exists on the page. Trust signals (testimonials, certifications, contact information) must be visually prominent to register.
- **PFD implication:** Trust signals that exist but are buried in footer text, small print, or low-contrast typography are functionally absent for L1 evaluation. Prominence-Interpretation Theory validates PFD's requirement that trust signals be visually prominent above the fold, not merely present somewhere on the page. A trust badge at the bottom of a long scroll page has near-zero credibility impact.

---

## Layer 2: Processing Fluency

Layer 2 governs the subconscious trust mechanism. When visual information is easy to process — consistent typography, coherent color systems, rhythmic spacing — users experience the design as more true, more trustworthy, and more pleasant. This operates below conscious awareness: users do not think "the spacing is consistent, therefore I trust this site." They simply feel trust. Or its absence.

### Reber & Schwarz 1999 — Fluency and Truth

- **Citation:** Reber, R. & Schwarz, N. (1999). Effects of Perceptual Fluency on Judgments of Truth. *Consciousness and Cognition*, 8(3), 338-342. https://doi.org/10.1006/ccog.1999.0386
- **Key finding:** Statements presented in high-contrast, easy-to-read formats were judged as more likely to be true than identical statements presented in low-contrast, hard-to-read formats. Processing fluency — the subjective ease of processing — functions as a heuristic for truth, quality, and trustworthiness. This is THE foundational finding for PFD Layer 2.
- **PFD implication:** Every design decision that affects processing ease — font choice, contrast ratio, spacing consistency, color coherence, layout predictability — is not aesthetic preference. It is a trust lever. Disfluent design (inconsistent styles, low contrast, chaotic spacing) makes content feel less true and the source less trustworthy, independent of actual content quality. L2 evaluation checks whether the design system creates fluent processing or impedes it.

### Alter & Oppenheimer 2009 — Fluency Meta-Review

- **Citation:** Alter, A. L. & Oppenheimer, D. M. (2009). Uniting the Tribes of Fluency to Form a Metacognitive Nation. *Personality and Social Psychology Review*, 13(3), 219-235. https://doi.org/10.1177/1088868309341564
- **Key finding:** Meta-review confirming fluency effects across domains: perceptual fluency, linguistic fluency, retrieval fluency. Key finding for PFD: fluency effects are strongest when users are unaware of the source. Users do not consciously think "the typography is consistent" — they feel trust without knowing why. Design consistency operates as a subconscious signal precisely because it is not consciously evaluated.
- **PFD implication:** L2 violations are invisible to the user but measurable in their behavior. Users will not say "your spacing is inconsistent" — they will say "something feels off" or simply leave. This is why L2 requires systematic evaluation against a design system's token values rather than user feedback. The user cannot articulate L2 failures; the evaluator must detect them.

### Bujack et al. 2022 — Non-Linear Color Perception

- **Citation:** Bujack, R., Teti, E., Miller, J., Caffrey, E., & Turton, T. L. (2022). The Non-Riemannian Nature of Perceptual Color Space. *Proceedings of the National Academy of Sciences*, 119(18). https://doi.org/10.1073/pnas.2119753119
- **Key finding:** Human color perception is non-additive: large color differences are perceived as less than the sum of their small-step components. The perceptual cost curve is non-linear. Small deviations sit in the steep, high-sensitivity zone of the perceptual metric where prediction error is maximal.
- **PFD implication (Learning #16):** Near-miss color deviations — a brand blue that is 3% off-target, a gray that almost matches the system neutral — impose disproportionate processing cost compared to a completely different color. The brain detects "almost right" as more wrong than "clearly different" because the small deviation maximizes prediction error. Design-token linting should weight near-miss deviations (within 5% of a system token) as more severe than far-miss deviations. Every CSS gradient, palette interpolation, and color scale built linearly in hex is non-linear in perception — a systematic L2 fluency violation invisible to the designer. Caveat: the non-additivity finding rests on aggregate data; cite as a theoretical framework, not settled law.

### Wertheimer 1923 — Gestalt Principles

- **Citation:** Wertheimer, M. (1923). Untersuchungen zur Lehre von der Gestalt II [Laws of Organization in Perceptual Forms]. *Psychologische Forschung*, 4, 301-350.
- **Key finding:** The brain organizes visual input according to proximity, similarity, closure, continuity, and figure-ground relationships. Elements that are close together are perceived as grouped. Elements that look similar are perceived as related. Incomplete shapes are completed by the perceptual system. These are not learned conventions — they are hardwired perceptual mechanisms.
- **PFD implication:** Inconsistent border radii, spacing, or color usage disrupts Gestalt similarity grouping — elements that should be perceived as related (same component type, same hierarchy level) are perceived as unrelated because their visual properties diverge. Conversely, elements with similar visual properties are perceived as functionally related even when they are not. L2 evaluation checks whether the visual properties of related elements are consistent (similarity grouping) and whether spacing between groups follows a clear proximity hierarchy.

---

## Layer 3: Perception Bias Optimization

Layer 3 works with how users actually decide, not how they say they decide. Users make rapid, autopilot decisions using System 1 heuristics — then construct rational explanations after the fact. L3 evaluates whether the design works with these decision mechanisms honestly and effectively.

### Kahneman & Tversky 1979 — Prospect Theory and Loss Aversion

- **Citation:** Kahneman, D. & Tversky, A. (1979). Prospect Theory: An Analysis of Decision Under Risk. *Econometrica*, 47(2), 263-292. https://doi.org/10.2307/1914185
- **Key finding:** People evaluate outcomes relative to a reference point (not absolute value), and losses loom larger than gains — approximately 2x. A $50 loss feels roughly as bad as a $100 gain feels good. People are also risk-averse for gains (prefer a certain $50 over a 50% chance of $100) and risk-seeking for losses (prefer a 50% chance of losing $100 over a certain loss of $50).
- **PFD implication:** Pricing pages, urgency messaging, and feature comparison tables all invoke prospect theory. Loss framing ("Don't miss out") is more motivating than gain framing ("Get access") — but only when the loss is genuine. Fake scarcity or artificial urgency triggers defensive pattern-matching rather than loss aversion. L3 evaluates whether loss/gain framing is honest and effective, and whether the reference point is established clearly (what the user has vs. what they could have).

### Cialdini 2001 — Six Principles of Influence

- **Citation:** Cialdini, R. B. (2001). *Influence: Science and Practice* (4th ed.). Boston: Allyn & Bacon.
- **Key finding:** Six universal principles of influence: (1) Reciprocity — people return favors. (2) Commitment/Consistency — people honor commitments. (3) Social Proof — people follow the crowd. (4) Authority — people defer to experts. (5) Liking — people say yes to those they like. (6) Scarcity — people want what is rare. These operate automatically; awareness does not eliminate their effect.
- **PFD implication:** L3 audits which of Cialdini's 6 principles are deployed on a site and whether they are deployed ethically. Social proof is the most relevant for web evaluation: testimonials, user counts, client logos, review ratings. Authority signals: certifications, press mentions, expert endorsements. Scarcity: limited availability, limited-time offers. L3 does NOT require all 6 principles — it evaluates whether the principles that ARE deployed are genuine, well-placed, and effective. Fabricated social proof ("1,000,000+ users" on a startup with no evidence) is an L3 violation, not an L3 feature.

### Clark 2013 — Predictive Processing

- **Citation:** Clark, A. (2013). Whatever Next? Predictive Brains, Situated Agents, and the Future of Cognitive Science. *Behavioral and Brain Sciences*, 36(3), 181-204. https://doi.org/10.1017/S0140525X12000477
- **Key finding:** The brain is fundamentally a prediction engine. It continuously generates predictions about incoming sensory input and processes the prediction errors (differences between expected and actual input). Prediction errors are metabolically expensive — they consume cognitive resources and trigger attention.
- **PFD implication:** Every design convention is a prediction. Users predict that navigation is at the top, that the logo links home, that blue underlined text is a link, that the largest text is the most important. Convention violations are prediction errors — they consume cognitive resources and trigger conscious attention (pulling users out of autopilot). This is the mechanism behind L3's "convention adherence" evaluation: deviations are costly unless they serve a clear purpose. Intentional deviations (brutalism, anti-design) must be classified as intentional and NOT flagged as accidental violations. Accidental deviations (inconsistent navigation placement, randomly styled links) are genuine L3 violations because they generate prediction errors without purpose.

---

## Layer 4: Decision Architecture

Layer 4 structures the environment so the right choice is the easiest choice. Not the only choice — not a dark pattern that eliminates alternatives — but the easiest. L4 is where perception translates into action. The other layers build the perceptual foundation; L4 is the conversion layer.

### Thaler & Sunstein 2008 — Nudge and Choice Architecture

- **Citation:** Thaler, R. H. & Sunstein, C. R. (2008). *Nudge: Improving Decisions About Health, Wealth, and Happiness*. New Haven: Yale University Press.
- **Key finding:** The way choices are presented (the "choice architecture") significantly affects which choices people make. Defaults, ordering, framing, and feedback all influence decisions — often more than the attributes of the options themselves. A "nudge" alters choice architecture in a way that predictably changes behavior without forbidding any options or significantly changing economic incentives.
- **PFD implication:** L4 evaluates the choice architecture of every decision point: Is there a clear default? Is the primary CTA visually weighted as the natural next step? Are alternatives present but not competing? Is the decision environment structured to reduce decision cost? The ethical constraint is critical: the "right choice" that is made easiest must align with user goals, not only business goals. Making a dark pattern easy is not L4 success — it is an ethics violation.

### Pirolli & Card 1999 — Information Foraging and Scent

- **Citation:** Pirolli, P. & Card, S. K. (1999). Information Foraging. *Psychological Review*, 106(4), 643-675. https://doi.org/10.1037/0033-295X.106.4.643
- **Key finding:** Users navigate information environments like animals forage for food — they follow "information scent." Link labels, navigation cues, and visual affordances create a scent trail that users follow to reach their goal. When scent is strong (link labels predict content accurately), users navigate efficiently. When scent is weak (generic labels, ambiguous navigation), users give up or take wrong paths.
- **PFD implication:** L4 evaluates information scent at every navigation point. CTA labels must predict outcomes: "Start free trial" has strong scent (user knows what happens next), "Submit" has weak scent (user does not know the result). Breadcrumbs must reflect the actual content hierarchy. Category labels must match user mental models. Deep pages (3+ levels) without breadcrumbs have zero scent for return navigation — users cannot retrace their path. Excessive outbound links on conversion pages leak scent away from the desired action.

### Green & Swets 1966 — Signal Detection Theory

- **Citation:** Green, D. M. & Swets, J. A. (1966). *Signal Detection Theory and Psychophysics*. New York: Wiley.
- **Key finding:** The ability to detect a signal depends on both signal strength and noise level. The metric d-prime (d') measures how well a signal can be distinguished from noise. High d-prime means the signal stands out clearly; low d-prime means the signal is lost in noise. The optimal detection criterion shifts with the observer's costs and benefits (bias).
- **PFD implication:** The primary CTA is the "signal" on a conversion page. Every other visual element — secondary CTAs, navigation links, decorative elements, competing content blocks — is "noise." L4 evaluation assesses CTA d-prime: does the CTA stand out from its visual surroundings through size, color contrast, whitespace, position, or motion? A CTA that matches the visual weight of surrounding elements (same size, same color, same border treatment) has low d-prime and will be missed. The CTA must break the visual pattern of its surroundings to achieve detection — but through legitimate visual hierarchy, not through deceptive flashing or modal takeover.

---

## Cross-Cutting: Ethics

Ethics is not a separate layer but a constraint that operates across all layers.

### PFD Ethics Tests (Learning #14)

- **Source:** PFD Accumulated Learnings, Learning #14 (2026-02-24)
- **Three tests applied to every evaluation:**
  - **Alignment:** Do user goals and business goals converge? If optimizing for business outcomes at user expense, the design fails Alignment.
  - **Sincerity:** Does what the user sees match what they will receive? If expectations are set that the product or service cannot fulfill, the design fails Sincerity.
  - **Golden Rule:** Would the designer be comfortable experiencing this design as a user? If not, the design fails the Golden Rule.
- **Operational scope:** These are practitioner-level operational ethics — executable by one designer in a single review session. They are NOT structural ethics in the Value Sensitive Design sense (systematic processes). The business model (long-term relationship accountability) provides structural ethics. The tests provide decision-making ethics.

### Fluency Trap Detection

- **Mechanism:** When L2 scores high (the design is polished, fluent, and visually cohesive) but the site contains unverifiable claims, misleading imagery, or hidden costs, the fluency itself becomes a weapon. Beautiful design making false promises is more dangerous than ugly design making false promises — because processing fluency increases believability (Reber & Schwarz 1999). The user's System 1 reads "fluent = true" and does not scrutinize the claims.
- **Detection pattern:** High L2 + unverifiable claims + no trust evidence = potential fluency trap. Flag for practitioner review. This is not an automatic violation — some sites are genuinely polished AND honest — but the combination warrants scrutiny.
- **PFD implication:** The evaluator must separately assess design quality (L2) and claim verifiability (L3 ethics). A site should not receive a high overall score simply because it looks good if its claims cannot be substantiated. Fluency is a trust lever — and like all levers, it can be used honestly or dishonestly.
