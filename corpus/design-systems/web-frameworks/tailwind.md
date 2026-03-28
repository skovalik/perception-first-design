# Tailwind CSS — Design System Profile

> **Purpose:** Enable automated detection of Tailwind CSS (v3 and v4) from HTML/CSS inspection, and adjust PFD evaluation rules for Tailwind's design system conventions. This profile is loaded at Slot [12] of the evaluation prompt when Tailwind is detected.

---

## 1. Detection Signals

### 1.1 Class Pattern Detection

Tailwind sites are identified by high density of atomic utility classes in HTML markup. These classes follow predictable naming conventions.

**Layout utilities:**
- `flex`, `inline-flex`, `grid`, `inline-grid`, `block`, `inline-block`, `hidden`
- `items-center`, `justify-between`, `gap-{n}`, `space-x-{n}`, `space-y-{n}`
- `container`, `mx-auto`, `max-w-{size}`

**Spacing utilities (4px base unit):**
- Padding: `p-{n}`, `px-{n}`, `py-{n}`, `pt-{n}`, `pr-{n}`, `pb-{n}`, `pl-{n}`
- Margin: `m-{n}`, `mx-{n}`, `my-{n}`, `mt-{n}`, `mr-{n}`, `mb-{n}`, `ml-{n}`
- Negative values: `-m-{n}`, `-mt-{n}`, etc.

**Typography utilities:**
- Size: `text-xs`, `text-sm`, `text-base`, `text-lg`, `text-xl` through `text-9xl`
- Weight: `font-thin`, `font-light`, `font-normal`, `font-medium`, `font-semibold`, `font-bold`, `font-extrabold`, `font-black`
- Leading: `leading-none`, `leading-tight`, `leading-snug`, `leading-normal`, `leading-relaxed`, `leading-loose`
- Tracking: `tracking-tighter`, `tracking-tight`, `tracking-normal`, `tracking-wide`, `tracking-wider`, `tracking-widest`
- Color: `text-{color}-{shade}` (e.g., `text-gray-700`, `text-slate-900`)

**Color/background utilities:**
- `bg-{color}-{shade}` (e.g., `bg-blue-500`, `bg-zinc-100`)
- `text-{color}-{shade}` for text color
- `border-{color}-{shade}` for border color
- `ring-{color}-{shade}` for focus rings

**Visual utilities:**
- Border radius: `rounded`, `rounded-sm`, `rounded-md`, `rounded-lg`, `rounded-xl`, `rounded-2xl`, `rounded-3xl`, `rounded-full`
- Shadow: `shadow-sm`, `shadow`, `shadow-md`, `shadow-lg`, `shadow-xl`, `shadow-2xl`
- Opacity: `opacity-{n}` (0-100)

**Responsive prefixes (mobile-first, min-width):**
- `sm:` (640px), `md:` (768px), `lg:` (1024px), `xl:` (1280px), `2xl:` (1536px)
- Applied as prefix to any utility: `md:flex`, `lg:grid-cols-3`, `xl:text-lg`

**State variants:**
- Interactive: `hover:`, `focus:`, `active:`, `visited:`, `disabled:`
- Focus variants: `focus-visible:`, `focus-within:`
- Group variants: `group-hover:`, `group-focus:`, `group-data-{attr}:`
- Peer variants: `peer-checked:`, `peer-focus:`, `peer-invalid:`
- Dark mode: `dark:`
- Conditional: `first:`, `last:`, `odd:`, `even:`, `empty:`
- Form state: `required:`, `invalid:`, `placeholder:`, `autofill:`

**Stacked variants (Tailwind-specific pattern):**
- Two or more variants combined: `dark:hover:bg-gray-700`, `sm:group-hover:text-white`, `lg:dark:bg-zinc-900`
- Stacked variants are a strong Tailwind signal; few other frameworks support this syntax

**JIT arbitrary values (square bracket syntax):**
- Arbitrary spacing: `w-[200px]`, `h-[calc(100vh-4rem)]`, `mt-[37px]`
- Arbitrary colors: `bg-[#1a1a2e]`, `text-[oklch(0.6_0.2_270)]`
- Arbitrary values: `grid-cols-[1fr_200px_1fr]`, `top-[117px]`
- These use square brackets directly in class names — a highly distinctive Tailwind signal

**v4-specific indicators:**
- `bg-linear-to-{dir}` replaces v3's `bg-gradient-to-{dir}` (e.g., `bg-linear-to-r` instead of `bg-gradient-to-r`)
- Dynamic spacing values without definition: `w-17`, `p-13` (v4 allows any spacing value, not just predefined scale)
- 3D transforms: `rotate-x-{n}`, `rotate-y-{n}`, `scale-z-{n}`, `translate-z-{n}`
- Container queries: `@container`, `@sm:`, `@md:`, `@lg:` etc.

**Detection threshold:**
- 20+ distinct utility classes on elements within `<body>` = high confidence
- Presence of responsive prefixes (`sm:`, `md:`, etc.) alongside utilities = very high confidence
- Stacked variants (`dark:hover:`, `lg:group-hover:`) = near-certain Tailwind

### 1.2 CSS Custom Properties

**Tailwind v3 internal properties (`--tw-*` namespace):**
- `--tw-shadow`, `--tw-shadow-color` (shadow utilities)
- `--tw-ring-color`, `--tw-ring-offset-width`, `--tw-ring-offset-color` (ring utilities)
- `--tw-translate-x`, `--tw-translate-y` (transform utilities)
- `--tw-rotate`, `--tw-skew-x`, `--tw-skew-y` (transform utilities)
- `--tw-scale-x`, `--tw-scale-y` (scale utilities)
- `--tw-blur`, `--tw-brightness`, `--tw-contrast`, `--tw-grayscale` (filter utilities)
- `--tw-border-opacity`, `--tw-bg-opacity`, `--tw-text-opacity` (opacity modifiers)
- These are implementation variables, not design tokens. Their presence strongly indicates Tailwind.

**Tailwind v4 theme variables (no `--tw-` prefix by default):**
- v4 exposes all theme tokens as CSS custom properties automatically
- Namespace convention: `--color-*`, `--font-*`, `--spacing-*`, `--breakpoint-*`, `--radius-*`, `--shadow-*`
- Example: `--color-blue-500`, `--font-sans`, `--spacing-4`
- If the site uses `prefix("tw")`, variables revert to `--tw-color-*`, `--tw-font-*`, etc.
- v4 uses `@property` registered custom properties for animations (enables gradient animation, etc.)

**shadcn/ui pattern (semantic CSS vars on `:root` and `.dark`):**
- `--background`, `--foreground`
- `--card`, `--card-foreground`
- `--popover`, `--popover-foreground`
- `--primary`, `--primary-foreground`
- `--secondary`, `--secondary-foreground`
- `--muted`, `--muted-foreground`
- `--accent`, `--accent-foreground`
- `--destructive`, `--destructive-foreground`
- `--border`, `--input`, `--ring`
- `--radius` (global border radius)
- `--chart-1` through `--chart-5` (chart colors)
- `--sidebar`, `--sidebar-foreground`, `--sidebar-primary`, `--sidebar-primary-foreground`, `--sidebar-accent`, `--sidebar-accent-foreground`, `--sidebar-border`, `--sidebar-ring`
- Modern shadcn uses OKLCH color values: `--background: oklch(1 0 0)`
- Legacy shadcn uses HSL values: `--background: 0 0% 100%`
- Presence of `--radius` + `--primary` + `--background` in the `background/foreground` naming pattern is near-certain shadcn/ui

**DaisyUI pattern (OKLCH theme variables):**
- Base colors: `--b1`, `--b2`, `--b3` (background shades, lightest to darkest), `--bc` (base content/text)
- Primary: `--p` (primary), `--pc` (primary content), `--pf` (primary focus)
- Secondary: `--s`, `--sc`, `--sf`
- Accent: `--a`, `--ac`, `--af`
- Neutral: `--n`, `--nc`, `--nf`
- Info/Success/Warning/Error: `--in`, `--su`, `--wa`, `--er` (plus content variants `--inc`, `--suc`, `--wac`, `--erc`)
- Values are OKLCH triplets: `--p: 49.12% 0.3096 275.75`
- `--b2` and `--b3` auto-derive from `--b1` if not set
- `data-theme` attribute on `<html>` selects the active DaisyUI theme

### 1.3 Config Artifacts

**v3 compiled output signals:**
- `@tailwind base;`, `@tailwind components;`, `@tailwind utilities;` directives (source; stripped in production)
- `@layer base { ... }`, `@layer components { ... }`, `@layer utilities { ... }` in compiled CSS
- Preflight reset: opinionated CSS reset (margin: 0, border-style: solid, etc.) present in `@layer base`
- Comment markers in development: `/* ! tailwindcss v3.x.x */`

**v4 compiled output signals:**
- `@import "tailwindcss"` (source; resolved in production)
- `@layer theme { ... }`, `@layer base { ... }`, `@layer components { ... }`, `@layer utilities { ... }` — note the addition of `theme` layer
- `@layer properties { ... }` — v4 uses this for `@property` registered custom properties
- `@theme { ... }` blocks defining custom tokens
- `@utility` and `@custom-variant` directives (source; inlined in production)
- `@source` directives for content detection hints

**Build tool indicators:**
- PostCSS config with `tailwindcss` plugin (v3)
- `@tailwindcss/vite`, `@tailwindcss/postcss`, or `@tailwindcss/cli` packages (v4)
- `tailwind.config.js` or `tailwind.config.ts` (v3; v4 uses CSS-first config, though JS config is still supported)

### 1.4 Component Library Detection

| Library | Detection Signal | Confidence Boost |
|---------|-----------------|-----------------|
| **shadcn/ui** | `data-slot` attributes on primitives (v4+), `data-state` attributes on interactive elements, CSS vars `--radius` + `--primary` + `--background` using OKLCH or HSL values, `cn()` utility in source | +15 (to 95+) |
| **Headless UI** | `data-headlessui-state` attributes, `data-open`, `data-closed`, `data-enter`, `data-leave`, `data-transition` attributes, `group-data-open:` Tailwind selectors | +10 |
| **DaisyUI** | Semantic component classes (`.btn`, `.card`, `.hero`, `.navbar`, `.drawer`, `.modal`, `.dock`) alongside Tailwind utilities, `data-theme` attribute on `<html>`, OKLCH CSS vars (`--b1`, `--p`, `--s`) | +10 |
| **Flowbite** | `data-modal-target`, `data-modal-toggle`, `data-dropdown-toggle`, `data-collapse-toggle`, `data-tooltip-target`, `data-accordion-target` attributes, `flowbite.min.js` script inclusion | +10 |
| **Radix UI** (without shadcn) | `data-state`, `data-orientation`, `data-side`, `data-align` attributes, `radix-*` CSS classes, but WITHOUT shadcn's CSS variable pattern | +5 |
| **Custom / None** | Tailwind utility classes without any component library indicators — raw utility composition | +0 (base score) |

---

## 2. Token System

### 2.1 Colors

**Neutral scales (6 variants, each with 11 shades: 50-950):**
- `slate` — cool blue-gray (default in many Tailwind projects)
- `gray` — true neutral gray
- `zinc` — warm-cool balanced gray
- `neutral` — mathematically neutral
- `stone` — warm brown-gray

**Chromatic palette (17 hues, each with 11 shades: 50-950):**
- Warm: `red`, `orange`, `amber`, `yellow`
- Green: `lime`, `green`, `emerald`, `teal`
- Cool: `cyan`, `sky`, `blue`, `indigo`
- Purple: `violet`, `purple`, `fuchsia`
- Pink: `pink`, `rose`

**Shade scale:** 50, 100, 200, 300, 400, 500, 600, 700, 800, 900, 950

**v4 color format:** OKLCH (Oklab color space) — replaces v3's sRGB hex/HSL values. Enables perceptually uniform color mixing and better dark mode palettes.

**Semantic tokens (when shadcn/ui or custom tokens are layered):**
- `primary`, `secondary`, `accent`, `destructive`, `muted` — applied via CSS variables, used as `bg-primary`, `text-primary-foreground`, etc.
- Black and white: `black`, `white`

### 2.2 Spacing

**Base unit:** 1 spacing unit = 0.25rem = 4px (at default 16px root font size)

**Full scale:**
| Class | Value | Pixels |
|-------|-------|--------|
| `{p\|m}-0` | 0 | 0px |
| `{p\|m}-px` | 1px | 1px |
| `{p\|m}-0.5` | 0.125rem | 2px |
| `{p\|m}-1` | 0.25rem | 4px |
| `{p\|m}-1.5` | 0.375rem | 6px |
| `{p\|m}-2` | 0.5rem | 8px |
| `{p\|m}-2.5` | 0.625rem | 10px |
| `{p\|m}-3` | 0.75rem | 12px |
| `{p\|m}-3.5` | 0.875rem | 14px |
| `{p\|m}-4` | 1rem | 16px |
| `{p\|m}-5` | 1.25rem | 20px |
| `{p\|m}-6` | 1.5rem | 24px |
| `{p\|m}-7` | 1.75rem | 28px |
| `{p\|m}-8` | 2rem | 32px |
| `{p\|m}-9` | 2.25rem | 36px |
| `{p\|m}-10` | 2.5rem | 40px |
| `{p\|m}-11` | 2.75rem | 44px |
| `{p\|m}-12` | 3rem | 48px |
| `{p\|m}-14` | 3.5rem | 56px |
| `{p\|m}-16` | 4rem | 64px |
| `{p\|m}-20` | 5rem | 80px |
| `{p\|m}-24` | 6rem | 96px |
| `{p\|m}-28` | 7rem | 112px |
| `{p\|m}-32` | 8rem | 128px |
| `{p\|m}-36` | 9rem | 144px |
| `{p\|m}-40` | 10rem | 160px |
| `{p\|m}-44` | 11rem | 176px |
| `{p\|m}-48` | 12rem | 192px |
| `{p\|m}-52` | 13rem | 208px |
| `{p\|m}-56` | 14rem | 224px |
| `{p\|m}-60` | 15rem | 240px |
| `{p\|m}-64` | 16rem | 256px |
| `{p\|m}-72` | 18rem | 288px |
| `{p\|m}-80` | 20rem | 320px |
| `{p\|m}-96` | 24rem | 384px |

**v4 addition:** Any integer value works (e.g., `p-13` = 3.25rem = 52px). The scale above is the named default; v4 generates utilities dynamically for any value on the 4px grid.

### 2.3 Typography

**Size scale:**
| Class | Font Size | Default Line Height |
|-------|-----------|-------------------|
| `text-xs` | 0.75rem (12px) | 1rem (16px) |
| `text-sm` | 0.875rem (14px) | 1.25rem (20px) |
| `text-base` | 1rem (16px) | 1.5rem (24px) |
| `text-lg` | 1.125rem (18px) | 1.75rem (28px) |
| `text-xl` | 1.25rem (20px) | 1.75rem (28px) |
| `text-2xl` | 1.5rem (24px) | 2rem (32px) |
| `text-3xl` | 1.875rem (30px) | 2.25rem (36px) |
| `text-4xl` | 2.25rem (36px) | 2.5rem (40px) |
| `text-5xl` | 3rem (48px) | 1 |
| `text-6xl` | 3.75rem (60px) | 1 |
| `text-7xl` | 4.5rem (72px) | 1 |
| `text-8xl` | 6rem (96px) | 1 |
| `text-9xl` | 8rem (128px) | 1 |

**Weight scale:** `font-thin` (100), `font-extralight` (200), `font-light` (300), `font-normal` (400), `font-medium` (500), `font-semibold` (600), `font-bold` (700), `font-extrabold` (800), `font-black` (900)

**Font families:** `font-sans` (system UI stack), `font-serif` (Georgia/system serif stack), `font-mono` (monospace stack). Custom fonts are defined via `@theme` (v4) or `tailwind.config.js` (v3) and used as `font-{name}`.

### 2.4 Borders

**Border radius scale:**
| Class | Value |
|-------|-------|
| `rounded-none` | 0 |
| `rounded-sm` | 0.125rem (2px) |
| `rounded` | 0.25rem (4px) |
| `rounded-md` | 0.375rem (6px) |
| `rounded-lg` | 0.5rem (8px) |
| `rounded-xl` | 0.75rem (12px) |
| `rounded-2xl` | 1rem (16px) |
| `rounded-3xl` | 1.5rem (24px) |
| `rounded-full` | 9999px |

**Border width:** `border` (1px default), `border-0`, `border-2`, `border-4`, `border-8`

**v4 note:** Default border color changed from `gray-200` to `currentColor`. Sites migrated from v3 that don't account for this may show unexpected border colors.

### 2.5 Shadows

| Class | Effect |
|-------|--------|
| `shadow-sm` | Subtle, barely visible |
| `shadow` | Small, default |
| `shadow-md` | Medium elevation |
| `shadow-lg` | Pronounced elevation |
| `shadow-xl` | High elevation |
| `shadow-2xl` | Maximum elevation |
| `shadow-none` | No shadow |
| `shadow-inner` | Inset shadow |

### 2.6 Default Breakpoints

| Prefix | Min-width | Typical target |
|--------|-----------|---------------|
| *(none)* | 0px | Mobile (base) |
| `sm:` | 640px | Large phones / small tablets |
| `md:` | 768px | Tablets |
| `lg:` | 1024px | Laptops |
| `xl:` | 1280px | Desktops |
| `2xl:` | 1536px | Large desktops |

---

## 3. Visual Language Patterns

How Tailwind sites typically look, by design system context. Use these patterns to distinguish intentional design choices from violations.

### 3.1 Border Radius

Modern Tailwind projects trend toward generous rounding. `rounded-lg` and `rounded-xl` are the most common on cards, buttons, and inputs. `rounded-full` is standard for avatars, badges, and pill buttons. Sharp corners (`rounded-none` or `rounded-sm`) signal a deliberately angular design language and should not be flagged as violations.

### 3.2 Density and Spacing

Varies by component library:
- **shadcn/ui:** Balanced density, generous padding (`p-4` to `p-6` on cards), clear breathing room. Buttons are `h-9` to `h-11`. Intentionally calm.
- **DaisyUI:** Denser, more opinionated defaults. Buttons and cards come pre-sized. Less whitespace than shadcn.
- **Flowbite:** Bootstrap-adjacent density. Components feel familiar to Bootstrap users.
- **Custom Tailwind (no library):** Wide variance. Density reflects the developer's intent. No default assumption.

### 3.3 Motion and Transitions

Tailwind's transition utilities encourage subtle, fast animations:
- `transition-all duration-150` — snappy interactions (common on hover states)
- `transition-colors duration-200` — color-only transitions
- `duration-300` — standard smoothness for most transitions
- `ease-in-out` is the default easing; `ease-out` for entrances, `ease-in` for exits
- Heavy animation (>500ms, complex keyframes) is unusual in Tailwind projects and typically indicates custom CSS additions or a specific animation library (Framer Motion, GSAP)

### 3.4 Shadow Depth

Tailwind's default shadow scale is deliberately subtle. Most production Tailwind sites use `shadow-sm` to `shadow-md`. Use of `shadow-xl` or `shadow-2xl` is intentional emphasis, not default styling. Deep shadows on every card or element may signal inconsistent design decisions but are not inherently wrong.

### 3.5 Color Usage

Most Tailwind sites use one neutral scale (gray/slate/zinc) plus 1-3 accent colors. The full 17-hue palette is available but rarely used in full. If a site uses more than 5 distinct hues, check whether it is intentional (data visualization, illustration-heavy design) or accidental (L2 color inconsistency).

---

## 4. PFD Evaluation Adjustments

When Tailwind CSS is detected, apply these modifications to standard PFD evaluation rules.

### 4.1 L2 — Token Compliance (Elevated Severity)

Tailwind provides an extensive, well-defined token system. This raises the bar for consistency:

- **Spacing violations are more severe.** Arbitrary values like `mt-[37px]` or `p-[13px]` when `mt-9` (36px) or `p-3` (12px) exist on the default scale are L2 processing fluency violations. Tailwind makes on-system trivially easy, so off-system is a stronger signal of broken design intent.
- **Exception:** Arbitrary values that are clearly outside the scale (e.g., `w-[calc(100vw-var(--sidebar-width))]`, `top-[var(--header-height)]`) are functional, not violations. The test is: does a standard scale value exist within 4px of this arbitrary value? If yes, flag it.
- **v4 dynamic values:** In Tailwind v4, any integer on the 4px grid is valid (e.g., `p-13` = 52px is valid, no brackets needed). Only flag spacing values that are not on the 4px grid AND use arbitrary syntax.

### 4.2 L2 — Color Consistency (Elevated Severity)

- **Off-palette colors are high-severity.** Arbitrary hex values in classes (e.g., `bg-[#3a7bd5]`) when a configured palette color exists nearby (e.g., `bg-blue-500`) are more costly in Tailwind than in vanilla CSS, per Learning #16 (near-miss color asymmetry). Tailwind makes palette adherence trivial, so violations signal broken process, not missing tooling.
- **Check the configured palette, not just defaults.** If the site has custom colors defined via `@theme` (v4) or `tailwind.config.js` (v3), those are the reference palette. Only flag colors that are off the site's configured system, not just Tailwind's defaults.
- **shadcn semantic tokens:** If shadcn is detected, the semantic layer (`bg-primary`, `text-muted-foreground`) is the authoritative system. Direct color scale usage (e.g., `bg-blue-500` instead of `bg-primary`) in non-utility contexts may indicate incomplete token adoption.

### 4.3 Foundation (L0) — Responsive (Elevated Expectation)

- **Absence of responsive prefixes is a stronger signal.** Tailwind's responsive prefix system is zero-friction. If layout-critical elements (grid columns, flex direction, font size, padding) lack responsive prefixes entirely, this is a stronger Foundation violation than in vanilla CSS, where responsive design requires more effort.
- **Check for mobile-first flow.** Tailwind is mobile-first by design — base classes apply at all sizes, prefixed classes apply at breakpoints and up. If the site works on desktop but breaks on mobile, the developer likely designed desktop-first and forgot base styles.
- **Container queries (v4):** Presence of `@container` or `@sm:`/`@md:` container query variants indicates component-level responsiveness. This is a positive signal — do not flag container query usage as unusual.

### 4.4 Fix Prescriptions — Use Tailwind Classes

When prescribing fixes for a Tailwind site, always use Tailwind utility classes, not raw CSS:

| Instead of | Use |
|-----------|-----|
| `position: absolute; clip: rect(0,0,0,0); width: 1px; height: 1px` | `sr-only` |
| `display: flex; align-items: center; justify-content: center` | `flex items-center justify-center` |
| `font-size: 0.875rem; line-height: 1.25rem` | `text-sm` |
| `padding: 1rem 1.5rem` | `py-4 px-6` |
| `border-radius: 0.5rem` | `rounded-lg` |
| `transition: all 150ms ease-in-out` | `transition-all duration-150 ease-in-out` |
| `@media (min-width: 768px) { display: grid; grid-template-columns: repeat(3, 1fr) }` | `md:grid md:grid-cols-3` |
| `color: hsl(var(--primary))` | `text-primary` (if shadcn detected) |
| Custom focus styles | `focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2` |

**For dark mode fixes:**
- Use `dark:` prefix: `dark:bg-zinc-900 dark:text-zinc-100`
- If shadcn detected, prefer semantic: `bg-background text-foreground` (auto-switches via `.dark` class)

### 4.5 L1 — Cognitive Load (Adjusted for Utility Class Density)

- **Do not count utility classes as visual complexity.** A `<div>` with 15 Tailwind classes is not 15x more complex than one with 1 class — the classes are implementation detail, not perceptual elements. Evaluate L1 cognitive load based on rendered visual output, not markup density.
- **Component extraction signal:** If the same long class string (8+ utilities) appears on multiple elements, this is a code quality issue (should be a component or `@apply`) but not a PFD violation. Note it as a maintenance concern, not a perception concern.

---

## 5. Common Anti-Patterns (Tailwind-Specific)

### 5.1 Mixed Paradigm — Tailwind + Extensive Custom CSS

**Signal:** Tailwind utility classes in HTML coexist with large custom CSS files containing properties that Tailwind covers (custom margin, padding, color, layout rules).

**PFD implication:** Indicates incomplete design system adoption. Two competing systems make token consistency harder to maintain. Check whether the custom CSS contradicts Tailwind's token scale (e.g., custom CSS uses `margin: 15px` while HTML uses `m-4` = 16px). Mixed paradigm is an L2 consistency risk.

**Not a violation when:** Custom CSS handles things Tailwind does not (complex animations, pseudo-element content, print styles, third-party widget overrides).

### 5.2 Arbitrary Values for Existing Scale Values

**Signal:** `p-[16px]` instead of `p-4`, `text-[14px]` instead of `text-sm`, `rounded-[8px]` instead of `rounded-lg`, `bg-[#3b82f6]` instead of `bg-blue-500`.

**PFD implication:** These indicate the developer is thinking in raw CSS values rather than the design system. Each instance is a potential L2 violation because it bypasses the token system that enforces visual consistency. In aggregate, it suggests the project lacks design system discipline.

### 5.3 Incomplete Dark Mode

**Signal:** `dark:` variants present on some elements but missing on others. Common pattern: hero and header have dark mode, but form inputs, cards, or footer do not.

**PFD implication:** Partial dark mode is an L2 coherence violation. The user expects consistency once they see dark mode activate. Elements that don't switch create jarring contrast and break the perceived visual system. Flag as L2 with specific elements that are missing dark mode treatment.

### 5.4 Missing Responsive Breakpoints on Layout Elements

**Signal:** No `sm:`, `md:`, `lg:` prefixes on grid columns, flex direction, or container widths. Site renders at fixed width or overflows on mobile.

**PFD implication:** Foundation (L0) responsive violation. In Tailwind, responsive design is a first-class concern with zero additional tooling required. Missing breakpoints in a Tailwind project is a stronger signal of neglect than in vanilla CSS projects.

### 5.5 Orphaned Hover/Focus States

**Signal:** `hover:` variants present but no corresponding `focus-visible:` variants. Clickable elements have hover effects but no keyboard focus indicators.

**PFD implication:** Foundation accessibility violation. Tailwind makes focus states trivially easy (`focus-visible:ring-2 focus-visible:ring-ring`). Missing focus states in a Tailwind project signal that accessibility was not considered.

### 5.6 Overriding Tailwind with `!important` or Inline Styles

**Signal:** `style="..."` attributes on elements that also have Tailwind classes. Or custom CSS with `!important` overriding Tailwind utilities.

**PFD implication:** Specificity battles indicate design system breakdown. The developer is fighting the framework rather than working within it. Check whether the overrides introduce off-system values.

### 5.7 Excessive Arbitrary Values

**Signal:** More than 15-20% of utility classes use bracket syntax `[...]` across the page.

**PFD implication:** The project is using Tailwind as a CSS-in-HTML engine rather than as a design system. The token system is effectively being bypassed. Evaluate as if no design system is present — apply standard PFD rules without the elevated-severity adjustments from Section 4.1/4.2.

---

## 6. Confidence Scoring

### 6.1 Detection Thresholds

| Condition | Confidence Range | Classification |
|-----------|-----------------|----------------|
| 30+ distinct Tailwind utility classes detected | 90-100 | **Confirmed Tailwind** |
| 10-29 Tailwind utility classes + no competing framework | 70-89 | **Probable Tailwind** |
| <10 Tailwind utility classes | <70 | **Possible Tailwind** — may be post-processed, purged, or a CDN subset |
| Tailwind classes + Bootstrap classes (`col-md-*`, `btn-primary`) | 40-60 | **Migration in progress** — evaluate both systems, flag conflicts |
| Only `--tw-*` CSS vars detected (no utility classes in HTML) | 50-65 | **Tailwind via `@apply` extraction** — utility classes compiled away; tokens still active |

### 6.2 Component Library Confidence Boosts

| Detection | Confidence Adjustment | Final Score |
|-----------|----------------------|-------------|
| shadcn CSS vars (`--radius` + `--primary` + `--background`) + Tailwind classes | **95+** | Confirmed Tailwind + shadcn |
| `data-slot` attributes + shadcn CSS vars | **98+** | Confirmed shadcn/ui v4+ |
| DaisyUI OKLCH vars (`--b1`, `--p`, `--s`) + semantic classes (`.btn`, `.card`) + Tailwind utilities | **90+** | Confirmed Tailwind + DaisyUI |
| `data-theme` attribute on `<html>` + OKLCH vars | **92+** | Confirmed DaisyUI theming |
| `data-headlessui-state` attributes + Tailwind classes | **90+** | Confirmed Tailwind + Headless UI |
| Flowbite `data-modal-target`/`data-dropdown-toggle` attributes + Tailwind classes | **90+** | Confirmed Tailwind + Flowbite |
| Radix `data-state` attributes WITHOUT shadcn CSS vars | **85+** | Confirmed Tailwind + Radix (no shadcn wrapper) |

### 6.3 Version Detection

| Signal | Version Indicator |
|--------|------------------|
| `@tailwind base/components/utilities` in CSS | v3 |
| `--tw-*` prefixed CSS vars (internal) | v3 (or v4 with prefix) |
| `@layer theme { ... }` or `@layer properties { ... }` in CSS | v4 |
| `bg-linear-to-*` class (not `bg-gradient-to-*`) | v4 |
| Dynamic spacing (e.g., `p-13` without brackets) | v4 |
| `@theme` block in CSS | v4 |
| `@import "tailwindcss"` in CSS source | v4 |
| OKLCH color values in theme variables | v4 (or v3 with manual config) |
| Container query variants (`@sm:`, `@md:`) | v4 |

### 6.4 Ambiguous Cases

- **Tailwind + custom utility layer:** Some teams build their own utility classes on top of Tailwind. If class naming follows Tailwind conventions (kebab-case, responsive prefixes) but includes classes not in the Tailwind reference, classify as "Tailwind + custom utilities" and evaluate the custom layer with standard PFD rules.
- **Tailwind CDN (Play CDN / v3 CDN):** CDN usage means all classes are available without purging. Unusually wide class variety may indicate CDN usage rather than a configured build.
- **Tailwind UI (commercial templates):** Tailwind's official premium component library. Detection: high-quality utility composition, often with Headless UI data attributes. Evaluate as high-baseline Tailwind — expect fewer anti-patterns.
