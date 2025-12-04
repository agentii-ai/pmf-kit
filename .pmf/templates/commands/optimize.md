---
command: pmfkit.optimize
description: Evaluate and improve PMF-Kit templates using multi-judge consensus and state-of-the-art optimization techniques
version: 0.0.4-mvp
---

# /pmfkit.optimize Command

**Status**: MVP Prototype
**Version**: v0.0.4
**Architecture**: 5-stage pipeline (EVALUATE → SUGGEST → IMPROVE → VALIDATE → ITERATE)

---

## Purpose

The `/pmfkit.optimize` command is a meta-optimization system that evaluates and improves PMF-Kit's own templates. Unlike typical optimization tools that improve user-generated content, this command optimizes the toolkit itself - enabling PMF-Kit to self-improve through AI evaluation.

**Key Innovation**: Self-improving infrastructure - PMF-Kit using multi-judge AI evaluation to enhance its own effectiveness, with compounding value for all users.

---

## Usage

```
/pmfkit.optimize <target> [options]
```

### Arguments

- `<target>`: Template or output to optimize
  - File path: `.pmf/templates/spec-template.md`
  - Directory: `.pmf/templates/` (all templates)
  - Keyword: `all` (optimize all PMF-Kit templates)

### Options

- `--mode=<mode>`: Execution mode (default: `full`)
  - `evaluate`: Run evaluation only (no changes)
  - `suggest`: Run evaluation + generate suggestions
  - `improve`: Full pipeline (evaluate → suggest → improve)
  - `full`: Complete workflow with validation

- `--judges=<n>`: Number of LLM judges (default: `3`)
  - Recommended: 3-5 judges for reliability
  - Models: GPT-4o (strict), Claude 3.5 Sonnet (balanced), Gemini 2.0 Pro (lenient)

- `--iterations=<n>`: Optimization iterations (default: `1`)
  - Use 2-3 for iterative refinement
  - Each iteration: evaluate → suggest → improve → validate

- `--output=<path>`: Save results to file (default: stdout)

---

## Workflow

### Stage 1: EVALUATE

**Purpose**: Multi-dimensional quality assessment using LLM judges

**Process**:
1. Load target template/output
2. Run 3 LLM judges in parallel:
   - **GPT-4o**: Strict evaluation (high standards)
   - **Claude 3.5 Sonnet**: Balanced evaluation (practical focus)
   - **Gemini 2.0 Pro**: Lenient evaluation (supportive lens)
3. Score on 8 dimensions:
   - Correctness (25%)
   - Coherence (15%)
   - Instruction-Following (15%)
   - Completeness (12%)
   - Specificity (10%)
   - Clarity (10%)
   - Actionability (8%)
   - Policy-Adherence (5%)
4. Aggregate scores using Bradley-Terry model
5. Calculate Fleiss' kappa for inter-judge reliability

**Output**: Evaluation report with dimensional scores, evidence, and failure modes

**Example**:
```
📊 Evaluation Results: spec-template.md

Overall Score: 7.8 / 10.0 (Strong Quality)
Inter-Judge Agreement (Fleiss' kappa): 0.52 (Moderate)

Dimensional Breakdown:
✅ Correctness: 8.5/10 (2.13 weighted)
✅ Coherence: 8.0/10 (1.20 weighted)
✅ Instruction-Following: 7.5/10 (1.13 weighted)
⚠️  Completeness: 6.8/10 (0.82 weighted) ← Improvement opportunity
✅ Specificity: 7.9/10 (0.79 weighted)
✅ Clarity: 8.2/10 (0.82 weighted)
⚠️  Actionability: 6.5/10 (0.52 weighted) ← Improvement opportunity
✅ Policy-Adherence: 9.0/10 (0.45 weighted)

Failure Modes Detected:
1. INCOMPLETE: Missing examples in JTBD section
2. AMBIGUOUS_INSTRUCTIONS: Vague guidance on success metrics
```

---

### Stage 2: SUGGEST

**Purpose**: Generate ranked, actionable improvement suggestions

**Process**:
1. Analyze evaluation results (dimensional scores + failure modes)
2. Perform root cause analysis:
   - Map failures to 8 improvement aspects (clarity, context, examples, etc.)
   - Identify patterns across dimensions
3. Generate 5-7 specific suggestions using meta-prompting (Claude Sonnet)
4. Rank suggestions by impact score:
   ```
   Impact = (Dimension_Weight × Failure_Frequency) / (1 + Implementation_Cost)
   ```
5. Provide before/after examples for each suggestion

**Output**: Ranked improvement suggestions with rationale and examples

**Example**:
```
💡 Improvement Suggestions (Ranked by Impact)

#1 [Impact: 3.2] Add concrete examples to JTBD section
   Dimension: Completeness (weight: 0.12)
   Before: "Users need systematic evaluation"
   After: "Users need systematic evaluation (e.g., 'Spec completeness: 7/10')"
   Rationale: Abstract concepts → concrete examples improves actionability

#2 [Impact: 2.8] Clarify success metric quantification
   Dimension: Specificity (weight: 0.10)
   Before: "Define clear metrics"
   After: "Define metrics with thresholds (e.g., ≥40% activation, ≥4.2/5 satisfaction)"
   Rationale: Vague "clear" → specific thresholds enables measurement

#3 [Impact: 2.4] Add chain-of-thought prompting for complex decisions
   Dimension: Actionability (weight: 0.08)
   Before: "Decide go/no-go"
   After: "Step 1: Review exit criteria. Step 2: Compare to thresholds. Step 3: Document decision rationale."
   Rationale: Single step → numbered steps improves executability
```

---

### Stage 3: IMPROVE

**Purpose**: Apply optimizations to generate improved template version

**Process**:
1. Load original template + top suggestions
2. Apply improvements systematically:
   - For each suggestion: modify template section
   - Track all changes (before/after diff)
   - Maintain template structure and formatting
3. Generate optimized template version
4. Document all modifications with rationale

**Output**: Optimized template file + change log

**Example**:
```
✨ Optimization Complete: spec-template.md → spec-template-v0.0.4.md

Changes Applied (7 improvements):
1. ✅ Added 3 concrete examples to JTBD section (completeness +1.2)
2. ✅ Specified metric thresholds (5 instances) (specificity +0.9)
3. ✅ Numbered steps in decision gates (4 sections) (actionability +0.8)
4. ✅ Added before/after examples (3 locations) (clarity +0.6)
5. ✅ Clarified constraint specifications (specificity +0.5)
6. ✅ Added glossary of key terms (clarity +0.4)
7. ✅ Improved section transitions (coherence +0.3)

Estimated Quality Improvement: +4.7 points (7.8 → 12.5... capped at 10.0)
Actual Improvement: +1.9 points (7.8 → 9.7) after re-evaluation
```

---

### Stage 4: VALIDATE (Optional)

**Purpose**: Confirm improvements are effective and introduce no regressions

**Process**:
1. Re-evaluate optimized template (same judges, same rubric)
2. Compare baseline vs. optimized scores
3. Statistical significance test (paired t-test)
4. Regression detection (check for score drops)
5. Generalization check (test on diverse examples)

**Output**: Validation report with before/after comparison

**Example**:
```
✓ Validation Passed

Before Optimization:
Overall Score: 7.8/10 (Strong)
Weakest Dimension: Actionability (6.5/10)

After Optimization:
Overall Score: 9.7/10 (Exceptional)
Improvement: +1.9 points (+24.4%)

Dimensional Changes:
📈 Completeness: 6.8 → 9.1 (+2.3) ✓ IMPROVED
📈 Specificity: 7.9 → 9.4 (+1.5) ✓ IMPROVED
📈 Actionability: 6.5 → 8.8 (+2.3) ✓ IMPROVED
→  Correctness: 8.5 → 8.4 (-0.1) ✓ NO REGRESSION

Statistical Significance: p < 0.01 (highly significant)
Regressions Detected: 0 critical, 1 minor (acceptable)

Recommendation: ✅ APPROVE - Deploy optimized template
```

---

### Stage 5: ITERATE (Optional)

**Purpose**: Continuous improvement through repeated optimization cycles

**Process**:
1. Use optimized template as new baseline
2. Re-run EVALUATE → SUGGEST → IMPROVE
3. Track quality trajectory across iterations
4. Stop when: target quality reached OR diminishing returns OR max iterations

**Output**: Optimization trajectory report

**Example**:
```
🔄 Iterative Optimization: spec-template.md (3 iterations)

Iteration 1:
  Start: 7.8/10 → End: 9.7/10 (+1.9)
  Top Fix: Add concrete examples (+2.3 completeness)

Iteration 2:
  Start: 9.7/10 → End: 9.9/10 (+0.2)
  Top Fix: Refine metric thresholds (+0.5 specificity)

Iteration 3:
  Start: 9.9/10 → End: 9.9/10 (+0.0)
  Status: Converged (no significant improvements possible)

Final Result: 9.9/10 (Exceptional Quality)
Total Improvement: +2.1 points over 3 iterations
Time: 15 minutes (vs. 2+ hours manual review)
```

---

## Examples

### Example 1: Evaluate Existing Spec

```bash
# Evaluation only - no changes
/pmfkit.optimize specs/003-workflow-optimization/spec.md --mode=evaluate

# Output: Dimensional scores + failure modes + improvement opportunities
```

### Example 2: Optimize Single Template

```bash
# Full optimization with validation
/pmfkit.optimize .pmf/templates/spec-template.md --mode=full

# Output: Optimized template + validation report + change log
```

### Example 3: Iterative Refinement

```bash
# 3 optimization cycles
/pmfkit.optimize .pmf/templates/plan-template.md --iterations=3 --output=optimization-report.md

# Output: Trajectory report showing quality improvement across iterations
```

### Example 4: Batch Optimization

```bash
# Optimize all PMF-Kit templates
/pmfkit.optimize all --mode=full --judges=5

# Output: Optimized templates for v0.0.4 release + aggregate report
```

---

## Integration with PMF-Kit Workflow

### When to Use `/pmfkit.optimize`

1. **After spec/plan/tasks generation**: Validate quality before implementation
2. **Before releasing templates**: Optimize PMF-Kit package itself (meta-optimization)
3. **When specs feel "off"**: Systematic diagnosis vs. gut feel
4. **Periodic quality audits**: Quarterly review of template effectiveness

### Workflow Integration

```
User runs:          /pmfkit.specify "Add payment feature"
                            ↓
                    specs/feature/spec.md created
                            ↓
User runs:          /pmfkit.optimize specs/feature/spec.md
                            ↓
                    Evaluation: 7.2/10 (Adequate)
                    Suggestions: 5 improvements identified
                            ↓
User chooses:       Apply top 3 suggestions
                            ↓
                    Optimized spec: 9.1/10 (Exceptional)
                            ↓
User continues:     /pmfkit.plan (with higher-quality spec)
```

---

## Success Criteria

### Activation Metrics

- **40%+ of users** run `/pmfkit.optimize` within first 3 workflows
- **85%+ success rate** on first attempt (good UX + error handling)

### Quality Metrics

- **+15-25% improvement** in template quality scores (baseline → optimized)
- **70%+ suggestion acceptance** rate (users apply recommended improvements)
- **4.2+ user satisfaction** with evaluation feedback quality

### Efficiency Metrics

- **60-80% time savings** vs. manual review (2 hours → 20-30 minutes)
- **<30 seconds** evaluation latency (maintain flow state)

---

## Current Limitations (MVP)

This is a prototype demonstration. Production limitations:

1. **No real LLM judge integration**: Uses mock evaluations for demo
2. **No actual template modification**: Generates suggestions but doesn't auto-apply
3. **No statistical validation**: Skips t-test and regression detection
4. **No persistent storage**: Results not saved to database
5. **No UI/dashboard**: Terminal output only

**Roadmap**: Full implementation in v0.0.4 will address all limitations with production-grade evaluation engine, optimization algorithms, and validation pipelines.

---

## Technical Architecture (MVP)

```
Input: Template file path
   ↓
[EVALUATE] Mock multi-judge scoring
   ├─ Load evaluation rubric
   ├─ Generate dimensional scores (simulated)
   ├─ Calculate weighted overall score
   └─ Identify failure modes
   ↓
[SUGGEST] Rule-based suggestion generation
   ├─ Map failures → improvement aspects
   ├─ Generate suggestions (templates)
   ├─ Rank by impact (formula)
   └─ Provide before/after examples
   ↓
[IMPROVE] Template analysis + recommendations
   ├─ Parse template structure
   ├─ Map suggestions to sections
   ├─ Generate change proposals
   └─ Document rationale
   ↓
Output: Evaluation report + suggestions + improvement plan
```

---

## Error Handling

### Invalid Target

```
❌ Error: Template not found: invalid-path.md

Suggestion: Check file path or use one of:
  - .pmf/templates/spec-template.md
  - .pmf/templates/plan-template.md
  - .pmf/templates/tasks-template.md
```

### Evaluation Failure

```
❌ Error: Evaluation failed - insufficient inter-judge agreement (kappa: 0.2)

Suggestion: Re-run with --judges=5 for better reliability
```

### No Improvements Possible

```
✓ Template already optimal (9.8/10)

No significant improvements detected. Template quality is exceptional.
```

---

## Related Commands

- **`/pmfkit.specify`**: Generate PMF specification → then optimize with `/pmfkit.optimize`
- **`/pmfkit.plan`**: Generate implementation plan → then optimize with `/pmfkit.optimize`
- **`/pmfkit.tasks`**: Generate task breakdown → then optimize with `/pmfkit.optimize`
- **`/pmfkit.analyze`**: Cross-artifact consistency check (complements optimization)

---

## References

### Research Foundation

- **refs/7_optimization.md**: Comprehensive research on agent evaluation-suggestion-improvement
- **refs/5_more/pmfkit_optimize_guide.md**: Detailed implementation guide (73KB)
- **refs/5_more/pmfkit_optimize_quick_ref.md**: Quick reference (17KB)
- **refs/5_more/pmfkit_optimize_code_examples.md**: Code examples (32KB)

### Academic Papers

- **G-Eval** (arXiv:2310.05470): Chain-of-thought evaluation pattern
- **MIPROv2** (Opsahl et al. 2024): Bayesian prompt optimization
- **TextGrad** (arXiv:2406.07496): Textual gradient-based optimization
- **TRACE** (arXiv:2510.02837): Multi-faceted trajectory evaluation

---

## Next Steps

After running `/pmfkit.optimize`:

1. **Review evaluation report**: Understand current quality level
2. **Prioritize suggestions**: Focus on high-impact improvements
3. **Apply changes**: Manually implement top 3-5 suggestions
4. **Re-evaluate**: Run optimize again to measure improvement
5. **Iterate**: Repeat until target quality reached

For template optimization (meta-optimization):
1. Collect baseline evaluations from examples/
2. Run optimize on all .pmf/templates/
3. Generate v0.0.4 optimized templates
4. Validate with user testing
5. Package and release

---

**Version**: v0.0.4-mvp
**Last Updated**: 2025-12-04
**Status**: Prototype demonstration - full implementation in progress
