# PFD Evaluation — [Site G — SaaS Pricing Page]

**Site type:** B2B SaaS project management tool. The evaluated page is the pricing page specifically (not the full site), as it demonstrates a cross-layer failure pattern where visual polish coexists with structural conversion failures.
**Framework:** Tailwind CSS v3 + custom component library (not shadcn, not DaisyUI)
**Detection confidence:** 88 — High density of Tailwind utility classes (`flex`, `items-center`, `gap-4`, `rounded-xl`, `shadow-lg`, `text-gray-700`, `bg-blue-600`), responsive prefixes (`md:grid-cols-3`, `lg:text-xl`), `--tw-shadow` and `--tw-ring-color` CSS custom properties. No shadcn/DaisyUI indicators — buttons and cards use custom class names (`.btn-primary`, `.card-pricing`) with Tailwind utilities composed inline. Stacked variants present (`hover:bg-blue-700`, `dark:text-gray-300`).

---

## Foundation (L0): 35/100 — fail

**Reasoning:** The pricing page presents an overwhelming decision environment. Above the fold: a heading ("Choose your plan"), an annual/monthly billing toggle, and 4 pricing tiers displayed as cards in a horizontal row. Each card contains: tier name, price, price annotation (per user/month or per workspace/month — the unit varies by tier), a "Most popular" badge on tier 3, a feature list (12-18 items per card), a comparison toggle ("See all features"), and a CTA button. Below the fold: an expanded feature comparison table with 75+ line items across all 4 tiers (checkmarks, X marks, and text values), an FAQ accordion (8 items), and 3 testimonials. The visible interactive element count on the pricing page is approximately 65 when the comparison table is expanded (4 CTA buttons, billing toggle, 4 "See all features" toggles, 75+ comparison rows that are hoverable, 8 FAQ items, 3 testimonial "Read more" links). The feature lists within each card use 12-18 items with no grouping — users must scan linearly to compare features across tiers. On mobile, the 4 pricing cards stack vertically, creating a scroll distance of approximately 4,500px before reaching the comparison table. No progressive disclosure within the cards — all 12-18 features are visible simultaneously.

**Violations:**
- **[Critical]** V-F-001: Four pricing tiers with 12-18 features each, displayed simultaneously without feature grouping or progressive disclosure within cards. The total information presented above the comparison table is approximately 60 feature claims that must be cross-compared across 4 columns. This exceeds working memory capacity for meaningful comparison by an order of magnitude. — *Cowan 2010: comparing 4 tiers across 12-18 features requires holding 48-72 data points in working memory simultaneously. Even with satisficing strategies (comparing only 2-3 key features), the unstructured feature lists force the user to scan all items to find the features they care about. The absence of feature grouping (e.g., "Collaboration," "Security," "Integrations") eliminates the chunking mechanism that would reduce the effective comparison set.*
- **[Major]** V-F-002: The feature comparison table expands to 75+ line items with no filtering or grouping. Users cannot isolate the feature category relevant to their decision. The table is a wall of checkmarks that requires linear scanning. — *Hick 1952: 75+ comparison rows impose logarithmic decision time scaling. Even with visual scanning shortcuts (looking for X marks vs. checkmarks), the table's length and density make systematic comparison impractical. Most users will satisfice by scanning the first 10-15 rows and ignoring the rest — which means the table's claimed comprehensiveness is illusory.*
- **[Major]** V-F-003: The pricing unit varies by tier. Tier 1 and 2 are priced "per user/month." Tier 3 is priced "per workspace/month." Tier 4 is "custom pricing." Three different pricing units across 4 tiers — the user must mentally convert between unit types to compare costs. — *Sweller 1988: converting between pricing units (per-user vs. per-workspace vs. custom) imposes extraneous cognitive load. The comparison task is inherently complex (choosing the right tier), but the varying units add unnecessary translation effort that is imposed by the pricing structure, not the decision.*

**Strengths:**
- The billing toggle (annual/monthly) is a clean, well-implemented UI element that correctly updates all prices simultaneously
- The FAQ accordion uses progressive disclosure appropriately — 8 questions collapsed with expand-on-click
- Responsive layout stacks the 4 cards vertically on mobile (not a horizontal scroll), which is the correct responsive pattern for pricing cards

**Fixes:**
- V-F-001: Group features within each pricing card into 3-4 categories (e.g., "Core Features," "Collaboration," "Security & Compliance," "Integrations"). Show only the 3-4 most differentiating features per card by default, with a "See all features" expansion for the full list. In Tailwind: wrap feature groups in collapsible `<details>` elements or use a tabbed interface within each card.
- V-F-002: Add category filters to the comparison table. Allow users to filter by feature category rather than scrolling through 75+ rows. Alternatively, restructure the table into tabbed sections by category.
- V-F-003: Standardize the pricing unit across all tiers. If per-user pricing is the primary model, convert Tier 3 to a per-user price with a minimum user count noted separately ("$25/user/month, 10-user minimum"). If workspace pricing is the intended model, convert all tiers to per-workspace. The pricing page should use one unit of comparison.

---

## Layer 1 — First Impression: 40/100 — fail

**Reasoning:** The 50ms impression of the pricing page is "busy." The four pricing cards in a horizontal row create a dense wall of text — each card is approximately 400px tall on desktop, filled with text at 14-16px font sizes. The "Most popular" badge on Tier 3 is the only visual differentiation between cards, but it is subtle (a small badge above the card, same blue as the CTA buttons). The visual weight is distributed evenly across all 4 cards — no clear hierarchy signals which tier the user should evaluate first. The page heading ("Choose your plan") is generic and does not help the user orient. No hero section, no value proposition — the page assumes the user has already decided to buy and jumps directly to tier comparison. Trust signals on the pricing page are limited to a small "30-day money-back guarantee" text note below the cards and a "Trusted by 10,000+ teams" line in the footer. No security badges, no client logos, no testimonials visible in the first viewport (the 3 testimonials are below the comparison table, far below the fold).

**Violations:**
- **[Major]** V-L1-001: No value proposition or orientation context on the pricing page. The page opens with "Choose your plan" and immediately presents 4 pricing cards. Users arriving from external links (email campaigns, search results, comparison sites) have no context about what the product does before being asked to choose a plan. — *Lindgaard 2006: the 50ms evaluation processes layout and density. Four identically-weighted text-heavy cards produce a "dense, undifferentiated" impression. Without a value proposition anchor, the user's rapid evaluation answers "what is this page about?" with "a wall of pricing information" rather than "the plan that's right for me."*
- **[Major]** V-L1-002: Trust signals are not prominent in the pricing viewport. The "30-day money-back guarantee" is small text below the cards. "Trusted by 10,000+ teams" is in the footer. For a page where users are making a purchase commitment, trust evidence should be prominent at the decision point. — *Fogg 2003 (Prominence-Interpretation Theory): on a pricing page — the highest-commitment page on a SaaS site — trust signals must be maximally prominent. Footer-level trust placement fails the prominence test. Users making purchase decisions need credibility evidence adjacent to the price, not 3,000px below it.*
- **[Minor]** V-L1-003: The 4 pricing cards are visually identical in weight (same card size, same shadow depth, same border treatment). The "Most popular" badge on Tier 3 is the only differentiator, but it is small and uses the same blue as the CTA buttons, reducing its salience. — *Practitioner observation: pricing page convention is to visually distinguish the recommended tier — larger card, different background, elevated shadow, contrasting border. The near-identical treatment forces the user to evaluate all 4 tiers rather than anchoring on the recommended option.*

**Strengths:**
- Card layout is clean and organized within each card — consistent internal spacing, clear price display, well-formatted feature lists
- The visual quality is modern — rounded cards, appropriate shadow depths, professional typography
- The page does not look "cheap" or "template" — the design quality matches SaaS conventions

**Fixes:**
- V-L1-001: Add a brief value proposition above the pricing cards: 1 sentence about what the product does and who it is for, plus the "Trusted by 10,000+ teams" metric. Example: "Project management that keeps your team on track. Trusted by 10,000+ teams." This provides context for users arriving from external sources.
- V-L1-002: Move trust signals to immediately below or alongside the pricing cards: money-back guarantee, team count, security certifications (SOC 2, GDPR), and 1-2 brief testimonial snippets. Place these between the cards and the comparison table.
- V-L1-003: Visually distinguish the recommended tier. Make the "Most popular" card 10-15% taller, use a contrasting border color (`border-blue-600` vs. `border-gray-200` for other cards), and increase its shadow depth. In Tailwind: `shadow-xl border-2 border-blue-600 scale-105` on the recommended card vs. `shadow-md border border-gray-200` on others.

---

## Layer 2 — Processing Fluency: 78/100 — pass

**Reasoning:** Within the Tailwind system, the visual language is cohesive. The color palette uses gray neutrals (slate-50 through slate-900) plus a single accent (blue-600). All cards use the same border-radius (`rounded-xl`), shadow (`shadow-lg`), and padding (`p-6`). Typography follows the Tailwind scale: headings at `text-2xl font-bold`, prices at `text-4xl font-bold`, features at `text-sm`, CTAs at `text-base font-medium`. No off-system colors detected — all values trace to the Tailwind slate + blue palette. Spacing is on the Tailwind 4px grid. The comparison table uses consistent row treatment (alternating `bg-slate-50` and `bg-white`). Dark mode is not implemented, which is neutral (not incomplete dark mode — it simply is not offered). The only fluency issue is the transition between the pricing cards section and the comparison table: the cards use generous whitespace and rounded aesthetics, while the table uses dense, flat rows with tight spacing — creating a subtle language shift mid-page.

**Violations:**
- **[Minor]** V-L2-001: The pricing cards (rounded corners, generous padding, shadow elevation) and the comparison table (flat, dense rows, no rounding, no shadow) use noticeably different visual treatments. The cards feel like a modern SaaS aesthetic; the table feels like a spreadsheet. The transition between them creates a subtle visual language break. — *Wertheimer 1923 (Gestalt similarity): the pricing cards and the comparison table serve the same functional purpose (communicate tier differences). Their visual treatments, however, use different design languages. This inconsistency prevents the user from perceiving the two sections as parts of a unified information system.*
- **[Minor]** V-L2-002: CTA buttons within pricing cards use `bg-blue-600 hover:bg-blue-700 text-white rounded-lg`, while the "See all features" toggle buttons use `text-blue-600 underline` — a text link style. Both are interactive elements within the pricing cards, but their visual treatment differs substantially, potentially confusing which is the primary action and which is secondary. — *Practitioner observation: the visual differentiation between primary (filled button) and secondary (text link) actions is appropriate in principle. However, within the context of a pricing card where both actions are vertically stacked and closely spaced, the visual gap between them may cause users to miss the "See all features" toggle.*

**Strengths:**
- Tailwind palette adherence is perfect — zero off-system color values across the entire page
- Spacing follows the 4px grid consistently: `gap-4`, `gap-6`, `p-6`, `py-12` — all on-system
- Border radius is uniform at `rounded-xl` for all cards and `rounded-lg` for all buttons — consistent component-level rounding
- Typography scale is systematic: `text-sm` / `text-base` / `text-lg` / `text-2xl` / `text-4xl` — clear hierarchy within the Tailwind scale
- No arbitrary bracket values detected in spacing, sizing, or color

**Fixes:**
- V-L2-001: Apply a card-like treatment to the comparison table: wrap it in `rounded-xl overflow-hidden shadow-lg`, add `px-6` padding to rows, and soften the alternating row colors to match the card aesthetic. This makes the table feel like an extension of the card system rather than a separate element.
- V-L2-002: Style the "See all features" toggle as a secondary button (`border border-blue-600 text-blue-600 rounded-lg px-4 py-2`) rather than a text link. This maintains the primary/secondary visual hierarchy while giving the secondary action enough visual weight to be noticed.

---

## Layer 3 — Perception Bias: 28/100 — critical

**Reasoning:** The pricing page demonstrates a severe experiential self-contradiction (Learning #15) and a backend-mechanics-surfaced-as-frontend-tiers failure (Learning #18). The product is positioned as a "simple project management tool" — the homepage (not evaluated here, but relevant as the user's arrival context) emphasizes "simplicity," "clarity," and "stop overcomplicating project management." The pricing page, however, presents 4 tiers with 3 different pricing units, 75+ comparison features, and a cognitive load profile that contradicts every simplicity claim. The user's experience of choosing a plan is the opposite of simple. Additionally, the feature comparison reveals that ~60% of the listed features are available on all 4 tiers — the actual tier differentiation is based on 8-10 features, but these are buried in the 75+ row table alongside 50+ shared features. The user is comparing tiers on features that don't differ. Social proof on the pricing page is minimal: "Trusted by 10,000+ teams" in the footer, 3 text testimonials below the comparison table (no photos, no company names, first name + last initial only), and a "30-day money-back guarantee." No security badges, no press logos, no case study links adjacent to the pricing decision.

**Violations:**
- **[Critical]** V-L3-001: Experiential self-contradiction. The product positions itself as "simple project management" but the pricing page is one of the most complex user experiences on the entire site. The user's lived experience of the pricing page — 4 tiers, 3 pricing units, 75+ comparison rows, dense feature lists — disproves the thesis that this company values simplicity. The page is proof that the product's promise of simplicity does not extend to the purchase experience. — *Clark 2013 (predictive processing): the user arrives at the pricing page with a prediction set by the product positioning ("this is a simple tool"). The pricing page violates that prediction at every level — complex tiers, mixed pricing units, dense comparison table. The prediction error is severe and sustained across the entire page experience. This is PFD Learning #15 at full severity: the site's experience contradicts its verbal promise.*
- **[Critical]** V-L3-002: Backend mechanics surfaced as frontend tiers (Learning #18). The 4-tier structure with 3 pricing units suggests the pricing architecture was designed to serve the billing system's needs (different subscription types, usage models, enterprise contracts) rather than the user's decision needs. The mixed pricing units (per-user, per-workspace, custom) are the clearest signal — these represent different billing system configurations presented as comparable options. — *Kahneman & Tversky 1979 (prospect theory): without a consistent reference point (same pricing unit), the user cannot evaluate relative value across tiers. Per-user and per-workspace are fundamentally different units — a user trying to compare "$12/user/month" with "$40/workspace/month" must know both their team size AND their workspace count, then calculate total costs for each model, then compare. The comparison is imposing mathematical computation on what should be a gut-level value judgment.*
- **[Major]** V-L3-003: Testimonials use first name + last initial only, no photos, no company names, no verifiable source. On a pricing page — the highest-commitment decision point — these read as potentially fabricated. — *Cialdini 2001 (social proof): at the moment of purchase commitment, social proof credibility requirements are highest. Anonymous testimonials at the pricing stage trigger defensive evaluation rather than trust. The user needs to see that real, identifiable people at real companies made this decision and were satisfied.*

**Strengths:**
- The "30-day money-back guarantee" is a genuine risk-reduction signal (reciprocity/commitment)
- The annual pricing discount is clearly displayed with both monthly and annual totals
- Feature descriptions in the card lists are specific and concrete ("Unlimited projects," "10 GB storage," "Priority email support")

**Fixes:**
- V-L3-001: Radically simplify the pricing page to match the product's simplicity positioning. Two tiers (Free + Pro) or three tiers maximum. Show only the 5-8 features that actually differentiate between tiers. Move the full comparison table to a separate "Compare plans in detail" page for users who want it. The pricing page should be as simple as the product claims to be.
- V-L3-002: Standardize all pricing to a single unit. Convert per-workspace pricing to per-user equivalent with a note about minimum users. Or convert all to per-workspace if that better represents the value model. One unit, one comparison axis.
- V-L3-003: Upgrade testimonials: add full names, company names, headshot photos, and link to the customer's company or LinkedIn. Alternatively, embed verified reviews from a platform (G2, Capterra). Place testimonials between the pricing cards and the comparison table, not below it.

---

## Layer 4 — Decision Architecture: 22/100 — critical

**Reasoning:** The pricing page's decision architecture is the site's primary failure point. Despite having 4 CTA buttons (one per tier), the decision path is unclear because the user cannot determine which tier is right for them. The "Most popular" badge on Tier 3 attempts to set a default, but it is visually weak (see L1) and does not explain WHY it is most popular (for what use case? what team size?). The feature comparison table, intended to help users decide, actually hinders decision-making — 60% of features are identical across tiers, which means the user must scan 75+ rows to find the 8-10 that differ. No "recommended for you" logic, no team-size-based suggestion, no use-case-based routing. The annual/monthly toggle adds a secondary decision axis before the user has resolved the primary one (which tier). The page presents a comparison task that requires evaluating 4 options across 75+ dimensions — this is decision architecture that optimizes for completeness rather than conversion. The ethics check reveals a concern: the Enterprise tier ("Contact sales") has no pricing information, and the "Get started" CTA on Tier 4 is identical in visual treatment to the self-serve CTAs on Tiers 1-3, potentially misleading users into expecting a self-serve signup when they will reach a sales contact form.

**Violations:**
- **[Critical]** V-L4-001: The decision environment overwhelms rather than guides. 4 tiers, 3 pricing units, 75+ comparison features, no use-case-based routing, no team-size recommendation. The page presents a comparison task so complex that most users will either satisfice (pick the "Most popular" without evaluating) or abandon. Neither outcome is optimal. — *Thaler & Sunstein 2008: effective choice architecture makes the right choice the easiest choice. This page makes NO choice easy — it presents an exhaustive comparison and leaves the user to navigate it alone. The absence of guidance (no "Recommended for teams of 5-20" or "Best for agencies") means the page relies on the user's analytical effort rather than architectural support.*
- **[Major]** V-L4-002: The Enterprise tier CTA ("Get started") uses the same button style and label pattern as the self-serve tiers. Users clicking "Get started" on the Enterprise tier expect to begin signing up; they will instead reach a sales contact form or a "request demo" page. This is a weak information scent issue that borders on a Sincerity violation. — *Pirolli & Card 1999: "Get started" creates scent for a self-serve signup flow. Delivering a sales contact form instead violates the scent prediction. The mismatch between the CTA label and the destination creates a micro-betrayal at the exact moment of commitment.*
- **[Major]** V-L4-003: 60% of comparison table features are identical across all 4 tiers. The table communicates "these tiers are mostly the same" rather than "here is why you should upgrade." The differentiating features (the 8-10 that actually vary) are visually identical to the shared features — no highlighting, no grouping, no "this is what changes when you upgrade" framing. — *Green & Swets 1966: the differentiating features are the "signal" in the comparison table. The shared features are "noise." With 60% noise and 40% signal, the d-prime for tier differentiation is low. The user cannot efficiently detect what is different because the different features look identical to the shared features.*

**Strengths:**
- The billing toggle (annual/monthly) correctly updates all prices and provides a clear price comparison between billing periods
- CTA buttons are present and functional on all tiers — the conversion path exists even if the decision path is unclear
- The FAQ section addresses common pricing concerns (cancellation, team changes, payment methods)

**Fixes:**
- V-L4-001: Add use-case-based routing above the pricing cards: "For individuals → Tier 1, For small teams (2-10) → Tier 2, For growing teams (10-50) → Tier 3, For enterprise (50+) → Tier 4." This provides a decision shortcut before the user evaluates features. In Tailwind: add a 4-item horizontal bar above the cards with team-size ranges that highlight the corresponding card on click or hover.
- V-L4-002: Change the Enterprise CTA from "Get started" to "Talk to sales" or "Request a demo." This honestly predicts the destination. Use a visually distinct button style (outlined instead of filled) to further differentiate it from the self-serve CTAs.
- V-L4-003: In the comparison table, visually distinguish the features that differ between tiers. Options: highlight differentiating rows with a subtle accent background (`bg-blue-50`), add a "Key differences" header above the differing features, or separate the table into "Included in all plans" (collapsed by default) and "What changes when you upgrade" (visible by default).

---

## Cross-Layer Patterns

- **Experiential self-contradiction is the dominant failure (L0 + L1 + L3 + L4).** A product positioned around simplicity has a pricing page that is the opposite of simple. This single contradiction degrades:
  - L0: cognitive load is excessive for a "simple" product's pricing page
  - L1: first impression is "dense comparison tool," not "simple choice"
  - L3: the simplicity claim is experientially disproven
  - L4: the decision architecture requires analytical effort that contradicts the simplicity promise
  The only layer that escapes is L2 — the visual system is cohesive. This is the defining characteristic of a cross-layer failure: the design LOOKS polished (L2 is strong) but the structure WORKS against the user at every other layer.

- **Backend-as-frontend failure (Learning #18): mixed pricing units.** The per-user vs. per-workspace vs. custom pricing structure is a billing system concern surfaced as a frontend comparison axis. The billing system needs different models for different subscription types; the user needs one comparison axis. These are different design surfaces operating at different layers.

- **High L2 + low L3 = potential fluency trap concern.** The visual polish (L2: 78) combined with unverifiable testimonials and an overwhelming decision environment could function as a fluency trap — the design looks credible enough to bypass critical evaluation, but the actual decision support is poor. This is not a confirmed fluency trap (the site does not make false claims), but the pattern warrants noting.

---

## Overall: 39/100

**Calculation:** (35 * 1.5 + 40 + 78 + 28 + 22) / 5.5 = (52.5 + 40 + 78 + 28 + 22) / 5.5 = 220.5 / 5.5 = 40.1 -> **40**

A polished pricing page that fails at its core job: helping users choose a plan. The Tailwind implementation is disciplined — L2 scores well because the visual system is genuinely cohesive. But L2 polish cannot compensate for L0 (overwhelming cognitive load), L1 (no orientation or trust), L3 (experiential self-contradiction with simplicity positioning), and L4 (decision architecture that compares rather than guides). This is the archetype of "beautiful but broken" — a page that passes visual inspection but fails behavioral analysis. The fix is structural, not cosmetic: reduce tiers, standardize pricing units, show only differentiating features, and add decision-support routing.

---

## Top 3 Fixes

1. **Reduce to 3 tiers with standardized pricing unit** — L0 + L3 + L4 — Expected impact: L0 +15 (from 35 to ~50), L3 +12 (from 28 to ~40, resolving one Critical violation), L4 +10 (from 22 to ~32). The single highest-impact change: fewer tiers, one pricing unit, reduced comparison complexity. This resolves the experiential self-contradiction and the backend-as-frontend failure simultaneously.
2. **Add use-case routing above pricing cards** — L4 (primary), L0 (secondary) — Expected impact: L4 +10 (from 32 to ~42 combined with fix 1), L0 +5. A "For individuals / small teams / growing teams" routing bar gives users a decision shortcut that bypasses the need for exhaustive comparison.
3. **Show only differentiating features in cards, move shared features to expandable section** — L0 + L4 — Expected impact: L0 +8 (from 50 to ~58 combined with fixes 1-2), L4 +5. Reducing the visible feature count from 12-18 to 5-8 per card transforms the cards from "comparison tables" to "value summaries."

---

## Dependency Notes

**Foundation < 40 dependency cascade applies:**
- L0 scored 35 (below 40 threshold)
- L1 cap: 50 (L1 scored 40 — below cap, no change)
- L2 cap: 45 (L2 scored 78 — **CAPPED to 45**)
- L3 cap: 40 (L3 scored 28 — below cap, no change)
- L4 cap: 35 (L4 scored 22 — below cap, no change)

**Critical violation caps:**
- L0 has Critical violation (V-F-001) — L0 capped at 30. L0 uncapped: 35, **CAPPED to 30**.
- L3 has Critical violation (V-L3-001 + V-L3-002) — L3 capped at 30. L3 uncapped: 28 — below cap, no change.
- L4 has Critical violation (V-L4-001) — L4 capped at 30. L4 uncapped: 22 — below cap, no change.

**Recalculating with caps applied:**
- L0: 30 (capped from 35)
- L1: 40 (no cap change)
- L2: 45 (capped from 78 due to Foundation < 40 cascade)
- L3: 28 (no cap change, already below Critical cap)
- L4: 22 (no cap change, already below all caps)

**Revised overall:** (30 * 1.5 + 40 + 45 + 28 + 22) / 5.5 = (45 + 40 + 45 + 28 + 22) / 5.5 = 180 / 5.5 = 32.7 -> **33**

**L2 dependency cap is the key observation.** The L2 visual polish (uncapped 78) is capped to 45 by the Foundation dependency — this is the mechanism that prevents a "beautiful but broken" page from scoring well overall. The dependency stack correctly communicates: "it does not matter how polished the design system is if the structural foundation is broken."

**Final score with all caps: 33/100** (revised from uncapped 40).
