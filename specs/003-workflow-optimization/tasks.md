# PMF-Kit Implementation Tasks: Workflow Optimization Command

**Branch**: `003-workflow-optimization` | **Date**: 2025-12-04 | **Plan**: [plan.md](./plan.md)

**Overview**: Implementation tasks for `/pmfkit.optimize` command - a meta-optimization system that evaluates and improves PMF-Kit's own templates using multi-judge consensus and state-of-the-art optimization techniques. Tasks organized by implementation phase with independent validation checkpoints.

**Target Version**: v0.0.4
**Timeline**: 14 weeks total (2 + 3 + 2 + 4 + 3)
**Architecture**: 5-stage pipeline (EVALUATE → SUGGEST → IMPROVE → VALIDATE → ITERATE)

---

## Phase 0: Research & Validation (2 weeks)

**Objective**: Validate multi-judge evaluation reliability; establish v0.0.3 baseline; design data model and API contracts

**Duration**: 2 weeks | **Owner**: Architecture Lead

**Exit Criteria**: Fleiss' kappa ≥ 0.4 between LLM judges; ≥75% agreement with human experts; baseline scores documented; data model and contracts defined

### Task Group 0.1: Evaluation Framework Validation

- [ ] T001 Recruit 3 expert PMF practitioners for human baseline evaluation
  - Owner: Product Lead
  - Deliverable: 3 experts with PMF-Kit experience confirmed
  - Due: Day 1-2

- [ ] T002 Create 20 template evaluation test cases from examples/ directory
  - Owner: Architecture Lead
  - Input: specs/001-pmf-kit-variant/spec.md, specs/002-automated-template-releases/spec.md outputs
  - Deliverable: specs/003-workflow-optimization/research/evaluation-test-set.md (20 examples)
  - Due: Day 2-3

- [X] T003 Design multi-dimensional evaluation rubric (8-10 dimensions)
  - Owner: Architecture Lead
  - Dimensions: Correctness (25%), Coherence (15%), Instruction-Following (15%), Completeness (12%), Specificity (10%), Clarity (10%), Actionability (8%), Policy-Adherence (5%)
  - Deliverable: specs/003-workflow-optimization/research/evaluation-rubric.md
  - Due: Day 3-4
  - **COMPLETED**: 2025-12-04 - Created comprehensive 8-dimensional rubric with scoring guidelines

- [ ] T004 [P] Run human expert evaluation on 20 test cases (Expert 1)
  - Owner: Expert 1
  - Use rubric from T003
  - Deliverable: specs/003-workflow-optimization/research/human-baseline-expert1.json
  - Due: Day 4-6

- [ ] T005 [P] Run human expert evaluation on 20 test cases (Expert 2)
  - Owner: Expert 2
  - Use rubric from T003
  - Deliverable: specs/003-workflow-optimization/research/human-baseline-expert2.json
  - Due: Day 4-6

- [ ] T006 [P] Run human expert evaluation on 20 test cases (Expert 3)
  - Owner: Expert 3
  - Use rubric from T003
  - Deliverable: specs/003-workflow-optimization/research/human-baseline-expert3.json
  - Due: Day 4-6

- [X] T007 Implement G-Eval chain-of-thought evaluation prompt
  - Owner: Architecture Lead
  - File: specs/003-workflow-optimization/research/g-eval-prompt.md
  - Content: Step-by-step reasoning → dimensional scoring → evidence capture
  - Due: Day 5-6
  - **COMPLETED**: 2025-12-04 - Created G-Eval prompt template with 4-step reasoning process

- [ ] T008 [P] Run GPT-4o judge evaluation on 20 test cases (strict rubric)
  - Owner: Architecture Lead
  - Use G-Eval prompt from T007
  - Deliverable: specs/003-workflow-optimization/research/llm-eval-gpt4o.json
  - Due: Day 6-7

- [ ] T009 [P] Run Claude 3.5 Sonnet judge evaluation on 20 test cases (balanced rubric)
  - Owner: Architecture Lead
  - Use G-Eval prompt from T007
  - Deliverable: specs/003-workflow-optimization/research/llm-eval-claude.json
  - Due: Day 6-7

- [ ] T010 [P] Run Gemini 2.0 Pro judge evaluation on 20 test cases (lenient rubric)
  - Owner: Architecture Lead
  - Use G-Eval prompt from T007
  - Deliverable: specs/003-workflow-optimization/research/llm-eval-gemini.json
  - Due: Day 6-7

- [ ] T011 Calculate Fleiss' kappa for inter-judge agreement (LLM judges)
  - Owner: Architecture Lead
  - Script: specs/003-workflow-optimization/research/calculate-kappa.py
  - Input: T008, T009, T010 results
  - Target: kappa ≥ 0.4
  - Deliverable: specs/003-workflow-optimization/research/inter-judge-reliability.md
  - Due: Day 8

- [ ] T012 Calculate agreement rate with human experts
  - Owner: Architecture Lead
  - Script: specs/003-workflow-optimization/research/human-agreement.py
  - Input: T004-T006 (human) vs T008-T010 (LLM)
  - Target: ≥ 75% agreement
  - Deliverable: specs/003-workflow-optimization/research/human-llm-agreement.md
  - Due: Day 8

- [ ] T013 Phase 0.1 checkpoint: Evaluation framework validation decision
  - Decision: Does multi-judge evaluation meet reliability thresholds?
  - Go: kappa ≥ 0.4 AND human agreement ≥ 75% → proceed to T014
  - Refine: Below thresholds → adjust rubric (T003) and re-run T008-T012
  - No-Go: Unreliable after refinement → explore alternative evaluation approaches
  - Deliverable: specs/003-workflow-optimization/research/evaluation-validation-decision.md
  - Due: Day 9

### Task Group 0.2: Baseline Measurement

- [ ] T014 Evaluate v0.0.3 spec-template.md using examples/ outputs
  - Owner: Architecture Lead
  - Input: .pmf/templates/spec-template.md + examples/001-pmf-kit-variant/
  - Use validated multi-judge evaluation from T013
  - Deliverable: specs/003-workflow-optimization/research/baseline-spec-template.json
  - Due: Day 9-10

- [ ] T015 [P] Evaluate v0.0.3 plan-template.md using examples/ outputs
  - Owner: Architecture Lead
  - Input: .pmf/templates/plan-template.md + examples/002-automated-template-releases/
  - Use validated multi-judge evaluation
  - Deliverable: specs/003-workflow-optimization/research/baseline-plan-template.json
  - Due: Day 9-10

- [ ] T016 [P] Evaluate v0.0.3 tasks-template.md using examples/ outputs
  - Owner: Architecture Lead
  - Input: .pmf/templates/tasks-template.md + examples/
  - Use validated multi-judge evaluation
  - Deliverable: specs/003-workflow-optimization/research/baseline-tasks-template.json
  - Due: Day 9-10

- [ ] T017 [P] Evaluate v0.0.3 command templates (pmfkit.specify, pmfkit.plan, pmfkit.clarify, etc.)
  - Owner: Architecture Lead
  - Input: .pmf/templates/commands/*.md
  - Use validated multi-judge evaluation
  - Deliverable: specs/003-workflow-optimization/research/baseline-commands.json
  - Due: Day 9-10

- [ ] T018 Create baseline quality report for v0.0.3
  - Owner: Architecture Lead
  - Input: T014-T017 results
  - Content: Dimensional scores per template, failure modes identified, improvement opportunities
  - Deliverable: specs/003-workflow-optimization/research/baseline-v0.0.3-report.md
  - Due: Day 10

### Task Group 0.3: Data Model & API Design

- [X] T019 Design optimization metadata schemas
  - Owner: Architecture Lead
  - Schemas: EvaluationResult, Suggestion, OptimizationHistory, ValidationReport
  - File: specs/003-workflow-optimization/data-model.md
  - Due: Day 11-12
  - **COMPLETED**: 2025-12-04 - Created comprehensive data model with all 4 core entities

- [X] T020 Design CLI command interface
  - Owner: Architecture Lead
  - Syntax: `pmf optimize <target> [--mode=evaluate|suggest|improve|full] [--optimizer=miprov2|textgrad]`
  - File: specs/003-workflow-optimization/api-contracts.md (CLI section)
  - Due: Day 12-13
  - **COMPLETED**: 2025-12-04 - Defined complete CLI interface with options and exit codes

- [X] T021 Design agent command interface
  - Owner: Architecture Lead
  - Syntax: `/pmfkit.optimize <target>`
  - File: specs/003-workflow-optimization/api-contracts.md (Agent section)
  - Due: Day 12-13
  - **COMPLETED**: 2025-12-04 - Specified agent workflow and command file integration

- [X] T022 Define optimization pipeline data flow
  - Owner: Architecture Lead
  - Content: Input → EVALUATE → SUGGEST → IMPROVE → Output (with intermediate schemas)
  - File: specs/003-workflow-optimization/api-contracts.md (Data Flow section)
  - Due: Day 13-14
  - **COMPLETED**: 2025-12-04 - Documented all 5 stage contracts with inputs/outputs

### Phase 0 Checkpoint & Decision Gate

- [ ] T023 Phase 0 exit review
  - Decision: Are evaluation framework, baseline, and design complete?
  - Go: All T001-T022 complete; kappa ≥ 0.4; baseline documented; contracts defined → advance to Phase 1
  - Refine: Incomplete or below threshold → extend Phase 0
  - Deliverable: specs/003-workflow-optimization/research/phase0-exit-decision.md
  - Due: End of week 2

---

## Phase 1: Evaluation Engine Implementation (3 weeks)

**Objective**: Build multi-judge consensus evaluation system; implement rubric-based scoring; establish measurement infrastructure

**Duration**: 3 weeks | **Owner**: Evaluation Team

**Exit Criteria**: All v0.0.3 templates evaluated; failure modes identified; evaluation engine production-ready

### Task Group 1.1: Multi-Judge System (Week 1)

- [ ] T024 [P] [US1] Create project structure for optimization system
  - Owner: Evaluation Team
  - Directories: src/evaluation/, src/suggestions/, src/optimization/, src/cli/
  - File: src/__init__.py, src/evaluation/__init__.py
  - Due: Day 1

- [X] T025 [US1] Implement LLM judge interface (abstract base class)
  - Owner: Evaluation Team
  - File: src/evaluation/judge_interface.py
  - Methods: evaluate(prompt, rubric) → JudgeScore
  - Due: Day 1-2
  - **COMPLETED**: 2025-12-04 - Created abstract judge interface with G-Eval support

- [ ] T026 [P] [US1] Implement GPT-4o judge (strict rubric)
  - Owner: Evaluation Team
  - File: src/evaluation/gpt4o_judge.py
  - Extends: JudgeInterface
  - Due: Day 2-3

- [ ] T027 [P] [US1] Implement Claude 3.5 Sonnet judge (balanced rubric)
  - Owner: Evaluation Team
  - File: src/evaluation/claude_judge.py
  - Extends: JudgeInterface
  - Due: Day 2-3

- [ ] T028 [P] [US1] Implement Gemini 2.0 Pro judge (lenient rubric)
  - Owner: Evaluation Team
  - File: src/evaluation/gemini_judge.py
  - Extends: JudgeInterface
  - Due: Day 2-3

- [ ] T029 [US1] Implement G-Eval chain-of-thought evaluation pattern
  - Owner: Evaluation Team
  - File: src/evaluation/g_eval.py
  - Function: format_g_eval_prompt(template, rubric) → prompt with CoT instructions
  - Due: Day 3-4

- [X] T030 [US1] Implement Fleiss' kappa calculation
  - Owner: Evaluation Team
  - File: src/evaluation/reliability.py
  - Function: calculate_fleiss_kappa(judge_scores) → float
  - Due: Day 4
  - **COMPLETED**: 2025-12-04 - Implemented Fleiss kappa with interpretation

- [ ] T031 [US1] Implement position randomization for bias reduction
  - Owner: Evaluation Team
  - File: src/evaluation/bias_mitigation.py
  - Function: randomize_positions(examples) → shuffled_examples
  - Due: Day 4

- [X] T032 [US1] Implement multi-judge consensus aggregation
  - Owner: Evaluation Team
  - File: src/evaluation/consensus.py
  - Function: aggregate_judges(judge_scores, method='bradley-terry') → AggregatedScore
  - Due: Day 5
  - **COMPLETED**: 2025-12-04 - Implemented Bradley-Terry model aggregation

### Task Group 1.2: Rubric Implementation (Week 1-2)

- [ ] T033 [US1] Implement evaluation rubric data model
  - Owner: Evaluation Team
  - File: src/evaluation/rubric.py
  - Classes: Dimension, Rubric
  - Due: Day 5-6

- [ ] T034 [US1] Create default 8-dimensional rubric configuration
  - Owner: Evaluation Team
  - File: configs/default-rubric.yaml
  - Dimensions: Correctness (25%), Coherence (15%), Instruction-Following (15%), Completeness (12%), Specificity (10%), Clarity (10%), Actionability (8%), Policy-Adherence (5%)
  - Due: Day 6

- [ ] T035 [US1] Implement weighted scoring aggregation (Bradley-Terry model)
  - Owner: Evaluation Team
  - File: src/evaluation/bradley_terry.py
  - Function: aggregate_pairwise(judge_scores) → weighted_score
  - Due: Day 6-7

- [ ] T036 [US1] Implement evidence capture for each dimension
  - Owner: Evaluation Team
  - File: src/evaluation/evidence.py
  - Function: extract_evidence(template, dimension_score) → quotes + reasoning
  - Due: Day 7-8

### Task Group 1.3: Trace-Based Evaluation (Week 2)

- [ ] T037 [US1] Implement trajectory analysis for multi-step workflows
  - Owner: Evaluation Team
  - File: src/evaluation/trajectory.py
  - Function: evaluate_trajectory(steps) → TrajectoryScore
  - Assess: observation → thought → action → result validity
  - Due: Day 8-9

- [ ] T038 [US1] Implement efficiency metrics (unnecessary steps detection)
  - Owner: Evaluation Team
  - File: src/evaluation/efficiency.py
  - Function: detect_redundancy(trajectory) → efficiency_score
  - Due: Day 9-10

- [ ] T039 [US1] Implement groundedness check (logical consistency)
  - Owner: Evaluation Team
  - File: src/evaluation/groundedness.py
  - Function: check_groundedness(step, prior_steps) → bool
  - Due: Day 10

### Task Group 1.4: Failure Mode Detection (Week 2-3)

- [X] T040 [US1] Implement failure mode classifier
  - Owner: Evaluation Team
  - File: src/evaluation/failure_modes.py
  - Classes: FailureMode (enum), FailureClassifier
  - Modes: AMBIGUOUS_INSTRUCTIONS, INSUFFICIENT_CONTEXT, FORMAT_VIOLATION, INSTRUCTION_DRIFT, INCOMPLETENESS
  - Due: Day 11-12
  - **COMPLETED**: 2025-12-04 - Implemented comprehensive failure mode classifier with 8 modes

- [X] T041 [US1] Implement LLM-based failure classification
  - Owner: Evaluation Team
  - File: src/evaluation/failure_classifier.py
  - Function: classify_failure(evaluation_result) → FailureMode + confidence
  - Due: Day 12-13
  - **COMPLETED**: 2025-12-04 - Integrated into failure_modes.py with pattern matching

- [X] T042 [US1] Implement root cause diagnosis
  - Owner: Evaluation Team
  - File: src/evaluation/root_cause.py
  - Function: diagnose_root_cause(failure_mode, evidence) → RootCauseAnalysis
  - Due: Day 13-14
  - **COMPLETED**: 2025-12-04 - Implemented root cause analysis with improvement recommendations

### Task Group 1.5: Measurement Infrastructure (Week 3)

- [X] T043 [US1] Implement batch evaluation runner
  - Owner: Evaluation Team
  - File: src/evaluation/batch_runner.py
  - Function: evaluate_batch(templates, examples, judges) → BatchResults
  - Due: Day 14-15
  - **COMPLETED**: 2025-12-04 - Implemented batch runner with result storage

- [X] T044 [US1] Implement evaluation result storage (JSON/YAML)
  - Owner: Evaluation Team
  - File: src/evaluation/storage.py
  - Functions: save_results(), load_results()
  - Due: Day 15
  - **COMPLETED**: 2025-12-04 - Integrated into batch_runner.py (EvaluationStorage class)

- [X] T045 [US1] Create evaluation report generator (markdown output)
  - Owner: Evaluation Team
  - File: src/evaluation/report_generator.py
  - Function: generate_report(results) → markdown_report
  - Due: Day 15-16
  - **COMPLETED**: 2025-12-04 - Implemented comprehensive markdown report generator

- [ ] T046 [US1] Run full baseline evaluation on all v0.0.3 templates
  - Owner: Evaluation Team
  - Input: .pmf/templates/ + examples/
  - Use: Complete evaluation engine (T024-T045)
  - Deliverable: reports/v0.0.3-full-evaluation.md
  - Due: Day 16-17

### Phase 1 Checkpoint & Decision Gate

- [ ] T047 Phase 1 exit review
  - Decision: Is evaluation engine reliable and production-ready?
  - Go: All templates evaluated; kappa ≥ 0.4; failure modes identified; infrastructure handles batch processing → advance to Phase 2
  - Refine: Performance issues or reliability below threshold → optimize and re-test
  - Deliverable: Phase 1 exit decision document
  - Due: End of week 3

---

## Phase 2: Suggestion Generation System (2 weeks)

**Objective**: Build root cause analysis and meta-prompting system for generating actionable improvement suggestions

**Duration**: 2 weeks | **Owner**: Suggestion Team

**Exit Criteria**: Suggestion system generates 5-7 actionable improvements per template; impact ranking correlates with expert judgment (≥70%)

### Task Group 2.1: Root Cause Analysis Engine (Week 1)

- [ ] T048 [US2] Implement improvement aspect mapping (8 aspects)
  - Owner: Suggestion Team
  - File: src/suggestions/aspect_mapping.py
  - Aspects: instruction_clarity, context_provision, chain_of_thought, tool_definitions, example_quality, constraint_specificity, format_specification, error_handling
  - Function: map_failure_to_aspects(failure_mode) → List[ImprovementAspect]
  - Due: Day 1-2

- [ ] T049 [US2] Implement root cause analysis for AMBIGUOUS_INSTRUCTIONS
  - Owner: Suggestion Team
  - File: src/suggestions/root_causes/ambiguous_instructions.py
  - Diagnosis: unclear language → numbered steps, explicit definitions
  - Due: Day 2

- [ ] T050 [P] [US2] Implement root cause analysis for INSUFFICIENT_CONTEXT
  - Owner: Suggestion Team
  - File: src/suggestions/root_causes/insufficient_context.py
  - Diagnosis: missing examples → add 2-3 in-context examples
  - Due: Day 2

- [ ] T051 [P] [US2] Implement root cause analysis for FORMAT_VIOLATION
  - Owner: Suggestion Team
  - File: src/suggestions/root_causes/format_violation.py
  - Diagnosis: unclear output → add schema/examples
  - Due: Day 2

- [ ] T052 [P] [US2] Implement root cause analysis for INSTRUCTION_DRIFT
  - Owner: Suggestion Team
  - File: src/suggestions/root_causes/instruction_drift.py
  - Diagnosis: template ignores constraints → make explicit with examples
  - Due: Day 2

- [ ] T053 [P] [US2] Implement root cause analysis for INCOMPLETENESS
  - Owner: Suggestion Team
  - File: src/suggestions/root_causes/incompleteness.py
  - Diagnosis: missing required sections → add completeness checklist
  - Due: Day 2

- [ ] T054 [US2] Implement root cause aggregator
  - Owner: Suggestion Team
  - File: src/suggestions/root_cause_aggregator.py
  - Function: aggregate_root_causes(evaluation_results) → RootCauseReport
  - Due: Day 3

### Task Group 2.2: Meta-Prompting System (Week 1-2)

- [ ] T055 [US2] Design meta-prompting template for suggestion generation
  - Owner: Suggestion Team
  - File: prompts/meta-prompt-suggestion.md
  - Input: current_template, dimensional_scores, failure_diagnosis, example_failures
  - Output: 5-7 specific suggestions with before/after, impact estimates
  - Due: Day 3-4

- [ ] T056 [US2] Implement Claude Sonnet suggestion generator
  - Owner: Suggestion Team
  - File: src/suggestions/meta_prompter.py
  - Function: generate_suggestions(template, evaluation, root_causes) → List[Suggestion]
  - Use Claude 3.5 Sonnet (best for meta-prompting)
  - Due: Day 4-5

- [ ] T057 [US2] Implement suggestion data model
  - Owner: Suggestion Team
  - File: src/suggestions/suggestion.py
  - Fields: aspect, before, after, impact_estimate, implementation_cost, rationale
  - Due: Day 5

- [ ] T058 [US2] Implement before/after comparison generator
  - Owner: Suggestion Team
  - File: src/suggestions/comparison.py
  - Function: generate_comparison(template, suggestion) → BeforeAfterExample
  - Due: Day 6

### Task Group 2.3: Impact Ranking (Week 2)

- [ ] T059 [US2] Implement impact score calculator
  - Owner: Suggestion Team
  - File: src/suggestions/impact_ranking.py
  - Formula: impact = (dimension_weight × failure_frequency) / (1 + implementation_cost)
  - Due: Day 7-8

- [ ] T060 [US2] Implement suggestion ranker
  - Owner: Suggestion Team
  - File: src/suggestions/ranker.py
  - Function: rank_suggestions(suggestions) → List[RankedSuggestion]
  - Due: Day 8

- [ ] T061 [US2] Generate suggestions for all v0.0.3 templates
  - Owner: Suggestion Team
  - Input: reports/v0.0.3-full-evaluation.md (from T046)
  - Use: Complete suggestion system (T048-T060)
  - Deliverable: reports/v0.0.3-suggestions.md (5-7 suggestions per template)
  - Due: Day 8-9

### Task Group 2.4: Suggestion Validation (Week 2)

- [ ] T062 [US2] Recruit PMF experts for suggestion validation
  - Owner: Product Lead
  - N=3 experts
  - Deliverable: Expert panel confirmed
  - Due: Day 9

- [ ] T063 [P] [US2] Expert validation: spec-template suggestions (Expert 1)
  - Owner: Expert 1
  - Task: Review top-3 suggestions for spec-template.md; rate quality 1-5
  - Deliverable: Expert validation feedback
  - Due: Day 10

- [ ] T064 [P] [US2] Expert validation: plan-template suggestions (Expert 2)
  - Owner: Expert 2
  - Task: Review top-3 suggestions for plan-template.md; rate quality 1-5
  - Deliverable: Expert validation feedback
  - Due: Day 10

- [ ] T065 [P] [US2] Expert validation: tasks-template suggestions (Expert 3)
  - Owner: Expert 3
  - Task: Review top-3 suggestions for tasks-template.md; rate quality 1-5
  - Deliverable: Expert validation feedback
  - Due: Day 10

- [ ] T066 [US2] Analyze expert validation results
  - Owner: Suggestion Team
  - Target: ≥70% agreement with expert ranking
  - Adjust ranking algorithm if needed
  - Deliverable: Expert validation analysis report
  - Due: Day 11

### Phase 2 Checkpoint & Decision Gate

- [ ] T067 Phase 2 exit review
  - Decision: Does suggestion system generate high-quality, actionable improvements?
  - Go: 5-7 suggestions per template; ≥70% expert agreement; suggestions address failure modes → advance to Phase 3
  - Refine: Suggestions too vague or low-quality → improve meta-prompting (T055-T056)
  - Deliverable: Phase 2 exit decision document
  - Due: End of week 2

---

## Phase 3: Optimization Engine Integration (4 weeks)

**Objective**: Integrate MIPROv2 and TextGrad optimizers; build validation pipeline; generate optimized v0.0.4 templates

**Duration**: 4 weeks | **Owner**: Optimization Team

**Exit Criteria**: All templates show ≥15% weighted quality improvement; statistical significance p < 0.05; no critical regressions

### Task Group 3.1: MIPROv2 Integration (Week 1-2)

- [ ] T068 [US3] Install DSPy framework
  - Owner: Optimization Team
  - Command: pip install dspy-ai
  - File: requirements.txt (add dspy-ai>=2.0.0)
  - Due: Day 1

- [ ] T069 [US3] Implement DSPy module interface for template optimization
  - Owner: Optimization Team
  - File: src/optimization/dspy_module.py
  - Class: TemplateOptimizer(dspy.Module)
  - Due: Day 1-2

- [ ] T070 [US3] Configure MIPROv2 optimizer (moderate_search mode)
  - Owner: Optimization Team
  - File: configs/miprov2-config.yaml
  - Settings: iterations=15, candidates_per_iter=4, surrogate_model='tree_parzen_estimator'
  - Due: Day 2

- [ ] T071 [US3] Implement Bayesian surrogate model integration
  - Owner: Optimization Team
  - File: src/optimization/bayesian_search.py
  - Function: optimize_with_bayesian(module, training_data) → OptimizedModule
  - Due: Day 3-4

- [ ] T072 [US3] Implement joint instruction + demo tuning
  - Owner: Optimization Team
  - File: src/optimization/joint_tuning.py
  - Function: tune_instructions_and_examples(template, suggestions) → TunedTemplate
  - Due: Day 4-5

- [ ] T073 [US3] Test MIPROv2 on spec-template.md
  - Owner: Optimization Team
  - Input: .pmf/templates/spec-template.md + reports/v0.0.3-suggestions.md
  - Target: +13-15% improvement
  - Deliverable: Optimized spec-template draft + improvement metrics
  - Due: Day 5-7

### Task Group 3.2: TextGrad Fallback (Week 2)

- [ ] T074 [US3] Install TextGrad framework
  - Owner: Optimization Team
  - Command: pip install textgrad
  - File: requirements.txt (add textgrad>=0.1.0)
  - Due: Day 7

- [ ] T075 [US3] Implement TextGrad optimizer wrapper
  - Owner: Optimization Team
  - File: src/optimization/textgrad_optimizer.py
  - Function: optimize_with_textgrad(template, evaluation_fn) → OptimizedTemplate
  - Configuration: 10-12 iterations, GPT-4o for feedback
  - Due: Day 8-9

- [ ] T076 [US3] Test TextGrad on plan-template.md
  - Owner: Optimization Team
  - Input: .pmf/templates/plan-template.md + reports/v0.0.3-suggestions.md
  - Target: +10-20% improvement
  - Deliverable: Optimized plan-template draft + improvement metrics
  - Due: Day 9-10

### Task Group 3.3: Few-Shot Example Optimization (Week 2-3)

- [ ] T077 [US3] Implement BootstrapFewShot algorithm
  - Owner: Optimization Team
  - File: src/optimization/bootstrap_fewshot.py
  - Steps: 1) Generate outputs, 2) Score, 3) Select top (≥0.7), 4) Diversity sampling, 5) Order simple→complex
  - Due: Day 10-11

- [ ] T078 [US3] Implement example quality scorer
  - Owner: Optimization Team
  - File: src/optimization/example_scorer.py
  - Function: score_example(example, evaluation_engine) → float
  - Due: Day 11

- [ ] T079 [US3] Implement diversity sampling
  - Owner: Optimization Team
  - File: src/optimization/diversity.py
  - Function: select_diverse_examples(candidates, n=4) → List[Example]
  - Due: Day 12

- [ ] T080 [US3] Implement simple-to-complex ordering
  - Owner: Optimization Team
  - File: src/optimization/ordering.py
  - Function: order_by_complexity(examples) → List[Example]
  - Due: Day 12

- [ ] T081 [US3] Optimize few-shot examples for all templates
  - Owner: Optimization Team
  - Input: examples/ directory
  - Target: 3-5 high-quality examples per template
  - Deliverable: Optimized example sets
  - Due: Day 13

### Task Group 3.4: Validation Pipeline (Week 3)

- [ ] T082 [US3] Create held-out test set (20% of examples/)
  - Owner: Optimization Team
  - Split: 80% training, 20% test
  - Deliverable: test_set/ directory with held-out examples
  - Due: Day 14

- [ ] T083 [US3] Implement paired t-test for statistical significance
  - Owner: Optimization Team
  - File: src/optimization/statistical_tests.py
  - Function: paired_ttest(baseline_scores, optimized_scores) → p_value
  - Due: Day 14-15

- [ ] T084 [US3] Implement regression detector
  - Owner: Optimization Team
  - File: src/optimization/regression_detection.py
  - Function: detect_regressions(baseline, optimized, threshold=0.02) → List[Regression]
  - Maximum acceptable: 1-2 regressions
  - Due: Day 15

- [ ] T085 [US3] Implement generalization check
  - Owner: Optimization Team
  - File: src/optimization/generalization.py
  - Function: check_generalization(optimized_template, test_set) → bool
  - Ensure: Performance stable on diverse inputs
  - Due: Day 15-16

- [ ] T086 [US3] Build validation pipeline orchestrator
  - Owner: Optimization Team
  - File: src/optimization/validator.py
  - Function: validate_optimization(baseline, optimized, test_set) → ValidationReport
  - Checks: improvement ≥ 2%, p < 0.05, regressions ≤ 2, generalization OK
  - Due: Day 16-17

### Task Group 3.5: Template Optimization Execution (Week 3-4)

- [ ] T087 [US3] Optimize spec-template.md (full pipeline)
  - Owner: Optimization Team
  - Input: .pmf/templates/spec-template.md + suggestions + training data
  - Pipeline: MIPROv2 → Few-shot optimization → Validation
  - Target: ≥15% improvement, p < 0.05
  - Deliverable: .pmf/templates/spec-template.md (v0.0.4), validation report
  - Due: Day 17-18

- [ ] T088 [US3] Optimize plan-template.md (full pipeline)
  - Owner: Optimization Team
  - Input: .pmf/templates/plan-template.md
  - Pipeline: TextGrad → Few-shot optimization → Validation
  - Target: ≥15% improvement, p < 0.05
  - Deliverable: .pmf/templates/plan-template.md (v0.0.4), validation report
  - Due: Day 18-19

- [ ] T089 [US3] Optimize tasks-template.md (full pipeline)
  - Owner: Optimization Team
  - Input: .pmf/templates/tasks-template.md
  - Pipeline: MIPROv2 → Few-shot optimization → Validation
  - Target: ≥15% improvement, p < 0.05
  - Deliverable: .pmf/templates/tasks-template.md (v0.0.4), validation report
  - Due: Day 19-20

- [ ] T090 [P] [US3] Optimize command templates: specify, plan, tasks, clarify
  - Owner: Optimization Team
  - Input: .pmf/templates/commands/{specify,plan,tasks,clarify}.md
  - Pipeline: MIPROv2 or TextGrad (based on complexity)
  - Deliverable: Optimized command files (v0.0.4)
  - Due: Day 20-21

- [ ] T091 [P] [US3] Optimize command templates: analyze, checklist, constitution, implement
  - Owner: Optimization Team
  - Input: .pmf/templates/commands/{analyze,checklist,constitution,implement}.md
  - Pipeline: MIPROv2 or TextGrad
  - Deliverable: Optimized command files (v0.0.4)
  - Due: Day 20-21

- [ ] T092 [US3] Create comprehensive optimization report
  - Owner: Optimization Team
  - Input: All validation reports (T087-T091)
  - Content: Before/after scores, improvement deltas, statistical significance, change documentation
  - Deliverable: reports/v0.0.4-optimization-report.md
  - Due: Day 22

### Phase 3 Checkpoint & Decision Gate

- [ ] T093 Phase 3 exit review
  - Decision: Are all templates optimized and validated?
  - Go: All templates ≥15% improvement; p < 0.05; no critical regressions → advance to Phase 4
  - Iterate: Improvements < 15% or regressions detected → additional optimization cycles
  - Refine: Optimization algorithm underperforming → consider alternative approaches
  - Deliverable: Phase 3 exit decision document
  - Due: End of week 4

---

## Phase 4: CLI Integration & User Testing (3 weeks)

**Objective**: Integrate optimization command into PMF-Kit CLI; build agent command; conduct user testing; package v0.0.4 release

**Duration**: 3 weeks | **Owner**: Integration Team

**Exit Criteria**: CLI command functional; 34 template variants built; user testing shows ≥10% quality improvement and satisfaction ≥4.2/5

### Task Group 4.1: CLI Command Implementation (Week 1)

- [ ] T094 [US4] Create CLI command entry point
  - Owner: Integration Team
  - File: src/cli/optimize_command.py
  - Function: pmf_optimize(target, mode, optimizer, iterations, validate, output)
  - Due: Day 1-2

- [ ] T095 [US4] Implement --mode flag (evaluate|suggest|improve|full)
  - Owner: Integration Team
  - File: src/cli/modes.py
  - Default: full (run all stages)
  - Due: Day 2

- [ ] T096 [US4] Implement --optimizer flag (miprov2|textgrad)
  - Owner: Integration Team
  - File: src/cli/optimizer_selection.py
  - Default: miprov2
  - Due: Day 2

- [ ] T097 [US4] Implement --iterations flag
  - Owner: Integration Team
  - Default: 15 for MIPROv2, 12 for TextGrad
  - Due: Day 2

- [ ] T098 [US4] Implement --validate flag (run validation stage)
  - Owner: Integration Team
  - Default: false
  - Due: Day 3

- [ ] T099 [US4] Implement --output flag (save results to file)
  - Owner: Integration Team
  - Default: stdout
  - Due: Day 3

- [ ] T100 [US4] Implement progress reporting (stage completion, scores, deltas)
  - Owner: Integration Team
  - File: src/cli/progress.py
  - Output: Real-time progress bars and status updates
  - Due: Day 3-4

- [ ] T101 [US4] Implement error handling with recovery guidance
  - Owner: Integration Team
  - File: src/cli/error_handler.py
  - Content: Clear error messages + suggested fixes
  - Due: Day 4

- [ ] T102 [US4] Test CLI command end-to-end
  - Owner: Integration Team
  - Test: `pmf optimize .pmf/templates/spec-template.md --mode=full --validate`
  - Verify: All stages execute; output correct; errors handled
  - Due: Day 5

### Task Group 4.2: Agent Command Implementation (Week 1)

- [ ] T103 [US4] Create agent command file
  - Owner: Integration Team
  - File: .pmf/templates/commands/optimize.md
  - Frontmatter: `pmfkit.optimize` namespace
  - Due: Day 5

- [ ] T104 [US4] Write agent command instructions
  - Owner: Integration Team
  - File: .pmf/templates/commands/optimize.md (content)
  - Sections: Purpose, Usage, Workflow (5 stages), Output, Examples
  - Due: Day 5-6

- [ ] T105 [US4] Test agent command with Claude Code
  - Owner: Integration Team
  - Test: Run `/pmfkit.optimize .pmf/templates/spec-template.md` in Claude Code
  - Verify: Agent executes workflow; generates markdown report + optimized file
  - Due: Day 6

### Task Group 4.3: Release Packaging (Week 2)

- [ ] T106 [US4] Update release packaging script
  - Owner: Integration Team
  - File: .github/workflows/scripts/create-release-packages.sh
  - Changes: Include optimized v0.0.4 templates, optimization metadata
  - Due: Day 7-8

- [ ] T107 [US4] Build all 34 template variants (18 agents × 2 script types)
  - Owner: Integration Team
  - Command: bash scripts/build-templates.sh v0.0.4
  - Verify: All variants build successfully
  - Deliverable: dist/templates/ (34 ZIP files)
  - Due: Day 8-9

- [ ] T108 [US4] Validate template archives pass quality checks
  - Owner: Integration Team
  - Command: bash scripts/validate-templates.sh dist/templates/
  - Checks: pmfkit.* namespace, required files, no regressions
  - Due: Day 9

- [ ] T109 [US4] Generate CHECKSUMS.sha256
  - Owner: Integration Team
  - Command: cd dist/templates && sha256sum *.zip > CHECKSUMS.sha256
  - Due: Day 9

### Task Group 4.4: User Testing (Week 2-3)

- [ ] T110 [US4] Recruit 8-10 PMF-Kit users for A/B testing
  - Owner: Product Lead
  - Mix: v0.0.2 and v0.0.3 users
  - Deliverable: Test participant roster
  - Due: Day 10

- [ ] T111 [US4] Create user testing protocol
  - Owner: Product Lead
  - Task: Generate spec.md for test feature using assigned template (v0.0.3 or v0.0.4)
  - Measures: Quality scores, time to completion, satisfaction survey
  - Deliverable: User testing guide
  - Due: Day 10

- [ ] T112 [US4] Conduct user testing sessions (Group A: v0.0.3 templates)
  - Owner: Product Lead
  - N=4-5 users
  - Deliverable: User-generated specs + timing + feedback
  - Due: Day 11-13

- [ ] T113 [US4] Conduct user testing sessions (Group B: v0.0.4 templates)
  - Owner: Product Lead
  - N=4-5 users
  - Deliverable: User-generated specs + timing + feedback
  - Due: Day 11-13

- [ ] T114 [US4] Evaluate user-generated artifacts with evaluation engine
  - Owner: Integration Team
  - Input: Specs from T112 and T113
  - Use: Evaluation engine from Phase 1
  - Target: v0.0.4 users ≥10% higher quality
  - Deliverable: Quality comparison report
  - Due: Day 14

- [ ] T115 [US4] Analyze user satisfaction surveys
  - Owner: Product Lead
  - Target: v0.0.4 users satisfaction ≥4.2/5
  - Deliverable: Satisfaction analysis report
  - Due: Day 14

- [ ] T116 [US4] Synthesize user testing results
  - Owner: Product Lead
  - Content: Quality delta, time savings, satisfaction, qualitative feedback
  - Deliverable: reports/user-testing-v0.0.4.md
  - Due: Day 15

### Task Group 4.5: Documentation (Week 3)

- [ ] T117 [P] [US4] Update README.md with /pmfkit.optimize usage
  - Owner: Integration Team
  - Section: "Optimizing PMF-Kit Templates" with CLI examples
  - Due: Day 16

- [ ] T118 [P] [US4] Create optimization usage tutorial
  - Owner: Integration Team
  - File: refs/8_optimization_usage.md
  - Content: Step-by-step guide, examples, troubleshooting
  - Due: Day 16-17

- [ ] T119 [P] [US4] Update CONTRIBUTING.md with optimization workflow
  - Owner: Integration Team
  - Section: How to optimize templates before submitting PRs
  - Due: Day 17

- [ ] T120 [P] [US4] Create troubleshooting guide
  - Owner: Integration Team
  - File: docs/troubleshooting-optimize.md
  - Content: Common issues + solutions
  - Due: Day 17

- [ ] T121 [US4] Prepare v0.0.4 release notes
  - Owner: Product Lead
  - Content: New /pmfkit.optimize command, template improvements, benchmarks
  - File: CHANGELOG.md (v0.0.4 section)
  - Due: Day 18

### Phase 4 Checkpoint & Decision Gate

- [ ] T122 Phase 4 exit review
  - Decision: Is v0.0.4 ready for release?
  - Go: CLI functional; 34 variants built; user testing ≥10% quality + ≥4.2/5 satisfaction; docs complete → release v0.0.4
  - Refine: User feedback indicates issues → iterate on UX or optimization
  - Deliverable: Phase 4 exit decision + release readiness checklist
  - Due: End of week 3

---

## Phase 5: Polish & Release (Final Tasks)

**Objective**: Final polish, release preparation, and v0.0.4 launch

**Duration**: 1-2 days | **Owner**: Release Manager

- [ ] T123 Create v0.0.4 GitHub release
  - Owner: Release Manager
  - Command: gh release create v0.0.4 --title "v0.0.4: Workflow Optimization Command" --notes-file CHANGELOG.md
  - Attach: dist/templates/*.zip, CHECKSUMS.sha256
  - Due: Release day

- [ ] T124 Update installation documentation
  - Owner: Integration Team
  - Files: README.md, docs/installation.md
  - Content: v0.0.4 installation instructions, migration from v0.0.3
  - Due: Release day

- [ ] T125 Announce v0.0.4 release
  - Owner: Product Lead
  - Channels: GitHub Discussions, Twitter/X, communities
  - Content: Release highlights, optimization benchmarks, usage examples
  - Due: Release day + 1

---

## Dependencies & Critical Path

### Phase Dependencies

```
Phase 0 (Research & Validation)
   ↓
Phase 1 (Evaluation Engine) ← MUST complete before Phase 2
   ↓
Phase 2 (Suggestion System) ← MUST complete before Phase 3
   ↓
Phase 3 (Optimization Engine) ← MUST complete before Phase 4
   ↓
Phase 4 (CLI Integration & Testing)
   ↓
Phase 5 (Release)
```

### User Story Dependencies

- **US1 (Evaluation Engine)**: No dependencies; foundational for US2 and US3
- **US2 (Suggestion System)**: Depends on US1 (needs evaluation results)
- **US3 (Optimization Engine)**: Depends on US1 and US2 (needs evaluation + suggestions)
- **US4 (CLI Integration)**: Depends on US1, US2, US3 (needs complete optimization pipeline)

### Parallel Execution Opportunities

**Phase 0**:
- T004-T006 (human evaluations) can run in parallel
- T008-T010 (LLM judge evaluations) can run in parallel

**Phase 1**:
- T026-T028 (judge implementations) can run in parallel
- T050-T053 (root cause analyses) can run in parallel
- T015-T017 (baseline evaluations) can run in parallel

**Phase 2**:
- T049-T053 (root cause implementations) can run in parallel
- T063-T065 (expert validations) can run in parallel

**Phase 3**:
- T090-T091 (command template optimizations) can run in parallel

**Phase 4**:
- T117-T120 (documentation updates) can run in parallel

**Total Duration**: 14 weeks (2 + 3 + 2 + 4 + 3)

---

## Success Metrics Summary

By end of all phases, we will have:

✅ **Evaluation Framework Validated**: Fleiss' kappa ≥ 0.4; ≥75% agreement with human experts

✅ **Baseline Established**: All v0.0.3 templates evaluated with dimensional scores documented

✅ **Suggestions Generated**: 5-7 actionable improvements per template with ≥70% expert validation

✅ **Templates Optimized**: All templates ≥15% quality improvement; p < 0.05; no critical regressions

✅ **CLI Functional**: `/pmfkit.optimize` command working; 34 template variants built

✅ **User Validation**: User testing shows ≥10% quality improvement; satisfaction ≥4.2/5

✅ **v0.0.4 Released**: Complete package with optimized templates and optimization command

---

## Implementation Strategy

**MVP Scope**: Phase 0 + Phase 1 (Research + Evaluation Engine)
- Validates core hypothesis: Can multi-judge evaluation reliably assess template quality?
- Delivers: Baseline evaluation of v0.0.3 with failure mode identification
- Timeline: 5 weeks
- Decision: If evaluation framework unreliable, reconsider optimization approach

**Incremental Delivery**:
1. Phase 0-1 → Evaluation system with baseline
2. Phase 2 → Add suggestion generation
3. Phase 3 → Add optimization and produce v0.0.4 templates
4. Phase 4 → Integrate into CLI and validate with users

**Rollback Strategy**: All v0.0.3 templates preserved; can revert if v0.0.4 shows regressions

---

## Task Count Summary

- **Phase 0**: 23 tasks (Research & Validation)
- **Phase 1**: 24 tasks (Evaluation Engine)
- **Phase 2**: 20 tasks (Suggestion System)
- **Phase 3**: 26 tasks (Optimization Engine)
- **Phase 4**: 29 tasks (CLI Integration & Testing)
- **Phase 5**: 3 tasks (Release)

**Total**: 125 tasks

**Parallel Opportunities**: 42 tasks marked with [P] can execute in parallel within their phase

**User Story Breakdown**:
- US1 (Evaluation): 24 tasks
- US2 (Suggestions): 20 tasks
- US3 (Optimization): 26 tasks
- US4 (Integration): 29 tasks
- Setup/Infrastructure: 26 tasks

**Suggested MVP**: Phase 0-1 (47 tasks, 5 weeks) to validate evaluation framework before committing to full optimization pipeline.
