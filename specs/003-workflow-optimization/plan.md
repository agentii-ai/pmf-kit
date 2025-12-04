# PMF-Kit Implementation Plan: Workflow Optimization Command

**Feature Branch**: `003-workflow-optimization`
**Created**: 2025-12-04
**Status**: Draft
**Target Version**: v0.0.4

---

## Technical Context *(mandatory)*

### What We're Building

The `/pmfkit.optimize` command is a **meta-optimization system** that evaluates and improves PMF-Kit's own templates, workflows, and prompts. Unlike typical optimization tools that improve user-generated content, this command optimizes the packaged toolkit itself using state-of-the-art agent evaluation and improvement techniques.

**Key Insight**: This is self-improving infrastructure - PMF-Kit using AI evaluation to enhance its own effectiveness.

### Core Architecture Decisions

**Decision 1: Meta-Optimization Target**
- **Target**: PMF-Kit templates in `.pmf/templates/` (spec-template.md, plan-template.md, tasks-template.md, commands/*.md)
- **Baseline**: Historical examples in `examples/` directory showing input/output from v0.0.2-0.0.3
- **Evaluation**: Compare template outputs against quality criteria from `refs/7_optimization.md` research
- **Rationale**: Optimizing the toolkit itself provides compounding value - every user benefits from improved templates

**Decision 2: Evaluation Framework - Multi-Judge Consensus**
- **Architecture**: 3 LLM judges (GPT-4o strict, Claude 3.5 Sonnet balanced, Gemini 2.0 Pro lenient)
- **Aggregation**: Bradley-Terry model for pairwise comparisons (more stable than Elo)
- **Reliability**: Fleiss' kappa ≥ 0.4 for inter-judge agreement
- **Rationale**: Single-judge evaluation is unreliable; multi-judge consensus reduces bias and improves calibration

**Decision 3: Optimization Pipeline - 5-Stage Design**
1. **EVALUATE**: Multi-dimensional quality assessment (8-10 dimensions: correctness, coherence, instruction-following, etc.)
2. **SUGGEST**: Root cause analysis + meta-prompting for improvement ideas
3. **IMPROVE**: MIPROv2 primary optimizer, TextGrad fallback
4. **VALIDATE** (optional): A/B testing on held-out examples
5. **ITERATE** (optional): Continuous monitoring with auto-reoptimization

**Decision 4: Infrastructure Reuse**
- **Constitution**: Shared `.specify/memory/constitution.md` (Principle II: Customer-Evidence-Driven)
- **Namespace**: `/pmfkit.optimize` command (not `/speckit.optimize`)
- **CLI**: `pmf optimize <target>` (integrates with existing `pmf` command)
- **Templates**: All optimizations applied to `.pmf/templates/` before packaging

### Primary Research Questions

**Question 1**: Can automated multi-judge evaluation accurately assess PMF-Kit template quality compared to human expert review?
- Hypothesis: Multi-judge consensus (3+ models) achieves ≥80% agreement with expert human evaluation
- Success threshold: Fleiss' kappa ≥ 0.4 between automated judges; ≥75% agreement with human baseline
- Evidence source: Validate on 20 template evaluation tasks with expert PMF practitioners as ground truth

**Question 2**: Can MIPROv2/TextGrad optimization improve template quality measurably?
- Hypothesis: Optimized templates show +15-25% improvement on quality dimensions vs. v0.0.3 baseline
- Success threshold: ≥15% improvement on weighted quality score; no regressions on critical dimensions
- Evidence source: Before/after comparison using examples/ directory outputs; statistical significance p < 0.05

**Question 3**: Does template optimization translate to better user outcomes?
- Hypothesis: Users of optimized templates (v0.0.4) produce higher-quality specs/plans than v0.0.3 users
- Success threshold: User-generated artifacts score ≥10% higher on evaluation rubric; user satisfaction ≥4.2/5
- Evidence source: A/B test with real PMF-Kit users generating specs with old vs. new templates

### Implementation Phases

Implementation follows PDCA cycles (Plan → Do → Check → Act) with independent validation checkpoints.

**Phase 0 – Research & Design**: Validate evaluation framework; design data model; create API contracts (2 weeks)
**Phase 1 – Evaluation Engine**: Implement multi-judge consensus; build rubric system; baseline measurement (3 weeks)
**Phase 2 – Suggestion System**: Root cause analysis; meta-prompting; impact ranking (2 weeks)
**Phase 3 – Optimization Engine**: Integrate MIPROv2 + TextGrad; validation pipeline (4 weeks)
**Phase 4 – Integration & Testing**: CLI command; template application; user testing (3 weeks)

---

## Constitution Check *(mandatory)*

Verify alignment with PMF-Kit principles (`.specify/memory/constitution.md`):

- [x] **Specification-First** (Principle I): Implementation starts with spec.md defining WHAT we're optimizing (templates) and WHY (compounding value for all users). Clear hypotheses about evaluation accuracy and improvement deltas.

- [x] **Customer-Evidence-Driven** (Principle II): Optimization decisions based on measurable quality improvements using examples/ baseline data. Multi-judge evaluation provides quantified evidence. User A/B testing validates that template improvements translate to better user outcomes.

- [x] **Iterative Validation** (Principle III): 5 implementation phases with independent validation checkpoints. Each phase has go/no-go criteria. Phase 0 validates evaluation framework before building optimization. Optional VALIDATE and ITERATE stages enable continuous improvement.

- [x] **Minimal Viable Process** (Principle IV): Start with manual evaluation (Phase 0: 20 examples with human baseline) before full automation. Use TextGrad (simpler) as fallback if MIPROv2 (complex) doesn't deliver. Qualitative analysis (root cause) before quantitative optimization.

- [x] **Cross-Functional Integration** (Principle V): Optimization affects all PMF-Kit users (product, research, growth teams). Template improvements must consider technical feasibility (.pmf/ architecture), user experience (CLI integration), and business viability (release packaging in v0.0.4).

- [x] **Kit Namespace Isolation** (Principle VI): Command uses `/pmfkit.optimize` prefix (not `/speckit.*`). CLI uses `pmf optimize` (not `specify optimize`). Enables coexistence with other kit variants.

- [x] **Template Extensibility** (Principle VII): Optimization system itself becomes reference implementation. Pattern can be adopted by other kit variants (pd-kit, marketing-kit) to self-improve their templates.

---

## Phase 0: Research & Validation

**Goal**: Validate that multi-judge evaluation can reliably assess template quality; design data model and API contracts

**Duration**: 2 weeks | **Owner**: Architecture Lead

**Research Activities**:
- **Evaluation Framework Validation**: Test multi-judge consensus on 20 template evaluation tasks
  - Recruit 3 expert PMF practitioners for human baseline
  - Run 3 LLM judges (GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Pro) on same tasks
  - Measure inter-judge agreement (Fleiss' kappa) and agreement with human experts
  - Target: kappa ≥ 0.4 between LLMs; ≥75% agreement with humans

- **Baseline Measurement**: Establish v0.0.3 template quality scores
  - Evaluate current templates (spec-template.md, plan-template.md, tasks-template.md) using examples/ outputs
  - Score on 8-10 dimensions (correctness, coherence, instruction-following, completeness, etc.)
  - Document baseline scores as optimization target

- **Data Model Design**: Define optimization metadata structure
  - Evaluation results schema (scores per dimension, evidence, timestamp)
  - Suggestion schema (root cause, improvement idea, impact score, before/after examples)
  - Optimization history schema (baseline, iterations, improvements, validation results)

- **API Contracts**: Define command interface and integration points
  - CLI: `pmf optimize <target>` where target = template file path or "all"
  - Agent: `/pmfkit.optimize <target>` for AI agent invocation
  - Output: Evaluation report (markdown), improved template file, validation summary

**Weekly PDCA**:
- **Week 1 - Do**: Run evaluation validation study; collect human baseline
- **Week 1 - Check**: Is inter-judge agreement ≥0.4? Do judges agree with humans?
- **Week 1 - Act**: Adjust rubric or judge models if needed; refine evaluation dimensions

- **Week 2 - Do**: Design data model; draft API contracts; baseline measurement
- **Week 2 - Check**: Does data model support all 5 stages? Are contracts clear?
- **Week 2 - Act**: Refine schemas based on phase requirements

**Phase 0 Exit Criteria** (Go/No-Go):
- [x] **GO**: Fleiss' kappa ≥ 0.4 between LLM judges; ≥75% agreement with human experts; baseline scores established
- [ ] **REFINE**: Agreement < threshold; need to adjust rubric or evaluation dimensions
- [ ] **NO-GO**: Multi-judge evaluation unreliable even after refinement; consider alternative approaches

**Successful Phase 0 Output**:
- Validated evaluation framework with reliability metrics
- Baseline quality scores for v0.0.3 templates
- Data model specification (schemas/003-optimization-data-model.md)
- API contracts document (contracts/003-optimize-api.md)
- Research findings documenting validation study

**Deliverables**:
1. `research/003-evaluation-validation.md` - Study results with inter-judge agreement analysis
2. `research/003-baseline-scores.md` - v0.0.3 template quality baseline
3. `data-model.md` - Optimization metadata schemas
4. `api-contracts.md` - Command interface and integration specifications

---

## Phase 1: Evaluation Engine Implementation

**Goal**: Build multi-judge consensus evaluation system; implement rubric-based scoring; establish measurement infrastructure

**Duration**: 3 weeks | **Owner**: Evaluation Team

**Implementation Activities**:
- **Multi-Judge System** (Week 1):
  - Implement judge interface for GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Pro
  - Build G-Eval chain-of-thought evaluation pattern (request reasoning before score)
  - Implement Fleiss' kappa calculation for inter-judge agreement
  - Add position randomization to reduce ordering bias

- **Rubric Implementation** (Week 1-2):
  - Build 8-10 dimensional evaluation rubric based on refs/7_optimization.md research
  - Dimensions: Correctness (25%), Coherence (15%), Instruction-Following (15%), Completeness (12%), Specificity (10%), Clarity (10%), Actionability (8%), Policy-Adherence (5%)
  - Implement weighted scoring aggregation (Bradley-Terry model)
  - Add evidence capture for each dimension score (quotes from template showing strength/weakness)

- **Trace-Based Evaluation** (Week 2):
  - For multi-step workflows (spec → plan → tasks), evaluate trajectory coherence
  - Assess each step: observation → thought → action → result validity
  - Measure efficiency (unnecessary steps?) and groundedness (logically consistent?)

- **Failure Mode Detection** (Week 2-3):
  - Build LLM-based classifier for failure categories:
    - Ambiguous instructions (unclear guidance)
    - Insufficient context (missing examples or definitions)
    - Format violations (output doesn't match expected structure)
    - Instruction drift (template ignores constraints)
    - Incompleteness (missing required sections)
  - Output: Root cause diagnosis with confidence scores

- **Measurement Infrastructure** (Week 3):
  - Batch evaluation runner for templates using examples/ baseline data
  - Evaluation result storage (JSON/YAML with timestamps)
  - Visualization dashboard for dimensional scores

**Weekly PDCA**:
- **Week 1 - Do**: Implement multi-judge system; build core rubric
- **Week 1 - Check**: Do judges produce consistent scores? Is kappa ≥ 0.4?
- **Week 1 - Act**: Debug inconsistencies; refine rubric descriptions

- **Week 2 - Do**: Add trace evaluation; build failure classifier
- **Week 2 - Check**: Does failure classification match manual analysis?
- **Week 2 - Act**: Refine failure categories based on examples/ analysis

- **Week 3 - Do**: Build measurement infrastructure; run full baseline evaluation
- **Week 3 - Check**: Can we evaluate all templates reliably? Performance acceptable?
- **Week 3 - Act**: Optimize for speed; add caching for redundant evaluations

**Phase 1 Exit Criteria** (Go/Refine):
- [x] **GO**: Evaluation system produces reliable scores (kappa ≥ 0.4); all v0.0.3 templates evaluated; failure modes identified; infrastructure handles batch processing
- [ ] **REFINE**: Performance issues or reliability below threshold; need optimization

**Successful Phase 1 Output**:
- Functional multi-judge evaluation engine
- Complete evaluation of v0.0.3 templates with dimensional scores
- Failure mode analysis report identifying improvement opportunities
- Measurement infrastructure ready for optimization cycles

**Deliverables**:
1. `src/evaluation/multi_judge.py` - Multi-judge consensus implementation
2. `src/evaluation/rubric.py` - Dimensional rubric scoring
3. `src/evaluation/failure_modes.py` - Failure classification system
4. `reports/v0.0.3-evaluation.md` - Baseline evaluation report with scores and failure analysis

---

## Phase 2: Suggestion Generation System

**Goal**: Build root cause analysis and meta-prompting system for generating actionable improvement suggestions

**Duration**: 2 weeks | **Owner**: Suggestion Team

**Implementation Activities**:
- **Root Cause Analysis Engine** (Week 1):
  - Map evaluation failures to 8 improvement aspects (refs/7_optimization.md):
    1. Instruction clarity (ambiguous language → numbered steps, definitions)
    2. Context provision (missing examples → add 2-3 in-context examples)
    3. Chain-of-thought (complex reasoning → add "think step by step")
    4. Tool definitions (unclear capabilities → document parameters)
    5. Example quality (weak demonstrations → use diverse, high-quality examples)
    6. Constraint specificity (implicit rules → make explicit with examples)
    7. Format specification (unclear output → add schema/examples)
    8. Error handling (no fallbacks → define recovery strategies)

- **Meta-Prompting System** (Week 1-2):
  - Build LLM-based suggestion generator using evaluation results
  - Input: Current template, dimensional scores, failure diagnosis, example failures
  - Output: 5-7 specific suggestions with before/after comparisons, impact estimates
  - Use Claude Sonnet (best for meta-prompting per refs/7_optimization.md)

- **Impact Ranking** (Week 2):
  - Implement impact score formula: `(Dimension_Weight × Failure_Frequency) / (1 + Implementation_Cost)`
  - Rank suggestions by expected improvement value
  - Prioritize high-impact, low-cost improvements first

- **Suggestion Validation** (Week 2):
  - Manual review of top-3 suggestions by PMF experts
  - Adjust ranking algorithm based on expert feedback
  - Ensure suggestions are specific, actionable, and realistic

**Weekly PDCA**:
- **Week 1 - Do**: Build root cause engine; implement meta-prompting
- **Week 1 - Check**: Do suggestions make sense? Are they specific enough?
- **Week 1 - Act**: Refine meta-prompt; add more examples to improve quality

- **Week 2 - Do**: Implement ranking; validate with experts
- **Week 2 - Check**: Do high-ranked suggestions actually address top failures?
- **Week 2 - Act**: Adjust ranking weights based on expert feedback

**Phase 2 Exit Criteria** (Go/Refine):
- [x] **GO**: Suggestion system generates 5-7 actionable improvements per template; impact ranking correlates with expert judgment (≥70%); suggestions address identified failure modes
- [ ] **REFINE**: Suggestions too vague or low-quality; need better meta-prompting

**Successful Phase 2 Output**:
- Root cause analysis engine identifying improvement opportunities
- Meta-prompting system generating specific before/after suggestions
- Impact-ranked suggestion list for each v0.0.3 template
- Expert validation confirming suggestion quality

**Deliverables**:
1. `src/suggestions/root_cause.py` - Failure → improvement mapping
2. `src/suggestions/meta_prompt.py` - LLM-based suggestion generator
3. `src/suggestions/ranking.py` - Impact score calculator
4. `reports/v0.0.3-suggestions.md` - Ranked improvement suggestions for all templates

---

## Phase 3: Optimization Engine Integration

**Goal**: Integrate MIPROv2 and TextGrad optimizers; build validation pipeline; generate optimized v0.0.4 templates

**Duration**: 4 weeks | **Owner**: Optimization Team

**Implementation Activities**:
- **MIPROv2 Integration** (Week 1-2):
  - Integrate DSPy MIPROv2 optimizer (primary optimization method)
  - Configuration: moderate_search mode (15 iterations, 4 candidates per iteration)
  - Joint optimization: Instructions + few-shot examples
  - Bayesian surrogate model (Tree-structured Parzen Estimator) for efficient search
  - Target: +13-15% improvement over baseline per refs/7_optimization.md

- **TextGrad Fallback** (Week 2):
  - Implement TextGrad optimizer as simpler fallback option
  - Use for focused optimizations (1-2 iterations) when MIPROv2 overkill
  - Advantages: Interpretable feedback, fewer evaluations needed
  - Configuration: 10-12 iterations, stronger model (GPT-4o) for feedback generation

- **Few-Shot Example Optimization** (Week 2-3):
  - Implement BootstrapFewShot algorithm:
    1. Generate outputs for ALL training examples (teacher model)
    2. Score each output using evaluation engine
    3. Select top-scoring examples (quality threshold ≥ 0.7)
    4. Apply diversity sampling (avoid similar examples)
    5. Order examples: simple → complex
  - Heuristics: 3-5 examples optimal; quality > quantity

- **Validation Pipeline** (Week 3):
  - Held-out test set evaluation (20% of examples/)
  - Statistical significance testing (paired t-test, p < 0.05)
  - Minimum improvement threshold: 2%
  - Maximum acceptable regressions: 1-2 examples
  - Generalization check: Performance stable on diverse inputs

- **Template Optimization Execution** (Week 3-4):
  - Run optimization on all v0.0.3 templates:
    - spec-template.md
    - plan-template.md
    - tasks-template.md
    - .pmf/templates/commands/*.md (all pmfkit.* commands)
  - Apply top suggestions from Phase 2
  - Validate improvements meet thresholds
  - Document all changes with before/after comparisons

**Weekly PDCA**:
- **Week 1 - Do**: Integrate MIPROv2; test on spec-template.md
- **Week 1 - Check**: Does optimization improve scores? By how much?
- **Week 1 - Act**: Tune search parameters if needed; debug integration issues

- **Week 2 - Do**: Add TextGrad; optimize few-shot examples
- **Week 2 - Check**: Are examples high-quality and diverse?
- **Week 2 - Act**: Adjust selection criteria; refine ordering

- **Week 3 - Do**: Build validation pipeline; run optimizations
- **Week 3 - Check**: Do optimized templates pass validation? Significant improvement?
- **Week 3 - Act**: Iterate on templates failing validation

- **Week 4 - Do**: Complete all template optimizations; document changes
- **Week 4 - Check**: Are all templates improved? No critical regressions?
- **Week 4 - Act**: Final refinements based on validation results

**Phase 3 Exit Criteria** (Go/Iterate):
- [x] **GO**: All templates show ≥15% weighted quality improvement; statistical significance p < 0.05; no critical regressions; validation passed
- [ ] **ITERATE**: Improvements < 15% or regressions detected; need additional optimization cycles
- [ ] **REFINE**: Optimization algorithm underperforming; consider alternative approaches

**Successful Phase 3 Output**:
- Optimized v0.0.4 templates with measurable quality improvements
- Validation report showing before/after comparisons
- Statistical significance confirmation (p < 0.05)
- Comprehensive change documentation with rationale

**Deliverables**:
1. `src/optimization/miprov2.py` - MIPROv2 integration
2. `src/optimization/textgrad.py` - TextGrad fallback
3. `src/optimization/few_shot.py` - Example optimization
4. `src/optimization/validator.py` - Validation pipeline
5. `.pmf/templates/` - Optimized v0.0.4 templates (all files updated)
6. `reports/v0.0.4-optimization.md` - Full optimization report with metrics

---

## Phase 4: CLI Integration & User Testing

**Goal**: Integrate optimization command into PMF-Kit CLI; build agent command; conduct user testing with real PMF practitioners

**Duration**: 3 weeks | **Owner**: Integration Team

**Implementation Activities**:
- **CLI Command Implementation** (Week 1):
  - Command syntax: `pmf optimize <target>` where target = file path or "all"
  - Flags:
    - `--mode=evaluate|suggest|improve|full` (default: full)
    - `--optimizer=miprov2|textgrad` (default: miprov2)
    - `--iterations=N` (default: 15 for MIPROv2, 12 for TextGrad)
    - `--validate` (run validation stage, default: false)
    - `--output=<path>` (save results, default: stdout)
  - Progress reporting: Show stage completion, scores, improvement deltas
  - Error handling: Clear error messages with recovery guidance

- **Agent Command Implementation** (Week 1):
  - Agent syntax: `/pmfkit.optimize <target>` for AI agent invocation
  - Command file: `.pmf/templates/commands/optimize.md`
  - Frontmatter metadata: `pmfkit.optimize` namespace
  - Agent instructions: Evaluate → Suggest → Improve workflow with reasoning
  - Output: Markdown report + updated template file

- **Release Packaging** (Week 2):
  - Update `.github/workflows/scripts/create-release-packages.sh` to include:
    - Optimized v0.0.4 templates
    - Optimization metadata (baseline scores, improvements)
    - Command files for all 18 agents (Claude, Copilot, Gemini, etc.)
  - Build all 34 template variants (18 agents × 2 script types)
  - Validate template archives pass quality checks
  - Generate CHECKSUMS.sha256

- **User Testing** (Week 2-3):
  - Recruit N=8-10 PMF-Kit users (mix of v0.0.2 and v0.0.3 users)
  - A/B test: Half use v0.0.3 templates, half use optimized v0.0.4 templates
  - Task: Generate spec.md for test feature using assigned template
  - Measure:
    - Quality scores of generated specs (using evaluation engine)
    - Time to completion
    - User satisfaction (1-5 scale survey)
    - Qualitative feedback on template improvements
  - Success criteria: v0.0.4 users show ≥10% higher quality; satisfaction ≥4.2/5

- **Documentation** (Week 3):
  - Update README.md with `/pmfkit.optimize` usage examples
  - Create refs/8_optimization_usage.md tutorial
  - Document optimization workflow in CONTRIBUTING.md
  - Add troubleshooting guide for common issues

**Weekly PDCA**:
- **Week 1 - Do**: Implement CLI + agent command
- **Week 1 - Check**: Does command work end-to-end? Clear UX?
- **Week 1 - Act**: Fix bugs; improve error messages

- **Week 2 - Do**: Package release; start user testing
- **Week 2 - Check**: Are templates building correctly? First user feedback?
- **Week 2 - Act**: Address packaging issues; refine based on early feedback

- **Week 3 - Do**: Complete user testing; finalize documentation
- **Week 3 - Check**: Do users see value? Quality improvements confirmed?
- **Week 3 - Act**: Final polish based on user feedback; prepare for release

**Phase 4 Exit Criteria** (Go/Scale):
- [x] **GO**: CLI command functional; all 34 template variants build successfully; user testing shows ≥10% quality improvement and satisfaction ≥4.2/5; documentation complete
- [ ] **REFINE**: User feedback indicates UX issues or quality improvements below threshold; need iteration

**Successful Phase 4 Output**:
- Functional `/pmfkit.optimize` CLI and agent command
- Complete v0.0.4 release package (34 template variants)
- User testing validation confirming improvements translate to better outcomes
- Comprehensive documentation and usage guides

**Deliverables**:
1. `src/cli/optimize_command.py` - CLI implementation
2. `.pmf/templates/commands/optimize.md` - Agent command file
3. `dist/templates/` - v0.0.4 release archives (34 variants)
4. `reports/user-testing-v0.0.4.md` - User testing results
5. `README.md`, `refs/8_optimization_usage.md` - Updated documentation

---

## Validation Checkpoints & Rituals

### Weekly Optimization Review (Every Monday)

**Attendees**: Architecture Lead, Evaluation Team, Suggestion Team, Optimization Team, Integration Team
**Duration**: 30-60 min

**Agenda**:
1. **Metrics**: What quality improvements achieved this week? Any regressions?
2. **Learnings**: What did we discover about evaluation reliability, suggestion quality, or optimization effectiveness?
3. **Blockers**: What's slowing development? Technical debt? Integration issues?
4. **Next week**: Which phase activities are priority? Any dependencies blocking progress?

**Output**: Updated sprint priorities + pivot decisions if quality targets not met

### Phase-End Review (Every 2-4 Weeks)

**Decision**: Does this phase exit criteria pass?
- If **GO** → Advance to next phase
- If **REFINE** → Adjust approach and iterate within current phase
- If **NO-GO** → Reconsider architecture; explore alternative approaches

---

## Success Criteria Summary

| Phase | Success Metric | Go Threshold |
|-------|----------------|--------------|
| 0: Research | Multi-judge inter-agreement (Fleiss' kappa) | ≥ 0.4 |
| 0: Research | Agreement with human experts | ≥ 75% |
| 1: Evaluation | All v0.0.3 templates evaluated | 100% completion |
| 1: Evaluation | Failure modes identified | All templates analyzed |
| 2: Suggestions | Actionable suggestions per template | 5-7 suggestions |
| 2: Suggestions | Expert validation of ranking | ≥ 70% agreement |
| 3: Optimization | Weighted quality improvement | ≥ 15% |
| 3: Optimization | Statistical significance | p < 0.05 |
| 3: Optimization | Critical regressions | 0 regressions |
| 4: Integration | Template build success | 34/34 variants |
| 4: Integration | User quality improvement | ≥ 10% |
| 4: Integration | User satisfaction | ≥ 4.2/5 |

---

## Technical Architecture

### System Components

```
┌─────────────────────────────────────────────────────────────┐
│                    /pmfkit.optimize Command                  │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐   ┌──────────────┐   ┌──────────────┐    │
│  │  EVALUATE    │──>│  SUGGEST     │──>│  IMPROVE     │    │
│  │              │   │              │   │              │    │
│  │ Multi-Judge  │   │ Root Cause   │   │  MIPROv2     │    │
│  │ Consensus    │   │ Analysis     │   │  TextGrad    │    │
│  │              │   │              │   │              │    │
│  │ Rubric       │   │ Meta-Prompt  │   │ Few-Shot     │    │
│  │ Scoring      │   │ Generator    │   │ Bootstrap    │    │
│  │              │   │              │   │              │    │
│  │ Failure      │   │ Impact       │   │ Validation   │    │
│  │ Detection    │   │ Ranking      │   │ Pipeline     │    │
│  └──────────────┘   └──────────────┘   └──────────────┘    │
│         │                   │                   │            │
│         ▼                   ▼                   ▼            │
│  ┌──────────────────────────────────────────────────────┐   │
│  │           Optimization Metadata Store                 │   │
│  │  (Evaluation results, suggestions, history, deltas)   │   │
│  └──────────────────────────────────────────────────────┘   │
│                              │                               │
│                              ▼                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │      Optional: VALIDATE (A/B Test) + ITERATE         │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                   ┌────────────────────┐
                   │  .pmf/templates/   │
                   │  (Optimized v0.0.4)│
                   └────────────────────┘
```

### Data Flow

**Input**: v0.0.3 template file + examples/ baseline data

**Stage 1 - EVALUATE**:
1. Load template and historical outputs from examples/
2. Run 3 LLM judges (GPT-4o, Claude 3.5 Sonnet, Gemini 2.0 Pro)
3. Calculate dimensional scores with weighted aggregation
4. Compute Fleiss' kappa for inter-judge agreement
5. Classify failure modes
6. Store evaluation results

**Stage 2 - SUGGEST**:
1. Load evaluation results
2. Map failures to root causes (8 improvement aspects)
3. Generate suggestions via meta-prompting (Claude Sonnet)
4. Calculate impact scores: `(Weight × Frequency) / (1 + Cost)`
5. Rank suggestions by impact
6. Store suggestion list

**Stage 3 - IMPROVE**:
1. Load template + suggestions
2. Run MIPROv2 optimizer (15 iterations, Bayesian search)
3. Optimize few-shot examples via BootstrapFewShot
4. Validate on held-out test set
5. Statistical significance test (p < 0.05)
6. If improvement ≥ 15% and no regressions → Accept
7. Update template file with optimized version
8. Store optimization history

**Output**: Optimized v0.0.4 template + evaluation report + change summary

### Technology Stack

**LLM Providers**:
- OpenAI GPT-4o (evaluation judge, feedback generation)
- Anthropic Claude 3.5 Sonnet (meta-prompting, suggestion generation)
- Google Gemini 2.0 Pro (evaluation judge)

**Optimization Frameworks**:
- DSPy (MIPROv2 optimizer, few-shot bootstrap)
- TextGrad (fallback optimizer)

**Evaluation Metrics**:
- Fleiss' kappa (inter-rater reliability)
- Bradley-Terry model (pairwise comparison aggregation)
- Paired t-test (statistical significance)

**Infrastructure**:
- Python 3.9+ (implementation language)
- YAML/JSON (data serialization)
- Markdown (reports and documentation)

---

## Risk Mitigation

### Top 5 Implementation Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **Multi-judge evaluation unreliable** (kappa < 0.4) | High | Phase 0 validates reliability before building; adjust rubric or judges if needed; human baseline provides calibration |
| **MIPROv2 optimization insufficient** (< 15% improvement) | High | TextGrad fallback provides alternative; iterative refinement with additional suggestions; manual review and adjustment if needed |
| **Template changes break release packaging** | Medium | Comprehensive validation in Phase 4; all 34 variants built and tested; rollback capability to v0.0.3 templates |
| **User testing shows no perceived benefit** | Medium | A/B test design measures both objective quality and subjective satisfaction; qualitative feedback informs refinement |
| **Optimization introduces regressions** | High | Validation pipeline with held-out test set; statistical testing; maximum 1-2 acceptable regressions; rollback mechanism |

---

## Agent Context Updates

After completing implementation, update the following agent context files to enable AI agents to use the optimization system:

### .pmf/templates/commands/optimize.md

```markdown
---
command: pmfkit.optimize
description: Evaluate and improve PMF-Kit templates using multi-judge consensus and state-of-the-art optimization
---

# /pmfkit.optimize Command

## Purpose
Evaluate PMF-Kit templates, generate improvement suggestions, and apply optimizations using MIPROv2/TextGrad.

## Usage
/pmfkit.optimize <target>

Where <target> is:
- Path to specific template file (e.g., .pmf/templates/spec-template.md)
- "all" to optimize all templates

## Workflow
1. EVALUATE: Multi-judge consensus scoring (GPT-4o, Claude, Gemini)
2. SUGGEST: Root cause analysis + meta-prompting for improvements
3. IMPROVE: Apply MIPROv2 optimization with validation
4. (Optional) VALIDATE: A/B test on held-out examples
5. (Optional) ITERATE: Continuous monitoring and reoptimization

## Output
- Evaluation report (dimensional scores, failure modes)
- Ranked improvement suggestions
- Optimized template file
- Validation summary (before/after comparison)

## Example
/pmfkit.optimize .pmf/templates/spec-template.md

This will evaluate the spec template, suggest improvements, and generate an optimized version.
```

### README.md updates

Add section:

```markdown
## Optimizing PMF-Kit Templates

PMF-Kit v0.0.4+ includes `/pmfkit.optimize` command for self-improvement:

bash
# Optimize specific template
pmf optimize .pmf/templates/spec-template.md

# Optimize all templates
pmf optimize all

# Evaluation only (no changes)
pmf optimize .pmf/templates/spec-template.md --mode=evaluate


See refs/8_optimization_usage.md for detailed tutorial.
```

---

## Next Steps

1. **Confirm Phase 0 research activities** (evaluation validation, baseline measurement, data model design)
2. **Run Phase 0** (2 weeks) → Validate multi-judge reliability and establish baseline
3. **Phase 0 Review** → Decision to proceed to Phase 1 or refine approach
4. **Execute Phases 1-4** (14 weeks total) → Build, optimize, integrate, test
5. **Release v0.0.4** with optimized templates and `/pmfkit.optimize` command
