# PFD-S: Spatial Interface Extension (v0.1)

Load this file when applying PFD to canvas tools, spatial interfaces, or any system where users create and navigate content layouts (Figma, Miro, Notion, etc.).

PFD-S extends the 5 core layers with spatial-specific constraints. Apply PFD-S principles IN ADDITION TO R1-R5, not instead of them.

---

## The Five PFD-S Principles

**S1: Depth-Attention Congruence** (extends Foundation)
Rendered information density must match the user's current attentional resolution. At spatial overview scale → landmark info only. At reading scale → full content. Mixing these creates cognitive overload without increasing comprehension.

**S2: Schema-Spatial Alignment** (extends L1)
Spatial container shapes must match the schemas of the content they hold. Cards trigger scan-mode. Documents trigger read-mode. Putting document-length content in card-sized containers activates the wrong cognitive mode — users scan when they should be reading.

**S3: Mode Signal Clarity** (extends L2)
Transitions between cognitive modes (navigation → comprehension → reflection) must be explicitly signaled. Implicit transitions cause disorientation. The signal must be legible at the moment of transition, not after.

**S4: Cognitive Mode Containers** (extends L3)
Each mode (map/navigation, document/comprehension, flow/creation) requires its own perceptual container. Containers cannot be merged, only switched. Attempting to serve multiple cognitive modes with one visual treatment satisfies none.

**S5: Spatial Trust Architecture** (extends L4)
Trust in spatial tools is built through depth access. Surface-only interaction = utility. Deep content access = cognitive partner. The decision architecture must make depth feel rewarding and recoverable, not risky.

---

## Key Spatial Findings (from accumulated learnings)

**Route vs Survey Knowledge** (Learning 12):
Users develop route knowledge before survey knowledge (Siegel & White, 1975). Canvas tools must support both stages:
- New users: route affordances (guided paths, breadcrumbs, landmarks)
- Experienced users: survey affordances (minimap, district overview, configurable views)

S1's "appropriate density" depends on which knowledge stage the user is in — don't assume survey knowledge in new users.

**Bertin's Visual Channels** (Learning 11):
Most canvas tools use 2-3 of Bertin's 7 visual variables (position, size, value, texture, color, orientation, shape). Run a channel audit after deriving R1-R5: which channels carry signal? Which are unused and could carry pre-attentive information?

---

## When to Apply PFD-S

Apply PFD-S when:
- The interface involves spatial navigation (zooming, panning, positioning)
- Users create layouts or arrange content nodes
- Multiple zoom levels reveal different amounts of content
- The user is both consumer and creator of content in the same space
- Cognitive mode switching is part of the core workflow
