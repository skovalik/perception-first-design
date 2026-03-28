# PFD Evaluation — [Site A — SaaS Dashboard Tool]

**Site type:** B2B SaaS analytics dashboard. Subscription product with free trial. Target audience: marketing managers at mid-market companies.
**Framework:** Tailwind CSS v4 + shadcn/ui
**Detection confidence:** 97 — `--radius`, `--primary`, `--background` CSS variables in OKLCH format, `data-slot` attributes on primitives, stacked responsive variants (`dark:hover:bg-zinc-700`), `@layer theme` block in compiled CSS.

---

## Foundation (L0): 88/100 — pass

**Reasoning:** The dashboard interface manages complexity well. Above-fold content presents 4 content blocks: navigation sidebar (collapsed to icon rail on mobile), top metric cards (3 KPIs), a primary chart, and a contextual action bar. Interactive elements on the main dashboard view total approximately 38 — within the 50-element threshold. Navigation uses 6 top-level items in the sidebar with secondary items behind disclosure (chevron-expand groups). Forms across the app use progressive disclosure: the report builder exposes 3 fields initially with an "Advanced filters" expansion that reveals 5 more. Responsive implementation is thorough — sidebar collapses to bottom tab bar on mobile (<768px), chart resizes via container queries (`@md:` variants), metric cards stack to single column. Typographic system uses 2 families: Inter for body/UI and a monospace (JetBrains Mono) for data values.

**Violations:**
- **[Minor]** V-F-001: Settings page exposes 14 form fields simultaneously without step grouping or tabs. While each field is clearly labeled, the count exceeds the 7-field threshold for progressive disclosure. — *Hick 1952: choice reaction time increases logarithmically with alternatives. 14 simultaneous fields impose measurable decision latency, even with clear labels, because each field requires evaluation of relevance and priority.*
- **[Minor]** V-F-002: Mobile bottom navigation uses 5 items including a "More" overflow. The 5th item ("More") groups 4 secondary actions behind a sheet. Acceptable, but the "More" label has weak information scent — users cannot predict what is behind it. — *Practitioner observation: "More" as a navigation label is a known weak-scent pattern, though this is a minor Foundation concern (primary impact is at L4).*

**Strengths:**
- Consistent progressive disclosure pattern across all multi-step flows (report builder, onboarding wizard, billing setup)
- Container query-based responsiveness — components adapt to their container, not just viewport, producing correct layouts in split-pane dashboard views
- Typographic system limited to 2 families with clear role separation (UI text vs. data values)
- Smart defaults on all filters and date pickers reduce required decisions (last 30 days pre-selected, primary metric pre-focused)

**Fixes:**
- V-F-001: Group the 14 settings fields into 3-4 tabbed sections (e.g., "Profile," "Notifications," "Integrations," "Billing") using shadcn `Tabs` component. Each tab exposes 3-5 fields. Implementation: wrap field groups in `<Tabs defaultValue="profile">` with `<TabsContent value="profile">` sections.
- V-F-002: Replace "More" label with the most important action it contains (e.g., "Settings") and move the remaining items to within that section. Alternatively, use an icon that communicates the grouped content (grid icon, not ellipsis).

---

## Layer 1 — First Impression: 92/100 — pass

**Reasoning:** The marketing/landing page (pre-login) has a focused hero: a single proposition ("See what's actually driving revenue"), a dashboard screenshot with real data (not placeholder), and a single CTA ("Start free trial — no credit card"). Trust signals are prominent above the fold: 3 recognizable client logos (anonymized but enterprise-tier), an aggregate review badge ("4.8 on G2, 200+ reviews"), and SOC 2 compliance badge. Visual quality matches the SaaS price point ($49-199/mo range implied by positioning). The screenshot uses a subtle parallax float effect that adds polish without distracting. Color scheme (zinc neutrals + blue-500 primary accent) communicates professionalism. The 50ms impression reads "competent, modern, trustworthy."

**Violations:**
- **[Minor]** V-L1-001: The G2 review badge uses a slightly different shade of green (#22C55E) than G2's actual brand green (#FF492C for the star, white/dark for the badge). This is a near-miss color issue — users familiar with G2 may perceive the badge as off, triggering a micro prediction error. — *Clark 2013 (predictive processing): the brain predicts familiar brand colors; deviations, even small ones, generate prediction errors that consume cognitive resources and may trigger credibility scrutiny.*

**Strengths:**
- Hero proposition is specific and benefit-framed ("what's actually driving revenue" rather than "analytics platform")
- Trust signals are integrated into the visual hierarchy, not appended as afterthought badges in a footer strip
- Dashboard screenshot uses real-looking data — not obviously lorem ipsum or round numbers — which passes the authenticity check at first glance
- CTA specificity is strong: "Start free trial — no credit card" addresses the two primary objections (cost and commitment) in the button label itself
- Visual weight distribution focuses attention: hero text (large, left) -> screenshot (right, slightly elevated via shadow) -> CTA (high contrast, below text)

**Fixes:**
- V-L1-001: Match the G2 badge to G2's actual brand colors exactly, or use G2's official embeddable badge widget which handles its own styling. In Tailwind: replace the custom `bg-[#22C55E]` with the actual G2 badge component or a verified color match.

---

## Layer 2 — Processing Fluency: 90/100 — pass

**Reasoning:** The design system is remarkably cohesive. shadcn/ui's semantic token layer (`bg-background`, `text-foreground`, `bg-muted`, `text-muted-foreground`) is used consistently — no instances of direct Tailwind color scale usage (e.g., no `bg-zinc-100` where `bg-muted` should be used). Spacing follows Tailwind's 4px grid without arbitrary value overrides — spot-checking 20+ elements revealed zero `[...]` bracket values in spacing. Border radius is globally set via shadcn's `--radius: 0.5rem` and applied consistently to all cards, inputs, buttons, and dialogs. Shadow usage follows a clear hierarchy: `shadow-sm` on cards, `shadow-md` on dropdowns and popovers, `shadow-lg` on modals. Typography sizes use the Tailwind scale exclusively (`text-sm`, `text-base`, `text-lg`, `text-xl`, `text-2xl`). The color palette uses zinc neutrals + 2 chromatic accents (blue primary, amber for warnings/alerts), totaling 3 color families plus the neutral scale. Dark mode implementation covers all components — no orphaned light-mode-only elements detected.

**Violations:**
- **[Minor]** V-L2-001: The marketing landing page uses `gap-6` (24px) between feature cards, while the dashboard's metric cards use `gap-4` (16px). Both are on-system values, but the inconsistency between two visually similar card grids across page types creates a subtle fluency break. — *Wertheimer 1923 (Gestalt similarity grouping): visually similar elements (card grids) are expected to share spatial properties. When two card grids use different spacing, the perceptual system registers them as belonging to different groups, which contradicts their functional equivalence.*

**Strengths:**
- Zero off-system color values detected — all colors trace to shadcn semantic tokens or the configured Tailwind palette
- Consistent component visual language: all buttons, inputs, cards, and dialogs follow the same border-radius, shadow depth, and padding patterns
- Font weight hierarchy is systematic: `font-normal` for body, `font-medium` for labels and secondary headings, `font-semibold` for primary headings, `font-bold` reserved for data emphasis (KPI values)
- Dark mode is complete and uses semantic tokens — the switch preserves all visual relationships
- Spacing scale usage is disciplined: section spacing uses `py-16` / `py-24` consistently, component internal padding uses `p-4` / `p-6` consistently

**Fixes:**
- V-L2-001: Standardize card grid gap to `gap-4` across both marketing and dashboard contexts, or use `gap-6` in both. Choose the value that provides better breathing room for the card content and apply it universally. In Tailwind: update the grid wrapper class to use the same `gap-{n}` token.

---

## Layer 3 — Perception Bias: 82/100 — pass

**Reasoning:** Social proof deployment is effective — the landing page uses client logos, aggregate G2 rating, and 3 specific testimonials with names, titles, and company names (credible sourcing). Pricing page uses loss framing appropriately: the free trial CTA says "Start free — upgrade when you're ready" (low commitment, no artificial urgency). Feature comparison between tiers uses concrete specifics (exact numbers: "50 reports/month" vs. "Unlimited reports") rather than vague tiers. No countdown timers, fake scarcity, or manipulative urgency detected. Copy-design alignment is strong — the clean, data-focused design matches the "clarity" messaging. However, the "Enterprise" tier uses "Contact sales" without any anchor pricing, creating a construal level mismatch on what is otherwise a concrete, self-serve pricing page.

**Violations:**
- **[Major]** V-L3-001: The Enterprise tier displays "Contact sales" with no price anchor, no starting-at price, and no usage-based estimate. On a pricing page where other tiers provide exact monthly costs ($49, $99, $199), the Enterprise tier's opacity creates a construal level mismatch. Users in concrete decision mode (comparing specific numbers) hit an abstract wall. — *Kahneman & Tversky 1979 (prospect theory): without a reference point, users cannot evaluate the Enterprise option relative to the visible tiers. The lack of an anchor makes it impossible to assess whether Enterprise represents a 2x or 20x jump from the $199 tier, triggering loss aversion (fear of unknown cost) rather than the intended prestige signal.*
- **[Minor]** V-L3-002: The annual billing toggle shows "Save 20%" but does not show the monthly-equivalent price alongside the annual price. Users must calculate the per-month savings mentally. — *Practitioner observation: failing to show the comparison price makes the "20% savings" claim abstract rather than concrete, reducing its effectiveness as a loss-framing tool. Users who see "$79/mo billed annually (vs. $99/mo)" process the saving immediately.*

**Strengths:**
- Social proof is credible, specific, and placed near decision points (testimonials adjacent to CTAs, not isolated in a separate section)
- No fake urgency, no countdown timers, no "limited spots" language on a SaaS product — the design respects the user's intelligence
- Feature comparison uses concrete numbers rather than checkmark grids, which supports informed decision-making
- Copy tone matches design tone: both are calm, professional, and data-focused — no experiential self-contradiction

**Fixes:**
- V-L3-001: Add a starting price or price range to the Enterprise tier: "Starting at $499/mo" or "Custom pricing from $499/mo." This provides a reference point without committing to a fixed price. In the pricing card component, add a `text-2xl font-semibold` price element above the CTA, styled consistently with the other tier price displays.
- V-L3-002: Show monthly-equivalent pricing on the annual toggle: display both "~~$99/mo~~ $79/mo billed annually" using Tailwind's `line-through` utility on the original price. This makes the saving concrete without requiring mental math.

---

## Layer 4 — Decision Architecture: 87/100 — pass

**Reasoning:** The primary decision path is clear: Landing hero CTA -> Sign up form (email + password, 2 fields) -> Onboarding wizard (3 steps) -> Dashboard. CTA language is specific throughout: "Start free trial" (not "Get started"), "Create your first report" (not "Continue"), "Invite your team" (not "Next"). The recommended pricing tier is visually distinguished with a "Most popular" badge and a subtle border highlight (`border-primary`), establishing a clear default. Navigation uses breadcrumbs on all pages 2+ levels deep. Information scent is strong — sidebar labels predict their destinations accurately. The one significant gap is exit handling: when a user starts the onboarding wizard and navigates away, there is no save-state or reminder — they return to step 1.

**Violations:**
- **[Major]** V-L4-001: The onboarding wizard does not persist progress. Users who leave mid-wizard (e.g., to check email for an API key) must restart from step 1. For a 3-step wizard where step 2 requires an external API key, this is a meaningful friction point. — *Pirolli & Card 1999 (information foraging): the wizard creates an information scent trail, but abandoning the trail and returning eliminates all accumulated progress signals. The user's "foraging path" is erased, requiring them to re-navigate territory they have already covered.*
- **[Minor]** V-L4-002: The "Upgrade" prompt in the dashboard sidebar uses the same visual weight (`text-primary font-medium`) as the navigation items. It does not stand out as a distinct action path. — *Green & Swets 1966 (signal detection theory): the upgrade prompt has low d-prime — its visual weight matches surrounding navigation labels, making it functionally invisible as a conversion signal. It registers as another navigation item, not a distinct action.*

**Strengths:**
- CTA labels are specific and outcome-predictive throughout the entire funnel — zero instances of "Submit," "Click here," or "Learn more" without context
- Pricing page default tier is clearly indicated via visual hierarchy (badge + border), following Thaler & Sunstein's choice architecture principle of making the recommended option the easiest choice
- Breadcrumb navigation on all pages beyond root level provides clear wayfinding
- The sign-up form is minimal (2 fields) — OAuth options (Google, GitHub) further reduce friction
- Ethics check: user goals (understand marketing data) and business goals (convert to paid tier) are well-aligned. No dark patterns detected. The free trial is genuinely free with no hidden credit card requirement.

**Fixes:**
- V-L4-001: Persist onboarding wizard state to `localStorage` or the user's account. When the user returns, show a "Continue where you left off" prompt with the current step indicated. If using React, wrap the wizard in a state provider that syncs to storage on each step completion.
- V-L4-002: Distinguish the "Upgrade" CTA from navigation items by using a filled button treatment (`bg-primary text-primary-foreground rounded-md px-3 py-1.5`) instead of a text link. Place it in a visually distinct zone (e.g., above the navigation list with a separator).

---

## Cross-Layer Patterns

- **No experiential self-contradiction detected.** The site claims to bring clarity to marketing data, and the design itself is clear and data-focused. The experience reinforces the thesis.
- **Minor cross-layer theme: the Enterprise pricing gap (L3) creates a downstream L4 issue.** Without a price anchor, users cannot make a decision about Enterprise — they must leave the self-serve flow and enter a sales process. This is a deliberate business choice (enterprise sales qualification), but it introduces friction that affects both L3 (no reference point) and L4 (broken self-serve decision path).

---

## Overall: 88/100

**Calculation:** (88 * 1.5 + 92 + 90 + 82 + 87) / 5.5 = (132 + 92 + 90 + 82 + 87) / 5.5 = 483 / 5.5 = 87.8 -> **88**

A cohesive, well-executed SaaS product with a clear design system and strong alignment between marketing positioning and actual product experience. The few violations are minor-to-moderate and concentrated in edge cases (settings page disclosure, Enterprise pricing opacity, onboarding state persistence) rather than systemic failures. The shadcn/ui + Tailwind foundation provides excellent token discipline, and the team has used it consistently.

---

## Top 3 Fixes

1. **Add Enterprise tier price anchor** — L3 + L4 — Expected impact: L3 +5 (from 82 to ~87), L4 +2 (from 87 to ~89). Unblocks the self-serve decision path for enterprise-interested users and provides the missing reference point.
2. **Persist onboarding wizard state** — L4 — Expected impact: L4 +4 (from 87 to ~91). Eliminates the highest-friction point in the conversion funnel for users who need to leave mid-onboarding.
3. **Group settings fields into tabs** — L0 — Expected impact: L0 +3 (from 88 to ~91). Reduces the one page that exceeds the progressive disclosure threshold.

---

## Dependency Notes

No dependency caps applied. All layer scores are above 40, and no Critical-severity violations were found. The score spread (82-92) is expected — L3 is naturally lower due to the Enterprise pricing gap, which is a genuine L3 issue, not leniency drift.
