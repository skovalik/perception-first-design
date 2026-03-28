# PFD Evaluation Output Schema

> **For Claude Code use, this defines the expected content structure (conversational output).** The evaluation is rendered as structured Markdown following the output format in the Tier 2 prompt template. For future API/Forge deployment, this becomes the strict JSON schema for Claude's structured outputs mode (`output_config.format`), where the Pydantic classes below compile into grammar artifacts that constrain token generation during inference.

---

## Schema Definition (Pydantic-Style)

### Severity

```python
class Severity(str, Enum):
    critical = "critical"   # Blocks the entire layer. Layer capped at 30.
    major = "major"         # Significant perception impact. Degrades the layer score substantially.
    minor = "minor"         # Noticeable but low perception impact. Small score deduction.
```

Severity maps to perception impact, not visual prominence. A 2px border-radius inconsistency is minor (low perception cost). A missing responsive viewport is critical (blocks the entire Foundation layer). A missing CTA above the fold is major (significant L1/L4 degradation). Match severity to how much the violation degrades the user's ability to process, trust, and act.

### Status

```python
class Status(str, Enum):
    pass_ = "pass"       # Layer score >= 70. Core requirements satisfied.
    fail = "fail"        # Layer score 30-69. Significant issues present.
    critical = "critical" # Layer score < 30. Fundamental failures.
```

### Citation

```python
class Citation(BaseModel):
    study: str = Field(
        ...,
        description="Study name and author from the reference material loaded in Slot [4]. "
                    "Must match a citation in the psychology reference corpus. "
                    "Example: 'Cowan 2010 — The Magical Mystery Four'"
    )
    finding: str = Field(
        ...,
        description="The specific finding being cited. Not the full abstract — "
                    "the particular result relevant to this violation. "
                    "Example: 'Working memory holds 3-5 chunks, not Miller's 7+/-2'"
    )
    relevance: str = Field(
        ...,
        description="Why this finding applies to THIS specific violation on THIS site. "
                    "Not a generic restatement of the finding. "
                    "Example: 'This site's 87 interactive elements exceed the 50-element "
                    "threshold derived from Cowan's 4+/-1 chunk capacity'"
    )
```

### Violation

```python
class Violation(BaseModel):
    id: str = Field(
        ...,
        description="Unique violation identifier. Format: V-{layer}-{number}. "
                    "Example: V-F-001 (Foundation violation 1), V-L2-003 (L2 violation 3)"
    )
    rule_id: Optional[str] = Field(
        None,
        description="Heuristic rule ID that detected this violation, if applicable. "
                    "Example: F-CL-001 (Foundation Cognitive Load rule 1). "
                    "Null for violations identified through Tier 2 judgment rather than Tier 1 rules."
    )
    description: str = Field(
        ...,
        description="What the violation is. Specific, observable, tied to HTML/CSS evidence. "
                    "Example: '6 distinct font families detected: Inter, Roboto, Open Sans, "
                    "Montserrat, Lato, and Georgia'"
    )
    severity: Severity
    psychology_mechanism: str = Field(
        ...,
        description="WHY this violation matters perceptually. The cognitive or perceptual "
                    "mechanism being disrupted. Must connect to a citation. "
                    "Example: 'Each additional typeface forces the visual system to build a "
                    "separate decoding schema, reducing processing fluency (Alter & Oppenheimer 2009)'"
    )
    citation: Citation
    fix: str = Field(
        ...,
        description="Design-system-specific fix prescription. Must match the detected framework. "
                    "Example (Tailwind): 'Consolidate to 2 font families in tailwind.config.js — "
                    "fontFamily: { sans: [\"Inter\"], display: [\"Playfair Display\"] }'"
    )
```

### FixPrescription

```python
class FixPrescription(BaseModel):
    description: str = Field(
        ...,
        description="What to fix and how. Specific and actionable — not 'improve the layout' "
                    "but 'reduce above-fold content blocks from 9 to 3 by moving feature grid "
                    "and testimonials below the fold'"
    )
    priority: int = Field(
        ...,
        ge=1,
        le=5,
        description="Priority ranking: 1 = highest (fix first), 5 = lowest (fix last). "
                    "Priority is determined by: dependency unblocking > critical violation removal "
                    "> cross-layer impact > single-layer impact"
    )
    layer: str = Field(
        ...,
        description="Which PFD layer(s) this fix addresses. "
                    "Examples: 'Foundation', 'L1 + L4', 'L2', 'Cross-layer (L1/L2/L3)'"
    )
    design_system_specific: bool = Field(
        ...,
        description="True if the fix prescription uses framework-specific language "
                    "(e.g., Tailwind classes, WordPress hooks, Shopify Liquid). "
                    "False if the fix is framework-agnostic."
    )
    expected_impact: str = Field(
        ...,
        description="Expected score improvement if this fix is implemented. "
                    "Example: 'Foundation +15 (from 35 to ~50), which also unblocks "
                    "L1-L4 dependency caps'"
    )
```

### LayerEvaluation

```python
class LayerEvaluation(BaseModel):
    layer: str = Field(
        ...,
        description="Layer identifier: 'foundation', 'l1_first_impression', "
                    "'l2_processing_fluency', 'l3_perception_bias', 'l4_decision_architecture'"
    )
    score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Layer score after dependency cap enforcement. 0-100 integer. "
                    "Must follow rubric ranges: 90-100 exceptional, 70-89 good, "
                    "50-69 mediocre, 30-49 poor, 10-29 severe, 0-9 absent."
    )
    status: Status = Field(
        ...,
        description="Derived from score: 'pass' if >= 70, 'fail' if 30-69, "
                    "'critical' if < 30"
    )
    reasoning: str = Field(
        ...,
        description="Chain-of-thought reasoning for this score. What was observed, "
                    "what it means for this layer, how the score was determined. "
                    "This is the CoT trace — show your work."
    )
    violations: List[Violation] = Field(
        ...,
        description="All violations found for this layer, ordered by severity "
                    "(critical first, then major, then minor)"
    )
    strengths: List[str] = Field(
        ...,
        description="Specific strengths observed for this layer, with evidence. "
                    "Not filler — genuine positive observations. "
                    "Example: 'Consistent 8px spacing scale across all section paddings'"
    )
    fixes: List[FixPrescription] = Field(
        ...,
        description="Fix prescriptions for this layer's violations, ordered by priority"
    )
```

### PFDEvaluation (Top-Level)

```python
class PFDEvaluation(BaseModel):
    model_version: str = Field(
        ...,
        description="Claude model ID used for this evaluation. "
                    "Example: 'claude-sonnet-4-6-20250929'. "
                    "Enables drift detection across model updates."
    )
    evaluation_timestamp: datetime = Field(
        ...,
        description="ISO 8601 timestamp of when this evaluation was produced. "
                    "Example: '2026-03-21T14:30:00Z'"
    )
    design_system: dict = Field(
        ...,
        description="Design system detection output: "
                    "{ framework: str, component_library: str|null, "
                    "confidence: int (0-100), notes: str }"
    )
    layers: List[LayerEvaluation] = Field(
        ...,
        description="Exactly 5 LayerEvaluation objects in order: "
                    "foundation, l1, l2, l3, l4"
    )
    cross_layer_patterns: List[str] = Field(
        ...,
        description="Issues spanning multiple layers. Experiential self-contradiction "
                    "(Learning #15), cascade effects, multi-layer violations from single "
                    "UI elements (Learning #18). Empty list if none detected."
    )
    overall_score: int = Field(
        ...,
        ge=0,
        le=100,
        description="Weighted average: (Foundation * 1.5 + L1 + L2 + L3 + L4) / 5.5. "
                    "Calculated AFTER dependency cap enforcement. Rounded to nearest integer."
    )
    executive_summary: str = Field(
        ...,
        description="Concise summary of findings. Target ~500 characters maximum. "
                    "Captures the site's core strengths and primary failure mode in 2-3 sentences. "
                    "(Note: max_length enforcement needs empirical testing with structured outputs.)"
    )
    top_fixes: List[FixPrescription] = Field(
        ...,
        description="Top 3 highest-impact fixes across all layers. Ordered by: "
                    "dependency unblocking > critical removal > cross-layer > single-layer"
    )
    dependency_notes: Optional[str] = Field(
        None,
        description="Notes on dependency cap effects. Which caps were applied, "
                    "original vs capped scores, cascade observations. "
                    "Null if no dependency caps were triggered."
    )
```

---

## Field Relationship Summary

```
PFDEvaluation
├── design_system               → Slot [12] detection output
├── layers[5]                   → One per PFD layer (Foundation, L1-L4)
│   ├── violations[]            → Each has severity + psychology + citation + fix
│   ├── strengths[]             → Evidence-based positive observations
│   └── fixes[]                 → Design-system-specific prescriptions
├── cross_layer_patterns[]      → Multi-layer issues (Learnings #15, #18)
├── overall_score               → Weighted formula from constitutional constraints
├── executive_summary           → 2-3 sentence synthesis
├── top_fixes[3]                → Highest-impact across all layers
└── dependency_notes            → Cap enforcement log
```
