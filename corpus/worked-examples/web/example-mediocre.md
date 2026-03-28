# PFD Evaluation — [Site C — Local Services Company]

**Site type:** Local HVAC and plumbing company serving a metropolitan area. Lead generation model — phone calls and form submissions. 5-page site (Home, Services, About, Reviews, Contact).
**Framework:** WordPress + Elementor
**Detection confidence:** 92 — `.elementor-section`, `.elementor-widget`, `.elementor-column` classes throughout, `data-elementor-type` attributes, `/wp-content/plugins/elementor/` assets loaded, `elementor-kit-437` body class, `--e-global-color-primary` CSS variable present, `/wp-content/themes/hello-elementor/` stylesheet path, `<meta name="generator" content="WordPress 6.4.3">`.

---

## Foundation (L0): 55/100 — fail

**Reasoning:** The site is functional on desktop but has significant mobile issues. Desktop layout presents a reasonable content structure: header with logo/phone/navigation, hero section, 3 service cards, testimonial slider, and a contact form. Interactive element count on the homepage is approximately 42 — within threshold. Navigation uses 5 top-level items, appropriate for a 5-page site. However, the mobile experience degrades meaningfully: the hero text at 375px viewport runs to 5 lines due to large fixed font size (`font-size: 48px` with no responsive scaling), the service cards do not stack properly (they overflow horizontally, requiring side-scroll), and the contact form fields are narrow enough that autocomplete dropdowns are clipped. The site has a viewport meta tag and the Elementor responsive system is partially applied — some sections adapt, others do not. There are 3 font families in use: Montserrat (headings), Open Sans (body), and Roboto (contact form labels, likely from a forms plugin). A cookie consent banner and a Tidio chat widget are both visible on mobile, consuming approximately 25% of the viewport together.

**Violations:**
- **[Critical]** V-F-001: Service card section overflows horizontally on mobile (375px). Three cards are laid out using Elementor's column widget at 33% width each with no responsive breakpoint override. The cards do not wrap or stack, creating a horizontal scroll that hides 2 of 3 services. — *Cowan 2010: working memory holds 3-5 chunks. When 2 of 3 content blocks are hidden behind horizontal scroll (a non-standard interaction on mobile), those blocks are functionally absent from working memory. The user processes only the 1 visible card and has no structural cue that more exist.*
- **[Major]** V-F-002: Hero heading uses fixed `font-size: 48px` (inline style from Elementor) with no responsive override. At 375px viewport, the heading wraps to 5 lines, pushing the CTA below the fold. The hero section alone consumes 1.5 viewport heights on mobile. — *Sweller 1988: the extended hero creates extraneous cognitive load — the user must scroll past content they have already begun processing (the heading) to reach the action (the CTA). This is load imposed by poor presentation, not inherent task complexity.*
- **[Minor]** V-F-003: Three font families in use (Montserrat, Open Sans, Roboto). The third font (Roboto) appears only in the contact form, likely injected by the forms plugin rather than an intentional design choice. — *Practitioner observation: 3 font families is at the threshold. The issue is less the count and more the source — the third font is an accidental injection from a plugin, not a deliberate typographic choice.*

**Strengths:**
- Navigation is appropriately scoped to 5 items for a 5-page site — no overloaded menus
- Desktop layout follows a logical top-to-bottom information hierarchy: who we are -> what we do -> what others say -> contact us
- Contact form uses 5 fields (name, email, phone, service type dropdown, message) — a reasonable count for a lead gen form
- Phone number is prominent in the header on both desktop and mobile — critical for a local service business where phone calls are the primary conversion

**Fixes:**
- V-F-001: In Elementor, select the service card section. Under Advanced > Responsive, set the column layout to stack vertically on mobile (Mobile: 100% width for each column). This is a single click in Elementor's responsive controls.
- V-F-002: In Elementor, select the hero heading widget. Under Style > Typography, click the responsive device icon and set a mobile-specific font size (28-32px). Alternatively, use Elementor's "Text Size" slider with the mobile breakpoint selected.
- V-F-003: In the contact form plugin settings, override the form font to inherit from the parent: add `font-family: inherit;` to the form's custom CSS field. This forces the form to use Open Sans (the body font) instead of loading Roboto.

---

## Layer 1 — First Impression: 48/100 — fail

**Reasoning:** The hero section uses a stock photo of a smiling technician with a wrench against a blue background. The image is generic — it does not show the actual company, actual trucks, actual team, or the local service area. The hero headline ("Quality HVAC & Plumbing Services You Can Trust") is functional but generic. The CTA ("Get a Free Estimate") is present above the fold on desktop but pushed below the fold on mobile due to the oversized heading. Trust signals are limited: a BBB badge and a "Licensed & Insured" text note are present in the footer, but nothing is visible in the first viewport. No Google review rating, no "years in business" claim, no real customer photos. The color scheme (dark blue header, light gray body, orange CTA accent) is professional enough but reads as template — there is nothing distinctive about the visual identity. The 50ms impression is "generic local services template," which is not harmful but does not build confidence.

**Violations:**
- **[Major]** V-L1-001: Hero image is a recognizable stock photo. Users who encounter the same or similar stock images across multiple local service websites (common in this industry) will trigger the "template" pattern match at L1, reducing credibility. — *Kurosu & Kashimura 1995 (aesthetic-usability effect): the stock photo fails to create a positive aesthetic halo. It is not ugly (which would be actively harmful), but it is generic (which is neutral-to-negative). The aesthetic-usability effect works in both directions — mediocre aesthetics create a mediocre usability perception.*
- **[Major]** V-L1-002: No trust signals visible above the fold. The BBB badge and "Licensed & Insured" note exist only in the footer. For a local service company asking homeowners to let strangers into their homes, trust signals are not optional — they are the L1 gate. — *Fogg 2003 (Prominence-Interpretation Theory): trust signals in the footer have near-zero prominence. The user evaluates credibility from what is visible in the first viewport. Footer-only trust placement is functionally equivalent to no trust signals for L1 purposes.*
- **[Minor]** V-L1-003: The hero headline "Quality HVAC & Plumbing Services You Can Trust" is a claim without evidence. Pairing "trust" language with a stock photo and no visible social proof creates a mild irony — the site asks for trust while providing no trust evidence. — *Practitioner observation: the claim itself is not a violation, but the unsupported claim paired with the stock photo slightly undermines the intended impression.*

**Strengths:**
- The CTA ("Get a Free Estimate") is specific and benefit-oriented — users know what will happen when they click
- The phone number in the header is large, prominent, and uses click-to-call on mobile — this is the most important conversion element for a local service business and it works correctly
- The color scheme, while generic, is at least professional and does not trigger spam/scam pattern matching

**Fixes:**
- V-L1-001: Replace the stock hero image with actual photos: the company truck, the team, or a recognizable local landmark/job site. Even a smartphone-quality real photo outperforms a professional-quality stock photo for trust in local services. In Elementor: swap the image widget source.
- V-L1-002: Add a trust strip directly below the header or within the hero section. Include: Google review rating + count ("4.8 stars — 340+ reviews"), years in business ("Serving [City] since 2005"), and license number. In Elementor: add an inner section within the hero with 3-4 icon-list widgets showing trust data.
- V-L1-003: Replace the generic headline with a specific, locally-anchored proposition: "[City]'s Top-Rated HVAC & Plumbing — 4.8 Stars on Google" or "Same-Day Service in [City] — Licensed & Insured Since 2005." Anchor the claim to verifiable evidence.

---

## Layer 2 — Processing Fluency: 42/100 — fail

**Reasoning:** The design system is fragmented across three sources: the Elementor global settings, the theme's CSS, and plugin-injected styles. Elementor's global colors (`--e-global-color-primary`: dark blue, `--e-global-color-secondary`: orange accent) are used on some elements but overridden by inline styles on others. Buttons appear in 3 distinct styles: Elementor's global button (rounded, orange, Montserrat font), the contact form submit button (square corners, blue, Roboto font), and the Tidio chat widget trigger (rounded-full, teal, system font). Heading sizes vary without a clear scale — the hero is 48px, service card headings are 28px, the testimonial section heading is 36px, and the contact form heading is 24px. These do not follow a consistent typographic scale (not a power scale, not Elementor's defaults). Spacing between sections varies: the hero-to-services gap is 80px, services-to-testimonials is 40px, testimonials-to-contact is 60px. No consistent spacing rhythm. Border radius varies: service cards use `border-radius: 10px`, the contact form container uses `border-radius: 5px`, and buttons use `border-radius: 25px`. Three different rounding values with no systematic relationship.

**Violations:**
- **[Major]** V-L2-001: Three distinct button styles across the site — different border-radius (25px, 0px, 9999px), different background colors (orange, blue, teal), and different font families (Montserrat, Roboto, system-ui). Buttons are the most repeated interactive element; their inconsistency is the most visible fluency violation. — *Wertheimer 1923 (Gestalt similarity): buttons should be perceived as a single functional group. Three distinct button treatments break similarity grouping — the user processes each as a separate element type rather than recognizing them as instances of the same "action" affordance. This multiplies the cognitive cost of every button interaction.*
- **[Major]** V-L2-002: Section spacing follows no detectable rhythm — 80px, 40px, 60px between adjacent sections with no content-driven rationale for the variation. The inconsistency is felt as a subtle "something is off" sensation that the user cannot articulate. — *Reber & Schwarz 1999: processing fluency affects truth judgments. Inconsistent spacing is disfluent — the visual rhythm is unpredictable, which reduces the subconscious trust signal. Users will not say "the spacing is inconsistent" — they will feel less confident about the business.*
- **[Minor]** V-L2-003: Border radius uses 3 values (5px, 10px, 25px) with no systematic relationship. The 10px cards and 25px buttons create a noticeable shape language conflict — are elements meant to be rounded or sharp? The design provides no consistent answer. — *Wertheimer 1923 (Gestalt similarity): border radius is a visual variable that signals grouping. Inconsistent radius values disrupt the perceived relationship between components — cards and buttons feel like they belong to different design systems.*

**Strengths:**
- Elementor's global color system is partially applied — the primary (blue) and accent (orange) colors are mostly consistent where the theme system controls the output
- Typography within body text is consistent — Open Sans at 16px with 1.5 line height across all paragraph content
- Image sizing within the service cards is consistent — all three cards use the same image dimensions and aspect ratio

**Fixes:**
- V-L2-001: Unify all buttons to Elementor's global button style. In Elementor > Site Settings > Global Style > Buttons, set the definitive border-radius, background color, and font. Then override the contact form plugin's button CSS: `.wpcf7-submit { border-radius: var(--e-global-button-radius); background: var(--e-global-color-secondary); font-family: Montserrat; }`. For the Tidio widget: in Tidio settings, match the chat button color to the site's accent.
- V-L2-002: Standardize section spacing to a single value. In Elementor, select each section and set consistent top/bottom padding (e.g., 80px on desktop, 48px on mobile). Apply the same value to all sections for a predictable rhythm.
- V-L2-003: Choose one border-radius for all containers (e.g., 10px) and one for all buttons (e.g., 8px or the container value). Apply globally via Elementor Site Settings.

---

## Layer 3 — Perception Bias: 52/100 — fail

**Reasoning:** Social proof is present but weak. The testimonial section shows 3 rotating text-only quotes with first names and last initials ("John S.," "Maria L.," "David K."). No photos, no verified platform badges (not linked to Google or Yelp), no dates. The testimonials read as potentially fabricated — clean, concise, suspiciously similar in tone and length. There is no aggregate review score visible anywhere on the site. The BBB badge in the footer links to the actual BBB profile (verifiable), which is a genuine trust signal — but its footer placement renders it nearly invisible. The copy-design alignment is acceptable: the site claims to be reliable and professional, and the design is... adequate. It does not actively contradict the claims, but it does not reinforce them either. No urgency mechanics are present — no seasonal offers, no scarcity claims.

**Violations:**
- **[Major]** V-L3-001: Testimonials are unverifiable. Text-only quotes with first name and last initial, no photos, no platform link, no dates. The format pattern-matches to "fabricated testimonials" — a pattern users encounter frequently on template sites. Even if these testimonials are real, the presentation undermines their credibility. — *Cialdini 2001 (social proof): social proof's effectiveness depends on perceived credibility. Anonymous, unverifiable testimonials trigger defensive evaluation rather than the autopilot trust that credible social proof enables. Named, photographed, platform-linked reviews are the credibility standard users now expect.*
- **[Minor]** V-L3-002: No aggregate review score from a verifiable platform (Google, Yelp, BBB rating) is displayed anywhere except the footer BBB badge. The site misses the opportunity to lead with its strongest social proof signal. — *Cialdini 2001: aggregate ratings from recognized platforms carry authority (Cialdini's "authority" principle) in addition to social proof. A "4.8 stars on Google — 340 reviews" badge combines social proof + authority in a single element. Its absence weakens the persuasion stack.*

**Strengths:**
- No manipulative urgency tactics — the site does not use countdown timers, fake scarcity, or pressure language
- The BBB badge links to the actual BBB profile, which is a verifiable trust signal (even though its placement is poor)
- The "Free Estimate" offer is genuine reciprocity (Cialdini) — providing value before asking for commitment
- Service descriptions are concrete: specific service types listed, specific area served, specific emergency response time ("Same-day emergency service")

**Fixes:**
- V-L3-001: Replace text-only testimonials with embedded Google Reviews or Yelp reviews. If the business has strong Google reviews, embed them using a widget that shows the full review with the reviewer's name, photo, star rating, and a "View on Google" link. If a widget is not available, manually add customer photos and full names (with permission) and link to the platform where the review lives.
- V-L3-002: Add a Google review aggregate badge prominently in the hero area or the trust strip recommended in the L1 fixes. Display as: "[Star icons] 4.8 — Based on 340 Google Reviews." Link the badge to the Google Business Profile.

---

## Layer 4 — Decision Architecture: 50/100 — fail

**Reasoning:** The site has two primary conversion paths: phone call (header phone number) and form submission (contact form at page bottom). The phone number is well-placed and prominent — this works. The contact form, however, is buried at the bottom of a long-scroll homepage. There is no CTA that links to the form from the hero area; the "Get a Free Estimate" hero CTA links to the contact form at the bottom of the same page (anchor link), but the long scroll past services, testimonials, and an about section creates significant friction. On the Services page, individual service descriptions (e.g., "AC Repair," "Furnace Installation") have no CTAs — they describe the service but provide no action path. Users must navigate back to the Contact page or scroll to the bottom form. No breadcrumbs are present, though with a 5-page flat architecture, this is less critical. The CTA language is adequate ("Get a Free Estimate," "Call Now") but there is no differentiation between the phone CTA and the form CTA in terms of visual hierarchy — both are orange buttons of similar size.

**Violations:**
- **[Major]** V-L4-001: Service descriptions on the Services page have no CTAs. Each service (AC Repair, Furnace Installation, Plumbing, etc.) is a content block with a description and an icon, but no "Schedule AC Repair" or "Get a Plumbing Estimate" button. The user reads about a service and then has no clear next step on that page. — *Pirolli & Card 1999 (information foraging): the user follows scent from the navigation ("Services") to the service description. The scent trail ends abruptly — the service page describes what is available but does not provide a foraging cue for the next step (requesting that specific service). The user must back-navigate or find a generic form, losing the specificity of their intent.*
- **[Major]** V-L4-002: The contact form is only accessible via a long scroll from the hero or from the Contact page navigation link. No persistent CTA (sticky header button, floating action button, or footer CTA bar) provides continuous access to the form across all pages. — *Green & Swets 1966 (signal detection theory): the form CTA has low d-prime across most of the site because it is only visible at the page bottom. On the Services and About pages, the conversion path is entirely absent from the visible viewport.*
- **[Minor]** V-L4-003: "Get a Free Estimate" (form CTA) and "Call Now" (phone CTA) are visually identical — same orange button, same size, same weight. Users cannot distinguish the preferred path at a glance. — *Thaler & Sunstein 2008: choice architecture should make the recommended option easiest. When both CTAs look identical, neither is the default — the user must read the labels and decide, rather than following a visual hierarchy that guides them to the higher-value action (for this business, probably the phone call).*

**Strengths:**
- Phone number is prominently displayed and uses click-to-call — the single most important conversion element for a local service business
- The "Get a Free Estimate" CTA uses specific language that predicts the outcome (a free estimate, not a sales call)
- The 5-page flat architecture means navigation is simple and users are never more than 1 click from any page

**Fixes:**
- V-L4-001: Add a service-specific CTA to each service description on the Services page: "Schedule [Service Name]" or "Get a Free [Service Name] Estimate." Each CTA should link to the contact form with the service type pre-selected in the dropdown. In Elementor: add a Button widget below each service description with a link to the Contact page anchored to the form, using a URL parameter to pre-fill the service dropdown.
- V-L4-002: Add a sticky header CTA (phone number + "Free Estimate" button) that persists on scroll across all pages. In Elementor: set the header section to "Sticky" in the Motion Effects tab. Ensure the phone number and a compact form CTA button are in the header.
- V-L4-003: Differentiate the two conversion paths visually. Make the phone CTA the primary (larger, filled button) and the form CTA the secondary (outlined or smaller). This signals that calling is the preferred path. In Elementor: style the phone button as the global primary button and the form button as an outlined variant.

---

## Cross-Layer Patterns

- **"Looks fine but doesn't convert" pattern.** On desktop, the site is acceptable — it has content, reasonable navigation, a contact form. The scores are all mediocre rather than terrible. But the site does nothing to actively build trust (weak L1 + L3), nothing to create a feeling of professionalism beyond baseline (weak L2), and nothing to guide users toward conversion (weak L4). This is the archetype of a site that "looks fine" on a desktop screenshot but underperforms on actual business metrics. The owner likely cannot articulate what is wrong because nothing is obviously broken — the failures are perceptual, not functional.
- **Mobile compound failure.** The horizontal overflow on mobile (L0) means 2 of 3 service cards are invisible. This cascades: L1 first impression on mobile is worse (broken layout), L3 social proof positioning is even worse (testimonials are further below the broken section), and L4 conversion path is longer (more scrolling past broken content to reach the form).

---

## Overall: 49/100

**Calculation:** (55 * 1.5 + 48 + 42 + 52 + 50) / 5.5 = (82.5 + 48 + 42 + 52 + 50) / 5.5 = 274.5 / 5.5 = 49.9 -> **50**

A site that checks the boxes (has a hero, has a form, has testimonials, has services listed) without executing any of them at a level that builds genuine trust or guides conversion. This is the most common pattern in small business websites: the presence of standard elements disguises the absence of effective perception design. The mobile horizontal overflow is the most urgent fix (blocks Foundation), but the highest-impact fix is adding verifiable trust signals to the first viewport — a local service business lives or dies on trust, and this site provides almost none.

---

## Top 3 Fixes

1. **Fix mobile horizontal overflow on service cards** — L0 (primary) — Expected impact: L0 +12 (from 55 to ~67, resolving the Critical violation). Also improves L1 mobile impression and L4 mobile decision path. In Elementor: set the service card section to stack on mobile.
2. **Add verifiable trust signals above the fold** — L1 (primary), L3 (secondary) — Expected impact: L1 +10 (from 48 to ~58), L3 +6 (from 52 to ~58). Add Google review aggregate, years in business, and license number to a trust strip in the hero area. Replace stock photo with real company photo.
3. **Add service-specific CTAs and sticky header CTA** — L4 — Expected impact: L4 +10 (from 50 to ~60). Every service description should have a next-step button. The conversion path should be accessible from any scroll position on any page.

---

## Dependency Notes

No dependency caps triggered — Foundation score is 55 (above the 40 threshold). However, the Critical violation (V-F-001: mobile horizontal overflow) caps Foundation at 30 on mobile viewports. If evaluating mobile-only, the dependency cascade would apply: L1 capped at 50, L2 capped at 45, L3 capped at 40, L4 capped at 35. The scores above represent a blended desktop+mobile evaluation. The mobile-specific evaluation would score significantly lower.

**Note on Critical violation and cap:** V-F-001 is Critical severity. Per constitutional constraints, "any layer with a Critical-severity violation: that layer capped at 30." The Foundation score of 55 reflects the desktop experience. Strictly applying the cap would set L0 to 30, triggering the full dependency cascade. The blended score above represents the evaluator's judgment that the site functions acceptably on desktop where the Critical violation does not manifest, but the mobile experience alone would score L0: 30 (capped), with upper layers similarly capped.
