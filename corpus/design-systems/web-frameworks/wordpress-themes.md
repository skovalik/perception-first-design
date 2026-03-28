# WordPress Themes — Design System Profile

## Detection Signals

### Core WordPress Indicators
- `<body>` class contains `wordpress` or `wp-` prefixed classes (e.g., `wp-custom-logo`, `wp-embed-responsive`)
- `wp-content/themes/{theme-name}/` in stylesheet and script URLs
- `wp-emoji-release.min.js` or `wp-embed.min.js` loaded in `<head>`
- Meta tag: `<meta name="generator" content="WordPress X.X">` (may be removed by security plugins)
- `<link rel="https://api.w.org/" href="/wp-json/">` in `<head>` — REST API discovery link
- REST API endpoint: `/wp-json/` returns WordPress site data (unless disabled)
- `X-WP-Total` and `X-WP-TotalPages` response headers on REST API calls
- Gutenberg block markup: `.wp-block-*` classes in post/page content
- `theme.json`-derived CSS custom properties on `<body>`: `--wp--preset--color--*`, `--wp--preset--font-size--*`, `--wp--preset--spacing--*`
- Login page at `/wp-login.php` or `/wp-admin/` redirect
- `xmlrpc.php` endpoint presence (legacy, often disabled)
- `style.css` accessible at `/wp-content/themes/{theme-name}/style.css` with theme header comment block (Theme Name, Author, Version, Description)

### Page Builder Detection
| Builder | Detection Signal | Implication |
|---------|-----------------|-------------|
| **Elementor** | `.elementor-*` classes (`.elementor-section`, `.elementor-widget`, `.elementor-column`), `data-elementor-type` attributes, `<meta name="elementor-version" content="X.X.X">`, `/wp-content/plugins/elementor/` assets, `elementor-kit-{id}` body class, CSS vars `--e-global-color-*`, `--e-global-typography-*` | Design system is Elementor's global settings, not the theme's. Evaluate Elementor's token system. |
| **WPBakery** | `.vc_row`, `.vc_column`, `.vc_column_container`, `.wpb_wrapper`, `.wpb_column` classes, `/wp-content/plugins/js_composer/` assets, `<meta name="generator" content="WPBakery Page Builder">`, shortcode artifacts `[vc_row]` in source | Legacy builder — often inconsistent tokens. No standardized CSS variable system. Evaluate inline and class-based styling. |
| **Divi** | `.et_pb_*` classes (`.et_pb_section`, `.et_pb_row`, `.et_pb_module`), `et-db` and `et-boc` body classes, `/wp-content/themes/Divi/` or `/wp-content/plugins/divi-builder/` assets, numbered module classes (`.et_pb_text_0`, `.et_pb_text_1`), `<!-- Added by Elegant Themes -->` comments | Divi controls the entire visual system. Theme and builder are unified. Evaluate Divi's variable system (`--et_*`). |
| **Beaver Builder** | `.fl-builder` wrapper class, `.fl-row`, `.fl-col-group`, `.fl-col`, `.fl-module` classes, `.fl-node-*` unique identifiers (e.g., `.fl-node-530d81d3093f5`), module-type classes (`.fl-module-heading`, `.fl-module-rich-text`), `/wp-content/plugins/bb-plugin/` assets | Builder-specific token system. Relatively clean HTML output. Evaluate builder-level styling. |
| **Gutenberg (native)** | `.wp-block-*` classes (`.wp-block-group`, `.wp-block-columns`, `.wp-block-image`), `.is-layout-*` classes (`.is-layout-flow`, `.is-layout-constrained`, `.is-layout-flex`), `.has-*` utility classes (`.has-text-color`, `.has-background`, `.has-large-font-size`), `is-style-{name}` block style classes, `wp-block-{namespace}-{block}` pattern | Uses theme.json tokens. Most standardized token system in WordPress. Evaluate `--wp--preset--*` CSS custom properties. |
| **None (classic)** | Standard WordPress classes only (post types, page templates, body classes like `page`, `single`, `home`, `archive`), no builder-specific class namespaces | Theme CSS controls everything. Tokens (if any) are theme-proprietary. Inspect theme's stylesheet for variable definitions. |

### Theme Detection
| Theme | Detection Signal | Common With |
|-------|-----------------|-------------|
| **Astra** | `.ast-*` classes (`ast-separate-container`, `ast-plain-container`, `ast-page-builder-template`), `astra-*` body classes, `/wp-content/themes/astra/` path, `ast-header-break-point` body class on mobile, `ast-desktop` body class on desktop, `astra-addon-*` plugin indicators | WooCommerce, Elementor. Most popular theme by install count. Lightweight base. |
| **Flatsome** | `.ux-*` classes, `flatsome` body class, `/wp-content/themes/flatsome/` path, UX Builder classes (`.ux-section`, `.ux-banner`), Flatsome-specific WooCommerce markup | WooCommerce-native. Built-in UX Builder. E-commerce focused layout patterns. |
| **OceanWP** | `.oceanwp-*` classes, `oceanwp` in body class, `/wp-content/themes/oceanwp/` path, `ocean-*` prefixed elements, OceanWP custom sidebar/header classes | Versatile, often paired with Elementor. Extensive customizer options. |
| **GeneratePress** | `.generate-*` classes (`generate-columns`, `generate-inside-container`), `/wp-content/themes/generatepress/` path, extremely minimal markup, GP-specific navigation classes, `no-sidebar` / `left-sidebar` / `right-sidebar` layout classes | Lightweight, developer-focused. <10KB base CSS. Often paired with GenerateBlocks plugin (`.gb-*` classes). |
| **Kadence** | `.kb-*` classes (from Kadence Blocks plugin), `kadence` in body class, `/wp-content/themes/kadence/` path, Kadence-specific header builder classes, `kadence-blocks` plugin indicators (`.kt-*` legacy, `.kb-*` current) | Modern block-first theme. Often uses Kadence Blocks for layout. Strong theme.json integration. |
| **Hello (Elementor)** | Minimal base markup, `hello-elementor` body class, `/wp-content/themes/hello-elementor/` path, near-zero theme-specific CSS — Elementor handles all styling | Pure Elementor canvas. Theme provides no visual system. Evaluate Elementor tokens exclusively. |

### WooCommerce Indicators
- `woocommerce` and `woocommerce-*` body classes (`woocommerce-page`, `woocommerce-cart`, `woocommerce-checkout`, `woocommerce-account`)
- `.woocommerce-*` prefixed classes (`.woocommerce-product-gallery`, `.woocommerce-breadcrumb`, `.woocommerce-result-count`, `.woocommerce-ordering`)
- `wc-*` script handles (`wc_add_to_cart_params`, `wc_checkout_params`, `wc_cart_fragments_params`)
- `/wp-content/plugins/woocommerce/assets/` in CSS/JS paths
- `wc-block-*` classes (WooCommerce Blocks — newer block-based components)
- Cart widget markup (`.widget_shopping_cart`, `.cart-contents`)
- Product page structured data (`@type: Product` JSON-LD)
- WooCommerce REST API: `/wp-json/wc/v3/` endpoint
- Notice classes: `.woocommerce-message`, `.woocommerce-error`, `.woocommerce-info`

---

## Token System

WordPress token systems vary dramatically by theme type and builder. The evaluator must first identify which token system is active before measuring compliance.

### Block Themes (theme.json — WordPress 5.9+, v3 schema in 6.6+)

**CSS custom property naming convention:**
- Presets: `--wp--preset--{category}--{slug}` (machine-parseable, double-hyphen separators)
- Custom: `--wp--custom--{variable-name}` (camelCase in JSON becomes hyphenated in CSS)
- Example: `--wp--preset--color--primary`, `--wp--preset--font-size--large`, `--wp--preset--spacing--50`

**Color palette:**
- Defined in `settings.color.palette[]` as `{ slug, color, name }` objects
- Generates: `--wp--preset--color--{slug}` CSS vars + `.has-{slug}-color` / `.has-{slug}-background-color` utility classes
- Typical palette: 5-12 named colors (primary, secondary, accent, base, contrast, plus theme-specific)

**Typography:**
- Font families: `settings.typography.fontFamilies[]` generates `--wp--preset--font-family--{slug}`
- Font sizes: `settings.typography.fontSizes[]` generates `--wp--preset--font-size--{slug}`
- Size scale often uses `clamp()` for fluid typography: e.g., `clamp(0.875rem, 0.875rem + ((1vw - 0.48rem) * 0.24), 1rem)`
- Common slugs: `small`, `medium`, `large`, `x-large`, `xx-large` (or numeric: `13`, `14`, `16`, `20`)

**Spacing:**
- `settings.spacing.spacingSizes[]` or `settings.spacing.spacingScale` (auto-generated)
- Generates: `--wp--preset--spacing--{slug}` (typically numeric: `20`, `30`, `40`, `50`, `60`, `70`, `80`)
- Applied via `.has-spacing-{slug}` utility classes or direct CSS var references
- Scale maps to `clamp()` values for fluid spacing

**Custom properties:**
- Theme-defined via `settings.custom` object in theme.json
- Naming: `--wp--custom--{path}` where nested keys use `--` separators
- Example: `settings.custom.lineHeight.heading` becomes `--wp--custom--line-height--heading`
- CamelCase auto-hyphenated: `textShadow` becomes `text-shadow`

**Origin cascade (specificity order):**
1. Core defaults (lowest)
2. Theme (`theme.json`)
3. User (Global Styles customization in Site Editor — highest)

### Classic Themes (pre-block-editor, or themes without theme.json)
- **No standardized token system** — each theme defines its own CSS variables (if any)
- Customizer-driven: colors and fonts often output as inline `<style>` block via `wp_head` hook
- Common pattern: 3-5 accent colors defined in customizer, inconsistently applied across components
- Many classic themes use no CSS custom properties at all — raw hex values, font stacks, and pixel values in compiled CSS
- Some premium classic themes (Avada, Flavor, X Theme) have proprietary option panels that generate inline CSS from 50+ settings — these create pseudo-token systems with no standard naming

### Page Builder Token Override
When a page builder is active, it injects its own token system that typically overrides the theme's tokens:

- **Elementor:** `--e-global-color-primary`, `--e-global-color-secondary`, `--e-global-color-text`, `--e-global-color-accent` (4 base global colors + unlimited custom), `--e-global-typography-*` for font settings. Elementor 3.33+ introduces a Variables Manager for centralized design token control.
- **Divi:** `--et_*` CSS variables, plus inline styles generated from Divi's Visual Builder settings. Module-level overrides are common (each `.et_pb_*` element can have unique inline styles).
- **Beaver Builder:** No standardized CSS variable system — uses compiled CSS from module settings. Global colors/fonts configured in BB Global Settings but output as direct CSS values, not variables.
- **WPBakery:** No CSS variable system. Styles are generated inline or via compiled custom CSS. Design tokens are effectively nonexistent — evaluate as raw CSS.

**Critical rule:** When a builder is detected, evaluate the builder's token system, not the theme's. The builder's tokens are what the user actually controls and what renders on the page.

---

## Visual Language Patterns

WordPress sites have the **widest design variance of any framework** — from polished modern block themes indistinguishable from custom builds to legacy sites with 2012-era aesthetics still running on outdated themes.

**Key visual patterns by configuration:**

- **Block themes (Twenty Twenty-Four, Flavor, Flavor Starter):** Modern, content-first design. Fluid typography and spacing. Minimal decorative elements. Strong vertical rhythm from spacing presets.
- **Elementor-based sites:** High visual variety. Common patterns: full-width sections, overlay text on images, heavy use of background colors/gradients, animated entrance effects. Visual quality depends on the template/kit used.
- **Divi-based sites:** Distinctive "Divi look" — wide sections with centered content, heavy use of parallax backgrounds, button hover effects, animated counters/stats. Recognizable visual language.
- **WooCommerce sites:** Often have **split design systems** — marketing pages follow the theme's visual language while shop/product/cart/checkout pages follow WooCommerce defaults partially overridden by the theme. This split is the #1 source of visual inconsistency.
- **Classic themes with customizer:** Visual polish ceiling is lower. Limited layout options lead to similar-looking sites within the same theme. Typography often defaults to system fonts or basic Google Fonts.

**Mobile responsiveness is theme-dependent, not WordPress-inherent.** WordPress core provides no responsive layout system — all responsiveness comes from the theme, builder, or both. This must be checked explicitly for every WordPress site. Block themes with `is-layout-*` classes provide the most reliable responsive behavior.

**Plugin visual injection:** WordPress sites frequently have visual elements injected by plugins that exist outside the theme's design system — cookie consent banners, chat widgets (Tidio, LiveChat, Drift), newsletter popups (OptinMonster, Sumo), notification bars, security challenge pages (Wordfence, Sucuri). These elements typically have their own styling that conflicts with or ignores the theme's design system.

---

## PFD Evaluation Adjustments

### L2 Token Compliance
**First: identify which token system is active.** This is the critical prerequisite for any L2 evaluation on WordPress.

1. Check for theme.json CSS vars (`--wp--preset--*`) — if present, the site uses the block theme token system
2. Check for builder CSS vars (`--e-global-*`, `--et_*`) — if present, the builder's tokens are the active system
3. If neither is present, the site uses raw CSS with no formal token system — evaluate for internal consistency rather than token compliance

Token compliance is measured against the **active** system, not a universal standard. A site using Elementor's 4 global colors consistently scores higher on L2 than a site with theme.json tokens that are inconsistently applied.

### L2 Processing Fluency — Cross-Source Inconsistency
WordPress sites commonly have **3+ distinct CSS sources** competing for visual control:
- Theme stylesheet(s)
- Builder stylesheet(s)
- Plugin stylesheets (WooCommerce, form plugins, slider plugins, etc.)
- Inline styles from customizer/builder settings
- Custom CSS added via Appearance > Additional CSS

**Cross-source inconsistency is the #1 L2 violation pattern in WordPress.** Typical manifestation: buttons styled one way in the theme, another way in the builder, and a third way in WooCommerce. Headings that use one font in blog posts (theme), another in landing pages (builder), and another in the sidebar (widget plugin).

When documenting L2 violations, specify which CSS source is responsible: "Button inconsistency: theme buttons use `border-radius: 4px` (theme.css), Elementor CTA buttons use `border-radius: 25px` (elementor-kit), WooCommerce buttons use `border-radius: 0` (woocommerce.css)."

### Foundation (L0) — Cognitive Load from Plugin Bloat
Plugin-injected elements frequently push cognitive load beyond thresholds:
- Cookie consent overlays (covers content, demands decision)
- Chat widgets (persistent floating element, animation draws attention)
- Newsletter popups (interrupts flow, typically timed or scroll-triggered)
- Notification bars (top-of-page, compresses viewport)
- Social sharing bars (fixed position, competes with primary content)
- Security challenge pages (Wordfence CAPTCHA, Sucuri verification)

**Distinguish plugin-injected from theme-designed elements.** Plugin-injected elements should be evaluated separately from the theme's intentional design. The fix for excessive cognitive load from plugins is to remove or consolidate plugins, not to redesign the theme.

Count visible interactive elements including plugin overlays. WordPress sites frequently exceed the 5-7 visible interactive elements guideline when plugins are included.

### Fix Prescriptions — Reference the Active System
Fix prescriptions must reference the tools the site owner actually uses:

| If detected... | Prescribe using... | Not... |
|----------------|-------------------|--------|
| Elementor | "In Elementor > Site Settings > Global Colors, consolidate to 2 font families" | "Change your CSS font-family declarations" |
| Divi | "In Divi Theme Options > General > Typography, set body font to match heading font family" | "Edit your stylesheet to unify fonts" |
| Block theme | "In Appearance > Editor > Styles, update the color palette to remove duplicate blues" | "Modify your theme.json file" |
| WooCommerce | "In WooCommerce > Customize, override button styles to match theme" | "Add CSS to fix shop buttons" |
| Classic + customizer | "In Appearance > Customize > Colors, set accent color to match your primary brand color" | "Change the hex values in your CSS" |

---

## Common Anti-Patterns (WordPress-Specific)

### Plugin CSS Conflicts
Multiple plugins inject competing stylesheets. Common symptom: buttons have 3+ different styles across the site (theme buttons, builder buttons, WooCommerce buttons, contact form buttons, newsletter form buttons). Each plugin loads its own CSS with its own specificity, creating an inconsistent visual language that no single control point can fix.

**Detection:** Inspect buttons or form elements across 3+ page types (homepage, blog post, product page, contact page). If they differ in border-radius, padding, font, or color — this anti-pattern is present.

### Partial WooCommerce Style Overrides
Theme provides WooCommerce integration but only overrides some default styles. Product pages match the theme, but cart/checkout pages revert to WooCommerce defaults. Common in themes that list "WooCommerce compatible" but only style the product grid, leaving transactional pages unstyled.

**Detection:** Compare visual treatment (colors, typography, spacing, button styles) of product listing pages vs cart vs checkout. Inconsistency between these three views confirms partial override.

### Mobile Menu Conflicts
Theme provides a mobile menu (hamburger/slide-out), but a plugin adds a sticky header, another plugin adds a mobile-specific CTA bar, and the builder has its own responsive header. Result: overlapping navigation elements, z-index battles, and tappable areas that are too small or overlap.

**Detection:** Test on mobile viewport (375px). Check for overlapping fixed/sticky elements. Verify hamburger menu opens cleanly without being obscured.

### Multiple Font Sources
Fonts loaded from multiple origins simultaneously:
- Google Fonts enqueued by the theme
- Google Fonts loaded by Elementor/Divi independently
- Google Fonts loaded by a typography plugin (Easy Google Fonts, etc.)
- System fonts or self-hosted fonts in the theme's CSS
- Web font loaded by a third-party widget/plugin

**Detection:** Check `<link>` tags and `@font-face` declarations in page source. Count unique font-loading sources. More than 2 sources loading fonts is a strong signal of this anti-pattern. Performance impact: each additional font source adds render-blocking time.

### Color Inconsistency Between Systems
Theme customizer defines a palette (e.g., primary blue `#2563EB`). Page builder defines its own global colors (e.g., primary blue `#3B82F6`). WooCommerce buttons use yet another blue (`#0073AA`). Cookie consent plugin uses its own brand color. Result: 3-4 "primary blues" that are close but not identical, creating subtle processing fluency violations.

**Detection:** Sample the primary accent color from 5+ elements across the site using a color picker. If the sampled values differ (even by small amounts like `#2563EB` vs `#2563eb` vs `#2764EC`), this anti-pattern is present.

### Unused Theme/Builder CSS Bloat
Page builders generate CSS for all possible widgets/modules even when only a few are used. Common: Elementor loads 300KB+ of CSS, Divi loads its entire framework CSS, WPBakery loads all grid/shortcode styles. Combined with theme CSS and plugin CSS, total stylesheet size can exceed 500KB.

**Detection:** Check total CSS payload in network tab. WordPress sites with builders commonly load 400-800KB of CSS. Compare against the 50-150KB range typical of purpose-built sites. This affects Foundation-layer load time and perceived performance.

---

## Confidence Scoring

### WordPress Platform Detection
| Signal | Confidence |
|--------|-----------|
| `wp-content/themes/` in any URL path | 90+ |
| `<meta name="generator" content="WordPress">` present | 95+ |
| WordPress body classes (`wp-custom-logo`, page-type classes) | 80+ |
| `/wp-json/` REST API endpoint responds | 85+ |
| `wp-emoji-release.min.js` loaded | 75 (can be removed) |
| `/wp-login.php` accessible | 80+ |
| No WordPress indicators detected | 0 — do not apply this profile |

### Page Builder Detection
| Signal | Confidence in Builder | Effect on Theme Detection |
|--------|-----------------------|--------------------------|
| Elementor classes (`.elementor-*`) + meta tag | 95+ | Theme detection still valid but theme visual system is secondary |
| Divi classes (`.et_pb_*`) + `et-boc` body class | 95+ | Theme is Divi — builder and theme are unified |
| WPBakery classes (`.vc_*`, `.wpb_*`) + `js_composer` assets | 90+ | Theme provides base, builder handles layout |
| Beaver Builder classes (`.fl-*`) + `bb-plugin` assets | 90+ | Theme provides base, builder handles layout |
| Gutenberg blocks (`.wp-block-*`) without other builders | 85+ | Theme.json tokens are the primary system |
| No builder classes detected | 0 for all builders | Theme CSS is the sole visual system — evaluate theme directly |

### WooCommerce Detection
| Signal | Confidence |
|--------|-----------|
| `woocommerce` body class + plugin assets | 95+ |
| WooCommerce CSS classes on product/cart/checkout pages | 90+ |
| `wc-block-*` classes (block-based WooCommerce) | 85+ |
| `/wp-json/wc/v3/` endpoint responds | 90+ |
| No WooCommerce indicators | 0 — do not apply WooCommerce-specific evaluation rules |

### Combined Confidence Logic
When multiple signals are detected, apply the most specific profile:
1. **WooCommerce + Builder + Theme:** Evaluate WooCommerce pages against WooCommerce rules, marketing pages against builder rules, and check consistency between the two systems. This is the highest-complexity evaluation scenario.
2. **Builder + Theme (no WooCommerce):** Evaluate against the builder's token system. Note theme name for context but measure against builder tokens.
3. **Theme only (no builder, no WooCommerce):** Evaluate against theme's CSS — either theme.json tokens (block themes) or raw CSS analysis (classic themes).
4. **WordPress detected but theme/builder unclear:** Flag low confidence on design system identification. Evaluate against general PFD principles without framework-specific adjustments.
