# PMF-Kit Optimize Command - MVP Prototype

**Version**: v0.0.4-mvp
**Status**: Demonstration prototype
**Created**: 2025-12-04

---

## Overview

This is a working prototype demonstration of the `/pmfkit.optimize` command - a meta-optimization system that evaluates and improves PMF-Kit templates using multi-judge consensus and state-of-the-art optimization techniques.

**Key Innovation**: Self-improving infrastructure - PMF-Kit using AI evaluation to enhance its own effectiveness.

---

## What's Included

### Research Documentation

1. **evaluation-rubric.md** (11KB)
   - 8-dimensional quality assessment framework
   - Scoring guidelines (1-10 scale)
   - Weight allocation across dimensions
   - Calibration examples for human/LLM judges

2. **g-eval-prompt.md** (15KB)
   - Chain-of-thought evaluation prompt template
   - Judge-specific calibration (GPT-4o strict, Claude balanced, Gemini lenient)
   - Example evaluations with detailed reasoning
   - Integration guidance for evaluation engine

### Prototype Implementation

3. **optimize_mvp.py** (14KB)
   - Working Python prototype demonstrating 5-stage pipeline
   - Mock multi-judge evaluation with dimensional scoring
   - Rule-based suggestion generation
   - Command-line interface

### Command Documentation

4. **/.pmf/templates/commands/optimize.md** (14KB)
   - Complete agent command documentation
   - Usage examples and workflow descriptions
   - Integration with existing PMF-Kit commands
   - Current limitations and roadmap

---

## Architecture

### 5-Stage Pipeline

```
Input: Template file path
   ↓
[EVALUATE] Multi-judge consensus scoring
   ├─ Run 3 LLM judges (GPT-4o, Claude, Gemini)
   ├─ Score on 8 dimensions (correctness, coherence, etc.)
   ├─ Calculate weighted overall score
   └─ Detect failure modes
   ↓
[SUGGEST] Generate improvement recommendations
   ├─ Analyze dimensional weaknesses
   ├─ Map to 8 improvement aspects
   ├─ Rank by impact score
   └─ Provide before/after examples
   ↓
[IMPROVE] Apply optimizations
   ├─ Modify template sections
   ├─ Track all changes
   └─ Generate optimized version
   ↓
[VALIDATE] Confirm improvements
   ├─ Re-evaluate optimized template
   ├─ Statistical significance test
   └─ Regression detection
   ↓
[ITERATE] Repeat until target quality
   └─ Use optimized as new baseline
```

---

## Quick Start

### Installation

```bash
# Navigate to prototype directory
cd specs/003-workflow-optimization/prototype

# No dependencies required (uses Python standard library)
```

### Usage

```bash
# Evaluate existing spec
python3 optimize_mvp.py ../spec.md --mode=evaluate

# Generate suggestions
python3 optimize_mvp.py ../spec.md --mode=suggest

# Full optimization pipeline
python3 optimize_mvp.py ../spec.md --mode=full
```

### Example Output

```
🚀 Starting /pmfkit.optimize
   Target: ../spec.md
   Mode: full

🔍 Evaluating: spec.md
   Running multi-judge consensus...

======================================================================
📊 Evaluation Report: spec.md
======================================================================

 Overall Score: 7.4/10.0 (Adequate)

 Dimensional Breakdown:
  ✅ Correctness              : 7.5/10 (weighted: 1.88)
  ✅ Coherence                : 7.5/10 (weighted: 1.12)
  ⚠️  Instruction-Following    : 7.0/10 (weighted: 1.05)
  ✅ Completeness             : 8.0/10 (weighted: 0.96)
  ✅ Specificity              : 7.8/10 (weighted: 0.78)
  ⚠️  Clarity                  : 6.5/10 (weighted: 0.65)
  ✅ Actionability            : 8.0/10 (weighted: 0.64)
  ⚠️  Policy-Adherence         : 7.0/10 (weighted: 0.35)

 Top 3 Improvement Opportunities:
  1. Clarity: 6.5/10 (needs +3.5)
  2. Instruction-Following: 7.0/10 (needs +3.0)
  3. Policy-Adherence: 7.0/10 (needs +3.0)

💡 Generating improvement suggestions...

======================================================================
💡 Improvement Suggestions (Ranked by Impact)
======================================================================

 #1 [Impact: 3.5] Complex language and jargon
    Dimension: Clarity
    Before: "Current clarity approach"
    After: "Improved clarity approach with specifics"
    Rationale: Improving clarity from 6.5/10 will increase overall quality by ~0.4 points

...
```

---

## MVP Limitations

This is a simplified prototype for demonstration. Production limitations:

1. **Mock Evaluations**: Uses rule-based scoring instead of real LLM judges
2. **No Auto-Apply**: Doesn't modify templates automatically (suggests only)
3. **No Validation**: Skips statistical testing and regression detection
4. **No Persistence**: Results not saved to database
5. **No CLI Integration**: Standalone script (not integrated with `pmf` command)

---

## Full Implementation Plan

See `../tasks.md` for the complete 125-task implementation plan across 5 phases:

- **Phase 0**: Research & Validation (23 tasks, 2 weeks)
- **Phase 1**: Evaluation Engine (24 tasks, 3 weeks)
- **Phase 2**: Suggestion System (20 tasks, 2 weeks)
- **Phase 3**: Optimization Engine (26 tasks, 4 weeks)
- **Phase 4**: CLI Integration & Testing (29 tasks, 3 weeks)

**Total Timeline**: 14 weeks

---

## Key Features Demonstrated

### 1. Multi-Dimensional Evaluation

```python
DIMENSIONS = [
    ("Correctness", 0.25),      # Accuracy and logical validity
    ("Coherence", 0.15),        # Logical flow and organization
    ("Instruction-Following", 0.15),  # Adherence to requirements
    ("Completeness", 0.12),     # Coverage and thoroughness
    ("Specificity", 0.10),      # Concreteness and actionability
    ("Clarity", 0.10),          # Readability and understanding
    ("Actionability", 0.08),    # Ease of translating to actions
    ("Policy-Adherence", 0.05), # PMF-Kit compliance
]
```

### 2. Weighted Scoring

```
Overall Score = Σ (Dimension_Score × Dimension_Weight)

Example:
  Correctness: 7.5 × 0.25 = 1.88
  Coherence: 7.5 × 0.15 = 1.12
  ...
  Total: 7.4/10.0
```

### 3. Impact-Based Ranking

```
Impact = (10 - Current_Score) × Dimension_Weight × 10

Example:
  Clarity: (10 - 6.5) × 0.10 × 10 = 3.5 impact score
  → Highest priority for improvement
```

---

## Integration with PMF-Kit

### Agent Command

The `/pmfkit.optimize` command is now available in Claude Code and other AI agents:

```
/pmfkit.optimize specs/003-workflow-optimization/spec.md
```

See `.pmf/templates/commands/optimize.md` for complete documentation.

### Workflow Example

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
User chooses:       Apply top 3 suggestions manually
                            ↓
User re-runs:       /pmfkit.optimize specs/feature/spec.md
                            ↓
                    Optimized: 9.1/10 (Exceptional)
                            ↓
User continues:     /pmfkit.plan (with higher-quality spec)
```

---

## Research Foundation

This MVP is based on extensive research from:

- **refs/7_optimization.md** (54KB): Comprehensive survey of agent optimization
- **refs/5_more/pmfkit_optimize_guide.md** (73KB): Detailed implementation guide
- **refs/5_more/pmfkit_optimize_quick_ref.md** (17KB): Quick reference
- **refs/5_more/pmfkit_optimize_code_examples.md** (32KB): Code examples

### Key Academic Papers

- **G-Eval** (arXiv:2310.05470): Chain-of-thought evaluation
- **MIPROv2** (Opsahl et al. 2024): Bayesian prompt optimization
- **TextGrad** (arXiv:2406.07496): Textual gradient-based optimization
- **TRACE** (arXiv:2510.02837): Multi-faceted trajectory evaluation
- **Bradley-Terry Model**: Pairwise comparison aggregation

---

## File Structure

```
specs/003-workflow-optimization/
├── spec.md                    # Feature specification
├── plan.md                    # Implementation plan
├── tasks.md                   # Task breakdown (125 tasks)
├── checklists/
│   └── requirements.md        # Quality checklist (PASSED)
├── research/
│   ├── evaluation-rubric.md   # 8-dimensional rubric
│   └── g-eval-prompt.md       # Chain-of-thought prompts
└── prototype/
    ├── README.md              # This file
    └── optimize_mvp.py        # Working prototype

/.pmf/templates/commands/
└── optimize.md                # Agent command documentation
```

---

## Next Steps

### For MVP Testing

1. **Test on Different Templates**:
   ```bash
   python3 optimize_mvp.py ../../spec.md --mode=full
   python3 optimize_mvp.py ../../plan.md --mode=evaluate
   ```

2. **Experiment with Modes**:
   - `evaluate`: Quick quality check
   - `suggest`: Get improvement ideas
   - `full`: Complete optimization workflow

3. **Compare Before/After**:
   - Run on v0.0.3 templates
   - Apply suggested improvements
   - Re-evaluate to measure delta

### For Full Implementation

1. **Phase 0**: Complete research validation
   - Recruit 3 expert PMF practitioners
   - Create 20 template evaluation test cases
   - Validate multi-judge reliability (Fleiss' kappa ≥ 0.4)

2. **Phase 1**: Build evaluation engine
   - Integrate GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Pro
   - Implement G-Eval chain-of-thought pattern
   - Add Bradley-Terry aggregation

3. **Phase 2**: Build suggestion system
   - Implement meta-prompting with Claude Sonnet
   - Add root cause analysis
   - Impact ranking algorithm

4. **Phase 3**: Build optimization engine
   - Integrate MIPROv2 (DSPy)
   - Add TextGrad fallback
   - Validation pipeline with statistical tests

5. **Phase 4**: CLI integration & testing
   - Add to `pmf` command
   - User testing (N=8-10)
   - Package v0.0.4 release

---

## Success Metrics

### Target Outcomes (from spec.md)

- **40%+ activation**: Users run optimize within first 3 workflows
- **+15-25% quality improvement**: Baseline → optimized scores
- **70%+ suggestion acceptance**: Users apply recommendations
- **60-80% time savings**: 2 hours → 20-30 minutes
- **4.2+ satisfaction**: User rating of evaluation quality

---

## Contributing

This is an MVP prototype. To contribute to full implementation:

1. Review `../tasks.md` for task breakdown
2. Pick a phase or specific tasks
3. Follow PMF-Kit constitution (`.specify/memory/constitution.md`)
4. Submit PRs with tests and documentation

---

## License

Same as PMF-Kit parent project.

---

## Version History

- **v0.0.4-mvp** (2025-12-04): Initial prototype demonstration
  - Mock multi-judge evaluation
  - Rule-based suggestions
  - Command-line interface
  - Agent command documentation

---

**Status**: Prototype demonstration - Full implementation in progress
**Questions**: See `../spec.md` for detailed feature specification
