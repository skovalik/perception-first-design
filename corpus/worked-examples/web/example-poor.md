# PFD Evaluation — [Site D — Restaurant with Online Ordering]

**Site type:** Independent restaurant with online ordering. Dine-in, takeout, and delivery. Menu-driven site with ordering integration via third-party platform (embedded iframe).
**Framework:** WordPress classic theme (no page builder detected)
**Detection confidence:** 78 — `<meta name="generator" content="WordPress 5.8.9">`, `wp-content/themes/flavor-starter/` in stylesheet path, `wp-emoji-release.min.js` loaded, standard WordPress body classes present. No page builder classes detected. No theme.json CSS variables. Theme appears to be a classic starter theme with minimal customizer options, heavily customized via Additional CSS. The WordPress version (5.8.9) is 2+ years behind current, suggesting the site is not actively maintained.

---

## Foundation (L0): 32/100 — fail

**Reasoning:** The site has fundamental structural problems. The homepage attempts to present: a hero image, a "Welcome" text block, the full dinner menu (85+ items in a single scrolling list with no categories, tabs, or accordions), a photo gallery (12 images), a Google Maps embed, hours of operation, and a contact form. Total page length exceeds 8,000 words of content. No progressive disclosure is used — the entire dinner menu is rendered as a single `<ul>` with no category groupings, no tabs, no search. Interactive element count on the homepage exceeds 120 (85 menu items as clickable links to individual item pages, 12 gallery images, navigation links, form fields, social media icons, and the ordering iframe). The site has a responsive viewport meta tag, but the layout breaks at 768px — the two-column layout (menu + sidebar) collapses into a single column where the sidebar content (hours, address, phone) falls below the 8,000-word menu, becoming effectively unreachable. The online ordering iframe (from a third-party platform) loads a full secondary site within the page, adding another ~30 interactive elements. Four font families are in use: a script font for the restaurant name, a serif for headings, a sans-serif for body text, and whatever the ordering iframe renders.

**Violations:**
- **[Critical]** V-F-001: The full dinner menu (85+ items) is rendered as a single unsectioned list on the homepage with no progressive disclosure — no categories, no tabs, no accordion, no search. A user looking for desserts must scroll past appetizers, salads, soups, entrees, sandwiches, sides, and beverages. — *Sweller 1988 (cognitive load theory): 85+ items in an unsectioned list maximize extraneous cognitive load. The user must maintain a mental model of position, progress, and relevance across 8,000+ words of menu content without any external scaffolding. This is a textbook extraneous load violation — the complexity is imposed by the presentation, not the task.*
- **[Critical]** V-F-002: Interactive element count exceeds 120 on a single view. The menu items alone contribute 85+ clickable links. Combined with navigation, gallery, form, social icons, and the embedded ordering iframe, the page far exceeds the 50-element threshold. — *Cowan 2010: with working memory holding 3-5 chunks, 120+ interactive elements are impossible to evaluate. Users cannot scan or satisfice — they must abandon systematic evaluation and resort to keyword search (if available) or random sampling. The element count is in the "absent" category of the rubric.*
- **[Major]** V-F-003: On mobile (768px and below), the sidebar (containing hours, address, and phone number) collapses below the 8,000-word menu. Users on mobile must scroll past the entire menu to find the restaurant's hours or phone number. — *Hick 1952: the mobile layout converts the sidebar's 3 critical information items (hours, address, phone) from immediately accessible to "hidden behind 8,000 words of content." The effective choice cost of reaching this information becomes prohibitive.*
- **[Minor]** V-F-004: Four font families: script (restaurant name/logo), serif (headings), sans-serif (body), plus the ordering iframe's font. Exceeds the 3-family threshold. — *Practitioner observation: 4 fonts is above the recommended 2-3, but the script font for the logo/brand name is a common and generally acceptable exception in restaurant sites. The iframe font is the uncontrolled injection.*

**Strengths:**
- The viewport meta tag is present — the site attempts responsive design, even if it fails at key breakpoints
- Navigation is limited to 5 items (Home, Menu, Order Online, Gallery, Contact) — appropriate for the site's scope
- The phone number is in the header and is clickable on mobile

**Fixes:**
- V-F-001: Restructure the menu using WordPress categories or custom post types. Group items into 8-10 categories (Appetizers, Salads, Entrees, etc.) and present them as tabbed sections or an accordion. Each category should expand to show only its items. If using Additional CSS + HTML: implement a simple tab interface. If considering a rebuild: use a WordPress menu plugin (e.g., Food Menu, Restaurant Menu) that provides built-in categorization.
- V-F-002: The element count fix follows from the menu restructuring — collapsing 85 items behind category tabs reduces the visible interactive elements from 120+ to approximately 35-40 (navigation + 8 category tabs + visible items in the active tab + gallery + form).
- V-F-003: On mobile, move the sidebar content (hours, address, phone) to a position above or immediately below the hero section, before the menu begins. In WordPress: restructure the template to output the sidebar widgets in a different position on mobile, or duplicate the critical information (hours, address) in a mobile-only block above the menu.

---

## Layer 1 — First Impression: 28/100 — critical

**Reasoning:** The hero is a low-resolution food image (visible pixelation at full-width, suggesting the original image was ~600px wide stretched to fill a 1440px container). Overlaid text ("Welcome to [Restaurant Name]") uses a cursive/script font with thin strokes on a busy food image background — contrast is poor and the text is difficult to read. No CTA is visible above the fold on desktop. The "Order Online" link is in the top navigation but is not visually emphasized. Below the fold, the immediate visual is a wall of menu text — no section images, no color breaks, no visual hierarchy between categories (because there are no categories). Trust signals are absent from the first viewport: no review ratings, no "family owned since [year]" messaging, no health department rating, no awards. The overall visual impression is dated — the design aesthetic reads as circa 2014-2016.

**Violations:**
- **[Critical]** V-L1-001: Hero image is low-resolution with visible pixelation when displayed full-width. The image quality signals "low effort" or "abandoned site" at the 50ms gate. For a restaurant — where food photography is the primary trust signal — a pixelated food image is actively damaging. — *Lindgaard 2006: the 50ms first impression processes image quality before any text. A pixelated hero image signals low quality to the perceptual system before the user can consciously evaluate the restaurant's offering. This triggers the negative halo of the aesthetic-usability effect (Kurosu & Kashimura 1995), coloring all subsequent evaluation negatively.*
- **[Major]** V-L1-002: No CTA visible above the fold. The "Order Online" action exists only as a navigation link (same size, weight, and color as other nav items). On a restaurant site, the primary conversion action (order food) should be the most prominent element in the first viewport. — *Fogg 2003 (Prominence-Interpretation Theory): a conversion path that has no prominence cannot influence the user's credibility or action assessment. "Order Online" as a standard nav link registers as a navigation option, not a primary action path.*
- **[Major]** V-L1-003: Hero text (script font, thin strokes) on a busy food photo background creates a contrast failure. The text is difficult to read even at leisure, let alone in the 50ms evaluation window where only high-contrast elements register. — *Lindgaard 2006: at 50ms, users process layout and color, not detailed text. Hero text that lacks contrast against its background simply does not register — the user sees an image with unreadable overlay, which communicates nothing about the restaurant's proposition.*
- **[Minor]** V-L1-004: Zero trust signals in the first viewport. No review rating, no "years in business" claim, no awards, no health inspection score. — *Fogg 2003: trust signals must be prominent to register. Their complete absence means the L1 credibility assessment is based entirely on visual quality (which is poor) and image quality (which is pixelated).*

**Strengths:**
- The restaurant name is readable in the header (separate from the hero text issue)
- The script font choice for the brand name is appropriate for the restaurant category — it communicates "dining" rather than "tech startup"

**Fixes:**
- V-L1-001: Replace the hero image with a high-resolution photo (minimum 1920px wide for full-bleed). If professional photography is not available, even a well-lit smartphone photo of the restaurant's best dish or dining room, taken in good light, will outperform the current pixelated stock image.
- V-L1-002: Add a prominent "Order Now" CTA button in the hero area. Style it distinctly from navigation: larger, filled background, high-contrast accent color. Position it directly below or beside the hero headline.
- V-L1-003: Add a semi-transparent dark overlay to the hero image (50-70% opacity) to create text contrast, or switch to a light text color on a dark-background image. Alternatively, place the text on a solid or semi-transparent background panel rather than directly on the image.
- V-L1-004: Add a trust strip below the header: Google review rating, years in business, and any awards or press mentions.

---

## Layer 2 — Processing Fluency: 25/100 — critical

**Reasoning:** No coherent design system is detectable. The site is styled via a combination of the starter theme's minimal CSS and approximately 200 lines of Additional CSS (via Appearance > Customize > Additional CSS) that overrides elements inconsistently. Colors appear in at least 7 distinct families: a dark maroon (#5C0000), a gold/amber (#D4A017), black (#000), white (#FFF), a medium gray (#777), a light gray (#F5F5F5), and the ordering iframe introduces its own blue-and-white color scheme. Heading sizes vary from 42px to 18px with no detectable typographic scale — sizes appear chosen per-element rather than from a system. Spacing between sections varies from 20px to 80px with no rhythm. The ordering iframe introduces a complete second visual language (different fonts, colors, button styles, layout grid) that coexists with the restaurant site's visual language with no attempt at integration.

**Violations:**
- **[Critical]** V-L2-001: The embedded ordering iframe renders a complete second design system within the page. The iframe has its own font stack (Helvetica), color scheme (blue primary, gray secondary), button style (rounded, blue fill), and spacing system that share nothing with the restaurant site's visual language. The user transitions from one visual language to another without warning or transition. — *Alter & Oppenheimer 2009: fluency effects are strongest when unconscious. The abrupt visual language switch forces the perceptual system to build a new decoding schema mid-page. This is the highest-cost fluency violation — not inconsistency within a system, but the collision of two unrelated systems.*
- **[Major]** V-L2-002: Seven distinct color families with no systematic relationship. The maroon, gold, black, white, gray, light gray, and iframe-blue colors are not derived from a palette — they are individual choices made at different times with no unifying logic. — *Reber & Schwarz 1999: visual information that is easy to process feels more true. An unsystematic color palette creates processing difficulty at every color transition. Users feel less trust without knowing why — the color chaos operates below conscious awareness.*
- **[Major]** V-L2-003: Heading sizes (42px, 36px, 28px, 24px, 18px) do not follow a consistent typographic scale. The sizes appear arbitrary rather than derived from a mathematical relationship (no modular scale, no Tailwind-style step system, no systematic progression). — *Wertheimer 1923 (Gestalt principles): heading hierarchy communicates content structure through size similarity grouping. When heading sizes are arbitrary, the perceptual system cannot build a reliable hierarchy model — a 28px heading and a 24px heading create ambiguity about their relative importance.*

**Strengths:**
- Body text is consistently styled: the same sans-serif font at 16px with ~1.5 line height is used across all paragraph content
- The starter theme's baseline CSS provides consistent link styling (maroon colored, underlined) throughout the main content area

**Fixes:**
- V-L2-001: If the ordering platform allows CSS customization, override its styles to match the restaurant site's colors and fonts. If not, consider switching to an ordering platform that supports white-label styling (e.g., ChowNow, Toast, Square Online all offer customizable embeds). At minimum, add a visual transition (a heading "Order Online" with matching restaurant styling) above the iframe to prepare the user for the context switch.
- V-L2-002: Establish a 4-color palette: background (#FFF or #F5F5F5), text (#000 or #333), primary accent (maroon #5C0000), secondary accent (gold #D4A017). Remove all other colors. Apply consistently via the theme customizer or Additional CSS.
- V-L2-003: Establish a heading scale. For a restaurant site using a serif heading font: H1: 42px, H2: 32px, H3: 24px, H4: 20px. Apply via Additional CSS: `h1 { font-size: 42px; } h2 { font-size: 32px; }` etc.

---

## Layer 3 — Perception Bias: 35/100 — fail

**Reasoning:** Social proof is almost entirely absent. No review ratings from any platform are displayed on the site. No testimonials, no customer photos, no "featured in" badges. The only social proof element is a Facebook widget in the sidebar showing the restaurant's Facebook page follower count and recent posts — but on mobile, this widget falls below the 8,000-word menu and is effectively invisible. The "About" content mentions the restaurant has been family-owned since 1998, which is a genuine authority and liking signal, but it is buried in a separate page rather than featured prominently. The ordering platform iframe introduces its own framing and messaging ("Delivery fee: $3.99, Minimum order: $15") with no preparation or context from the restaurant site — the user encounters fees and minimums as a surprise rather than a framed expectation. No urgency mechanics are present, which is appropriate.

**Violations:**
- **[Major]** V-L3-001: Zero social proof on the homepage or any page where the user makes a decision (menu viewing, ordering). No Google reviews, no Yelp rating, no testimonials, no customer photos. For a restaurant — an industry where review ratings are a primary decision factor — this is a significant omission. — *Cialdini 2001 (social proof): restaurants are high-uncertainty decisions (will the food be good? is it safe? is it worth the price?). Social proof is the primary uncertainty reducer for restaurants. Its complete absence forces the user to make the decision based solely on the menu and food photos (which are low-quality). The user's System 1 has no heuristic to latch onto.*
- **[Major]** V-L3-002: Delivery fees and order minimums appear as a surprise inside the ordering iframe. The restaurant site makes no mention of delivery fees, minimum order amounts, or delivery radius before the user enters the ordering flow. This creates an expectation mismatch — the user expects to order, encounters unexpected costs, and may abandon. — *Kahneman & Tversky 1979 (prospect theory): unexpected costs are processed as losses relative to the expected reference point (free/no-minimum ordering). Even if the $3.99 fee is reasonable, its unexpected appearance at the commitment point triggers loss aversion disproportionate to the actual cost. Framing the fee earlier ("Delivery from $3.99") sets the reference point before the decision.*
- **[Minor]** V-L3-003: The "family-owned since 1998" claim is buried on the About page. This is a genuine authority and liking signal that should be prominent on the homepage. — *Cialdini 2001 (liking + authority): "family-owned since 1998" triggers both the liking principle (personal, relatable, not a chain) and authority through longevity (28 years of operation signals stability). Burying this on a secondary page wastes its persuasive potential.*

**Strengths:**
- No fake urgency — appropriate for a restaurant context
- The "family-owned since 1998" claim, while poorly placed, is a genuine and verifiable trust signal
- Menu prices are clearly displayed with no hidden fees on the restaurant site itself (the iframe fees are the third-party platform's issue)

**Fixes:**
- V-L3-001: Add a Google review badge prominently in the header or hero area. If the restaurant has a Google Business Profile (most do), display the aggregate rating and review count. Use a widget, a screenshot, or a manually created badge that links to the Google profile.
- V-L3-002: Add a brief delivery information note above the ordering iframe: "Delivery available within [X] miles. Delivery fee: $3.99. Minimum order: $15." This sets the reference point before the user encounters the fees, converting a "surprise loss" into an expected cost.
- V-L3-003: Move the "Family-owned since 1998" claim to the homepage — either in the hero area or immediately below it. Consider adding a family photo to humanize the claim.

---

## Layer 4 — Decision Architecture: 30/100 — fail

**Reasoning:** The decision path is unclear. The site presents three possible actions — dine in (implied, no CTA), order online (navigation link, no emphasis), or call (phone number in header, reasonably placed). The "Order Online" path leads to the ordering iframe embedded on a dedicated page, which is functional but visually disconnected from the restaurant site. Within the ordering iframe, the user must re-browse the menu (the iframe has its own menu, not linked to the menu displayed on the homepage). This means the user views the menu twice: once on the homepage (text-only, 85 items unsectioned) and once in the ordering iframe (different format, different categorization, different prices). Menu items on the homepage link to individual item detail pages that have no "Add to Cart" or "Order This" functionality — they are dead ends. The contact form exists on the Contact page but is generic (no "Make a Reservation" framing or service-specific fields).

**Violations:**
- **[Critical]** V-L4-001: Menu items on the homepage link to individual item pages that have no ordering or action path. Each item page shows a description, a price, and sometimes a photo — but no "Order This Item," no "Add to Cart," no link to the ordering platform with this item pre-selected. The user clicks a menu item expecting to take action but reaches a dead end. — *Pirolli & Card 1999 (information foraging): the menu item link creates strong information scent ("click to see more about this item"). The item page satisfies the information need but eliminates the action scent. The user's foraging path terminates without a next step. This is a scent dead end — the most damaging L4 pattern.*
- **[Major]** V-L4-002: The user must browse the menu twice — once on the homepage (text list) and once in the ordering iframe (different format, different organization). The two menu presentations are not linked. A user who spent 3 minutes finding a dish on the homepage menu must find it again in the ordering iframe. — *Sweller 1988 (extraneous load): requiring the user to locate the same information twice in two different systems imposes pure extraneous cognitive load. The redundant search is imposed by poor design, not inherent task complexity.*
- **[Minor]** V-L4-003: The Contact page form is generic (name, email, message) with no reservation-specific fields (date, time, party size, occasion). A restaurant's contact form should support the primary non-ordering action: making a reservation. — *Thaler & Sunstein 2008: the contact form's structure does not match the user's likely intent. A user reaching the Contact page of a restaurant most likely wants to make a reservation, not send a generic message. The form's fields do not create a decision path aligned with the probable user goal.*

**Strengths:**
- The phone number in the header is clickable and prominent — for users who call to order (common for restaurants), this works
- The "Order Online" navigation item, while not emphasized, is correctly labeled and links to the ordering page
- The ordering iframe itself (once reached) is functional — the third-party platform handles the cart, payment, and checkout competently

**Fixes:**
- V-L4-001: Either (a) add an "Order This Item" button on each individual menu item page that deep-links to that item in the ordering platform, or (b) remove the individual item pages entirely and keep the menu as a browse-only reference that feeds into the ordering flow. Option (b) is simpler: replace individual item links with a prominent "Ready to Order?" CTA at the end of each menu category section that links to the ordering page.
- V-L4-002: Consolidate to a single menu experience. Either use the ordering platform's menu as the only menu (embed it more prominently and remove the duplicate homepage menu) or integrate the homepage menu with direct ordering links per item.
- V-L4-003: Add reservation-specific fields to the contact form: Date, Time, Party Size, and an optional Special Occasions/Requests field. Rename the page from "Contact" to "Reservations & Contact." Consider adding an OpenTable or Resy integration if the restaurant uses a reservation platform.

---

## Cross-Layer Patterns

- **Double-menu problem is a 3-layer failure (L0 + L2 + L4).** The unsectioned 85-item homepage menu is an L0 cognitive load violation. Its visual disconnect from the ordering iframe's menu is an L2 fluency violation. The requirement to browse the menu twice is an L4 decision architecture violation. Fixing this single issue (consolidate to one menu) would improve three layers simultaneously.
- **Dead-end item pages create a L1 + L4 compound failure.** Users who click a menu item expecting to see appetizing food photos and an ordering path (L1 expectation) instead reach a text-only page with no action (L4 dead end). The expectation mismatch damages both the impression of the site and the conversion funnel.

---

## Overall: 30/100

**Calculation:** (32 * 1.5 + 28 + 25 + 35 + 30) / 5.5 = (48 + 28 + 25 + 35 + 30) / 5.5 = 166 / 5.5 = 30.2 -> **30**

A restaurant website with structural problems that prevent it from functioning as a conversion tool. The site has content (a full menu, photos, business information) but no system for organizing, presenting, or acting on that content. The double-menu problem is the most damaging single issue — it wastes user effort, fragments the experience, and disconnects browsing from ordering. The low-resolution hero image and absent trust signals mean even users who persist past the structural problems receive no trust signals to encourage commitment. The site needs a fundamental restructuring around a single, categorized, order-ready menu experience, not incremental fixes.

---

## Top 3 Fixes

1. **Consolidate to a single, categorized menu with ordering** — L0 + L2 + L4 — Expected impact: L0 +20 (from 32 to ~52, resolving the Critical violations), L2 +8 (removes the dual-system fluency break), L4 +15 (from 30 to ~45, creating a functional decision path). This is the single highest-impact change: replace the 85-item unsectioned list and the disconnected iframe with a single categorized menu where items link directly to ordering.
2. **Replace hero image and add trust signals** — L1 — Expected impact: L1 +18 (from 28 to ~46, resolving the Critical violation). A high-resolution real food photo, readable hero text with proper contrast, a visible "Order Now" CTA, and a Google review badge would transform the first impression from "abandoned template" to "functioning restaurant."
3. **Frame delivery fees before the ordering flow** — L3 — Expected impact: L3 +8 (from 35 to ~43). Setting the reference point for fees before the user encounters them converts a "surprise cost" into an expected cost, reducing abandonment at the critical ordering step.

---

## Dependency Notes

**Foundation Critical violations triggered.** Two Critical-severity violations (V-F-001: unsectioned 85-item menu, V-F-002: 120+ interactive elements) are present. Per constitutional constraints, the Foundation layer is capped at 30 due to Critical violations.

Applying the Foundation < 40 dependency cascade:
- L1 cap: 50 (L1 scored 28 — below cap, no effect)
- L2 cap: 45 (L2 scored 25 — below cap, no effect)
- L3 cap: 40 (L3 scored 35 — below cap, no effect)
- L4 cap: 35 (L4 scored 30 — below cap, no effect)

Additionally, L1 has a Critical violation (V-L1-001: pixelated hero image), capping L1 at 30. L1 uncapped score: 28 — below the cap, so the Critical cap does not change the score.

L2 has a Critical violation (V-L2-001: ordering iframe dual design system), capping L2 at 30. L2 uncapped score: 25 — below the cap, so no effect.

In this case, the dependency caps do not alter any scores because the uncapped scores are already below the cap thresholds. This is typical for poor-scoring sites — the caps are designed to catch situations where upper layers are scored too high relative to a broken foundation, but when all layers are genuinely low, the caps are already satisfied.
