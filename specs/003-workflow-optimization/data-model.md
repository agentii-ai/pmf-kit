# Optimization Metadata Data Model

**Feature**: Workflow Optimization Command
**Version**: v0.0.4
**Created**: 2025-12-04

---

## Overview

This document defines the data schemas for the `/pmfkit.optimize` command's evaluation results, improvement suggestions, optimization history, and validation reports.

---

## Core Entities

### 1. EvaluationResult

Represents the outcome of multi-judge template quality assessment.

```yaml
EvaluationResult:
  id: string                      # Unique evaluation ID (UUID)
  timestamp: datetime             # When evaluation was performed
  target:
    type: enum                    # "template" | "spec" | "plan" | "tasks"
    path: string                  # File path (e.g., ".pmf/templates/spec-template.md")
    version: string               # Template version (e.g., "v0.0.3")
    content_hash: string          # SHA-256 hash of evaluated content

  judges:
    - judge_id: string            # "gpt4o" | "claude35sonnet" | "gemini2pro"
      model: string               # Full model name
      role: enum                  # "strict" | "balanced" | "lenient"
      scores:
        correctness: float        # 0.0-10.0
        coherence: float
        instruction_following: float
        completeness: float
        specificity: float
        clarity: float
        actionability: float
        policy_adherence: float
      overall_score: float        # Weighted aggregate
      evidence:                   # Supporting quotes/reasoning per dimension
        correctness: string
        coherence: string
        # ... other dimensions
      reasoning: string           # Chain-of-thought explanation
      confidence: float           # 0.0-1.0

  aggregated_scores:
    method: enum                  # "bradley_terry" | "elo" | "simple_average"
    correctness: float            # Aggregated across judges
    coherence: float
    instruction_following: float
    completeness: float
    specificity: float
    clarity: float
    actionability: float
    policy_adherence: float
    overall_score: float          # Weighted sum
    weights:                      # Dimension weights
      correctness: 0.25
      coherence: 0.15
      instruction_following: 0.15
      completeness: 0.12
      specificity: 0.10
      clarity: 0.10
      actionability: 0.08
      policy_adherence: 0.05

  reliability_metrics:
    fleiss_kappa: float           # Inter-judge agreement (target: ≥ 0.4)
    pairwise_agreements:          # Judge-to-judge agreement rates
      gpt4o_claude: float
      gpt4o_gemini: float
      claude_gemini: float
    variance: float               # Score variance across judges
    consensus_confidence: float   # 0.0-1.0

  failure_modes:
    - type: enum                  # "AMBIGUOUS_INSTRUCTIONS" | "INSUFFICIENT_CONTEXT" | ...
      dimension: string           # Which dimension failed
      severity: enum              # "minor" | "moderate" | "critical"
      confidence: float           # 0.0-1.0
      evidence: string            # Quote/example showing failure
      description: string         # Human-readable explanation

  metadata:
    duration_seconds: float       # Evaluation time
    cost_usd: float              # API costs
    evaluation_set_size: int      # Number of examples evaluated
```

---

### 2. Suggestion

Represents an actionable improvement recommendation.

```yaml
Suggestion:
  id: string                      # Unique suggestion ID (UUID)
  evaluation_id: string           # Links to source evaluation
  timestamp: datetime

  improvement_aspect: enum        # One of 8 aspects
    # "instruction_clarity" | "context_provision" | "chain_of_thought" |
    # "tool_definitions" | "example_quality" | "constraint_specificity" |
    # "format_specification" | "error_handling"

  root_cause:
    failure_mode: enum            # Source failure from evaluation
    affected_dimensions: [string] # List of impacted dimensions
    diagnosis: string             # Why this failure occurred

  proposed_change:
    section: string               # Template section to modify
    before: string                # Current text (quote)
    after: string                 # Improved version
    diff: string                  # Unified diff format
    rationale: string             # Why this improves quality

  impact_analysis:
    target_dimension: string      # Primary dimension improved
    estimated_improvement: float  # Expected points gained (0.0-10.0)
    dimension_weight: float       # Weight of target dimension
    failure_frequency: int        # How often this failure occurs
    implementation_cost: enum     # "low" (1) | "medium" (2) | "high" (3)
    impact_score: float           # Calculated: (weight × freq) / (1 + cost)

  before_after_examples:          # Concrete demonstrations
    - scenario: string
      before: string
      after: string
      improvement_note: string

  confidence: float               # 0.0-1.0
  priority_rank: int              # Ranking among all suggestions (1 = highest)
```

---

### 3. OptimizationHistory

Tracks the complete optimization process and results.

```yaml
OptimizationHistory:
  id: string                      # Unique optimization ID (UUID)
  target:
    type: enum
    path: string
    baseline_version: string      # e.g., "v0.0.3"
    optimized_version: string     # e.g., "v0.0.4"

  started_at: datetime
  completed_at: datetime
  duration_seconds: float

  pipeline_stages:
    evaluate:
      evaluation_id: string       # Links to EvaluationResult
      baseline_score: float
      completed_at: datetime

    suggest:
      suggestion_count: int
      suggestions: [string]       # List of Suggestion IDs
      top_suggestion_ids: [string] # Top 5-7 by impact
      completed_at: datetime

    improve:
      optimizer: enum             # "miprov2" | "textgrad" | "manual"
      iterations: int
      changes_applied: int
      optimized_content_hash: string
      completed_at: datetime

    validate:
      validation_id: string       # Links to ValidationReport
      passed: bool
      completed_at: datetime

    iterate:
      iteration_count: int
      trajectory: [
        {
          iteration: int
          score_before: float
          score_after: float
          improvement: float
          top_change: string
        }
      ]

  results:
    baseline_score: float
    optimized_score: float
    improvement_absolute: float
    improvement_percentage: float
    statistical_significance: float # p-value
    regressions_detected: int

    dimensional_changes:
      - dimension: string
        before: float
        after: float
        delta: float
        status: enum              # "improved" | "regressed" | "unchanged"

  metadata:
    total_cost_usd: float
    optimizer_config:
      iterations: int
      candidates_per_iteration: int
      # ... other hyperparameters
```

---

### 4. ValidationReport

Documents validation stage results.

```yaml
ValidationReport:
  id: string
  optimization_id: string         # Links to OptimizationHistory
  timestamp: datetime

  test_set:
    type: enum                    # "held_out" | "synthetic" | "user_generated"
    size: int
    split_ratio: float            # e.g., 0.2 for 20% held-out

  comparison:
    baseline_evaluation_id: string
    optimized_evaluation_id: string

    score_comparison:
      baseline: float
      optimized: float
      improvement: float
      improvement_percentage: float

    dimensional_comparison:
      - dimension: string
        baseline: float
        optimized: float
        delta: float
        significant: bool

  statistical_tests:
    paired_ttest:
      statistic: float
      p_value: float              # Target: < 0.05
      significant: bool
      confidence_interval_95: [float, float]

    effect_size:
      cohens_d: float             # Standardized improvement

  regression_analysis:
    critical_regressions: int     # Target: 0
    minor_regressions: int        # Target: ≤ 2
    regressed_dimensions: [string]
    details:
      - dimension: string
        before: float
        after: float
        delta: float
        severity: enum            # "minor" | "critical"

  generalization_check:
    diverse_inputs_tested: int
    performance_stable: bool
    variance: float

  decision:
    approved: bool
    recommendation: enum          # "DEPLOY" | "REFINE" | "REJECT"
    rationale: string

  metadata:
    validator: string             # "automated" | "human" | "hybrid"
    confidence: float
```

---

## Data Flow

```
Template File
    ↓
┌─────────────────┐
│  EVALUATE       │
│  EvaluationResult│ ──────┐
└─────────────────┘       │
    ↓                      │
┌─────────────────┐       │
│  SUGGEST        │       │
│  Suggestion[]   │ ──────┤──> OptimizationHistory
└─────────────────┘       │    (complete record)
    ↓                      │
┌─────────────────┐       │
│  IMPROVE        │       │
│  optimized file │ ──────┤
└─────────────────┘       │
    ↓                      │
┌─────────────────┐       │
│  VALIDATE       │       │
│  ValidationReport│ ──────┘
└─────────────────┘
```

---

## Storage Format

### File Organization

```
specs/003-workflow-optimization/
├── evaluations/
│   ├── eval_20251204_spec-template_v0.0.3.yaml
│   ├── eval_20251204_plan-template_v0.0.3.yaml
│   └── ...
├── suggestions/
│   ├── sugg_20251204_spec-template_001.yaml
│   ├── sugg_20251204_spec-template_002.yaml
│   └── ...
├── optimizations/
│   ├── opt_20251204_spec-template.yaml
│   └── ...
└── validations/
    ├── val_20251204_spec-template.yaml
    └── ...
```

### Serialization

- **Primary format**: YAML (human-readable, version-controllable)
- **Alternative**: JSON (for API responses)
- **Timestamps**: ISO 8601 format (UTC)
- **IDs**: UUID v4
- **Hashes**: SHA-256

---

## Indexes and Relationships

### Primary Keys

- `EvaluationResult.id`
- `Suggestion.id`
- `OptimizationHistory.id`
- `ValidationReport.id`

### Foreign Keys

- `Suggestion.evaluation_id` → `EvaluationResult.id`
- `OptimizationHistory.pipeline_stages.evaluate.evaluation_id` → `EvaluationResult.id`
- `OptimizationHistory.pipeline_stages.suggest.suggestions[]` → `Suggestion.id`
- `OptimizationHistory.pipeline_stages.validate.validation_id` → `ValidationReport.id`
- `ValidationReport.optimization_id` → `OptimizationHistory.id`

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-04 | Initial data model design |
