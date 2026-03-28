# Shopify Themes — Design System Profile

## Detection Signals

### Core Shopify Indicators
- `cdn.shopify.com` in asset URLs (JS, CSS, images, fonts) — the single most reliable indicator. Assets served from `cdn.shopify.com/s/files/{shop_id}/...` or `cdn.shopify.com/shopifycloud/...`
- `Shopify.theme` JavaScript object in inline `<script>` tags — contains `name`, `id`, `role` (e.g., `"main"` or `"unpublished"`), and `theme_store_id`
- `Shopify.routes` JavaScript object — exposes `/cart`, `/cart/add`, `/search/suggest` endpoint patterns
- `window.shopUrl` set to the store's origin URL
- `<meta name="shopify-checkout-api-token">` in `<head>` — Shopify-specific checkout token
- `<meta name="shopify-digital-wallet">` tags for payment integration metadata
- `.shopify-section` wrapper class on all rendered sections — Shopify wraps every section in `<div class="shopify-section shopify-section--{section-type}" id="shopify-section-{id}">`
- `shopify-block` data attributes on block-level elements within sections
- URL path patterns: `/collections/`, `/collections/{handle}`, `/products/{handle}`, `/cart`, `/pages/{handle}`, `/blogs/{blog}/`, `/account/login`
- `myshopify.com` appearing in canonical URLs, `<link>` tags, or detectable via subdomain (even when custom domain is primary, the `.myshopify.com` domain often appears in source comments or API calls)
- `Shopify.designMode` — boolean present when the Theme Editor is active (edge case, but appears in source)
- `<link rel="preconnect" href="https://cdn.shopify.com">` in `<head>` — near-universal on Shopify stores
- `/cart.js`, `/cart/add.js`, `/products/{handle}.js` AJAX API endpoints — Shopify-specific storefront API patterns
- `shopify-payment-terms` custom element or `shopify-accelerated-checkout` in checkout-related markup

### Theme Detection

| Theme | Developer | Detection Signals | Architecture | Notes |
|-------|-----------|-------------------|-------------|-------|
| **Dawn** | Shopify (free) | CSS vars `--color-foreground`, `--color-background`, `--font-body-family`, `--font-heading-family`, `--page-width`, `--buttons-radius`, `--inputs-radius`; BEM-inspired classes `.card--*`, `.button--*`; files `base.css`, `section-*.css` loaded individually per section | OS 2.0, JSON templates, section groups | Default free theme since OS 2.0 launch. Reference architecture for all modern Shopify themes. Most forks inherit its CSS variable namespace. |
| **Refresh** | Shopify (free) | Dawn-derived CSS variable namespace; similar section structure; distinct visual treatment (bolder typography, more color variation) | OS 2.0 | Free theme, Dawn descendant. |
| **Sense** | Shopify (free) | Dawn-derived variables; organic/rounded visual language; `rounded` border-radius values more prominent; soft shadow usage | OS 2.0 | Wellness/lifestyle positioning. Rounded elements, warm palette defaults. |
| **Ride** | Shopify (free) | Dawn-derived variables; sport/outdoor visual language; bold heading scale; high-contrast color defaults | OS 2.0 | Active/outdoor positioning. |
| **Debut** | Shopify (legacy) | `.template-*` body classes (e.g., `.template-index`, `.template-product`); no CSS custom properties; jQuery dependency (`jquery.min.js` loaded); Sass-compiled `theme.scss.css`; `.site-header`, `.site-footer` class patterns | Vintage (pre-OS 2.0), `.liquid` templates | Pre-OS 2.0 legacy. No JSON templates. Section support limited to homepage. Still active on ~15-20% of stores. |
| **Brooklyn** | Shopify (legacy) | Similar to Debut detection; `.site-header--*` modifier classes; hero slideshow patterns; jQuery dependent | Vintage | Legacy free theme. Edge-to-edge slideshow hero, dynamic product grid. |
| **Supply** | Shopify (legacy) | `.template-*` classes; sidebar-heavy layout; `.site-nav--*` classes; jQuery dependent | Vintage | Legacy theme. Sidebar navigation, collection-focused. |
| **Prestige** | Maestrooo (premium) | Single `theme.css` file (not split per-section); CSS variables defined at section level in `snippets/css-variables.liquid`; no CSS framework; `theme.js` + `vendor.min.js` in assets; premium typography (often serif headings) | OS 2.0 (v7+), Vintage (v6-) | Fashion/luxury focus. Maestrooo handcrafts all CSS (no framework). v7+ is OS 2.0 native. |
| **Impact** | Maestrooo (premium) | Same Maestrooo architecture as Prestige; single `theme.css`; bold typography defaults; full-width section patterns; `vendor.min.js` + `theme.js` | OS 2.0 (v6+) | High-energy/bold brands. Shares Maestrooo architecture with Prestige and Stretch. 35+ configurable sections. |
| **Impulse** | Archetype Themes (premium) | `.impulse-*` class patterns possible; Archetype-specific JS patterns; product quickview modals; advanced filtering UI | OS 2.0 | Feature-rich premium theme. Common on high-volume stores. |
| **Custom / Headless** | Agency-built | No theme-store theme indicators; may still use `cdn.shopify.com` for product images; Hydrogen/Remix patterns (React, `@shopify/hydrogen` imports); or fully custom Liquid with proprietary class naming | Varies | Agency builds. Detect via Shopify CDN + absence of known theme patterns. Hydrogen stores use Shopify Storefront API but render client-side. |

### Shopify App Artifacts

Common Shopify apps inject their own CSS/JS that can conflict with theme design systems. Detecting these helps explain visual inconsistencies.

| App | CSS Indicators | JS/HTML Indicators | PFD Impact |
|-----|---------------|-------------------|------------|
| **Klarna** (BNPL messaging) | `.klarna-message-info`, `.klarna-message-info2`, `klarna-placement` elements | `<klarna-placement>` custom element, `klarna.com` script sources | Payment messaging widget — can break visual rhythm if unstyled |
| **Judge.me** (reviews) | `.jdgm-widget`, `.jdgm-review-widget`, `.jdgm-preview-badge`, `.jdgm-prev-badge__stars`, `.jdgm-star`, `#judgeme_product_reviews` | Judge.me script tags, `.jdgm--done-setup` state class | Review stars and widget inject own font/color — common L2 violation source |
| **Stamped.io** (reviews) | `.stamped-*` classes, `#stamped-main-widget` | `stamped.io` script sources | Similar to Judge.me — injected review styling |
| **Loox** (photo reviews) | `.loox-*` classes, `.loox-rating` | `loox.io` script sources | Photo grid widget — layout disruption risk on mobile |
| **Recharge** (subscriptions) | `.rc-container`, `.rc-widget`, `.rc-template`, `.rc-template__legacy-radio`, `.rca-subscription`; bundles use `.rb-*` prefix | Recharge script tags, subscription option radio buttons on product pages | Subscription toggle widget — often visually mismatched with theme buttons/inputs |
| **Klaviyo** (email/SMS) | `.klaviyo-*` classes, `#klaviyo-product-reviews-wrapper` (if using Klaviyo Reviews); popup forms with z-index ~90000 | `static.klaviyo.com` script sources, `<div class="klaviyo-form-*">` | Popup forms and embedded signup — z-index conflicts, font mismatch, mobile overlay issues |
| **Shopify Product Reviews** (native, deprecated) | `.spr-*` classes, `#shopify-product-reviews` | `shopify-product-reviews` script | Legacy — being replaced by Judge.me/Klaviyo Reviews but still widespread |
| **Yotpo** (reviews + UGC) | `.yotpo`, `.yotpo-*` classes, `.yotpo-bottomline` | `staticw2.yotpo.com` script sources | Heavy widget injection — star ratings, Q&A, photo galleries |
| **Bold Subscriptions** | `.bold-*` classes, `.bold-ro__*` (recurring orders) | Bold Commerce script sources | Subscription UI on product pages |
| **AfterShip / Track123** (tracking) | `.aftership-*` classes | Tracking page widget injection | Tracking pages — usually isolated to `/pages/track` |
| **Shogun Page Builder** | `.shg-*` classes, Shogun-specific section wrappers | `lib.getshogun.com` scripts | Creates a parallel design system — like Elementor on WordPress. Evaluate Shogun's system, not the theme's, on Shogun-built pages. |

---

## Token System

### Dawn and OS 2.0+ Themes

Dawn defines its entire design token system as CSS custom properties, generated from Liquid `{{ settings.* }}` values in `theme.liquid`. These tokens are the authoritative design system for any Dawn-based or Dawn-forked theme.

**Color Tokens** (defined per color scheme, iterated via `{% for scheme in settings.color_schemes %}`):
- `--color-foreground` — primary text color (RGB triplet)
- `--color-background` — page/section background (RGB triplet)
- `--gradient-background` — background gradient or solid fallback
- `--color-background-contrast` — calculated from background brightness for contrast
- `--color-shadow` — shadow color (RGB triplet)
- `--color-button` — primary button fill (RGB triplet)
- `--color-button-text` — primary button label (RGB triplet)
- `--color-secondary-button` — secondary/outline button fill
- `--color-secondary-button-text` — secondary button label
- `--color-link` — link color
- `--color-badge-foreground`, `--color-badge-background`, `--color-badge-border` — badge system

**Typography Tokens:**
- `--font-body-family` — body typeface (family + fallback)
- `--font-body-style` — italic/normal
- `--font-body-weight` — base weight
- `--font-body-weight-bold` — bold weight (base + 300, capped at 1000)
- `--font-body-scale` — body size multiplier (from `settings.body_scale`)
- `--font-heading-family` — heading typeface
- `--font-heading-style` — heading italic/normal
- `--font-heading-weight` — heading weight
- `--font-heading-scale` — heading size multiplier (relative to body scale)

**Layout + Spacing Tokens:**
- `--page-width` — max content width (default 1600px range, converted to rem)
- `--page-width-margin` — gutter margin (`2rem` or `0rem`)
- `--spacing-sections-desktop` — vertical space between sections
- `--spacing-sections-mobile` — mobile section spacing (scaled down)
- `--grid-desktop-vertical-spacing`, `--grid-desktop-horizontal-spacing` — grid gaps
- `--grid-mobile-vertical-spacing`, `--grid-mobile-horizontal-spacing` — mobile grid gaps (typically half desktop)

**Component Shape Tokens:**
- `--buttons-radius` — button corner radius
- `--buttons-border-width`, `--buttons-border-opacity` — button border
- `--buttons-shadow-*` — button shadow (opacity, offsets, blur)
- `--inputs-radius` — form input corner radius
- `--inputs-border-width`, `--inputs-border-opacity` — input border
- `--inputs-shadow-*` — input shadow system
- `--variant-pills-radius` — product variant selector radius
- `--variant-pills-border-width`, `--variant-pills-border-opacity`
- `--media-radius`, `--media-padding`, `--media-border-width` — image/media containers
- `--badge-corner-radius` — badge rounding
- `--text-boxes-radius`, `--text-boxes-border-width` — text container rounding

**Card Tokens** (product, collection, blog cards each have parallel systems):
- `--product-card-image-padding`, `--product-card-corner-radius`, `--product-card-text-alignment`
- `--product-card-border-width`, `--product-card-border-opacity`
- `--product-card-shadow-*` (opacity, offsets, blur, visible toggle)
- `--collection-card-*` — same pattern for collection cards
- `--blog-card-*` — same pattern for blog article cards

**Popup + Drawer Tokens:**
- `--popup-border-width`, `--popup-corner-radius`, `--popup-shadow-*`
- `--drawer-border-width`, `--drawer-border-opacity`, `--drawer-shadow-*`

**Animation Tokens** (defined in `base.css`):
- `--duration-short` through `--duration-extended` — timing scale
- `--ease-out-slow` — easing curve
- `--animation-slide-in`, `--animation-fade-in` — keyframe references

**CSS Architecture Notes:**
- Dawn uses per-section CSS files (`section-*.css`) loaded only when that section is rendered — aggressive code splitting
- `base.css` contains resets, typography baseline, grid system, utilities, and animation definitions
- BEM-inspired class naming: `.card--standard`, `.button--primary`, `.button--secondary`
- Layout utilities: `.page-width`, `.grid`, `.grid--1-col` through `.grid--6-col`
- Visibility utilities: `.small-hide`, `.medium-hide`, `.large-up-hide`
- Responsive breakpoints: 750px (tablet), 990px (desktop)
- Focus system: `--focused-base-outline`, `--focused-base-outline-offset`, `--focused-base-box-shadow`

### Legacy Themes (Debut, Supply, Brooklyn)

Legacy ("vintage") Shopify themes use a fundamentally different token architecture:

- **No CSS custom properties** — Sass variables compiled to static CSS at theme upload time
- **Liquid-injected inline styles** — `{{ settings.color_primary }}` outputs hex values directly into `<style>` blocks in `theme.liquid`
- **Common Sass variable patterns** (pre-compiled, not inspectable at runtime):
  - `$color-primary`, `$color-secondary`, `$color-body-text`, `$color-bg`
  - `$font-stack-header`, `$font-stack-body`
  - `$width-site` (max content width)
- **Settings via `settings_schema.json`** — defines what appears in Theme Editor; values stored in `settings_data.json`
- **Detection of legacy tokens:** Look for inline `<style>` blocks in `<head>` containing hardcoded color/font values (not CSS custom property declarations). This is the primary distinction from OS 2.0 themes.
- **jQuery dependency** — legacy themes load `jquery.min.js`; OS 2.0 themes (Dawn) are jQuery-free, using native web components and vanilla JS

### Section-Based Architecture (OS 2.0)

Shopify OS 2.0 introduced JSON templates that define page layouts as ordered lists of sections:

- **JSON templates** replace `.liquid` template files — found at `templates/*.json`
- Each JSON template can render up to **25 sections**, each with up to **50 blocks**
- **Section groups** (`header-group`, `footer-group`) allow merchants to customize layout-level regions (header, footer, overlays)
- **Section-level CSS overrides** — sections can define their own CSS variables via inline `<style>` tags generated from section schema settings. This is the primary mechanism for per-section color schemes in Dawn.
- **PFD L2 implication:** Section-level color overrides are a design feature, not inherently a violation. They become violations when they create jarring transitions between adjacent sections with no design rationale (e.g., alternating warm/cool backgrounds with no visual logic).
- **Section rendering markup:** `<div class="shopify-section shopify-section--{type}" id="shopify-section-{template-id}">` wraps every section. The `{type}` class reveals the section template name.

---

## Visual Language Patterns

### Dawn-Based Themes (Majority of Modern Shopify Stores)
- **Clean, minimal aesthetic** — generous whitespace, restrained use of color, low visual noise
- **System fonts or Google Fonts** — Dawn defaults to system font stack; merchants commonly switch to 1-2 Google Fonts
- **Conservative design tendency** — Shopify themes are designed for broad merchant compatibility, not cutting-edge design. This means safe typographic hierarchies, predictable layouts, and conventional e-commerce patterns.
- **Card-based product presentation** — product grid uses consistent card components with configurable image padding, border radius, and shadow
- **Color scheme system** — Dawn supports multiple named color schemes (Scheme 1, Scheme 2, etc.) applied per-section. The norm is 2-3 schemes: a primary, an inverted/dark, and an accent.

### Standardized Page Layouts
- **Product pages:** Image gallery (left/top) + product details (right/bottom). Gallery is swipeable on mobile. Variant selectors, Add to Cart, and payment buttons follow a consistent vertical stack.
- **Collection pages:** Grid of product cards (2-4 columns desktop, 1-2 mobile) with filtering sidebar or inline filter bar. Predictable sort/filter patterns.
- **Cart page / Cart drawer:** Line items + quantity adjusters + subtotal + checkout button. Cart drawer (slide-out) is default on Dawn.
- **Homepage:** Modular section stack — hero/slideshow, featured collection, image with text, rich text, newsletter. Order is merchant-configurable.

### Shopify-Controlled Checkout
- The checkout page (`/checkout`) is **not part of the theme** — it is rendered by Shopify's checkout system with limited merchant customization (logo, colors, fonts via Checkout Settings)
- **Evaluate checkout separately** from the theme — it follows Shopify's design system, not the merchant's
- Checkout Extensions (OS 2.0) allow limited UI injection but the core layout is Shopify-controlled
- **PFD implication:** Do not penalize merchants for checkout design decisions they cannot control. Focus evaluation on pre-checkout pages.

### Typography Norms
- Heading + body font pair is the standard (2 font families)
- Dawn's heading scale defaults large (2.5-4x body size) — this is intentional, not a violation
- Body scale defaults to 100% (16px equivalent)
- Line height and letter-spacing are theme-controlled, not merchant-configurable in most cases

### Mobile Patterns
- Dawn and OS 2.0 themes are mobile-first responsive
- Hamburger menu (drawer navigation) is standard
- Product image galleries convert to horizontal swipe
- Grid collapses from 4-col to 2-col to 1-col
- Sticky Add to Cart bar on mobile product pages is common

---

## PFD Evaluation Adjustments

### L2: Token Compliance
- **Check against CSS custom properties** (Dawn/OS 2.0) or inline Liquid styles (legacy). The theme's token system is the source of truth.
- **Section-level overrides:** Dawn's color scheme system allows per-section color application. This is not automatically a violation — it is Shopify's intended design mechanism. Flag as L2 violation only when:
  - Adjacent sections use conflicting color schemes with no visual logic (e.g., warm beige followed by cool blue followed by warm beige again)
  - A section's color scheme creates insufficient contrast between text and background
  - Custom CSS bypasses the color scheme system entirely (inline styles overriding CSS variables)
- **App-injected off-system styles** are a stronger violation signal than section overrides. An app using `font-family: Arial` when the theme uses `--font-heading-family: Playfair Display` is a clear L2 violation.

### L2: Color Consistency
- **Norm for Dawn-based stores:** 2 accent colors + background + text per color scheme, with 2-3 color schemes total. This yields 8-12 distinct intentional color values across the site.
- **Violation signal:** More than 5-6 distinct colors appearing outside the defined color schemes — indicates off-system usage from apps, custom CSS, or inconsistent section settings.
- **Legacy themes:** Typically define 3-5 colors in theme settings. Inconsistency often appears between the theme's configured palette and hardcoded values in custom CSS additions.

### Foundation (L0): Cognitive Load — App Widget Bloat
- Shopify stores commonly run 5-15 apps, many of which inject visible UI: review stars, trust badges, BNPL messaging, cookie consent, chat widgets, loyalty program launchers, upsell popups, countdown timers, spin-to-win wheels, newsletter modals.
- **Distinguish app-injected elements from theme-designed elements.** App elements inflate the interactive element count but are not the merchant's design system failing — they are a curation/management issue.
- **Prescriptions for bloat:** "Consider reducing the number of active apps that inject visible UI elements. Prioritize the 2-3 that demonstrably drive conversions and disable the rest." Not: "Remove 15 interactive elements from your product page."
- **Popup cascade:** Multiple apps competing for modal/popup display (newsletter, chat, cookie consent, exit intent) is a critical Foundation violation. Shopify has no native popup prioritization — apps fight for z-index supremacy.

### L4: Decision Architecture
- **Shopify's checkout is standardized and generally well-optimized** — Shopify invests heavily in checkout conversion. Do not evaluate checkout UX as if the merchant controls it.
- **Focus L4 evaluation on pre-checkout pages** where merchant decisions dominate:
  - **Product page:** Is the Add to Cart button prominent? Are variant selectors clear? Is pricing hierarchy obvious? Is the buy path unobstructed by app widgets?
  - **Collection page:** Is filtering effective? Can users quickly find products? Is the sort mechanism accessible?
  - **Cart page/drawer:** Is the path to checkout clear? Are upsell/cross-sell elements helping or cluttering?
  - **Homepage:** Is the primary CTA (shop now, browse collections) clear? Or is the hero section competing with 5 different action paths?
- **Payment option clarity:** Evaluate whether accelerated checkout options (Shop Pay, Apple Pay, Google Pay) are presented clearly vs. cluttering the buy button area.

### Fix Prescriptions — Reference Shopify's Customization Layer
- **Use Theme Editor language:** "In Theme Editor > Theme Settings > Colors, adjust Color Scheme 1's accent color to match your primary brand color"
- **Not raw CSS:** Avoid "Change the CSS variable `--color-foreground` to `#1a1a1a`" — most Shopify merchants are non-technical and customize through the Theme Editor
- **For app issues:** "In the Judge.me app settings, match the review widget's font and star color to your theme's accent color" or "Consider disabling the Klarna messaging widget on mobile if it disrupts the product page layout"
- **For section overrides:** "In Theme Editor, click on the section and verify its color scheme matches the intended design. Shopify's color scheme system works best when you define 2-3 schemes and apply them consistently."
- **For legacy themes:** "This store uses a vintage (pre-OS 2.0) Shopify theme. Many improvements require upgrading to a modern OS 2.0 theme like Dawn, which provides CSS custom properties, section groups, and better performance out of the box."

---

## Common Anti-Patterns (Shopify-Specific)

### App CSS Conflicts
- Multiple review apps installed (Judge.me + Yotpo + native Shopify Reviews), each injecting their own star rating component with different sizing, colors, and fonts
- BNPL messaging widgets (Klarna, Afterpay, Shop Pay Installments) each adding payment messaging with inconsistent typography
- Apps loading their own font stacks that don't match the theme's `--font-body-family` or `--font-heading-family`
- App widgets ignecting CSS that overrides theme styles globally (e.g., `.button { background: #000 !important; }`)

### Section Color Override Patchwork
- Merchants applying different color schemes to adjacent sections with no design logic, creating a quilt-like visual effect
- Color scheme 1 (white bg) -> Color scheme 2 (dark bg) -> Color scheme 1 -> Color scheme 3 (accent bg) on a single page with no rhythm or rationale
- Per-section gradient backgrounds that don't relate to the global color system

### Font Inconsistency
- Theme defines 2 fonts (heading + body), but apps inject 1-3 additional font families
- Merchant adding custom CSS with `font-family` declarations that don't match theme settings
- Google Fonts loaded by both the theme and an app, resulting in duplicate font downloads and visual mismatch if different weights are used

### Non-Responsive App Widgets
- Dawn and modern Shopify themes are responsive, but third-party app widgets often are not
- Review photo grids that overflow on mobile
- Trust badge bars with fixed-width layouts that break below 375px
- Subscription widgets (Recharge) that don't adapt their radio button/toggle layout for small screens
- Klarna/Afterpay messaging that overlaps with Add to Cart on narrow viewports

### Trust Signal Fragmentation
- Trust badges from 3+ sources: Shopify Payments badge, app-injected security seals, manually uploaded PNG badges, and review aggregation widgets — each with different visual treatments
- No visual hierarchy among trust signals — all competing for attention on the product page
- Badge images at inconsistent sizes, resolutions (some retina, some not), and vertical alignment

### Popup and Overlay Overload
- Newsletter popup (Klaviyo) + cookie consent (native or app) + chat widget (Tidio/Gorgias) + exit-intent popup (Privy) all firing within 30 seconds of page load
- Z-index wars between apps — Klaviyo forms default to z-index ~90000; other apps compete with their own high values
- No merchant-level orchestration of when and how popups appear — each app manages its own trigger independently

### Legacy Theme Limitations
- Vintage themes (Debut, Brooklyn, Supply) lack CSS custom properties, making design consistency harder to maintain and evaluate
- jQuery dependency adds page weight and prevents modern performance patterns
- Limited section support (homepage only) means interior pages are less customizable and often visually inconsistent with the homepage
- No JSON templates means no merchant-controlled section reordering on product/collection pages

---

## Confidence Scoring

| Signal Combination | Confidence | Classification |
|---|---|---|
| `cdn.shopify.com` in 3+ asset URLs | 95+ | Shopify platform confirmed |
| `Shopify.theme` or `Shopify.routes` JS object detected | 90+ | Shopify platform confirmed |
| `<meta name="shopify-checkout-api-token">` present | 95+ | Shopify platform confirmed |
| `.shopify-section` wrapper classes in DOM | 90+ | Shopify platform + OS 2.0 theme confirmed |
| Theme-specific CSS vars (`--color-foreground`, `--font-body-family`, etc.) + Shopify CDN | 95+ | Specific theme identification (Dawn-based) |
| Dawn CSS variable namespace + `base.css` + per-section CSS loading | 95+ | Dawn or Dawn-fork confirmed |
| Maestrooo architecture (single `theme.css` + `vendor.min.js` + section-level CSS vars) | 85+ | Prestige/Impact/Stretch (check `Shopify.theme.name` for specifics) |
| `Shopify.theme.name` JS value readable | 98+ | Exact theme name confirmed |
| `Shopify.theme.theme_store_id` matches known theme store ID | 98+ | Exact theme confirmed via Shopify's theme registry |
| Shopify CDN detected but no theme-specific CSS patterns | 85 | Shopify confirmed, theme unidentified (custom or heavily modified) |
| `/collections/` + `/products/` URL patterns only (no CDN, no JS objects) | 60 | Possible Shopify — could be other e-commerce platforms using similar URL structures |
| `myshopify.com` in any source reference | 95+ | Shopify confirmed (even if custom domain is primary) |
| No Shopify indicators detected | 0 | This profile does not apply |

### Multi-Signal Stacking
Combine signals for highest confidence. A site showing `cdn.shopify.com` + `.shopify-section` classes + Dawn CSS variables = 98+ confidence in "Shopify running Dawn-based OS 2.0 theme." A site showing only `/products/` URL patterns = 60 confidence in Shopify (needs corroborating evidence).

### Theme vs. Platform Distinction
Platform confidence (is this Shopify?) and theme confidence (which Shopify theme?) are separate scores. A site can be 98% confirmed Shopify but 40% confident on the specific theme (e.g., heavily customized or agency-built). Always report both.
