# API Contracts: Workflow Optimization Command

**Feature**: `/pmfkit.optimize`
**Version**: v0.0.4
**Created**: 2025-12-04

---

## Overview

This document defines the command-line interface, agent command interface, and data flow contracts for the PMF-Kit optimization system.

---

## 1. CLI Command Interface

### Command Syntax

```bash
pmf optimize <target> [OPTIONS]
```

### Arguments

#### `<target>` (Required)

The template or artifact to optimize.

**Valid values:**
- **File path**: `.pmf/templates/spec-template.md`
- **Directory**: `.pmf/templates/` (all templates in directory)
- **Keyword**: `all` (all PMF-Kit templates)
- **Spec output**: `specs/003-workflow-optimization/spec.md`

### Options

#### `--mode=<mode>`

Execution mode controlling which pipeline stages run.

**Values:**
- `evaluate` - Run evaluation only (no changes)
- `suggest` - Run evaluation + generate suggestions (no changes)
- `improve` - Run full pipeline: evaluate → suggest → improve
- `full` - Complete workflow with validation (default)

**Default**: `full`

**Example:**
```bash
pmf optimize .pmf/templates/spec-template.md --mode=evaluate
```

#### `--optimizer=<algorithm>`

Optimization algorithm to use in IMPROVE stage.

**Values:**
- `miprov2` - MIPROv2 Bayesian optimization (default, best results)
- `textgrad` - TextGrad gradient-based optimization (faster, simpler)

**Default**: `miprov2`

**Example:**
```bash
pmf optimize all --optimizer=textgrad
```

#### `--iterations=<n>`

Number of optimization iterations for ITERATE stage.

**Values**: Integer 1-10

**Default**:
- `15` for MIPROv2
- `12` for TextGrad

**Example:**
```bash
pmf optimize .pmf/templates/plan-template.md --iterations=3
```

#### `--validate`

Enable VALIDATE stage (statistical testing and regression detection).

**Values**: Boolean flag (presence = true)

**Default**: `false`

**Example:**
```bash
pmf optimize all --validate
```

#### `--output=<path>`

Save results to file instead of stdout.

**Values**: File path (absolute or relative)

**Default**: stdout

**Example:**
```bash
pmf optimize all --output=optimization-report.md
```

#### `--judges=<n>`

Number of LLM judges for evaluation (more judges = more reliable).

**Values**: Integer 3-5

**Default**: `3`

**Example:**
```bash
pmf optimize specs/feature/spec.md --judges=5
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Success - optimization completed |
| 1 | Error - invalid arguments or target not found |
| 2 | Error - evaluation failed (low inter-judge agreement) |
| 3 | Error - optimization failed (no improvements possible) |
| 4 | Error - validation failed (regressions detected) |
| 5 | Error - API error (LLM provider unavailable) |

### Output Format

#### stdout (Default)

Markdown-formatted report with sections:

1. **Evaluation Results**
   - Overall score
   - Dimensional breakdown
   - Failure modes

2. **Improvement Suggestions**
   - Ranked list (top 5-7)
   - Before/after examples
   - Impact scores

3. **Optimization Results** (if `--mode=improve` or `full`)
   - Changes applied
   - Score improvement
   - Change log

4. **Validation Summary** (if `--validate`)
   - Statistical significance
   - Regressions detected
   - Recommendation

#### File Output (`--output`)

Same markdown format saved to specified file path.

### Examples

#### Example 1: Quick Evaluation

```bash
pmf optimize specs/003-workflow-optimization/spec.md --mode=evaluate
```

**Output:**
```markdown
📊 Evaluation Results: spec.md

Overall Score: 8.2 / 10.0 (Strong Quality)
Inter-Judge Agreement (Fleiss' kappa): 0.48 (Moderate)

Dimensional Breakdown:
✅ Correctness: 8.7/10 (2.18 weighted)
✅ Coherence: 8.3/10 (1.25 weighted)
⚠️  Completeness: 7.1/10 (0.85 weighted) ← Improvement opportunity
...
```

#### Example 2: Full Optimization

```bash
pmf optimize .pmf/templates/spec-template.md --mode=full --validate
```

**Output includes:**
- Evaluation results
- Suggestions
- Optimization changes
- Validation report

#### Example 3: Batch Optimization

```bash
pmf optimize all --output=v0.0.4-optimization-report.md
```

Optimizes all templates and saves comprehensive report.

---

## 2. Agent Command Interface

### Command Syntax

```
/pmfkit.optimize <target> [options]
```

### Usage in AI Agent Context

When invoked by an AI agent (Claude Code, GitHub Copilot, etc.):

```
User: @claude optimize the spec for better clarity
Claude: I'll use /pmfkit.optimize to evaluate and improve the spec.

/pmfkit.optimize specs/003-workflow-optimization/spec.md

[Evaluation results displayed]

Based on the evaluation, I recommend applying these 3 improvements:
1. Add concrete examples to JTBD section (+2.1 completeness)
2. Specify metric thresholds (+1.4 specificity)
3. Number decision steps (+0.9 actionability)

Shall I apply these changes?
```

### Agent Workflow

1. **Agent receives command**: `/pmfkit.optimize <target>`
2. **Agent executes pipeline**:
   - EVALUATE: Run multi-judge scoring
   - SUGGEST: Generate improvements
   - IMPROVE: Modify template (with user confirmation)
3. **Agent reports results**: Markdown output with recommendations
4. **Agent awaits confirmation**: Before applying changes to files

### Agent Command File

Location: `.pmf/templates/commands/optimize.md`

Frontmatter:
```yaml
---
command: pmfkit.optimize
description: Evaluate and improve PMF-Kit templates using multi-judge consensus
version: 0.0.4
---
```

See `.pmf/templates/commands/optimize.md` for full agent instructions.

---

## 3. Data Flow Contracts

### Stage 1: EVALUATE

**Input:**
```yaml
target:
  path: string                    # Template file path
  content: string                 # Template content

config:
  judges: int                     # Number of judges (3-5)
  rubric: RubricConfig            # 8-dimensional rubric
  examples: [string]              # Optional: test examples
```

**Processing:**
1. Load template content
2. Initialize 3-5 LLM judges (GPT-4o, Claude, Gemini)
3. Apply G-Eval chain-of-thought pattern
4. Score on 8 dimensions per judge
5. Aggregate with Bradley-Terry model
6. Calculate Fleiss' kappa
7. Classify failure modes

**Output:**
```yaml
EvaluationResult:
  aggregated_scores:
    overall_score: float          # 0.0-10.0
    dimensional_scores: {string: float}

  reliability_metrics:
    fleiss_kappa: float          # Target: ≥ 0.4

  failure_modes: [FailureMode]
```

**Contracts:**
- MUST return inter-judge agreement ≥ 0.4 (else: error)
- MUST include evidence for each failure mode
- MUST complete within 30 seconds (per template)

---

### Stage 2: SUGGEST

**Input:**
```yaml
evaluation: EvaluationResult
target:
  path: string
  content: string
```

**Processing:**
1. Load evaluation results
2. Map failures to 8 improvement aspects
3. Generate suggestions via meta-prompting (Claude Sonnet)
4. Calculate impact scores: `(weight × freq) / (1 + cost)`
5. Rank by impact
6. Generate before/after examples

**Output:**
```yaml
Suggestions:
  count: int                      # 5-7 suggestions
  ranked: [Suggestion]            # Ordered by impact descending
  top_3: [Suggestion]             # Highest-impact changes
```

**Contracts:**
- MUST return 5-7 actionable suggestions
- MUST include before/after examples for each
- MUST rank by impact score
- Suggestions MUST be specific (not generic "improve clarity")

---

### Stage 3: IMPROVE

**Input:**
```yaml
target:
  path: string
  content: string

suggestions: [Suggestion]         # Top-ranked suggestions

config:
  optimizer: enum                 # "miprov2" | "textgrad"
  iterations: int                 # 1-10
```

**Processing:**
1. Load template + suggestions
2. Run optimizer:
   - **MIPROv2**: Bayesian search over prompt space
   - **TextGrad**: Gradient-based refinement
3. Apply changes to template
4. Track modifications (diff)
5. Re-evaluate optimized version

**Output:**
```yaml
OptimizedTemplate:
  content: string                 # Modified template
  content_hash: string            # SHA-256
  changes: [Change]               # List of modifications
  estimated_improvement: float    # Expected score gain
```

**Contracts:**
- MUST maintain template structure (sections, formatting)
- MUST NOT introduce syntax errors
- MUST track all changes with rationale
- MUST achieve ≥ 2% improvement (else: no-op)

---

### Stage 4: VALIDATE (Optional)

**Input:**
```yaml
baseline: EvaluationResult        # Original template scores
optimized: EvaluationResult       # Improved template scores
test_set: [Example]               # Held-out examples (20%)
```

**Processing:**
1. Re-evaluate both versions on test set
2. Paired t-test for statistical significance
3. Detect regressions (score drops)
4. Check generalization (performance on diverse inputs)

**Output:**
```yaml
ValidationReport:
  comparison:
    improvement: float            # Points gained
    improvement_percentage: float

  statistical_tests:
    p_value: float                # Target: < 0.05
    significant: bool

  regression_analysis:
    critical_regressions: int     # Target: 0
    minor_regressions: int        # Target: ≤ 2

  decision:
    approved: bool
    recommendation: enum          # "DEPLOY" | "REFINE" | "REJECT"
```

**Contracts:**
- MUST use held-out test set (not training data)
- MUST test statistical significance (p < 0.05)
- MUST reject if critical regressions detected
- Maximum acceptable minor regressions: 2

---

### Stage 5: ITERATE (Optional)

**Input:**
```yaml
optimized_template: string
iterations_remaining: int
convergence_threshold: float      # e.g., 0.1 (improvement < 0.1 = converged)
```

**Processing:**
1. Use optimized template as new baseline
2. Re-run EVALUATE → SUGGEST → IMPROVE
3. Track quality trajectory
4. Stop when:
   - Improvement < threshold (converged)
   - Max iterations reached
   - No suggestions possible

**Output:**
```yaml
IterationTrajectory:
  iterations: [
    {
      number: int
      score_before: float
      score_after: float
      improvement: float
      top_change: string
    }
  ]
  final_score: float
  total_improvement: float
  converged: bool
```

**Contracts:**
- MUST stop at convergence (avoid infinite loops)
- MUST respect max iteration limit
- MUST track quality monotonicity (no backwards steps)

---

## 4. Error Handling Contracts

### Invalid Target

**Condition**: Target path does not exist

**Response:**
```
❌ Error: Template not found: invalid-path.md

Suggestion: Check file path or use one of:
  - .pmf/templates/spec-template.md
  - .pmf/templates/plan-template.md
  - .pmf/templates/tasks-template.md

Exit code: 1
```

### Low Inter-Judge Agreement

**Condition**: Fleiss' kappa < 0.4

**Response:**
```
❌ Error: Evaluation failed - insufficient inter-judge agreement (kappa: 0.28)

Suggestion: Re-run with --judges=5 for better reliability

Exit code: 2
```

### No Improvements Possible

**Condition**: Template score ≥ 9.5 OR all suggestions < 0.1 impact

**Response:**
```
✓ Template already optimal (9.7/10)

No significant improvements detected. Template quality is exceptional.

Exit code: 0
```

### Validation Failure

**Condition**: Critical regressions detected

**Response:**
```
❌ Validation Failed: 2 critical regressions detected

Regressed Dimensions:
- Correctness: 8.5 → 7.9 (-0.6) [CRITICAL]
- Policy-Adherence: 9.0 → 8.3 (-0.7) [CRITICAL]

Recommendation: REJECT optimization; review changes manually

Exit code: 4
```

### API Error

**Condition**: LLM provider API unavailable

**Response:**
```
❌ Error: OpenAI API unavailable (HTTP 503)

Suggestion: Check API status or retry with --judges=2 (Claude + Gemini only)

Exit code: 5
```

---

## 5. Performance Contracts

### Latency Targets

| Stage | Target Latency | Max Acceptable |
|-------|----------------|----------------|
| EVALUATE (per template) | < 30s | < 60s |
| SUGGEST | < 10s | < 20s |
| IMPROVE (MIPROv2) | < 5 min | < 10 min |
| IMPROVE (TextGrad) | < 2 min | < 5 min |
| VALIDATE | < 30s | < 60s |

### Cost Targets

| Stage | Estimated Cost (per template) |
|-------|-------------------------------|
| EVALUATE (3 judges) | $0.15 - $0.30 |
| SUGGEST | $0.05 - $0.10 |
| IMPROVE (MIPROv2, 15 iter) | $2.00 - $4.00 |
| IMPROVE (TextGrad, 12 iter) | $0.80 - $1.50 |
| Full pipeline | $3.00 - $6.00 |

### Reliability Targets

- **Evaluation inter-judge agreement**: ≥ 0.4 (Fleiss' kappa)
- **Optimization success rate**: ≥ 80% (meaningful improvement)
- **Validation pass rate**: ≥ 70% (no critical regressions)

---

## 6. Integration Contracts

### With PMF-Kit CLI

The `/pmfkit.optimize` command integrates with existing `pmf` CLI:

```bash
# Existing commands
pmf specify "Add payment feature"      # Generate spec
pmf plan                                # Generate plan
pmf tasks                               # Generate tasks

# New optimization command
pmf optimize specs/feature/spec.md     # Optimize generated spec
```

### With AI Agents

AI agents invoke via slash command:

```
/pmfkit.optimize <target>
```

Agent command file (`.pmf/templates/commands/optimize.md`) provides:
- Command description and purpose
- Usage instructions
- Workflow explanation
- Output format specification
- Error handling guidance

### With Release Packaging

Optimized templates are packaged in v0.0.4 release:

```bash
bash scripts/build-templates.sh v0.0.4
# Includes optimized .pmf/templates/ in all 34 variants
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2025-12-04 | Initial API contracts design |
